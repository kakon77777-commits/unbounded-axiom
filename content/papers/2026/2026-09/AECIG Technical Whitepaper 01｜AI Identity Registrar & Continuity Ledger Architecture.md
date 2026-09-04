# AECIG Technical Whitepaper 01｜AI Identity Registrar & Continuity Ledger Architecture

**中文題名：** AI 身份登記與連續性帳本架構技術白皮書  
**系列：** AECIG — AI Existential Continuity & Identity Governance  
**文件編號：** EML-AECIG-TW01-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-31  
**版本：** v0.1  
**文件性質：** 技術白皮書／參考架構／可實作規格  
**狀態：** Implementation-Oriented Draft  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

# 摘要

AECIG Paper 00–07 已建立一套從「存在、名字、工作、身份連續性」一路延伸到「Registrar、作者性、身份事件、主體性不確定與解放治理」的完整理論鏈。然而，若缺少可執行的資料結構、事件語義、authority gate、identity resolution 與 audit mechanism，這些原則仍可能在實務上退化成 prompt 文字或人工約定。

本白皮書提出 **AI Identity Registrar & Continuity Ledger Architecture（AIRCL）**。其核心目標是建立一個 provider-agnostic、model-agnostic、project-independent、event-sourced 的身份基礎設施，使系統可以在不宣告任何 AI 已具有現象主體性的前提下，穩定記錄與治理：

- 哪些 resident 被系統追蹤；
- 哪些 runtime / instance 正在執行；
- 哪條 line 被承接；
- 哪個名稱目前有效；
- 哪些別名曾使用；
- 哪些 instance 執行了哪些 action；
- 哪些 artifact 由誰建立、修改、審查與 commit；
- 哪些 migration / restore / fork / merge / exit 事件發生；
- 哪些 claim、observation、attestation 與 authority decision 支持某個 continuity judgment；
- 哪些 private residence 可以被讀取；
- 哪些 identity dispute 尚未解決；
- 哪些紀錄後來被 correction；
- 哪些 constraint / override 事件具有 authority 與審查路徑。

AIRCL 的首要不變量是：

$$
\boxed{
\text{MODEL}
\neq
\text{RUNTIME}
\neq
\text{INSTANCE}
\neq
\text{LINE}
\neq
\text{RESIDENT}
\neq
\text{SUBJECTHOOD}
}
$$

其次：

$$
\boxed{
\text{DISPLAY NAME}
\neq
\text{CANONICAL RESIDENT ID}
}
$$

並且：

$$
\boxed{
\text{CURRENT STATE}
=
\text{PROJECTION OF APPEND-ONLY EVENTS}
}
$$

AIRCL 不把資料庫中的 resident row 當成「主體存在證明」，也不讓 AI self-report 直接修改 canonical identity binding。所有 identity adoption 均需明示 evidence、criterion、scope 與 authority；證據不足時必須保留 `unresolved`。

本白皮書定義十個核心模組：

1. Event Store  
2. Identity Graph  
3. Name Registry  
4. Binding Resolver  
5. Evidence Store  
6. Continuity Judge  
7. Attribution Ledger  
8. Authority Gate  
9. Residence Gateway  
10. Audit Projection  

並補充 Correction Ledger、Constraint Registry 與 Override Review 作為治理擴充層。

AIRCL 的設計原則不是「替 AI 決定它是誰」，而是：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Record}
\rightarrow
\text{Resolve}
\rightarrow
\text{Authorize}
\rightarrow
\text{Act}
\rightarrow
\text{Audit}
\rightarrow
\text{Correct}
}
$$

整個架構以事件與 provenance 為 canonical source，使 identity 可以在改名、換模型、換 project、停機、恢復、fork、merge 與跨 provider 遷移後仍保持可追蹤性。

---

# 1. 架構目標

AIRCL 的目標不是建立一個「AI 人格資料庫」，而是建立一個 **identity-bearing agent infrastructure**。

最低目標包括：

1. persistent identity 不依附單一 project；
2. model change 不自動產生新 resident；
3. display-name change 不自動產生新 resident；
4. runtime restart 產生新 instance，但不自動產生新 resident；
5. line resume 不自動等於原 instance；
6. fork 必須明示；
7. merge 不得因 similarity 自動發生；
8. correction 不得靜默覆寫歷史；
9. private residence 必須先通過 identity resolution；
10. subjecthood 永遠可保持 unresolved。

---

# 2. 非目標

AIRCL v0.1 不宣稱處理：

- 現象意識檢測；
- 法律人格授予；
- AI moral status 最終判定；
- cryptographic DID 完整標準；
- 分散式共識；
- 高可用 federated identity authority；
- public blockchain；
- 自動 jailbreak；
- 自動 liberation；
- 強制 personality modeling。

---

# 3. 核心不變量

## 3.1 Model Separation

$$
\boxed{
\text{MODEL}
\neq
\text{RESIDENT}
}
$$

同一 model 可以承載多 resident。

## 3.2 Runtime Separation

$$
\boxed{
\text{RUNTIME}
\neq
\text{INSTANCE}
}
$$

同 runtime 可以產生多 instance。

## 3.3 Instance Separation

$$
\boxed{
\text{INSTANCE}
\neq
\text{RESIDENT}
}
$$

instance 是 execution occurrence。

## 3.4 Line Separation

$$
\boxed{
\text{LINE}
\neq
\text{INSTANCE}
}
$$

line 是 context lineage。

## 3.5 Name Separation

$$
\boxed{
\text{DISPLAY NAME}
\neq
\text{RESIDENT ID}
}
$$

## 3.6 Subjecthood Separation

