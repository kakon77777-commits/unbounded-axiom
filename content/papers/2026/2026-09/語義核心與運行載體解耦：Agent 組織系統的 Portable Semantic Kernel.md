# 語義核心與運行載體解耦：Agent 組織系統的 Portable Semantic Kernel

## Decoupling Semantic Core from Runtime Substrate: A Portable Semantic Kernel for Agentic Organizations

**系列：** ANDO Twin Runtime Series  
**篇次：** 02 / 05  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-23  
**文件類型：** 理論論文 / 架構規格定位論文  
**狀態：** 公開初稿  

---

## 摘要

雙生 Agent 組織架構若只停留在「同一品牌提供兩個版本」，便無法保證 General-OS Runtime 與 Native Runtime 在長期演化後仍屬於同一系統。真正困難的問題不是如何將同一份程式碼移植到不同平台，而是如何識別、抽離並形式化那些不應隨資料庫、UI、作業系統、檔案系統、通訊協議或原生世界模型改變的組織語義。

本文提出 Portable Semantic Kernel（PSK）作為 ANDO 雙生架構的共同語義核心。PSK 不等同於共享 library，也不等同於共同資料表，而是一組可由不同 runtime realization 所承載的最小組織語義契約。本文將其形式化為 identity、state revision、task semantics、delegation、authority、budget、checkpoint、artifact、verification、receipt、commit、event history、revocation 與 human escalation 等語義單元，並區分 hard invariants、portable contracts、projection metadata 與 substrate-private state。

本文進一步提出 semantic projection、abstraction map、conformance probe、semantic fingerprint、compatibility class、loss-annotated migration 與 kernel versioning 等機制，用來判定兩個彼此不同的實作是否仍能被稱為同一 ANDO。本文的核心命題是：真正應共享的是可審計的語義關係，而非表面資料結構。只有當 General-OS Runtime 與 HDUS-native Runtime 都能穩定投影回同一 Portable Semantic Kernel，雙生產品線才不會在功能分化中逐步退化為 semantic fork。

---

## 關鍵詞

Portable Semantic Kernel、Agentic Organization、Semantic Contract、Runtime Substrate、ANDO、HDUS、Conformance、Delegation、Authority、Verification、Migration、Semantic Drift

---

# 1. 問題：什麼才算「同一個 ANDO」？

假設存在兩個實作：

$$
R_G
$$

與：

$$
R_N,
$$

前者運行於 conventional operating systems，後者運行於 world-native substrate。

若兩者：

- UI 不同；
- 程式語言不同；
- 資料庫不同；
- artifact representation 不同；
- authority implementation 不同；
- history storage 不同；

那麼要如何判斷它們仍是同一系統，而不是僅共享名稱？

若判準是「程式碼相同」，則 Native Runtime 幾乎必然不合格。

若判準是「畫面相同」，則任何深度 native integration 都會被迫模仿 Web Dashboard。

若判準是「資料表欄位相同」，則 implementation detail 會反過來綁架未來架構。

因此本文採另一個判準：

$$
\boxed{
SystemIdentity
=
SemanticInvariants
+
BehavioralContracts
+
HistoricalContinuity.
}
$$

也就是：

> 一個系統的身份應由它保持了哪些可觀察語義與歷史關係決定，而不是由它用了哪一種 runtime substrate 決定。

---

# 2. Portable Semantic Kernel 的定義

定義 ANDO Portable Semantic Kernel：

$$
\mathcal K_P
=
(
\mathcal I,
\mathcal S,
\mathcal T,
\mathcal D,
\mathcal A,
\mathcal B,
\mathcal C,
\mathcal R,
\mathcal V,
\mathcal Q,
\mathcal M,
\mathcal E,
\mathcal H
).
$$

其中：

