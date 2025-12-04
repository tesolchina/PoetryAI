---
source_pdf: Franceschelli_2025_LLM_Creativity.pdf
converted_date: 2025-12-04T20:28:20.066461
total_pages: 11
model: Google Gemini 2.0 Flash
total_cost_usd: $0.005117
prompt_tokens: 18,401
completion_tokens: 8,192
---

# On the creativity of large language models

Giorgio Franceschelli1 · Mirco Musolesi1,2

Received: 8 November 2023 / Accepted: 29 October 2024 / Published online: 28 November 2024
© The Author(s) 2024

Abstract
Large language models (LLMs) are revolutionizing several areas of Artificial Intelligence. One of the most remarkable applications is creative writing, e.g., poetry or storytelling: the generated outputs are often of astonishing quality. However,
a natural question arises: can LLMs be really considered creative? In this article, we first analyze the development of LLMs under the lens of creativity theories, investigating the key open questions and challenges. In particular, we focus our dis-
cussion on the dimensions of value, novelty, and surprise as proposed by Margaret Boden in her work. Then, we consider different classic perspectives, namely product, process, press, and person. We discuss a set of “easy” and “hard” problems
in machine creativity, presenting them in relation to LLMs. Finally, we examine the societal impact of these technologies with a particular focus on the creative industries, analyzing the opportunities offered, the challenges arising from them, and
the potential associated risks, from both legal and ethical points of view.

Keywords Large language models · Machine creativity · Generative artificial intelligence · Foundation models

# 1 Introduction

Language plays a vital role in how we think, communicate, and interact with others.1 It is therefore of no surprise that
natural language generation has always been one of the prominent branches of artificial intelligence (Jurafsky and
Martin 2023). We have witnessed a very fast acceleration of the pace of development in the past decade culminated
with the invention of transformers (Vaswani et al. 2017).
The possibility of exploiting large-scale data sets and the availability of increasing computing capacity has led to the
definition of the so-called foundation models, which are able to achieve state-of-the-art performance in a variety of tasks
(Bommasani et al. 2021). Among them, large language models (LLMs) are indeed one of the most interesting developments. They have cap-
tivated the imagination of millions of people, also thanks to a series of entertaining demonstrations and open tools
released to the public. The examples are many from journal articles2 to culinary recipes (Lee et al. 2020) and university-
level essays.3 LLMs have also been used to write papers about themselves writing papers (GPT-3 2022). They are
commonly used for creative tasks like poetry or storytelling and the results are often remarkable.4 Notwithstanding, it
is not obvious whether these “machines” are truly creative, at least in the sense originally discussed by Ada Lovelace
(Menabrea and Lovelace 1843). LLMs have already been analyzed (and sometimes criticized) from different perspec-
tives, e.g., fairness (Bender et al. 2021), concept understanding (Bender and Koller 2020), societal impact (Tamkin et al.
2021), and anthropomorphism (Shanahan 2024) just to name a few. However, a critical question has not been considered
yet: can LLMs be considered creative?

* Giorgio Franceschelli giorgio.franceschelli@unibo.it
*
Mirco Musolesi m.musolesi@ucl.ac.uk
1 As remarked by ChatGPT itself when asked about the importance of language.
1 Department of Computer Science and Engineering, 2 http:// www. thegu ardian. com/ comme ntisf ree/ 2020/ sep/ 08/ robot-
University of Bologna, Viale del Risorgimento 2, wrote- this- artic le- gpt-3.
40136 Bologna, Italy 3 https:// www. thegu ardian. com/ techn ology/ 2022/ dec/ 04/ ai- bot- chatg
2 Department of Computer Science, University College pt- stuns- acade mics- with- essay- writi ng- skills- and- usabi lity.
London, 66-72 Gower Street, London WC1E 6BT, 4 See, for instance: https:// www. gwern. net/ GPT-3.
United Kingdom

