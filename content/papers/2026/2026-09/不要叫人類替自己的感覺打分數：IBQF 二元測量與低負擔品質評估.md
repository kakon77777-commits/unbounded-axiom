# 不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估

## Do Not Ask Humans to Numerically Score Their Own Feelings: IBQF Binary Measurement and Low-Burden Quality Evaluation

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**英文系列：** *Physical Metrology of Intelligence: From Minimal Semantic Execution to Quality and Computational Spacetime*  
**系列編號：** EML-IPM  
**篇次：** Paper 07 / 10  
**文件編號：** EML-IPM-07  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開純理論論文／測量方法論  
**工程狀態：** 無 MVP；本文將 FDCS／IBQF 的微觀二元—宏觀湧現思想接入 IPM 品質計量，不宣稱取代任何已驗證臨床量表

---

## 摘要

IPM Paper 06 提出：

$$
\boxed{
\text{Objectifiable First,\ Human Residual Last}.
}
$$

亦即，能由形式系統驗證的品質先形式驗證，能拆成結構化條件的品質先結構化，最後才把真正無法被可靠客觀化的部分交給人類。

問題在於：當人類真的必須介入時，我們應該問什麼？

傳統方法經常要求受測者或評審直接把複雜主觀狀態映射到數字：

$$
0\sim10,
$$

$$
1\sim5,
$$

或：

$$
1\sim7.
$$

這類量表具有實務價值，但它們也把大量測量工作推回回答者本身。回答者不只需要「感受／判斷」，還必須完成：

$$
\boxed{
\text{Perception}
+
\text{Reference Construction}
+
\text{Scale Calibration}
+
\text{Multidimensional Integration}
+
\text{Numeric Mapping}.
}
$$

因此一個看似簡單的問題：

> 你現在有多痛？0 到 10 分。

實際要求回答者自行建立：

- 0 與 10 的內部參照；
- 1 與 2、6 與 7 的心理距離；
- 當前感受在整體尺度中的位置；
- 多種疼痛／功能干擾的整體整合。

當被測狀態本身已經占用大量注意力、工作記憶或執行功能時，這個要求甚至可能形成：

$$
\boxed{
\text{State Severity}\uparrow
\Rightarrow
\text{Self-Quantification Capacity}\downarrow.
}
$$

本文不主張因此廢除所有 numeric rating scale；它們在許多已驗證場景中仍有價值。本文要指出的是一個更一般的測量原則：

$$
\boxed{
\textbf{
不要讓回答者同時負責「觀察」與「建立測量尺度」。
}
}
$$

EveMissLab 先前在 IBQF（Infinite Binary-Quantified Field）與 FDCS 相關工作中提出另一條路：複雜連續狀態可以先被拆成大量局部、具體、低負擔的二元事件：

$$
\boxed{
b_i\in\{0,1\},
}
$$

再由系統從大量微觀二元反應中重建宏觀連續／多維狀態。

因此：

$$
\boxed{
\text{Binary Observation}
\neq
\text{Binary Phenomenon}.
}
$$

底層回答可以是「是／否」「A／B」「成立／不成立」，而被測的潛在品質仍然可以是：

$$
\boxed{
\boldsymbol{\theta}
\in
\mathbb R^d.
}
$$

本文將這套思想正式接入 IPM，定義 **Binary Residual Quality Measurement（BRQM）**：

$$
\boxed{
\mathcal B_Q:
\mathfrak Q_H
\rightarrow
\{0,1\}^{N}
\rightarrow
\widehat{\boldsymbol{\theta}}_H.
}
$$

其中：

- $\mathfrak Q_H$：Paper 06 留下的 Human Residual Quality；
- $\{0,1\}^{N}$：大量人類二元判斷；
- $\widehat{\boldsymbol{\theta}}_H$：由系統估計出的潛在品質向量。

本文提出兩種基本問法。

第一種為 **Local Binary Judgment**：

> 這個解釋是否讓你在第一次閱讀後知道下一步該做什麼？  
> 是／否。

> 這張圖是否有一個你第一眼就能辨識出的主視覺焦點？  
> 是／否。

第二種為 **Pairwise Comparative Judgment**：

> A 與 B 哪一個更容易理解？

回答：

$$
\boxed{
A/B.
}
$$

Pairwise data 可以使用 Thurstone、Bradley–Terry、Thurstonian IRT 等模型反推出 latent ordering，而不要求受試者自行建立全域 0–10 尺度。

例如 Bradley–Terry 型模型：

$$
\boxed{
P(A\succ B)
=
\frac{
e^{q_A}
}{
e^{q_A}+e^{q_B}
}
=
\sigma(q_A-q_B).
}
$$

