#!/usr/bin/env python3
"""
Simple RAG implementation using Groq + local embeddings
Bypasses complex LlamaIndex embedding integration issues
"""
import os
import sys
import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
import fitz  # PyMuPDF
import faiss
import requests
import time
from openai import OpenAI

# Determine base directory dynamically for Streamlit Cloud compatibility
_THIS_DIR = Path(__file__).parent.resolve()
_BASE_DIR = _THIS_DIR.parent  # Parent of prototype/


class Config:
    """
    Central configuration management.
    Inlined here to avoid import conflicts with Streamlit Cloud mount paths.
    """

    # API Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"

    # Model Configuration
    EMBEDDING_MODEL = "text-embedding-ada-002"  # Still using OpenAI for embeddings
    LLM_MODEL = "llama-3.3-70b-versatile"  # Groq model
    MAX_TOKENS = 2000
    TEMPERATURE = 0.1  # Low temperature for precision

    # Vector Store Configuration
    CHUNK_SIZE = 1024
    CHUNK_OVERLAP = 200
    TOP_K = 5  # Number of chunks to retrieve

    # File Paths - computed dynamically
    BASE_DIR = str(_BASE_DIR)
    DATA_DIR = str(_THIS_DIR / "data" / "pdfs")
    STORAGE_DIR = str(_THIS_DIR / "storage")
    TEMPLATE_DIR = str(_THIS_DIR / "templates")
    OUTPUT_DIR = str(_THIS_DIR / "outputs")

    # Document Types
    DOC_TYPES = {
        "specification": "PDF specifications and guidelines",
        "postmortem": "PowerPoint postmortem reports",
        "engineering_drawing": "Engineering drawing PDFs"
    }

    # Target elements for drawing extraction
    DRAWING_ELEMENTS = [
        'Prebend', 'pre-bend', 'B2B stiffener', 'B2B stiffener_SUS material',
        'B2B stiffener_harness', 'B2B stiffener_finish', 'B2B stiffener_gloss',
        'B2B stiffener_roughness', 'B2B stiffener_adhesive', 'bonding sheet',
        'adhesive', 'liner', 'underfill', 'encapsulation', 'gold plating',
        'switch', 'vestige', 'tab', 'PSA', 'TSA', 'barcode', 'stackup',
        'bending', 'copper layers', 'coverlay', 'UL', 'mic', 'glue'
    ]

    @classmethod
    def get_groq_api_key(cls) -> str:
        """Get Groq API key from environment or Streamlit secrets"""
        if cls.GROQ_API_KEY:
            return cls.GROQ_API_KEY
        try:
            import streamlit as st
            # Try flat key first, then nested
            return st.secrets.get("GROQ_API_KEY", "") or st.secrets.get("groq", {}).get("api_key", "")
        except Exception:
            return ""

    @classmethod
    def get_openai_api_key(cls) -> str:
        """Get OpenAI API key for embeddings (fallback to Groq for now)"""
        return cls.get_groq_api_key()

    @classmethod
    def validate_config(cls) -> Dict[str, bool]:
        """Validate configuration settings"""
        return {
            "groq_api_key": bool(cls.get_groq_api_key()),
            "data_directory": os.path.exists(cls.DATA_DIR),
            "storage_directory": os.path.exists(cls.STORAGE_DIR),
        }

    @classmethod
    def create_directories(cls):
        """Create necessary directories if they don't exist"""
        os.makedirs(cls.STORAGE_DIR, exist_ok=True)
        os.makedirs(cls.TEMPLATE_DIR, exist_ok=True)
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)
        for doc_type in cls.DOC_TYPES.keys():
            os.makedirs(f"{cls.STORAGE_DIR}/{doc_type}", exist_ok=True)

