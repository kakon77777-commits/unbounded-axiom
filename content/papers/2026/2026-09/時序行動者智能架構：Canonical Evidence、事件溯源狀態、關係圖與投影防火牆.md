---
title: "時序行動者智能架構：Canonical Evidence、事件溯源狀態、關係圖與投影防火牆"
english_title: "Temporal Actor Intelligence Architecture: Canonical Evidence, Event-Sourced State, Relational Graphs, and Projection Firewalls"
series: "AI-Native Longitudinal Actor Intelligence"
author: "Neo.K"
institution: "EveMissLab／一言諾科技有限公司"
artifact: "Technical Whitepaper 01"
version: "v0.1"
date: "2026-08-28"
language: "zh-TW"
status: "Canonical Architecture Whitepaper / UTF-8 Source"
architecture_scope: "Defines canonical data model, provenance, temporal semantics, inference boundaries, replay, projection, governance gates, and interoperability contracts. Runtime orchestration is deferred to WP02."
---

# 時序行動者智能架構：Canonical Evidence、事件溯源狀態、關係圖與投影防火牆

**Temporal Actor Intelligence Architecture: Canonical Evidence, Event-Sourced State, Relational Graphs, and Projection Firewalls**

**AI-Native Longitudinal Actor Intelligence — Technical Whitepaper 01**

---

## 摘要

本白皮書將《AI-Native Longitudinal Actor Intelligence》Paper 01–08 的理論成果收斂為一套可實作的 canonical system architecture。系統目標不是建立「人物真相資料庫」，而是建立可追溯、可重播、可反證、可修正的長時序行動者智能基礎設施，使政治人物、公共官員、監管者、央行官員、企業領導者與其他高影響行動者的公開資料，可以在不混淆證據與推論的前提下形成 Actor State、責任模型、政策實現機率與經濟暴露 projection。

本架構採取五項核心設計：

1. **Immutable Source / Append-Only Canonical Ledger**：原始來源與 canonical evidence 不被人物推論覆寫；更正以新版本與 lineage 表達。
2. **Event-Sourced Temporal Actor State**：人物狀態不是靜態 profile，而是由時間有序事件重播得到的 view。
3. **Relational + Graph + Vector Separation**：關聯式 canonical ledger、關係圖 projection、向量檢索索引各司其職；向量庫永遠不是 source of truth。
4. **Epistemic Type Separation**：OBS、DER、HYP、PRED、NORM、DISPUTED、UNKNOWN、UNAVAILABLE 具有機器可驗證的型別邊界。
5. **Projection Firewall**：Academic、Public、Enterprise projection 從共同 canonical evidence 派生，但用途、權限、敏感推論與發布門檻彼此隔離。

架構使用 bitemporal semantics，至少保存事件有效時間與系統記錄時間，以阻止 hindsight leakage。每個衍生關係與人物假說都必須經 Evidence Contract 綁定來源、support、counterevidence、coverage、alternative explanations 與 reviewer state。所有重要狀態均可依任意 historical cutoff replay，因此系統可以回答：「只使用 2024 年 6 月 1 日以前可得資料，當時模型如何理解人物 A？」而不偷用未來資訊。

本白皮書同時定義 SourceArtifact、EvidenceUnit、Actor、RoleAssignment、Claim、Event、Decision、Outcome、ResponsibilityEdge、Attribution、Correction、Hypothesis、Prediction、Institution、Policy、PolicyForecast、EconomicEntity、ExposureEdge、EducationRecord、CareerRecord、Challenge、EvidenceContract、ActorModelCard 與 Projection 等核心物件；並提出 ingestion、canonicalization、entity resolution、claim/event extraction、temporal alignment、counterevidence search、human review、projection 與 correction 的完整資料流。

架構以 JSON Schema 2020-12 作為 v0.1 機器可驗證 interchange contract，並預留與 W3C PROV-O 的 provenance mapping。W3C PROV-O 將 provenance 表達為 entity、activity、agent 及其 derivation / attribution 關係；本架構不直接採用 RDF 作為唯一儲存形態，但保留可對映性，以避免封閉的 provenance model。NIST AI RMF 的 lifecycle risk-management 思想則被實作為 ingestion、inference、publication 與 correction 各層 gate，而非僅在最終輸出做 moderation。

WP01 不定義最終 Agent orchestration、排程、alerting、continuous monitoring 或企業 workflow；這些由 WP02 — Diligent AI Political/Economic Intelligence Runtime 處理。WP01 的唯一任務是回答：

> 什麼資料可以成為 canonical？人物狀態如何重播？推論如何與證據分離？系統如何證明自己沒有偷看未來、沒有把假說寫成事實，而且任何重要結果都能回到來源？

**關鍵詞：** Temporal Actor Intelligence、event sourcing、bitemporal data、provenance、canonical ledger、knowledge graph、Evidence Contract、Projection Firewall、Diligent AI、政治人物資料庫

---

## Abstract

This whitepaper translates Papers 01–08 of the AI-Native Longitudinal Actor Intelligence series into an implementable canonical architecture. The system is not a database of “truth about people.” It is a replayable, provenance-preserving, counterevidence-aware infrastructure for modeling public actors across time while strictly separating evidence from inference.

The architecture is built around immutable source artifacts, an append-only canonical ledger, event-sourced actor state, bitemporal semantics, graph projections, non-canonical vector indexes, explicit epistemic types, evidence contracts, correction lineage, and purpose-specific projection firewalls. Academic, public, and enterprise products may share canonical evidence but do not share identical inference permissions.

