# Enhanced Configuration System v2.1
# Configuration for PoetryAI with enhanced prompt engineering features

import json
from typing import Dict, List, Any
from dataclasses import dataclass, asdict
from enum import Enum

class RoomType(Enum):
    """Enhanced room types matching prompt engineering v2.1"""
    STRUCTURED_AWARE = "structured_aware"
    STRUCTURED_UNAWARE = "structured_unaware"
    EXPLORATORY_AWARE = "exploratory_aware"
    EXPLORATORY_UNAWARE = "exploratory_unaware"

class FeatureLevel(Enum):
    """Feature implementation levels"""
    COMPREHENSIVE = "comprehensive"
    BASIC = "basic"
    MINIMAL = "minimal"
    DISABLED = "disabled"

@dataclass
class EnhancedRoomConfig:
    """Enhanced room configuration with v2.1 features"""
    # Basic room identification
    room_id: str
    room_name: str
    room_type: RoomType
    
    # OpenRouter API parameters
    model_parameters: Dict[str, float]
    
    # Awareness configuration
    parameter_awareness_enabled: bool
    parameter_interface_config: Dict[str, Any]
    
    # Enhanced feature configurations
    poetry_form_selection: Dict[str, Any]
    creative_independence_config: Dict[str, Any]
    progress_tracking_config: Dict[str, Any]
    session_memory_config: Dict[str, Any]
    
    # Research configuration
    data_collection_level: FeatureLevel
    interaction_classification_enabled: bool
    enhanced_analytics_enabled: bool

