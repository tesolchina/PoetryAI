## 2. Methodology

### 2.1 Platform Design and Parameter Configuration

We designed a specialized poetry writing platform (poetry.aitutor.ink) featuring a prompt-engineered chatbot that functions as collaborative guide rather than content generator. Unlike commercial AI tools that produce complete poems on demand, our chatbot—built using Claude Sonnet 4 via OpenRouter API—provides graduated scaffolding while preserving learner authorship through three distinct pedagogical roles: writing coach (questioning word choice and structural decisions), creative collaborator (proposing alternatives without imposing solutions), and language resource (illuminating English poetic possibilities for L2 writers navigating cross-linguistic creative challenges).

The platform architecture emphasizes observability and experimental control through four design features: (1) parameter manipulation controls allowing researchers to configure distinct scaffolding environments, (2) verification logging capturing exact parameter values and token-level model outputs, (3) identical prompt engineering across all experimental conditions to isolate parameter effects, and (4) comprehensive interaction capture including timestamps, message sequences, and behavioral metadata.

**Prompt Engineering for DDL-Compatible Scaffolding**

The chatbot's system prompt operationalizes DDL-scaffolding principles through explicit behavioral specifications. Rather than generating complete creative outputs, the chatbot must help learners discover expressive possibilities through strategic questioning ("What feeling do you want this image to convey?"), pattern exposure ("Consider how published poets use enjambment to create tension"), and reflective prompting ("Does this metaphor match your intended meaning?"). The prompt emphasizes cultural responsiveness to Hong Kong learners' experiences while maintaining a supportive rather than corrective stance. Response length constraints (40-80 words) prevent overwhelming learners while encouraging iterative dialogue.

A critical meta-instruction enables parameter-driven adaptivity: "Your response style naturally varies based on underlying model parameters: higher temperature/top-p lead to more creative, divergent suggestions; lower settings produce more structured, conventional guidance." This instruction ensures the chatbot's scaffolding style adapts to parameter configurations without explicitly revealing technical details to unaware participants.

**Parameter Configuration as Pedagogical Design Variable**

The platform's core innovation lies in treating temperature and top-p settings as manipulable pedagogical variables rather than hidden technical specifications. We configured two distinct scaffolding environments representing contrasting DDL philosophies:

**Structured Configuration** (Temperature 0.3, Top-p 0.4): This low-variability configuration constrains the AI to corpus-typical outputs, functioning as a "proactive concordancer" that delivers conventional English poetic patterns in contextually appropriate moments. From a technical perspective, these parameters restrict token sampling to high-probability options matching training data frequencies. From a DDL perspective, this mimics guided corpus consultation where learners encounter established linguistic patterns. From a scaffolding perspective, this provides heavy support reducing cognitive load during initial creative attempts. The learner experience emphasizes clarity and security—suggestions feel authoritative and grammatically reliable, though potentially constraining creative autonomy. This configuration predominantly generates Type A (constraint repair) and Type B (exemplar giving) interactions.

**Exploratory Configuration** (Temperature 0.8, Top-p 0.9): This high-variability configuration enables corpus-divergent outputs, extending beyond training data frequencies into generative possibility space. Technically, these parameters broaden token sampling to include lower-probability creative combinations. From a DDL perspective, this resembles open corpus exploration where learners encounter unexpected patterns sparking discovery. From a scaffolding perspective, this provides light support that stimulates creative expansion while demanding critical evaluation. The learner experience emphasizes surprise and partnership—suggestions feel collaborative and inspiring, though requiring judgment about appropriateness. This configuration elevates Type C (surprise harvest) interactions where AI outputs become creative catalysts rather than authoritative models.

### 2.2 Experimental Design and Procedures

**2×2 Factorial Configuration**

Twenty L2 English learners (CEFR B1-B2, ages 18-23, predominantly Cantonese L1) from Hong Kong Baptist University participated in a 2×2 factorial design manipulating two independent variables:

