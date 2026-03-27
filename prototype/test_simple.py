#!/usr/bin/env python3
"""
Simple test of Groq LLM without embeddings
"""
import os
from openai import OpenAI

# Test Groq API directly
def test_groq_direct():
    print("=== Testing Groq API Directly ===")
    
    groq_client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )
    
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is bending location tolerance in FPC manufacturing?"}
            ],
            temperature=0.1,
            max_tokens=500
        )
        
        print("✓ Groq API call successful")
        print(f"Response: {response.choices[0].message.content[:200]}...")
        return True
        
    except Exception as e:
        print(f"✗ Groq API call failed: {e}")
        return False

if __name__ == "__main__":
    test_groq_direct()