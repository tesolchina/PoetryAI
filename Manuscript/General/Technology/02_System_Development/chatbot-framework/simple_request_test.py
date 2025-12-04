"""
Simple Poetry AI Request Builder - Based on your original code
Quick test version with fixes applied.
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def simple_poetry_request():
    """Simple request function based on your original code with improvements"""
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000"  # Better rate limits
    }
    
    # Fixed the payload - removed "models" array, use single "model"
    payload = {
        "model": "google/gemma-2-9b-it:free",  # Use working model from your config
        "messages": [
            {
                "role": "system", 
                "content": "You are a helpful creative writing assistant for English language learners working on poetry. Your role is to support students in exploring creative expression through collaborative writing."
            },
            {
                "role": "user",
                "content": "Poetry partner"
            }
        ],
        "temperature": 0.3,
        "top_p": 0.4,
        "stream": False  # Fixed: set to False for non-streaming
        # Note: removed "stream": True because print(response.json()) won't work with streaming
    }
    
    try:
        print("🔄 Sending request to OpenRouter...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        result = response.json()
        print("✅ Response received!")
        print("\n📋 Full Response:")
        print(json.dumps(result, indent=2))
        
        # Extract and display the assistant's message more clearly
        if 'choices' in result and len(result['choices']) > 0:
            assistant_message = result['choices'][0]['message']['content']
            print(f"\n🤖 Assistant Response:")
            print(f"{assistant_message}")
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON response: {e}")
        return None

if __name__ == "__main__":
    # Check API key
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found!")
        print("💡 Make sure your .env file is in the chatbot-framework directory")
    else:
        print("🔑 API Key loaded successfully")
        print("🚀 Testing Poetry AI...")
        simple_poetry_request()