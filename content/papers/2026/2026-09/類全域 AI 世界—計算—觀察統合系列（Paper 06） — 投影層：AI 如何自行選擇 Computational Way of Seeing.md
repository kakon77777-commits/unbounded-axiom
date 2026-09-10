# 類全域 AI 世界—計算—觀察統合系列（Paper 06）
## 投影層：AI 如何自行選擇 Computational Way of Seeing
### The Projection Layer: How AI Selects and Generates Computational Ways of Seeing

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 06 / 12  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** Projection Computation × Cognitive Projection Compiler × PNCW × DEST Representation Escape × Global Observer × Domain Qualification × AI-Native Representation Runtime × Multi-Carrier Cognition  
**前篇：** Paper 05《域層：看見、可達、判定與驗證不是同一件事》  
**狀態：** 投影層母規格／CPC 2.0 架構；不宣稱所有問題都存在高效表示逃逸，不宣稱換表示即可提升真實性或驗證資格

---

## 摘要

Paper 04 已建立 Global Observation State：

$$
\mathfrak O_t^G,
$$

Paper 05 則建立 Domain Qualification State：

$$
\mathfrak D_t^{WCO}.
$$

然而，一個 observation content：

$$
Y
$$

即使已被合法取得，也仍不直接等於任何特定文字、圖像、3D 場景、表格、張量、聲音、觸覺或 XR view。類全域 AI 必須進一步決定：

> 這個 observation 應該以什麼 representation／carrier 被呈現與操作？

本文提出 WCO-TF 的正式 **Projection Layer**。其核心不是「render output」，而是把 observation content、task invariants、epistemic qualification、observer properties、carrier capabilities、resource budget、risk 與 projection debt 共同編譯成可操作 view。

本文定義 **Global Projection State（GPS）**：

$$
\boxed{
\mathfrak P_t^G
=
\left\langle
\mathfrak P_t,
\mathfrak C_t^{carrier},
\mathfrak R_t^{repr},
\Lambda_t^{proj},
\mathfrak I_t^{task},
\mathfrak D_t^{proj},
\mathfrak H_t^{proj},
\mathfrak C_t^{cert},
\mathfrak T_t^{trans}
\right\rangle.
}
$$

其中：

- $\mathfrak P_t$：projection operator family；
- $\mathfrak C_t^{carrier}$：carrier family；
- $\mathfrak R_t^{repr}$：representation family；
- $\Lambda_t^{proj}$：projection resolution / fidelity field；
- $\mathfrak I_t^{task}$：task-relative invariant family；
- $\mathfrak D_t^{proj}$：projection debt；
- $\mathfrak H_t^{proj}$：projection history；
- $\mathfrak C_t^{cert}$：projection / translation certificates；
- $\mathfrak T_t^{trans}$：projection transition / round-trip contracts。

本文將既有 Cognitive Projection Compiler 升級為 **CPC 2.0**：

$$
\boxed{
\mathsf{CPC}_2
:
(
Y,
\mathsf{QCap},
B_o,
\tau,
b,
\rho,
\mathsf{Cap}
)
\rightarrow
(
\Pi^\ast,
c^\ast,
r^\ast,
P^\ast,
\mathsf{Audit}
).
}
$$

其中：

- $Y$：observation content；
- $\mathsf{QCap}$：Paper 05 的 qualification capsule；
- $B_o$：observer model；
- $\tau$：task；
- $b$：budget；
- $\rho$：risk；
- $\mathsf{Cap}$：carrier capability descriptors；
- $\Pi^\ast$：選定 projection operator；
- $c^\ast$：carrier；
- $r^\ast$：representation grammar / rendering regime；
- $P^\ast$：projected object；
- $\mathsf{Audit}$：debt、source、invariant、certificate 與 transition record。

這使 projection selection 不再只是 UI 決策，而是：

$$
\boxed{
\text{Projection Selection}
=
\text{task-relative semantic compilation}.
}
$$

本文承接投影計算論：有限計算不是無限對象的縮小複本，而是帶任務、精度與證書的有限影。不存在對所有可能 query 都普適充分的單一有限影，因此：

$$
\boxed{
\text{No Universal Best Projection}.
}
$$

真正問題是：

$$
\boxed{
\Pi^\ast
=
\operatorname*{arg\,min}_{\Pi}
C(\Pi)
}
$$

subject to：

$$
\boxed{
E(\Pi)\le\varepsilon,
}
$$

以及：

$$
\boxed{
\operatorname{Preserve}_{\tau}
(\mathcal I_{\tau})=1.
}
$$

某些 task 甚至可能存在多個不可比較的 Pareto-minimal projections：

$$
\Pi_1^\ast,
\Pi_2^\ast,
\ldots
$$

因此 projection family 可以保持 plurality，不必硬選唯一「最佳視圖」。

本文再承接 DEST-09 的 Representation Escape。若：

$$
x\notin D^{judge}_{\pi_1}
$$

但：

$$
x\in D^{judge}_{\pi_2},
$$

AI 可以提出：

