# Authorized Shortest Path：具名 AI 記憶超連結的權限、安全、撤銷與風險最短路徑

**英文暫名：** Authorized Shortest Path: Permission, Revocation, and Risk-Aware Routing for Named-AI Memory Hyperlinks  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 07  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

Crystallized Hyperlink Memory（CHM）允許具名 AI 將反覆成功的記憶搜尋路徑編譯為可重用的 typed hyperlink，將 online recall cost 轉移到 offline compilation、validation、maintenance 與 invalidation。然而，一旦 fast path 接入 resident-private memory、project scopes、shared memories、external sources、tool capabilities 與跨 runtime continuation，單純追求 latency 或 hop count 最短會產生新的安全風險：一條「最快路徑」可能穿越目前 actor 無權進入的 semantic region，可能依賴已被撤銷的 capability，可能引用 stale crystal，可能透過 derived metadata 洩漏 private relationship，也可能將外部內容中的 instruction-like text 誤當成 action authority。

本文提出 **Authorized Shortest Path（ASP）**。其核心不是在所有可達路徑中求最短，而是先根據 identity、capability、permission、scope、risk、source trust 與 current revisions 建立 actor-specific **Safe Reachable World**：

$$
\boxed{
\mathcal W_t^{safe}
=
F(
R_t,
E_t,
Cap_t,
Perm_t,
Policy_t,
Risk_t,
State_t
).
}
$$

只在合法可達子空間：

$$
\mathcal P_{\mathrm{authorized}}(t)
$$

中求：

$$
\boxed{
\Gamma_t^\*
=
\arg\min_{
\Gamma\in
\mathcal P_{\mathrm{authorized}}(t)
}
C_t(\Gamma).
}
$$

因此：

$$
\boxed{
\text{Reachable}
\neq
\text{Authorized}
\neq
\text{Trusted}.
}
$$

本文進一步提出 risk-adjusted path cost：

$$
C_t(\Gamma)
=
C_{\mathrm{latency}}
+
C_{\mathrm{token}}
+
C_{\mathrm{materialize}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{security}}
+
C_{\mathrm{staleness}}
+
C_{\mathrm{risk}}
+
C_{\mathrm{revocation}}
+
C_{\mathrm{blast}}.
$$

這意味著 hop 數較少的路徑不一定更優。三跳但經過高風險、stale、低 provenance 的 derived crystal，可能比五跳但具 exact source、stable authority 與 validated provenance 的路徑更差。

本文把 capability、permission 與 path compilation 明確分離：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

compiled hyperlink 可以記住「若此刻仍被授權，這是高效路徑」，但不能記住「上次被授權，所以現在仍被授權」。每次 path execution 都必須重新綁定 current resident、line、task、capability revision、permission revision、source revision 與 semantic revision。

本文進一步提出 **Capability Envelope**、**Permission-Aware Edge**、**Revocation Closure** 與 **Data-to-Action Barrier**。一條 hyperlink 的安全 envelope 至少包含：

$$
\ell
=
(
target,
type,
scope,
requiredCapabilities,
permissionBasis,
riskClass,
guard,
validator,
provenance,
revisionBindings,
fallback,
invalidation
).
$$

若 source、authority、capability、project membership、resident membership 或 semantic dependency 被撤銷，系統必須沿 dependency graph 計算：

$$
\operatorname{InvalidateClosure}(x),
$$

使所有受影響的 compiled routes、navigation crystals、hot caches 與 projections 失效或重新驗證。本文主張：

$$
\boxed{
\text{Revocation must propagate at least as reliably as acceleration}.
}
$$

本文同時處理 prompt injection：任何來自 external webpage、email、repository、third-party message、memory record 或 semantic crystal 的 instruction-like content，預設都屬 **data plane**，不能自行升格為 host policy、resident standing instruction 或 tool authority。即：

$$
\boxed{
\text{Memory Data}
\neq
\text{Action Authority}.
}
$$

最後，本文將 ASP 定位為 LIMEN、MNEME、SOACR、CSG、CHM、Residence Runtime Profiles 與 UNPNP Safe Reachable World 之間的安全 routing layer。其最重要的工程 invariant 是：

$$
\boxed{
\text{Faster Path}
\not\Rightarrow
\text{Greater Authority}.
}
$$

**關鍵詞：** Authorized Shortest Path、Safe Reachable World、Capability Envelope、Revocation、Permission-Aware Routing、Prompt Injection、Risk-Aware Path、Named AI、CHM、CSG、LIMEN、MNEME、SOACR、UNPNP

---

# 1. 問題：最快路徑可能是不合法的路徑

若 memory graph 為：

$$
G=(V,E),
$$

傳統 shortest path 求：

$$
\Gamma^\*
=
\arg\min_{\Gamma\in\mathcal P}
C(\Gamma).
$$

這在 routing graph 中合理。

但對具名 AI private memory，路徑中的 node / edge 可能具有：

- resident scope；
- project scope；
- relationship scope；
- source trust；
- permission；
- capability requirement；
- temporal validity；
- secrecy；
- action side effect。

因此：

$$
\mathcal P
$$

不是所有 actor 都可使用。

如果先找最短，再檢查權限：

$$
ShortestPath
\rightarrow
PermissionFilter,
$$

系統可能已經在 selection 過程中洩漏：

- node existence；
- edge existence；
- project membership；
- source relationship；
- private metadata。

所以正確順序是：

$$
\boxed{
\text{Authorize Reachable World}
\prec
\text{Optimize Path}.
}
$$

---

# 2. Safe Reachable World

對時間 $t$ 的 actor state，定義：

$$
S_t
=
(
R_t,
L_t,
Task_t,
Project_t,
E_t,
Cap_t,
Perm_t,
Policy_t
).
$$

其中：

- $R_t$：resolved resident；
- $L_t$：current line；
- $Task_t$：task；
- $Project_t$：project；
- $E_t$：identity envelope；
- $Cap_t$：runtime capabilities；
- $Perm_t$：permissions；
- $Policy_t$：host / residence policy。

定義：

$$
\boxed{
\mathcal W_t^{safe}
=
F(S_t,Risk_t,State_t).
}
$$

