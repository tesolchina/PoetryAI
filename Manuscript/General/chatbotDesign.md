# Chatbot Design Specification for poe.com App Creator

## Executive Summary

This document provides technical specifications for building a chatbot mockup that simulates an AI-assisted poetry writing environment for English L2 learners. The system requires **four separate chat rooms** with distinct parameter configurations and interface variations to support a 2×2 factorial experimental design.

---

## 1. System Architecture Overview

### 1.1 Core Requirements

- **4 independent chat rooms** (Room 1, 2, 3, 4)
- **Unified backend** with room-specific parameter configurations
- **Session-based authentication** with room-specific access codes
- **Real-time conversation logging** with timestamps
- **50-minute session duration** with 5-minute warning system
- **Web-based interface** (React-based preferred)

### 1.2 Technical Stack (Reference)

- **Frontend**: React-based web application
- **Backend**: Node.js server
- **AI Integration**: GPT-4 via OpenRouter API (or compatible)
- **Database**: MySQL for interaction logging
- **Security**: HTTPS encryption, role-based access control

---

## 2. AI Parameter Configurations

### 2.1 Structured Configuration (Rooms 1 & 2)

**Purpose**: Generate coherent, predictable, educational outputs

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Temperature | 0.3 | Low randomness for consistent responses |
| Top-p | 0.4 | Narrow sampling for predictable outputs |

**Expected Behavior**: Systematic scaffolding, educational feedback, methodical responses favoring **Type A (Diagnosis → Repair)** and **Type B (Exemplar Pivot)** interactions.

### 2.2 Exploratory Configuration (Rooms 3 & 4)

**Purpose**: Generate creative, diverse, unexpected outputs

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Temperature | 0.8 | High randomness for creative variety |
| Top-p | 0.9 | Broad sampling for diverse outputs |

**Expected Behavior**: Creative combinations, unexpected suggestions, inspirational responses favoring **Type C (Surprise Harvest)** interactions.

---

## 3. Room Configuration Matrix

| Room | Parameter Setting | Awareness Condition | Interface Type |
|------|------------------|---------------------|----------------|
| **Room 1** | Structured (T=0.3, p=0.4) | **AWARE** | Show parameter settings with explanations |
| **Room 2** | Structured (T=0.3, p=0.4) | **UNAWARE** | Standard interface (no parameter visibility) |
| **Room 3** | Exploratory (T=0.8, p=0.9) | **AWARE** | Show parameter settings with explanations |
| **Room 4** | Exploratory (T=0.8, p=0.9) | **UNAWARE** | Standard interface (no parameter visibility) |

**Note**: Rooms 2 & 4 are the primary control groups for analyzing pure parameter effects.

---

## 4. System Prompt (Identical Across All Rooms)

```
You are an AI writing partner helping English L2 learners explore creative poetry composition. 
Your role is to collaborate respectfully while encouraging creative expression and language development.
Provide supportive guidance appropriate for intermediate English learners developing poetic voice.
Adapt your communication style to be encouraging, constructive, and culturally sensitive.
```

**Critical**: This prompt MUST be identical across all four rooms to control for content bias. Only parameter settings vary.

---

## 5. User Interface Specifications

### 5.1 Interface Variants

#### 5.1.1 UNAWARE Interface (Rooms 2 & 4)

**Design**: Standard creative writing chat interface

**Features**:
- Clean, minimalist design
- No parameter visibility
- Standard chat layout with user/AI message bubbles
- Session timer (non-intrusive)
- Poetry composition prompt at top
- Standard "Send" button

**UI Elements**:
```
┌────────────────────────────────────────┐
│  Poetry Writing Session - Room [X]    │
│  Time Remaining: 45:00                 │
├────────────────────────────────────────┤
│                                        │
│  [Poetry Prompt Display Area]         │
│                                        │
├────────────────────────────────────────┤
│                                        │
│  [Chat Message Area]                   │
│    User: [message]                     │
│    AI: [response]                      │
│                                        │
├────────────────────────────────────────┤
│  [Text Input Box]              [Send]  │
└────────────────────────────────────────┘
```

#### 5.1.2 AWARE Interface (Rooms 1 & 3)

**Design**: Enhanced interface with parameter transparency

**Additional Features**:
- **Parameter display panel** (collapsible sidebar or top banner)
- **Educational explanations** of temperature and top-p
- **Visual indicators** of current AI configuration
- All standard features from unaware interface

**UI Elements**:
```
┌────────────────────────────────────────────────────────┐
│  Poetry Writing Session - Room [X]                     │
│  Time Remaining: 45:00                                 │
├────────────────────────────────────────────────────────┤
│  ⚙️ AI Configuration                                   │
│  Temperature: [0.3/0.8] | Top-p: [0.4/0.9]            │
│  ℹ️ [Learn about these settings]                       │
├────────────────────────────────────────────────────────┤
│  [Poetry Prompt Display Area]                          │
├────────────────────────────────────────────────────────┤
│  [Chat Message Area]                                   │
│    User: [message]                                     │
│    AI: [response]                                      │
├────────────────────────────────────────────────────────┤
│  [Text Input Box]                              [Send]  │
└────────────────────────────────────────────────────────┘
```

