#!/usr/bin/env python3
"""
Improved PDF to Markdown Converter - V2
Uses better models and improved prompts for higher quality output
"""

import os
import csv
import json
import time
from datetime import datetime
from pathlib import Path
import requests

# Configuration
LITERATURE_DIR = Path(__file__).parent
API_KEY_FILE = LITERATURE_DIR.parent / "AI" / "openrouterKey.md"
TRACKER_CSV = LITERATURE_DIR / "pdf_conversion_tracker.csv"
PROCESS_LOG = LITERATURE_DIR / "conversion_process.log"

# Model selection - Using cheaper paid model with longer timeout
MODELS = [
    {
        "id": "google/gemini-2.0-flash-001",
        "name": "Google Gemini 2.0 Flash",
        "cost_per_1m_prompt": 0.10,
        "cost_per_1m_completion": 0.40,
        "context_length": 1048576,
        "timeout": 240,  # 4 minutes for large PDFs
    },
    {
        "id": "deepseek/deepseek-chat-v3.1",
        "name": "DeepSeek V3.1",
        "cost_per_1m_prompt": 0.20,
        "cost_per_1m_completion": 0.80,
        "context_length": 163840,
        "timeout": 240,
    },
]

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


def log_message(message, to_file_only=False):
    """Write message to console and log file in real-time"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    
    # Write to log file
    with open(PROCESS_LOG, 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')
        f.flush()  # Force write immediately
    
    # Print to console unless file-only
    if not to_file_only:
        print(message)


def load_api_key():
    """Load OpenRouter API key from file"""
    try:
        with open(API_KEY_FILE, 'r') as f:
            api_key = f.read().strip()
        return api_key
    except Exception as e:
        print(f"❌ Error loading API key: {e}")
        return None


def load_tracker():
    """Load the CSV tracker into memory"""
    rows = []
    with open(TRACKER_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def save_tracker(rows):
    """Save updated tracker back to CSV"""
    if not rows:
        return
    
    fieldnames = rows[0].keys()
    with open(TRACKER_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    # Silent save - no logging needed for every save


def extract_pdf_text_pdfplumber(pdf_path):
    """Extract text from PDF using pdfplumber"""
    try:
        import pdfplumber
        
        pages_text = []
        with pdfplumber.open(pdf_path) as pdf:
            num_pages = len(pdf.pages)
            
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                pages_text.append({
                    'page_num': page_num + 1,
                    'text': text if text else ""
                })
            
            return pages_text, num_pages
    except Exception as e:
        print(f"❌ Error extracting PDF: {e}")
        return None, 0


def convert_whole_pdf_to_markdown(all_text, model, api_key, max_retries=3):
    """Convert entire PDF text to markdown in one request (for small PDFs)"""
    
    prompt = f"""You are an expert academic document converter specializing in high-fidelity PDF-to-Markdown conversion with ZERO content loss.

MISSION: Convert this academic paper to clean, professional markdown while preserving 100% of the content and formatting.