其中 $q_A,q_B$ 是系統事後估計的 latent quality。

對單一輸出的二元項目，可使用 IRT 類形式：

$$
\boxed{
P(b_{rij}=1)
=
\sigma
\left(
a_i\theta_j
-d_i
+\beta_r
\right),
}
$$

其中：

- $\theta_j$：輸出 $j$ 的 latent quality；
- $a_i$：題目辨識力；
- $d_i$：題目難度／門檻；
- $\beta_r$：評審 $r$ 的系統性寬鬆／嚴格偏移。

因此：

$$
\boxed{
\text{Human gives local observations;}
}
$$

$$
\boxed{
\text{measurement system estimates the scale.}
}
$$

本文進一步提出 **Evaluator Cognitive Load Separation**。

直接數字評分的認知成本可抽象表示為：

$$
\boxed{
C_{\mathrm{rating}}
=
C_{\mathrm{perceive}}
+
C_{\mathrm{reference}}
+
C_{\mathrm{scale}}
+
C_{\mathrm{integrate}}
+
C_{\mathrm{map}}.
}
$$

局部二元判斷則近似：

$$
\boxed{
C_{\mathrm{binary}}
=
C_{\mathrm{local\ perceive}}
+
C_{\mathrm{choose}}.
}
$$

Pairwise comparison 也可避免全域 scale calibration：

$$
\boxed{
C_{\mathrm{pair}}
=
C_{\mathrm{compare}}
+
C_{\mathrm{choose}}.
}
$$

所以在設計良好的情況下：

$$
\boxed{
C_{\mathrm{binary}},
C_{\mathrm{pair}}
<
C_{\mathrm{direct\ numeric}}
}
$$

是一個可檢驗的設計假說，而不是先驗真理。

本文再提出 **Adaptive Binary Measurement**。不是所有人都需要回答固定 100 題。系統應根據目前 posterior 選擇最有資訊價值、同時負擔最低的下一題：

$$
\boxed{
i^\*
=
\arg\max_i
\frac{
\mathbb E[
IG(
\boldsymbol{\theta};
b_i
\mid
\mathcal H
)
]
}{
C_H(i)
}.
}
$$

其中：

- $IG$：預期 information gain；
- $\mathcal H$：既有回答歷史；
- $C_H(i)$：人類回答該題的估計認知成本。

這將 Paper 03 的 resource-rationality 與 FDCS／IBQF 的低負擔測量直接接在一起：

$$
\boxed{
\text{Maximum Measurement Information}
\quad
\text{per Human Cognitive Cost}.
}
$$

本文也拒絕把所有 disagreement 當成 measurement noise。

若評審對一個創意作品形成穩定的兩群偏好：

$$
P(q\mid r)
$$

呈現多峰，

這可能代表：

- 不同文化；
- 不同審美；
- 不同使用情境；
- 不同任務目的。

因此：

$$
\boxed{
Disagreement
\neq
Error.
}
$$

有時真正的品質物件應保留：

$$
\boxed{
\widehat{\boldsymbol{\theta}}_H(c,r\text{-group})
}
$$

而不是把所有人平均成一個不存在的「全人類 7.4 分」。

本文最後建立 IPM 人類殘餘品質物件：

$$
\boxed{
\mathfrak Q_H^{IBQF}
=
(
\widehat{\boldsymbol{\theta}}_H,
\Sigma_H,
N_{\mathrm{obs}},
\mathcal D_R,
B_H,
U_H,
Grade_H
)
}
$$

其中：

- $\widehat{\boldsymbol{\theta}}_H$：latent residual quality vector；
- $\Sigma_H$：posterior uncertainty / covariance；
- $N_{\mathrm{obs}}$：有效二元觀測數；
- $\mathcal D_R$：rater-disagreement structure；
- $B_H$：human-evaluation boundary / context；
- $U_H$：測量不確定性；
- $Grade_H$：人類測量證據等級。

因此 Paper 06 的：

$$
\mathfrak Q
$$

可擴張為：

$$
\boxed{
\mathfrak Q^{(7)}
=
(
\mathfrak Q_F,
\mathfrak Q_S,
\mathfrak Q_H^{IBQF}
).
}
$$

本文終端命題為：

$$
\boxed{
\textbf{
評分者負責做容易、局部、具體的判斷；
測量系統負責做困難、全域、連續的量化。
}
}
$$

---

# 1. 為什麼 0–10 看起來簡單，實際不簡單

表面上：

> 請選一個數字。

只有 11 個選項。

但人的內部工作並不是：

$$
Choice\in\{0,\ldots,10\}.
$$

---

# 2. 回答者首先要知道自己在測什麼

例如「痛」可能包含：

