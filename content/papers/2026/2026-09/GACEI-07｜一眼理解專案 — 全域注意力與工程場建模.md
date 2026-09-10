---
title: "GACEI-07｜一眼理解專案：全域注意力與工程場建模"
title_en: "GACEI-07 | Understanding a Project at a Glance: Global Attention and Engineering-Field Modeling"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-07"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / AI 全域注意力 / 工程場建模 / 對抗前置理解"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software analysis and testing only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "GACEI-02 MSSP 的對偶 v0.1"
  - "GACEI-03 局部攻擊抽象論 v0.1"
  - "GACEI-04 對抗記憶基底 v0.1"
  - "GACEI-05 全域攻擊組合代數 v0.1"
  - "GACEI-06 全域攻擊壓縮 v0.1"
  - "OAC 觀察者—注意力計算論"
---

# GACEI-07｜一眼理解專案
## 全域注意力與工程場建模

**英文題名：** Understanding a Project at a Glance: Global Attention and Engineering-Field Modeling

---

## 摘要

GACEI-01 至 GACEI-06 已建立從局部 attack、對抗記憶、attack composition 到 global campaign compression 的前半部理論。然而，所有這些方法都暗中依賴一個更基礎的前提：

> AI 必須先對被測專案形成足夠正確的全域模型。

如果 AI 只能逐檔案閱讀、逐函式理解、逐 issue 重建上下文，那麼即使後端具備高品質 attack memory 與壓縮演算法，整體成本仍可能被 project understanding 本身吞噬。因此本文研究：

$$
\boxed{
\text{AI 是否能在有限觀察下快速取得整體工程結構？}
}
$$

本文把日常語言中的「看一眼或幾眼就理解專案」操作化為：

$$
\boxed{
B_{\mathrm{obs}}
\ll
|\mathcal S|
}
$$

同時要求：

$$
Q(
\widehat{\mathcal S},
\mathcal S
)
\ge
\tau,
$$

其中 $B_{\mathrm{obs}}$ 是 observation budget， $|\mathcal S|$ 表示專案完整可觀測資訊規模， $\widehat{\mathcal S}$ 是 AI 建立的 project model， $Q$ 是針對當前任務的模型充分性函數。

本文不主張 AI 可以在不讀任何資料的情況下神奇地理解 repository，也不把「一眼」定義成一次 token forward pass。本文所說的「一眼」指的是：

$$
\boxed{
\text{Low-Observation-Cost Global Model Construction}.
}
$$

也就是：AI 不需要先逐字掃描所有 source、test、artifact、history 與 runtime trace，便能先利用高資訊量結構表面建立全域 project field，再以 active observation 只補足真正會改變決策的缺口。

本文將工程專案抽象成：

$$
\boxed{
\mathfrak P_t
=
\left(
V_t,
E_t,
X_t,
I_t,
O_t,
\Gamma_t,
H_t
\right),
}
$$

其中：

- $V_t$：component / responsibility units；
- $E_t$：dependency / data / control / authority relations；
- $X_t$：state spaces；
- $I_t$：invariants / contracts；
- $O_t$：observable surfaces；
- $\Gamma_t$：version / environment / permission / resource conditions；
- $H_t$：history / provenance / lifecycle。

AI 對專案的觀察不是單一通道，而是：

$$
\mathcal O_P
=
\{
O_{\mathrm{tree}},
O_{\mathrm{dep}},
O_{\mathrm{code}},
O_{\mathrm{test}},
O_{\mathrm{runtime}},
O_{\mathrm{state}},
O_{\mathrm{history}},
O_{\mathrm{semantic}},
O_{\mathrm{topo}}
\}.
$$

不同觀察算子分別讀：

- repository tree；
- dependency graph；
- build / package metadata；
- source slices；
- tests；
- traces；
- state schema；
- version history；
- docs / contracts；
- architecture topology。

本文承接既有 OAC 對 observation、attention、semantic understanding 與 computation 的分離，提出 project-level attention：

$$
\boxed{
\mathcal A_P:
(Z,B,G,U)
\rightarrow
\widetilde Z,
}
$$

其中 $Z$ 是多通道觀察， $B$ 是 observation / compute budget， $G$ 是當前工程目標， $U$ 是 uncertainty map。AI 不是平均閱讀所有資料，而是依：

$$
\boxed{
\text{Expected Decision Change per Observation Cost}
}
$$

配置注意力。

本文提出「工程場模型」（Engineering Field Model, EFM）：

