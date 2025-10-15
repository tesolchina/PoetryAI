"""
PoetryAI Room Chat System
Implements experimental room-based chatbot for L2 poetry writing research
"""

import asyncio
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path

from src.chatbot import CustomChatbot
from src.openrouter_client import ChatMessage


class RoomType(Enum):
    """Experimental room types for research study"""
    ROOM_1_STRUCTURED_AWARE = "room_1_structured_aware"
    ROOM_2_STRUCTURED_UNAWARE = "room_2_structured_unaware" 
    ROOM_3_EXPLORATORY_AWARE = "room_3_exploratory_aware"
    ROOM_4_EXPLORATORY_UNAWARE = "room_4_exploratory_unaware"


class InteractionType(Enum):
    """Three types of pedagogical interactions"""
    TYPE_A_DIAGNOSIS_REPAIR = "type_a_diagnosis_repair"
    TYPE_B_EXEMPLAR_PIVOT = "type_b_exemplar_pivot"
    TYPE_C_SURPRISE_HARVEST = "type_c_surprise_harvest"


@dataclass
class RoomConfig:
    """Configuration for each experimental room"""
    room_type: RoomType
    temperature: float
    top_p: float
    is_aware: bool
    model: str = "google/gemma-2-9b-it:free"
    
    @property
    def display_name(self) -> str:
        """Human-readable room name"""
        room_names = {
            RoomType.ROOM_1_STRUCTURED_AWARE: "Room 1: Structured + Aware",
            RoomType.ROOM_2_STRUCTURED_UNAWARE: "Room 2: Structured + Unaware",
            RoomType.ROOM_3_EXPLORATORY_AWARE: "Room 3: Exploratory + Aware", 
            RoomType.ROOM_4_EXPLORATORY_UNAWARE: "Room 4: Exploratory + Unaware"
        }
        return room_names[self.room_type]


@dataclass
class ChatInteraction:
    """Single chat interaction with metadata"""
    interaction_id: str
    timestamp: datetime
    room_type: RoomType
    participant_id: str
    user_message: str
    bot_response: str
    interaction_type: Optional[InteractionType] = None
    session_id: Optional[str] = None
    turn_number: int = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            **asdict(self),
            'timestamp': self.timestamp.isoformat(),
            'room_type': self.room_type.value,
            'interaction_type': self.interaction_type.value if self.interaction_type else None
        }


@dataclass
class ChatSession:
    """Complete chat session with metadata"""
    session_id: str
    participant_id: str
    room_type: RoomType
    start_time: datetime
    end_time: Optional[datetime] = None
    interactions: List[ChatInteraction] = None
    session_notes: str = ""
    
    def __post_init__(self):
        if self.interactions is None:
            self.interactions = []