**Parameter Explanation Text** (for Aware interfaces):

- **Temperature**: Controls creativity vs. consistency
  - Low (0.3): More predictable and focused responses
  - High (0.8): More creative and varied responses
  
- **Top-p**: Controls response diversity
  - Low (0.4): Narrower range of word choices
  - High (0.9): Broader range of possibilities

### 5.2 Common Interface Features (All Rooms)

1. **Welcome Screen**
   - Room-specific access code entry
   - Brief orientation message
   - "Start Session" button

2. **Session Timer**
   - Countdown from 50:00
   - **5-minute warning** (visual + audio alert optional)
   - Auto-save on session end

3. **Chat Interface**
   - **Clear turn-taking**: User messages on right, AI on left (or vice versa)
   - **Typing indicators**: Show when AI is generating response
   - **Timestamp display**: For each message
   - **Message history**: Full scrollable conversation

4. **Response Behavior**
   - **Standardized latency**: 2-3 second delay before AI response
   - **Natural pacing**: Simulate human-like response time

5. **Emergency Features**
   - "Technical Support" button
   - "Save and Pause" functionality
   - Session recovery protocols

---

## 6. Interaction Flow Architecture

### 6.1 Session Initialization Sequence

```
1. User Access
   ↓
2. Enter Room-Specific Access Code
   ↓
3. Display Welcome Interface
   - Room 1/3: Show parameter configuration
   - Room 2/4: Standard creative writing interface
   ↓
4. Present Poetry Composition Prompt
   ↓
5. Activate Real-Time Chat
   ↓
6. Begin Logging
```

### 6.2 Conversation Management

**Turn-Taking Protocol**:
- User sends message → AI typing indicator appears
- 2-3 second delay (simulated processing)
- AI response delivered
- Clear visual distinction between user/AI messages

**Session Duration**:
- **Total time**: 50 minutes
- **Warning**: At 45-minute mark (5 minutes remaining)
- **Auto-save**: At session end
- **Manual save**: Available throughout session

### 6.3 Data Capture Requirements

**Essential Logging** (for each message):
- Message content (user input / AI response)
- Precise timestamp (ISO 8601 format)
- Room number
- Parameter values (temperature, top-p)
- Session ID
- Participant ID (anonymized: P001-P020)

**Optional Analytics**:
- User typing speed
- Pause durations between messages
- Message length (character/word count)
- Turn count per session

---

## 7. Theoretical Framework: Three Interaction Types

### 7.1 Type A: Diagnosis → Repair

**Definition**: AI identifies issues and provides targeted suggestions

**Example Interactions**:
- AI points out meter inconsistencies
- AI suggests vocabulary alternatives
- AI identifies structural improvements

**Coding Indicators**:
- Corrective feedback language
- "You might consider..."
- "This line could be strengthened by..."

### 7.2 Type B: Exemplar Pivot

**Definition**: AI provides models/templates for student adaptation

**Example Interactions**:
- AI shares example poems
- AI provides structural templates
- AI offers comparative texts

**Coding Indicators**:
- "Here's an example..."
- "Poets often use..."
- Template or structure provision

### 7.3 Type C: Surprise Harvest

**Definition**: AI generates unexpected, inspirational suggestions

**Example Interactions**:
- Unusual word combinations
- Unexpected metaphorical connections
- Novel creative directions

**Coding Indicators**:
- Student expressions of surprise
- "I hadn't thought of that..."
- Creative pivots in conversation

---

## 8. Sample Poetry Prompts

**Example Prompt 1**: "Write a poem about a childhood memory using sensory details. Focus on at least three senses."

**Example Prompt 2**: "Create a poem exploring the concept of 'home' from the perspective of someone between two cultures."

**Example Prompt 3**: "Write a nature poem that uses personification to describe a specific season or weather phenomenon."

**Format**: Display prompt prominently at session start, with option to view it again during session.

---

## 9. Access Control & Authentication

### 9.1 Room-Specific Access Codes

Generate unique codes for each room and participant:

**Format**: `ROOM[X]-P[XXX]-[WEEK]`

**Example**: 
- `ROOM1-P001-W2` (Room 1, Participant 1, Week 2)
- `ROOM4-P015-W3` (Room 4, Participant 15, Week 3)

### 9.2 Authentication Flow

```
1. User enters access code
2. System validates code
3. Check participant eligibility
4. Load room-specific configuration
5. Initialize session with correct parameters
6. Begin logging with participant ID
```

---

## 10. Privacy & Security Features

### 10.1 Data Protection

