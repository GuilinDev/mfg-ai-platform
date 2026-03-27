# Configuration management for Manufacturing AI RAG Prototype
import os
from typing import Dict, Any
import streamlit as st

class Config:
    """Central configuration management"""
    
    # API Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_BASE_URL = "https://api.groq.com/openai/v1"
    
    # Model Configuration  
    EMBEDDING_MODEL = "text-embedding-ada-002"  # Still using OpenAI for embeddings
    LLM_MODEL = "llama-3.3-70b-versatile"  # Groq model
    MAX_TOKENS = 2000
    TEMPERATURE = 0.1  # Low temperature for precision
    
    # Vector Store Configuration
    CHUNK_SIZE = 1024
    CHUNK_OVERLAP = 200
    TOP_K = 5  # Number of chunks to retrieve
    
    # File Paths
    BASE_DIR = "/home/guilinzhang/allProjects/mfg-ai-platform"
    DATA_DIR = f"{BASE_DIR}/docs"
    STORAGE_DIR = f"{BASE_DIR}/prototype/storage"
    TEMPLATE_DIR = f"{BASE_DIR}/prototype/templates"
    OUTPUT_DIR = f"{BASE_DIR}/prototype/outputs"
    
    # Document Types
    DOC_TYPES = {
        "specification": "PDF specifications and guidelines",
        "postmortem": "PowerPoint postmortem reports",  
        "engineering_drawing": "Engineering drawing PDFs"
    }
    
    # Target elements for drawing extraction
    DRAWING_ELEMENTS = [
        'Prebend', 'pre-bend', 'B2B stiffener', 'B2B stiffener_SUS material',
        'B2B stiffener_harness', 'B2B stiffener_finish', 'B2B stiffener_gloss',
        'B2B stiffener_roughness', 'B2B stiffener_adhesive', 'bonding sheet',
        'adhesive', 'liner', 'underfill', 'encapsulation', 'gold plating',
        'switch', 'vestige', 'tab', 'PSA', 'TSA', 'barcode', 'stackup',
        'bending', 'copper layers', 'coverlay', 'UL', 'mic', 'glue'
    ]
    
    @classmethod
    def get_groq_api_key(cls) -> str:
        """Get Groq API key from environment or Streamlit secrets"""
        if cls.GROQ_API_KEY:
            return cls.GROQ_API_KEY
        
        try:
            return st.secrets["groq"]["api_key"]
        except:
            return ""
    
    @classmethod
    def get_openai_api_key(cls) -> str:
        """Get OpenAI API key for embeddings (fallback to Groq for now)"""
        # For embeddings, we'll need to use an alternative since Groq doesn't provide embeddings
        # We'll use a free embedding service or local embeddings
        return cls.get_groq_api_key()
    
    @classmethod
    def validate_config(cls) -> Dict[str, bool]:
        """Validate configuration settings"""
        validations = {
            "groq_api_key": bool(cls.get_groq_api_key()),
            "data_directory": os.path.exists(cls.DATA_DIR),
            "storage_directory": os.path.exists(cls.STORAGE_DIR),
        }
        
        return validations
    
    @classmethod
    def create_directories(cls):
        """Create necessary directories if they don't exist"""
        os.makedirs(cls.STORAGE_DIR, exist_ok=True)
        os.makedirs(cls.TEMPLATE_DIR, exist_ok=True)
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)
        
        for doc_type in cls.DOC_TYPES.keys():
            os.makedirs(f"{cls.STORAGE_DIR}/{doc_type}", exist_ok=True)