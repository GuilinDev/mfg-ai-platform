#!/usr/bin/env python3
"""
Final test with specific query about bending location tolerance
"""
from simple_rag import SimpleRAGSystem

def main():
    # Initialize system
    print("Loading RAG system...")
    rag = SimpleRAGSystem()
    
    if rag.load_index("simple_rag_index"):
        print("✅ Index loaded successfully")
    else:
        print("❌ Failed to load index")
        return
    
    # Test specific query
    query = "What is bending location tolerance?"
    print(f"\n🔍 Query: {query}")
    print("=" * 60)
    
    result = rag.query(query, top_k=3)
    
    if result['error']:
        print(f"❌ Error: {result['error']}")
    else:
        print("📋 Answer:")
        print(result['answer'])
        print(f"\n📚 Found {len(result['sources'])} sources:")
        
        for i, source in enumerate(result['sources'], 1):
            print(f"\n{i}. {source['file']} (Page {source['page']}) - Score: {source['score']:.3f}")
            print(f"   Preview: {source['text_preview'][:150]}...")

if __name__ == "__main__":
    main()