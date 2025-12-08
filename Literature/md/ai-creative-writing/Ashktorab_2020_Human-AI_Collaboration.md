---
source_pdf: Ashktorab_2020_Human-AI_Collaboration.pdf
converted_date: 2025-12-04T20:08:50.864183
total_pages: 20
model: Google Gemini 2.0 Flash
total_cost_usd: $0.005283
prompt_tokens: 20,059
completion_tokens: 8,192
---

# Human-AI Collaboration in a Cooperative Game Setting:
Measuring Social Perception and Outcomes
ZAHRA ASHKTORAB, IBM Research AI, USA
Q. VERA LIAO, IBM Research AI, USA
CASEY DUGAN, IBM Research AI, USA
JAMES JOHNSON, IBM Research AI, USA
QIAN PAN, IBM Research AI, USA
WEI ZHANG, IBM Research AI, USA
SADHANA KUMARAVEL, IBM Research AI, USA
MURRAY CAMPBELL, IBM Research AI, USA

Human-AI interaction is pervasive across many areas of our day to day lives. In this paper, we investigate human-AI collaboration in the context of a collaborative AI-driven word association game with partially
observable information. In our experiments, we test various dimensions of subjective social perceptions
(rapport, intelligence, creativity and likeability) of participants towards their partners when participants believe they are playing with an AI or with a human. We also test subjective social perception of participants
towards their partners when participants are presented with a variety of confidence levels. We ran a large scale study on Mechanical Turk (n=164) of this collaborative game. Our results show that when participants believe
their partners were human, they found their partners to be more likeable, intelligent, creative and having more rapport and use more positive words to describe their partner’s attributes than when they believed they were
interacting with an AI partner. We also found no differences in game outcome including win rate and turns to completion. Drawing on both quantitative and qualitative findings, we discuss AI agent transparency, include
design implications for tools incorporating or supporting human-AI collaboration, and layout directions for future research. Our findings lead to implications for other forms of human-AI interaction and communication.

CCS Concepts: • **Human-centered computing → HCI design and evaluation methods; Natural language interfaces; Interactive systems and tools; Empirical studies in interaction design; User studies; User
interface design.**

Additional Key Words and Phrases: Games, AI, Agents, Collaboration, Social Perception

ACM Reference Format:
Zahra Ashktorab, Q. Vera Liao, Casey Dugan, James Johnson, Qian Pan, Wei Zhang, Sadhana Kumaravel, and Murray Campbell. 2020. Human-AI Collaboration in a Cooperative Game Setting: Measuring Social
Perception and Outcomes. *Proc. ACM Hum.-Comput. Interact.* 4, CSCW2, Article 96 (October 2020), 20 pages.
https://doi.org/10.1145/3415167

Authors’ addresses: Zahra Ashktorab, IBM Research AI, Yorktown, NY, USA, zahra.ashktorab1@ibm.com; Q. Vera Liao, IBM
Research AI, Yorktown, NY, USA, vera.liao@ibm.com; Casey Dugan, IBM Research AI, Yorktown, NY, USA, cadugan@ us.ibm.com; James Johnson, IBM Research AI, Cambridge, Massachusetts, USA, jmjohnson@us.ibm.com; Qian Pan, IBM
Research AI, Cambridge, Massachusetts, USA, qian.pan@us.ibm.com; Wei Zhang, IBM Research AI, Yorktown, NY, USA, zhangwei@us.ibm.com; Sadhana Kumaravel, IBM Research AI, Yorktown, NY, USA, sadhana.kumaravel1@us.ibm.com;
Murray Campbell, IBM Research AI, Yorktown, NY, USA, mcam@us.ibm.com.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2020 Association for Computing Machinery.
2573-0142/2020/10-ART96$15.00 https://doi.org/10.1145/3415167

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020. 96

