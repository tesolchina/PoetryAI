import asyncio
import aiohttp
import json
from typing import Dict, List, Optional, AsyncGenerator
from dataclasses import dataclass
from config.config import Config

@dataclass
class ChatMessage:
    """Represents a chat message with role and content"""
    role: str  # 'system', 'user', or 'assistant'
    content: str

class OpenRouterClient:
    """Client for interacting with OpenRouter API"""
    
    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key or Config.OPENROUTER_API_KEY
        self.base_url = base_url or Config.OPENROUTER_BASE_URL
        
        if not self.api_key:
            raise ValueError("API key is required")
    
    async def create_completion(
        self, 
        messages: List[ChatMessage], 
        model: str = None,
        temperature: float = None,
        max_tokens: int = None,
        stream: bool = False
    ) -> Dict:
        """Create a chat completion using OpenRouter API"""
        
        model = model or Config.DEFAULT_MODEL
        temperature = temperature or Config.TEMPERATURE
        max_tokens = max_tokens or Config.MAX_TOKENS
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": Config.HTTP_REFERER,
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": [{"role": msg.role, "content": msg.content} for msg in messages],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data
            ) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"API request failed: {response.status} - {error_text}")
    
    async def stream_completion(
        self, 
        messages: List[ChatMessage], 
        model: str = None,
        temperature: float = None,
        max_tokens: int = None
    ) -> AsyncGenerator[str, None]:
        """Stream a chat completion using OpenRouter API"""
        
        model = model or Config.DEFAULT_MODEL
        temperature = temperature or Config.TEMPERATURE
        max_tokens = max_tokens or Config.MAX_TOKENS
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": Config.HTTP_REFERER,
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": [{"role": msg.role, "content": msg.content} for msg in messages],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"API request failed: {response.status} - {error_text}")
                
                async for line in response.content:
                    line = line.decode('utf-8').strip()
                    if line.startswith('data: '):
                        chunk_data = line[6:]
                        if chunk_data == '[DONE]':
                            break
                        try:
                            chunk = json.loads(chunk_data)
                            if 'choices' in chunk and len(chunk['choices']) > 0:
                                delta = chunk['choices'][0].get('delta', {})
                                if 'content' in delta:
                                    yield delta['content']
                        except json.JSONDecodeError:
                            continue
