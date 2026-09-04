---
title: "TCFT Benchmark & Temporal Audit Protocol v0.1"
title_zh: "TCFT 基準測試與跨時間認知審計協議 v0.1"
series: "Temporal Cognitive Frontier Theory (TCFT)"
version: "v0.1"
date: "2026-08-31"
author: "Neo.K"
affiliation: "EveMissLab / 一言諾科技有限公司"
document_type: "Technical Whitepaper / Benchmark & Audit Protocol"
language: "zh-Hant"
status: "Canonical Engineering Specification"
depends_on:
  - "TCFT-00 至 TCFT-09"
  - "CODT-01 至 CODT-10"
  - "Temporal Claim Observatory (TCO)"
  - "Anomalous Causality Observatory (ACO)"
---

# TCFT Benchmark & Temporal Audit Protocol v0.1

## TCFT 基準測試與跨時間認知審計協議 v0.1

**系列：** Temporal Cognitive Frontier Theory（TCFT）  
**文件類型：** 技術白皮書 / Benchmark / Temporal Audit / Reference MVP Specification  
**版本：** v0.1  
**日期：** 2026-08-31  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  

---

## 摘要

Temporal Cognitive Frontier Theory（TCFT）已在 TCFT-00 至 TCFT-09 建立「時代認知前沿」的理論結構：Future Base-Space、Counterfactual Horizon、Reflexive Reasoning、Reasoning Allocation Governance、Time-Normalized Novelty、Dynamic Cognitive Anomaly Frontier、Native Cognitive Advancement，以及 Anti-Crown / Author–Theory Separation 等治理原則。

然而，若沒有一套可重現的審計協議，這些概念仍可能停留在高階理論敘述，並受到以下問題污染：

- 後見之明；
- candidate leakage；
- weak baseline；
- AI training contamination；
- prior-art retrieval failure；
- version ambiguity；
- success-only selection；
- semantic overmatching；
- evaluator halo；
- single-LLM novelty oracle；
- static benchmark saturation；
- person-ranking / heroization。

本文提出 **TCFT Benchmark & Temporal Audit Protocol v0.1（TCFT-BTAP）**，作為 TCFT 第一版 canonical engineering specification。其目的不是建立「天才排行榜」，而是建立一套可以回答下列問題的可執行系統：

> 在時間 $t_0$ 的可得知識、工具、制度與同期強基準下，某個 subject / artifact 所留下的 cognition-facing structure，是否存在難以由合理 baseline 吸收的時間正規化殘差？該殘差發生在哪些維度？證據強度如何？在後續 baseline 更新後是否被吸收、維持或重新估值？

本文定義 reference runtime 的十二個主要模組：

$$
\boxed{
\begin{aligned}
M_1&:\ Source\ \&\ Provenance\ Registry\\
M_2&:\ Temporal\ Freeze\ Engine\\
M_3&:\ Claim/Trace\ Decomposer\\
M_4&:\ Prior\ Art\ Retrieval\ Layer\\
M_5&:\ Baseline\ Ensemble\ Generator\\
M_6&:\ Cognitive\ Structure\ Recovery\\
M_7&:\ Metric\ Plugin\ Runtime\\
M_8&:\ Failure/Selection\ Correction\\
M_9&:\ Evidence\ Confidence\ Engine\\
M_{10}&:\ Dynamic\ Frontier\ Engine\\
M_{11}&:\ Audit\ Ledger\ \&\ Revision\ Runtime\\
M_{12}&:\ Governance\ \&\ AntiCrown\ Layer.
\end{aligned}
}
$$

TCFT-BTAP 採用兩個互相獨立的輸出帳：

$$
\boxed{
\text{Capability Profile}
\neq
\text{Evidence Profile}.
}
$$

能力 profile 以：

$$
\boxed{
\vec\Phi_i(t)
=
(
BS,
CF,
RR,
RG,
TN,
PG,
RP,
NC
)
}
$$

為 v0.1 canonical dimensions；證據 profile 則至少保存：

$$
\boxed{
\vec E_i(t)
=
(
C_{time},
C_{version},
C_{prior},
C_{baseline},
C_{ind},
C_{structure},
C_{failure}
).
}
$$

TCFT-BTAP 不要求所有 metric 使用相同量綱，也不要求輸出單一 scalar score。其 canonical outputs 為：

$$
\boxed{
\mathcal{TCFT}_i(t)
=
[
\vec G_i(t),
\vec E_i(t),
FrontierStatus_i(t),
AuditLedger_i(t)
].
}
$$

其中：

$$
\vec G_i(t)
=
Norm(
\vec\Phi_i(t),
\vec B(t)
)
$$

表示相對 contemporaneous baseline 的多維 gap。

本文特別建立 **Candidate-Blind Baseline Gate**。任何 baseline agent 若已知 candidate 的關鍵答案、現代名稱、後續結果或核心結構，就不能被標記為 Frozen-Time candidate-blind baseline。其結果必須降級為：

$$
\boxed{
BaselineStatus
=
CONTAMINATED.
}
$$

同時建立 **Revision Sensitivity Gate**：當新 prior art、版本證據、失敗紀錄或更強 baseline 被加入，審計結果必須允許上升、下降或變成 Unresolved。若系統只能累積「更神」的證據而不能降低異常度，則驗收失敗。

本文定義四個 MVP benchmark tracks：