96:2 Zahra Ashktorab et al.
# INTRODUCTION
As AI is becoming more pervasive in today’s society, it is being used more in collaborative settings, replacing work a human collaborator may have been used for in the past. This includes customer
support applications where chatbots are being increasingly employed, for example in empowering low health-literacy patients in hospitals using virtual nurse agents [8], pedagogical systems for
tutoring [24], or even creative endeavors such as collaborative writing [16] or art [37]. In computermediated communication in which collaboration is taking place between people, HCI researchers
have done much work on determining what can lead to many successful collaborations and outcomes, including distance, diversity or inter-generational challenges [25, 39, 49]. Other factors
that have been explored are social perceptions between collaborators [46, 54]. As we move into a world of Human-AI collaboration, these perceptions and how they impact the outcomes of the
collaboration are not yet well understood. In this work, we study the differences between human-AI and perceived human-human social perceptions in a collaborative interaction setting.

One opportunity for studying user perceptions of AI agents in cooperative games are Cooperative
Partially Observable games. Cooperative Partially Observable games (CPO) require players to cooperate with one another, especially since there are aspects of the game that are only partially
observable [32]. AI research has made strides on competitive games, showing improvements for games like chess, checkers, and poker [9, 13]. More recently however, there has been an interest in
the investigation of Cooperative Partially Observable games that are AI-driven. These cooperative games require users to coordinate, cooperate and communicate with an AI agent in ways that their
actions are deemed interpretable and interpret the actions of the AI agent. [33]. These cooperative games require consideration of theory of mind. In this paper, we introduce a cooperative game that
requires the user to interpret an AI agent’s clues as there is information withheld from the user.

We studied collaboration between humans and AI in the context of a real-time, interactive collaborative word guessing game. Due to the cooperative nature of the game objective (i.e. guessing
a target word based on a partner’s clues) and the clear notion of success (i.e. win/loss) in this setting, the game afforded us a unique opportunity to study human-AI collaboration. Further, due
to the constrained interactions between partners in the game, we were able to study how social perceptions differ when players believe they are playing with AI versus another human. Prior work
investigating social perception of AI agents was not in a truly collaborative setting. [8, 26, 50, 56].

Our work is not interested in the intentional anthropomorphizing of a system, but the effect of identity disclosure and the effect of that identity on outcomes and social perception of AI or human
partner in a collaborative environment.

Our findings show that even while the same AI agent plays across all conditions (i.e. during game play the “human” partners interacted just as the “AI” partners interacted), if people perceive they are
playing with a human partner, as opposed to AI, and they believed their partners to be human, they find their partner more intelligent, creative, and likeable. This potential “bias” against an AI partner
on dimensions of social perception does not seem to effect collaboration outcomes, however. We also report on findings around transparency (i.e. confidence scores) that can lead to more positive
social perception of AI agents. We discuss AI agent disclosure and transparency, share design implications from these findings and believe our research leads to new insights and topics for
researchers to study how Human-AI collaboration is similar to and different from Human-Human collaboration and even methodology implications for how to run experiments in this space.

In this paper, we investigate the following research questions:

**RQ1** How does a participant’s belief in whether they are interacting with an AI or a human affect social perceptions of their partner?

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

Human-AI Collaboration in a Game Setting: Measuring Social Perception and Outcomes 96:3

**RQ2** How does a participant’s belief in whether they are interacting with an AI or a human affect game performance/outcome of the collaboration?

**RQ3** How does a partner’s confidence level affect social perceptions of their partner?

**RQ4** How does a partner’s confidence level impact game performance/outcome of the collaboration?

# RELATED WORK
Our inquiry is motivated by the prevalent use of AI systems in human-AI collaborative environments.
Previous research has studied both human-human collaboration through computer mediated communication [19, 29, 31] and human-AI interaction [8, 24]. This research builds on prior work by
investigating collaboration between humans and AI in real time, measuring collaboration outcomes, and social perceptions of human/AI partners.

## Cooperative Games with Partially Observable Information
Few studies have looked at the social perception of the agent in the context of a cooperative partially observable (CPO) game [61]. Liang et al. investigated implicature communication in
Hanabi, a cooperative partially observable game [36] that has been studied in AI literature as
CPO [33]. In their study they found that an Implicature AI, i.e. one that implicitly communicates information, led to a more successful outcome than non implicature AIs. This paper is one of the
first to begin exploring interactions between users and agents in cooperative partially observable games. In this study, we explore social perception of an AI agent and outcome of a game. There
have been many AI-infused word association games developed, resulting in studies on how users understand, interact and communicate in these games [62]. Games like the ‘Taboo’ word game
[48] “forces agents to speculate about their partner’s understanding of the domain, rather than just performing inference on their own knowledge”, and similarly for “Hanabi” [4]. There has been
work in which AI agents have been trained to play these games as a way of testing theories around how people interact and communicate, but ultimately as a contribution to furthering Artificial
Intelligence research [1, 17, 27]. Other research has investigated communication in games like
‘Password’ and found that people playing both roles (speakers and hearers) are collaborative and considerate of one another [63].

