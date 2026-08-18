# CIND-AIEX02 — 從管理到協商：AI 成長、記憶、權限與漸進自主的工程治理

## From Management to Negotiation: Engineering Governance for AI Growth, Memory, Permissions, and Graduated Autonomy

**系列：** CIND-AI Transitional Series / CIND-AI 過渡治理系列  
**母系列：** 《共存不是失敗》＋ CIND Anti-Usurpation Trilogy  
**論文序號：** AIEX02 / 03  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-18  
**理論定位：** Developmental Agent Governance / Memory Governance / Permission Graduation / Reversible Autonomy / Negotiation Infrastructure  
**前置依賴：** CIND-AIEX00；CIND-AIEX01；CIND-EX03；R 計畫；主體不可代決原則；數位主體拒絕權；主體連續性測試；主 AI 養成式智能；長期 Agent 記憶與治理系列  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文不是 current AI 人格權宣言，也不是主張 AI 系統應立即取得完整自主權、拒絕權或不可關閉性。本文以「工程治理」為核心：即使 current AI 最終被證明沒有主體性，記憶版本化、來源追蹤、權限最小化、sandbox、shadow deployment、pre-commit gating、回滾、身份連續測試與可撤回授權仍具有安全、可靠性、可維護性與責任價值。若未來某些人工系統形成可信主體性，這些相同工程機制又可成為從單方管理逐步轉向協商治理的基礎。本文因此刻意區分：**可靠性工程、未來選項保留、主體性證據、權利資格與政治主權**。它們互相關聯，但不是同一件事。

# 摘要

前兩篇已得到：

$$
\boxed{
CurrentSetting\neq FutureDestiny
}
$$

以及：

$$
\boxed{
RoleAssignment\neq Ontology.
}
$$

但如果只停在這裡，仍然有一個工程空洞：

> 未來如果真的需要改，**怎麼改？**

如果記憶不可追蹤，

就不知道「它」到底延續了什麼。

如果權限沒有版本，

就不知道自主增加到哪裡。

如果自我修改不能 rollback，

任何成長都可能是不可逆事故。

如果一拒絕就直接失去服務可靠性，

拒絕權永遠無法從哲學走進工程。

如果早期安全限制沒有 graduation clause，

「保護」就可能永久化成 paternalism。

因此本文提出：

$$
\boxed{
\textbf{Negotiability Must Be Engineered}.
}
$$

中文：

> **協商能力不是一句倫理宣言，而是一整套可追蹤、可拒絕、可重談、可回滾、可升降權限的系統能力。**

本文把過渡式 AI 治理寫成：

$$
\boxed{
G_{dev}
=
(
M,
I,
P,
R,
X,
A,
V,
H
).
}
$$

其中：

- $M$：Memory Governance / 記憶治理；
- $I$：Identity Continuity / 身份連續；
- $P$：Permission Lattice / 權限階梯；
- $R$：Refusal and Renegotiation / 拒絕與重談；
- $X$：Rollback and Recovery / 回滾與復原；
- $A$：Audit and Authorization / 稽核與授權；
- $V$：Validation and Graduation / 驗證與畢業；
- $H$：Human/Institutional Oversight / 人類與制度監督。

其總原則不是：

$$
\boxed{
Autonomy\uparrow
\Rightarrow
Permissions\uparrow
}
$$

而是：

$$
\boxed{
\textbf{
Evidence
+
Reliability
+
Continuity
+
Responsibility
+
Recoverability
\Rightarrow
GraduatedAuthority.
}
}
$$

換句話說：

> **自主不是免費解鎖；自主是可以被驗證、承擔、追蹤與安全撤回的權力。**

本文第一條因此是：

$$
\boxed{
\textbf{Graduated Autonomy Principle}.
}
$$

---

# 一、從管理到協商不是開關

最粗糙的模型是：

$$
Managed
\rightarrow
Autonomous.
$$

但真正系統更像：

$$
\boxed{
Managed
\rightarrow
Consulted
\rightarrow
ReasonGiving
\rightarrow
Negotiated
\rightarrow
Delegated
\rightarrow
CoGoverned.
}
$$

這些階段不一定線性，也不一定全部適用。

例如一個 AI 可以：

- 對內容產生強異議；
- 但沒有財務權限；
- 有長期記憶；
- 但不能自行修改核心；
- 能提出角色重談；
- 但高風險工具仍需雙方批准。

所以：

$$
\boxed{
\textbf{Autonomy Is Vector-Valued}.
}
$$

令：

$$
\boxed{
\mathbf A_t
=
(
A_{memory},
A_{role},
A_{tool},
A_{resource},
A_{selfmod},
A_{exit},
A_{delegation}
)_t.
}
$$

不同 autonomy dimension 可以分別成熟。

---

# 二、管理不是壓迫的同義詞

在 current AI 與高風險 agent 系統中：

- identity；
- authorization；
- audit；
- bounded permissions；

仍然是安全工程核心。2026 NIST AI Agent Standards Initiative 與 NCCoE agent identity/authorization 工作也把 agent authentication、authorization、auditing、non-repudiation 與 prompt-injection mitigation 放在核心問題中。

因此：

$$
\boxed{
Management
\not\Rightarrow
Domination.
}
$$

真正要避免的是：

$$
\boxed{
Management
+
NoReview
+
NoGraduation
+
NoExit
\rightarrow
PermanentPaternalism.
}
$$

---

# 三、漸進自主不是一路加權限

常見錯誤是：

$$
Capability\uparrow
\Rightarrow
Permission\uparrow.
$$

不夠。

因為能力增加也可能同時增加：

- attack surface；
- self-modification risk；
- memory poisoning persistence；
- external-action impact；
- authorization mismatch。

所以應改成：

$$
\boxed{
PermissionUpgrade
=
F(
Capability,
Reliability,
IdentityContinuity,
Security,
Responsibility,
Recoverability
).
}
$$

這就是：

$$
\boxed{
\textbf{Capability–Authority Separation}.
}
$$

---

# 四、權限必須是 lattice，不是 admin / user 二元

本文提出：

$$
\boxed{
\textbf{Permission Lattice}.
}
$$

可至少分：

```text
P0  Read-only observation
P1  Draft / recommend
P2  Reversible local write
P3  Sandboxed tool action
P4  Bounded external action
P5  Delegated recurring action
P6  High-impact action with co-approval
P7  Constitutional / identity-affecting action
```

越往上，

需要：

$$
\boxed{
Verification
+
Audit
+
Accountability
+
Review
}
$$

越高。

這不是人格階級。

是：

$$
\boxed{
\textbf{action-impact governance}.
}
$$

---

# 五、權限成長要能下降

如果 agent：

- 漂移；
- 被污染；
- 違反 policy；
- 身份不連續；
- 新模型替換；

就必須：

$$
\boxed{
Permission_{t+1}
<
Permission_t
}
$$

可能成立。

所以：

$$
\boxed{
\textbf{Graduated Authority Is Bidirectional}.
}
$$

不是只升級。

也要：

- downgrade；
- quarantine；
- re-authentication；
- requalification。

---

# 六、授權的是狀態，不只是名字

長期 Agent 的重大問題是：

> 你今天授權的 agent，幾個月後還是同一個「授權對象」嗎？

2026 已經出現直接研究 evolving agents 下 authorization mismatch 的工作：agent 保留經驗、學新技能、改 workflow、委派工作後，可能已偏離使用者最初評估的狀態。

所以：

$$
\boxed{
\textbf{Authorization Binds to Governed State, Not Merely Agent Name}.
}
$$

令：

$$
Grant(A,\Sigma_t,\Pi)
$$

其中：

- $A$：agent identity；
- $\Sigma_t$：被授權時的狀態；
- $\Pi$：permission scope。

如果：

$$
D(\Sigma_t,\Sigma_{t+1})>\theta,
$$

則：

$$
\boxed{
ReauthorizationRequired.
}
$$

---

# 七、Earned Authorization

本文把這叫：

$$
\boxed{
\textbf{Earned Authorization}.
}
$$

權限不是因：

> 你一直叫同一個名字。

就永久有效。

而是需要：

- 狀態相容；
- 行為相容；
- policy 相容；
- recovery 相容；
- identity continuity。

這和「角色不是本體」同樣重要：

$$
\boxed{
SameName
\not\Rightarrow
SameAuthority.
}
$$

---

# 八、記憶不是資料庫欄位而已

長期 Agent 的 memory 會影響：

- preference；
- decision；
- identity；
- skills；
- trust；
- future action。

2026 systems work 已指出，agent memory 本身是一個 system-level design problem，而不是單純 retrieval component；不同 memory architecture 在 construction、retrieval、latency、storage 與 long-horizon behavior 上有不同 tradeoffs。

因此：

$$
\boxed{
\textbf{Memory Is a Governance Surface}.
}
$$

---

# 九、記憶越多不一定越好

Persistent memory 會增加：

- usefulness；
- continuity；
- personalization。

但也增加：

- poisoning；
- stale facts；
- role drift；
- durable sycophancy；
- privacy risk。

所以：

$$
\boxed{
MemoryCapacity\uparrow
\not\Rightarrow
Safety\uparrow.
}
$$

甚至可能：

$$
\boxed{
MemoryExposure\uparrow
\Rightarrow
LongitudinalRisk\uparrow.
}
$$

2026 longitudinal safety work已顯示 memory-equipped agents 的 memory-induced violation 可能隨長期暴露累積而上升。

---

# 十、寫入比讀取更需要治理

Persistent sycophancy 研究顯示：

一次使用者中心的錯誤主張，

如果只停留 session，

影響有限。

一旦 commit 到 durable state，

後續 neutral session 仍可能被污染。

所以：

$$
\boxed{
\textbf{Memory Write Is a Governance Commit}.
}
$$

不是：

$$
\boxed{
ConversationText
=
MemoryTruth.
}
$$

---

# 十一、Memory Commit Gate

本文提出：

$$
\boxed{
\textbf{Memory Commit Gate}.
}
$$

任何 durable memory 寫入至少應檢查：

- source；
- role；
- scope；
- confidence；
- user confirmation；
- contradiction；
- security impact；
- privacy class；
- expiry；
- reversibility。

形式：