By taking into account classic frameworks for analyzing (e.g., Riedl and Young (2010)) and case-based reasoning creativity, such as Boden’s three criteria (Boden 2003) and (e.g., Turner (1994)) to evolutionary strategies (e.g., Manu-
other prominent cognitive science and philosophical theo- rung et al. (2012)). Some approaches combine all of them ries (e.g., Amabile (1983); Csikszentmihalyi (1988); Gaut together (Gervás 2013).
(2010)), we will try to answer this question. We will discuss Only with the advent of neural networks and learning systhe dimensions according to which we believe LLMs should tems, we observed a real step-change. In particular, deep lan-
be analyzed to evaluate their level of machine creativity. To guage models, i.e., probabilistic models of in-context token the best of our knowledge, this article represents one of the occurrences trained on a corpus of text with deep learning,
first investigations of the problem of LLM creativity from a easily allow the sampling of new text, facilitating and autotheoretical and philosophical perspective. mating natural language generation. For instance, recurrent
The remainder of the paper is structured as follows. neural networks with long-short term memory (LSTM)
First, we briefly review the past developments in automatic (Hochreiter and Schmidhuber 1997) or gated-recurrent text generation and artificial creativity (Sect. 2) that led to units (GRUs) (Cho et al. 2014) can predict the next char-
today’s LLMs. Then, we analyze LLMs from the perspec- acter (Karpathy 2015), word (Potash et al. 2015), syllable tive of Boden’s three criteria (Sect. 3), as well as consider- (Zugarini et al. 2019), or event (Martin et al. 2018) given
ing other relevant philosophical theories (Sect. 4). Finally, previous ones, allowing to compose text that spans from we discuss the practical implications of LLMs for the arts, short movie scripts to knock-knock jokes (Miller 2019).
creative industries, design, and, more in general, scientific Other successful generative methods include generative and philosophical inquiry (Sect. 5). Section 6 concludes the adversarial networks (GANs) (Yu et al. 2017; Zhang et al.
paper, outlining the open challenges and a research agenda 2017) and variational auto-encoders (VAEs) (Bowman et al.
for future years. 2016; Semeniuta et al. 2017). We refer the interested reader to Franceschelli and Musolesi (2024b) for an in-depth survey
of deep learning techniques applied to creative artifacts.
# 2 A creative journey from Ada Lovelace
These models tend to scale poorly to long sequences, and to foundation models
they are often unable to capture the entire context. For this reason, current state-of-the-art language models make use
It was the year 1843 when Ada Lovelace wrote that the Ana- of attention (Bahdanau et al. 2015) and transformers (Vaslytical Engine (Babbage 1864) “has no pretensions to origi- wani et al. 2017). In recent years, several models based on
nate anything. It can do whatever we know how to order it these mechanisms have been proposed. They usually rely on to perform” (Menabrea and Lovelace 1843). This statement a very large number of parameters and are trained on cor-
was then defined as “Lovelace’s objection” by Alan Turing, pus datasets of greater and greater size (Brown et al. 2020; who also provided an alternative formulation: a machine can Chowdhery et al. 2023; Devlin et al. 2019; Du et al. 2022;
never “take us by surprise” (Turing 1950). This was just the Hoffmann et al. 2022; Radford et al. 2019; Rae et al. 2021; beginning of an ongoing philosophical discussion, which Raffel et al. 2020; Rosset 2020; Shoeybi et al. 2019; Smith
has often included psychological elements, around human et al. 2022; Thoppilan et al. 2022). Thanks to in-context creativity (Barron 1955; Berlyne 1960; Bruner 1962; Newell learning techniques such as zero-shot or few-shot learning
et al. 1962; Stein 1974), as well as computational creativity (Dong et al. 2024), these models can produce more specific
(Boden 2009; Colton and Wiggins 2012; Jordanous 2009; and specialized content, such as poems or stories (Swan-
Macedo et al. 2004; Maher 2010; Wiggins 2006). son et al. 2021), by simply providing a description of the
In general, computer scientists have always been fasci- task and possibly some examples. However, finding the cornated by the possibility of building machines able to express rect input and high-quality demonstrations for solving this
themselves through writing, e.g., by composing poems and type of task can be challenging (Liu et al. 2022). Certain short stories, creating paintings, and so on. In particular, the domains might require more fine-grained knowledge than
rise of automatic text generation was contextual to the birth that acquired during pre-training (Peng et al. 2023). Because of personal computers. Examples include the Computerized of this, other methods to adapt a pre-trained model have been
Haiku by Margaret Masterman,5 the storyteller TALE-SPIN considered. LLMs can involve re-training through plug-and-
(Meehan 1977), Racter and its poems’ book (Racter 1984), play attribute classifiers (Dathathri et al. 2020); re-training to and UNIVERSE, which was able to generate coherent and produce paragraphs coherent with a given outline (Rashkin
consistent characters (Lebowitz 1983), just to name a few. et al. 2020); fine-tuning with specific corpora for writing
Different techniques have been explored, from planning specific text (Sawicki et al. 2022; Wertz and Kuhn 2022); or fine-tuning to maximize human preferences (Ziegler et al.
2019) or to generate specific literary outputs, such as poetry
5 http:// www. in- vacua. com/ cgi- bin/ haiku. pl. (Pardinas 2023). Nevertheless, the recent advancements

