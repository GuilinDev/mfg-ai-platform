# Query Engine for Manufacturing RAG System
from typing import Dict, List, Optional, Any, Tuple
import re
from dataclasses import dataclass

from llama_index.core import QueryBundle
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.response_synthesizers import TreeSummarize
from llama_index.llms.openai_like import OpenAILike

from ..utils.config import Config
from .index_manager import IndexManager

@dataclass
class QueryResponse:
    """Structured response from query engine"""
    answer: str
    confidence: float
    sources: List[Dict[str, Any]]
    query_type: str
    processing_time: float
    error: Optional[str] = None

class ConfidenceCalculator:
    """Calculate confidence scores for query responses"""
    
    @staticmethod
    def calculate_confidence(response, sources: List[Dict], query: str) -> float:
        """Multi-factor confidence scoring"""
        
        factors = {
            'source_similarity': ConfidenceCalculator._calculate_similarity_score(sources),
            'answer_completeness': ConfidenceCalculator._calculate_completeness_score(response, query),
            'source_count': min(len(sources) / 3.0, 1.0),
            'answer_length': min(len(str(response)) / 200.0, 1.0),
            'numerical_precision': ConfidenceCalculator._check_numerical_precision(response, query)
        }
        
        weights = {
            'source_similarity': 0.35,
            'answer_completeness': 0.25, 
            'source_count': 0.20,
            'answer_length': 0.10,
            'numerical_precision': 0.10
        }
        
        confidence = sum(factors[k] * weights[k] for k in factors.keys())
        return min(max(confidence, 0.0), 1.0)  # Clamp to [0, 1]
        
    @staticmethod
    def _calculate_similarity_score(sources: List[Dict]) -> float:
        """Calculate similarity score based on source relevance"""
        if not sources:
            return 0.0
            
        # Average similarity scores from sources
        similarities = [source.get('score', 0.0) for source in sources]
        return sum(similarities) / len(similarities) if similarities else 0.0
        
    @staticmethod
    def _calculate_completeness_score(response: str, query: str) -> float:
        """Score based on answer completeness"""
        response_str = str(response).lower()
        query_str = query.lower()
        
        # Check if response addresses the query
        score = 0.5  # Base score
        
        # Boost if response contains specific values
        if re.search(r'\d+\.?\d*\s*(mm|um|%)', response_str):
            score += 0.3
            
        # Boost if response mentions source information
        if any(keyword in response_str for keyword in ['page', 'section', 'document']):
            score += 0.2
            
        return min(score, 1.0)
        
    @staticmethod
    def _check_numerical_precision(response: str, query: str) -> float:
        """Check numerical precision for specification queries"""
        response_str = str(response)
        
        # If query asks for numerical value, check if response provides it
        if any(keyword in query.lower() for keyword in ['tolerance', 'thickness', 'dimension', 'what is']):
            if re.search(r'\d+\.?\d*\s*(mm|um|%|inch)', response_str):
                return 1.0
            else:
                return 0.3
                
        return 0.7  # Default for non-numerical queries

class QueryClassifier:
    """Classify query types to optimize retrieval strategy"""
    
    QUERY_PATTERNS = {
        'specification_lookup': [
            r'what is.*?(tolerance|thickness|dimension|size)',
            r'(tolerance|thickness|dimension|size).*?is',
            r'what.*?(specification|spec)',
        ],
        'process_inquiry': [
            r'what.*?(process|procedure|method)',
            r'how.*?(process|procedure|test)',
            r'(process|procedure|method).*?for',
        ],
        'comparison': [
            r'(compare|difference|vs|versus)',
            r'(better|worse|higher|lower).*?than',
        ],
        'definition': [
            r'what is.*?(\w+)$',
            r'define.*?(\w+)',
            r'(\w+).*?definition',
        ]
    }
    
    @classmethod
    def classify_query(cls, query: str) -> str:
        """Classify query type based on patterns"""
        query_lower = query.lower().strip()
        
        for query_type, patterns in cls.QUERY_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    return query_type
                    
        return 'general'