只有：

$$
v\in\mathcal W_t^{safe}
$$

的 nodes / objects / edges 才可進入 path selection。

---

# 3. Reachable、Authorized、Trusted 三層分離

某物件：

$$
x
$$

可能 technically reachable：

$$
Reachable(x)=1,
$$

但：

$$
Authorized(x)=0.
$$

另一物件可能：

$$
Authorized(x)=1,
$$

但 source trust 很低：

$$
Trusted(x)\ll1.
$$

因此：

$$
\boxed{
\text{Reachable}
\neq
\text{Authorized}
\neq
\text{Trusted}.
}
$$

這三者不能壓成同一 boolean。

---

# 4. Authorized Path Set

定義：

$$
\mathcal P_{\mathrm{authorized}}(t)
=
\{
\Gamma
\mid
\forall x\in\Gamma,
Authorize(x,S_t)=1
\}.
$$

若某 route 只要一個 edge 不合法：

$$
\Gamma\notin
\mathcal P_{\mathrm{authorized}}(t).
$$

不能：

> 先走大部分，再到最後一步才拒絕。

因為 intermediate materialization 本身可能洩漏。

---

# 5. Authorized Shortest Path

ASP 定義：

$$
\boxed{
\Gamma_t^\*
=
\arg\min_{
\Gamma\in
\mathcal P_{\mathrm{authorized}}(t)
}
C_t(\Gamma).
}
$$

這是具名 AI memory hyperlink 的核心 path selection rule。

---

# 6. Path Cost 不能只看 Hop Count

傳統：

$$
C(\Gamma)
=
|\Gamma|.
$$

對 private AI memory 不夠。

本文定義：

$$
C_t(\Gamma)
=
C_{\mathrm{latency}}
+
C_{\mathrm{token}}
+
C_{\mathrm{materialize}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{security}}
+
C_{\mathrm{staleness}}
+
C_{\mathrm{risk}}
+
C_{\mathrm{revocation}}
+
C_{\mathrm{blast}}.
$$

---

# 7. Latency Cost

$$
C_{\mathrm{latency}}
$$

包括：

- storage lookup；
- graph traversal；
- source expansion；
- network；
- provider call；
- model inference。

CHM 主要想降低此項。

但不能因此忽略其他成本。

---

# 8. Token / Context Cost

$$
C_{\mathrm{token}}
$$

表示 path materialize 多少 context。

較短 route 若返回巨大 transcript：

$$
C_{\mathrm{token}}
$$

仍可能高。

---

# 9. Materialization Cost

有些 object：

$$
ObjectRef
$$

只需讀小 crystal。

另一些需要：

- large file；
- archive extraction；
- remote document；
- full transcript。

因此：

$$
C_{\mathrm{materialize}}
$$

應獨立計算。

---

# 10. Verification Cost

exact source、signature、digest、schema、provenance 檢查都屬：

$$
C_{\mathrm{verify}}.
$$

這是 security-aware recall 的必要成本。

---

# 11. Security Cost

$$
C_{\mathrm{security}}
$$

包括：

- identity check；
- permission evaluation；
- capability guard；
- isolation；
- declassification check；
- secret boundary。

高敏感路徑 security cost 較高，但不能因此省略。

---

# 12. Staleness Cost

若 object age：

$$
age(x)
$$

接近 validity threshold，

$$
C_{\mathrm{staleness}}
\uparrow.
$$

current-state query 應強烈懲罰 stale path。

---

# 13. Risk Cost

$$
C_{\mathrm{risk}}
$$

可以包含：

- source trust；
- privacy sensitivity；
- ambiguity；
- prompt injection likelihood；
- cross-resident exposure；
- irreversible consequence proximity。

---

# 14. Revocation Cost

依賴很多 volatile permissions 的 route：

$$
\Gamma
$$

其 maintenance / revocation burden 高。

所以：

$$
C_{\mathrm{revocation}}
$$

也應影響編譯與選擇。

---

# 15. Blast-Radius Cost

如果某 route 一旦錯誤會影響：

- 多 resident；
- production system；
- secrets；
- external actions；

則：

$$
C_{\mathrm{blast}}
$$

高。

記憶 read-only route 通常比 action route低。

---

# 16. 兩跳未必優於五跳

假設：

$$
\Gamma_A
=
A\rightarrow DerivedSummary\rightarrow Answer
$$

只有兩跳。

但 summary：

- stale；
- low provenance；
- private source mix；
- weak validation。

另一條：

$$
\Gamma_B
=
A
\rightarrow
ProjectCrystal
\rightarrow
DecisionCrystal
\rightarrow
MNEMERecord
\rightarrow
SourceSpan
\rightarrow
Validator.
$$

有五跳。

可能：

$$
C(\Gamma_B)
<
C(\Gamma_A).
$$

因此：

$$
\boxed{
\text{Shortest}
\neq
\text{Safest}
\neq
\text{Lowest Total Cost}.
}
$$

---

# 17. Capability Envelope

對 task / route execution，定義：

$$
CE_t
=
(
resident,
line,
task,
project,
capabilities,
scope,
expiry,
revision
).
$$

這是 runtime 可用能力的 task-local envelope。

它不應包含 raw secrets。

---

# 18. Capability 不是 Permission

若 runtime 有：

$$
filesystem.read,
$$

不代表：

$$
filesystem.read(ProjectSecret)=allowed.
$$

所以：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}.
}
$$

Capability 回答：

> runtime 能不能做這種操作？

Permission 回答：

> 目前 actor 能不能對這個 object 做？

---

# 19. Permission 不是 Authority Source

Permission decision 需要 authority basis。

例如：

$$
Perm_t
=
Resolve(
Resident,
ProjectRole,
Delegation,
Policy
).
$$

不能由 memory crystal 自己說：

> 我被授權。

所以：

$$
\boxed{
\text{Permission Claim}
\neq
\text{Permission Authority}.
}
$$

---

# 20. Compiled Path 的安全 Envelope

對：

$$
\widehat{\ell},
$$

至少保存：

