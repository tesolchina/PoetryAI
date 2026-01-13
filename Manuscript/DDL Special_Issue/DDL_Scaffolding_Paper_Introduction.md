# From Static to Dynamic: Parameter Manipulation as Adaptive DDL Scaffolding in L2 Creative Writing with AI

## Introduction and Literature Review

### Answering Crosthwaite (2023): Evolution, Not Replacement

Crosthwaite (2023) poses a fundamental challenge to the language teaching profession: Does generative AI represent "the death of DDL" by allowing learners to bypass the inductive pattern discovery processes central to Data-Driven Learning pedagogy? This paper argues the opposite—**generative AI represents an evolution rather than replacement of DDL principles**, extending Johns' (1991) vision of learners as "research workers" into dynamic, system-initiated pattern engagement that traditional corpus tools cannot provide.

We examine this proposition through L2 creative writing, where the tension between DDL principles and generative AI becomes most visible. Unlike discrete grammar or vocabulary tasks where corpus patterns offer clear guidance, creative writing demands that learners **discover generative possibilities** within linguistic constraints—a process that generative AI can either support through adaptive scaffolding or undermine through over-determination. Understanding ***how* AI enables *dynamic* DDL scaffolding** in creative contexts requires examining the fundamental differences between traditional corpus consultation and AI-mediated pattern engagement, and identifying the mechanisms through which AI's pedagogical affordances can be systematically shaped.

### 1. From Static Concordances to System-Initiated Pattern Presentation: DDL Principles in the Generative AI Era

Data-Driven Learning (DDL), pioneered by Johns (1991) as "the use of concordance data in language learning," has long championed inductive pattern discovery over deductive rule presentation. By engaging learners directly with corpus evidence—concordance lines, frequency distributions, collocational patterns—DDL transforms language pedagogy from teacher-transmitted knowledge to learner-discovered insights (Boulton, 2012). The pedagogical power of DDL lies in its emphasis on **learner autonomy** and **evidence-based discovery**—principles that align closely with constructivist learning theory and sociocultural approaches to second language acquisition (Lantolf & Thorne, 2006).

**The Critical Difference: Traditional DDL vs. Generative AI-Assisted DDL**

Traditional DDL positions learners as active **query initiators** who formulate search criteria and interpret concordance results (Johns, 1991). This learner-driven approach, while fostering autonomy, imposes heavy cognitive demands: metalinguistic awareness to formulate queries, technical competence in corpus tools, and tolerance for data ambiguity (Sun & Wang, 2003). Moreover, corpus data by definition represents **patterns of what has been written**, not necessarily what *could* be written—a limitation particularly salient in creative writing where novelty and originality are pedagogical goals.

Generative AI fundamentally transforms this dynamic by enabling **system-initiated pattern presentation**. Rather than learners searching corpora for patterns, AI proactively generates contextually relevant examples, corrections, or alternatives in real-time conversational exchanges. This shift from **learner-initiated queries to system-initiated presentations** represents a fundamental reconceptualization of DDL: 

- **In traditional DDL**: Learners decide *what* to search for, *when* to query the corpus, and *how* to interpret concordance results. The corpus remains passive; learner agency drives the discovery process.
  
- **In AI-assisted DDL**: The system decides *when* to intervene, *what* patterns to present, and *how* to frame linguistic information. AI actively shapes the learning trajectory through real-time responsiveness.

This transformation addresses traditional DDL's cognitive overload and technical barriers (Bernardini, 2004; Crosthwaite, 2023) by providing **scaffolded, contextualized pattern engagement** rather than requiring learners to independently navigate large corpora. However, it also introduces critical pedagogical questions: When AI presents patterns without learner queries, does this bypass inductive discovery? When AI generates novel text rather than retrieving corpus examples, does this violate DDL's evidence-based foundation? Most importantly, ***how* can AI-mediated pattern presentation be *dynamically* adapted** to provide appropriate scaffolding—supportive without over-determining, generative without overwhelming—across different learning contexts and learner needs?

### 2. Scaffolding Theory and L2 Creative Writing: The Need for Adaptive Support