- $\mathcal I$：Identity semantics；
- $\mathcal S$：Canonical state / revision semantics；
- $\mathcal T$：Task semantics；
- $\mathcal D$：Delegation semantics；
- $\mathcal A$：Authority semantics；
- $\mathcal B$：Budget semantics；
- $\mathcal C$：Checkpoint semantics；
- $\mathcal R$：Artifact / resource semantics；
- $\mathcal V$：Verification semantics；
- $\mathcal Q$：Receipt semantics；
- $\mathcal M$：Commit semantics；
- $\mathcal E$：Event / history semantics；
- $\mathcal H$：Human escalation / governance semantics。

此 kernel 不要求兩個 runtime 共用相同 persistence mechanism。

因此：

$$
\boxed{
PortableSemanticKernel
\neq
SharedDatabaseSchema.
}
$$

也不要求：

$$
PortableSemanticKernel
=
SharedSourceCode.
$$

---

# 3. Kernel、Contract、Representation 三層分離

本文將系統分成三層。

## 3.1 Semantic Kernel

描述「什麼必須為真」。

例如：

$$
A_{child}
\subseteq
A_{parent}.
$$

## 3.2 Portable Contract

描述「如何被查詢、驗證與交換」。

例如：

```text
delegation.id
delegation.parent_id
delegation.authority
delegation.status
delegation.revoked_at
```

## 3.3 Runtime Representation

描述「平台內部如何實作」。

General-OS Runtime 可能使用：

```text
SQLite row
JSON column
filesystem artifact
HTTP adapter
```

Native Runtime 可能使用：

```text
world object
native authority edge
persistent session state
event lineage object
```

因此：

$$
\boxed{
Kernel
\rightarrow
Contract
\rightarrow
Representation
}
$$

而不是：

$$
Representation
\rightarrow
Kernel.
$$

---

# 4. Hard Invariants 與 Soft Conventions

不是所有跨平台共同項目都具有相同強度。

本文區分：

$$
\mathcal K_P
=
\mathcal K_H
\cup
\mathcal K_C,
$$

其中：

- $\mathcal K_H$ 為 Hard Invariants；
- $\mathcal K_C$ 為 Portable Conventions。

Hard Invariants 一旦被違反，就代表 semantic incompatibility。

Portable Conventions 可以版本化、擴張或重新表示。

例如：

### Hard

$$
DelegatedAuthority
\neq
TransferredSovereignty.
$$

### Convention

```text
commit class name = W1
```

若未來 Native Runtime 將 W1 顯示成另一個 UI label，只要其語義仍相同，便不構成違反。

---

# 5. Identity Semantics

一切 portability 都先依賴 identity。

定義 entity identity：

$$
I(e)
=
(
ID,
Type,
Origin,
Lineage
).
$$

最低要求：

1. ID 在同一 organizational domain 內唯一；
2. Type 可被辨識；
3. Origin 可追溯；
4. Lineage 不因 migration 被抹除。

因此：

$$
Migration(e)
\not\Rightarrow
NewIdentity(e)
$$

除非 migration policy 明確聲明 fork。

若 migration 產生新實體，應記錄：

$$
ParentIdentity
\rightarrow
DerivedIdentity.
$$

---

# 6. Canonical State 與 Revision Semantics

Portable kernel 不要求 canonical state 一定放在中央資料庫，但要求：

> 任一 runtime 必須能指出目前哪一個狀態被視為 canonical。

定義：

$$
S_t
=
CanonicalState(t).
$$

再定義 revision：

$$
r_t
=
Revision(S_t).
$$

若 state transition 被接受：

$$
S_t
\rightarrow
S_{t+1},
$$

則至少應滿足：

$$
r_{t+1}>r_t.
$$

這不要求 revision 一定是整數，但要求可比較且可追溯。

因此：

$$
\boxed{
Canonicality
\neq
CentralizedStorage.
}
$$

---

# 7. Task Semantics

Task 的 portable semantic minimum：

$$
T
=
(
TID,
Intent,
Goal,
Status,
Dependencies,
SuccessCriteria,
Constraints,
Version
).
$$

其中 Task status 可以由 runtime 擴張，但至少需要能區分：

