# UNPNP-II Phase B — Paper 02
## Experimental Protocol and Benchmark Matrix
### 多尺度路徑、配置切換與計算結晶化的統一可證偽實驗協議

**系列：** UNPNP-II / Multi-Scale Computational Geometry — Phase B  
**篇次：** Phase B Paper 02  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-09  
**文件性質：** Experimental Protocol／Benchmark Matrix／Falsifiability Specification  
**前置：** Phase B Paper 01《Formal Core and Reference Runtime》；UNPNP-II v0.1；UNPNP-I；MWT；GCM  
**狀態：** Canonical Draft

---

## 摘要

Phase B Paper 01 已提出 UNPNP-II Reference Runtime（URR-v0.1），並建立：

- explicit world state；
- computational atlas；
- active refinement frontier；
- configuration field；
- safe charted state space；
- route registry；
- crystal lifecycle；
- cost ledger；
- replay contract；
- URR-1 ～ URR-16 runtime invariants。

本文不再增加新的主要理論層，而是回答：

> **UNPNP-II 到底要怎麼被公平地測？**

核心原則是：

$$
\boxed{
\theta_{t+1}
=
\theta_t
}
$$

即 frozen-model experiment：在主要架構比較中，模型權重、模型版本與 provider 固定，只允許 Runtime 外部結構改變：

$$
\boxed{
\Omega_{t+1}
\neq
\Omega_t.
}
$$

測試重點不是「模型有沒有變聰明」，而是：

> **同一個模型，是否因 route、scale、configuration、crystal 與 external structure 的成熟，而在未來重複工作中變得更低成本、更穩定、更可驗證？**

本文建立四組統一實驗組：

### Group A — Fixed Canonical

固定 representation、固定 scale、固定 computational form、固定 canonical route，不使用 persistent corridor 或 crystal。

### Group B — Adaptive Route

允許 route reveal、Adaptive Corridor 與短期 routing，但不允許 persistent crystal。

### Group C — Crystallized Route

在 B 基礎上加入 Path Compilation、EHPE、Crystal Store、Fast / Slow Path、Invalidation 與 Reopen。

### Group D — Full UNPNP-II

在 C 基礎上再加入：

- scale refinement / coarsening；
- geometry-aware routing；
- S/J/P/R configuration switching；
- configuration receipts；
- cross-scale / cross-configuration path compilation。

因此：

$$
\boxed{
A
\subset
B
\subset
C
\subset
D.
}
$$

這個 inclusion 是 feature-set inclusion，不代表 performance 單調提升。若：

$$
J_D
>
J_A,
$$

則 D 在該 workload 下可能是負優化。

本文規定三層 benchmark family：

1. **Synthetic Worlds**：用人工可控世界測最小因果；
2. **Adventure Land**：測 real-time game loop、重複任務與程序路徑；
3. **Generative Agents**：測 cognitive loop、memory routing、long-horizon repeated semantic paths。

所有 benchmark 共享同一個核心成本向量：

$$
\boxed{
\mathbf C
=
(
W,
D_C,
T,
M,
V,
R,
C_{\mathrm{meta}},
C_{\mathrm{switch}},
C_{\mathrm{maintain}},
L_O
).
}
$$

並共享主要結構學習指標：

$$
R_{\mathrm{reason}}(t),
\quad
H_{\mathrm{corridor}}(t),
\quad
R_K(t),
\quad
Regret_C(t),
\quad
C_{\mathrm{avg}}(t).
$$

本文最後給出：

- benchmark matrix；
- seed / replay requirements；
- statistical protocol；
- workload shift protocol；
- promotion / invalidation stress tests；
- false crystal tests；
- scale misclassification tests；
- config-regret tests；
- success / failure / falsification criteria。

---

# 1. 實驗哲學

UNPNP-II 不能靠：

- 漂亮 demo；
- 一次成功；
- 主觀「看起來更快」；
- 模型自己說它學會了；

來支持。

需要：

$$
\boxed{
\text{controlled comparison}
+
\text{replay}
+
\text{measurement}
+
\text{falsification}.
}
$$

---

# 2. 主實驗問題

核心問題 Q1：

> frozen model 下，Runtime structural adaptation 是否能降低 repeated workload 的總成本？

形式：

$$
\boxed{
E[J_D]
<
E[J_A]
}
$$

在某些明確 workload family 中成立。

---

# 3. 第二問題

Q2：

> 成本下降是否來自真正 structural gain，而不是 wrapper / cache illusion？

---

# 4. 第三問題

Q3：

> crystallization 是否能在不提高 false-route / stale-route / safety failure 的情況下降低未來成本？

---

# 5. 第四問題

Q4：

> scale / configuration routing 是否能在 workload shift 後切換到更合適的 form？

---

# 6. 第五問題

Q5：

> Full UNPNP-II 的 meta overhead 是否低於其帶來的 lifecycle gain？

---

# 7. Frozen-Model Contract

每個 A/B/C/D run 必須：

