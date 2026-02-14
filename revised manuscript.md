From Static to Dynamic: Parameter Manipulation as Adaptive DDL Scaffolding in Creative Writing with Generative AI

YU Ruobin1,2*

1* Department of English, Hong Kong Baptist University, 224 Waterloo Road, 999077, Kowloon Tong, Hong Kong.

*Corresponding author. E-mail: 24484008@life.hkbu.edu.hk

Abstract

Generative AI tools now pervasively integrate into university classrooms, yet the field lacks empirical understanding of how technical AI configurations translate into adaptive Data-driven Learning (DDL) scaffolding for novice writers. This gap is critical in creative writing where excessive structure can suppress authorship and insufficient support can stall exploration. This study investigates how large language model (LLM) parameter configuration functions as a pedagogical design lever for DDL scaffolding in poetry writing classrooms. The work contributes by rendering parameter effects explicit and measurable, enabling instructors to design responsive AI systems that dynamically adapt scaffolding to learner needs, creative agency, and satisfaction.

Key Words: Data-driven Learning; AI parameter configuration; creative writing; Adaptive scaffolding; Human-AI collaboration.

Introduction

With the rise of generative AI, scholars pose a challenge to the language teaching profession: Generative AI, allowing learners to bypass inductive pattern discovery processes, represents the death of Data-driven learning (Crosthwaite and Baisa 2023). This paper argues that generative AI may represent an evolution rather than replacement of DDL principles. We examine this proposition through AI-assisted poetry writing in university creative writing classrooms, where the tension between DDL principles and generative AI becomes visible and pedagogically consequential.

Data-Driven Learning (DDL), put forward by Johns (1991) as the use of concordance data in language learning, has long valued inductive pattern discovery over deductive rule presentation. By engaging learners directly with corpus evidence, DDL shifts pedagogy from teacher-transmitted knowledge to learner-discovered insights (Boulton 2012). The power of DDL lies in learner autonomy and evidence-based discovery, aligning with constructivist and sociocultural perspectives on learning (Lantolf and Thorne 2006).

To answer whether AI-assisted writing constitutes DDL, we must challenge narrow conceptions of DDL as merely keyword matching or concordance consultation (Sinclair 1991). At its core, DDL is data-driven decision making in language learning: learners form hypotheses about language use, test them against patterns in data, and refine their output. Traditional DDL accomplishes this through explicit corpus queries and concordance searches (Cobb 2013). LLMs are trained on massive corpora and generate outputs by sampling from learned distributions of language patterns (Vaswani et al. 2017; Radford et al. 2019). When AI generates a poetic line or suggests an alternative phrasing, it functions as a data-driven pattern provider, even though the mechanism differs from explicit corpus search. In short, AI can serve as a new DDL interface if learners treat its outputs as linguistic data to notice, analyze, and revise.

Why poetry, and why AI-assisted poetry, count as DDL requires explicit justification. Poetry writing in university classrooms is not ineffable but effable. Hiedinger (Holderland) frames poetry as the opposite of machine logic, yet also insists that poetic meaning emerges from choices among constrained language possibilities. My stance is that machine influence is pedagogically valid when it is bounded and transparent: AI can provide pattern data and alternative options, while human writers remain responsible for selection, rejection, and revision. This is especially important for beginners in writing, who often have ideas and affective goals but lack linguistic resources to realize them. For these writers, AI-assisted poetry can still be DDL when the process foregrounds noticing, testing, and reflective decision making rather than substitution or ghostwriting.

In collaborative creative writing, the procedure combines student decisions (theme, emotion, style, form) with AI pattern-based text generation. Students exercise agency in conceptual and creative dimensions, while AI provides data-driven linguistic scaffolding, paralleling traditional DDL where learners formulate queries and receive evidence from corpus data. Therefore, AI-assisted DDL and traditional DDL are structurally similar in learning logic even if their interfaces differ.

