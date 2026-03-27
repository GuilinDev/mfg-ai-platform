#!/usr/bin/env python3
"""
Test script to verify Groq integration works
"""
import sys
import os
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from src.utils.config import Config
from src.processors.pdf_processor import PDFProcessor
from src.engines.index_manager import IndexManager
from src.engines.query_engine import MultiModalQueryEngine

def test_config():
    """Test configuration"""
    print("=== Testing Configuration ===")
    print(f"Groq API Key configured: {bool(Config.get_groq_api_key())}")
    print(f"LLM Model: {Config.LLM_MODEL}")
    print(f"Data directory exists: {os.path.exists(Config.DATA_DIR)}")
    print(f"Data directory: {Config.DATA_DIR}")
    
    # List PDF files
    pdf_files = list(Path(Config.DATA_DIR).glob("*.pdf"))
    print(f"PDF files found: {len(pdf_files)}")
    for pdf in pdf_files[:3]:  # Show first 3
        print(f"  - {pdf.name}")
    if len(pdf_files) > 3:
        print(f"  ... and {len(pdf_files)-3} more")
    print()

def test_embedding():
    """Test embedding functionality"""
    print("=== Testing Embeddings ===")
    try:
        index_manager = IndexManager()
        print("✓ Index manager initialized successfully")
        print(f"Using local embeddings: {index_manager.use_local_embeddings}")
        print()
    except Exception as e:
        print(f"✗ Failed to initialize index manager: {e}")
        return False
    return True

def test_pdf_processing():
    """Test PDF processing"""
    print("=== Testing PDF Processing ===")
    try:
        processor = PDFProcessor()
        pdf_files = list(Path(Config.DATA_DIR).glob("*.pdf"))
        
        if not pdf_files:
            print("No PDF files to test with")
            return False
            
        # Test with first PDF file
        test_pdf = pdf_files[0]
        print(f"Processing: {test_pdf.name}")
        
        documents = processor.process_file(str(test_pdf))
        print(f"✓ Processed {len(documents)} document chunks")
        
        if documents:
            stats = processor.get_processing_stats(documents)
            print(f"  Pages: {stats['total_pages']}")
            print(f"  Chunks: {stats['total_chunks']}")
            print(f"  Avg chunk length: {stats['average_chunk_length']:.0f} chars")
            print(f"  Sections: {stats['sections']}")
        print()
        return documents
        
    except Exception as e:
        print(f"✗ PDF processing failed: {e}")
        return False

def test_index_building(documents):
    """Test index building"""
    print("=== Testing Index Building ===")
    try:
        index_manager = IndexManager()
        
        # Build index with subset of documents (faster test)
        test_docs = documents[:10]  # Use first 10 chunks
        print(f"Building index with {len(test_docs)} documents...")
        
        index = index_manager.build_index(test_docs, 'test_specification', force_rebuild=True)
        print("✓ Index built successfully")
        
        # Test retrieval
        print("Testing retrieval...")
        test_index = index_manager.get_index('test_specification')
        if test_index:
            print("✓ Index retrieval successful")
            return index
        else:
            print("✗ Index retrieval failed")
            return False
            
    except Exception as e:
        print(f"✗ Index building failed: {e}")
        return False

def test_query_engine(index_manager):
    """Test query engine with Groq"""
    print("=== Testing Query Engine ===")
    try:
        query_engine = MultiModalQueryEngine(index_manager)
        print("✓ Query engine initialized")
        
        # Test a simple query
        test_query = "What is bending location tolerance?"
        print(f"Testing query: '{test_query}'")
        
        response = query_engine.query_specifications(test_query)
        
        if response.error:
            print(f"✗ Query failed: {response.error}")
            return False
        else:
            print("✓ Query executed successfully")
            print(f"  Answer: {response.answer[:200]}...")
            print(f"  Confidence: {response.confidence:.2f}")
            print(f"  Processing time: {response.processing_time:.2f}s")
            print(f"  Sources: {len(response.sources)}")
            return True
            
    except Exception as e:
        print(f"✗ Query engine test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Manufacturing AI RAG - Groq Integration Test")
    print("=" * 50)
    
    # Test configuration
    test_config()
    
    # Test embeddings
    if not test_embedding():
        return
    
    # Test PDF processing
    documents = test_pdf_processing()
    if not documents:
        return
    
    # Test index building
    index_manager = IndexManager()
    index = test_index_building(documents)
    if not index:
        return
    
    # Test query engine
    success = test_query_engine(index_manager)
    
    if success:
        print("🎉 All tests passed! Groq integration is working.")
    else:
        print("❌ Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()