## Human-AI Collaboration
The term “human-AI collaboration” has emerged in recent work studying user interaction with AI systems [2, 11, 45, 58]. This marks both a shift to a collaborative instead of automated perspective
of AI, and the advancement of AI capabilities to be a truly interactive and collaborative partner in some domains. For example, utilizing deep learning technologies that can reach human comparable
performance in drawing, Oh et al. explored user experience in drawing pictures collaboratively with
AI [45]. They found that while people perceived the AI to be low in predictability, controllability, and comprehensibility, they enjoyed the collaborative experience. Wang et al. surveyed data scientists
on their attitudes toward AI systems automating data science projects and found they remain optimistic about a collaborative future with such technologies [58]. A collaborative framework
has also been used to study AI-assisted decision systems to understand how to improve human-AI joint decision outcomes [65], users’ onboarding needs to facilitate the collaboration [10] and the
appropriate level of human and AI contributions in a collaboration [30, 38].

In this paper, we study cooperative games as a new domain of human-AI collaboration. Games are both an important application domain of AI and frequently used as a testbed for state-of-the-art
AI algorithms [13, 23, 53, 55], leading to current game-playing AI reaching human-comparable

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

96:4 Zahra Ashktorab et al.
performance. Meanwhile, the user experience of gaming includes unique aspects to consider for a collaborative partner. One of the aspects we focus on in this paper is the social perception, the
impression people form about the AI, especially in terms of human-like social characteristics.
Unlike purely utility tools, such as decision-support AI, game-playing AI applications often adopt anthropomorphic designs or even disguise as human players [18]. Such designs are not only of
hedonic value but could also affect gamer behaviors, such as cooperative attitudes and decisions with AI [28].

Outside collaborative and gaming contexts, research on embodied conversational agents and robots have focused on how the embodiment and anthropomorphic design of agents (not necessarily
AI-powered) affect people’s social perception. Prior work investigated how people anthropomorphize and attribute social characteristics to robots in general [21]. For example, multiple scales
were developed to measure people’s self-reported social perception of robots [5, 14] including likability, perceived intelligence, warmth and competence. A bulk of literature studied the effect
of embodiment, e.g., adding a talking head or full-fledged virtual body to a system, on people’s social perception and task performance for pedagogical tools [8, 34], soliciting questionnaire re-
sponse [56], autonomous driving [26], group decision support [50] and so on. A meta-analysis of literature on the topic concluded that embodiment enhances social perception but the effect on
task performance is small [64]. Research also explored other anthropomorphic design of agents such as personality [35], and using emoji [6].

Our work differs from prior work in that we are not interested in design that intentionally anthropomorphizes computing systems, but the effect disclosure of AI-identity, for an AI partner
that has human-comparable performance, has on people’s social perception and performance. A few recent works explored the effect of disclosure. Focusing on cooperative behavior in a repeated
prisoner’s dilemma game, Ishowo-Oloko et al. found that disclosing the bot nature averts people’s tendency to cooperate, and participants do not recover despite experiencing cooperative attitudes
exhibited by bots [28]. Shi et al. found that compared to a human identity, people are less persuaded by a chatbot even when the same dialogue are used [52]. Interestingly, it is not the displayed
identity but the perceived identity that impacts the outcome, as people still suspected the identity of the agent, despite the display.

Our work is also informed by CSCW and HCI research that explored the factors that can lead to successful collaboration outcomes through computer mediated communication [25, 39, 49],
including investigating social perceptions between collaborators [46, 54]. CMC and AI-MC research informs us that people interpret signals they see online to form impressions about other humans-
but what are the signals used to draw conclusions in human-AI collaboration and communication?
According to the Hyperpersonal Model [57] humans over-interpret cues in computer-mediated communication to form impressions about their partners. Jakesch et al. coin the term replicant
effect, that only when individuals do not know whether content has been generated by a human or
AI, they mistrust the AI less than the humans [29].

