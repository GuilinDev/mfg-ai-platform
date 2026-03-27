#!/usr/bin/env python3
"""
Quick test without BGE model - focus on other improvements
"""

import sys
from advanced_rag_system import AdvancedRAGSystem

def test_quick():
    """Quick test with standard embeddings but advanced chunking"""
    print("QUICK TEST - Advanced chunking + Hybrid search")
    print("=" * 60)
    
    # Initialize with standard embeddings but advanced features
    rag = AdvancedRAGSystem(chunk_size=1200, chunk_overlap=300, use_bge=False)
    
    # Check if we can load existing index
    if rag.load_indices("advanced_rag_index"):
        print("Loaded existing advanced index")
    else:
        print("Building new advanced index...")
        rag.process_pdfs("/home/guilinzhang/allProjects/mfg-ai-platform/docs")
        rag.build_indices()
        rag.save_indices("advanced_rag_index")
    
    # Test one key question
    question = "What is bending location tolerance?"
    print(f"\\nTesting: {question}")
    
    result = rag.query(question, use_hybrid=True)
    print(f"\\nAnswer: {result['answer']}")
    print(f"Method: {result['method']}")
    print(f"Sources: {len(result['sources'])}")
    
    return result

if __name__ == "__main__":
    test_quick()