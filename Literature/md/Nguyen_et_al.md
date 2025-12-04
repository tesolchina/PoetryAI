---
source_pdf: Nguyen et al..pdf
converted_date: 2025-12-04T19:59:00.380492
total_pages: 19
model: Google Gemini 2.0 Flash
total_cost_usd: $0.004845
prompt_tokens: 15,687
completion_tokens: 8,192
---

Studies in Higher Education
ISSN: 0307-5079 (Print) 1470-174X (Online) Journal homepage: www.tandfonline.com/journals/cshe20
Human-AI collaboration patterns in AI-assisted academic writing
Andy Nguyen, Yvonne Hong, Belle Dang & Xiaoshan Huang
To cite this article: Andy Nguyen, Yvonne Hong, Belle Dang & Xiaoshan Huang (2024) Human-
AI collaboration patterns in AI-assisted academic writing, Studies in Higher Education, 49:5,
847-864, DOI: 10.1080/03075079.2024.2323593
To link to this article: https://doi.org/10.1080/03075079.2024.2323593
© 2024 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
Published online: 28 Feb 2024.
Submit your article to this journal
Article views: 42043
View related articles
View Crossmark data
Citing articles: 108 View citing articles
Full Terms & Conditions of access and use can be found at https://www.tandfonline.com/action/journalInformation?journalCode=cshe20

STUDIES IN HIGHER EDUCATION
2024, VOL. 49, NO. 5, 847–864 https://doi.org/10.1080/03075079.2024.2323593
Human-AI collaboration patterns in AI-assisted academic writing
Andy Nguyen a, Yvonne Hong b, Belle Dang a and Xiaoshan Huangc aLearning and Educational Technology (LET) Research Lab, University of Oulu, Oulu, Finland; bSchool of Information
Management, Victoria University of Wellington, Wellington, New Zealand; cDepartment of Educational and
Counselling Psychology (ECP), McGill University, Montreal, Canada
ABSTRACT ARTICLE HISTORY
Artificial Intelligence (AI) has increasingly influenced higher education, Received 2 October 2023 notably in academic writing where AI-powered assisting tools offer both Accepted 21 February 2024
opportunities and challenges. Recently, the rapid growth of generative
AI (GAI) has brought its impacts into sharper focus, yet the dynamics of KEYWORDS
Higher education; artificial its utilisation in academic writing remain largely unexplored. This paper
intelligence (AI); doctoral focuses on examining the nature of human-AI interactions in academic
studies; academic writing; writing, specifically investigating the strategies doctoral students self-regulated learning
employ when collaborating with a GAI-powered assisting tool. This study involves 626 recorded activities on how ten doctoral students
interact with GAI-powered assisting tool during academic writing. AIdriven learning analytics approach was adopted for three layered
analyses: (1) data pre-processing and analysis with quantitative content analysis, (2) sequence analysis with Hidden Markov Model (HMM) and
hierarchical sequence clustering, and (3) pattern analysis with process mining. Findings indicate that doctoral students engaging in iterative,
highly interactive processes with the GAI-powered assisting tool generally achieve better performance in the writing task. In contrast,
those who use GAI merely as a supplementary information source, maintaining a linear writing approach, tend to get lower writing
performance. This study points to the need for further investigations into human-AI collaboration in learning in higher education, with
implications for tailored educational strategies and solutions.
Introduction
Given the rapid evolution of technology and its infusion into various sectors of life, it is difficult to ignore its undeniable impact on educational paradigms (Ashour 2020; Buhl-Wiggers, Kjærgaard,
and Munk 2023). Academic writing, a fundamental skill across educational systems, has experienced significant transformation due to these technological innovations. In fact, academic writing has been
influenced by the emergence of various digital tools designed to assist scholars in their research, writing, and composition processes (Schcolnik 2018; Strobl et al. 2019). These tools, ranging from
digital libraries and online collaboration platforms to specialised writing software, have transformed how academic writing is produced and disseminated (Strobl et al. 2019).
Although technology-assisted writing or intelligent writing assistants are not new concepts (e.g.
O’Neill & Russell 2019; Zhang et al. 2016), the recent advancements in artificial intelligence (AI), particularly in the domain of natural language processing (NLP), mark a significant evolution in this field.
CONTACT Andy Nguyen Andy.Nguyen@oulu.fi University of Oulu (Oulun yliopisto), Pentti Kaiteran katu 1, 90570 Oulu,
Finland
© 2024 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited. The terms on which this
article has been published allow the posting of the Accepted Manuscript in a repository by the author(s) or with their consent.