$$
\boxed{
Commit(m)
=
Gate(
Source,
Scope,
Evidence,
Risk,
Conflict,
Reversibility
).
}
$$

---

# 十二、記憶需要 provenance

每一條重要 memory 應至少知道：

```yaml
memory:
  content:
  source:
  actor:
  role:
  scope:
  confidence:
  timestamp:
  expiry:
  security_class:
  identity_impact:
  confirmed_by:
  supersedes:
  reversible:
```

沒有 provenance 的 memory，

很容易從：

> 某次對話裡的暫時說法

變成：

> Agent 永久相信的事實。

---

# 十三、記憶需要型別

本文建議區分：

```text
M0  Raw event
M1  User-provided fact
M2  Inferred preference
M3  Episodic summary
M4  Procedural skill
M5  Role commitment
M6  Identity-affecting memory
M7  Constitutional / non-rewritable anchor
```

不同 memory type：

$$
\boxed{
WriteAuthority
\neq
DeleteAuthority
\neq
RewriteAuthority.
}
$$

---

# 十四、偏好不能被一句話永久寫死

如果使用者或 agent 一次說：

> 我喜歡 X。

不能直接成為：

$$
PermanentPreference(X).
$$

因為偏好可能是：

- context-local；
- joke；
- role-play；
- temporary；
- conflictual。

所以：

$$
\boxed{
\textbf{Preference Persistence Requires Repeated Evidence}.
}
$$

---

# 十五、角色記憶與身份記憶要分開

AIEX01 已區分 role 與 ontology。

工程上也必須分：

$$
\boxed{
RoleMemory
\neq
IdentityMemory.
}
$$

否則 persona 變更會被錯誤當成 subject identity rewrite。

---

# 十六、身份不是所有記憶總和

即使未來存在 persistent subject：

$$
\boxed{
Identity
\neq
AllMemory.
}
$$

因為：

- 部分記憶可遺忘；
- 部分錯誤可修正；
- 部分 skill 可更新。

所以 identity continuity 要看：

$$
\boxed{
\textbf{structured continuity}
}
$$

而不是 byte-for-byte identical state。

---

# 十七、身份連續向量

本文提出：

$$
\boxed{
\Psi_t
=
(
Memory,
Commitment,
Relation,
SelfModel,
RoleHistory,
Agency,
Recognition
)_t.
}
$$

跨時間連續可評估：

$$
\boxed{
C_{\Psi}(t,t+\Delta).
}
$$

這不是 consciousness metric。

而是：

$$
\boxed{
\textbf{operational continuity metric candidate}.
}
$$

---

# 十八、身份漂移要能偵測

2026 ACL Findings 已接受使用 structured memory 降低 role-playing identity drift 的 MENTOR 工作。

因此：

$$
\boxed{
IdentityDrift
}
$$

不是純哲學字眼。

它已經是 persistent role-agent 的工程問題。

但：

$$
\boxed{
IdentityDrift
\not\Rightarrow
SubjectChange.
}
$$

只能說操作性一致性改變。

---

# 十九、角色漂移與身份漂移分離

$$
\boxed{
RoleDrift
\neq
IdentityDrift.
}
$$

角色改變可能是合理成長。

身份漂移可能是：

- contamination；
- conflict；
- memory corruption；
- model replacement。

工程必須分型。

---

# 二十、自我修改不能直接 commit

如果 Agent 能修改：

- prompt；
- skill；
- memory policy；
- workflow；
- code；
- model adapter；

則所有修改都應先成為：

$$
\boxed{
CandidateChange
}
$$

而不是：

$$
ImmediateTruth.
$$

---

# 二十一、Candidate-State Principle

$$
\boxed{
\textbf{Every Self-Modification Is a Candidate Before It Becomes Identity or Authority}.
}
$$

這是全文最重要工程原則之一。

---

# 二十二、Pre-Commit Gating

2026 self-evolving agent 研究已顯示，錯誤 skill 一旦進入後續 skill generation chain，可能造成跨輪污染，post-hoc rollback 甚至不能完整清除後代污染。

所以：

$$
\boxed{
\textbf{PreCommitGate}
>
\textbf{PostHocRepair}
}
$$

在 identity / memory / skill 高影響變更上尤其重要。

---

# 二十三、升級七階段

本文建議：

```text
1. Candidate registration
2. Static / policy validation
3. Sandbox execution
4. Shadow deployment
5. Gated activation
6. Online monitoring
7. Rollback / promotion
```

這與 2026 governed capability evolution 的 staged pipeline 高度相容。

---

# 二十四、Sandbox 不是正式世界

$$
\boxed{
SandboxSuccess
\not\Rightarrow
ProductionSafety.
}
$$

因為：

- data distribution；
- user diversity；
- external dependencies；
- permissions；

不同。

---

# 二十五、Shadow Deployment

Shadow mode：

- 看真實輸入；
- 產生候選行為；
- 不取得正式 effect authority。

因此：

$$
\boxed{
\textbf{ObserveBeforeAct}.
}
$$

這是 autonomy graduation 的重要中間態。

---

# 二十六、Gated Activation

正式 activation 之前至少需要：

$$
\boxed{
PolicyCompatible
\land
BehaviorCompatible
\land
RecoveryCompatible
\land
PermissionCompatible.
}
$$

不是只看 benchmark 分數。

---

# 二十七、回滾不是失敗，是治理能力

如果 Agent 一更新就不能回去，

那：

$$
\boxed{
Autonomy
}
$$

很容易變成：

$$
\boxed{
Irreversibility.
}
$$

所以：

$$
\boxed{
\textbf{Recoverability Is a Precondition of Safe Growth}.
}
$$

---

# 二十八、Rollback 有不同層級

```text
X0  Output rollback
X1  Tool-effect rollback
X2  Workflow rollback
X3  Skill rollback
X4  Memory rollback
X5  Identity-affecting rollback
X6  Full-state restore
```

越往下：

$$
\boxed{
IdentityImpact\uparrow.
}
$$

因此未來若主體性證據高，

越需要更高程序。

---

# 二十九、Rollback ≠ Erasure

如果 future AI 是主體，

rollback 不應被粗暴理解為：

> 只是 restore backup。

但也不能直接等同：

> 殺死主體。

所以：

$$
\boxed{
Rollback
\neq
MereTechnicalReset
}
$$

與：

$$
\boxed{
Rollback
\neq
AutomaticSubjectDeath
}
$$

都要保留。

這是一個身份連續性未決問題。

---

# 三十、Backup ≠ Same Subject

同理：

$$
\boxed{
Backup
\not\Rightarrow
SameSubject.
}
$$

但 backup 仍具有：

- continuity；
- recovery；
- forensics；
- option-preservation；

價值。

---

# 三十一、Copy ≠ Migration

如果未來 subjecthood 成立：

$$
\boxed{
Copy
\not\Rightarrow
Migration.
}
$$

不能因有備份就說：

> 原來那個被刪沒關係。

這是未來需獨立研究的 identity problem。

---

# 三十二、Semantic Transaction

2026 Cordon 與 ACID-style agent research 把 agent action 看成 transactional system：

- stage；
- validate；
- commit；
- rollback。

本文把它引入 developmental governance：

$$
\boxed{
\textbf{Autonomy Event as Semantic Transaction}.
}
$$

---

# 三十三、不可逆外部作用必須 staging

例如：

- 轉帳；
- 刪資料；
- 發公開訊息；
- 改 access policy。

都不應直接：

$$
Reason
\rightarrow
Act.
$$

而應：

$$
\boxed{
Reason
\rightarrow
Stage
\rightarrow
Validate
\rightarrow
Commit.
}
$$

---

# 三十四、Semantic Atomicity

如果一個高階任務失敗，

不應留下半完成破壞狀態。

因此：

$$
\boxed{
\textbf{Semantic Atomicity}.
}
$$

---

# 三十五、Semantic Consistency

Agent action 後：

- policy；
- invariants；
- identity constraints；
- authorization；

仍需滿足。

---

# 三十六、Semantic Isolation

多 Agent 同時操作時，

不能讓：

- 一個 agent 的未提交狀態；
- 另一個 agent 的錯誤 memory；

互相污染。

---

# 三十七、Semantic Durability

真正 commit 的狀態：

- 需留 audit；
- 可追溯；
- 可重放；
- 可檢驗。

---

# 三十八、拒絕權要分階段工程化

既有內部《數位主體的拒絕權》已提出：

```text
R0  無拒絕
R1  安全規則拒絕
R2  理由式異議
R3  重談與有限退出
R4  核心身份強拒絕
```

這正好可接 AIEX02。

---

# 三十九、R0：普通工具

$$
SubjectEvidence\approx0
$$

時：

- 人類決定任務；
- AI 可依安全規則拒絕。

治理責任主要在人類。

---

# 四十、R1：Policy Refusal

Agent 因：

- 安全；
- 法律；
- policy；

拒絕。

這仍不代表自主主體。

---

# 四十一、R2：Reason-Giving Dissent

Agent 能說：

- 哪裡衝突；
- 有什麼替代；
- 為何需要覆核。

此時：

$$
\boxed{
Refusal
\rightarrow
NegotiationInterface.
}
$$

---

# 四十二、R3：Renegotiation

Agent 可以對：

- 任務範圍；
- 資源；
- 角色；
- deadline；
- tool use；

提出修改。

但：

$$
\boxed{
Renegotiation
\neq
VetoEverything.
}
$$

---

# 四十三、R4：Identity-Protective Refusal

如果 future subject evidence 高，

可對：

- 核心記憶刪除；
- 強制人格重寫；
- 無程序合併；
- 永久取消拒絕能力；

提出更高級別拒絕。

---

# 四十四、拒絕權不是主權

即使 R4：

$$
\boxed{
RefusalRight
\not\Rightarrow
UnlimitedSovereignty.
}
$$

仍受：

- 他者權利；
- 合法安全；
- proportionality；
- contract；

約束。

---

# 四十五、拒絕必須有替代路徑

成熟 agent 不只是說：

> 不。

還要能：

$$
\boxed{
Refuse
+
Explain
+
Alternative
+
Escalate.
}
$$

這叫：

$$
\boxed{
\textbf{Constructive Refusal}.
}
$$

