---
title: "Generative Seed Runtime Architecture：生成種子抽取、重建、驗證與持久化參考架構"
english_title: "Generative Seed Runtime Architecture: Reference Architecture for Extraction, Reconstruction, Validation, and Persistence"
series: "Generative Seed Reconstruction Theory"
document_id: "GSRT-TW01"
author: "Neo.K"
organization: "EveMissLab"
version: "0.1.0"
status: "Technical Whitepaper / Reference Runtime Architecture"
date: "2026-08-30"
language: "zh-TW"
canonical_source: "UTF-8 Markdown"
upstream:
  - GSRT-00
  - GSRT-01
  - GSRT-02
  - GSRT-03
  - GSRT-04
  - GSRT-05
  - GSRT-06
  - GSRT-07
  - GSRT-08
---

# Generative Seed Runtime Architecture

## 生成種子抽取、重建、驗證與持久化參考架構

### Generative Seed Runtime Architecture: Reference Architecture for Extraction, Reconstruction, Validation, and Persistence

**文件：** GSRT-TW01  
**版本：** v0.1.0  
**作者：** Neo.K  
**機構：** EveMissLab  
**日期：** 2026-08-30  
**性質：** Technical Whitepaper / Reference Runtime Architecture

---

# 0. 執行摘要

Generative Seed Reconstruction Theory（GSRT）已將研究問題從單次生成擴展為：

$$
X
\xrightarrow{E}
S_X
\xrightarrow{G_\gamma}
\widehat X,
$$

並進一步研究：

- seed 最小性；
- decoder-side shared priors；
- factorization；
- cross-modal meta-seeds；
- Seed Library；
- seed-space navigation；
- persistent interoperability。

但理論成立與否，最終必須交給 runtime 實驗。

本白皮書定義第一個可實作的 **Generative Seed Runtime Architecture（GSRA）**。它的工作不是證明 GSRT，而是提供一套能讓 GSRT 被反覆測量、被否證、被版本化的工程基底。

核心 runtime loop：

```text
Artifact
   |
   v
Artifact Ingest
   |
   v
Seed Extractor
   |
   v
Candidate Seed
   |
   +--> Dependency Audit
   |
   +--> Structural / Contract Validation
   |
   v
Blind Reconstructor
   |
   v
Reconstructed Artifact
   |
   v
Evaluator
   |
   v
Validation Certificate
   |
   +--> Reject / Retain Candidate
   |
   +--> Promote as Validated Seed
   |
   v
Seed Store / Factor Store / Meta-Seed Store
```

reuse path：

```text
Generation Request
   |
   v
Retriever
   |
   v
Recall Portfolio
   |
   v
Compatibility Check
   |
   v
Composer / Mutator
   |
   v
Generator Adapter
   |
   v
Generator
   |
   v
Artifact
   |
   v
Evaluator
   |
   v
Lineage + Certificate + Memory Update
```

本白皮書固定五條工程原則：

$$
\boxed{
\text{Scientific Evidence}
\neq
\text{Protocol Conformance}.
}
$$

$$
\boxed{
\text{Candidate}
\neq
\text{Validated}
\neq
\text{Canonical}.
}
$$

$$
\boxed{
\text{Artifact Authority}
\neq
\text{Seed Reconstruction State}.
}
$$

$$
\boxed{
\text{Deterministic Control Plane}
\neq
\text{Probabilistic Generation Plane}.
}
$$

$$
\boxed{
\text{ISQL Adapter}
\text{ is optional in early MVP}.
}
$$

第一版 MVP 的優先順序是：

```text
v0.1 Text Blind Reconstruction
v0.2 Seed Budget / Compression Curve
v0.3 Cross-Decoder Reconstruction
v0.4 Image Seed Reconstruction
v0.5 Factorization / Ablation
v0.6 Seed Library
v0.7 Composition / Mutation
v0.8 Seed-Space Navigation
v0.9 Canonical / ISQL Adapter
v1.0 Validated Generative Seed Runtime
```

本架構故意把 canonical protocol 延後至 v0.9。理由是：

> GSRT 首先要驗證「生成種子現象」是否存在，再驗證哪種 representation 最適合持久互通。

---

# 1. 文件目標

本白皮書回答：

1. artifact 如何進入 runtime？
2. seed candidate 如何被抽取？
3. 如何防止 hidden side information？
4. blind reconstruction 如何執行？
5. evaluator 如何避免只看表面相似？
6. seed 何時可從 Candidate 升為 Validated？
7. factor / meta-seed 如何存放？
8. generator adapter 如何隔離 model-specific condition？
9. Seed Library 如何與 source archive 分離？
10. version drift 如何處理？
11. failure 如何被保存？
12. MVP 如何逐步驗收？

---

# 2. 非目標

TW01 v0.1 不追求：

1. 一開始支援所有 modality；
2. 一開始建立 universal seed grammar；
3. 一開始把 ISQL 設為唯一 canonical representation；
4. 一開始建立 distributed database；
5. 一開始建立完整 SaaS；
6. 一開始進行 model training；
7. 一開始取代原 artifact archive；
8. 一開始宣稱跨 provider interoperability；
9. 一開始自動刪除可重建 source；
10. 一開始把所有 evaluator 交給 LLM-as-judge。

---

# 3. 規範詞

本文使用：

- **MUST**：MVP 若缺少則 contract 不成立；
- **MUST NOT**：禁止；
- **SHOULD**：高度建議；
- **MAY**：可選。

---

# 4. 核心資料流

完整流程：

$$
\boxed{
X
\rightarrow
Ingest
\rightarrow
E
\rightarrow
S_c
\rightarrow
Audit
\rightarrow
Reconstruct
\rightarrow
\widehat X
\rightarrow
Evaluate
\rightarrow
Certify
\rightarrow
Persist.
}
$$

其中：

- $X$：source artifact；
- $S_c$：candidate seed；
- $\widehat X$：blind reconstruction。

---

# 5. Source Authority Plane

Source Artifact MUST：