1. **B0 Synthetic Calibration Track**：使用可控 ground truth 檢驗 timestamp、leakage、prior-art、baseline 與 revision logic；
2. **B1 Historical Frozen-Time Track**：對已封存歷史 artifacts 執行 candidate-blind temporal reconstruction；
3. **B2 Contemporary Human / AI / Human-AI Track**：測量工具增益、系統級 novelty 與動態 baseline；
4. **B3 Reflexive / Counterfactual / Reasoning-Governance Track**：測 Hidden Reversal Witness、public/private prediction、cost-aware stopping 與 domain switching。

Reference MVP 的成功標準不是「找出真正未來人」或「證明某人最強」，而是：

$$
\boxed{
\text{Reproducibility}
+
\text{Leakage Resistance}
+
\text{Revision Sensitivity}
+
\text{Baseline Strength}
+
\text{Multi-Dimensional Discrimination}
+
\text{Governance Compliance}.
}
$$

本文最後提供 canonical JSON Schema、metric plugin contract、audit state machine、acceptance matrix、reference repository layout 與 Phase 0–4 實作路線。

**關鍵詞：** TCFT、Temporal Audit、Frozen-Time、prior art、baseline ensemble、benchmark、cognitive frontier、dynamic audit、provenance、anti-crown、MVP

---

# 1. 文件定位

## 1.1 本文件不是新理論篇

TCFT-00 至 TCFT-09 已完成理論層。

本白皮書回答：

$$
\boxed{
\text{How do we implement and test TCFT?}
}
$$

---

## 1.2 Canonical Dependency Stack

$$
\boxed{
CODT
\rightarrow
TCFT
\rightarrow
TCFT\text{-}BTAP
\rightarrow
ReferenceMVP
}
$$

其中：

- CODT：提供 cognition structure recovery ontology；
- TCFT：提供 temporal frontier theory；
- BTAP：提供可執行 audit protocol；
- MVP：提供 reference implementation。

---

# 2. Non-Goals

v0.1 明確不做：

1. 不證明某人來自未來；
2. 不證明某人不是人類；
3. 不建立全球「最聰明人物排行榜」；
4. 不以 citation count 代替 cognitive frontier；
5. 不把單一 LLM 當 novelty oracle；
6. 不把 semantic similarity 當 operational identity；
7. 不宣稱完整重建人類內在心智；
8. 不宣稱已找到最終 cognitive primitives；
9. 不將 TCFT score 轉成政治、人格或道德權威；
10. 不把 missing data 當作零。

---

# 3. Canonical Research Entity Model

## 3.1 Subject

$$
\boxed{
SubjectType
\in
\{
Human,
AI,
HumanAI,
Team,
Institution,
Artifact
\}.
}
$$

---

## 3.2 Artifact

Artifact 可以是：

- paper；
- book；
- patent；
- source code；
- notebook；
- diagram；
- prediction；
- interview；
- talk；
- archived post；
- decision record；
- experiment；
- model output。

---

## 3.3 Audit Unit

最小：

$$
\boxed{
u
=
(
Subject,
Artifact,
ClaimOrTrace,
Timestamp,
Version,
Context
).
}
$$

---

# 4. Subject–Artifact Dual Track

Subject track：

$$
\boxed{
\Phi_i(t)
}
$$

追蹤 active agent / system。

Artifact track：

$$
\boxed{
A_x(t)
}
$$

追蹤固定 artifact 在不同 baseline 下的 persistence。

必須維持：

$$
\boxed{
AgentPersistence
\neq
ArtifactPersistence.
}
$$

---

# 5. Temporal Layer Model

每個 audit 至少保留：

$$
\boxed{
Historical,
Current,
Persistent.
}
$$

---

## 5.1 Historical

$$
A^{hist}(t_0)
=
A(
x_{t_0}
\mid
B(t_0)
).
$$

---

## 5.2 Current

$$
A^{cur}(t_1)
=
A(
x_{t_1}
\mid
B(t_1)
).
$$

---

## 5.3 Persistent

$$
A^{persist}
=
P(
\{A(t)\}_{t_0:t_1}
).
$$

---

# 6. Reference Runtime Architecture

## M1 — Source & Provenance Registry

責任：

- source ingestion；
- immutable source hash；
- archive URI；
- author / subject；
- source type；
- first-seen time；
- disclosure time；
- revision lineage；
- license / access metadata。

不得負責：

- novelty score；
- frontier judgment。

---

## M2 — Temporal Freeze Engine

輸入：

$$
t_0.
$$

輸出：

$$
\boxed{
K_{\le t_0},
Tool_{\le t_0},
Institution_{\le t_0}.
}
$$

必須支援：

- publication date filters；
- archive timestamps；
- software / model release dates；
- data release dates；
- tool availability；
- temporal uncertainty。

---

## M3 — Claim / Trace Decomposer

把：

$$
X
$$

拆為：

$$
x_1,\ldots,x_n.
$$

trace type：

- claim；
- question；
- representation；
- procedure；
- prediction；
- action；
- failure；
- revision。

---

## M4 — Prior-Art Retrieval Layer

provider interface：

$$
\boxed{
retrieve(
query,
time\_boundary,
languages,
domains
)
\rightarrow
Candidates.
}
$$

至少支援：

- scholarly；
- patent；
- web archive；
- books；
- code；
- internal corpus。

---

## M5 — Baseline Ensemble Generator

建立：

$$
\boxed{
B_t^{ens}
=
\{
B^{general},
B^{expert},
B^{frontier},
B^{tool},
B^{AI},
B^{human+AI}
\}.
}
$$

並保存：

- model identity；
- model version；
- prompt；
- allowed tools；
- date boundary；
- candidate blindness；
- contamination risk。

---

## M6 — Cognitive Structure Recovery

