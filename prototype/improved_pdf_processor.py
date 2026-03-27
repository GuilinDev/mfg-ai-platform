#!/usr/bin/env python3
"""
Improved PDF processor using PyMuPDF4LLM for better text and table extraction
"""
import os
import sys
from pathlib import Path
from typing import List, Dict, Any
import pymupdf4llm

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

class ImprovedPDFProcessor:
    """Enhanced PDF processor using PyMuPDF4LLM for markdown output"""
    
    def __init__(self, chunk_size: int = 1024, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
    def process_file(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Process a single PDF file using PyMuPDF4LLM"""
        try:
            print(f"Processing {pdf_path} with PyMuPDF4LLM...")
            
            # Extract markdown content using PyMuPDF4LLM
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            filename = os.path.basename(pdf_path)
            
            # Clean up the markdown text
            cleaned_text = self._clean_markdown(md_text)
            
            # Chunk the text
            chunks = self._chunk_text(cleaned_text, self.chunk_size, self.chunk_overlap)
            
            documents = []
            for i, chunk in enumerate(chunks):
                doc_data = {
                    'text': chunk,
                    'metadata': {
                        'source_file': filename,
                        'chunk_index': i,
                        'total_chunks': len(chunks),
                        'chunk_id': f"{filename}_chunk_{i}",
                        'extraction_method': 'pymupdf4llm_markdown',
                        'document_type': 'specification'
                    }
                }
                documents.append(doc_data)
            
            print(f"Extracted {len(documents)} chunks from {filename}")
            return documents
            
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
            return []
    
    def _clean_markdown(self, md_text: str) -> str:
        """Clean up markdown text and filter out low-quality content"""
        lines = md_text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Skip lines that are just repeated characters or formatting
            if len(set(line.replace(' ', ''))) <= 2 and len(line) > 10:
                continue
                
            # Skip Apple confidentiality headers (they appear in every document)
            if any(phrase in line.lower() for phrase in [
                'property of apple',
                'confidential and proprietary',
                'prior written consent',
                'maintain this document in confidence'
            ]):
                continue
                
            # Skip overly generic content
            if any(phrase in line.lower() for phrase in [
                'fpc (flexible printed circuit) design guideline',
                'introduction:',
                'the purpose of this document'
            ]) and len(line) < 200:
                continue
            
            cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def _chunk_text(self, text: str, chunk_size: int, overlap: int) -> List[str]:
        """Chunk text by sentences/paragraphs for better context preservation"""
        # Split by double newlines (paragraphs) first
        paragraphs = text.split('\n\n')
        
        chunks = []
        current_chunk = ""
        
        for paragraph in paragraphs:
            # If adding this paragraph would exceed chunk size, finalize current chunk
            if len(current_chunk) + len(paragraph) > chunk_size and current_chunk:
                chunks.append(current_chunk.strip())
                
                # Start new chunk with overlap
                words = current_chunk.split()
                if len(words) > overlap:
                    overlap_text = ' '.join(words[-overlap:])
                    current_chunk = overlap_text + '\n\n' + paragraph
                else:
                    current_chunk = paragraph
            else:
                # Add paragraph to current chunk
                if current_chunk:
                    current_chunk += '\n\n' + paragraph
                else:
                    current_chunk = paragraph
        
        # Add the final chunk
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        # Filter out chunks that are too small or low-quality
        filtered_chunks = []
        for chunk in chunks:
            if len(chunk) > 100 and self._is_meaningful_chunk(chunk):
                filtered_chunks.append(chunk)
        
        return filtered_chunks
    
    def _is_meaningful_chunk(self, chunk: str) -> bool:
        """Check if chunk contains meaningful technical content"""
        chunk_lower = chunk.lower()
        
        # Must contain some technical terms or measurements
        technical_indicators = [
            'mm', 'um', 'mil', 'ohm', '%', '±', 'tolerance', 'thickness',
            'temperature', 'voltage', 'current', 'resistance', 'specification',
            'requirement', 'minimum', 'maximum', 'diameter', 'width', 'length',
            'solder', 'copper', 'adhesive', 'polyimide', 'coverlay', 'via',
            'trace', 'pad', 'mask', 'plating', 'drill', 'laser', 'test',
            'quality', 'control', 'inspection', 'reflow', 'thermal', 'bend'
        ]
        
        # Count technical indicators
        tech_count = sum(1 for indicator in technical_indicators if indicator in chunk_lower)
        
        # Also look for numerical values
        import re
        number_pattern = r'\d+\.?\d*\s*(mm|um|mil|%|ohm|°c|mhz|khz|v|a|w)'
        numbers = len(re.findall(number_pattern, chunk_lower))
        
        # Consider meaningful if it has technical terms or numerical specifications
        return tech_count >= 2 or numbers >= 1

def test_improved_processor():
    """Test the improved PDF processor on a single file"""
    processor = ImprovedPDFProcessor()
    
    # Test on one PDF first
    test_pdf = "/home/guilinzhang/allProjects/mfg-ai-platform/docs/080-3649-E_design_guideline_FPC.pdf"
    
    documents = processor.process_file(test_pdf)
    
    print(f"\nProcessed {len(documents)} chunks")
    print("\nSample chunks:")
    
    for i, doc in enumerate(documents[:5]):  # Show first 5 chunks
        print(f"\nChunk {i+1}:")
        print(f"Length: {len(doc['text'])} chars")
        print(f"Preview: {doc['text'][:200]}...")
        print("-" * 50)

if __name__ == "__main__":
    test_improved_processor()