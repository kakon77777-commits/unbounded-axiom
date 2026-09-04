# CSM Paper 08 — Closure-Space Runtime Semantics and Executable Reference Model
## 閉包空間數學論：Runtime 語義、狀態機、登錄器與可執行參考模型

**Version:** v0.1  
**Date:** 2026-08-27  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Status:** Executable Runtime Specification  
**Language:** zh-TW  
**Canonical source:** UTF-8 Markdown

---

## 摘要

Paper 00–07 已建立 CSM 的 closure object、scope typing、typed graph、frontier / cut / exhaustion、reopening dynamics、projection、cross-domain transfer 與 proof-carrying operator calculus。本文把它們收斂為第一版可直接實作的 runtime semantics。

核心 machine state：

$$
\boxed{
\mathsf{State}_\nu
=
\langle
G_\nu,\Sigma_\nu,C_\nu,D_\nu,F_\nu,K_\nu,O_\nu,X_\nu,P_\nu,L_\nu,\nu
\rangle
}
$$

其中依序為 native graph、status map、certificate registry、debt registry、frontier、cuts、obstruction covers、exhaustion、policies、ledger head 與 version。

所有 theorem-level mutation 必須以 transaction 執行：

$$
\boxed{
\mathsf{Txn}:
\mathsf{State}_\nu
\rightharpoonup
\mathsf{State}_{\nu+1}.
}
$$

核心安全原則：

$$
\boxed{
\text{No certificate path}
\Rightarrow
\text{No native theorem mutation}.
}
$$

---

# 1. 三層 Runtime

CSM Runtime 固定分三層：

$$
L_0=\text{Canonical Event Ledger},
$$

$$
L_1=\text{Native Materialized Closure State},
$$

$$
L_2=\text{Purpose-Specific Views}.
$$

`L0` 是 committed history 的 canonical source；`L1` 必可由 replay 重建；`L2` 包含 audit / research / visual / execution views，authority 永遠不得超過 native state。

---

# 2. Canonical Event Ledger

每個 committed event：

$$
e_i
=
\langle
\mathsf{id},
\mathsf{type},
\mathsf{payload},
\mathsf{refs},
\mathsf{certRefs},
\Delta\mathsf{Debt},
\nu,
\mathsf{provenance}
\rangle.
$$

Ledger append-only：

$$
\boxed{
L_\nu\subseteq L_{\nu+1}.
}
$$

錯誤不覆寫，而新增 `CORRECTION` / `SUPERSEDE` event。

---

# 3. Runtime State and Native State Hash

每個 native state 必 canonical serialize：

$$
h_\nu
=
\mathsf{Hash}
(
\mathsf{CanonicalSerialize}(\mathsf{State}_\nu)
).
$$

canonical serialization 至少要求：

- deterministic field ordering；
- UTF-8；
- stable IDs；
- explicit null；
- schema version；
- deterministic scalar normalization。

state hash 是一致性工具，不是 mathematical truth score。

---

# 4. Runtime Registries

Runtime 至少有六個 registry：

1. `ObjectRegistry`
2. `CertificateRegistry`
3. `DebtRegistry`
4. `PolicyRegistry`
5. `SnapshotRegistry`
6. `SchemaRegistry`

它們不得塌縮成單一 record，因為 object identity、proof authority、unresolved obligation、policy 與 materialization version 是不同語義。

---

# 5. Object Registry

Object record 最低欄位：

```yaml
object:
  object_id:
  object_type:
  domain_id:
  scope_id:
  representation_id:
  version:
  aliases: []
  provenance_refs: []
```

Stable ID 不得依 filename、visual position、parser order 或 temporary DB row id。

---

# 6. Certificate Registry

```yaml
certificate:
  certificate_id:
  certificate_type:
  subject_ids: []
  scope_id:
  assumption_ids: []
  evidence_refs: []
  verifier_results: []
  version:
  status:
```

status：

`VALID | STALE | REVOKED | PENDING | FAILED`

證書失效不刪除歷史。

---

# 7. Debt Registry

```yaml
debt:
  debt_id:
  debt_type:
  subject_id:
  cause:
  scope_id:
  discharge_requirements: []
  dependency_ids: []
  version:
  status:
```

status：

`OPEN | PARTIAL | DISCHARGED | SUPERSEDED`

