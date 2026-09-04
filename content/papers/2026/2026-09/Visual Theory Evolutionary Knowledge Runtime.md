# Visual Theory Evolutionary Knowledge Runtime
## 視覺理論演化知識執行層技術白皮書
### ——將 VUSD 的意圖、理由、共享域、反事實與演化理論落地為 AI 可操作的版本化知識 Runtime

**VUSD Series — Technical Whitepaper 01**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-31  
**定位：** Technical Whitepaper / Knowledge Runtime / EveAtelier Integration  
**相依理論：** VUSD Paper 01–05  
**目標系統：** EveAtelier / SEDB-Visual / Style Atlas / AADS / RABCL / MRMIC-NVCL / RVGR

---

# 摘要

VUSD 五篇理論建立了一個從視覺作品走向視覺理解的完整理論鏈：

$$
I_t
\rightarrow
C_t
\rightarrow
D_t
\rightarrow
P_t
\rightarrow
U_t
\rightarrow
\Pi_{O_t}
\rightarrow
M_t.
$$

其中：

- $I_t$：Creator / User Intent；
- $C_t$：Context / Constraint；
- $D_t$：Visual Decision；
- $P_t$：Perceptual / Relational Mechanism；
- $U_t$：Understanding Shared-Domain State；
- $O_t$：Observer；
- $M_t$：Experienced Meaning。

VUSD 同時區分：

$$
R=
(
R_c,
R_x,
R_f,
R_e
),
$$

其中：

- $R_c$：Creator Rationale；
- $R_x$：Contextual Cause；
- $R_f$：Functional Rationale；
- $R_e$：Evolutionary Rationale。

Paper 04 再加入：

$$
\Delta D
\rightarrow
\Delta P
\rightarrow
\Delta U
\rightarrow
\Delta M_O,
$$

並以反事實作為視覺理解的重要可操作檢驗。

Paper 05 則將整個模型時間化：

$$
VUSD
=
VUSD(t),
$$

並明確拒絕把目前的 Operator Set 凍結成永久視覺本體。

因此本白皮書提出：

# **Visual Theory Evolutionary Knowledge Runtime**
## **VTEKR**

其定位不是：

```text
藝術百科全書
風格標籤資料庫
prompt library
固定美術規則表
```

而是：

> **可由 AI 與人類共同讀寫、可追溯證據、可版本化、可反事實驗證、可演化又不任意漂移的視覺理論知識執行層。**

核心架構不變量為：

$$
\boxed{
\text{Source}
\neq
\text{Observation}
\neq
\text{Analysis}
\neq
\text{Theory}
\neq
\text{Judgment}.
}
$$

以及：

$$
\boxed{
\text{Operator Proposal}
\neq
\text{Operator Promotion}.
}
$$

$$
\boxed{
\text{Visual Edit Authority}
\neq
\text{Theory Mutation Authority}.
}
$$

$$
\boxed{
\text{Unknown}
\neq
\text{Error}.
}
$$

$$
\boxed{
\text{Current Canon}
\neq
\text{Permanent Ontology}.
}
$$

---

# 1. Runtime 的問題不是「存更多知識」

一般知識庫可以保存：

```text
印象派是什麼
某畫家常用什麼顏色
三分法是什麼
互補色是什麼
```

但 VUSD 所需的 Runtime 必須回答更複雜的查詢：

```text
這個畫家在哪個時期開始反覆使用這種構圖？
這是作者自己說的，還是後世研究者的解釋？
這個視覺決策在什麼 domain 中通常提高 salience？
有哪些反例？
如果把它移除，預期哪些 Shared-Domain State 會改變？
2026 年的 AI evaluator 與 2030 年 evaluator 是否仍給相同判斷？
這個 operator 是不是已經 split 成兩個？
目前這個 style label 在不同年代的意義有沒有 drift？
```

因此：

$$
\boxed{
\text{Visual Knowledge}
\neq
\text{Static Text Retrieval}.
}
$$

---

# 2. VTEKR 的責任邊界

VTEKR 負責：

```text
知識實體
證據來源
理論關係
版本
時間作用域
Observer Scope
Operator Lifecycle
Counterfactual Record
Promotion / Deprecation
Migration
```

VTEKR 不直接負責：

```text
像素編輯
Canvas state
Provider execution
GPU generation
最終人類審美決定
```

因此：

$$
\boxed{
\text{VTEKR}
\neq
\text{Image Editor}.
}
$$

---

# 3. 與 EveAtelier 既有權限層對齊

建議權限分工：

```text
AADS
= Visual Intelligence / planning authority

SEDB-Visual + VTEKR
= Visual knowledge / theory authority

RABCL
= Workflow compiler

MRMIC
= Persistent canvas authority

NVCL
= Observation-action runtime

RVGR
= Reflexive generation runtime

Provider
= Concrete execution backend
```

所以：

$$
\boxed{
\text{Theory Authority}
\neq
\text{Execution Authority}.
}
$$

---

# 4. Canonical Runtime Object Families

VTEKR v0.1 至少需要十二個核心 Object Family：

1. `ArtifactRecord`
2. `CreatorRecord`
3. `IntentRecord`
4. `ContextRecord`
5. `VisualDecisionRecord`
6. `RationaleRecord`
7. `SharedOperatorRecord`
8. `ObserverRecord`
9. `MeaningProjectionRecord`
10. `EvidenceRecord`
11. `CounterfactualRecord`
12. `TheoryRecord`

外加：

13. `OperatorVersionRecord`
14. `MigrationRecord`
15. `PromotionRecord`
16. `DisagreementRecord`

---

# 5. Source / Observation / Analysis / Theory 必須分離

最重要的資料不變量：

$$
\boxed{
\text{Source}
\neq
\text{Observation}
\neq
\text{Analysis}
\neq
\text{Theory}.
}
$$

例如一封畫家書信：

```text
SOURCE
```

其中一句：

> 我故意把背景壓暗，讓人物更突出。

是：

```text
SOURCE CLAIM
```

系統整理成：

```text
CreatorIntentObservation
```

再建立：

```text
IntentRecord
```

若跨作品發現：

> dark background 在 portrait domain 中常提高 figure-ground separation。

才是：

```text
Functional Rationale / Theory Candidate
```

不能直接把來源文字塞成普適理論。

---

# 6. ArtifactRecord

建議：

```json
{
  "artifactId": "artifact:...",
  "title": "...",
  "creatorRefs": [],
  "time": {},
  "medium": [],
  "sourceRefs": [],
  "rights": {},
  "semanticRefs": [],
  "revision": 1
}
```

VTEKR 不一定保存 image bytes。

可只保存：

```text
asset URI
hash
metadata
semantic graph ref
```