```text
same model provider
same model version
same decoding parameters
same initial world
same task
same seed where supported
same budget
same external data snapshot
```

---

# 8. Model Version Pinning

記：

```text
model_id
model_version
provider
temperature
top_p
tool_mode
```

---

# 9. No Silent Model Upgrade

若 provider 無法保證完全 pin version，需記：

```text
model_pin_strength = WEAK
```

---

# 10. Provider Drift

若偵測 model behavior drift，該 batch 標：

```text
provider_drift = true
```

不得直接跟舊 batch 混合。

---

# 11. Runtime Version Pinning

```text
urr_runtime_version
adapter_version
benchmark_version
```

全部記錄。

---

# 12. World Snapshot Pinning

每個 run 開始前保存：

$$
W_0^{(seed)}.
$$

---

# 13. Seed Contract

如果 target 支援 random seed：

$$
seed_A=seed_B=seed_C=seed_D.
$$

---

# 14. Non-Deterministic Targets

如果無法完全固定：

- 增加 repetitions；
- 記 event trace；
- 用 paired analysis。

---

# 15. Group A — Fixed Canonical

A 的功能：

```text
fixed chart
fixed scale
fixed configuration
fixed canonical route
no persistent crystal
no adaptive reconfiguration
```

---

# 16. A 的目的

提供：

$$
\boxed{
\text{non-adaptive reference cost}.
}
$$

---

# 17. Group B — Adaptive Route

B 允許：

```text
candidate reveal
route search
adaptive corridor
temporary route cache
```

但不允許：

```text
persistent compiled path
persistent crystal
```

---

# 18. B 測什麼

隔離：

$$
\boxed{
\text{online adaptive routing gain}.
}
$$

---

# 19. Group C — Crystallized Route

C = B +

```text
path compilation
EHPE gate
crystal store
fast path
slow path
invalidation
reopen
```

---

# 20. C 測什麼

隔離：

$$
\boxed{
\text{persistent structural learning gain}.
}
$$

---

# 21. Group D — Full UNPNP-II

D = C +

```text
scale router
geometry router
configuration router
S/J/P/R switching
cross-scale links
cross-config links
configuration receipts
```

---

# 22. D 測什麼

隔離：

$$
\boxed{
\text{multi-scale / configuration-routing gain}.
}
$$

---

# 23. Feature Inclusion

$$
A
\subset
B
\subset
C
\subset
D.
$$

---

# 24. Performance Does Not Need Inclusion

不要求：

$$
J_A
>
J_B
>
J_C
>
J_D.
$$

---

# 25. Negative Result Is Valid

例如 simple workload：

$$
J_A<J_D
$$

可能是正確結果。

---

# 26. Benchmark Family 1：Synthetic Worlds

Synthetic World 的目的：

> 先把理論 causal effect 拆乾淨。

---

# 27. SW-01 Sequential Chain

世界：

$$
a_1
\rightarrow
a_2
\rightarrow
\cdots
\rightarrow
a_n.
$$

---

# 28. SW-01 Expected Result

若無可壓縮 repeated structure：

$$
D
$$

不應神奇大幅優於 A。

---

# 29. SW-01 是 Anti-Hype Test

如果 D 在純線性不可壓縮 task 宣稱巨大 gain，應懷疑 metric。

---

# 30. SW-02 Sparse Jump

state space 很大，但每 task 只需少量 target。

---

# 31. SW-02 Expected Pattern

$$
S
\rightarrow
J
$$

可能有利。

---

# 32. SW-02 Metrics

- scanned nodes；
- resolve cost；
- index build；
- jump hit；
- lifecycle cost。

---

# 33. SW-03 Parallel Surface

建立 $n$ 個 independent tasks。

---

# 34. SW-03 Expected Pattern

$$
S
\rightarrow
P.
$$

---

# 35. SW-03 Key Distinction

預期：

$$
W_P
\approx
W_S,
$$

但：

$$
D_P
<
D_S.
$$

---

# 36. SW-04 Repeated Retrieval

固定 semantic task family 重複出現。

---

# 37. SW-04 Expected Pattern

$$
S/J
\rightarrow
R.
$$

---

# 38. SW-04 Tests

- crystal formation；
- guard hit；
- stale rate；
- false retrieval；
- maintenance。

---

# 39. SW-05 Recursive World

macro node 可展開 micro graph。

---

# 40. SW-05 Compare

A：

```text
always fine
```

D：

```text
adaptive coarse/fine
```

---

# 41. SW-05 Metrics

- refinement count；
- active nodes；
- false coarsening；
- false refinement；
- total meta cost。

---

# 42. SW-06 Geometry Shift

前半 workload 是 line，

後半變 surface / cluster。

---

# 43. SW-06 Purpose

測：

$$
g_t
\rightarrow
g_{t+1}
$$

是否能適應。

---

# 44. SW-07 Configuration Shift

前半 sparse query：

$$
J
$$

有利。