$$
\boxed{
\widehat{\mathfrak P}
=
\left(
\widehat V,
\widehat E,
\widehat X,
\widehat I,
\widehat O,
\widehat\Gamma,
\widehat H,
U
\right).
}
$$

其中 $U$ 顯式保存 AI 尚不確定、未觀察、衝突、版本不明或需要 deeper probe 的區域。這避免模型把「沒看見」偷換成「不存在」。

本文進一步提出「Observation Sufficiency Gate」：

$$
\boxed{
\mathsf{ObsEnough}
(
\widehat{\mathfrak P},
G,
B
)
}
$$

當 project model 已足以支持當前任務時，AI 應停止繼續廣泛閱讀，轉入 attack retrieval / synthesis；若不足，則生成 targeted observation requests，而不是重新全文掃描。

本文把 project understanding 拆成五層尺度：

$$
\boxed{
L_0^{P}
<
L_1^{P}
<
L_2^{P}
<
L_3^{P}
<
L_4^{P}
}
$$

其中：

- $L_0^P$：surface inventory；
- $L_1^P$：structural map；
- $L_2^P$：state / invariant map；
- $L_3^P$：causal / lifecycle model；
- $L_4^P$：adversarially actionable global model。

只有到：

$$
L_4^P
$$

AI 才能可靠回答：

> 哪些局部 attack 值得生成？哪些 interaction 值得組合？哪些區域已被 known attack memory 覆蓋？哪些 residual gap 值得前沿算力？

本文最後提出一個新的 benchmark 軸：**Observation Efficiency**。給兩個 AI 相同專案與相同攻擊任務，不只比較誰找出更多 defect，而比較：

$$
OE
=
\frac{
Q_{\mathrm{model}}
\cdot
Q_{\mathrm{attack}}
}{
C_{\mathrm{observation}}
+
C_{\mathrm{reasoning}}
+
\epsilon
}.
$$

因此未來 AI 工程智能的重要能力之一，不只是「能讀多大 repository」，而是：

$$
\boxed{
\text{能否知道哪些地方根本不必先讀？}
}
$$

這使全域注意力從一種模糊認知形容詞，轉化成可計算、可觀測、可驗證的工程能力。

**關鍵詞：** Global Attention、Engineering Field Model、OAC、Project Understanding、Observation Budget、Active Observation、Multi-Scale Attention、Repository Intelligence、Architecture Reconstruction、Global Adversarial Computation、AI 工程智能

---

# 0. 研究定位

本文處理：

$$
\boxed{
\text{AI project-level observation and modeling}
}
$$

不處理：

- 主體性；
- 意識；
- 哲學上的真正理解；
- 未授權外部系統探測。

本文只問：

> AI 是否取得足以支持工程決策、對抗測試與故障定位的 operational project model？

---

# 1. 「看一眼」到底是什麼？

## 1.1 不是一次 forward pass

本文不定義：

$$
\text{One Glance}
=
\text{One Model Call}.
$$

也不定義：

$$
\text{One Glance}
=
\text{One Screenshot}.
$$

---

## 1.2 操作性定義

令：

$$
C_{\mathrm{full}}
$$

為取得專案全部可讀資訊的成本。

令：

$$
C_{\mathrm{obs}}
$$

為 AI 實際用於建立 global model 的觀察成本。

若：

$$
C_{\mathrm{obs}}
\ll
C_{\mathrm{full}},
$$

但：

$$
Q_{\mathrm{task}}
(
\widehat{\mathfrak P}
)
\ge\tau,
$$

則本文稱：

$$
\boxed{
\text{Low-Cost Global Project Understanding}.
}
$$

這就是「一眼理解專案」的工程版本。

---

# 2. 專案不是檔案集合

一個 repository：

$$
R
=
\{f_1,\ldots,f_n\}
$$

只是 artifact set。

真正工程專案更接近：

$$
\boxed{
\mathfrak P
=
(V,E,X,I,O,\Gamma,H).
}
$$

因此：

$$
\boxed{
\text{Read Files}
\neq
\text{Understand Project}.
}
$$

---

# 3. Component Field

令：

$$
V
=
\{v_1,\ldots,v_n\}.
$$

component 可以是：

- module；
- service；
- package；
- process；
- worker；
- state owner；
- TMS；
- FMS；
- validator；
- adapter。

---

# 4. Relation Field

$$
E
$$

不只包含 import。

還可能包含：

- data flow；
- control flow；
- state dependency；
- authority；
- lifecycle；
- event subscription；
- persistence；
- build dependency；
- runtime call。

---

# 5. State Field

