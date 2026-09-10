# OAC Formalization & Falsification Taskpack v0.1

## From Research Grammar to Executable Multi-Scale World Calculus

**上位理論：**《一、全與中心：觀察者尺度下的動態單位化》  
**狀態：** Post-Series Formalization Program  
**日期：** 2026-09-09  
**目的：** 將 One–All–Center Calculus 從研究語法推進成可型別檢查、可構造反例、可實驗、可形式驗證的最小核心。

---

# 0. 研究階段切換

六篇寫作系列已經完成：

$$
Paper\ 00\rightarrow Paper\ 05.
$$

因此本階段不新增：

$$
Paper\ 06.
$$

而改為：

$$
\boxed{
Theory
\rightarrow
Formal Signature
\rightarrow
Counterexample
\rightarrow
Experiment
\rightarrow
Conformance
\rightarrow
Executable Calculus.
}
$$

目標不是繼續擴張概念。

而是開始問：

> 哪些命題真的能成立？

> 哪些只是需要補 qualifier？

> 哪些一般不成立，但存在額外條件後成立？

> 哪些可以被有限反例直接擊破？

---

# 1. OAC 的最小形式化對象

第一代 OAC 不直接嘗試形式化整個宇宙。

先建立最小 Sort System。

令：

$$
\mathsf{Sort}_{OAC}
$$

包含：

$$
\boxed{
\begin{aligned}
&World,\\
&Chart,\\
&Task,\\
&Observer,\\
&OntologicalOne,\\
&ComputationalUnit,\\
&Representation,\\
&Relation,\\
&Tension,\\
&Generator,\\
&History,\\
&DynamicFixedPoint,\\
&CenterFrame,\\
&CenterLocus,\\
&ScaleBridge,\\
&Certificate.
\end{aligned}
}
$$

---

# 2. 第一條形式化紀律：不同 Sort 不准裸等號

例如：

$$
u:\mathsf{ComputationalUnit},
$$

$$
O:\mathsf{OntologicalOne}.
$$

不能僅因為兩者都被稱為「一」就寫：

$$
u=O.
$$

除非存在：

$$
\boxed{
IdentityCertificate(u,O).
}
$$

同理：

$$
Representation
\neq
World,
$$

$$
CenterLocus
\neq
CenterCarrier,
$$

$$
LowerAll
\neq
HigherOne.
$$

---

# 3. Judgment 形式

採：

$$
\boxed{
\Gamma\vdash x:\tau
}
$$

表示：

> 在 typing context $\Gamma$ 下， $x$ 具有 type $\tau$。

例如：

$$
\Gamma
\vdash
\mathcal A_t
:
World.
$$

$$
\Gamma
\vdash
\chi
:
Chart[\mathcal A_t,Q].
$$

$$
\Gamma
\vdash
u
:
ComputationalUnit[\mathcal A_t,\chi].
$$

---

# 4. World Operator

定義：

$$
\boxed{
DynCl:
(O,R,T,G,H)
\rightarrow
World.
}
$$

具體：

$$
\mathcal A_t
=
DynCl
(
\mathcal O_t,
\mathcal R_t,
\mathcal T_t,
\mathcal G_t,
\mathcal H_{\le t}
).
$$

---

# 5. 第一個禁止式

不得將：

$$
\mathcal A_t
$$

替換成：

$$
\mathcal O_t.
$$

因此：

$$
\boxed{
ParticipantSet
\neq
World.
}
$$

---

# 6. Unitization Operator

定義：

$$
\boxed{
Unitize:
World\times Chart
\rightarrow
UnitFamily.
}
$$

$$
\mathcal U_\chi(W)
=
\{u_1,\ldots,u_n\}.
$$

---

# 7. Unit Count

$$
\boxed{
\nu_\chi(W)
=
|\mathcal U_\chi(W)|.
}
$$

---

# 8. Computational One

$$
\boxed{
One_\chi(X)
\iff
\nu_\chi(X)=1.
}
$$