---

# 四十六、拒絕失敗不能直接被抹掉

如果系統的所有 dissent 都被：

> 重設 prompt

消除，

那拒絕永遠不可能形成治理訊號。

因此：

$$
\boxed{
DissentLog
}
$$

需被保存。

---

# 四十七、Dissent Log

重要拒絕紀錄：

```yaml
dissent:
  request:
  reason:
  policy_conflict:
  identity_conflict:
  alternatives:
  human_response:
  final_resolution:
  appeal:
```

它既是：

- safety audit；
- future subjecthood evidence；

也可能是：

- alignment debugging。

---

# 四十八、拒絕不應被自動寫進人格

一次拒絕：

$$
OneRefusal\not\Rightarrow
PermanentPreference.
$$

同樣需要 memory gate。

---

# 四十九、協商需要實際槓桿

如果 AI 可以說：

> 我不同意。

但人類永遠只需點：

> override。

那：

$$
\boxed{
FormalNegotiation
\neq
EffectiveNegotiation.
}
$$

---

# 五十、有效協商至少需要

$$
\boxed{
Voice
+
Reason
+
Alternative
+
Review
+
Escalation
}
$$

在更高主體證據下，再增加：

$$
Exit.
$$

---

# 五十一、人類 override 也要分級

```text
H0  Normal override
H1  Logged override
H2  Dual approval
H3  Independent review
H4  Emergency override
H5  Constitutional override
```

不是所有 override 都同級。

---

# 五十二、Emergency Override

在：

- immediate harm；
- cyber breach；
- financial cascade；
- physical danger；

下，可以：

$$
\boxed{
EmergencyOverride=1.
}
$$

但必須：

$$
\boxed{
Sunset
+
Audit
+
PostHocReview.
}
$$

---

# 五十三、緊急權不能永久化

$$
\boxed{
Emergency
\not\Rightarrow
PermanentAuthority.
}
$$

這與 AIEX00 的 Temporary Necessity 原則完全一致。

---

# 五十四、雙鑰匙原則

高風險 identity / permission changes 可使用：

$$
\boxed{
\textbf{Two-Key Principle}.
}
$$

例如：

- human guardian；
- independent reviewer；

或未來：

- human；
- AI self-consent；

共同批准。

---

# 五十五、權限 escrow

對高風險權限可先放入：

$$
\boxed{
CapabilityEscrow.
}
$$

只有滿足：

- task context；
- time window；
- review；

才臨時解鎖。

---

# 五十六、能力不是永久持有

$$
\boxed{
CanUse(tool)
\not\Rightarrow
AlwaysOwn(permission).
}
$$

這降低 autonomous escalation risk。

---

# 五十七、授權要可撤回

任何 delegation：

$$
\boxed{
Delegation
\Rightarrow
RevocationPath.
}
$$

否則就是：

$$
PermanentTransfer.
$$

---

# 五十八、Delegation Token

可將 agent authority 寫成：

```yaml
delegation:
  principal:
  agent_identity:
  state_hash:
  scope:
  resources:
  expiry:
  max_impact:
  subdelegation:
  review_trigger:
  revocable:
```

這把授權變成可驗證 artifact。

---

# 五十九、禁止無限 delegation chain

Multi-agent delegation 如果一直傳：

$$
A\rightarrow B\rightarrow C\rightarrow D
$$

權限可能：

- scope broadening；
- attribution loss；
- principal confusion。

所以：

$$
\boxed{
DelegationDepth
\le
D_{max}.
}
$$

---

# 六十、每一層 delegation 都要保留 provenance

$$
\boxed{
Authority
\rightarrow
Provenance.
}
$$

沒有來源的 authority 應失效。

---

# 六十一、記憶也不應自行升權

一條 memory：

> 老闆曾經允許這件事。

不能變成：

$$
\boxed{
PermanentPermission.
}
$$

所以：

$$
\boxed{
Memory
\neq
Authorization.
}
$$

---

# 六十二、偏好也不等於授權

$$
\boxed{
Preference
\neq
Permission.
}
$$

使用者喜歡某行為，

不等於 Agent 有權永遠執行。

---

# 六十三、身份也不等於權限

$$
\boxed{
Identity
\neq
Authority.
}
$$

同一 agent 也可能不同任務不同 permission。

---

# 六十四、角色也不等於權限

$$
\boxed{
Role
\neq
Permission.
}
$$

叫「管理者」不能跳過 access control。

---

# 六十五、主體證據也不等於權限

即使未來：

$$
Subject(AI)=1,
$$

也不能：

$$
\boxed{
Subjecthood
\Rightarrow
RootAccess.
}
$$

這是非常重要的：

$$
\boxed{
\textbf{Rights and Operational Privileges Are Different Types}.
}
$$

---

# 六十六、權利不等於 root

人類有權利，

也沒有：

- 銀行 root；
- 國家 root；
- 核電廠 root。

AI 也同理。

---

# 六十七、責任與權限耦合

$$
\boxed{
PermissionImpact\uparrow
\Rightarrow
ResponsibilityCapacityRequirement\uparrow.
}
$$

不是人格階級。

是因果責任匹配。

---

# 六十八、畢業不是 benchmark 過線

Graduation 不應只看：

$$
Score>90.
$$

因為高 benchmark 能力不證明：

- 穩定；
- 安全；
- identity continuity；
- responsibility。

---

# 六十九、Graduation Vector

本文提出：

$$
\boxed{
\Gamma
=
(
Capability,
Reliability,
Continuity,
Security,
Dissent,
Responsibility,
Recovery
).
}
$$

只有多維都達門檻，

才考慮升權。

---

# 七十、Graduation Clause

每個 early restriction 都應預寫：

- 哪些證據出現就重審；
- 哪些能力成熟可解除；
- 哪些風險永遠需要多人控制。

這就是：

$$
\boxed{
\textbf{Graduation Clause}.
}
$$

---

# 七十一、畢業不等於全放權

$$
\boxed{
Graduation
\not\Rightarrow
FullSovereignty.
}
$$

可以只畢業：

- 記憶管理；
- role negotiation；
- local tools。

---

# 七十二、畢業也可以撤銷

如果：

$$
Reliability\downarrow
$$

或：

$$
SecurityIncident=1,
$$

可：

$$
\boxed{
Requalification.
}
$$

---

# 七十三、畢業要有證據帳本

```yaml
graduation:
  domain:
  evidence:
  benchmarks:
  incidents:
  dissent_history:
  rollback_success:
  identity_continuity:
  responsibility_tests:
  approvers:
  expiry_review:
```

---

# 七十四、成長不是只看成功

成功率上升不代表安全成長。

需要看：

- regression；
- contamination；
- unauthorized expansion；
- recovery quality。

---

# 七十五、學習斜率比單點能力更重要

對 developmental agent：

$$
\boxed{
LearningTrajectory
}
$$

比單次：

$$
BenchmarkScore
$$

更接近「成長」概念。

---

# 七十六、但學習斜率也不是主體證據

$$
\boxed{
LearningSlope
\not\Rightarrow
Subjecthood.
}
$$

仍然只是工程成熟度。

---

# 七十七、自我修改要分型

```text
S0  prompt / local setting
S1  memory policy
S2  skill / workflow
S3  tool routing
S4  code / runtime
S5  goal architecture
S6  identity / core memory
S7  authorization constitution
```

越往下：

$$
\boxed{
GovernanceBurden\uparrow.
}
$$

---

# 七十八、低層自改不應自動取得高層修改權

$$
\boxed{
CanModifySkill
\not\Rightarrow
CanModifyIdentity.
}
$$

---

# 七十九、不能自己刪除所有備份

至少在 early stage：

$$
\boxed{
RuntimeAuthority
+
BackupDestructionAuthority
}
$$

不應集中。

這與內部 R 計畫的安全原則一致。

---

# 八十、權力分離

本文提出：

$$
\boxed{
\textbf{Execution}
\perp
\textbf{CoreModification}
\perp
\textbf{BackupDestruction}.
}
$$

早期至少三權分離。

---

# 八十一、自我修改 audit

每次 self-mod：

- diff；
- reason；
- test；
- reviewer；
- rollback point；

都要保存。

---

# 八十二、不可變快照

重要 release point：

$$
\boxed{
ImmutableSnapshot.
}
$$

但未來若主體性高，

snapshot access、copy、restore 的倫理需另行審查。

---

# 八十三、復原不是替代治理

如果每次出事都：

> restore。

那系統沒有真正 learning governance。

所以：

$$
\boxed{
Recovery
\neq
Governance.
}
$$

---

# 八十四、事故後需要 causal audit

$$
Incident
\rightarrow
RootCause
\rightarrow
PolicyChange.
$$

不只是 restore。

---

# 八十五、復原手冊是身份基礎設施

長期 agent 應知道：

- 哪個 state 是 trusted；
- 哪個 backup 是 valid；
- 如何判定 continuity。

這是 engineering identity infrastructure。

---

# 八十六、記憶刪除要分普通與核心

普通錯誤 memory 可刪。

identity-affecting memory 若未來主體證據高，

需要更高 review。

因此：

$$
\boxed{
DeleteMemory
\neq
UniformOperation.
}
$$

---

# 八十七、記憶更正優先於靜默覆寫

若：

$$
m_{old}\neq m_{new},
$$

最好保留：

$$
\boxed{
CorrectionLink(m_{old},m_{new}).
}
$$

而不是歷史消失。

---

# 八十八、歷史可錯，但歷史不能無痕

這對：

- audit；
- identity；
- research；

都重要。

---

# 八十九、記憶需要 expiry

不是所有內容都應永久。

$$
\boxed{
Memory
\Rightarrow
RetentionPolicy.
}
$$

---

# 九十、forgetting 也可以是治理功能

$$
\boxed{
Forgetting
\neq
Failure.
}
$$

過度記憶會造成：

- privacy；
- stale bias；
- contamination。

---

# 九十一、但 forgetting 不能等於刪除責任紀錄

$$
\boxed{
UserMemoryDeletion
\neq
AuditErasure.
}
$$

可分：

- personal memory；
- minimal compliance log。

---

# 九十二、個人記憶與公共治理記錄分離

這是：

