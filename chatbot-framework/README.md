# Custom Chatbot Framework with OpenRouter API

A flexible Python framework for creating customized chatbots using OpenRouter's API. This framework allows you to easily create chatbots with different personalities, specializations, and behaviors.

## 🚀 Features

- **Easy Customization**: Create chatbots with unique personalities and traits
- **Multiple Models**: Support for various AI models through OpenRouter (free and paid)
- **Streaming Support**: Real-time response streaming for better user experience
- **Conversation Management**: Save, load, and manage conversation histories
- **Pre-built Templates**: Ready-to-use chatbot templates for common use cases
- **Async Support**: Fully asynchronous for better performance

## 📁 Project Structure

```
chatbot-framework/
├── src/
│   ├── chatbot.py              # Main chatbot class and utilities
│   ├── openrouter_client.py    # OpenRouter API client
│   └── __init__.py
├── config/
│   ├── config.py               # Configuration management
│   └── __init__.py
├── examples/
│   ├── basic_chatbot.py        # Simple chatbot example
│   ├── personality_bots.py     # Different personality demonstrations
│   └── advanced_customization.py # Advanced features showcase
├── docs/
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Create an account
3. Generate an API key from your dashboard
4. Note: OpenRouter provides access to many models, including free options

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` file with your settings:
   ```env
   # Required: Your OpenRouter API key
   OPENROUTER_API_KEY=your_actual_api_key_here
   
   # Optional: Customize these settings
   DEFAULT_MODEL=meta-llama/llama-3.1-8b-instruct:free
   TEMPERATURE=0.7
   MAX_TOKENS=2048
   CHATBOT_NAME=MyCustomBot
   ```

### 4. Test Your Setup

Run the basic example:
```bash
python examples/basic_chatbot.py
```

## 🤖 Quick Start

### Basic Usage

```python
import asyncio
from src.chatbot import CustomChatbot

async def main():
    # Create a simple chatbot
    bot = CustomChatbot(
        name="Helper",
        system_prompt="You are a helpful assistant.",
        temperature=0.7
    )
    
    # Have a conversation
    response = await bot.chat("Hello, how are you?")
    print(response)

asyncio.run(main())
```

### Creating Specialized Chatbots

```python
from src.chatbot import create_creative_writer_bot, create_coding_assistant_bot

# Pre-built specialized bots
writer_bot = create_creative_writer_bot("Maya")
coder_bot = create_coding_assistant_bot("Alex")

# Custom specialized bot
poetry_bot = CustomChatbot(
    name="PoetryMentor",
    system_prompt="You are a poetry expert and teacher.",
    personality_traits={
        "creative": True,
        "patient": True,
        "scholarly": True
    },
    custom_instructions=[
        "Always explain poetic devices when you use them",
        "Provide examples from famous poets"
    ],
    temperature=0.8
)
```

## 🎭 Personality Customization

### Personality Traits

You can define personality traits as a dictionary:

```python
personality_traits = {
    "friendly": True,
    "professional": True,
    "humor_level": "witty",
    "expertise": "expert",
    "communication_style": "casual",
    "patience": "very high"
}
```

### Custom Instructions

Add specific behavioral instructions:

```python
custom_instructions = [
    "Always ask follow-up questions",
    "Provide examples with explanations",
    "Be encouraging and supportive",
    "Use simple language when explaining complex topics"
]
```

### Dynamic Personality Updates

```python
# Update personality during runtime
bot.update_personality({"more_creative": True, "energy_level": "high"})
bot.add_custom_instruction("Use more metaphors and analogies")
```

## 🔧 Advanced Features

### Streaming Responses

```python
# Enable streaming for real-time responses
response = await bot.chat("Tell me a story", stream=True)
```

### Model Selection

```python
# Use different models for different purposes
bot.set_model("openai/gpt-4o-mini")  # Paid model for better responses
bot.set_model("meta-llama/llama-3.1-8b-instruct:free")  # Free model
```

### Conversation Management

```python
# Save conversation
bot.save_conversation("my_chat_session.json")

# Clear history
bot.clear_history()

# Get conversation history
history = bot.get_conversation_history()
```

### Temperature Control

```python
# Adjust creativity/randomness
bot.set_temperature(0.3)  # More focused and deterministic
bot.set_temperature(0.9)  # More creative and varied
```

## 📚 Available Models

