#!/usr/bin/env python3
"""
Focused diagnosis: Check the specific failing Q&A cases
"""

import sys
import pandas as pd
from improved_rag_system import ImprovedRAGSystem

def diagnose_failures():
    """Diagnose specific failure cases"""
    print("DIAGNOSING FAILURE CASES")
    print("=" * 50)
    
    # Load existing system
    rag = ImprovedRAGSystem()
    if not rag.load_index("improved_rag_index"):
        print("Could not load existing index")
        return
    
    # Questions that are failing
    failing_cases = [
        {
            'question': "What is bending location tolerance?",
            'expected': "0.300 mm",
            'current_status': "PARTIALLY_CORRECT"
        },
        {
            'question': "What is FPC design guideline of De-cap?", 
            'expected': "When a flex needs to have different numbers of copper layers for different regions of the same flex, de-cap is required at the layer transition to cut away the excess layers...",
            'current_status': "WRONG"
        },
        {
            'question': "What is the bonding adhesive patch back?",
            'expected': "After drill hole plasma and wet desmear, the adhesive between 2 FCCL will has etch back...",
            'current_status': "WRONG"
        },
        {
            'question': "What is UPD?",
            'expected': "Unit Process Development", 
            'current_status': "PARTIALLY_CORRECT"
        }
    ]
    
    for i, case in enumerate(failing_cases, 1):
        print(f"\\n=== CASE {i}: {case['question']} ===")
        print(f"Expected: {case['expected'][:100]}...")
        print(f"Current Status: {case['current_status']}")
        
        # Get current answer
        result = rag.query(case['question'], top_k=5)
        print(f"\\nCurrent Answer: {result['answer'][:200]}...")
        
        # Check what documents were retrieved
        print(f"\\nRetrieved {len(result['sources'])} sources:")
        for j, source in enumerate(result['sources'][:3], 1):
            print(f"  {j}. {source['file']} (score: {source['score']:.3f})")
            print(f"     Preview: {source['text_preview'][:150]}...")
        
        # Try different search terms
        print(f"\\nTesting search variations:")
        if "tolerance" in case['question'].lower():
            test_queries = ["bending location tolerance", "0.300 mm", "bending tolerance"]
        elif "de-cap" in case['question'].lower():
            test_queries = ["de-cap", "layer transition", "copper layers flex"]
        elif "bonding adhesive" in case['question'].lower():
            test_queries = ["bonding adhesive patch back", "drill hole plasma", "wet desmear"]
        elif "upd" in case['question'].lower():
            test_queries = ["UPD", "Unit Process Development", "qualification process"]
        else:
            test_queries = [case['question']]
        
        for query in test_queries:
            search_results = rag.search(query, top_k=3)
            if search_results:
                best_result = search_results[0]
                print(f"  '{query}' -> {best_result['metadata']['source_file']} (score: {best_result['score']:.3f})")
                # Check if expected answer appears in the text
                if any(word in best_result['text'].lower() for word in case['expected'].lower().split()[:3]):
                    print(f"    ✓ Contains expected content")
                else:
                    print(f"    ✗ Missing expected content")
            else:
                print(f"  '{query}' -> No results")
        
        print("-" * 60)

if __name__ == "__main__":
    diagnose_failures()