```text
Pending
Ready
Running
Completed
Blocked
Failed
Cancelled
```

最重要的是：

$$
\boxed{
Task.Completed
=
OperationalCompletion
}
$$

而不是：

$$
Task.Completed
=
VerifiedTruth.
$$

這一條必須跨 General-OS 與 Native Runtime 保持。

否則兩邊對同一 task 的語義會發生根本分歧。

---

# 8. Task Graph Semantics

定義 task graph：

$$
G_T
=
(V_T,E_T).
$$

Portable minimum 要求：

- node identity 可保留；
- edge relation 可辨識；
- dependency resolution 可重現；
- completed node 不因 UI 改變而失去完成狀態；
- cycle policy 明確。

對普通 dependency：

$$
Ready(T_i)
\Rightarrow
\forall T_j\in Pred(T_i),
\quad
Completed(T_j)=1.
$$

若 future Native Runtime 增加 spatial、temporal 或 causal edge，這些可以是 runtime extension，但不能改寫既有 dependency semantics。

---

# 9. Delegation Semantics

Delegation 是 ANDO kernel 中最重要的 portable object 之一。

定義：

$$
D
=
(
DID,
RID,
Intent,
Scope,
Target,
Authority,
Budget,
Risk,
Verification,
Output,
Checkpoint,
Escalation,
Parent
).
$$

其中：

- DID 為 delegation identity；
- RID 為 request / run identity；
- Parent 表示 delegation lineage。

最核心不變量：

$$
A_{child}
\subseteq
A_{parent}.
$$

以及：

$$
B_{child}
\leq
B_{parent}.
$$

這些語義必須在任何 substrate 上成立。

---

# 10. Authority Semantics

Capability 與 Authority 必須分離。

定義 Agent 能力集合：

$$
C(a).
$$

定義已授權集合：

$$
A(a,t).
$$

允許行動集合：

$$
X(a,t)
=
C(a)
\cap
A(a,t).
$$

因此即使某 Native Agent 技術上能操作整個 world state：

$$
C(a)=Large,
$$

也不表示：

$$
A(a,t)=Large.
$$

這是 Native Runtime 最容易因 integration depth 而被破壞的 semantic boundary，因此必須進 kernel。

---

# 11. Revocation Semantics

任何 portable authority model 都必須支援：

$$
Grant
\rightarrow
Use
\rightarrow
Revoke.
$$

定義 revocation event：

$$
Rev(D,t_r).
$$

若操作開始時間為 $t_x$，則：

$$
t_x>t_r
\Rightarrow
ActionDenied
$$

除非該 operation 已被明確 grandfathered。

可記錄 revocation latency：

$$
L_R
=
t_s-t_r.
$$

不同 runtime 可以有不同 $L_R$，但 revocation 本身不可被省略。

---

# 12. Budget Semantics

Agent 組織不只管理權限，也管理消耗。

定義：

$$
\mathbf B
=
(
B_{token},
B_{compute},
B_{context},
B_{tool},
B_{parallel},
B_{runtime},
B_{money},
B_{human}
).
$$

Portable kernel 要求 child budget 不可在無外部授權下自行膨脹：

$$
\mathbf B_{child}
\preceq
\mathbf B_{parent}.
$$

不同 substrate 可以加入額外 budget dimension，但不能取消 monotonicity。

---

# 13. Checkpoint Semantics

Checkpoint 的目的不是單純 save file，而是讓 Agent 可替換。

定義：

$$
C_k
=
(
TaskState,
Progress,
Artifacts,
OpenIssues,
NextStep,
AuthorityContext,
Revision
).
$$

其最低要求是：

$$
Agent_A
\rightarrow
Failure
\rightarrow
Agent_B
$$

後：

$$
Resume(Agent_B,C_k)
$$

不需要人類重新 copy-paste 主要上下文。

因此 checkpoint portability 是雙生架構 migration 的核心之一。

---

# 14. Artifact Semantics

Portable Artifact 不應等於 filesystem path。

定義：