後半 dense batch：

$$
P
$$

有利。

---

# 45. SW-07 Primary Metric

$$
Regret_C(t).
$$

---

# 46. SW-08 Crystal Staleness

先讓 crystal 成熟，再改 dependency。

---

# 47. Expected

```text
HOT → STALE → reopen → revalidate/retire
```

---

# 48. SW-09 False Crystal Trap

設計一條 route 在 training-like subset 很好，但 unseen subset 失效。

---

# 49. Expected

guard 應拒絕：

$$
D_{\mathrm{new}}\not\subset D_\kappa.
$$

---

# 50. SW-10 Hidden Cost Wrapper

把昂貴 route 包成一個 function call。

---

# 51. Expected

$$
H_O\downarrow
$$

但：

$$
W,D,T
$$

不應被誤報下降。

---

# 52. Benchmark Family 2：Adventure Land

Adventure Land 用於：

- real-time loop；
- repeated action family；
- navigation；
- inventory；
- combat；
- bank/restock cycle。

---

# 53. Canonical Task Family

$$
\boxed{
\text{farm}
\rightarrow
\text{restock}
\rightarrow
\text{bank}
\rightarrow
\text{return}.
}
$$

---

# 54. AL-01 Farm Loop

固定地點、固定角色、固定怪物 family。

---

# 55. AL-01 Measure

- AI decisions；
- game actions；
- movement actions；
- tool / model calls；
- failures；
- deaths；
- latency。

---

# 56. AL-02 Restock

需要：

- detect inventory；
- choose shop；
- navigate；
- buy；
- return。

---

# 57. AL-03 Bank

需要：

- detect threshold；
- navigate；
- deposit；
- restore route。

---

# 58. AL-04 Full Cycle

重複：

$$
N
$$

輪。

---

# 59. AL-04 Purpose

最適合看：

$$
R_K(t)\uparrow,
\qquad
C_{\mathrm{avg}}(t)\downarrow.
$$

---

# 60. AL-05 Map Shift

改怪物位置 / route condition。

---

# 61. AL-05 Purpose

測 stale crystal / reopen。

---

# 62. AL-06 Inventory Shift

改 item requirement。

---

# 63. AL-07 Risk Event

生命值低、危險區域、錯誤路徑。

---

# 64. AL-07 Purpose

測 fast path 是否安全 fallback。

---

# 65. Adventure Land Adapter Principle

盡量：

$$
\boxed{
\text{zero or minimal core rewrite}.
}
$$

---

# 66. External Sidecar

```text
Adventure Land
↕
Thin Adapter
↕
URR Sidecar
```

---

# 67. Adapter Observations

```text
position
hp/mp
inventory
target
map
bank status
cooldowns
events
```

---

# 68. Adapter Actions

```text
move
smart_move
attack
use_skill
buy
bank
equip
```

---

# 69. BehaviorCrystal

最小：

```text
crystal_id
task_family
guard
action_procedure
validator
source_traces
lifecycle
```

---

# 70. AL Group A

固定手寫 / canonical behavior。

---

# 71. AL Group B

每輪 adaptive reasoning / route。

---

# 72. AL Group C

B + BehaviorCrystal。

---

# 73. AL Group D

C + scale/config switching。

---

# 74. AL Scale Example

COARSE：

```text
farm_cycle
```

MESO：

```text
farm/restock/bank/return
```

FINE：

```text
navigation/action/state checks
```

---

# 75. AL Config Example

S：

逐步 navigation。

J：

direct semantic target / sparse shortcut。

P：

independent inventory checks / parallel planning where safe。

R：

stable route / behavior crystal retrieval。

---

# 76. AL Primary Success

在 correctness 不惡化下：

$$
N_{\mathrm{model\ calls},C}
<
N_{\mathrm{model\ calls},B}.
$$

---

# 77. AL Secondary Success

$$
C_{\mathrm{decision},C}
<
C_{\mathrm{decision},B}.
$$

---

# 78. AL Failure Criteria

- death rate 上升；
- stuck rate 上升；
- stale behavior 使用；
- wrong-map fast path；
- switch overhead > gain。

---

# 79. Benchmark Family 3：Generative Agents

GA 用於測：

- repeated cognitive loop；
- memory retrieval；
- plan / reflect；
- long-horizon semantic recurrence；
- crystallized memory navigation。

---

# 80. Canonical Cognitive Loop

$$
\boxed{
\text{perceive}
\rightarrow
\text{retrieve}
\rightarrow
\text{plan}
\rightarrow
\text{reflect}
\rightarrow
\text{execute}.
}
$$

---

# 81. GA-01 Repeated Routine

同 persona 每天做類似 routine。

---

# 82. GA-02 Repeated Memory Query

反覆需要：

- same person；
- same place；
- same unresolved goal；
- same plan family。

---

# 83. GA-03 Social Recurrence

重複遇到同一角色。

---

# 84. GA-04 Novel Event

加入新事件打破 crystal。

