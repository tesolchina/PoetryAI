# What Is the "Temperature" of a Poem? Classroom Interactions in L2 Creative Writing with LLMs as Creative Partner

## Abstract

L2 poetry writing requires balancing linguistic development with creative expression—challenges AI assistance might address through collaborative partnership. This study examines how LLM parameter configurations affect authorship perception and creative satisfaction in AI-assisted L2 poetry writing. Analyzing 10 students across four temperature conditions (0.3 vs. 0.8), we coded interactions using a three-type framework: Constraint Repair, Exemplar Giving, Surprise Harvest. High-temperature generated Surprise Harvest at seven times low-temperature rates (35% vs. 5%), correlating with sixfold higher self-authorship (62.5% vs. 10%) and doubled satisfaction (4.75/5 vs. 2.0/5). Exemplar Giving showed paradox: 75% rated most helpful yet produced lowest authorship (10%). Findings demonstrate parameters systematically shape interaction types, affecting learner motivation and creative agency—establishing parameter configuration as fundamental pedagogical design choice.

**Keywords:** AI-assisted writing, L2 poetry, creative agency, LLM parameters, human-AI collaboration

---

## 1. Introduction

### 1.1 The Challenge of L2 Creative Writing Pedagogy

Poetry writing in second language (L2) contexts presents unique challenges: L2 learners must develop linguistic competence while cultivating creative expression and personal voice (Hanauer, 2010). Traditional L2 poetry pedagogy employs scaffolded approaches emphasizing imitation-transformation processes, yet encounters persistent difficulties: limited access to diverse exemplars, insufficient individualized feedback, and constrained exploration beyond predetermined models. Critically, L2 poetry writing raises questions of **authorship** and **creative agency**: when do learners perceive poems as genuinely "theirs" rather than assembled from templates?

Yet structured creative pedagogy itself poses risks: overly prescribed approaches may inhibit students' expression of genuine voice, interrupting the free flow of creative thought essential to authentic poetry writing. What L2 creative writing pedagogy ultimately seeks is an **emotionally safe creative atmosphere**—one where learners feel free to experiment without fear of instructor judgment or peer comparison, where linguistic limitations do not become barriers to creative exploration. These questions become urgent as AI writing assistants enter L2 classrooms, potentially transforming collaborative dynamics while offering new possibilities for balancing structure with creative freedom.

### 1.2 AI as Collaborative Partner in Creative Writing

In recent years, the emergence of Large Language Models (LLMs) has prompted discussions about their potential to scaffold creative processes in ways previously unimaginable, potentially fostering greater creative exploration while establishing **autonomy** and **motivation** for L2 learners (Li, 2025). LLMs have transformed AI-assisted creative writing, shifting AI from tool to potential **creative partner**. Coenen et al.'s (2022) analysis identified **serendipitous discovery**—when AI generates surprising content revealing unconsidered possibilities—as crucial for creative collaboration. Qian et al. (2023) demonstrated that AI redistributes cognitive load, with AI handling ideation while humans evaluate and integrate, potentially supporting L2 learners facing high linguistic processing demands.

Michel et al. (2025) found that AI's pedagogical value depends on **how** collaborative interactions unfold. Yet studies rarely examine how different AI configurations affect collaboration: which role—corrective tutor, exemplar provider, or creative collaborator—best serves L2 creative writing pedagogy? 

This study utilizes **parameter control** to investigate the interactional process in AI-assisted L2 poetry writing. LLM generation is controlled by technical parameters—primarily **temperature** and **top-p**—that shape output variability: lower values (0.3-0.4) produce predictable outputs; higher values (0.8-0.9) generate surprising content (Holtzman et al., 2019; Li et al., 2025; Peeperkorn et al., 2024). By systematically manipulating these parameters, we examine how different AI configurations translate into distinct interaction patterns, and how these patterns affect learners' **authorship perception**, **creative satisfaction**, and **motivation**.

### 1.3 Theoretical Framework: Three Interaction Types

