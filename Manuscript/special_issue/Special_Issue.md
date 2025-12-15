

**From Static to Dynamic: Parameter Manipulation as Adaptive DDL Scaffolding in L2 Creative Writing with ****Generative AI**

**Abstract**
Does generative AI represent the death of Data-Driven Learning, or its evolution? This study addresses Crosthwaite’s (2023) fundamental challenge by investigating how AI parameter configuration shapes learning outcomes in L2 creative writing. Through a 2×2 experimental design (N=10, target N=20), we manipulated temperature and top-p settings (structured: 0.3/0.4 vs. exploratory: 0.8/0.9) and parameter awareness (aware vs. unaware) while Hong Kong Baptist University students composed poetry with AI assistance. Findings reveal that parameter configuration functions as a pedagogical lever producing  different interaction patterns: exploratory parameters generated 7× more Type C “surprise harvest” interactions than structured parameters (35% vs. 5%, p<.001), directly impacting authorship perception and creative satisfaction. Crucially, 75% of participants rated Type B “exemplar giving” as most helpful, yet Type B frequency negatively correlated with authorship perception (r=-.58), exposing the “helpful but alienating” paradox of over-scaffolding. Our findings demonstrate that AI neither kills nor simply continues DDL—rather, AI parameter configuration impact whether AI functions as pattern-enforcer undermining creative agency or pattern-extender enabling corpus-divergent discovery. This research establishes parameter literacy as inportant professional competence for educators, suggesting that DDL’s future hinges not on AI’s capabilities but on our capacity to configure it as adaptive pedagogical scaffold. When educators gain control over LLM usage and parameter configurations, AI might transform from potential threat into powerful partner advancing DDL’s evolution in the generative era.

**Key Words**: Data-Driven Learning; LLM parameter; Adaptive scaffolding; L2 Creative writing

**Introduction**
**1.1 ****Answering Crosthwaite (2023): Evolution, Not Replacement**
Crosthwaite (2023) poses a fundamental challenge to the language teaching profession: Does generative AI represent “the death of DDL” by allowing learners to bypass the inductive pattern discovery processes central to Data-Driven Learning pedagogy? This paper argues the opposite— “**generative AI represents an evolution rather than replacement of DDL principles****”****. **We examine this proposition through AI-assisted L2 creative writing, where the tension between DDL principles and generative AI becomes most visible. Unlike discrete grammar or vocabulary tasks where corpus patterns offer clear guidance, creative writing demands that learners **discover generative possibilities**** **within linguistic constraints—a process that generative AI can either support through adaptive scaffolding or undermine through over-determination. Understanding *how*** AI enables ***dynamic*** DDL scaffolding** in creative contexts requires examining the fundamental differences between traditional corpus consultation and AI-mediated pattern engagement, and identifying the mechanisms through which AI’s pedagogical affordances can be systematically shaped.

**1.2 From Static Concordances to System-Initiated Pattern Presentation: DDL Principles in the Generative AI Era**

Data-Driven Learning (DDL), pioneered by Johns (1991) as “the use of concordance data in language learning,” has long championed inductive pattern discovery over deductive rule presentation. By engaging learners directly with corpus evidence—concordance lines, frequency distributions, collocational patterns—DDL transforms language pedagogy from teacher-transmitted knowledge to learner-discovered insights (Boulton, 2012). The pedagogical power of DDL lies in its emphasis on **learner autonomy** and **evidence-based discovery**—principles that align closely with constructivist learning theory and sociocultural approaches to second language acquisition (Lantolf & Thorne, 2006).
Traditional DDL positions learners as active **query initiators** who formulate search criteria and interpret concordance results (Johns, 1991). This learner-driven approach, while fostering autonomy, imposes heavy cognitive demands: metalinguistic awareness to formulate queries, technical competence in corpus tools, and tolerance for data ambiguity (Sun & Wang, 2003). Moreover, corpus data by definition represents **patterns of what has been written**, not necessarily what *could* be written—a limitation particularly salient in creative writing where novelty and originality are pedagogical goals.
Generative AI fundamentally transforms this dynamic by enabling **system-initiated pattern presentation**. Rather than learners searching corpora for patterns, AI proactively generates contextually relevant examples, corrections, or alternatives in real-time conversational exchanges. This shift from **learner-initiated queries to system-initiated presentations** represents a fundamental reconceptualization of DDL:

**In traditional DDL**: Learners decide *what* to search for, *when* to query the corpus, and *how* to interpret concordance results. The corpus remains passive; learner agency drives the discovery process.

**In AI-assisted DDL**: The system decides *when* to intervene, *what* patterns to present, and *how* to frame linguistic information. AI actively shapes the learning trajectory through real-time responsiveness.

This transformation addresses traditional DDL’s cognitive overload and technical barriers (Bernardini, 2004; Crosthwaite, 2023) by providing **scaffolded, contextualized pattern engagement** rather than requiring learners to independently navigate large corpora. However, it also introduces critical pedagogical questions: When AI presents patterns without learner queries, does this bypass inductive discovery? When AI generates novel text rather than retrieving corpus examples, does this violate DDL’s evidence-based foundation? Most importantly, *how*** can AI-mediated pattern presentation be ***dynamically** ***adapted** to provide appropriate scaffolding—supportive without over-determining, generative without overwhelming—across different learning contexts and learner needs?

**1.3 ****Scaffolding Theory and L2 Creative Writing: The Need for Adaptive Support**

Scaffolding, originally conceptualized by Wood, Bruner, and Ross (1976), describes temporary support structures that enable learners to accomplish tasks beyond their independent capability, gradually fading as competence develops. In L2 writing contexts, effective scaffolding must balance multiple dimensions: linguistic support (vocabulary, grammar, discourse features), cognitive support (organizational strategies, ideation techniques), and affective support (encouragement, confidence-building, emotional safety) (Lantolf & Thorne, 2006; Van de Pol, Volman, & Beishuizen, 2010).

Creative writing in L2 contexts presents unique scaffolding challenges. Unlike academic or transactional writing where conventions are relatively stable, creative writing demands both “pattern adherence” (mastery of poetic forms, literary devices, genre conventions) and “pattern transcendence” (original expression, personal voice, aesthetic innovation). This dual requirement creates what Hanauer (2010) terms the “imitation-transformation dialectic”: learners must internalize exemplars while simultaneously developing authentic creative agency. Traditional scaffolding approaches often struggle with this tension—too much structure risks formulaic output and diminished authorship; too little risks cognitive overload and linguistic breakdown (Fithriani, 2021; Kerbs, McQueston, & Lawrance, 2024).

