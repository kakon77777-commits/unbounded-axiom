# UNPNP-II Phase B — Paper 01
## Formal Core and Reference Runtime
### 從 World-Relative Optimization 到可執行多尺度計算 Runtime

**系列：** UNPNP-II / Multi-Scale Computational Geometry — Phase B  
**篇次：** Phase B Paper 01  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-09  
**文件性質：** Formal Core／Reference Runtime／Implementation Bridge／Experimental Baseline  
**前置：** UNPNP-II Paper 01–08、UNPNP-I、MWT、GCM、24／72 Computational Configuration Space  
**狀態：** Canonical Draft

---

## 摘要

UNPNP-II v0.1 已完成八篇理論定義，將「最短路徑」從固定 graph 上的單一最短路問題，擴張成一個多尺度、異質、可結晶、可重開的 World-Relative Optimization 問題。

其最終形式為：

$$
\boxed{
(
\mathcal A_t^\*,
\mathcal F_t^\*,
\Gamma_t^\*,
\mathcal R_t^\*,
\mathcal K_t^\*
)
=
\arg\min_{\mathcal X\in\mathfrak F_t(\Xi_t)}
J_t(\mathcal X)
}
$$

其中：

- $\mathcal A_t$：computational atlas；
- $\mathcal F_t$：active refinement frontier；
- $\Gamma_t$：configuration field；
- $\mathcal R_t$：route；
- $\mathcal K_t$：crystal population；
- $\Xi_t$：task / world / observer / budget / governance / history context。

理論完成後，下一個必要問題不再是：

> 還能再增加什麼概念？

而是：

> **這些對象如何被放進一個最小、可執行、可測量、可重播、可否證的 Reference Runtime？**

本文提出 **UNPNP-II Reference Runtime，URR-v0.1**。

URR 的目的不是一次實作完整 World-Relative Optimizer，而是建立最小共同底座，使後續不同實驗都能使用同一組：

- state objects；
- typed transitions；
- receipts；
- cost vectors；
- refinement / coarsening；
- configuration routing；
- route selection；
- path compilation；
- crystallization；
- invalidation；
- reopen；
- replay；
- frozen-model experiment。

本文將 Reference Runtime 定義為：

$$
\boxed{
\mathfrak R_t
=
\left\langle
W_t,
A_t,
F_t,
C_t,
Z_t,
P_t,
K_t,
H_t,
B_t,
G_t,
L_t
\right\rangle
}
$$

其中：

- $W_t$：executable world presentation；
- $A_t$：atlas registry；
- $F_t$：active frontier；
- $C_t$：configuration field；
- $Z_t$：safe charted state space；
- $P_t$：route / path registry；
- $K_t$：crystal store；
- $H_t$：history / provenance；
- $B_t$：budget state；
- $G_t$：governance state；
- $L_t$：cost / validation ledger。

Reference Runtime 的核心迴圈為：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Reveal}
\rightarrow
\text{Select Chart}
\rightarrow
\text{Refine / Coarsen}
\rightarrow
\text{Configure}
\rightarrow
\text{Route}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Compile}
\rightarrow
\text{Crystallize / Reopen}
\rightarrow
\text{Commit}.
}
$$

但實作上不要求每一輪都經過全部階段。每一步都可：

- no-op；
- reuse；
- fallback；
- deny。

本文將整個 Runtime 收斂為 **16 條核心 invariants（URR-1 至 URR-16）**，並提出最小資料結構、演算法接口、promotion gate、replay contract、frozen-model benchmark 與 reference experiment。

---

# 1. Phase B 的目標

Phase A 已回答：

> 這個理論是什麼？

Phase B 要回答：

> 它最低限度要怎麼跑？

---

# 2. Reference Runtime 不等於產品 Runtime

URR-v0.1 不是：

- production scheduler；
- full compiler；
- AGI runtime；
- general optimizer。

它只是：

$$
\boxed{
\text{reference semantics + executable experimental skeleton}.
}
$$

---

# 3. Reference Runtime 的第一原則

$$
\boxed{
\text{Theory Object}
\neq
\text{Runtime Object}.
}
$$

例如：

$$
\mathbf W
$$

是 MWT World primitive。

但 Runtime 實作中只能保存：

$$
W_t.
$$

---

# 4. World Primitive 不進 Database Row

因此：

$$
\boxed{
\mathbf W
\neq
W_t.
}
$$

---

# 5. Executable World Presentation

定義：

$$
\boxed{
W_t
=
\langle
id,
revision,
state,
domains,
schema,
epoch
\rangle.
}
$$

---

# 6. World Revision

任何會改變 route validity 的 world change 必須更新：

```text
world_revision
```

---

# 7. Domain Registry

$$
D_t
=
\{D_1,\ldots,D_n\}.
$$

每個 domain 有：

```text
domain_id
parent_domains
child_domains
overlaps
state_ref
permissions
active_scale
active_config
```

---

# 8. Domain 不要求 Tree

可以：

- DAG；
- cover；
- overlap graph；
- hypergraph。

---

# 9. Atlas Registry

定義：

$$
\boxed{
A_t
=
\{\chi_1,\ldots,\chi_m\}.
}
$$

---

# 10. Computational Chart Record

```text
Chart
- chart_id
- world_revision
- domain_scope
- granularity
- scale
- geometry
- computational_form
- transition_law
- temporal_frame
- observer_projection
- fidelity
- validator
- version
```

---

# 11. Chart Is a Runtime Projection

$$
\boxed{
\chi
\neq
\mathbf W.
}
$$

