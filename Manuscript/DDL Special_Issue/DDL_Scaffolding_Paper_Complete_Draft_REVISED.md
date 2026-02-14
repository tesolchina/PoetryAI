# From Static to Dynamic: Parameter Manipulation as Adaptive DDL Scaffolding in L2 Creative Writing with Generative AI

## Abstract

Does generative AI represent the death of Data-Driven Learning, or its evolution? This study addresses Crosthwaite's (2023) fundamental challenge by investigating how AI parameter configuration may shape learning outcomes in L2 creative writing. Through a 2×2 experimental design with preliminary data (N=10, target N=20), we manipulated temperature and top-p settings (structured: 0.3/0.4 vs. exploratory: 0.8/0.9) and parameter awareness (aware vs. unaware) while Hong Kong university students composed poetry with AI assistance. Preliminary findings suggest that parameter configuration appears to function as a pedagogical lever producing notably different interaction patterns: exploratory parameters generated approximately 7× more Type C "surprise harvest" interactions than structured parameters (35% vs. 5%, p<.001), potentially impacting authorship perception and creative satisfaction. Notably, 75% of participants rated Type B "exemplar giving" as most helpful, yet Type B frequency showed a negative association with authorship perception (r=-.58), which may reflect the "helpful but alienating" paradox of over-scaffolding. Our exploratory findings indicate that parameter configuration may determine whether AI functions as pattern-enforcer potentially undermining creative agency or pattern-extender enabling corpus-divergent discovery. This research tentatively establishes parameter literacy as potentially essential professional competence for educators, with implications that DDL's future may hinge not solely on AI's capabilities but also on educators' capacity to configure it as adaptive pedagogical scaffold. This small-scale study suggests that when educators gain control over temperature and top-p settings, AI may transform from potential threat into collaborative partner in DDL's evolution in the generative era.

**Key Words:** Data-Driven Learning; LLM parameter; Adaptive scaffolding; L2 Creative writing

---

## 1. Introduction

### 1.1 Answering Crosthwaite (2023): Evolution, Not Replacement

Crosthwaite (2023) poses a question that has sent ripples of concern through the language teaching community: Does generative AI spell "the death of DDL" by allowing learners to bypass the very inductive pattern discovery processes that have defined Data-Driven Learning pedagogy for over three decades? Rather than accepting this grim prognosis, this paper argues for a more nuanced perspective—**generative AI may represent an evolution rather than replacement of DDL principles**, though this outcome depends critically on how educators understand, configure, and deploy such tools. We examine this proposition through the lens of AI-assisted L2 creative writing, a context where the tensions between DDL's core values and generative AI's affordances become particularly visible and consequential. Unlike discrete grammar or vocabulary tasks where corpus patterns offer clear guidance, creative writing demands that learners **discover generative possibilities** within linguistic constraints—a process that generative AI can either support through adaptive scaffolding or undermine through over-determination. Understanding ***how* AI enables *dynamic* DDL scaffolding** in creative contexts requires examining the fundamental differences between traditional corpus consultation and AI-mediated pattern engagement, and identifying the mechanisms through which AI's pedagogical affordances can be systematically shaped.

#### 1.1.1 Reconceptualizing DDL for the 21st Century: From Keyword Matching to Data-Driven Pattern Learning

Data-Driven Learning (DDL), pioneered by Johns (1991) as "the use of concordance data in language learning," has long championed inductive pattern discovery over deductive rule presentation. By engaging learners directly with corpus evidence—concordance lines, frequency distributions, collocational patterns—DDL transforms language pedagogy from teacher-transmitted knowledge to learner-discovered insights (Boulton, 2012). The pedagogical power of DDL lies in its emphasis on **learner autonomy** and **evidence-based discovery**—principles that align closely with constructivist learning theory and sociocultural approaches to second language acquisition (Lantolf & Thorne, 2006).

Yet to answer whether AI-assisted creative writing truly constitutes DDL, we must first challenge outdated conceptions of DDL as merely "keyword matching" or "concordance consultation"—relics of late 20th-century corpus linguistics. At its heart, **DDL represents data-driven decision making in language learning**: making pedagogical choices grounded in patterns observed within language data. Traditional DDL accomplished this through explicit corpus queries and concordance searches—a relatively low-tech approach where learners typed keywords and examined frequency lists. Contemporary large language models achieve the same fundamental goal through radically different means: **data-driven pattern recognition and application** powered by machine learning and neural network architectures that process billions of language examples. The underlying logic of DDL—making language learning decisions based on patterns found in language data—remains constant, even as the mechanisms shift from explicit corpus consultation to implicit pattern learning through neural network training.

#### 1.1.2 Does AI-Assisted Poetry Writing Count as DDL? Establishing Legitimacy

This question is critical for establishing our study's legitimacy within the DDL framework. **We argue yes, for the following reasons:**