核心不變量：

$$
\boxed{
\text{Debt cannot disappear without a discharge event.}
}
$$

---

# 8. Status Record

status 不是自由覆寫欄位，而是 versioned record：

```yaml
status_record:
  object_id:
  status:
  environment_id:
  certificate_ids: []
  debt_ids: []
  event_id:
  valid_from:
  valid_to:
```

因此：

$$
\mathsf{BLOCKED}
\to
\mathsf{REOPENED}
$$

不會刪掉原本的 blocked history。

---

# 9. Candidate Layer

所有非 deterministic / heuristic ingestion，例如自然語言 parsing、LLM extraction、embedding cluster，都先進：

$$
\boxed{
\mathsf{CandidateStore}.
}
$$

Candidate record：

```yaml
candidate:
  candidate_id:
  source_ref:
  extracted_type:
  text_span:
  proposed_object:
  confidence:
  parser_version:
```

核心 firewall：

$$
\boxed{
\mathsf{Candidate}
\not\Rightarrow
\mathsf{NativeObject}.
}
$$

---

# 10. Candidate-to-Native Promotion

Candidate 只有經：

$$
\mathsf{Extract}
\to
\mathsf{Normalize}
\to
\mathsf{Validate}
$$

並取得相應 certificate 後，才能進 native layer。

因此 LLM extraction 可以 non-deterministic；Native Closure Layer 的 mutation 不可以靠未驗證自然語言直接決定。

---

# 11. Closure Transaction

transaction：

```yaml
closure_transaction:
  txn_id:
  input_state_hash:
  policy_id:
  operator_plan: []
  precheck_results: {}
  operator_instances: []
  certificate_ids: []
  debt_delta:
  graph_delta:
  status_delta:
  output_state_hash:
  commit_status:
```

---

# 12. Transaction State Machine

$$
\boxed{
\mathsf{IDLE}
\to
\mathsf{PLANNED}
\to
\mathsf{PREFLIGHT}
\to
\mathsf{EXECUTING}
\to
\mathsf{COMMITTING}
\to
\mathsf{COMMITTED}
}
$$

任一 critical gate 失敗：

$$
\to
\mathsf{ABORTED}.
$$

---

# 13. Atomicity

Theorem-level mutation 必須 atomic：

$$
\boxed{
\mathsf{COMMIT}
\vee
\mathsf{ABORT}.
}
$$

禁止 partial native mutation。

---

# 14. Preflight

Preflight 必檢查：

- input state hash；
- object existence；
- version freshness；
- operator composition；
- scope compatibility；
- certificate validity；
- debt compatibility；
- authority boundary；
- expected output types。

---

# 15. Stale Transaction

若 transaction 建立後 native head 已變：

$$
\boxed{
\mathsf{STALE\_TXN}.
}
$$

不得 blind commit。

---

# 16. Deterministic Commit

在固定：

- input state hash；
- operator versions；
- policy version；
- certificate results；

下，相同 transaction 必得到相同 output hash。

---

# 17. Replay

$$
\boxed{
\widehat{\mathsf{State}}_\nu
=
\mathsf{Replay}
(
L_{\le\nu},
P_\nu
).
}
$$

Replay 驗證：

$$
\boxed{
\mathsf{Hash}
(
\widehat{\mathsf{State}}_\nu
)
=
h_\nu.
}
$$

不相等時：

$$
\mathsf{RUNTIME\_INCONSISTENT}.
$$

並 fail closed。

---

# 18. Snapshot

Snapshot 可加速恢復，但不是 canonical source：

```yaml
snapshot:
  state_version:
  state_hash:
  ledger_head:
  policy_version:
  schema_version:
  artifact_refs: []
```

restore 後必 replay-check。

---

# 19. Query Model

Query：

$$
\mathsf{Query}:
(\mathsf{State},q)
\to
\mathsf{QueryResult}.
$$

Result 不能只有 boolean：

$$
\boxed{
\mathsf{QueryResult}
=
\langle
\mathsf{Answer},
\mathsf{Authority},
\mathsf{Scope},
\mathsf{CertRefs},
\mathsf{DebtRefs},
\mathsf{Version},
\mathsf{SourceLayer}
\rangle.
}
$$

---

# 20. Query Family v0.1

