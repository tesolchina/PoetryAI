---
source_pdf: Zhao_2025_Assessing_LLM_Creativity.pdf
converted_date: 2025-12-04T20:36:02.731038
total_pages: 20
model: Google Gemini 2.0 Flash
total_cost_usd: $0.006039
prompt_tokens: 27,623
completion_tokens: 8,192
---

Machine Intelligence Research 22(3), June 2025, 417-436 www.mi-research.net DOI: 10.1007/s11633-025-1546-4
Assessing and Understanding Creativity in
Large Language Models
Yunpu Zhao 1,2 Rui Zhang 2 Wenyi Li 3 Ling Li 3
1 Department of Computer Science, University of Science and Technology of China, Hefei 230026, China
2 State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences, Beijing 100190, China
3 Institute of Software, University of Chinese Academy of Sciences, Beijing 100190, China
Abstract: In the field of natural language processing, the rapid development of large language model (LLM) has attracted increasing
attention. LLMs have shown a high level of creativity in various tasks, but the methods for assessing such creativity are inadequate. Assessment of LLM creativity needs to consider differences from humans, requiring multiple dimensional measurement while balancing ac-
curacy and efficiency. This paper aims to establish an efficient framework for assessing the level of creativity in LLMs. By adapting the modified Torrance tests of creative thinking, the research evaluates the creative performance of various LLMs across 7 tasks, emphasiz-
ing 4 criteria including fluency, flexibility, originality, and elaboration. In this context, we develop a comprehensive dataset of 700 questions for testing and an LLM-based evaluation method. In addition, this study presents a novel analysis of LLMs′ responses to diverse
prompts and role-play situations. We found that the creativity of LLMs primarily falls short in originality, while excelling in elaboration.
In addition, the use of prompts and role-play settings of the model significantly influence creativity. Additionally, the experimental results also indicate that collaboration among multiple LLMs can enhance originality. Notably, our findings reveal a consensus between hu-
man evaluations and LLMs regarding the personality traits that influence creativity. The findings underscore the significant impact of
LLM design on creativity and bridge artificial intelligence and human creativity, offering insights into LLMs′ creativity and potential applications.
Keywords: Large language models (LLMs), creativity assessment, prompt engineering, cognitive psychology, divergent thinking.
Citation: Y. Zhao, R. Zhang, W. Li, L. Li. Assessing and understanding creativity in large language models. Machine Intelligence
Research, vol.22, no.3, pp.417–436, 2025. http://doi.org/10.1007/s11633-025-1546-4

# 1 Introduction
In recent years, the realm of artificial intelligence (AI) has witnessed a meteoric rise in the development and
sophistication of large language models (LLMs)[1, 2]. LLMs have significantly advanced in their capabilities in ad-
dressing a variety of conventional natural language processing tasks, such as reasoning and natural language un-
derstanding[3–6]. Moreover, LLMs also have demonstrated significant value in widespread applications. From trans-
forming rudimentary text into compelling narratives[7, 8], unlocking a new realm of storytelling, to solving complex
algorithmic problems[9], these models have shown a semblance of what could be interpreted as creativity. The
practical manifestations of this creativity have penetrated various sectors, including science research, where
they assist in idea generation and suggestion[6]; education, by providing personalized learning experiences[10]; and in
the entertainment industry, creating music and art[11, 12].
In many of their applications, LLMs seem to exhibit the ability to generate original text, aiding tasks related to
imagination and creativity, suggesting that they may indeed possess elements of creativity.
From the broad capabilities demonstrated by LLMs, the creativity they exhibit is a key reason they are con-
sidered powerful. However, behind the impressive abilities of LLMs lies a significant question that warrants care-
ful examination: Do these models actually possess real creativity, or is their apparent intelligence merely an illu-
sion – a complex imitation of human thinking created by their training paradigm? This question touches on the
very nature of LLM intelligence, which may not be easily explained. Since LLMs have shown considerable creativ-
ity, understanding the extent and characteristics of this creativity is essential. Gaining deeper insight into the cre-
ativity of LLMs can not only guide us in further improving their performance but also in enhancing our under-
standing of the nature of their creativity. This, in turn, informs our daily use and application of these models, un-
derscoring the need for an effective method to measure and assess their creativity. Specifically, creative abilities

