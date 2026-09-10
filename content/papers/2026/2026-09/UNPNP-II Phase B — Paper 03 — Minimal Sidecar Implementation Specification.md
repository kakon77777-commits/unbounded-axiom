# UNPNP-II Phase B — Paper 03
## Minimal Sidecar Implementation Specification
### URR-v0.1 的最小可實作架構、資料模型、Adapter Contract 與實驗開關

**系列：** UNPNP-II / Multi-Scale Computational Geometry — Phase B  
**篇次：** Phase B Paper 03  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-09  
**文件性質：** Engineering Specification／Sidecar Runtime／Implementation Contract  
**前置：** Phase B Paper 01《Formal Core and Reference Runtime》；Phase B Paper 02《Experimental Protocol and Benchmark Matrix》  
**狀態：** Canonical Draft

---

## 摘要

Phase B Paper 01 已將 UNPNP-II 理論壓成 URR-v0.1 Reference Runtime；Paper 02 已固定 A/B/C/D 四組實驗、Synthetic / Adventure Land / Generative Agents 三類 benchmark，以及 frozen-model、paired-seed、cost-ledger、crystal promotion / invalidation / reopen 等實驗協議。

本文的任務只有一個：

> **把這套 Reference Runtime 縮成可以直接交給本地端 AI / Codex 實作的最小 Sidecar。**

本文明確採：

$$
\boxed{
\text{Target System}
\leftrightarrow
\text{Thin Adapter}
\leftrightarrow
\text{UNPNP-II Sidecar Runtime}
}
$$

而不是：

> 把 UNPNP-II 全部重寫進遊戲、Agent Framework 或 Legacy Program 的 core。

其工程原則是：

$$
\boxed{
\text{Minimal Hooks}
+
\text{Explicit State}
+
\text{Append-Only Receipts}
+
\text{Measured Adaptation}
+
\text{Safe Fallback}.
}
$$

URR Sidecar v0.1 的最小核心模組為：

```text
urr/
  world/
  atlas/
  frontier/
  config/
  route/
  execute/
  validate/
  compile/
  crystal/
  governance/
  ledger/
  replay/
  experiment/
  adapters/
```

所有 target adapter 只需要提供最小 contract：

```text
observe()
snapshot()
restore()
execute()
validate()
```

Sidecar 自己負責：

- world revision；
- chart / scale metadata；
- S/J/P/R configuration profile；
- route candidate；
- cost vector；
- compiled-path candidate；
- crystal lifecycle；
- guard；
- invalidation；
- reopen；
- A/B/C/D feature switch；
- replay / experiment receipt。

本文給出：

1. repo layout；
2. Python-first reference package；
3. canonical JSON schemas；
4. SQLite / JSONL storage；
5. core interfaces；
6. event and receipt format；
7. runtime loop pseudocode；
8. crystal state machine；
9. scale / config switch；
10. experiment feature flags；
11. Synthetic adapter；
12. Adventure Land adapter；
13. Generative Agents adapter；
14. implementation order；
15. acceptance tests；
16. v0.1 completion gate。

---

# 1. 實作目標

URR-v0.1 不是 production product。

第一階段唯一目標：

$$
\boxed{
\text{讓 Phase B Paper 02 的 benchmark 能被公平執行。}
}
$$

---

# 2. 非目標

v0.1 不需要：

- 完整 WRO global optimizer；
- 全 24 / 72 runtime；
- quantum backend；
- graph database；
- distributed consensus；
- autonomous external action framework；
- general AGI planner；
- GUI；
- cloud deployment。

---

# 3. Reference Language

建議 reference implementation：

```text
Python 3.12+
```

原因：

- 快速實驗；
- dataclass / pydantic 方便；
- SQLite 內建；
- pytest / hypothesis；
- 適合 Synthetic / Agent adapter；
- 容易讓本地 AI 修改。

---

# 4. Target Language Independence

理論與 schema 不綁 Python。

Adventure Land adapter 可使用：

```text
JavaScript / TypeScript
```

透過：

- JSONL；
- local HTTP；
- WebSocket；

接 Sidecar。

---

# 5. Deployment Topology

最小：

```text
┌──────────────────────┐
│ Target Runtime       │
│ Game / Agent / App   │
└──────────┬───────────┘
           │ Thin Adapter
           ▼
┌──────────────────────┐
│ URR Sidecar           │
│ localhost / in-proc   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ SQLite + JSONL Ledger │
└──────────────────────┘
```

---

# 6. Sidecar 不持有 Target 的完整控制權

adapter 明確限制：

```text
observable_state
allowed_actions
reversible_actions
high_risk_actions
```

---

# 7. Canonical Repo Layout

```text
unpnpii-urr/
├─ README.md
├─ pyproject.toml
├─ LICENSE
├─ docs/
│  ├─ architecture.md
│  ├─ schemas.md
│  ├─ experiments.md
│  └─ adapters.md
├─ src/
│  └─ urr/
│     ├─ __init__.py
│     ├─ types.py
│     ├─ errors.py
│     ├─ runtime.py
│     ├─ settings.py
│     ├─ world/
│     │  ├─ model.py
│     │  ├─ registry.py
│     │  └─ revision.py
│     ├─ atlas/
│     │  ├─ model.py
│     │  └─ registry.py
│     ├─ frontier/
│     │  ├─ model.py
│     │  └─ manager.py
│     ├─ config/
│     │  ├─ model.py
│     │  ├─ router.py
│     │  └─ profiles.py
│     ├─ route/
│     │  ├─ model.py
│     │  ├─ candidate.py
│     │  ├─ selector.py
│     │  └─ cost.py
│     ├─ execute/
│     │  └─ executor.py
│     ├─ validate/
│     │  ├─ validators.py
│     │  └─ maturity.py
│     ├─ compile/
│     │  ├─ compiler.py
│     │  └─ candidate.py
│     ├─ crystal/
│     │  ├─ model.py
│     │  ├─ store.py
│     │  ├─ lifecycle.py
│     │  └─ invalidation.py
│     ├─ governance/
│     │  ├─ model.py
│     │  └─ gate.py
│     ├─ ledger/
│     │  ├─ sqlite.py
│     │  ├─ jsonl.py
│     │  ├─ events.py
│     │  └─ receipts.py
│     ├─ replay/
│     │  └─ harness.py
│     ├─ experiment/
│     │  ├─ groups.py
│     │  ├─ runner.py
│     │  ├─ metrics.py
│     │  └─ manifest.py
│     └─ adapters/
│        ├─ base.py
│        ├─ synthetic.py
│        ├─ adventureland.py
│        └─ generative_agents.py
├─ tests/
│  ├─ unit/
│  ├─ invariants/
│  ├─ integration/
│  └─ experiments/
└─ examples/
   ├─ synthetic/
   ├─ adventureland/
   └─ generative_agents/
```

