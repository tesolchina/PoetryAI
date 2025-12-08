---
source_pdf: Li_2025_Temperature_Impact_LLM.pdf
converted_date: 2025-12-04T20:30:18.846919
total_pages: 10
model: Google Gemini 2.0 Flash
total_cost_usd: $0.004723
prompt_tokens: 14,460
completion_tokens: 8,192
---

Available online at www.sciencedirect.com
ScienceDirect
Procedia Computer Science 264 (2025) 242–251
InternationalNeuralNetworkSocietyWorkshoponDeepLearningInnovationsandApplications
Exploring the Impact of Temperature on Large Language Models:
Hot or Cold?
Lujun Lia, , Lama Sleema, Niccolo’ Gentileb, Geoffrey Nichilb, Radu Statea
∗ aUniversityofLuxembourg
bFoyerS.A.
Abstract
Thesamplingtemperature,acriticalhyperparameterinlargelanguagemodels(LLMs),modifiesthelogitsbeforethesoftmaxlayer, therebyreshapingthedistributionofoutputtokens.Recentstudieshavechallengedthe“StochasticParrots”analogybydemon-
stratingthatLLMsarecapableofunderstandingsemanticsratherthanmerelymemorizingdataandthatrandomness,modulatedby samplingtemperature,playsacrucialroleinmodelinference.Inthisstudy,wesystematicallyevaluatedtheimpactoftemperature
intherangeof0to2ondatasetsdesignedtoassesssixdifferentcapabilities,conductingstatisticalanalysesonopensourcemodels ofthreedifferentsizes:small(1B–4B),medium(6B–13B),andlarge(40B–80B).Ourfindingsrevealdistinctskill-specificeffects
oftemperatureonmodelperformance,highlightingthecomplexityofoptimaltemperatureselectioninpracticalapplications.To addressthischallenge,weproposeaBERT-basedtemperatureselectorthattakesadvantageoftheseobservedeffectstoidentify
theoptimaltemperatureforagivenprompt.Wedemonstratethatthisapproachcansignificantlyimprovetheperformanceofsmall andmediummodelsintheSuperGLUEdatasets.Furthermore,ourstudyextendstoFP16precisioninference,revealingthattem-
peratureeffectsareconsistentwiththoseobservedin4-bitquantizedmodels.Byevaluatingtemperatureeffectsupto4.0inthree quantizedmodels,wefindthatthe“MutationTemperature”—thepointatwhichsignificantperformancechangesoccur—increases
withmodelsize1.
© 2025 The Authors. Published by Elsevier B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of the IJCNN 2025
Keywords: LargeLanguageModels;SamplingTemperature;ModelPerformanceEvaluation;BERT-basedClassifier;GPT-basedEvaluation
1. Introduction
SincethereleaseofChatGPT,LLMshavesignificantlyimpactedbothacademiaandindustry,revolutionizingthe developmentofartificialintelligence.Opensourcemodelsofdifferentsizeshavefacilitatedadvancesinvariousdo-
mains,[27]includingquestionansweringandsummarization.AkeyfactorinfluencingtheperformanceofLLMsis hyperparameter adjustment. For example, Top-K sampling selects the next token from the K most probable candi-
1 https://github.com/DobricLilujun/temperature_eval
∗
Correspondingauthor.Tel.:+0033-766636416.
E-mailaddress:lilujun588588@gmail.com
1877-0509 © 2025 The Authors. Published by Elsevier B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of the IJCNN 2025
10.1016/j.procs.2025.07.135