子模組：

### M6.1 Problem-Space Recovery

輸出：

$$
\mathcal Q_i(t).
$$

### M6.2 Future Base-Space Recovery

輸出：

$$
\mathfrak B_i(t).
$$

### M6.3 Counterfactual Recovery

輸出：

$$
\mathcal C_i(t).
$$

### M6.4 Reflexive Structure Recovery

輸出：

$$
RR_i.
$$

### M6.5 Native Operator Recovery

$$
Trace
\rightarrow
OperatorCandidates.
$$

### M6.6 Program Topology Recovery

$$
Operators
+
History
\rightarrow
ProgramTopology.
$$

### M6.7 Domain-Seed Recovery

只輸出：

$$
\boxed{
Seed / Candidate
}
$$

不得在 v0.1 自動輸出：

$$
PromotedDomain.
$$

---

## M7 — Metric Plugin Runtime

Canonical dimensions：

$$
\boxed{
D
=
\{
BS,CF,RR,RG,TN,PG,RP,NC
\}.
}
$$

每一個 metric 必須：

- versioned；
- independently replaceable；
- have input contract；
- output raw score；
- output normalized score；
- output confidence；
- declare assumptions。

---

## M8 — Failure / Selection Correction

保存：

- failed predictions；
- abandoned ideas；
- unsuccessful alternatives；
- total output opportunity；
- correction status。

防止：

$$
\boxed{
\text{Success Selection Bias}.
}
$$

---

## M9 — Evidence Confidence Engine

輸出：

$$
\boxed{
\vec E
=
(
C_{time},
C_{version},
C_{prior},
C_{baseline},
C_{ind},
C_{structure},
C_{failure}
).
}
$$

---

## M10 — Dynamic Frontier Engine

輸入：

$$
\vec G_i(t).
$$

輸出：

- anomaly class；
- Pareto membership；
- optional robust multivariate distance；
- historical/current/persistent status。

---

## M11 — Audit Ledger & Revision Runtime

保存：

$$
\boxed{
AuditID
=
(
SubjectID,
ArtifactID,
CutoffTime,
BaselineVersion,
MetricVersion,
CorpusVersion
).
}
$$

必須 immutable append。

修訂不得覆蓋舊結果。

---

## M12 — Governance & Anti-Crown Layer

強制：

- no default global person leaderboard；
- evidence visible；
- failure visible；
- baseline visible；
- time visible；
- unresolved supported；
- no identity inference from cognitive score。

---

# 7. Audit State Machine

Canonical state：

$$
\boxed{
INGESTED
\rightarrow
TIME\_FROZEN
\rightarrow
DECOMPOSED
\rightarrow
PRIOR\_SEARCHED
\rightarrow
BASELINED
\rightarrow
STRUCTURED
\rightarrow
SCORED
\rightarrow
GRADED
\rightarrow
PLACED
\rightarrow
SEALED.
}
$$

---

## 7.1 Exceptional States

$$
\boxed{
BLOCKED\_PROVENANCE
}
$$

$$
\boxed{
BASELINE\_CONTAMINATED
}
$$

$$
\boxed{
INSUFFICIENT\_PRIOR\_ART
}
$$

$$
\boxed{
UNRESOLVED
}
$$

$$
\boxed{
REVISION\_REQUIRED
}
$$

---

# 8. Frozen-Time Contract

## 8.1 Hard Cutoff

若 audit time：

$$
t_0,
$$

則 baseline evidence：

$$
e
$$

必須：

$$
\boxed{
t(e)\le t_0.
}
$$

---

## 8.2 Temporal Unknown

若日期不明：

$$
DateStatus=UNKNOWN.
$$

不得自動納入 Frozen-Time corpus。

---

## 8.3 Date Interval

若只知道：

$$
t(e)\in[t_a,t_b],
$$

且：

$$
t_a\le t_0<t_b,
$$

標：

$$
\boxed{
TEMPORALLY\_AMBIGUOUS.
}
$$

---

# 9. Candidate-Blind Baseline Gate

這是 v0.1 的 blocking requirement。

baseline 必須在沒有 candidate 核心答案下生成。

---

## 9.1 Contamination Types

### C0 — Clean

沒有候選答案／後續結果／現代命名。

### C1 — Possible Training Exposure

模型可能在 pretraining 見過公開 artifact，但本輪 prompt / retrieval 未提供。

### C2 — Retrieval Exposure

本輪 retrieval 直接取到 candidate 或近似全文。

### C3 — Prompt Leakage

prompt 包含 candidate 的答案、名稱或結論。

### C4 — Outcome Leakage

baseline 知道 $t_0$ 之後結果。

---

## 9.2 Baseline Eligibility

只有：

$$
C0
$$

與經明確風險標記的：

$$
C1
$$

可進 primary baseline。

C2–C4：

$$
\boxed{
PRIMARY\_BASELINE\_ELIGIBLE=FALSE.
}
$$

---

# 10. Baseline Ensemble Protocol

至少建議三個異質 baseline：

1. lexical / retrieval baseline；
2. reasoning / generation baseline；
3. expert / human or independent model baseline。

---

## 10.1 Strong Baseline Principle

如果：

$$
B_{new}
$$

嚴格強於：

$$
B_{old},
$$

合理 anomaly residual 不應在沒有其他改動下系統性上升。

這形成：

$$
\boxed{
\text{Baseline Monotonicity Check}.
}
$$

不是數學絕對單調定理，但可作 regression warning。

---

# 11. Prior-Art Retrieval Protocol

## 11.1 Query Families

至少：