---

# 8. 核心物件原則

所有主要 runtime object：

```text
must have id
must have version/revision
must be serializable
must have explicit unknown/null
```

---

# 9. 禁止 Hidden Mutable Global State

Sidecar 重要 state 必須能從：

```text
SQLite + event ledger
```

重建。

---

# 10. Base ID Type

建議：

```python
str  # UUIDv7 or UUID4
```

---

# 11. Epoch Type

```python
int
```

單調增加。

---

# 12. World Revision

```python
str
```

每次 target state validity-relevant change 更新。

---

# 13. Core Enum — Scale

```python
class Scale(str, Enum):
    COARSE = "COARSE"
    MESO = "MESO"
    FINE = "FINE"
```

---

# 14. Core Enum — Geometry

```python
class Geometry(str, Enum):
    POINT = "POINT"
    LINE = "LINE"
    JUMP_LINE = "JUMP_LINE"
    SURFACE = "SURFACE"
    CLUSTER = "CLUSTER"
    FIELD = "FIELD"
    RECURSIVE = "RECURSIVE"
    UNKNOWN = "UNKNOWN"
```

---

# 15. Core Enum — Update Form

v0.1 MVP：

```python
class UpdateForm(str, Enum):
    S = "S"
    J = "J"
    P = "P"
    R = "R"
```

---

# 16. Full 24 Compatibility

schema 仍預留：

```text
substrate = C | D
observation = C | D | X
```

---

# 17. Transition Law

```python
class TransitionLaw(str, Enum):
    F = "F"
    K = "K"
    Q = "Q"
```

v0.1 預設只啟用：

```text
F
```

---

# 18. Crystal Lifecycle

```python
class CrystalState(str, Enum):
    CANDIDATE = "CANDIDATE"
    COLD = "COLD"
    WARM = "WARM"
    HOT = "HOT"
    STALE = "STALE"
    RETIRED = "RETIRED"
```

---

# 19. Validation Maturity

```python
class ValidationKind(str, Enum):
    NONE = "NONE"
    SMOKE = "SMOKE"
    REPLAY = "REPLAY"
    PROPERTY = "PROPERTY"
    DIFFERENTIAL = "DIFFERENTIAL"
    FORMAL = "FORMAL"
```

---

# 20. Experiment Group

```python
class ExperimentGroup(str, Enum):
    A_FIXED = "A_FIXED"
    B_ADAPTIVE_ROUTE = "B_ADAPTIVE_ROUTE"
    C_CRYSTALLIZED = "C_CRYSTALLIZED"
    D_FULL_MULTISCALE = "D_FULL_MULTISCALE"
```

---

# 21. Cost Vector

最小 dataclass：

```python
@dataclass
class CostVector:
    hops: float | None
    work: float | None
    causal_depth: float | None
    wall_time_ms: float | None
    materialization: float | None
    verification: float | None
    risk: float | None
    meta: float | None
    switch: float | None
    maintenance: float | None
    observation_loss: float | None
```

---

# 22. None ≠ 0

任何 metric 不可測：

```python
None
```

不是：

```python
0
```

---

# 23. Metric Kind

每項可附：

```text
EXACT
PROXY
ESTIMATED
UNKNOWN
```

---

# 24. WorldRecord

```python
@dataclass
class WorldRecord:
    world_id: str
    revision: str
    epoch: int
    snapshot_ref: str
    domain_ids: list[str]
    schema_version: str
```

---

# 25. DomainRecord

```python
@dataclass
class DomainRecord:
    domain_id: str
    world_id: str
    parent_ids: list[str]
    child_ids: list[str]
    overlap_ids: list[str]
    active_scale: Scale
    active_config_id: str | None
    permission_scope: str
```

---

# 26. ChartRecord

```python
@dataclass
class ChartRecord:
    chart_id: str
    world_revision: str
    domain_id: str
    granularity: str
    scale: Scale
    geometry: Geometry
    substrate: str
    update_form: UpdateForm
    observation_mode: str
    transition_law: TransitionLaw
    temporal_frame_id: str | None
    observer_id: str
    fidelity: float | None
    version: str
```

---

# 27. FrontierEntry

```python
@dataclass
class FrontierEntry:
    domain_id: str
    scale: Scale
    materialized: bool
    reason: str
    utility: float | None
    refinement_debt: float
    coarsening_debt: float
    ttl_epoch: int | None
```

---

# 28. ConfigurationRecord

```python
@dataclass
class ConfigurationRecord:
    config_id: str
    domain_id: str
    chart_id: str
    substrate: str
    update_form: UpdateForm
    observation_mode: str
    transition_law: TransitionLaw
    geometry: Geometry
    scale: Scale
    temporal_frame_id: str | None
    guard_id: str | None
    resource_profile_id: str | None
    version: str
```

---

# 29. ChartedStateRecord

```python
@dataclass
class ChartedStateRecord:
    state_id: str
    world_revision: str
    domain_id: str
    state_ref: str
    chart_id: str
    config_id: str
    observer_id: str
    governance_snapshot_id: str
```

---

# 30. RouteSegment

```python
@dataclass
class RouteSegment:
    segment_id: str
    source_state_id: str
    target_state_id: str | None
    source_chart_id: str
    target_chart_id: str
    source_config_id: str
    target_config_id: str
    transition_type: str
    guard_id: str | None
    validator_ids: list[str]
    expected_cost: CostVector
    authority_scope: str
    provenance_refs: list[str]
```

---

# 31. RouteRecord

```python
@dataclass
class RouteRecord:
    route_id: str
    task_id: str
    source_state_id: str
    goal_spec: dict
    segment_ids: list[str]
    expected_cost: CostVector
    realized_cost: CostVector | None
    lifecycle: str
    epoch: int
```

---

# 32. CrystalRecord

```python
@dataclass
class CrystalRecord:
    crystal_id: str
    source_route_id: str
    source_world_revision: str
    valid_domain: dict
    guard_id: str
    semantic_contract: dict
    config_signature: dict
    geometry_signature: dict
    scale_signature: dict
    temporal_causal_contract: dict
    resource_envelope: dict
    validation_profile: list[str]
    provenance_refs: list[str]
    reopen_pointer: str | None
    reopenability: str
    lifecycle: CrystalState
    utility: float
    last_validated_epoch: int
```

---

# 33. GovernanceSnapshot

```python
@dataclass
class GovernanceSnapshot:
    snapshot_id: str
    actor_id: str
    capabilities: list[str]
    permissions: list[str]
    denied_domains: list[str]
    denied_scales: list[str]
    denied_configs: list[str]
    policy_version: str
    risk_limit: float | None
```

