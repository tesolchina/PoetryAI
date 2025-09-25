# What Is the "Temperature" of a Poem? Classroom Interactions in L2 Poetry Writing with LLMs as Co-creation Partners

**Yu Ruobin** | Department of English, Academy of Language and Culture | Hong Kong Baptist University  
**Supervisor**: [Supervisor Name] | **Contact**: [email@hkbu.edu.hk]

---

## 1. BACKGROUND

### The Challenge
- **AI in creative writing** is rapidly expanding, yet we know little about the **interactional processes** by which learners collaborate with generative models
- **Data-driven learning (DDL)** traditionally focuses on corpus analysis, but generative AI requires new pedagogical approaches
- **Parameter manipulation** (temperature, top-p) affects AI creativity, but their educational implications remain unexplored

### Current State of Research
- Creative writing with AI focuses on **products rather than processes** (Clark et al., 2018)
- L2 writing research emphasizes **academic writing** over **creative contexts** (Michel et al., 2025)
- **Gap**: No systematic investigation of how technical parameters affect learning interactions in creative writing

### Research Innovation
> **First study to examine parameter literacy effects in L2 creative writing contexts**
- Bridges technical AI research with educational applications
- Introduces **parameter awareness** as pedagogical variable
- Focuses on **process-oriented analysis** of human-AI collaboration

---

## 2. LITERATURE REVIEW & RESEARCH QUESTIONS

### Key Literature Domains

#### **Human-AI Creative Collaboration**
- **"Second Mind" Effect**: AI as cognitive extension in creative processes (Qian et al., 2023)
- **Collaborative Dynamics**: Evaluation, negotiation, co-construction patterns (Ashktorab et al., 2020)
- **Creative Process Focus**: Need for process-based evaluation vs. product assessment (McGregor et al., 2016)

#### **Parameter Studies & Creativity**
- **Temperature-Creativity Relationship**: "Is temperature the creativity parameter?" (Peeperkorn et al., 2024)
- **Top-p Sampling Effects**: Nucleus sampling impact on text consistency (Ravfogel et al., 2023)
- **L2 Context Relevance**: Parameter consistency in language learning environments (Üzümcü & Ganiz, 2025)

#### **L2 Creative Writing & DDL**
- **DDL Evolution**: From corpus analysis to generative AI integration (Crosthwaite & Baisa, 2023)
- **Creative Writing Pedagogy**: Scaffolding poetry writing in L2 contexts (Kerbs et al., 2024)
- **AI Literacy**: Critical thinking in AI-assisted writing (Wang & Wang, 2025)

### Research Questions

**RQ1**: How do parameter settings (low vs. high temperature/top-p) condition learners' **inquiry moves** and **appeals to exemplars** during poem co-creation?

**RQ2**: What forms of **teacher/peer scaffolding** emerge, and how do learners take up this scaffolding across **parameter conditions**?

**RQ3**: How do **collaborative dynamics** (evaluation, negotiation, co-creation) unfold and vary by **parameter settings**?

**RQ4**: Which **interaction types** are most useful for instruction, as indicated by their frequency, sequencing centrality, and **impact on revision** and **metalinguistic talk**?

---

## 3. HYPOTHESES

### Three Interaction Type Framework

#### **Type A: Diagnosis → Repair**
- **Definition**: Identify form issues (rhyme, syllable, meter) and execute targeted fixes
- **Hypothesis A1**: Low-variability settings (Room A) → more frequent Type A moves
- **Expected Evidence**: Higher cohesion/clarity ratings, shorter time-to-fix

#### **Type B: Exemplar Pivot** 
- **Definition**: Request exemplars, extract characteristics, apply to draft
- **Hypothesis B1**: High-variability settings (Room B) → increased Type B usage to control drift
- **Expected Evidence**: More exemplar requests after surprising outputs

#### **Type C: Surprise Harvest**
- **Definition**: Seek divergent metaphors/images, selectively integrate into human-led draft
- **Hypothesis C1**: High-variability settings → more Surprise Harvest moves
- **Expected Evidence**: More C→A sequences (creative exploration + repair)

### Parameter Awareness Effects

