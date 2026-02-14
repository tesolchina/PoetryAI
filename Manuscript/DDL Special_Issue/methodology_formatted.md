Methodology

Research Design
We designed and deployed a poetry writing platform (poetry.aitutor.ink) that transforms the theoretical framework established in our introduction into a living experimental environment. The web-based platform features a prompt-designed chatbot system with two critical design principles distinguished from commercial AI tools: 1) Commercial AI tools typically position themselves as content generators. Through careful prompt engineering, we constrained the AI to function as a guide rather than ghostwriter. 2) Where commercial AI tools treat parameters as trade secrets, our platform exposes them as manipulable pedagogy. We engineered the system to function as both learning environment and  research instrument. In this way, we can trace the causal pathways through which technical configurations translate into learner experiences.
The platform was built using Lovable with OpenRouter API integration, enabling access to GPT-4 as the underlying language model while maintaining full control over generation parameters.

Prompt Engineering and Parameter Configuration

We crafted prompts that would govern AI behavior across chatrooms, making it impossible to discern whether observed variations stem from how the AI is configured (parameters) or what it is instructed to do (prompts). By holding the prompts while manipulating parameters, we created a clean experimental contrast where differences in interaction patterns could be attributed to different scaffolding strategies under various parameter conditions.
Our prompt defines the chatbot’s role as a poetry writing assistant for L2 learners (CEFR B1-B2 proficiency) and establishes response frameworks supporting all three interaction types:
Type A (Constraint Repair): Diagnostic feedback on structural, linguistic, or poetic elements requiring attention;
Type B (Exemplar Giving): Model texts, phrase alternatives, and curated options for learner selection and adaptation; 
Type C (Surprise Harvest): Creative suggestions, unexpected metaphors, and generative possibilities extending beyond learner’s initial ideas.
The prompt establishes clear conversational boundaries, while encouraging diverse creative perspectives. Rather than positioning the AI as a corrector, the prompt frames it as a collaborative partner in the learner’s creative process.
By establishing two chatroom with different parameter conditions, we re-conceptualizes temperature and top-p as pedagogical design instruments that educators can use to scaffold:
Structured Chatroom: The Steady Guide (in low parameters condition)
Temperature: 0.3 | Top-p: 0.4
Technical function: Tightens the AI’s decision-making scope, producing predictable, corpus-typical outputs.
DDL function: Transforms the AI into a proactive tutor, surfacing linguistic patterns that learners would encounter through traditional corpus searches, but delivering them contextually and conversationally.
Scaffolding function: Generates a teaching style dominated by Type A normative corrections (“This line needs a stronger verb”) and Type B conventional exemplars (“You could try ‘whispers’ instead of ‘says’”), creating heavy scaffolding that reduces cognitive load but risks constraining creative autonomy.
Exploratory Chatroom: The Creative Catalyst (in high parameters condition)
Temperature: 0.8 | Top-p: 0.9
Technical function: Loosens the AI’s generative constraints, sampling from broader, more diverse token distributions, enabling outputs that deviate creatively from corpus norms.
DDL function: Generating linguistic possibilities that transcend training data frequencies.
Scaffolding function: Shifts the interaction ecology toward Type C exploratory divergence (“What if rain becomes hunger in your metaphor?”), providing light scaffolding that sparks creative expansion. 
This parameter-interaction design reveals the mechanism through which AI can dynamically adapt to its pedagogical circumstances, transitioning from structured tutor to exploratory partner simply by adjusting two numerical values. The how of dynamic DDL scaffolding, theorized but yet empirically demonstrated, becomes operationally tractable. 

2.2 Experimental Design: Three-Phase Investigation

  This study employed a three-phase design investigating AI-mediated DDL scaffolding across controlled experimental and naturalistic classroom contexts:
Phase 1: 2×2 Factorial Experiment (N=10)
Design: Controlled laboratory-style experiment manipulating two independent variables:
1. Parameter Configuration (Between-subjects)
Structured: Temperature 0.3, Top-p 0.4 (Rooms A & B)
Exploratory: Temperature 0.8, Top-p 0.9 (Rooms C & D)
2. Awareness Condition (Between-subjects)
Aware: Participants are aware the parameters and their potential effects (Rooms A & C)
Unaware: Participants don’t know about the parameter or their effects (Rooms B & D), serving as control group for isolating genuine parameter effects uncontaminated by demand characteristics.
   This factorial design enabled examination of direct parameter effects (structured vs. exploratory) and meta-cognitive influences of parameter literacy (aware vs. unaware), addressing research questions about both technical mechanisms and learner perceptions under controlled conditions. 

