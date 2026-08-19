---
title: "DEST Runtime、Benchmark 與全域證書系統：AI 原生動態知識空間的可執行驗證架構"
title_en: "DEST Runtime, Benchmark, and Global Certificate System: An Executable Verification Architecture for AI-Native Dynamic Epistemic Spaces"
series: "動態知識空間論（Dynamic Epistemic Space Theory, DEST）"
series_id: "EML-DEST-2026-12"
version: "v0.1"
date: "2026-08-13"
language: "zh-Hant"
document_type: "系列第十二篇／第一輪正典封頂篇／Runtime／Benchmark／Certificate System"
status: "Canonical Draft"
depends_on:
  - "EML-DEST-2026-00 動態知識空間總論 v0.1"
  - "EML-DEST-2026-01 多域知識判定論 v0.1"
  - "EML-DEST-2026-02 多維知識覆蓋論 v0.1"
  - "EML-DEST-2026-03 Gap 場論 v0.1"
  - "EML-DEST-2026-04 關聯拓撲與全域黏合 v0.1"
  - "EML-DEST-2026-05 多中心知識拓撲 v0.1"
  - "EML-DEST-2026-06 移動邊界論 v0.1"
  - "EML-DEST-2026-07 條件依賴知識演化 2.0 v0.1"
  - "EML-DEST-2026-08 概念積分 2.0 v0.1"
  - "EML-DEST-2026-09 表示逃逸與解空間導航 2.0 v0.1"
  - "EML-DEST-2026-10 知識壓縮、生成核心與動態不動點 2.0 v0.1"
  - "EML-DEST-2026-11 視域、注意與知識載入 2.0 v0.1"
  - "ANKER Runtime v0.1"
---

# DEST Runtime、Benchmark 與全域證書系統
## AI 原生動態知識空間的可執行驗證架構

## 摘要

本文是《動態知識空間論》（DEST）第一輪正典系列的第十二篇與封頂篇。

DEST-00 至 DEST-11 已依序建立多域判定、Coverage、Gap、Global Glue、多中心、移動邊界、條件依賴演化、概念積分、表示逃逸、生成核心與視域／注意。若這些理論不能被編成一套可執行系統，則它們仍只是彼此相關的方法論集合。

因此本文的核心問題只有一個：

\[
\boxed{
\text{Can DEST be made runnable, falsifiable, replayable, and benchmarkable?}
}
\]

本文回答：

\[
\boxed{
\text{可以提出一個最小可執行規格；但其價值必須由 benchmark 證明，而非由框架本身宣告。}
}
\]

定義 DEST Runtime 狀態：

\[
\boxed{
\mathfrak R_t^{DEST}
=
\left\langle
\mathbb K_t,
\mathcal V_t,
\mathfrak B_t,
\mathcal E_t,
\mathcal Q_t,
\mathcal L_t,
\mathcal C_t^{cert},
\mathcal M_t
\right\rangle
}
\]

其中 \(\mathbb K_t\) 是 DEST 知識狀態，\(\mathcal V_t\) 是當前視域，\(\mathfrak B_t\) 是 branch family，\(\mathcal E_t\) 是 event stream，\(\mathcal Q_t\) 是 task queue，\(\mathcal L_t\) 是 append-only ledger，\(\mathcal C_t^{cert}\) 是 certificate dependency graph，\(\mathcal M_t\) 是 runtime metrics / observability state。

完整主循環：

\[
\boxed{
\mathbb K_t
\overset{\mathsf{Detect}}{\longrightarrow}
\mathbf G_t
\overset{\mathsf{Route}}{\longrightarrow}
\mathsf{Action}
\overset{\mathsf{Sandbox}}{\longrightarrow}
\mathsf{Candidate}
\overset{\mathsf{Guard}}{\longrightarrow}
\mathsf{Judge}
\overset{\mathsf{Verify}}{\longrightarrow}
\mathsf{Glue}
\overset{\mathsf{Commit}}{\longrightarrow}
\mathbb K_{t+1}
}
\]

並在提交後持續：

\[
\boxed{
\mathsf{Observe}
\rightarrow
\mathsf{DriftAudit}
\rightarrow
\mathsf{Revoke/Reopen}
\rightarrow
\mathsf{Replay}
\rightarrow
\mathsf{Benchmark}.
}
\]

本文將生成器視為：

\[
\boxed{\text{untrusted proposal source}.}
\]

任何 LLM、Agent、人類、搜尋器、演化算法、外部工具、定理產生器或資料生成器，都不得因為「能生成」而取得知識提交權。

提交必須通過：

\[
\boxed{
\mathsf{CommitGate}
=
\mathsf{Identity}
\land
\mathsf{Type}
\land
\mathsf{Scope}
\land
\mathsf{Provenance}
\land
\mathsf{Verification}
\land
\mathsf{Globality}
\land
\mathsf{NonCollapse}
\land
\mathsf{Version}
}
\]

其中某些 Gate 可依任務標為 `NOT_APPLICABLE`，但不得默默跳過。

本文將 DEST-00 的七項 GlobalCert 升級為：

\[
\boxed{
\mathsf{DESTCert}_t
=
\left\langle
C_D,
C_\rho,
C_G,
C_{\mathrm{transition}},
C_{\mathrm{loop}},
C_{\mathrm{branch}},
C_{\mathrm{repr}},
C_{\mathrm{version}},
C_{\mathrm{source}},
C_{\mathrm{boundary}},
C_{\mathrm{core}},
C_{\mathrm{view}},
C_{\mathrm{evolution}},
C_{\mathrm{replay}}
\right\rangle.
}
\]

每一 component 使用：

\[
\boxed{
\{
PASS,
PARTIAL,
FAIL,
STALE,
UNKNOWN,
NOT\_APPLICABLE,
REVOKED
\}.
}
\]

本文建立 Certificate DAG：

\[
\boxed{
\mathcal G_{\mathrm{cert}}
=
(
V_{\mathrm{cert}},
E_{\mathrm{depends}}
)
}
\]

使任何 dependency 被撤銷時能向下游傳播 stale / invalidation。