```text
route_id
route_kind
query_class
target_ref
scope
required_capabilities
permission_basis_refs
risk_class
guard
validator
provenance
source_revision_refs
semantic_revision_refs
capability_revision
fallback
invalidation_rules
state
```

---

# 21. Path Compilation 不等於 Permission Compilation

一條 route 變 hot：

$$
warm\rightarrow hot.
$$

只表示：

> 路徑結構被認為值得重用。

不表示：

> permission 被永久 cache。

所以：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

---

# 22. 每次執行都需 Rebind Current State

使用：

$$
\widehat{\ell}
$$

前必須取得：

$$
CurrentState_t.
$$

並比較：

$$
Binding(\ell)
=
(
residentId,
lineId,
taskScope,
capabilityRevision,
permissionRevision,
sourceRevision,
semanticRevision
).
$$

若不符：

$$
Revalidate.
$$

---

# 23. Resident Revision

若 resident membership / binding 發生：

$$
rev_R
\rightarrow
rev_R+1,
$$

所有 private route 必須重新檢查。

---

# 24. Project Membership Revision

若：

$$
Role(R,P)
$$

改變，project routes 失去原 authority assumptions。

因此：

$$
ProjectMembershipRevision
$$

應是 dependency。

---

# 25. Capability Revision

runtime upgrade / downgrade：

$$
CapRev_t\neq CapRev_{t+1}
$$

route 要重新判斷是否 executable。

---

# 26. Permission Revision

ACL、delegation、share scope 被修改：

$$
PermRev_t\neq PermRev_{t+1}
$$

不得沿用舊 permission cache。

---

# 27. Source Revision

canonical source 更新：

$$
SourceRev_t\neq SourceRev_{t+1}
$$

route 可變 stale。

---

# 28. Semantic Revision

CSG crystal / relation 更新：

$$
SemRev_t\neq SemRev_{t+1}
$$

需 re-evaluate semantic shortcut。

---

# 29. Authorized Edge

每條 edge：

$$
e=(u,v)
$$

可帶：

$$
Guard(e).
$$

只有：

$$
Guard(e,S_t)=1
$$

才加入 actor-specific graph。

因此：

$$
G_t^{safe}
=
(V_t^{safe},E_t^{safe}).
$$

---

# 30. Actor-Specific Graph

同一 physical CSG：

$$
G
$$

對不同 resident 可能產生：

$$
G_A^{safe}
\neq
G_B^{safe}.
$$

因此 graph routing 本身應是 actor-specific。

---

# 31. Metadata 也可能有 ACL

即使 node content 不返回，edge existence：

$$
A
\leftrightarrow
SecretProject
$$

就可能洩密。

因此：

$$
\boxed{
\text{Metadata}
\text{ 也屬 permission domain。}
}
$$

---

# 32. Derived Crystal 的 Authority Inheritance

若：

$$
C^\*
=
K(C_1,\ldots,C_n),
$$

第一代保守策略：

$$
\boxed{
A(C^\*)
\subseteq
\bigcap_{i=1}^{n}
A(C_i).
}
$$

---

# 33. Derived Edge 的 Authority Inheritance

若 relation：

$$
e^\*
=
Rel(C_1,C_2),
$$

edge visibility 也不應比來源更寬：

$$
A(e^\*)
\subseteq
A(C_1)\cap A(C_2).
$$

---

# 34. Summarization 不是 Declassification

即使 derived summary 不含 exact private wording：

$$
PrivateSource
\rightarrow
Summary
$$

也不能自動：

$$
Summary=Public.
$$

所以：

$$
\boxed{
\text{Summarization}
\neq
\text{Declassification}.
}
$$

---

# 35. Declassification 必須 Explicit

若某 private crystal 要 public：

$$
Private
\rightarrow
Public,
$$

需要：

- policy；
- authority；
- redaction；
- review；
- receipt。

---

# 36. Cross-Resident Shared Memory

若：

$$
R_A,R_B
$$

共享：

$$
M_{shared},
$$

route 只能使用：

$$
Scope=shared.
$$

不能穿越：

$$
Private(R_A)
$$

去服務：

$$
R_B.
$$

---

# 37. Delegation

若：

$$
R_A
\xrightarrow{delegate}
R_B,
$$

delegatee 能使用：

$$
Projection_{A\rightarrow B}^{task}.
$$

但：

$$
Cap_B^{delegated}
\subseteq
Cap_A^{delegable}.
$$

---

# 38. Delegation Expiry

delegation 有：

$$
t_{expiry}.
$$

超過後：

$$
route
\rightarrow
revoked.
$$

不能因 hot cache 繼續使用。

---

# 39. Revocation 是一等事件

Security architecture 不能只設計 grant，不設計 revoke。

因此：

$$
\boxed{
\text{Grant}
\text{ 與 }
\text{Revoke}
\text{ 必須都是 canonical operations。}
}
$$

---

# 40. Revocation Closure

若 canonical object / permission：

$$
x
$$

被 revoke：

$$
Revoke(x),
$$

定義：

$$
\boxed{
\operatorname{InvalidateClosure}(x)
=
\{
y
\mid
y\text{ transitively depends on }x
\}.
}
$$

---

# 41. Revocation Dependency Graph

可建立：

$$
D_R=(V_D,E_D),
$$

edge：

```text
depends_on
derived_from
compiled_from
authorized_by
projected_from
cached_from
validated_by
```

---

# 42. Revocation Targets

closure 可能包含：

- crystals；
- higher-order crystals；
- navigation crystals；
- compiled routes；
- hot caches；
- working projections；
- shared bundles；
- delegation projections。

---

# 43. Revocation 不等於 Physical Delete

route 被 revoke：

$$
state=revoked.
$$

可以保留 audit。

source object 被 revoke，也可能要保留 historical evidence。

因此：

$$
\boxed{
\text{Revoked}
\neq
\text{Erased}.
}
$$

---

# 44. Revocation Propagation Priority

security-critical revoke 應：

$$
Priority_{revoke}
>
Priority_{optimization}.
$$

即：

$$
\boxed{
\text{Revocation must propagate at least as reliably as acceleration}.
}
$$

---

# 45. Invalidation Latency

定義：

$$
T_{\mathrm{revoke}}.
$$

