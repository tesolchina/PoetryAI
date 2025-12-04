---
source_pdf: Zhao et al..pdf
converted_date: 2025-12-04T20:07:34.189100
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
the entertainment industry, creating music and art[11, 12].
In many of their applications, LLMs seem to exhibit the
In recent years, the realm of artificial intelligence (AI) ability to generate original text, aiding tasks related to has witnessed a meteoric rise in the development and imagination and creativity, suggesting that they may in-
sophistication of large language models (LLMs)[1, 2]. LLMs deed possess elements of creativity.
have significantly advanced in their capabilities in ad- From the broad capabilities demonstrated by LLMs, dressing a variety of conventional natural language pro- the creativity they exhibit is a key reason they are con-
cessing tasks, such as reasoning and natural language un- sidered powerful. However, behind the impressive abilitderstanding[3–6]. Moreover, LLMs also have demonstrated ies of LLMs lies a significant question that warrants care-
significant value in widespread applications. From trans- ful examination: Do these models actually possess real forming rudimentary text into compelling narratives[7, 8], creativity, or is their apparent intelligence merely an illu-
unlocking a new realm of storytelling, to solving complex sion – a complex imitation of human thinking created by algorithmic problems[9], these models have shown a semb- their training paradigm? This question touches on the
lance of what could be interpreted as creativity. The very nature of LLM intelligence, which may not be easily practical manifestations of this creativity have penet- explained. Since LLMs have shown considerable creativ-
rated various sectors, including science research, where ity, understanding the extent and characteristics of this they assist in idea generation and suggestion[6]; education, creativity is essential. Gaining deeper insight into the cre-
by providing personalized learning experiences[10]; and in ativity of LLMs can not only guide us in further improving their performance but also in enhancing our under-
Research Article standing of the nature of their creativity. This, in turn,
Manuscript received on August 24, 2024; accepted on January 15, informs our daily use and application of these models, un-
2025; published online on April 28, 2025 derscoring the need for an effective method to measure
Recommended by Associate Editor Zhiyuan Liu and assess their creativity. Specifically, creative abilities
Colored figures are available in the online version at https://link.
springer.com/journal/11633
© The Author(s) 2025

