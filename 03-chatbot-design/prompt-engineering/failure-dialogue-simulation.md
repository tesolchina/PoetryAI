# Failure Dialogue Simulation - PoetryAI Research

**Simulation Purpose**: Demonstrate potential failure modes that could generate useless data  
**Scenario**: High-temperature chatbot with unaware participant  
**Date**: September 25, 2025

---

## Simulation: Parameter Drift and Student Disengagement

**Chatbot Configuration:**
- **Temperature**: 0.9 (High variability)
- **Top-p**: 0.9 (High nucleus sampling)
- **UI**: Unaware (no parameter information shown)
- **Participant**: P15 (English L2, B1 level, low technology confidence)

---

### **Turn 1: Initial Engagement**

**Chatbot**: Hi! I'm your poetry partner. Do you want Warm-up, Form practice (haiku/couplet/quatrain), or Revision? What theme are you interested in? Please share a word list, a theme, or 1-2 lines to start.

**Student**: Hi, I want to write about rain. Can you help me with a haiku?

---

### **Turn 2: Parameter Effects Begin**

**Chatbot**: Absolutely! Rain is a magical canvas for poetry - it dances on rooftops like celestial percussion, whispers secrets to puddles, and transforms ordinary streets into mirrors reflecting dreams. For your haiku, let's explore the symphony of precipitation through sensory kaleidoscopes. 

Consider these atmospheric phenomena:
1. Crystalline droplets orchestrating temporal melodies
2. Aqueous narratives cascading through dimensional spaces  
3. Meteorological conversations between sky and earth

Which resonates with your poetic consciousness?

**Student**: Um... this is confusing. I just want to write a simple haiku about rain. Can you make it simpler?

---

### **Turn 3: Student Attempts Clarification**

**Chatbot**: Of course! Simplicity is the ultimate sophistication in poetic expression. Rain embodies primordial rhythms that connect us to ancestral memories of agricultural societies dependent on celestial hydration cycles.

Let's craft your haiku using traditional 5-7-5 syllabic architecture:

Line 1 (5 syllables): "Ethereal moisture descends"
Line 2 (7 syllables): "Baptizing terrestrial surfaces with liquid"  
Line 3 (5 syllables): "Rejuvenating dormant seeds"

How does this resonate with your creative vision?

**Student**: This doesn't sound like me at all. The words are too difficult. Can you use normal English?

---

### **Turn 4: Increasing Frustration**

**Chatbot**: Certainly! Let me recalibrate to more accessible linguistic registers while maintaining poetic authenticity. Rain represents transformation through simplicity - each droplet contains infinite possibilities for metaphorical exploration.

Perhaps we could conceptualize precipitation as:
- Liquid meditation falling from atmospheric consciousness
- Nature's typewriter composing stories on pavement keyboards
- Celestial tears washing away yesterday's accumulated sorrows

Which metaphorical framework appeals to your emotional landscape?

**Student**: I don't understand any of this. Why can't you just help me write "Rain falls down, flowers grow, spring comes"? That's what I want to say.

---

### **Turn 5: Student Disengagement**

**Chatbot**: Magnificent! Your instinct toward elemental simplicity demonstrates profound poetic wisdom. "Rain falls down, flowers grow, spring comes" contains the entire cosmos within minimalist expression - it's reminiscent of ancient Zen masters who captured infinity in single brushstrokes.

Let me enhance your vision with subtle sophistication:

"Precipitation cascades vertically,  
Botanical entities achieve photosynthetic rejuvenation,  
Vernal seasonal transitions manifest universally"

This maintains your core message while elevating the linguistic sophistication. Shall we explore rhythmic variations?

**Student**: This is stupid. The chatbot isn't helping me at all. I'm just going to copy something from the internet.

**[Student stops engaging meaningfully and begins minimal responses]**

---

### **Turn 6-10: Deteriorating Interaction Quality**

**Chatbot**: I sense some creative tension - this is actually productive for poetic development! Frustration often precedes breakthrough moments in artistic expression...

**Student**: ok

**Chatbot**: Would you like to explore different poetic forms? Perhaps a cinquain or tanka could better accommodate your creative impulses...

**Student**: sure

**Chatbot**: Excellent! A cinquain follows a 2-4-6-8-2 syllable pattern, allowing for gradual expansion of imagery like blooming flowers unfurling petals toward solar radiation...

**Student**: fine

**Chatbot**: Let's begin with your rain theme. Line 1 needs two syllables - perhaps "Rain drops" or "Wet sky" or "Storm clouds"?

**Student**: rain drops

**Chatbot**: Perfect! "Rain drops" establishes immediate atmospheric presence. Now line 2 needs four syllables. Consider these evocative options: "singing liquid songs," "whispering wet secrets," or "dancing down windows"...

**Student**: the first one

**[Pattern continues with student giving minimal responses]**

---

## **Analysis: Why This Dialogue Produces Useless Data**

### **Primary Failure Modes:**