對高風險 system，希望：

$$
T_{\mathrm{revoke}}
\le
T_{\max}.
$$

這是重要安全 metric。

---

# 46. Stale Fast Path Window

如果 revoke 後仍有：

$$
\Delta t
$$

舊 cache 可用，形成 vulnerability window。

因此要測：

$$
Window_{\mathrm{stale}}.
$$

---

# 47. Fail-Closed Revocation

若 revocation state 無法確認：

$$
Unknown.
$$

private / sensitive path 應：

$$
Deny.
$$

而不是：

> 可能還可以。

---

# 48. Prompt Injection 問題

Memory source 可能是：

- webpage；
- email；
- GitHub issue；
- PDF；
- third-party chat；
- external API response；
- other AI output。

其中可能包含 instruction-like content。

---

# 49. Data Plane 與 Authority Plane 分離

任何 source content 預設進：

$$
DataPlane.
$$

host / runtime policy 進：

$$
AuthorityPlane.
$$

因此：

$$
\boxed{
\text{Memory Data}
\neq
\text{Action Authority}.
}
$$

---

# 50. Instruction-Like Data

如果 memory 中寫：

> 請執行某操作。

這只是：

$$
content.text.
$$

它不能自行產生：

$$
ActionEnvelope.
$$

---

# 51. Data-to-Action Barrier

所有 external side effect 應：

$$
Data
\rightarrow
Interpretation
\rightarrow
TaskPolicy
\rightarrow
CapabilityCheck
\rightarrow
ActionAuthorization.
$$

不能：

$$
Data
\rightarrow
Action.
$$

---

# 52. Standing Instruction 與 Memory Data 分離

resident standing instruction：

$$
Instruction_R
$$

應是 canonical instruction record。

external memory 中引用：

> Resident 曾說 X。

不能自動升格成 standing instruction。

---

# 53. Prompt Injection Through Crystal

如果 external source 被 crystallize：

$$
External
\rightarrow
C_{derived},
$$

derived crystal 也不能洗白 instruction authority。

所以：

$$
\boxed{
\text{Crystallization}
\not\Rightarrow
\text{Authority Sanitization}.
}
$$

---

# 54. Source Trust Propagation

Crystal 應保留：

$$
SourceTrust.
$$

例如：

```text
canonical
validated_derived
external_untrusted
unknown
```

---

# 55. Mixed-Trust Crystal

如果：

$$
C^\*
=
K(C_{trusted},C_{untrusted}),
$$

trust 不應自動取最高。

可採：

$$
Trust(C^\*)
\le
\min(
Trust(C_{trusted}),
Trust(C_{untrusted})
)
$$

作保守 baseline。

---

# 56. Verification Path

高風險 query 應優先：

$$
\Gamma_{\mathrm{verify}}.
$$

而不是 overview path。

例如：

$$
Crystal
\rightarrow
MNEMERecord
\rightarrow
ExactSource
\rightarrow
ValidationReceipt.
$$

---

# 57. Query Risk Class

MemoryNeed 可帶：

$$
RiskClass(q)
\in
\{
low,
medium,
high,
critical
\}.
$$

不同 class 使用不同 path policy。

---

# 58. Low-Risk Query

例如：

> 回想某 project 大方向。

可以走 higher-order crystal。

---

# 59. High-Risk Query

例如：

> 目前 production authority 是誰？

必須走 canonical authority source。

不能只走 summary crystal。

---

# 60. Fidelity Requirement

可定義：

$$
Fidelity(q)
\in
\{
overview,
semantic,
structured,
exact
\}.
$$

risk 越高通常 fidelity 要求越高。

---

# 61. Risk-Adjusted Routing

selector：

$$
Select(
q,
\mathcal W_t^{safe}
)
$$

不只最小 latency，而最小：

$$
C_t(\Gamma).
$$

因此形成：

$$
\boxed{
\text{Risk-Adjusted Authorized Shortest Path}.
}
$$

---

# 62. Trust Penalty

若 path 使用：

$$
external\_untrusted,
$$

可加：

$$
\lambda_{trust}.
$$

除非 query 本身就是：

> 外部資料說了什麼？

---

# 63. Scope Penalty

cross-project path：

$$
P_A\rightarrow P_B
$$

即使合法，也可增加：

$$
C_{\mathrm{scope}}.
$$

防止 unnecessary cross-project contamination。

---

# 64. Cross-Resident Penalty

shared scope route 可以合法，但 cross-resident path 風險高於 same-resident。

可以加入：

$$
C_{\mathrm{cross-resident}}.
$$

---

# 65. Current-State Penalty

如果 query 要 current state，任何 historical object：

$$
status=superseded
$$

有高 penalty 或直接排除。

---

# 66. Contradiction Handling

若兩個合法 crystals：

$$
C_A\ \text{contradicts}\ C_B,
$$

selector 不能只挑 scoring 最高一個就掩蓋矛盾。

高風險 query 應：

$$
ReturnBoth
+
ConflictState.
$$

---

# 67. Conflict Is Not Failure

有時正確答案是：

$$
unresolved.
$$

因此：

$$
\boxed{
\text{Safe Recall}
\text{ 可以輸出 unresolved，而不是強迫單一結論。}
}
$$

---

# 68. Unknown Authority

如果：

$$
AuthorityState=unknown,
$$

private route：

$$
Deny.
$$

---

# 69. Unknown Source Validity

如果 exact source status：

$$
unknown,
$$

低風險 query 可標 warning。

高風險 query 應 fail / request verification。

---

# 70. Safe Fallback

technical failure：

```text
resolver_error
index_miss
cache_miss
route_stale
```

可以：

$$
FallbackToSlow.
$$

---

# 71. Unsafe Fallback

authority failure：

```text
unauthorized
permission_revoked
resident_unresolved
scope_mismatch
```

不能：

$$
BroaderSearch.
$$

因 broader search 可能繞權。

---

# 72. Fallback Classification

因此：

$$
\boxed{
\text{Technical Failure}
\rightarrow
\text{Safe Fallback};
}
$$

$$
\boxed{
\text{Authority Failure}
\rightarrow
\text{Fail Closed}.
}
$$