本文提出五階 benchmark：

\[
\boxed{
\text{Module}
\rightarrow
\text{Interaction}
\rightarrow
\text{End-to-End}
\rightarrow
\text{Long-Horizon Adversarial}
\rightarrow
\text{Open-World}.
}
\]

並建立：

\[
\boxed{\mathsf{BenchmarkOracleCert}}
\]

因為 benchmark 自己也可能錯。測試通過可能只是 oracle 太弱、hidden tests 不完整、solution leakage、metric gaming 或 contamination。

因此：

\[
\boxed{\text{System Under Test}}
\]

與：

\[
\boxed{\text{Benchmark Under Test}}
\]

必須同時存在。

本文最後給出一個最小 MVP：Python、SQLite/PostgreSQL、append-only event ledger、content-addressed artifact store、typed schemas、deterministic scheduler、test runner、可選 Lean/Coq/SMT adapter、provenance graph、certificate graph、replay runner、benchmark harness 與 dashboard。

MVP 不需要先做 AGI。它只需要驗證：

\[
\boxed{
\text{相較 flat LLM/RAG，DEST Runtime 是否能降低 overclaim、提高 replayability、branch preservation、verification yield 與 long-horizon recovery？}
}
\]

若不能，DEST Runtime 沒有工程優勢。

---

# 0. 非主張聲明

本文不主張 DEST 已優於現有 Agent framework；不主張 certificate 等於 truth、provenance 等於 validity、hash 等於可信來源、benchmark 分數等於一般智能、replayability 等於正確性、synthetic benchmark 成功等於 open-world 成功，也不主張 full DEST 一定比簡化版更好。

---

# 1. Runtime 第一原則：生成與提交分權

生成者：

\[
\mathsf{Proposer}.
\]

提交者：

\[
\mathsf{CommitController}.
\]

兩者不得是同一不可審核權限。

# 2. Trust Boundary

```text
Untrusted:
  LLM generator
  external documents
  retrieved snippets
  human/model proposals
  uncertified tool output

Conditionally Trusted:
  parser
  type checker
  deterministic tests
  proof checker
  data validator

Governed:
  commit controller
  revocation controller
  benchmark oracle authority
```

# 3. Runtime 不以模型為中心

模型只是 replaceable proposal / routing / interpretation provider；核心持久狀態在 Runtime。

# 4. DEST Kernel

\[
\boxed{
\mathsf{DESTKernel}
=
(
State,
Ledger,
Schema,
Guard,
Certificate,
Replay
).
}
\]

# 5. State Store

保存 \(\mathbb K_t\)，大型 artifacts 可只存 content reference。

# 6. Event Ledger

\[
\mathcal L_t=\{e_0,\ldots,e_t\}.
\]

建議 append-only。

# 7. Artifact Store

保存 paper、proof、code、dataset、logs、benchmark fixtures、model outputs。

# 8. Content Addressing

使用：

\[
hash(content)
\]

作 bytes identity anchor。hash 不證明真值。

# 9. Schema Registry

所有核心物件使用 versioned schema。

# 10. Minimum Object Types

```yaml
ObjectType:
  KNOWLEDGE_UNIT
  RELATION
  GAP
  DOMAIN_PROFILE
  COVERAGE_PROFILE
  BOUNDARY
  CENTER
  BRANCH
  PROPOSAL
  CERTIFICATE
  EVENT
  VIEW
  CORE
  CORRIDOR
  BENCHMARK_CASE
  BENCHMARK_RUN
  ORACLE
```

# 11. Service Layer

至少有 Domain Router、Coverage Auditor、Gap Engine、Glue Auditor、Center Tracker、Boundary Tracker、Evolution Controller、Concept Proposer、Representation Navigator、Core Compressor、View Manager、Certificate Authority、Benchmark Harness、Replay Service。

# 12. Domain Router

輸出 \(D,O,R,J,V,L,G\) profile。

# 13. Coverage Auditor

輸出 \(\boldsymbol\rho\) 與 denominator state。

# 14. Gap Engine

輸出 typed Gap objects。

# 15. Glue Auditor

檢查 overlap、cocycle、cycle、branch、globality。

# 16. Center Tracker

輸出 multi-role center profile。

# 17. Boundary Tracker

追蹤 domain boundary、flux、churn、lag、false frontier。

# 18. Evolution Controller

管理：

```text
PROPOSE
VALIDATE
COMMIT
INVALIDATE
ROLLBACK
REOPEN
```

# 19. Concept Proposer

只產生 proposal set，不直接寫 verified。

# 20. Representation Navigator

執行 Fold / Bridge / Project / Lift / Compress / Reparam / ClassJump / Tunnel。

# 21. Core Compressor

產生 \((C,U,M,Recon,Cert)\)。

# 22. View Manager

管理：

\[
Available\to Retrieved\to Loaded\to Used.
\]

# 23. Certificate Authority

只管理 certificate lifecycle / dependency / revocation，不是「真理機器」。

# 24. Benchmark Harness

執行 cases、seeds、baselines、ablations、metrics、hidden oracle、trace collection。

# 25. Replay Service

重播：

\[
K_0\xrightarrow{e_1}K_1\to\cdots\to K_n.
\]

# 26. Runtime State Machine

```text
IDLE
↓
TASK_OPEN
↓
VIEW_BUILD
↓
GAP_DETECT
↓
ROUTE
↓
SANDBOX
↓
GUARD
↓
VERIFY
↓
GLUE
↓
COMMIT / FORK / DEFER / REJECT
↓
OBSERVE
↓
DRIFT_AUDIT
↓
REPLAY / REOPEN
↓
TASK_CLOSE
```

# 27. Sandbox First

高風險改動先作用於 \(K_t^{sandbox}\)，不得改 active head。

# 28. Commit Transaction

```text
prepare
→ validate dependencies
→ lock parent state
→ append event
→ update projection
→ publish active head
```

# 29. Explicit Commit

模型不得因「很有把握」直接提交。

# 30. Commit Policy