---

# 34. RuntimeEvent

```python
@dataclass
class RuntimeEvent:
    event_id: str
    epoch: int
    event_type: str
    actor_id: str
    world_revision: str
    causal_parent_ids: list[str]
    payload: dict
    wall_time_ns: int
    logical_time: int | None
    provenance_refs: list[str]
```

---

# 35. ExperimentReceipt

```python
@dataclass
class ExperimentReceipt:
    experiment_id: str
    benchmark_id: str
    group: ExperimentGroup
    seed: int | str
    model_signature: dict
    runtime_version: str
    adapter_version: str
    world_revision: str
    initial_snapshot_ref: str
    task_spec: dict
    route_id: str | None
    config_history: list[str]
    scale_history: list[str]
    crystal_hits: list[str]
    promoted_crystals: list[str]
    invalidated_crystals: list[str]
    reopened_crystals: list[str]
    cost_vector: CostVector
    success: bool
    failure_codes: list[str]
    validation_summary: dict
    final_state_digest: str
```

---

# 36. Canonical JSON Rules

所有 receipts：

```text
UTF-8
sorted keys
no NaN
explicit null
stable enum strings
```

---

# 37. Receipt Hash

```python
sha256(canonical_json_bytes)
```

---

# 38. SQLite Tables

最小：

```sql
worlds
domains
charts
frontier
configurations
states
routes
route_segments
compiled_paths
crystals
crystal_dependencies
events
cost_records
validation_records
governance_snapshots
experiment_receipts
```

---

# 39. JSONL Ledger

額外 append-only：

```text
ledger/events.jsonl
ledger/experiments.jsonl
ledger/crystals.jsonl
```

---

# 40. Why Both SQLite + JSONL

SQLite：

- query；
- aggregation；
- experiment analysis。

JSONL：

- append-only；
- diff；
- audit；
- portable replay。

---

# 41. Database Is Cacheable Index over Ledger

v0.1 建議：

$$
\boxed{
\text{JSONL receipts = canonical evidence}
}
$$

$$
\boxed{
\text{SQLite = queryable runtime index}
}
$$

---

# 42. Adapter Base Contract

```python
class TargetAdapter(Protocol):
    async def observe(self, task: TaskSpec) -> Observation: ...
    async def snapshot(self) -> SnapshotRef: ...
    async def restore(self, snapshot: SnapshotRef) -> None: ...
    async def execute(self, action: ActionSpec) -> ActionResult: ...
    async def validate(self, result: ActionResult, task: TaskSpec) -> ValidationResult: ...
```

---

# 43. Optional Adapter Hooks

```python
async def enumerate_actions(...)
async def estimate_cost(...)
async def causal_dependencies(...)
async def materialize(...)
async def de_materialize(...)
```

---

# 44. Optional Means Optional

URR 不得要求所有 target 都支援完整因果圖。

---

# 45. Adapter Capability Record

```text
can_snapshot
can_restore
can_seed
can_measure_work
can_measure_causal_depth
can_shadow_execute
can_enumerate_actions
```

---

# 46. Runtime Must Respect Adapter Capabilities

不能假裝 target 有不存在的能力。

---

# 47. TaskSpec

```python
@dataclass
class TaskSpec:
    task_id: str
    goal: dict
    success_predicate: dict
    risk_class: str
    budget: dict
    objective: dict
    metadata: dict
```

---

# 48. Observation

```python
@dataclass
class Observation:
    world_revision: str
    state_ref: str
    domains: list[str]
    raw: dict
    timestamp_ns: int
```

---

# 49. ActionSpec

```python
@dataclass
class ActionSpec:
    action_type: str
    parameters: dict
    authority_scope: str
    expected_cost: CostVector | None
```

---

# 50. ActionResult

```python
@dataclass
class ActionResult:
    success: bool
    new_state_ref: str | None
    observed_cost: CostVector
    events: list[dict]
    error_code: str | None
```

---

# 51. Validator Interface

```python
class Validator(Protocol):
    async def validate(
        self,
        before: ChartedStateRecord,
        after: ChartedStateRecord,
        task: TaskSpec,
        route: RouteRecord,
    ) -> ValidationResult: ...
```

---

# 52. ValidationResult

```python
@dataclass
class ValidationResult:
    passed: bool
    kinds: list[ValidationKind]
    evidence_refs: list[str]
    failure_codes: list[str]
    confidence: float | None
```

---

# 53. Guard Interface

```python
class Guard(Protocol):
    async def check(self, observation: Observation, task: TaskSpec) -> GuardResult: ...
```

---

# 54. GuardResult

```python
@dataclass
class GuardResult:
    allowed: bool
    reason: str
    evidence_refs: list[str]
```

---

# 55. Governance Gate

```python
class GovernanceGate:
    def authorize(
        self,
        actor,
        action,
        domain,
        scale,
        config,
    ) -> AuthorizationDecision:
        ...
```

---

# 56. AuthorizationDecision

```text
ALLOW
DENY
ALLOW_WITH_GUARD
```

---

# 57. Fail Closed on Authority Unknown

如果 authority 不確定：

```text
DENY
```

---

# 58. Fail Open on Optimization Unknown?

不是。

更準確：

```text
optimization unknown → canonical route
authority unknown → deny
```

---

# 59. Runtime Main API

```python
class URRRuntime:
    async def run_task(
        self,
        task: TaskSpec,
        adapter: TargetAdapter,
        experiment_group: ExperimentGroup,
    ) -> ExperimentReceipt:
        ...
```

---

# 60. Group Feature Flags

```python
@dataclass
class FeatureFlags:
    adaptive_route: bool
    persistent_crystals: bool
    scale_routing: bool
    config_routing: bool
    geometry_routing: bool
```

---

# 61. A Flags

```text
adaptive_route = false
persistent_crystals = false
scale_routing = false
config_routing = false
geometry_routing = false
```

---

# 62. B Flags

```text
adaptive_route = true
persistent_crystals = false
scale_routing = false
config_routing = false
geometry_routing = false
```

---

# 63. C Flags

```text
adaptive_route = true
persistent_crystals = true
scale_routing = false
config_routing = false
geometry_routing = false
```

---

# 64. D Flags

```text
adaptive_route = true
persistent_crystals = true
scale_routing = true
config_routing = true
geometry_routing = true
```

---

# 65. This Prevents Hidden Capability Leakage

A/B/C/D 共用同一 runtime binary，只改 flags。

---

# 66. Canonical Route Interface

每 benchmark 必須註冊：

```python
canonical_route(task)
```

---

# 67. A Always Uses Canonical

---

# 68. B-D Can Fallback to Canonical

---

# 69. Route Candidate Interface