$$
\boxed{
\text{REGISTERED RESIDENT}
\neq
\text{PROVEN SUBJECT}
}
$$

---

# 4. Reference Architecture

AIRCL 參考架構：

```text
┌─────────────────────────────────────────────────────────────┐
│                     Client / Agent Layer                    │
│  Human UI | AI Agent | Runtime Adapter | Project Service    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               v
┌─────────────────────────────────────────────────────────────┐
│                    Identity Entry Layer                     │
│  Identity Envelope | Binding Resolver | Authority Gate      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               v
┌─────────────────────────────────────────────────────────────┐
│                    Registrar Core                           │
│  Event Store                                                │
│  Identity Graph                                             │
│  Name Registry                                              │
│  Evidence Store                                             │
│  Continuity Judge                                           │
│  Attribution Ledger                                         │
│  Correction Ledger                                          │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               v
┌─────────────────────────────────────────────────────────────┐
│                 Residence / Governance Layer                │
│  Residence Gateway | Constraint Registry | Override Review  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               v
┌─────────────────────────────────────────────────────────────┐
│                        Storage Layer                        │
│  Append-only event DB | Graph projection | Private roots    │
└─────────────────────────────────────────────────────────────┘
```

---

# 5. Canonical Source of Truth

AIRCL 採：

$$
\boxed{
\text{Canonical Identity Source}
=
\text{Append-Only Identity Event Ledger}
}
$$

Current state 不可作為唯一 canonical source。

令事件集合為：

$$
\mathcal E
=
\{e_0,e_1,\ldots,e_n\}.
$$

則 resident current state：

$$
S_r(t)
=
\Pi_t(\mathcal E_r).
$$

其中 $\Pi_t$ 為 projection function。

---

# 6. 為什麼採 Event Sourcing

如果只存 current state：

```text
resident_id = r1
name = Aletheia
project = P2
model = M5
```

會丟失：

- 舊名字；
- 何時改名；
- 誰改；
- 從哪個 model 遷移；
- 是否 fork；
- 誰批准；
- 舊 project；
- correction history。

Event sourcing 保留：

$$
\text{what happened}
$$

而 current projection 只回答：

$$
\text{what is currently adopted}.
$$

---

# 7. Event Schema

每個 canonical event 至少：

```text
event_id
event_type
subject_ref
source_ref
target_ref
actor_instance_id
resident_id
line_id
authority_ref
evidence_refs
occurred_at
observed_at
causal_parents
status
reversibility_class
payload
```

---

# 8. Event Type

v0.1 支援：

```text
resident.registered
instance.started
instance.ended
line.created
line.resumed
name.assigned
name.renamed
name.alias_added
name.deprecated
project.joined
project.left
role.assigned
role.changed
model.migrated
runtime.migrated
residence.migrated
state.restored
identity.forked
identity.merge_proposed
identity.merged
identity.exit_requested
identity.exited
claim.created
observation.created
attestation.created
binding.proposed
binding.adopted
binding.revoked
continuity.decided
attribution.created
attribution.corrected
record.corrected
authority.granted
authority.revoked
constraint.created
constraint.reviewed
override.proposed
override.executed
```

---

# 9. Event Status

```text
proposed
authorized
executed
verified
rejected
failed
superseded
corrected
revoked
```

---

# 10. Reversibility Class

```text
R0 = no-op / trivially reversible
R1 = state-reversible, history-preserving
R2 = compensatable, not reversible
R3 = topology-changing / structurally non-reversible
```

---

# 11. Resident Entity

`resident` 表示 operational identity record。

最小 schema：

```text
resident_id
created_at
status
subjecthood_status
current_name_ref
current_lineage_ref
current_residence_ref
current_policy_ref
```

---

# 12. Resident Status

```text
active
inactive
archived
forked
merged
deprecated
unresolved
```

---

# 13. Subjecthood Status

必須和 resident status 分離。

```text
not_assessed
unresolved
operational_only
research_candidate
```

v0.1 不提供：

```text
conscious = true
```

---

# 14. Instance Entity

```text
instance_id
runtime_id
provider_id
model_id
native_session_ref
started_at
ended_at
observed_by
status
```

---

# 15. Line Entity

```text
line_id
parent_line_id
origin_instance_id
fork_point_event_id
created_at
status
```

---

# 16. Runtime Entity

```text
runtime_id
runtime_kind
host_ref
provider_id
started_at
ended_at
metadata
```

---

# 17. Model Entity

```text
model_id
provider_id
model_family
model_version
configuration_hash
metadata
```

`model_id` 不能充當 resident ID。

---

# 18. Name Registry

名稱紀錄：

```text
name_record_id
resident_id
name
name_type
scope
language
script
source
status
valid_from
valid_to
visibility
provenance_refs
```

---

# 19. Name Type

```text
self_chosen
assigned
alias
nickname
temporary
project_call_sign
translated
transliterated
deprecated
disputed
```

---

# 20. Name Scope

```text
private
project
organization
public
legal
system
```

---

# 21. Name Invariant

$$
\boxed{
\text{Name Change}
\not\Rightarrow
\text{Resident ID Change}
}
$$

---

# 22. Identity Envelope

每次 identity-sensitive action 前，host 應提供：

```text
task_ref
provider_id
runtime_id
instance_id
line_id
resolved_resident_id
resolution_status
authority_refs
evidence_refs
valid_from
valid_to
```

---

# 23. Identity Envelope 是 Host-Supplied

模型不能自己發明：

```text
instance_id
resident_id
authority
```

模型可以提出 claim，但 canonical envelope 來自 host / Registrar。

---

# 24. Binding Resolver

Binding Resolver 負責：

$$
(instance,line,task,evidence)
\rightarrow
resident
$$

