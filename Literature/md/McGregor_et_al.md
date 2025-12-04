---
source_pdf: McGregor et al..pdf
converted_date: 2025-12-04T19:58:10.365653
total_pages: 10
model: Google Gemini 2.0 Flash
total_cost_usd: $0.004282
prompt_tokens: 10,051
completion_tokens: 8,192
---

# Process Based Evaluation of Computer Generated Poetry
StephenMcGregor and MatthewPurver and GeraintWiggins
QueenMaryUniversityofLondon
SchoolofElectronicEngineeringandComputerScience s.e.mcgregor@qmul.ac.uk m.purver@qmul.ac.uk
geraint.wiggins@qmul.ac.uk

Abstract generative procedure employed by the system, includingitsengagementwithacorpusofrelevantex-
Thispaperpresentsandevaluatesanovelsystantculturalartefacts,issubjecttosuspicionsofpas-
tem for computer generated poetry. Framed ticheorevenplagiarism. Theburdenofcreativejus-
within contemporary theoretical trends in the tification is on the system itself: it is reasonable to
evaluationofcomputationalcreativity, weinvestigate how evidence of generative process expect a creative computational agent to justify its
influencesreaders’opinionsofcomputergen- outputintermsofthewayinwhichitwasgenerated, erated textual output. In addition to a techni- andinparticulartodemonstratethewayinwhichits
cal description of our system, we present re- procedurescanbeostensiblyconstruedasinstances sultsfromastudyaskingrespondentstoeval-
of autonomous engagement with an existing inspiruateshortcomputergeneratedpoemsprefaced
ingset (Ritchie, 2012). Thejudgmentofdiscerning with different types of descriptions, in some
observersofcomputationaloutputwillultimatelybe cases objectively presenting the poem as the
influenced by the effectiveness of this presentation productofastatisticalanalysisofcorporaand
insomecasessubjectivelypresentingthecom- ofprocess.
puterasaself-awareagent.
Inthisstudy,wesystematicallytestthedifference between how human readers react to poems gener-
ated by computers when the computational process
1 Introduction is,ontheonehand,framedasaprocedureofstatisti-
The trope of the poet as inscrutable genius figures calanalysis,and,ontheotherhand,asacreativeenlarge in our collective cultural appreciation of po- deavour undertaken by an autonomous and ostensi-
etry. Coleridge emerging from a drunken stupor blyself-awareagent. Inbothcases,weareexploring with the lines to “Kubla Kahn” fully formed in his thewaysinwhichhumansreacttocreativeartefacts
mind, Blake hallucinating trees full of angels, the whichhavebeenopenlygeneratedbycomputers;in drunken,stonedverseofRimbaudandVerlaine,the this work, we are not concerned with exploring the
psychicdivinationsofBretonandSoupault: regard- ability of human observers to distinguish between lessofthelegitimacyoftheselegends,weasreaders workcreatedbyotherhumansversusoutputcovertly
are seduced by the idea of the poet as a transmitter generatedbycomputationalprocesses. Theappreciof the ineffable, tapped into an mental space inac- ation of creative work is always a moving target, in
cessibleandunknowabletomostofus. thatpopularopinionsofwhatqualifiesasinnovation
Ofcoursewhenitcomestocomputers,wearenot is perpetually evolving, and our stance is that pubwilling to give them this kind of credit, nor should lic consideration of art is moving towards a point
webe. Whenweencounteramachinethatproduces wheretheideaofcreativemachinesisbecominginexemplary poetry, we suspect there might be an el- creasinglypalatable. Inthisregardinparticular, we
ement of human interference lurking in the mecha- feelthatpoetrygeneratedbyprocessestransparently nism. Such output, without any explanation of the
ProceedingsoftheINLG2016WorkshoponComputationalCreativityandNaturalLanguageGeneration,pages51–60,
Edinburgh,September2016.(cid:13)c2016AssociationforComputationalLinguistics
51

