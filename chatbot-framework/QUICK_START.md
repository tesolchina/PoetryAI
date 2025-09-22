# 🚀 Quick Start Guide - Building Your First Chatbot with OpenRouter

## ✅ Your Setup Status
- ✅ API Key configured: `sk-or-v1-732...234`
- ✅ Framework files ready
- ⚠️ Need to install Python and dependencies

## 📋 Step-by-Step Instructions

### 1. Install Python (if not already installed)
1. Go to [python.org](https://python.org/downloads/)
2. Download Python 3.8 or higher
3. **Important**: Check "Add Python to PATH" during installation
4. Restart your terminal/PowerShell

### 2. Install Required Packages
Open PowerShell in this directory and run:
```bash
pip install aiohttp python-dotenv requests colorama rich pydantic
```

### 3. Test Your API Connection
```bash
python test_api.py
```

### 4. Run Your First Chatbot
```bash
python examples/basic_chatbot.py
```

## 🤖 Quick Examples to Try

### Example 1: Simple Chat (Copy & Save as `my_first_bot.py`)
```python
import asyncio
import aiohttp
import json

async def simple_chat():
    headers = {
        "Authorization": "Bearer sk-or-v1-732...234",
        "HTTP-Referer": "http://localhost:3000",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "user", "content": "Hello! Tell me a joke."}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        ) as response:
            result = await response.json()
            print("Bot:", result['choices'][0]['message']['content'])

# Run it
asyncio.run(simple_chat())
```

### Example 2: Interactive Chatbot (Copy & Save as `interactive_bot.py`)
```python
import asyncio
import aiohttp
import json

class SimpleChatbot:
    def __init__(self):
        self.api_key = "sk-or-v1-732...234"
        self.conversation = []
    
    async def chat(self, message):
        self.conversation.append({"role": "user", "content": message})
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http://localhost:3000",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "meta-llama/llama-3.1-8b-instruct:free",
            "messages": self.conversation,
            "temperature": 0.7,
            "max_tokens": 200
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data
            ) as response:
                result = await response.json()
                reply = result['choices'][0]['message']['content']
                
                self.conversation.append({"role": "assistant", "content": reply})
                return reply

async def main():
    bot = SimpleChatbot()
    print("Chatbot ready! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = await bot.chat(user_input)
        print(f"Bot: {response}")

asyncio.run(main())
```

## 🎭 Creating Specialized Chatbots

### Creative Writer Bot
```python
# Add this system message to make your bot creative
system_message = {
    "role": "system", 
    "content": "You are a creative writing assistant. Help with stories, poems, and creative ideas. Be imaginative and inspiring."
}
```

### Coding Assistant Bot
```python
# Add this system message for coding help
system_message = {
    "role": "system", 
    "content": "You are a programming assistant. Provide clear code examples, explain concepts, and help debug issues."
}
```

### Study Buddy Bot
```python
# Add this system message for learning support
system_message = {
    "role": "system", 
    "content": "You are a patient tutor. Explain concepts clearly, ask questions to check understanding, and encourage learning."
}
```

## 🔧 Troubleshooting

### If you get "pip not found":
```bash
python -m pip install aiohttp python-dotenv
```

### If you get "python not found":
- Install Python from python.org
- Make sure to check "Add to PATH"
- Restart your terminal

### If API returns errors:
- Check your API key is correct
- Verify you have credits in your OpenRouter account
- Make sure your internet connection works

## 🚀 Next Steps

1. **Test the API**: Run `python test_api.py`
2. **Try simple examples**: Copy the code above into new files
3. **Use the full framework**: Once Python is set up, use our advanced examples
4. **Customize**: Experiment with different models and personalities

## 📚 Available Models (Free Tier)
- `meta-llama/llama-3.1-8b-instruct:free` (recommended to start)
- `microsoft/phi-3-mini-128k-instruct:free`
- `google/gemma-2-9b-it:free`

## 💡 Tips for Success
- Start simple with the basic examples above
- Experiment with different `temperature` values (0.1 = focused, 0.9 = creative)
- Use system messages to define your bot's personality
- Keep conversations in the `conversation` array for context