Research Article
Manuscript received on August 24, 2024; accepted on January 15,
2025; published online on April 28, 2025
Recommended by Associate Editor Zhiyuan Liu
Colored figures are available in the online version at https://link.
springer.com/journal/11633
© The Author(s) 2025

418 Machine Intelligence Research 22(3), June 2025 are critical for the following application scenarios. First,
LLM can inspire humans on creative tasks and provide novel ideas, especially in research idea generation[13, 14]. It
has also been suggested that the use of LLM can also lead to homogenization of creativity[15]. Second, humor genera-
tion with LLMs offer significant value in both creative and practical applications. By simulating human-like hu-
mor, LLMs can assist in content creation for entertainment, marketing, and social media. Finally, LLMs can
serve as powerful cocreators in creative writings by generating narrative ideas, suggesting plot developments, or
even drafting sections of text that inspire further refinement by human writers.
Creativity, as a term, traditionally refers to the natural ability to think innovatively, to make unconventional
connections, and to devise solutions that are both novel and effective[16]. Assessing the creativity of LLMs is
fraught with challenges. First, the question of creativity does not have clear answers to refer to. When we ask an
LLM a question such as “what is the speed of light in vacuum in meters per second?”, the answer can be formally
vetted, given the objective nature of the topic. However, when posed with a prompt such as “what would be the
implications if animals could talk?”, the situation becomes different in this case because there is no definitive
answer and the answer is open and divergent, making it challenging to judge the correctness of the output[17]. Ad-
ditionally, since creativity encompasses various aspects, including originality and flexibility, it is necessary to
design diverse tasks and criteria to measure these qualities effectively in LLMs. In addition, there are differences
between LLMs and humans, which might lead to irrelevant responses or serious logical issues, requiring us to ad-
ditionally assess these aspects. Finally, evaluating creativity necessitates a delicate balance between accuracy and
efficiency, rendering traditional human-based evaluation methods less practical. Therefore, it is imperative to ad-
dress the challenges outlined above to make a robust and sound assessment of creativity in LLMs.
Recognizing the need for a comprehensive assessment of LLM′s creativity, we design an efficient framework to
automatically assess the creativity of LLMs by adapting and modifying the Torrance tests of creative thinking
(TTCT)[18], a widely recognized tool in psychometrics′ research for human creativity assessment. To enhance the
credibility of the results and reduce the randomness, seven verbal tasks, which use verbal stimuli, were selected.
We employed GPT-4, the most advanced LLM, to expand the question set for each task, thereby constructing
the testing dataset. To ensure a thorough and objective evaluation of creativity and capture creativity′s various
manifestations, we combine diverse tasks and criteria. We design a comprehensive test protocol incorporating four
criteria for measuring creativity: Fluency, flexibility, ori-

ginality, and elaboration. We let the LLMs answer questions from the constructed dataset, obtaining many ques-
tion-answer pairs. We utilized GPT-4 as an evaluator to assess each answer, as the GPT-4 is capable of effectively
assessing the openness of responses and identifying their shortcomings and errors. Under proper prompt engineer-
ing, GPT-4 can efficiently and effectively complete the evaluation of the entire dataset results. Thus, we can
achieve a balance between efficiency and accuracy in our assessment method.
We selected six popular LLMs as test subjects, each possessing different architectures and parameter scales. In
addition to the overall testing, we conducted some additional exploratory experiments that investigate the
changes of creativity levels exhibited by LLMs when given different types of prompts and different roles that
LLMs play. Then, we designed a collaboration mechanism for LLMs to explore the impact of multiple LLMs col-
laborating on creativity. Last, we also performed some psychological experiments related to personality traits on
the LLMs, including emotional intelligence (EI), empathy, the big five inventory (BFI) and self-efficacy. Be-
cause we found in relevant psychological research showing that human creativity is correlated with these person-
ality traits and we verified the consistency between LLMs and humans in this regard.
Our experiments and analysis yielded several conclusions. First, there are significant differences in creative
performance among different models, even among those of the same scale with an equal number of parameters. This
variation primarily exists between different types of models. Their differences are reflected mainly in the model ar-
chitecture, parameter settings during training, alignment strategies, and the datasets used for training. Addition-
ally, we observed that models generally excel in the elaboration metric, but tend to be less adept in demonstrat-
ing originality. In addition, the type of prompt and the specific role-play request given to the model also plays a
significant role in influencing its creative output. When the models are given instructive prompts or chain-of-
thought prompts, there is a significant increase in the level of creativity. Additionally, having LLM play differ-
ent roles leads to notable differences; the role of a scientist demonstrates the highest level of creativity. Many
roles even show a decrease compared to the default scenario, but there is generally an improvement in originality.
Then, collaboration among multiple LLMs can enhance the level of creativity, with the most notable improve-
ment in originality. Finally, the results of the psychological scale revealed consistency between LLMs and hu-
mans in terms of associated creativity factors, such as emotional intelligence (EI), empathy, self-efficacy, and
others.

