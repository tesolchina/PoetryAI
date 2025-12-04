---
source_pdf: Analysis_of_Consistency_of_Large_Language_Models_for_Low-Resource_Languages_like_Turkish_with_Min-P_and_Top-P_Sampling_Parameters.pdf
converted_date: 2025-12-04T11:38:34.190022
total_pages: 4
model: Google Gemini 2.5 Flash
total_cost_usd: $0.022086
prompt_tokens: 8,144
completion_tokens: 7,857
---

Türkçe gibi Az Kaynaklı Diller için Büyük Dil Modeli Tutarlılıg˘ının Min-P ve Top-P Örnekleme Parametreleri ile Analizi
Analysis of Consistency of Large Language Models for Low-Resource Languages like Turkish with Min-P and Top-P Sampling Parameters

Taha Üzümcü
VeriUs Teknoloji
Marmara Üniversitesi taha.uzumcu@verius.com.tr

Murat Can Ganiz
VeriUs Teknoloji
Marmara Üniversitesi murat.ganiz@verius.com.tr

Özetçe —Büyük Dil Modelleri (BDM), yüksek sıcaklık parametrelerinde örnekleme yaparken Türkçe gibi az kaynaklı dillerde dil tutarlılıg˘ını korumakta zorlanmaktadır. Bu çalıs¸mada, yakın zamanda tanıtılan ve düs¸ük olasılıklı kelimeleri (token) filtreleyen min-p ve top-p parametre deg˘erlerinin, ag˘ırlıklı olarak I˙ngilizce eg˘itimi almıs¸ açık kaynak BDM’lerde Türkçe metin üretimi üzerindeki etkisi incelenmis¸tir. Min-p’nin Türkçe tutarlılıg˘ını farklı sıcaklık ve top-p ayarlarında koruma etkinlig˘i, Yüksek Mahkeme karar özetleri kullanılarak deg˘erlendirilmis¸tir. Ayrıntılı deneyler sonucunda, min-p örneklemesinin yüksek sıcaklıklarda dilsel tutarlılıg˘ı önemli ölçüde artırdıg˘ı ve tutarlılıktan ödün vermeden daha fazla yaratıcılıg˘a olanak tanıdıg˘ı gözlemlenmis¸tir.

Anahtar Kelimeler—Büyük Dil Modelleri, Az Kaynaklı Diller, Türkçe Metin Üretimi, Sıcaklık Örneklemesi, Min-P, Top-P, Örnekleme Stratejileri

Abstract—Large Language Models (LLMs) struggle to maintain language consistency in low-resource languages like Turkish when sampling at high temperature parameters. This study investigates the effects of recently introduced min-p and top-p parameter values, which filter low-probability tokens, on Turkish text generation in open-source LLMs trained predominantly on English. The effectiveness of min-p in maintaining Turkish consistency across different temperature and top-p settings is evaluated using Supreme Court decision summaries. Detailed experiments demonstrate that min-p sampling significantly increases linguistic consistency at high temperatures and allows for greater creativity without compromising consistency.

Keywords—Large Language Models, Low-Resource Languages, Turkish Text Generation, Temperature Sampling, Min-P, Top-P, Sampling Strategies

# I. GIRIS¸

Büyük dil modelleri (BDM) metin üretme konusunda olag˘anüstü performans göstermektedir ancak bu modellerin az kaynaklı dillerdeki performanslarında çes¸itli sorunlar bulunmaktadır [1]. Bu sorunlardan biri örnekleme stratejileri ile ilgilidir. Sıcaklık, BDM çıktılarındaki rastgelelik veya "yaratıcılık" seviyesini kontrol eden bir örnekleme parametresidir [2]. Bu parametre, metin üretiminde kelime (token) seçimi sırasında olasılık dag˘ılımını etkiler. Sıcaklık deg˘erinin artması, modelin daha çes¸itli ve zengin içerik üretmesini sag˘larken, aynı zamanda hatalara da yol açabilir [3]. Model daha az olası kelimeleri seçtikçe dil bilgisi hataları, tuhaf ifadeler ve söz dizimsel hataların olasılıg˘ı artar [2].