---

# 7. CreatorRecord

```json
{
  "creatorId": "creator:...",
  "names": [],
  "activePeriods": [],
  "roles": [],
  "sourceRefs": [],
  "trajectoryRefs": []
}
```

核心：

$$
\boxed{
Creator
=
Trajectory(t),
}
$$

不是固定風格向量。

---

# 8. IntentRecord

```json
{
  "intentId": "intent:...",
  "artifactRef": "artifact:...",
  "actorRef": "creator:...",
  "statement": "...",
  "status": "DOCUMENTED",
  "evidenceClass": "EXPLICIT_AUTHOR_STATEMENT",
  "sourceRefs": [],
  "timeScope": {},
  "confidence": 0.94,
  "alternatives": []
}
```

---

# 9. Intent Status

標準：

```text
UNKNOWN
INFERRED
SUPPORTED
DOCUMENTED
DISPUTED
```

不能用：

```text
TRUE
FALSE
```

簡化全部作者意圖。

---

# 10. Intent Evidence Classes

沿用 Paper 02：

```text
EXPLICIT_AUTHOR_STATEMENT
AUTHOR_NOTE
AUTHOR_LETTER
AUTHOR_INTERVIEW
COMMISSION_BRIEF
DESIGN_SPEC
CONTEMPORARY_DOCUMENT
HISTORICAL_DOCUMENT
SCHOLARLY_INTERPRETATION
HUMAN_ANALYST_INFERENCE
MODEL_INFERENCE
UNKNOWN
```

---

# 11. ContextRecord

```json
{
  "contextId": "context:...",
  "artifactRef": "artifact:...",
  "medium": [],
  "technology": [],
  "historical": [],
  "cultural": [],
  "economic": [],
  "political": [],
  "audience": [],
  "evidenceRefs": []
}
```

---

# 12. VisualDecisionRecord

```json
{
  "decisionId": "decision:...",
  "artifactRef": "artifact:...",
  "operatorRef": "visual.op....",
  "targetRef": "region:...",
  "parameters": {},
  "relations": [],
  "observationRefs": [],
  "confidence": 0.83
}
```

這一層只回答：

> 做了什麼。

不應偷偷放入：

> 為什麼。

---

# 13. RationaleRecord

```json
{
  "rationaleId": "rationale:...",
  "type": "FUNCTIONAL",
  "fromRefs": [],
  "toRefs": [],
  "statement": "...",
  "evidenceRefs": [],
  "counterevidenceRefs": [],
  "scope": {},
  "confidence": 0.66,
  "status": "PROVISIONAL"
}
```

---

# 14. 四類 Rationale

```text
CREATOR
CONTEXTUAL
FUNCTIONAL
EVOLUTIONARY
```

對應：

$$
R_c,R_x,R_f,R_e.
$$

---

# 15. SharedOperatorRecord

```json
{
  "operatorId": "vusd.shared.reveal_conceal",
  "currentConceptVersion": "0.1",
  "class": "RELATIONAL",
  "status": "ACTIVE",
  "definition": "...",
  "inputSchemaRef": "...",
  "outputSchemaRef": "...",
  "observerConditioned": false,
  "scope": {},
  "evidenceRefs": [],
  "lineageRefs": [],
  "versionRefs": []
}
```

---

# 16. Operator Class

Paper 03 的四類：

```text
STRUCTURAL
PERCEPTUAL
RELATIONAL
CONTEXT_CONDITIONED
```

另可有：

```text
COMPOSITE
DOMAIN_SPECIFIC
META
```

---

# 17. Bootstrap Operator Namespace

例如：

```text
vusd.shared.attention
vusd.shared.salience
vusd.shared.contrast
vusd.shared.distance
vusd.shared.reciprocity
vusd.shared.reveal_conceal
vusd.shared.uncertainty
vusd.shared.rhythm
vusd.shared.dominance
vusd.shared.tension.directional
vusd.shared.tension.relational
```

---

# 18. Operator Identity 與 Label 分離

核心：

$$
\boxed{
\text{Name}
\neq
\text{Operator Identity}.
}
$$

因此：

```json
{
  "operatorId": "vusd.shared.reciprocity",
  "labels": {
    "zh-TW": "互惠指向",
    "en": "Reciprocity"
  }
}
```

未來可換名稱，

不破壞 identity。

---

# 19. OperatorVersionRecord

```json
{
  "operatorId": "vusd.shared.reciprocity",
  "conceptVersion": "0.2",
  "previous": "0.1",
  "definition": "...",
  "scopeChange": "...",
  "evidenceDelta": [],
  "migrationNotes": []
}
```

---

# 20. Concept Version ≠ Runtime Version

分開：

```text
concept_version
schema_version
runtime_version
```

不應共用一個版本號。

---

# 21. ObserverRecord

```json
{
  "observerId": "observer:...",
  "type": "HUMAN_PROFILE",
  "culture": [],
  "time": {},
  "expertise": [],
  "genreFamiliarity": [],
  "task": [],
  "preference": {},
  "capabilities": {}
}
```

---

# 22. AI Observer

```json
{
  "observerId": "observer:ai:gpt-...",
  "type": "AI_MODEL",
  "provider": "...",
  "model": "...",
  "version": "...",
  "promptSchema": "...",
  "evaluationSchema": "..."
}
```

因此同一模型不同版本：

```text
不同 ObserverRecord
```

或具有 lineage 的 observer trajectory。

---

# 23. Observer ≠ Human-only

VTEKR 保持：

$$
\boxed{
\text{Observer}
\neq
\text{Human-only}.
}
$$

但也不宣稱：

```text
AI has human phenomenal experience
```

---

# 24. MeaningProjectionRecord

```json
{
  "projectionId": "projection:...",
  "artifactRef": "artifact:...",
  "observerRef": "observer:...",
  "sharedStateRef": "sharedstate:...",
  "meanings": [
    {
      "label": "mystery",
      "weight": 0.63
    }
  ],
  "source": "MODEL_PREDICTION",
  "confidence": 0.58
}
```

---

# 25. Projection Source

```text
HUMAN_REPORT
HUMAN_ANALYST_INFERENCE
MODEL_PREDICTION
SCHOLARLY_INTERPRETATION
HISTORICAL_RECORD
```

---

# 26. SharedDomainState

```json
{
  "sharedStateId": "sharedstate:...",
  "artifactRef": "artifact:...",
  "regionRef": null,
  "operatorStates": {
    "vusd.shared.salience": 0.82,
    "vusd.shared.reciprocity": 0.71
  },
  "extractorRef": "observer:ai:...",
  "revision": 4
}
```

---

# 27. Shared State 不要求全部 scalar

有些 operator 應是：