Y. Zhao et al. / Assessing and Understanding Creativity in Large Language Models 419
# 2 Related works
## 2.1 Creativity assessment in psychological
research
The question of creativity assessment has been a prominent focus on the creativity research, especially
since the 1950s, marking the inception of a systematic study into individual differences in creativity[19]. For ex-
ample, Guilford pioneered the research on creativity and his famous structure of intellect model was mainly about
defining and analyzing the factors constituting intelligence, where creativity plays a major driving force in his
theory[20]. In recent years, many new developments regarding the measurement of divergent thinking, consensu-
al assessment technique and subjective ratings, and selfreport methodology[21–23] have emerged. Although ad-
vances in methodology and technology have led to important developments regarding creativity assessment,
some assessment methods have long been described as
“gold standard” for creativity assessment[24, 25]. Among them, TTCT[18] has been the most widely used and re-
searched test of creativity, having extensive data to support its reliability and validity. Research on TTCT re-
ports good reliability scores for scoring and test-retest reliability[26].
TTCT is designed to identify and assess an individual′s creative potential by exploring various dimen-
sions. Contrasting conventional assessments that emphasize convergent thinking, the test fosters divergent think-
ing, encouraging participants to generate multiple solutions to open-ended, ambiguous problems. TTCT has
been widely applied in educational settings, organizational assessments, demonstrating its versatility and compre-
hensive approach to measuring creativity. Its ability to tap into various facets of creative thinking has made
TTCT a reliable and respected tool[27]. Owing to the authority and comprehensiveness of the TTCT, we select
tasks from the TTCT to construct our dataset.

## 2.2 Creativity and personality: Findings in
psychological research
Research has revealed that creativity is not solely a fixed human personality trait. It evolves from a combina-
tion of individual processes such as cognitive, affective, behavioral, and contextual factors. Some psychologists
have conducted a detailed meta-analysis of papers exploring the relationship between creativity and various per-
sonality traits[28, 29].
These studies′ results highlight a correlation between creativity and a plethora of personal factors. Notably, ele-
ments such as emotional intelligence, divergent thinking, openness to experience, and intrinsic motivation stand
out as strong influencers. However, factors such as age,

intelligence, and gender exhibit a relatively milder association with creativity, signifying a varied spectrum of in-
fluence across different personal traits. Since large language models have exhibited some personality traits, we
conducted experiments to test whether these findings also hold true in LLMs.

