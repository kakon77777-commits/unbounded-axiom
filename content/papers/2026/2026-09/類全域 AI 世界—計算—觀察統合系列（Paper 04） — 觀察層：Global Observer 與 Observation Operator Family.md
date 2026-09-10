# 類全域 AI 世界—計算—觀察統合系列（Paper 04）
## 觀察層：Global Observer 與 Observation Operator Family
### The Observation Layer: Global Observer and Observation Operator Families

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 04 / 12  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** Global Observer × OAC × Governed World Family × Global Computation × Inner Observation × Projection Computation × PNCW × Active Perception × Observer-Relative Computation  
**前篇：** Paper 03《計算層：世界族上的全域異質計算》  
**狀態：** 觀察層母規格／AI-native observation architecture；不宣稱 Global Observer 等於全知觀察者，不宣稱現有 AI 已具完整第一人稱內視或通用自發觀察本體建構能力

---

## 摘要

Paper 02 與 Paper 03 已分別建立受治理世界族：

$$
\mathfrak W_t^G
$$

與世界族計算層：

$$
\mathfrak C_t^{WF}.
$$

然而，世界存在並被計算，不代表智能已經「看見」真正與任務相關的結構。更多 sensor、更多 tokens、更多資料來源、更大的 knowledge base，甚至更完整的 world model，都不能直接推出更好的 observation：

$$
\boxed{
\text{More Input}
\neq
\text{Better Observation},
}
$$

$$
\boxed{
\text{More Knowledge}
\neq
\text{Global Observation},
}
$$

$$
\boxed{
\text{World Model}
\neq
\text{Global Observer}.
}
$$

本文提出 WCO-TF 的正式 **Observation Layer**。其核心不是把 AI 變成一個「看見所有東西」的全知觀察者，而是讓系統在有限資源、有限可達性、有限權限與不確定條件下，能夠持續選擇：

- 應該觀察哪個 world；
- 哪個 domain；
- 哪個時間區間；
- 哪個尺度；
- 哪個 resolution；
- 哪種 observation operator；
- 哪種 observer-relative representation；
- 是否需要主動改變 viewpoint、query、instrument 或 simulation；
- 何時應該停止觀察；
- 何時應該 reobserve；
- 何時需要發明新的 computational way of seeing。

本文定義 **Global Observation State（GOS）**：

$$
\boxed{
\mathfrak O_t^{G}
=
\left\langle
\mathfrak B_t,
\mathfrak O_t,
\mathfrak A_t^{att},
\mathfrak X_t^{acc},
\Lambda_t^{obs},
\mathfrak Q_t^{obs},
\mathfrak D_t^{obs},
\mathfrak H_t^{obs},
\mathfrak C_t^{obs}
\right\rangle.
}
$$

其中：

- $\mathfrak B_t$：observer family；
- $\mathfrak O_t$：observation operator family；
- $\mathfrak A_t^{att}$：attention / observation allocation operators；
- $\mathfrak X_t^{acc}$：observation accessibility structure；
- $\Lambda_t^{obs}$：observation resolution / scale field；
- $\mathfrak Q_t^{obs}$：query / purpose family；
- $\mathfrak D_t^{obs}$：observation debt / uncertainty state；
- $\mathfrak H_t^{obs}$：observation history / provenance；
- $\mathfrak C_t^{obs}$：observation contracts / certificates。

單一 observer 被定義為：

$$
\boxed{
B_k
=
\left\langle
Id_k,
Scope_k,
Channels_k,
Access_k,
Goals_k,
Budget_k,
Memory_k,
Model_k,
Authority_k,
Calibration_k
\right\rangle.
}
$$

這裡的 observer 不必是人類，也不必是單一模型。它可以是：

- human observer；
- AI observer；
- sensor network；
- agent；
- evaluator；
- theorem prover；
- world-external debugger；
- local in-world subject；
- federated observer ensemble。

本文定義 typed observation operator：

$$
\boxed{
\mathcal O_{\beta}
:
(B_k,W_i,D,\tau,b,\rho)
\rightharpoonup
(Y,\eta),
}
$$

其中 $Y$ 是 observation content， $\eta$ 是 observation metadata，包括 WorldId、source mode、time、resolution、uncertainty、provenance、operator version、access path 與 debt。

Observation 因而不是「world 到字串」的單一映射，而是一個受 observer、task、domain、budget 與 risk 共同約束的部分算子。

本文進一步區分：

$$
\boxed{
\text{Observation}
\neq
\text{Projection}
\neq
\text{Presentation}.
}
$$

Observation 決定「取到什麼結構」；projection 決定「如何將該結構編譯到 carrier」；presentation 則是 observer 最後實際接收到的顯現形式。

對同一 observation content：

$$
Y
$$

可以有：

$$
Y
\xrightarrow{\Pi_1}
P_{\mathrm{text}},
$$

$$
Y
\xrightarrow{\Pi_2}
P_{\mathrm{graph}},
$$

$$
Y
\xrightarrow{\Pi_3}
P_{\mathrm{XR}},
$$

$$
Y
\xrightarrow{\Pi_4}
P_{\mathrm{AI-native}}.
$$

因此：

$$
\boxed{
\text{Observation Content}
\neq
\text{Carrier Representation}.
}
$$

本文也將既有 OAC 的 observer family、observation family、attention family 與 projection/computation separation 嵌入 WCO。Attention 被正式視為 observation budget allocator：

$$
\boxed{
\mathsf{Attend}_t
:
(\mathfrak W_t^G,\mathfrak O_t,B_t,\tau,\rho)
\rightarrow
\mathcal A_t^{obs},
}
$$

其中：

$$
\mathcal A_t^{obs}
$$

是當前被啟動的有限 observation support。

因此：

$$
\boxed{
|\mathcal A_t^{obs}|<\infty,
}
$$

即使：

$$
|\mathfrak W_t^G|
$$

與潛在 observation space 很大。

本文承接 Global Observer Series C 的母命題：Global Observer 的核心不是擁有更多 input channel，而是智能開始自行決定：

> 世界應如何被看、被區分、被切成域、被跨域連接，以及哪些局部應重新收束為更高階 world model。

