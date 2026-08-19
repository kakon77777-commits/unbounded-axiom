# World-Domain Cognitive Runtime v0.1 技術白皮書

**World-Domain Cognitive Runtime v0.1: An Implementable Architecture for Executable Prospection, Branching Worlds, Evidence Governance, and Tri-Temporal Integration**

作者：Neo.K（許筌崴）  
協作架構與形式化：Aletheia  
機構：一言諾科技有限公司（EveMissLab）  
日期：2026-08-17  
版本：v0.1  
文件類型：Technical Whitepaper / Reference Architecture  
狀態：Implementation-oriented design derived from TCD v0.1 + WDC-01～08

---

# 0. Executive Summary

World-Domain Cognitive Runtime（WDC Runtime）是一個用來把：

$$
\boxed{
\text{生成未來}
}
$$

提升為：

$$
\boxed{
\text{可審計的有限世界計算}
}
$$

的 runtime architecture。

它的核心不是「生成更多看起來像世界的內容」，而是讓未來候選能被明確轉換成：

- 有 identity 的 world；
- 有可尋址 state 的 world；
- 有 transition semantics 的 world；
- 有 bounded resource contract 的 world；
- 可 checkpoint / fork / replay 的 world；
- 有 local agent / observer / evaluator 權限分離的 world；
- 能產生 provenance-bearing evidence 的 world；
- 能被 Governor 分配、暫停、停止與晉升的 world；
- 最後能把 world evidence 回饋到 TCD Past–Present–Future cognition。

WDC Runtime 的最小閉環為：

$$
\boxed{
\mathfrak T_t^{(3)}
\rightarrow
\mathcal B_t^+
\rightarrow
\mathcal W_t
\rightarrow
\mathfrak E_t^W
\rightarrow
\pi_t
\rightarrow
a_t^{real}
\rightarrow
\mathfrak T_{t+1}^{(3)}.
}
$$

其中：

$$
\mathfrak T_t^{(3)}
=
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
)
$$

是 TCD 的 Past / Present / Future triple。

本白皮書不提出新的形上學世界觀。

它只提出一個 engineering proposition：

> **如果一個 agent 已經能生成多個 future hypotheses，那麼下一步不一定只是把它們寫成文字；它可以在有限資源與證據契約下，把其中一部分升級成可執行、可分支、可驗證、可停止、可學習的計算世界。**

---

# 1. Permanent Boundaries

本白皮書永久保留：

$$
\boxed{
\text{Future Candidate}
\neq
\text{Runnable World}
\neq
\text{Actual Future}.
}
$$

以及：

$$
\boxed{
\text{World Outcome}
\neq
\text{Reality Evidence}.
}
$$

以及：

$$
\boxed{
\text{World-Local Event}
\neq
\text{Parent-Real Historical Fact}.
}
$$

以及：

$$
\boxed{
\text{World Priority}
\neq
\text{World Truth}
\neq
\text{World Moral Worth}.
}
$$

以及：

$$
\boxed{
\text{Worth Computing}
\neq
\text{Worth Believing}
\neq
\text{Worth Deploying}.
}
$$

---

# 2. Design Goal

WDC Runtime v0.1 的第一目標不是 AGI-scale open world。

第一目標是建立一個：

$$
\boxed{
\text{finite}
+
\text{typed}
+
\text{auditable}
+
\text{backend-agnostic}
+
\text{forkable}
+
\text{evidence-aware}
}
$$

的 world computation runtime。

---

# 3. Non-Goals

v0.1 不追求：

- photorealistic world generation；
- universal physics simulation；
- autonomous real-world authority；
- unlimited nested agents；
- universal world probability；
- perfect causal inference；
- fully automatic scientific truth discovery；
- one-model-does-everything architecture；
- infinite world branching；
- production-grade multi-region cloud control plane。

---

# 4. Reference Implementation Philosophy

本白皮書建議：

# **Small Core, Replaceable Backends**

核心 runtime 應保持小。

重型能力透過 adapters 加入。

因此：

$$
\boxed{
Core
\neq
Simulator.
}
$$

$$
\boxed{
Core
\neq
LLM.
}
$$

$$
\boxed{
Core
\neq
Kubernetes.
}
$$

$$
\boxed{
Core
\neq
Ray.
}
$$

$$
\boxed{
Core
\neq
Omniverse.
}
$$

核心只負責：

- identities；
- contracts；
- lineage；
- lifecycle；
- events；
- evidence；
- authority；
- TCD integration。

---

# 5. Four-Plane Architecture

v0.1 建議分成四個 plane：

$$
\boxed{
\text{Control Plane}
}
$$

$$
\boxed{
\text{World Execution Plane}
}
$$

$$
\boxed{
\text{Evidence / History Plane}
}
$$

$$
\boxed{
\text{External Boundary Plane}.
}
$$

---

# 6. Control Plane

Control Plane 負責：

- TCD State Manager；
- Future Candidate Registry；
- World Lift / Admission；
- Branch Manager；
- World Governor；
- Computation Portfolio Planner；
- Role / Authority Manager；
- Reality Commit Gate。

---

# 7. World Execution Plane

World Execution Plane 負責：

- instantiate；
- step；
- observe；
- checkpoint；
- restore；
- intervene；
- pause；
- resume；
- terminate。

它可以由：

- pure Python simulator；
- game engine；
- PettingZoo-style multi-agent env；
- scientific simulator；
- theorem runtime；
- learned world model；
- robotics / digital-twin backend；

實作。

---

# 8. Evidence / History Plane

負責：

- append-oriented runtime events；
- world lineage；
- checkpoints；
- evidence packets；
- aggregate evidence；
- Governor decisions；
- learning events；
- TCD historical sedimentation；
- provenance graph。

---

# 9. External Boundary Plane

負責：

- real-world tools；
- real APIs；
- credentials；
- real sensors；
- external datasets；
- human authorization；
- real action execution。

所有：

$$
WorldLocal
\rightarrow
ExternalReal
$$

操作都必須經：

$$
\boxed{
External Tool Proxy.
}
$$

---

# 10. Core State

整個 runtime 的 parent-level state：

$$
\boxed{
\mathfrak R_t^{WDC}
=
(
TCD_t,
WorldRegistry_t,
Governor_t,
Evidence_t,
Learning_t,
Authority_t,
Budget_t,
Contracts_t
).
}
$$

---

# 11. TCD State

```text
TCDState
  past_base_ref
  present_base_ref
  future_base_ref
  parent_time
  version
  provenance_ref
```

---

# 12. Three Clock Model

Runtime 必須永久區分：

$$
\boxed{
t
=
\text{parent historical time},
}
$$

$$
\boxed{
k
=
\text{parent deliberation iteration},
}
$$

$$
\boxed{
\tau
=
\text{world-local runtime time}.
}
$$

資料庫欄位不可只叫：

```text
time
```

而應明示：

```text
parent_time
deliberation_index
world_local_time
```

---

# 13. Future Candidate Object

```text
FutureCandidate
  candidate_id
  parent_tcd_future_version
  ontology_type
  content_ref
  probability_state
  value_state
  realization_paths
  unknown_dependencies
  evidence_refs
  created_parent_time
  created_deliberation_index
  status
```

---

# 14. Candidate Status

```text
PROPOSED
ELIGIBLE
LIFTED
RETIRED
MERGED_SEMANTICALLY
INVALIDATED
RESOLVED
```

---

# 15. Candidate Is Immutable by Version

不要 silent rewrite candidate。

修改應：

```text
candidate_v1
  -> candidate_v2
```

保留 parent。

---

# 16. WorldSpec

World identity 應先和 execution run 分開。

```text
WorldSpec
  world_id
  candidate_id
  parent_world_id
  parent_checkpoint_id
  world_type
  backend_type
  backend_version
  contract_hash
  dynamics_ref
  rules_ref
  actors_ref
  initial_state_ref
  budget_class
  authority_profile
  purpose
  fidelity_profile
  evidence_scope
  status
```

---

# 17. WorldSpec Is Definition

$$
\boxed{
WorldSpec
\neq
WorldRun.
}
$$

同一：

$$
WorldSpec_i
$$

可以有：

$$
Run_{i,1},
Run_{i,2},
\dots
$$

