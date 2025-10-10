"""
Example showing how to create chatbots with different personalities
"""

import asyncio
import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.chatbot import (
    create_creative_writer_bot, 
    create_coding_assistant_bot, 
    create_friendly_companion_bot
)

async def test_personality_bot(bot, test_message, bot_description):
    print(f"\n=== {bot_description} ===")
    print(f"Test message: '{test_message}'")
    print(f"\n{bot.name}: ", end="")
    
    response = await bot.chat(test_message, stream=True)
    print("\n" + "="*50)

async def main():
    print("=== Personality Chatbots Demo ===")
    print("Testing different specialized chatbots with the same message...\n")
    
    # Create different personality bots
    writer_bot = create_creative_writer_bot("Maya")
    coder_bot = create_coding_assistant_bot("Alex")
    friend_bot = create_friendly_companion_bot("Sam")
    
    test_message = "I'm feeling stuck and don't know what to do next."
    
    # Test each bot with the same message to see personality differences
    await test_personality_bot(writer_bot, test_message, "Creative Writer Bot")
    await test_personality_bot(coder_bot, test_message, "Coding Assistant Bot")
    await test_personality_bot(friend_bot, test_message, "Friendly Companion Bot")
    
    print("\nNotice how each bot responds differently based on their personality!")
    
    # Interactive session with one bot
    print("\n" + "="*60)
    print("Interactive session with the Friendly Companion Bot")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                break
            elif not user_input:
                continue
            
            print(f"\n{friend_bot.name}: ", end="")
            response = await friend_bot.chat(user_input, stream=True)
            print("\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    asyncio.run(main())