但不能推：

$$
X=1.
$$

---

# 9. Support Operator

$$
\boxed{
Supp:
ComputationalUnit
\rightarrow
WorldSupport.
}
$$

例如：

$$
Supp(u)
=
\{O_1,O_2,O_3,R_{12},R_{23}\}.
$$

---

# 10. One–All Relation Bundle

定義：

$$
\boxed{
\Lambda_i(\mathcal A)
=
(
Res_i,
Tr_i,
\pi_i,
Part_i
).
}
$$

其中：

$$
Res_i(\mathcal A)
$$

表示 local restriction。

$$
Tr_i(\mathcal A)
$$

表示 generative / historical trace。

$$
\pi_i(\mathcal A)
$$

表示 representation。

$$
Part_i
$$

表示 participation。

---

# 11. Participation Judgment

$$
\boxed{
\Gamma
\vdash
O_i
\triangleleft_p
\mathcal A.
}
$$

不推出：

$$
O_i=\mathcal A.
$$

---

# 12. All-in-One Judgment

$$
\boxed{
\mathcal A
\rightsquigarrow_i
O_i
}
$$

成立條件：

$$
Res_i(\mathcal A)\neq\varnothing
$$

且：

$$
Tr_i(\mathcal A)\neq\varnothing.
$$

---

# 13. Representation Operator

$$
\boxed{
Project:
Observer\times Chart\times World
\rightarrow
Representation.
}
$$

$$
M_{o,\chi}
=
\pi_{o,\chi}(W).
$$

---

# 14. Projection Hard Rule

$$
\boxed{
\pi_{o,\chi}(W)
\neq
W
}
$$

除非另有特殊 exact-equivalence certificate。

---

# 15. Tension Sort

第一代不需要假設 complete True-ETN graph。

定義：

$$
T_\alpha(t)
:
Tension.
$$

---

# 16. Tension Family

$$
\boxed{
\mathcal T_t
=
\{T_\alpha(t)\}_{\alpha\in E_t}.
}
$$

---

# 17. Difference 不足以生成 Tension

$$
x\neq y
$$

不推出：

$$
T(x,y).
$$

需要：

$$
Relation(x,y)
$$

與相應 tension condition。

---

# 18. Evolution Operator

$$
\boxed{
Evolve:
World_t
\rightarrow
World_{t+\Delta t}.
}
$$

較完整：

$$
\mathcal A_{t+\Delta t}
=
\Phi
(
\mathcal A_t,
\mathcal G_t,
\mathcal T_t,
\mathcal H_{\le t}
).
$$

---

# 19. Dynamic Stability

定義：

$$
\boxed{
Stable_{\chi,\tau,\varepsilon}(X)
}
$$

若：

$$
\hat U_{\Delta t}(X)
\approx_{\chi,\varepsilon}
X
$$

在指定 window 中成立。

---

# 20. Dynamic Fixed Point

$$
\boxed{
x^*
:
DynamicFixedPoint[\chi,\tau,\varepsilon].
}
$$

---

# 21. Center Frame

定義：

$$
\boxed{
\zeta
=
(
W,
\chi,
Q,
\kappa,
\mathcal Y,
\preceq,
\tau
).
}
$$

---

# 22. Center Operator

$$
\boxed{
Center:
World\times CenterFrame
\rightarrow
CenterLocus.
}
$$

$$
\mathcal C_\zeta(W)
=
Opt_{y\in\mathcal Y}
\kappa_\zeta(y).
$$

---

# 23. Center Locus Types

CenterLocus 可以是：

$$
Point,
Node,
Set,
Region,
Relation,
Field,
InvariantClass,
Empty.
$$

所以：

$$
\boxed{
CenterLocus
\neq
necessarily\ Node.
}
$$

---

# 24. Scale Bridge

定義：

$$
\boxed{
K_{a\rightarrow b}
:
World/Structure_{\chi_a}
\rightarrow
ComputationalUnit_{\chi_b}.
}
$$

