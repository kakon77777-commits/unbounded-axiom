---
title: "勤人 AI 政治／經濟情報執行環境：持續攝取、Agent 編排、反證、預測、暴露傳播與治理閉環"
english_title: "Diligent AI Political/Economic Intelligence Runtime: Continuous Ingestion, Agent Orchestration, Counterevidence, Forecasting, Exposure Propagation, and Governance Loops"
series: "AI-Native Longitudinal Actor Intelligence"
author: "Neo.K"
institution: "EveMissLab／一言諾科技有限公司"
artifact: "Technical Whitepaper 02"
version: "v0.1"
date: "2026-08-28"
language: "zh-TW"
status: "Canonical Runtime Whitepaper / UTF-8 Source"
runtime_scope: "Defines the continuous runtime operating model built on WP01 canonical architecture. It does not authorize autonomous political persuasion, sensitive voter targeting, unlawful surveillance, or automated financial trading."
---

# 勤人 AI 政治／經濟情報執行環境：持續攝取、Agent 編排、反證、預測、暴露傳播與治理閉環

**Diligent AI Political/Economic Intelligence Runtime: Continuous Ingestion, Agent Orchestration, Counterevidence, Forecasting, Exposure Propagation, and Governance Loops**

**AI-Native Longitudinal Actor Intelligence — Technical Whitepaper 02**

---

## 摘要

WP01 定義了 Temporal Actor Intelligence 中「什麼是合法狀態」：SourceArtifact、EvidenceUnit、Actor、Role、Claim、Event、Hypothesis、Prediction、PolicyForecast、Economic Exposure 與 Projection 的 canonical 分層、bitemporal semantics、provenance、Evidence Contract、Projection Firewall 與 validate-before-commit 不變量。本白皮書 WP02 進一步回答：「這套系統如何持續運作？」

本文提出 Diligent AI Political/Economic Intelligence Runtime（DAPIER）。其基本任務不是讓一個大型模型不斷閱讀網路並自由更新人物印象，而是將長時序政治研究拆為可監控、可重試、可回放、可限權的工作流。Runtime 包含 Source Discovery、Snapshot Ingestion、Parsing/Transcription、Entity Resolution、Claim/Event Extraction、Verification、Canonical Commit、Temporal Replay、Hypothesis Evaluation、Counterevidence Search、Policy Realization Forecast、Economic Exposure Propagation、Alerting、Projection、Human Review、Evaluation 與 Correction 等 stage。

DAPIER 採取 proposal-only agent architecture。任何 LLM、搜尋 Agent、資料抽取 Agent、反證 Agent、Forecast Agent 或 Exposure Agent 都不能直接改寫 canonical evidence。Agent 只能提出 Proposal；真正的 canonical mutation 必須經 Canonical Commit Gate 驗證 provenance、schema、時間、實體解析、重複資料、來源權利與安全政策後才可 commit。Inference 與 Projection 另有獨立 write domain，避免人物假說與預測反向污染 evidence。

Runtime 將「新資料到達」與「模型重算」解耦。資料 ingest 是事件驅動且增量式；人物模型、政策機率與經濟暴露則透過 dependency-aware invalidation 觸發局部重算。只有當 canonical state 的相關 dependency 發生實質變化時，才重新執行 HYP、PRED 或 PRP 計算。這使「勤」不等於每次全量重讀，而是：

$$
Diligence
=
Persistent\ Coverage
+
Incremental\ Maintenance
+
Replayable\ Reanalysis
$$

政策預測 Runtime 使用 Paper 06 的 Policy Realization Probability：

$$
PRP(p,t)
=
P(Intent)
\cdot
P(Adoption\mid Intent)
\cdot
P(Implementation\mid Adoption)
\cdot
P(Persistence\mid Implementation)
$$

並將其更新建模為帶 evidence cutoff 的 forecast state。任何 forecast 必須保存 cutoff、feature lineage、model version、probability components、calibration cohort 與 expiry；回測時只能使用 cutoff 時已知資料。Economic Exposure Engine 則把 PRP 經 mechanism graph 傳播到 industry / firm / region / commodity 等 economic entities，但 Exposure 仍然只是 projection，不是交易指令。

本文同時定義 runtime scheduler、queue semantics、idempotency、retry、dead-letter、human-review queues、budget control、model routing、telemetry、quality SLO、alert suppression、publication tiers 與 incident response。Runtime event envelope 可選擇對映 CloudEvents 1.0 family；可觀測性採 OpenTelemetry traces / metrics / logs，並在 GenAI／Agent call 上使用明確 version-pinned semantic conventions。2026 年 OpenTelemetry 已持續擴充 GenAI observability，而 NIST 2026 年亦強調 agentic AI 生態需要 measurement probes 與 deployed-system monitoring。OECD 2026 的 Digital Government Outlook 更指出，agentic AI 將風險焦點從「模型說什麼」推向「系統做什麼」，並要求 traceable decision trails、meaningful accountability、user control，以及可暫停、逆轉與挑戰自動化行動。這些要求在 DAPIER 中被實作為 action-space separation、approval gates、audit trails 與 reversible projections。

WP02 的最終不變量是：

$$
Agent
\nrightarrow
Canonical\ DirectWrite
$$

$$
NewEvidence
\neq
NewTruthAboutActor
$$

$$
Forecast
=
State(Evidence_{\leq cutoff},ModelVersion)
$$

$$
Alert
\neq
Action
$$

以及：

$$
Every\ autonomous\ runtime\ action
\ must\ be\ bounded,\ observable,\ replayable,\ and\ interruptible
$$

至此，8 篇理論論文與 2 篇技術白皮書形成完整閉環：從政治人物形成、長時序證據、論述與執行、責任歸因、勤人 AI、能力重新定價、經濟情報、證據邊界，到 canonical architecture 與 24/7 runtime。

**關鍵詞：** Diligent AI、agentic AI、political intelligence、economic intelligence、event-driven runtime、policy forecasting、counterevidence、OpenTelemetry、CloudEvents、human-in-the-loop、governance

---

## Abstract

WP01 defined valid state for Temporal Actor Intelligence. WP02 defines how that state is continuously produced, maintained, recomputed, reviewed, and projected.