- content-addressed；
- immutable or versioned；
- preserve exact bytes when available；
- preserve provenance；
- never be silently replaced by reconstruction。

因此：

$$
\boxed{
SourceStore
\neq
SeedStore.
}
$$

---

# 6. Candidate Plane

Extractor 產生：

$$
S_c.
$$

Candidate MAY：

- freeform；
- structured；
- JSON；
- symbolic shorthand；
- learned latent reference；
- factor graph；
- multimodal state。

Candidate MUST NOT：

- 自動進 canonical registry；
- 自動取代 source；
- 自動被視為 validated。

---

# 7. Validation Plane

Candidate 只有經：

$$
BlindReconstruction
+
Evaluation
+
DependencyAudit
$$

才能升格。

---

# 8. Persistence Plane

Validated objects 才進：

- SeedStore；
- FactorStore；
- MetaSeedStore；
- CertificateStore；
- LineageGraph。

---

# 9. Optional Canonical Plane

Canonicalization 是 optional layer：

```text
Validated Seed
   |
   v
Canonicalization Adapter
   |
   v
Canonical Seed Object
```

MVP v0.1--v0.8 MAY 不啟用。

---

# 10. Deterministic / Probabilistic Split

## 10.1 Deterministic Control Plane

SHOULD 包含：

- IDs；
- hashes；
- manifests；
- experiment config；
- seed budget；
- dependency audit；
- version；
- lineage；
- certificate schema；
- pass/fail rules。

## 10.2 Probabilistic Generation Plane

包含：

- AI extraction；
- AI reconstruction；
- stochastic image generation；
- model reasoning；
- model-specific adaptation。

---

# 11. Deterministic Plane 不能被 AI 猜測覆蓋

例如：

> generator version unknown

MUST 記：

```text
UNKNOWN
```

不能由模型猜一個版本。

---

# 12. Runtime Component Map

TW01 定義 20 個主要模組：

```text
01 ArtifactStore
02 ArtifactIngestor
03 SeedExtractor
04 CandidateNormalizer
05 DependencyAuditor
06 ReconstructionRunner
07 EvaluatorHub
08 CertificateManager
09 SeedStore
10 FactorStore
11 MetaSeedStore
12 Registry
13 IndexHub
14 Retriever
15 CompatibilityEngine
16 ComposerMutator
17 GeneratorAdapter
18 LineageLedger
19 LifecycleController
20 MigrationRevalidationEngine
```

---

# 13. ArtifactStore

職責：

- exact bytes；
- content hash；
- metadata；
- provenance；
- modality；
- access policy。

Minimum key：

$$
artifact\_id
=
Hash(bytes).
$$

---

# 14. Artifact Ingestor

輸入：

- text；
- image；
- audio；
- code；
- later modalities。

輸出：

```yaml
artifact_record:
  artifact_id:
  modality:
  source_hash:
  source_bytes:
  source_metadata:
  imported_at:
  provenance:
```

---

# 15. SeedExtractor

介面：

$$
\boxed{
E:
ArtifactRecord
\times
ExtractionContract
\rightarrow
SeedCandidate.
}
$$

---

# 16. ExtractionContract

至少：

```yaml
extraction_contract:
  objective:
  seed_family:
  max_budget:
  budget_unit:
  allowed_side_information:
  forbidden_side_information:
  reconstruction_target:
  style_policy:
```

---

# 17. Seed Families

MVP SHOULD 支援：

```text
summary
keyword
freeform
structured
experimental_isql_like
```

目的是 matched-budget baseline。

---

# 18. CandidateNormalizer

Normalizer 不負責改 semantic meaning。

職責：

- Unicode normalization policy；
- deterministic metadata ordering；
- budget measurement；
- payload hashing；
- dependency normalization；
- seed-family tagging。

---

# 19. Normalization 不等於 Canonicalization

$$
\boxed{
Normalize(S)
\neq
Canonicalize(S).
}
$$

---

# 20. DependencyAuditor

GSRT-02 的 No Hidden Artifact Contract 在 runtime 中由此模組執行。

---

# 21. Dependency Classes

```text
SHARED_BASELINE
PUBLIC_REGISTRY
MODEL_BINDING
EXTERNAL_ASSET
PRIVATE_PER_ITEM
HIDDEN_CACHE
UNKNOWN
```

---

# 22. Private Dependency MUST 計成本

若：

```text
seed = "artifact-42"
```

實際 lookup 完整 artifact，則：

$$
C_{\mathrm{private}}
$$

必須納入。

---

# 23. Adjusted Cost

最低版本：

$$
\boxed{
C_{\mathrm{adj}}
=
C_{\mathrm{wire}}
+
C_{\mathrm{private}}.
}
$$

工程版：

$$
\mathbf C
=
(
C_{\mathrm{wire}},
C_{\mathrm{private}},
C_{\mathrm{decode}},
C_{\mathrm{retrieve}},
C_{\mathrm{version}},
C_{\mathrm{runtime}}
).
$$

---

# 24. ReconstructionRunner

介面：

$$
\boxed{
R:
SeedCandidate
\times
ReconstructionContract
\times
GeneratorBinding
\rightarrow
ReconstructionRun.
}
$$

---

# 25. Blind Reconstruction

Reconstructor MUST NOT 看：

- original artifact；
- original prompt；
- extractor rationale；
- previous reconstruction；
- hidden answer key。

---

# 26. Seed-Only Context

允許：

- seed；
- reconstruction instruction；
- shared baseline schema；
- declared public registry。

---

# 27. ReconstructionRun

```yaml
reconstruction_run:
  run_id:
  seed_id:
  generator:
  generator_version:
  adapter_version:
  stochastic_params:
  output_artifact_id:
  started_at:
  ended_at:
```

---

# 28. Repeated Reconstruction

對 stochastic generator，MUST 支援：

$$
\widehat X_1,\ldots,\widehat X_n.
$$

---

# 29. Estimated Success Probability

