#!/usr/bin/env python3
"""
Script to query OpenRouter and Poe APIs for available models
and their specifications (context window, costs, etc.)
"""

import requests
import json
import csv
from typing import List, Dict

# API Keys
OPENROUTER_API_KEY = "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"
POE_API_KEY = "QF6ucv7Te3nWofhGsoOzzBDR-CzMLf9LsIDOJ6-GqgU"

def get_openrouter_models() -> List[Dict]:
    """Fetch available models from OpenRouter API"""
    print("Fetching OpenRouter models...")
    
    url = "https://openrouter.ai/api/v1/models"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Model Testing Script"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        models = []
        for model in data.get('data', []):
            model_info = {
                'provider': 'OpenRouter',
                'model_id': model.get('id', 'N/A'),
                'name': model.get('name', 'N/A'),
                'context_length': model.get('context_length', 'N/A'),
                'prompt_cost': model.get('pricing', {}).get('prompt', 'N/A'),
                'completion_cost': model.get('pricing', {}).get('completion', 'N/A'),
                'created': model.get('created', 'N/A'),
                'description': model.get('description', '')[:100] if model.get('description') else 'N/A'
            }
            models.append(model_info)
        
        print(f"Found {len(models)} OpenRouter models")
        return models
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching OpenRouter models: {e}")
        return []

def get_poe_models() -> List[Dict]:
    """Fetch available models from Poe API"""
    print("Fetching Poe models...")
    
    # Poe API endpoint for bots/models
    url = "https://api.poe.com/bot/get_settings"
    headers = {
        "Authorization": f"Bearer {POE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # If this endpoint doesn't work, we'll document known Poe models manually
        if response.status_code == 404 or response.status_code == 401:
            print("Poe API endpoint not accessible. Using known Poe models list...")
            # Known Poe models as of 2024
            known_poe_models = [
                {'provider': 'Poe', 'model_id': 'GPT-4', 'name': 'GPT-4', 'context_length': '8192', 'prompt_cost': 'Subscription', 'completion_cost': 'Subscription', 'created': 'N/A', 'description': 'OpenAI GPT-4 via Poe'},
                {'provider': 'Poe', 'model_id': 'GPT-3.5-Turbo', 'name': 'GPT-3.5-Turbo', 'context_length': '4096', 'prompt_cost': 'Subscription', 'completion_cost': 'Subscription', 'created': 'N/A', 'description': 'OpenAI GPT-3.5-Turbo via Poe'},
                {'provider': 'Poe', 'model_id': 'Claude-3-Opus', 'name': 'Claude-3-Opus', 'context_length': '200000', 'prompt_cost': 'Subscription', 'completion_cost': 'Subscription', 'created': 'N/A', 'description': 'Anthropic Claude 3 Opus via Poe'},
                {'provider': 'Poe', 'model_id': 'Claude-3-Sonnet', 'name': 'Claude-3-Sonnet', 'context_length': '200000', 'prompt_cost': 'Subscription', 'completion_cost': 'Subscription', 'created': 'N/A', 'description': 'Anthropic Claude 3 Sonnet via Poe'},
                {'provider': 'Poe', 'model_id': 'Claude-instant', 'name': 'Claude-Instant', 'context_length': '100000', 'prompt_cost': 'Subscription', 'completion_cost': 'Subscription', 'created': 'N/A', 'description': 'Anthropic Claude Instant via Poe'},
                {'provider': 'Poe', 'model_id': 'Google-PaLM', 'name': 'Google-PaLM', 'context_length': '8000', 'prompt_cost': 'Subscription', 'completion_cost': 'Subscription', 'created': 'N/A', 'description': 'Google PaLM via Poe'},
            ]
            return known_poe_models
        
        response.raise_for_status()
        data = response.json()
        
        # Parse Poe response (structure may vary)
        models = []
        # Add parsing logic based on actual Poe API response structure
        
        return models
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Poe models: {e}")
        print("Using known Poe models list instead...")
        return []

def save_to_csv(models: List[Dict], filename: str):
    """Save models list to CSV file"""
    print(f"\nSaving results to {filename}...")
    
    if not models:
        print("No models to save!")
        return
    
    # Define CSV columns
    fieldnames = ['provider', 'model_id', 'name', 'context_length', 
                  'prompt_cost', 'completion_cost', 'created', 'description']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(models)
    
    print(f"Successfully saved {len(models)} models to {filename}")

def main():
    print("="*60)
    print("API Model Testing Script")
    print("="*60)
    
    # Fetch models from both APIs
    openrouter_models = get_openrouter_models()
    poe_models = get_poe_models()
    
    # Combine all models
    all_models = openrouter_models + poe_models
    
    # Save to CSV
    output_file = "/Users/simonwang/Documents/Usage/AIpoetry/AI/available_models.csv"
    save_to_csv(all_models, output_file)
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"OpenRouter models: {len(openrouter_models)}")
    print(f"Poe models: {len(poe_models)}")
    print(f"Total models: {len(all_models)}")
    print(f"\nResults saved to: {output_file}")
    
    # Print a few example models
    if all_models:
        print("\n" + "="*60)
        print("SAMPLE MODELS (first 5)")
        print("="*60)
        for i, model in enumerate(all_models[:5], 1):
            print(f"\n{i}. {model['name']}")
            print(f"   ID: {model['model_id']}")
            print(f"   Context: {model['context_length']} tokens")
            print(f"   Costs: Prompt=${model['prompt_cost']}, Completion=${model['completion_cost']}")

if __name__ == "__main__":
    main()

