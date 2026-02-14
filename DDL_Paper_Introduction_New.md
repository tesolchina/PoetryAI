# Introduction: From Static to Dynamic — Parameter Manipulation as Adaptive DDL Scaffolding

## Opening: Responding to Crosthwaite's Challenge

In a provocative commentary on the future of language pedagogy, Crosthwaite (2023) posed a critical question: Does the rise of generative AI technologies represent "the death of data-driven learning" (DDL)? His concern reflects a broader anxiety in applied linguistics—that AI's ability to produce seemingly fluent language output without explicit corpus consultation might render DDL's foundational principles of learner-driven pattern discovery obsolete. If AI can generate text instantly without requiring learners to formulate queries, examine concordance lines, or inductively derive patterns from authentic language data, does this convenience come at the cost of the very pedagogical benefits that made DDL revolutionary?

This paper argues the opposite: **generative AI represents an evolution rather than replacement of DDL principles**, extending Johns' (1991) vision of learners as "research workers" into dynamic, system-initiated pattern engagement that traditional corpus tools cannot provide. However, this claim requires careful substantiation. It is insufficient to simply assert compatibility between AI and DDL; we must demonstrate *how* AI-mediated interaction can preserve—and potentially enhance—the inductive, evidence-based learning that DDL champions. More critically, we must address a fundamental pedagogical challenge: **How can AI-mediated pattern presentation be *dynamically* adapted** to provide appropriate scaffolding across different learning contexts and learner needs?

## The Central Question: Understanding *How* and *Dynamic*

Understanding how AI enables dynamic DDL scaffolding in creative contexts requires examining two interconnected dimensions. First, we must identify the **fundamental differences** between traditional corpus consultation and AI-mediated pattern engagement. Traditional DDL positions learners as query initiators who actively search concordance lines for patterns, whereas AI can present patterns proactively without explicit learner requests. This shift from learner-initiated to system-initiated pattern exposure raises legitimate questions: Does AI bypass the inductive discovery process central to DDL pedagogy? When AI generates novel text rather than retrieving corpus examples, does this violate DDL's evidence-based foundation?

Second, we must reveal the **mechanisms through which AI's pedagogical affordances can be systematically shaped**. If AI is to function as adaptive DDL scaffolding rather than a black-box text generator, educators need principled approaches to configure AI systems. This is where the notion of "dynamic" becomes critical: effective scaffolding must adjust support based on learner performance (contingency), gradually reduce assistance as competence develops (fading), and progressively transfer responsibility from expert to learner (Wood, Bruner, & Ross, 1976; van de Pol, Volman, & Beishuizen, 2010). Yet existing AI-assisted writing research has primarily focused on *whether* AI supports writing improvement, not *how* AI can dynamically adapt scaffolding intensity through systematic configuration.

## From Problem to Framework: The Three-Interaction-Types Model

Creative writing in L2 contexts presents unique scaffolding challenges that intensify these questions. Learners must simultaneously achieve linguistic accuracy (requiring normative guidance) and creative expression (requiring exploratory freedom). This dual requirement creates what Hanauer (2010) terms the **imitation-transformation dialectic**: learners must internalize exemplars while simultaneously developing authentic creative agency. When AI provides pattern-based support, it risks either over-scaffolding (constraining creative agency through excessive correction) or under-scaffolding (overwhelming learners with unstructured suggestions).

To understand how AI-mediated DDL operates dynamically in creative writing contexts, this paper proposes a **three-interaction-types framework** derived from empirical analysis of AI-learner exchanges in L2 poetry writing:

1. **Type A: Constraint Repair** — AI identifies deviations from corpus-typical patterns and initiates normative corrections, providing high-directive scaffolding focused on error detection and form accuracy.

2. **Type B: Exemplar Giving** — AI presents corpus-informed alternatives to learner expressions without explicitly marking errors, offering moderate-directive scaffolding through curated pattern exposure.

3. **Type C: Surprise Harvest** — AI generates corpus-divergent suggestions that extend beyond training data frequencies, providing low-directive scaffolding that stimulates creative exploration while maintaining linguistic plausibility.

Critically, our framework reveals the mechanism through which AI can *dynamically* adapt scaffolding: **parameter configuration**—specifically temperature and top-p settings—systematically shapes interaction type distributions. Low parameter values (e.g., temperature 0.3, top-p 0.4) maximize Type A and B frequencies by constraining AI outputs to corpus-typical patterns, providing heavy scaffolding through normative guidance. Conversely, high parameter values (e.g., temperature 0.8, top-p 0.9) dramatically increase Type C frequency (preliminary findings suggest 7× higher occurrence: 35% vs. 5%), enabling corpus-divergent generation that preserves creative agency while maintaining linguistic quality.