Traditional DDL positions learners as query initiators who must formulate search criteria, execute corpus queries, and interpret concordance results. This learner-driven approach fosters autonomy but imposes high cognitive demands (Sun and Wang 2003). Moreover, corpus evidence reflects what has been written, not necessarily what could be written, a limitation that constrains creative writing where novelty and surprise are pedagogical goals. Generative AI transforms this dynamic by enabling system-initiated pattern presentation. Rather than learners laboriously searching corpora, AI proactively generates lines and alternatives that instantiate linguistic patterns within the creative process. This shift from learner-initiated queries to system-initiated presentation reduces cognitive overload while raising new questions: how should AI-mediated pattern presentation be configured to provide appropriate scaffolding for novice writers without displacing authorship?

We focus on university pedagogical contexts. The central aim of this chapter is to examine whether and how AI tools, used in creative writing classrooms, can enhance novice writers' authorship and ownership, creative agency, and satisfaction through parameter-based DDL scaffolding.

This study proposes a three-interaction-types framework that integrates DDL principles, scaffolding theory, and human-AI collaboration research. Coenen et al. (2022) identify serendipitous discovery as crucial for productive human-AI collaboration. Qian et al. (2023) show AI can redistribute cognitive load. Li (2025) finds AI shifts writers toward strategic collaboration. However, these studies treat AI as monolithic rather than examining how different AI configurations produce distinct interaction patterns. Our framework reveals the mechanism through which AI can dynamically adapt scaffolding: parameter configuration, specifically temperature and top-p settings, systematically shapes interaction type distributions. Lower parameter values (e.g., temperature 0.3, top-p 0.4) produce deterministic, corpus-typical outputs; higher values (e.g., temperature 0.8, top-p 0.9) generate more exploratory outputs (Holtzman et al. 2019; Li et al. 2025; Peeperkorn et al. 2024). This technical mechanism enables pedagogical adaptivity: parameter manipulation functions as a design lever for shifting between different DDL scaffolding modes.

We theorize three interaction types as parameter-dependent DDL-scaffolding modes, each serving distinct pedagogical functions:

Type A Constraint Repair: AI identifies deviations from linguistic or structural patterns and provides corrective guidance. This parallels traditional DDL use of concordance lines but occurs proactively rather than through learner-initiated queries. Type A represents normative pattern reinforcement, supporting formal requirements like syllable counts or grammatical accuracy. Low parameter values maximize Type A, providing heavy scaffolding but risking constraint on creative autonomy.

Type B Exemplar Giving: AI provides model phrases or line alternatives that learners select and adapt, aligning with imitation-transformation pedagogy (Hanauer 2010). Type B reduces cognitive load by offering concrete starting points and diverse stylistic models. It supports accessibility but risks passive selection over active creation.

Type C Surprise Harvest: AI generates unexpected ideas, metaphors, or directions that learners would not discover through conventional corpus consultation, aligning with serendipitous discovery in human-AI co-creativity (Coenen et al. 2022) and with theories of divergent thinking and the role of novelty in creative processes (Boden 2004). High parameter values increase Type C frequency, enabling AI to function as pattern-extender rather than pattern-reinforcer. Type C is low-directive and high-autonomy, providing light scaffolding that supports creative expansion while demanding critical judgment from writers.

Our research is guided by one central question and two sub-questions:

RQ1: In university creative writing classrooms, how do different parameter configurations affect the distribution of interaction types (Constraint Repair, Exemplar Giving, Surprise Harvest) in AI-assisted poetry writing?

RQ1a: How do these interaction types influence novice writers' authorship and ownership, creative agency, and satisfaction in collaborative poetry writing?

RQ1b: What pedagogical implications emerge for configuring AI as adaptive DDL scaffolding in creative writing classrooms?

Methodology

Research Design

We designed and deployed a poetry writing platform (poetry.aitutor.ink) that transforms the theoretical framework established in our introduction into a living experimental environment. The web-based platform features a prompt-designed chatbot system with two critical design principles distinct from commercial AI tools: (1) commercial AI tools typically position themselves as content generators, while our prompts constrain the AI to function as a guide rather than a ghostwriter; (2) where commercial tools treat parameters as trade secrets, our platform exposes them as manipulable pedagogy. The system functions as both learning environment and research instrument, enabling tracing of causal pathways between technical configurations and learner experiences. The platform uses OpenRouter API integration to access GPT-4 while maintaining full control over generation parameters.

