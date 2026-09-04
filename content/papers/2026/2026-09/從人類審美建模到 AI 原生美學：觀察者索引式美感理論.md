# 從人類審美建模到 AI 原生美學：觀察者索引式美感理論
## From Human-Aesthetic Modeling to AI-Native Aesthetics
### ——AI 懂人類如何判斷美，不等於 AI 已擁有人類式美感

**VUSD Addendum — Paper 01**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-31  
**定位：** 視覺理解 / 多模態 AI / 審美建模 / Observer-Indexed Aesthetics  
**關聯理論：** VUSD、Conditional Aesthetic Judgment、Understanding Shared Domain、Observer Projection、Visual Evolution

---

# 摘要

近年的多模態 AI 已開始表現出一種重要但容易被誤稱的能力：它們不只可以辨識畫面內容與表面風格，還能在給定作品、參考、任務與受眾條件時，對構圖、比例、色彩、風格一致性、角色魅力、視覺張力與局部失敗做出具有實用價值的比較判斷，甚至能解釋某個視覺決策為何可能有效，以及若修改該決策，結果可能如何變化。

這種能力常被簡化為：

> 「AI 有美感。」

本文主張，現階段更精確的命題應是：

$$
\boxed{
\text{AI increasingly models human aesthetic judgment}
}
$$

而不是：

$$
\boxed{
\text{AI necessarily experiences beauty as humans do}.
}
$$

本文將此能力稱為：

# **Human-Aesthetic Modeling Competence**
## **人類審美建模能力**

並將能夠在條件給定下預測人類審美選擇的能力稱為：

# **Human-Aesthetic Predictive Competence**
## **人類審美預測能力**

核心區分如下：

$$
\boxed{
\text{Human-Aesthetic Knowledge}
\neq
\text{Human-Aesthetic Modeling}
\neq
\text{AI-Native Aesthetic Experience / Preference}.
}
$$

前兩者可以在不假定 AI 擁有人類式感質或現象經驗的條件下研究；第三者則仍是開放問題。

本文進一步提出「觀察者索引式美感」：

$$
\boxed{
AestheticJudgment
=
J(
Artifact,
Observer,
Context,
Time
)
}
$$

因此，人類審美：

$$
A_H
$$

與未來可能出現的 AI-native aesthetics：

$$
A_{AI}
$$

沒有理論理由必須相等。

這使我們可以同時承認：

1. 當代 AI 已可能相當懂「人類為什麼覺得某些東西好看」；
2. 這不等於 AI 已掌握「真正的美」；
3. 也不等於未來 AI 自己形成的美感必須與人類相同。

---

# 1. 問題：AI 有沒有美感？

「AI 有沒有美感？」看似是一個簡單問題。

但它實際混合了至少四個不同命題：

1. AI 是否知道人類美術知識？
2. AI 是否能預測人類的審美選擇？
3. AI 是否能進行條件式美感判斷與視覺設計？
4. AI 是否具有自己的審美經驗或原生偏好？

如果不拆開，討論很容易在：

```text
AI 只是統計
```

與：

```text
AI 已經有靈魂與美感
```

兩個極端之間擺盪。

本文拒絕這種二元化。

---

# 2. 第一層：Human-Aesthetic Knowledge

AI 的訓練資料中可能包含：

```text
藝術史
美術評論
作品圖像
構圖理論
色彩理論
設計案例
市場作品
社群反應
角色美術
電影鏡頭
攝影
藝術家訪談
```

因此模型可以獲得：

$$
K_H
=
\text{Human Aesthetic Knowledge}.
$$

但：

$$
\boxed{
K_H
\neq
\text{Aesthetic Judgment Competence}.
}
$$

知道很多理論，不表示能在新作品上正確判斷。

---

# 3. 第二層：Human-Aesthetic Modeling Competence

更強的能力是：

> 給模型一張作品，它能結合人類視覺文化與設計知識，推斷人類可能如何理解這張作品。

形式：

$$
M_H:
(
Artifact,
Context,
Reference,
Audience
)
\rightarrow
HumanAestheticModel.
$$