```text
scalar
vector
categorical
graph
distribution
```

例如：

```text
direction graph
grouping graph
reveal/conceal map
```

不能全部硬壓成：

$$
[0,1].
$$

---

# 28. EvidenceRecord

```json
{
  "evidenceId": "evidence:...",
  "type": "SCHOLARLY_INTERPRETATION",
  "sourceRef": "source:...",
  "supports": [],
  "contradicts": [],
  "time": {},
  "scope": {},
  "confidence": null
}
```

Evidence 本身不需要假裝有「真實度分數」。

---

# 29. Evidence Provenance ≠ Confidence

核心：

$$
\boxed{
\text{Confidence}
\neq
\text{Evidence Provenance}.
}
$$

模型可：

```text
confidence 0.95
```

但若 evidence 是：

```text
MODEL_INFERENCE
```

仍不能升成：

```text
DOCUMENTED AUTHOR INTENT
```

---

# 30. TheoryRecord

```json
{
  "theoryId": "theory:...",
  "statement": "...",
  "status": "PROVISIONAL",
  "scope": {},
  "supportingEvidenceRefs": [],
  "counterEvidenceRefs": [],
  "counterfactualRefs": [],
  "operatorRefs": [],
  "version": "0.1"
}
```

---

# 31. Theory Status

```text
CANDIDATE
PROVISIONAL
ACTIVE
DOMAIN_ACTIVE
DISPUTED
HISTORICAL
DEPRECATED
```

---

# 32. DisagreementRecord

若：

```text
Theory A
contradicts
Theory B
```

不要消掉其中一個。

```json
{
  "disagreementId": "disagreement:...",
  "theoryRefs": ["theory:A", "theory:B"],
  "relation": "CONTRADICTS",
  "scopeOverlap": {},
  "resolutionStatus": "UNRESOLVED"
}
```

---

# 33. Plurality by Design

核心：

$$
\boxed{
\text{Knowledge Runtime}
\neq
\text{Single Doctrine}.
}
$$

可以保存：

```text
形式主義解釋
歷史解釋
市場解釋
符號解釋
創作者自述
```

---

# 34. CounterfactualRecord

```json
{
  "counterfactualId": "cf:...",
  "artifactBefore": "artifact:A",
  "artifactAfter": "artifact:B",
  "intervention": {},
  "minimalClosure": [],
  "lockedSemantics": [],
  "expectedDeltaShared": {},
  "observedDeltaShared": {},
  "observerProjectionRefs": [],
  "evidenceType": "GENERATED_VARIANT",
  "status": "OBSERVED"
}
```

---

# 35. Counterfactual Evidence Type

```text
MODEL_SIMULATION
GENERATED_VARIANT
MANUAL_EDIT
CONTROLLED_EXPERIMENT
HUMAN_AB_TEST
HISTORICAL_VARIANT
```

---

# 36. Prediction 與 Observation 分離

$$
\boxed{
\text{Predicted Counterfactual}
\neq
\text{Observed Counterfactual}.
}
$$

所以：

```text
expectedDelta
```

與：

```text
observedDelta
```

必須分欄。

---

# 37. Counterfactual Prediction Error

$$
E_{cf}
=
d(
\widehat{\Delta U},
\Delta U_{obs}
).
$$

可作為 rationale calibration evidence。

---

# 38. Counterexample 是一級資料

Runtime 必須保存：

```text
支持案例
反例
失敗 domain
observer disagreement
```

不是只存「成功規則」。

---

# 39. Persistent Residual

對 theory：

$$
Residual
=
ObservedEffect
-
PredictedEffect.
$$

若持續偏大：

```text
可能 operator 缺失
scope 太寬
theory 定義錯
observer model 漂移
```

---

# 40. Candidate Operator Discovery

觸發：

```text
persistent residual
pattern cluster
cross-model recurrence
human analyst proposal
counterfactual discovery
```

建立：

```text
CANDIDATE_OPERATOR
```

---

# 41. Candidate Operator 最低資料

```json
{
  "candidateId": "candidateop:...",
  "temporaryLabel": "operator_candidate_7831",
  "signature": {},
  "exampleRefs": [],
  "counterexampleRefs": [],
  "proposedScope": {},
  "proposedRelations": [],
  "origin": "AI_DISCOVERED"
}
```

---

# 42. Operator Discovery ≠ Promotion

硬規則：

$$
\boxed{
\text{Operator Discovery}
\neq
\text{Operator Promotion}.
}
$$

---

# 43. PromotionRecord

```json
{
  "promotionId": "promotion:...",
  "targetRef": "candidateop:...",
  "fromStatus": "CANDIDATE",
  "toStatus": "PROVISIONAL",
  "evidenceRefs": [],
  "reviewRefs": [],
  "decision": "PROMOTE",
  "actor": "knowledge-governance:..."
}
```

---

# 44. Promotion Gate

至少：

```text
distinctiveness
definition stability
evidence sufficiency
counterfactual utility
scope clarity
counterexamples considered
compatibility
review
```

---

# 45. Self-Proposal ≠ Self-Grant

AI 可以：

```text
propose operator
propose theory
propose scope update
```

但：

$$
\boxed{
\text{AI Proposal}
\neq
\text{Canonical Admission}.
}
$$

---

# 46. Capability ≠ Authority

沿用：

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

模型「能」修改理論，

不代表它「有權」直接修改 canonical knowledge。

---

# 47. Theory Mutation Authority

建議獨立 Authority：

```text
KnowledgeGovernor
```

可由：

```text
human review
policy
multi-model evidence
automated tests
```

共同驅動。

---

# 48. Ordinary Runtime Write Path

普通 AADS / Evaluator：

```text
read canonical theory
write observations
write candidate hypotheses
write counterfactual results
```

不可：

```text
直接覆寫 canonical operator
```

---

# 49. Canonical Knowledge Commit Gate

可類比 MRMIC World write：

```text
TheoryCommitGate
```

作為 canonical knowledge 的 ordinary writer。

---

# 50. Candidate ≠ Canonical

所有：

```text
new theory
new operator
new migration
```

先進 Candidate space。

---

# 51. Knowledge Revision

每個 canonical object 有：

```text
revision
```

Mutation request 必須帶：

```text
expectedRevision
```

---

# 52. Stale Revision Fail Closed

$$
\boxed{
\text{Stale Knowledge Revision}
\Rightarrow
\text{Fail Closed}.
}
$$

避免兩個 AI 同時把 operator 改成不同定義。

---

# 53. Concept Revision 與 Evidence Append 分離

新增 evidence：

```text
append evidence
```

不一定要：

```text
bump concept version
```

只有：

```text
definition
scope
semantic relation
```

改變時才需要 concept version。

