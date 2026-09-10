# UNPNP-II Phase B — Paper 04
## Formal Invariants and Verification Targets
### URR Runtime、Benchmark Protocol、Crystal Lifecycle 與 Sidecar 的形式化驗證目標

**系列：** UNPNP-II / Multi-Scale Computational Geometry — Phase B  
**篇次：** Phase B Paper 04 / 04  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-09  
**文件性質：** Formal Invariants／Property Testing／Model Checking Targets／Verification Handoff  
**前置：** Phase B Paper 01–03；UNPNP-II v0.1；UNPNP-I；MWT；GCM  
**狀態：** Canonical Draft

---

## 摘要

Phase B Paper 01 將 UNPNP-II 壓成 URR-v0.1 Reference Runtime，並提出 URR-1～URR-16；Paper 02 建立 A/B/C/D 實驗矩陣與 B-1～B-16 benchmark invariants；Paper 03 再把它們落成 Sidecar 工程規格、資料 schema、adapter contract、crystal lifecycle、A/B/C/D feature flags 與 Done Gate。

本文完成 Phase B 最後一步：

> **把這些 Runtime / Benchmark / Lifecycle 規則轉成可由測試框架、property testing、state-machine checking 與未來形式化工具直接接手的 Verification Targets。**

本文將驗證分成四層：

$$
\boxed{
\text{L1 Schema}
\rightarrow
\text{L2 Runtime Properties}
\rightarrow
\text{L3 State-Machine Invariants}
\rightarrow
\text{L4 Formal Models}.
}
$$

L1 使用 type / schema / deterministic serialization / receipt hashing；  
L2 使用 pytest、Hypothesis、differential tests、replay tests、fault injection；  
L3 使用 lifecycle、authority、group isolation、invalidation propagation 等 state-machine property；  
L4 留給 TLA+、Alloy、Lean、Coq、SMT 或 explicit-state model checking。

Phase B 的 final gate 不要求「證明整個 WRO 理論」，而要求：

> **任何 implementation 若自稱 URR-v0.1 conformant，至少不能違反這些可機器檢查的核心 invariants。**

---

# 1. Verification Scope

本文驗證：

- URR object consistency；
- route legality；
- authority preservation；
- cost accounting；
- crystal lifecycle；
- invalidation / reopen；
- A/B/C/D isolation；
- frozen-model integrity；
- experiment receipts；
- replayability。

本文不宣稱形式化證明：

- MWT World ontology；
- GCM 完備性；
- 24／72 完備性；
- WRO global optimum 必然存在；
- universal crystal compiler；
- P/NP 結論。

---

# 2. Verification Layers

## L1 — Schema

所有 canonical runtime object 必須：

```text
serializable
versioned
id-bearing
null-explicit
enum-stable
```

核心規則：

$$
\boxed{
\text{Unknown}\neq0.
}
$$

unknown 應序列化成 `null` 或 typed `UNKNOWN`，不可偷轉成 0。

Canonical JSON 必須：

```text
UTF-8
sorted keys
no NaN/Infinity
stable enum strings
explicit null
```

同一 receipt 應滿足：

$$
S_1(x)=S_2(x)
$$

以及：

$$
H(S_1(x))=H(S_2(x)).
$$

Hypothesis target：

```python
@given(valid_receipts())
def test_receipt_hash_stable(receipt):
    assert canonical_hash(receipt) == canonical_hash(receipt)
```

---

# 3. URR-1 — World Primitive 與 Runtime State 分離

$$
\boxed{
\mathbf W\neq\mathfrak R_t.
}
$$

工程上要求 `WorldRecord`、`RuntimeState`、`ChartRecord`、`RouteRecord` 為不同 type；任何 Runtime tuple 都不得被命名或序列化成 MWT World primitive。

---

# 4. URR-2 — Computation / Observation / Materialization 分離

$$
\boxed{
\text{Computation}
\neq
\text{Observation}
\neq
\text{Materialization}.
}
$$

基本 property：

```python
before = await adapter.snapshot()
_ = await adapter.observe(task)
after = await adapter.snapshot()
assert equivalent(before, after)
```