grounded in the machine learning paradigm will be to the perception of aesthetic value in the case of judgedfavourably. computergeneratedart. Morerecently, (Coltonand
Inthispaper,we’llbeginwithaoverviewofcom- Wiggins, 2012) have advocated “assessing the beputational creativity, focusing in particular on ideas haviourofsoftwareviaprocessratherthanproduct”
abouttheevaluationofnotonlycreativeartefactsbut (p. 24), by way of creative systems “framing their also creative processes. The nature of our study is creative acts with information that adds value” (p.
motivated by an examination of some specific ex- 25,emphasisinoriginal).
amplesofcomputationalpoetrygeneratingsystems.
In Section 3, we’ll outline the technical details of
The work presented here has been undertaken a novel system for generating short, simple poems,
verymuchinthisspiritofofferingthecomputational grounded in statistical analyses of large sets of tex-
process behind the generation of our system’s outtual data. In Section 4, we’ll present a study col-
put as an element of the artefact itself. In fact, in lectingevaluationsofoursystemsoutputinfluenced
line with (Jordanous, 2015), we feel that much of by different ways of presenting the computational
what counts as creativity exists not merely within process behind the generation of the output. In our
the creative agent, but also in the dynamic between final analysis, we will discover that the procedural
agent, audience, and environment. In the specific presentation does not, in fact, influence the ratings
case of the new system for poetry generation which returned by readers, at least to a statistically sig-
will be described throughout Section 3, the compunificant degree, and at least for the type of highly
tational agent engages with the world through a set autonomous output produced by the system which
ofstatisticalanalyseswithlargescale,highlypublic we’lldescribehere.
corpora, spanning the canonical and the encyclopedic. Ourhopeisthat,onmultiplelevels,thiskindof
2 Computers,Creativity,andPoetry engagementwithdata-in-the-worldor,alternatively,
world-as-dataoffersaperspectiveonanagentwhich
This paper is in particular concerned with the evalis situated in an accessible and even familiar envi-
uation of computer generated poetry. With this in ronment.
mind, however, an overview of recent and ongoing general trends in the field of computational creativ-
ityseemsanappropriatestartingpoint. Inparticular
Notably, this idea of statistical analysis as enviherewe’reconcernedwithpresentingsomethoughts
ronmental grounding has likewise been adopted by on the question of the evaluation of creative work
the field of cognitive science, where, for instance, undertakenbycomputationalagents,andinparticu-
(Barsalou,2008)hasproposedtheintegrationofstalartheissueoftheassessmentofcomputationalpro-
tisticalinformationaboutwordsandlinguisticstruccessasacriticalelementinthiskindofevaluation.
tures as part of a model of cognition as grounded in dynamic environmental processes. The upshot
2.1 EvaluatingComputationalCreativity of this kind of theory is that there is some hope of
While the concept of the Turing Test – the be- understandingtheseambetweenwordsandideasin haviouralist assessment of a symbol manipulating terms of the data that is available in large scale cor-
system sheerly on the basis of its output – has cap- pora,thatculturalleveloflinguisticphenomenabetured the popular imagination, the field of Compu- tweentheevolutionaryandthedevelopmentalwhich
tational Creativity has probably since its inception hasbeendescribedby(Smithetal.,2003)asglossobeenconcernednotonlywiththeevaluationofarte- genetic. For this reason, we think that the machine
facts produced by machines but also with the per- learning paradigm in particular, which takes as its ception of the machine itself as a producer. (Bo- basis corpora on the comprehensive scale of large
den,1990),forinstance,isgenerallyconcernedwith cultural repositories such as an exhaustive encyclotheimportanceofself-evaluationinthecreativepro- pedia or a literary canon, is an appropriate setting
cess, and in particular considers the way in which for exploring computer generated poetry as a crethe “computer’s performance” (p. 159) contributes ativeprocess.
52