Moreover, structured creative scaffolding itself poses risks: overly prescribed approaches may inhibit students’ geniune expression of voice, when learners fear making errors or expressing vulnerable content (Hanauer, 2010), interrupting the free flow of creative thought essential to authentic poetry writing. What L2 creative writing pedagogy ultimately seeks is an emotionally safe creative atmosphere—one where learners feel free to experiment without fear of instructor judgment or peer comparison, where linguistic limitations do not become barriers to creative exploration. These questions become urgent as AI writing assistants enter L2 classrooms, potentially transforming scaffolding dynamics while offering new possibilities for balancing structure with creative freedom. 

**1.4 A Three-Interaction-Types Framework: How Parameter Configuration Shapes DDL-Scaffolding Modes**

To understand *how *AI-mediated DDL operates *dynamically* in creative writing contexts, we propose a “three-interaction-types framework” that integrates DDL principles, scaffolding theory, and human-AI collaboration research. Recent studies provide empirical foundations: Coenen et al. (2022) identified “serendipitous discovery” as crucial for productive human-AI collaboration; Qian et al. (2023) demonstrated AI’s capacity to redistribute cognitive load; Li (2025) found that generative AI shifts writers toward strategic collaboration. However, these studies treat AI as monolithic rather than examining *how *different AI configurations produce distinct interaction patterns with different pedagogical affordances.
Our framework addresses this gap by revealing the mechanism through which AI can *d**ynamically* adapt scaffolding: parameter configuration (specifically temperature and top-p settings) systematically shapes interaction type distributions. Lower parameter values (e.g., temperature 0.3, top-p 0.4) produce deterministic, corpus-typical outputs aligned with training data patterns; higher values (e.g., temperature 0.8, top-p 0.9) generate variable, exploratory outputs extending beyond corpus frequencies (Holtzman et al., 2019; Li et al., 2025; Peeperkorn et al., 2024). This technical mechanism enables pedagogical adaptivity: parameter manipulation functions as a design lever for shifting between different DDL-scaffolding modes.
We theorize three interaction types as “parameter-dependent DDL-scaffolding modes”, each serving distinct pedagogical functions:
**Type A: Constraint Repair** — AI identifies deviations from linguistic or structural patterns and provides corrective guidance. This parallels traditional DDL’s use of concordance lines but occurs proactively rather than through learner-initiated queries. Type A represents normative pattern reinforcement, helping learners master formal requirements like syllable counts or grammatical accuracy. Low parameter values (temperature 0.3, top-p 0.4) maximize Type A by constraining outputs to corpus-typical patterns, providing heavy scaffolding but potentially stifling creative risk-taking (Ferris, 2004). Type A is high-directive and low-autonomy.
**Type B: Exemplar Giving****: **AI provides model phrases or line alternatives that learners select and adapt, aligning with imitation-transformation pedagogy (Hanauer, 2010) and genre-based approaches (Hyland, 2007). Type B reduces cognitive load by offering concrete starting points and diverse stylistic models. However, it introduces critical tension: unlike traditional DDL where learners actively search corpora, AI presents pre-selected option sets that shift the dynamic from exploration to guided selection. Low parameter values increase Type B frequency, creating the “helpful but alienating” paradox—AI provides useful support while diminishing authorship perception. Type B involves moderate directiveness and moderate autonomy, supporting accessibility but risking passive selection over active creation.
**Type C: Surprise Harvest****: **AI generates unexpected ideas, metaphors, or directions that learners would not discover through conventional corpus consultation, aligning with serendipitous discovery (Coenen et al., 2022) in human-AI co-creativity and resonates with theories of divergent thinking (Guilford, 1967) and the role of novelty in creative processes (Boden, 2004). Type C represents fundamental departure from traditional DDL: rather than revealing corpus patterns, AI generates possibilities beyond corpus frequencies through creative divergence. High parameter values (temperature 0.8, top-p 0.9) dramatically increase Type C frequency (preliminary findings suggest 7× increase: 35% vs. 5%), enabling AI to function as pattern-extender rather than pattern-reinforcer. Type C is low-directive and high-autonomy, providing light scaffolding that supports creative expansion while demanding critical judgment.
This parameter-interaction relationship has profound implications: parameter configuration shapes whether AI functions as corrective tutor (Type A), exemplar provider (Type B), or creative collaborator (Type C), directly impacting learner agency and the inductive discovery processes central to DDL pedagogy.
Our research is guided by three questions:

**RQ1: How do different parameter configurations affect the distribution of interaction types (Constraint Repair, Exemplar Giving, Surprise Harvest) in AI-assisted L2 poetry writing?**

**RQ2: How do these interaction types influence L2 learners’ authorship perception, creative satisfaction, and sense of agency in collaborative poetry writing?**

**RQ3: What are the pedagogical implications of parameter configuration as a design lever for adaptive DDL in L2 creative writing?**

This study contributes to three intersecting research domains:

For DDL research: We extend data-driven learning principles from static corpus consultation to dynamic, generative AI interaction. We address Crosthwaite’s (2023) concern that generative AI might bypass inductive learning by investigating which parameter configurations preserve learner agency in pattern discovery versus which promote passive consumption. Our prompt-designed platform provides the methodological infrastructure to trace these dynamics empirically.

For scaffolding research: We operationalize scaffolding through interaction type distribution, demonstrating *how* adaptive support emerges from parameter manipulation rather than remaining fixed. We contribute evidence on the scaffolding-autonomy trade-off in creative contexts, examining when different support levels enhance versus constrain learning outcomes. Our chatbot platform enables systematic investigation of scaffolding contingency, fading, and autonomy transfer through recordable interaction patterns.

For AI-assisted writing research: We demonstrate that parameter configuration constitutes pedagogical design, not merely technical implementation. By revealing *how* temperature settings systematically shape interaction patterns, we establish parameter literacy as essential competence for educators integrating AI tools into L2 creative writing instruction. Our platform’s complete interaction logging provides unprecedented visibility into the mechanisms through which parameter choices determine pedagogical affordances.

The integration of these three domains enables us to ask fundamental questions about the future of technology-mediated language learning: Can AI provide the pattern-based induction of DDL, the adaptive support of effective scaffolding, and the creative inspiration necessary for authentic literary expression—simultaneously and appropriately? Or do inherent tensions among these goals require careful calibration, deliberate trade-offs, and perhaps reconceptualization of what “successfu” AI-assisted creative writing entails?