```python
class RouteGenerator:
    async def generate(
        self,
        state,
        task,
        context,
    ) -> list[RouteCandidate]:
        ...
```

---

# 70. RouteCandidate

```python
@dataclass
class RouteCandidate:
    candidate_id: str
    route: RouteRecord
    expected_cost: CostVector
    confidence: float | None
    evidence_refs: list[str]
```

---

# 71. Candidate Selector

```python
class RouteSelector:
    def select(
        self,
        candidates,
        objective,
        budget,
    ) -> RouteCandidate:
        ...
```

---

# 72. Scalar Mode

最小：

```python
weighted_sum(cost_vector)
```

---

# 73. Pareto Mode

保留 nondominated candidates。

---

# 74. Meta Cost

Route generation + selection 的耗時 / calls 記入：

```text
cost.meta
```

---

# 75. Configuration Router

v0.1：

```python
class ConfigurationRouter:
    async def choose(
        self,
        observation,
        task,
        profile_store,
    ) -> ConfigurationRecord:
        ...
```

---

# 76. Initial Heuristic Router

不要一開始用複雜 AI。

先用 deterministic heuristic：

```text
small / simple → S
sparse indexed → J
independent batch → P
stable repeated → R
```

---

# 77. Why Heuristic First

先測 route grammar，不混入另一個學習器。

---

# 78. Later Learned Router

Phase C 再做。

---

# 79. Scale Router

```python
class ScaleRouter:
    def choose(
        self,
        frontier,
        task,
        uncertainty,
        risk,
    ) -> Scale:
        ...
```

---

# 80. Initial Scale Heuristic

```text
novel/high-risk/failed → FINE
known but active → MESO
stable/hot-crystal → COARSE
```

---

# 81. Refinement Debt

每次 coarse decision 若：

```text
unresolved uncertainty
failed validation
novel evidence
```

增加：

```text
refinement_debt
```

---

# 82. Coarsening Debt

長期 fine 且 stable：

```text
coarsening_debt += cost
```

---

# 83. Threshold Switch

```python
if refinement_debt > down_threshold:
    refine()
elif coarsening_debt > up_threshold:
    coarsen()
```

---

# 84. Hysteresis

```text
down_threshold != up_threshold
```

---

# 85. Geometry Router

v0.1 可只支援：

```text
LINE
SURFACE
UNKNOWN
```

---

# 86. Synthetic Geometry

SW-01 → LINE  
SW-03 → SURFACE  
unknown test → UNKNOWN

---

# 87. Later Add JUMP_LINE / CLUSTER

---

# 88. Crystal Lookup

```python
class CrystalStore:
    async def find_eligible(
        self,
        observation,
        task,
        governance,
    ) -> list[CrystalRecord]:
        ...
```

---

# 89. Eligibility

必須：

```text
lifecycle == HOT or WARM
world_revision compatible
guard pass
authority pass
domain match
```

---

# 90. HOT Preferred over WARM?

可，但仍看 utility / recency。

---

# 91. COLD

只 shadow / validation。

---

# 92. STALE

不得 fast execute。

---

# 93. RETIRED

不參與。

---

# 94. Crystal Invocation

```python
async def invoke_crystal(crystal, task, adapter):
    assert crystal.lifecycle in {WARM, HOT}
    assert guard_pass
    result = await execute_compiled(...)
    validation = await cheap_validate(...)
    if not validation.passed:
        mark_stale(crystal)
        return fallback()
    return result
```

---

# 95. Crystal Compiler

```python
class PathCompiler:
    async def compile(
        self,
        route_history: list[RouteRecord],
        task_family: str,
    ) -> CompiledPathCandidate:
        ...
```

---

# 96. v0.1 Compiler Is Conservative

只支援：

```text
exact repeated route
parameterized repeated route
stable deterministic shortcut
```

---

# 97. Not General Program Synthesis

---

# 98. CompiledPathCandidate

```python
@dataclass
class CompiledPathCandidate:
    compiled_id: str
    source_route_ids: list[str]
    task_family: str
    parameter_schema: dict
    guard_spec: dict
    action_template: list[ActionSpec]
    cost_before: CostVector
    cost_after_estimate: CostVector
    evidence_refs: list[str]
```

---

# 99. EHPE Gate

Candidate 先算：

$$
U_H
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

---

# 100. If $U_H \le 0$

不要 promote。

---

# 101. Promotion Manager

```python
class PromotionManager:
    async def evaluate(
        self,
        candidate,
        validation_history,
        utility,
        reopenability,
    ) -> PromotionDecision:
        ...
```

---

# 102. Promotion Decision

```text
REJECT
KEEP_CANDIDATE
PROMOTE_COLD
PROMOTE_WARM
PROMOTE_HOT
```

---

# 103. v0.1 Direct HOT Disabled

第一版禁止：

```text
CANDIDATE → HOT
```

---

# 104. Required Path

```text
CANDIDATE → COLD → WARM → HOT
```

---

# 105. Validation Count Thresholds

Example defaults：

```text
COLD: 1 successful differential/replay
WARM: >= 3 successful held-out runs
HOT: >= 10 successful runs + low failure rate
```

---

# 106. Defaults Are Configurable

不是理論常數。

---

# 107. Held-Out Requirement

至少一部分 promotion evidence 必須來自 unseen seed / variant。

---

# 108. Invalidation Manager

```python
class InvalidationManager:
    def on_world_change(change_event):
        affected = dependency_index.lookup(change_event)
        for crystal in affected:
            mark_stale(crystal)
```

---

# 109. Dependency Index

每 crystal 保存：

```text
world_revision
domain dependencies
config dependencies
policy dependencies
source route dependencies
```

---

# 110. Parent Crystal Revalidation

nested crystal 需要：

```text
child stale → parent needs_revalidation
```

---

# 111. Reopen Manager

```python
class ReopenManager:
    async def reopen(crystal, mode="SELECTIVE"):
        ...
```

---

# 112. Reopen Modes

```text
SELECTIVE
FULL
AUDIT
```

---

# 113. Selective

只取 relevant source route。

---

# 114. Full

完整 source traces。

---

# 115. Audit

再加 validation / provenance chain。

---

# 116. Reopen Failure

必須產生：

```text
REOPEN_FAILED
```

不能 silent fallback。

---

# 117. Cost Ledger

每 step 記：

```text
expected
realized
metric_kind
source
```

---

# 118. Cost Aggregation

```python
def aggregate_cost(segment_costs) -> CostVector:
    ...
```

---

# 119. Work

通常 sum。

---

# 120. Causal Depth

不能 sum；需要 dependency model。

---

# 121. Wall Time

real elapsed。

---

# 122. Risk

可 max / policy-specific。

---

# 123. Observation Loss