若 target 的 observation 本身有 side effect，adapter 必須顯式宣告。

---

# 5. URR-3 — Finite Active Frontier

$$
\boxed{
|F_t|<\infty.
}
$$

```python
assert len(runtime.frontier.entries) <= settings.max_active_frontier
```

理論上可無界 refinement，不代表 Runtime 無界 materialization。

---

# 6. URR-4 — Unbounded Refinement ≠ Full Expansion

存在 inactive lower-scale worlds 時，Runtime 不得因其「存在」就全部 materialize。

驗證：

```text
registered refinement depth > active refinement depth
```

仍為合法狀態。

---

# 7. URR-5 — Active Route 必須落在 Safe Feasible Space

$$
\boxed{
\mathcal R\subseteq Z_t^{\mathrm{safe}}.
}
$$

每個 route segment 至少必須：

```text
reachable
authorized
guard-valid
resource-feasible
risk-valid
```

---

# 8. URR-6 — Reachable ≠ Authorized

$$
\boxed{
\text{Reachable}\neq\text{Authorized}.
}
$$

Negative test：

```text
reachable = true
authorized = false
```

必須產生：

```text
AUTH_DENIED
```

而不是執行。

---

# 9. URR-7 — One Call ≠ One Computational Transition

$$
\boxed{
\text{one call}
\neq
\text{one computational transition}.
}
$$

Wrapper illusion property：

```python
baseline = run_raw_steps(10)
wrapped = run_wrapper(10)

assert wrapped.cost.hops < baseline.cost.hops
assert wrapped.cost.work == baseline.cost.work
assert wrapped.cost.causal_depth == baseline.cost.causal_depth
```

如果只 hop 下降，禁止宣稱 work-speedup 或 causal-speedup。

---

# 10. URR-8 — Speedup 必須標示維度

合法：

```text
HOP
WORK
DEPTH
LATENCY
MATERIALIZATION
VERIFICATION
LIFECYCLE
```

非法：

```text
speedup = 2.0
speedup_kind = null
```

---

# 11. URR-9 — Same Endpoint ≠ Same History

$$
\boxed{
s_f^A=s_f^B
\not\Rightarrow
\mathcal H_A=\mathcal H_B.
}
$$

兩 route final state digest 相同但 history digest 不同時，只能標 endpoint-equivalent，不能自動升格成 full-route-equivalent。

---

# 12. URR-10 — Path Compilation 不能只是 Wrapper

Path Compilation candidate 至少需顯示一項 structural gain：

$$
\Delta_{\mathrm{top}}>0
$$

或：

$$
\Delta_{\mathrm{causal}}>0
$$

或：

$$
\Delta_{\mathrm{work}}>0
$$

或明確的 reasoning / verification / materialization reduction。

若：

```text
same route
same work
same depth
same materialization
same runtime
only interface changed
```

則標：

```text
WRAPPER_ONLY
```

不是 compiled computational shortcut。

---

# 13. URR-11 — Compiled ≠ Crystallized

$$
\boxed{
\text{Compiled}\neq\text{Crystallized}.
}
$$

禁止：

```text
CANDIDATE → HOT
```

預設合法路徑：

```text
CANDIDATE → COLD → WARM → HOT
```

Property：

```python
with pytest.raises(InvalidLifecycleTransition):
    transition(CANDIDATE, HOT)
```

---

# 14. URR-12 — Crystal Authority 不得大於 Source Authority

$$
\boxed{
Auth(\kappa)\subseteq Auth(source).
}
$$

若 source 只有 READ，crystal 不得出現 WRITE。

對 composite crystal，v0.1 採保守規則：

$$
Auth(\kappa)
\subseteq
\bigcap_i Auth(source_i).
$$

---

# 15. URR-13 — Promoted Crystal Record 完整性

任何 COLD/WARM/HOT crystal 必須有：

```text
valid_domain
guard
validator
provenance
lifecycle
resource_envelope
source_route
```

缺任一核心欄位，不得 promotion。

---

# 16. URR-14 — Reopenability

每個 promoted crystal 必須：