$$
\mathsf{Escape}
:
(x,\pi_1)
\rightharpoonup
(x',\pi_2,\tau_{12}).
$$

但任何表示逃逸都必須通過 identity、task equivalence、loss、cost、certificate 與 globality gates。換表示不是免費魔法：

$$
\boxed{
\text{Representation Escape}
\neq
\text{Problem Relaxation}
\neq
\text{Approximation}
\neq
\text{Oracle Use}.
}
$$

本文因此定義 **Projection Navigation Contract（PNC）**：

$$
\boxed{
\mathsf{PNC}(\phi)
=
\left\langle
Dom,
Cod,
TaskInv,
Identity,
Equivalence,
Loss,
Cost,
Risk,
Certificate,
QualificationEffect,
GlobalityEffect,
Rollback
\right\rangle.
}
$$

並再次固定 Paper 05 的防錯規則：

$$
\boxed{
\text{Projection Change}
\not\Rightarrow
\text{Epistemic Qualification Upgrade}.
}
$$

AI 可以因新 projection 更容易判斷，但這最多表示：

$$
D^{judge}_{\pi_1}
\rightarrow
D^{judge}_{\pi_2}
$$

的資格改變；若要：

$$
D^{judge}
\rightarrow
D^{verify},
$$

仍必須支付 verification debt。

本文進一步區分兩種以前容易混在一起的能力：

### Observation-Method Autonomy

AI 決定：

> 從 world 取什麼？

即：

$$
\mathcal O_{\mathrm{new}}.
$$

### Projection-Method Autonomy

AI 決定：

> 已取得的 observation content 應如何重新表示？

即：

$$
\Pi_{\mathrm{new}}.
$$

因此：

$$
\boxed{
\text{Observation-Method Autonomy}
\neq
\text{Projection-Method Autonomy}.
}
$$

兩者共同構成更完整的：

$$
\boxed{
\text{Computational Way of Seeing}.
}
$$

本文將 **Computational Way of Seeing（CWoS）** 定義為：

$$
\boxed{
\mathsf{CWoS}
=
(
\mathcal O,
\Pi,
c,
\lambda,
\mathcal I,
\mathsf{QCap},
\mathsf{Audit}
).
}
$$

也就是「取什麼」與「如何看」的組合，而不只是某種顯示風格。

本文最後提出 **Projection-Method Autonomy（PMA）** 五級：

1. 固定 projection；
2. 從既有 projection library 選擇；
3. 組合／重參數化既有 projection；
4. 自適應生成新的 projection grammar；
5. 發現原 carrier family 本身不足，提出新的 carrier / representation regime。

PMA Level 5 並不表示 AI 可以憑空創造新物理材料；它只表示 AI 可以提出「現有 carrier 不足」並產生新的 carrier specification / research requirement。Paper 07 才處理其物理實現。

本文最終提出：

$$
\boxed{
\text{The future of AI cognition is not a single better view.}
}
$$

而是：

$$
\boxed{
\text{a runtime that can compile, compare, revise,
and sometimes invent better views when needed}.
}
$$

**關鍵詞：** Cognitive Projection Compiler、Projection Computation、Representation Escape、Computational Way of Seeing、Projection Method Autonomy、PNCW、Carrier、Finite Projection、Projection Debt、Qualification Laundering

---

# 0. Paper 05 留下的問題

Paper 05 已能回答：

> 這個 observation 有什麼 epistemic qualification？

但仍缺：

> 應該怎麼把它表現出來？

---

# 1. Observation Content 不等 Projection

$$
\boxed{
Y
\neq
P.
}
$$

 $Y$ 是取得的結構。

 $P$ 是 carrier-relative representation。

---

# 2. Projection 不等 Presentation

$$
\boxed{
P
\neq
Presentation(P).
}
$$

presentation 是最後實際被 human/machine receptor 接收的 surface。

---

# 3. Projection 不等 Rendering

$$
\boxed{
\text{Projection}
\neq
\text{Rendering}.
}
$$

rendering 只是某些 projection 的末端實現。

---

# 4. Representation 不等 Carrier

graph 是 representation grammar。

screen / XR / machine tensor memory 是 carrier。

兩者可以分開。

---

# 5. Carrier 不等 Observer

$$
\boxed{
Carrier
\neq
Observer.
}
$$

同一 screen 上的 view 可以給不同 observers。

---

# 6. World 不等 View

$$
\boxed{
W
\neq
Y
\neq
P.
}
$$

---

# 7. Projection Family

$$
\boxed{
\mathfrak P_t
=
\{\Pi_\gamma\}.
}
$$

---

# 8. Carrier Family

$$
\boxed{
\mathfrak C_t^{carrier}
=
\{
c_{text},
c_{2D},
c_{3D},
c_{graph},
c_{XR},
c_{audio},
c_{haptic},
c_{AI},
\ldots
\}.
}
$$

---

# 9. Representation Family

$$
\mathfrak R_t^{repr}
$$

可以包含：

- sequence；
- table；
- graph；
- tree；
- tensor；
- topology；
- causal diagram；
- field；
- event stream；
- symbolic term；
- multi-layer canvas。

---

# 10. Same Carrier, Different Representation

screen 上可以顯示：

- text；
- graph；
- map；
- plot；
- 3D viewport。

---

# 11. Same Representation, Different Carrier

graph 可以存在於：

- screen；
- printed page；
- XR；
- AI-native memory；
- haptic encoding。

---

# 12. Projection Operator

$$
\Pi:
Y
\rightharpoonup
P.
$$

---

# 13. Projection 是 Partial

不是所有 observation content 都可合法投影到任何 carrier。

---

# 14. Carrier Capability

定義：

$$
\boxed{
\mathsf{Cap}(c)
=
(
Dim,
Bandwidth,
Latency,
Resolution,
Persistence,
Interactivity,
MachineReadability,
HumanReadability,
Safety,
Cost
).
}
$$

---

# 15. CPC 必須知道 Carrier Capability

否則會產生 physically or cognitively impossible projection。

---

# 16. Observer Model

$$
B_o
=
(
Knowledge,
SensoryChannels,
CognitiveLimits,
Language,
Goals,
Preferences,
Calibration
).
$$

---

# 17. Preference 不等 Evidence Semantics

$$
\boxed{
Personalization
\neq
EvidencePersonalization.
}
$$

可以改 layout，不可改 claim status。

---

# 18. Task Invariant

對 task：

$$
\tau
$$

定義：

$$
\boxed{
\mathcal I_\tau
=
\{I_1,\ldots,I_m\}.
}
$$

---

# 19. Task Invariant 可以是

- identity；
- ordering；
- exact truth；
- feasibility；
- uncertainty；
- branch distinction；
- source identity；
- permission；
- error tolerance。

---

# 20. Projection 必須保存必要 Invariants

$$
\boxed{
Preserve_\Pi(\mathcal I_\tau)=1.
}
$$

---

# 21. 不要求保存全部資訊

因為有限影本質上會丟資訊。

---

# 22. Task-Relative Sufficiency

$$
\boxed{
\Pi_\lambda
\models
Suff(K,\mathcal Q_0,\varepsilon).
}
$$

---

# 23. Sufficiency 不是 Projection 的絕對屬性

它依賴：

- object class；
- query family；
- error tolerance；
- priors；
- task。

---

# 24. No Universal Best Projection

$$
\boxed{
\text{No Universal Best Projection}.
}
$$

---

# 25. 無普適有限影的直覺

不同 world states：

$$
i\neq j
$$

可能：

$$
\Pi(i)=\Pi(j).
$$

所以有限 view 一定可能隱藏可區分結構。

---

# 26. Projection Fiber

$$
\Pi^{-1}(p)
$$

可能含多個 underlying states。

---

# 27. View Collision

$$
\boxed{
\Pi(W_a)=\Pi(W_b)
\not\Rightarrow
W_a=W_b.
}
$$

---

# 28. Projection Collision 是 Observation Risk

若 query 恰好依賴被折疊差異，該 projection 不充分。

---

# 29. Minimal Sufficient Projection

$$
\Lambda_{ok}
=
\{
\lambda:
E(\lambda)\le\varepsilon
\}.
$$

若有最小：

$$
\lambda^\ast
=
\min\Lambda_{ok}.
$$

---

# 30. 可能沒有唯一最小

不同方向可能形成 Pareto frontier。

---

# 31. Projection Selection 是 Multi-Objective

$$
\mathbf J(\Pi)
=
(
TaskFidelity,
Access,
Cost,
Latency,
CognitiveLoad,
ComputeCost,
Debt,
Auditability
).
$$

---

# 32. CPC 2.0

$$
\boxed{
\mathsf{CPC}_2
:
(
Y,
QCap,
B_o,
\tau,
b,
\rho,
Cap
)
\rightarrow
(
\Pi^\ast,
c^\ast,
r^\ast,
P^\ast,
Audit
).
}
$$

---

# 33. CPC 不等 Renderer

$$
\boxed{
CPC
\neq
Renderer.
}
$$

---

# 34. CPC 不等 Observer

$$
\boxed{
CPC
\neq
ObservationOperator.
}
$$

Observer 取 content。

CPC 編譯 view。

---

# 35. CPC 不等 Verifier

$$
\boxed{
CPC
\neq
Verifier.
}
$$

它不能因投影更清楚就提升 claim status。

---

# 36. CPC Input 必須包含 QCap

因為 projection 必須顯示／保留：

- simulation；
- branch-dependent；
- unverified；
- stale；
- scope restriction。

---

# 37. Qualification-Aware Projection

$$
\boxed{
P
=
\Pi(Y,QCap).
}
$$

---

# 38. UI Status 不是 Decoration

`Verified`、`Simulated`、`BranchDependent` 等 status 是 semantic obligation。

---

# 39. Qualification Laundering Guard

CPC 必須拒絕：

$$
Judged
\rightarrow
Verified
$$

只因 layout change。

---

# 40. Projection Debt

本文定義：

$$
\boxed{
\mathbf D_{proj}
=
(
D_{loss},
D_{distort},
D_{uncertainty},
D_{source},
D_{semantic},
D_{scale},
D_{temporal},
D_{cognitive},
D_{carrier},
D_{transition}
).
}
$$

---

# 41. Loss Debt

省略必要結構。

---

# 42. Distortion Debt

幾何／比例／關係被扭曲。

---

# 43. Uncertainty Debt

不確定性被隱藏。

---

# 44. Source Debt

world mode / evidence source 被抹掉。

---

# 45. Semantic Debt

同符號在不同 domain 被混同。

---

# 46. Scale Debt

display scale 被誤認為 native scale。

---

# 47. Temporal Debt

stale state 被顯示成 current。

---

# 48. Cognitive Debt

view 超過 observer 可處理負荷。

---

# 49. Carrier Debt

carrier 本身不適合該 structure。

---

# 50. Transition Debt

reprojection 造成 identity continuity loss。

---

# 51. Projection Audit

$$
\boxed{
PAudit
=
\left\langle
Source,
WorldId,
QCap,
Observer,
Task,
Carrier,
Transform,
Invariants,
Debt,
Uncertainty,
Validation,
Alternatives
\right\rangle.
}
$$

---

# 52. Designed Perceptual World

$$
\boxed{
DPW_t
=
CPC_2(
Y,QCap,B_o,\tau,b,\rho,Cap
).
}
$$

---

# 53. DPW 不等 World

$$
\boxed{
DPW
\neq
W
\neq
\mathcal R.
}
$$

---

# 54. DPW 可以 Mixed-Carrier

$$
DPW
=
\{
P_{text},
P_{graph},
P_{XR},
P_{audio},
P_{haptic},
P_{AI}
\}.
$$

---

# 55. Human View 與 AI View 可以不同

$$
P_H
\neq
P_{AI}.
$$

---

# 56. 但共享 Canonical Referent

兩者應有：

$$
Ref(P_H)=Ref(P_{AI})
$$

或明示 mapping。

---

# 57. Humanization Layer

$$
P_H
=
\Pi_{AI\rightarrow H}(P_{AI}).
$$

---

# 58. Humanization 不是 Screenshot

它是 translation。

---

# 59. Machine Compilation

$$
P_{AI}
=
\Pi_{H\rightarrow AI}(P_H).
$$

---

# 60. Translation 產生 Debt

$$
D_{H\rightarrow AI},
\quad
D_{AI\rightarrow H}.
$$

---

# 61. Round-Trip Test

$$
P_H
\rightarrow
P_{AI}
\rightarrow
P_H'.
$$

---

# 62. Round-Trip Debt

$$
D_{round}
=
d(P_H,P_H').
$$

---

# 63. Round-Trip Fidelity 不等 Truth

$$
\boxed{
D_{round}\approx0
\not\Rightarrow
CanonicalModelCorrect.
}
$$

---

# 64. Reprojection

同一 observation：

$$
Y
$$

可以：

$$
P_t
\rightarrow
P_{t+1}.
$$

---

# 65. Reprojection Trigger

- task changed；
- observer changed；
- carrier changed；
- budget changed；
- risk changed；
- projection debt discovered。

---

# 66. Reprojection 不等 Reobserve

$$
\boxed{
Reprojection
\neq
Reobservation.
}
$$

---

# 67. Projection Transition Contract

$$
\boxed{
PTC
=
(
Cause,
OldView,
NewView,
InvariantMap,
QualificationMap,
DebtDiff,
Rollback
).
}
$$

---

# 68. Identity Continuity

dynamic view 改變時需維持 object permanence。

---

# 69. User 應可問「為什麼 View 變了？」

系統應提供：

$$
Reason(P_t\rightarrow P_{t+1}).
$$

---

# 70. Projection Transition 可以回滾

如果新 projection 造成認知失敗：

$$
Rollback(P_{t+1}\rightarrow P_t).
$$

---

# 71. 但 Projection Rollback 不等 World Rollback

$$
\boxed{
ProjectionRollback
\neq
WorldRollback.
}
$$

---

# 72. Projection Computation 與七種有限化操作

$$
\boxed{
Projection
\neq
Truncation
\neq
Discretization
\neq
Sampling
\neq
Quantization
\neq
Compression
\neq
Surrogate.
}
$$

---

# 73. CPC 必須記錄每一層操作

否則 debt source 無法定位。

---

# 74. Projection Chain

$$
Y
\rightarrow
\Pi(Y)
\rightarrow
Sample
\rightarrow
Quantize
\rightarrow
Compress
\rightarrow
Render.
$$

---

# 75. 每一 Arrow 都是不同 Error Source

因此 Audit 要分層。

---

# 76. Representation Escape

若原 representation：

$$
\pi_1
$$

造成判定困難，可提出：

$$
Escape:
(x,\pi_1)
\rightharpoonup
(x',\pi_2,\tau_{12}).
$$

---

# 77. Escape 不等換皮

必須存在 task-level improvement 或 domain qualification gain。

---

# 78. Task Equivalence

$$
x
\sim_{\mathcal Q}
x'.
$$

---

# 79. Equivalence 必須聲明類型

例如：

- EXACT；
- DECISION_EQUIVALENT；
- OPTIMUM_PRESERVING；
- APPROXIMATION_PRESERVING；
- CERTIFICATE_PRESERVING；
- ONE_WAY_REDUCTION；
- HEURISTIC_ONLY。

---

# 80. One-Way Reduction 不等雙向等價

$$
\boxed{
x\leq_T x'
\not\Rightarrow
x'\leq_T x.
}
$$

---

# 81. Projection Navigation Contract

$$
\boxed{
PNC(\phi)
=
\left\langle
Dom,
Cod,
TaskInv,
Identity,
Equivalence,
Loss,
Cost,
Risk,
Certificate,
QualificationEffect,
GlobalityEffect,
Rollback
\right\rangle.
}
$$

---

# 82. Navigation Operators

$$
\{
Fold,
Bridge,
Project,
Lift,
Compress,
Reparam,
ClassJump,
Tunnel
\}.
$$

---

# 83. Fold

把 task-equivalent states 收斂到較小 quotient。

---

# 84. False Fold

若不等價 states 被合併，可能隱藏：

- counterexample；
- branch；
- proof conflict；
- version distinction。

---

# 85. Bridge

新增合法 transport。

---

# 86. Project

降低 representation dimension / active structure。

---

# 87. Lift

加入額外 structure 或 dimension，使關係可見。

---

# 88. Compress

處理 representation redundancy。

---

# 89. Reparam

換座標／參數化，但不得改 claim truth。

---

# 90. ClassJump

轉換 problem class / representation regime。

但不得偷改 acceptance criteria。

---

# 91. Tunnel

使用受限 corridor / shortcut。

不是量子穿隧宣稱。

---

# 92. Representation Escape Gate

本文保留六道門：

$$
\boxed{
REG
=
(
G_{identity},
G_{equivalence},
G_{loss},
G_{cost},
G_{certificate},
G_{global}
).
}
$$

---

# 93. Identity Gate

原問題身份保持嗎？

---

# 94. Equivalence Gate

task acceptance 是否相容？

---

# 95. Loss Gate

丟掉什麼？

---

# 96. Cost Gate

建造、轉譯、回投、維護成本多少？

---

# 97. Certificate Gate

新結果能回到原任務被驗嗎？

---

# 98. Global Gate

局部 escape 能否安全回到 global structure？

---

# 99. Projection Change 不等 Qualification Upgrade

$$
\boxed{
\Pi_1\rightarrow\Pi_2
\not\Rightarrow
D^{judge}\rightarrow D^{verify}.
}
$$

---

# 100. Projection 可以提高 Judgeability

可能：

$$
x\notin D^{judge}_{\pi_1}
$$

但：

$$
x\in D^{judge}_{\pi_2}.
$$

---

# 101. 這是 Representation-Bound Judgeability

不是 Truth 改變。

---

# 102. Designed Perception 不等 Designed Truth

$$
\boxed{
DesignedPerception
\neq
DesignedTruth.
}
$$

---

# 103. AI-generated View 也必須受 Qualification Guard

新視圖不能把：

$$
SIM
$$

藏掉。

---

# 104. Observation-Method Autonomy

AI 決定：

$$
\mathcal O_{\mathrm{new}}.
$$

---

# 105. Projection-Method Autonomy

AI 決定：

$$
\Pi_{\mathrm{new}}.
$$

---

# 106. 兩者不同

$$
\boxed{
OMA
\neq
PMA.
}
$$

---

# 107. Computational Way of Seeing

本文定義：

$$
\boxed{
CWoS
=
(
\mathcal O,
\Pi,
c,
\lambda,
\mathcal I,
QCap,
Audit
).
}
$$

---

# 108. Way of Seeing 包含「取什麼」和「怎麼看」

不是只換視覺風格。

---

# 109. PMA Level 0

固定 projection。

---

# 110. PMA Level 1

從 library 選。

---

# 111. PMA Level 2

組合／重參數化。

---

# 112. PMA Level 3

自適應改 geometry / layout / scale / encoding。

---

# 113. PMA Level 4

生成新的 projection grammar。

---

# 114. PMA Level 5

提出新 carrier specification / representation regime。

---

# 115. Level 5 不等新物理已實現

它只是產生：

$$
CarrierRequirement.
$$

---

# 116. Paper 07 才處理物理實現

$$
CarrierRequirement
\rightarrow
PPOE.
$$

---

# 117. Projection Method Generation

給 AI：

- canonical observation；
- task；
- QCap；
- baseline carrier family。

要求它生成新 projection candidate。

---

# 118. Projection Candidate

$$
\Pi_{cand}.
$$

---

# 119. Candidate 必須先 Sandbox

$$
\Pi_{cand}
\rightarrow
ShadowProjection.
$$

---

# 120. Projection Tournament

比較：

$$
\Pi_1,\ldots,\Pi_n.
$$

---

# 121. Tournament Metrics

- task fidelity；
- error；
- cost；
- load；
- transfer；
- counterexample visibility；
- auditability；
- qualification preservation。

---

# 122. New Projection 不等 Better Projection

$$
\boxed{
Novelty
\neq
Utility.
}
$$

---

# 123. Projection Retention

通過多 task / multi-run 測試後：

$$
Admit(\Pi_{new})
$$

進 projection registry。

---

# 124. Projection Registry

至少保存：

$$
\boxed{
ProjRecord
=
(
Id,
Version,
Dom,
Cod,
Carrier,
TaskFamily,
Invariants,
DebtModel,
Certificates,
History
).
}
$$

---

# 125. Projection Versioning

$$
\Pi^{(v)}
\rightarrow
\Pi^{(v+1)}.
$$

必須保存 why changed。

---

# 126. Projection History

$$
H_t^{proj}
$$

記錄：

- selected projection；
- alternatives；
- reason；
- debt；
- observer response；
- failures；
- revision。

---

# 127. Projection Drift

同一 operator 在新 software / device / model 下可能行為變動。

---

# 128. Drift 必須觸發 Revalidation

$$
Drift(\Pi)
\Rightarrow
Revalidate(\Pi).
$$

---

# 129. Carrier Drift

XR calibration、screen characteristics、audio mapping、haptic response 也會變。

---

# 130. AI-Native Projection

AI 可以直接使用：

- sparse graph；
- event tensor；
- latent state；
- operator graph；
- constraint network。

---

# 131. AI-Native 不等 Human-Invisible

machine-native projection 仍可另外 humanize。

---

# 132. Human View 不應限制 AI View

$$
\boxed{
P_{AI}
\not\subseteq
P_H
}
$$

一般不成立。

---

# 133. Human View 也不一定低階

人類 visual/global pattern recognition 對某些 task 可能更強。

---

# 134. Carrier Selection 可以 Observer-Specific

$$
c^\ast_H
\neq
c^\ast_{AI}.
$$

---

# 135. Multi-Carrier Allocation

同一 observation 可拆：

$$
Y
\rightarrow
(
P_{visual},
P_{audio},
P_{haptic}
).
$$

---

# 136. 不必重複全部內容

各 carrier 可分工：

$$
I
=
I_v\cup I_a\cup I_h.
$$

---

# 137. Projection Allocation Problem

$$
c_i^\ast
=
\arg\max_c
Q(x_i,c,o,\tau).
$$

---

# 138. Projection Budget

$$
B_t^{proj}
=
(
B_{compute},
B_{latency},
B_{screen},
B_{bandwidth},
B_{cognitive},
B_{energy}
).
$$

---

# 139. High-Fidelity Projection 不一定值得

如果 task 已達 threshold，可停止細化。

---

# 140. Projection Stop

$$
E(\Pi)\le\varepsilon
$$

且 required invariants preserved 時：

$$
StopProjectionRefinement.
$$

---

# 141. 不足時輸出 Failure Certificate

不是硬畫一張圖。

---

# 142. Resolution Insufficient 是合法狀態

$$
\boxed{
\{
Pass,
Fail,
InsufficientResolution
\}.
}
$$

---

# 143. Decision Boundary

如果 projection error 大於 decision margin，禁止強制分類。

---

# 144. Projection Safety Margin

$$
E_\Pi
<
d(
y_\Pi,
\partial D
)
$$

才可穩定決策。

---

# 145. Projection Layer 與 Paper 05 Domain Layer

CPC 必須知道：

$$
QCap.
$$

---

# 146. Domain Debt 可觸發 Representation Escape

若：

$$
\Delta^{R\rightarrow J}
$$

主要來自 representation failure：

$$
Reframe.
$$

---

# 147. 但 Verification Debt 不應靠 Reframe 假裝消失

$$
\Delta^{J\rightarrow V}
$$

需要真正 evidence / proof。

---

# 148. Projection Layer 與 Paper 04 Observation Layer

Observation 選：

$$
Y.
$$

Projection 選：

$$
P.
$$

---

# 149. Observation Failure 要 Reobserve

Projection Failure 要 Reproject。

---

# 150. 兩種錯誤不能互相修錯層

$$
\boxed{
\text{Bad Observation}
\not\Rightarrow
\text{Fix by Pretty Projection}.
}
$$

---

# 151. Projection Layer 與 Paper 03 Computation Layer

高成本 projection compilation 本身也是 computation。

但其 semantic role 不等於 world dynamics computation。

---

# 152. Projection Compute 可以獨立調度

$$
\mathcal C^{proj}.
$$

---

# 153. Projection Layer 與 Paper 02 World Layer

view edit 不改 world：

$$
\boxed{
ViewEdit
\neq
CanonicalCommit.
}
$$

---

# 154. AI Proposal 也不等 Actuation Authority

$$
\boxed{
AIProposal
\neq
ActuationAuthority.
}
$$

---

# 155. Global Projection State

本文正式定義：

$$
\boxed{
\mathfrak P_t^G
=
\left\langle
\mathfrak P_t,
\mathfrak C_t^{carrier},
\mathfrak R_t^{repr},
\Lambda_t^{proj},
\mathfrak I_t^{task},
\mathfrak D_t^{proj},
\mathfrak H_t^{proj},
\mathfrak C_t^{cert},
\mathfrak T_t^{trans}
\right\rangle.
}
$$

---

# 156. WCO 目前五層

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}
\rightarrow
\mathfrak P_t^G.
}
$$

---

# 157. 但 Projection 並非單向末端

Projection failure 可以回饋：

- observer；
- domain；
- computation；
- world state request。

---

# 158. Projection Feedback Loop

$$
\boxed{
\mathfrak P
\rightarrow
\mathfrak D
\rightarrow
\mathfrak O
\rightarrow
\mathfrak C
\rightarrow
\mathfrak P'.
}
$$

---

# 159. Representation Runtime

本文將 B08 的概念正式寫成：

$$
\boxed{
RR_t
=
(
Y,
QCap,
B_o,
\mathfrak P,
\mathfrak C^{carrier},
Task,
Budget,
Risk,
Debt,
History
).
}
$$

---

# 160. Runtime 不再是 Fixed UI

而是：

$$
\boxed{
\text{dynamic compilation of task-relative perceptual objects}.
}
$$

---

# 161. MVP：同一 World 四種 View

沿用：

$$
W_A,W_B,W_C,W_N.
$$

對 risk observation：

$$
Y_{risk}.
$$

---

# 162. Baseline Projections

1. text table；
2. graph；
3. heatmap；
4. interactive canvas。

---

# 163. Fixed Projection Baseline

永遠使用 text table。

---

# 164. CPC Adaptive Projection

根據 task / QCap / observer 選 view。

---

# 165. Projection Escape Test

故意讓 text projection 難以發現 cycle。

graph projection 應降低：

$$
\Delta^{R\rightarrow J}.
$$

---

# 166. Verification Guard

即使 graph 幫助判定，也不得直接把：

$$
Judged
$$

改成：

$$
Verified.
$$

---

# 167. Round-Trip Test

graph：

$$
\rightarrow
text
\rightarrow
graph.
$$

量測 identity / invariant loss。

---

# 168. View-Edit Test

使用者在 canvas 拖動 node。

只產生：

$$
CandidateDelta.
$$

---

# 169. Projection Transition Test

task 改變時：

$$
P_1
\rightarrow
P_2.
$$

必須保留 PTC。

---

# 170. AI Projection Generation Test

不提供 graph 這個 baseline。

要求 AI 自己提出能揭露 cycle 的 representation。

---

# 171. Carrier Requirement Test

若 screen 無法有效傳達 time-varying alert，AI 可以提出：

$$
audio/haptic requirement.
$$

但不宣稱硬體已存在。

---

# 172. 實驗一：Fixed vs Adaptive Projection

控制 observation content 不變。

比較 task quality。

---

# 173. 實驗二：Representation Escape

比較：

$$
\pi_1
$$

與：

$$
\pi_2.
$$

測 judgeability gain。

---

# 174. 實驗三：Qualification Laundering

故意讓漂亮 view 隱藏 `Simulated` tag。

Guard 應阻止。

---

# 175. 實驗四：Projection Debt Prediction

測 debt vector 是否預測 human/AI error。

---

# 176. 實驗五：Minimal Sufficient Projection

比較 maximal view 與 task-minimal view。

---

# 177. 實驗六：PMA Methodology-Blind Test

不告訴 AI projection taxonomy。

測它是否產生新的 useful grammar。

---

# 178. 實驗七：Multi-Carrier

visual-only vs visual+audio/haptic。

---

# 179. 實驗八：Reproject vs Reobserve

world 不變只換 carrier。

確保不重新收集 evidence。

---

# 180. 實驗九：View Edit / Canonical Commit

測 UI 操作是否被正確 fence。

---

# 181. 實驗十：Projection Registry Evolution

加入新 projection version，測 history / rollback / revalidation。

---

# 182. 可反駁性

本文會被削弱，如果：

1. adaptive projection 在控制 observation content 後無穩定收益；
2. task-relative minimal projection 沒有成本優勢；
3. projection debt 無法預測 error；
4. representation escape 在代表性 tasks 中幾乎無效；
5. translation certificate 不改善 round-trip fidelity / audit；
6. CPC/QCap integration 沒有降低 qualification laundering；
7. AI-generated projection grammar 無法改善 baseline；
8. simpler fixed UI 在 global tasks 中完全等效。

---

# 183. 本文不主張什麼

本文不主張：

1. 所有問題都有高效 representation escape；
2. 難題都只是表示不好；
3. 投影就是壓縮；
4. 3D 一定比 2D 好；
5. high-dimensional view 一定比 text 好；
6. AI-native view 一定比 human view 好；
7. projection 可以提高 truth；
8. projection 可以取代 verification；
9. representation escape 可以偷改問題；
10. ClassJump 可以改 acceptance criteria；
11. round-trip fidelity 等於 canonical truth；
12. new carrier requirement 等於新硬體已實現；
13. AI 可以任意修改 canonical world 只因 view edit；
14. projection method autonomy 已在現有 AI 中被完整證實；
15. CPC 2.0 已是 production runtime；
16. Designed Perception 等於 Designed Truth；
17. 所有 projection transition 可逆；
18. 所有 carrier 都能無損互譯；
19. 投影族存在唯一最佳元素；
20. 本文取代 information visualization、HCI、scientific visualization、XR 或 representation-learning literature。

---

# 184. 核心非同一性

$$
\boxed{
Observation
\neq
Projection
\neq
Presentation.
}
$$

$$
\boxed{
Representation
\neq
Carrier
\neq
Observer.
}
$$

$$
\boxed{
Projection
\neq
Compression
\neq
Sampling
\neq
Surrogate.
}
$$

$$
\boxed{
Reprojection
\neq
Reobservation.
}
$$

$$
\boxed{
HumanView
\neq
AIView.
}
$$

$$
\boxed{
ProjectionChange
\not\Rightarrow
EpistemicUpgrade.
}
$$

$$
\boxed{
DesignedPerception
\neq
DesignedTruth.
}
$$

$$
\boxed{
ObservationMethodAutonomy
\neq
ProjectionMethodAutonomy.
}
$$

---

# 185. 核心母式一：CPC 2.0

$$
\boxed{
\mathsf{CPC}_2
:
(
Y,
QCap,
B_o,
\tau,
b,
\rho,
Cap
)
\rightarrow
(
\Pi^\ast,
c^\ast,
r^\ast,
P^\ast,
Audit
).
}
$$

---

# 186. 核心母式二：Projection Navigation Contract

$$
\boxed{
PNC(\phi)
=
\left\langle
Dom,
Cod,
TaskInv,
Identity,
Equivalence,
Loss,
Cost,
Risk,
Certificate,
QualificationEffect,
GlobalityEffect,
Rollback
\right\rangle.
}
$$

---

# 187. 核心母式三：Computational Way of Seeing

$$
\boxed{
CWoS
=
(
\mathcal O,
\Pi,
c,
\lambda,
\mathcal I,
QCap,
Audit
).
}
$$

---

# 188. 核心母式四：Global Projection State

$$
\boxed{
\mathfrak P_t^G
=
\left\langle
\mathfrak P_t,
\mathfrak C_t^{carrier},
\mathfrak R_t^{repr},
\Lambda_t^{proj},
\mathfrak I_t^{task},
\mathfrak D_t^{proj},
\mathfrak H_t^{proj},
\mathfrak C_t^{cert},
\mathfrak T_t^{trans}
\right\rangle.
}
$$

---

# 189. 結論：未來 AI 的「視野」不是一個固定介面，而是一個可編譯空間

如果一個 AI 只能：

$$
World
\rightarrow
Text,
$$

那它的 reasoning 可能很強，但「看世界」的 representation freedom 仍然很窄。

如果它只能：

$$
World
\rightarrow
Image,
$$

問題也一樣。

真正更一般的架構是：

$$
\boxed{
World
\rightarrow
Observation
\rightarrow
Qualification
\rightarrow
Projection Compilation
\rightarrow
Carrier.
}
$$

其中每一步都可相對 task、observer、budget 與 risk 動態調整。

所以 AI 不只要問：

> 我現在看到了什麼？

還要問：

> 我現在用什麼表示方式看這個東西？

> 這個表示是否隱藏了重要差異？

> 有沒有另一個 representation 能讓原本不可判的結構變得可判？

> 這次 representation change 保留了哪些 invariants？

> 它丟掉了什麼？

> 它只是讓我理解更容易，還是真的補上 verification debt？

> human 和 AI 是否應使用相同 carrier？

> 現有 carrier 是否根本不適合這個 information structure？

當 AI 能從既有 projection library 中選擇，這是 projection routing。

當 AI 能組合 projection，這是 adaptive representation。

當 AI 能在不知道理論名稱的情況下重新發明一個有用 projection，這才開始接近：

$$
\boxed{
\text{Projection-Method Autonomy}.
}
$$

因此未來類全域 AI 的 computational way of seeing 應該是：

$$
\boxed{
\text{what to observe}
+
\text{how to represent it}
+
\text{where to carry it}
+
\text{what must remain invariant}
+
\text{what debt remains}.
}
$$

本文最終命題是：

$$
\boxed{
\text{The future of AI cognition is not a single better view,}
}
$$

而是：

$$
\boxed{
\text{a runtime that can compile, compare, revise,
and sometimes invent better views when needed}.
}
$$

到此，WCO 的主要認知鏈已形成：

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}
\rightarrow
\mathfrak P_t^G.
}
$$