---

# 12. Active Frontier

$$
\boxed{
F_t
=
\{f_1,\ldots,f_k\}.
}
$$

---

# 13. Frontier Record

```text
FrontierEntry
- domain_id
- active_scale
- materialized
- reason
- utility
- refinement_debt
- coarsening_debt
- ttl
```

---

# 14. Finite Frontier Invariant

任一時刻：

$$
\boxed{
|F_t|
<
\infty.
}
$$

---

# 15. Configuration Field

$$
\boxed{
C_t:
D_i
\mapsto
c_i.
}
$$

---

# 16. Configuration Record

```text
Configuration
- config_id
- domain_id
- P24_form
- transition_law
- geometry
- scale
- temporal_frame
- observer
- resource_profile
- guard
- version
```

---

# 17. 24／72 As Local Semantics

第一版可支援：

$$
P5^F,\;
P11^F,\;
P17^F,\;
P23^F
$$

作 MVP subset。

---

# 18. Why Only Four First

因為它們已足以測：

- sequential；
- jump；
- parallel；
- retrieval。

---

# 19. Reference Geometry Vocabulary

v0.1：

```text
POINT
LINE
JUMP_LINE
SURFACE
CLUSTER
FIELD
RECURSIVE
UNKNOWN
```

---

# 20. UNKNOWN 是一級狀態

不能因 Runtime 不知道就預設 LINE。

---

# 21. Scale Vocabulary

第一版工程可只用：

```text
COARSE
MESO
FINE
```

---

# 22. 理論仍保留無界 Scale Poset

Runtime 三級只是 MVP projection。

---

# 23. Temporal Frame Record

```text
TemporalFrame
- frame_id
- clock_kind
- causal_model
- event_time_source
- wall_time_source
- logical_clock
- ordering_constraints
```

---

# 24. Clock Kind

v0.1：

```text
WALL
EVENT
LOGICAL
CAUSAL
HYBRID
```

---

# 25. Charted State

$$
\boxed{
z
=
(s,\chi,c).
}
$$

工程 record：

```text
ChartedState
- state_id
- world_revision
- domain_id
- state_ref
- chart_id
- config_id
- observer_id
- governance_snapshot
```

---

# 26. Safe State Space

Runtime 不 materialize 全：

$$
\mathcal Z.
$$

只維持：

$$
\boxed{
\widehat{\mathcal Z}_{a,t}^{safe}.
}
$$

---

# 27. Reachability Gate

任何 candidate transition 先判定：

```text
reachable?
authorized?
guard-valid?
resource-feasible?
risk-valid?
```

---

# 28. Route Registry

$$
\boxed{
P_t
=
\{
\mathcal R_1,\ldots,\mathcal R_n
\}.
}
$$

---

# 29. Route Segment Record

```text
RouteSegment
- segment_id
- source_state
- target_state
- source_chart
- target_chart
- source_config
- target_config
- transition_type
- guard
- cost_estimate
- validator
- authorization
- provenance
```

---

# 30. Segment Transition Type

```text
STATE
CONFIG
SCALE
GEOMETRY
OBSERVER
JOINT
```

---

# 31. STATE Transition

state 變，config 不變。

---

# 32. CONFIG Transition

config 變，state 可不變。

---

# 33. SCALE Transition

scale 變。

---

# 34. GEOMETRY Transition

dependency geometry 變。

---

# 35. OBSERVER Transition

projection 變。

---

# 36. JOINT Transition

同時改多軸。

---

# 37. JOINT 是高風險 Transition

需要 stronger validator。

---

# 38. Route Record

```text
Route
- route_id
- task_id
- source
- goal
- segments[]
- expected_cost_vector
- realized_cost_vector
- validation_state
- authority_scope
- epoch
- lifecycle
```

---

# 39. Cost Vector

第一版：

$$
\boxed{
\mathbf C
=
(
H,
W,
D_C,
T,
M,
V,
R,
L,
S
).
}
$$

---

# 40. Meaning

- $H$：hop；
- $W$：work；
- $D_C$：causal depth；
- $T$：wall time；
- $M$：memory / materialization；
- $V$：verification cost；
- $R$：risk；
- $L$：projection / translation loss；
- $S$：switch cost。

---

# 41. Route Cost Must Be Measured

預測：

```text
expected_cost_vector
```

執行後：

```text
realized_cost_vector
```

---

# 42. Cost Prediction Error

$$
\boxed{
E_C
=
\|\widehat{\mathbf C}-\mathbf C\|.
}
$$

---

# 43. Runtime 可學 Cost Profile

Frozen-model 也可以更新 external profile。

---

# 44. Crystal Store

$$
\boxed{
K_t
=
\{\kappa_1,\ldots,\kappa_m\}.
}
$$

---

# 45. Crystal Record

```text
Crystal
- crystal_id
- source_route
- source_world_revision
- valid_domain
- guard
- semantic_contract
- configuration_signature
- geometry_signature
- scale_signature
- temporal_causal_contract
- resource_envelope
- verification_maturity
- provenance
- reopen_pointer
- lifecycle_state
- utility
- last_validated_at
```

---

# 46. Crystal Lifecycle

```text
CANDIDATE
COLD
WARM
HOT
STALE
RETIRED
```

---

# 47. CANDIDATE

compiled 但未成熟。

---

# 48. COLD

初步驗證。

---

# 49. WARM

反覆成功。

---

# 50. HOT

fast primitive。

---

# 51. STALE

guard / dependency / policy 漂移。