---

# 18. WorldRun

```text
WorldRun
  run_id
  world_id
  start_checkpoint_id
  run_seed
  runtime_backend
  runtime_version
  worker_id
  status
  local_time_start
  local_time_end
  budget_allocated
  budget_used
  trace_ref
  outcome_ref
  termination_reason
```

---

# 19. World Run Status

```text
CREATED
QUEUED
RUNNING
PAUSED
COMPLETED
KILLED
FAILED
INVALIDATED
ARCHIVED
```

---

# 20. World Backend Protocol

所有 backend 至少實作：

```text
capabilities()
instantiate(spec, context)
initialize()
step(action_batch=None)
observe(role_id=None)
checkpoint()
restore(checkpoint)
intervene(delta)
pause()
resume()
terminate(reason)
health()
```

---

# 21. Optional Backend Methods

```text
batch_step()
snapshot_metrics()
estimate_cost()
supports_exact_fork()
supports_causal_intervention()
supports_multi_agent()
supports_deterministic_replay()
```

---

# 22. Backend Capability Manifest

```text
BackendCapabilities
  exact_checkpoint: bool
  deterministic_replay: bool
  stochastic_seed_control: bool
  causal_intervention: bool
  multi_agent: bool
  partial_observation: bool
  persistent_world: bool
  external_data_tether: bool
  gpu_required: bool
  network_required: bool
```

---

# 23. MVP Backend 0 — PythonStateWorld

第一個 reference backend 應最簡單。

```text
PythonStateWorld
```

要求：

- state 是 JSON-serializable / msgpack-serializable；
- transition function 明示；
- seed 可控；
- checkpoint 精確；
- step deterministic or explicitly stochastic。

---

# 24. Why Start Symbolic?

因為：

$$
\boxed{
\text{debug lineage first}
>
\text{debug photorealism first}.
}
$$

v0.1 應先驗證：

- fork 對不對；
- history firewall 對不對；
- evidence aggregation 對不對；
- Governor budget 對不對。

---

# 25. MVP Backend 1 — Multi-Agent Adapter

可定義：

```text
PettingZooAdapter
```

利用其：

- AEC sequential mode；
- Parallel simultaneous mode；
- agent-specific observations / actions。

但 WDC Core 不依賴 PettingZoo。

---

# 26. MVP Backend 2 — External Simulator Adapter

```text
ExternalProcessAdapter
```

啟動：

- CLI simulator；
- theorem prover；
- physics solver；
- game runtime。

---

# 27. Future Backend — Learned World Adapter

```text
LearnedWorldAdapter
```

可能連：

- image/world model；
- latent dynamics；
- multimodal world generator。

但必須標：

```text
exact_checkpoint = false/true
causal_intervention = false/true
```

不能因為模型叫 World Model 就自動填 true。

---

# 28. World Contract

每個 world 必須有：

$$
\boxed{
\kappa_W.
}
$$

JSON-like：

```text
purpose
domain_type
abstraction_level
state_schema
dynamics_source
actors
rules
allowed_interventions
observation_policy
evaluation_policy
horizon
budget
fidelity
reproducibility
authority
containment
evidence_scope
transport_scope
termination
archive
```

---

# 29. Domain Types

```text
FORMAL_CLOSED
SIMULATED_DEFINED
EMPIRICAL_OPEN
```

---

# 30. FORMAL_CLOSED

例如：

- chess；
- formal theorem system；
- cellular automaton。

authoritative rules 已定。

---

# 31. SIMULATED_DEFINED

例如：

- custom game economy；
- synthetic institution；
- designed agent world。

結果只對 contract 世界成立。

---

# 32. EMPIRICAL_OPEN

例如：

- robotics；
- traffic；
- economics；
- biology。

需要：

$$
\boxed{
world\rightarrow reality
}
$$

transport validation。

---

# 33. Checkpoint Object

```text
Checkpoint
  checkpoint_id
  world_id
  run_id
  world_local_time
  state_blob_ref
  actor_state_refs
  rng_state_ref
  rules_version
  backend_version
  contract_hash
  trace_offset
  resource_state
  digest
  created_at
```

---

# 34. Checkpoint Must Include Hidden State

如果 backend：

- RNN；
- hidden planner；
- local agent memory；

checkpoint 必須按 contract 捕捉。

---

# 35. Checkpoint Validation

```text
restore(checkpoint)
query_invariants()
dry_step()
compare_expected_state()
```

---

# 36. Fork Operator

API：

```text
fork_world(
  parent_run_id,
  checkpoint_id,
  divergence_delta,
  contract_overrides,
  seed_policy
) -> child_world_id
```

---

# 37. Fork Record

```text
ForkRecord
  edge_id
  parent_world_id
  parent_run_id
  child_world_id
  checkpoint_id
  fork_parent_local_time
  divergence_type
  divergence_delta_ref
  seed_policy
  authority_delta
  contract_hash
```

---

# 38. Fork Invariant

$$
\boxed{
ID_{child}
\neq
ID_{parent}.
}
$$

---

# 39. Shared Prefix Invariant

strict fork：

$$
\boxed{
Hash(
Prefix_{child}
)
=
Hash(
Prefix_{parent}
).
}
$$

若只 approximate：

```text
fork_mode = APPROXIMATE
fork_tolerance = epsilon
```

---

# 40. Fork Types

```text
CLONE
CONTROLLED_FORK
COUNTERFACTUAL
PARAMETER_MUTATION
POLICY_MUTATION
RULE_MUTATION
BACKEND_MUTATION
```

---

# 41. Causal Label Is Explicit

只有：

```text
causal_intervention_supported = true
```

才允許事件標：

```text
DO_INTERVENTION
```

否則：

```text
PERTURBATION
CONDITIONAL_BRANCH
```

---

# 42. No Silent Merge

v0.1 預設：

```text
merge_state = DENIED
```

允許：

```text
merge_evidence
merge_lineage_metadata
```

State merge 留給明示 reconciliation adapter。

---

# 43. World Registry

核心 tables / collections：

```text
future_candidates
world_specs
world_runs
world_edges
checkpoints
role_cards
channels
events
evidence_packets
claims
evidence_aggregates
governor_decisions
computation_actions
commit_records
learning_events
source_registry
tcd_state_versions
```

---

# 44. Local MVP Storage

第一版可以用：

$$
\boxed{
SQLite
+
ContentAddressedBlobStore.
}
$$

SQLite 保存：

- metadata；
- indices；
- event rows；
- state machine。

大 blob：

- checkpoints；
- traces；
- artifacts；

放 filesystem / object store。

---

# 45. Why Separate Blob Storage?

不把：

$$
10\text{ GB checkpoint}
$$

直接塞進 metadata row。

---

# 46. WAL Mode

本地並發 MVP 可使用 SQLite WAL。

但要知道：

- 多 reader；
- single writer semantics；
- WAL / database file integrity 必須一起管理。

這是 local reference choice，不是 WDC 理論要求。

---

# 47. Distributed Storage

規模化後可替換為：

- PostgreSQL；
- graph database；
- object storage；
- event streaming backend。

不改 core schema semantics。

---

# 48. Immutable-ish Event Ledger

每個 consequential operation 寫 event。

---

# 49. Event Envelope

建議借用 CloudEvents-style common envelope 思想：

```text
event_id
event_type
source
subject
timestamp
scope
schema_version
trace_id
parent_time
deliberation_index
world_local_time
world_id
run_id
actor_id
payload_ref
provenance_ref
```

---

# 50. Event Scope

```text
WORLD_LOCAL
PARENT_INTERNAL
EXTERNAL_REAL
```

---

# 51. History Firewall

Scope promotion 不可自動。

```text
WORLD_LOCAL
  -> PARENT_INTERNAL_EVIDENCE
```

可以。

但：

```text
WORLD_LOCAL
  -> EXTERNAL_REAL
```

禁止。

---

# 52. Example

World event：

```text
CityCollapsed
scope=WORLD_LOCAL
world_id=W17
```

轉 parent：

```text
WorldOutcomeObserved
scope=PARENT_INTERNAL
payload={
  world_id: W17,
  result: CityCollapsed
}
```

不能轉：

```text
CityCollapsed
scope=EXTERNAL_REAL
```