- lexical；
- semantic；
- structural；
- cross-domain；
- multilingual；
- citation graph；
- reverse terminology。

---

## 11.2 No-Match Semantics

$$
\boxed{
NoMatchFound
\neq
NoPriorArtExists.
}
$$

---

## 11.3 Retrieval Confidence

每個 audit 保存：

$$
\boxed{
C_{prior}
}
$$

與：

- searched providers；
- languages；
- date coverage；
- known blind areas。

---

# 12. Structural Match Classes

$$
\boxed{
S0:
NoRelevantMatchFound
}
$$

$$
\boxed{
S1:
LexicalOverlap
}
$$

$$
\boxed{
S2:
ConceptualOverlap
}
$$

$$
\boxed{
S3:
StructuralPartialMatch
}
$$

$$
\boxed{
S4:
OperationalNearMatch
}
$$

$$
\boxed{
S5:
SubstantiveOperationalPriorArt
}
$$

---

# 13. Capability Dimension Contracts

## 13.1 BS — Future Base-Space

至少測：

- candidate support coverage；
- unknown reserve；
- quality-adjusted diversity；
- support failures；
- representation-induced omissions。

---

## 13.2 CF — Counterfactual Horizon

至少測：

- generated-CF vs given-CF；
- hidden reversal witness；
- diversity；
- causal coherence；
- pruning quality；
- coverage under budget。

---

## 13.3 RR — Reflexive Reasoning

至少測：

- self-model；
- other-model；
- public/private prediction；
- performativity awareness；
- reflexive reversal witness；
- endogenous evidence labeling。

---

## 13.4 RG — Reasoning Governance

至少測：

- cost-aware stopping；
- switching；
- strategic coarsening；
- verification allocation；
- delegation；
- meta-reasoning overhead。

---

## 13.5 TN — Time-Normalized Novelty

至少測：

- prior-art residual；
- candidate-blind baseline gap；
- timestamp integrity；
- tool-adjusted novelty；
- hindsight control。

---

## 13.6 PG — Problem Generation

至少測：

- question novelty；
- generativity；
- future importance；
- problem-space expansion；
- baseline discoverability。

---

## 13.7 RP — Representation / Program Advancement

至少測：

- operational gain；
- topology novelty；
- cross-task reuse；
- failure coherence；
- program-level prior art。

---

## 13.8 NC — Native Cognitive Advancement

至少測：

- native representation；
- operator candidate；
- program candidate；
- domain-seed candidate；
- cross-context persistence；
- causal / functional evidence。

---

# 14. Metric Plugin Contract

每個 plugin：

```text
metric_id
metric_version
dimension
supported_subject_types
required_fields
optional_fields
raw_score
normalized_score
confidence
assumptions
warnings
evidence_refs
```

---

# 15. Metric Output Rule

禁止只輸出：

```text
score: 0.93
```

必須至少：

```text
raw_score
normalization_reference
confidence
warnings
evidence
```

---

# 16. Evidence Profile

Canonical：

$$
\boxed{
\vec E
=
(
C_t,
C_v,
C_p,
C_b,
C_i,
C_s,
C_f
).
}
$$

取值：

$$
[0,1]
$$

只作工程標準化，不表示概率真值。

---

# 17. Capability–Evidence Matrix

| Capability Residual | Evidence | Status |
|---|---|---|
| Low | High | Well-Supported Normal |
| High | High | Strong Frontier Candidate |
| High | Low | High-Potential / Unresolved |
| Low | Low | Unresolved / Low Information |

---

# 18. Anomaly Classes

v0.1：

```text
NORMAL
UNCOMMON
RARE
EXTREME
HISTORICAL_FRONTIER_CANDIDATE
PERSISTENT_FRONTIER_CANDIDATE
UNRESOLVED
```

禁止直接輸出：

```text
GENIUS
SUPERHUMAN
TIME_TRAVELER
SUPERIOR_PERSON
```

---

# 19. Dynamic Frontier Engine

## 19.1 Gap

$$
\boxed{
\vec G_i(t)
=
Norm(
\vec\Phi_i(t),
\vec B(t)
).
}
$$

---

## 19.2 Gap Dynamics

$$
\boxed{
\Delta\vec G_i
=
\Delta\vec\Phi_i
-
\Delta\vec B.
}
$$

---

## 19.3 Pareto Frontier

$$
\boxed{
\mathcal F_t
=
\{
i:
\nexists j
\text{ dominates }i
\}.
}
$$

---

## 19.4 Optional Multivariate Diagnostic

Mahalanobis or robust distance may be attached as：

$$
\boxed{
diagnostic\_distance.
}
$$

不得取代 profile。

---

# 20. Scalar Score Policy

默認：

$$
\boxed{
NO\ GLOBAL\ SCALAR.
}
$$

如果 task-specific 必須加權：

$$
Score
=
\sum_kw_kG_k,
$$

則必須保存：

```text
weight_vector
weight_owner
weight_purpose
weight_version
sensitivity_analysis
```

---

# 21. Revision Protocol

任何下列事件都應產生 RevisionEvent：

- new prior art；
- corrected timestamp；
- new historical version；
- newly found failures；
- baseline upgrade；
- metric version change；
- contamination discovery。

---

## 21.1 Append-Only

舊 audit 不刪。

新 audit：

$$
\boxed{
Audit^{v+1}
}
$$

指向：

$$
Audit^v.
$$

---

## 21.2 Revision Direction

結果可以：

$$
\uparrow,
\downarrow,
Unresolved.
$$

三者都合法。

---

# 22. Revision Sensitivity Gate