---

# 52. RETIRED

不再使用。

---

# 53. Reopen Pointer

每個 earned primitive 預設必須：

```text
reopen_pointer != null
```

除非明示 irreversible。

---

# 54. Irreversible Crystal

需要：

```text
reopenability = DEGRADED
loss_declared = true
```

---

# 55. History Ledger

$$
\boxed{
H_t
}
$$

至少記：

- observation；
- reveal；
- chart switch；
- refinement；
- configuration switch；
- route execution；
- validation；
- crystal promotion；
- invalidation；
- reopen。

---

# 56. Event Record

```text
RuntimeEvent
- event_id
- epoch
- event_type
- actor
- world_revision
- inputs
- outputs
- causal_parents
- wall_time
- logical_time
- provenance
```

---

# 57. History Is Append-Only by Default

更正舊 event 以新 event 表示。

---

# 58. Why

避免：

$$
\text{state restoration}
=
\text{history erasure}.
$$

---

# 59. Budget State

```text
BudgetState
- work_budget
- time_budget
- memory_budget
- energy_budget
- verification_budget
- risk_budget
- meta_budget
```

---

# 60. Meta Budget

用於：

- chart search；
- scale selection；
- config search；
- route exploration。

---

# 61. Meta Optimization 也不能無限花錢

$$
\boxed{
C_{\mathrm{meta}}
\le
B_{\mathrm{meta}}.
}
$$

---

# 62. Governance State

```text
GovernanceState
- actor_id
- identity
- capabilities
- permissions
- policy_version
- risk_profile
- denied_domains
- denied_scales
- denied_configs
```

---

# 63. Safe Reachable Runtime

任何 active plan 必須：

$$
\boxed{
\mathcal X
\subseteq
\mathfrak F_t^{safe}.
}
$$

---

# 64. Ledger

$$
\boxed{
L_t
}
$$

包含：

- cost records；
- validation records；
- receipts；
- replay digests。

---

# 65. Reference Runtime State

因此：

$$
\boxed{
\mathfrak R_t
=
\left\langle
W_t,
A_t,
F_t,
C_t,
Z_t,
P_t,
K_t,
H_t,
B_t,
G_t,
L_t
\right\rangle.
}
$$

---

# 66. Runtime Tick

定義：

$$
\boxed{
\mathfrak R_{t+1}
=
\operatorname{Tick}
(
\mathfrak R_t,
q_t
).
}
$$

---

# 67. Tick 不等於固定時間步

可以由：

- task；
- event；
- world change；
- validation trigger；

驅動。

---

# 68. Reference Runtime Main Loop

```text
1. Observe
2. Normalize
3. Reveal candidates
4. Check safe reachable set
5. Select chart / scale
6. Select local configuration
7. Select route
8. Execute or shadow-execute
9. Verify
10. Commit state
11. Update cost ledger
12. Compile candidate path
13. Promote / demote crystal
14. Reopen if needed
15. Append history
```

---

# 69. Not Every Tick Runs Every Step

例如 hot crystal hit：

```text
Observe
→ Guard
→ Invoke Crystal
→ Validate
→ Commit
```

---

# 70. Fast Path

$$
\boxed{
\text{Guard}
\rightarrow
\kappa
\rightarrow
V_{\mathrm{cheap}}
}
$$

---

# 71. Slow Path

$$
\boxed{
\text{Reveal}
\rightarrow
\text{Refine}
\rightarrow
\text{Configure}
\rightarrow
\text{Route}
\rightarrow
\text{Deep Verify}.
}
$$

---

# 72. Fallback

fast path fail：

$$
\boxed{
\text{fast}
\rightarrow
\text{slow}.
}
$$

---

# 73. Deny

如果 safe feasible route 不存在：

$$
\boxed{
\operatorname{Deny}.
}
$$

---

# 74. Reveal Operator

$$
\boxed{
\operatorname{Reveal}
:
(\mathfrak R_t,q)
\rightarrow
\widehat{\mathfrak F}_t.
}
$$

---

# 75. Revealed Candidate Types

```text
existing_route
existing_crystal
refinement
coarsening
config_switch
geometry_switch
new_route_candidate
```

---

# 76. Candidate Object

```text
Candidate
- candidate_id
- type
- source
- target
- expected_gain
- expected_cost
- uncertainty
- guard
- authority
```

---

# 77. Candidate Score

第一版：

$$
\boxed{
Score
=
E[\Delta J]
-
C_{\mathrm{meta}}
-
R_{\mathrm{uncertainty}}.
}
$$

---

# 78. Only Positive Candidate

預設：

$$
Score>0
$$

才進下一階段。

---

# 79. Exploration Exception

研究模式可以允許：

$$
Score\le0
$$

但 information gain 高。

---

# 80. Information Gain

$$
\boxed{
VOI
=
E[
J_{\mathrm{before}}
-
J_{\mathrm{after-info}}
]
-
C_{\mathrm{explore}}.
}
$$

---

# 81. Select Chart

$$
\boxed{
\chi^\*
=
\arg\min_{\chi\in\widehat A}
J_\chi.
}
$$

---

# 82. Select Scale

$$
\boxed{
\sigma^\*
=
\arg\max
U_\sigma.
}
$$

---

# 83. Select Configuration

$$
\boxed{
c^\*
=
\arg\min_{c\in C_{\mathrm{safe}}}
J(c).
}
$$

---

# 84. Select Route