Scaffolding, originally conceptualized by Wood, Bruner, and Ross (1976), describes temporary support structures that enable learners to accomplish tasks beyond their independent capability, gradually fading as competence develops. In L2 writing contexts, effective scaffolding must balance multiple dimensions: **linguistic support** (vocabulary, grammar, discourse features), **cognitive support** (organizational strategies, ideation techniques), and **affective support** (encouragement, confidence-building, emotional safety) (Lantolf & Thorne, 2006; Van de Pol, Volman, & Beishuizen, 2010).

Creative writing in L2 contexts presents unique scaffolding challenges. Unlike academic or transactional writing where conventions are relatively stable, creative writing demands both **pattern adherence** (mastery of poetic forms, literary devices, genre conventions) and **pattern transcendence** (original expression, personal voice, aesthetic innovation). This dual requirement creates what Hanauer (2010) terms the **imitation-transformation dialectic**: learners must internalize exemplars while simultaneously developing authentic creative agency. Traditional scaffolding approaches often struggle with this tension—too much structure risks formulaic output and diminished authorship; too little risks cognitive overload and linguistic breakdown (Fithriani, 2021; Kerbs, McQueston, & Lawrance, 2024).

Moreover, L2 creative writing pedagogy faces persistent practical constraints: **limited access to diverse exemplars** that reflect learners' cultural and linguistic backgrounds; **insufficient individualized feedback** given instructor time limitations and large class sizes; and **constrained exploration opportunities** when learners fear making errors or expressing vulnerable content (Hanauer, 2010). These challenges create pedagogical gaps that AI technologies might potentially address—provided we understand how to configure such systems to provide appropriate scaffolding rather than undermining creative agency.

### 3. A Three-Interaction-Types Framework: How Parameter Configuration Shapes DDL-Scaffolding Modes

To understand ***how* AI-mediated DDL operates *dynamically*** in creative writing contexts, we propose a **three-interaction-types framework** that integrates DDL principles, scaffolding theory, and human-AI collaboration research. Recent studies provide empirical foundations: Coenen et al. (2022) identified **serendipitous discovery** as crucial for productive human-AI collaboration; Qian et al. (2023) demonstrated AI's capacity to redistribute cognitive load; Li (2025) found that generative AI shifts writers toward strategic collaboration. However, these studies treat AI as monolithic rather than examining ***how* different AI configurations produce distinct interaction patterns** with different pedagogical affordances.

Our framework addresses this gap by revealing the mechanism through which AI can *dynamically* adapt scaffolding: **parameter configuration** (specifically temperature and top-p settings) systematically shapes interaction type distributions. Lower parameter values (e.g., temperature 0.3, top-p 0.4) produce deterministic, corpus-typical outputs aligned with training data patterns; higher values (e.g., temperature 0.8, top-p 0.9) generate variable, exploratory outputs extending beyond corpus frequencies (Holtzman et al., 2019; Li et al., 2025; Peeperkorn et al., 2024). This technical mechanism enables pedagogical adaptivity: parameter manipulation functions as a design lever for shifting between different DDL-scaffolding modes.

We theorize three interaction types as **parameter-dependent DDL-scaffolding modes**, each serving distinct pedagogical functions:

#### 3.1 Type A (Constraint Repair): Pattern-Focused DDL as High-Directive Scaffolding

**Type A interactions** occur when AI identifies deviations from linguistic or structural patterns and provides corrective guidance. This parallels traditional DDL's use of concordance lines to establish grammatical rules or collocation patterns, but occurs **proactively and contextually** rather than through learner-initiated corpus queries. Aligned with Lyster and Ranta's (1997) corrective feedback taxonomy, Type A functions as a diagnostic tool that surfaces areas requiring attention, enabling focused revision.

In DDL terms, Type A represents **normative pattern reinforcement**: AI draws on corpus-derived knowledge to guide learners toward conventional usage—functioning as **high-frequency pattern reinforcement** similar to concordance-based DDL but delivered proactively. This is particularly valuable for **form-focused instruction** in creative writing—helping learners master syllable counts in haiku, rhyme schemes in sonnets, or grammatical accuracy in free verse.

