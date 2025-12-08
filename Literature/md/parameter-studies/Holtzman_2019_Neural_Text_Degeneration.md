---
source_pdf: Holtzman_2019_Neural_Text_Degeneration.pdf
converted_date: 2025-12-04T20:29:21.640783
total_pages: 16
model: Google Gemini 2.0 Flash
total_cost_usd: $0.004726
prompt_tokens: 14,488
completion_tokens: 8,193
---

PublishedasaconferencepaperatICLR2020
THE CURIOUS CASE OF
NEURAL TEXT De GENERATION
AriHoltzman†‡ JanBuys§† LiDu† MaxwellForbes†‡ YejinChoi†‡
†PaulG.AllenSchoolofComputerScience&Engineering,UniversityofWashington
‡AllenInstituteforArtificialIntelligence
§DepartmentofComputerScience,UniversityofCapeTown
{ahai,dul2,mbforbes,yejin}@cs.washington.edu, jbuys@cs.uct.ac.za
ABSTRACT
Despite considerable advances in neural language modeling, it remains an open question what the best decoding strategy is for text generation from a language
model (e.g. to generate a story). The counter-intuitive empirical observation is that even though the use of likelihood as training objective leads to high quality
models for a broad range of language understanding tasks, maximization-based decodingmethodssuchasbeamsearchleadtodegeneration—outputtextthatis
bland,incoherent,orgetsstuckinrepetitiveloops.
ToaddressthisweproposeNucleusSampling,asimplebuteffectivemethodto draw considerably higher quality text out of neural language models than previ-
ousdecodingstrategies. Ourapproachavoidstextdegenerationbytruncatingthe unreliabletailoftheprobabilitydistribution,samplingfromthedynamicnucleus
oftokenscontainingthevastmajorityoftheprobabilitymass.
To properly examine current maximization-based and stochastic decoding methods, we compare generations from each of these methods to the distribution of
humantextalongseveralaxessuchaslikelihood,diversity,andrepetition.Ourresultsshowthat(1)maximizationisaninappropriatedecodingobjectiveforopen-
endedtextgeneration,(2)theprobabilitydistributionsofthebestcurrentlanguage modelshaveanunreliabletailwhichneedstobetruncatedduringgenerationand
(3)NucleusSamplingiscurrentlythebestavailabledecodingstrategyforgeneratinglong-formtextthatisbothhigh-quality—asmeasuredbyhumanevaluation
—andasdiverseashuman-writtentext.
Context:Inashockingfinding,scientistdiscoveredaherdofunicornslivinginaremote,previouslyunexploredvalley, intheAndesMountains.EvenmoresurprisingtotheresearcherswasthefactthattheunicornsspokeperfectEnglish.
BeamSearch,b=32: PureSampling:
"Thestudy,publishedintheProceedingsofthe TheywerecattlecalledBolivianCavalleros;theyliveina
NationalAcademyofSciencesoftheUnitedStatesof remotedesertuninterruptedbytown,andtheyspeakhuge,
America(PNAS),wasconductedbyresearchersfromthe beautiful,paradisiacalBolivianlinguisticthing.Theysay,
UniversidadNacionalAutónomadeMéxico(UNAM)and 'Lunch,marge.'Theydon'ttellwhatthelunchis,"director theUniversidadNacionalAutónomadeMéxico ProfessorChuperasOmwelltoldSkyNews."They'veonly
(UNAM/UniversidadNacionalAutónomade beentalkingtoscientists,likewe'rebeinginterviewedbyTV
México/UniversidadNacionalAutónomade reporters.Wedon'tevenstickaroundtobeinterviewedby
México/UniversidadNacionalAutónomade TVreporters.Maybethat'showtheyfiguredoutthatthey're
México/UniversidadNacionalAutónomade...” cosplayingastheBolivianCavalleros."
Figure 1: Even with substantial human context and the powerful GPT-2 Large language model,
Beam Search (size 32) leads to degenerate repetition (highlighted in blue) while pure sampling leadstoincoherentgibberish(highlightedinred). Whenb ≥ 64,bothGPT-2LargeandXL(774M
and1542Mparameters,respectively)prefertostopgeneratingimmediatelyafterthegivencontext.

1 INTRODUCTION
On February 14th 2019, OpenAI surprised the scientific community with an impressively highquality article about Ovid’s Unicorn, written by GPT-2.1 Notably, the top-quality generations ob-
1https://openai.com/blog/better-language-models/
1
0202 beF
41
]LC.sc[
2v15790.4091:viXra
PublishedasaconferencepaperatICLR2020 tainedfromthemodelrelyonrandomnessinthedecodingmethod,inparticularthroughtop-ksam-
plingthatsamplesthenextwordfromthetopkmostprobablechoices(Fanetal.,2018;Holtzman etal.,2018;Radfordetal.,2019),insteadofaimingtodecodetextthatmaximizeslikelihood.
Infact,decodingstrategiesthatoptimizeforoutputwithhighprobability,suchasbeamsearch,lead totextthatisincrediblydegenerate,evenwhenusingstate-of-the-artmodelssuchasGPT-2Large,
as shown in Figure 1. This may seem counter-intuitive, as one would expect that good models would assign higher probability to more human-like, grammatical text. Indeed, language models
dogenerallyassignhighscorestowell-formedtext,yetthehighestscoresforlongertextsareoften generic, repetitive, and awkward. Figure 2 exposes how different the distribution of probabilities
assignedtobeamsearchdecodedtextandnaturallyoccurringtextreallyare.
PerhapsequallysurprisingistherightsideofFigure1,whichshowsthatpuresampling—sampling directlyfromtheprobabilitiespredictedbythemodel—resultsintextthatisincoherentandalmost
unrelated to the context. Why is text produced by pure sampling so degenerate? In this work we showthatthe“unreliabletail”istoblame. Thisunreliabletailiscomposedoftensofthousandsof
candidatetokenswithrelativelylowprobabilitythatareover-representedintheaggregate.
To overcome these issues we introduce Nucleus Sampling (§3.1). The key intuition of Nucleus
Samplingisthatthevastmajorityofprobabilitymassateachtimestepisconcentratedinthenucleus, asmallsubsetofthevocabularythattendstorangebetweenoneandathousandcandidates. Instead
ofrelyingonafixedtop-k,orusingatemperatureparametertocontroltheshapeofthedistribution withoutsufficientlysuppressingtheunreliabletail,weproposesamplingfromthetop-pportionof
theprobabilitymass,expandingandcontractingthecandidatepooldynamically.
In order to compare current methods to Nucleus Sampling, we compare various distributional properties of generated text to the reference distribution, such
as the likelihood of veering into repetition and the perplexity of generated text.
1
0.8
0.6
0.4
0.2
0
0 20 40 60 80 100 ytilibaborP
The latter reveals that text generated by maximizationortop-k samplingistooprobable,in-
BeamSearchTextisLessSurprising dicating a lack of diversity and divergence in
vocabularyusagefromthehumandistribution.
Ontheotherhand,puresamplingproducestext that is significantly less likely than the gold,
correspondingtolowergenerationquality.
Vocabulary usage and Self-BLEU (Zhu et al.,
2018)statisticsrevealthathighvaluesofk are
Timestep BeamSearch needed to make top-k sampling match human Human
statistics. Yet, generations based on high val-
BeamSearch Human uesofkoftenhavehighvarianceinlikelihood,
hintingatqualitativelyobservableincoherency ...toprovideanoverviewofthe ...whichgrantincreasedlifespan currentstate-of-the-artinthefield andthreeyearswarranty.The
issues. NucleusSamplingcaneasilymatchref- ofcomputervisionandmachine AntecHCGseriesconsistsoffive learning,andtoprovidean modelswithcapacitiesspanning
erence perplexity through tuning the value of overviewofthecurrent from400Wto900W.Herewe p,avoidingtheincoherencecausedbysettingk state-of-the-artinthefieldof shouldnotethatwehavealready
computervisionandmachine testedtheHCG-620inaprevious highenoughtomatchdistributionalstatistics. learning,andtoprovidean reviewandwerequitesatisfied
overviewofthecurrent Withitsperformance.Intoday's state-of-the-artinthefieldof reviewwewillrigorouslytestthe
Finally, we perform Human Unified with Sta- computervisionandmachine AntecHCG-520,whichasitsmodel learning,andtoprovidean numberimplies,has520Wcapacity
tistical Evaluation (HUSE; Hashimoto et al., overviewofthecurrent andcontrarytoAntec'sstrong
2019) to jointly assess the overall quality and state-of-the-artinthefieldof beliefsinmulti-railPSUsis
computervisionandmachine equipped...
diversityofthedecodingstrategies,whichcan- learning,and...
not be captured using either human or auto-
Figure2: Theprobabilityassignedtotokensgenmatic evaluation alone. The HUSE evaluation
erated by Beam Search and humans, given the demonstratesthatNucleusSamplingisthebest
same context. Note the increased variance that overall decoding strategy. We include gener-
characterizeshumantext,incontrastwiththeendatedexamplesforqualitativeanalysis–seeFig-
lessrepetitionoftextdecodedbyBeamSearch.
ure 3 for a representative example, and further examplesintheappendix.2
2Codeandallgenerationsareavailableathttps://github.com/ari-holtzman/degen
2
PublishedasaconferencepaperatICLR2020
2 BACKGROUND
2.1 TEXTGENERATIONDECODINGSTRATEGIES
Anumberofrecentworkshavealludedtothedisadvantagesofgenerationbymaximization,which tendtogenerateoutputwithhighgrammaticalitybutlowdiversity(Kulikovetal.,2019;Holtzman
et al., 2018; Fan et al., 2018). Generative Adversarial Networks (GANs) have been a prominent research direction (Yu et al., 2017; Xu et al., 2018), but recent work has shown that when qual-
ity and diversity are considered jointly, GAN-generated text fails to outperform generations from languagemodels(Cacciaetal.,2018;Tevetetal.,2019;Semeniutaetal.,2018). Workonneuraldi-
alogsystemshaveproposedmethodsfordiversebeamsearch,usingatask-specificdiversityscoring functionorconstrainingbeamhypothesestobesufficientlydifferent(Lietal.,2016a;Vijayakumar
etal.,2018;Kulikovetal.,2019;Paletal.,2006). Whilesuchutilityfunctionsencouragedesirable propertiesingenerations,theydonotremovetheneedtochooseanappropriatedecodingstrategy,
and we believe that Nucleus Sampling will have complementary advantages in such approaches.
Finally, Welleck et al. (2020) begin to address the problem of neural text degeneration through an
“unlikelihood loss”, which decreases training loss on repeated tokens and thus implicitly reduces gradientsonfrequenttokensaswell. Ourfocusisonexposingneuraltextdegenerationandprovid-
ingadecodingsolutionthatcanbeusedwitharbitrarymodels,butfutureworkwilllikelycombine training-timeandinference-timesolutions.
2.2 OPEN-ENDEDVSDIRECTEDGENERATION
Manytextgenerationtasksaredefinedthrough(input, output)pairs, suchthattheoutputisaconstrainedtransformationoftheinput. Exampleapplicationsincludemachinetranslation(Bahdanau
et al., 2015), data-to-text generation (Wiseman et al., 2017), and summarization (Nallapati et al.,
2016). We refer to these tasks as directed generation. Typically encoder-decoder architectures are used, often with an attention mechanism (Bahdanau et al., 2015; Luong et al., 2015) or using
attention-basedarchitecturessuchastheTransformer(Vaswanietal.,2017). Generationisusually performed using beam search; since output is tightly scoped by the input, repetition and generic-
ness are not as problematic. Still, similar issues have been reported when using large beam sizes
(Koehn & Knowles, 2017) and more recently with exact inference (Stahlberg & Byrne, 2019), a counter-intuitiveobservationsincemorecomprehensivesearchhelpsmaximizeprobability.
Open-endedgeneration, whichincludesconditionalstorygenerationandcontextualtextcontinuation(asinFigure1),hasrecentlybecomeapromisingresearchdirectionduetosignificantadvances
inneurallanguagemodels(Clarketal.,2018;Holtzmanetal.,2018;Fanetal.,2018;Pengetal.,
2018;Radfordetal.,2019). Whiletheinputcontextrestrictsthespaceofacceptableoutputgenerations,thereisaconsiderabledegreeoffreedominwhatcanplausiblycomenext,unlikeindirected
generation settings. Our work addresses the challenges faced by neural text generation with this increased level of freedom, but we note that some tasks, such as goal-oriented dialog, may fall
somewhereinbetweenopen-endedanddirectedgeneration.

3 LANGUAGE MODEL DECODING
Given an input text passage as context, the task of open-ended generation is to generate text that formsacoherentcontinuationfromthegivencontext. Moreformally,givenasequenceofmtokens
x ...x ascontext,thetaskistogeneratethenextncontinuationtokenstoobtainthecompleted
1 m sequencex ...x . WeassumethatmodelscomputeP(x )usingthecommonleft-to-right
1 m+n 1:m+n decompositionofthetextprobability,
m+n
(cid:89)
P(x )= P(x |x ...x ), (1)
1:m+n i 1 i−1 i=1
whichisusedtogeneratethegenerationtoken-by-tokenusingaparticulardecodingstrategy.
Maximization-based decoding The most commonly used decoding objective, in particular for directedgeneration,ismaximization-baseddecoding.Assumingthatthemodelassignshigherprob-
abilitytohigherqualitytext,thesedecodingstrategiessearchforthecontinuationwiththehighest
3
PublishedasaconferencepaperatICLR2020
Anunprecedentednumberofmostlyyoungwhaleshavebecomestrandedon theWestAustraliancoastsince2008.
WebText dsfsadfd
Thenumberofstrandedwhaleshasincreasedbymorethan50percentinthepastyear, withthenumberofstrandedwhalesontheWestAustraliancoastincreasingbymore
than50percentinthepastyear.ThenumberofwhalesstrandedontheWestAustralian coasthasincreasedbymorethan50percentinthepastyear,withthenumberof
strandedwhalesontheWestAustraliancoastincreasingbymorethan50percentinthe pastyear.
BeamSearch,b=16
TheAustralianFoodSafetyAuthorityhaswarnedAustralia'sbeachesmayberevitalised thisyearbecausehealthyseabirdsandsealshavebeenonthemove.Morethan50,000
seabirds,seamammalsandseahorseshavebeensweptintotheseabytheHolden
CS118andAdelaideAirportCS300from2013.Amajorwhite-batandumidauda
PureSampling migrationacrossAustraliaisunderwayinAustraliaforthefirsttime,withnumbers reachinganestimated50,000.
Lastweek'sintensestormsandaseriesofpowerfulcycloneshavebeenofficiallyblamed forthedeathsofatleastninelargefinwhalesnearWhitsundays-thelargestlossofany
speciesglobally.Thefinwhales:packedinthebellyofonekillerwhalethrashingmadly infearasanothertriestobringittosafety.Whenthecolossalanimalbreachedthe
Sampling,t=0.9 watersofWhitsundays,he'dbeenseentaggedforadecade.
PumpingStation#3shutdownduetoconstructiondamageFindmoreat:
www.abc.net.au/environment/species-worry/ in-the-top-10-killer-whale-catastrophes-in-history.html
“Inthetop10killerwhalecatastrophesinhistory:
1)1986:Upto12orcasstruckbylightning;manydrownedandmanymorebadlyinjured.
Top-k,k=640
Thewhale'sfatewasconfirmedlatelastweekwhentheanimalwasfoundbyfishermen offthecoastofBundaberg.Expertsbelievethewhalewasstruckbyafishingvesseloff
thecoastofBundaberg,anddiedafterbeingsuckedintotheocean.Thewhale'sfate wasconfirmedlatelastweekwhentheanimalwasfoundbyfishermenoffthecoastof
Bundaberg.
Top-k,k=40,t=0.7
Therehasbeenanunprecedentednumberofcalvescaughtinthenetsofwhaling stationsthatoperateinWA.Pilotwhalescontinuetomigratetofeedinggroundsto
feedtheircalves.Theyarenowvulnerableduetothedeclineofwildpopulations; theyarerestrictedtoonebreedingsiteeachyear.ImagecopyrightYoonBoKimBut,
withsharpdeclineinwildpopulationsthesizeofthePetrelsareshrinkinganddwindling
Nucleus,p=0.95 populationmeanstherewillonlyberoomforafewnewfowl.
Poornutritionhasledtoariseinthenumberofstrandedhumpbackwhalesonthe
WestAustraliancoast,veterinaryresearchershavesaid.CarlyHolyoake,fromMurdoch
University,attheAustralianVeterinaryAssociation'sannualconferenceinPerthon
Wednesday,saidanunprecedentednumberofmostlyyoungwhaleshadbecome
WebText strandedonthecoastssince2008.
Figure 3: Example generations continuing an initial sentence. Maximization and top-k truncation methodsleadtocopiousrepetition(highlightedinblue),whilesamplingwithandwithouttempera-
turetendstoleadtoincoherence(highlightedinred). NucleusSamplinglargelyavoidsbothissues.
likelihood. Sincefindingtheoptimumargmaxsequencefromrecurrentneurallanguagemodelsor
Transformersisnottractable(Chenetal.,2018),commonpracticeistousebeamsearch(Lietal.,
2016b; Shen et al., 2017; Wiseman et al., 2017). However, several recent studies on open-ended generationhavereportedthatmaximization-baseddecodingdoesnotleadtohighqualitytext(Fan
etal.,2018;Holtzmanetal.,2018).

