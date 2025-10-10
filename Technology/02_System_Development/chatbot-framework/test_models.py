"""
Test with different available models
"""

import asyncio
import aiohttp
import json

# Try different models that should be available
MODELS_TO_TRY = [
    "microsoft/phi-3-mini-128k-instruct:free",
    "google/gemma-2-9b-it:free", 
    "meta-llama/llama-3.1-8b-instruct",  # Paid version
    "openai/gpt-3.5-turbo",  # Paid but cheaper
]

async def test_model(api_key, model_name):
    """Test a specific model"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:3000",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": "Hello! Say 'Model test successful' if you can read this."}
        ],
        "temperature": 0.7,
        "max_tokens": 50
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    message = result['choices'][0]['message']['content']
                    return True, message
                else:
                    error_text = await response.text()
                    return False, f"Status {response.status}: {error_text}"
    except Exception as e:
        return False, f"Error: {str(e)}"

async def main():
    # Load API key from .env
    with open('.env', 'r') as f:
        content = f.read()
        for line in content.split('\n'):
            if line.startswith('OPENROUTER_API_KEY='):
                api_key = line.split('=', 1)[1].strip()
                break
    
    print("🧪 Testing Different Models")
    print("=" * 50)
    print(f"🔑 API Key: {api_key[:20]}...{api_key[-6:]}")
    print("=" * 50)
    
    for model in MODELS_TO_TRY:
        print(f"\n🤖 Testing: {model}")
        success, result = await test_model(api_key, model)
        
        if success:
            print(f"✅ SUCCESS! Model is working")
            print(f"🎯 Response: {result}")
            print(f"\n🎉 Great! You can use this model: {model}")
            return model
        else:
            print(f"❌ Failed: {result}")
    
    print(f"\n🔧 No models worked. This might mean:")
    print("1. You need to add credits to your OpenRouter account")
    print("2. Free tier models might be temporarily unavailable")
    print("3. Try visiting https://openrouter.ai/models to see available models")

if __name__ == "__main__":
    asyncio.run(main())