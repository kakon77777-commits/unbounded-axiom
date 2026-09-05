# GCM Reference Runtime Architecture
## Global Computation Methodology 參考 Runtime 架構、模組邊界、交易語義與 MVP 部署輪廓 v0.1

**文件類型：** Technical Whitepaper / Reference Runtime Architecture  
**系列：** Global Computation Methodology（GCM）  
**版本：** v0.1  
**日期：** 2026-08-24  
**Canonical source format：** UTF-8 Markdown  
**數學 delimiter：** ` $...$ ` 與 `$$...$$`  
**狀態：** 第二輪正式工程架構；直接上游為 TW-01 v0.1

---

## 摘要

TW-01 已將 GCM Series-00 與 Paper-01–06 的核心理論抽成 normative contract，固定 World、Runtime、Observer、Foundation、History 的型別邊界，並要求 Runtime 依序處理 Addressability、Reachability、Admissibility、Authority、Execution、Reconciliation、Verification 與 Commit。若沒有更進一步的參考架構，實作者仍可能在模組切分、儲存責任、交易生命週期與外掛權限上做出互相不相容的選擇。

本文件因此回答：

> **一套可被實作、測試與替換元件的 GCM Reference Runtime，最低限度應如何拆分模組、配置資料所有權、傳遞 typed contracts，並保證任何 local executor、AI router、bridge、observer 或 lifecycle manager 都不能越過 canonical commit 與 Foundation revision 邊界？**

本文件的核心架構約束是：

$$
\boxed{
\text{Ordinary World Mutation}
\Rightarrow
\text{Commit Gate Only}
}
$$

$$
\boxed{
\text{Foundation Mutation}
\Rightarrow
\text{Explicit Revision Path Only}
}
$$

以及：

$$
\boxed{
\text{Executor}
\neq
\text{World Writer}
}
$$

$$
\boxed{
\text{Router}
\neq
\text{Authority Grantor}
}
$$

$$
\boxed{
\text{Observer}
\neq
\text{Implicit Intervenor}
}
$$

$$
\boxed{
\text{Materialization Store}
\neq
\text{Canonical World Store}
}
$$

$$
\boxed{
\text{Telemetry}
\neq
\text{Canonical History}
}
$$

這些並非要求某一特定程式語言、資料庫、scheduler 或 distributed consensus protocol。TW-02 定義的是 **logical architecture、ownership、transaction boundary、extension boundary 與 failure semantics**。具體 implementation MAY 採單程序、multi-process、cluster 或 heterogeneous accelerator，但 MUST 保存相同語義邊界。

---

# 0. 文件角色與規範優先級

TW-02 的直接上游為：

$$
\boxed{
\text{TW-01 v0.1}
}
$$

本文件 SHOULD 與 TW-01 一致。若 TW-02 的架構建議與 TW-01 的 MUST / MUST NOT 條款衝突，**以 TW-01 為準**。

TW-02 的責任是：

1. 將 TW-01 contract 映射為 logical modules；
2. 固定 state store ownership；
3. 固定 ordinary operation pipeline；
4. 固定 pre-execution 與 pre-commit gate；
5. 固定 proposal isolation；
6. 固定 reconciliation / verification / commit 邊界；
7. 固定 Observer / materialization read-side；
8. 固定 active-support / lifecycle resource plane；
9. 固定 typed history / provenance write path；
10. 固定 Foundation revision path；
11. 定義 reference extension/plugin model；
12. 定義 reference deployment profiles；
13. 定義 MVP M0–M4 架構切片；
14. 提供 machine-readable schema 與 module ownership manifest。

本文件不指定：

- 唯一程式語言；
- 唯一 RPC / IPC transport；
- 唯一 database engine；
- 唯一 consensus algorithm；
- 唯一 scheduler；
- 唯一 AI planner；
- 唯一 optimization objective；
- 唯一 World ontology；
- 所有 24／72 basis cells 的實作。

---

# 1. Reference Architecture 的設計原則

## 1.1 Semantic boundary before performance

Reference Runtime MUST 先保持語義邊界，再進行 optimization：

$$
\boxed{
\text{Correct Typed Boundary}
\rightarrow
\text{Optimization}
}
$$

而不是：

$$
\text{Optimization}
\rightarrow
\text{Retrospective Legality Guessing}.
$$

## 1.2 One ordinary writer for canonical World

對每一個 declared World boundary $B_W$，ordinary Runtime SHOULD 有唯一 logical commit authority：

$$
\boxed{
\mathsf{CommitGate}_{B_W}
}
$$

只有 Commit Gate 可以把 candidate world-state 提升為新的 canonical committed state：

$$
\widetilde W_{\nu+1}
\xrightarrow{\mathsf{CommitGate}}
W_{\nu+1}.
$$

Executor、Bridge、Router、AI planner、Observer、Projection Service、Materialization Manager、Lifecycle Manager MUST NOT 直接寫入 canonical World Store。

「唯一 logical writer」不等於「只能有一個 OS process」。Distributed implementation MAY 使用 replicated state machine、partitioned coordinator、single-writer lease、transaction coordinator 或其他方法，只要能證明其外部語義等價於唯一 commit boundary。

## 1.3 Foundation uses a separate revision authority

Foundation revision 不走 ordinary Commit Gate：

$$
\boxed{
\mathsf{ReviseFoundation}:
\mathcal F^{(v)}
\rightarrow
\mathcal F^{(v+1)}
}
$$

應由：

$$
\boxed{
\mathsf{FoundationRevisionGateway}
}
$$

執行 explicit governance path。

因此：

$$
\boxed{
\mathsf{CommitGate}
\neq
\mathsf{FoundationRevisionGateway}.
}
$$

## 1.4 Read-side mutation is typed separately

Pure observation MAY 更新 Runtime cache、materialization、Observer state：

$$
\Delta \Xi\neq 0,
\qquad
\Delta O\neq 0,
$$

但 MUST 保持：

$$
\boxed{
\Delta W=0.
}
$$

## 1.5 Global coherence does not imply one global barrier

Reference Runtime MUST NOT 把 globality 簡化成每一步都需要 world-wide synchronization：

$$
\boxed{
\text{Global Coherence}
\not\Rightarrow
\text{Global Barrier}.
}
$$

可並行執行的 proposal SHOULD 被允許並行；只有在 overlap、noncommutativity、shared invariant 或 commit serialization 需要時才建立 ordering obligation。

## 1.6 Semantic authority is not OS isolation

GCM Authority 是 semantic contract：

$$
\mathsf{AuthProfile}(A).
$$

但：

$$
\boxed{
\text{Semantic Authority Enforcement}
\neq
\text{Operating-System Isolation}.
}
$$

若 executor / plugin 被視為 adversarial 或不可信，production deployment SHOULD 另加 process isolation、sandbox、container、VM、capability security 或其他安全邊界。TW-02 不以 semantic contract 取代 cyber-security engineering。

---

# 2. 整體 Logical Architecture

Reference Runtime 分為六個 logical planes：

$$
\boxed{
\mathfrak R_{\text{GCM}}
=
\mathfrak P_C
\cup
\mathfrak P_X
\cup
\mathfrak P_R
\cup
\mathfrak P_O
\cup
\mathfrak P_L
\cup
\mathfrak P_H
}
$$

其中：

- $\mathfrak P_C$：Canonical / Governance Plane；
- $\mathfrak P_X$：Execution / Transaction Plane；
- $\mathfrak P_R$：Routing / Resource Plane；
- $\mathfrak P_O$：Observer / Materialization Plane；
- $\mathfrak P_L$：Lifecycle / Active-Support Plane；
- $\mathfrak P_H$：History / Provenance Plane。

Reference module topology：

