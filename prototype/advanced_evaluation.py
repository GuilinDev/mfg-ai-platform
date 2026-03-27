#!/usr/bin/env python3
"""
Advanced evaluation script for the improved RAG system
Tests all Q&A pairs and provides detailed analysis
"""

import sys
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import re

# Import our advanced system
from advanced_rag_system import AdvancedRAGSystem

class AdvancedEvaluator:
    """Advanced evaluation with detailed analysis"""
    
    def __init__(self):
        # Load Q&A pairs
        self.qa_pairs = self._load_qa_pairs()
        self.results = []
        
    def _load_qa_pairs(self) -> List[Dict[str, str]]:
        """Load Q&A pairs from Excel file"""
        df = pd.read_excel('/home/guilinzhang/allProjects/mfg-ai-platform/docs/QA_pdf_2026_03_26.xlsx')
        
        qa_pairs = []
        for i, row in df.iterrows():
            if i == 0:  # Skip header row
                continue
            
            question = str(row.iloc[0]).strip()
            answer = str(row.iloc[1]).strip()
            
            # Skip if either is empty or just headers
            if question and answer and question != 'Question' and answer != 'Answer':
                qa_pairs.append({
                    'id': i,
                    'question': question,
                    'expected_answer': answer
                })
        
        return qa_pairs
    
    def _evaluate_answer(self, question: str, expected: str, actual: str) -> Dict[str, Any]:
        """Evaluate answer quality with detailed scoring"""
        evaluation = {
            'question': question,
            'expected': expected,
            'actual': actual,
            'score': 0,
            'status': 'WRONG',
            'analysis': {},
            'reasons': []
        }
        
        expected_lower = expected.lower()
        actual_lower = actual.lower()
        
        # Check for "not found" or error responses
        if any(phrase in actual_lower for phrase in [
            'not found in', 'cannot find', 'not explicitly', 
            'not mentioned', 'not available', 'not in the provided context'
        ]):
            evaluation['status'] = 'NOT_FOUND'
            evaluation['reasons'].append('System could not find the information')
            return evaluation
        
        # Extract key information for different question types
        analysis = self._analyze_by_question_type(question, expected, actual)
        evaluation['analysis'] = analysis
        
        # Scoring based on analysis
        if analysis['question_type'] == 'measurement':
            score = self._score_measurement(analysis)
        elif analysis['question_type'] == 'definition':
            score = self._score_definition(analysis)
        elif analysis['question_type'] == 'process_list':
            score = self._score_process_list(analysis)
        else:
            score = self._score_general(expected_lower, actual_lower)
        
        evaluation['score'] = score
        
        # Determine status
        if score >= 0.9:
            evaluation['status'] = 'CORRECT'
        elif score >= 0.5:
            evaluation['status'] = 'PARTIALLY_CORRECT'
        else:
            evaluation['status'] = 'WRONG'
        
        return evaluation
    
    def _analyze_by_question_type(self, question: str, expected: str, actual: str) -> Dict[str, Any]:
        """Analyze answer based on question type"""
        question_lower = question.lower()
        
        analysis = {
            'question_type': 'general',
            'expected_values': [],
            'actual_values': [],
            'key_terms_found': [],
            'missing_terms': []
        }
        
        # Identify question type
        if any(word in question_lower for word in ['tolerance', 'thickness', 'dimension', 'size']):
            analysis['question_type'] = 'measurement'
            analysis['expected_values'] = self._extract_measurements(expected)
            analysis['actual_values'] = self._extract_measurements(actual)
            
        elif any(word in question_lower for word in ['what is', 'define', 'definition']):
            if any(word in expected.lower() for word in ['process', 'steps', 'criteria', 'plan']):
                analysis['question_type'] = 'process_list'
                analysis['expected_items'] = self._extract_list_items(expected)
                analysis['actual_items'] = self._extract_list_items(actual)
            else:
                analysis['question_type'] = 'definition'
        
        # Extract key terms for all types
        key_terms = self._extract_key_terms(expected)
        analysis['key_terms'] = key_terms
        analysis['key_terms_found'] = [term for term in key_terms if term.lower() in actual.lower()]
        analysis['missing_terms'] = [term for term in key_terms if term.lower() not in actual.lower()]
        
        return analysis
    
    def _extract_measurements(self, text: str) -> List[str]:
        """Extract measurements and their units"""
        patterns = [
            r'\d+\.?\d*\s*(mm|um|mil|µm|%|ohm|°c|mhz|khz|v|a|w)',
            r'\d+\.?\d*\s*-\s*\d+\.?\d*\s*(mm|um|mil|µm|%)',
            r'±\s*\d+\.?\d*\s*(mm|um|mil|µm|%)'
        ]
        
        measurements = []
        for pattern in patterns:
            matches = re.findall(pattern, text.lower(), re.IGNORECASE)
            measurements.extend(matches)
        
        return list(set(measurements))
    
    def _extract_list_items(self, text: str) -> List[str]:
        """Extract list items from text"""
        # Split by common separators
        items = []
        
        # Try bullet points first
        if '•' in text:
            items = [item.strip() for item in text.split('•') if item.strip()]
        elif ',' in text:
            items = [item.strip() for item in text.split(',') if item.strip()]
        else:
            # Try to extract individual words/phrases
            words = text.split()
            items = [word for word in words if len(word) > 2]
        
        return items[:10]  # Limit to avoid noise
    
    def _extract_key_terms(self, text: str) -> List[str]:
        """Extract key technical terms"""
        # Technical terms that are likely important
        tech_patterns = [
            r'\b[A-Z]{2,5}\b',  # Acronyms like UPD, LPI, EMI
            r'\d+\.?\d*\s*(mm|um|mil|µm|%)',  # Measurements
            r'\b(tolerance|thickness|dimension|process|criteria|test|quality|control|plan)\b'
        ]
        
        key_terms = []
        for pattern in tech_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if isinstance(matches[0], tuple):  # If pattern returns tuples
                matches = [match[0] for match in matches]
            key_terms.extend(matches)
        
        return list(set(key_terms))
    
    def _score_measurement(self, analysis: Dict[str, Any]) -> float:
        """Score measurement-based answers"""
        expected_measurements = analysis['expected_values'] 
        actual_measurements = analysis['actual_values']
        
        if not expected_measurements:
            return 0.5  # No clear measurement to compare
        
        if not actual_measurements:
            return 0.0  # No measurement found in answer
        
        # Check for exact matches
        exact_matches = 0
        for expected in expected_measurements:
            if any(self._measurements_match(expected, actual) for actual in actual_measurements):
                exact_matches += 1
        
        # Score based on proportion of measurements found
        score = exact_matches / len(expected_measurements)
        
        # Bonus for finding key terms
        key_terms_score = len(analysis['key_terms_found']) / max(len(analysis['key_terms']), 1)
        
        return min(score + (key_terms_score * 0.2), 1.0)
    
    def _measurements_match(self, measurement1: str, measurement2: str) -> bool:
        """Check if two measurements are equivalent"""
        # Extract numbers and units
        m1_nums = re.findall(r'\d+\.?\d*', measurement1)
        m1_units = re.findall(r'[a-z%]+', measurement1.lower())
        
        m2_nums = re.findall(r'\d+\.?\d*', measurement2)
        m2_units = re.findall(r'[a-z%]+', measurement2.lower())
        
        # Check if numbers are close and units match
        if m1_units == m2_units and m1_nums and m2_nums:
            try:
                n1, n2 = float(m1_nums[0]), float(m2_nums[0])
                return abs(n1 - n2) / max(n1, n2) < 0.1  # Within 10%
            except ValueError:
                pass
        
        return measurement1.lower() in measurement2.lower() or measurement2.lower() in measurement1.lower()
    
    def _score_definition(self, analysis: Dict[str, Any]) -> float:
        """Score definition-based answers"""
        key_terms_found = len(analysis['key_terms_found'])
        total_key_terms = len(analysis['key_terms'])
        
        if total_key_terms == 0:
            return 0.5
        
        return min(key_terms_found / total_key_terms, 1.0)
    
    def _score_process_list(self, analysis: Dict[str, Any]) -> float:
        """Score process list answers"""
        expected_items = analysis.get('expected_items', [])
        actual_items = analysis.get('actual_items', [])
        
        if not expected_items:
            return self._score_definition(analysis)
        
        matches = 0
        for expected_item in expected_items:
            if any(expected_item.lower() in actual_item.lower() for actual_item in actual_items):
                matches += 1
        
        return min(matches / len(expected_items), 1.0)
    
    def _score_general(self, expected_lower: str, actual_lower: str) -> float:
        """General scoring for other answer types"""
        # Simple similarity scoring
        expected_words = set(expected_lower.split())
        actual_words = set(actual_lower.split())
        
        if not expected_words:
            return 0.0
        
        intersection = expected_words.intersection(actual_words)
        return len(intersection) / len(expected_words)
    
    def run_evaluation(self, rag_system: AdvancedRAGSystem) -> Dict[str, Any]:
        """Run complete evaluation"""
        print(f"Starting advanced evaluation with {len(self.qa_pairs)} Q&A pairs...")
        print("=" * 70)
        
        for i, qa in enumerate(self.qa_pairs, 1):
            print(f"Question {i}: {qa['question']}")
            print(f"Expected: {qa['expected_answer']}")
            print("-" * 60)
            
            # Get answer from RAG system
            result = rag_system.query(qa['question'], top_k=5, use_hybrid=True)
            
            if result['error']:
                print(f"Error: {result['error']}")
                evaluation = {
                    'question': qa['question'],
                    'expected': qa['expected_answer'], 
                    'actual': f"ERROR: {result['error']}",
                    'score': 0,
                    'status': 'ERROR'
                }
            else:
                print(f"Actual: {result['answer']}")
                evaluation = self._evaluate_answer(
                    qa['question'],
                    qa['expected_answer'],
                    result['answer']
                )
                
                # Add source information
                evaluation['sources'] = result['sources']
                evaluation['method'] = result['method']
                evaluation['query_variants'] = result.get('query_variants', [])
            
            print(f"Evaluation: {evaluation['status']} (Score: {evaluation['score']:.2f})")
            
            if evaluation.get('analysis'):
                analysis = evaluation['analysis']
                print(f"Analysis: Type={analysis['question_type']}, Key terms found={len(analysis.get('key_terms_found', []))}/{len(analysis.get('key_terms', []))}")
            
            print("=" * 70)
            
            self.results.append({
                'id': qa['id'],
                **evaluation
            })
        
        return self._calculate_summary()
    
    def _calculate_summary(self) -> Dict[str, Any]:
        """Calculate summary statistics"""
        if not self.results:
            return {}
        
        total = len(self.results)
        correct = sum(1 for r in self.results if r['status'] == 'CORRECT')
        partial = sum(1 for r in self.results if r['status'] == 'PARTIALLY_CORRECT')  
        wrong = sum(1 for r in self.results if r['status'] == 'WRONG')
        not_found = sum(1 for r in self.results if r['status'] == 'NOT_FOUND')
        errors = sum(1 for r in self.results if r['status'] == 'ERROR')
        
        # Weighted accuracy (correct=1.0, partial=0.5, wrong=0.0)
        weighted_score = sum(r['score'] for r in self.results) / total
        
        summary = {
            'total_questions': total,
            'correct': correct,
            'partially_correct': partial,
            'wrong': wrong,
            'not_found': not_found,
            'errors': errors,
            'accuracy_percent': (correct / total) * 100,
            'partial_accuracy_percent': ((correct + partial) / total) * 100,
            'weighted_accuracy_percent': weighted_score * 100,
            'results': self.results,
            'timestamp': datetime.now().isoformat()
        }
        
        return summary
    
    def print_summary(self, summary: Dict[str, Any]):
        """Print evaluation summary"""
        print("\\n" + "=" * 70)
        print("ADVANCED EVALUATION RESULTS SUMMARY")
        print("=" * 70)
        print(f"Total Questions: {summary['total_questions']}")
        print(f"Correct: {summary['correct']} ({summary['accuracy_percent']:.1f}%)")
        print(f"Partially Correct: {summary['partially_correct']} ({summary['partially_correct']/summary['total_questions']*100:.1f}%)")
        print(f"Wrong: {summary['wrong']} ({summary['wrong']/summary['total_questions']*100:.1f}%)")
        print(f"Not Found: {summary['not_found']} ({summary['not_found']/summary['total_questions']*100:.1f}%)")
        if summary['errors'] > 0:
            print(f"Errors: {summary['errors']} ({summary['errors']/summary['total_questions']*100:.1f}%)")
        print()
        print(f"**Weighted Accuracy: {summary['weighted_accuracy_percent']:.1f}%**")
        
        # Target analysis
        if summary['weighted_accuracy_percent'] >= 80.0:
            print("\\n🎯 **TARGET ACHIEVED: 80%+ accuracy reached!**")
        else:
            print(f"\\n⚠️  Need {80.0 - summary['weighted_accuracy_percent']:.1f} more percentage points to reach 80% target")
        
        print("=" * 70)
    
    def save_results(self, summary: Dict[str, Any], filename: str):
        """Save detailed results to JSON"""
        with open(filename, 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"Detailed results saved to: {filename}")

def main():
    """Run advanced evaluation"""
    print("=" * 70)
    print("ADVANCED RAG EVALUATION - Target: 80%+ Accuracy")
    print("=" * 70)
    
    # Initialize advanced RAG system
    print("Initializing advanced RAG system...")
    rag = AdvancedRAGSystem(chunk_size=1200, chunk_overlap=300, use_bge=True)
    
    # Try to load existing index, otherwise build new one
    if not rag.load_indices("advanced_rag_index"):
        print("Building new advanced indices...")
        rag.process_pdfs("/home/guilinzhang/allProjects/mfg-ai-platform/docs")
        rag.build_indices()
        rag.save_indices("advanced_rag_index")
    
    # Run evaluation
    evaluator = AdvancedEvaluator()
    summary = evaluator.run_evaluation(rag)
    
    # Print and save results
    evaluator.print_summary(summary)
    evaluator.save_results(summary, "advanced_evaluation_results.json")
    
    return summary['weighted_accuracy_percent']

if __name__ == "__main__":
    accuracy = main()
    sys.exit(0 if accuracy >= 80.0 else 1)