# PoetryAI Enhanced Logging System v2.1
# Updated to align with enhanced prompt engineering features

import json
import sqlite3
import asyncio
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import uuid
import logging

class InteractionType(Enum):
    """Enhanced interaction types based on prompt engineering v2.1"""
    GUIDED_WRITING = "A"  # Type A - Guided Writing
    ASSISTED_REVISION = "B"  # Type B - Assisted Revision
    COLLABORATIVE_CREATION = "C"  # Type C - Collaborative Creation
    FORM_SELECTION = "F"  # New: Poetry form selection
    PROGRESS_SUMMARY = "P"  # New: Progress tracking summaries
    CREATIVE_INDEPENDENCE = "I"  # New: Creative independence encouragement
    PARAMETER_AWARENESS = "PA"  # New: Parameter awareness interface
    OTHER = "O"

class PoetryForm(Enum):
    """Poetry forms from enhanced prompt design"""
    HAIKU = "haiku"
    FREE_VERSE = "free_verse"
    COUPLETS = "couplets"
    QUATRAIN = "quatrain"
    CUSTOM = "custom"

class SessionPhase(Enum):
    """Session phases with enhanced tracking"""
    TUTORIAL = "tutorial"
    FORM_SELECTION = "form_selection"  # New phase
    WARMUP = "warmup"
    CREATION = "creation"
    REVISION = "revision"
    PROGRESS_REVIEW = "progress_review"  # New phase
    COMPLETION = "completion"

@dataclass
class EnhancedMessage:
    """Enhanced message structure for v2.1 features"""
    message_id: str
    timestamp: datetime
    sender: str  # 'user' or 'ai'
    content: str
    interaction_type: InteractionType
    session_phase: SessionPhase
    room_id: str
    participant_id: str
    
    # Enhanced metadata
    metadata: Dict[str, Any]
    poetry_form: Optional[PoetryForm] = None
    creative_independence_marker: bool = False
    progress_related: bool = False
    parameter_awareness_shown: bool = False
    
    # Performance metrics
    response_time_ms: Optional[float] = None
    character_count: int = 0
    word_count: int = 0
    sentiment_score: Optional[float] = None

@dataclass
class PoetryCreation:
    """Enhanced poetry tracking structure"""
    poem_id: str
    timestamp: datetime
    participant_id: str
    room_id: str
    form: PoetryForm
    content: str
    creation_phase: str  # 'initial', 'revised', 'final'
    
    # Enhanced tracking
    form_selection_process: Dict[str, Any]
    creative_independence_level: float  # 0.0-1.0 scale
    ai_collaboration_level: float  # 0.0-1.0 scale
    revision_history: List[Dict[str, Any]]
    progress_milestone: bool = False
    
    # Quality metrics
    word_count: int = 0
    unique_words: int = 0
    metaphor_count: int = 0
    imagery_richness: float = 0.0

@dataclass
class SessionProgress:
    """New session progress tracking"""
    session_id: str
    participant_id: str
    poems_completed: int
    forms_explored: List[PoetryForm]
    creative_independence_events: List[Dict[str, Any]]
    progress_summaries_generated: int
    milestones_achieved: List[str]
    session_memory: Dict[str, Any]