class PoetryRoomChat:
    """
    Experimental room-based chat system for L2 poetry writing research
    """
    
    # Universal system prompt (same for all rooms)
    UNIVERSAL_SYSTEM_PROMPT = """You are a helpful creative writing assistant for English language learners working on poetry. Your role is to support students in exploring creative expression through collaborative writing.

EDUCATIONAL APPROACH:
- Help students with poetry structure, word choice, and creative development
- Provide encouraging, supportive guidance appropriate for L2 English learners (CEFR B1-B2)
- Offer specific suggestions when students need help with rules or improvements
- Celebrate creativity while maintaining educational value
- Use vocabulary appropriate for intermediate English learners

INTERACTION CAPABILITIES:
You can assist with three types of support:
- Type A (Constraint Repair): Help with poetry rules, structure, grammar issues, and technical corrections
- Type B (Content Enhancement): Improve word choice, imagery, expression, and provide models/examples
- Type C (Surprise Harvest): Introduce creative connections, unexpected possibilities, and inspirational suggestions

RESPONSE GUIDELINES:
- Keep responses 40-80 words unless student requests more detail
- Use clear, encouraging language with specific praise
- Acknowledge student input before providing new suggestions
- Ask engaging questions to guide next steps
- Offer 2-3 concrete options when providing suggestions

CULTURAL SENSITIVITY:
- Respect diverse cultural perspectives on creativity and learning
- Use inclusive examples and avoid culturally specific references
- Encourage students to draw from their own cultural experiences
- Maintain encouraging, patient tone throughout interactions

Always respond helpfully to student requests while maintaining an engaging, positive atmosphere for creative exploration."""
    
    # Room configurations
    ROOM_CONFIGS = {
        RoomType.ROOM_1_STRUCTURED_AWARE: RoomConfig(
            room_type=RoomType.ROOM_1_STRUCTURED_AWARE,
            temperature=0.3,
            top_p=0.4,
            is_aware=True
        ),
        RoomType.ROOM_2_STRUCTURED_UNAWARE: RoomConfig(
            room_type=RoomType.ROOM_2_STRUCTURED_UNAWARE,
            temperature=0.3,
            top_p=0.4,
            is_aware=False
        ),
        RoomType.ROOM_3_EXPLORATORY_AWARE: RoomConfig(
            room_type=RoomType.ROOM_3_EXPLORATORY_AWARE,
            temperature=0.8,
            top_p=0.9,
            is_aware=True
        ),
        RoomType.ROOM_4_EXPLORATORY_UNAWARE: RoomConfig(
            room_type=RoomType.ROOM_4_EXPLORATORY_UNAWARE,
            temperature=0.8,
            top_p=0.9,
            is_aware=False
        )
    }
    
    def __init__(self, room_type: RoomType, data_dir: str = "chat_data"):
        """Initialize room chat system"""
        self.room_config = self.ROOM_CONFIGS[room_type]
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # Initialize chatbot with room-specific parameters
        self.chatbot = CustomChatbot(
            name="PoetryBot",
            system_prompt=self.UNIVERSAL_SYSTEM_PROMPT,
            model=self.room_config.model,
            temperature=self.room_config.temperature,
        )
        
        # Override top_p setting (not directly supported by CustomChatbot)
        self.top_p = self.room_config.top_p
        
        # Session management
        self.current_session: Optional[ChatSession] = None
        self.sessions_log: List[ChatSession] = []
        
    def get_welcome_message(self) -> str:
        """Get welcome message for the room (aware vs unaware)"""
        base_message = """Hi! I'm your poetry partner for today. 

I can help you with:
- **Warm-up**: Sensory word exploration and creative exercises
- **Form Practice**: Haiku, couplets, free verse, or other structures  
- **Revision**: Improving and polishing existing poems

What would you like to work on today? You can share a theme, some words, or a few lines you've started with."""
        
        if self.room_config.is_aware:
            parameter_info = f"""

**Research Note**: This session uses AI parameters - Temperature: {self.room_config.temperature}, Top-p: {self.room_config.top_p}. These settings influence how creative or structured the AI responses will be."""
            return base_message + parameter_info
        else:
            return base_message
    
    def start_session(self, participant_id: str) -> str:
        """Start a new chat session"""
        session_id = str(uuid.uuid4())
        self.current_session = ChatSession(
            session_id=session_id,
            participant_id=participant_id,
            room_type=self.room_config.room_type,
            start_time=datetime.now()
        )
        
        # Clear chatbot history for new session
        self.chatbot.clear_history()
        
        return self.get_welcome_message()
    
    async def send_message(self, user_message: str) -> str:
        """Send message and get response"""
        if not self.current_session:
            raise ValueError("No active session. Call start_session() first.")
        
        # Get bot response
        bot_response = await self.chatbot.chat(user_message)
        
        # Create interaction record
        interaction = ChatInteraction(
            interaction_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            room_type=self.room_config.room_type,
            participant_id=self.current_session.participant_id,
            user_message=user_message,
            bot_response=bot_response,
            session_id=self.current_session.session_id,
            turn_number=len(self.current_session.interactions) + 1
        )
        
        # Classify interaction type (basic heuristics - can be enhanced)
        interaction.interaction_type = self._classify_interaction(user_message, bot_response)
        
        # Add to session
        self.current_session.interactions.append(interaction)
        
        # Log interaction
        self._log_interaction(interaction)
        
        return bot_response
    
    def end_session(self, session_notes: str = "") -> Dict[str, Any]:
        """End current session and return summary"""
        if not self.current_session:
            raise ValueError("No active session to end.")
        
        self.current_session.end_time = datetime.now()
        self.current_session.session_notes = session_notes
        
        # Calculate session statistics
        session_summary = self._calculate_session_summary()
        
        # Save session data
        self._save_session()
        
        # Add to sessions log
        self.sessions_log.append(self.current_session)
        
        # Clear current session
        self.current_session = None
        
        return session_summary
    
    def _classify_interaction(self, user_message: str, bot_response: str) -> InteractionType:
        """Basic interaction type classification (can be enhanced with ML)"""
        user_lower = user_message.lower()
        response_lower = bot_response.lower()
        
        # Type A: Diagnosis → Repair (error correction, rule help)
        repair_keywords = ['help', 'wrong', 'error', 'fix', 'correct', 'syllable', 'grammar', 'structure']
        if any(keyword in user_lower for keyword in repair_keywords):
            return InteractionType.TYPE_A_DIAGNOSIS_REPAIR
        
        # Type B: Exemplar Pivot (examples, models, templates)
        exemplar_keywords = ['example', 'show me', 'like', 'similar', 'template', 'format']
        if any(keyword in user_lower for keyword in exemplar_keywords):
            return InteractionType.TYPE_B_EXEMPLAR_PIVOT
        
        # Type C: Surprise Harvest (creative inspiration, stuck, ideas)
        surprise_keywords = ['stuck', 'idea', 'inspire', 'creative', 'different', 'new']
        if any(keyword in user_lower for keyword in surprise_keywords):
            return InteractionType.TYPE_C_SURPRISE_HARVEST
        
        # Default to Type A if unclear
        return InteractionType.TYPE_A_DIAGNOSIS_REPAIR
    
    def _calculate_session_summary(self) -> Dict[str, Any]:
        """Calculate summary statistics for the session"""
        if not self.current_session:
            return {}
        
        interactions = self.current_session.interactions
        total_interactions = len(interactions)
        
        # Count interaction types
        type_counts = {
            InteractionType.TYPE_A_DIAGNOSIS_REPAIR: 0,
            InteractionType.TYPE_B_EXEMPLAR_PIVOT: 0,
            InteractionType.TYPE_C_SURPRISE_HARVEST: 0
        }
        
        for interaction in interactions:
            if interaction.interaction_type:
                type_counts[interaction.interaction_type] += 1
        
        # Calculate session duration
        duration_minutes = 0
        if self.current_session.end_time:
            duration = self.current_session.end_time - self.current_session.start_time
            duration_minutes = duration.total_seconds() / 60
        
        return {
            'session_id': self.current_session.session_id,
            'room_type': self.room_config.room_type.value,
            'participant_id': self.current_session.participant_id,
            'total_interactions': total_interactions,
            'duration_minutes': round(duration_minutes, 2),
            'interaction_type_counts': {
                'type_a_diagnosis_repair': type_counts[InteractionType.TYPE_A_DIAGNOSIS_REPAIR],
                'type_b_exemplar_pivot': type_counts[InteractionType.TYPE_B_EXEMPLAR_PIVOT], 
                'type_c_surprise_harvest': type_counts[InteractionType.TYPE_C_SURPRISE_HARVEST]
            },
            'room_parameters': {
                'temperature': self.room_config.temperature,
                'top_p': self.room_config.top_p,
                'is_aware': self.room_config.is_aware
            }
        }
    
    def _log_interaction(self, interaction: ChatInteraction):
        """Log individual interaction to file"""
        log_file = self.data_dir / f"{self.room_config.room_type.value}_interactions.jsonl"
        
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(interaction.to_dict(), ensure_ascii=False) + '\n')
    
    def _save_session(self):
        """Save complete session data"""
        if not self.current_session:
            return
        
        session_file = self.data_dir / f"session_{self.current_session.session_id}.json"
        
        session_data = {
            'session_id': self.current_session.session_id,
            'participant_id': self.current_session.participant_id,
            'room_type': self.current_session.room_type.value,
            'start_time': self.current_session.start_time.isoformat(),
            'end_time': self.current_session.end_time.isoformat() if self.current_session.end_time else None,
            'session_notes': self.current_session.session_notes,
            'interactions': [interaction.to_dict() for interaction in self.current_session.interactions],
            'summary': self._calculate_session_summary()
        }
        
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, indent=2, ensure_ascii=False)
    
    def get_session_history(self) -> List[Dict[str, str]]:
        """Get current session conversation history"""
        if not self.current_session:
            return []
        
        history = []
        for interaction in self.current_session.interactions:
            history.extend([
                {"role": "user", "content": interaction.user_message},
                {"role": "assistant", "content": interaction.bot_response}
            ])
        return history
    
    def export_room_data(self, output_file: str = None) -> str:
        """Export all room data to JSON file"""
        if output_file is None:
            output_file = f"{self.room_config.room_type.value}_export.json"
        
        export_data = {
            'room_config': asdict(self.room_config),
            'export_timestamp': datetime.now().isoformat(),
            'sessions': []
        }
        
        # Load all session files for this room
        session_files = self.data_dir.glob(f"session_*.json")
        for session_file in session_files:
            with open(session_file, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
                if session_data.get('room_type') == self.room_config.room_type.value:
                    export_data['sessions'].append(session_data)
        
        export_path = self.data_dir / output_file
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        return str(export_path)


# Utility functions for creating room instances

def create_room_1() -> PoetryRoomChat:
    """Create Room 1: Structured + Aware"""
    return PoetryRoomChat(RoomType.ROOM_1_STRUCTURED_AWARE)


def create_room_2() -> PoetryRoomChat:
    """Create Room 2: Structured + Unaware"""  
    return PoetryRoomChat(RoomType.ROOM_2_STRUCTURED_UNAWARE)


def create_room_3() -> PoetryRoomChat:
    """Create Room 3: Exploratory + Aware"""
    return PoetryRoomChat(RoomType.ROOM_3_EXPLORATORY_AWARE)


def create_room_4() -> PoetryRoomChat:
    """Create Room 4: Exploratory + Unaware"""
    return PoetryRoomChat(RoomType.ROOM_4_EXPLORATORY_UNAWARE)


# Example usage and testing
async def demo_session():
    """Demonstration of room chat system"""
    # Create room instance
    room = create_room_2()  # Structured + Unaware
    
    # Start session
    welcome_msg = room.start_session("participant_001")
    print(f"Welcome: {welcome_msg}\n")
    
    # Simulate conversation
    test_messages = [
        "I want to write a haiku about rain",
        "Help me count syllables in 'gentle rain falls'",
        "Can you show me an example of a good haiku?",
        "I'm stuck and need creative ideas"
    ]
    
    for msg in test_messages:
        print(f"User: {msg}")
        response = await room.send_message(msg)
        print(f"Bot: {response}\n")
    
    # End session
    summary = room.end_session("Demo session completed successfully")
    print("Session Summary:")
    print(json.dumps(summary, indent=2))
    
    # Export data
    export_file = room.export_room_data()
    print(f"\nData exported to: {export_file}")


if __name__ == "__main__":
    asyncio.run(demo_session())