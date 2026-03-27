#!/usr/bin/env python3
"""
Improved RAG system using PyMuPDF4LLM for better PDF parsing
"""
import os
import sys
import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
import pymupdf4llm
from sentence_transformers import SentenceTransformer
import faiss
from openai import OpenAI
import re

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from src.utils.config import Config

class ImprovedRAGSystem:
    """Improved RAG system with PyMuPDF4LLM parsing"""
    
    def __init__(self, chunk_size=800, chunk_overlap=100):
        # Initialize components
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dimension = self.embedding_model.get_sentence_embedding_dimension()
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        self.groq_client = OpenAI(
            api_key=Config.get_groq_api_key(),
            base_url=Config.GROQ_BASE_URL
        )
        
        # Storage for documents and embeddings
        self.documents = []
        self.metadata = []
        self.index = None
        
        print(f"Initialized ImprovedRAG with embedding dimension: {self.dimension}")
    
    def process_pdfs(self, pdf_dir: str) -> None:
        """Process all PDFs in a directory with improved parsing"""
        print(f"Processing PDFs from: {pdf_dir} with PyMuPDF4LLM")
        
        pdf_files = list(Path(pdf_dir).glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDF files")
        
        for pdf_file in pdf_files:
            print(f"  Processing: {pdf_file.name}")
            self._process_single_pdf(str(pdf_file))
        
        print(f"Total documents processed: {len(self.documents)}")
    
    def _process_single_pdf(self, pdf_path: str) -> None:
        """Process a single PDF file using PyMuPDF4LLM"""
        try:
            filename = os.path.basename(pdf_path)
            
            # Extract markdown content using PyMuPDF4LLM
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            # Clean and chunk the content
            cleaned_text = self._clean_markdown(md_text)
            chunks = self._chunk_text_smartly(cleaned_text)
            
            print(f"    Extracted {len(chunks)} chunks from {filename}")
            
            for i, chunk in enumerate(chunks):
                if len(chunk.strip()) > 50:  # Only keep substantial chunks
                    self.documents.append(chunk)
                    self.metadata.append({
                        'source_file': filename,
                        'chunk_index': i,
                        'total_chunks': len(chunks),
                        'chunk_id': f"{filename}_chunk_{i}",
                        'extraction_method': 'pymupdf4llm_markdown'
                    })
            
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
    
    def _clean_markdown(self, md_text: str) -> str:
        """Clean up markdown text and filter out low-quality content"""
        lines = md_text.split('\n')
        cleaned_lines = []
        
        skip_patterns = [
            'property of apple',
            'confidential and proprietary',
            'prior written consent',
            'maintain this document in confidence',
            'fpc (flexible printed circuit) design guideline',
            '==> picture',
            'intentionally omitted',
        ]
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                cleaned_lines.append('')  # Keep line breaks for structure
                continue
                
            # Skip lines that are just repeated characters
            if len(set(line.replace(' ', ''))) <= 2 and len(line) > 10:
                continue
                
            # Skip confidentiality headers and boilerplate
            if any(pattern in line.lower() for pattern in skip_patterns):
                continue
            
            # Clean up table formatting markers
            line = re.sub(r'\|\|+', '', line)  # Remove excessive table markers
            line = re.sub(r'\s+', ' ', line)    # Normalize whitespace
            
            if line.strip():  # Only add non-empty lines
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def _chunk_text_smartly(self, text: str) -> List[str]:
        """Smart text chunking that preserves technical context"""
        # First, split by major sections (double newlines)
        sections = text.split('\n\n')
        chunks = []
        current_chunk = ""
        
        for section in sections:
            section = section.strip()
            if not section:
                continue
                
            # If this section would make chunk too big, finalize current chunk
            if len(current_chunk) + len(section) > self.chunk_size and current_chunk:
                if self._is_meaningful_chunk(current_chunk):
                    chunks.append(current_chunk.strip())
                
                # Start new chunk with some overlap for context
                current_chunk = self._get_overlap(current_chunk) + section
            else:
                # Add to current chunk
                if current_chunk:
                    current_chunk += '\n\n' + section
                else:
                    current_chunk = section
        
        # Add final chunk
        if current_chunk.strip() and self._is_meaningful_chunk(current_chunk):
            chunks.append(current_chunk.strip())
        
        # Further split any overly large chunks
        final_chunks = []
        for chunk in chunks:
            if len(chunk) > self.chunk_size * 2:  # If still too large
                sub_chunks = self._split_large_chunk(chunk)
                final_chunks.extend(sub_chunks)
            else:
                final_chunks.append(chunk)
        
        return final_chunks
    
    def _get_overlap(self, text: str) -> str:
        """Get overlap text from end of previous chunk"""
        sentences = text.split('. ')
        if len(sentences) >= 2:
            # Take last 1-2 sentences as overlap
            overlap_sentences = sentences[-2:]
            return '. '.join(overlap_sentences) + '. '
        return ""
    
    def _split_large_chunk(self, chunk: str) -> List[str]:
        """Split overly large chunks while preserving context"""
        sentences = chunk.split('. ')
        sub_chunks = []
        current_sub = ""
        
        for sentence in sentences:
            if len(current_sub) + len(sentence) > self.chunk_size and current_sub:
                sub_chunks.append(current_sub.strip() + '.')
                current_sub = sentence
            else:
                if current_sub:
                    current_sub += '. ' + sentence
                else:
                    current_sub = sentence
        
        if current_sub.strip():
            sub_chunks.append(current_sub.strip())
        
        return sub_chunks
    
    def _is_meaningful_chunk(self, chunk: str) -> bool:
        """Check if chunk contains meaningful technical content"""
        if len(chunk) < 50:
            return False
            
        chunk_lower = chunk.lower()
        
        # Technical indicators
        technical_terms = [
            'tolerance', 'thickness', 'diameter', 'width', 'length', 'mm', 'um', 'mil',
            'specification', 'requirement', 'minimum', 'maximum', 'test', 'quality',
            'solder', 'copper', 'adhesive', 'drill', 'laser', 'reflow', 'thermal',
            'resistance', 'voltage', 'current', 'impedance', 'frequency', 'temperature',
            'bending', 'via', 'trace', 'pad', 'mask', 'plating', 'coverlay', 'polyimide',
            'inspection', 'control', 'plan', 'process', 'procedure', 'acceptance', 'criteria'
        ]
        
        tech_count = sum(1 for term in technical_terms if term in chunk_lower)
        
        # Look for numerical specifications
        number_patterns = [
            r'\d+\.?\d*\s*(mm|um|mil|%|ohm|°c|mhz|khz|v|a|w|pf|nh)',
            r'±\s*\d+\.?\d*',
            r'\d+\.?\d*\s*±\s*\d+\.?\d*',
            r'(minimum|maximum|min|max)\s*[:\-]?\s*\d+\.?\d*'
        ]
        
        number_count = sum(len(re.findall(pattern, chunk_lower)) for pattern in number_patterns)
        
        # Tables or structured data
        has_table = '|' in chunk or 'table' in chunk_lower
        
        return tech_count >= 2 or number_count >= 1 or has_table
    
    def build_index(self) -> None:
        """Build FAISS vector index"""
        if not self.documents:
            print("No documents to index")
            return
        
        print(f"Building index for {len(self.documents)} documents...")
        
        # Generate embeddings in batches to avoid memory issues
        batch_size = 32
        all_embeddings = []
        
        for i in range(0, len(self.documents), batch_size):
            batch = self.documents[i:i+batch_size]
            batch_embeddings = self.embedding_model.encode(batch, show_progress_bar=True)
            all_embeddings.append(batch_embeddings)
        
        embeddings = np.vstack(all_embeddings)
        
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
        """Answer a question using improved RAG"""
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
            context_texts.append(f"Source: {result['metadata']['source_file']}\\n{result['text']}")
            sources.append({
                'file': result['metadata']['source_file'],
                'chunk_id': result['metadata']['chunk_id'],
                'score': result['score'],
                'text_preview': result['text'][:300] + "..." if len(result['text']) > 300 else result['text']
            })
        
        context = "\\n\\n---\\n\\n".join(context_texts)
        
        # Create prompt
        prompt = f"""You are a manufacturing expert analyzing technical specifications. 
Based on the provided context documents, answer the following question accurately and precisely.

Context:
{context}

Question: {question}

Instructions:
- Provide a clear, specific answer with exact values and units when available
- Always cite the source document 
- If the answer requires multiple sources, reference all relevant ones
- If the information is not in the provided context, say so clearly
- Focus on extracting exact specifications, measurements, and technical details

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
        
        print(f"Improved index saved to {filename}.faiss and {filename}_data.json")
    
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
            
            print(f"Improved index loaded from {filename} with {len(self.documents)} documents")
            return True
            
        except Exception as e:
            print(f"Error loading index: {e}")
            return False

def main():
    """Test the improved RAG system"""
    print("=" * 60)
    print("IMPROVED RAG SYSTEM - PyMuPDF4LLM")
    print("=" * 60)
    
    # Initialize system
    rag = ImprovedRAGSystem()
    
    # Build new improved index
    print("Building improved index with PyMuPDF4LLM...")
    rag.process_pdfs("/home/guilinzhang/allProjects/mfg-ai-platform/docs")
    rag.build_index()
    rag.save_index("improved_rag_index")
    
    # Test a few queries
    test_queries = [
        "What is bending location tolerance?",
        "What is LPI or Solder mask thickness?",
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
            for i, source in enumerate(result['sources'][:3], 1):
                print(f"  {i}. {source['file']} - Score: {source['score']:.3f}")
                print(f"     Preview: {source['text_preview']}")

if __name__ == "__main__":
    main()