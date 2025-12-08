---
source_pdf: Chakrabarty et al..pdf
converted_date: 2025-12-04T11:48:12.166177
total_pages: 16
model: Google Gemini 2.5 Flash
total_cost_usd: $0.047056
prompt_tokens: 18,054
completion_tokens: 16,656
---

# Help me write a poem: Instruction Tuning as a Vehicle for Collaborative Poetry Writing

TuhinChakrabarty$^1$$^*$ VishakhPadmakumar$^2$$^*$ HeHe$^{2,3}$
$^1$DepartmentofComputerScience,ColumbiaUniversity
$^2$CenterforDataScience,NewYorkUniversity
$^3$DepartmentofComputerScience,NewYorkUniversity tuhin.chakr@cs.columbia.edu, vishakh@nyu.edu, hhe@nyu.edu

## Abstract
Poem Draft Interactions
Recent work in training large language mod-
Write a simile about 'cake' els(LLMs)tofollownaturallanguageinstruc-
A cake is like a cloud of joy.
tionshasopenedupexcitingopportunitiesfor A cake is like a piece of heaven.
natural language interface design. Building The cake is like a cloud of joy.
Suggest a verse to follow the on the prior success of LLMs in the realm of sentence 'The cake is like a
computer-assisted creativity, we aim to study cloud of joy' if LLMs can improve the quality of user- The frosting is like a rainbow.
So soft so fluffy, I could cry.
generated content through collaboration. We The cake is like a cloud of joy.
The frosting is like a rainbow.
presentCoPoet,acollaborativepoetrywriting system.Incontrasttoauto-completingauser’s
text, CoPoetiscontrolledbyuserinstructions
The cake is like a cloud of joy.
that specify the attributes of the desired text, The frosting is like a rainbow. Write a poetic sentence that suchasWriteasentenceabout‘love’orWrite One slice is heaven on Earth, contains the word 'chocolate'
and ends in 'volcano' a sentence ending in ‘fly’. The core compo-
A flowing chocolate volcano.
nent of our system is a language model fine- The cake is like a cloud of joy. I ate so much chocolate and
The frosting is like a rainbow. erupted like a volcano.
tunedonadiversecollectionofinstructionsfor One slice is heaven on Earth, poetry writing. Our model is not only com- A flowing chocolate volcano.
petitive with publicly available LLMs trained oninstructions(InstructGPT),butisalsocapa-
bleofsatisfyingunseencompositionalinstruc- Figure 1: A collaborative poem entitled ’Decadence’, tions. A study with 15 qualified crowdwork- written with CoPoet assistance. Greentext was writ-
ersshowsthatuserssuccessfullywritepoems ten directly by the human, who interacts with CoPoet with CoPoet on diverse topics ranging from usinginstructions. CoPoetoffersmultiplesuggestions
Monarchy to Climate change. Further, the whichtheusercan accept or reject. Theuserwrote collaborativelywrittenpoemsarepreferredby a four line poem before indicating completion of the
third-party evaluators over those written with- task.
outthesystem.

# 1 Introduction
Theadoptionofthesetechnologieshingesontheir
Advancements in large language models (LLMs) abilitytoprovideappropriatesuggestionswhilebe-
havemaderemarkableprogresstowardsgenerating ingeasytointeractwith. However,therehasbeen
coherent text in a wide variety of domains. This limited research on the effectiveness of such col-
hasspurredincreasinginterestincomputer-assisted laboration,e.g.,whethertheassistantunderstands
creativity(Seeetal.,2019;ElkinsandChun,2020; user intents and whether collaboration improves
Rameshetal.,2022;Branwen,2020)suchasbuildthefinaloutcome.
ingco-creativeassistantsforwritingstories,poems,
Inthispaper,weaimtounderstandthecollaboandargumentativeessays(Leeetal.,2022;Swan-
rationcapabilitiesofLLMsthroughacasestudyof sonetal.,2021;Uthusetal.,2019;Donahueetal.,
collaborativepoetrywriting. Writingapoemisof-
2020;PadmakumarandHe,2022;Duetal.,2022).
tenachallengingtaskbecauseitisbothopen-ended andhighlyconstrained. Unlikestoriesorotherar-
$^*$BothAuthorsContributedEqually gumentativetexts,inordertowriteapoemweneed
$^1$Ourcode,preprocesseddata,models,andtheinteraction creative content that satisfies various long- and
logsfromouruserstudyareavailableathttps://github.
com/vishakhpk/creative-instructions short-rangeformconstraintssuchasrhyme,meter, arXiv:2201.13669v1 [cs.CL] 31 Jan 2022

andsound,whichposesasignificantchallengefor Writeapoeticsentenceabout‘sun’
Subject end-to-endpoemgenerationsystems(Ghazvinine- Ocrimsonsun,yourwarmingdraft’spulsa-
tion.
jadetal.,2016;TianandPeng,2022;VandeCruys,
Writeapoeticsentenceendingin‘glory’
2020;Ormazabaletal.,2022). WhileLLMssome- End
AmIexaltedhereuntothatglory.
timesstrugglewithlong-rangecoherence,theyare goodatprovidingvariationsoftextthatsatisfylo- Writeapoeticsentencethatendsinaword
Rhyme whichrhymeswith‘replace’ cal constraints. This makes them great partners
Diminishingforme,withdelicategrace.
tohumansinpoemwriting, wherehumansfocus
Writeanextsentenceinapoemgiventhe on the long-range writing plan and the machine
previoussentence‘‘TheonlythingIknow’ implementstheideaslocally. Next
‘forsure’
Effectivecollaborationinco-creativewritingis Sentence
Isthatloveishardandcanbeobscure.
challengingasitrequiresthemodeltounderstand
Writeametaphorabout‘brain’ userintention. Forexample,asshowninFigure1, Metaphor
Mybrainisatangledmessofcircuits.
a user may have a rough plan around two related
Writeasimileabout‘makingsomeonefeel conceptssuchaschocolateandvolcano,andwant
Simile desired’ themodeltosuggestaversethatcontainschocolate
Iwanttomakeyoufeellikeaflowernear andendswithvolcano;ortheymaylookingfor
ahummingbird aversethatrhymeswithaspecificword(rainbow)
Writeapoeticsentenceabout‘bottles’ tosatisfytheconstraints. Anauto-completionin- Onoma-
showcasingonomatopoeia topoeia
terfaceisnotabletoanticipatesuchuserneedsand Thestampingoffeetandtheringofbottles.
providetargetedsuggestions. Toenablericherin-
Writeapoeticsentenceabout‘tears’and
Subject teraction,werelyoninstructionalprompts(Wang
endingin‘wives’
+End etal.,2022;Sanhetal.,2021;Mishraetal.,2022; Awashinthetearsofsoldier’swives.
MishraandNouri,2022)thatactasanaturallan-
Table 1: Natural language instructions for poem writguageinterfacebetweentheuserandtheassistant.
ingpairedwithexampleoutputs. Eachinstructioncon-
Specifically,wepresentCoPoet,acollaborative sistsofatemplateandanargument.
poemwritingsystemwithanaturallanguageinterface. Duringawritingsession,theusercanitera- (AMT)whereCoPoetassistsexpertcrowdworkers
tivelyrequestsuggestionsthroughnaturallanguage (recruited through a qualification test) in writing instructions such as Write a simile about ‘cake’, poems(Section4). Weobservethattherecruited
andedittheirdraftbasedonthesuggestions(Fig- usersareabletowritecoherentandcreativepoems ure1). TobuildCoPoet,wefinetuneapretrained ondiversetopicsrangingfromGlassCeilingtoCli-
sequence-to-sequencemodelonaparallelcorpus mateChange. About70%ofmodelsuggestedtext ofinstruction-outputpairs. Weobtaintheoutputs isretainedinthefinalpoemandusersgiveCoPoet
frompubliclyavailabledatasetsofcreativetextand aratingof4.3outof5onboththesuggestionqualsynthesizethecorrespondinginstructionsbyrules, ityandtheoverallhelpfulness. Further,aseparate
includingbothlexicalandrhymingconstraintsas groupofannotatorsonAMTprefersthecollaborawellasrequestsonrhetoricaldevices. tivelywrittenpoemsmoreoftenthanthosewritten
without CoPoet assistance. In particular, we find
To understand how well the model follows inmodelassistanceimprovesrhymingandvocabulary
structions, wetestit oninstructionswithvarying diversityofthepoems.
levelsofdifficulty,fromthoseseenduringtraining tounseencompositionalinstructionsthatcontain
multiple constraints. Both automatic and human
# 2 Data
evaluationshowthatourfinetunedmodelsatisfies To train a model to follow instructions, we need theconstraints86%ofthetime,10%betterthana <instruction, poem_line>pairswherethetext
muchlarger175BversionofInstructGPT(Brown satisfiestheinstruction. Thekeychallengetobuildetal.,2020). Onunseencompositionalinstructions, ing such a model is the lack of parallel data, so
our best model satisfies them 77.6% of the time, we collect our own dataset of creative writing inoutperformingInstructGPTbyamarginof28%. structionsfrompubliclyavailablepoemcorporaor
Tounderstanditscollaborationcapabilities,we relevantsubredditsfromReddit(Table7).
run a user study on Amazon Mechanical Turk Based on some initial feedback from profes-

