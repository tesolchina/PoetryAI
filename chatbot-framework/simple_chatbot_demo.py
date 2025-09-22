"""
Minimal Working Chatbot Example
This is the simplest possible chatbot using your OpenRouter API key
"""

import asyncio
import json

# Try importing aiohttp, provide helpful error if not installed
try:
    import aiohttp
except ImportError:
    print("❌ Error: aiohttp not installed")
    print("Please run: pip install aiohttp")
    print("Then try running this script again")
    exit(1)

class MinimalChatbot:
    def __init__(self):
        # Load API key from .env file
        with open('.env', 'r') as f:
            content = f.read()
            for line in content.split('\n'):
                if line.startswith('OPENROUTER_API_KEY='):
                    self.api_key = line.split('=', 1)[1].strip()
                    break
        self.base_url = "https://openrouter.ai/api/v1"
        self.conversation_history = []
    
    async def send_message(self, user_message, system_prompt=None):
        """Send a message and get a response"""
        
        # Build conversation
        messages = []
        
        # Add system prompt if provided
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        # Add conversation history
        messages.extend(self.conversation_history)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        # API request setup
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "http://localhost:3000",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "google/gemma-2-9b-it:free",  # Working model
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 300
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data
                ) as response:
                    
                    if response.status == 200:
                        result = await response.json()
                        bot_response = result['choices'][0]['message']['content']
                        
                        # Save to conversation history
                        self.conversation_history.append({"role": "user", "content": user_message})
                        self.conversation_history.append({"role": "assistant", "content": bot_response})
                        
                        return bot_response
                    else:
                        error_text = await response.text()
                        return f"❌ API Error ({response.status}): {error_text}"
                        
        except Exception as e:
            return f"❌ Connection Error: {str(e)}"
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

async def demo_basic_chat():
    """Demo 1: Basic question and answer"""
    print("🤖 Demo 1: Basic Chat")
    print("-" * 30)
    
    bot = MinimalChatbot()
    
    response = await bot.send_message("Hello! What's your name?")
    print(f"User: Hello! What's your name?")
    print(f"Bot: {response}")
    print()

async def demo_creative_writer():
    """Demo 2: Creative writing assistant"""
    print("🎨 Demo 2: Creative Writing Assistant")
    print("-" * 40)
    
    bot = MinimalChatbot()
    
    system_prompt = "You are a creative writing assistant. Help users with stories, poems, and creative ideas. Be imaginative and inspiring."
    
    response = await bot.send_message(
        "Help me write the opening line for a mystery novel set in a small town.",
        system_prompt=system_prompt
    )
    
    print(f"User: Help me write the opening line for a mystery novel set in a small town.")
    print(f"Creative Writer Bot: {response}")
    print()

async def demo_coding_helper():
    """Demo 3: Coding assistant"""
    print("💻 Demo 3: Coding Assistant")
    print("-" * 30)
    
    bot = MinimalChatbot()
    
    system_prompt = "You are a programming assistant. Provide clear, working code examples and explain concepts simply."
    
    response = await bot.send_message(
        "Show me how to create a simple function in Python that adds two numbers.",
        system_prompt=system_prompt
    )
    
    print(f"User: Show me how to create a simple function in Python that adds two numbers.")
    print(f"Coding Bot: {response}")
    print()

async def demo_interactive_chat():
    """Demo 4: Interactive conversation"""
    print("💬 Demo 4: Interactive Chat")
    print("-" * 30)
    print("Type your messages (type 'quit' to exit, 'clear' to clear history)")
    print()
    
    bot = MinimalChatbot()
    
    # Optional: Set a personality
    system_prompt = "You are a friendly, helpful assistant with a good sense of humor."
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye! 👋")
            break
        elif user_input.lower() == 'clear':
            bot.clear_history()
            print("🗑️ Conversation history cleared!")
            continue
        elif not user_input:
            continue
        
        print("Bot: ", end="", flush=True)
        response = await bot.send_message(user_input, system_prompt=system_prompt)
        print(response)
        print()

async def main():
    """Main function - run all demos"""
    print("🚀 OpenRouter Chatbot Demo")
    print("=" * 50)
    print(f"API Key: {MinimalChatbot().api_key[:20]}...")
    print("=" * 50)
    print()
    
    # Run demos
    await demo_basic_chat()
    await demo_creative_writer()
    await demo_coding_helper()
    
    # Interactive chat
    await demo_interactive_chat()

if __name__ == "__main__":
    print("Starting chatbot demos...")
    print("Make sure you have 'aiohttp' installed: pip install aiohttp")
    print()
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Demo stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure Python is installed")
        print("2. Install required package: pip install aiohttp")
        print("3. Check your internet connection")
        print("4. Verify your OpenRouter API key has credits")