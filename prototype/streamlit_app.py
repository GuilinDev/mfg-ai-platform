# Manufacturing AI RAG Prototype - Streamlit Application
import streamlit as st
import os
import sys
from pathlib import Path
import time
from typing import Dict, List, Any

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from src.utils.config import Config
from src.processors.pdf_processor import PDFProcessor
from src.engines.index_manager import IndexManager
from src.engines.query_engine import MultiModalQueryEngine

# Page configuration
st.set_page_config(
    page_title="Manufacturing AI RAG Demo",
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
.use-case-header {
    font-size: 1.5rem;
    font-weight: bold;
    color: #2c5aa0;
    margin: 1rem 0;
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
.metric-container {
    background-color: #e9ecef;
    border-radius: 10px;
    padding: 1rem;
    margin: 0.5rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def initialize_system():
    """Initialize the RAG system components"""
    try:
        # Validate configuration
        config_status = Config.validate_config()
        
        if not config_status["groq_api_key"]:
            st.error("Groq API key not found. Please set GROQ_API_KEY environment variable.")
            return None, None
            
        # Initialize components
        index_manager = IndexManager()
        query_engine = MultiModalQueryEngine(index_manager)
        
        return index_manager, query_engine
        
    except Exception as e:
        st.error(f"Error initializing system: {str(e)}")
        return None, None

@st.cache_data
def build_pdf_index(_index_manager):
    """Build the PDF specification index"""
    try:
        processor = PDFProcessor()
        documents = []
        
        # Process PDF files
        pdf_dir = Path(Config.DATA_DIR)
        pdf_files = list(pdf_dir.glob("*.pdf"))
        
        if not pdf_files:
            st.warning("No PDF files found in data directory")
            return None
            
        with st.spinner(f"Processing {len(pdf_files)} PDF files..."):
            for pdf_file in pdf_files:
                docs = processor.process_file(str(pdf_file))
                documents.extend(docs)
                
        if documents:
            with st.spinner("Building search index..."):
                index = _index_manager.build_index(documents, 'specification', force_rebuild=True)
                return index
        else:
            st.error("No documents processed successfully")
            return None
            
    except Exception as e:
        st.error(f"Error building PDF index: {str(e)}")
        return None

def render_confidence_badge(confidence: float) -> str:
    """Render confidence score as colored badge"""
    if confidence >= 0.8:
        return f'<span class="confidence-high">🟢 {confidence:.1%} Confidence</span>'
    elif confidence >= 0.6:
        return f'<span class="confidence-medium">🟡 {confidence:.1%} Confidence</span>'
    else:
        return f'<span class="confidence-low">🔴 {confidence:.1%} Confidence</span>'

def render_sources(sources: List[Dict[str, Any]]):
    """Render source citations"""
    if not sources:
        st.warning("No sources found")
        return
        
    st.markdown("### 📚 Sources")
    
    for i, source in enumerate(sources, 1):
        with st.expander(f"Source {i}: {source.get('file', 'Unknown')} - Page {source.get('page', 'Unknown')}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**File:** {source.get('file', 'Unknown')}")
                st.markdown(f"**Page:** {source.get('page', 'Unknown')}")
                st.markdown(f"**Section:** {source.get('section', 'Unknown')}")
                
            with col2:
                st.markdown(f"**Document Type:** {source.get('document_type', 'Unknown')}")
                st.markdown(f"**Confidence:** {source.get('confidence', 0):.3f}")
                
            st.markdown("**Text Preview:**")
            st.text(source.get('text_preview', 'No preview available'))

def main():
    """Main application"""
    
    # Header
    st.markdown('<h1 class="main-header">🏭 Manufacturing AI RAG Demo</h1>', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; color: #666; margin-bottom: 2rem;">
    Advanced Document Retrieval for FPC/PCB Manufacturing - Confidential Demo
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize system
    index_manager, query_engine = initialize_system()
    
    if not index_manager or not query_engine:
        st.stop()
    
    # Sidebar navigation
    st.sidebar.markdown("## 🎯 Navigation")
    use_case = st.sidebar.radio(
        "Select Use Case:",
        ["📄 PDF Specifications", "📊 PPT Analysis", "🔧 Drawing Analysis"],
        key="use_case_selector"
    )
    
    # System status
    with st.sidebar.expander("🔧 System Status"):
        config_status = Config.validate_config()
        
        for check, status in config_status.items():
            icon = "✅" if status else "❌"
            st.markdown(f"{icon} {check.replace('_', ' ').title()}")
            
        # Index status
        indices_info = index_manager.list_indices()
        st.markdown("**Indices Status:**")
        for doc_type, info in indices_info.items():
            if info.get('exists', False):
                st.markdown(f"✅ {doc_type}: {info.get('num_documents', 'Unknown')} docs")
            else:
                st.markdown(f"❌ {doc_type}: Not built")
    
    # Main content area
    if use_case == "📄 PDF Specifications":
        render_pdf_specifications_tab(index_manager, query_engine)
    elif use_case == "📊 PPT Analysis":
        render_ppt_analysis_tab(index_manager, query_engine)
    elif use_case == "🔧 Drawing Analysis":
        render_drawing_analysis_tab(index_manager, query_engine)

def render_pdf_specifications_tab(index_manager, query_engine):
    """Render PDF specifications interface"""
    
    st.markdown('<h2 class="use-case-header">📄 PDF Specification Query</h2>', unsafe_allow_html=True)
    
    # Check if index exists
    spec_index = index_manager.get_index('specification')
    
    if not spec_index:
        st.warning("PDF index not found. Building index...")
        spec_index = build_pdf_index(index_manager)
        
        if not spec_index:
            st.error("Failed to build PDF index. Please check your data files.")
            return
    
    # Sample questions
    st.markdown("### 💡 Sample Questions")
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
    
    if search_button and query:
        with st.spinner("Searching specifications..."):
            response = query_engine.query_specifications(query)
            
        if response.error:
            st.error(f"Error: {response.error}")
            return
            
        # Display results
        st.markdown("### 📋 Answer")
        
        # Confidence badge
        st.markdown(render_confidence_badge(response.confidence), unsafe_allow_html=True)
        
        # Answer
        st.markdown(f"**Answer:** {response.answer}")
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Query Type", response.query_type.replace('_', ' ').title())
        with col2:
            st.metric("Processing Time", f"{response.processing_time:.2f}s")
        with col3:
            st.metric("Sources Found", len(response.sources))
            
        # Sources
        render_sources(response.sources)

def render_ppt_analysis_tab(index_manager, query_engine):
    """Render PowerPoint analysis interface"""
    
    st.markdown('<h2 class="use-case-header">📊 PowerPoint Analysis</h2>', unsafe_allow_html=True)
    
    st.info("🚧 PowerPoint analysis functionality is under development. This will include:")
    st.markdown("""
    - Analysis of AMP and ICT postmortem reports
    - Yield comparison and issue analysis  
    - Automated PowerPoint report generation
    - Cross-platform FMEA comparison
    """)
    
    # Placeholder for PPT functionality
    query = st.text_input("PowerPoint query (demo):", placeholder="e.g., What is yield of P2 of V53 UAT1 in ICT?")
    
    if st.button("Analyze (Demo)", type="primary"):
        with st.spinner("Analyzing presentations..."):
            time.sleep(2)  # Simulate processing
            
        st.success("Demo Response: 0.9734 (97.34% yield)")
        st.info("Source: ICT_V53_P2_Postmortem.pptx, Slide 15")

def render_drawing_analysis_tab(index_manager, query_engine):
    """Render engineering drawing analysis interface"""
    
    st.markdown('<h2 class="use-case-header">🔧 Engineering Drawing Analysis</h2>', unsafe_allow_html=True)
    
    st.info("🚧 Drawing analysis functionality is under development. This will include:")
    st.markdown("""
    - OCR extraction from engineering drawings
    - Identification of 28 key elements (stiffeners, adhesives, etc.)
    - Excel report generation with structured data
    - Confidence scoring for extractions
    """)
    
    # File upload placeholder
    uploaded_file = st.file_uploader("Upload Engineering Drawing", type=['pdf'])
    
    if uploaded_file:
        st.success(f"File uploaded: {uploaded_file.name}")
        
        if st.button("Analyze Drawing (Demo)", type="primary"):
            with st.spinner("Processing drawing with OCR..."):
                time.sleep(3)  # Simulate processing
                
            st.success("Analysis complete!")
            
            # Demo results
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### ✅ Elements Found")
                st.markdown("- 🟢 B2B stiffener (89% confidence)")
                st.markdown("- 🟢 Copper layers (94% confidence)")  
                st.markdown("- 🟢 Bending specifications (76% confidence)")
                
            with col2:
                st.markdown("### ⚠️ Elements with Issues")
                st.markdown("- 🟡 PSA information (45% confidence)")
                st.markdown("- 🔴 TSA information (Not found)")
                
            st.download_button(
                "📥 Download Excel Report", 
                data="Demo Excel Data",
                file_name="drawing_analysis.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()