---

# 54. Operator Lifecycle State Machine

```text
CANDIDATE
↓
PROVISIONAL
↓
ACTIVE
↘
DISPUTED
↘
HISTORICAL
↘
DEPRECATED
```

另有：

```text
FORKED
MERGED
```

---

# 55. Fork

```json
{
  "operation": "FORK",
  "source": "vusd.shared.tension.v0.1",
  "targets": [
    "vusd.shared.tension.directional",
    "vusd.shared.tension.relational"
  ]
}
```

---

# 56. Merge

```json
{
  "operation": "MERGE",
  "sources": ["operator:A", "operator:B"],
  "target": "operator:C"
}
```

---

# 57. Deprecation

Deprecated object：

```text
仍可查
仍可重現歷史分析
不建議新分析預設使用
```

---

# 58. Historical ≠ Deprecated

```text
HISTORICAL
```

表示：

> 在特定歷史範圍仍有描述價值。

`DEPRECATED` 則表示：

> 概念模型本身已不建議使用。

---

# 59. MigrationRecord

```json
{
  "migrationId": "migration:...",
  "fromRef": "operator:old",
  "toRefs": ["operator:newA", "operator:newB"],
  "mapping": "PARTIAL",
  "unresolved": [],
  "strategy": "REVIEW_REQUIRED"
}
```

---

# 60. Unresolved Mapping

若不能安全轉換：

```text
UNRESOLVED
```

而不是猜。

$$
\boxed{
\text{Unresolved Semantic Migration}
\Rightarrow
\text{Fail Closed}.
}
$$

---

# 61. Unknown-field Preservation

Schema 新版本增加欄位時，

舊 Runtime 應盡量：

```text
read known fields
preserve unknown fields
round-trip unknown data
```

避免資料被舊 client 洗掉。

---

# 62. Extension Namespace

建議：

```text
vusd.core.*
vusd.shared.*
vusd.domain.character.*
vusd.domain.film.*
vusd.experimental.*
vendor.*
lab.*
```

---

# 63. Domain Layer

例如：

```text
vusd.domain.character.bodyline_salience
vusd.domain.character.gaze_reciprocity
vusd.domain.character.garment_reveal_conceal
```

建立在 Shared Core 上。

---

# 64. Domain Constraint ≠ Ontological Closure

Runtime schema 必須支持：

```text
new domain
new operator family
```

而不是寫死：

```text
character
landscape
film
```

---

# 65. Artist Model

未來 Artist Archive：

```json
{
  "artistId": "creator:...",
  "trajectory": [
    {
      "timeScope": {},
      "decisionDistributionRefs": [],
      "sharedStateDistributionRefs": [],
      "intentEvidenceRefs": [],
      "rationaleRefs": [],
      "historicalContextRefs": []
    }
  ]
}
```

---

# 66. Artist ≠ One Style Vector

核心：

$$
\boxed{
Artist
=
Trajectory(t).
}
$$

---

# 67. StyleProfile

```json
{
  "styleProfileId": "styleprofile:...",
  "creatorRef": "creator:...",
  "timeScope": {},
  "surfaceFeatures": {},
  "decisionDistribution": {},
  "sharedDomainDistribution": {},
  "rationaleRefs": [],
  "counterfactualBoundaryRefs": []
}
```

---

# 68. Style Atlas Query

未來 Style Atlas 可問：

```text
找同樣 surface 但不同 relational syntax
找同樣 composition rhythm 但不同 palette
找同樣 shared-domain profile 的不同畫家
找某畫家的早期 vs 晚期 operator drift
```

---

# 69. Style Similarity 多層化

$$
Sim_{style}
=
(
Sim_{surface},
Sim_{decision},
Sim_{shared},
Sim_{context}
).
$$

不能只用一個 embedding cosine。

---

# 70. Style Boundary

Paper 04 的 Counterfactual Boundary：

```text
改哪些東西仍像同系列？
```

可存：

```json
{
  "boundaryId": "boundary:style:...",
  "lockedDimensions": [],
  "tolerances": {},
  "observedFailures": []
}
```

---

# 71. Observer Trajectory

```text
observer v1
→ observer v2
→ observer v3
```

保存：

```text
model/version
training cut-off
evaluation schema
time
```

---

# 72. Judgment Record

```json
{
  "judgmentId": "judgment:...",
  "artifactRef": "artifact:...",
  "observerRef": "observer:...",
  "theorySnapshotRef": "snapshot:...",
  "result": {},
  "time": "..."
}
```

---

# 73. Theory Snapshot

每次正式 evaluation 可綁：

```text
operator versions
theory versions
observer version
```

形成可重現：

```text
VisualTheorySnapshot
```

---

# 74. Re-evaluation ≠ Historical Rewrite

新 evaluator 可重評，

但舊 judgment 不刪。

```text
judgment:v1
judgment:v2
```

並列。

---

# 75. Judgment Lineage

```json
{
  "previousJudgmentRef": "...",
  "changeReason": "observer_model_update"
}
```

---

# 76. Audience Profile

```json
{
  "audienceId": "audience:...",
  "timeScope": {},
  "culture": [],
  "market": [],
  "genreFamiliarity": [],
  "appealProfile": {}
}
```

---

# 77. Appeal 不固定

$$
A_t
\neq
A_{t+1}.
$$

所以：

```text
Audience Appeal Lock
```

必須綁特定：

```text
source artifact
audience profile
time scope
```

---

# 78. AADS Query Interface

AADS 可查：

```text
get_visual_rationales(artifact)
get_operator_candidates(target_shared_state)
get_locked_semantics(artifact)
get_counterfactual_history(artifact)
get_style_boundary(style)
get_theory_snapshot(domain)
```

---

# 79. AADS 不直接讀原始資料庫表

建議透過：

```text
VTEKR Query API
```

避免 AADS 耦合 schema internals。

---

# 80. Suggested Query API

```text
resolve_artifact_context()
infer_visual_decisions()
resolve_rationales()
resolve_shared_state()
resolve_observer_projection()
search_counterfactuals()
search_theories()
get_operator_version()
```

---

# 81. Mutation API

普通 client：

```text
append_observation()
append_evidence()
propose_rationale()
propose_operator()
record_counterfactual()
record_judgment()
```

治理 client：

```text
promote_operator()
fork_operator()
merge_operator()
deprecate_operator()
migrate_knowledge()
```

---

# 82. RABCL Integration

RABCL 可以編譯：

```text
Intent
→ Shared Target
→ Visual Operator Plan
```

但 RABCL 不應：

```text
改寫 theory ontology
```

---

# 83. RABCL Workflow Node Example