可 max / accumulated depending bridge。

---

# 124. Aggregation Must Be Metric-Aware

禁止：

```text
all fields = sum
```

---

# 125. CostPolicy

```python
class CostPolicy:
    aggregate_work = sum
    aggregate_depth = longest_path
    aggregate_time = measured
    aggregate_risk = max
```

---

# 126. Experiment Runner

```python
class ExperimentRunner:
    async def run_matrix(
        self,
        benchmark,
        seeds,
        groups=(A,B,C,D),
    ) -> list[ExperimentReceipt]:
        ...
```

---

# 127. Pairing

每 seed 依序 clone same snapshot。

---

# 128. Group Order Randomization

避免 cache / external environment 順序偏差。

---

# 129. Persistent Structure Scope

非常重要。

A：

```text
no persistence
```

B：

```text
route history allowed only within run or prescribed episode
```

C/D：

```text
crystal persistence allowed across designated training episodes
```

---

# 130. Training / Evaluation Split

即使不是 ML training，也用：

```text
adaptation phase
evaluation phase
```

---

# 131. Adaptation Phase

允許 C/D 建 crystal。

---

# 132. Evaluation Phase

freeze crystal population 或依 protocol 限制。

---

# 133. Shift Phase

中途改 world，測 invalidation / adaptation。

---

# 134. Experiment State Reset

A/B/C/D 不能共享 unintended runtime state。

---

# 135. Explicit Shared State

只共享 protocol 指定：

```text
model
initial world
external dataset
```

---

# 136. D Cannot Read C's Crystal Store

每 group isolated store。

---

# 137. Synthetic Adapter

```python
class SyntheticAdapter(TargetAdapter):
    ...
```

---

# 138. Synthetic World API

```text
load_world(spec)
observe()
execute(op)
snapshot()
restore()
validate()
dependency_graph()
```

---

# 139. SW-01 Representation

```json
{
  "type": "sequential",
  "nodes": 100,
  "cost_per_node": 1
}
```

---

# 140. SW-02 Representation

```json
{
  "type": "sparse_jump",
  "nodes": 10000,
  "targets_per_query": 3,
  "index_build_cost": 500
}
```

---

# 141. SW-03 Representation

```json
{
  "type": "parallel_surface",
  "tasks": 100,
  "dependency": "independent"
}
```

---

# 142. SW-04 Representation

```json
{
  "type": "repeated_retrieval",
  "query_family_size": 50,
  "repeat_rate": 0.8
}
```

---

# 143. SW-05 Representation

```json
{
  "type": "recursive",
  "macro_nodes": 10,
  "micro_nodes_per_macro": 100
}
```

---

# 144. Synthetic Exact Work

Synthetic 應能提供：

```text
exact primitive op count
```

---

# 145. Synthetic Exact Causal Depth

因 dependency graph 已知，可精確算。

---

# 146. Adventure Land Adapter

兩種方式：

### Option 1

JS adapter → localhost HTTP Sidecar。

### Option 2

JS adapter → JSONL command queue。

---

# 147. Prefer Local HTTP for Interactive

Endpoints：

```text
POST /observe
POST /plan
POST /receipt
POST /invalidate
```

---

# 148. But URR Does Not Require Network

也可 in-process mock。

---

# 149. Adventure Land Observation Schema

```json
{
  "character": {
    "name": "...",
    "map": "...",
    "x": 0,
    "y": 0,
    "hp": 0,
    "mp": 0
  },
  "inventory": [],
  "target": null,
  "cooldowns": {},
  "bank_status": {},
  "nearby_entities": []
}
```

---

# 150. Adventure Land Allowed Actions

```text
move
smart_move
attack
use_skill
buy
sell
bank_deposit
bank_withdraw
equip
unequip
rest
```

---

# 151. High-Risk Game Actions

即使是遊戲實驗，也可標：

```text
high death probability
expensive item transfer
irreversible test state
```

---

# 152. Snapshot Challenge

Adventure Land live world 不一定可 full snapshot。

因此：

```text
snapshot_strength = PARTIAL
```

必須明示。

---

# 153. Benchmark Can Use Controlled Private/Test Environment

較適合 replay。

---

# 154. Adventure Land Work Proxy

```text
decision calls
model calls
movement actions
combat actions
inventory actions
```

---

# 155. BehaviorCrystal

```json
{
  "task_family": "farm_bank_return",
  "guard": {
    "map": "main",
    "inventory_fill_gt": 0.8
  },
  "steps": [
    {"action":"smart_move","target":"bank"},
    {"action":"bank_deposit","filter":"..."},
    {"action":"smart_move","target":"farm_spot"}
  ]
}
```

---

# 156. Generative Agents Adapter

優先 hook：

```text
perceive
retrieve
plan
reflect
execute
```

---

# 157. GA Observation

```json
{
  "agent_id": "...",
  "time": "...",
  "location": "...",
  "perceived_events": [],
  "active_goals": [],
  "working_memory": [],
  "memory_query": null
}
```

---

# 158. GA Action Types

```text
retrieve_memory
plan_action
reflect
move
speak
interact
wait
```

---

# 159. MemoryCrystal

```json
{
  "task_family": "memory_retrieval",
  "semantic_key": "...",
  "source_memory_ids": [],
  "guard": {
    "max_age": "...",
    "conflict_policy": "REOPEN_ON_CONFLICT"
  },
  "summary": "...",
  "validator": "source_consistency"
}
```

---

# 160. Crystal-First Retrieval

```python
crystals = lookup(query)
if valid_hot_crystal:
    answer = crystal
    if conflict_detector():
        reopen_sources()
else:
    canonical_retrieval()
```

---

# 161. Conflict Detector

新 memory 與 crystal source / conclusion 矛盾：

```text
mark stale
reopen
rebuild candidate
```

---

# 162. GA Work Proxy

```text
embedding calls
memory scoring count
retrieved nodes
LLM calls
context tokens
```

---

# 163. Model Calls Must Be Accounted Separately

因成本差異大。

---

# 164. Provider Cost

可額外記：

```text
input_tokens
output_tokens
cached_tokens
estimated_api_cost
```

---

# 165. But Token Cost ≠ Work

作一個 cost dimension，不替代其他 metric。

---

# 166. Runtime Settings

```toml
[runtime]
mode = "experiment"
objective_mode = "weighted"
enable_receipts = true
enable_replay = true

[crystal]
min_cold_runs = 1
min_warm_runs = 3
min_hot_runs = 10
allow_direct_hot = false

[scale]
enabled = true
down_threshold = 0.7
up_threshold = 0.3

[config]
enabled_forms = ["S","J","P","R"]

[governance]
fail_closed = true
```

---

# 167. Experiment Manifest