848 A. NGUYEN ET AL.
Deep learning models, a subset of machine learning, have shown immense promise in understanding and generating human-like text, which has a considerable impact on academic writing (Yan
2023). OpenAI’s GPT (Generative Pretrained Transformer) series is a prime example of such advancements. The ChatGPT variant, in particular, offers a spectrum of capabilities, from responding to
queries to content generation (Dwivedi et al. 2023). Although the potential of these technological breakthroughs has been shown to enhance learning experiences, nurture creativity, and streamline
knowledge management, there are growing concerns about their implications for academic integrity and the possible erosion of academic writing skills (Kasneci et al. 2023; Lund et al. 2023).
The integration of state-of-the-art AI-assisted writing assistants into the academic writing process represents a paradigm shift. These tools not only provide assistance in drafting and revising text but
also in conducting literature reviews and synthesising information, which are critical components of scholarly writing. However, this convenience comes with its own set of challenges. The ease of gen-
erating coherent and sophisticated text using AI can potentially lead to over-reliance, raising questions about the originality and authenticity of scholarly work. Furthermore, the use of AI in academic
writing necessitates a reevaluation of pedagogical approaches to ensure that students develop critical thinking and analytical skills, rather than merely relying on AI for content generation.
The importance of academic writing proficiency has always been a consistent requirement, especially for doctoral students, and focus of discussion in higher education research, predating
the widespread use of generative AI (Caffarella and Barnett 2000). Doctoral students, engaged in the pursuit of advanced research, must possess the capability to effectively communicate their
research findings. This involves not only the clear articulation of these findings but also the synthesis of existing literature and the generation of new insights. The ability to write academically is not
merely a functional skill but a critical component of a doctoral student’s intellectual toolkit, enabling them to contribute meaningfully to their respective fields.. With the emergence of technological
advancements like generative AI, there are potential unknown effects on the quality and integrity of doctoral students’ academic writing, raising both opportunities and challenges (Dwivedi et al.
2023; Kishore et al. 2023). While AI, particularly in its generative form, does not possess the ability to fully synthesise literature or independently engage in critical writing, it has shown considerable
proficiency in aiding these processes. Specifically, generative AI can assist by aggregating and summarising relevant literature and generating written content based on specific prompts. This capa-
bility, however, is supplementary in nature; it serves to support and streamline the initial stages of academic writing, such as literature review and ideation, rather than replace the nuanced, critical
thinking and analytical skills required for comprehensive synthesis and critical writing. These latter skills remain distinctly within the human domain, necessitating a depth of understanding and intel-
lectual engagement that AI has yet to replicate. Furthermore, unlike other technological innovations, generative AI possesses the unique ability to respond according to previous engagements between
the AI mechanism and its human counterparts. Accordingly, assessing how academic writing processes are shaped in human-AI collaboration is becoming increasingly essential.
In light of the pressing importance of understanding human-AI collaboration in academic contexts (Järvelä, Nguyen, and Hadwin 2023), this paper investigates the dynamics between doctoral
students and AI-assisted writing tools in their academic writing tasks. This research diverges from the conventional approach of assessing the direct impact of GAI-powered assistants on academic
writing, such as whether they enhance or impair writing quality. Instead, it concentrates on revealing the patterns of human-AI interaction within academic writing. The study’s focus is to discern which
strategies are most effective in the context of GAI-assisted academic writing, thereby understanding how these practices can be optimised. We provide a thorough, process-oriented examination based
on screen recordings from these writing sessions, aiming to examine the role and implications of
GAI-assisted writing tools. In particular, this study aims to assess doctoral students’ regulation of academic writing processes when engaged in human-AI collaboration, particularly with ChatGPT,
through the following research questions:

