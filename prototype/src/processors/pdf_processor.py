# PDF Document Processor for Manufacturing RAG System
import os
from typing import List, Dict, Any
import fitz  # PyMuPDF
from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter
import re

class PDFProcessor:
    """Process PDF documents with enhanced metadata extraction"""
    
    def __init__(self, chunk_size: int = 1024, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = SentenceSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap
        )
        
    def process_file(self, pdf_path: str) -> List[Document]:
        """Process a single PDF file and return chunked documents with metadata"""
        try:
            doc = fitz.open(pdf_path)
            documents = []
            
            # Extract document metadata
            doc_metadata = self._extract_document_metadata(doc, pdf_path)
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                
                # Extract text content
                text = page.get_text()
                
                if len(text.strip()) > 50:  # Only process pages with substantial content
                    
                    # Enhanced page metadata
                    page_metadata = {
                        **doc_metadata,
                        'page_number': page_num + 1,
                        'total_pages': len(doc),
                        'section': self._identify_section(text),
                        'content_type': self._classify_content_type(text),
                        'has_tables': 'Table' in text or '|' in text,
                        'has_specifications': self._has_specifications(text),
                        'extraction_method': 'pdf_text'
                    }
                    
                    # Create document object
                    page_doc = Document(
                        text=text,
                        metadata=page_metadata
                    )
                    
                    documents.append(page_doc)
                    
            doc.close()
            
            # Chunk the documents
            chunked_docs = []
            for doc in documents:
                chunks = self.splitter.split_text(doc.text)
                for i, chunk in enumerate(chunks):
                    chunk_metadata = doc.metadata.copy()
                    chunk_metadata.update({
                        'chunk_index': i,
                        'total_chunks': len(chunks),
                        'chunk_id': f"{doc.metadata['source_file']}_p{doc.metadata['page_number']}_c{i}"
                    })
                    
                    chunked_doc = Document(
                        text=chunk,
                        metadata=chunk_metadata
                    )
                    chunked_docs.append(chunked_doc)
                    
            return chunked_docs
            
        except Exception as e:
            print(f"Error processing PDF {pdf_path}: {str(e)}")
            return []
    
    def _extract_document_metadata(self, doc: fitz.Document, file_path: str) -> Dict[str, Any]:
        """Extract document-level metadata"""
        filename = os.path.basename(file_path)
        
        # Extract document info
        doc_info = doc.metadata
        
        # Identify document type from filename patterns
        doc_type = self._identify_document_type(filename)
        
        metadata = {
            'source_file': filename,
            'full_path': file_path,
            'document_type': 'specification',
            'doc_subtype': doc_type,
            'title': doc_info.get('title', ''),
            'author': doc_info.get('author', ''),
            'subject': doc_info.get('subject', ''),
            'creation_date': doc_info.get('creationDate', ''),
            'modification_date': doc_info.get('modDate', ''),
            'is_confidential': self._check_confidentiality(doc),
            'revision': self._extract_revision(doc),
            'document_number': self._extract_document_number(filename)
        }
        
        return metadata
    
    def _identify_document_type(self, filename: str) -> str:
        """Identify document subtype from filename"""
        filename_lower = filename.lower()
        
        if 'design_guideline' in filename_lower or 'guideline' in filename_lower:
            return 'design_guidelines'
        elif 'qualification' in filename_lower:
            return 'qualification_guidelines'
        elif 'qcp' in filename_lower or 'quality_control' in filename_lower:
            return 'quality_control_plan'
        elif 'specification' in filename_lower or 'spec' in filename_lower:
            return 'board_specifications'
        else:
            return 'unknown'
    
    def _identify_section(self, text: str) -> str:
        """Identify the section of the document from text content"""
        text_lower = text.lower()
        
        # Common section patterns
        if any(keyword in text_lower for keyword in ['table of contents', 'contents']):
            return 'table_of_contents'
        elif any(keyword in text_lower for keyword in ['introduction', 'overview', 'scope']):
            return 'introduction'
        elif any(keyword in text_lower for keyword in ['specification', 'requirements', 'tolerance']):
            return 'specifications'
        elif any(keyword in text_lower for keyword in ['procedure', 'process', 'method']):
            return 'procedures'
        elif any(keyword in text_lower for keyword in ['quality', 'inspection', 'test']):
            return 'quality_control'
        elif any(keyword in text_lower for keyword in ['material', 'component']):
            return 'materials'
        else:
            return 'general'
    
    def _classify_content_type(self, text: str) -> str:
        """Classify the type of content on the page"""
        if len(re.findall(r'\d+\.?\d*\s*mm|um|%', text)) > 3:
            return 'measurements'
        elif 'Figure' in text and 'Image' in text:
            return 'diagrams'
        elif '|' in text or 'Table' in text:
            return 'tables'
        elif len(text) > 500:
            return 'detailed_text'
        else:
            return 'brief_text'
    
    def _has_specifications(self, text: str) -> bool:
        """Check if text contains technical specifications"""
        spec_patterns = [
            r'\d+\.?\d*\s*(mm|um|mil|inch)',  # Dimensional tolerances
            r'±\s*\d+\.?\d*',  # Plus/minus tolerances
            r'\d+\.?\d*\s*%',  # Percentage values
            r'(minimum|maximum|min|max)\s*[:\-]?\s*\d+',  # Min/max values
        ]
        
        for pattern in spec_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        return False
    
    def _check_confidentiality(self, doc: fitz.Document) -> bool:
        """Check if document contains confidentiality notices"""
        try:
            first_page = doc[0]
            text = first_page.get_text().lower()
            
            confidential_indicators = [
                'property of apple',
                'confidential',
                'proprietary',
                'maintain this document in confidence'
            ]
            
            return any(indicator in text for indicator in confidential_indicators)
        except:
            return False
    
    def _extract_revision(self, doc: fitz.Document) -> str:
        """Extract revision information from document"""
        try:
            first_page = doc[0]
            text = first_page.get_text()
            
            # Look for revision patterns
            rev_patterns = [
                r'Rev:?\s*([A-Z]\d*)',
                r'Revision:?\s*([A-Z]\d*)',
                r'Rev\s+([A-Z]\d*)'
            ]
            
            for pattern in rev_patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    return match.group(1)
                    
            return 'Unknown'
        except:
            return 'Unknown'
    
    def _extract_document_number(self, filename: str) -> str:
        """Extract document number from filename"""
        # Pattern for Apple document numbers (e.g., 080-3649-E)
        pattern = r'(\d{3}-\d{4,5}-[A-Z]\d*)'
        match = re.search(pattern, filename)
        
        if match:
            return match.group(1)
        else:
            return filename.split('.')[0]  # Return filename without extension
    
    def get_processing_stats(self, documents: List[Document]) -> Dict[str, Any]:
        """Get statistics about processed documents"""
        if not documents:
            return {}
        
        stats = {
            'total_chunks': len(documents),
            'total_pages': len(set(doc.metadata.get('page_number', 0) for doc in documents)),
            'document_types': list(set(doc.metadata.get('doc_subtype', 'unknown') for doc in documents)),
            'sections': list(set(doc.metadata.get('section', 'unknown') for doc in documents)),
            'content_types': list(set(doc.metadata.get('content_type', 'unknown') for doc in documents)),
            'average_chunk_length': sum(len(doc.text) for doc in documents) / len(documents),
            'files_processed': list(set(doc.metadata.get('source_file', 'unknown') for doc in documents))
        }
        
        return stats