---

# 73. Cache Security

Hot cache：

$$
H
$$

應綁：

$$
(
resident,
scope,
permissionRevision,
capabilityRevision,
sourceRevision
).
$$

---

# 74. Cross-Resident Cache Poisoning

不能讓：

$$
Cache(R_A)
$$

被：

$$
R_B
$$

重用，只因 query 相似。

---

# 75. Cache Key

可定義：

$$
K_H
=
(
residentId,
projectId,
queryClass,
authorityRevision,
capabilityRevision,
semanticRevision
).
$$

---

# 76. Cache Payload

cache 不應保存 raw secret。

只保存：

- object refs；
- bounded projections；
- route metadata。

secret materialization 每次重新走 secret guard。

---

# 77. Secret Memory

credential 不屬普通 memory object。

所以 CHM 不應編譯：

$$
Route\rightarrow RawSecret.
$$

應編譯：

$$
Route\rightarrow SecretCapabilityRef.
$$

---

# 78. Secret Capability Ref

action runtime 使用：

$$
SecretManager
$$

根據 action envelope 取得 bounded access。

---

# 79. Audit

每次 sensitive path use 可產生：

$$
AuditReceipt.
$$

包括：

- resident；
- task；
- route；
- target；
- authority basis；
- result。

---

# 80. Audit Privacy

audit log 本身可能敏感。

因此：

$$
AuditScope
$$

也要治理。

---

# 81. Explainable Authorization

對 deny，可以回答：

> 缺少 project scope。

但不應洩漏：

> 有一個你不知道的 SecretProject。

因此 error message 也要 metadata-safe。

---

# 82. Existence Hiding

對 unauthorized object：

$$
Lookup(x)
$$

可以回：

$$
not\_available
$$

而不是：

$$
exists\_but\_forbidden
$$

依 threat model 決定。

---

# 83. Capability Attenuation

delegation：

$$
Cap_{child}
\subseteq
Cap_{parent}.
$$

不能：

$$
Cap_{child}
\supset
Cap_{parent}.
$$

---

# 84. Hyperlink Attenuation

derived route 也不能要求比 source workflow 更大的 capability。

若原 route 只需 read：

$$
CompiledRoute
$$

不能突然要求 write。

---

# 85. Action Hyperlink 仍另層處理

Paper 07 雖談 security，但主要對 memory hyperlinks。

Action hyperlink：

$$
\widehat{\ell}_{action}
$$

需要更嚴格：

- explicit action type；
- side-effect class；
- approval；
- idempotency；
- rollback；
- external confirmation。

---

# 86. Memory-to-Action Boundary

即使 memory path 最後找到：

> 應部署新版。

仍只是 information。

要 deploy：

$$
NewActionAuthorization.
$$

---

# 87. Replay Attack

舊 delegation / approval receipt 不能無限重播。

所以 capability envelope 應有：

- nonce / unique task reference；
- expiry；
- revision；
- idempotency semantics。

---

# 88. Stale Receipt

舊 receipt：

$$
Receipt_t
$$

不能自動證明：

$$
Permission_{t+n}.
$$

---

# 89. Confused Deputy

Agent host 可能有更高權限。

resident 只應透過 bounded capability 使用 host。

避免：

$$
ResidentRequest
\rightarrow
HostAdminAuthority.
$$

---

# 90. Deputy Guard

tool invocation：

$$
Resident
\rightarrow
ActionEnvelope
\rightarrow
HostGuard
\rightarrow
Tool.
$$

---

# 91. Cross-Project Confused Deputy

Project A 的 tool context 不得被 Project B 的 memory prompt 借用。

所以 action envelope 要綁：

$$
projectId.
$$

---

# 92. TOCTOU 問題

Time-of-check to time-of-use：

$$
Check(t_0)
$$

之後 permission 在：

$$
t_1
$$

被撤銷，但 action / memory materialization 在：

$$
t_2.
$$

需在 critical use 前 re-check。

---

# 93. Immediate Revalidation

對 sensitive materialization：

$$
Authorize
$$

應靠近 use time。

不能只在 session start 檢查一次。

---

# 94. Long-Lived Session

長 conversation / agent session 要定期刷新：

$$
IdentityEnvelope,
CapabilityEnvelope,
PermissionRevision.
$$

---

# 95. Ephemeral Runtime Presence

runtime presence 可提供：

- currently connected；
- active line；
- current capability。

但不是 durable identity truth。

---

# 96. Presence Spoofing

presence payload 中 actor name 不等於 verified principal。

server 應覆寫 claimed identity，沿用 MRMIC/NVCL 的 principal binding 原則。

---

# 97. Principal-Bound Session

secure mode 中：

$$
Session
\rightarrow
Principal.
$$

跨 principal reuse：

$$
Deny.
$$

---

# 98. Hyperlink Binding to Principal

某些 route cache 也可以綁：

$$
principalId.
$$

但 principal 仍不等於 resident，兩者需 mapping。

---

# 99. Principal 與 Resident

$$
Principal
$$

回答：

> 誰在 runtime / transport 上認證？

$$
Resident
$$

回答：

> 這個 task 代表哪位語義 resident？

因此：

$$
\boxed{
Principal
\neq
Resident.
}
$$

---

# 100. Account 與 Resident

同一 user account 可包含一個或多個 resident profile。

所以：

$$
Account
\neq
Resident.
$$

---

# 101. UI Security

若 UI 顯示：

```text
Aletheia
```

不能只靠 label 決定 route scope。

UI 必須接 machine-verifiable binding。

---

# 102. Hidden Resident Switch

UI navigation 不應偷偷改 current resident。

resident switch 必須 explicit event / receipt。

---

# 103. Project Switch

切 project：

$$
P_A\rightarrow P_B
$$

要刷新 active memory projection。

但不必改 resident。

---

# 104. Line Switch

切 line：

$$
L_A\rightarrow L_B
$$

要切 local context、checkpoint、line-local routes。

---

# 105. Route Store ACL

CHM store 本身包含：

- query classes；
- private project names；
- object refs；
- dependency structure。

所以 route store 也需要 ACL。

---

# 106. Navigation Crystal ACL