Bu durum, ana amacı I˙ngilizce metin üretme olarak eg˘itilmis¸ ancak eg˘itim kümesinde daha az miktarlarda bas¸ka dillerden de metinler içeren LLama, Gemma gibi açık kaynak BDM’lerde I˙ngilizce dıs¸ı metin üretmede farklı sorunlara yol açmaktadır. Daha ayrıntılı olarak, yüksek sıcaklık deg˘erleri, bu tarz açık kaynak BDM’lerin Türkçe gibi az kaynaklı dillerde metin üretirken I˙ngilizce veya dig˘er dillerden kelimeler yerles¸tirme eg˘ilimini artırmaktadır [4].

BDM’ler genellikle I˙ngilizce ag˘ırlıklı verikümeleriyle eg˘itilir. Bu nedenle, Türkçe gibi dillerin token dag˘ılımları, modelin dahili temsilinde daha düs¸ük olasılıklara sahiptir. Yüksek sıcaklık, daha az yaygın tokenların seçilmesini tes¸vik etse de, I˙ngilizce’nin veri fazlalıg˘ı bu etkiyi bastırabilir. Yüksek sıcaklık ayarlarında, modeller Türkçe gibi az kaynaklı dillerin düs¸ük olasılıklı kelimelerini üretmektense, araya baskın dilin düs¸ük olasılıklı kelimelerini koyabildig˘i gözlemlenmis¸tir [4]. Sıcaklık arttıkça, model dil sınırlarını koruma yeteneg˘ini kaybeder. Öte yandan diller arasındaki sınırlar alana göre mug˘lak olabilir. Örneg˘in, özellikle bilgisayar bilimleri gibi teknik alanlardaki Türkçe metinlerde birçok I˙ngilizce kelime geçmektedir. Bu tür metinler eg˘itim kümelerinde yer aldıklarında modelin Türkçe metin üretimi içinde I˙ngilizce kelime üretme davranıs¸ını ög˘renmesine yol açabilir. Bu sorunu çözmek için çes¸itli yöntemler önerilebilir. Model, Türkçe metin üretiminde düs¸ük sıcaklık deg˘erleri ile kullanılabilir ancak bu, özellikle yaratıcı yazma gerektiren uygulamalarda modelin farklı metinler üretmesini kısıtlayacaktır. Bir bas¸ka çözüm yöntemi olarak modeller sadece Türkçe metinlerle ince ayarlama eg˘itimine tabi tutulabilir. Bu durumda ise özellikle on milyarlarca hatta yüz milyarlarca parametreye sahip BDM’lerde modelin yüksek sıcaklıklardaki davranıs¸ını deg˘is¸tirebilmek için çok büyük miktarlarda veri gereklilig˘i ve bununla bag˘lantılı çok pahalı hesaplama kaynakları ihtiyacı önemli bir sorun olus¸turmaktadır.

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
Authorized licensed use limited to: Hong Kong Baptist University. Downloaded on October 10,2025 at 09:27:37 UTC from IEEE Xplore. Restrictions apply.

Bu çalıs¸mada Türkçe bag˘lamında, daha özel olarak Türkçe metin özetleme için metin üretimi bag˘lamında dil dıs¸ı kelime hatalarını analiz etmek ve azaltmak için min-p ve top-p örnekleme parametreleri incelenmis¸tir. Top-k ve top-p gibi geleneksel örnekleme yaklas¸ımlarının aksine, min-p düs¸ük olasılıklı kelimeleri dinamik bir s¸ekilde elimine eder. Bu sayede çes¸itlilig˘i ve yaratıcılıg˘ı korurken, dil dıs¸ı kelimelerin örneklenmesini engeller [3]. Çalıs¸mada min-p parametresinin etkisinin deg˘erlendirilmesi için Türkçe Yargıtay kararlarından ve özetlerinden olus¸an metinler kullanılmıs¸tır. Bu veri kümesi Türkçe’nin zorluklarına ek olarak, içerisinde hukuk alanına özel, günlük Türkçede çok nadir kullanılan kelimeleri barındırdıg˘ından ve özetler metin uzunlug˘una kıyasla çok kısa oldug˘undan metin üretiminin ög˘renilmesi açısından önemli zorluklar içermektedir.

Ana katkılar s¸u s¸ekilde özetlenebilir:
* Sıcaklık, top-p ve min-p deg˘erlerinin Türkçe metin üretiminde dil dıs¸ı kelime üretimi sorunu bag˘lamında sistematik bir s¸ekilde incelenmesi yapılmıs¸tır.
* Min-p yaklas¸ımının Türkçe metin üretiminde kararlılıg˘ı arttırma etkisi analiz edilmis¸tir.
* Farklı örnekleme ayarları ile modelin yapmıs¸ oldug˘u hata tiplerini ortaya konmus¸tur.