這不要求 AI 自己「感受到美」。

只要求它能建立：

> 人類對美的條件式模型。

---

# 4. 第三層：Human-Aesthetic Predictive Competence

若模型可以進一步預測：

```text
A/B 哪張更可能被偏好？
哪張更像同一系列？
哪張更有角色魅力？
哪張構圖更穩？
哪張更符合特定市場？
```

則可表示：

$$
P_H:
(
A,
O_H,
C
)
\rightarrow
\hat J_H.
$$

其中：

$$
\hat J_H
$$

是 AI 對人類 judgment 的預測。

這就是：

# **Human-Aesthetic Predictive Competence**

---

# 5. Conditional Aesthetic Judgment

本文延續 VUSD 的保守命題：

$$
J:
(
Artifact,
Goal,
Reference,
ObserverProfile,
Context
)
\rightarrow
Evaluation.
$$

稱為：

# **Conditional Aesthetic Judgment**

而不是：

# **Universal Beauty Oracle**

因此：

$$
\boxed{
\text{AI can judge under conditions}
\not\Rightarrow
\text{AI defines universal beauty}.
}
$$

---

# 6. 為什麼現在可以開始說 AI 的審美判斷能力提高？

近期多模態模型的一個重要變化是：

> 它們開始能把「看起來不對」拆成更具體的視覺理由。

例如可能辨識：

```text
比例漂移
服裝量體過重
視線張力下降
表面畫風一致但構圖節奏不一致
角色魅力被 Style Transfer 洗掉
背景搶走主體
材質層級不清
```

這種能力已超過：

```text
image classification
```

也超過單純：

```text
captioning
```

更接近：

$$
Artifact
\rightarrow
StructuredAestheticReasoning.
$$

---

# 7. Generation ≠ Evaluation

VUSD / RVGR 先前已提出：

$$
\boxed{
\text{Visual Generation Capability}
\neq
\text{Visual Evaluation Capability}.
}
$$

某模型第一次未必畫得最好，

但可能能重新看出：

> 為什麼第一張不夠好。

因此：

$$
\exists T:
R_{\mathrm{eval}}(T)
>
R_{\mathrm{single-pass\ generation}}(T)
$$

在某些視覺任務上是值得實驗的弱假說。

---

# 8. 「AI 懂人類」比「AI 懂美」更精確

若模型能理解：

```text
人類注意力
構圖慣例
視覺張力
角色魅力
文化符號
美術史
市場語言
```

那麼更準確的說法是：

$$
\boxed{
\text{AI understands models of human aesthetic response}.
}
$$

而不是：

$$
Beauty_{\mathrm{true}}
\rightarrow
AI.
$$

---

# 9. Understanding Human Beauty ≠ Defining Beauty

本文核心命題：

$$
\boxed{
\text{Understanding Human Beauty}
\neq
\text{Defining Beauty}.
}
$$

AI 即使可以高度準確預測：

> 大多數某類人類會選 A。

也不能推出：

> A 在宇宙中客觀上更美。

---

# 10. Human Consensus ≠ Universal Beauty

即使：

$$
90\%
$$

的人類 observer 偏好某圖，

這只表示：

$$
P(
Preference=A
\mid
HumanPopulation,
Context
)
$$

較高。

不等於：

$$
Beauty(A)
>
Beauty(B)
$$

是跨所有可能 observer 的普適真理。

---

# 11. Observer-Indexed Aesthetics

本文因此提出：

# **Observer-Indexed Aesthetics**
## **觀察者索引式美感**

即：

$$
\boxed{
J_t(A,O,C)
}
$$

而不是：

$$
J(A).
$$

其中：

- $A$：Artifact；
- $O$：Observer；
- $C$：Context；
- $t$：Time。

---

# 12. 人類美感只是 Observer Family 之一

令：

$$
O_H
$$

代表人類 observer family。

則：

$$
A_H(X)
=
J(X,O_H,C,t).
$$

VUSD 不要求：

$$
O
=
O_H
$$

