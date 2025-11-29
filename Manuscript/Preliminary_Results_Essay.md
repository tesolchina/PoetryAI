# Preliminary Findings: Parameter Effects on Authorship and Creative Agency in AI-Assisted L2 Poetry Writing

## Abstract

This paper presents preliminary findings from an ongoing experimental study examining how LLM parameter configurations affect collaborative interaction types in L2 poetry writing. Using an established web-based platform (poetry.aitutor.ink), Session 1 (completed November 2024) analyzed 10 graduate students across four conditions varying temperature (0.3 vs. 0.8) and awareness. A three-type framework—Constraint Repair, Exemplar Giving, Surprise Harvest—coded chat transcripts, validated by panel discussion and feedback forms. High-temperature generated Type C (Surprise Harvest) at seven times the rate of low-temperature (35% vs. 5%), correlating with sixfold higher self-authorship (62.5% vs. 10%) and doubled satisfaction (4.75/5 vs. 2.0/5). Type B interactions (Exemplar Giving) showed paradox: 75% rated most helpful yet produced lowest authorship (10%). Findings demonstrate parameter configurations systematically determine interaction type distribution, functioning as pedagogical design choices. Two additional sessions (10 participants) will validate these patterns.

**Keywords:** AI-assisted writing, L2 poetry, authorship, creative agency, LLM parameters, human-AI collaboration

---

## 1. Introduction

The rapid integration of Large Language Models (LLMs) into educational contexts has transformed writing pedagogy, particularly for second language (L2) learners who face dual challenges of linguistic development and creative expression (Li, 2025). While AI writing assistants offer unprecedented scaffolding opportunities, fundamental questions persist about how technical configurations affect collaborative interaction patterns and learner agency in creative writing tasks.

LLM parameter configurations—specifically temperature and top-p nucleus sampling—directly control output characteristics. Temperature governs response variability (lower values produce predictable outputs; higher values generate diverse possibilities), while top-p determines vocabulary selection scope (Holtzman et al., 2019; Peeperkorn et al., 2024). Despite their technical significance, these parameters remain underexplored as pedagogical design elements in controlled L2 educational research.

### 1.1 Theoretical Framework: Three Interaction Types

This research builds on three established frameworks: **L2 creative writing pedagogy** (Hanauer, 2010), **corrective feedback and uptake theory** (Lyster & Ranta, 1997), and **human-AI co-creativity research** (Coenen et al., 2022). We conceptualize AI-human poetry collaboration as involving three distinct interaction types, each serving different pedagogical functions:

**Type A: Constraint Repair** occurs when AI identifies structural, formal, or linguistic issues in student drafts and provides targeted corrections or suggestions. This interaction type aligns with Lyster and Ranta's (1997) corrective feedback taxonomy, where AI functions as a diagnostic tool that surfaces specific areas needing attention—from meter irregularities to unclear imagery—enabling focused revision activities.

**Type B: Exemplar Giving** involves AI providing model texts, example lines, or complete poem options that students can select, adapt, or transform for their own creative purposes. Grounded in Hanauer's (2010) imitation-transformation pedagogy, this interaction type supports scaffolded learning where students evaluate exemplary features before making creative decisions.

**Type C: Surprise Harvest** emerges when AI generates unexpected creative possibilities that inspire new directions or reveal previously unconsidered options. Following Coenen et al.'s (2022) findings on serendipitous discovery in human-AI collaboration, this interaction type capitalizes on AI's capacity to expand creative search spaces and offer novel combinatorial possibilities.

### 1.2 Research Focus

This paper presents preliminary findings from an ongoing three-session experimental study examining how parameter configurations affect the distribution and quality of these three interaction types in AI-assisted L2 poetry writing. Session 1, completed in November 2024, provides initial evidence that parameter choices systematically influence interaction type distribution, with profound implications for authorship perception and collaborative dynamics.

---

## 2. Research Design and Implementation Status

### 2.1 Platform and Experimental Design

A custom web-based platform (poetry.aitutor.ink) enables systematic investigation of parameter effects through a 2×2 factorial design: **Parameter Configuration** (Structured: temp=0.3, top-p=0.4 vs. Exploratory: temp=0.8, top-p=0.9) × **Awareness Condition** (Aware vs. Unaware). Four rooms (A: Structured-Aware; B: Structured-Unaware; C: Exploratory-Aware; D: Exploratory-Unaware) employ identical system prompts with only parameters varied, ensuring observed differences reflect genuine parameter effects.

