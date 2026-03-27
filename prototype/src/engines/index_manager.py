# Index Manager for Manufacturing RAG System
import os
from typing import Dict, List, Optional, Any
import pickle
from pathlib import Path

from llama_index.core import VectorStoreIndex, StorageContext, Document, load_index_from_storage
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
import faiss
from .custom_embeddings import CustomSentenceTransformerEmbedding

from ..utils.config import Config

class IndexManager:
    """Manage FAISS vector indices for different document types"""
    
    def __init__(self):
        # Use local sentence transformers for embeddings since Groq doesn't provide them
        try:
            self.embedding = CustomSentenceTransformerEmbedding("all-MiniLM-L6-v2")
            self.use_local_embeddings = True
            print("Using local sentence transformers for embeddings")
        except Exception as e:
            print(f"Failed to load local embeddings: {e}")
            # Fallback to OpenAI embeddings (will require OpenAI key)
            self.embedding = OpenAIEmbedding(
                model=Config.EMBEDDING_MODEL,
                api_key=Config.get_openai_api_key()
            )
            self.use_local_embeddings = False
        self.indices: Dict[str, VectorStoreIndex] = {}
        self.vector_stores: Dict[str, FaissVectorStore] = {}
        
        # Ensure storage directories exist
        Config.create_directories()
        
    def build_index(self, documents: List[Document], doc_type: str, force_rebuild: bool = False) -> VectorStoreIndex:
        """Build and persist a FAISS index for a document type"""
        
        storage_path = f"{Config.STORAGE_DIR}/{doc_type}"
        index_path = f"{storage_path}/index.faiss"
        
        # Check if index already exists
        if os.path.exists(index_path) and not force_rebuild:
            print(f"Loading existing index for {doc_type}")
            return self.load_index(doc_type)
        
        print(f"Building new index for {doc_type} with {len(documents)} documents...")
        
        # Create FAISS index with appropriate dimension
        if self.use_local_embeddings:
            dimension = 384  # MiniLM-L6 dimension
        else:
            dimension = 1536  # OpenAI embedding dimension
        faiss_index = faiss.IndexFlatL2(dimension)
        
        # Create vector store
        vector_store = FaissVectorStore(faiss_index=faiss_index)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        
        # Build index
        index = VectorStoreIndex.from_documents(
            documents,
            storage_context=storage_context,
            embed_model=self.embedding,
            show_progress=True
        )
        
        # Persist index
        os.makedirs(storage_path, exist_ok=True)
        index.storage_context.persist(persist_dir=storage_path)
        
        # Save additional metadata
        metadata = {
            'doc_type': doc_type,
            'num_documents': len(documents),
            'embedding_model': "BAAI/bge-small-en-v1.5",
            'chunk_size': Config.CHUNK_SIZE,
            'build_timestamp': str(pd.Timestamp.now())
        }
        
        with open(f"{storage_path}/metadata.pkl", 'wb') as f:
            pickle.dump(metadata, f)
        
        self.indices[doc_type] = index
        self.vector_stores[doc_type] = vector_store
        
        print(f"Index built and saved for {doc_type}")
        return index
        
    def load_index(self, doc_type: str) -> Optional[VectorStoreIndex]:
        """Load an existing index from disk"""
        storage_path = f"{Config.STORAGE_DIR}/{doc_type}"
        
        if not os.path.exists(f"{storage_path}/index.faiss"):
            print(f"No existing index found for {doc_type}")
            return None
            
        try:
            # Load FAISS index
            faiss_index = faiss.read_index(f"{storage_path}/index.faiss")
            vector_store = FaissVectorStore(faiss_index=faiss_index)
            
            # Recreate storage context
            storage_context = StorageContext.from_defaults(
                vector_store=vector_store,
                persist_dir=storage_path
            )
            
            # Load index
            index = VectorStoreIndex.from_vector_store(
                vector_store=vector_store,
                storage_context=storage_context,
                embed_model=self.embedding
            )
            
            self.indices[doc_type] = index
            self.vector_stores[doc_type] = vector_store
            
            # Load metadata
            metadata_path = f"{storage_path}/metadata.pkl"
            if os.path.exists(metadata_path):
                with open(metadata_path, 'rb') as f:
                    metadata = pickle.load(f)
                    print(f"Loaded {doc_type} index: {metadata.get('num_documents', 'unknown')} documents")
            
            return index
            
        except Exception as e:
            print(f"Error loading index for {doc_type}: {str(e)}")
            return None
            
    def get_index(self, doc_type: str) -> Optional[VectorStoreIndex]:
        """Get index for a document type, loading if necessary"""
        if doc_type in self.indices:
            return self.indices[doc_type]
        else:
            return self.load_index(doc_type)
            
    def delete_index(self, doc_type: str) -> bool:
        """Delete an index and its storage"""
        try:
            storage_path = f"{Config.STORAGE_DIR}/{doc_type}"
            if os.path.exists(storage_path):
                import shutil
                shutil.rmtree(storage_path)
                
            if doc_type in self.indices:
                del self.indices[doc_type]
                
            if doc_type in self.vector_stores:
                del self.vector_stores[doc_type]
                
            print(f"Deleted index for {doc_type}")
            return True
            
        except Exception as e:
            print(f"Error deleting index for {doc_type}: {str(e)}")
            return False
            
    def list_indices(self) -> Dict[str, Dict[str, Any]]:
        """List all available indices with metadata"""
        indices_info = {}
        
        storage_dir = Path(Config.STORAGE_DIR)
        for doc_type_dir in storage_dir.iterdir():
            if doc_type_dir.is_dir():
                doc_type = doc_type_dir.name
                metadata_path = doc_type_dir / "metadata.pkl"
                index_path = doc_type_dir / "index.faiss"
                
                if index_path.exists():
                    info = {
                        'exists': True,
                        'path': str(index_path),
                        'size_mb': round(index_path.stat().st_size / (1024*1024), 2)
                    }
                    
                    # Load metadata if available
                    if metadata_path.exists():
                        try:
                            with open(metadata_path, 'rb') as f:
                                metadata = pickle.load(f)
                                info.update(metadata)
                        except:
                            pass
                            
                    indices_info[doc_type] = info
                    
        return indices_info
        
    def get_index_stats(self, doc_type: str) -> Optional[Dict[str, Any]]:
        """Get statistics about a specific index"""
        index = self.get_index(doc_type)
        if not index:
            return None
            
        try:
            # Get vector store info
            vector_store = self.vector_stores.get(doc_type)
            if vector_store and hasattr(vector_store, 'faiss_index'):
                faiss_index = vector_store.faiss_index
                stats = {
                    'doc_type': doc_type,
                    'vector_count': faiss_index.ntotal,
                    'dimension': faiss_index.d,
                    'index_type': type(faiss_index).__name__,
                    'is_trained': faiss_index.is_trained,
                    'storage_path': f"{Config.STORAGE_DIR}/{doc_type}"
                }
                return stats
                
        except Exception as e:
            print(f"Error getting stats for {doc_type}: {str(e)}")
            
        return None

# Import pandas here to avoid circular imports
try:
    import pandas as pd
except ImportError:
    # Fallback for timestamp without pandas
    from datetime import datetime
    class pd:
        class Timestamp:
            @staticmethod
            def now():
                return datetime.now()