CRITICAL REQUIREMENTS - ZERO CONTENT LOSS:
1. Preserve EVERY word, sentence, citation, reference, footnote, and number
2. Maintain ALL author names, affiliations, emails, dates, and metadata
3. Keep ALL tables complete with proper markdown table syntax
4. Preserve ALL mathematical notation, formulas, and equations
5. Maintain ALL figures captions, references, and descriptions
6. Keep ALL section headings with proper hierarchy (# ## ### ####)
7. Preserve ALL lists (numbered, bulleted, nested)
8. Keep ALL URLs, DOIs, ORCIDs, and links intact
9. Maintain paragraph structure and logical flow
10. Preserve acknowledgments, funding information, and supplementary notes

FORMATTING RULES:
- Use # for main title, ## for major sections, ### for subsections, #### for sub-subsections
- Format citations exactly as they appear: [1], (Author, Year), etc.
- Convert tables to markdown table format (| header | header |)
- Keep bold (**text**) and italic (*text*) formatting where evident
- Preserve block quotes using > prefix
- Keep code or technical notation in backticks when appropriate
- Maintain proper spacing between sections

OUTPUT RULES - ABSOLUTELY CRITICAL:
- Output ONLY the markdown content
- NO code fences (```), NO wrappers, NO ```markdown
- Start immediately with the document content
- Do NOT add any commentary, explanations, or meta-text
- Do NOT omit or summarize any content
- When in doubt, include rather than exclude

Academic paper text to convert:
{all_text}"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/simonwang/AIpoetry",
    }
    
    data = {
        "model": model["id"],
        "messages": [
            {
                "role": "system",
                "content": "You are an expert academic document converter. Your core mission is ZERO content loss - preserve every word, citation, table, formula, and formatting element. Output clean markdown directly without any code fences, wrappers, or commentary. Never use ```markdown or ``` in your output."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.1,  # Very low for consistency and accuracy
    }
    
    # Retry logic
    timeout = model.get('timeout', 180)
    for attempt in range(max_retries):
        try:
            response = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=timeout)
            response.raise_for_status()
            
            result = response.json()
            markdown = result['choices'][0]['message']['content']
            
            # Post-processing: remove code fences if model added them anyway
            markdown = markdown.strip()
            if markdown.startswith('```markdown'):
                markdown = markdown[11:]  # Remove ```markdown
            if markdown.startswith('```'):
                markdown = markdown[3:]  # Remove ```
            if markdown.endswith('```'):
                markdown = markdown[:-3]  # Remove trailing ```
            markdown = markdown.strip()
            
            usage = result.get('usage', {})
            prompt_tokens = usage.get('prompt_tokens', 0)
            completion_tokens = usage.get('completion_tokens', 0)
            
            return markdown, prompt_tokens, completion_tokens, None
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                wait_time = (2 ** attempt) * 3
                print(f"\n⚠️  Rate limit. Waiting {wait_time}s (retry {attempt+1}/{max_retries})...", flush=True)
                time.sleep(wait_time)
                continue
            else:
                return None, 0, 0, f"HTTP error: {e}"
        except Exception as e:
            return None, 0, 0, f"Error: {e}"
    
    return None, 0, 0, "Max retries exceeded"


def process_pdf(row, api_key, model):
    """Process a single PDF file"""
    pdf_path = LITERATURE_DIR / row['relative_path']
    output_path = LITERATURE_DIR / row['output_md_path']
    
    log_message(f"\n{'='*80}")
    log_message(f"📄 {row['filename']}")
    log_message(f"   Category: {row['category']}")
    log_message(f"   Model: {model['name']} (${model['cost_per_1m_prompt']}-${model['cost_per_1m_completion']}/1M tokens)")
    log_message(f"{'='*80}")
    
    if not pdf_path.exists():
        log_message(f"❌ PDF not found: {pdf_path}")
        row['status'] = 'error'
        row['notes'] = 'PDF file not found'
        return row
    
    row['status'] = 'processing'
    
    # Extract PDF text
    log_message("📖 Extracting text from PDF...")
    pages_text, num_pages = extract_pdf_text_pdfplumber(pdf_path)
    
    if not pages_text:
        log_message("❌ Failed to extract text")
        row['status'] = 'error'
        row['notes'] = 'Failed to extract text'
        return row
    
    log_message(f"✅ Extracted {num_pages} pages")
    row['page_count'] = str(num_pages)
    
    # Combine all pages
    all_text = "\n\n".join([f"[Page {p['page_num']}]\n{p['text']}" for p in pages_text])
    
    # Check if text fits in context (rough estimate: 4 chars = 1 token)
    estimated_tokens = len(all_text) // 4
    
    if estimated_tokens > model['context_length'] * 0.7:  # Use 70% of context to be safe
        log_message(f"⚠️  PDF too large ({estimated_tokens:,} est. tokens) for single-shot conversion")
        row['status'] = 'error'
        row['notes'] = f'PDF too large ({estimated_tokens:,} tokens). Try page-by-page.'
        return row
    
    log_message(f"🔄 Converting to markdown (est. {estimated_tokens:,} tokens)...")
    
    # Convert to markdown
    markdown, prompt_tokens, completion_tokens, error = convert_whole_pdf_to_markdown(
        all_text, model, api_key
    )
    
    if error:
        log_message(f"❌ Conversion failed: {error}")
        row['status'] = 'error'
        row['notes'] = f'Conversion failed: {error}'
        return row
    
    # Calculate cost
    total_cost = (
        (prompt_tokens / 1_000_000) * model['cost_per_1m_prompt'] +
        (completion_tokens / 1_000_000) * model['cost_per_1m_completion']
    )
    
    # Add metadata header
    metadata = f"""---
source_pdf: {row['filename']}
converted_date: {datetime.now().isoformat()}
total_pages: {num_pages}
model: {model['name']}
total_cost_usd: ${total_cost:.6f}
prompt_tokens: {prompt_tokens:,}
completion_tokens: {completion_tokens:,}
---

"""
    
    final_markdown = metadata + markdown
    
    # Save markdown file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_markdown)
    
    log_message(f"✅ Saved to: {output_path.name}")
    log_message(f"💰 Cost: ${total_cost:.6f}")
    log_message(f"📊 Tokens: {prompt_tokens:,} prompt + {completion_tokens:,} completion")
    
    # Update row
    row['status'] = 'completed'
    row['model_used'] = model['name']
    row['prompt_tokens'] = str(prompt_tokens)
    row['completion_tokens'] = str(completion_tokens)
    row['total_cost_usd'] = f"{total_cost:.6f}"
    row['date_processed'] = datetime.now().isoformat()
    row['notes'] = 'Successfully converted'
    
    return row


def main():
    """Main execution"""
    # Initialize log file
    with open(PROCESS_LOG, 'w', encoding='utf-8') as f:
        f.write(f"PDF to Markdown Conversion Log - Started {datetime.now()}\n")
        f.write("="*80 + "\n\n")
    
    log_message("="*80)
    log_message("PDF to Markdown Converter V2 - Batch Processing")
    log_message("="*80)
    
    api_key = load_api_key()
    if not api_key:
        log_message("❌ Cannot proceed without API key")
        return
    
    log_message(f"\n📋 Loading tracker from {TRACKER_CSV}")
    rows = load_tracker()
    pending = [r for r in rows if r['status'] == 'pending']
    completed = [r for r in rows if r['status'] == 'completed']
    
    log_message(f"✅ {len(rows)} PDFs total")
    log_message(f"   {len(pending)} pending")
    log_message(f"   {len(completed)} already completed")
    
    if not pending:
        log_message("\n✨ All PDFs already converted!")
        return
    
    # Select model
    model = MODELS[0]
    log_message(f"\n🤖 Using model: {model['name']}")
    log_message(f"   Cost: ${model['cost_per_1m_prompt']}/1M prompt, ${model['cost_per_1m_completion']}/1M completion tokens")
    
    # Calculate progress tracking
    total_to_process = len(pending)
    processed_count = 0
    
    log_message(f"\n🚀 Starting batch conversion of {total_to_process} PDFs...")
    log_message(f"📝 Real-time log: {PROCESS_LOG}\n")
    
    # Process PDFs
    for i, row in enumerate(rows, 1):
        if row['status'] != 'pending':
            continue
        
        processed_count += 1
        log_message(f"\n{'='*80}")
        log_message(f"[{processed_count}/{total_to_process}] Processing PDF {i}/{len(rows)}")
        
        updated_row = process_pdf(row, api_key, model)
        rows[rows.index(row)] = updated_row
        save_tracker(rows)
        
        # Progress summary after each PDF
        if updated_row['status'] == 'completed':
            log_message(f"✅ SUCCESS: {updated_row['filename']}")
        else:
            log_message(f"⚠️  ISSUE: {updated_row['filename']} - {updated_row['notes']}")
        
        # Delay between PDFs to avoid rate limits
        if processed_count < total_to_process:
            delay = 5  # 5 seconds between PDFs
            log_message(f"⏳ Waiting {delay}s before next PDF...")
            time.sleep(delay)
    
    # Final summary
    log_message("\n" + "="*80)
    log_message("✨ BATCH CONVERSION COMPLETE!")
    log_message("="*80)
    
    completed = [r for r in rows if r['status'] == 'completed']
    errors = [r for r in rows if r['status'] == 'error']
    total_cost = sum(float(r['total_cost_usd']) for r in completed if r['total_cost_usd'])
    
    log_message(f"\n📊 Final Statistics:")
    log_message(f"   Total PDFs: {len(rows)}")
    log_message(f"   ✅ Completed: {len(completed)}")
    log_message(f"   ❌ Errors: {len(errors)}")
    log_message(f"   💰 Total cost: ${total_cost:.6f}")
    
    if errors:
        log_message(f"\n⚠️  PDFs with errors:")
        for err_row in errors:
            log_message(f"   - {err_row['filename']}: {err_row['notes']}")
    
    log_message(f"\n📝 Full log saved to: {PROCESS_LOG}")
    log_message(f"📊 Tracker updated: {TRACKER_CSV}")
    log_message("="*80)


if __name__ == "__main__":
    main()