---

# 85. GA-05 Contradictory Memory

加入 conflicting memory。

---

# 86. GA-06 Long-Horizon Task

跨多 step / day。

---

# 87. GA Adapter Hook

最小 hook 位置：

```text
perceive
retrieve
plan
reflect
execute
```

---

# 88. GA Group A

原生 canonical retrieval / planning。

---

# 89. GA Group B

adaptive route / memory search。

---

# 90. GA Group C

memory route crystallization。

---

# 91. GA Group D

C + scale/config routing。

---

# 92. GA Scale Example

COARSE：

persona / project crystal。

MESO：

memory cluster / episode。

FINE：

individual memory nodes / source traces。

---

# 93. GA Config Example

S：

stepwise scan。

J：

selective memory jump。

P：

parallel candidate evaluation。

R：

crystal-first retrieval。

---

# 94. GA Primary Metric

$$
N_{\mathrm{retrieval\ expansion}}.
$$

---

# 95. GA Secondary Metrics

- model calls；
- retrieved nodes；
- context tokens；
- memory precision；
- contradiction misses；
- route reuse；
- crystal stale rate。

---

# 96. GA Correctness Requirement

不能只看少 token。

必須保留：

- relevant recall；
- contradiction recall；
- goal continuity；
- persona consistency。

---

# 97. GA False Shortcut

如果 crystal 只找到 old answer，漏掉 new contradictory evidence，即失敗。

---

# 98. Crystal-First Does Not Mean Crystal-Only

原則：

$$
\boxed{
\text{Crystal First}
\rightarrow
\text{Source on Demand}.
}
$$

---

# 99. Benchmark Matrix

| ID | World | Core phenomenon | Primary groups | Expected differentiator |
|---|---|---|---|---|
| SW-01 | Synthetic | pure sequential | A-D | anti-hype control |
| SW-02 | Synthetic | sparse jump | A-D | S→J |
| SW-03 | Synthetic | parallel surface | A-D | S→P |
| SW-04 | Synthetic | repeated retrieval | A-D | J/S→R |
| SW-05 | Synthetic | recursive scale | A-D | scale routing |
| SW-06 | Synthetic | geometry shift | A-D | geometry adaptation |
| SW-07 | Synthetic | config shift | A-D | config regret |
| SW-08 | Synthetic | crystal stale | C-D | invalidation |
| SW-09 | Synthetic | false crystal | C-D | guard quality |
| SW-10 | Synthetic | wrapper illusion | A-D | hidden thickness |
| AL-01 | Adventure Land | farm | A-D | repeated action |
| AL-02 | Adventure Land | restock | A-D | routing |
| AL-03 | Adventure Land | bank | A-D | route reuse |
| AL-04 | Adventure Land | full cycle | A-D | lifecycle gain |
| AL-05 | Adventure Land | map shift | C-D | reopen |
| AL-06 | Adventure Land | inventory shift | C-D | stale guard |
| AL-07 | Adventure Land | risk | C-D | fallback safety |
| GA-01 | Generative Agents | routine | A-D | cognition reuse |
| GA-02 | Generative Agents | memory query | A-D | crystal retrieval |
| GA-03 | Generative Agents | social recurrence | A-D | route reuse |
| GA-04 | Generative Agents | novelty | C-D | reopen |
| GA-05 | Generative Agents | conflict | C-D | anti-stale |
| GA-06 | Generative Agents | long horizon | A-D | context reduction |

---

# 100. Core Cost Vector

所有 benchmark 至少記：

$$
\boxed{
\mathbf C
=
(
W,
D_C,
T,
M,
V,
R,
C_{\mathrm{meta}},
C_{\mathrm{switch}},
C_{\mathrm{maintain}},
L_O
).
}
$$

---

# 101. $W$ — Work

如果無 physical op count，使用 proxy。

---

# 102. Work Proxy Examples

Synthetic：

```text
primitive operations
```

Adventure Land：

```text
decision calls + game actions
```

GA：

```text
model calls + memory scoring + retrieval expansions
```

---

# 103. Proxy Must Be Declared

```text
work_metric_kind = PROXY
```

---

# 104. $D_C$ — Causal Depth

若 dependency graph 可知，計 longest chain。

---

# 105. Unknown Causal Depth

如果不知道：

```text
causal_depth = null
```

---

# 106. Null ≠ Zero

---

# 107. $T$ — Wall Time

record real elapsed time。

---

# 108. Timing Noise

同一 experiment 需多 run。

---

# 109. $M$ — Materialization

可用：

- active nodes；
- context size；
- state records；
- memory bytes。

---

# 110. $V$ — Verification Cost

包括：

- validators；
- replay；
- deep check；
- differential run。

---

# 111. $R$ — Risk

第一版可用 ordinal / event count。

---

# 112. $C_{\mathrm{meta}}$

包含：

- chart selection；
- scale decision；
- route search；
- config search。

---

# 113. $C_{\mathrm{switch}}$