- intensity；
- interference；
- duration；
- location；
- unpleasantness；
- urgency。

---

# 3. 然後要自己整合

$$
\mathbf x
=
(x_1,\ldots,x_d)
$$

被回答者壓縮成：

$$
s\in\{0,\ldots,10\}.
$$

---

# 4. 這其實是一個 projection

$$
\boxed{
\Pi_{\mathrm{human}}:
\mathbb R^d
\rightarrow
\{0,\ldots,10\}.
}
$$

---

# 5. 問題是 projection rule 沒有被觀察

每個人可能偷偷使用不同：

$$
\Pi_r.
$$

---

# 6. 所以同樣的 7

未必代表：

$$
State_A\approx State_B.
$$

---

# 7. 同一個人不同時間也可能重新校準

經歷新的極端事件後，

原本的：

$$
10
$$

可能變成：

$$
7.
$$

---

# 8. 因此 Numeric Self-Rating 有 Scale Drift

$$
\boxed{
Scale_r(t_1)
\neq
Scale_r(t_2).
}
$$

---

# 9. 這不表示 numeric scale 無用

而表示：

$$
\boxed{
ObservedNumber
=
State
+
ScaleConstruction
+
Context.
}
$$

---

# 10. Measurement Burden Paradox

有些被測狀態本身會消耗：

- attention；
- working memory；
- executive function。

---

# 11. 此時：

$$
\boxed{
Severity\uparrow
\Rightarrow
AvailableCognitiveResource\downarrow
}
$$

完全可能成立。

---

# 12. 但直接量化又要求

$$
C_{\mathrm{reference}}
+
C_{\mathrm{scale}}
+
C_{\mathrm{integration}}
$$

存在。

---

# 13. 因此最需要測量的時候

可能最不適合要求複雜 self-quantification。

---

# 14. 這是一般測量問題，不只疼痛

也可能出現在：

- fatigue；
- stress；
- cognitive overload；
- aesthetic judgment；
- complex AI-output evaluation。

---

# 15. 本文不是臨床量表提案

疼痛例子只用來展示：

$$
\boxed{
\text{observer burden}
}
$$

如何污染 measurement。

任何醫療替代工具都必須另外經過臨床驗證。

---

# 16. FDCS／IBQF 的核心轉向

EveMissLab 早期 IBQF 思想把宏觀連續值看成大量微觀二元事件的統計湧現。

基本形式：

$$
\boxed{
b_i\in\{0,1\}.
}
$$

---

# 17. 宏觀 latent state

則可以是：

$$
\boxed{
\theta
=
F(b_1,\ldots,b_n).
}
$$

---

# 18. 二元的是「觀測事件」

不是現象本身。

所以：

$$
\boxed{
BinaryObservation
\neq
BinaryOntology.
}
$$

---

# 19. 這一點非常重要

否則會把 IBQF 誤解成：

> 世界所有事情都只有是或否。

不是。

---

# 20. 更準確是

> 每一次局部回答盡量只要求一個清楚決斷。

而大量局部回答可以重建高維狀態。

---

# 21. Micro-Binary / Macro-Continuous

$$
\boxed{
\{0,1\}^{N}
\rightarrow
\mathbb R^d.
}
$$

這是本文的基本測量幾何。

---

# 22. Paper 06 留下 Human Residual

Paper 06：

$$
\boxed{
\mathfrak Q
=
(
Q_F,
Q_S,
Q_H
).
}
$$

---

# 23. $Q_F$ 已盡量形式化

例如 proof checker、compiler、schema。

---

# 24. $Q_S$ 已盡量結構化

例如 constraint coverage、citation adequacy、consistency。

---

# 25. 所以 Paper 07 只處理真正剩下的

$$
\boxed{
Q_H.
}
$$

---

# 26. Human Residual 例子

- clarity；
- naturalness；
- aesthetic fit；
- emotional impact；
- perceived coherence；
- preference。

---

# 27. 第一種問法：Local Binary Judgment

不要問：

> 清晰度幾分？

---

# 28. 改問

> 你第一次讀完後，是否知道下一步該做什麼？

回答：

$$
Yes/No.
$$

---

# 29. 或

> 你是否需要重讀前一段才能理解這句？

$$
Yes/No.
$$

---

# 30. 這些仍不是完全客觀

但它們把評審工作縮小成：

$$
\boxed{
\text{local detection}.
}
$$

---

# 31. 好問題的條件

本文提出：

$$
\boxed{
\mathcal C_B
=
(
C_L,
C_1,
C_C,
C_T,
C_N
)
}
$$

---

# 32. $C_L$ — Local

只問局部可判斷事件。

---

# 33. $C_1$ — Single Construct