### 2.2 Implementation Status

**Session 1 (COMPLETED - November 24, 2024):** 10 participants, 2.5-hour session, 500+ message exchanges, 22-minute panel discussion, 8 feedback forms (66 questions each).

**Sessions 2-3 (SCHEDULED):** Remaining 10 participants (December 2024) plus follow-up interviews (January 2025).

**Participants:** Twenty English L2 graduate students at Hong Kong Baptist University with advanced proficiency (IELTS 6.5-7.5 equivalent).

### 2.3 Data Collection

Three data sources enable triangulation: (1) **Chat transcripts**—behavioral patterns; (2) **Panel discussion**—spontaneous reflection; (3) **Feedback forms**—systematic measurement of authorship, satisfaction, and interaction type preferences.

---

## 3. Preliminary Findings from Session 1

### 3.1 Finding 1: Parameter Settings Systematically Affect Interaction Type Distribution

Convergent evidence across all three data sources demonstrates that parameter configuration emerges as the primary determinant of interaction type distribution, which subsequently shapes both authorship perception and collaborative satisfaction in profound ways.

**Interaction Type Distribution:**

Systematic coding of chat transcripts revealed striking disparities between parameter conditions:

| Configuration | Rooms | Type A % | Type B % | Type C % |
|--------------|-------|----------|----------|----------|
| Low temperature, top-p (0.3) | A, B | 60% | 35% | 5% |
| High temperature, top-p (0.8) | C, D | 20% | 45% | 35% |

*Table 1: Interaction Type Distribution by Parameter Configuration*

The data illustrates a remarkable pattern: high-temperature settings generated Type C interactions at **seven times the rate** of their low-temperature counterparts (35% versus 5%), while low-temperature configurations produced **three times more Type A interactions** (60% versus 20%). This sevenfold difference in Type C frequency represents a fundamental shift in the pedagogical affordances available to learners.

**Panel Discussion Validation:**

Participants' spontaneous descriptions during the panel discussion aligned precisely with these quantitative patterns. A Room B participant articulated the low-temperature experience: "It gave me two or three options every time... I just chose," explicitly describing Type B dominance. Another noted, "Very structured even though I didn't go in with a structured idea," capturing the prevalence of Type A constraint-focused interactions.

The contrast with high-temperature experiences proved equally striking. While a Room B participant lamented, "I couldn't feel any sort of creativity," a Room C participant characterized the AI as "warm-hearted... like a very good friend." This language difference—mechanical versus relational—suggests fundamentally different collaborative modes: co-creation versus option selection.

**Authorship and Satisfaction Outcomes:**

| Room | Parameters | Avg Self-Authorship | Satisfaction |
|------|-----------|---------------------|---------------|
| A, B | Low (0.3/0.4) | 10-20% | 2.0/5 |
| C, D | High (0.8/0.9) | 62.5% | 4.75/5 |

*Table 2: Authorship and Satisfaction by Parameter Configuration*

The authorship data reveals a **sixfold difference** in self-perceived authorship (10-20% versus 62.5%) and a **90% satisfaction gap** (2.0/5 versus 4.75/5) directly attributable to parameter configuration.

**Critical Insight:** A Room B participant's written reflection crystallizes the authorship paradox: "I do not feel ownership... other than the last line I wrote myself." Despite making hundreds of selection decisions throughout the session, this participant claimed authorship only for independently generated content. This profound observation suggests that **selection among AI-provided options does not constitute authorship** in learners' phenomenological experience—a finding with significant implications for AI-assisted creative writing pedagogy.

### 3.2 Finding 2: Type B Creates "Helpful but Alienating" Paradox

Analysis of feedback forms unveiled a fundamental pedagogical tension: while 75% of participants rated Type B (Exemplar Giving) interactions as most helpful, Room B—which experienced 35% Type B interactions—reported merely 10% self-authorship. This paradox reveals a critical disconnect between perceived usefulness and authentic creative agency.

A Room B participant articulated this tension poignantly: "It felt more true and emotional before the AI. After it became **more formulaic and didn't really capture it**... good poem in the traditional sense, but I wish it was **less structurally rigid**." This observation illuminates how Type B interactions, while pedagogically accessible and immediately satisfying, may inadvertently undermine the very creative authenticity learners seek to achieve.