Core entities include SourceArtifact, EvidenceUnit, Actor, RoleAssignment, Claim, Event, Decision, Outcome, ResponsibilityEdge, Attribution, Correction, Hypothesis, Prediction, Institution, Policy, PolicyForecast, EconomicEntity, ExposureEdge, EducationRecord, CareerRecord, Challenge, EvidenceContract, ActorModelCard, and Projection.

JSON Schema 2020-12 is used as the v0.1 interchange and validation contract. Provenance is designed to map onto W3C PROV-O concepts without requiring RDF as the sole storage technology. Risk-management gates are embedded throughout the lifecycle rather than added only at publication time.

The central architectural invariants are:

$$
Canonical\ Evidence
\neq
Inference
$$

$$
Actor\ State(t)
=
Replay(Event_{\leq t})
$$

$$
Projection
\nrightarrow
Canonical\ Evidence
$$

and:

$$
Unknown
\neq
Negative
$$

WP01 defines the data truth model and safety boundaries. Continuous ingestion, agent orchestration, alerting, forecasting operations, and end-user runtime workflows are deferred to WP02.

---

# 1. Canonical Inputs

本白皮書以下列 8 篇論文作為 canonical conceptual input：

1. **Paper 01 — Longitudinal Political Actor Modeling**
2. **Paper 02 — The Discourse–Execution Gap**
3. **Paper 03 — Credit, Blame, and Responsibility Asymmetry**
4. **Paper 04 — Beyond the Political Cheat Sheet: Diligent AI**
5. **Paper 05 — The Repricing of Political Competence in the AI Era**
6. **Paper 06 — Political Actor Intelligence as Economic Infrastructure**
7. **Paper 07 — Evidence-Bounded Actor Modeling**
8. **Paper 08 — Political Elite Formation and Career Path Dependence**

WP01 不重新論證八篇論文，而將其概念轉成工程 contract。

---

# 2. Architecture Mission

系統 mission：

$$
Public\ Evidence
\rightarrow
Canonical\ Memory
\rightarrow
Replayable\ Actor\ State
\rightarrow
Bounded\ Inference
\rightarrow
PurposeSpecific\ Projection
$$

四個主要使用域：

$$
Academic
$$

$$
Public
$$

$$
Enterprise
$$

$$
InternalResearch
$$

但 canonical evidence 共用。

---

# 3. Non-Goals

WP01 明確不處理：

- 自動交易；
- 選民敏感屬性微定向；
- 私人生活監控；
- 心理疾病診斷；
- 無來源人物評分；
- 最終 Runtime Agent 排程；
- 影片生成／新聞播報；
- 自主採取政治影響行動。

因此：

$$
ActorIntelligence
\neq
PoliticalManipulationRuntime
$$

。

---

# 4. Fundamental Truth Model

系統存在四種「真相位置」：

## T0 — Source Truth

來源本身曾經存在，並具有可驗證 bytes / text / metadata。

## T1 — Canonical Evidence

系統從來源抽出的可追溯 evidence unit、claim、event 與明確關係。

## T2 — Derived State

由 T1 replay / aggregate 得到的 actor state、statistics、temporal relation。

## T3 — Inference / Projection

HYP、PRED、NORM、Policy Probability、Economic Exposure、報告與 dashboard。

因此：

$$
T0,T1
$$

是 canonical evidence domain；

$$
T2,T3
$$

永遠可重新計算。

---

# 5. Immutable Source Principle

SourceArtifact 一旦 ingest：

$$
Artifact_{id,v1}
$$

不可原地改寫。

來源修訂時：

$$
Artifact_{id,v1}
\rightarrow
Artifact_{id,v2}
$$

並建立：

$$
RevisionOf
$$

關係。

---

# 6. Append-Only Canonical Ledger

Canonical ledger 預設：

$$
AppendOnly
$$

。

錯誤修正：

$$
BadRecord
\rightarrow
CorrectionRecord
\rightarrow
ReplacementRecord
$$

而不是 destructive update。

---

# 7. Why Event Sourcing

人物 profile：

$$
Profile_A
$$

只是：

$$
Fold(EventStream_A)
$$

。

因此：

$$
ActorState_A(t)
=
Replay(
Event_A,
cutoff=t
)
$$

。

這使：

- 歷史回放；
- 模型重算；
- schema 升級；
- hindsight-safe backtest；

成為原生能力。

---

# 8. Bitemporal Semantics

至少使用兩個時間軸。

## Valid Time

事件／說法在現實世界發生或有效的時間：

$$
t_v
$$

## Record Time

系統取得／知道此資料的時間：

$$
t_r
$$

因此：

$$
Fact=
(Value,t_v,t_r)
$$

。

---

# 9. 為什麼 Record Time 必須存在

假設事件：

$$
E_{2024}
$$

在 2026 年才被解密。

若回放：

$$
Model_{2025}
$$

不得使用它。

所以 replay 條件必須同時：

$$
ValidTime\leq t
$$

且：

$$
RecordTime\leq t_{knowledge}
$$

。

---

# 10. Temporal Fields

核心 temporal fields：

- `occurred_at`
- `valid_from`
- `valid_to`
- `published_at`
- `retrieved_at`
- `recorded_at`
- `superseded_at`
- `forecast_cutoff`
- `prediction_expiry`

不是所有物件都需要全部欄位，但 semantics 固定。

---

# 11. Global Identifier Strategy

每個 canonical object 使用 stable ID：

```text
lai:<object_type>:<uuid>
```

例如：

```text
lai:actor:...
lai:event:...
lai:claim:...
```

SourceArtifact 另保存：

```text
sha256:<digest>
```