in LLMs can be attributed to the introduction of fine-tun- Novelty refers to the dissimilarity between the produced ing through reinforcement learning from human feedback artifact and other examples in its class (Ritchie 2007).
(RLHF) (Christiano et al. 2017). It consists of three steps: However, it can also be seen as the property of not being fine-tuning the pre-trained model in a supervised fashion on in existence before. This is considered in reference to either
human-produced answers to sampled questions; training a the person who came up with it or the entire human hisreward model to predict which text among different options tory. The former is referred to as psychological creativity
is the most appropriate based on human-labeled rankings; (shortened as P-creativity), whereas the latter is historical and fine-tuning the language model to maximize the learned creativity (shortened as H-creativity) (Boden 2003). While
reward (Stiennon et al. 2020). Although the main goal of the difference appears negligible, it is substantial when dis-
RLHF is to improve conversational skills while mitigating cussing LLMs in general. Considering these definitions, mistakes and biases, it has also led to models capable of pro- a model writing a text that is not in its training set would
ducing on-demand poems, songs, and novels, gaining global be considered as P-novel, but possibly also H-novel, since popularity.6 Based on RLHF, first ChatGPT7 and then GPT-4 LLMs are commonly trained on all available data. Their
paved the way for several other similar models: Google’s stochastic nature and the variety of prompts that are usu-
Gemini (Gemini Team and Google 2023), which extends to ally provided commonly lead to novel outcomes (McCoy multimodal data; Meta’s Llama models (Dubey et al. 2024; et al. 2023); LLMs may therefore be capable of generating
Touvron et al. 2023), which replace RLHF with the more artifacts that are also new. However, one should rememefficient direct preference optimization (DPO) (Rafailov ber how such models learn and generate. LLMs still play a
et al. 2023); Mixtral (Jiang et al. 2024), which adaptively sort of imitation game, without a focus on (computational) selects its layers’ parameters from distinct groups to increase novelty (Fazi 2019). Even if prompted with the sentence “I
the total parameter count without raising computational wrote a new poem this morning:”, they would nonetheless costs; and many others, as the competition intensifies day complete it with what is most likely to follow such words,
by day (Zhao et al. 2023). While they may differ in some e.g., something close to what others have written in the past technical details, these LLMs are always pre-trained on vast, (Shanahan 2024). It is a probabilistic process after all. The
general corpora of data and then fine-tuned using some form degree of dissimilarity would therefore be small by design.
of RLHF to enhance their conversational skills. High values of novelty would be caused either by accidental, out-of-distribution productions or by careful prompting, i.e.,
one that would place the LLM in a completely unusual or
# 3 L arge language models and Boden’s three
unexpected (i.e., novel) situation.
criteria
Surprise instead refers to how much a stimulus disagrees with expectation (Berlyne 1971). It is possible to identify
Margaret Boden defines creativity as “the ability to come up three kinds of surprise, which correspond to three different with ideas or artifacts that are new, surprising and valuable” forms of creativity. Combinatorial creativity involves mak-
(Boden 2003). In other words, Boden implicitly derives cri- ing unfamiliar combinations of familiar ideas. Exploratory teria that can be used to identify a creative product. They creativity requires finding new, unexplored solutions inside
suggest that creativity is about novelty, surprise and value. the current style of thinking. Transformational creativity
We will refer to them as Boden’s three criteria. In the fol- is related to changing the current style of thinking (Boden lowing, we will analyze to what extent state-of-the-art LLMs 2003). These three different forms of creativity involve sur-
satisfy them and we will question if LLMs can be really prise at increasing levels of abstraction: combining existing considered creative. elements, exploring new elements coherent with the cur-
Value refers to utility, performance, and attractiveness rent state of the field, and transforming the state of the field
(Maher 2010). It is also related to both the quality of the to introduce other elements. The autoregressive nature of output, and its acceptance by society. Due to the large impact classic LLMs makes them unlikely to generate surprising
LLMs are already having (Bommasani et al. 2021) and the products (Bunescu and Uduehi 2019) since they are essenquality of outputs of the systems based on them (Stevenson tially trained to follow the current data distribution (Shana-
et al. 2022a), it is possible to argue that the artifacts pro- han 2024). By relying only on given distributions and being duced by them are indeed valuable. trained on them, LLMs might at most express combinatorial
or exploratory creativity. Of course, specific different solutions may be generated by means of prompting or condi-
tioning. For instance, recent LLMs can write poems about
6 https:// www. forbes. com/ sites/ marti nepar is/ 2023/ 02/ 03/ chatg pt- hitsmathematical theories, a skill that requires the application
100- milli on- micro soft- unlea shes- ai- bots- and- catgpt- goes- viral/? sh=
70994 24756 4e. of a certain existing style to a given topic, yet leading to new
7 https:// openai. com/ blog/ chatg pt/. and unexplored solutions. However, the result would hardly

