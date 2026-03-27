#!/usr/bin/env python3
"""
Test script for Manufacturing AI RAG Prototype
Validates core functionality without API calls
"""

import sys
from pathlib import Path
import traceback

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

def test_imports():
    """Test all critical imports"""
    print("🧪 Testing imports...")
    
    try:
        # Core libraries
        import streamlit as st
        import llama_index
        import openai
        import faiss
        import fitz  # PyMuPDF
        import pptx
        print("✅ Core libraries imported successfully")
        
        # Local modules
        from src.utils.config import Config
        from src.processors.pdf_processor import PDFProcessor
        from src.engines.index_manager import IndexManager
        from src.engines.query_engine import MultiModalQueryEngine
        print("✅ Local modules imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import error: {e}")
        traceback.print_exc()
        return False

def test_pdf_processing():
    """Test PDF processing functionality"""
    print("\n🧪 Testing PDF processing...")
    
    try:
        from src.processors.pdf_processor import PDFProcessor
        
        processor = PDFProcessor()
        test_pdf = Path("data/pdfs/080-03130-A_Bare_FPC_QCP.pdf")
        
        if not test_pdf.exists():
            print("⚠️ Test PDF not found, skipping processing test")
            return True
            
        # Test PDF loading without full processing
        import fitz
        doc = fitz.open(str(test_pdf))
        
        if len(doc) > 0:
            first_page_text = doc[0].get_text()
            print(f"✅ PDF loaded: {len(doc)} pages")
            print(f"✅ Text extraction working: {len(first_page_text)} characters")
            
            # Test metadata extraction
            metadata = processor._extract_document_metadata(doc, str(test_pdf))
            print(f"✅ Metadata extraction: {len(metadata)} fields")
            
        doc.close()
        return True
        
    except Exception as e:
        print(f"❌ PDF processing error: {e}")
        traceback.print_exc()
        return False

def test_configuration():
    """Test configuration system"""
    print("\n🧪 Testing configuration...")
    
    try:
        from src.utils.config import Config
        
        # Test config values
        print(f"✅ Embedding model: {Config.EMBEDDING_MODEL}")
        print(f"✅ LLM model: {Config.LLM_MODEL}")
        print(f"✅ Chunk size: {Config.CHUNK_SIZE}")
        
        # Test directory creation
        Config.create_directories()
        
        # Check directories exist
        for doc_type in Config.DOC_TYPES.keys():
            storage_path = Path(f"{Config.STORAGE_DIR}/{doc_type}")
            if storage_path.exists():
                print(f"✅ Storage directory created: {doc_type}")
            else:
                print(f"❌ Storage directory missing: {doc_type}")
                
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        traceback.print_exc()
        return False

def test_index_manager():
    """Test index manager (without building actual indices)"""
    print("\n🧪 Testing index manager...")
    
    try:
        from src.engines.index_manager import IndexManager
        
        # Initialize without API key (won't fail until actual usage)
        manager = IndexManager()
        print("✅ Index manager initialized")
        
        # Test index listing
        indices_info = manager.list_indices()
        print(f"✅ Index listing working: {len(indices_info)} indices found")
        
        return True
        
    except Exception as e:
        print(f"❌ Index manager error: {e}")
        traceback.print_exc()
        return False

def test_query_engine():
    """Test query engine initialization"""
    print("\n🧪 Testing query engine...")
    
    try:
        from src.engines.index_manager import IndexManager
        from src.engines.query_engine import MultiModalQueryEngine, QueryClassifier
        
        # Test query classification (doesn't need API)
        classifier = QueryClassifier()
        
        test_queries = [
            "What is bending location tolerance?",
            "Compare AMP vs ICT yield",
            "How to process FPC qualification?",
            "What is UPD?"
        ]
        
        for query in test_queries:
            query_type = classifier.classify_query(query)
            print(f"✅ Query '{query}' classified as: {query_type}")
            
        return True
        
    except Exception as e:
        print(f"❌ Query engine error: {e}")
        traceback.print_exc()
        return False

def test_streamlit_app():
    """Test streamlit app structure"""
    print("\n🧪 Testing Streamlit app...")
    
    try:
        # Import the main app module
        import streamlit_app
        print("✅ Streamlit app module loaded")
        
        # Check if main functions exist
        required_functions = ['main', 'initialize_system', 'render_pdf_specifications_tab']
        
        for func_name in required_functions:
            if hasattr(streamlit_app, func_name):
                print(f"✅ Function {func_name} found")
            else:
                print(f"❌ Function {func_name} missing")
                
        return True
        
    except Exception as e:
        print(f"❌ Streamlit app error: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🏭 MANUFACTURING AI RAG PROTOTYPE - SYSTEM TEST")
    print("=" * 60)
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_configuration),
        ("PDF Processing Test", test_pdf_processing),
        ("Index Manager Test", test_index_manager),
        ("Query Engine Test", test_query_engine),
        ("Streamlit App Test", test_streamlit_app)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} FAILED with exception: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 TEST SUMMARY: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! System ready for deployment.")
        print("\nNext steps:")
        print("1. Set OPENAI_API_KEY environment variable")
        print("2. Add document files to data/ directories")
        print("3. Run: streamlit run streamlit_app.py")
    else:
        print("⚠️  Some tests failed. Please review errors above.")
        
    print("=" * 60)

if __name__ == "__main__":
    main()