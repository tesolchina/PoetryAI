# Methodology

## 3.1 Platform Building and Chatbot Design: Operationalizing DDL-Scaffolding Theory

To investigate ***how* parameter configuration enables *dynamic* DDL scaffolding**, we designed and deployed a purpose-built poetry writing platform (poetry.aitutor.ink) that transforms the theoretical framework established in our introduction into a living experimental environment. Where commercial AI tools like ChatGPT and Claude operate as black boxes—concealing their parameter settings and offering uniform, one-size-fits-all interactions—our platform functions as a transparent research laboratory. Every parameter adjustment, every AI response, every learner keystroke becomes visible data, enabling us to trace the intricate pathways through which technical configurations shape pedagogical experiences.

### 3.1.1 Platform Architecture

The web-based platform features a **prompt-designed chatbot system** accessible through four distinct virtual rooms, each configured with specific parameter settings. Two critical design principles distinguish our platform from commercial AI tools:

**1. Instructional vs. Generative Function: Preserving Learner Authorship**  
Commercial AI tools typically position themselves as content generators—producing complete poems with a single prompt, effectively displacing the writer from the creative process. Our chatbot deliberately rejects this model. Through careful prompt engineering, we constrained the AI to function as a **guide rather than ghostwriter**, embodying three complementary pedagogical roles:

- A **writing coach** who reads drafts attentively and poses thoughtful questions about word choice, imagery, and structure
- A **creative collaborator** who brainstorms alongside learners, proposing alternatives without imposing solutions
- A **language resource** who illuminates possibilities within the English lexicon, helping L2 writers navigate unfamiliar poetic terrain

This instructional architecture ensures that learners retain authorship of their creative work—they select words, shape lines, make aesthetic judgments—while receiving graduated support that responds to their evolving needs. The AI never writes *for* learners; it writes *with* them, preserving the DDL principle of active pattern engagement over passive consumption.

**2. Parameter-Adjustable Experimental Infrastructure: Making the Invisible Visible**  
Where commercial AI tools treat parameters as proprietary trade secrets, our platform exposes them as manipulable pedagogical variables. We engineered the system to function as both learning environment *and* research instrument, embedding multiple layers of observability:

- **Systematic parameter manipulation**: Each virtual room operates as a controlled microclimate—temperature and top-p values locked at predetermined levels, creating stable conditions for observing how learners navigate different scaffolding intensities
- **Parameter verification logging**: Every AI response carries a digital fingerprint recording its generative conditions, enabling us to verify that exploratory rooms truly generated more variable outputs, that structured rooms maintained consistency
- **Identical baseline prompt**: Like scientists controlling for confounding variables, we ensured all four rooms received the same instructional DNA—only parameters varied, isolating their effects from prompt engineering differences
- **Complete interaction capture**: The platform archives the full conversational ecology—not just final poems, but the hesitations, revisions, and collaborative negotiations through which they emerged

This dual specialization—instructional prompt design married to parameter observability—creates a methodological breakthrough: we can finally trace the causal pathways through which technical configurations translate into learner experiences, answering the "how" question that previous research left unresolved.

**Technical Implementation**  
The platform architecture includes:

1. **Systematic parameter control**: Precise temperature and top-p manipulation across experimental conditions
2. **Complete interaction logging**: Turn-by-turn conversation capture with timestamps, parameter settings, and AI response generation metadata
3. **Session management**: Timed writing sessions (45 minutes) with automatic progress tracking
4. **Multi-modal data collection**: Integrated chat logs, poem artifacts, real-time behavioral analytics, and post-session reflection prompts

The platform was built using Python (Flask framework) with OpenRouter API integration, enabling access to GPT-4 as the underlying language model while maintaining full control over generation parameters.

### 3.1.2 Unified Prompt Engineering Design: Isolating Parameter Effects

A pivotal methodological choice shaped the platform's experimental validity: we crafted a **single, universal system prompt** that would govern AI behavior across all four rooms. This decision addressed a persistent weakness in human-AI creativity research—the tendency to confound parameter effects with prompt engineering differences, making it impossible to discern whether observed variations stem from *how* the AI is configured (parameters) or *what* it is instructed to do (prompts). By holding the prompt constant while manipulating only parameters, we created a clean experimental contrast where differences in interaction patterns could be confidently attributed to parameter settings rather than instructional ambiguities.

**The Universal System Prompt** defines the chatbot's role as a poetry writing assistant for L2 learners (CEFR B1-B2 proficiency) and establishes response frameworks supporting all three interaction types:

