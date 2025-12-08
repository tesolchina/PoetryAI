---
source_pdf: Ravfogel et al..pdf
converted_date: 2025-12-04T20:02:28.291754
total_pages: 6
model: Google Gemini 2.0 Flash
total_cost_usd: $0.003239
prompt_tokens: 6,454
completion_tokens: 6,484
---

# Conformal Nucleus Sampling
ShauliRavfogel1,2 YoavGoldberg1,2 JacobGoldberger1
1Bar-IlanUniversity 2AllenInstituteforArtificialIntelligence
{shauli.ravfogel, yoav.goldberg}@gmail.com,jacob.goldberger@biu.ac.il

Abstract Directsamplingfromthenext-worddistribution computed by the model often generates incoher-
entgibberishtext. Temperaturesampling(Ackley etal.,1985)isawordsamplingapproachbasedon
rescalinglogitscoresbeforeapplyingthesoftmax functiontocomputetheworddistribution. Other
methods limit the sampling space to a small predictionsettoavoidthe“unreliabletail”(Holtzman
etal.,2020). Intop-k sampling(Fanetal.,2018), wesampleonlyfromthetop-k mostlikelywords.
Instead of sampling only from the most likely k words,top-p(nucleus)samplingchoosesfromthe
smallest possible set of words whose cumulative probability exceeds the probability p (Holtzman
et al., 2020). Top-p sampling enables a dynamicallysizedwindowofwords,unliketop-k which
fixes the size of k for every step. Finally, locally typical sampling (Meister et al., 2022) and trun-
cation sampling (Hewitt et al., 2022) are recent variantsoftop-pthataimtomakeitmoresuitable
forlanguagegeneration.

Language models generate text based on successively sampling the next word. A
decoding procedure based on nucleus (top-p) sampling chooses from the smallest possible
set of words whose cumulative probability exceeds the probability p. In this work, we
assess whether a top-p set is indeed aligned with its probabilistic meaning in various
linguisticcontexts. Weemployconformalprediction, a calibration procedure that focuses
ontheconstructionofminimalpredictionsets according to a desired confidence level, to
calibrate the parameter p as a function of the entropyofthenextworddistribution. Wefind
that OPT models are overconfident, and that calibration shows a moderate inverse scaling
withmodelsize.

https://github.com/shauli-ravfogel/ conformal-prediction

# 1 Introduction
Modernlanguagegenerationmethodsareallbased oncomputingtheconditionalnext-worddistribu-
tion. However, there is still considerable debate about the best way to extract the next word from
thatdistribution. Mostcurrenttextgenerationmethods employ one of a handful of standard decod-
ing strategies, which are characterized as either deterministic or stochastic in nature. A greedy
search strategy selects the word with the highest probability at each timestep. The greedy method
and its beam search variations work remarkably well for machine translation but outside of this
context,tendtoreturndulltextordegeneratetext
(Holtzman et al., 2020; Cohen and Beck, 2019).
Holtzmanetal.(2020)arguedthathigh-qualityhumanlanguagedoesnotfollowapatternofhighest-
probabilitynextwords,ashumansexpectthegeneratedtexttonotberepetitiveorboring. Thesame
problemoccurswithbeamsearch.

