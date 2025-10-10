"""
Debug API Key Loading
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check API key
api_key = os.environ.get('OPENROUTER_API_KEY')

print("🔍 Debugging API Key Setup:")
print(f"📁 Current directory: {os.getcwd()}")
print(f"📄 .env file exists: {os.path.exists('.env')}")

if api_key:
    # Show first and last 10 characters for security
    masked_key = f"{api_key[:10]}...{api_key[-10:]}" if len(api_key) > 20 else "KEY_TOO_SHORT"
    print(f"🔑 API Key found: {masked_key}")
    print(f"📏 Key length: {len(api_key)} characters")
    print(f"🔤 Key starts with: {api_key[:15] if len(api_key) >= 15 else api_key}")
else:
    print("❌ No API Key found!")
    print("🔧 Available environment variables:")
    for key, value in os.environ.items():
        if 'OPENROUTER' in key.upper() or 'API' in key.upper():
            print(f"   {key}: {value[:20]}...")

# Check .env file contents
if os.path.exists('.env'):
    print("\n📖 .env file contents (first few lines):")
    with open('.env', 'r') as f:
        lines = f.readlines()[:5]
        for i, line in enumerate(lines, 1):
            # Mask the API key for security
            if 'OPENROUTER_API_KEY' in line:
                parts = line.split('=', 1)
                if len(parts) == 2:
                    key_part = parts[1].strip()
                    masked = f"{key_part[:15]}..." if len(key_part) > 15 else key_part
                    print(f"   Line {i}: OPENROUTER_API_KEY={masked}")
                else:
                    print(f"   Line {i}: {line.strip()}")
            else:
                print(f"   Line {i}: {line.strip()}")
else:
    print("\n❌ .env file not found in current directory")