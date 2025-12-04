---
source_pdf: Uzumcu_2025_Turkish_LLM_Parameters.pdf
converted_date: 2025-12-04T20:35:04.025651
total_pages: 4
model: Google Gemini 2.0 Flash
total_cost_usd: $0.003896
prompt_tokens: 8,144
completion_tokens: 7,704
---

# Türkçe gibi Az Kaynaklı Diller için Büyük Dil
Modeli Tutarlılıg˘ının Min-P ve Top-P Örnekleme
Parametreleri ile Analizi
Analysis of Consistency of Large Language Models for Low-Resource Languages like Turkish with
Min-P and Top-P Sampling Parameters
Taha Üzümcü Murat Can Ganiz
VeriUs Teknoloji VeriUs Teknoloji
Marmara Üniversitesi Marmara Üniversitesi taha.uzumcu@verius.com.tr murat.ganiz@verius.com.tr

Özetçe —Büyük Dil Modelleri (BDM), yüksek sıcaklık pa- kaynaklı dillerdeki performanslarında çes¸itli sorunlar bulunrametrelerinde örnekleme yaparken Türkçe gibi az kaynaklı maktadır [1]. Bu sorunlardan biri örnekleme stratejileri ile
dillerde diltutarlılıg˘ını korumakta zorlanmaktadır. Bu çalıs¸mada, ilgilidir. Sıcaklık, BDM çıktılarındaki rastgelelik veya "yarayakın zamanda tanıtılan ve düs¸ük olasılıklı kelimeleri (token) tıcılık" seviyesini kontrol eden bir örnekleme parametresidir
filtreleyen min-p ve top-p parametre deg˘erlerinin, ag˘ırlıklı olarak [2]. Bu parametre, metin üretiminde kelime (token) seçimi
I˙ngilizce eg˘itimi almıs¸ açık kaynak BDM’lerde Türkçe metin üre- sırasında olasılık dag˘ılımını etkiler. Sıcaklık deg˘erinin artması, timi üzerindeki etkisi incelenmis¸tir. Min-p’nin Türkçe tutarlılıg˘ını modelin daha çes¸itli ve zengin içerik üretmesini sag˘larken,
farklı sıcaklık ve top-p ayarlarında koruma etkinlig˘i, Yüksek aynı zamanda hatalara da yol açabilir [3]. Model daha az olası
Mahkeme karar özetleri kullanılarak deg˘erlendirilmis¸tir. Ayrıntılı kelimeleri seçtikçe dil bilgisi hataları, tuhaf ifadeler ve söz deneyler sonucunda, min-p örneklemesinin yüksek sıcaklıklarda dizimsel hataların olasılıg˘ı artar [2].
dilsel tutarlılıg˘ı önemli ölçüde artırdıg˘ı ve tutarlılıktan ödün Bu durum, ana amacı ˙Ingilizce metin üretme olarak eg˘ivermeden daha fazla yaratıcılıg˘a olanak tanıdıg˘ı gözlemlenmis¸tir. tilmis¸ ancak eg˘itim kümesinde daha az miktarlarda bas¸ka
dillerden de metinler içeren LLama, Gemma gibi açık kaynak
Anahtar Kelimeler—Büyük Dil Modelleri, Az Kaynaklı Diller, BDM’lerde ˙Ingilizce dıs¸ı metin üretmede farklı sorunlara yol
Türkçe Metin Üretimi, Sıcaklık Örneklemesi, Min-P, Top-P, Örnek- açmaktadır. Daha ayrıntılı olarak, yüksek sıcaklık deg˘erleri, leme Stratejileri bu tarz açık kaynak BDM’lerin Türkçe gibi az kaynaklı
dillerde metin üretirken ˙Ingilizce veya dig˘er dillerden kelimeler
Abstract—Large Language Models (LLMs) struggle to main- yerles¸tirme eg˘ilimini artırmaktadır [4].
tain language consistency in low-resource languages like Turkish when sampling at high temperature parameters. This study BDM’ler genellikle ˙Ingilizce ag˘ırlıklı veri kümeleriyle eg˘i-
investigates the effects of recently introduced min-p and top-p tilir. Bu nedenle, Türkçe gibi dillerin token dag˘ılımları, modeparameter values, which filter low-probability tokens, on Turkish lin dahili temsilinde daha düs¸ük olasılıklara sahiptir. Yüksek
text generation in open-source LLMs trained predominantly on sıcaklık, daha az yaygın tokenların seçilmesini tes¸vik etse de,
English. The effectiveness of min-p in maintaining Turkish consis- ˙Ingilizce’nin veri fazlalıg˘ı bu etkiyi bastırabilir. Yüksek sıcaktency across different temperature and top-p settings is evaluated lık ayarlarında, modeller Türkçe gibi az kaynaklı dillerin düs¸ük
using Supreme Court decision summaries. Detailed experiments olasılıklı kelimelerini üretmektense, araya baskın dilin düs¸ük demonstrate that min-p sampling significantly increases linguistic olasılıklı kelimelerini koyabildig˘i gözlemlenmis¸tir [4]. Sıcaklık
consistency at high temperatures and allows for greater creativity arttıkça, model dil sınırlarını koruma yeteneg˘ini kaybeder. Öte without compromising consistency. yandan diller arasındaki sınırlar alana göre mug˘lak olabilir.
Örneg˘in, özellikle bilgisayar bilimleri gibi teknik alanlardaki
Keywords—Large Language Models, Low-Resource Languages, Türkçe metinlerde birçok ˙Ingilizce kelime geçmektedir. Bu tür
Turkish Text Generation, Temperature Sampling, Min-P, Top-P, metinler eg˘itim kümelerinde yer aldıklarında modelin Türkçe
Sampling Strategies metin üretimi içinde ˙Ingilizce kelime üretme davranıs¸ını ög˘renmesine yol açabilir. Bu sorunu çözmek için çes¸itli yöntemler
önerilebilir. Model, Türkçe metin üretiminde düs¸ük sıcaklık
# GIRIS¸
deg˘erleri ile kullanılabilir ancak bu, özellikle yaratıcı yazma
Büyük dil modelleri (BDM) metin üretme konusunda ola- gerektiren uygulamalarda modelin farklı metinler üretmesini g˘anüstü performans göstermektedir ancak bu modellerin az
979-8-3315-6655-5/25/$31.00©2025IEEE
08021111.5202.79466UIS/9011.01
:IOD
|
EEEI
5202©
00.13$/52/5-5566-5133-8-979
|
)UIS( ecnerefnoC
snoitacilppA snoitacinummoC
dna gnissecorP
langiS dr33
5202

kısıtlayacaktır. Bir bas¸ka çözüm yöntemi olarak modeller sa- etkilese de, dil dıs¸ı tokenların örneklenmesini tam anlamıyla dece Türkçe metinlerle ince ayarlama eg˘itimine tabi tutulabilir. önlemez [8].
Bu durumda ise özellikle on milyarlarca hatta yüz milyarlarca Min-p örnekleme, düs¸ük olasılıklı tokenları en yüksek parametreye sahip BDM’lerde modelin yüksek sıcaklıklardaki olasılıklı tokenın deg˘erine göre ölçekleyip ayıklar. Yapılan
davranıs¸ını deg˘is¸tirebilmek için çok büyük miktarlarda veri ge- aras¸tırmalarda Min-p yönteminin dil içi karalılıg˘ını etkisi inreklilig˘i ve bununla bag˘lantılı çok pahalı hesaplama kaynakları celenmis¸tir [3]. Bu çalıs¸mada ise bu üst parametrelerin Türkçe
ihtiyacı önemli bir sorun olus¸turmaktadır. metin üretimindeki tutarlılıg˘a olan etkisi incelenmektedir.
Bu çalıs¸mada Türkçe bag˘lamında, daha özel olarak Türkçe Çok dilli modeller genellikle az kaynaklı dillerde veri metin özetleme için metin üretimi bag˘lamında dil dıs¸ı ke- kıtlıg˘ı ve dengesiz eg˘itimden kaynaklı zorluk çekmektedir-
lime hatalarını analiz etmek ve azaltmak için min-p ve top- ler [1]. Bu modeller özellikte yüksek sıcaklıklarda, kararsız p örnekleme parametreleri incelenmis¸tir. Top-k ve top-p gibi kaldıklarında yüksek-kaynaklı dillerin kelimelerinden örnek-
geleneksel örnekleme yaklas¸ımlarının aksine, min-p düs¸ük leme yapmaktadırlar. Var olan aras¸tırmalar bu problemin inceolasılıklı kelimeleri dinamik bir s¸ekilde elimine eder. Bu ayarlama ve pekis¸tirmeli-ög˘renme yöntemleri ile performans
sayede çes¸itlilig˘i ve yaratıcılıg˘ı korurken, dil dıs¸ı kelimelerin artıs¸ını incelemis¸lerdir [9], [10].
örneklenmesini engeller [3]. Çalıs¸mada min-p parametresinin Az kaynak modelleri inceleyen bir çalıs¸mada, tek dilli etkisinin deg˘erlendirilmesi için Türkçe Yargıtay kararlarından soru cevaplarda, en gelis¸mis¸ BDM’lerin bile aynı dilde metin
ve özetlerinden olus¸an metinler kullanılmıs¸tır. Bu veri kümesi üretmekte zorlandıg˘ı, özellikle LlaMa ve Mistral modellerinin
Türkçe’nin zorluklarına ek olarak, içerisinde hukuk alanına bu konuda zayıf oldug˘u belirtilmis¸tir [4]. Llama3 modelleri özel, günlük Türkçede çok nadir kullanılan kelimeleri ba- düs¸ük parametrelerde ortalama %18-%33 kararlılık sag˘larken,
rındırdıg˘ından ve özetler metin uzunlug˘una kıyasla çok kısa Mistral Modelleri %70-%90 arası kararlılık sag˘lamaktadır .
oldug˘undan metin üretiminin ög˘renilmesi açısından önemli Dil karıs¸ıklıg˘ının niceliksel olarak ölçmek için Dil Karıs¸ıklık zorluklar içermektedir. Kıyası (Language Confusion Benchmark) gelis¸tirilmis¸tir [4].
Ana katkılar s¸u s¸ekilde özetlenebilir: Bu kıyas, model cevaplarının hem satır (LPR) hem de kelime düzeyinde (WPR) ölçülmesini hedefler. Bu metrikleri kulla-
• Sıcaklık, top-p ve min-p deg˘erlerinin Türkçe metin narak BDM çıktılarının istenilen dilde cevap verip vermedig˘i üretiminde dil dıs¸ı kelime üretimi sorunu bag˘lamında niceliksel olarak ölçülebilmektedir. Testler dıs¸ında yazarlar
sistematik bir s¸ekilde incelenmesi yapılmıs¸tır. aynı zamanda bu problemin önlenmesini de aras¸tırmaktalar.
Tek dil testinde birkaç az örnek (few-shot) yönteminin büyük
• Min-p yaklas¸ımının Türkçe metin üretiminde kararlı- oranda sorunu azalttıg˘ı, aynı zamanda hedef dil veri kümeleri lıg˘ı arttırma etkisi analiz edilmis¸tir. ile ince-ayarlama ve tercih-ayarlaması eg˘itimleri yapmanın
modeli istenilen dilde daha iyi hizalandıg˘ını gözlemlemis¸lerdir.
• Farklı örnekleme ayarları ile modelin yapmıs¸ oldug˘u Bu yöntemlerin problemi kısmen çözdüg˘ü ve en güçlü GPT-4 hata tiplerini ortaya konmus¸tur. gibi modellerin bile ara sıra hata yaptıg˘ını ve bu problemin
hala gelis¸tirmeye açık oldug˘u not edilmis¸tir [4].

## ALAKALI ÇALIS¸MALAR
### YÖNTEM
Meta firması tarafından gelis¸tirilen LlaMa 3 açık kaynak Bu çalıs¸mada Yargıtay içtihatları ve bunların kısa özetlerini
BDM ailesi özellikle 405 milyar parametreye kadar çıkan içeren bir veri kümesi kullanılmıs¸tır. Bu veri kümesi 290 modelleri ile kendisini dig˘er model ailelerinden ayırır. 128 bin içtihat ve özet ikilisinden olus¸maktadır. Veri kümesi hukuki
kelimeye (token) kadar bag˘lam penceresi vardır. Bu çalıs¸mada terminoloji ve nadir kelime kullanımı nedeniyle BDM’ler için sırasıyla 3 milyar ve 8 milyar parametreli LlaMa-3.2-3B ve zorluklar sunmaktadır. ˙Içtihat özetleri içtihat metnine kıyasla
LlaMa-3.1-8B modelleri kullanılmıs¸tır. Önemli bir not olarak oldukça kısadır ve gerek dil kullanımı gerekse kelimeler iti-
LlaMa dil modeli ailesinin ˙Ingilizce dıs¸ında 7 dili destekledig˘i bariyle genel içtihat metninden farklılık göstermektedir. Bu belirtilmis¸tir. Fakat bu diller arasında Türkçe yoktur [5]. açıdan bu çalıs¸mamızda odaklandıg˘ımız sorunlar açısından
ideal bir veri kümesi olarak deg˘erlendirilmektedir çünkü metin
Microsoft Phi-4, ise 14 milyar parametreli bir dil modelidir. içinden birebir cümleler ve kelimeler ile bu özetin üretilmesi
16 bin kelimeye (token) kadar bag˘lam penceresi vardır. Eg˘itim oldukça zordur.
kümesi içerisinde ki dillerin deg˘erlendirilmesinde fastText [6] Bu çalıs¸ma için Türkiye’de gerek endüstri gerekse akadekullanılmıs¸ ve 176 adet dil tespit edilmis¸tir. Benzer s¸ekilde mide yaygın olarak kullanılan, resmi olarak Türkçe destek-
Türkçe resmi olarak listelenen dillerin arasında deg˘ildir [7]. lemeyen ama Türkçe metin üretimi kabiliyeti olan LLaMa
Sıcaklık parametresi örnekleme alanında çes¸itlilig˘i arttır- ve Phi ailesi açık kaynak modeller seçilmis¸tir. Bu modeller mak için sıkça kullanılan yöntemlerden bir tanesidir. Düs¸ük kullanılarak toplamda 400’den fazla deney yapılmıs¸tır. LlaMa
sıcaklık deg˘erlerinde model daha kesin cevaplar verme eg˘i- 3 milyar parametreli model Türkçe metin üretimi açısından limindeyken, yüksek sıcaklıklarda kelime (token) çes¸itlilig˘i son derece zayıf oldug˘u, Phi 14 milyar parametreli model ise
artmaktadır. Ancak bu çes¸itlik modelin kararlılıg˘ını düs¸ürmek- deney sürelerini uzattıg˘ı ve bag˘lam uzunlug˘u göreceli olarak tedir. [3], [8]. az oldug˘u için sadece LlaMa 8 milyarlık model üzerinden iler-
Top-k örnekleme yöntemi BDM modelinin seçimlerini son lenmis¸tir. Temel olarak sıcaklık, top-p ve min-p olmak üzere olasılıg˘ı en yüksek olan k seçenek ile sınırlandırmakta, ve üç farklı örnekleme üst parametresi incelenmis¸tir (TABLO II:
düs¸ük olasılıkla çıktıları elemektedir. Nucleus (top-p) yöntemi Örnekleme Üst Parametreleri ve Aralıkları).
ise, dinamik olarak kümülatif s¸ekilde en yüksekten en düs¸ük olasılıg˘a dog˘ru toplar ve belli bir es¸ig˘in altında kalan tokenları
elimine eder. Bu iki yöntemde metinin akıcılıg˘ı iyi yönde

Model Boyut Bag˘lam Firma Çıkıs¸
|:---|:---|:---|:---|:---|
MicrosoftPhi-4 | 14B | 16K | Microsoft | Aralık 2024 |
MetaLLaMA-3.2-3B | 3B | 128K | Meta | Eylül 2024 |
MetaLLaMA-3.1-8B | 8B | 128K | Meta | Temmuz 2024 |
TABLO I: Modeller

Parametre | Min | Max | Açıklama
|:---|:---|:---|:---|
Sıcaklık | 0.3 | 4.0 | Olasılık dag˘ılımını kontrol eder
Top-p | 0.4 | 1.0 | Kümülatif olarak olasılıkları sınırlar
Min-p | 0.0 | 0.4 | Düs¸ük olasılıklı tokenları elimine eder
TABLO II: Örnekleme Parametreleri ve Aralıkları

S¸ekil 2: Dil Dıs¸ı Token Ekleme

Modeller (TABLO I: Modeller) vLLM [11], kütüphanesi ile çalıs¸tırılmıs¸tır. Deg˘erlendirme için özetleme literatüründe sık
kullanılan ROUGE-1, ROUGE-2, ve ROUGE-L puanları kullanılmıs¸tır. ROUGE (Recall-Oriented Understudy for Gisting
Evaluation) puanı, kelime sekanslarından parametresi ile farklı büyüklüklerden -gram örtüs¸melerini ölçen, ve L parametresi ile
en uzun örtüs¸en alt dizinleri hesaplayan bir ölçüttür [12].
ROUGE puanı dıs¸ında aynı zamanda Dil Karmas¸ıklık Kıyası (Language Confusion Benchmark - LCB) incelenmis¸tir
[4]. Bu kıyasta Line-level Pass Rate (LPR) satır bazında dilin hedef dil olup olmadıg˘ını kontrol ederken, Word-level
Pass Rate (WPR) satırın içerisindeki kelimelerin Türkçe olup olmadıg˘ını kontrol etmekte ve hata oranlarını hesaplamaktadır.
LPR puanı Türkçe bir cümle içerisindeki az sayıda farklı dilden kelime olsa dahi çog˘unluk Türkçe kelimelerden olus¸uyorsa
olumlu sonuç vermektedir. WPR puanı ise kelime bazında olup
Türkçe desteklememektedir. WPR puanı hesaplamaya Türkçe desteg˘i eklemek için temel bir Türkçe kelime listesine ilave
olarak içtihatlardan çıkartılan kelimeler, özel isimler ayıklandıktan sonra FPS5 [13], [14] kök bulma fonksiyonundan
geçirilerek elde edilen kelime listesi kullanılmıs¸tır.

## BULGULAR VE TARTIS¸MA
Yapılan Deneyler modellerin üç ana s¸ekilde bozuldug˘unu ortaya koymaktadır.

1) Küçük Yazım Hataları – Küçük yazım hataları veya
dil bilgisi tutarsızlıkları (Bkz. S¸ekil 1).
2) Dil Dıs¸ı Token Ekleme – Bazı kelimeler farklı
dilde geçmektedir ancak çevrildig˘inde dog˘ru anlamını korumaktadır (Bkz. S¸ekil 2).
3) Anlamsız Token Çıktısı – Anlamsız karakterler ver-
mektedir (Bkz. S¸ekil 3).

