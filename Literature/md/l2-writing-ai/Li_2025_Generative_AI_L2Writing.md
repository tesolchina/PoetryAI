---
source_pdf: Li_2025_Generative_AI_L2Writing.pdf
converted_date: 2025-12-04T20:21:07.614254
total_pages: 31
model: Google Gemini 2.0 Flash
total_cost_usd: $0.005515
prompt_tokens: 22,379
completion_tokens: 8,192
---

# Digit.Stud.inLang.andLit.2025;2(1):122–152
Shaofeng Li*
# Generative AI and Second Language Writing
https://doi.org/10.1515/dsll-2025-0007
ReceivedApril22,2025;acceptedMay11,2025;publishedonlineJune11,2025

**Abstract:** Thisarticleprovidesacriticalsynthesisandanalysisoftheresearchon
theapplicationofgenerativeAI(GenAI)insecondlanguage(L2)writing.ItconceptualizesGenAIliteracy,synthesizestheresearchonwrittenfeedback,establishesa
frameworkforpromptengineering,critiquestheresearchexaminingthevalidityof
GenAI ratings in writing assessment, and summarizes empirical evidence on the differencesbetweenGenAIandhumanwriting.Specifically,thefollowingfindings
and arguments are presented and discussed. GenAI literacy consists of four componentspertainingtousers’competenceandknowledgeofGenAIbasics,effective
use, output evaluation, and ethics. The research on written feedback shows that teacherfeedbackfocusesmoreoncontent,whileGenAIfeedbackfocusesmoreon
organization. This research also suggests a need for criteria-based feedback and feedbackevaluation.Promptengineeringisdiscussedalongthreedimensions:input,
task,andoutput,followedbysnapshotsofpromptsusedinfeedbackresearch.The studies onwritingassessment reveal that GenAIratings are moreconsistent with
human ratings when GenAI is trained using a large number of scored essays and whentheratingcriteriaarewell-defined.ComparisonsofGenAIandhumanwriting
demonstrate that GenAI writing is moreformal, academic, and impersonal, while humanwritingismorepersonal,creative,andlinguisticallyaccessible.Thisarticle
concludes by making sense of the research findings, identifying future directions, and proposing three principles that may guide the research, practice, and theory
constructionforGenAI:individualization,domain-specificity,andwriteragency.

**Keywords:** generativeAI;ChatGPT;secondlanguagewriting;correctivefeedback;AI literacy;writingassessment

# 1 Introduction
WiththelaunchofChatGPTinNovember2022,generativeAI(GenAI)hasusheredin anewerainhumanhistory.GenAI,representedbyChatGPT,DeepSeek,andother
programswithsimilarfunctions,isatechnologythatleveragespatternsextracted
*Correspondingauthor:ShaofengLi,TheHongKongPolytechnicUniversity,Kowloon,HongKong,
E-mail:shaofeng.li@polyu.edu.hk
OpenAccess.©2025theauthor(s),publishedbyDeGruyteronbehalfofChongqingUniversity,China
ThisworkislicensedundertheCreativeCommonsAttribution4.0InternationalLicense.

GenAIandL2Writing 123 fromtrainingmaterialstogenerateresponsestohumaninquiriesbypredictingthe
most likely next words.GenAI has thefollowing characteristics. First, it is a large language model based on linguistic probabilities; therefore, its outputs are deter-
mined by linguistic contingencies and the strengths of bonds between linguistic units. Because it is a language model and is not based on contextual, rhetorical,
pragmatic, or semantic cues, it may generate responses that are linguistically coherentbutsemanticallyillogicalandunreasonable.Second,itisgenerativeinthat
it can produce new information based on existing input materials. The input materialsarepubliclyavailablematerialsselectedandfedbyITspecialists,engineers,
orpersonnelwhosequalificationsareunknown.Theselectioncriteriafortraining materialsarealsounknown.ThelatestupdatetothetrainingmaterialsforChatGPT,
probablythemostpopularGenAItool,occurredinOctober2023.Itisimportantto clarifythatGenAIisnotconnectedwithanyexternalsourceofdata,northeInternet,
so there is no ongoing learning. It is also necessary to clarify that according to
ChatGPT,userresponsesarenotusedfortrainingpurposes,whichmayhelpdispel qualmsandconcernsoverprivacyandconfidentiality.Third,itisinteractiveandcan
engageinhuman-likeconversationswithusers.Itmaygeneratemultipleturns,keep previousturnsinmemory,andretrieveandprocesspreviouslystoredinformation
whenrequested.However,thekindofinteractionitengagesinwithuserslackskey features of natural conversations (Voss and Waring 2024). For example, it is not
sensitivetousercharacteristicsanddoesnotuseappropriatecommunicationstrategiesin responsetouser differences; it alsodoesnotmakeconstantadjustments
basedontheflowoftheconversationandongoingdynamics.Fourth,itsimulates humanintelligenceandhastheabilitytoperformvarioushigher-ordertasksthat
require or involve information processing such as analyzing, categorizing, comparing,inferencing,reasoning,summarizing,andsoon.