每題盡量只問一件事。

---

# 34. $C_C$ — Concrete

避免「整體而言是否很優秀」這種大詞。

---

# 35. $C_T$ — Temporally Bounded

若涉及時間，限定近且具體區段。

---

# 36. $C_N$ — Non-Numeric for Respondent

回答者不必建立連續尺度。

---

# 37. 第二種問法：Pairwise Comparison

給兩個輸出：

$$
A,B.
$$

問：

> 哪一個更容易理解？

---

# 38. 回答

$$
\boxed{
A/B.
}
$$

---

# 39. 這與 psychophysics / comparative judgment 有長歷史

Thurstone 的 comparative judgment、Bradley–Terry probability model，以及後來的 Thurstonian IRT 都是在利用相對判斷重建 latent ordering。

---

# 40. Bradley–Terry 基本形式

$$
\boxed{
P(A\succ B)
=
\sigma(q_A-q_B).
}
$$

---

# 41. 人不必知道 $q_A=7.3$

也不必知道 $q_B=6.8$。

只要判斷：

$$
A\succ B?
$$

---

# 42. Scale 由比較網路湧現

若有很多 pair：

$$
(A,B),
(A,C),
(B,C),
\ldots
$$

系統可以估：

$$
\widehat q_A,
\widehat q_B,
\widehat q_C.
$$

---

# 43. 這就是：

$$
\boxed{
\text{local ordinal judgments}
\rightarrow
\text{global latent scale}.
}
$$

---

# 44. Forced-Choice 的優點不是「永遠更好」

而是它可以降低某些：

- scale-use bias；
- acquiescence；
- direct self-presentation bias。

但也會帶來：

- item-context effects；
- forced discrimination noise。

---

# 45. 所以本文不主張所有題目都強迫二選一

若回答者真的無法判斷，

應允許：

$$
\boxed{
Skip / Missing
}
$$

作為 measurement metadata。

---

# 46. Skip 不是第三個品質值

真正評價變量仍是：

$$
b_i\in\{0,1\}.
$$

---

# 47. Missing 只是：

$$
\boxed{
b_i=\varnothing.
}
$$

---

# 48. 這比逼一個不知道的人亂選更誠實

---

# 49. Absolute Binary 與 Pairwise Binary

本文因此有兩種 primitive：

$$
\boxed{
b_i^{abs}\in\{0,1\}
}
$$

以及：

$$
\boxed{
b_{AB}^{pair}\in\{A,B\}.
}
$$

---

# 50. Absolute Binary 適合具體現象

例如：

> 是否需要重讀？

---

# 51. Pairwise 適合難以絕對定標的品質

例如：

> 哪一個畫面更協調？

---

# 52. 兩者可以混合

先用 absolute probes 找明顯問題，

再用 pairwise comparisons 排序剩餘候選。

---

# 53. Respondent 不再提供 latent score

這是最核心的角色分工。

$$
\boxed{
Human
\rightarrow
Observations
}
$$

---

# 54. Measurement System

$$
\boxed{
Observations
\rightarrow
LatentInference.
}
$$

---

# 55. 認知負擔分解

直接數字評分：

$$
\boxed{
C_{\mathrm{rating}}
=
C_P+C_R+C_S+C_I+C_M.
}
$$

---

# 56. $C_P$

Perception。

---

# 57. $C_R$

Reference construction。

---

# 58. $C_S$

Scale calibration。

---

# 59. $C_I$

Multidimensional integration。

---

# 60. $C_M$

Numeric mapping。

---

# 61. Binary

$$
\boxed{
C_{\mathrm{binary}}
=
C_P^{local}
+
C_{\mathrm{choice}}.
}
$$

---

# 62. Pairwise

$$
\boxed{
C_{\mathrm{pair}}
=
C_{\mathrm{compare}}
+
C_{\mathrm{choice}}.
}
$$

---

# 63. 預測

在問題設計良好時：

$$
\boxed{
C_{\mathrm{binary}},
C_{\mathrm{pair}}
<
C_{\mathrm{rating}}.
}
$$

---

# 64. 但這是一個 empirical hypothesis

不能因理論漂亮就當成已證明普遍律。

---

# 65. 可以怎麼實測負擔？

例如：

- response time；
- skip rate；
- reversal inconsistency；
- dropout；
- subjective fatigue；
- later recall interference。

---

# 66. 這些是 Measurement Process Metrics

記為：

$$
\boxed{
\mathbf C_H
=
(
RT_H,
Skip,
Inconsistency,
Dropout,
Fatigue
).
}
$$

---

# 67. 它們不是品質答案本身

所以：

$$
\boxed{
MeasurementBurden
\neq
MeasuredQuality.
}
$$

