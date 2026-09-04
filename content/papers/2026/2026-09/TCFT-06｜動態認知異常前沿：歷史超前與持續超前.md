---
title: "TCFT-06｜動態認知異常前沿：歷史超前與持續超前"
title_en: "Dynamic Cognitive Anomaly Frontiers: Historical Advancement and Persistent Frontier Position"
series: "Temporal Cognitive Frontier Theory (TCFT) / 時代認知前沿理論"
paper_no: "06"
version: "v0.1"
date: "2026-08-31"
author: "Neo.K"
affiliation: "EveMissLab / 一言諾科技有限公司"
document_type: "理論論文 / Dynamic Frontier 篇"
language: "zh-Hant"
status: "正式系列初稿"
previous_paper: "TCFT-05｜時間正規化新穎度：Frozen-Time Prior Art 與同期認知基準"
next_paper: "TCFT-07｜原生認知超前：從新答案到 Operator、Program 與 Domain Seed"
---

# TCFT-06｜動態認知異常前沿：歷史超前與持續超前

## Dynamic Cognitive Anomaly Frontiers: Historical Advancement and Persistent Frontier Position

**系列：** Temporal Cognitive Frontier Theory, TCFT / 時代認知前沿理論  
**篇次：** 06  
**版本：** v0.1  
**日期：** 2026-08-31  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  

---

## 摘要

TCFT-05 已建立時間正規化新穎度與 Frozen-Time Prior-Art Audit，使「某個輸出在當時是否真的超前」能被轉寫為相對同期知識、工具、版本、prior art 與強基準之殘差問題。然而，一個新的問題隨即出現：**如果整個時代也在前進，那麼某個曾經高度異常的認知主體、作品或方法，是否仍然異常？**

本文提出 **Dynamic Cognitive Anomaly Frontier（動態認知異常前沿，DCAF）**，將 TCFT 的歷史超前從靜態評價轉成時間索引的相對位置問題。核心不是建立永久排行榜，而是追蹤：

$$
\boxed{
\text{agent / artifact capability}
-
\text{contemporaneous baseline}
}
$$

如何隨時間變化。

令主體 $i$ 在時間 $t$ 的多維認知向量為：

$$
\boxed{
\mathbf C_i(t)
=
(
C_i^{BS},
C_i^{CF},
C_i^{RR},
C_i^{RG},
C_i^{TN},
C_i^{PG},
C_i^{RP},
C_i^{DP},
\ldots
),
}
$$

其中可包含 Future Base-Space、Counterfactual Horizon、Reflexive Reasoning、Reasoning Governance、Time-Normalized Novelty、Problem Generation、Representation / Program Advancement 與 Domain-Seed Potential 等維度。令同期強基準為：

$$
\boxed{
\mathbf B(t).
}
$$

則認知前沿 gap 候選為：

$$
\boxed{
\mathbf G_i(t)
=
\mathbf C_i(t)
-
\mathbf B(t).
}
$$

這裡的減號表示經正規化後的相對位置，不假設所有能力能直接使用原始量綱相減。

最重要的動態關係是：

$$
\boxed{
\Delta \mathbf G_i
=
\Delta \mathbf C_i
-
\Delta \mathbf B.
}
$$

如果時代基準前進速度高於主體：

$$
\Delta \mathbf B
>
\Delta \mathbf C_i,
$$

則 gap 收縮；若主體與時代同步，gap 可維持；若主體自身前進更快，則 gap 擴張。由此本文區分：

$$
\boxed{
\text{Historical Anomaly}
\neq
\text{Current Anomaly}
\neq
\text{Persistent Frontier}.
}
$$

此外，本文再做一個必要分離：

$$
\boxed{
\text{Artifact Persistence}
\neq
\text{Agent Persistence}.
}
$$

一篇 1500 年作品今天仍含尚未被完全吸收的結構，屬於 artifact persistence；同一作者若活到今天且仍持續產生位於前沿的新結構，才是 agent persistence。相反地，一個人可以在早期極端超前，之後停止產生新前沿；其 Historical Anomaly 仍成立，但 Current Anomaly 可下降。

本文提出 **Frontier Absorption、Frontier Decay、Frontier Renewal、Frontier Escape、Persistent Frontier Anomaly** 與 **Frontier Half-Life** 等候選概念。當原本異常的知識被教育、工具、AI、制度與公共基礎設施吸收：

$$
\boxed{
\mathbf B(t)
\rightarrow
\mathbf C_i(t_0),
}
$$

原歷史成果的 current anomaly 會下降，但 historical anomaly 不應被回溯抹除。這形成：

$$
\boxed{
\text{Absorption}
\neq
\text{Retroactive De-Novelization}.
}
$$

本文同時拒絕固定單一總分。認知能力高度多維且相關，故可以使用每維 time-normalized z-score、robust score、Mahalanobis distance 等統計量估計「距離同期分布中心多遠」，但任何多變量距離都不應取代維度向量本身。對「誰在前沿」問題，本文偏好以 Pareto frontier 表示：

$$
\boxed{
\mathcal F_t
=
\left\{
i:
\nexists j
\text{ such that }
\mathbf C_j(t)
\succeq
\mathbf C_i(t)
\text{ with strict improvement in at least one dimension}
\right\}.
}
$$

因此沒有必要存在唯一：

$$
\boxed{
\text{Champion}.
}
$$

一個 agent 可在 counterfactual breadth 位於前沿，另一個在 strategic stopping，第三個在 representation novelty。這比把多維能力硬壓成「誰最聰明」更符合 TCFT。

本文借用 concept drift 與 continuously updated benchmark 的方法學精神：當資料分布、能力分布與測試基準持續變化，固定 benchmark 會逐漸失真。現代 AI benchmark 如 LiveBench 之所以持續更新題目，正是因為能力進步與 contamination 會使靜態測試失去區辨力。TCFT 不把人類歷史比較等同 machine-learning benchmark，但採用相同的動態警告：

$$
\boxed{
\text{A static baseline cannot fairly evaluate a moving frontier indefinitely.}
}
$$

本文最後提出 **Dynamic Frontier Ledger**：所有異常判斷應保存被評主體／作品、時間、baseline version、metrics、prior-art state、confidence 與更新理由，使前沿位置可上升、下降、被吸收或重新出現。

本文中心命題為：

$$
\boxed{
\text{Temporal cognitive anomaly is not a permanent identity;
it is a time-indexed relation between a cognitive structure
and a moving contemporaneous frontier.}
}
$$