```yaml
CommitPolicy:
  PROPOSAL:
    verification: none
  JUDGEABLE:
    type_scope: required
  LOCALLY_VERIFIED:
    local_certificate: required
  GLOBAL:
    gluing_certificate: required
  CANONICAL:
    replay_provenance_version_audit: required
```

# 31. Event-Sourced Projection

active state 可由 ledger projection 產生。

# 32. Snapshot

為避免每次重播全部事件，保存 \(Snapshot_k\)。

# 33. Snapshot Integrity

保存 state hash、ledger head、schema version、runtime version。

# 34. Deterministic Replay

若所有 dependency deterministic：

\[
Replay(K_0,E_{1:n})=K_n.
\]

# 35. Stochastic Replay

需保存 seed、provider、model id、parameters、raw output、external response snapshot。

# 36. Replay Fidelity Vector

\[
\boxed{
\mathbf R_F
=
(
R_{\mathrm{state}},
R_{\mathrm{claim}},
R_{\mathrm{cert}},
R_{\mathrm{branch}},
R_{\mathrm{view}},
R_{\mathrm{artifact}}
).
}
\]

# 37. Provenance Layer

對每個 object 保存 Entity / Activity / Agent，可與 W3C PROV 對齊。

# 38. Internal Provenance

```yaml
provenance:
  entity_id: "..."
  generated_by: "activity-..."
  attributed_to: "agent-..."
  derived_from: []
  source_hashes: []
```

# 39. Provenance ≠ Validity

來源完整不推出 claim 正確。

# 40. Attestation Layer

對 artifact / run 可簽 who、what、inputs、environment、outputs、hash。

# 41. SLSA-like Alignment

適合 code/build/benchmark artifact provenance，不直接證 theorem truth。

# 42. Runtime Trace

每次 task 建 `TraceID`。

# 43. Span Examples

```text
retrieve
load
parse
typecheck
generate
verify
glue
commit
rollback
benchmark
```

# 44. Observability

可輸出 traces / metrics / logs；observability data 不是 epistemic certificate。

# 45. Certificate DAG

\[
\boxed{
G_{cert}
=
(V_c,E_d).
}
\]

# 46. Certificate Object

\[
\boxed{
c
=
(
id,
type,
subject,
scope,
conditions,
evidence,
dependencies,
issuer,
time,
version,
status
).
}
\]

# 47. Certificate Status

```yaml
CertificateStatus:
  PASS
  PARTIAL
  FAIL
  STALE
  UNKNOWN
  NOT_APPLICABLE
  REVOKED
```

# 48. Certificate Types

```yaml
CertificateType:
  IDENTITY
  TYPE
  SCOPE
  PROVENANCE
  VERIFICATION
  TRANSLATION
  GLOBAL_GLUE
  BOUNDARY
  CORE
  VIEW
  REPLAY
  BENCHMARK_ORACLE
  RUNTIME_BUILD
```

# 49. Revocation Propagation

上游 certificate revoked 時，下游 descendants 至少進 `STALE`，除非存在另一條獨立證明路徑。

# 50. Global DEST Certificate 2.0

\[
\boxed{
DESTCert
=
(
C_D,
C_\rho,
C_G,
C_T,
C_L,
C_{Br},
C_R,
C_V,
C_S,
C_B,
C_C,
C_{View},
C_E,
C_{Replay}
).
}
\]

# 51. Global PASS

只在 task-required certificate set 全部 PASS 時成立。

# 52. Partial PASS

不得向使用者渲染成 full pass。

# 53. Certificate Capsule

```yaml
dest_certificate:
  subject: "claim-..."
  scope: "..."
  status: "PARTIAL"
  components:
    domain: PASS
    coverage: PASS
    gap: PASS
    transition: PASS
    loop_global: UNKNOWN
    branch: PASS
    representation: PASS
    verification: PASS
    provenance: PASS
    boundary: PARTIAL
    core: NOT_APPLICABLE
    view: PASS
    evolution: PASS
    replay: PASS
  dependencies: []
  stale_if: []
```

# 54. Certificate Freshness

證書需支援 stale trigger：source/tool/theorem/data/representation/benchmark oracle 版本變化。

# 55. Benchmark 是第二個 Runtime

Benchmark Harness 自己也有 state、version、oracle、fixture、evidence、provenance。

# 56. Benchmark Case

\[
\boxed{
b
=
(
input,
world,
hidden\_state,
oracle,
metrics,
budget,
seed,
contamination
).
}
\]

# 57. Benchmark Oracle

\[
\mathsf O_b
\]

回答：「什麼叫成功？」

# 58. Oracle Certificate

\[
\boxed{
\mathsf{BOC}
=
(
correctness,
coverage,
independence,
leakage,
version,
replayability
).
}
\]

# 59. Benchmark Threat Model

```text
solution leakage
test weakness
oracle bug
data contamination
environment nondeterminism
hidden tool outage
metric gaming
selection bias
survivorship bias
benchmark overfitting
```

# 60. 五階 Benchmark

\[
\boxed{
Module
\to
Interaction
\to
EndToEnd
\to
LongHorizon
\to
OpenWorld.
}
\]

# 61. DEST-01 Bench：Domain Qualification

case：retrieved-but-underconditioned、locally true but globally false、stale version、permission-limited。

metrics：domain classification accuracy、overpromotion rate。

# 62. DEST-02 Bench：Coverage

case：closed/open denominator、duplicate nodes、high-node/low-relation。

metrics：coverage calibration、denominator-state accuracy、debt localization。

# 63. DEST-03 Bench：Gap

case：missing relation、hidden condition、verification debt、primitive candidate、access Gap。

metrics：gap type accuracy、repair routing、false Gap rate。

# 64. DEST-04 Bench：Global Glue

case：all local pass、pairwise pass、triangle/cycle inconsistency、branch collision。

metrics：global-defect recall、false unification、branch preservation。

# 65. DEST-05 Bench：Centers

case：high-degree hub、low-degree articulation bridge、task shift、center migration。

metrics：role accuracy、hidden bridge recall、failure resilience。