**Parameter Effect on Type A**: Low parameter values (structured settings: temperature 0.3, top-p 0.4) maximize Type A frequency by constraining AI outputs to corpus-typical patterns, emphasizing error detection and normative correction. This provides **heavy scaffolding** through constraint-focused feedback but may stifle creative risk-taking (Ferris, 2004; Bitchener & Ferris, 2012).

**Scaffolding Characteristics**: Type A is **high-directive** (AI determines what needs fixing) and **low-autonomy** (learner response is corrective rather than generative). This supports form accuracy but may create dependency on external correction rather than developing internal monitoring capabilities.

#### 3.2 Type B (Exemplar Giving): Model-Based DDL as Moderate-Directive Scaffolding

**Type B interactions** occur when AI provides model texts, phrase options, or line alternatives that learners can select and adapt. This aligns with Hanauer's (2010) **imitation-transformation pedagogy** and resonates with **genre pedagogy** approaches (Hyland, 2007) and text-modeling practices (Tardy, 2006) in L2 writing. Type B embodies DDL's exemplar principle: learners encounter language patterns—in this case, AI-generated exemplars—and appropriate features for their own purposes.

The pedagogical appeal of Type B is substantial: it **reduces cognitive load** by providing concrete starting points, offers **diverse stylistic models** that learners might not encounter in limited classroom resources, and enables **safe experimentation** where learners can compare options before committing. However, Type B also introduces a critical tension. Unlike traditional DDL where learners actively search and select from large corpora, AI's Type B interactions present **pre-selected, constrained option sets** that fundamentally alter the learning dynamic from active exploration to guided selection.

**Parameter Effect on Type B**: Low parameter values (structured settings) also increase Type B frequency by generating conventional, corpus-typical exemplars. When combined with Type A dominance, this creates what we term the **"helpful but alienating" paradox**—AI provides immediately useful support (high accessibility) while diminishing authorship perception (low agency). Learners may select from AI-generated options rather than generating language themselves, bypassing the transformation process central to DDL pedagogy.

**Scaffolding Characteristics**: Type B involves **moderate directiveness** (AI provides options but learner chooses) and **moderate autonomy** (learner makes decisions within constrained sets). This supports creative accessibility but risks passive selection over active creation, potentially undermining the creative agency that makes poetry writing pedagogically valuable for L2 development.

#### 3.3 Type C (Surprise Harvest): Exploratory DDL as Low-Directive Scaffolding

**Type C interactions** occur when AI generates unexpected content—ideas, metaphors, framings, or directions—that learners had not considered and would not have discovered through conventional corpus consultation. This aligns with Coenen et al.'s (2022) **serendipitous discovery** concept in human-AI co-creativity and resonates with theories of **divergent thinking** (Guilford, 1967) and the role of novelty in creative processes (Boden, 2004).

Type C represents a fundamental departure from traditional DDL: rather than revealing patterns *within* corpus data, AI generates possibilities *beyond* corpus frequencies through **pattern extension and creative divergence**. This unique capability emerges when LLMs recombine learned patterns in novel ways. For L2 creative writers, Type C offers transformative potential: unexpected suggestions can **overcome lexical fixedness**, **challenge cultural or linguistic assumptions**, **expand creative search spaces**, and **provide entry points into more sophisticated expression** (Shneiderman, 2007).

**Parameter Effect on Type C**: High parameter values (exploratory settings: temperature 0.8, top-p 0.9) dramatically increase Type C frequency by enabling corpus-divergent generation that extends beyond training data frequencies. This parameter manipulation enables AI to function not as pattern-reinforcer (Type A) or pattern-provider (Type B) but as **pattern-extender**—a role impossible in static corpus DDL. Preliminary findings suggest **7× higher Type C frequency** in exploratory conditions (35% vs. 5%), fundamentally transforming the creative collaboration dynamic.