class MultiModalQueryEngine:
    """Advanced query engine supporting multiple document types"""
    
    def __init__(self, index_manager: IndexManager):
        self.index_manager = index_manager
        self.llm = OpenAILike(
            model=Config.LLM_MODEL,
            temperature=Config.TEMPERATURE,
            max_tokens=Config.MAX_TOKENS,
            api_key=Config.get_groq_api_key(),
            api_base=Config.GROQ_BASE_URL,
            is_chat_model=True,
        )
        self.query_classifier = QueryClassifier()
        self.confidence_calculator = ConfidenceCalculator()
        
    def query_specifications(self, query: str) -> QueryResponse:
        """Query PDF specifications (Use Case 1)"""
        import time
        start_time = time.time()
        
        try:
            # Get specification index
            spec_index = self.index_manager.get_index('specification')
            if not spec_index:
                return QueryResponse(
                    answer="Specification index not available. Please build the index first.",
                    confidence=0.0,
                    sources=[],
                    query_type="error",
                    processing_time=time.time() - start_time,
                    error="Index not found"
                )
            
            # Classify query type
            query_type = self.query_classifier.classify_query(query)
            
            # Create query engine with custom prompt
            query_engine = spec_index.as_query_engine(
                llm=self.llm,
                response_mode="tree_summarize",
                similarity_top_k=Config.TOP_K,
                streaming=False
            )
            
            # Enhanced prompt for specifications
            enhanced_query = self._enhance_specification_query(query, query_type)
            
            # Execute query
            response = query_engine.query(enhanced_query)
            
            # Extract source information
            sources = self._extract_source_info(response.source_nodes)
            
            # Calculate confidence
            confidence = self.confidence_calculator.calculate_confidence(
                response.response, sources, query
            )
            
            processing_time = time.time() - start_time
            
            return QueryResponse(
                answer=str(response.response),
                confidence=confidence,
                sources=sources,
                query_type=query_type,
                processing_time=processing_time
            )
            
        except Exception as e:
            return QueryResponse(
                answer=f"Error processing query: {str(e)}",
                confidence=0.0,
                sources=[],
                query_type="error",
                processing_time=time.time() - start_time,
                error=str(e)
            )
    
    def query_postmortems(self, query: str) -> QueryResponse:
        """Query PowerPoint postmortems (Use Case 2)"""
        import time
        start_time = time.time()
        
        try:
            postmortem_index = self.index_manager.get_index('postmortem')
            if not postmortem_index:
                return QueryResponse(
                    answer="Postmortem index not available. Please build the index first.",
                    confidence=0.0,
                    sources=[],
                    query_type="error",
                    processing_time=time.time() - start_time,
                    error="Index not found"
                )
            
            query_type = self.query_classifier.classify_query(query)
            
            # Create query engine
            query_engine = postmortem_index.as_query_engine(
                llm=self.llm,
                response_mode="tree_summarize",
                similarity_top_k=Config.TOP_K,
                streaming=False
            )
            
            # Enhanced prompt for postmortem analysis
            enhanced_query = self._enhance_postmortem_query(query, query_type)
            
            response = query_engine.query(enhanced_query)
            sources = self._extract_source_info(response.source_nodes)
            
            confidence = self.confidence_calculator.calculate_confidence(
                response.response, sources, query
            )
            
            processing_time = time.time() - start_time
            
            return QueryResponse(
                answer=str(response.response),
                confidence=confidence,
                sources=sources,
                query_type=query_type,
                processing_time=processing_time
            )
            
        except Exception as e:
            return QueryResponse(
                answer=f"Error processing postmortem query: {str(e)}",
                confidence=0.0,
                sources=[],
                query_type="error",
                processing_time=time.time() - start_time,
                error=str(e)
            )
    
    def query_drawings(self, query: str) -> QueryResponse:
        """Query engineering drawings (Use Case 3)"""
        import time
        start_time = time.time()
        
        try:
            drawing_index = self.index_manager.get_index('engineering_drawing')
            if not drawing_index:
                return QueryResponse(
                    answer="Engineering drawing index not available. Please build the index first.",
                    confidence=0.0,
                    sources=[],
                    query_type="error",
                    processing_time=time.time() - start_time,
                    error="Index not found"
                )
            
            query_type = self.query_classifier.classify_query(query)
            
            query_engine = drawing_index.as_query_engine(
                llm=self.llm,
                response_mode="tree_summarize",
                similarity_top_k=Config.TOP_K,
                streaming=False
            )
            
            enhanced_query = self._enhance_drawing_query(query, query_type)
            
            response = query_engine.query(enhanced_query)
            sources = self._extract_source_info(response.source_nodes)
            
            confidence = self.confidence_calculator.calculate_confidence(
                response.response, sources, query
            )
            
            processing_time = time.time() - start_time
            
            return QueryResponse(
                answer=str(response.response),
                confidence=confidence,
                sources=sources,
                query_type=query_type,
                processing_time=processing_time
            )
            
        except Exception as e:
            return QueryResponse(
                answer=f"Error processing drawing query: {str(e)}",
                confidence=0.0,
                sources=[],
                query_type="error",
                processing_time=time.time() - start_time,
                error=str(e)
            )
    
    def _enhance_specification_query(self, query: str, query_type: str) -> str:
        """Enhance query with specification-specific context"""
        
        base_context = """You are a manufacturing expert analyzing technical specifications. 
        Provide precise, accurate answers with specific values and units when available.
        Always cite the source document and page number."""
        
        if query_type == 'specification_lookup':
            context = f"""{base_context}
            Focus on finding exact numerical values, tolerances, and specifications.
            Include units (mm, um, %, etc.) and any applicable conditions."""
        elif query_type == 'process_inquiry':
            context = f"""{base_context}
            Explain procedures step-by-step with any quality control requirements."""
        else:
            context = base_context
            
        return f"{context}\n\nQuery: {query}"
    
    def _enhance_postmortem_query(self, query: str, query_type: str) -> str:
        """Enhance query for postmortem analysis"""
        
        base_context = """You are analyzing manufacturing postmortem reports. 
        Provide data-driven answers with specific metrics, percentages, and comparisons.
        Always cite the source presentation and slide number."""
        
        if query_type == 'comparison':
            context = f"""{base_context}
            Compare data between different platforms (AMP vs ICT) or time periods (P1 vs P2).
            Present quantitative differences clearly."""
        else:
            context = base_context
            
        return f"{context}\n\nQuery: {query}"
    
    def _enhance_drawing_query(self, query: str, query_type: str) -> str:
        """Enhance query for engineering drawings"""
        
        base_context = """You are analyzing engineering drawings and technical specifications.
        Extract specific component information, dimensions, materials, and assembly details.
        Focus on the 28 key elements: stiffeners, adhesives, layers, bending, etc."""
        
        return f"{base_context}\n\nQuery: {query}"
    
    def _extract_source_info(self, source_nodes) -> List[Dict[str, Any]]:
        """Extract source information from retrieved nodes"""
        sources = []
        
        for node in source_nodes:
            if hasattr(node, 'metadata'):
                metadata = node.metadata
                source_info = {
                    'file': metadata.get('source_file', 'Unknown'),
                    'page': metadata.get('page_number', 'Unknown'),
                    'section': metadata.get('section', 'Unknown'),
                    'chunk_id': metadata.get('chunk_id', 'Unknown'),
                    'document_type': metadata.get('document_type', 'Unknown'),
                    'confidence': getattr(node, 'score', 0.0),
                    'text_preview': node.text[:200] + "..." if len(node.text) > 200 else node.text
                }
                sources.append(source_info)
                
        return sources