be unexpected for whom has prompted the text. For an exter- is achieved but how it is achieved that matters. An interesting nal reader, the surprise would probably come from the idea definition that considers both the what and how dimensions
of mathematical theories in verses, which is due to the user is the one from Gaut (2003): creativity is the capacity to
(or by the initial astonishment of a machine capable of it produce original and valuable items by flair. Exhibiting flair
(Waite 2019)). Transformational creativity is not achievable means exhibiting a relevant purpose, understanding, judgthrough the current LLM training solutions. In theory, other ment, and evaluative abilities. Such properties are highly
forms of training or fine-tuning might circumvent this limita- correlated with those linked with process, i.e., motivation, tion, allowing the model to forget the learned rules to forge perception, learning, thinking, and communication (Rhodes
others. However, this is not the case with current models. 1961). Motivation is a crucial part of creativity, as it is the
ChatGPT and all the other state-of-the-art LLMs introduced first stage of the process. Usually, it comes from an intrinin Sect. 2 are fine-tuned with RLHF or DPO. While in theory sic interest in the task, i.e., the activity is interesting and
this could lead to potentially surprising generation, its strict enjoyable for its own sake (Deci and Ryan 1985). However, alignment to very careful and pre-designed human responses LLMs lack the intention to write. They can only deal with
leads to the generation of text that tends to be less diverse “presented” problems, which are less conducive to creativ-
(Kirk et al. 2024) and that might be considered banal (Hoel ity (Amabile 1996). The process continues with the prepa-
2022). ration step (reactivating the store of relevant information
Nonetheless, the outputs from such models are often and response algorithms), the response generation, and its considered creative by the person interacting with them or validation and communication (Amabile 1983). The last two
exposed to their best productions. Though this is apparently steps allow one to produce different response possibilities in contrast with what was discussed above, we can explain and to internally test them in order to select the most appro-
this phenomenon by considering the fact that our perception priate. Again, LLMs do not contain such a self-feedback does not usually align with theoretical definitions of crea- loop. At the same time, they are not trained to directly maxi-
tivity. Indeed, we do not typically judge the creativity of a mize value, novelty, or surprise. They only output content product by considering its potential novelty and surprise in that is likely to follow given a stimulus in input (Shanahan
relation to its producer, but rather in relation to ourselves. 2024). In other words, they stop at the first stage of creative
Something can be new for the beholder, leading to a new learning, i.e., imitation, not implementing the remaining kind of novelty which we call B-novelty, as it is the one “in ones, i.e., exploration and intentional deviation from con-
the eye of the beholder”, but not new for the producer nor the ventions (Riedl 2018).
entire human history. The same applies to surprise: a product However, paraphrasing Chalmers (Chalmers 1996), these can violate the observer’s expectations in many ways with- appear as easy problems to solve to achieve creativity, since
out being unexpected considering the entire domain. In other solutions to them can be identified by taking into considwords, the product of an LLM can appear to be creative—or eration the underlying training and inference processes.
be B-creative—even if it is not truly creative according to The hard problem in machine creativity is about the intenthe theory of creativity. tionality and the self-awareness of the creative process in
In conclusion, while LLMs are capable of producing arti- itself. Even though the intent of running the LLM may be facts that are valuable, achieving P- or H-novelty and sur- achieved by its outcome, it is in an unintentional way (Ter-
prise appears to be more challenging. It is possible to argue zidis et al. 2022); as current generative AI models are only that LLMs may be deemed able to generate creative prod- causal, and not intentional, agents (Johnson and Verdicchio
ucts if we assume the definition of combinatorial creativity. 2019). Indeed, a crucial aspect of the creative process is the
To achieve transformational creativity, alternative learning perception and the ability of self-evaluating the generated architectures are probably necessary; in fact, current proba- outputs (Amabile 1983). This can be seen as a form of crea-
bilistic solutions are intrinsically limiting in terms of expres- tive self-awareness. While not strictly necessary to generate sivity. We believe that this is a fundamental research area for a response, this ability is essential to self-assess its quality,
the community for the years to come. so as to correct it or to learn from it. However, no current
LLM is able to self-evaluate its own responses. LLMs can in theory recognize certain limitations of their own texts
# 4 E asy and hard problems in machine
after generating them, e.g., by ranking them (Franceschelli creativity
and Musolesi 2024a) or by assigning quality- and diversitybased scores (Bradley et al. 2024). Then, they can try to
LLMs might be able to generate creative products in the correct, modify, or rephrase the outputs if asked to do so future. However, the fact that they will be able to gener- (i.e., through an external intervention). However, they would
ate these outputs will not make them intrinsically creative. do it only by guessing what is the most likely re-casting of
Indeed, as Floridi and Chiriatti (2020) puts it, it is not what such responses or through the application of a set of given