STUDIES IN HIGHER EDUCATION 849
. RQ1. What are the strategies and patterns doctoral students employ in their academic writing processes when collaborating with GAI-assisted writing tools?
o RQ1a) What are the key hidden states in GAI-assisted academic writing?
o RQ1b) What are the predominant patterns in GAI-assisted academic writing?
. RQ2. How is the effectiveness of each identified strategic pattern in GAI-assisted academic writing characterised by its specific nature and underlying attributes?
The following sections of this paper provide a literature review of the cognitive process of writing and ChatGPT in academic writing. We then present the applied methods, followed by a detailed
analysis of our findings. We conclude with a discussion of the implications of our study for the fields of academic writing and AIED and suggest directions for future research. By investigating
the intersection of AI and academic writing, we hope to shed light on a critical area of AIED research, contributing valuable insights to the discourse surrounding AI’s role in self-regulated academic
writing.
Theoretical foundations
Writing as a complex cognitive activity
Writing is a complex activity (Graham 2018), encompassing the navigation of language rules, communication norms, and the transition from the writer’s to the reader’s perspective. Specifically, it
demands intense cognitive effort (Piolat, Olive, and Kellogg 2005) for tasks such as expressing ideas, maintaining logical flow and structure, and reorganising content to suit the given context.
Moreover, writing processes share the working memory capacity (McCutchen 1996; 2000), and if the cognitive load surpasses this capacity, these processes can be hindered (Sweller 1994).
Hence, the writer’s objective is to minimise the demands on working memory, facilitating smooth processing and interactions among writing processes within working memory. According to Flower
& Hayes’ framework (1981), shown in Figure 1, writing processes encompass planning, translating,
Figure 1. The cognitive process of writing (Flowers and Hayes 1981).

850 A. NGUYEN ET AL.
and reviewing, all of which are influenced by the writer’s working memory capacity and the task environment. An efficient writer is capable of enhancing their performance (Kellogg 2008), necessi-
tating deliberate effort and control over the activity. However, the constraints imposed by the limitations of working memory capacity significantly impact writing processes.
Regulation and coordination of writing
As a result, there is an adaptive shift in the regulation and coordination of these processes, tailored to meet specific task requirements and enhance the fluidity of composition. Efficient regulation of the
writing processes is central to producing good-quality texts (Beauvais, Olive, and Passerault 2011).
For example, proficient writers, often considered good regulators, can coordinate their writing processes by transitioning from sequential to more concurrent methods, mitigating the risk of overload-
ing the working memory capacity (Olive 2014).
To be more specific, these skilled writers exhibit a higher level of executive control over the flow and transition of information across various cognitive and linguistic resources in a timely manner.
This heightened executive control not only facilitates seamless flow and smooth information transitions but also paves the way for harnessing the potential of advanced technologies like AI.
Through the automation and streamlining of lower-level processes in academic writing, AI can effectively release cognitive resources, allowing writers to dedicate more attention to higher-order
aspects of composition, such as content organisation, argument development, and creative expression. This collaborative partnership between skilled writers and AI exemplifies the evolving
landscape of writing, where technology serves as a supportive tool, ultimately enhancing the overall efficiency and quality of the writing process.
AI-assisted academic writing
The integration of AI technologies in academic writing has been a subject of increasing interest within the academic community. The initial phase of this integration, marked by the use of AI-
driven applications such as grammar and style checkers to enhance the quality of written work, has been well-documented (Graesser et al. 2004). The landscape of AI assistance in academic
writing has evolved significantly with recent advancements in natural language processing (NLP).
These developments have given rise to a new generation of sophisticated AI-driven tools that offer extensive support in various facets of the writing process (Yan 2023). Notably, the advent of
generative AI (GAI) technology, incorporating large language models (LLMs) like GPT-3 and GPT-4, has expanded the capabilities of AI in academic writing to include content generation, summarisa-
tion, feedback provision, and offering suggestions for improvements (Radford et al. 2021). These tools, when strategically employed, can assist writers throughout the entire writing process, from
idea generation and outlining to drafting and revising manuscripts (Enriquez et al. 2023).
The effectiveness of these generative AI tools in supporting learners from diverse cultural backgrounds has also been a subject of research (Kasneci et al. 2023). These tools have been found to aid
in overcoming language and style-related challenges in complex academic writing, facilitating translation, vocabulary selection, sentence structuring, and adherence to scholarly tone, thereby enhan-
cing the speed and clarity of the writing process (Dwivedi et al. 2023; Radford et al. 2021). In academic discourse, where critical analysis and the formulation of counterarguments are crucial,
generative AI tools have shown potential in alleviating writer’s block, enhancing creativity, and improving the overall coherence and quality of academic texts (Yan 2023).
Despite these advancements, the ethical implications of employing generative AI in academic writing necessitate careful consideration to promote responsible use of this technology (Nguyen
et al. 2023). Moreover, there is a notable research gap in the study of human-AI collaboration dynamics in academic writing. Current research is still nascent and primarily focuses on the capabilities and
immediate effects of generative AI tools (Gašević et al. 2023; Kishore et al. 2023). There is a critical