**Pedagogical Implications:** The findings suggest that Type B interactions maximize immediate pedagogical comfort while simultaneously minimizing creative agency. Low-temperature parameters (0.3/0.4) generate heavy Type B concentration (35%) that participants find helpful in the moment yet ultimately alienating to their authorial identity. In contrast, high-temperature parameters (0.8/0.9) achieve a more balanced ecosystem—maintaining substantial Type B support (45%) for scaffolding while introducing significant Type C discovery opportunities (35%)—thereby enabling both structured guidance and authentic co-creation.

### 3.3 Finding 3: Type C Enables Creative Transformation

Analysis of high-temperature chat transcripts revealed that Type C (Surprise Harvest) interactions functioned as pivotal transformative moments in the creative process, introducing unexpected possibilities that fundamentally altered participants' creative trajectories.

A striking example emerged from Room C, where the AI suggested to one participant: "Would using some found aspects such as citations help highlight the gravity?" This unexpected proposition introduced the **found poetry technique**—an advanced literary strategy the participant had not previously considered. Rather than simply correcting or exemplifying, the AI expanded the participant's creative repertoire through genuine surprise.

Another Room C participant described how "the AI reframed the entire interaction from poetry construction to therapeutic creative expression," illustrating Type C's capacity to transform not merely the poem but the fundamental purpose and meaning of the creative activity itself.

**Striking Contrast:** Chat transcripts from Room B (low-temperature) contained no comparable Type C moments. Instead, interactions remained confined to predictable patterns: Type B exemplar provision (AI offering 2-4 line options such as "Here are a few options based on your dream...") and Type A minor corrections. The absence of unexpected creative pivots resulted in qualitatively different collaborative experiences.

This experiential difference manifested vividly in participants' language during panel discussion. Room B participants characterized the AI using mechanical metaphors—"just following instructions"—while Rooms C and D participants employed relational language—"warm-hearted," "like a very good friend." These contrasting metaphors reflect fundamentally different collaborative modes: technical assistant versus creative partner.

### 3.4 Finding 4: Interaction Type Differences Are Observable to Learners

A particularly revealing moment of meta-awareness emerged during panel discussion when a Room B participant, despite belonging to the unaware condition, spontaneously articulated systematic differences in collaborative experiences across rooms:

> "Yeah, it's pretty obvious! Ours **took our words and put it in poem form** [Type B]. Whereas comparing C and D... **there's a lot of changes to the input** [Type C]. For me, **it only outputted exactly what I asked** [no Type C]. **I couldn't feel any sort of creativity.**"

This unprompted comparative analysis demonstrates that interaction type differences constituted **phenomenologically salient experiences** rather than subtle variations detectable only through post-hoc researcher coding. The participant precisely identified Type B's reformulation pattern and Type C's transformative quality using experiential language ("I couldn't feel any sort of creativity") that maps directly onto the theoretical framework.

**Methodological Significance:** This meta-awareness validates that parameter effects manifest as genuine technical phenomena sufficiently distinct for learners to perceive, categorize, and evaluate through direct experience. This finding suggests powerful pedagogical potential: rather than requiring explicit technical instruction about temperature and top-p parameters, students might develop sophisticated "AI literacy" by experiencing how different interaction patterns enable or constrain creative agency—learning to recognize, request, and critically evaluate interaction types for their creative goals.

### 3.5 Finding 5: Type C Predicts Authorship Perception and Satisfaction

**Table 3: Type C Presence Predicts Authorship and Satisfaction Outcomes**

| Room | Type C % | Self-Authorship | Satisfaction |
|------|----------|-----------------|---------------|
| A, B (Low-temp) | 5% | 10-20% | 2.0/5 |
| C, D (High-temp) | 35% | 62.5% | 4.75/5 |

The convergence of interaction type analysis with authorship and satisfaction measures reveals a striking predictive relationship: rooms characterized by Type C presence demonstrated **4-6 times higher self-authorship perception** (62.5% vs. 10-20%) and **more than doubled satisfaction ratings** (4.75/5 vs. 2.0/5).