- **Type A (Constraint Repair)**: Diagnostic feedback on structural, linguistic, or poetic elements requiring attention
- **Type B (Exemplar Giving)**: Model texts, phrase alternatives, and curated options for learner selection and adaptation  
- **Type C (Surprise Harvest)**: Creative suggestions, unexpected metaphors, and generative possibilities extending beyond learner's initial ideas

The prompt establishes clear conversational boundaries—responses constrained to 40-80 words to prevent overwhelming learners—while cultivating an encouraging, culturally responsive voice that honors diverse creative perspectives. Rather than positioning the AI as an error-hunting corrector, the prompt frames it as a collaborative partner invested in the learner's creative vision.

Most crucially, the prompt includes a sophisticated **meta-instruction** that enables parameter-driven adaptivity:

> "Your response style naturally varies based on the underlying model parameters: higher temperature/top-p settings lead to more creative, experimental suggestions; lower settings produce more focused, structured guidance. These variations occur organically without explicit parameter awareness."

This carefully worded directive achieves an elegant solution to a technical challenge: it instructs the LLM to modulate its behavior according to parameter settings *without* revealing those settings to learners in unaware conditions. The AI adapts its scaffolding intensity—shifting between normative correction and exploratory divergence—while learners experience this as natural conversational flow rather than algorithmic adjustment.

### 3.1.3 Parameter Configuration as Pedagogical Design Variable: From Technical Knobs to Teaching Tools

The conceptual breakthrough enabling our investigation lies in reconceptualizing **temperature and top-p not as obscure technical settings but as pedagogical design instruments**—adjustable dials that educators can turn to calibrate scaffolding intensity. Where software engineers view these parameters as controls for output randomness, we theorize them as mechanisms for shaping the *pedagogical character* of AI interaction:

**Structured Configuration: The Steady Guide (Low Parameters)**
- Temperature: 0.3 | Top-p: 0.4
- **Technical function**: Tightens the AI's decision-making scope, constraining token selection to high-probability choices that mirror training data frequencies—producing predictable, corpus-typical outputs
- **DDL function**: Transforms the AI into a proactive concordancer, surfacing linguistic patterns that learners would encounter through traditional corpus searches, but delivering them contextually and conversationally
- **Scaffolding function**: Generates a teaching style dominated by Type A normative corrections ("This line needs a stronger verb") and Type B conventional exemplars ("You could try 'whispers' instead of 'says'"), creating **heavy scaffolding** that reduces cognitive load but risks constraining creative autonomy
- **Learner experience**: Encounters an AI that behaves like a patient tutor—systematic, educational, reliably helpful, but potentially over-directive

**Exploratory Configuration: The Creative Catalyst (High Parameters)**  
- Temperature: 0.8 | Top-p: 0.9
- **Technical function**: Loosens the AI's generative constraints, sampling from broader, more diverse token distributions, enabling outputs that deviate creatively from corpus norms
- **DDL function**: Elevates the AI beyond pattern retrieval into pattern *extension*—generating linguistic possibilities that transcend training data frequencies, a generative capability impossible in static corpus DDL
- **Scaffolding function**: Shifts the interaction ecology toward Type C exploratory divergence ("What if rain becomes *hunger* in your metaphor?"), providing **light scaffolding** that sparks creative expansion while demanding learners critically evaluate and selectively integrate surprising suggestions
- **Learner experience**: Encounters an AI that behaves like an experimental collaborator—imaginative, sometimes unexpected, occasionally confusing, but potentially inspiring

This parameter-interaction choreography reveals the mechanism through which AI can *dynamically* modulate its pedagogical presence—transitioning from structured tutor to exploratory partner simply by adjusting two numerical values. The "how" of dynamic DDL scaffolding, long theorized but never empirically demonstrated, becomes operationally tractable.

---

## 3.2 Experimental Design: 2×2 Factorial Configuration

### 3.2.1 Independent Variables

The study employed a 2×2 factorial design manipulating two independent variables:

**1. Parameter Configuration** (Between-subjects)
- **Structured**: Temperature 0.3, Top-p 0.4 (Rooms 1 & 2)
- **Exploratory**: Temperature 0.8, Top-p 0.9 (Rooms 3 & 4)

**2. Awareness Condition** (Between-subjects)
- **Aware**: Participants informed about parameter manipulation and its potential effects (Rooms 1 & 3)
- **Unaware**: No information provided about technical parameters (Rooms 2 & 4)

This design enables examination of **direct parameter effects** (structured vs. exploratory) and **metacognitive influences** of parameter literacy (aware vs. unaware), addressing research questions about both technical mechanisms and learner perceptions.

### 3.2.2 Four-Room Configuration Matrix