**Scaffolding Characteristics**: Type C is **low-directive** (AI proposes but doesn't prescribe) and **high-autonomy** (learner determines how/whether to incorporate suggestions). This provides **light scaffolding** supporting creative expansion and critical judgment, but demands higher metacognitive capacity to assess relevance and fit. Surprise can be productive (inspiring breakthrough insights) or disruptive (confusing learners), with effectiveness potentially depending on learner readiness and proficiency levels.

### 4. Implications for Adaptive DDL Scaffolding in L2 Creative Writing

The integration of interaction types and parameter effects reveals ***how* AI enables *dynamic* scaffolding adaptation** in ways traditional DDL cannot. Effective scaffolding requires **contingency** (adjusting support based on learner performance), **fading** (gradually reducing support as competence develops), and **transfer of responsibility** (shifting control from expert to learner) (Van de Pol et al., 2010). Traditional DDL assumes learners will self-scaffold through query refinement; AI enables **system-initiated scaffolding that adapts through parameter manipulation**.

The scaffolding literature emphasizes that **optimal support varies by learner proficiency, task demands, and learning phase** (Wood et al., 1976; Puntambekar & Hübscher, 2005). Parameter configuration addresses this requirement by functioning as a pedagogical design variable:

**Structured Parameters (Low Temperature/Top-p) → Heavy Scaffolding**
- Predominantly Type A + Type B interactions
- Supports form accuracy and provides accessible exemplars
- Reduces cognitive load for novice writers or complex tasks
- Risks: Over-scaffolding may diminish authorship and creative agency

**Exploratory Parameters (High Temperature/Top-p) → Light Scaffolding**  
- Higher Type C frequency with pattern-extending divergence
- Supports creative expansion and critical evaluation skills
- Demands higher metacognitive capacity and learner readiness
- Benefits: Preserves agency and enables serendipitous discovery

This parameter-interaction relationship has profound implications: **parameter configuration shapes whether AI functions as corrective tutor (Type A), exemplar provider (Type B), or creative collaborator (Type C)**, directly impacting learner agency, creative satisfaction, and the inductive discovery processes central to DDL pedagogy. Unlike commercial AI tools with fixed, hidden parameters, **parameter awareness and manipulation enable adaptive DDL scaffolding** tailored to pedagogical contexts.

### 5. The Present Study: Investigating *How* Parameter Manipulation Enables *Dynamic* DDL Scaffolding

Returning to Crosthwaite's (2023) challenge about generative AI and DDL's future, existing research has established *that* AI can support L2 creative writing but has not investigated ***how* AI can *dynamically* adapt scaffolding intensity** through systematic configuration manipulation. This "how" and "dynamic" gap is critical: if parameter settings determine interaction type distributions, then controlled parameter manipulation should enable **adaptive DDL scaffolding** that shifts between normative correction (Type A), curated exemplars (Type B), and exploratory divergence (Type C) depending on pedagogical goals.

**The Methodological Innovation: A Prompt-Designed Chatbot Platform**

To address this gap, we designed and deployed a **specialized poetry writing platform** featuring a prompt-engineered chatbot that operationalizes DDL-scaffolding theory through controlled parameter manipulation. Unlike commercial AI tools (e.g., ChatGPT, Claude) where parameters remain hidden and fixed, our platform enables:

1. **Systematic parameter control**: Four experimental conditions with precisely configured temperature/top-p settings
2. **Interaction pattern documentation**: Complete chat logs capturing turn-by-turn human-AI exchanges
3. **Theoretical grounding**: Unified base prompt designed to support all three interaction types while allowing parameter-driven scaffolding variation
4. **Real-time adaptivity**: AI responses shaped by parameter settings to provide differential scaffolding intensities

This methodological approach constitutes the **significance of this study**: by building a research infrastructure that makes parameter effects visible and recordable, we provide the first empirical examination of ***how* parameter configuration dynamically shapes the pedagogical nature of AI-assisted L2 creative writing**. Our findings demonstrate whether and how educators can leverage parameter settings as design levers for adaptive DDL scaffolding.

We employ a 2×2 factorial design crossing **Parameter Configuration** (Structured: 0.3/0.4 vs. Exploratory: 0.8/0.9) with **Awareness Condition** (Aware vs. Unaware of parameter settings) to examine both direct parameter effects and metacognitive influences of parameter literacy.

Our research is guided by three questions:

**RQ1: How do different parameter configurations affect the distribution of interaction types (Constraint Repair, Exemplar Giving, Surprise Harvest) in AI-assisted L2 poetry writing?**

We hypothesize that low-temperature settings will generate predominantly Type A and Type B interactions (pattern reinforcement and exemplar provision), while high-temperature settings will enable significantly higher Type C frequency (exploratory divergence). This prediction derives from temperature's technical function: lower values constrain outputs to corpus-typical patterns, while higher values increase generative variability.

**RQ2: How do these interaction types influence L2 learners' authorship perception, creative satisfaction, and sense of agency in collaborative poetry writing?**

We hypothesize that Type C presence will strongly predict higher authorship perception and creative satisfaction, while Type B dominance will correlate with diminished authorship despite high perceived helpfulness. This paradox—**helpful but alienating scaffolding**—reflects the tension between accessibility and agency documented in scaffolding research (Wood et al., 1976; Van de Pol et al., 2010).

**RQ3: What are the pedagogical implications of parameter configuration as a design lever for adaptive DDL in L2 creative writing?**

This question explores whether parameter manipulation can serve as a mechanism for **adaptive scaffolding**—adjusting AI behavior to match task phases, learner proficiency, and pedagogical goals. We investigate whether awareness of parameter effects enables learners to develop **AI literacy** and make informed decisions about when different scaffolding types serve their learning needs.

### 6. Bridging DDL, Scaffolding, and AI-Assisted Creative Writing

This study contributes to three intersecting research domains:

**For DDL research**: We extend data-driven learning principles from static corpus consultation to **dynamic, generative AI interaction**, examining ***how* AI-mediated engagement with linguistic patterns differs from traditional concordance-based approaches**. We address Crosthwaite's (2023) concern that generative AI might bypass inductive learning by investigating **which parameter configurations preserve learner agency in pattern discovery versus which promote passive consumption**. Our prompt-designed platform provides the methodological infrastructure to trace these dynamics empirically.

**For scaffolding research**: We operationalize scaffolding through **interaction type distribution**, demonstrating ***how* adaptive support emerges from parameter manipulation** rather than remaining fixed. We contribute evidence on the **scaffolding-autonomy trade-off** in creative contexts, examining when different support levels enhance versus constrain learning outcomes. Our chatbot platform enables systematic investigation of scaffolding contingency, fading, and autonomy transfer through recordable interaction patterns.

**For AI-assisted writing research**: We demonstrate that **parameter configuration constitutes pedagogical design**, not merely technical implementation. By revealing ***how* temperature settings systematically shape interaction patterns**, we establish parameter literacy as essential competence for educators integrating AI tools into L2 creative writing instruction. Our platform's complete interaction logging provides unprecedented visibility into the mechanisms through which parameter choices determine pedagogical affordances.

The integration of these three domains enables us to ask fundamental questions about the future of technology-mediated language learning: **Can AI provide the pattern-based induction of DDL, the adaptive support of effective scaffolding, and the creative inspiration necessary for authentic literary expression—simultaneously and appropriately?** Or do inherent tensions among these goals require careful calibration, deliberate trade-offs, and perhaps reconceptualization of what "successful" AI-assisted creative writing entails?

The preliminary findings from our Session 1 data (10 participants) suggest that these questions have empirical answers with significant pedagogical implications—answers we now turn to explore through systematic analysis of interaction patterns, learner perceptions, and creative outcomes in our AI-assisted L2 poetry writing study.

---

## References

Bitchener, J., & Ferris, D. R. (2012). *Written corrective feedback in second language acquisition and writing*. Routledge.

Boden, M. A. (2004). *The creative mind: Myths and mechanisms*. Routledge.

Boulton, A. (2012). Data-driven learning: Taking the computer out of the equation. *Language Learning*, *62*(2), 534-572.

Chakrabarty, T., Padmakumar, V., & He, H. (2022). Help me write a poem: Instruction tuning as a vehicle for collaborative poetry writing. *arXiv preprint arXiv:2210.13669*. https://doi.org/10.48550/arXiv.2210.13669

Coenen, A., Retelny, D., Wu, J., Michaux, J., Narayanan, A., Dang, H., Kua, T., Qian, H., Nham, K., Ma, F., & Agrawala, M. (2022). Wordcraft: Story writing with large language models. In *IUI '22: 27th International Conference on Intelligent User Interfaces Companion* (pp. 841-843). Association for Computing Machinery. https://doi.org/10.1145/3490100.3516505

Crosthwaite, P. (2023). Generative AI and the end of corpus-assisted data-driven learning? Not so fast! *Applied Corpus Linguistics*, *3*(3), 100[]()067.

Ferris, D. R. (2004). The "grammar correction" debate in L2 writing: Where are we, and where do we go from here? *Journal of Second Language Writing*, *13*(1), 49-62.

Fithriani, R. (2021). Poetry writing in EFL classrooms: Learning from Indonesian students' strategies. *KnE Social Sciences*.

Guilford, J. P. (1967). *The nature of human intelligence*. McGraw-Hill.

Hanauer, D. I. (2010). *Poetry as research: Exploring second language poetry writing*. John Benjamins Publishing Company.

Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2019). The curious case of neural text degeneration. *arXiv preprint arXiv:1904.09751*. https://doi.org/10.48550/arXiv:1904.09751