The top-p prediction set has a concrete probabilistic interpretation. Here we examine whether
theprobabilitythatthe“correct”wordbelongsto thesetofwordsproducedbythetop-palgorithmis
indeedp. Moregenerallyweexpectthatthenextwordpredictionwouldbecalibrated,meaningthat
the output of the next-word softmax layer would accuratelyreflectthetrueworddistribution. Para-
metric calibration methods, such as Temperature
Scaling(Guoetal.,2017),whichadjusttheconfidenceofthemostprobableword,arenotsuitable
for adjusting the size of the prediction set. ConformalPrediction(CP) (Vovketal.,1999,2005;
ShaferandVovk,2008;AngelopoulosandBates,
2021)isanon-parametriccalibrationmethodthat, givenavaluep,aimstobuildapredictionsetwitha
guaranteethattheprobabilitythatthecorrectword is within this set is indeed p. Note that this no-
tionofcalibration,whichisdistinctfromtheway calibrationisusuallyformulatedinlanguagemod-
3202 yaM
4
]LC.sc[
1v33620.5032:viXra

elingsettings,exactlycoincideswiththegoalofthe Denotep (i) = p(y = i|x ;θ). Definetheconfort t t
top-p prediction model. The model-agnostic and malscorestobe:
distribution-freenatureofCPmakesitparticularly
(cid:88) s = p (i) t = 1,...,n (2)
suitableforlargeneuralnetworkmodels. Wethus t t
{i|pt(i)≥pt(yt)} appliedCPanalysistoasseswhetherthetop-ppro- ThisCPscoreisknownastheAdaptivePrediction
cedureiscalibratedand,ifneeded,tuneittohave Sets(APS)score,andwasfirstintroducedin(Rothe desired probabilistic interpretation. We find manoetal.,2020). Notethaty ∈ C (x )ands
t st t t that OPT models of different sizes (Zhang et al., istheminimalthresholdinwhichthetrueclassy
t
2022) are not calibrated according to the confor- isinapredictionsetofx .
t malprediction theory, andthat calibrationshows We next look for a minimal threshold qˆsuch
moderate inverse scaling. Additionally, we show thatthecorrectlabely isincludedintheprediction t
that the degree of calibration varies significantly setC (x )foratleast(1−α)npointsofthevalidaqˆ t
with the entropy of the model’s distribution over tionset. Inotherwords,qˆcalibratesthetop-(1−α) the vocabulary. We thus propose a new Confor- prediction-setonthevalidationset. Wecaneasily
maltop-pdecodingalgorithm,whichensuresthat find qˆby first sorting the n scores s ,...,s and
1 n thetop-psamplinghasameaningfulprobabilistic thenqˆisthe(1−α)-quantileofthevalidation-set
interpretation. scores. Oncethenetworkiscalibrated,ifwewant to form a prediction set for a new test sample x,
# 2 CPforLanguageGeneration thatcontainsthetrueclasswithprobability(1−α),
we use C (x). The CP Calibration procedure for qˆ
Inthissection,webrieflyreviewtheSplitConforcalibratingthetop-pworddecodingissummarized
mal Prediction algorithm (Vovk et al., 2005) and inAlgorithm1. Theconformalpredictiontheory
discussitsrelevancetolanguagegenerationmodprovidesthefollowingguaranteeonthethreshold
els. Consider anetworkthat classifies aninputx qˆ(Vovketal.,2005).
intok pre-definedclasses. Thenetwork(softmax
Theorem: Assumeatestpoint(x,y)andthen layer) output has the mathematical form of a dis-
validation points are independent and identically tribution. However,thisdoesnotnecessarilymean
distributed(oratleastexchangeable). Letqˆbethe thatitaccuratelyreflectthetrueclassdistribution.
(cid:100)(n+1)(1−α)/n(cid:101)-quantile of the validation set
Let(x,y)beatestinstanceanditscorrespondscores. Then
ingclass. Wewanttofindasmallsubsetofclasses
1
(apredictionset)C(x) ⊂ {1,...,k}suchthat 1−α ≤ p(y ∈ C (x)) ≤ 1−α+ . (3) qˆ
n+1 p(y ∈ C(x)) ≥ 1−α (1) Note that this is a marginal probability over all
the test points and is not conditioned on a given where 1−α ∈ [0,1] is a user-chosen error rate. input. Exchangeability means that the sequence
(Weusetheterm1−αinsteadofptocomplywith distribution is not altered by permuting the order
CP standard notation). In words, the probability oftherandomvariables.
that the set C(x) contains the correct label is at Inthisstudy,weaimtoapplytheconformalpreleast 1−α. We call this property the marginal dictionframeworktolanguagegenerationmodels
coveragesincetheprobabilityisaveragedoverall toanalyzethepredictionsetsusedforsamplingthe the data points (x,y). Denote the prediction set nextword. Thejointdistributionofwordsinatext
obtainedbytakingthemostprobableclassesuntil is neither IID nor exchangeable, since the words the total mass just exceeds a value q, by C q(x). arecorrelatedandtheorderofthewordsinasen-
Letqˆ∈ [0,1]bethesmallestthresholdvaluethat tenceissignificant. Arecentstudy(Oliveiraetal., p(y ∈ C qˆ(x)) ≥ 1−α. If qˆ > 1−α the model 2022)showedthatapplyingtheusualCPalgorithm
can be viewed as over-confident. If qˆ < 1−α to a stationary β-mixing process (rather than an themodelcanbeviewedasunder-confidentandif exchangeableone)resultsinaguaranteedcoverage
qˆ= 1−αthemodeliscalibratedinthesensethat levelof1−α−η,whereη dependsonthemixing theprobabilitythatthecorrectlabelisinthe1−α propertiesoftheprocessandistheoreticallyhardto
predictionsetisindeed1−α. know,orbound. Roughlyspeaking,β-mixingpro-
Ifthemodelisnotcalibrated,wecancalibrateit cessesarestochasticprocessesinwhichfar-away usingalabeledvalidationset(x ,y ),...,(x ,y ).
1 1 n n

Algorithm1CPCalibrationoftheTop-pdecoding
Input: Avalidationsetcomprisedofnextword distributions p ,..,p with the corresponding 1 n
correctwordsy ,..,y andaconfidencelevelp.
1 n fort = 1,...,ndo
s = (cid:80) p (i) t {i|pt(i)≥pt(yt)} t endfor
Define qˆ to be the (cid:100)(n+1)p/n(cid:101)-quantile of
{s ,...,s }.
1 n
Output: Use top-qˆdecoding to guarantee that the probability that the correct word is in the
top-qˆpredictionsetisatleastp.

# 3 Experiments
Inthissection,weapplytheconformalprediction calibrationmethodtoanalyzethecalibrationstatus
ofthetop-pnucleussampling.

Setup. We experimented with variants—from
125Mparametersupto30Bparameters—ofOPT
(Zhangetal.,2022),aleft-to-rightlanguagemodel.
We ran the models on 10,000 English Wikipedia
1https://huggingface.co/datasets/wikipedia

|        |        |
| ------------- |:-------------:|
| 10000 |        |
| 8000  |        |
| 6000  |        |
| 4000  |        |
| 2000  |        |
| 0     |        |
| 0 1 2 3 4 |        |
| Entropy |        |
| tnuoC |        |
| Entropy Histogram |        |

|        |        |
| ------------- |:-------------:|
| 8000 |        |
| 7000  |        |
| 6000  |        |
| 5000  |        |
| 4000  |        |
| 3000  |        |
| 2000  |        |
| 1000  |        |
| 00.0 0.2 0.4 0.6 0.8 1.0 |        |
| Max probability |        |
| tnuoC |        |
| Max probability Histogram |        |

|        |        |
| ------------- |:-------------:|
| 0.9 |        |
| 0.8 |        |
| Acc. |        |
| 0.7 |        |
| 0.6 |        |
| 0.5 |        |
| 20 40 60 80 100 |        |
| Entropy Percentile |        |
| Figure2: Effectiveaccuracywhenusingnucleussam- |        |
| pling with p = 0.9, for different entropy percentiles, |        |
| fortheOPT350Mmodel. |        |

|        |        |
| ------------- |:-------------:|
| 1.0 |        |
| 0.9 |        |
| 0.8 |        |
| q |        |
| 0.7 |        |
| 1 =0.99 |        |
| 1 =0.9 |        |
| 0.6 |        |
| 1 =0.8 |        |
| 1 =0.7 |        |
| 1 =0.6 |        |
| 1 =0.5 |        |
| 0.5 |        |
| 20 40 60 80 100 |        |
| Entropy Percentile |        |
| Figure 3: qˆthreshold scores when calibration is per- |        |
| formed over the examples belonging to each entropy |        |
| percentileseparately. |        |

Figure1:HistogramsofentropyoftheoutputprobabilitydistributionfortheOPT350Mmodel.

points are approximately independent in a quantifiablemanner. Inalltheexamplestheychecked,
theauthorsassessedthattheadditionalpenaltyincurredbyusingCPwithstationaryβ-mixingpro-
cesses was virtually insignificant. Manning and
Schutze (1999) argue that even though not quite correct,naturallanguagecanbemodeledasstation-
ary, ergodic processes. Khandelwal et al. (2018) showedthattheLSTMlanguagemodel’smemory
isempiricallyboundedatroughly200wordsand thus the model can be viewed as an aperiodic re-
current(andthereforeβ-mixing)Markovchain. It isreasonabletoassumethathumanlanguageand
transformer-based language models can also be modeledasβ-mixingprocesses. Hence,applying
CPtolanguagegenerationmodelsyieldsmeaningfulresults(atleastqualitatively).

sentences1,andcollectedthedistributionofthevocabularyovereachtokenineachsentence,resulting
inatotalof245,923distributions. Thedistribution oftheentropyvalues,aswellasthemaximumprob-
ability, was far from being uniform (Fig. 1). We sortedalltheinstancesbyentropy,andcalibrated
theexamplesbelongingtoeachequally-sizedpercentile independently (from 0-10% to 90-100%).
Thepatternsarehighlysimilaracrossmodels. We report results on the 350M parameters model un-
less specified otherwise. We use Nvidia 2080TI
GPUs.

Dependency of the confidence on the entropy.
First,weevaluatedtheconfidencescoresofastandardnucleussamplingscheme. Wechosep = 0.9
(a commonly used value) and recorded the effectiveconfidence,i.e.,theproportionofcaseswhere
thecorrectwordwasindeedinthetop-pprediction set. Fig. 2 shows the effective confidence for the

|        |        |
| ------------- |:-------------:|
| 1.T 0hreshold value for different levels of confidence |        |
| Calibrated |        |
| 125M |        |
| 0.8 |        |
| 350M |        |
| 1B |        |
| 2B |        |
| 0.6 |        |
| 6B |        |
| q |        |
| 13B |        |
| 30B |        |
| 0.4 |        |
| 0.2 |        |
| 0.0 |        |
| 0.0 0.2 0.4 0.6 0.8 1.0 |        |
| 1 (Confidence) |        |
| Figure 4: qˆthreshold values needed to ensure a con- |        |
| fidence of 1-α. The OPT models show slight inverse |        |
| scalingwithrespecttocalibration. |        |

predictionsbelongingtodifferentpercentilesofentropy. The results indicated that setting p = 0.9
didnottranslatetoapredictionsetthatcontained thecorrecttokenin90%ofthecases,motivating
our calibrated decoding. In Fig. 3, we show the per-entropyCPcalibrationresults,for10entropy
binscorrespondingtopercentiles. Whilethemodel was always overconfident, the level of overcon-
fidence decreases with the entropy percentile. In otherwords,whenthemodelisapparentlythemost
certain—asreflectedinlowentropyvalues—itis most overconfident. Note that in the case of low
entropythesinglehighestprobabilitycanbemore than 0.9. Hence, there is no way to calibrate the
prediction set by changing its size. In particular, wefoundthatthemodelisoverconfidentwhenthe
goldtokenisafunctionword: ittendstoallocate high probability to a small set of function words,
whilethetruedistributionismorevaried.

Calibration and scale. Fig. 4 presents the conformalthresholdvaluesqˆversusdesiredconfidence
(1−α),whencalibrationisperformedovertheentire validation set (without partition to entropy bins).
Asshown,forallconfidencelevels,thethresholdqˆ neededtoensurethatthecorrectwordisincluded
within the prediction set is larger than the confidence level itself (the y = x dashed line). This
indicates that the model is overconfident. Fig. 4 also shows the dependency of calibration on the
scale. Scaling language models has been shown toinducetheemergenceofnewabilities,suchas
in-contextlearning(Brownetal.,2020). Empirical powerlawswereshowntopredictperformancein
adifferenttaskasafunctionofscale(Kaplanetal.,
2020; Wei et al., 2022a), where models usually showimprovedperformancewithscale. Here,we
findinversescaling(Weietal.,2022b),wherecalibrationmoderatelydeteriorateswithmodelscale.

Generation. Howdoesconformalpsamplingaffectgeneration? weusethe350Mmodeltocom-
parethequalityofgenerationofconformalpsamplingwiththenaturalbaselineofpsampling. We
generate continuations to 1,000 prompts of size
35 words from the OpenWebText dataset 2. We generateuptolength200tokens,andcomparecon-
formal p = 0.9 prediction (setting 1−α = 0.9) with conventional p = 0.9 sampling.3 Following
Fig.3,whenapplyingourmethod,wecalculatethe

entropyoftheoutputdistributionovereachtoken, anddynamicallysetthethresholdpforeachtoken
prediction,accordingtothethresholdvalueqˆthat fits this entropy percentile. This ensures that the
trueprobabilityofthetokentobeincludedwithin thepredictionset(accordingtothetrainingsetused
forcalibration)is0.9.

Weevaluatethequalityofthegenerationusing
MAUVE (Pillutla et al., 2021) and BERTScore
(Zhang et al., 2019).4 MAUVE score is 0.933 for conformal-p sampling, and 0.0.920 for con-
ventionalpsampling. AsforBERTScore,theF1 scoreis0.840forconformal-psampling,and0.843
forconventionalpsampling. Theseresultsindicate thatconformal-psamplingisperformingsimilarly
toconventionalpsampling.

ApplicabilityofCPtononIIDdata Conformal predictiontheoryassumesIID,whilewebuildon
the model outputs distributions over consecutive tokensinthesamesentence, whichare ofcourse
highlydependent. Werepeatedtheper-entropy-bin calibrationprocesswhenuniformlysamplingasin-
gletokenpersentence,thus(almost)satisfyingthe independenceassumption. Theresultsweresimilar
toFig.3andinthatcase,Eq.(3))isapplicable.

