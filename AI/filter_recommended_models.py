#!/usr/bin/env python3
"""
Filter and organize models into recommended categories
"""

import csv
import json

def load_models(filename):
    """Load models from CSV file"""
    models = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            models.append(row)
    return models

def filter_recommended_models(models):
    """Filter and categorize recommended models"""
    
    # Keywords for popular model families
    popular_keywords = [
        'gpt-4', 'gpt-3.5', 'claude', 'gemini', 'llama', 'mistral',
        'qwen', 'deepseek', 'phi', 'wizardlm', 'nova', 'command'
    ]
    
    recommended = []
    
    for model in models:
        model_id_lower = model['model_id'].lower()
        name_lower = model['name'].lower()
        
        # Check if it's a popular model
        is_popular = any(keyword in model_id_lower or keyword in name_lower 
                        for keyword in popular_keywords)
        
        if is_popular:
            # Parse costs
            try:
                prompt_cost = float(model['prompt_cost']) if model['prompt_cost'] != 'N/A' else 0
                completion_cost = float(model['completion_cost']) if model['completion_cost'] != 'N/A' else 0
            except (ValueError, TypeError):
                prompt_cost = 0
                completion_cost = 0
            
            # Calculate cost per million tokens (for easier comparison)
            prompt_cost_per_million = prompt_cost * 1_000_000
            completion_cost_per_million = completion_cost * 1_000_000
            
            # Add categorization
            if prompt_cost == 0 and completion_cost == 0:
                cost_tier = 'Free'
            elif prompt_cost_per_million < 0.5:
                cost_tier = 'Very Low Cost'
            elif prompt_cost_per_million < 2:
                cost_tier = 'Low Cost'
            elif prompt_cost_per_million < 10:
                cost_tier = 'Medium Cost'
            else:
                cost_tier = 'Premium'
            
            recommended.append({
                'provider': model['provider'],
                'model_id': model['model_id'],
                'name': model['name'],
                'context_length': model['context_length'],
                'prompt_cost_per_1M': f"${prompt_cost_per_million:.4f}",
                'completion_cost_per_1M': f"${completion_cost_per_million:.4f}",
                'cost_tier': cost_tier,
                'description': model['description'][:80] if model['description'] != 'N/A' else ''
            })
    
    # Sort by cost tier and then by name
    tier_order = {'Free': 0, 'Very Low Cost': 1, 'Low Cost': 2, 'Medium Cost': 3, 'Premium': 4}
    recommended.sort(key=lambda x: (tier_order.get(x['cost_tier'], 5), x['name']))
    
    return recommended

def save_recommended_csv(models, filename):
    """Save filtered models to CSV"""
    if not models:
        print("No models to save!")
        return
    
    fieldnames = ['cost_tier', 'name', 'model_id', 'context_length', 
                  'prompt_cost_per_1M', 'completion_cost_per_1M', 'provider', 'description']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(models)
    
    print(f"Saved {len(models)} recommended models to {filename}")

def print_summary_by_tier(models):
    """Print summary organized by cost tier"""
    print("\n" + "="*80)
    print("RECOMMENDED MODELS BY COST TIER")
    print("="*80)
    
    current_tier = None
    for model in models:
        if model['cost_tier'] != current_tier:
            current_tier = model['cost_tier']
            print(f"\n{'='*80}")
            print(f"{current_tier.upper()}")
            print("="*80)
        
        print(f"\n• {model['name']}")
        print(f"  Model ID: {model['model_id']}")
        print(f"  Context: {model['context_length']} tokens")
        print(f"  Cost per 1M tokens: {model['prompt_cost_per_1M']} (prompt) / {model['completion_cost_per_1M']} (completion)")
        if model['description']:
            print(f"  Note: {model['description']}")

def main():
    input_file = "/Users/simonwang/Documents/Usage/AIpoetry/AI/available_models.csv"
    output_file = "/Users/simonwang/Documents/Usage/AIpoetry/AI/recommended_models.csv"
    
    print("Loading all models...")
    all_models = load_models(input_file)
    print(f"Loaded {len(all_models)} models")
    
    print("\nFiltering recommended models...")
    recommended = filter_recommended_models(all_models)
    
    print(f"\nFound {len(recommended)} recommended models")
    
    # Save to CSV
    save_recommended_csv(recommended, output_file)
    
    # Print summary
    print_summary_by_tier(recommended)
    
    print("\n" + "="*80)
    print(f"Full list saved to: {output_file}")
    print("="*80)

if __name__ == "__main__":
    main()