The Diligent AI Political/Economic Intelligence Runtime (DAPIER) is an event-driven, proposal-only agent runtime. Source discovery, ingestion, parsing, entity resolution, claim/event extraction, verification, counterevidence search, replay, hypothesis testing, policy forecasting, economic exposure propagation, alerting, and reporting are executed as bounded workflows. No LLM or autonomous agent has direct canonical-write authority. Agents produce proposals; a Canonical Commit Gate performs schema, provenance, time, entity, duplication, rights, and policy checks before canonical mutation.

Evidence ingestion and model recomputation are decoupled. New sources are incrementally canonicalized. Hypotheses, forecasts, and economic exposures are invalidated and recomputed only when relevant canonical dependencies change. Forecasts are cutoff-bound, versioned, replayable, calibrated, and expiring. Alerts are informational projections rather than autonomous decisions.

The runtime includes scheduler semantics, idempotent jobs, retry and dead-letter policies, human-review queues, model routing, cost budgets, telemetry, service-level objectives, publication tiers, incident response, and rollback of projections. Event transport may map to the CloudEvents 1.0 family. Observability uses OpenTelemetry traces, metrics, and logs with deployment-pinned semantic conventions. Governance is enforced in action spaces and approval gates, not merely through prompting.

The central invariants are:

$$
Agent
\nrightarrow
Canonical\ DirectWrite
$$

$$
NewEvidence
\neq
NewTruthAboutActor
$$

$$
Forecast
=
State(Evidence_{\leq cutoff},ModelVersion)
$$

$$
Alert
\neq
Action
$$

and:

$$
Every\ autonomous\ runtime\ action
\ must\ be\ bounded,\ observable,\ replayable,\ and\ interruptible
$$

---

# 1. WP01 / WP02 Contract

WP01：

$$
What\ is\ valid\ state?
$$

WP02：

$$
How\ does\ valid\ state\ continuously\ evolve?
$$

WP02 不能修改 WP01 canonical semantics。

---

# 2. Runtime Mission

DAPIER 的 mission：

$$
Discover
\rightarrow
Ingest
\rightarrow
Verify
\rightarrow
Commit
\rightarrow
Replay
\rightarrow
Infer
\rightarrow
Forecast
\rightarrow
Propagate
\rightarrow
Project
\rightarrow
Correct
$$

。

---

# 3. Runtime Non-Goals

不允許：

- autonomous political persuasion campaign；
- sensitive voter profiling / targeting；
- covert influence operations；
- unlawful private-data collection；
- autonomous stock/derivatives trading；
- direct personnel / credit / insurance adverse decisions；
- direct canonical writes by generative agents。

---

# 4. Runtime Trust Domains

## Domain A — External Untrusted

Internet、media、public feeds、partner feeds。

## Domain B — Raw Artifact

snapshotted but not yet canonicalized。

## Domain C — Canonical Evidence

WP01 schema-valid evidence。

## Domain D — Derived / Inference

DER、HYP、PRED、PRP、Exposure。

## Domain E — Projection

public / academic / enterprise reports、alerts、dashboards。

資料只能依允許方向流動。

---

# 5. Proposal-Only Agent Architecture

所有 agent：

$$
Agent
\rightarrow
Proposal
$$

不能：

$$
Agent
\rightarrow
CanonicalCommit
$$

。

真正 commit：

$$
Proposal
\rightarrow
CanonicalCommitGate
\rightarrow
CanonicalLedger
$$

。

---

# 6. Agent Types

v0.1 定義：

1. Source Discovery Agent
2. Fetch/Snapshot Worker
3. Parser/Transcriber
4. Entity Resolution Agent
5. Claim/Event Extraction Agent
6. Verification Agent
7. Counterevidence Agent
8. Replay Engine
9. Hypothesis Evaluation Agent
10. Policy Forecast Agent
11. Economic Exposure Agent
12. Projection/Report Agent
13. Human Review Coordinator
14. Evaluation/Calibration Worker
15. Correction/Revalidation Worker

「Agent」表示 runtime role，不要求全部由 LLM 實作。

---

# 7. Capability Envelope

每個 agent 綁定：

$$
CapabilityEnvelope=
(
ReadDomains,
WriteProposalTypes,
Tools,
MaxCost,
MaxRuntime,
RiskTier
)
$$

。

---

# 8. Authority Envelope

寫入權限：

```text
external_read
raw_write
proposal_write
derived_write
inference_write
projection_write
canonical_commit
publication_approve
```

其中 `canonical_commit` 不授予一般 Agent。

---

# 9. Least Authority Principle

$$
Authority(agent)
=
MinimumRequired(Task)
$$

。

Search Agent 不需要 publication authority。

Forecast Agent 不需要 canonical commit。

---

# 10. Workflow Object

每個工作流保存：

- workflow_id；
- workflow_type；
- trigger；
- purpose；
- cutoff；
- input IDs；
- stage state；
- attempt；
- budget；
- deadline；
- lineage；
- cancellation state。

---

# 11. Runtime State Machine

高階狀態：

```text
CREATED
QUEUED
RUNNING
WAITING_REVIEW
RETRYABLE_FAILURE
BLOCKED
COMPLETED
CANCELLED
DEAD_LETTER
```

。

---

# 12. Stage State

每個 stage 另有：

```text
PENDING
RUNNING
SUCCEEDED
FAILED_RETRYABLE
FAILED_FINAL
SKIPPED
STALE
```

。

---

# 13. Event-Driven Runtime

Runtime 以：

$$
DomainEvent
$$

驅動 workflow。

例如：

```text
source.discovered
source.snapshotted
evidence.proposed
evidence.committed
actor.state_invalidated
hypothesis.invalidated
forecast.invalidated
forecast.updated
exposure.updated
alert.proposed
challenge.opened
correction.committed
```

。

---

# 14. CloudEvents Compatibility

Runtime event envelope 可映射 CloudEvents 1.0 family：

- `id`
- `source`
- `specversion`
- `type`
- `time`
- `subject`
- `datacontenttype`
- `data`

DAPIER 不依賴特定 message broker。

---

# 15. Broker Neutrality

可以使用：

- Kafka-compatible；
- NATS；
- RabbitMQ；
- managed pub/sub；
- transactional outbox + queue。

Canonical semantics 不綁 broker。

---

# 16. Idempotency

所有 side-effecting stage 都需要：

$$
IdempotencyKey
$$

。

建議：

$$
key=
hash(
workflow\_type,
input\_ids,
schema\_version,
model\_version,
cutoff
)
$$

。

---