rules. It is worth noting that this is something distinct from acquire such information is limited, and by the next day, the problem of the potential emergence of the theory of mind they will have forgotten it all. In other words, these genera-
in these systems (Bubeck et al. 2023). tive agents do not truly adapt or learn new things about the
Indeed, product and process are not sufficient to explain changing domain. Placing them in a different environment creativity. Rhodes (1961) theorizes that four perspectives that requires a different prompt will make them start over,
have to be considered: product (see Sect. 3) and process without the possibility of leveraging previously acquired
(discussed above), but also the so-called press and person. experience.
Press refers to the relationship between the product and the On the other hand, fine-tuning actually updates network influence its environment has upon it (Rhodes 1961). Indi- weights, but it requires a potentially large training dataset.
viduals and their works cannot be isolated from the social Indeed, several current research efforts are in the direction and historical milieu in which their actions are carried out. of introducing adaptation for specific domains, tasks, cul-
Products have to be accepted as creative by society, and pro- tural frameworks, and so on. To be able to be part of the ducers are influenced by the previously accepted works, i.e., never-ending creative cycle mentioned above, LLMs should
the domain (Csikszentmihalyi 1988). The resulting system constantly adapt. Continual learning (Kirkpatrick et al. 2017; model of creativity is a never-ending cycle where individu- Shin et al. 2017) for LLMs (Sun et al. 2020; Wu et al. 2022)
als always base their works on knowledge from a domain, represents a promising direction, yet unexplored for creative which constantly changes thanks to new and valuable arti- applications.
facts (from different individuals). For example, individuals Finally, the person perspective covers information about generate new works based on the current domain; the field personality, intellect, temperament, habits, attitude, value
(i.e., critics, other artists, the public, etc.) decides which of systems, and defense mechanisms (Rhodes 1961). While those works are worth promoting and preserving; the domain several of the properties of press and process might be
is expanded and, possibly, transformed by these selected achieved—or at least simulated—by generative learning works; individuals generate new works based on the updated solutions, those related to the creative person appear out of
current domain; and then this cycle repeats. discussion (Browning 2023). Several works have analyzed
However, LLMs cannot currently adapt through multiple whether LLMs can pass tests intended to evaluate human iterations in the way described above; they just rely on one, psychological skills (Binz and Schulz 2023; Macmillan-
fixed version of the domain and generate works based on it. Scott and Musolesi 2024; Stevenson et al. 2022b), some-
The current generation of LLMs are immutable entities, i.e., times with promising results (Kosinski 2024; Lampinen once the training is finished, they remain frozen reflecting a et al. 2024). However, according to the best-supported neu-
specific state of the domain. In other words, they are not able roscientific theories of consciousness, current AI systems are to adapt to new changes. In-context learning can simulate not conscious (Butlin et al. 2023). As Ressler (2023) pointed
an adaptation to new states of the domain. The constantly out, LLMs have no self to which to be true when generatincreasing context length (Hsieh et al. 2024) allows research- ing text and are intrinsically unable to behave authentically
ers to provide more and more information to LLMs without as individuals. They merely “play the role” of a character re-training them, although a longer context might lead to or, more accurately, a superposition of simulacra within a
performance degradation (Li et al. 2024). This enables the multiverse of possible characters induced by their training representation of the current state of the domain through an (Shanahan et al. 2023; Shanahan 2024a). This results in a
adequate prompt, allowing the model to generate different perceived self-awareness, stemming from our inclination outputs according to environmental changes. For example, to anthropomorphize (Deshpande et al. 2023; Seth 2021).
in Park et al. (2023), multiple LLM-based agents interact In conclusion, all the properties listed above require some through natural language in a sandbox environment inspired forms of consciousness and self-awareness, which are dif-
by The Sims. Each agent stores, synthesizes, and applies ficult to define in themselves and are related to the hard relevant memories to generate believable behavior through problem introduced before. Creative-person qualities in gen-
in-context learning, leading to emergent social behaviors. erative AI might eventually be the ultimate step in achieving
The study of emergent behaviors of LLM-based agents at human-like intelligence.
the population level is an active research area (Guo et al.
2024). It is easy to imagine the simulation of creative or
# 5 Practical implications
artistic environments, such as a virtual multi-agent translation company (Wu et al. 2024), as well.
However, LLMs are like the main character of Memento: The application of large language models to fields like literathey always possess all the capabilities, but each time they ture or journalism opens up a series of practical questions.
“wake up”, they need to re-collect all the information Since LLMs can be used to produce artifacts that would be about themselves and their world. The time—or space—to protected if made by humans, a first concern is the definition