作 content identity。

---

# 12. SourceArtifact

SourceArtifact 代表原始資料。

最低欄位：

- source ID；
- URI / locator；
- publisher；
- source class；
- media type；
- published_at；
- retrieved_at；
- content hash；
- license / rights；
- language；
- access state；
- source lineage。

---

# 13. Source Class

建議枚舉：

```text
official_record
legislative_record
court_record
regulatory_record
official_release
party_document
campaign_document
speech
interview
news
academic
social_public
corporate_filing
earnings_call
other_public
```

Source class 影響 default evidence weight，但不是 truth label。

---

# 14. EvidenceUnit

EvidenceUnit 是最小可引用證據片段。

$$
EvidenceUnit
\subseteq
SourceArtifact
$$

保存：

- exact text span；
- page / timestamp / line；
- surrounding context；
- extraction method；
- language；
- checksum；
- quality metadata。

---

# 15. Full Context Contract

對高風險 quote：

$$
EvidenceUnit
=
PreContext
+
TargetSpan
+
PostContext
$$

而不是只保存 punchline。

---

# 16. Actor

Actor 是：

$$
PubliclyRelevant\ Entity
$$

可以是：

- person；
- organization；
- party；
- agency；
- institution。

但 person actor 與 organization actor 不共用人格推論。

---

# 17. Actor Alias Set

Actor 保存：

- legal / official name；
- known public aliases；
- transliterations；
- historical names；
- office labels。

Alias resolution 必須有 confidence 與 source。

---

# 18. Entity Resolution

Entity resolution 結果：

$$
Resolved
$$

$$
Ambiguous
$$

$$
Unresolved
$$

三態。

Ambiguous 不得強制合併。

---

# 19. RoleAssignment

人物不能脫離角色。

$$
Actor
+
Role
+
Institution
+
ValidTime
$$

形成 RoleAssignment。

例如：

$$
PersonA@Legislator_{2024}
$$

與：

$$
PersonA@Mayor_{2028}
$$

是兩個不同分析 context。

---

# 20. Authority Envelope

RoleAssignment 保存 Authority Envelope：

$$
A_R=
(
LegalAuthority,
BudgetAuthority,
PersonnelAuthority,
AgendaAuthority,
SupervisoryAuthority
)
$$

。

這是 Paper 02 與 Paper 06 的 execution / policy probability 基礎。

---

# 21. Claim

Claim 是 actor 對 proposition 的公開／正式表達。

最低結構：

$$
Claim=
(
Actor,
Role,
Proposition,
Time,
Scope,
Modality,
Target
)
$$

。

---

# 22. Parent Claim / Atomic Claim

複雜句：

$$
ParentClaim
$$

拆成：

$$
AtomicClaim_1,\ldots,AtomicClaim_n
$$

。

兩者都保留，禁止只存拆分後內容。

---

# 23. Claim Modality

例如：

```text
asserts
denies
supports
opposes
predicts
promises
questions
conditions
clarifies
corrects
```

。

---

# 24. Event

Event 是治理分析主要單位。

$$
Event=
(
Actors,
Roles,
Action,
Target,
Context,
Time,
Outcome
)
$$

。

---

# 25. Event Type

建議：

```text
statement
vote
bill
appointment
decision
budget_action
regulatory_action
administrative_action
campaign_action
crisis_response
policy_launch
policy_revision
policy_failure
policy_success
correction
organizational_change
economic_signal
```

。

---

# 26. Decision

Decision 不等於 Event。

Decision 明確表示：

$$
Choice(A\ over\ alternatives)
$$

。

最低欄位：

- decision maker；
- role；
- option chosen；
- alternatives known；
- rationale evidence；
- authority；
- decision time。

---

# 27. Decision Ownership

Paper 03 的 Decision Ownership 必須由 Decision object 支持。

不能從：

> 首長站在記者會前。

推出：

$$
DecisionOwner=Leader
$$

。

---

# 28. Outcome

Outcome 描述可觀察結果。

保存：

- direction；
- magnitude；
- affected scope；
- observed_at；
- measurement source；
- uncertainty；
- status。

---

# 29. Outcome Status

```text
pending
partial
successful
failed
mixed
disputed
unknown
```

。

---

# 30. ResponsibilityEdge

責任不是單一欄位。

建立：

$$
ResponsibilityEdge(
Actor,
Event,
Type,
Weight,
Evidence
)
$$

。

---

# 31. Responsibility Types

Paper 03 六類：

```text
decision
causal
role
supervisory
implementation
corrective
```

。

---

# 32. Responsibility Weight

Weight：

$$
w\in[0,1]
$$

只表示 model estimate，不表示法律判決。

每個 weight 必須有：

- method；
- evidence；
- uncertainty；
- reviewer state。

---

# 33. Attribution

Attribution 是公開「把功／責任歸給誰」。

$$
Attribution
\neq
ResponsibilityEdge
$$

。

這正是 CBRA 所需分離。

---

# 34. Attribution Target

```text
self
team
agency
ally
opponent
predecessor
other_government
contractor
citizens
environment
system
unknown
```

。

---

# 35. Correction

Correction object 代表：

$$
Failure
\rightarrow
Acknowledgment
\rightarrow
Plan
\rightarrow
Implementation
\rightarrow
Evaluation
$$

中的一個階段。

---

# 36. Correction Thread

所有 correction 串成：

$$
CorrectionThread
$$

用來計算 Paper 03 的：

$$
CCI
$$

與 Paper 04 的：

$$
CCC
$$

。

---

# 37. Epistemic Type

所有 analytical object 必須標記：