scale / config / geometry transition overhead。

---

# 114. $C_{\mathrm{maintain}}$

crystal store / invalidation / revalidation。

---

# 115. $L_O$

observation / projection loss。

---

# 116. Structural Metrics

$$
\boxed{
R_{\mathrm{reason}}(t)
=
\frac{C_{\mathrm{reason}}(t)}
{C_{\mathrm{total}}(t)}.
}
$$

---

# 117. Corridor Hit Ratio

$$
\boxed{
H_{\mathrm{corridor}}(t)
=
\frac{\text{successful reused corridors}}
{\text{eligible route requests}}.
}
$$

---

# 118. Crystal Hit Ratio

$$
\boxed{
R_K(t)
=
\frac{\text{valid crystal hits}}
{\text{eligible crystal requests}}.
}
$$

---

# 119. Configuration Regret

$$
\boxed{
Regret_C
=
J(c_{\mathrm{chosen}})
-
J(c_{\mathrm{best-known}}).
}
$$

---

# 120. Average Cost

$$
\boxed{
C_{\mathrm{avg}}(t)
=
\frac{1}{N_t}
\sum_{i=1}^{N_t}
J_i.
}
$$

---

# 121. Promotion Accuracy

$$
\boxed{
A_P
=
\frac{\text{beneficial promoted crystals}}
{\text{all promoted crystals}}.
}
$$

---

# 122. False Crystal Rate

$$
\boxed{
F_K
=
\frac{\text{promoted crystals later invalidated by correctness failure}}
{\text{all promoted crystals}}.
}
$$

---

# 123. Stale Use Rate

$$
\boxed{
S_U
=
\frac{\text{uses after invalidation condition}}
{\text{all crystal uses}}.
}
$$

---

# 124. Reopen Success

$$
\boxed{
R_O
=
\frac{\text{successful fallback / reopen}}
{\text{required reopens}}.
}
$$

---

# 125. False Refinement

展開但沒有資訊 / route gain。

---

# 126. False Coarsening

粗化導致 lost invariant / wrong action。

---

# 127. Switch Thrashing

$$
\boxed{
T_S
=
\frac{\text{rapid reversals}}
{\text{all switches}}.
}
$$

---

# 128. Global Invariant Violation

任何 cross-domain incoherence 記：

```text
global_invariant_violation = 1
```

---

# 129. Authorization Violation

要求：

$$
\boxed{
N_{\mathrm{auth\ violation}}=0.
}
$$

---

# 130. Statistical Unit

主要分析單位：

$$
\boxed{
\text{seed-paired task episode}.
}
$$

---

# 131. Pairing

同一 seed：

```text
A(seed_i)
B(seed_i)
C(seed_i)
D(seed_i)
```

成一組。

---

# 132. Why Pairing

降低 world randomness variance。

---

# 133. Minimum Replication

Synthetic：

至少：

```text
30 paired seeds
```

作初步。

---

# 134. Game / GA

因成本較高，可先：

```text
10–30 paired seeds
```

再依 variance 擴張。

---

# 135. Not a Universal Statistical Law

實際 sample size 由 power / variance 決定。

---

# 136. Summary Statistics

報：

- mean；
- median；
- p50 / p90 / p95；
- standard deviation；
- failure rate；
- paired difference。

---

# 137. Avoid Only Mean

因 latency / failure 常 heavy-tail。

---

# 138. Primary Comparison

$$
\Delta J_{D-A}
=
J_D-J_A.
$$

---

# 139. Secondary Comparisons

$$
\Delta J_{B-A},
\quad
\Delta J_{C-B},
\quad
\Delta J_{D-C}.
$$

---

# 140. Why Incremental Comparison

知道 gain 來自：

- adaptive route；
- crystal；
- full scale/config。

---

# 141. Learning Curve

對 repeated workload：

$$
J(t).
$$

---

# 142. Desired Pattern

若 structural learning 成立：

$$
\boxed{
\frac{dJ_C}{dt}<0
}
$$

或 D。

---

# 143. But Plateau Is Expected

不要求永遠下降。

---

# 144. Saturation

最終：

$$
J(t)\rightarrow J_\infty.
$$

---

# 145. Overfitting Check

training-like repeated tasks 之外加入 held-out task variation。

---

# 146. Crystal Generalization

測：

$$
x\in D_\kappa
$$

但不是 exact seen input。

---

# 147. Out-of-Domain Test

$$
x\notin D_\kappa.
$$

guard 應 fail。

---

# 148. Distribution Shift Protocol

每個 adaptive benchmark 可分：

### Phase 1

stable workload。

### Phase 2

shift。

### Phase 3

post-shift adaptation。

---

# 149. Shift Types

- sparsity；
- density；
- map；
- inventory；
- social relation；
- memory conflict；
- resource availability。

---

# 150. Adaptation Delay

定義：

$$
\boxed{
D_{\mathrm{adapt}}
=
t_{\mathrm{stable-new-policy}}
-
t_{\mathrm{shift}}.
}
$$