Researchers have been interested in impressions of users towards these intelligent systems and even how they form mental models of these systems [22]. In prior work for example, the mental
model of an AI agent is described as having three components: AI Knowledge: described as the
AI’s knowledge of various topics, Local Behavior: described as an AI’s behavior of an individuals output, and Global Behavior described as the AI’s behavior at large [22]. In the context of our
collaborative word guessing game setting, for example, an example of Local behavior is the memory of prior guesses by an individual within one game, where as an example of global behavior is the
memory of guesses and user behavior across multiple games.

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

Human-AI Collaboration in a Game Setting: Measuring Social Perception and Outcomes 96:5

## System Confidence and Expectation Setting
Research on AI systems has focused on explainability and trust. Many studies investigating explainability have explored the role of system transparency, particularly user-perception of the system’s
confidence or certainty in its response or output. Furthermore, many systems can set expectations by showing AI confidence levels to users. Prior research has shown that setting expectations
impacts user satisfaction towards technologies [15, 59, 60]. Kocielnik et al. introduce the accuracy indicator, a chart that communicates the accuracy of the AI. They find that including an accuracy
indicator lowers user expectations with respect to the system performance. A number of theories regarding expectation setting have been proposed [7, 15]. One theory that has been tested in many
HCI studies is the Expectation Confirmation Model (ECM) [7], which suggests that user satisfaction is directly related to user expectations of the system. Specifically, if a user expects more than the
system is capable of delivering, the user will ultimately not be satisfied with the system.

# SYSTEM DESIGN OF WORD GAME: A COOPERATIVE WORD GUESSING GAME
To learn about user perceptions of their opponent in a collaborative setting, we used a simple two-person collaborative game we call Wordgame. In Wordgame, the opponent has a target word
and gives clues to their partner so that their partner guesses the target word. We refer to the player who is giving hints as the “giver” and the player who is guessing as the “guesser”. The game begins
with the AI starting the game with a hint like “car”. After every hint, the player inputs a guess.
In this example, the target word is “engine”. The player gets 10 attempts to guess before they lose. If the player inputs the correct word, they win. Figure 1 shows a typical round. Wordgame is
cooperative, meaning partners work together for the “guesser” to correctly guess the target word.
The cooperative nature of this game means that partners are open and honest in achieving a shared goal.

## AI Agent Description
The AI used to play the Wordgame was developed by a team of researchers. The researchers developed two AI agents, one for the giver role (AI has the target word and provides hints to the
user) and one for the guesser role (user has the target role and provides hints to the AI). Below, we describe the high-level technical details of the AI agent. The Giver AI generates candidate
hints using free association norms, word embeddings, and WordNet [47] (a collection of word level features like antonyms, synonyms, hypernyms etc). Hints are scored based on a Gradient Boosting
Machine (Supervised Machine learning) model trained on Taboo cards(taboo words as clues).
Upon receiving a guess, it reranks the candidates based on which is closer to the target than the previous guess. Candidate guesses are generated using free association norms, word embeddings,
and WordNet, and scores them based on a GBM (supervised machine learning) model trained on free association norms (as hints). On receiving a hint, the guesser finds the intersecting words of
the hint and the previous hints based on paths in a knowledge graph and ranks them based on the model. The giver agent uses a secret word to generate candidates using the Candidate Generation
features (Free Association Norm, WordNet and Word embeddings), scores the candidates based on a GBM model trained on words from Taboo cards as hints and outputs the candidate with highest
score as next clue. Upon receiving a new guess, the giver agent re-scores the candidates treating the new guess as secret word and outputs the candidate which is closer to the target than the guess.

The AI response typically takes 2-3 seconds. Across all conditions we added a delay of 2 more additional seconds. Wordgame is a collaborative game because users have to interpret the clues
given by the AI to guess the target word. Building cooperative games with imperfect information

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