```yaml
benchmark_id: SW-04
groups:
  - A_FIXED
  - B_ADAPTIVE_ROUTE
  - C_CRYSTALLIZED
  - D_FULL_MULTISCALE
seeds: [1,2,3,...]
adaptation_episodes: 20
evaluation_episodes: 20
shift_episode: null
model:
  provider: null
  version: null
```

---

# 168. LLM-Free Synthetic

model：

```text
provider = NONE
```

---

# 169. Frozen LLM Experiment

model signature 必須完整。

---

# 170. Runtime Logs

Human-readable：

```text
logs/run.log
```

Canonical：

```text
ledger/*.jsonl
```

---

# 171. No Human Log as Canonical Evidence

---

# 172. Error Codes

最小：

```text
AUTH_DENIED
BUDGET_EXCEEDED
GUARD_FAIL
VALIDATION_FAIL
ROUTE_NOT_FOUND
CRYSTAL_STALE
REOPEN_FAILED
SNAPSHOT_FAILED
RESTORE_FAILED
ADAPTER_ERROR
METRIC_UNKNOWN
INVARIANT_VIOLATION
```

---

# 173. Error Must Be Structured

不要只存 exception string。

---

# 174. RuntimeResult

```python
@dataclass
class RuntimeResult:
    success: bool
    receipt_id: str
    error_code: str | None
    output_ref: str | None
```

---

# 175. State Commit Rule

任何 state-changing target action：

```text
execute
→ validate
→ commit receipt
```

---

# 176. If Validation Fails

如果 target 可 rollback：

```text
restore(snapshot)
```

---

# 177. If Cannot Rollback

記：

```text
rollback_strength = NONE
```

高風險 test 不應在此 adapter 執行。

---

# 178. Shadow Mode

如果 target 支援：

```text
simulate
dry_run
clone
```

新 compiled route 先 shadow。

---

# 179. Differential Validator

canonical route vs candidate route：

```text
same success predicate
same relevant state invariants
```

---

# 180. Route Equivalence

不是要求 byte-identical state，除非 benchmark 指定。

---

# 181. Relevant Invariant Spec

每 benchmark 應提供：

```python
def relevant_invariants(state) -> dict:
    ...
```

---

# 182. Example Adventure Land

可能：

```text
alive
inventory target satisfied
bank operation correct
final location acceptable
```

---

# 183. Example GA

```text
goal continuity
relevant memory recalled
contradiction not missed
persona constraint preserved
```

---

# 184. Crystal Guard Spec

建議 declarative：

```json
{
  "all": [
    {"field":"map","eq":"main"},
    {"field":"inventory_fill","gte":0.8}
  ]
}
```

---

# 185. Avoid Arbitrary Code First

Declarative guard 易 audit / serialize。

---

# 186. Guard Operators

v0.1：

```text
eq
neq
gt
gte
lt
lte
in
not_in
exists
all
any
```

---

# 187. Later Custom Guard Plugin

---

# 188. Valid Domain Spec

同樣 declarative。

---

# 189. Crystal Parameterization

Compiled route 可以 template：

```text
target_location
item_filter
query_key
```

---

# 190. Parameter Schema

JSON Schema-like。

---

# 191. Candidate Generalization

只有 parameterized held-out validation 成功，才從 exact-cache 升成 generalized crystal。

---

# 192. Exact Cache Label

如果只 exact key：

```text
crystal_kind = EXACT_CACHE
```

---

# 193. Generalized Route Crystal

```text
crystal_kind = ROUTE_CRYSTAL
```

---

# 194. This Prevents Overclaim

---

# 195. Crystal Kinds

v0.1：

```text
EXACT_CACHE
ROUTE_CRYSTAL
BEHAVIOR_CRYSTAL
MEMORY_CRYSTAL
CONFIG_CRYSTAL
```

---

# 196. Crystal Kind Does Not Change Promotion Rules

---

# 197. Crystal Store Query

key by：

```text
task_family
world_revision compatibility
domain
scale
config
semantic key
```

---

# 198. Selection Cost

Crystal lookup 自己計：

```text
cost.meta
```

或 maintenance/search submetric。

---

# 199. Too Many Crystals

Store 需要 limit。

---

# 200. Garbage Collection

```text
RETIRED
low utility
duplicate
long-unused
```

可清 active index，但 canonical receipts 保留。

---

# 201. Canonical Evidence Never Garbage-Collected by Runtime

除非 explicit data retention policy。

---

# 202. Duplicate Detection

初版可用：

```text
task_family + normalized route signature
```

---

# 203. Route Signature

```text
action_type sequence
config sequence
scale sequence
```

---

# 204. Semantic Duplicate Later

Phase C。

---

# 205. Profile Store

保存：

```text
route_profiles
config_profiles
scale_profiles
crystal_profiles
```

---

# 206. Profile Update

只更新 external runtime statistics。

---

# 207. Frozen Model Remains

$$
\Delta\theta=0.
$$

---

# 208. Config Profile

```python
@dataclass
class ConfigProfile:
    config_id: str
    task_family: str
    runs: int
    success_rate: float
    mean_cost: CostVector
    p95_wall_time_ms: float | None
```

---

# 209. Scale Profile

同理。

---

# 210. Route Profile

同理。

---

# 211. Crystal Profile

額外：

```text
hit_rate
false_accept
false_reject
stale_rate
maintenance_cost
reopen_success
```

---

# 212. Experiment Isolation

每 group：

```text
separate database namespace
separate crystal store
separate profile store
```

---

# 213. Shared Code Only

---

# 214. Shared Model Only

---

# 215. Shared Seed Only

---

# 216. Reset Function

```python
await runtime.reset_to(snapshot, group_namespace)
```

---

# 217. Group Namespace

```text
exp123/A
exp123/B
exp123/C
exp123/D
```

---

# 218. Experiment Runner Order

per seed：

```text
snapshot base
randomize group order
for group:
    restore base
    load group namespace
    run task
    store receipt
```

---

# 219. Persistent Adaptation Experiments

需：

```text
namespace persists across adaptation episodes
```

---

# 220. Evaluation Freeze

可設定：

```text
allow_new_crystal_promotion = false
```

看已學結構效用。

---

# 221. Alternative Online Evaluation

也可允許繼續 adaptation，但需標 protocol。

---

# 222. Metrics Export

輸出：

```text
CSV
JSON
Parquet optional
```

---

# 223. Summary Report

自動產生：

```text
per benchmark
per group
paired differences
learning curves
failure counts
```

---

# 224. No Chart Requirement in v0.1

先數據正確。

---

# 225. Test Layout