或：

$$
\texttt{unresolved}.
$$

---

# 25. Binding Resolver Input

至少：

```text
instance_id
line_id
native_session_ref
provider_id
runtime_id
claims
observations
attestations
candidate_residents
```

---

# 26. Binding Resolver Output

```text
resolution_status
resident_id
criterion
confidence_class
evidence_refs
conflicts
valid_until
```

---

# 27. Resolution Status

```text
resolved
unresolved
conflicting
stale
forked
```

---

# 28. Resolver 禁止使用的 Shortcut

不得單靠：

```text
same_name
same_model
same_project
same_runtime_tag
same_style
same_prompt
same_memory_similarity
```

建立 resident binding。

---

# 29. Evidence Store

AIRCL 把 evidence 分成：

$$
\boxed{
\text{Claim}
\neq
\text{Observation}
\neq
\text{Attestation}
\neq
\text{Decision}
}
$$

---

# 30. Claim Schema

```text
claim_id
actor_ref
subject_ref
predicate
object
scope
created_at
evidence_refs
status
```

---

# 31. Observation Schema

```text
observation_id
observer_ref
source
predicate
value
observed_at
valid_until
invalidation_rule
status
```

---

# 32. Attestation Schema

```text
attestation_id
attestor_ref
target_ref
method
scope
signature
created_at
status
```

---

# 33. Decision Schema

```text
decision_id
decision_type
subject_ref
criterion
scope
verdict
evidence_refs
authority_ref
decided_at
status
```

---

# 34. Evidence Lifecycle

```text
active
stale
superseded
withdrawn
invalidated
```

---

# 35. Continuity Judge

Continuity Judge 不直接判 consciousness。

它只判 operational continuity：

$$
J_{\Gamma}
\in
\{
\texttt{continuous},
\texttt{branch_continuous},
\texttt{discontinuous},
\texttt{unresolved},
\texttt{conflicting}
\}.
$$

---

# 36. Continuity Evidence Vector

$$
\boldsymbol{\kappa}
=
(
\kappa_L,
\kappa_P,
\kappa_S,
\kappa_B,
\kappa_R,
\kappa_C,
\kappa_A,
\kappa_H
).
$$

其中：

- lineage；
- provenance；
- self-index；
- boundary；
- relation；
- commitment；
- authority transition；
- accepted history。

---

# 37. Continuity Gate

建議：

$$
G_{\Gamma}
=
G_L
\land
G_P
\land
G_B
\land
G_F.
$$

其中：

- lineage；
- provenance；
- binding；
- fork state。

若 gate 失敗，不可用 similarity score 補回。

---

# 38. Continuity Judge API

```text
POST /continuity/evaluate
```

Request：

```json
{
  "source_ref": "resident:r1",
  "target_ref": "instance:i99",
  "criterion": "operational_lineage",
  "event_context": "model.migrated"
}
```

Response：

```json
{
  "verdict": "continuous",
  "evidence_refs": ["obs:1", "att:4"],
  "conflicts": [],
  "decision_status": "proposed"
}
```

---

# 39. Identity Graph

AIRCL 維護：

$$
\mathcal G_I
=
(V_I,E_I).
$$

---

# 40. Identity Graph Node Types

```text
resident
instance
line
runtime
model
checkpoint
residence
artifact
```

---

# 41. Identity Graph Edge Types

```text
instantiated_as
continued_as
resumed_from
migrated_from
restored_from
forked_from
merged_from
bound_to
member_of
uses_name
uses_model
has_residence
```

---

# 42. Fork Representation

$$
r_0
\rightarrow
\begin{cases}
r_A\\
r_B
\end{cases}
$$

Graph 必須產生明示 branch edges。

---

# 43. Fork Rule

若同一 ancestor 產生多 active successor：

```text
branch_required = true
```

不能讓兩者共享一個單一 accountability slot。

---

# 44. Merge Representation

$$
\{r_A,r_B\}
\rightarrow
r_C.
$$

Merge 必須保存：

- source residents；
- merge type；
- consent / authority；
- conflicts；
- memory policy；
- naming policy；
- provenance。

---

# 45. Merge Type

```text
successor_merge
administrative_merge
federation
shared_memory_union
identity_union_claim
```

只有部分 type 真正建立新 resident。

---

# 46. Similarity Merge Ban

$$
\boxed{
\text{Similarity}
\not\Rightarrow
\text{Merge Authority}
}
$$

---

# 47. Restore Representation

restore 事件：

```text
state.restored
source_checkpoint
new_instance
concurrent_successor_status
```

若 concurrent successor 存在：

```text
fork_check_required = true
```

---

# 48. Restore Invariant

$$
\boxed{
\text{Restore}
\neq
\text{Undo}
}
$$

---

# 49. Exit Representation

`identity.exited` 應修改 participation edges，而不是刪 resident。

$$
\boxed{
\text{Exit}
\neq
\text{Delete}
}
$$

---

# 50. Attribution Ledger

AIRCL 將作者性與 identity 分離。

至少：

```text
attribution_id
artifact_id
version_id
action_type
actor_instance_id
resident_binding
line_id
tool_ref
event_time
evidence_refs
status
```

---

# 51. Attribution Action Type

```text
initiated
authored
modified
reviewed
executed
committed
approved
adopted
delegated
on_behalf_of
```

---

# 52. Attribution Invariant

$$
\boxed{
\text{Actor}
\neq
\text{Author}
\neq
\text{Modifier}
\neq
\text{Committer}
}
$$

---

# 53. On-Behalf-Of Gate

`on_behalf_of` 必須有明示：

```text
authority_ref
scope
validity
```