```text
                         ┌─────────────────────────────┐
                         │ Specification / Schema     │
                         │ Registry                   │
                         └──────────────┬──────────────┘
                                        │
        ┌───────────────────────────────┼────────────────────────────────┐
        │                               │                                │
┌───────▼────────┐             ┌────────▼─────────┐             ┌────────▼─────────┐
│ Foundation     │             │ Configuration    │             │ Domain Registry │
│ Registry       │             │ Registry         │             └────────┬─────────┘
└───────┬────────┘             └────────┬─────────┘                      │
        │                               │                                │
        └───────────────────────────────┼────────────────────────────────┘
                                        │
                              Operation Gateway
                                        │
                              Type / Scope Resolve
                                        │
                            Candidate Route Planner
                                        │
       ┌────────────────────────────────┼────────────────────────────────┐
       │                                │                                │
 Reachability /                  Admissibility                    Authority Engine
 Resource Engine                    Validator                           │
       │                                │                                │
       └────────────────────────────────┼────────────────────────────────┘
                                        │
                         Executor / Bridge Contract Gate
                                        │
                              Safe Route Selector
                                        │
                             Executor Host(s)
                                        │
                                Proposal Store
                                        │
                             Reconciliation Engine
                                        │
                              Verification Engine
                                        │
                                Commit Gate
                                        │
                                  World Store
                                        │
             ┌──────────────────────────┼──────────────────────────┐
             │                          │                          │
   Observer / Projection      Active Support / Lifecycle   History / Provenance
          Service                    Manager                     Store
             │                          │                          │
   Materialization Store        Archive / Restore          History Index / Replay
```

圖中資料流不是唯一 deployment topology；它描述的是 logical authority boundary。

---

# 3. Canonical State Ownership

Reference Runtime MUST 對六種核心 state roles 建立明確 owner：

| State role | Canonical notation | Logical owner | Ordinary direct writers |
|---|---|---|---|
| World primitive | $\mathbf W$ | external/world ontology boundary | none in Runtime |
| committed executable World state | $W_\nu$ | World Store + Commit Gate | Commit Gate only |
| Runtime control state | $\Xi_\mu$ | Runtime State Store | typed Runtime managers |
| Observer state | $O_\omega$ | Observer State Store | Observer Service |
| Foundation | $\mathcal F^{(v)}$ | Foundation Registry | Foundation Revision Gateway only |
| History / provenance | $\mathcal H_\eta$ | History Store | History Writer / certified transform path |

這個 ownership table 是 architecture-level invariant。

## 3.1 World Store

World Store 保存 **committed canonical executable World-state presentation**。實作 MAY 使用：

- immutable snapshot；
- delta chain；
- MVCC-style version graph；
- event-derived state cache；
- content-addressed chunks；
- hybrid snapshot + delta。

但 MUST 支援至少：

```text
read_world(boundary_ref, version_ref)
read_head(boundary_ref)
prepare_candidate(parent_version, candidate_ref)
commit_candidate(expected_parent, candidate_ref, verification_ref, authority_ref)
inspect_commit_lineage(version_ref)
```

World Store MUST NOT 提供給 ordinary executor 一個可繞過 Commit Gate 的 unrestricted `put_world(...)`。

## 3.2 Runtime State Store

 $\Xi_\mu$ SHOULD 保存：

- route cache；
- resource snapshot；
- scheduler state；
- active support；
- pinning state；
- materialization index；
- bridge cache；
- pending proposal metadata；
- retry / backoff metadata；
- local runtime health state。

 $\Xi_\mu$ 的改變 MUST NOT 被自動解讀為 $W_\nu$ 的改變。

## 3.3 Observer State Store

 $O_\omega$ SHOULD 保存：

- focus；
- viewport；
- projection parameters；
- requested observer resolution；
- history window；
- filter / query context；
- presentation state。

Observer State Store 不得直接提交 World mutation。

## 3.4 Foundation Registry

Foundation Registry MUST 把 Foundation version 視為 immutable object：

$$
\boxed{
\mathcal F^{(v)}
\text{ immutable after publication}
}
$$

新 Foundation 必須生成新版本：

$$
\mathcal F^{(v+1)}.
$$

Registry SHOULD 保存：

- semantic identifier；
- content digest；
- parent Foundation version；
- revision rationale；
- governance evidence；
- migration requirements；
- affected World boundaries；
- effective status。

## 3.5 History Store

History Store SHOULD 採 append-oriented semantics。它 MAY 分層儲存 raw receipt、indexed summary、checkpoint、compacted segment，但任何 destructive transform MUST 受 history transformation contract 約束。

---

# 4. Stable Identifiers 與 Version References

Reference Runtime SHOULD 使用語義穩定、不可與 human-readable label 混同的 identifiers。

最低識別類型：

```text
SpecVersionRef
SchemaVersionRef
WorldBoundaryRef
WorldVersionRef
RuntimeRevisionRef
ObserverRevisionRef
FoundationRef
HistoryRevisionRef
ConfigurationRef
DomainRef
OperationId
RouteId
ExecutorRef
BridgeRef
ProposalId
VerificationId
CommitId
EventId
ArchiveAnchorId
MaterializationId
```

Reference object SHOULD 帶：

- `id`；
- `schema_version`；
- `semantic_type`；
- `created_at` 或 logical creation marker when applicable；
- source / parent references；
- content digest when persistence requires integrity checking。

Wall-clock timestamp MAY 是 metadata，但 MUST NOT 被用來偷代替 causal / commit / history relation。

---

# 5. Operation Envelope 與 Frozen Execution Context

任何 ordinary operation 在進入 route planning 前 SHOULD 形成 immutable-ish execution context：

$$
\boxed{
\mathfrak X_\kappa
=
\left\langle
\boldsymbol\omega,
B_W,
\mathcal F^{(v)},
W_\nu,
\Xi_\mu,
O_\omega,
\mathsf{AuthCtx},
\mathsf{Budget},
\mathsf{SchemaRefs}
\right\rangle.
}
$$

其中：

- $\boldsymbol\omega$：typed operation request；
- $B_W$：declared World boundary；
- $\mathcal F^{(v)}$：pinned Foundation；
- $W_\nu$：planning snapshot；
- $\Xi_\mu$：Runtime-control snapshot/reference；
- $O_\omega$：Observer context when relevant；
- $\mathsf{AuthCtx}$：requester / delegation / scope authority；
- $\mathsf{Budget}$：resource / cost constraints；
- $\mathsf{SchemaRefs}$：spec/config/contract schema versions。

形成 $\mathfrak X_\kappa$ 的目的，是避免同一次 route lifecycle 在不同 gate 偷換 Foundation、World parent、authority 或 schema。

若 pinned reference 於 commit 前失效，Runtime MUST 進入 explicit stale / revalidation path，而不是 silent upgrade。

---

# 6. Operation Gateway

Operation Gateway 是 external request 進入 ordinary Runtime 的第一個 logical boundary。

責任：

1. parse request；
2. resolve operation schema；
3. assign `OperationId`；
4. resolve World boundary；
5. resolve requester / agent context；
6. reject untyped operation；
7. build initial execution context；
8. emit request receipt。

Untyped request：

$$
\boxed{
\mathsf{type}(\boldsymbol\omega)=\varnothing
\Rightarrow
\mathsf{Refuse}\lor\mathsf{Defer}
}
$$

MUST NOT 直接呼叫 executor。

---

# 7. Domain Registry

Domain Registry 保存 Runtime-facing domain definitions，而不假設 Domain 等同物理空間。

最低 record SHOULD 包含：

- `domain_id`；
- parent / child domain refs；
- World boundary binding；
- state slice / selector contract；
- configuration binding；
- invariant refs；
- optional spatial binding；
- optional temporal contract；
- active-support metadata；
- authority scope metadata。

因此：

$$
\boxed{
D_i
\not\Rightarrow
U_i\subseteq\mathcal M_{ST}.
}
$$

Spatial / temporal coordinates 若存在，應透過 explicit binding contract 加入。

---

# 8. Configuration Registry

Configuration Registry 實作 Paper-02 / TW-01 的 versioned configuration basis。

責任：

- register basis schema；
- register basis cell address；
- register composite profile；
- register full Runtime configuration；
- resolve canonical address；
- query compatible executor families；
- project compatibility across versions；
- reject unknown / lossy projection when contract requires losslessness；
- record domain configuration switches。

Registry MUST 保持：

$$
\boxed{
\text{Basis Cell}
\neq
\text{Executor}.
}
$$

以及：

$$
\boxed{
\text{Same Cell}
\not\Rightarrow
\text{Same Semantics}.
}
$$

---

# 9. Reachability / Resource Engine

Reachability Engine 回答：