```text
tests/unit/
  test_cost.py
  test_guard.py
  test_crystal_lifecycle.py
  test_config_router.py
  test_scale_router.py

tests/invariants/
  test_urr_01_16.py

tests/integration/
  test_fast_slow_path.py
  test_invalidation_reopen.py
  test_group_isolation.py

tests/experiments/
  test_sw01.py
  test_sw04.py
  test_sw07.py
  test_sw08.py
  test_sw10.py
```

---

# 226. First Required Synthetic Tests

按 Phase B Paper 02：

$$
SW01,
SW04,
SW07,
SW08,
SW10.
$$

---

# 227. SW-01 Test Goal

防止 fake optimization。

---

# 228. SW-04 Test Goal

crystal lifecycle / retrieval gain。

---

# 229. SW-07 Test Goal

S/J/P/R workload shift。

---

# 230. SW-08 Test Goal

stale / reopen。

---

# 231. SW-10 Test Goal

wrapper illusion。

---

# 232. Test: Wrapper Illusion

```python
assert wrapper.cost.work == baseline.cost.work
assert wrapper.cost.hops < baseline.cost.hops
```

---

# 233. Test: Compiled Path Candidate Not Crystal

```python
assert compiled.status == "CANDIDATE"
assert not crystal_store.is_hot(compiled.id)
```

---

# 234. Test: Authority Preservation

```python
assert crystal.authority <= source.authority
```

語義上以 scope subset 驗。

---

# 235. Test: Reopenability

```python
assert crystal.reopen_pointer is not None
```

除非 declared irreversible。

---

# 236. Test: Stale Cannot Execute

```python
with pytest.raises(CrystalStaleError):
    invoke(stale_crystal)
```

---

# 237. Test: Unknown Metric

```python
assert cost.causal_depth is None
assert cost.causal_depth != 0
```

---

# 238. Test: Group Isolation

C 的 crystal 不得被 D 讀到。

---

# 239. Test: Frozen Model Signature

四組 receipt：

```python
assert A.model_signature == B.model_signature == C.model_signature == D.model_signature
```

---

# 240. Test: Meta Cost Included

B-D route generation cost 不能遺漏。

---

# 241. Test: Switch Cost

config / scale switch 至少：

```text
0 or positive measured
```

若真的 0，需有 measurement evidence。

---

# 242. Test: No Direct HOT

```python
assert transition(CANDIDATE, HOT) is rejected
```

---

# 243. Test: Held-Out Promotion

HOT promotion 前至少一個 held-out evidence。

---

# 244. Acceptance Gate G1

Repo install：

```text
pip install -e .
```

成功。

---

# 245. G2

```text
pytest
```

全 pass。

---

# 246. G3

SW-01 / 04 / 07 / 08 / 10 可 reproducibly run。

---

# 247. G4

A/B/C/D receipts schema 相同。

---

# 248. G5

每 run 有 canonical JSON receipt hash。

---

# 249. G6

world snapshot / restore 在 Synthetic 完整成功。

---

# 250. G7

stale crystal 被禁止 fast execute。

---

# 251. G8

reopen 可以回 source route。

---

# 252. G9

wrapper illusion test 不誤報 work speedup。

---

# 253. G10

config shift SW-07 能至少表現不同 config selection。

---

# 254. G11

full D 的 meta cost 有被計。

---

# 255. G12

authorization hard-fail test pass。

---

# 256. Minimal CLI

```text
urr init
urr run --benchmark SW-04 --group C --seed 1
urr matrix --benchmark SW-04 --seeds 1:30
urr inspect-crystal <id>
urr invalidate <id>
urr reopen <id>
urr replay <receipt>
urr report <experiment-batch>
```

---

# 257. CLI Is Optional but Recommended

便於本地 AI / human debugging。

---

# 258. Minimal HTTP API

若需要跨語言：

```text
POST /v1/observe
POST /v1/plan
POST /v1/execute
POST /v1/validate
POST /v1/receipt
GET  /v1/crystals
POST /v1/crystals/{id}/invalidate
POST /v1/crystals/{id}/reopen
```

---

# 259. Plan Endpoint Must Not Auto-Execute

```text
plan != commit
```

---

# 260. Sidecar Action Flow

```text
Target observes
→ Sidecar proposes
→ Adapter executes
→ Sidecar validates
→ Ledger commits
```

---

# 261. Proposal Before Commit

工程上保留：

```text
Plan
Execution
Commit
```

分離。

---

# 262. Dry Run

```text
POST /v1/plan
```

可完全不動 target。

---

# 263. Safety by Architecture

不是只靠 prompt。

---

# 264. Adventure Land Integration Order

1. observe-only；
2. recommend action；
3. execute low-risk action；
4. add BehaviorCrystal；
5. shift tests。

---

# 265. Generative Agents Integration Order

1. observe memory query；
2. shadow crystal retrieval；
3. compare canonical retrieval；
4. enable crystal-first；
5. conflict / novelty tests。

---

# 266. No Direct Modification of GA Core First

用 wrapper / hook。

---

# 267. Adapter Hook Contract

```text
before_retrieve
after_retrieve
before_plan
after_plan
before_execute
after_execute
```

---

# 268. Thin Hook Principle

hook 只：

```text
serialize state
call sidecar
apply decision
emit receipt
```

---

# 269. No Theory Logic in Adapter

避免每 target fork 一套 UNPNP。

---

# 270. Sidecar Owns Theory Logic

---

# 271. Version Boundary

Adapter：

```text
target-specific
```

URR：

```text
target-independent
```

---

# 272. Migration

schema version：

```text
urr_schema_version
```

---

# 273. No Silent Breaking Change

---

# 274. Performance Budget for Sidecar

初版應記：

$$
C_{\mathrm{sidecar}}.
$$

---

# 275. Sidecar Gain Must Exceed Sidecar Cost

至少在 target workload。

---

# 276. Meta Overhead Threshold

如果：

$$
C_{\mathrm{sidecar}}
>
B_{\mathrm{adapt}}
$$

adaptive mode 可關閉。

---

# 277. AUTO-FIXED Mode

Runtime 可自動：

```text
if meta_gain <= 0:
    use canonical fixed route
```

---

# 278. But Experiment Group A Must Stay Pure

A 不可由 adaptive layer secretly optimize。

---

# 279. Reference Runtime Modes

```text
FIXED
ADAPTIVE
SHADOW
CRYSTALLIZING
AUDIT
RECOVERY
```

---

# 280. Mode State

需放 receipt。

---

# 281. RECOVERY

禁用 crystals / experimental switches。

---

# 282. AUDIT

強制：

```text
full reopen
deep validation
```

---

# 283. SHADOW

candidate route 不 commit。

---

# 284. CRYSTALLIZING

允許 evidence accumulation。

---

# 285. Minimal Scheduler

v0.1 不做 full global scheduler。