96:6 Zahra Ashktorab et al.
is a “new frontier for AI research” and requires an elevation of reasoning about the beliefs and intentions of other agents, requiring a consideration of theory of mind [4].

In this paper, we approach our research questions in the context of the AI agent playing the giver role and the participants in the study playing the guesser role (AI agent gives hints and participants
submit guesses for the target word). The two roles (giver and guesser) have slightly different actual and intended behaviors, so we focus on one role to answer our research questions and conduct our
experiment.

Fig. 1. Game interface detail. On the left, the target word is “plastic” in the consistently high confidence condition. The participant is told they are playing against an AI. On the right, the target word is “school” In
this condition, participant is told they are playing against another person in the consistently low confidence condition. Red squares in each interface delineated differences (giver avatar, robot image, and prompt about
partner).

# METHODOLOGY
To better understand how confidence and whether users believed they were playing with an AI agent or a human impacted how they characterized their partner, we ran a large-scale on study on
Amazon Mechanical Turk. For this study we limited participants to playing as the guesser and the
AI agent to play as the giver.

Each participant played 5 rounds with five different words. For each round, participants were allowed a maximum of 10 guesses. If they did not guess the target word correctly after 10 attempts,
they lost the round and moved to the next target word. The decision to limit the number of attempts was motivated by findings in previous studies that demonstrate user frustration when the number
of attempts are not limited [22]. Based on these previous findings and to reduce user agitation and maximize the use of participant time, we limited the maximum length of the game. We looked at
how the following factors impacted user perceptions of their opponent:
• Whether participants were told their partner was: an AI agent, a human, or undisclosed
• Their opponent’s confidence: consistently high, consistently low, none displayed, or mixed

Participants were either told they were playing with an AI agent, they were playing with another human, or they might be partnered up with a human or an AI agent. Before being assigned to their
opponent, they saw a configuration page that informed them of the nature of their opponent (See
Figure 2). Participants were also assigned conditions related to confidence transparency. They were either shown consistently high confidence (75-100) shown in green on every turn, consistently low
confidence (0-25) shown in red on every turn, mixed confidence across the turns, or no display of confidence. Participants were told that confidence is a self-report of how confident their gameplay

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

Human-AI Collaboration in a Game Setting: Measuring Social Perception and Outcomes 96:7 partners (AI, human, undisclosed) are of each clue. Every time a new clue was given by the agent,
a new confidence value within the interval for that condition (consistently high, consistently low, or mixed) was communicated to the user. The colors communicated are colors typically used to
express positive settings (high confidence = green), negative settings (low confidence = red) [41].
One reason for using this color scheme was to ensure that participants noticed the variations in the interfaces so that we could accurately measure the conditions to which they were assigned. The
robot avatar appearing during the AI agent condition meant to also more clearly communicate that the user was interacting with a bot and not a human. Two variations of a partner’s confidence
level are shown in in Figure 1. This was a between-subjects study. Upon registering their Amazon worker ids participants could no longer participate in the HIT. There is some degree of deception
in the study and we wanted to prevent the same player participating in multiple conditions as to make the experimental design as reliable as possible.

Fig. 2. Configuration page. Participants were told they were either playing with an AI, with another person, or that they may be matched with a human or an AI.

For all players, we used one word list of five words and balanced it for difficulty: “school”, “music”,
“plastic”, “ring”, “sun”. Similar prior work [22] used a similar metric (accessibility index of words, a measure from [42]) to balance for word difficulty. Gero et. al compared user mental model of AI
agents in a collaborative word game to win rate. Using two different sets of words balanced for word difficulty, they found similar results. The game was developed into an online web application
using Flask (a lightweight Python framework for web apps) and React (a Javascript library for building front-end interfaces).

Participants played a game of 5 rounds and they took a survey (described in the following section).
In pilot studies, the average time of completion was 15 minutes. Based on this all participants were paid $3.00 commensurate with federal minimum wage.

## Data Validation
We performed several attentiveness tests to preserve the integrity of the data collected. We excluded those who did not pass the linguistic attentiveness task [40] and workers whose time for finishing
the survey portion of the task was less than 15 seconds. We also excluded those whose average ratings for trustworthiness, rapport, creativity, and intelligence fell outside the mean ± 2D statistic
of participant averages. This left us with 164 subjects.