Lujun Li et al. / Procedia Computer Science 264 (2025) 242–251 243 dates, while Top-P sampling samples from the smallest set of tokens whose cumulative probability exceeds P [9].
Additionally, the repetition penalty reduces the probability of tokens that have already appeared, helping to avoid repetition.Inthispaper,wefocusontemperature,whichisoneofthemostfrequentlyusedhyperparameters.During
inferenceinLLMs,thisparameterisusedtoscalethelogitsoftheoutputlayer,effectivelycontrollingtherandomness of model predictions. The concept of temperature, denoted as T [1], was first introduced by Ackley, who empha-
sizeditscrucialroleinshapingtheBoltzmanndistribution.Formally,theprobability P ofthei-thtokenisgivenby i
P = eyi/T ,wherey denotesthepre-softmaxactivationofthei-thtoken(commonlycalledthelogit),T represents i V eyj/T i
j=1 thetemperature,andV isthetotalnumberoftokensinthevocabulary.Thevalue P determinestheprobabilitythat
(cid:31) i thei-thtokenwillbegenerated,afterwhichthemodeloutputisproducedbyasamplingalgorithm.AsT increases,
the probability mass function (PMF) [8] becomes more uniform; conversely, as T approaches zero, the distribution collapsestoadeltafunction,causingthealgorithmtobehavegreedilybyalwaysselectingthemostlikelytoken.At
eachgenerationstep,anewtokenisselectedbyrandomlysamplingtheupdatedprobabilitydistribution[13].
Inthisstudy,wefocusonthreekeyresearchquestions(RQs):(RQ1)Towhatextentdoestemperatureimpactthe performanceofLLMsacrossdifferentabilities?(RQ2)Doestemperaturehaveuniformeffectsacrossdifferent
abilitiesandmodels,andwhatarethemaindifferencesobserved?(RQ3)Isthereanoptimaltemperaturefor eachcapability,andcanthebesttemperaturebedeterminedforaspecificprompt?Theremainderofthispaperis
organizedasfollows:Section2reviewsrelatedwork.Section3describestheexperimentalmethods.Section4details theexperimentalsettings.Section5presentsandanalyzestheresults.Finally,Section6concludesthepaper.
2. RelatedWork
Investigationsoftheeffectsoftemperatureremainlimitedintherecentliterature.Moststudiesreportresultsusing only one temperature value, without systematically exploring a wider range, except for the series of Llama models,
whichtestedtwosettingsforcodegeneration[24].Furthermore,generaldatasetsdesignedtoevaluatemultiplemodel capabilitiessimultaneously,suchasthoseforArtificialGeneralIntelligence(AGI;[28]),tendtolackaspecificfocus
onasinglefoundationalability.Forexample,highertemperaturesincreasecreativity[29],whilelowertemperatures improve logical reasoning. For tasks like complex math problems that need both logic and creativity, these effects
may cancel each other out. This makes it difficult to see the real impact of temperature, a phenomenon we call the
“TemperatureParadox”.
Recent studies have examined how temperature settings affect different tasks and dynamic configurations. [22] explored temperature in multitask scenarios using prompt engineering and a range from 0 to 1, finding no signifi-
canteffectonLLMperformance.[19]investigatedtemperatureincreativewriting,measuringperplexityandcosine similarity,andfoundonlyaweakeffectoncreativity.[29]proposedanadaptivetemperaturestrategyforcodegener-
ation,assigninghighertemperaturestohardertokens(suchasthestartofaPythonfunction)andlowertemperatures to tokens with greater model confidence, showing that higher temperatures can help with complex tasks. However,
thereisstillnoclearguidelineforchoosingtemperaturefordifferentLLMs,tasks,orprompts,althoughtemperature adjustmentisimportantforLLMusers,RAGsystems,andagenticAIsystems.
3. Approaches
Toaddressthe“TemperatureParadox”andmoreaccuratelymeasuretheeffectoftemperatureoneachabilitywith minimal bias, we adopt datasets with clear capability preferences and employ a single-prompt format, querying the
modelonlyoncetoavoidmulti-promptassistance.Thisapproachenablesamorepreciseandunbiasedassessmentof theintrinsicabilitiesofLLMs.Wehypothesizethattemperatureinfluencesdifferentmodelabilitiesindistinctways.
Therefore,ourstudyfocusesonsixcoreintrinsicabilitiesthatnotonlyrepresenttheprimarycompetenciesofLLMs butarealsocentraltocomputationallinguisticsresearch.
3.1. EvaluatingIntrinsicAbilities
CausalReasoning(CR):Acognitivefacultyhistoricallyascribedsolelytohumansthatconsistsinderivingconclusionsfromgivenpremisesbyadheringtostrictlogicalprinciples[14].Inthispaper,weuseCRASS[10],apublicly