$$
\boxed{
\widehat p
=
\frac{1}{n}
\sum_{i=1}^{n}
\mathbf 1[
D(X,\widehat X_i)\le\varepsilon
].
}
$$

---

# 30. EvaluatorHub

EvaluatorHub MUST 支援 multiple evaluators。

---

# 31. Evaluator Types

```text
deterministic structural evaluator
rule evaluator
test runner
embedding evaluator
vision evaluator
LLM judge
human adjudication
```

---

# 32. LLM Judge 不得是唯一高風險裁判

特別是：

- negation；
- exact source；
- code behavior；
- identity hard gate。

---

# 33. Text Fidelity Vector

$$
\boxed{
\mathbf F_T
=
(
F_C,
F_R,
F_N,
F_Q,
F_E,
F_O,
F_S,
F_{\mathrm{func}}
).
}
$$

---

# 34. Image Fidelity Vector

$$
\boxed{
\mathbf F_I
=
(
F_{\mathrm{object}},
F_{\mathrm{id}},
F_{\mathrm{layout}},
F_{\mathrm{spatial}},
F_{\mathrm{camera}},
F_{\mathrm{light}},
F_{\mathrm{palette}},
F_{\mathrm{style}},
F_{\mathrm{percept}}
).
}
$$

---

# 35. Hard Gates

例如：

$$
F_N<\tau_N
$$

可直接 fail。

---

# 36. Evaluator Version

每個 score MUST 綁：

```text
evaluator_id
evaluator_version
metric_version
threshold_version
```

---

# 37. CertificateManager

Validation certificate：

```yaml
certificate:
  certificate_id:
  subject_seed:
  artifact:
  reconstruction_contract:
  generator_scope:
  evaluator_scope:
  repeated_runs:
  metrics:
  pass:
  issued_at:
  expires_on_change:
```

---

# 38. Certificate 不是 Seed Identity

$$
\boxed{
CertificateIdentity
\neq
SeedIdentity.
}
$$

---

# 39. SeedStore

Validated seed SHOULD 使用 immutable versioned record。

---

# 40. SeedStore Minimum Record

```yaml
seed:
  seed_id:
  seed_version:
  seed_family:
  modality:
  payload:
  payload_hash:
  status:
  reconstruction_contract:
  dependencies:
  provenance:
  certificate_refs:
  lineage_refs:
```

---

# 41. Seed Status

```text
CANDIDATE
VALIDATED
REUSABLE
PORTABLE
STALE
INVALID
SUPERSEDED
ARCHIVED
```

---

# 42. Candidate 不進正式 reuse index

IndexHub MAY 搜 candidate，但 Retriever 預設 SHOULD 排除未驗證 candidate。

---

# 43. FactorStore

GSRT-04 factors：

```yaml
factor:
  factor_id:
  type:
  version:
  payload:
  target_coordinates:
  protected_coordinates:
  dependencies:
  incompatibilities:
  generator_scope:
  evidence:
```

---

# 44. Factor 必須有 Intervention Evidence

有欄位名：

```text
style
```

不夠。

---

# 45. Factor Quality

SHOULD 保存：

$$
\Lambda_i,
\quad
L_i^{\mathrm{pres}},
\quad
C_i^{\mathrm{effect}},
\quad
P_i^{\mathrm{port}}.
$$

---

# 46. MetaSeedStore

GSRT-05 meta-seed：

```yaml
meta_seed:
  meta_seed_id:
  identity:
  relations:
  temporal_structure:
  spatial_structure:
  dynamic_structure:
  constraints:
  projection_refs:
  private_residue_refs:
```

---

# 47. Registry

Registry MUST 管理 stable semantic / field / factor identities。

---

# 48. Registry Entity

```yaml
registry_entry:
  registry_id:
  namespace:
  stable_id:
  label:
  definition:
  type:
  version:
  status:
  replaced_by:
```

---

# 49. Embedding 不得取代 Registry Identity

$$
\boxed{
NearestVector
\neq
SameIdentity.
}
$$

---

# 50. IndexHub

MVP index：

```text
hash index
metadata index
vector index
factor index
identity index
lineage index
certificate freshness index
```

---

# 51. Vector Index 是 Proposal Layer

其輸出：

$$
CandidateSet.
$$

最終 selection MUST 再經：

- identity；
- compatibility；
- freshness；
- certificate；
- cost。

---

# 52. Retriever

介面：

$$
\boxed{
Retrieve:
GenerationQuery
\times
SeedLibrary
\rightarrow
RecallPortfolio.
}
$$

---

# 53. RecallPortfolio

```yaml
recall_portfolio:
  base_seed:
  factors:
  meta_seed:
  compatibility_contract:
  certificate_refs:
  rejected_candidates:
```

---

# 54. Retrieval Scoring Vector

$$
\mathbf V_{\mathrm{ret}}
=
(
R_{\mathrm{semantic}},
R_{\mathrm{relational}},
R_{\mathrm{identity}},
R_{\mathrm{factor}},
R_{\mathrm{compat}},
R_{\mathrm{fresh}},
R_{\mathrm{cert}},
R_{\mathrm{cost}}
).
$$

---

# 55. CompatibilityEngine

輸入：

- selected seeds；
- factors；
- target generator；
- goal contract。

輸出：

```text
PASS
SOFT_CONFLICT
REPAIR_REQUIRED
FAIL
UNKNOWN
```

---

# 56. Hard Conflict MUST Fail Closed

例如：

```text
identity must preserve A
identity factor requests B
```

MUST FAIL 或要求 explicit override。

---

# 57. ComposerMutator

支持 operation：

```text
replace
merge
interpolate
constrain
suppress
inherit
branch
override
repair
```

---

# 58. Composition 是 Partial

$$
\oplus_{\mathcal K}
:
\mathcal S
\times
\mathcal S
\rightharpoonup
\mathcal S.
$$

---

# 59. GeneratorAdapter

核心介面：

$$
\boxed{
A_\gamma:
SeedState
\rightarrow
NativeCondition_\gamma.
}
$$

---

# 60. Adapter Output 可以是