S¸ekil 3: Anlamsız Token Çıktısı

IV numaralı tabloda, 0.7 Sıcaklık deg˘eri itibariyle üretilen metnin Türkçesinin bozulmaya bas¸ladıg˘ı görülmektedir, Bura-
daki bozulmalar, genellikle küçük yazım hataları ve nadir dil dıs¸ı token ekleme s¸eklinde olmaktadır. III numaralı tablonun
aksine, burada ki ufak top-p ve min-p deg˘erleri modelin performansını düzeltmektedir.

Sıcaklık 1’e geldig˘inde (Tablo V), model anlamsız metin üretmeye bas¸lamıs¸tır. Top-p ve min-p deg˘erleri hala bu bozul-
manın önüne geçebildig˘i gözlemlenmis¸tir.

Sıcaklık 1.5’e çıktıg˘ında (Tablo VI), top-p ve min-p deg˘erleri tek bas¸larına kullanıldıg˘ında modelin anlamsız token
çıktısı vermesini önlemekte, ancak küçük yazım hataları ve dil dıs¸ı token ekleme devam etmektedir. Model performansının
düzelmesi için top-p ve min-p’nin birlikte kullanılması gerekmektedir.

Sıcaklık 1.75’e çıktıg˘ında (Tablo VII), top-p ve min-p birlikte kullanılmasına rag˘men model performansının düzel-
medig˘i gözlemlenmis¸tir.

