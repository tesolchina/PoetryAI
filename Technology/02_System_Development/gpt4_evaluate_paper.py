"""
GPT-4 Evaluation Script for Conference Paper
Uses OpenRouter API to evaluate the revised conference paper draft
against Simon's original feedback criteria.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

def read_file(filepath):
    """Read file contents"""
    # Convert Path object to string explicitly
    filepath_str = str(filepath)
    print(f"   Attempting to read: {filepath_str}")
    
    # Check if file exists
    if not Path(filepath_str).exists():
        print(f"   ✗ File not found: {filepath_str}")
        return ""
    
    with open(filepath_str, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"   ✓ Successfully read {len(content)} characters")
        return content

def call_gpt4_via_openrouter(prompt, model="openai/gpt-4o"):
    """
    Call GPT-4 through OpenRouter API
    
    Args:
        prompt: The evaluation prompt
        model: Model identifier (default: gpt-4o)
    
    Returns:
        Response text from GPT-4
    """
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 8000
    }
    
    print(f"Calling {model} via OpenRouter...")
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    
    result = response.json()
    return result['choices'][0]['message']['content']

def create_evaluation_prompt(paper_content, simon_feedback):
    """
    Create comprehensive evaluation prompt combining paper and Simon's feedback
    
    Args:
        paper_content: The revised conference paper draft
        simon_feedback: Simon's original detailed feedback
    
    Returns:
        Formatted evaluation prompt for GPT-4
    """
    prompt = f"""You are an expert academic reviewer evaluating a revised research paper for a conference submission. You will assess whether the revisions have successfully addressed the original feedback provided by a previous reviewer (Simon).

# ORIGINAL PAPER DRAFT TO EVALUATE

{paper_content}

# ORIGINAL REVIEWER FEEDBACK (Simon's Comments)

{simon_feedback}

---

# YOUR EVALUATION TASK

Please provide a comprehensive evaluation of the revised paper, structured as follows:

## 1. OVERALL ASSESSMENT
- Has the paper successfully addressed Simon's main concerns?
- Overall quality and readiness for conference submission
- Strengths and remaining weaknesses

## 2. ASSESSMENT OF SIMON'S FOUR MAIN CONCERNS

### Concern #1: Introduce creative writing problems more deeply
- **Current state**: Assess whether the paper now provides sufficient depth on L2 creative writing pedagogical challenges
- **Evidence**: Specific sections/paragraphs that address or fail to address this concern
- **Verdict**: Fully addressed / Partially addressed / Not addressed
- **Recommendations**: What improvements are still needed (if any)

### Concern #2: Postpone AI assistance introduction
- **Current state**: Assess whether AI is introduced at the appropriate point in the narrative
- **Evidence**: How the introduction is now structured
- **Verdict**: Fully addressed / Partially addressed / Not addressed
- **Recommendations**: What improvements are still needed (if any)

### Concern #3: Clarify research objectives/questions
- **Current state**: Are research questions explicit and well-formulated?
- **Evidence**: Where RQs appear and their clarity
- **Verdict**: Fully addressed / Partially addressed / Not addressed
- **Recommendations**: What improvements are still needed (if any)

### Concern #4: Expand discussion of three engagement types with prior studies
- **Current state**: Is the theoretical grounding of the three interaction types sufficiently deep?
- **Evidence**: Literature citations and depth of discussion for each type
- **Verdict**: Fully addressed / Partially addressed / Not addressed
- **Recommendations**: What improvements are still needed (if any)

## 3. STRUCTURAL AND CONTENT QUALITY

### Introduction Section (1.1-1.4)
- Narrative flow and logical progression
- Balance between problem establishment and AI introduction
- Depth of pedagogical challenge discussion
- Quality of theoretical framework presentation

### Research Design Section
- Clarity and appropriateness of methodology
- Adequate detail for replication

### Findings Section (3.1-3.5)
- Clarity and persuasiveness of results presentation
- Effective use of figures (replacing tables)
- Quality of qualitative evidence (quotes)
- Interpretation depth

### Conclusion Section
- Appropriate synthesis of key findings
- Discussion of implications
- Appropriate scope (not overreaching given preliminary data)

## 4. SPECIFIC ISSUES AND LINE-BY-LINE OBSERVATIONS

Identify at least 5-10 specific issues:
- Formatting errors (e.g., missing spaces, typos)
- Unclear or problematic phrasing
- Claims that need qualification
- Missing or weak connections to literature
- Statistical interpretations that need clarification
- Areas where the argument could be strengthened

For each issue:
- **Location**: Section and approximate line/paragraph
- **Issue**: Description of the problem
- **Severity**: Critical / Moderate / Minor
- **Suggested fix**: Specific recommendation

## 5. WORD COUNT AND SCOPE ASSESSMENT
- Is the 2,000-word target appropriate for the content?
- Are there areas that feel rushed or over-condensed?
- Are there unnecessary elements that could be cut?

## 6. FIGURE INTEGRATION ASSESSMENT
- Quality and appropriateness of the 4 figures
- Effective replacement of original tables
- Figure captions and in-text references
- Visual clarity and professional presentation

