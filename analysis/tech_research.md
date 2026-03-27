# Technology Research Report
## Manufacturing AI RAG Prototype - Phase 2

**Date:** March 26, 2026  
**Analyst:** Manufacturing AI PM/Tech Lead  

---

## Executive Summary

Evaluated deployment platforms, RAG frameworks, LLMs, and document processing libraries for a manufacturing AI RAG prototype. Key recommendations: **Streamlit Cloud** for deployment, **LlamaIndex** for RAG, **OpenAI GPT-4o** for LLM, **PyMuPDF + python-pptx + PaddleOCR** for document processing, **FAISS + OpenAI Embeddings** for vector store. Focus on offline-capable demo with superior retrieval quality.

---

## 1. Deployment Platform Analysis

### Streamlit Community Cloud ⭐ **RECOMMENDED**
**Pros:**
- ✅ **Free Hosting** for public repositories
- ✅ **Easy Deployment** - Git-based auto-deployment  
- ✅ **Python Native** - Perfect for ML/AI prototypes
- ✅ **Custom Domains** available
- ✅ **Resource Limits** reasonable for demo (1GB RAM, 800 MB storage)
- ✅ **Environment Control** via requirements.txt + packages.txt

**Cons:**
- ⚠️ **Public Repository Required** - Need to sanitize proprietary data
- ⚠️ **Limited Compute** - No GPU support
- ⚠️ **Timeout Limits** - 10min max execution time

**Suitability for Use Case:** 9/10 - Ideal for demo deployment with data sanitization

### Hugging Face Spaces
**Pros:**
- ✅ **Free GPU** available (limited hours)
- ✅ **ML-Focused** community and tooling
- ✅ **Model Integration** with HF ecosystem
- ✅ **Multiple Frameworks** (Streamlit, Gradio, Flask)

**Cons:**
- ⚠️ **Slower Cold Starts** especially for CPU spaces
- ⚠️ **Resource Competition** during peak hours
- ⚠️ **Complex Setup** for non-HF models

**Suitability for Use Case:** 7/10 - Good alternative if GPU needed

### Gradio (Standalone)  
**Pros:**
- ✅ **Rapid Prototyping** - Minimal code for UI
- ✅ **Auto-Documentation** of API
- ✅ **Easy Sharing** via public links

**Cons:**
- ⚠️ **Limited UI Customization** compared to Streamlit
- ⚠️ **Hosting Dependency** - Needs platform (HF Spaces or cloud)

**Suitability for Use Case:** 6/10 - Good for quick demos but limited customization

**Decision: Streamlit Community Cloud** - Best balance of features, cost, and demo requirements

---

## 2. RAG Framework Comparison

### LlamaIndex ⭐ **RECOMMENDED**
**Pros:**
- ✅ **Document-Centric Design** - Built specifically for RAG over documents
- ✅ **Multi-Modal Support** - Text, tables, images in single pipeline
- ✅ **Source Attribution** - Built-in citation and metadata preservation
- ✅ **Advanced Chunking** - Hierarchical and semantic splitting strategies
- ✅ **Query Engines** - Multiple retrieval strategies (vector, keyword, hybrid)
- ✅ **Observability** - Built-in logging and evaluation tools
- ✅ **Active Development** - Rapid feature updates, strong community

**Cons:**
- ⚠️ **Learning Curve** - More complex than simple vector search
- ⚠️ **Memory Usage** - Can be resource-intensive for large documents

**Code Example:**
```python
from llama_index import Document, VectorStoreIndex, ServiceContext
from llama_index.readers import PDFReader, PptxReader
from llama_index.node_parser import SimpleNodeParser

# Multi-format document loading
pdf_reader = PDFReader()
pptx_reader = PptxReader()
documents = pdf_reader.load_data("specs.pdf") + pptx_reader.load_data("reports.pptx")

# Build index with source tracking
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(response_mode="tree_summarize")
```

### LangChain
**Pros:**
- ✅ **Mature Ecosystem** - Extensive integrations and tools
- ✅ **Agent Framework** - Good for complex workflows
- ✅ **Memory Management** - Conversation state handling
- ✅ **Production Ready** - Battle-tested in enterprise