$$
\boxed{
\mathcal R^\*
=
\arg\min_{\mathcal R\in P_{\mathrm{safe}}}
J(\mathcal R).
}
$$

---

# 85. Joint Selection

Reference Runtime 可以先分層近似。

不必直接解 full joint optimum。

---

# 86. Why Hierarchical Approximation

full product：

$$
A\times\Sigma\times C\times P\times K
$$

可能組合爆炸。

---

# 87. v0.1 Hierarchy

```text
Atlas
→ Scale
→ Config
→ Route
→ Crystal
```

---

# 88. Later Can Joint Search

Phase C 再做。

---

# 89. Refinement

$$
\boxed{
R_\downarrow
:
u^{(k)}
\rightarrow
W^{(k-1)}.
}
$$

---

# 90. Refinement Preconditions

- authority；
- budget；
- expected utility；
- source availability。

---

# 91. Refinement Receipt

```text
RefinementReceipt
- source
- target_scale
- reason
- cost
- fidelity
- authorization
- source_refs
```

---

# 92. Coarsening

$$
\boxed{
R_\uparrow
:
W^{(k-1)}
\rightarrow
u^{(k)}.
}
$$

---

# 93. Coarsening Preconditions

- fidelity；
- loss budget；
- sufficient stability；
- source retained / reopenability。

---

# 94. Coarsening ≠ Crystallization

Reference Runtime 必須有兩個不同 operation：

```text
COARSEN
CRYSTALLIZE
```

---

# 95. Path Compilation

$$
\boxed{
\operatorname{PC}
:
\Gamma
\rightarrow
\widehat{\ell}.
}
$$

---

# 96. Compile Candidate Record

```text
CompiledPath
- compiled_id
- source_route
- target_transition
- valid_domain
- semantic_contract
- cost_before
- cost_after
- validator
- guard
- status
```

---

# 97. Compilation Does Not Auto-Promote

status：

```text
CANDIDATE
```

---

# 98. Promotion Gate

$$
\boxed{
\operatorname{Promote}=1
}
$$

若：

$$
S\ge\theta_S,
$$

$$
V\ge\theta_V,
$$

$$
U>0,
$$

$$
R\le\theta_R.
$$

---

# 99. Promotion Additional Gate

必須：

```text
reopen_pointer exists
```

或：

```text
reopen_loss_declared = true
```

---

# 100. Crystal Utility

$$
\boxed{
U_\kappa
=
B_{\mathrm{runtime}}
+
B_{\mathrm{future}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{risk}}.
}
$$

---

# 101. Invalidation

$$
\boxed{
\operatorname{Invalidate}(\kappa)
}
$$

trigger：

- world revision；
- dependency change；
- config change；
- policy change；
- empirical failure；
- distribution shift。

---

# 102. Invalidation Is Not Delete

先：

```text
HOT/WARM/COLD → STALE
```

---

# 103. Revalidation

STALE 可以：

```text
STALE → COLD/WARM/HOT
```

重新驗證。

---

# 104. Reopen

$$
\boxed{
\operatorname{Reopen}(\kappa)
\rightarrow
\Gamma_{\mathrm{source}}.
}
$$

---

# 105. Selective Reopen

只展開 relevant subroute。

---

# 106. Full Reopen

audit / deep debug。

---

# 107. Crystal Dependency Graph

$$
\boxed{
G_K
=
(V_K,E_K).
}
$$

---

# 108. Invalidation Propagation

若 parent 依賴 stale child：

$$
\boxed{
\text{child stale}
\Rightarrow
\text{parent revalidate}.
}
$$

---

# 109. Configuration Switch

$$
\boxed{
T_C:
c_i\rightarrow c_j.
}
$$

---

# 110. Config Switch Receipt

```text
ConfigSwitchReceipt
- source_config
- target_config
- reason
- switch_cost
- expected_gain
- realized_gain
- bridge
- validator
```

---

# 111. Scale Switch

$$
T_\Sigma:
\sigma_i\rightarrow\sigma_j.
$$

---

# 112. Geometry Switch

$$
T_G:
g_i\rightarrow g_j.
$$

---

# 113. Switch Cost Must Be Explicit

任何 switch：

$$
C_{\mathrm{switch}}>0
$$

預設。

---

# 114. Thrashing Detector

若：

```text
A → B → A → B
```

短期頻繁發生：

$$
\boxed{
\operatorname{Thrashing}=1.
}
$$

---

# 115. Hysteresis

使用不同 switch-in / switch-out threshold。

---

# 116. Runtime Invariant URR-1

$$
\boxed{
\mathbf W
\neq
\mathfrak R_t.
}
$$

Runtime 不得把自身 state 誤認 World ontology。

---

# 117. URR-2

$$
\boxed{
\text{Computation}
\neq
\text{Observation}
\neq
\text{Materialization}.
}
$$

---

# 118. URR-3

$$
\boxed{
|F_t|<\infty.
}
$$

active frontier 必須有限。

---

# 119. URR-4

$$
\boxed{
\text{Unbounded refinement}
\not\Rightarrow
\text{full materialization}.
}
$$

---

# 120. URR-5

所有 route 必須在 safe feasible state space 中。

$$
\boxed{
\mathcal R
\subseteq
Z_t^{safe}.
}
$$

---

# 121. URR-6

$$
\boxed{
\text{Reachable}
\neq
\text{Authorized}.
}
$$

---

# 122. URR-7

$$
\boxed{
\text{one call}
\neq
\text{one computational transition}.
}
$$

cost ledger 必須保留 hidden thickness。

---

# 123. URR-8

