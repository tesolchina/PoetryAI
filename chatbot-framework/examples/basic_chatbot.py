"""
Basic usage example of the CustomChatbot framework
"""

import asyncio
import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.chatbot import CustomChatbot
from config.config import Config

async def main():
    print("=== Basic Chatbot Example ===\n")
    
    # Validate configuration
    try:
        Config.validate_config()
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set up your .env file with your OpenRouter API key.")
        return
    
    # Create a basic chatbot
    bot = CustomChatbot(
        name="BasicBot",
        system_prompt="You are a helpful assistant that provides clear, concise answers.",
        temperature=0.7
    )
    
    print(f"Chatbot '{bot.name}' is ready!")
    print("Type 'quit' to exit, 'clear' to clear history, or 'save' to save conversation\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'clear':
                bot.clear_history()
                print("Conversation history cleared!\n")
                continue
            elif user_input.lower() == 'save':
                filename = f"conversation_{bot.name}_{asyncio.get_event_loop().time()}.json"
                bot.save_conversation(filename)
                print(f"Conversation saved to {filename}\n")
                continue
            elif not user_input:
                continue
            
            print(f"\n{bot.name}: ", end="")
            
            # Get response with streaming
            response = await bot.chat(user_input, stream=True)
            print("\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())