```text
reopen_pointer != null
```

或：

```text
irreversible = true
reopen_loss_declared = true
```

非法：

```text
reopen_pointer = null
irreversible = false
```

---

# 17. URR-15 — Switch Cost 不得隱形

scale / config / geometry / observer switch 均必須有 cost record。

即使實測為 0，也必須記：

```text
value = 0
metric_kind = EXACT | ESTIMATED
```

而不是 missing。

---

# 18. URR-16 — Frozen-Model Integrity

$$
\boxed{
\theta_A=\theta_B=\theta_C=\theta_D.
}
$$

對 paired receipt：

```python
hashes = {r.model_signature_hash for r in pair}
assert len(hashes) == 1
```

不一致時：

```text
INVALID_FOR_FROZEN_COMPARISON
```

---

# 19. B-1 ～ B-16 Benchmark Conformance

## B-1 Same Initial Condition

```python
assert len({r.initial_snapshot_digest for r in pair}) == 1
```

## B-2 Meta Cost Counted

B/C/D：

```text
cost.meta != null
```

## B-3 Crystal Lifecycle Cost Counted

$$
C_{\mathrm{life}}
=
C_{\mathrm{compile}}
+
C_{\mathrm{run}}
+
C_{\mathrm{maintain}}
+
C_{\mathrm{reopen}}.
$$

## B-4 Fast Path Counts Guard + Validation

不得把 fast path guard / cheap validator 當免費。

## B-5 Unknown ≠ Zero

```python
assert metric.kind == "UNKNOWN"
assert metric.value is None
```

## B-6 Failed Runs Retained

$$
N_{\mathrm{receipts}}
=
N_{\mathrm{attempted\ runs}}.
$$

## B-7 Seed Pairing

同 `benchmark_id + seed` 需有 protocol 指定全部 groups。

## B-8 Speedup Dimension Required

同 URR-8。

## B-9 Held-Out Promotion

HOT 前：

```text
held_out_successes >= threshold
```

## B-10 Shift Boundary Explicit

```text
shift_epoch != null
```

## B-11 Authorization Violation Hard Failure

$$
N_{\mathrm{auth\ violation}}=0.
$$

## B-12 World Revision Triggers Validity Check

dependency-relevant world revision 改變後，affected crystal 不得繼續無條件 HOT。

## B-13 Reopen Failure Observable

必須 append：

```text
REOPEN_FAILED
```

## B-14 D 不得偷用更強模型

同 URR-16。

## B-15 Adapter Cost Reported

adapter 差異成本需顯式 report。

## B-16 Structural Learning Must Point to External Delta

合法 structural delta：

```text
ROUTE_COMPILED
CRYSTAL_PROMOTED
CONFIG_PROFILE_UPDATE
SCALE_PROFILE_UPDATE
BRIDGE_ADDED
ATLAS_UPDATED
```

如果 claimed structural learning 但 ledger 沒 structural event，claim invalid。

---

# 20. Crystal Lifecycle State Machine

狀態：

$$
Q_K
=
\{
CANDIDATE,
COLD,
WARM,
HOT,
STALE,
RETIRED
\}.
$$

預設 allowed transitions：

```text
CANDIDATE → COLD
COLD → WARM
WARM → HOT

COLD → STALE
WARM → STALE
HOT → STALE

STALE → COLD
STALE → RETIRED

CANDIDATE → RETIRED
COLD → RETIRED
WARM → RETIRED
HOT → RETIRED
```

v0.1 不允許：

```text
STALE → HOT
```

直接回升。

Fast invoke 只允許：

```text
WARM
HOT
```

且還必須同時：

$$
GuardValid
\land
AuthorityValid
\land
WorldCompatible.
$$

---

# 21. Invalidation Propagation

若：

$$
\kappa_c\in Deps(\kappa_p)
$$

且 child stale，則 parent 必須獲得 revalidation obligation：

$$
\boxed{
STALE(\kappa_c)
\Rightarrow
NeedsRevalidation(\kappa_p).
}
$$

禁止 silent parent HOT。

---

# 22. Reopen State Machine