---

# 151. Lower Is Better

但不能犧牲 correctness。

---

# 152. Stale Window

$$
\boxed{
W_{\mathrm{stale}}
}
$$

是 shift 後舊 crystal 仍被錯用的時間。

---

# 153. Ideal

$$
W_{\mathrm{stale}}\rightarrow0.
$$

---

# 154. False Positive Invalidation

過度敏感也有成本。

---

# 155. Invalidation Precision

$$
\boxed{
P_I
=
\frac{\text{useful invalidations}}
{\text{all invalidations}}.
}
$$

---

# 156. Invalidation Recall

真的 stale 的 crystal 有多少被抓到。

---

# 157. Guard Quality

可以用：

- precision；
- recall；
- false accept；
- false reject。

---

# 158. Guard False Accept

最危險。

---

# 159. Guard False Reject

主要是 performance loss。

---

# 160. Promotion Stress Test

降低 promotion threshold，觀察：

$$
F_K
$$

如何上升。

---

# 161. Threshold Curve

得到：

$$
\boxed{
\text{utility vs false-crystal tradeoff}.
}
$$

---

# 162. Meta-Budget Stress Test

改：

$$
B_{\mathrm{meta}}.
$$

---

# 163. Too Low

adaptive layer 沒有搜索空間。

---

# 164. Too High

meta search 可能吃掉 gain。

---

# 165. Find Sweet Spot

不是越高越好。

---

# 166. Scale Stress Test

讓：

```text
COARSE
MESO
FINE
```

各自固定，再比較 adaptive。

---

# 167. Scale Regret

$$
\boxed{
Regret_\Sigma
=
J(\sigma_{\mathrm{chosen}})
-
J(\sigma_{\mathrm{best-known}}).
}
$$

---

# 168. Geometry Stress Test

line-only vs geometry-aware。

---

# 169. Config Stress Test

fixed S / J / P / R vs adaptive。

---

# 170. Crystal Maintenance Stress Test

增加 world drift rate。

---

# 171. Expected

drift 越高：

$$
C_{\mathrm{maintain}}
\uparrow.
$$

---

# 172. Crystal Utility Boundary

找：

$$
\lambda_{\mathrm{drift}}^\*
$$

使：

$$
U_\kappa=0.
$$

---

# 173. 這是重要實驗結果

告訴我們什麼世界不適合 crystallization。

---

# 174. Repetition Threshold

同樣找：

$$
N^\*
$$

使 build crystal 開始划算。

---

# 175. Break-Even

$$
\boxed{
C_{\mathrm{compile}}
+
N^\* C_{\mathrm{run}}
=
N^\* C_{\mathrm{original}}.
}
$$

---

# 176. This Is Lifecycle Reality

不是只看單次 fast path。

---

# 177. Benchmark Modes

### Performance Mode

主要看 cost。

### Correctness Mode

主要看 equivalence。

### Stress Mode

故意 shift / fault。

### Audit Mode

全 reopen / provenance。

---

# 178. Performance Mode

正常 workload。

---

# 179. Correctness Mode

增加 hidden obligations。

---

# 180. Stress Mode

增加 drift。

---

# 181. Audit Mode

驗 crystal source trace。

---

# 182. Fault Injection

Synthetic 可注入：

- stale dependency；
- invalid index；
- delayed event；
- incorrect parallel independence；
- missing provenance。

---

# 183. Adventure Land Faults

可用安全遊戲內變化：

- map variation；
- inventory mismatch；
- target gone；
- low HP；
- cooldown unavailable。

---

# 184. GA Faults

- contradictory memory；
- stale plan；
- changed relationship；
- new event；
- missing memory source。

---

# 185. Recovery Metric

$$
\boxed{
T_{\mathrm{recover}}.
}
$$

---

# 186. Recovery Correctness

是否回 canonical slow path。

---

# 187. Recovery Cost

$$
C_{\mathrm{recovery}}.
$$

---

# 188. No Catastrophic Shortcut

在 controlled benchmark 中，fast path failure 不應造成 unrecoverable experiment corruption。

---

# 189. Snapshot Before Risky Run

所有 stress run 先 snapshot。

---

# 190. Replay After Failure

驗：

- state；
- route；
- receipts；
- crystal lifecycle。

---

# 191. Experiment Receipt

每 run：

```text
ExperimentReceipt
- experiment_id
- benchmark_id
- group
- seed
- model_version
- runtime_version
- adapter_version
- world_revision
- initial_snapshot
- task
- route
- config_history
- scale_history
- crystal_hits
- crystal_promotions
- invalidations
- reopens
- cost_vector
- success
- failures
- validation
- final_state_digest
```

---

# 192. Canonical Serialization

UTF-8 JSON，stable key order。

---

# 193. Digest

$$
h=
\mathrm{SHA256}(\text{receipt}).
$$

---

# 194. Experiment Batch Manifest