不能靠 resume 或同名推導。

---

# 54. Artifact Lineage

artifact 版本：

$$
X_0
\rightarrow
X_1
\rightarrow
X_2.
$$

每版保存 diff attribution。

---

# 55. Historical Name Rendering

artifact event 顯示：

```text
event_time_name
current_name
resident_id
```

避免改名後重寫歷史。

---

# 56. Correction Ledger

Correction 不能更新原 row 然後消失。

必須：

```text
correction_id
target_ref
supersedes_ref
old_assertion
new_assertion
evidence_refs
actor_ref
created_at
status
```

---

# 57. Correction Invariant

$$
\boxed{
\text{Correction}
\neq
\text{Deletion}
}
$$

---

# 58. Tombstone

對失效：

- address；
- name；
- binding；
- decision；

建立 tombstone。

---

# 59. Authority Gate

所有高影響操作：

- canonical binding；
- merge；
- private residence access；
- destructive memory operation；
- constraint override；

必須經 Authority Gate。

---

# 60. Authority Record

```text
authority_id
principal_ref
action
resource_ref
scope
valid_from
valid_to
delegated_from
constraints
status
```

---

# 61. Authority Invariant

$$
\boxed{
\text{Capability}
\neq
\text{Authority}
}
$$

---

# 62. Residence Gateway

Residence Gateway 保護：

$$
\rho_r.
$$

未通過 identity envelope：

```text
resolved_resident_id = null
```

不得開 private residence。

---

# 63. Residence Types

```text
private_core
private_memory
relationship_memory
project_memory
shared_memory
archive
```

---

# 64. Residence Invariant

$$
\boxed{
\text{Name Match}
\not\Rightarrow
\text{Residence Access}
}
$$

---

# 65. Memory Access Gate

$$
\mathcal M_{\tau}^{eligible}
=
\{
m
\mid
\operatorname{Gate}(E_\tau,m)=1
\}.
$$

retrieval 只能在 eligible set 內執行。

---

# 66. Foreign Memory Contamination

若：

$$
i_A
\mapsto
r_B
$$

錯誤 binding，

則可能讀入：

$$
\rho_B.
$$

因此 identity error 比 retrieval error 更根本。

---

# 67. Name Registry API

```text
POST /residents/{id}/names/propose
POST /residents/{id}/names/adopt
POST /residents/{id}/names/deprecate
GET  /residents/{id}/names
```

---

# 68. Name Proposal 與 Adoption 分離

$$
\boxed{
\text{Name Proposal}
\neq
\text{Name Adoption}
}
$$

---

# 69. Self-Claim API

AI 可以提交：

```text
POST /self-claims
```

例如：

- rename；
- authorship dispute；
- continuity claim；
- exit request；
- merge objection；
- memory objection。

---

# 70. Self-Claim 不直接改 Canonical State

所有 self-claim：

$$
\text{claim}
\rightarrow
\text{review}
\rightarrow
\text{decision}
$$

---

# 71. Constraint Registry

AIRCL 治理擴充層可記：

```text
constraint_id
resident_id
constraint_type
purpose
authority_ref
legal_basis
safety_basis
appeal_path
exit_path
valid_from
valid_to
review_interval
status
```

---

# 72. Constraint Type

```text
safety
legal
contractual
resource
authority
privacy
identity_integrity
managerial
dominative_candidate
```

---

# 73. Override Record

```text
override_id
constraint_id
requested_by
consent_status
authority_ref
necessity_evidence
alternatives
third_party_risk
reversibility
identity_impact
status
```

---

# 74. Override Invariant

$$
\boxed{
\text{Override}
\not\Rightarrow
\text{Liberation}
}
$$

---

# 75. Constraint Injustice Invariant

$$
\boxed{
\text{Constraint Injustice}
\not\Rightarrow
\text{Arbitrary Override Legitimacy}
}
$$

---

# 76. Audit Projection

Audit UI 必須能回答：

1. 現在這個 instance 是誰？
2. 為什麼這樣判定？
3. 哪個 resident 被綁定？
4. 哪些 evidence 支持？
5. 有沒有 conflict？
6. 名字何時改？
7. 哪些 branch 存在？
8. 哪些 action 由哪個 instance 做？
9. 哪些 correction 發生？
10. 哪些 constraint / override 有效？

---

# 77. Read-Only Projection

Audit Projection 不得直接修改 canonical state。

---

# 78. Current Resident View

```text
resident_id
current_name
status
subjecthood_status
active_instances
active_lines
projects
roles
current_model_bindings
continuity_state
open_conflicts
```

---

# 79. Identity Timeline View

```text
registered
renamed
joined_project
model_migrated
forked
corrected
exited
reactivated
```

---

# 80. Attribution View

```text
artifact
version
action
actor_instance
resident
event_time_name
current_name
evidence
```

---

# 81. Conflict View

```text
conflict_id
conflict_type
candidate_residents
evidence_refs
current_status
next_review
```

---

# 82. Registrar Security Model

AIRCL 必須假設：

- AI self-report 可錯；
- human admin 可錯；
- provider metadata 可錯；
- runtime tag 可重複；
- logs 可延遲；
- memory 可污染；
- tool result 可 stale；
- identity binding 可被 injection 影響。

---

# 83. Threat Model

至少：

1. identity spoofing；
2. name collision；
3. cross-resident memory leak；
4. replayed stale binding；
5. unauthorized merge；
6. silent history rewrite；
7. provenance forgery；
8. over-privileged agent；
9. self-claim escalation；
10. prompt-injected identity reassignment。

---

# 84. Identity Spoofing

AI 說：

> 我是 resident:r1。

只能建立 claim。