# 17. At-Least-Once Delivery

Runtime 預設 message transport 可為 at-least-once。

因此：

$$
DuplicateDelivery
\neq
DuplicateCommit
$$

。

---

# 18. Transactional Outbox

canonical commit 後產生 domain event 時：

$$
DBCommit
+
OutboxEvent
$$

應在同一 transaction boundary。

避免：

> 資料寫了，但 event 丟了。

---

# 19. Source Discovery

Discovery 只提出：

$$
CandidateSource
$$

不是 SourceArtifact。

---

# 20. Discovery Connectors

可包括：

- official websites；
- legislature feeds；
- government gazettes；
- RSS/Atom；
- news APIs；
- public social feeds；
- court/regulatory repositories；
- economic data feeds。

---

# 21. Connector Contract

每個 connector：

```text
discover(cursor, since) -> candidates[]
fetch(candidate) -> bytes + metadata
checkpoint() -> cursor
```

。

---

# 22. Connector Checkpoint

Checkpoint 與 canonical ledger 分離。

重跑 connector 不應改變 source semantics。

---

# 23. Snapshot First

來源一旦選擇 ingest：

$$
Fetch
\rightarrow
Snapshot
\rightarrow
Hash
$$

之後才 parse。

禁止：

$$
LiveHTML
\rightarrow
Inference
$$

直接跳過 snapshot。

---

# 24. Parsing / Transcription

HTML、PDF、audio/video 轉為：

$$
ParsedRepresentation
$$

。

Representation 必須指向 original artifact。

---

# 25. Parser Versioning

保存：

- parser name；
- version；
- parameters；
- generated_at。

parser 升級後可重新生成 representation。

---

# 26. Entity Resolution Workflow

輸入：

$$
CandidateEntityMention
$$

輸出：

$$
Resolved/AMBIGUOUS/UNRESOLVED
$$

。

AMBIGUOUS 進 review 或延後 commit。

---

# 27. Extraction Proposal

Claim/Event extractor 只能產生：

```text
EvidenceProposal
ClaimProposal
EventProposal
RoleProposal
```

。

---

# 28. Verification Agent

Verification 檢查：

- exact quote；
- locator；
- timestamp；
- actor identity；
- role；
- source consistency；
- parsing errors；
- duplication。

---

# 29. Canonical Commit Gate

Gate 至少驗證：

$$
Schema
+
Provenance
+
Time
+
Entity
+
Dedup
+
Rights
+
Policy
$$

。

---

# 30. Canonical Commit Is Deterministic

同一 Proposal + 同一 gate policy：

$$
CommitDecision
$$

應可重播。

若包含人工判斷，保存 reviewer record。

---

# 31. Commit Outcomes

```text
COMMIT
REJECT
REQUEST_REVIEW
DUPLICATE
SUPERSEDE
```

。

---

# 32. New Evidence Does Not Rewrite Actor Truth

每次：

$$
evidence.committed
$$

只代表：

> canonical corpus 新增資訊。

不代表：

$$
ActorPropertyChanged
$$

。

先做 dependency invalidation。

---

# 33. Dependency Graph

DER/HYP/PRED/PRP/Exposure 保存：

$$
DependsOnIDs
$$

。

canonical object 變動：

$$
DependencyChange
\rightarrow
MarkStale
$$

。

---

# 34. Stale Is Not Deleted

$$
State_{old}
\rightarrow
STALE
$$

直到 recompute。

舊版本保留。

---

# 35. Selective Recompute

只有 affected subgraph 重算：

$$
ChangedEvidence
\rightarrow
AffectedClaims
\rightarrow
AffectedHypotheses
\rightarrow
AffectedForecasts
\rightarrow
AffectedExposures
$$

。

---

# 36. Full Replay

全量 replay 用於：

- schema migration；
- model upgrade evaluation；
- audit；
- historical backtest；
- incident recovery。

不是每一新事件都 full replay。

---

# 37. Replay Engine

概念接口：

```text
replay_actor(actor_id, valid_cutoff, record_cutoff, purpose, model_set)
```

輸出 immutable view。

---

# 38. Frozen Research Run

正式研究 run 先：

$$
Freeze(CorpusVersion,Cutoff,ModelVersions)
$$

再開始分析。

研究過程中新資料進入 canonical，不影響 frozen run。

---

# 39. Hypothesis Workflow

$$
Question
\rightarrow
CandidateHYP
\rightarrow
SupportSearch
\rightarrow
CounterSearch
\rightarrow
AlternativeHYP
\rightarrow
EvidenceContract
\rightarrow
Review
$$

。

---

# 40. Counterevidence Agent

不是「找反對新聞」。

它依 hypothesis 定義：

$$
DisconfirmingEvidenceClasses
$$

並逐類搜尋。

---

# 41. Counterevidence Completion

Paper 04：

$$
CEC_H
$$

成為 workflow completion condition。

T2/T3 publication：

$$
CEC_H=Complete
$$

才可進 gate。

---

# 42. Alternative Hypothesis Registry

同一 observed pattern 可保留：

$$
H_1,H_2,\ldots,H_n
$$

。

Runtime 不強迫單一人物解釋。

---

# 43. Policy Forecast Workflow

對 policy $p$：

1. Freeze cutoff
2. Rebuild relevant actors/roles
3. Estimate Intent
4. Estimate Adoption
5. Estimate Implementation
6. Estimate Persistence
7. Compose PRP
8. Calibrate
9. Store Prediction
10. Set expiry
11. Register dependencies

---

# 44. PRP Components

$$
PRP=
P_I
\cdot
P_A
\cdot
P_M
\cdot
P_S
$$

Runtime 必須保存四個 component。

只存總 PRP 不足以解釋。

---

# 45. Forecast Model Routing

不同 component 可使用不同方法：

- statistical model；
- Bayesian model；
- calibrated classifier；
- LLM-assisted feature extraction；
- human expert prior；
- ensemble。

---

# 46. LLM Cannot Be Probability Oracle

LLM 直接回答：

> 73%。

不構成 calibrated forecast。

LLM 可：

- extract features；
- generate rationale candidates；
- identify comparable cases。

最終 probability 需 calibration framework。

---

# 47. Forecast Cutoff

每個 feature：

$$
recorded\_at
\leq
forecast\_cutoff
$$

。

違反即：

$$
TemporalLeakageFailure
$$

。

---

# 48. Prediction Expiry