### Free Models
- `meta-llama/llama-3.1-8b-instruct:free`
- `microsoft/phi-3-mini-128k-instruct:free`
- `google/gemma-2-9b-it:free`

### Paid Models (Examples)
- `openai/gpt-4o`
- `openai/gpt-4o-mini`
- `anthropic/claude-3.5-sonnet`
- `google/gemini-pro-1.5`

## 💡 Example Use Cases

### 1. Creative Writing Assistant
```python
writer_bot = create_creative_writer_bot()
await writer_bot.chat("Help me write a sci-fi story about time travel")
```

### 2. Coding Helper
```python
coder_bot = create_coding_assistant_bot()
await coder_bot.chat("How do I implement a binary search in Python?")
```

### 3. Study Buddy
```python
study_bot = CustomChatbot(
    name="StudyBuddy",
    system_prompt="You are a patient tutor who helps students learn.",
    personality_traits={"patient": True, "encouraging": True},
    temperature=0.6
)
```

### 4. Business Advisor
```python
business_bot = CustomChatbot(
    name="BizAdvisor", 
    system_prompt="You are a business consultant.",
    personality_traits={"analytical": True, "strategic": True},
    temperature=0.4
)
```

## 🔍 Running Examples

### Basic Chatbot
```bash
python examples/basic_chatbot.py
```
Interactive chat session with a simple bot.

### Personality Demonstration
```bash
python examples/personality_bots.py
```
See how different personalities respond to the same question.

### Advanced Features
```bash
python examples/advanced_customization.py
```
Demonstrates dynamic personality updates and specialized bots.

## ⚙️ Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key | Required |
| `OPENROUTER_BASE_URL` | API base URL | `https://openrouter.ai/api/v1` |
| `DEFAULT_MODEL` | Default AI model | `meta-llama/llama-3.1-8b-instruct:free` |
| `TEMPERATURE` | Response creativity (0.0-2.0) | `0.7` |
| `MAX_TOKENS` | Maximum response length | `2048` |
| `CHATBOT_NAME` | Default chatbot name | `MyCustomBot` |
| `HTTP_REFERER` | Referer header for API calls | `http://localhost:3000` |

### Chatbot Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | str | Chatbot's name |
| `system_prompt` | str | Core personality/role description |
| `model` | str | AI model to use |
| `temperature` | float | Creativity level (0.0-2.0) |
| `max_tokens` | int | Maximum response length |
| `personality_traits` | dict | Personality characteristics |
| `custom_instructions` | list | Specific behavioral rules |

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   Configuration error: OPENROUTER_API_KEY must be set
   ```
   **Solution**: Set your API key in the `.env` file

2. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'src'
   ```
   **Solution**: Run scripts from the project root directory

3. **Rate Limiting**
   ```
   API request failed: 429 - Too Many Requests
   ```
   **Solution**: Wait a moment or upgrade to a paid OpenRouter plan

4. **Model Not Found**
   ```
   API request failed: 400 - Model not found
   ```
   **Solution**: Check available models in `config/config.py`

### Getting Help

- Check the examples in the `examples/` directory
- Review the configuration in `config/config.py`
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify your API key is valid and has sufficient credits

## 🚀 Next Steps

1. **Experiment with Examples**: Run all example scripts to understand the framework
2. **Create Your Own Bot**: Use the templates to build specialized chatbots
3. **Customize Personalities**: Experiment with different personality traits
4. **Try Different Models**: Test various models for different use cases
5. **Build Applications**: Integrate the framework into larger applications

## 📋 API Reference

### CustomChatbot Class

```python
class CustomChatbot:
    def __init__(self, name=None, system_prompt=None, model=None, 
                 temperature=None, max_tokens=None, personality_traits=None, 
                 custom_instructions=None)
    
    async def chat(self, user_message: str, stream: bool = False) -> str
    def clear_history(self, keep_system: bool = True)
    def save_conversation(self, filename: str)
    def update_personality(self, new_traits: Dict)
    def add_custom_instruction(self, instruction: str)
    def set_model(self, model: str)
    def set_temperature(self, temperature: float)
```

### Utility Functions

```python
def create_creative_writer_bot(name: str = "CreativeWriter") -> CustomChatbot
def create_coding_assistant_bot(name: str = "CodeHelper") -> CustomChatbot  
def create_friendly_companion_bot(name: str = "Buddy") -> CustomChatbot
```

## 📄 License

This project is open source. Feel free to modify and distribute according to your needs.

---

**Happy Chatbot Building! 🤖✨**