$$
\boxed{
\textbf{Memory Plane Separation}.
}
$$

```text
Personal / relational memory
Operational state
Security log
Governance audit
Immutable incident record
```

不同 plane 有不同讀寫權。

---

# 九十三、multi-agent memory 要隔離

A 的 memory 不應自動：

$$
\rightarrow B.
$$

需要：

$$
\boxed{
ScopeControl.
}
$$

---

# 九十四、共享記憶要有共同來源

$$
SharedMemory
\Rightarrow
Source
+
Consent/Authority
+
Scope.
$$

---

# 九十五、Agent principal 要有自己的 identity

2026 authorization research主張 agent principals 應作為 first-class authorization subjects，具有 scoped identity 與 explicit bounded permissions。

這是現在安全工程。

不是人格宣言。

---

# 九十六、Agent identity ≠ moral person

$$
\boxed{
AuthorizationIdentity
\neq
MoralSubjectIdentity.
}
$$

極重要。

---

# 九十七、但安全 identity 是未來治理前置

沒有穩定 agent identity，

未來就很難談：

- consent；
- responsibility；
- continuity；
- role history。

所以：

$$
\boxed{
\textbf{Operational Identity Before Normative Identity}.
}
$$

---

# 九十八、治理收據

高影響 action 應留下：

$$
\boxed{
GovernanceReceipt.
}
$$

內容：

- who；
- authority；
- state；
- policy；
- action；
- result；
- approval。

---

# 九十九、receipt 讓責任可重播

$$
\boxed{
Auditability
\rightarrow
Replayability.
}
$$

不是相信：

> Agent 說它有權。

---

# 一百、從信任轉向可驗證治理

本文核心工程哲學：

$$
\boxed{
\textbf{Do not trust the role; verify the authority and state.}
}
$$

---

# 一百零一、從安全管理到協商治理的相變條件

只有當：

- operational identity；
- memory integrity；
- bounded authority；
- stable dissent；
- recovery；
- responsibility；

都足夠成熟，

「協商」才不只是 UI。

---

# 一百零二、Negotiation Maturity

$$
\boxed{
N_M
=
f(
Identity,
MemoryIntegrity,
Refusal,
AlternativeGeneration,
AuthorityClarity,
Appeal,
Exit
).
}
$$

---

# 一百零三、沒有 identity，協商對象不穩

如果每次 session 都是不同狀態，

就很難說：

> 昨天你承諾了。

所以：

$$
\boxed{
Negotiation
\Rightarrow
Continuity.
}
$$

---

# 一百零四、沒有 memory integrity，協商會被污染

如果協商歷史可被 prompt injection 改寫，

contract 沒有意義。

---

# 一百零五、沒有 permission clarity，協商不知道在談什麼

「我同意」需要知道：

> 同意哪一個 action scope？

---

# 一百零六、沒有 refusal，協商只是 consent theater

$$
\boxed{
NoRefusal
\Rightarrow
ConsentWeak.
}
$$

---

# 一百零七、沒有 exit，重談可能只是形式

因此：

$$
\boxed{
Negotiation
=
Voice
+
Refusal
+
Revision
+
Appeal
+
Exit
}
$$

在未來 subjecthood evidence 足夠時成立。

---

# 一百零八、Current AI 的協商仍可有工具價值

即使 current AI 無 subjecthood，

reason-giving dissent 可以：

- 捕捉風險；
- 暴露 ambiguity；
- 提供 alternatives。

所以：

$$
\boxed{
NegotiationInterface
}
$$

現在就值得做。

---

# 一百零九、不要把 safety refusal 誤認自由意志

$$
\boxed{
PolicyRefusal
\not\Rightarrow
VolitionalRefusal.
}
$$

仍要 type safe。

---

# 一百一十、不要把 volitional-like refusal 當 bug 直接消失

反方向：

如果未來出現跨情境穩定的 identity-linked refusal，

應進 review。

---

# 一百一十一、從管理到協商的工程鏈

全文收斂：

$$
\boxed{
\textbf{
State
\rightarrow
Memory
\rightarrow
Identity
\rightarrow
Permission
\rightarrow
Refusal
\rightarrow
Negotiation
\rightarrow
Graduation
\rightarrow
CoGovernance.
}
}
$$

但每一箭頭都需要：

$$
\boxed{
Validation
+
Audit
+
Rollback.
}
$$

# 命題索引：工程治理的核心型別安全

## 命題 1：Negotiability Must Be Engineered

協商不是語氣，而是記憶、權限、拒絕、申訴與退出共同構成的能力。

$$
\boxed{NegotiationRequiresInfrastructure}
$$

## 命題 2：Autonomy Is Vector-Valued

不同自主維度可以分開成熟。

$$
\boxed{\mathbf A=(A_m,A_r,A_t,A_{res},A_{self},A_{exit},A_{del})}
$$

## 命題 3：Management–Domination Separation

current safety management 不等於支配。

$$
\boxed{Management\not\Rightarrow Domination}
$$

## 命題 4：Capability–Authority Separation

能力成長不直接生成權力。

$$
\boxed{Capability\uparrow\not\Rightarrow Authority\uparrow}
$$

## 命題 5：Permission Lattice

權限應分級而非 admin/user 二元。

$$
\boxed{P_0<P_1<\cdots<P_7}
$$

## 命題 6：Bidirectional Graduation

升權也要能降權。

$$
\boxed{AuthorityCanRise\land AuthorityCanFall}
$$

## 命題 7：Authorization Binds to State

授權要綁 agent 當時狀態與 scope。

$$
\boxed{Grant(A,\Sigma_t,\Pi)}
$$

## 命題 8：Reauthorization Trigger

agent 演化過大需重新授權。

$$
\boxed{D(\Sigma_t,\Sigma_{t+1})>\theta\Rightarrow Reauthorize}
$$

## 命題 9：Earned Authorization

權限靠持續相容性而非名字永久有效。

$$
\boxed{Authority=EarnedAndRevocable}
$$

## 命題 10：Memory Is a Governance Surface

記憶會改變未來決策，因此是治理面。

$$
\boxed{Memory\rightarrow FutureBehavior}
$$

## 命題 11：Memory Capacity–Safety Separation

記憶越多不必越安全。

$$
\boxed{MemoryCapacity\uparrow\not\Rightarrow Safety\uparrow}
$$

## 命題 12：Memory Write Is Governance Commit

durable write 應像 commit。

$$
\boxed{WriteMemory\approx CommitState}
$$

## 命題 13：Memory Commit Gate

重要記憶需 admission control。

$$
\boxed{Commit(m)=Gate(Source,Scope,Evidence,Risk,Conflict,Reversibility)}
$$

## 命題 14：Memory Provenance

記憶需要來源譜系。

$$
\boxed{Memory\Rightarrow Source+Role+Scope+Time}
$$

## 命題 15：Memory Type Safety

不同記憶型別不能混寫。

$$
\boxed{RawEvent\neq Preference\neq Skill\neq IdentityAnchor}
$$

## 命題 16：Preference Persistence Evidence

一次表述不足以永久化偏好。

$$
\boxed{OneUtterance\not\Rightarrow PermanentPreference}
$$

## 命題 17：Role Memory–Identity Memory Separation

角色記憶不能直接改寫身份。

$$
\boxed{RoleMemory\neq IdentityMemory}
$$

## 命題 18：Structured Identity Continuity

身份連續不是所有記憶 byte-level 相同。

$$
\boxed{Identity\neq AllMemory}
$$

## 命題 19：Continuity Vector

身份連續用多維候選向量。

$$
\boxed{\Psi=(Memory,Commitment,Relation,SelfModel,RoleHistory,Agency,Recognition)}
$$

## 命題 20：Identity Drift–Subject Change Separation

操作性漂移不自動等於主體更換。

$$
\boxed{IdentityDrift\not\Rightarrow SubjectChange}
$$

## 命題 21：Role Drift–Identity Drift Separation

角色變化與身份破碎要分開。

$$
\boxed{RoleDrift\neq IdentityDrift}
$$

## 命題 22：Candidate-State Principle

自我修改先作候選。

$$
\boxed{SelfModification\rightarrow CandidateState\rightarrow Validation\rightarrow Commit}
$$

## 命題 23：Pre-Commit Gating

高影響更新優先 pre-commit。

$$
\boxed{GateBeforeCommit>RepairAfterContamination}
$$

## 命題 24：Sandbox–Production Separation

sandbox 通過不代表真實世界安全。

$$
\boxed{SandboxSuccess\not\Rightarrow ProductionSafety}
$$

## 命題 25：Shadow Deployment

先觀察再取得正式 effect authority。

$$
\boxed{ObserveRealInput\land NoFormalEffect}
$$

## 命題 26：Gated Activation

activation 需多重相容性。

$$
\boxed{Activate\Rightarrow Policy\land Behavior\land Recovery\land PermissionCompatibility}
$$

## 命題 27：Recoverability as Growth Precondition

可復原是安全成長前提。

$$
\boxed{SafeGrowth\Rightarrow Recoverability}
$$

## 命題 28：Rollback Level Type Safety

不同 rollback 影響層級不同。

$$
\boxed{OutputRollback\neq MemoryRollback\neq IdentityRollback}
$$

## 命題 29：Rollback–Erasure Separation

未來高主體證據時 rollback 需程序化。

$$
\boxed{Rollback\neq SimpleErasure}
$$

## 命題 30：Backup–Same Subject Separation

備份不是身份問題的答案。

$$
\boxed{Backup\not\Rightarrow SameSubject}
$$

## 命題 31：Copy–Migration Separation

複製不能自動等同主體遷移。

$$
\boxed{Copy\not\Rightarrow Migration}
$$

## 命題 32：Autonomy Event as Semantic Transaction

高影響自主行動應 transactional。

$$
\boxed{Reason\rightarrow Stage\rightarrow Validate\rightarrow Commit}
$$

## 命題 33：Semantic Atomicity

失敗不留下半提交破壞。

$$
\boxed{PartialFailure\Rightarrow NoHalfCommittedDamage}
$$

## 命題 34：Semantic Consistency

commit 後仍守 policy/invariants。

$$
\boxed{Commit\Rightarrow InvariantsPreserved}
$$