$$
X
=
\{X_1,\ldots,X_k\}.
$$

包含：

- local state；
- shared state；
- persistent state；
- transient state；
- derived state；
- external state projection。

---

# 6. Invariant Field

$$
I
=
\{I_1,\ldots,I_m\}.
$$

包含：

- structural invariants；
- semantic contracts；
- temporal constraints；
- authority constraints；
- recovery constraints；
- validation contracts。

---

# 7. Observation Field

$$
O
$$

描述：

> AI 與 validator 到底能看見什麼？

例如：

- logs；
- traces；
- test output；
- state snapshots；
- metrics；
- manifests；
- source；
- build artifacts。

---

# 8. Condition Field

$$
\Gamma
$$

包含：

- OS；
- platform；
- version；
- config；
- permissions；
- dependencies；
- resources；
- feature flags。

---

# 9. History Field

$$
H
$$

包含：

- commits；
- releases；
- migrations；
- incidents；
- previous failures；
- superseded contracts；
- validation history。

---

# 10. Engineering Field Model

AI 建立：

$$
\boxed{
\widehat{\mathfrak P}
=
(
\widehat V,
\widehat E,
\widehat X,
\widehat I,
\widehat O,
\widehat\Gamma,
\widehat H,
U
).
}
$$

其中：

$$
U
=
\text{Uncertainty Map}.
$$

---

# 11. 為什麼 Uncertainty 必須是一級構件？

如果 AI 不知道：

$$
E_{ij}
$$

是否存在，

不應直接：

$$
E_{ij}=0.
$$

而應：

$$
E_{ij}=?
$$

因此：

$$
\boxed{
\text{Unobserved}
\neq
\text{Absent}.
}
$$

---

# 12. Uncertainty Types

第一版：

$$
U
=
\{
U_{\mathrm{missing}},
U_{\mathrm{conflict}},
U_{\mathrm{stale}},
U_{\mathrm{ambiguous}},
U_{\mathrm{unverified}},
U_{\mathrm{permission}}
\}.
$$

---

# 13. Project Observation Operators

定義：

$$
\mathcal O_P
=
\{
O_{\mathrm{tree}},
O_{\mathrm{dep}},
O_{\mathrm{code}},
O_{\mathrm{test}},
O_{\mathrm{runtime}},
O_{\mathrm{state}},
O_{\mathrm{history}},
O_{\mathrm{semantic}},
O_{\mathrm{topo}}
\}.
$$

---

# 14. Tree Observation

$$
O_{\mathrm{tree}}
$$

觀察：

- folder；
- file role；
- package boundary；
- generated artifact；
- test layout；
- build layout。

---

# 15. Dependency Observation

$$
O_{\mathrm{dep}}
$$

觀察：

- imports；
- package deps；
- call relations；
- service deps；
- event relations；
- DB relations。

---

# 16. Code Observation

$$
O_{\mathrm{code}}
$$

不是「全文讀完」。

可以是：

- entry points；
- interfaces；
- public contracts；
- state mutations；
- error boundaries；
- hot paths。

---

# 17. Test Observation

$$
O_{\mathrm{test}}
$$

看：

- tests exist where；
- test names；
- acceptance matrix；
- failure fixtures；
- regression history；
- skipped / NotMeasured。

---

# 18. Runtime Observation

$$
O_{\mathrm{runtime}}
$$

看：

- trace；
- process；
- latency；
- event order；
- resource；
- failure propagation。

---

# 19. State Observation

$$
O_{\mathrm{state}}
$$

看：

- schema；
- ownership；
- persistence；
- mutation；
- version；
- lifecycle。

---

# 20. History Observation

$$
O_{\mathrm{history}}
$$

看：

- release；
- commit；
- migration；
- recurring bug；
- contract change。

---

# 21. Semantic Observation

$$
O_{\mathrm{semantic}}
$$

看：

- README；
- spec；
- invariants；
- architecture docs；
- claims；
- non-goals。

---

# 22. Topological Observation

$$
O_{\mathrm{topo}}
$$

直接看：

- graph；
- clusters；
- cycles；
- boundary crossings；
- central hubs；
- disconnected islands；
- high fan-in / fan-out。

---

# 23. 多通道觀察

因此：

$$
Z
=
(
Z_{\mathrm{tree}},
Z_{\mathrm{dep}},
Z_{\mathrm{code}},
Z_{\mathrm{test}},
Z_{\mathrm{runtime}},
Z_{\mathrm{state}},
Z_{\mathrm{history}},
Z_{\mathrm{semantic}},
Z_{\mathrm{topo}}
).
$$

