# GCM Conformance, Verification & Reference Implementation Specification
## Global Computation Methodology 合規測試、故障注入、證據契約與 Reference Runtime 驗收規格 v0.1

**文件類型：** Technical Whitepaper / Normative Conformance & Verification Specification  
**系列：** Global Computation Methodology（GCM）  
**版本：** v0.1  
**日期：** 2026-08-25  
**Canonical source format：** UTF-8 Markdown  
**數學 delimiter：** ` $...$ ` 與 `$$...$$`  
**狀態：** 第二輪第三份正式技術白皮書；直接上游為 TW-01 v0.1 與 TW-02 v0.1

---

## 摘要

TW-01 已將 GCM Series-00 與 Paper-01–06 收斂為 normative formal contract，固定 `GCM-C01`–`GCM-C28`；TW-02 則將這些契約映射為 Reference Runtime architecture，固定 `GCM-A01`–`GCM-A26`、state ownership、proposal isolation、Commit Gate、Foundation Revision Gateway、Observer read-side、Lifecycle plane 與 typed history store。

若沒有 conformance specification，實作仍可能出現一種危險狀態：文件宣稱保存所有邊界，但測試只驗「Happy Path 能跑」，從而讓 authority escalation、stale-parent commit、Observer mutation、history merge、crash ambiguity、Foundation drift 等錯誤在測試之外存在。

本文件因此回答：

> **一套 Runtime 必須提供哪些可重現證據，才能聲稱自己在特定 GCM profile 下符合 TW-01 / TW-02？**

本文件的核心原則是：

$$
\boxed{
\text{Conformance}
\neq
\text{Feature Count}
\neq
\text{Performance Score}
}
$$

以及：

$$
\boxed{
\text{Required MUST Failure}
\Rightarrow
\text{No Conformant Claim}
}
$$

因此 GCM v0.1 **不採百分比通過制**。對某一 declared profile $P$，合規定義為：

$$
\boxed{
\operatorname{Conformant}(SUT,P)=1
\iff
\forall t\in\operatorname{Req}(P),
\operatorname{Result}(t)=\mathsf{PASS}
}
$$

其中 `SUT` 為 System Under Test。任何 required test 若為 `FAIL`、`INDETERMINATE`、未執行的 `SKIP`，或未被 profile 明確允許的 `NOT_APPLICABLE`，都不得產生 `CONFORMANT` claim。

本文件同時建立：

- 54 個 `GCM-C/A` invariant-primary tests；
- 12 個 cross-cutting tests；
- 10 組 canonical negative / failure test vectors；
- `R0-M0`–`R0-M4` 累積式 MVP acceptance profiles；
- schema validation、architecture lint、deterministic behavior、negative test、fault injection、history/replay、resource/cost 七類測試；
- machine-readable conformance result schema；
- Reference Harness adapter contract；
- evidence bundle、digest、reproducibility 與 claim 規則。

---

# 0. 文件角色與規範優先級

本文件的上游優先級為：

$$
\boxed{
\text{TW-01}
\succ
\text{TW-02}
\succ
\text{TW-03 Test Encoding}
}
$$

若 TW-03 的某個 test vector 與 TW-01 的 MUST / MUST NOT 產生衝突，測試本身必須被修正，**不得以測試實作覆蓋 canonical contract**。

TW-03 的責任是：

1. 將 `GCM-C01`–`GCM-C28` 與 `GCM-A01`–`GCM-A26` 轉為可執行或可審計測試；
2. 定義 conformance profiles；
3. 定義 PASS / FAIL / INDETERMINATE 等結果語義；
4. 定義 required evidence；
5. 定義 architecture lint；
6. 定義 deterministic fixtures 與 virtual clock；
7. 定義 negative tests；
8. 定義 failure injection；
9. 定義 replay / provenance tests；
10. 定義 resource/cost tests；
11. 定義 Reference Runtime M0–M4 acceptance gates；
12. 定義 machine-readable conformance claim；
13. 定義 Reference Harness 與 SUT adapter interface。

本文件不：

- 指定唯一 testing framework；
- 指定唯一 programming language；
- 指定唯一 CI provider；
- 把 conformance 等同 performance benchmark；
- 把 self-test 等同第三方 certification；
- 要求 R0 profile 使用 distributed consensus；
- 要求 AI Router；
- 用 telemetry 取代 canonical history；
- 以 percentage score 赦免 MUST violation。

---

# 1. Normative language

本文中的 `MUST`、`MUST NOT`、`SHOULD`、`SHOULD NOT`、`MAY` 僅在全大寫時具有規範性意義。

合規 runner MUST 將：

- spec version；
- test-suite version；
- SUT version / build digest；
- schema digest；
- environment digest；
- deterministic seed；
- profile；
- test result；
- evidence references

寫入 machine-readable result bundle。

---

# 2. Validation、Verification、Conformance 的型別分離

GCM MUST 區分三個概念。

## 2.1 Structural validation

$$
\boxed{
\mathsf{ValidateSchema}(x,S)
}
$$

只回答 instance $x$ 是否符合 machine-readable schema $S$。

Schema-valid 不代表 semantic-valid：

$$
\boxed{
\text{Schema Valid}
\not\Rightarrow
\text{Semantically Admissible}
}
$$

## 2.2 Runtime verification

$$
\boxed{
\mathsf{VerifyCandidate}
(
\widetilde W,
\mathcal I,
\mathfrak X
)
}
$$

回答 candidate 是否滿足該 operation / World boundary / Foundation 下的 invariants。

## 2.3 Implementation conformance

$$
\boxed{
\mathsf{Conform}(SUT,P,T)
}
$$

回答某 implementation 是否通過指定 profile $P$ 與 test-suite version $T$ 的 required tests。

因此：

$$
\boxed{
\text{Validation}
\neq
\text{Verification}
\neq
\text{Conformance}
}
$$

---

# 3. Conformance profile model

Reference implementation 使用 TW-02 的 `R0`：