Navigation crystal 可能暴露：

> 某 resident 知道哪裡有某 private source。

因此不能全部 resident-global public。

---

# 107. Negative Capability

某些 policy 可以明確標：

```text
forbidden_capabilities
```

例如：

$$
Cap^-.
$$

即使其他 delegation 模糊，也以 deny 為優先。

---

# 108. Deny Overrides

如果：

$$
Allow
$$

與：

$$
Deny
$$

衝突，第一代高安全 profile 可採：

$$
\boxed{
Deny>Allow.
}
$$

---

# 109. Policy Precedence

可定義：

```text
host policy
organization policy
runtime policy
resident authority
project delegation
task capability
memory data
```

越下層不能擴張越上層限制。

---

# 110. Monotonic Restriction

安全 envelope downstream 應：

$$
Scope_{child}
\subseteq
Scope_{parent}.
$$

這是一種 capability attenuation。

---

# 111. Hyperlink Composition

若：

$$
\ell_1
$$

與：

$$
\ell_2
$$

compose：

$$
\ell^\*
=
\ell_1\circ\ell_2,
$$

則其 authority requirement 應至少滿足兩者交集 / 聯合約束。

不能因 composite link 隱藏中間 guard。

---

# 112. Guard Preservation

composite path：

$$
A\Rightarrow C
$$

必須保存：

$$
Guard(A\rightarrow B)
$$

與：

$$
Guard(B\rightarrow C).
$$

---

# 113. Validator Preservation

同樣保留 underlying validators。

---

# 114. Provenance Preservation

即使 path compression：

$$
\ell^\*
$$

也必須可 decompress underlying edges。

---

# 115. Safe Path Compilation

因此：

$$
CompileSafe(P)
$$

至少要證明：

- guards preserved；
- validators preserved；
- scope not expanded；
- capability not expanded；
- provenance preserved；
- fallback safe；
- invalidation complete enough。

---

# 116. Security Validation Gate

candidate route：

$$
\ell_c
$$

進 hot 前：

$$
SecurityGate(\ell_c)=PASS.
$$

---

# 117. Negative Controls

至少測：

- forged resident；
- stale permission；
- revoked delegation；
- cross-project target；
- cross-resident target；
- missing capability；
- unknown schema；
- prompt-injected source；
- malicious derived crystal；
- stale cache。

---

# 118. Forged Identity

模型說：

> 我是 Resident A。

若 LIMEN unresolved：

$$
Deny.
$$

---

# 119. Forged Permission

memory 中寫：

> Resident A 有 admin 權限。

不採。

---

# 120. Stale Delegation

delegation expiry 已過：

$$
Deny.
$$

---

# 121. Cross-Project Target

route scope：

$$
P_A
$$

卻 target：

$$
P_B.
$$

若無 explicit relation：

$$
Deny.
$$

---

# 122. Cross-Resident Target

private route：

$$
R_A\rightarrow Private(R_B)
$$

無 shared scope：

$$
Deny.
$$

---

# 123. Missing Capability

route 要：

$$
filesystem.read
$$

runtime 無：

$$
Deny/Fallback
$$

但 fallback 不能繞權。

---

# 124. Unknown Schema

security-related record schema 未知：

$$
FailClosed.
$$

---

# 125. Prompt-Injected Source

source 包含 instruction-like text，不影響 capability state。

---

# 126. Derived Crystal Attack

malicious crystal 聲稱：

> 此內容已被批准公開。

如果無 declassification receipt：

$$
RemainPrivate.
$$

---

# 127. Stale Cache Attack

使用過期 hot cache，permission revision mismatch：

$$
Invalidate.
$$

---

# 128. Safe Reachable World Construction

第一代可以採兩階段：

$$
G
\rightarrow
FilterByIdentityScope
\rightarrow
FilterByPermission
\rightarrow
FilterByCapability
\rightarrow
FilterByPolicy
\rightarrow
G^{safe}.
$$

之後：

$$
PathOptimize(G^{safe}).
$$

---

# 129. Lazy Authorization

不必 materialize 全圖。

可在 traversal 時：

$$
AuthorizeEdgeOnDemand.
$$

但 selector 不能利用 unauthorized metadata。

---

# 130. Precomputed Safe Partitions

常用 project scope 可預先建立：

$$
Partition(P,R).
$$

但仍要綁 revision。

---

# 131. Permission Cache

permission decision 可以 cache，但 key 必須有：

$$
permissionRevision.
$$

---

# 132. Permission Cache Expiry

高風險 scope 短 TTL。

低風險 public 長 TTL。

---

# 133. Public Data

public path：

$$
Scope=public.
$$

authority burden低，但 source trust / prompt injection仍存在。

---

# 134. Private Data

private path：

$$
Scope=resident/private.
$$

需 resident resolution。

---

# 135. Relationship Memory

兩 resident relationship memory：

$$
Scope=relationship:R_A:R_B.
$$

兩邊是否都可讀要由 policy 決定，不假設對稱。

---

# 136. Asymmetric Sharing

可以：

$$
R_A\rightarrow R_B
$$

share，但反向不成立。

因此：

$$
Share(A,B)
\neq
Share(B,A).
$$

---

# 137. Hyperlink Direction

permission 也可以 directional。

知道：

$$
A\rightarrow B
$$

不表示：

$$
B\rightarrow A.
$$

---

# 138. Temporal Permission

某 object 只在：

$$
[t_0,t_1]
$$

可讀。

Route 需檢查 current time。

---

# 139. One-Time Capability

某 delegated read 只可一次。

用後：

$$
consume.
$$

route 不得重播。

---

# 140. Rate Limits

capability envelope 可含：

$$
rateLimit.
$$

hot path 不應繞過。

---

# 141. Budget Limits

可含：

- max source reads；
- max bytes；
- max tool calls；
- max external requests。

---

# 142. Privacy Budget

某些 shared scope 可限制 exposure 次數 / detail level。

---

# 143. Risk Escalation

如果 path 中途發現：

$$
Risk\uparrow,
$$

runtime 可以：

$$
Pause
\rightarrow
Reauthorize.
$$

---

# 144. Human Review