3.1 NUCLEUSSAMPLING
Weproposeanewstochasticdecodingmethod: NucleusSampling. Thekeyideaistousetheshape oftheprobabilitydistributiontodeterminethesetoftokenstobesampledfrom.Givenadistribution
P(x|x ),wedefineitstop-pvocabularyV(p) ⊂V asthesmallestsetsuchthat
1:i−1
(cid:88)
P(x|x )≥p. (2)
1:i−1 x∈V(p)
4
PublishedasaconferencepaperatICLR2020 ytilibaborp
1
0.9
0.8
0.7
0.6
0.5
0.4
I do n’tknow .
Figure 4: The probability of a repeated phrase increases with each repetition, creating a positive feedbackloop. Wefoundthiseffecttoholdforthevastmajorityofphraseswetested,regardlessof
phraselengthorifthephrasesweresampledrandomlyratherthantakenfromhumantext.
Figure5: Theprobabilitymassassignedtopartialhumansentences. Flatdistributionsleadtomany moderatelyprobabletokens,whilepeakeddistributionsconcentratemostprobabilitymassintojust
a few tokens. The presence of flat distributions makes the use of a small k in top-k sampling problematic,whilethepresenceofpeakeddistributionsmakeslargek’sproblematic.
Let p(cid:48) = (cid:80) P(x|x ). The original distribution is re-scaled to a new distribution, from x∈V(p) 1:i−1
whichthenextwordissampled:
(cid:26)
P(x|x )/p(cid:48) ifx∈V(p)
P(cid:48)(x|x )= 1:i−1 (3)
1:i−1 0 otherwise.
In practice this means selecting the highest probability tokens whose cumulative probability mass exceedsthepre-chosenthresholdp. Thesizeofthesamplingsetwilladjustdynamicallybasedon
theshapeoftheprobabilitydistributionateachtimestep. Forhighvaluesofp,thisisasmallsubset ofvocabularythattakesupvastmajorityoftheprobabilitymass—thenucleus.

