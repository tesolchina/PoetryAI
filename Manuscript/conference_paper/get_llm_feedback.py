#!/usr/bin/env python3
"""
Script to get LLM feedback on the preliminary results essay.
Uses Google Gemini 2.5 Flash for cost-effective, high-quality review.
"""

import requests
import json
from datetime import datetime

# Configuration
API_KEY = "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"
MODEL = "google/gemini-2.5-flash"  # Very low cost: $0.30/$2.50 per 1M tokens
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Read the essay
with open("Preliminary_Results_Essay_Restructured.md", "r", encoding="utf-8") as f:
    essay_content = f.read()

# Prepare the review prompt
review_prompt = f"""You are an expert academic reviewer specializing in educational technology, L2 writing pedagogy, and human-AI collaboration research. Please provide a detailed, constructive review of the following conference paper.

**REVIEWER INSTRUCTIONS:**

The author (Simon) has requested specific feedback on the following issues:

1. **Introduce creative writing problems more deeply** - The paper should establish the challenges and problems in creative writing pedagogy more thoroughly before introducing AI assistance as a solution.

2. **Postpone AI assistance introduction** - Delay discussing AI until the pedagogical problems have been fully established.

3. **Clarify research objectives/questions** - The research objectives or questions need to be stated more explicitly and clearly.

4. **Expand discussion of three engagement types with prior studies** - The three ways of student engagements (Constraint Repair, Exemplar Giving, Surprise Harvest) should be introduced with more substantial discussion of relevant prior studies.

**YOUR TASK:**

Please provide:

1. **OVERALL ASSESSMENT** (1 paragraph): Your general impression of the paper's strengths and areas for improvement.

2. **SPECIFIC COMMENTS ON SIMON'S CONCERNS** (detailed section-by-section):
   - For each of the 4 issues above, provide:
     a) Assessment of the current state
     b) Specific suggestions for improvement
     c) Concrete examples or recommendations

3. **STRUCTURAL REVISION SUGGESTIONS**:
   - Recommend a revised structure for the Introduction section that addresses concerns #1 and #2
   - Suggest where and how to clarify research questions (concern #3)
   - Propose how to integrate more prior studies for the three interaction types (concern #4)

4. **LINE-BY-LINE SUGGESTIONS** (at least 10 specific examples):
   - Identify specific paragraphs/sections that need revision
   - Provide concrete rewrite suggestions or additional content to add
   - Flag any claims that need more support or citations

5. **RECOMMENDATIONS FOR ADDITIONAL LITERATURE**:
   - Suggest specific research areas or key papers that should be cited
   - Identify gaps in the literature review

6. **CONCLUSION**:
   - Prioritized action items for revision
   - Estimated impact of changes on paper quality

Please be thorough, specific, and constructive. Use academic language appropriate for a conference paper review.

---

**PAPER TO REVIEW:**

{essay_content}
"""

print("=" * 80)
print("SUBMITTING ESSAY TO LLM FOR REVIEW")
print("=" * 80)
print(f"Model: {MODEL}")
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Essay length: {len(essay_content)} characters")
print(f"Estimated tokens: ~{len(essay_content.split())}")
print("=" * 80)
print("\nSending request to OpenRouter API...")

# Prepare the API request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:3000",  # Optional, for rankings
    "X-Title": "Poetry AI Project - Essay Review"  # Optional, for rankings
}

data = {
    "model": MODEL,
    "messages": [
        {
            "role": "user",
            "content": review_prompt
        }
    ],
    "temperature": 0.7,  # Balanced for analytical review
    "max_tokens": 8000   # Allow for comprehensive feedback
}

try:
    response = requests.post(API_URL, headers=headers, json=data, timeout=180)
    response.raise_for_status()
    
    result = response.json()
    
    if "choices" in result and len(result["choices"]) > 0:
        review_content = result["choices"][0]["message"]["content"]
        
        print("\n✓ Review received successfully!")
        print(f"Response length: {len(review_content)} characters")
        
        # Save the review to a file
        output_filename = f"LLM_Review_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(f"# LLM Review of Preliminary Results Essay\n\n")
            f.write(f"**Model Used:** {MODEL}\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Cost Tier:** Very Low Cost ($0.30 input / $2.50 output per 1M tokens)\n\n")
            f.write("---\n\n")
            f.write(review_content)
        
        print(f"\n✓ Review saved to: {output_filename}")
        print("\n" + "=" * 80)
        print("PREVIEW OF REVIEW (first 1000 characters):")
        print("=" * 80)
        print(review_content[:1000])
        print("\n[...see full review in output file...]")
        print("=" * 80)
        
        # Also print usage information if available
        if "usage" in result:
            usage = result["usage"]
            print(f"\nAPI Usage:")
            print(f"  - Prompt tokens: {usage.get('prompt_tokens', 'N/A')}")
            print(f"  - Completion tokens: {usage.get('completion_tokens', 'N/A')}")
            print(f"  - Total tokens: {usage.get('total_tokens', 'N/A')}")
            
            # Estimate cost
            prompt_cost = (usage.get('prompt_tokens', 0) / 1_000_000) * 0.30
            completion_cost = (usage.get('completion_tokens', 0) / 1_000_000) * 2.50
            total_cost = prompt_cost + completion_cost
            print(f"  - Estimated cost: ${total_cost:.4f}")
        
    else:
        print("Error: Unexpected response format")
        print(json.dumps(result, indent=2))
        
except requests.exceptions.RequestException as e:
    print(f"\n✗ Error occurred: {e}")
    if hasattr(e.response, 'text'):
        print(f"Response: {e.response.text}")
except Exception as e:
    print(f"\n✗ Unexpected error: {e}")

print("\n" + "=" * 80)
print("SCRIPT COMPLETED")
print("=" * 80)