2.2 ComputerGeneratedPoetry also with observation of the process which the system undertakes to produce its output. With regard
Theprevalenttrendincomputergeneratedpoetryto topoetryinparticular,themodelarchitectsarecon-
date has involved a combination of rule-based macernedwiththecriticalconveyanceof“communica-
nipulationsofsymbolsandcleverheuristicdatamintive purpose” (p. 96) which is essential to the un-
ing designed to populate templates affording varyderstanding of linguistic expression: as consumers
ingdegreesoffreedom. TheWASPsystem(Gerva´s, ofpoetry,werelyonthebeliefthatsomethingmore
2000), for instance, uses a battery of “judges” to thanjustarandomorcleverlyconstrainedbutdecon-
evaluate an unfolding “draft” of a poem along a setextualisedprocessliesattheotherendofthepoem
ries of criteria such as rhyme, scansion, line length, itself. Inshort,wecountonmeaningbeinganchored
and so forth. The resulting poem is a product of inintent.
theinteractionofthesevariousweightedconstraints,
In the case of the poetic implementation of the coupled with n-gram driven text generation based
FACEmodel,thishasmeantthatpoemsarecoupled on an analysis of a corpus of canonical Spanish po-
with expository statements regarding data analysis etry. Similarly,PoeTryMe(Oliveira,2012)employs
thathasservedasasituationspecificmotivationfor a network of information processing nodes that in-
the generation of each poem. The system itself opteracttogenerategrammatical,metricalverse.
eratesbywayoftemplatecompletion,insertinginto
Moving into a more statistical mode of produc- prefiguredlinesofversesimilesminedfromtheweb tion, (Toivanen et al., 2012) describe a poetry gen- using a pattern fitting heuristic to determine viable
erating system which discovers semantic relation- word combinations. In order to convey a sense of ships based on word co-occurrence statistics in a intent to its output, the system weights the phrases
largescalecorpus. Inadditiontothisstatisticaltech- it extracts from the web based on a sentiment analniqueformodelling semantics, thissystemimposes ysis,seekingtochoosesimileswhichcorrespondin
additionalsyntacticandphonologicalconstraintson sentimentwithasimilarlyanalysedselectionoftext its output, and in this regard is comparable with from a current newspaper. The idea here is that, by
the system described in this paper. Also within the rooting the poem in the mood of a currently or regeneral family of statistical, corpus based models, centlyunfoldingevent,thesystem’soutputbecomes
Haiku generation in particular has been a target for tied to something happening in the world, and the vectorspacemodelapproachestocomputationalpo- readerbecomesmorecommittedtotheideathatthe
etry. Gaiku (Netzer et al., 2009), for instance, uses computerisanagentcreatinganartefactinreaction acombinationofhumangeneratedwordassociation to a situation. In particular, the system frames its
normsandsequencesofsyntaxderivedfromastatis- explanationasafirst-personexpositioninvolvingan ticalanalysisofacorpusofexistinghaikutogener- analysisofthemoodofthenewsonagivenday,with
atenewhaikuwhicharedesignedtobeasmeaning- adegreeofjustificationforthisanalysis: thesystem ful, grammatical, and poetic as possible. The First presents itself as a willful actor knowingly engaged
Sally system for Haiku generation (Droog-Hayes inacreative,interpretiveprocess.
and Wiggins, 2015) uses a distributional semantic Our hypothesis is that the system based on the model,basedonananalysisofwordco-occurrences FACE model, when it comes to the evaluation of
in a large scale textual corpus, to generate sets of computer generated poetry, has got it at least half conceptually related words, and in this regard is right, in that the perception of a creative procedure
closely related to the semantic element of the new underlyingthecomputationalgenerationofpoetryis systemdescribedinSection3.1. a crucial factor in the creative quality of the poetic
Of particular interest to the study presented here artefact. And one way to convey a creative proceis the system for poetry generation based on the dure is to couch the operation of the computer in
FACE model for assessing computational creativity a narrative of the machine having a self-reflective
(Colton et al., 2012). This model focuses on the senseofgoal-directedness,akindoftransparentficevaluation of creativity associated not just with as- tion of agency exploiting the human tendency to
sessmentoftheartefactgeneratedbythesystem,but readintentionsandbeliefsintoallsortsofsituations
53

