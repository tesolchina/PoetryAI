"""
Advanced example showing custom chatbot creation and dynamic personality updates
"""

import asyncio
import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.chatbot import CustomChatbot
from config.config import AVAILABLE_MODELS

async def create_poetry_tutor():
    """Create a specialized poetry tutoring chatbot"""
    return CustomChatbot(
        name="PoetryMentor",
        system_prompt="You are an expert poetry tutor and literary analyst. You help students understand poetry, create their own poems, and appreciate literary devices.",
        personality_traits={
            "scholarly": True,
            "patient": True,
            "encouraging": True,
            "creative": True,
            "analytical": True,
            "expertise_level": "PhD in Literature"
        },
        custom_instructions=[
            "Always explain poetic devices when you use them",
            "Provide examples from famous poets when relevant",
            "Encourage creative expression while teaching technique",
            "Break down complex concepts into understandable parts",
            "Ask students about their preferences and interests"
        ],
        temperature=0.8,
        model="meta-llama/llama-3.1-8b-instruct:free"  # Free model for poetry
    )

async def create_business_advisor():
    """Create a business strategy advisor chatbot"""
    return CustomChatbot(
        name="BizAdvisor",
        system_prompt="You are a senior business strategy consultant with expertise in startups, market analysis, and business planning.",
        personality_traits={
            "analytical": True,
            "strategic": True,
            "experienced": True,
            "practical": True,
            "communication_style": "direct but supportive"
        },
        custom_instructions=[
            "Always ask clarifying questions about business context",
            "Provide actionable, specific advice",
            "Consider both risks and opportunities",
            "Reference real-world business examples when helpful",
            "Focus on practical implementation"
        ],
        temperature=0.4,  # Lower temperature for more focused business advice
        model="meta-llama/llama-3.1-8b-instruct:free"
    )

async def demonstrate_dynamic_personality():
    """Show how to dynamically update chatbot personality"""
    print("=== Dynamic Personality Update Demo ===\n")
    
    # Start with a neutral bot
    bot = CustomChatbot(
        name="AdaptiveBot",
        system_prompt="You are a helpful assistant.",
        temperature=0.7
    )
    
    print("1. Starting with neutral personality...")
    response1 = await bot.chat("Tell me about artificial intelligence.")
    print(f"Response: {response1[:100]}...\n")
    
    # Update to be more technical
    print("2. Updating to technical expert personality...")
    bot.update_personality({
        "technical": True,
        "detailed": True,
        "academic": True,
        "expertise_level": "PhD in Computer Science"
    })
    bot.add_custom_instruction("Provide technical details and cite relevant research when possible")
    
    response2 = await bot.chat("Tell me about artificial intelligence.")
    print(f"Response: {response2[:100]}...\n")
    
    # Update to be more casual and friendly
    print("3. Updating to casual, friendly personality...")
    bot.update_personality({
        "casual": True,
        "friendly": True,
        "humorous": True,
        "accessible": True
    })
    bot.custom_instructions = ["Keep explanations simple and fun", "Use analogies and examples from everyday life"]
    bot._setup_system_message()  # Refresh system message
    
    response3 = await bot.chat("Tell me about artificial intelligence.")
    print(f"Response: {response3[:100]}...\n")

async def main():
    print("=== Advanced Custom Chatbots Demo ===\n")
    
    # Create specialized chatbots
    poetry_bot = await create_poetry_tutor()
    business_bot = await create_business_advisor()
    
    print("Created specialized chatbots:")
    print(f"1. {poetry_bot.name} - Poetry tutor and literary expert")
    print(f"2. {business_bot.name} - Business strategy advisor")
    print()
    
    # Test poetry bot
    print("=== Testing Poetry Tutor ===")
    poetry_response = await poetry_bot.chat("I want to write a poem about autumn. Can you help me get started?")
    print(f"{poetry_bot.name}: {poetry_response}\n")
    
    # Test business bot
    print("=== Testing Business Advisor ===")
    business_response = await business_bot.chat("I'm thinking of starting a food delivery app. What should I consider?")
    print(f"{business_bot.name}: {business_response}\n")
    
    # Demonstrate dynamic personality updates
    await demonstrate_dynamic_personality()
    
    # Show available models
    print("=== Available Models ===")
    print("Free models:", AVAILABLE_MODELS['free'])
    print("Paid models (first 3):", AVAILABLE_MODELS['paid'][:3])
    print("\nYou can change models using bot.set_model('model_name')")

if __name__ == "__main__":
    asyncio.run(main())