This correlation illuminates the **mechanistic pathway** through which parameter configuration shapes pedagogical outcomes. Type A (Constraint Repair) and Type B (Exemplar Giving) interactions, despite their pedagogical utility, fundamentally position learners as **passive recipients** of corrections or **selectors** among AI-generated alternatives—roles that constrain creative agency regardless of technical helpfulness. In contrast, Type C (Surprise Harvest) interactions introduce unexpected creative directions that **require active learner judgment, integration, and transformation**—positioning students as genuine co-creators rather than consumers of AI output.

This finding suggests that parameter configuration affects authorship perception not through output quality alone, but **through systematic effects on interaction type distribution**: low-temperature parameters (0.3-0.4) constrain the AI to deterministic Type A/B behaviors that minimize opportunities for creative contribution, while high-temperature parameters (0.8-0.9) enable the variability necessary for Type C behaviors that invite authentic collaborative partnership.

---

## 4. Methodological Contributions

**Multi-source triangulation:** Chat histories (behavioral), panel discussion (spontaneous), and feedback forms (systematic) provide convergent validation. The "formulaic problem" emerged uniquely through feedback reflections, demonstrating value of triangulation.

**Interaction type framework:** The three-type coding scheme successfully captured parameter effects, with 87% inter-rater reliability (Cohen's κ=0.82), providing replicable method for analyzing human-AI creative collaboration.

---

## 5. Limitations and Future Directions

Small sample (n=10/20 completed) and single-session design limit generalizability. Cross-room comparison compromised awareness manipulation. Sessions 2-3 will validate findings with full sample, explore longitudinal development, and investigate individual difference moderators.

---

## 6. Preliminary Implications

**1. Interaction Type Distribution as Design Principle:** Sevenfold Type C difference (35% vs. 5%) shows parameter selection is fundamental pedagogical choice determining available interaction types, not minor technical detail.

**2. Progressive Pedagogy:** Navigate Type B paradox (75% helpful, 10% authorship) through progression: initial sessions use low-temperature (Type A/B scaffolding), transition to high-temperature as learners develop (Type C co-creation).

**3. Type C Enables Authorship:** Correlation between Type C presence and 4-6x higher authorship suggests creative writing should prioritize high-temperature parameters (0.7-0.9) despite output variability.

**4. AI Literacy through Interaction Types:** Learners spontaneously detected interaction type differences. Explicit instruction in three-type framework could enhance AI literacy: recognizing, requesting, and evaluating interaction types for creative goals.

---

## 7. Conclusion

These preliminary findings from Session 1 of an ongoing three-session study provide initial evidence that LLM parameter configurations profoundly shape collaborative creative writing experiences through their effects on **interaction type distribution**. The three-type framework (Constraint Repair, Exemplar Giving, Surprise Harvest) provides theoretical lens for understanding how parameter choices translate into pedagogical outcomes.

**Key Findings:**
1. **Sevenfold Type C difference:** High-temperature generates Type C at 35% vs. 5% in low-temperature
2. **Type B paradox:** Most helpful (75% preference) yet most alienating (10% authorship)
3. **Type C enables authorship:** Rooms with 35% Type C show 4-8x higher self-authorship
4. **Observable differences:** Learners spontaneously detect and articulate interaction type distributions

The established platform (poetry.aitutor.ink) has proven technically robust and educationally viable. Sessions 2 and 3, scheduled for December 2024 and January 2025, will validate these initial patterns with the full 20-participant sample and provide longitudinal perspective on how interaction type exposure affects creative development over time.

While preliminary, these findings challenge assumptions about AI parameter configuration as a neutral technical choice, demonstrating that temperature and top-p settings **systematically determine which pedagogical interaction types become available** to learners. As AI writing assistants become ubiquitous in educational settings, understanding the interaction type implications of parameter configuration becomes essential for pedagogically grounded implementation.

**Word Count: 1,997 words**

---

## References

Hanauer, D. I. (2010). *Poetry as research: Exploring second language poetry writing*. John Benjamins.

Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2019). The curious case of neural text degeneration. *arXiv preprint arXiv:1904.09751*.

Li, M. (2025). Generative artificial intelligence in second language writing: A comprehensive review of current research. *Language Teaching*, 1-29.

Peeperkorn, M., Bewersdorff, A., & Zhai, X. (2024). Is temperature the creativity parameter of large language models? *arXiv preprint arXiv:2405.00492*.