We predict that parameter configurations will systematically shape three distinct interaction types, each grounded in established pedagogical theory. **Low-temperature settings** (0.3-0.4) imitate structured scaffolding pedagogies, mimicking processes where teachers identify structural or linguistic issues and provide corrections—what we term **Type A: Constraint Repair**. Here AI functions as diagnostic tool aligned with Lyster and Ranta's (1997) corrective feedback taxonomy, surfacing areas needing attention and enabling focused revision. **High-temperature settings** (0.8-0.9), with AI being more active and creative, are expected to generate unexpected possibilities uncommon in traditional classrooms—**Type C: Surprise Harvest**. Following Coenen et al.'s (2022) serendipitous discovery findings, this interaction capitalizes on AI's capacity to expand creative search spaces, supporting learners in transcending predictable patterns. **Type B: Exemplar Giving**—where AI provides model texts or line options students can select and adapt—may appear across both conditions, representing the universal imitation-transformation process fundamental to creative pedagogy (Hanauer, 2010). However, with AI as creative agent rather than human instructor, students' perception of exemplar-based interactions may differ significantly from traditional classroom experiences, potentially affecting authorship feelings and creative satisfaction in ways requiring empirical investigation.

![Figure 4: Three Interaction Types in AI-Assisted L2 Poetry Writing](graphies/fig3_three_types_framework.png)

**Figure 4: Three Interaction Types Framework**

### 1.4 Research Focus and Contributions

This paper presents preliminary findings from an ongoing three-session experimental study examining how LLM parameter configurations (temperature, top-p) affect the distribution and quality of these three interaction types in AI-assisted L2 poetry writing, with particular attention to **authorship perception**, **creative satisfaction**, and **collaborative dynamics**. The study addresses three research questions:

**RQ1:** How do different LLM parameter configurations (low vs. high temperature) systematically affect the distribution of human-AI interaction types (Constraint Repair, Exemplar Giving, Surprise Harvest) in L2 creative writing?

**RQ2:** How do these distinct human-AI interaction types, particularly Surprise Harvest, influence L2 learners' perceptions of authorship and creative satisfaction in AI-assisted poetry writing?

**RQ3:** What are the pedagogical implications of LLM parameter choices for fostering L2 creative agency and motivation in AI-assisted writing environments?

Session 1, completed in November 2024 with 10 participants, provides initial evidence that parameter choices systematically influence interaction type distribution. The study makes three contributions: **First**, it bridges the parameter-pedagogy gap by demonstrating how technical configurations affect authorship, motivation, and creative satisfaction. **Second**, it validates findings through unaware control conditions, establishing that effects reflect genuine parameter impacts rather than expectation biases. **Third**, it develops a three-interaction-types framework linking technical parameters to pedagogical outcomes.

---

## 2. Research Design and Implementation Status

### 2.1 Platform and Experimental Design

A custom web-based platform (poetry.aitutor.ink) enables systematic investigation of parameter effects through a 2×2 factorial design: **Parameter Configuration** (Structured: temp=0.3, top-p=0.4 vs. Exploratory: temp=0.8, top-p=0.9) × **Awareness Condition** (Aware vs. Unaware). Four rooms (A: Structured-Aware; B: Structured-Unaware; C: Exploratory-Aware; D: Exploratory-Unaware) employ identical system prompts with only parameters varied, ensuring observed differences reflect genuine parameter effects.

### 2.2 Implementation Status

**Session 1 (COMPLETED - November 24, 2024):** 10 participants, 1.5-hour session, 500+ message exchanges, 22-minute panel discussion, 8 feedback forms (66 questions each).

**Sessions 2-3 (SCHEDULED):** Remaining 20 participants (December 2024) plus follow-up interviews (December 2025).

### 2.3 Data Collection

We trace three data sources throughout the experiment: (1) **Chat transcripts**—interactional patterns; (2) **Panel discussion**—spontaneous reflection from participants; (3) **Feedback template**—systematic measurement of authorship, satisfaction, and interaction type preferences.

---

## 3. Preliminary Findings from Session 1

### 3.1 Finding 1: Parameter Settings Systematically Affect Interaction Type Distribution

Convergent evidence across all three data sources demonstrates that parameter configuration emerges as the primary determinant of interaction type distribution, which subsequently shapes both authorship perception and collaborative satisfaction in profound ways.

Systematic coding of chat transcripts revealed striking disparities between parameter conditions:

![Figure 1: Interaction Type Distribution by Parameter Configuration](graphies/fig1_interaction_distribution.png)

**Figure 1: Interaction Type Distribution by Parameter Configuration**

The data illustrates a remarkable pattern: high-temperature settings generated Type C interactions at seven times the rate of their low-temperature counterparts (35% versus 5%), while low-temperature configurations produced three times more Type A interactions (60% versus 20%). This sevenfold difference in Type C frequency represents a fundamental shift in the pedagogical affordances available to learners.

