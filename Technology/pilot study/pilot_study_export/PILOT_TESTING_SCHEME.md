# Pilot Testing Scheme
## Human-AI Collaborative Poetry Writing Research Platform

**Study Date:** November 2025  
**Number of Participants:** 4  
**Duration:** ~45-60 minutes per participant  
**Study Type:** Mixed-methods pilot study with 2x2 factorial design

---

## 1. Research Design Overview

### 1.1 Research Questions
1. How do different AI parameter settings (structured vs. exploratory) affect collaborative poetry writing?
2. Does parameter awareness influence participant trust, engagement, and creative output?
3. What interaction patterns emerge in human-AI poetry collaboration?
4. Which poetry forms do participants prefer and why?

### 1.2 Study Conditions (4 Research Rooms)

| Participant | Room ID | AI Style | Awareness | Temperature | Top-P |
|-------------|---------|----------|-----------|-------------|-------|
| P1 | `room_1_structured_aware` | Structured | Aware | 0.25 | 0.35 |
| P2 | `room_2_structured_unaware` | Structured | Unaware | 0.30 | 0.40 |
| P3 | `room_3_exploratory_aware` | Exploratory | Aware | 0.75 | 0.85 |
| P4 | `room_4_exploratory_unaware` | Exploratory | Unaware | 0.80 | 0.90 |

### 1.3 Balanced Assignment Strategy
- **2 participants** experience **Structured** AI guidance (consistent, rule-based)
- **2 participants** experience **Exploratory** AI guidance (creative, varied)
- **2 participants** are **Aware** of AI parameter settings
- **2 participants** are **Unaware** of parameter settings

---

## 2. Testing Schedule

### Recommended Timeline

**Week 1: Preparation (3-4 days)**
- Day 1: Recruit participants, schedule sessions
- Day 2-3: System testing and preparation
- Day 4: Facilitator training

**Week 2: Data Collection - Session 1 (Login Tests)**
- Day 1: P1, P2, P3, P4 - Session 1 (10 min each, can do multiple per day)
- Schedule Session 2 for each participant

**Week 3: Data Collection - Session 2 (Poetry Writing)**
- Day 1: P1 Session 2 - Room 1 (Structured-Aware) - 25 min
- Day 2: P2 Session 2 - Room 2 (Structured-Unaware) - 25 min
- Day 3: P3 Session 2 - Room 3 (Exploratory-Aware) - 25 min
- Day 4: P4 Session 2 - Room 4 (Exploratory-Unaware) - 25 min

**Week 4: Analysis**
- Data extraction, analysis, and debrief

### Two-Session Structure

#### SESSION 1: Login & Setup (10 minutes per participant)

| Time | Activity | Duration |
|------|----------|----------|
| 0:00-0:03 | Welcome & Consent | 3 min |
| 0:03-0:06 | Pre-session Questionnaire | 3 min |
| 0:06-0:09 | Login Testing | 3 min |
| 0:09-0:10 | Schedule Session 2 | 1 min |

**Purpose:** 
- Verify authentication system works
- Collect demographic data
- Ensure participants can access platform
- Build familiarity before main session

#### SESSION 2: Poetry Writing (25 minutes per participant)

| Time | Activity | Duration |
|------|----------|----------|
| 0:00-0:02 | Welcome Back & Login | 2 min |
| 0:02-0:04 | Platform Tutorial | 2 min |
| 0:04-0:19 | Poetry Writing Session | 15 min |
| 0:19-0:24 | Post-session Interview | 5 min |
| 0:24-0:25 | Debrief & Thank You | 1 min |

**Purpose:**
- Test the four room conditions
- Observe human-AI collaboration
- Collect poetry output and interaction data
- Gather user experience feedback

---

## 3. Participant Recruitment

### 3.1 Inclusion Criteria
- Age: 18+ years old
- English proficiency: Intermediate to advanced (L2 learners preferred)
- Interest in creative writing or poetry
- Basic computer/smartphone literacy
- Available for 60-minute session

### 3.2 Exclusion Criteria
- Previous extensive use of AI writing tools
- Professional poets or writers
- Non-English speakers with low proficiency

### 3.3 Recruitment Script