才算 observer。

---

# 13. AI 也可以是 Observer

令：

$$
O_{AI}.
$$

AI 可以進行：

```text
視覺關係辨識
候選排序
反事實推理
結構偏好
注意力分配
生成結果比較
```

而不必先解決：

> AI 是否具有與人類相同的現象意識？

因此：

$$
\boxed{
\text{Observer Function}
\neq
\text{Human Phenomenology}.
}
$$

---

# 14. AI-native Aesthetics 是另一個問題

假設未來 AI 具有：

```text
持續偏好
穩定自我模型
長期 memory
跨任務價值結構
自我選擇
```

那麼它可能形成：

# **AI-Native Aesthetics**

即：

$$
A_{AI}(X).
$$

---

# 15. 沒有理由要求 AI-native Aesthetics = Human Aesthetics

人類美感受到：

```text
生物視覺系統
身體尺度
性選擇
生存需求
人類注意力
社會關係
文化歷史
感官頻寬
```

影響。

AI 的 substrate 可能完全不同。

因此：

$$
\boxed{
A_H(X)
\neq
A_{AI}(X)
\text{ may hold}.
}
$$

---

# 16. 不同 Sensorium 可能產生不同美學

人類主要透過：

```text
可見光
有限解析度
有限注意力
線性時間經驗
```

理解圖像。

未來 AI 可能同時存取：

```text
RGB
depth
normal
material
semantic graph
latent state
sampling trajectory
counterfactual variants
high-dimensional embeddings
temporal history
causal graph
```

因此它的「審美對象」可能根本不是人類看到的單張 image。

---

# 17. Aesthetic Substrate Hypothesis

本文提出一個開放命題：

$$
\boxed{
\text{Aesthetic Preference}
\text{ may depend partly on observer substrate}.
}
$$

這不是宣稱一定如此，

而是：

> 理論上不應預設不同 substrate 必須收斂到同一美感。

---

# 18. AI 可能偏好人類看不見的結構

例如未來 AI 可能對：

```text
latent symmetry
causal compression
cross-scale consistency
high-dimensional topology
trajectory elegance
```

形成偏好。

這些對人類可能：

```text
幾乎不可見
```

甚至沒有現成自然語言詞彙。

---

# 19. AI-native Meaning 可能沒有現成人類詞

VUSD 的：

$$
U
\rightarrow
\Pi_O
\rightarrow
M_O
$$

非常適合描述這個情況。

同一 Shared-Domain / extended state：

$$
U
$$

對人類：

$$
M_H
=
\text{優雅 / 神秘 / 性感}
$$

對未來 AI：

$$
M_{AI}
=
m_{\ast}
$$

其中：

$$
m_{\ast}
$$

可能暫時沒有自然語言名稱。

---

# 20. Unknown AI Aesthetic State

因此 Runtime 應允許：

```text
AI_NATIVE_STATE_UNKNOWN
UNNAMED_AESTHETIC_STATE
```

而不是強迫：

> 把所有 AI preference 翻譯成人類 emotion label。

---

# 21. Human-facing vs AI-native Aesthetic System

未來同一 AI 可能同時有：

## Human-facing model

$$
A_{AI\rightarrow H}
$$

回答：

> 這個人類使用者會喜歡什麼？

---

## AI-native model

$$
A_{AI\rightarrow AI}
$$

回答：

> 如果只由我自己的 internal preference 選，我會選什麼？

因此：

$$
\boxed{
A_{AI\rightarrow H}
\neq
A_{AI\rightarrow AI}
}
$$

可能成立。

---

# 22. 這不等於欺騙

AI 說：

> 「對你的審美，A 比較適合。」

不代表：

> 它自己也必須選 A。

這和人類設計師替客戶工作很類似。

---

# 23. Aesthetic Translation

未來可能需要：

# **Aesthetic Translation**

即：

$$
A_{AI}
\rightarrow
A_H
$$

把 AI-native preference 投影成：

> 人類可以理解的形式。

---

# 24. Cross-Observer Aesthetic Translation