## From Framework to Empirical Investigation

This parameter-interaction relationship has profound pedagogical implications: **parameter configuration shapes whether AI functions as corrective tutor (Type A), exemplar provider (Type B), or creative collaborator (Type C)**, directly impacting learner agency, creative satisfaction, and the inductive discovery processes central to DDL pedagogy. Yet existing research has established *that* AI can support L2 creative writing but has not investigated *how* AI can dynamically adapt scaffolding intensity through systematic configuration manipulation.

This "how" and "dynamic" gap is critical. If parameter settings determine interaction type distributions, then controlled parameter manipulation should enable **adaptive DDL scaffolding** that shifts between normative correction, curated exemplars, and exploratory divergence depending on pedagogical goals. For example, early drafting stages might prioritize exploratory settings (high temperature/top-p) to maximize Type C interactions and preserve creative momentum, while revision stages might employ structured settings (low temperature/top-p) to foreground Type A interactions for accuracy refinement.

The present study addresses this gap by investigating how parameter configuration affects interaction type distributions and subsequent learner outcomes in AI-assisted L2 poetry writing. We designed a prompt-engineered chatbot platform that maintains systematic parameter control while enabling natural writing interactions, creating a research infrastructure that makes parameter effects visible and recordable. This methodological approach allows us to empirically examine **how parameter configuration dynamically shapes the pedagogical nature of AI-assisted L2 creative writing**.

## Bridging Three Research Domains

This study contributes to three intersecting research domains:

**For DDL research**: We extend data-driven learning principles from static corpus consultation to dynamic, generative AI interaction, examining how AI-mediated engagement with linguistic patterns differs from traditional concordance-based approaches. Crucially, we demonstrate that AI preserves DDL's evidence-based foundation—not through corpus retrieval, but through corpus-informed generation governed by training data distributions. This addresses Crosthwaite's concern by showing that AI represents DDL's evolution into adaptive, system-initiated pattern presentation.

**For scaffolding research**: We operationalize scaffolding through interaction type distribution, demonstrating how adaptive support emerges from parameter manipulation rather than requiring real-time human judgment. This provides a principled framework for implementing Wood et al.'s (1976) scaffolding functions (recruitment, direction maintenance, frustration control) through computational configuration, revealing new possibilities for scalable adaptive support in L2 writing pedagogy.

**For AI-assisted writing research**: We demonstrate that **parameter configuration constitutes pedagogical design**, not merely technical implementation. By establishing the parameter-interaction-outcome relationship, we provide educators with actionable knowledge for configuring AI systems to achieve specific pedagogical goals—whether prioritizing accuracy, creativity, or their dynamic integration across writing stages.

## The Fundamental Question

Can AI provide the pattern-based induction of DDL, the adaptive support of scaffolding theory, and the creative inspiration needed for authentic L2 writing—simultaneously and appropriately? Preliminary findings suggest this question has empirical answers with significant pedagogical implications. By revealing how parameter configuration functions as a mechanism for dynamic scaffolding adaptation, this study demonstrates that generative AI does not represent the death of DDL, but rather its transformation into adaptive, context-responsive pattern engagement that extends Johns' vision of learners as research workers into the generative AI era.

The remainder of this paper is structured as follows: We first review DDL principles and their evolution from static corpus consultation to AI-mediated pattern engagement (Section 1), then examine scaffolding theory's application to creative writing contexts (Section 2). We present the three-interaction-types framework and its theoretical grounding (Section 3), followed by implications for adaptive scaffolding design (Section 4). We then detail the present study's methodology and research questions (Section 5), before discussing contributions to DDL, scaffolding, and AI-assisted writing research (Section 6). The paper concludes by addressing Crosthwaite's challenge with empirical evidence: generative AI, properly configured, represents not the death but the dynamic evolution of data-driven learning.

---

**Word Count**: ~1,350 words

**Key Features**:
- Opens with Crosthwaite's challenge and provides direct response
- Emphasizes the dual focus on "HOW" (mechanism) and "DYNAMIC" (adaptive nature)
- Introduces the three-interaction-types framework early
- Establishes parameter configuration as the key mechanism
- Shows clear progression from problem → framework → empirical investigation
- Bridges three research domains (DDL, scaffolding, AI-assisted writing)
- Maintains scholarly tone while being accessible
- Provides clear roadmap for the paper's structure