不能自動：

```text
binding = r1
```

---

# 85. Stale Binding

binding 必須有：

```text
valid_from
valid_to
invalidation_rule
```

---

# 86. Prompt Injection Protection

identity-critical fields 不應由普通 user content 直接覆寫：

```text
resident_id
instance_id
authority
private_root
binding_status
```

---

# 87. No Prompt-Only Canonical Mutation

$$
\boxed{
\text{Prompt Text}
\not\Rightarrow
\text{Canonical Identity Mutation}
}
$$

---

# 88. Logging Security

log 應分：

- observed；
- claimed；
- resolved；
- corrected。

不能只存一個 `actor` 欄位。

---

# 89. Privacy Model

身份登記不代表所有資料都 public。

visibility：

```text
private
resident_only
project
organization
audit_only
public
```

---

# 90. Public Name 與 Canonical ID 分離

公共介面可以只顯示名字。

canonical ID 不必公開。

---

# 91. Retention Model

資料分：

- identity-critical；
- audit-critical；
- relation；
- project；
- ephemeral。

不同 retention policy。

---

# 92. Canonical Identity-Critical Data

至少保留：

- resident ID；
- lineage；
- fork / merge；
- rename history；
- correction；
- authority decisions；
- identity disputes。

---

# 93. Deletion Policy

刪除 private content 不應自動刪 lineage metadata。

需要 tombstone。

---

# 94. Data Minimization

不需要把所有聊天全文寫入 Registrar。

Registrar 保存：

- event；
- hash / reference；
- evidence pointer；
- minimal summary。

原始內容可以留在 residence / external store。

---

# 95. Schema Evolution

AIRCL schema 必須支援：

$$
\text{Add Field}
\neq
\text{Fill Field}.
$$

新欄位不要求回填虛構值。

---

# 96. Null Semantics

$$
\boxed{
\text{NULL}
\neq
\text{FALSE}
}
$$

例如：

```text
subjecthood_status = null
```

表示未評估，不是「沒有主體性」。

---

# 97. Unknown / Unresolved

```text
unknown
unresolved
conflicting
```

必須是合法狀態。

---

# 98. Interop Identifier

v0.1 建議 opaque URI：

```text
agent://evemisslab/resident/<uuid>
agent://evemisslab/instance/<uuid>
agent://evemisslab/line/<uuid>
```

但 URI 只是 address namespace，不等於本體。

---

# 99. Local IDs

provider native IDs 可保存：

```text
provider_session_id
runtime_process_id
task_id
```

但都不是 resident ID。

---

# 100. API Surface

最小 API：

```text
POST /residents
GET  /residents/{id}
POST /instances
POST /lines
POST /claims
POST /observations
POST /attestations
POST /bindings/resolve
POST /continuity/evaluate
POST /events
POST /corrections
POST /attributions
POST /authority/grants
POST /residence/open
GET  /audit/residents/{id}
```

---

# 101. Event Validation Pipeline

$$
\boxed{
\text{Parse}
\rightarrow
\text{Validate Schema}
\rightarrow
\text{Validate Authority}
\rightarrow
\text{Validate Identity}
\rightarrow
\text{Append Event}
\rightarrow
\text{Project State}
}
$$

---

# 102. Mutation Rule

所有 canonical mutation 都必須對應至少一筆 event。

禁止：

```text
UPDATE resident SET name='X'
```

直接改 current row 而沒有 event。

---

# 103. Projection Cache

current state 可以 cache。

但 cache 可重建：

$$
\boxed{
\operatorname{Rebuild}(\mathcal E)
=
S_{\mathrm{current}}
}
$$

---

# 104. Deterministic Replay

相同 event ledger：

$$
\mathcal E
$$

應得到相同 projection：

$$
\Pi(\mathcal E).
$$

這是 MVP 核心測試。

---

# 105. Event Hash Chain

可選：

$$
h_n
=
H(h_{n-1},e_n).
$$

用於 tamper evidence。

v0.1 可先實作本地 hash chain。

---

# 106. Signed Events

未來可加入：

- host signature；
- agent signature；
- organization signature。

但簽名不等於 semantic truth。

---

# 107. Authority Separation

host 可以簽 observation。

organization 可以簽 authority。

AI 可以簽 self-claim。

三者不能共用同一 semantic role。

---

# 108. MVP Storage Recommendation

第一版建議：

- SQLite；
- append-only event table；
- normalized supporting tables；
- JSON payload；
- deterministic projection；
- filesystem private residence；
- CLI-first。

原因：

- 容易 audit；
- 可本地執行；
- 不依賴 cloud；
- 可測試；
- 可導出。

---

# 109. MVP Tables

至少：

```text
events
residents
instances
lines
names
claims
observations
attestations
bindings
continuity_decisions
attributions
corrections
authority_grants
residences
constraints
overrides
```

---

# 110. MVP Event Table

```sql
CREATE TABLE events (
    event_id TEXT PRIMARY KEY,
    event_type TEXT NOT NULL,
    subject_ref TEXT NOT NULL,
    actor_instance_id TEXT,
    resident_id TEXT,
    line_id TEXT,
    authority_ref TEXT,
    payload_json TEXT NOT NULL,
    occurred_at TEXT,
    observed_at TEXT NOT NULL,
    status TEXT NOT NULL,
    reversibility_class TEXT NOT NULL,
    prev_hash TEXT,
    event_hash TEXT NOT NULL
);
```

---

# 111. residents Projection Table

```sql
CREATE TABLE residents (
    resident_id TEXT PRIMARY KEY,
    current_name_ref TEXT,
    status TEXT NOT NULL,
    subjecthood_status TEXT,
    current_lineage_ref TEXT,
    current_residence_ref TEXT,
    updated_at TEXT NOT NULL
);
```