**Cons:**
- ⚠️ **General Purpose** - Not optimized specifically for document RAG
- ⚠️ **Complex Abstractions** - Can be overkill for focused use cases  
- ⚠️ **Citation Tracking** - Requires custom implementation
- ⚠️ **Breaking Changes** - Frequent API changes

### Lightweight Custom (FAISS + OpenAI)
**Pros:**
- ✅ **Full Control** - Custom chunking and retrieval logic
- ✅ **Minimal Dependencies** - Easier deployment
- ✅ **Performance** - Optimized for specific use case

**Cons:**
- ⚠️ **Development Time** - Need to implement RAG components from scratch
- ⚠️ **Maintenance Burden** - No community support for custom code
- ⚠️ **Feature Gap** - Missing advanced RAG features (re-ranking, etc.)

**Decision: LlamaIndex** - Purpose-built for document RAG with excellent source attribution

---

## 3. Large Language Model Selection

### OpenAI GPT-4o ⭐ **RECOMMENDED** (Prototype Phase)
**Pros:**
- ✅ **Superior Quality** - Best-in-class reasoning and extraction
- ✅ **Multi-Modal** - Native image + text processing for drawings  
- ✅ **Reliable API** - 99.9% uptime, consistent performance
- ✅ **128K Context** - Can handle large document chunks
- ✅ **JSON Mode** - Structured output for Excel generation
- ✅ **Client Approval** - Explicitly approved for prototype phase

**Cons:**
- 💰 **Cost** - $10/1M input tokens, $30/1M output tokens
- ⚠️ **External Dependency** - Requires internet for inference
- ⚠️ **Rate Limits** - May need queuing for batch processing

**Cost Estimation for Demo:**
- Embedding 1000 pages: ~$2
- 100 queries during demo: ~$20  
- **Total Demo Cost: ~$25**

### Free Alternatives Analysis

#### Qwen2.5-72B (Future Production)
**Pros:**
- ✅ **Free** - No per-token costs after deployment
- ✅ **Privacy** - Fully local inference  
- ✅ **Customizable** - Fine-tuning possible

**Cons:**
- ⚠️ **Hardware Requirements** - Needs significant GPU resources  
- ⚠️ **Setup Complexity** - Model deployment and optimization
- ⚠️ **Quality Gap** - Likely performance degradation vs GPT-4o

#### Ollama + Llama-3.1-70B
**Pros:**
- ✅ **Local Deployment** - No external API calls
- ✅ **Good Performance** - Competitive with commercial models

**Cons:**
- ⚠️ **Resource Intensive** - 80GB+ RAM requirement
- ⚠️ **Slow Inference** - Without GPU acceleration

**Decision: OpenAI GPT-4o for prototype** - Quality and reliability critical for client demo

---

## 4. Document Processing Library Analysis

### PDF Processing

#### PyMuPDF (fitz) ⭐ **RECOMMENDED**
**Pros:**
- ✅ **High Performance** - Fast C++ backend
- ✅ **Rich Extraction** - Text, images, tables, metadata
- ✅ **Layout Preservation** - Maintains spatial relationships  
- ✅ **Table Detection** - Built-in table extraction capabilities
- ✅ **Already Available** - Tested in our environment

**Code Example:**
```python
import fitz
doc = fitz.open("specs.pdf")
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    tables = page.find_tables()  # Built-in table detection
    metadata = {"source": f"page_{page_num}", "doc": "specs.pdf"}
```

#### pdfplumber  
**Pros:**
- ✅ **Table Focused** - Excellent table extraction
- ✅ **Precise Layout** - Character-level positioning

**Cons:**
- ⚠️ **Slower** - Pure Python implementation
- ⚠️ **Memory Usage** - Higher overhead for large PDFs

#### Unstructured
**Pros:**
- ✅ **AI-Powered** - Intelligent document understanding
- ✅ **Multi-format** - Single API for many formats

**Cons:**
- ⚠️ **External Dependency** - Requires API calls or complex setup
- ⚠️ **Cost** - Premium features require subscription

### PowerPoint Processing