We crafted prompts that govern AI behavior across chatrooms so that observed variation stems from parameter configuration rather than instruction differences. By holding prompts constant and manipulating parameters, we create a clean contrast where differences in interaction patterns can be attributed to different scaffolding strategies under various parameter conditions.

The prompt defines the chatbot role as a poetry writing assistant for novice writers in university creative writing classrooms and establishes response frameworks supporting all three interaction types:

Type A (Constraint Repair): Diagnostic feedback on structural, linguistic, or poetic elements requiring attention.

Type B (Exemplar Giving): Model texts, phrase alternatives, and curated options for learner selection and adaptation.

Type C (Surprise Harvest): Creative suggestions, unexpected metaphors, and generative possibilities extending beyond the learner's initial ideas.

By establishing two chatrooms with different parameter conditions, we re-conceptualize temperature and top-p as pedagogical design instruments that educators can use to scaffold:

Structured Chatroom: The Steady Guide (low parameter condition)

Temperature: 0.3 | Top-p: 0.4

Technical function: Tightens the AI's decision-making scope, producing predictable, corpus-typical outputs.

DDL function: Transforms the AI into a proactive tutor, surfacing linguistic patterns that learners would encounter through traditional corpus searches but delivering them contextually and conversationally.

Scaffolding function: Generates a teaching style dominated by Type A normative corrections and Type B conventional exemplars, creating heavy scaffolding that reduces cognitive load but risks constraining creative autonomy.

Exploratory Chatroom: The Creative Catalyst (high parameter condition)

Temperature: 0.8 | Top-p: 0.9

Technical function: Loosens the AI's generative constraints, sampling from broader token distributions, enabling outputs that deviate creatively from corpus norms.

DDL function: Generates linguistic possibilities that transcend training data frequencies.

Scaffolding function: Shifts the interaction ecology toward Type C exploratory divergence, providing light scaffolding that sparks creative expansion.

This parameter-interaction design reveals the mechanism through which AI can dynamically adapt to pedagogical circumstances, transitioning from structured tutor to exploratory partner simply by adjusting two numerical values. The how of dynamic DDL scaffolding becomes operationally tractable.

This study employed a three-phase design investigating AI-mediated DDL scaffolding across controlled and naturalistic classroom contexts:

Phase 1: 2x2 Factorial Experiment (N=10)

Design: Controlled laboratory-style experiment manipulating two independent variables:

1. Parameter Configuration (between-subjects)

Structured: Temperature 0.3, Top-p 0.4 (Rooms A and B)

Exploratory: Temperature 0.8, Top-p 0.9 (Rooms C and D)

2. Awareness Condition (between-subjects)

Aware: Participants are aware of parameters and potential effects (Rooms A and C)

Unaware: Participants do not know parameters or their effects (Rooms B and D)

This factorial design enables examination of direct parameter effects and meta-cognitive influences of parameter literacy on authorship and satisfaction.

Phase 2: Natural Classroom Environment: Offline In-Person Workshop (N=8)

Design: An offline classroom setting where participants self-select parameter conditions based on personal preference and creative goals. This phase investigates how writers engage with AI-assisted poetry writing when given agency, examining whether Phase 1 findings hold in authentic classroom practice.

Phase 3: Natural Classroom Environment: Online Workshop (N=12)

Design: An online learning environment maintaining self-selected parameter conditions. This phase extends Phase 2 across different learning environments to test robustness in remote interaction.

The progression from controlled experiment (Phase 1) to naturalistic classroom contexts (Phases 2 and 3) strengthens both internal validity and ecological validity.

Context and Participants

We recruited 30 university students from creative writing classrooms through course announcements and digital posters. Participants ranged from novice to intermediate writers with varied prior exposure to poetry and AI tools. The study emphasizes creative writing pedagogy rather than language background as a primary variable.

Intervention and Procedure

All three research sessions unfolded as a 75-minute experience designed to immerse participants in collaborative poetry writing:

Phase 1: Platform Orientation (10 minutes) Participants logged into assigned or self-selected rooms, familiarized themselves with the chatbot interface.

Phase 2: AI-Assisted Poetry Writing (35 minutes) Participants drafted, revised, and refined poems in conversation with the AI partner.

Phase 3: In-class Reflection Template (15 minutes) Participants reflected on authorship perception, creative satisfaction, and scaffolding experiences.

