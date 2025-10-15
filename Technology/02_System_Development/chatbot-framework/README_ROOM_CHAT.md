# PoetryAI Room Chat System

A comprehensive chat system implementing the four experimental conditions for L2 poetry writing research.

## 🏠 Room Structure

### Room Configurations
- **Room 1**: Structured + Aware (Temperature: 0.3, Top-p: 0.4, Parameter visibility: ON)
- **Room 2**: Structured + Unaware (Temperature: 0.3, Top-p: 0.4, Parameter visibility: OFF)  
- **Room 3**: Exploratory + Aware (Temperature: 0.8, Top-p: 0.9, Parameter visibility: ON)
- **Room 4**: Exploratory + Unaware (Temperature: 0.8, Top-p: 0.9, Parameter visibility: OFF)

### Universal System Prompt
All rooms use the identical system prompt to ensure experimental validity:
- Poetry writing assistance for L2 learners (CEFR B1-B2)
- Three interaction types: Constraint Repair, Content Enhancement, Surprise Harvest
- Response guidelines: 40-80 words, encouraging tone, cultural sensitivity

## 🚀 Getting Started

### Prerequisites
```bash
pip install flask python-dotenv openai requests asyncio
```

### Environment Setup
1. Copy `.env.example` to `.env`
2. Add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
DEFAULT_MODEL=google/gemma-2-9b-it:free
```

### Running the System

#### Option 1: Web Interface (Recommended)
```bash
python room_chat_web.py
```
Then visit: http://localhost:5000

#### Option 2: Command Line Demo
```bash
python room_chat_demo.py
```

#### Option 3: Programmatic Usage
```python
from room_chat import create_room_2
import asyncio

async def example():
    room = create_room_2()  # Structured + Unaware
    
    # Start session
    welcome = room.start_session("participant_001")
    print(welcome)
    
    # Chat
    response = await room.send_message("I want to write a haiku about rain")
    print(response)
    
    # End session
    summary = room.end_session("Session completed")
    print(summary)

asyncio.run(example())
```

## 📊 Data Collection Features

### Automatic Logging
- **Individual Interactions**: Logged to `{room_type}_interactions.jsonl`
- **Complete Sessions**: Saved as `session_{session_id}.json`
- **Interaction Classification**: Automatic Type A/B/C classification
- **Metadata Tracking**: Timestamps, room parameters, participant IDs

### Data Export
```python
# Export all room data
export_file = room.export_room_data()
print(f"Data exported to: {export_file}")
```

### Session Summary Format
```json
{
  "session_id": "uuid-string",
  "room_type": "room_2_structured_unaware", 
  "participant_id": "participant_001",
  "total_interactions": 8,
  "duration_minutes": 15.5,
  "interaction_type_counts": {
    "type_a_diagnosis_repair": 3,
    "type_b_exemplar_pivot": 2, 
    "type_c_surprise_harvest": 3
  },
  "room_parameters": {
    "temperature": 0.3,
    "top_p": 0.4,
    "is_aware": false
  }
}
```

## 🔬 Research Features

### Three Interaction Types
The system automatically classifies interactions based on user messages:

#### Type A: Diagnosis → Repair
**Triggers**: "help", "wrong", "error", "fix", "correct", "syllable", "grammar"
**Example**: "Help me count syllables in 'gentle rain falls'"

#### Type B: Exemplar Pivot  
**Triggers**: "example", "show me", "like", "similar", "template"
**Example**: "Can you show me an example of a good haiku?"

#### Type C: Surprise Harvest
**Triggers**: "stuck", "idea", "inspire", "creative", "different", "new"
**Example**: "I'm stuck and need creative ideas for nature poetry"

### Parameter Effects
The system demonstrates different behaviors based on parameter settings:

**Structured Conditions (0.3/0.4)**:
- Systematic, step-by-step explanations
- Consistent vocabulary suggestions
- Rule-based guidance
- Methodical scaffolding

**Exploratory Conditions (0.8/0.9)**:
- Creative, metaphorical language
- Varied vocabulary suggestions  
- Imaginative connections
- Adaptive, discovery-based guidance

## 📁 File Structure

```
chatbot-framework/
├── room_chat.py              # Main room chat system
├── room_chat_demo.py         # Command line demo
├── room_chat_web.py          # Web interface
├── src/
│   ├── chatbot.py           # Base chatbot class
│   └── openrouter_client.py # API client
├── config/
│   └── config.py           # Configuration settings
├── templates/              # Web interface templates
├── chat_data/             # Generated data files
│   ├── session_*.json     # Individual session files
│   └── *_interactions.jsonl # Raw interaction logs
└── README_ROOM_CHAT.md   # This file
```

## 🎯 Usage Examples

### Research Session Workflow
```python
# 1. Create room instance
room = create_room_2()  # or room_1, room_3, room_4

