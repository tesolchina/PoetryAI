"""
Automated Poetry AI Test - No Interactive Input Required
Tests both structured and exploratory conditions automatically
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_poetry_chatbot_auto(condition="structured", user_message="Help me write a haiku about rain"):
    """
    Test the poetry chatbot automatically with unified prompt system.
    """
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",
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
        "model": "google/gemma-2-9b-it:free",
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
        "max_tokens": 300,
        "stream": False
    }
    
    try:
        print(f"\n🧪 Testing {condition.upper()} condition")
        print(f"🎯 Temperature: {temperature}, Top-p: {top_p}")
        print(f"📝 User: '{user_message}'")
        print("⏳ Processing...")
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            assistant_message = result['choices'][0]['message']['content']
            print(f"\n🤖 Assistant Response:")
            print(f"{assistant_message}")
            
            # Token usage
            if 'usage' in result:
                usage = result['usage']
                print(f"\n📊 Tokens - Input: {usage.get('prompt_tokens')}, Output: {usage.get('completion_tokens')}, Total: {usage.get('total_tokens')}")
        
        return result
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return {"error": str(e)}

def run_comparison():
    """Run comparison between structured and exploratory conditions"""
    
    test_cases = [
        "Help me write a haiku about rain",
        "I need help counting syllables in 'beautiful'", 
        "Can you suggest a better word than 'nice' for my poem?",
        "I'm stuck writing about friendship. Give me ideas.",
        "Poetry partner"
    ]
    
    print("🎭 POETRY AI COMPARATIVE TESTING")
    print("=" * 60)
    print("Testing unified prompt system with parameter-only differentiation")
    print("=" * 60)
    
    for i, test_message in enumerate(test_cases, 1):
        print(f"\n🔬 TEST {i}: '{test_message}'")
        print("-" * 50)
        
        # Test structured condition
        test_poetry_chatbot_auto("structured", test_message)
        
        print("\n" + "🔄" * 25)
        
        # Test exploratory condition  
        test_poetry_chatbot_auto("exploratory", test_message)
        
        print("\n" + "="*60)

if __name__ == "__main__":
    # Check API key
    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found")
        exit(1)
    
    print("🔑 API Key loaded ✅")
    print("🚀 Running automated Poetry AI tests...\n")
    
    # Run quick single test first
    print("📋 SINGLE TEST DEMO:")
    test_poetry_chatbot_auto("structured", "Help me write a haiku about autumn leaves")
    
    print("\n" + "="*60)
    input("Press Enter to run full comparative test suite...")
    
    # Run full comparison
    run_comparison()