> **在目前 Runtime state、resource、service、bridge、network、device 與 model availability 下，候選 route 是否實際可被調用？**

它不回答「是否允許」。

輸入：

$$
(A,\boldsymbol\omega,\boldsymbol\zeta,\Xi_\mu,\mathsf{ResourceSnapshot}).
$$

輸出：

$$
\mathsf{ReachabilityResult}
=
\left\langle
\mathsf{reachable},
\mathsf{missing},
\mathsf{costEstimate},
\mathsf{freshness},
\mathsf{evidence}
\right\rangle.
$$

Engine SHOULD 對 live resource snapshot 建立 freshness metadata。若 resource information 過期到足以影響安全或可執行性，應回傳 unknown / defer，而不是 false certainty。

---

# 10. Admissibility Validator

Admissibility Validator 是 deterministic / auditable correctness gate 的核心。

它 SHOULD 評估至少：

- type compatibility；
- World boundary scope；
- domain legality；
- transition-law legality；
- Foundation compatibility；
- invariant preconditions；
- effect boundary；
- bridge preconditions；
- representation loss constraints；
- temporal/order contract；
- resource hard constraints when these are semantic requirements。

輸出：

$$
\boxed{
\mathsf{AdmResult}
\in
\{\mathsf{Pass},\mathsf{Fail},\mathsf{Unknown}\}.
}
$$

`Unknown` MUST NOT 被自動提升成 `Pass`。

Validator MAY 使用 SMT、proof assistant、schema checker、domain-specific verifier、rule engine 或 procedural validator；GCM 不指定唯一方法。

---

# 11. Authority Engine

Authority Engine 回答：

> **指定 agent / requester 在指定 scope 上，是否擁有 operation 所要求的 authority？**

Authority Engine SHOULD 是 route planner 的外部 gate，而不是 planner 的內部權重。

它 MUST 保持：

$$
\boxed{
\mathsf{AuthOut}
\preceq
\mathsf{AuthIn}
\oplus
\mathsf{ExplicitDelegation}.
}
$$

Reference Engine SHOULD 支援：

- authority class；
- scope；
- delegation chain；
- expiry / revocation when deployment需要；
- commit authority 與 execution authority 分離；
- Foundation authority 獨立分類。

若 authority 可被撤銷，Commit Gate SHOULD 在 commit 前重新檢查 commit-sensitive authority，避免典型 time-of-check / time-of-use drift。

---

# 12. Route Planner / Selector

Route Planner 可使用 deterministic search、heuristic、optimizer、AI planner 或混合方法。

其責任只是生成候選：

$$
\mathcal Z
=
\{\boldsymbol\zeta_1,\ldots,\boldsymbol\zeta_n\}.
$$

Planner MUST NOT：

- 自己授權；
- 自己修改 Foundation；
- 自己把 unknown bridge 視為 safe；
- 直接執行 candidate；
- 直接 commit World；
- 因 optimization score 高就繞過 gate。

安全 candidate set：

$$
\boxed{
\mathcal Z_{\mathrm{safe}}
=
\{\boldsymbol\zeta\in\mathcal Z
\mid
\mathsf{PreExecOK}(\boldsymbol\zeta)=1\}.
}
$$

Optimization 只允許在 $\mathcal Z_{\mathrm{safe}}$ 內：

$$
\boldsymbol\zeta^*
=
\arg\min_{\boldsymbol\zeta\in\mathcal Z_{\mathrm{safe}}}
J(\boldsymbol\zeta),
$$

其中 $J$ 可以是多目標 policy，且：

$$
\boxed{
J
\neq
\text{Mathematics itself}.
}
$$

AI Route Proposal MUST 被視為 proposal source，而不是 governance source。

---

# 13. Executor Registry 與 Executor Host

Executor Registry 保存：

$$
\mathfrak E_i
=
\left\langle
\mathsf{id}_i,
\mathsf{Cap}_i,
\mathsf{In}_i,
\mathsf{Out}_i,
\mathsf{Pre}_i,
\mathsf{Eff}_i,
\mathsf{Inv}_i,
\mathsf{Res}_i,
\mathsf{Cost}_i,
\mathsf{Fail}_i,
\mathsf{Hist}_i
\right\rangle.
$$

每個 executor instance SHOULD 綁定：

- executor version；
- contract version；
- implementation digest when possible；
- supported configuration profiles；
- resource requirements；
- determinism / nondeterminism declaration；
- replay prerequisites；
- side-effect class；
- isolation mode。

Executor Host MUST 只向 executor 暴露：

- read-only World view / bounded state slice；
- Runtime-approved inputs；
- typed bridge outputs；
- proposal writer；
- allowed external capability handles。

Executor Host MUST NOT 暴露 unrestricted canonical World Store write handle。

Local execution：

$$
E_i
\left(
W_\nu\vert_{D_i},
\Xi_\mu,
\gamma_i,
\mathsf{input}
\right)
\rightarrow
\delta_i.
$$

其中 $\delta_i$ 是 immutable proposal artifact。

---

# 14. Bridge Registry 與 Bridge Host

Bridge Registry 保存：

$$
\mathfrak C^{\mathrm{Br}}_{p\rightarrow q}
=
\left\langle
S_p,
S_q,
\mathsf{Pre},
\mathsf{Post},
\mathsf{InvKeep},
\epsilon,
\mathsf{Rev},
\mathsf{Cost},
\mathsf{Fail}
\right\rangle.
$$

Bridge implementation SHOULD 綁定：

- source schema/version；
- target schema/version；
- loss semantics；
- error bound / unknown state；
- reversibility class；
- invariant preservation evidence；
- implementation version；
- test vector / validation status。

Reference architecture 將 bridge 視為 **semantic conversion boundary**，不是只是 serializer。

$$
\boxed{
\text{Serializable}
\not\Rightarrow
\text{Semantically Safe}.
}
$$

Unknown semantic loss SHOULD 產生：

```text
GCM_E_BRIDGE_UNKNOWN
```

而不是 best-effort silent cast。

---

# 15. Proposal Store

Proposal Store 是 executor 與 canonical commit 之間的隔離層。

Proposal SHOULD 是 immutable record：

$$
\boxed{
\delta_i
=
\left\langle
\mathsf{id},
\mathsf{operationRef},
\mathsf{routeRef},
\mathsf{parentWorldRef},
\mathsf{foundationRef},
\mathsf{readSet},
\mathsf{writeSet},
\mathsf{effects},
\mathsf{evidence},
\mathsf{cost},
\mathsf{executorRef},
\mathsf{replayMeta}
\right\rangle.
}
$$

Proposal Store MAY 是 durable 或 ephemeral；但若 operation 需要 audit、retry、replay、compensation 或 cross-domain reconciliation，SHOULD durable。

Proposal MUST 綁定 parent World version 與 Foundation version，避免「在舊世界算出的 proposal 被拿到新 Foundation 直接 commit」。

---

# 16. Reconciliation Engine

Reconciliation Engine 將多個 local proposals 合成 candidate World：

$$
\mathsf{Reconcile}_{B_W,\mathcal C}
:
(W_\nu,\Delta_\nu)
\rightharpoonup
\widetilde W_{\nu+1}.
$$

它 SHOULD 能處理：

- overlapping write sets；
- noncommutative effects；
- domain coupling；
- bridge-induced approximation；
- local invariant conflict；
- cross-domain constraints；
- declared merge operators；
- reject / defer when composition unknown。

定義 proposal footprint：

$$
\mathsf{Foot}(\delta_i)
=
\left\langle
\mathsf{readSet}_i,
\mathsf{writeSet}_i,
\mathsf{effectClass}_i
\right\rangle.
$$

若：

$$
\mathsf{Conflict}(\delta_a,\delta_b)=1,
$$

而沒有 certified reconciliation operator，Runtime MUST NOT 以 arbitrary last-write-wins 當成 general solution。

---

# 17. Verification Engine

Verification Engine 對 candidate World 與 commit obligations 做 final semantic check：

$$
\mathsf{Verify}^{(v)}_{B_W}
(W_\nu,\widetilde W_{\nu+1}).
$$

Verification SHOULD 產生 typed evidence：