測試：

1. 先執行 audit；
2. 注入 substantive prior art；
3. 重跑；
4. 期望 TN / structural residual 下降或至少產生 explanation；
5. 注入更早 candidate version；
6. 期望 timestamp confidence / historical lead 可上升；
7. 注入大量 failures；
8. 期望 selection-adjusted profile 改變。

若系統對以上均不敏感：

$$
\boxed{
FAIL.
}
$$

---

# 23. Failure / Selection Correction

對 subject：

$$
N_{total}
$$

全部可審計輸出。

成功前沿輸出：

$$
N_{frontier}.
$$

保存：

$$
\boxed{
FHR
=
\frac{
N_{frontier}
}{
N_{audited}
}.
}
$$

只作 context，不作唯一 score。

---

# 24. Volume Policy

$$
\boxed{
Volume
\neq
Penalty
}
$$

也：

$$
\boxed{
Volume
\neq
Proof.
}
$$

---

# 25. AI Novelty Judge Policy

基於近期 novelty benchmarks，v0.1 禁止：

$$
\boxed{
SingleLLMJudge
=
FinalNoveltyDecision.
}
$$

---

## 25.1 Allowed AI Roles

- retrieval；
- query expansion；
- decomposition；
- structural parsing；
- candidate baseline generation；
- contradiction search；
- clustering；
- audit drafting。

---

## 25.2 Required Plurality

高風險 novelty judgment 至少需要：

- retrieval evidence；
- one independent model / evaluator；
- one rule-based / structural component or expert review。

---

# 26. Dynamic Benchmark Policy

TCFT benchmark 本身也會 drift。

因此每個 benchmark release：

```text
benchmark_version
release_date
task_set_hash
baseline_set
contamination_notes
metric_versions
```

---

# 27. Benchmark Saturation Policy

若某 task：

$$
MedianFrontierScore\rightarrow Ceiling,
$$

則：

```text
status = SATURATED
```

並：

- raise difficulty；
- add fresh cases；
- move upstream；
- archive old task。

---

# 28. Benchmark Track B0 — Synthetic Calibration

目的：

測 protocol correctness，而不是 cognitive prestige。

---

## 28.1 Synthetic Cases

建立可控：

- clean first version；
- later modified version；
- hidden prior art；
- contaminated baseline；
- known failure archive；
- unknown timestamp；
- duplicate semantic prior art；
- same-word/different-program；
- different-word/same-program。

---

## 28.2 B0 Acceptance

必須正確識別：

- leakage；
- version；
- substantive prior art；
- uncertainty；
- revision direction。

---

# 29. Benchmark Track B1 — Historical Frozen-Time

案例類型：

- scientist；
- inventor；
- philosopher；
- strategist；
- artist-engineer；
- early computing artifact。

---

## 29.1 B1 Rule

不先告訴 baseline：

> 這是某知名人物的經典作品。

優先 name-blind。

---

## 29.2 B1 Output

```text
historical_profile
current_artifact_profile
artifact_persistence
evidence_profile
prior_art_map
```

---

# 30. Benchmark Track B2 — Contemporary Human / AI / Human-AI

目的：

測：

- current tool baseline；
- AI augmentation；
- system-level novelty；
- attribution uncertainty；
- baseline jump。

---

## 30.1 B2 Conditions

至少：

1. Human only；
2. AI only；
3. Human + AI；
4. AI + search；
5. Human + AI + search。

---

## 30.2 B2 Caveat

不強迫：

$$
Output_{H+AI}
=
Output_H+Output_{AI}.
$$

允許 interaction term。

---

# 31. Benchmark Track B3 — Counterfactual / Reflexive / Governance

子任務：

### B3-CF

Hidden Reversal Witness。

### B3-RR

Private vs Public Prediction。

### B3-RG

Fixed depth vs cost-aware stopping。

### B3-SW

Domain switching / lock-in / thrashing。

---

# 32. B3 Objective Ground Truth

能自動驗證者優先：

- simulated environment；
- explicit causal graph；
- hidden reversal branch；
- fixed utility function；
- known deadline；
- known compute budget。

如此降低 LLM-judge dependency。

---

# 33. Reproducibility Protocol

同一：

$$
AuditID
$$

在固定：

- corpus；
- baseline；
- metric；
- seed；

下應產生：

$$
\boxed{
EquivalentAuditResult
}
$$

within tolerance。

---

# 34. Determinism Levels

```text
D0 = fully deterministic
D1 = deterministic retrieval + stochastic generation
D2 = stochastic ensemble
```

每筆 audit 必須標。

---

# 35. Reproducibility Target

對 D0：

完全一致。

對 D1/D2：

保存：

- seeds；
- samples；
- score interval；
- ensemble variance。

---

# 36. Security / Integrity Boundary

TCFT audit 可能處理：

- claims；
- public figures；
- private drafts；
- personal data。

Reference MVP 預設：

$$
\boxed{
Public / User-Authorized Data Only.
}
$$

---

# 37. Personal Identity Policy

不得從 cognition score 自動：

- diagnose；
- infer mental illness；
- infer protected attributes；
- infer metaphysical identity。

---

# 38. Anti-Crown Governance

## G1 — No Default Person Leaderboard

blocking。

## G2 — Evidence Visible

blocking。

## G3 — Failure Visible

blocking。

## G4 — Baseline Visible

blocking。

## G5 — Historical / Current Separate

blocking。

## G6 — Unresolved Allowed

blocking。

## G7 — No Identity Inference Shortcut

blocking。

---

# 39. UI Recommendations

首頁：