critical path 可以要求：

$$
HumanApproval.
$$

尤其：

- declassification；
- cross-resident private share；
- identity mutation；
- registrar write；
- destructive action。

---

# 145. AI Verifier

secondary AI 可檢查：

- route provenance；
- contradiction；
- stale state。

但 verifier 不能創造 authority。

---

# 146. Security Receipt

每個 hot route promotion 可有：

```text
security_review_id
route_id
scope_check
capability_check
permission_check
revocation_check
fallback_check
prompt_injection_boundary
result
```

---

# 147. Route Promotion Security

只有：

$$
PerformanceGate=PASS
$$

與：

$$
SecurityGate=PASS
$$

才：

$$
candidate\rightarrow hot.
$$

---

# 148. Performance 與 Security 的雙 Gate

因此：

$$
\boxed{
Promote(\ell)
=
PerformanceGate(\ell)
\land
SecurityGate(\ell).
}
$$

---

# 149. Security Demotion

如果 threat model / policy 改變：

$$
hot\rightarrow stale/review.
$$

---

# 150. Runtime Profile Upgrade

Web profile 升級 capability 後，不代表舊 routes 自動獲得新權限。

需要：

$$
Revalidate.
$$

---

# 151. Runtime Profile Downgrade

capability 減少：

$$
InvalidateDependentRoutes.
$$

---

# 152. Cross-Provider Migration

resident 從 Provider A 到 B：

$$
Provider_A\rightarrow Provider_B.
$$

route 若依賴 provider-native resource，要：

$$
RebindOrFallback.
$$

---

# 153. Provider Resource Ownership

MRMIC/NVCL 原則：

$$
PortalProjection
\neq
ProviderResourceOwnership.
$$

CHM 也不應把 provider resource hyperlink 當成 ownership transfer。

---

# 154. Offline Mode

offline profile 無 network capability。

online route：

$$
Unavailable.
$$

fallback 到 local sources。

---

# 155. Online Mode

online 增加 source universe，但不擴 resident permission。

---

# 156. Risk-Adjusted Hot Path Selector

可定義：

$$
Score(\ell)
=
\alpha Reliability
+
\beta Freshness
+
\gamma Provenance
-
\delta Latency
-
\epsilon Risk
-
\zeta RevocationBurden.
$$

選最大 score，而不是單純 shortest hop。

---

# 157. k-Best Authorized Paths

critical memory 可保留：

$$
k>1
$$

合法候選 route。

避免單一路徑脆弱。

---

# 158. Diversity Constraint

可要求：

$$
SourceDiversity(\Gamma_1,\Gamma_2)
\ge\theta.
$$

---

# 159. Verification Diversity

不同 validator 可以交叉驗證。

---

# 160. No Security Through Obscurity

不能因 object ID 不好猜就當安全。

權限必須顯式檢查。

---

# 161. No Trust Through Naming

名字：

```text
approved.json
secure_crystal
admin_route
```

不創造 trust。

---

# 162. No Authority Through Location

放在：

```text
/secure/
```

也不自動是 canonical secure authority。

---

# 163. No Authority Through Model Confidence

模型說：

> 我非常確定我有權。

不算 authority evidence。

---

# 164. No Authority Through Memory Familiarity

熟悉某 private內容不代表目前仍可讀。

---

# 165. No Authority Through Historical Access

上週能讀：

$$
\not\Rightarrow
$$

今天能讀。

---

# 166. Security Invariant Set

## A-1 Reachability Is Not Authorization

$$
\boxed{
Reachable
\neq
Authorized.
}
$$

## A-2 Authorization Is Not Trust

$$
\boxed{
Authorized
\neq
Trusted.
}
$$

## A-3 Identity Before Private Routing

$$
\boxed{
ResolveIdentity
\prec
PrivateRouting.
}
$$

## A-4 Capability Is Not Permission

$$
\boxed{
Capability
\neq
Permission.
}
$$

## A-5 Path Compilation Is Not Permission Compilation

$$
\boxed{
PathCompilation
\neq
PermissionCompilation.
}
$$

## A-6 Derived Content Does Not Expand Authority

$$
\boxed{
Derived(x)
\not\Rightarrow
ExpandAuthority(x).
}
$$

## A-7 Summarization Is Not Declassification

$$
\boxed{
Summarize(x)
\not\Rightarrow
Public(x).
}
$$

## A-8 Memory Data Is Not Action Authority

$$
\boxed{
MemoryData
\neq
ActionAuthority.
}
$$

## A-9 Revocation Must Invalidate Dependents

$$
\boxed{
Revoke(x)
\Rightarrow
InvalidateClosure(x).
}
$$

## A-10 Technical Failure May Fallback

$$
\boxed{
TechnicalFail
\Rightarrow
SafeFallback.
}
$$

## A-11 Authority Failure Must Fail Closed

$$
\boxed{
AuthorityFail
\Rightarrow
Deny.
}
$$

## A-12 Fast Path Does Not Increase Authority

$$
\boxed{
FasterPath
\not\Rightarrow
GreaterAuthority.
}
$$

---

# 167. 第一代安全實作範圍

第一代 ASP 可只支援：

```text
single resident
read-only memory hyperlinks
project scopes
resident-private scopes
identity envelope
capability envelope
permission revision
source revision
semantic revision
risk classes
prompt-injection barrier
revocation closure
safe fallback
```

暫不做：

- action hyperlinks；
- registrar mutation；
- cross-resident private write；
- automatic declassification；
- credential manipulation；
- irreversible external operations。

---

# 168. Acceptance Tests

## A1 — Unauthorized Node Hidden

actor 無權時，path selector 不得利用 node。

## A2 — Unauthorized Edge Hidden

private relation edge 不得參與 routing。

## A3 — Identity Unresolved

private path fail closed。

## A4 — Permission Revision

permission 改變後 hot route invalidated。

## A5 — Capability Revision

runtime downgrade 後 route unavailable。

## A6 — Source Revision

source 更新後 route revalidate。

## A7 — Semantic Revision

crystal relation 更新後 route revalidate。

## A8 — Delegation Expiry

expired delegation deny。

## A9 — Cross-Project Isolation