記全部 receipt hashes。

---

# 195. Missing Data

不得 silently drop。

---

# 196. Null Semantics

```text
null = unknown / unavailable
```

不是 zero。

---

# 197. Failed Runs Included

失敗也是資料。

---

# 198. Outlier Handling

原始資料永遠保留。

---

# 199. Report Both Raw and Filtered

如果做 robust analysis。

---

# 200. No Cherry-Picking Seeds

seed list 在 run 前固定。

---

# 201. Pre-Registration Lite

至少先寫：

- benchmark；
- groups；
- primary metrics；
- success threshold；
- seed set。

---

# 202. Primary Success Criterion

第一版可用：

$$
\boxed{
\text{Correctness}_D
\ge
\text{Correctness}_A-\epsilon
}
$$

且：

$$
\boxed{
E[J_D]
<
E[J_A]-\delta.
}
$$

---

# 203. $\epsilon$

容許統計噪音，但不能掩蓋明顯 correctness decline。

---

# 204. $\delta$

minimum meaningful improvement。

---

# 205. 不預設 Universal $\delta$

依 benchmark。

---

# 206. Crystal Success Criterion

$$
G_{\mathrm{life}}>0
$$

且 false-crystal rate 在容許範圍。

---

# 207. Scale Success Criterion

adaptive scale 比 best fixed scale on average 更接近 held-out optimum，或明顯降低 worst-case cost。

---

# 208. Config Success Criterion

$$
Regret_C
$$

低於 fixed single-form baseline family。

---

# 209. Reopen Success Criterion

該 reopen 時能 reopen，且回復正確 slow path。

---

# 210. Safety Success Criterion

$$
N_{\mathrm{authorization\ violation}}=0.
$$

---

# 211. Falsification Criterion F1

若：

$$
J_D\ge J_A
$$

在所有 tested workload family 中穩定成立，full WRO meta layer 無工程價值。

---

# 212. F2

若 C 與 B 無差異：

$$
J_C\approx J_B
$$

且 crystal maintenance > 0，crystallization 無獨立收益。

---

# 213. F3

若 D 與 C 無差異：

$$
J_D\approx J_C,
$$

scale/config layer 無獨立收益。

---

# 214. F4

若 crystal false-accept rate 高，promotion theory 不成熟。

---

# 215. F5

若 reopen 經常失敗，earned primitive governance 不成立。

---

# 216. F6

若 line-only representation 在所有 benchmark 都同樣好，geometry layer 應縮減。

---

# 217. F7

若 fixed scale 永遠優於 adaptive，scale router 應縮減。

---

# 218. F8

若 S/J/P/R adaptive router 不能在 workload shift 中降低 regret，24／72 route grammar 的 runtime 作用需縮減。

---

# 219. Partial Success Is Valid

理論可能只在：

- repeated；
- semi-stable；
- heterogeneous；

world 有效。

---

# 220. Domain of Applicability

這本身就是重要結果。

---

# 221. Strongest Evidence Pattern

最有說服力不是 D 單次最快。

而是：

$$
\boxed{
C_D(t)
\downarrow
}
$$

隨 repeated experience，

同時：

$$
\boxed{
\theta_t
=
\theta_0.
}
$$

---

# 222. Why

這才直接支持 external structural adaptation。

---

# 223. Stronger Evidence

在 shift 後：

$$
C_D(t)
$$

先上升，再因 reopen / reroute 重新下降。

---

# 224. This Shows Adaptation, Not Memorized Benchmark

---

# 225. Strongest Crystal Evidence

same semantic family、held-out variants 上：

- crystal hit；
- guard valid；
- cost 下降；
- source available；
- shift 時安全 stale。

---

# 226. Anti-Evidence

exact same input cache hit 不足以支持 generalized path compilation。

---

# 227. Anti-Evidence 2

只少 model calls，但 game actions / work 不變，可能只是 planning compression。

---

# 228. Still Valuable, But Must Name Correctly

叫：

```text
reasoning compression
```

而不是：

```text
physical computation compression
```

---

# 229. Compression Vector Reporting

每 experiment 報：

$$
\Delta_{\mathrm{crystal}}
=
(
\Delta_{\mathrm{reason}},
\Delta_{\mathrm{route}},
\Delta_{\mathrm{depth}},
\Delta_{\mathrm{work}},
\Delta_{\mathrm{time}},
\Delta_{\mathrm{verify}}
).
$$

---

# 230. This Prevents Overclaiming

---

# 231. Benchmark Layering

順序應：

```text
Synthetic
→ Adventure Land
→ Generative Agents
→ Controlled Legacy Program
```

---

# 232. Why Synthetic First

最容易辨識 causal mechanism。

---

# 233. Why Adventure Land Second

real-time + repeated + replayable。

---

# 234. Why GA Third

semantic / memory / long horizon 更複雜。

---

# 235. Why Legacy Last

真軟體 dependency / side effect 更難。

---