Phase 2: Natural Classroom Environment : Offline In-Person Workshop (N=8)
Design: An offline in-person classroom setting where participants self-selected into parameter conditions based on personal preference and creative goals.
  This phase investigated how learners engage with AI-assisted poetry writing when given agency in a traditional classroom setting, examining the validity of Phase 1 findings while exploring how self-selection of parameter conditions affect creative outcomes, authorship perception, and interaction patterns. 8 L2 learners from Hong Kong Baptist University enrolled. 

Phase 3: Natural Classroom Environment - Online Workshop (N=12)
Design: An online learning environment, maintaining self-selected parameter conditions. This phase shifted from face-to-face to remote interaction to test environmental robustness.
  This phase extended Phase 2 findings across different learning environments (offline vs. online), examining whether parameter effects and interaction patterns remain consistent when learners engage with the platform remotely rather than in physical classroom settings, exploring how online interaction affects learner engagement and creative development. 12 L2 learners from universities across Hong Kong participated. 

Rationale for Three-Phase Design

  The progression from controlled experiment (Phase 1) to naturalistic classroom contexts (Phases 2-3) addresses a critical limitation in educational technology research: findings from tightly controlled laboratory studies often fail to translate to authentic classroom practice. The design strengthens both internal validity (Phase 1’s controlled parameter manipulation) and ecological validity (Phases 2-3’s authentic classroom contexts in different environments). 

Context and Participants
     We recruited 10 L2 English learners from Hong Kong Baptist University through course announcements and digital posters. All participants met CEFR B1-B2 proficiency criteria. Their ages ranged from 18 to 32, with Indian, Thai, Mandarin, and Cantonese L1 backgrounds reflecting Hong Kong’s linguistic landscape. Participants were randomly assigned to experimental rooms, ensuring balanced representation across parameter conditions.

Intervention / Action Plan
Orchestrating the Poetry Writing Experience

All three research sessions unfolded as a 75-minute experience designed to immerse participants in collaborative poetry writing:

 Phase 1: Platform Orientation (10 minutes) Participants logged into their assigned rooms (or self-selected rooms in Phases 2-3), familiarized themselves with the chatbot interface. 

Phase 2: AI-Assisted Poetry Writing (35 minutes) Participants entered  chatrooms where they drafted, revised, and refined poems in conversation with their AI partner.

Phase 3: In-class Reflection Template (15 minutes) Participants responded to reflection on authorship perception, creative satisfaction, and scaffolding experiences.

Phase 4: Panel Discussion (15 minutes) Participants shared their insights on parameter effects, their creative journeys, insights about authorship and collaboration.

Data Collection Methods
2.3 Data Collection and Analysis

Multi-Modal Data Sources

1. Complete Chat Histories
2. Interaction Type Coding: We classified each AI responses according to the three interaction types.
3. Poem Artifacts
4. Reflection Templates: Participants’ reflection templates which consist of five essential questions: (a) authorship perception (b) creative satisfaction (c) most helpful interaction (d) open-ended AI role descriptions, and (e) preferences for future use.
5. Panel Discussion Transcripts: Discussions that reveals poetic understandings, themes, and emotions which are hard to express in reflection templates.

Data Analysis
Quantitative Analysis
We use the three research questions to guide statistical analyses:
RQ1: Do parameter configurations generate distinct interaction type profiles? 
We use Chi-square tests to compare Type A, B, and C distributions across structured vs. exploratory conditions, with Cramér's V measuring effect sizes.
RQ2: How do interaction type profiles relate to authorship perception and creative satisfaction? 
We use Pearson correlations to examine relationships between each interaction type’s frequency (percentage of total AI responses) and outcome measures.
RQ3: Does awareness of parameter settings moderate parameter-driven effects?
We use Two-way ANOVA with parameter configuration (structured/exploratory) and awareness (aware/unaware) as independent variables tested main effects and interactions on authorship and satisfaction.
All statistical analyses used α = .05 significance threshold with effect sizes (Cohen’s d, Cramér’s V, η²) following APA standards. 

Qualitative Analysis
For qualitative analysis, we apply two analytical traditions to examine different facets of creative processes:
Conversation Analysis (Jefferson, 2004): How learners responded to AI suggestions), uptake patterns (active transformation vs. passive acceptance), and scaffolding trajectories (whether support increased, decreased, or remained stable across sessions). 
Discourse Analysis: How spontaneous participant characterizations during panel discussions reveals identity (selector vs. co-creator) under different parameter conditions. Metaphors, agency attributions, and evaluative stance are all considered and analyzed.

Ethical Considerations
Ethical Safeguards and Transparency
All participants provided consent before engaging with the platform. Their Chat logs and personal information were stored in separate databases following HKBU IRB protocols, with data retention and destruction procedures clearly communicated.  
