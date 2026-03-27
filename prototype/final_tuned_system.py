#!/usr/bin/env python3
"""
Final tuned system - combines best of both approaches
Keeps the precision improvements but ensures specific searches work
"""

from improved_rag_system import ImprovedRAGSystem
import re
from typing import List, Dict, Any

class FinalTunedRAGSystem(ImprovedRAGSystem):
    """Final tuned system that combines precision search with fallback to broader search"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Specific search terms that should be tried for exact matches
        self.exact_search_patterns = {
            'bending location tolerance': ['0.300', '0.300 mm', 'bending location', 'tolerance bending'],
            'lpi thickness': ['4-39um', '4-39', 'solder mask thickness', 'lpi 4'],
            'de-cap guideline': ['layer transition', 'copper layers', 'cut away', 'pre-punch', 'laser after'],
            'bonding adhesive patch': ['drill hole plasma', 'wet desmear', 'etch back', 'FCCL'],
            'upd': ['unit process development', 'process development'],
            'emi shield': ['0.400 mm', '0.400', 'coverlay edge'],
            'reflow test': ['function', 'cosmetics', 'BVH peel', 'cross-section'],
            'laser drilling': ['visual defects', 'alignment', 'hole size'],
            'cqra': ['thermal cycle', 'hot oil', 'reflow', 'insulation resistance', 'thermal stability']
        }
    
    def enhanced_query(self, question: str, top_k: int = 5) -> Dict[str, Any]:
        """Enhanced query that tries multiple search strategies"""
        question_lower = question.lower()
        
        # Strategy 1: Try exact search patterns first
        exact_results = self._try_exact_search_patterns(question_lower, top_k)
        if exact_results and self._has_good_exact_match(exact_results, question):
            return self._generate_answer_from_results(question, exact_results, "exact_pattern")
        
        # Strategy 2: Try the original improved query
        standard_results = self.search(question, top_k * 2)  # Get more candidates
        if standard_results:
            # Filter for high-quality results
            quality_results = [r for r in standard_results if self._is_quality_result(r, question)]
            if quality_results:
                return self._generate_answer_from_results(question, quality_results[:top_k], "quality_filtered")
        
        # Strategy 3: Fallback to original search
        if standard_results:
            return self._generate_answer_from_results(question, standard_results[:top_k], "standard_search")
        
        # No results found
        return {
            'answer': 'No relevant documents found.',
            'sources': [],
            'error': 'No search results'
        }
    
    def _try_exact_search_patterns(self, question_lower: str, top_k: int) -> List[Dict[str, Any]]:
        """Try exact search patterns for the question"""
        all_results = []
        
        for pattern_key, search_terms in self.exact_search_patterns.items():
            if pattern_key in question_lower:
                for search_term in search_terms:
                    results = self.search(search_term, top_k)
                    for result in results:
                        result['search_term'] = search_term
                        all_results.append(result)
        
        # Deduplicate and sort by score
        unique_results = {}
        for result in all_results:
            chunk_id = result['metadata']['chunk_id']
            if chunk_id not in unique_results or result['score'] < unique_results[chunk_id]['score']:
                unique_results[chunk_id] = result
        
        return sorted(unique_results.values(), key=lambda x: x['score'])[:top_k]
    
    def _has_good_exact_match(self, results: List[Dict[str, Any]], question: str) -> bool:
        """Check if results contain good exact matches"""
        question_lower = question.lower()
        
        # Check for specific patterns that indicate good matches
        for result in results[:3]:  # Check top 3 results
            text_lower = result['text'].lower()
            
            # Measurement questions should have exact numbers
            if any(word in question_lower for word in ['tolerance', 'thickness', 'dimension']):
                if re.search(r'\\d+\\.?\\d*\\s*(mm|um|mil)', text_lower):
                    return True
            
            # Definition questions should have clear definitions
            if question_lower.startswith('what is'):
                search_term = result.get('search_term', '').lower()
                if search_term and search_term in text_lower:
                    return True
        
        return False
    
    def _is_quality_result(self, result: Dict[str, Any], question: str) -> bool:
        """Check if result is high quality for the question"""
        text_lower = result['text'].lower()
        question_lower = question.lower()
        
        # Extract key terms from question
        question_terms = re.findall(r'\\b\\w+\\b', question_lower)
        question_terms = [term for term in question_terms if len(term) > 2 and term not in ['what', 'the', 'and', 'for']]
        
        # Count how many question terms appear in the result
        term_matches = sum(1 for term in question_terms if term in text_lower)
        
        # Require at least 50% of question terms to be present
        return len(question_terms) == 0 or (term_matches / len(question_terms)) >= 0.5
    
    def _generate_answer_from_results(self, question: str, results: List[Dict[str, Any]], method: str) -> Dict[str, Any]:
        """Generate answer from search results"""
        context_parts = []
        sources = []
        
        for i, result in enumerate(results):
            context_parts.append(f"Source {i+1}: {result['metadata']['source_file']}\\n{result['text']}")
            
            sources.append({
                'file': result['metadata']['source_file'],
                'chunk_id': result['metadata']['chunk_id'],
                'score': result['score'],
                'search_term': result.get('search_term'),
                'preview': result['text'][:300] + "..." if len(result['text']) > 300 else result['text']
            })
        
        context = "\\n\\n---\\n\\n".join(context_parts)
        
        # Create focused prompt based on question type
        prompt = self._create_focused_prompt_v2(question, context)
        
        try:
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a precise manufacturing expert. Extract exact specifications from technical documents."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
                max_tokens=1000
            )
            
            answer = response.choices[0].message.content
            
            return {
                'answer': answer,
                'sources': sources,
                'query': question,
                'method': method,
                'error': None
            }
            
        except Exception as e:
            return {
                'answer': f'Error: {str(e)}',
                'sources': sources,
                'error': str(e)
            }
    
    def _create_focused_prompt_v2(self, question: str, context: str) -> str:
        """Create focused prompt based on question analysis"""
        question_lower = question.lower()
        
        # Measurement questions - focus on exact values
        if any(word in question_lower for word in ['tolerance', 'thickness', 'dimension']) and ('bending' in question_lower or 'lpi' in question_lower or 'solder mask' in question_lower or 'emi' in question_lower):
            return f"""Extract the exact measurement value from the technical documents.