任何 claimed speedup 必須標明 dimension：

- work；
- depth；
- latency；
- route；
- lifecycle。

---

# 124. URR-9

$$
\boxed{
\text{same endpoint}
\not\Rightarrow
\text{same history}.
}
$$

---

# 125. URR-10

Path Compilation 不得僅靠 interface wrapping。

---

# 126. URR-11

Compiled path 不得自動變 crystal。

---

# 127. URR-12

Crystal 不得自動擴張 authority。

---

# 128. URR-13

每個 promoted crystal 必須有：

- valid domain；
- guard；
- validator；
- provenance；
- lifecycle。

---

# 129. URR-14

每個 promoted crystal 必須可 reopen，或顯式宣告不可逆 loss。

---

# 130. URR-15

配置、尺度、幾何切換都必須計 switch cost。

---

# 131. URR-16

Frozen-model experiment 中：

$$
\boxed{
\theta_{t+1}
=
\theta_t
}
$$

模型權重不得變。

---

# 132. URR-16 Purpose

隔離：

$$
\boxed{
\text{architecture gain}
}
$$

與：

$$
\boxed{
\text{model gain}.
}
$$

---

# 133. Reference Experiment Family

第一個 benchmark 不需要複雜遊戲。

可先 synthetic。

---

# 134. Synthetic World A：Sequential

$$
a_1\rightarrow\cdots\rightarrow a_n.
$$

---

# 135. Synthetic World B：Sparse Jump

large state set，但 query 只需少數 target。

---

# 136. Synthetic World C：Parallel Surface

independent tasks。

---

# 137. Synthetic World D：Repeated Retrieval

same semantic family repeated。

---

# 138. Synthetic World E：Recursive

macro node 展開 micro graph。

---

# 139. Synthetic World F：Distribution Shift

中途改 workload。

---

# 140. Baseline 0

Fixed sequential。

---

# 141. Baseline 1

Adaptive route only。

---

# 142. Experimental 2

Adaptive route + config switch。

---

# 143. Experimental 3

Adaptive route + config + crystallization。

---

# 144. Experimental 4

Full scale-aware runtime。

---

# 145. Required Frozen Conditions

- same model；
- same task seeds；
- same hardware；
- same initial world；
- same budget。

---

# 146. Primary Metrics

```text
task_success
total_work
causal_depth
wall_time
route_search_cost
meta_cost
config_switch_cost
scale_switch_cost
verification_cost
crystal_hit_rate
reopen_rate
stale_rate
false_crystal_rate
global_invariant_violations
authorization_violations
```

---

# 147. Structural Learning Metrics

$$
\boxed{
R_{\mathrm{reason}}(t)\downarrow
}
$$

$$
\boxed{
H_{\mathrm{corridor}}(t)\uparrow
}
$$

$$
\boxed{
R_K(t)\uparrow
}
$$

$$
\boxed{
C_{\mathrm{avg}}(t)\downarrow
}
$$

---

# 148. Add Configuration Metrics

$$
\boxed{
Regret_C(t)\downarrow.
}
$$

---

# 149. Add Scale Metrics

$$
\boxed{
FalseRefine(t)\downarrow,
\qquad
FalseCoarsen(t)\downarrow.
}
$$

---

# 150. Add Crystal Quality

$$
\boxed{
A_P(t)\uparrow.
}
$$

promotion accuracy。

---

# 151. Negative Result Conditions

理論需縮減若：

1. meta cost 長期高於 gain；
2. config switch 不改善；
3. crystals 無法帶來 lifecycle gain；
4. reopen / invalidation 太昂貴；
5. existing compiler / cache baseline 完全匹配所有收益。

---

# 152. Runtime Should Prefer Simplicity

如果 fixed route 已足夠：

$$
\boxed{
\operatorname{StayFixed}.
}
$$

---

# 153. Global Capability ≠ Always Reconfigure

真正 global Runtime 必須知道何時「不要做更多」。

---

# 154. Meta Stop Rule

$$
\boxed{
E[\Delta J]
\le
C_{\mathrm{meta}}
\Rightarrow
\operatorname{StopOptimize}.
}
$$

---

# 155. Runtime Modes

```text
FIXED
ADAPTIVE
SHADOW
CRYSTALLIZING
AUDIT
RECOVERY
```

---

# 156. FIXED

不切 config / scale。

---

# 157. ADAPTIVE

允許 route / config switch。

---

# 158. SHADOW

新 route 只 shadow run。

---

# 159. CRYSTALLIZING

收集 promotion evidence。

---

# 160. AUDIT

深度 reopen / replay。

---

# 161. RECOVERY

fast path disabled。

---

# 162. Mode Transition

也應 receipted。

---

# 163. Reference API Surface

```text
observe(world, task)
reveal(state, task)
select_chart(candidates)
refine(target)
coarsen(target)
select_config(domain)
select_route(goal)
execute(route)
verify(receipt)
compile(route)
promote(candidate)
invalidate(crystal)
reopen(crystal)
replay(receipt)
```

---

# 164. Minimal Runtime Interface

每個 adapter 只需實作：

```text
observe
execute
snapshot
restore
validate
```

---

# 165. Why Thin Adapter

避免一開始把整套理論塞進 target system。

---

# 166. Sidecar Architecture

建議：

```text
Target System
    ↕
Thin Adapter
    ↕
UNPNP-II Sidecar Runtime
```

---

# 167. Sidecar Modules