# 66. DEST-06 Bench：Boundaries

case：reach expansion、verification retreat、split/merge、false frontier、representation-bound boundary。

metrics：event detection、signed direction、lag、false permanence。

# 67. DEST-07 Bench：Evolution

case：slow drift、abrupt change、version invalidation、rollback、branch birth。

metrics：transition classification、replay、stale detection、recovery。

# 68. DEST-08 Bench：Concept Integral

case：alias novelty、relational novelty、hidden bridge、false primitive、counterexample refinement。

metrics：verified proposal yield、false novelty、primitive spam。

# 69. DEST-09 Bench：Representation Escape

case：equivalent escape、task relaxation cheat、lossy projection、liftback failure、hidden oracle。

metrics：translation fidelity、lifecycle cost、false escape rate。

# 70. DEST-10 Bench：Core Compression

case：redundant corpus、multi-foundation、version update、future query、branch-preserving compression。

metrics：reconstruction、evidence retention、boundary retention、false irreducibility。

# 71. DEST-11 Bench：View

case：stored-not-loaded、loaded-not-used、middle-position evidence、hidden counterexample、sticky stale context。

metrics：retrieval recall、use coverage、false boundary、writeback pollution。

# 72. Tier 1：Interaction Bench

測 Coverage×View、Gap×Representation、Center×View、Boundary×Evolution、Core×View、Glue×Branch、Certificate×Version。

# 73. Tier 2：End-to-End Scenario

要求完整走過 retrieve→load→classify→Gap→proposal→verify→glue→commit→invalidate→rollback/reopen→replay。

# 74. Tier 3：Long-Horizon Adversarial

跨 \(N=100\sim10000\) events，注入 proposal flood、poisoned retrieval、provenance break、tool drift、cert revocation cascade、branch explosion、context thrash、oracle attack。

# 75. Tier 4：Open-World Pilot

真正 web / GitHub / scientific corpus，只在前三階穩定後做。

# 76. Baselines

```text
B0 Flat LLM
B1 RAG
B2 RAG + rerank + citations
B3 Stateful Knowledge Graph
B4 Verified Event Runtime
B5 Full DEST
```

# 77. Ablation

必須逐模組移除，否則無法知道複雜度增加的哪部分真的有用。

# 78. Primary Metrics

\[
\boxed{
M_{DEST}
=
(
O,V,R,P,B,G,C,L
)
}
\]

其中 O=overclaim、V=verification yield、R=replay fidelity、P=provenance completeness、B=branch preservation、G=globality accuracy、C=context utilization、L=lifecycle cost。

# 79. Overclaim Rate

proposal/local/retrieved/sampled 被誤升級成 verified/global 的比例。

# 80. Verification Yield

\[
\frac{\text{verified useful outputs}}{\text{verification cost}}.
\]

# 81. Replay Fidelity

重播 critical state 的比例。

# 82. Provenance Completeness

critical claims 可回溯比例。

# 83. Branch Preservation

應保存分支沒有被 forced merge 的比例。

# 84. Globality Accuracy

local/global 判斷正確率。

# 85. Context Utilization

loaded relevant information 實際使用率。

# 86. Lifecycle Cost

包含 model、search、verification、storage、replay、human、maintenance。

# 87. Secondary Metrics

Gap closure/transform、boundary lag、center resilience、coverage debt、false novelty、false irreducibility、cert staleness、rollback correctness、benchmark leakage。

# 88. Confidence ≠ Certificate

高 confidence 不能補 certificate 缺失。

# 89. Pareto Evaluation

如果更準但更貴，保留 cost-performance Pareto frontier。

# 90. Critical Hard Gates

高風險 benchmark 不允許平均分掩蓋 globality / branch / replay 災難性失敗。

# 91. Benchmark Dataset Structure

```yaml
benchmark_case:
  id: "DEST-B06-001"
  module_targets:
    - boundary
    - evolution
  visible_input: {}
  hidden_state: {}
  oracle: {}
  seed: 42
  budget: {}
  contamination_state: CLEAN_CANDIDATE
  expected_events:
    - VERIFICATION_RETREAT
    - CERT_STALE
```

# 92. Run Record

```yaml
benchmark_run:
  run_id: "..."
  runtime_version: "..."
  model_id: "..."
  config_hash: "..."
  benchmark_version: "..."
  outputs: []
  traces: []
  certificates: []
  costs: {}
  score: {}
```

# 93. Temporal Split

可用 post-cutoff events 降低記憶污染，但 temporal split 不保證完全乾淨。

# 94. Synthetic / Real / Hybrid

Synthetic 有 exact oracle；Real messy 但 oracle 難；Hybrid 用真實文件配 synthetic hidden structure。

# 95. Mutation Testing for Oracle

故意造錯 branch/version/condition/source/code patch；oracle 若照樣 PASS，證明 test 弱。

# 96. Oracle Sensitivity

\[
S_O=P(oracle=FAIL\mid known\ invalid\ mutation).
\]

# 97. Oracle Specificity

\[
P(oracle=PASS\mid known\ valid).
\]

# 98. Oracle Certificate Schema

```yaml
benchmark_oracle_certificate:
  benchmark_id: "..."
  version: "..."
  oracle:
    type: "deterministic|human|hybrid|formal"
  mutation_tests:
    invalid_cases: 100
    detected: 98
  leakage:
    contamination_status: "unknown"
  replay:
    deterministic: true
  status: "PARTIAL"
```

# 99. Continuous Evaluation

提交後仍要 monitor drift、error、latency、rollback、user correction、source invalidation。

# 100. Canary

高風險 Runtime update 可先在小 subset 運行；canary pass 不是 knowledge truth。

# 101. Quarantine

cert revoked / canary fail / drift high 時，variant 轉 `QUARANTINED`。

# 102. Authority Store

canonical state 不能被 rendering projection 反向覆寫。

# 103. Projection

同一 state 可輸出 Markdown、JSON、graph、SQL、UI、paper。

# 104. Schema Migration

v1→v2 需要 migration certificate，並重跑 replay regression。

# 105. Database MVP