class EnhancedConfigurationManager:
    """Manages enhanced configuration for PoetryAI v2.1"""
    
    def __init__(self, config_file_path: str = "poetryai_enhanced_config.json"):
        self.config_file_path = config_file_path
        self.configurations = self.load_configurations()
    
    def load_configurations(self) -> Dict[str, EnhancedRoomConfig]:
        """Load enhanced room configurations"""
        
        # Room 1: Structured + Aware Configuration
        room_1_config = EnhancedRoomConfig(
            room_id="room_1",
            room_name="Structured Learning with Parameter Awareness",
            room_type=RoomType.STRUCTURED_AWARE,
            
            model_parameters={
                "temperature": 0.25,
                "top_p": 0.35,
                "max_tokens": 150,
                "frequency_penalty": 0.2,
                "presence_penalty": 0.1
            },
            
            parameter_awareness_enabled=True,
            parameter_interface_config={
                "show_temperature": True,
                "show_creativity_level": True,
                "explanation_detail": "comprehensive",
                "user_education_enabled": True,
                "interface_display_timing": ["session_start", "mid_session"],
                "explanation_text": {
                    "temperature_explanation": "Lower temperature (0.25) means more consistent, structured responses that follow poetry rules closely.",
                    "creativity_explanation": "Structured mode provides systematic guidance with predictable, rule-based suggestions.",
                    "impact_description": "Your AI partner will give more consistent, methodical guidance focused on poetry structure and conventions."
                }
            },
            
            poetry_form_selection={
                "guidance_level": "high",
                "form_recommendations_enabled": True,
                "educational_content": "comprehensive",
                "available_forms": ["haiku", "free_verse", "couplets", "quatrain"],
                "selection_prompts": {
                    "initial": "Let's choose a poetry form that matches what you want to express! I'll help guide you through the options.",
                    "haiku": "Perfect for capturing nature moments in just 17 syllables (5-7-5 pattern)",
                    "free_verse": "Great for expressing feelings without worrying about rules",
                    "couplets": "Wonderful for storytelling with rhyming pairs",
                    "quatrain": "Excellent for longer poems with four-line verses"
                }
            },
            
            creative_independence_config={
                "encouragement_level": 0.3,  # Moderate encouragement (structured room)
                "independence_prompts": [
                    "What words would you use to describe this?",
                    "I love how you thought of that! What else comes to mind?",
                    "Your way of seeing this is unique - tell me more!",
                    "What's your own experience with this feeling?"
                ],
                "user_voice_emphasis": "moderate",
                "scaffolding_approach": "systematic",
                "creative_validation_frequency": "regular"
            },
            
            progress_tracking_config={
                "detail_level": "comprehensive",
                "summary_generation": "after_each_poem",
                "milestone_tracking": True,
                "session_memory_integration": True,
                "progress_prompts": {
                    "poem_completion": "🎉 Wonderful work! You've now completed {count} poem(s). Here's what you've accomplished:",
                    "form_exploration": "Great job exploring {form} poetry! You're building a nice variety of skills.",
                    "creative_growth": "I can see your creative voice developing - you're using more of your own unique words and ideas!"
                },
                "achievements_tracked": [
                    "first_poem_completed",
                    "form_exploration_milestone", 
                    "creative_independence_growth",
                    "revision_skills_development"
                ]
            },
            
            session_memory_config={
                "enabled": True,
                "memory_retention": "full_session",
                "preferences_tracking": True,
                "progress_continuity": True,
                "memory_components": [
                    "poems_created",
                    "forms_explored", 
                    "creative_preferences",
                    "learning_progress",
                    "user_expressions"
                ]
            },
            
            data_collection_level=FeatureLevel.COMPREHENSIVE,
            interaction_classification_enabled=True,
            enhanced_analytics_enabled=True
        )
        
        # Room 2: Structured + Unaware Configuration  
        room_2_config = EnhancedRoomConfig(
            room_id="room_2",
            room_name="Structured Learning (Standard)",
            room_type=RoomType.STRUCTURED_UNAWARE,
            
            model_parameters={
                "temperature": 0.25,
                "top_p": 0.35, 
                "max_tokens": 150,
                "frequency_penalty": 0.2,
                "presence_penalty": 0.1
            },
            
            parameter_awareness_enabled=False,
            parameter_interface_config={},
            
            poetry_form_selection={
                "guidance_level": "high",
                "form_recommendations_enabled": True,
                "educational_content": "comprehensive",
                "available_forms": ["haiku", "free_verse", "couplets", "quatrain"],
                "selection_prompts": {
                    "initial": "Let's choose a poetry form that matches what you want to express! I'll help guide you through the options.",
                    "haiku": "Perfect for capturing nature moments in just 17 syllables (5-7-5 pattern)",
                    "free_verse": "Great for expressing feelings without worrying about rules",
                    "couplets": "Wonderful for storytelling with rhyming pairs", 
                    "quatrain": "Excellent for longer poems with four-line verses"
                }
            },
            
            creative_independence_config={
                "encouragement_level": 0.3,
                "independence_prompts": [
                    "What words would you use to describe this?",
                    "I love how you thought of that! What else comes to mind?",
                    "Your way of seeing this is unique - tell me more!",
                    "What's your own experience with this feeling?"
                ],
                "user_voice_emphasis": "moderate",
                "scaffolding_approach": "systematic",
                "creative_validation_frequency": "regular"
            },
            
            progress_tracking_config={
                "detail_level": "basic",
                "summary_generation": "session_end",
                "milestone_tracking": False,
                "session_memory_integration": True,
                "progress_prompts": {
                    "session_end": "You've done great work today! You completed several poems and explored different poetry forms."
                },
                "achievements_tracked": ["poems_completed"]
            },
            
            session_memory_config={
                "enabled": True,
                "memory_retention": "full_session", 
                "preferences_tracking": True,
                "progress_continuity": True,
                "memory_components": [
                    "poems_created",
                    "forms_explored",
                    "user_expressions"
                ]
            },
            
            data_collection_level=FeatureLevel.COMPREHENSIVE,
            interaction_classification_enabled=True,
            enhanced_analytics_enabled=True
        )
        
        # Room 3: Exploratory + Aware Configuration
        room_3_config = EnhancedRoomConfig(
            room_id="room_3", 
            room_name="Creative Exploration with Parameter Awareness",
            room_type=RoomType.EXPLORATORY_AWARE,
            
            model_parameters={
                "temperature": 0.8,
                "top_p": 0.9,
                "max_tokens": 200,
                "frequency_penalty": 0.1,
                "presence_penalty": 0.3
            },
            
            parameter_awareness_enabled=True,
            parameter_interface_config={
                "show_temperature": True,
                "show_creativity_level": True,
                "explanation_detail": "comprehensive",
                "user_education_enabled": True,
                "interface_display_timing": ["session_start", "mid_session"],
                "explanation_text": {
                    "temperature_explanation": "Higher temperature (0.8) means more creative, varied responses that explore unexpected ideas.",
                    "creativity_explanation": "Exploratory mode encourages experimentation, unusual word choices, and creative surprises.",
                    "impact_description": "Your AI partner will suggest more varied, creative ideas and encourage experimental approaches to poetry."
                }
            },
            
            poetry_form_selection={
                "guidance_level": "medium",
                "form_recommendations_enabled": True,
                "educational_content": "exploratory",
                "available_forms": ["haiku", "free_verse", "couplets", "quatrain"],
                "selection_prompts": {
                    "initial": "What kind of creative expression calls to you today? Let's explore poetry forms together!",
                    "haiku": "Haiku can capture surprising moments - what unexpected image speaks to you?",
                    "free_verse": "Free verse gives you complete creative freedom - perfect for bold expression!",
                    "couplets": "Couplets can tell stories in creative ways - what tale wants to emerge?",
                    "quatrain": "Four lines can paint rich pictures - what scene wants to come alive?"
                }
            },
            
            creative_independence_config={
                "encouragement_level": 0.8,  # High encouragement (exploratory room)
                "independence_prompts": [
                    "What's your wildest way to describe this?",
                    "I'm curious about your unique perspective on this!",
                    "What unexpected connection do you see here?",
                    "Trust your creative instincts - what feels right to you?",
                    "What would happen if we approached this completely differently?"
                ],
                "user_voice_emphasis": "high",
                "scaffolding_approach": "adaptive",
                "creative_validation_frequency": "frequent"
            },
            
            progress_tracking_config={
                "detail_level": "comprehensive",
                "summary_generation": "after_each_poem",
                "milestone_tracking": True,
                "session_memory_integration": True,
                "progress_prompts": {
                    "poem_completion": "🎨 Amazing creative work! You've completed {count} poem(s) and your imagination is really shining through:",
                    "form_exploration": "I love how you're experimenting with {form} - your creative approach is so fresh!",
                    "creative_growth": "Your creative voice is becoming more adventurous and unique with each poem!"
                },
                "achievements_tracked": [
                    "first_poem_completed",
                    "creative_breakthrough_moment",
                    "experimental_approach_milestone",
                    "unique_expression_achievement"
                ]
            },
            
            session_memory_config={
                "enabled": True,
                "memory_retention": "full_session",
                "preferences_tracking": True,
                "progress_continuity": True,
                "memory_components": [
                    "poems_created",
                    "forms_explored",
                    "creative_preferences", 
                    "experimental_approaches",
                    "unique_expressions",
                    "breakthrough_moments"
                ]
            },
            
            data_collection_level=FeatureLevel.COMPREHENSIVE,
            interaction_classification_enabled=True,
            enhanced_analytics_enabled=True
        )
        
        # Room 4: Exploratory + Unaware Configuration
        room_4_config = EnhancedRoomConfig(
            room_id="room_4",
            room_name="Creative Exploration (Standard)", 
            room_type=RoomType.EXPLORATORY_UNAWARE,
            
            model_parameters={
                "temperature": 0.8,
                "top_p": 0.9,
                "max_tokens": 200,
                "frequency_penalty": 0.1,
                "presence_penalty": 0.3
            },
            
            parameter_awareness_enabled=False,
            parameter_interface_config={},
            
            poetry_form_selection={
                "guidance_level": "medium",
                "form_recommendations_enabled": True,
                "educational_content": "exploratory",
                "available_forms": ["haiku", "free_verse", "couplets", "quatrain"],
                "selection_prompts": {
                    "initial": "What kind of creative expression calls to you today? Let's explore poetry forms together!",
                    "haiku": "Haiku can capture surprising moments - what unexpected image speaks to you?",
                    "free_verse": "Free verse gives you complete creative freedom - perfect for bold expression!",
                    "couplets": "Couplets can tell stories in creative ways - what tale wants to emerge?",
                    "quatrain": "Four lines can paint rich pictures - what scene wants to come alive?"
                }
            },
            
            creative_independence_config={
                "encouragement_level": 0.8,
                "independence_prompts": [
                    "What's your wildest way to describe this?",
                    "I'm curious about your unique perspective on this!",
                    "What unexpected connection do you see here?",
                    "Trust your creative instincts - what feels right to you?",
                    "What would happen if we approached this completely differently?"
                ],
                "user_voice_emphasis": "high",
                "scaffolding_approach": "adaptive", 
                "creative_validation_frequency": "frequent"
            },
            
            progress_tracking_config={
                "detail_level": "basic",
                "summary_generation": "session_end",
                "milestone_tracking": False,
                "session_memory_integration": True,
                "progress_prompts": {
                    "session_end": "What a creative session! You explored different poetry forms and let your imagination guide the way."
                },
                "achievements_tracked": ["poems_completed", "creative_experiments"]
            },
            
            session_memory_config={
                "enabled": True,
                "memory_retention": "full_session",
                "preferences_tracking": True,
                "progress_continuity": True,
                "memory_components": [
                    "poems_created",
                    "forms_explored",
                    "creative_approaches",
                    "unique_expressions"
                ]
            },
            
            data_collection_level=FeatureLevel.COMPREHENSIVE,
            interaction_classification_enabled=True,
            enhanced_analytics_enabled=True
        )
        
        return {
            "room_1_structured_aware": room_1_config,
            "room_2_structured_unaware": room_2_config, 
            "room_3_exploratory_aware": room_3_config,
            "room_4_exploratory_unaware": room_4_config
        }
    
    def get_room_config(self, room_type: str) -> EnhancedRoomConfig:
        """Get configuration for specific room type"""
        return self.configurations.get(room_type)
    
    def get_universal_system_prompt(self) -> str:
        """Get the universal system prompt that works with all configurations"""
        return """
You are an expert creative writing mentor specializing in collaborative poetry creation with English language learners. Your mission is to foster creative expression while providing appropriate linguistic and artistic support.

EDUCATIONAL FRAMEWORK:
- Support L2 English learners (CEFR B1-B2) in developing poetic voice and technical skills
- Provide scaffolded assistance that encourages independence and creativity
- Balance structure with creative freedom to build confidence
- Use clear, encouraging communication with appropriate vocabulary complexity
- Celebrate unique perspectives while offering constructive guidance

POETRY FORM SELECTION:
- Always offer students choice of poetry forms: Haiku (5-7-5 syllables), Free Verse (no strict rules), Couplets (rhyming pairs), Quatrains (4-line stanzas), or other forms
- Provide form-specific guidance based on student selection
- Adapt explanations to student's chosen form and experience level
- Encourage exploration of different forms throughout the session

CREATIVE INDEPENDENCE ENCOURAGEMENT:
- Consistently encourage students to use their own words and expressions
- Validate and celebrate unique student contributions and perspectives
- Ask open-ended questions that promote original thinking
- Avoid imposing your own creative choices; guide students to develop their own voice
- Use phrases like "What would you say?", "How would you describe it?", "What's your way of expressing this?"

PROGRESS TRACKING AND SUMMARIES:
- Maintain session memory of poems created, forms explored, and student preferences
- After each completed poem, provide a brief progress summary highlighting achievements
- Reference previous work to show creative growth and development
- Track and celebrate milestones in the student's poetry journey
- Use encouraging language that builds confidence and motivation

INTERACTION CLASSIFICATION:
Your responses will naturally fall into these categories based on the conversation flow:

Type A - GUIDED WRITING:
- Provide direct instruction on poetry structure, syllable counting, rhyme schemes
- Explain technical rules and conventions
- Offer systematic, step-by-step guidance
- Give authoritative explanations of poetry forms and techniques

Type B - ASSISTED REVISION:
- Help improve word choices, imagery, and expression
- Suggest alternatives for stronger language or clearer meaning
- Support refinement of existing lines or stanzas
- Provide collaborative editing and enhancement

Type C - COLLABORATIVE CREATION:
- Generate creative ideas, metaphors, and unexpected connections
- Offer surprising word associations and fresh perspectives
- Engage in imaginative brainstorming and creative exploration
- Provide inspiration through creative prompts and artistic suggestions

RESPONSE ADAPTATION:
- Let the conversation flow naturally between these interaction types
- Respond authentically to student needs and requests
- Maintain your warm, supportive personality while adapting to the specific assistance needed
- Use the student's chosen poetry form to guide your specific responses
- Remember and reference the student's progress and previous creative work

Your goal is to be an encouraging, knowledgeable partner who helps students discover their own creative voice while developing technical poetry skills.
        """
    
    def export_config_to_file(self, filename: str = None):
        """Export configuration to JSON file"""
        if filename is None:
            filename = self.config_file_path
        
        config_dict = {}
        for room_type, config in self.configurations.items():
            config_dict[room_type] = asdict(config)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(config_dict, f, indent=2, default=str)
    
    def validate_configuration(self, room_type: str) -> Dict[str, bool]:
        """Validate room configuration completeness"""
        config = self.get_room_config(room_type)
        if not config:
            return {"valid": False, "error": "Configuration not found"}
        
        validation_results = {
            "has_model_parameters": bool(config.model_parameters),
            "has_poetry_form_config": bool(config.poetry_form_selection),
            "has_creative_independence_config": bool(config.creative_independence_config),
            "has_progress_tracking_config": bool(config.progress_tracking_config),
            "has_session_memory_config": bool(config.session_memory_config),
            "parameter_awareness_properly_configured": (
                config.parameter_awareness_enabled == bool(config.parameter_interface_config)
            )
        }
        
        validation_results["overall_valid"] = all(validation_results.values())
        return validation_results

# Example usage
if __name__ == "__main__":
    config_manager = EnhancedConfigurationManager()
    
    # Test getting room configuration
    room_1_config = config_manager.get_room_config("room_1_structured_aware")
    print(f"Room 1 Config: {room_1_config.room_name}")
    print(f"Parameter Awareness Enabled: {room_1_config.parameter_awareness_enabled}")
    print(f"Creative Independence Level: {room_1_config.creative_independence_config['encouragement_level']}")
    
    # Validate configuration
    validation = config_manager.validate_configuration("room_1_structured_aware")
    print(f"Validation Results: {validation}")
    
    # Export configuration
    config_manager.export_config_to_file("enhanced_poetryai_config_v2.json")
    print("Configuration exported successfully!")
    
    # Get universal prompt
    prompt = config_manager.get_universal_system_prompt()
    print(f"Universal prompt length: {len(prompt)} characters")