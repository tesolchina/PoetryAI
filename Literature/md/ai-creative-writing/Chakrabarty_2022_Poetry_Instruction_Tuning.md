---
source_pdf: Chakrabarty_2022_Poetry_Instruction_Tuning.pdf
converted_date: 2025-12-04T20:09:43.915493
total_pages: 16
model: Google Gemini 2.0 Flash
total_cost_usd: $0.005083
prompt_tokens: 18,054
completion_tokens: 8,193
---

# Help me write a poem: Instruction Tuning as a Vehicle for Collaborative
# Poetry Writing
TuhinChakrabarty1∗ VishakhPadmakumar2∗ HeHe2,3
1DepartmentofComputerScience,ColumbiaUniversity
2CenterforDataScience,NewYorkUniversity
3DepartmentofComputerScience,NewYorkUniversity tuhin.chakr@cs.columbia.edu, vishakh@nyu.edu, hhe@nyu.edu
Abstract Poem Draft Interactions
Recent work in training large language mod-
Write a simile about 'cake' els(LLMs)tofollownaturallanguageinstruc-
A cake is like a cloud of joy.
tionshasopenedupexcitingopportunitiesfor A cake is like a piece of heaven.
natural language interface design. Building The cake is like a cloud of joy.
Suggest a verse to follow the on the prior success of LLMs in the realm of sentence 'The cake is like a
computer-assisted creativity, we aim to study cloud of joy' if LLMs can improve the quality of user- The frosting is like a rainbow.
So soft so fluffy, I could cry.
generated content through collaboration. We The cake is like a cloud of joy.
presentCoPoet,acollaborativepoetrywriting The frosting is like a rainbow.
system.Incontrasttoauto-completingauser’s text, CoPoetiscontrolledbyuserinstructions
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
outthesystem.1
# 1 Introduction Theadoptionofthesetechnologieshingesontheir
abilitytoprovideappropriatesuggestionswhilebe-
Advancements in large language models (LLMs) ingeasytointeractwith. However,therehasbeen
havemaderemarkableprogresstowardsgenerating limited research on the effectiveness of such col-
coherent text in a wide variety of domains. This laboration,e.g.,whethertheassistantunderstands
hasspurredincreasinginterestincomputer-assisted user intents and whether collaboration improves
creativity(Seeetal.,2019;ElkinsandChun,2020; thefinaloutcome.
Rameshetal.,2022;Branwen,2020)suchasbuild-
Inthispaper,weaimtounderstandthecollaboingco-creativeassistantsforwritingstories,poems,
rationcapabilitiesofLLMsthroughacasestudyof andargumentativeessays(Leeetal.,2022;Swan-
collaborativepoetrywriting. Writingapoemisofsonetal.,2021;Uthusetal.,2019;Donahueetal.,
tenachallengingtaskbecauseitisbothopen-ended
2020;PadmakumarandHe,2022;Duetal.,2022).
andhighlyconstrained. Unlikestoriesorotherar-
∗BothAuthorsContributedEqually gumentativetexts,inordertowriteapoemweneed
1Ourcode,preprocesseddata,models,andtheinteraction creative content that satisfies various long- and
logsfromouruserstudyareavailableathttps://github.
com/vishakhpk/creative-instructions short-rangeformconstraintssuchasrhyme,meter,
2202 tcO
52
]LC.sc[
1v96631.0122:viXra

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
Iwanttomakeyoufeellikeaflowernear andendswithvolcano;ortheymaybelookingfor
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
# 2 Data
multiple constraints. Both automatic and human evaluationshowthatourfinetunedmodelsatisfies To train a model to follow instructions, we need
theconstraints86%ofthetime,10%betterthana <instruction, poem_line>pairswherethetext muchlarger175BversionofInstructGPT(Brown satisfiestheinstruction. Thekeychallengetobuild-
etal.,2020). Onunseencompositionalinstructions, ing such a model is the lack of parallel data, so our best model satisfies them 77.6% of the time, we collect our own dataset of creative writing in-
outperformingInstructGPTbyamarginof28%. structionsfrompubliclyavailablepoemcorporaor
Tounderstanditscollaborationcapabilities,we relevantsubredditsfromReddit(Table7).
run a user study on Amazon Mechanical Turk Based on some initial feedback from profes-

sional poets, we decided to include 3 major # 3 HowWellDoLLMsFollow types of instructions: 1) Continuation based in- Instructions?
structions that suggest content when writers are
In this section, we first describe our models and blocked/cluelessonhowtoproceed;2)Instructions
baselines,followedbytheevaluationresultsusing on Lexical Constraints to enable greater control
both automatic metrics (Section 3.3) and human of poetic form such as rhyme, sound, and meter.
evaluation(Section3.4).
Theseareinstructionsthatforcelanguagemodels toobeyspecificchoicessuchasgeneratingaline
## 3.1 ExperimentSetup
thatcontainsaspecifictopic,startword,endword or a sentence with a particular rhyme; 3) Instruc- Model Details We finetune the pretrained T5
tionsonRhetoricaldevicesthataremostlyusedfor (Raffel et al., 2020) and T0 (Sanh et al., 2021) introducingembellishmentsandimageryinapoem modelsfromHuggingFace(Wolfetal.,2019)on
suchasmetaphor,similes,andonomatopoeia. the collected data (Section 2) to produce the outputgiventheinstructionusingcross-entropyloss.
Table1showstheprimaryinstructionsusedto WereportresultsonfinetunedT5-3B,T5-11Band trainourmodels. Theseinstructionsarecraftedby T0-3Bmodels,whicharehenceforthreferredtoas
theauthorsofthepaper,whoconverteverypoem T5-3B-poem,T5-11B-poem,andT0-3B-poem. We linetoan<instruction, poem_line>pairusing selectthehyperparametersbythevalidationloss:
rules. forT5-11B-poem,weusetheAdamoptimizerwith a learning rate of 1e−4; for T5-3B-poem and T0-
Eachinstructionconsistsofatemplate(unique 3B-poem, weusetheAdafactoroptimizerwitha totheinstructiontype)andoneormorearguments, learningrateof1e−3. Eachmodelistrainedfor3
as can be seen in Table 1. Given a poem line in epochswithearlystoppingbasedonvalidationloss.
thecorpus,wereverse-engineertheinstructionby WefinetuneallmodelsonanA100GPUanduse picking a template and extracting the arguments Deepspeed(Rasleyetal.,2020)integrationforthe
fromthepoemline. Forcontinuationinstructions, 11Bmodel. Duringfinetuning,werestrictthemaxweusethepreviouscontextastheargument. For imumsequencelengthofboththesourceandthe
instructionsonlexicalconstraints,weextractnoun targetto64tokens(viatruncation).4 Atinference phrases and start/end words as arguments using time, we generate output sequences using top-k
NLTKfortokenization. Toconstructinstructions samplingwithk = 5andatemperatureof0.7per on rhymes, we use the CMU dictionary to find recommendationsfromearlierworkinopen-ended
rhymingwords.2 WedescribemoredetailsinAp- creativetextgeneration(Fanetal.,2018;Holtzman pendix A on how we create instructions for each etal.,2020;PadmakumarandHe,2022).
particulartype. Baselines We compare our finetuned models
Toallowmodelstoadapttolinguisticvariations withtwoothermodels: (i)theT0ppmodel(Sanh oftheinstructiontemplates,wealsoincludepara- etal.,2021),trainedoninstruction-basedprompts
phrases of the instruction templates, e.g., instead from49datasets;5 and(ii)the175Bdavincivariant of “Write" we also use“Generate”, or instead of ofInstructGPT(Ouyangetal.,2022)thatistrained
“Writeasentenceabout”weuse“Writeasentence onhuman-writteninstructionsondiversetasksina thatcontainstheword”or“Writeasentencethat human-in-the-loopfashion. Givenaninstruction,
includestheword”. Intotal,ourdatasetconsistsof wegeneratetextdirectly(i.e.zero-shot)fromT0pp
873,574<instruction, poem_line>pairswhich usingtop-ksampling(Fanetal.,2018).
we randomly split into 808,180 train and 65,394 For InstructGPT, we evaluate on both zeroheld-outvalidationexamples.3 Weevaluateperfor- shot and few-shot settings. For zero-shot, the
manceonthreetestsetsofhand-craftedinstructions prompt consists of only the instruction. For fewofvaryingdifficulty(Section3.2). shot, the prompt consists of 26 <instruction,
4Thelengthlimitischosentoavoidmemoryexplosion.It hasminimalimpactonmodelperformancesincemostverses
areshorter.
2https://pypi.org/project/pronouncing/ 5These include question-answering, summarization,
3Our dataset is publicly available at https://github. structure-to-textgeneration,sentimentandtopicclassification com/vishakhpk/creative-instructions. tasksbutnoexplicitcreativewritingtasks.

