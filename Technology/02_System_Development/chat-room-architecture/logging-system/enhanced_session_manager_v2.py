# Enhanced Session Management System v2.1
# Integrates with prompt engineering v2.1 features

import json
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
import uuid

from enhanced_logging_system_v2 import (
    EnhancedPoetryLogger, InteractionType, PoetryForm, 
    SessionPhase, PoetryCreation, SessionProgress
)

@dataclass
class RoomConfiguration:
    """Enhanced room configuration with v2.1 parameters"""
    room_id: str
    room_type: str  # structured_aware, structured_unaware, exploratory_aware, exploratory_unaware
    parameters: Dict[str, float]
    awareness_level: str  # 'aware' or 'unaware'
    structure_level: str  # 'structured' or 'exploratory'
    
    # Enhanced features availability
    parameter_interface_enabled: bool
    form_selection_guidance_level: str  # 'high', 'medium', 'low'
    creative_independence_emphasis: float  # 0.0-1.0
    progress_tracking_detail: str  # 'comprehensive', 'basic', 'minimal'

class EnhancedPoetrySessionManager:
    """Enhanced session management with v2.1 prompt engineering features"""
    
    def __init__(self):
        self.logger = EnhancedPoetryLogger()
        self.active_sessions: Dict[str, Dict] = {}
        self.room_configurations = self.setup_room_configurations()
        self.session_memory: Dict[str, Dict] = {}
        
        # Enhanced tracking
        self.form_selection_tracker: Dict[str, List] = {}
        self.creative_independence_tracker: Dict[str, List] = {}
        self.progress_milestone_tracker: Dict[str, List] = {}
    
    def setup_room_configurations(self) -> Dict[str, RoomConfiguration]:
        """Setup the 4 enhanced room configurations"""
        return {
            'room_1_structured_aware': RoomConfiguration(
                room_id='room_1',
                room_type='structured_aware',
                parameters={'temperature': 0.25, 'top_p': 0.35, 'max_tokens': 150},
                awareness_level='aware',
                structure_level='structured',
                parameter_interface_enabled=True,
                form_selection_guidance_level='high',
                creative_independence_emphasis=0.3,
                progress_tracking_detail='comprehensive'
            ),
            'room_2_structured_unaware': RoomConfiguration(
                room_id='room_2',
                room_type='structured_unaware',
                parameters={'temperature': 0.25, 'top_p': 0.35, 'max_tokens': 150},
                awareness_level='unaware',
                structure_level='structured',
                parameter_interface_enabled=False,
                form_selection_guidance_level='high',
                creative_independence_emphasis=0.3,
                progress_tracking_detail='basic'
            ),
            'room_3_exploratory_aware': RoomConfiguration(
                room_id='room_3',
                room_type='exploratory_aware',
                parameters={'temperature': 0.8, 'top_p': 0.9, 'max_tokens': 200},
                awareness_level='aware',
                structure_level='exploratory',
                parameter_interface_enabled=True,
                form_selection_guidance_level='medium',
                creative_independence_emphasis=0.8,
                progress_tracking_detail='comprehensive'
            ),
            'room_4_exploratory_unaware': RoomConfiguration(
                room_id='room_4',
                room_type='exploratory_unaware',
                parameters={'temperature': 0.8, 'top_p': 0.9, 'max_tokens': 200},
                awareness_level='unaware',
                structure_level='exploratory',
                parameter_interface_enabled=False,
                form_selection_guidance_level='medium',
                creative_independence_emphasis=0.8,
                progress_tracking_detail='basic'
            )
        }
    
    async def create_enhanced_session(self, participant_id: str, room_type: str) -> Tuple[str, Dict]:
        """Create new enhanced session with v2.1 features"""
        session_id = str(uuid.uuid4())
        room_config = self.room_configurations.get(room_type)
        
        if not room_config:
            raise ValueError(f"Invalid room type: {room_type}")
        
        # Initialize session with enhanced features
        session_data = {
            'session_id': session_id,
            'participant_id': participant_id,
            'room_config': room_config,
            'start_time': datetime.now(),
            'current_phase': SessionPhase.TUTORIAL,
            
            # Enhanced v2.1 features
            'session_memory': {
                'poems_created': [],
                'forms_explored': [],
                'creative_milestones': [],
                'user_preferences': {},
                'progress_summaries': []
            },
            
            # Form selection tracking
            'form_selection_history': [],
            'current_form': None,
            'form_guidance_provided': [],
            
            # Creative independence tracking
            'creative_independence_events': [],
            'independence_level': 0.0,
            'user_initiated_ideas': [],
            
            # Progress tracking
            'progress_milestones': [],
            'poems_completed_count': 0,
            'session_achievements': [],
            
            # Parameter awareness (for rooms 1 & 3)
            'parameter_interface_shown': False,
            'parameter_understanding_level': 'none',
            'parameter_acknowledgments': []
        }
        
        self.active_sessions[session_id] = session_data
        
        # Initialize enhanced logging
        logger_session_id = self.logger.start_enhanced_session(
            participant_id=participant_id,
            room_id=room_config.room_id,
            room_type=room_type
        )
        
        # Initialize session-specific trackers
        self.form_selection_tracker[session_id] = []
        self.creative_independence_tracker[session_id] = []
        self.progress_milestone_tracker[session_id] = []
        self.session_memory[session_id] = session_data['session_memory']
        
        return session_id, session_data
    
    async def handle_poetry_form_selection(self, session_id: str, user_message: str) -> Dict[str, Any]:
        """Handle poetry form selection with enhanced guidance"""
        if session_id not in self.active_sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.active_sessions[session_id]
        room_config = session['room_config']
        
        # Analyze user's form preference
        form_analysis = self.analyze_form_preference(user_message)
        
        # Generate form selection response based on room configuration
        response_data = await self.generate_form_selection_response(
            session_id=session_id,
            user_preference=form_analysis,
            guidance_level=room_config.form_selection_guidance_level
        )
        
        # Log form selection process
        self.logger.log_poetry_form_selection(
            session_id=session_id,
            form_selected=response_data['recommended_form'],
            selection_process={
                'user_preference': form_analysis,
                'guidance_level': room_config.form_selection_guidance_level,
                'options_presented': response_data['options_presented'],
                'reasoning': response_data['reasoning']
            }
        )
        
        # Update session tracking
        session['current_form'] = response_data['recommended_form']
        session['form_selection_history'].append({
            'timestamp': datetime.now(),
            'form_selected': response_data['recommended_form'],
            'user_input': user_message,
            'guidance_provided': response_data['guidance']
        })
        
        # Update session memory
        if response_data['recommended_form'] not in session['session_memory']['forms_explored']:
            session['session_memory']['forms_explored'].append(response_data['recommended_form'])
        
        return response_data
    
    async def process_creative_independence_moment(self, session_id: str, 
                                                 user_message: str, ai_response: str) -> Dict[str, Any]:
        """Process and log creative independence encouragement moments"""
        if session_id not in self.active_sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.active_sessions[session_id]
        room_config = session['room_config']
        
        # Analyze creative independence in the interaction
        independence_analysis = self.analyze_creative_independence(user_message, ai_response)
        
        if independence_analysis['independence_detected']:
            # Calculate independence level
            independence_level = min(1.0, 
                session['independence_level'] + independence_analysis['independence_score'])
            session['independence_level'] = independence_level
            
            # Log the event
            self.logger.log_creative_independence_event(
                session_id=session_id,
                event_type=independence_analysis['event_type'],
                content=ai_response,
                independence_level=independence_level
            )
            
            # Update session tracking
            independence_event = {
                'timestamp': datetime.now(),
                'event_type': independence_analysis['event_type'],
                'user_contribution': independence_analysis['user_contribution'],
                'ai_encouragement': independence_analysis['ai_encouragement'],
                'independence_score': independence_analysis['independence_score']
            }
            
            session['creative_independence_events'].append(independence_event)
            self.creative_independence_tracker[session_id].append(independence_event)
            
            # Check for milestones
            milestone_reached = self.check_independence_milestones(session_id, independence_level)
            if milestone_reached:
                await self.handle_milestone_achievement(session_id, milestone_reached)
        
        return independence_analysis
    
    async def generate_progress_summary(self, session_id: str, trigger: str = 'poem_completion') -> Dict[str, Any]:
        """Generate enhanced progress summary with session memory"""
        if session_id not in self.active_sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.active_sessions[session_id]
        room_config = session['room_config']
        
        # Only generate detailed summaries for comprehensive tracking rooms
        if room_config.progress_tracking_detail != 'comprehensive':
            return {'summary_generated': False, 'reason': 'minimal tracking room'}
        
        # Compile progress data
        progress_data = {
            'poems_completed': session['poems_completed_count'],
            'forms_explored': session['session_memory']['forms_explored'],
            'creative_independence_level': session['independence_level'],
            'milestones_achieved': session['progress_milestones'],
            'session_duration': self.calculate_session_duration(session_id),
            'achievements': session['session_achievements']
        }
        
        # Generate personalized summary content
        summary_content = await self.create_personalized_summary(session_id, progress_data, trigger)
        
        # Log the progress summary
        self.logger.log_progress_summary(
            session_id=session_id,
            summary_content=summary_content['content'],
            poems_completed=progress_data['poems_completed'],
            milestones=progress_data['milestones_achieved']
        )
        
        # Update session memory
        session['session_memory']['progress_summaries'].append({
            'timestamp': datetime.now(),
            'trigger': trigger,
            'content': summary_content,
            'data_snapshot': progress_data
        })
        
        return summary_content
    
    async def handle_parameter_awareness_interface(self, session_id: str, 
                                                 user_interaction: str) -> Dict[str, Any]:
        """Handle parameter awareness interface for rooms 1 & 3"""
        if session_id not in self.active_sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.active_sessions[session_id]
        room_config = session['room_config']
        
        # Only show parameter interface for aware rooms (1 & 3)
        if not room_config.parameter_interface_enabled:
            return {'interface_shown': False, 'reason': 'unaware condition'}
        
        # Prepare parameter information based on room
        parameter_info = self.prepare_parameter_interface_content(room_config)
        
        # Analyze user's understanding level
        understanding_analysis = self.analyze_parameter_understanding(user_interaction)
        
        # Log the parameter awareness interaction
        self.logger.log_parameter_awareness_interaction(
            session_id=session_id,
            parameters_displayed=parameter_info,
            user_response=user_interaction,
            understanding_level=understanding_analysis['level']
        )
        
        # Update session tracking
        session['parameter_interface_shown'] = True
        session['parameter_understanding_level'] = understanding_analysis['level']
        session['parameter_acknowledgments'].append({
            'timestamp': datetime.now(),
            'user_response': user_interaction,
            'understanding_level': understanding_analysis['level'],
            'parameters_shown': parameter_info
        })
        
        return {
            'interface_shown': True,
            'parameter_info': parameter_info,
            'understanding_analysis': understanding_analysis,
            'followup_needed': understanding_analysis['level'] == 'low'
        }
    
    def analyze_form_preference(self, user_message: str) -> Dict[str, Any]:
        """Analyze user's poetry form preference from their message"""
        form_keywords = {
            PoetryForm.HAIKU: ['haiku', '5-7-5', 'syllables', 'nature', 'moment', 'short'],
            PoetryForm.FREE_VERSE: ['free', 'no rules', 'expression', 'flow', 'natural'],
            PoetryForm.COUPLETS: ['couplet', 'rhyme', 'pairs', 'two lines'],
            PoetryForm.QUATRAIN: ['quatrain', 'four lines', 'stanza', 'verse'],
        }
        
        theme_indicators = {
            'nature': ['tree', 'flower', 'sky', 'sun', 'moon', 'rain', 'wind'],
            'emotion': ['happy', 'sad', 'love', 'fear', 'joy', 'anger', 'peace'],
            'memory': ['remember', 'childhood', 'past', 'nostalgia', 'yesterday'],
            'relationships': ['friend', 'family', 'mother', 'father', 'love', 'together']
        }
        
        # Analyze form preference
        form_scores = {}
        for form, keywords in form_keywords.items():
            score = sum(1 for keyword in keywords if keyword in user_message.lower())
            if score > 0:
                form_scores[form] = score
        
        # Analyze theme
        theme_scores = {}
        for theme, keywords in theme_indicators.items():
            score = sum(1 for keyword in keywords if keyword in user_message.lower())
            if score > 0:
                theme_scores[theme] = score
        
        # Determine preference
        preferred_form = max(form_scores, key=form_scores.get) if form_scores else None
        preferred_theme = max(theme_scores, key=theme_scores.get) if theme_scores else 'general'
        
        return {
            'preferred_form': preferred_form,
            'preferred_theme': preferred_theme,
            'form_scores': form_scores,
            'theme_scores': theme_scores,
            'confidence': max(form_scores.values()) if form_scores else 0
        }
    
    def analyze_creative_independence(self, user_message: str, ai_response: str) -> Dict[str, Any]:
        """Analyze creative independence in the interaction"""
        # User contribution indicators
        user_independence_indicators = [
            'I think', 'my idea', 'what if', 'I want to', 'I imagine',
            'my way', 'I prefer', 'I feel', 'I see', 'my experience'
        ]
        
        # AI encouragement indicators
        ai_encouragement_indicators = [
            'your words', 'your idea', 'your way', 'what do you think',
            'your choice', 'your creativity', 'your voice', 'your style',
            'express yourself', 'your imagination', 'your perspective'
        ]
        
        # Calculate scores
        user_independence_score = sum(1 for indicator in user_independence_indicators 
                                    if indicator in user_message.lower()) / len(user_independence_indicators)
        
        ai_encouragement_score = sum(1 for indicator in ai_encouragement_indicators 
                                   if indicator in ai_response.lower()) / len(ai_encouragement_indicators)
        
        # Determine event type
        event_type = 'none'
        if user_independence_score > 0.1 and ai_encouragement_score > 0.1:
            event_type = 'mutual_creative_exchange'
        elif user_independence_score > 0.1:
            event_type = 'user_creative_initiative'
        elif ai_encouragement_score > 0.1:
            event_type = 'ai_independence_encouragement'
        
        independence_detected = event_type != 'none'
        overall_score = (user_independence_score + ai_encouragement_score) / 2
        
        return {
            'independence_detected': independence_detected,
            'event_type': event_type,
            'independence_score': overall_score,
            'user_contribution': user_independence_score,
            'ai_encouragement': ai_encouragement_score,
            'analysis_details': {
                'user_indicators_found': [ind for ind in user_independence_indicators 
                                        if ind in user_message.lower()],
                'ai_indicators_found': [ind for ind in ai_encouragement_indicators 
                                      if ind in ai_response.lower()]
            }
        }
    
    def prepare_parameter_interface_content(self, room_config: RoomConfiguration) -> Dict[str, Any]:
        """Prepare parameter awareness interface content"""
        base_content = {
            'room_type': room_config.room_type,
            'parameters': room_config.parameters,
            'explanation': {
                'temperature': room_config.parameters['temperature'],
                'creativity_level': 'Low/Structured' if room_config.structure_level == 'structured' else 'High/Exploratory'
            }
        }
        
        if room_config.room_id == 'room_1':  # Structured + Aware
            base_content['description'] = """
            🔧 Current AI Settings:
            • Temperature: 0.25 (Low creativity/High consistency)
            • Style: Structured and systematic guidance
            
            What this means for you:
            • The AI provides more consistent, rule-based guidance
            • Suggestions focus on clear structure and established poetry conventions
            • Responses are more predictable and systematic
            """
        
        elif room_config.room_id == 'room_3':  # Exploratory + Aware
            base_content['description'] = """
            🔧 Current AI Settings:
            • Temperature: 0.8 (High creativity/Lower consistency)
            • Style: Exploratory and creative guidance
            
            What this means for you:
            • The AI provides more varied, creative suggestions
            • Responses encourage experimentation and unusual word choices
            • Guidance is more adaptive and surprising
            """
        
        return base_content
    
    def analyze_parameter_understanding(self, user_response: str) -> Dict[str, str]:
        """Analyze user's understanding of parameter effects"""
        understanding_keywords = {
            'high': ['understand', 'makes sense', 'I see', 'clear', 'got it', 'helpful'],
            'medium': ['think so', 'maybe', 'interesting', 'okay', 'sort of'],
            'low': ['confused', "don't understand", 'unclear', 'what does that mean', 'help']
        }
        
        for level, keywords in understanding_keywords.items():
            if any(keyword in user_response.lower() for keyword in keywords):
                return {'level': level, 'keywords_found': keywords}
        
        return {'level': 'medium', 'keywords_found': []}
    
    async def generate_enhanced_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Generate comprehensive session summary with all v2.1 features"""
        if session_id not in self.active_sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.active_sessions[session_id]
        
        # Get comprehensive report from logger
        logger_report = self.logger.generate_enhanced_session_report(session_id)
        
        # Add session manager specific insights
        session_manager_insights = {
            'form_selection_analysis': {
                'forms_explored': len(session['session_memory']['forms_explored']),
                'selection_pattern': self.analyze_form_selection_pattern(session_id),
                'guidance_effectiveness': self.evaluate_form_guidance_effectiveness(session_id)
            },
            'creative_independence_analysis': {
                'final_independence_level': session['independence_level'],
                'independence_progression': self.analyze_independence_progression(session_id),
                'milestone_achievements': len(session['progress_milestones'])
            },
            'session_memory_utilization': {
                'memory_items_created': len(session['session_memory']['poems_created']),
                'preferences_learned': len(session['session_memory']['user_preferences']),
                'progress_summaries_generated': len(session['session_memory']['progress_summaries'])
            }
        }
        
        # Combine all insights
        comprehensive_summary = {
            **logger_report,
            'session_manager_insights': session_manager_insights,
            'enhanced_features_effectiveness': self.evaluate_enhanced_features_effectiveness(session_id),
            'research_recommendations': self.generate_research_recommendations(session_id)
        }
        
        return comprehensive_summary

# Example usage and testing
if __name__ == "__main__":
    import asyncio
    
    async def test_enhanced_session():
        manager = EnhancedPoetrySessionManager()
        
        # Create enhanced session
        session_id, session_data = await manager.create_enhanced_session(
            participant_id="TEST_PARTICIPANT_001",
            room_type="room_1_structured_aware"
        )
        
        print(f"Enhanced session created: {session_id}")
        
        # Test form selection
        form_response = await manager.handle_poetry_form_selection(
            session_id=session_id,
            user_message="I want to write about nature and morning sunshine"
        )
        print(f"Form selection response: {form_response}")
        
        # Test creative independence tracking
        independence_analysis = await manager.process_creative_independence_moment(
            session_id=session_id,
            user_message="I think the sunrise looks like golden honey",
            ai_response="I love how you chose the word 'honey' - that's such a unique way to describe sunlight! What other creative comparisons come to mind?"
        )
        print(f"Creative independence analysis: {independence_analysis}")
        
        # Test progress summary generation
        progress_summary = await manager.generate_progress_summary(
            session_id=session_id,
            trigger="poem_completion"
        )
        print(f"Progress summary: {progress_summary}")
        
        # Test parameter awareness interface
        parameter_response = await manager.handle_parameter_awareness_interface(
            session_id=session_id,
            user_interaction="That's interesting! So the AI is set to be more structured and consistent?"
        )
        print(f"Parameter awareness response: {parameter_response}")
        
        # Generate final comprehensive summary
        final_summary = await manager.generate_enhanced_session_summary(session_id)
        print("Enhanced session summary generated successfully!")
        print(f"Summary keys: {list(final_summary.keys())}")
    
    # Run the test
    asyncio.run(test_enhanced_session())