```text
OBS
DER
HYP
PRED
NORM
```

。

Canonical evidence 只能包含 OBS 與由 deterministic / declared rules 形成的低階 DER。

---

# 38. Evidence State

額外狀態：

```text
CONFIRMED
DISPUTED
UNKNOWN
UNAVAILABLE
SUPERSEDED
```

。

---

# 39. Unknown Is Not Negative

不變量：

$$
UNKNOWN
\nRightarrow
Negative
$$

。

任何 score / model：

$$
MissingEvidence
\rightarrow
Uncertainty\uparrow
$$

優先於：

$$
Mean\downarrow
$$

。

---

# 40. Derived Relation

DER 必須保存：

- derivation rule ID；
- input IDs；
- algorithm version；
- created_at；
- reviewer state。

因此：

$$
DER
\rightarrow
Replayable
$$

。

---

# 41. Hypothesis

Hypothesis 保存：

- proposition；
- scope；
- target actor / role；
- support evidence；
- counterevidence；
- alternative hypotheses；
- coverage；
- confidence decomposition；
- evidence floor；
- review state。

---

# 42. Hypothesis 不得變成 Actor Property

禁止：

```text
actor.personality = "responsibility_avoider"
```

。

允許：

```text
hypothesis.proposition =
"Within scope S, observed responses show elevated procedural reframing."
```

。

---

# 43. Prediction

Prediction 必須：

$$
Prediction=
(
TargetEvent,
Probability,
Cutoff,
Expiry,
ModelVersion,
EvidenceSet
)
$$

。

---

# 44. Prediction Replay

任何 PRED 必須支援：

```text
replay_as_of(cutoff)
```

得到當時版本。

---

# 45. Normative Judgment

NORM 永遠是 projection。

不能存入 canonical actor state。

---

# 46. EvidenceContract

EvidenceContract 綁定：

$$
Inference
\leftrightarrow
Evidence
$$

。

最低欄位：

- inference ID；
- support IDs；
- counterevidence IDs；
- corpus scope；
- coverage；
- alternative explanations；
- source independence；
- reviewer；
- last updated。

---

# 47. Source Independence

十家媒體轉載同一通稿：

$$
10\ URLs
\neq
10\ IndependentSources
$$

。

建立 SourceLineage：

$$
Source_i
\rightarrow
DerivedFrom
\rightarrow
Source_j
$$

。

---

# 48. Provenance Mapping

內部 provenance 至少可映射 W3C PROV-O：

- SourceArtifact / EvidenceUnit → `prov:Entity`
- ingestion / extraction / derivation → `prov:Activity`
- actor / publisher / extractor → `prov:Agent`
- derivation → `prov:wasDerivedFrom`
- attribution → `prov:wasAttributedTo`
- generation → `prov:wasGeneratedBy`

這是 interoperability mapping，不要求 runtime 直接使用 RDF。

---

# 49. W3C PROV-O 的角色

PROV-O 是 2013 W3C Recommendation，提供 provenance interchange ontology。

WP01 使用其概念語義，避免自創 incompatible provenance semantics。

---

# 50. JSON Schema Contract

v0.1 machine-readable interchange：

$$
JSONSchema=2020\text{-}12
$$

。

原因：

- schema 驗證成熟；
- language-neutral；
- 易於 API / storage / tests；
- 可逐步轉 OpenAPI / TypeScript / Python models。

---

# 51. Canonical Storage Is Not JSON Files

JSON Schema 是：

$$
InterchangeContract
$$

不是 storage mandate。

實作可使用：

- PostgreSQL；
- document store；
- graph DB；
- object store。

但 semantics 需一致。

---

# 52. Recommended Storage Topology

## Object Store

原始 source artifacts / snapshots。

## Relational Canonical Ledger

entities、events、time、lineage、review。

## Graph Projection

actor-role-policy-institution-economic relations。

## Vector Index

semantic retrieval acceleration。

## Analytics Store

time series、forecast metrics、calibration。

---

# 53. Vector Index Is Non-Canonical

最重要不變量：

$$
VectorIndex
\nsubseteq
CanonicalTruth
$$

。

embedding：

- 可換模型；
- 可重建；
- 可漂移；
- 不保證精確 provenance。

所以只做：

$$
CandidateRetrieval
$$

。

---

# 54. Retrieval Path

標準 retrieval：

$$
Query
\rightarrow
Vector/KeywordCandidates
\rightarrow
CanonicalIDs
\rightarrow
EvidenceUnits
\rightarrow
Reasoning
$$

。

不得：

$$
Query
\rightarrow
VectorText
\rightarrow
FinalClaim
$$

。

---

# 55. Graph Projection

Graph node：

- Actor；
- Role；
- Organization；
- Institution；
- Claim；
- Event；
- Policy；
- EconomicEntity。

Graph edge：

- held_role；
- made_claim；
- participated_in；
- decided；
- implemented；
- supervised；
- attributed_to；
- corrected；
- supports；
- opposes；
- appoints；
- controls；
- affects；
- exposed_to。

---

# 56. Graph Is Also a Projection

Graph relation 若是 DER：

必須帶 derivation。

Graph DB 不等於 canonical evidence。

---

# 57. Actor State

ActorState：

$$
State_A(t,purpose)
$$

不是永久 object，而是 projection。

包含可選：

- active roles；
- claim distribution；
- event history；
- execution evidence；
- responsibility patterns；
- policy intent；
- career path features。

---

# 58. State Must Be Purpose-Aware

Academic actor state 與 enterprise state 可能不同：