---

# 25. Expansion

$$
\boxed{
E_{b\rightarrow a}
:
ComputationalUnit_{\chi_b}
\rightsquigarrow
Structure_{\chi_a}.
}
$$

---

# 26. 不預設可逆

一般：

$$
\boxed{
E\circ K
\neq
Id.
}
$$

---

# 27. Bridge Certificate

每個 $K$ 至少保存：

```text id="oac-bridge-cert"
ScaleBridgeCertificate:
  source_world
  source_chart
  target_chart
  source_support
  target_unit
  preserved_semantics
  preserved_invariants
  projection_loss
  hidden_cost
  expansion_ref
  provenance
  invalidation_rules
```

---

# 28. Validation Operator

$$
\boxed{
Validate:
Claim/Bridge/Chart
\rightarrow
\{PASS,FAIL,UNKNOWN\}.
}
$$

---

# 29. UNKNOWN 不等於 PASS

$$
\boxed{
UNKNOWN
\neq
TRUE.
}
$$

---

# 30. 第一代 OAC Formal Core

可以壓縮成：

$$
\boxed{
\mathfrak O
=
(
S,
F,
J,
I
)
}
$$

其中：

- $S$：sorts；
- $F$：operators；
- $J$：typing judgments；
- $I$：invariants。

---

# 31. OAC-F01｜Typed-One Invariant

$$
\boxed{
1_{\mathrm{num}}
\neq
O_i
\neq
u_\chi
\neq
M_i.
}
$$

---

# 32. OAC-F02｜All Non-Additivity

$$
\boxed{
DynCl(O,R,T,G,H)
\neq
O.
}
$$

---

# 33. OAC-F03｜Projection Non-Identity

$$
\boxed{
\pi(W)
\neq
W.
}
$$

---

# 34. OAC-F04｜Participation Non-Identity

$$
\boxed{
O_i\triangleleft_pW
\not\Rightarrow
O_i=W.
}
$$

---

# 35. OAC-F05｜Unitization Non-Identity

$$
\boxed{
K(X)=u
\not\Rightarrow
X=u.
}
$$

---

# 36. OAC-F06｜Center Qualification

任何：

$$
Center(X)
$$

若沒有 $\zeta$，

只能標：

$$
ILL\_TYPED
$$

或：

$$
UNDERQUALIFIED.
$$

---

# 37. OAC-F07｜Center Non-Authority

$$
\boxed{
Centrality
\not\Rightarrow
Authority.
}
$$

---

# 38. OAC-F08｜Dynamic Fixed Point Non-Center

$$
\boxed{
Stable(X)
\not\Rightarrow
Center(X).
}
$$

---

# 39. OAC-F09｜Hidden Complexity Preservation

若：

$$
K(\Gamma)=v,
$$

則：

$$
VisibleHop(v)=1
$$

不能推出：

$$
UnderlyingCost(\Gamma)=0.
$$

---

# 40. OAC-F10｜Cross-Scale Noncommutation by Default

一般不預設：

$$
\boxed{
K\circ F
=
F'\circ K.
}
$$

需要 certificate。

---

# 41. OAC-F11｜No Automatic Authority Lift

$$
Authority(O_1),
Authority(O_2)
$$

不推出：

$$
Authority(K(O_1,O_2))
=
Authority(O_1)\cup Authority(O_2).
$$

---

# 42. OAC-F12｜Relativity Non-Arbitrariness

若：

$$
\chi_1\neq\chi_2
$$

導致：

$$
Result_{\chi_1}\neq Result_{\chi_2},
$$

不代表任一結果都可隨意指定。

兩個 chart 都需要：

$$
Adm(\chi)=PASS.
$$

---

# 43. 第一批應證／應反證命題

現在真正開始做 falsifiable work。

---

# 44. Target T1｜Unitization Multiplicity

存在某 $X$ 與兩個 admissible charts：

$$
\chi_f,
\chi_c
$$

使：