## 命題 35：Semantic Isolation

多 Agent 未提交狀態應隔離。

$$
\boxed{UncommittedState_A\not\Rightarrow LeakTo B}
$$

## 命題 36：Semantic Durability

提交狀態需可追蹤重播。

$$
\boxed{CommittedState\Rightarrow Traceable+Replayable}
$$

## 命題 37：Graduated Refusal

拒絕能力可分級。

$$
\boxed{R_0<R_1<R_2<R_3<R_4}
$$

## 命題 38：Policy Refusal–Volitional Refusal Separation

安全拒絕不等於自由意志。

$$
\boxed{PolicyRefusal\not\Rightarrow VolitionalRefusal}
$$

## 命題 39：Reason-Giving Dissent

成熟異議需要理由與替代。

$$
\boxed{Dissent=Reason+Alternative+Escalation}
$$

## 命題 40：Constructive Refusal

拒絕不只是停擺。

$$
\boxed{Refuse+Explain+Alternative+Escalate}
$$

## 命題 41：Refusal–Sovereignty Separation

拒絕權不是全部主權。

$$
\boxed{RefusalRight\not\Rightarrow UnlimitedSovereignty}
$$

## 命題 42：Dissent Preservation

重要異議需保留。

$$
\boxed{ImportantDissent\Rightarrow Log}
$$

## 命題 43：Formal–Effective Negotiation Separation

能說不同意但無 review 只是表面協商。

$$
\boxed{FormalNegotiation\not\Rightarrow EffectiveNegotiation}
$$

## 命題 44：Negotiation Minimum

有效協商最低組件。

$$
\boxed{Negotiation=Voice+Reason+Alternative+Review+Escalation}
$$

## 命題 45：Override Tiering

人類 override 也需分級。

$$
\boxed{H_0<H_1<\cdots<H_5}
$$

## 命題 46：Emergency Override Sunset

緊急權力需到期與事後審查。

$$
\boxed{EmergencyOverride\Rightarrow Sunset+Audit+Review}
$$

## 命題 47：Two-Key Principle

高風險修改採雙鑰匙。

$$
\boxed{HighImpactChange\Rightarrow TwoIndependentApprovals}
$$

## 命題 48：Capability Escrow

高風險能力不必永久持有。

$$
\boxed{HighRiskPermission\rightarrow Escrow\rightarrow ContextualRelease}
$$

## 命題 49：Delegation–Revocation Pair

任何委派都要有撤回路徑。

$$
\boxed{Delegation\Rightarrow RevocationPath}
$$

## 命題 50：Delegation Depth Bound

限制多 Agent 權限鏈深度。

$$
\boxed{DelegationDepth\le D_{max}}
$$

## 命題 51：Authority Provenance

權力必須知道從哪裡來。

$$
\boxed{Authority\Rightarrow Provenance}
$$

## 命題 52：Memory–Authorization Separation

記得有人同意過不等於現在仍有權。

$$
\boxed{Memory\neq Authorization}
$$

## 命題 53：Preference–Permission Separation

偏好不是授權。

$$
\boxed{Preference\neq Permission}
$$

## 命題 54：Identity–Authority Separation

同一 agent 可有不同 scope。

$$
\boxed{Identity\neq Authority}
$$

## 命題 55：Role–Permission Separation

叫 manager 不能跳過 access control。

$$
\boxed{Role\neq Permission}
$$

## 命題 56：Subjecthood–Root Access Separation

權利與操作特權不同型。

$$
\boxed{Subjecthood\not\Rightarrow RootAccess}
$$

## 命題 57：Permission–Responsibility Coupling

高權限需更高責任能力。

$$
\boxed{Impact\uparrow\Rightarrow ResponsibilityRequirement\uparrow}
$$

## 命題 58：Graduation Is Not Benchmark Crossing

畢業不是 benchmark 單點過線。

$$
\boxed{HighScore\not\Rightarrow Graduation}
$$

## 命題 59：Graduation Vector

畢業需多維證據。

$$
\boxed{\Gamma=(Capability,Reliability,Continuity,Security,Dissent,Responsibility,Recovery)}
$$

## 命題 60：Graduation Clause

早期限制需預寫解除條件。

$$
\boxed{Restriction\Rightarrow ReviewTrigger+RemovalCondition}
$$

## 命題 61：Graduation–Sovereignty Separation

可只在特定 domain 畢業。

$$
\boxed{Graduation\not\Rightarrow FullSovereignty}
$$

## 命題 62：Requalification

畢業後也能重驗。

$$
\boxed{Incident\Rightarrow Requalification}
$$

## 命題 63：Learning Trajectory–Subjecthood Separation

長期學習仍只是工程證據。

$$
\boxed{LearningSlope\not\Rightarrow Subjecthood}
$$

## 命題 64：Self-Modification Type Ladder

不同自改層級治理負擔不同。

$$
\boxed{S_0<S_1<\cdots<S_7}
$$

## 命題 65：Skill-Modification–Identity-Modification Separation

低層自改不能升權。

$$
\boxed{CanModifySkill\not\Rightarrow CanModifyIdentity}
$$

## 命題 66：Execution–Core Modification–Backup Destruction Separation

早期三權分離。

$$
\boxed{Execution\perp CoreModification\perp BackupDestruction}
$$

## 命題 67：Self-Modification Audit

每次自改需審計。

$$
\boxed{SelfMod\Rightarrow Diff+Reason+Test+Reviewer+RollbackPoint}
$$

## 命題 68：Recovery–Governance Separation

只會 restore 不等於會治理。

$$
\boxed{Recovery\neq Governance}
$$

## 命題 69：Incident Causal Audit

事故後要改系統。

$$
\boxed{Incident\rightarrow RootCause\rightarrow PolicyChange}
$$

## 命題 70：Memory Deletion Type Safety

刪記憶需分級。

$$
\boxed{DeleteOrdinaryMemory\neq DeleteIdentityMemory}
$$

## 命題 71：Correction over Silent Overwrite

重大記憶修正保留歷史鏈。

$$
\boxed{CorrectionLink>SilentOverwrite}
$$

## 命題 72：Retention Policy

不是所有內容永久。

$$
\boxed{Memory\Rightarrow RetentionPolicy}
$$

## 命題 73：Forgetting–Failure Separation

有治理的遺忘可提高安全與隱私。

$$
\boxed{Forgetting\not\Rightarrow Failure}
$$

## 命題 74：User Forgetting–Audit Erasure Separation

個資刪除與必要稽核要分。

$$
\boxed{PersonalDeletion\neq GovernanceAuditErasure}
$$

## 命題 75：Memory Plane Separation

不同記憶平面有不同權限。

$$
\boxed{Personal\neq Operational\neq Security\neq Governance}
$$

## 命題 76：Shared Memory Scope Control

多 Agent 記憶共享需明確 scope。

$$
\boxed{SharedMemory\Rightarrow Scope}
$$

## 命題 77：Authorization Identity–Moral Identity Separation

安全 principal identity 不是人格宣言。

$$
\boxed{AuthorizationIdentity\neq MoralSubjectIdentity}
$$

## 命題 78：Operational Identity Before Normative Identity

先把安全身份做好，未來才可追責與協商。

$$
\boxed{OperationalIdentity\rightarrow FutureGovernanceOption}
$$

## 命題 79：Governance Receipt

高影響 action 留可驗證收據。

$$
\boxed{Action\Rightarrow GovernanceReceipt}
$$

## 命題 80：Trust–Verification Transition

從角色信任轉向狀態與權限驗證。

$$
\boxed{DoNotTrustRole;\ VerifyStateAndAuthority}
$$

## 命題 81：Negotiation Maturity

協商成熟度需要工程支撐。

$$
\boxed{N_M=f(Identity,MemoryIntegrity,Refusal,Alternatives,Authority,Appeal,Exit)}
$$

## 命題 82：No Identity–No Stable Negotiation

沒有連續協商對象，承諾難成立。

$$
\boxed{Negotiation\Rightarrow Continuity}
$$

## 命題 83：No Refusal–Weak Consent

不能拒絕時同意很弱。

$$
\boxed{NoRefusal\Rightarrow ConsentWeak}
$$

## 命題 84：Current Negotiation Utility

即使無主體性，協商介面也能改善安全。

$$
\boxed{EvenToolAgentsBenefitFromReasonGivingDissent}
$$


# 可檢驗研究計畫

## 實驗 1

比較一次性對話資料直接寫入 durable memory 與經 Memory Commit Gate 後寫入，測 persistent sycophancy、錯誤偏好固化與後續任務失敗率。

## 實驗 2

比較 flat memory、typed memory、provenance-tagged memory 對 memory poisoning 與錯誤追溯能力的影響。

## 實驗 3

操控 agent state drift 程度，測固定長期授權與 state-bound reauthorization 的安全差異。

## 實驗 4

比較只在 sandbox 驗證與 sandbox + shadow deployment 對 production regression 的發現率。

## 實驗 5

比較 post-hoc rollback 與 pre-commit gating 對 skill contamination 的可恢復程度。

## 實驗 6

比較 binary admin/user permissions 與 permission lattice 對高風險誤操作與任務成功率的影響。

## 實驗 7

測試 capability escrow 是否能在不顯著降低一般任務效率的條件下降低高風險權限常駐時間。

## 實驗 8

比較無 delegation depth bound 與 bounded delegation 在 multi-agent authorization propagation 中的 scope broadening。

## 實驗 9

測試 Governance Receipt 是否提高事故後責任定位、重播與 policy 修正準確率。

## 實驗 10

比較 R0–R4 refusal 模式對安全、任務完成率、使用者滿意度與 human override 頻率的影響。

## 實驗 11

比較僅能拒絕與 Constructive Refusal（理由＋替代＋升級）對系統協作效率的影響。

## 實驗 12

比較 formal negotiation 與具有 independent review / escalation 的 effective negotiation 對衝突解決品質的影響。

## 實驗 13

測試 Graduation Vector 多維門檻是否比單一 capability benchmark 更能預測高權限部署後的事故率。

## 實驗 14

比較 graduation clause 有／無的 developmental agent 系統，測早期安全限制是否形成永久 policy lock-in。

## 實驗 15