- prompt；
- JSON；
- latent；
- image references；
- workflow；
- tool configuration；
- model control graph。

---

# 61. NativeCondition 不得反向成 Seed Identity

$$
\boxed{
NativeCondition_\gamma
\neq
SeedState.
}
$$

---

# 62. Generator Adapter Contract

```yaml
adapter:
  adapter_id:
  version:
  generator_family:
  supported_seed_families:
  required_dependencies:
  projection_loss:
  unsupported_features:
```

---

# 63. LineageLedger

每次：

- extract；
- compress；
- factorize；
- compose；
- mutate；
- migrate；
- validate；

都產生 edge。

---

# 64. Lineage Edge

```yaml
lineage_edge:
  source:
  target:
  operation:
  operator_version:
  evidence:
  timestamp:
```

---

# 65. Immutable Parent Preference

Branch SHOULD 不修改 parent。

---

# 66. SearchWorkspace 與 Canonical SeedStore 分離

大量 failed candidates MAY 留在 search workspace。

只有：

- elite；
- reusable；
- high-value failure exemplar；

才升格持久記錄。

---

# 67. LifecycleController

管理：

```text
HOT
WARM
COLD
ARCHIVE
DORMANT
STALE
INVALID
```

---

# 68. ActiveContext / Resident / Addressable

$$
\boxed{
ActiveContext
\neq
ResidentMemory
\neq
AddressableMemory.
}
$$

---

# 69. MigrationRevalidationEngine

觸發：

- model update；
- adapter update；
- evaluator update；
- registry update；
- profile update。

---

# 70. Stale Propagation

若 generator：

$$
\gamma_v
\rightarrow
\gamma_{v+1},
$$

對綁定 $\gamma_v$ 的 certificates：

$$
VALID
\rightarrow
STALE.
$$

---

# 71. Revalidation 不改 Seed Identity

除非 seed payload / canonical state 真正變更。

---

# 72. Runtime Boundary Diagram

```text
+----------------------------------------------------+
| Source Authority                                   |
| ArtifactStore                                      |
+--------------------------+-------------------------+
                           |
                           v
+----------------------------------------------------+
| Experimental Plane                                |
| Extractor -> Candidate -> Dependency Audit         |
|          -> Blind Reconstruction -> Evaluation     |
+--------------------------+-------------------------+
                           |
                           v
+----------------------------------------------------+
| Validated Generative Memory                       |
| SeedStore / FactorStore / MetaSeedStore           |
| CertificateStore / LineageLedger                  |
+--------------------------+-------------------------+
                           |
                           v
+----------------------------------------------------+
| Reuse Plane                                        |
| Retriever -> Compatibility -> Composer / Mutator   |
| -> GeneratorAdapter -> Generator -> Evaluator      |
+--------------------------+-------------------------+
                           |
                           v
+----------------------------------------------------+
| Optional Canonical Interop Plane                   |
| Canonicalizer / Registry / ISQL Adapter            |
+----------------------------------------------------+
```

---

# 73. Core State Machine

```text
INGESTED
  -> CANDIDATE
  -> VALIDATING
  -> VALIDATED
  -> REUSABLE
  -> PORTABLE

VALIDATED / REUSABLE
  -> STALE
  -> REVALIDATING
  -> VALIDATED

any non-source derived object
  -> INVALID

VALIDATED
  -> SUPERSEDED
  -> ARCHIVED
```

---

# 74. Validation Failure 不刪 Candidate

保留：

- failure reason；
- evaluator；
- generator；
- version。

---

# 75. Failure Taxonomy

最低：

```text
F-SEED-01 hidden dependency
F-SEED-02 budget violation
F-SEED-03 reconstruction failure
F-SEED-04 relation loss
F-SEED-05 negation flip
F-SEED-06 qualifier loss
F-SEED-07 identity drift
F-SEED-08 style-only success but structure fail
F-SEED-09 evaluator disagreement
F-SEED-10 leakage suspected
F-SEED-11 stale generator binding
F-SEED-12 incompatible factors
F-SEED-13 adapter unsupported
F-SEED-14 registry ambiguity
F-SEED-15 canonicalization mismatch
```

---

# 76. Leakage Controls

MVP MUST 包含：

- random seed；
- shuffled relations；
- contradictory seed；
- wrong identity；
- unrelated seed。

---

# 77. Contradictory Seed Control

如果 decoder 仍重建原答案：

可能：

- memory contamination；
- benchmark leakage；
- evaluator bias。

---

# 78. Experiment Manifest

每次 run MUST 有 immutable manifest。

---

# 79. Manifest Minimum Fields

```yaml
experiment:
  experiment_id:
  protocol_version:
  artifact_id:
  modality:

  extractor:
    model:
    version:
    seed_family:

  seed_budget:
    value:
    unit:

  reconstructor:
    model:
    version:

  evaluator:
    evaluator_ids:

  repetition:
    count:

  blindness:
    source_visible_to_decoder: false

  controls:
```

---

# 80. Budget Ladder

Text MVP：

$$
\rho
\in
\{
0.50,
0.25,
0.125,
0.0625,
0.03125
\}.
$$

短文本 MAY 改 absolute token budgets。

---

# 81. Matched-Budget Rule

Summary / Freeform / Structured 必須同 budget 比較。

---

# 82. Scientific Evidence Table

每個 artifact：

```text
artifact
seed family
budget
success probability
fidelity vector
dependency cost
cross-decoder result
```

---

# 83. Protocol Evidence Table

若啟用 canonical adapter：

```text
canonical roundtrip
invalid vectors
registry mismatch
migration
independent decoder
```

Scientific table 與 Protocol table MUST 分開。

---

# 84. MVP Storage Architecture

第一版：

$$
\boxed{
SQLite
+
ContentAddressedFiles
+
VectorIndex
+
GraphTables.
}
$$

---

# 85. SQLite Core Tables

```text
artifacts
seed_candidates
seeds
factors
meta_seeds
dependencies
reconstruction_runs
evaluations
certificates
lineage_edges
registry_entries
adapters
lifecycle_events
```