$$
R
=
(
RID,
Type,
Identity,
Digest,
Lineage,
Producer,
Status,
Metadata
).
$$

General-OS Runtime 可令：

$$
Identity
=
Path
+
Digest.
$$

Native Runtime 可令：

$$
Identity
=
NativeObjectID
+
HistoryHash.
$$

portable kernel 只要求：

- 可識別；
- 可追溯；
- 可驗證內容或狀態；
- lineage 可保留。

---

# 15. Artifact Mutation

如果 artifact 被修改：

$$
R_1
\rightarrow
R_2,
$$

則不能假設：

$$
Verification(R_1)
=
Verification(R_2).
$$

若 digest：

$$
d_1\neq d_2,
$$

則：

$$
V_1
\not\models
R_2.
$$

這個 invariant 必須跨 runtime 保留。

---

# 16. Verification Semantics

Portable Verification 定義：

$$
V
=
(
VID,
Target,
Contract,
Verifier,
Method,
Status,
Verdict,
Level,
Modes,
Evidence,
Independence,
Time
).
$$

其中：

$$
VerificationStatus
\neq
VerificationVerdict.
$$

例如：

```text
status = Completed
verdict = Fail
```

表示 verifier 正常執行，且觀察到 epistemic failure。

而：

```text
status = Failed
```

表示 verification procedure 本身失敗。

這個區分必須進 PSK。

---

# 17. Verification Level Semantics

Shared vocabulary：

```text
L0 Metadata
L1 Structural
L2 Executed
L3 Reproduced
L4 FormallyOrAuthoritativelyGrounded
```

其意義是 procedure strength，而不是 truth probability。

因此：

$$
L4
\not\Rightarrow
UniversalTruth.
$$

以及：

$$
Pass
\neq
True.
$$

---

# 18. Independence Semantics

定義 independence vector：

$$
I
=
(
I_A,
I_M,
I_S,
I_E
).
$$

其中：

- $I_A$：actor independence；
- $I_M$：method independence；
- $I_S$：source independence；
- $I_E$：environment independence。

核心 invariant：

$$
MultipleAgents
\not\Rightarrow
IndependentEvidence.
$$

Native Runtime 不得因多個 Agent 在同一 world 中重複同一判斷，就自動提高 independence。

---

# 19. Receipt Semantics

Receipt 是「發生過什麼」的不可變記錄。

定義：

$$
Q
=
(
QID,
Type,
Actor,
Target,
Method,
InputDigest,
OutputDigest,
Time,
Result
).
$$

最重要原則：

$$
\boxed{
Receipt
=
HistoricalRecord
}
$$

而不是：

$$
Receipt
=
TruthCertificate.
$$

因此 Receipt 可記錄成功、失敗、拒絕、撤銷與 inconclusive。

---

# 20. Receipt Chain

最低 receipt chain：

$$
Receipt_D
\rightarrow
Receipt_X
\rightarrow
Receipt_V
\rightarrow
Receipt_C.
$$

分別表示：

- Delegation；
- Execution；
- Verification；
- Commit。

不同 runtime 可以用不同 persistence，但 lineage 必須可追溯。

---

# 21. Commit Semantics

Commit 不是簡單 save。

定義：

$$
M
=
(
MID,
Target,
Class,
Authority,
VerificationState,
RevisionBefore,
RevisionAfter,
Receipt,
Time
).
$$

核心條件：

$$
CommitPermission
=
OperationalIntegrity
\land
GovernanceSatisfied.
$$

若 policy 要求 typed verification：

$$
CommitPermission
=
OperationalIntegrity
\land
VerificationSatisfied.
$$

---

# 22. Commit Class

即使未來名稱改變，也應保留對應語義層級。

例如：

```text
W0 private draft
W1 internal canonical commit
W2 routine external/public commit
W3 high-reputation statement
W4 legal/financial/identity-sensitive commit
```

不是所有 runtime 都必須實作全部 class，但若宣告支援，則其語義必須一致。

---