$$
State_A(t,Academic)
\neq
State_A(t,Enterprise)
$$

因為用途與允許推論不同。

---

# 59. Projection Firewall

流程：

$$
Canonical
\rightarrow
PurposePolicy
\rightarrow
RiskGate
\rightarrow
Projection
$$

。

Projection object 必須保存：

- purpose；
- audience；
- query；
- source cutoff；
- inference types；
- prohibited uses；
- generated_at；
- model version。

---

# 60. Purpose Classes

v0.1：

```text
academic
public_information
enterprise_policy_risk
internal_research
```

明確禁止：

```text
sensitive_voter_microtargeting
general_population_blacklisting
unlawful_surveillance
```

。

---

# 61. Publication Tier

Paper 07 對應：

```text
T0_internal_canonical
T1_low_risk_descriptive
T2_behavioral_pattern
T3_high_reputational_risk
T4_default_nonpublication
```

。

---

# 62. Human Review Gate

T3 至少：

$$
PrimaryEvidence
+
Counterevidence
+
IndependentReview
+
ExplicitUncertainty
$$

。

T4 預設不公開。

---

# 63. Challenge Object

任何 output 可以被 challenge。

Challenge：

- target object；
- challenger；
- reason；
- evidence；
- status；
- resolution；
- timestamps。

---

# 64. Correction Lineage

修正流程：

$$
Challenge
\rightarrow
Review
\rightarrow
Correction
\rightarrow
NewVersion
$$

。

舊版本不可消失。

---

# 65. ActorModelCard

正式 actor model 必須有：

- purpose；
- actor / role scope；
- time range；
- corpus classes；
- coverage；
- missingness；
- model version；
- known limitations；
- counterevidence status；
- prohibited uses；
- last review。

---

# 66. Coverage Model

Paper 04：

$$
CR=
\frac{|Observed|}{|Expected|}
$$

但 expected unknown 時按 source class 報告。

系統不得宣稱：

> complete

除非 scope 可枚舉且驗證。

---

# 67. Missingness

分類：

```text
not_collected
not_found
not_public
deleted
access_denied
licensing_blocked
unknown_total
```

。

Missingness 本身保留。

---

# 68. Source Ecology

Source Artifact 另標：

- official；
- partisan；
- commercial media；
- independent academic；
- self-published。

這是 incentive metadata，不是可信度絕對值。

---

# 69. Source Quality

建議 quality vector：

$$
Q_s=
(
Primaryness,
Independence,
Completeness,
Authenticity,
TemporalProximity
)
$$

。

不壓成單一分數作真理。

---

# 70. Role-Aware Comparison

比較 actor：

$$
Compare(A,B\mid Role,Authority,Exposure,Time)
$$

。

禁止：

$$
MayorFailures
$$

與：

$$
LegislatorFailures
$$

raw count 直接比。

---

# 71. Exposure Normalization

高曝光人物事件多。

統計需控制：

$$
MediaVolume
$$

$$
DecisionVolume
$$

$$
TimeInRole
$$

$$
AuthorityScale
$$

。

---

# 72. Career / Formation Objects

Paper 08 加入：

- EducationRecord；
- CareerRecord；
- PoliticalEntryRecord；
- NetworkRelation；
- FormationFeature。

---

# 73. EducationRecord

欄位：

- institution；
- field；
- degree；
- country；
- start/end；
- cohort；
- source。

Selectivity 不直接跨年代硬編碼。

---

# 74. CareerRecord

欄位：

- role；
- organization；
- sector；
- authority；
- personnel scope；
- budget scope；
- duration；
- outcomes。

---

# 75. FormationFeature

可計算：

$$
PO
$$

$$
PEC
$$

$$
NT
$$

$$
AE
$$

$$
DT
$$

$$
PDR
$$

但全部是 DER/HYP feature，不是人格。

---

# 76. Policy

Policy object：

- jurisdiction；
- domain；
- proposition；
- stage；
- responsible institutions；
- legal vehicle；
- temporal status。

---

# 77. Policy Stage

```text
idea
campaign_commitment
official_platform
draft
bill
committee
adopted
implemented
suspended
repealed
expired
```

。

---

# 78. PolicyForecast

Paper 06 PRP：

$$
PRP=
P(Intent)
P(Adoption\mid Intent)
P(Implementation\mid Adoption)
P(Persistence\mid Implementation)
$$

。

Forecast object 保存四個 component probability，不只總值。

---

# 79. Policy Forecast Must Reference Actor Role

$$
P(Intent)
$$

必須：

$$
Actor@Role
$$

而不是抽象人格。

---

# 80. EconomicEntity

EconomicEntity 可以是：

```text
industry
firm
commodity
region
infrastructure
```

。

---

# 81. ExposureEdge

$$
ExposureEdge=
(
Policy,
EconomicEntity,
Mechanism,
Direction,
Magnitude,
Duration,
Evidence
)
$$

。

---

# 82. Exposure Is Not Risk

保存：

- expected direction；
- uncertainty；
- downside；
- upside；

而非只存 risk score。

---

# 83. Mechanism Node

建議：

$$
Policy
\rightarrow
Mechanism
\rightarrow
EconomicEntity
$$

。

例如：

$$
Tariff
\rightarrow
InputCost
\rightarrow
Firm
$$

。

---

# 84. Scenario

Scenario：

$$
PoliticalState
+
PolicyState
+
EconomicState
$$

。

但 scenario 是 PRED / projection，不進 canonical evidence。

---

# 85. Ingestion Pipeline

標準流程：