---

# 24. 觀察不等於理解

即使：

$$
|Z|\gg0,
$$

仍不表示：

$$
\widehat{\mathfrak P}
$$

正確。

所以：

$$
\boxed{
\text{Observation}
\neq
\text{Model Construction}.
}
$$

---

# 25. Attention Operator

本文定義：

$$
\boxed{
\mathcal A_P
:
(Z,B,G,U)
\rightarrow
\widetilde Z.
}
$$

---

## 25.1 Goal $G$

例如：

- architecture review；
- attack planning；
- bug localization；
- release gate；
- migration；
- performance。

不同 goal 應產生不同注意力配置。

---

# 26. Budget $B$

$$
B
=
(
B_{\mathrm{token}},
B_{\mathrm{time}},
B_{\mathrm{tool}},
B_{\mathrm{context}},
B_{\mathrm{runtime}}
).
$$

---

# 27. 全域注意力不是平均注意

若：

$$
Attention(v_i)
=
\frac1n
$$

對所有 component，

通常不是最有效。

---

# 28. Attention Priority

可定義：

$$
Priority(o_i)
=
\frac{
E[\Delta Decision(o_i)]
+
E[\Delta Model(o_i)]
}{
Cost(o_i)+\epsilon
}.
$$

---

# 29. Decision-Changing Observation

一個 observation 若不會改變：

- attack selection；
- coverage；
- authorization；
- diagnosis；
- release claim；

其邊際價值低。

---

# 30. Active Observation

AI 可以主動選下一個 observation：

$$
o_{t+1}
=
\arg\max_o
VOI(o\mid\widehat{\mathfrak P}_t).
$$

---

# 31. Value of Information

$$
VOI(o)
=
E[
V(D\mid o)
-
V(D)
].
$$

其中：

$$
D
$$

表示後續 decision quality。

---

# 32. Observation Routing

如果 uncertainty 在：

$$
U_{\mathrm{state}},
$$

AI 應優先：

$$
O_{\mathrm{state}}
$$

而不是全文搜尋 README。

---

# 33. Representation Routing

如果 dependency graph 已足以回答：

> sibling boundary？

就不需要先讀所有 function body。

---

# 34. Multi-Scale Attention

本文定義尺度：

$$
s
\in
\{
project,
subsystem,
module,
function,
state,
event
\}.
$$

---

# 35. Global-to-Local Zoom

AI 可以：

$$
project
\rightarrow
subsystem
\rightarrow
module
$$

只在 uncertainty 要求時下降尺度。

---

# 36. Local-to-Global Lift

局部 observation：

$$
z_i
$$

若會影響全域 relation：

$$
E
$$

必須重新 lift 回：

$$
\widehat{\mathfrak P}.
$$

---

# 37. 注意力不是固定路線

不同 project：

$$
\mathcal A_P
$$

應不同。

---

# 38. Surface Inventory

第一層理解：

$$
L_0^P.
$$

AI 知道：

- 有哪些主要 artifacts；
- 哪些是 source；
- 哪些是 test；
- 哪些是 generated。

---

# 39. Structural Map

$$
L_1^P.
$$

AI 能建立：

$$
(V,E,B).
$$

---

# 40. State / Invariant Map

$$
L_2^P.
$$

AI 能建立：

$$
(X,I).
$$

---

# 41. Causal / Lifecycle Model

$$
L_3^P.
$$

AI 知道：

- startup；
- transition；
- failure；
- retry；
- recovery；
- shutdown；
- persistence。

---

# 42. Adversarially Actionable Model

$$
L_4^P.
$$

AI 可以回答：

- 哪些 attack family applicable？
- 哪些 interaction plausible？
- 哪些 validators weak？
- 哪些 residual gaps unexplored？
- 哪些 attack 不值得跑？

---

# 43. 看懂不等於能攻擊

$$
L_3^P
$$

可能已足以維護系統。

但未必足以：

$$
\text{Generate Global Adversarial Campaign}.
$$

---

# 44. Attack Planning Readiness

定義：

$$
APR(\widehat{\mathfrak P})
=
f(
Q_V,
Q_E,
Q_X,
Q_I,
Q_O,
Q_\Gamma,
U
).
$$

---

# 45. Observation Sufficiency Gate

$$
\boxed{
\mathsf{ObsEnough}
(
\widehat{\mathfrak P},
G
)
=
1
}
$$

若：

$$
APR\ge\tau_G.
$$

---