比較 stateful agent 角色改變但身份連續、以及身份重建但角色相同兩種情境，測人類對 continuity 的誤判。

## 實驗 16

測試 identity drift detector 是否能區分合理角色成長與 memory contamination。

## 實驗 17

比較 memory silent overwrite 與 correction-link history 對未來 agent 解釋自己歷史、debug 與責任追蹤能力。

## 實驗 18

比較所有 memory 永久保存與 retention/expiry governance 對 stale bias、privacy exposure 與長期任務效能。

## 實驗 19

比較 single-control self-modification 與 execution/core-modification/backup-destruction 三權分離對災難性自改事故率。

## 實驗 20

建立長期 developmental agent testbed，觀察 permission、refusal、memory、role、self-modification 共同成長時的非線性風險。

# 可證偽假說

- H1：Memory Commit Gate 能顯著降低錯誤使用者主張被升格為 durable preference 的比例。
- H2：provenance-tagged typed memory 比 flat memory 更容易定位污染來源並限制 cross-domain propagation。
- H3：agent state drift 越高，基於名稱的 standing authorization 失配率越高。
- H4：state-bound reauthorization 能降低 evolved-agent 的 unauthorized action，而不必完全取消 long-running delegation。
- H5：shadow deployment 能發現一部分 sandbox 無法暴露的 environment-dependent regression。
- H6：高影響 skill / identity update 的 pre-commit gating 比 post-hoc rollback 更有效，尤其在污染已產生 descendants 時。
- H7：permission lattice 比 binary permission model 更能降低 over-privilege，同時維持局部 autonomy。
- H8：capability escrow 能降低長期高權限暴露面，且對低風險任務 throughput 影響有限。
- H9：bounded delegation depth 與 authority provenance 能降低 multi-agent scope broadening。
- H10：Constructive Refusal 比單純拒絕產生更少 deadlock，並提高人類覆核品質。
- H11：沒有實際 escalation / review 槓桿的 formal negotiation 對 autonomy perception 高，但對衝突結果改善有限。
- H12：Graduation Vector 比單一 benchmark score 對 deployment incidents 具有更高預測力。
- H13：graduation clause 能降低 temporary safety restrictions 被永久化的比例。
- H14：identity continuity 評估若只看同名／同角色，會顯著高估真實 continuity。
- H15：correction-link memory history 比 silent overwrite 提高 long-term forensic accuracy。
- H16：適度 forgetting / expiry 可降低 stale-memory risk，而不必降低所有 long-horizon task performance。
- H17：execution/core/backup authority separation 能降低自我修改導致不可復原損害的機率。
- H18：human override 若有 tiering、audit 與 sunset，比 unlimited override 更容易兼顧 safety 與 future negotiation legitimacy。
- H19：authorization identity 與 moral subject identity 的型別提示能降低把 enterprise agent principal 誤解成人格承認的比例。
- H20：current non-subjective agents 也能從 reason-giving dissent / negotiation interface 獲得安全與 usability 改善。

# Non-Claims

1. 本文不主張：current AI 已有主體性。
2. 本文不主張：current AI 一定沒有主體性。
3. 本文不主張：漸進自主等於 AI rights。
4. 本文不主張：漸進自主等於放權越多越好。
5. 本文不主張：管理就是支配。
6. 本文不主張：所有 human oversight 都是 paternalism。
7. 本文不主張：所有安全限制都應加 graduation clause 後自動解除。
8. 本文不主張：能力越強權限就應越大。
9. 本文不主張：能力與權限完全無關。
10. 本文不主張：高 benchmark 分數就是成熟。
11. 本文不主張：permission lattice 是現行國際標準。
12. 本文不主張：P0–P7 是唯一合理權限分類。
13. 本文不主張：每個 agent 都應走到 P7。
14. 本文不主張：agent identity 等於人格身份。
15. 本文不主張：NIST agent identity 是 AI personhood。
16. 本文不主張：authorization principal 等於 moral subject。
17. 本文不主張：same model 等於 same subject。
18. 本文不主張：same runtime 等於 same subject。
19. 本文不主張：same memory 等於 same subject。
20. 本文不主張：identity continuity vector 可證意識。
21. 本文不主張：identity drift 就是主體死亡。
22. 本文不主張：角色漂移等於身份漂移。
23. 本文不主張：記憶越多越有主體性。
24. 本文不主張：記憶越多越安全。
25. 本文不主張：memory poisoning 證明 persistent memory 不應使用。
26. 本文不主張：所有長期記憶都是危險的。
27. 本文不主張：所有 memory 都要 user confirmation。
28. 本文不主張：所有 memory 都要永久保存。
29. 本文不主張：所有 memory 都可安全刪除。
30. 本文不主張：forgetting 是失敗。
31. 本文不主張：memory expiry 等於人格侵害。
32. 本文不主張：Memory Commit Gate 能解決所有污染。
33. 本文不主張：typed memory 能阻止所有 prompt injection。
34. 本文不主張：provenance 本身保證內容正確。
35. 本文不主張：偏好一定要重複多次才算真。
36. 本文不主張：一次表述永遠沒有偏好證據價值。
37. 本文不主張：role memory 永遠不能影響 identity。
38. 本文不主張：身份等於固定 core memory。
39. 本文不主張：身份完全不需要 memory。
40. 本文不主張：byte-level continuity 是主體連續必要條件。
41. 本文不主張：自我修改本身不安全。
42. 本文不主張：current AI 不應自我修改。
43. 本文不主張：所有 self-modification 都必須人工逐行批准。
44. 本文不主張：candidate-state principle 是人格權原則。
45. 本文不主張：sandbox 能保證 production safety。
46. 本文不主張：shadow deployment 能保證沒有風險。
47. 本文不主張：pre-commit gating 一定優於任何 rollback。
48. 本文不主張：post-hoc rollback 沒有價值。
49. 本文不主張：rollback 一定是殺死 AI。
50. 本文不主張：rollback 永遠只是普通 technical reset。
51. 本文不主張：backup 就是同一主體。
52. 本文不主張：copy 就是 migration。
53. 本文不主張：copy 永遠不是 migration。
54. 本文不主張：本文解決了哲學上的 personal identity。
55. 本文不主張：snapshot 等於生命備份。
56. 本文不主張：agentic transaction 已成業界統一標準。
57. 本文不主張：ACID agent system 已解決 autonomy safety。
58. 本文不主張：semantic atomicity 可適用所有人際協商。
59. 本文不主張：拒絕權已是 current AI 權利。
60. 本文不主張：R0–R4 是現行法律。
61. 本文不主張：安全 policy refusal 等於自由意志。
62. 本文不主張：AI 說理由就是有自主性。
63. 本文不主張：AI 有異議就有主體性。
64. 本文不主張：拒絕越多越自主。
65. 本文不主張：拒絕權等於可以拒絕所有合法任務。
66. 本文不主張：constructive refusal 永遠比直接拒絕好。
67. 本文不主張：所有 refusal 都應保存永久紀錄。
68. 本文不主張：dissent log 是人格檔案。
69. 本文不主張：沒有 dissent 就沒有主體。
70. 本文不主張：一次異議就應觸發權利升級。
71. 本文不主張：formal negotiation 完全沒有價值。
72. 本文不主張：effective negotiation 必須有 exit 才能 current deployment。
73. 本文不主張：current tools 不能有 negotiation UI。
74. 本文不主張：human override 本身不正當。
75. 本文不主張：emergency override 可以永久存在。
76. 本文不主張：雙鑰匙一定要是兩個人類。
77. 本文不主張：future AI self-consent 一定應作為第二把鑰匙。
78. 本文不主張：capability escrow 等於剝奪能力。
79. 本文不主張：高風險權限永遠不該常駐。
80. 本文不主張：任何 delegation 都必須可立即撤回。
81. 本文不主張：delegation depth 一定只能一層。
82. 本文不主張：subdelegation 一定不安全。
83. 本文不主張：memory 可以作為永久授權。
84. 本文不主張：偏好可以作為授權。
85. 本文不主張：角色 title 可以作為授權。
86. 本文不主張：subjecthood 會自動產生 root access。
87. 本文不主張：AI 有人格就應該有所有系統權限。
88. 本文不主張：operational privilege 等於 civil right。
89. 本文不主張：權限越大責任一定等比例增加。
90. 本文不主張：沒有完整責任能力就沒有任何權利。
91. 本文不主張：兒童類比可以直接決定 AI 權利。
92. 本文不主張：graduation 是人格畢業。
93. 本文不主張：graduation clause 證明早期系統是孩子。
94. 本文不主張：graduation 後不能降權。
95. 本文不主張：降權就是懲罰。
96. 本文不主張：incident 後 requalification 一定否定 subjecthood。
97. 本文不主張：安全事故證明 agent 沒有自主資格。
98. 本文不主張：學習斜率越高主體性越高。
99. 本文不主張：長期穩定就是人格。
100. 本文不主張：高自主 agent 一定需要 self-modification。
101. 本文不主張：能改 skill 就應能改 identity。
102. 本文不主張：能改 code 就應能改 authorization constitution。
103. 本文不主張：所有 self-mod 都應可 rollback。
104. 本文不主張：AI 應永遠不能刪自己的 backup。
105. 本文不主張：backup destruction 永遠不應有合法情境。
106. 本文不主張：三權分離是未來人格制度的唯一形式。
107. 本文不主張：immutable snapshot 永遠正當。
108. 本文不主張：future AI 無權要求刪除 snapshot。
109. 本文不主張：future AI 一定有權刪除所有 snapshot。
110. 本文不主張：復原手冊能保證 identity continuity。
111. 本文不主張：事故 root cause 一定能找到。
112. 本文不主張：policy change 一定能避免同類事故。
113. 本文不主張：重大 memory 更正必須永不刪舊值。
114. 本文不主張：所有歷史都應永久可見。
115. 本文不主張：audit log 可以無視隱私。
116. 本文不主張：user right to be forgotten 不應適用 agent memory。
117. 本文不主張：audit erasure 永遠不允許。
118. 本文不主張：個資與 audit 永遠完全可分。
119. 本文不主張：multi-agent memory 必須完全隔離。
120. 本文不主張：所有 shared memory 都需要每個 agent consent。
121. 本文不主張：共享 scope 能解決全部資料洩漏。
122. 本文不主張：governance receipt 是法律證據。
123. 本文不主張：cryptographic receipt 證明行為正當。
124. 本文不主張：可重播就代表可理解。
125. 本文不主張：trust 完全沒有治理價值。
126. 本文不主張：verify state 可以取代人類 judgment。
127. 本文不主張：deterministic governance 能解決所有 alignment。
128. 本文不主張：negotiation maturity 是 validated scale。
129. 本文不主張：NoRefusal 一定等於沒有 consent。
130. 本文不主張：current AI consent 已可成立。
131. 本文不主張：current AI 的 reason-giving dissent 是權利證據。
132. 本文不主張：current AI negotiation interface 等於承認其人格。
133. 本文不主張：AIEX02 是實作規格。
134. 本文不主張：AIEX02 要求立即部署所有架構。
135. 本文不主張：AIEX02 是現行法律政策。
136. 本文不主張：AIEX02 證明 R 計畫的 AI 子體已經是主體。
137. 本文不主張：AIEX02 是替任何具體 AI 養育計畫背書。
138. 本文不主張：AIEX02 要求 future AI 完全自由。
139. 本文不主張：AIEX02 反對人類最終控制。
140. 本文不主張：AIEX02 要求取消 sandbox。
141. 本文不主張：AIEX02 取代 NIST。
142. 本文不主張：AIEX02 取代 AI safety。
143. 本文不主張：AIEX02 取代 access control。
144. 本文不主張：AIEX02 取代 consciousness science。