Sıcaklık 1.75’ten (Tablo VII) sonra model bas¸arımı düs¸meye devam etmektedir. Sıcaklık 3’e (Tablo VIII) geldig˘inde
ise örnekleme parametrelerinden bag˘ımsız model anlamsız token çıktısı vermektedir.

## SONUÇ
Türkçe metin üretiminde, ince ayarlama gibi maliyetlere katlanmadan, açık kaynak BDM’lerin yüksek sıcaklık deg˘er-
lerinde, amaçlanan dil dıs¸ı token üretimi sorununun minp ve top-p parametre deg˘erinin ayarlanarak 1.5 sıcaklıg˘ına
kadar tamamen, 2.5 sıcaklıg˘ına kadar kısmen kontrol altına alınabildig˘ini görülmektedir.

WPR ag˘ırlıklı olarak kaynak derleme (örn. Hukuk) bag˘lı oldug˘undan, WPR bozuk kelimeler dıs¸ında aynı zamanda
alan dıs¸ı kelimelere hassas hale gelmis¸tir. Dolayısıyla düs¸ük
WPR deg˘erleri modelin tamamen bozulmaya ug˘radıg˘ına is¸aret

Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L
|:---|:---|:---|:---|:---|:---|:---|
N/A | N/A | 0.67 | 1.00 | 0.32 | 0.17 | 0.23
0.8 | N/A | 0.66 | 1.00 | 0.32 | 0.17 | 0.23
N/A | 0.1 | 0.68 | 1.00 | 0.32 | 0.17 | 0.23
0.8 | 0.1 | 0.67 | 1.00 | 0.33 | 0.18 | 0.23
TABLO III: Sıcaklık 0.3 için top-p, min-p deg˘erlerine kars¸ılık gelen deg˘erlendirme ölçütleri

Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L
|:---|:---|:---|:---|:---|:---|:---|
N/A | N/A | 0.53 | 1.00 | 0.31 | 0.14 | 0.20
0.8 | N/A | 0.66 | 1.00 | 0.32 | 0.16 | 0.22
N/A | 0.1 | 0.68 | 0.99 | 0.15 | 0.21 | 0.11
0.8 | 0.1 | 0.70 | 1.00 | 0.32 | 0.17 | 0.22
TABLO IV: Sıcaklık 0.7 top-p, min-p deg˘erlerine kars¸ılık gelen deg˘erlendirme ölçütleri

Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L
|:---|:---|:---|:---|:---|:---|:---|
N/A | N/A | 0.01 | 0.34 | 0.14 | 0.04 | 0.08
0.6 | N/A | 0.66 | 1.00 | 0.31 | 0.15 | 0.21
0.4 | N/A | 0.69 | 1.00 | 0.32 | 0.17 | 0.22
N/A | 0.1 | 0.60 | 1.00 | 0.30 | 0.14 | 0.20
N/A | 0.2 | 0.68 | 1.00 | 0.32 | 0.16 | 0.22
0.6 | 0.2 | 0.64 | 1.00 | 0.32 | 0.17 | 0.22
TABLO V: Sıcaklık 1.0 top-p, min-p deg˘erlerine kars¸ılık gelen deg˘erlendirme ölçütleri

Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L
|:---|:---|:---|:---|:---|:---|:---|
N/A | N/A | 0.00 | 0.00 | 0.03 | 0.00 | 0.02
0.6 | N/A | 0.00 | 0.00 | 0.02 | 0.00 | 0.01
0.4 | N/A | 0.00 | 0.08 | 0.08 | 0.01 | 0.04
N/A | 0.1 | 0.33 | 1.00 | 0.28 | 0.11 | 0.17
N/A | 0.2 | 0.54 | 1.00 | 0.31 | 0.14 | 0.20
0.6 | 0.2 | 0.39 | 0.99 | 0.28 | 0.11 | 0.17
0.4 | 0.2 | 0.56 | 0.99 | 0.31 | 0.14 | 0.20
TABLO VI: Sıcaklık 1.50

Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L
|:---|:---|:---|:---|:---|:---|:---|
N/A | N/A | 0.00 | 0.00 | 0.03 | 0.00 | 0.02
0.4 | N/A | 0.00 | 0.00 | 0.04 | 0.00 | 0.02
N/A | 0.1 | 0.21 | 1.00 | 0.26 | 0.08 | 0.15
N/A | 0.2 | 0.44 | 1.00 | 0.29 | 0.12 | 0.18
0.6 | 0.2 | 0.47 | 1.00 | 0.29 | 0.12 | 0.18
0.4 | 0.2 | 0.47 | 1.00 | 0.28 | 0.11 | 0.18
TABLO VII: Sıcaklık 1.75

Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L
|:---|:---|:---|:---|:---|:---|:---|
N/A | 0.1 | 0.00 | 0.05 | 0.06 | 0.00 | 0.03
N/A | 0.2 | 0.02 | 0.97 | 0.19 | 0.03 | 0.10
0.4 | 0.2 | 0.02 | 0.96 | 0.20 | 0.03 | 0.11
TABLO VIII: Sıcaklık 3