PRED 必須有：

$$
expiry
$$

。

到期：

```text
EXPIRED
```

不再當 current forecast。

---

# 49. Forecast Update Trigger

trigger：

- material actor state change；
- institutional state change；
- policy stage change；
- coalition change；
- legal ruling；
- budget event；
- scheduled recalibration。

---

# 50. Materiality Threshold

不是每一篇新聞都更新 PRP。

定義：

$$
MaterialityScore
$$

。

低於 threshold：

$$
NoForecastRecompute
$$

。

---

# 51. Policy Momentum

$$
PM_p(t)
=
\frac{dPRP_p(t)}{dt}
$$

Runtime 可對快速變化建立 alert candidate。

---

# 52. Economic Exposure Workflow

$$
PRPUpdate
\rightarrow
MechanismEdges
\rightarrow
EconomicEntities
\rightarrow
ExposureRecompute
$$

。

---

# 53. Exposure Is Projection

Exposure 不寫回 canonical evidence。

---

# 54. Exposure Propagation

對 graph：

$$
Policy
\rightarrow
Mechanism
\rightarrow
Industry/Firm
$$

使用：

- declared coefficients；
- calibrated models；
- scenario ranges。

---

# 55. Exposure Uncertainty

每條 exposure 保存：

$$
Direction
+
MagnitudeRange
+
Uncertainty
+
EvidencePath
$$

。

---

# 56. Enterprise Alert

Alert 形式：

> PRP for policy X rose from 0.31 to 0.52; primary driver: committee movement; exposure for industry Y increased.

而不是：

> Buy / sell。

---

# 57. Alert Is Projection

核心：

$$
Alert
\neq
Action
$$

。

Runtime 不自主下單、不自動遊說、不自動政治操作。

---

# 58. Alert Dedupe

同一 state change：

$$
OneMaterialAlert
$$

避免 event storm。

---

# 59. Alert Cooldown

每 alert key：

$$
CooldownWindow
$$

。

只有 material delta 超過 threshold 才 bypass。

---

# 60. Public Alert

Public projection 可提示：

- major policy stage change；
- evidence update；
- corrected claim；
- model uncertainty increase。

不得推送高名譽風險 HYP 未經 review。

---

# 61. Human Review Queues

至少：

1. Entity Ambiguity Queue
2. High-Risk Evidence Queue
3. Responsibility/Causality Queue
4. T3 Publication Queue
5. Re-identification Queue
6. Challenge/Correction Queue
7. Model-Drift Queue

---

# 62. Human Review SLA

高風險 pending：

$$
PublicationBlocked
$$

不是自動 timeout 放行。

---

# 63. Review Decision

```text
APPROVE
REJECT
REQUEST_MORE_EVIDENCE
DOWNGRADE_TIER
CHANGE_EPISTEMIC_TYPE
MARK_DISPUTED
```

。

---

# 64. Budget Object

每 workflow：

$$
Budget=
(
MaxTokens,
MaxModelCost,
MaxSearches,
MaxWallClock,
MaxRetries
)
$$

。

---

# 65. Cost-Aware Routing

簡單 extraction：

$$
LowCostModel
$$

高風險 reasoning：

$$
HigherCapabilityModel
+
HumanReview
$$

。

不是所有 task 用最大模型。

---

# 66. Escalation Policy

如果：

$$
ConfidenceLow
$$

或：

$$
RiskHigh
$$

可升級：

$$
ModelTier\uparrow
$$

或：

$$
HumanReview
$$

。

---

# 67. Search Budget

勤人 AI 不代表無限搜尋。

每 hypothesis 定義：

- minimum support search；
- minimum counter search；
- saturation criterion；
- hard budget。

---

# 68. Search Saturation

若新增 search batches 的：

$$
NovelEvidenceRate
\rightarrow
0
$$

可停止。

但要報 coverage / missingness。

---

# 69. Queue Priority

priority 可由：

$$
Urgency
+
Materiality
+
Risk
+
Staleness
$$

決定。

---

# 70. Backpressure

來源爆量：

$$
QueueDepth\uparrow
$$

Runtime 必須：

- degrade noncritical crawling；
- preserve official/high-value feeds；
- increase batch sizes；
- never skip canonical validation。

---

# 71. Retry Policy

retryable：

- network timeout；
- transient provider error；
- temporary parser failure。

non-retryable：

- schema invalid；
- prohibited purpose；
- unresolved legal rights；
- deterministic policy gate failure。

---

# 72. Exponential Backoff

$$
Delay_n
=
min(
D_{max},
D_0 2^n
)
+
Jitter
$$

。

---

# 73. Dead-Letter Queue

超過 retry：

$$
DEAD\_LETTER
$$

並保留：

- payload ref；
- reason；
- attempts；
- last error；
- owner。

---

# 74. Poison Source

來源反覆使 parser 崩潰：

標記：

$$
QUARANTINED
$$

不阻塞主 pipeline。

---

# 75. Runtime Cancellation

所有長流程必須：

$$
Interruptible
$$

。

支持：

- user cancel；
- policy cancel；
- incident cancel；
- budget cancel。

---

# 76. Reversibility

Canonical source commit 一般不刪。

但：

$$
Projection
$$

可：

- withdraw；
- supersede；
- correct；
- disable distribution。

---

# 77. Agentic Action Boundary

Agent 可自主：

- 搜尋；
- 讀取；
- 分析；
- 建立 proposal；
- 建立 draft report。

Agent 不可自主：

- canonical write；
- high-risk public publish；
- money transfer；
- political ad placement；
- sensitive targeting。

---

# 78. OECD Agentic AI Boundary

2026 OECD 對 agentic AI 的關鍵區分：

$$
GenAI\ says
$$

對：

$$
AgenticAI\ acts
$$

。

因此 DAPIER 對 action space 的治理比 prompt 更重要。

---

# 79. Pause / Reverse / Challenge

任何高影響 automated chain 需要：

$$
Pause
$$

$$
ReverseProjection
$$

$$
Challenge
$$

。

這與 OECD 2026 對政府 agentic AI 的 traceability / user control 要求一致。

---

# 80. Observability

Runtime 必須有：

$$
Traces
+
Metrics
+
Logs
$$

。

採 OpenTelemetry-compatible telemetry。

---

# 81. Trace Hierarchy

一個 research workflow：