# II. ALAKALI ÇALIS¸MALAR

Meta firması tarafından gelis¸tirilen LlaMa 3 açık kaynak BDM ailesi özellikle 405 milyar parametreye kadar çıkan modelleri ile kendisini dig˘er model ailelerinden ayırır. 128 bin kelimeye (token) kadar bag˘lam penceresi vardır. Bu çalıs¸mada sırasıyla 3 milyar ve 8 milyar parametreli LlaMa-3.2-3B ve LlaMa-3.1-8B modelleri kullanılmıs¸tır. Önemli bir not olarak LlaMa dil modeli ailesinin I˙ngilizce dıs¸ında 7 dili destekledig˘i belirtilmis¸tir. Fakat bu diller arasında Türkçe yoktur [5].

Microsoft Phi-4, ise 14 milyar parametreli bir dil modelidir. 16 bin kelimeye (token) kadar bag˘lam penceresi vardır. Eg˘itim kümesi içerisinde ki dillerin deg˘erlendirilmesinde fastText [6] kullanılmıs¸ ve 176 adet dil tespit edilmis¸tir. Benzer s¸ekilde Türkçe resmi olarak listelenen dillerin arasında deg˘ildir [7].

Sıcaklık parametresi örnekleme alanında çes¸itlilig˘i arttırmak için sıkça kullanılan yöntemlerden bir tanesidir. Düs¸ük sıcaklık deg˘erlerinde model daha kesin cevaplar verme eg˘ilimindeyken, yüksek sıcaklıklarda kelime (token) çes¸itlilig˘i artmaktadır. Ancak bu çes¸itlik modelin kararlılıg˘ını düs¸ürmektedir. [3], [8].

Top-k örnekleme yöntemi BDM modelinin seçimlerini olasılıg˘ı en yüksek olan k seçenek ile sınırlandırmakta, ve düs¸ük olasılıkla çıktıları elemektedir. Nucleus (top-p) yöntemi ise, dinamik olarak kümülatif s¸ekilde en yüksekten en düs¸ük olasılıg˘a dog˘ru toplar ve belli bir es¸ig˘in altında kalan tokenları elimine eder. Bu iki yöntemde metinin akıcılıg˘ı iyi yönde etkilese de, dil dıs¸ı tokenların örneklenmesini tam anlamıyla önlemez [8].

Min-p örnekleme, düs¸ük olasılıklı tokenları en yüksek olasılıklı tokenın deg˘erine göre ölçekleyip ayıklar. Yapılan aras¸tırmalarda Min-p yönteminin dil içi karalılıg˘ını etkisi incelenmis¸tir [3]. Bu çalıs¸mada ise bu üst parametrelerin Türkçe metin üretimindeki tutarlılıg˘a olan etkisi incelenmektedir.

Çok dilli modeller genellikle az kaynaklı dillerde veri kıtlıg˘ı ve dengesiz eg˘itimden kaynaklı zorluk çekmektedirler [1]. Bu modeller özellikte yüksek sıcaklıklarda, kararsız kaldıklarında yüksek-kaynaklı dillerin kelimelerinden örnekleme yapmaktadırlar. Var olan aras¸tırmalar bu problemin inceayarlama ve pekis¸tirmeli-ög˘renme yöntemleri ile performans artıs¸ını incelemis¸lerdir [9], [10].

Az kaynak modelleri inceleyen bir çalıs¸mada, tek dilli soru cevaplarda, en gelis¸mis¸ BDM’lerin bile aynı dilde metin üretmekte zorlandıg˘ı, özellikle LlaMa ve Mistral modellerinin bu konuda zayıf oldug˘u belirtilmis¸tir [4]. Llama3 modelleri düs¸ük parametrelerde ortalama %18-%33 kararlılık sag˘larken, Mistral Modelleri %70-%90 arası kararlılık sag˘lamaktadır.

