# Manufacturing AI RAG Prototype - Streamlit Application (Simple Version)
import streamlit as st
import os
import sys
from pathlib import Path
import time
from typing import Dict, List, Any
import json

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from simple_rag import SimpleRAGSystem
from src.utils.config import Config

# Page configuration
st.set_page_config(
    page_title="Manufacturing AI RAG Demo (Groq)",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    font-weight: bold;
    color: #1e3a5f;
    text-align: center;
    padding: 1rem 0;
}
.confidence-high { color: #28a745; font-weight: bold; }
.confidence-medium { color: #ffc107; font-weight: bold; }
.confidence-low { color: #dc3545; font-weight: bold; }
.source-box {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 1rem;
    margin: 0.5rem 0;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def initialize_rag_system():
    """Initialize the simple RAG system (lazy — index built on first query)"""
    try:
        rag = SimpleRAGSystem()
        
        # Try to load existing index (fast, no API calls)
        if rag.load_index("simple_rag_index"):
            rag._ready = True
        else:
            rag._ready = False  # Will build on first query
        
        return rag
        
    except Exception as e:
        st.error(f"❌ Error initializing RAG system: {str(e)}")
        return None

def ensure_index_ready(rag):
    """Build index on demand, not at startup"""
    if getattr(rag, '_ready', False):
        return True
    st.info("🔨 First-time setup: Building index from PDFs...")
    with st.spinner("Processing PDF documents + generating embeddings (1-2 min)..."):
        rag.process_pdfs(Config.DATA_DIR)
        rag.build_index()
        rag.save_index("simple_rag_index")
    rag._ready = True
    st.success("✅ Index built successfully!")
    return True

def render_confidence_badge(score: float) -> str:
    """Render confidence score as colored badge based on retrieval score"""
    # Lower FAISS L2 distance score = better match
    if score < 0.8:
        return f'<span class="confidence-high">🟢 High Relevance (Score: {score:.3f})</span>'
    elif score < 1.2:
        return f'<span class="confidence-medium">🟡 Medium Relevance (Score: {score:.3f})</span>'
    else:
        return f'<span class="confidence-low">🔴 Low Relevance (Score: {score:.3f})</span>'

def main():
    """Main application"""
    
    # Header
    st.markdown('<h1 class="main-header">🏭 Manufacturing AI RAG Demo (Groq)</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #666; margin-bottom: 2rem;">
    Advanced Document Retrieval with Groq LLM - Simple RAG Implementation
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize RAG system
    rag_system = initialize_rag_system()
    
    if not rag_system:
        st.stop()
    
    # Sidebar
    st.sidebar.markdown("## 🎯 System Status")
    
    # Check configuration
    groq_key_status = "✅" if Config.get_groq_api_key() else "❌"
    data_dir_status = "✅" if os.path.exists(Config.DATA_DIR) else "❌"
    
    st.sidebar.markdown(f"{groq_key_status} Groq API Key")
    st.sidebar.markdown(f"{data_dir_status} Data Directory")
    st.sidebar.markdown(f"🤖 Model: {Config.LLM_MODEL}")
    
    # Show document stats
    if hasattr(rag_system, 'documents') and rag_system.documents:
        st.sidebar.markdown("## 📊 Index Stats")
        st.sidebar.markdown(f"📄 Documents: {len(rag_system.documents)}")
        
        # Count unique files
        unique_files = set(meta['source_file'] for meta in rag_system.metadata)
        st.sidebar.markdown(f"📁 Files: {len(unique_files)}")
        
        # Show file list
        with st.sidebar.expander("📋 Processed Files"):
            for file in sorted(unique_files):
                st.markdown(f"• {file}")
    
    # Main interface
    st.markdown("## 💡 Sample Questions")
    sample_questions = [
        "What is bending location tolerance?",
        "What is LPI or Solder mask thickness?", 
        "What is FPC design guideline of De-cap?",
        "What is the bonding adhesive patch back?",
        "What is dimension of EMI shield to coverlay edge?",
        "What is FPC reflow test acceptance criteria?"
    ]
    
    selected_sample = st.selectbox("Choose a sample question:", [""] + sample_questions)
    
    # Query input
    query = st.text_input(
        "Enter your specification question:",
        value=selected_sample,
        placeholder="e.g., What is bending location tolerance?"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        search_button = st.button("🔍 Search", type="primary")
    with col2:
        top_k = st.slider("Number of sources", 3, 10, 5)
    
    if search_button and query:
        # Build index on first query (lazy init)
        if not ensure_index_ready(rag_system):
            st.error("Failed to build index")
            st.stop()
        
        start_time = time.time()
        
        with st.spinner("🔍 Searching documents and generating answer..."):
            result = rag_system.query(query, top_k=top_k)
        
        processing_time = time.time() - start_time
        
        if result['error']:
            st.error(f"❌ Error: {result['error']}")
        else:
            # Display results
            st.markdown("## 📋 Answer")
            
            # Processing metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Processing Time", f"{processing_time:.2f}s")
            with col2:
                st.metric("Sources Found", len(result['sources']))
            with col3:
                avg_score = sum(s['score'] for s in result['sources']) / len(result['sources'])
                st.metric("Avg Relevance Score", f"{avg_score:.3f}")
            
            # Answer
            st.markdown(f"**Answer:** {result['answer']}")
            
            # Sources
            st.markdown("### 📚 Sources")
            
            if result['sources']:
                for i, source in enumerate(result['sources'], 1):
                    with st.expander(f"Source {i}: {source['file']} - Page {source['page']} {render_confidence_badge(source['score'])}"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown(f"**File:** {source['file']}")
                            st.markdown(f"**Page:** {source['page']}")
                            st.markdown(f"**Chunk ID:** {source['chunk_id']}")
                            
                        with col2:
                            st.markdown(f"**Relevance Score:** {source['score']:.6f}")
                            st.markdown("*Lower score = better match*")
                            
                        st.markdown("**Text Preview:**")
                        st.text(source['text_preview'])
                        
                        # Show full text in a collapsible section
                        if st.button(f"Show full text {i}", key=f"full_text_{i}"):
                            st.text(source.get('full_text', 'Full text not available'))
            else:
                st.warning("No sources found")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **About this demo:**
    - Uses Groq LLM (llama-3.3-70b-versatile) for fast inference
    - Local sentence transformers for embeddings (all-MiniLM-L6-v2)
    - FAISS vector database for efficient similarity search
    - Processing Apple FPC/PCB manufacturing specifications
    """)

if __name__ == "__main__":
    main()