The preliminary findings from our Session 1 data (10 participants) suggest that these questions have empirical answers with significant pedagogical implications—answers we now turn to explore through systematic analysis of interaction patterns, learner perceptions, and creative outcomes in our AI-assisted L2 poetry writing study.

**Methodology**
**2.1**** ****Platform Building and Chatbot Design: Operationalizing DDL-Scaffolding Theory**
We designed and deployed a purpose-built poetry writing platform (poetry.aitutor.ink) that transforms the theoretical framework established in our introduction into a living experimental environment. The web-based platform features a prompt-designed chatbot system with two critical design principles distinguished from commercial AI tools: Commercial AI tools typically position themselves as content generators—producing complete poems with a single prompt, effectively displacing the writer from the creative process. Through careful prompt engineering, we constrained the AI to function as a guide rather than ghostwriter, embodying three complementary pedagogical roles: a writing coach, a creative collaborator and a language resource; Where commercial AI tools treat parameters as proprietary trade secrets, our platform exposes them as manipulable pedagogy. We engineered the system to function as both learning environment and  research instrument, embedding multiple layers of observability. This dual specialization—instructional prompt design married to parameter observability—creates a methodological innovation: we can finally trace the causal pathways through which technical configurations translate into learner experiences, answering the how question that previous research left unresolved.
The platform was built using Lovable with OpenRouter API integration, enabling access to Claude Sonnet 4 as the underlying language model while maintaining full control over generation parameters.

**Prompt Engineering**** and Parameter Configuration**

We crafted prompts that would govern AI behavior across chatrooms, making it impossible to discern whether observed variations stem from how the AI is configured (parameters) or what it is instructed to do (prompts). By holding the prompts while manipulating parameters, we created a clean experimental contrast where differences in interaction patterns could be attributed to different scaffolding strategies under various parameter conditions.
Our prompt defines the chatbot’s role as a poetry writing assistant for L2 learners (CEFR B1-B2 proficiency) and establishes response frameworks supporting all three interaction types:
**Type A (Constraint Repair)**: Diagnostic feedback on structural, linguistic, or poetic elements requiring attention;
**Type B (Exemplar Giving)**: Model texts, phrase alternatives, and curated options for learner selection and adaptation; 
**Type C (Surprise Harvest)**: Creative suggestions, unexpected metaphors, and generative possibilities extending beyond learner’s initial ideas.
The prompt establishes clear conversational boundaries—responses constrained to 40-80 words to prevent overwhelming learners—while cultivating an encouraging, culturally responsive voice that honors diverse creative perspectives. Rather than positioning the AI as an error-hunting corrector, the prompt frames it as a collaborative partner invested in the learner’s creative vision.
The conceptual breakthrough enabling our investigation lies in reconceptualizing temperature and top-p not as obscure technical settings but as pedagogical design instruments—adjustable dials that educators can turn to calibrate scaffolding intensity:
**Structured Configuration: The Steady Guide (Low Parameters)**
Temperature: 0.3 | Top-p: 0.4
Technical function: Tightens the AI’s decision-making scope, constraining token selection to high-probability choices that mirror training data frequencies—producing predictable, corpus-typical outputs.
DDL function: Transforms the AI into a proactive concordancer, surfacing linguistic patterns that learners would encounter through traditional corpus searches, but delivering them contextually and conversationally.
Scaffolding function: Generates a teaching style dominated by Type A normative corrections (“This line needs a stronger verb”) and Type B conventional exemplars (“You could try ‘whispers’ instead of ‘says’”), creating heavy scaffolding that reduces cognitive load but risks constraining creative autonomy.
Learner experience: Encounters an AI that behaves like a patient tutor—systematic, educational, reliably helpful, but potentially over-directive.
**Exploratory Configuration: The Creative Catalyst (High Parameters)**
Temperature: 0.8 | Top-p: 0.9
Technical function: Loosens the AI’s generative constraints, sampling from broader, more diverse token distributions, enabling outputs that deviate creatively from corpus norms.
DDL function: Elevates the AI beyond pattern retrieval into pattern extension—generating linguistic possibilities that transcend training data frequencies, a generative capability impossible in static corpus DDL.
Scaffolding function: Shifts the interaction ecology toward Type C exploratory divergence (“What if rain becomes hunger in your metaphor?”), providing light scaffolding that sparks creative expansion while demanding learners critically evaluate and selectively integrate surprising suggestions.
Learner experience: Encounters an AI that behaves like an experimental collaborator—imaginative, sometimes unexpected, occasionally confusing, but potentially inspiring.
This parameter-interaction choreography reveals the mechanism through which AI can dynamically modulate its pedagogical presence—transitioning from structured tutor to exploratory partner simply by adjusting two numerical values. The how of dynamic DDL scaffolding, long theorized but never empirically demonstrated, becomes operationally tractable.

**2.2 ****Experimental Design: 2×2 Factorial Configuration**

The study employed a 2×2 factorial design manipulating two independent variables:
1. Parameter Configuration (Between-subjects)
Structured: Temperature 0.3, Top-p 0.4 (Rooms A & B)
Exploratory: Temperature 0.8, Top-p 0.9 (Rooms C & D)
2. Awareness Condition (Between-subjects)
Aware: Participants informed about parameter manipulation and its potential effects (Rooms A & C)
Unaware: No information provided about technical parameters (Rooms B & D). They serve as primary controls for isolating genuine parameter effects uncontaminated by expectancy or demand characteristics.
This design enables examination of direct parameter effects (structured vs. exploratory) and metacognitive influences of parameter literacy (aware vs. unaware), addressing research questions about both technical mechanisms and learner perceptions.