Dil karıs¸ıklıg˘ının niceliksel olarak ölçmek için Dil Karıs¸ıklık Kıyası (Language Confusion Benchmark) gelis¸tirilmis¸tir [4]. Bu kıyas, model cevaplarının hem satır (LPR) hem de kelime düzeyinde (WPR) ölçülmesini hedefler. Bu metrikleri kullanarak BDM çıktılarının istenilen dilde cevap verip vermedig˘i niceliksel olarak ölçülebilmektedir. Testler dıs¸ında yazarlar aynı zamanda bu problemin önlenmesini de aras¸tırmaktalar. Tek dil testinde birkaç az örnek (few-shot) yönteminin büyük oranda sorunu azalttıg˘ı, aynı zamanda hedef dil veri kümeleri ile ince-ayarlama ve tercih-ayarlaması eg˘itimleri yapmanın modeli istenilen dilde daha iyi hizalandıg˘ını gözlemlemis¸lerdir. Bu yöntemlerin problemi kısmen çözdüg˘ü ve en güçlü GPT-4 gibi modellerin bile ara sıra hata yaptıg˘ını ve bu problemin hala gelis¸tirmeye açık oldug˘u not edilmis¸tir [4].

# III. YÖNTEM

Bu çalıs¸mada Yargıtay içtihatları ve bunların kısa özetlerini içeren bir veri kümesi kullanılmıs¸tır. Bu veri kümesi 290 içtihat ve özet ikilisinden olus¸maktadır. Veri kümesi hukuki terminoloji ve nadir kelime kullanımı nedeniyle BDM’ler için zorluklar sunmaktadır. I˙çtihat özetleri içtihat metnine kıyasla oldukça kısadır ve gerek dil kullanımı gerekse kelimeler itibariyle genel içtihat metninden farklılık göstermektedir. Bu açıdan bu çalıs¸mamızda odaklandıg˘ımız sorunlar açısından ideal bir veri kümesi olarak deg˘erlendirilmektedir çünkü metin içinden birebir cümleler ve kelimeler ile bu özetin üretilmesi oldukça zordur.

Bu çalıs¸ma için Türkiye’de gerek endüstri gerekse akademide yaygın olarak kullanılan, resmi olarak Türkçe desteklemeyen ama Türkçe metin üretimi kabiliyeti olan LLaMa ve Phi ailesi açık kaynak modeller seçilmis¸tir. Bu modeller kullanılarak toplamda 400’den fazla deney yapılmıs¸tır. LlaMa 3 milyar parametreli model Türkçe metin üretimi açısından son derece zayıf oldug˘u, Phi 14 milyar parametreli model ise deney sürelerini uzattıg˘ı ve bag˘lam uzunlug˘u göreceli olarak az oldug˘u için sadece LlaMa 8 milyarlık model üzerinden ilerlenmis¸tir. Temel olarak sıcaklık, top-p ve min-p olmak üzere üç farklı örnekleme üst parametresi incelenmis¸tir (TABLO II: Örnekleme Üst Parametreleri ve Aralıkları).

Authorized licensed use limited to: Hong Kong Baptist University. Downloaded on October 10,2025 at 09:27:37 UTC from IEEE Xplore. Restrictions apply.

| Model | Boyut | Bag˘lam | Firma | Çıkıs¸ |
| :---------- | :---- | :------- | :------ | :------- |
| Microsoft Phi-4 | 14B | 16K | Microsoft | Aralık 2024 |
| Meta LLaMA-3.2-3B | 3B | 128K | Meta | Eylül 2024 |
| Meta LLaMA-3.1-8B | 8B | 128K | Meta | Temmuz 2024 |

TABLO I: Modeller

| Parametre | Min | Max | Açıklama |
| :---------- | :-- | :-- | :-------------------------------- |
| Sıcaklık | 0.3 | 4.0 | Olasılık dag˘ılımını kontrol eder |
| Top-p | 0.4 | 1.0 | Kümülatif olarak olasılıkları sınırlar |
| Min-p | 0.0 | 0.4 | Düs¸ük olasılıklı tokenları elimine eder |

TABLO II: Örnekleme Parametreleri ve Aralıkları

![S¸ekil 2: Dil Dıs¸ı Token Ekleme](image_placeholder_for_figure_2)
S¸ekil 2: Dil Dıs¸ı Token Ekleme

Modeller (TABLO I: Modeller) vLLM [11], kütüphanesi ile çalıs¸tırılmıs¸tır. Deg˘erlendirme için özetleme literatüründe sık kullanılan ROUGE-1, ROUGE-2, ve ROUGE-L puanları kullanılmıs¸tır. ROUGE (Recall-Oriented Understudy for Gisting Evaluation) puanı, kelime sekanslarından parametresi ile farklı büyüklüklerden -gram örtüs¸melerini ölçen, ve L parametresi ile en uzun örtüs¸en alt dizinleri hesaplayan bir ölçüttür [12].