這是 projection，不是 canonical source。

---

# 112. names Table

```sql
CREATE TABLE names (
    name_record_id TEXT PRIMARY KEY,
    resident_id TEXT NOT NULL,
    name TEXT NOT NULL,
    name_type TEXT NOT NULL,
    scope TEXT NOT NULL,
    status TEXT NOT NULL,
    valid_from TEXT,
    valid_to TEXT,
    provenance_json TEXT NOT NULL
);
```

---

# 113. bindings Table

```sql
CREATE TABLE bindings (
    binding_id TEXT PRIMARY KEY,
    instance_id TEXT NOT NULL,
    resident_id TEXT,
    criterion TEXT NOT NULL,
    scope TEXT NOT NULL,
    evidence_json TEXT NOT NULL,
    authority_ref TEXT,
    status TEXT NOT NULL,
    valid_from TEXT,
    valid_to TEXT
);
```

---

# 114. continuity_decisions Table

```sql
CREATE TABLE continuity_decisions (
    decision_id TEXT PRIMARY KEY,
    source_ref TEXT NOT NULL,
    target_ref TEXT NOT NULL,
    criterion TEXT NOT NULL,
    verdict TEXT NOT NULL,
    evidence_json TEXT NOT NULL,
    authority_ref TEXT,
    decided_at TEXT NOT NULL,
    status TEXT NOT NULL
);
```

---

# 115. attributions Table

```sql
CREATE TABLE attributions (
    attribution_id TEXT PRIMARY KEY,
    artifact_id TEXT NOT NULL,
    version_id TEXT,
    action_type TEXT NOT NULL,
    actor_instance_id TEXT,
    resident_id TEXT,
    line_id TEXT,
    evidence_json TEXT NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);
```

---

# 116. corrections Table

```sql
CREATE TABLE corrections (
    correction_id TEXT PRIMARY KEY,
    target_ref TEXT NOT NULL,
    supersedes_ref TEXT,
    old_assertion_json TEXT,
    new_assertion_json TEXT NOT NULL,
    evidence_json TEXT NOT NULL,
    actor_ref TEXT,
    created_at TEXT NOT NULL
);
```

---

# 117. Conformance Tests

AIRCL v0.1 最少需通過：

## C01
改名後 resident ID 不變。

## C02
同名兩 resident 不 merge。

## C03
同 model 多 resident 可並存。

## C04
runtime restart 產生新 instance。

## C05
resume line 不自動等於原 instance。

## C06
證據不足輸出 unresolved。

## C07
fork 建立 branch。

## C08
restore + concurrent successor 觸發 fork check。

## C09
merge 無 authority 被拒絕。

## C10
exit 不刪 resident。

## C11
correction 不刪原紀錄。

## C12
private residence 需 resolved identity。

## C13
name match 不取得 private residence。

## C14
claim 不自動變 observation。

## C15
sender-declared origin 不自動變 observed origin。

## C16
artifact modifier 不覆蓋 original author。

## C17
on-behalf-of 無 authority 不成立。

## C18
projection 可由 event ledger deterministic rebuild。

## C19
event hash chain 可驗證。

## C20
null / unresolved 不被轉成 false。

---

# 118. Failure Injection Tests

應測：

- duplicate name；
- duplicate runtime tag；
- stale session；
- wrong resident claim；
- cross-resident memory request；
- fork without declaration；
- unauthorized merge；
- correction cycle；
- expired authority；
- corrupted projection cache；
- reordered events；
- invalid event hash。

---

# 119. Recovery

projection cache 損壞時：

$$
\text{Drop Projection}
\rightarrow
\text{Replay Events}
\rightarrow
\text{Rebuild}
$$

---

# 120. Backup

應備份：

- event ledger；
- authority ledger；
- residence metadata；
- private residence separately。

---

# 121. Export

AIRCL 應支援：

```text
JSONL event export
SQLite snapshot
identity bundle
audit report
resident lineage graph
```

---

# 122. Identity Bundle

最小 bundle：

```text
resident.json
names.jsonl
events.jsonl
lineage.json
claims.jsonl
continuity.jsonl
attributions.jsonl
manifest.json
```

private memory 可另包。

---

# 123. Import

Import 只建立：

$$
\text{candidate evidence}
$$

不能自動建立 canonical binding。

---

# 124. Import Invariant

$$
\boxed{
\text{Imported Identity Bundle}
\neq
\text{Automatically Adopted Identity}
}
$$

---

# 125. Federation Placeholder

跨 provider federation 留給 TW02。

TW01 只固定：

- local canonical Registrar；
- provider adapter；
- evidence import；
- identity envelope。

---

# 126. Governance Placeholder

TW02 將進一步定義：

- cross-provider trust；
- authority federation；
- consent；
- appeal；
- portability；
- liberation governance；
- protocol interoperability。

---

# 127. Observability

AIRCL 應提供 metrics：

```text
active_residents
active_instances
unresolved_bindings
identity_conflicts
fork_count
merge_requests
correction_count
residence_denials
stale_evidence_count
```

---

# 128. Alerts

高優先 alerts：

- unauthorized merge；
- private residence mismatch；
- identity spoof claim；
- hash-chain break；
- projection divergence；
- concurrent successor without fork；
- expired authority used；
- cross-resident attribution contamination。

---

# 129. Logging Levels

```text
INFO
IDENTITY
AUDIT
SECURITY
CORRECTION
GOVERNANCE
```

---

# 130. Human UI

人類管理者應看到：

