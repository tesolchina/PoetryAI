"""
Fixed version of your original request builder
All issues corrected and ready to use with a valid API key.
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Your original request builder - FIXED VERSION
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:3000",  # Added for better rate limits
    "X-Title": "PoetryAI Research"  # Added for identification
}

payload = {
    # FIXED: Changed from "models" array to single "model" string
    "model": "google/gemma-2-9b-it:free",  # Use a working free model
    
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful creative writing assistant for English language learners working on poetry. Your role is to support students in exploring creative expression through collaborative writing"
        },
        {
            "role": "user",
            "content": "Poetry partner"
        }
    ],
    "temperature": 0.3,
    "top_p": 0.4,
    
    # FIXED: Set stream to False for simple JSON response
    "stream": False  # Changed from True to work with response.json()
}

# Make the request
try:
    print("🚀 Making request to OpenRouter...")
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    
    # Check for HTTP errors
    response.raise_for_status()
    
    # Parse and display response
    result = response.json()
    print("✅ Request successful!")
    print("\n📋 Response:")
    print(json.dumps(result, indent=2))
    
    # Extract assistant message
    if 'choices' in result and result['choices']:
        assistant_message = result['choices'][0]['message']['content']
        print(f"\n🤖 Assistant says:")
        print(f'"{assistant_message}"')
    
except requests.exceptions.HTTPError as e:
    print(f"❌ HTTP Error: {e}")
    if hasattr(e.response, 'text'):
        print(f"Response: {e.response.text}")
except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
except json.JSONDecodeError as e:
    print(f"❌ Failed to parse response as JSON: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n" + "="*50)
print("📝 NOTES ABOUT YOUR ORIGINAL CODE:")
print("1. ✅ FIXED: Changed 'models' array to single 'model' string")  
print("2. ✅ FIXED: Set 'stream': False to work with response.json()")
print("3. ⚠️  API KEY: You need a valid OpenRouter API key")
print("4. 💡 TIP: Visit https://openrouter.ai to get a new API key")
print("="*50)