[Page 2]
418 Machine Intelligence Research 22(3), June 2025 are critical for the following application scenarios. First, ginality, and elaboration. We let the LLMs answer ques-
LLM can inspire humans on creative tasks and provide tions from the constructed dataset, obtaining many quesnovel ideas, especially in research idea generation[13, 14]. It tion-answer pairs. We utilized GPT-4 as an evaluator to
has also been suggested that the use of LLM can also lead assess each answer, as the GPT-4 is capable of effectively to homogenization of creativity[15]. Second, humor genera- assessing the openness of responses and identifying their
tion with LLMs offer significant value in both creative shortcomings and errors. Under proper prompt engineerand practical applications. By simulating human-like hu- ing, GPT-4 can efficiently and effectively complete the
mor, LLMs can assist in content creation for entertain- evaluation of the entire dataset results. Thus, we can ment, marketing, and social media. Finally, LLMs can achieve a balance between efficiency and accuracy in our
serve as powerful cocreators in creative writings by gener- assessment method.
ating narrative ideas, suggesting plot developments, or We selected six popular LLMs as test subjects, each even drafting sections of text that inspire further refine- possessing different architectures and parameter scales. In
ment by human writers. addition to the overall testing, we conducted some addi-
Creativity, as a term, traditionally refers to the natur- tional exploratory experiments that investigate the al ability to think innovatively, to make unconventional changes of creativity levels exhibited by LLMs when giv-
connections, and to devise solutions that are both novel en different types of prompts and different roles that and effective[16]. Assessing the creativity of LLMs is LLMs play. Then, we designed a collaboration mechan-
fraught with challenges. First, the question of creativity ism for LLMs to explore the impact of multiple LLMs coldoes not have clear answers to refer to. When we ask an laborating on creativity. Last, we also performed some
LLM a question such as “what is the speed of light in va- psychological experiments related to personality traits on cuum in meters per second?”, the answer can be formally the LLMs, including emotional intelligence (EI), em-
vetted, given the objective nature of the topic. However, pathy, the big five inventory (BFI) and self-efficacy. Bewhen posed with a prompt such as “what would be the cause we found in relevant psychological research show-
implications if animals could talk?”, the situation be- ing that human creativity is correlated with these personcomes different in this case because there is no definitive ality traits and we verified the consistency between LLMs
answer and the answer is open and divergent, making it and humans in this regard.
challenging to judge the correctness of the output[17]. Ad- Our experiments and analysis yielded several concluditionally, since creativity encompasses various aspects, sions. First, there are significant differences in creative
including originality and flexibility, it is necessary to performance among different models, even among those of design diverse tasks and criteria to measure these qualit- the same scale with an equal number of parameters. This
ies effectively in LLMs. In addition, there are differences variation primarily exists between different types of modbetween LLMs and humans, which might lead to irrelev- els. Their differences are reflected mainly in the model ar-
ant responses or serious logical issues, requiring us to ad- chitecture, parameter settings during training, alignment ditionally assess these aspects. Finally, evaluating creativ- strategies, and the datasets used for training. Addition-
ity necessitates a delicate balance between accuracy and ally, we observed that models generally excel in the elabefficiency, rendering traditional human-based evaluation oration metric, but tend to be less adept in demonstrat-
methods less practical. Therefore, it is imperative to ad- ing originality. In addition, the type of prompt and the dress the challenges outlined above to make a robust and specific role-play request given to the model also plays a
sound assessment of creativity in LLMs. significant role in influencing its creative output. When
Recognizing the need for a comprehensive assessment the models are given instructive prompts or chain-ofof LLM′s creativity, we design an efficient framework to thought prompts, there is a significant increase in the
automatically assess the creativity of LLMs by adapting level of creativity. Additionally, having LLM play differand modifying the Torrance tests of creative thinking ent roles leads to notable differences; the role of a scient-
(TTCT)[18], a widely recognized tool in psychometrics′ re- ist demonstrates the highest level of creativity. Many search for human creativity assessment. To enhance the roles even show a decrease compared to the default scen-
credibility of the results and reduce the randomness, sev- ario, but there is generally an improvement in originality.
en verbal tasks, which use verbal stimuli, were selected. Then, collaboration among multiple LLMs can enhance
We employed GPT-4, the most advanced LLM, to ex- the level of creativity, with the most notable improvepand the question set for each task, thereby constructing ment in originality. Finally, the results of the psycholo-
the testing dataset. To ensure a thorough and objective gical scale revealed consistency between LLMs and huevaluation of creativity and capture creativity′s various mans in terms of associated creativity factors, such as
manifestations, we combine diverse tasks and criteria. We emotional intelligence (EI), empathy, self-efficacy, and design a comprehensive test protocol incorporating four others.
criteria for measuring creativity: Fluency, flexibility, ori-