| Room | Parameter Setting | Awareness | n | Primary Analysis Focus |
|------|------------------|-----------|---|------------------------|
| **Room 1** | Structured (0.3/0.4) | Aware | 5 | Parameter awareness effects |
| **Room 2** | Structured (0.3/0.4) | Unaware | 5 | **Pure parameter effects** |
| **Room 3** | Exploratory (0.8/0.9) | Aware | 5 | Parameter awareness effects |
| **Room 4** | Exploratory (0.8/0.9) | Unaware | 5 | **Pure parameter effects** |

**Rationale for Awareness Manipulation**: Rooms 2 and 4 (unaware conditions) serve as primary controls for isolating genuine parameter effects uncontaminated by expectancy or demand characteristics. Rooms 1 and 3 (aware conditions) investigate whether **parameter literacy**—explicit knowledge about how AI configuration shapes interaction patterns—enables learners to develop metacognitive strategies for adaptive tool use.

### 3.2.3 Interface Differentiation

**Aware Interface** (Rooms 1 & 3):
- Welcome message explains temperature and top-p concepts using accessible language
- Parameter display panel shows current settings (e.g., "Temperature: 0.8 | Top-p: 0.9")
- Educational tooltips explain: "Higher values = more creative, surprising suggestions"
- All standard chatbot functionality remains identical to unaware interface

**Unaware Interface** (Rooms 2 & 4):
- Standard creative writing partner introduction with no parameter mentions
- Clean interface focused on poetry writing task and AI assistance
- Identical chatbot functionality and system prompt
- Post-session debriefing explains parameter manipulation (ethical disclosure)

This interface design ensures experimental validity: Any behavioral or perceptual differences between aware and unaware conditions reflect parameter literacy effects rather than functional differences in AI capabilities.

### 3.2.4 Participants and Procedures: Orchestrating the Poetry Writing Experience

**Participant Recruitment and Profile**  
Twenty L2 English learners volunteered for this study, recruited from Hong Kong Baptist University's undergraduate population through course announcements and digital posters. All participants met CEFR B1-B2 proficiency criteria—intermediate English users capable of expressing themselves creatively while still grappling with linguistic constraints that make scaffolding valuable. Their ages ranged from 18 to 23, with predominantly Cantonese L1 backgrounds reflecting Hong Kong's linguistic landscape. Random assignment distributed five participants to each experimental room, ensuring balanced representation across parameter conditions.

**Session Choreography: A 75-Minute Creative Journey**  

The research session unfolded as a carefully sequenced 75-minute experience designed to immerse participants in collaborative poetry writing while capturing multiple layers of data:

**Phase 1: Platform Orientation (5 minutes)** – *Setting the Stage*  
Participants logged into their assigned rooms, familiarized themselves with the chatbot interface, and selected a poetry form to guide their work—haiku's disciplined syllable structure, free verse's open possibilities, limerick's playful rhythm, or an open exploration unconstrained by form. This brief orientation established technical comfort before creative work began.

**Phase 2: AI-Assisted Poetry Writing (45 minutes)** – *The Creative Crucible*  
Participants entered a focused creative space where they drafted, revised, and refined poems in conversation with their AI partner. They worked independently but simultaneously—five writers in each room, each engaged in their own poetic dialogue—generating a rich corpus of human-AI interaction. The platform imposed no restrictions on AI consultation frequency; some learners engaged in intensive back-and-forth exchanges, while others drafted independently before seeking AI feedback. This unstructured interaction time revealed organic collaboration patterns rather than researcher-imposed behaviors.

**Phase 3: Reflection Journal (8 minutes)** – *Capturing Immediate Impressions*  
While creative experiences remained vivid, participants responded to structured reflection prompts probing authorship perception ("To what extent does this poem reflect YOUR ideas vs. the AI's ideas?"), creative satisfaction, and scaffolding experiences. These immediate post-session reflections captured perceptions before group discussion could influence individual perspectives.

**Phase 4: Group Panel Discussion (22 minutes)** – *Collaborative Meaning-Making*  
Participants reconvened in room-specific groups, sharing poems aloud and narrating their creative journeys. These discussions—audio recorded and later transcribed—generated rich qualitative data as learners compared experiences, debated AI's role, and articulated insights about authorship and collaboration. The social dimension of this phase revealed shared patterns within parameter conditions while honoring individual creative variations.

**Ethical Safeguards and Transparency**  
All participants provided informed consent before engaging with the platform. For those in unaware conditions (Rooms 2 and 4), we implemented a two-stage consent process: initial consent for "AI-assisted poetry writing research" followed by post-session debriefing that revealed the parameter manipulation and provided opportunities to withdraw data. Notably, no participants chose withdrawal—many expressed fascination upon learning about the technical mechanisms underlying their experiences. Chat logs and personal identifiers were stored in separate encrypted databases following HKBU IRB protocols, with data retention and destruction procedures clearly communicated.

