"""
API Key Validation Test
Tests if the API key is valid by making a simple request to OpenRouter
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_api_key():
    """Test if the API key is valid"""
    
    url = "https://openrouter.ai/api/v1/models"  # Simple endpoint to test auth
    
    api_key = os.environ.get('OPENROUTER_API_KEY')
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        print("🔍 Testing API key validity...")
        print(f"🔑 Using key: {api_key[:15]}...")
        
        response = requests.get(url, headers=headers, timeout=10)
        print(f"📡 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ API Key is valid!")
            # models = response.json()
            # print(f"📋 Available models: {len(models.get('data', []))} found")
            return True
        elif response.status_code == 401:
            print("❌ API Key is invalid or expired")
            print("💡 You may need to:")
            print("   1. Check if the key is correct")
            print("   2. Generate a new API key at https://openrouter.ai")
            print("   3. Verify your OpenRouter account has credits")
            return False
        else:
            print(f"⚠️  Unexpected status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False

def test_chat_endpoint():
    """Test the chat completions endpoint specifically"""
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    api_key = os.environ.get('OPENROUTER_API_KEY')
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "PoetryAI Test"
    }
    
    # Minimal test payload
    payload = {
        "model": "google/gemma-2-9b-it:free",
        "messages": [{"role": "user", "content": "Hello"}],
        "max_tokens": 10
    }
    
    try:
        print("\n🧪 Testing chat completions endpoint...")
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        print(f"📡 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Chat endpoint working!")
            if 'choices' in result:
                message = result['choices'][0]['message']['content']
                print(f"🤖 Test response: {message}")
            return True
        else:
            print(f"❌ Chat endpoint failed: {response.status_code}")
            try:
                error_info = response.json()
                print(f"Error details: {json.dumps(error_info, indent=2)}")
            except:
                print(f"Raw response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ No API key found!")
    else:
        print("🚀 Running API validation tests...\n")
        
        # Test 1: Basic API key validation
        key_valid = test_api_key()
        
        # Test 2: Chat completions endpoint (only if key is valid)
        if key_valid:
            test_chat_endpoint()
        else:
            print("\n⏭️  Skipping chat test due to invalid API key")
            print("\n🔧 Troubleshooting suggestions:")
            print("1. Visit https://openrouter.ai/keys")
            print("2. Generate a new API key")
            print("3. Update your .env file with the new key")
            print("4. Make sure your account has available credits")