# 2. Start session with participant ID
welcome_msg = room.start_session("P001")

# 3. Conduct conversation
response1 = await room.send_message("I want to write about nature")
response2 = await room.send_message("Help me with haiku structure")
response3 = await room.send_message("Can you give me an example?")

# 4. End session with notes
summary = room.end_session("Participant engaged well, 20 minutes")

# 5. Export data
export_file = room.export_room_data()
```

### Batch Testing Multiple Rooms
```python
async def compare_rooms():
    test_message = "Help me write a haiku about rain"
    
    for room_name, room_creator in [
        ("Structured", create_room_2),
        ("Exploratory", create_room_4)
    ]:
        room = room_creator()
        room.start_session(f"test_{room_name.lower()}")
        response = await room.send_message(test_message)
        
        print(f"{room_name}: {response}")
        
        summary = room.end_session("Comparison test")
        print(f"Interactions: {summary['total_interactions']}")
```

## 🔧 Advanced Configuration

### Custom Interaction Classification
```python
# Override the _classify_interaction method for custom logic
class CustomRoomChat(PoetryRoomChat):
    def _classify_interaction(self, user_message, bot_response):
        # Custom classification logic here
        return InteractionType.TYPE_A_DIAGNOSIS_REPAIR
```

### Additional Metadata
```python
# Add custom metadata to interactions
interaction.custom_metadata = {
    "poem_type": "haiku",
    "difficulty_level": "beginner",
    "session_phase": "warm_up"
}
```

### Data Analysis Integration
```python
import pandas as pd

# Load interaction data for analysis
def load_room_data(room_type):
    interactions = []
    log_file = f"chat_data/{room_type}_interactions.jsonl"
    
    with open(log_file, 'r') as f:
        for line in f:
            interactions.append(json.loads(line))
    
    return pd.DataFrame(interactions)

# Analyze interaction patterns
df = load_room_data("room_2_structured_unaware")
interaction_counts = df['interaction_type'].value_counts()
```

## 🧪 Testing & Validation

### Unit Tests
```bash
python -m pytest room_chat_test.py  # (create this file)
```

### Integration Tests
```bash
python room_chat_demo.py  # Automated comparison mode
```

### Data Quality Checks
- Verify interaction logging accuracy
- Validate parameter settings consistency
- Check session data completeness
- Confirm interaction type classification reliability

## 🔒 Privacy & Ethics

### Data Protection
- Automatic participant ID anonymization
- Secure local file storage
- No external data transmission (except API calls)
- Session data export control

### Research Ethics
- Clear consent process integration ready
- Participant withdrawal support
- Data deletion capabilities
- Transparent parameter disclosure options

## 📈 Research Applications

This system supports investigation of:
1. **Parameter effects** on interaction patterns
2. **Awareness bias** in human-AI collaboration
3. **L2 learning** progression tracking
4. **Creative confidence** development
5. **Collaborative dynamics** in educational AI

## 🚧 Troubleshooting

### Common Issues
1. **API Key Error**: Ensure OPENROUTER_API_KEY is set in .env
2. **Import Error**: Check Python path and dependencies
3. **Data Directory**: Ensure write permissions for chat_data folder
4. **Port Conflict**: Change port in room_chat_web.py if 5000 is occupied

### Debug Mode
```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

To extend the system:
1. Follow the existing room configuration pattern
2. Maintain the universal system prompt principle  
3. Preserve interaction logging format
4. Add appropriate error handling
5. Update documentation

---

**Version**: 1.0  
**Date**: October 2025  
**Research Context**: L2 Poetry Writing AI Parameter Effects Study