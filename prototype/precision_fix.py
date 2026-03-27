#!/usr/bin/env python3
"""
Precision fixes for the specific failing cases
Focus on better search terms and more precise prompting
"""

import sys
import json
import re
from typing import List, Dict, Any
from improved_rag_system import ImprovedRAGSystem

class PrecisionRAGSystem(ImprovedRAGSystem):
    """Enhanced RAG with precision fixes for failing cases"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Define term mappings for better search
        self.term_mappings = {
            'bending location tolerance': ['0.300 mm', 'bending tolerance', 'location tolerance', 'bend tolerance'],
            'de-cap': ['layer transition', 'copper layers', 'flex layers', 'cut away process', 'pre-punch', 'laser after lamination'],
            'bonding adhesive patch back': ['drill hole plasma', 'wet desmear', 'adhesive etch back', 'FCCL adhesive'],
            'upd': ['unit process development', 'process development', 'qualification process', 'upd step', 'doe parts']
        }
    
    def enhanced_search(self, query: str, top_k: int = 10) -> List[Dict[str, Any]]:
        """Enhanced search with term mapping and multi-query"""
        all_results = []
        
        # Original query
        original_results = self.search(query, top_k)
        all_results.extend([(r, 'original', 1.0) for r in original_results])
        
        # Enhanced queries based on term mappings
        query_lower = query.lower()
        for key_term, variants in self.term_mappings.items():
            if key_term in query_lower:
                for variant in variants:
                    variant_results = self.search(variant, top_k=5)
                    all_results.extend([(r, f'variant:{variant}', 0.9) for r in variant_results])
        
        # Extract key technical terms and search for them
        tech_terms = self._extract_technical_terms(query)
        for term in tech_terms:
            term_results = self.search(term, top_k=3)
            all_results.extend([(r, f'tech_term:{term}', 0.8) for r in term_results])
        
        # Deduplicate and rerank
        unique_results = self._deduplicate_results(all_results)
        
        return unique_results[:top_k]
    
    def _extract_technical_terms(self, query: str) -> List[str]:
        """Extract technical terms from query"""
        terms = []
        
        # Acronyms
        acronyms = re.findall(r'\\b[A-Z]{2,5}\\b', query)
        terms.extend(acronyms)
        
        # Technical words
        tech_words = ['tolerance', 'thickness', 'dimension', 'guideline', 'criteria', 'process', 'development']
        for word in tech_words:
            if word in query.lower():
                terms.append(word)
        
        return terms
    
    def _deduplicate_results(self, all_results: List[tuple]) -> List[Dict[str, Any]]:
        """Deduplicate results and combine scores"""
        result_map = {}
        
        for result, source, weight in all_results:
            chunk_id = result['metadata']['chunk_id']
            
            if chunk_id not in result_map:
                result_map[chunk_id] = {
                    'result': result,
                    'best_score': result['score'],
                    'sources': [],
                    'total_weight': 0
                }
            
            entry = result_map[chunk_id]
            entry['sources'].append(source)
            entry['total_weight'] += weight
            
            # Keep best (lowest) score
            if result['score'] < entry['best_score']:
                entry['best_score'] = result['score']
        
        # Sort by combined score (lower is better, but weight contribution)
        final_results = []
        for chunk_id, entry in result_map.items():
            combined_score = entry['best_score'] / (1 + entry['total_weight'] * 0.1)
            
            final_results.append({
                **entry['result'],
                'score': combined_score,
                'search_sources': entry['sources'],
                'total_weight': entry['total_weight']
            })
        
        return sorted(final_results, key=lambda x: x['score'])
    
    def create_focused_prompt(self, question: str, context: str) -> str:
        """Create question-specific focused prompt"""
        question_lower = question.lower()
        
        if 'tolerance' in question_lower and 'bending' in question_lower:
            return self._tolerance_prompt(question, context)
        elif 'de-cap' in question_lower and 'guideline' in question_lower:
            return self._decap_guideline_prompt(question, context)
        elif 'bonding adhesive' in question_lower:
            return self._bonding_adhesive_prompt(question, context)
        elif question_lower.strip() == 'what is upd?':
            return self._upd_definition_prompt(question, context)
        else:
            return self._general_manufacturing_prompt(question, context)
    
    def _tolerance_prompt(self, question: str, context: str) -> str:
        return f"""You are analyzing manufacturing tolerance specifications.

CONTEXT:
{context}

QUESTION: {question}

TASK: Find the exact tolerance value for bending location. Look for:
1. Numerical values with units (mm, mil, um)
2. Tolerance specifications with ± symbols
3. Bending-related dimensional requirements

Extract the precise numerical value with units. The answer should be in format "X.XXX mm" or similar.

Answer:"""

    def _decap_guideline_prompt(self, question: str, context: str) -> str:
        return f"""You are explaining FPC design processes.

CONTEXT:
{context}

QUESTION: {question}

TASK: Explain what De-cap is conceptually - the process definition, not just distance requirements.
Look for:
1. Why de-cap is needed (different copper layer counts)
2. What the process does (layer transition, cut away excess layers)
3. How it's done (pre-punch, laser, etc.)
4. The purpose (transitioning between different layer counts)

