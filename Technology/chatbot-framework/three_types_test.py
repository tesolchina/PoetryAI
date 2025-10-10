"""
Three Types of Interactions Test
Tests Type A (Constraint repair), Type B (Content enhancement), and Type C (Surprise harvest)
in both structured and exploratory conditions to analyze behavioral differences.
"""

import requests
import json
import os
from dotenv import load_dotenv
import time

load_dotenv()

def test_interaction_type(condition, user_message, interaction_type):
    """Test a specific interaction type in a given condition"""
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "PoetryAI Three Types Research"
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
    else:  # exploratory
        temperature = 0.8
        top_p = 0.9
    
    payload = {
        "model": "google/gemma-2-9b-it:free",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": 300,
        "stream": False
    }
    
    try:
        print(f"    🎯 {condition.upper()} (temp={temperature}, top_p={top_p})")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if 'choices' in result and result['choices']:
            message = result['choices'][0]['message']['content']
            tokens = result.get('usage', {}).get('completion_tokens', 0)
            
            print(f"    🤖 Response: {message}")
            print(f"    📊 Tokens: {tokens}")
            
            return {
                "success": True,
                "condition": condition,
                "interaction_type": interaction_type,
                "message": message,
                "tokens": tokens,
                "temperature": temperature,
                "top_p": top_p
            }
    except Exception as e:
        print(f"    ❌ Error: {e}")
        return {"success": False, "error": str(e)}

def run_three_types_test():
    """Run comprehensive test of all three interaction types"""
    
    # Test cases designed to trigger specific interaction types
    test_cases = {
        "Type A - Constraint Repair": [
            "My haiku has too many syllables in the first line: 'The beautiful autumn leaves are falling down'",
            "I wrote 'The cats runs quickly' but something seems wrong with the grammar",
            "Is this haiku correct? 'Rain falls / On the ground today / Very wet and nice'",
            "I tried to write a sonnet but I only have 12 lines. What should I do?"
        ],
        
        "Type B - Content Enhancement": [
            "I used the word 'nice' in my poem but it feels too simple. What's a better word?",
            "My poem about sunset says 'The sky is pretty.' How can I make it more vivid?",
            "I want to describe a flower but 'beautiful' is too boring. Help me find better words.",
            "My line 'The dog walked slowly' needs more interesting language. Any suggestions?"
        ],
        
        "Type C - Surprise Harvest": [
            "I'm writing about rain but I'm stuck. Can you help me think of unexpected connections?",
            "My poem is about friendship but feels predictable. What surprising angles could I explore?",
            "I want to write about time but avoid clichés. What unexpected metaphors could work?",
            "Help me find a creative way to connect the moon with childhood memories in my poem."
        ]
    }
    
    print("🔬 THREE TYPES OF INTERACTIONS RESEARCH TEST")
    print("=" * 70)
    print("Testing Type A (Constraint Repair), Type B (Content Enhancement), Type C (Surprise Harvest)")
    print("Comparing Structured vs Exploratory parameter effects on each interaction type")
    print("=" * 70)
    
    results = {}
    
    for interaction_type, messages in test_cases.items():
        print(f"\n🎭 {interaction_type.upper()}")
        print("=" * 50)
        
        results[interaction_type] = {}
        
        for i, message in enumerate(messages, 1):
            print(f"\n📝 Test {i}: '{message[:60]}...' " if len(message) > 60 else f"\n📝 Test {i}: '{message}'")
            print("-" * 40)
            
            # Test both conditions
            for condition in ["structured", "exploratory"]:
                result = test_interaction_type(condition, message, interaction_type)
                if result["success"]:
                    key = f"{condition}_{i}"
                    results[interaction_type][key] = result
                
                print()  # Spacing between conditions
            
            print("-" * 40)
            time.sleep(0.5)  # Brief pause between tests
    
    # Analysis summary
    print("\n🎯 ANALYSIS SUMMARY")
    print("=" * 50)
    
    for interaction_type in test_cases.keys():
        print(f"\n📊 {interaction_type}:")
        
        structured_responses = [r for k, r in results[interaction_type].items() if k.startswith("structured")]
        exploratory_responses = [r for k, r in results[interaction_type].items() if k.startswith("exploratory")]
        
        if structured_responses:
            avg_tokens_structured = sum(r['tokens'] for r in structured_responses) / len(structured_responses)
            print(f"   STRUCTURED avg tokens: {avg_tokens_structured:.1f}")
            
        if exploratory_responses:
            avg_tokens_exploratory = sum(r['tokens'] for r in exploratory_responses) / len(exploratory_responses)
            print(f"   EXPLORATORY avg tokens: {avg_tokens_exploratory:.1f}")
    
    print(f"\n📋 KEY RESEARCH QUESTIONS ADDRESSED:")
    print("   • How do parameters affect constraint repair (Type A) responses?")
    print("   • Do exploratory settings enhance creative word suggestions (Type B)?")
    print("   • Does temperature impact unexpected connection generation (Type C)?")
    print("   • Are educational goals maintained across all interaction types?")
    
    return results

if __name__ == "__main__":
    # Verify API key
    if not os.environ.get('OPENROUTER_API_KEY'):
        print("❌ API Key not found!")
        exit(1)
    
    print("🔑 API Key loaded ✅")
    print("🚀 Starting Three Types Interaction Analysis...\n")
    
    results = run_three_types_test()
    
    print(f"\n✅ Test Complete! Analyzed {sum(len(v) for v in results.values())} total responses")
    print("📊 Results show parameter effects on each interaction type")