# 4 Conclusions
Toconclude,inthisstudyweapplythenotionof calibrationbyconformalpredictiontocalibratethe
top-p nucleus sampling as a function of the next worddistributionentropyandthusmadethetop-p
decodingpolicyconsistent. Thesameanalysisand

2https://github.com/jcpeterson/openwebtext
3Wemakethegenerationsavailableatthislink.
4DefaultHuggingFacev4.22.0Parameterswereused.

calibrationcanalsobeappliedtoothercommonly used decoding methods, such as variants of top-
p (Meister et al., 2022) and truncation sampling
(Hewittetal.,2022).

## Limitations
WecalibratedOPTmodelsbasedonWikipedia data. Futureworkshouldapplycalibrationproce-
duretoawiderrangeofdatasets,tocheckwhether ourresultsgeneralizetodifferentdomains. Addi-
tionally,welimitedourevaluationtoentropyasa measure of uncertainty and did not explore other
measures. Finally,weaimedatvalidatingthecalibration status of commonly used LMs. Future
workshouldthoroughlyevaluatetheimpactofthe calibrationstatusondifferentfacetsofgeneration
quality, as text generation is one of the main usecasesoflargeLMs.

## EthicsStatement
Wedonotforeseeethicalissueswiththiswork.

## Acknowledgements
ThisprojectreceivedfundingfromtheEuropoean
Research Council (ERC) under the Europoean
Union’s Horizon 2020 research and innovation programme, grant agreement No. 802774 (iEX-
TRACT). Shauli Ravfogel is grateful to be supportedbytheBloombergDataSciencePh.D.Fel-
lowship.