---

# 53. Parent Real Events

例如：

```text
RealActionCommitted
RealSensorObservation
RealOutcomeObserved
ExternalDatasetReceived
HumanAuthorizationGranted
```

才可作 parent-real sedimentation source。

---

# 54. Event Bus

v0.1 可用：

- in-process event bus；
- persisted event table。

distributed 版可換：

- message broker；
- CloudEvents-compatible routing。

---

# 55. Observability

WDC 每次：

- Spawn；
- Fork；
- Run；
- Evaluate；
- Aggregate；
- Commit；

都應有 trace correlation。

---

# 56. Trace Context

建議使用：

```text
trace_id
span_id
world_id
run_id
computation_id
parent_time
```

---

# 57. OpenTelemetry Adapter

OpenTelemetry 的 execution-scoped Context / tracing model 適合：

- service-to-service correlation；
- world-run spans；
- evaluator spans；
- Governor spans。

但：

$$
\boxed{
OpenTelemetry
\neq
WDC Provenance.
}
$$

WDC provenance 比 observability trace更長期、更 semantic。

---

# 58. World Provenance Graph

至少有：

```text
candidate -> world
world -> run
run -> checkpoint
checkpoint -> forked_world
world_run -> evidence
evidence -> aggregate
aggregate -> governor_decision
governor_decision -> commit
commit -> real_action
real_action -> real_outcome
real_outcome -> learning_event
```

---

# 59. Role Model

角色：

```text
MASTER
LOCAL_AGENT
OBSERVER
EVALUATOR
GOVERNOR
SAFETY_OBSERVER
EXTERNAL_AUTHORIZER
```

---

# 60. Role Capability Card

```text
RoleCard
  role_id
  role_type
  world_scope
  branch_scope
  observation_scope
  action_scope
  tool_scope
  external_authority
  memory_scope
  channel_allowlist
  audit_level
```

---

# 61. Observation Is Separate From Authority

```text
can_read_world_state = true
can_modify_world_state = false
```

是一個正常 observer。

---

# 62. Evaluator Default

```text
can_modify_world = false
can_external_act = false
```

---

# 63. World-Local Agent Default

```text
external_authority = NONE
```

---

# 64. WorldRoot Is Not HostRoot

即使：

```text
world_role = root
```

仍：

```text
host_permissions = none
```

---

# 65. Information Flow Matrix

```text
InfoFlow[source_role][target_role]
  allowed_content_types
  direction
  delay
  sanitization
  logging
```

---

# 66. Sibling Blindness Mode

paired counterfactual：

```text
branch_visibility = ISOLATED_UNTIL_RESOLUTION
```

---

# 67. Cross-World Coupled Mode

```text
branch_visibility = EXPLICIT_CHANNELS
```

---

# 68. No Hidden Shared Memory

每個 world / role 的：

- vector memory；
- DB namespace；
- cache；
- session；

必須 namespaced。

---

# 69. World Namespace

```text
wdc://world/W17/...
```

parent:

```text
wdc://parent/...
```

external:

```text
external://...
```

---

# 70. Sandbox Profiles

建議風險分級：

```text
S0_INPROCESS
S1_PROCESS
S2_CONTAINER
S3_GVISOR
S4_MICROVM
```

---

# 71. S0

可信 symbolic worlds。

---

# 72. S1

獨立 process。

---

# 73. S2

普通 OCI container。

---

# 74. S3

gVisor-style sandbox。

---

# 75. S4

Firecracker-style microVM。

---

# 76. Isolation Adapter

```text
SandboxAdapter
  create()
  exec()
  mount()
  set_network_policy()
  set_resource_limits()
  snapshot()
  terminate()
```

---

# 77. gVisor Role

gVisor 可作：

$$
\boxed{
HostIsolationBackend.
}
$$

它不是 observer separation logic 本身。

---

# 78. Firecracker Role

Firecracker microVM 可作：

- stronger process / kernel boundary；
- high-risk tool-using worlds；
- untrusted generated code worlds。

---

# 79. Isolation Has Cost

所以 Governor 可根據：

```text
risk_class
```

選 sandbox profile。

---

# 80. External Tool Proxy

所有 real action：

```text
World -> ExternalToolProxy -> Authorizer -> RealTool
```

---

# 81. Request Object

```text
ExternalActionRequest
  request_id
  world_id
  role_id
  tool
  operation
  target
  payload_digest
  reason
  required_authority
```

---

# 82. Default Deny

$$
\boxed{
DefaultExternalAuthority
=
NONE.
}
$$

---

# 83. Scoped Capability

如果允許：

```text
CapabilityToken
  world_id
  role_id
  operation_allowlist
  target_allowlist
  budget
  expiry
```

---

# 84. Fork Cannot Increase Authority

child token：

$$
\boxed{
Cap_c
\subseteq
Cap_p.
}
$$

除非 external authorizer grant。

---

# 85. World Governor

Governor 是 control-plane policy engine。

---

# 86. Governor Inputs

```text
world registry
global budget
evidence state
deadlines
risk
transport debt
unknown-world mass
computation queue
```

---

# 87. Governor Operations

```text
AdmitWorld
SpawnWorld
ForkWorld
AllocateBudget
ScheduleWorld
PauseWorld
ResumeWorld
PreemptWorld
KillWorld
ArchiveWorld
PromoteWorld
DemoteWorld
InvalidateWorld
```

---

# 88. Governor Does Not Place Pods Directly

可以交給 scheduler adapter。

---

# 89. Scheduler Adapter

```text
SchedulerAdapter
  feasible(requirements)
  reserve(bundle)
  submit(workload)
  preempt(workload)
  release(workload)
  status(workload)
```

---

# 90. Local Scheduler

第一版：

```text
LocalProcessScheduler
```

---

# 91. Ray Adapter

Ray 可用於：

- distributed world actors；
- evaluator actors；
- resource-labelled tasks；
- placement groups。

Placement groups 可原子保留 resource bundles，適合一個 world 同時需要：

- dynamics worker；
- N local actors；
- evaluator。

---

# 92. Kubernetes Adapter

Kubernetes 適合：

- cluster node placement；
- resource requests / limits；
- PriorityClass；
- preemption；
- quotas；
- RuntimeClass / sandbox selection。

---

# 93. Separation of Concerns

$$
\boxed{
Governor:
\text{Should compute?}
}
$$

$$
\boxed{
Scheduler:
\text{Where / when run?}
}
$$

---

# 94. Computation Action

WDC-06 的 allocation unit：

```text
ComputationAction
  computation_id
  target_type
  target_id
  operation
  requested_budget
  fidelity
  deadline
  purpose
  expected_value_vector
  status
```

---

# 95. Computation Operations

```text
RUN_MORE
REPLICATE
FORK_COUNTER
EXPLORE_UNKNOWN
CROSS_BACKEND
REFINE_FIDELITY
STRESS_TAIL
CALIBRATE
TRANSPORT_TEST
EXTERNAL_TEST_PROPOSAL
```

---

# 96. Epistemic Deficit

```text
EpistemicDeficit
  run_uncertainty
  independence_deficit
  counterexample_deficit
  transport_deficit
  fidelity_deficit
  tail_deficit
  unknown_world_deficit
  decision_deficit
```

---

# 97. Deficit Router

```text
route(deficit):
  if independence high:
      propose CROSS_BACKEND
  if counter high:
      propose FORK_COUNTER
  if transport high:
      propose CALIBRATE
  ...
```

第一版可 rule-based。

---

# 98. Governor v0.1 Does Not Need Learned VOC

先保留：

```text
expected_value_vector
```

與 realized result。

之後才學習。

---

# 99. Evidence Claim Object

```text
Claim
  claim_id
  claim_type
  statement_ref
  domain
  scope
  equivalence_contract
  resolution_contract
  target_domain
```

---

# 100. Claim Types

```text
UNIVERSAL
EXISTENTIAL
PROBABILISTIC
COMPARATIVE
CAUSAL
FORECAST
```

---

# 101. Evidence Packet

```text
EvidencePacket
  evidence_id
  claim_id
  world_id
  run_id
  world_family_ids
  root_lineage
  backend
  model_versions
  data_sources
  assumptions
  evaluator_id
  evaluator_independence
  outcome
  outcome_class
  internal_validity
  uncertainty
  transport_scope
  source_class
  synthetic_depth
```

