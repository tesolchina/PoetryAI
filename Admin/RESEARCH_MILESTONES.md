# PoetryAI Research Project Milestones
**Researcher:** Yu Ruobin, Department of English, Hong Kong Baptist University  
**Project:** L2 Poetry Writing with AI Parameter Effects Study  
**Research Question:** How do AI parameter settings (temperature/top-p) affect collaborative creativity in L2 poetry writing?  
**Last Updated:** November 18, 2025

---

## 📊 Executive Summary

| Phase | Timeline | Status | Key Outputs |
|-------|----------|--------|-------------|
| **Research Design** | May-Oct 2024 | ✅ Complete | 2×2 factorial design, 4 research questions, ethical approval |
| **Literature Review** | May-Oct 2024 | ✅ Complete | 50+ papers across 4 domains, comprehensive synthesis |
| **Platform Development** | May-Nov 2025 | ✅ Complete | Functional platform at poetry.aitutor.ink, 4 rooms deployed |
| **Pilot Testing** | Nov 16, 2025 | ✅ Complete | 4 testers, 87 conversations, 100% technical success |
| **Pilot Analysis** | Nov 17-18, 2025 | ✅ Complete | 43,000+ words analysis & improvement solutions |
| **Main Study Session 1** | Nov 24, 2025 | ✅ Complete | 10 participants, 500+ messages, preliminary findings |
| **Data Analysis Session 1** | Nov 25-29, 2025 | ✅ Complete | Three-type coding, triangulation, preliminary essay (2,000 words) |
| **Main Study Session 2 (CCL Seminar)** | Jan 2026 | ✅ Complete | 9 participants, 7 completed feedback, comprehensive analysis |
| **Dissertation** | Ongoing | 🔄 In Progress | Introduction & Methodology chapters drafted |

---

## 🎯 Major Milestones Achieved

### 1. Research Design & Theoretical Foundation (May-Oct 2024)

**Core Framework Established:**
- **2×2 Factorial Design:** Temperature/top-p settings (0.3/0.8, 0.4/0.9) × Awareness conditions (visible/hidden)
- **Three Interaction Types:** Type A (Constraint Repair), Type B (Content Enhancement), Type C (Surprise Harvest)
- **Four Research Questions:** 
  - RQ1: Parameter effects on inquiry moves
  - RQ2: Scaffolding patterns in AI-assisted writing
  - RQ3: Student perceptions of collaboration
  - RQ4: Interaction type preferences

**Theoretical Integration:**
- L2 poetry pedagogy (Hanauer, 2015)
- Human-AI co-creativity (Coenen et al., 2021 - Wordcraft)
- Data-Driven Learning principles
- 50+ papers reviewed across AI creative writing, DDL, L2 pedagogy, parameter studies

**Documentation:** Research design, methodology justification, sample size rationale, ethical consent materials, risk assessment

---

### 2. Platform Development & Technical Implementation (May-Nov 2025)

**Self-Taught Programming Journey:**
- Acquired Python programming from zero coding background
- Mastered async/await patterns, API integration, web architecture
- Built chatbot framework with OpenRouter integration
- Developed 15+ testing scripts for validation
- **Platform URL:** https://poetry.aitutor.ink/

**Four-Room System Features:**
- ✅ Room A-D with distinct parameter configurations (structured vs. exploratory)
- ✅ User authentication (Email/Password)
- ✅ Real-time conversation logging
- ✅ Chat history management & PDF export
- ✅ Session persistence across rooms
- ✅ Mobile-responsive interface

**Prompt Engineering:**
- Unified system prompt across all conditions (maintains research validity)
- Parameter-only differentiation strategy
- Response framework: 40-80 words, three interaction types
- Quality control checklist & error recovery protocols

**Key Documents:** Chatbot framework code, unified prompt design, testing suite, deployment documentation

---

### 3. Pilot Testing & Comprehensive Analysis (Nov 16-18, 2025)

**Pilot Execution (November 16, 2025):**
- **4 testers** via Zoom supervision (01:43-03:19 UTC)
- **87 conversation sessions** created across all rooms
- **167 messages** exchanged (40-46 messages per tester)
- **Testing durations:** T1 (40min), T2 (17min), T3 (97min), T4 (15min)
- **Poetry output:** All testers successfully created poems (love, pain, nature, haiku themes)