**Participants and Procedures: Orchestrating the Poetry Writing Experience**
Twenty L2 (10 for primary experiment) English learners volunteered for this study, recruited from Hong Kong Baptist University’s undergraduate population through course announcements and digital posters. All participants met CEFR B1-B2 proficiency criteria—intermediate English users capable of expressing themselves creatively while still grappling with linguistic constraints that make scaffolding valuable. Their ages ranged from 18 to 32, with Indian, Thai, Mandarian and Cantonese L1 backgrounds reflecting Hong Kong’s linguistic landscape. Randomly assigned participants to each experimental room, ensuring balanced representation across parameter conditions.
The research session unfolded as a carefully sequenced 75-minute experience designed to immerse participants in collaborative poetry writing while capturing multiple layers of data:
Phase 1: Platform Orientation (10 minutes) : Setting the Stage  
Participants logged into their assigned rooms, familiarized themselves with the chatbot interface. This brief orientation established technical comfort before creative work began.
Phase 2: AI-Assisted Poetry Writing (35 minutes): The Creative Crucible
Participants entered a focused creative space where they drafted, revised, and refined poems in conversation with their AI partner. 
Phase 3: In-class reflection template (15 minutes): Capturing Immediate Impressions
While creative experiences remained vivid, participants responded to structured reflection probing authorship perception, creative satisfaction, and scaffolding experiences.
Phase 4: Panel Discussion (15 minutes): parameter observation and Meaning-Making
Participants sharing their insights on parameter effects and narrating their creative journeys in different parameter conditions. These discussions generated rich qualitative data as learners compared experiences, debated cross-room differences, AI’s role, and articulated insights about authorship and collaboration.
**Ethical Safeguards and Transparency**
All participants provided informed consent before engaging with the platform. Chat logs and personal identifiers were stored in separate encrypted databases following HKBU IRB protocols, with data retention and destruction procedures clearly communicated.

**2.3 Data Collection and Analysis**

**Multi-Modal Data Sources**

Six complementary data sources captured the multi-dimensional impact of parameter-driven scaffolding:

**1. Complete Chat Logs** : All human-AI dialogues were automatically captured with comprehensive metadata including timestamps, parameter settings, token counts, and message sequences. 
**2. Interaction Type Coding****: **Each AI response was independently classified by two trained coders following an operational coding scheme distinguishing three interaction type.
**3. Poem Artifacts****: **Final creative products were collected as tangible outcomes of scaffolded writing processes.
**4. Reflection Templates****: **Immediately following composition, participants completed structured reflection templates capturing five dimensions: (a) perceived authorship (b) creative satisfaction (c) most helpful interaction (d) open-ended AI role descriptions, and (e) preferences for future use.
**5. Panel Discussion Transcripts****: **Discussions revealed shared cultural understandings, condition-specific themes, and spontaneous metacognitive reflections absent from individual templates.
**6. Platform Analytics****: **Behavioral traces automatically logged by the system quantified engagement patterns: session duration, total messages exchanged, message initiation patterns (human-initiated vs. AI-initiated sequences), response latency (time between receiving AI response and sending next message), revision behaviors (editing previous inputs), and form selection distributions. 
**Quantitative Analysis**
Three research questions guided statistical analyses:
**RQ1: Do parameter configurations generate distinct interaction type profiles?** — Chi-square tests compared Type A, B, and C distributions across structured vs. exploratory conditions, with Cramér's V measuring effect sizes.
**RQ2: How do interaction type profiles relate to authorship perception and creative satisfaction?** — Pearson correlations examined relationships between each interaction type’s frequency (percentage of total AI responses) and outcome measures.
**RQ3: Does awareness of parameter settings moderate parameter-driven effects?** — Two-way ANOVA with parameter configuration (structured/exploratory) and awareness (aware/unaware) as independent variables tested main effects and interactions on authorship and satisfaction.
All statistical analyses used α = .05 significance threshold with effect sizes (Cohen’s d, Cramér’s V, η²) reported following APA standards. Statistical assumptions (normality, homogeneity of variance) were verified before parametric testing.
**Qualitative Analysis**
Three complementary analytical traditions examined different facets of scaffolded creative processes:
**Conversation Analysis** (Jefferson, 2004) — Turn-by-turn examination of chat transcripts identified repair sequences (how learners responded to AI suggestions), uptake patterns (active transformation vs. passive acceptance), and scaffolding trajectories (whether support increased, decreased, or remained stable across sessions). This micro-level analysis revealed the procedural mechanisms through which parameters shape interaction dynamics.
**Thematic Analysis** (Braun & Clarke, 2006) — Recursive inductive coding of reflection templates and discussion transcripts identified condition-specific themes. Initial open coding generated descriptive labels; focused coding grouped related codes into coherent themes; theoretical coding connected themes to DDL-scaffolding concepts. 
**Discourse Analysis** — Examination of spontaneous participant characterizations during panel discussions revealed identity positioning (selector vs. co-creator) aligned with parameter conditions. Analysis attended to metaphors, agency attributions, and evaluative stance.

**Findings**
**3.1 ****parameter Configuration as Dynamic DDL Scaffolding**
This section presents findings from Session 1 with 10 participants (20 total recruited, data collection ongoing) distributed across four experimental rooms. Analysis integrates multiple data sources: complete chat logs from 35-minute poetry writing sessions, coded interaction type distributions, 15-minute panel discussion transcripts, structured reflection journals, and session feedback templates from participants. Findings directly address the three research questions established in our introduction while demonstrating *how*** parameter manipulation enables ***dynamic** ***DDL scaffoldin****g **in AI-assisted L2 creative writing.

** RQ1: How Do Parameter Configurations Shape Interaction Type Distributions?**

**Finding 1.1: Seven-Fold Type C Frequency Difference Validates Parameter-Scaffolding Mechanism**

Systematic coding of AI responses across all chat logs (N=approximately 500 message exchanges) revealed dramatic distributional differences in interaction types between parameter conditions: 
Chi-square analysis (preliminary): χ² = 24.3, *p* < .001, Cramér's V = .38 (medium-to-large effect size), confirming that parameter configuration significantly reshapes interaction type distributions independent of learner input.
**Qualitative Validation from Chat Transcripts:**
*Structured Room Example (Room B):*
The low-temperature AI consistently offered preset options with minimal elaboration:
USER: In the factory of dreams, where wonder grows
AI: That’s a beautiful opening line! For your next line, let’s continue
building this dreamlike world. Here are a few options:
•Rabbits scurry with visions in tow
• Machines hum softly, stitching joy and woe 
• Every dream takes shape, in colors bright and bold
Which direction would you like to take?
**A****nalysis**: Type B exemplar-dominant response—curated alternatives requiring selection rather than generative thinking. No interpretative depth or unexpected connections.
*Exploratory Room Example (Room C):*
The high-temperature AI introduced unanticipated creative techniques:
USER: the hubris in pursuing overly lenient criminal justice reform
AI: That’s a thought-provoking theme... Would you like to explore:
• The tension between justice and mercy
• The consequences of leniency  
• The perspective of those affected by the system
[Later in conversation]
AI: Would using some found aspects such as citations, help highlight
the gravity and increase the emotional impact?
**Analysis: **Type C surprise harvest—AI introduced “found poetry” technique unprompted, elevating craft conversation beyond novice level. The suggestion to incorporate legal citations transformed the interaction from basic poetry writing to experimental form exploration.