# SURVEY INSTRUMENT
We asked participants about demographics, their prior experience with Artificial Intelligence, as well as their prior experience with word games. To ascertain whether participants felt that they
were competing against a human or an AI (though in several conditions we told them explicitly whether their partner was an AI or a human), we also collected an AI score as done in [29], in
which we asked participants about whether they believed they were interacting with a human or an AI in two questions on a 7-point Likert scale. The AI score is the average of those two questions.
We further asked participants to provide open-ended reasons for their AI score. We also asked

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

96:8 Zahra Ashktorab et al.

Social Perception Index | Cronbach 𝛼 | Mean | SD
--- | --- | --- | ---
Intelligence | 0.79 | 5.13 | 1.49
Rapport | 0.95 | 4.65 | 1.38
Likeability | 0.97 | 4.61 | 1.35
Creativity | 0.95 | 4.17 | 1.09

Table 1. Cronbach Alpha, Mean, and SD for each Social Perception Index, N=164

participants to list three attributes they would use to describe their partner and provide reasons for why they selected those attributes.

## Dependent Variables: User Perception of Opponent
To address our research questions, we assessed user perception of rapport, likeability, intelligence and creativity of the opponent. Based on previous work [43], we asked participants to indicate
how much they agreed/disagreed with statements like, “My opponent was not paying attention to me,” “My opponent and I worked towards a common goal,” and “I feel that my opponent trusts me.”
To measure the other dimensions in our research questions (likeability, intelligence, creativity), we used a list of semantic differential scales. We adapted scales on these dimensions by [5, 44, 50].
Participants were asked to rate their opponent on pairs of antonyms (i.e. unfriendly/friendly, unpleasant/likeable, ignorant/knowledgeable). All of the perception questions were asked based
on a 7 point Likert scale. The averages for perception dimensions were calculated for analysis.

Following past studies [5, 44, 50], we combined the items for an Intelligence/Rapport/Likeability and Creativity index by calculating their mean (see Table 1), reliable and consistent with prior
work). Below, we list the dependent variables measured in the post-survey.
• **Intelligence** To measure intelligence, we used a list of four semantic differential scales also used in [5, 44, 50], in which participants rated their opponent on a team 7 point Likert
scale as Unintelligent/Intelligent, Ignorant/Knowledgeable, Incompetent/Competent, and
Irresponsible/Responsible. The intelligence value was an average of these four scales.
• **Rapport** We measured rapport by adapting an instrument from [43], in which participants rated items like “My opponent seemed engaged” or “My opponent and I worked towards
a common goal” on a 7 point Likert scale. To measure rapport, we asked nine questions in which participants responded with Strongly Disagree/Strongly Agree.
• **Likeability** To measure likeability, we used five semantic differential scales, also used in [5, 44,
50] in which participants rated their opponent on a 7 point Likert scale as unfriendly/friendly, not kind/kind, unpleasant/pleasant, not cheerful/cheerful and dissimilar to me/similar to me.
• **Creativity** To measure creativity, we used three semantic differential scales in which participants rated their opponent on a 7 point scale as not funny/funny, not creative/creative, and
unique/ordinary.

# RESULTS
When people interact with a human opponent or they interact with an AI opponent, do they have different social perceptions (rapport, likeability, creativity and intelligence) of their opponent? Five
regressions were calculated to predict these measures (intelligence, likeability, creativity, rapport, and gameplay) based on the assigned partner (human, AI, undisclosed) and the confidence of the
partner (high, low, mixed, none), AI Score, and demographic variables including education, prior exposure to Artificial Intelligence, and prior exposure to word games. Results can be seen in Table
2.

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

Human-AI Collaboration in a Game Setting: Measuring Social Perception and Outcomes 96:9