244 Lujun Li et al. / Procedia Computer Science 264 (2025) 242–251 availablecounterfactualreasoningdatasetthatsimplifiestheevaluationprocessbyrequiringthemodeltoselectthe
correctanswerratherthangenerateit.Top-1Accuracy(T1)isusedtoquantifythefrequencywithwhichthemodel correctlypredictsthetrueclassbyselectingtheclasswiththehighestconfidenceaftermultiplerepetitions.
Creativity(CT):Creativityinvolvesthegenerationofnovelandvaluableideas,concepts,orproductsthatrequire bothoriginalityandeffectiveness[23].ForCT,weadoptaframeworkthatassessesstoriesinfourdimensions:fluency,
flexibility, originality, and elaboration, using customized questions based on the Torrance Test of Creative Writing
(TTCW)procedure[7].Inthisframework,each categoryincludesmultiplestandardevaluationquestions,withtrue orfalsedeterminedbyexpertjudgment.TwelvepubliclyavailableNewYorkerstoriesareusedasplots.TheTTCW
AccuracyisthencalculatedbycountingthenumberofpositiveevaluationsamongallQ&Apairs[12].
In-Context Learning (ICL): ICL reflects an LLM’s ability to understand text and perform tasks using contextual informationandafewexamples[21].Inthisstudy,wefocusontheLongBench-TREClong-contexttask[3],where
themodellearnsfromasequenceofquestionsandanswersandmustclassifyafinalquestionbasedonthiscontext.
Classification Score (CLS), measured by accuracy, evaluates the model’s ability to recognize patterns and make correctpredictionscomparedtothegroundtruth.
InstructionFollowing(IF):IFmeasuresthemodel’sabilitytofollowinstructionsprovidedintheprompts,which is essential for effective LLM applications. For this study, we used InfoBench [20], which introduces the Decom-
posedRequirementsFollowingRatio(DRFR)asametrictoassesstheperformanceofthefollow-upofinstruction.
DRFR decomposes complex instructions for more granular evaluation and has demonstrated greater reliability and effectiveness.
MachineTranslation(MT):MTevaluatesanLLM’sabilitytotranslatetextbetweenlanguages,akeyareawhere
LLMshaveshownstrongperformance.WeusetheFLORES-101benchmark[11]formultilingualevaluation,adopting spBLEU as the metric. BLEU scores measure the similarity between model outputs and reference translations.
Toensurecomparability,wenormalizethespBLEUscoresbydividingby100,sothatallresultsfallwithintherange
[0,1].GiventheprevalenceofEnglishintheLLMtrainingdata,wefocusonEnglish-to-other-languagetranslation, selectingdiversepairs(e.g.,English-to-Maltesian,Indonesian,Latvian,IcelandicandKhmer)tocovervaryinglevels
oftranslationdifficulty.
Summarization (SUMM): Summarization aims to condense long texts into concise summaries while preserving key information and main ideas. One of the main challenges in this task is the reliable evaluation. To address this,
we use the “benchmark_llm_summarization” dataset [26], which provides expert-written reference summaries. For evaluation, we adopt the reference-based metric Rouge-L F1, which measures the overlap of the longest common
subsequence between generated and reference summaries, balancing precision and recall, and has been shown to correlatewellwithhumanjudgments[16].
3.2. LLM-as-a-JudgeEvaluation
Table1:Selecteddatasetsandevaluationmetrics
Ability Dataset Samples Metrics Source Evaluations
CR CRASS 3500 Top-1accuracy [10] GPT3.5
CT Creativity_eval 84 TTCWAccuracy [7] GPT3.5
ICL LongBench-TREC 1015 CLSscore [3] ExactMatching
IF InfoBench 3500 DRFR [20] GPT3.5
MT Flore101 2100 NormalizedspBLEU [11] SPMtokenizers
SUMM benchmark_llm_summarization 2114 Rouge-LF1Score [26] ExactMatching Fig.1:CosineSimilarityUsingBERTEmbeddingModel
LLM-as-a-Judge has been widely used and has been proven to be highly aligned with human judgment [18].
Due to the inherent stochasticity of LLMs and the flexibility in textual expressions that convey identical meanings, particularlyinsmallandmediummodels,unintendedresultsoftenappearprecedingorfollowingthetargetresponse.
This makes reference-based evaluations, such as exact matching or similarity metrics, particularly challenging. For example,similaritymetricshavetwomainissues:(1)Itishardtosetaclearcutoffforcorrectanswers;(2)Embedding-
basedmethodsoftenmisskeywordslike“not,”asshowninFigure1[2].
AdvancedmodelssuchasGPT-4oandDeepSeek[5,4]haveachievedstrongresultsonmanybenchmarks.Fortasks withcomplexanswersorchallengingevaluation,weuseLLM-as-a-Judge.ForCR,CT,andIF,weuseChatGPTwith
carefully designed prompts instead of exact matching or human annotation. These judgments are used to calculate