最低支援：

- `status(object)`
- `why_blocked(route)`
- `why_closed(claim)`
- `frontier(target)`
- `applicable_obstructions(route)`
- `uncovered_routes(target)`
- `debt(object)`
- `history(object)`
- `transferability(a,b)`
- `diff(v1,v2)`
- `replay(version)`

---

# 21. Query Authority

若 query source 是 projected view：

$$
\mathsf{Authority}(result)
\le
\mathsf{Authority}(view).
$$

DISPLAY view 不得回答 proof-authority query。

---

# 22. Why-Blocked

`why_blocked` 至少回傳：

- applicable obstruction；
- OPCert；
- scope；
- assumptions；
- cert refs；
- active debt；
- version。

因此 runtime 不只回「被封了」，而回答「誰、在什麼條件下、用什麼證書封的」。

---

# 23. Frontier Engine

輸入：

- native graph；
- status map；
- quotient policy；
- target；
- route grammar。

輸出：

$$
\partial^\ast_{D,\Gamma,\rho,\nu}\mathfrak C(Q).
$$

若 route completeness 尚未證，必附 `RouteCompletenessDebt`。

---

# 24. Cut / Cover Engines

Graph algorithm 只能產生：

$$
\mathsf{CutCandidate},
\qquad
\mathsf{CoverCandidate}.
$$

不能直接生成 theorem-level：

$$
\mathsf{CutCert},
\qquad
\mathsf{CoverCert}.
$$

這是 Candidate-to-Native firewall 在 graph mining 上的具體實現。

---

# 25. Exhaustion Engine

只有：

- RCCert；
- CutCert；
- CoverCert；
- scope fidelity；
- parent bridge；

符合 Paper 03 條件時，才能產生 RECert。

輸出仍必標：

$$
\mathsf{EXH}_{k}^{D,\Gamma,\nu}.
$$

不得冒充 absolute exhaustion。

---

# 26. Projection Engine

Projection output：

```yaml
projection_artifact:
  artifact_id:
  native_state_id:
  native_state_hash:
  projection_policy:
  preserved_invariants: []
  projection_debt_ids: []
  authority:
  version:
  status:
```

Native reopening / revision 發生後，相依 view：

$$
\mathsf{VALID}
\to
\mathsf{STALE}.
$$

---

# 27. Verifier Interface

```yaml
verifier:
  verifier_id:
  accepted_certificate_types: []
  version:
  deterministic:
  trust_policy:
```

Verifier result：

```yaml
verification_result:
  certificate_id:
  verifier_id:
  result:
  evidence_refs: []
  verifier_version:
```

若 verifier 結果衝突：

$$
\mathsf{CERT\_CONFLICT}
$$

theorem-level mutation必 DEFER / REFUSE。

---

# 28. Runtime Exec Result

$$
\boxed{
\mathsf{ExecResult}
\in
\{
\mathsf{PASS},
\mathsf{REFUSE},
\mathsf{DEFER},
\mathsf{UNKNOWN},
\mathsf{ERROR}
\}.
}
$$

`PASS_runtime` 不等於 theorem proven；它只代表 operation 符合 runtime semantics。

---

# 29. Fail-Closed Semantics

critical precondition FAIL：

$$
\boxed{
\mathsf{REFUSE}.
}
$$

資訊不足：

$$
\mathsf{DEFER}
$$

並新增 debt。

未分類：

$$
\mathsf{UNKNOWN}.
$$

runtime/schema bug：

$$
\mathsf{ERROR}.
$$

ERROR 不得被誤當 mathematical status。

---

# 30. Crash Recovery

Transaction recovery 至少分類：

- `NOT_STARTED`
- `PREPARED`
- `COMMITTED`
- `COMMIT_STATE_UNKNOWN`

不確定時以 ledger head 為基準重建；禁止 blind recommit。

---

# 31. Idempotency

每個 mutation transaction 應有 stable idempotency key。

同一 committed txn 不得重複產生 theorem mutation。

---

# 32. Runtime Safety Invariants

$$
\boxed{
\begin{aligned}
&\text{No theorem mutation without cert path};\\
&\text{No debt disappearance without discharge};\\
&\text{No reopening history erasure};\\
&\text{No projected-view native mutation};\\
&\text{Replay must reconstruct native state};\\
&\text{No candidate-to-theorem direct jump};\\
&\text{No cross-domain authority without transfer cert};\\
&\text{No silent version mismatch composition}.
\end{aligned}
}
$$