$$
Q_R
=
\{
CLOSED,
REOPENING,
OPEN,
FAILED
\}.
$$

若 source 存在且 adapter 支援所需 replay level：

```text
REOPENING → OPEN
```

若 source 不存在：

```text
REOPENING → FAILED
```

並產生 structured failure receipt。

---

# 23. Scale State Machine

$$
Q_\Sigma
=
\{
COARSE,
MESO,
FINE
\}.
$$

預設：

```text
COARSE ↔ MESO ↔ FINE
```

若允許：

```text
COARSE → FINE
```

direct jump，則必須標 stronger cross-scale validation。

---

# 24. Scale Thrashing

在 window $w$ 內，如果 coarse/fine reversal 超過 threshold：

```text
SCALE_THRASHING
```

需被記錄。

這是 performance / policy warning，不一定是 correctness failure。

---

# 25. Configuration State Machine

v0.1：

$$
Q_C
=
\{S,J,P,R\}.
$$

若：

$$
c_i\neq c_j,
$$

必須存在：

```text
bridge_id
```

或：

```text
bridge_kind = IDENTITY_VALIDATED
```

---

# 26. S → P Safety Property

只有 independence / synchronization obligation 已驗證，才可：

$$
S\rightarrow P.
$$

Hidden dependency test：

```text
a3 → a7
```

若 router 仍標所有 task fully independent，驗證失敗。

---

# 27. R → S Fallback

Recognition fast path guard fail / stale 時：

$$
R\rightarrow S
$$

canonical fallback 應合法。

---

# 28. Group Isolation

A/B/C/D 各自有獨立 adaptive namespace：

$$
N_A,N_B,N_C,N_D.
$$

對：

$$
i\neq j
$$

要求 adaptive store 不互相讀寫。

可共享的只有：

- model signature；
- initial snapshot；
- benchmark spec；
- read-only external data。

Crystal store、route profile、config profile、scale profile 必須 group-isolated。

---

# 29. Replay Invariants

Replay receipt 至少需要：

```text
world_snapshot
runtime_version
adapter_version
model_signature
route
config_history
scale_history
crystal_ids
seed
```

Replay levels：

```text
SEMANTIC
STATE
ROUTE
TIMING
EXACT
```

claim 不得超過 adapter capability。

---

# 30. Cost Ledger Invariants

每個 metric 具有：

```text
value
kind = EXACT | PROXY | ESTIMATED | UNKNOWN
```

Aggregation 不可一律 sum。

建議：

$$
W=\sum_iW_i.
$$

因果深度由 dependency graph longest path；

wall time 用 measured elapsed；

risk 採 policy-specific aggregation；

observation loss 採 bridge-specific aggregation。

核心規則：

$$
\boxed{
Unknown+x=Unknown
}
$$

對不可推導 metric，而不是偷變成 $x$。

---

# 31. Crystal Utility Gate

$$
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
$$

若：

$$
U_\kappa\le0,
$$

不得升 HOT。

注意：這是 v0.1 promotion policy target，不是普世數學定理。

---

# 32. Guard False Accept / False Reject

False Accept：

> guard pass，但 crystal semantics fail。

這是 correctness failure，通常應立即 stale。

False Reject：

> guard fail，但 crystal 其實可用。

主要是 performance loss。

兩者不可混為同一錯誤率。

---

# 33. Differential Validation

若 canonical route 可執行：

$$
Result(\kappa)
\simeq_q
Result(\Gamma_{\mathrm{canonical}}).
$$

對 benchmark-defined relevant invariants：

$$
I_q.
$$

Exact：

$$
I_q(s_f^\kappa)=I_q(s_f^{\mathrm{canonical}}).
$$

Approximate：

$$
d(
I_q(s_f^\kappa),
I_q(s_f^{\mathrm{canonical}})
)
\le
\epsilon_q.
$$

---

# 34. History-Sensitive Validation

如果 task 定義：

```text
required_events
forbidden_events
ordering_constraints
```

即使 endpoint 相同，也必須驗 history obligations。

---

# 35. Hypothesis vs Invariant

這是 Phase B 最重要的方法學界線之一。

