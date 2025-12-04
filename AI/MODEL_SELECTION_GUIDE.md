# AI Model Selection Guide

## Summary
- **Total models available**: 336 from OpenRouter
- **Recommended models**: 200 (filtered for popular and well-performing models)
- **CSV files generated**:
  - `available_models.csv` - Complete list of all 336 models
  - `recommended_models.csv` - Curated list of 200 recommended models

---

## Top Recommendations by Use Case

### 🎯 Best for Poetry Generation (Creative Writing)

#### FREE Options:
1. **Google Gemini 2.0 Flash Experimental**
   - Context: 1,048,576 tokens (1M+)
   - Cost: FREE
   - Model ID: `google/gemini-2.0-flash-exp:free`
   - Best for: Fast creative writing, large context

2. **Meta Llama 3.3 70B Instruct**
   - Context: 131,072 tokens
   - Cost: FREE
   - Model ID: `meta-llama/llama-3.3-70b-instruct:free`
   - Best for: High-quality creative text, good reasoning

3. **Amazon Nova 2 Lite**
   - Context: 1,000,000 tokens
   - Cost: FREE
   - Model ID: `amazon/nova-2-lite-v1:free`
   - Best for: Fast everyday tasks, large documents

#### LOW COST Premium Options:
1. **Claude 3.5 Sonnet** (if available)
   - Excellent for creative writing and poetry
   - Strong instruction following
   - Great at understanding nuance

2. **GPT-4 Turbo/GPT-4o**
   - Versatile and creative
   - Good at understanding prompts
   - Wide context window

3. **Qwen 3 Coder 480B**
   - Context: 262,000 tokens
   - Cost: FREE
   - Excellent for structured creative tasks

---

## Cost Tiers Overview

### 🆓 FREE Tier (12 models)
Perfect for testing and high-volume use:
- Amazon Nova 2 Lite (1M context)
- Google Gemini 2.0 Flash (1M context)
- Meta Llama 3.3 70B
- Meta Llama 3.2 3B
- Mistral 7B Instruct
- Mistral Small 3.1 24B
- Qwen3 235B, 4B, Coder 480B
- DeepSeek R1T Chimera models

### 💰 Very Low Cost ($0.00-$0.50 per 1M tokens)
Great balance of cost and quality:
- Multiple Llama variants
- Mistral models
- Qwen models
- DeepSeek models

### 💵 Low Cost ($0.50-$2.00 per 1M tokens)
Professional quality:
- Claude variants
- GPT-3.5 Turbo
- Gemini Pro

### 💎 Premium ($10+ per 1M tokens)
Top-tier performance:
- GPT-4
- Claude 3 Opus
- Advanced reasoning models

---

## Recommended Testing Strategy

### Phase 1: Free Models Test (No Cost)
Test these 3 models with your poetry prompts:
1. **Gemini 2.0 Flash Experimental** - fastest, large context
2. **Llama 3.3 70B** - best free quality
3. **Amazon Nova 2 Lite** - good balance

### Phase 2: Low-Cost Models (if needed)
If free models don't meet quality needs:
1. Test Claude 3.5 Haiku (very affordable)
2. Test GPT-3.5 Turbo (proven quality)

### Phase 3: Premium Models (for comparison)
For final quality benchmark:
1. Claude 3.5 Sonnet
2. GPT-4o

---

## Context Window Comparison

| Model | Context Length | Cost Tier |
|-------|---------------|-----------|
| Google Gemini 2.0 Flash | 1,048,576 | FREE |
| Amazon Nova 2 Lite | 1,000,000 | FREE |
| Qwen3 Coder 480B | 262,000 | FREE |
| DeepSeek R1T Chimera | 163,840 | FREE |
| Llama 3.3 70B | 131,072 | FREE |
| Mistral Small 3.1 24B | 128,000 | FREE |

---

## Quick Start Commands

### To test a model via API:
```python
import requests

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

data = {
    "model": "google/gemini-2.0-flash-exp:free",  # Change model ID here
    "messages": [
        {"role": "user", "content": "Write a haiku about autumn"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

---

## Notes on Poe API
- Poe API doesn't provide a public model listing endpoint
- Poe works on a subscription basis rather than pay-per-token
- Available models through Poe typically include:
  - GPT-4, GPT-3.5-Turbo
  - Claude 3 variants
  - Google PaLM
  - Access is subscription-based (monthly fee)

---

## Files Generated

1. **available_models.csv** - All 336 models with full details
2. **recommended_models.csv** - 200 curated models organized by cost tier
3. **This guide** - Selection recommendations

---

## My Recommendations for Poetry AI Project

For your poetry generation project, I recommend starting with:

1. **Primary Model**: Google Gemini 2.0 Flash Experimental (FREE)
   - Huge context window (1M tokens)
   - Fast responses
   - Good creative capabilities
   - Zero cost for testing

2. **Backup/Alternative**: Meta Llama 3.3 70B (FREE)
   - Excellent quality
   - Good instruction following
   - Free tier available

3. **Premium Option** (if budget allows): Claude 3.5 Sonnet
   - Best-in-class creative writing
   - Excellent at nuanced understanding
   - Worth testing for quality comparison

**Cost Strategy**: Start with free models for development and testing. Only move to paid models if you need specific capabilities that free models don't provide.

