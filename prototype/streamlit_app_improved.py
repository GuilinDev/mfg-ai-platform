#!/usr/bin/env python3
"""
Improved Streamlit app using PyMuPDF4LLM for better PDF parsing
"""
import os
import streamlit as st
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from src.utils.config import Config
from improved_rag_system import ImprovedRAGSystem

# Set page config
st.set_page_config(
    page_title="Manufacturing RAG Prototype (Improved)",
    page_icon="🏭",
    layout="wide"
)

# Initialize session state
if 'rag_system' not in st.session_state:
    st.session_state.rag_system = None
    st.session_state.index_loaded = False

def load_improved_rag_system():
    """Load the improved RAG system"""
    if st.session_state.rag_system is None:
        with st.spinner("Initializing improved RAG system..."):
            rag = ImprovedRAGSystem()
            
            # Try to load existing improved index
            if rag.load_index("improved_rag_index"):
                st.session_state.rag_system = rag
                st.session_state.index_loaded = True
                st.success("✅ Improved index loaded successfully!")
                st.info(f"📊 Loaded {len(rag.documents)} document chunks with PyMuPDF4LLM parsing")
            else:
                st.error("❌ Could not load improved index. Please rebuild it first.")
                st.session_state.index_loaded = False

def main():
    st.title("🏭 Manufacturing RAG Prototype (Improved)")
    st.markdown("**Enhanced with PyMuPDF4LLM for better PDF parsing quality**")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 System Info")
        
        # Configuration status
        config_status = Config.validate_config()
        st.subheader("Configuration")
        
        for key, status in config_status.items():
            icon = "✅" if status else "❌"
            st.write(f"{icon} {key.replace('_', ' ').title()}")
        
        st.divider()
        
        # Load system button
        if st.button("🔄 Load/Reload RAG System", type="primary"):
            st.session_state.rag_system = None
            load_improved_rag_system()
        
        # Index status
        if st.session_state.index_loaded:
            st.success("✅ System Ready")
            if st.session_state.rag_system:
                st.metric("Documents", len(st.session_state.rag_system.documents))
                st.metric("Method", "PyMuPDF4LLM")
        else:
            st.warning("⚠️ System Not Loaded")
    
    # Main content area
    if not st.session_state.index_loaded:
        load_improved_rag_system()
    
    if st.session_state.index_loaded and st.session_state.rag_system:
        # Query interface
        st.header("💬 Ask Questions About Manufacturing Specifications")
        
        # Example questions
        with st.expander("📝 Example Questions"):
            example_questions = [
                "What is bending location tolerance?",
                "What is LPI or Solder mask thickness?",
                "What is FPC design guideline of De-cap?",
                "What is the bonding adhesive patch back?",
                "What is dimension of EMI shield to coverlay edge?",
                "What is FPC reflow test acceptance criteria?",
                "What is laser drilling quality control plan?",
                "What is UPD?",
                "What is CQRA of FPC line qualification?"
            ]
            
            for i, q in enumerate(example_questions, 1):
                st.write(f"{i}. {q}")
        
        # Query input
        query = st.text_input(
            "Enter your question:",
            placeholder="e.g., What is the minimum trace width for FPC design?",
            help="Ask about manufacturing specifications, tolerances, quality control, etc."
        )
        
        # Advanced options
        with st.expander("⚙️ Advanced Options"):
            top_k = st.slider("Number of sources to retrieve", 1, 10, 5)
            show_sources = st.checkbox("Show detailed source information", True)
        
        # Process query
        if query:
            with st.spinner("🔍 Searching documents and generating answer..."):
                try:
                    result = st.session_state.rag_system.query(query, top_k=top_k)
                    
                    if result['error']:
                        st.error(f"❌ Error: {result['error']}")
                    else:
                        # Display answer
                        st.subheader("📋 Answer")
                        st.write(result['answer'])
                        
                        # Display sources
                        if show_sources and result['sources']:
                            st.subheader("📚 Sources")
                            
                            for i, source in enumerate(result['sources'], 1):
                                with st.expander(f"Source {i}: {source['file']} (Score: {source['score']:.3f})"):
                                    st.write("**File:**", source['file'])
                                    st.write("**Chunk ID:**", source['chunk_id'])
                                    st.write("**Relevance Score:**", f"{source['score']:.3f}")
                                    st.write("**Text Preview:**")
                                    st.text_area("Content", source['text_preview'], height=100, key=f"source_{i}")
                        
                        # Query metadata
                        with st.expander("🔍 Query Details"):
                            st.json({
                                "query": result['query'],
                                "sources_found": len(result['sources']),
                                "extraction_method": "PyMuPDF4LLM"
                            })
                
                except Exception as e:
                    st.error(f"❌ Unexpected error: {str(e)}")
        
        # Performance comparison
        st.divider()
        
        with st.expander("📊 Performance Comparison"):
            st.subheader("Baseline vs Improved Results")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Baseline Accuracy",
                    "11.1%",
                    help="Original PyMuPDF basic text extraction"
                )
            
            with col2:
                st.metric(
                    "Improved Accuracy", 
                    "55.6%",
                    delta="+44.5pp",
                    help="PyMuPDF4LLM with markdown output"
                )
            
            with col3:
                st.metric(
                    "Document Chunks",
                    "1,203",
                    delta="+893",
                    help="Processed document chunks"
                )
            
            st.info("🎯 **Key Improvements:** Better table extraction, reduced header noise, improved technical content capture")
    
    else:
        # System not ready
        st.warning("⚠️ RAG System not loaded. Please check the configuration and try reloading.")
        
        with st.expander("🔧 Troubleshooting"):
            st.write("**Common issues:**")
            st.write("1. Missing GROQ_API_KEY environment variable")
            st.write("2. Improved index files not found (need to rebuild)")
            st.write("3. Documents directory not accessible")
            
            st.write("**To rebuild the improved index:**")
            st.code("""
cd /home/guilinzhang/allProjects/mfg-ai-platform/prototype
python3 improved_rag_system.py
""")

    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: gray;'>
    Manufacturing RAG Prototype - Enhanced with PyMuPDF4LLM<br>
    Improved PDF parsing for better technical specification extraction
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()