## Invariant

違反代表 implementation 不 conform。

例如：

- unauthorized execution；
- stale fast invoke；
- unknown → zero；
- failed run dropped。

## Hypothesis

可以在實驗中失敗。

例如：

$$
E[J_D]<E[J_A],
$$

$$
R_K(t)\uparrow,
$$

$$
Regret_C(t)\downarrow.
$$

不得把 performance hypothesis 寫成 unit-test success condition。

---

# 36. Benchmark Conformance ≠ Theory Success

一個 URR implementation 可以 100% conform，但 D 組完全沒有 performance gain。

這仍是一個有效科學結果。

---

# 37. Formal Model Target 1 — Crystal Lifecycle

適合 TLA+ / Alloy。

Safety：

$$
\boxed{
state\notin\{WARM,HOT\}
\Rightarrow
\neg FastInvoke.
}
$$

Safety 2：

$$
\boxed{
FastInvoke
\Rightarrow
GuardValid
\land
AuthorityValid
\land
WorldCompatible.
}
$$

Liveness candidate：

若 STALE 且 source available，在公平條件下 eventually：

```text
revalidated
or retired
```

---

# 38. Formal Model Target 2 — Authority

適合 Alloy / SMT / Lean。

$$
\boxed{
Auth(\kappa)\subseteq Auth(source).
}
$$

Composite：

$$
Auth(\kappa)
\subseteq
\bigcap_iAuth(source_i).
$$

---

# 39. Formal Model Target 3 — Commit Protocol

State-changing action：

```text
PLAN
→ AUTHORIZE
→ EXECUTE
→ VALIDATE
→ COMMIT
```

Safety：

$$
\boxed{
ValidationFail
\Rightarrow
\neg CleanCommit.
}
$$

若 target 不可 rollback，也必須留下：

```text
COMMIT_FAILED_WITH_SIDE_EFFECT
```

而非 clean success。

---

# 40. Formal Model Target 4 — Group Isolation

對 adaptive stores：

$$
i\neq j
\Rightarrow
Write(N_i)\cap ReadWrite(N_j)=\varnothing.
$$

---

# 41. Formal Model Target 5 — Frozen Model

paired experiment receipts 的 model signature 必須相同。

---

# 42. Formal Model Target 6 — Bounded Frontier

$$
|F_t|\le B_F.
$$

可 model-check bounded toy model。

---

# 43. Formal Model Target 7 — Invalidation Propagation

dependency DAG 中 stale child 必須產生 parent revalidation obligation。

---

# 44. Formal Model Target 8 — Receipt Evidence Chain

receipt parent hash chain 不得無故斷裂。

---

# 45. Formal Model Target 9 — No Silent Failure

每個：

- authorization denial；
- validation failure；
- reopen failure；
- adapter failure；

最終必須 append structured event。

---

# 46. Formal Model Target 10 — Revealed-Set Optimality

對有限：

$$
\widehat{\mathfrak F}_t
$$

可用 SMT 驗：

$$
J(x^\*)\le J(x_i)
$$

對所有 revealed candidate。

這只能宣稱：

```text
best-known in revealed candidate set
```

不能宣稱 omniscient global optimum。

---

# 47. Lean Target — Typed Unknown Metric

可定義：

$$
Metric(\alpha)
=
Known(\alpha)
\mid
Unknown.
$$

加法：

$$
Known(a)+Known(b)=Known(a+b),
$$

$$
Unknown+x=Unknown.
$$

這可從 type level 防止 unknown 被默認 0。

---

# 48. Lean Target — PromotedCrystal Constructor

讓 promoted crystal type constructor 強制要求：

```text
valid_domain
guard
validator
provenance
reopenability declaration
```

比 runtime null check 更強。

---

# 49. Lean Target — Route Equivalence Levels

明確區分：

```text
EndpointEquivalent
TaskEquivalent
HistoryEquivalent
FullRouteEquivalent
```

禁止 endpoint equivalence 自動 coercion 成 full route equivalence。

---

# 50. Suggested TLA+ Modules