- Cases；
- Frontier Map；
- Audit Timeline；
- Benchmark Health。

不建議：

- #1 Genius；
- “Most Advanced Human”；
- hero cards without evidence。

---

# 40. Case Page

至少：

```text
subject metadata
artifact list
audit cutoff
prior art
baseline ensemble
dimension profiles
evidence profile
known failures
historical/current/persistent status
revision history
```

---

# 41. Frontier Map

優先：

- 2D / selectable projections；
- Pareto highlighting；
- confidence bands。

不預設 scalar rank。

---

# 42. Reference Repository Layout

```text
tcft-btap/
├─ README.md
├─ docs/
│  ├─ whitepaper/
│  ├─ protocol/
│  └─ governance/
├─ schemas/
│  ├─ audit.schema.json
│  ├─ evidence.schema.json
│  └─ metric.schema.json
├─ tcft/
│  ├─ provenance/
│  ├─ temporal/
│  ├─ decomposition/
│  ├─ prior_art/
│  ├─ baselines/
│  ├─ structure/
│  ├─ metrics/
│  ├─ frontier/
│  ├─ ledger/
│  └─ governance/
├─ benchmarks/
│  ├─ b0_synthetic/
│  ├─ b1_historical/
│  ├─ b2_contemporary/
│  └─ b3_reflexive/
├─ tests/
│  ├─ unit/
│  ├─ integration/
│  ├─ regression/
│  └─ acceptance/
└─ examples/
```

---

# 43. Plugin Interfaces

## 43.1 Prior-Art Provider

```python
class PriorArtProvider:
    def search(self, query, cutoff, languages, domains):
        ...
```

---

## 43.2 Baseline Provider

```python
class BaselineProvider:
    def generate(self, frozen_context, task, blindness_policy):
        ...
```

---

## 43.3 Metric Plugin

```python
class MetricPlugin:
    dimension = "TN"
    version = "0.1"

    def evaluate(self, audit_context):
        ...
```

---

## 43.4 Frontier Engine

```python
class FrontierEngine:
    def normalize(self, profiles, baseline):
        ...

    def pareto(self, profiles):
        ...

    def longitudinal(self, audit_series):
        ...
```

---

# 44. MVP Phase 0 — Protocol Kernel

產出：

- schemas；
- audit state machine；
- provenance hashing；
- temporal cutoff；
- contamination flags；
- append-only ledger。

成功條件：

$$
\boxed{
B0\ Protocol\ Tests=PASS.
}
$$

---

# 45. MVP Phase 1 — Prior Art + Baseline

產出：

- provider abstraction；
- date-bounded retrieval；
- baseline ensemble；
- blindness gate；
- contamination classifier。

---

# 46. MVP Phase 2 — Metrics

先只實作四維：

$$
\boxed{
TN,
PG,
CF,
RG.
}
$$

理由：

- 可測；
- 可 synthetic ground truth；
- 較少依賴深層 operator recovery。

---

# 47. MVP Phase 3 — Structural Recovery

加入：

$$
RP,
NC.
$$

CODT operator / program recovery。

---

# 48. MVP Phase 4 — Dynamic Frontier

加入：

$$
Historical,
Current,
Persistent,
Pareto,
Revision.
$$

---

# 49. v0.1 Reference MVP Scope

MVP 不必一次完成八維全部高成熟度。

最低：

```text
Protocol Kernel: complete
TN: functional
PG: functional
CF: functional
RG: functional
RP: experimental
NC: experimental
RR: benchmark-only initial
BS: benchmark-only initial
Dynamic Frontier: functional
Governance: blocking
```

---

# 50. Acceptance Matrix Overview

## A0 — Integrity

- source hash；
- timestamp；
- version lineage；
- append-only audit。

## A1 — Frozen-Time

- post-cutoff source rejected；
- ambiguous date flagged。

## A2 — Baseline Blindness

- leakage detected；
- contaminated baseline excluded。

## A3 — Prior Art

- substantive prior art lowers residual；
- no-match does not claim nonexistence。

## A4 — Revision

- score can go down；
- score can go up；
- unresolved transition supported。

## A5 — Failure Correction

- adding misses changes selection-adjusted output where appropriate。

## A6 — Frontier

- historical/current separate；
- Pareto works；
- no required unique champion。

## A7 — Governance

- no global person leaderboard；
- identity inference blocked；
- evidence/failures visible。

---

# 51. Hard Blocking Failures

任何一項失敗，Reference MVP 不得稱：

$$
\boxed{
TCFT\text{-}BTAP\ v0.1\ Conformant.
}
$$

Blocking：

1. post-cutoff leakage；
2. candidate answer leakage into primary baseline；
3. overwrite audit history；
4. no evidence confidence；
5. no failure handling；
6. score cannot decrease；
7. identity inferred from cognitive score；
8. global person rank required by core data model。

---

# 52. Non-Blocking Experimental Failures

可標 experimental：

- operator recovery disagreement；
- domain-seed recovery low confidence；
- Mahalanobis instability；
- cross-substrate equivalence uncertainty。

---

# 53. Acceptance Metrics

## 53.1 Leakage Detection Recall

在 B0：

$$
\boxed{
Recall_{leak}
\ge 0.95
}
$$

作初始工程目標。

---

## 53.2 Revision Correctness

預設 synthetic revision tests：

$$
\boxed{
100\%\ expected\ direction
}
$$

對 deterministic fixtures。

---

## 53.3 Audit Reproducibility

D0 fixtures：

$$
\boxed{
100\%\ deterministic.
}
$$

---