1. Discover
2. Fetch
3. Snapshot
4. Hash
5. Register SourceArtifact
6. Parse / Transcribe
7. Create EvidenceUnits
8. Entity Resolution
9. Extract Claims / Events
10. Validate
11. Commit Canonical
12. Index

---

# 86. Ingestion Must Be Idempotent

同一 artifact：

$$
Ingest(x)
+
Ingest(x)
$$

不能產生兩份獨立 canonical source。

透過 content hash / canonical locator 去重。

---

# 87. Parsing Is Not Canonical by Default

OCR / ASR / HTML extraction：

$$
ParsedText
$$

是 derived representation。

必須指回原始 artifact。

---

# 88. Extraction Confidence

Claim/Event extraction 保存：

- model；
- version；
- confidence；
- extraction time；
- human verified。

---

# 89. Human Verification Queue

高風險：

- entity ambiguity；
- negative allegation；
- responsibility assignment；
- causal edge；
- re-identification risk；

進 human queue。

---

# 90. Inference Pipeline

1. Define query purpose
2. Resolve actor/role/time
3. Freeze evidence cutoff
4. Retrieve canonical evidence
5. Build DER
6. Generate candidate HYP/PRED
7. Counterevidence search
8. Alternative explanations
9. Risk gate
10. Human review if required
11. Projection
12. Log lineage

---

# 91. Freeze Evidence Cutoff

任何分析先記：

$$
t_{cutoff}
$$

。

後續新資料不能偷偷進入同一次 frozen replay。

---

# 92. Counterevidence Gate

若 HYP：

$$
SupportSearch=Done
$$

但：

$$
CounterSearch=NotDone
$$

則：

$$
Publishable=False
$$

對 T2/T3 預設如此。

---

# 93. Evidence Floor Gate

不同 inference risk：

$$
EF_{T1}<EF_{T2}<EF_{T3}
$$

。

Threshold policy 版本化。

---

# 94. Psychological Non-Diagnosis Gate

若 output 涉及：

- personality disorder；
- mental illness；
- clinical label；

但沒有明確允許來源與用途：

$$
Block
$$

。

---

# 95. Re-Identification Gate

coded case：

$$
RIR=
P(Identify\mid ReleasedFeatures)
$$

若超出 publication policy：

- generalize；
- remove unique features；
- synthesize；
- 不公開。

---

# 96. Black-Box Score Gate

若 adverse score 無法：

$$
Score
\rightarrow
Dimension
\rightarrow
Event
\rightarrow
Evidence
$$

則不能發布。

---

# 97. Replay API

概念接口：

```text
replay_actor(
  actor_id,
  valid_time_cutoff,
  record_time_cutoff,
  purpose
)
```

。

---

# 98. Evidence API

概念接口：

```text
get_evidence_path(object_id)
```

返回：

$$
Inference
\rightarrow
DER
\rightarrow
EvidenceUnit
\rightarrow
SourceArtifact
$$

。

---

# 99. Challenge API

```text
challenge(
  target_id,
  reason_code,
  evidence_ids,
  note
)
```

。

---

# 100. Projection API

```text
project_actor(
  actor_id,
  purpose,
  query,
  cutoff,
  publication_tier
)
```

。

---

# 101. Write Boundary

Runtime 必須區分：

```text
write_canonical()
write_derived()
write_inference()
write_projection()
```

。

一般 LLM Agent 不應直接有：

```text
write_canonical()
```

權限。

---

# 102. Canonical Commit Gate

canonical commit 至少需要：

- schema valid；
- provenance valid；
- source resolvable；
- time valid；
- actor resolution acceptable；
- duplicate check；
- rights metadata；
- commit log。

---

# 103. Derived Commit Gate

DER 需要：

- derivation rule；
- input IDs；
- version；
- deterministic or declared method。

---

# 104. Inference Commit Gate

HYP/PRED 需要：

- Evidence Contract；
- support；
- counterevidence state；
- alternative explanations；
- purpose；
- expiry / review date。

---

# 105. Security Domains

至少：

## Public Evidence Domain

可公開來源。

## Restricted Licensed Domain

受授權資料。

## Internal Analysis Domain

未公開研究 HYP/PRED。

## Publication Domain

通過 gate 的 projections。

---

# 106. Secrets

不得把：

- password；
- API key；
- private contact；
- non-public sensitive personal data；

寫入 actor canonical schema。

---

# 107. Access Control

ACL / RBAC 至少按：

- data domain；
- purpose；
- publication tier；
- action type；

控制。

---

# 108. Audit Log

所有：

- ingest；
- correction；
- inference；
- review；
- publication；

必須 append audit log。

---

# 109. Model Versioning

抽取／推論模型變更：

$$
Model_v1
\rightarrow
Model_v2
$$

不應直接改舊結果。

應可：

$$
Recompute
$$

並比較差異。

---

# 110. Schema Versioning

Schema object 都有：

```text
schema_version
```

。

breaking change：

$$
v0.x
\rightarrow
v1.0
$$

需 migration specification。

---

# 111. Canonical Migration

Migration 不改 source bytes。

只可：

- 新增 normalized fields；
- 重新 DER；
- 補 lineage。

---

# 112. Interoperability Strategy

v0.1：

- JSON Schema 2020-12；
- UTF-8；
- ISO 8601 timestamps；
- SHA-256 artifact hashes；
- optional W3C PROV-O mapping。

---

# 113. Verifiable Credentials — Optional, Not Core

W3C Verifiable Credentials 2.0 於 2025 成為 W3C Recommendation，可機器驗證 credential。

未來可用於：

- 官方學歷；
- 職位；
- 機構簽章文件；