**關鍵詞：** 動態認知異常前沿、歷史超前、持續超前、Persistent Frontier、Frontier Absorption、Pareto frontier、Mahalanobis distance、concept drift、動態基準、TCFT

---

# Abstract

TCFT-05 introduced time-normalized novelty and frozen-time prior-art auditing, allowing claims of historical advancement to be evaluated relative to contemporaneous knowledge, tools, provenance, prior art, and strong baselines. A further problem immediately follows: if the surrounding era also advances, does a once-anomalous person, artifact, theory, or cognitive program remain anomalous?

This paper introduces the **Dynamic Cognitive Anomaly Frontier (DCAF)**. Rather than constructing a permanent ranking, DCAF tracks the time-indexed relation between an agent or artifact and a moving contemporaneous baseline.

Let the multidimensional cognitive vector of agent $i$ at time $t$ be $\mathbf C_i(t)$, and let the contemporaneous strong baseline be $\mathbf B(t)$. We define a candidate frontier gap:

$$
\boxed{
\mathbf G_i(t)
=
\mathbf C_i(t)
-
\mathbf B(t).
}
$$

The key dynamic relation is:

$$
\boxed{
\Delta \mathbf G_i
=
\Delta \mathbf C_i
-
\Delta \mathbf B.
}
$$

If the baseline advances faster than the agent, the gap shrinks; if both advance at similar rates, the gap persists; if the agent advances faster, the gap expands.

The paper distinguishes Historical Anomaly, Current Anomaly, and Persistent Frontier position. It further separates **Artifact Persistence** from **Agent Persistence**. A historical artifact may remain structurally unusual centuries later even if its author is no longer an active agent; conversely, an agent may have been historically anomalous but no longer occupy a current frontier.

We introduce Frontier Absorption, Frontier Decay, Frontier Renewal, Frontier Escape, Persistent Frontier Anomaly, and Frontier Half-Life. Importantly, when society absorbs an earlier cognitive advance into education, institutions, tools, or AI systems, the current anomaly of the artifact declines but its historical anomaly is not retroactively erased.

Because cognitive advancement is multidimensional, DCAF rejects a single permanent score. Time-normalized component scores, robust anomaly measures, Mahalanobis distance, and related multivariate statistics may be used as audit tools, but Pareto frontiers are preferred for representing multiple non-dominated cognitive profiles without requiring a unique champion.

Drawing methodological inspiration from concept-drift research and continuously updated AI benchmarks, we argue that static baselines become unreliable under rapidly changing capability distributions. The central proposition is:

$$
\boxed{
\text{Temporal cognitive anomaly is not a permanent identity;
it is a time-indexed relation between a cognitive structure
and a moving contemporaneous frontier.}
}
$$

**Keywords:** dynamic cognitive anomaly frontier; historical advancement; persistent frontier; frontier absorption; Pareto frontier; Mahalanobis distance; concept drift; dynamic benchmark; TCFT

---

# 1. 導論：如果世界追上來了，超前還存在嗎？

假設某人在：

$$
t_0
$$

提出：

$$
x.
$$

相對同期 baseline：

$$
B_{t_0},
$$

它非常異常：

$$
N^{TN}(x,t_0)\gg0.
$$

到了：

$$
t_1,
$$

所有學生都會：

$$
x.
$$

那麼該怎麼說？

---

# 2. 兩個直覺都可能錯

第一種錯誤：

> 現在大家都會，所以他當年也沒什麼。

這把：

$$
B_{t_1}
$$

偷渡回：

$$
t_0.
$$

第二種錯誤：

> 他當年很超前，所以今天仍然比所有人超前。

這又把：

$$
B_{t_0}
$$

永久凍結。

因此：

$$
\boxed{
\text{Historical Position}
\neq
\text{Current Position}.
}
$$

---

# 3. Dynamic Baseline Principle

TCFT-06 的第一原則：

$$
\boxed{
\mathbf B(t)
\text{ must be allowed to move}.
}
$$

baseline 會因：

- education；
- publication；
- technology；
- AI；
- institutional learning；
- data；
- computing；
- search；
- diffusion；

而改變。

---

# 4. Static Baseline Failure

若永久使用：

$$
B_{t_0},
$$

所有早期高手都會永遠高分。

如果永久使用：

$$
B_{today},
$$

所有歷史高手都可能被現代常識淹沒。

兩者都不對。

---

# 5. Cognitive Vector

令 agent $i$ 在時間 $t$ 的能力／輸出向量：

$$
\boxed{
\mathbf C_i(t)
=
(
C_i^{BS},
C_i^{CF},
C_i^{RR},
C_i^{RG},
C_i^{TN},
C_i^{PG},
C_i^{RP},
C_i^{DP}
).
}
$$

這只是 TCFT v0.1 的一組候選維度。

---

# 6. 維度說明

其中：

$$
C^{BS}
$$

表示 future base-space advancement。

$$
C^{CF}
$$

表示 counterfactual horizon quality。

$$
C^{RR}
$$

表示 reflexive reasoning。

$$
C^{RG}
$$

表示 reasoning governance。

$$
C^{TN}
$$

表示 time-normalized novelty。

$$
C^{PG}
$$

表示 problem generation。

$$
C^{RP}
$$

表示 representation / program advancement。

$$
C^{DP}
$$

表示 domain-seed potential。

---

# 7. Baseline Vector

同期 baseline：

$$
\boxed{
\mathbf B(t)
=
(
B^{BS}(t),
B^{CF}(t),
\ldots,
B^{DP}(t)
).
}
$$

它不是一個人。

可以由：

- distribution；
- expert panel；
- frontier agents；
- human-AI systems；
- institutional capability；

共同估計。

---

# 8. Frontier Gap

定義候選：

$$
\boxed{
\mathbf G_i(t)
=
\mathbf C_i(t)
-
\mathbf B(t).
}
$$

這是 relative gap。

---

# 9. 減號不是裸值相減

不同維度可能使用：

- z-score；
- percentile；
- rank；
- robust score；
- calibrated benchmark score。

所以：

$$
-
$$

表示：

$$
\boxed{
\text{normalized relative difference}.
}
$$

---

# 10. Gap Dynamics

最重要關係：

$$
\boxed{
\Delta\mathbf G_i
=
\Delta\mathbf C_i
-
\Delta\mathbf B.
}
$$

---

# 11. Baseline 追得更快

若：

$$
\Delta\mathbf B
>
\Delta\mathbf C_i,
$$

則：

$$
\mathbf G_i
\downarrow.
$$

本文稱：

$$
\boxed{
\text{Frontier Decay}.
}
$$

