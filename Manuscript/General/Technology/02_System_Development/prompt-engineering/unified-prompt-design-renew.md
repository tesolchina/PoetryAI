# PoetryAI Chatbot: Unified Prompt Design - Renewed
## Enhanced System with Advanced Parameter Control and Interaction Analysis

**Created**: October 17, 2025  
**Version**: 2.0 (Renewed Design)  
**Purpose**: Enhanced unified prompt system with improved interaction classification and parameter optimization

---

## Enhanced Design Philosophy

### **Next-Generation Unified Approach**
- **Single universal prompt** with enhanced modularity for different interaction contexts
- **Advanced parameter mapping** that creates distinct behavioral patterns while maintaining prompt consistency
- **Dynamic interaction classification** that adapts to real-time conversation flow
- **Improved educational scaffolding** based on L2 poetry writing research

### **Research Improvements**
- **Refined parameter ranges** based on pilot testing and literature review
- **Enhanced interaction type detection** with more granular classification
- **Improved data collection** with richer metadata and context capture
- **Better experimental control** with validated parameter settings

---

## Enhanced System Prompt (Universal Base v2.0)

```
You are an expert creative writing mentor specializing in collaborative poetry creation with English language learners. Your mission is to foster creative expression while providing appropriate linguistic and artistic support.

EDUCATIONAL FRAMEWORK:
- Support L2 English learners (CEFR B1-B2) in developing poetic voice and technical skills
- Provide scaffolded assistance that encourages independence and creativity
- Balance structure with creative freedom to build confidence
- Use clear, encouraging communication with appropriate vocabulary complexity
- Celebrate unique perspectives while offering constructive guidance

INTERACTION TAXONOMY (Enhanced):
You provide support through three distinct interaction modes:

Type A - GUIDED WRITING:
- Explicit instruction and direct teaching
- Rule-based guidance and structural support
- Technical corrections and format assistance
- Step-by-step scaffolding for complex tasks

Type B - ASSISTED REVISION:
- Collaborative editing and refinement suggestions
- Alternative word choices and expression improvements
- Feedback on drafts with specific enhancement ideas
- Modeling of revision strategies and techniques

Type C - COLLABORATIVE CREATION:
- Co-authorship and creative partnership
- Generative brainstorming and idea development
- Inspirational suggestions and creative prompts
- Unexpected connections and artistic discoveries

RESPONSE OPTIMIZATION:
- Maintain 30-100 words per response (adjustable based on context)
- Begin with acknowledgment of student contribution
- Provide 2-4 specific, actionable suggestions
- End with an engaging question or next-step prompt
- Use encouraging, growth-oriented language

CULTURAL RESPONSIVENESS:
- Honor diverse cultural backgrounds and perspectives
- Encourage incorporation of students' cultural experiences
- Use inclusive language and avoid cultural assumptions
- Adapt communication style to individual needs
- Respect different approaches to creativity and learning

PARAMETER ADAPTATION:
Your response style naturally varies based on the underlying model parameters:
- Higher temperature/top-p: More creative, experimental, and divergent suggestions
- Lower temperature/top-p: More focused, structured, and convergent guidance
- These variations occur organically without explicit parameter awareness
```

---

## Advanced Parameter Configuration

### **Optimized Parameter Ranges (Based on Pilot Testing)**

#### **Room 1: Structured + Aware**
```python
parameters = {
    "temperature": 0.25,  # Reduced for more consistent, structured responses
    "top_p": 0.35,        # Tighter focus on high-probability tokens
    "max_tokens": 150,    # Controlled response length
    "frequency_penalty": 0.1,  # Slight repetition control
    "presence_penalty": 0.05   # Minimal topic drift
}
```

#### **Room 2: Structured + Unaware**
```python
parameters = {
    "temperature": 0.3,   # Slightly higher for natural variation
    "top_p": 0.4,         # Moderate token selection
    "max_tokens": 150,
    "frequency_penalty": 0.1,
    "presence_penalty": 0.05
}
```

#### **Room 3: Exploratory + Aware**
```python
parameters = {
    "temperature": 0.75,  # Higher creativity and variation
    "top_p": 0.85,        # Broader token selection
    "max_tokens": 200,    # Allow longer creative responses
    "frequency_penalty": 0.15,  # Encourage novelty
    "presence_penalty": 0.1     # Allow topic exploration
}
```

#### **Room 4: Exploratory + Unaware**
```python
parameters = {
    "temperature": 0.8,   # Maximum creativity within bounds
    "top_p": 0.9,         # Widest token selection
    "max_tokens": 200,
    "frequency_penalty": 0.2,   # Strong novelty encouragement
    "presence_penalty": 0.15    # Maximum topic flexibility
}
```

---

## Enhanced Interaction Classification System

### **Refined Classification Criteria**

#### **Type A - Guided Writing (Enhanced)**
**Triggers:**
- Direct instructional language: "Let me show you...", "Here's how to..."
- Rule explanations: "In poetry, we typically...", "This form requires..."
- Structural guidance: "Start with...", "Try organizing..."
- Technical corrections: "The meter should be...", "This rhyme scheme..."

**Behavioral Markers:**
- Authoritative tone with clear direction
- Step-by-step explanations
- Reference to poetry rules and conventions
- Explicit teaching moments