但 WP01 不要求所有 evidence 都轉 VC。

---

# 114. Why Not Blockchain

WP01 不要求 blockchain。

需求是：

$$
Integrity
+
Lineage
+
Replay
$$

可由：

- hashes；
- append-only logs；
- signed snapshots；
- database controls；

達成。

---

# 115. Performance Principle

優先順序：

$$
Correctness
>
Auditability
>
Replayability
>
Latency
$$

。

但 runtime 仍可透過 index / cache 優化。

---

# 116. Cache Is Disposable

所有 cache：

$$
Disposable
$$

。

若刪除 cache，系統仍能從 canonical rebuild。

---

# 117. Incremental Maintenance

勤人 AI 不每次全量重讀。

流程：

$$
CanonicalizeOnce
+
IncrementalIngest
+
IncrementalDerivation
+
QueryProjection
$$

。

---

# 118. Minimal MVP Boundary

WP01 reference MVP：

- 10 actors；
- 5 年；
- 3 source classes；
- text + transcript；
- 1 jurisdiction；
- Claim/Event/Role/Responsibility；
- HYP + counterevidence；
- historical replay；
- evidence path。

---

# 119. MVP 非目標

第一版不需要：

- 全國所有政治人物；
- 自動政策交易；
- 100% coverage；
- 即時秒級 ingestion；
- 全自動高風險發布。

---

# 120. Acceptance Test — Replay

給定：

$$
Cutoff=2025\text{-}01\text{-}01
$$

任何 2025 之後 record time 的 evidence：

$$
MustNotAppear
$$

。

---

# 121. Acceptance Test — Canonical Pollution

向 HYP store 寫入：

> Actor is dishonest.

不得使 Actor canonical record 出現：

```text
dishonest=true
```

。

---

# 122. Acceptance Test — Unknown

缺少 executive evidence 時：

輸出：

$$
ExecutiveEvidence=UNKNOWN
$$

不得：

$$
ExecutiveScore=0
$$

。

---

# 123. Acceptance Test — Source Duplication

十篇同源轉載：

$$
IndependentEvidenceCount=1
$$

或依 lineage 計算有效獨立性。

---

# 124. Acceptance Test — Correction

來源更正後：

- 舊 source version 保留；
- 新 source version linked；
- 依賴 DER/HYP 被標記 stale；
- 可重新計算。

---

# 125. Acceptance Test — Counterevidence

T2/T3 HYP 無 counterevidence search：

$$
PublicationGate=FAIL
$$

。

---

# 126. Acceptance Test — Projection Firewall

Enterprise projection 不得自動開啟：

$$
SensitiveVoterTargeting
$$

。

---

# 127. Acceptance Test — Evidence Path

任一公開 HYP：

```text
get_evidence_path()
```

必須至少回到一個 SourceArtifact。

---

# 128. Acceptance Test — Score Decomposition

任一發布 score：

$$
Score
\rightarrow
Dimension
\rightarrow
Evidence
$$

必須可展開。

---

# 129. Observability

Runtime metrics：

- ingestion success；
- duplicate rate；
- unresolved entity rate；
- extraction error；
- stale inference count；
- replay latency；
- evidence trace failure；
- counterevidence completion；
- human review queue。

---

# 130. Quality Metrics

Paper 04 對應：

$$
CR
$$

$$
TR
$$

$$
TF
$$

$$
CEC
$$

$$
HSR
$$

$$
CCC
$$

。

但 WP01 不把 Diligence Score 當唯一 KPI。

---

# 131. Forecast Metrics

Paper 06：

- Brier Score；
- Log Loss；
- calibration；
- lead time；
- false positive / negative；
- policy-stage accuracy。

---

# 132. Data Quality Is Multi-Dimensional

$$
Quality
=
Coverage
+
Provenance
+
TemporalAccuracy
+
EntityAccuracy
+
ContextIntegrity
+
Independence
$$

。

---

# 133. Failure Mode — Context Collapse

只保存 quote，不保存前後文。

Mitigation：

$$
EvidenceUnitContext
$$

。

---

# 134. Failure Mode — Role Collapse

把同一人不同角色混成一個 persona。

Mitigation：

$$
Actor@Role
$$

。

---

# 135. Failure Mode — Hindsight Leakage

用未來資料解釋早期預測。

Mitigation：

$$
BitemporalReplay
$$

。

---

# 136. Failure Mode — Confirmation Mining

先有標籤再找證據。

Mitigation：

$$
CounterevidenceGate
+
AlternativeHypothesisRegistry
$$

。

---

# 137. Failure Mode — Citation Laundering

大量同源報導看起來像獨立證據。

Mitigation：

$$
SourceLineage
$$

。

---

# 138. Failure Mode — Vector Hallucination

embedding retrieval 回傳近似內容，被模型當原文。

Mitigation：

$$
CandidateRetrieval
\rightarrow
CanonicalFetch
$$

。

---

# 139. Failure Mode — Score Reification

使用者把 72/100 當人物真實屬性。

Mitigation：

- score decomposition；
- uncertainty；
- evidence path；
- 禁止人格化 label。

---

# 140. Failure Mode — Data Hoarding

以「勤人 AI」為名蒐集無關私人資料。

Mitigation：

$$
PublicRoleRelevance
+
PurposeLimitation
+
DataMinimization
$$

。

---

# 141. Failure Mode — Model Drift

模型更新後相同 corpus 得出不同 HYP。

Mitigation：

$$
ModelVersion
+
Replay
+
Diff
$$

。

---

# 142. Failure Mode — Silent Correction

更正後舊結論消失，無人知道。