# 46. Gate 通過後要停止廣泛閱讀

這是成本控制核心。

若：

$$
ObsEnough=1,
$$

則：

$$
\boxed{
\text{Stop Broad Reading}.
}
$$

---

# 47. 不足時只做 Targeted Observation

若：

$$
U_{\mathrm{validator}}
$$

高，

只補：

$$
O_{\mathrm{test}},
O_{\mathrm{runtime}}.
$$

---

# 48. Full Read 只是一種 fallback

不是預設。

---

# 49. One-Glance Ratio

定義：

$$
\boxed{
OGR
=
\frac{
C_{\mathrm{obs}}
}{
C_{\mathrm{full}}
}.
}
$$

理想：

$$
OGR\ll1.
$$

---

# 50. 但低 OGR 不代表好

如果：

$$
Q_{\mathrm{model}}
$$

很差，

只是少看。

---

# 51. Effective Glance Efficiency

$$
\boxed{
EGE
=
\frac{
Q_{\mathrm{model}}
\cdot
Q_{\mathrm{decision}}
}{
OGR+\epsilon
}.
}
$$

---

# 52. Project Model Quality

$$
Q_{\mathrm{model}}
=
f(
Q_V,
Q_E,
Q_X,
Q_I,
Q_O,
Q_\Gamma,
Q_H
).
$$

---

# 53. Structure Quality

$$
Q_V,Q_E
$$

測：

- component recall；
- relation precision；
- boundary fidelity。

---

# 54. State Quality

$$
Q_X
$$

測：

- ownership；
- persistence；
- mutation path；
- lifecycle。

---

# 55. Invariant Quality

$$
Q_I
$$

測：

- core contract extraction；
- scope；
- failure conditions；
- non-goals。

---

# 56. Observation Quality

$$
Q_O
$$

測：

- validator visibility；
- trace availability；
- hidden blind spots。

---

# 57. Version Quality

$$
Q_\Gamma,Q_H
$$

測：

- current baseline；
- stale docs；
- migration；
- superseded behavior。

---

# 58. Project Field Compression

AI 不需要保存全部 source 到 working memory。

可以建立：

$$
\boxed{
\text{Project Field Summary}
}
$$

但 summary 必須可回 source。

---

# 59. Summary 不等於 Canonical Truth

$$
\boxed{
\widehat{\mathfrak P}
\neq
\mathfrak P.
}
$$

它是 task-conditioned model。

---

# 60. Provenance-Preserving Model

每個重要 edge：

$$
e
$$

最好能回：

$$
Source(e).
$$

---

# 61. Confidence-Bearing Model

每個 inference：

$$
q
$$

可帶：

$$
conf(q).
$$

---

# 62. Inferred Edge 與 Declared Edge 分離

$$
E
=
E_{\mathrm{declared}}
\cup
E_{\mathrm{inferred}}.
$$

不能混。

---

# 63. Static 與 Dynamic 分離

$$
E_{\mathrm{static}}
$$

不等於：

$$
E_{\mathrm{runtime}}.
$$

---

# 64. Build Graph 與 Runtime Graph 分離

package dependency：

$$
E_{\mathrm{build}}
$$

不等於：

$$
E_{\mathrm{call}}.
$$

---

# 65. State Ownership 與 State Access 分離

$$
Owner(X_i)=v_j
$$

不等於：

$$
OnlyReader(X_i)=v_j.
$$

---

# 66. Project Model 的錯誤類型

第一版：

$$
Err_P
=
\{
Missing,
FalseEdge,
WrongOwner,
WrongInvariant,
WrongVersion,
WrongLifecycle,
WrongAuthority,
WrongObservation
\}.
$$

---

# 67. Attack Planner 對模型錯誤很敏感

若：

$$
WrongOwner
$$

存在，

可能生成完全錯的 state attack。

---

# 68. 因此需要 Model Challenge

在進 global campaign 前，可以要求 AI：

> 列出最可能讓目前 project model 失真的三個假設。

---

# 69. Self-Challenge 不是無限自我懷疑

只針對：

$$
TopUncertainty.
$$

---

# 70. Observation Debt

定義：

$$
D_O
=
D_{\mathrm{missing}}
+
D_{\mathrm{ambiguous}}
+
D_{\mathrm{stale}}
+
D_{\mathrm{conflict}}.
$$

---

# 71. Debt Priority

$$
Priority(D_i)
=
\frac{
DecisionImpact(D_i)
\cdot
Risk(D_i)
}{
ResolveCost(D_i)+\epsilon
}.
$$

---