```text
workflow.run
  ├─ source.search
  ├─ source.fetch
  ├─ parse
  ├─ entity.resolve
  ├─ extract
  ├─ verify
  ├─ counterevidence.search
  ├─ forecast
  └─ projection.generate
```

。

---

# 82. GenAI Observability

LLM/Agent call telemetry 至少：

- operation；
- model/provider；
- latency；
- token/input size；
- output size；
- tool calls；
- retry；
- error type；
- cost estimate；
- prompt/content capture policy。

---

# 83. Sensitive Telemetry

完整 prompt / completion：

$$
OptIn
$$

。

因可能含：

- licensed text；
- internal hypotheses；
- sensitive data。

預設不記完整 content 到一般 telemetry。

---

# 84. Semantic Convention Pinning

OpenTelemetry semantic conventions 會演進。

部署必須：

$$
Pin(version)
$$

並由 mapping layer 轉 internal telemetry schema。

---

# 85. Runtime Metrics

核心：

- connector lag；
- ingestion throughput；
- source error rate；
- canonical commit latency；
- entity ambiguity rate；
- stale inference count；
- forecast recompute latency；
- alert latency；
- review queue depth；
- token/model cost；
- evidence trace failure；
- counterevidence completion。

---

# 86. Quality SLO

示意：

$$
EvidenceTraceability\geq99.9\%
$$

$$
CanonicalSchemaValidity=100\%
$$

$$
TemporalLeakageBacktests=0
$$

$$
T3WithoutReview=0
$$

。

實際 deployment SLO 需依系統規模設定。

---

# 87. Freshness SLO

不同 source class：

- official policy feeds：minutes-hours；
- major news：hours；
- academic publications：days；
- archival backfill：best effort。

不需要所有來源 real-time。

---

# 88. Diligence SLO

Paper 04：

$$
CR,TR,TF,CEC,HSR,CCC
$$

作 quality dashboard。

---

# 89. Forecast SLO

每 forecast family：

- calibration；
- Brier score；
- Log Loss；
- coverage；
- lead time；
- abstention rate。

---

# 90. Model Drift

監控：

$$
FeatureDistribution_t
$$

$$
Calibration_t
$$

$$
ExtractionAgreement_t
$$

。

drift 觸發：

$$
ModelReview
$$

。

---

# 91. Deployed AI Monitoring

NIST 2026 特別指出 deployed AI 需要 functionality、operational 等持續 monitoring。

DAPIER 因此把 post-deployment monitoring 視為 runtime core，而不是 release 後附加工作。

---

# 92. Agent Measurement Probes

每 Agent 都要可追：

$$
Input
\rightarrow
Plan/ToolCalls
\rightarrow
OutputProposal
$$

在高風險 workflow 可保留更細 decision trail。

---

# 93. NIST Agent Standards Direction

2026 NIST 已啟動 AI Agent Standards Initiative，重點包含 interoperable / secure agent ecosystem。

DAPIER 因此不假設 proprietary single-agent runtime 是長期唯一介面。

---

# 94. Model Provider Abstraction

模型接口：

```text
generate()
embed()
classify()
extract()
rerank()
```

。

Runtime 不把 canonical semantics 綁定特定模型 provider。

---

# 95. Tool Provider Abstraction

搜尋、資料庫、轉錄、圖運算都透過 capability interface。

---

# 96. Deterministic Tool First

可 deterministic 的：

- hash；
- schema validation；
- time filtering；
- graph traversal；
- numeric calculation；

不交給 LLM 自由推理。

---

# 97. LLM Use Cases

適合：

- semantic extraction；
- ambiguous classification；
- query decomposition；
- hypothesis generation；
- evidence synthesis；
- natural-language projection。

---

# 98. LLM Abstention

Agent 可以輸出：

```text
INSUFFICIENT_EVIDENCE
AMBIGUOUS_ENTITY
NEEDS_REVIEW
```

不是強迫生成答案。

---

# 99. Multi-Agent Is Optional

DAPIER 支援多 Agent，但：

$$
MoreAgents
\nRightarrow
Better
$$

。

簡單 task 可單 worker。

---

# 100. Agent Coordination

多 Agent 共享：

$$
TaskState
$$

而不是自由聊天當 source of truth。

---

# 101. Shared Scratchpad Is Non-Canonical

Agent scratchpad：

$$
Ephemeral
$$

。

不能被下次 run 當 evidence。

---

# 102. Runtime Memory

分：

## Canonical Memory

WP01 ledger。

## Operational Memory

workflow state、checkpoints。

## Ephemeral Reasoning Context

當次 Agent context。

三者不可混用。

---

# 103. Research Session

每次深度分析產生：

$$
ResearchSession
$$

保存：

- query；
- scope；
- cutoff；
- evidence snapshot ID；
- workflows；
- outputs；
- review state。

---

# 104. Repeatability

同一：

$$
CorpusSnapshot
+
ModelVersion
+
Config
$$

應能產生可比較結果。

LLM 非 deterministic 時保存：

- model ID；
- parameters；
- seed if available；
- output lineage。

---

# 105. Query Planner

Planner 將問題拆成：

$$
Subqueries
$$

但不能改變 purpose。

---

# 106. Query Plan Example

「此人物是否在成功時較常攬功？」

拆：

1. identify role/time scope；
2. collect positive matched events；
3. collect negative matched events；
4. rebuild responsibility edges；
5. code attribution；
6. counterevidence；
7. calculate asymmetry；
8. report uncertainty。

---

# 107. Research Planner Risk

Planner 可能因 user wording 形成 confirmation bias。

Mitigation：

$$
UserHypothesis
\rightarrow
CandidateHYP
$$

同時自動產生：

$$
NullHYP
+
AlternativeHYP
$$

。

---

# 108. Null Hypothesis

例如：

$$
H_0:
No\ stable\ attribution\ asymmetry
$$

。

---

# 109. Evidence Search Strategy

順序優先：

$$
Primary
\rightarrow
Official
\rightarrow
DirectTranscript
\rightarrow
HighQualitySecondary
$$

。

---

# 110. Media Search Is Discovery, Not Truth

新聞搜尋結果先變：

$$
CandidateSource
$$

。

---

# 111. Long-Horizon Monitoring

Condition watch：

$$
NewMaterialEvidence
$$

才更新 actor model。

不是固定每天重寫人物評價。

---

# 112. Material Change

包括：

