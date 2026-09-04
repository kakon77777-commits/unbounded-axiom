# 從賽馬預測到生命週期智能：AI、遺傳學、配種、育成、拍賣與馬主效用

## From Horse-Race Prediction to Lifecycle Intelligence: AI, Genetics, Breeding, Development, Auctions, and Owner Utility

**Series:** AI Game Intelligence, Randomness, and Adaptive Markets  
**Paper 04**  
**Version:** v0.1  
**Date:** 2026-09-02
**Author:** Neo.K with Aletheia（GPT-5.6 Sol）  
**Institution:** EveMissLab／一言諾科技有限公司

---

## 摘要

前一篇把賽馬視為一個共同彩池中的群體智能市場：人工智慧不只需要估計馬匹勝率，還必須理解群眾、資金流與最終價格。本篇再向前移動一層：如果 AI 不再只預測一匹「已經存在」的馬，而是介入配種、遺傳風險、幼駒選擇、育成、訓練、傷病管理、拍賣估值與退役後繁殖，那麼 AI 已不只是賽事預測器，而開始參與賽馬生命週期本身的決策。

本文將此問題寫成：

$$
\boxed{
\text{Racehorse Lifecycle Intelligence}
=
\text{Genotype}
+
\text{Pedigree}
+
\text{Phenotype}
+
\text{Development}
+
\text{Training}
+
\text{Health}
+
\text{Market}
+
\text{Owner Utility}
}
$$

其中，基因不是命運；血統不是完整基因型；拍賣價格不是競賽價值；競賽價值也不等於馬主效用。真正的生命週期決策是一個高不確定、多目標、長時間延遲而且具有強烈文化與所有權效用的問題。

現代 Thoroughbred 研究已顯示，MSTN 等基因座與最佳競賽距離、速度及早熟性具有可重複的關聯，但競賽能力整體仍是高度多基因且受環境影響的性狀。[1] 大規模基因體研究亦顯示，全球純血馬在近數十年存在顯著的基因多樣性下降與近交增加，且基因體資訊可以用來尋找較遠的 outcross、降低某些近交風險。[2] 另一項研究進一步發現，較高的 genomic inbreeding 與較低的實際出賽機率有關。[3]

這意味著未來 AI 配種不應被簡化成：

$$
\max \text{Speed}.
$$

更合理的問題是：

$$
\max_s
E\left[
U(
\text{performance},
\text{soundness},
\text{distance aptitude},
\text{fertility},
\text{market value},
\text{genetic diversity},
\text{owner preference}
)
\right].
$$

另一方面，純血馬制度本身對技術介入存在明確邊界。2026 年版 IFHA 國際規範與日本 Stud Book 規則仍要求自然交配與自然妊娠；人工授精、胚胎移植、複製與未明定的遺傳操弄所產生的後代不具備 Thoroughbred 登錄資格。[4][5] 因此，「AI 可以決定如何配」與「可以任意使用生物技術改造繁殖」是兩個完全不同的命題。

在育成端，日本 JRA 已建立從生產、營養、繁殖、運動生理、訓練、疾病到生物力學的長期研究體系；2026 年仍有研究直接分析調教內容與競賽成績、運動器疾病的關聯。[6][7] 美國的大型 wearable-sensor 研究則已在 $11,834$ 匹 Thoroughbred、 $28,481$ 次出賽中，用加速度感測與演算法風險評分辨識出極高風險小群體；最高風險級別的致命肌肉骨骼傷害概率約為最低級別的 $44.6$ 倍。[8]

拍賣端也開始正式出現機器學習估值。2026 年一篇研究使用 $5,788$ 匹 Keeneland September 一歲馬資料，機器學習模型可以解釋約 $54\%$ 的 out-of-sample 拍賣價格變異，而 sire 與 dam reputation 是重要預測因素。[9] 同年日本 Select Sale 共上場 $509$ 匹、成交 $478$ 匹，成交總額達 $33.484$ billion yen，顯示即使估值模型只改善少量決策品質，也可能對高價血統市場產生巨大經濟意義。[10]

但本文最重要的主張是：馬主不是單純的投資者。

日本 JRA 對馬主活動的制度設計本身就包括愛馬出賽時進入專屬 paddock 區、勝利後在 Winner's Circle 合影、自訂勝負服、為馬命名，以及與調教師、馬匹共同形成長期參與體驗。[11] 因此馬主效用應寫成：

$$
U_{\mathrm{owner}}
=
\alpha E[\Pi]
+
\beta V_{\mathrm{ownership}}
+
\gamma V_{\mathrm{choice}}
+
\delta V_{\mathrm{story}}
+
\epsilon V_{\mathrm{competition}}
+
\zeta V_{\mathrm{legacy}}
-
C.
$$

在這個效用函數下，AI 推薦的「數學最優馬」不必然是馬主真正想要的馬。

所以，AI 賽馬生命週期的合理終態不一定是 full automation。更可能是：

$$
\boxed{
\text{AI as Bloodstock and Lifecycle Advisor}
}
$$

即 AI 擴張觀測、風險估計與候選空間，但保留人類對配種、購買、命名、養成與長期故事的最終作者性。

---

# 1. 從「預測存在」到「參與生成」

Paper 03 的世界是：

$$
\text{Horse}
\rightarrow
\text{Race}
\rightarrow
\text{Market}.
$$

Paper 04 增加一個更早的時間軸：

$$
\text{Mating}
\rightarrow
\text{Foal}
\rightarrow
\text{Development}
\rightarrow
\text{Auction}
\rightarrow
\text{Training}
\rightarrow
\text{Race}
\rightarrow
\text{Retirement}
\rightarrow
\text{Breeding}.
$$

因此 AI 不再只是：

$$
P(Y\mid X).
$$

它開始影響：

$$
X
$$

本身將如何被生成。

這是本篇真正的理論轉折。

---

# 2. 預測型 AI 與生成型生命週期決策

賽事 AI 問：

$$
P(\text{win}\mid h).
$$

育種 AI 問：

$$
P(
\text{future phenotype}
\mid
\text{mare},
\text{stallion},
\text{environment}
).
$$

養成 AI 問：

$$
P(
\text{future performance and health}
\mid
\text{current developmental trajectory},
a_t
),
$$

其中 $a_t$ 是當前管理或訓練決策。

因此：

$$
\boxed{
\text{forecasting an outcome}
\neq
\text{choosing interventions that change the outcome distribution}.
}
$$

---

# 3. 生命週期是 Sequential Decision Problem

定義馬匹在時間 $t$ 的狀態：

$$
S_t.
$$

人類或 AI 選擇：

$$
a_t.
$$

環境與生物發育產生：