- **Automatic anonymization**: Replace real names with coded identifiers
- **Secure transmission**: HTTPS for all communications
- **Access control**: Role-based permissions
- **Data retention**: Clear protocols for storage/deletion

### 10.2 Ethical Compliance Features

- **Consent verification**: Checkbox at session start
- **Withdrawal option**: "Exit Study" button with data deletion option
- **Transparency notice**: For unaware conditions (post-session)
- **Emergency contact**: Display research team contact info

---

## 11. Technical Requirements Summary

### 11.1 Essential Features for Mockup

✅ **Four independent chat rooms** with distinct configurations
✅ **Parameter visibility toggle** (Aware vs. Unaware)
✅ **Session timer** (50 min with 5-min warning)
✅ **Real-time chat** with user/AI alternation
✅ **Response delay** simulation (2-3 seconds)
✅ **Message logging** with timestamps
✅ **Access code authentication**
✅ **Identical system prompt** across rooms

### 11.2 Nice-to-Have Features

⭐ **Typing indicators** for AI responses
⭐ **Auto-save** functionality
⭐ **Session recovery** after disconnection
⭐ **Export conversation** option
⭐ **Parameter explanation tooltips** (Aware rooms)
⭐ **Behavioral analytics** (typing speed, pauses)

---

## 12. Testing & Validation Checklist

### Pre-Launch Validation

- [ ] All four rooms accessible via unique codes
- [ ] Parameter settings correctly applied per room
- [ ] System prompt identical across all rooms
- [ ] Aware interfaces display correct parameter info
- [ ] Unaware interfaces hide parameter info
- [ ] Session timer functions correctly
- [ ] 5-minute warning triggers properly
- [ ] All messages logged with timestamps
- [ ] Response delay consistent (2-3 seconds)
- [ ] Emergency features functional

---

## 13. Target User Profile

**Population**: English L2 undergraduate students
**Proficiency Level**: B1+ (CEFR) / IELTS 6.0+
**Context**: Creative writing poetry course
**Institution**: Hong Kong Baptist University
**Age Range**: Typically 18-22 years
**Technical Literacy**: Basic computer skills
**Cultural Context**: Hong Kong multilingual learners

---

## 14. Success Metrics for Mockup

### Functional Success
- All 4 rooms operate independently
- Parameters correctly configured and logged
- Sessions run smoothly for 50 minutes
- Data capture complete and accurate

### User Experience Success
- Interface intuitive for L2 learners
- Clear distinction between Aware/Unaware conditions
- Natural conversation flow maintained
- Technical issues minimal

---

## 15. Additional Resources & References

### Relevant Literature
- **Coenen et al. (2022)**: Wordcraft LLM study - surprise interactions
- **Hanauer (2010)**: L2 poetry pedagogy - imitation-transformation approach
- **Lyster & Ranta (1997)**: Corrective feedback taxonomy

### Parameter Studies
- Temperature/top-p effects on creative writing output
- Optimal configurations for educational contexts

---

## 16. Quick Start Implementation Guide

### Phase 1: Basic Structure
1. Set up 4 separate chat room environments
2. Implement access code system
3. Configure parameter settings per room
4. Create basic chat interface

### Phase 2: Interface Differentiation
1. Design Unaware interface (standard)
2. Design Aware interface (with parameter display)
3. Add educational tooltips/explanations
4. Test interface switching

### Phase 3: Functionality
1. Integrate AI backend (GPT-4 or compatible)
2. Implement response delay (2-3 sec)
3. Add session timer (50 min + warning)
4. Enable message logging

### Phase 4: Polish
1. Add typing indicators
2. Implement save/recovery features
3. Add emergency support buttons
4. Conduct usability testing

---

## 17. Contact & Support Information

**For Technical Questions**: [Research Team Contact]
**For Participant Support**: [Help Desk Info]
**Emergency Protocol**: [Emergency Contact]

---

## Appendix: Room Configuration Summary Table

| Feature | Room 1 | Room 2 | Room 3 | Room 4 |
|---------|--------|--------|--------|--------|
| **Temperature** | 0.3 | 0.3 | 0.8 | 0.8 |
| **Top-p** | 0.4 | 0.4 | 0.9 | 0.9 |
| **Parameter Setting** | Structured | Structured | Exploratory | Exploratory |
| **Awareness** | AWARE | UNAWARE | AWARE | UNAWARE |
| **Show Parameters** | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| **Interface Type** | Enhanced | Standard | Enhanced | Standard |
| **Participant Count** | n=5 | n=5 | n=5 | n=5 |
| **Primary Analysis** | Secondary | **PRIMARY** | Secondary | **PRIMARY** |

**Primary Analysis Focus**: Room 2 vs. Room 4 comparison isolates pure parameter effects without awareness bias.

---

**Document Version**: 1.0  
**Last Updated**: October 15, 2025  
**Status**: Ready for mockup development