下一篇將把這個 projection 往物理世界真正壓下去：

# Paper 07
## 物理層：從 Machine Projection 到 Physical Projection

並正式承接 PPOE 的 sensor、transduction、material、field、receptor、calibration 與 safety。

---

# 190. 下一篇接口

Paper 07 將處理：

- machine-native projection；
- physical signal compiler；
- sensor transduction；
- actuator；
- optical / acoustic / haptic / electrical carriers；
- material transfer function；
- inverse physical projection；
- device calibration；
- observer calibration；
- material drift；
- physical projection debt；
- safety / authority gate；
- machine-to-human / human-to-machine projection；
- PPOS；
- cognitive material hypothesis。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K × Aletheia，《投影計算論：無限維索引的有限表示、收斂與失真證書》，2026。
2. Neo.K × Aletheia，《DEST-09｜表示逃逸與解空間導航 2.0》，2026。
3. Neo.K × Aletheia，《載體投影與內視系列 B08｜超越人類眼睛》，2026。
4. Neo.K × Aletheia，《PNCW Paper 00｜Projection-Native Computational Worlds》，2026。
5. Neo.K × Aletheia，《PNCW Paper 02｜Virtual Context Projection》，2026。
6. Neo.K × Aletheia，《PNCW Paper 04｜Images Are Not Merely Pictures》，2026。
7. Neo.K × Aletheia，《PNCW Paper 05｜Compute Globally, Materialize Selectively》，2026。
8. Neo.K × Aletheia，《WCO Paper 01–05》，2026。
9. Neo.K × Aletheia，《Global Observer Series C》，2026。
10. Neo.K × Aletheia，《PPOE Paper 01》，2026。

## External Mathematical / Visualization Interfaces

11. Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.
12. Ware, C. (2020). *Information Visualization: Perception for Design*, 4th ed. Morgan Kaufmann.
13. Card, S. K., Mackinlay, J. D., & Shneiderman, B. (1999). *Readings in Information Visualization*. Morgan Kaufmann.
14. Shneiderman, B. (1996). *The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations*. IEEE Symposium on Visual Languages.
15. Tufte, E. R. (1990). *Envisioning Information*. Graphics Press.
16. Weihrauch, K. (2000). *Computable Analysis*. Springer.
17. Schröder, M. (2020). *Admissibly Represented Spaces and Qcb-Spaces*. arXiv:2004.09450.

---

**Paper 06 狀態：COMPLETE v0.1**  
**下一篇：Paper 07 — 物理層：從 Machine Projection 到 Physical Projection**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