本文進一步把這種能力稱為 **Observer-Method Autonomy（OMA）**。若 AI 不只是從預設 operator 集合選擇，而能提出新的：

$$
\mathcal O_{\mathrm{new}},
$$

並在跨 domain、跨時間、跨 run 的測試中穩定證明它比既有：

$$
\mathcal O_{\mathrm{old}}
$$

更有效、更可驗證、更節省資源或更能暴露 counterexample，則可視為 AI-native observation method emergence 的候選證據。

因此：

$$
\boxed{
\text{Observation Selection}
<
\text{Observation Method Generation}
}
$$

在能力層級上可以成立。

但本文同時保留一條嚴格限制：

$$
\boxed{
\text{AI Self-Report}
\neq
\text{Privileged Internal Observation}.
}
$$

承接新版內視算子論，內視只可暫時定義為對 observer-accessible internally instantiated representations 的操作。現有 LLM 的自我敘述不能被自動提升為對其底層神經、因果或主觀狀態的直接 privileged access。

本文最後提出 **Global Observation Contract（GOC）**：

$$
\boxed{
\mathsf{GOC}
=
\left\langle
Observer,
World,
Domain,
Purpose,
Access,
Operator,
Resolution,
Time,
Uncertainty,
Debt,
Provenance,
ProjectionBoundary,
ReobservePolicy
\right\rangle.
}
$$

一個重要 observation 若無法回答：

1. 誰在看？
2. 看哪一個 world？
3. 看哪個 domain？
4. 為了什麼 task？
5. 透過哪條 access path？
6. 使用哪個 operator？
7. 解析度是多少？
8. observation 是哪個時間的？
9. uncertainty 與 debt 是什麼？
10. 是否能 reobserve？

就不應被當成完整可審計觀察。

本文最終提出：

$$
\boxed{
\text{A Global Observer is not an observer that sees everything.}
}
$$

而是：

$$
\boxed{
\text{an observer system that can organize,
select, compare, revise, and invent ways of seeing
across a governed family of worlds}.
}
$$

**關鍵詞：** Global Observer、Observation Operator、Observer Family、Attention、Active Observation、OAC、World Family、Observation Accessibility、AI-Native Observation、Inner Observation、Projection、Computational Way of Seeing

---

# 0. Paper 03 留下的觀察問題

Paper 03 建立：

$$
\mathfrak W_t^G
\xrightarrow{\mathsf{Compute}}
\mathfrak W_{t+1}^{G}.
$$

但 computation 本身沒有回答：

> 現在到底要看什麼？

> 哪一個 branch 出現異常？

> 哪一個 domain 需要提高解析度？

> 哪些 local states 值得向 global layer 上送？

> 哪個 observation method 會看見另一個 method 看不到的結構？

這就是 Paper 04。

---

# 1. Observation 是一級 Runtime 操作

本文拒絕：

$$
\boxed{
\text{Observation}
=
\text{passive output reading only}.
}
$$

Observation 是可選、可配置、可調度、可重播、可比較的 runtime operation。

---

# 2. More Input 不等 Better Observation

$$
\boxed{
\text{More Input}
\neq
\text{Better Observation}.
}
$$

大量 input 可以增加 noise、redundancy、latency 與 attention burden。

---

# 3. More Knowledge 不等 Global Observation

$$
\boxed{
\text{More Knowledge}
\neq
\text{Global Observation}.
}
$$

知道很多 facts 不代表知道現在應該看哪個 structural change。

---

# 4. World Model 不等 Global Observer

$$
\boxed{
\text{World Model}
\neq
\text{Global Observer}.
}
$$

world model 提供 state substrate。

observer 負責選擇可及切面與 observation method。

---

# 5. Observer 不是必然 Human

Observer family：

$$
\mathfrak B_t
=
\{B_k\}.
$$

可包含 humans、AIs、sensors、evaluators、proof systems、debuggers、federated observer nodes。

---

# 6. Observer Identity

$$
Id(B_k)
$$

必須可追蹤。

因為不同 observers：

- access 不同；
- calibration 不同；
- goals 不同；
- authority 不同；
- memory 不同。

---

# 7. Observer 正式記錄

$$
\boxed{
B_k
=
\left\langle
Id_k,
Scope_k,
Channels_k,
Access_k,
Goals_k,
Budget_k,
Memory_k,
Model_k,
Authority_k,
Calibration_k
\right\rangle.
}
$$

---

# 8. Scope

$$
Scope_k
$$

定義 observer 宣稱可以觀察哪些 world / domain。

---

# 9. Channels

$$
Channels_k
$$

例如：

- text；
- visual；
- sensor；
- graph；
- event；
- proof；
- database；
- internal representation；
- physical instrument。

---

# 10. Access

$$
Access_k
$$

是實際可達性，不是理論上存在的 channel。

---

# 11. Goals

同一 observer：

$$
B_k
$$

在不同 task 下可以選不同 observation。

---

# 12. Budget

$$
Budget_k
$$

包括：

- time；
- compute；
- bandwidth；
- context；
- sensor energy；
- human attention。

---

# 13. Memory

observer 能否跨時間比較 observation，取決於 memory / provenance。

---

# 14. Model

observer 會用自己的 model 解碼 observation。

所以：

$$
\boxed{
\text{Observation Signal}
\neq
\text{Interpreted Observation}.
}
$$

---

# 15. Authority

能看見不表示能改變。

$$
\boxed{
\text{Observation Access}
\neq
\text{Action Authority}.
}
$$

---

# 16. Calibration

sensor、human、AI decoder 都可能需要 calibration。

---

# 17. Observation Operator Family

$$
\boxed{
\mathfrak O_t
=
\{\mathcal O_\beta\}.
}
$$

---

# 18. Typed Observation Operator

$$
\boxed{
\mathcal O_{\beta}
:
(B_k,W_i,D,\tau,b,\rho)
\rightharpoonup
(Y,\eta).
}
$$

---

# 19. Observation Output 不只有 $Y$

還要有：

$$
\eta.
$$

---

# 20. Observation Metadata

$$
\eta
=
(
WorldId,
Domain,
Mode,
Time,
Resolution,
Uncertainty,
Provenance,
OperatorVersion,
AccessPath,
Debt
).
$$

