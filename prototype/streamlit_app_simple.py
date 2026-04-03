# Manufacturing AI RAG Prototype - Streamlit Application (Simple Version)
import streamlit as st
import os
import sys
from pathlib import Path
import time
from typing import Dict, List, Any
import json

# Add parent dir to path for simple_rag import
sys.path.insert(0, str(Path(__file__).parent))

# Import both SimpleRAGSystem and Config from simple_rag (Config is inlined there)
from simple_rag import SimpleRAGSystem, Config

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

INDEX_VERSION = "v4"  # Bump this to force index rebuild after doc changes

@st.cache_resource
def initialize_rag_system():
    """Initialize the simple RAG system (lazy — index built on first query)"""
    try:
        rag = SimpleRAGSystem()
        index_name = f"simple_rag_index_{INDEX_VERSION}"

        # Try to load existing index (fast, no API calls)
        if rag.load_index(index_name):
            rag._ready = True
            rag._index_name = index_name
        else:
            rag._ready = False  # Will build on first query
            rag._index_name = index_name

        return rag

    except Exception as e:
        st.error("Unable to start the search system. Please refresh the page or contact support.")
        return None

def ensure_index_ready(rag):
    """Build index on demand, not at startup"""
    if getattr(rag, '_ready', False):
        return True
    index_name = getattr(rag, '_index_name', f"simple_rag_index_{INDEX_VERSION}")
    with st.spinner("🔄 Preparing your document search... (first time only, ~1 min)"):
        rag.process_pdfs(Config.DATA_DIR)
        rag.build_index()
        rag.save_index(index_name)
    rag._ready = True
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

    # FAISS L2 distance: lower = better. Typical range 0.5-2.0
    if len(sources) >= 3 and avg_score < 1.5:
        return "🟢 High", "high"
    elif len(sources) >= 1 and avg_score < 2.0:
        return "🟡 Medium", "medium"
    else:
        return "🔴 Low", "low"


def clean_document_name(filename: str) -> str:
    """Clean up document filename for display"""
    name = Path(filename).stem
    # Replace underscores and hyphens with spaces, title case
    return name.replace("_", " ").replace("-", " ").title()


def get_pdf_files_from_data_dir() -> List[str]:
    """Scan data directory for PDF files and return cleaned names"""
    data_path = Path(Config.DATA_DIR)
    if not data_path.exists():
        return []
    pdf_files = list(data_path.glob("*.pdf"))
    return sorted([clean_document_name(f.name) for f in pdf_files])