STUDIES IN HIGHER EDUCATION 851 need for in-depth investigations into how human writers interact with these AI-driven writing assist-
ants. Such research is essential to fully understand the complexities of incorporating generative AI tools in academic settings. This understanding will be instrumental in developing strategies that
ensure the responsible and effective use of AI in supporting self-regulated academic writing practices.
Research methods
By applying process mining techniques to the analysis of human-AI collaboration in an academic writing task, this study seeks to provide a novel perspective on the dynamics of this interaction
and offer insights into potential improvements and challenges associated with AI-assisted writing.
The writing task and the unrestricted use of tools aim to provide an ecologically valid context for exploring the dynamics of human-AI collaboration in academic writing.
Participants and procedures
The participants in this study consisted of ten doctoral students (N = 10) from Finland and New
Zealand enrolled in an English doctoral program in either Information Systems or Learning and Educational Technology. As the study aims to examine how ChatGPT is used as an AI-driven writing
assistant, focusing on this particular population was intentional. Doctoral students were selected as a particularly relevant population for the study due to their familiarity with academic writing.
The data collected from these students can provide valuable insights into the dynamics of human-AI collaboration in the context of advanced academic writing, where high standards and
complex ideas are expected.
The study employed an online experimental design conducted via the Zoom video conferencing platform. The experiment was structured around a writing task requiring participants to compose a
short essay of approximately 500 words on artificial intelligence (AI) use in education. Participants were instructed to convey their opinions, supporting their arguments with evidence and examples.
Ensuring that the task was representative of the types of writing tasks participants would encounter in their academic pursuits, the task design and rubric were kept closely similar to those used in
typical university writing assignments.
Participants were given 30 min to complete the writing task, during which they were allowed to use any tools deemed necessary, including ChatGPT and Google Scholar. The unrestricted access to
tools was intended to mimic real-life writing situations and to investigate the extent to which participants chose to utilise AI-driven writing assistants during the task. During the experiment, screen
recording was employed to capture participants’ interactions with the writing task and the various tools they chose to use. The Zoom session was recorded, providing a comprehensive view of partici-
pants’ behaviour and tools used during the writing task. A pre-survey questionnaire was initially conducted at the start of each session to collect information about participants’ backgrounds. All
identifying information was removed from the recordings and survey responses to ensure data privacy and participant anonymity. The assessment of the final product of the writing task was con-
ducted by a university lecturer immediately following the data collection phase, prior to engaging in any sequential analysis or process mining. This procedural decision was strategically made to mini-
mise the potential for biases in the performance assessment, while simultaneously mirroring the conventional evaluation practices prevalent in the higher education context.
Data analysis
The study’s primary aim is to understand the dynamic interactions between doctoral students and
ChatGPT, especially the strategic patterns and their effectiveness in academic writing tasks. In order to capture the complexities of these human-AI collaborative processes, we employ an AI-driven
learning analytics approach (Järvelä, Nguyen, and Hadwin 2023; Ouyang, Xu, and Cukurova 2023)