#### python-pptx ⭐ **RECOMMENDED**
**Pros:**
- ✅ **Native Support** - Direct PowerPoint file manipulation
- ✅ **Complete Access** - Text, images, shapes, slide metadata
- ✅ **Generation Capable** - Can create new presentations
- ✅ **Already Installed** - Available in our environment

**Code Example:**
```python
from pptx import Presentation

# Reading
prs = Presentation("postmortem.pptx")
for i, slide in enumerate(prs.slides):
    for shape in slide.shapes:
        if hasattr(shape, 'text'):
            text = shape.text
            metadata = {"slide": i+1, "source": "postmortem.pptx"}

# Generation
from pptx import Presentation
new_prs = Presentation("template.pptx")  
# Add content to slides
new_prs.save("generated_report.pptx")
```

### Engineering Drawing OCR

#### PaddleOCR ⭐ **RECOMMENDED**
**Pros:**
- ✅ **High Accuracy** - State-of-the-art OCR performance  
- ✅ **Multi-Language** - Supports technical terminology
- ✅ **Table Detection** - Can identify tabular structures
- ✅ **Free** - Open source, no API costs
- ✅ **CPU Capable** - Works without GPU (slower but functional)

**Installation:**
```bash
pip install paddlepaddle paddleocr
```

#### Tesseract OCR
**Pros:**
- ✅ **Mature** - Long-established, reliable
- ✅ **Lightweight** - Minimal system requirements
- ✅ **Free** - Open source

**Cons:**
- ⚠️ **Lower Accuracy** - Especially on technical drawings
- ⚠️ **Limited Table Support** - Requires additional processing

**Decision: PyMuPDF + python-pptx + PaddleOCR** - Optimal balance of performance and capabilities

---

## 5. Vector Store Analysis

### FAISS ⭐ **RECOMMENDED**
**Pros:**
- ✅ **High Performance** - Optimized similarity search
- ✅ **Memory Efficient** - Compressed vector storage
- ✅ **Offline** - No external dependencies after index creation
- ✅ **Scalable** - Handles large document collections
- ✅ **Free** - No usage costs

**Code Example:**
```python
import faiss
from sentence_transformers import SentenceTransformer

# Create index
dimension = 384  # For all-MiniLM-L6-v2
index = faiss.IndexFlatL2(dimension)

# Add vectors
embeddings = model.encode(texts)
index.add(embeddings)

# Save for offline use
faiss.write_index(index, "document_index.faiss")
```

#### Chroma
**Pros:**
- ✅ **Simple API** - Easy to use
- ✅ **Metadata Support** - Built-in filtering
- ✅ **Persistence** - Automatic saving

**Cons:**
- ⚠️ **Performance** - Slower than FAISS for large datasets
- ⚠️ **Memory Usage** - Higher overhead

#### Pinecone
**Pros:**
- ✅ **Managed Service** - No infrastructure management
- ✅ **Real-time Updates** - Dynamic index modification

**Cons:**
- 💰 **Cost** - Usage-based pricing
- ⚠️ **External Dependency** - Internet required

**Decision: FAISS** - Best performance and offline capability for demo

---

## 6. Embedding Model Analysis

### OpenAI text-embedding-ada-002 ⭐ **RECOMMENDED** (Prototype)
**Pros:**
- ✅ **High Quality** - Optimized for diverse content types
- ✅ **Consistent Performance** - Reliable API
- ✅ **1536 Dimensions** - Rich representation space
- ✅ **Technical Content** - Good performance on engineering documents

**Cost:** $0.0001/1K tokens (~$2 for full document corpus)

### Free Alternatives

#### all-MiniLM-L6-v2 (Sentence Transformers)
**Pros:**
- ✅ **Free** - No API costs
- ✅ **Fast** - Efficient inference
- ✅ **Offline** - Local processing

**Cons:**
- ⚠️ **Quality Gap** - Lower performance on technical content
- ⚠️ **Context Length** - 256 token limit

#### text2vec-large-chinese (for Chinese content in templates)
**Pros:**
- ✅ **Bilingual** - Handles Chinese text in PPT templates
- ✅ **Free** - Open source