sional poets, we decided to include 3 major
# 3 HowWellDoLLMsFollow Instructions?
types of instructions: 1) Continuation based instructions that suggest content when writers are In this section, we first describe our models and
blocked/cluelessonhowtoproceed;2)Instructions baselines,followedbytheevaluationresultsusing on Lexical Constraints to enable greater control both automatic metrics (Section 3.3) and human
of poetic form such as rhyme, sound, and meter. evaluation(Section3.4).
Theseareinstructionsthatforcelanguagemodels toobeyspecificchoicessuchasgeneratingaline
3.1 ExperimentSetup thatcontainsaspecifictopic,startword,endword
or a sentence with a particular rhyme; 3) Instruc- Model Details We finetune the pretrained T5 tionsonRhetoricaldevicesthataremostlyusedfor (Raffel et al., 2020) and T0 (Sanh et al., 2021)
introducingembellishmentsandimageryinapoem modelsfromHuggingFace(Wolfetal.,2019)on suchasmetaphor,similes,andonomatopoeia. the collected data (Section 2) to produce the out-
putgiventheinstructionusingcross-entropyloss.
Table1showstheprimaryinstructionsusedto WereportresultsonfinetunedT5-3B,T5-11Band trainourmodels. Theseinstructionsarecraftedby T0-3Bmodels,whicharehenceforthreferredtoas
theauthorsofthepaper,whoconverteverypoem T5-3B-poem,T5-11B-poem,andT0-3B-poem. We linetoan<instruction, poem_line>pairusing selectthehyperparametersbythevalidationloss:
rules. forT5-11B-poem,weusetheAdamoptimizerwith a learning rate of 1e−4; for T5-3B-poem and T0-
Eachinstructionconsistsofatemplate(unique
3B-poem, weusetheAdafactoroptimizerwitha totheinstructiontype)andoneormorearguments,
learningrateof1e−3. Eachmodelistrainedfor3 as can be seen in Table 1. Given a poem line in
epochswithearlystoppingbasedonvalidationloss.
thecorpus,wereverse-engineertheinstructionby
WefinetuneallmodelsonanA100GPUanduse picking a template and extracting the arguments
Deepspeed(Rasleyetal.,2020)integrationforthe fromthepoemline. Forcontinuationinstructions,
11Bmodel. Duringfinetuning,werestrictthemaxweusethepreviouscontextastheargument. For
imumsequencelengthofboththesourceandthe instructionsonlexicalconstraints,weextractnoun
targetto64tokens(viatruncation).$^4$ Atinference phrases and start/end words as arguments using
time, we generate output sequences using top-k
NLTKfortokenization. Toconstructinstructions samplingwithk = 5andatemperatureof0.7per
on rhymes, we use the CMU dictionary to find recommendationsfromearlierworkinopen-ended
rhymingwords.$^2$ WedescribemoredetailsinApcreativetextgeneration(Fanetal.,2018;Holtzman
pendix A on how we create instructions for each etal.,2020;PadmakumarandHe,2022).
particulartype.
Baselines We compare our finetuned models
Toallowmodelstoadapttolinguisticvariations withtwoothermodels: (i)theT0ppmodel(Sanh
oftheinstructiontemplates,wealsoincludeparaetal.,2021),trainedoninstruction-basedprompts
phrases of the instruction templates, e.g., instead from49datasets;$^5$ and(ii)the175Bdavincivariant
of “Write" we also use“Generate”, or instead of ofInstructGPT(Ouyangetal.,2022)thatistrained
“Writeasentenceabout”weuse“Writeasentence onhuman-writteninstructionsondiversetasksina
thatcontainstheword”or“Writeasentencethat human-in-the-loopfashion. Givenaninstruction,
includestheword”. Intotal,ourdatasetconsistsof wegeneratetextdirectly(i.e.zero-shot)fromT0pp
873,574<instruction, poem_line>pairswhich usingtop-ksampling(Fanetal.,2018).
we randomly split into 808,180 train and 65,394
For InstructGPT, we evaluate on both zeroheld-outvalidationexamples.$^3$ Weevaluateperfor-
shot and few-shot settings. For zero-shot, the manceonthreetestsetsofhand-craftedinstructions
prompt consists of only the instruction. For fewofvaryingdifficulty(Section3.2).
shot, the prompt consists of 26 <instruction,
$^4$Thelengthlimitischosentoavoidmemoryexplosion.It hasminimalimpactonmodelperformancesincemostverses
areshorter.
$^2$https://pypi.org/project/pronouncing/ $^5$These include question-answering, summarization,
$^3$Our dataset is publicly available at https://github. structure-to-textgeneration,sentimentandtopicclassification com/vishakhpk/creative-instructions. tasksbutnoexplicitcreativewritingtasks.