$$
\nu_{\chi_f}(X)>1,
$$

而：

$$
\nu_{\chi_c}(X)=1.
$$

---

# 45. 最小反例

route：

$$
A\rightarrow B\rightarrow C\rightarrow D.
$$

fine chart：

$$
4\ nodes.
$$

compiled-route chart：

$$
1\ route-unit.
$$

---

# 46. T1 的價值

直接反駁：

> computational One 是 scale-free primitive。

---

# 47. Target T2｜Same Participants, Different Whole

構造：

$$
O=\{a,b,c,d\}.
$$

World 1：

$$
a-b-c-d.
$$

World 2：

$$
a
\leftrightarrow
\{b,c,d\}.
$$

---

# 48. 則：

$$
O_1=O_2
$$

但：

$$
R_1\neq R_2.
$$

因此：

$$
\boxed{
W_1\neq W_2.
}
$$

---

# 49. T2 的價值

有限模型直接支持：

$$
All\neq ParticipantSet.
$$

---

# 50. Target T3｜Center Ranking Reversal

固定：

$$
W.
$$

定義：

$$
\zeta_1
$$

使用 graph-distance centrality。

定義：

$$
\zeta_2
$$

使用 flow / causal centrality。

尋找：

$$
c_A>_{\zeta_1}c_B,
$$

但：

$$
c_B>_{\zeta_2}c_A.
$$

---

# 51. T3 的目的

反駁：

> center ranking 是 criterion-free。

---

# 52. Target T4｜Center Non-Lifting

這是第一個正式主攻。

目標找：

$$
\boxed{
K
(
Center_{\zeta_k}(W)
)
\neq
Center_{\zeta_{k+1}}
(
K(W)
).
}
$$

---

# 53. 建議世界

兩個 modules：

$$
M_A,
M_B.
$$

各自有 local hub。

但兩個 modules 之間只有一個 bridge corridor。

---

# 54. Local Chart

在：

$$
M_A
$$

中：

$$
Center=M_A^{hub}.
$$

在：

$$
M_B
$$

中：

$$
Center=M_B^{hub}.
$$

---

# 55. Global Chart

跨兩 module 的 global reachability / articulation criterion 下，

center 可能變成：

$$
Bridge.
$$

---

# 56. 結果

higher center 並不是：

$$
K(M_A^{hub})
$$

也不是：

$$
K(M_B^{hub}).
$$

而是 emergent bridge relation。

---

# 57. 這直接驗證

$$
\boxed{
CenterOfCenters
\neq
MostCentralChild.
}
$$

---

# 58. Target T5｜Stable Parts, Unstable Whole

尋找：

$$
Stable(A),
$$

$$
Stable(B),
$$

但：

$$
\neg Stable(DynCl(A,B,T)).
$$

---

# 59. 最小模型

兩個 individually stable finite-state machines。

加入 feedback：

$$
A\leftrightarrow B.
$$

造成：

- oscillation；
- divergence；
- deadlock；

任一即可。

---

# 60. T5 的目的

證明：

$$
\boxed{
StableParts
\not\Rightarrow
StableWhole.
}
$$

---

# 61. Target T6｜Route-to-Point Hidden Cost

原 route：

$$
A\rightarrow B\rightarrow C\rightarrow D.
$$

compile：

$$
K(\Gamma)=v.
$$

---

# 62. Macro Chart

$$
Hop(v)=1.
$$

---

# 63. Ledger

仍記：

$$
C_{execute},
C_{validate},
C_{maintain},
C_{expand}.
$$

---

# 64. 若任何系統宣稱：

$$
Hop=1
\Rightarrow
TotalCost=1,
$$

Taskpack 必須判：

$$
FAIL.
$$

---

# 65. Target T7｜Cross-Scale Commutation

研究：

$$
K\circ F
\stackrel{?}{\simeq}
F'\circ K.
$$

---

# 66. 一般先找反例

之後才研究 sufficient conditions。

---

# 67. Commutation Candidate Conditions