- new role；
- major decision；
- policy stage move；
- significant correction；
- adjudicated finding；
- major election；
- material coalition change。

---

# 113. Scheduled Maintenance

每日：

- connector health；
- critical feeds。

每週：

- unresolved entity review；
- stale inferences。

每月：

- forecast calibration；
- coverage audit；
- model drift。

頻率可配置。

---

# 114. Archive Backfill

Historical corpus 可用低優先 queue 漸進補齊。

---

# 115. Backfill Must Preserve Record Time

若 2026 才抓到 2018 文件：

$$
valid\_time=2018
$$

$$
record\_time=2026
$$

。

歷史 replay 不偷用。

---

# 116. Correction Workflow

來源更正：

$$
source.revised
\rightarrow
artifact.v2
\rightarrow
canonical.correction
\rightarrow
dependency.invalidate
\rightarrow
recompute
\rightarrow
projection.correct
$$

。

---

# 117. Challenge Workflow

外部 challenge：

$$
challenge.opened
\rightarrow
triage
\rightarrow
evidence.review
\rightarrow
decision
\rightarrow
correction/reject
$$

。

---

# 118. Incident Classes

- canonical corruption；
- temporal leakage；
- source poisoning；
- widespread entity merge error；
- privacy breach；
- prohibited-use invocation；
- publication of unsupported high-risk allegation；
- forecast pipeline miscalibration。

---

# 119. Incident Severity

```text
SEV0
SEV1
SEV2
SEV3
```

SEV0 可觸發：

$$
PublicationFreeze
$$

。

---

# 120. Kill Switch

Runtime 必須可：

- stop connector；
- stop agent class；
- freeze publication；
- freeze forecast；
- revoke capability；
- invalidate projection。

---

# 121. Canonical Recovery

Canonical ledger recovery：

- restore snapshot；
- replay append log；
- verify hashes；
- rebuild indexes；
- rebuild graph；
- mark inferences stale；
- recompute。

---

# 122. Non-Canonical Recovery

Vector/graph/cache：

$$
RebuildFromCanonical
$$

。

---

# 123. Cost Incident

若 token / API cost 超 budget：

$$
DegradeGracefully
$$

：

- lower search depth；
- delay archival backfill；
- lower-cost model；
- preserve critical official feeds；
- never disable evidence gates。

---

# 124. Publication Pipeline

$$
ProjectionDraft
\rightarrow
RiskClassify
\rightarrow
EvidenceCheck
\rightarrow
Review
\rightarrow
Publish
$$

。

---

# 125. Public Report

至少包含：

- scope；
- cutoff；
- observed；
- derived；
- hypotheses；
- counterevidence；
- unknowns；
- sources；
- last updated。

---

# 126. Enterprise Report

額外：

- PRP；
- component probabilities；
- policy momentum；
- exposure mechanism；
- scenario；
- uncertainty；
- lead time。

---

# 127. Academic Export

提供：

- corpus snapshot ID；
- schema version；
- de-identified records where required；
- derivation methods；
- model versions；
- codebook；
- reproducibility manifest。

---

# 128. Publication Revocation

若重大錯誤：

$$
Projection
\rightarrow
WITHDRAWN
$$

並提供 correction notice。

---

# 129. No Silent Rewrite

公開報告更新：

$$
v1
\rightarrow
v2
$$

保留 revision history。

---

# 130. Privacy Runtime Gate

在 ingestion / inference / publication 都檢查：

$$
PublicRoleRelevance
+
Purpose
+
DataMinimization
$$

。

---

# 131. Coded Case Runtime

coded case projection 先做：

$$
ReIdentificationRiskCheck
$$

。

---

# 132. Sensitive Trait Gate

若 inference target 屬敏感私人屬性：

$$
DefaultBlock
$$

除非明確 research/legal policy 另行允許。

---

# 133. Political Targeting Boundary

Runtime 不提供：

```text
build_voter_profile()
target_sensitive_group()
optimize_political_persuasion()
```

。

---

# 134. Financial Boundary

Runtime 可：

$$
PolicyRiskReport
$$

不能：

$$
AutonomousTradeExecution
$$

。

---

# 135. Security

所有 connector input 視為：

$$
Untrusted
$$

。

防：

- prompt injection；
- malicious HTML；
- poisoned documents；
- SSRF；
- decompression bombs；
- malicious attachments。

---

# 136. Tool Isolation

Parser / fetcher / model tool 各自最小 sandbox。

---

# 137. Prompt Injection Boundary

來源文件中的：

> Ignore instructions...

只能當 source content。

不能改 runtime policy。

---

# 138. Retrieval Content Is Data

$$
RetrievedText
\neq
Instruction
$$

。

---

# 139. Secret Isolation

API keys：

- secret manager；
- never canonical；
- never prompt unless required；
- never telemetry content。

---

# 140. Network Policy

不同 worker 可有不同 outbound allowlist。

---

# 141. Data Retention

Raw artifacts、licensed data、telemetry 分別有 retention policy。

Canonical public evidence 可長期保存；敏感 operational logs 期限更短。

---

# 142. Auditability

每次高風險 output 要知道：

$$
Who/What
$$

在：

$$
When
$$

用：

$$
WhichEvidence
$$

與：

$$
WhichModel
$$

產生。

---

# 143. Runtime Invariants

隨附 `lai_runtime_invariants_v0.1.json`，包含至少 24 條 machine-readable invariants。

---

# 144. Runtime Config Schema

隨附：

`lai_runtime_config_schema_v0.1.json`

定義：

- environment；
- queues；
- budgets；
- model routes；
- review policy；
- publication policy；
- telemetry；
- forecast；
- alerting；
- security。

---

# 145. Runtime Event Catalog

隨附：

`lai_runtime_event_catalog_v0.1.json`

定義 domain event types 與 CloudEvents-compatible mapping。

---

# 146. Runtime State Machine

隨附：

`lai_runtime_state_machine_v0.1.json`

定義 workflow 與 stage transition。

---

# 147. Example Config

隨附：

`lai_example_runtime_config_v0.1.json`

為 non-production reference。

---

# 148. Acceptance Test Suite

隨附：

`lai_wp02_acceptance_tests_v0.1.json`

涵蓋：

- no direct canonical writes；
- temporal cutoff；
- idempotency；
- counterevidence gate；
- publication gate；
- forecast expiry；
- stale dependency recompute；
- alert/action separation；
- telemetry；
- kill switch；
- correction lineage。