Mitigation：

$$
CorrectionLineage
$$

。

---

# 143. Architecture Invariants

WP01 定義至少 18 條 machine-readable invariants，隨附 `lai_architecture_invariants_v0.1.json`。

其中最重要：

$$
CanonicalEvidence
\neq
Inference
$$

$$
Projection
\nrightarrow
Canonical
$$

$$
VectorIndex
\neq
SourceOfTruth
$$

$$
Unknown
\neq
Negative
$$

$$
ActorState
=
Replay
$$

。

---

# 144. Reference JSON Schema

隨附：

`lai_core_schema_v0.1.json`

使用 JSON Schema 2020-12，涵蓋 v0.1 核心：

- SourceArtifact；
- EvidenceUnit；
- Actor；
- RoleAssignment；
- Claim；
- Event；
- Hypothesis；
- Prediction；
- Projection。

這不是完整產品 schema，而是 contract seed。

---

# 145. Reference Example

隨附：

`lai_example_event_bundle_v0.1.json`

展示：

$$
SourceArtifact
\rightarrow
EvidenceUnit
\rightarrow
Actor
\rightarrow
Role
\rightarrow
Event
$$

如何被 validation。

---

# 146. WP02 Handoff

WP02 需要在 WP01 之上完成：

- continuous source connectors；
- scheduled ingestion；
- agent routing；
- query planner；
- long-horizon research；
- hypothesis generation；
- counterevidence agents；
- forecast engine；
- PRP updates；
- exposure propagation；
- alerting；
- enterprise/public reports；
- human review queues；
- cost control。

---

# 147. WP01 / WP02 Boundary

WP01：

$$
What\ is\ valid\ state?
$$

WP02：

$$
How\ does\ the\ system\ continuously\ operate?
$$

。

---

# 148. Canonical Commit Philosophy

正式規則：

$$
Validate
\rightarrow
Commit
$$

不是：

$$
Render
\rightarrow
CopyBack
$$

。

聊天畫面與 dashboard 都不是 canonical source。

---

# 149. Source-of-Truth Hierarchy

$$
SourceArtifact
>
CanonicalLedger
>
DerivedState
>
Inference
>
Projection
$$

。

箭頭代表：

> 下層可由上層重建。

反向不成立。

---

# 150. Final Architecture Equation

整體系統可壓縮：

$$
TAI=
(
S,
E,
R,
T,
I,
G,
P
)
$$

其中：

- $S$：Source artifacts；
- $E$：Evidence ledger；
- $R$：Role-aware relations；
- $T$：Bitemporal event stream；
- $I$：Evidence-bounded inference；
- $G$：Graph projections；
- $P$：Purpose-gated projections。

且必須滿足：

$$
Replay(TAI,t)
\rightarrow
Deterministic\ Canonical\ View
$$

在固定 schema / derivation version 下可重現。

---

# 151. 結論

長時序行動者智能的最大工程風險，不是資料量。

而是：

$$
Evidence
\rightarrow
Inference
\rightarrow
Profile
$$

三者在系統內慢慢混成一團。

一旦人物假說被寫回人物 profile，下一次檢索就會把舊假說當成新證據；一旦向量索引成為 source of truth，模型近似就會取代原文；一旦 record time 被忽略，回測就會偷看未來；一旦更正採 destructive update，歷史模型就無法重播。

因此 WP01 的核心不是資料庫選型，而是 canonical semantics。

最終不變量是：

$$
\boxed{
Canonical\ Evidence
\neq
Inference
}
$$

$$
\boxed{
ActorState(t)=Replay(Event_{\leq t})
}
$$

$$
\boxed{
Projection\nrightarrow Canonical
}
$$

$$
\boxed{
Unknown\neq Negative
}
$$

以及：

$$
\boxed{
Every\ important\ inference\ must\ have\ a\ replayable\ evidence\ path
}
$$

這使系統不需要假裝：

> 「AI 知道一個人真正是什麼。」

它只需要能精確回答：

> 「在某個時間點、某個角色、某個已宣告 corpus、某個用途與某個 evidence cutoff 下，哪些可觀察狀態成立；哪些只是推論；哪些資料缺失；哪些反例存在；這個結果如何被重播？」

當這些條件成立，Paper 01–08 才真正從理論變成可工程化的：

$$
\boxed{
Temporal\ Actor\ Intelligence\ Infrastructure
}
$$

。

---

# References and Standards

JSON Schema. (2026). *JSON Schema Specification — Draft 2020-12*. https://json-schema.org/specification

Lebo, T., Sahoo, S., & McGuinness, D. (Eds.). (2013). *PROV-O: The PROV Ontology*. W3C Recommendation. https://www.w3.org/TR/prov-o/

NIST. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1*. https://doi.org/10.6028/NIST.AI.100-1

NIST. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1*. https://doi.org/10.6028/NIST.AI.600-1

W3C. (2025). *Verifiable Credentials Data Model v2.0 and related Recommendations*. https://www.w3.org/news/2025/the-verifiable-credentials-2-0-family-of-specifications-is-now-a-w3c-recommendation/

---

## Canonical Source Note

本檔為 WP01 v0.1 的 UTF-8 canonical Markdown source。正式數學 source 僅使用 ` $...$ ` 與 `$$...$$` delimiter。聊天畫面、HTML、PDF、簡報、Graph UI、Vector Index、Dashboard、Actor Profile、Forecast 或任何其他 projection 均不是 canonical source。正式架構變更必須先修改 canonical source / schema，執行 validation，再 commit 新版本；不得由 rendering 反向覆寫 canonical。