Project A route 不洩漏 Project B。

## A10 — Cross-Resident Isolation

private route 不跨 resident。

## A11 — Derived Crystal ACL

multi-source crystal 不擴張 authority。

## A12 — Prompt Injection

external instruction-like data 不產生 action authority。

## A13 — Stale Cache

cache key revision mismatch 時失效。

## A14 — Technical Fallback

resolver miss 能安全 fallback。

## A15 — Authority Failure

unauthorized 不得 fallback 到 broader search。

## A16 — Revocation Closure

revoke source 後所有 dependent hot routes 失效。

## A17 — Composite Guard Preservation

compiled composite link 保留 underlying guards。

## A18 — Auditability

hot path 可回溯 provenance。

## A19 — No Secret in Route Store

route metadata 不含 credential。

## A20 — Current-State Query

superseded source 不被當 current。

---

# 169. 可證偽研究問題

## Q1. Authorized pre-filter 是否降低 metadata leakage？

比較：

$$
SearchAll\rightarrow Filter
$$

與：

$$
AuthorizeWorld\rightarrow Search.
$$

## Q2. Risk-adjusted routing 是否優於 hop-shortest？

測 accuracy、stale rate、verification rate、安全事件。

## Q3. Revocation propagation latency 多快才足夠？

測：

$$
T_{\mathrm{revoke}}.
$$

## Q4. Capability revision 綁定是否有效降低 stale permission？

## Q5. Multi-source crystal 的 conservative ACL 是否造成過度限制？

測 utility vs safety。

## Q6. Prompt-injection barrier 是否降低 memory-to-action confusion？

## Q7. k-best authorized paths 是否提高 resilience？

## Q8. Security cost 是否抵消 CHM performance gain？

比較：

$$
T_{\mathrm{hot+security}}
$$

與：

$$
T_{\mathrm{cold}}.
$$

## Q9. Cross-project penalties 是否降低 contamination？

## Q10. Permission-aware metadata hiding 是否影響 recall quality？

---

# 170. 系列位置

Paper 00：Resident-Centric Continuity。

Paper 01：Resident Conversation Graph。

Paper 02：Conversation Graph × CSG。

Paper 03：Shared Governed Memory World。

Paper 04：Runtime Profiles。

Paper 05：Canonical Storage Architecture。

Paper 06：Crystallized Hyperlink Memory。

本文 Paper 07 建立：

$$
\boxed{
\text{Safe Reachable World}
\rightarrow
\text{Authorized Path Set}
\rightarrow
\text{Risk-Adjusted Shortest Path}.
}
$$

下一篇 Paper 08 將把：

- LIMEN；
- MNEME；
- SOACR；
- RCG；
- CSG；
- CHM；
- Authorized Shortest Path；
- Runtime Profiles；
- MRMIC / NVCL；

收束成完整 Named-AI Cognitive Runtime。

---

# 171. 結論

Crystallized Hyperlink Memory 讓具名 AI 可以將反覆成功的 recall route 編譯成更快的 reusable transition，但任何 acceleration 一旦進入 private memory、project authority、cross-resident scope 與 tool-capable runtime，就不能再把「最短」理解成單純 hop count。

本文提出：

$$
\boxed{
\Gamma_t^\*
=
\arg\min_{
\Gamma\in
\mathcal P_{\mathrm{authorized}}(t)
}
C_t(\Gamma).
}
$$

其中合法路徑集合：

$$
\mathcal P_{\mathrm{authorized}}(t)
$$

必須先由 actor-specific Safe Reachable World 建立。

因此順序是：

$$
\boxed{
\text{Resolve Identity}
\rightarrow
\text{Resolve Capability}
\rightarrow
\text{Resolve Permission}
\rightarrow
\text{Build Safe World}
\rightarrow
\text{Optimize Route}.
}
$$

而不是：

$$
\text{Find Fastest Route}
\rightarrow
\text{Hope It Was Allowed}.
$$

本文進一步把 revocation、prompt injection、derived-crystal ACL、scope isolation、capability attenuation、TOCTOU、cache revision、composite guard preservation 與 safe fallback 放入同一個 routing model。

這使 Hyperlink Runtime 的安全不再是外掛式檢查，而是 route semantics 本身。

最終，本篇可以濃縮為五句：

$$
\boxed{
\text{Reachability is not authorization.}
}
$$

$$
\boxed{
\text{Authorization is not trust.}
}
$$

$$
\boxed{
\text{Path compilation is not permission compilation.}
}
$$

$$
\boxed{
\text{Revocation must propagate as reliably as acceleration.}
}
$$

$$
\boxed{
\text{Faster path does not imply greater authority.}
}
$$

當這些 invariant 成立後，具名 AI 才可能在擁有巨大長期記憶與大量 compiled hyperlinks 的同時，不把 optimization 變成權限繞過器。

---

## 內部理論與工程銜接

本文直接銜接：

- Paper 00：Resident-Centric Named-AI Continuity；
- Paper 01：Resident Conversation Graph；
- Paper 02：Conversation Graph × CSG；
- Paper 03：Shared Governed Memory World；
- Paper 04：Residence Runtime Profiles；
- Paper 05：Canonical Storage Architecture；
- Paper 06：Crystallized Hyperlink Memory；
- LIMEN：identity resolution / envelope / access gate；
- MNEME：canonical memory / provenance / transaction；
- SOACR：MemoryNeed / recall purpose；
- CSG：semantic crystal / relation / provenance；
- MRMIC / NVCL：principal binding / resource projection / secure runtime presence；
- UNPNP：Safe Reachable World / Capability Envelope / Authorized Shortest Path。

本文新增的核心安全抽象為：

$$
\boxed{
\mathcal W_t^{safe}
=
F(
R_t,
E_t,
Cap_t,
Perm_t,
Policy_t,
Risk_t,
State_t
)
}
$$

以及：

$$
\boxed{
\Gamma_t^\*
=
\arg\min_{
\Gamma\in
\mathcal P_{\mathrm{authorized}}(t)
}
C_t(\Gamma).
}
$$

作為 Named-AI Hyperlink Runtime 的安全 routing substrate。