3.2 TOP-kSAMPLING
Top-k sampling has recently become a popular alternative sampling procedure (Fan et al., 2018;
Holtzmanetal.,2018;Radfordetal.,2019). NucleusSampling andtop-k bothsamplefromtruncatedNeuralLMdistributions,differingonlyinthestrategyofwheretotruncate. Choosingwhere
totruncatecanbeinterpretedasdeterminingthegenerativemodel’strustworthypredictionzone.
Ateachtimestep,thetopkpossiblenexttokensaresampledfromaccordingtotheirrelativeprobabilities. Formally, given a distribution P(x|x ), we define its top-k vocabulary V(k) ⊂ V as
1:i−1 the set of size k which maximizes (cid:80) P(x|x ). Let p(cid:48) = (cid:80) P(x|x ). The
x∈V(k) 1:i−1 x∈V(k) 1:i−1 distributionisthenre-scaledasinequation3,andsamplingisperformedbasedonthatdistribution.
Notethatthescalingfactorp(cid:48)canvarywildlyateachtime-step,incontrasttoNucleusSampling.
Difficulty in choosing a suitable value of k While top-k sampling leads to considerably higher
5
PublishedasaconferencepaperatICLR2020 qualitytextthaneitherbeamsearchorsamplingfromthefulldistribution,theuseofaconstantkis
sub-optimalacrossvaryingcontexts. AsillustratedontheleftofFigure5,insomecontextsthehead ofthenextworddistributioncanbeflatacrosstensorhundredsofreasonableoptions(e.g. nounsor
verbsingenericcontexts),whileinothercontextsmostoftheprobabilitymassisconcentratedinone orasmallnumberoftokens,asontherightofthefigure. Thereforeifk issmall,insomecontexts
there is a risk of generating bland or generic text, while if k is large the top-k vocabulary will include inappropriate candidates which will have their probability of being sampled increased by
therenormalization. UnderNucleusSampling,thenumberofcandidatesconsideredrisesandfalls dynamically, corresponding to the changes in the model’s confidence region over the vocabulary
whichtop-ksamplingfailstocaptureforanyonechoiceofk.

