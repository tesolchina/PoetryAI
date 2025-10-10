"""
Complete Poetry AI Comparison Test
Automatically runs both structured and exploratory conditions
"""

import requests
import json
import os
from dotenv import load_dotenv
import time

load_dotenv()

def test_condition(condition, user_message):
    """Test a specific condition"""
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000"
    }
    
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

    # Parameters based on condition
    temp, top_p = (0.3, 0.4) if condition == "structured" else (0.8, 0.9)
    
    payload = {
        "model": "google/gemma-2-9b-it:free",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": temp,
        "top_p": top_p,
        "max_tokens": 200
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        result = response.json()
        
        if 'choices' in result:
            return {
                "success": True,
                "message": result['choices'][0]['message']['content'],
                "tokens": result.get('usage', {}).get('completion_tokens', 0)
            }
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    """Run complete comparison"""
    
    tests = [
        "Help me write a haiku about rain",
        "I need a better word than 'nice'", 
        "I'm stuck on a friendship poem",
        "How do I count syllables?",
        "Poetry partner!"
    ]
    
    print("🎭 POETRY AI COMPARISON TEST")
    print("="*50)
    
    for i, test in enumerate(tests, 1):
        print(f"\n🔬 TEST {i}: '{test}'")
        print("-"*40)
        
        # Structured
        print(f"📊 STRUCTURED (0.3/0.4):")
        s_result = test_condition("structured", test)
        if s_result["success"]:
            print(f"🤖 {s_result['message'][:200]}...")
            print(f"📈 Tokens: {s_result['tokens']}")
        
        # Exploratory  
        print(f"\n📊 EXPLORATORY (0.8/0.9):")
        e_result = test_condition("exploratory", test)
        if e_result["success"]:
            print(f"🤖 {e_result['message'][:200]}...")
            print(f"📈 Tokens: {e_result['tokens']}")
        
        print("="*50)
        time.sleep(1)

if __name__ == "__main__":
    if not os.environ.get('OPENROUTER_API_KEY'):
        print("❌ API Key missing!")
        exit(1)
    
    print("🔑 API Key found ✅")
    main()