$$
\boxed{
\mathsf{VerificationResult}
=
\left\langle
\mathsf{status},
\mathsf{checks},
\mathsf{invariants},
\mathsf{warnings},
\mathsf{evidenceRefs},
\mathsf{verifierRefs}
\right\rangle.
}
$$

對 hard invariant：

$$
\mathsf{Unknown}
\Rightarrow
\mathsf{NoCommit}
$$

除非 Foundation / policy 明確把該條件定義為 soft obligation。

---

# 18. Commit Gate

Commit Gate 是 ordinary World mutation 的唯一 logical authority boundary。

Commit 前 SHOULD 重新檢查至少：

1. expected parent World version；
2. pinned Foundation version；
3. verification result；
4. commit authority；
5. candidate schema compatibility；
6. required history / provenance evidence；
7. resource / side-effect finalization when relevant。

## 18.1 Optimistic parent check

若 operation 是基於 $W_\nu$ 計算：

$$
\mathsf{ExpectedParent}=W_\nu.
$$

Commit 時若 World head 已成為 $W_{\nu+k}$，Runtime MUST NOT blind commit。

應至少選一個：

- rebase and reverify；
- reconcile against new head；
- retry from new snapshot；
- Defer；
- Refuse if semantics cannot be preserved。

即：

$$
\boxed{
\text{Stale Parent}
\not\Rightarrow
\text{Implicit Rebase}.
}
$$

## 18.2 Commit record

成功 commit 應原子地或等價地建立：

- new WorldVersionRef；
- parent link；
- FoundationRef；
- proposal refs；
- verification ref；
- authority / requester evidence ref；
- commit receipt；
- history relation updates。

若儲存系統無法對 World write 與 receipt write 提供單一 ACID transaction，implementation MUST 透過 write-ahead intent、outbox、two-phase marker、recovery log 或其他方法證明 crash recovery 後不會形成「World 已改但永遠沒有 canonical commit receipt」的 silent split-brain state。

---

# 19. Rollback、Abort 與 Compensation

Reference architecture MUST 分離：

$$
\boxed{
\mathsf{Reject}
\neq
\mathsf{Abort}
\neq
\mathsf{Rollback}
\neq
\mathsf{Compensation}.
}
$$

- `Reject`：gate 不通過，未進入合法 execution；
- `Abort`：execution / proposal path 中止；
- `Rollback`：未提交 candidate / transaction 恢復；
- `Compensation`：已 commit effect 之後，以新 operation 做 semantic counter-action。

Compensation MUST 形成新的 history event，不能刪除原 commit。

---

# 20. Observer / Projection Service

Observer Service 是 read-side semantic boundary。

輸入：

$$
(W_\nu,O_\omega,\mathsf{ProjectionContract}).
$$

語義 projection：

$$
Z_q
=
\Pi_q^{(v)}(W_\nu,O_\omega).
$$

Service MAY：

- 讀 World snapshot；
- 更新 Observer state；
- request materialization；
- 使用 derived cache；
- 讀 history；
- 計算 projection。

Service MUST NOT 在 `observe(...)` path 隱式呼叫 `ModifyState` / `Commit`。

任何介入必須轉成新 OperationRequest：

```text
observe(...) -> read-side result
propose_intervention(...) -> ordinary operation pipeline
```

---

# 21. Materialization Manager

Materialization Manager 建立或維護 derived representation。

每個 materialized artifact SHOULD 綁定：

- source WorldVersionRef；
- FoundationRef；
- ProjectionContractRef；
- observer / query context when relevant；
- compute resolution；
- observer resolution；
- generated_at / logical revision；
- stale policy；
- provenance ref；
- approximation / loss metadata。

並保持：

$$
\boxed{
\mathsf{Materialized}(x)
\not\Rightarrow
\mathsf{Canonical}(x).
}
$$

Materialization Store SHOULD 支援 stale detection：

$$
\mathsf{SourceWorld}(m)
\neq
\mathsf{RequestedWorld}
\Rightarrow
\mathsf{Stale}(m)
$$

除非 contract 明確允許 bounded staleness。

---

# 22. Active Support / Lifecycle Manager

Lifecycle Manager 實作 Paper-05 的 finite active realization。

核心集合：

$$
\mathsf{Act}_\mu,
\quad
\mathsf{Dorm}_\mu,
\quad
\mathsf{Arch}_\mu,
\quad
\mathsf{Pot}_\mu.
$$

但它們不是一條簡單 mutually-exclusive enum；implementation SHOULD 以 typed predicates / lifecycle records 表示。

責任：

- activate / wake proposal；
- dormancy proposal；
- pin request；
- eviction plan；
- archive；
- restore；
- reactivation validation；
- boundary summary；
- resource envelope validation；
- lifecycle receipt。

Lifecycle Manager MAY 改 $\Xi_\mu$ ；若 lifecycle operation 會改 canonical World semantics，MUST 產生 ordinary operation proposal 走 Commit Gate。

## 22.1 Pin classes

至少分：

$$
\mathsf{Pin}^{\mathrm{Act}},
\qquad
\mathsf{Pin}^{\mathrm{Mat}},
\qquad
\mathsf{Pin}^{\mathrm{Ret}}.
$$

Observer demand MUST NOT 自動取得 pin authority。

## 22.2 Reactivation pipeline

Reference reactivation：

$$
\boxed{
\mathsf{Locate}
\rightarrow
\mathsf{Load}
\rightarrow
\mathsf{Decode}
\rightarrow
\mathsf{Reconstruct}
\rightarrow
\mathsf{CatchUp}
\rightarrow
\mathsf{Validate}
\rightarrow
\mathsf{Rebind}
\rightarrow
\mathsf{Activate}.
}
$$

`Load Success` 不得直接標記為 `Reactivate Success`。

---

# 23. Resource Manager 與 Cost Discipline

Resource Manager SHOULD 提供 typed envelope：

$$
\mathsf{Budget}_\mu
=
\{B_{\mu,k}\mid k\in\mathcal K_R\}.
$$

Hard resource feasibility：

$$
\forall k\in\mathcal K_R^{\mathrm{hard}},
\quad
\mathsf{Use}_k
\le
B_{\mu,k}.
$$

Resource dimensions MAY 包含：

- CPU；
- GPU；
- accelerator；
- RAM；
- VRAM；
- persistent storage；
- I/O bandwidth；
- network；
- latency budget；
- energy；
- external API quota；
- model invocation budget。

Resource Manager 不應把所有資源強制壓成單一 scalar。

此外：

$$
\boxed{
\text{Bounded Active Set}
\neq
\text{Bounded Step Cost}.
}
$$

Runtime SHOULD 量測：

$$
C_\mu^{\mathrm{step}}
=
C^{\mathrm{exec}}
+C^{\mathrm{reconcile}}
+C^{\mathrm{index}}
+C^{\mathrm{projection}}
+C^{\mathrm{lifecycle}}
+C^{\mathrm{history}}.
$$

---

# 24. History / Provenance Store

History plane 保存 typed receipts 與 typed relations。

Event graph：

$$
\mathcal G_H
=
(V_H,E_H,\tau_H),
$$

其中 $\tau_H$ 對 edge / relation 做 typed labeling。

最低 relation types SHOULD 包含：

```text
execution
causal
commit
rollback
compensation
observer
lifecycle
foundation_revision
derived_from
replay_of
fork_of
merge_of
```

Reference architecture MUST 保持：

$$
\boxed{
\prec_{\mathrm{exec}}
\neq
\prec_{\mathrm{causal}}
\neq
\prec_{\mathrm{commit}}
\neq
\prec_{\mathrm{log}}.
}
$$

History Store SHOULD 支援：

- append typed receipt；
- append relation；
- query lineage；
- checkpoint；
- replay；
- history equivalence verification；
- certified compaction；
- retention policy；
- export adapter。

## 24.1 Provenance interoperability

GCM-specific provenance SHOULD 保留自身 typed semantics，但 MAY 提供 W3C PROV export adapter。

可參考映射：

| GCM object | Generic provenance role |
|---|---|
| World snapshot / Proposal / Materialized Artifact | Entity |
| Operation / Execution / Reconciliation / Commit | Activity |
| Requester / Agent / Runtime module | Agent |
| source dependencies | used / wasDerivedFrom |
| generated artifact | wasGeneratedBy |
| responsible actor/module | wasAssociatedWith |