$$
S_{t+1}
\sim
P(S_{t+1}\mid S_t,a_t,\epsilon_t).
$$

因此整個生命週期可以表示為：

$$
S_0
\rightarrow
a_0
\rightarrow
S_1
\rightarrow
a_1
\rightarrow
\cdots
\rightarrow
S_T.
$$

這比一次性的賽果分類複雜很多。

---

# 4. 結果延遲極長

配種決策在：

$$
t_0
$$

做出。

真正競賽價值可能要到：

$$
t_0+3\text{ to }5\text{ years}
$$

甚至更久才能充分觀察。

繁殖價值則可能要：

$$
t_0+8\text{ to }15\text{ years}
$$

後才變得清楚。

因此 feedback loop 很慢：

$$
\boxed{
\text{slow biological feedback}
}
$$

是 AI 育種最大的統計困難之一。

---

# 5. 「血統」不是「基因體」

傳統 pedigree 可以表示為圖：

$$
G_P=(V,E),
$$

其中節點是祖先，邊表示親子關係。

但兩匹具有相同 pedigree 關係的後代，實際 inherited genome 並不完全相同。

所以：

$$
\boxed{
\text{Pedigree Relatedness}
\neq
\text{Realized Genomic Relatedness}.
}
$$

---

# 6. 這就是 Genomics 增加的資訊

若只有 pedigree：

$$
X_P.
$$

加入 SNP、ROH 與其他 genomic measurement：

$$
X_G.
$$

則理論上：

$$
I(
X_P,X_G;
Y
)
\geq
I(X_P;Y).
$$

但是否具有實際增量資訊仍必須透過 out-of-sample 驗證。

---

# 7. MSTN 是最經典的例子

純血馬中，MSTN 附近的變異與最適競賽距離具有強烈關聯。

經典研究指出：

$$
C/C
$$

通常偏向較短距離與速度，

$$
C/T
$$

較常適於中距離，

$$
T/T
$$

則較偏向耐力與較長距離；這一關聯在包括日本與美國在內的不同 Thoroughbred 群體中得到重複驗證。[1]

---

# 8. 但 MSTN 不是「冠軍基因」

重要的是：

$$
\boxed{
\text{distance aptitude}
\neq
\text{total racing ability}.
}
$$

一匹馬能否成功還受：

- 心肺；
- 骨骼；
- 肌腱；
- 神經；
- 行為；
- 成長；
- 訓練；
- 傷病；
- 場地；
- 騎乘；

等大量因素影響。

因此：

$$
Y
=
f(
G_1,G_2,\ldots,G_k,
E,
G\times E
).
$$

---

# 9. Polygenic Reality

競賽能力更接近：

$$
Y
=
\sum_{j=1}^{k}\beta_jG_j
+
\sum_{m=1}^{r}\gamma_mE_m
+
\sum_{j,m}\eta_{jm}G_jE_m
+
\epsilon.
$$

其中：

$$
k\gg1.
$$

因此單一基因測試不能取代完整的 phenotype 與 longitudinal observation。

---

# 10. Genetic Potential 與 Realized Performance

可以定義：

$$
Z_G
=
\text{genetic potential}.
$$

實際表現：

$$
Y
=
F(Z_G,E_t,A_t,\epsilon_t).
$$

所以：

$$
\boxed{
\text{high genetic potential}
\not\Rightarrow
\text{high realized performance}.
}
$$

---

# 11. AI 配種不是「找最強公馬」

設母馬為 $m$，候選公馬集合：

$$
\mathcal S
=
\{s_1,\ldots,s_n\}.
$$

傳統簡化問題：

$$
s^*
=
\arg\max_s
\text{StallionQuality}(s).
$$

這其實錯了。

真正問題是：

$$
s^*
=
\arg\max_s
E[
U(\text{offspring})
\mid
m,s
].
$$

---

# 12. 配種是 Conditional Compatibility Problem

同一匹公馬對不同母馬的價值可能完全不同：

$$
U(m_1,s)
\neq
U(m_2,s).
$$

所以：

$$
\boxed{
\text{best sire}
\neq
\text{best sire for this mare}.
}
$$

這也是 pedigree nicking 工具存在多年的原因。

---

# 13. 電腦化配種早於現代 AI

例如 TrueNicks 現行服務可以對一匹 broodmare 評估最多 $50$ 匹候選種公馬，並按照 pedigree cross、stud fee、地點與近交等條件協助縮小候選範圍。[12]

因此：

$$
\boxed{
\text{computational mating assistance}
}
$$

本身並不是生成式 AI 時代才出現。

現代 AI 的差別是可加入更多 heterogeneous data。

---

# 14. 從 Pedigree Score 到 Multimodal Mating Model

傳統：

$$
Score(m,s)
=
f(Pedigree).
$$

未來可以變成：

$$
Score(m,s)
=
f(
Pedigree,
Genome,
Phenotype,
Health,
Performance,
Progeny,
Market,
Diversity
).
$$

但這也讓模型更容易過擬合。

---

# 15. 配種的第一個多目標衝突：速度與耐久

若單獨最大化：

$$
E[\text{speed}],
$$

可能犧牲：

$$
E[\text{soundness}].
$$

因此需要：

$$
U
=
w_1V_{\mathrm{speed}}
+
w_2V_{\mathrm{stamina}}
+
w_3V_{\mathrm{soundness}}
+\cdots
$$

而不是單目標冠軍模型。

---

# 16. 第二個衝突：個體最佳化與族群多樣性

假設某熱門 sire：

$$
s^*
$$

對大量母馬都有高短期評分。

如果所有 breeder 都選：

$$
s^*,
$$

族群層面可能：

$$
D_{\mathrm{genetic}}\downarrow.
$$

所以：

$$
\boxed{
\text{locally optimal mating}
\not\Rightarrow
\text{globally healthy breeding population}.
}
$$

---

# 17. Thoroughbred 的近交問題是真實存在的

一項涵蓋：

$$
n=10,118
$$

匹純血馬的全球基因體研究顯示，過去五十年全球 Thoroughbred 的 genomic diversity 顯著下降，inbreeding 顯著增加，熱門 sire lines 被認為是重要因素之一。[2]

因此配種 AI 不能只有：

$$
\max E[\text{performance}].
$$

還需要：

$$
\min R_{\mathrm{inbreeding}}.
$$

---

# 18. 近交不是只看血統表中的 $3\times4$

pedigree coefficient 是期望量。

真正 genome 中的 runs of homozygosity：

$$
F_{\mathrm{ROH}}
$$

可以提供 realized inbreeding 的直接資訊。

因此：

$$
\boxed{
F_{\mathrm{pedigree}}
\neq
F_{\mathrm{ROH}}.
}
$$

---

