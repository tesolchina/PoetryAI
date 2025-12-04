"""
Evaluate Preliminary Results Essay using GPT-4 via OpenRouter
Based on review format from LLM_Review_20251204_115453.md and instructions.md
"""

import requests
import os
from pathlib import Path
from datetime import datetime

# Load environment variables
def load_env():
    env_path = Path(__file__).parent.parent.parent / '.env'
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

load_env()

def read_essay():
    """Read the restructured essay"""
    essay_path = Path(__file__).parent.parent / 'Preliminary_Results_Essay_Restructured.md'
    with open(essay_path, 'r', encoding='utf-8') as f:
        return f.read()

def create_evaluation_prompt(essay_content):
    """Create comprehensive evaluation prompt based on Simon's concerns and review format"""
    
    prompt = f"""You are an expert academic reviewer evaluating a preliminary results essay for a conference submission. Please provide comprehensive, constructive feedback following this structure:

**CONTEXT:**
This paper investigates how LLM parameter configurations (temperature/top-p) affect human-AI interaction types and learner outcomes (authorship, satisfaction, motivation) in AI-assisted L2 poetry writing.

**SUPERVISOR'S SPECIFIC CONCERNS TO ADDRESS:**
1. Introduce creative writing problems more deeply before discussing AI
2. Postpone AI assistance introduction until problems are well-established
3. Clarify research objectives/questions 
4. Expand discussion of three engagement types with more prior studies

**YOUR EVALUATION TASK:**

## 1. OVERALL ASSESSMENT
Provide a 2-3 paragraph overall assessment of the paper's strengths, weaknesses, and potential impact.

## 2. SPECIFIC COMMENTS ON SUPERVISOR'S CONCERNS

For each of the 4 concerns above:
- **Assessment of current state:** Has this concern been adequately addressed? What remains?
- **Specific suggestions for improvement:** Concrete recommendations
- **Concrete examples/recommendations:** Detailed guidance with specific wording suggestions where helpful

## 3. STRUCTURAL REVISION SUGGESTIONS

Propose how to restructure sections if needed. Be specific about:
- Which sections need expansion/condensation
- What order sections should follow
- What new subsections might be needed

## 4. LINE-BY-LINE SUGGESTIONS

Provide at least 10 specific line-by-line suggestions with:
- Quote the original text
- Explain the issue
- Provide revised wording
- Justify the change

## 5. RECOMMENDATIONS FOR ADDITIONAL LITERATURE

Identify gaps in the literature review:
- What key papers/concepts are missing?
- What theoretical frameworks should be added?
- Suggest 5-10 specific references that would strengthen the paper

## 6. CONCLUSION

- Prioritized action items for revision (top 5)
- Estimated impact of changes on paper quality
- Overall recommendation (accept with major revisions / minor revisions / reject)

**ESSAY TO REVIEW:**

{essay_content}

---

Please provide detailed, actionable feedback that will help improve this paper for conference publication.
"""
    return prompt

def call_gpt4(prompt, model="openai/gpt-4o"):
    """Call GPT-4 via OpenRouter"""
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 4000
    }
    
    print(f"Calling {model}...")
    print("This may take a minute or two...\n")
    
    response = requests.post(url, headers=headers, json=payload, timeout=120)
    response.raise_for_status()
    
    result = response.json()
    return result['choices'][0]['message']['content']

def save_review(review_content, model_name):
    """Save review to markdown file"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(__file__).parent
    output_file = output_dir / f"LLM_Review_{timestamp}.md"
    
    # Create header
    header = f"""# LLM Review of Preliminary Results Essay

**Model Used:** {model_name}
**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Evaluator:** GPT-4 (OpenAI via OpenRouter)

---

"""
    
    full_content = header + review_content
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"\n✓ Review saved to: {output_file}")
    return output_file

def main():
    """Main execution function"""
    
    print("=== Essay Evaluation using GPT-4 ===\n")
    
    try:
        # Read essay
        print("Reading essay...")
        essay_content = read_essay()
        print(f"✓ Essay loaded ({len(essay_content)} characters)\n")
        
        # Create evaluation prompt
        print("Creating evaluation prompt...")
        prompt = create_evaluation_prompt(essay_content)
        print(f"✓ Prompt created ({len(prompt)} characters)\n")
        
        # Call GPT-4
        model = "openai/gpt-4o"
        review = call_gpt4(prompt, model)
        
        print("✓ Review completed\n")
        
        # Save review
        output_file = save_review(review, model)
        
        print(f"\n✓ Evaluation complete!")
        print(f"✓ Review saved to: {output_file.name}")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        raise

if __name__ == "__main__":
    main()