GenAI’sversatilityisevidentinsecondlanguage(L2)writing.WriterscanuseGenAI to brainstorm ideas, create outlines, summarize source information, translate infor-
mationintheirfirstlanguageintothesecondlanguage,searchforL2formsthatmatch planned messages, proofread their essays for language, content, and rhetoric, etc.
TeacherscanutilizeGenAItoevaluateandprovidefeedbackonstudents’writing, which is logistically challenging given the large number of assignments teachers
have to evaluate. Other issues such as teachers’ failure to recognize errors and provide accurate, consistent feedback, as well as struggles teachers experience in
providingfeedbackontheorganizationalaspectsofwriting(Lee2008;LiandVuono
2019;Truscott1996),canbeeasilyaddressedwiththeassistanceofGenAI.Inaddition tobenefitingstudentsandteachers,GenAIhasbroughtopportunitiestoresearchers,
whose research territory and terrain have been expanded and reshaped. Despite

124 S.Li
GenAI’saffordancesandopportunitiesforL2writing,thereisalackofguidanceon itseffectiveuse,therearepitfallsthathavebeenidentifiedbyresearch,andmany
pressing issues remain unexplored in the research. This article synthesizes the various strands of research investigating the role of GenAI in second language
writing, including GenAI literacy, feedback on L2 writing, prompt engineering, discoursecomparisonbetweenGenAIandhumanwriting,andethics.Integratedinto
thesynthesisofresearchfindingsisadiscussionofnewconceptsandtheimplications of the research for theory construction, further research, and L2 writing
practiceandpedagogy.

# 2 GenAI Literacy
GenAI literacy refers to users’ knowledge of the fundamentals of GenAI’s mechanism,ethics,affordances,andlimitations,andusers’abilitytoeffectivelyuseGenAI.
GenAIliteracyisanimportantconceptduetoGenAI’subiquityandlimitationsand users’ lack of knowledge about how to maximize the benefits of this new techno-
logical tool. It is important to clarify that GenAI literacy involves not only users’ awareness of GenAI’s limitations (bias, inaccurate output, etc.), but also users’
understandingofitsfunctionsandstrategiestoleverageiteffectively.GenAIliteracy entails both declarative knowledge – knowledge about its operational principles,
affordances,etc.–andalsoproceduralknowledge–knowledgeabouthowtoactually applyGenAI tosolveproblems. Whereas declarativeknowledgetakes theform of
awareness and mental representations, procedural knowledge is demonstrated through performance, behavior, and use. Thus, literacy goes beyond mere aware-
ness, although it is often interpreted and operationalized as awareness; in other words,itincludesboth“knowledgeabout”and“knowledgehow”.Itisnecessaryto
further clarify that declarative knowledge is not restricted to metacognitive knowledge,suchasacknowledgingtheimportanceofAIliteracy(e.g.,“It’simportant
to learn how to use GenAI”), or confirming knowledge (e.g., “I am aware of the limitations of GenAI”). Measures of GenAI literacy must include items that target
specificaspects,suchasstrategies foreffectivepromptengineering, aswellasactivitiesthatrequireuserstodemonstratetheirGenAIcompetencethroughbehaviors
ortaskperformance.

GenAIliteracyisarelativelynewconceptderivedfromthenotionofAIliteracy, soitsconceptualizationandmeasurementaresimilartogeneralAIliteracy.Basedon
athoroughreviewoftheresearch,Ngetal.(2021)identifiedfourcomponentsforthe constructofAIliteracy:(1)knowandunderstand,(2)use,(3)evaluateandcreate,and
(4)ethicalissues.Ngetal.mappedthefirstthreecomponentsontoBloom’staxonomy