class EnhancedPoetryLogger:
    """Enhanced logging system aligned with prompt engineering v2.1"""
    
    def __init__(self, db_path: str = "poetryai_enhanced_v2.db"):
        self.db_path = db_path
        self.setup_database()
        self.setup_logging()
        
        # Enhanced tracking attributes
        self.active_sessions: Dict[str, Dict] = {}
        self.interaction_classifiers = {}
        self.progress_trackers: Dict[str, SessionProgress] = {}
        
    def setup_database(self):
        """Create enhanced database schema for v2.1 features"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Enhanced sessions table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS enhanced_sessions (
            session_id TEXT PRIMARY KEY,
            participant_id TEXT NOT NULL,
            room_id TEXT NOT NULL,
            room_type TEXT NOT NULL, -- structured_aware, structured_unaware, etc.
            start_time TIMESTAMP,
            end_time TIMESTAMP,
            total_duration INTEGER,
            
            -- Enhanced features tracking
            forms_selected TEXT, -- JSON array of selected forms
            creative_independence_score REAL,
            progress_summaries_count INTEGER,
            parameter_awareness_interactions INTEGER,
            session_memory TEXT, -- JSON object
            
            -- Session outcomes
            poems_created INTEGER,
            interaction_type_distribution TEXT, -- JSON object
            engagement_score REAL,
            completion_status TEXT,
            
            FOREIGN KEY (participant_id) REFERENCES participants (participant_id)
        )
        ''')
        
        # Enhanced messages table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS enhanced_messages (
            message_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            timestamp TIMESTAMP,
            sender TEXT NOT NULL,
            content TEXT NOT NULL,
            interaction_type TEXT NOT NULL,
            session_phase TEXT NOT NULL,
            
            -- Enhanced classifications
            poetry_form TEXT,
            creative_independence_marker BOOLEAN,
            progress_related BOOLEAN,
            parameter_awareness_shown BOOLEAN,
            
            -- Performance metrics
            response_time_ms REAL,
            character_count INTEGER,
            word_count INTEGER,
            sentiment_score REAL,
            
            -- Metadata
            metadata TEXT, -- JSON object
            
            FOREIGN KEY (session_id) REFERENCES enhanced_sessions (session_id)
        )
        ''')
        
        # Enhanced poetry creations table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS enhanced_poetry_creations (
            poem_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            timestamp TIMESTAMP,
            participant_id TEXT NOT NULL,
            room_id TEXT NOT NULL,
            
            -- Poetry details
            form TEXT NOT NULL,
            content TEXT NOT NULL,
            creation_phase TEXT NOT NULL,
            
            -- Enhanced tracking
            form_selection_process TEXT, -- JSON object
            creative_independence_level REAL,
            ai_collaboration_level REAL,
            revision_history TEXT, -- JSON array
            progress_milestone BOOLEAN,
            
            -- Quality metrics
            word_count INTEGER,
            unique_words INTEGER,
            metaphor_count INTEGER,
            imagery_richness REAL,
            
            FOREIGN KEY (session_id) REFERENCES enhanced_sessions (session_id)
        )
        ''')
        
        # New progress tracking table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS session_progress (
            progress_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            timestamp TIMESTAMP,
            
            -- Progress metrics
            poems_completed INTEGER,
            forms_explored TEXT, -- JSON array
            creative_independence_events TEXT, -- JSON array
            progress_summaries_generated INTEGER,
            milestones_achieved TEXT, -- JSON array
            session_memory TEXT, -- JSON object
            
            FOREIGN KEY (session_id) REFERENCES enhanced_sessions (session_id)
        )
        ''')
        
        # Enhanced parameter awareness tracking
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS parameter_awareness_interactions (
            interaction_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            timestamp TIMESTAMP,
            room_id TEXT NOT NULL,
            
            -- Parameter information shown
            parameters_displayed TEXT, -- JSON object
            user_response TEXT,
            understanding_level TEXT, -- 'high', 'medium', 'low'
            parameter_influence_acknowledged BOOLEAN,
            
            FOREIGN KEY (session_id) REFERENCES enhanced_sessions (session_id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def setup_logging(self):
        """Setup enhanced logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'poetryai_enhanced_{datetime.now().strftime("%Y%m%d")}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('PoetryAI_Enhanced_Logger')
    
    def start_enhanced_session(self, participant_id: str, room_id: str, room_type: str) -> str:
        """Start a new enhanced session with v2.1 features"""
        session_id = str(uuid.uuid4())
        
        session_data = {
            'session_id': session_id,
            'participant_id': participant_id,
            'room_id': room_id,
            'room_type': room_type,
            'start_time': datetime.now(),
            'forms_selected': [],
            'creative_independence_events': [],
            'progress_summaries': [],
            'parameter_awareness_interactions': [],
            'session_memory': {
                'poems_created': [],
                'preferences': {},
                'progress_milestones': []
            }
        }
        
        self.active_sessions[session_id] = session_data
        
        # Initialize progress tracker
        self.progress_trackers[session_id] = SessionProgress(
            session_id=session_id,
            participant_id=participant_id,
            poems_completed=0,
            forms_explored=[],
            creative_independence_events=[],
            progress_summaries_generated=0,
            milestones_achieved=[],
            session_memory={}
        )
        
        # Log session start
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO enhanced_sessions 
        (session_id, participant_id, room_id, room_type, start_time,
         forms_selected, creative_independence_score, progress_summaries_count,
         parameter_awareness_interactions, session_memory, poems_created,
         interaction_type_distribution, engagement_score, completion_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (session_id, participant_id, room_id, room_type, datetime.now(),
              json.dumps([]), 0.0, 0, 0, json.dumps({}), 0,
              json.dumps({}), 0.0, 'active'))
        
        conn.commit()
        conn.close()
        
        self.logger.info(f"Enhanced session started: {session_id} for participant {participant_id} in room {room_id}")
        return session_id
    
    def log_enhanced_message(self, session_id: str, sender: str, content: str, 
                           interaction_type: InteractionType, session_phase: SessionPhase,
                           **kwargs) -> str:
        """Log message with enhanced v2.1 features"""
        message_id = str(uuid.uuid4())
        timestamp = datetime.now()
        
        # Enhanced classification
        poetry_form = kwargs.get('poetry_form')
        creative_independence_marker = self.detect_creative_independence(content)
        progress_related = self.detect_progress_content(content)
        parameter_awareness_shown = kwargs.get('parameter_awareness_shown', False)
        
        # Create enhanced message
        message = EnhancedMessage(
            message_id=message_id,
            timestamp=timestamp,
            sender=sender,
            content=content,
            interaction_type=interaction_type,
            session_phase=session_phase,
            room_id=self.active_sessions[session_id]['room_id'],
            participant_id=self.active_sessions[session_id]['participant_id'],
            metadata=kwargs.get('metadata', {}),
            poetry_form=poetry_form,
            creative_independence_marker=creative_independence_marker,
            progress_related=progress_related,
            parameter_awareness_shown=parameter_awareness_shown,
            response_time_ms=kwargs.get('response_time_ms'),
            character_count=len(content),
            word_count=len(content.split()),
            sentiment_score=kwargs.get('sentiment_score')
        )
        
        # Store in database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO enhanced_messages 
        (message_id, session_id, timestamp, sender, content, interaction_type,
         session_phase, poetry_form, creative_independence_marker, progress_related,
         parameter_awareness_shown, response_time_ms, character_count, word_count,
         sentiment_score, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (message_id, session_id, timestamp, sender, content, interaction_type.value,
              session_phase.value, poetry_form.value if poetry_form else None,
              creative_independence_marker, progress_related, parameter_awareness_shown,
              message.response_time_ms, message.character_count, message.word_count,
              message.sentiment_score, json.dumps(message.metadata)))
        
        conn.commit()
        conn.close()
        
        # Update session tracking
        self.update_session_tracking(session_id, message)
        
        return message_id
    
    def log_poetry_form_selection(self, session_id: str, form_selected: PoetryForm, 
                                selection_process: Dict[str, Any]):
        """Log poetry form selection process (new v2.1 feature)"""
        if session_id in self.active_sessions:
            self.active_sessions[session_id]['forms_selected'].append({
                'form': form_selected.value,
                'timestamp': datetime.now().isoformat(),
                'selection_process': selection_process
            })
            
            # Update progress tracker
            if session_id in self.progress_trackers:
                if form_selected not in self.progress_trackers[session_id].forms_explored:
                    self.progress_trackers[session_id].forms_explored.append(form_selected)
        
        self.logger.info(f"Poetry form selected in session {session_id}: {form_selected.value}")
    
    def log_creative_independence_event(self, session_id: str, event_type: str, 
                                     content: str, independence_level: float):
        """Log creative independence encouragement events (new v2.1 feature)"""
        event = {
            'timestamp': datetime.now().isoformat(),
            'event_type': event_type,
            'content': content,
            'independence_level': independence_level,
            'session_phase': self.get_current_phase(session_id)
        }
        
        if session_id in self.active_sessions:
            self.active_sessions[session_id]['creative_independence_events'].append(event)
        
        if session_id in self.progress_trackers:
            self.progress_trackers[session_id].creative_independence_events.append(event)
        
        self.logger.info(f"Creative independence event logged for session {session_id}: {event_type}")
    
    def log_progress_summary(self, session_id: str, summary_content: str, 
                           poems_completed: int, milestones: List[str]):
        """Log progress summary generation (new v2.1 feature)"""
        summary_data = {
            'timestamp': datetime.now().isoformat(),
            'content': summary_content,
            'poems_completed': poems_completed,
            'milestones': milestones,
            'session_phase': self.get_current_phase(session_id)
        }
        
        if session_id in self.active_sessions:
            self.active_sessions[session_id]['progress_summaries'].append(summary_data)
        
        if session_id in self.progress_trackers:
            self.progress_trackers[session_id].progress_summaries_generated += 1
            self.progress_trackers[session_id].milestones_achieved.extend(milestones)
        
        # Store in database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO session_progress 
        (progress_id, session_id, timestamp, poems_completed, forms_explored,
         creative_independence_events, progress_summaries_generated, milestones_achieved,
         session_memory)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (str(uuid.uuid4()), session_id, datetime.now(), poems_completed,
              json.dumps([f.value for f in self.progress_trackers[session_id].forms_explored]),
              json.dumps(self.progress_trackers[session_id].creative_independence_events),
              self.progress_trackers[session_id].progress_summaries_generated,
              json.dumps(milestones), json.dumps({})))
        
        conn.commit()
        conn.close()
        
        self.logger.info(f"Progress summary logged for session {session_id}")
    
    def log_parameter_awareness_interaction(self, session_id: str, parameters_displayed: Dict[str, Any],
                                          user_response: str, understanding_level: str):
        """Log parameter awareness interface interactions (new v2.1 feature)"""
        interaction_id = str(uuid.uuid4())
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO parameter_awareness_interactions
        (interaction_id, session_id, timestamp, room_id, parameters_displayed,
         user_response, understanding_level, parameter_influence_acknowledged)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (interaction_id, session_id, datetime.now(),
              self.active_sessions[session_id]['room_id'],
              json.dumps(parameters_displayed), user_response, understanding_level,
              'parameter' in user_response.lower()))
        
        conn.commit()
        conn.close()
        
        # Update session tracking
        if session_id in self.active_sessions:
            self.active_sessions[session_id]['parameter_awareness_interactions'].append({
                'interaction_id': interaction_id,
                'timestamp': datetime.now().isoformat(),
                'parameters_displayed': parameters_displayed,
                'user_response': user_response,
                'understanding_level': understanding_level
            })
        
        self.logger.info(f"Parameter awareness interaction logged for session {session_id}")
    
    def detect_creative_independence(self, content: str) -> bool:
        """Detect creative independence encouragement patterns"""
        independence_keywords = [
            'your own words', 'your way', 'your style', 'your voice',
            'what do you think', 'your idea', 'your choice', 'express yourself',
            'your creativity', 'your imagination', 'your perspective'
        ]
        return any(keyword in content.lower() for keyword in independence_keywords)
    
    def detect_progress_content(self, content: str) -> bool:
        """Detect progress-related content"""
        progress_keywords = [
            'progress', 'completed', 'accomplished', 'achieved', 'milestone',
            'summary', 'so far', 'journey', 'improvement', 'growth'
        ]
        return any(keyword in content.lower() for keyword in progress_keywords)
    
    def get_current_phase(self, session_id: str) -> str:
        """Get current session phase"""
        if session_id in self.active_sessions:
            return self.active_sessions[session_id].get('current_phase', 'unknown')
        return 'unknown'
    
    def update_session_tracking(self, session_id: str, message: EnhancedMessage):
        """Update session-level tracking based on new message"""
        if session_id not in self.active_sessions:
            return
        
        session = self.active_sessions[session_id]
        
        # Update interaction type counts
        interaction_counts = session.get('interaction_type_counts', {})
        interaction_type = message.interaction_type.value
        interaction_counts[interaction_type] = interaction_counts.get(interaction_type, 0) + 1
        session['interaction_type_counts'] = interaction_counts
        
        # Update creative independence score
        if message.creative_independence_marker:
            current_score = session.get('creative_independence_score', 0.0)
            session['creative_independence_score'] = min(1.0, current_score + 0.1)
    
    def generate_enhanced_session_report(self, session_id: str) -> Dict[str, Any]:
        """Generate comprehensive session report with v2.1 features"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get session data
        cursor.execute('''
        SELECT * FROM enhanced_sessions WHERE session_id = ?
        ''', (session_id,))
        session_data = cursor.fetchone()
        
        # Get messages
        cursor.execute('''
        SELECT * FROM enhanced_messages WHERE session_id = ? ORDER BY timestamp
        ''', (session_id,))
        messages = cursor.fetchall()
        
        # Get poetry creations
        cursor.execute('''
        SELECT * FROM enhanced_poetry_creations WHERE session_id = ?
        ''', (session_id,))
        poems = cursor.fetchall()
        
        # Get progress data
        cursor.execute('''
        SELECT * FROM session_progress WHERE session_id = ? ORDER BY timestamp DESC LIMIT 1
        ''', (session_id,))
        progress_data = cursor.fetchone()
        
        # Get parameter awareness interactions
        cursor.execute('''
        SELECT * FROM parameter_awareness_interactions WHERE session_id = ?
        ''', (session_id,))
        parameter_interactions = cursor.fetchall()
        
        conn.close()
        
        # Compile comprehensive report
        report = {
            'session_overview': {
                'session_id': session_id,
                'participant_id': session_data[1] if session_data else None,
                'room_id': session_data[2] if session_data else None,
                'room_type': session_data[3] if session_data else None,
                'duration': self.calculate_session_duration(session_id),
                'completion_status': session_data[14] if session_data else None
            },
            'enhanced_features_usage': {
                'poetry_forms_explored': json.loads(session_data[5]) if session_data and session_data[5] else [],
                'creative_independence_score': session_data[6] if session_data else 0.0,
                'progress_summaries_count': session_data[7] if session_data else 0,
                'parameter_awareness_interactions': len(parameter_interactions),
                'session_memory_size': len(json.loads(session_data[9])) if session_data and session_data[9] else 0
            },
            'interaction_analysis': self.analyze_enhanced_interactions(messages),
            'poetry_analysis': self.analyze_enhanced_poetry_creation(poems),
            'progress_tracking': self.analyze_progress_tracking(progress_data),
            'parameter_awareness_analysis': self.analyze_parameter_awareness(parameter_interactions),
            'engagement_metrics': self.calculate_enhanced_engagement_metrics(messages),
            'research_insights': self.generate_research_insights(session_id)
        }
        
        return report
    
    def analyze_enhanced_interactions(self, messages) -> Dict[str, Any]:
        """Analyze interactions with v2.1 enhanced features"""
        if not messages:
            return {}
        
        total_messages = len(messages)
        interaction_types = {}
        creative_independence_count = 0
        progress_related_count = 0
        parameter_awareness_count = 0
        
        for message in messages:
            # Count interaction types
            interaction_type = message[5]  # interaction_type column
            interaction_types[interaction_type] = interaction_types.get(interaction_type, 0) + 1
            
            # Count enhanced features
            if message[8]:  # creative_independence_marker
                creative_independence_count += 1
            if message[9]:  # progress_related
                progress_related_count += 1
            if message[10]:  # parameter_awareness_shown
                parameter_awareness_count += 1
        
        return {
            'total_interactions': total_messages,
            'interaction_type_distribution': interaction_types,
            'creative_independence_percentage': (creative_independence_count / total_messages) * 100,
            'progress_related_percentage': (progress_related_count / total_messages) * 100,
            'parameter_awareness_percentage': (parameter_awareness_count / total_messages) * 100,
            'enhanced_feature_utilization': {
                'creative_independence_events': creative_independence_count,
                'progress_discussions': progress_related_count,
                'parameter_awareness_moments': parameter_awareness_count
            }
        }
    
    def export_enhanced_data(self, session_id: str, export_format: str = 'json') -> str:
        """Export enhanced session data in specified format"""
        report = self.generate_enhanced_session_report(session_id)
        
        if export_format.lower() == 'json':
            filename = f"poetryai_enhanced_session_{session_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, default=str)
            
        elif export_format.lower() == 'csv':
            import pandas as pd
            
            # Flatten the report for CSV export
            flattened_data = self.flatten_report_for_csv(report)
            df = pd.DataFrame([flattened_data])
            filename = f"poetryai_enhanced_session_{session_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            df.to_csv(filename, index=False)
        
        self.logger.info(f"Enhanced session data exported: {filename}")
        return filename

# Example usage
if __name__ == "__main__":
    # Initialize enhanced logger
    logger = EnhancedPoetryLogger()
    
    # Start enhanced session
    session_id = logger.start_enhanced_session(
        participant_id="PART_001",
        room_id="room_1",
        room_type="structured_aware"
    )
    
    # Log poetry form selection
    logger.log_poetry_form_selection(
        session_id=session_id,
        form_selected=PoetryForm.HAIKU,
        selection_process={
            'options_shown': ['haiku', 'free_verse', 'couplets'],
            'user_preference': 'nature poetry',
            'ai_recommendation': 'haiku for nature themes'
        }
    )
    
    # Log enhanced message
    logger.log_enhanced_message(
        session_id=session_id,
        sender="ai",
        content="I love how you chose your own words to describe the sunrise! What other unique words come to mind when you think about morning?",
        interaction_type=InteractionType.CREATIVE_INDEPENDENCE,
        session_phase=SessionPhase.CREATION,
        poetry_form=PoetryForm.HAIKU,
        metadata={"creativity_encouragement": True}
    )
    
    # Log progress summary
    logger.log_progress_summary(
        session_id=session_id,
        summary_content="Great work! You've completed 2 poems and explored haiku and free verse forms.",
        poems_completed=2,
        milestones=["first_poem_completed", "form_exploration_milestone"]
    )
    
    # Generate comprehensive report
    report = logger.generate_enhanced_session_report(session_id)
    print("Enhanced session report generated successfully!")