---

# 33. NS Ingestion Profile v0.1

第一個大型實例：

$$
\boxed{
\mathsf{NSProfile}_{v0.1}.
}
$$

預期來源：

- ETN--X Integration；
- C1；
- C2；
- C3--C6；
- X72；
- DCRP；
- RFP；
- MORP；
- FCBP；
- Proof Asset Map；
- validation scripts。

---

# 34. NS Artifact Record

```yaml
ns_artifact:
  artifact_id:
  source_ref:
  series:
  round:
  title:
  date:
  source_hash:
  parser_version:
```

---

# 35. NS Claim Candidate

```yaml
ns_claim_candidate:
  candidate_id:
  artifact_id:
  text_span:
  normalized_statement:
  claim_type:
  explicit_status_label:
  assumptions: []
  scope:
  dependencies: []
  evidence_refs: []
```

---

# 36. NS Status Labels Are Hints

原始：

`CLOSED | OPEN | NO-GO | SURVIVOR | STOP | CONDITIONAL`

只能解析成：

- `StatusCandidate`
- `OpenClaimCandidate`
- `ObstructionCandidate`
- `RouteStateCandidate`
- `FrontierCandidate`
- `ConditionalCandidate`

不能直接 mutate native status。

---

# 37. NS Operator Planning

例如 `NO-GO`：

$$
\mathsf{Extract}
\to
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{Block?}
$$

不是：

$$
\mathsf{Refute}.
$$

`CLOSED` 可能最後被判為：

- `Prove`
- `Condition`
- `Block`
- `UNVERIFIED`

依 actual evidence 決定。

---

# 38. NS Seed Dataset

第一版 seed 建議先用：

1. ETN--X Integration；
2. C1；
3. C2；
4. C6-Q；
5. DCRP103；
6. DCRP104；
7. DCRP105。

原因是這組同時具有：

- CLOSED；
- OPEN；
- NO-GO；
- survivor；
- STOP；
- cross-series / cross-stage semantics；
- validation scripts。

足以測試 compiler，而不用一開始吞整個 corpus。

---

# 39. NS Native Graph v0.1

第一版只宣稱：

$$
\boxed{
\mathfrak C_{\rm NS,obs}^{\rm nat,v0.1}
}
$$

即 observed-relative graph。

不宣稱：

$$
\Omega_{\rm NS}^{\rm math}.
$$

---

# 40. NS Frontier v0.1

輸出：

$$
\boxed{
\partial_{\rm NS,obs}^{\ast,v0.1}.
}
$$

任何 route completeness 未證部分都進 debt registry。

---

# 41. Runtime Conformance Suite

CSM Runtime v0.1 必有 conformance suite。

最小 12 vectors：

1. diagnostic obstruction；
2. counterexample；
3. proof + unmet assumption；
4. debt discharge；
5. projected-view mutation refusal；
6. lossy transfer；
7. reopening wave；
8. false quotient split；
9. deterministic replay；
10. stale transaction；
11. NS `NO-GO` candidate；
12. NS `CLOSED` without cert。

---

# 42. Conformance Vector — Deterministic Replay

同 ledger + 同 policy replay 兩次：

$$
h_1=h_2.
$$

---

# 43. Conformance Vector — Block Is Not Refute

route OPEN + valid obstruction：

$$
\mathsf{OPEN}
\to
\mathsf{BLOCKED}.
$$

Parent claim 不變。

---

# 44. Conformance Vector — Conditional

proof cert 有效但 assumption 未償：

$$
\sigma(Q)=\mathsf{CONDITIONAL}.
$$

---

# 45. Conformance Vector — Debt Discharge

debt discharge 後：

$$
\mathsf{CONDITIONAL}
\to
\mathsf{CLOSED}^{+}
$$

若其它 cert 全 valid。

---

# 46. Conformance Vector — Reopening

共用 premise 被 invalidated：

- downstream certs -> STALE；
- routes -> REOPENED / audit；
- frontier rebuild。

---

# 47. Conformance Vector — NS NO-GO

文件標 `NO-GO`：

Expected：