# 19. Genomic Inbreeding 與可出賽性

另一項涵蓋 $6,128$ 匹 Thoroughbred 的研究發現：

$$
F_{\mathrm{ROH}}
$$

增加與「終其一生是否實際出賽」的概率下降相關；研究報告 $10\%$ 的 inbreeding 增加與約 $7\%$ 較低的 ever-racing probability 相關。[3]

這表示 soundness 與可用性不能被競賽速度模型忽略。

---

# 20. 配種模型因此必須加入 Constraint

可以寫成：

$$
\max_s E[U_{\mathrm{offspring}}]
$$

subject to：

$$
R_{\mathrm{inbreeding}}(m,s)
\leq
\tau_I,
$$

$$
R_{\mathrm{deleterious}}(m,s)
\leq
\tau_D.
$$

這比「AI 挑最強配種」更合理。

---

# 21. Population-Level AI 與 Owner-Level AI 不是同一個目標

個別馬主可能：

$$
\max U_i.
$$

整個 breed authority 可能更在意：

$$
\max
\left[
E[\text{population performance}]
+
\lambda D_{\mathrm{genetic}}
-
\mu R_{\mathrm{disease}}
\right].
$$

因此：

$$
\boxed{
\text{private breeding optimum}
\neq
\text{population breeding optimum}.
}
$$

---

# 22. AI 甚至可能放大熱門血統偏誤

假設訓練資料來自過去市場。

市場長期偏好熱門 sire。

模型學到：

$$
\text{popular sire}
\rightarrow
\text{high sale price}.
$$

然後推薦：

$$
\text{popular sire}.
$$

更多 breeder 跟隨。

於是：

$$
\boxed{
\text{historical preference}
\rightarrow
\text{model}
\rightarrow
\text{reinforced preference}.
}
$$

這是 breeding feedback loop。

---

# 23. Prediction 與 Prescription 必須分開

模型可以準確預測：

$$
P(\text{high auction price}\mid m,s).
$$

但不能直接推出：

$$
\boxed{
\text{therefore breed }m\text{ to }s.
}
$$

因為：

$$
\text{market value}
\neq
\text{welfare}
\neq
\text{racing value}
\neq
\text{genetic diversity}.
$$

---

# 24. Thoroughbred 制度本身對生物技術有清楚界線

2026 年 IFHA International Agreement Article 12 仍要求 Thoroughbred 來自 stallion 對 mare 的自然交配，以及由同一母馬自然妊娠與生產；人工授精、胚胎移植、複製與未明定的遺傳操弄所產後代不具 Approved Thoroughbred Stud Book 資格。[4]

這是 AI 時代很重要的制度背景。

---

# 25. 日本 Stud Book 也採相同原則

日本現行 Stud Book 登錄規則同樣要求 natural mating 與 natural gestation，並明確表示 Artificial Insemination、Embryo Transfer、Cloning 或其他未明定的 genetic manipulation 所產後代不能登錄。[5]

所以：

$$
\boxed{
\text{AI-assisted breeding selection}
}
$$

與：

$$
\boxed{
\text{genetic engineering of Thoroughbreds}
}
$$

必須完全區分。

---

# 26. 有趣的縮寫悖論

馬產業中的傳統：

$$
AI
=
\text{Artificial Insemination}.
$$

而本文：

$$
AI
=
\text{Artificial Intelligence}.
$$

因此可以出現：

$$
\boxed{
\text{Artificial Intelligence may assist mating selection, while Artificial Insemination is disallowed for registered Thoroughbreds.}
}
$$

這恰好說明「決策智能」與「繁殖技術」是兩個制度層級。

---

# 27. 從出生後開始，問題變成 Developmental Control

出生後狀態：

$$
S_0
$$

不是固定。

營養、運動、疾病與成長共同產生：

$$
S_t.
$$

所以：

$$
\boxed{
\text{genotype is an initial condition, not a final outcome}.
}
$$

---

# 28. 日本 JRA 已經有完整的育成研究鏈

JRA 表示，自有育成馬會被用於「強い馬づくり」的生產育成研究；2008 年起更利用自家生產馬研究「從生產到育成」的連續流程。[6]

這代表日本不是把育成只當技藝。

它已經是：

$$
\boxed{
\text{longitudinal applied science}.
}
$$

---

# 29. 日高生產育成研究室的範圍非常廣

JRA Equine Science Division 的公開任務包含：

- nutrition；
- reproduction；
- pasture management；
- veterinary medicine；
- exercise physiology；

並把成果傳回 breeder、veterinarian 與生產育成現場。[7]

所以未來 AI 能介入的 feature space 本來就非常多。

---

# 30. 運動科學也已經是可量化狀態

JRA Sports Science Division 目前研究：

$$
\text{cardiovascular physiology},
$$

$$
\text{muscle adaptation},
$$

$$
\text{biomechanics},
$$

$$
\text{nutrition}.
$$

2026--2028 的研究課題還直接包含調教內容與競賽成績、運動器疾病發生率的關聯。[13]

---

# 31. 這使 Training AI 成為因果決策問題

如果只是預測：

$$
P(\text{injury}\mid X_t),
$$

是 risk model。

如果 AI 接著建議：

$$
a_t=\text{reduce workload},
$$

它就進入：

$$
\boxed{
\text{causal intervention}.
}
$$

因此需要回答：

$$
P(Y\mid do(a_t))
$$

而不只是：

$$
P(Y\mid a_t).
$$

---

# 32. Observation Bias 特別嚴重

假設高風險馬被減少訓練。

資料裡：

$$
\text{low workload}
\leftrightarrow
\text{high injury risk}.
$$

一個只學 correlation 的 AI 可能錯誤推論：

> 低訓練量造成受傷。

實際因果可能是：

$$
\text{latent injury}
\rightarrow
\begin{cases}
\text{lower workload}\\
\text{higher injury probability}
\end{cases}
$$

這是典型 confounding。

---

# 33. 所以 Lifecycle AI 比賽事 AI 更需要因果推論

賽事模型：

$$
\hat P(Y).
$$

養成模型：

$$
\hat P(Y\mid do(a)).
$$

兩者不是同一個能力。

因此：

$$
\boxed{
\text{predictive ML}
\not\Rightarrow
\text{safe prescriptive ML}.
}
$$

---

# 34. Wearable Sensor 已開始提供新的 Observation Layer

2025 年發表的大型美國研究分析：

$$
11,834
$$

匹 Thoroughbred 與：

$$
28,481
$$

次出賽的 stride data。

使用 accelerometer-based inertial measurement unit 加上演算法風險評分，將馬匹分成 $1$ 到 $6$ 級。[8]

---

# 35. 高風險小群體的訊號非常強

研究中 risk score $6$ 只占約：