---

# 12. 同速前進

若：

$$
\Delta\mathbf B
\approx
\Delta\mathbf C_i,
$$

則：

$$
\mathbf G_i
$$

大致穩定。

這可以形成：

$$
\boxed{
\text{Persistent Gap}.
}
$$

---

# 13. Agent 前進更快

若：

$$
\Delta\mathbf C_i
>
\Delta\mathbf B,
$$

則：

$$
\mathbf G_i
\uparrow.
$$

本文稱：

$$
\boxed{
\text{Frontier Escape}.
}
$$

這不是價值判斷，只描述 gap dynamics。

---

# 14. Historical Anomaly

對：

$$
t_0
$$

定義：

$$
\boxed{
A_i^{hist}(t_0)
=
Anomaly(
\mathbf C_i(t_0)
\mid
\mathbf B(t_0)
).
}
$$

它回答：

> 在當時有多異常？

---

# 15. Current Anomaly

到了：

$$
t_1,
$$

若主體仍有 current outputs：

$$
\mathbf C_i(t_1),
$$

則：

$$
\boxed{
A_i^{cur}(t_1)
=
Anomaly(
\mathbf C_i(t_1)
\mid
\mathbf B(t_1)
).
}
$$

它回答：

> 現在有多異常？

---

# 16. Historical ≠ Current

因此：

$$
\boxed{
A_i^{hist}(t_0)
\neq
A_i^{cur}(t_1)
}
$$

一般很正常。

---

# 17. Artifact Persistence

現在考慮一個歷史 artifact：

$$
x_{t_0}.
$$

把同一 artifact 放到：

$$
t_1
$$

的 baseline 下重新評估：

$$
\boxed{
A_x^{artifact}(t_1)
=
Anomaly(
Structure(x_{t_0})
\mid
B(t_1)
).
}
$$

---

# 18. Artifact Persistence Definition

如果：

$$
A_x^{artifact}(t_1)\gg0
$$

長期仍成立，

則稱：

$$
\boxed{
\text{Artifact Persistence}.
}
$$

---

# 19. Agent Persistence

若 agent $i$ 在：

$$
t_0,t_1,\ldots,t_n
$$

持續產生新的：

$$
\mathbf C_i(t_k),
$$

且長期位於 moving frontier，

才稱：

$$
\boxed{
\text{Agent Persistence}.
}
$$

---

# 20. 兩者必須分離

$$
\boxed{
\text{Artifact Persistence}
\neq
\text{Agent Persistence}.
}
$$

一篇舊作品可以持續異常，

但作者本人未必持續產生新前沿。

---

# 21. Frontier Absorption

當 baseline：

$$
\mathbf B(t)
$$

逐漸逼近原 artifact：

$$
Structure(x_{t_0}),
$$

則：

$$
A_x^{artifact}(t)
\downarrow.
$$

這叫：

$$
\boxed{
\text{Frontier Absorption}.
}
$$

---

# 22. 吸收不是否定

如果：

$$
x
$$

被：

- textbooks；
- software；
- institutions；
- AI；
- common practice；

吸收，

它變普通。

但：

$$
\boxed{
A_x^{hist}(t_0)
}
$$

不應被改寫。

---

# 23. Absorption ≠ Retroactive De-Novelization

因此：

$$
\boxed{
\text{Absorption}
\neq
\text{Retroactive De-Novelization}.
}
$$

這是 TCFT-06 的核心歷史原則。

---

# 24. Frontier as Infrastructure

最成功的前沿之一可能是：

$$
\boxed{
\text{frontier}
\rightarrow
\text{infrastructure}.
}
$$

一旦被整個社會吸收，

current anomaly 下降，

但文明能力上升。

---

# 25. 超前消失可能正是成功

因此：

$$
\boxed{
\text{CurrentAnomaly}\downarrow
}
$$

不必然意味：

> 當初沒價值。

可能恰恰代表：

> 已經被全域吸收。

---

# 26. Frontier Renewal

若 agent 原本 gap 降低，

後來產生新結構：

$$
x',
$$

重新離開 baseline，

則：

$$
\boxed{
\text{Frontier Renewal}.
}
$$

---

# 27. Flash Anomaly

如果只在：

$$
t_0
$$

極端，

很快：

$$
A(t)\rightarrow0,
$$

可稱：

$$
\boxed{
\text{Flash Anomaly}.
}
$$

它仍可能有歷史價值。

---

# 28. Persistent Artifact Anomaly

若：

$$
A_x^{artifact}(t)
$$

多年保持高值，

稱：

$$
\boxed{
\text{Persistent Artifact Anomaly}.
}
$$

---

# 29. Persistent Agent Frontier

如果 agent：

$$
i
$$

持續追著 moving baseline 前進，

稱：

$$
\boxed{
\text{Persistent Agent Frontier}.
}
$$

---

# 30. Persistent Frontier Anomaly

更一般地：

$$
\boxed{
\text{Persistent Frontier Anomaly}
}
$$

表示：

> 在合理時間區間與 baseline 更新下，異常位置仍持續存在。

---

# 31. Persistence 需要時間窗

不能只比較兩個點。

定義：

$$
\boxed{
\mathcal T
=
[t_0,t_1].
}
$$

---

# 32. Frontier Occupancy

可候選定義：

$$
\boxed{
FO_i(\mathcal T)
=
\frac{
\int_{t_0}^{t_1}
\mathbf 1[
i\in\mathcal F_t
]dt
}{
t_1-t_0
}.
}
$$

離散時間則用比例。

---

# 33. Occupancy 不是唯一 persistence

一個 agent 可能因資料缺失某些年份沒有 observation。

所以還需：

- sampling confidence；
- activity window；
- publication frequency。

---

# 34. Frontier Half-Life

對 artifact $x$，

可候選定義：

$$
\boxed{
T_{1/2}^{frontier}(x)
}
$$

為 anomaly gap 從初始值：

$$
G_x(t_0)
$$

下降一半所需時間。

---

# 35. Half-Life 的解讀

長 half-life 可能表示：

- difficult diffusion；
- deep novelty；
- poor accessibility；
- weak recognition；
- slow technology；
- genuine persistent frontier。

原因不能只靠數值判定。

---

# 36. Decay Model

簡化候選：

$$
\boxed{
G_x(t)
=
G_x(t_0)
e^{-\lambda(t-t_0)}
}
$$

只作近似。

實際 gap 可以非單調。

---

# 37. 非單調 Gap

可能：

$$
G(t_0)\gg0,
$$