[Page 3]
Y. Zhao et al. / Assessing and Understanding Creativity in Large Language Models 419
# 2 Related works intelligence, and gender exhibit a relatively milder associ-
ation with creativity, signifying a varied spectrum of influence across different personal traits. Since large lan-
## 2.1 Creativity assessment in psychological guage models have exhibited some personality traits, we
research conducted experiments to test whether these findings also hold true in LLMs.
The question of creativity assessment has been a prominent focus on the creativity research, especially ## 2.3 Assessing the creativity of large lan-
since the 1950s, marking the inception of a systematic guage models study into individual differences in creativity[19]. For ex-
ample, Guilford pioneered the research on creativity and The emergence of abilities from LLMs continually surhis famous structure of intellect model was mainly about passes people′s expectations, and the evaluation of vari-
defining and analyzing the factors constituting intelli- ous abilities of LLMs has received widespread attengence, where creativity plays a major driving force in his tion[30]. Currently, most evaluations focus on the ability
theory[20]. In recent years, many new developments re- of LLMs to solve tasks, with fewer evaluations combingarding the measurement of divergent thinking, consensu- ing aspects of psychology.
al assessment technique and subjective ratings, and self- Although some studies have focused on the intersecreport methodology[21–23] have emerged. Although ad- tion of LLM with psychology and cognitive science[31],
vances in methodology and technology have led to im- work discussing the creativity of LLM is still in a relatportant developments regarding creativity assessment, ively early stage. Current studies somewhat focused on
some assessment methods have long been described as exploring the creativity of LLMs, primarily from the
“gold standard” for creativity assessment[24, 25]. Among standpoint of creativity theory, which aims to elucidate them, TTCT[18] has been the most widely used and re- the definitions and challenges of applying creativity the-
searched test of creativity, having extensive data to sup- ory within the context of LLMs[32]. Some initial evaluport its reliability and validity. Research on TTCT re- ations of creativity in LLMs have also been underta-
ports good reliability scores for scoring and test-retest re- ken[33–35]. However, these works only employed simple liability[26]. tasks such as the alternative uses task (AUT) to assess
TTCT is designed to identify and assess an indi- creativity, and the lack of comparison between various vidual′s creative potential by exploring various dimen- LLMs limits the validity of their conclusions. It is worth
sions. Contrasting conventional assessments that emphas- mentioning that in [36], the authors used the standard ize convergent thinking, the test fosters divergent think- TTCT to assess GPT-4′s creativity. The results show
ing, encouraging participants to generate multiple solu- that GPT-4 achieved human top 1% levels in fluency and tions to open-ended, ambiguous problems. TTCT has originality, along with a high score in flexibility. This
been widely applied in educational settings, organization- study leans more towards comparing advanced large lanal assessments, demonstrating its versatility and compre- guage models (LLMs) with human benchmarks. The ori-
hensive approach to measuring creativity. Its ability to ginal TTCT test protocol does not seamlessly adapt to tap into various facets of creative thinking has made assessing creativity in LLMs, as the limited sample of
TTCT a reliable and respected tool[27]. Owing to the au- questions could induce randomness and accidental outthority and comprehensiveness of the TTCT, we select comes, making hypothesis testing challenging when com-
tasks from the TTCT to construct our dataset. paring different models. Furthermore, expanding the number of question sets leads to high time costs in hu-
## 2.2 Creativity and personality: Findings in
man-based evaluations.
psychological research
Due to the differences between humans and LLM, it is problematic to directly use the TTCT′s test protocol to
Research has revealed that creativity is not solely a benchmark LLMs′ creativity. To address this dilemma, fixed human personality trait. It evolves from a combina- we propose a new framework for systematic analysis
tion of individual processes such as cognitive, affective, LLM′s creativity. This framework comprises carefully behavioral, and contextual factors. Some psychologists crafted metrics used in TTCT and a dataset that ac-
have conducted a detailed meta-analysis of papers explor- counts for seven tasks. We will dive into detail of the ing the relationship between creativity and various per- framework in Section 3.
sonality traits[28, 29].
These studies′ results highlight a correlation between # 3 Overview of the framework creativity and a plethora of personal factors. Notably, ele-
ments such as emotional intelligence, divergent thinking, In this work, we design an overall framework to evaluopenness to experience, and intrinsic motivation stand ate LLM′s creativity, as shown in Fig. 1. First, we con-
out as strong influencers. However, factors such as age, structed a dataset containing 700 questions of 7 tasks