(1) **Parameter Configuration** (Between-subjects): Structured rooms (A/B) received low-variability settings (temperature 0.3, top-p 0.4) promoting corpus-typical patterns, while Exploratory rooms (C/D) received high-variability settings (temperature 0.8, top-p 0.9) enabling corpus-divergent creativity.

(2) **Awareness Condition** (Between-subjects): Aware rooms (A/C) received explicit information about parameter settings including interface displays showing current values with explanatory tooltips ("Temperature controls AI creativity: lower values produce conventional suggestions, higher values generate surprising alternatives"). Unaware rooms (B/D) received no parameter information—interfaces displayed only the chat interface without technical details, with post-session debriefing ensuring ethical transparency.

This design isolates parameter effects (comparing structured vs. exploratory while collapsing across awareness) and tests whether metacognitive knowledge moderates parameter-driven scaffolding (testing Parameter × Awareness interaction). Each room contained 5 participants working individually, allowing within-condition pattern observation while maintaining between-subjects statistical independence.

**Participants and Recruitment**

Participants were recruited from undergraduate poetry writing courses at Hong Kong Baptist University through purposive sampling targeting intermediate English proficiency (CEFR B1-B2). This proficiency range ensures sufficient linguistic competence to engage creatively while representing the population most likely to benefit from AI-assisted poetry writing—advanced enough to evaluate AI suggestions critically, yet developing enough to value scaffolding support. All participants had prior experience writing Chinese poetry but limited exposure to English poetic forms, making the cross-linguistic creative challenge authentic and meaningful.

**Study Phases**

**Phase 1: Main Study Sessions (November 2024 - January 2026)**

The primary study comprised two distinct data collection phases:

**Session 1 (November 24, 2025):** Following the 2×2 factorial design described above, 10 participants engaged in the experimental protocol with parameter-controlled scaffolding environments. This session focused on isolating parameter effects in controlled conditions, generating chat transcripts, interaction coding, artifact analysis, and immediate reflection data.

**Session 2 - CCL Seminar (January 2026):** As a naturalistic follow-up validation study, 9 participants from the Centre for Applied English Studies (CCL) seminar series engaged with the PoetryAI platform in a workshop format (7 participants completed feedback forms). Unlike Session 1's controlled 2×2 factorial design, Session 2 allowed open exploration of both Exploratory Atelier (high-variability parameters) and Structured Studio (low-variability parameters) without experimental manipulation. This naturalistic design enabled validation of parameter effects in real-world educational settings while capturing authentic user preferences and long-term applicability perceptions. Comprehensive post-session feedback forms captured satisfaction metrics, authorship perceptions, interaction type preferences, and future use intentions.

**Session Protocol (75 minutes for Session 1; Workshop Format for Session 2)**

**Session 1 Protocol (75 minutes)**

Each experimental session in Session 1 followed a standardized four-phase protocol balancing ecological validity with experimental control:

**Phase 1: Platform Orientation (10 minutes)** — Facilitators demonstrated the chat interface, explained the chatbot's supportive (non-generative) role, and guided participants through poetry form selection. Participants chose from four options: haiku (5-7-5 syllable structure), free verse (no formal constraints), limerick (AABBA rhyme scheme), or open form (participant-defined structure). This choice preserved creative agency while providing optional structural scaffolding for those desiring it.

**Phase 2: AI-Assisted Writing (35 minutes)** — Participants composed poetry through iterative dialogue with the chatbot. No prescriptive interaction patterns were imposed—learners initiated conversations organically, asking questions, requesting feedback, or seeking suggestions as needs arose. This naturalistic approach captures authentic scaffolding dynamics rather than researcher-imposed interaction sequences. Platform analytics recorded all messages, timestamps, and behavioral traces.

**Phase 3: Individual Reflection (15 minutes)** — Immediately following composition, participants completed structured reflection templates capturing: (a) perceived authorship (5-point scale: 1 = "entirely AI's poem" to 5 = "entirely my poem"), (b) creative satisfaction (5-point scale: 1 = "much worse than without AI" to 5 = "much better with AI"), (c) most helpful interaction type (selecting example exchanges), and (d) open-ended descriptions of the AI's role. These immediate reflections capture authentic perceptions before panel discussions introduce social influence.