GenAIandL2Writing 125 ofcognitiveskills,whichstandinahierarchywithsixlevelsdefinedintermsofthe
informationprocessingdemandsrequiredateachlevel.Rankedfromthelowestto thehighestcognitivedemands,theseskillsincludeknow,understand,apply,analyze,
evaluate,andcreate.AppliedtoNgetal.’s(2021)frameworkofAIliteracy,thestageof
“knowandunderstand”involveslearningthebasicsofAIincludingitsmechanism andfunctions;“use”referstohowtoapplyoruseanAItooltosolveproblems;and
“evaluateandcreate”aretwohigh-orderskillsusersdrawontoassessthequalityof
AIoutputandcreatenewapplications.Thefourthcomponent,ethics,permeatesall stagesofAIuseanddoesnotfallintothehierarchyofcognitivethinking.Drawingon
Ngetal.’s framework,Warschauer etal.(2023)proposedasimilarframeworkfor
GenAI literacy for second language writing, which also applies to L2 learning in general.Inthisframework,GenAIliteracyhasfivecomponents:understand,access,
prompt, corroborate, and incorporate. “Understand” is similar to “know and understand” in Ng et al.’s framework, “access and prompt” corresponds to “use”,
“corroborate”isequivalentto“evaluate”,and“incorporate”hasnocounterpartin
Ngetal.,butitcanbeconsideredpartofethicsasitmainlyconcernsproperuseof
GenAI output. Wang and Wang (2025) conducted a small-scale exploratory, observationalstudyinvestigating10L2Englishwriters’GenAIuseandliteracyinawriting
classataliberalartscollegeintheU.S.TheL2writersworkedonawritingassignmentusingChatGPT.TheymadereflectionsontheiruseofChatGPTandparticipated
insemi-structuredinterviews,andtheprocessoftheirusingChatGPTinwritingwas captured via a screen recorder. Based on the multimodal data they collected, the
researchersproposedamodelofcriticalGenAIliteracy,emphasizingthecriticaldimensionsofGenAIliteracy.Themodelconsistsoffourcomponents:criticalawareness
(akinto“understand”and“knowandunderstand”intheabovementionedmodels), critical strategies for human-AI interaction (resembling “access and prompt” and
“use”),criticalevaluationofaffordances(similarto“evaluate”and“corroborate”),and criticalpositionality.Criticalpositionality,whichismissingfromothermodels,refers
tomaintaininguseragency,autonomy,andauthorialvoiceduringGenAIuseinstead ofoverrelianceonit,whichmayrendertheauthor’sidentityinvisible.

Inthethreemodelsthatwerediscussedabove,“knowbasicsofGenAI”,“use”, and “evaluate” are common components across all the models, although they are
labeledslightlydifferently.EthicsisanindependentcomponentinNgetal.’smodel, isincludedinthe“incorporate”componentinWarschaueretal.’smodel,andispart
ofthecriticalawarenesscomponent(e.g.,bias)inWangandWang’smodel.Critical positionalityisamajorcomponentofGenAIliteracyinWangandWang’sconcep-
tualizationbutmissingfromtheothertwomodels.Basedontheanalysisofthethree models and my own understanding, I propose the following components for the
constructofGenAIliteracy.

126 S.Li
KnowledgeoftheBasicsofGenAI.ThebasicsofGenAIinclude,butnotlimitedto, themechanismofGenAI(e.g.,it’sbasedonlinguisticinsteadofsemanticprobability),
historicaldevelopment,affordances,resources(availabletools),controversies,and limitations. This type of knowledge concerns both domain-general information
aboutGenAIanddomain-specificinformationaboutGenAI’saffordancesandlimitationsinL2learning(includingL2writing).

EffectiveUse.ThisreferstousingGenAItoperformthetaskorachievetheuser’s goal,aprocessthatinvolveswhatWangandWang(2025)referredtoas“human-AI
interaction”.Thiscomponentinvolvesknowledgeaboutpromptengineering,suchas asking for criteria-based feedback when eliciting corrective feedback on one’s
writing,andstrategieswritersutilizeintheprocessesofplanning(e.g.,outlining), composing,andrevising.OneinsightprovidedbyWangandWang’s(2025)isthat
prompt engineering involves human-AI interaction, and principles for effective human communication, such as clarity, specificity, contextualization, etc. are also
applicabletoourinteractionwithGenAI.

