import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for OpenRouter API and chatbot settings"""
    
    # OpenRouter API Configuration
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
    OPENROUTER_BASE_URL = os.getenv('OPENROUTER_BASE_URL', 'https://openrouter.ai/api/v1')
    HTTP_REFERER = os.getenv('HTTP_REFERER', 'http://localhost:3000')
    
    # Model Settings
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'meta-llama/llama-3.1-8b-instruct:free')
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 2048))
    
    # Chatbot Settings
    CHATBOT_NAME = os.getenv('CHATBOT_NAME', 'MyCustomBot')
    SYSTEM_PROMPT = os.getenv('SYSTEM_PROMPT', 'You are a helpful AI assistant.')
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present"""
        if not cls.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY must be set in environment variables")
        return True

# Available models on OpenRouter (free and paid options)
AVAILABLE_MODELS = {
    'free': [
        'meta-llama/llama-3.1-8b-instruct:free',
        'microsoft/phi-3-mini-128k-instruct:free',
        'google/gemma-2-9b-it:free',
    ],
    'paid': [
        'openai/gpt-4o',
        'openai/gpt-4o-mini',
        'anthropic/claude-3.5-sonnet',
        'google/gemini-pro-1.5',
        'meta-llama/llama-3.1-70b-instruct',
        'mistralai/mixtral-8x7b-instruct',
    ]
}