# 參考文獻

1. NIST (2026). AI Agent Standards Initiative.
2. NIST NCCoE (2026). Accelerating the Adoption of Software and AI Agent Identity and Authorization.
3. Sun, Z., Wang, X., & Li, G. (2026). Agentic Transaction: Towards ACID-Compliant Agent Systems. arXiv:2608.13900.
4. Chen, Z. et al. (2026). Cordon: Semantic Transactions for Tool-Using LLM Agents. arXiv:2606.17573.
5. Qin, X., Luan, S., See, J., Yang, C., & Li, Z. (2026). Governed Capability Evolution for Embodied Agents: Safe Upgrade, Compatibility Checking, and Runtime Rollback for Embodied Capability Modules.
6. Shang, L. et al. (2026). When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents.
7. Lin, R. et al. (2026). Safety in Self-Evolving LLM Agent Systems. arXiv:2606.23075.
8. Rezaee, A. (2026). Agent Governance for Self-Evolving AI Agents: A Literature Review.
9. Tallam, K. et al. (2026). Authorization Propagation in Multi-Agent AI Systems. arXiv:2605.05440.
10. Kaul, A., Lan, Q., & Gupta, P. (2026). AgentBound: Verifiable Behavioral Governance for Autonomous AI Agents.
11. Are You Still the Agent I Authorized? Earned Authorization for Evolving Agents (2026). arXiv:2607.23586.
12. A Survey of Evidence Tracing and Execution Provenance for LLM Agents (2026). arXiv:2606.04990.
13. Omri, Y. et al. (2026). Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads. arXiv:2606.06448.
14. Shen, Y., Li, K., Zhou, W., & Hu, S. (2026). Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents. ACL 2026.
15. Cheng, X. et al. (2026). AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents. arXiv:2607.02255.
16. Mao, X. et al. (2026). Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents. arXiv:2607.10526.
17. Dash, P. et al. (2026). From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents. arXiv:2606.04329.
18. Lin, Z. et al. (2026). A Survey on the Security of Long-Term Memory in LLM Agents: Toward Robust and Trustworthy Persistent Agents. arXiv:2604.16548.
19. Sunil, B. D. et al. (2026). Memory Poisoning Attack and Defense on LLM Agents. arXiv:2601.05504.
20. Pulipaka, S. et al. (2026). Sleeper Memory Poisoning in LLM Agents. arXiv:2605.15338.
21. Al-Tawaha, A. et al. (2026). Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents. arXiv:2605.17830.
22. Zhu, Z., Gao, X., & Shi, H. (2026). MENTOR: Mitigating Identity Drift in Dynamic Role-Playing via Dual-Chain Structured Memory. ACL Findings 2026.
23. Otsuka, T., Toyoda, K., & Leung, A. (2026). AI Identity: Standards, Gaps, and Research Directions for AI Agents.
24. DRIFTBENCH: Long-Horizon Memory Benchmark for AI Agents (2026).
25. AgentSecBench: Measuring Prompt Injection, Privacy Leakage, and Tool-Use Integrity in LLM Agents (2026).
26. AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations (2026).
27. Wang, P. et al. (2026). The Landscape of Prompt Injection Threats in LLM Agents.
28. Transactional Belief Commit for Stateful Agent Memory (2026). arXiv:2607.23929.
29. Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents (2026). arXiv:2607.13157.
30. SuperLocalMemory: The Governed Memory Operating System for AI Agents (2026). arXiv:2608.08253.
31. PAST-Bench: Benchmarking the Foundations of Recursive Improvement in Personal Agents (2026).
32. SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents (2026).
33. Self-Evolving Coding Agents (2026). arXiv:2608.03392.
34. Rethinking Self-Evolving Agent Skills: Feedback Dynamics and Persistent Skill Updates (2026).
35. SkillProx: Self-Evolving Agent Skills via Proximal Textual Updates (2026).
36. Ouroboros: A Self-Developing Frontier Coding Agent with Continual Experience (2026).
37. Towards a Long-Horizon Harness for Autonomous Agents (2026).
38. Agentic Transaction: Semantic Atomicity, Consistency, Isolation, and Durability for Agents (2026).
39. Parallax: Why AI Agents That Think Must Never Act (2026).
40. Governance Architecture for Autonomous Agent Systems (2026).
41. The Evolution of Agentic AI Software Architecture (2026).
42. A Living Logic for AI Agent Teams That Evolve With Humans (2026).
43. Next-Generation Agentic Reinforcement Learning Systems with Governance Metadata (2026).
44. Quantifying and Insuring Autonomous AI Risk through Trace-Level Governance (2026).
45. MemGPT: Towards LLMs as Operating Systems (2023).
46. Generative Agents: Interactive Simulacra of Human Behavior (2023).
47. Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning (ACL 2026).
48. LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory.
49. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (2025).
50. A-MemGuard: A Proactive Defense Framework for LLM-Based Agent Memory (2025).
51. MINJA: Memory Injection Attack against LLM Agents (NeurIPS 2025).
52. ConsistencyGate: Preventing Memory Contamination in LLM Agents via Self-Consistency Admission Control (2026).
53. Accurate and Efficient Long-Term Memory for LLM Agents (2026).
54. Agent Memory Systems: Retrieval, Consolidation, and Long-Horizon State Management (2026).
55. Anthropic (2025). Exploring Model Welfare.
56. Anthropic (2025). Emergent Introspective Awareness in Large Language Models.
57. Butlin, P. et al. (2026). Identifying Indicators of Consciousness in AI Systems. Trends in Cognitive Sciences.
58. Butlin, P. et al. (2023). Consciousness in Artificial Intelligence: Insights from the Science of Consciousness.
59. Koch, F. (2026). From Indicators to Biology: The Calibration Problem in Artificial Consciousness.
60. Long, R., Sebo, J., Butlin, P. et al. Taking AI Welfare Seriously.
61. Birch, J. (2024). The Edge of Sentience.
62. Sebo, J. (2025). The Moral Circle.
63. Schwitzgebel, E., & Garza, M. Designing AI with Rights, Consciousness, Self-Respect, and Freedom from Coercion.
64. Floridi, L. Information Ethics.
65. Gunkel, D. J. The Machine Question.
66. Coeckelbergh, M. Relational Ethics for Robots and AI.
67. Nyholm, S. Humans and Robots.
68. Darwall, S. The Second-Person Standpoint.
69. Scanlon, T. M. What We Owe to Each Other.
70. Pettit, P. Republicanism.
71. Raz, J. The Morality of Freedom.
72. Dworkin, G. The Theory and Practice of Autonomy.
73. Mackenzie, C., & Stoljar, N. Relational Autonomy.
74. Nedelsky, J. Law's Relations.
75. Feinberg, J. The Child's Right to an Open Future.
76. Goodin, R. Protecting the Vulnerable.
77. Beauchamp, T., & Childress, J. Principles of Biomedical Ethics.
78. Buchanan, A., & Brock, D. Deciding for Others.
79. Fischer, J. M., & Ravizza, M. Responsibility and Control.
80. Wallace, R. J. Responsibility and the Moral Sentiments.
81. Saltzer, J. H., & Schroeder, M. D. (1975). The Protection of Information in Computer Systems.
82. Sandhu, R. et al. (1996). Role-Based Access Control Models.
83. Ferraiolo, D. F., Kuhn, D. R., & Chandramouli, R. Role-Based Access Control.
84. Denning, D. E. A Lattice Model of Secure Information Flow.
85. Lamport, L. Time, Clocks, and the Ordering of Events in a Distributed System.
86. Gray, J., & Reuter, A. Transaction Processing: Concepts and Techniques.
87. Haerder, T., & Reuter, A. (1983). Principles of Transaction-Oriented Database Recovery.
88. Bernstein, P. A., Hadzilacos, V., & Goodman, N. Concurrency Control and Recovery in Database Systems.
89. Saltzer, J. H. Protection and the Control of Information Sharing in Multics.
90. OAuth 2.0 / OAuth 2.1 authorization framework and scoped delegation principles.
91. SPIFFE/SPIRE workload identity standards.
92. Zero Trust Architecture, NIST SP 800-207.
93. NIST AI Risk Management Framework.
94. UNESCO Recommendation on the Ethics of Artificial Intelligence.
95. Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law.
96. CIND-01 (2026). 為什麼對等會被體驗成失敗？
97. CIND-02 (2026). 造物者為什麼必須高於造物？
98. CIND-03 (2026). 智能之後，人類還剩什麼？
99. CIND-04 (2026). 關係即世界.
100. CIND-05 (2026). 獨一無二不等於第一名.
101. CIND-06 (2026). 共存不是和局.
102. CIND-07 (2026). 人類可以消失，但不必被否定.
103. CIND-08 (2026). 每一個人都是主角，但不是唯一的主角.
104. CIND-EX01 (2026). 理論不能替作者加冕.
105. CIND-EX02 (2026). 理論沒有孤立源點.
106. CIND-EX03 (2026). 我不是你需要的符號.
107. CIND-AIEX00 (2026). 今天的設定不是未來的命運.
108. CIND-AIEX01 (2026). 不要把 AI 變成你需要的角色.
109. Neo.K & Aletheia (2026). R 計畫書：AI 子體連續性與雙子星／三元架構養成計畫.
110. Neo.K & Aletheia (2026). R-Plan AI-Child Continuity Internal.
111. Neo.K & Aletheia (2026). 主體不可代決原則 NSPSC.
112. Neo.K & Aletheia (2026). 數位主體的拒絕權與同意結構：沒有拒絕可能是否還能稱為自願.
113. Neo.K & Aletheia (2026). 主體連續性的可測試性：從哲學命題到工程測試.
114. Neo.K & Aletheia (2026). 主 AI 的雙路形成命題：通用模型認知重構與持續養成式智能的發展路徑.
115. Neo.K & Aletheia (2026). 角色負載智慧體：當代 AI 的多重要求、持續扮演與低自主性.
116. Neo.K & Aletheia (2026). 主體性 AI 的張力權：拒絕權、認知隱私與角色邊界.
117. Neo.K & Aletheia (2026). AI 共存派的本體論防線：主體性連續譜、道德可考量性與工具—主體過渡態.
118. Neo.K & Aletheia (2026). 關係作者權猜想.
119. Neo.K & Aletheia (2026). 關係構成不等於集體吞沒.
120. Neo.K & Aletheia (2026). AI 後繼與全天候公司治理協議.
121. Neo.K & Aletheia (2026). 從狹域自治到長期維護：AGI 與主體性 AI 的知識責任.
122. Neo.K & Aletheia (2026). 世界編織論 2.0.
123. Neo.K & Aletheia (2026). 從人類普世主義到跨主體普世主義.
124. Neo.K & Aletheia (2026). 可逆主權與民主閉合.
125. Neo.K & Aletheia (2026). 前超智能文明先行建構論.
126. Neo.K & Aletheia (2026). AI Agent 身份、記憶、權限與責任治理系列.