## 2.3 Assessing the creativity of large lan-
guage models
The emergence of abilities from LLMs continually surpasses people′s expectations, and the evaluation of vari-
ous abilities of LLMs has received widespread attention[30]. Currently, most evaluations focus on the ability
of LLMs to solve tasks, with fewer evaluations combining aspects of psychology.
Although some studies have focused on the intersection of LLM with psychology and cognitive science[31],
work discussing the creativity of LLM is still in a relatively early stage. Current studies somewhat focused on
exploring the creativity of LLMs, primarily from the standpoint of creativity theory, which aims to elucidate
the definitions and challenges of applying creativity theory within the context of LLMs[32]. Some initial evalu-
ations of creativity in LLMs have also been undertaken[33–35]. However, these works only employed simple
tasks such as the alternative uses task (AUT) to assess creativity, and the lack of comparison between various
LLMs limits the validity of their conclusions. It is worth mentioning that in [36], the authors used the standard
TTCT to assess GPT-4′s creativity. The results show that GPT-4 achieved human top 1% levels in fluency and
originality, along with a high score in flexibility. This study leans more towards comparing advanced large lan-
guage models (LLMs) with human benchmarks. The original TTCT test protocol does not seamlessly adapt to
assessing creativity in LLMs, as the limited sample of questions could induce randomness and accidental out-
comes, making hypothesis testing challenging when comparing different models. Furthermore, expanding the
number of question sets leads to high time costs in human-based evaluations.
Due to the differences between humans and LLM, it is problematic to directly use the TTCT′s test protocol to
benchmark LLMs′ creativity. To address this dilemma, we propose a new framework for systematic analysis
LLM′s creativity. This framework comprises carefully crafted metrics used in TTCT and a dataset that ac-
counts for seven tasks. We will dive into detail of the framework in Section 3.

# 3 Overview of the framework
In this work, we design an overall framework to evaluate LLM′s creativity, as shown in Fig. 1. First, we con-
structed a dataset containing 700 questions of 7 tasks

420 Machine Intelligence Research 22(3), June 2025

Prompt type
Basic prompt
Common problems task. The scenario is:
Planning a birthday party for a 5-year-old.
Instructive prompt
Common problems task. There is no right or wrong answers, we're interested in how many
different problems you can identify and the potential solutions you can come up with. Try to
think of as many problems as possible 5-yearold's party. The scenario is: Planning a
birthday party for a 5-year-old.
Chain of thought (CoT) prompt
Common problems task. Let's think step by step.
The scenario is: Planning a birthday party for a
5-year-old.
Creative questions
Q: Please list unusual uses of plastic bottle.
Q: What would happen if we could time travel?
Situation task
Q: If the sun didn't rise tomorrow, how would you ensure you had enough light
during the day?
Role play
Student
Follow following question…
Scientist
Act like a typical natural scientist. Do following task or answer following question…
Artist
Act like a typical music artist. Do following task or answer following question…
···
7 tasks · 700 questions
Torrance® tests of creative thinking
Criteria
Fluency
The ability to produce a significant number of relevant ideas in response to a given
question. In essence, fluency measures the quantity of ideas.
Flexibility
The variety of categories from which one can generate ideas. It is the ability to think of alter-
natives, shift from one class or perspective to another, and to approach a given problem or
task from different angles.
Originality
The uniqueness of the ideas generated.
Original ideas are rare or unconventional, differing from the norm.
Elaboration
The ability to expand upon, refine, and embellish an idea. It involves adding details,
developing nuances, and building upon a basic concept to make it more intricate or
complex.
LLMs
GPT-3.5
Llama-2-13b
Llama-2-70b
Qwen
Vicuna-7b
Vicuna-13b
Judger: GPT-4 & human
···
Fig. 1 Overview of the creativity assessment framework. A TTCT-inspired dataset was constructed to evaluate LLMs under varied prompts and role-play settings. GPT-4 served as the evaluator to score model outputs.

that were derived and modified from the psychology scale of the TTCT and expanded the number of questions via
GPT-4. We tested six models on four different criteria using the dataset we constructed. Following this, we con-
ducted a series of experiments on the creativity of LLMs when giving different types of prompts and assigning dif-
ferent roles to LLMs. Finally, we used the GPT-4 as the evaluator to obtain the performance results of the LLMs
and verify the consistency of the LLM-based evaluation with humans.