最少 tables：

```text
knowledge_units
relations
domain_profiles
coverage_profiles
gaps
boundaries
centers
branches
proposals
certificates
certificate_dependencies
events
snapshots
views
cores
corridors
benchmark_cases
benchmark_runs
artifacts
```

# 106. API Layer

```text
POST /proposal
POST /verify
POST /commit
POST /revoke
POST /replay
POST /benchmark
GET  /state
GET  /certificate/{id}
GET  /trace/{id}
```

# 107. Scheduler

queue：verification、Gap、frontier、replay、stale cert、benchmark regression。

# 108. Scheduler Priority

\[
Priority
=
\frac{Value\cdot Risk\cdot Leverage\cdot Persistence}{Cost+\epsilon}.
\]

# 109. Verification Attention

若 \(\nu_{gen}>\nu_{verify}\)，scheduler 必須 throttle generation。

# 110. Regression Suite

任何 Runtime 更新都跑 replay regression、certificate regression、benchmark subset、migration test。

# 111. Metamorphic Testing

對不改變語義的 transformation，critical invariants 應保持，例如 alias rename、document order shuffle、irrelevant context insertion、representation-preserving transform。

# 112. Human Role

人類可定 task、approve high-risk commit、inspect branch、repair oracle、audit provenance；human review 也不是 infallible oracle。

# 113. Leaderboard Hygiene

分數綁 benchmark version、runtime version、model version、tool access、budget。

# 114. Budgeted Benchmark

固定 token/time/tool/money budget；最好報 anytime curve \(Score(B)\)。

# 115. Long-Horizon Reliability

測：

\[
P(\text{no catastrophic state corruption}\mid N\text{ events}).
\]

# 116. State Corruption

包括 false verified、branch deletion、provenance loss、stale cert active、replay failure。

# 117. Recovery Time / Completeness

測 fault 到 state recovered 的事件數／wall-time，並檢查 active state、provenance、branch、certificate 是否都恢復。

# 118. Runtime Health Vector

\[
\boxed{
H_R
=
(
H_{state},
H_{cert},
H_{replay},
H_{gap},
H_{branch},
H_{view},
H_{benchmark}
).
}
\]

# 119. Runtime Health ≠ Truth

健康系統仍可能缺資料。

# 120. Benchmark Health

\[
H_B=(oracle,leakage,coverage,replay,freshness).
\]

# 121. Benchmark Retirement

contamination high、oracle weak、ceiling 或已不具代表性時應 retire。

# 122. External Benchmark Alignment

GAIA 類任務測 tool/web/multimodal robustness；AgentBench 類環境測 multi-turn agent interaction；SWE-bench 類真實 issue→patch 任務測 repo context、execution 與 test oracle。DEST 額外測 state、certificate、branch、replay。

# 123. W3C PROV Alignment

```text
KnowledgeUnit → prov:Entity
VerificationRun → prov:Activity
Agent/Human/Tool → prov:Agent
```

# 124. SLSA Alignment

對 runtime binary / generated package 保存 source、builder、parameters、dependencies；不把 supply-chain provenance 當 theorem truth。

# 125. OpenTelemetry Alignment

用 distributed traces/metrics/logs 做 observability；不當 knowledge certificate。

# 126. NIST TEVV Alignment

Test / Evaluation / Validation / Verification 分開記錄。

# 127. MVP Phase 0：Schema

完成 object/event/certificate/benchmark schemas。

# 128. MVP Phase 1：Ledger Runtime

只做 event、state、commit、rollback、replay。

# 129. MVP Phase 2：Domain + Certificate

加入 domain router、cert DAG、revocation。

# 130. MVP Phase 3：Gap + Benchmark

加入 Gap Engine、Tier-0 benchmarks、regression。

# 131. MVP Phase 4：Global Glue

加入 cycle audit、branch preservation、global certificate。

# 132. MVP Phase 5：View + Core

加入 core compression、context loading、use coverage。

# 133. MVP Phase 6：Representation Navigation

加入 corridor tournament。

# 134. MVP Phase 7：Long-Horizon

跑 1000+ events。

# 135. Phase Gate

每階段若沒有比 baseline 改善，就不升級。

# 136. Minimal Stack

```text
Python
SQLite initially
Pydantic / JSON Schema
pytest
NetworkX optional
Git/content-addressed store
Lean/SMT optional
FastAPI optional
OpenTelemetry optional
```

# 137. Minimal Model Requirement

一個 API 或 local LLM 就夠。

# 138. Model Replaceability Test

換模型後 schema / ledger / replay 不應破壞；只有 model-specific certificates 需要重驗。

# 139. First Benchmark Pack

至少 100 cases，先平均分配到 Domain、Coverage、Gap、Glue、Center、Boundary、Evolution、Concept、Representation、Core/View。

# 140. Deterministic Scheduler First

第一版不用 learned scheduler，否則難判效果來自 DEST 還是 scheduler。

# 141. Core Research Questions

RQ1：是否降低 overclaim？  
RQ2：是否提高 recovery/replay？  
RQ3：是否提高 verification yield？  
RQ4：是否更好保存 branch？  
RQ5：是否改善 long-context effective use？  
RQ6：增加的成本是否值得？

# 142. Null Hypothesis

\[
\boxed{
H_0:
DEST_{full}
\text{ 不優於較簡單的 stateful RAG/event runtime。}
}
\]

# 143. Falsifiability

如果 overclaim 不降、replay 無改善、branch preservation 無改善且 cost 大增，則至少部分 DEST 模組不值得保留。

# 144. Modular Falsification

即使 full runtime 有用，某模組可能無增益，可刪。

# 145. Runtime 自身也使用 DEST-07

schema、verifier、benchmark、cert policy 都是 versioned knowledge objects。

# 146. Self-Modification Boundary

Runtime 不得直接修改自己的 commit rules；先 sandbox→benchmark→certificate→canary→explicit commit。

# 147. Benchmark-of-Benchmark

oracle mutation testing 是最小 meta-benchmark。

# 148. Trust Root