def fallback_llm_answer(rag_system, query: str) -> str:
    """Call Groq LLM directly when no knowledge base results found"""
    try:
        response = rag_system.groq_client.chat.completions.create(
            model=Config.LLM_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for manufacturing and electronics questions. Provide clear, concise answers."},
                {"role": "user", "content": query}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Unable to generate a response. Please try again later."


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

    # Sidebar - Knowledge Base (Fix 4: Show documents immediately)
    st.sidebar.markdown("## 📚 Knowledge Base")

    # Show indexed documents if available, otherwise show PDF files from data directory
    if hasattr(rag_system, 'metadata') and rag_system.metadata:
        unique_files = set(meta['source_file'] for meta in rag_system.metadata)
        st.sidebar.markdown(f"**{len(unique_files)} specifications indexed**")
        st.sidebar.markdown("---")
        for file in sorted(unique_files):
            clean_name = Path(file).stem.replace("_", " ").replace("-", " ")
            st.sidebar.markdown(f"📄 {clean_name}")
    else:
        # Show PDF files from data directory immediately
        pdf_files = get_pdf_files_from_data_dir()
        if pdf_files:
            st.sidebar.markdown(f"**{len(pdf_files)} specifications available**")
            st.sidebar.markdown("---")
            for name in pdf_files:
                st.sidebar.markdown(f"📄 {name}")
        else:
            st.sidebar.markdown("*No documents found in data directory*")

    # Main interface - Sample questions as clickable chips
    st.markdown("#### 💡 Try a sample question:")
    sample_questions = [
        "What is bending location tolerance?",
        "What is LPI or Solder mask thickness?",
        "What is FPC design guideline of De-cap?",
        "What is yield of P2 of V53 UAT1 in ICT?",
        "What is top 1 issue of P2 of V53 UAT1 in AMP?",
        "What are the B2B stiffener specifications?",
    ]

    # Initialize session state for query
    if 'query_text' not in st.session_state:
        st.session_state.query_text = ""
    if 'trigger_search' not in st.session_state:
        st.session_state.trigger_search = False

    # Create clickable chips using columns (Fix 5: Auto-search on click)
    cols = st.columns(3)
    for idx, question in enumerate(sample_questions):
        with cols[idx % 3]:
            if st.button(question, key=f"sample_{idx}", use_container_width=True):
                st.session_state.query_text = question
                st.session_state.trigger_search = True
                st.rerun()

    st.markdown("")  # Spacer

    # Fix 2: Use form for Enter key submission
    with st.form(key="search_form", clear_on_submit=False):
        query = st.text_input(
            "Or type your own question:",
            value=st.session_state.query_text,
            placeholder="e.g., What is bending location tolerance?",
            key="query_input"
        )
        submit_button = st.form_submit_button("🔍 Search", type="primary")

    # Update session state when form submitted
    if submit_button:
        st.session_state.query_text = query
        st.session_state.trigger_search = True

    # Determine if we should search
    should_search = st.session_state.trigger_search and st.session_state.query_text

    # Reset trigger after checking
    if st.session_state.trigger_search:
        st.session_state.trigger_search = False

    if should_search:
        query = st.session_state.query_text

        # Build index on first query (lazy init)
        if not ensure_index_ready(rag_system):
            st.error("Unable to prepare the document search. Please refresh the page.")
            st.stop()

        start_time = time.time()

        with st.spinner("🔍 Searching specifications..."):
            result = rag_system.query(query, top_k=5)  # Fix 1: Hardcoded top_k=5

        processing_time = time.time() - start_time

        if result['error']:
            # No results — tell user clearly, no fabrication
            if "No search results" in str(result['error']) or "no results" in str(result['error']).lower():
                st.markdown("## 📋 Answer")
                st.warning("⚠️ No matching information found in the uploaded documents.")

                st.info("""
                **Tips:**
                - Rephrase your question with different keywords
                - Use more specific terms (e.g., "coverlay thickness" instead of "thickness")
                - Browse the indexed documents in the sidebar for available topics
                """)
            else:
                st.error(f"Something went wrong. Please try again or rephrase your question.")
        else:
            # Display results
            st.markdown("## 📋 Answer")

            # Show response time and source count
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
                    with st.expander(f"📄 {doc_name}, Page {source['page']}"):
                        st.markdown(f"**From:** {doc_name}")
                        st.markdown(f"**Page:** {source['page']}")

                        st.markdown("**Relevant excerpt:**")
                        st.text(source['text_preview'])

                        # Render source PDF page as image
                        try:
                            import fitz
                            source_file = source.get('file', '')
                            page_num = source.get('page', 1)
                            pdf_path = Path(Config.DATA_DIR) / source_file
                            if pdf_path.exists() and source_file.endswith('.pdf'):
                                doc = fitz.open(str(pdf_path))
                                if 0 < page_num <= len(doc):
                                    page = doc[page_num - 1]
                                    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
                                    img_bytes = pix.tobytes("png")
                                    st.image(img_bytes, caption=f"{source_file} — Page {page_num}", use_container_width=True)
                                doc.close()
                        except Exception:
                            pass  # Silently skip if PDF rendering fails

                        # Show full text in a collapsible section
                        with st.expander("View Full Context"):
                            st.text(source.get('full_text', source.get('text_preview', 'Full text not available')))
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
    else:
        doc_count = len(get_pdf_files_from_data_dir())
    st.markdown(f"""
    <div style="text-align: center; color: #888; font-size: 0.9rem;">
    © 2026 • Powered by AI • {doc_count} specifications indexed
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
# v1774664921