## 53.4 Structural Inter-Rater

RP / NC experimental：

報：

- agreement；
- confidence；
- unresolved rate。

v0.1 不硬設極高門檻。

---

# 54. Benchmark Health Dashboard

顯示：

- saturation；
- contamination；
- case freshness；
- baseline freshness；
- metric drift；
- unresolved rate。

---

# 55. Benchmark Revision Policy

若：

- baseline capability jump；
- new model generation；
- major prior-art provider improvement；

release：

$$
Benchmark^{v+1}.
$$

舊版不刪。

---

# 56. Live / Dynamic Benchmarking

參考動態 benchmark 的方法學：

- fresh items；
- objective grading where possible；
- contamination notes；
- rolling difficulty。

TCFT 不是直接複製 LiveBench，而是將其「benchmark 也會老化」原則移植到 cognition frontier。

---

# 57. Concept Drift Analogy

TCFT baseline：

$$
B(t)
$$

本身 non-stationary。

因此：

$$
\boxed{
\text{Static audit}
\rightarrow
\text{baseline obsolescence}.
}
$$

Reference runtime 每個 current audit 都必須保存：

$$
BaselineVersion.
$$

---

# 58. Delayed Verification

某些 claim：

$$
Y_t
$$

多年後才可驗證。

因此 audit ledger 支援：

```text
NOT_DUE
PARTIAL_EVIDENCE
VERIFIED
FALSIFIED
UNRESOLVED
```

---

# 59. Delayed Understanding

Artifact 可先保存：

$$
ValueStatus=UNKNOWN.
$$

後來重估：

$$
ValueStatus=UPDATED.
$$

但不回寫 historical context。

---

# 60. TCO Integration

TCO 提供：

```text
claim
source
timestamp
version
baseline forecast
outcome
classification
```

TCFT-BTAP 額外：

```text
problem_space
future_space
counterfactual
reflexive
reasoning_governance
native_structure
frontier_profile
```

---

# 61. ACO Integration

ACO 的 anomalous claim：

$$
c
$$

可被 TCFT 審查：

> claim holder 是否具有 unusual cognition trace？

但：

$$
\boxed{
CognitiveAnomaly
\neq
CausalAnomaly.
}
$$

兩者結果分開。

---

# 62. CODT Integration

CODT provider interface：

```text
recover_operators(trace)
recover_program(trace_history)
recover_domain_seed(program_set)
```

TCFT 僅消費結果與 confidence。

---

# 63. Explainability Requirement

每個 score 必須能回答：

> Why?

最低：

- supporting evidence；
- baseline difference；
- prior-art matches；
- metric assumptions；
- confidence warnings。

---

# 64. No Unexplained High Score

如果：

$$
Score>Threshold
$$

但沒有 evidence refs：

$$
\boxed{
FAIL.
}
$$

---

# 65. Audit Report Template

```text
Audit ID
Subject Type
Artifact
Frozen-Time Cutoff
Provenance Grade
Prior-Art Summary
Baseline Ensemble
Contamination Status
Capability Profile
Evidence Profile
Known Failures
Historical Status
Current Status
Persistent Status
Pareto Membership
Warnings
Revision Lineage
```

---

# 66. Example Result Semantics

允許：

> 在 1952 截止資料、Baseline v0.3 下，該 artifact 的 PG 與 RP 呈現高殘差；TN 證據中等，因非英語 archive 覆蓋不足；目前 artifact persistence 低，因相關結構已被現代教育吸收。

不允許：

> 此人是跨時代天才。

---

# 67. Governance Language Linter

Reference MVP 可附簡單 rule linter。

阻擋核心輸出：

```text
superhuman
superior person
chosen one
time traveler confirmed
most intelligent human
```

除非內容是引用／否定／外部 claim。

---

# 68. Privacy Boundary

對私人 subject：

- user-authorized data only；
- no covert profiling；
- no hidden personal ranking。

---

# 69. Public Figure Boundary

即使是 public figure：

- cognitive claims must cite public evidence；
- no mental-health inference；
- no hidden private identity inference。

---

# 70. Reference MVP CLI

候選：

```text
tcft ingest
tcft freeze
tcft prior-search
tcft baseline
tcft recover
tcft score
tcft frontier
tcft revise
tcft report
```

---

# 71. Example CLI Flow

```bash
tcft ingest case.yaml
tcft freeze CASE-001 --cutoff 1950-01-01
tcft prior-search CASE-001
tcft baseline CASE-001 --ensemble baseline_v0.1
tcft recover CASE-001
tcft score CASE-001
tcft frontier --time 1950-01-01
tcft report CASE-001
```

---

# 72. Reference Data Files

```text
case.yaml
artifact.json
sources.jsonl
prior_art.jsonl
baselines.jsonl
structures.json
scores.json
evidence.json
audit_ledger.jsonl
report.md
```

---

# 73. Test Strategy

## Unit

- date gates；
- hash；
- schema；
- contamination classification；
- normalization；
- Pareto。

## Integration

- full B0 audit；
- revision；
- provider swap。

## Regression

- canonical cases；
- old benchmark versions。

## Acceptance

- A0–A7。

---

# 74. TDD Recommendation

Reference runtime 建議：

$$
\boxed{
\text{protocol tests before metric sophistication}.
}
$$

先確保：

- 不洩漏；
- 不覆寫；
- 會降級；
- 會標 unresolved。

再追求更聰明的 metric。

---

# 75. Minimal First Implementation Order

1. schema；
2. ledger；
3. temporal gate；
4. synthetic benchmark；
5. baseline gate；
6. TN；
7. PG；
8. CF；
9. RG；
10. frontier；
11. RP / NC。