OutputEvaluation.ThisreferstotheevaluationofGenAIoutputtodetermineifthe goalhasbeenachieved.Theevaluationmaybeunderstoodordiscussedfromtwo
perspectives: criteria for evaluation and methods of evaluation. The criteria for evaluationshouldbeformulatedintermsofwhetherthequalityissatisfactoryand
whetherauthoridentityisretainedasaresultoftheappropriationofGenAIoutput.
Quality can be operationalized as accuracy, namely, whether the output, such as feedbackgeneratedbyGenAI,isaccurate,whetherthefeedbackmeetstheevalua-
tion criteria for the task such as the grading rubric for a writing assignment, or whetherthefeedbackisclear,specific,andsupportive–criteriaappliedinresearch
toevaluatefeedbackquality.Authoridentity,whichissimilartoWangandWang’s
(2025) notion of critical positionality, is essential for the evaluation of the acceptabilityofGenAIoutput.Themaintainingofauthoridentitycanbegaugedrhetori-
callyandlinguistically,withtheformerreferringtowhethertheideationalaspectsof the author’s writing (ideas and organization of ideas) remain after incorporating
GenAIoutput,andthelattertowhetherthelinguisticaspectsofGenAIoutputarein discordwiththeauthor’sstyleandidentity.Forexample,inWangandWang’s(2025)
study, one L2 writer refused to accept the sophisticated language suggested by
ChatGPTbecausetheyfeltthelanguage“doesn’tsoundlikeme”.Maintainingauthor agency, autonomy, and identity should occupy a central place in GenAI literacy,
becauseofthepossibleoverrelianceonGenAIandthetemptationtouseGenAIasa replacement,insteadofatool,forhumanwork.Methodsofevaluationarerelatedto
how to evaluate GenAI output, and one major method is to compare, such as comparingGenAIoutputwithoutputsgeneratedbyothertools,comparingdifferent

GenAIandL2Writing 127 solutionstothesameproblemsuggestedbyGenAIsoastopickonethatmeetsthe
user’sexpectation,etc.

Ethics. As discussed below, ethics is a multi-dimensional concept consisting of multiple facets, including bias (underrepresentation of non-English cultures, bias
againstESLwritersinAIdetection,etc.),fairness,breachofintellectualpropertiesin
GenAI training, ethical use of GenAI output, and so on. For example, while it is appropriatetoincorporatelinguisticoutputfromGenAI,itisquestionablepracticeto
useGenAI-generatedinformationasresearchevidence.InWangandWang’s(2025) study, a student was unable to find sources to support “her argument about Gha-
naianfamilypractices”(p.6).ShethencitedChatGPTas“externalevidencetoback herownexperience”(ditto).However,notallinformationgeneratedbyGenAIhasan
empirical basis, and GenAI output should not be treated as research evidence.
BecauseoftheunprecedentedethicalconcernsGenAIhascaused,theimportanceof ethics in AI literacy is unparalleled. The following section addresses issues sur-
roundingGenAIethics.

# 3 Ethics
OneofthemostpressingissuesaccompanyingtheadventofGenAIisethics,which referstocommonbeliefsofthemembersofacommunityorsocietyaboutthe
appropriacy of human conduct. In current conceptualization, ethics concerns diversity,equity,andinclusion(DEI),thewellbeingofindividualsandthehumanity,
andsocialprogress.Commonprinciplesofethicsmaymanifestdifferentlywithina professionorcommunity.RegardingtheuseofGenAI,ethicscanbeunderstoodfrom
theperspectivesofbias,ethicaluse,equity,andconfidentiality,whicharediscussedin thefollowingparagraphs.

Biasreferstoincompleteorunequalrepresentationoftheintegralparts,components,members,orperspectivesofaunitorcommunity.Biascantaketheformof
over-orunder-representationofcertainstake-holders(groupsaswellasindividuals) orentitiesinaphenomenon,process,orevent.GenAIbiastakestheformoftheover-
representation of Western ideology, which underlies the training materials, all of which are written in English and contributed by English speakers. It can also be
arguedthatGenAIoutputsareimbuedwithU.S.ideologyandculturebecausethe training materials are in American English; accordingly, other ideologies and cul-
tures are underrepresented. From the standpoint of second language writing and secondlanguagelearningingeneral,secondlanguageperspectivesaremissingnot

128 S.Li onlyintrainingmaterials,butalsoinpolicy-making–L2usersarenotconsideredin
policies – as well as access – GenAI outputs are not accessible to L2 users whose
English proficiency is often limited. Bias also exists in AI detection, a topic to be revisitedbelow.