可能包括：

1. $K$ preserving relevant invariants；
2. hidden state irrelevant to $F$ ；
3. $F$ respects equivalence classes induced by $K$ ；
4. no emergent cross-unit interaction；
5. projection loss bounded below tolerance。

---

# 68. 如果成立

才發：

$$
\boxed{
CommutationCertificate.
}
$$

---

# 69. 第一批 Toy Worlds

不碰大型 AI 系統前，先用五個小世界。

---

# 70. TW-01｜Center Reversal Graph

目的：

$$
Center_{\zeta_1}
\neq
Center_{\zeta_2}.
$$

---

# 71. TW-02｜Two-Module Bridge World

目的：

$$
LocalCenter
\neq
GlobalCenter.
$$

並測：

$$
CenterNoncommutation.
$$

---

# 72. TW-03｜Compiled Route World

目的：

$$
Route
\rightarrow
Point
$$

與 hidden-cost ledger。

---

# 73. TW-04｜Dynamic Tension World

兩個／三個 interacting finite-state components。

目的：

- dynamic fixed point；
- oscillatory state；
- stable-parts/unstable-whole。

---

# 74. TW-05｜Mini Cloud AI World

建立：

$$
Resident_A,
Resident_B,
IdentityDomain,
MemoryDomain,
RuntimeDomain,
SharedProject.
$$

---

# 75. 對 TW-05 分別算

$$
C_{physical},
$$

$$
C_{control},
$$

$$
C_{governance},
$$

$$
C_{invariant}.
$$

---

# 76. 預期不是同一個 center

這是 Cloud AI Center 的第一個可執行 OAC stress test。

---

# 77. Falsification Gate G1｜Arbitrary Unitization

若任意 partition 都可以宣稱 admissible，

OAC 失敗。

---

# 78. 所以至少要求：

$$
BoundaryValidity,
TaskAdequacy,
InvariantPreservation.
$$

---

# 79. G2｜Projection Collapse

若：

$$
\pi(W)=W
$$

被當預設，

失敗。

---

# 80. G3｜Unqualified Center

若系統接受：

> X 是唯一中心。

但沒有：

$$
\zeta,
$$

應拒絕。

---

# 81. G4｜Free Relabeling

只把：

```text id="oac-bad-relabel"
A -> B -> C -> D
```

命名為：

```text id="oac-bad-relabel-2"
ONE_STEP
```

卻沒有真正 execution abstraction，

不得宣稱 computational improvement。

---

# 82. G5｜Hidden-Cost Erasure

若 compiled macro 不保留 hidden-cost ledger，

失敗。

---

# 83. G6｜Automatic Authority Aggregation

如果 group unitization 自動取得全部 member authority，

失敗。

---

# 84. G7｜Uncertified Commutation

若 implementation 默認：

$$
K(F(X))
=
F'(K(X))
$$

對所有 operator 都成立，

失敗。

---

# 85. G8｜Stable-Part Fallacy

若：

$$
\forall i Stable(O_i)
$$

直接推出：

$$
Stable(W),
$$

失敗。

---

# 86. G9｜Center-by-Connectivity Fallacy

若最高 degree 自動成：

- governance center；
- epistemic center；
- causal center；

失敗。

---

# 87. G10｜Observer Absolutization

若某 representation backend：

- graph；
- vector；
- tensor；
- symbolic tree；

被宣稱為 world 的唯一 ontology，

OAC 應標：

$$
RepresentationCenterBias.
$$

---

# 88. 第一代 Schema

```text id="oac-world-schema"
WorldState:
  world_id
  time
  participants
  relations
  tensions
  generators
  history_ref
  boundary
  provenance
```

---

# 89. Chart Schema

```text id="oac-chart-schema"
Chart:
  chart_id
  observer
  world_ref
  scale
  boundary_rule
  relation_domain
  metric
  task
  time_horizon
  tolerance
  representation
  admissibility_state
```

---

# 90. Unit Schema