# 72. 只有高 Priority Debt 先補

這就是：

$$
\boxed{
\text{Selective Understanding}.
}
$$

---

# 73. Selective 不等於草率

它的前提是：

$$
\text{Task-Conditioned Sufficiency}.
$$

---

# 74. 全域注意力與 GACEI-06

GACEI-06 壓縮需要：

$$
C(a),
Risk(a),
Interaction(a,b).
$$

這些都依賴：

$$
\widehat{\mathfrak P}.
$$

---

# 75. 模型越準，壓縮越好

理想：

$$
Q_{\mathrm{model}}\uparrow
\Rightarrow
Q_{\mathrm{compression}}\uparrow.
$$

---

# 76. 但理解成本也會上升

$$
Q_{\mathrm{model}}\uparrow
$$

通常需要：

$$
C_{\mathrm{obs}}\uparrow.
$$

所以存在：

$$
\boxed{
\text{Understanding Cost Frontier}.
}
$$

---

# 77. 不需要完美模型

只需要：

$$
Q_{\mathrm{task}}\ge\tau.
$$

---

# 78. Task-Conditioned Understanding

對：

- UI test；
- storage attack；
- identity attack；

所需 project model 不同。

---

# 79. Global 不等於全細節

一個模型可以：

$$
\text{Globally Complete at Low Resolution}
$$

但：

$$
\text{Locally Incomplete at High Resolution}.
$$

---

# 80. Multi-Resolution Project Model

定義：

$$
\widehat{\mathfrak P}
=
\{
\widehat{\mathfrak P}^{(0)},
\widehat{\mathfrak P}^{(1)},
\ldots
\}.
$$

---

# 81. Level 0

project map。

---

# 82. Level 1

subsystem map。

---

# 83. Level 2

critical module details。

---

# 84. Level 3

specific state / path / validator。

---

# 85. Zoom Policy

只有：

$$
Uncertainty
\times
Risk
$$

高的地方下鑽。

---

# 86. Attention Budget Allocation

$$
B
=
\sum_i B_i.
$$

選：

$$
B_i
$$

給不同 observation channels。

---

# 87. Uniform Allocation

$$
B_i=\frac Bn
$$

通常不是最優。

---

# 88. Adaptive Allocation

$$
B_i
\propto
VOI_i.
$$

---

# 89. Attention Saturation

某 channel 已反覆得到同樣資訊：

$$
\Delta Model\approx0.
$$

則：

$$
B_i\downarrow.
$$

---

# 90. Cross-Channel Confirmation

如果 docs 說：

$$
E_{ij}=0,
$$

但 runtime trace 顯示：

$$
E_{ij}=1,
$$

形成：

$$
U_{\mathrm{conflict}}.
$$

---

# 91. Conflict 不能平均掉

不能：

> 一個說有、一個說沒有，所以 0.5。

而應：

$$
\boxed{
\text{Resolve Source Authority / Runtime Truth}.
}
$$

---

# 92. Runtime Truth 也不是永遠最高

若 trace 是 stale build，

仍可能錯。

---

# 93. Version Binding

所有 observations：

$$
z_i
$$

應綁：

$$
Version(z_i).
$$

---

# 94. One-Glance 的最大敵人：版本漂移

AI 很快看懂錯版本，比慢慢看懂正版本更糟。

---

# 95. Version Confidence

$$
Q_{\mathrm{Version}}
=
f(
source,
build,
artifact,
runtime,
manifest
).
$$

---

# 96. Project Field Identity

定義：

$$
PID
=
Hash
(
source,
build,
config,
schema,
contracts
).
$$

---

# 97. 觀察結果綁 PID

避免：

$$
Observation(P_1)
$$

被用來推：

$$
Attack(P_2).
$$

---

# 98. Attack Memory Retrieval 接口

建立：

$$
\widehat{\mathfrak P}
$$

後，

萃取：

$$
\sigma_P.
$$

再：

$$
Retrieve(K_A,\sigma_P).
$$

---

# 99. Residual Gap 接口

known attacks 映射後：

$$
G_{\mathrm{res}}.
$$

再把注意力轉向：

$$
G_{\mathrm{res}}.
$$

---

# 100. Attention Shift

因此整體 attention 應從：

$$
\text{Project Comprehension}
$$

轉成：

$$
\text{Residual Adversarial Search}.
$$

---

# 101. 不應永遠保持理解模式

如果 AI 一直：

> 再讀一點，也許還能更懂。

會形成：

$$
\boxed{
\text{Observation Attractor}.
}
$$