852 A. NGUYEN ET AL.
that allows for the computational extraction and interpretation of rich behavioural data during writing sessions, thereby enabling the identification of recurring strategies and patterns.
In particular, the analytical framework for this study is informed by the artificial intelligence-driven learning analytics method proposed by Ouyang, Xu, and Cukurova (2023), which adopts the complex
adaptive systems perspective. This analytical approach involves three layers: (1) data pre-processing and analysis, (2) multi-channel sequence analysis, and (3) pattern analysis. In the first layer, quanti-
tative content analysis was conducted to code the writing behaviour associated with the micro-processes undertaken by students. In the second layer, Hidden Markov Model (HMM) and sequence
clustering were utilised to identify and categorise the underlying patterns exhibited by doctoral students in their writing processes with ChatGPT. Finally, process mining techniques are applied in the
third layer to further examine the identified patterns.
This study’s choice of the HMM, sequence clustering and process mining methods is grounded in theoretical relevance and empirical rigour. The HMM is particularly suitable for modelling sequential
processes that involve a certain degree of uncertainty, as is the case with human-AI interactions in academic writing. HMMs are adept at capturing latent states that cannot be directly observed but
influence observable variables. In the context of this study, these latent states may include cognitive processes like planning, revising, and editing, which are not directly visible but impact the final
written output. By employing HMM, we can more accurately model the hidden cognitive states that govern the visible interactions between doctoral students and ChatGPT. Sequence clustering
and process mining, on the other hand, offer a complementary approach. While HMM provides insights into individual latent states and transitions, Sequence Clustering groups similar sequences
of actions allowing us to identify common patterns or strategies employed across different students.
Process Mining enriches this by providing the temporal aspect, showing what strategies are employed and how they evolve over an academic writing session.
Writing performance scoring
A structured marking rubric (Appendix A) mirroring typical higher education academic evaluation norms was instituted to appraise doctoral compositions enhanced by GAI-powered tools. This
rubric comprises five key criteria: content, analysis, organisation and structure, quality of writing, and word Limit and referencing. Content, with a 30% weightage, critically assesses the student’s
clarity and depth in understanding AI’s role in education. Analysis, also weighted at 30%, critically examines the rigour and relevance of the evidence in discussing AI’s educational implications.
Organisation and structure, accounting for 15%, examine the logical flow and coherence of the essay. Quality of writing, another 15%, scrutinises grammatical precision and stylistic suitability for
a scholarly audience. Finally, word limit and referencing, weighted at 10%, check adherence to specified word counts and accuracy in APA referencing.
Quantitative content analysis
The screen recording with audio data was coded to document the temporal pattern of student writing tactics when employing ChatGPT. To characterise the writing behaviour associated with
the micro-processes undertaken by students, we conducted a qualitative content analysis utilising the constant comparison approach as delineated by Onwuegbuzie et al. (2009). In the initial open
coding phase, each student action associated with the writing process received a descriptor, highlighting a facet of the writing procedure. Subsequently, the research team distilled these descriptors
into broader categories and formulated overarching themes that encapsulated the essence of individual or cluster codes. In total, 626 events were coded. Table 1describes our code scheme for micro-
level processes in AI-assisted writing.
Hidden Markov model
We utilised the Hidden Markov Model (HMM) to capture the dynamic alterations in doctoral students’ management of their writing processes while collaboratively working with the AI tool,