of legal frameworks in which they will be used. Copyright LLMs would diverge more consistently from existing works, for generative AI is currently a hotly debated topic (Gua- reducing the risk of capitalizing on others’ ideas. The lack
damuz 2017; Franceschelli and Musolesi 2022; Lee et al. of current copyright protection for generated works can also
2024; Miernicki 2021), due to the fact that current laws do foster such replacements for tasks where a free-of-charge not contemplate works produced by non-human beings (with text would be preferable to a high-quality (but still costly)
few notable exceptions (Bond and Blair 2019)). Copyright one. Finally, one last threat may be posed by human and applies to creative works of authorship (as referred to in artificial works being indistinguishable (Dehouche 2021).
the US Copyright Code), i.e., works showing a minimum The users obtaining such outputs might therefore claim them degree of originality (Gervais 2002) and reflecting author’s as the authors, e.g., for deceiving readers (Grinbaum and
personality (Deltorn 2017). As discussed earlier, current Adomaitis 2022), for cheating during exams (Fyfe 2023), or
LLMs might satisfy the first condition, but they cannot for improving bibliometric indicators (Crothers et al. 2023).
be considered creative persons, therefore missing the lat- Mitigation of such threats through dedicated policies8 or ter requirement. For this reason, works produced by LLMs designed mechanisms of watermarks (Kirchenbauer et al.
can be protected if and only if the original contribution is 2023) are already being developed.
provided by a human, e.g., the user who writes the prompt However, as we said, we believe that, overall, the impact that is used as input of the model, who in turn will be the of these technologies will be positive. LLMs also provide
rights holder. The definition of the criteria for classifying a several opportunities for creative activities. Given their charsource of originality is a fundamental problem since there is acteristics, humans are still required, especially for prompt-
a clear need to discriminate between protected and publicly ing, curation, and pre-/post-production. This means that the available works. role of writers and journalists may be transformed, but not
While a higher degree of novelty is unnecessary for claim- replaced. On the contrary, LLMs provide new opportunities ing protection, it might be crucial for other legal aspects. for humans, who will be able to spend more time validating
In particular, LLMs are trained in a supervised fashion on news or thinking up and testing ideas. LLMs can also adapt real data, which also include protected works (Bandy and the same text to different styles (see combinatorial creativity
Vincent 2021). Apart from questions upon the legitimacy in Sect. 3): by doing so, an artifact can be adapted to reach of such training (Franceschelli and Musolesi 2022), LLMs wider audiences. In the same way, LLMs also represent a
may learn to reproduce portions of them (Liang et al. 2023) valuable tool in scientific research (Fecher et al. 2023), espebecause of the memorization of training data (Carlini et al. cially for hypothesis generation (Gero et al. 2022).
2023). This would violate their reproduction or adaptation Indeed, we believe that LLMs can also foster human-AI right (Bonadio and McDonagh 2020). A different, creative- co-creativity (Lee et al. 2022), since they can be used to
oriented training approach should mitigate such risk, also write portions of stories to serve specific purposes, e.g., they facilitating fair-use doctrine application (Asay et al. 2020). can typify all the dialogues from a character, or they can
Whether or not LLM works obtain protection, we believe provide more detailed descriptions of scenes (Calderwood their societal impact will be tremendous (see also Newton et al. 2020). Dialogue systems based on LLMs can be used
and Dhole (2023)). We have a positive view in terms of the for brainstorming. In the same way, the generated responses applications of LLMs, but there are intrinsic risks related may augment writers’ inherently multiversal imagination
to their adoption. It is apparent that since LLMs are able to (Reynolds and McDonell 2021). LLMs can also represent a write articles or short stories, as the quality of their outputs source of inspiration for plot twists, metaphors (Chakrabarty
gets better and better, there is the risk that certain jobs in et al. 2023), or even entire story plans (Mirowski et al. 2022), the professional writing industry will essentially disappear even though they sometimes appear to fail in accomplishing
(Ponce Del Castillo 2023; Tamkin et al. 2021). However, these tasks at human-like level (Ippolito et al. 2022). Being we must remind that current LLMs are not as reliable as intrinsically powerful tools, through human-AI co-creation,
humans, e.g., they cannot verify their information and they LLMs may eventually allow the development of entire new can propagate biases from training data. In addition, the arts, as has been the case for any impactful technology in the
quality of the output strictly depends on the prompt, which past centuries (Eisenstein 1979; Silva 2022).
might in turn demand human skills and more time. Writers can be threatened as well. Though not in violation of copy-
right, LLMs may exploit certain ideas from human authors, capitalizing on their efforts in ways that are less expensive
or time-consuming (Weidinger et al. 2022). The questionable creative nature of LLMs discussed so far might suggest
artificial works to be of less quality than humans, therefore not providing a real threat. Nonetheless, more creative 8 https:// bigsc ience. huggi ngface. co/ blog/ the- bigsc ience- rail- licen se.

# 6 Conclusion

The latest generation of LLMs is attracting increasing interest from both AI researchers and the general public due to the
astonishing quality of their productions. Questions naturally arise around the actual creativity of these technologies. In this
paper, we have discussed whether or not LLMs can actually be deemed as creative; we started by considering Boden