intheworldwhereweknowthereactuallyarenone Theobjectiveofthiscomponentofthepoetrygener-
(Carruthers,2011). Webelieve,though,thatreaders atingsystemistogeneratespacesinwhichtheconofpoetryareatthisstageinthehistoryoftechnology ceptualrelationshipsbetweenwords
andartpreparedtoengagewithcomputerproduced The motivation for using this particular model is verse in a more frank way, acknowledging the sta- twofold. For one thing, the model derives its fea-
tistical character of the underlying operation with- turesfromanunsupervisedtraversalofacorpus, so out losing regard for the inherent degree of creativ- thesemanticrelationshipswhichitcapturesaredis-
ity,andinfactpossiblytakingtheoutputmoreseri- covered without the human dictated assignment of ouslywhenthegenerativeprocedureispresentedin symbolmanipulatingrules. Thispropertyostensibly
astraightforward,objectivemanner. gives the poetry generating system at least a semblance of agency. And, on the other hand, the dy-
3 AutonomousandContextualPoetry namic, contextual component of the model enables
In order to evaluate human assessment of both cre- it to engage with ad hoc input, allowing the model ative process and output, we have designed a rela- to generate output topically related to other textual
tively straightforward system for generating short, artefacts. This means there is some hope of conloosely constrained poems. This system has been veying a sense of intentionality or aboutness to an
designedwiththreecriticalprinciplesinmind: observerofthesystem’sprocess.
This semantic model is based on a very high-
The system uses a machine learning technique dimensional (approximately 7.5 million), very
• fortheunsupervisedgenerationofsemanticre- sparse space of word-vectors generated from a
lationships. traversal of the English language component of
Wikipedia. Thedimensionsofthisspacecorrespond
The semantic relationships which serve as one
• totermsthatco-occurinsentenceswithwordsfrom of the constraints on the systems output are
the model’s 200,000 word vocabulary. The value context sensitive, and in this way can be asso-
for each dimension is based on a pointwise mutual ciatedwithadhocinputallowingthepoemsto
information metric derived as follows, where n w,c
beaboutsomethingtopical.
correspondstothefrequencywithwhichvocabulary
The system uses a statistical technique to con- word w co-occurs with context word c, W is the
• strainthephonologyofthepoem,andsoisde- overallcountofvocabularywordtokens,n w andn c
signedtoproducetextthatsoundspoetic. aretherespectiveindependentfrequenciesofw and c,andaisasmoothingconstant:
Over the course of this section, we’ll lay out a series of models which are algoritmically concate- n W
w,c
M = log × +1 (1) nated into a system which seeks to fulfill these re- w,c 2 n (n +a)
(cid:18) w × c (cid:19) quirement.
The sparse space generated through this process
3.1 ASemanticModel canbereducedtoacontextdependent,conceptually
Atitsrootthissystemisbasedonastatisticalmodel orientedsubspacethroughananalsyisofasetofinof word meaning constructed within the distribu- put terms. So, for instance, in a 200 dimensional
tional semantic paradigm, construing words as vec- subspacebasedonco-occurrencedimensionssalient tors within a space of dimensions representing co- to the words cat, dog, and goldfish, cat is
occurrences with other words over the course of a closest to the words like rabbit, hamster, and large-scale textual corpus (Turney and Patel, 2010; pet. If, on the other hand, we build a subspace
Clark, 2015). The key feature of this particular based on the input words cat, lion, and tiger, model is its context sensitivity: it dynamically gen- cat becomes proximate to words like leopard,
erates new semantic spaces based on an analysis of hyena,andwild. Technicaldetailsforgenerating the conceptual relationships between a set of input subspaces are laid out in detail in (McGregor et al.,
terms (McGregor et al., 2015; Agres et al., 2015). 2015).
54