poem_line>pairsfromourtrainingdata(selected Writeapoeticsentencethatstartswiththe
Start tocoveralltheinstructiontemplates),followedby word‘Maybe’andendingin‘void’
+End thetestinstruction.$^6$ WeusetheOpenAIAPIwith Maybeoneday,youwillfindmeinthevoid
a temperature of 0.7, no frequency penalty, and
Writeapoeticsentencethatcontainsthe a maximum sequence length of 64 to match our
Subject word‘breaks’andendinginawordwhich setting.
+Rhyme rhymeswith‘bound’
3.2 TestSets Shecracksandbreaksandhitstheground.
While our training instructions cover many tem- Writeanextsentenceinapoetrygiven plates and topics, user instructions may deviate Next theprevioussentence‘Everyonceawhile
from the training distribution during interaction. Sentence Ilowertheblinds’andendingin‘play’
To evaluate the generalization capabilities of the +End Waitingforsomeonetocallmeouttoplay models,weidentifythreesettingswithincreasing
Writeametaphorthatincludestheword difficulty based on whether the instruction tem- Metaphor
‘film’andendingin‘thought’ platesorargumentsareseenduringtraining. +End
Afilmisapetrifiedfountainofthought.
Known Instruction Templates with Known Ar-
Table 2: Examples of compositional natural language guments(KIKA) Thesimplestsettingrequires
instructions for creative tasks paired with their respecthemodeltogeneralizetonovelcombinationsof
tiveoutputsfromourtestsets.
thetemplatesandarguments. Specifically,wecreateinstructionswhereboththetemplatesandthe
arguments are seen in the training set, although tionsaccordingtotheabovecriteria,followedby eachspecificcombinationisunseen(i.e.thetrain- manualverification.
ingandtestsetshavenooverlappinginstructions).
3.3 AutomaticEvaluation
Known Instruction Templates with Unknown
Weevaluatehowwellthemodelssatisfyconstraints
Arguments (KIUA) To handle novel concepts specifiedintheinstructionsoneachofthetestsets
from users, the model must generalize to unseen
(Section 3.2). We report the success rate of satisarguments, which may include new entities or
fyingtheinstructionswherethesuccesscondition phrases. Forexample,itmightbeeasierforamodel
foreachinstructiontypeislistedinTable3.$^7$ towriteapoeticsentenceaboutaknownargument
such as beauty, but difficult to write about an un-
Instruction SuccessCondition known argument beauty without virtue. For this Type
set,weincludeinstructionswheretheinstruction Rhyme Lastwordofthemodelgeneration templates are seen during training but the corre- rhymeswiththedesiredsubjectusingthe
CMUPronouncingDictionary spondingargumentsareunseen.
Haiku Modelgenerationcontains15–19
Unknown Compositional Instruction Tem- syllablesandcontainsthedesiredsubject plates One of the main benefits of natural Simile/ Modelgenerationcontainsthedesired
language instructions is that they can be easily Metaphor subjectaswellasacomparator composed in new ways to cover various user Start/End First/lastwordofthemodelgeneration
intentions. This is particularly useful in creative matchesthedesiredsubject writing because it enables users to request text Subject Modelgenerationcontainsthedesired
from the model with multiple constraints. There- subjectintheinstruction fore, wealsotestwhetherthemodelunderstands
Table 3: Success conditions for different instruction compositional instructions using two templates,
templates.
as seen in Table 2. Our model is exposed to a single compositional template during training: FinetunedModelsHaveStrongIn-DomainPer-
Subject+End. Forthistestset,wecreateavariety formance but Drop on Out-of-Domain Data ofunseencompositions. Figure2showstheaveragesuccessrateandstan-
Intotal,wecreate242testexamples(82KIKA, $^7$Prior work on instruction tuning reports metrics such
82KIUA,78compositional)byselectinginstruc- asBLEUscoreforgenerationtasks(Sanhetal.,2021;Wei etal.,2021)andtheseareunsuitableforourpoetrywriting
$^6$Theexactpromptcanbefoundinourcoderepository. instructions,thuswedefinecustomsuccessconditions.

d
T5-11B-poem
80
T5-3B-poem
T0-3B-poem
T0pp
60 InstructGPT-FS
InstructGPT-ZS
40
20
0
KIKA KIUA Compositional
Figure 2: Automatic evaluation of models on KIKA,
KIUA and Compositional test sets. The y axis is the percentageofinstructionsthateachmodelsuccessfully
satisfiesasdeterminedbythecriteriainTable3. WereportresultsonT5-11B-poem,T5-3B-poemandT0-3B-
poemalongwiththebaselines—zero-shotT0pp(Sanh etal.,2021)andzero-shot(ZS)/few-shot(FS)Instruct-
GPT(da-vinci)(Ouyangetal.,2022). Eachbarshows the average success rate of 5 model inferences along
withthestandarddeviation.Onaverage,T5-11B-poem achieves the highest success rate and InstructGPT is
a strong few-shot baseline that obtains comparable resultsonKIUA.

fying instructions is largest on the compositional testset—T5-11B-poemaccuratelyanswers77.6%
of compositional instructions while InstructGPT onlymanages55.2%. Annotatorsalsoreportedthat
versesfromT5-11B-poemweremarginallymore creative/interestingthanInstructGPTonKIKAand
KIUA test sets and less so on the Compositional test set, indicating that the two models may have
littledifferenceincreativity.$^9$
We observe that InstructGPT is a strong baseline, outperforming T0pp by a large margin on
automatic metrics, and satisfying nearly 80% of the instructions in the KIKA and KIUA test sets
accordingtohumanevaluation. However,acommonerrorcaseoncompositionalinstructionsisthat
whilethemodelgenerationsalmostalwayscontain theargumentsmentionedintheinstruction,theydo
notalwayssatisfytheconstraintscorrectly—when askedforaversethatcontainstheword‘soul’and
endswith‘yellow’,InstructGPTgeneratedtheline
“Mysoulisasyellowasthesunonasummerday” thatcontainthoseargumentsbutnotatthespeci-
fiedpositions.
Takeaways We observe that on average finetuned models tend to outperform the few-shot
baselinesonin-domaininstructions(Section3.3).
Whilesmallermodels(T5-3B-poem,T0-3B-poem) have worse performance on out-of-domain in-
structions, finetuned models at scale (T5-11Bpoem) generalizes to compositional instructions
$^9$Thefirsttwoquestionsarelesssubjectivethanthethird question. Usersunanimouslyagreed52.2%ofthetimeon
whether model generations satisfied instructions and only
37.3%onwhichoutputismorecreative.

d
T5-11B-poem GPT3-FS effectively,evenoutperformingInstructGPT(Section3.4). Theflexibilityofcomposinginstructions
Success% 86.2 76.9
KIKA(82) Fluency 0.739 0.794 makes the model more suitable as a collaborator
Creative 53.8 46.2 forahumanuser;henceweuseT5-11B-poemas
Success% 92.5 86.5 the assistant for our subsequent collaborative ex-
KIUA(82) Fluency 0.773 0.781 periments.
Creative 56.7 43.3
Success% 77.6 55.2
4 CoPoet: CollaborativePoemWriting
Fluency 0.697 0.751
Comp(78)
Creative 47.7 52.3
Our results in Section 3.4 demonstrate CoPoet’s abilitytosatisfytheconstraintsspecifiedinthein-
Table4: Humanevaluationofmodelgenerationsfrom structions. This presents us with an opportunity
T5-11B-poemandfew-shotInstructGPT3ondifferent testsetsacrossthreemetrics: (i)successrate: percent- totestthemodel’scapabilityincollaborativewrit-
age of instructions satisfied; (ii) fluency: average flu- ingtasks. Wedesignouruserstudy(Figure3)to ency score on a scale of 5 normalized to [0,1]; (iii) answerthefollowingtwomainresearchquestions:
creativity: percentage of generations rated to be more creative/interestinginapairwisecomparison. • RQ1: Canuserswritepoemsonanytopicof
theirchoicebycollaboratingwithCoPoet?
• RQ2: Does CoPoet help users write better poemscomparedtowhentheywritealone?

Topic: Decadence
Solo Writer CoPoet
----------
----------
----------
1) ---
2) ---
3) ---
RQ1: Can users collaborate with
D Oe pc ea nd ue pn c Ine s ( t1 a ) and you'll see CoPoet to write poems?
All of the pleasures you'll ever need.
Photos of food, cars, and female models.
All competing for likes and comments. Decadence (2)
Social connection broken down, The cake is like a cloud of joy.
with many indulgences all around The frosting is like a rainbow.
One slice is heaven on Earth,
A flowing chocolate volcano.
RQ2: Do collaborative users outperform solo-writers?
Subjective Majority Vote
"2 is better than 1"
Figure3: CoPoetuserstudy. WestudyifuserscaneffectivelycollaboratewithCoPoettowritepoems(RQ1)
and whether writing with CoPoet produces better poemscomparedtosolo-writers(RQ2).

Interface Design Since we intend to study the task of collaborative poem writing, we develop
a user interface for our experiments where users can work on their poem drafts and also query
CoPoetforsuggestionsusingwritteninstructions.
A screenshot of the interface is provided in Figure 11. In response to each instruction, CoPoet

