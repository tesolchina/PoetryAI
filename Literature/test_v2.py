#!/usr/bin/env python3
"""Test V2 converter on Park.pdf"""
from pdf_to_markdown_v2 import load_api_key, load_tracker, save_tracker, process_pdf, MODELS

api_key = load_api_key()
if not api_key:
    exit(1)

rows = load_tracker()
test_row = next((r for r in rows if r['filename'] == 'Park.pdf'), None)

if not test_row:
    print("❌ Park.pdf not found in tracker")
    exit(1)

print(f"\n🧪 Testing V2 with: {test_row['filename']}")
print(f"   Model: {MODELS[0]['name']}")

response = input("\n▶️  Proceed? (y/n): ")
if response.lower() != 'y':
    exit(0)

updated_row = process_pdf(test_row, api_key, MODELS[0])

for i, row in enumerate(rows):
    if row['id'] == updated_row['id']:
        rows[i] = updated_row
        break

save_tracker(rows)

print("\n✅ TEST COMPLETE!")
print(f"📄 Check: {test_row['output_md_path']}")