3.3 SAMPLINGWITHTEMPERATURE
Another common approach to sampling-based generation is to shape a probability distribution through temperature (Ackley et al., 1985). Temperature sampling has been applied widely to text
generation(Ficler&Goldberg,2017;Fanetal.,2018;Cacciaetal.,2018). Giventhelogitsu
1:|V| andtemperaturet,thesoftmaxisre-estimatedas
exp(u /t) p(x=V |x )= l . (4)
l 1:i−1 (cid:80) exp(u(cid:48)/t) l(cid:48) l
Setting t ∈ [0,1) skews the distribution towards high probability events, which implicitly lowers themassinthetaildistribution. Lowtemperaturesamplinghasalsobeenusedtopartiallyalleviate
the issues of top-k sampling discussed above, by shaping the distribution before top-k sampling
(Radfordetal.,2018;Fanetal.,2018). However,recentanalysishasshownthat,whileloweringthe temperatureimprovesgenerationquality,itcomesatthecostofdecreasingdiversity(Cacciaetal.,
2018;Hashimotoetal.,2019).

4 LIKELIHOOD EVALUATION
4.1 EXPERIMENTALSETUP
While many neural network architectures have been proposed for language modeling, including
LSTMs (Sundermeyer et al., 2012) and convolutional networks (Dauphin et al., 2017), the Transformerarchitecture(Vaswanietal.,2017)hasbeenthemostsuccessfulintheextremelylarge-scale
trainingsetupsinrecentliterature(Radfordetal.,2018;2019).InthisstudyweusetheGeneratively
Pre-trained Transformer, version 2 (GPT2; Radford et al., 2019), which was trained on WebText, a40GBcollectionoftextscrapedfromtheweb.3 WeperformexperimentsusingtheLargemodel
(762Mparameters). Ouranalysisisbasedongenerating5,000textpassages,whichenduponreachinganend-of-documenttokenoramaximumlengthof200tokens. Textsaregeneratedcondition-
ally, conditioned on the initial paragraph (restricted to 1-40 tokens) of documents in the held-out portionofWebText,exceptwhereotherwisementioned.