`ObstructionCandidate`

而不是：

`CLOSED_NEGATIVE`.

---

# 48. Conformance Vector — NS CLOSED

文件標 `CLOSED` 但沒有 proof cert：

Expected：

`StatusCandidate / UNVERIFIED`.

---

# 49. Reference Runtime Module Layout

```text
csm_runtime/
  model/
  schema/
  registry/
  ledger/
  operators/
  transaction/
  replay/
  frontier/
  query/
  projection/
  transfer/
  compiler/
    ns/
  conformance/
```

---

# 50. MVP Boundary

CSM Reference Runtime v0.1 **不需要**：

- LLM；
- theorem prover；
- GUI；
- web service；
- distributed database。

它只需要：

$$
\boxed{
\text{deterministic semantics}
+
\text{registries}
+
\text{ledger}
+
\text{PCOs}
+
\text{transaction}
+
\text{replay}
+
\text{query}
+
\text{conformance}.
}
$$

---

# 51. Runtime Nonclaims

本文不主張：

1. runtime 可自動證明所有 theorem；
2. graph completeness 可自動決定；
3. LLM extraction 等於 formal verification；
4. state hash 等於 truth；
5. deterministic replay 解決 semantic ambiguity；
6. NS ingestion 完成即等於 Clay proof；
7. candidate cut 等於 theorem cut；
8. observed frontier 等於 absolute frontier。

---

# 52. 核心命題

## 52.1 Ledger Reconstruction Principle

固定 ledger、policy、schema、operator versions：

$$
\boxed{
\mathsf{Replay}
\text{ must reconstruct the native state deterministically}.
}
$$

## 52.2 Transactional Closure Principle

theorem-level mutation：

$$
\boxed{
\text{atomic commit or abort}.
}
$$

## 52.3 Registry Separation Principle

Object、Cert、Debt、Policy、Snapshot 不得語義塌縮。

## 52.4 Query Authority Principle

任何 query result 必帶 authority / scope / cert / debt / version / source layer。

## 52.5 Candidate Isolation Principle

heuristic extraction 只能進 Candidate Layer。

## 52.6 NS Safe-Ingestion Principle

NS 的自然語言 status label 只作 hints；closure status 必由 runtime calculus 重建。

---

# 53. 下一階段

Paper 09 應回到第一個大型實例：

$$
\boxed{
\textbf{NS Relative-Global Closure Graph:
Canonical Domain Model and Ingestion Specification}
}
$$

Paper 09 不再新增通用 CSM 基礎，而開始定義：

- NS target objects；
- formal / generalized / physical domain graph；
- series ontology；
- route family taxonomy；
- obstruction taxonomy；
- survivor taxonomy；
- artifact inventory schema；
- seed ingestion order；
- cross-series bridges；
- canonical graph construction plan。

---

# 54. 結論

Paper 08 使 CSM 從 closure calculus 進入 machine semantics。

現在整個系統已經具有：

$$
\boxed{
\text{State}
+
\text{Events}
+
\text{Operators}
+
\text{Transactions}
+
\text{Registries}
+
\text{Replay}
+
\text{Queries}
+
\text{Conformance}.
}
$$

最重要的 runtime boundary 是：

$$
\boxed{
\text{Candidate uncertainty outside;
deterministic closure authority inside}.
}
$$

以及：

$$
\boxed{
\text{No certificate path}
\Rightarrow
\text{No native theorem mutation}.
}
$$

因此未來 NS corpus 進入系統時，不再是「把幾百篇文章塞進 graph」，而是把每一篇 artifact 編譯成 candidate events，再逐步通過 validation、operator transaction、replay 與 frontier rebuild，形成真正可稽核的 observed-relative closure state。

---

## 附錄 A — Paper 08 核心不變量

1. ledger append-only；
2. native state replayable；
3. theorem mutation atomic；
4. candidate layer 無 theorem authority；
5. debt 無 discharge 不消失；
6. cert revoke/stale 不刪歷史；
7. projected view 不得 native mutate；
8. replay mismatch fail closed；
9. operator/schema/policy 全部 versioned；
10. NS status labels 只作 candidate hints；
11. query 必帶 authority metadata；
12. observed NS graph 不冒充 absolute proof space。

---

**END OF CSM PAPER 08 v0.1**