## AIScore: Perceived Partner Type
Often, in studies in which users are told they are interacting with humans/AI and they are not (i.e.
some level of deception involved), participants mistrust the conditions and do not believe them.
Additional metrics must be collected to affirm whether participants believed the conditions or to include during analysis to gain a better understanding of all the results. A study investigating
how identities and inquiry strategies influence a conversation’s effectiveness used deception and found that participants did not believe the conditions of the study. For example, only 34.3% of
participants who were told they were interacting with a human believed they were interacting with a human. The authors used a similar approach employed in this paper, by using perceived
identity to model their dependent variable [52]. These results further motivated us to include the
AI score as a dependent variable in our models, as done in prior work using deception in disclosure of AI identity [52]. In this paper, we investigate whether a participant believed whether they were
interacting with a human or an AI impacted gameplay and subjective social perceptions. Thus, it is not enough that we simply look at the conditions we assigned to participants (See Figure 2), since
not all participants were convinced that they were competing against an AI or an agent. In fact, only 35% of those individuals who we told were interacting with a human in the study believed
they were interacting with a human more than an AI (>4.5 on post-survey 1-7 Likert scale). To account for this, we added the AI score, a continuous independent variable, to the model. AI score
is calculated based on the average of two questions in our post survey that asked participants about whether they perceived their opponent to be human or AI (on a 7 point Likert scale). We keep
assigned identity in the model because of the possibility that there may be a “suspicion” effect with the same perceived identity in different manipulated conditions, i.e. people are suspicious when
we tell them they are interacting with a human, or when we do not disclose with whom they are interacting. We calculated a linear regression for each of the dependent variables and present the
results below.

## Demographics and Previous Experience
We asked participants about their demographics (language, education) and previous experience with AI: “What kind of exposure have you had to Artificial Intelligence (AI)” (1=I don’t know what
machine learning is., 7=I have implemented a Machine Learning Algorithm) (M=4.7, SD=1.4), as well as prior experience with word games: “How familiar are you with word games like Scrabble, Taboo,
crosswords, etc.?” (1=I never play word games. 7=I play word games every day) (M=4.7, SD=1.2).
We asked these questions on a 7 point Likert scale. We present other demographic information of our participants in Table 3.

## Subjective Social Perception of Opponent
When people are presented with a human partner or an AI partner, do they perceive one as more intelligent, creative, likeable, and have more rapport with one than the other? We conducted a
regression to compare the effects of perceived opponent, confidence (low, high, mixed, none), and assigned opponent as part of the condition (human vs. AI. vs. not disclosed) (see Figure 2) and
their interaction on perceived intelligence, rapport, likeability and creativity. We treat intelligence, rapport, likeability, creativity and gameplay win rate as dependent variables in our models and
describe the results for each below. The details of the each regression are included in Table 2, with details in the subsections below.

### Intelligence.
A multiple regression was calculated to predict intelligence based on AI score of the partner, the assigned role (human, AI, undisclosed) and the confidence of the partner
(high, low, mixed, none), and demographic variables. A significant regression was found F(17,146)=15.22,

*Proc. ACM Hum.-Comput. Interact.*, Vol. 4, No. CSCW2, Article 96. Publication date: October 2020.

96:10 Zahra Ashktorab et al.

Dependent Variable | Significant Effects | 𝛽
--- | --- | ---
Intelligence | Role of Agent: Undisclosed | -1.98**
 | Role of Agent: Human | -1.46***
 | AI Score | 0.42***
 | AI Score x Role of Agent: Human | 0.26*
 | AI Score x Role of Agent: Undisclosed | 0.33*
 | Exposure to AI | -0.22***
 | 𝑅2=0.64*** | 
Likeability | Prior Experience with Word Games | 0.11*
 | AI Score | 0.51***
 | 𝑅2=0.75*** | 
Rapport | Role of Agent: Human | -1.08*
 | Role of Agent: Undisclosed | -1.51***
 | AI Score | 0.37***
 | AI Score x Role of Agent: Human | 0.20*
 | AI Score x Role of Agent: Undisclosed | 0.31**
 | 𝑅2=0.58** | 
Creativity | Exposure to AI | 0.10*
 | AI Score | 0.34***
 | 𝑅2=0.65*** | 
Gameplay Win Rate | 𝑅2=0.15 | 
Significance Codes: ***p<0.001, **p<0.01, *p<0.05

Table 2. Regression predicting dependent variables (subjective social perception of opponent) and gameplay win rate based on assigned conditions: assigned role (human, AI, undisclosed), assigned confidence (high,