4.2 PERPLEXITY
Ourfirstevaluationistocomputetheperplexityofgeneratedtextusingvariousdecodingstrategies, accordingtothemodelthatisbeinggeneratedfrom. Wecomparetheseperplexitiesagainstthatof
thegoldtext(Figure6). Importantly,wearguethattheoptimalgenerationstrategyshouldproduce textwhichhasaperplexityclosetothatofthegoldtext: Eventhoughthemodelhastheabilityto
generatetextthathaslowerperplexity(higherprobability),suchtexttendstohavelowdiversityand getstuckinrepetitionloops,asshownin§5andillustratedinFigure4.
Weseethatperplexityoftextobtainedfrompuresamplingisworsethantheperplexityofthegold.
This indicates that the model is confusing itself: sampling too many unlikely tokens and creating contextthatmakesitdifficulttorecoverthehumandistributionoftext,asinFigure1. Yet,setting
the temperature lower creates diversity and repetition issues, as we shall see in §5. Even with our relativelyfine-grainedparametersweep,NucleusSamplingobtainsclosestperplexitytohumantext,
asshowninTable1.
3Availableathttps://github.com/openai/gpt-2-output-dataset
6
PublishedasaconferencepaperatICLR2020
Method Perplexity Self-BLEU4 ZipfCoefficient Repetition% HUSE
Human 12.38 0.31 0.93 0.28 -
Greedy 1.50 0.50 1.00 73.66 -
Beam,b=16 1.48 0.44 0.94 28.94 -
StochasticBeam,b=16 19.20 0.28 0.91 0.32 -
PureSampling 22.73 0.28 0.93 0.22 0.67
Sampling,t=0.9 10.25 0.35 0.96 0.66 0.79
Top-k=40 6.88 0.39 0.96 0.78 0.19
Top-k=640 13.82 0.32 0.96 0.28 0.94
Top-k=40,t=0.7 3.48 0.44 1.00 8.86 0.08
Nucleusp=0.95 13.13 0.32 0.95 0.36 0.97
Table1:Mainresultsforcomparingalldecodingmethodswithselectedparametersofeachmethod.
The numbers closest to human scores are in bold except for HUSE (Hashimoto et al., 2019), a combinedhumanandstatisticalevaluation,wherethehighest(best)valueisbolded. ForTop-kand
NucleusSampling,HUSEiscomputedwithinterpolationratherthantruncation(see§6.1).