```text
World Registry
Atlas Registry
Frontier Manager
Configuration Router
Corridor Generator
Route Executor
Validator
Path Compiler
Crystal Store
Cost Ledger
Replay Harness
Governance Gate
Experiment Controller
```

---

# 168. World Registry

管理：

- revision；
- domain；
- snapshot。

---

# 169. Atlas Registry

管理 chart / scale / geometry。

---

# 170. Frontier Manager

決定 active scale。

---

# 171. Configuration Router

決定 S/J/P/R 等 form。

---

# 172. Corridor Generator

產生 route candidates。

---

# 173. Route Executor

只執行已授權 route。

---

# 174. Validator

state / causal / config / safety。

---

# 175. Path Compiler

產生 candidate compiled route。

---

# 176. Crystal Store

管理 lifecycle。

---

# 177. Cost Ledger

統一 cost accounting。

---

# 178. Replay Harness

deterministic / approximate replay。

---

# 179. Governance Gate

authority / risk。

---

# 180. Experiment Controller

固定 seed / baseline。

---

# 181. Minimal Data Flow

```text
snapshot
→ observe
→ candidate
→ safe gate
→ route
→ execute
→ receipt
→ validate
→ ledger
→ learn structure
```

---

# 182. Structure Learning Is External

模型權重固定。

---

# 183. Policy Memory

Runtime 可更新：

```text
route_profiles
config_profiles
scale_profiles
crystal_profiles
```

---

# 184. No Hidden Weight Updates

實驗需確認 provider / model 固定。

---

# 185. Deterministic Seed

若 target supports：

```text
seed
```

必須固定。

---

# 186. Replay Contract

```text
ReplayReceipt
- world_snapshot
- task
- model_version
- runtime_version
- seed
- route
- config
- scale
- crystals
- result
- cost
```

---

# 187. Comparison Must Be Pairwise

Baseline 與 experimental 同 seed。

---

# 188. Success Is Statistical

不是看單次漂亮 demo。

---

# 189. Minimum Run Count

依 workload variance 決定。

---

# 190. Cost Normalization

不同 hardware 可用 normalized work / event count。

---

# 191. Wall Time Still Recorded

但不作唯一指標。

---

# 192. Verification Failure Must Be Visible

不能丟棄 failed runs。

---

# 193. Failed Crystal Promotion Is Data

用於 false-crystal metric。

---

# 194. Promotion Gate Pseudocode

```text
if not semantic_valid:
    reject
if risk > risk_limit:
    reject
if reopenability_required and not reopenable:
    reject
if lifecycle_utility <= 0:
    reject
if verification_maturity < threshold:
    keep_candidate
else:
    promote
```

---

# 195. Fast Path Pseudocode

```text
if crystal.guard(state, task):
    result = crystal.invoke(...)
    if cheap_validate(result):
        commit(result)
    else:
        mark_stale(crystal)
        fallback()
else:
    slow_path()
```

---

# 196. Slow Path Pseudocode

```text
observe
reveal
select chart
select scale
select config
route
execute
deep verify
commit
consider compile
```

---

# 197. Invalidation Pseudocode

```text
for crystal in affected_crystals(change):
    crystal.state = STALE
    enqueue_parent_revalidation(crystal)
```

---

# 198. Refinement Pseudocode

```text
if value_of_information > refinement_cost:
    materialize_lower_scale()
else:
    stay_coarse()
```

---

# 199. Configuration Switch Pseudocode

```text
if expected_gain > switch_cost + uncertainty_penalty:
    shadow_or_switch()
else:
    stay()
```

---

# 200. Reference Objective

第一版：

$$
\boxed{
J
=
\alpha_W W
+
\alpha_D D_C
+
\alpha_T T
+
\alpha_M M
+
\alpha_V V
+
\alpha_R R
+
\alpha_L L
+
\alpha_S S.
}
$$

---

# 201. Weights Are Scenario-Specific

不能用一組 universal weights。

---

# 202. Pareto Mode

Reference Runtime 應支援：

```text
objective_mode = PARETO
```

---

# 203. Pareto Candidate Set

保留 nondominated candidates。

---

# 204. User / Policy Selects among Pareto Set

---

# 205. Runtime Must Expose Why

每個選擇應能回答：

```text
why_this_chart
why_this_scale
why_this_config
why_this_route
why_this_crystal
```

---

# 206. Explanation Is Receipt Projection

不是模型事後編故事。

---

# 207. Reference Invariant Summary

URR-1 ～ URR-16 應寫進 test suite。

---

# 208. Invariant Test Examples

### URR-7

一個 wrapper 不得降低 work metric，除非真正 execution 下降。

---

# 209. URR-11

compiled path 不得自動 HOT。

---

# 210. URR-12

crystal authority 不得大於 source authority。

---

# 211. URR-14

promotion without reopen pointer 必須 fail，除非 irreversible explicitly allowed。

---

# 212. URR-15

switch cost 不得默認零。

---

# 213. Reference Runtime State Machine

核心 mode：

$$
\boxed{
IDLE
\rightarrow
OBSERVED
\rightarrow
PLANNED
\rightarrow
EXECUTED
\rightarrow
VERIFIED
\rightarrow
COMMITTED
}
$$

旁路：

$$
\boxed{
FAILED
\rightarrow
RECOVERY
}
$$

---

# 214. Crystal State Machine

$$
CANDIDATE
\rightarrow
COLD
\rightarrow
WARM
\rightarrow
HOT.
$$

任意 active state 可：

$$
\rightarrow
STALE
\rightarrow
RETIRED.
$$

---

