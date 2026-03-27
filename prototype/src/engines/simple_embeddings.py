# Simple embedding wrapper using HuggingFace Inference API
from typing import List
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


class SimpleEmbedding:
    """Simple embedding using HuggingFace Inference API"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Initialize with HuggingFace Inference API"""
        self.model_name = model_name
        self.dimension = EMBEDDING_DIMENSION
        # Validate token is available at init time
        _get_hf_token()
        print(f"Using HuggingFace Inference API for embeddings: {self.model_name}")

    def embed_query(self, query: str) -> List[float]:
        """Embed a single query"""
        result = _call_hf_api([query])
        return result[0]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple documents"""
        return _call_hf_api(texts)

    def get_dimension(self) -> int:
        """Get embedding dimension"""
        return self.dimension