$$
0.4\%
$$

的 starts，

但其致命肌肉骨骼傷害概率約為 risk score $1$ 的：

$$
44.6
$$

倍。[8]

這說明 sensor + algorithm 可以把肉眼不容易整合的步態訊號轉成臨床風險分層。

---

# 36. 但 Risk Score 不應變成 Automatic Exclusion Oracle

一個高 risk score 代表：

$$
P(\text{injury}\mid X)\uparrow.
$$

不代表：

$$
P(\text{injury}\mid X)=1.
$$

因此：

$$
\boxed{
\text{risk model}
\neq
\text{diagnosis}.
}
$$

需要 veterinarian review、影像、臨床與時間序列共同判斷。

---

# 37. AI 的合理角色是 Triage

可以寫成：

$$
\text{Sensor}
\rightarrow
\text{Risk Model}
\rightarrow
\text{Triage}
\rightarrow
\text{Veterinary Examination}.
$$

而不是：

$$
\text{Sensor}
\rightarrow
\text{automatic irreversible decision}.
$$

---

# 38. 生命週期模型必須把 Welfare 當一級變數

如果只最大化：

$$
E[\text{earnings}],
$$

模型可能偏好更高風險策略。

所以需要：

$$
U
=
E[\Pi]
-
\lambda R_{\mathrm{injury}}
+
\eta W_{\mathrm{welfare}}
+\cdots
$$

其中：

$$
\lambda>0.
$$

---

# 39. Welfare 與 Performance 不必然對立

降低嚴重傷病：

$$
R_{\mathrm{injury}}\downarrow
$$

往往同時提高：

$$
\text{career length},
$$

$$
\text{availability},
$$

$$
\text{realized racing value}.
$$

因此健康資料不是「額外道德欄位」。

它也是核心 performance variable。

---

# 40. 拍賣是另一種完全不同的模型

在 auction 時間 $t_a$，真正 lifetime value 尚未知道。

市場觀察：

$$
X_a.
$$

形成價格：

$$
P_a.
$$

未來才實現：

$$
V_T.
$$

因此：

$$
\boxed{
\text{Auction Price}
\neq
\text{Future Racing Value}.
}
$$

---

# 41. 拍賣 AI 首先可以只是 Price Model

$$
\hat P_a
=
f(
pedigree,
sire,
dam,
session,
reputation,
conformation,
\ldots
).
$$

它回答：

> 市場大概會出多少錢？

這不是：

> 這匹馬真正值多少錢？

---

# 42. 2026 Keeneland ML 研究

2026 年 Yang 等人使用：

$$
5,788
$$

筆 2020--2024 Keeneland September Yearling Sale 資料，使用 Ridge 與多種 tree-based ML 模型預測 log auction price。

其解釋模型的 out-of-sample：

$$
R^2\approx0.5403.
$$

且 sire 與 dam reputation 是主要 predictors。[9]

---

# 43. 這個結果很強，也同時顯示限制

如果：

$$
R^2\approx0.54,
$$

表示大量價格變異仍沒有被模型解釋。

可能來源包括：

- conformation；
- veterinary report；
- walking impression；
- physical maturity；
- buyer preference；
- bidding competition；
- information not present in dataset。

所以：

$$
\boxed{
\text{auction valuation remains partially irreducible to pedigree tables}.
}
$$

---

# 44. 未來 Multimodal Auction AI

可以加入：

$$
X_{\mathrm{image}},
$$

$$
X_{\mathrm{video}},
$$

$$
X_{\mathrm{gait}},
$$

$$
X_{\mathrm{veterinary}},
$$

$$
X_{\mathrm{genomic}}.
$$

形成：

$$
\hat V
=
f(
X_P,
X_G,
X_I,
X_V,
X_H
).
$$

但這也需要非常嚴格的 point-in-time 資料與 leakage control。

---

# 45. 日本 Select Sale 是極高價值的自然研究場

2026 Select Sale：

$$
509
$$

匹上場，

$$
478
$$

匹成交，

成交率：

$$
93.9\%.
$$

成交總額：

$$
33.484\text{ billion yen}.
$$

平均成交價約：

$$
70.05\text{ million yen}.
$$

最高價：

$$
420\text{ million yen}.
$$

[10]

---

# 46. 所以小幅估值改善也可能具有巨大價值

若一個大型買方每年購買總額：

$$
B
$$

非常高，

即使 decision quality 只改善：

$$
\delta=0.01,
$$

理論經濟影響也可能約為：

$$
\delta B.
$$

但這仍不能保證「AI 買馬會賺」。

---

# 47. 因為 Auction Value 有多個目標

馬主可能追求：

$$
V_{\mathrm{race}},
$$

breeder 可能追求：

$$
V_{\mathrm{breeding}},
$$

reseller 可能追求：

$$
V_{\mathrm{resale}},
$$

而 hobby owner 可能追求：

$$
V_{\mathrm{experience}}.
$$

所以：

$$
\boxed{
\text{one horse}
\neq
\text{one universal value}.
}
$$

---

# 48. 這帶回本篇最重要的「馬主效用」

假設馬主只被建模成投資者：

$$
U_{\mathrm{owner}}
=
E[\Pi].
$$

那會漏掉日本馬主制度非常重要的一部分。

JRA 自己把馬主活動描述成「愛馬に夢をのせて」，並提供與愛馬、命名、勝負服、paddock、Winner's Circle 等直接參與相關的制度性體驗。[11][14]

---

# 49. 馬主不是 Bettor

賭徒效用可以粗略寫：

$$
U_{\mathrm{bettor}}
=
E[\Pi]
-
\lambda Var(\Pi).
$$

馬主則更合理寫為：

$$
U_{\mathrm{owner}}
=
\alpha E[\Pi]
+
\beta V_O
+
\gamma V_C
+
\delta V_S
+
\epsilon V_L
-
C.
$$

其中：

$$
V_O=\text{ownership value},
$$

$$
V_C=\text{choice and control value},
$$

$$
V_S=\text{story and participation value},
$$

$$
V_L=\text{legacy value}.
$$

---

# 50. 日本 JRA 的制度本身支持這個模型

JRA 馬主可以：

- 在愛馬出賽時進入馬主 paddock 區；
- 勝利後進行 Winner's Circle 紀念拍攝；
- 設計自己的勝負服；
- 為馬匹命名；
- 進入 training center；
- 參與馬主社群與活動。[11]

所以：

$$
\boxed{
\text{ownership utility is institutionally real}.
}
$$

它不是研究者憑空加入的情緒變數。

---

# 51. 經濟層面當然也仍然重要

JRA 公開資料顯示，2025 年向馬主支付的獎金等約：

$$
104\text{ billion yen},
$$

