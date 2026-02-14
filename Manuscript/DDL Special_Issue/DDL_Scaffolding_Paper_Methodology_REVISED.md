# Methodology Section - REVISED VERSION
## Three-Phase Experimental Design

---

## 2. Methodology

### 2.1 Platform Building and Chatbot Design: Operationalizing DDL-Scaffolding Theory

We designed and deployed a purpose-built poetry writing platform (poetry.aitutor.ink) that transforms the theoretical framework established in our introduction into a living experimental environment. The web-based platform features a prompt-designed chatbot system with two critical design principles distinguished from commercial AI tools: 

**Commercial AI tools** typically position themselves as content generators—producing complete poems with a single prompt, effectively displacing the writer from the creative process. Through careful prompt engineering, we constrained the AI to function as a guide rather than ghostwriter, embodying three complementary pedagogical roles: a writing coach, a creative collaborator, and a language resource.

**Where commercial AI tools** treat parameters as proprietary trade secrets, our platform exposes them as manipulable pedagogy. We engineered the system to function as both learning environment and research instrument, embedding multiple layers of observability. This dual specialization—instructional prompt design married to parameter observability—creates a methodological innovation: we can finally trace the causal pathways through which technical configurations translate into learner experiences, answering the how question that previous research left unresolved.

The platform was built using Lovable with OpenRouter API integration, enabling access to GPT-4 as the underlying language model while maintaining full control over generation parameters.

#### Prompt Engineering and Parameter Configuration

We crafted prompts that would govern AI behavior across chatrooms, making it impossible to discern whether observed variations stem from how the AI is configured (parameters) or what it is instructed to do (prompts). By holding the prompts while manipulating parameters, we created a clean experimental contrast where differences in interaction patterns could be attributed to different scaffolding strategies under various parameter conditions.

Our prompt defines the chatbot's role as a poetry writing assistant for L2 learners (CEFR B1-B2 proficiency) and establishes response frameworks supporting all three interaction types:

- **Type A (Constraint Repair)**: Diagnostic feedback on structural, linguistic, or poetic elements requiring attention;
- **Type B (Exemplar Giving)**: Model texts, phrase alternatives, and curated options for learner selection and adaptation; 
- **Type C (Surprise Harvest)**: Creative suggestions, unexpected metaphors, and generative possibilities extending beyond learner's initial ideas.

The prompt establishes clear conversational boundaries—responses constrained to 40-80 words to prevent overwhelming learners—while cultivating an encouraging, culturally responsive voice that honors diverse creative perspectives. Rather than positioning the AI as an error-hunting corrector, the prompt frames it as a collaborative partner invested in the learner's creative vision.

The conceptual breakthrough enabling our investigation lies in reconceptualizing temperature and top-p not as obscure technical settings but as **pedagogical design instruments**—adjustable dials that educators can turn to calibrate scaffolding intensity:

##### Structured Configuration: The Steady Guide (Low Parameters)

**Temperature: 0.3 | Top-p: 0.4**

- **Technical function**: Tightens the AI's decision-making scope, constraining token selection to high-probability choices that mirror training data frequencies—producing predictable, corpus-typical outputs.
- **DDL function**: Transforms the AI into a proactive concordancer, surfacing linguistic patterns that learners would encounter through traditional corpus searches, but delivering them contextually and conversationally.
- **Scaffolding function**: Generates a teaching style dominated by Type A normative corrections ("This line needs a stronger verb") and Type B conventional exemplars ("You could try 'whispers' instead of 'says'"), creating heavy scaffolding that reduces cognitive load but risks constraining creative autonomy.
- **Learner experience**: Encounters an AI that behaves like a patient tutor—systematic, educational, reliably helpful, but potentially over-directive.

##### Exploratory Configuration: The Creative Catalyst (High Parameters)

**Temperature: 0.8 | Top-p: 0.9**

- **Technical function**: Loosens the AI's generative constraints, sampling from broader, more diverse token distributions, enabling outputs that deviate creatively from corpus norms.
- **DDL function**: Elevates the AI beyond pattern retrieval into pattern extension—generating linguistic possibilities that transcend training data frequencies, a generative capability impossible in static corpus DDL.
- **Scaffolding function**: Shifts the interaction ecology toward Type C exploratory divergence ("What if rain becomes hunger in your metaphor?"), providing light scaffolding that sparks creative expansion while demanding learners critically evaluate and selectively integrate surprising suggestions.
- **Learner experience**: Encounters an AI that behaves like an experimental collaborator—imaginative, sometimes unexpected, occasionally confusing, but potentially inspiring.

This parameter-interaction choreography reveals the mechanism through which AI can dynamically modulate its pedagogical presence—transitioning from structured tutor to exploratory partner simply by adjusting two numerical values. The how of dynamic DDL scaffolding, long theorized but never empirically demonstrated, becomes operationally tractable.

### 2.2 Experimental Design: Three-Phase Investigation

This study employed a three-phase design investigating AI-mediated DDL scaffolding across controlled experimental and naturalistic classroom contexts:

#### Phase 1: 2×2 Factorial Experiment (N=10)

**Design**: Controlled laboratory-style experiment manipulating two independent variables:

**1. Parameter Configuration (Between-subjects)**
- Structured: Temperature 0.3, Top-p 0.4 (Rooms A & B)
- Exploratory: Temperature 0.8, Top-p 0.9 (Rooms C & D)