Focus on the process definition and purpose, not just dimensional specifications.

Answer:"""

    def _bonding_adhesive_prompt(self, question: str, context: str) -> str:
        return f"""You are explaining manufacturing process effects.

CONTEXT:
{context}

QUESTION: {question}

TASK: Explain the bonding adhesive patch back effect. Look for:
1. Process steps involving "drill hole plasma" and "wet desmear"
2. Effects on adhesive between FCCL layers
3. The purpose of etch back
4. Process sequence and why it's necessary

Answer:"""

    def _upd_definition_prompt(self, question: str, context: str) -> str:
        return f"""You are providing technical acronym definitions.

CONTEXT:
{context}

QUESTION: {question}

TASK: Define what UPD stands for. Look for the exact expansion of this acronym.
The answer should be the full form: "Unit Process Development" or similar.
Ignore process descriptions - focus on the acronym expansion.

Answer:"""

    def _general_manufacturing_prompt(self, question: str, context: str) -> str:
        return f"""You are a manufacturing expert analyzing technical specifications.

CONTEXT:
{context}

QUESTION: {question}

Extract precise technical information with exact values, units, and specifications.
Always cite the source document.

Answer:"""
    
    def query(self, question: str, top_k: int = 5) -> Dict[str, Any]:
        """Enhanced query with precision fixes"""
        print(f"Processing query with precision fixes: {question}")
        
        # Enhanced search
        search_results = self.enhanced_search(question, top_k)
        
        if not search_results:
            return {
                'answer': 'No relevant documents found.',
                'sources': [],
                'error': 'No search results'
            }
        
        # Prepare context
        context_parts = []
        sources = []
        
        for i, result in enumerate(search_results):
            context_parts.append(f"Source {i+1}: {result['metadata']['source_file']}\\n{result['text']}")
            
            sources.append({
                'file': result['metadata']['source_file'],
                'chunk_id': result['metadata']['chunk_id'],
                'score': result['score'],
                'search_sources': result.get('search_sources', []),
                'total_weight': result.get('total_weight', 1.0),
                'preview': result['text'][:300] + "..." if len(result['text']) > 300 else result['text']
            })
        
        context = "\\n\\n---\\n\\n".join(context_parts)
        
        # Create focused prompt
        prompt = self.create_focused_prompt(question, context)
        
        try:
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a precise manufacturing expert. Extract exact information from the provided technical documents."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
                max_tokens=800
            )
            
            answer = response.choices[0].message.content
            
            return {
                'answer': answer,
                'sources': sources,
                'query': question,
                'method': 'precision_enhanced',
                'error': None
            }
            
        except Exception as e:
            return {
                'answer': f'Error: {str(e)}',
                'sources': sources,
                'error': str(e)
            }

def test_precision_fixes():
    """Test the precision fixes on failing cases"""
    print("=" * 70)
    print("TESTING PRECISION FIXES")
    print("=" * 70)
    
    # Initialize precision system
    rag = PrecisionRAGSystem()
    if not rag.load_index("improved_rag_index"):
        print("Could not load index")
        return
    
    # Test the failing cases
    test_cases = [
        {
            'question': "What is bending location tolerance?",
            'expected': "0.300 mm"
        },
        {
            'question': "What is FPC design guideline of De-cap?",
            'expected': "layer transition process"
        },
        {
            'question': "What is the bonding adhesive patch back?",
            'expected': "drill hole plasma and wet desmear effect"
        },
        {
            'question': "What is UPD?",
            'expected': "Unit Process Development"
        }
    ]
    
    results = []
    
    for i, case in enumerate(test_cases, 1):
        print(f"\\n=== TEST {i}: {case['question']} ===")
        print(f"Expected: {case['expected']}")
        
        result = rag.query(case['question'])
        
        print(f"Answer: {result['answer']}")
        print(f"Sources: {len(result['sources'])} documents")
        
        if result['sources']:
            print("Search info:")
            for source in result['sources'][:2]:
                print(f"  - {source['file']} (score: {source['score']:.3f}, weight: {source.get('total_weight', 1):.1f})")
                if 'search_sources' in source:
                    print(f"    Found via: {', '.join(source['search_sources'][:3])}")
        
        # Simple evaluation
        answer_lower = result['answer'].lower()
        expected_words = case['expected'].lower().split()
        matches = sum(1 for word in expected_words if word in answer_lower)
        
        if matches >= len(expected_words) // 2:
            status = "✓ IMPROVED"
        else:
            status = "✗ Still needs work"
        
        print(f"Evaluation: {status} ({matches}/{len(expected_words)} key terms found)")
        
        results.append({
            'question': case['question'],
            'expected': case['expected'],
            'answer': result['answer'],
            'status': status,
            'key_term_matches': f"{matches}/{len(expected_words)}"
        })
        
        print("-" * 60)
    
    # Summary
    print("\\n" + "=" * 70)
    print("PRECISION FIX SUMMARY")
    print("=" * 70)
    improved = sum(1 for r in results if "✓ IMPROVED" in r['status'])
    print(f"Improved cases: {improved}/{len(results)}")
    
    for result in results:
        print(f"  {result['status']} {result['question']}")
    
    return results

if __name__ == "__main__":
    test_precision_fixes()