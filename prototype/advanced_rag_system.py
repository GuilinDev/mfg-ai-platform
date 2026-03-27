#!/usr/bin/env python3
"""
Advanced RAG system with multiple improvements to achieve 80%+ accuracy
- Better embeddings (BGE models)
- Hybrid retrieval (vector + BM25)
- Query reformulation
- Better chunking strategy
- Manufacturing-specific prompting
"""

import os
import sys
import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
import pymupdf4llm
import faiss
from openai import OpenAI
import re
from dataclasses import dataclass
from rank_bm25 import BM25Okapi
import pickle
from sentence_transformers import SentenceTransformer

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))
from src.utils.config import Config

@dataclass
class SearchResult:
    """Structured search result"""
    text: str
    metadata: Dict[str, Any]
    score: float
    rank: int
    source_type: str  # 'vector', 'bm25', 'hybrid'

class AdvancedRAGSystem:
    """Advanced RAG system for manufacturing specifications"""
    
    def __init__(self, chunk_size=1000, chunk_overlap=200, use_bge=True):
        """Initialize with advanced configuration"""
        # Enhanced chunking parameters
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Initialize better embedding model
        if use_bge:
            try:
                self.embedding_model = SentenceTransformer("BAAI/bge-small-en-v1.5")
                print("Using BGE-small embedding model for better retrieval")
            except Exception as e:
                print(f"Failed to load BGE model, falling back to MiniLM: {e}")
                self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        else:
            self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        
        self.dimension = self.embedding_model.get_sentence_embedding_dimension()
        
        # Initialize Groq client
        self.groq_client = OpenAI(
            api_key=Config.get_groq_api_key(),
            base_url=Config.GROQ_BASE_URL
        )
        
        # Storage for documents, embeddings, and BM25
        self.documents = []
        self.metadata = []
        self.vector_index = None
        self.bm25_index = None
        
        print(f"Initialized AdvancedRAG with {self.embedding_model} (dim: {self.dimension})")
    
    def process_pdfs(self, pdf_dir: str) -> None:
        """Process all PDFs with enhanced extraction and chunking"""
        print(f"Processing PDFs from: {pdf_dir} with advanced parsing")
        
        pdf_files = list(Path(pdf_dir).glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDF files")
        
        for pdf_file in pdf_files:
            print(f"  Processing: {pdf_file.name}")
            self._process_single_pdf(str(pdf_file))
        
        print(f"Total documents processed: {len(self.documents)}")
    
    def _process_single_pdf(self, pdf_path: str) -> None:
        """Process a single PDF with advanced text extraction"""
        try:
            filename = os.path.basename(pdf_path)
            
            # Extract markdown content using PyMuPDF4LLM
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            # Advanced cleaning and preprocessing
            cleaned_text = self._advanced_clean_markdown(md_text)
            
            # Smart section-aware chunking
            chunks = self._advanced_chunking(cleaned_text)
            
            print(f"    Extracted {len(chunks)} chunks from {filename}")
            
            for i, chunk in enumerate(chunks):
                if len(chunk.strip()) > 80:  # Higher threshold for quality
                    self.documents.append(chunk)
                    self.metadata.append({
                        'source_file': filename,
                        'chunk_index': i,
                        'total_chunks': len(chunks),
                        'chunk_id': f"{filename}_chunk_{i}",
                        'extraction_method': 'advanced_pymupdf4llm',
                        'chunk_quality_score': self._calculate_quality_score(chunk)
                    })
            
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
    
    def _advanced_clean_markdown(self, md_text: str) -> str:
        """Advanced markdown cleaning with manufacturing focus"""
        lines = md_text.split('\n')
        cleaned_lines = []
        
        # Enhanced skip patterns
        skip_patterns = [
            'property of apple',
            'confidential and proprietary', 
            'prior written consent',
            'maintain this document in confidence',
            'fpc (flexible printed circuit) design guideline',
            'design guidelines for flexible printed circuits',
            '==> picture',
            'intentionally omitted',
            'page [0-9]+ of [0-9]+',
            'dwg number:',
            'apple inc.',
            'size: letter',
            'scale: none',
            'commodity code:'
        ]
        
        # Track context to avoid breaking table structures
        in_table = False
        table_buffer = []
        
        for line in lines:
            original_line = line
            line = line.strip()
            
            # Skip empty lines but preserve for table structure
            if not line:
                if in_table and table_buffer:
                    continue  # Skip empty lines in tables
                cleaned_lines.append('')
                continue
                
            # Detect tables
            if '|' in line and len([c for c in line if c == '|']) >= 3:
                in_table = True
                table_buffer.append(line)
                continue
            elif in_table and line and '|' not in line:
                # End of table - process buffer
                if table_buffer:
                    processed_table = self._process_table_buffer(table_buffer)
                    cleaned_lines.extend(processed_table)
                    table_buffer = []
                in_table = False
            
            # Skip lines matching skip patterns
            if any(re.search(pattern, line.lower()) for pattern in skip_patterns):
                continue
                
            # Skip lines that are just repeated characters
            if len(set(line.replace(' ', ''))) <= 2 and len(line) > 10:
                continue
            
            # Clean up formatting
            line = re.sub(r'\|\|+', ' | ', line)  # Normalize table separators
            line = re.sub(r'\s+', ' ', line)      # Normalize whitespace
            line = re.sub(r'^[\|\s]*$', '', line) # Remove lines that are just separators
            
            if line.strip():
                cleaned_lines.append(line)
        
        # Process any remaining table buffer
        if table_buffer:
            processed_table = self._process_table_buffer(table_buffer)
            cleaned_lines.extend(processed_table)
        
        return '\n'.join(cleaned_lines)
    
    def _process_table_buffer(self, table_lines: List[str]) -> List[str]:
        """Process table lines to improve structure"""
        if not table_lines:
            return []
        
        # Clean and structure table
        processed = []
        for line in table_lines:
            # Clean excessive separators while preserving structure
            cleaned = re.sub(r'\|{3,}', '|', line)
            cleaned = re.sub(r'\s*\|\s*', ' | ', cleaned)
            if cleaned.strip() and not re.match(r'^[\|\s\-]*$', cleaned):
                processed.append(cleaned)
        
        return processed
    
    def _advanced_chunking(self, text: str) -> List[str]:
        """Advanced section-aware chunking that preserves technical context"""
        # Split into sections by headers and major separators  
        section_patterns = [
            r'\n#{1,3}\s',      # Markdown headers
            r'\n\d+\.\s',       # Numbered sections
            r'\n[A-Z][A-Z\s]{10,}\n',  # ALL CAPS headers
            r'\n\*\*[^*]+\*\*\n',      # Bold headers
        ]
        
        # Split by sections first
        sections = [text]
        for pattern in section_patterns:
            new_sections = []
            for section in sections:
                parts = re.split(pattern, section)
                new_sections.extend(parts)
            sections = [s for s in new_sections if s.strip()]
        
        # Smart chunking within sections
        chunks = []
        for section in sections:
            section_chunks = self._chunk_section(section)
            chunks.extend(section_chunks)
        
        return [chunk for chunk in chunks if self._is_high_quality_chunk(chunk)]
    
    def _chunk_section(self, section: str) -> List[str]:
        """Chunk a section while preserving technical context"""
        if len(section) <= self.chunk_size:
            return [section]
        
        # Try to split by tables first
        if '|' in section:
            return self._chunk_with_tables(section)
        
        # Split by paragraphs, then sentences
        paragraphs = section.split('\n\n')
        chunks = []
        current_chunk = ""
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
                
            # If adding this paragraph exceeds chunk size
            if len(current_chunk) + len(para) > self.chunk_size and current_chunk:
                # Add overlap from previous chunk
                overlap = self._extract_overlap(current_chunk)
                chunks.append(current_chunk.strip())
                current_chunk = overlap + para
            else:
                if current_chunk:
                    current_chunk += '\n\n' + para
                else:
                    current_chunk = para
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def _chunk_with_tables(self, section: str) -> List[str]:
        """Special handling for sections containing tables"""
        # Keep tables together as much as possible
        parts = []
        current_part = ""
        
        lines = section.split('\n')
        in_table = False
        
        for line in lines:
            if '|' in line and len([c for c in line if c == '|']) >= 2:
                if not in_table and len(current_part) > self.chunk_size:
                    parts.append(current_part.strip())
                    current_part = ""
                in_table = True
            elif in_table and '|' not in line and line.strip():
                in_table = False
            
            current_part += line + '\n'
            
            # If we're not in a table and chunk is getting large
            if not in_table and len(current_part) > self.chunk_size:
                parts.append(current_part.strip())
                current_part = ""
        
        if current_part.strip():
            parts.append(current_part.strip())
        
        return parts
    
    def _extract_overlap(self, chunk: str) -> str:
        """Extract overlap text for context continuity"""
        sentences = chunk.split('. ')
        if len(sentences) >= 2:
            # Take last 1-2 sentences as overlap
            overlap_sentences = sentences[-2:]
            return '. '.join(overlap_sentences) + '. '
        return ""
    
    def _is_high_quality_chunk(self, chunk: str) -> bool:
        """Enhanced quality check for chunks"""
        if len(chunk) < 80:
            return False
        
        quality_score = self._calculate_quality_score(chunk)
        return quality_score > 0.3  # Threshold for quality
    
    def _calculate_quality_score(self, chunk: str) -> float:
        """Calculate quality score for a chunk"""
        chunk_lower = chunk.lower()
        score = 0.0
        
        # Technical terms (manufacturing focus)
        tech_terms = [
            'tolerance', 'thickness', 'diameter', 'width', 'length', 'mm', 'um', 'mil',
            'specification', 'requirement', 'minimum', 'maximum', 'test', 'quality',
            'solder', 'copper', 'adhesive', 'drill', 'laser', 'reflow', 'thermal',
            'resistance', 'voltage', 'current', 'impedance', 'frequency', 'temperature',
            'bending', 'via', 'trace', 'pad', 'mask', 'plating', 'coverlay', 'polyimide',
            'inspection', 'control', 'plan', 'process', 'procedure', 'acceptance', 'criteria',
            'fpc', 'pcb', 'flex', 'circuit', 'lamination', 'etching', 'alignment'
        ]
        
        # Count technical terms with different weights
        for term in tech_terms:
            count = chunk_lower.count(term)
            if term in ['mm', 'um', 'mil', '%']:  # Units are very valuable
                score += count * 0.15
            elif term in ['tolerance', 'thickness', 'specification', 'requirement']:
                score += count * 0.12
            else:
                score += count * 0.08
        
        # Numerical specifications (very important for manufacturing)
        number_patterns = [
            r'\d+\.?\d*\s*(mm|um|mil|%|ohm|°c|mhz|khz|v|a|w|pf|nh)',
            r'±\s*\d+\.?\d*',
            r'\d+\.?\d*\s*±\s*\d+\.?\d*',
            r'(minimum|maximum|min|max)\s*[:\-]?\s*\d+\.?\d*'
        ]
        
        for pattern in number_patterns:
            matches = len(re.findall(pattern, chunk_lower))
            score += matches * 0.2
        
        # Tables and structured data
        if '|' in chunk:
            score += 0.3
        
        # Normalize by chunk length
        normalized_score = min(score / (len(chunk) / 1000), 1.0)
        
        return normalized_score
    
    def build_indices(self) -> None:
        """Build both vector and BM25 indices"""
        if not self.documents:
            print("No documents to index")
            return
        
        print(f"Building indices for {len(self.documents)} documents...")
        
        # Build vector index
        print("Building FAISS vector index...")
        batch_size = 32
        all_embeddings = []
        
        for i in range(0, len(self.documents), batch_size):
            batch = self.documents[i:i+batch_size]
            batch_embeddings = self.embedding_model.encode(batch, show_progress_bar=True)
            all_embeddings.append(batch_embeddings)
        
        embeddings = np.vstack(all_embeddings)
        
        self.vector_index = faiss.IndexFlatL2(self.dimension)
        self.vector_index.add(embeddings.astype('float32'))
        
        # Build BM25 index
        print("Building BM25 keyword index...")
        tokenized_docs = []
        for doc in self.documents:
            # Simple tokenization - split by whitespace and clean
            tokens = re.findall(r'\b\w+\b', doc.lower())
            tokenized_docs.append(tokens)
        
        self.bm25_index = BM25Okapi(tokenized_docs)
        
        print(f"Indices built: Vector={self.vector_index.ntotal} docs, BM25={len(tokenized_docs)} docs")
    
    def _reformulate_query(self, query: str) -> List[str]:
        """Generate multiple search-friendly query variants"""
        variants = [query]  # Original query
        
        # Extract key technical terms and create focused queries
        tech_terms = re.findall(r'\b(tolerance|thickness|dimension|diameter|width|length|spec|criteria|plan|process|requirement|guideline)\b', query.lower())
        
        if tech_terms:
            # Create term-focused variant
            focused_query = ' '.join(tech_terms + [query])
            variants.append(focused_query)
        
        # Look for specific measurement requests
        if any(word in query.lower() for word in ['what is', 'define', 'definition']):
            # For definition queries, try without question words
            clean_query = re.sub(r'^(what is|define|definition of)\s*', '', query, flags=re.IGNORECASE)
            variants.append(clean_query)
        
        # Add manufacturing context
        if not any(term in query.lower() for term in ['fpc', 'pcb', 'manufacturing', 'circuit']):
            variants.append(f"{query} FPC manufacturing specification")
        
        return list(set(variants))  # Remove duplicates
    
    def vector_search(self, query: str, top_k: int = 10) -> List[SearchResult]:
        """Vector-based semantic search"""
        if self.vector_index is None:
            return []
        
        query_embedding = self.embedding_model.encode([query])
        scores, indices = self.vector_index.search(query_embedding.astype('float32'), top_k)
        
        results = []
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx < len(self.documents):  # Valid index
                results.append(SearchResult(
                    text=self.documents[idx],
                    metadata=self.metadata[idx],
                    score=float(score),
                    rank=i + 1,
                    source_type='vector'
                ))
        
        return results
    
    def bm25_search(self, query: str, top_k: int = 10) -> List[SearchResult]:
        """BM25-based keyword search"""
        if self.bm25_index is None:
            return []
        
        query_tokens = re.findall(r'\b\w+\b', query.lower())
        scores = self.bm25_index.get_scores(query_tokens)
        
        # Get top-k indices
        top_indices = np.argsort(scores)[::-1][:top_k]
        
        results = []
        for i, idx in enumerate(top_indices):
            if scores[idx] > 0:  # Only include relevant results
                results.append(SearchResult(
                    text=self.documents[idx],
                    metadata=self.metadata[idx],
                    score=float(scores[idx]),
                    rank=i + 1,
                    source_type='bm25'
                ))
        
        return results
    
    def hybrid_search(self, query: str, top_k: int = 5) -> List[SearchResult]:
        """Hybrid search combining vector and BM25 with query reformulation"""
        all_results = []
        
        # Get query variants
        query_variants = self._reformulate_query(query)
        
        for variant in query_variants:
            # Vector search
            vector_results = self.vector_search(variant, top_k=10)
            # BM25 search  
            bm25_results = self.bm25_search(variant, top_k=10)
            
            all_results.extend(vector_results)
            all_results.extend(bm25_results)
        
        # Deduplicate and rerank
        unique_results = self._deduplicate_and_rerank(all_results)
        
        return unique_results[:top_k]
    
    def _deduplicate_and_rerank(self, results: List[SearchResult]) -> List[SearchResult]:
        """Remove duplicates and rerank results"""
        # Group by document ID
        doc_groups = {}
        for result in results:
            doc_id = result.metadata['chunk_id']
            if doc_id not in doc_groups:
                doc_groups[doc_id] = []
            doc_groups[doc_id].append(result)
        
        # For each document, take the best score from either method
        final_results = []
        for doc_id, group in doc_groups.items():
            # Normalize scores for comparison (lower is better for vector, higher for BM25)
            vector_results = [r for r in group if r.source_type == 'vector']
            bm25_results = [r for r in group if r.source_type == 'bm25']
            
            best_result = None
            
            if vector_results and bm25_results:
                # Both types available - combine scores
                best_vector = min(vector_results, key=lambda x: x.score)
                best_bm25 = max(bm25_results, key=lambda x: x.score)
                
                # Normalize and combine (simple approach)
                combined_score = (1.0 / (1.0 + best_vector.score)) + (best_bm25.score / 10.0)
                
                best_result = SearchResult(
                    text=best_vector.text,
                    metadata=best_vector.metadata,
                    score=combined_score,
                    rank=0,  # Will be reassigned
                    source_type='hybrid'
                )
            elif vector_results:
                best_result = min(vector_results, key=lambda x: x.score)
                best_result.score = 1.0 / (1.0 + best_result.score)  # Normalize
            elif bm25_results:
                best_result = max(bm25_results, key=lambda x: x.score)
                best_result.score = best_result.score / 10.0  # Normalize
            
            if best_result:
                final_results.append(best_result)
        
        # Sort by combined score (higher is better now)
        final_results.sort(key=lambda x: x.score, reverse=True)
        
        # Reassign ranks
        for i, result in enumerate(final_results):
            result.rank = i + 1
        
        return final_results
    
    def query(self, question: str, top_k: int = 5, use_hybrid: bool = True) -> Dict[str, Any]:
        """Answer a question using advanced RAG techniques"""
        print(f"Processing query with advanced RAG: {question}")
        
        # Use hybrid search by default
        if use_hybrid:
            search_results = self.hybrid_search(question, top_k)
        else:
            search_results = self.vector_search(question, top_k)
        
        if not search_results:
            return {
                'answer': 'No relevant documents found.',
                'sources': [],
                'error': 'No search results',
                'method': 'hybrid' if use_hybrid else 'vector'
            }
        
        # Prepare context with quality-based filtering
        context_texts = []
        sources = []
        
        for result in search_results:
            quality_score = result.metadata.get('chunk_quality_score', 0.5)
            
            # Include high-quality results or ensure at least one result
            if quality_score > 0.3 or len(context_texts) == 0:
                context_texts.append(
                    f"Source: {result.metadata['source_file']}\\n"
                    f"Quality: {quality_score:.2f} | Search: {result.source_type}\\n"
                    f"{result.text}"
                )
                
                sources.append({
                    'file': result.metadata['source_file'],
                    'chunk_id': result.metadata['chunk_id'],
                    'score': result.score,
                    'quality_score': quality_score,
                    'search_type': result.source_type,
                    'text_preview': result.text[:300] + "..." if len(result.text) > 300 else result.text
                })
        
        context = "\\n\\n---\\n\\n".join(context_texts)
        
        # Enhanced prompt for manufacturing domain
        prompt = f"""You are a technical expert specializing in FPC (Flexible Printed Circuit) and PCB manufacturing specifications. 

Your task is to answer the question based ONLY on the provided technical documents. You have access to Apple's internal manufacturing guidelines and quality control plans.

Context Documents:
{context}

Question: {question}

Instructions:
1. Extract the exact answer with precise values, units, and specifications
2. For numerical answers, provide the exact number with correct units (mm, um, %, etc.)
3. For process questions, list the specific steps, criteria, or components mentioned
4. Always cite the source document name
5. If multiple values or criteria are mentioned, include ALL of them
6. If the exact answer is not in the provided context, state that clearly
7. Focus on technical accuracy - manufacturing specifications must be precise

Technical Guidelines:
- When extracting measurements, preserve units exactly as written (mm, um, mil, %)
- For tolerance questions, look for ± symbols and range values
- For process questions, extract step-by-step procedures or criteria lists
- For definition questions, provide the complete technical definition

Answer:"""

        try:
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a precise technical expert in FPC/PCB manufacturing. Provide exact specifications from the provided documents."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.05,  # Very low temperature for precision
                max_tokens=2000
            )
            
            answer = response.choices[0].message.content
            
            return {
                'answer': answer,
                'sources': sources,
                'query': question,
                'method': 'hybrid' if use_hybrid else 'vector',
                'query_variants': self._reformulate_query(question),
                'error': None
            }
            
        except Exception as e:
            return {
                'answer': f'Error generating answer: {str(e)}',
                'sources': sources,
                'query': question,
                'error': str(e)
            }
    
    def save_indices(self, filename: str) -> None:
        """Save all indices and data"""
        if self.vector_index is None:
            print("No indices to save")
            return
        
        # Save FAISS vector index
        faiss.write_index(self.vector_index, f"{filename}_vector.faiss")
        
        # Save BM25 index
        with open(f"{filename}_bm25.pkl", 'wb') as f:
            pickle.dump(self.bm25_index, f)
        
        # Save documents and metadata
        with open(f"{filename}_data.json", 'w') as f:
            json.dump({
                'documents': self.documents,
                'metadata': self.metadata,
                'config': {
                    'chunk_size': self.chunk_size,
                    'chunk_overlap': self.chunk_overlap,
                    'embedding_model': str(self.embedding_model)
                }
            }, f)
        
        print(f"Advanced indices saved to {filename}_*.faiss/pkl/json")
    
    def load_indices(self, filename: str) -> bool:
        """Load all indices and data"""
        try:
            # Load FAISS index
            self.vector_index = faiss.read_index(f"{filename}_vector.faiss")
            
            # Load BM25 index
            with open(f"{filename}_bm25.pkl", 'rb') as f:
                self.bm25_index = pickle.load(f)
            
            # Load documents and metadata
            with open(f"{filename}_data.json", 'r') as f:
                data = json.load(f)
                self.documents = data['documents']
                self.metadata = data['metadata']
            
            print(f"Advanced indices loaded: {len(self.documents)} docs")
            return True
            
        except Exception as e:
            print(f"Error loading indices: {e}")
            return False

def main():
    """Test the advanced RAG system"""
    print("=" * 70)
    print("ADVANCED RAG SYSTEM - Multiple Improvements for 80%+ Accuracy")
    print("=" * 70)
    
    # Initialize advanced system
    rag = AdvancedRAGSystem(chunk_size=1200, chunk_overlap=300, use_bge=True)
    
    # Build new advanced indices
    print("Building advanced indices...")
    rag.process_pdfs("/home/guilinzhang/allProjects/mfg-ai-platform/docs")
    rag.build_indices()
    rag.save_indices("advanced_rag_index")
    
    # Quick test
    test_query = "What is bending location tolerance?"
    print(f"\\nTesting query: {test_query}")
    result = rag.query(test_query, use_hybrid=True)
    
    print(f"Answer: {result['answer']}")
    print(f"Method: {result['method']}")
    print(f"Sources: {len(result['sources'])} documents")

if __name__ == "__main__":
    main()