3.2 APhonologicalModel emerge in the system’s output, these elements are discovered by the system itself as statistical proper-
This process of building a space of potential subtiesinherenttotheunderlyingcorpusofsonnets.
spaces is coupled with a phonological model which similarlyusesaninformationtheoreticmetrictotry
3.3 ASyntacticModel to capture the way in which word-sounds are ex-
Thethirdconstraintplacedonourpoetrygenerating pected to co-occur in poetry. This model is also
systemconsistsofann-grammodelforstringingtoconstructed from a statistical model of a corpus, in
gether parts of speech in ostensibly syntactic ways.
this instance a corpus containing about 1500 Englishlanguagesonnets.1 Thesesonnetsarerendered Statistics are once again harvested from the corpus
ofabout1,500Englishlanguagesonnets,inthiscase intoaformatcontainingbothphonemicandsyllabic
with each word tagged with a part of speech label information, based on a syllabified version of the
usingthePythonNaturalLanguageToolkitwordto-
CMU Arpabet (Bartlett et al., 2009). Frequencies keniser.2 Once these tagged renditions of the cor-
ofphonemicco-occurrenceC (p ,p )arethentabui a b
pusaregenerated,aprobabilisticmodelforpredictlated,wherethecountC isthetotalnumberoftimes
ing the syntactic continuation of a string of parts of phoneme p occurs i syllables in front of phoneme
b speech is built, describe here with n representing
p in a line of a poem. Once all frequencies for all t,q b
the frequency with which part of speech t follows lines in all poems in the corpus are compiled, these
thesequenceofpartsofspeechq inalineofpoetry, statisticsareconvertedintomutualinformationmea-
and n signifying the total number of times the seq
sures, formulated here with C (T) representing the quenceq isobservedinanyline:
i totalnumberofphonemesoccurringisyllablesapart
and C i(p a) and C i(p b) standing for the indepen- n dentfrequenciesat− whichphonemesp andp occur G(t q) = t,q (4)
a b | n q
i or i syllables away respectively from any other
− If,inthecourseofgeneratingalineverse,thesyssyllable:
temgeneratesasequenceq thathasnoobservedextension, is will remove the first element in q to pro-
P (p ,p ) = log
C i(p a,p b)C i(T)
+1 (2) duce sequence q
0 and will then generate element t
i a b 2
(cid:18)
C i(p a)C i(p b)
(cid:19) withprobabilityG(t q 0). Thepurposeofthisopera-
− | tion is to impose an arguably superficial element of
From this matrix of phoneme-distance relationgrammaticalityonthesystem’soutput. Anecdotally,
ships,ascorecanbegeneratedforthephonological but also significantly, professional poets who have
strengthofanytwogivencandidatesyllabless and
1 interacted with the system have actually suggested s potentially occurring in a line of poetry gener-
2 that this component of the process over-constrains atedbythesystem,wherel andl aretherespective
1 2 theoutputtothedetrimentoftheinterestingconceplengths of s and s , and p and p are correspond-
1 2 1 2 tualandphonologicalrelationshipsgeneratedbythe ingconstituentphonemes:
other models.3 Nonetheless, for the purpose of the comparative study presented here, this component
1 l1 l2 ofthesystemismaintained. Alsoofnoteisthatthis
S i(s 1,s 2) = P i(p 1,p 2) (3) syntacticmodelistheonlycomponentofthesystem l l ×
1 2 p X1=1p X2=1 thatsimulatesanon-deterministicprocess.
This phonological model is incorporated into our
3.4 SentimentAnalysis poetrygeneratingsysteminordertoimposeasense
The final aspect of the poetry generating system is of prosody on the output. As with the semantic
a model for analysing the sentiment of a document model, there are no phonetic or metric constraints
hand-coded by human designers, and so we can 2www.nltk.org/ modules/nltk/tokenize.html claim that, to the degree that prosodic features do 3InthecourseoftheGlobeRoadPoetryFestivalatQueen
MaryinNovember2015andthePortraitoftheMachineasa
1www.sonnets.org. YoungArtisteventattheBritishLibraryinFebruary2016.
55