**Technical Success (100% across all features):**
- ✅ Login authentication
- ✅ Chat history saving & viewing
- ✅ Conversation renaming
- ✅ PDF download functionality
- ✅ Zero system crashes or API failures

**Critical Issues Identified:**

**🚨 Priority 1 - Emotional Safety Gap (CRITICAL):**
- No mental health protection when students discuss trauma/pain
- T1 concern: "AI continues to induce user to transform pain into creative poems may have potential risks"
- T2 example: Discussed childhood trauma, chatbot said "I'm sorry" and continued poetry prompts

**⚠️ Priority 2 - Over-Scaffolding (HIGH):**
- T1 feedback: "Too much guidance (too restrictive)"
- Constant 3-option presentation reduces creative autonomy
- Type B interactions dominate at 50% (should be balanced)
- T1 suggestion: "Put keywords beside screen, let users initiate poem structuring"

**⚠️ Priority 3 - Theme Deviation (HIGH):**
- T3: "Chatbot tends to deviate from original poetry theme, particularly after users inquiring about poetic forms"
- Generic resets: "What would you like to write about?" after theme already established

**⚠️ Priority 4-5 - Medium Issues:**
- T2: "Can't follow my abstract mindset" (naturalness: 3/5)
- T4: Needs more creative inspiration vs. operational guidance, "show its thinking process"

**User Ratings:** Naturalness 3.75/5, Balance mostly "Good" (except T1: "Too much"), Helpfulness mixed

---

### 4. Post-Pilot Improvement Solutions (Nov 17-18, 2025)

**Comprehensive 23,000-word solution document addressing all 5 issues:**

**1. Emotional Safety Protocol (Week 1 Implementation):**
- **Three-tier detection system:**
  - Tier 1: Gentle check-in (mild emotions) → "How are you feeling about continuing?"
  - Tier 2: Active concern (trauma/distress) → Resources, pause options
  - Tier 3: Crisis protocol (severe distress) → Stop creative work, provide hotlines (Samaritans: 2389 2222)
- Hong Kong mental health resources integrated
- Continued support framework with frequent check-ins

**2. Adaptive Scaffolding System (Week 2):**
- **Three modes based on autonomy signals:**
  - Mode A (Minimal): High autonomy → No automatic options, open questions
  - Mode B (Balanced): Moderate autonomy → Conditional options **[DEFAULT]**
  - Mode C (High): Low autonomy → Structured guidance with 2-3 options
- T1's keyword sidebar concept integrated
- Autonomy negotiation at session start
- Maximum 2 options (not 3) to reduce burden

**3. Theme Continuity System (Week 2):**
- Store PRIMARY THEME throughout conversation
- Form-to-theme bridge responses (never lose original theme)
- Theme echo every 2-3 exchanges
- No inappropriate resets after theme established
- Immediate theme connection after form explanations

**4. Abstract Thinking Support (Week 3):**
- Recognition of abstract/surreal expression
- No concreteness demands ("Can you be more specific?" prohibited)
- Open-ended exploration prompts
- Mirror abstract style in responses

**5. Creative Inspiration Enhancement (Week 3):**
- Inspiration-first response pattern (before structure)
- Thinking process transparency ("I'm thinking about...")
- Creative direction prompts vs. operational questions
- Possibility mapping (sensory/emotional/symbolic paths)

**Implementation Timeline:** 3 weeks total (Critical → High → Medium priority)  
**Validation:** 60+ test cases designed for all scenarios

---

### 5. Main Study Session 1 (November 24, 2025)

**Session Execution:**
- **Date:** November 24, 2025 (Monday)
- **Duration:** 2.5 hours
- **Participants:** 10 HKBU graduate students with advanced English proficiency (IELTS 6.5-7.5 equivalent)
- **Distribution:** 4 experimental rooms (A: Structured-Aware, B: Structured-Unaware, C: Exploratory-Aware, D: Exploratory-Unaware)
- **Platform Performance:** 100% technical success, zero system failures

**Data Collection (Three Sources for Triangulation):**
1. **Chat Transcripts:** 500+ message exchanges across all rooms
   - Complete behavioral records of human-AI interactions
   - Coded using three-type framework (Type A: Constraint Repair, Type B: Exemplar Giving, Type C: Surprise Harvest)
   - Inter-rater reliability: Cohen's κ=0.82 (87% agreement)

