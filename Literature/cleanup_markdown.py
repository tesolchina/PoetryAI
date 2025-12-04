#!/usr/bin/env python3
"""
Cleanup script for markdown files:
- Fix hyphenated words split across lines
- Remove excessive line breaks within paragraphs
- Preserve headers, lists, and formatting
"""

import re
from pathlib import Path

LITERATURE_DIR = Path(__file__).parent
MD_DIR = LITERATURE_DIR / "md"


def cleanup_markdown(text):
    """Clean up markdown text"""
    
    # Split into lines
    lines = text.split('\n')
    cleaned_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Skip metadata block at start
        if i < 20 and (line.startswith('---') or ':' in line[:50]):
            cleaned_lines.append(line)
            i += 1
            continue
        
        # Preserve headers
        if line.startswith('#'):
            cleaned_lines.append(line)
            i += 1
            continue
        
        # Preserve lists
        if re.match(r'^\s*[-*+\d]+[\.\)]\s', line):
            cleaned_lines.append(line)
            i += 1
            continue
        
        # Preserve block quotes
        if line.startswith('>'):
            cleaned_lines.append(line)
            i += 1
            continue
        
        # Preserve code blocks
        if line.startswith('```') or line.startswith('    '):
            cleaned_lines.append(line)
            i += 1
            continue
        
        # Preserve blank lines (but consolidate multiple blanks)
        if not line.strip():
            # Only add blank line if previous wasn't blank
            if cleaned_lines and cleaned_lines[-1].strip():
                cleaned_lines.append('')
            i += 1
            continue
        
        # Fix hyphenated words split across lines
        if line.rstrip().endswith('-') and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            # Check if next line starts with lowercase (continuation)
            if next_line and next_line[0].islower():
                # Join the hyphenated word
                current = line.rstrip()[:-1]  # Remove hyphen
                combined = current + next_line
                cleaned_lines.append(combined)
                i += 2
                continue
        
        # Join lines within paragraphs (lines that don't end with sentence-ending punctuation)
        # But preserve intentional line breaks before headers, lists, etc.
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            
            # If current line doesn't end with sentence-ending punctuation
            # and next line exists and isn't special formatting
            if (not re.search(r'[.!?:"]$', line.rstrip()) and 
                next_line and
                not next_line.startswith('#') and
                not next_line.startswith('>') and
                not next_line.startswith('```') and
                not re.match(r'^\s*[-*+\d]+[\.\)]\s', next_line) and
                not next_line.startswith('**') and  # Not bold header
                next_line[0].islower()):  # Continues with lowercase
                
                # Join with next line
                cleaned_lines.append(line.rstrip() + ' ' + next_line)
                i += 2
                continue
        
        # Default: keep the line as is
        cleaned_lines.append(line)
        i += 1
    
    # Join lines and clean up excessive blank lines
    result = '\n'.join(cleaned_lines)
    
    # Replace 3+ consecutive newlines with just 2
    result = re.sub(r'\n{3,}', '\n\n', result)
    
    return result


def process_all_md_files():
    """Process all markdown files in md directory"""
    
    print("="*60)
    print("Markdown Cleanup Script")
    print("="*60)
    
    # Find all .md files
    md_files = list(MD_DIR.rglob("*.md"))
    
    print(f"\nFound {len(md_files)} markdown files")
    
    cleaned_count = 0
    
    for md_file in md_files:
        print(f"\n📄 Processing: {md_file.name}")
        
        # Read original
        with open(md_file, 'r', encoding='utf-8') as f:
            original = f.read()
        
        # Cleanup
        cleaned = cleanup_markdown(original)
        
        # Check if changed
        if cleaned != original:
            # Backup original
            backup_file = md_file.with_suffix('.md.bak')
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(original)
            
            # Write cleaned version
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            
            print(f"   ✅ Cleaned (backup: {backup_file.name})")
            cleaned_count += 1
        else:
            print(f"   ⏭️  No changes needed")
    
    print(f"\n{'='*60}")
    print(f"✨ Complete!")
    print(f"   Processed: {len(md_files)} files")
    print(f"   Cleaned: {cleaned_count} files")
    print("="*60)


if __name__ == "__main__":
    process_all_md_files()