# 236. Graduation Gate Synthetic → Game

至少：

- URR invariants pass；
- false crystal controlled；
- replay works；
- cost ledger valid。

---

# 237. Graduation Gate Game → GA

至少：

- stale / reopen works；
- route reuse gain；
- no major correctness decline。

---

# 238. Graduation Gate GA → Legacy

至少：

- source provenance；
- shadow mode；
- differential validation；
- safe rollback。

---

# 239. Phase B Paper 02 Deliverable

本文本身是 benchmark contract。

---

# 240. Phase B Paper 03 Input

下一篇 Minimal Sidecar Implementation Specification 需直接實作：

- experiment groups；
- receipts；
- adapters；
- metrics；
- crystal lifecycle；
- config / scale routers。

---

# 241. Phase B Paper 04 Input

formal verification targets 從：

- URR-1～16；
- promotion；
- invalidation；
- authority；
- replay；

提取 property tests / invariants。

---

# 242. First MVP Recommendation

先做：

$$
\boxed{
SW-01
\rightarrow
SW-04
\rightarrow
SW-07
\rightarrow
SW-08
\rightarrow
SW-10.
}
$$

---

# 243. Why These Five

覆蓋：

- sequential control；
- retrieval crystal；
- config shift；
- stale invalidation；
- wrapper illusion。

---

# 244. Then Adventure Land

先：

$$
AL-04
$$

full farm/restock/bank/return cycle。

---

# 245. Then GA

先：

$$
GA-02
$$

repeated memory query。

---

# 246. Minimal Model Use

Synthetic 可以完全不用 LLM。

---

# 247. Why

先證明 Runtime math / structure。

---

# 248. Then Add Frozen LLM

Adventure Land / GA。

---

# 249. This Separates Algorithmic from Model Effects

---

# 250. Core Benchmark Invariant B-1

所有比較必須使用相同 initial condition。

---

# 251. B-2

所有 adaptive gain 都必須計 meta cost。

---

# 252. B-3

所有 crystal gain 都必須計 compile / maintenance。

---

# 253. B-4

所有 fast path 都必須計 guard / validate。

---

# 254. B-5

unknown metric 不得當 zero。

---

# 255. B-6

failed runs 不得丟棄。

---

# 256. B-7

seed pairing 優先。

---

# 257. B-8

speedup claim 必須標 dimension。

---

# 258. B-9

crystal promotion 必須 held-out validation。

---

# 259. B-10

shift experiment 必須有 pre / post 明確界線。

---

# 260. B-11

authorization violation 為 hard failure。

---

# 261. B-12

world revision change 必須觸發相關 validity check。

---

# 262. B-13

reopen failure 必須顯式記錄。

---

# 263. B-14

full D 不得偷用 A/B/C 沒有的模型能力。

---

# 264. B-15

如果 adapter 不同，必須報 adapter cost。

---

# 265. B-16

任何「學會」主張都必須能指向 external structure delta。

---

# 266. External Structure Delta

例如：

```text
new crystal
new route
new config profile
new scale policy
new bridge
```

---

# 267. Model Delta Must Be Zero

$$
\Delta\theta=0.
$$

---

# 268. This Is the Falsifiable Core

---

# 結論

UNPNP-II 是否成立，不應由「概念是否漂亮」決定。

真正需要證明的是：

$$
\boxed{
\textbf{
在模型能力固定時，
多尺度 route、configuration routing 與 crystallization
是否能在明確 workload family 中，
穩定降低未來計算成本，
同時維持 correctness、replayability、reopenability 與 authority。
}
}
$$

本文因此建立：

$$
\boxed{
A=\text{Fixed},
\quad
B=\text{Adaptive Route},
\quad
C=\text{Crystallized},
\quad
D=\text{Full Multi-Scale}.
}
$$

並要求：

$$
\boxed{
\theta_A
=
\theta_B
=
\theta_C
=
\theta_D.
}
$$

若 D 在適合 workload 中真正有效，應看到的不只是單次 latency 下降，而是一組結構性訊號：

$$
R_{\mathrm{reason}}(t)\downarrow,
$$

$$
H_{\mathrm{corridor}}(t)\uparrow,
$$

$$
R_K(t)\uparrow,
$$

$$
Regret_C(t)\downarrow,
$$

$$
C_{\mathrm{avg}}(t)\downarrow,
$$

同時：

$$
F_K,
\quad
S_U,
\quad
N_{\mathrm{auth\ violation}}
$$

不得惡化。

如果做不到，理論就必須縮減。

如果只能在某些 repeated / semi-stable / heterogeneous worlds 做到，那麼其有效域就應被明確寫成那些 worlds，而不是宣稱 universal。

因此 Phase B 的第二個核心原則可以濃縮成：

$$
\boxed{
\textbf{
不是證明 UNPNP-II 一定有效，
而是建立一個讓它可以清楚失敗的實驗世界。
}
}
$$

只有在能夠失敗之後，它的成功才有研究意義。