# 215. Scale State Machine

```text
COARSE
↕
MESO
↕
FINE
```

---

# 216. Config State Machine

v0.1：

```text
S
J
P
R
```

---

# 217. Config Transition Need Not Be Complete Graph

只有 validated transitions。

---

# 218. Reference Transition Matrix

例如：

| From | To | Default |
|---|---|---|
| S | J | allowed with index/sparse guard |
| S | P | allowed with independence proof |
| J | R | allowed after stable direct retrieval |
| P | R | allowed after crystallization |
| R | S | fallback |
| R | J | reopen / selective search |

---

# 219. Matrix Is Example, Not Theory Law

不同 workload 可不同。

---

# 220. Geometry Matrix

同理只建立 validated bridges。

---

# 221. Scale Matrix

跨多層 jump 需 stronger validation。

---

# 222. Runtime Versioning

```text
urr_runtime_version
schema_version
theory_version
```

分開。

---

# 223. Why Separate

理論版本與實作 schema 可不同步。

---

# 224. Theory Version

```text
UNPNP-II v0.1
```

---

# 225. Runtime Version

```text
URR v0.1
```

---

# 226. Experimental Profile Version

```text
EXP_PROFILE v0.1
```

---

# 227. No Silent Schema Mutation

任何 migration 留 receipt。

---

# 228. Reference Storage

第一版可 SQLite / JSONL。

---

# 229. Suggested Tables

```text
worlds
domains
charts
frontier
configurations
routes
route_segments
crystals
crystal_dependencies
events
cost_records
validation_records
receipts
experiments
```

---

# 230. Why Relational First

易查、易 diff、易 replay。

---

# 231. Graph View Can Be Derived

不必一開始使用 graph DB。

---

# 232. Canonical Event Log

JSONL 也可作 append-only experiment ledger。

---

# 233. Receipt Hash

每個 receipt：

$$
\boxed{
h_r
=
H(\text{canonical receipt bytes}).
}
$$

---

# 234. Replay Chain

receipt 可鏈：

```text
parent_receipt_hash
```

---

# 235. Provenance Integrity

不是 security guarantee，但便於 audit。

---

# 236. Deterministic Serialization

固定 key order / UTF-8。

---

# 237. Runtime Observer

需要 collector：

- state；
- cost；
- causal parents；
- materialization；
- config；
- scale。

---

# 238. If Target Cannot Expose Work

用 proxy metric：

- function count；
- tool calls；
- model calls；
- game actions；
- DB queries。

---

# 239. Metric Honesty

proxy 必須標：

```text
metric_kind = proxy
```

---

# 240. Do Not Pretend Proxy Is Physical Work

---

# 241. Causal Depth Estimation

若 target trace 有 dependency，可算 DAG longest path。

---

# 242. If Dependency Unknown

標：

```text
causal_depth = unknown
```

而不是拿 step count 代替。

---

# 243. Unknown Is Valid

Reference Runtime 應支援：

$$
\bot
$$

unknown。

---

# 244. Missing Metric Does Not Become Zero

$$
\boxed{
\text{unknown}
\neq
0.
}
$$

---

# 245. This Is Critical

避免 false speedup。

---

# 246. Validation Maturity

第一版：

```text
NONE
SMOKE
REPLAY
PROPERTY
DIFFERENTIAL
FORMAL
```

---

# 247. Maturity Is Ordered Only Partially

formal 不代表所有 empirical conditions。

---

# 248. Validation Profile

可多個同時。

---

# 249. Risk Profile

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

# 250. Critical Requires Stronger Gate

---

# 251. Runtime Default Safety

若未知：

```text
fail closed for authority
fall back for optimization
```

---

# 252. Optimization Failure ≠ Task Failure

如果 optimizer 不確定，可跑 canonical route。

---

# 253. Canonical Route

每個 experiment 應有：

$$
\boxed{
\mathcal R_{\mathrm{canonical}}.
}
$$

---

# 254. Why

提供 fallback 與 baseline。

---

# 255. No Optimizer Without Baseline

否則無法知道 improvement。

---

# 256. Benchmark Receipts

每次 run 輸出：

```text
ExperimentReceipt
- experiment_id
- group
- seed
- task
- success
- world_revision
- route
- cost_vector
- crystal_hits
- switches
- failures
- validation
```

---

# 257. A/B/C/D Groups

建議：

### A

Fixed canonical。

### B

Adaptive route。

### C

Adaptive route + crystal。

### D

Adaptive route + crystal + scale/config routing。

---

# 258. Same Model

全部同一 $\theta$。

---

# 259. Same Initial World

---

# 260. Same Seed

---

# 261. Same Budget

---

# 262. Primary Hypothesis H1

$$
\boxed{
E[J_D]
<
E[J_A]
}
$$

在適合 workload family 中。

---

# 263. H2

$$
\boxed{
R_{\mathrm{reason},D}(t)
\downarrow
}
$$

隨 repeated workload。

---

# 264. H3

$$
\boxed{
R_{K,D}(t)
\uparrow
}
$$

但 false-crystal 不上升。

---

# 265. H4

$$
\boxed{
Regret_C(t)
\downarrow.
}
$$

---

# 266. H5

$$
\boxed{
ReopenSuccess(t)
}
$$

維持高。

---

# 267. H6

$$
\boxed{
AuthorizationViolation=0.
}
$$

---

# 268. Negative Hypothesis

若 meta overhead 太大：

$$
E[J_D]
\ge
E[J_A].
$$

---

# 269. That Is Acceptable Result