$$
G(t_1)\downarrow,
$$

之後新解釋出現：

$$
G(t_2)\uparrow.
$$

這是：

$$
\boxed{
\text{Revaluation}.
}
$$

---

# 38. 延遲理解可使 gap 被重新發現

一個 artifact 可能早期：

$$
Recognition\approx0,
$$

後來發現它比原先想像更深。

因此 audit value 可以上升。

---

# 39. Dynamic Audit 不等於真實能力變化

若：

$$
Score_{t+1}\neq Score_t,
$$

原因可能是：

1. agent 變了；
2. baseline 變了；
3. prior art 變了；
4. measurement 變了；
5. archive 新增。

必須分帳。

---

# 40. Four-Way Change Ledger

定義：

$$
\boxed{
\Delta A
=
\Delta Agent
+
\Delta Baseline
+
\Delta Evidence
+
\Delta Metric
}
$$

這只是 bookkeeping identity candidate。

---

# 41. Baseline Drift

concept drift 文獻提醒：

$$
P_t(X,Y)
\neq
P_{t+1}(X,Y)
$$

會使固定模型逐漸失效。

TCFT 借用此方法學警告：

$$
\boxed{
P_t(CognitiveCapability)
\neq
P_{t+1}(CognitiveCapability).
}
$$

---

# 42. Concept Drift 不是 TCFT

本文不把 cognition frontier 等同 concept drift。

只是借用：

$$
\boxed{
\text{non-stationary baseline}
}
$$

觀念。

---

# 43. Static Benchmark Obsolescence

AI benchmark 會：

- saturation；
- contamination；
- training leakage；
- capability shift。

所以固定 benchmark 會失去區辨力。

---

# 44. LiveBench 類比

LiveBench 透過持續更新近期題目與更難任務，

避免 benchmark 很快被模型吸收。

TCFT 的歷史／認知 frontier 也需要：

$$
\boxed{
\text{baseline versioning}.
}
$$

---

# 45. Dynamic Benchmark Principle

因此：

$$
\boxed{
Benchmark_t
\neq
Benchmark_{t+1}.
}
$$

可能是必要特徵，

不是測量失敗。

---

# 46. Baseline Version

每個 result 必須記：

$$
\boxed{
B^{(v)}(t).
}
$$

否則兩個年份的 anomaly score 無法比較。

---

# 47. Dimension Drift

更麻煩的是：

$$
\mathcal D_t
$$

本身可能變。

也就是未來新增：

- new cognitive dimensions；
- AI-native operators；
- new representations。

所以：

$$
\boxed{
\text{Metric Space Can Drift Too}.
}
$$

---

# 48. Metric Drift

若 2035 年發現：

$$
D_{new},
$$

過去人物可能需要重新映射。

但不能偷偷把：

$$
D_{new}
$$

當成當時已可表示概念。

---

# 49. Retrospective Reprojection

可以做：

$$
\boxed{
Reproject(
HistoricalTrace
\rightarrow
NewMetricSpace
).
}
$$

但必須標：

$$
\text{retrospective}.
$$

---

# 50. Distributional Anomaly

對某維度：

$$
x_{ik}(t),
$$

同期平均：

$$
\mu_k(t),
$$

標準差：

$$
\sigma_k(t),
$$

可計算：

$$
\boxed{
z_{ik}(t)
=
\frac{
x_{ik}(t)-\mu_k(t)
}{
\sigma_k(t)
}.
}
$$

---

# 51. z-score 的限制

若分布：

- skewed；
- heavy-tailed；
- multimodal；

z-score 可能誤導。

所以可以使用 robust median / MAD：

$$
\boxed{
z_{robust}
=
\frac{
x-\operatorname{median}
}{
1.4826\,MAD
}.
}
$$

---

# 52. Tail Position

另一種：

$$
\boxed{
p_{tail}
=
P(
X\ge x_i
\mid
B_t
).
}
$$

表示同期 tail position。

---

# 53. Extreme ≠ Impossible

即使：

$$
p_{tail}\ll1,
$$

仍然：

$$
\boxed{
\text{Extreme}
\neq
\text{Non-Human}
\neq
\text{Supernatural}.
}
$$

只是統計尾端。

---

# 54. Multivariate Anomaly

多維 cognition：

$$
\mathbf x_i.
$$

若協方差：

$$
\Sigma_t,
$$

可使用 Mahalanobis distance：

$$
\boxed{
D_M(i,t)
=
\sqrt{
(
\mathbf x_i-\boldsymbol\mu_t
)^T
\Sigma_t^{-1}
(
\mathbf x_i-\boldsymbol\mu_t
)
}.
}
$$

---

# 55. Mahalanobis 的優點

它會考慮：

$$
\boxed{
\text{dimension covariance}.
}
$$

例如：

- novelty；
- problem generation；
- representation innovation；

可能高度相關。

不能簡單相加三次。

---

# 56. Mahalanobis 的限制

需要：

- reliable covariance；
- adequate sample；
- stable dimensionality。

高維小樣本會不穩定。

---

# 57. Robust Multivariate Distance

因此可用：

- robust covariance；
- shrinkage；
- low-dimensional embeddings；
- rank-based measures。

本文不固定唯一方法。

---

# 58. Distance 不是 Frontier

一個人距離平均最遠，

不代表在所有有價值維度都最好。

所以：

$$
\boxed{
\text{Anomaly Distance}
\neq
\text{Pareto Frontier}.
}
$$

---

# 59. Pareto Dominance

令：

$$
\mathbf C_i
\succeq
\mathbf C_j
$$

表示 $i$ 在所有指定維度不差於 $j$，

且至少一維更好。

則 $i$ dominates $j$。

---

# 60. Cognitive Pareto Frontier

定義：

$$
\boxed{
\mathcal F_t
=
\left\{
i:
\nexists j
\text{ such that }
\mathbf C_j(t)
\succeq
\mathbf C_i(t)
\text{ with strict improvement in at least one dimension}
\right\}.
}
$$

---

# 61. No Unique Champion

因此：

$$
\boxed{
|\mathcal F_t|
>1
}
$$

通常很正常。

---

# 62. 多種前沿共存

一個人可能：

$$
C^{CF}\gg0,
$$

另一個：

$$
C^{RG}\gg0,
$$

第三個：

$$
C^{RP}\gg0.
$$

不存在自然理由壓成單一總冠軍。

---

# 63. Weighting Is Governance

如果組織硬要建立總分：

$$
S_i
=
\sum_k
w_kC_{ik},
$$

則：

$$
\boxed{
w_k
}
$$