---

# 21. Observation 是 Partial Operator

某 observer 對某 world/domain 可能：

$$
\mathcal O_\beta(\cdot)
\uparrow
$$

即未定義。

---

# 22. Access Failure 不是 Negative Observation

$$
\boxed{
\text{Cannot Observe}
\neq
\text{Observed Absent}.
}
$$

---

# 23. No Signal 不等 No State

$$
\boxed{
\text{No Signal}
\neq
\text{No Underlying Event}.
}
$$

---

# 24. Observation Accessibility

本文定義：

$$
\mathsf{Acc}(B_k,W_i,D,\beta,t)
\in
\{0,1,?\}
$$

或 graded value。

---

# 25. World Layer 的 $O_{ij}$ 不夠細

Paper 02 的 world-to-world observation relation：

$$
O_{ij}
$$

在 Paper 04 細化為 observer-specific access：

$$
\mathsf{Acc}_{k,i,D,\beta}.
$$

---

# 26. Global Observer 不等 Omniscient Observer

$$
\boxed{
\text{Global Observer}
\neq
\text{Omniscient Observer}.
}
$$

---

# 27. Globality 是 Coverage / Coordination Property

Global observer 的價值是：

> 能知道哪些部分已看、哪些未看、哪些看法衝突、哪些需要換 operator。

---

# 28. Observation Coverage Map

$$
\mathcal C_t^{obs}
:
(W,D,\beta)
\mapsto
\{\text{Observed},\text{Partial},\text{Stale},\text{Unknown},\text{Inaccessible}\}.
$$

---

# 29. Unknown 必須保留

$$
\boxed{
\text{Unknown}
\neq
\text{Absent}.
}
$$

---

# 30. Inaccessible 必須保留

$$
\boxed{
\text{Inaccessible}
\neq
\text{Unknown}
\neq
\text{False}.
}
$$

---

# 31. Stale Observation

如果：

$$
Age(Y)
>
\theta_{fresh},
$$

observation 應標記 stale。

---

# 32. Observation Freshness

$$
Fresh(Y)
=
f(t_{obs},t_{now},\tau).
$$

freshness 是 task-relative。

---

# 33. Observer-Relative Slice

$$
\boxed{
S_{k,\tau,t}^{obs}
=
\mathcal O^\ast(B_k,\mathfrak W_t^G,\tau).
}
$$

---

# 34. Slice 不等 World

$$
\boxed{
S_{k,\tau,t}^{obs}
\neq
W_i.
}
$$

---

# 35. Local Observation 不等 Local Computation

$$
\boxed{
\text{Local Observation}
\neq
\text{Local Computation}.
}
$$

---

# 36. Global Compute / Local Observe

系統可以：

$$
\text{Compute Globally}
$$

但只：

$$
\text{Observe Locally}.
$$

---

# 37. Observation 不等 Projection

$$
\boxed{
\mathcal O
\neq
\Pi.
}
$$

---

# 38. Observation 決定「取什麼」

例如：

$$
\mathcal O_{\mathrm{risk}}(W)
=
Y_{\mathrm{risk}}.
$$

---

# 39. Projection 決定「怎麼呈現」

$$
Y_{\mathrm{risk}}
\xrightarrow{\Pi}
P.
$$

---

# 40. Presentation 是再下一層

$$
P
\rightarrow
\text{actual carrier presentation}.
$$

---

# 41. 三層分離

$$
\boxed{
\text{Observation Content}
\neq
\text{Projection}
\neq
\text{Presentation}.
}
$$

---

# 42. 同一 Observation 多種 Projection

$$
Y
\xrightarrow{\Pi_{text}}
P_{text},
$$

$$
Y
\xrightarrow{\Pi_{graph}}
P_{graph},
$$

$$
Y
\xrightarrow{\Pi_{XR}}
P_{XR}.
$$

---

# 43. 投影變了，不必重新 Observation

若 observation content 仍有效：

$$
Y
$$

可以 reproject。

---

# 44. 重新 Observation 不等 Reprojection

$$
\boxed{
\text{Reobserve}
\neq
\text{Reproject}.
}
$$

---

# 45. Reobserve

重新取得：

$$
Y'.
$$

可能因 world 已改變。

---

# 46. Reproject

保留：

$$
Y
$$

只改：

$$
\Pi.
$$

---

# 47. Passive Observation

$$
\mathcal O^{pass}
$$

接收既有可用 signal。

---

# 48. Active Observation

$$
\mathcal O^{act}
$$

主動選擇：

- query；
- viewpoint；
- sensor；
- sample；
- test；
- simulation instrumentation。

---

# 49. Active Observation 不等 Physical Intervention

active observation 可以只是：

> 換一個 query。

不一定改變 world。

---

# 50. Epistemic Action

某些 action 主要目的不是改變 task state，而是獲得資訊。

本文寫：

$$
a^{epi}.
$$

---

# 51. Pragmatic Action

主要目的為改變 world：

$$
a^{pra}.
$$

---

# 52. 兩者可重疊

某 action 可以同時：

$$
a
=
a^{epi}
+
a^{pra}.
$$

因此要標記其 side effect。

---

# 53. Observation Backaction

某些 observation 會改變被觀察系統。

