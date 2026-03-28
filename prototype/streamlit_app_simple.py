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
    page_title="Manufacturing Spec Assistant",
    page_icon="🔍",
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
        st.error("Unable to start the search system. Please refresh the page or contact support.")
        return None

def ensure_index_ready(rag):
    """Build index on demand, not at startup"""
    if getattr(rag, '_ready', False):
        return True
    with st.spinner("🔄 Preparing your document search... (first time only, ~1 min)"):
        rag.process_pdfs(Config.DATA_DIR)
        rag.build_index()
        rag.save_index("simple_rag_index")
    rag._ready = True
    st.success("✅ Ready! You can now search your specifications.")
    return True

def render_confidence_badge(score: float, show_label: bool = True) -> str:
    """Render confidence score as colored badge based on retrieval score"""
    # Lower FAISS L2 distance score = better match
    if score < 0.8:
        return '🟢 High Confidence' if show_label else '🟢'
    elif score < 1.2:
        return '🟡 Medium Confidence' if show_label else '🟡'
    else:
        return '🔴 Low Confidence' if show_label else '🔴'


def get_overall_confidence(sources: List[Dict]) -> tuple:
    """Calculate overall confidence based on number of sources and their scores"""
    if not sources:
        return "🔴 Low", "low"

    avg_score = sum(s['score'] for s in sources) / len(sources)
    high_confidence_count = sum(1 for s in sources if s['score'] < 0.8)

    # High confidence: multiple good matches with low scores
    if len(sources) >= 3 and high_confidence_count >= 2 and avg_score < 1.0:
        return "🟢 High", "high"
    # Medium confidence: some good matches
    elif high_confidence_count >= 1 or avg_score < 1.2:
        return "🟡 Medium", "medium"
    # Low confidence: poor matches
    else:
        return "🔴 Low", "low"


def clean_document_name(filename: str) -> str:
    """Clean up document filename for display"""
    name = Path(filename).stem
    # Replace underscores and hyphens with spaces, title case
    return name.replace("_", " ").replace("-", " ").title()

def main():
    """Main application"""
    
    # Header
    st.markdown('<h1 class="main-header">🔍 Manufacturing Spec Assistant</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #666; margin-bottom: 2rem;">
    Search across your FPC/PCB specifications instantly
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize RAG system
    rag_system = initialize_rag_system()
    
    if not rag_system:
        st.stop()
    
    # Sidebar - Knowledge Base
    st.sidebar.markdown("## 📚 Knowledge Base")

    # Show indexed documents
    if hasattr(rag_system, 'metadata') and rag_system.metadata:
        unique_files = set(meta['source_file'] for meta in rag_system.metadata)
        st.sidebar.markdown(f"**{len(unique_files)} specifications indexed**")
        st.sidebar.markdown("---")
        for file in sorted(unique_files):
            # Clean file name - remove extension and path
            clean_name = Path(file).stem.replace("_", " ").replace("-", " ")
            st.sidebar.markdown(f"📄 {clean_name}")
    else:
        st.sidebar.markdown("*Documents will appear here after first search*")
    
    # Main interface - Sample questions as clickable chips
    st.markdown("#### 💡 Try a sample question:")
    sample_questions = [
        "What is bending location tolerance?",
        "What is LPI or Solder mask thickness?",
        "What is FPC design guideline of De-cap?",
        "What is the bonding adhesive patch back?",
        "What is dimension of EMI shield to coverlay edge?",
        "What is FPC reflow test acceptance criteria?"
    ]

    # Initialize session state for query
    if 'query_text' not in st.session_state:
        st.session_state.query_text = ""
    if 'auto_search' not in st.session_state:
        st.session_state.auto_search = False

    # Create clickable chips using columns
    cols = st.columns(3)
    for idx, question in enumerate(sample_questions):
        with cols[idx % 3]:
            if st.button(question, key=f"sample_{idx}", use_container_width=True):
                st.session_state.query_text = question
                st.session_state.auto_search = True
                st.rerun()

    st.markdown("")  # Spacer

    # Query input
    query = st.text_input(
        "Or type your own question:",
        value=st.session_state.query_text,
        placeholder="e.g., What is bending location tolerance?",
        key="query_input"
    )

    # Update session state when text input changes
    if query != st.session_state.query_text:
        st.session_state.query_text = query
        st.session_state.auto_search = False

    col1, col2 = st.columns([1, 4])
    with col1:
        search_button = st.button("🔍 Search", type="primary")
    with col2:
        top_k = st.slider("Number of sources", 3, 10, 5)

    # Auto-search when sample question clicked
    if st.session_state.auto_search:
        search_button = True
        st.session_state.auto_search = False
    
    if search_button and query:
        # Build index on first query (lazy init)
        if not ensure_index_ready(rag_system):
            st.error("Unable to prepare the document search. Please refresh the page.")
            st.stop()
        
        start_time = time.time()
        
        with st.spinner("🔍 Searching specifications..."):
            result = rag_system.query(query, top_k=top_k)
        
        processing_time = time.time() - start_time
        
        if result['error']:
            # Friendly error message for no results
            if "No search results" in str(result['error']) or "no results" in str(result['error']).lower():
                st.warning("🔎 No exact match found in the knowledge base.")
                st.info("""
                **Try these suggestions:**
                - Rephrase your question with different keywords
                - Use more specific terms (e.g., "coverlay thickness" instead of "thickness")
                - Browse the indexed documents in the sidebar for available topics
                """)
            else:
                st.error(f"Something went wrong. Please try again or rephrase your question.")
        else:
            # Display results
            st.markdown("## 📋 Answer")

            # Get overall confidence
            confidence_label, confidence_level = get_overall_confidence(result['sources'])

            # Show confidence and response time
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**Confidence:** {confidence_label}")
            with col2:
                st.markdown(f"*Response time: {processing_time:.1f}s • {len(result['sources'])} sources found*")

            # Answer with styled box
            st.markdown(f"""
            <div style="background-color: #f0f7ff; border-left: 4px solid #1e3a5f; padding: 1rem; margin: 1rem 0; border-radius: 4px;">
            {result['answer']}
            </div>
            """, unsafe_allow_html=True)

            # Sources
            st.markdown("### 📚 Sources")

            if result['sources']:
                for i, source in enumerate(result['sources'], 1):
                    doc_name = clean_document_name(source['file'])
                    confidence = render_confidence_badge(source['score'], show_label=False)
                    with st.expander(f"{confidence} 📄 {doc_name}, Page {source['page']}"):
                        st.markdown(f"**From:** {doc_name}")
                        st.markdown(f"**Page:** {source['page']}")

                        st.markdown("**Relevant excerpt:**")
                        st.text(source['text_preview'])

                        # Show full text in a collapsible section
                        if st.button(f"View full context", key=f"full_text_{i}"):
                            st.text(source.get('full_text', 'Full text not available'))
            else:
                st.warning("No sources found")
    
    # Sidebar - About section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About")
    st.sidebar.markdown("Powered by AI • Searches across your FPC/PCB specifications")

    # Professional footer
    st.markdown("---")
    doc_count = 0
    if hasattr(rag_system, 'metadata') and rag_system.metadata:
        doc_count = len(set(meta['source_file'] for meta in rag_system.metadata))
    st.markdown(f"""
    <div style="text-align: center; color: #888; font-size: 0.9rem;">
    © 2026 • Powered by AI • {doc_count} specifications indexed
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()