當年在 JRA 出賽馬匹 $11,923$ 匹，平均每匹年度獎金等收入約：

$$
8.72\text{ million yen}.
$$

同時 JRA 列出的 2025 年一歲馬市場平均價格約為：

$$
14.77\text{ million yen},
$$

而訓練中心預託料約：

$$
0.7\text{ million yen per month}
$$

程度。[15]

這顯示馬主活動具有明確成本與財務面，但不因此變成單純投資產品。

---

# 52. AI 可以比馬主更「理性」，但仍可能選錯馬

如果 AI objective 是：

$$
\max E[\Pi],
$$

而馬主真正 objective 是：

$$
\max U_{\mathrm{owner}},
$$

那麼 AI 所謂最佳選擇：

$$
h^*_{\mathrm{AI}}
$$

可能不是：

$$
h^*_{\mathrm{owner}}.
$$

因此：

$$
\boxed{
\text{objective misspecification}
}
$$

比預測誤差更危險。

---

# 53. 例如「我就是喜歡這條母系」

這可能沒有最大化：

$$
E[\Pi].
$$

但它提高：

$$
V_S
$$

與：

$$
V_L.
$$

所以在人類真正效用函數下，它未必是不理性。

這是把文化性 hobby 錯誤金融化時最容易漏掉的一點。

---

# 54. AI 可能反而降低 Owner Utility

若流程變成：

$$
\text{AI ranks}
\rightarrow
\text{owner blindly accepts}
\rightarrow
\text{AI manages everything},
$$

可能：

$$
E[\Pi]\uparrow
$$

但：

$$
V_C\downarrow,
$$

$$
V_S\downarrow.
$$

若：

$$
\beta,\gamma,\delta
$$

很大，總效用甚至：

$$
U_{\mathrm{owner}}\downarrow.
$$

---

# 55. 這是 Automation Paradox

本文提出：

$$
\boxed{
\text{Ownership Automation Paradox}
}
$$

即：

> 對以參與、選擇與故事為主要價值來源的活動，最佳化結果的自動化可能同時降低從活動本身得到的效用。

形式上：

$$
\frac{\partial E[\Pi]}{\partial A}>0
$$

但可能：

$$
\frac{\partial V_{\mathrm{participation}}}{\partial A}<0.
$$

---

# 56. 因此「反 AI 馬主」不一定反科技

一名馬主完全可能接受：

$$
\text{genomic risk report},
$$

$$
\text{injury monitoring},
$$

但拒絕：

$$
\text{AI final horse selection}.
$$

這是一種：

$$
\boxed{
\text{selective delegation}
}
$$

而不是 irrational technology rejection。

---

# 57. 未來很可能形成不同的馬主策略類型

第一類：

$$
\text{Traditional Owner}.
$$

第二類：

$$
\text{AI-Assisted Owner}.
$$

第三類：

$$
\text{Quant Owner}.
$$

第四類：

$$
\text{Experience-Preserving Owner}.
$$

不同類型最佳化不同 utility。

---

# 58. AI-Assisted Owner 可能成為主要均衡

一個合理流程：

$$
300\text{ candidates}
$$

$$
\xrightarrow{\text{AI}}
30
$$

$$
\xrightarrow{\text{human inspection}}
5
$$

$$
\xrightarrow{\text{owner choice}}
1.
$$

AI 負責擴張認知能力，但不拿走最終決策。

---

# 59. 這叫 Human Sovereignty over Final Selection

可以定義：

$$
\boxed{
a_{\mathrm{final}}
\in
\mathcal A_{\mathrm{human}}
}
$$

即使候選集合：

$$
\mathcal C
$$

由 AI 產生，最後決策權仍保留在人類。

---

# 60. Breeder 的作者性甚至更強

馬主買的是一匹馬。

breeder 做的是：

$$
\text{mare}
+
\text{stallion}
\rightarrow
\text{new lineage branch}.
$$

所以配種選擇包含：

$$
\boxed{
\text{biological authorship}.
}
$$

這種效用無法完全用 sale price 取代。

---

# 61. AI 配出 Derby Winner 後「誰的判斷？」

假設：

$$
AI
\rightarrow
\text{stallion choice}
\rightarrow
\text{training plan}
\rightarrow
\text{race selection}.
$$

人類只負責批准。

最終成功時，會出現：

$$
\boxed{
\text{Decision Authorship Problem}.
}
$$

這與 Paper 06、07 之後的 Decision Provenance 其實是同一族問題。

---

# 62. 生命週期 AI 的 Decision Provenance

每個重要決策可以保存：

$$
D_t
=
(
\text{human proposal},
\text{AI recommendation},
\text{evidence},
\text{final decision},
\text{responsible actor}
).
$$

這不只是問責工具。

它也保留：