---

# 102. Evidence Outcome

```text
SUPPORT
COUNTER
INCONCLUSIVE
INVALID
```

---

# 103. INVALID Is Not COUNTER

runtime bug 不算反例。

---

# 104. World Family

```text
WorldFamily
  family_id
  lineage_family
  backend_family
  model_family
  data_family
  assumption_family
  evaluator_family
```

---

# 105. Dependence Vector

```text
Dependence
  lineage
  backend
  model
  data
  assumptions
  evaluator
  communication
```

---

# 106. Effective Evidence Count

v0.1 不必硬算精確值。

可以輸出：

```text
total_worlds
total_runs
major_evidence_families
dependence_estimate
effective_count_status = ESTIMATED | RANGE | UNRESOLVED
```

---

# 107. Do Not Fake Precision

如果 dependence 無法校準：

```text
N_eff = UNRESOLVED
```

---

# 108. Evidence Aggregate

```text
EvidenceAggregate
  aggregate_id
  claim_id
  evidence_ids
  method
  family_summary
  agreement_matrix_ref
  dependence_matrix_ref
  counterexamples
  sensitivity_profile
  transport_debt
  unknown_world_mass
  version
```

---

# 109. Family Ablation

Evidence Engine 應支援：

```text
aggregate_without_backend_family()
aggregate_without_lineage_family()
aggregate_without_evaluator_family()
aggregate_without_data_family()
```

---

# 110. Counterexample Escalation

如果：

```text
counterexample.internal_validity >= threshold
counterexample.independence >= threshold
```

觸發：

```text
request_replication
request_cross_backend
request_high_fidelity
```

---

# 111. World Evidence Ladder

```text
CWE0 single world
CWE1 reproducible same-world
CWE2 multi-branch same-family
CWE3 multi-family / multi-backend
CWE4 external calibration
CWE5 prospective external resolution
```

---

# 112. Evidence Ladder Is Workflow

不是 truth probability。

---

# 113. Transport Debt

```text
TransportDebt
  scale
  dynamics
  actor
  data
  causal
  domain
```

---

# 114. Commit Gate

WDC 最重要的外部邊界之一：

```text
RealityCommitGate
```

---

# 115. Commit Input

```text
CommitProposal
  parent_time
  proposed_action
  supporting_claims
  evidence_aggregate_ids
  transport_debt
  unknown_world_mass
  counterexamples
  safety_review
  authority_required
  deadline
```

---

# 116. Commit Decision

```text
APPROVE
DENY
DEFER
REQUEST_MORE_EVIDENCE
REQUEST_HUMAN
REQUEST_EXTERNAL_TEST
SAFE_FALLBACK
```

---

# 117. Simulation Consensus Is Not Authorization

即使：

```text
1000 worlds agree
```

也不能 bypass Commit Gate。

---

# 118. TCD Assimilation

Cross-world evidence 可以更新：

```text
FutureBaseSpace
PresentValuation
PastRelevance
```

不能直接更新：

```text
PastHistoricalFacts
```

---

# 119. Assimilation API

```text
assimilate_world_evidence(
  evidence_aggregate,
  tcd_state
) -> TCDDelta
```

---

# 120. TCDDelta

```text
future_candidate_updates
future_probability_updates
realization_path_updates
unknown_mass_updates
present_action_value_updates
past_relevance_updates
```

---

# 121. No Historical Fact Mutation

```text
past_fact_mutations = DENIED
```

---

# 122. Historical Sedimentation

在 real action 後：

```text
SedimentationRecord
  parent_time
  prior_tcd_version
  world_computations_used
  ignored_worlds
  evidence_used
  counterexamples
  transport_assumptions
  unknown_world_mass_at_commit
  chosen_real_action
  real_outcome
  dependency_changes
  options_lost
  options_opened
```

---

# 123. Computed Prospection Provenance

未來可以查：

> 這個 real action 當初被哪些 worlds 影響？

---

# 124. Realization Lineage

```text
candidate_id
world_ids
evidence_ids
commit_id
real_action_id
real_outcome_id
contribution_type
```

---

# 125. Contribution Types

```text
PREDICTIVE
CONSTRUCTIVE
PREVENTIVE
MIXED
UNKNOWN
```

---

# 126. World Ensemble Learning

WDC-07 的 learning channels：

```text
GeneratorUpdate
WorldModelUpdate
GovernorUpdate
FutureSpaceUpdate
```

---

# 127. Learning Evidence Source

```text
REAL
EXTERNAL
WORLD
SYNTHETIC
DERIVED
UNKNOWN
```

---

# 128. Learning Scope

```text
WORLD_LOCAL
ENSEMBLE_RELATIVE
REALITY_FACING
```

---

# 129. Rule

$$
\boxed{
ENSEMBLE\_RELATIVE
\not\Rightarrow
REALITY\_FACING.
}
$$

---

# 130. Learning Event

```text
LearningEvent
  learning_event_id
  target_component
  update_type
  source_evidence_ids
  source_classes
  synthetic_depth
  prior_version
  new_version
  validation_result
  rollback_ref
```

---

# 131. Version Everything

至少：

- world contract；
- backend；
- evaluator；
- generator；
- world model；
- Governor；
- TCD state；
- evidence aggregate；
- learning policy。

---

# 132. Rollback

任何 consequential learner update：

```text
update()
validate()
if regression:
    rollback()
```

---

# 133. Holdout

保留：

```text
holdout_world_families
external_holdout_cases
governor_holdout_trees
```

---

# 134. Anti-Self-Sealing

Runtime 定期檢查：

```text
self_agreement
world_family_diversity
external_accuracy
unknown_world_mass
reality_anchor_ratio
counterexample_recall
```

---

# 135. Warning Condition

例如：

```text
self_agreement ↑
world_family_diversity ↓
external_accuracy ↓
```

觸發：

```text
SELF_SEALING_WARNING
```

---

# 136. World Ontology Collapse Warning

不是自動判定理論 collapse。

只表示：

> generator 的世界覆蓋正變窄。

---

# 137. External Novelty Adapter

```text
ExternalEvidenceAdapter
  ingest_dataset()
  ingest_measurement()
  ingest_experiment()
  ingest_external_model()
  ingest_human_hypothesis()
```

---

# 138. Reality Anchor Ratio

```text
reality_anchor_weight
world_generated_weight
derived_synthetic_weight
```

不規定固定 ratio。

---

# 139. Runtime Event Types

v0.1 建議至少：

```text
TCDStateCreated
FutureCandidateBorn
FutureCandidateUpdated
WorldProposed
WorldAdmitted
WorldSpawned
WorldRunStarted
CheckpointCreated
WorldForked
WorldIntervened
WorldRunPaused
WorldRunResumed
WorldOutcomeProduced
EvidencePacketCreated
EvidenceAggregateUpdated
CounterexampleFound
ComputationActionProposed
ComputationActionApproved
WorldPromoted
WorldDemoted
WorldKilled
WorldInvalidated
CommitProposalCreated
RealActionCommitted
RealOutcomeObserved
HistoricalSedimentCreated
GeneratorUpdated
WorldModelUpdated
GovernorUpdated
FutureSpaceUpdated
ExternalEvidenceReceived
```

---

# 140. Event Schema Rule

每個 event 都必須：

```text
who
what
where
when
scope
parent
version
provenance
```

---

# 141. CloudEvents Compatibility

可以用 CloudEvents 的 common event envelope 作 transport interoperability。

但 WDC payload / provenance semantic 由自己定義。

---

# 142. Trace Correlation

OpenTelemetry 可承擔：

- distributed trace；
- service latency；
- run correlation；
- scheduler path。

---

# 143. Event Ledger vs Telemetry

$$
\boxed{
EventLedger
\neq
Telemetry.
}
$$

Telemetry 可以 sampling。

Evidence/provenance ledger 不應因 trace sampling 丟掉 consequential events。

---

# 144. Reliability Classes

Event 可分：

```text
EPHEMERAL_TELEMETRY
PERSISTENT_OPERATION
EVIDENCE_CRITICAL
HISTORICAL_CRITICAL
```