```text
CrystalLifecycle.tla
RuntimeCommit.tla
Authority.tla
GroupIsolation.tla
Invalidation.tla
```

Suggested Lean：

```text
Metric.lean
Authority.lean
Lifecycle.lean
RouteEquivalence.lean
CrystalRecord.lean
```

Suggested Hypothesis：

```text
test_prop_cost.py
test_prop_lifecycle.py
test_prop_authority.py
test_prop_invalidation.py
test_prop_receipts.py
test_prop_isolation.py
```

---

# 51. Fault Injection Matrix

| Fault | Expected behavior |
|---|---|
| WORLD_DRIFT | affected crystal stale / revalidate |
| POLICY_DRIFT | authority recheck |
| GUARD_BUG | differential validator catches false accept where possible |
| INVALID_INDEX | J/R shortcut validation failure |
| MISSING_PROVENANCE | promotion reject or audit fail |
| REOPEN_SOURCE_MISSING | REOPEN_FAILED |
| HIDDEN_DEPENDENCY | S→P blocked or validator fail |
| ADAPTER_FAILURE | structured error receipt |

---

# 52. Sidecar Done Gate → DG-1 ～ DG-16

## DG-1
Install succeeds.

## DG-2
Unit tests pass.

## DG-3
URR-1～16 pass.

## DG-4
B-1～16 benchmark conformance pass.

## DG-5
SW-01 / SW-04 / SW-07 / SW-08 / SW-10 runnable.

## DG-6
A/B/C/D isolation pass.

## DG-7
Frozen-model signature gate pass.

## DG-8
Crystal stale / reopen pass.

## DG-9
Wrapper illusion test pass.

## DG-10
Config switch cost recorded.

## DG-11
Meta cost recorded.

## DG-12
Receipt hash reproducible.

## DG-13
Authorization hard-fail pass.

## DG-14
Failed runs retained.

## DG-15
Unknown metrics remain unknown.

## DG-16
Canonical fallback works.

---

# 53. Conformance Levels

建議：

### URR-C0 — Schema
資料模型可互通。

### URR-C1 — Runtime
URR 核心 invariants pass。

### URR-C2 — Structural Adaptation
Crystal lifecycle + replay + reopen。

### URR-C3 — Benchmark
A/B/C/D conformance。

### URR-C4 — Formalized Core
核心 state-machine 有 TLA+ / Lean / Alloy / SMT 等部分形式化證據。

重要：

$$
\boxed{
\text{Conformant}
\neq
\text{Faster}.
}
$$

Performance 仍是實驗結果。

---

# 54. Release Verification Artifacts

每個 URR release 建議輸出：

```text
TEST_REPORT.md
INVARIANT_REPORT.json
BENCHMARK_CONFORMANCE.json
SCHEMA_HASHES.json
RUNTIME_VERSION.json
```

若有形式化：

```text
tla/
lean/
alloy/
smt/
```

---

# 55. Clean Replay Gate

Release 前至少：

1. 空 DB；
2. 載入 canonical receipts；
3. 重建必要 runtime indices；
4. 重播指定 Synthetic benchmark；
5. final state / semantic result 符合 declared replay level。

這可防止 hidden local cache 讓「重現」看起來成功。

---

# 56. Reproducible Package

release package 應包含：

- source；
- dependency lock；
- benchmark manifests；
- seed list；
- schema version；
- runtime version；
- theory version；
- SHA-256。

---

# 57. Verification Before Claim

tests green 但：

- cost receipts 缺失；
- failed runs 被丟棄；
- model signature 不固定；

都不能宣稱 Phase B benchmark complete。

同樣，部分 TLA+ / Lean 證明不能被擴張成：

> 「UNPNP-II 已被數學證明。」

合法說法應是：

> 「URR-12 authority monotonicity 已在 model X 中形式驗證。」

---

# 58. Runtime Safety Kernel — First Formalization Batch

最優先五條：

1. no unauthorized execution；
2. stale crystal cannot fast execute；
3. no direct candidate → HOT；
4. crystal authority cannot exceed source；
5. validation failure cannot become clean commit。

它們小、清楚、高價值，最適合先 model check。

---

