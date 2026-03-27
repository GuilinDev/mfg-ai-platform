#!/usr/bin/env python3
"""
Baseline evaluation of current PDF parsing quality
Tests all 10 Q&A pairs from the Excel file
"""
import os
import sys
import pandas as pd
import json
from pathlib import Path
from simple_rag import SimpleRAGSystem

# Q&A pairs from Excel file
QA_PAIRS = [
    {
        "question": "What is bending location tolerance?",
        "expected_answer": "0.300 mm"
    },
    {
        "question": "What is FPC design guideline of De-cap ?",
        "expected_answer": "When a flex needs to have different numbers of copper layers for different regions of the same flex, de-cap isrequired at the layer transition to cut away the excess layers. For example, a flex may have two layers of copper forhalf and be only one layer for the other half, with the layer transition being the area for de-cap. The cut awayprocess is done with either a pre-punch of PI and bonding sheet (usually only for 3+ layer flexes) before laminationor with a laser after lamination"
    },
    {
        "question": "What is the bonding adhesive patch back?",
        "expected_answer": "After drill hole plasma and wet desmear, the adhesive between 2 FCCL will has etch back. This is to ensure the palm and wet desmear are effective to remove adhesive."
    },
    {
        "question": "What is the LPI or Solder mask thickness ?",
        "expected_answer": "4-39um"
    },
    {
        "question": "What is dimension of EMI shield to coverlay edge ?",
        "expected_answer": "0.400 mm"
    },
    {
        "question": "What is FPC reflow test acceptance criteria?",
        "expected_answer": "function, SUS stiffener resistance, cosmetics, BVH peel fir multi-layer FPC, cross-section"
    },
    {
        "question": "What is laser drilling quality control plan ?",
        "expected_answer": "visual defects, alignment, hole size...."
    },
    {
        "question": "What is UPD?",
        "expected_answer": "Unit Process Development"
    },
    {
        "question": "What is CQRA of FPC line qualification.",
        "expected_answer": "Thermal cycle\n• Hot Oil\n• Reflow\n• Insulation resistance (via to via)\n• Thermal stability (Solder shock) fo"
    }
]

def evaluate_answer(question, expected, actual):
    """
    Evaluate if the actual answer is correct
    Returns: correct, partially_correct, or wrong
    """
    actual_lower = actual.lower()
    expected_lower = expected.lower()
    
    # Extract key terms and values from expected answer
    if "0.300 mm" in expected:
        return "correct" if "0.300" in actual and "mm" in actual else "wrong"
    elif "4-39um" in expected:
        return "correct" if ("4-39" in actual or ("4" in actual and "39" in actual)) and "um" in actual else "wrong"
    elif "0.400 mm" in expected:
        return "correct" if "0.400" in actual and "mm" in actual else "wrong"
    elif "unit process development" in expected_lower:
        return "correct" if "unit process development" in actual_lower else "wrong"
    elif "de-cap" in expected_lower:
        key_terms = ["de-cap", "layer transition", "copper layers", "laser", "lamination"]
        matches = sum(1 for term in key_terms if term in actual_lower)
        if matches >= 3:
            return "correct"
        elif matches >= 2:
            return "partially_correct"
        else:
            return "wrong"
    elif "adhesive" in expected_lower and "etch back" in expected_lower:
        key_terms = ["adhesive", "etch back", "desmear", "plasma"]
        matches = sum(1 for term in key_terms if term in actual_lower)
        if matches >= 2:
            return "correct"
        elif matches >= 1:
            return "partially_correct"
        else:
            return "wrong"
    elif "thermal cycle" in expected_lower:
        key_terms = ["thermal cycle", "hot oil", "reflow", "insulation resistance"]
        matches = sum(1 for term in key_terms if term in actual_lower)
        if matches >= 2:
            return "correct"
        elif matches >= 1:
            return "partially_correct"
        else:
            return "wrong"
    else:
        # For other questions, do partial string matching
        expected_words = set(expected_lower.split())
        actual_words = set(actual_lower.split())
        common_words = expected_words.intersection(actual_words)
        overlap_ratio = len(common_words) / len(expected_words) if expected_words else 0
        
        if overlap_ratio >= 0.5:
            return "correct"
        elif overlap_ratio >= 0.3:
            return "partially_correct"
        else:
            return "wrong"

def run_baseline_evaluation():
    """Run baseline evaluation with current PDF parsing"""
    print("=" * 60)
    print("BASELINE EVALUATION - Current PDF Parsing Quality")
    print("=" * 60)
    
    # Initialize RAG system
    rag = SimpleRAGSystem()
    
    # Load existing index or build new one
    if not rag.load_index("simple_rag_index"):
        print("Building new index...")
        rag.process_pdfs("/home/guilinzhang/allProjects/mfg-ai-platform/docs")
        rag.build_index()
        rag.save_index("simple_rag_index")
    
    results = []
    scores = {"correct": 0, "partially_correct": 0, "wrong": 0}
    
    for i, qa in enumerate(QA_PAIRS, 1):
        print(f"\n{'='*50}")
        print(f"Question {i}: {qa['question']}")
        print(f"Expected: {qa['expected_answer']}")
        print("-" * 50)
        
        # Query the system
        result = rag.query(qa['question'])
        actual_answer = result['answer'] if not result['error'] else f"Error: {result['error']}"
        
        # Evaluate
        evaluation = evaluate_answer(qa['question'], qa['expected_answer'], actual_answer)
        scores[evaluation] += 1
        
        print(f"Actual: {actual_answer}")
        print(f"Evaluation: {evaluation.upper()}")
        
        # Show sources
        if result['sources']:
            print("Sources:")
            for j, source in enumerate(result['sources'][:3], 1):
                print(f"  {j}. {source['file']} (Page {source['page']}) - Score: {source['score']:.3f}")
        
        results.append({
            "question_num": i,
            "question": qa['question'],
            "expected_answer": qa['expected_answer'],
            "actual_answer": actual_answer,
            "evaluation": evaluation,
            "sources": result['sources'][:3] if result['sources'] else []
        })
    
    # Calculate final score
    total = len(QA_PAIRS)
    correct_pct = (scores['correct'] / total) * 100
    partial_pct = (scores['partially_correct'] / total) * 100
    wrong_pct = (scores['wrong'] / total) * 100
    
    print("\n" + "=" * 60)
    print("BASELINE RESULTS SUMMARY")
    print("=" * 60)
    print(f"Total Questions: {total}")
    print(f"Correct: {scores['correct']} ({correct_pct:.1f}%)")
    print(f"Partially Correct: {scores['partially_correct']} ({partial_pct:.1f}%)")
    print(f"Wrong: {scores['wrong']} ({wrong_pct:.1f}%)")
    print(f"Overall Accuracy: {correct_pct + partial_pct * 0.5:.1f}%")
    print("=" * 60)
    
    # Save detailed results
    with open("baseline_evaluation_results.json", "w") as f:
        json.dump({
            "summary": scores,
            "overall_accuracy": correct_pct + partial_pct * 0.5,
            "detailed_results": results
        }, f, indent=2)
    
    print("Detailed results saved to: baseline_evaluation_results.json")
    return scores, results

if __name__ == "__main__":
    run_baseline_evaluation()