---

# 68. Latent Aggregation 的最簡單版本

若所有 binary items 同質：

$$
\boxed{
\widehat q
=
\frac{1}{N}
\sum_i b_i.
}
$$

---

# 69. 但實際通常不夠

因為題目：

- 難度不同；
- 辨識力不同；
- 維度不同。

---

# 70. IRT-like Binary Model

可以寫：

$$
\boxed{
P(b_{rij}=1)
=
\sigma(
a_i\theta_j-d_i+\beta_r
).
}
$$

---

# 71. $\theta_j$

輸出 $j$ 的 latent quality。

---

# 72. $a_i$

題目對該品質的 discrimination。

---

# 73. $d_i$

題目 threshold / difficulty。

---

# 74. $\beta_r$

rater severity / leniency。

---

# 75. 這比把所有人的 Yes 直接平均更有表達力

---

# 76. Multidimensional Latent Quality

Human residual 通常不是一維。

令：

$$
\boxed{
\boldsymbol{\theta}_j
=
(
\theta_{\mathrm{clarity}},
\theta_{\mathrm{naturalness}},
\theta_{\mathrm{aesthetic}},
\theta_{\mathrm{impact}},
\ldots
).
}
$$

---

# 77. 每題 loading

$$
\boldsymbol{\lambda}_i.
$$

---

# 78. 則：

$$
\boxed{
P(b_{rij}=1)
=
\sigma(
\boldsymbol{\lambda}_i^\top
\boldsymbol{\theta}_j
-d_i+\beta_r
).
}
$$

---

# 79. 這就是從二元觀測回到多維品質空間

---

# 80. Context 也應進模型

同一作品在：

- 手機；
- 大螢幕；
- 專業使用；
- 娛樂使用；

可能品質不同。

---

# 81. 所以：

$$
\boxed{
\boldsymbol{\theta}_j
=
\boldsymbol{\theta}_j(c).
}
$$

---

# 82. 這直接延續 IBQF 的 context-conditioned field

---

# 83. Rater 也不是純噪音

不同人可能真的有：

$$
\boxed{
\text{different utility functions}.
}
$$

---

# 84. 所以：

$$
\beta_r
$$

只能表示某些系統性偏移，

不能把所有人差異都叫 bias。

---

# 85. Disagreement 結構

定義：

$$
\boxed{
\mathcal D_R
=
P(
Response
\mid
RaterGroup,
Context
).
}
$$

---

# 86. 若 disagreement 隨機

可能是 noise。

---

# 87. 若形成穩定群集

可能是：

- culture；
- expertise；
- usage goal；
- aesthetic school。

---

# 88. 所以：

$$
\boxed{
Disagreement
\neq
Error.
}
$$

---

# 89. 不要平均掉真正的多峰結構

假設：

Group A：

$$
P(A\succ B)=0.9.
$$

Group B：

$$
P(A\succ B)=0.1.
$$

---

# 90. 全部平均

$$
P(A\succ B)=0.5.
$$

會得到：

> 大家無所謂。

---

# 91. 但真相可能是

> 兩群人非常有意見，而且完全相反。

---

# 92. 所以：

$$
\boxed{
MeanPreference
\neq
PreferenceStructure.
}
$$

---

# 93. Blind Evaluation

若評審知道：

> 這是模型 X。

可能引入 brand / reputation effects。

---

# 94. 所以 human residual benchmark 應優先：

$$
\boxed{
BlindIdentity=1.
}
$$

在可行情況下。

---

# 95. Order Randomization

Pairwise A/B 左右位置要平衡。

---

# 96. Counterbalancing

同一 pair 可用：

$$
(A,B)
$$

和：

$$
(B,A)
$$

檢查 position bias。

---

# 97. Reversal Consistency

若：

$$
A\succ B
$$

但反轉位置後：

$$
B\succ A,
$$

可能存在：

- position bias；
- instability；
- low discrimination。

---

# 98. 可定義

$$
\boxed{
C_{\mathrm{rev}}
=
P(
\text{same preference}
\mid
\text{position reversed}
).
}
$$

---

# 99. 但重複太多也會造成記憶與疲勞

所以需要 adaptive design。

---

# 100. Adaptive Binary Measurement

不是固定問所有題。

---

# 101. 系統維持 posterior

$$
P(
\boldsymbol{\theta}
\mid
\mathcal H
).
$$

---

# 102. 對候選題 $i$

估計 expected information gain：

$$
\mathbb E[
IG_i
].
$$

---

# 103. 同時計入 human cost：

$$
C_H(i).
$$

---

# 104. 選：