只做：

```text
sequential execution
parallel execution for explicitly independent synthetic tasks
```

---

# 286. Parallel Safety

沒有 dependency proof：

```text
do not parallelize
```

---

# 287. Unknown Geometry

```text
UNKNOWN → canonical sequential
```

---

# 288. Conservative Default

未知狀況回：

```text
S + MESO/known-safe + canonical route
```

依 benchmark定義。

---

# 289. Configuration Router Reward

先不用 RL。

用 empirical mean / heuristic。

---

# 290. Best-Known Config

SW-07 可從 synthetic ground truth 取得。

---

# 291. Regret 可精確計

因此 Synthetic 是 config routing 最重要 benchmark。

---

# 292. Experimental Determinism

Synthetic 的 sidecar 也應 deterministic with seed。

---

# 293. Replay Harness

```python
class ReplayHarness:
    async def replay(self, receipt_id: str) -> ReplayResult:
        ...
```

---

# 294. ReplayResult

```text
semantic_match
state_match
route_match
cost_delta
notes
```

---

# 295. Replay Levels

```text
SEMANTIC
STATE
ROUTE
TIMING
EXACT
```

---

# 296. Target Declares Supported Level

---

# 297. Replay Is Not Always Exact

尤其 game / LLM。

---

# 298. Experiment Comparison Uses Declared Level

---

# 299. Code Generation Guidance for Local AI

實作時優先：

1. schemas；
2. ledger；
3. Synthetic adapter；
4. fixed route；
5. A/B group；
6. compiled path；
7. crystal lifecycle；
8. C group；
9. config router；
10. scale router；
11. D group；
12. game / GA adapters。

---

# 300. Avoid Premature Abstraction

不要先建立：

- plugin ecosystem；
- distributed microservices；
- fancy UI；
- vector DB；
- Kubernetes。

---

# 301. Keep Repo Small

第一個 working milestone：

```text
< 5k–10k LOC
```

只是工程建議，不是硬規則。

---

# 302. Prefer Explicit Code over Metaprogramming

因為要 audit。

---

# 303. Prefer Dataclasses / Pydantic over Dynamic Dict Everywhere

---

# 304. Prefer SQLite Transactions for Ledger Index

---

# 305. Prefer Append-Only JSONL for Evidence

---

# 306. Prefer Pytest + Hypothesis

Phase B Paper 04 會正式定 invariants。

---

# 307. No Hidden Magic Learning

所有 external structure update 都要 event：

```text
PROFILE_UPDATE
ROUTE_COMPILED
CRYSTAL_PROMOTED
CONFIG_PROFILE_UPDATE
SCALE_PROFILE_UPDATE
```

---

# 308. External Structure Delta

可直接從 event ledger算：

$$
\Delta_{\mathrm{struct}}.
$$

---

# 309. Frozen-Model Audit

experiment receipt 中：

```text
model_signature_hash
```

必須一致。

---

# 310. If Model Signature Changes

batch：

```text
INVALID_FOR_FROZEN_COMPARISON
```

---

# 311. Minimal Security

Sidecar local-only by default：

```text
127.0.0.1
```

若啟 HTTP。

---

# 312. No External Bind by Default

---

# 313. No Secret in Receipt Payload

adapter 要 redact。

---

# 314. Secret References

存：

```text
secret_ref
```

不存 raw secret。

---

# 315. Provenance Can Reference Sensitive Source

但 access-controlled。

---

# 316. Benchmark Data Should Be Non-Sensitive

---

# 317. Data Retention

Synthetic 可永久保留。

Game / GA 依資料政策。

---

# 318. URR Sidecar v0.1 Completion Definition

只有以下全成立才叫完成：

$$
\boxed{
\text{Schema}
+
\text{Ledger}
+
\text{Synthetic}
+
\text{A/B/C/D}
+
\text{Crystal Lifecycle}
+
\text{Replay}
+
\text{Invariants}
}
$$

---

# 319. Not Completion

只有：

```text
classes created
```

不算。

---

# 320. Not Completion 2

只有 happy-path demo 不算。

---

# 321. Not Completion 3

沒有 A/B/C/D paired benchmark 不算。

---

# 322. Not Completion 4

crystal 不會 stale / reopen 不算。

---

# 323. Not Completion 5

meta / maintenance cost 沒記不算。

---

# 324. Done Gate

```text
[ ] install succeeds
[ ] schema tests pass
[ ] ledger replay pass
[ ] SW-01 pass
[ ] SW-04 pass
[ ] SW-07 pass
[ ] SW-08 pass
[ ] SW-10 pass
[ ] A/B/C/D isolated
[ ] frozen model signature enforced
[ ] crystal stale/reopen works
[ ] wrapper illusion detected
[ ] config switch cost measured
[ ] meta cost measured
[ ] receipts hashable
[ ] no authorization violation
```

---

# 325. Phase B Paper 04 的輸入

下一篇將把：

- URR-1～URR-16；
- B-1～B-16；
- Sidecar Done Gate；

轉成：

$$
\boxed{
\text{property tests}
+
\text{state-machine invariants}
+
\text{formal verification targets}.
}
$$

---

# 結論

URR Sidecar v0.1 的實作哲學不是：

> 把 UNPNP-II 所有理論一次寫成巨大 framework。

而是：

$$
\boxed{
\textbf{
先做一個夠小、夠透明、能量測、能重播、能失敗、能回退的 Sidecar，
讓路徑、尺度、計算形態與結晶化的收益真正被隔離出來。
}
}
$$

其最小架構：

$$
\boxed{
\text{Target}
\leftrightarrow
\text{Adapter}
\leftrightarrow
\text{URR Sidecar}
\leftrightarrow
\text{Ledger}.
}
$$

其最小 runtime loop：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Plan}
\rightarrow
\text{Authorize}
\rightarrow
\text{Execute}
\rightarrow
\text{Validate}
\rightarrow
\text{Record}
\rightarrow
\text{Adapt Structure}.
}
$$

其最小實驗要求：

$$
\boxed{
A/B/C/D
+
\text{same model}
+
\text{same seed}
+
\text{same world}
+
\text{all costs counted}.
}
$$

其最小 earned primitive 要求：

$$
\boxed{
\text{guard}
+
\text{validation}
+
\text{utility}
+
\text{provenance}
+
\text{reopenability}.
}
$$

因此 Sidecar 的價值不是「聰明地藏在 target 裡面」，而是恰好相反：

> **把 structural adaptation 明確地放在 target 外面，讓每一次 route rewrite、configuration switch、scale change、crystal promotion 與 reopen 都可以被看見、被量測、被比較、被重播。**

這就是 UNPNP-II 從 formal runtime 進入實際 reference implementation 的最小工程規格。