Hyland, K. (2007). Genre pedagogy: Language, literacy and L2 writing instruction. *Journal of Second Language Writing*, *16*(3), 148-164.

Johns, T. (1991). Should you be persuaded: Two examples of data-driven learning. *Classroom Concordancing Newsletter*, *4*, 1-16.

Kerbs, M., McQueston, J., & Lawrance, L. (2024). Playing with words: Scaffolding writing through poetry. *Reading Teacher*, *78*(1).

Lantolf, J. P., & Thorne, S. L. (2006). *Sociocultural theory and the genesis of second language development*. Oxford University Press.

Li, L., Wei, Y., Xu, M., Xiao, M., He, X., Liu, W., & Liang, S. (2025). Exploring the impact of temperature on large language models: Hot or cold? *Procedia Computer Science*, *264*, 242-251. https://doi.org/10.1016/j.procs.2024.10.130

Li, M. (2025). Generative artificial intelligence in second language writing: A comprehensive review of current research. *Language Teaching*, 1-29. https://doi.org/10.1017/S0261444824000424

Lyster, R., & Ranta, L. (1997). Corrective feedback and learner uptake: Negotiation of form in communicative classrooms. *Studies in Second Language Acquisition*, *19*(1), 37-66. https://doi.org/10.1017/S0272263197001034