---

# 86. Content-Addressed Files

保存：

- large artifacts；
- reconstructed outputs；
- image assets；
- raw experiment bundles。

---

# 87. VectorIndex

可用：

- SQLite extension；
- FAISS；
- Qdrant；
- other。

Vendor MUST NOT 成為 logical contract。

---

# 88. GraphTables

先用 edge table 即可。

第一版不需要 Neo4j。

---

# 89. Sparse Field Evolution

若 factor types 快速增加，可導入 SEDB-like：

$$
\boxed{
\text{field registry}
+
\text{sparse values}
+
\text{field lifecycle}.
}
$$

---

# 90. Repository Layout

推薦：

```text
gsrt-runtime/
  README.md
  pyproject.toml

  src/gsrt/
    artifacts/
    extraction/
    seeds/
    dependencies/
    reconstruction/
    evaluation/
    certificates/
    factors/
    metaseeds/
    registry/
    index/
    retrieval/
    compatibility/
    composition/
    adapters/
    lineage/
    lifecycle/
    migration/
    canonical/

  schemas/
  profiles/
  corpus/
  manifests/
  runs/
  fixtures/
    positive/
    negative/
    leakage/
  tests/
    unit/
    integration/
    conformance/
    experiments/
  docs/
```

---

# 91. Python First

Reference MVP MAY 使用 Python。

理由：

- model SDK；
- experiment tooling；
- ML metrics；
- image pipeline；
- fast iteration。

---

# 92. Deterministic Core Later 可獨立實作

如果 canonical protocol 進 v0.9：

SHOULD 建第二語言 decoder，例如 Rust。

---

# 93. CLI

MVP CLI 建議：

```text
gsrt artifact ingest
gsrt seed extract
gsrt seed inspect
gsrt reconstruct
gsrt evaluate
gsrt validate
gsrt seed promote
gsrt seed list
gsrt factor extract
gsrt factor test
gsrt retrieve
gsrt compose
gsrt generate
gsrt lineage show
gsrt revalidate
```

---

# 94. `artifact ingest`

輸出 artifact ID。

---

# 95. `seed extract`

不得自動 promote。

---

# 96. `reconstruct`

預設 seed-only mode。

---

# 97. `validate`

產 certificate。

---

# 98. `promote`

需要 passing certificate。

---

# 99. API Boundary

runtime MAY 提供：

```text
POST /artifacts
POST /seed-candidates
POST /reconstructions
POST /evaluations
POST /promotions
POST /retrieval
POST /compositions
GET  /lineage/{id}
```

但 REST 不是 canonical requirement。

---

# 100. Profile Interface

```python
class SeedProfile:
    profile_id: str
    version: str

    def validate_candidate(self, candidate): ...
    def measure_cost(self, candidate): ...
    def build_reconstruction_contract(self, candidate): ...
    def project_for_generator(self, seed, generator): ...
```

---

# 101. GeneratorAdapter Interface

```python
class GeneratorAdapter:
    adapter_id: str
    version: str

    def supports(self, seed, generator) -> bool: ...
    def project(self, seed, generator): ...
    def declare_dependencies(self): ...
```

---

# 102. Evaluator Interface

```python
class Evaluator:
    evaluator_id: str
    version: str

    def evaluate(self, source, reconstruction, contract): ...
```

---

# 103. Certificate Interface

```python
class CertificateIssuer:
    def issue(self, subject, contract, evidence): ...
    def is_stale(self, certificate, runtime_state): ...
```

---

# 104. Determinism Contract

以下 MUST deterministic：

- hashes；
- IDs derived from exact bytes；
- experiment manifests；
- certificate schema；
- budget accounting；
- lineage edges；
- pass/fail rules given scores。

---

# 105. Probabilistic Components

MAY stochastic：

- extraction；
- reconstruction；
- image generation；
- candidate proposal；
- LLM evaluation。

---

# 106. Seed Extraction Repetition

同 artifact 可抽：

$$
S_1,\ldots,S_k.
$$

runtime SHOULD 保存 multiple candidates。

---

# 107. Candidate Diversity

可研究：

- same extractor multiple runs；
- multiple extractors；
- multiple seed families。

---

# 108. Near-Minimal Region

Runtime SHOULD 不只保存一顆 winner。

可以保存：

$$
\mathcal S_\eta^\star.
$$

---

# 109. Seed Candidate Competition

同 budget 下比較：

- reconstruction；
- dependency cost；
- portability；
- editability。

---

# 110. Promotion Policy

MVP 可使用：

```text
VALIDATED_SINGLE_MODEL
VALIDATED_MULTI_RUN
VALIDATED_CROSS_DECODER
REUSABLE_FACTOR
PORTABLE
```

---

# 111. Text v0.1 Acceptance

至少：

1. 100 artifacts；
2. 4 seed families；
3. matched budgets；
4. blind decoding；
5. repeated runs；
6. relation-sensitive evaluator；
7. negative controls；
8. reproducible manifests。

---

# 112. Text v0.1 不需要 ISQL

這是 hard scope rule。

---

# 113. v0.2 Compression Curve

對每 artifact 建：

$$
R_X^\gamma(b;\varepsilon).
$$

---

# 114. v0.2 Output

```text
empirical minimum
candidate cliff
near-minimal seeds
failure budget
```

---

# 115. v0.3 Cross-Decoder

建立：

$$
A_{ij}
=
F(
X,
G_j(E_i(X))
).
$$

---

# 116. Cross-Decoder Metadata

記：

- same model；
- same family；
- same provider；
- independent family；
- architecture class。

---

# 117. v0.4 Image Seed

Source image MUST 為完成 artifact。

不要拿 original prompt 直接當 seed。

---

# 118. Image Seed Candidate

保存：

- identity；
- composition；
- camera；
- lighting；
- palette；
- style；
- constraints。

---

# 119. v0.5 Factorization

執行：

- deletion；
- replacement；
- donor-recipient swap；
- round-trip；
- protected leakage。