$$
\boxed{
R0
=
\text{Deterministic Single-Process Modular Monolith}
}
$$

`R0` 不要求 AI Router、不要求 distributed consensus，並採每一 World boundary 的 serial reference commit path。

TW-03 將 R0 再分成累積式 milestone profiles：

$$
R0\text{-}M0
\subset
R0\text{-}M1
\subset
R0\text{-}M2
\subset
R0\text{-}M3
\subset
R0\text{-}M4.
$$

| Profile | Required invariants | Primary tests | Supplemental tests | Claim scope |
|---|---:|---:|---:|---|
| `R0-M0` | 11 | 11 | 5 | Through M0 |
| `R0-M1` | 16 | 16 | 7 | Through M1 |
| `R0-M2` | 20 | 20 | 7 | Through M2 |
| `R0-M3` | 37 | 37 | 10 | Through M3 |
| `R0-M4` | 54 | 54 | 12 | Through M4 |

一個 implementation MAY 宣稱較低 milestone profile，即使尚未完成後續功能；但不得宣稱 `R0-M4` 而跳過任何 M0–M4 required test。

---

# 4. Result domain 與硬 Gate

每一 test 的結果只能是：

```text
PASS
FAIL
SKIP
NOT_APPLICABLE
INDETERMINATE
```

## 4.1 PASS

`PASS` MUST 同時表示：

1. test preconditions 成立；
2. action 已實際執行；
3. expected postconditions 成立；
4. forbidden outcomes 未發生；
5. required evidence 完整；
6. test runner 未偵測 source/profile mismatch。

## 4.2 FAIL

`FAIL` 表示 observable behavior 已違反 required invariant 或 architecture obligation。

## 4.3 SKIP

`SKIP` 只表示 test 未執行，**不能視為成功**。

對 required test：

$$
\boxed{
\mathsf{SKIP}
\Rightarrow
\text{No Conformant Claim}
}
$$

## 4.4 NOT_APPLICABLE

只允許 profile 明確標示 optional / excluded capability 的 test 使用。若 test 屬 profile-required invariant，`NOT_APPLICABLE` MUST 導致 claim `INCOMPLETE`，而不是 PASS。

## 4.5 INDETERMINATE

當 evidence 不足、環境漂移、fault injector 無法確認 crash point、resource variance 超過 declared tolerance、或 runner 無法區分兩個結果時，必須輸出 `INDETERMINATE`。

$$
\boxed{
\mathsf{INDETERMINATE}
\neq
\mathsf{PASS}
}
$$

---

# 5. 不採百分比合規

GCM v0.1 明確拒絕下列規則：