2. **Panel Discussion:** 22-minute recorded discussion
   - Spontaneous comparative reflection across rooms
   - Unprompted identification of interaction type differences
   - Qualitative evidence of parameter effects on collaborative experience

3. **Feedback Forms:** 8 participants completed (66 questions each)
   - Authorship perception ratings
   - Satisfaction scores (5-point scale)
   - Interaction type preference rankings
   - Open-ended reflection responses

**Preliminary Key Findings:**

**Finding 1 - Sevenfold Type C Difference:**
- High-temperature rooms (C, D): 35% Type C (Surprise Harvest) interactions
- Low-temperature rooms (A, B): 5% Type C interactions
- Demonstrates parameter configuration as primary determinant of interaction type distribution

**Finding 2 - Type B Paradox:**
- 75% of participants rated Type B (Exemplar Giving) as "most helpful"
- Yet Type B correlates with only 10% self-authorship perception
- Reveals tension between pedagogical accessibility and creative agency

**Finding 3 - Type C Enables Creative Transformation:**
- P09 (Room C): AI suggested "found poetry technique" - advanced strategy participant hadn't considered
- P10 (Room C): AI reframed interaction from poetry construction to therapeutic expression
- No comparable Type C moments observed in low-temperature rooms

**Finding 4 - Observable Differences:**
- P09 spontaneously asked: "Is the difference between the rooms pretty obvious?"
- Validates that parameter effects are phenomenologically detectable through interaction patterns
- Suggests potential for experiential AI literacy development

**Finding 5 - Type C Predicts Authorship:**
- Rooms with 35% Type C: 62.5% self-authorship, 4.75/5 satisfaction
- Rooms with 5% Type C: 10-20% self-authorship, 2.0/5 satisfaction
- 4-6x authorship difference, 2x satisfaction difference

**Panel Discussion Themes:**
- Room B participants: AI described as "mechanical," "just following instructions"
- Rooms C/D participants: AI described as "warm-hearted," "like a very good friend"
- Contrasting metaphors reflect different collaborative modes (technical assistant vs. creative partner)

**Analytical Framework Applied:**
- Convergent evidence across all three data sources (triangulation validated)
- Three-type coding successfully captured parameter effects
- Multi-method approach revealed "helpful but alienating" paradox unique to feedback forms

---

### 6. Post-Session 1 Analysis & Documentation (November 25-29, 2025)

**Comprehensive Data Analysis:**
- **Chat Transcript Coding:** All 500+ messages coded for interaction types (Type A/B/C)
- **Statistical Patterns:** Chi-square analysis of interaction type distribution by parameter configuration
- **Qualitative Analysis:** Panel discussion transcribed and thematically coded
- **Feedback Forms:** 8 forms (66 questions each) analyzed for authorship, satisfaction, preferences

**Research Output - Preliminary Results Essay:**
- **Title:** "Preliminary Findings: Parameter Effects on Authorship and Creative Agency in AI-Assisted L2 Poetry Writing"
- **Length:** 1,997 words
- **Structure:** Abstract, Introduction (with three-type framework), Method, Findings (5 findings), Methodological Contributions, Limitations, Implications, Conclusion
- **Status:** Draft completed, shared with supervisors for PolyU conference application

**Key Contributions Identified:**
1. **Interaction Type Distribution as Design Principle:** Parameter selection determines available interaction types, not minor technical detail
2. **Progressive Pedagogy Strategy:** Navigate Type B paradox through scaffolding progression (low-temp initially, high-temp as learners develop)
3. **Type C Enables Authorship:** Creative writing should prioritize high-temperature parameters (0.7-0.9) for authentic co-creation
4. **AI Literacy through Interaction Types:** Learners can develop sophisticated understanding through experiential engagement with interaction patterns

**Next Steps for Full Study:**
- Sessions 2-3 scheduled (10 additional participants)
- Validation of preliminary patterns with full 20-participant sample
- Longitudinal perspective on interaction type exposure effects
- Individual difference moderators investigation

---

## 📈 Key Research Outputs

**Technical Achievements:**
1. Fully functional PoetryAI platform (poetry.aitutor.ink)
2. Four-room experimental system with parameter differentiation
3. Comprehensive testing suite (15+ scripts)
4. Complete data logging infrastructure