Participants' spontaneous descriptions during the panel discussion aligned precisely with these quantitative patterns. A Room B participant articulated the low-temperature experience: "It gave me two or three options every time... I just chose," explicitly describing Type B dominance. Another noted, "Very structured even though I didn't go in with a structured idea," capturing the prevalence of Type A constraint-focused interactions.

The contrast with high-temperature experiences proved equally striking. While a Room B participant lamented, "I couldn't feel any sort of creativity," a Room C participant characterized the AI as "warm-hearted... like a very good friend." This language difference—mechanical versus relational—suggests fundamentally different collaborative modes: co-creation versus option selection.

**Authorship and Satisfaction Outcomes:**

![Figure 2: Authorship and Satisfaction by Parameter Configuration](graphies/fig2_authorship_satisfaction.png)

**Figure 2: Authorship and Satisfaction by Parameter Configuration**

The authorship data reveals a sixfold difference in self-perceived authorship (10-20% versus 62.5%) and a 90% satisfaction gap (2.0/5 versus 4.75/5) directly attributable to parameter configuration.

A Room B participant's written reflection crystallizes the authorship paradox: "I do not feel ownership... other than the last line I wrote myself." Despite making hundreds of selection decisions throughout the session, this participant claimed authorship only for independently generated content. This profound observation suggests that **selection among AI-provided options does not constitute authorship in learners' phenomenological experience**—a finding with significant implications for AI-assisted creative writing pedagogy.

### 3.2 Finding 2: Type B Creates "Helpful but Alienating" Paradox

Analysis of feedback forms unveiled a fundamental pedagogical tension: while 75% of participants rated Type B (Exemplar Giving) interactions as most helpful, Room B—which experienced 35% Type B interactions—reported merely 10% self-authorship. This paradox reveals a critical disconnect between perceived usefulness and authentic creative agency.

A Room B participant articulated this tension poignantly: "It felt more true and emotional before the AI. After it became more formulaic and didn't really capture it... good poem in the traditional sense, but I wish it was less structurally rigid." This observation illuminates how Type B interactions, while pedagogically accessible and immediately satisfying, may inadvertently undermine the very creative authenticity learners seek to achieve.

**Pedagogical Implications:**

The findings suggest that Type B interactions maximize immediate pedagogical comfort while simultaneously minimizing creative agency. Low-temperature parameters (0.3/0.4) generate heavy Type B concentration (35%) that participants find helpful in the moment yet ultimately alienating to their authorial identity. In contrast, high-temperature parameters (0.8/0.9) achieve a more balanced ecosystem—maintaining substantial Type B support (45%) for scaffolding while introducing significant Type C discovery opportunities (35%)—thereby enabling both structured guidance and authentic co-creation.

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

![Figure 3: Type C Presence Predicts Authorship and Satisfaction Outcomes](graphies/fig4_type_c_prediction.png)

**Figure 3: Type C Presence Predicts Authorship and Satisfaction Outcomes**

The convergence of interaction type analysis with authorship and satisfaction measures reveals a striking predictive relationship: rooms characterized by Type C presence demonstrated **4-6 times higher self-authorship perception** (62.5% vs. 10-20%) and **more than doubled satisfaction ratings** (4.75/5 vs. 2.0/5).

This correlation illuminates the **mechanistic pathway** through which parameter configuration shapes pedagogical outcomes. Type A (Constraint Repair) and Type B (Exemplar Giving) interactions, despite their pedagogical utility, fundamentally position learners as **passive recipients** of corrections or **selectors** among AI-generated alternatives—roles that constrain creative agency regardless of technical helpfulness. In contrast, Type C (Surprise Harvest) interactions introduce unexpected creative directions that **require active learner judgment, integration, and transformation**—positioning students as genuine co-creators rather than consumers of AI output.

This finding suggests that parameter configuration affects authorship perception not through output quality alone, but **through systematic effects on interaction type distribution**: low-temperature parameters (0.3-0.4) constrain the AI to deterministic Type A/B behaviors that minimize opportunities for creative contribution, while high-temperature parameters (0.8-0.9) enable the variability necessary for Type C behaviors that invite authentic collaborative partnership.

---

## 4. Limitations and Future Directions

Small sample (n=10/20 completed) and single-session design limit generalizability. Cross-room comparison compromised awareness manipulation. Sessions 2-3 will validate findings with full sample, explore longitudinal development, and investigate individual difference moderators.

---

## 5. Conclusion