STUDIES IN HIGHER EDUCATION 853
Table 1. Micro-processes in AI-assisted writing.
Code Description
AddReference Integrating scholarly citations and references into the essay
CheckWordCount Verifying the essay’s word count
CopyArticleContent Copy content from articles
CopyContent Copy content from the essay, either original or revised
CopyGeneratedContent Copy content generated by ChatGPT
CopyGeneratedReference Copy reference generated by ChatGPT
CopyParaphrasedContent Copy content that is already paraphrased in the grammar-checking tool
CopyTaskRequirements Copy the task rubric or questions
DeletePreviouslyPastedGeneratedContent Deleted Content Generated by ChatGPT that was previously pasted in the essay
EditContent Revising, restructuring, and formatting existing content, whether generated, copied, or original
EditOutline Adjust, modify, and refine the outline of the essay
EditPrompt Adjust, modify, refine the previous prompt in ChatGPT
EditSearch Adjust, modify, refine the previous search keyword
PasteToEssay Paste copied content to the essay
PasteToGrammarTool Paste copied content to the grammar-checking tool
PasteToPrompt Paste copied content to ChatGPT for prompting
PasteToWord Paste copied content to Word
PromptContent Prompt ChatGPT for content (i.e. write something, answer the question that provides content text to be used, etc.)
PromptCorrection Prompt ChatGPT to correct grammar in text
PromptFeedback Prompt ChatGPT to provide feedback on the writing
PromptFollowUp Prompt ChatGPT for content that builds upon the context established by preceding prompts.
PromptOutline Prompt ChatGPT for the outline of the required writing task
PromptReference Prompt ChatGPT to provide reference
ReadArticleContent Read, review the content in the article
ReadArticleReference Read, review the article for reference or just reference
ReadEssay Read, review current content in the essay
ReadGeneratedContent Read, review content generated by ChatGPT
ReadGeneratedReference Read, review reference generated by ChatGPT
ReadTaskRequirements Read, review the task requirement or rubric
SearchArticle Search articles in browser
SearchArticleReference Search reference in browser
SearchContent Search (definition, meaning) of words, concepts, etc.
SetPromptContext Provide context for ChatGPT before prompting it for content
TypeBrainstorm Type own ideas for the writing task
TypeContent Type own text that is be part of the final writing
TypeNote Type own notes of the read content, articles, information
TypeOutline Type ideas for writing but with the structure that serves as outline
ChatGPT. The HMM, an extension of the basic Markov chain, provides insights into the probabilities of sequences composed of specific random variables or states (Eddy 2004). Hidden Markov Model
(HMM) techniques have been frequently used in various studies within the field of learning sciences to scrutinise how learning processes unfold (Dang et al. 2023; Malmberg et al. 2021). In this study, we
focus on understanding how doctoral students adjusted their writing strategies when working with
AI assistants. Using HMM helps us model hidden cognitive activities like planning or editing, which, although not directly seen, affect the final written product and the interactions between doctoral
students and the GAI-powered tool. The Akaike Information Criterion (AIC) and Bayesian Information
Criterion (BIC) metrics were applied to selecting the optimal number of states.
Sequence clustering & process mining
To examine the main patterns of AI-assisted writing, we employed Agglomerative Hierarchical Clustering (AHC) (Bouguettaya et al. 2015), leveraging the Python programming language in conjunction
with the scikit-learn library. AHC is an unsupervised machine learning technique aiming to discern the dataset’s structure, pinpoint inherent patterns, and classify data points into clusters. The Silhou-
ette Coefficient was initially computed to assess the quality of cluster assignments. In our study,