poem_line>pairsfromourtrainingdata(selected Writeapoeticsentencethatstartswiththe
Start tocoveralltheinstructiontemplates),followedby word‘Maybe’andendingin‘void’
+End thetestinstruction.6 WeusetheOpenAIAPIwith Maybeoneday,youwillfindmeinthevoid
a temperature of 0.7, no frequency penalty, and
Writeapoeticsentencethatcontainsthe a maximum sequence length of 64 to match our
Subject word‘breaks’andendinginawordwhich setting.
+Rhyme rhymeswith‘bound’
## 3.2 TestSets Shecracksandbreaksandhitstheground.
While our training instructions cover many tem- Writeanextsentenceinapoetrygiven
Next theprevioussentence‘Everyonceawhile plates and topics, user instructions may deviate Sentence Ilowertheblinds’andendingin‘play’
from the training distribution during interaction. +End Waitingforsomeonetocallmeouttoplay
To evaluate the generalization capabilities of the
Writeametaphorthatincludestheword models,weidentifythreesettingswithincreasing Metaphor
‘film’andendingin‘thought’ difficulty based on whether the instruction tem- +End
Afilmisapetrifiedfountainofthought.
platesorargumentsareseenduringtraining.
Table 2: Examples of compositional natural language
Known Instruction Templates with Known Ar- instructions for creative tasks paired with their respecguments(KIKA) Thesimplestsettingrequires tiveoutputsfromourtestsets.
themodeltogeneralizetonovelcombinationsof thetemplatesandarguments. Specifically,wecre- tionsaccordingtotheabovecriteria,followedby
ateinstructionswhereboththetemplatesandthe manualverification.
arguments are seen in the training set, although eachspecificcombinationisunseen(i.e.thetrain- ## 3.3 AutomaticEvaluation
ingandtestsetshavenooverlappinginstructions).
Weevaluatehowwellthemodelssatisfyconstraints
Known Instruction Templates with Unknown specifiedintheinstructionsoneachofthetestsets
Arguments (KIUA) To handle novel concepts (Section 3.2). We report the success rate of satisfrom users, the model must generalize to unseen fyingtheinstructionswherethesuccesscondition
arguments, which may include new entities or foreachinstructiontypeislistedinTable3.7 phrases. Forexample,itmightbeeasierforamodel
towriteapoeticsentenceaboutaknownargument Instruction SuccessCondition
Type such as beauty, but difficult to write about an un-
Rhyme Lastwordofthemodelgeneration known argument beauty without virtue. For this rhymeswiththedesiredsubjectusingthe
set,weincludeinstructionswheretheinstruction CMUPronouncingDictionary templates are seen during training but the corre- Haiku Modelgenerationcontains15–19
syllablesandcontainsthedesiredsubject spondingargumentsareunseen.
Simile/ Modelgenerationcontainsthedesired
Unknown Compositional Instruction Tem- Metaphor subjectaswellasacomparator plates One of the main benefits of natural Start/End First/lastwordofthemodelgeneration
matchesthedesiredsubject language instructions is that they can be easily
Subject Modelgenerationcontainsthedesired composed in new ways to cover various user subjectintheinstruction
intentions. This is particularly useful in creative
Table 3: Success conditions for different instruction writing because it enables users to request text
templates.
from the model with multiple constraints. Therefore, wealsotestwhetherthemodelunderstands FinetunedModelsHaveStrongIn-DomainPer-
compositional instructions using two templates, formance but Drop on Out-of-Domain Data as seen in Table 2. Our model is exposed to a Figure2showstheaveragesuccessrateandstan-
single compositional template during training: dard deviations of each model on the three test
Subject+End. Forthistestset,wecreateavariety setsacross5modelinferencestoaccountforvariofunseencompositions.
7Prior work on instruction tuning reports metrics such
Intotal,wecreate242testexamples(82KIKA, asBLEUscoreforgenerationtasks(Sanhetal.,2021;Wei
82KIUA,78compositional)byselectinginstruc- etal.,2021)andtheseareunsuitableforourpoetrywriting instructions,thuswedefinecustomsuccessconditions.
6Theexactpromptcanbefoundinourcoderepository.