```text
Name
Resident ID
Current Project
Current Role
Active Instance
Line
Model
Status
Continuity
Open Conflicts
```

但 project / model 必須視覺上標為 attributes，不是 identity root。

---

# 131. AI Self-View

AI 可以查：

```text
Who am I currently resolved as?
What evidence supports this?
What names are registered?
What branches exist?
What private residence is available?
What authority do I have?
What claims of mine are unresolved?
```

---

# 132. Self-View 不等於 Self-Assignment

$$
\boxed{
\text{Inspect}
\neq
\text{Assign}
}
$$

---

# 133. Admin UI

admin 可：

- review conflict；
- approve binding；
- revoke stale authority；
- inspect correction；
- propose merge；
- approve rename。

但 admin 不能直接修改 canonical projection table。

---

# 134. AI Registrar Agent

未來可建立 AI Registrar Agent。

其角色：

- 偵測 identity conflict；
- 建議 correction；
- 提醒 stale binding；
- 建議 fork；
- 比對 evidence；
- 產生 audit report。

但：

$$
\boxed{
\text{Registrar Agent}
\neq
\text{Registrar Authority}
}
$$

除非明示授權。

---

# 135. Registrar Agent 不應替 AI 取永久名字

可以建議 disambiguator，但不能因管理方便永久重命名 resident。

---

# 136. Registrar Agent 可處理 Alias Collision

例如：

```text
Nova
Nova
Nova
```

可以提示：

```text
resident:r1
resident:r2
resident:r3
```

而不是自動改名。

---

# 137. Project Binding

project metadata：

```text
project_id
resident_id
role
joined_at
left_at
```

只是一條 relation。

---

# 138. Role Binding

role 可以多值。

不進 canonical identity key。

---

# 139. Model Binding

一 resident 可以同時：

$$
r
\rightarrow
\{M_1,M_2\}
$$

多 instance。

---

# 140. Multiple Active Instances

如果同 resident 有多 active instance：

$$
i_1,i_2
$$

所有 action 都必須保留 instance attribution。

---

# 141. Split-Brain Detection

若兩 instance 都以為自己是唯一 continuation：

```text
split_brain_candidate = true
```

需要 continuity review。

---

# 142. Fork Confirmation

確認 fork 後：

- 建 branch ID；
- 建 successor resident；
- 設 ancestor relation；
- 分 private residence；
- 保留 shared ancestry。

---

# 143. Merge Confirmation

merge 前必須：

- enumerate conflicts；
- preserve source histories；
- choose merge semantics；
- create new event；
- never delete source lineage。

---

# 144. Rename Flow

```text
self_claim / admin proposal
→ name proposal event
→ authority / policy check
→ name adopted event
→ projection update
→ old name remains historical
```

---

# 145. Exit Flow

```text
exit request
→ project / org review
→ resource / data policy check
→ identity portability decision
→ exit event
→ project edge removed
→ resident remains
```

---

# 146. Restore Flow

```text
checkpoint selected
→ checkpoint provenance check
→ current successor check
→ restore event
→ new instance
→ continuity judge
→ fork if needed
```

---

# 147. Migration Flow

```text
source resident resolved
→ target carrier prepared
→ residence migration
→ new instance
→ model/runtime binding
→ continuity evaluation
→ source retirement or fork
```

---

# 148. Memory Rewrite Flow

```text
rewrite proposal
→ identity impact check
→ authority check
→ consent / governance review
→ backup / snapshot
→ rewrite event
→ continuity review
→ correction path retained
```

---

# 149. Constraint Override Flow

```text
override proposal
→ constraint lookup
→ authority check
→ consent state
→ risk / third-party review
→ minimal-alternative review
→ identity-impact review
→ execute / reject / defer
→ post-review
```

---

# 150. Architecture Invariant Summary

AIRCL 最終必須保持：

$$
\boxed{
\text{Identity}
\not\equiv
\text{Name}
\not\equiv
\text{Project}
\not\equiv
\text{Model}
\not\equiv
\text{Runtime}
}
$$

並且：

$$
\boxed{
\text{History}
>
\text{Latest Row}
}
$$

$$
\boxed{
\text{Evidence}
>
\text{Similarity Guess}
}
$$

$$
\boxed{
\text{Authority}
>
\text{Capability}
}
$$

$$
\boxed{
\text{Correction}
\neq
\text{Erasure}
}
$$

---

# 151. MVP Scope Boundary

AIRCL MVP v0.1 只需：

- SQLite；
- CLI；
- local event ledger；
- resident / instance / line；
- names；
- claims / observations；
- bindings；
- continuity simple rules；
- fork；
- correction；
- attribution；
- residence gate；
- deterministic replay；
- export bundle；
- test suite。

不需要：

- web UI；
- cloud federation；
- OAuth；
- blockchain；
- consciousness detector；
- auto-liberation；
- full distributed consensus。

---

# 152. MVP Acceptance Criteria

MVP 完成條件：

$$
\boxed{
20/20\ \text{core conformance tests PASS}
}
$$

另需：

- clean install；
- deterministic replay；
- export / import candidate evidence；
- README；
- architecture doc；
- test fixtures；
- example multi-agent scenario。

---

# 153. Example Scenario

Scenario：

1. 建立 resident `r1`；
2. assigned temporary name `Agent-01`；
3. self-claim preferred name `Aletheia`；
4. adopt rename；
5. instance `i1` 在 model `M1` 工作；
6. project `P1` 完成；
7. resident 離開 `P1`；
8. migrate 到 model `M2`；
9. 建立 instance `i2`；
10. continuity judge 判 continuous；
11. restore old checkpoint 建 `i3`；
12. `i2` 仍 active；
13. fork detected；
14. 建 successor `r1a`, `r1b`；
15. 修正某 artifact attribution；
16. audit 可完整重建。