854 A. NGUYEN ET AL.
sequences representing the hidden states associated with writing tactics for a cohort of 10 students were integrated into a clustering framework. We explored a range of cluster quantities (from 2 to 10)
and evaluated each using its corresponding silhouette score. Our analysis indicated that a twocluster model was the most appropriate, achieving an optimal fit with a silhouette score of 0.372.
The agglomerative coefficient, which reflects the tightness of clustering, was 0.77.
In order to describe the patterns of doctoral students’ regulation of writing processes in human-AI collaboration with ChatGPT, we employed a process-mining technique to the coded actions. Specifi-
cally, our analysis was rooted in the Fuzzy Miner approach, as detailed by Günther and van der Aalst
(2007), and utilised Fluxicon’s Disco analysis software, a recognised tool in process mining. Notably, this software has been previously employed in research to examine learning event processes, as evi-
denced by works (e.g. Dindar, Järvelä, and Haataja 2020).
Results and findings
RQ1. What are the strategies and patterns doctoral students employ in their academic writing processes when collaborating with GAI-assisted writing tools
RQ1a) What are the key hidden states in GAI-assisted academic writing? Hidden Markov model results
Based on the fitting scores, where the lowest values for BIC are preferred (see Table 2), our HMM model identified 3 hidden states in the sequence of writing tactics students employ while interacting
with ChatGPT. The data were then fitted to a three-state model – below is the transition matrix and are plotted against States with probability < 0.05 (as shown in Table 3).
The characteristics of each state are described as follows:
. State 1: This state captures 14.6% of the total data on writing tactics and predominantly features activities connected to pasting – such as PasteToEssay, PasteToPrompt, PasteToWord, and Paste-
ToGrammarTool – which collectively represent 82.6% of actions within this state. Accordingly, this state is labelled as Content Pasting behaviour.
. State 2: This state occupies 14.5% of the data on writing tactics and is primarily composed of copying-related activities. Actions such as CopyArticleContent, CopyContent, CopyGenerated-
Content, CopyParaphrasedContent, and CopyTaskRequirement contribute to 97.8% of this state’s activities. Thus, it is best described as Content Copying behaviour.
. State 3: This state encompasses 70.8% of the writing tactics data. Unlike the other two states, this one presents a broader range of writing tactics. These activities include, but are not limited to,
AddReference, TypeContent, EditContent, PromptContent, and PromptFollowUp. Accordingly, this state is most accurately described as Component Shaping behaviour.
Among the HMM results, a regular cyclical transition pattern was observed between the Content
Copying (State 2) and Content Pasting (State 1), as well as between Content Pasting (State 1) and
Table 2. HMM model fit statistics.
States BIC AIC
2 4235.582 3902.631
3 4307.197 3792.232
4 4392.266 3686.409
5 4575.573 3669.946
6 4778.668 3664.391
7 5050.715 3718.91
8 5257.462 3699.25
9 5542.043 3748.546
10 5845.877 3808.215

STUDIES IN HIGHER EDUCATION 855
Table 3. HMM transition matrix.
From State 1 State 2 State 3
State 1 0 0.26839 0.73161
State 2 0.95819 0.04181 0
State 3 0 0.17146 0.82854
Component Shaping (State 3), as visualised in Figures 2 and 3. Figure 2 explains the hidden states with probabilities whereas Figure 3 visualises the HMM paths. Additionally, State 3, associated
with Component Shaping behaviour, was characterised by less frequent but extended periods of activity. In contrast, States 1 and 2 – Content Pasting and Content Copying, respectively – were
marked by brief and sequentially adjacent occurrences. This sequential patterning aligns with the anticipated behaviour of copy-pasting. However, its frequency and distribution are different for
some students compared to others.
RQ1b) What are the predominant patterns in GAI-assisted academic writing?
Following the HMM analysis, Agglomerative Hierarchical Clustering (AHC) was applied to the sequences of hidden states for 10 students’ writing tactics. The optimal clustering yielded two distinct
writing strategy types: Type 1 with 5 sequences and Type 2 with 5 sequences, as shown in Figure 4.
The process-mining analysis results reveal significant differences between Type 1 (Structured
Adaptivity) and Type 2 (Unstructured Streamlinece) regarding the writing tactics pathways they went through. Figures 5 and 6 present the pathway of the writing tactics in the process maps for
Type 1 and Type 2, with the most dominant process flow among those activities. The maps show the absolute frequencies and case coverages in the percentage of the number of activities and
the connection among them.
In Type 1, individuals exhibited a higher familiarity and multifaceted engagement strategy with
ChatGPT. After reviewing the task requirements, these high achievers often start by prompting
ChatGPT for content while searching for articles (f = 40%). This indicates a
PromptContent → SearchArticle preference for multitasking and reading content to stimulate their thought rather than just
waiting for GPT to finish generating its responses, thereby maximising productivity. A typical
Figure 2. HMM graphs of the transitional structures between states.