---

# 120. v0.6 Seed Library

啟用：

- Retriever；
- IndexHub；
- Lifecycle；
- Lineage。

---

# 121. v0.7 Composition / Mutation

加入：

- CompatibilityEngine；
- ComposerMutator；
- branch workspace。

---

# 122. v0.8 Navigation

完整 navigation runtime 在 TW02 細化。

---

# 123. v0.9 Canonical / ISQL Adapter

只有此時開始：

- canonical seed profile；
- conformance vectors；
- registry binding；
- second decoder。

---

# 124. v1.0 Acceptance

v1.0 不是「所有 GSRT 猜想被證明」。

它代表：

> reference runtime 已足以穩定執行已聲明 experimental contracts。

---

# 125. Observability

Runtime MUST 輸出：

- run ID；
- artifact ID；
- seed ID；
- generator；
- evaluator；
- budget；
- cost；
- fidelity；
- certificate；
- failure class。

---

# 126. Reproducibility Bundle

每個重要實驗 SHOULD 可 export：

```text
manifest
seed
dependency manifest
reconstruction outputs
evaluation report
certificate
checksums
```

---

# 127. Run Directory

```text
runs/<experiment_id>/
  manifest.yaml
  seed.txt
  dependencies.json
  outputs/
  evaluation.json
  certificate.json
  checksums.sha256
```

---

# 128. Source / Output Separation

原 artifact：

```text
artifacts/
```

decoder outputs：

```text
runs/.../outputs/
```

MUST 不混。

---

# 129. Leakage Audit

MUST 支援：

- decoder prompt inspection；
- context hash；
- source visibility flag；
- retrieval visibility flag；
- memory mode。

---

# 130. Same-Model Pilot Label

同模型 parallel session：

```text
evidence_level = PILOT_SAME_MODEL
```

不能標 cross-model independent。

---

# 131. Human Adjudication

對 evaluator disagreement：

SHOULD 有 sample-based human adjudication。

---

# 132. Evaluator Ensemble

可：

$$
Decision
=
Rule
+
Model
+
HumanSubset.
$$

---

# 133. Exact Artifacts

code / text exact source：

可用 deterministic hash。

---

# 134. Functional Artifacts

code：

- tests；
- type check；
- API contract。

---

# 135. Image Evaluation

SHOULD 盡量拆：

- identity；
- layout；
- relation；
- style。

---

# 136. Avoid One-Score Collapse

MUST 保存 metric vector，不只總分。

---

# 137. Security：Untrusted Artifact

Artifact ingest MUST 防：

- path traversal；
- decompression bomb；
- malformed file；
- oversized input。

---

# 138. Security：Untrusted Seed

Seed payload MUST 有：

- size bounds；
- nesting bounds；
- dependency bounds；
- tool-execution boundary。

---

# 139. Seed 不得直接取得工具 Authority

$$
\boxed{
SeedDescription
\neq
ExecutionPermission.
}
$$

---

# 140. Code Seed

若包含 code：

MUST sandbox or disable execution by default。

---

# 141. Prompt Injection

external artifact 若被模型讀取，可能包含 instruction injection。

Extractor SHOULD 有：

- content/instruction separation；
- untrusted-content marker。

---

# 142. Authority

Source owner / project policy 決定：

- export；
- deletion；
- publication；
- execution。

Seed validation 不決定權限。

---

# 143. Privacy

Private source MAY 禁止：

- external provider；
- external embeddings；
- cloud evaluation。

---

# 144. Rebuildability

Library metadata MUST 能辨識：

```text
DERIVED_REBUILDABLE
CANONICAL_PERSISTENT
SOURCE_AUTHORITY
CACHE
```

---

# 145. Index Rebuild

vector index：

$$
DERIVED\_REBUILDABLE.
$$

不是 authority。

---

# 146. Certificate Freshness

Certificate MUST 有：

```text
generator version
adapter version
evaluator version
registry version
```

---

# 147. Revalidation Trigger

任一 critical version change：

MAY mark stale。

---

# 148. Migration

Seed payload migration SHOULD 產 receipt。

---

# 149. Migration Receipt

```yaml
migration_receipt:
  source_seed:
  source_version:
  target_seed:
  target_version:
  preserved:
  approximated:
  lost:
  evaluator:
  result:
```

---

# 150. Canonical Adapter Boundary

若 v0.9 加入 ISQL：

architecture：

```text
Validated GSRT Logical Seed
          |
          v
ISQL Profile Adapter
          |
          v
Candidate Canonical Object
          |
          v
Conformance Validation
          |
          v
Canonical ISQL Object
```

---

# 151. ISQL 不進 Scientific Scoring

例如：

> ISQL encoding 比 freeform seed 長。

不直接否定 seed phenomenon。

---

# 152. Canonicalization Value

v0.9 SHOULD 測：

- portability gain；
- audit gain；
- migration gain；
- dedup gain；
- overhead。

---

# 153. Protocol Conformance 跟實驗分開

tests：

```text
tests/experiments/
tests/conformance/
```

MUST 分開。

---

# 154. Positive Conformance Fixtures

若有 canonical profile：

- minimal seed；
- multilingual；
- factor seed；
- registry ref；
- version；
- optional extension。

---

# 155. Invalid Fixtures

- bad version；
- wrong registry；
- duplicate critical field；
- invalid digest；
- exact/semantic mislabel；
- unknown critical extension。

---

# 156. Second Implementation

v0.9+ SHOULD 建獨立 decoder。

---

# 157. Metrics Dashboard

最小：

```text
reconstruction success
seed cost
dependency cost
cross-decoder fidelity
factor locality
portability
reuse benefit
navigation gain
certificate freshness
```

---

# 158. Seed Runtime Health

```text
candidate backlog
validation throughput
stale certificate count
invalid seed rate
revalidation backlog
retrieval failure rate
```

---

# 159. Failure Budget

runtime SHOULD 設：

- per artifact max extraction attempts；
- max reconstruction runs；
- max evaluation cost。