Lujun Li et al. / Procedia Computer Science 264 (2025) 242–251 245 the metrics described in Section 3.1. For the other three abilities with simple reference answers, we use standard
evaluationmethods,asshowninTable1.
4. Experiments
4.1. GeneralExperimentSettings
In this study, experiments begin with the selection of diverse benchmark datasets designed to challenge state-ofthe-art(SOTA)models,asshowninTable2.Evaluationiscarriedoutprimarilyinaquestion-answerformatorthrough
matchingfunctions,withspecificmetricsappliedtoeachdataset.Allmodelsarequantizedto4bitsusingtheAWQ method [17], and vLLM [15] is used as the default inference acceleration framework. Each question is tested three
timesacross12models.
SmallSizeModels(1B-4B) MediumSizeModels(6B-13B) LargeSizeModels(40B-80B)
Model Size Date Model Size Date Model Size Date
Llama-3.2-1B-Instruct 1.2B Sep2024 Llama-2-7b-chat-hf 6.7B Jul2023 Llama-2-70b-chat-hf 69.0B Jul2023
Llama-3.2-3B-Instruct 3.2B Sep2024 Llama-2-13b-chat-hf 13.0B Jul2023 Meta-Llama-3-70B-Instruct 70.6B Apr2024
Phi-3.5-mini-instruct 3.8B Jun2024 Mistral-7B-Instruct-v0.2 7.2B Mar2024 Mixtral-8x7B-Instruct-v0.1 46.7B Dec2023
Qwen2.5-1.5B-Instruct 1.5B Sep2025 Meta-Llama-3-8B-Instruct 8.0B Apr2024 – – –
Qwen2.5-3B-Instruct 3.1B Sep2025 – – – – – –
Table2:InvestigatedSmall,Medium,andLargemodelswiththeirrespectivesizesandreleasedates.
The temperature settings range from 0.1 to 1.9 in increments of 0.3, resulting in seven distinct configurations for each model. Temperatures above 2.0 are excluded, as previous research has shown that higher values tend to
produce non-informative and excessively incoherent text [6]. Each model is evaluated using only one question per test.Weconsistentlyusedgpt-3.5-turbo-0125astheevaluationmodelwithatemperaturesettingof0.01,andselected
open source models as listed in Table 2. Nucleus sampling was adopted, as it yields perplexity values closest to humantext[13],withthefollowingparameters:max_length=4096,Top_P=0.9,repetitionpenalty(RP)=1.0,and
max_new_tokens=1024.
4.2. SupplementaryExperiment
4.2.1. BestTemperatureSelectionOnSuperGLUE
SuperGLUEisabenchmarkconsistingofeighttasksforevaluatingword-sensedisambiguation,naturallanguage inference,coreferenceresolution,andquestionanswering[25].Themainresultsfromtheprevioussectioncanbeused
toidentifytheoptimaltemperatureforagivenpromptandmodel,providedthattheprimaryabilityrequiredforthe promptisknown.Tothisend,aclassificationmodelbasedonafine-tunedBERTframework,denotedas“BERT-based
Selector",isproposed,whichistrainedontheexperimentalpromptstailoredforthemainexperimentsandwillfinally beusedinclassifyingeveryinputprompt.Anotheroptionistoobtaintherequiredabilityforthepromptbasedonthe
well-designedpromptthatwillbeaskedtoGPTmodels,denotedas“GPT-basedSelector".
The basic idea of this selector is the following: Let F be a selection model, either BERT or GPT, acting as an ability predictor based on a given prompt x . The model output F(x ) represents the predicted ability most closely
p p associatedwiththegivenprompt x .Forexample,givenatrainingpromptsuchas x =“Translate‘J’aimelechat’
p p from French to English”, the model F(x ) would be expected to predict “MT” (Machine Translation) as the most
p requiredability.Assuch,theoptimaltemperatureparameterT = argmax (T,F(x ),M)isselectedtomaximize
∗ T p
D theestimatedperformanceofthemodelMonthetaskF(x )underdifferenttemperaturesettings,where ()represents
p
D theperformancedistributionofagivenmodelMovertemperaturesobtainedfrompreviousmainexperimentalresults.
Totestthisframework,weevaluatedthreemodelsofdifferentsizes—Llama-3.2-1B-Instruct(Small),Llama-3-8B-
Instruct(Medium),andMixtral-8x7B-Instruct-v0.1(Large)[25]—ontheSuperGLUEbenchmark.Eachquestionin thebenchmarkwasaskedthreetimes,andeachinstancewasgeneratedbyincrementingtherandomseed,initiallyset
to42,by1foreachsuccessiveiteration.