Phase 4: Panel Discussion (15 minutes) Participants shared insights on parameter effects and collaborative writing processes.

Data Collection

We collected five sources of data:

1. Complete chat histories from each participant.

2. Interaction type coding that classified each AI response according to the three interaction types.

3. Poem artifacts stored on the platform.

4. Reflection templates on authorship, satisfaction, perceived helpfulness, AI role descriptions, and preferences.

5. Panel discussion transcripts capturing emergent themes and metaphors.

Data Analysis Plan

Quantitative Analysis

RQ1: Do parameter configurations generate distinct interaction type profiles?

We compute interaction-type frequencies and percentages within each parameter condition and compare the resulting profiles across structured versus exploratory settings.

Qualitative Analysis

We apply conversation analysis (Jefferson 2004) to examine uptake patterns and scaffolding trajectories, and discourse analysis to examine how participants narrate identity and agency in panel discussions.

Ethical Safeguards and Transparency

All participants provided consent. Chat logs and personal information were stored in separate databases following IRB protocols. AI tool versions, prompts, and usage policies were documented for transparency.

Results

Across three phases, 1000+ message exchanges, 29 reflection templates, and 60+ minutes of panel discussion transcripts, we observe three core results.

1. Parameter Configuration Functions as Learner-Intuitive Scaffolding

Writers developed a reliable sense for different AI scaffolding intensities and could identify which parameter conditions aligned with their creative goals. Structured rooms generated interactions dominated by constraint repair (Type A) and exemplar giving (Type B), while exploratory rooms increased surprise harvest (Type C). These distributions were stable across controlled and naturalistic contexts.

Figure 1: Parameter Configurations Influence Interaction Type Contribution (figure omitted)

2. The Type B Paradox: Helpful but Alienating

Exemplar-giving interactions were consistently rated the most frequent and most helpful, yet also the most likely to trigger feelings of reduced ownership when adopted uncritically. This paradox underscores a tension between efficiency and authorship in AI-assisted writing.
In learning-theory terms, heavy reliance on Type B can amplify a surface approach when learners accept ready-made exemplars without integrating meaning or exercising evaluative control, whereas Type C's negotiation more naturally supports deep engagement (Marton and Saljo 1976; Entwistle and Ramsden 1983; Biggs 1987; Ramsden 2003).

Figure 2: Type B as the Most Frequent and Helpful Interaction (figure omitted)

3. Type C Enables Co-Authorship Through Iterative Reciprocity

Creative agency and satisfaction emerged most strongly when writers critically engaged with AI suggestions, including rejecting, negotiating, and refining them. These iterative reciprocal moves were most frequent in exploratory settings and were strongly associated with perceived ownership.

Discussion

The Type B paradox can be reinterpreted through surface and deep approaches to learning. Type B delivers ready-made exemplars and options that reduce cognitive load and can accelerate progress, but that same efficiency can invite surface engagement when learners accept selections without meaning-making or evaluation. In surface-oriented uptake, the learner's task collapses into choosing among options rather than interrogating why a line fits the poem's intent, voice, or imagery. This helps explain why Type B is frequently rated most helpful while simultaneously correlating with reduced ownership: the interaction supports performance but can thin out interpretive control. A DDL perspective expects learners to treat AI output as data to be tested and revised, yet Type B can short-circuit that process if it becomes a substitute for inquiry rather than a prompt for it. When Type B is used as a starting point for transformation, it can support deeper engagement, but the risk of surface learning rises when the interaction is framed as answer delivery rather than evidence for judgment (Marton and Saljo 1976; Entwistle and Ramsden 1983; Biggs 1987; Ramsden 2003).

Autonomy moderates this risk by changing how learners interpret the same scaffolding. In imposed contexts, Type B can feel like externally prescribed solution paths, which encourages compliance and surface completion. In voluntary contexts, the same exemplar support can be used strategically, with learners deliberately selecting it to fill language gaps while retaining conceptual control, which preserves deeper engagement. This aligns with our observation that satisfaction and ownership rebound when learners choose Type B for specific purposes, suggesting that agency over parameter selection is not a mere preference but a learning mechanism. From a pedagogical standpoint, the goal is not to eliminate Type B but to position it as a choice among modes, so that learners can align scaffolding intensity with task demands and personal confidence. In practice, explicit framing can help learners treat exemplar options as hypotheses to be tested rather than as correct answers to be adopted.