## References
DavidHAckley,GeoffreyEHinton,andTerrenceJSejnowski.1985. Alearningalgorithmforboltzmann
machines. Cognitivescience,9(1):147–169.

Anastasios N Angelopoulos and Stephen Bates. 2021.
A gentle introduction to conformal prediction and distribution-free uncertainty quantification. arXiv
preprintarXiv:2107.07511.

Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind
Neelakantan,PranavShyam,GirishSastry,Amanda
Askell, et al. 2020. Language models are few-shot learners. Advancesinneuralinformationprocessing
systems,33:1877–1901.

Eldan Cohen and Christopher Beck. 2019. Empirical analysisofbeamsearchperformancedegradationin
neural sequence models. In International ConferenceonMachineLearning(ICML).

AngelaFan,MikeLewis,andYannDauphin.2018. Hierarchical neural story generation. arXiv preprint
arXiv:1805.04833.

ChuanGuo,GeoffPleiss,YuSun,andKilianQWeinberger. 2017. On calibration of modern neural net-
works. In International Conference on Machine
Learning(ICML).

JohnHewitt,ChristopherDManning,andPercyLiang.
2022. Truncation sampling as language model
smoothing. In Proceedings of the Conference on
Empirical Methods in Natural Language Processing.

AriHoltzman, JanBuys, LiDu, MaxwellForbes, and
YejinChoi.2020. Thecuriouscaseofneuraltextdegeneration. In International Conference on Learn-
ingRepresentations(ICLR).