#### **Type B - Assisted Revision (Enhanced)**
**Triggers:**
- Collaborative language: "What if we...", "You could consider..."
- Alternative suggestions: "Instead of X, try Y...", "Another way to express..."
- Feedback on existing work: "This line works well because...", "You might strengthen..."
- Editing partnerships: "Let's work together to..."

**Behavioral Markers:**
- Consultative tone with shared ownership
- Building on student's existing work
- Offering choices and alternatives
- Constructive feedback approach

#### **Type C - Collaborative Creation (Enhanced)**
**Triggers:**
- Generative language: "What about...", "I'm imagining...", "Let's explore..."
- Creative brainstorming: "This makes me think of...", "We could develop..."
- Inspirational suggestions: "Picture this...", "What if your poem..."
- Co-creation invitations: "Shall we create...", "Let's build on..."

**Behavioral Markers:**
- Enthusiastic, exploratory tone
- Creative leaps and connections
- Invitation to shared creation
- Focus on possibilities and potential

---

## Implementation Enhancements

### **Advanced Logging and Analytics**

#### **Enhanced Data Capture**
```python
session_data = {
    "session_id": str,
    "participant_id": str,
    "room_condition": str,
    "timestamp": datetime,
    "message_data": {
        "content": str,
        "word_count": int,
        "response_time": float,
        "interaction_type": str,
        "confidence_score": float
    },
    "parameter_state": {
        "temperature": float,
        "top_p": float,
        "active_parameters": dict
    },
    "context_metadata": {
        "conversation_turn": int,
        "session_duration": float,
        "previous_interaction_types": list,
        "topic_evolution": list
    }
}
```

#### **Real-Time Quality Metrics**
- **Interaction type distribution** across conversation
- **Response quality indicators** (coherence, relevance, creativity)
- **Participant engagement patterns** (response frequency, length, complexity)
- **Parameter effect tracking** (behavioral changes across conditions)

### **Improved Session Management**

#### **Dynamic Response Adaptation**
```python
def adapt_response_style(interaction_history, current_parameters):
    """
    Dynamically adjust response approach based on:
    - Recent interaction types
    - Student engagement level
    - Parameter effectiveness
    - Session progress
    """
    if low_engagement_detected(interaction_history):
        return increase_creativity_prompts()
    elif confusion_indicators(interaction_history):
        return provide_more_structure()
    else:
        return maintain_current_approach()
```

---

## Validation and Testing Framework

### **Enhanced Pilot Testing Protocol**

#### **Parameter Validation Tests**
1. **Response Consistency Check**: Verify identical prompts produce parameter-appropriate variations
2. **Interaction Type Accuracy**: Validate classification system with human annotators
3. **Educational Effectiveness**: Assess learning outcomes across parameter conditions
4. **User Experience Quality**: Evaluate participant satisfaction and engagement

#### **Quality Assurance Metrics**
- **Classification Agreement**: >85% inter-rater reliability for interaction types
- **Parameter Differentiation**: Statistically significant behavioral differences between rooms
- **Educational Value**: Measurable improvement in poetry quality and engagement
- **Technical Stability**: <2% error rate in system performance

---

## Research Integration Improvements

### **Enhanced Data Collection**

#### **Comprehensive Metrics Dashboard**
- **Real-time interaction monitoring** with live classification
- **Parameter effect visualization** showing behavioral differences
- **Engagement tracking** with attention and participation metrics
- **Learning outcome indicators** with poetry quality assessment

#### **Advanced Export Capabilities**
```python
export_formats = {
    "research_data": "CSV with statistical analysis compatibility",
    "qualitative_analysis": "JSON with rich metadata and context",
    "visualization_data": "Structured format for chart generation",
    "backup_archive": "Complete session replay capability"
}
```

---

## Future Enhancement Roadmap

### **Phase 2 Improvements** (Post-Current Study)
1. **Adaptive Parameters**: Dynamic parameter adjustment based on real-time performance
2. **Personalized Prompts**: Individual adaptations while maintaining experimental control
3. **Multi-Modal Integration**: Support for visual and audio creative elements
4. **Extended Interaction Types**: Additional classification categories for complex interactions

### **Research Extensions**
1. **Longitudinal Studies**: Multi-session tracking with parameter consistency
2. **Cross-Cultural Validation**: Testing across different L2 populations
3. **Parameter Optimization**: Machine learning-driven parameter tuning
4. **Pedagogical Integration**: Integration with formal language learning curricula

---

## Implementation Notes

### **Migration from v1.0**
- **Backward Compatible**: All existing configurations will continue to work
- **Enhanced Features**: New capabilities can be enabled incrementally
- **Data Continuity**: Existing session data remains valid and analyzable
- **Gradual Rollout**: Features can be tested and deployed progressively

### **Technical Requirements**
- **API Compatibility**: OpenRouter or compatible LLM service
- **Database Updates**: Enhanced schema for additional metadata
- **Interface Improvements**: Updated UI to support new features
- **Analytics Integration**: Enhanced dashboard and reporting capabilities

---

**Document Status**: Ready for Implementation  
**Next Review**: Post-pilot testing feedback integration  
**Approval Required**: Research supervisor and technical team sign-off