**Data-driven foundation**: Large language models are trained on massive language corpora—often hundreds of billions of words—learning patterns through machine learning and neural networks that identify regularities in how language actually works. When AI generates a poetic line or suggests an alternative phrasing, it applies these learned patterns, making the process inherently **data-driven** even though it occurs through neural network inference rather than the explicit corpus queries familiar from traditional DDL.

**Pattern-based generation**: AI generates text by recognizing and applying the linguistic patterns it absorbed during training. Where traditional DDL presents patterns by displaying *existing* corpus examples through concordance lines ("Here are 50 instances of 'make' + noun"), AI-assisted DDL **generates new text that instantiates those same patterns** ("You could write 'make a promise' or 'make amends'"). This shift from pattern retrieval to pattern generation represents a fundamental technological evolution, but both approaches rely on the same corpus-derived knowledge to inform language learning.

**Student input + AI pattern application**: The collaborative poetry writing process combines student decisions (input about theme, emotion, style, form) with AI's pattern-based text generation. Students exercise agency in conceptual and creative dimensions while AI provides pattern-informed linguistic scaffolding—paralleling how traditional DDL learners formulate queries (student agency) and receive pattern-based evidence (corpus data).

**Pedagogical control through parameter configuration**: Crucially, parameter settings (temperature, top-p) provide a mechanism for adjusting how AI applies learned patterns—enabling pedagogical control over the data-driven process. This configurability transforms AI from a black-box text generator into an adjustable DDL scaffold whose pattern presentation can be systematically shaped.

**Core principle maintained**: Both traditional DDL and AI-assisted DDL are fundamentally data-driven, but use different technological mechanisms. The difference lies not in the principle (pattern-based learning from language data), but in the mechanism (explicit corpus queries versus implicit pattern application through neural network inference).

#### 1.1.3 Traditional DDL vs. AI-Assisted DDL: From Learner-Initiated Queries to System-Initiated Pattern Presentation

Traditional DDL positions learners as active **query initiators** who must formulate search criteria, execute corpus queries, and interpret concordance results—often dense pages of decontextualized sentence fragments (Johns, 1991). This learner-driven approach, while admirably fostering autonomy, imposes considerable cognitive demands: sufficient metalinguistic awareness to know *what* to search for, technical competence to navigate corpus interfaces, and the patience to tolerate data ambiguity and information overload (Sun & Wang, 2003). Moreover, corpus data by its very nature represents **patterns of what has been written**—frozen snapshots of past language use—not necessarily what *could* be written, a limitation that becomes especially constraining in creative writing where novelty, surprise, and originality are pedagogical goals rather than deviations to be corrected.

Generative AI fundamentally transforms this dynamic by enabling **system-initiated pattern presentation**. Rather than learners laboriously searching corpora for patterns, AI proactively generates contextually relevant examples, corrections, or creative alternatives through real-time conversational exchanges that feel more like dialogue than database consultation. This "pattern presentation" occurs through actual text generation—AI creates poetry lines, phrases, or corrections that instantiate linguistic patterns, making them visible to learners through the creative writing process itself. This shift from **learner-initiated queries to system-initiated presentations** represents a fundamental reconceptualization of DDL:

- **In traditional DDL**: Learners decide *what* to search for, *when* to query the corpus, and *how* to interpret concordance results. The corpus remains passive; learner agency drives the discovery process.
  
- **In AI-assisted DDL**: The system decides *when* to intervene, *what* patterns to present (through generated text outputs), and *how* to frame linguistic information. AI actively shapes the learning trajectory through real-time responsiveness.

This transformation addresses traditional DDL's cognitive overload and technical barriers (Bernardini, 2004; Crosthwaite, 2023) by providing **scaffolded, contextualized pattern engagement** rather than requiring learners to independently navigate large corpora. However, it also introduces critical pedagogical questions: When AI presents patterns without learner queries, does this bypass inductive discovery? When AI generates novel text rather than retrieving corpus examples, does this violate DDL's evidence-based foundation? Most importantly, ***how* can AI-mediated pattern presentation be *dynamically* adapted** to provide appropriate scaffolding—supportive without over-determining, generative without overwhelming—across different learning contexts and learner needs?

### 1.2 The Poetry Writing Process and L2 Creative Writing Scaffolding Challenges

#### 1.2.1 Understanding the Poetry Writing Process: From Ideation to Text

Traditional poetry writing involves a holistic process where writers move from ideation and emotional expression through theme selection, word choice, text generation, and revision. For pedagogical purposes, this process can be conceptually divided into distinct but interconnected phases:

**1. Ideation & Emotion**: The writer has ideas, feelings, or experiences to express
**2. Theme/Topic Selection**: Choosing specific theme, context, or subject matter
**3. Word Selection**: Selecting appropriate words and expressions
**4. Text Generation**: Creating actual text in poetic form
**5. Revision/Editing**: Polishing and refining the poem

For L2 learners, this multifaceted process presents unique challenges. We can distinguish between **decision-making** (prewriting choices about theme, topic, emotions to express, poetic form, style, and length) and **execution/implementation** (the actual transformation of ideas into written text). While experienced poets integrate these phases seamlessly, L2 learners often struggle disproportionately with the execution phase despite having clear ideas and emotional content to express.

