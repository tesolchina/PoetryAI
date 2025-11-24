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
| **Main Study** | Nov.24, 2025 |  | 20 HKBU students, B1+ proficiency |
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

---

## 🚨 Next Steps (Before Main Study)

### Immediate (3-Week Implementation):
1. **Week 1:** Emotional safety protocols (CRITICAL)
2. **Week 2:** Adaptive scaffolding + Theme continuity (HIGH)
3. **Week 3:** Abstract thinking + Creative inspiration (MEDIUM)
4. Comprehensive validation testing (60+ test cases)

### Recruitment & Execution:
5. Launch HKBU recruitment campaign (20 students, B1+ proficiency)
6. Schedule main study sessions (4 experimental rooms, 5 students each)
7. Conduct testing with improved system
8. Deploy post-session questionnaire & interviews

### Analysis & Writing:
9. Quantitative analysis (RQ1: Chi-square, RQ2: Scaffolding coding)
10. Qualitative analysis (RQ3-4: Thematic coding, preference ranking)
11. Complete dissertation findings & discussion chapters
12. Prepare defense materials

---

## 💡 Key Insights & Reflections

**On Transdisciplinary Learning:**
Building the platform wasn't separate from research—it was integral. Every design decision was methodological. Learning to code as a humanities scholar required reconciling ambiguity-tolerance (literary analysis) with precision-demands (programming), producing deeper understanding of both domains.

**On Pilot Testing Value:**
Pilot testing revealed critical issues (emotional safety, over-scaffolding) that could have compromised main study validity and ethics. The 3-week implementation delay ensures research quality and participant wellbeing.

**On Research Impact:**
- **Academic:** Novel AI parameter study in L2 creative writing, DDL integration with poetry pedagogy
- **Practical:** Evidence-based prompt engineering, emotional safety protocols for creative AI
- **Pedagogical:** Guidelines for AI in L2 poetry teaching, balancing guidance with autonomy

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

**Status:** Ready for prompt implementation phase (3 weeks) before main study  
**Next Update:** After improvement implementation completion  
**Contact:** Yu Ruobin, Department of English, Hong Kong Baptist University