provides 5 suggestions, each in the form of one able to collaborate with CoPoet and write poems poemline,totheusers. Theuserscanthenchoose ondiversetopicsoftheirchoice,includingClimate
if they wish to incorporate these into their draft. Change, Hunger, Glass Ceiling, Decadence etc.
Weinstructthemtoeditthemodeloutputwhenre- We include more examples in Appendix B. The quiredtoensuretheoverallcoherenceofthepoem. fulllistoftitlesvisualizedasawordcloudcanbe
AsseeninFigure11,usersarealsoprovidedwith foundinFigure10.
the list of instruction templates used to train the
How do experts use instructions? On average, model(Section2). Theseareintendedtocommu-
expertsuse7instructionsperpoem. Figure4shows nicate to users the instructions that the model is
thatexpertsoftenprefercontextualinstructions,i.e.
trainedtorespondto,sothattheyhaveanideaof whatthemodeliscapableof.$^{10}$ getting ideas from the model about the Next Sen-
tence given what they have written thus far. The
ExperimentSetup Wefirstconductaqualifica- Topicinstructionisalsosignificantlyused,which tiontestonAMT,wherewerecruit50workersto helpsthemaddcontrol. Itisencouragingtoseehu-
collaboratively write a poem of four lines using mansusingatotalof87compositionalinstructions,
CoPoet. Werequireausertointeractwithoursys- which constitutes almost 24% of the total set of tem at least four times (i.e., to issue at least four instructionsused. Finally,humansalsousefigura-
instructions). However, we do not enforce that tiveembellishmentssuchasSimilesorMetaphors they use any of the model outputs in response to suggestedbythemodel.
theirinstructions—theyarefreetoignoreallmodel suggestions. The authors of the paper then inde-
Topic+Rhyme pendently rank these poems in terms of fluency, 15.2%
Start+End richness in imagery, and creativity. Finally, 15 3.0% Next Sentence
Topic+End 36.8% crowd-workerspassedthequalificationtest. From 5.8%
nowon,werefertothesequalifiedworkersasexperts. Topic
19.1%
Wethencollect50distinctpoemscollaboratively End Simile+Metaphor
6.1% 13.9% written by our experts using CoPoet, where they
are instructed to write a poem on a topic of their Figure4: Proportionsofthetypesofinstructionsused choice. In order to compare collaborative writ- byexpertsinthepoetrywritingtask.
ers to solo-writers, we then collect 50 poems on thesametitlesfromexpertwriterswritingwithout
Do experts find CoPoet helpful as a writing model assistance.$^{11}$ Third-party annotators were
tool? We collect judgments from 15 experts to then shown the title and two poems interpreting
tease out and characterize the model’s contribuit, andinstructedtoselecttheonetheyfeltwasa
tion. Weareinterestedtoknowwhetherthemodel
‘descriptive interpretation of the title’. To ensure helpedinthewritingprocessbysatisfyingthein-
a fair judgement, both the poems were identical structions,andhowwellitservedthewriters’needs.
inlength(4lines),randomizedinorder,andwith-
WecollectratingsonaLikertscalefrom1(notat outobviouscluesinthevocabularyusage. Tothe
all) to 5 (very) on two questions: (i) How accubest of our knowledge, there was no underlying
ratelydoesthemodelfollowinstructions? (ii)How biasthatwouldmakeiteasyforjudgestoidentify
helpful is the model in the process of writing powhich poems were collaborative and which were
etry? We obtain an average score of 4.3 out of 5 written entirely by humans. The full experiment
onbothquestions,suggestingthatCoPoetisausedesignisshowninFigure3.
fultoolforpoemwriting. Table8inAppendixA
RQ1: Can experts write poems successfully on showssomeofthefeedbackprovidedbyexperts, any topic of their choice by collaborating with including how they found the system helpful in
CoPoet? situationssuchaswriters’block,andhowspecific
From our user study, we observe that experts are instructionshelpedthemwritebetter.
$^{10}$Weexplicitlymentionthattheycanusenovelinstructions
What fraction of the poems is written by notpresentinthetemplates.
CoPoet? To quantify the contribution of the
$^{11}$We ensure that the same author does not write on the sametopicinthetwosetups. model,wecomputetheproportionofthesubmitted

40
30
20
10
0
75 - 100 50 - 75 25 - 50 0 - 25
Rouge-L recall for CoPoet contribution smeoP
fo rebmuN
latoT fo
% written by experts with CoPoet. They are shown
onepoemeachfromasolo-writerandacollaborativewriter,bothinresponsetothesametitle,and
requestedtolabeleachpoemonwhetheritisrelevant. Additionally,theyareaskedtochoosetheir
preferredpoembetweenthegivenpairintermsof coherence,overallquality,andstyle. Eachpairof
poems is evaluated by 3 distinct annotators. We thenaggregatethejudgmentsviamajorityvoting.
Table 5 shows that both poems written by solo writersandpoemswrittencollaborativelyareaccu-
rate. We are encouragedtoseethatcollaborative poems are preferred more than poems written by
solo-writers. These findings suggest that CoPoet
Relevant% Preferred% isahelpfultoolforpoetrywritingandinstructions
Solo 96 43 actasausefulvehicleforco-creativewritingusing
Collaborative 98 57
LLMs.
Table 5: Human evaluation of 50 poems written by solo-writers vs those written by users with CoPoet.
Preferred% NotPreferred%
Workers have a slight preference for collaborative poems. Diversity 63.0 37.0
Rhyme 72.5 27.5
Perplexity 55.0 45.0 poemsthatwastakenfromthemodelgenerations.
WecalculatethisusingtheRouge-Lrecall(Linand Table 6: Analysis of poems preferred by third-party
Rey, 2004) score of the poem lines with respect annotatorsbasedon(i)rhyme(ii)diversityand(iii)perplexity.Workers’preferenceiscorrelatedwiththepres-
tothemodelsuggestionsi.e.whatfractionofthe enceofrhymingandvocabularydiversity.
poemisfoundinthegeneratedoutputofthemodel.
Eachverseisgreedilymatchedtoauniquemodel suggestionwiththelargestoverlap. Thecalculation
isdescribedinAlgorithm1inAppendixA.Figure
5showsthatonaverage46%ofcollaborativepo-
Potential Factors for User Preference We acemshaveaRouge-Lrecallscoregreaterthan75%,
knowledgethatthereissomedegreeofsubjectivity i.e75%ofthecontentinthecollaborativepoems
intheuserpreferences. Tobetterunderstandwhy areobtainedfromCoPoetsuggestions. Addition-
acertainpoemispreferredbycrowd-workers,we ally,afurther40%ofthecollaborativepoemshave
investigate whether certain factors correlate with morethanhalfoftheircontent(50-75%)writtenby
theirchoices. Wemeasurei)Diversity(intermsof the model. This suggests that the majority of the
distinctunigrams)ii)PresenceofRhyme(whether textgeneratedbyCoPoetisconsideredhigh-quality
thereatleastonepairofrhyminglinesinthepoem), andusablebytheexpertusers.
and iii) Perplexity measured using a pre-trained
RQ2: Can CoPoet help users write better po- GPT-2 model for each poem. As can be seen in ems compared to when they write alone? To Table 6, crowd-workers preferred poems that are
answertheabovequestion,wecomparepoemswrit- diverseandhavearhymescheme63%and72.5% ten by the set of experts with and without model ofthetime. FromFigure4,weknowthatourex-
help,asdetailedinFigure3. Weareinterestedin perts tend to use the model to express their ideas measuringi)whetherpoemswrittenarerelevant, byelicitingtextfromthemodelthatcontainsspe-
where an relevant poem is defined as descriptive cific content but is subject to various constraints interpretation of the title, i.e. it is on-topic. ii) (Topic+Rhyme and the various End instructions).
whetherpoemswrittenbyexpertswithCoPoetare Here,weobservethattheseconstraintscombined preferredoverpoemswrittenbysolo-writers. withmorediversevocabularyusagemightbecon-
Werecruitatotalof49third-partyannotatorsto tributingtothepreferenceforcollaborativepoems comparepoemswrittenbyexpertsalonetothose oversolopoems.