$$
\boxed{
i^\*
=
\arg\max_i
\frac{
\mathbb E[IG_i]
}{
C_H(i)
}.
}
$$

---

# 105. 這是一種 Measurement Resource Rationality

$$
\boxed{
\text{information gained}
/
\text{human cognitive cost}.
}
$$

---

# 106. 這也符合 FDCS 的有效維度子空間思想

理論上可以問無限多題。

實務上只需問：

$$
\boxed{
D_{\mathrm{eff}}
}
$$

中最有辨識力的部分。

---

# 107. Stopping Rule

當 posterior uncertainty：

$$
U_H
$$

低於 threshold：

$$
\epsilon,
$$

即可停止。

---

# 108. 所以：

$$
\boxed{
N_{\mathrm{questions}}
}
$$

不是固定常數。

---

# 109. 難分的案例多問

容易分的案例少問。

---

# 110. 這比所有作品都叫 100 個人填 50 題更有效率

---

# 111. Pairwise Graph

把作品視為 nodes：

$$
V_Q.
$$

比較視為 edges：

$$
E_Q.
$$

---

# 112. 得到：

$$
\boxed{
G_Q=(V_Q,E_Q).
}
$$

---

# 113. 不必比較所有：

$$
O(n^2)
$$

pairs。

---

# 114. Adaptive pairing 可以優先比較：

- posterior 接近者；
- graph uncertainty 高者；
- ranking boundary 附近者。

---

# 115. 這可以大幅降低人類成本

---

# 116. 問題本身也需要校準

壞問題會產生壞測量。

---

# 117. Item Quality

可以建立：

$$
\boxed{
\mathfrak I_B
=
(
Discrimination,
Stability,
ContextSensitivity,
Burden,
BiasRisk
).
}
$$

---

# 118. 高 discrimination

能區分不同品質。

---

# 119. 高 stability

同一狀態下重測較一致。

---

# 120. 過度 context sensitivity

可能表示題目不是測我們想要的構念。

---

# 121. 高 burden

即使資訊量高，也未必划算。

---

# 122. 問題生成不是隨便問

Paper 08 會處理：

> 自然語言、圖像、創意到底該拆哪些 quality dimensions？

Paper 07 只固定 measurement protocol。

---

# 123. Observer Calibration Without Numbers

即使不要求 rater 打數字，

仍可估 rater reliability。

---

# 124. 方法包括

- repeated items；
- reversed pairs；
- known-dominance sentinel；
- cross-rater overlap。

---

# 125. 估：

$$
\boxed{
Rel_r.
}
$$

---

# 126. 但 reliability 也不能當 truthfulness

一個人可以非常一致地偏好某風格。

---

# 127. 所以：

$$
\boxed{
Reliability
\neq
Objectivity.
}
$$

---

# 128. Human Residual Quality 不是「人類說了算」

它是：

$$
\boxed{
\text{human perception evidence}.
}
$$

---

# 129. 如果任務是使用者體驗

那人類感知本身就是 outcome 的一部分。

---

# 130. 如果任務是數學真理

那人類偏好不能覆蓋 proof invalidity。

---

# 131. 所以 Hard Gate from Paper 06 保留

$$
\boxed{
G_H
}
$$

先過。

---

# 132. 再做人類 residual。

這避免：

> 一篇錯誤答案因為比較好讀就贏。

---

# 133. Quality Composition

完整品質：

$$
\boxed{
\mathfrak Q^{(7)}
=
(
\mathfrak Q_F,
\mathfrak Q_S,
\mathfrak Q_H^{IBQF}
).
}
$$

---

# 134. Formal / Structured 不被 Human Residual 抵消

這是 typed composition，

不是全部加權平均。

---

# 135. Scalar Projection 若真的需要

可以：

$$
\boxed{
Q^*
=
\Pi_Q(
\mathfrak Q^{(7)}
\mid
TaskPolicy
).
}
$$

---

# 136. 但 TaskPolicy 必須公開

例如：

1. hard gate first；
2. correctness primary；
3. clarity tie-breaker。

---

# 137. 這比：

> 總分 92.4

更可解釋。

---

# 138. Measurement Uncertainty

Latent estimate 應附：

$$
\Sigma_H
$$

或 credible interval。

---

# 139. 如果 A 和 B：

$$
q_A-q_B
$$

落在高不確定區，

就不應硬排名。

---

# 140. 所以：

$$
\boxed{
NoSignificantDifference
}
$$

也是合法結果。

---

# 141. 排名不是測量的必然終點

有時我們只需要：

- equivalent；
- better；
- uncertain。

---

# 142. Binary input 不代表 binary output

最後 posterior 可以非常豐富。

---

# 143. Human Evaluation Boundary

必須寫：

