#!/usr/bin/env python3
"""
Final evaluation with precision fixes applied
"""

import sys
import json
import pandas as pd
from datetime import datetime
from precision_fix import PrecisionRAGSystem

def evaluate_answer(question: str, expected: str, actual: str) -> tuple:
    """Simple but effective evaluation"""
    expected_lower = expected.lower()
    actual_lower = actual.lower()
    
    # Check for "not found" responses
    if any(phrase in actual_lower for phrase in [
        'not found', 'not explicitly', 'not mentioned', 
        'not available', 'not in the provided context', 'cannot find'
    ]):
        return 0.0, 'NOT_FOUND'
    
    # Extract key terms from expected answer
    expected_words = set(expected_lower.split())
    actual_words = set(actual_lower.split())
    
    # Count matches
    matches = len(expected_words.intersection(actual_words))
    total_expected = len(expected_words)
    
    if total_expected == 0:
        return 0.5, 'UNCLEAR'
    
    match_ratio = matches / total_expected
    
    # Special handling for measurements
    if any(unit in expected_lower for unit in ['mm', 'um', 'mil', '%']):
        # For measurements, look for exact numerical matches
        import re
        expected_numbers = re.findall(r'\\d+\\.?\\d*', expected)
        actual_numbers = re.findall(r'\\d+\\.?\\d*', actual)
        
        if expected_numbers and actual_numbers:
            for exp_num in expected_numbers:
                if any(abs(float(exp_num) - float(act_num)) < 0.01 for act_num in actual_numbers):
                    match_ratio = max(match_ratio, 0.9)  # High score for correct number
                    break
    
    # Determine status
    if match_ratio >= 0.8:
        return match_ratio, 'CORRECT'
    elif match_ratio >= 0.4:
        return match_ratio, 'PARTIALLY_CORRECT'
    else:
        return match_ratio, 'WRONG'

def run_final_evaluation():
    """Run complete evaluation with precision fixes"""
    print("=" * 80)
    print("FINAL EVALUATION - Precision-Enhanced RAG System")
    print("=" * 80)
    
    # Load Q&A pairs
    df = pd.read_excel('/home/guilinzhang/allProjects/mfg-ai-platform/docs/QA_pdf_2026_03_26.xlsx')
    
    qa_pairs = []
    for i, row in df.iterrows():
        if i == 0:  # Skip header
            continue
        question = str(row.iloc[0]).strip()
        answer = str(row.iloc[1]).strip()
        if question and answer and question != 'Question':
            qa_pairs.append({'question': question, 'expected': answer})
    
    print(f"Loaded {len(qa_pairs)} Q&A pairs")
    
    # Initialize precision RAG system
    rag = PrecisionRAGSystem()
    if not rag.load_index("improved_rag_index"):
        print("ERROR: Could not load index")
        return
    
    # Run evaluation
    results = []
    
    for i, qa in enumerate(qa_pairs, 1):
        print(f"\\n{'='*60}")
        print(f"Question {i}: {qa['question']}")
        print(f"Expected: {qa['expected']}")
        print("-" * 60)
        
        # Get answer
        result = rag.query(qa['question'])
        
        if result['error']:
            score, status = 0.0, 'ERROR'
            print(f"ERROR: {result['error']}")
        else:
            print(f"Actual: {result['answer']}")
            score, status = evaluate_answer(qa['question'], qa['expected'], result['answer'])
        
        print(f"Evaluation: {status} (Score: {score:.2f})")
        
        results.append({
            'id': i,
            'question': qa['question'],
            'expected': qa['expected'],
            'actual': result['answer'] if not result['error'] else f"ERROR: {result['error']}",
            'score': score,
            'status': status,
            'sources': result.get('sources', [])
        })
        
        print("=" * 60)
    
    # Calculate summary statistics
    total = len(results)
    correct = sum(1 for r in results if r['status'] == 'CORRECT')
    partial = sum(1 for r in results if r['status'] == 'PARTIALLY_CORRECT')
    wrong = sum(1 for r in results if r['status'] == 'WRONG')
    not_found = sum(1 for r in results if r['status'] == 'NOT_FOUND')
    errors = sum(1 for r in results if r['status'] == 'ERROR')
    
    # Weighted accuracy
    weighted_score = sum(r['score'] for r in results) / total
    weighted_accuracy = weighted_score * 100
    
    # Print summary
    print("\\n" + "=" * 80)
    print("FINAL EVALUATION SUMMARY")
    print("=" * 80)
    print(f"Total Questions: {total}")
    print(f"Correct: {correct} ({correct/total*100:.1f}%)")
    print(f"Partially Correct: {partial} ({partial/total*100:.1f}%)")
    print(f"Wrong: {wrong} ({wrong/total*100:.1f}%)")
    print(f"Not Found: {not_found} ({not_found/total*100:.1f}%)")
    if errors > 0:
        print(f"Errors: {errors} ({errors/total*100:.1f}%)")
    print()
    print(f"**WEIGHTED ACCURACY: {weighted_accuracy:.1f}%**")
    
    # Compare with previous results
    print("\\nComparison with Previous Results:")
    print(f"  Baseline (PyMuPDF):        11.1%")
    print(f"  Improved (PyMuPDF4LLM):    55.6%")
    print(f"  Final (Precision-Enhanced): {weighted_accuracy:.1f}%")
    print(f"  Improvement: +{weighted_accuracy - 55.6:.1f} percentage points")
    
    # Target analysis
    if weighted_accuracy >= 80.0:
        print("\\n🎯 **SUCCESS! Target of 80%+ accuracy achieved!**")
    else:
        needed = 80.0 - weighted_accuracy
        print(f"\\n⚠️  Need {needed:.1f} more percentage points to reach 80% target")
    
    print("=" * 80)
    
    # Save detailed results
    summary = {
        'evaluation_date': datetime.now().isoformat(),
        'total_questions': total,
        'correct': correct,
        'partially_correct': partial,
        'wrong': wrong,
        'not_found': not_found,
        'errors': errors,
        'weighted_accuracy_percent': weighted_accuracy,
        'method': 'precision_enhanced_rag',
        'results': results,
        'comparison': {
            'baseline': 11.1,
            'improved': 55.6,
            'final': weighted_accuracy,
            'improvement_from_baseline': weighted_accuracy - 11.1,
            'improvement_from_improved': weighted_accuracy - 55.6
        }
    }
    
    with open('final_evaluation_results.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\\nDetailed results saved to: final_evaluation_results.json")
    
    return weighted_accuracy

if __name__ == "__main__":
    final_accuracy = run_final_evaluation()
    
    # Exit with success if target achieved
    if final_accuracy >= 80.0:
        print("\\n✅ Target achieved! Manufacturing RAG prototype is ready for client demo.")
        sys.exit(0)
    else:
        print(f"\\n❌ Target not reached. Need {80.0 - final_accuracy:.1f} more percentage points.")
        sys.exit(1)