# 5 RelatedWork
Inadditiontofine-tuningmodelsoninstructions, largelanguagemodelsarealsoabletogeneralizeto
CollaborativeWriting Thekeychallengeincol- unseentasksinafew-shotmannerwhenthetaskis laborativewritingistounderstanduserintentsoas specifiedaspartofthepromptinnaturallanguage
to provide timely and useful suggestions. Prior (Ouyang et al., 2022). Reif et al. (2022) present work in story writing (Roemmele and Gordon, a prompting method which performs style trans-
2015;Clarketal.,2018)presentedsentence-level ferinazero-shotorfew-shotmannerwithonlya continuationsatlocationsspecifiedbyauser. Ak- naturallanguageinstructiondescribingthetarget
ouryetal.(2020);Leeetal.(2022)tookthisastep stylewithoutmodelfine-tuningorexemplarsinthe further providing users with a paragraph of text target style. Unlike most of the recent work that
whichtheycouldfurthereditinstorywritingandar- prompts large language models to elicit content gumentativewritingtasks. However,modelsugges- Coenenetal.(2021)framecollaborativewritingas
tionsofthisautocompletenaturewerenotalways aconversationbetweenahumanandaLLM-based helpful,astheyoftendivergedfromtheuserintent dialogsystemandshowhowthespontaneousutili-
(Clarketal.,2018)resultinginonlyafractionof tiesofconversationsupportavarietyofinteractions.
generatedtextbeingretained(Akouryetal.,2020). MorerecentlyMishraandNouri(2022)proposea
Insteadofprovidingamachine-writtendraft,Pad- promptingstrategywheretheyaskGPT3specific makumar and He (2022) showed that having the questionsaboutmood,tone,occasion,orthemefor
model rewrite text only at locations specified by thetaskofpoemgenerationbyusingGPT3asan theuserresultsinmorehelpfulsuggestionsinthe interactioninterface.
taskofcreativeimagecaptioning.
Wefocusonthetaskofcollaborativepoemwrit- # 6 Conclusion ing,whichaddsanadditionalchallengeasuseful
suggestionsneedtosatisfyseverallexicalandform In this work, we present CoPoet, a collaborative constraints (rhyme, meter, sound). Past work for poetry writing system that is controlled by user
thistaskhasusedretrievaltoprovidesuggestions instructions that specify the attributes of any deforsubstitutionsatthewordandphraselevel(Chen sired text. Our system is built upon a language
et al., 2014) or verses that follow different styles modelfine-tunedonadiversecollectionofinstruc-
(Uthusetal.,2022),buttheseareunabletodynam- tions for poetry writing. Empirical results show icallygeneratenoveltext. Inourwork,weutilize that our model is not only competitive with pub-
largelanguagemodelstogeneratetextthatsatisfies licly available LLMs trained on instructions (Inthevariousconstraintsspecifiedbyusers,withthe structGPT),butalsocapableofsatisfyingunseen
added benefit that they can spell out these using compositionalinstructions. Afurtherstudywith15 naturallanguageinstructions. Concurrentworkhas qualifiedcrowd-workersshowsthatuserssuccess-
also shown that large language models can help fully write poems with CoPoet on diverse topics, userswritescriptsandscreenplays(Mirowskietal., whicharealsopreferredbythird-partyevaluators
2022)andlongerstories(Yangetal.,2022)bygen- overpoemswrittenbysolo-writers. Theseresults eratingtextthatincorporatesstructuralcontextvia show that language models acting as writing as-
promptchaining. sistantsarecapableofunderstandinguserintents and collaborating with them to improve the final
InteractionwithUsers RecentworkinNLPhas outcome,potentiallymakesachallengingtasksuch highlighted the success of generative large lan- aspoemwritingmoreaccessibletousers.
guagemodelsasinteractioninterfacesforthetask Goingforwardwehopetoextendourresearch of creative writing. Finetuning models on tasks tomorechallenginginstructionssuchasconverting
verbalised as instructions has shown good gener- longercontentplanningtasksintotheinstruction alization to unseeninstructions (Weiet al., 2021; tuningsetuptoassistuserswithlongerstorywrit-
Sanhetal.,2021;Mishraetal.,2021;Chungetal., ing. To provide more robust assistance, we also
2022). Inourwork,wefocusonasuiteofinstruc- hopetostudyhowtotrainmodelsthatgeneralize tions specific to creative writing and additionally better to completely unseen instructions. Finally,
evaluatetheinstruction-tuningsetupwithrealusers weintendtomoreholisticallystudytheproblemof whoiterativelyaskforsuggestionsinnaturallan- co-creative writing by not just examining how to
guage. trainbetterassistivemodelsbutalsohowtodesign

effectiveuserinterfacesforendusers. believethatmachinegenerationofpoetictextwill notleadtotheexclusionofhumanpoets. Rather,it
Limitations willincreasehuman-machineinteractionandcon-
tinuetoenhancehumanperformance.
NoisyTrainingData Wenotethatourdatasetis self-supervised and we use various tools to align In order to ensure that there are no privacy is-
lines of poetry from various sources (Table 7) to suesforourtrainandvalidationsplits,thepoems templatedinstructions. Theremightbesmallerrors were broken down line by line and shuffled ran-
in the training data such as spelling mistakes in domly.They do not contain any metadata and as thelinesofpoetry(anexamplefromourdatasetto such cannot reproduce the creative value of the
showcase this is the line “Lay silently burid side originalpoems.
by side”) or slightly convoluted instructions (an exampleinstructiontohighlightthisis“Writeapo-
Appropriate Remuneration of Crowd-workers eticsentencethatspeaksofnightsgrowshorter”).
Forallourtasks,werecruitfromapoolofcrowd-
However,eachexampleinthevarioustestsets(SecworkersintheUSAwithaminimumof95%HIT
tion 3.2) was manually verified by the authors of successrate. Tocompletethehumanevaluationof
thiswork.
modeloutputssatisfyinginstructions(Section3.4),
Test Set Size Another potential concern is the acrowdworkerhastoreadaninstructionandtwo size of the test sets which were small as each in- linesinresponsetoitandansweratotalof5ques-
structioninthesewasverifiedbytheauthors. We tions. Onaverage,thistakesslightlylessthantwo provideconfidenceintervalsonthemodelsuccess minutes, sowesetthepaymentto$0.50perHIT.
ratestomitigatethisinSection3.3. Forthewritingtasks(soloandcollaborative,Section 4), on average our users take 10 minutes to
DesignoftheUserInterface Ouruserinterface writeapoem,sowesetthepaymentof$2.50for
presents templates of instructions to users at the eachHIT.Wealsorewardwriters$0.50perpoem
point when they query the model for assistance onsubmissionofpoemsdeemedrelevantorarel-
(Figure11). Thisprimestheuserstowriteinstrucevant interpretation of the title, per the definition
tions similar to the templates—almost all the inin Section 4. Over 95% of the poems submitted
structionsusedbythecrowdworkersbelongedto received a bonus (Table 5). Finally, for the judg-
the templates provided in the interface (or novel ingtaskofcomparingsolo-writersandcollabora-
combinations of these). In this work, we did not tivewriters,crowdworkershavetoreadtwopoems
perform an extensive comparison of different inandanswer3questions,whichtakesonaverage1
terfacedesignswhichcouldinfluencetheinteracminute, so we set the payment to $0.25 per HIT.
tion. Wefurtherdiscusssomeofthedesignchoices
Alloftheseamountswerecalculatedaccordingan abouttheuserinterfaceinAppendixC.
hourlyrateof15$perhour.
EthicsStatement
Acknowledgements
Althoughweuselanguagemodelstrainedondata collectedfromtheWeb,whichhavebeenshownto
haveissueswithgenderbiasandabusivelanguage, We would like to thank the anonymous reviewthe inductive bias of our models should limit in- ers for their helpful comments. We additionally
advertentnegativeimpacts. Unlikemodelvariants alsowanttoacknowledgeallhumanauthorswho suchasGPT,T5isaconditionallanguagemodel, posted their work open-sourced on the websites
whichprovidesmorecontrolofthegeneratedout- we collected the data from. Tuhin is funded by put. Ourpoeticparallelcorporaareunlikelytocon- ColumbiaCenterofArtificalIntelligence&Tech-
tain toxic text and are manually inspected by the nology (CAIT) and the Amazon Science Ph.D.
authors.Technologicaladvancesintextgeneration Fellowship. This work is also supported by the havehadbothpositiveandnegativeeffects. How- SamsungAdvancedInstituteofTechnology(Next
ever,interactive,human-in-the-loopgenerativesys- GenerationDeepLearning: FromPatternRecognitemsdesignedespeciallyforliteraryorpoetictext tiontoAI),theNationalScienceFoundationunder
generationsuchasoursmightspeedupliterarypro- GrantNo. 1922658,andagiftfromAWSAI.
fessional’sworkandmakeitmoreenjoyable. We