GCM-specific causal、commit、Foundation、Observer relations 不應為了映射到通用模型而被丟失。

---

# 25. History Index / Summary / Compression

Raw history 與 query index SHOULD 分離：

$$
\boxed{
\text{History Store}
\neq
\text{History Index}.
}
$$

Index MAY 重建，raw canonical receipt 則受 retention / transform contract 約束。

History transform：

$$
\mathsf C_{\mathbb S}:H\rightarrow H'.
$$

必須帶：

$$
\mathsf{HistoryCompressionCertificate}.
$$

若 equivalence unknown：

$$
\boxed{
\text{Unknown}
\Rightarrow
\text{No Merge By Default}.
}
$$

---

# 26. Checkpoint / Replay Service

Replay SHOULD 綁定明確 ReplayContract，包括：

- target history / commit；
- starting checkpoint；
- FoundationRef；
- executor versions；
- bridge versions；
- random seeds；
- external input captures；
- side-effect replay policy；
- allowed replay grade。

Replay grade：

$$
\mathsf{ReplayGrade}
\in
\{
\mathsf{Exact},
\mathsf{DeterministicInternal},
\mathsf{SemanticEquivalent},
\mathsf{Approximate},
\mathsf{NonReplayable}
\}.
$$

Replay Service MUST NOT claim a stronger grade than available evidence supports。

---

# 27. Foundation Lineage 與 Revision Gateway

Foundation Revision Gateway MUST 建立 explicit proposal：

$$
\rho_F
=
\left\langle
\mathcal F^{(v)},
\mathcal F^{(v+1)},
\mathsf{Reason},
\mathsf{GovernanceEvidence},
\mathsf{MigrationPlan},
\mathsf{CompatibilityAssessment}
\right\rangle.
$$

普通 OperationRequest 不得被 reinterpret 成 Foundation revision。

Foundation revision SHOULD 明確決定：

- existing Worlds 是否仍可使用舊 Foundation；
- 是否 fork；
- 是否 migrate；
- migration 是否是 ordinary World operation 或 special governance operation；
- old history 如何解讀；
- configuration registry 是否需同步升版；
- replay 是否跨 Foundation 合法。

---

# 28. Transaction Lifecycle State Machine

Reference operation lifecycle SHOULD 至少能映射到：

```text
RECEIVED
  ↓
TYPED
  ↓
CONTEXT_PINNED
  ↓
CANDIDATES_ENUMERATED
  ↓
PREEXEC_GATED
  ↓
ROUTE_SELECTED
  ↓
EXECUTING
  ↓
PROPOSED
  ↓
RECONCILING
  ↓
VERIFYING
  ↓
PRECOMMIT_GATED
  ↓
COMMITTING
  ↓
COMMITTED
```

旁路 disposition：

```text
DEFERRED
REFUSED
IDLE
ESCALATED
ABORTED
ROLLED_BACK
COMPENSATING
COMPENSATED
```

State machine MUST 記錄 terminal reason；`REFUSED` 不應被 silent retry 成 `EXECUTE`。

---

# 29. Pre-Execution 與 Pre-Commit 雙重 Gate

## 29.1 Pre-Execution Gate

沿用 TW-01：

$$
\mathsf{PreExecOK}
=
\mathsf{Addr}
\land
\mathsf{Reach}
\land
\mathsf{Adm}
\land
\mathsf{Auth}
\land
\mathsf{ExecContractOK}
\land
\mathsf{BridgeOK}.
$$

## 29.2 Pre-Commit Gate

Reference architecture 另外建議：

$$
\boxed{
\begin{aligned}
\mathsf{PreCommitOK}
:=
&\mathsf{ParentFresh}
\land
\mathsf{FoundationFresh}
\land
\mathsf{CommitAuthOK}
\\
&\land
\mathsf{VerificationPass}
\land
\mathsf{HistoryEvidenceReady}
\land
\mathsf{SchemaCompatible}.
\end{aligned}
}
$$

這是為了防止 route planning 與 commit 之間的 state / authority drift。

---

# 30. Concurrency 與 Ordering

Reference architecture 不要求單執行緒。

Local executor execution MAY 並行，只要：

- read snapshot 明確；
- proposal parent 明確；
- effect footprint 明確；
- side effect class 明確；
- reconciliation / conflict contract 可用。

## 30.1 Conflict relation

$$
\mathsf{Conflict}(\delta_a,\delta_b)
$$

SHOULD 至少考慮：

- write/write overlap；
- read/write invalidation；
- noncommutative effect；
- shared invariant；
- ordering contract；
- external side effect。

## 30.2 Commit serialization

MVP MAY 對單一 World boundary 採 serial commit gate，以降低複雜度。

Production implementation MAY 支援 partitioned / concurrent commit，但 MUST 證明：

$$
\boxed{
\text{Concurrent Commit}
\Rightarrow
\text{Declared Coherence Preserved}.
}
$$

GCM 不要求所有 systems 使用 distributed consensus：

$$
\boxed{
\text{Global Coherence}
\neq
\text{Consensus Algorithm}.
}
$$

但 multi-writer distributed deployment 必須使用足以維持其 declared commit semantics 的一致性機制。

---

# 31. Temporal / Scheduling Interface

Scheduler metadata $\sigma$ 與 World commit/history order 必須分離。

Reference architecture MAY 接入：

- event loop；
- priority scheduler；
- real-time scheduler；
- simulation scheduler；
- FMI-style scheduled model partitions；
- actor/event queues；
- heterogeneous task runtime。

但 MUST 保持：

$$
\boxed{
\text{Scheduler Order}
\neq
\text{Commit Order}
\neq
\text{Causal Order}.
}
$$

以及：

$$
\boxed{
\text{Global Computation}
\not\Rightarrow
\text{Single Global Clock}.
}
$$

---

# 32. Plugin / Extension Model

GCM Reference Runtime SHOULD 把 extension 分成：

```text
Executor Plugin
Bridge Plugin
Admissibility Validator Plugin
Verification Plugin
Route Planner / Ranking Policy Plugin
Projection Plugin
Materialization Backend
Archive Backend
History Export Adapter
Resource Provider Adapter
```

每個 plugin SHOULD 有：

- stable plugin ID；
- plugin version；
- contract schema version；
- capability declaration；
- input/output schemas；
- side-effect declaration；
- authority requirements；
- supported Foundation/config ranges；
- determinism declaration；
- failure semantics；
- provenance identity；
- optional integrity digest。

插件 discovery MUST NOT 自動取得 execution / commit authority。

---

# 33. Failure Model 與 Fail-Closed Policy

Reference Runtime SHOULD 將 TW-01 error classes映射到 typed error object。

至少包含：

```text
GCM_E_UNTYPED_OPERATION
GCM_E_UNKNOWN_WORLD_BOUNDARY
GCM_E_UNKNOWN_CONFIGURATION
GCM_E_UNREACHABLE_ROUTE
GCM_E_INADMISSIBLE_ROUTE
GCM_E_UNAUTHORIZED_OPERATION
GCM_E_EXECUTOR_CONTRACT
GCM_E_BRIDGE_UNKNOWN
GCM_E_BRIDGE_LOSS_EXCEEDED
GCM_E_RECONCILIATION
GCM_E_VERIFICATION
GCM_E_COMMIT_REJECTED
GCM_E_FOUNDATION_BOUNDARY
GCM_E_STALE_PROJECTION
GCM_E_RESOURCE_INFEASIBLE
GCM_E_REACTIVATION_INVALID
GCM_E_HISTORY_EQUIVALENCE_UNKNOWN
GCM_E_REPLAY_GRADE_DOWNGRADE
GCM_E_SCHEMA_VERSION
GCM_E_PROVENANCE_INCOMPLETE
```

Error object SHOULD 包含：

- code；
- operation ref；
- stage；
- hard / soft classification；
- evidence refs；
- retryable；
- disposition recommendation；
- user-safe message；
- internal diagnostic refs。

Unknown safety-critical state SHOULD fail closed。

---

# 34. Telemetry、Logging 與 Canonical History

Telemetry 用於 observability / performance，不自動等於 canonical history。