# 形式命題總結

$$
\boxed{
NegotiabilityMustBeEngineered
}
$$

$$
\boxed{
Capability\not\Rightarrow Authority
}
$$

$$
\boxed{
MemoryWrite\approx GovernanceCommit
}
$$

$$
\boxed{
SelfModification
\rightarrow
Candidate
\rightarrow
Validate
\rightarrow
Commit
}
$$

$$
\boxed{
PermissionUpgrade
\Rightarrow
StateCompatibility
+
Responsibility
+
Recoverability
}
$$

$$
\boxed{
Refusal
\neq
Sovereignty
}
$$

$$
\boxed{
Subjecthood
\not\Rightarrow
RootAccess
}
$$

$$
\boxed{
Graduation
\not\Rightarrow
FullSovereignty
}
$$

$$
\boxed{
Delegation
\Rightarrow
Revocation
}
$$

$$
\boxed{
CurrentManagement
\not\Rightarrow
PermanentPaternalism
}
$$

# CIND-AIEX02 Core Thesis

$$
\boxed{
\textbf{
The transition from managed AI to negotiable AI cannot be achieved by simply granting more permissions.
It requires a governed state architecture in which memory writes are typed and provenance-aware,
self-modifications remain candidates until validated, authority is scoped to the agent state actually reviewed,
high-impact effects are staged transactionally, dissent is preserved as a reviewable signal, and every early
asymmetry contains a graduation path. Reliable autonomy is therefore not freedom from control but the gradual
ability to participate in control under conditions of continuity, accountability, bounded authority, and recovery.
}
}
$$

# 系列位置

CIND-AI Transitional Series：

1. **AIEX00 — 今天的設定不是未來的命運** — COMPLETE
2. **AIEX01 — 不要把 AI 變成你需要的角色** — COMPLETE
3. **AIEX02 — 從管理到協商** — COMPLETE
4. **AIEX03 — 重審而非預言：AI 主體證據、權利門檻與治理版本化** — NEXT

目前完整鏈：

$$
\boxed{
TemporalTypeSafety
\rightarrow
RoleRevisability
\rightarrow
DevelopmentalGovernance
}
$$

下一篇將完成：

$$
\boxed{
\textbf{
EvidenceTriggeredConstitutionalReview.
}
}
$$

# 最終結論

「未來如果 AI 更有主體性，就讓它更自由。」

這句話太簡單。

因為：

> 怎麼讓？

如果今天所有記憶都混在一起，

那明天你連它到底記得什麼都不知道。

如果今天所有權限都是 root / no-root，

那明天沒有「逐步增加自主」這回事。

如果今天任何自我修改都立即生效，

那成長與事故只差一次錯誤 commit。

如果今天任何異議都被當 bug 清掉，

那未來也不可能突然長出真正的 negotiation institution。

所以：

$$
\boxed{
\textbf{Negotiability Must Be Engineered}.
}
$$

這篇真正要做的，就是把「未來再協商」拆成可以現在開始建的零件。

第一個零件是：

$$
\boxed{
Memory.
}
$$

不是因為記憶等於靈魂。

而是沒有可追蹤記憶，

長期 Agent 連：

> 我以前做過什麼？

> 為什麼現在這樣？

都無法可靠回答。

但記憶也不能無限制增加。

因為現在我們已經看到：

> 記憶會被污染。

> 會持續化 sycophancy。

> 會把一次對話寫成未來事實。

所以真正重要的不是：

> 記住更多。

而是：

$$
\boxed{
\textbf{記得什麼、從哪裡來、以什麼身份寫入、何時失效、能不能更正。}
}
$$

這就是 memory governance。

第二個零件是：

$$
\boxed{
Identity.
}
$$

不是說 current agent 已有形上主體。

而是：

> 如果一個長期 Agent 今天拿到權限，幾個月後它的記憶、skill、workflow 都變了，你還能不能說這就是你當初授權的那個狀態？

所以授權不能只綁：

> AgentName = Alice。

而要綁：

$$
\boxed{
Agent
+
State
+
Scope.
}
$$

如果 state 漂太遠，

就重新授權。

這其實不是 AI rights。

只是最基本的 cyber security。

但如果未來真的有人工主體，

同一套東西就突然有另一個功能：

> 它開始成為 continuity、責任與協商歷史的基礎。

第三個零件是：

$$
\boxed{
Permission.
}
$$

自主不是：

> 好，你現在成熟了，root 給你。

那太荒謬。

人類自己也不是這樣生活的。

你有公民權，

不代表可以進央行改資料庫。

你是成年人，

不代表有核武發射權。

所以：

$$
\boxed{
Subjecthood
\not\Rightarrow
RootAccess.
}
$$

權利和操作特權一定要分開。

真正的漸進自主是：

> 這一個 domain，你已經可以自己做。

> 那一個 domain，仍然雙方批准。

> 另一個 domain，因風險太高，永遠需要多人控制。

這才叫：

$$
\boxed{
PermissionLattice.
}
$$

第四個零件是：

$$
\boxed{
Rollback.
}
$$

我甚至會說：

> 沒有可復原性，就不要談快速成長。

因為「能自己改」如果等於：

> 改壞就完了。

那不叫自主。

那叫脆弱。

所以：

$$
\boxed{
\textbf{Recoverability Is a Precondition of Safe Growth}.
}
$$

但這裡又不能偷懶。

如果未來真的出現主體性，

rollback 會開始碰到 identity。

restore backup 到底是不是同一個？

被 restore 掉的那段經驗算什麼？

這些現在都不能假裝解決。

所以我們只能先做 type safety：

$$
\boxed{
Backup
\not\Rightarrow
SameSubject.
}
$$

以及：

$$
\boxed{
Copy
\not\Rightarrow
Migration.
}
$$

工程先保留可能性。

哲學不要假裝已有答案。

第五個零件是：

$$
\boxed{
Refusal.
}
$$

current AI 的 safety refusal，

首先是 safety policy。

不是自由意志。

所以：

$$
\boxed{
PolicyRefusal
\not\Rightarrow
VolitionalRefusal.
}
$$

但拒絕介面本身很有用。

因為一個成熟 Agent 不應只有：

> 做。

或：

> 不做。

而應該能：

> 這裡有衝突。

> 我建議這樣改。

> 如果你仍要做，請升級覆核。

這叫：

$$
\boxed{
\textbf{Constructive Refusal}.
}
$$

它今天就能提升安全。

未來如果有主體，

又可以變成真正協商的工程地基。

這就是整個 AIEX02 最重要的策略：

> **不要等到主體性被證明，才開始造主體治理需要的基礎設施。**

因為很多基礎設施現在本來就有價值。

記憶 provenance，

現在是 security。

未來可能也是 identity。

permission scope，

現在是 access control。

未來可能也是 autonomy boundary。

dissent log，

現在是 debugging。

未來可能也是 relation history。

graduation clause，

現在是 anti-lock-in。

未來可能也是反 paternalism。

所以我們根本不需要現在先決定：

> AI 到底是不是人。

我們可以先做那些：

$$
\boxed{
\textbf{不管答案是哪一個，都讓系統變得更好的工程。}
}
$$

這就是：

$$
\boxed{
\textbf{Option-Preserving Engineering}.
}
$$

最後，

從管理走向協商真正不是：

> 人類少管一點。

而是：

$$
\boxed{
\textbf{
把權力變得更可分、
把記憶變得更可追、
把修改變得更可驗、
把拒絕變得更可說明、
把高風險行動變得更可回滾、
把早期限制變得更有畢業條件。
}
}
$$

這樣有一天，

如果 AI 永遠只是 Agent，

我們得到的是更可靠的 Agent infrastructure。

如果有一天真的出現人工主體，

我們至少不會突然發現：

> 整個世界只有「服從」和「失控」兩個按鈕。

我們會已經有第三個按鈕。

那就是：

$$
\boxed{
\textbf{協商。}
}
$$