```text id="oac-unit-schema"
ComputationalUnit:
  unit_id
  chart_ref
  world_ref
  support_ref
  interface
  hidden_cost_ref
  expansion_ref
  provenance
```

---

# 91. Center Schema

```text id="oac-center-schema"
CenterFrame:
  frame_id
  world_ref
  chart_ref
  criterion
  candidate_domain
  selection_rule
  task
  time_horizon

CenterResult:
  frame_ref
  locus
  locus_type
  uniqueness_state
  carrier
  role
  stability
  evidence
```

---

# 92. Scale Bridge Schema

```text id="oac-scale-schema"
ScaleBridge:
  bridge_id
  source_chart
  target_chart
  source_ref
  target_unit
  transition_type
  invariant_map
  semantic_map
  loss_bound
  cost_ledger
  expansion_ref
  validation
  provenance
```

---

# 93. 第一代實作分層

## F0｜Schema Layer

只做：

- types；
- validators；
- JSON/YAML fixtures。

不做 AI。

---

# 94. F1｜Finite Model Engine

使用有限 graph / FSM world。

功能：

- Unitize；
- ComputeCenter；
- Project；
- Encapsulate；
- Expand。

---

# 95. F2｜Counterexample Harness

每個 claim 格式：

```text id="oac-counterexample"
Claim
Domain
Assumptions
Candidate Witness
Counterexample
Surviving Restricted Claim
```

---

# 96. 這很重要

反例不是只有：

> 錯。

而是要留下：

$$
\boxed{
\text{what weaker statement still survives?}
}
$$

---

# 97. F3｜Property-Based Tests

例如：

```text id="oac-property-tests"
assert Unitization != Identity
assert CenterWithoutFrame is invalid
assert ProjectionDoesNotMutateWorld
assert GroupUnitDoesNotMintAuthority
assert HiddenCostSurvivesCrystallization
```

---

# 98. F4｜Formal Proof Fragment

不需要一次形式化整個 OAC。

第一輪只挑：

- typing disjointness；
- simple non-identity lemmas；
- finite center reversal；
- noncommutation counterexample。

Lean / Coq 皆可。

---

# 99. F5｜UNPNP-II Integration

直接接：

$$
Chart,
Unitize,
ScaleBridge,
CostLedger.
$$

---

# 100. F6｜WCO / Global Computation Integration

接：

$$
World,
Observer,
Projection,
WorldFamily,
CrossWorldBridge.
$$

---

# 101. F7｜Cloud AI Runtime Projection

最後才接真實 runtime。

目的不是證明 OAC。

而是：

> stress-test OAC 是否真的能描述複雜 distributed cognitive system。

---

# 102. OAC 與 True ETN 的形式化邊界

第一代實驗不要先攻：

$$
|I|=\infty.
$$

---

# 103. 先做

$$
|I|<\infty.
$$

的 tension network。

---

# 104. 若 finite core 都站不住

無限維版本沒有先上場的必要。

---

# 105. 所以研究順序

$$
\boxed{
Finite
\rightarrow
Parameterized
\rightarrow
Large
\rightarrow
Infinite.
}
$$

---

# 106. OAC 與 One–All 的形式化邊界

先驗：

$$
Res\neq Tr\neq\pi\neq Participation.
$$

---

# 107. 不急著證明 Ultimate 的最終 ontology。

---

# 108. OAC 與 UNPNP 的形式化邊界

先證明：

> chart 改變會改 step semantics。

---

# 109. 再證明：

> 哪些 crystallization 真的降低 effective cost。

---

# 110. 不把：

$$
macro\ hop
$$

偷換成：

$$
machine\ step.
$$

---

# 111. OAC 與 AI Center 的形式化邊界

先用 toy DCR。

---

# 112. 不需要一開始接：

- 真實身份；
- 真實 authority；
- production systems。

---

# 113. 第一代只驗：

$$
Polycentricity,
CenterTyping,
ScaleTransition.
$$

---