$$
\boxed{
B_H
=
(
Population,
Context,
TaskFrame,
PresentationMode
).
}
$$

---

# 144. 因為：

> 對誰而言品質高？

永遠是一個 measurement question。

---

# 145. 同一 AI 答案

對 expert：

$$
Q_H^{expert}
$$

和 novice：

$$
Q_H^{novice}
$$

可以不同。

---

# 146. 這不一定有誰錯

可能是：

$$
\boxed{
AudienceFit.
}
$$

---

# 147. Measurement Grade

本文提出 Human Residual Grade：

### H-Grade E — Uncontrolled Rating

少量非盲、直接總分。

---

# 148. H-Grade D — Structured Binary

有明確 binary items，但無 rater/item calibration。

---

# 149. H-Grade C — Balanced Comparative

盲測、randomized order、pairwise / binary balanced design。

---

# 150. H-Grade B — Psychometric Latent Model

估計 item difficulty、rater effects、posterior uncertainty。

---

# 151. H-Grade A — Adaptive + Replicated

adaptive sampling、跨 rater replication、holdout / reversal consistency。

---

# 152. H-Grade A+ — Cross-Context Validated

在不同 population/context 中驗證 measurement invariance，並明確保留 genuine preference heterogeneity。

---

# 153. Human Residual Object

$$
\boxed{
\mathfrak Q_H^{IBQF}
=
(
\widehat{\boldsymbol{\theta}}_H,
\Sigma_H,
N_{\mathrm{obs}},
\mathcal D_R,
\mathbf C_H,
B_H,
U_H,
Grade_H
).
}
$$

---

# 154. 這就是 Paper 07 的正式輸出

它不要求任何一個人回答：

> 你的品質分數是多少？

---

# 155. 每個人只提供：

$$
\boxed{
b_i.
}
$$

---

# 156. 系統才估：

$$
\boxed{
\widehat{\boldsymbol{\theta}}_H.
}
$$

---

# 157. 十二個 Canonical Invariants

**Invariant 1**

$$
\boxed{
BinaryObservation
\neq
BinaryPhenomenon.
}
$$

**Invariant 2**

$$
\boxed{
HumanObservation
\neq
HumanScaleConstruction.
}
$$

**Invariant 3**

$$
\boxed{
NumericRating
=
State
+
ScaleUse
+
Context.
}
$$

**Invariant 4**

$$
\boxed{
LocalJudgment
\neq
GlobalLatentScore.
}
$$

**Invariant 5**

$$
\boxed{
PairwisePreference
\neq
AbsoluteQuality.
}
$$

**Invariant 6**

$$
\boxed{
Skip
\neq
ThirdQualityValue.
}
$$

**Invariant 7**

$$
\boxed{
MeasurementBurden
\neq
MeasuredQuality.
}
$$

**Invariant 8**

$$
\boxed{
Disagreement
\neq
Error.
}
$$

**Invariant 9**

$$
\boxed{
MeanPreference
\neq
PreferenceStructure.
}
$$

**Invariant 10**

$$
\boxed{
Reliability
\neq
Objectivity.
}
$$

**Invariant 11**

$$
\boxed{
HumanResidual
\not\Rightarrow
HumanOverridesFormalTruth.
}
$$

**Invariant 12**

$$
\boxed{
BinaryInput
\not\Rightarrow
BinaryLatentOutput.
}
$$

---

# 158. 結論：把困難的量化工作從回答者身上拿回來

傳統量表最容易被忽略的一件事是：

$$
\boxed{
\text{measurement itself is a task}.
}
$$

當我們問：

> 0 到 10 分，你現在是多少？

我們不是只在「讀取」一個早就存在於人腦裡的數字。

很多時候，我們其實要求回答者當場建構那個數字。

他需要：

- 找參照；
- 建尺度；
- 整合多維感受；
- 做映射。

因此：

$$
\boxed{
\text{Observed Rating}
}
$$

同時混入了：

$$
\boxed{
\text{Target State}
+
\text{Measurement Cognition}.
}
$$

FDCS／IBQF 的微觀二元方法提供另一條路。

不要問：

> 你整體是多少分？

而是逐步取得：

$$
\boxed{
b_1,b_2,\ldots,b_N.
}
$$

每一個都盡量：

- 小；
- 具體；
- 局部；
- 容易回答。

再讓系統去完成：

$$
\boxed{
\{0,1\}^{N}
\rightarrow
\widehat{\boldsymbol{\theta}}.
}
$$

這不是因為世界是二元的。

而是因為：

$$
\boxed{
\textbf{
二元可以是測量介面，
連續與高維可以是被重建的現象。
}
}
$$