**Phase 4: Panel Discussion (15 minutes)** — Participants gathered in room-based groups (5 per panel, 4 panels total) for facilitated discussions exploring their creative experiences. Facilitators used open-ended prompts ("How did the AI influence your creative process?" "Did you feel like a creator or a selector?") without mentioning parameters or experimental conditions. Audio-recorded discussions generated rich qualitative data revealing shared cultural understandings and condition-specific themes.

**Session 2 Protocol (Workshop Format)**

Session 2 (CCL Seminar) employed a simplified, non-experimental protocol focused on user experience and real-world applicability:

**Phase 1: Platform Orientation & Open Exploration (45-50 minutes)** — Participants received brief platform orientation explaining the supportive chatbot role and interface navigation. Unlike Session 1's constrained room assignments, participants freely chose which room to enter (Exploratory Atelier with high-variability parameters or Structured Studio with low-variability parameters), enabling naturalistic parameter preference observation. Participants composed poetry organically without experimental constraints, with all interactions automatically logged.

**Phase 2: Post-Session Feedback Collection (15-20 minutes)** — Participants completed comprehensive feedback forms (66 questions across multiple dimensions) capturing: overall satisfaction with seminar and platform, comfort using the platform, intention for future use, creative ownership percentages, disagreements with AI suggestions, interaction type preferences and helpfulness ratings, emotional safety perceptions, confidence gains, and detailed scenarios for future AI tool use. This expanded feedback instrument provided granular data on user perceptions, satisfaction drivers, and design appreciation.

**Ethical Safeguards**

All participants provided informed consent following HKBU IRB protocols. Unaware participants underwent two-stage consent: initial consent for "studying AI-assisted creative writing" without revealing parameter manipulation, then post-debriefing consent after full experimental disclosure with withdrawal option (none exercised). This approach balances methodological validity (preventing demand characteristics) with ethical transparency (ensuring genuine informed consent). All data stored on encrypted servers with participant anonymization.

### 2.3 Data Collection and Analysis

**Multi-Modal Data Sources**

Six complementary data sources captured the multi-dimensional impact of parameter-driven scaffolding in Session 1, with expanded feedback collection in Session 2:

**Session 1 Data Sources (Experimental Design):**

**1. Complete Chat Logs** — All human-AI dialogues were automatically captured with comprehensive metadata including timestamps, parameter settings, token counts, and message sequences. These logs document the moment-by-moment unfolding of scaffolded creative processes, preserving both explicit conversational content and implicit interaction patterns.