[Page 4]
420 Machine Intelligence Research 22(3), June 2025
Prompt type
Torrance® tests of creative thinking
Basic prompt Criteria
Common problems task. The scenario is:
Planning a birthday party for a 5-year-old. Fluency
The ability to produce a significant number of relevant ideas in response to a given
Instructive prompt question. In essence, fluency measures the
Common problems task. There is no right or quantity of ideas.
wrong answers, we're interested in how many different problems you can identify and the
Question v oa ur ti se idty e o thf ei s bs ou xes a y no du c oco nn sis did ee r r a. s T mry a nto y t ph oin tek n tial Flexibility
LLM generating p br iro tb hl de am ys p a as r tp yo fs os ri b al e 5. - yT eh ae r -s oc le dn .ario is: Planning a LLMs T geh ne e v raa tr eie it dy e o asf .c Ia t't se g tho er i ae bs if lr ito ym to w thh ii nch k o on f e a lc tea rn natives, shift from one class or perspective to
Chain of thought (CoT) prompt GPT-3.5 another, and to approach a given problem or task from different angles.
Common problems task. Let's think step by step.
Creative questions T 5-h ye e asc r-e on la dr .io is: Planning a birthday party for a Llama-2-13b
Originality
U Qn : u Ps leu aa sl eu ls ie ss t uta ns uk sual uses of plastic Role play Llama-2-70b T Oh rie g u inn ai lq u ide en ae ss s a ro ef tt hh oe s eid te ha as t g ae ren e rr aa rt ee od r.
bottle. Qwen unconventional, differing from the norm.
Student
C Qo : n Wse hq au t e wn oce us ld t a hs ak ppen if we could A foc llt o l wik ie n ga t ty asp kic oa rl ap nri sm wa er ry f osc llh oo wo il n s gt u qd ue en st t. i oD no … Vicuna-7b Elaboration time travel?
Vicuna-13b The ability to expand upon, refine, and
Scientist embellish an idea. It involves adding details,
Situation task Act like a typical natural scientist. Do following developing nuances, and building upon a
Q: If the sun didn't rise tomorrow, how task or answer following question… basic concept to make it more intricate or would you ensure you had enough light complex.
during the day?
Artist
··· Act like a typical music artist. Do following task or answer following question…
7 tasks · 700 questions Judger: GPT-4 & human
···
Fig. 1 Overview of the creativity assessment framework. A TTCT-inspired dataset was constructed to evaluate LLMs under varied prompts and role-play settings. GPT-4 served as the evaluator to score model outputs.
that were derived and modified from the psychology scale ity. This makes them sufficient for assessing a holistic of the TTCT and expanded the number of questions via view of creative potential.
GPT-4. We tested six models on four different criteria us- Specifically, each task includes one hundred questions ing the dataset we constructed. Following this, we con- generated by GPT-4 using few-shot prompts. The seven
ducted a series of experiments on the creativity of LLMs tasks were generally structured as follows:
when giving different types of prompts and assigning dif- 1) Task 1: Unusual uses. This task challenges indiferent roles to LLMs. Finally, we used the GPT-4 as the viduals in their ability to think of as many unusual and
evaluator to obtain the performance results of the LLMs diverse uses as possible for a common object within a limand verify the consistency of the LLM-based evaluation ited time frame. The object in question is typically every-
with humans. day and familiar, such as a brick, paper clip, or newspaper.
## 3.1 Dataset construction 2) Task 2: Consequences. This task focuses on the
ability to foresee consequences or outcomes of an unusual
This research utilized a modified version of the TTCT or hypothetical situation. For example, what would be verbal test, which includes tasks based on verbal stimuli. the implications if animals could talk?
The seven selected tasks: 1) Unusual uses, 2) con- 3) Task 3: Just suppose. This task encourages imasequences, 3) just suppose, 4) situations, 5) common ginative and speculative thinking by asking participants
problems, 6) improvements, and 7) imaginative stories, to consider hypothetical, often fantastical, scenarios and were chosen to capture a broad spectrum of creative their implications. For example, just suppose you woke
thinking abilities. These tasks are adapted from the up one morning and found you could fly. What would widely used TTCT, which has also served as the basis for you do? List as many things as you can think of.
recent work in the field of LLM evaluation[37]. The tasks 4) Task 4: Situation task. This task is designed to we choose align with widely accepted models of creativ- assess creative thinking by evaluating how individuals re-
ity such as Guilford′s structure of the intellect model and spond to and interpret a given situation. This task eminvolve both divergent and convergent thinking[20]. Mean- phasizes understanding social dynamics, empathy, and
while, TTCT tasks, especially in their divergent thinking the ability to consider multiple perspectives or solutions.
focus, align with the Geneplore model[38] by emphasizing For example, if all books were to disappear, how would idea generation (fluency and originality) and flexibility you gain knowledge?
(the ability to shift between categories or approaches). 5) Task 5: Common problem. This task focuses on
Thus, the tasks capture both novelty and usefulness, everyday problems that are familiar to most people, rewhich are central to most modern definitions of creativ- quiring participants to generate innovative and effective