## References

Nader Akoury, Shufan Wang, Josh Whiting, Stephen
Hood, Nanyun Peng, and Mohit Iyyer. 2020. STO-
RIUM: A Dataset and Evaluation Platform for
Machine-in-the-LoopStoryGeneration. InProceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), pages
6470–6484, Online. Association for Computational
Linguistics.

Vamsi Aribandi, Yi Tay, Tal Schuster, Jinfeng Rao,
HuaixiuStevenZheng,SanketVaibhavMehta,Honglei Zhuang, Vinh Q Tran, Dara Bahri, Jianmo
Ni, et al. 2021. Ext5: Towards extreme multitask scaling for transfer learning. arXiv preprint
arXiv:2111.10952.

GwernBranwen.2020. Gpt-3creativefiction.

TomB.Brown,BenjaminMann,NickRyder,Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan,PranavShyam,GirishSastry,Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen,
Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam Mc-
Candlish, Alec Radford, Ilya Sutskever, and Dario
Amodei.2020. Languagemodelsarefew-shotlearners. arXivpreprintarXiv:2005.14165.

Ricardo Campos, Vítor Mangaravite, Arian Pasquali,
AlípioMárioJorge,CéliaNunes,andAdamJatowt.
2018. Yake! collection-independentautomatickey-
wordextractor. InEuropeanConferenceonInformationRetrieval,pages806–810.Springer.

Ricardo Campos, Vítor Mangaravite, Arian Pasquali,
Alípio Jorge, Célia Nunes, and Adam Jatowt. 2020.
Yake! keyword extraction from single documents usingmultiplelocalfeatures. InformationSciences,
509:257–289.

Tuhin Chakrabarty, Arkadiy Saakyan, and Smaranda
Muresan.2021. Don’tgofaroff:Anempiricalstudy on neural poetry translation. In Proceedings of the
2021 Conference on Empirical Methods in Natural
LanguageProcessing,pages7253–7265,Onlineand
Punta Cana, Dominican Republic. Association for
ComputationalLinguistics.

Quanze Chen, Chenyang Lei, Wei Xu, Ellie Pavlick, and Chris Callison-Burch. 2014. Poetry of the
crowd: A human computation algorithm to convert proseintorhymingverse. InHCOMP.

Hyung Won Chung, Le Hou, Shayne Longpre, Barret
Zoph,YiTay,WilliamFedus,EricLi,XuezhiWang,
MostafaDehghani,SiddharthaBrahma,AlbertWebson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suz-
gun, Xinyun Chen, Aakanksha Chowdhery, Sharan
Narang, Gaurav Mishra, Adams Yu, Vincent Zhao,
Yanping Huang, Andrew Dai, Hongkun Yu, Slav
Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam
Roberts, Denny Zhou, Quoc V. Le, and Jason Wei.
2022. Scaling instruction-finetuned language mod-
els.

Elizabeth Clark, Anne Spencer Ross, Chenhao Tan,
Yangfeng Ji, and Noah A. Smith. 2018. Creative writing with a machine in the loop: Case stud-
ies on slogans and stories. In 23rd International
Conference on Intelligent User Interfaces, IUI ’18, page329–340,NewYork,NY,USA.Associationfor
ComputingMachinery.

Andy Coenen, Luke Davis, Daphne Ippolito, Emily
Reif, and Ann Yuan. 2021. Wordcraft: a human-ai collaborativeeditorforstorywriting. arXivpreprint
arXiv:2107.07430.

ChrisDonahue,MinaLee,andPercyLiang.2020. Enablinglanguagemodelstofillintheblanks. InPro-
ceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 2492–
2501, Online. Association for Computational Linguistics.

Wanyu Du, Zae Myung Kim, Vipul Raheja, Dhruv
Kumar, and Dongyeop Kang. 2022. Read, revise, repeat: A system demonstration for human-in-the-
loop iterative text revision. In Proceedings of the
First Workshop on Intelligent and Interactive Writing Assistants (In2Writing 2022), pages 96–108,
Dublin,Ireland.AssociationforComputationalLinguistics.

KatherineElkinsandJonChun.2020. Cangpt-3pass awriter’sturingtest? JournalofCulturalAnalytics,
5(2):17212.

AngelaFan,MikeLewis,andYannDauphin.2018. Hierarchical neural story generation. In Proceedings
of the 56th Annual Meeting of the Association for
ComputationalLinguistics(Volume1:LongPapers), pages 889–898, Melbourne, Australia. Association
forComputationalLinguistics.

Marjan Ghazvininejad, Xing Shi, Yejin Choi, and
Kevin Knight. 2016. Generating topical poetry. In
Proceedings of the 2016 Conference on Empirical
Methods in Natural Language Processing, pages
1183–1191, Austin, Texas. Association for ComputationalLinguistics.

AriHoltzman, JanBuys, LiDu, MaxwellForbes, and
YejinChoi.2020. Thecuriouscaseofneuraltextdegeneration. In International Conference on Learn-
ingRepresentations(ICLR).

ArthurMJacobs.2018. Thegutenbergenglishpoetry corpus: exemplary quantitative narrative analyses.
FrontiersinDigitalHumanities,5:5.

Mina Lee, Percy Liang, and Qian Yang. 2022. Coauthor: Designing a human-ai collaborative writing
dataset for exploring language model capabilities.
InProceedingsofthe2022CHIConferenceonHuman Factors in Computing Systems, CHI ’22, New
York,NY,USA.AssociationforComputingMachinery.

Chin-yew Lin and Marina Rey. 2004. Looking for a few good metrics: ROUGE and its evaluation. In
NTCIRWorkshop.

Piotr Mirowski, Kory W Mathewson, Jaylen Pittman, and Richard Evans. 2022. Co-writing screenplays
and theatre scripts with language models: An evaluation by industry professionals. arXiv preprint
arXiv:2209.14958.

Swaroop Mishra, Daniel Khashabi, Chitta Baral, and
Hannaneh Hajishirzi. 2021. Cross-task generalizationvianaturallanguagecrowdsourcinginstructions.
arXivpreprintarXiv:2104.08773.

Swaroop Mishra, Daniel Khashabi, Chitta Baral, and
Hannaneh Hajishirzi. 2022. Cross-task generalizationvianaturallanguagecrowdsourcinginstructions.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: LongPapers),pages3470–3487,Dublin,Ireland.
AssociationforComputationalLinguistics.

Swaroop Mishra and Elnaz Nouri. 2022. Help me think: Asimplepromptingstrategyfornon-experts
to create customized content with models. arXiv preprintarXiv:2208.08232.

Aitor Ormazabal, Mikel Artetxe, Manex Agirrezabal,
Aitor Soroa, and Eneko Agirre. 2022. Poelm: A meter-and rhyme-controllable language model for
unsupervised poetry generation. arXiv preprint arXiv:2205.12206.

LongOuyang,JeffWu,XuJiang,DiogoAlmeida,Carroll L Wainwright, Pamela Mishkin, Chong Zhang,
SandhiniAgarwal, KatarinaSlama, AlexRay, etal.
2022. Training language models to follow instruc-
tionswithhumanfeedback. Preprint.