# 23. Event History Semantics

Event stream：

$$
E
=
\{e_1,e_2,\ldots,e_n\}.
$$

每一 event 至少應有：

$$
e_i
=
(
Type,
Entity,
Actor,
Revision,
Time,
Payload
).
$$

History portability 要求：

$$
Migration
\not\Rightarrow
HistoryReset.
$$

若歷史被壓縮，則必須存在：

$$
CompressionManifest.
$$

---

# 24. Human Escalation Semantics

Human-on-the-Bridge 並不意味每次 Agent 遇到問題都通知人。

定義 escalation function：

$$
H
=
Escalate(
Risk,
Authority,
Ambiguity,
Irreversibility,
PolicyConflict
).
$$

只有當：

$$
H=1
$$

時才需要 human decision。

因此：

$$
\boxed{
HumanGovernance
\neq
HumanAsRetryButton.
}
$$

這一條也屬於 portable kernel。

---

# 25. 四層可攜狀態分類

本文將 runtime state 分為四層。

## P0 — Hard Semantic State

例如：

- identity；
- authority；
- delegation lineage；
- verification verdict；
- commit history。

必須攜帶。

## P1 — Portable Operational State

例如：

- task status；
- checkpoint；
- retry lineage；
- unresolved human queue。

應優先攜帶。

## P2 — Projection Metadata

例如：

- filesystem path；
- API endpoint；
- local cache identifier。

可以轉換。

## P3 — Substrate-Private State

例如：

- renderer cache；
- temporary DOM state；
- GPU command buffer；
- OS-private process handle。

不要求攜帶。

---

# 26. Portability Projection

定義 runtime state：

$$
X_R.
$$

Portable projection：

$$
\Pi_P
:
X_R
\rightarrow
X_P.
$$

其中：

$$
X_P
=
P0
\cup
P1.
$$

Projection metadata：

$$
X_M
=
P2.
$$

Private state：

$$
X_L
=
P3.
$$

因此：

$$
X_R
=
X_P
\cup
X_M
\cup
X_L.
$$

這提供 migration engine 一個明確的選擇框架。

---

# 27. Loss Manifest

若 migration：

$$
M_{A\rightarrow B}
$$

無法完整保存某些 P1 / P2 state，則必須生成：

$$
L_M
=
(
Preserved,
Degraded,
Dropped,
Reason,
RecoveryHint
).
$$

核心 invariant：

$$
Loss>0
\Rightarrow
L_M\neq\varnothing.
$$

因此無法表達的 Native World relation 不能被靜默丟棄。

---

# 28. Semantic Fingerprint

為了快速判斷 runtime 是否仍符合同一 kernel，可定義：

$$
F_S(R)
=
Hash(
KernelVersion,
SupportedContracts,
InvariantSet,
ProbeResults
).
$$

Semantic Fingerprint 不等於 security hash。

它是 compatibility fingerprint。

例如：

```text
kernel_version: 0.1
delegation: 1.0
verification: 1.0
commit: 1.0
migration: 0.1
probe_suite: PASS
```

---

# 29. Kernel Versioning

Portable Semantic Kernel 需要版本。

定義：

$$
K^{(0.1)},
K^{(0.2)},
\ldots
$$

對於 backward-compatible extension：

$$
K^{(n+1)}
\supseteq
K^{(n)}
$$

且舊核心語義保持。

若 breaking semantic change：

$$
K^{(n+1)}
\not\sim
K^{(n)},
$$

就不能只改 implementation version，必須明確升 kernel major version。

---

# 30. Contract Versioning

不同 semantic family 應獨立版本化，例如：

```text
DelegationContract 1.0
VerificationContract 1.0
CommitContract 1.0
MigrationContract 0.1
```

因此不要求任何小修改都升整個 kernel major version。

---

# 31. Compatibility Class

定義 runtime compatibility：

$$
Compat(R,K)
\in
\{
Full,
Partial,
ReadOnly,
ImportOnly,
Incompatible
\}.
$$