246 Lujun Li et al. / Procedia Computer Science 264 (2025) 242–251
4.2.2. ExperimentsOnExtendedSettings
We also investigated the temperature range [0,4] while maintaining 4-bit quantization. Although we observed performancedegradationandinconsistentgenerationsattemperaturesabove2,wedidnotfindevidenceforaspecific
“Mutation Temperature” in large models. To further explore the effect of inference precision, we repeated the main experiments on the same three models using FP16 precision, focusing on the temperature range from 0 to 2, to
determinewhethertemperatureeffectsdifferwheninferenceprecisionisaltered.Additionally,sinceTop-K andTop-
Psamplinginfluencetheoutputdistributionatthecandidateselectionlevel,whileRPoperatesatthelogitslevel,we furtherevaluatedvarioussettingsforTop-K(2,5,10),Top-P(0.8,0.9,1.0),andRP(0.0,1.0,2.0).Theseexperiments
were conducted on all three models mentioned above to systematically assess the impact of these parameters on performance.
5. ResultsandAnalysis
5.1. FindingsfromStatisticalAnalysis
Table 3 provides a summary of the temperature-performance correlations in six abilities, based on results from threecategoriesofmodels.“P.Coef.”and“S.Coef.”correspondtothePearsonandSpearmancorrelationcoefficients,
respectively. “Range (%)Max” may be interpreted as the relative performance variation across temperatures, while
“Range Max (%)” refers to the maximum relative ranges within the size category. “CV” (Coefficient of variation) representstheratioofaverageperformancetostandarddeviation,and“CVMax”indicatesthehighestCVsobserved
within the size category. The average accuracy and standard deviation for the temperatures and models within each grouparealsoreported.
Table3:Comparisonoftemperature-performancecorrelationsforsixabilitiesacrossthreemodelcategories.
RangeMax(%) CVMax AverageAccuracy StandardDeviation
Ability P.Coef. P.p-value S.Coef. S.p-value
Small Medium Large Small Medium Large Small Medium Large Small Medium Large
CR -0.07 0.00 -0.07 0.00 146.02 49.37 19.41 58.79 14.88 6.43 0.41 0.52 0.82 0.05 0.03 0.02
CT -0.14 0.00 -0.10 0.00 186.81 154.55 82.02 82.64 72.90 28.07 0.36 0.45 0.47 0.27 0.12 0.08
ICL -0.10 0.00 -0.09 0.00 122.04 55.52 20.19 48.83 21.66 7.20 0.38 0.26 0.49 0.06 0.04 0.01
IF -0.40 0.00 -0.37 0.00 154.65 116.63 22.03 72.22 47.64 8.04 0.49 0.68 0.73 0.26 0.08 0.02
MT -0.216 0.00 -0.40 0.00 192.32 162.59 76.86 91.09 72.14 27.35 4.72 5.95 11.55 3.19 2.54 1.96
SUMM -0.51 0.00 -0.45 0.01 154.29 89.20 4.35 72.89 32.70 1.57 0.16 0.21 0.23 0.09 0.02 0.00
Inthistable,itcanbeobservedthattheperformanceofIF,MT,andSUMMexhibitsrelativelystrongcorrelations with temperature, as indicated by both correlation coefficients. The statistical significance of these correlations is
further supported by p-values of zero. Furthermore, both “Range Max” and “CV Max” decrease as the size of the model increases, which statistically suggests that larger models are more robust to temperature-induced variations.
Theaverageaccuracymetricfurtherdemonstratesthatlargermodelsachievehigherstatisticalperformanceacrossall sixabilities.Inparticular,performancedifferencesamongmodelsofdifferentsizesarerelativelysmallforCT,IF,and
SUMM,butmuchmorepronouncedforCR,ICL,andMT.Thesefindingsprovidepracticalguidanceforselectingthe modelsizeaccordingtospecificfunctionalrequirements.
5.2. TemperatureEffectsonDifferentAbilities
Figure2illustratestheimpactoftemperatureonmodelsofvaryingsizesacrossarangeofevaluatedabilities.Lines showthemeanperformanceforeachmodelsize,whileshadedregionscorrespondto 0.2standarddeviations.Forthe
± sakeofconsistency,allevaluationmetricsenumeratedinTable1—includingspBLEUformachinetranslation—are
uniformlyreferredtoas“accuracy”andhavebeennormalizedtotheinterval[0,1].
Causal Reasoning (CR). CR questions are counterintuitive and require logical reasoning, each with three options.
Medium and large models exceed the 33.3% random baseline, while small models perform only slightly above this chancelevel—byapproximately7%—acrossmosttemperaturesettings,indicatinglimitedreasoningability.Thelarge
andmediummodelsshowslightimprovementatatemperatureof1.3,suggestingthathighertemperaturesmayhelp toaddresscomplexproblems.TheoptimaltemperatureforCRisnotalwayszeroandanincreaseintemperaturedoes