```json
{
  "nodeType": "VUSD_SHARED_TARGET",
  "target": {
    "reciprocity": "retain",
    "reveal_conceal": "retain",
    "subject_salience": "increase"
  },
  "theorySnapshotRef": "snapshot:..."
}
```

---

# 84. RVGR Integration

RVGR 在生成中：

```text
observe generation
extract shared-state drift
compare target
propose rewrite
```

但：

$$
\boxed{
\text{In-loop Observation}
\neq
\text{Final Acceptance}.
}
$$

---

# 85. RVGR Observation Record

```json
{
  "generationRef": "...",
  "checkpoint": 12,
  "sharedState": {},
  "drift": {},
  "observerRef": "..."
}
```

---

# 86. RVGR 可以回報 Theory Residual

如果：

```text
expected effect
```

反覆不成立，

RVGR 可：

```text
propose theory residual
```

但不能自行 promotion。

---

# 87. MRMIC / NVCL Integration

MRMIC 保存：

```text
canonical canvas / document state
```

NVCL 提供：

```text
observe / act
```

VTEKR 保存：

```text
why / relation / theory / evidence
```

因此：

$$
\boxed{
\text{Canvas State}
\neq
\text{Theory State}.
}
$$

---

# 88. Asset State ≠ Knowledge State

圖片刪除、

版本切換，

不一定刪除歷史：

```text
counterfactual evidence
judgment
theory
```

---

# 89. Rights / Provenance

ArtifactRecord 需保留：

```text
rights
source
redistribution status
```

因為畫家建檔、作品建檔與公開展示不是同一件事。

---

# 90. Reference Role

Style Atlas / SEDB-Visual 可沿用：

```text
STYLE_CORE_REFERENCE
IDENTITY_REFERENCE
FACE_REFERENCE
PROPORTION_REFERENCE
POSE_REFERENCE
COSTUME_REFERENCE
COLOR_REFERENCE
LINE_REFERENCE
LIGHTING_REFERENCE
COMPOSITION_REFERENCE
NEGATIVE_REFERENCE
```

---

# 91. Reference ≠ Theory

一張 reference：

```text
可以作 evidence / example
```

但不應：

```text
自動成為 theory
```

---

# 92. Visual Theory Snapshot

建議：

```json
{
  "snapshotId": "snapshot:...",
  "domain": "character_art",
  "operatorVersions": {},
  "theoryVersions": {},
  "schemaVersion": "0.1",
  "createdAt": "..."
}
```

---

# 93. Deterministic Replay

若：

```text
artifact
observer
snapshot
evaluation schema
```

固定，

應盡量可重放 evaluation。

生成式 evaluator 仍可能有隨機性，

需記：

```text
seed / sampling settings
```

若支援。

---

# 94. Explanation Record

每個正式 judgment 建議輸出：

```text
Finding
Rationale
Evidence
Scope
Uncertainty
Counterfactual suggestion
```

而不是只：

```text
score
```

---

# 95. Natural-Language Rationale

VUSD 強調：

$$
\boxed{
\text{Formal Representation}
+
\text{Natural-Language Rationale}.
}
$$

所以每個 Operator / Theory 可有：

```text
formal schema
plain-language explanation
examples
counterexamples
historical notes
```

---

# 96. Language Versioning

自然語言 explanation 本身也可版本化。

例如：

```text
explanationVersion
```

不一定等於 conceptVersion。

---

# 97. Multi-language

同一 theory：

```text
zh-TW
en
ja
...
```

應共享：

```text
theoryId
```

避免每種語言變不同 ontology。

---

# 98. Historical Interpretation Layer

藝術史內容至少：

```text
creator evidence
contemporary interpretation
later scholarship
modern model inference
```

分欄。

---

# 99. Anachronism Flag

```text
ANACHRONISTIC_TERM
MODERN_INTERPRETATION
HISTORICAL_TERM
```

例如用：

```text
cinematic
```

描述攝影術之前作品時，

應標：

```text
modern analogy
```

---

# 100. Unknown 必須是一級狀態

以下皆合法：

```text
UNKNOWN_INTENT
UNKNOWN_RATIONALE
UNKNOWN_OPERATOR
UNKNOWN_OBSERVER_EFFECT
UNRESOLVED_MIGRATION
```

---

# 101. Unknown ≠ Null Everywhere

不同：

```text
null
unknown
not_applicable
not_observed
not_supported
```

應分開。

---

# 102. Semantic State Values

建議：

```text
KNOWN
UNKNOWN
UNOBSERVED
NOT_APPLICABLE
DISPUTED
UNRESOLVED
```

---

# 103. Storage Model

VTEKR 適合：

```text
relational core
+
graph relations
+
document/evidence store
+
vector retrieval
```

不建議只靠一種 DB。

---

# 104. Canonical IDs

建議所有實體有穩定 ID：

```text
creator:
artifact:
intent:
context:
decision:
rationale:
operator:
observer:
theory:
counterfactual:
evidence:
```

---

# 105. Graph Relation

核心 relation：

```text
supports
contradicts
derived_from
interprets
causes_candidate
projects_to
observed_in
applies_to
specializes
generalizes
forked_from
merged_from
supersedes
```

---

# 106. Retrieval Layer

AI Query 可以：

```text
semantic retrieval
graph traversal
time filtering
scope filtering
evidence filtering
```

混合。

---

# 107. Search Intent

例如：

> 為什麼這張角色圖看起來更有危險吸引力？

Runtime 可查：

1. artifact decisions；
2. Shared-domain states；
3. domain theories；
4. relevant appeal/tension models；
5. observer profile；
6. counterfactual evidence。

---

# 108. Do Not Let Retrieval Become Truth

Top-1 retrieval：

$$
\not\Rightarrow
$$

canonical answer。

AI 還需要：

```text
evidence comparison
scope check
conflict check
```

---

# 109. Theory Applicability Gate

在使用 Theory $T$ 前：

```text
domain match?
time scope match?
observer scope match?
medium match?
status active?
counterevidence?
```

---

# 110. Applicability Score

可以：

$$
A(T,q)
=
f(
ScopeMatch,
EvidenceStrength,
VersionCompatibility,
Counterevidence
).
$$

但不應把 score 當 absolute truth。

---

# 111. Conflict-aware Retrieval

若兩個 theory：

```text
contradict
```

結果中應一起回傳。

---

# 112. Evidence-first Response

AI 回答最好：

```text
Known:
...

Strongly supported:
...

Plausible:
...

Alternative:
...

Unknown:
...
```

---

# 113. Operator Discovery Queue

新 pattern：

```text
candidate queue
```

可排序：

$$
Priority
=
PersistentResidual
+
CrossArtifactRecurrence
+
CounterfactualUtility
-
ComplexityCost.
$$

---

