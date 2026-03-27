#!/usr/bin/env python3
"""
Targeted improvements to the existing working system
Focus on: Better chunking, Query reformulation, Better prompting
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

class TargetedImprovedRAG:
    """Targeted improvements to existing RAG system"""
    
    def __init__(self, chunk_size=1200, chunk_overlap=300):
        # Enhanced chunking parameters
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Use existing embedding model for compatibility
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dimension = self.embedding_model.get_sentence_embedding_dimension()
        
        self.groq_client = OpenAI(
            api_key=Config.get_groq_api_key(),
            base_url=Config.GROQ_BASE_URL
        )
        
        # Storage
        self.documents = []
        self.metadata = []
        self.index = None
        
        print(f"Initialized TargetedImprovedRAG with dim: {self.dimension}")
    
    def process_pdfs(self, pdf_dir: str) -> None:
        """Process PDFs with better chunking strategy"""
        print(f"Processing PDFs with improved chunking: {pdf_dir}")
        
        pdf_files = list(Path(pdf_dir).glob("*.pdf"))
        print(f"Found {len(pdf_files)} PDF files")
        
        for pdf_file in pdf_files:
            print(f"  Processing: {pdf_file.name}")
            self._process_single_pdf(str(pdf_file))
        
        print(f"Total documents processed: {len(self.documents)}")
    
    def _process_single_pdf(self, pdf_path: str) -> None:
        """Process single PDF with enhanced extraction"""
        try:
            filename = os.path.basename(pdf_path)
            
            # Use PyMuPDF4LLM for markdown extraction
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            # Enhanced cleaning
            cleaned_text = self._enhanced_clean_markdown(md_text)
            
            # Better chunking strategy
            chunks = self._improved_chunking(cleaned_text)
            
            print(f"    Extracted {len(chunks)} chunks from {filename}")
            
            for i, chunk in enumerate(chunks):
                if len(chunk.strip()) > 100:  # Higher quality threshold
                    quality_score = self._calculate_chunk_quality(chunk)
                    
                    self.documents.append(chunk)
                    self.metadata.append({
                        'source_file': filename,
                        'chunk_index': i,
                        'total_chunks': len(chunks),
                        'chunk_id': f"{filename}_chunk_{i}",
                        'extraction_method': 'targeted_improved',
                        'quality_score': quality_score
                    })
            
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
    
    def _enhanced_clean_markdown(self, md_text: str) -> str:
        """Enhanced markdown cleaning focused on manufacturing content"""
        lines = md_text.split('\\n')
        cleaned_lines = []
        
        # Comprehensive skip patterns for manufacturing docs
        skip_patterns = [
            'property of apple',
            'confidential and proprietary', 
            'prior written consent',
            'maintain this document in confidence',
            'design guidelines for flexible printed circuits',
            'fpc \\(flexible printed circuit\\) design guideline',
            'page [0-9]+ of [0-9]+',
            'dwg number:',
            'apple inc\\.?$',
            'size:\\s*letter',
            'scale:\\s*none',
            'commodity code:',
            'rev:\\s*[a-z]',
            '==> picture',
            'intentionally omitted'
        ]
        
        for line in lines:
            line = line.strip()
            
            if not line:
                cleaned_lines.append('')  # Keep structure
                continue
                
            # Skip confidentiality and formatting lines
            if any(re.search(pattern, line.lower()) for pattern in skip_patterns):
                continue
            
            # Skip lines that are just repeated characters
            if len(set(line.replace(' ', ''))) <= 2 and len(line) > 10:
                continue
            
            # Clean table formatting but preserve structure
            if '|' in line:
                # Clean excessive table separators
                line = re.sub(r'\\|{3,}', '|', line)
                line = re.sub(r'\\s*\\|\\s*', ' | ', line)
                # Skip separator-only lines
                if re.match(r'^[\\s\\|\\-]+$', line):
                    continue
            
            # Normalize whitespace
            line = re.sub(r'\\s+', ' ', line)
            
            if line.strip():
                cleaned_lines.append(line)
        
        return '\\n'.join(cleaned_lines)
    
    def _improved_chunking(self, text: str) -> List[str]:
        """Improved chunking that preserves technical context"""
        # Split by major sections and tables
        chunks = []
        
        # First, handle tables separately (they should stay together)
        table_chunks, non_table_text = self._extract_and_chunk_tables(text)
        chunks.extend(table_chunks)
        
        # Then chunk the remaining text
        if non_table_text.strip():
            text_chunks = self._chunk_text_by_sections(non_table_text)
            chunks.extend(text_chunks)
        
        # Filter and improve chunks
        final_chunks = []
        for chunk in chunks:
            if self._is_high_quality_chunk(chunk):
                final_chunks.append(chunk.strip())
        
        return final_chunks
    
    def _extract_and_chunk_tables(self, text: str) -> Tuple[List[str], str]:
        """Extract tables and chunk them appropriately"""
        lines = text.split('\\n')
        table_chunks = []
        non_table_lines = []
        
        current_table = []
        in_table = False
        
        for line in lines:
            if '|' in line and len([c for c in line if c == '|']) >= 2:
                if not in_table:
                    in_table = True
                current_table.append(line)
            else:
                if in_table:
                    # End of table - process it
                    if current_table:
                        table_text = '\\n'.join(current_table)
                        # Split large tables but keep logical sections
                        if len(table_text) > self.chunk_size:
                            table_sections = self._split_large_table(table_text)
                            table_chunks.extend(table_sections)
                        else:
                            table_chunks.append(table_text)
                        current_table = []
                    in_table = False
                
                non_table_lines.append(line)
        
        # Handle any remaining table
        if current_table:
            table_text = '\\n'.join(current_table)
            table_chunks.append(table_text)
        
        return table_chunks, '\\n'.join(non_table_lines)
    
    def _split_large_table(self, table_text: str) -> List[str]:
        """Split large tables while preserving structure"""
        lines = table_text.split('\\n')
        header_lines = []
        data_lines = []
        
        # Identify header (usually first 1-2 lines)
        for i, line in enumerate(lines):
            if i < 2 or 'description' in line.lower() or 'item' in line.lower():
                header_lines.append(line)
            else:
                data_lines.append(line)
        
        chunks = []
        current_chunk_lines = header_lines.copy()
        
        for line in data_lines:
            if len('\\n'.join(current_chunk_lines + [line])) > self.chunk_size:
                # Finalize current chunk
                if len(current_chunk_lines) > len(header_lines):
                    chunks.append('\\n'.join(current_chunk_lines))
                # Start new chunk with header
                current_chunk_lines = header_lines + [line]
            else:
                current_chunk_lines.append(line)
        
        if len(current_chunk_lines) > len(header_lines):
            chunks.append('\\n'.join(current_chunk_lines))
        
        return chunks
    
    def _chunk_text_by_sections(self, text: str) -> List[str]:
        """Chunk non-table text by logical sections"""
        # Split by headers and major separators
        section_patterns = [
            r'\\n#{1,3}\\s+[^\\n]+',  # Markdown headers
            r'\\n\\d+\\.\\s+[^\\n]+', # Numbered sections  
            r'\\n[A-Z][A-Z\\s]{10,}\\n', # ALL CAPS headers
            r'\\n\\*\\*[^*]+\\*\\*\\n'    # Bold headers
        ]
        
        sections = [text]
        for pattern in section_patterns:
            new_sections = []
            for section in sections:
                if len(section.strip()) > 0:
                    parts = re.split(pattern, section)
                    new_sections.extend([p for p in parts if p.strip()])
            sections = new_sections
        
        # Chunk each section
        chunks = []
        for section in sections:
            if len(section.strip()) <= self.chunk_size:
                chunks.append(section.strip())
            else:
                # Split large sections by paragraphs with overlap
                para_chunks = self._chunk_by_paragraphs(section)
                chunks.extend(para_chunks)
        
        return chunks
    
    def _chunk_by_paragraphs(self, text: str) -> List[str]:
        """Chunk text by paragraphs with smart overlap"""
        paragraphs = [p.strip() for p in text.split('\\n\\n') if p.strip()]
        
        if not paragraphs:
            return []
        
        chunks = []
        current_chunk = ""
        
        for i, para in enumerate(paragraphs):
            # Test if adding this paragraph exceeds chunk size
            test_chunk = current_chunk + "\\n\\n" + para if current_chunk else para
            
            if len(test_chunk) > self.chunk_size and current_chunk:
                # Finalize current chunk
                chunks.append(current_chunk.strip())
                
                # Start new chunk with overlap
                overlap = self._get_paragraph_overlap(current_chunk)
                current_chunk = overlap + para
            else:
                current_chunk = test_chunk
        
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def _get_paragraph_overlap(self, text: str) -> str:
        """Get overlap text from previous chunk"""
        sentences = text.split('. ')
        if len(sentences) >= 2:
            # Take last 1-2 sentences for context
            return '. '.join(sentences[-2:]) + '. '
        return ""
    
    def _is_high_quality_chunk(self, chunk: str) -> bool:
        """Determine if chunk is high quality"""
        quality_score = self._calculate_chunk_quality(chunk)
        return quality_score > 0.25
    
    def _calculate_chunk_quality(self, chunk: str) -> float:
        """Calculate quality score for chunk"""
        if len(chunk) < 100:
            return 0.0
        
        chunk_lower = chunk.lower()
        score = 0.0
        
        # Technical manufacturing terms
        tech_terms = [
            'tolerance', 'thickness', 'diameter', 'width', 'length', 'mm', 'um', 'mil',
            'specification', 'requirement', 'minimum', 'maximum', 'test', 'quality',
            'solder', 'copper', 'adhesive', 'drill', 'laser', 'reflow', 'thermal',
            'resistance', 'voltage', 'current', 'impedance', 'frequency', 'temperature',
            'bending', 'via', 'trace', 'pad', 'mask', 'plating', 'coverlay', 'polyimide',
            'inspection', 'control', 'plan', 'process', 'procedure', 'acceptance', 'criteria',
            'fpc', 'pcb', 'flex', 'circuit', 'lamination', 'etching', 'alignment', 'upd',
            'cqra', 'qcp', 'lpi', 'emi', 'de-cap', 'bonding', 'adhesive'
        ]
        
        term_count = sum(chunk_lower.count(term) for term in tech_terms)
        score += min(term_count * 0.05, 0.5)
        
        # Numerical specifications
        number_patterns = [
            r'\\d+\\.?\\d*\\s*(mm|um|mil|%|ohm|°c)',
            r'±\\s*\\d+\\.?\\d*',
            r'\\d+\\.?\\d*\\s*±\\s*\\d+\\.?\\d*'
        ]
        
        for pattern in number_patterns:
            matches = len(re.findall(pattern, chunk_lower))
            score += matches * 0.15
        
        # Tables and structured data
        if '|' in chunk:
            score += 0.25
        
        # Normalize by length
        return min(score, 1.0)
    
    def build_index(self) -> None:
        """Build FAISS index"""
        if not self.documents:
            return
        
        print(f"Building index for {len(self.documents)} documents...")
        
        # Generate embeddings
        embeddings = self.embedding_model.encode(self.documents, show_progress_bar=True)
        
        # Create FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings.astype('float32'))
        
        print(f"Index built with {self.index.ntotal} vectors")
    
    def _reformulate_queries(self, question: str) -> List[str]:
        """Generate better search queries"""
        queries = [question]
        
        # Extract key technical terms
        tech_terms = re.findall(r'\\b(tolerance|thickness|dimension|diameter|criteria|plan|process|upd|lpi|cqra|de-cap|emi)\\b', question.lower())
        
        # Create acronym-focused queries
        acronyms = re.findall(r'\\b[A-Z]{2,5}\\b', question)
        if acronyms:
            for acronym in acronyms:
                queries.append(f"{acronym} definition manufacturing")
                queries.append(f"what is {acronym}")
        
        # For measurement questions, add unit-focused variants
        if any(word in question.lower() for word in ['tolerance', 'thickness', 'dimension', 'size']):
            queries.append(f"{question} mm um specification")
            
        # For process questions
        if any(word in question.lower() for word in ['plan', 'criteria', 'process', 'guideline']):
            base_term = question.lower().replace('what is', '').replace('?', '').strip()
            queries.append(f"{base_term} steps procedure requirements")
        
        return list(set(queries))[:5]  # Max 5 variants
    
    def search_with_query_expansion(self, question: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """Search with multiple query variants"""
        all_results = []
        query_variants = self._reformulate_queries(question)
        
        for query in query_variants:
            # Search for this query variant
            query_embedding = self.embedding_model.encode([query])
            scores, indices = self.index.search(query_embedding.astype('float32'), top_k)
            
            for score, idx in zip(scores[0], indices[0]):
                if idx < len(self.documents):
                    all_results.append({
                        'text': self.documents[idx],
                        'metadata': self.metadata[idx],
                        'score': float(score),
                        'query_variant': query
                    })
        
        # Deduplicate and sort
        unique_results = {}
        for result in all_results:
            chunk_id = result['metadata']['chunk_id']
            if chunk_id not in unique_results or result['score'] < unique_results[chunk_id]['score']:
                unique_results[chunk_id] = result
        
        sorted_results = sorted(unique_results.values(), key=lambda x: x['score'])
        return sorted_results[:top_k]
    
    def query(self, question: str, top_k: int = 5) -> Dict[str, Any]:
        """Query with all improvements"""
        print(f"Processing query with improvements: {question}")
        
        # Enhanced search
        search_results = self.search_with_query_expansion(question, top_k)
        
        if not search_results:
            return {
                'answer': 'No relevant documents found.',
                'sources': [],
                'error': 'No search results'
            }
        
        # Prepare enhanced context
        context_parts = []
        sources = []
        
        for i, result in enumerate(search_results):
            quality_score = result['metadata'].get('quality_score', 0.5)
            
            context_parts.append(
                f"Document {i+1}: {result['metadata']['source_file']}\\n"
                f"Quality Score: {quality_score:.2f}\\n"
                f"Content: {result['text']}"
            )
            
            sources.append({
                'file': result['metadata']['source_file'],
                'chunk_id': result['metadata']['chunk_id'],
                'score': result['score'],
                'quality_score': quality_score,
                'query_variant': result['query_variant'],
                'preview': result['text'][:300] + "..." if len(result['text']) > 300 else result['text']
            })
        
        context = "\\n\\n" + "="*50 + "\\n\\n".join(context_parts)
        
        # Enhanced manufacturing-specific prompt
        prompt = f"""You are a senior technical expert in FPC (Flexible Printed Circuit) and PCB manufacturing with deep knowledge of Apple's internal specifications and quality control procedures.