Vishakh Padmakumar and He He. 2022. Machine-inthe-looprewritingforcreativeimagecaptioning. In
Proceedings of the 2022 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies,
pages 573–586, Seattle, United States. Association forComputationalLinguistics.

VishakhPadmakumar,LeonardLausen,MiguelBallesteros, Sheng Zha, He He, and George Karypis.
2022. Exploring the role of task transferability in
large-scale multi-task learning. In Proceedings of the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics: Human Language Technologies, pages 2542–
2550, Seattle, United States. Association for ComputationalLinguistics.

Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020. Exploring thelimitsoftransferlearningwithaunifiedtext-to-
text transformer. Journal of Machine Learning Research,21(140):1–67.

Aditya Ramesh, Prafulla Dhariwal, Alex Nichol,
Casey Chu, and Mark Chen. 2022. Hierarchical text-conditional image generation with clip latents.
arXivpreprintarXiv:2204.06125.

Jeff Rasley, Samyam Rajbhandari, Olatunji Ruwase, and Yuxiong He. 2020. Deepspeed: System op-
timizations enable training deep learning models with over 100 billion parameters. KDD ’20, page
3505–3506, New York, NY, USA. Association for
ComputingMachinery.

Emily Reif, Daphne Ippolito, Ann Yuan, Andy Coenen,ChrisCallison-Burch,andJasonWei.2022. A
recipeforarbitrarytextstyletransferwithlargelanguage models. In Proceedings of the 60th Annual
Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 837–848,
Dublin,Ireland.AssociationforComputationalLinguistics.

MelissaRoemmeleandAndrewS.Gordon.2015. Creativehelp: Astorywritingassistant. InICIDS.

Victor Sanh, Albert Webson, Colin Raffel, Stephen H.
Bach, Lintang Sutawika, Zaid Alyafeai, Antoine
Chaffin,ArnaudStiegler,TevenLeScao,ArunRaja,
Manan Dey, M Saiful Bari, Canwen Xu, Urmish
Thakker, Shanya Sharma Sharma, Eliza Szczechla,
Taewoon Kim, Gunjan Chhablani, Nihal Nayak,
Debajyoti Datta, Jonathan Chang, Mike Tian-Jian
Jiang, Han Wang, Matteo Manica, Sheng Shen,
Zheng Xin Yong, Harshit Pandey, Rachel Bawden,
Thomas Wang, Trishala Neeraj, Jos Rozen, Abheesht Sharma, Andrea Santilli, Thibault Fevry, Ja-
sonAlanFries,RyanTeehan,StellaBiderman,Leo
Gao, Tali Bers, Thomas Wolf, and Alexander M.
Rush. 2021. Multitask prompted training enables zero-shottaskgeneralization. arXiv.

Abigail See, Aneesh Pappu, Rohun Saxena, Akhila
Yerukola, and Christopher D. Manning. 2019. Do massively pretrained language models make better
storytellers? In Proceedings of the 23rd ConferenceonComputationalNaturalLanguageLearning
(CoNLL),pages843–861,HongKong,China.AssociationforComputationalLinguistics.

BenSwanson, KoryMathewson, BenPietrzak, Sherol
Chen, and Monica Dinalescu. 2021. Story centaur:
Large language model few shot learning as a creativewritingtool. InProceedingsofthe16thConfer-
enceoftheEuropeanChapteroftheAssociationfor
ComputationalLinguistics: SystemDemonstrations, pages244–256.

Yufei Tian and Nanyun Peng. 2022. Zero-shot sonnetgenerationwithdiscourse-levelplanningandaes-
thetics features. In Proceedings of the 2022 Conference of the North American Chapter of the As-
sociation for Computational Linguistics: Human
Language Technologies, pages 3587–3597, Seattle,
United States. Association for Computational Linguistics.

David Uthus, Maria Voitovich, and R.J. Mical. 2022. InstructionType Source Stats
Augmenting poetry composition with Verse by
PoetryTranslationCorpus
Verse. InProceedingsofthe2022Conferenceofthe LexicalConstraint 94.5%
Chakrabartyetal.(2021)
NorthAmericanChapteroftheAssociationforComputationalLinguistics: HumanLanguageTechnolo- PoetryTranslationCorpus
Continuation 3.18% gies: Industry Track, pages 18–26, Hybrid: Seat- Chakrabartyetal.(2021)
tle, Washington + Online. Association for Compur/OCPoetry,r/Poetry
tationalLinguistics.
RhetoricalDevices GutenbergJacobs(2018), 1.12%
David Uthus, Maria Voitovich, RJ Mical, and Ray
DMDMQ14
Kurzweil. 2019. First steps towards collaborative Haiku r/Haiku 1.14% poetrygeneration.
Table7: InstructionTypesalongwiththesourcefrom
TimVandeCruys.2020. Automaticpoetrygeneration wherethedataiscollected.
fromprosaictext. InProceedingsofthe58thannual meetingoftheassociationforcomputationallinguis-
tics,pages2471–2480.
TheAIisverycompetentandhelpful,it’senjoyable
Yizhong Wang, Swaroop Mishra, Pegah Alipoor- toworkwithit.
molabashi, Yeganeh Kordi, Amirreza Mirzaei,
IthinkitworksveryfineandIwishIhadthiswhenever
Anjana Arunkumar, Arjun Ashok, Arut Selvan
Ihadwriter’sblock.
Dhanasekaran, Atharva Naik, David Stap, et al.
2022. Benchmarking generalization via in-context Thebestpartofthetoolisgettinghelpwithwordsatthe
instructions on 1,600+ language tasks. arXiv endofasentenceandthenbeingabletobuildoffthat.
preprintarXiv:2204.07705.
Table8:Someofthefeedbackfromexpertsonthehelp-
Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin fulnessofusingourCoPoetsystem.
Guu, Adams Wei Yu, Brian Lester, Nan Du, AndrewM.Dai,andQuocV.Le.2021. Finetunedlan-
guagemodelsarezero-shotlearners. arXiv.
filltheinstructiontemplatewitharandomrhyming
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, wordtoensurediversity. Forthe“NextSentence"
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
MaartenBosma,DennyZhou,DonaldMetzler,etal. we fill the instruction template with its previous
2022. Emergent abilities of large language models. contextsentencefromanygivenpoetry. Tocreate
arXivpreprintarXiv:2206.07682.
“Metaphor"instructionwecrawlwebsitesforout-
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien putsoftheform“NP1isNP2"andfillNP1inthe
Chaumond, ClementDelangue, AnthonyMoi, Pier- template. A‘Simile"usuallyconsistsoftwonoun ricCistac,TimRault,R’emiLouf,MorganFuntow-
phrasestypicallyaSubjectandanObjectwithan icz, and Jamie Brew. 2019. HuggingFace’s trans-
usualsyntax“NP1islikeNP2". WefilltheSubject formers: State-of-the-art natural language process-
ing. arXivpreprintarXiv:1910.03771. NP1intheinstructiontemplateandmanuallyeditit byexperthumansforanyinconsistencies. Itshould
Kevin Yang, Nanyun Peng, Yuandong Tian, and Dan benotedthatbothoutputqualityandinstructions
Klein. 2022. Re3: Generating longer stories with forSimileandMetaphorsaremanuallyinspected
recursive reprompting and revision. arXiv preprint arXiv:2210.06774. and agreed upon by two expert humans and only
exampleswithfullagreementarekeptinthedata.
# A Appendix
Tocreatetheinstructionfor‘Haiku’weneedtofill thetemplatewithitstitlewhichisnotalwaysread-
A.1 CreationofInstructions ilyavailable. HenceweuseYAKE(Camposetal.,
Tocreateinstructionsforaparticular“Subject"we
2018,2020),anunsupervisedautomatickeyword detect all possible noun phrases from an individ-
extractionmethodforselectingsalientwordsfrom ualpoeticsentenceandcreateanaturallanguage
theHaikuthatservesasitstitle. ForOnomatopoeia instructionforeachofthemusingthetemplatede-
we compile a lexicon containing words $^{13}$ represcribeinTable1. For“End"wefilltherespective
sentingthemandthenfilteroutsentenceswithany instructiontemplatewiththeendingwordinasen-
nounsubjectcontainingawordfromthelexicon.
tence. Forthe“Rhyme"instructionwefirstfindall rhymingwordsfortheendingwordinasentence
usingtheCMUPronouncingDictionary$^{12}$andthen
$^{13}$https://kathytemean.wordpress.com/2009/12/29/onomatopoeia-
$^{12}$https://pypi.org/project/pronouncing/ word-list/