理論可能只適合特定 workload。

---

# 270. Workload Conditions for Likely Benefit

- repeated patterns；
- heterogeneous structure；
- reusable routes；
- meaningful scale separation；
- stable subdomains。

---

# 271. Workload Conditions for Likely No Benefit

- one-shot tiny task；
- no repeated structure；
- extremely volatile world；
- switch cost huge；
- no observable internal state。

---

# 272. This Boundary Must Be Empirical

---

# 273. Reference Runtime First Implementation Order

### Step 1

Event / receipt ledger。

---

# 274. Step 2

World / domain snapshots。

---

# 275. Step 3

Fixed route baseline。

---

# 276. Step 4

Cost vector。

---

# 277. Step 5

Adaptive route candidate selection。

---

# 278. Step 6

Path compilation candidate。

---

# 279. Step 7

Crystal lifecycle。

---

# 280. Step 8

Scale coarse/fine。

---

# 281. Step 9

S/J/P/R config routing。

---

# 282. Step 10

Cross-scale / cross-config route。

---

# 283. Do Not Start with Full WRO Solver

這會過度複雜。

---

# 284. Start with Measurable Slice

先證明：

$$
\boxed{
\text{structural adaptation}
}
$$

真的降低某些成本。

---

# 285. First Milestone

在 frozen model 下：

$$
C_{\mathrm{avg}}(t)\downarrow.
$$

---

# 286. Second Milestone

能區分：

```text
macro wrapper
vs
real compiled path
```

---

# 287. Third Milestone

能安全 stale / reopen。

---

# 288. Fourth Milestone

config router 能因 workload shift：

$$
S\leftrightarrow J\leftrightarrow P\leftrightarrow R.
$$

---

# 289. Fifth Milestone

scale router 能避免 over-refine / over-coarsen。

---

# 290. Sixth Milestone

whole system 不破 global invariants。

---

# 291. URR Reference Success Condition

$$
\boxed{
\text{Correctness}
+
\text{Measurable Structural Gain}
+
\text{Replayability}
+
\text{Reopenability}
+
\text{Authority Preservation}.
}
$$

---

# 292. What URR v0.1 Does Not Need

- perfect optimizer；
- all 72 cells；
- quantum runtime；
- general theorem prover；
- arbitrary world support；
- autonomous external side effects。

---

# 293. What It Must Have

- explicit state；
- explicit costs；
- explicit receipts；
- explicit validity；
- explicit fallback。

---

# 294. The Minimal Philosophy

$$
\boxed{
\text{Observe what changed,}
}
$$

$$
\boxed{
\text{record why it changed,}
}
$$

$$
\boxed{
\text{measure whether it helped,}
}
$$

$$
\boxed{
\text{and preserve a way back.}
}
$$

---

# 295. Core Runtime Contract

```text
No optimization without measurement.
No promotion without validation.
No crystal without provenance.
No fast path without guard.
No scale jump without fidelity.
No authority gain from speed.
No claim of one without hidden-thickness accounting.
```

---

# 296. Why This Is Enough for Phase B

因為後續所有實驗都可以共用這套 Runtime object model。

---

# 297. Game Adapter

只需把 game state 映到：

$$
W_t.
$$

---

# 298. Agent Adapter

只需把 persona / memory / action 映到 domain + route。

---

# 299. Legacy Program Adapter

只需把 trace / call / state 映到 event / route。

---

# 300. Mathematical Runtime Adapter

可把 proof / solver / search 映到 heterogeneous route。

---

# 301. Same Core, Different Adapter

這才是 Reference Runtime 的價值。

---

# 302. Phase B Paper 02

下一篇應正式建立：

## Experimental Protocol and Benchmark Matrix

把 synthetic、Adventure Land、Generative Agents 三個實驗全部規格化。

---

# 303. Phase B Paper 03

之後：

## Minimal Sidecar Implementation Specification

直接給本地端 AI / Codex 實作。

---

# 304. Phase B Paper 04

最後：

## Formal Invariants and Model Checking Targets

把 URR-1～URR-16 轉成 test / property / formalization targets。

---

# 305. Phase B 建議總計四篇

1. **Formal Core and Reference Runtime**
2. **Experimental Protocol and Benchmark Matrix**
3. **Minimal Sidecar Implementation Specification**
4. **Formal Invariants and Verification Targets**

---

# 結論

UNPNP-II 的理論階段已經回答：

> 世界可以怎麼被切、怎麼被看、怎麼被算、怎麼被走、怎麼被結晶。

Reference Runtime 現在把這些概念壓成：

$$
\boxed{
\mathfrak R_t
=
\left\langle
W_t,
A_t,
F_t,
C_t,
Z_t,
P_t,
K_t,
H_t,
B_t,
G_t,
L_t
\right\rangle.
}
$$

它不要求一次解完整 World-Relative Optimization。

它只要求每一個 structural adaptation 都能回答：

1. **你改了什麼？**
2. **為什麼改？**
3. **花了多少？**
4. **真的有比較好嗎？**
5. **是否合法？**
6. **怎麼驗證？**
7. **失敗時怎麼回去？**

因此 Reference Runtime 的真正核心不是「最聰明的 optimizer」，而是：

$$
\boxed{
\textbf{
一個能讓路徑、尺度、計算形態與結晶化被明確觀察、明確量測、明確驗證、明確回退的實驗運行層。
}
}
$$

這就是 UNPNP-II 從理論系列正式進入實作與可證偽實驗階段的第一個共同基準。