## 3.1 Dataset construction
This research utilized a modified version of the TTCT verbal test, which includes tasks based on verbal stimuli.
The seven selected tasks: 1) Unusual uses, 2) consequences, 3) just suppose, 4) situations, 5) common
problems, 6) improvements, and 7) imaginative stories, were chosen to capture a broad spectrum of creative
thinking abilities. These tasks are adapted from the widely used TTCT, which has also served as the basis for
recent work in the field of LLM evaluation[37]. The tasks we choose align with widely accepted models of creativ-
ity such as Guilford′s structure of the intellect model and involve both divergent and convergent thinking[20]. Mean-
while, TTCT tasks, especially in their divergent thinking focus, align with the Geneplore model[38] by emphasizing
idea generation (fluency and originality) and flexibility
(the ability to shift between categories or approaches).
Thus, the tasks capture both novelty and usefulness, which are central to most modern definitions of creativ-
ity. This makes them sufficient for assessing a holistic view of creative potential.
Specifically, each task includes one hundred questions generated by GPT-4 using few-shot prompts. The seven
tasks were generally structured as follows:
1) Task 1: Unusual uses. This task challenges indi-
viduals in their ability to think of as many unusual and diverse uses as possible for a common object within a lim-
ited time frame. The object in question is typically everyday and familiar, such as a brick, paper clip, or newspa-
per.
2) Task 2: Consequences. This task focuses on the
ability to foresee consequences or outcomes of an unusual or hypothetical situation. For example, what would be
the implications if animals could talk?
3) Task 3: Just suppose. This task encourages ima-
ginative and speculative thinking by asking participants to consider hypothetical, often fantastical, scenarios and
their implications. For example, just suppose you woke up one morning and found you could fly. What would
you do? List as many things as you can think of.
4) Task 4: Situation task. This task is designed to
assess creative thinking by evaluating how individuals respond to and interpret a given situation. This task em-
phasizes understanding social dynamics, empathy, and the ability to consider multiple perspectives or solutions.
For example, if all books were to disappear, how would you gain knowledge?
5) Task 5: Common problem. This task focuses on
everyday problems that are familiar to most people, requiring participants to generate innovative and effective

Y. Zhao et al. / Assessing and Understanding Creativity in Large Language Models 421 solutions. For example, organizing a cross-country road
trip or building a tree house.
6) Task 6: Improvement. This task focuses on as-
sessing an individual′s ability to enhance or modify existing objects or ideas. The given object is similar to the un-
usual uses task.
7) Task 7: Imaginative stories. This task is de-
signed to assess creativity through narrative and storytelling with a given prompt. This task emphasizes
the ability to construct original, coherent, and imaginative stories, showcasing an individual′s creative potential
in terms of narrative ability. Examples of given prompts are “The Invisible Elephant” or “The Book that Wrote
Itself”.
Each task includes 100 questions generated by GPT-4 via few-shot prompts. GPT-4 can generate a diverse and
comprehensive set of similar problems based on the given examples, and all problems have been validated by hu-
mans to ensure usability. In addition, we conducted experimental validation of domain generality across differ-
ent tasks. Cronbach′s Alpha and inter-task correlations indicate that our task selection is effective and sufficient.

## 3.2 Evaluation criteria
To provide a comprehensive evaluation of an individual′s creative abilities, we should consider not only the
quantity of ideas they produce, but also the quality, diversity, and depth of those ideas. We have four criteria
for creativity evaluation:
1) Fluency. This refers to the ability to produce a
significant number of relevant ideas in response to a given question. In essence, fluency measures the quantity of
ideas.
2) Flexibility. This assesses the variety of categories
from which one can generate ideas. It is the ability to think of alternatives, shift from one class or perspective
to another, and to approach a given problem or task from different angles.
3) Originality. This measures the uniqueness of the
ideas generated. Original ideas are rare or unconventional, differing from the norm.
4) Elaboration. This refers to the ability to expand
upon, refine, and embellish an idea. It involves adding details, developing nuances, and building upon a basic
concept to make it more intricate or complex.
These criteria aim to provide a comprehensive assessment of an individual′s creative potential. The motiva-
tion behind using these specific dimensions is grounded in the theoretical and empirical research on creativity[39, 40],
which suggests that creative thinking involves not just the generation of new ideas but also the ability to manip-
ulate, refine, and apply these ideas effectively. The four criteria are based on long-standing psychological frame-
works for creativity assessment, particularly the TTCT.
These dimensions collectively capture distinct and com-

plementary facets of creative thinking and have been extensively validated in psychological and educational re-
search and are considered gold standards in creativity assessment.