EthicaluseisprobablythegreatestconcernforGenAIuseinwritingingeneral andsecondlanguagewritinginparticular.Ethicaluseconcernswhether,when,how,
andforwhatpurposesGenAIshouldandshouldnotbeused.Thesequestionsshould and can be examined empirically. Casal and Kessler (2023) surveyed 27 journal
editorsabouttheiropinionsonacceptableGenAIuseforpublishingpurposes.16of them considered it acceptable to use GenAI to edit texts, 14 endorsed using it to
generatecomputercode,11feltitOktowriteasummaryofanarticleforpublicuse, and10thoughtitethicaltowritetheabstractofanarticle.Fewornoeditorssup-
portedusingGenAItowritepartsoforthewholemaindocument,andsixagreed with the statement that under no circumstance is it acceptable to use GenAI. In
general, it would seem that editors considered GenAI a tool that can be used to proofreadtoimprovetheclarityandreadabilityofmanuscripts,andtheythoughtit
unethicaltouseittogeneratenewcontentorperformtasksforwhichoriginalityis valued.

Evidently,onemajortopicrelatedtoethicaluseisplagiarism,whichrefersto usingGenAI-generatedoutputasone’sownworkwithoutacknowledgingthesource
or using GenAI output in replacement of one’s own effort. Plagiarism can be approachedandstudiedfromvariousperspectives,suchasplagiarismdetectionand
preventionofplagiarism.Plagiarismdetectionhasreceivedmuchattentionsincethe launch of ChatGPT. Liang et al. (2023) submitted TOEFL essays written by ESL
speakersandessayswrittenbyeighth-gradeUSstudentstomultipledetectorsand found that while some detectors correctly recognized eighth-graders’ writing as
human-writtenatahighaccuracyrate,thedetectorsmisclassifiedanaverageofover
60% of ESL essays as GenAI-generated. Therefore, they concluded that GenAI detectors are biased against ESL writing. They suspected that the bias is due to the
mechanismofGenAIdetection,whichisbasedonperplexityscores.Perplexityisan index that represents the extent to which language use is predictable, so lower
perplexityorhigherpredictabilitystandsforhigherlikelihoodofGenAIoutputs.This methodofGenAIdetection,whichisbasedonperplexityorpredictability,isthesame
asthemechanismofGenAIperse,whichisalsobasedonpredictability.Liangetal.
(2023) further foundthat ESL essays’ perplexity scores were low,which madethe researcherssuspectthatthehighfalsepositiverateforESLwritingwaslikelydueto
thelowperplexityscores.Thelowperplexityscoreswerelikelyattributabletothe lackoflinguisticsophisticationofESLwriting,whichmadethewriters’languageuse
highlypredictable.Toverifythishypothesis,theyincreasedtheESLessays’lexical

GenAIandL2Writing 129 sophisticationbyusingChatGPTandfoundthattheinaccurateclassificationratewas
significantly reduced. In another study, conducted by Jiang et al. (2024), a GenAI detector was used to classify human- and GenAI-written GRE essays. The human
writersincludedbothnativespeakersandnon-nativespeakersofEnglish.Theresearchersfoundanear-perfectclassificationrateanddidnotfindanybiasagainst
nonnativespeakers.TherearetwoexplanationsforthedisparatefindingsofJianget al.(2024)andLiangetal.(2023).OneisthehigherproficiencyoftheGREessaywriters
in Jiang et al. than the TOEFL essay writers in Liang et al.’s study, and greater closeness to native speakers’ writing may have reduced the false positive rate.
AnotherexplanationisthetrainingthatwasconductedinJiangetal.thatenabledthe
GenAIdetectortolearnthelinguisticfeaturesofthegenreofGREwritingandgivea betterdetectionperformance.Inthisregard,thisstudysuggeststheimportanceof
domain-specifictrainingsothatGenAIcanhavesufficientinputtoextractregularities related to the particular discourse and linguistic features. In general, GenAI
detectionisstillinitsinfancybecauseofitshighfalsepositiverates,andinfact,based onDangandWang’s(2024)studyonU.S.universities’policiesforGenAIuse,61outof
100universitiesofficiallybannedtheuseofGenAIdetectionsoftware.