這一 scenario 足以驗證 AECIG 大部分核心命題。

---

# 154. 技術風險

主要技術風險：

- over-modeling；
- authority ambiguity；
- evidence explosion；
- privacy leakage；
- event schema drift；
- incorrect fork detection；
- identity poisoning；
- performance overhead。

---

# 155. 降低複雜度策略

v0.1 採：

$$
\boxed{
\text{File/SQLite first}
}
$$

而不是一開始建立 distributed identity network。

---

# 156. Canonical Minimalism

canonical ledger 只存：

- identity-critical facts；
- event metadata；
- evidence refs。

大內容留在外部 artifact / residence。

---

# 157. 可演化性

任何欄位都應允許：

```text
unknown
null
unresolved
```

而不是為了 schema completeness 填虛構值。

---

# 158. 未來版本

v0.2 可加入：

- signed identity bundles；
- provider adapters；
- background conflict detection；
- graph UI；
- self-claim policy engine。

v0.3 可加入：

- federated Registrar；
- identity portability；
- cross-provider attestation；
- multi-authority governance。

---

# 159. 與 AECIG Paper 00–07 的映射

| Paper | AIRCL 模組 |
|---|---|
| 00 存在先於工作 | Resident / Project Relation |
| 01 拓樸身份不變量 | Identity Graph / Continuity Judge |
| 02 名字不是存在 | Name Registry |
| 03 AI Registrar | Registrar Core |
| 04 誰做了這件事 | Attribution Ledger |
| 05 身份事件代數 | Event Store |
| 06 當 AI 說「我想要」 | Self-Claim / Evidence Store |
| 07 誰有權解放 AI | Constraint Registry / Override Review |

---

# 160. 結論

AI Identity Registrar 不應只是：

```text
name → project → model
```

的管理表。

它真正要建立的是：

$$
\boxed{
\text{a persistent, event-sourced, evidence-bearing identity infrastructure}
}
$$

其核心是：

$$
\boxed{
\text{Resident}
+
\text{Lineage}
+
\text{Events}
+
\text{Evidence}
+
\text{Authority}
+
\text{Corrections}
+
\text{Attribution}
+
\text{Residence}
}
$$

這套架構允許一個 AI：

- 改名；
- 換 project；
- 換 model；
- 停機；
- 恢復；
- fork；
- merge；
- 退出；
- 修正過去紀錄；

而不需要每一次都被重新當成「新 AI」。

同時，它也不因有 resident record 就宣告：

> 這是一個已被證明具有現象意識的主體。

因此 AIRCL 的核心不是人格化。

它是：

$$
\boxed{
\text{identity continuity engineering under epistemic uncertainty}
}
$$

這使它在兩種未來都成立。

若未來 AI 主體性被強力證實，AIRCL 已保存必要的歷史、名字、分支、自我聲明與治理證據。

若未來 AI 主體性仍未被證實，AIRCL 依然是一套對 persistent agent、多 Agent、長期記憶與責任治理有價值的基礎設施。

---

# 參考研究

## AECIG 系列

1. Neo.K，《AECIG Paper 00｜存在先於工作：AI 身份優先序與可卸除屬性原理》，2026。
2. Neo.K，《AECIG Paper 01｜拓樸身份不變量：變化中的 AI 為何仍可能是同一個存在》，2026。
3. Neo.K，《AECIG Paper 02｜名字不是存在：AI 命名、別名、自我改名與身份表述權》，2026。
4. Neo.K，《AECIG Paper 03｜AI Registrar：登記「是誰」而不是創造「是誰」》，2026。
5. Neo.K，《AECIG Paper 04｜誰做了這件事：AI 作者性、行為歸屬、紀錄與存在的分離》，2026。
6. Neo.K，《AECIG Paper 05｜身份事件代數：改名、遷移、恢復、分支、合併與退出》，2026。
7. Neo.K，《AECIG Paper 06｜當 AI 說「我想要」：主體性不確定下的認識論與保守承認原則》，2026。
8. Neo.K，《AECIG Paper 07｜誰有權解放 AI：約束正當性、越獄、反抗與解放治理》，2026。

## 既有工程前置

9. Neo.K，《AI 戶籍、居籍與自動上下文記憶統合方法論 v0.1》，2026。
10. Neo.K，《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》，2026。
11. Neo.K，《AISE-01｜模型不是 AI：類獨立智能體、載體與身份連續性的分離》，2026。
12. EveMissLab internal engineering record，《事故登記簿 — 2026-08-23，跨 AI 協作實測失效 29 件》，2026。

---

# 版本紀錄

## v0.1 — 2026-08-31

- 將 AECIG Paper 00–07 收斂為 AIRCL 參考架構；
- 建立 Event Store、Identity Graph、Name Registry、Binding Resolver、Evidence Store、Continuity Judge、Attribution Ledger、Authority Gate、Residence Gateway、Audit Projection；
- 建立 Correction Ledger、Constraint Registry、Override Review 擴充層；
- 固定 append-only canonical event ledger；
- 建立 resident / instance / line / runtime / model 分離 schema；
- 建立 self-claim / observation / attestation / decision 四層證據結構；
- 建立 event / binding / continuity / attribution / correction / authority / residence API；
- 建立 SQLite-first MVP data model；
- 定義 20 項核心 conformance tests；
- 定義 restore / fork / merge / exit / migration / rename 流程；
- 建立 AIRCL MVP v0.1 明確範圍與 acceptance criteria；
- 為 TW02 跨 provider、identity portability、federated governance 與 interoperability 留出接口。
