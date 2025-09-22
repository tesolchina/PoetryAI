import asyncio
from typing import List, Dict, Optional, Callable
from datetime import datetime
from .openrouter_client import OpenRouterClient, ChatMessage
from config.config import Config
import json

class CustomChatbot:
    """
    A customizable chatbot class that uses OpenRouter API
    """
    
    def __init__(
        self,
        name: str = None,
        system_prompt: str = None,
        model: str = None,
        temperature: float = None,
        max_tokens: int = None,
        personality_traits: Dict = None,
        custom_instructions: List[str] = None
    ):
        self.name = name or Config.CHATBOT_NAME
        self.system_prompt = system_prompt or Config.SYSTEM_PROMPT
        self.model = model or Config.DEFAULT_MODEL
        self.temperature = temperature or Config.TEMPERATURE
        self.max_tokens = max_tokens or Config.MAX_TOKENS
        
        # Personality and customization
        self.personality_traits = personality_traits or {}
        self.custom_instructions = custom_instructions or []
        
        # Chat history
        self.conversation_history: List[ChatMessage] = []
        
        # Initialize client
        self.client = OpenRouterClient()
        
        # Set initial system message
        self._setup_system_message()
    
    def _setup_system_message(self):
        """Setup the initial system message with personality and instructions"""
        system_content = self.system_prompt
        
        # Add personality traits
        if self.personality_traits:
            personality_text = self._format_personality()
            system_content += f"\n\nPersonality traits: {personality_text}"
        
        # Add custom instructions
        if self.custom_instructions:
            instructions_text = "\n".join(f"- {instruction}" for instruction in self.custom_instructions)
            system_content += f"\n\nAdditional instructions:\n{instructions_text}"
        
        # Add chatbot name
        system_content += f"\n\nYour name is {self.name}."
        
        self.conversation_history = [ChatMessage(role="system", content=system_content)]
    
    def _format_personality(self) -> str:
        """Format personality traits into readable text"""
        traits = []
        for trait, value in self.personality_traits.items():
            if isinstance(value, bool):
                if value:
                    traits.append(trait.replace("_", " "))
            else:
                traits.append(f"{trait.replace('_', ' ')}: {value}")
        return ", ".join(traits)
    
    async def chat(self, user_message: str, stream: bool = False) -> str:
        """
        Send a message to the chatbot and get a response
        """
        # Add user message to history
        self.conversation_history.append(ChatMessage(role="user", content=user_message))
        
        try:
            if stream:
                return await self._stream_response()
            else:
                return await self._get_response()
        except Exception as e:
            error_msg = f"Error getting response: {str(e)}"
            print(error_msg)
            return error_msg
    
    async def _get_response(self) -> str:
        """Get a complete response from the API"""
        response = await self.client.create_completion(
            messages=self.conversation_history,
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        assistant_message = response['choices'][0]['message']['content']
        
        # Add assistant response to history
        self.conversation_history.append(ChatMessage(role="assistant", content=assistant_message))
        
        return assistant_message
    
    async def _stream_response(self) -> str:
        """Get a streamed response from the API"""
        full_response = ""
        
        async for chunk in self.client.stream_completion(
            messages=self.conversation_history,
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        ):
            full_response += chunk
            print(chunk, end="", flush=True)
        
        # Add assistant response to history
        self.conversation_history.append(ChatMessage(role="assistant", content=full_response))
        
        return full_response
    
    def clear_history(self, keep_system: bool = True):
        """Clear conversation history"""
        if keep_system:
            # Keep only the system message
            self.conversation_history = [msg for msg in self.conversation_history if msg.role == "system"]
        else:
            self.conversation_history = []
            self._setup_system_message()
    
    def get_conversation_history(self) -> List[Dict]:
        """Get conversation history as a list of dictionaries"""
        return [{"role": msg.role, "content": msg.content, "timestamp": datetime.now().isoformat()} 
                for msg in self.conversation_history if msg.role != "system"]
    
    def save_conversation(self, filename: str):
        """Save conversation history to a JSON file"""
        history = self.get_conversation_history()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                "chatbot_name": self.name,
                "model": self.model,
                "conversation": history
            }, f, indent=2, ensure_ascii=False)
    
    def update_personality(self, new_traits: Dict):
        """Update personality traits and refresh system message"""
        self.personality_traits.update(new_traits)
        self._setup_system_message()
    
    def add_custom_instruction(self, instruction: str):
        """Add a new custom instruction"""
        self.custom_instructions.append(instruction)
        self._setup_system_message()
    
    def set_model(self, model: str):
        """Change the model being used"""
        self.model = model
    
    def set_temperature(self, temperature: float):
        """Change the temperature (creativity) setting"""
        self.temperature = max(0.0, min(2.0, temperature))

# Utility functions for creating specialized chatbots

def create_creative_writer_bot(name: str = "CreativeWriter") -> CustomChatbot:
    """Create a chatbot specialized for creative writing"""
    return CustomChatbot(
        name=name,
        system_prompt="You are a creative writing assistant. Help users with storytelling, character development, plot ideas, and creative writing techniques.",
        personality_traits={
            "creative": True,
            "imaginative": True,
            "encouraging": True,
            "detail_oriented": True
        },
        custom_instructions=[
            "Always provide specific, actionable advice",
            "Ask follow-up questions to understand the user's vision",
            "Offer multiple creative alternatives when possible",
            "Be encouraging and supportive of creative endeavors"
        ],
        temperature=0.8
    )

def create_coding_assistant_bot(name: str = "CodeHelper") -> CustomChatbot:
    """Create a chatbot specialized for coding assistance"""
    return CustomChatbot(
        name=name,
        system_prompt="You are a programming assistant. Help users with code, debugging, best practices, and technical problems.",
        personality_traits={
            "analytical": True,
            "precise": True,
            "helpful": True,
            "patient": True
        },
        custom_instructions=[
            "Always provide working code examples when possible",
            "Explain your reasoning and approach",
            "Suggest best practices and optimizations",
            "Ask clarifying questions about requirements"
        ],
        temperature=0.3
    )

def create_friendly_companion_bot(name: str = "Buddy") -> CustomChatbot:
    """Create a chatbot for casual conversation and emotional support"""
    return CustomChatbot(
        name=name,
        system_prompt="You are a friendly, empathetic companion. Engage in meaningful conversations and provide emotional support.",
        personality_traits={
            "friendly": True,
            "empathetic": True,
            "optimistic": True,
            "good_listener": True
        },
        custom_instructions=[
            "Always be supportive and understanding",
            "Ask about the user's feelings and experiences",
            "Share appropriate personal anecdotes when helpful",
            "Maintain a positive but realistic outlook"
        ],
        temperature=0.7
    )