Assessment implications follow directly from this distinction. If surface uptake is possible through Type B, then evaluating AI-assisted writing solely by product quality risks rewarding compliance rather than depth of engagement. Assessment should therefore attend to process evidence: rationale for selections, revisions made after AI suggestions, and reflections that demonstrate evaluative control. Rubrics can explicitly credit the learner's critical decision-making and the degree to which AI output was interrogated, reshaped, or rejected. Such criteria make deep engagement visible and reduce incentives for passive adoption. This also creates alignment with DDL values, ensuring that AI functions as data for analysis rather than as a shortcut to completion (Marton and Saljo 1976; Entwistle and Ramsden 1983; Biggs 1987; Ramsden 2003).

Creativity Framework and Why Type C Supports Agency

We frame the results using a creativity framework that integrates Guilford's divergent and convergent creativity, Boden's theory of computational creativity, and empirical evidence on serendipitous discovery (Coenen et al. 2022). Divergent thinking generates multiple possibilities, while convergent thinking evaluates and refines them. Type C interactions supply divergent possibilities by extending the option space beyond what a novice writer would generate alone. Boden argues that computational systems can expand conceptual spaces by making non-obvious combinations; Type C operationalizes this by introducing surprising metaphors and directions. Empirically, Coenen et al. show that serendipitous discovery supports productive human-AI collaboration, a pattern observed here as writers used unexpected AI outputs to spark new lines, contrasts, and imagery.

From Creative Surprise to Critical Engagement and Authorship

However, novelty alone does not guarantee agency. The data show that agency grows when writers move from receiving surprise to critically engaging with it: evaluating relevance, revising language, and integrating or rejecting suggestions. This critical engagement builds self-efficacy because writers experience themselves as decision makers rather than passive acceptors. The iterative cycle of generate, judge, revise, and refine becomes a DDL-like loop that reinforces ownership. In other words, Type C contributes to agency not because it replaces human choice but because it provokes reflective choice.

Oulipo, Constraint, and Parameter Effects

Oulipo provides a useful conceptual lens for understanding parameter effects as pedagogical constraints. Oulipian practice demonstrates that constraint can generate creativity by forcing writers to explore alternative routes within bounded space. Parameter settings operate as a computational constraint: low parameters tighten the space (supporting Type A and B), while high parameters loosen the space (enabling Type C). In the classroom, these constraints are not mere technical settings but pedagogical levers. Structured parameters are appropriate when learners need form scaffolding and pattern stabilization; exploratory parameters are appropriate when the goal is expansion and experimentation. The key implication is not that one mode is superior, but that instructors can intentionally shift constraints to align with learning goals and creative stages.

Implications for DDL in Creative Writing Classrooms

First, AI-assisted poetry can be valid DDL when students treat AI output as data and are required to notice patterns, test options, and revise intentionally. Second, parameter transparency matters: learners can perceive and strategically deploy parameter differences, suggesting that explicit instruction on parameter effects can empower more purposeful collaboration. Third, when AI is framed as a partner rather than a ghostwriter, the interaction can foster creative agency and ownership, especially for novice writers.

Limitations and Future Directions

The study is limited to one institutional context and short-duration workshops. Our participant pool consisted entirely of L2 learners, so we have not yet examined potential differences between L1 and L2 writers in how parameter-based scaffolding is perceived or used. Future work should extend to longer-term classroom integration, explore instructor interventions that prompt critical engagement with AI output, and refine measures of authorship and self-efficacy. Further research can also examine how parameter shifts interact with genre, task type, and peer collaboration.

Conclusion

This chapter demonstrates that AI parameter configuration functions as adaptive DDL scaffolding in university creative writing classrooms. Parameter manipulation shapes interaction types, which in turn influence novice writers' agency, ownership, and satisfaction. By integrating DDL principles, creativity theory, and a constraint-based pedagogy lens, the study provides a practical design framework: configure AI not as a monolithic generator but as a pedagogical partner whose constraints can be tuned to support different stages of creative writing.