etmeyebilir. Örneg˘in, 290 karar özeti için yaklas¸ık 28 bin kelime üreten bir modelin (Sıcaklık 2.5, Top-p 0.4, Min-p
0.2) almıs¸ oldug˘u 0.1 WPR puanı incelendig˘inde, gerçekten hatalı olarak bulunan 26 kelime s¸u s¸ekildedir: processindeki,
argumentü, yukaridaki, mikroforu, however, feshte, someone, niteliikli, aboniye, incceledi, absence, feraat, muvaza, avuka-
tinin, dosalarla, etti"nin, reasonlar, case, tebligname, management, tesbelliinin, kanunu"un, iddiastan, davinin, companies,
argumentleri.

TES¸EKKÜR
Bu çalıs¸ma TÜB˙ITAK TEYDEB 3231058 numaralı proje ile kısmi olarak desteklenmis¸tir.

KAYNAKLAR
[1] S. Cahyawijaya, "LLM for Everyone: Representing the Underrepresented in Large Language Models", *arXiv preprint arXiv:2409.13897*, 2024.
[2] M. Peeperkorn, T. Kouwenhoven, D. Brown, and A. Jordanous,
"Is Temperature the Creativity Parameter of Large Language Models?", *arXiv preprint arXiv:2405.00492*, 2024. [Online]. Available:
https://arxiv.org/abs/2405.00492
[3] M. Nguyen, A. Baker, C. Neo, A. Roush, A. Kirsch, R. Shwartz-Ziv,
"Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM
Outputs", *arXiv preprint arXiv:2407.01082*, 2024.
[4] K. Marchisio, W.-Y. Ko, A. Bérard, T. Dehaze, S. Ruder, "Understanding and Mitigating Language Confusion in LLMs", *arXiv preprint
arXiv:2406.20052*, 2024.
[5] A. Grattafiori, A. Dubey, A. Jauhri, et al., "The Llama3 Herd of Models",
*arXiv preprint arXiv:2407.21783*, 2024.
[6] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, "Bag of Tricks for
Efficient Text Classification", *arXiv preprint arXiv:1607.01759*, 2016.
[7] M. Abdin, J. Aneja, H. Behl, et al., "Phi-4 Technical Report", *arXiv preprint arXiv:2412.08905*, 2024.
[8] A. Holtzman, J. Buys, L. Du, M. Forbes, Y. Choi, "The Curious Case of Neural Text Degeneration", ICLR, 2020.
[9] O. Khade, S. Jagdale, A. Phaltankar, G. Takalikar, R. Joshi, "Challenges in Adapting Multilingual LLMs to Low-Resource Languages using
LoRA PEFT Tuning", *arXiv preprint arXiv:2411.18571*, 2024.
[10] H. Zhang, M. Liu, C. Li, Y. Chen, J. Xu, M. Zhou, "A Reinforcement
Learning Approach to Improve Low-Resource Machine Translation Leveraging Domain Monolingual Data", LREC-COLING, 2024.
[11] W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E.
Gonzalez, H. Zhang, I. Stoica, "Efficient Memory Management for Large
Language Model Serving with PagedAttention", ACMSIGOPS, 2023.
[12] C.-Y. Lin, "ROUGE: A Package for Automatic Evaluation of Summaries", Text Summarization Branches Out, ACL, 2004.
[13] F. Can, S. Kocberber, E. Balcik, C. Kaynak, H. C. Ocalan, and O.
M. Vursavas, "Information retrieval on Turkish texts", *Journal of the
American Society for Information Science and Technology*, vol. 59, no. 3, pp. 407–421, 2008.
[14] D. Torunog˘lu, E. Çakırman, M. C. Ganiz, S. Akyokus¸, and M. Z.
Gürbüz, "Analysis of preprocessing methods on classification of Turkish texts", in *Proc. 2011 International Symposium on Innovations in Intel-
ligent Systems and Applications*, pp. 112–117, 2011.