**2. Interaction Type Coding** — Each AI response was independently classified by two trained coders following an operational coding scheme distinguishing three interaction types: Type A (constraint repair: AI corrects errors or suggests grammatical improvements), Type B (exemplar giving: AI provides model phrases or conventional patterns), and Type C (surprise harvest: AI generates unexpected creative possibilities requiring learner evaluation). Inter-rater reliability reached substantial agreement (Cohen's κ = 0.84), with discrepancies resolved through discussion. This systematic coding transforms qualitative chat data into quantifiable scaffolding profiles.

**3. Poem Artifacts** — Final creative products were collected as tangible outcomes of scaffolded writing processes. Poems were analyzed for linguistic sophistication (lexical diversity, syntactic complexity, figurative language density) and blindly evaluated by three experienced poetry educators rating originality, coherence, and emotional impact on 5-point scales. Artifact analysis connects process data (interactions) with product quality (poems).

**4. Reflection Templates** — Immediately following composition, participants completed structured reflection templates capturing five dimensions: (a) perceived authorship ("How much of this poem feels like yours vs. the AI's?" on 1-5 scale anchored at "entirely AI's" and "entirely mine"), (b) creative satisfaction ("How does writing with AI compare to writing alone?" on 1-5 scale from "much worse" to "much better"), (c) most helpful interaction (selecting specific chat exchanges), (d) open-ended AI role descriptions ("In your own words, what role did the AI play?"), and (e) preferences for future use. These immediate reflections capture authentic perceptions before panel discussions introduce social influence.

**5. Panel Discussion Transcripts** — Four room-based group discussions (5 participants each, 15 minutes, audio-recorded and transcribed) generated rich qualitative data through collaborative sense-making. Facilitators used open-ended prompts ("How did the AI influence your creative decisions?" "Did you feel like a creator or a selector?") without revealing experimental manipulations. Discussions revealed shared cultural understandings, condition-specific themes, and spontaneous metacognitive reflections absent from individual templates.

**6. Platform Analytics** — Behavioral traces automatically logged by the system quantified engagement patterns: session duration, total messages exchanged, message initiation patterns (human-initiated vs. AI-initiated sequences), response latency (time between receiving AI response and sending next message), revision behaviors (editing previous inputs), and form selection distributions. Analytics provide objective behavioral complements to self-reported perceptions.

**Session 2 Data Sources (Naturalistic Validation):**

**7. Comprehensive Feedback Forms** — All participants completing Session 2 (7 of 9 participants) submitted detailed feedback forms capturing 66 questions across multiple dimensions: (a) overall satisfaction metrics (enjoyment, comfort, future use intention on 5-point scales), (b) creative process approach (learner-guided vs. AI-guided decision-making), (c) creative ownership percentages ("What percentage of your poem is yours vs. the AI's?"), (d) AI disagreement areas (word choices, structure, emotion, creativity level with multi-select options), (e) interaction type distribution and preferences (Type A, B, C frequency and helpfulness ratings), (f) confidence gains from AI engagement (5-point scale), (g) perceived AI partnership (whether AI felt like creative partner vs. instructor), (h) emotional safety with AI (5-point scale), (i) pre-existing poetry ideas (whether participants arrived with initial concepts), (j) future use scenarios (multiple-select options: brainstorming, technique learning, feedback, exploration, writing practice, personal expression, homework, etc.), (k) interface preferences (Exploratory Atelier vs. Structured Studio for personal vs. academic contexts), and (l) open-ended comments on platform design and experience quality.

**8. Session 2 Chat Logs & Interaction Coding** — Like Session 1, all Session 2 conversations were logged and coded for interaction types, enabling comparison of parameter effects across experimental (Session 1) and naturalistic (Session 2) conditions.

**9. Poem Artifacts** — Session 2 participants' final poems were collected and analyzed using identical quality evaluation procedures as Session 1, enabling cross-session product comparison.

This expanded Session 2 data collection enabled validation of Session 1 parameter effects in realistic educational settings while providing rich user preference data informing practical implementation guidance.

**Analytical Approaches**

This study employed convergent parallel mixed-methods design (Creswell & Plano Clark, 2017) where quantitative and qualitative analyses proceeded independently before integration at interpretation stage.

**Quantitative Analysis**

Three research questions guided statistical analyses:

**RQ1: Do parameter configurations generate distinct interaction type profiles?** — Chi-square tests compared Type A, B, and C distributions across structured vs. exploratory conditions, with Cramér's V measuring effect sizes. Follow-up tests examined pairwise differences (e.g., Type C in exploratory vs. structured) to identify which interaction types drive overall distributional differences.

**RQ2: How do interaction type profiles relate to authorship perception and creative satisfaction?** — Pearson correlations examined relationships between each interaction type's frequency (percentage of total AI responses) and outcome measures. Multiple regression predicted authorship scores from Type A, B, and C percentages simultaneously, revealing unique contributions of each scaffolding approach. Independent samples t-tests compared authorship and satisfaction between Type B-dominant (>50% Type B) and Type C-dominant profiles to examine the "helpful but alienating" paradox.

**RQ3: Does awareness of parameter settings moderate parameter-driven effects?** — Two-way ANOVA with parameter configuration (structured/exploratory) and awareness (aware/unaware) as independent variables tested main effects and interactions on authorship and satisfaction. Non-significant awareness main effects or interactions would suggest parameter manipulation operates independently of metacognitive knowledge.

All statistical analyses used α = .05 significance threshold with effect sizes (Cohen's d, Cramér's V, η²) reported following APA standards. Statistical assumptions (normality, homogeneity of variance) were verified before parametric testing.

**Qualitative Analysis**

Three complementary analytical traditions examined different facets of scaffolded creative processes:

**Conversation Analysis** (Jefferson, 2004) — Turn-by-turn examination of chat transcripts identified repair sequences (how learners responded to AI suggestions), uptake patterns (active transformation vs. passive acceptance), and scaffolding trajectories (whether support increased, decreased, or remained stable across sessions). This micro-level analysis revealed the procedural mechanisms through which parameters shape interaction dynamics.

**Thematic Analysis** (Braun & Clarke, 2006) — Recursive inductive coding of reflection templates and discussion transcripts identified condition-specific themes. Initial open coding generated descriptive labels; focused coding grouped related codes into coherent themes; theoretical coding connected themes to DDL-scaffolding concepts. Structured rooms generated themes like "over-scaffolding concerns" and "clarity and confidence," while exploratory rooms generated "inspiring surprises" and "creative partnership." This pattern-level analysis revealed shared cultural meanings within experimental conditions.

**Discourse Analysis** — Examination of spontaneous participant characterizations during panel discussions revealed identity positioning (selector vs. co-creator) aligned with parameter conditions. Analysis attended to metaphors ("the AI was like a co-author" vs. "the AI was like a dictionary"), agency attributions ("the AI helped me discover" vs. "the AI gave me phrases"), and evaluative stance. This meaning-level analysis illuminated how scaffolding environments shape creative self-concepts.

**Data Integration and Triangulation**

Integration occurred through three critical convergence points where quantitative evidence and qualitative insights addressed the same phenomena from different angles:

**Convergence Point 1: Parameter→Interaction Mechanism** — Quantitative evidence showed structured parameters generated 14% Type C responses while exploratory parameters generated 35% (χ²=24.3, p<.001, Cramér's V=.48). Qualitative analysis validated this distinction: structured room participants described AI responses as "clear examples" and "correct patterns" matching Type A/B definitions, while exploratory room participants described "surprising metaphors" and "unexpected connections" matching Type C definitions. This convergence confirms interaction type coding captured meaningful functional distinctions.

**Convergence Point 2: Authorship-Autonomy Paradox** — Quantitative evidence revealed negative correlation (r=-.58, p=.005) between Type B frequency and authorship perception. Qualitative narratives illuminated this paradox: Type B-dominant participants appreciated helpfulness ("The AI gave me beautiful phrases I couldn't think of") while lamenting diminished ownership ("But they felt more like the AI's words than mine"). This convergence explains the statistical pattern through participant sense-making.

**Convergence Point 3: Dynamic DDL Mechanism** — Quantitative evidence demonstrated parameter configuration exerted large effects (η²=.58) while awareness showed negligible effects (η²=.07). Qualitative analysis revealed even aware participants couldn't strategically override parameter-driven scaffolding—their awareness enabled metacognitive reflection ("I know the AI is set to be creative, so I'm more critical of its suggestions") but didn't fundamentally alter interaction distributions. This convergence establishes that parameter manipulation operates as infrastructural DDL scaffolding rather than explicit metacognitive tool.

This triangulated approach provides multi-dimensional evidence that parameter configurations enable dynamic DDL scaffolding. Neither quantitative frequencies nor qualitative narratives alone could establish this claim—quantitative data demonstrate systematic patterns but not underlying meanings; qualitative data reveal meanings but not generalizable distributions. Convergence across evidence types validates the theoretical contribution that generative AI can extend DDL principles through parameter-based adaptivity.