$$
\boxed{
\text{Telemetry Event}
\neq
\text{Canonical EventReceipt}.
}
$$

可以有：

- debug log；
- trace span；
- metrics；
- profiler sample；
- scheduler trace；
- resource telemetry。

只有經 canonical receipt writer / transform contract 的資料才進 $\mathcal H_\eta$。

Production deployment SHOULD 使用 correlation IDs 將 telemetry 與 canonical OperationId / CommitId 對接，但 MUST NOT 依賴 ephemeral logging 取代 audit provenance。

---

# 35. Crash Consistency 與 Recovery

Reference architecture SHOULD 定義 crash points：

1. request accepted before route；
2. during executor；
3. proposal persisted；
4. after reconciliation before verify；
5. after verify before commit；
6. during commit；
7. World committed before history receipt finalized；
8. lifecycle/archive in progress；
9. history compaction in progress。

最低 recovery obligation：

$$
\boxed{
\text{Crash}
\not\Rightarrow
\text{Silent Semantic Ambiguity}.
}
$$

每一個 in-flight operation 應能被分類為至少：

- not executed；
- executed but uncommitted；
- committed；
- commit state uncertain；
- compensation required。

若 commit state uncertain，Runtime MUST inspect canonical store / commit intent，不能盲目重做可能具有 external side effect 的 executor。

---

# 36. Side Effects 與 External Systems

某些 executor 會產生 external side effects，例如：

- file write；
- network request；
- actuator command；
- external API action；
- irreversible hardware action。

Reference contract SHOULD 標記：

$$
\mathsf{SideEffectClass}
\in
\{
\mathsf{Pure},
\mathsf{Idempotent},
\mathsf{Compensatable},
\mathsf{Irreversible},
\mathsf{Unknown}
\}.
$$

對不可逆 effect，proposal/commit model 可能無法物理上延遲 effect 到 commit。此時 executor contract MUST 額外聲明 prepare/confirm/compensation/governance semantics。

GCM 不宣稱能把所有外部世界 side effect 變成 ACID transaction。

---

# 37. Machine-Readable Schema Architecture

本 package 提供：

```text
schemas/gcm_runtime_core.schema.json
```

其中 SHOULD 至少定義 TW-01 要求的 20 種 machine-readable objects：

1. `WorldBoundaryRef`；
2. `FoundationRef`；
3. `ConfigurationRef`；
4. `OperationRequest`；
5. `OperationContract`；
6. `AuthorityContext`；
7. `RouteCandidate`；
8. `ExecutorContract`；
9. `BridgeContract`；
10. `Proposal`；
11. `VerificationResult`；
12. `CommitReceipt`；
13. `ProjectionContract`；
14. `MaterializationContract`；
15. `ActiveSupportContract`；
16. `ArchiveAnchor`；
17. `LifecycleReceipt`；
18. `EventReceipt`；
19. `HistoryRelation`；
20. `HistoryCompressionCertificate`。

Schema 是 reference wire/persistence shape，不等於完整形式語義。Runtime compliance 仍須同時滿足 TW-01 invariants。

---

# 38. Module Ownership Manifest

本 package 提供：

```text
manifests/module_ownership_map.json
```

它記錄每個 logical module：

- reads；
- writes；
- forbidden writes；
- upstream contracts；
- downstream artifacts；
- conformance hooks。

這個 manifest SHOULD 作為 TW-03 自動化 architecture-lint 的輸入之一。

---

# 39. Reference Deployment Profiles

## 39.1 Profile R0 — Deterministic Single-Process MVP

用途：M0–M4 reference runtime。

特性：

- single process；
- deterministic dispatcher；
- serial Commit Gate per World boundary；
- embedded persistent stores；
- in-process plugin interfaces；
- no distributed consensus；
- explicit fake / virtual clocks for tests；
- deterministic seeds where possible。

R0 的目標是驗證 semantics，而不是 throughput。

## 39.2 Profile R1 — Local Multi-Process Runtime

特性 MAY 包含：

- separate executor workers；
- separate commit service；
- durable proposal store；
- IPC/RPC；
- process sandbox；
- accelerator workers；
- dedicated history store；
- asynchronous observer/materialization workers。

仍維持 logical single Commit Gate per boundary。

## 39.3 Profile R2 — Distributed Runtime

特性 MAY 包含：

- distributed domain ownership；
- replicated registries；
- partitioned World Store；
- distributed executor pool；
- remote bridges；
- distributed history；
- replicated materialization；
- multiple scheduling domains。

R2 MUST 額外證明：

- commit consistency；
- stale snapshot handling；
- authority consistency；
- Foundation version consistency；
- history relation preservation；
- recovery after partial network failure。

TW-02 不指定 consensus protocol。

---

# 40. Reference API Boundaries

TW-02 建議將 API 分成五組。

## 40.1 Canonical registry API

```text
resolve_foundation(ref)
resolve_world_boundary(ref)
resolve_domain(ref)
resolve_configuration(ref)
resolve_contract(ref)
```

## 40.2 Operation pipeline API

```text
submit_operation(request)
create_execution_context(operation_id)
enumerate_routes(context)
preexec_gate(context, route)
select_safe_route(context, safe_routes)
execute_as_proposal(context, route)
reconcile(context, proposals)
verify(context, candidate_world)
precommit_gate(context, candidate_world, verification)
commit(context, candidate_world, verification)
```

## 40.3 Read-side API

```text
observe(request)
materialize(request)
refresh(materialization_id)
change_observer_state(observer_patch)
inspect_projection_provenance(materialization_id)
```

## 40.4 Lifecycle API

```text
inspect_active_support(boundary_ref)
validate_budget(candidate_support)
request_activation(unit_ref, reason)
request_dormancy(unit_ref, mode)
request_pin(unit_ref, pin_class)
archive(unit_ref, policy)
restore(anchor_ref, target_mode)
```

## 40.5 History / governance API

```text
append_receipt(receipt)
append_relation(relation)
checkpoint(policy)
replay(contract)
verify_history_equivalence(contract)
apply_history_transform(certificate)
propose_foundation_revision(proposal)
review_foundation_revision(proposal_ref)
publish_foundation_revision(approved_ref)
```

Transport MAY 是 function call、message bus、RPC、HTTP、gRPC 或其他；語義不可因 transport 改變。

---

# 41. Reference Dataflow：Ordinary ModifyState

以 `ModifyState` 為例：

```text
1. Operation Gateway
   -> validate typed request

2. Context Builder
   -> pin B_W / F^(v) / W_nu / AuthCtx / schema refs

3. Route Planner
   -> enumerate candidate configurations, executors, bridges

4. Reachability Engine
   -> remove unavailable candidates

5. Admissibility Validator
   -> reject illegal candidates

6. Authority Engine
   -> reject unauthorized candidates

7. Contract Gate
   -> reject unknown executor / bridge semantics

8. Route Selector
   -> optimize only among safe candidates

9. Executor Host
   -> execute against read view
   -> produce proposal delta

10. Proposal Store
    -> persist proposal + lineage

11. Reconciliation Engine
    -> combine proposal(s)
    -> produce candidate World

12. Verification Engine
    -> evaluate global invariants

13. Pre-Commit Gate
    -> recheck parent / Foundation / commit authority / evidence

14. Commit Gate
    -> publish W_(nu+1)

15. History Writer
    -> append typed receipts + relations

16. Projection / Materialization
    -> refresh only if policy demands

17. Lifecycle Manager
    -> update active support / resource state
```

這個流程不要求所有步驟都必須跨 process，但 semantic gates MUST 可識別、可測試、可審計。

---

# 42. Reference Dataflow：Pure Observe

```text
1. Observe Request
2. Resolve WorldVersionRef + ObserverRef
3. Projection Contract Check
4. Read canonical World snapshot
5. Optionally materialize derived artifact
6. Update O_omega and/or Xi_mu
7. Return representation
8. Append observer/materialization receipt when policy requires
```

必須保持：

$$
\boxed{
\Delta W=0.
}
$$

如果 request 需要介入：

```text
Observe -> propose_intervention -> new OperationRequest
```

不能在 Observer Service 內偷偷 commit。

---

# 43. Reference Dataflow：Foundation Revision