**Cons:**
- ⚠️ **Specialized** - May not perform well on technical English

**Decision: OpenAI Embeddings for prototype** - Quality critical for client demo

---

## 7. OCR Pipeline Design for Engineering Drawings

### Recommended Architecture
```
Engineering Drawing PDF
         ↓
    [PyMuPDF] Extract pages as images  
         ↓
    [PaddleOCR] Text detection + recognition
         ↓
    [Post-processing] Clean and structure extracted text
         ↓
    [Spatial Analysis] Associate text with drawing elements
         ↓  
    [Classification] Categorize into 28 target elements
         ↓
    [Excel Export] Structured output generation
```

### Implementation Strategy
1. **Image Preprocessing:** Convert PDF pages to high-resolution images
2. **OCR Processing:** Use PaddleOCR for text extraction with bounding boxes
3. **Text Cleanup:** Remove OCR artifacts, standardize formatting
4. **Spatial Clustering:** Group related text elements by proximity
5. **Pattern Matching:** Identify tolerance patterns (±), material specs, dimensions
6. **Classification:** Map extracted elements to the 28 target categories
7. **Excel Generation:** Use openpyxl to create structured output

### Accuracy Considerations
- **OCR Confidence Scoring:** Filter low-confidence extractions
- **Validation Rules:** Check for expected patterns (dimension formats, etc.)
- **Human Review Flags:** Mark uncertain extractions for manual verification

---

## 8. Cost Analysis for Prototype

### API Costs (OpenAI)
| Component | Usage | Cost |
|-----------|-------|------|
| Document Embedding | 1000 pages (~500K tokens) | $0.05 |
| Query Processing | 100 demo queries | $20.00 |
| Image Analysis (Drawings) | 50 images | $15.00 |
| **Total Prototype Cost** | | **~$35** |

### Development Time Estimate
| Phase | Estimated Hours |
|-------|----------------|
| Use Case 1 (PDF RAG) | 16 hours |
| Use Case 2 (PPT + Generation) | 24 hours |
| Use Case 3 (Drawing + Excel) | 32 hours |
| Integration + UI | 16 hours |
| Testing + Refinement | 16 hours |
| **Total Development** | **104 hours** |

### Infrastructure Costs
- **Streamlit Cloud:** Free
- **Development Environment:** Existing
- **Storage:** Minimal (documents already provided)

**Total Prototype Budget: ~$35 in API costs**

---

## 9. Technology Stack Summary

### Final Recommended Stack ⭐

| Component | Technology | Rationale |
|-----------|------------|-----------|
| **Deployment** | Streamlit Community Cloud | Free, easy, Python-native |
| **RAG Framework** | LlamaIndex | Document-focused, source attribution |
| **LLM** | OpenAI GPT-4o | Quality critical for demo |
| **Embeddings** | OpenAI text-embedding-ada-002 | Consistency with LLM |
| **Vector Store** | FAISS | Performance + offline capability |
| **PDF Processing** | PyMuPDF (fitz) | Fast, comprehensive |
| **PPT Processing** | python-pptx | Native PowerPoint support |
| **OCR** | PaddleOCR | High accuracy for technical drawings |
| **Excel Generation** | openpyxl | Structured data export |
| **UI Framework** | Streamlit | Rapid prototyping |

### Alternative Stack (Cost-Optimized)

| Component | Technology | Trade-offs |
|-----------|------------|------------|
| **LLM** | Ollama + Llama-3.1-70B | Free but requires significant hardware |
| **Embeddings** | all-MiniLM-L6-v2 | Free but lower quality |
| **Deployment** | Local Gradio | No hosting costs but less accessible |

---

## Next Phase: Architecture Design

Key architectural decisions to detail:
1. **System Integration** - How components interact for each use case
2. **Data Pipeline Flow** - Document processing → Indexing → Retrieval → Generation  
3. **Error Handling** - Graceful failures and confidence scoring
4. **Performance Optimization** - Caching strategies and response times
5. **Security Considerations** - Handling confidential data in demo environment

This technology research provides the foundation for creating a robust, demo-ready manufacturing AI RAG prototype that balances quality, performance, and cost considerations.