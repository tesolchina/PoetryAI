#!/usr/bin/env python3
"""
PDF to Markdown Converter using OpenRouter API
Processes PDFs page-by-page and tracks progress/costs in CSV
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

# Model selection (ordered by preference: cheapest paid models)
MODELS = [
    {
        "id": "amazon/nova-lite-v1",
        "name": "Amazon Nova Lite",
        "cost_per_1m_prompt": 0.06,
        "cost_per_1m_completion": 0.24,
    },
    {
        "id": "google/gemini-2.0-flash-001",
        "name": "Google Gemini 2.0 Flash",
        "cost_per_1m_prompt": 0.10,
        "cost_per_1m_completion": 0.40,
    },
    {
        "id": "deepseek/deepseek-chat-v3.1",
        "name": "DeepSeek V3.1",
        "cost_per_1m_prompt": 0.20,
        "cost_per_1m_completion": 0.80,
    },
]

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


def load_api_key():
    """Load OpenRouter API key from file"""
    try:
        with open(API_KEY_FILE, 'r') as f:
            api_key = f.read().strip()
        print(f"✅ API key loaded from {API_KEY_FILE}")
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
    print(f"💾 Tracker CSV updated")


def extract_pdf_text_pypdf2(pdf_path):
    """Extract text from PDF using PyPDF2"""
    try:
        import PyPDF2
        
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = len(reader.pages)
            
            pages_text = []
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                pages_text.append({
                    'page_num': page_num + 1,
                    'text': text
                })
            
            return pages_text, num_pages
    except ImportError:
        print("⚠️  PyPDF2 not installed. Install with: pip install PyPDF2")
        return None, 0
    except Exception as e:
        print(f"❌ Error extracting PDF text: {e}")
        return None, 0


def extract_pdf_text_pdfplumber(pdf_path):
    """Extract text from PDF using pdfplumber (better quality)"""
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
    except ImportError:
        print("⚠️  pdfplumber not installed. Falling back to PyPDF2...")
        return extract_pdf_text_pypdf2(pdf_path)
    except Exception as e:
        print(f"❌ Error extracting PDF with pdfplumber: {e}")
        return extract_pdf_text_pypdf2(pdf_path)


def convert_page_to_markdown(page_text, page_num, model, api_key, max_retries=3):
    """Convert a single page of text to markdown using OpenRouter API with retry logic"""
    
    prompt = f"""Convert the following academic paper text from page {page_num} into clean, well-formatted markdown.