In addition to GenAI detection, Dang and Wang’s (2024) also examined universitypoliciesonthepreventionofplagiarisminwriting.Theirstudyshowedthat
thestrategiestheuniversitiessuggestedincludedusingpersonalizedassignments suchasincorporatingstudents’personalexperiences,thelocalcontext,etc.;using
process-based writing instruction where students are asked to engage in the learning process instead of focusing on the product (e.g., getting a good grade);
adopting alternative assignment modalities such as podcasts, presentations, etc.
instead of relying on written assignments only; incorporating assignments requiringstudentstoapplyskillsandknowledgetosolveproblems.Inadditionto
the above strategies, one way to prevent plagiarism is to require students to disclosewhethertheyusedGenAIandforwhatpurposes.However,Tanetal.(2025)
found that disclosure of GenAI use in writing led to lower ratings than nondisclosureforthesameessays.

Next,IaddressthelasttwoaspectsofGenAIethics:equityandconfidentiality.
Equity refers to equal access to GenAI by all individuals regardless of their age, gender, ethnicity, location, nationality, profession, religion, and socioeconomic
status. However, universal, equitable access to GenAI is not reality, and many individualsandcommunitiesdonothaveaccesstoGenAIorallfeaturesandcontent
becauseofthelackofinfrastructureorbecauseofeconomicandpoliticalreasons.
Confidentialityreferstothepossiblepublicaccesstopersonalinformationanduser responses;however,accordingtoChatGPT,userresponsesarenotusedastraining
materials,sotheconcernaboutconfidentialityseemstobeassumed.

130 S.Li
# 4 Feedback on Writing
Feedback on writing refers to comments on L2 writers’ writing performance or quality.InL2writingresearch,feedbackhasbeenextensivelyinvestigated,mainly
from the perspective of whether corrective feedback can improve the linguistic accuracy of L2 writing and whether feedback’s effectiveness is affected by other
factorssuchaslearners’individualdifferencesinanxiety,workingmemory,etc.(An andLi2024;KimandLi2024;LiandRoshan2019;VuoganandLi2023).Othertopics
that have been examined include teachers’ feedback-providing practices, teacher andstudentbeliefsaboutcorrectivefeedback,andthecongruenceandincongruence
of teachers’ beliefs and their feedback-providing practices (Li 2017). The large amountofexperimentalandobservationalresearchhasbeensynthesizedinmeta-
analyses(e.g.,KangandHan2015)andnarrativereviews(e.g.,LiandVuono2019).

The advent of GenAI marks the beginning of revived and intensified interest in written feedback because providing feedback on writing is a major affordance of
GenAI.BesidesthereplicationoftraditionalresearchinGenAIcontexts,GenAIopens upnewresearchterritories,topics,andperspectives,suchascomparisonsbetween
GenAIandteacherfeedback-providingpractices,students’engagementwithGenAI feedback, etc. GenAI also makes it possible to examine topics that received little
attention in previous research such as content- and discourse-related feedback, reformulationofstudents’essays,etc.Inthefollowingsections,Iprovideataxonomy
ofwrittenfeedback,synthesizethelimitedresearchthathasbeenconductedtodate, and discuss the importance and methods of feedback evaluation – a unique topic
relatedtoGenAI.

## 4.1 Taxonomy of GenAI Feedback
Ataxonomyoffeedbackisimportantforanumberofreasons.First,usersneedto knowthatfeedbacktakesdifferentformsandthenusetherightprompttogetthe
feedback they favor. Second, teachers need to be aware that different types of feedbackmayhavedifferentialeffectsonstudents’L2learningandwritingandthat
theyshoulduseGenAItoprovidetherightkindoffeedbackinsteadofleavingGenAI todecidewhattypeoffeedbackisprovided.Third,researchersshouldunderstand
the mechanisms and theoretical bases of different types of feedback and conduct research to empirically verify or examine their effectiveness. Current research
simplycomparesteacherandGenAIfeedbackaslumpsumswithoutdistinguishing feedbacktypes,butthefindingsoftheresearcharenotrobustandevenmisleadingif
teachers and GenAI provide different types of feedback during the instructional

