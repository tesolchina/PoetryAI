"""
Poetry AI Chatbot Request Builder Test
Based on the unified prompt engineering design from the research framework.
Tests both structured and exploratory conditions with identical system prompts.
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_poetry_chatbot(condition="structured", user_message="Poetry partner"):
    """
    Test the poetry chatbot with unified prompt system.
    
    Args:
        condition (str): "structured" (temp=0.3, top_p=0.4) or "exploratory" (temp=0.8, top_p=0.9)
        user_message (str): The user's input message
    
    Returns:
        dict: API response or error information
    """
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",  # For better rate limits
        "X-Title": "PoetryAI Research Project"
    }
    
    # Unified system prompt (identical for both conditions)
    system_prompt = """You are a helpful creative writing assistant for English language learners working on poetry. Your role is to support students in exploring creative expression through collaborative writing.

EDUCATIONAL APPROACH:
- Help students with poetry structure, word choice, and creative development
- Provide encouraging, supportive guidance appropriate for L2 English learners
- Offer specific suggestions when students need help with rules or improvements
- Celebrate creativity while maintaining educational value

INTERACTION CAPABILITIES:
You can assist with three types of support:
- Type A: Constraint repair (helping with poetry rules, structure, grammar issues)
- Type B: Content enhancement (improving word choice, imagery, expression)  
- Type C: Surprise harvest (introducing creative connections and unexpected possibilities)

TONE: Encouraging, supportive, educational, and appropriate for collaborative creative writing with L2 learners.

Always respond helpfully to student requests while maintaining an engaging, positive atmosphere for creative exploration."""

    # Parameter settings based on condition
    if condition == "structured":
        temperature = 0.3
        top_p = 0.4
    elif condition == "exploratory":
        temperature = 0.8
        top_p = 0.9
    else:
        raise ValueError("Condition must be 'structured' or 'exploratory'")
    
    payload = {
        "model": "google/gemma-2-9b-it:free",  # Using working model from config
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": 2048,
        "stream": False  # Set to True if you want streaming responses
    }
    
    try:
        print(f"\n🧪 Testing {condition.upper()} condition (temp={temperature}, top_p={top_p})")
        print(f"📝 User message: '{user_message}'")
        print("⏳ Sending request...")
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # Raise exception for bad status codes
        
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            assistant_message = result['choices'][0]['message']['content']
            print(f"\n✅ Response received:")
            print(f"🤖 Assistant: {assistant_message}")
            
            # Token usage info if available
            if 'usage' in result:
                print(f"\n📊 Token Usage:")
                print(f"   Input: {result['usage'].get('prompt_tokens', 'N/A')}")
                print(f"   Output: {result['usage'].get('completion_tokens', 'N/A')}")
                print(f"   Total: {result['usage'].get('total_tokens', 'N/A')}")
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request Error: {e}")
        return {"error": str(e)}
    except json.JSONDecodeError as e:
        print(f"\n❌ JSON Decode Error: {e}")
        return {"error": f"JSON decode error: {e}"}
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        return {"error": f"Unexpected error: {e}"}

def run_comparative_test():
    """Run tests for both structured and exploratory conditions with the same input."""
    
    test_messages = [
        "Poetry partner",
        "Help me write a haiku about rain",
        "I need help counting syllables",
        "I need a better word than 'nice'",
        "I'm stuck and need ideas for a poem about friendship"
    ]
    
    print("🎭 POETRY AI COMPARATIVE TESTING")
    print("=" * 50)
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🔬 TEST {i}: Comparing conditions with same input")
        print("-" * 40)
        
        # Test structured condition
        structured_result = test_poetry_chatbot("structured", message)
        
        print("\n" + "="*20)
        
        # Test exploratory condition  
        exploratory_result = test_poetry_chatbot("exploratory", message)
        
        print("\n" + "="*50)
        
        # Brief pause between tests
        import time
        time.sleep(1)

if __name__ == "__main__":
    # Check if API key is available
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found in environment variables")
        print("💡 Make sure your .env file is properly configured")
        exit(1)
    
    print("🔑 API Key found ✅")
    
    # Run a single test or comparative test
    choice = input("\nChoose test type:\n1. Single test\n2. Comparative test (both conditions)\nEnter 1 or 2: ")
    
    if choice == "1":
        condition = input("Enter condition (structured/exploratory): ").lower()
        if condition in ["structured", "exploratory"]:
            message = input("Enter your message: ")
            test_poetry_chatbot(condition, message)
        else:
            print("❌ Invalid condition. Use 'structured' or 'exploratory'")
    elif choice == "2":
        run_comparative_test()
    else:
        print("❌ Invalid choice")