Requirements:
- Preserve all headings, converting them to proper markdown headers (# ## ###)
- Preserve citations and references in their original format
- Format lists, tables, and code blocks appropriately
- Keep mathematical notation if present
- Remove any OCR artifacts or formatting errors
- Do NOT add any commentary or explanations
- Output ONLY the markdown content

Page {page_num} text:
---
{page_text}
---

Markdown output:"""

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/simonwang/AIpoetry",
    }
    
    data = {
        "model": model["id"],
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3,  # Lower temperature for consistent formatting
    }
    
    # Retry logic with exponential backoff
    for attempt in range(max_retries):
        try:
            response = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            
            # Extract markdown content
            markdown = result['choices'][0]['message']['content']
            
            # Extract token usage
            usage = result.get('usage', {})
            prompt_tokens = usage.get('prompt_tokens', 0)
            completion_tokens = usage.get('completion_tokens', 0)
            
            return markdown, prompt_tokens, completion_tokens, None
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Rate limit
                wait_time = (2 ** attempt) * 2  # Exponential backoff: 2, 4, 8 seconds
                print(f"\n⚠️  Rate limit hit. Waiting {wait_time}s before retry {attempt+1}/{max_retries}...", end="", flush=True)
                time.sleep(wait_time)
                continue
            else:
                return None, 0, 0, f"API HTTP error: {e}"
        except requests.exceptions.RequestException as e:
            return None, 0, 0, f"API request failed: {e}"
        except Exception as e:
            return None, 0, 0, f"Error: {e}"
    
    return None, 0, 0, "Max retries exceeded due to rate limiting"


def process_pdf(row, api_key, model):
    """Process a single PDF file"""
    pdf_path = LITERATURE_DIR / row['relative_path']
    output_path = LITERATURE_DIR / row['output_md_path']
    
    print(f"\n{'='*80}")
    print(f"📄 Processing: {row['filename']}")
    print(f"   Category: {row['category']}")
    print(f"   Model: {model['name']}")
    print(f"{'='*80}")
    
    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        row['status'] = 'error'
        row['notes'] = 'PDF file not found'
        return row
    
    # Update status to processing
    row['status'] = 'processing'
    
    # Extract PDF text
    print("📖 Extracting text from PDF...")
    pages_text, num_pages = extract_pdf_text_pdfplumber(pdf_path)
    
    if not pages_text:
        print("❌ Failed to extract PDF text")
        row['status'] = 'error'
        row['notes'] = 'Failed to extract text from PDF'
        return row
    
    print(f"✅ Extracted {num_pages} pages")
    row['page_count'] = str(num_pages)
    
    # Process pages
    total_prompt_tokens = 0
    total_completion_tokens = 0
    all_markdown = []
    
    for i, page_data in enumerate(pages_text, 1):
        print(f"  🔄 Converting page {i}/{num_pages}...", end=" ", flush=True)
        
        markdown, prompt_tokens, completion_tokens, error = convert_page_to_markdown(
            page_data['text'],
            page_data['page_num'],
            model,
            api_key
        )
        
        if error:
            print(f"❌ {error}")
            row['status'] = 'error'
            row['notes'] = f'Failed at page {i}: {error}'
            return row
        
        total_prompt_tokens += prompt_tokens
        total_completion_tokens += completion_tokens
        
        all_markdown.append(markdown)
        print(f"✅ ({prompt_tokens} + {completion_tokens} tokens)")
        
        # Rate limiting: small delay between requests
        if i < num_pages:
            time.sleep(1)  # 1 second for paid tier
    
    # Calculate cost
    total_cost = (
        (total_prompt_tokens / 1_000_000) * model['cost_per_1m_prompt'] +
        (total_completion_tokens / 1_000_000) * model['cost_per_1m_completion']
    )
    
    # Combine all pages
    combined_markdown = "\n\n---\n\n".join(all_markdown)
    
    # Add metadata header
    metadata = f"""---
source_pdf: {row['filename']}
converted_date: {datetime.now().isoformat()}
total_pages: {num_pages}
model: {model['name']}
total_cost: ${total_cost:.6f}
---

"""
    
    final_markdown = metadata + combined_markdown
    
    # Save markdown file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_markdown)
    
    print(f"\n✅ Markdown saved to: {output_path}")
    print(f"💰 Total cost: ${total_cost:.6f}")
    print(f"📊 Tokens: {total_prompt_tokens:,} prompt + {total_completion_tokens:,} completion")
    
    # Update row
    row['status'] = 'completed'
    row['model_used'] = model['name']
    row['prompt_tokens'] = str(total_prompt_tokens)
    row['completion_tokens'] = str(total_completion_tokens)
    row['total_cost_usd'] = f"{total_cost:.6f}"
    row['date_processed'] = datetime.now().isoformat()
    row['notes'] = 'Successfully converted'
    
    return row


def main():
    """Main execution function"""
    print("="*80)
    print("PDF to Markdown Converter")
    print("="*80)
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        print("❌ Cannot proceed without API key")
        return
    
    # Load tracker
    print(f"\n📋 Loading tracker from {TRACKER_CSV}")
    rows = load_tracker()
    print(f"✅ Loaded {len(rows)} PDFs")
    
    # Count pending
    pending = [r for r in rows if r['status'] == 'pending']
    print(f"📊 Status: {len(pending)} pending, {len([r for r in rows if r['status'] == 'completed'])} completed")
    
    if not pending:
        print("\n✨ All PDFs already processed!")
        return
    
    # Select model (use first available, which is free)
    model = MODELS[0]
    print(f"\n🤖 Using model: {model['name']}")
    
    # Process PDFs
    print(f"\n🚀 Starting conversion of {len(pending)} PDFs...")
    
    for i, row in enumerate(rows):
        if row['status'] != 'pending':
            continue
        
        print(f"\n[{i+1}/{len(rows)}] ", end="")
        
        # Process PDF
        updated_row = process_pdf(row, api_key, model)
        
        # Update the row in place
        rows[rows.index(row)] = updated_row
        
        # Save tracker after each PDF
        save_tracker(rows)
        
        # Small delay between PDFs
        time.sleep(1)
    
    print("\n" + "="*80)
    print("✨ Conversion complete!")
    print("="*80)
    
    # Print summary
    completed = [r for r in rows if r['status'] == 'completed']
    total_cost = sum(float(r['total_cost_usd']) for r in completed if r['total_cost_usd'])
    
    print(f"\n📊 Summary:")
    print(f"   Total PDFs: {len(rows)}")
    print(f"   Completed: {len(completed)}")
    print(f"   Total cost: ${total_cost:.6f}")


if __name__ == "__main__":
    main()