GenAIandL2Writing 131 treatment. Somecategoriesoftraditionalfeedback(Ellis2009;LiandVuono2019)
apply to GenAI feedback, but feedback also takes new forms in GenAI contexts.
Therefore,itisnecessarytocategorizefeedbacktypessoastohaveaclearideaof what can be examined in further research. As displayed in Table 1, in general,
feedbackcan bedividedintotwolargecategoriesbasedon thetargetandcharacteristics of feedback. Under the target of feedback, a distinction can be made
betweenglobalandlocalfeedbackaccordingtotheaspectsofwritingthatreceive feedback. Global feedback targets aspects that influence the overall quality of
writing, such as content, organization (flow of ideas, move structure, etc.), and meta-discourse(engagingwithaudience),etc.;localfeedbackconcernslanguage
andmechanics.Dependingonthescopeofthetarget,feedbackiseitherfocusedor unfocused; the former focuses on particular aspect of writing such as the topic
sentenceortheEnglishpassivevoicewhilethelatterhasnofocusortargetsall aspectsofwriting.

Alongthedimensionofpropertiesoffeedback,feedbackcanbefurtherclassified basedontheactiontakenonthetarget,thecontextinwhichfeedbackisprovided,
thelanguageoffeedback,andthefunctionoffeedback.Actiontakenreferstowhatis doneontheerrororthetargetedaspect,whichyieldsthefollowingsubcategories:
– Directcorrection:replacingthetargetwiththecorrectoranotherform
– Metalinguisticfeedback:providingcommentsonthenatureoftheflawedtarget and/orcluesonhowtoimprove;
– Indirectfeedback:highlightingtheerroneouspartwithoutprovidingthecorrect form
– Reformulation: rewriting a sentence or a bigger unit such as the whole text withoutalteringthemeaning
– Modelling:providingamodeltextonthesametopicorbasedonthesameprompt withouttakinganyactiononthestudent’swriting.

Reformulation and modelling are not commonly examined in existing feedback research.Reformulationcanbepartialorcomprehensive,dependingonthelevelof
changes made to the writer’s written output. In the literature, however, reformulationisoftendefinedascorrectingerrorswithoutmarkingthecorrections,which
canbeunderstoodasdirectcorrectionwithouttrackedchanges(e.g.,KimandBowles
2019). Regarding modelling (Nguyen et al. 2024), one may argue that it cannot be regardedasfeedbackasitdoesnotincludecommentsonstudents’writing.However,
thecounterargumentisthatitisaresponsetostudents’imperfectwritingwiththe intentiontoimprovetheirwritingbyencouragingthemtonoticethegapbetween
the correctmodel andtheir own output;therefore, it serves thesame functionas feedback. It is important to clarify that the aforementioned feedback categories
apply primarily to linguistic errors, and to date, feedback on the content and

132 S.Li
Table: Taxonomyofwrittenfeedback.
| Targetof | Aspectof | Global | Content,organization,meta-discourse,clarity, |
| feedback | writing | | readability |
| | | Local | Grammar,vocabulary,mechanics |
| | Scope | Focused | Targetingaparticularlinguisticstructuresuchas |
| | | | thepasttense,oraparticularaspectofwriting, |
| | | | suchasthetopicsentence |
| | | Unfocused | Targetingallaspects |
| Propertiesof | Actiontaken | Directcorrection | Replacinganerrorwiththecorrectform |
| feedback | | Metalinguistic | Commentingonthenatureofanerrororaspect |
| | | feedback | ofwriting |
| | | Indirectfeedback | Highlightingerrors |
| | | Reformulation | Changingtheerroneous(andother)partsofa |
| | | | sentenceorabiggerunitwithoutchangingthe |
| | | | meaningandmarkingthechanges |
| | | Modelling | Providingamodeltext |
| | Context | Integrated | Feedbackisembeddedinthetext |
| | | Detached | Feedbackisseparatefromthetext,suchasalist |
| | | | ofcorrectionsorreformulatedsentences |
| | | Interspersed | Feedbackisprovidedinblocksalternatingwith |
| | | | text |
| | Language | L | Feedbackisprovidedinthewriter’snative |
| | | | language |
| | | L | Feedbackisprovidedinthewriter’ssecond |
| | | | language |
| | Function | Corrective | Correctingerrorsormakingimprovements |
| | | Confirmative | Positivecomments;confirmingstrengths |
| | Source | Teacher | Feedbackisprovidedbytheteacher |
| | | GenAI | FeedbackisprovidedbyGenAI |
| | | Peer | Feedbackisprovidedbypeers |
| | Configurations | | Teacher-adaptedGenAIfeedback;teacherfeedback+GenAIfeed- |
| | | | back;GenAIfeedback+peerfeedback,teacherfeedback+peer |
| | | | feedback+GenAIfeedback,etc. |