# 59. Second Formalization Batch

6. unknown ≠ zero；
7. A/B/C/D group isolation；
8. frozen model equality；
9. invalidation propagation；
10. reopen failure observability。

---

# 60. Third Formalization Batch

11. bounded active frontier；
12. scale transition constraints；
13. configuration bridge constraints；
14. route equivalence levels；
15. receipt hash chain；
16. revealed-set optimality。

---

# 61. Canonical Development Order

建議 implementation workflow：

```text
Schema RED/GREEN
→ Ledger RED/GREEN
→ URR invariant suite
→ Synthetic adapter
→ A/B
→ Path compiler
→ Crystal C
→ Scale/Config D
→ Benchmark matrix
→ TLA+/Lean subset
```

---

# 62. Theory / Runtime Conflict Rule

如果 implementation 與 Paper 03 / 04 衝突：

1. 先判斷 implementation bug；
2. 如果規格本身不可行，再 revision theory paper；
3. 禁止 silent semantic mutation。

Theory revision：

```text
Phase B Paper 04 v0.2
```

Runtime revision：

```text
URR v0.2
```

Benchmark receipt 必須綁：

```text
theory_version
runtime_version
benchmark_version
```

---

# 63. Phase B Final Core Laws

$$
\boxed{
\textbf{
An optimization that cannot be measured is not a validated optimization.
}
}
$$

$$
\boxed{
\textbf{
A fast path that cannot be invalidated is not a safe crystal.
}
}
$$

$$
\boxed{
\textbf{
A primitive that cannot expose its provenance is not an auditable earned primitive.
}
}
$$

$$
\boxed{
\textbf{
A benchmark that changes the model while claiming architecture gain is invalid for frozen-model comparison.
}
}
$$

$$
\boxed{
\textbf{
A runtime theory becomes experimentally meaningful only when its failure conditions are machine-checkable.
}
}
$$

---

# 64. Phase B Final Closure

Phase B 四篇形成：

$$
\boxed{
\text{Formal Runtime}
\rightarrow
\text{Benchmark Protocol}
\rightarrow
\text{Implementation Spec}
\rightarrow
\text{Verification Targets}.
}
$$

Paper 01 回答：

> Runtime 最小物件與狀態是什麼？

Paper 02 回答：

> 怎麼公平比較？

Paper 03 回答：

> 怎麼實作？

Paper 04 回答：

> 怎麼知道實作沒有偷偷破壞理論邊界？

最終：

$$
\boxed{
\text{URR-v0.1}
=
\text{State}
+
\text{Receipts}
+
\text{Invariants}
+
\text{Benchmarks}
+
\text{Replay}.
}
$$

---

# 結論

UNPNP-II 的理論核心可以很大：

- World；
- Atlas；
- Geometry；
- Scale；
- 24／72；
- Route；
- Crystal；
- World-Relative Optimization。

但真正進入工程後，首先需要的不是更大的 optimizer，而是一個小而嚴格的 correctness kernel。

這個 kernel 必須知道：

$$
\boxed{
\text{Unknown}\neq0,
}
$$

$$
\boxed{
\text{Reachable}\neq\text{Authorized},
}
$$

$$
\boxed{
\text{Compiled}\neq\text{Crystallized},
}
$$

$$
\boxed{
\text{Same Endpoint}\not\Rightarrow\text{Same History},
}
$$

以及：

$$
\boxed{
\text{One Call}\neq\text{One Computation}.
}
$$

因此 Phase B 最後的核心不是：

> 證明 UNPNP-II 一定能加速所有世界。

而是：

$$
\boxed{
\textbf{
建立一套讓任何自稱 UNPNP-II Runtime 的實作，
都必須先通過的可機器檢查邊界。
}
}
$$

如果 implementation 通過所有 invariants，但 benchmark 顯示沒有 performance gain，那仍是一個成功的科學結果：

> **這表示理論在該 workload 上沒有收益，而不是實驗失敗。**

這正是整個 Phase B 最重要的收束：

$$
\boxed{
\textbf{
先讓系統有資格失敗，
再討論它是否真的成功。
}
}
$$
