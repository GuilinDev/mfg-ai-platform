# Custom embedding wrapper that integrates with LlamaIndex
# Uses HuggingFace Inference API instead of local sentence-transformers
from typing import List, Any
from llama_index.core.embeddings import BaseEmbedding
from pydantic import PrivateAttr
import os
import time
import requests


HF_API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384  # all-MiniLM-L6-v2 dimension


def _get_hf_token() -> str:
    """Get HuggingFace token from environment"""
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    if not token:
        raise ValueError(
            "HuggingFace token not found. Set HF_TOKEN or HUGGINGFACE_TOKEN environment variable."
        )
    return token


def _call_hf_api(texts: List[str], retries: int = 2) -> List[List[float]]:
    """Call HuggingFace Inference API with retry logic"""
    token = _get_hf_token()
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(retries + 1):
        try:
            response = requests.post(
                HF_API_URL,
                headers=headers,
                json={"inputs": texts, "options": {"wait_for_model": True}},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < retries:
                time.sleep(1)
                continue
            raise RuntimeError(
                f"HuggingFace Inference API failed after {retries + 1} attempts: {e}"
            ) from e


class CustomSentenceTransformerEmbedding(BaseEmbedding):
    """Custom embedding class using HuggingFace Inference API"""

    _model_name: str = PrivateAttr(default="all-MiniLM-L6-v2")

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", **kwargs):
        super().__init__(**kwargs)
        self._model_name = model_name
        # Validate token is available at init time
        _get_hf_token()
        print(f"Using HuggingFace Inference API for embeddings: {self._model_name}")

    def _get_query_embedding(self, query: str) -> List[float]:
        result = _call_hf_api([query])
        return result[0]

    def _get_text_embedding(self, text: str) -> List[float]:
        result = _call_hf_api([text])
        return result[0]

    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        return _call_hf_api(texts)

    async def _aget_query_embedding(self, query: str) -> List[float]:
        return self._get_query_embedding(query)

    async def _aget_text_embedding(self, text: str) -> List[float]:
        return self._get_text_embedding(text)

    async def _aget_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self._get_text_embeddings(texts)