$$
\boxed{
\text{who shaped the horse's lifecycle}.
}
$$

---

# 63. 因此 Lifecycle Ledger 具有理論價值

可以想像：

$$
L_i
=
\{D_0,D_1,\ldots,D_T\}.
$$

它記錄：

- 配種決策；
- 購買；
- nutrition changes；
- training changes；
- veterinary interventions；
- race placement；
- retirement。

這不是本文要做的 MVP。

它只是指出：生命週期 AI 的科學分析需要 longitudinal decision provenance。

---

# 64. Digital Twin 是自然延伸，但不能被神化

若建立 horse state：

$$
Z_i(t)
=
f(
G_i,
P_i,
M_i(t),
N_i(t),
T_i(t),
V_i(t),
B_i(t),
R_i(t)
),
$$

其中：

$$
G_i=\text{genome},
$$

$$
P_i=\text{pedigree},
$$

$$
M_i=\text{morphology},
$$

$$
N_i=\text{nutrition},
$$

$$
T_i=\text{training},
$$

$$
V_i=\text{veterinary state},
$$

$$
B_i=\text{biomechanics},
$$

$$
R_i=\text{racing state}.
$$

可以稱為 longitudinal digital twin。

但：

$$
\boxed{
Z_i(t)
\neq
\text{the horse itself}.
}
$$

它永遠只是有限觀測下的模型。

---

# 65. Missing State 永遠存在

例如：

- 微小疼痛；
- 情緒；
- 尚未顯現的病理；
- 無法觀測的組織變化；
- measurement error。

因此：

$$
S_t^{\mathrm{true}}
\neq
S_t^{\mathrm{observed}}.
$$

AI 必須保持：

$$
U_t>0.
$$

---

# 66. Digital Twin 的價值在 Counterfactual

真正有用的問題是：

$$
P(
S_{t+1}
\mid
do(a_1)
)
$$

與：

$$
P(
S_{t+1}
\mid
do(a_2)
).
$$

即：

> 如果今天改變訓練、休息或營養，未來風險與能力分布可能怎麼改？

但這要求因果驗證，不只是漂亮 simulation。

---

# 67. 生命週期 AI 最危險的錯誤之一是 Proxy Optimization

如果目標：

$$
Y=\text{auction price},
$$

AI 可能學會提高拍賣吸引力。

如果真正關心：

$$
Z=\text{healthy successful racehorse},
$$

則：

$$
Y
$$

只是 proxy。

當：

$$
Corr(Y,Z)<1,
$$

過度最佳化：

$$
Y
$$

不保證：

$$
Z\uparrow.
$$

---

# 68. Goodhart's Law 在配種中特別危險

當某個 genetic score：

$$
G_s
$$

被當成主要 selection criterion：

$$
G_s
$$

就可能不再保持原本與整體能力的關係。

因此：

$$
\boxed{
\text{genetic score}
\rightarrow
\text{selection pressure}
\rightarrow
\text{population change}.
}
$$

模型會改變自己下一代所面對的資料分布。

---

# 69. 這又是一個 Adaptive System

Paper 03：

$$
\text{AI prediction}
\rightarrow
\text{betting flow}
\rightarrow
\text{price changes}.
$$

Paper 04：

$$
\text{AI breeding model}
\rightarrow
\text{mating choices}
\rightarrow
\text{population changes}
\rightarrow
\text{future training data changes}.
$$

所以：

$$
\boxed{
\text{AI changes the population it later models}.
}
$$

---

# 70. Breeding Model Reflexivity

設第 $t$ 代的 genetic distribution：

$$
P_t(G).
$$

AI selection policy：

$$
\pi_t(m,s).
$$

則下一代：

$$
P_{t+1}(G)
=
F(
P_t(G),
\pi_t
).
$$

因此訓練資料不是外生固定分布。

---

# 71. 這比市場反身性更慢，但更深

價格反身性：

$$
\text{minutes to days}.
$$

育種反身性：

$$
\text{years to generations}.
$$

但一旦發生，影響的是：

$$
\boxed{
\text{population state itself}.
}
$$

而不只是市場價格。

---

# 72. AI 因此可能產生 Diversity Externality

單一 owner 的 objective：

$$
U_i.
$$

不一定包含整個 population 的：

$$
D_{\mathrm{genetic}}.
$$

所以需要：

$$
C_{\mathrm{externality}}
$$

或制度 constraint。

否則每個個體都追求局部最優，可能導致集體 diversity 下降。

---

# 73. 這是非常標準的 Multi-Agent Optimization Failure

若：

$$
\forall i,\quad
a_i=\arg\max U_i,
$$

仍可能：

$$
W_{\mathrm{population}}
<
W_{\mathrm{population}}^*.
$$

所以：

$$
\boxed{
\text{individual AI optimization}
\not\Rightarrow
\text{population optimality}.
}
$$

---

# 74. 配種 AI 最終需要 Governance Layer

不一定是禁止 AI。

而可能是：

- diversity monitoring；
- genomic risk disclosure；
- welfare constraints；
- model uncertainty disclosure；
- Stud Book rules；
- breeder autonomy。

因此：

$$
\boxed{
\text{AI}
+
\text{biology}
+
\text{institution}
}
$$

三者不能分開。

---

# 75. 日本尤其適合觀察 Human-AI Coexistence

日本同時具有：

- 高度成熟的育種與育成研究；
- 高價 Select Sale；
- 強烈血統文化；
- 個人與法人馬主；
- 馬主參與體驗；
- 高密度的長期賽馬資料。

因此它很可能成為：

$$
\boxed{
\text{AI optimization}
\quad\text{vs}\quad
\text{ownership culture}
}
$$

最有代表性的研究場景之一。

---

# 76. 未來真正的爭議可能不是「AI 準不準」

更可能是：

> AI 可以介入到哪一層？

例如：

$$
\text{risk report}
\quad\checkmark
$$

$$
\text{candidate ranking}
\quad\checkmark
$$

$$
\text{automatic mating selection}
\quad ?
$$

$$
\text{automatic sale purchase}
\quad ?
$$

$$
\text{automatic training control}
\quad ?
$$

每一層的可接受性可能不同。

---

# 77. 技術接受度可以寫成 Delegation Depth

定義：

$$
d\in[0,1].
$$

其中：

$$
d=0
$$

代表 AI 不介入，

$$
d=1
$$

代表完整自動化。

不同馬主具有：

$$
d_i^*.
$$

而：

$$
d_i^*
$$

取決於其效用函數。

---

# 78. Profit-Maximizing Owner 可能偏高 $d$

若：

$$
\alpha\gg\beta,\gamma,\delta,
$$

則：

$$
d^*\uparrow.
$$

也就是更願意把決策交給模型。

---

# 79. Experience-Maximizing Owner 可能偏低 $d$

若：

$$
\beta+\gamma+\delta
$$

很大，

則：

$$
d^*\downarrow.
$$

因為：

$$
\text{participation}
$$

本身就是產品。

---

# 80. 所以市場會同時存在不同 AI 採用層級

這不一定收斂成：

$$
d=1.
$$

更可能形成：

$$
P(d)
$$

的長期分布。

這跟攝影、棋類、創作、汽車駕駛一樣：技術可自動化，不代表所有使用者都最大化自動化程度。

---

# 81. 本文提出 Lifecycle Intelligence Stack

$$
\boxed{
\begin{array}{c}
\text{Layer 0: Stud Book / Rule Constraints}\\
\downarrow\\
\text{Layer 1: Pedigree and Genomics}\\
\downarrow\\
\text{Layer 2: Reproduction and Development}\\
\downarrow\\
\text{Layer 3: Morphology and Biomechanics}\\
\downarrow\\
\text{Layer 4: Training and Nutrition}\\
\downarrow\\
\text{Layer 5: Veterinary and Welfare}\\
\downarrow\\
\text{Layer 6: Auction and Market}\\
\downarrow\\
\text{Layer 7: Racing Outcomes}\\
\downarrow\\
\text{Layer 8: Owner and Breeder Utility}
\end{array}
}
$$

只有把最後一層保留，才不會把人類參與活動錯誤簡化成資產工程。

---

# 82. 第一核心命題：Genotype Is Not Destiny

$$
\boxed{
P(Y\mid G)
\neq
1.
}
$$

因此 genomic information 可以降低不確定性，但不能消除發育、訓練與偶然性。

---

# 83. 第二核心命題：Pedigree--Genome Separation

$$
\boxed{
X_P
\neq
X_G.
}
$$

pedigree 描述 ancestry structure；genomics 描述實際遺傳變異。兩者互補但不可互換。

---

# 84. 第三核心命題：Local--Population Optimum Separation

$$
\boxed{
\arg\max U_{\mathrm{private}}
\neq
\arg\max W_{\mathrm{population}}
}
$$

可能成立。

當熱門 sire 的個體優勢累積成 population diversity loss 時尤其如此。

---

# 85. 第四核心命題：Prediction--Intervention Separation

$$
\boxed{
P(Y\mid A)
\neq
P(Y\mid do(A)).
}
$$

能預測 injury risk 的模型，不自動具備設計訓練處方的因果能力。

---

# 86. 第五核心命題：Price--Value Separation

$$
\boxed{
P_{\mathrm{auction}}
\neq
V_{\mathrm{racing}}
\neq
V_{\mathrm{breeding}}
\neq
U_{\mathrm{owner}}.
}
$$

因此不存在一個可供所有參與者共享的單一「真正馬匹價值」。

---

# 87. 第六核心命題：Ownership Utility

馬主效用至少可表示：

$$
\boxed{
U_{\mathrm{owner}}
=
f(
\Pi,
Ownership,
Choice,
Story,
Competition,
Legacy
).
}
$$

所以：

$$
\text{AI economic optimum}
$$

不必然等於：

$$
\text{owner optimum}.
$$

---

# 88. 第七核心命題：Automation Paradox

在 participation utility 很高的活動中：

$$
\frac{\partial Performance}{\partial Automation}>0
$$

可以與：

$$
\frac{\partial ExperienceUtility}{\partial Automation}<0
$$

同時成立。

因此 full automation 不必然 Pareto-improve 馬主體驗。

---

# 89. 第八核心命題：Biological Reflexivity

若 AI policy 影響 mating：

$$
\pi_{\mathrm{AI}}
\rightarrow
P_{t+1}(G),
$$

則：

$$
\boxed{
\text{the model changes the biological distribution that trains its successors}.
}
$$

這是比市場價格反身性更慢、但更深的 AI feedback loop。

---

# 90. 第九核心命題：Advisor Equilibrium

當：

- AI 能提高資訊品質；
- owner utility 含有 participation；
- 生物決策不可完全回復；
- uncertainty 無法消除；

則長期穩定形態很可能不是：

$$
\text{AI replaces owner},
$$

而是：

$$
\boxed{
\text{AI advisor}
+
\text{human final authority}.
}
$$

---

# 91. 這不代表永遠不會有 Quant Owner

相反地，大型法人或 portfolio-style owner 可能建立：

$$
\text{many horses}
+
\text{portfolio statistics}
+
\text{high delegation}.
$$

他們的：

$$
U_{\mathrm{owner}}
$$

可能更接近財務與競賽績效。

所以不同 owner class 會形成不同 AI ecology。

---

# 92. 一口馬主又是另一個效用結構

share ownership 讓：

$$
C_i\downarrow
$$

並可能增加：

$$
V_{\mathrm{participation}}.
$$

AI 若大量進入募集馬篩選，可能降低資訊門檻，但同時也可能造成熱門候選更集中。

這值得後續獨立研究，但不在本篇展開具體工具。

---

# 93. AI 甚至可能改變拍賣敘事本身

當越來越多人看到：

$$
\hat V_{\mathrm{AI}},
$$

價格可能：

$$
P_a
\rightarrow
\hat V_{\mathrm{AI}}.
$$

於是模型不只預測價格。

它可能開始：

$$
\boxed{
\text{anchor price}.
}
$$

這和 Paper 03 中 AI 資金改變賠率具有相同反身性。

---

# 94. Model Reputation 也可能成為新的 Pedigree Reputation

若某 bloodstock AI 被大量使用：

$$
\text{AI score}
$$

本身可能進入市場敘事。

然後：

$$
AI\ Score
\rightarrow
Buyer\ Demand
\rightarrow
Auction\ Price.
$$

此時模型失去純外部觀察者地位。

---

# 95. 因此拍賣模型也需要 Anti-Reflexive Evaluation

不能只問：

$$
Corr(\hat P,P_a).
$$

還應問：

$$
\hat P
$$

是否已經影響：

$$
P_a.
$$

否則高預測力可能部分來自：

$$
\boxed{
\text{self-fulfilling valuation}.
}
$$

---

# 96. 生命週期 AI 的資料問題比賽事資料更難

因為資料跨：

- breeding farm；
- sale company；
- owner；
- trainer；
- veterinarian；
- race authority；
- genetic lab。

所以：

$$
\boxed{
\text{data fragmentation}
}
$$

可能是比模型本身更大的限制。

---

# 97. 最稀缺的不是演算法，而是 Canonical Longitudinal Dataset

真正理想資料：

$$
D_i
=
(
G_i,
P_i,
Birth_i,
Growth_i,
Health_i,
Training_i,
Auction_i,
Racing_i,
Breeding_i
).
$$

而且每一層都要：

$$
\text{timestamped}
+
\text{quality-controlled}
+
\text{identity-linked}.
$$

這種資料集極具商業與隱私價值，因此很難公開集中。

---

# 98. 這解釋了為什麼零件已存在但完整系統仍少見

目前已存在：

$$
\text{pedigree analytics},
$$

$$
\text{genetic tests},
$$

$$
\text{biomechanics},
$$

$$
\text{wearables},
$$

$$
\text{auction ML},
$$

$$
\text{race models}.
$$

缺的往往是：

$$
\boxed{
\text{cross-stage identity-linked integration}.
}
$$

---

# 99. AI Racehorse Lifecycle Twin 因此是可預判方向，但不是已完成事實

從現有技術可以合理推論：

$$
\text{integration pressure}\uparrow.
$$

但截至本文所檢索的公開資料，不能把日本頂級牧場描述成已經公開部署一套完整、全自動的 genome-to-race lifecycle optimizer。

因此應區分：

$$
\boxed{
\text{technically plausible trajectory}
}
$$

與：

$$
\boxed{
\text{publicly verified current deployment}.
}
$$

---

# 100. 研究邊界

本篇不提供：

$$
\text{deployable breeding optimizer},
$$

$$
\text{automatic auction bidder},
$$

$$
\text{prescriptive veterinary engine},
$$

$$
\text{automatic training controller}.
$$

本篇研究的是：

- AI 如何改變生命週期決策；
- genomics 與 pedigree 如何互補；
- 育種與族群風險；
- auction valuation；
- owner utility；
- automation boundary；
- decision authorship；
- governance。

---

# 101. 與 Paper 03 的關係

Paper 03：

$$
\boxed{
\text{collective intelligence produces price}.
}
$$

Paper 04：

$$
\boxed{
\text{lifecycle intelligence can alter which future competitors exist}.
}
$$

所以我們從：

$$
\text{market reflexivity}
$$

進入：

$$
\boxed{
\text{biological reflexivity}.
}
$$

---

# 102. 從 Price Formation 到 Population Formation

在共同彩池：

$$
AI
\rightarrow
Bet
\rightarrow
Price.
$$

在 breeding：

$$
AI
\rightarrow
Mate\ Selection
\rightarrow
Offspring\ Population.
$$

這兩者有一個深層同構：

$$
\boxed{
\text{prediction system}
\rightarrow
\text{action}
\rightarrow
\text{changes future data-generating system}.
}
$$

---

# 103. 結論

人工智慧進入賽馬產業後，最直觀的應用是：

$$
\text{predict which horse wins}.
$$

但這只是生命週期的最後幾個時間點。

真正更深的 AI 化會逐漸向前延伸：

$$
\text{Pedigree}
\rightarrow
\text{Genomics}
\rightarrow
\text{Mating}
\rightarrow
\text{Development}
\rightarrow
\text{Training}
\rightarrow
\text{Health}
\rightarrow
\text{Auction}
\rightarrow
\text{Racing}
\rightarrow
\text{Breeding}.
$$

每一步都產生新的資料，也改變下一步的狀態。

因此：

$$
\boxed{
\text{Racehorse AI}
}
$$

最終可能不再是一個預測器，而是一個：

$$
\boxed{
\text{long-horizon biological decision-support system}.
}
$$

然而，這個系統不能只最大化速度、獎金或拍賣價格。

基因體研究已顯示 Thoroughbred 面臨真實的 diversity 與 inbreeding 問題。[2][3] 競賽能力也不是單一基因決定；MSTN 提供的重要資訊主要是距離適性與速度相關傾向，而非完整冠軍命運。[1]

同時，現代育成科學已經使營養、運動生理、步態、傷病風險與訓練負荷逐漸可以量化。[6][7][8] 拍賣市場也已出現正式的機器學習價格模型。[9]

所以技術方向並不神秘。

真正困難的是：

$$
\boxed{
\text{what should be optimized?}
}
$$

如果回答只是：

$$
\max E[\Pi],
$$

就會錯過 welfare、genetic diversity、biological uncertainty 與日本馬主文化中非常重要的 ownership experience。

因此本文最後提出的不是：

$$
\text{Fully Autonomous Racehorse Factory}.
$$

而是：

$$
\boxed{
\text{AI as Bloodstock and Lifecycle Advisor}.
}
$$

AI 可以：

- 看更多資料；
- 找到人類不容易察覺的配種風險；
- 提醒近交與健康問題；
- 建立更好的育成狀態模型；
- 輔助拍賣估值；
- 協助長期風險管理。

但是：

$$
\boxed{
\text{better advice}
\neq
\text{mandatory delegation}.
}
$$

對某些 Quant Owner，最深的自動化可能本身就是效用最大化。

對另一些馬主，真正珍貴的恰恰是：

> 我自己看中了牠。  
> 我選了這個血統。  
> 我替牠取了名字。  
> 我等著牠長大。  
> 最後牠真的跑出來了。

在這樣的效用函數中，不確定性、選擇與參與不是需要全部消除的 defect。

它們本身就是：

$$
\boxed{
\text{part of the value}.
}
$$

因此 AI 生命週期智能最後面對的，不只是「如何做出更好的馬」。

而是：

$$
\boxed{
\text{當智能足以最佳化一個長期的人與生命共同參與活動時，
究竟哪些決策應該交給模型，
哪些決策的價值恰恰來自人仍然親自作出它？}
}
$$

這個問題將直接連接後續 Paper 05 與 Paper 06：當 AI 進入賭場與策略牌局後，制度不再只問 AI 能不能提高決策能力，而會進一步問「什麼樣的智能輔助仍屬於合理參與，什麼時候已經取代了原本被要求的人類決策」。

---

## References

[1] Hill, E. W. et al. *The genetic origin and history of speed in the Thoroughbred racehorse*. Nature Communications 3, 643 (2012).  
https://www.nature.com/articles/ncomms1644

[2] McGivney, B. A. et al. *Genomic inbreeding trends, influential sire lines and selection in the global Thoroughbred horse population*. Scientific Reports 10, 466 (2020).  
https://pmc.ncbi.nlm.nih.gov/articles/PMC6965197/

[3] Todd, E. T. et al. *Inbreeding depression and the probability of racing in the Thoroughbred horse*.  
https://pmc.ncbi.nlm.nih.gov/articles/PMC9240673/

[4] International Federation of Horseracing Authorities. *International Agreement on Breeding, Racing and Wagering*, Article 12, June 2026 edition.  
https://www.ifhaonline.org/default.asp?AREA=2&section=IABRW

[5] Japanese Stud Book / JAIRS. *Conditions of Entry to the Japanese Stud Book*.  
https://www.studbook.jp/en/kyokai/pdf/e-kitei.pdf

[6] Japan Racing Association. *JRA育成馬を用いた生産育成研究業務*.  
https://www.jra.go.jp/facilities/farm/training/research/

[7] JRA Equine Research Institute. *Equine Science Division, Hidaka Training and Research Center*.  
https://company.jra.jp/equinst/laboratories/hidaka.html

[8] McSweeney, D. et al. *Thoroughbreds deemed to be most at risk by inertial measurement unit sensors suffered a fatal musculoskeletal injury at a higher rate than other racehorses*. Journal of the American Veterinary Medical Association (2025).  
https://pubmed.ncbi.nlm.nih.gov/40961979/

[9] Yang, Y., Clarke, J., Mandal, T., Nguyen, T. & Pham, T. *Predicting Thoroughbred Yearling Auction Prices with Machine Learning: Evidence from the Keeneland September Sale*. Journal of Agricultural and Applied Economics (2026).  
https://scholarship.depauw.edu/bus_facpubs/11/

[10] Japan Racing Horse Association. *Select Sale 2026 Results*.  
https://www.jrha.or.jp/selectsale/2026_list4.html

[11] Japan Racing Association. *馬主の特典・楽しみ*.  
https://www.jra.go.jp/owner/howto/benefits/

[12] TrueNicks. *Broodmare Analysis / Hypothetical Mating Reports*.  
https://www.truenicks.com/

[13] JRA Equine Research Institute. *Sports Science Division*.  
https://company.jra.jp/equinst/laboratories/Sports.html

[14] Japan Racing Association. *馬主になるには*.  
https://www.jra.go.jp/owner/howto/

[15] Japan Racing Association. *馬主活動に伴う収入・支出*.  
https://www.jra.go.jp/owner/howto/income/

---

**Next:**  
**Paper 05 — AI 與莊家制賭場：可計算、可預測、可利用與制度限制**