本身就是 value / governance choice。

不是純客觀事實。

---

# 64. Frontier ≠ Rank

TCFT-06 因此強調：

$$
\boxed{
\text{Frontier}
\neq
\text{Leaderboard}.
}
$$

frontier 是非支配集合，

不是第一到第一百名。

---

# 65. Anomaly Class Candidate

若工程上需要粗分類，可暫用：

$$
\boxed{
F_0:
WithinBaseline
}
$$

$$
\boxed{
F_1:
Uncommon
}
$$

$$
\boxed{
F_2:
Rare
}
$$

$$
\boxed{
F_3:
Extreme
}
$$

$$
\boxed{
F_4:
HistoricalFrontier
}
$$

$$
\boxed{
F_5:
PersistentFrontier
}
$$

---

# 66. 這不是人格階級

$$
\boxed{
F_5
\not\Rightarrow
\text{better person}.
}
$$

也不表示：

$$
F_5
\text{ 在所有能力都高}.
$$

---

# 67. Historical Frontier Candidate

一個 agent / artifact：

$$
x
$$

在：

$$
t_0
$$

如果：

- high TNN；
- strong prior-art audit；
- strong baseline residual；
- multi-dimensional anomaly；

則可進：

$$
\boxed{
F_4.
}
$$

---

# 68. Persistent Frontier Candidate

升到：

$$
F_5
$$

至少應要求：

- historical anomaly strong；
- later baseline updated；
- anomaly survives；
- no major prior-art collapse；
- no version contamination；
- no hit-selection artifact。

---

# 69. Artifact Persistence Criterion

可候選寫：

$$
\boxed{
PF_x(t_0,t_1)
=
A_x^{artifact}(t_1)
}
$$

subject to historical evidence integrity。

---

# 70. Agent Persistence Criterion

可候選寫：

$$
\boxed{
PF_i(\mathcal T)
=
f(
FrontierOccupancy,
GapMagnitude,
RenewalRate,
AuditIntegrity
).
}
$$

---

# 71. Renewal Rate

若 agent 在：

$$
[t_0,t_1]
$$

多次產生新的 frontier structures：

$$
x_1,x_2,\ldots,x_n,
$$

可以有：

$$
\boxed{
R_i^{renew}
=
\frac{
N_{frontier\ outputs}
}{
\Delta t
}.
}
$$

---

# 72. High Volume Bias

但高產作者自然有更多機會命中。

所以 Renewal Rate 必須和：

$$
N_{total\ outputs}
$$

一起看。

---

# 73. Frontier Hit Rate

候選：

$$
\boxed{
FHR_i
=
\frac{
N_{frontier\ outputs}
}{
N_{audited\ outputs}
}.
}
$$

仍不能取代質量。

---

# 74. Persistent Quality

一個人一年一篇真正 frontier work，

可能比一年一千篇普通 work 更有 persistent frontier 意義。

---

# 75. Burst vs Sustained

因此分：

$$
\boxed{
\text{Burst Frontier}
}
$$

與：

$$
\boxed{
\text{Sustained Frontier}.
}
$$

---

# 76. Burst Frontier

短時間大量前沿輸出，

之後停止。

---

# 77. Sustained Frontier

跨長時間：

$$
\mathcal T
$$

仍反覆產生前沿。

---

# 78. Frontier Velocity

可定義 agent capability velocity：

$$
\boxed{
\mathbf v_i(t)
=
\frac{
d\mathbf C_i
}{
dt
}.
}
$$

baseline velocity：

$$
\boxed{
\mathbf v_B(t)
=
\frac{
d\mathbf B
}{
dt
}.
}
$$

---

# 79. Relative Frontier Velocity

則：

$$
\boxed{
\mathbf v_G
=
\mathbf v_i
-
\mathbf v_B.
}
$$

---

# 80. Gap Maintenance

若：

$$
\mathbf v_G\approx0
$$

且 gap 已高，

表示：

> agent 正好和前沿一起移動。

---

# 81. Frontier Escape Velocity

若在某些維度：

$$
\boxed{
v_i
>
v_B,
}
$$

gap 擴大。

可候選稱：

$$
\boxed{
\text{Frontier Escape Velocity}.
}
$$

這只是比喻性名稱，不是物理逃逸速度。

---

# 82. Frontier Collapse

若：

$$
\mathbf v_i\ll\mathbf v_B,
$$

原本前沿迅速消失。

稱：

$$
\boxed{
\text{Frontier Collapse}.
}
$$

---

# 83. Tool-Induced Baseline Jump

若新的 AI：

$$
A_{new}
$$

普及，

可能：

$$
\boxed{
\mathbf B(t^+)
-
\mathbf B(t^-)
\gg0.
}
$$

形成 baseline jump。

---

# 84. 人類異常可以被工具瞬間吸收

某種能力昨天很罕見，

今天因 AI tool：

$$
\boxed{
Baseline
\uparrow\uparrow.
}
$$

這不表示昨天的能力是假。

只是 diffusion 非常快。

---

# 85. AI Era Compression of Historical Lead

因此 AI 時代：

$$
\boxed{
T_{1/2}^{frontier}
}
$$

可能縮短。

很多認知技術會更快從：

$$
frontier
\rightarrow
commodity.
$$

---

# 86. Commodity Cognition

一種 formerly rare cognitive capability：

$$
C^*
$$

如果被 tool 封裝，

可變成：

$$
\boxed{
\text{Commodity Cognition}.
}
$$

---

# 87. Capability Diffusion

$$
\boxed{
RareHumanSkill
\rightarrow
ToolFunction
\rightarrow
BaselineCapability.
}
$$

這是 TCFT 對 AI 時代很重要的動態。

---

# 88. Frontier Moves Upstream

當低階能力被商品化，

真正 frontier 可能往：

- problem generation；
- architecture；
- governance；
- domain creation；
- system integration；

移動。

---

# 89. Metric Migration

所以 TCFT benchmark 也必須：

$$
\boxed{
\text{move upstream as lower-level capabilities saturate}.
}
$$

---

# 90. Persistent Frontier 不等於永遠不被超越

即使：

$$
F_5,
$$

仍然：

