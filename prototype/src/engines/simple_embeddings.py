# Simple embedding wrapper for sentence transformers
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class SimpleEmbedding:
    """Simple embedding using sentence transformers for local use"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Initialize with a lightweight sentence transformer model"""
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()
    
    def embed_query(self, query: str) -> List[float]:
        """Embed a single query"""
        embedding = self.model.encode(query)
        return embedding.tolist()
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple documents"""
        embeddings = self.model.encode(texts)
        return embeddings.tolist()
    
    def get_dimension(self) -> int:
        """Get embedding dimension"""
        return self.dimension