ROUGE puanı dıs¸ında aynı zamanda Dil Karmas¸ıklık Kıyası (Language Confusion Benchmark - LCB) incelenmis¸tir [4]. Bu kıyasta Line-level Pass Rate (LPR) satır bazında dilin hedef dil olup olmadıg˘ını kontrol ederken, Word-level Pass Rate (WPR) satırın içerisindeki kelimelerin Türkçe olup olmadıg˘ını kontrol etmekte ve hata oranlarını hesaplamaktadır. LPR puanı Türkçe bir cümle içerisindeki az sayıda farklı dilden kelime olsa dahi çog˘unluk Türkçe kelimelerden olus¸uyorsa olumlu sonuç vermektedir. WPR puanı ise kelime bazında olup Türkçe desteklememektedir. WPR puanı hesaplamaya Türkçe desteg˘i eklemek için temel bir Türkçe kelime listesine ilave olarak içtihatlardan çıkartılan kelimeler, özel isimler ayıklandıktan sonra FPS5 [13], [14] kök bulma fonksiyonundan geçirilerek elde edilen kelime listesi kullanılmıs¸tır.

# IV. BULGULAR VE TARTIS¸MA

Yapılan Deneyler modellerin üç ana s¸ekilde bozuldug˘unu ortaya koymaktadır.

1) Küçük Yazım Hataları – Küçük yazım hataları veya dil bilgisi tutarsızlıkları (Bkz. S¸ekil 1).
2) Dil Dıs¸ı Token Ekleme – Bazı kelimeler farklı dilde geçmektedir ancak çevrildig˘inde dog˘ru anlamını korumaktadır (Bkz. S¸ekil 2).
3) Anlamsız Token Çıktısı – Anlamsız karakterler vermektedir (Bkz. S¸ekil 3).

![S¸ekil 3: Anlamsız Token Çıktısı](image_placeholder_for_figure_3)
S¸ekil 3: Anlamsız Token Çıktısı

IV numaralı tabloda, 0.7 Sıcaklık deg˘eri itibariyle üretilen metnin Türkçesinin bozulmaya bas¸ladıg˘ı görülmektedir, Buradaki bozulmalar, genellikle küçük yazım hataları ve nadir dil dıs¸ı token ekleme s¸eklinde olmaktadır. III numaralı tablonun aksine, burada ki ufak top-p ve min-p deg˘erleri modelin performansını düzeltmektedir.

Sıcaklık 1’e geldig˘inde (Tablo V), model anlamsız metin üretmeye bas¸lamıs¸tır. Top-p ve min-p deg˘erleri hala bu bozulmanın önüne geçebildig˘i gözlemlenmis¸tir.

Sıcaklık 1.5’e çıktıg˘ında (Tablo VI), top-p ve min-p deg˘erleri tek bas¸larına kullanıldıg˘ında modelin anlamsız token çıktısı vermesini önlemekte, ancak küçük yazım hataları ve dil dıs¸ı token ekleme devam etmektedir. Model performansının düzelmesi için top-p ve min-p’nin birlikte kullanılması gerekmektedir.

Sıcaklık 1.75’e çıktıg˘ında (Tablo VII), top-p ve min-p birlikte kullanılmasına rag˘men model performansının düzelmedig˘i gözlemlenmis¸tir.

Sıcaklık 1.75’ten (Tablo VII) sonra model bas¸arımı düs¸meye devam etmektedir. Sıcaklık 3’e (Tablo VIII) geldig˘inde ise örnekleme parametrelerinden bag˘ımsız model anlamsız token çıktısı vermektedir.

![S¸ekil 1: Küçük Yazım Hataları](image_placeholder_for_figure_1)
S¸ekil 1: Küçük Yazım Hataları

# V. SONUÇ

Türkçe metin üretiminde, ince ayarlama gibi maliyetlere katlanmadan, açık kaynak BDM’lerin yüksek sıcaklık deg˘erlerinde, amaçlanan dil dıs¸ı token üretimi sorununun min-p ve top-p parametre deg˘erinin ayarlanarak 1.5 sıcaklıg˘ına kadar tamamen, 2.5 sıcaklıg˘ına kadar kısmen kontrol altına alınabildig˘ini görülmektedir.