**2. Awareness Condition (Between-subjects)**
- Aware: Participants informed about parameter manipulation and its potential effects (Rooms A & C)
- Unaware: No information provided about technical parameters (Rooms B & D), serving as primary controls for isolating genuine parameter effects uncontaminated by expectancy or demand characteristics.

**Purpose**: This factorial design enabled systematic examination of direct parameter effects (structured vs. exploratory) and metacognitive influences of parameter literacy (aware vs. unaware), addressing research questions about both technical mechanisms and learner perceptions under controlled conditions.

**Participants**: Ten L2 English learners recruited from Hong Kong Baptist University's undergraduate population through course announcements and digital posters. All participants met CEFR B1-B2 proficiency criteria—intermediate English users capable of expressing themselves creatively while still grappling with linguistic constraints that make scaffolding valuable. Their ages ranged from 18 to 32, with Indian, Thai, Mandarin, and Cantonese L1 backgrounds reflecting Hong Kong's linguistic landscape. Participants were randomly assigned to experimental rooms, ensuring balanced representation across parameter conditions.

#### Phase 2: Natural Classroom Environment - Offline In-Person Workshop (N=8)

**Design**: Naturalistic offline in-person classroom setting where participants self-selected into parameter conditions based on personal preference and creative goals, shifting from experimental control to authentic face-to-face pedagogical context.

**Purpose**: This phase investigated how learners engage with AI-assisted poetry writing when given agency over their learning environment in a traditional classroom setting, examining ecological validity of Phase 1 findings and exploring how voluntary participation, self-selection, and face-to-face interaction affect creative outcomes, authorship perception, and interaction patterns.

**Participants**: Eight undergraduate students from Hong Kong Baptist University enrolled in an offline L2 creative writing workshop. Participants voluntarily joined the session without grade-related incentives, creating a low-stakes, intrinsically motivated learning environment with opportunities for real-time peer interaction and instructor support.

#### Phase 3: Natural Classroom Environment - Online Workshop (N=12)

**Design**: Extended naturalistic implementation in an online learning environment, maintaining voluntary participation and self-selected parameter conditions while introducing iterative refinements based on Phase 2 observations. This phase shifted from face-to-face to remote interaction to test environmental robustness.

**Purpose**: This phase validated and extended Phase 2 findings across different learning environments (offline vs. online), examining whether parameter effects and interaction patterns remain consistent when learners engage with the platform remotely rather than in physical classroom settings, and exploring how synchronous online interaction affects learner engagement and creative development.

**Participants**: Twelve undergraduate students from Hong Kong Baptist University, similarly recruited through voluntary workshop participation without grade-related incentives, joining via online video conferencing platform.

**Rationale for Three-Phase Design**: The progression from controlled experiment (Phase 1) to naturalistic classroom contexts (Phases 2-3) addresses a critical limitation in educational technology research: findings from tightly controlled laboratory studies often fail to translate to authentic classroom practice. By triangulating across experimental and naturalistic settings, and across offline in-person and online environments, this design strengthens both internal validity (Phase 1's controlled parameter manipulation) and ecological validity (Phases 2-3's authentic classroom contexts in different modalities). This multi-environment approach provides evidence about how parameter configuration functions as pedagogical design under ideal conditions, in traditional face-to-face classrooms, and in remote online learning contexts—addressing concerns about environmental robustness and technological scalability.

#### Orchestrating the Poetry Writing Experience

Across all three phases, research sessions unfolded as a carefully sequenced 75-minute experience designed to immerse participants in collaborative poetry writing while capturing multiple layers of data:

##### Phase 1: Platform Orientation (10 minutes)

Setting the Stage - Participants logged into their assigned rooms (or self-selected rooms in Phases 2-3), familiarized themselves with the chatbot interface. This brief orientation established technical comfort before creative work began.

##### Phase 2: AI-Assisted Poetry Writing (35 minutes)

The Creative Crucible - Participants entered a focused creative space where they drafted, revised, and refined poems in conversation with their AI partner.

##### Phase 3: In-class Reflection Template (15 minutes)

Capturing Immediate Impressions - While creative experiences remained vivid, participants responded to structured reflection probing authorship perception, creative satisfaction, and scaffolding experiences.

##### Phase 4: Panel Discussion (15 minutes)

Parameter Observation and Meaning-Making - Participants sharing their insights on parameter effects and narrating their creative journeys in different parameter conditions. These discussions generated rich qualitative data as learners compared experiences, debated cross-room differences, AI's role, and articulated insights about authorship and collaboration.

#### Ethical Safeguards and Transparency

All participants provided informed consent before engaging with the platform. Chat logs and personal identifiers were stored in separate encrypted databases following HKBU IRB protocols, with data retention and destruction procedures clearly communicated.

---

**Note**: This revised methodology section reflects the three-phase design:
- Phase 1: Controlled 2×2 factorial experiment (N=10)
- Phase 2: Natural classroom environment - Offline in-person workshop (N=8)
- Phase 3: Natural classroom environment - Online workshop (N=12)

The revision maintains all other methodological details (platform design, prompt engineering, parameter configurations, session procedures, ethical safeguards) from the original while restructuring the experimental design section to accurately represent the multi-phase approach.
