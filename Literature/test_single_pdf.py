#!/usr/bin/env python3
"""
Test script to convert a single PDF to verify quality before batch processing
"""

import csv
from pathlib import Path
from pdf_to_markdown_converter import (
    load_api_key, load_tracker, save_tracker, 
    process_pdf, MODELS, TRACKER_CSV
)

def test_single_pdf():
    """Test conversion on a single PDF"""
    print("="*80)
    print("TEST: Single PDF Conversion")
    print("="*80)
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        print("❌ Cannot proceed without API key")
        return
    
    # Load tracker
    rows = load_tracker()
    
    # Find a small PDF from root to test (Park.pdf is likely smaller)
    test_row = None
    for row in rows:
        if row['filename'] == 'Park.pdf' and row['status'] == 'pending':
            test_row = row
            break
    
    if not test_row:
        # Try another small one
        for row in rows:
            if row['status'] == 'pending':
                test_row = row
                break
    
    if not test_row:
        print("❌ No pending PDFs found to test")
        return
    
    print(f"\n🧪 Testing with: {test_row['filename']}")
    print(f"   Category: {test_row['category']}")
    print(f"   Model: {MODELS[0]['name']}")
    
    # Ask for confirmation
    response = input("\n▶️  Proceed with test conversion? (y/n): ")
    if response.lower() != 'y':
        print("❌ Test cancelled")
        return
    
    # Process the PDF
    updated_row = process_pdf(test_row, api_key, MODELS[0])
    
    # Update tracker
    for i, row in enumerate(rows):
        if row['id'] == updated_row['id']:
            rows[i] = updated_row
            break
    
    save_tracker(rows)
    
    print("\n" + "="*80)
    print("✅ TEST COMPLETE!")
    print("="*80)
    print(f"\n📄 Check the output file:")
    print(f"   {test_row['output_md_path']}")
    print(f"\n💡 Review the markdown quality before proceeding with batch conversion.")
    print(f"   If satisfied, run: python3 pdf_to_markdown_converter.py")

if __name__ == "__main__":
    test_single_pdf()