Peeperkorn, M., Bewersdorff, A., & Zhai, X. (2024). Is temperature the creativity parameter of large language models? *arXiv preprint arXiv:2405.00492*. https://doi.org/10.48550/arXiv.2405.00492

Puntambekar, S., & Hübscher, R. (2005). Tools for scaffolding students in a complex learning environment. *Computers & Education*, *45*(2), 141-162.

Qian, W., Ma, J., Fox, R., Zhang, B., Liaw, R., Krishna, K., & Laban, P. (2023). "It felt like having a second mind": Investigating human-AI co-creativity in prewriting with large language models. *arXiv preprint arXiv:2307.10811*. https://doi.org/10.48550/arXiv.2307.10811

Shneiderman, B. (2007). Creativity support tools: Accelerating discovery and innovation. *Communications of the ACM*, *50*(12), 20-32.

Sun, Y. C., & Wang, L. Y. (2003). Concordancers in the EFL classroom: Cognitive approaches and collocation difficulty. *Computer Assisted Language Learning*, *16*(1), 83-94.

Tardy, C. M. (2006). Researching first and second language genre learning: A comparative review and a look ahead. *Journal of Second Language Writing*, *15*(2), 79-101.

Van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher–student interaction: A decade of research. *Educational Psychology Review*, *22*(3), 271-296.

Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, *17*(2), 89-100.