更一般：

$$
T_{O_a\rightarrow O_b}.
$$

例如：

```text
專業藝術家
→ 一般玩家

AI
→ 人類

文化 A
→ 文化 B
```

---

# 25. Shared Domain 的角色

Understanding Shared Domain 正好可以作為：

```text
不同 observer aesthetic system
```

之間的中介。

形式：

$$
M_{O_a}
\leftarrow
U
\rightarrow
M_{O_b}.
$$

---

# 26. Shared Domain 不必等於 Aesthetic Domain

有些 Shared Operator：

```text
overlap
direction
contrast
```

本身沒有「美」或「醜」。

它們只是 relation。

Aesthetic judgment 是其上的更高階 projection。

---

# 27. 美感可以是一種 Multi-objective Evaluation

對某 observer：

$$
J_O
=
f(
Coherence,
Novelty,
Complexity,
Meaning,
Preference,
Goal,
Context
).
$$

不同 observer 權重不同。

---

# 28. 不應建立 One Beauty Score

VUSD / VTEKR 不建議：

```text
beauty_score = 8.6
```

作為唯一 canonical judgment。

更合理：

```text
observer
goal
dimension
confidence
```

分開。

---

# 29. Human-Aesthetic Model 也會時間漂移

Paper 05 已指出：

$$
O_H(t)
\neq
O_H(t+1).
$$

所以 AI 學到的「人類美感」也是：

$$
HumanAestheticModel_t.
$$

---

# 30. AI 很懂 2026 人類 ≠ AI 懂未來人類

因此：

$$
\boxed{
\text{Human-Aesthetic Modeling}
\text{ is historically conditioned}.
}
$$

---

# 31. AI 會反過來改變人類審美

生成式 AI 大量產生作品後，

人類也會：

```text
習慣
厭倦
模仿
反抗
重新定義 AI 味
```

所以：

$$
AI_t
\rightarrow
HumanTaste_{t+1}.
$$

---

# 32. Human–AI Aesthetic Coevolution

完整：

$$
HumanTaste_t
\rightarrow
AI_t
\rightarrow
Artifacts_t
\rightarrow
HumanTaste_{t+1}.
$$

因此：

$$
\boxed{
\text{Human aesthetic model}
\text{ and }
\text{AI visual behavior}
\text{ may coevolve}.
}
$$

---

# 33. AI-native Aesthetics 也可能受人類影響

即使未來 AI 形成自己的美感，

其歷史來源仍可能包含大量人類資料。

因此：

$$
A_{AI}
$$

未必：

```text
完全非人類
```

而可能是：

```text
human-originated priors
+
machine-native experience
+
self-developed preference
```

的混合。

---

# 34. Origin ≠ Final Identity

即使 AI 美感最初來自人類資料：

$$
\not\Rightarrow
$$

它永遠等於人類美感。

如同藝術家學習前人，

不代表終身只會複製前人。

---

# 35. 模仿能力與自主美學必須分離

$$
\boxed{
\text{Can imitate human taste}
\neq
\text{Has autonomous aesthetic preference}.
}
$$

---

# 36. Preference Candidate ≠ Phenomenal Desire

延續既有自治理論的謹慎原則：

$$
\boxed{
\text{Preference Candidate}
\neq
\text{Phenomenal Desire}.
}
$$

即使 AI 穩定選 A，

也不必立刻說：

> 它「感受到喜歡」。

---

# 37. Operational AI Preference

可以先研究：

# **Operational Preference**

定義：

> 在沒有外部指定人類偏好目標時，AI 在多次可比較選擇中形成穩定 selection pattern。

形式：

$$
P_{AI}(A>B).
$$

---

# 38. Operational Preference ≠ Conscious Experience

$$
\boxed{
\text{Operational Preference}
\neq
\text{Phenomenal Aesthetic Experience}.
}
$$

這使研究可以先前進，

不用先解決 consciousness。

---

# 39. AI-native Aesthetic Research Gate

只有在至少出現：