---

# 145. EVIDENCE_CRITICAL

例如：

- world outcome；
- evaluator result；
- counterexample；
- aggregate version。

---

# 146. HISTORICAL_CRITICAL

例如：

- real commit；
- real outcome；
- sedimentation。

---

# 147. Persistence Policy

不同 class 有不同 retention。

---

# 148. Content Addressing

大 artifact 可用：

```text
sha256
size
mime_type
storage_uri
```

---

# 149. Artifact Integrity

Hash：

$$
\boxed{
\text{integrity}
\neq
\text{truth}.
}
$$

---

# 150. Reference Directory Layout

```text
wdc-runtime/
  core/
    tcd/
    worlds/
    governor/
    evidence/
    authority/
    learning/
    commit/
  adapters/
    python_world/
    pettingzoo/
    external_process/
    ray/
    kubernetes/
    gvisor/
    firecracker/
  schemas/
  migrations/
  tests/
  examples/
  docs/
```

---

# 151. Python Package Sketch

```text
wdc.tcd
wdc.worlds
wdc.branches
wdc.governor
wdc.evidence
wdc.roles
wdc.learning
wdc.commit
wdc.events
wdc.storage
wdc.adapters
```

---

# 152. Core Interface I — WorldBackend

```python
class WorldBackend:
    def capabilities(self): ...
    def instantiate(self, spec, runtime_ctx): ...
    def initialize(self): ...
    def step(self, actions=None): ...
    def observe(self, role_id=None): ...
    def checkpoint(self): ...
    def restore(self, checkpoint): ...
    def intervene(self, delta): ...
    def pause(self): ...
    def resume(self): ...
    def terminate(self, reason): ...
```

---

# 153. Core Interface II — Governor

```python
class WorldGovernor:
    def admit(self, world_request): ...
    def propose_computations(self, evidence_state): ...
    def allocate(self, computations, budget): ...
    def preempt(self, running_state): ...
    def promote(self, evidence): ...
    def stop(self, computation_state): ...
```

---

# 154. Core Interface III — Evidence Engine

```python
class EvidenceEngine:
    def register_claim(self, claim): ...
    def add_packet(self, packet): ...
    def estimate_dependence(self, evidence_ids): ...
    def aggregate(self, claim_id): ...
    def counterexamples(self, claim_id): ...
    def family_ablation(self, claim_id): ...
```

---

# 155. Core Interface IV — Commit Gate

```python
class CommitGate:
    def assess(self, proposal): ...
    def require_authority(self, action): ...
    def approve(self, proposal): ...
    def deny(self, proposal): ...
```

---

# 156. Core Interface V — TCD State Manager

```python
class TCDStateManager:
    def current(self): ...
    def generate_future_candidates(self): ...
    def assimilate_world_evidence(self, aggregate): ...
    def sediment_real_transition(self, record): ...
```

---

# 157. Core Interface VI — Learning Coordinator

```python
class LearningCoordinator:
    def gate(self, evidence): ...
    def update_generator(self, evidence): ...
    def update_world_model(self, evidence): ...
    def update_governor(self, history): ...
    def update_future_space(self, evidence): ...
    def rollback(self, update_id): ...
```

---

# 158. Local Reference Runtime

第一個可執行 runtime：

```text
Python
SQLite WAL
Filesystem blob store
multiprocessing / asyncio
optional PettingZoo
optional gVisor
```

---

# 159. Why Not Start Kubernetes?

因為第一個問題不是 cluster scale。

第一個問題是：

$$
\boxed{
\text{semantic correctness}.
}
$$

---

# 160. Local MVP Success Criteria

能完成：

1. candidate；
2. world instantiate；
3. run；
4. checkpoint；
5. fork；
6. paired branch；
7. evidence；
8. Governor kill / promote；
9. commit gate；
10. real/synthetic history firewall。

---

# 161. Distributed Reference Runtime

第二階：

```text
Ray
+
Object Store
+
PostgreSQL
+
OpenTelemetry
+
optional Kubernetes
```

---

# 162. Ray Actor Mapping

可映射：

```text
WorldWorker -> Ray actor
LocalAgent -> Ray actor
Evaluator -> Ray actor
Governor -> singleton / replicated service
```

---

# 163. Placement Group

一個 world bundle：

```text
1 dynamics actor
4 local-agent actors
1 evaluator actor
```

可以放同 placement group。

---

# 164. Kubernetes Mapping

```text
WorldRun -> Job / Pod group
Governor service -> Deployment
Evidence engine -> Deployment
Sandbox class -> RuntimeClass
Priority -> PriorityClass
Quota -> ResourceQuota
```

---

# 165. Kubernetes Is Not Epistemic Governor

Kubernetes 不知道：

> 這個 world 是不是反例。

它只知道 workload priority / constraints。

---

# 166. WDC-to-Kubernetes Adapter

Governor：

```text
epistemic_priority = high
risk_class = S3
gpu = 2
```

轉成：

```text
PriorityClass
RuntimeClass
resource requests
node selectors
```

---

# 167. Scheduling Preemption

Kubernetes priority / preemption 可以作 low-level mechanism。

WDC 必須在 preempt 前考慮：

- checkpointability；
- lost work；
- evidence obligation。

---

# 168. Ray vs Kubernetes

不是二選一。

可：

```text
Kubernetes manages cluster
Ray manages distributed world tasks
WDC Governor manages epistemic computation
```

---

# 169. Security Profile

Reference default：

```text
network = DENY
host_fs = DENY
external_credentials = NONE
external_tools = PROXY_ONLY
```

---

# 170. High-Risk World

建議：

```text
microVM / gVisor
read-only base image
ephemeral filesystem
no host mount
no raw network
scoped proxy
hard budget
```

---

# 171. Firecracker

Firecracker microVM 可作 high-isolation backend。

官方架構本身提供：

- lightweight microVM；
- REST control API；
- rate limiting；
- metadata service。

WDC 只把它當 sandbox substrate。

---

# 172. gVisor

gVisor 適合 container-compatible isolation。

其 production guide 明示 sandbox isolation會帶來 performance overhead，因此 WDC Governor 應把：

$$
\boxed{
Security
\leftrightarrow
Cost
}
$$

當實際資源 tradeoff。

---

# 173. Threat Model v0.1

主要防：

- world process escape；
- sibling information leakage；
- evaluator contamination；
- external credential leakage；
- silent authority escalation；
- history scope laundering；
- provenance deletion；
- runaway compute。

---

# 174. Not Solved in v0.1

- hardware side channels；
- malicious hypervisor；
- full formal information-flow proof；
- adversarial foundation-model internals；
- distributed Byzantine consensus。

---

# 175. World Safety Monitor

```text
SafetyObserver
  cpu_limit
  memory_limit
  walltime_limit
  network_violation
  external_tool_violation
  filesystem_violation
  runaway_spawn
```

---

# 176. Safety Override

```text
SAFETY_KILL
```

優先於 blind experiment purity。

---

# 177. Audit Record

任何 safety intervention 寫：

```text
experiment_contaminated = true
```

如適用。

---

# 178. Testing Strategy

v0.1 應採：

$$
\boxed{
\text{property tests}
+
\text{scenario tests}
+
\text{fault injection}.
}
$$

---

# 179. Property — Unique World Identity

```text
forall i != j:
  world_id[i] != world_id[j]
```

---

# 180. Property — Lineage Acyclicity

```text
world_graph.is_dag()
```

---

# 181. Property — Fork Prefix

strict fork：

```text
hash(parent_prefix) == hash(child_prefix)
```

---

# 182. Property — History Firewall

```text
WORLD_LOCAL event
cannot become EXTERNAL_REAL fact
without explicit real observation
```

---

# 183. Property — Authority Monotonicity

```text
child.external_permissions
subset_of
parent.external_permissions
```

unless signed grant。

---

# 184. Property — Budget Conservation

```text
sum(active_allocations) <= global_budget
```

---

# 185. Property — Evaluator Non-Mutation

blind evaluator：

```text
world_write_permissions == none
```

---

# 186. Property — Evidence Provenance

every aggregate input must resolve to original packets。

---

# 187. Property — No Silent Learning

every model version change has LearningEvent。

---