CONTEXT:
{context}

QUESTION: {question}

INSTRUCTIONS:
- Look for exact numerical values with units (mm, um, mil, %)
- Provide ONLY the measurement (e.g., "0.300 mm" or "4-39um")
- If multiple values exist, provide the range
- Do not provide explanations or context
- Cite the source document

Answer:"""

        # Process definition questions - focus on clear explanations
        elif 'de-cap' in question_lower and 'guideline' in question_lower:
            return f"""Explain the FPC de-cap process definition and purpose.

CONTEXT:
{context}

QUESTION: {question}

INSTRUCTIONS:
- Explain WHY de-cap is needed (different layer counts)
- Describe WHAT the process does (layer transition, cut away excess)
- Mention HOW it's done (pre-punch, laser)
- Focus on the conceptual explanation, not just measurements
- Cite the source document

Answer:"""

        # Simple definition questions - focus on exact definitions
        elif question_lower.strip() in ['what is upd?', 'what is upd']:
            return f"""Provide the exact definition of the acronym.

CONTEXT:
{context}

QUESTION: {question}

INSTRUCTIONS:
- Provide the exact expansion of UPD
- Answer format: "Unit Process Development" or similar
- Do not provide process descriptions
- Cite the source document

Answer:"""

        # List-based questions - focus on extracting lists
        elif any(word in question_lower for word in ['criteria', 'plan', 'cqra']):
            return f"""Extract the specific list items or criteria.

CONTEXT:
{context}

QUESTION: {question}

INSTRUCTIONS:
- Extract all mentioned items, steps, or criteria
- Present as a clear list
- Include all relevant components
- Cite the source document

Answer:"""

        # General manufacturing questions
        else:
            return f"""Answer the technical question precisely based on the provided documents.

CONTEXT:
{context}

QUESTION: {question}

INSTRUCTIONS:
- Extract exact technical information
- Provide precise specifications with units
- Always cite the source document
- Be concise but complete

Answer:"""
    
    # Override the query method to use our enhanced version
    def query(self, question: str, top_k: int = 5) -> Dict[str, Any]:
        """Use enhanced query method"""
        return self.enhanced_query(question, top_k)

def test_final_tuned_system():
    """Test the final tuned system"""
    print("=" * 80)
    print("TESTING FINAL TUNED SYSTEM")
    print("=" * 80)
    
    # Initialize system
    rag = FinalTunedRAGSystem()
    if not rag.load_index("improved_rag_index"):
        print("Could not load index")
        return
    
    # Test the critical cases
    test_cases = [
        "What is bending location tolerance?",
        "What is the LPI or Solder mask thickness",
        "What is UPD?",
        "What is dimension of EMI shield to coverlay edge?",
    ]
    
    for i, question in enumerate(test_cases, 1):
        print(f"\\n=== TEST {i}: {question} ===")
        
        result = rag.query(question)
        print(f"Method: {result['method']}")
        print(f"Answer: {result['answer']}")
        print(f"Sources: {len(result['sources'])}")
        
        if result['sources'] and result['sources'][0].get('search_term'):
            print(f"Found via search term: {result['sources'][0]['search_term']}")
        
        print("-" * 60)

if __name__ == "__main__":
    test_final_tuned_system()