#### 1.2.2 The "Eye-High, Hand-Low" Problem in L2 Creative Writing

L2 creative writing pedagogy faces a persistent and often frustrating challenge that we term the **"eye-high, hand-low" problem** (眼高手低), borrowing from a Chinese idiom describing those whose critical vision exceeds their practical ability: learners often possess rich ideas, emotions, and creative vision—they know what they want to say, they can recognize good poetry when they see it, they have aesthetic awareness ("eye-high")—but they lack the linguistic proficiency and text generation skills necessary to transform these intentions into actual written poetry ("hand-low"). This painful gap between creative intention and linguistic execution creates a barrier that stops many learners from engaging in poetry writing at all, despite having genuine motivation, meaningful content to express, and sophisticated conceptual understanding.

The problem manifests concretely in moments of creative paralysis: students can choose evocative themes, emotionally resonant topics, and appropriate poetic forms (the decision-making they excel at), but they **cannot execute** the actual writing—they cannot find the precise English words they need, cannot construct grammatically accurate lines that also sound poetic, cannot achieve the sonic or rhythmic effects they can hear in their minds but cannot produce on the page. While aesthetic awareness can be developed relatively quickly through exposure and discussion, linguistic execution requires extensive practice that many learners cannot access precisely because the execution barrier prevents them from engaging in that practice. This creates a pedagogical impasse.

#### 1.2.3 How AI Addresses the "Eye-High, Hand-Low" Problem

Our study addresses this problem by positioning large language models as **AI tutors or co-pilots** that can bridge the gap between creative intention and linguistic execution at precisely the moment when learners need help most. In our approach, learners can express their ideas, emotions, and creative choices—the themes they care about, the topics they want to explore, the forms they find appealing, the style and mood they envision—using whatever language feels most natural, even their L1. The AI then assists in generating an initial draft in English, transforming those expressed intentions into actual poetic text. This intervention occurs at the critical juncture where many learners previously hit an insurmountable wall and either gave up or never started, thereby enabling learning opportunities that traditional approaches leave inaccessible.

Critically, this approach preserves—rather than eliminates—the pedagogical division between decision-making (which remains squarely with the learner) and execution (where AI provides pattern-based scaffolding). Students continue to exercise genuine creative agency in determining *what* they want to express, *why* it matters to them, and *how* they want to frame it conceptually and emotionally. Meanwhile, AI provides linguistic support for transforming those creative intentions into actual English text that instantiates their vision while introducing them to language patterns they can learn from and eventually internalize. This maintains the creative and cognitive engagement essential for learning while removing the execution barrier that traditionally prevented many L2 learners from accessing poetry writing as a developmental activity.

#### 1.2.4 The Need for Adaptive Support: Scaffolding Theory and Creative Agency

Creative writing in L2 contexts presents unique scaffolding challenges, and importantly, **L2 poetry writing has distinctive pedagogical goals** that differ significantly from teaching poetry as a literature course. While literature courses emphasize **originality, meaning, and personal voice** as primary outcomes, **L2 poetry pedagogy emphasizes language development through engagement with sound patterns, lexical choices, grammatical structures, and linguistic expressivity** (Hanauer, 2010; Lao & Krashen, 2000). In L2 contexts, poetry serves as a vehicle for developing phonological awareness, collocation sensitivity, and syntactic flexibility—dimensions that align closely with Data-Driven Learning's emphasis on pattern discovery. This pedagogical distinction is crucial: AI scaffolding effective for developing linguistic pattern sensitivity may differ from scaffolding designed to cultivate personal artistic voice.

Both approaches, however, demand addressing what Hanauer (2010) terms the **imitation-transformation dialectic**: learners must internalize exemplars while simultaneously developing authentic creative agency. Traditional scaffolding approaches often struggle with this tension—too much structure risks formulaic output and diminished authorship; too little risks cognitive overload and linguistic breakdown (Fithriani, 2021; Kerbs, McQueston, & Lawrance, 2024). Moreover, L2 poetry pedagogy faces persistent practical constraints: **limited access to diverse exemplars** reflecting learners' cultural and linguistic backgrounds; **insufficient individualized feedback** on language use patterns; and **constrained exploration opportunities** when learners fear grammatical errors or uncertain expression. These challenges create pedagogical gaps that AI technologies might potentially address—provided we understand how to configure such systems to provide appropriate scaffolding rather than undermining the dual goals of linguistic development and authentic creative agency.

[Remainder of the paper continues as in original draft...]

---

**Note**: This revised introduction incorporates:
- More descriptive and natural language throughout
- Explicit DDL legitimacy argument with concrete examples
- Detailed explanation of the poetry writing process
- Clear articulation of the "eye-high, hand-low" problem
- More vivid and emotionally resonant descriptions
- Concrete examples throughout (e.g., concordance line examples)
- More engaging academic prose while maintaining scholarly rigor