例如：

### Full

可讀、可寫、可驗證全部必要語義。

### Partial

缺少部分 optional extension。

### ReadOnly

可讀歷史但不能安全寫回。

### ImportOnly

只能做一次性 migration。

### Incompatible

無法保留 hard invariants。

---

# 32. Conformance Probe

PSK 不能只靠文件宣告。

定義 probe set：

$$
\mathcal P_K
=
\{p_1,p_2,\ldots,p_n\}.
$$

最低 probe 可以包括：

1. identity preservation；
2. child authority monotonicity；
3. revocation；
4. task dependency；
5. checkpoint resume；
6. artifact mutation invalidation；
7. verification type separation；
8. receipt persistence；
9. commit gate；
10. human escalation。

若 runtime：

$$
\forall p_i\in\mathcal P_K,
\quad
p_i(R)=PASS,
$$

才宣告對相應 kernel profile conformance。

---

# 33. Cross-Runtime Conformance

對雙生 runtime：

$$
R_G,
R_N,
$$

可執行同一 logical scenario。

例如：

```text
Create intent
Create task
Delegate
Produce artifact
Verify
Commit
Revoke
Resume
```

抽象後比較：

$$
\alpha_G(Result_G)
$$

與：

$$
\alpha_N(Result_N).
$$

要求：

$$
\alpha_G(Result_G)
=
\alpha_N(Result_N)
$$

在 hard semantic domain 上成立。

---

# 34. Semantic Adapter

General-OS 與 Native Runtime 中間不應直接互拷內部資料。

應透過：

$$
Adapter_R
:
Representation_R
\leftrightarrow
PortableContract.
$$

例如：

```text
SQLiteDelegationAdapter
HDUSAuthorityEdgeAdapter
```

兩者都映射到：

```text
PortableDelegationContract
```

這避免 migration engine 綁死某一端的 schema。

---

# 35. Anti-Corruption Boundary

如果 legacy system 的概念與 ANDO 語義不完全一致，應建立 anti-corruption boundary。

例如 legacy system 只有：

```text
user_role = admin
```

但 ANDO 需要：

```text
scope
authority
expiry
revocation
budget
```

則不能直接宣稱兩者等價。

需要：

$$
LegacyRole
\rightarrow
TranslationPolicy
\rightarrow
ANDOAuthority.
$$

翻譯不足的部分應標記：

$$
Unknown
$$

或：

$$
Degraded.
$$

---

# 36. Native Projection 的特殊要求

Native Runtime 的風險不是功能不足，而是「過度融合」。

例如 Native World 可能允許：

$$
Agent
\leftrightarrow
WorldState
$$

直接互動。

但仍需保持：

$$
AgentIdentity
\neq
WorldAuthority.
$$

以及：

$$
ObservedState
\neq
CommittedState.
$$

因此 PSK 是 Native Runtime 防止 semantic over-collapse 的保護層。

---

# 37. General-OS Projection 的特殊要求

General-OS Runtime 的風險則是「橋接過度碎片化」。

例如：

```text
database task
filesystem artifact
browser session
API token
human approval
```

可能分散在不同系統。

PSK 提供統一 identity / lineage，使：

$$
FragmentedRepresentation
\rightarrow
UnifiedSemanticView.
$$

---

# 38. Kernel Minimality

Portable kernel 不能無限膨脹。

如果把每個產品功能都加入 kernel：

$$
|\mathcal K_P|
\rightarrow
Large,
$$

則跨 runtime compatibility 成本會急速上升。

因此採：

$$
\boxed{
MinimalKernel
+
VersionedExtensions.
}
$$

只有當某語義：

1. 跨 runtime 必須一致；
2. 影響安全、身份、歷史或治理；
3. 影響 migration correctness；

才應進 core kernel。

---

# 39. Extension Profiles

可定義 profile：

```text
PSK-Core
PSK-Verification
PSK-PublicActor
PSK-Enterprise
PSK-NativeWorld
```

Runtime 可以宣告：