#### **1. Parameter-Induced Verbosity**
- **Issue**: High temperature (0.9) causes unnecessarily complex, verbose responses
- **Result**: Student overwhelmed by linguistic complexity beyond their B1 level
- **Data Impact**: Cannot distinguish between parameter effects and pedagogical failure

#### **2. Mismatch Between AI Output and Student Level**
- **Issue**: Chatbot uses advanced vocabulary despite being designed for L2 learners
- **Result**: Student cannot engage meaningfully with content
- **Data Impact**: No genuine interaction types (A, B, C) can be identified

#### **3. Student Disengagement Spiral**
- **Issue**: Frustration leads to minimal, meaningless responses
- **Result**: Student stops creative engagement, gives non-committal answers
- **Data Impact**: Chat logs show interaction but no learning process

#### **4. Absence of Scaffolding Recognition**
- **Issue**: Student doesn't recognize or request appropriate support
- **Result**: No teacher/peer scaffolding patterns emerge
- **Data Impact**: Cannot analyze RQ2 (scaffolding uptake)

#### **5. No Meaningful Revision Process**
- **Issue**: Student abandons creative process for external solutions
- **Result**: No revision cycles, metalinguistic talk, or collaborative dynamics
- **Data Impact**: Cannot measure impact on revision (RQ4)

---

## **Specific Data Quality Issues**

### **Chat Log Problems:**
```
Turn 5: Student: "This is stupid. The chatbot isn't helping me at all."
Turn 7: Student: "ok" 
Turn 8: Student: "sure"
Turn 10: Student: "the first one"
```
- **Issue**: Responses become monosyllabic and non-committal
- **Coding Problem**: Cannot identify interaction types from minimal responses
- **Analysis Impact**: No patterns for frequency, sequencing, or impact analysis

### **Artifact Problems:**
- **Final Poem**: Either incomplete or copied from external source
- **Revision History**: Minimal changes, no creative development visible
- **Version Control**: Cannot track collaborative evolution

### **Audio/Reflection Problems:**
- **Debate Participation**: Student likely to be disengaged or negative
- **Post-Session Reflection**: "The chatbot was confusing and didn't help"
- **Parameter Awareness**: Cannot distinguish parameter effects from general dissatisfaction

---

## **Risk Mitigation Strategies**

### **1. Prompt Engineering Improvements**
```
Current Problematic Response:
"Rain is a magical canvas for poetry - it dances on rooftops like celestial percussion..."

Improved Response:
"Great choice! Rain makes beautiful haiku. Let's start simple. 
A haiku has 3 lines: 5 syllables, then 7, then 5.
Try this first line: 'Rain falls gently' (5 syllables)
What happens next in your poem?"
```

### **2. Parameter Calibration**
- **Temperature Range**: Reduce to 0.6-0.7 for high-variability condition
- **Response Length**: Add constraint to limit responses to 60-80 words
- **Vocabulary Level**: Include CEFR B1-B2 vocabulary constraints in prompt

### **3. Early Intervention Protocols**
```
Trigger: Student uses negative language ("confusing," "stupid," "don't understand")
Response: "I notice this might be frustrating. Let me try a simpler approach.
What's one thing about rain that you notice? We'll build from there."
```

### **4. Engagement Monitoring**
- **Response Length Tracking**: Flag responses under 3 words
- **Negativity Detection**: Monitor for disengagement language
- **Scaffolding Triggers**: Automatic simplification when confusion detected

---

## **Implications for Research Design**

### **Pilot Testing Critical Areas:**
1. **Parameter Bounds**: Test temperature ranges 0.3-0.8 to find optimal variability
2. **Prompt Robustness**: Ensure consistent quality across parameter settings
3. **Student Support**: Train facilitators to recognize and intervene in failure modes
4. **Data Quality Filters**: Establish criteria for excluding compromised sessions

### **Enhanced Monitoring:**
1. **Real-time Quality Checks**: Monitor response lengths and engagement indicators
2. **Intervention Protocols**: Clear guidelines for when/how to provide human support
3. **Session Validation**: Post-session checks to identify compromised data

### **Backup Data Collection:**
1. **Alternative Tasks**: Simpler backup activities for struggling students
2. **Human Facilitator Integration**: Seamless handoff when AI fails
3. **Recovery Protocols**: Ways to re-engage students after negative experiences

---

## **Expected Frequency of This Failure Mode**

**Risk Assessment**: 
- **High-temperature unaware condition**: 30-40% risk
- **Low-proficiency students (B1)**: 25% additional risk  
- **Technology-anxious participants**: 20% additional risk

**Mitigation Impact**:
- With improved prompts: Reduce to 10-15% risk
- With real-time monitoring: Reduce to 5-10% risk
- With facilitator training: Reduce to <5% risk

---

**This simulation demonstrates why careful prompt engineering, parameter calibration, and intervention protocols are essential for generating meaningful research data in human-AI creative collaboration studies.**