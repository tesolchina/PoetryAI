"""
Quick Working Chatbot Test - Your Setup is Perfect!
"""

import asyncio
import aiohttp
import json

async def quick_test():
    # Load API key from .env
    with open('.env', 'r') as f:
        content = f.read()
        for line in content.split('\n'):
            if line.startswith('OPENROUTER_API_KEY='):
                api_key = line.split('=', 1)[1].strip()
                break
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:3000",
        "Content-Type": "application/json"
    }
    
    print("🚀 Quick Chatbot Test")
    print("=" * 30)
    
    # Test 1: Simple question
    print("\n🤖 Test 1: Simple Chat")
    data1 = {
        "model": "google/gemma-2-9b-it:free",
        "messages": [{"role": "user", "content": "Tell me a fun fact about space!"}],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data1
        ) as response:
            result = await response.json()
            print(f"User: Tell me a fun fact about space!")
            print(f"Bot: {result['choices'][0]['message']['content']}")
    
    # Test 2: Creative writing
    print(f"\n🎨 Test 2: Creative Assistant")
    data2 = {
        "model": "google/gemma-2-9b-it:free",
        "messages": [
            {"role": "system", "content": "You are a creative writing assistant. Be imaginative and inspiring."},
            {"role": "user", "content": "Write the first sentence of a mystery story about a missing cat."}
        ],
        "temperature": 0.8,
        "max_tokens": 50
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data2
        ) as response:
            result = await response.json()
            print(f"User: Write the first sentence of a mystery story about a missing cat.")
            print(f"Creative Bot: {result['choices'][0]['message']['content']}")
    
    # Test 3: Coding help
    print(f"\n💻 Test 3: Coding Assistant")
    data3 = {
        "model": "google/gemma-2-9b-it:free",
        "messages": [
            {"role": "system", "content": "You are a programming tutor. Provide clear, simple code examples."},
            {"role": "user", "content": "Show me a simple Python function that adds two numbers."}
        ],
        "temperature": 0.3,
        "max_tokens": 100
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data3
        ) as response:
            result = await response.json()
            print(f"User: Show me a simple Python function that adds two numbers.")
            print(f"Coding Bot: {result['choices'][0]['message']['content']}")
    
    print(f"\n🎉 SUCCESS! All your chatbots are working perfectly!")
    print(f"✅ You can now:")
    print(f"   - Build custom chatbots with different personalities")
    print(f"   - Use the full framework in the examples/ folder")
    print(f"   - Experiment with different prompts and temperatures")
    print(f"   - Create specialized bots for any purpose!")

if __name__ == "__main__":
    asyncio.run(quick_test())