Jared Kaplan, Sam McCandlish, Tom Henighan,
TomBBrown,BenjaminChess,RewonChild,Scott
Gray,AlecRadford,JeffreyWu,andDarioAmodei.
2020. Scaling laws for neural language models.
arXivpreprintarXiv:2001.08361.

Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky.2018. Sharpnearby,fuzzyfaraway: Howneu-
rallanguagemodelsusecontext. InProceedingsof theAnnualMeetingoftheAssociationforComputa-
tionalLinguistics.

Christopher Manning and Hinrich Schutze. 1999.
Foundationsofstatisticalnaturallanguageprocessing. MITpress.

Clara Meister, Tiago Pimentel, Gian Wiher, and
Ryan Cotterell. 2022. Typical decoding for natural language generation. arXiv preprint arXiv:
2202.00666.

Roberto I Oliveira, Paulo Orenstein, Thiago Ramos, and João Vitor Romano. 2022. Split conformal
prediction for dependent data. arXiv preprint arXiv:2203.15885.

KrishnaPillutla,SwabhaSwayamdipta,RowanZellers,
JohnThickstun,SeanWelleck,YejinChoi,andZaid
Harchaoui. 2021. Mauve: Measuring the gap between neural text and human text using divergence
frontiers. Advances in Neural Information ProcessingSystems,34:4816–4828.