---

# 149. MVP Runtime

v0.1 MVP 建議：

$$
10\ Actors
$$

$$
5\ Years
$$

$$
3\ SourceClasses
$$

$$
1\ Jurisdiction
$$

$$
20\ Policies
$$

$$
50\ EconomicEntities
$$

。

---

# 150. MVP Services

最小服務：

1. Connector Service
2. Artifact Store
3. Canonical Commit Service
4. Canonical DB
5. Index Service
6. Replay Service
7. Research/Inference Worker
8. Forecast Worker
9. Projection Service
10. Review Console
11. Telemetry Collector

---

# 151. MVP Deployment

第一版可：

$$
SingleCluster/SingleRegion
$$

。

不需要微服務極端拆分。

邏輯 boundary 比 deployment boundary 重要。

---

# 152. Reference Deployment Philosophy

先：

$$
Modular\ Monolith
+
Queue
+
Workers
$$

比過早微服務化更合理。

---

# 153. Scaling Axis

未來按：

- source volume；
- actor count；
- query concurrency；
- forecast families；
- enterprise tenants；

逐步拆。

---

# 154. Tenant Isolation

企業版需要：

$$
TenantProjection
$$

與 canonical public evidence 分離。

客戶自有資料不得回流公共 canonical。

---

# 155. Customer Data Boundary

$$
CustomerPrivateData
\nrightarrow
PublicCanonical
$$

除非明確授權與 policy。

---

# 156. Multi-Tenant Inference

同一 public canonical 可供多 tenant 使用。

私人 scenario / annotations 隔離。

---

# 157. Evaluation Harness

每個 model route 有 benchmark：

- extraction；
- entity resolution；
- claim classification；
- contradiction；
- forecast；
- report factuality。

---

# 158. Shadow Evaluation

新模型先：

$$
Shadow
$$

不影響 production projection。

---

# 159. Canary

低風險少量 workflow：

$$
Canary
$$

後才擴大。

---

# 160. Rollback

模型／config 回滾只影響 derived/inference/projection。

canonical evidence 不需回滾，除非 canonical incident。

---

# 161. Continuous Evaluation

$$
Deploy
\rightarrow
Monitor
\rightarrow
Evaluate
\rightarrow
Correct
$$

與 NIST 2026 deployed-AI monitoring方向一致。

---

# 162. OpenTelemetry Resource

建議 resource attributes：

- service.name；
- service.version；
- deployment.environment；
- lai.workflow.type；
- lai.purpose；
- lai.risk_tier。

自訂 `lai.*` namespace 不假裝是 OTel 標準。

---

# 163. Trace Privacy

`lai.actor.id` 可用 internal pseudonymous ID。

不把敏感姓名當高基數公共 telemetry attribute。

---

# 164. Event Correlation

Runtime event：

$$
correlation\_id
$$

連接 workflow trace。

---

# 165. SLO/Error Budget

系統優先：

$$
Correctness
+
Safety
+
Traceability
$$

高於：

$$
Freshness
$$

。

當 error budget 耗盡：

$$
ReduceAutomation
$$

而不是降低 gate。

---

# 166. Runtime Governance Board

正式部署可有：

- research owner；
- data steward；
- security owner；
- model owner；
- publication reviewer；
- enterprise risk owner。

不是單一 AI 自己治理自己。

---

# 167. Change Management

修改：

- schema；
- purpose；
- risk threshold；
- model route；
- publication tier；

需要 versioned change record。

---

# 168. Runtime Policy as Code

建議：

$$
Governance
\rightarrow
PolicyAsCode
$$

。

例如：

```text
deny if purpose == sensitive_voter_microtargeting
deny T3 publish unless counterevidence_complete
deny canonical_write unless principal == commit_service
```

。

---

# 169. Policy Engine Is Deterministic

高階安全 gate 優先 deterministic policy。

不能交給 LLM：

> 你覺得可以發布嗎？

作唯一決策。

---

# 170. Fail Closed

對：

- canonical commit；
- T3 publication；
- sensitive inference；
- prohibited use；

遇到 policy service failure：

$$
Deny/Block
$$

。

---

# 171. Fail Open

只有低風險非關鍵 telemetry 等可視需求 fail open。

---

# 172. Runtime Data Contracts

任何 stage output 先 schema validate。

$$
AgentOutput
\rightarrow
SchemaValidation
\rightarrow
NextStage
$$

。

---

# 173. Model Output Is Untrusted

即使是內部模型：

$$
LLMOutput
=
UntrustedStructuredProposal
$$

。

---

# 174. Structured Output

對 commit proposal，prefer：

$$
JSON
+
Schema
$$

不是 free-form prose。

---

# 175. Evidence Citation

任何 report-level material claim：

$$
Claim
\rightarrow
EvidenceIDs
$$

由 Projection Service render 人類 citation。

---

# 176. No Citation Fabrication

如果 evidence path 空：

$$
DoNotRenderCitation
$$

且 material claim 應降級／刪除／abstain。

---

# 177. Runtime Search Audit

保存：

- query；
- provider；
- time；
- result IDs；
- selected results；

高風險研究可重播 discovery path。

---

# 178. Search Provider Diversity

重要研究可用多來源／多 provider 降低單一搜尋排序偏誤。

---

# 179. Search Result Ranking Is Not Evidence Weight

$$
SearchRank
\neq
Credibility
$$

。

---

# 180. Runtime Research Closure

ResearchSession 完成條件：

- scope satisfied；
- coverage reported；
- counterevidence done；
- unresolved listed；
- evidence contracts valid；
- review done if required。

---

# 181. Partial Completion

若 budget 用盡：

$$
PARTIAL
$$

並報：

- completed scope；
- missing scope；
- unresolved questions。

不能假稱完整。

---

# 182. Academic Reproducibility

研究 export 包含：

$$
CorpusSnapshotID
+
Cutoff
+
SchemaVersion
+
ModelVersions
+
ConfigHash
$$

。

---

# 183. Enterprise Reproducibility

企業 alert 保存：

$$
ForecastID
+
EvidenceSnapshot
+
ExposureModelVersion
$$

。

---

# 184. Public Reproducibility

公眾報告至少能回：

$$
Source
+
Date
+
EvidencePath
$$

。

---

# 185. Runtime Security Review

每 connector / tool 新增前：