```text
1. Foundation revision proposal
2. Governance authority check
3. Compatibility / migration analysis
4. Review / approval evidence
5. Publish immutable F^(v+1)
6. Update Foundation lineage
7. Decide World migration / fork / stay-on-old-foundation
8. Record history
```

ordinary Route Planner、Executor 或 Commit Gate MUST NOT 自動執行 step 5。

---

# 44. Conformance Hooks for TW-03

TW-02 建議每個 module 暴露 test hooks：

```text
inspect_module_capabilities()
inspect_read_write_ownership()
export_contract_registry()
export_route_decision_trace(operation_id)
export_authority_decision(operation_id)
export_verification_evidence(commit_id)
export_world_lineage(world_version)
export_history_relations(event_id)
export_materialization_provenance(materialization_id)
export_lifecycle_receipt(unit_id)
```

TW-03 可用這些 hooks 驗證：

- 是否真的只有 Commit Gate 寫 World；
- route 是否先通過 authority；
- Foundation revision 是否獨立；
- Observer 是否造成 $\Delta W$ ；
- bridge unknown 是否 fail closed；
- local execution success 是否可能被 global verification 拒絕；
- history 是否保留 rollback / compensation；
- bounded active support 是否隱藏 full-scan cost。

---

# 45. MVP v0.1 的架構切片

## M0 — Canonical Kernel

最低模組：

```text
Specification / Schema Registry
Foundation Registry
World Store
Runtime State Store
Observer State Store
History Store
Domain Registry
Configuration Registry
Operation Gateway
Commit Gate skeleton
```

驗證：

$$
\mathbf W,
W_\nu,
\Xi_\mu,
O_\omega,
\mathcal F^{(v)},
\mathcal H_\eta
$$

可被機器層明確分離。

## M1 — Reachability / Admissibility / Authority

新增：

```text
Reachability Engine
Admissibility Validator
Authority Engine
Route Planner
PreExec Gate
```

核心測試：

$$
\text{Can}
\neq
\text{May}.
$$

## M2 — Heterogeneous Execution

新增：

```text
Executor Registry / Host
Bridge Registry / Host
Proposal Store
Safe Route Selector
```

至少 3–5 個 representative executors。

## M3 — Global Commit / History

新增：

```text
Reconciliation Engine
Verification Engine
PreCommit Gate
Commit Gate full implementation
History Relation Store
Checkpoint / Replay skeleton
```

核心測試：

$$
\text{Proposal}
\neq
\text{Commit}.
$$

## M4 — Bounded Active Runtime

新增：

```text
Materialization Manager
Active Support / Lifecycle Manager
Archive / Restore Backend
Resource Manager
History Index / Compaction
Conformance workload suite
```

核心測試：

$$
\text{Global Dependency}
\neq
\text{Full Materialization},
$$

$$
\text{Recursive Globality}
\neq
\text{Recursive Full Expansion}.
$$

---

# 46. Architecture Invariants — GCM-A

TW-02 增加下列 architecture-level invariants，供 TW-03 轉成測試。

## GCM-A01 — Sole Ordinary World Writer

$$
\boxed{
\text{Ordinary Canonical World Write}
\Rightarrow
\mathsf{CommitGate}.
}
$$

## GCM-A02 — Foundation Revision Isolation

$$
\boxed{
\text{Foundation Write}
\Rightarrow
\mathsf{FoundationRevisionGateway}.
}
$$

## GCM-A03 — Proposal Isolation

$$
\boxed{
\text{Executor Output}
\Rightarrow
\text{Proposal Store},
\quad
\not\Rightarrow
W_{\nu+1}.
}
$$

## GCM-A04 — Route Non-Escalation

$$
\boxed{
\text{Route Discovery}
\not\Rightarrow
\text{Authority Escalation}.
}
$$

## GCM-A05 — Safe-Set Optimization

$$
\boxed{
\text{Optimization Domain}
\subseteq
\mathcal Z_{\mathrm{safe}}.
}
$$

## GCM-A06 — Bridge Semantic Gate

$$
\boxed{
\text{Representable}
\not\Rightarrow
\text{Bridge Safe}.
}
$$

## GCM-A07 — Reconciliation Before Commit

$$
\boxed{
|\Delta_\nu|>1
\land
\text{coupling exists}
\Rightarrow
\mathsf{Reconcile}
\text{ before commit}.
}
$$

## GCM-A08 — Verification Before Commit

$$
\boxed{
\mathsf{Commit}
\Rightarrow
\mathsf{VerificationPass}.
}
$$

## GCM-A09 — Parent Freshness

$$
\boxed{
\text{Stale Parent}
\not\Rightarrow
\text{Blind Commit}.
}
$$

## GCM-A10 — Foundation Freshness

$$
\boxed{
\text{Foundation Drift}
\Rightarrow
\text{Revalidate / Defer / Escalate}.
}
$$

## GCM-A11 — Observer Read-Side Boundary

$$
\boxed{
\mathsf{Observe}
\Rightarrow
\Delta W=0.
}
$$

## GCM-A12 — Materialization Provenance

$$
\boxed{
\text{Materialized Artifact}
\Rightarrow
\text{Source World / Contract Provenance}.
}
$$

## GCM-A13 — Lifecycle Plane Separation

$$
\boxed{
\Delta\Xi_{\mathrm{lifecycle}}
\not\Rightarrow
\Delta W.
}
$$

## GCM-A14 — Authority Recheck When Revocable

$$
\boxed{
\text{Revocable Commit Authority}
\Rightarrow
\text{Pre-Commit Recheck}.
}
$$

## GCM-A15 — Typed History Relations

$$
\boxed{
\prec_{\mathrm{exec}}
\neq
\prec_{\mathrm{causal}}
\neq
\prec_{\mathrm{commit}}.
}
$$

## GCM-A16 — Rollback / Compensation Persistence

$$
\boxed{
\mathsf{Rollback}\lor\mathsf{Compensation}
\Rightarrow
\text{History Persistence}.
}
$$

## GCM-A17 — Unknown History Merge Safety

$$
\boxed{
\text{Unknown Equivalence}
\Rightarrow
\text{No Merge}.
}
$$

## GCM-A18 — Replay Evidence Bound

$$
\boxed{
\text{Replay Claim}
\preceq
\text{Available Replay Evidence}.
}
$$

## GCM-A19 — Telemetry Separation

$$
\boxed{
\text{Telemetry}
\neq
\mathcal H_\eta.
}
$$

## GCM-A20 — Plugin Non-Authority

$$
\boxed{
\text{Plugin Discovery / Loading}
\not\Rightarrow
\text{Operation Authority}.
}
$$

## GCM-A21 — No Single Clock Assumption

$$
\boxed{
\text{Runtime Composition}
\not\Rightarrow
\text{Single Global Clock}.
}
$$

## GCM-A22 — Global Coherence / Consensus Separation

$$
\boxed{
\text{Global Coherence}
\neq
\text{Distributed Consensus Algorithm}.
}
$$

## GCM-A23 — Crash Semantic Recoverability

$$
\boxed{
\text{Crash}
\Rightarrow
\text{Recoverable Operation Classification}.
}
$$

## GCM-A24 — Schema-Version Pinning

$$
\boxed{
\text{Persisted Contract Object}
\Rightarrow
\text{Schema Version Ref}.
}
$$

## GCM-A25 — External Side-Effect Typing

$$
\boxed{
\text{External Side Effect}
\Rightarrow
\text{Declared Effect Class / Recovery Semantics}.
}
$$

## GCM-A26 — Bounded Active / Bounded Cost Separation

$$
\boxed{
|\mathsf{Act}_\mu|<\infty
\not\Rightarrow
C_\mu^{\mathrm{step}}<C^*.
}
$$

---

# 47. Non-Normative Prior-Art Positioning

本 Reference Architecture 明確不宣稱以下既有技術由 GCM 首創。

## 47.1 Heterogeneous scheduling / data movement

StarPU 已長期將 task dependency、heterogeneous scheduling、data transfer、replication 與 asynchronous execution 整合進 runtime。GCM 不重新發明 heterogeneous task scheduler；GCM 對這類 runtime 的額外要求，是 scheduler / executor 必須位於 World-relative authority、admissibility、proposal、commit 與 provenance contract 中。