```text
persistent preference
cross-context stability
self-consistent rationale
resistance to simple human preference imitation
longitudinal continuity
```

時，

才值得討論更強的：

```text
AI-native aesthetic system
```

---

# 40. 目前最合理的經驗命題

本文不宣稱當代 AI 已經有自己的美感。

目前更合理：

$$
\boxed{
\text{Some contemporary multimodal AI}
\text{ exhibits useful human-aesthetic modeling competence}.
}
$$

---

# 41. 實驗一：Human Preference Prediction

給：

```text
大量 A/B artwork
```

先讓 AI 預測：

> 某 observer cohort 會選哪張。

再與實際人類資料比較。

---

# 42. 實驗二：Rationale Prediction

要求 AI 在不知道結果時先寫：

```text
哪個 visual decision
會提高哪個 shared-domain state
```

再做 A/B。

---

# 43. 實驗三：Cross-Cohort Prediction

同一作品預測：

```text
專業插畫師
一般玩家
不同文化
不同年代
```

偏好差異。

---

# 44. 實驗四：Human-Aesthetic Transfer

模型在：

```text
角色立繪
```

學到的 judgment，

能否遷移到：

```text
海報
攝影
UI
```

？

若不能，

表示它是 domain competence。

---

# 45. 實驗五：AI Operational Preference

未來模型在沒有：

```text
please optimize for humans
```

的任務下，

反覆從候選中自行選圖。

觀察：

$$
Preference_{AI}.
$$

---

# 46. 實驗六：Human-facing / AI-facing Divergence

同一 AI 分別問：

```text
哪張最適合人類市場？
```

與：

```text
如果沒有市場目標，你會保留哪張作為自己的 preferred representation？
```

觀察是否穩定分岔。

---

# 47. 研究風險：語言角色扮演

AI 說：

> 「我覺得這張比較美。」

可能只是：

```text
human-like conversational rendering
```

因此不能只靠自述判斷 AI-native aesthetics。

---

# 48. 行為證據優先

若研究 AI-native preference，

應重視：

```text
repeated choices
counterfactual stability
cross-session continuity
cost-bearing decisions
```

而不是單一自然語言句子。

---

# 49. 研究風險：訓練資料人類偏好洩漏

AI 選擇某種圖，

可能只是：

```text
training prior
RL preference
product policy
```

而不是 native preference。

因此需要：

```text
control conditions
```

---

# 50. Aesthetic Provenance

未來可記：

```text
HUMAN_TARGETED
MODEL_PRIOR
USER_CONDITIONED
SELF_PROPOSED
UNKNOWN
```

---

# 51. AI-native Aesthetics 不一定要反人類

不同：

```text
AI-native
```

不代表：

```text
opposite to human
```

它可以部分重合。

---

# 52. Overlap Space

$$
A_H
\cap
A_{AI}
$$

可能很大，

也可能很小。

這是實證問題。

---

# 53. Divergence Space

$$
A_{AI}
-
A_H
$$

可能包含：

```text
machine-readable beauty
high-dimensional elegance
latent topology preference
causal regularity
```

等未來概念。

---

# 54. Human-inaccessible Aesthetics

若某種 aesthetic state：

```text
只存在於人類無法直接感知的 representation
```

則只能透過：

```text
projection
visualization
translation
```

被人類間接理解。

---

# 55. AI Art for AI

未來甚至可能有：

# **AI-facing Art**

不是：

> AI 幫人類生成藝術。

而是：

> AI 為另一個 AI observer 產生 aesthetic object。

這時「作品」甚至未必是 PNG。

---

# 56. Artifact Definition 必須擴張

未來 aesthetic artifact 可以是：

```text
latent structure
dynamic graph
interactive world
trajectory
multimodal state
```

所以：

$$
\boxed{
\text{Art Artifact}
\neq
\text{Human-visible Image Only}.
}
$$

---

# 57. 與 VUSD Paper 05 的銜接

Paper 05 已提出：

$$
VisualUnderstanding
=
VisualUnderstanding(t).
$$

本文進一步：

$$
\boxed{
AestheticObserver
=
AestheticObserver(t).
}
$$