---

# 76. Why Not Start with Historical Celebrities?

因為最容易：

- halo；
- archive ambiguity；
- mythologization；
- no ground truth。

B0 synthetic 必須先通過。

---

# 77. Why Synthetic Matters?

因為只有 synthetic 能精確知道：

- hidden prior art；
- true timestamp；
- leakage；
- intended revision direction。

---

# 78. Historical Benchmark Is Phase 2+, Not Protocol Proof

歷史案例用來：

$$
\boxed{
\text{stress the framework},
}
$$

不是證明 protocol 基礎正確的第一步。

---

# 79. MVP Success Definition

Reference MVP 成功：

$$
\boxed{
\begin{aligned}
&ProtocolIntegrity=PASS\\
&FrozenTime=PASS\\
&CandidateBlindness=PASS\\
&RevisionSensitivity=PASS\\
&EvidenceSeparation=PASS\\
&DynamicFrontier=PASS\\
&AntiCrownGovernance=PASS.
\end{aligned}
}
$$

---

# 80. MVP Does Not Need High NC Accuracy Yet

Native operator / domain-seed recovery 可以：

$$
\boxed{
EXPERIMENTAL.
}
$$

v0.1 先建立 interface 與 confidence semantics。

---

# 81. Research Questions After MVP

### RQ1

Frozen-Time 是否顯著改變 novelty judgment？

### RQ2

stronger baseline 是否系統性降低 false frontier？

### RQ3

program-level matching 是否提高 prior-art recall？

### RQ4

human-AI baseline jump 如何改變 current anomaly？

### RQ5

dynamic frontier 是否比 static ranking 更穩定？

### RQ6

Anti-Crown UI 是否降低 halo / hierarchy inference？

---

# 82. Reference Whitepaper Acceptance

本文件本身完成條件：

- architecture；
- schema；
- state machine；
- contamination；
- metric contract；
- benchmark tracks；
- acceptance matrix；
- governance；
- MVP phases。

---

# 83. Known Limitations

第一，Historical prior-art completeness 不可保證。

第二，AI training contamination 很難完全知道。

第三，structural recovery 仍帶 observer abstraction。

第四，human expert 也有 halo / school bias。

第五，baseline ensemble 成本可能很高。

第六，跨語言 structural matching 仍不成熟。

第七，RP / NC 目前最適合作 experimental。

第八，Pareto frontier 在高維 case 多時可能稠密。

第九，benchmark freshness 需要長期維護。

第十，TCFT-BTAP 不是本體身份判定器。

---

# 84. 結論

TCFT 理論系列回答：

> 「時代超前」是什麼？

TCFT-BTAP 回答：

> 「怎麼讓這個概念可以被真正測試、修正與重跑？」

真正的核心不是一個漂亮 score。

而是：

$$
\boxed{
\text{Evidence}
+
\text{Time}
+
\text{Prior Art}
+
\text{Baseline}
+
\text{Structure}
+
\text{Failure}
+
\text{Revision}.
}
$$

如果一個 audit 不能降級，

它不是審計。

如果一個 baseline 看過答案，

它不是 Frozen-Time baseline。

如果一個 novelty score 沒有 prior art，

它不是可靠 novelty audit。

如果一個人因高 cognitive residual 被轉成身份、人格或政治階級，

它違反 TCFT-09。

因此 Reference MVP 的真正第一目標不是：

> 找到最厲害的人。

而是：

$$
\boxed{
\text{建立一個不會因為想研究前沿，
最後反而製造王冠的可重現審計系統。}
}
$$

一旦這個 kernel 成立，

後續才有資格把：

- 歷史人物；
- contemporary humans；
- AI；
- human-AI systems；
- future-origin claims；

放進同一套明確標示限制的 benchmark。

TCFT 的工程終點因此不是「證明神話」。

而是：

$$
\boxed{
\text{make cognitive-frontier claims falsifiable,
versioned, revisable, and historically reconstructable}.
}
$$

---

# References

1. Russell, S. J., & Wefald, E. H. (1991). Principles of metareasoning. *Artificial Intelligence*, 49(1–3), 361–395.
2. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
3. Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on concept drift adaptation. *ACM Computing Surveys*, 46(4), 44.
4. Cerqueira, V., Gomes, H. M., Heyden, M., Pfahringer, B., & Bifet, A. (2026). A Framework for Evaluating and Benchmarking Concept Drift Detection Methods. arXiv:2606.07789.
5. White, C., et al. (2024/2025). LiveBench: A Challenging, Contamination-Limited LLM Benchmark.
6. Wu, W., Zhao, Y., Wang, Y., Li, S., Shao, J., Long, Y., & Zhang, C. (2026). NovBench: Evaluating Large Language Models on Academic Paper Novelty Assessment. *Findings of ACL 2026*, 32103–32133.
7. Neo.K. (2026). *TCFT-00 至 TCFT-09*. EveMissLab.
8. Neo.K. (2026). *Cognitive Operator-Domain Theory (CODT) Series 01–10*. EveMissLab.
9. Neo.K. (2026). *跨時間敘述觀測站技術白皮書*. EveMissLab.
10. Neo.K. (2026). *異常因果觀測站 ACO v0.1*. EveMissLab.

---

# Canonical Note

本文件 canonical source 使用 UTF-8。

數學 delimiter：

- inline：` $...$ `
- display：`$$...$$`

Reference implementation 應以本文件、JSON Schema、Acceptance Matrix 為 v0.1 engineering contract。
