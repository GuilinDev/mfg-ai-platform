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
from sentence_transformers import SentenceTransformer
import faiss
from openai import OpenAI

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from src.utils.config import Config

class SimpleRAGSystem:
    """Simple RAG system with Groq LLM and local embeddings"""
    
    def __init__(self):
        # Initialize components
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dimension = self.embedding_model.get_sentence_embedding_dimension()
        
        self.groq_client = OpenAI(
            api_key=Config.get_groq_api_key(),
            base_url=Config.GROQ_BASE_URL
        )
        
        # Storage for documents and embeddings
        self.documents = []
        self.metadata = []
        self.index = None
        
        print(f"Initialized SimpleRAG with embedding dimension: {self.dimension}")
    
    def process_pdfs(self, pdf_dir: str) -> None:
        """Process all PDFs in a directory"""
        print(f"Processing PDFs from: {pdf_dir}")
        
        pdf_files = list(Path(pdf_dir).glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDF files")
        
        for pdf_file in pdf_files:
            print(f"  Processing: {pdf_file.name}")
            self._process_single_pdf(str(pdf_file))
        
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
                    chunks = self._chunk_text(text, chunk_size=512, overlap=50)
                    
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
        
        # Generate embeddings
        embeddings = self.embedding_model.encode(self.documents, show_progress_bar=True)
        
        # Create FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings.astype('float32'))
        
        print(f"Index built with {self.index.ntotal} vectors")
    
    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for relevant documents"""
        if self.index is None:
            return []
        
        # Generate query embedding
        query_embedding = self.embedding_model.encode([query])
        
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