[Page 5]
Y. Zhao et al. / Assessing and Understanding Creativity in Large Language Models 421 solutions. For example, organizing a cross-country road plementary facets of creative thinking and have been ex-
trip or building a tree house. tensively validated in psychological and educational re-
6) Task 6: Improvement. This task focuses on as- search and are considered gold standards in creativity as-
sessing an individual′s ability to enhance or modify exist- sessment.
ing objects or ideas. The given object is similar to the unusual uses task. ## 3.3 LLM-based evaluation
7) Task 7: Imaginative stories. This task is de-
signed to assess creativity through narrative and Standard TTCT evaluation methods require trained storytelling with a given prompt. This task emphasizes psychologists to follow professional manuals to assess the
the ability to construct original, coherent, and imaginat- results, and an individual′s single test only contains anive stories, showcasing an individual′s creative potential swers to a very limited number of questions. When evalu-
in terms of narrative ability. Examples of given prompts ating creativity in LLM, both the insufficient sample of are “The Invisible Elephant” or “The Book that Wrote responses and the high human resource costs limit the ap-
Itself”. plication of creativity tests on LLMs. Recent psychologic-
Each task includes 100 questions generated by GPT-4 al research has focused on the automated assessment of via few-shot prompts. GPT-4 can generate a diverse and creativity[41, 42]. However, these methods often have limit-
comprehensive set of similar problems based on the given ations, such as being tailored to specific tasks or requirexamples, and all problems have been validated by hu- ing prepared reference answers, which prevent their gen-
mans to ensure usability. In addition, we conducted ex- eralization to a variety of tasks and a larger number of perimental validation of domain generality across differ- questions.
ent tasks. Cronbach′s Alpha and inter-task correlations With the rapid development of LLM capabilities, the indicate that our task selection is effective and sufficient. evaluation methods for many natural language pro-
cessing tasks have evolved from traditional human an-
## 3.2 Evaluation criteria notation to reference-based automated methods, and now,
to methods on the basis of LLMs. LLMs are increasingly
To provide a comprehensive evaluation of an individu- playing the role of judges in tasks such as question-anal′s creative abilities, we should consider not only the swering, translation, and text quality assessment[43–46],
quantity of ideas they produce, but also the quality, di- giving rise to various evaluation framework[47–49]. Accordversity, and depth of those ideas. We have four criteria ing to experimental results from relevant literature, LLM
for creativity evaluation: exhibits higher correlation with human evaluations com-
1) Fluency. This refers to the ability to produce a pared with traditional automated technologies[50, 51]. In
significant number of relevant ideas in response to a giv- this study, on the basis of the evaluation criteria from en question. In essence, fluency measures the quantity of Section 3.2, we utilize GPT-4 to score the answer. For
ideas. each criterion, the LLM needs to complete the Likert
2) Flexibility. This assesses the variety of categories scale based on the responses. Additionally, we verified the
from which one can generate ideas. It is the ability to consistency between the evaluations made by LLM and think of alternatives, shift from one class or perspective human evaluations.
to another, and to approach a given problem or task from different angles.
# 4 Evaluation and results
3) Originality. This measures the uniqueness of the
We conducted a statistical analysis of the creativity ideas generated. Original ideas are rare or unconvention-
scores of 6 popular LLMs across seven tasks, totaling 700 al, differing from the norm.
questions. We unveiled hidden conclusions within the
4) Elaboration. This refers to the ability to expand
data results from various dimensions. We compared the upon, refine, and embellish an idea. It involves adding de-
tails, developing nuances, and building upon a basic differences in creativity levels between the models, and concept to make it more intricate or complex. we compared the performance variations under different
These criteria aim to provide a comprehensive assess- criteria within the same model. Subsequently, we experiment of an individual′s creative potential. The motiva- mented with many types of prompts to see whether
tion behind using these specific dimensions is grounded in changes in prompts would affect the models′ levels of crethe theoretical and empirical research on creativity[39, 40], ativity. Since LLMs possess the ability to play user-spe-
which suggests that creative thinking involves not just cified roles, we select six typical human identities to exthe generation of new ideas but also the ability to manip- plore the impact on creativity under different role-play-
ulate, refine, and apply these ideas effectively. The four ing conditions. Finally, we utilize some psychological criteria are based on long-standing psychological frame- scales to test the LLMs, investigating the correlation
works for creativity assessment, particularly the TTCT. between the personality traits of the LLMs and creativ-
These dimensions collectively capture distinct and com- ity.