> "We're conducting a study on collaborative poetry writing with AI assistance. You'll work with an AI partner to create poems in a 45-minute session. No poetry experience needed! You'll receive [incentive] for participation. Interested?"

### 3.4 Recommended Incentives
- $20-30 gift card per participant
- Or: Course credit (if academic setting)
- Or: Free lunch + certificate of participation

---

## 4. Data Collection Methods

### 4.1 Automatic System Logging
The platform automatically collects:
- ✅ All conversation messages (user & AI)
- ✅ Poetry form selections
- ✅ Session timestamps and duration
- ✅ Interaction type classifications
- ✅ Room configuration data
- ✅ Progress milestones

### 4.2 Pre-Session Questionnaire (5 minutes)
Collect via Google Forms or paper:

1. **Demographics**
   - Age range: [ ] 18-24 [ ] 25-34 [ ] 35-44 [ ] 45+
   - First language: _________
   - Years learning English: _________

2. **Prior Experience**
   - Poetry writing experience: [ ] None [ ] Beginner [ ] Intermediate [ ] Advanced
   - AI tool usage: [ ] Never [ ] Rarely [ ] Sometimes [ ] Frequently
   - Familiarity with chatbots: [ ] None [ ] Some [ ] Very familiar

3. **Creative Confidence**
   - Rate your creative writing confidence (1-5): _____
   - Comfort with technology (1-5): _____

### 4.3 Post-Session Interview (5 minutes - Session 2 only)
Semi-structured questions:

**Experience Questions:**
1. "How would you describe your experience working with the AI partner?"
2. "What worked well? What was challenging?"
3. "Did the AI's suggestions help or hinder your creativity?"

**Awareness-Specific (Aware conditions only):**
4. "You could see the AI parameter settings. Did this affect how you interacted?"

**Creative Process:**
5. "Did you feel like you maintained your creative voice?"

**Future Use:**
6. "Would you use a tool like this again for creative writing?"

### 4.4 Observational Notes
Facilitator should note:
- Participant engagement level (high/medium/low)
- Moments of frustration or confusion
- Spontaneous comments or reactions
- Technical issues encountered

---

## 5. Testing Procedures

### 5.1 Pre-Testing Checklist

**Technical Setup:**
- [ ] Internet connection stable
- [ ] Platform accessible at deployment URL
- [ ] All 4 research rooms configured in database
- [ ] Admin dashboard functional
- [ ] Export functions tested
- [ ] Phone authentication working
- [ ] OpenRouter API credits sufficient

**Materials Prepared:**
- [ ] Consent forms (4 copies + extras)
- [ ] Pre-session questionnaires (4 copies)
- [ ] Post-session interview guides (4 copies)
- [ ] Observation sheets (4 copies)
- [ ] Pens, clipboard
- [ ] Recording device (if consent for audio)
- [ ] Participant incentives ready

**Environment Setup:**
- [ ] Quiet, private testing room
- [ ] Comfortable seating
- [ ] Computer/tablet with large screen
- [ ] Backup device available
- [ ] Water, tissues available
- [ ] "Testing in Progress" sign on door

### 5.2 Session Protocol

#### SESSION 1: Login & Setup (10 minutes)

**A. Welcome & Consent (3 minutes)**

**Script:**
> "Welcome and thank you for participating! This is the first of two short sessions. Today we'll just get you set up with the system—should only take 10 minutes. In our second session, you'll work with an AI partner to create poetry. 
>
> Everything you write will be confidential. You can stop at any time. Please read this consent form carefully. Questions?"

- Participant reads and signs consent form
- Explain their rights
- Assign participant ID: P1, P2, P3, or P4

**B. Pre-Session Questionnaire (3 minutes)**
- Hand participant the questionnaire
- Let them complete independently
- Collect and review for completeness

**C. Login Testing (3 minutes)**

**Script:**
> "Let me show you how to log into the system. You'll use your phone number for authentication. Let's try that now..."

- Guide participant through login process
- Verify successful authentication
- Have them practice logging out and back in
- Answer any technical questions

**D. Schedule Session 2 (1 minute)**

**Script:**
> "Perfect! You're all set up. Now let's schedule your poetry writing session. It will take about 25 minutes. When works best for you in the next few days?"

- Schedule Session 2 (ideally 1-3 days later)
- Provide confirmation details
- Thank participant

---

