#!/usr/bin/env python3
"""
Quick test of the advanced RAG system on a few key questions
"""

import sys
from advanced_rag_system import AdvancedRAGSystem

def test_advanced_rag():
    """Test advanced RAG on key failing questions"""
    print("=" * 70)
    print("TESTING ADVANCED RAG SYSTEM")
    print("=" * 70)
    
    # Initialize system
    print("Initializing advanced RAG system...")
    rag = AdvancedRAGSystem(chunk_size=1200, chunk_overlap=300, use_bge=True)
    
    # Build indices
    print("Building advanced indices...")
    rag.process_pdfs("/home/guilinzhang/allProjects/mfg-ai-platform/docs")
    rag.build_indices()
    
    # Test key questions that were failing
    test_questions = [
        "What is bending location tolerance?",
        "What is UPD?", 
        "What is FPC design guideline of De-cap?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\\n{'='*50}")
        print(f"Test {i}: {question}")
        print(f"{'='*50}")
        
        # Test both hybrid and vector-only
        print("\\n--- Hybrid Search ---")
        result_hybrid = rag.query(question, use_hybrid=True)
        print(f"Answer: {result_hybrid['answer'][:500]}...")
        print(f"Sources: {len(result_hybrid['sources'])} documents")
        
        print("\\n--- Vector Only ---")
        result_vector = rag.query(question, use_hybrid=False)
        print(f"Answer: {result_vector['answer'][:500]}...")
        print(f"Sources: {len(result_vector['sources'])} documents")
    
    print("\\nTesting completed!")

if __name__ == "__main__":
    test_advanced_rag()