Lujun Li et al. / Procedia Computer Science 264 (2025) 242–251 247
0.90
0.80
0.70
0.60
0.50
0.40
0.30
0.20
Temperature ycaruccA
CR
0.60
0.50
0.40
0.30
0.20
0.10
Temperature ycaruccA
CT
0.60
0.50
0.40
0.30
0.20
Temperature ycaruccA
ICL
0.80
0.70
0.60
0.50
0.40
0.30
0.20
0.10
0.00
0.25 0.50 0.75 1.00 1.25 1.50 1.75
Temperature ycaruccA
IF
0.14
0.12
0.10 0.08
0.06
0.04
0.02
0.00
0.25 0.50 0.75 1.00 1.25 1.50 1.75
Temperature ycaruccA
MT
0.25
0.20
0.15
0.10
0.05
0.25 0.50 0.75 1.00 1.25 1.50 1.75
Temperature ycaruccA
SUMM
Model Averages
Small Average Medium Average Large Average
Fig.2:Averageperformancetrendsfordifferentmodelsizes,withshadedbandsindicatingvariability.
notnecessarilyreduceperformance.Incontrast,smallmodelsdonotdemonstratesubstantialcausalreasoningability withinthescopeofthisstudy.
Creativity(CT). Anoptimaltemperatureof1.3isrecommendedformediumandlargemodelstomaximizecreativity.
Small models show a marked decline in creativity at T = 1.0, while medium and large models are only affected at
T =1.7.Generally,temperaturefirstincreasesandthendecreasescreativity.Smallmodelsaremorecreativeatlower temperatures,butlargemodelsaremorerobustandgeneratemorediverseoutputs,asindicatedbytheirwidershaded
regions.Ingeneral,temperaturestronglyinfluencescreativity,withmoderatevaluesbeingthemostbeneficial.
In-Context Learning (ICL). Large models achieve the best average performance, while the difference between medium and small models is minimal. This indicates that ICL, as an emerging property of LLMs, requires a suffi-
cientlylargemodelsize,highlightingthesignificanceofscalinglaws.Mediummodelsshowlessperformancedecline than small models. At a temperature of 1.7, small models degrade faster than medium models, despite outperform-
ing them at lower temperatures. Large models maintain stable performance across temperatures from 0 to 2, with noabruptperformancedropobserved.Increasingtemperaturegenerallyreducesperformance,althoughlargemodels
mayexperienceslightimprovementsathighertemperatures.
InstructionFollowing(IF). ThebehaviorofIFisparticularlynoteworthy.Asthetemperatureincreasesfrom0to1,
IFperformanceremainslargelyunchanged.However,whenthetemperatureexceeds1,differentmodelsexperience relativelypronouncednegativeeffects,andthelargerthemodelsize,thelaterthesenegativeeffectsemerge.Perfor-
mance changes with temperature are abrupt: small models exhibit a mutation between 1.0 and 1.3, medium models between1.3and1.6,andlargemodelsdemonstrateamoderatemutationtemperaturefrom1.6to1.9.Therefore,for
usersofLLMswhorequirestrictadherencetoinstructions,itisadvisabletosetthetemperaturebelow1.
MachineTranslation(MT). Slightlyincreasingthetemperaturewithinthelowrangemarginallyimprovestranslation performance for small and medium models only. The rise in temperature has the most detrimental effect on MT, as
indicatedbythehighestrangeofperformanceandCVinTable3.Thistrendcanbeattributedtotheinherentlydeterministicnatureoftranslation,andallmodelsexhibitcomparabledeclinesinperformance.Theoptimaltemperatureis
closetozero(0+ϵ),andlanguageunderstandingperformancedependsprimarilyonthebreadthofthetrainingdata andthemodel’sparametersize.
Summarization(SUMM). Temperatureeffectcurvesareinitiallystablebutdropsharplyathighertemperatures,especiallyforsmallmodels.Statisticalanalysisshowsastrongnegativecorrelationbetweenperformanceandtemperature.
SUMMtasksfollowasimilartrendtoIFtasks,butthemutationtemperatureformediummodelsishigher(about1.7), andlargemodelsshownoclearmutationtemperature.