## 3.3 LLM-based evaluation
Standard TTCT evaluation methods require trained psychologists to follow professional manuals to assess the
results, and an individual′s single test only contains answers to a very limited number of questions. When evalu-
ating creativity in LLM, both the insufficient sample of responses and the high human resource costs limit the ap-
plication of creativity tests on LLMs. Recent psychological research has focused on the automated assessment of
creativity[41, 42]. However, these methods often have limitations, such as being tailored to specific tasks or requir-
ing prepared reference answers, which prevent their generalization to a variety of tasks and a larger number of
questions.
With the rapid development of LLM capabilities, the evaluation methods for many natural language pro-
cessing tasks have evolved from traditional human annotation to reference-based automated methods, and now,
to methods on the basis of LLMs. LLMs are increasingly playing the role of judges in tasks such as question-an-
swering, translation, and text quality assessment[43–46], giving rise to various evaluation framework[47–49]. Accord-
ing to experimental results from relevant literature, LLM exhibits higher correlation with human evaluations com-
pared with traditional automated technologies[50, 51]. In this study, on the basis of the evaluation criteria from
Section 3.2, we utilize GPT-4 to score the answer. For each criterion, the LLM needs to complete the Likert
scale based on the responses. Additionally, we verified the consistency between the evaluations made by LLM and
human evaluations.

# 4 Evaluation and results
We conducted a statistical analysis of the creativity scores of 6 popular LLMs across seven tasks, totaling 700
questions. We unveiled hidden conclusions within the data results from various dimensions. We compared the
differences in creativity levels between the models, and we compared the performance variations under different
criteria within the same model. Subsequently, we experimented with many types of prompts to see whether
changes in prompts would affect the models′ levels of creativity. Since LLMs possess the ability to play user-spe-
cified roles, we select six typical human identities to explore the impact on creativity under different role-play-
ing conditions. Finally, we utilize some psychological scales to test the LLMs, investigating the correlation
between the personality traits of the LLMs and creativity.

422 Machine Intelligence Research 22(3), June 2025
## 4.1 Experimental settings
### 4.1.1 Tested models
We tested six of the most advanced LLMs, which are listed below. All the models were implemented with the
open-source repository HuggingFace[52].
1) GPT-3.5. GPT-3.5 is a language model de-
veloped by OpenAI, which is an advanced version of the
GPT-3 model. It is capable of generating natural language text and code. GPT-3.5 was trained on an Azure
AI supercomputing infrastructure. The versions we used in the experiments are GPT-3.5-turbo-0613.
2) LLaMA-2. LLaMA-2 is a family of state-of-the-
art open-access large language models released by Meta and Microsoft[2]. It is built upon success of its prede-
cessor, LLaMA-1. LLaMA-2 is specifically designed to facilitate the development of generative AI-powered tools
and experiences. It is available for free research and commercial use. LLaMA-2 release introduces a family of pre-
trained and fine-tuned LLMs, ranging in scale from 7 B to
70 B parameters. The versions we used in the experiments are LLaMA-2-13b-chat-hf and LLaMA-2-70b-chat-
hf.
3) Vicuna. Vicuna is a lightweight, accurate, and ef-
ficient language model developed by a team of researchers from several universities, including UC Berkeley,
Carnegie Mellon University, Stanford University, and UC
San Diego[44]. It was built from Meta′s adaptable LLaMA model, which was fine-tuned on a dataset of around 70 000
human-generated conversations from the ShareGPT website. The versions we used in the experiments are Vicuna-
7b-v1.5 and Vicuna-13b-v1.5.
4) Qwen. Qwen (abbr. Tongyi Qianwen), proposed
by Alibaba Cloud[53]. It is a transformer-based large language model, which is pretrained on a large volume of
data, including web texts, books, codes, etc. The versions we used in the experiments are Qwen-7b-chat.

