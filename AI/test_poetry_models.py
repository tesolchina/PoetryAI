#!/usr/bin/env python3
"""
Test script to compare different AI models for poetry generation
"""

import requests
import json
from datetime import datetime

# API Configuration
OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Models to test (mix of free and low-cost)
MODELS_TO_TEST = [
    {
        "id": "google/gemini-2.0-flash-exp:free",
        "name": "Google Gemini 2.0 Flash (FREE)",
        "tier": "Free"
    },
    {
        "id": "meta-llama/llama-3.3-70b-instruct:free",
        "name": "Meta Llama 3.3 70B (FREE)",
        "tier": "Free"
    },
    {
        "id": "amazon/nova-2-lite-v1:free",
        "name": "Amazon Nova 2 Lite (FREE)",
        "tier": "Free"
    },
    {
        "id": "mistralai/mistral-small-3.1-24b-instruct:free",
        "name": "Mistral Small 3.1 24B (FREE)",
        "tier": "Free"
    },
    {
        "id": "qwen/qwen3-235b-a22b:free",
        "name": "Qwen3 235B (FREE)",
        "tier": "Free"
    }
]

# Test prompt for poetry generation
POETRY_PROMPT = """Write a short haiku about the changing seasons and the passage of time. 
The poem should evoke feelings of nostalgia and reflection."""

def test_model(model_id, model_name):
    """Test a single model with the poetry prompt"""
    print(f"\n{'='*80}")
    print(f"Testing: {model_name}")
    print(f"Model ID: {model_id}")
    print(f"{'='*80}")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Poetry Testing Script"
    }
    
    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "user",
                "content": POETRY_PROMPT
            }
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        print("Sending request...")
        start_time = datetime.now()
        
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=30)
        
        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract the response
            if 'choices' in data and len(data['choices']) > 0:
                poem = data['choices'][0]['message']['content']
                
                print(f"\n✅ SUCCESS (Response time: {response_time:.2f}s)")
                print(f"\n{'-'*80}")
                print("GENERATED POEM:")
                print(f"{'-'*80}")
                print(poem)
                print(f"{'-'*80}")
                
                # Show usage statistics if available
                if 'usage' in data:
                    usage = data['usage']
                    print(f"\nUsage Statistics:")
                    print(f"  Prompt tokens: {usage.get('prompt_tokens', 'N/A')}")
                    print(f"  Completion tokens: {usage.get('completion_tokens', 'N/A')}")
                    print(f"  Total tokens: {usage.get('total_tokens', 'N/A')}")
                
                return {
                    'success': True,
                    'model': model_name,
                    'model_id': model_id,
                    'poem': poem,
                    'response_time': response_time,
                    'usage': data.get('usage', {})
                }
            else:
                print(f"\n❌ ERROR: Unexpected response format")
                print(json.dumps(data, indent=2))
                return {'success': False, 'model': model_name, 'error': 'Unexpected format'}
                
        else:
            print(f"\n❌ ERROR: Status code {response.status_code}")
            print(response.text)
            return {'success': False, 'model': model_name, 'error': f"Status {response.status_code}"}
            
    except requests.exceptions.Timeout:
        print(f"\n❌ ERROR: Request timeout (>30s)")
        return {'success': False, 'model': model_name, 'error': 'Timeout'}
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        return {'success': False, 'model': model_name, 'error': str(e)}

def save_results(results, filename):
    """Save test results to a JSON file"""
    output = {
        'test_date': datetime.now().isoformat(),
        'prompt': POETRY_PROMPT,
        'results': results
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n\nResults saved to: {filename}")

def print_summary(results):
    """Print a summary of all results"""
    print("\n\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    print(f"\nTotal models tested: {len(results)}")
    print(f"Successful: {len(successful)}")
    print(f"Failed: {len(failed)}")
    
    if successful:
        print("\n" + "-"*80)
        print("SUCCESSFUL MODELS:")
        print("-"*80)
        for r in successful:
            print(f"\n✅ {r['model']}")
            print(f"   Response time: {r['response_time']:.2f}s")
            if 'usage' in r and 'total_tokens' in r['usage']:
                print(f"   Total tokens: {r['usage']['total_tokens']}")
    
    if failed:
        print("\n" + "-"*80)
        print("FAILED MODELS:")
        print("-"*80)
        for r in failed:
            print(f"\n❌ {r['model']}")
            print(f"   Error: {r.get('error', 'Unknown error')}")

def main():
    print("="*80)
    print("POETRY AI MODEL TESTING SCRIPT")
    print("="*80)
    print(f"\nTest Prompt: {POETRY_PROMPT}")
    print(f"\nTesting {len(MODELS_TO_TEST)} models...")
    print("="*80)
    
    results = []
    
    for i, model in enumerate(MODELS_TO_TEST, 1):
        print(f"\n\n[{i}/{len(MODELS_TO_TEST)}]")
        result = test_model(model['id'], model['name'])
        results.append(result)
        
        # Small delay between requests
        if i < len(MODELS_TO_TEST):
            print("\n(Waiting 2 seconds before next request...)")
            import time
            time.sleep(2)
    
    # Print summary
    print_summary(results)
    
    # Save results
    output_file = "/Users/simonwang/Documents/Usage/AIpoetry/AI/poetry_test_results.json"
    save_results(results, output_file)
    
    print("\n" + "="*80)
    print("TESTING COMPLETE!")
    print("="*80)

if __name__ == "__main__":
    main()