class SimpleRAGSystem:
    """Simple RAG system with Groq LLM and local embeddings"""
    
    HF_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(self):
        # Initialize components
        self.dimension = 384  # all-MiniLM-L6-v2 dimension
        # Try env var first, then Streamlit secrets
        self._hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN") or ""
        if not self._hf_token:
            try:
                import streamlit as st
                self._hf_token = st.secrets.get("HF_TOKEN", "")
            except Exception:
                pass
        
        self.groq_client = OpenAI(
            api_key=Config.get_groq_api_key(),
            base_url=Config.GROQ_BASE_URL
        )
        
        # Storage for documents and embeddings
        self.documents = []
        self.metadata = []
        self.index = None
        
        print(f"Initialized SimpleRAG with embedding dimension: {self.dimension}")

    def _embed(self, texts: List[str]) -> np.ndarray:
        """Get embeddings — local sentence-transformers (fast, no API key needed)"""
        try:
            from sentence_transformers import SentenceTransformer
            if not hasattr(self, '_st_model'):
                self._st_model = SentenceTransformer(self.HF_EMBED_MODEL)
            vecs = self._st_model.encode(texts, batch_size=64, show_progress_bar=False)
            return np.array(vecs, dtype='float32')
        except ImportError:
            pass

        # Fallback: HuggingFace InferenceClient (slower, needs token)
        from huggingface_hub import InferenceClient
        client = InferenceClient(token=self._hf_token or None)
        all_embeddings = []
        batch_size = 32
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            for attempt in range(3):
                try:
                    for text in batch:
                        vec = client.feature_extraction(text, model=self.HF_EMBED_MODEL)
                        all_embeddings.append(vec)
                    break
                except Exception as e:
                    if attempt < 2:
                        time.sleep(2)
                    else:
                        raise RuntimeError(f"HF Embedding API failed: {e}")
        return np.array(all_embeddings, dtype='float32')
    
    def process_pdfs(self, pdf_dir: str) -> None:
        """Process all PDFs and markdown files in a directory (recursively)"""
        print(f"Processing documents from: {pdf_dir}")
        
        base = Path(pdf_dir)
        pdf_files = list(base.glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDF files")
        
        for pdf_file in pdf_files:
            print(f"  Processing: {pdf_file.name}")
            self._process_single_pdf(str(pdf_file))
        
        # Also process markdown files (e.g. extracted PPT content)
        md_dir = base.parent / "ppt_extracted"
        if md_dir.exists():
            md_files = list(md_dir.glob("*.md"))
            print(f"Found {len(md_files)} markdown files (PPT extractions)")
            for md_file in md_files:
                print(f"  Processing: {md_file.name}")
                self._process_single_markdown(str(md_file))
        
        print(f"Total documents processed: {len(self.documents)}")
    
    def _process_single_pdf(self, pdf_path: str) -> None:
        """Process a single PDF file"""
        try:
            doc = fitz.open(pdf_path)
            filename = os.path.basename(pdf_path)
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()
                
                if len(text.strip()) > 100:  # Only process substantial content
                    # Split into chunks
                    chunks = self._chunk_text(text, chunk_size=Config.CHUNK_SIZE, overlap=Config.CHUNK_OVERLAP)
                    
                    for i, chunk in enumerate(chunks):
                        self.documents.append(chunk)
                        self.metadata.append({
                            'source_file': filename,
                            'page_number': page_num + 1,
                            'chunk_index': i,
                            'total_pages': len(doc),
                            'chunk_id': f"{filename}_p{page_num+1}_c{i}"
                        })
            
            doc.close()
            
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")

    def _process_single_markdown(self, md_path: str) -> None:
        """Process a single markdown file (extracted PPT content)"""
        try:
            filename = os.path.basename(md_path)
            text = Path(md_path).read_text(encoding='utf-8')

            # Split by slide headers (## Slide N)
            import re
            sections = re.split(r'(?=^## Slide \d+)', text, flags=re.MULTILINE)

            for sec_idx, section in enumerate(sections):
                if len(section.strip()) < 50:
                    continue
                # Chunk each section
                chunks = self._chunk_text(section, chunk_size=Config.CHUNK_SIZE, overlap=Config.CHUNK_OVERLAP)
                for i, chunk in enumerate(chunks):
                    self.documents.append(chunk)
                    self.metadata.append({
                        'source_file': filename,
                        'page_number': sec_idx,
                        'chunk_index': i,
                        'total_pages': len(sections),
                        'chunk_id': f"{filename}_s{sec_idx}_c{i}"
                    })

        except Exception as e:
            print(f"Error processing {md_path}: {e}")

    def _chunk_text(self, text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """Simple text chunking"""
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size - overlap):
            chunk_words = words[i:i + chunk_size]
            chunk = ' '.join(chunk_words)
            if len(chunk.strip()) > 50:  # Only keep substantial chunks
                chunks.append(chunk)
        
        return chunks
    
    def build_index(self) -> None:
        """Build FAISS vector index"""
        if not self.documents:
            print("No documents to index")
            return
        
        print(f"Building index for {len(self.documents)} documents...")
        
        # Generate embeddings via HF API
        embeddings = self._embed(self.documents)
        
        # Create FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings.astype('float32'))
        
        print(f"Index built with {self.index.ntotal} vectors")
    
    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for relevant documents"""
        if self.index is None:
            return []
        
        # Generate query embedding via HF API
        query_embedding = self._embed([query])
        
        # Search
        scores, indices = self.index.search(query_embedding.astype('float32'), top_k)
        
        results = []
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            results.append({
                'text': self.documents[idx],
                'metadata': self.metadata[idx],
                'score': float(score),
                'rank': i + 1
            })
        
        return results
    
    def query(self, question: str, top_k: int = 5) -> Dict[str, Any]:
        """Answer a question using RAG"""
        print(f"Processing query: {question}")
        
        # Search for relevant documents
        search_results = self.search(question, top_k)
        
        if not search_results:
            return {
                'answer': 'No relevant documents found.',
                'sources': [],
                'error': 'No search results'
            }
        
        # Prepare context
        context_texts = []
        sources = []
        
        for result in search_results:
            context_texts.append(f"Source: {result['metadata']['source_file']} (Page {result['metadata']['page_number']})\\n{result['text']}")
            sources.append({
                'file': result['metadata']['source_file'],
                'page': result['metadata']['page_number'],
                'chunk_id': result['metadata']['chunk_id'],
                'score': result['score'],
                'text_preview': result['text'][:200] + "..." if len(result['text']) > 200 else result['text']
            })
        
        context = "\\n\\n".join(context_texts)
        
        # Create prompt
        prompt = f"""You are a manufacturing expert analyzing technical specifications. 
Based on the provided context documents, answer the following question accurately and precisely.

Context:
{context}

Question: {question}

Instructions:
- Provide a clear, specific answer with exact values and units when available
- Always cite the source document and page number
- If the answer requires multiple sources, reference all relevant ones
- If the information is not in the provided context, say so clearly

Answer:"""

        try:
            # Query Groq
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful manufacturing expert assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=1500
            )
            
            answer = response.choices[0].message.content
            
            return {
                'answer': answer,
                'sources': sources,
                'query': question,
                'error': None
            }
            
        except Exception as e:
            return {
                'answer': f'Error generating answer: {str(e)}',
                'sources': sources,
                'query': question,
                'error': str(e)
            }
    
    def save_index(self, filename: str) -> None:
        """Save the index and metadata"""
        if self.index is None:
            print("No index to save")
            return
        
        # Save FAISS index
        faiss.write_index(self.index, f"{filename}.faiss")
        
        # Save documents and metadata
        with open(f"{filename}_data.json", 'w') as f:
            json.dump({
                'documents': self.documents,
                'metadata': self.metadata
            }, f)
        
        print(f"Index saved to {filename}.faiss and {filename}_data.json")
    
    def load_index(self, filename: str) -> bool:
        """Load the index and metadata"""
        try:
            # Load FAISS index
            self.index = faiss.read_index(f"{filename}.faiss")
            
            # Load documents and metadata
            with open(f"{filename}_data.json", 'r') as f:
                data = json.load(f)
                self.documents = data['documents']
                self.metadata = data['metadata']
            
            print(f"Index loaded from {filename} with {len(self.documents)} documents")
            return True
            
        except Exception as e:
            print(f"Error loading index: {e}")
            return False

def main():
    """Main function to test the simple RAG system"""
    print("Simple RAG System Test with Groq")
    print("=" * 40)
    
    # Initialize system
    rag = SimpleRAGSystem()
    
    # Try to load existing index
    if rag.load_index("simple_rag_index"):
        print("Loaded existing index")
    else:
        print("Building new index...")
        # Process PDFs
        rag.process_pdfs(Config.DATA_DIR)
        
        # Build index
        rag.build_index()
        
        # Save index
        rag.save_index("simple_rag_index")
    
    # Test queries
    test_queries = [
        "What is bending location tolerance?",
        "What is LPI or Solder mask thickness?",
        "What is FPC design guideline of De-cap?",
    ]
    
    for query in test_queries:
        print(f"\\n{'='*50}")
        print(f"Query: {query}")
        print(f"{'='*50}")
        
        result = rag.query(query)
        
        if result['error']:
            print(f"Error: {result['error']}")
        else:
            print(f"Answer: {result['answer']}")
            print(f"\\nSources:")
            for i, source in enumerate(result['sources'], 1):
                print(f"  {i}. {source['file']} (Page {source['page']}) - Score: {source['score']:.3f}")
                print(f"     Preview: {source['text_preview']}")
        print()

if __name__ == "__main__":
    main()