withinacorpus. Inthecaseofthepoemsusedforthe 2. The four topics of each conversation are fed study here, the corpus in question is the Penn Tree- intothesemanticmodeldescribeinSection3.1.
bank Switchboard corpus, consisting of 1,126 tran- A subspace of conceptually related words is scribedtelephoneconversations.4 Astraightforward generated, with the salient region of this space
term frequency-inverse document frequency tech- consideredthatwhichisclosesttothemeanof nique is employed in order to create a topic model the topical input terms. The words in this sub-
for each conversation within the corpus (Salton and space are tagged with their most likely part of
McGill, 1983). Specifically, for a given document speech.
(conversation) d, the words representing the salient topics of the conversation are ranked according to 3. Asyntacticstringisprobabilisticallygenerated
this equation, where w is a word that occurs within based on Equation 4, and a line of poetry of thedocument, w isthenumberoftimesw appears no more than 11 syllables is correspondingly
d in d, and w is the number of times w occurs in the composed.
c entirecorpusofconversations:
4. At each step in the generative process, the
w
T(d,w) = d (5) word that is closest to the salient region of the w
c space described in Step 2, aside from the in-
For each conversation in the corpus, the top four puttermsthemselves,thatmatchesthenextpart topical terms based on the above equation are se- of speech prescribed by Step 3 is choosen as
lected, and the sentiment of these terms is rated a continuation of the line being composed. A along a negative-positive spectrum. The rating for basepoemoffourlinesisgenerated.
a given word is derived from the SentiWordNet database of word sentiment scores, which assigns 5. Each word in each line is given a score of
negative and positive ratings to senses of a large phonological appropriateness based on the avnumberofwords.5 Inordertorankthesentimentof erage score of each of its syllables compared
each conversation, each word is assigned the mean withallothersyllablesintheline,includingthe score of its various sentences, and then the average other syllables in the word itself. This phono-
scoresofthefourmostsalienttermsistakentogive logical score is then multiplied by 1 (z
− × eachconversationanoverallranking. sent(w)), where sent(w) is the sentimental
Thepurposeofanalysingthesentimentofatran- rating of word w according to the SentiWordscribedconversationistogivethepoetrygenerating Net database, while the value of z is -1 if the
systematopicasatopicalhandle,allowingthepoem overallsentimentoftheinputtermsisnegative to be about something specific and intersubjective. and+1iftheprevalentsentimentispositive.
The idea, following on from (Colton et al., 2012), isthatapoemthatisendowedwithintentionalityis 6. The least appropriate word in the poem is re-
morelikelytobedeemedascreativebyanobserver. moved and replaced with the most appropriate word, selected from a vocabulary defined
3.5 AssemblingaPoem intermsofthe1,000mostconceptuallysalient
Finally, the various modular components described wordsasestablishedinthesubspacederivedin above are linked together to algorithmically gener- Step 2. Steps 5 and 6 are repeated until the
atepoemsforsubsequentanalysisbyhumanreaders poemconvergestoamaximallyscoredstate.
accordingtothefollowingprocedure:
Thefinalproductofthisprocessisintendedtobe
1. The17mostnegativeand16mostpositivecon-
apoemwhichisconceptuallyrelevanttotheconverversations, ranked as described in Section 3.4,
sation serving as the basis for the input terms while areselectedastopicsforpoems.
exhibiting poetic phonology, sentiment appropriate
4www.cis.upenn.edu/˜treebank/ to the input topic, and a modicum of grammatical-
5http://sentiwordnet.isti.cnr.it/ ity.
56