Yaniv Romano, Matteo Sesia, and Emmanuel Candes.
2020. Classification with valid and adaptive cover-
age. Advances in Neural Information Processing
Systems.

GlennShaferandVladimirVovk.2008. Atutorialon conformalprediction. JournalofMachineLearning
Research,9(3).

Vladimir Vovk, Alexander Gammerman, and Glenn
Shafer. 2005. Algorithmic learning in a random world. SpringerScience&BusinessMedia.

Volodya Vovk, Alexander Gammerman, and Craig
Saunders. 1999. Machine-learning applications of algorithmic randomness. In International Confer-
enceonMachineLearning.

Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel,
Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
MaartenBosma,DennyZhou,DonaldMetzler,etal.
2022a. Emergentabilitiesoflargelanguagemodels.
arXivpreprintarXiv:2206.07682.

Jason Wei, Yi Tay, and Quoc V Le. 2022b. Inverse scaling can become u-shaped. arXiv preprint
arXiv:2211.02011.

Susan Zhang, Stephen Roller, Naman Goyal, Mikel
Artetxe,MoyaChen,ShuohuiChen,ChristopherDewan, Mona Diab, Xian Li, Xi Victoria Lin, et al.
2022. Opt: Open pre-trained transformer language
models. arXivpreprintarXiv:2205.01068.

Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q
Weinberger,andYoavArtzi.2019. Bertscore: Evaluating text generation with bert. arXiv preprint
arXiv:1904.09675.