Your task is to provide precise, accurate answers based ONLY on the provided technical documents. These are official Apple manufacturing guidelines and quality control plans.

TECHNICAL CONTEXT:
{context}

QUESTION: {question}

ANALYSIS INSTRUCTIONS:
1. PRECISION: For measurements, extract exact numerical values with correct units (mm, um, %, etc.)
2. COMPLETENESS: For process/criteria questions, list ALL mentioned items, steps, or requirements  
3. ACCURACY: Quote specifications exactly as written in the source documents
4. SOURCE ATTRIBUTION: Always cite the specific document name
5. TECHNICAL FOCUS: Prioritize technical specifications over general descriptions

MANUFACTURING DOMAIN EXPERTISE:
- UPD = Unit Process Development (typically a qualification process)
- CQRA = Component Quality and Reliability Assessment 
- LPI = Liquid Photo-imageable (solder mask)
- EMI = Electromagnetic Interference
- De-cap = Layer removal process in multi-layer flex circuits
- FPC = Flexible Printed Circuit
- Tolerance values are critical - extract with ± symbols when present

ANSWER FORMAT:
- Start with the direct answer (measurement, definition, or list)
- Include all relevant technical details from the context
- End with source citation: "Source: [document name]"
- If multiple documents provide information, reference all

Answer:"""

        try:
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a precise manufacturing expert. Extract exact technical specifications from provided documents."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,  # Maximum precision
                max_tokens=1500
            )
            
            answer = response.choices[0].message.content
            
            return {
                'answer': answer,
                'sources': sources,
                'query': question,
                'query_variants': self._reformulate_queries(question),
                'error': None
            }
            
        except Exception as e:
            return {
                'answer': f'Error: {str(e)}',
                'sources': sources,
                'error': str(e)
            }
    
    def save_index(self, filename: str) -> None:
        """Save index and data"""
        if self.index is None:
            return
        
        faiss.write_index(self.index, f"{filename}.faiss")
        
        with open(f"{filename}_data.json", 'w') as f:
            json.dump({
                'documents': self.documents,
                'metadata': self.metadata
            }, f)
        
        print(f"Improved index saved to {filename}")
    
    def load_index(self, filename: str) -> bool:
        """Load index and data"""
        try:
            self.index = faiss.read_index(f"{filename}.faiss")
            
            with open(f"{filename}_data.json", 'r') as f:
                data = json.load(f)
                self.documents = data['documents']
                self.metadata = data['metadata']
            
            print(f"Improved index loaded with {len(self.documents)} documents")
            return True
            
        except Exception as e:
            print(f"Error loading index: {e}")
            return False

def main():
    """Test targeted improvements"""
    print("=" * 70)
    print("TARGETED IMPROVEMENTS - Better Chunking + Query Enhancement")
    print("=" * 70)
    
    rag = TargetedImprovedRAG(chunk_size=1200, chunk_overlap=300)
    
    # Build index
    rag.process_pdfs("/home/guilinzhang/allProjects/mfg-ai-platform/docs")
    rag.build_index()
    rag.save_index("targeted_improved_index")
    
    # Test key questions
    questions = [
        "What is bending location tolerance?",
        "What is UPD?"
    ]
    
    for question in questions:
        print(f"\\nTesting: {question}")
        result = rag.query(question)
        print(f"Answer: {result['answer'][:300]}...")
        print(f"Query variants: {result.get('query_variants', [])}")

if __name__ == "__main__":
    main()