---

## 3.3 Data Collection and Analysis Scheme: Weaving a Rich Evidentiary Tapestry

This study orchestrates a convergent parallel mixed-methods design (Creswell & Plano Clark, 2017) in which quantitative measurements and qualitative insights emerge simultaneously, then converge during interpretation to reveal patterns invisible to either tradition alone. The research design creates *multiple windows* onto the same phenomenon—parameter-driven scaffolding adaptation—allowing us to triangulate across numerical patterns, linguistic artifacts, learner narratives, and social meaning-making. What emerges is not mere data aggregation but rather a *systematic excavation* of how AI parameters reshape the texture of creative collaboration.

### 3.3.1 Multi-Modal Data Sources: Capturing the Complete Experience

Six complementary data sources together form a comprehensive portrait of the AI-assisted poetry writing experience, each illuminating dimensions invisible to the others:

**1. Complete Chat Logs: The Digital Transcript of Collaboration**  
Every keystroke, every AI response, every moment of the 45-minute poetry writing sessions lives in the platform's comprehensive chat logs. These turn-by-turn conversation records capture the raw material of human-AI creative dialogue—timestamps marking interaction rhythm, user messages revealing intent and uncertainty, AI responses demonstrating scaffolding moves. Rich metadata accompanies each exchange: parameter settings confirming experimental conditions, response generation times hinting at computational complexity, token counts measuring linguistic elaboration. The corpus spans 20 participants across 75-minute sessions, yielding approximately 900 minutes of logged interaction—a dense record of *thinking aloud together* between humans and machines.

**2. Interaction Type Coding: Making Patterns Visible**  
Raw chat logs transform into analytical gold through systematic coding aligned with the DDL-scaffolding framework. Each AI response receives classification along three interaction types that capture distinct pedagogical functions:
  * **Type A (Constraint Repair)**: The AI spots linguistic missteps or structural deviations—a violated syllable pattern in haiku, awkward phrasing, inconsistent metaphors—and offers corrective guidance that brings learners back to conventional norms
  * **Type B (Exemplar Giving)**: The AI curates linguistic options, presenting model phrases, alternative word choices, or exemplar lines that learners can select from or adapt—a moderately directive scaffolding move
  * **Type C (Surprise Harvest)**: The AI generates unexpected creative directions that leap beyond the learner's initial ideas, introducing novel themes, surprising imagery, or conceptual extensions that *expand* rather than merely *correct* the learner's creative vision