T5-11B-poem ency,accuracy,andcreativityofthegenerationby
80
T5-3B-poem answeringthefollowingquestions:
T5-11B-poem
T0-3B-poem
• Ratethefluencyofeachverseonascaleof1–5.
60 T0pp
InstructGPT-FS
• Doeseachverseadequatelysatisfytheinstruc-
InstructGPT-ZS
40 tion? (Yes/No)
• Which of the two verses is more cre-
20 ative/interestingwhilebeingcoherentandsatis-
fyingtheinstruction?
0
Thefirsttwoquestionsevaluatethequalityofeach
KIKA KIUA Compositional verse against the instruction individually. In ad-
dition to satisfying the constraints in the instruc-
Figure 2: Automatic evaluation of models on KIKA, tionwithfluenttext,wewantthemodeltoprovide
KIUA and Compositional test sets. The y axis is the novelsuggestionsthatarehelpfulforcreativewrit-
percentageofinstructionsthateachmodelsuccessfully satisfiesasdeterminedbythecriteriainTable3. Were- ing. Thus we also ask the annotators to compare
portresultsonT5-11B-poem,T5-3B-poemandT0-3B- thetwoversesandprovideasubjectivejudgement poemalongwiththebaselines—zero-shotT0pp(Sanh on which one is more creative. We collect three
etal.,2021)andzero-shot(ZS)/few-shot(FS)Instruct- annotationsforeachquestionandusethemajority
GPT(da-vinci)(Ouyangetal.,2022). Eachbarshows voteasthefinaljudgement.
the average success rate of 5 model inferences along withthestandarddeviation.Onaverage,T5-11B-poem T5-11B-poemSatisfiesInstructionsBetterthan
achieves the highest success rate and InstructGPT is Few-Shot InstructGPT Table 4 shows the hua strong few-shot baseline that obtains comparable re- man evaluation results on all three test sets. We
sultsonKIUA. findthat,onaverage,modelgenerationsfromT5-
11B-poemsatisfythegiveninstructionsbetteron anceintop-ksampling. OnbothKIKAandKIUA, allthreetestsets,whileInstructGPTisratedtobe
T5-11B-poemhasthehighestaveragesuccessrate. morefluentconsistently. Wefindthatgapinsatis-
T5-3B-poemandT0-3B-poemoutperformthefewshotandzero-shotbaselinesonbothtestsets. How-
T5-11B-poem GPT3-FS ever, these finetuned models suffer a big drop in
Success% 86.2 76.9 performancefromKIKAtoKIUA—T5-11B-poem KIKA(82) Fluency 0.739 0.794
suffersarelativedropof51.09%froma73.2%suc- Creative 53.8 46.2 cess rate on KIKA to a 35.8% rate on KIUA. In Success% 92.5 86.5
KIUA(82) Fluency 0.773 0.781 contrast, the few-shot InstructGPT baseline only
Creative 56.7 43.3 suffers a relative drop of 30.4% from a success
Success% 77.6 55.2 rateof46.6%onKIKAto32.4%onKIUA.This Comp(78) Fluency 0.697 0.751
result is consistent with prior findings that task- Creative 47.7 52.3 specific finetuning may destroy pretrained repre-
Table4: Humanevaluationofmodelgenerationsfrom sentationwhichleadstodegradingperformanceon
T5-11B-poemandfew-shotInstructGPT3ondifferent other non-finetuning tasks (Aribandi et al., 2021;
testsetsacrossthreemetrics: (i)successrate: percent-
Padmakumaretal.,2022). Withoutfinetuning,inage of instructions satisfied; (ii) fluency: average flu-
domain examples are still helpful though: on all ency score on a scale of 5 normalized to [0,1]; (iii)
testsets,theInstructGPTfew-shotbaselineoutpercreativity: percentage of generations rated to be more
formsthecorrespondingzero-shotbaselinealong creative/interestinginapairwisecomparison.
withareductioninvarianceacrossruns.
Larger Models Compose Instructions Better fying instructions is largest on the compositional
On compositional instructions, we find that T5- testset—T5-11B-poemaccuratelyanswers77.6%
11B-poem has the best average performance. In of compositional instructions while InstructGPT addition,thereisaclearperformancegapbetween onlymanages55.2%. Annotatorsalsoreportedthat
the11Band3Bmodels,showingtheimportanceof versesfromT5-11B-poemweremarginallymore modelscaleforcomposition,similartorecentob- creative/interestingthanInstructGPTonKIKAand
servationsofemergentabilitiesinLLMs(Weietal., KIUA test sets and less so on the Compositional
2022). Wealsofindthatfew-shotInstructGPTout- test set, indicating that the two models may have performs T5-3B-poem and T0-3B-poem despite littledifferenceincreativity.9
havingnocompositionalinstructionsintheprompt.
We observe that InstructGPT is a strong base-
Thisindicatesthatsmallermodels,whenfinetuned line, outperforming T0pp by a large margin on
on instructions, tend to overfit to templates seen automatic metrics, and satisfying nearly 80% of
during training, which hurts their generalization the instructions in the KIKA and KIUA test sets
capability,asalsoreportedinWeietal.(2021).
accordingtohumanevaluation. However,acom-
## 3.4 HumanEvaluation monerrorcaseoncompositionalinstructionsisthat
Sinceourautomaticmetricsarenotalwaysaccurate whilethemodelgenerationsalmostalwayscontain inmeasuringifaninstructionissatisfied,wealso theargumentsmentionedintheinstruction,theydo
performhumanevaluationbyhavingcrowdwork- notalwayssatisfytheconstraintscorrectly—when ersmanuallycheckifmodelgenerationssatisfythe askedforaversethatcontainstheword‘soul’and
instructionconstraints. Giventheautomaticeval- endswith‘yellow’,InstructGPTgeneratedtheline uationresultsinSection3.3,wecompareourbest “Mysoulisasyellowasthesunonasummerday”
finetuned model, T5-11B-poem, against the top thatcontainsthoseargumentsbutnotatthespeciperformingbaseline,few-shotInstructGPT.Specif- fiedpositions.
ically,weconductpairwisecomparison: eachan-
Takeaways We observe that on average finenotator is shown an instruction and generations
tuned models tend to outperform the few-shot frombothmodels.8 Theyareaskedtoratetheflu-
baselinesonin-domaininstructions(Section3.3).
Whilesmallermodels(T5-3B-poem,T0-3B-poem)
8Wesample5generationsfromeachmodelandselectthe have worse performance on out-of-domain in-
bestoneusingthecriteriainTable3. Ifmultiplecandidates areevaluatedassuccess,werandomlysampleone. structions, finetuned models at scale (T5-11B-
poem) generalizes to compositional instructions
9Thefirsttwoquestionsarelesssubjectivethanthethird question. Usersunanimouslyagreed52.2%ofthetimeon
whether model generations satisfied instructions and only
37.3%onwhichoutputismorecreative.