248 Lujun Li et al. / Procedia Computer Science 264 (2025) 242–251
5.3. SupplementaryExperiment
5.3.1. BestTemperatureSelectiononSuperGLUE
We conducted experiments on three models, as shown in Table 4. The table presents the SuperGLUE validationaccuracyunderdifferenttemperaturesettings: ACC
D denotestheaccuracywiththeDefaulttemperatureof1.0,
while ACC and ACC represent the precision achieved by dynamically selecting the optimal temperature using
B C ourfine-tunedBERTmodelandChatGPT-basedprompting,respectively.Thiscomparisonclearlydemonstratesthe
performancedifferencefromoptimaltemperatureselection.
Table4:SuperGLUEvalidationaccuracyunderdefaultanddynamicallyselectedtemperaturesettings.
Model Type COPA WIC WSC Average
ACCD 0.510 0.196 0.346 0.252
Llama-3.2-1B-Instruct ACCB 0.600 0.500 0.356 0.494
ACCC 0.600 0.477 0.365 0.477
ACCD 0.860 0.547 0.673 0.600
Meta-Llama-3-8B-Instruct ACCB 0.900 0.556 0.673 0.612
ACCC 0.900 0.549 0.664 0.605
ACCD 0.800 0.608 0.298 0.593
Mixtral-8x7B-Instruct-v0.1 ACCB 0.800 0.608 0.298 0.593
ACCC 0.800 0.608 0.298 0.593
Adjusting the temperature can greatly improve the performance of WIC (one of the tasks in SuperGLUE) for
Llama-3.2-1BandMeta-Llama-3-8B-Instruct.Thisshowsthattheoptimaltemperatureselectorprovidesstableperformance,avoidingpotentialperformancedropsthatcanoccurwhenusingafixedtemperature.Whenworkingwith
smallmodels,thisisindeedoneofthenecessaryparameterstoconsider,especiallyinresource-constrainedscenarios.
Considering that SuperGLUE primarily evaluates a range of different capabilities, our optimal temperature selector still demonstrates consistent improvements. It is important to mention that this selector does not inherently boost
performance—Supervised Fine-Tuning (SFT) remains the primary method—but it ensures that the model achieves thebestpossibleperformancebyavoidingsuboptimalsettings.Forlargemodels,wedidnotobservesignificantper-
formance differences, indicating that optimizing the temperature setting is generally less critical for larger models.
However,assuggestedinpreviousfindings,whenlargemodelsareusedtosolvecomplexreasoningtasks,ahigher temperaturecansometimesleadtoperformancegains.Therefore,adjustingthetemperaturemaystillbenecessaryin
suchscenarios.
5.3.2. ResultsonExtendedSettings
0.80
0.60
0.40
0.20
0.00
Temperature ycaruccA
CR
0.70
0.60
0.50
0.40
0.30
0.20
0.10
0.00
Temperature ycaruccA
CT
0.60
0.50
0.40
0.30
0.20
0.10
0.00
Temperature ycaruccA
ICL
0.70
0.60
0.50
0.40
0.30
0.20
0.10
0.00
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
Temperature ycaruccA
IF
0.18
0.15
0.13
0.10
0.08
0.05
0.03
0.00
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
Temperature ycaruccA
MT
0.25
0.20
0.15
0.10
0.05
0.00
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
Temperature ycaruccA
SUMM
Models
Llama-3.2-1B-Instruct (4-bit) Meta-Llama-3-8B-Instruct (4-bit) Mixtral-8x7B-Instruct-v0.1 (4-bit)
Llama-3.2-1B-Instruct (full) Meta-Llama-3-8B-Instruct (full) Mixtral-8x7B-Instruct-v0.1 (full)
Fig.3:Performancewithextendedtemperatureto4.0

Lujun Li et al. / Procedia Computer Science 264 (2025) 242–251 249
Extension to 4.0. Fig. 3 presents the performance curves of models with 4-bit precision across six capabilities as temperature varies; “Full” refers to FP16 precision inference. Extending the temperature range helps identify both
the“mutationtemperature,”whereperform