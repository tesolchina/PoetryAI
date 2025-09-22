"""
Quick test to verify your OpenRouter API key works
Run this script first to test your setup before building complex chatbots
"""

import asyncio
import aiohttp
import json

# Your API key
API_KEY = "sk-or-v1-732...234"
BASE_URL = "https://openrouter.ai/api/v1"

async def test_openrouter_api():
    """Test if your OpenRouter API key works"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
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
            async with session.post(
                f"{BASE_URL}/chat/completions",
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
                    return False
                    
    except Exception as e:
        print(f"❌ ERROR: Failed to connect to OpenRouter API")
        print(f"Details: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing OpenRouter API connection...")
    print("-" * 50)
    
    # Run the test
    result = asyncio.run(test_openrouter_api())
    
    if result:
        print("\n🎉 Great! Your API key is working. You're ready to build chatbots!")
        print("\nNext steps:")
        print("1. Install Python dependencies: pip install aiohttp python-dotenv")
        print("2. Run the basic chatbot example")
        print("3. Start customizing your own chatbots")
    else:
        print("\n🔧 Please check:")
        print("1. Your API key is correct")
        print("2. You have sufficient credits in your OpenRouter account")
        print("3. Your internet connection is working")