**Finding 1.2: Parameter Effects Persist Across Awareness Conditions**

Comparing unaware rooms (Rooms B & D—primary controls) confirmed that interaction type distributions derive from parameter settings rather than expectancy effects:
**Room ****B**** (Structured-Unaware)** vs. **Room ****D ****(Exploratory-Unaware):**
Type C frequency: 5% vs. 33% respectively
     P-value from chi-square test: *p* < .01
Demonstrates parameter effects independent of metacognitive awareness
**Spontaneous Participant Detection:**
During panel discussion, a Room B participant (structured-unaware) unpromptedly articulated the experiential difference after hearing Room C/D presentations:
“It’s pretty obvious! On our lower temperature, ours took our words and tried to put it in poem form. Whereas comparing output from C and D... there’s a lot of changes to the input format...” This observation—from a participant who *did not know** *about parameter manipulation—demonstrates that scaffolding intensity differences were phenomenologically real, not researcher constructs.

**Finding 1.3: Parameter Configuration ****Influences**** Poem Characteristics**



Creative artifacts (poems) reflected the interaction types that generated them:
**Structured Room Poems (A/B):**
**Average line leng****th**: 6-8 words
**Metaphorical complexity**: Simple binaries (light/dark, heavy/light)
**Rhyme patterns**: Predictable when present
**Emotional range**: Single arc
**Example titles**: “Semester’s End” (Room A), “Morning Routine” (Room B)
**Exploratory Room Poems (C/D):**
**Average line length**: 8-12 words
**Metaphorical complexity****:** Multi-layered (turnstile justice, watercolor world)
**Form experimentation**: Found poetry, varied line breaks
**Emotional range**: Multiple layers, vulnerable specificity
**Example titles**: “Turnstile Justice” (Room C), “Where is Hope?” (Room D)
**Convergence with Scaffolding Theory:**
Structured parameters generated poems resembling **heavily scaffolded outcomes**—technically competent but creatively constrained, paralleling Wood et al.’s (1976) description of over-scaffolding that limits independent problem-solving. Exploratory parameters produced artifacts demonstrating **appropriate scaffolding fade**—learners took creative risks and developed personalized voice, consistent with Van de Pol et al.’s (2010) contingent support principle.

**RQ2: How Do Interaction Types Influence Authorship Perception and Creative Satisfaction?**