effectively,evenoutperformingInstructGPT(Section3.4). Theflexibilityofcomposinginstructions
makes the model more suitable as a collaborator forahumanuser;henceweuseT5-11B-poemas
the assistant for our subsequent collaborative experiments.

# 4 CoPoet: CollaborativePoemWriting
Our results in Section 3.4 demonstrate CoPoet’s abilitytosatisfytheconstraintsspecifiedinthein-
structions. This presents us with an opportunity
Topic: Decadence totestthemodel’scapabilityincollaborativewrit-
ingtasks. Wedesignouruserstudy(Figure3)to
Solo Writer CoPoet
----------
----------
---------answerthefollowingtwomainresearchquestions:
1) ---
2) ---
3) ---
• RQ1: Canuserswritepoemsonanytopicof theirchoicebycollaboratingwithCoPoet?
RQ1: Can users collaborate with
D Oe pc ea nd ue pn c Ine s ( t1 a ) and you'll see CoPoet to write poems?
All of the pleasures you'll ever need.
• RQ2: Does CoPoet help users write better
All competing for likes and comments. Decadence (2)
Photos of food, cars, and female models.
poemscomparedtowhentheywritealone?
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
trainedtorespondto,sothattheyhaveanideaof whatthemodeliscapableof.10 getting ideas from the model about the Next Sen-
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
Do experts find CoPoet helpful as a writing model assistance.11 Third-party annotators were
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
10Weexplicitlymentionthattheycanusenovelinstructions
What fraction of the poems is written by notpresentinthetemplates.
CoPoet? To quantify the contribution of the
11We ensure that the same author does not write on the sametopicinthetwosetups. model,wecomputetheproportionofthesubmitted

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
poems is evaluated by 3 distinct annotators. We
Figure 5: Content overlap between sentences of an thenaggregatethejudgmentsviamajorityvoting.
individual poem and the corresponding model sugges- Table 5 shows that both poems written by solo tionscalculatedusingRouge-Lrecall.Yaxisshowsthe writersandpoemswrittencollaborativelyareaccu-
percentageofpoemsoutof50whileXaxisshowsthe rate. We are encouragedtoseethatcollaborative amountofCopoetcontributionintermsofRouge-L. poems are preferred more than poems written by