**Aware Participants**: Strategic interaction type selection based on parameter knowledge
- Deliberate Type A prompting in low-variability conditions
- Planned Surprise Harvest in high-variability conditions

**Unaware Participants**: Intuitive responses without explicit parameter attribution
- Similar patterns but attributed to "careful prompting" vs. parameter differences
- Later pivoting after experiencing frustration

---

## 4. METHODOLOGY

### **Research Design**
- **Mixed-methods experimental study**
- **Setting**: English L2 creative writing course, HKBU
- **Duration**: 3 months (September-November 2025)

### **Participants**
- **N = 20** English L2 undergraduates
- **Eligibility**: B1+ CEFR proficiency
- **Distribution**: 10 per room (A/B), balanced by awareness condition

### **Experimental Conditions**

| Condition | Temperature | Top-p | Characteristics |
|-----------|-------------|-------|-----------------|
| **Room A** | 0.1-0.2 | 0.1-0.2 | **Constrained**: Predictable, focused outputs |
| **Room B** | 0.8-0.9 | 0.8-0.9 | **Exploratory**: Creative, variable outputs |

### **UI Manipulation**
- **Aware UI**: Displays parameter settings and effects
- **Unaware UI**: No parameter information provided

### **Chatbot Design**
- **Role**: Supportive L2 poetry coach
- **Six Modes**: Warm-up, Exemplar analysis, Form practice, Constraint drafting, Surprise generation, Revision coaching
- **Pedagogy**: One device per turn, student voice central

### **Data Collection Protocol**

1. **Pre-experiment** (10 min): Consent, orientation, baseline survey
2. **Chatbot Interaction** (15 min): Draft 4-6 lines with AI partner
3. **Reflection** (10 min): Parameter perception, learning experience  
4. **Debate Session** (20 min): "Are LLM-assisted results good poetry?"

### **Data Sources**
- ✅ **Chat logs**: Complete interaction transcripts with timestamps
- ✅ **Audio recordings**: Panel discussions and debates
- ✅ **Artifacts**: Poem versions and revisions with version control
- ✅ **Surveys**: Pre/post questionnaires (validated instruments)
- ✅ **API logging**: Granular interaction data with parameter verification
- ✅ **Reflection journals**: Weekly participant experience documentation

### **Analysis Framework**
- **Interaction coding**: Three-type taxonomy with inter-rater reliability (κ > 0.8)
- **Sequence analysis**: Markov chain modeling of interaction patterns
- **Statistical tests**: Mixed-effects modeling for parameter awareness effects
- **Qualitative analysis**: Thematic analysis of debates and reflections

---

## 5. IMPLICATIONS & IMPACT

### **Theoretical Contributions**

#### **1. Parameter Literacy Theory**
- **Novel concept**: How technical knowledge affects learning processes
- **Bridge**: Connects AI technical research with educational applications
- **Framework**: Parameter awareness as pedagogical variable

#### **2. Creative DDL Framework**
- **Extension**: DDL methodology to creative writing contexts  
- **Evolution**: From corpus analysis to generative AI collaboration
- **Innovation**: Process-oriented approach to human-AI creative interaction

#### **3. Multi-Agent Scaffolding Model**
- **Integration**: Teacher + peer + AI support systems
- **Dynamics**: How AI changes traditional scaffolding patterns
- **Agency**: Balancing AI assistance with learner creativity

### **Practical Applications**

#### **For Educators**
- **Interaction Ranking**: Evidence-based priority of teaching targets
- **Parameter Guidelines**: When to use constrained vs. exploratory settings
- **Scaffolding Strategies**: How to support learners across parameter conditions

#### **For Curriculum Design**
- **Lesson Plans**: Structured activities for AI-assisted creative writing
- **Assessment Framework**: Evaluating process vs. product in AI collaboration
- **Progression Model**: Scaffolding from constrained to exploratory settings

#### **For Technology Integration**
- **Interface Design**: Parameter awareness vs. transparency decisions
- **API Implementation**: Logging and tracking for educational contexts
- **Customization**: Adapting AI tools for specific learning objectives

### **Broader Impact**

