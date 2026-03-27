# Custom embedding wrapper that integrates with LlamaIndex
from typing import List, Any, ClassVar
from llama_index.core.embeddings import BaseEmbedding
from sentence_transformers import SentenceTransformer
from pydantic import PrivateAttr


class CustomSentenceTransformerEmbedding(BaseEmbedding):
    """Custom embedding class using sentence transformers"""
    
    _st_model: Any = PrivateAttr(default=None)
    _st_model_name: str = PrivateAttr(default="all-MiniLM-L6-v2")
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", **kwargs):
        super().__init__(**kwargs)
        self._st_model_name = model_name
        self._st_model = None
    
    @property
    def st_model(self):
        """Lazy load the model"""
        if self._st_model is None:
            try:
                self._st_model = SentenceTransformer(self._st_model_name)
                print(f"Loaded sentence transformer model: {self._st_model_name}")
            except Exception as e:
                print(f"Failed to load sentence transformer: {e}")
                raise
        return self._st_model
    
    def _get_query_embedding(self, query: str) -> List[float]:
        return self.st_model.encode(query).tolist()
    
    def _get_text_embedding(self, text: str) -> List[float]:
        return self.st_model.encode(text).tolist()
    
    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        embeddings = self.st_model.encode(texts)
        return [embedding.tolist() for embedding in embeddings]
    
    async def _aget_query_embedding(self, query: str) -> List[float]:
        return self._get_query_embedding(query)
    
    async def _aget_text_embedding(self, text: str) -> List[float]:
        return self._get_text_embedding(text)
    
    async def _aget_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self._get_text_embeddings(texts)
