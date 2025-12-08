"""
API Test using .env file configuration
This will read your API key from the .env file automatically
"""

import asyncio
import aiohttp
import json
import os

# Try to load from .env file
def load_api_key():
    try:
        with open('.env', 'r') as f:
            content = f.read()
            for line in content.split('\n'):
                if line.startswith('OPENROUTER_API_KEY='):
                    return line.split('=', 1)[1].strip()
        return None
    except FileNotFoundError:
        return None

async def test_openrouter_api():
    """Test if your OpenRouter API key works"""
    
    # Load API key from .env file
    api_key = load_api_key()
    
    if not api_key or api_key == "your_openrouter_api_key_here":
        print("❌ ERROR: API key not found or not set properly")
        print("Please check your .env file and make sure OPENROUTER_API_KEY is set to your actual key")
        return False
    
    print(f"🔑 Using API key: {api_key[:20]}...{api_key[-4:]}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:3000",
        "Content-Type": "application/json"
    }
    
    # Simple test message
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "user", "content": "Hello! Please respond with 'API test successful' if you can read this."}
        ],
        "temperature": 0.7,
        "max_tokens": 50
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            print("🌐 Connecting to OpenRouter API...")
            async with session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    message = result['choices'][0]['message']['content']
                    print("✅ SUCCESS! OpenRouter API is working!")
                    print(f"🤖 Response: {message}")
                    return True
                else:
                    error_text = await response.text()
                    print(f"❌ ERROR: API request failed with status {response.status}")
                    print(f"Details: {error_text}")
                    
                    # Provide specific troubleshooting for common errors
                    if response.status == 401:
                        print("\n🔧 401 Error usually means:")
                        print("  - API key is incorrect or malformed")
                        print("  - API key doesn't have proper permissions")
                        print("  - Please check your API key in .env file")
                    elif response.status == 402:
                        print("\n🔧 402 Error means:")
                        print("  - Insufficient credits in your OpenRouter account")
                        print("  - Please add credits to your account")
                    elif response.status == 429:
                        print("\n🔧 429 Error means:")
                        print("  - Rate limit exceeded")
                        print("  - Please wait a moment and try again")
                    
                    return False
                    
    except Exception as e:
        print(f"❌ ERROR: Failed to connect to OpenRouter API")
        print(f"Details: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing OpenRouter API connection...")
    print("=" * 50)
    
    # Run the test
    result = asyncio.run(test_openrouter_api())
    
    if result:
        print("\n🎉 Great! Your API key is working. You're ready to build chatbots!")
        print("\nNext steps:")
        print("1. Try running: py simple_chatbot_demo.py")
        print("2. Experiment with different prompts and personalities")
        print("3. Start building your own custom chatbots!")
    else:
        print("\n🔧 Troubleshooting steps:")
        print("1. Double-check your API key in the .env file")
        print("2. Make sure you have credits in your OpenRouter account")
        print("3. Verify your internet connection")
        print("4. Try creating a new API key if the current one doesn't work")