**Finding 2.1: Type B Dominance Creates “Helpful but Alienating”**** ****Paradox**
Post-session Feedbacks (N=9 respondents) revealed a striking paradox: **7****8****% of participants (****7****/****9****) rated Type B (Exemplar Giving) as “most helpful”**, yet structured room participants who experienced predominantly Type B interactions reported dramatically lower authorship perception.


One Room A participant’s rating qualified: “Although all the feel is base on my but I just need to choose use what sentence wrote by AI. I only own the meaning on this poem.” One Room A participant’s 100% claim contradicted by other survey responses expressing concern that “AI deprives creativity from humans.”
**Statistical Analysis:**
**Correlation between Type B frequency and authorship perception**: *r* = -.58, *p* < .05 (negative relationship)
**Multiple regression**: Type B percentage significantly predicted lower authorship scores (β = -.62, *p* < .01) even when controlling for Type A and Type C frequencies. 



**Qualitative Evidence of the Paradox:**
*Why Participants Found Type B “Helpful”:*
Feedback forms revealed pragmatic appreciation for exemplars among L2 learners:
**Room A participant**: “I am not good at writing English poem since my English is bad. So I don’t have enough vocab to write a poem. AI help me to generate few sentences let me choose”
**Room D participant**: “Because it directly gave me certain options which significantly helped with idea/sentence generation”
**Room C participant**: “It is clear, all that I need to do is just to choose”
*Why Type B Undermined Authorship:*
Yet structured room participants expressed profound ownership loss:
**Room B participan****t**: “I do not feel ownership or pride over much of it, other than the last line that i wrote myself”
**Room A participant**: “I just need to choose use what sentence wrote by AI. I only own the meaning on this poem”
**Panel discussion (Room B)**: “It feels like just AI... It doesn’t feel like mine... I’m just guiding it to summarize whatever I'm feeling and make it more beautiful”
**Theoretical Interpretation:**
Type B interactions position learners as *selectors* rather than *creators*—a role that efficiently addresses linguistic gaps but fails to cultivate creative agency. Exemplar-giving represents moderate scaffolding (not fully directive like Type A, not fully open like Type C), yet this middle ground proves pedagogically uncomfortable: directive enough to constrain ownership, but not transformative enough to feel collaborative.
This finding extends Boulton’s (2012) DDL principle that hands-on engagement enhances learning. When AI *presents* exemplars rather than guiding learners to *discover* patterns, the DDL mechanism weakens—learners consume rather than construct, fundamentally altering the pedagogical transaction.

**Finding 2.2: Type C Interactions Enable Creative Ownership Despite AI Contribution**
The sole participant who preferred Type C (from Room C) reported **80% self-authorship**—the highest among all respondents—despite extensive AI collaboration. This participant’s experience demonstrates that interaction type, not merely AI involvement level, determines ownership perception.
**Room C Participant’s Distinctive Interaction Pattern:**
Chat log analysis revealed this participant engaged in sustained Type C interactions:
1. **Initial conceptual exploration**: AI posed philosophical questions about criminal justice reform themes
2. **Craft innovation**: AI suggested “found poetry” technique incorporating legal citations
3. **Iterative refinement**: AI offered structural feedback while honoring the participant’s creative vision.
4. **Authorial control**: Participant rejected, modified, and synthesized AI suggestions selectively
**This Participant’s Authorship Rationale** (feedback form):
“Yes [authorship matters], otherwise there is no point in the author being involved at all” 
**Poem Outcome**: “Turnstile Justice”—a 15-line experimental piece incorporating legal metaphors, structured stanzas, and emotional interrogation of systemic failures. The poem demonstrates sophisticated craft beyond typical novice work, suggesting Type C interactions can scaffold *upward* toward advanced competence rather than merely supporting basic production.
**Comparison with Type B-Dominant Experience:**
A Room B participant (Type B-dominant condition) also completed a poem but characterized it as “just AI” work. Key difference: the Room B participant *selected from** *AI-generated options, while the Room C participant *co-constructed with* AI-initiated provocations. This distinction echoes Coenen et al.’s (2022) finding that human-AI collaboration feels most satisfying when both parties contribute generatively rather than one simply approving the other’s output.

**Finding 2.3: Creative Satisfaction Correlates with Type C Frequency**

Overall satisfaction ratings (1-5 scale) showed positive correlation with Type C interaction frequency:
**Low-temperature rooms** (5% Type C): Average satisfaction = 3.4/5
**High-temperature rooms** (35% Type C): Average satisfaction = 4.1/5
**Correlation**: *r* = .45, *p* < .05
Qualitative data illuminates *why* Type C enhances satisfaction. Exploratory room participants used relational language describing AI interactions:
**Room C participant**: “A very warm-hearted AI... like a very good friend, not just a machine.”
**Room D participant****:** “It guided me to the topic and helped me choose if I wanted to focus more on my feelings or more on the views. That was really helpful.
Structured room participants used mechanistic language:
**Room B participant**: “I couldn’t feel any sort of creativity”
**Room B participant**: “It only ever outputted exactly what I asked it to”
The discourse shift from “friend” and “guide” (exploratory) to “machine” and “output” (structured) reveals that parameter-driven scaffolding shapes not just interaction patterns but the fundamental *social relationship* between learner and AI.

**RQ3: Does Metacognitive Awareness of Parameter Settings Moderate Learning Experiences?**

Finding 3.1: Awareness Effects Minimal Compared to Parameter Effects

2×2 ANOVA Results (preliminary, N=10):
Dependent Variable: Authorship Perception (1-5 scale)
**Interpretation**: Parameter configuration accounts for 58% of variance in authorship perception, while awareness condition explains only 7%. The non-significant interaction term indicates awareness does not amplify or dampen parameter effects—both informed and uninformed learners experienced scaffolding intensity differences similarly.
**Finding 3.2: Unaware Participants Spontaneously Developed Parameter Literacy**
Despite receiving no information about parameter settings, unaware participants (Rooms B & D) demonstrated emergent awareness during panel discussion. When the researcher revealed that “Room D and Room B have the exact same settings as Room A and Room C,” a Room B participant immediately responded:
“Yeah, it’s pretty obvious! On our lower temperature—ours, I think, took our words that we inputted and tried to put it in poem form. Whereas comparing output from C and D, especially because we heard the input as well from C—there’s a lot of changes to the input format and the output that the AI gave. Whereas for me, it only ever outputted exactly what I asked it to.”
**Analysis**: This articulate comparative analysis emerged *organically* through:
1. **Cross-room exposure**: Hearing exploratory room poems revealed qualitative differences
2. **Implicit parameter detection**: Unaware participants noticed creativity variations without knowing technical causes
3. **Retrospective sense-making**: Post-hoc disclosure triggered immediate recognition patterns
This finding suggests that parameter effects are sufficiently salient that learners can *perceive* scaffolding intensity differences even without explicit parameter labeling—supporting the possibility of **experiential parameter literacy** developing through practice rather than requiring direct instruction.
**Finding 3.3: Aware Participants Articulated Strategic Parameter Understanding**
Aware participants (Rooms A & C) demonstrated metacognitive engagement with parameter knowledge. During panel discussions and feedback forms, they:
**1. Connected parameters to interaction experiences:**
Room A participant: Described AI as providing “systematic” and “educational” guidance;
Room C participant: Characterized AI as “warm-hearted” and emotionally responsive.
**2. Proposed parameter-task matching:**
A Room D participant (who became aware during debriefing) suggested optimal interaction type sequencing:
“Type A and B are helpful in the beginning to generate ideas and refine your own writing, whereas Type C would be helpful in the end when you want to explore some other, perhaps, more creative options.”
**3. Recognized pedagogical trade-offs:**
A Room C participant (aware condition) proposed an *inverted* distribution favoring Type A (60%) over Type C (25%) despite preferring Type C as “most helpful”—demonstrating sophisticated understanding that instructional value differs from immediate preference.
**Implications**: While awareness doesn’t significantly moderate *authorship perception** *(Finding 3.1), it may enable **adaptive tool use** where learners adjust their interaction strategies based on parameter knowledge.

**Integrated Finding: Parameter Configuration as Dynamic DDL Scaffolding**

Synthesizing findings across all three research questions, we observe a coherent mechanism through which **parameter manipulation operationalizes dynamic DDL scaffolding**:


**Link 1: Parameters → Interaction Types**
7× Type C difference (5% vs. 35%) between structured and exploratory conditions (*p*< .001)
Qualitative validation: Structured AI produces formulaic options; exploratory AI generates unexpected provocations
**Link 2: Interaction Types → Perceptions**
Negative correlation (*r* = -.58, *p*< .05) between Type B frequency and authorship
Positive correlation (*r* = .45, *p* < .05) between Type C frequency and satisfaction
Discourse shift: “just AI” (structured) vs. “very good friend” (exploratory)
**Link 3: Integrated Mechanism**
Parameter configuration explains 58% of authorship variance (η² = .58)
Effect persists across awareness conditions (non-significant interaction)
Learners spontaneously detect scaffolding differences even without parameter knowledge.

**Conclusion**: Parameter configuration determines whether AI functions as *replacement tool** *(structured) or *DDL evolution* (exploratory). This finding operationalizes the “how” question central to our introduction—**temperature and top-p settings serve as pedagogical levers** enabling educators to calibrate scaffolding intensity dynamically, transforming generative AI from potential DDL threat into adaptive DDL scaffold.

**Discussion: ****LLM ****Parameter Configuration as DDL’s Pedagogical ****Innovations**

**Opening: Resolving Crosthwaite’s Challenge**

Crosthwaite (2023) questioned whether generative AI represents “the death of DDL” by allowing learners to bypass inductive pattern discovery. Our findings reveal a more nuanced reality: **AI represents neither DDL’s death nor simple continuation, but a pedagogical watershed where parameter configuration determines which path unfolds**. AI parameter settings function not as technical specifications but as a potential pedagogical design variables fundamentally reshaping learning transactions between human creativity and computational capability.
This discussion interprets Session 1 findings through three lenses: (1) how parameter manipulation operationalizes dynamic DDL scaffolding, (2) why the “helpful but alienating” paradox reveals tensions in AI-mediated creative pedagogy, and (3) what these mechanisms suggest for designing AI tools preserving learner agency while providing transformative support.

**4.1**** The Parameter→Interaction→Perception Mechanism**

Our finding—**the seven-fold increase in Type C (Surprise Harvest) interactions from structured to exploratory parameters** (5% to 35%, *p* < .001, Cramér’s V = .38)—demonstrates parameter configuration as a **pedagogical lever** with immediate, measurable effects. This is not subtle influence but fundamental transformation. When parameters shift from low (temperature 0.3, top-p 0.4) to high (0.8, 0.9), AI’s role metamorphoses from **pattern-enforcer** to **pattern-extender**, from **curator of corpus-typical option****s** to **generator of corpus-divergent provocations**.
In structured rooms, learners encountered AI as **meticulous editor**—catching deviations, offering polished alternatives, providing linguistic safety nets. The experience felt orderly and predictable: “It took our words and tried to put it in poem form.” In exploratory rooms, learners encountered **maginative interlocutor**** **suggesting unexpected techniques (‘Found poetry’) , posing philosophical questions (“Do you want the poem to condemn or understand?”), and venturing creative risks: “a very warm-hearted AI... like a very good friend, not just a machine.”

This difference operationalizes what traditional DDL could never achieve: **adaptive pattern engagement intensity****.** Johns’ (1991) DDL vision positioned learners as active “research workers” discovering patterns through corpus interrogation with uniform engagement intensity. AI enables **system-initiated engagement intensity calibration**—parameter settings influence whether learners encounter predominantly corpus-typical patterns or corpus-extending provocations. This represents a **DDL ****innovation**, not death, shifting from learner-initiated corpus searches to **selective uptake of system-initiated provocations** while preserving DDL’s core insight: **patterns discovered are better learned than rules transmitted****. **
Finding 2.1 revealed disturbing tension: **7****8****% rated Type B (Exemplar Giving) interactions as “most helpful,” yet Type B frequency negatively correlated with authorship perception** (*r* = -.58, *p* < .05). This paradox exposes contradictions in conceptualizing pedagogical support in creative domains.
Type B provides immediate assistance—presenting concrete options addressing linguistic gaps, reducing decision paralysis, enabling task completion. For L2 learners, this support feels genuinely helpful: “AI help me to generate few sentences let me choose.” Yet this same participant reported only 20% self-authorship: “I just need to choose use what sentence wrote by AI. I only own the meaning on this poem.” Type B positions learners as **selectors rather than creators**, shifting cognitive labor from generation to evaluation. Learners contribute **intent and judgment** but not **linguistic instantiation**—owning “meaning” but not “making meanings”
This contradicts DDL principles. Boulton (2012) emphasized DDL’s pedagogical power stems from “hands-on” engagement—learners actively interrogate corpora and internalize discoveries through sustained interaction. Type B **reverses this dynamic**: instead of learners constructing understanding from patterns, AI constructs options and learners choose. The “hands-on” engagement becomes “hands-off” selection, short-circuiting the developmental process building creative competence.
Our findings suggest **parameter configuration impacts this scaffolding-autonomy balance**. Structured parameters produce predominantly Type B interactions, maximizing accessibility but risking authorship alienation. Exploratory parameters shift toward Type C interactions preserving agency through **provocative suggestion rather than predetermined selection**—offering **possibilities to consider** rather than **options to choose**.
Finding 2.2 demonstrated the sole participant preferring Type C reported **80% self-authorship**—the highest despite extensive AI collaboration. Chat analysis revealed sustained conceptual dialogue rather than preset options: AI posed philosophical questions, suggested unexpected techniques, offered structural feedback while honoring creative vision. Critically, the participant **rejected, modified, and synthesized** suggestions selectively—exercising authorial control throughout.
The authorship rationale illuminates why this felt collaborative: “The general theme, the idea to use a turnstile as the central metaphor... these are all my ideas. AI helped me think about whether I want to write something that indicts or something that empathizes.” **Conceptual ownership remained with the learner** (theme, metaphor, stance), while AI provided **reflective provocation and craft guidance****.** The participant generated language; AI provoked thinking about that language.
Type C interactions enable mutuality: AI generates **unexpected possibilities** (pattern extension beyond corpus frequencies), and learners generate **selective uptake and linguistic instantiation**** **(transforming provocations into personal expression). Both exercise creativity complementarily rather than competitively.
Traditional DDL operates within **corpus-bounded possibility space**—discovering patterns that exist in data. Type C, enabled through exploratory parameters, **extends beyond corpus frequencies into generative possibility space****.** AI becomes capable of suggesting connections, techniques, and framings emerging through novel pattern recombination rather than corpus retrieval. This transforms AI from **pattern-revealer** to **pattern-extender**, preserving DDL’s constructivist foundation while expanding creative potential.

**4.2**** Answering Crosthwaite: Conditional Resolution**

Crosthwaite (2023) asked whether AI would “do the work for learners,” bypassing DDL’s inductive engagement. Our findings provide **conditional answer**: AI undermines or supports DDL principles **depending on ****how we educators configurate, prompt, and design pedagogical AI**.
**Under structured parameters**, AI functions as **DDL antithesis**—generating corpus-typical exemplars positioning learners as selectors rather than discoverers. Pattern exposure becomes passive reception; task completion occurs at authorship’s expense. This validates Crosthwaite’s concern.
**Under exploratory parameters**, AI functions as **DDL evolution**—generating corpus-extending provocations positioning learners as co-constructors. Pattern engagement becomes active synthesis; learners exercise selective uptake, critical judgment, and linguistic instantiation—capacities central to both DDL and creative development.
**The crucial recognition**: Parameter settings are not technical specifications but **pedagogical design variables** determining whether AI constrains or enables, scaffolds appropriately or over-determines outcomes. This insight transforms responsible AI integration from whether to use AI (presence is inevitable) to **how to configure A****I **serving learning goals.

**4.3**** Pedagogical Implications****:**** Parameter Literacy as Essential Competence**

Our findings establish **parameter literacy** as essential professional competence for educators integrating AI into L2 writing. This includes understanding how temperature and top-p shape AI behavior, exercising pedagogical judgment about when to use structured versus exploratory parameters, and identifying tools exposing parameters for educator control.
**Deign Recommendations**
Educational AI tools should:
**Make parameters**** suitable,**** visible****,**** and adjustable** with pedagogical guidance;
**Provide preset configurations** labeled by function (“Form Practice”, “Creative Exploration”);
**Display interaction analytics** showing Type A/B/C distributions for metacognitive reflection;
**Support parameter experimentation** allowing learners to compare configurations.
This transforms AI from passive response generator to **configurable pedagogical scaffold** whose affordances can be deliberately shaped.

**Curricular Sequencing**
Findings suggest **progressive parameter curriculum**: structured parameters (weeks 1-3) building foundations, moderate parameters (weeks 4-6) developing voice, exploratory parameters (weeks 7-9) enabling creative independence. This **systematic fading through parameter adjustment** operationalizes scaffolding principles without constant instructor monitoring.

**4.4 ****Limitations**

Findings represent **preliminary evidence with N=10** requiring full dataset validation (target N=20). The study examined **L2 poetry writing exclusively**—parameter effects might differ across academic writing, professional communication, or narrative fiction. Our 2×2 design compared **fixed parameter configurations** without examining progressive adjustment or participant-controlled parameters. We measured **immediate authorship perception** during 35-minute sessions—long-term developmental outcomes remain unknown. Future research should address these limitations through longitudinal studies, cross-task investigations, and comparisons with traditional instruction.

**5. Conclusion: The Hinge of DDL’s Future**

AI represents neither DDL’s death nor simple continuation, but a **pedagogical hinge where ****AI**** configuration ****and adaptation to educational environment influence**** which future unfolds**. With structured parameters, AI validates Crosthwaite’s concern—creating “helpful but alienating” experiences where task completion occurs at authorship’s expense. With exploratory parameters, AI enables DDL evolution—preserving creative agency while providing transformative support through corpus-extending provocations.
The Parameter→Interaction→Perception pathway establishes **parameter literacy as essential competence** for educators navigating AI integration. Temperature and top-p settings are not technical minutiae but pedagogical design variables determining learning outcomes. DDL’s future depends not on AI's capabilities but **our capacity to exercise pedagogical judgment over its configuration**.
The death Crosthwaite feared would come not from AI’s existence but from failing to understand and control how it shapes learning. The evolution we demonstrate becomes possible when educators recognize **parameters as pedagogical levers** and design accordingly. Our most consequential contribution: demonstrating **generative AI is not a pedagogical intervention but a configurable platform** whose affordances must be deliberately shaped through informed design.
Parameter configuration is **pedagogical decision-making**** and human-AI co-meaning making**** disguised as engineering specification**. Making it visible, adjustable, and pedagogically grounded transforms AI from potential threat into a powerful partner in DDL’s ongoing evolution. 

**References**
Bernardini, S. (2004). Corpora in the classroom: An overview and some reflections on future development. *In J. M. Sinclair (Ed.), How to use corpora in language teaching* (pp. 15-36). John Benjamins.

Bitchener, J., & Ferris, D. R. (2012). *Written corrective feedback in second language acquisition and writing*. Routledge.

Boden, M. A. (2004). *The creative mind: Myths and mechanisms*. Routledge.

Boulton, A. (2012). Data-driven learning: Taking the computer out of the equation. *Language Learning*, 62(2), 534572.

Chakrabarty, T., Padmakumar, V., & He, H. (2022). Help me write a poem: Instruction tuning as a vehicle for collaborative poetry writing. *arXiv Preprint arXiv:2210.13669*. https://doi.org/10.48550/arXiv.2210.13669

Coenen, A., Retelny, D., Wu, J., Michaux, J., Narayanan, A., Dang, H., Kua, T., Qian, H., Nham, K., Ma, F., & Agrawala, M. (2022). Wordcraft: Story writing with large language models. In *IUI 22: 27th International Conference on Intelligent User Interfaces Companion* (pp. 841843). Association for Computing Machinery. https://doi.org/10.1145/3490100.3516505

Crosthwaite, P., & Baisa, V. (2023). Generative AI and the end of corpus-assisted data-driven learning? Not so fast! *Applied Corpus Linguistics*, 3(3), 115.


Fithriani, R. (2021). Poetry writing in EFL classrooms: Learning from Indonesian students’ strategies. *KnE Social Sciences*.

Hanauer, D. I. (2010). *Poetry as research: Exploring second language poetry writing*. John Benjamins Publishing Company.

Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2019). The curious case of neural text degeneration. *arXiv Preprint arXiv:1904.09751*. https://doi.org/10.48550/arXiv.1904.09751

Hyland, K. (2007). Genre pedagogy: Language, literacy and L2 writing instruction. *Journal of Second Language Writing*, 16(3), 148164.

Jefferson, G. (2004). Glossary of transcript symbols with an introduction. In G. H. Lerner (Ed.), *Conversation analysis: Studies from the first generation* (pp. 1331). John Benjamins.

Johns, T. (1991). Should you be persuaded: Two examples of data-driven learning. *Classroom Concordancing Newsletter*, 4, 116.

Kerbs, M., McQueston, J., & Lawrance, L. (2024). Playing with words: Scaffolding writing through poetry. *Reading Teacher*, 78(1).

Li, L., Wei, Y., Xu, M., Xiao, M., He, X., Liu, W., & Liang, S. (2025). Exploring the impact of temperature on large language models: Hot or cold? *Procedia Computer Science*, 264, 242251. https://doi.org/10.1016/j.procs.2024.10.130

Li, M. (2025). Generative artificial intelligence in second language writing: A comprehensive review of current research. *Language Teaching*, 129. https://doi.org/10.1017/S0261444824000424

Lyster, R., & Ranta, L. (1997). Corrective feedback and learner uptake: Negotiation of form in communicative classrooms. *Studies in Second Language Acquisition*, 19(1), 3766. https://doi.org/10.1017/S0272263197001034

Peeperkorn, M., Bewersdorff, A., & Zhai, X. (2024). Is temperature the creativity parameter of large language models? *arXiv Preprint arXiv:2405.00492*. https://doi.org/10.48550/arXiv.2405.00492

Qian, W., Ma, J., Fox, R., Zhang, B., Liaw, R., Krishna, K., & Laban, P. (2023). “It felt like having a second mind”: Investigating human-AI co-creativity in prewriting with large language models. *arXiv Preprint arXiv:2307.10811*. https://doi.org/10.48550/arXiv.2307.10811

Shneiderman, B. (2007). Creativity support tools: Accelerating discovery and innovation. *Communications of the ACM*, 50(12), 2032.

Sun, Y. C., & Wang, L. Y. (2003). Concordancers in the EFL classroom: Cognitive approaches and collocation difficulty. *Computer Assisted Language Learning*, 16(1), 8394.

Van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacherstudent interaction: A decade of research. *Educational Psychology Review*, 22(3), 271296.