# 114. Operator Novelty Threshold

避免 AI 無限發明術語。

需要：

```text
minimum recurrence
minimum explanatory gain
minimum distinctness
```

---

# 115. Composite-first Policy

若新候選可以表示為：

$$
Compose(O_a,O_b,O_c),
$$

優先：

```text
COMPOSITE_OPERATOR
```

而不是新 primitive。

---

# 116. Primitive Promotion Gate

只有：

```text
不可有效分解
具穩定獨立效果
```

才升：

```text
PRIMITIVE_CANDIDATE
```

---

# 117. Complexity Budget

Knowledge Runtime 也有 complexity cost。

$$
Utility_{new}
=
ExplanationGain
+
RevisionUtility
-
ComplexityCost.
$$

---

# 118. Dynamic Canon Layers

建議：

```text
Canonical Core
Domain Canon
Provisional
Experimental
Historical
Deprecated
```

---

# 119. Canonical Core

跨 domain 高穩定，

但仍不是永久 universal。

---

# 120. Domain Canon

例如：

```text
character_art
film
UI
```

各自 canonical operator family。

---

# 121. Provisional

有 evidence，

但尚不足升 canonical。

---

# 122. Experimental

AI / 人類探索中的新語法。

---

# 123. Historical

為重現歷史分析保留。

---

# 124. Deprecated

不建議新任務預設使用，

但 lineage 不刪。

---

# 125. Theory Snapshot Promotion

正式 production evaluator 應綁：

```text
approved snapshot
```

而不是直接讀：

```text
latest experimental theory
```

---

# 126. Experimental Theory ≠ Production Default

$$
\boxed{
\text{Experimental Knowledge}
\neq
\text{Production Canon}.
}
$$

---

# 127. Safety 與 Aesthetic 不應混成一層

沿用既有：

$$
\boxed{
\text{Safety Constraint}
\neq
\text{Conservative Aesthetic}.
}
$$

VTEKR 可以保存：

```text
safety constraint
aesthetic effect
audience appeal
```

但不可互相替代。

---

# 128. Character-Specific Expressive Override

Style Core 不應洗掉：

```text
性感
華麗
危險
高飽和
透明材質
```

等角色特有語義。

所以可保存：

```text
CharacterExpressiveProfile
```

---

# 129. Expressive Profile

```json
{
  "identityRef": "...",
  "paletteBias": {},
  "materialBias": {},
  "tensionProfile": {},
  "audienceAppealProfile": {},
  "styleOverridePolicy": {}
}
```

---

# 130. Style Core ≠ Character Expression

$$
\boxed{
\text{Style Core}
\neq
\text{Character-Specific Expression}.
}
$$

---

# 131. Evaluation Pipeline

建議：

$$
Observe
\rightarrow
DecisionExtraction
\rightarrow
SharedState
\rightarrow
TheoryBinding
\rightarrow
ObserverProjection
\rightarrow
Judgment.
$$

---

# 132. Explainability Pipeline

再輸出：

```text
what changed
why it matters
which theory applies
what evidence supports it
what remains uncertain
what counterfactual could test it
```

---

# 133. Counterfactual Planning Pipeline

$$
Goal
\rightarrow
TargetU
\rightarrow
CandidateD
\rightarrow
MinimalClosure
\rightarrow
Intervention
\rightarrow
Observe
\rightarrow
Update.
$$

---

# 134. Learning Pipeline

$$
Prediction
\rightarrow
Outcome
\rightarrow
Residual
\rightarrow
TheoryUpdateProposal.
$$

---

# 135. Theory Update 不應直接在線修改 canonical

生產 runtime：

```text
append evidence
append residual
```

離線／治理流程：

```text
review
promote
migrate
```

---

# 136. Batch Revalidation

新模型／新 domain 出現時：

```text
revalidate high-impact operators
```

而非全部盲重算。

---

# 137. Revalidation Priority

$$
Priority=
Usage
+
DriftRisk
+
ObserverDisagreement
+
NewMediumImpact.
$$

---

# 138. Regression Test

Operator 改版後需測：

```text
known examples
counterexamples
historical cases
style preservation cases
observer cases
```

---

# 139. Knowledge Regression

若新版：

```text
解釋更多
```

但造成：

```text
大量舊案例錯誤
```

需阻止 promotion。

---

# 140. Rollback

Theory version 可以：

```text
rollback active pointer
```

但不刪新版失敗版本。

---

# 141. Audit Log

所有：

```text
promotion
fork
merge
deprecation
migration
rollback
```

必須 durable log。

---

# 142. Reproducible Research

每篇研究或實驗可引用：

```text
theory snapshot
operator version
observer model
artifact hash
```

提高重現性。

---

# 143. Privacy / Proprietary Works

私人作品可建立：

```text
private semantic record
```

但：

```text
raw asset
```

不必公開。

---

# 144. Knowledge Derived from Private Asset

若 theory 來自私人資產：

```text
可保存抽象研究結論
```

但要保留：

```text
source visibility / rights constraint
```

---

# 145. Public Knowledge Export

輸出時可：

```text
strip private asset refs
keep abstract evidence statistics
```

但不能偽造來源。

---

# 146. Artist Archive Ingestion Workflow

建議：

```text
1. register creator
2. ingest works metadata
3. extract observable decisions
4. bind historical context
5. ingest explicit intent evidence
6. infer candidate rationale
7. extract shared-domain profile
8. run counterfactual tests where possible
9. create trajectory
10. human / AI review
```

---

# 147. 不要求一次全部完成

Artist profile 可以：

```text
metadata_only
pending_visual_analysis
partial_evidence
```

漸進建立。

---

# 148. Unknown Intent 是正常狀態

大量歷史藝術：

```text
intent unknown
```

不影響：

```text
functional analysis
```

---

# 149. Automated Artist Profiling

AI 可以先做：

```text
candidate decisions
candidate style profile
candidate rationale
```

全部標：

```text
MODEL_INFERENCE
```

---

# 150. Scholar / Human Review

人類可以：

```text
confirm
reject
refine
add evidence
```

但也不會把 human inference 自動變史實。

---

# 151. Cross-AI Analysis

多個 AI 對同作品分析。

可保存：

```text
model-specific observations
```

再比較：

$$
Agreement.
$$

---

# 152. Consensus ≠ Truth

即使十個 AI 都同意：

$$
\not\Rightarrow
$$

作者真的這樣想。

但可提升：

```text
shared-domain relation hypothesis
```

的穩定度。

---

# 153. Cross-Observer Agreement

$$
S(u_i)
=
f(
Agreement,
Transfer,
CounterfactualStability
).
$$

作為 Sharedness Score。

---

# 154. Sharedness 隨時間更新