4.3 NATURALLANGUAGEDOESNOTMAXIMIZEPROBABILITY
One might wonder if the issue with maximization is a search error, i.e., there are higher quality sentencestowhichthemodelassignshigherprobabilitythantothedecodedones,beamsearchhas
just failed to find them. Yet Figures 2 & 6 show that the per-token probability of natural text is, onaverage,muchlower thantextgeneratedbybeamsearch. Naturallanguagerarelyremainsina
highprobabilityzoneformultipleconsecutivetimesteps,insteadveeringintolower-probabilitybut moreinformativetokens. Nordoesnaturallanguagetendtofallintorepetitionloops,eventhough
themodeltendstoassignhighprobabilitytothis,asseeninFigure4.
Whyishuman-writtentextnotthemostprobabletext?Weconjecturethatthisisanintrinsicproperty ofhumanlanguage. Languagemodelsthatassignprobabilitiesonewordatatimewithoutaglobal
modelofthetextwillhavetroublecapturingthiseffect. Grice’sMaximsofCommunication(Grice,
1975)showthatpeopleoptimizeagainststatingtheobvious.Thus,makingeverywordaspredictable aspossiblewillbedisfavored. Thismakessolvingtheproblemsimplybytraininglargermodelsor
improving neural architectures using standard per-word learning objectives unlikely: such models areforcedtofavorthelowestcommondenominator,ratherthaninformativelanguage.