外部 psychometrics 的 forced-choice、pairwise comparison、Bradley–Terry、Thurstonian IRT 等工作也證明，這種「局部選擇 → latent scale」的測量路徑具有成熟數學傳統。

而 IPM 對它做的進一步擴張，是把這套方法專門用來承接：

$$
\boxed{
Q_H
}
$$

——也就是形式驗證與結構化核查之後，真正剩下的人類品質感知。

如此一來：

$$
\boxed{
\mathfrak P_{\mathrm{compute}}
\rightarrow
\mathbf N_{\mu}
\rightarrow
\mathfrak Q_F
\oplus
\mathfrak Q_S
\oplus
\mathfrak Q_H^{IBQF}.
}
$$

整個智能計量的「品質分子」已經不再依賴一個隨手打出的 8/10。

我們可以讓：

$$
\boxed{
\textbf{
評分者負責做容易的判斷；
測量系統負責做困難的量化。
}
}
$$

但下一個問題立即出現。

自然語言、圖片、設計、創意、音樂、故事等高歧義輸出，到底該拆成哪些 binary / pairwise dimensions？

如果維度本身選錯，

再好的 psychometric model 也只會：

> 精密地測量錯的東西。

因此 Paper 08 必須正式研究：

$$
\boxed{
\textbf{
高歧義成果如何先被結構化成可測的品質空間？
}
}
$$

也就是：

**《自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間》**。

---

## EveMissLab 內部理論來源

[EML-IBQF/MTF] Neo.K. (2025). *多維真與假：從向量到無限場的本體論革命*.  
核心：微觀二元事件 $\{0,1\}$ 與宏觀連續真值／高維場的湧現。

[EML-FDCS] Neo.K. (2025). *分形動態因果系統：超越反事實的因果推斷新範式*.  
核心：IBQF 作為三元場域中的主觀—客觀轉化機制，以大量微觀二元事件建立宏觀概率／因果結構。

[EML-IBQF-Clinical] Neo.K. (2025). *三元場域在心理治療評估中的應用：突破主觀評分的認知陷阱*.  
核心：以大量簡單是／否問題降低回答者的自我量化負擔，再由專業人士或 AI 系統綜合重建狀態。

---

## 外部文獻基礎

[1] Thurstone, L. L. (1927). A Law of Comparative Judgment. *Psychological Review*, 34, 273–286.  

[2] Bradley, R. A., & Terry, M. E. (1952). Rank Analysis of Incomplete Block Designs: I. The Method of Paired Comparisons. *Biometrika*, 39(3/4), 324–345.  

[3] Brown, A., & Maydeu-Olivares, A. (2013). How IRT Can Solve Problems of Ipsative Data in Forced-Choice Questionnaires. *Psychological Methods*, 18(1), 36–52.  

[4] Brown, A., & Maydeu-Olivares, A. (2012/2013). Fitting a Thurstonian IRT Model to Forced-Choice Data Using Mplus. *Behavior Research Methods*, 44, 1135–1147. DOI: 10.3758/s13428-012-0217-x.  

[5] Kreitchmann, R. S., Abad, F. J., Ponsoda, V., Nieto, M. D., & Morillo, D. (2019). Controlling for Response Biases in Self-Report Scales: Forced-Choice vs. Psychometric Modeling of Likert Items. *Frontiers in Psychology*, 10, 2309. DOI: 10.3389/fpsyg.2019.02309.  

[6] Clark, A. P., Howard, K. L., Woods, A., Penton-Voak, I. S., & Neumann, C. (2018). Why Rate When You Could Compare? Using the EloChoice Package to Assess Pairwise Comparisons of Perceived Physical Strength. *PLOS ONE*, 13(1), e0190393. DOI: 10.1371/journal.pone.0190393.  

[7] Joo, S.-H., Lee, P., & Stark, S. (2019/2020). Adaptive Testing with the GGUM-RANK Multidimensional Forced Choice Model: Comparison of Pair, Triplet, and Tetrad Scoring. *Behavior Research Methods*.  

---

## 系列路徑

1. **Paper 01｜一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義**  
2. **Paper 02｜智能到底算了一次什麼？：最小智能語意執行單位的候選理論**  
3. **Paper 03｜從認知到神經元：人腦如何跨層測量智能計算**  
4. **Paper 04｜從神經元到焦耳：智能計算的能量、熱力學與物理下界**  
5. **Paper 05｜計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積**  
6. **Paper 06｜成果品質到底怎麼量？：從形式化正確性到結構化智能品質**  
7. **Paper 07｜不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估**  
8. **Paper 08｜自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間**  
9. **Paper 09｜拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本**  
10. **Paper 10｜一個答案值多少物理世界？：智能產率的統一計量框架**