$$
S_t(u_i).
$$

---

# 155. Drift Monitor

定期觀察：

```text
operator meaning drift
observer drift
style drift
audience drift
```

---

# 156. Drift ≠ Automatic Mutation

檢測到 drift：

```text
PROPOSE_UPDATE
```

而不是：

```text
AUTO_REWRITE_CANON
```

---

# 157. Proposed Meta-Operator Family

```text
vusd.meta.operator_discover
vusd.meta.operator_hypothesize
vusd.meta.operator_promote
vusd.meta.operator_split
vusd.meta.operator_merge
vusd.meta.operator_deprecate
vusd.meta.scope_rebind
vusd.meta.evidence_append
vusd.meta.observer_recalibrate
vusd.meta.snapshot_create
```

---

# 158. Meta-Operator Authority

$$
\boxed{
\text{Meta-Operator Authority}
>
\text{Ordinary Visual Edit Authority}
}
$$

但只在知識治理域。

---

# 159. Security / Governance Boundary

Provider 或外部模型不得：

```text
直接提交 canonical theory mutation
```

只能：

```text
submit proposal / evidence
```

---

# 160. Untrusted External Evidence

外部 AI / web / user source：

```text
untrusted-by-default
```

需：

```text
provenance
verification
```

---

# 161. Source Quality 不應全域固定

不同研究問題需要：

```text
不同 source hierarchy
```

例如作者意圖最重作者來源，

functional effect 可能更重實驗。

---

# 162. Evidence Weight by Claim Type

所以：

$$
Weight(E)
=
f(
EvidenceType,
ClaimType
).
$$

不是固定：

```text
academic paper > everything
```

---

# 163. Claim Type

```text
AUTHOR_INTENT
HISTORICAL_FACT
FUNCTIONAL_EFFECT
OBSERVER_RESPONSE
EVOLUTIONARY_RATIONALE
```

---

# 164. Claim-aware Evidence Resolver

API：

```text
resolve_evidence(claim_type, claim)
```

---

# 165. Data Separation

推薦物理層：

```text
raw sources
observations
semantic records
canonical theory
experimental theory
audit
```

分區。

---

# 166. Backup / Export

至少支援：

```text
JSONL
graph export
markdown synthesis
snapshot bundle
```

方便跨 AI 使用。

---

# 167. Canonical Markdown Export

每個 theory 可導出：

```text
Definition
Scope
Evidence
Counterevidence
Examples
Counterexamples
Version History
```

方便人讀。

---

# 168. Machine-native Export

同時導出：

```text
JSON / graph
```

供 AI runtime。

---

# 169. Human-readable ≠ Machine-readable

兩者都要。

$$
\boxed{
\text{Human-readable Theory}
+
\text{Machine-operable Theory}.
}
$$

---

# 170. API-level Invariants

## VTEKR-I1

$$
\boxed{
\text{Source}
\neq
\text{Observation}.
}
$$

## VTEKR-I2

$$
\boxed{
\text{Observation}
\neq
\text{Analysis}.
}
$$

## VTEKR-I3

$$
\boxed{
\text{Analysis}
\neq
\text{Canonical Theory}.
}
$$

## VTEKR-I4

$$
\boxed{
\text{Inferred Intent}
\neq
\text{Known Intent}.
}
$$

## VTEKR-I5

$$
\boxed{
\text{Operator Proposal}
\neq
\text{Operator Promotion}.
}
$$

## VTEKR-I6

$$
\boxed{
\text{Visual Edit Authority}
\neq
\text{Theory Mutation Authority}.
}
$$

## VTEKR-I7

$$
\boxed{
\text{Predicted Counterfactual}
\neq
\text{Observed Counterfactual}.
}
$$

## VTEKR-I8

$$
\boxed{
\text{Experimental Knowledge}
\neq
\text{Production Canon}.
}
$$

## VTEKR-I9

$$
\boxed{
\text{Stale Knowledge Revision}
\Rightarrow
\text{Fail Closed}.
}
$$

## VTEKR-I10

$$
\boxed{
\text{Unknown}
\neq
\text{Error}.
}
$$

## VTEKR-I11

$$
\boxed{
\text{Current Canon}
\neq
\text{Permanent Ontology}.
}
$$

## VTEKR-I12

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

---

# 171. MVP 範圍

VTEKR 第一個 MVP 不需要完整藝術史。

建議只做：

# **Character Art Domain MVP**

原因：

```text
EveAtelier 已有角色圖實驗
Style Control 已建立
Appeal / Exposure / Tension 已有 domain models
RVGR 可直接使用
```

---

# 172. MVP Core Objects

只實作：

```text
Artifact
VisualDecision
SharedOperator
SharedState
Rationale
Evidence
Observer
Counterfactual
Theory
```

---

# 173. MVP Operator Set

先固定約：

```text
salience
contrast
direction
reciprocity
distance
reveal_conceal
repetition
symmetry
dominance
uncertainty
tension.directional
tension.relational
```

---

# 174. MVP 不聲稱完整

README 必須寫：

```text
Bootstrap operator set.
Not a final visual ontology.
```

---

# 175. MVP Query 1

```text
analyze_artifact(artifact)
```

輸出：

```text
decisions
shared state
rationale candidates
uncertainty
```

---

# 176. MVP Query 2

```text
compare_artifacts(A, B)
```

輸出：

```text
ΔDecision
ΔSharedState
possible meaning changes
```

---

# 177. MVP Query 3

```text
predict_counterfactual(A, intervention)
```

---

# 178. MVP Query 4

```text
record_observed_counterfactual(A, B)
```

校準：

$$
E_{cf}.
$$

---

# 179. MVP Query 5

```text
query_style_boundary(style)
```

---

# 180. MVP Query 6

```text
get_visual_rationale(decision)
```

帶：

```text
scope
evidence
alternatives
```

---

# 181. MVP Mutation

只允許：

```text
append evidence
append observation
propose rationale
propose operator
```

Canonical promotion 暫時人工。

---

# 182. Phase 1

## VTEKR-1 — Canonical Schema

建立：

```text
IDs
objects
revision
evidence relation
```

---

# 183. Phase 2

## VTEKR-2 — Bootstrap Operator Registry

12–20 個 operator。

---

# 184. Phase 3

## VTEKR-3 — Character Art Adapter

接：

```text
Exposure
Tension
Audience Appeal
Style Control
```

---

# 185. Phase 4

## VTEKR-4 — Counterfactual Store

記：

```text
prediction
variant
observed delta
```

---

# 186. Phase 5

## VTEKR-5 — AADS Query Bridge

讓 AADS：

```text
why / target shared state
```

可查。

---

# 187. Phase 6