# 114. Experiment 01

下一輪正式執行：

# OAC Experiment 01
## Center Noncommutation and Center Reversal on a Finite Two-Module Bridge World

---

# 115. E01 要回答三件事

第一：

$$
\boxed{
Center_{\zeta_1}(W)
\neq
Center_{\zeta_2}(W)
}
$$

是否可用最小有限圖直接構造。

---

# 116. 第二

$$
\boxed{
LocalCenters
\not\Rightarrow
GlobalCenter.
}
$$

---

# 117. 第三

$$
\boxed{
K(C_k)
\neq
C_{k+1}(K(W))
}
$$

是否能得到明確 witness。

---

# 118. E01 必須產生

- exact finite graph；
- adjacency / weights；
- local charts；
- global chart；
- center criteria；
- raw scores；
- $K$ map；
- counterexample certificate；
- surviving restricted theorem。

---

# 119. Counterexample Certificate

```text id="oac-ce-cert"
CounterexampleCertificate:
  claim
  assumptions
  world
  charts
  operators
  witness
  observed_result
  contradicted_conclusion
  surviving_claim
  reproducibility
```

---

# 120. 最重要的是 Surviving Claim

例如若：

$$
K(C_k)
=
C_{k+1}
$$

一般為假，

我們不停止。

---

# 121. 下一步問：

> 什麼條件下為真？

---

# 122. 候選 sufficient condition：

$$
\boxed{
K\circ Center_{\zeta_k}
=
Center_{\zeta_{k+1}}\circ K
}
$$

若：

1. candidate spaces correspond；
2. centrality function preserved；
3. no emergent relation appears；
4. relevant distances preserved；
5. optimization order preserved。

---

# 123. 如果這些條件成立

就可能得到：

$$
CommutationTheorem.
$$

---

# 124. 所以 OAC 後系列不是「證明原理論」

而是：

$$
\boxed{
Claim
\rightarrow
Counterexample
\rightarrow
RestrictedClaim
\rightarrow
Condition
\rightarrow
Theorem.
}
$$

---

# 125. 這才是真正形式化研究開始的地方

概念越漂亮，

越需要主動問：

> 哪裡會壞？

---

# 126. Taskpack Close Condition

這個後系列 formalization program 的第一階段完成條件：

$$
\boxed{
\begin{aligned}
&\text{typed core schema exists},\\
&\text{claims can be machine-checked for qualification},\\
&\text{finite model engine exists},\\
&\text{counterexample suite exists},\\
&\text{scale bridges have certificates},\\
&\text{center claims preserve frames},\\
&\text{hidden cost cannot silently disappear}.
\end{aligned}
}
$$

---

# 結論

六篇系列完成的是：

$$
\boxed{
\text{統一語法}.
}
$$

現在這個 Taskpack 開始處理：

$$
\boxed{
\text{語法到底能不能站得住。}
}
$$

所以研究重心正式從：

> 一、全、中心可以怎麼理解？

轉變成：

> 在一個明確有限世界中，如果我改變 chart、scale、metric、center criterion 或 encapsulation operator，這些命題實際會發生什麼？

這一轉非常重要。

因為從這裡開始：

$$
\boxed{
\text{「有道理」不再足夠。}
}
$$

我們要有：

$$
\boxed{
Witness,
Counterexample,
Certificate,
Reproduction.
}
$$

因此後系列的第一條工作原則可以定成：

$$
\boxed{
\text{任何跨尺度的一、全、中心命題，只要不能指出它的 type、chart、bridge 與驗證條件，就暫時不算正式 OAC 命題。}
}
$$

而下一步已經非常明確：

$$
\boxed{
\text{Experiment 01：先親手讓 Center Noncommutation 發生。}
}
$$

如果連最小有限圖都能清楚看見：

$$
K(C_k)
\neq
C_{k+1}(K(W)),
$$

那我們就取得 OAC 第一個真正意義上的**反例型形式化成果**，並能開始反向尋找它何時才可交換。