Coding treats each AI response turn as the unit of analysis, assigning the dominant interaction type exhibited. Two trained coders independently classified 30% of responses, achieving strong inter-rater reliability (Cohen's κ = 0.84), confirming that these interaction types represent replicable, observable phenomena rather than subjective interpretations.

**3. Poem Artifacts: Tangible Creative Outcomes**  
All drafts and final poems—the concrete products of AI-assisted creativity—were collected and preserved. These texts became subjects of systematic linguistic analysis examining vocabulary sophistication (lexical diversity, academic word use), syntactic complexity (clause structures, sentence length variation), and figurative language deployment (metaphor density, imagery richness). Additionally, two experienced poetry educators conducted blind evaluations, rating poems on creative quality dimensions including originality, emotional resonance, and technical craft—providing external validation beyond self-reported satisfaction.

**4. Reflection Journals: Capturing Immediate Perceptions**  
Immediately post-session, while creative experiences remained vivid, participants responded to structured reflection prompts probing multiple dimensions:
- **Authorship perception**: "To what extent does this poem reflect YOUR ideas vs. the AI's ideas?" (1-7 scale)—the central perceptual variable
- **Creative satisfaction**: "How satisfied are you with the final creative product?" (1-7 scale)—measuring affective response
- **AI role descriptions**: Open-ended prompt "Describe the AI's role in your creative process"—inviting metaphorical characterizations
- **Scaffolding perceptions**: "Was the AI's support helpful? Too much? Too little?"—assessing scaffolding calibration

These individual reflections, written before group discussion, captured *uncontaminated* first impressions before social interaction could shape perspectives.

**5. Panel Discussion Transcripts: Collaborative Sense-Making**  
The 22-minute room-specific panel discussions—four groups corresponding to the four experimental rooms—generated rich qualitative data as participants moved from private reflection to social meaning-making. Audio recordings captured lively exchanges as learners read poems aloud, narrated creative journeys, debated AI authorship boundaries, and articulated emergent insights about collaboration. Verbatim transcripts preserve moments of realization ("Oh! *That's* why the AI kept suggesting..."), collective pattern recognition (participants comparing Type C surprise discoveries), and contested interpretations (debates about whether curated options feel "helpful but alienating"). These discussions reveal not only individual experiences but also *shared cultural understandings* emerging within parameter conditions.

**6. Platform Analytics: The Behavioral Footprint**  
Behind the scenes, the platform logged behavioral traces that quantify engagement patterns invisible in qualitative accounts: session duration revealing stamina and immersion, message frequency indicating interaction intensity, response latency hinting at cognitive processing time. Poem revision patterns—how many times learners returned to earlier drafts—illuminate iterative refinement processes. Form selection choices (haiku's constraints vs. free verse's openness) correlate with scaffolding preferences. Interaction intensity metrics (messages per minute) distinguish intensive collaborative bursts from contemplative independent drafting phases. Together, these analytics provide the *behavioral texture* complementing linguistic and perceptual data.

### 3.3.2 Quantitative Analysis Procedures

**Primary Hypothesis Testing:**

**RQ1: Do Parameter Configurations Shape Interaction Type Distributions?**

Our first hypothesis—that parameter manipulation drives systematic differences in DDL scaffolding patterns—demands categorical analysis comparing interaction type frequencies across experimental conditions:

- **Chi-square tests** assess whether Type A, B, and C distributions differ significantly between structured (temp=0.3, top-p=0.4) and exploratory (temp=0.8, top-p=0.9) conditions. These tests ask: Is the observed Type C frequency difference statistically reliable or merely sampling noise?
- **Effect size measurement** via Cramér's V quantifies association strength beyond statistical significance, distinguishing trivial differences from pedagogically meaningful patterns
- **Expected pattern**: Structured parameters should elevate Type A (constraint repair) and Type B (exemplar giving) frequencies, while exploratory parameters should dramatically increase Type C (surprise harvest) occurrences—revealing how temperature and top-p settings *tune* scaffolding directiveness

**RQ2: How Do Interaction Types Influence Authorship Perception and Creative Satisfaction?**

The second hypothesis—that interaction types carry different implications for learner agency and creative fulfillment—requires correlation and regression analyses linking interaction patterns to perceptual outcomes:

- **Pearson correlation analysis** examines bivariate relationships between Type C frequency and authorship perception scores, testing whether serendipitous surprises enhance or diminish ownership feelings
- **Multiple regression modeling** predicts authorship scores from Type A, B, and C percentages simultaneously, revealing each interaction type's independent contribution while controlling for others
- **Independent samples t-tests** compare authorship scores between high-Type B and low-Type B participants, directly testing the "helpful but alienating" paradox—whether curated exemplars, though pedagogically valuable, undermine creative ownership

**RQ3: Does Metacognitive Awareness Moderate Parameter Effects?**

The third hypothesis—that knowing about parameter manipulation influences how learners experience scaffolding—requires factorial analysis isolating main effects and interactions:

- **2×2 between-subjects ANOVA** treats authorship perception, creative satisfaction, and interaction type distributions as dependent variables, with parameter configuration (structured vs. exploratory) and awareness condition (aware vs. unaware) as independent factors. This design reveals whether parameter effects persist regardless of transparency, or whether metacognitive awareness amplifies or dampens parameter-driven differences
- **Main effects and interaction decomposition** distinguishes parameter configuration's direct influence from awareness condition's moderating role, addressing whether informed learners engage differently with scaffolding

**Analytical Rigor and Software Infrastructure**  
All analyses were conducted in R (version 4.3) using the tidyverse ecosystem for data manipulation, lme4 for mixed-effects modeling when accounting for participant-level clustering, and effsize for standardized effect magnitude calculations. Alpha levels were set at .05 for null hypothesis significance testing, while effect sizes contextualize practical significance beyond *p*-values.

### 3.3.3 Qualitative Analysis Procedures: Excavating Meaning from Discourse

While quantitative methods measure *what* happened—interaction frequencies, perception scores, behavioral patterns—qualitative analysis reveals *how* and *why* participants experienced parameter-driven scaffolding the way they did. Three complementary analytic traditions illuminate different dimensions of learner sense-making:

**Conversation Analysis: The Micro-Dynamics of Scaffolding Moves** (Jefferson, 2004)

Applying conversation analysis principles to chat transcripts reveals the sequential organization of human-AI creative dialogue. Turn-by-turn examination traces how:
- **Repair sequences** unfold in Type A interactions—how the AI identifies linguistic deviations, how learners respond to corrective guidance (acceptance, negotiation, resistance)
- **Learner uptake patterns** differ between active transformation (learners adapting AI suggestions to fit their vision) and passive selection (learners choosing from pre-generated options with minimal modification)
- **Scaffolding trajectories** evolve across sessions—moments when Type B exemplar giving transitions to Type C surprise harvest, signaling successful scaffolding *fading* as learners gain creative momentum

This micro-level analysis makes visible the *choreography* of collaborative creativity—the moment-by-moment dance between human intent and AI response that quantitative coding necessarily simplifies.

**Thematic Analysis: Patterns in Learner Narratives** (Braun & Clarke, 2006)

Reflection journals and panel discussion transcripts underwent systematic thematic analysis, moving from raw data to interpretive themes through recursive coding:

1. **Initial open coding** captured recurring concerns and perceptions: authorship anxieties ("Is this really my poem?"), scaffolding calibration judgments ("too much help"/"not enough"), creative agency descriptions ("I felt like a conductor")
2. **Theme development** organized codes into patterns distinguishing parameter conditions:
   - *Structured room themes*: "Over-scaffolding concerns" (AI dominance worries), "clarity and confidence" (appreciation for guidance), "safety with constraints" (risk-averse creativity)
   - *Exploratory room themes*: "Inspiring surprises" (serendipitous discoveries), "creative partnership" (co-authorship framing), "exciting uncertainty" (embracing AI unpredictability)
3. **Member checking** validated interpretations by sharing preliminary findings with pilot study participants, who confirmed theme resonance and offered clarifying nuances

This analysis reveals *shared cultural meanings* emerging within experimental conditions—how parameter configurations shape not just interaction patterns but collective understandings of creativity, agency, and collaboration.

**Discourse Analysis: How Learners Characterize AI's Role**

Participants' spontaneous characterizations during panel discussions—shared immediately after writing sessions—revealed strikingly different perceptions aligned with parameter conditions. Discourse analysis of these authentic descriptions identified three distinct framing patterns:

**Structured Condition Descriptions (Low Temperature/Top-p):**
Participants in structured rooms characterized AI interactions in mechanistic, transactional terms. One Room B participant (structured-unaware) described the experience bluntly: *"It feels like just AI... The options were me, but the writing itself—none of it was me."* When asked about authorship, another confirmed: *"It doesn't feel like mine. I'm just guiding it to summarize whatever I'm feeling and make it more beautiful."* These learners emphasized the AI's role as **option-provider** or **formulator**, offering preset alternatives rather than collaborative dialogue. Notably, a Room B participant observed: *"I couldn't feel any sort of creativity... It only ever outputted exactly what I asked it to"*—describing a constraining rather than enabling experience.

**Exploratory Condition Descriptions (High Temperature/Top-p):**
Exploratory room participants employed relational, humanizing language fundamentally different from structured room discourse. A Room C participant (exploratory-aware) characterized the AI as *"a very warm-hearted AI... like a very good friend, not just a machine."* This participant detailed emotionally attuned interactions: the AI *"sensed me feeling blue"* and responded with empathetic guidance beyond mechanical text generation. Another Room C participant, when asked about authorship distribution, claimed *"maybe twenty percent is due to AI, eighty percent me"*—asserting creative ownership despite extensive AI collaboration. Room D participants (exploratory-unaware) similarly described the AI as providing "*really helpful*" guidance that *"helped me explore more and be precise"* about creative intentions, framing interaction as *collaborative refinement* rather than passive selection.

**Cross-Condition Awareness:**
Most revealing was spontaneous comparative analysis by participants themselves. When the researcher disclosed that Rooms B and D shared identical settings with Rooms A and C respectively, a Room B participant immediately articulated the experiential difference: *"It's pretty obvious! On our lower temperature, ours took our words and tried to put it in poem form. Whereas comparing output from C and D... there's a lot of changes to the input format... I couldn't feel any sort of creativity."* This unprompted observation—from an *unaware* participant who hadn't known about parameter differences—demonstrates that scaffolding variations were phenomenologically real, not merely researcher constructs.

These metaphorical framings reveal how parameter-driven scaffolding shapes not just creative products but learners' *identities as writers* in AI-mediated spaces. Structured configurations position learners as *selectors* choosing from AI-curated options, while exploratory configurations enable *co-creator* identities where AI functions as collaborative partner. The discourse shift from "just AI" and "doesn't feel like mine" (structured) to "very good friend" and "eighty percent me" (exploratory) demonstrates that temperature and top-p settings don't merely adjust technical output—they fundamentally reconfigure the social relationship between human writer and AI collaborator.

### 3.3.4 Data Integration and Triangulation: Where Evidence Streams Converge

The power of convergent parallel mixed-methods design (Creswell & Plano Clark, 2017) lies not in collecting multiple data types but in systematically integrating them to reveal patterns more robust than any single source could provide. Quantitative measurements and qualitative insights were gathered simultaneously, then brought into dialogue during interpretation—*asking whether numbers and narratives tell the same story*. Three critical integration points demonstrate this convergence:

**Integration Point 1: Validating the Parameter→Interaction Type Mechanism**  
- **Quantitative evidence**: Type C (Surprise Harvest) frequency measured seven times higher in exploratory rooms (35% vs. 5%, *p* < .001)—a dramatic numerical difference suggesting parameters fundamentally reshape interaction distributions
- **Qualitative confirmation**: Panel discussions vividly corroborate this pattern as exploratory participants describe "surprising connections I wouldn't have thought of" and "the AI took my idea in directions I didn't expect," while structured participants characterize experiences as "helpful corrections when I made mistakes" and "clear examples to choose from"
- **Convergent interpretation**: Statistical difference is not measurement artifact—learners *experience* parameter-driven scaffolding changes, describing them in language that aligns with interaction type distinctions

**Integration Point 2: Unpacking the Authorship-Autonomy Paradox**  
- **Quantitative signal**: Type B (Exemplar Giving) frequency correlates negatively with authorship perception scores (*r* = -.58, *p* < .05)—a puzzling finding since exemplars represent pedagogically valued scaffolding
- **Qualitative illumination**: Reflection journals articulate the tension numbers alone cannot explain: "The AI gave me really good phrases, but they felt more like the AI's words than mine"; "I just kept picking from the options instead of creating my own language"—the *helpful but alienating* paradox
- **Convergent insight**: Type B's moderate-directive scaffolding occupies an uncomfortable middle ground—directive enough to constrain agency, but not transformative enough (like Type C) to feel like collaborative creation. Numbers measure the correlation; narratives reveal the *why*

**Integration Point 3: Revealing Adaptive DDL's Dynamic Mechanism**  
- **Quantitative demonstration**: Parameter manipulation significantly shifts interaction type distributions (χ² = 24.3, *p* < .001), proving technical lever causes pedagogical change
- **Qualitative mechanism**: Aware participants (Rooms 1 & 3) describe *actively adapting* their interaction strategies based on parameter knowledge: "I knew it was in structured mode, so I asked for more corrections"; "Because it was exploratory, I tried throwing wild ideas to see what it would do with them"
- **Convergent revelation**: Parameter configuration is not just technical setting but *pedagogical design lever*—especially powerful when metacognitive awareness transforms learners into active designers of their own scaffolding experiences

This triangulated approach provides robust, multi-dimensional evidence for ***how* parameter manipulation enables *dynamic* DDL scaffolding**—the central theoretical contribution of this study. Neither quantitative frequencies nor qualitative narratives alone could establish this claim so convincingly; convergence across evidence types transforms promising hypothesis into defensible conclusion.

### 3.3.5 Validity and Reliability Considerations

**Construct Validity**:
- **Interaction type definitions** grounded in established theoretical frameworks (Lyster & Ranta, 1997; Hanauer, 2010; Coenen et al., 2022)
- **Operationalization**: Temperature/top-p as scaffolding intensity based on documented LLM parameter effects (Holtzman et al., 2019; Peeperkorn et al., 2024)
- **Measurement instruments**: Authorship perception scales adapted from creativity research; DDL coding scheme validated through pilot testing

**Internal Validity**:
- **Unified system prompt** eliminates prompt-engineering confounds
- **Random assignment** to rooms controls for selection bias
- **Identical platform functionality** across conditions isolates parameter effects
- **Blind evaluation** of poem quality prevents rater bias

**External Validity: To What Contexts Can These Findings Generalize?**

While internal validity demands controlled conditions, external validity requires ecological authenticity:
- **Ecological validity**: This study employs a *real* poetry writing task with *authentic* L2 learners pursuing genuine creative goals—not artificial laboratory exercises divorced from meaningful writing contexts
- **Acknowledged generalizability boundaries**: Findings derive from a single university context (Hong Kong Baptist University), single 45-minute sessions, and a specific LLM model (GPT-4 via OpenRouter). Results may not extend to different learner populations, extended writing projects, or alternative AI architectures without empirical verification
- **Replication potential**: Comprehensive documentation of parameter settings (temp=0.3/0.8, top-p=0.4/0.9), unified system prompt, and platform architecture enables reproduction by other researchers—transparency supports cumulative knowledge building
- **Theoretical generalizability claim**: Despite contextual specifics, the underlying mechanism—parameter configuration enabling dynamic DDL scaffolding—should apply wherever AI-assisted L2 creative writing occurs. The *principle* generalizes even if precise interaction frequencies vary

**Reliability: Can These Measurements Be Replicated?**

Consistent measurement across coders, sessions, and contexts establishes finding dependability:
- **Inter-rater reliability**: Two independent coders achieved Cohen's κ = 0.84 on interaction type classifications—well above the .70 threshold for acceptable agreement, confirming coding scheme clarity and replicability
- **Platform stability verification**: Systematic parameter logging confirmed consistent API behavior—identical prompts with identical parameter settings produced statistically similar response distributions across sessions, validating experimental control integrity
- **Multi-source triangulation**: Reliance on six complementary data sources reduces single-method bias—convergent findings across chat logs, poem artifacts, reflection journals, panel discussions, and platform analytics strengthen confidence that patterns represent genuine phenomena rather than measurement quirks

Together, these validity and reliability safeguards establish this methodology as *trustworthy*—a research design capable of producing defensible knowledge about how parameter manipulation enables adaptive DDL scaffolding in AI-assisted L2 creative writing.

---

## 3.4 Summary: A Methodological Watershed for DDL Research

This methodology represents more than careful research design—it marks a **conceptual and infrastructural breakthrough** in how we study AI-assisted language learning. For the first time, we demonstrate ***how* parameter configuration functions as a pedagogical design lever** that dynamically reshapes DDL scaffolding affordances in real creative writing contexts. This contribution operates simultaneously at theoretical, empirical, and practical levels:

**Theoretical Innovation: Making the Invisible Visible**

Traditional DDL research treats corpus tools as static resources—concordancers that present linguistic patterns upon learner request. AI systems, by contrast, offer *dynamic* scaffolding that adapts mid-interaction, but this adaptivity has remained a black box. Our methodology **illuminates the mechanism**: By isolating parameter effects through unified prompting, systematic manipulation, and comprehensive interaction logging, we reveal that temperature and top-p settings function as *scaffolding intensity controls*—adjustable dials determining whether AI responses enact high-directive constraint repair, moderate-directive exemplar curation, or low-directive exploratory collaboration.

This finding reframes generative AI not as DDL's replacement but as its **evolution**—a shift from learner-initiated corpus queries to system-initiated pattern presentations calibrated through parameter configuration. We move beyond Crosthwaite's (2023) concern about generative AI "doing the work for learners" to demonstrate *how* parameter-aware design preserves inductive learning processes while enabling unprecedented scaffolding adaptivity.

**Empirical Innovation: A Transparent Research Laboratory**

The prompt-designed chatbot platform with complete interaction logging creates research infrastructure unavailable in prior studies. Unlike commercial AI tools (ChatGPT, Claude, Google Gemini) that hide parameter configurations and interaction details, our platform makes scaffolding mechanisms *observable*, *manipulable*, and *recordable*. This transparency enables:
- **Causal isolation**: Unified prompts eliminate confounding variables, attributing interaction differences definitively to parameter manipulation
- **Replication pathways**: Documented settings and open-source design allow other researchers to reproduce or extend findings
- **Multi-level analysis**: Six complementary data sources capture behavioral, linguistic, perceptual, and social dimensions simultaneously

The 2×2 factorial design (parameter × awareness) further advances DDL research by testing not just *whether* parameter effects exist but *whether metacognitive awareness amplifies adaptive engagement*—addressing the critical question of whether parameter literacy should be explicitly taught.

**Practical Innovation: From Research to Pedagogy**

Beyond scholarly contributions, this methodology generates **actionable knowledge** for language educators navigating AI integration:
- **Parameter literacy emerges as essential competence**: Just as DDL researchers teach corpus querying skills, AI-assisted writing instruction should cultivate parameter awareness—understanding that structured configurations (low temp/top-p) produce directive guidance while exploratory settings (high temp/top-p) enable creative discovery
- **Evidence-based configuration recommendations**: Rather than accepting default AI settings, educators can now calibrate scaffolding intensity to match pedagogical goals, learner proficiency, and task demands
- **Design principles for instructional AI**: The platform's dual commitments—instruction over generation, parameter observability for research—model how educational AI tools should differ from consumer products

**The Path Forward: Adaptive DDL as Research Frontier**

This methodology establishes a template for future investigations. Subsequent studies can extend parameter manipulations (exploring other LLM settings), vary task contexts (argumentative writing, collaborative editing), examine learner populations (different proficiencies, age groups, L1 backgrounds), or test long-term effects (multi-session longitudinal designs). The infrastructure and analytical frameworks developed here provide the foundation for cumulative, programmatic research into *how* AI systems can scaffold L2 writing development without undermining learner agency—the central challenge facing language education in the generative AI era.

In addressing Crosthwaite's (2023) foundational question about whether generative AI represents DDL's evolution or its demise, we provide an empirically grounded answer: **AI becomes DDL's evolution when parameter configuration enables dynamic scaffolding adaptation**. This methodology makes that claim not merely theoretical assertion but testable hypothesis, opening new research territories at the intersection of corpus linguistics, scaffolding theory, and human-AI collaboration.