---

# 160. Stop Condition

同一 failure class 重複超過門檻：

STOP or escalate。

---

# 161. No Infinite Agent Loop

MVP MUST 有 hard iteration cap。

---

# 162. Experiment Queue

可排：

```text
artifact_id
seed_family
budget
extractor
reconstructor
repetitions
```

---

# 163. Parallelization

可平行：

- artifacts；
- seed families；
- reconstruction repeats。

---

# 164. Parallelism 不等於 Independence

metadata MUST 標 model lineage。

---

# 165. Data Split

若 seed schema 持續被調：

需要：

- development set；
- holdout set。

---

# 166. Benchmark Overfitting

如果 schema 只對 100 個 benchmark 成功：

不代表 general phenomenon。

---

# 167. Corpus Design

Text corpus SHOULD 包含：

- theory；
- causal；
- conditional；
- narrative；
- technical；
- instruction；
- negation；
- exception；
- style-sensitive。

---

# 168. Image Corpus

SHOULD 包含：

- portrait；
- object；
- multi-object scene；
- spatial relation；
- style；
- lighting；
- identity-sensitive。

---

# 169. Artifact Complexity Stratification

SHOULD 標：

```text
simple
medium
complex
```

避免平均值掩蓋。

---

# 170. Generator Diversity

MVP v0.3+ 才開始擴。

第一版可同模型 pilot。

---

# 171. Model Metadata 不猜測

unknown lineage：

```text
UNKNOWN
```

---

# 172. Science Claim Ledger

每個 claim：

```yaml
claim:
  id:
  statement:
  evidence_required:
  evidence_present:
  status:
```

---

# 173. Claim Status

```text
HYPOTHESIS
PILOT_OBSERVATION
SUPPORTED_IN_SCOPE
PARTIALLY_SUPPORTED
NOT_SUPPORTED
FALSIFIED_IN_SCOPE
```

---

# 174. Protocol Claim Ledger

分開：

```text
IMPLEMENTED
CONFORMANT
PARTIAL
BLOCKED
```

---

# 175. Release Gate

版本不能因「計畫寫完」就升級。

必須對應實際 acceptance gates。

---

# 176. v0.1 Release Gate

```text
R1 artifact ingestion
R2 candidate extraction
R3 matched-budget accounting
R4 blind reconstruction
R5 evaluator vector
R6 negative controls
R7 certificate issuance
R8 reproducible manifest
R9 full regression
```

---

# 177. v0.1 不包含

- factor store；
- meta-seed；
- navigation；
- ISQL。

---

# 178. v0.2 Release Gate

增加：

- budget ladder；
- empirical minimum；
- cliff candidate；
- near-minimal region。

---

# 179. v0.3 Release Gate

增加：

- off-diagonal cross-decoder matrix；
- clean-room metadata；
- holdout decoder。

---

# 180. v0.4 Release Gate

增加 image modality。

---

# 181. v0.5 Release Gate

增加 factor intervention / ablation。

---

# 182. v0.6 Release Gate

增加 Seed Library persist / retrieve / reuse。

---

# 183. v0.7 Release Gate

增加 legal composition / mutation / branch。

---

# 184. v0.8 Release Gate

增加 navigation gain experiment。

---

# 185. v0.9 Release Gate

增加 canonical profile / conformance。

---

# 186. v1.0 Release Gate

要求：

```text
text scientific pipeline stable
image pipeline stable
seed library stable
versioned experiment records
negative controls
revalidation
optional canonical adapter separated
documented failures
```

---

# 187. Build Sequence

真正工程順序：

```text
P0 schemas + IDs + artifact store
P1 text extractor/reconstructor/evaluator
P2 experiment harness + controls
P3 budget ladder
P4 cross-decoder
P5 image adapter
P6 factor runtime
P7 library
P8 composition/navigation
P9 canonical protocol adapter
```

---

# 188. 不要反過來

不建議：

```text
先做 universal binary protocol
再找 seed 是否有用
```

---

# 189. Runtime Constitution

TW01 v0.1 固定 12 條最小憲法：

### C1 — Source Is Authority

seed 不取代 source。

### C2 — Candidate Is Not Validated

AI 產生不等於通過。

### C3 — Blind Reconstruction

decoder 不看答案。

### C4 — Hidden Dependencies Are Charged

不能把 artifact 藏在外部。

### C5 — Fidelity Is Multidimensional

不只 embedding similarity。

### C6 — Exact, Semantic, Generative Are Distinct

不可混標。

### C7 — Version Everything Critical

model、adapter、evaluator、registry。

### C8 — Lineage Is Persistent

重要 mutation 可追。

### C9 — Index Is Rebuildable

vector index 不當 authority。

### C10 — Authority Is Separate

seed 不自帶 tool permission。

### C11 — Scientific Evidence Is Separate from Protocol Conformance

兩張表。

### C12 — ISQL Is an Adapter Until Proven Otherwise

MVP 前期不鎖死。

---

# 190. Reference End-to-End Text Flow

```text
1. ingest source text
2. create artifact hash
3. create extraction contract
4. extractor creates 4 seed-family candidates
5. normalize + measure budget
6. audit dependencies
7. blind reconstruct n times
8. evaluator computes fidelity vector
9. run negative controls
10. issue certificate
11. promote passing candidates
12. persist lineage
13. export experiment bundle
```

---

# 191. Reference End-to-End Reuse Flow

```text
1. user gives generation goal
2. query parser creates generation contract
3. Retriever proposes seed portfolio
4. CompatibilityEngine filters conflicts
5. Composer / Mutator creates candidate state
6. GeneratorAdapter projects to native condition
7. generator produces artifact
8. Evaluator scores output
9. pass -> save lineage / certificate
10. fail -> branch / repair / reject
```

---

# 192. Reference End-to-End Revalidation Flow

```text
1. generator version changes
2. bound certificates marked STALE
3. scheduler samples affected seeds
4. ReconstructionRunner reruns
5. Evaluator compares
6. passing cert refreshed
7. failing seed scope reduced or invalidated
8. lineage records revalidation event
```