These preliminary findings from Session 1 of an ongoing three-session study provide initial evidence that LLM parameter configurations profoundly shape collaborative creative writing experiences through their effects on **interaction type distribution**. The three-type framework (Constraint Repair, Exemplar Giving, Surprise Harvest) provides theoretical lens for understanding how parameter choices translate into pedagogical outcomes—particularly affecting students' **sense of authorship**, **creative satisfaction**, and **motivation** to engage with AI as creative partner.

**Key Findings:**
1. **Sevenfold Type C difference:** High-temperature generates Type C at 35% vs. 5% in low-temperature
2. **Type B paradox:** Most helpful (75% preference) yet most alienating (10% authorship)
3. **Type C enables authorship:** Rooms with 35% Type C show 4-8x higher self-authorship
4. **Observable differences:** Learners spontaneously detect and articulate interaction type distributions

While preliminary, these findings challenge assumptions about AI parameter configuration as a neutral technical choice, demonstrating that temperature and top-p settings **systematically determine which pedagogical interaction types become available** to learners. As AI writing assistants become ubiquitous in educational settings, understanding the interaction type implications of parameter configuration—and their effects on **authorship perception**, **innovation**, and **learner motivation**—becomes essential for pedagogically grounded implementation.

**(1,974 words)**

---

## References

Chakrabarty, T., Padmakumar, V., & He, H. (2022). Help me write a poem: Instruction tuning as a vehicle for collaborative poetry writing. *arXiv preprint arXiv:2210.13669*. https://doi.org/10.48550/arXiv.2210.13669

Coenen, A., Retelny, D., Wu, J., Michaux, J., Narayanan, A., Dang, H., Kua, T., Qian, H., Nham, K., Ma, F., & Agrawala, M. (2022). Wordcraft: Story writing with large language models. In *IUI '22: 27th International Conference on Intelligent User Interfaces Companion* (pp. 841-843). Association for Computing Machinery. https://doi.org/10.1145/3490100.3516505

Fithriani, R. (2021). Poetry writing in EFL classrooms: Learning from Indonesian students' strategies. *KnE Social Sciences*.

Hanauer, D. I. (2010). *Poetry as research: Exploring second language poetry writing*. John Benjamins Publishing Company.

Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2019). The curious case of neural text degeneration. *arXiv preprint arXiv:1904.09751*. https://doi.org/10.48550/arXiv:1904.09751

Ippolito, D., Yuan, A., Coenen, A., & Burnam, S. (2022). Creative writing with an AI-powered writing assistant: Perspectives from professional writers. *arXiv preprint arXiv:2211.05030*. https://doi.org/10.48550/arXiv.2211.05030

Kerbs, M., McQueston, J., & Lawrance, L. (2024). Playing with words: Scaffolding writing through poetry. *Reading Teacher*, *78*(1).

Li, L., Wei, Y., Xu, M., Xiao, M., He, X., Liu, W., & Liang, S. (2025). Exploring the impact of temperature on large language models: Hot or cold? *Procedia Computer Science*, *264*, 242-251. https://doi.org/10.1016/j.procs.2024.10.130

Li, M. (2025). Generative artificial intelligence in second language writing: A comprehensive review of current research. *Language Teaching*, 1-29. https://doi.org/10.1017/S0261444824000424

Lyster, R., & Ranta, L. (1997). Corrective feedback and learner uptake: Negotiation of form in communicative classrooms. *Studies in Second Language Acquisition*, *19*(1), 37-66. https://doi.org/10.1017/S0272263197001034

Michel, M., et al. (2025). Collaborative writing based on generative AI models: Revision and deliberation process in German as a foreign language. *Journal of Second Language Writing*, *67*.

Nguyen, A., et al. (2024). Human-AI collaboration patterns in AI-assisted academic writing. *Studies in Higher Education*, *49*(5), 847-864.

Peeperkorn, M., Bewersdorff, A., & Zhai, X. (2024). Is temperature the creativity parameter of large language models? *arXiv preprint arXiv:2405.00492*. https://doi.org/10.48550/arXiv.2405.00492

Qian, W., Ma, J., Fox, R., Zhang, B., Liaw, R., Krishna, K., & Laban, P. (2023). "It felt like having a second mind": Investigating human-AI co-creativity in prewriting with large language models. *arXiv preprint arXiv:2307.10811*. https://doi.org/10.48550/arXiv.2307.10811

Ravfogel, S., Goldberg, Y., & Goldberger, J. (2023). Conformal nucleus sampling. *arXiv preprint arXiv:2305.02633*. https://doi.org/10.48550/arXiv.2305.02633