## 7. COMPARISON WITH SIMON'S STRUCTURAL SUGGESTIONS

Simon suggested a revised introduction structure:
1. Section 1.1: Deep dive into L2 creative writing pedagogical challenges
2. Section 1.2: Cautious introduction of AI as potential solution
3. Section 1.3: LLM parameters as pedagogical levers
4. Section 1.4: Theoretical framework with expanded literature
5. Section 1.5: Explicit research questions and contributions

Assess how well the revised paper follows or improves upon this structure.

## 8. FINAL RECOMMENDATIONS

### Critical Issues (Must Fix Before Submission)
List 3-5 most important changes needed

### Suggested Improvements (Strongly Recommended)
List 5-8 improvements that would significantly strengthen the paper

### Optional Enhancements (Nice to Have)
List 3-5 minor improvements

## 9. SUBMISSION READINESS RATING

Provide an overall rating:
- **Ready to submit**: Minimal changes needed
- **Nearly ready**: Minor revisions required (1-2 days work)
- **Needs revision**: Moderate revisions required (3-5 days work)
- **Major revision needed**: Substantial work required (1-2 weeks)

Justify your rating based on the analysis above.

---

Please be thorough, specific, and constructive in your evaluation. Reference specific sections and provide concrete examples. Your goal is to help ensure this paper is as strong as possible for conference submission while acknowledging the constraints of preliminary results from only Session 1 of a 3-session study."""

    return prompt

def save_evaluation(evaluation_text, output_dir):
    """
    Save evaluation to timestamped markdown file
    
    Args:
        evaluation_text: GPT-4 evaluation response
        output_dir: Directory to save the evaluation
    
    Returns:
        Path to saved file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"GPT4_Evaluation_{timestamp}.md"
    filepath = output_dir / filename
    
    # Create markdown document with metadata
    content = f"""# GPT-4 Evaluation of Conference Paper Draft

**Model Used:** OpenAI GPT-4o via OpenRouter
**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Evaluation Framework:** Based on Simon's original feedback (LLM_Review_20251204_115453.md)

---

{evaluation_text}

---

## Evaluation Metadata

- **Paper Evaluated:** `draft of conference paper`
- **Reference Feedback:** Simon's comments from Gemini 2.5 Flash review
- **Word Count Target:** 2,000 words (excluding references)
- **Study Status:** Preliminary results from Session 1 (10 participants)
- **Figures Integrated:** 4 figures (interaction distribution, authorship/satisfaction, three types framework, Type C prediction)
"""
    
    filepath.write_text(content, encoding='utf-8')
    print(f"\n✓ Evaluation saved to: {filepath}")
    return filepath

def main():
    """Main evaluation workflow"""
    
    # Define paths - use absolute paths for Windows
    base_dir = Path(r"c:\Users\ruobin Yu\.vscode\PoetryAI-6")
    # Use the actual working file that has all the revisions
    paper_path = base_dir / "Manuscript" / "Preliminary_Results_Essay_Restructured.md"
    simon_feedback_path = base_dir / "Manuscript" / "conference_paper" / "LLM_Review_20251204_115453.md"
    output_dir = base_dir / "Manuscript" / "conference_paper"
    
    print("=" * 80)
    print("GPT-4 EVALUATION OF CONFERENCE PAPER")
    print("=" * 80)
    
    # Read files
    print("\n1. Reading conference paper draft...")
    paper_content = read_file(paper_path)
    print(f"   ✓ Loaded {len(paper_content)} characters")
    
    print("\n2. Reading Simon's original feedback...")
    simon_feedback = read_file(simon_feedback_path)
    print(f"   ✓ Loaded {len(simon_feedback)} characters")
    
    # Create evaluation prompt
    print("\n3. Creating evaluation prompt...")
    prompt = create_evaluation_prompt(paper_content, simon_feedback)
    print(f"   ✓ Prompt created ({len(prompt)} characters)")
    
    # Call GPT-4
    print("\n4. Sending to GPT-4 via OpenRouter...")
    print("   (This may take 30-60 seconds for comprehensive evaluation...)")
    try:
        evaluation = call_gpt4_via_openrouter(prompt)
        print(f"   ✓ Received evaluation ({len(evaluation)} characters)")
    except Exception as e:
        print(f"\n✗ Error calling GPT-4: {e}")
        raise
    
    # Save evaluation
    print("\n5. Saving evaluation...")
    output_path = save_evaluation(evaluation, output_dir)
    
    # Print summary
    print("\n" + "=" * 80)
    print("EVALUATION COMPLETE")
    print("=" * 80)
    print(f"\nFull evaluation saved to:")
    print(f"  {output_path}")
    print("\nNext steps:")
    print("  1. Review the evaluation document")
    print("  2. Address critical issues identified")
    print("  3. Implement recommended improvements")
    print("  4. Final proofreading before submission")
    print("\n" + "=" * 80)
    
    # Print first few lines of evaluation as preview
    print("\n📄 EVALUATION PREVIEW (first 500 characters):\n")
    print(evaluation[:500] + "...")
    
    return output_path

if __name__ == "__main__":
    main()