---

# 193. Reference End-to-End Canonical Flow

v0.9+：

```text
Validated Seed
-> logical canonical candidate
-> registry resolution
-> canonical encoding
-> conformance validation
-> independent decoder test
-> canonical object
```

---

# 194. TW01 與 TW02 分工

TW01：

$$
\boxed{
\text{Seed Lifecycle Runtime}.
}
$$

TW02：

$$
\boxed{
\text{Seed Library Retrieval + Navigation Runtime}.
}
$$

TW02 將深入：

- archive topology；
- QD niches；
- retrieval planner；
- operator routing；
- navigation workspace；
- mutation graph；
- search policy；
- navigation gain benchmark。

---

# 195. TW01 最終架構

$$
\boxed{
\begin{aligned}
&\text{Artifact Authority}\\
&\rightarrow
\text{Candidate Extraction}\\
&\rightarrow
\text{Blind Reconstruction}\\
&\rightarrow
\text{Evaluation}\\
&\rightarrow
\text{Validated Seed}\\
&\rightarrow
\text{Persistent Generative Memory}\\
&\rightarrow
\text{Reuse / Mutation}\\
&\rightarrow
\text{Revalidation}\\
&\rightarrow
\text{Optional Canonical Interop}.
\end{aligned}
}
$$

---

# 196. 結論

GSRT 的理論核心不是「把 prompt 存起來」。

真正要實驗的是：

$$
\boxed{
\text{Can successful generation be converted into reusable generative state?}
}
$$

TW01 將這個問題落成 runtime。

它保留了三種不同權威：

1. **Artifact Authority**：原始完成內容；
2. **Experimental Seed State**：用於重建、比較、組合；
3. **Optional Canonical Protocol State**：用於長期跨實作互通。

並且把：

$$
\boxed{
\text{extract}
\rightarrow
\text{reconstruct}
\rightarrow
\text{evaluate}
\rightarrow
\text{persist}
}
$$

設為第一階段真正的工程閉環。

如果此閉環本身不成立，就沒有必要提前建立龐大的 Seed Library 或 universal protocol。

如果此閉環穩定成立，才依序增加：

- minimum seed search；
- cross-decoder；
- image；
- factorization；
- library；
- composition；
- navigation；
- canonical interoperability。

因此 GSRA 的核心設計哲學是：

$$
\boxed{
\text{Evidence before Canonicalization}
}
$$

以及：

$$
\boxed{
\text{Reconstruction before Reuse}
}
$$

再加上：

$$
\boxed{
\text{Reuse before Navigation}.
}
$$

這使整個 GSRT 系列從理論論證真正進入可以被實作與否證的工程階段。

---

# Appendix A. Runtime Object Graph

```text
Artifact
  |
  +-- extracted_from --> SeedCandidate
                           |
                           +-- validated_as --> Seed
                                                   |
                                                   +-- factorized_into --> Factor
                                                   |
                                                   +-- projected_from --> MetaSeed
                                                   |
                                                   +-- certified_by --> Certificate
                                                   |
                                                   +-- parent/child --> Seed
```

---

# Appendix B. Minimal Experiment Schema

```yaml
gsrt_experiment:
  id:
  version:

  artifact:
    id:
    modality:
    source_hash:

  extraction:
    model:
    version:
    seed_family:
    budget:
    budget_unit:

  seed:
    candidate_id:
    payload_hash:
    dependency_manifest:

  reconstruction:
    decoder:
    version:
    adapter:
    repeated_runs:

  evaluation:
    evaluator_versions:
    fidelity_vector:
    hard_gates:
    controls:
    pass:

  promotion:
    status:
    certificate:
```

---

# Appendix C. Minimal Seed Schema

```yaml
seed:
  id:
  version:
  family:
  modality:
  status:
  payload:
  payload_hash:

  reconstruction_contract:
    recovery_class:
    epsilon:
    delta:

  dependencies:
  generator_bindings:
  factor_refs:
  meta_seed_ref:
  private_residue_refs:
  provenance:
  lineage:
  certificates:
```

---

# Appendix D. Minimal Failure Record

```yaml
failure:
  failure_id:
  class:
  subject:
  experiment:
  generator:
  evaluator:
  message:
  evidence:
  retryable:
  reopen_on:
```

---

# Appendix E. MVP Acceptance Matrix

| Phase | Primary claim tested | Required output |
|---|---|---|
| v0.1 | Text seed reconstructibility | blind reconstruction report |
| v0.2 | Seed budget / minimum | budget-fidelity curve |
| v0.3 | Cross-decoder portability | off-diagonal matrix |
| v0.4 | Image reconstructibility | image fidelity report |
| v0.5 | Factorization | intervention / ablation matrix |
| v0.6 | Generative memory reuse | reuse benefit report |
| v0.7 | Composition / mutation | transfer + preservation report |
| v0.8 | Seed-space navigation | navigation gain report |
| v0.9 | Canonical protocol value | conformance + overhead report |
| v1.0 | Runtime stability | integrated validation pack |

---

# Appendix F. Implementation Handoff

下一個實作者應先完成：

```text
1. repository scaffold
2. SQLite schema
3. artifact content-addressed store
4. experiment manifest
5. text seed extractor interface
6. blind reconstructor interface
7. evaluator interface
8. negative controls
9. certificate issuer
10. v0.1 CLI
```

明確禁止第一輪就：

```text
build ISQL canonical encoder
build image runtime
build navigation planner
build distributed storage
```

除非 v0.1 text blind reconstruction 已通過。

---

# Appendix G. Canonical Claim Strength

TW01 目前允許：

$$
\boxed{
\text{GSRT can be implemented as a staged experimental runtime whose deterministic evidence plane is separated from probabilistic extraction/generation and from optional canonical protocol adapters.}
}
$$

TW01 不允許：

$$
\boxed{
\text{The runtime architecture itself proves that reconstructive generative seeds are universally useful.}
}
$$

---

**文件結束**