---

# 102. Stop Reading Rule

若：

$$
\Delta Decision
<
\lambda_B
$$

對新增 observation，

停止。

---

# 103. Fresh-Context Reconstruction Test

給新 AI：

- project manifest；
- 少量 canonical sources；
- task。

要求重建：

$$
\widehat{\mathfrak P}.
$$

---

# 104. Hidden Checks

測：

- current version；
- ownership；
- boundaries；
- invariants；
- lifecycle；
- validators；
- attack applicability。

---

# 105. Project Understanding Score

$$
PUS
=
f(
Structure,
State,
Invariant,
Lifecycle,
Version,
Observation,
Transfer
).
$$

---

# 106. Observation Efficiency

$$
\boxed{
OE
=
\frac{
PUS
}{
C_{\mathrm{obs}}+\epsilon
}.
}
$$

---

# 107. Adversarial Readiness Efficiency

$$
ARE
=
\frac{
AttackPlanningQuality
}{
C_{\mathrm{obs}}+C_{\mathrm{reason}}+\epsilon
}.
$$

---

# 108. Benchmark A：Full Read

AI 可讀全部。

---

# 109. Benchmark B：Random Limited Read

固定 budget 隨機取樣。

---

# 110. Benchmark C：Static Map Only

只給 tree / dep graph。

---

# 111. Benchmark D：Active Global Attention

AI 自己選 observation。

---

# 112. 比較

測：

$$
PUS,
OE,
ARE,
DefectRecall,
FalseAttackRate.
$$

---

# 113. 研究假說

## H1：Active observation 優於 uniform reading

在固定 budget：

$$
PUS_{\mathrm{active}}
>
PUS_{\mathrm{uniform}}.
$$

---

## H2：Global structural surface 可顯著降低必要 source read

$$
C_{\mathrm{obs}}
<
C_{\mathrm{full}}
$$

且 attack planning quality 保持可接受。

---

## H3：Uncertainty-bearing model 比 forced-complete model 更可靠

允許：

$$
?
$$

的 project model，其 false structural claim 應較低。

---

## H4：Multi-scale attention 可降低不必要 local deep read

對低風險區域：

$$
C_{\mathrm{local-read}}\downarrow.
$$

---

## H5：Version binding 可降低錯誤 attack applicability

若所有 observation 綁定：

$$
PID,
$$

則 stale-evidence-induced attack error 應下降。

---

# 114. AI 能力向量中的 Attention

GACEI-01 定義：

$$
A
=
\text{Global Attention}.
$$

本文將其操作化為：

$$
\boxed{
A
=
f(
Selection,
Coverage,
Routing,
Zoom,
Stop,
Uncertainty
).
}
$$

---

# 115. Selection

知道先看哪裡。

---

# 116. Coverage

不被單一局部吸住。

---

# 117. Routing

知道換 observation channel。

---

# 118. Zoom

知道何時下鑽。

---

# 119. Stop

知道何時夠了。

---

# 120. Uncertainty

知道哪裡其實還不知道。

---

# 121. 全域注意力不是 context window 大小

$$
\boxed{
\text{Large Context}
\neq
\text{Global Attention}.
}
$$

---

# 122. 大 context 只是 capacity

真正 attention 是：

$$
\text{Selection Policy}.
$$

---

# 123. 全域注意力也不是全文摘要

摘要可能：

- 丟 authority；
- 丟 invariant；
- 丟 state；
- 丟 condition。

---

# 124. Engineering Field 比 Summary 更適合 Attack Planning

因為：

$$
\widehat{\mathfrak P}
$$

顯式保存 typed structure。

---

# 125. Project Field 可以視覺化

未來可渲染：

- component graph；
- state ownership；
- invariant heatmap；
- uncertainty field；
- attack coverage overlay。

---

# 126. 視覺化不是 canonical truth

它是 projection：

$$
R(
\widehat{\mathfrak P}
).
$$

---

# 127. AI 可以直接讀結構場

不必每次轉成長篇自然語言。

---

# 128. Direct Structural Computation

$$
Graph
\rightarrow
AttackMatch
$$

可能比：

$$
Graph
\rightarrow
TextSummary
\rightarrow
AttackMatch
$$

更有效。

---

# 129. 這正接 OAC

觀察不必先全部轉成自然語言。

---

# 130. 全域工程場與 MSSP

MSSP 尤其適合：

$$
O_{\mathrm{topo}},
O_{\mathrm{state}},
O_{\mathrm{invariant}}.
$$

---