#### **Educational Technology**
- **Evidence Base**: Empirical foundation for AI parameter effects in learning
- **Best Practices**: Guidelines for implementing generative AI in classrooms
- **Teacher Training**: Professional development for AI-assisted instruction

#### **L2 Writing Pedagogy**
- **Creative Writing**: Expanding beyond academic writing contexts
- **Process Orientation**: Focus on learning journey vs. final products
- **Agency Preservation**: Maintaining student voice in AI collaboration

#### **AI and Creativity**
- **Human-AI Partnership**: Understanding collaborative creative processes  
- **Creativity Assessment**: Process-based evaluation frameworks
- **Parameter Effects**: Empirical evidence for creativity-control relationships

---

## 6. EXPECTED DELIVERABLES

### **Academic Outputs**
1. **Empirical Report**: Detailed findings on parameter-conditioned differences
2. **Journal Articles**: Submissions to *Journal of Second Language Writing*, *Applied Corpus Linguistics*
3. **Conference Presentations**: AAAL, CALICO, WorldCALL conferences

### **Practical Resources**
1. **Practitioner-Oriented Ranking**: Interaction types prioritized for instruction
2. **Open Tutorial**: Complete lesson plans and facilitation guidelines
3. **Parameter Cheat Sheet**: Quick reference for educators
4. **Reusable Interface**: Open-source chatbot and logging scripts

### **Community Impact**
1. **Workshop Series**: Training sessions for L2 writing instructors
2. **Open Datasets**: De-identified interaction data for further research
3. **Implementation Guide**: Step-by-step adoption framework for institutions

---

## 7. REFERENCES

**Core DDL & AI in L2 Writing:**
- Crosthwaite, P., & Baisa, V. (2023). Generative AI and the end of corpus-assisted data-driven learning? *Applied Corpus Linguistics*, 3(3).
- Li, S. (2025). Generative AI and second language writing. *Digital Studies in Language and Literature*.
- Michel, M., et al. (2025). Collaborative writing based on generative AI models. *Journal of Second Language Writing*, 67.
- Wang, C., & Wang, Z. (2025). Investigating L2 writers' critical AI literacy in AI-assisted writing. *Journal of Second Language Writing*, 67.

**Human-AI Collaboration:**
- Ashktorab, Z., et al. (2020). Human-AI collaboration in a cooperative game setting. *Proceedings of the ACM on Human-Computer Interaction*, 4(CSCW2), 1-20.
- Clark, E., et al. (2018). Creative writing with a machine in the loop. *Proceedings of the 23rd International Conference on Intelligent User Interfaces*.
- Qian, W., et al. (2023). 'It felt like having a second mind': Investigating human-AI co-creativity in prewriting with large language models. *arXiv:2307.10811*.

**Parameter Studies:**
- Peeperkorn, M., et al. (2024). Is temperature the creativity parameter of large language models? *arXiv:2405.00492*.
- Ravfogel, S., Goldberg, Y., & Goldberger, J. (2023). Conformal nucleus sampling. *arXiv:2305.02633*.
- Üzümcü, T., & Ganiz, M. C. (2025). Analysis of consistency of large language models for low-resource languages. *2025 33rd Signal Processing and Communications Applications Conference*.

**Creative Writing & AI:**
- Chakrabarty, T., Padmakumar, V., & He, H. (2022). Help me write a poem: Instruction tuning as a vehicle for collaborative poetry writing. *arXiv:2210.13669*.
- McGregor, S., Purver, M., & Wiggins, G. (2016). Process-based evaluation of computer generated poetry. *Proceedings of the INLG 2016 Workshop on Computational Creativity in Natural Language Generation*.

**L2 Poetry & Creative Writing:**
- Iida, A. (2016). Second language poetry writing as reflective practice. *Language Teacher Cognition Research Bulletin*, 12(1), 81-93.
- Kerbs, M., McQueston, J., & Lawrance, L. (2024). Playing with words: Scaffolding writing through poetry. *Reading Teacher*, 78(1).

---

**Research Timeline**: September-November 2025 | **Ethics Approval**: Pending | **Funding**: HKBU Graduate Research Support