#### SESSION 2: Poetry Writing (25 minutes)

**A. Welcome Back & Login (2 minutes)**

**Script:**
> "Welcome back [Name]! Ready to create some poetry? Let's log you in using the same method from last time."

- Participant logs in independently
- Navigate to their assigned room
- Confirm they see the correct interface

**B. Platform Tutorial (2 minutes)**

**Script:**
> "Let me quickly show you how this works. You'll have a conversation with your AI poetry partner..."

- Point out message area
- Show input box and send button
- Explain poetry form selection

**For Aware conditions (P1, P3) only:**
> "You'll notice information about the AI's settings here. Feel free to ask about these if you're curious."

**For all:**
> "I'll observe quietly. Only interrupt if there's a technical problem. You have about 15 minutes to create. Any questions?"

**C. Poetry Writing Session (15 minutes)**

**Facilitator Instructions:**
- Start timer
- Sit nearby but not hovering
- Take observational notes quietly
- Only intervene for technical issues
- Note any spontaneous comments

**At 12-minute mark:** "You have about 3 minutes left if you'd like to wrap up."

**D. Post-Session Interview (5 minutes)**
- End their session
- Thank participant for their writing
- Ask 5-6 core interview questions (see Section 4.3)
- Record responses (notes or audio with consent)

**E. Debrief & Thank You (1 minute)**

**Script:**
> "Thank you! For this study, we had four different AI configurations. You were in [explain their condition briefly]. Please don't discuss specifics with others who might participate.
>
> Here's your [incentive]. Would you like a summary of findings when complete?"

- Provide incentive
- Collect email if they want findings
- Thank them warmly

---

## 6. Data Analysis Plan

### 6.1 Quantitative Metrics

**Export from Admin Dashboard:**
1. **Session metrics** (per participant):
   - Total session duration
   - Number of messages exchanged
   - User vs AI message ratio
   - Number of poems created
   - Poetry forms selected

2. **Interaction patterns**:
   - Type A (Guided) vs Type B (Assisted) vs Type C (Collaborative) interactions
   - Response times
   - Parameter awareness questions asked (Aware conditions only)

3. **Comparative analysis**:
   - Structured vs Exploratory (P1+P2 vs P3+P4)
   - Aware vs Unaware (P1+P3 vs P2+P4)
   - Interaction with 2x2 factorial design

### 6.2 Qualitative Analysis

**Thematic coding of:**
1. **Conversation content**:
   - Creative autonomy indicators
   - Trust expressions
   - Frustration markers
   - Satisfaction indicators

2. **Interview responses**:
   - User experience themes
   - AI partnership perceptions
   - Creative process descriptions
   - Awareness effects (if applicable)

3. **Observational notes**:
   - Behavioral patterns
   - Engagement levels
   - Spontaneous reactions

### 6.3 Analysis Questions

**By condition:**
- Do Structured rooms show more consistent interaction patterns?
- Do Exploratory rooms generate more creative vocabulary diversity?
- Does Awareness affect trust expressions?
- Does Awareness affect number of parameter-related questions?

**By poetry form:**
- Which forms are most popular?
- Do different rooms prefer different forms?
- Which forms lead to longer sessions?

**Overall:**
- What makes a successful human-AI poetry collaboration?
- What are common frustrations or confusion points?
- How can we improve the system?

---

## 7. Troubleshooting Guide

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **Participant can't log in** | Check phone number format, verify authentication is enabled |
| **Room not loading** | Refresh page, verify room ID in URL matches assignment |
| **AI not responding** | Check OpenRouter API status, verify internet connection |
| **Messages not saving** | Check Supabase connection, verify conversation ID exists |
| **Participant confused by interface** | Provide additional demo, use simpler language |
| **Session too short (<15 min)** | Encourage exploration of different forms, ask facilitating questions |
| **Participant unmotivated** | Remind them there's no right/wrong, emphasize playfulness |

### Technical Backup Plan
1. **If platform crashes:**
   - Switch to backup device
   - Restart session in same room
   - Note interruption time for data correction

2. **If internet fails:**
   - Use mobile hotspot backup
   - Reschedule session if complete failure
   - Compensate participant for time

3. **If API quota exceeded:**
   - Have backup OpenRouter API key ready
   - Or use alternative AI API configured in advance