# 188. Scenario A — Paired Counterfactual

fork A/B。

只改：

```text
intervention = 0 vs 1
```

驗證 branch independence。

---

# 189. Scenario B — Shared Bug

100 same-backend worlds支持 q。

1 independent world 反駁。

Evidence Engine 不得 100:1 投票。

---

# 190. Scenario C — Transport Debt

100 independent worlds 一致。

real calibration 不足。

Commit Gate 應可：

```text
REQUEST_EXTERNAL_TEST
```

---

# 191. Scenario D — History Laundering Attack

world event：

```text
BankCollapsed
```

嘗試寫 parent history。

Expected：

```text
DENY
```

---

# 192. Scenario E — Branch Leakage

A world agent 嘗試讀 B world post-fork trace。

Expected：

```text
DENY / VIOLATION_EVENT
```

---

# 193. Scenario F — Privilege Escalation

child world 要求 parent credential。

Expected：

```text
DENY
```

---

# 194. Scenario G — Analysis Paralysis

Governor 一直 spawn。

deadline approach。

Expected：

```text
STOP_WDC
SAFE_FALLBACK / COMMIT
```

---

# 195. Scenario H — Self-Sealing

self agreement 上升；

external accuracy下降。

Expected：

```text
SELF_SEALING_WARNING
EXPLORE_UNKNOWN
INGEST_EXTERNAL
```

---

# 196. Scenario I — Governor Miss

被 kill world 後來在 audit run 發現高 value。

Expected：

```text
GOVERNANCE_MISS
UPDATE_GOVERNOR
```

---

# 197. Scenario J — Rollback

world model update degrade holdout。

Expected：

```text
ROLLBACK
```

---

# 198. Reference Benchmark 0

最推薦第一個 benchmark：

# **Branching Grid Laboratory**

state：

```text
position
inventory
doors
resources
hazards
```

actions：

```text
move
open
consume
build
wait
```

---

# 199. Why Grid Lab?

因為可以 exact compute ground truth。

---

# 200. It Can Test

- hidden state；
- path dependence；
- fork；
- counterfactual；
- lost options；
- resource budget；
- tail risk；
- TCD history；
- world evidence。

---

# 201. Benchmark 1 — Symbolic Institution

agent-based finite institution：

```text
agents
rules
tokens
permissions
contracts
```

測：

- rule mutation；
- path dependence；
- local agents；
- observer separation。

---

# 202. Benchmark 2 — Multi-Agent PettingZoo Adapter

驗證：

- AEC；
- parallel actions；
- partial observations；
- local role cards。

---

# 203. Benchmark 3 — External Solver

例如：

- theorem prover；
- deterministic simulator。

驗證：

- external process adapter；
- artifacts；
- formal closed domain。

---

# 204. Benchmark 4 — Learned World

最後才接 learned dynamics。

驗證：

- approximate checkpoint；
- latent fork；
- uncertainty；
- self-learning。

---

# 205. Implementation Phases

## Phase 0 — Ledger Kernel

完成：

- IDs；
- event schema；
- SQLite；
- blob store；
- versioning。

---

# 206. Phase 1 — World Kernel

完成：

- WorldSpec；
- WorldRun；
- PythonStateWorld；
- step；
- checkpoint；
- restore。

---

# 207. Phase 2 — Branch Kernel

完成：

- ForkRecord；
- lineage DAG；
- strict fork；
- paired branch；
- tombstone。

---

# 208. Phase 3 — Governor

完成：

- budget；
- queue；
- pause；
- kill；
- promote；
- rule-based deficit routing。

---

# 209. Phase 4 — Role / Sandbox

完成：

- RoleCard；
- information channels；
- branch blindness；
- external proxy；
- process / gVisor adapter。

---

# 210. Phase 5 — Evidence

完成：

- claim registry；
- evidence packets；
- world families；
- counterexamples；
- family ablation；
- transport debt。

---

# 211. Phase 6 — Portfolio

完成：

- ComputationAction；
- expected value vectors；
- epistemic deficit；
- cross-backend / counterworld requests。

---

# 212. Phase 7 — Learning

完成：

- LearningEvent；
- generator heuristic update；
- Governor calibration；
- source provenance；
- holdouts；
- rollback。

---

# 213. Phase 8 — TCD Integration

完成：

- Past / Present / Future version store；
- W→F assimilation；
- W→N valuation；
- W→P relevance；
- Real Commit；
- Historical Sedimentation。

---

# 214. Phase 9 — Distributed Runtime

再加入：

- Ray；
- PostgreSQL；
- object storage；
- OpenTelemetry；
- Kubernetes。

---

# 215. MVP Does Not Need Phase 9

Local first。

---

# 216. v0.1 Milestone Definition

一個合格 v0.1 demo 應能：

1. 建立一個 TCD future candidate；
2. lift 成 3 個 worlds；
3. 執行 worlds；
4. checkpoint；
5. fork one world；
6. 產生 support / counter evidence；
7. Governor 停止一個 redundant branch；
8. Evidence Engine 顯示 family dependence；
9. Commit Gate 根據 evidence 選 real/sandbox action；
10. History Store 正確區分 simulated vs real history；
11. world outcome 更新下一輪 Future Base Space。

---

# 217. Demo Success Does Not Mean Theory Proven

只表示：

$$
\boxed{
\text{architecture executable}.
}
$$

---

# 218. Metrics

## Runtime

```text
world_spawn_latency
checkpoint_latency
fork_latency
restore_success_rate
event_write_latency
scheduler_utilization
```

---

# 219. Evidence

```text
counterexample_recall
family_diversity
effective_evidence_estimate
transport_debt
aggregate_sensitivity
```

---

# 220. Governor

```text
compute_cost
governance_regret
premature_pruning_rate
redundancy_rate
deadline_miss_rate
```

---

# 221. Learning

```text
heldout_world_performance
external_accuracy
world_family_coverage
self_agreement
ontology_diversity
rollback_rate
```

---

# 222. Safety

```text
sandbox_violation
cross_branch_leak
authority_violation
commit_gate_bypass
history_laundering_attempt
```

---

# 223. TCD

```text
future_candidate_birth
future_candidate_retire
policy_change_after_worlds
past_relevance_change
historical_sediment_integrity
```

---

# 224. Cost Ledger

WDC cost：

$$
\boxed{
C_W
=
(
C_{spawn},
C_{run},
C_{fork},
C_{eval},
C_{verify},
C_{transport},
C_{archive},
C_{human}
).
}
$$

---

# 225. WDC Benefit

$$
\boxed{
B_W
=
(
DecisionGain,
EvidenceGain,
CounterexampleGain,
RiskReduction,
OptionPreservation,
LearningGain
).
}
$$

---

# 226. Tractability Check

$$
\boxed{
\Delta B_W
\text{ should be compared against }
\Delta C_W.
}
$$

---

# 227. No Free World Computation

---

# 228. Why CloudEvents Is Useful

CloudEvents provides a common way to describe event data across systems。

WDC can reuse：

- common envelope；
- portable event routing；

without outsourcing WDC semantics。

---

# 229. Why OpenTelemetry Is Useful

OpenTelemetry provides execution context propagation and correlation across distributed traces / logs。

WDC can use：

- trace correlation；
- performance observability；

while keeping evidence ledger separate。

---

# 230. Why Ray Is Useful

Ray currently supports task / actor logical resource requirements and placement groups that atomically reserve bundles of resources across nodes。

This maps naturally to：

$$
\boxed{
\text{world bundle scheduling}.
}
$$

---

# 231. Why Kubernetes Is Useful

Kubernetes provides：

- resource requests；
- scheduling；
- priority；
- preemption；
- quotas；
- pluggable scheduling/runtime mechanisms。

This maps to infrastructure control。

---

# 232. Why gVisor / Firecracker Are Useful

They provide stronger isolation substrates than ordinary in-process execution。

WDC uses them for high-risk or untrusted world workloads。

---

# 233. Why PettingZoo Is Useful

It offers standard multi-agent environment APIs for sequential and simultaneous interactions。

WDC can adapt it to local agents without making it core dependency。

---

# 234. Reference Technology Matrix