**Research Documentation (43,000+ words):**
1. Research design framework & methodological justification
2. Literature review (50+ papers synthesized)
3. Ethical consent materials & risk assessment
4. Pilot testing comprehensive analysis (20,000 words)
5. Prompt improvement solution (23,000 words)
6. Chatbot design documentation
7. Nature Career article draft (1,400 words on transdisciplinary learning)
8. **Preliminary Results Essay (2,000 words) - Session 1 findings**
9. **Session 1 Data Analysis Documentation:** Chat transcript coding, panel discussion transcription, feedback form analysis

---

## 🚨 Next Steps

### Main Study Completion (Dec 2025 - Jan 2026):
1. **Session 2:** Recruit and conduct second session with 10 additional participants
2. **Session 3:** Complete final session and follow-up interviews (January 2025)
3. Validate preliminary findings with full 20-participant sample
4. Investigate individual difference moderators
5. Longitudinal analysis of interaction type exposure effects

### Data Analysis & Writing:
6. Comprehensive quantitative analysis (RQ1: Chi-square, RQ2: Scaffolding coding)
7. Full qualitative analysis (RQ3-4: Thematic coding, preference ranking)
8. Complete dissertation findings & discussion chapters
9. Expand preliminary essay to full research paper
10. Prepare conference presentation materials (PolyU conference application)

### Dissemination:
11. Submit to academic conferences (PolyU, international venues)
12. Prepare journal article submission
13. Finalize dissertation defense materials

---

### 7. Main Study Session 2 - CCL Seminar (January 2026)

**Session Context:**
- **Event:** CCL (Centre for Applied English Studies) Seminar Series
- **Date:** January 2026
- **Duration:** One-time workshop format
- **Participants:** 9 graduate students from Hong Kong Baptist University
- **Feedback Completion:** 7 participants completed the feedback form
- **Setting:** Different from Session 1 (workshop vs. experimental session)
- **Platform:** PoetryAI platform (poetry.aitutor.ink)

**Participant Feedback Summary (N=7):**

**Overall Satisfaction (Extremely High):**
| Metric | Average | Range | Consensus |
|--------|---------|-------|-----------|
| Seminar Enjoyment | 4.9/5 | 4-5 | 86% gave 5/5 |
| Platform Comfort | 4.7/5 | 4-5 | 86% gave 5/5 |
| Future Usage Intent | 4.6/5 | 4-5 | 86% gave 5/5 |

**Creative Ownership & Collaboration Patterns:**
- **AI-Guided Approach (43%):** 3 participants allowed AI to guide most creative decisions (10-20% self-authorship)
- **Exploratory Approach (43%):** 3 participants explored different directions (60-90% self-authorship)
- **Linear Approach (14%):** 1 participant followed one clear path (50% self-authorship)
- **Mean Authorship Attribution:** 40% self (consistent with Session 1)

**Key Findings:**

**Finding 1 - Type B Remains Most Utilized:**
- 71% experienced Type B (Content Enhancement) most frequently
- 57% rated Type B as most helpful for writing
- Aligns with Session 1 findings of Type B prevalence

**Finding 2 - Type A (Constraint Repair) Most Frustrating:**
- 43% found Type A interactions most frustrating
- Critical example: Wong Tiana - "The AI didn't really fix my format problems, it gave me an even longer haiku"
- Validates pilot testing findings about over-scaffolding and constraint handling

**Finding 3 - Word Choice Quality Concerns:**
- 57% disagreed with AI-suggested word choices
- 29% disagreed with meaning/message suggestions
- 29% disagreed with emotional aspects
- Indicates need for improved language quality and emotional authenticity

**Finding 4 - High Autonomy Case (Wong Tiana):**
- Only participant claiming 90% personal ownership
- Maintained 5/5 satisfaction across all metrics
- Preferred Type C (Surprise Harvest) interactions
- Suggests high-autonomy approach yields strong engagement

**Finding 5 - Interface Preferences:**
- **Exploratory Atelier:** Strongly preferred for personal writing (71%)
- **Structured Studio:** Slightly preferred for academic purposes (57%)
- Both rooms serve distinct pedagogical purposes effectively

**Top Future Use Cases (Ranked by Frequency):**
1. Learning new poetic forms or techniques (71%)
2. Getting feedback on drafts (71%)
3. Exploring creative directions (71%)
4. Personal creative expression (71%)
5. Brainstorming ideas when stuck (57%)