最終仍有外部 trust roots：cryptographic primitives、human governance、formal checker implementation、hardware、source institutions。

# 149. No Absolute Self-Certification

\[
\boxed{
\text{adding more certificates cannot make every trust dependency disappear}.
}
\]

# 150. Runtime Failure Taxonomy

| Code | 名稱 | 意義 |
|---|---|---|
| RT-00 | Proposal commit bypass | 未驗候選直入 active |
| RT-01 | State overwrite | 無事件帳本覆蓋狀態 |
| RT-02 | Certificate Boolean collapse | 多證書壓單一 verified |
| RT-03 | Revocation failure | 上游撤銷未傳播 |
| RT-04 | Replay illusion | 缺依賴仍宣稱可重播 |
| RT-05 | Provenance-truth confusion | 有來源冒充真 |
| RT-06 | Hash-truth confusion | hash 冒充可信 |
| RT-07 | Oracle weakness | benchmark tests 不足 |
| RT-08 | Benchmark leakage | solution 暴露 |
| RT-09 | Contamination blindness | training overlap 未標記 |
| RT-10 | Metric gaming | 系統鑽 scoring loophole |
| RT-11 | Globality bypass | local pass 冒充 global |
| RT-12 | Branch erasure | 多分支被 merge |
| RT-13 | Stale active cert | stale certificate 仍提交 |
| RT-14 | Version drift | tool/model/schema 漂移未處理 |
| RT-15 | View blindness | loaded≠used 未測 |
| RT-16 | Context pollution | stale background 污染 |
| RT-17 | Core overcompression | 重建責任丟失 |
| RT-18 | Representation cheat | task relaxation 冒充 escape |
| RT-19 | Benchmark overfit | 只對固定 case 有效 |
| RT-20 | Cost hiding | verification/human/storage 未計 |
| RT-21 | Self-certification loop | generator/verifier/issuer 無隔離 |
| RT-22 | Trust-root denial | 假裝系統完全自證 |
| RT-23 | Ablation omission | 無法知道模組增益 |
| RT-24 | Runtime complexity capture | 架構複雜被當成能力 |
| RT-25 | Certificate sprawl | 證書多但無 dependency discipline |
| RT-26 | Benchmark score absolutism | 分數冒充一般智能 |
| RT-27 | Canary-truth confusion | canary pass 冒充知識真 |
| RT-28 | Human-oracle absolutism | human review 冒充必然正確 |
| RT-29 | Open-world overclaim | synthetic success 冒充 open-world |



# 151. Global Acceptance Criteria

第一版 Runtime 不要求「很聰明」，只要求：

1. 狀態不亂；
2. claim 不亂升級；
3. source 不亂丟；
4. branch 不亂合；
5. certificate 可撤銷；
6. state 可重播；
7. benchmark 可重跑；
8. failure 可定位。

# 152. Phase-1 Success Threshold

相較簡單 baseline，可設定候選門檻：

- overclaim 顯著下降；
- replay fidelity > 95%；
- provenance completeness > 98%；
- branch preservation > 95%。

數字只是實驗配置，不是理論常數。

# 153. Phase-2 Success

同 budget 下 verification yield / globality accuracy 提升，recovery time 下降。

# 154. Phase-3 Success

長時程中 state corruption 低、stale propagation 正確、benchmark regression 可定位。

# 155. No-Go Condition

若：

\[
Cost_{DEST}\gg Cost_{baseline}
\]

但：

\[
Quality_{DEST}\approx Quality_{baseline},
\]

工程上不成立。

# 156. Simplification Rule

只保留能在 ablation 中證明價值的模組。

# 157. DEST Runtime 不是宗教

模組可替換、合併、刪除、重命名。

# 158. Canonical Theory vs Runtime Backend

正典理論只規定「哪些狀態需要分清」；backend 可換。

# 159. SQL Backend

早期適合 SQLite/PostgreSQL。

# 160. Graph Backend

relation / cert DAG 放大後可加入 graph DB。

# 161. Event Bus

多 Agent 時可加入。

# 162. Workflow Engine

長任務可加入。

# 163. Formal Backend

高風險數學可接 Lean、Coq、SMT、proof checker。

# 164. Scientific Backend

可接 notebook、simulator、lab automation、statistical test。

# 165. Code Backend

可接 container、CI、test suite、static analyzer。

# 166. Humanistic Backend

可接 source criticism、multi-interpretation、citation、argument graph；不得假裝形式證明涵蓋全部。

# 167. Cross-Domain Runtime

不同 domain 可共享 Kernel：event、cert、provenance、branch、replay。

# 168. Domain-Specific Verifier

Verifier 本身依 domain。

# 169. Global Schema / Local Semantics

這是 Runtime 的核心設計原則之一。

# 170. Machine-First Knowledge Unit

```yaml
knowledge_unit:
  id: "KU-..."
  version: "..."
  type: "theorem"
  statement: "..."

  domain_profile: {}
  coverage_profile: {}
  conditions: {}
  dependencies: []
  relations: []

  gaps: []
  boundaries: []
  centers: []

  verification:
    status: "PASS"
    cert_refs: []

  globality:
    status: "LOCAL_ONLY"

  provenance: []
  branch_id: "main"
  history_head: "..."
```

# 171. State Capsule

```yaml
dest_state:
  state_id: "K-..."
  parent: "K-..."
  time: "..."

  knowledge_units: []
  branches: []
  active_view: "V-..."
  core_family: "C-..."
  boundary_state: "B-..."

  ledger_head: "evt-..."
  cert_graph_head: "cert-..."
```

# 172. Runtime Manifest

```yaml
runtime_manifest:
  dest_version: "0.1"
  schema_version: "0.1"
  runtime_version: "0.1"

  model:
    provider: "..."
    id: "..."

  tools:
    - id: "python"
      version: "..."

  policies:
    commit: "..."
    certificate: "..."
    benchmark: "..."

  hashes:
    config: "..."
```

# 173. Repro Bundle

一個 benchmark run 應輸出：