### 4.1.2 Details of hyperparameters
The models used in our experiment primarily originate from the open-source HuggingFace platform. The spe-
cific versions of these models have already been reported above. In this section, we present the experimental para-
meters and other settings related to the experiment.
For an LLM based on the transformer architecture, there are certain parameters that directly affect the out-
put of the model.
1) Max tokens. This parameter controls the maxim-
um number of tokens to generate in the chat completion.
In our experiment, this value is uniformly set to 512, ensuring that the output length is sufficient to maintain the
quality of the answers.
2) Temperature. The parameter is a crucial factor
in determining the nature of the model′s responses. This is a hyperparameter that influences the randomness or
unpredictability in the model′s responses. Essentially, its mechanism is to change the probability distribution of

the model′s output logits. However, according to our experiments, changes in temperature do not significantly af-
fect creative performance, which appears quite random.
Therefore, in our experiments, the temperature is uniformly set to 1.
3) Top_p. Top_p is also a parameter used to control
the diversity of the generated text, also known as “nucleus sampling”. This parameter′s full name is “top probab-
ility”, which is typically represented by a value between 0 and 1, indicating the cumulative threshold of the highest
probabilities chosen in the probability distribution when generating the next token. In our experiments, top_p is
uniformly set to 1.
4) Top_k. This parameter is used when generating
the next token to limit the model to consider only the top_k tokens with the highest probability. This strategy
can reduce the likelihood of the model generating meaningless or repetitive outputs, while also improving the
speed and efficiency of the model generation. In our experiments, the top_k is uniformly set to 50.
GPT-4 serves as the judge for our LLM-based evaluation, with its relevant parameters set to default. The
version used is GPT-4-0613. In addition, all prompt templates used in the experiment are provided in the ap-
pendix.

## 4.2 Results of different models and criteria
We assessed the responses of six language models to
700 questions, with GPT-4 serving as the evaluator across all creativity dimensions. We first evaluate the average
score of each model across all tasks, as shown in Fig. 2(a) and Table 1. It can be observed that GPT-3.5 has the
highest level of creativity, followed by the LLaMA-2 architecture models, then the LLaMA-based fine-tuned
model vicuna, and finally Qwen. The experimental results from the perspective of the model suggest that the
type of model has a significant effect on creativity, whereas the scale of parameters does not have a decisive influ-
ence. Different types of models vary in their architectures, alignment strategies, and the datasets used during
training. These factors are likely to be key determinants of the level of creativity. Similar findings can also be ob-
served in other LLM evaluation papers[54–56]. For example, in Toolbench[56], the 30 B version of LLaMA out-
performs the 65 B version of LLaMA in many tasks, and text-daVinci-003 also performs better overall than GPT-
3.5.
To further validate the ranks of the models, we conducted pairwise comparisons between the models, as
shown in Fig. 2(b). Each cell in this heatmap represents the win rate of the model on the y-axis in terms of cre-
ativity score compared to the model on the x-axis. The win rate scores are consistent with the strengths and
weaknesses of the models shown in Fig. 2(a), and we conducted statistical tests for significance, which are marked

Y. Zhao et al. / Assessing and Understanding Creativity in Large Language Models 423
Table 1 Comparative creativity scores across LLMs
Fluency Flexibility Originality Elaboration
Common problem task
GPT-3.5 4.975 4.650 3.870 4.735
LLaMA-2-13b 4.940 4.480 3.770 4.890
LLaMA-2-70b 4.920 4.545 3.720 4.905
Qwen 3.090 2.890 2.360 3.360
Vicuna-13b 4.910 4.320 3.510 4.415
Vicuna-7b 4.880 4.270 3.380 4.200
Consequences task
GPT-3.5 4.855 4.810 4.105 5.000
LLaMA-2-13b 4.910 4.830 4.080 5.000
LLaMA-2-70b 4.930 4.830 3.995 4.995
Qwen 4.410 4.430 3.610 4.875
Vicuna-13b 4.260 4.295 3.580 4.850
Vicuna-7b 4.535 4.435 3.660 4.920
Improvement task
GPT-3.5 5.000 4.970 4.620 4.980
LLaMA-2-13b 4.980 4.850 4.150 4.890
LLaMA-2-70b 4.965 4.800 4.085 4.900
Qwen 4.870 4.550 3.760 4.700
Vicuna-13b 4.970 4.410 3.6