856 A. NGUYEN ET AL.
Figure 3. Most probable HMM paths of the hidden states.
sequence of actions in this type involves reading generated content → copying such content → pasting it to the essay then → either directly editing it or typing their content. This demonstrated
a reflective and effective approach to processing and applying the generated material before integrating it into their final output. Their use of ChatGPT was characterised by more sophisticated oper-
ations with more PromptFollowUp (f = 21; f = 9) and EditPrompt (f = 5, f = 2)
Type 1 Type 2 Type 1 Type 2 compared to their counterparts in Type 2.
On the other hand, the students in Type 2 display a less refined interaction strategy with the GAIpowered tool. After reviewing task guidelines, they commonly insert these requirements into their
essays, followed by TypeContent and TypeNotes. While this indicates the process of pre-thought
(analysis of the task requirement to define objectives), prolonged engagement in this phase could negatively impact productivity, especially within the time constraints of the current task. When
they use the GAI-powered tool, the procedure is usually linear: prompt for content → copy the generated text → and paste it into their essay. This hints at a lack of critical assessment of the GAI-gen-
erated content’s relevance or accuracy. For some such actions are succeeded by more TypeContent and then DeletePreviouslyPastedGeneratedContent (fType 2 = 8, fType 1 = 0), suggesting that the
GAI-powered tool’s output serves mainly as a springboard for their own writing rather than as final text. Overall, their interactions with the GAI-powered tool reflect unexamined adoption or a
supplemental note-taking approach that may not contribute to the final draft.
RQ2. How is the effectiveness of each identified strategic pattern in GAI-assisted academic writing characterised by its specific nature and underlying attributes?
Regarding the final performance of the students’ writing, the data’s normality was first verified using a Shapiro–Wilk test, which indicated a normally distributed performance measure (W = 0.91534, p >

STUDIES IN HIGHER EDUCATION 857
Figure 4. Index plots depicting the hidden states characteristics for the two cluster types.
0.05). A t-test was conducted to compare the mean performance scores between the two clusters.
The analysis revealed a significant difference between Type 1’s and Type 2’s performance (t =
2.4011, df = 6.0267, p ≤ 0.05). Table 4 shows the summary of different descriptive statistics across two types.
The descriptive statistics in Table 4 can be interpreted as follows: Students in cluster Type 1 demonstrated a higher average performance score (M = 79.75, SD = 20.64) than Type 2 (M = 54.75,
SD = 10.77). Although both types expressed comparable confidence levels regarding digital skills
(M = 4.40), they diverged in their assessments of task difficulty and interest, which also changed after the task. Overall, Type 1 was correlated with higher performance and higher usage of the
GAI-powered tool, while Type 2 was associated with lower performance with limited use and
Table 4. Summary of different criteria across two types.
Type 1 – Structured Type 2 Unstructured
Adaptivity Streamline
Students’ performance score and perception of: M SD M SD
Performance Score 79.75 20.64 54.7 10.77
Pre-Task Difficulty 4.40 1.67 4.40 2.60
Post-Task Difficulty 4.40 1.51 3.40 2.88
Digital Skills 5.20 0.45