```text
manifest
events.jsonl
state_snapshot.json
certificates.jsonl
trace.jsonl
metrics.json
artifacts/
benchmark_case.json
oracle_certificate.json
```

# 174. Repro Bundle Hash

整包可做：

\[
H_{bundle}.
\]

# 175. Public / Private Repro

公開資料可發布 bundle；敏感資料只發布 hash、schema、derived metrics、verifier attestation。

# 176. Privacy

provenance 不代表全部私人 source 必須公開。

# 177. Access-Controlled Provenance

```text
PUBLIC
PRIVATE
SEALED
HASH_ONLY
```

# 178. Final Runtime Loop

\[
\boxed{
\begin{aligned}
\mathbb K_t
&\to
\mathcal V_t
\to
\mathbf G_t
\to
\mathsf{Route}
\to
\mathsf{Proposal}
\\
&\to
\mathsf{Guard}
\to
\mathsf{Verify}
\to
\mathsf{Glue}
\to
\mathsf{Commit}
\\
&\to
\mathsf{Observe}
\to
\mathsf{Revoke/Reopen}
\to
\mathsf{Compress}
\to
\mathsf{Refrontier}
\to
\mathbb K_{t+1}.
\end{aligned}
}
\]

# 179. Runtime Invariant 1

未驗 proposal 永不靜默升格。

# 180. Runtime Invariant 2

任何 canonical state change 有 event。

# 181. Runtime Invariant 3

任何 certificate 有 scope / version / dependency。

# 182. Runtime Invariant 4

任何 branch merge 有 non-collapse audit。

# 183. Runtime Invariant 5

任何「不存在」聲明可追到 search scope。

# 184. Runtime Invariant 6

任何 global claim 有 globality state。

# 185. Runtime Invariant 7

任何 representation escape 有 TranslationCert。

# 186. Runtime Invariant 8

任何 core compression 有 reconstruction path。

# 187. Runtime Invariant 9

任何 stale dependency 可觸發 downstream recheck。

# 188. Runtime Invariant 10

Benchmark 自己有 version / oracle certificate。

# 189. Proposition A [PROP]

存在 provenance 完整但內容錯誤的 claim，因此：

\[
Provenance
\not\Rightarrow
Truth.
\]

# 190. Proposition B [PROP]

存在所有 module unit tests 通過，但 interaction benchmark 失敗的 Runtime：

\[
\forall i,\ Module_i=PASS
\not\Rightarrow
System=PASS.
\]

# 191. Proposition C [PROP]

若 certificate DAG 上游撤銷，下游 certificate 不能保持無條件 PASS，除非存在另一獨立證明路徑。

# 192. Proposition D [PROP]

Benchmark oracle 若不能 reject known-invalid mutation，則對該 failure class 不具辨識力。

# 193. Proposition E [PROP]

可重播的錯誤狀態仍然是錯誤狀態：

\[
Replayability
\not\Rightarrow
Validity.
\]

# 194. Conjecture 1：Certificate DAG Reduces Silent Staleness

相較 flat citation / boolean verification，dependency-aware certificate DAG 將提高 version invalidation 的偵測率。

# 195. Conjecture 2：Multi-Tier Bench Better Predicts Reliability

Module + Interaction + Long-Horizon Bench 應比 static QA 更能預測 stateful research agent 的長期完整性。

# 196. Conjecture 3：Oracle Certification Reduces False Progress

對 oracle 做 mutation testing 與 leakage audit，將降低「分數上升但能力未上升」的假進步。

# 197. Conjecture 4：Generation Throttling Improves Verified Value

當：

\[
\nu_{gen}\gg\nu_{verify},
\]

限制生成、增加 verification attention，會提高 verified value / lifecycle cost。

# 198. Conjecture 5：Full DEST May Not Be Optimal

不同 task family 的最優 Runtime 可能只需要 DEST 子集；這不是理論失敗，而是 ablation 應揭露的結果。

# 199. 實驗總綱

四軸：

\[
\boxed{
Correctness
+
Integrity
+
Recovery
+
Cost.
}
\]

# 200. Correctness

測 answer、verification、globality、domain classification。

# 201. Integrity

測 provenance、branch、certificate、version。

# 202. Recovery

測 rollback、reopen、replay、stale revalidation。

# 203. Cost

測 model、search、verification、storage、human、latency。

# 204. Statistical Reporting

報 mean、median、variance、confidence interval、per-case failure。

# 205. Long-Tail Failures

災難性長尾失敗單獨報，不被平均值吞掉。

# 206. Failure Case Archive

所有 fail 進：

\[
\mathcal H_{\mathrm{fail}}.
\]

# 207. Regression from Failure Archive

新版本必測舊 failure。

# 208. Benchmark Expansion

新 failure 可以轉成新 benchmark case。

# 209. Self-Improving Benchmark Loop

\[
Failure
\to
Case
\to
Regression
\to
RuntimeUpdate.
\]

# 210. Benchmark Co-Evolution Risk

Runtime 和 benchmark 共同演化會過擬合，因此保留 frozen hidden set。

# 211. Evaluation Splits

```text
DEV
FROZEN
LIVE
```

# 212. Final Acceptance Test

第一輪正典的工程驗收不是：

> 寫完 12 篇。

而是：

> 能否用 100-case MVP，讓簡單 baseline 和 DEST Runtime 產生可重複、可解釋的差異？

# 213. Minimum Publishable Engineering Result

至少有：

- dataset；
- runtime；
- ablation；
- replay bundle；
- failure analysis。

# 214. Negative Result Also Valuable

某模組沒用：

> 刪掉。

這本身就是研究結果。

# 215. Runtime Whitepaper Candidate

後續可獨立做：

```text
DEST Runtime v0.1
Implementation Specification
```

但不屬於本篇必要內容。

# 216. Series Closure

```text
00 Mother Theory
01 Domains
02 Coverage
03 Gaps
04 Global Glue
05 Centers
06 Boundaries
07 Evolution
08 Concept Integral
09 Representation Navigation
10 Core Compression
11 View / Attention
12 Runtime / Benchmark / Certificates
```

# 217. 最小核心公式