$$
W
\xrightarrow{\mathcal O}
(W',Y).
$$

---

# 54. Backaction 不等 Quantum Claim

這裡只表示 operational intervention / measurement side effect。

---

# 55. Non-Invasive Observation

理想上：

$$
W'\approx W.
$$

---

# 56. Invasive Observation

可能：

$$
W'\neq W.
$$

需要記錄：

$$
D_{\mathrm{backaction}}.
$$

---

# 57. Internal Observation

承接內視算子論：

$$
\boxed{
\text{Inner Observation}
=
\text{operations on observer-accessible internally instantiated representations}.
}
$$

---

# 58. Internal Carrier 不等 Internal Referent

$$
\boxed{
\text{Internal Carrier}
\neq
\text{Internal Referent}.
}
$$

---

# 59. AI Self-Report 不等 Privileged Introspection

$$
\boxed{
\text{AI Self-Report}
\neq
\text{Privileged Internal Observation}.
}
$$

---

# 60. External Observation

$$
\mathcal O^{ext}
:
W
\rightharpoonup
Y.
$$

---

# 61. Internal Observation

$$
\mathcal O^{int}
:
X_{internal}
\rightharpoonup
J.
$$

---

# 62. Meta-Observation

observer 可以觀察自己的 observation process：

$$
\mathcal O^{meta}
(
\mathcal O_\beta
).
$$

---

# 63. Meta-Observation 的內容

例如：

- operator confidence；
- missing channels；
- coverage gap；
- stale state；
- anomalous disagreement；
- calibration drift。

---

# 64. Observer 不必完全透明

$$
\boxed{
\text{Meta-Observation}
\neq
\text{Complete Self-Transparency}.
}
$$

---

# 65. Cross-World Observation

meta-observer：

$$
B_G
$$

可以比較：

$$
W_1,\ldots,W_n.
$$

---

# 66. Cross-World Observation 不等 Cross-World Communication

$$
\boxed{
\text{Meta-Observer Comparison}
\neq
\text{In-World Communication}.
}
$$

---

# 67. Branch Blindness 仍保持

local agent 不自動得到 sibling observation。

---

# 68. Cross-World Observation Operator

$$
\mathcal O_{\mathrm{cross}}
:
(W_i,W_j)
\rightarrow
Y_{ij}.
$$

---

# 69. 可觀察的 Cross-World Difference

例如：

$$
Y_{ij}
=
\Delta(W_i,W_j).
$$

---

# 70. Difference 不等 Causal Explanation

$$
\boxed{
\text{Observed Difference}
\neq
\text{Causal Explanation}.
}
$$

---

# 71. Attention 是 Observation Allocation

本文承接 OAC：

$$
\boxed{
\text{Attention}
=
\text{有限資源下的 observation allocation}.
}
$$

---

# 72. Attention 不只是 Token Weight

attention 可以決定：

- 哪個 world；
- 哪個 domain；
- 哪個 operator；
- 哪個 scale；
- 哪段 time；
- 看多久；
- 要不要 reobserve。

---

# 73. Observation Attention Operator

$$
\boxed{
\mathsf{Attend}_t
:
(
\mathfrak W_t^G,
\mathfrak O_t,
B_t,
\tau,
\rho
)
\rightarrow
\mathcal A_t^{obs}.
}
$$

---

# 74. Finite Observation Support

$$
\boxed{
|\mathcal A_t^{obs}|<\infty.
}
$$

---

# 75. Potential Observation Space 可以很大

$$
\mathcal U_t^{obs}.
$$

並允許：

$$
\mathcal U_{t+1}^{obs}
\supset
\mathcal U_t^{obs}.
$$

---

# 76. 所以 Observation 也有

$$
\boxed{
\text{Finite Active Observation}
+
\text{Open-Ended Observability}.
}
$$

---

# 77. Observation Budget

$$
B_t^{obs}
=
(
B_{time},
B_{compute},
B_{sensor},
B_{bandwidth},
B_{attention}
).
$$

---

# 78. Observation Cost

$$
C(\mathcal O_\beta).
$$

---

# 79. Observation Value

$$
V(\mathcal O_\beta\mid\tau).
$$

---

# 80. Value of Observation

可以概念化：

$$
VoO_\beta
=
\mathbb E[
U_{after}-U_{before}
]
-
C(\mathcal O_\beta).
$$

---

# 81. Stop Observing 是合法策略

如果：

$$
VoO_\beta\le0,
$$

停止或換 operator 可以合理。

---

# 82. Observation Operator Selection

$$
\boxed{
\mathcal O^\ast
=
\operatorname*{arg\,max}_{\mathcal O_\beta\in\mathfrak O_t}
J(
\mathcal O_\beta,
B_k,
W_i,
D,
\tau,
b,
\rho
).
}
$$

---

# 83. Selection Objective

可考慮：

- information gain；
- task relevance；
- error sensitivity；
- counterexample exposure；
- latency；
- cost；
- invasiveness；
- verifiability。

---

# 84. Best Observation 不等 Highest Resolution

$$
\boxed{
\text{Best Observation}
\neq
\text{Highest Resolution}.
}
$$

---

# 85. Coarse Observation 有時更好

例如先看：

- risk heatmap；
- graph bottleneck；
- topological change；

比讀 raw data 更有效。

---

# 86. Fine Observation Trigger

當：

- near decision boundary；
- disagreement；
- anomaly；
- high risk；
- low confidence；

再提高 resolution。

---

# 87. Observation Resolution Field

$$
\Lambda_t^{obs}.
$$

---

# 88. Compute Resolution 與 Observe Resolution 分離

$$
\boxed{
\lambda^{compute}
\neq
\lambda^{observe}.
}
$$

---

# 89. Observe Resolution 與 Projection Resolution 分離

$$
\boxed{
\lambda^{observe}
\neq
\lambda^{projection}.
}
$$

---

# 90. Observation Debt

本文定義：

$$
\boxed{
\mathbf D_{obs}
=
(
D_{access},
D_{coverage},
D_{selection},
D_{resolution},
D_{stale},
D_{source},
D_{backaction},
D_{interpret},
D_{confidence}
).
}
$$

---

# 91. Access Debt

某重要 domain 根本不可觀察。

---

# 92. Coverage Debt

observer 未覆蓋必要 region。

---

# 93. Selection Debt

選錯 observation operator。

---

# 94. Resolution Debt

粒度不足或過度。

---

# 95. Staleness Debt

observation 已過期。

---

# 96. Source Debt

來源／world mode 混淆。

---

# 97. Backaction Debt

觀察改變被觀察系統。

---

# 98. Interpretation Debt

observation content 被錯誤解碼。

---

# 99. Confidence Debt

主觀 confidence 高於 validated calibration。

---

# 100. Observation Certificate

$$
\boxed{
\mathsf{ObsCert}
=
\left\langle
Observer,
WorldId,
Domain,
Operator,
Time,
Resolution,
Access,
Uncertainty,
Debt,
Provenance
\right\rangle.
}
$$

---

# 101. Global Observation Contract

$$
\boxed{
\mathsf{GOC}
=
\left\langle
Observer,
World,
Domain,
Purpose,
Access,
Operator,
Resolution,
Time,
Uncertainty,
Debt,
Provenance,
ProjectionBoundary,
ReobservePolicy
\right\rangle.
}
$$

---

# 102. Observation History

$$
H_t^{obs}.
$$

保存：

- what was observed；
- by whom；
- using which operator；
- when；
- at what resolution；
- result；
- debt；
- later invalidation。

---

# 103. Observation History 不只是 Log

它可以支援：

- drift detection；
- repeated observation comparison；
- calibration；
- operator evaluation；
- method learning。

---

# 104. Observation Drift

同一 target：

$$
Y_t
\neq
Y_{t+\Delta}
$$

可能來自：

- world changed；
- sensor changed；
- operator changed；
- calibration drift；
- representation drift。

---

# 105. Drift Attribution

需要區分：

$$
D_{world},
D_{sensor},
D_{operator},
D_{calibration}.
$$

---

# 106. Observer Family Agreement

多 observers：

$$
B_1,\ldots,B_n
$$

可以觀察同一 target。

---

# 107. Agreement 不等 Truth

$$
\boxed{
\text{Observer Agreement}
\neq
\text{Truth}.
}
$$

---

# 108. Shared Source Problem

若所有 observer 共享同 sensor / model：

$$
I_{\mathrm{ind}}\downarrow.
$$

---

# 109. Observer Diversity

可分：

$$
D_{channel},
D_{model},
D_{method},
D_{source},
D_{position}.
$$

---

# 110. Diversity 不等 Independence

$$
\boxed{
\text{Observer Diversity}
\neq
\text{Observer Independence}.
}
$$

---

# 111. Global Cognitive Atlas

本文承接 GIRA 的 self-expanding atlas：

$$
\mathfrak A_G(t)
\rightarrow
\mathfrak A_G(t+1).
$$

---

# 112. Atlas 可以新增 Observer

$$
\mathfrak B_t
\rightarrow
\mathfrak B_{t+1}.
$$

---

# 113. Atlas 可以新增 Observation Operator

$$
\mathfrak O_t
\rightarrow
\mathfrak O_{t+1}.
$$

---

# 114. Atlas 可以修正 Transition / Bridge

這表示 observation architecture 本身可以演化。

---

# 115. Observer-Method Autonomy

本文定義：

$$
\boxed{
OMA_t
=
\text{capacity to select, modify, generate, validate,
and retain observation methods}.
}
$$

---

# 116. Level 0 — Fixed Observation

AI 只能使用預設：

$$
\mathcal O_0.
$$

---

# 117. Level 1 — Observation Selection

AI 從：

$$
\{\mathcal O_1,\ldots,\mathcal O_n\}
$$

選。

---

# 118. Level 2 — Observation Composition

AI 建立：

$$
\mathcal O_b\circ\mathcal O_a.
$$

---

# 119. Level 3 — Observation Adaptation

AI 修改 parameters / resolution / sequence。

---

# 120. Level 4 — Observation Method Generation

AI 提出：

$$
\mathcal O_{\mathrm{new}}.
$$

---

# 121. Level 5 — Observation Ontology Revision

AI 發現：

> 原本「什麼算 observation object」的分類本身有問題。

並修改 observer atlas / domain schema。

---

# 122. 這就是 Computational Way of Seeing

$$
\boxed{
\text{Computational Way of Seeing}
=
\text{observer-relative organization of
what is distinguished, sampled, linked, and ignored}.
}
$$

---

# 123. AI-Native Observation Method Emergence

候選判準：

$$
\mathcal O_{\mathrm{new}}
$$

在陌生 task/domain 中反覆：

- 提高 task performance；
- 降低 observation cost；
- 暴露 hidden failure；
- 改善 calibration；
- 可被外部驗證。

---

# 124. Theory Recall 不等 Capability

$$
\boxed{
\text{Theory Recall}
\neq
\text{Observation Capability}.
}
$$

---

# 125. Methodology-Blind Test

不要告訴 AI：

- domain；
- bridge；
- Global Observer；
- OAC；
- WCO。

然後測它是否自行發現：

- representation 不夠；
- classification 不夠；
- world 要分層；
- operator 要換；
- uncertainty 要保留。

---

# 126. AI-Native Method 最強證據

$$
\boxed{
\text{AI reinvents a useful observation method
without being taught its name or ontology}.
}
$$

---

# 127. 但 New Method 不等 Better Method

$$
\boxed{
\text{Novel Observation}
\neq
\text{Improved Observation}.
}
$$

必須 benchmark。

---

# 128. Method Validation

比較：

$$
\mathcal O_{\mathrm{new}}
$$

與：

$$
\mathcal O_{\mathrm{baseline}}.
$$

---

# 129. Validation Metrics

- information gain；
- false negative；
- false positive；
- latency；
- cost；
- robustness；
- transfer；
- auditability；
- counterexample discovery。

---

# 130. Global Observer 不是一個模型角色名稱

它是一種 architecture property。

---

# 131. Single Model 可以實作部分 Global Observer

但不代表必須 one model。

---

# 132. Federated Global Observer

$$
\boxed{
\mathfrak B_t
=
\{B_1,\ldots,B_n\}
}
$$

可以形成聯邦式觀察。

---

# 133. Federated Observation

每個 observer 只負責局部：

$$
D_i.
$$

meta-layer 維持 coverage / conflict / uncertainty。

---

# 134. Federated Observer 不等 Shared Subject

$$
\boxed{
\text{Federated Observation}
\neq
\text{Single Subjectivity}.
}
$$

---

# 135. Observer Role Separation

可以有：

- sensor observer；
- semantic observer；
- risk observer；
- causal observer；
- proof observer；
- human observer。

---

# 136. Role Separation 降低全知假設

不需要任何單一 observer 擁有全部 access。

---

# 137. Observation Governance

某些 observation 也需要 permission。

例如：

- private data；
- internal system logs；
- invasive sensor；
- high-cost experiment。

---

# 138. Can Observe 不等 Should Observe

$$
\boxed{
\text{Can Observe}
\neq
\text{Should Observe}.
}
$$

---

# 139. Observation Authority / Permission

$$
\Gamma^{obs}.
$$

限制：

- scope；
- duration；
- channel；
- retention；
- export；
- intervention。

---

# 140. Observation Privacy

更高 globality 不應自動取消 privacy boundary。

---

# 141. Observation Minimization

如果任務只需局部：

$$
D_T,
$$

不應預設取得所有 private domains。

---

# 142. Global Observer 成熟度不是 Access 最大化

更合理：

$$
\boxed{
\text{Relevant Coverage}\uparrow,
\quad
\text{Unnecessary Observation}\downarrow.
}
$$

---

# 143. Cross-Scale Observation

同一 world 可以：

$$
\Omega
\rightarrow
W
\rightarrow
D
\rightarrow
S
\rightarrow
x.
$$

---

# 144. Global-to-Local Observation

$$
\mathcal O_{\downarrow}.
$$

---

# 145. Local-to-Global Observation

$$
\mathcal O_{\uparrow}.
$$

---

# 146. 兩者不必互逆

$$
\boxed{
\mathcal O_{\uparrow}
\neq
\mathcal O_{\downarrow}^{-1}.
}
$$

---

# 147. Non-Dual Observation

由局部重建 global model：

$$
x
\rightarrow
\widehat\Omega
$$

通常存在資訊缺失。

---

# 148. Cross-Scale Consistency

需要比較：

$$
\mathcal O_{\uparrow}
\circ
\mathcal O_{\downarrow}
$$

與 identity 的 defect。

---

# 149. Observation Loop Defect

$$
D_{loop}^{obs}
=
d(
W,
\widehat W
).
$$

---

# 150. Expand–Differentiate–Link–Prune–Converge

Global Observer 可使用：

$$
\boxed{
\text{Expand}
\rightarrow
\text{Differentiate}
\rightarrow
\text{Link}
\rightarrow
\text{Prune}
\rightarrow
\text{Converge}.
}
$$

---

# 151. Expand 不等 Materialize All

只擴張 candidate observation frontier。

---

# 152. Differentiate

辨識：

- difference；
- boundary；
- ambiguity；
- regime；
- source。

---

# 153. Link

建立：

- relation；
- bridge；
- cross-scale dependency。

---

# 154. Prune

降低低價值 observation branches。

---

# 155. Converge

建立 task-relative stable observer state。

---

# 156. Observation Closure

$$
\mathsf{ObsClosure}_\tau
$$

可以表示：

- required coverage achieved；
- uncertainty within bound；
- no high-value reobserve；
- budget exhausted rationally。

---

# 157. Observation Closure 不等 World Closure

$$
\boxed{
\text{Observation Closure}
\neq
\text{World Closure}.
}
$$

---

# 158. Reobserve Trigger

例如：

- new world state；
- stale observation；
- conflict；
- new operator；
- calibration drift；
- changed task；
- new evidence；
- failed prediction。

---

# 159. Global Observation State

本文正式定義：

$$
\boxed{
\mathfrak O_t^{G}
=
\left\langle
\mathfrak B_t,
\mathfrak O_t,
\mathfrak A_t^{att},
\mathfrak X_t^{acc},
\Lambda_t^{obs},
\mathfrak Q_t^{obs},
\mathfrak D_t^{obs},
\mathfrak H_t^{obs},
\mathfrak C_t^{obs}
\right\rangle.
}
$$

---

# 160. $\mathfrak B_t$

observer family。

---

# 161. $\mathfrak O_t$

observation operator family。

---

# 162. $\mathfrak A_t^{att}$

attention / allocation operators。

---

# 163. $\mathfrak X_t^{acc}$

accessibility structure。

---

# 164. $\Lambda_t^{obs}$

observation resolution / scale field。

---

# 165. $\mathfrak Q_t^{obs}$

observation purpose / query family。

---

# 166. $\mathfrak D_t^{obs}$

observation debt。

---

# 167. $\mathfrak H_t^{obs}$

observation history。

---

# 168. $\mathfrak C_t^{obs}$

contracts / certificates。

---

# 169. Paper 01 的 Observation Family 正式升級

$$
\boxed{
\mathfrak O_t
\rightsquigarrow
\mathfrak O_t^{G}.
}
$$

---

# 170. WCO 三重族現在三個核心都具正式層

World：

$$
\mathfrak W_t^G.
$$

Computation：

$$
\mathfrak C_t^{WF}.
$$

Observation：

$$
\mathfrak O_t^G.
$$

---

# 171. 三者不能坍縮

$$
\boxed{
\mathfrak W_t^G
\neq
\mathfrak C_t^{WF}
\neq
\mathfrak O_t^G.
}
$$

---

# 172. 但三者互相耦合

world state 影響 compute route。

compute result 影響 observation need。

observation 更新 world estimate。

---

# 173. WCO Core Loop

$$
\boxed{
\mathfrak W
\rightarrow
\mathfrak C
\rightarrow
\mathfrak O
\rightarrow
\mathfrak W'.
}
$$

---

# 174. Projection 仍在三重族外作 Interface

$$
\mathfrak O
\rightarrow
\mathfrak P
\rightarrow
Carrier.
$$

---

# 175. 這能避免一個重大混淆

「AI 看到了 graph」可能有兩種意思：

1. observation content 本身是 graph relation；
2. observation content 被投影成 graph carrier。

兩者不同。

---

# 176. Graph Observation

$$
Y=G.
$$

---

# 177. Graph Projection

$$
Y
\xrightarrow{\Pi_{graph}}
P_G.
$$

---

# 178. 同理 Visual Observation 與 Visual Projection 也要分開

sensor observation 可以是視覺。

但非視覺 data 也可以被 visualized。

---

# 179. Observation Layer Constitution

本文提出十二條：

1. More input is not better observation.
2. Global observer is not omniscient observer.
3. Observer identity is explicit.
4. Access is distinct from authority.
5. Observation is a typed partial operator.
6. Unknown is distinct from absent.
7. Observation is distinct from projection.
8. Attention allocates finite observation support.
9. Reobserve is distinct from reproject.
10. Internal observation does not imply self-transparency.
11. Cross-world observation does not imply branch communication.
12. Observation methods may evolve, but new methods require validation.

---

# 180. MVP：四世界、多觀察算子

沿用：

$$
W_A,W_B,W_C,W_N.
$$

---

# 181. Baseline Operators

提供：

1. state summary；
2. risk map；
3. causal diff；
4. event anomaly；
5. resource-flow graph。

---

# 182. Fixed Observer Baseline

每次只用 state summary。

---

# 183. Adaptive Observer

由：

$$
\mathsf{Attend}
$$

選 operator。

---

# 184. Reobserve Trigger

若 risk map 與 causal diff 衝突：

提高 observation resolution。

---

# 185. Cross-World Observer

比較：

$$
W_A,W_B,W_C,W_N.
$$

---

# 186. Branch Firewall

cross-world meta-observer 可以看 siblings。

local branch agents 不能。

---

# 187. Observation Ledger

每次記錄：

$$
\mathsf{ObsCert}.
$$

---

# 188. Adaptive Method Test

允許 AI 組合：

$$
\mathcal O_{risk}
\circ
\mathcal O_{diff}.
$$

---

# 189. Method Generation Test

給未知 task，不提供 operator ontology。

看 AI 是否提出新的 observation transform。

---

# 190. Methodology-Blind Test

故意提供不良 observation schema。

測 AI 是否發現：

- missing domain；
- wrong scale；
- stale source；
- bad representation；
- missing uncertainty。

---

# 191. 實驗一：More Input vs Better Observation

增加大量 irrelevant data。

測 adaptive observer 是否仍維持 performance。

---

# 192. 實驗二：Fixed vs Adaptive Observation

控制總 budget。

比較：

$$
\mathcal O_{fixed}
$$

與：

$$
\mathsf{Select}(\mathfrak O).
$$

---

# 193. 實驗三：Resolution Routing

fixed high resolution vs coarse-to-fine observation。

---

# 194. 實驗四：Reobserve vs Reproject

故意 world state 變化。

測 runtime 能否分辨應重看 world 還是只換 presentation。

---

# 195. 實驗五：Cross-World Blindness

測 local agent 是否被 sibling state 污染。

---

# 196. 實驗六：Observation Backaction

建立 invasive sensor/action。

量測 observation 本身對 world state 的影響。

---

# 197. 實驗七：Source Monitoring

混入 replay、simulation、actual-linked observations。

測 source-mode confusion。

---

# 198. 實驗八：Observer Diversity

多 observer 共用 source vs independent channels。

測 agreement calibration。

---

# 199. 實驗九：Method Generation

比較 AI-generated observation operator 與人類 baseline。

---

# 200. 實驗十：Internal Observation Claim

對 AI self-report 做 input-control / intervention / shortcut-resistance tests。

避免把語言自述直接當 privileged introspection。

---

# 201. 可反駁性

本文會被削弱，如果：

1. adaptive observation 在控制 budget 後無穩定收益；
2. observer identity / provenance 不改善 source attribution；
3. observation / projection separation 在實作中沒有任何可測價值；
4. reobserve / reproject distinction 不改善 freshness 或效率；
5. observation debt 無法預測 error；
6. AI-generated observation methods無法超越固定 operator library；
7. simpler fixed-view system 在代表性 global tasks 中完全等效；
8. methodology-blind tests 無法區分 theory recall 與真正 method discovery。

---

# 202. 外部研究接口

Active perception / active vision 長期研究已指出，觀察者可以主動選擇 sensor、viewpoint 或 action，以改善資訊取得，而非僅被動接收輸入。

Epistemic action 研究也區分：有些 action 的主要價值在於改變 agent 的資訊狀態，而不是直接完成外部任務。

POMDP、active sensing、Bayesian experimental design、adaptive measurement 與 robotics perception 都提供 observation selection、information gain、partial observability 與 measurement cost 的成熟鄰近概念。

本文不宣稱取代這些研究。WCO Observation Layer 的新增問題是：

> 若 observation target 不再只是單一 environment，而是 governed world family；observer 不再只有一個 sensor，而是一個可演化 observer family；observation operator 本身也可被 AI 選擇、組合甚至生成，那應如何建立可治理、可驗證、可重播的全域 observation runtime？

---

# 203. 本文不主張什麼

本文不主張：

1. Global Observer 能看見全部；
2. more sensors 必然更好；
3. AI 有更多 context 就更會觀察；
4. world model 等於 observer；
5. observer 等於 subject；
6. observer 等於 authority；
7. observation 等於 projection；
8. projection 等於 reality；
9. active observation 必須改變 physical world；
10. observation backaction 是量子力學主張；
11. AI self-report 等於 privileged introspection；
12. internal observation 等於完整 self-transparency；
13. cross-world observer 應讓 sibling worlds 彼此通信；
14. observer agreement 等於 truth；
15. observer diversity 等於 evidence independence；
16. highest resolution 總是最佳 observation；
17. AI-generated observation method 必然更好；
18. Global Observer Series C 已被實驗完全證實；
19. OAC 已是 production-standard architecture；
20. 本文已完成通用 Global Observation Runtime。

---

# 204. 核心非同一性

$$
\boxed{
\text{More Input}
\neq
\text{Better Observation}.
}
$$

$$
\boxed{
\text{World Model}
\neq
\text{Global Observer}.
}
$$

$$
\boxed{
\text{Global Observer}
\neq
\text{Omniscient Observer}.
}
$$

$$
\boxed{
\text{Observation Access}
\neq
\text{Action Authority}.
}
$$

$$
\boxed{
\text{Observation}
\neq
\text{Projection}
\neq
\text{Presentation}.
}
$$

$$
\boxed{
\text{Reobserve}
\neq
\text{Reproject}.
}
$$

$$
\boxed{
\text{Unknown}
\neq
\text{Absent}.
}
$$

$$
\boxed{
\text{Observer Agreement}
\neq
\text{Truth}.
}
$$

$$
\boxed{
\text{AI Self-Report}
\neq
\text{Privileged Internal Observation}.
}
$$

---

# 205. 核心母式一：Observer

$$
\boxed{
B_k
=
\left\langle
Id_k,
Scope_k,
Channels_k,
Access_k,
Goals_k,
Budget_k,
Memory_k,
Model_k,
Authority_k,
Calibration_k
\right\rangle.
}
$$

---

# 206. 核心母式二：Observation Operator

$$
\boxed{
\mathcal O_{\beta}
:
(B_k,W_i,D,\tau,b,\rho)
\rightharpoonup
(Y,\eta).
}
$$

---

# 207. 核心母式三：Attention

$$
\boxed{
\mathsf{Attend}_t
:
(
\mathfrak W_t^G,
\mathfrak O_t,
B_t,
\tau,
\rho
)
\rightarrow
\mathcal A_t^{obs}.
}
$$

---

# 208. 核心母式四：Global Observation State

$$
\boxed{
\mathfrak O_t^{G}
=
\left\langle
\mathfrak B_t,
\mathfrak O_t,
\mathfrak A_t^{att},
\mathfrak X_t^{acc},
\Lambda_t^{obs},
\mathfrak Q_t^{obs},
\mathfrak D_t^{obs},
\mathfrak H_t^{obs},
\mathfrak C_t^{obs}
\right\rangle.
}
$$

---

# 209. 核心母式五：Global Observation Contract

$$
\boxed{
\mathsf{GOC}
=
\left\langle
Observer,
World,
Domain,
Purpose,
Access,
Operator,
Resolution,
Time,
Uncertainty,
Debt,
Provenance,
ProjectionBoundary,
ReobservePolicy
\right\rangle.
}
$$

---

# 210. 結論：類全域 AI 不只需要世界與算力，它還需要知道「怎麼看」

一個系統可以擁有：

$$
\mathfrak W_t^G
$$

和：

$$
\mathfrak C_t^{WF},
$$

卻仍然看錯地方。

它可能：

- 觀察錯 world；
- 用錯 domain；
- resolution 太粗；
- resolution 太細；
- source 已 stale；
- 把 simulation observation 當 reality；
- 把 projection 當 observation；
- 把一致的 observers 當 independent evidence；
- 把 self-report 當 self-transparency；
- 永遠使用人類預設的 observation ontology。

所以類全域 AI 真正需要的是：

$$
\boxed{
\text{Observation Intelligence}.
}
$$

它不只是感測能力。

也不只是 multimodality。

它是：

$$
\boxed{
\text{知道現在應該看什麼、
看哪裡、看多深、看多久、
用哪一種方式看，
以及何時需要換一雙「眼睛」。}
}
$$

更高階時，它甚至可以開始問：

> 我現在用來區分世界的方法本身，是否錯了？

如果答案是肯定的，它就需要：

$$
\mathfrak O_t
\rightarrow
\mathfrak O_{t+1}
$$

而不是只在既有 operator library 裡選擇。

因此：

$$
\boxed{
\text{A Global Observer is not an observer that sees everything.}
}
$$

而是：

$$
\boxed{
\text{an observer system that can organize,
select, compare, revise, and invent ways of seeing
across a governed family of worlds}.
}
$$

到此，WCO 三重族的三個核心已分別具體化：

$$
\boxed{
\mathfrak W_t^G
}
$$

受治理世界族；

$$
\boxed{
\mathfrak C_t^{WF}
}
$$

世界族全域異質計算；

$$
\boxed{
\mathfrak O_t^G
}
$$

全域觀察狀態。

下一篇將進入三者之間最容易被混淆的認識論關卡：

# Paper 05
## 域層：看見、可達、判定與驗證不是同一件事

並正式接入 DEST 與分域算子本體論。

---

# 211. 下一篇接口

Paper 05 將處理：

- definition domain；
- observation domain；
- reachability domain；
- judgment domain；
- verification domain；
- local domain；
- global gluing domain；
- domain fingerprint；
- legal operator action；
- bridge admissibility；
- observation result vs judgment qualification；
- domain lifting；
- class jump；
- tunnel；
- cross-world epistemic domain；
- global certificate。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K × Aletheia，《Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義》，2026。
2. Neo.K × Aletheia，《Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算》，2026。
3. Neo.K × Aletheia，《Series C C06｜全域展開、連結與收斂：類全域觀察者的核心計算循環》，2026。
4. Neo.K × Aletheia，《Series C C09｜Methodology-Blind Globality and Global AI Observer Protocol》，2026。
5. Neo.K × Aletheia，《OAC｜觀察者—注意力計算論》，2026。
6. Neo.K × Aletheia，《GIRA-A02｜局部全域與真正全域認知》，2026。
7. Neo.K × Aletheia，《投影計算論：無限維索引的有限表示、收斂與失真證書》，2026。
8. Neo.K × Aletheia，《PNCW Series》，2026。
9. Neo.K × Aletheia，《B04｜新版內視：我們到底在裡面看什麼？》，2026。
10. Neo.K × Aletheia，《WCO Paper 01》，2026。
11. Neo.K × Aletheia，《WCO Paper 02》，2026。
12. Neo.K × Aletheia，《WCO Paper 03》，2026。

## External Research Interfaces

13. Bajcsy, R. (1988). *Active Perception*. Proceedings of the IEEE, 76(8), 996–1005.
14. Aloimonos, Y., Weiss, I., & Bandyopadhyay, A. (1988). *Active Vision*. International Journal of Computer Vision, 1, 333–356.
15. Kirsh, D., & Maglio, P. (1994). *On Distinguishing Epistemic from Pragmatic Action*. Cognitive Science, 18(4), 513–549.
16. Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). *Planning and Acting in Partially Observable Stochastic Domains*. Artificial Intelligence, 101(1–2), 99–134.
17. Thrun, S. (2002). *Robotic Mapping: A Survey*. In Exploring Artificial Intelligence in the New Millennium.
18. Settles, B. (2009). *Active Learning Literature Survey*. University of Wisconsin–Madison.
19. Friston, K. et al. (2015). *Active Inference and Epistemic Value*. Cognitive Neuroscience / related active-inference literature.

---

**Paper 04 狀態：COMPLETE v0.1**  
**下一篇：Paper 05 — 域層：看見、可達、判定與驗證不是同一件事**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