## VTEKR-6 — RVGR Observation Bridge

生成中回傳：

```text
shared-domain drift
```

---

# 188. Phase 7

## VTEKR-7 — Operator Proposal Queue

Residual-driven candidate。

---

# 189. Phase 8

## VTEKR-8 — Governance / Promotion

加入：

```text
review
promotion
fork
merge
deprecate
```

---

# 190. Phase 9

## VTEKR-9 — Artist Trajectory

開始畫家建檔。

---

# 191. Phase 10

## VTEKR-10 — Cross-domain Expansion

再擴：

```text
film
UI
painting
animation
```

---

# 192. MVP 驗證問題

## V1

同一 artifact 多次分析是否能穩定抽取主要 decision？

## V2

不同 AI 是否在 selected shared operators 上有可測 agreement？

## V3

Counterfactual prediction 是否優於純 caption-based prediction？

## V4

加入 Shared-domain diagnosis 後，RVGR repair 是否更精準？

## V5

Style-only transformation 是否降低 semantic drift？

## V6

Operator Proposal 是否能避免無限術語爆炸？

## V7

Theory version migration 是否可重放？

---

# 193. 成功標準

第一階段不要求：

```text
AI 理解所有藝術
```

只要求：

1. 資料層不混淆；
2. evidence lineage 可追；
3. counterfactual 可記；
4. operator 有版本；
5. observer 有版本；
6. theory 可以 competing；
7. unknown 可保存；
8. AADS / RVGR 可查；
9. canonical mutation 有 gate；
10. schema 可擴充。

---

# 194. 非目標

v0.1 不做：

```text
Universal Beauty Score
Global Artist Ranking
Final Art Ontology
Automatic Art-history Truth Engine
Automatic Canon Mutation
```

---

# 195. 最大風險一：Theory Hallucination

AI 很會：

```text
合理解釋
```

但：

```text
合理
```

不等於：

```text
有 evidence
```

防護：

```text
evidence class
intent status
alternative explanation
UNKNOWN
```

---

# 196. 最大風險二：Ontology Explosion

AI 發明太多 operator。

防護：

```text
composite-first
novelty threshold
complexity budget
promotion gate
```

---

# 197. 最大風險三：Ontology Fossilization

反過來 canonical 太穩，

新藝術無法進入。

防護：

```text
experimental edge
candidate operator
residual monitor
open extension namespace
```

---

# 198. 最大風險四：Observer Collapse

把：

```text
human
AI
culture
era
```

壓成一個 universal observer。

防護：

```text
ObserverRecord
ProjectionRecord
time scope
```

---

# 199. 最大風險五：Historical Hallucination

把現代術語投射到歷史作者。

防護：

```text
anachronism flag
source lineage
historical vs modern interpretation
```

---

# 200. 最大風險六：Aesthetic Default Convergence

Runtime 的「最佳實務」最後變成：

```text
所有圖都同一種好看
```

防護：

```text
style boundary
artist trajectory
rare operator preservation
domain canon
observer plurality
```

---

# 201. 最大風險七：AI Theory Self-lock

AI 自己提出 theory，

自己 promotion，

自己用 theory 評估，

最後形成封閉回音室。

防護：

$$
\boxed{
\text{Generator}
\neq
\text{Observer}
\neq
\text{Judge}
\neq
\text{Theory Governor}.
}
$$

---

# 202. 最低治理架構

```text
Proposal
↓
Evidence
↓
Independent Evaluation
↓
Counterfactual Test
↓
Review
↓
Promotion
```

---

# 203. 可選 Multi-model Review

不同模型：

```text
proposer
critic
counterfactual evaluator
```

角色分開。

但不是 v0.1 必須。

---

# 204. Human Authority

某些：

```text
aesthetic preference
historical interpretation
canonical research claim
```

仍適合 human review。

---

# 205. Human ≠ Always Correct

但 human review 也：

```text
有 provenance
有 disagreement
```

而不是不可追蹤的 final truth。

---

# 206. 最終架構

$$
\boxed{
\text{VTEKR}
=
\text{Versioned Visual Theory Graph}
+
\text{Evidence Graph}
+
\text{Observer Registry}
+
\text{Counterfactual Store}
+
\text{Operator Ecology}
+
\text{Promotion Governance}
}
$$

---

# 207. 與整個 EveAtelier 的最終關係

完整：

```text
Human / AI Intent
        ↓
      AADS
        ↓
      VTEKR
  rationale / theory
        ↓
      RABCL
        ↓
Operator Plan
        ↓
MRMIC / NVCL / RVGR
        ↓
   Provider Execution
        ↓
     Artifact
        ↓
     Observer
        ↓
     VTEKR
 evidence / residual
        ↓
Theory Proposal / Update
```

這形成：

# **Visual Intelligence Learning Loop**

---

# 208. 這不是讓 AI 永遠服從舊理論

反而是：

> 讓 AI 能夠知道現在使用的是哪一套理論、它的證據在哪、它的適用域在哪，以及什麼時候應該懷疑它。

因此：

$$
\boxed{
\text{Theory-aware AI}
\neq
\text{Theory-bound AI}.
}
$$

---

# 209. 最終命題

一套 AI-native 美術知識系統不應只是：

```text
更多畫風
更多 artist embeddings
更多 rules
更多 prompt templates
```

它真正需要的是：

$$
\boxed{
\text{可追溯的理由}
+
\text{可操作的共享域}
+
\text{可驗證的反事實}
+
\text{可演化的算子}
+
\text{可版本化的觀察者}
}
$$

---

# 210. 結論

VUSD 五篇理論提出了一個核心問題：

> AI 是否能從「看見作品」走向「理解作品為什麼這樣存在」？

VTEKR 則回答：

> 如果要把這種理解變成真正能被系統使用的能力，我們需要什麼資料結構與治理機制？

答案不是建立一本更厚的美術百科。

而是建立一個：

```text
有來源
有觀察
有推論
有證據
有反例
有 Observer
有版本
有時間
有反事實
有競爭理論
有 Operator Lifecycle
```

的動態知識執行層。

最重要的不變量仍然是：

$$
\boxed{
\text{現在的理論}
\neq
\text{未來的全部美術}.
}
$$

所以 VTEKR 必須同時具備兩個看似矛盾的能力：

```text
足夠穩定，讓 AI 今天能工作；
足夠開放，讓明天的新美術不必服從今天的分類。
```

最終：

$$
\boxed{
\text{Stable Canon}
+
\text{Experimental Edge}
+
\text{Evidence-driven Evolution}
}
$$

才是 VUSD 從理論走向 AI-native Visual Intelligence Runtime 的合理工程形態。

---

**End of VUSD Technical Whitepaper 01 — v0.1**