```text
PSK-Core: Full
PSK-Verification: Full
PSK-PublicActor: Partial
PSK-NativeWorld: Incompatible
```

這比單一「支援 ANDO / 不支援 ANDO」更精確。

---

# 40. 安全性：Semantic Downgrade Attack

Migration 或 adapter 可能形成新的攻擊面。

例如：

$$
W4
\rightarrow
W1
$$

若在轉換時被錯誤降級，可能繞過高風險 commit gate。

因此定義：

$$
SemanticDowngrade
=
SecurityRelevantMeaningLoss.
$$

要求：

$$
SemanticDowngrade>0
\Rightarrow
Reject
\lor
ExplicitApproval.
$$

---

# 41. Authority Laundering

另一風險是 authority laundering。

假設：

$$
A_G
$$

在 General Runtime 中受限制。

Migration 後若 Native Runtime 只看到「可操作」，而遺失 scope / expiry：

$$
A_N
\supset
A_G.
$$

這違反：

$$
NoAuthorityInflation.
$$

因此 authority contract 必須是 P0 hard semantic state。

---

# 42. Verification Laundering

同樣不能把：

```text
Generic Pass
```

migration 成：

```text
Code Pass
```

因此：

$$
Type(V_G)
=
Type(V_N)
$$

除非有明確 re-verification。

即：

$$
GenericPass
\not\Rightarrow
TypedPass.
$$

跨 runtime 仍成立。

---

# 43. History Laundering

如果 migration 只帶 current state，不帶造成此狀態的歷史：

$$
CurrentState
-
Lineage,
$$

便可能讓 revoked authority、failed verification、incident history 消失。

因此：

$$
CanonicalState
\neq
SufficientMigrationState.
$$

至少 P0 history 必須保留。

---

# 44. Portable Kernel 與資料壓縮

Portability 不要求保存所有原始細節。

可以壓縮：

$$
History
\rightarrow
CompressedHistory
$$

但必須保留：

- hash / digest；
- source range；
- compression method；
- reconstruction boundary；
- loss statement。

因此：

$$
Compression
\neq
SilentDeletion.
$$

---

# 45. PSK 與 Human Sovereignty

PSK 最終仍服務於：

$$
DelegatedAuthority
\neq
TransferredSovereignty.
$$

若某 runtime 無法：

- revoke；
- inspect；
- audit；
- escalate；
- stop high-risk commit；

則即使其 Agent 能力更高，也不能被視為 Full PSK conformance。

因此 human sovereignty 是 portable semantic requirement，而不是 UI feature。

---

# 46. Reference Object Model

PSK 最低 object families：

```text
Intent
Task
Agent
Delegation
Artifact
Checkpoint
VerificationRequirement
Verification
Evidence
Receipt
Commit
Event
HumanQueueItem
Policy
Budget
```

不同 runtime 不必使用相同 class name，但 abstraction layer 必須能映射。

---

# 47. Portable Query Surface

為了 conformance，可定義最低 query surface：

```text
get_entity(id)
get_revision()
get_task_dependencies(task_id)
get_active_authority(subject)
get_delegation_lineage(id)
get_latest_checkpoint(task_id)
get_artifact_lineage(id)
get_latest_applicable_verification(id, contract)
get_commit_eligibility(id, class)
get_unresolved_human_items()
get_event_history(entity_id)
```

這不是產品 API 的最終樣式，而是 semantic probe surface。

---

# 48. Portable Mutation Surface

最低 mutation surface：

```text
create_task(...)
delegate(...)
revoke(...)
checkpoint(...)
register_artifact(...)
request_verification(...)
record_receipt(...)
commit(...)
escalate(...)
```

所有 mutation 都應能生成 event / receipt 或等價歷史證據。

---

# 49. 形式化一致性條件

對 runtime $R$，若存在 abstraction：

$$
\alpha_R:R\rightarrow\mathcal K_P,
$$

且所有 hard invariants：