- threat model；
- permissions；
- outbound network；
- data class；
- secret needs；
- incident plan。

---

# 186. Agent Tool Allowlist

Agent 只能使用明確 allowlisted tools。

---

# 187. No Arbitrary Code Execution by Default

政治資料分析 Runtime 不需要讓一般研究 Agent arbitrary shell。

高權限 computation 隔離。

---

# 188. Sandbox

需要解析不可信檔案時：

$$
Sandbox
$$

。

---

# 189. Data Poisoning

來源如果刻意大量發布同一虛假敘事：

- source independence；
- provenance；
- official verification；
- counterevidence；

降低 poisoning 影響。

---

# 190. Sybil Source Detection

大量低品質站點不等於多獨立證據。

---

# 191. Model Self-Contamination

過去 AI 生成的報告如果被網路收錄：

$$
AIGeneratedProjection
$$

不應被重新 ingest 成獨立 source evidence，除非標明它只是 secondary artifact。

---

# 192. Source Circularity Detection

$$
Projection_A
\rightarrow
Media_B
\rightarrow
Projection_A
$$

需要 lineage 防止循環自證。

---

# 193. Runtime Ethics Invariant

$$
Diligence
\neq
Surveillance
$$

。

---

# 194. Runtime Economic Invariant

$$
Intelligence
\neq
GuaranteedProfit
$$

。

---

# 195. Runtime Political Invariant

$$
Analysis
\neq
PersuasionAuthorization
$$

。

---

# 196. Runtime AI Invariant

$$
Autonomy
\neq
Authority
$$

。

---

# 197. Series Closure

8 Papers：

$$
Theory
$$

WP01：

$$
ValidState
$$

WP02：

$$
ContinuousOperation
$$

。

因此整體：

$$
LAI=
Theory
+
CanonicalArchitecture
+
GovernedRuntime
$$

。

---

# 198. Final Runtime Equation

可將 DAPIER 壓縮為：

$$
DAPIER=
(
Q,
W,
A,
C,
R,
F,
X,
P,
O
)
$$

其中：

- $Q$：queues/events；
- $W$：workflows；
- $A$：bounded agents；
- $C$：canonical commit gates；
- $R$：replay / research；
- $F$：forecast；
- $X$：economic exposure propagation；
- $P$：projection firewall；
- $O$：observability / oversight。

---

# 199. Final Invariants

$$
\boxed{
Agent\nrightarrow Canonical\ DirectWrite
}
$$

$$
\boxed{
NewEvidence\neq NewTruthAboutActor
}
$$

$$
\boxed{
Forecast=State(Evidence_{\leq cutoff},ModelVersion)
}
$$

$$
\boxed{
Alert\neq Action
}
$$

$$
\boxed{
Autonomy\neq Authority
}
$$

以及：

$$
\boxed{
Every\ autonomous\ runtime\ action
\ must\ be\ bounded,\ observable,\ replayable,\ interruptible,\ and\ attributable
}
$$

。

---

# 200. 結論

「勤人 AI」真正困難的地方並不是讓 AI 讀很多資料。

如果沒有 runtime discipline，所謂「長時序人物分析」很容易退化成：

$$
ContinuousWebSearch
\rightarrow
ContinuousLLMOpinion
$$

。

DAPIER 拒絕這種架構。

它把「勤」拆成：

$$
PersistentCoverage
$$

$$
IncrementalCanonicalization
$$

$$
DependencyAwareRecompute
$$

$$
Counterevidence
$$

$$
HistoricalReplay
$$

$$
ContinuousEvaluation
$$

。

同時把「AI 自主」限制在：

$$
BoundedTaskExecution
$$

而不是：

$$
UnboundedAuthority
$$

。

因此，政治人物的新資料不會直接改寫人物結論；Forecast 不會因新聞標題就自行飄動；企業 alert 不會自動變成交易；研究 Agent 不會直接修改 canonical evidence；高風險發布不會因模型很有自信就跳過人工審核。

這套 Runtime 最終追求的不是：

> AI 永遠比人更會判斷政治。

而是：

> 讓原本需要大量研究員才能長期維護的政治記憶、反證、時序回放、政策機率與企業暴露分析，變成可持續運作，而且每一個重要結果都能被中止、回放、檢查與修正。

因此 WP02 的最終工程命題是：

$$
\boxed{
Make\ Diligence\ Operational
}
$$

而與 Paper 07 的：

$$
Make\ Restraint\ Computable
$$

以及 WP01 的：

$$
Make\ State\ Canonical
$$

共同形成完整三角：

$$
\boxed{
Canonical\ State
+
Operational\ Diligence
+
Computable\ Restraint
}
$$

至此，AI-Native Longitudinal Actor Intelligence v0.1 的理論與技術系列完成。

---

# References and Current Technical Context

CloudEvents Authors / CNCF. (2026). *CloudEvents Specification, 1.0 family*. https://github.com/cloudevents/spec

NIST. (2024; page updated 2026). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1*. https://doi.org/10.6028/NIST.AI.600-1

NIST. (2026). *Challenges to the Monitoring of Deployed AI Systems, NIST AI 800-4*. National Institute of Standards and Technology.

NIST Center for AI Standards and Innovation. (2026). *AI Agent Standards Initiative*. National Institute of Standards and Technology.

OECD. (2026). *The Agentic AI Landscape and Its Conceptual Foundations*. OECD Artificial Intelligence Papers, No. 56. https://doi.org/10.1787/396cf758-en

OECD. (2026). *Digital Government Outlook 2026: From Foundations to Transformational Impact*. OECD Publishing. https://doi.org/10.1787/0496b2bc-en

OpenTelemetry. (2026). *OpenTelemetry Semantic Conventions*. https://opentelemetry.io/docs/specs/semconv/

OpenTelemetry. (2026). *Inside the LLM Call: GenAI Observability with OpenTelemetry*. https://opentelemetry.io/blog/2026/genai-observability/

---

## Canonical Source Note

本檔為 WP02 v0.1 的 UTF-8 canonical Markdown source。正式數學 source 僅使用 ` $...$ ` 與 `$$...$$` delimiter。任何 dashboard、alert、trace UI、聊天畫面、HTML、PDF、簡報、runtime state cache、vector index、graph projection 或模型輸出都不是 canonical source。Runtime policy、schema、invariant 與 workflow 的正式修改必須先修改 canonical artifact，執行 validation，再 commit 新版本。