5 DISTRIBUTIONAL STATISTICAL EVALUATION
5.1 ZIPFDISTRIBUTIONANALYSIS
In order to compare generations to the reference text, we begin by analyzing their use of vocabulary. Zipf’slawsuggeststhatthereisanexponentialrelationshipbetweentherankofawordandits
frequencyintext. TheZipfiancoefficientscanbeusedtocomparethedistributioninagiventext
20
15
10
5
5 10 15
Beam Width
LPP lanoitidnoC
Beam Search Sampling Top-k (t=1.0) Top-k (t=0.7) Nucleus
Human
0.2 T5 em0 p.5 e0 rat0 u.7 re5 1.00 101 102 k103 104 101 102 k103 104
0.1 0.5 0.9 0.99 0.999 0.9999 p
Figure 6: Perplexities of generations from various decoding methods. Note that beam search has unnaturallylowperplexities.Asimilareffectisseenusingatemperatureof0.7withtop-kasinboth
Radfordetal.(2019)andFanetal.(2018). Sampling,Top-k,andNucleuscanallbecalibratedto humanperplexities,butthefirsttwofacecoherencyissueswhentheirparametersaresetthishigh.
7
PublishedasaconferencepaperatICLR2020
Figure 7: A rank-frequency plot of the distributional differences between n-gram frequencies of human and machine text. Sampling and Nucleus Sampling are by far the closest to the human
distribution,whileBeamSearchclearlyfollowsaverydifferentdistributionthannaturallanguage.
Self-BLEUofGenerationsOver5000Documents
1
Self-BLEU4
0.9
Self-BLEU5
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0 t=0.1 t=0.2 t=0.3 t=0.4 t=0.5 t=0.6 t=0.7 t=0.8 t=0.9 t=1.0 k=5 k=10 k=20 k=40 k=8 k0 =16 k0 =32 k0 =6 k40 =12 k80 =25 k60 =5 k12 =0 10 k24 =0 20480 p=0.1 p=0.2 p=0.3 p=0.4 p=0.5 p=0.6 p=0.7 p=0.8 p=0. p9 =0. p9 =5 0. p9 =75 0. p9 =87 0. p5 9 =93 0. p7 95 =96 0. p8 97 =95 8 0. p4 93 =97 95 0. p2 91 =98 97 0. p65 90 =99 93 0. p87 905 =94 96 0.98 907 925 93 94 53 17 15 71875
Figure8: Self-BLEUcalculatedontheunconditionalgenerationsproducedbystochasticdecoding methods;lowerSelf-BLEUscoresimplyhigherdiversity.Horizontalblueandorangelinesrepresent
humanself-BLEUscores. Notehowcommonvaluesoft ∈ [0.5,1]andk ∈ [1,100]resultinhigh self-similarity,whereas“normal”valuesofp∈[0.9,1)closelymatchthehumandistributionoftext.
to a theoretically perfect exponential curve, where s = 1 (Piantadosi, 2014). Figure 7 shows the vocabularydistributionsalongwithestimatedZipfcoefficientsforselectedparametersofdifferent
decodingmethods. Asexpected,puresamplingistheclosesttothehumandistribution,followedby
NucleusSampling. Thevisualizationofthedistributionshowsthatpuresamplingslightlyoverestimatestheuseofrarewords,likelyonereasonwhypuresamplingalsohashigherperplexitythan
human text. Furthermore, lower temperature sampling avoids sampling these rare words from the tail,whichiswhyithasbeenusedinsomerecentwork(Fanetal.,2018;Radfordetal.,2019).

5.2 SELF-BLEU
WefollowpreviousworkandcomputeSelf-BLEU(Zhuetal.,2018)asametricofdiversity. Self-
BLEU is calculated by computing the BLEU score of each generated document using all other generationsintheevaluationsetasreferences. Duetotheexpenseofcomputingsuchanoperation,
wesample1000generations, eachofwhichiscomparedwithall4999othergenerationsasreferences. AlowerSelf-BLEU scoreimplieshigherdiversity. Figure 8showsthatSelf-BLEU results
largelyfollowthatoftheZipfiandistributionanalysisasadiversitymeasure. Itisworthnotingthat
8
PublishedasaconferencepaperatICLR2020
Figure 9: We visualize how often different decoding methods get “stuck” in loops within the first
200tokens. Aphrase(minimumlength2)isconsideredarepetitionwhenitrepeatsatleastthree times