WPR ag˘ırlıklı olarak kaynak derleme (örn. Hukuk) bag˘lı oldug˘undan, WPR bozuk kelimeler dıs¸ında aynı zamanda alan dıs¸ı kelimelere hassas hale gelmis¸tir. Dolayısıyla düs¸ük WPR deg˘erleri modelin tamamen bozulmaya ug˘radıg˘ına is¸aret etmeyebilir. Örneg˘in, 290 karar özeti için yaklas¸ık 28 bin kelime üreten bir modelin (Sıcaklık 2.5, Top-p 0.4, Min-p 0.2) almıs¸ oldug˘u 0.1 WPR puanı incelendig˘inde, gerçekten hatalı olarak bulunan 26 kelime s¸u s¸ekildedir: processindeki, argumentü, yukaridaki, mikroforu, however, feshte, someone, niteliikli, aboniye, incceledi, absence, feraat, muvaza, avukatinin, dosalarla, etti"nin, reasonlar, case, tebligname, management, tesbelliinin, kanunu"un, iddiastan, davinin, companies, argumentleri.

| Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L |
| :---- | :---- | :-- | :-- | :-- | :-- | :-- |
| N/A | N/A | 0.67 | 1.00 | 0.32 | 0.17 | 0.23 |
| 0.8 | N/A | 0.66 | 1.00 | 0.32 | 0.17 | 0.23 |
| N/A | 0.1 | 0.68 | 1.00 | 0.32 | 0.17 | 0.23 |
| 0.8 | 0.1 | 0.67 | 1.00 | 0.33 | 0.18 | 0.23 |

TABLO III: Sıcaklık 0.3 için top-p, min-p deg˘erlerine kars¸ılık gelen deg˘erlendirme ölçütleri

| Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L |
| :---- | :---- | :-- | :-- | :-- | :-- | :-- |
| N/A | N/A | 0.53 | 1.00 | 0.31 | 0.14 | 0.20 |
| 0.8 | N/A | 0.66 | 1.00 | 0.32 | 0.16 | 0.22 |
| N/A | 0.1 | 0.68 | 0.99 | 0.15 | 0.21 | 0.11 |
| 0.8 | 0.1 | 0.70 | 1.00 | 0.32 | 0.17 | 0.22 |

TABLO IV: Sıcaklık 0.7 top-p, min-p deg˘erlerine kars¸ılık gelen deg˘erlendirme ölçütleri

| Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L |
| :---- | :---- | :-- | :-- | :-- | :-- | :-- |
| N/A | N/A | 0.01 | 0.34 | 0.14 | 0.04 | 0.08 |
| 0.6 | N/A | 0.66 | 1.00 | 0.31 | 0.15 | 0.21 |
| 0.4 | N/A | 0.69 | 1.00 | 0.32 | 0.17 | 0.22 |
| N/A | 0.1 | 0.60 | 1.00 | 0.30 | 0.14 | 0.20 |
| N/A | 0.2 | 0.68 | 1.00 | 0.32 | 0.16 | 0.22 |
| 0.6 | 0.2 | 0.64 | 1.00 | 0.32 | 0.17 | 0.22 |

TABLO V: Sıcaklık 1.0 top-p, min-p deg˘erlerine kars¸ılık gelen deg˘erlendirme ölçütleri

| Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L |
| :---- | :---- | :-- | :-- | :-- | :-- | :-- |
| N/A | N/A | 0.00 | 0.00 | 0.03 | 0.00 | 0.02 |
| 0.6 | N/A | 0.00 | 0.00 | 0.02 | 0.00 | 0.01 |
| 0.4 | N/A | 0.00 | 0.08 | 0.08 | 0.01 | 0.04 |
| N/A | 0.1 | 0.33 | 1.00 | 0.28 | 0.11 | 0.17 |
| N/A | 0.2 | 0.54 | 1.00 | 0.31 | 0.14 | 0.20 |
| 0.6 | 0.2 | 0.39 | 0.99 | 0.28 | 0.11 | 0.17 |
| 0.4 | 0.2 | 0.56 | 0.99 | 0.31 | 0.14 | 0.20 |

TABLO VI: Sıcaklık 1.50

| Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L |
| :---- | :---- | :-- | :-- | :-- | :-- | :-- |
| N/A | N/A | 0.00 | 0.00 | 0.03 | 0.00 | 0.02 |
| 0.4 | N/A | 0.00 | 0.00 | 0.04 | 0.00 | 0.02 |
| N/A | 0.1 | 0.21 | 1.00 | 0.26 | 0.08 | 0.15 |
| N/A | 0.2 | 0.44 | 1.00 | 0.29 | 0.12 | 0.18 |
| 0.6 | 0.2 | 0.47 | 1.00 | 0.29 | 0.12 | 0.18 |
| 0.4 | 0.2 | 0.47 | 1.00 | 0.28 | 0.11 | 0.18 |

TABLO VII: Sıcaklık 1.75

| Top-P | Min-P | WPR | LPR | R-1 | R-2 | R-L |
| :---- | :---- | :-- | :-- | :-- | :-- | :-- |
| N/A | 0.1 | 0.00 | 0.05 | 0.06 | 0.00 | 0.03 |
| N/A | 0.2 | 0.02 | 0.97 | 0.19 | 0.03 | 0.10 |
| 0.4 | 0.2 | 0.02 | 0.96 | 0.20 | 0.03 | 0.11 |

TABLO VIII: Sıcaklık 3

# TES¸EKKÜR

Bu çalıs¸ma TÜB˙ITAK TEYDEB 3231058 numaralı proje ile kısmi olarak desteklenmis¸tir.

# KAYNAKLAR

[1] S. Cahyawijaya, "LLM for Everyone: Representing the Underrepresented in Large Language Models", *arXiv preprint arXiv:2409.13897*, 2024.
[2] M. Peeperkorn, T. Kouwenhoven, D. Brown, and A. Jordanous, "Is Temperature the Creativity Parameter of Large Language Models?", *arXiv preprint arXiv:2405.00492*, 2024. [Online]. Available: https://arxiv.org/abs/2405.00492
[3] M. Nguyen, A. Baker, C. Neo, A. Roush, A. Kirsch, R. Shwartz-Ziv, "Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs", *arXiv preprint arXiv:2407.01082*, 2024.
[4] K. Marchisio, W.-Y. Ko, A. Bérard, T. Dehaze, S. Ruder, "Understanding and Mitigating Language Confusion in LLMs", *arXiv preprint arXiv:2406.20052*, 2024.
[5] A. Grattafiori, A. Dubey, A. Jauhri, et al., "The Llama3 Herd of Models", *arXiv preprint arXiv:2407.21783*, 2024.
[6] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, "Bag of Tricks for Efficient Text Classification", *arXiv preprint arXiv:1607.01759*, 2016.
[7] M. Abdin, J. Aneja, H. Behl, et al., "Phi-4 Technical Report", *arXiv preprint arXiv:2412.08905*, 2024.
[8] A. Holtzman, J. Buys, L. Du, M. Forbes, Y. Choi, "The Curious Case of Neural Text Degeneration", ICLR, 2020.
[9] O. Khade, S. Jagdale, A. Phaltankar, G. Takalikar, R. Joshi, "Challenges in Adapting Multilingual LLMs to Low-Resource Languages using LoRA PEFT Tuning", *arXiv preprint arXiv:2411.18571*, 2024.
[10] H. Zhang, M. Liu, C. Li, Y. Chen, J. Xu, M. Zhou, "A Reinforcement Learning Approach to Improve Low-Resource Machine Translation Leveraging Domain Monolingual Data", LREC-COLING, 2024.
[11] W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, I. Stoica, "Efficient Memory Management for Large Language Model Serving with Paged Attention", ACMSIGOPS, 2023.
[12] C.-Y. Lin, "ROUGE: A Package for Automatic Evaluation of Summaries", Text Summarization Branches Out, ACL, 2004.
[13] F. Can, S. Kocberber, E. Balcik, C. Kaynak, H. C. Ocalan, and O. M. Vursavas, "Information retrieval on Turkish texts", *Journal of the American Society for Information Science and Technology*, vol. 59, no. 3, pp. 407–421, 2008.
[14] D. Torunog˘lu, E. Çakırman, M. C. Ganiz, S. Akyokus¸, and M. Z. Gürbüz, "Analysis of preprocessing methods on classification of Turkish texts", in *Proc. 2011 International Symposium on Innovations in Intelligent Systems and Applications*, pp. 112–117, 2011.

Authorized licensed use limited to: Hong Kong Baptist University. Downloaded on October 10,2025 at 09:27:37 UTC from IEEE Xplore. Restrictions apply.