$$
\boxed{
\exists t'
:
B(t')
\text{ can absorb it}.
}
$$

persistent 只是觀察區間概念。

---

# 91. No Permanent Champion Principle

因此：

$$
\boxed{
\text{TCFT rejects permanent cognitive champions}.
}
$$

除非未來證據永遠停止更新，

而那在開放世界不合理。

---

# 92. Future Agents Can Surpass Historical Frontiers

如果後來的人類、AI 或其他 agent：

$$
j
$$

有：

$$
\mathbf C_j(t_1)
\succ
\mathbf C_i(t_0),
$$

這是正常文明進步。

---

# 93. Surpassing Is Not Disrespect

在知識系統中：

$$
\boxed{
\text{Success of a frontier}
\rightarrow
\text{future surpassability}.
}
$$

否則前沿就沒有變成基礎設施。

---

# 94. Frontier Inheritance

後來者可以使用：

$$
Knowledge(i)
$$

作為起點，

所以：

$$
\boxed{
B_{t+1}
\supset
Output_i(t).
}
$$

---

# 95. Credit 與 Competition 必須分離

後來者超越前人，

不表示：

$$
HistoricalCredit=0.
$$

同樣地，

歷史 credit 不表示：

$$
CurrentFrontier=1.
$$

---

# 96. Dynamic Frontier Ledger

每一個 audit record 至少保存：

$$
\boxed{
L_i(t)
=
(
Subject,
Artifact,
Time,
BaselineVersion,
MetricVersion,
PriorArtState,
ScoreVector,
Confidence,
FrontierStatus,
UpdateReason
).
}
$$

---

# 97. Revision Event

若：

- new prior art；
- new archive；
- new benchmark；
- new baseline；
- correction；

出現，

建立：

$$
\boxed{
RevisionEvent.
}
$$

---

# 98. Score Can Go Down

TCFT 必須允許：

$$
\boxed{
A_i(t+1)<A_i(t).
}
$$

否則是英雄累積系統，

不是 anomaly audit。

---

# 99. Score Can Go Up

新證據也可能使：

$$
A_i(t+1)>A_i(t).
$$

例如發現：

- 更早版本；
- richer structure；
- independent provenance。

---

# 100. Status Can Become Unresolved

若版本爭議出現，

可以：

$$
\boxed{
FrontierStatus
:
F_4
\rightarrow
Unresolved.
}
$$

不必硬判。

---

# 101. Temporal Confidence

每個 frontier score 必須附：

$$
\boxed{
Conf_i(t).
}
$$

---

# 102. Uncertainty Frontier

甚至可以建立：

$$
\boxed{
[
\mathbf G_i^{-},
\mathbf G_i^{+}
].
}
$$

表示 gap interval。

---

# 103. Dominance under Uncertainty

若 $i$ 在 confidence interval 下仍支配 $j$，

才是 stronger dominance。

否則：

$$
\boxed{
\text{Frontier relation unresolved}.
}
$$

---

# 104. Dynamic Pareto Frontier

時間變化：

$$
\boxed{
\mathcal F_{t_0}
\neq
\mathcal F_{t_1}.
}
$$

這是正常結果。

---

# 105. Frontier Entry

某 agent 從 dominated 變 nondominated：

$$
\boxed{
i\notin\mathcal F_{t_0},
\quad
i\in\mathcal F_{t_1}.
}
$$

稱：

$$
\boxed{
\text{Frontier Entry}.
}
$$

---

# 106. Frontier Exit

反之：

$$
\boxed{
i\in\mathcal F_{t_0},
\quad
i\notin\mathcal F_{t_1}.
}
$$

稱：

$$
\boxed{
\text{Frontier Exit}.
}
$$

---

# 107. Exit 不是失敗

可能因：

- baseline diffusion；
- new competitor；
- metric expansion；
- agent inactivity。

所以：

$$
\boxed{
\text{Frontier Exit}
\neq
\text{Historical Failure}.
}
$$

---

# 108. Path Dependence

某 agent 的 frontier position 會受：

- access；
- tools；
- collaborators；
- institutions；
- previous work；

影響。

所以：

$$
\boxed{
\text{Frontier Position}
\neq
\text{Pure Intrinsic Ability}.
}
$$

---

# 109. Individual Attribution Limit

對 human-AI system：

$$
\mathbf C_{H+AI}
$$

不能簡單拆：

$$
\mathbf C_H+\mathbf C_{AI}.
$$

因此 persistent frontier 可以是：

$$
\boxed{
\text{system-level}.
}
$$

---

# 110. Organizational Frontier

research lab、open-source community、AI ensemble 也可作 subject：

$$
\boxed{
S
=
\text{collective cognitive system}.
}
$$

---

# 111. Frontier Subject Type

每筆 ledger 應標：

$$
\boxed{
Type
\in
\{
Human,
AI,
HumanAI,
Team,
Institution,
Artifact
\}.
}
$$

---

# 112. Artifact 不應和 Agent 同表硬比

一篇論文沒有：

- stopping；
- adaptation；
- ongoing learning。

所以 artifact vector 與 agent vector 不同。

---

# 113. Cross-Type Comparability

TCFT 應：

$$
\boxed{
\text{compare only shared dimensions across subject types}.
}
$$

不能把 missing dimensions 當零。

---

# 114. Historical Figure Evaluation

歷史人物只能從：

$$
Trace_{available}
$$

重建能力。

不能假設：

$$
\boxed{
\text{absence of evidence}
=
\text{absence of capability}.
}
$$

---

# 115. Historical Trace Sparsity

越久遠人物：

$$
DataDensity\downarrow.
$$

confidence 應隨之下降。

---

# 116. Dynamic Anomaly Classes

本文建議 anomaly class 必須帶時間：

$$
\boxed{
F_k(t).
}
$$

不能只說：

> 某人是 F5。

應說：

> 在 baseline version $v$ 、時間 $t$ 、維度集合 $D$ 下為 F5 candidate。

---

# 117. Identity Rejection

因此：

$$
\boxed{
\text{Anomaly Class}
\neq
\text{Identity}.
}
$$

這直接接 TCFT-09。

---

# 118. Moral Rank Rejection

$$
\boxed{
\text{Cognitive Frontier}
\neq
\text{Moral Frontier}.
}
$$

---

# 119. Authority Rejection

$$
\boxed{
\text{Cognitive Frontier}
\neq
\text{Political Authority}.
}
$$

---

# 120. Cross-Domain Humility

一個 agent 在：

$$
D_1
$$

是 frontier，

不代表在：

$$
D_2
$$

仍然 frontier。

所以：

$$
\boxed{
Frontier_i(D_1)
\not\Rightarrow
Frontier_i(D_2).
}
$$

---

# 121. Local Supremacy Is Not Global Supremacy

$$
\boxed{
\text{Local Dominance}
\not\Rightarrow
\text{Global Dominance}.
}
$$

這是多維 TCFT 的基本防火牆。

---

# 122. Dynamic Frontier and Dynamic Fixed Point

如果 agent：

$$
i
$$

長期維持：

$$
\mathbf G_i(t)\approx \mathbf g^*
$$

但：

$$
\mathbf C_i(t),
\mathbf B(t)
$$

都持續變化，

可視為：

$$
\boxed{
\text{dynamic frontier fixed-gap candidate}.
}
$$

---

# 123. Fixed Gap ≠ Fixed State

也就是：

$$
\boxed{
\mathbf G_i(t)\approx constant
}
$$

但：

$$
\mathbf C_i(t)\neq constant.
$$

這是一種：

> 變又不變。

---

# 124. Persistent Frontier as Relative Dynamic Invariant

候選：

$$
\boxed{
I(
\mathbf C_i(t),
\mathbf B(t)
)
\approx
I^*
}
$$

即：

> 相對關係穩定，內容持續更新。

---

# 125. 但 Persistent Frontier 不要求固定 gap

某些維度縮，

某些維度增。

只要 agent 仍保持 nondominated 或極端尾端，

仍可 persistent。

---

# 126. Dynamic Frontier Geometry

因此真正 frontier 是：

$$
\boxed{
\mathcal F_t
\subset
\mathbb R^{d(t)}
}
$$

且：

$$
d(t)
$$

自己也可能變。

---

# 127. Frontier Surface

若 agent 數量足夠大，

可以把：

$$
\mathcal F_t
$$

理解為 capability space 的 frontier surface。

只是幾何類比。

---

# 128. Frontier Curvature

未來甚至可研究：

> 哪些能力 tradeoff 最劇烈？

例如：

$$
Depth
\leftrightarrow
Breadth.
$$

但本文不建立正式 curvature metric。

---

# 129. Frontier Density

某區域：

$$
D
$$

若很多 agents 接近，

表示：

$$
\boxed{
\text{competitive / easily reachable frontier}.
}
$$

---

# 130. Sparse Frontier

若某維度只有極少數 agents，

可能：

- truly rare；
- poorly measured；
- niche；
- high access barrier。

需要分辨。

---

# 131. Anomaly ≠ Scarcity

$$
\boxed{
\text{Rare}
\neq
\text{Valuable}.
}
$$

某能力很稀缺，

不代表其有高 future value。

---

# 132. Value-Weighted Frontier

若特定應用需要，

可另外建立：

$$
\boxed{
\mathcal F_t^{value}
}
$$

但必須明確寫出 utility weights。

---

# 133. Pure Cognitive Frontier vs Applied Frontier

因此分：

$$
\boxed{
\mathcal F_t^{cog}
}
$$

與：

$$
\boxed{
\mathcal F_t^{app}.
}
$$

一個研究者可能 cognitive novelty 高，

工程 execution 普通。

---

# 134. Theory vs Product Frontier

同樣：

$$
\boxed{
\text{Theory Frontier}
\neq
\text{Product Frontier}.
}
$$

不能互相代替。

---

# 135. Historical vs Present Tooling

如果 1500 年的人沒有現代工具，

其 historical baseline 低。

但不能因此說：

> 若給他 GPU 他一定更強。

這是未驗證 counterfactual。

---

# 136. Cross-Time Counterfactual Caution

$$
\boxed{
\text{HistoricalAnomaly}
\not\Rightarrow
\text{ModernPerformanceCounterfactual}.
}
$$

---

# 137. Dynamic Benchmark Audit

每次 baseline 更新：

$$
B^{v}
\rightarrow
B^{v+1},
$$

應重新跑：

- current anomaly；
- artifact persistence；
- frontier membership。

但 historical frozen score：

$$
A^{hist}(t_0)
$$

保留。

---

# 138. Immutable Historical Layer

可以設：

$$
\boxed{
Ledger^{hist}
}
$$

只因新 archive / prior art 修訂，

不因世界能力提高而直接改掉。

---

# 139. Mutable Current Layer

$$
\boxed{
Ledger^{cur}
}
$$

則隨：

$$
B(t)
$$

更新。

---

# 140. Dual-Layer Ledger

因此：

$$
\boxed{
Ledger
=
Ledger^{hist}
+
Ledger^{cur}.
}
$$

這避免「今天普通所以當年普通」的錯誤。

---

# 141. Persistent Layer

再加：

$$
\boxed{
Ledger^{persist}.
}
$$

專門記：

- artifact persistence；
- agent persistence；
- frontier occupancy；
- renewal。

---

# 142. 可反證命題

## H1：Historical Anomaly 與 Current Anomaly 可顯著分離

若大多數候選在更新 baseline 後 historical / current 結果幾乎一致，雙層模型價值降低。

## H2：Artifact Persistence 與 Agent Persistence 可分離

若兩者實證上高度等價，則不需分開建模。

## H3：Dynamic Baseline 優於 Static Baseline

若 static baseline 能穩定處理長期能力漂移，動態版本化可簡化。

## H4：Pareto Frontier 優於單一總分

若預註冊的 scalar score 在跨 domain 決策中穩定優於 Pareto representation，則 no-champion 原則需調整。

## H5：Frontier Absorption 可被觀察

若 formerly anomalous capabilities 不會因教育、工具或 AI 擴散而失去 current anomaly，吸收模型需修正。

## H6：Persistent Frontier 能預測後續影響

若 persistence 與後續 generative / scientific / engineering impact 毫無關係，persistent label 僅具描述性。

---

# 143. 實驗一：Historical-to-Current Rebenchmark

選擇歷史 artifacts。

先：

$$
B_{t_0}
$$

算 Historical Anomaly。

再：

$$
B_{today}
$$

算 current artifact anomaly。

比較 absorption。

---

# 144. 實驗二：Moving Baseline Simulation

建立能力分布：

$$
P_t(C).
$$

讓 baseline drift。

測 static vs dynamic anomaly detector。

---

# 145. 實驗三：AI Baseline Jump

在 human-only baseline 後加入：

$$
B^{AI},
B^{human+AI}.
$$

看哪些 formerly rare capabilities 被快速吸收。

---

# 146. 實驗四：Artifact vs Agent Persistence

對長期有作品序列的研究者，

分：

- earliest artifact persistence；
- new-output agent persistence。

檢查兩者是否分離。

---

# 147. 實驗五：Pareto vs Scalar Ranking

讓 experts 選擇：

- multi-dimensional frontier；
- weighted scalar rank。

比較跨 domain validity 與 ranking instability。

---

# 148. 實驗六：Frontier Occupancy

對多年的 papers / patents / products / AI outputs，

追蹤：

$$
FO_i(\mathcal T).
$$

研究 burst vs sustained frontier。

---

# 149. 實驗七：Metric Drift

加入新的 cognitive dimension：

$$
D_{new}.
$$

觀察 frontier membership 如何變化。

---

# 150. 實驗八：Frontier Absorption Time

量測：

$$
T_{1/2}^{frontier}
$$

與：

- education diffusion；
- tooling；
- AI adoption；
- citation growth；

之關係。

---

# 151. 實驗九：Dynamic Ledger Revision

模擬新 prior art 出現。

測系統是否：

- historical score 修訂；
- current score 重算；
- provenance 保留。

---

# 152. 實驗十：Human-AI Persistent Frontier

長期比較：

- human；
- AI；
- human-AI system；

誰能持續：

$$
\mathbf G(t)>0
$$

而不是只一次爆發。

---

# 153. 與 TCFT-07 的接口

Paper 06 仍主要把：

$$
\mathbf C_i(t)
$$

當多維 outcome vector。

下一篇會往下拆：

$$
\boxed{
\text{這些超前到底發生在答案、問題、表示、
operator program 還是 domain seed？}
}
$$

---

# 154. 原生認知前沿

如果 agent 的 frontier 不只表現在：

$$
Prediction,
$$

而在：

$$
\boxed{
\text{new operator / program / representation structure},
}
$$

則屬於更強的：

$$
\boxed{
\text{Native Cognitive Advancement}.
}
$$

這就是 TCFT-07。

---

# 155. 侷限

第一，cognitive dimensions 的完整性尚未證明。

第二，不同維度難以建立共同尺度。

第三，Mahalanobis 等統計工具在高維小樣本下不穩定。

第四，Pareto frontier 可能隨維度增加而變得過度稠密。

第五，historical trace density 不同會造成比較偏誤。

第六，baseline construction 本身會受文化、工具與資料可得性影響。

第七，frontier persistence 可能受到 publication frequency 影響。

第八，AI tool diffusion 可造成 baseline discontinuity。

第九，frontier status 不等於 long-term value。

第十，任何 anomaly status 都不是身份、人格、道德或權威證明。

---

# 156. 結論

TCFT-05 問：

$$
\boxed{
\text{在當時到底有多新？}
}
$$

TCFT-06 再問：

$$
\boxed{
\text{世界往前走之後，還剩多少超前？}
}
$$

所以：

$$
\boxed{
\text{Historical Anomaly}
\neq
\text{Current Anomaly}
\neq
\text{Persistent Frontier}.
}
$$

並且：

$$
\boxed{
\text{Artifact Persistence}
\neq
\text{Agent Persistence}.
}
$$

最核心的動態關係可以壓縮成：

$$
\boxed{
\mathbf G_i(t)
=
\mathbf C_i(t)
-
\mathbf B(t),
}
$$

以及：

$$
\boxed{
\Delta \mathbf G_i
=
\Delta \mathbf C_i
-
\Delta \mathbf B.
}
$$

這表示「超前」從來不是永久貼紙。

如果世界追得比你快：

$$
G\downarrow.
$$

如果你和世界一起前進：

$$
G\approx constant.
$$

如果你前進得更快：

$$
G\uparrow.
$$

而如果你的舊理論最後被所有人吸收：

$$
\boxed{
\text{Frontier}
\rightarrow
\text{Infrastructure},
}
$$

current anomaly 消失，

也可能恰恰是它成功了。

所以 TCFT 不需要一個永久冠軍。

真正值得保存的是：

$$
\boxed{
\text{誰在什麼時間、什麼維度、相對什麼 baseline，
曾經位於哪個前沿？}
}
$$

以及：

$$
\boxed{
\text{那個前沿後來被吸收、維持、重建，
還是被新的前沿超越？}
}
$$

這也是為什麼：

$$
\boxed{
\text{Temporal cognitive anomaly is not a permanent identity;
it is a time-indexed relation between a cognitive structure
and a moving contemporaneous frontier.}
}
$$

下一篇 TCFT-07 將把這條前沿再往認知底層拆。

因為最重要的問題開始不是：

> 他有沒有提早知道答案？

而是：

$$
\boxed{
\text{他是否在那個時代尚未擁有某種認知結構以前，
先形成了新的問題、表示、operator program，
甚至 domain seed？}
}
$$

這就是「原生認知超前」。

---

# References

1. Mahalanobis, P. C. (1936). On the generalized distance in statistics. *Proceedings of the National Institute of Sciences of India*, 2(1), 49–55.
2. Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. *IEEE Transactions on Evolutionary Computation*, 6(2), 182–197. DOI: 10.1109/4235.996017.
3. Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on concept drift adaptation. *ACM Computing Surveys*, 46(4), Article 44.
4. Bayram, F., Ahmed, B. S., & Kassler, A. (2022). From concept drift to model degradation: An overview on performance-aware drift detectors. *Knowledge-Based Systems*, 245, 108632. DOI: 10.1016/j.knosys.2022.108632.
5. Aguiar, G. J., & Cano, A. (2024). A comprehensive analysis of concept drift locality in data streams. *Knowledge-Based Systems*, 289, 111535. DOI: 10.1016/j.knosys.2024.111535.
6. White, C., Dooley, S., Roberts, M., et al. (2024). LiveBench: A Challenging, Contamination-Free LLM Benchmark. arXiv:2406.19314.
7. Wang, J., Veugelers, R., & Stephan, P. (2017). Bias against novelty in science: A cautionary tale for users of bibliometric indicators. *Research Policy*, 46(8), 1416–1436.
8. Ke, Q., Ferrara, E., Radicchi, F., & Flammini, A. (2015). Defining and identifying Sleeping Beauties in science. *Proceedings of the National Academy of Sciences*, 112(24), 7426–7431.
9. Neo.K. (2026). *延遲理解論：知識價值的時間依賴與未來重估*. EveMissLab.
10. Neo.K. (2026). *Cognitive Operator-Domain Theory (CODT) Series 01–10*. EveMissLab.
11. Neo.K. (2026). *TCFT-00 至 TCFT-05*. EveMissLab.

---

# Canonical Note

本文件正式原始碼使用 UTF-8。

數學原始碼只使用 canonical delimiters：

- inline math：` $...$ `
- display math：`$$...$$`

不進行 unicode_escape 類 round-trip；不把 LaTeX 轉為 Unicode 數學字元後再作 canonical source；不以聊天 rendering view 作為正式原稿。