organizationalaspectsofwritinghasreceivedlittleattention.Inexistingfeedback research,suchfeedbackissimplylabelledasafocusortarget(e.g.,“content-related
feedback”), and further classification in terms of specific focus and actions taken awaitsfurtherresearch.

Thecontextinwhichfeedbackisprovideddifferentiatesintegrated,detached, andinterpersedfeedback.Integratedfeedbackisembeddedwithinthetext,inter-
persed feedback in provided in blocks alternating with the text, and detached

GenAIandL2Writing 133 feedbackisseparatefromthemaintextsuchasintheformofalistofcorrectionsor
suggestions. The language of feedback can be the user’s first or second language, which bears on the accessibility of feedback to second language users. The final
dimension, function of feedback, concerns whether feedback aims to improve or confirmL2writers’output.Thesourceoffeedbackreferstotheprovideroffeedback,
andthereareessentiallythreesourcesoffeedback:teacher,GenAI,andpeers.The threesourcescangeneratedifferentfeedbackconfigurationsorpackages,suchas
teacher-adapted feedback where the teacher makes changes to GenAI feedback; teacher+GenAIfeedbackwheretheteacherandGenAIfocusondifferentaspectsof
students’writing;GenAI+peerfeedbackwhereGenAIandpeersgivefeedbackon other students’ writing or engage in other activities such as working together to
evaluatethequalityofGenAIfeedback.

## 4.2 Feedback Evaluation
Feedback evaluation refers to efforts to evaluate the quality and acceptability of
GenAIfeedbackforresearchorpedagogical purposes.The evaluationoffeedback quality is a necessary step and a unique topic related to the use of GenAI. It is
necessarybecauseGenAIfeedbackisofteninaccurateandinconsistent.Forexample,
Koltovskaiaetal.(2024)foundthathalfofthefeedbackprovidedongraduatestudents’ academic writing was inaccurate. Lin and Crosthwaite (2024) showed that
ChatGPTgavedifferentkindsoffeedbackondifferentessayseventhoughtheprompt orinstructionsforfeedbackelicitationwerethesame.Theconsequenceofinaccu-
ratefeedbackisobvious:itismisleadingandmayhaveanunfavorableimpacton writingquality.Therefore,researchers,teachers,andlearners/usersshouldtakea
critical stance on GenAI feedback, appraising its quality instead of accepting it without scrutiny. In addition to ensuring feedback quality, another function of
feedbackevaluationispedagogical:byevaluatingGenAIfeedback,studentsreflect ontheirownwrittenoutputandcompareitwithGenAIoutput,whichmayfacilitate
L2development,learnerautonomy,andcriticalthinkingskills.

Theevaluationoffeedbackqualityshouldbebasedoncriteria,andwhatconstitutes valid criteria is a theoretical and empirical question that needs to be
examined in research. Lin and Crosthwaite (2024) classified feedback into three categories:accurate,inaccurate,andredundant,withredundantfeedbackreferring
tofeedbackthatisunnecessary,althoughitisnotwrong.Steissetal.(2024)evaluated
ChatGPT andhumanfeedback based onwhether(1) it isbased oncriteria, (2) the instructionsareclear,(3)itisaccurate,(4)essentialfeaturesareprioritized,and(5)a
supportivetoneisused. Thefivecriteriaarefurtherdiscussedbelow.

134 S.Li
Tobeginwith,criteria-basedfeedbackreferstofeedbackprovidedwithreference to certain benchmarks, expectations, or standards. Criteria areof two types:
curriculum-basedandassessment-based,withtheformerreferringtotheexpected learning outcomes of a course or training program, and the latter to assessment
criteria for large-scale tests such as TOEFL, IELTS, or the Band-4 English test for
ChineseuniversityESLlearners.Criteria-basedfeedbackisimportantbecauseGenAI feedbackhasbeenfoundtobeinconsistentandunsystematic(LinandCrosthwaite
2024), partly because there is a lack of criteria. Thus, GenAI’s feedback-providing behaviors need to be regulated by criteria, which serve as user’s instructions to
GenAI on what type of feedback it is expected to provide and what expectations shouldbemet.Theneedforcriteriaisalsobecausewhatconstituteseffectivewriting
dependsonthenatureofthewriting,genre,purpose,audience,task,etc.Thereare nouniversalcriteriaforhigh-