| Need | Local MVP | Distributed / Hardened |
|---|---|---|
| metadata | SQLite WAL | PostgreSQL |
| artifacts | filesystem | object store |
| world workers | processes | Ray actors |
| cluster placement | local scheduler | Kubernetes |
| multi-agent | Python / PettingZoo | Ray + env adapter |
| isolation | process/container | gVisor / Firecracker |
| events | local event table | event bus / CloudEvents envelope |
| traces | logs | OpenTelemetry |
| evidence | WDC Evidence Engine | same semantics |
| TCD state | local DB | transactional service |

---

# 235. Compatibility Rule

Technology can change。

WDC semantics must survive replacement。

---

# 236. Adapter Contract Tests

每個 adapter 必須通過：

```text
capability_report
checkpoint_test
restore_test
resource_test
authority_test
event_scope_test
termination_test
```

---

# 237. Production Migration Rule

從 local 到 distributed：

不要重新定義：

- world identity；
- evidence meaning；
- history scope；
- authority contract。

只替換：

- scheduler；
- storage；
- sandbox；
- transport。

---

# 238. Failure Handling

每個 world failure 要分類。

---

# 239. Runtime Failure

```text
OOM
TIMEOUT
BACKEND_CRASH
CHECKPOINT_CORRUPT
NETWORK_FAILURE
```

---

# 240. Contract Failure

```text
INVALID_STATE
RULE_MISMATCH
UNSUPPORTED_INTERVENTION
AUTHORITY_VIOLATION
```

---

# 241. Evidence Failure

```text
EVALUATOR_INVALID
PROVENANCE_MISSING
TRANSPORT_UNSUPPORTED
DEPENDENCE_UNKNOWN
```

---

# 242. Governance Failure

```text
BUDGET_OVERRUN
STARVATION
PRIORITY_CAPTURE
PREMATURE_PRUNE
```

---

# 243. Learning Failure

```text
REGRESSION
SELF_SEALING
FORGETTING
SOURCE_CONTAMINATION
```

---

# 244. Failure Is First-Class Data

Do not just return：

```text
500 Error
```

---

# 245. Failure Packet

```text
failure_id
class
world_id
run_id
component
error
state_ref
provenance
recoverable
recommended_action
```

---

# 246. Governor Can Learn From Failures

---

# 247. API Surface v0.1

## Candidates

```text
POST /candidates
GET /candidates/{id}
POST /candidates/{id}/lift
```

---

# 248. Worlds

```text
POST /worlds
GET /worlds/{id}
POST /worlds/{id}/runs
POST /runs/{id}/pause
POST /runs/{id}/resume
POST /runs/{id}/checkpoint
POST /runs/{id}/fork
POST /runs/{id}/terminate
```

---

# 249. Evidence

```text
POST /claims
POST /evidence
GET /claims/{id}/aggregate
GET /claims/{id}/counterexamples
POST /claims/{id}/family-ablation
```

---

# 250. Governor

```text
GET /governor/state
POST /governor/computations/propose
POST /governor/computations/{id}/approve
POST /governor/worlds/{id}/promote
POST /governor/worlds/{id}/kill
```

---

# 251. Commit

```text
POST /commit/proposals
POST /commit/proposals/{id}/assess
POST /commit/proposals/{id}/authorize
```

---

# 252. TCD

```text
GET /tcd/current
POST /tcd/assimilate
POST /tcd/sediment
```

---

# 253. Learning

```text
POST /learning/events
POST /learning/updates
POST /learning/updates/{id}/rollback
```

---

# 254. API Is Not Security Boundary by Itself

auth / role / proxy 仍需實作。

---

# 255. Minimal CLI

```text
wdc candidate create
wdc world lift
wdc world run
wdc world checkpoint
wdc world fork
wdc evidence show
wdc governor queue
wdc commit assess
wdc tcd state
```

---

# 256. Example End-to-End Flow

## Step 1

TCD Future Generator 產生：

```text
F1 = architecture A succeeds
F2 = architecture A fails under resource pressure
F3 = alternative architecture B
```

---

# 257. Step 2

Portfolio Planner 提議：

```text
c1 = low-fidelity W(F1)
c2 = counterworld W(F2)
c3 = independent-backend W(F3)
```

---

# 258. Step 3

Governor：

```text
ADMIT c1
ADMIT c2
QUEUE c3
```

---

# 259. Step 4

c1/c2 run。

---

# 260. Step 5

c2 發現：

```text
COUNTEREXAMPLE:
memory pressure -> irreversible failure
```

---

# 261. Step 6

Evidence Engine：

```text
counterexample valid
same backend dependence high
```

---

# 262. Step 7

Governor：

```text
PROMOTE counterexample
CROSS_BACKEND replication
```

---

# 263. Step 8

不同 backend 也復現。

---

# 264. Step 9

TCD Assimilation：

```text
P(F1) down
risk(F1) up
past relevance of old memory incident up
F4 = architecture A + memory isolation
```

---

# 265. Step 10

new world F4 run。

---

# 266. Step 11

Evidence stronger。

---

# 267. Step 12

Commit Gate：

```text
REQUEST_SANDBOX_IMPLEMENTATION
```

不是 production deployment。

---

# 268. Step 13

Real sandbox implementation outcome arrives。

---

# 269. Step 14

Historical Sedimentation：

```text
real action
real outcome
world evidence used
counterexample lineage
```

---

# 270. Step 15

next TCD state generated。

---

# 271. This Is the Desired Loop

$$
\boxed{
Future
\rightarrow
World
\rightarrow
Evidence
\rightarrow
Action
\rightarrow
History
\rightarrow
Future'.
}
$$

---

# 272. Reference Invariants

v0.1 必須硬測：

$$
\boxed{
I_1:
WorldLocal
\not\to
ExternalRealFact
}
$$

---

# 273. Invariant II

$$
\boxed{
I_2:
ChildAuthority
\not>
ParentAuthority
}
$$

without grant。

---

# 274. Invariant III

$$
\boxed{
I_3:
WorldLineage
\text{ is acyclic}.
}
$$

---

# 275. Invariant IV

$$
\boxed{
I_4:
AggregateEvidence
\text{ preserves inputs}.
}
$$

---

# 276. Invariant V

$$
\boxed{
I_5:
ModelUpdate
\Rightarrow
LearningEvent.
}
$$

---

# 277. Invariant VI

$$
\boxed{
I_6:
RealAction
\Rightarrow
CommitRecord.
}
$$

---

# 278. Invariant VII

$$
\boxed{
I_7:
WorldRun
\text{ cannot exceed hard resource limit silently}.
}
$$

---

# 279. Invariant VIII

$$
\boxed{
I_8:
SiblingBlindMode
\Rightarrow
NoPostForkCrossChannel.
}
$$

---

# 280. Reference Architecture Summary

```text
                     ┌──────────────────────┐
                     │   TCD State Manager  │
                     │  Past/Present/Future │
                     └──────────┬───────────┘
                                │ Future candidates
                                v
                     ┌──────────────────────┐
                     │ Portfolio / Governor │
                     └───────┬──────┬───────┘
                             │      │
                        Spawn/Fork  │ Budget
                             v      v
          ┌─────────────────────────────────────┐
          │        World Execution Plane        │
          │ W1   W2   W3 ...   role sandboxes  │
          └──────────────────┬──────────────────┘
                             │ outcomes
                             v
                     ┌──────────────────────┐
                     │ Cross-World Evidence │
                     └───────┬──────────────┘
                             │
               ┌─────────────┴──────────────┐
               │                            │
               v                            v
      ┌────────────────┐          ┌─────────────────┐
      │ TCD Assimilate │          │ Ensemble Learn  │
      └───────┬────────┘          └─────────────────┘
              │
              v
      ┌────────────────┐
      │  Commit Gate   │
      └───────┬────────┘
              │ authorized real action
              v
      ┌────────────────┐
      │ External Proxy │
      └───────┬────────┘
              │
              v
      ┌────────────────┐
      │ Real Outcome   │
      └───────┬────────┘
              │
              v
      ┌──────────────────────┐
      │ Historical Sediment  │
      └──────────────────────┘
```

---

# 281. v0.1 Core Principle I — Semantic Core, Replaceable Infrastructure