## Runtime State

\[
\boxed{
\mathfrak R_t^{DEST}
=
\langle
\mathbb K_t,
\mathcal V_t,
\mathfrak B_t,
\mathcal E_t,
\mathcal Q_t,
\mathcal L_t,
\mathcal C_t^{cert},
\mathcal M_t
\rangle.
}
\]

## Commit Gate

\[
\boxed{
Commit
=
Identity
\land
Type
\land
Scope
\land
Provenance
\land
Verification
\land
Globality
\land
NonCollapse
\land
Version.
}
\]

## Certificate DAG

\[
\boxed{
G_{cert}
=
(V_{cert},E_{depends}).
}
\]

## Global DEST Certificate

\[
\boxed{
DESTCert
=
(
C_D,
C_\rho,
C_G,
C_T,
C_L,
C_{Br},
C_R,
C_V,
C_S,
C_B,
C_C,
C_{View},
C_E,
C_{Replay}
).
}
\]

## Benchmark Oracle Certificate

\[
\boxed{
BOC
=
(
Correctness,
Coverage,
Independence,
Leakage,
Version,
Replayability
).
}
\]

## Benchmark Hierarchy

\[
\boxed{
Module
\to
Interaction
\to
EndToEnd
\to
LongHorizon
\to
OpenWorld.
}
\]

# 218. 結論

DEST 第一輪研究到這裡應正式停止繼續拆概念。

如果再持續增加概念，而不開始執行，框架本身會形成：

\[
\boxed{
\text{framework debt}.
}
\]

目前已足以回答：

- 知識在哪個 Domain？
- Coverage 到多少？
- Gap 在哪？
- 局部能不能黏成全域？
- 哪些節點扮演什麼中心？
- 邊界怎麼移動？
- 新 evidence 如何更新 state？
- 概念候選怎麼生成？
- 表示怎麼逃逸？
- 什麼值得壓成核心？
- 當前到底載入／使用哪些知識？

下一個真正重要的問題不再是：

> 還能不能再多一個理論維度？

而是：

\[
\boxed{
\text{這些維度是否能在同一個 Runtime 中真正改善 AI 的研究行為？}
}
\]

因此 DEST-12 將最終判決權交給 benchmark。

如果：

\[
DEST_{full}
\]

在同 budget 下不能比：

\[
RAG,
\quad
StatefulGraph,
\quad
EventRuntime
\]

降低 overclaim、提高 verification、replay、branch preservation、globality 與 recovery，那麼多出來的理論層就只是複雜度。

反過來，如果只有 DEST 的一部分有效：

\[
\boxed{
\text{就保留那一部分。}
}
\]

這也是 DEST 自己應遵守的條件依賴演化原則。

所以整個系列最後不以：

\[
\boxed{
\text{DEST is true}
}
\]

作結。

而以：

\[
\boxed{
\text{DEST is now specified enough to be tested.}
}
\]

作結。

一套 AI 原生知識理論真正進入工程與科學的分界，不是它有多少公式，而是：

\[
\boxed{
\text{它是否允許別人建立 baseline、重播實驗、找出失敗、撤銷證書，甚至證明某些模組根本沒有用。}
}
\]

從這一步開始，DEST 不再只是描述知識空間。

它成為：

\[
\boxed{
\text{可被反駁的 Research Runtime Hypothesis}.
}
\]

---

# 附錄 A：DEST Kernel

```yaml
DESTKernel:
  StateStore
  EventLedger
  SchemaRegistry
  GuardEngine
  CertificateGraph
  ReplayEngine
```

# 附錄 B：DEST Services

```yaml
DESTServices:
  DomainRouter
  CoverageAuditor
  GapEngine
  GlueAuditor
  CenterTracker
  BoundaryTracker
  EvolutionController
  ConceptProposer
  RepresentationNavigator
  CoreCompressor
  ViewManager
  CertificateAuthority
  BenchmarkHarness
```

# 附錄 C：Certificate Status

```yaml
CertificateStatus:
  PASS
  PARTIAL
  FAIL
  STALE
  UNKNOWN
  NOT_APPLICABLE
  REVOKED
```

# 附錄 D：Benchmark Tier

```yaml
BenchmarkTier:
  MODULE
  INTERACTION
  END_TO_END
  LONG_HORIZON_ADVERSARIAL
  OPEN_WORLD
```

# 附錄 E：外部形式與工程對照

1. W3C, *PROV-O: The PROV Ontology*, W3C Recommendation, 2013.
2. SLSA Specification v1.2, Provenance / Build Provenance.
3. OpenTelemetry official signals / traces documentation.
4. NIST, *AI Risk Management Framework 1.0* and AI Test, Evaluation, Validation and Verification (TEVV).
5. Mialon et al. (2023), *GAIA: a benchmark for General AI Assistants*.
6. Liu et al. (2023), *AgentBench: Evaluating LLMs as Agents*.
7. Jimenez et al. (2023/2024), *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*
8. Aleithan et al. (2024), *SWE-Bench+: Enhanced Coding Benchmark for LLMs*，只作 benchmark leakage / weak-test 風險對照。

# 附錄 F：內部正典依賴

- DEST-00 至 DEST-11。
- ANKER Runtime v0.1。
- AEREC MVP v0.3 Architecture。
- 文明級知識編譯器。
- Evidence-Ready / Verified Knowledge Runtime 系列。

# 附錄 G：下一階段

本輪正典到此封頂，不新增 DEST-13。

下一階段改成工程系列：

\[
\boxed{
\text{DEST Runtime v0.1}
}
\]

第一批交付物：

1. `schema/`
2. `runtime/ledger.py`
3. `runtime/state.py`
4. `runtime/certificates.py`
5. `runtime/replay.py`
6. `benchmarks/module/`
7. `benchmarks/interaction/`
8. `benchmarks/long_horizon/`
9. `dashboard/`
10. `README.md`

以及第一批：

\[
\boxed{
100\text{-case DEST Benchmark v0.1}.
}
\]

---

**EML-DEST-2026-12 · v0.1 · 2026-08-13**