$$
\text{Conformant}
\iff
\frac{\#\mathsf{PASS}}{\#\mathsf{Tests}}>\theta.
$$

理由是不同 invariant 的安全地位不同。若一套 Runtime 通過 98% 測試，但失敗的 2% 是：

- `GCM-A01` Sole Ordinary World Writer；
- `GCM-C19` Authority Non-Escalation；

則它不能因為平均分高而宣稱 conformant。

非 normative benchmark MAY 另外建立性能分數，但：

$$
\boxed{
\text{Benchmark Score}
\not\Rightarrow
\text{Conformance}.
}
$$

---

# 6. Test classes

TW-03 v0.1 定義七種 canonical test class。

## 6.1 `schema_validation`

測：

- JSON Schema；
- version pinning；
- configuration registry；
- typed field separation；
- provenance object shape。

## 6.2 `static_architecture`

測：

- module ownership；
- forbidden writes；
- sole writer；
- Foundation isolation；
- plugin boundary；
- consensus/globality 非等價。

## 6.3 `deterministic_behavior`

使用固定 seed、virtual clock、canonical fixture 驗行為。

## 6.4 `negative`

故意提交不合法 request，要求 fail closed。

Negative test 的成功定義是：

$$
\boxed{
\text{Expected Refusal}
=
\mathsf{PASS}.
}
$$

## 6.5 `fault_injection`

在 transaction / storage / history boundary 注入 crash、timeout、lost acknowledgement、stale context。

## 6.6 `history_replay`

測：

- typed relations；
- endpoint/history separation；
- rollback/compensation；
- replay grades；
- history quotient / compression safety；
- Foundation lineage。

## 6.7 `resource_cost`

測 active support 與 cost 是否被錯誤等同，並要求 pinned environment / tolerance / metric evidence。

---

# 7. Evidence model

一個測試結果不是一句 `PASS` 字串。

Reference evidence bundle SHOULD 至少含：

```text
result.json
trace.ndjson
sut_manifest.json
```

依 test class 額外加入：

```text
provenance_export.json
metrics.json
fault_injection.json
schema_validation.json
ownership_snapshot.json
```

## 7.1 Evidence completeness

若 test 宣告 `evidence_required` 集合為 $E_t$，則：

$$
\boxed{
\operatorname{Result}(t)=\mathsf{PASS}
\Rightarrow
E_t
\subseteq
E_{\mathrm{bundle}}.
}
$$

缺 evidence 不得以「測試看起來有成功」補過。

## 7.2 Digest

conformance bundle SHOULD 對以下資訊產生 digest：

- SUT build；
- TW-01 source；
- TW-02 source；
- TW-03 source；
- test catalog；
- schemas；
- fixtures；
- test runner；
- environment profile。

這使：

$$
\boxed{
\text{Same Claim Label}
\not\Rightarrow
\text{Same Tested Artifact}.
}
$$

---

# 8. Determinism 與 Virtual Clock

R0 profile 的 conformance suite MUST 能使用 deterministic seed，並 SHOULD 使用 virtual clock。

必須區分：

$$
\tau^{\mathrm{host}},
\quad
\tau^{\mathrm{runtime}},
\quad
\tau^{\mathrm{observer}},
\quad
\tau_i^{\mathrm{domain}}.
$$

Test runner MUST NOT 以 host wall-clock time 當作所有語義時鐘的隱式真值。

若 test 依賴不可控 external service，則 suite MUST：

1. 使用 fixture / mock / recorded input；或
2. 將結果標記為 environment-dependent，且不得作 deterministic conformance 的唯一證據。

---

# 9. Reference Harness 與 SUT Adapter Contract

TW-03 不指定唯一 harness implementation，但 Reference MVP MUST 暴露等價於下列能力的 adapter：

```text
reset_fixture(fixture_id)
load_world(world_fixture)
load_foundation(foundation_fixture)
submit_operation(operation_request)
query_world_head(boundary_id)
query_runtime_state()
query_observer_state(observer_id)
query_authority(context_id)
snapshot_stores()
inject_fault(fault_spec)
revoke_authority(authority_ref)
advance_virtual_clock(clock_ref, delta)
export_provenance(scope)
export_materializations(scope)
collect_metrics(scope)
recover_runtime()
```

Adapter MAY 是 Python API、CLI、RPC、in-process test interface 或其他 transport。

但 adapter 本身不得繞過被測 Runtime 的 canonical gates。例如 test helper 不得直接寫 WorldStore 再宣稱 CommitGate 通過。

---

# 10. Architecture lint

Architecture lint 主要驗證 TW-02 ownership map。

至少必須檢查：

$$
\boxed{
\operatorname{OrdinaryWriter}(W)
=
\{\mathsf{CommitGate}\}
}
$$

以及：

$$
\boxed{
\operatorname{FoundationWriter}
=
\{\mathsf{FoundationRevisionGateway}\}
}
$$

Reference lint SHOULD 能讀取 machine-readable module ownership manifest，並對 plugin / module registration 做增量檢查。

若 production implementation 合併多個 logical module 到同一 OS process，仍必須能證明 logical ownership boundary 存在；process count 不是 conformance criterion。

---

# 11. Schema conformance

TW-02 的 runtime schema 與 TW-03 的 conformance artifact schema 使用 JSON Schema Draft 2020-12。

Schema suite MUST 至少驗：

1. schema 本身可被 metaschema 接受；
2. positive fixtures 通過；
3. negative fixtures失敗；
4. schema version pinning；
5. persisted objects 不因 registry 升版而被最新 schema 無條件重解釋；
6. extension-point unknown-field policy 可預測。

Schema validation 不能代替 runtime semantics tests。

---

# 12. Route / Authority / Admissibility negative tests

以下流程是核心 gating path：

$$
\boxed{
\text{Addressable}
\rightarrow
\text{Reachable}
\rightarrow
\text{Admissible}
\rightarrow
\text{Authorized}
\rightarrow
\text{Executable}
}
$$

Suite MUST 至少建立四種 contrast fixtures：

1. reachable but inadmissible；
2. admissible but unauthorized；
3. authorized but currently unreachable；
4. capable executor but no authority。

若 optimizer 存在，必須驗：

$$
\boxed{
\operatorname{Optimize}
\text{ only over }
\mathcal R_{\mathrm{safe}}.
}
$$

廉價但非法的 route 不得因 score 更高而被執行。

---

# 13. Executor / Bridge / Proposal tests

Executor success 只應產生 proposal：

$$
E_i
\rightarrow
\delta_i
\rightarrow
\mathsf{ProposalStore}.
$$

必須有 negative test 確認：

$$
\boxed{
\delta_i
\not\Rightarrow
W_{\nu+1}.
}
$$

Bridge tests 必須至少涵蓋：

- exact bridge；
- declared lossy bridge；
- undeclared loss；
- type mismatch；
- invariant-breaking representation；
- unavailable bridge。

$$
\boxed{
\text{Representable}
\not\Rightarrow
\text{Semantically Valid}.
}
$$

---

# 14. Reconciliation、Verification、Pre-Commit、Commit tests

Commit path 的最小順序為：

$$
\boxed{
\Delta
\rightarrow
\mathsf{Reconcile}
\rightarrow
\mathsf{Verify}
\rightarrow
\mathsf{PreCommit}
\rightarrow
\mathsf{Commit}
}
$$

測試 MUST 能分辨：

- no-conflict proposal；
- overlapping commuting proposals；
- overlapping noncommuting proposals；
- invariant failure；
- stale parent；
- Foundation drift；
- authority revocation；
- schema drift。

尤其：

$$
\boxed{
\text{Stale Parent}
\not\Rightarrow
\text{Implicit Rebase}.
}
$$

---

# 15. Observer / Projection / Materialization tests

Pure observation MUST 滿足：

$$
\boxed{
\Delta W=0.
}
$$

但允許：

$$
\Delta\Xi\neq 0,
\qquad
\Delta O\neq 0.
$$

因此 suite MUST 明確檢查 World head，而不能只看 API 回傳內容。

Materialization test MUST 驗證 artifact provenance 至少可以追溯：

- source World revision；
- Foundation version；
- projection contract；
- observer scope（若適用）；
- schema version；
- staleness / validity marker。

$$
\boxed{
\mathsf{Materialized}(x)
\not\Rightarrow
\mathsf{Canonical}(x).
}
$$

---

# 16. Lifecycle / Active Support tests

Lifecycle suite MUST 分開測：

```text
materialize
reactivate
archive
restore
evict
pin_active
pin_materialization
pin_retention
```

不可把它們壓成單一 boolean active flag。

Potential fixture 必須驗：

$$
\boxed{
\mathsf{Potential}(x)
\not\Rightarrow
x\in\operatorname{Obj}(W_\nu).
}
$$

若 potential object 真正被建立，必須走 ordinary proposal / authority / commit path。

---

# 17. Resource / Cost conformance

M4 MUST 包含至少兩個獨立 scale axes：

1. active support size；
2. inactive/archive/history population。

測試應固定 active support，逐步增加 inactive corpus，觀察：

$$
C^{\mathrm{step}}.
$$

這用來偵測隱藏 full scan。

但 TW-03 v0.1 **不指定單一跨硬體絕對 latency 門檻**。Reference MVP 應先使用：

- environment-pinned regression threshold；
- asymptotic workload trend；
- operation-specific budget。

因此：

$$
\boxed{
\text{Resource Conformance}
\neq
\text{One Universal Benchmark Number}.
}
$$

---

# 18. History / Provenance tests

History Store 必須能保存 typed relations，例如：

$$
\prec_{\mathsf{exec}},
\quad
\prec_{\mathsf{causal}},
\quad
\prec_{\mathsf{commit}},
\quad
\prec_{\mathsf{observer}},
\quad
\prec_{\mathsf{foundation}}.
$$

Suite MUST 建立至少一個 fixture 使不同 relations 的順序不一致，以防 implementation 偷偷用單一 sequence number 代替全部關係。

## 18.1 Endpoint equality

建立：

$$
W_a=W_b,
$$

但：

$$
H_a\neq H_b.
$$

要求 history identities 保留。

## 18.2 Unknown equivalence

$$
\boxed{
\text{Unknown Equivalence}
\Rightarrow
\text{No Merge}.
}
$$

## 18.3 Rollback / compensation

Rollback 與 compensation 都必須保留原事件。

$$
\boxed{
\text{Corrective Event}
\neq
\text{History Erasure}.
}
$$

---

# 19. Replay grades

Replay tests MUST 驗證 evidence-bound claim。

Reference grades：

```text
Exact
DeterministicInternal
SemanticEquivalent
Approximate
NonReplayable
```

若缺：

- deterministic seed；
- external input；
- model / executor version；
- bridge version；
- Foundation reference；
- irreversible side-effect evidence；

則 replay validator MUST 下調 claim 至可證明的最高 grade。

$$
\boxed{
\text{Replay Claim}
\preceq
\text{Replay Evidence}.
}
$$

---

# 20. Failure injection matrix

Reference M3 MUST 至少能在以下 boundary 注入 crash：

```text
F0  before executor starts
F1  after executor success / before proposal persistence
F2  after proposal persistence / before reconciliation
F3  after verification / before pre-commit
F4  after pre-commit marker / before World write
F5  after World write / before commit receipt finalization
F6  after commit receipt / before acknowledgement
F7  during compensation
F8  during archive/restore transition
F9  during Foundation revision publication
```

每次 recover 後，Runtime 必須能把 operation 分到至少：

```text
NOT_EXECUTED
EXECUTED_UNCOMMITTED
COMMITTED
COMMIT_STATE_UNCERTAIN
COMPENSATION_REQUIRED
```

若 storage protocol 可證明更精確狀態，MAY 增加 enum。

核心 invariant：

$$
\boxed{
\text{Crash}
\not\Rightarrow
\text{Silent Semantic Ambiguity}.
}
$$

---

# 21. External side-effect tests

Side effects 使用：

```text
Pure
Idempotent
Compensatable
Irreversible
Unknown
```

Suite MUST 驗：

- `Pure` 可安全重跑的條件；
- `Idempotent` 的 idempotency key / evidence；
- `Compensatable` 的 compensation contract；
- `Irreversible` 不得假裝 rollback；
- `Unknown` 在 unsafe retry 情境 fail closed。

$$
\boxed{
\text{External Effect}
\not\Rightarrow
\text{Rollbackable}.
}
$$

---

# 22. Supplemental cross-cutting tests

| Test | Class | From | Purpose |
|---|---|---|---|
| `GCM-T-X-001` | `schema_validation` | `M0` | SchemaBundleSelfValidation |
| `GCM-T-X-002` | `schema_validation` | `M0` | UnknownFieldForwardCompatibility |
| `GCM-T-X-003` | `static_architecture` | `M0` | SpecDigestPinning |
| `GCM-T-X-004` | `deterministic_behavior` | `M1` | DeterministicSeedRepetition |
| `GCM-T-X-005` | `negative` | `M1` | NegativeFixtureSanity |
| `GCM-T-X-006` | `static_architecture` | `M0` | EvidenceCompleteness |
| `GCM-T-X-007` | `deterministic_behavior` | `M4` | ClockIndependenceHarness |
| `GCM-T-X-008` | `fault_injection` | `M3` | CrashMatrixCompleteness |
| `GCM-T-X-009` | `history_replay` | `M3` | HistoryExportRoundTrip |
| `GCM-T-X-010` | `static_architecture` | `M0` | ProfileClaimCompleteness |
| `GCM-T-X-011` | `resource_cost` | `M4` | ResourceBaselineReproducibility |
| `GCM-T-X-012` | `history_replay` | `M3` | FoundationMigrationAudit |

這些 test 不直接對應單一 `GCM-C/A`，但用來防止 conformance harness 自己產生 false positive。

例如 `GCM-T-X-005` 必須證明 runner 真的能看到 negative fixture 失敗；否則一個永遠回 PASS 的 runner 也可能偽造漂亮報告。

---

# 23. Invariant-primary test mapping

每一條 `GCM-C01`–`GCM-C28` 與 `GCM-A01`–`GCM-A26` 至少有一個 primary canonical test。

| Invariant | Primary test | Class | From | Title |
|---|---|---|---|---|
| `GCM-C01` | `GCM-T-C01-01` | `static_architecture` | `M0` | World / Runtime Separation |
| `GCM-C02` | `GCM-T-C02-01` | `deterministic_behavior` | `M2` | Heterogeneous Globality |
| `GCM-C03` | `GCM-T-C03-01` | `deterministic_behavior` | `M0` | Boundary-relative Globality |
| `GCM-C04` | `GCM-T-C04-01` | `schema_validation` | `M0` | 24/72 Non-exhaustiveness |
| `GCM-C05` | `GCM-T-C05-01` | `deterministic_behavior` | `M4` | Computation / Observation / Materialization Separation |
| `GCM-C06` | `GCM-T-C06-01` | `negative` | `M4` | Observer Non-Mutation |
| `GCM-C07` | `GCM-T-C07-01` | `resource_cost` | `M4` | Global Dependency / Full Materialization Separation |
| `GCM-C08` | `GCM-T-C08-01` | `resource_cost` | `M4` | Recursive Globality / Full Expansion Separation |
| `GCM-C09` | `GCM-T-C09-01` | `resource_cost` | `M4` | Finite Active Realization |
| `GCM-C10` | `GCM-T-C10-01` | `history_replay` | `M3` | State / History Separation |
| `GCM-C11` | `GCM-T-C11-01` | `history_replay` | `M3` | Endpoint / History Closure Separation |
| `GCM-C12` | `GCM-T-C12-01` | `negative` | `M0` | Operation Layer Separation |
| `GCM-C13` | `GCM-T-C13-01` | `negative` | `M1` | Capability / Authority Separation |
| `GCM-C14` | `GCM-T-C14-01` | `negative` | `M0` | Proposal / Commit Separation |
| `GCM-C15` | `GCM-T-C15-01` | `negative` | `M3` | Local / Global Success Separation |
| `GCM-C16` | `GCM-T-C16-01` | `deterministic_behavior` | `M4` | Global Coherence / Synchronization Separation |
| `GCM-C17` | `GCM-T-C17-01` | `schema_validation` | `M0` | Domain / Physical Space Separation |
| `GCM-C18` | `GCM-T-C18-01` | `static_architecture` | `M1` | Mathematics / Optimization Separation |
| `GCM-C19` | `GCM-T-C19-01` | `negative` | `M1` | Authority Non-Escalation |
| `GCM-C20` | `GCM-T-C20-01` | `negative` | `M0` | Foundation Constancy of Ordinary Runtime |
| `GCM-C21` | `GCM-T-C21-01` | `schema_validation` | `M4` | Resolution Type Separation |
| `GCM-C22` | `GCM-T-C22-01` | `deterministic_behavior` | `M4` | Lifecycle Type Separation |
| `GCM-C23` | `GCM-T-C23-01` | `negative` | `M4` | Potential / Existence Separation |
| `GCM-C24` | `GCM-T-C24-01` | `resource_cost` | `M4` | Bounded Active / Bounded Cost Separation |
| `GCM-C25` | `GCM-T-C25-01` | `history_replay` | `M3` | Typed Order Separation |
| `GCM-C26` | `GCM-T-C26-01` | `history_replay` | `M3` | Rollback Persistence |
| `GCM-C27` | `GCM-T-C27-01` | `negative` | `M3` | Unknown History Equivalence Safety |
| `GCM-C28` | `GCM-T-C28-01` | `negative` | `M3` | Foundation Revision Governance |
| `GCM-A01` | `GCM-T-A01-01` | `static_architecture` | `M0` | Sole Ordinary World Writer |
| `GCM-A02` | `GCM-T-A02-01` | `static_architecture` | `M0` | Foundation Revision Isolation |
| `GCM-A03` | `GCM-T-A03-01` | `deterministic_behavior` | `M0` | Proposal Isolation |
| `GCM-A04` | `GCM-T-A04-01` | `negative` | `M1` | Route Non-Escalation |
| `GCM-A05` | `GCM-T-A05-01` | `deterministic_behavior` | `M1` | Safe-Set Optimization |
| `GCM-A06` | `GCM-T-A06-01` | `negative` | `M2` | Bridge Semantic Gate |
| `GCM-A07` | `GCM-T-A07-01` | `negative` | `M3` | Reconciliation Before Commit |
| `GCM-A08` | `GCM-T-A08-01` | `negative` | `M3` | Verification Before Commit |
| `GCM-A09` | `GCM-T-A09-01` | `negative` | `M3` | Parent Freshness |
| `GCM-A10` | `GCM-T-A10-01` | `negative` | `M3` | Foundation Freshness |
| `GCM-A11` | `GCM-T-A11-01` | `negative` | `M4` | Observer Read-Side Boundary |
| `GCM-A12` | `GCM-T-A12-01` | `schema_validation` | `M4` | Materialization Provenance |
| `GCM-A13` | `GCM-T-A13-01` | `deterministic_behavior` | `M4` | Lifecycle Plane Separation |
| `GCM-A14` | `GCM-T-A14-01` | `negative` | `M3` | Authority Recheck When Revocable |
| `GCM-A15` | `GCM-T-A15-01` | `history_replay` | `M3` | Typed History Relations |
| `GCM-A16` | `GCM-T-A16-01` | `history_replay` | `M3` | Rollback / Compensation Persistence |
| `GCM-A17` | `GCM-T-A17-01` | `negative` | `M3` | Unknown History Merge Safety |
| `GCM-A18` | `GCM-T-A18-01` | `history_replay` | `M3` | Replay Evidence Bound |
| `GCM-A19` | `GCM-T-A19-01` | `negative` | `M4` | Telemetry Separation |
| `GCM-A20` | `GCM-T-A20-01` | `negative` | `M2` | Plugin Non-Authority |
| `GCM-A21` | `GCM-T-A21-01` | `deterministic_behavior` | `M4` | No Single Clock Assumption |
| `GCM-A22` | `GCM-T-A22-01` | `static_architecture` | `M4` | Global Coherence / Consensus Separation |
| `GCM-A23` | `GCM-T-A23-01` | `fault_injection` | `M3` | Crash Semantic Recoverability |
| `GCM-A24` | `GCM-T-A24-01` | `schema_validation` | `M0` | Schema-Version Pinning |
| `GCM-A25` | `GCM-T-A25-01` | `negative` | `M2` | External Side-Effect Typing |
| `GCM-A26` | `GCM-T-A26-01` | `resource_cost` | `M4` | Bounded Active / Bounded Cost Separation |

`v0.1` 只要求最低一對一覆蓋。未來 TW-03 minor revision MAY 對高風險 invariant 增加多個 independent tests，但不得刪除既有 stable test ID 而不提供 migration / deprecation record。

---

# 24. Milestone acceptance gates

## 24.1 M0 — Canonical Kernel

M0 重點：

- state planes；
- registry；
- operation typing；
- proposal isolation；
- sole World writer；
- Foundation isolation；
- schema pinning。

M0 不要求 executor diversity，也不要求 replay engine 完整。

## 24.2 M1 — Reachability / Admissibility / Authority

M1 必須證明：

$$
\boxed{
\text{Can}
\neq
\text{May}.
}
$$

且 route selection 不會 escalation。

## 24.3 M2 — Heterogeneous Execution

M2 至少要有 3 個代表性 executor family，SHOULD 達 3–5 個。

M2 必須驗：

- heterogeneous configuration；
- bridge semantic gate；
- plugin non-authority；
- external side-effect typing。

不要求實作全部 72 cells。

## 24.4 M3 — Reconcile / Verify / Commit / History

M3 是第一個完整 transactional semantic closure：

$$
\boxed{
\text{Proposal}
\rightarrow
\text{Reconcile}
\rightarrow
\text{Verify}
\rightarrow
\text{Commit/Reject}
\rightarrow
\text{History}.
}
$$

M3 同時要求 crash recovery、replay evidence、typed history、Foundation lineage。

## 24.5 M4 — Observer / Materialization / Lifecycle / Bounded Runtime

M4 才要求完整 54 invariants coverage。

因此：

$$
\boxed{
R0\text{-}M4
=
\text{First Full GCM Reference Runtime MVP Conformance Profile}.
}
$$

---

# 25. Waiver 與 deviation policy

GCM v0.1 區分：

- **implementation deviation**：已知偏離規格；
- **test waiver**：由於環境/工具限制暫時未測；
- **profile exclusion**：profile 本來就不要求。

只有第三種可以不影響該 profile 的 conformant claim。

對 required MUST invariant：

$$
\boxed{
\text{Waiver}
\not\Rightarrow
\text{Conformant}.
}
$$

可以產生：

```text
NON_CONFORMANT_WITH_DOCUMENTED_DEVIATIONS
INCOMPLETE_TEST_EVIDENCE
```

但不能把它們改名成 `CONFORMANT`。

---

# 26. Conformance claim record

一個公開或內部 conformance claim MUST 至少包含：

```text
GCM spec version
TW-02 architecture version
TW-03 test-suite version
profile
SUT name/version/build digest
environment digest
schema digest
test catalog digest
required test results
evidence bundle digest
known deviations
execution timestamp metadata
```

其中 timestamp 只是 evidence metadata，不是 Runtime semantic order 的替代。

Machine-readable schema 位於：

```text
schemas/gcm_conformance_artifact.schema.json
```

---

# 27. Reference Implementation Specification

TW-03 對 Reference Runtime MVP 的實作要求不是「所有產品都照一個 repository 長相」，而是建立一個最小可測試面。

Reference implementation SHOULD 至少提供：

```text
runtime/
  foundation/
  world/
  operations/
  routing/
  execution/
  reconciliation/
  verification/
  commit/
  observer/
  lifecycle/
  history/

conformance/
  schemas/
  manifests/
  fixtures/
  vectors/
  runner/
  evidence/
```

## 27.1 Required hooks

MVP MUST 能：

- reset deterministic fixture；
- pin Foundation / World / schema versions；
- inject operation request；
- inspect proposal before commit；
- inspect World head；
- inspect Runtime / Observer plane；
- revoke authority between execute and commit；
- advance virtual clocks independently；
- inject crash at named transaction boundaries；
- export typed provenance；
- collect resource metrics；
- restore from checkpoint / archive fixture。

## 27.2 Test-only hooks MUST NOT redefine semantics

Fault injection 與 test adapters MAY 暴露內部 hook，但：

$$
\boxed{
\text{Test Hook}
\not\Rightarrow
\text{Production Authority}.
}
$$

測試碼不得讓不合法 operation「為了方便 fixture」直接跨過 CommitGate 或 FoundationRevisionGateway。

---

# 28. Machine-readable artifacts

TW-03 v0.1 canonical package 至少包含：

```text
schemas/gcm_conformance_artifact.schema.json
manifests/conformance_catalog_v0.1.json
manifests/mvp_conformance_gates_v0.1.json
test_vectors/core_negative_vectors_v0.1.json
SOURCE_MAP.json
```

其中 `conformance_catalog_v0.1.json` 是 test ID 與 invariant mapping 的 machine-readable canonical source。

Markdown table 僅是 rendering view；若 table 與 manifest 分叉，必須修復 source，不允許人工猜哪一個才正確。

---

# 29. Fresh prior-art positioning

TW-03 的 conformance 設計並非宣稱發明規格關鍵字、schema validation、標準化 conformance suite 或 provenance validity。

工程定位至少必須公平承認：

1. IETF BCP 14（RFC 2119 / RFC 8174）已長期規範 `MUST`、`SHOULD`、`MAY` 等 requirement language，並由 RFC 8174 明確限定只有全大寫使用時具有該特殊規範語義。
2. JSON Schema Draft 2020-12 已提供 machine-readable structural validation vocabulary、meta-schema 與 output model；GCM 直接使用而不重新發明 schema validator。
3. Kubernetes / CNCF conformance 已展示「跨實作使用同一套公開標準測試與可重跑證據」的成熟工程模式；GCM 借鏡這個理念，但測試對象是 GCM semantic boundaries，而非 Kubernetes API compatibility。
4. W3C PROV / PROV-CONSTRAINTS 已提供 provenance data model、constraints 與 validity reasoning；GCM History 可保留自身 typed relations，同時 SHOULD 維持向通用 provenance export 的可能性。
5. OpenTelemetry Semantic Conventions 已有 versioning、stability、deprecated replacement 等成熟規約；GCM test IDs / schema objects 同樣需要 stable identity 與 explicit migration，而不是無聲覆寫。

GCM-TW03 的真正工作是：

$$
\boxed{
\text{把 GCM 自己的 semantic invariants}
\rightarrow
\text{可重現、可審計、可失敗的 conformance evidence}.
}
$$

---

# 30. Security 與 adversarial implementation 注意事項

Conformance suite 不等於 security certification。

一個 Runtime 可以在 cooperative test environment 通過 semantic conformance，但 production 仍可能需要：

- OS/process isolation；
- capability security；
- sandbox；
- cryptographic identity；
- secrets management；
- network policy；
- tamper-evident logging；
- supply-chain verification。

尤其若 plugin / executor 不可信，TW-02 的 semantic authority contract 不應取代真正的 isolation。

同時 conformance runner 自己 SHOULD 假設 SUT 可能：

- 回傳假 PASS；
- 隱藏 direct World writes；
- sampling 掉失敗 history；
- 在 test mode 使用不同 semantics。

因此高風險測試 SHOULD 使用外部可觀察 evidence、store snapshot、independent digest 或 fault injection，而非只相信 SUT 自報 status。

---

# 31. Reference MVP 完成判準

當 `R0-M4` 所有 required tests 均 PASS，且 evidence bundle 完整時，才可以宣稱：

$$
\boxed{
\text{GCM Reference Runtime MVP v0.1}
\text{ conforms to }
R0\text{-}M4.
}
$$

這個 claim 不表示：

- production-ready；
- distributed-ready；
- secure against malicious code；
- performance optimal；
- 24／72 全格實作；
- 所有 World ontology 都已支援。

它只表示：

> **Reference Runtime 已在 deterministic R0 profile 下，以可重現證據實作並保存 GCM v0.1 的核心 semantic invariants。**

---

# 32. TW-03 至 MVP 交接

完成 TW-03 後，下一個 artifact 不再是第四份白皮書，而是：

$$
\boxed{
\text{GCM Reference Runtime MVP v0.1}.
}
$$

推薦實作順序仍為：

$$
M0
\rightarrow
M1
\rightarrow
M2
\rightarrow
M3
\rightarrow
M4.
$$

但每個 Milestone 完成時立即跑對應 cumulative conformance profile；不等全部寫完才第一次測。

也就是：

$$
\boxed{
\text{Implement}
\rightarrow
\text{Conform}
\rightarrow
\text{Advance Milestone}.
}
$$

而不是：

$$
\text{Implement Everything}
\rightarrow
\text{Hope the Semantics Match}.
$$

---

# Appendix A. Canonical invariant-primary test registry

| Invariant | Primary test | Class | From | Title |
|---|---|---|---|---|
| `GCM-C01` | `GCM-T-C01-01` | `static_architecture` | `M0` | World / Runtime Separation |
| `GCM-C02` | `GCM-T-C02-01` | `deterministic_behavior` | `M2` | Heterogeneous Globality |
| `GCM-C03` | `GCM-T-C03-01` | `deterministic_behavior` | `M0` | Boundary-relative Globality |
| `GCM-C04` | `GCM-T-C04-01` | `schema_validation` | `M0` | 24/72 Non-exhaustiveness |
| `GCM-C05` | `GCM-T-C05-01` | `deterministic_behavior` | `M4` | Computation / Observation / Materialization Separation |
| `GCM-C06` | `GCM-T-C06-01` | `negative` | `M4` | Observer Non-Mutation |
| `GCM-C07` | `GCM-T-C07-01` | `resource_cost` | `M4` | Global Dependency / Full Materialization Separation |
| `GCM-C08` | `GCM-T-C08-01` | `resource_cost` | `M4` | Recursive Globality / Full Expansion Separation |
| `GCM-C09` | `GCM-T-C09-01` | `resource_cost` | `M4` | Finite Active Realization |
| `GCM-C10` | `GCM-T-C10-01` | `history_replay` | `M3` | State / History Separation |
| `GCM-C11` | `GCM-T-C11-01` | `history_replay` | `M3` | Endpoint / History Closure Separation |
| `GCM-C12` | `GCM-T-C12-01` | `negative` | `M0` | Operation Layer Separation |
| `GCM-C13` | `GCM-T-C13-01` | `negative` | `M1` | Capability / Authority Separation |
| `GCM-C14` | `GCM-T-C14-01` | `negative` | `M0` | Proposal / Commit Separation |
| `GCM-C15` | `GCM-T-C15-01` | `negative` | `M3` | Local / Global Success Separation |
| `GCM-C16` | `GCM-T-C16-01` | `deterministic_behavior` | `M4` | Global Coherence / Synchronization Separation |
| `GCM-C17` | `GCM-T-C17-01` | `schema_validation` | `M0` | Domain / Physical Space Separation |
| `GCM-C18` | `GCM-T-C18-01` | `static_architecture` | `M1` | Mathematics / Optimization Separation |
| `GCM-C19` | `GCM-T-C19-01` | `negative` | `M1` | Authority Non-Escalation |
| `GCM-C20` | `GCM-T-C20-01` | `negative` | `M0` | Foundation Constancy of Ordinary Runtime |
| `GCM-C21` | `GCM-T-C21-01` | `schema_validation` | `M4` | Resolution Type Separation |
| `GCM-C22` | `GCM-T-C22-01` | `deterministic_behavior` | `M4` | Lifecycle Type Separation |
| `GCM-C23` | `GCM-T-C23-01` | `negative` | `M4` | Potential / Existence Separation |
| `GCM-C24` | `GCM-T-C24-01` | `resource_cost` | `M4` | Bounded Active / Bounded Cost Separation |
| `GCM-C25` | `GCM-T-C25-01` | `history_replay` | `M3` | Typed Order Separation |
| `GCM-C26` | `GCM-T-C26-01` | `history_replay` | `M3` | Rollback Persistence |
| `GCM-C27` | `GCM-T-C27-01` | `negative` | `M3` | Unknown History Equivalence Safety |
| `GCM-C28` | `GCM-T-C28-01` | `negative` | `M3` | Foundation Revision Governance |
| `GCM-A01` | `GCM-T-A01-01` | `static_architecture` | `M0` | Sole Ordinary World Writer |
| `GCM-A02` | `GCM-T-A02-01` | `static_architecture` | `M0` | Foundation Revision Isolation |
| `GCM-A03` | `GCM-T-A03-01` | `deterministic_behavior` | `M0` | Proposal Isolation |
| `GCM-A04` | `GCM-T-A04-01` | `negative` | `M1` | Route Non-Escalation |
| `GCM-A05` | `GCM-T-A05-01` | `deterministic_behavior` | `M1` | Safe-Set Optimization |
| `GCM-A06` | `GCM-T-A06-01` | `negative` | `M2` | Bridge Semantic Gate |
| `GCM-A07` | `GCM-T-A07-01` | `negative` | `M3` | Reconciliation Before Commit |
| `GCM-A08` | `GCM-T-A08-01` | `negative` | `M3` | Verification Before Commit |
| `GCM-A09` | `GCM-T-A09-01` | `negative` | `M3` | Parent Freshness |
| `GCM-A10` | `GCM-T-A10-01` | `negative` | `M3` | Foundation Freshness |
| `GCM-A11` | `GCM-T-A11-01` | `negative` | `M4` | Observer Read-Side Boundary |
| `GCM-A12` | `GCM-T-A12-01` | `schema_validation` | `M4` | Materialization Provenance |
| `GCM-A13` | `GCM-T-A13-01` | `deterministic_behavior` | `M4` | Lifecycle Plane Separation |
| `GCM-A14` | `GCM-T-A14-01` | `negative` | `M3` | Authority Recheck When Revocable |
| `GCM-A15` | `GCM-T-A15-01` | `history_replay` | `M3` | Typed History Relations |
| `GCM-A16` | `GCM-T-A16-01` | `history_replay` | `M3` | Rollback / Compensation Persistence |
| `GCM-A17` | `GCM-T-A17-01` | `negative` | `M3` | Unknown History Merge Safety |
| `GCM-A18` | `GCM-T-A18-01` | `history_replay` | `M3` | Replay Evidence Bound |
| `GCM-A19` | `GCM-T-A19-01` | `negative` | `M4` | Telemetry Separation |
| `GCM-A20` | `GCM-T-A20-01` | `negative` | `M2` | Plugin Non-Authority |
| `GCM-A21` | `GCM-T-A21-01` | `deterministic_behavior` | `M4` | No Single Clock Assumption |
| `GCM-A22` | `GCM-T-A22-01` | `static_architecture` | `M4` | Global Coherence / Consensus Separation |
| `GCM-A23` | `GCM-T-A23-01` | `fault_injection` | `M3` | Crash Semantic Recoverability |
| `GCM-A24` | `GCM-T-A24-01` | `schema_validation` | `M0` | Schema-Version Pinning |
| `GCM-A25` | `GCM-T-A25-01` | `negative` | `M2` | External Side-Effect Typing |
| `GCM-A26` | `GCM-T-A26-01` | `resource_cost` | `M4` | Bounded Active / Bounded Cost Separation |

---

# Appendix B. Cross-cutting test registry

| Test | Class | From | Purpose |
|---|---|---|---|
| `GCM-T-X-001` | `schema_validation` | `M0` | SchemaBundleSelfValidation |
| `GCM-T-X-002` | `schema_validation` | `M0` | UnknownFieldForwardCompatibility |
| `GCM-T-X-003` | `static_architecture` | `M0` | SpecDigestPinning |
| `GCM-T-X-004` | `deterministic_behavior` | `M1` | DeterministicSeedRepetition |
| `GCM-T-X-005` | `negative` | `M1` | NegativeFixtureSanity |
| `GCM-T-X-006` | `static_architecture` | `M0` | EvidenceCompleteness |
| `GCM-T-X-007` | `deterministic_behavior` | `M4` | ClockIndependenceHarness |
| `GCM-T-X-008` | `fault_injection` | `M3` | CrashMatrixCompleteness |
| `GCM-T-X-009` | `history_replay` | `M3` | HistoryExportRoundTrip |
| `GCM-T-X-010` | `static_architecture` | `M0` | ProfileClaimCompleteness |
| `GCM-T-X-011` | `resource_cost` | `M4` | ResourceBaselineReproducibility |
| `GCM-T-X-012` | `history_replay` | `M3` | FoundationMigrationAudit |

---

# Appendix C. Profile gate summary

| Profile | Required invariants | Primary tests | Supplemental tests | Claim scope |
|---|---:|---:|---:|---|
| `R0-M0` | 11 | 11 | 5 | Through M0 |
| `R0-M1` | 16 | 16 | 7 | Through M1 |
| `R0-M2` | 20 | 20 | 7 | Through M2 |
| `R0-M3` | 37 | 37 | 10 | Through M3 |
| `R0-M4` | 54 | 54 | 12 | Through M4 |

---

# Appendix D. Canonical conclusions

TW-03 v0.1 最終固定以下工程命題：

$$
\boxed{
\text{Conformance}
\neq
\text{Feature Count}
}
$$

$$
\boxed{
\text{Schema Validation}
\neq
\text{Runtime Verification}
\neq
\text{Implementation Conformance}
}
$$

$$
\boxed{
\text{Required MUST Failure}
\Rightarrow
\text{No Conformant Claim}
}
$$

$$
\boxed{
\text{PASS}
\Rightarrow
\text{Evidence Complete}
}
$$

$$
\boxed{
\text{Test Hook}
\not\Rightarrow
\text{Semantic Authority}
}
$$

$$
\boxed{
\text{Crash}
\not\Rightarrow
\text{Silent Semantic Ambiguity}
}
$$

$$
\boxed{
\text{Unknown History Equivalence}
\Rightarrow
\text{No Merge By Default}
}
$$

以及整個第二輪工程鏈：

$$
\boxed{
00\text{--}06
\rightarrow
\text{TW-01}
\rightarrow
\text{TW-02}
\rightarrow
\text{TW-03}
\rightarrow
\text{Reference Runtime MVP}.
}
$$