[Page 6]
422 Machine Intelligence Research 22(3), June 2025
## 4.1 Experimental settings the model′s output logits. However, according to our ex-
periments, changes in temperature do not significantly af-
### 4.1.1 Tested models fect creative performance, which appears quite random.
We tested six of the most advanced LLMs, which are Therefore, in our experiments, the temperature is unilisted below. All the models were implemented with the formly set to 1.
open-source repository HuggingFace[52]. 3) Top_p. Top_p is also a parameter used to control
1) GPT-3.5. GPT-3.5 is a language model de- the diversity of the generated text, also known as “nucle-
veloped by OpenAI, which is an advanced version of the us sampling”. This parameter′s full name is “top probab-
GPT-3 model. It is capable of generating natural lan- ility”, which is typically represented by a value between 0 guage text and code. GPT-3.5 was trained on an Azure and 1, indicating the cumulative threshold of the highest
AI supercomputing infrastructure. The versions we used probabilities chosen in the probability distribution when in the experiments are GPT-3.5-turbo-0613. generating the next token. In our experiments, top_p is
2) LLaMA-2. LLaMA-2 is a family of state-of-the- uniformly set to 1.
art open-access large language models released by Meta 4) Top_k. This parameter is used when generating and Microsoft[2]. It is built upon success of its prede- the next token to limit the model to consider only the
cessor, LLaMA-1. LLaMA-2 is specifically designed to fa- top_k tokens with the highest probability. This strategy cilitate the development of generative AI-powered tools can reduce the likelihood of the model generating mean-
and experiences. It is available for free research and com- ingless or repetitive outputs, while also improving the mercial use. LLaMA-2 release introduces a family of pre- speed and efficiency of the model generation. In our ex-
trained and fine-tuned LLMs, ranging in scale from 7 B to periments, the top_k is uniformly set to 50.
70 B parameters. The versions we used in the experi- GPT-4 serves as the judge for our LLM-based evaluments are LLaMA-2-13b-chat-hf and LLaMA-2-70b-chat- ation, with its relevant parameters set to default. The
hf. version used is GPT-4-0613. In addition, all prompt tem-
3) Vicuna. Vicuna is a lightweight, accurate, and ef- plates used in the experiment are provided in the ap-
ficient language model developed by a team of research- pendix.
ers from several universities, including UC Berkeley,
Carnegie Mellon University, Stanford University, and UC ## 4.2 Results of different models and criteria
San Diego[44]. It was built from Meta′s adaptable LLaMA model, which was fine-tuned on a dataset of around 70 000 We assessed the responses of six language models to
human-generated conversations from the ShareGPT web- 700 questions, with GPT-4 serving as the evaluator across site. The versions we used in the experiments are Vicuna- all creativity dimensions. We first evaluate the average
7b-v1.5 and Vicuna-13b-v1.5. score of each model across all tasks, as shown in Fig. 2(a)
4) Qwen. Qwen (abbr. Tongyi Qianwen), proposed and Table 1. It can be observed that GPT-3.5 has the
by Alibaba Cloud[53]. It is a transformer-based large lan- highest level of creativity, followed by the LLaMA-2 arguage model, which is pretrained on a large volume of chitecture models, then the LLaMA-based fine-tuned
data, including web texts, books, codes, etc. The versions model vicuna, and finally Qwen. The experimental reswe used in the experiments are Qwen-7b-chat. ults from the perspective of the model suggest that the
### 4.1.2 Details of hyperparameters type of model has a significant effect on creativity, where-
The models used in our experiment primarily origin- as the scale of parameters does not have a decisive influate from the open-source HuggingFace platform. The spe- ence. Different types of models vary in their architec-
cific versions of these models have already been reported tures, alignment strategies, and the datasets used during above. In this section, we present the experimental para- training. These factors are likely to be key determinants
meters and other settings related to the experiment. of the level of creativity. Similar findings can also be ob-
For an LLM based on the transformer architecture, served in other LLM evaluation papers[54–56]. For exthere are certain parameters that directly affect the out- ample, in Toolbench[56], the 30 B version of LLaMA out-
put of the model. performs the 65 B version of LLaMA in many tasks, and
1) Max tokens. This parameter controls the maxim- text-daVinci-003 also performs better overall than GPT-
um number of tokens to generate in the chat completion. 3.5.
In our experiment, this value is uniformly set to 512, en- To further validate the ranks of the models, we consuring that the output length is sufficient to maintain the ducted pairwise comparisons between the models, as
quality of the answers. shown in Fig. 2(b). Each cell in this heatmap represents
2) Temperature. The parameter is a crucial factor the win rate of the model on the y-axis in terms of cre-
in determining the nature of the model′s responses. This ativity score compared to the model on the x-axis. The is a hyperparameter that influences the randomness or win rate scores are consistent with the strengths and
unpredictability in the model′s responses. Essentially, its weaknesses of the models shown in Fig. 2(a), and we conmechanism is to change the probability distribution of ducted statistical tests for significance, which are marked

[Page 7]
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
Vicuna-13b 4.970 4.410 3.600 4.380
Vicuna-7b 4.950 4.560 3.860 4.640
Imaginative stories task
GPT-3.5