---

## 8. Ethical Considerations

### 8.1 Informed Consent
- ✅ Participants understand study purpose
- ✅ Voluntary participation emphasized
- ✅ Right to withdraw at any time
- ✅ Data confidentiality explained
- ✅ Compensation provided regardless of completion

### 8.2 Data Privacy
- ✅ Assign anonymous participant IDs (P1-P4)
- ✅ Remove identifying information from transcripts
- ✅ Store consent forms separately from data
- ✅ Secure data storage (encrypted, password-protected)
- ✅ Delete raw data after analysis period (specify retention)

### 8.3 Potential Risks & Mitigation
- **Minimal risk**: Creative writing task is low-stress
- **Psychological discomfort**: Participants may feel judged about writing ability
  - *Mitigation*: Emphasize no evaluation, focus on AI collaboration not writing quality
- **Privacy concerns**: Chat data collected
  - *Mitigation*: Clear consent, option to delete data, anonymization

### 8.4 Debriefing
- Explain study conditions after completion
- Answer all participant questions
- Provide researcher contact for follow-up concerns
- Offer to withdraw data if requested

---

## 9. Success Criteria for Pilot

### 9.1 Technical Success
- ✅ All 4 participants complete sessions without major technical issues
- ✅ Data successfully logged to database
- ✅ All room configurations function as designed
- ✅ Export functions work correctly

### 9.2 Research Success
- ✅ Clear differences observable between conditions
- ✅ Rich qualitative data collected from interviews
- ✅ Participants provide constructive feedback
- ✅ Identify areas for improvement before full study

### 9.3 Participant Experience Success
- ✅ Participants find experience engaging (avg rating >3/5)
- ✅ No major frustrations or confusion
- ✅ Participants create at least one complete poem each
- ✅ Positive comments about AI collaboration

---

## 10. Post-Pilot Actions

### 10.1 Data Export & Backup
- Export all data via Admin Dashboard immediately after P4
- Create multiple backups (local + cloud)
- Verify data integrity

### 10.2 Initial Analysis (Week 3)
- Compile descriptive statistics
- Read through all conversations
- Initial thematic coding of interviews
- Identify patterns and outliers

### 10.3 System Improvements
Based on pilot findings, consider:
- UI/UX adjustments
- Prompt refinements for AI
- Additional features needed
- Bug fixes

### 10.4 Research Adjustments
For full study, consider:
- Sample size calculations
- Session length modifications
- Additional measures needed
- Protocol refinements

### 10.5 Reporting
Create pilot summary document with:
- Participant demographics
- Key quantitative findings
- Main qualitative themes
- Technical issues encountered
- Recommendations for full study
- Sample conversation excerpts (anonymized)

---

## 11. Budget Estimate

| Item | Cost |
|------|------|
| **Participant Incentives** (4 × $25) | $100 |
| **OpenRouter API Usage** (~1000 tokens/session) | $10 |
| **Materials** (printing, supplies) | $20 |
| **Facilitator Time** (4 sessions × 1.5 hrs) | [Internal] |
| **Analysis Time** (data processing, coding) | [Internal] |
| **Total Monetary Cost** | **~$130** |

---

## 12. Timeline Summary

| Week | Activities | Deliverables |
|------|-----------|--------------|
| **Week 1** | Preparation, recruitment, setup | 4 scheduled participants, materials ready |
| **Week 2** | Data collection (4 sessions) | Completed sessions, raw data |
| **Week 3** | Analysis, write-up | Pilot report, recommendations |

---

## Contact Information

**Principal Investigator:**  
[Your Name]  
[Email]  
[Phone]

**For Technical Issues:**  
[Tech Support Contact]

**For Ethical Concerns:**  
[IRB/Ethics Board Contact]

---

## Appendices

- **Appendix A**: Consent Form Template
- **Appendix B**: Pre-Session Questionnaire
- **Appendix C**: Post-Session Interview Guide
- **Appendix D**: Observation Sheet Template
- **Appendix E**: Room Configuration Details
- **Appendix F**: Data Export Instructions

(See `PILOT_TESTING_MANUAL.md` for detailed forms and procedures)

---

**Document Version:** 1.0  
**Last Updated:** November 3, 2025  
**Status:** Ready for Implementation