4 EvaluationofProcessandProduct creativity meaningful quality obj 3.14(1.88) 1.67(0.78) 2.05(1.05)
Based on the generative process described throughsubj 2.93(1.63) 2.00(1.32) 2.07(0.96)
out Section 3, 33 poems have been randomly gennone 2.93(1.60) 1.54(0.63) 2.14(1.33)
erated, each associated with a conversation sum-
Table1: Meanscoresalongaseven-pointscale(withstandard marisedbythefourwordsderivedthroughthetech-
deviationsinparentheses)forhumansubjectevaluationsofcrenique described in Section 3.4. We have subse-
ativity,meaningfulness,andqualityofcomputergeneratedpoquently generated three different versions of these
ems prefaced with an objective description of the generative poems, one prefaced with a brief objective descrip-
process,asubjectivedescription,ornodescriptionatall.
tion of the generative process, one prefaced with a brief subjective description framing the system as a
self-awareagent,andonewithnoprefaceatall. An poemitselfwaspresented,precededbyeitheroneof exampleoftheobjectiveprefaceisasfollows: the two types of procedural descriptions illustrated
aboveorbynodescriptionatall. Onthesamepage,
Thispoemisbasedonasentimentalandconceptual subjects were asked to evaluate the poem they had
analysis of a conversation containing words like justreadbasedonthreedifferentcriteria: creativity,
‘sickening’,‘shitty’,‘novice’,and‘hack’. Thesenmeaningfulness,andquality,ineachcasegivingthe
timentalcomponentoftheanalysisdeterminedthe poemaratingalongasevenpointscalerangingfrom
conversationwasnegative.Thepoememergedasa
“low”to“high”. Finallythesubjectswerepresented pathwayinaspaceofwordpointsderivedfromthis
with a third page where they were asked to prostatisticalanalysis,withanadditionalcriterionfor
vide optional information about their age and their selectingpoeticsoundingcombinationsofwords.
self-assessed proficiency or knowledge in the En-
And the subjective description of the same poem glish language, poetry, and computer science, again
readsasfollows:
in each case rating themselves along a seven-point scale, in these instances ranging from “novice” to
I listened to a conversation containing words like “expert”.
‘sickening’, ‘shitty’, ‘novice’, and ‘hack’. I con- Wereceivedresponsesfrom79participants,with sidered this to be a negative conversation. I de- each participant evaluating a unique preface-poem
cidedtowriteapoemaboutthisconversation,and combination. Reported ages ranged from 20 to 72, havetriedtocapturesomeofthenegativesentiment with a mean of 40. The mean value for proficiency
whilealsofocusingonhowthepoemsounds. inEnglishwas6.26,withstandarddeviationof0.92; for knowledge of poetry, the mean was 4.12 with
Finally,thepoemthataccompaniesthesedescripstdv of 1.46; for knowledge of computer science,
tionsreadslikethis:
the mean was 4.66, with stdv of 1.96. The mean responses, along with standard deviations, are pre-
andwonderedbuttalkedmeshiftySinatra sentedinTable4.
likehangsaysincurrentorthatfourman
The overall picture these results paint is that, in becausethisfullgetsreallytheremakesboth
thecaseofthetypeofpoetrybeinggeneratedbyour anothergoldenwaythoughyourman
system, themodeofpresentationhasamarginaleffect on the evaluation of content. The higher value
Weconstructedasurveyconsistingofatotalof99 of creativity typically accorded to poems presented poems: eachofthe33poemsoursystemgenerated, withanobjectivedescriptioncorrelateswithourhy-
with each of the three versions of the explanatory pothesis that readers would react favourably to this preface (or lack thereof). Each survey participant transparent presentation of process, by the differ-
was first presented with a introduction page laying ence between this value and the mean creativity asout the survey, informing them that they would be signed to poems subjectively framed is not statis-
reading a poem generated by a computer and then tically significant: a two-tailed Student’s t-test on asked to evaluate the poem. On the next page, the the results gives a p-value of 0.68 and a t-value of
57