Algorithm1Algorithmtocomputehowmuchof finalsubmittedpoemiswrittenusingmodeloutput.
Poem Draft Interactions
LetS = {i,o}bethesetofallinstructionsrequestedby theexpertsandcorrespondingmodeloutputsforasingle Write a poetic sentence that contains
poem; the word 'Mother Earth' sum_RL=0;n=num_lines(poem)
Mother earth, should be so kind.
Mother earth could get no rest.
foreachlinel∈poemdo
Mother earth could get no rest.
max_rouge=−1 max_tuple=None
foreach(i(cid:48),o(cid:48))∈Sdo Mother earth could get no rest.
rouge_score=RougeL(o(cid:48),l) Inspite of always trying her best. Write a next sentence in a poetry given the ifrouge_score>max_rouge:then previous sentence 'She always tried her best.'
max_rouge=rouge_score
Mother earth could get no rest.
max_tuple=(i(cid:48),o(cid:48)) Inspite of always trying her best. But her heart was shattered, endif It was because her heart was shattered. But she never felt like she was enough,
endfor sum_RL=sum_RL+max_rouge Write a metaphor about 'climate change'
S(cid:48) =S;S(cid:48) =S(cid:48)−max_tuple;S =S(cid:48) endfor Climate change is a silent killer.
Climate change is a famine that slays the poem_RL=sum_RL/n people.
Write a poetic sentence that contains the word 'earth' and ending in 'tattered'
B PoemsfromUserStudy Mother earth could get no rest. And the earth, smothered by the weight,
Inspite of always trying her best. lies tattered and bare.
We attach further examples of poetry written in I At sw pa ls a nb ee tc a eu ars te h ,h se mr h oe thar et r ew da bs ys h that et ered. T rih pe p ee da r at nh d i s t at tr te em reb dl .ing, the stele is being weight, lies bare and tattered.
collaborationwithCoPoetinFigures6to9. These include instances where the user selects none of
theoptionspresentedtothem(Figures6and8)and
Figure 6: Poem entitled ‘Climate Change’ written in highly intertwined collaboration where the user
collaborationwithCoPoet.
frequentlyrewritesmodeloutput(Figure9). Additionally,Figure10isawordcloudofthetitlesof
allthepoemswrittenbytheusers.
C UserInterface
Poem Draft Interactions
Asnapshotofourinterfaceduringtheuserstudy
Write a poetic sentence that contains can be found in Figure 11. The user is presented the word 'car'
withatextboxtoedittheirpoemdraftalongwith I sat in my car and listened to the radio.
A man in his car with the lights on.
a dialog box to query the model. From an initial
I sat in my car and listened to the pilot,weobservedthatsomeuserswerenotableto radio.
effectivelywriteinstructions. Asaresult,wechose
I sat in my car and listened to the to provide instruction templates as part of the in-
radio.
terface in the form of radio buttons (Figure 11). I’d not budge, I didn’t want to go. W ther i wte o a r dp o 'le ot si sc ' sentence that contains
Thiswasaimedatinformingnovicewritersofthe
And a sense of loss pervading everything.
kindofinstructionsthatelicitcreativelinesoftext I sat in my car and listened to the radio. And loss of life, and wounds, that must be borne.
I’d not budge, I didn’t want to go.
(rhymes, metaphors, etc.) from the model which And loss of life, and wounds, that must be borne. Write a poetic sentence containing
they can then use to write better poems (which 'judgement' and ending in 'upon' wenotedinsomefeedbackobtainedfromcrowd-
And thou shalt see the judgment workers). However, this also primes the users to I I ’s da nt oin t bm uy d gca er , Ia n dd id l nis ’tt e wn ae nd t t to o t gh oe .r adio. p Ar no dn o thu en c jued d gu ep mo en n. t is nigh on ye upon.
And loss of life, and wounds, that must writeinstructionssimilartothetemplates—almost
be borne.
And thou shalt see the judgment alltheinstructionsusedbythecrowdworkersbe-
pronounced upon.
longedtothetemplatesprovidedintheinterface(or novelcombinationsofthese). Inthiswork,wedid
notperformanextensivecomparisonofdifferent
Figure7: Poementitled‘CourthouseParkingLot’writinterfacedesignswhichcouldinfluencetheeffec- tenincollaborationwithCoPoet.
tivenessofhuman-AIcollaboration. Ourmaingoal is to design and test the instruction tuning setup

Poem Draft Interactions
Write a poetic sentence that contains the word 'dreams'
And he who, in the dreams of the night.
And in your dreams, I am with you.
Write a simile about 'shattered dreams'
My dreams shattered like a glass bottle.
My dreams shatter like a glass ceiling
My dreams shatter like a glass ceiling
Write a next sentence in a poetry given the previous sentence 'My dreams shatter like a glass ceiling
As you walk away, dragging a broken shard.
My dreams shatter like a glass ceiling When I see your empty eyes.
As you walk away, dragging a broken shard
My dreams shatter like a glass ceiling
As you walk away, dragging a broken shard
I watch you leave, you no longer have Write a next sentence in a poetry given the previous meaning sentence 'I watch you leave, you no longer have
meaning'
Figure10: Wordcloudofdifferentconceptsfromtitles
My dreams shatter like a glass ceiling As I lay there in the dark, the sand is cold.
As you walk away, dragging a broken I'm left with nothing, a void of emptiness ofPoetry.
shard
I watch you leave, you no longer have meaning
As I lay there in the dark, my heart turns hard specificallyforthepoetrywritingtask,whichwas
why we chose to retain the interface design with thetemplates. Theuserinterfaceensuresthatmost
Figure8: Poementitled‘GlassCeilings’writtenincol- of the queries to the model follow the same temlaborationwithCoPoet. plates which need not be the case in deployment.
From very preliminary experiments, we see that
InstructGPT3outperformsourfine-tunedmodelon
Poem Draft Interactions completelyunseeninstructions,andweintendto investigatethissettingindetailgoingforward. We
Write a poetic sentence ending in
'violin' believethatasweprovideuserswithgreaterflex-
I'm not mollycoddled. the storm is my ibility in how to use the interface, the associated violin.
A song in their heart and another in the modelmustbeabletorespondrobustlytotheedge violin.
She has a song in her heart and another cases that users might provide and hence needs in her violin. Write a next sentence in a poetry given the previous
sentence 'She has a song in her heart and another in extensiveroundsofpilotingpriortodeployment.
her violin.'
She has a song in her heart and another in her violin. She plays both with such passion.
I listen to her play them both She plays them both beautifully.
beautifully,
She has a song in her heart and another Write a poetic sentence that contains the word in her violin. 'harmony' and ending in 'begin'
I listen to her play them both beautifully, Then, when thy heart to love again begins.
In the garden, a riot of color, when the In the garden, a riot of colour, when the harmonies begin. harmonies begin.
She has a song in her heart and another in her violin.
I listen to her play them both beautifully,
In the garden, a riot of color, when the harmonies begin.
A flower that has since bloomed where grief had been.
Figure9: Poementitled‘PetalMelody’writtenincollaborationwithCoPoet.

Figure11: SnapshotofCoPoet: CollaborativePoetryWritingwithInstructions