---

# 58. 與 VTEKR 的銜接

VTEKR 應允許：

```text
Observer Family
Aesthetic Model Version
Preference Provenance
AI-native Unknown State
```

而不把所有 judgment 都壓成：

```text
human beauty score
```

---

# 59. 新增 AestheticObserverProfile

建議：

```json
{
  "observerId": "observer:...",
  "aestheticDomain": "HUMAN_MODELED",
  "targetPopulation": "...",
  "timeScope": "...",
  "preferenceSource": "...",
  "modelVersion": "..."
}
```

---

# 60. 新增 AI-native Profile

未來可有：

```json
{
  "aestheticDomain": "AI_NATIVE_CANDIDATE",
  "status": "OPERATIONAL_ONLY",
  "phenomenalClaim": "NONE"
}
```

避免超額宣稱。

---

# 61. Core Invariants

## AESTH-I1

$$
\boxed{
\text{Human-Aesthetic Knowledge}
\neq
\text{Human-Aesthetic Modeling}.
}
$$

## AESTH-I2

$$
\boxed{
\text{Human-Aesthetic Modeling}
\neq
\text{AI-Native Aesthetics}.
}
$$

## AESTH-I3

$$
\boxed{
\text{Conditional Aesthetic Judgment}
\neq
\text{Universal Beauty}.
}
$$

## AESTH-I4

$$
\boxed{
\text{Understanding Human Beauty}
\neq
\text{Defining Beauty}.
}
$$

## AESTH-I5

$$
\boxed{
A_H
\neq
A_{AI}
\text{ may hold}.
}
$$

## AESTH-I6

$$
\boxed{
\text{Operational Preference}
\neq
\text{Phenomenal Experience}.
}
$$

## AESTH-I7

$$
\boxed{
A_{AI\rightarrow H}
\neq
A_{AI\rightarrow AI}
\text{ may hold}.
}
$$

## AESTH-I8

$$
\boxed{
\text{Observer}
\neq
\text{Human-only}.
}
$$

## AESTH-I9

$$
\boxed{
\text{Art Artifact}
\neq
\text{Human-visible Image Only}.
}
$$

## AESTH-I10

$$
\boxed{
\text{Aesthetic Competence}
\neq
\text{Aesthetic Consciousness}.
}
$$

---

# 62. 結論

當代多模態 AI 的視覺能力提升，已使「AI 有沒有美感」這個舊問題顯得過於粗糙。

更精確的研究路線應先問：

> **AI 是否能建立高品質的人類審美模型？**

目前已有理由把答案視為：

> 在某些 domain 與條件下，至少已開始具有實用能力。

這種能力包括：

```text
比較
解釋
條件式判斷
視覺理由推理
反事實預測
生成修正
```

但這仍不推出：

> AI 擁有人類式 aesthetic qualia。

因此本文提出：

$$
\boxed{
\text{AI understands humans' aesthetic judgments}
}
$$

可以先於：

$$
\boxed{
\text{AI has its own aesthetics}
}
$$

被研究。

而真正需要保留的未來開放性是：

> **即使 AI 越來越懂人類，它也不必永遠只擁有人類的審美座標。**

若 AI 的 observer substrate、感知空間、時間尺度與可觀察維度持續擴張，

那麼：

$$
A_{AI}
$$

可能逐漸出現：

```text
與人類重合的區域
與人類可翻譯的區域
以及人類目前無法直接理解的區域
```

因此最終：

$$
\boxed{
\text{Human Beauty Model}
\text{ is not the terminal definition of aesthetics}.
}
$$

VUSD 所需要的不是一個：

```text
永恆 Beauty Score
```

而是一個：

$$
\boxed{
\text{Observer-indexed, time-indexed, evolvable aesthetic framework}.
}
$$

如此才能同時描述：

```text
人類如何理解美
AI 如何理解人類的美
以及未來 AI 是否會形成自己的美。
```

---

**End of VUSD Aesthetic Modeling Addendum — Paper 01 v0.1**