0.42. The relatively similar mean scores, combined inthefirstplace. Anecdotally,responsesinmostcatwithhighdegreesofstandarddeviation,indicatethat egories for most types of presentation ranged from
these results, at least in terms of a comparison be- one to seven, despite all of the 33 poems being of a tween the data for each type of presentation, aren’t generally similar quality. There seems to be a lack
distinguishable from what we would expect if sub- of consensus regarding how to consider computers jectsrandomlyassignedvaluestopoems. aspoets.
Also of not is the relatively high scores given to This analysis aligns with the feedback received the subjectively presented poems in terms of the in the course of the the events involving engage-
meaningfulness of the poems. Statistical signifi- ment between human poets and computational syscance is slightly higher here, with a p-value of 0.31 temsforpoetrygenerationmentionedinSection3.3.
and a t-value of 1.02, but still hardly noteworthy. Specifically, a self-selecting group of technologi-
The one thing that does perhaps bear further con- cally receptive poets found much value in engagsideration here is the way that subjects seem rela- ing with the system described here, which they saw
tivelycomfortableascribingcreativitytopoemspre- as a mechanism for discovering interesting, novel, sentedasproductsofstatisticalprocessesversusthe andpotentiallyproductiveconceptualconcordances
meaningfulness attributed to poems framed as sub- within a corpus which were obscure to a human jective experiences of information in and about the readerbutnonethelesspoetically valuable. Thisap-
world. Perhapstheappropriateinterpretationhereis proachtopoetryasanartefactofadynamicengagethatreadersappreciatetheinsightintotheproductive ment between poets, readers, corpora, society, and
mechanism afforded by the objective presentation, the environment is conducive to the type of poetry andassociatethiswithcreativity,whereasmeaning- generated by our system—but this particular aes-
fulness is more closely connected to the impression thetic stance is hardly universal in the world of poofagencyandindividuationconveyedbythesubjec- etryreaders.
tivepresentation. ComparedtotheoutputoftheFullFACEsystem,
Finally, it is also worth mentioning that the po- theoutputofoursystemis,moreorlessobjectively, ems presented with no procedural description at all moregarbledandlessstructured. Ontheotherhand,
do just about as well as the lesser of the two ex- the FACE system resorts to heuristic simile mining plained poems in terms of creativity and meaning- and template filling, where our system maintains a
fulness,andactuallydoslightlybetterthantheother somewhat higher degree of autonomy in its analytwo types in terms of quality. Quality is arguably a sis of a corpus and dynamic projection of concep-
somewhatvaguecategory,andwasintendedtocover tually loaded semantic subspaces. Whether readarangeofpropertiessuchaspoeticnessandcompo- ers provided with more comprehensive descriptions
sition. Onthewhole,though,thestoryhereseemsto of the differences between these approaches would be that, at least in terms of this type of poetry, with consideronesystemmorecreativethantheotherre-
therelativelycursorykindofproceduraldescription mainstobeseen,andisbesidethepointofthestudy we were able to offer in the course of a survey that presentedhere, whichhasbeenafirstattemptatas-
was, by design, quite brief, the way that the poems sessingwhetherornotthewaythatthecreativeproarepresenteddoesn’tmakeabigdifferenceinterms cessinvolvedinthecomputationalproductionofpo-
ofhowhumansratethistypeofoutput. etryisframedhasasignificantimpactonevaluation ofoutput.
Returningtoourearlierdiscussionofcreativityas
5 Conclusion a phenomenon dynamically distributed across a so-
Further to the brief analysis offered above, another cietyandanenvironment,weultimatelyexpectevalpoint of interest with this study relates to the rel- uationsofcreativitytotakeintoaccountvariousfac-
atively high degree of standard deviation evident tors integrating the overall situation of an artefact.
across all the results. The story here would seem to So,forinstance,inthecaseofpoetry,wewouldprebe that there is a wide range of opinion on how ex- dict that the relationship between a poem, its mode
actlycomputergeneratedpoetryshouldbeevaluated of production, and the milieu in which the poem is
58

produced should all contribute to the assessment of Proceedings of the 6th International Conference on