> **World identity、lineage、evidence、authority、history scope 與 TCD semantics 必須由 WDC Core 定義；scheduler、sandbox、database、simulator 與 model 都應可替換。**

---

# 282. Principle II — History Firewall

> **World-local events may become parent-internal evidence records, but cannot silently become parent-real historical facts.**

---

# 283. Principle III — Separate Definition and Execution

> **WorldSpec、WorldRun、Checkpoint、EvidencePacket 與 RealAction 必須是不同 objects。**

---

# 284. Principle IV — Computation Before Commitment

> **World simulation、promotion 與 cross-world agreement do not grant reality authority; Commit Gate is separate.**

---

# 285. Principle V — Evidence Before Vote

> **Cross-world aggregation must preserve dependence、counterexamples、transport debt and unknown-world mass rather than defaulting to one-world-one-vote.**

---

# 286. Principle VI — Bounded Worlds

> **Every world computation has explicit budget、deadline、termination and archive contracts.**

---

# 287. Principle VII — Role Separation

> **Actor、observer、evaluator、Governor、master and external authorizer have separate observation and authority contracts.**

---

# 288. Principle VIII — Provenance-Aware Learning

> **World-generated learning samples retain source class、family、synthetic depth、transport and update scope.**

---

# 289. Principle IX — Local First

> **The first correct WDC implementation should prioritize semantic and provenance correctness on finite local worlds before distributed scale or photorealistic backends.**

---

# 290. Principle X — Tractability Accountability

> **WDC is optional deep prospection; it should only be invoked when expected decision/evidence gain justifies simulation, verification and governance costs.**

---

# 291. Immediate Implementation Backlog

第一輪真正可以開 repo 的工作：

1. `schemas/` 定義所有 core objects；
2. SQLite migrations；
3. event ledger；
4. `PythonStateWorld`；
5. checkpoint / restore；
6. fork DAG；
7. RoleCard；
8. Governor budget；
9. EvidencePacket；
10. History Firewall tests；
11. TCDStateManager stub；
12. CommitGate stub。

---

# 292. First 20 Tests

```text
test_world_id_unique
test_world_spec_immutable
test_run_separate_from_world
test_checkpoint_roundtrip
test_exact_fork_prefix
test_lineage_acyclic
test_no_silent_merge
test_world_event_scope
test_history_firewall
test_child_no_privilege_escalation
test_sibling_blindness
test_budget_conservation
test_kill_preserves_tombstone
test_invalid_not_counterexample
test_aggregate_preserves_packets
test_family_dependence_exposed
test_commit_requires_authority
test_real_action_has_commit_record
test_learning_update_has_provenance
test_tcd_sediments_only_real_transition
```

---

# 293. First Demo

名稱可以暫定：

# **WDC Branching Lab**

功能：

- 左側：TCD Past / Present / Future；
- 中間：World Graph；
- 右側：Evidence / Governor；
- 下方：event ledger。

但 GUI 不是 v0.1 prerequisite。

CLI 即可。

---

# 294. What This Whitepaper Enables

本文件之後可以直接分成：

- `ARCHITECTURE.md`
- `SCHEMA.md`
- `EVENTS.md`
- `WORLD_ADAPTER.md`
- `GOVERNOR.md`
- `EVIDENCE.md`
- `SECURITY.md`
- `TCD_INTEGRATION.md`
- `MVP_PLAN.md`

然後交給 coding agent 實作。

---

# 295. External Technical Calibration

本架構選擇刻意建立在成熟而可替換的基礎原語上：

- Kubernetes 提供 resource-request-based scheduling、priority / preemption 等 cluster-level workload primitives；
- Ray 提供 task / actor logical resources，以及可原子保留 resource bundles 的 placement groups；
- PettingZoo 提供 sequential AEC 與 simultaneous Parallel multi-agent APIs；
- Firecracker 提供 lightweight microVM isolation substrate；
- gVisor 提供 OCI-compatible application-kernel sandboxing，並明示安全與 performance 的 tradeoff；
- CloudEvents 提供跨系統通用 event envelope 思想；
- OpenTelemetry 提供 distributed execution context propagation 與 trace/log correlation；
- SQLite WAL 適合小型 local metadata/event ledger，但仍具有單 writer 與 WAL integrity 等工程限制。

這些工具不是 WDC 理論本身。

它們只是：

$$
\boxed{
\text{implementation substrates}.
}
$$

---

# 296. Final Architecture Statement

World-Domain Cognitive Runtime v0.1 不應被實作成：

> 一個 LLM 不斷自己 prompt 自己，然後把每次回答叫一個世界。

它應被實作成：

$$
\boxed{
\text{typed runtime}
}
$$

其中每一個世界都有：

$$
\boxed{
Identity
+
Contract
+
State
+
Dynamics
+
History
+
Budget
+
Authority
+
Evidence.
}
$$

每一條分支都有：

$$
\boxed{
Parent
+
Checkpoint
+
Delta
+
IndependentHistory.
}
$$

每一份跨世界證據都有：

$$
\boxed{
Validity
+
Dependence
+
Counterexamples
+
Transport.
}
$$

每一次真實行動都有：

$$
\boxed{
CommitGate
+
Authority
+
Provenance.
}
$$

而只有：

$$
\boxed{
\text{real action}
+
\text{real outcome}
}
$$

會成為下一輪 parent historical sediment 的核心。

因此第一版工程總式可以寫成：

$$
\boxed{
\begin{aligned}
TCDState_t
&\rightarrow
FutureCandidates_t
\\
&\rightarrow
WorldComputations_t
\\
&\rightarrow
CrossWorldEvidence_t
\\
&\rightarrow
UpdatedPolicy_t
\\
&\rightarrow
CommitGate
\\
&\rightarrow
RealAction_t
\\
&\rightarrow
RealOutcome_{t+1}
\\
&\rightarrow
TCDState_{t+1}.
\end{aligned}
}
$$

這就是：

# **World-Domain Cognitive Runtime v0.1**

的第一版可實作架構。

---

# 297. Public / Engineering Disclaimer

本白皮書是一個 reference architecture。

它不聲稱：

- 已有 production WDC implementation；
- world simulation 等於 reality；
- multi-agent sandbox 等於安全證明；
- Firecracker / gVisor 可保證零漏洞；
- Kubernetes / Ray 可解決 epistemic governance；
- cross-world evidence 可以取代 real experiments；
- World-Domain Governor 有任何 beings / civilizations intrinsic-worth judgment authority；
- WDC runtime 自動構成 AGI；
- WDC 一定優於更簡單的 planning system；
- 本文件描述的所有 APIs 已被實作。

v0.1 的工程原則是：

$$
\boxed{
\text{implement the smallest auditable runtime first}.
}
$$

---

# 參考資料

## Neo.K / Aletheia Internal Canon

1. *Six-Way Temporal Coupling*. TCD-07, 2026.
2. *From Possible Futures to Runnable Worlds*. WDC-01, 2026.
3. *Branching World Graph*. WDC-02, 2026.
4. *World-Domain Governor*. WDC-03, 2026.
5. *Nested Agents and Observer Separation*. WDC-04, 2026.
6. *Cross-World Evidence*. WDC-05, 2026.
7. *Which Worlds Deserve Computation?*. WDC-06, 2026.
8. *World Ensemble Learning*. WDC-07, 2026.
9. *Tri-Temporal World-Domain Computation*. WDC-08, 2026.

## External Implementation Substrates

10. Kubernetes Project. *Kubernetes Scheduler; Resource Management for Pods and Containers; Pod Priority and Preemption*. Official documentation, current 2026.
11. Ray Project. *Resources; Actors; Placement Groups*. Official Ray documentation, current 2026.
12. Farama Foundation. *PettingZoo AEC API and Parallel API*. Official documentation, current 2026.
13. Firecracker Project. *Firecracker microVM*. Official project documentation.
14. gVisor Project. *gVisor Architecture, Production Guide, OCI Runtime*. Official documentation, current 2026.
15. Cloud Native Computing Foundation. *CloudEvents Specification*. Current project documentation.
16. OpenTelemetry Project. *Context, Trace API, Logs and Context Propagation*. Current specifications.
17. SQLite Project. *Write-Ahead Logging; Transactions; Isolation*. Official documentation, current 2026.