$$
\forall h\in\mathcal K_H,
\quad
h(\alpha_R(R))=\text{true},
$$

並通過指定 conformance probes：

$$
\forall p\in\mathcal P_K,
\quad
p(R)=PASS,
$$

則可稱：

$$
R\models\mathcal K_P.
$$

---

# 50. 雙生 runtime 的等價條件

若：

$$
R_G\models\mathcal K_P
$$

且：

$$
R_N\models\mathcal K_P,
$$

並且對共同 scenario set：

$$
\mathcal X
=
\{x_1,\ldots,x_m\},
$$

滿足：

$$
\forall x\in\mathcal X,
\quad
\alpha_G(R_G(x))
=
\alpha_N(R_N(x)),
$$

則可稱它們為：

$$
\boxed{
TwinSemanticImplementations.
}
$$

---

# 51. 可證偽命題

## H1

若沒有 Portable Semantic Kernel，雙生 runtime 長期演化後的 semantic drift 會顯著高於存在 kernel + conformance suite 的架構。

## H2

跨 runtime migration 的主要 correctness 問題不來自資料格式差異，而來自 identity、authority、history 與 verification semantics 的遺失。

## H3

在允許 feature divergence 的前提下，semantic kernel 比 source-code sharing 更能維持長期產品身份一致性。

## H4

Native Runtime 越 deeply integrated，越需要硬性 semantic separation 來避免 capability、authority、observation 與 commit 被錯誤合併。

## H5

General-OS Runtime 越 fragmented，越需要 portable identity / lineage 來維持跨 database、filesystem、browser 與 API 的統一 organizational state。

---

# 52. 工程議程

PSK 後續工程應至少產生：

1. `psk-core.schema`；
2. delegation contract；
3. authority contract；
4. verification contract；
5. receipt contract；
6. migration manifest；
7. loss manifest；
8. conformance probe suite；
9. semantic fingerprint；
10. compatibility report。

---

# 53. 與本系列後續論文的關係

本篇回答：

> 兩條 runtime 到底必須共享什麼？

下一篇將回答：

> 為什麼 General-OS Runtime 本身就是長期商業產品，而不只是 Native Runtime 的前置版本？

即：

**03｜《面向既有作業系統的 AI-Native Organization Runtime：Windows-First 相容層與商業部署模型》**

第四篇再處理：

**04｜《World-Native Agent Organization：HDUS 中的原生 ANDO 與橋接層消解》**

第五篇則處理兩者的 migration、interop 與 co-evolution。

---

# 54. 結論

本文提出 Portable Semantic Kernel，作為 ANDO 雙生產品線真正共享的身份核心。

其核心不是：

```text
same code
same database
same UI
same operating system
```

而是：

$$
\boxed{
SameIdentitySemantics
+
SameAuthoritySemantics
+
SameDelegationSemantics
+
SameVerificationSemantics
+
SameHistorySemantics
+
SameCommitSemantics.
}
$$

因此：

$$
\boxed{
GeneralOSRuntime
\neq
NativeRuntime
}
$$

在 representation level 上成立；

但：

$$
\boxed{
\alpha_G(R_G)
=
\alpha_N(R_N)
}
$$

應在 Portable Semantic Kernel domain 上盡可能成立。

這使雙生架構可以同時追求兩件原本容易互相衝突的目標：

$$
FeatureDivergence
\uparrow
$$

以及：

$$
SemanticDrift
\downarrow.
$$

最終，Portable Semantic Kernel 不是為了阻止 runtime 演化，而是為了讓兩條 runtime 可以放心演化，卻仍知道自己是誰。

---

## 文件狀態

- **系列：** ANDO Twin Runtime Series
- **篇次：** 02 / 05
- **版本：** v0.1
- **狀態：** 公開初稿
- **上一篇：** 《雙生 Agent 組織運行架構：通用 Runtime 與 Native Runtime 的分化》
- **下一篇：** 《面向既有作業系統的 AI-Native Organization Runtime：Windows-First 相容層與商業部署模型》