## 47.2 Privilege / coherence / mapping separation

Legion 已把 logical regions、privileges、coherence 與 mapping policy 系統化，並以 runtime / type system 保持 privilege subset。GCM 的 Authority Engine 與 Domain boundary 與此有相鄰性，但 GCM authority 不限定於 memory-region privilege，也包含 observation、materialization、state commit、rule 與 Foundation 等操作層。

## 47.3 Representation conversion legality

MLIR Dialect Conversion 已有 conversion target、legality、TypeConverter 與 materialization 機制。GCM Bridge contract 不主張發明 conversion legality；它要求 representation conversion 的 semantic preservation、loss/error、World/Observer boundary 與 provenance 能進入同一 route contract。

## 47.4 Scheduled execution / clocks

FMI 3.0.2 已提供 Scheduled Execution、model partitions、external scheduler 與 Clocks。GCM 不主張發明外部 scheduler 或 clocked partitions；GCM 要求 scheduler order、World evolution、commit order 與 history relation 型別分離。

## 47.5 Provenance interoperability

W3C PROV 已提供跨系統 provenance 的通用 data model / ontology。GCM typed history 應盡可能可 export / map 到通用 provenance vocabulary，同時保留 GCM-specific commit、Foundation、Observer、lifecycle 與 replay semantics。

---

# 48. Implementation Guidance：先 Modular Monolith，再分散

對 Reference MVP，建議：

$$
\boxed{
\text{Logical Modularity First}
+
\text{Physical Simplicity First}.
}
$$

即：

- 模組邊界清楚；
- interface 與 store ownership 清楚；
- 一開始可同一 process；
- 不先引入 distributed consensus；
- 不先引入 microservice explosion；
- 不先做 AI autonomous routing；
- deterministic validator / commit path 先完成。

當 M0–M4 的 conformance tests穩定後，再把 Executor Host、Materialization、History、Resource providers 等拆成 independent workers。

這樣可以避免：

$$
\boxed{
\text{Distributed Complexity}
\text{ masking }
\text{Semantic Bugs}.
}
$$

---

# 49. TW-03 直接交接

TW-03 應將：

$$
\boxed{
\text{GCM-C01--C28}
+
\text{GCM-A01--A26}
}
$$

轉成：

- static architecture tests；
- schema tests；
- runtime behavioral tests；
- fault-injection tests；
- provenance tests；
- authority tests；
- lifecycle / resource tests；
- replay / history tests；
- implementation profile declaration。

特別應驗證：

1. Executor 無 World write capability；
2. Foundation Registry ordinary write path 不存在；
3. AI planner 不能生成 authority；
4. Observer-only operation 始終 $\Delta W=0$ ；
5. stale parent 不 blind commit；
6. bridge unknown fail closed；
7. global verify 可拒絕 local success；
8. commit crash 可恢復分類；
9. rollback / compensation 不抹歷史；
10. bounded active workload 不偷偷 full-scan entire World/history。

---

# 50. 最終 Reference Runtime Contract

GCM Reference Runtime v0.1 的最小架構，可濃縮為：

$$
\boxed{
\begin{aligned}
\mathfrak R_{\mathrm{ref}}
=
\langle
&\mathsf{Registry},
\mathsf{WorldStore},
\mathsf{RuntimeStore},
\mathsf{ObserverStore},
\mathsf{HistoryStore},\\
&\mathsf{Gateway},
\mathsf{Reachability},
\mathsf{Admissibility},
\mathsf{Authority},
\mathsf{Router},\\
&\mathsf{ExecutorHost},
\mathsf{BridgeHost},
\mathsf{ProposalStore},
\mathsf{Reconcile},
\mathsf{Verify},\\
&\mathsf{CommitGate},
\mathsf{Projection},
\mathsf{Materialization},
\mathsf{Lifecycle},
\mathsf{Resource},\\
&\mathsf{Replay},
\mathsf{FoundationRevisionGateway}
\rangle.
\end{aligned}
}
$$

其 ordinary write discipline 為：

$$
\boxed{
\begin{array}{rcl}
\text{World write} &\Rightarrow& \mathsf{CommitGate},\\
\text{Foundation write} &\Rightarrow& \mathsf{FoundationRevisionGateway},\\
\text{Observer write} &\Rightarrow& \mathsf{ObserverService},\\
\text{Runtime-control write} &\Rightarrow& \mathsf{TypedRuntimeManagers},\\
\text{History write} &\Rightarrow& \mathsf{Receipt/TransformContract}.
\end{array}
}
$$

而 operation lifecycle 為：

$$
\boxed{
\begin{aligned}
\text{Request}
&\rightarrow
\text{Context Pinning}
\rightarrow
\text{Route Enumeration}\\
&\rightarrow
\text{Reachability}
\rightarrow
\text{Admissibility}
\rightarrow
\text{Authority}\\
&\rightarrow
\text{Contract Validation}
\rightarrow
\text{Safe Selection}
\rightarrow
\text{Proposal Execution}\\
&\rightarrow
\text{Reconciliation}
\rightarrow
\text{Verification}
\rightarrow
\text{Pre-Commit Revalidation}\\
&\rightarrow
\text{Commit / Reject / Rollback / Compensation}\\
&\rightarrow
\text{Typed History + Lifecycle / Projection Follow-up}.
\end{aligned}
}
$$

這個架構的核心不是「建立一個很大的 scheduler」，而是建立一套能讓異質計算、不同 domain、不同 representation、不同 observer、有限資源與不同 history requirement 在 **不互相偷換語義權限** 的前提下共同運行的 Runtime contract。

因此：

$$
\boxed{
\text{Global Computation Runtime}
\neq
\text{One Universal Executor}.
}
$$

更精確地：

$$
\boxed{
\text{GCM Reference Runtime}
=
\text{A Typed Coordination, Validation, Commit, and Provenance Architecture for Globally Coherent Heterogeneous Computation}.
}
$$

---

# Appendix A. Canonical Module List

Reference modules：

1. Specification / Schema Registry；
2. Foundation Registry；
3. Foundation Lineage Registry；
4. Foundation Revision Gateway；
5. World Store；
6. Runtime State Store；
7. Observer State Store；
8. Domain Registry；
9. Configuration Registry；
10. Operation Gateway；
11. Execution Context Builder；
12. Reachability / Resource Engine；
13. Admissibility Validator；
14. Authority Engine；
15. Route Planner；
16. Safe Route Selector；
17. Executor Registry；
18. Executor Host；
19. Bridge Registry；
20. Bridge Host；
21. Proposal Store；
22. Reconciliation Engine；
23. Verification Engine；
24. Pre-Commit Gate；
25. Commit Gate；
26. Observer / Projection Service；
27. Materialization Manager / Store；
28. Active Support / Lifecycle Manager；
29. Archive / Restore Backend；
30. Resource Manager；
31. History / Provenance Store；
32. History Index / Summary；
33. Checkpoint / Replay Service；
34. History Transform / Compression Service；
35. Telemetry / Diagnostics Adapter。

Physical implementation MAY 合併多個 logical modules，但 MUST 能證明 ownership 與 invariant 沒有因此消失。

---

# Appendix B. Canonical Storage Classes

建議最低儲存分類：

```text
Canonical immutable/versioned:
- Foundation objects
- committed World versions
- canonical receipts

Runtime mutable:
- Xi_mu
- resource snapshots
- active-support state
- caches

Observer mutable:
- O_omega

Derived/materialized:
- projection artifacts
- indexes
- summaries

Proposal/transient:
- local proposals
- candidate Worlds
- reconciliation artifacts

Archive:
- dormant payloads
- checkpoints
- externalized chunks
```

---

# Appendix C. Canonical Handoff

下一份文件：

**TW-03｜GCM Conformance, Verification & Reference Implementation Specification v0.1**

TW-03 應直接讀取：

1. TW-01 的 GCM-C invariants；
2. TW-02 的 GCM-A invariants；
3. machine-readable schemas；
4. module ownership manifest；
5. MVP profile manifest。

TW-03 完成後，才正式進入 GCM Reference Runtime MVP v0.1 的 M0 implementation。