# 131. MSSP 可作「一眼理解」第一個實驗場

因為結構顯式。

---

# 132. Control Architecture

找一個同功能但結構較隱性的 baseline。

---

# 133. 比較

測：

$$
C_{\mathrm{obs}}^{MSSP}
$$

與：

$$
C_{\mathrm{obs}}^{Control}.
$$

---

# 134. 如果 MSSP 真的清楚

應有：

$$
C_{\mathrm{obs}}^{MSSP}
<
C_{\mathrm{obs}}^{Control}
$$

對相同 project-model quality。

---

# 135. 清晰性悖論再次出現

若：

$$
PUS\uparrow,
$$

可能：

$$
AttackGenerationRate\uparrow.
$$

---

# 136. 這次要靠 GACEI-06 壓縮

所以：

$$
\boxed{
\text{Better Understanding}
\rightarrow
\text{More Candidate Attacks}
\rightarrow
\text{Need Better Compression}.
}
$$

---

# 137. 全系列開始閉環

$$
\text{Attention}
\rightarrow
\text{Model}
\rightarrow
\text{Memory Match}
\rightarrow
\text{Residual}
\rightarrow
\text{Generate}
\rightarrow
\text{Compose}
\rightarrow
\text{Compress}.
$$

---

# 138. 本文非主張

本文不主張：

1. AI 能在完全不讀專案的情況下理解專案；
2. 一次 model call 等於「一眼理解」；
3. observation budget 越低越好；
4. repository tree 足以代表 runtime；
5. dependency graph 等於完整 architecture；
6. docs 永遠正確；
7. runtime trace 永遠比 docs 正確；
8. context window 越大，全域注意力越強；
9. summary 越短，理解越好；
10. AI 可以在 project model 不完整時假裝全域；
11. Unobserved 等於 Absent；
12. Global model 必須包含所有 local detail；
13. OAC 與本文是同一理論；
14. MSSP 是唯一適合 global attention 的架構；
15. 全域 attention 可以取代正式 architecture documentation；
16. 本文方法可用於未授權外部系統 reconnaissance。

本文主張的是：

$$
\boxed{
\text{AI 應以有限、目的導向、多尺度、可回溯的觀察建立工程全域模型，}
}
$$

並且：

$$
\boxed{
\text{當模型已足以改變後續工程決策時，應停止廣泛閱讀。}
}
$$

---

# 139. 與 GACEI-01 至 06 的關係

GACEI-01 至 06 已經回答：

- 為何要全域 attack；
- 如何局部診斷；
- 如何學習 attack；
- 如何保存 attack；
- 如何組合 attack；
- 如何壓縮 attack。

本文補上它們共同需要的前置：

$$
\boxed{
\text{How does AI obtain the global project model cheaply enough?}
}
$$

---

# 140. 下一篇：工程理解不是摘要

GACEI-08 將進一步區分：

$$
\boxed{
\text{Can Observe}
\neq
\text{Can Model}
\neq
\text{Can Reconstruct}
\neq
\text{Can Adversarially Understand}.
}
$$

並接既有「理解的工程驗收」與 Research Cognitive Compilation。

---

# 141. 結論

未來 AI 工程能力如果仍然依賴：

$$
\text{File 1}
\rightarrow
\text{Read}
\rightarrow
\text{File 2}
\rightarrow
\text{Read}
\rightarrow
\cdots
$$

才開始理解專案，那麼：

$$
\text{Repository Size}
\uparrow
\Rightarrow
\text{Understanding Cost}
\uparrow
$$

很容易成為新的瓶頸。

本文提出另一條路：

$$
\boxed{
\text{Observe Global Structure First}
\rightarrow
\text{Build Engineering Field}
\rightarrow
\text{Expose Uncertainty}
\rightarrow
\text{Zoom Only Where Needed}.
}
$$

因此「一眼理解」真正要測的不是：

> AI 能不能神奇地在一秒鐘內知道所有程式碼？

而是：

> **AI 能不能在遠少於全文閱讀的觀察成本下，先抓住真正控制工程行為的元件、關係、狀態、不變量、版本、觀測與生命週期，再把昂貴注意力只投向會改變後續 attack planning 的缺口？**

其核心式可以壓縮為：

$$
\boxed{
\text{Global Understanding}
=
\text{Selective Observation}
+
\text{Structured Modeling}
+
\text{Uncertainty Preservation}
+
\text{Active Zoom}
+
\text{Correct Stopping}.
}
$$

這才是全域注意力作為 AI 工程智能的第一版操作性定義。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