**Positive Feedback Highlights:**
- Zhao Fangyu: "The platform is well designed, very clear, concise, and elegant. I like the image generator function, all the pictures are very imaginative and cool, also the styles are very consistent."
- Chen Yujing: "I really like this platform and I will definitely use it again :)"
- Overall sentiment: Strong appreciation for platform design and image generation features

**Data Deliverables:**
1. **Organized_Feedback_Data.md:** Structured participant responses with clear categorization
2. **Feedback_Analysis_Report.md:** Comprehensive 11-section analysis including:
   - Executive summary
   - Satisfaction metrics
   - Creative ownership patterns
   - Interaction type analysis
   - Disagreement patterns
   - Interface preferences
   - Critical issues & recommendations
   - Longitudinal recommendations

**Analytical Insights:**

**Cross-Session Validation:**
- Type B prevalence consistent across Session 1 and Session 2
- Type A frustration issues validated (pilot → Session 1 → Session 2)
- Mean authorship attribution (~40%) consistent across sessions
- Word choice concerns identified in both sessions

**New Session 2 Insights:**
- **Design Excellence Recognized:** Participants spontaneously praised platform clarity and image generation
- **Educational Scalability:** 71% identified multiple future use cases across academic and personal contexts
- **Emotion-Centric Concerns:** More participants mentioned emotional aspects in Session 2 than Session 1
- **Autonomy-Satisfaction Link:** High-autonomy participants (Wong Tiana, 90%) show stronger satisfaction
- **Type C Engagement:** Chen Yujing's preference for Type C (Surprise Harvest) aligns with Session 1 high-autonomy pattern

**Comparative Session Analysis:**
- **Session 1 (Experimental):** 10 participants, controlled parameter conditions, focused on comparing room differences
- **Session 2 (Workshop):** 7 participants, open exploration, focus on real-world usability and future applications
- **Combined Effect:** Session 2 validates Session 1 findings in naturalistic setting while revealing design appreciation

---

## 💡 Key Insights & Reflections

**On Transdisciplinary Learning:**
Building the platform wasn't separate from research—it was integral. Every design decision was methodological. Learning to code as a humanities scholar required reconciling ambiguity-tolerance (literary analysis) with precision-demands (programming), producing deeper understanding of both domains.

**On Pilot Testing Value:**
Pilot testing revealed critical issues (emotional safety, over-scaffolding) that could have compromised main study validity and ethics. The 3-week implementation delay ensured research quality and participant wellbeing before Session 1.

**On Session 1 Preliminary Findings:**
The sevenfold Type C difference (35% vs. 5%) and sixfold authorship difference (62.5% vs. 10%) demonstrate that parameter configuration functions as a fundamental pedagogical design choice, not a minor technical detail. The "helpful but alienating" Type B paradox reveals critical tensions between scaffolding accessibility and creative agency that warrant careful pedagogical navigation.

**On Methodological Innovation:**
Multi-source triangulation (chat transcripts + panel discussion + feedback forms) proved essential. The Type B paradox emerged uniquely through feedback forms, while panel discussion captured spontaneous meta-awareness of interaction differences. This validates the three-type framework as an effective analytical lens for human-AI creative collaboration.

**On Research Impact:**
- **Academic:** Novel AI parameter study in L2 creative writing with preliminary evidence of systematic parameter effects on interaction types, authorship, and satisfaction
- **Practical:** Evidence-based prompt engineering, three-type interaction framework for analyzing human-AI collaboration
- **Pedagogical:** Guidelines for AI in L2 poetry teaching—balance guidance with autonomy through progressive parameter configuration (structured → exploratory as learners develop)

---

## 📚 Repository Structure
```
PoetryAI-6/
├── Admin/RESEARCH_MILESTONES.md (this file)
├── Literature/ (50+ papers, bibliography, synthesis)
├── Manuscript/ (Introduction, Methodology, Design docs, Nature article)
└── Technology/
    ├── 01_Research_Design/ (methodology, ethics, validity)
    ├── 02_System_Development/ (chatbot, prompts, UI, improvements)
    ├── 03_Testing_Validation/ (pilot analysis, chat histories, feedback)
    ├── 04_Data_Collection/ (participant materials)
    └── 05_Deployment_Operations/ (platform deployment docs)
```

---

**Status:** Session 1 complete with promising preliminary findings; Sessions 2-3 recruitment in progress  
**Next Update:** After Sessions 2-3 completion  
**Contact:** Yu Ruobin, Department of English, Hong Kong Baptist University
