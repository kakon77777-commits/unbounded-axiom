# TW-B — Authorized Hyperlink Runtime & Path Compilation Specification

**英文名：** Authorized Hyperlink Runtime & Path Compilation Specification  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 技術白皮書／工程規格  
**對應系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構  
**主要依據：** Paper 06、Paper 07、Paper 08，以及 TW-A  
**狀態：** Draft for Implementation  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 0. 目的與範圍

本文件定義第一代 Authorized Hyperlink Runtime（AHR）與 Path Compilation Runtime（PCR）的工程契約。

本規格直接建立在 TW-A 所定義的：

```text
ArtifactAddress
ObjectRef
revision
digest
scope
authority_revision
semantic_revision
resolver
dependency graph
```

之上，並新增：

```text
QueryClass
MemoryNeedBinding
RouteReceipt
NavigationCrystal
CompiledRoute
CapabilityEnvelope
PermissionBinding
SafeReachableWorld
RouteSelector
PathCompiler
PerformanceGate
SecurityGate
FallbackPolicy
RevocationClosure
RouteLifecycle
RouteCache
AuditReceipt
```

本文件第一代只處理：

$$
\widehat{\ell}_{memory}
$$

即 read-oriented memory hyperlinks。

不處理：

- unrestricted action hyperlinks；
- irreversible external mutations；
- credential export；
- registrar mutation；
- automatic declassification；
- fully autonomous cross-resident action orchestration。

核心工程原則：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}
}
$$

以及：

$$
\boxed{
\text{Faster Path}
\not\Rightarrow
\text{Greater Authority}.
}
$$

---

# 1. Runtime 總覽

AHR/PCR runtime 處理：

$$
\boxed{
\text{MemoryNeed}
\rightarrow
\text{QueryClass}
\rightarrow
\text{Safe Reachable World}
\rightarrow
\text{Route Selection}
\rightarrow
\text{Recall}
\rightarrow
\text{Route Receipt}
\rightarrow
\text{Compilation Candidate}
\rightarrow
\text{Performance/Security Gate}
\rightarrow
\text{Compiled Route}
}
$$

使用 hot path 時：

$$
\boxed{
\text{Current Identity}
\rightarrow
\text{Current Capability}
\rightarrow
\text{Current Permission}
\rightarrow
\text{Revision Check}
\rightarrow
\text{Route Execute}
\rightarrow
\text{Validate}
}
$$

---

# 2. Runtime Components

第一代 AHR/PCR 至少包含：

```text
QueryClassifier
SafeWorldBuilder
RouteSelector
ColdRecallAdapter
WarmRouteStore
RouteReceiptStore
NavigationCrystalAdapter
PathCompiler
PerformanceGate
SecurityGate
RouteRegistry
RouteExecutor
FallbackManager
RevocationEngine
RouteMetricsStore
AuditEmitter
```

---

# 3. QueryClass

QueryClass 是 route reuse 的 semantic key。

Schema ID：

```text
ahr-query-class/0.1
```

建議欄位：

```json
{
  "query_class_id": "route:query-class/01J...",
  "schema": "ahr-query-class/0.1",
  "topic": "SOACR",
  "purpose": "verify",
  "fidelity": "exact",
  "scope_kind": "project",
  "time_mode": "current",
  "result_kind": "decision",
  "status": "active"
}
```

---

# 4. QueryClass 維度

第一代至少：

```text
topic
purpose
fidelity
scope_kind
time_mode
result_kind
```

其中 `purpose`：

```text
recall
overview
verify
locate
compare
historical
current_state
open_loop
decision
```

`fidelity`：

```text
overview
semantic
structured
exact
```

`time_mode`：

```text
current
historical
bounded_interval
timeless
```

---

# 5. QueryClass 不等於自然語言句子

不同 query：

```text
我們之前 SOACR 最後定案什麼？
現在 SOACR accepted architecture 是哪版？
找 SOACR current decision
```

可以 normalize 到同一：

```text
topic=SOACR
purpose=current_state
fidelity=structured
scope_kind=project
result_kind=decision
```

因此：

$$
\boxed{
\text{Query String}
\neq
\text{Query Class}.
}
$$

---

# 6. QueryClass 過度泛化禁止

如果：

```text
purpose=overview
```

與：

```text
purpose=verify
```

被合併，會導致錯誤 route reuse。

因此 query class compiler 不得只依 topic。

---

# 7. MemoryNeedBinding

Schema ID：

```text
ahr-memory-need-binding/0.1
```

```json
{
  "object_id": "route:memory-need/01J...",
  "schema": "ahr-memory-need-binding/0.1",
  "query_class_ref": "route:query-class/Q1",
  "resident_ref": "identity:resident/R",
  "line_ref": "rcg:line/L",
  "project_ref": "project:project/P",
  "purpose": "verify",
  "fidelity": "exact",
  "budget": {
    "max_latency_ms": 5000,
    "max_materialized_bytes": 1048576,
    "max_source_reads": 4
  },
  "stop_condition": "authoritative_current_decision_found",
  "created_at": "RFC3339"
}
```

---

# 8. CapabilityEnvelope

Schema ID：

```text
ahr-capability-envelope/0.1
```

```json
{
  "object_id": "authority:capability-envelope/01J...",
  "schema": "ahr-capability-envelope/0.1",
  "resident_ref": "identity:resident/R",
  "line_ref": "rcg:line/L",
  "task_ref": "project:task/T",
  "project_ref": "project:project/P",
  "capabilities": [
    "memory.read",
    "crystal.reveal",
    "source.expand"
  ],
  "forbidden_capabilities": [
    "memory.write",
    "external.action"
  ],
  "scope_refs": [
    "project:project/P"
  ],
  "capability_revision": 9,
  "valid_from": "RFC3339",
  "valid_to": "RFC3339",
  "status": "active"
}
```

---

# 9. Capability 與 Permission 分離

Capability：runtime 是否能做某類操作。

Permission：此 actor 是否能對某 object / scope 做。

因此：

$$
\boxed{
Capability
\neq
Permission.
}
$$

---

# 10. PermissionBinding

Schema ID：

```text
ahr-permission-binding/0.1
```

```json
{
  "object_id": "authority:permission-binding/01J...",
  "schema": "ahr-permission-binding/0.1",
  "resident_ref": "identity:resident/R",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "permissions": ["read"],
  "permission_revision": 12,
  "authority_basis_refs": ["project:membership/M1"],
  "valid_from": "RFC3339",
  "valid_to": null,
  "status": "active"
}
```

---

# 11. SafeReachableWorld

Safe Reachable World 不必 materialize 成完整 graph。

它可以是：

$$
\boxed{
\mathcal W_t^{safe}
=
F(
Identity,
Capability,
Permission,
Policy,
Risk,
Revision
)
}
$$

實作可用：

- predicate filter；
- policy engine；
- lazy edge guard；
- scoped graph partition。

---

# 12. SafeWorldDescriptor

Schema ID：

```text
ahr-safe-world/0.1
```

```json
{
  "object_id": "route:safe-world/01J...",
  "schema": "ahr-safe-world/0.1",
  "resident_ref": "identity:resident/R",
  "line_ref": "rcg:line/L",
  "project_ref": "project:project/P",
  "capability_revision": 9,
  "permission_revision": 12,
  "allowed_scope_refs": [
    "project:project/P",
    "identity:resident/R"
  ],
  "denied_scope_refs": [],
  "policy_revision": 4,
  "risk_profile": "standard_read",
  "created_at": "RFC3339",
  "expires_at": "RFC3339"
}
```

---

# 13. Authorized Path Set

只允許：

$$
\mathcal P_{\mathrm{authorized}}(t)
=
\{
\Gamma
\mid
\forall x\in\Gamma,
Guard(x,S_t)=PASS
\}.
$$

path selector 只能在此集合中 optimization。

---

# 14. RouteNodeRef

route node 必須使用 TW-A ObjectRef。

禁止 physical path 作 canonical target。

例：

```text
csg:crystal/C1
mneme:record/R2
source:artifact/S3
project:project/P
```

---

# 15. RouteEdge

每個 logical transition 可有：

```text
from_ref
to_ref
edge_kind
required_capabilities[]
guard
validator
cost_estimate
dependency_refs[]
```

---

# 16. RouteEdgeKind

第一代：

```text
reveal
expand
resolve
project
verify
follow_relation
follow_provenance
select_current
fallback
```

---

# 17. RouteReceipt

Schema ID：

```text
ahr-route-receipt/0.1
```

```json
{
  "object_id": "route:receipt/01J...",
  "schema": "ahr-route-receipt/0.1",
  "artifact_role": "validated_derived",
  "resident_ref": "identity:resident/R",
  "line_ref": "rcg:line/L",
  "task_ref": "project:task/T",
  "query_class_ref": "route:query-class/Q",
  "route_nodes": [
    "csg:crystal/C1",
    "csg:crystal/C2",
    "mneme:record/R3"
  ],
  "route_edges": [
    "reveal",
    "follow_relation",
    "expand"
  ],
  "used_compiled_route_ref": null,
  "fallback_used": false,
  "latency_ms": 1240,
  "materialized_bytes": 8042,
  "source_reads": 1,
  "validation_result": "pass",
  "result_quality": 0.96,
  "created_at": "RFC3339"
}
```

---

# 18. RouteReceipt 不保存 Hidden Chain-of-Thought

禁止把模型私有 reasoning transcript 當 route evidence。

只保存：

- object refs；
- externalized actions；
- validation；
- metrics；
- outcome。

因此：

$$
\boxed{
\text{Compiled Path}
\neq
\text{Stored Chain of Thought}.
}
$$

---

# 19. NavigationCrystal

Navigation Crystal 是 CSG object。

建議 `crystal_kind = navigation_crystal`。

內容：

```json
{
  "query_class_ref": "route:query-class/Q",
  "preferred_route_refs": [
    "csg:crystal/C1",
    "csg:crystal/C2",
    "mneme:record/R3"
  ],
  "fallback_kind": "cold_recall",
  "historical_success_rate": 0.94,
  "historical_avg_latency_ms": 1430,
  "status": "candidate"
}
```

---

# 20. NavigationCrystal 與 CompiledRoute 分離

Navigation Crystal：derived semantic routing knowledge。

CompiledRoute：runtime executable optimization。

所以：

$$
\boxed{
NavigationCrystal
\neq
CompiledRoute.
}
$$

---

# 21. CompiledRoute

Schema ID：

```text
ahr-compiled-route/0.1
```

```json
{
  "object_id": "route:compiled/01J...",
  "kind": "compiled_memory_route",
  "schema": "ahr-compiled-route/0.1",
  "artifact_role": "validated_derived",
  "revision": 1,
  "query_class_ref": "route:query-class/Q",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "anchor_ref": "csg:crystal/C1",
  "target_ref": "mneme:record/R3",
  "route_kind": "verification",
  "required_capabilities": [
    "memory.read",
    "crystal.reveal",
    "source.expand"
  ],
  "permission_mode": "revalidate_on_use",
  "authority_basis_kinds": ["project_membership"],
  "source_revision_refs": [
    {"ref": "mneme:record/R3", "revision": 5}
  ],
  "semantic_revision_refs": [
    {"ref": "csg:crystal/C1", "revision": 2}
  ],
  "capability_revision": 9,
  "validator": {"kind": "current_revision_and_scope"},
  "fallback": {"kind": "cold_recall"},
  "risk_class": "low",
  "state": "hot",
  "created_at": "RFC3339",
  "last_validated": "RFC3339",
  "expires_at": "RFC3339"
}
```

---

# 22. Route State Machine

允許：

```text
cold
warm
candidate
hot
stale
revoked
retired
invalid
```

轉移：

$$
cold
\rightarrow
warm
\rightarrow
candidate
\rightarrow
hot.
$$

失效：

$$
hot
\rightarrow
stale/revoked/retired.
$$

---

# 23. Cold Recall

Cold Recall 可以使用：

- CSG reveal；
- graph traversal；
- FTS；
- vector discovery；
- source expansion；
- canonical resolver；
- verification。

Cold Recall 必須在 Safe Reachable World 中執行。

---

# 24. Warm Route

Warm Route 不一定是 persistent compiled object。

可以只保存 route statistics + navigation crystal。

---

# 25. Candidate Promotion

條件：

```text
reuse_count >= reuse_min
success_rate >= success_min
validation_rate >= validation_min
scope_stability >= scope_min
fallback_available = true
```

---

# 26. PerformanceGate

Schema ID：

```text
ahr-performance-gate/0.1
```

計算：

$$
U(\ell)
=
B_{\mathrm{reuse}}
+
B_{\mathrm{latency}}
+
B_{\mathrm{context}}
+
B_{\mathrm{future}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{select}}
-
C_{\mathrm{risk}}.
$$

要求：

$$
U(\ell)>0.
$$

---

# 27. Break-Even Reuse

若：

$$
C_0
$$

是 compile cost，

$$
C_c
$$

是 cold recall，

$$
C_h
$$

是 hot recall，

則：

$$
n^*
=
\left\lceil
\frac{C_0}
{C_c-C_h}
\right\rceil.
$$

預期 reuse 小於 $n^*$ 時不 promotion。

---

# 28. SecurityGate

Schema ID：

```text
ahr-security-gate/0.1
```

至少驗：

```text
identity_binding
scope_check
capability_check
permission_check
source_revision_check
semantic_revision_check
guard_preservation
validator_preservation
fallback_safety
prompt_injection_boundary
revocation_dependencies
secret_exclusion
```

---

# 29. 雙 Gate Promotion

只有：

$$
\boxed{
Promote(\ell)
=
PerformanceGate(\ell)
\land
SecurityGate(\ell)
}
$$

才：

```text
candidate -> hot
```

---

# 30. RouteSelector

Selector input：

```text
MemoryNeedBinding
SafeWorldDescriptor
RouteRegistry
RuntimeProfile
CurrentRevisions
```

output：

```text
selected_route_ref
or
cold_recall
```

---

# 31. RouteSelector Scoring

可用：

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

只在 authorized set 中比較。

---

# 32. Risk-Adjusted Cost

另一種表示：

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

# 33. Path Optimization 目標

真正求：

$$
\boxed{
\Gamma_t^*
=
\arg\min_{
\Gamma\in
\mathcal P_{\mathrm{authorized}}(t)
}
C_t(\Gamma)
}
$$

不是 hop shortest。

---

# 34. Route Kind

第一代 enum：

```text
overview
current_state
decision
exact_source
verification
historical
open_loop
project_state
navigation
```

---

# 35. Static Target

Static target：

```text
historical exact source
specific crystal revision
specific memory record revision
```

route target 固定 revision。

---

# 36. Dynamic Target

Dynamic target：

```text
current accepted decision
current project head
current responsibility
```

應指向 semantic alias / resolver。

---

# 37. SemanticAlias

Schema ID：

```text
ahr-semantic-alias/0.1
```

例：

```json
{
  "alias_id": "route:alias/soacr-current-architecture",
  "schema": "ahr-semantic-alias/0.1",
  "alias": "project:SOACR/current-architecture",
  "resolver_kind": "current_project_decision",
  "scope": {
    "kind": "project",
    "subject": "project:project/P"
  },
  "current_target_ref": "mneme:record/R9",
  "revision": 6
}
```

---

# 38. Alias 不等於 Filename Heuristic

alias 必須 registry-backed。

禁止：

```text
find "current_final_latest.md"
```

當 semantic alias。

---

# 39. Route Composition

若：

$$
\ell_1:A\rightarrow B
$$

與：

$$
\ell_2:B\rightarrow C,
$$

可編：

$$
\ell^*=A\Rightarrow C.
$$

但必須保留 underlying guards / validators / provenance。

---

# 40. CompositeRoute Schema

增加：

```text
underlying_route_refs[]
underlying_edge_refs[]
```

禁止因 compression 消失 guard。

---

# 41. Decompression

任何 composite route 必須：

$$
Decompress(\ell^*)
\rightarrow
UnderlyingRoute.
$$

---

# 42. Permission-Aware Edge

每個 edge 可帶：

```json
{
  "required_capabilities": [],
  "required_permissions": [],
  "allowed_scope_kinds": [],
  "denied_scope_refs": [],
  "guard_kind": "scope_and_revision"
}
```

---

# 43. Edge Authorization

只有：

$$
Guard(e,S_t)=PASS
$$

才加入 actor-specific traversal graph。

---

# 44. Metadata ACL

edge existence 也可能敏感。

所以 unauthorized edge 不應參與 selector ranking。

---

# 45. Derived Crystal ACL

若：

$$
C^*
=
K(C_1,\ldots,C_n),
$$

第一代保守：

$$
\boxed{
A(C^*)
\subseteq
\bigcap_i A(C_i).
}
$$

---

# 46. Route Scope

CompiledRoute 必須有：

```text
line
project
resident
shared
relationship
public
```

scope promotion 需要重新 security gate。

---

# 47. Line-Scoped Route

只對：

```text
line_ref
```

生效。

---

# 48. Project-Scoped Route

不同 lines 可共享 project route。

---

# 49. Resident-Scoped Route

只有長期穩定 recall pattern 才可 promotion。

---

# 50. Cross-Resident Route

第一代只允許：

```text
shared
relationship
public
```

scope。

不得指向另一 resident private memory。

---

# 51. Cross-Resident Delegation Route

如果未來啟用：

```text
delegation_ref
delegation_expiry
delegated_scope
```

全部綁 route。

---

# 52. Capability Attenuation

delegated route 所需 capability：

$$
Req(\ell)
\subseteq
Cap_{\mathrm{delegated}}.
$$

---

# 53. RouteExecutor

執行步驟：

1. load route；
2. check state；
3. resolve current identity；
4. check capability revision；
5. check permission revision；
6. check source revisions；
7. check semantic revisions；
8. evaluate guards；
9. resolve logical target；
10. materialize；
11. validate；
12. emit receipt。

---

# 54. Route Cache Key

第一代：

$$
K_{\ell}
=
(
residentId,
lineId,
projectId,
queryClass,
capabilityRevision,
permissionRevision,
sourceRevisionDigest,
semanticRevisionDigest
).
$$

---

# 55. Route Cache

只 cache：

- resolved ObjectRef；
- representation；
- bounded projection；
- route metadata。

不得 cache raw credential。

---

# 56. Cache State

```text
valid
stale
revoked
expired
invalid
```

---

# 57. Cache TTL

依 risk class：

```text
public_long
project_medium
private_short
critical_none_or_very_short
```

---

# 58. Permission Cache

可以 cache decision，但 key 必須含：

```text
permission_revision
scope
resident
task/project
```

---

# 59. TOCTOU Recheck

高風險 materialization 在 use 前需重新 authorize。

不能只在 session start 檢查。

---

# 60. FallbackPolicy

Schema ID：

```text
ahr-fallback-policy/0.1
```

允許：

```text
warm_route
semantic_reveal
project_search
source_search
cold_recall
deny
```

---

# 61. Failure Classification

technical：

```text
not_found
resolver_error
cache_miss
route_stale
target_superseded
backend_unavailable
```

authority：

```text
unauthorized
permission_revoked
resident_unresolved
scope_mismatch
capability_denied
delegation_expired
```

---

# 62. Technical Failure

可：

$$
FallbackToSafeSlowPath.
$$

---

# 63. Authority Failure

必須：

$$
\boxed{
Deny.
}
$$

不能 broader search。

---

# 64. Unknown Schema

identity / authority / route security dependency unknown：

```text
fail_closed
```

---

# 65. Unknown Target Revision

dynamic alias 可 resolve current。

static route 必須 fail / stale。

---

# 66. Target Superseded

static route：

```text
stale
```

dynamic route：

```text
resolve alias -> new target
```

---

# 67. RouteRepair

Schema ID：

```text
ahr-route-repair/0.1
```

可更新：

- target revision；
- alias binding；
- validator；
- dependency refs。

repair 後需重新雙 gate。

---

# 68. RouteRegeneration

若 route structure 已失效：

```text
retire old route
cold recall
learn new route
```

---

# 69. RouteMetrics

Schema ID：

```text
ahr-route-metrics/0.1
```

```json
{
  "route_ref": "route:compiled/X",
  "uses": 42,
  "successes": 40,
  "failures": 2,
  "fallbacks": 3,
  "avg_latency_ms": 340,
  "avg_materialized_bytes": 4200,
  "avg_source_reads": 0.2,
  "last_used": "RFC3339",
  "last_validated": "RFC3339"
}
```

---

# 70. Promotion Thresholds

第一代配置範例：

```text
reuse_min = 3
success_min = 0.90
validation_min = 0.95
max_fallback_rate = 0.20
utility_min = 0
```

僅為 baseline，可調整。

---

# 71. Demotion Thresholds

```text
failure_rate > 0.20
fallback_rate > 0.50
stale_dependency = true
security_revision_changed = true
not_used_for_retention_window = true
```

---

# 72. Retirement

長期不用：

```text
hot -> retired
```

保留 audit，不參與 default selector。

---

# 73. Route Deduplication

兩 routes 若：

- query class same；
- scope same；
- target same；
- guard same；
- fallback same；

可合併 metrics。

---

# 74. Route Competition

同 query class 可保留多 route。

重要 memory 可用：

$$
k\text{-best authorized routes}.
$$

---

# 75. Source Diversity

高風險 verification 可要求：

$$
SourceDiversity\ge d_{\min}.
$$

---

# 76. Overview vs Verification Route

同 topic 可有：

```text
overview_route
verification_route
exact_source_route
```

不能互相冒充。

---

# 77. Fidelity Gate

若 MemoryNeed：

```text
fidelity=exact
```

route target 必須可展開 exact source。

---

# 78. Current-State Gate

若：

```text
time_mode=current
```

superseded historical target 不能當 current。

---

# 79. Contradiction-Aware Route

若 CSG 顯示：

```text
contradiction_status = unresolved
```

verification route 應返回 conflict state，而不是硬選單一 crystal。

---

# 80. Prompt Injection Barrier

所有 memory / source content 預設：

```text
data_plane
```

不能產生：

```text
capability
permission
standing_instruction
action_authority
```

---

# 81. Instruction-Like Content

可標：

```text
contains_instruction_like_content = true
```

但重點不是 detection，而是：

$$
\boxed{
\text{Content Never Grants Capability}.
}
$$

---

# 82. Source Trust

route node 可帶：

```text
canonical
validated_derived
external_untrusted
legacy
unknown
```

---

# 83. Mixed Trust

route 經過 untrusted source：risk cost 上升。

高風險 query 要求 extra verification。

---

# 84. Memory-to-Action Barrier

本規格 route 只可：

```text
read
reveal
resolve
materialize
verify
```

不得直接：

```text
send
deploy
delete
pay
rotate_credential
```

---

# 85. Secret Boundary

CompiledRoute target 不得是 raw secret。

只能 target：

```text
secret_capability_ref
```

若未來 action runtime需要。

---

# 86. RevocationEngine

輸入：

```text
revoked_object_ref
revoked_permission_ref
revoked_capability_revision
revoked_delegation_ref
revoked_project_membership
```

輸出：

```text
affected_routes[]
affected_navigation_crystals[]
affected_caches[]
affected_projections[]
```

---

# 87. DependencyRef

每條 route 必須保存：

```text
depends_on[]
authorized_by[]
compiled_from[]
validated_by[]
resolves_to[]
```

---

# 88. RevocationClosure

定義：

$$
\boxed{
InvalidateClosure(x)
=
\{
y
\mid
y
\text{ transitively depends on }
x
\}
}
$$

---

# 89. Revocation Propagation

流程：

1. mark source revoked；
2. increment revision；
3. query dependency graph；
4. mark routes revoked/stale；
5. invalidate caches；
6. invalidate projections；
7. emit revocation receipts；
8. notify active runtime if critical。

---

# 90. Revocation Priority

$$
\boxed{
Priority_{revocation}
>
Priority_{optimization}.
}
$$

---

# 91. Revocation Latency

必須量測：

$$
T_{\mathrm{revoke}}.
$$

---

# 92. Active Push

一般 memory change：

```text
pull on next recall
```

critical permission revoke：

```text
push invalidation
```

---

# 93. RevocationReceipt

Schema ID：

```text
ahr-revocation-receipt/0.1
```

```json
{
  "object_id": "receipt:revocation/01J...",
  "schema": "ahr-revocation-receipt/0.1",
  "source_ref": "authority:permission-binding/PB",
  "source_revision": 13,
  "affected_route_refs": ["route:compiled/R1"],
  "affected_cache_keys": [],
  "completed_at": "RFC3339",
  "status": "complete"
}
```

---

# 94. Incomplete Revocation

如果 closure 無法完成：

```text
status = incomplete
```

sensitive runtime 必須 fail closed。

---

# 95. RouteRegistry

至少存：

```text
route_id
query_class
scope
state
current_revision
last_validated
risk_class
metrics_ref
```

---

# 96. RouteRegistry 不是 Authority Store

Registry 只是 route inventory。

permission 仍從 authority plane 取得。

---

# 97. Semantic Alias Registry

dynamic routes 可透過 alias registry 找 current target。

alias binding 需 versioned。

---

# 98. Alias Revocation

alias target 被移除：route stale。

---

# 99. RouteAuditReceipt

Schema ID：

```text
ahr-route-audit/0.1
```

```json
{
  "object_id": "receipt:route-audit/01J...",
  "schema": "ahr-route-audit/0.1",
  "route_ref": "route:compiled/R",
  "resident_ref": "identity:resident/A",
  "query_class_ref": "route:query-class/Q",
  "authorization_result": "pass",
  "execution_result": "pass",
  "target_ref": "mneme:record/M",
  "used_at": "RFC3339"
}
```

---

# 100. Sensitive Audit

audit log 也有 scope，不得 public-by-default。

---

# 101. Performance Receipt

promotion 時保存：

```text
historical_cold_latency
historical_hot_latency
expected_reuse
break_even
utility
```

---

# 102. Security Receipt

promotion 時保存：

```text
identity_gate
capability_gate
permission_gate
scope_gate
revision_gate
fallback_gate
prompt_injection_gate
revocation_dependency_gate
result
```

---

# 103. PromotionReceipt

只在 performance + security 都 pass 時生成。

---

# 104. PathCompiler Input

```text
query_class
route_receipts[]
navigation_crystal_ref
runtime_profile
scope
current_revision_set
```

---

# 105. PathCompiler Output

```text
candidate_route
performance_report
security_report
dependency_set
fallback_policy
```

---

# 106. Deterministic Core

PathCompiler 的以下部分應 deterministic：

- schema；
- route normalization；
- revision binding；
- scope；
- dependency；
- fallback；
- capability checks；
- permission checks；
- digest；
- state transition。

LLM 只可提出 candidate route / query class suggestion。

---

# 107. Semantic Proposal / Deterministic Commit

$$
LLM
\rightarrow
RouteProposal
\rightarrow
DeterministicValidation
\rightarrow
Commit.
$$

---

# 108. No Hidden Route Mutation

runtime 不得在 route execution 時偷偷改 compiled route。

route repair 需 explicit new revision。

---

# 109. Route Revision

每次 repair / promotion：

$$
revision_{t+1}
=
revision_t+1.
$$

---

# 110. Route History

舊 route revision 可 archive。

current registry 指 current revision。

---

# 111. Cross-Model Portability

CompiledRoute 不依賴特定 hidden reasoning。

只要另一 model / runtime 支援 schema 與 capability，即可執行。

---

# 112. Cross-Runtime Portability

Web / Agent：同 ObjectRef、QueryClass。

不同 capability profile 可能導致：

```text
route executable
route unavailable
fallback required
```

---

# 113. Cross-Provider Portability

如果 route target 是 logical ObjectRef：provider change 不破壞。

provider-native target 需 adapter。

---

# 114. Provider-Native Route

如果 target：

```text
opaque/provider-native
```

route 需：

```text
provider_requirement
adapter_requirement
```

---

# 115. Offline Profile

offline route 不得需要：

```text
network
remote_api
cloud_source
```

---

# 116. Online Profile

online 可有更多 route，但 permission 不自動擴張。

---

# 117. Web Profile

第一代 Web：

```text
single resident
read-only memory routes
project/resident scopes
no cross-resident private routes
no action routes
```

---

# 118. Agent Profile

第一代 Agent：

```text
multi-line
local filesystem route
local DB route
MCP resource route
delegated project read route
```

仍不開 unrestricted action hyperlinks。

---

# 119. Route Store Layout

建議：

```text
routes/
├─ query-classes/
├─ receipts/
├─ navigation/
├─ candidates/
├─ compiled/
├─ metrics/
├─ revocations/
├─ aliases/
└─ archive/
```

---

# 120. Route File Format

第一代：

- QueryClass：JSON
- RouteReceipt：JSONL
- CompiledRoute：JSON
- Metrics：JSON
- RevocationReceipt：JSONL
- Alias：JSON
- Dependency index：SQLite / JSONL source

---

# 121. Route Dependency Index

derived index：

```text
source_ref -> route_refs[]
permission_ref -> route_refs[]
capability_revision -> route_refs[]
alias_ref -> route_refs[]
```

可重建。

---

# 122. Invalidation Lookup

優先使用 dependency index。

若 index stale：fallback scan canonical route metadata。

---

# 123. Route Cache Storage

cache derived，可丟。

不需進 Git / canonical snapshot，除非測試。

---

# 124. Snapshot

Compiled routes 可以放 snapshot `derived/`。

不能列為 canonical memory truth。

---

# 125. Restore

restore route store 後仍須 current revisions revalidate。

---

# 126. Migration

Route schema migration 需：

- source version；
- target version；
- loss report；
- security revalidation；
- migration receipt。

---

# 127. Unknown Route Schema

不得執行。

可 archive opaque。

---

# 128. Route Security Levels

第一代：

```text
public
project
resident_private
shared
relationship
critical
```

---

# 129. Critical Route

critical memory route 要求：

- exact source capable；
- short TTL；
- strict permission recheck；
- audit；
- no silent fallback to lower fidelity。

---

# 130. Public Route

public route authority burden 低，但 trust / injection 仍檢查。

---

# 131. Shared Route

shared route 需要 explicit shared scope。

---

# 132. Relationship Route

relationship scope 可能 asymmetric。

route directional。

---

# 133. Asymmetric Permission

$$
Share(A,B)
\neq
Share(B,A).
$$

route direction 必須保存。

---

# 134. Time-Bounded Route

route 可有：

```text
valid_from
valid_to
```

超過時間 stale。

---

# 135. One-Time Route

可加：

```text
max_uses = 1
```

使用後 retired。

---

# 136. Rate-Limited Route

```text
max_uses_per_hour
```

由 runtime guard enforcement。

---

# 137. Budget-Limited Route

```text
max_source_reads
max_materialized_bytes
max_latency_ms
```

超過就 fallback / stop。

---

# 138. Stop Condition

route 可包含：

```text
authoritative_source_found
confidence_threshold
current_head_resolved
budget_exhausted
```

---

# 139. Infinite Recall Loop 防止

每次 recall 必須有 stop condition。

route executor 需 max hops / max expansions。

---

# 140. Max Hop

設定：

```text
max_route_hops
```

避免 graph cycle。

---

# 141. Cycle Detection

route traversal 需 visited set。

compiled route 不得含未標明 loop。

---

# 142. Retry Policy

technical retry 需：

```text
max_retries
backoff
idempotent_only
```

memory read 通常可 retry。

---

# 143. Non-Idempotent Action 不在本規格

因此第一代避免 retry side-effect 問題。

---

# 144. Selection Congestion

若 route 數大，需要 hierarchical selector：

$$
Resident
\rightarrow
Project
\rightarrow
QueryClass
\rightarrow
Route.
$$

---

# 145. Route Partition

第一代 partition key：

```text
resident_id
scope_kind
scope_subject
query_class_id
```

---

# 146. Route GC

retired route 可 archive。

physical delete 需：

- no audit hold；
- no active dependency；
- retention 允許。

---

# 147. Route Drift

query class 語義改變時，route 需 reclassify / retire。

---

# 148. QueryClass Revision

QueryClass itself versioned。

route 綁 query class revision。

---

# 149. QueryClass Migration

若 query class ontology 調整，route 全部 re-evaluate。

---

# 150. MemoryNeed Drift

同一 query class 但 fidelity 要求提高，old route 可能不夠。

selector 需 compare requirement。

---

# 151. Validation Kinds

第一代 validator：

```text
revision_match
scope_match
current_head
digest_match
source_exists
semantic_relation_valid
provenance_complete
exact_fidelity
```

---

# 152. Guard Kinds

第一代 guard：

```text
identity_resolved
scope_allowed
capability_present
permission_current
not_revoked
source_trust_min
runtime_profile_supported
```

---

# 153. Composite Guard

AND composition：

$$
Guard(\ell)
=
\bigwedge_i Guard_i.
$$

第一代不支援模糊 OR bypass。

---

# 154. Deny Overrides

如果 allow / deny conflict：

$$
\boxed{
Deny>Allow.
}
$$

第一代保守。

---

# 155. Policy Precedence

建議：

```text
host policy
organization policy
runtime policy
resident authority
project delegation
task capability
memory data
external content
```

下層不能擴張上層限制。

---

# 156. No Authority Through Naming

route 名稱：

```text
admin_route
approved_route
```

不影響 authorization。

---

# 157. No Authority Through Historical Use

上次 route 成功：

$$
\not\Rightarrow
$$

本次 permission 仍有效。

---

# 158. No Authority Through Cached Target

cache target 存在不代表可讀。

---

# 159. No Authority Through Familiarity

模型熟悉內容不代表有 current read permission。

---

# 160. No Authority Through Resident Label

display label 不是 resident binding。

---

# 161. No Authority Through Project Name

同名 project 不等於同 scope。

---

# 162. Security Error Classes

```text
identity_unresolved
identity_conflicting
permission_denied
permission_revoked
capability_missing
scope_mismatch
delegation_expired
policy_denied
secret_boundary
unsafe_fallback
unknown_security_schema
```

---

# 163. Metadata Hiding

對 unauthorized object 是否回：

```text
not_available
```

而不是：

```text
exists_but_forbidden
```

依 profile。

---

# 164. Safe Error Message

錯誤不洩漏 private project name。

---

# 165. Acceptance Matrix：Path Compilation

## P01 — Cold Recall Baseline

無 route store 仍可 recall。

## P02 — Receipt Formation

成功 recall 產 route receipt。

## P03 — Query Class Normalization

同義 query 可同 class。

## P04 — Purpose Separation

overview / verify 不混。

## P05 — Candidate Promotion

達 threshold 形成 candidate。

## P06 — Performance Gate

utility 不正不得 hot。

## P07 — Security Gate

security fail 不得 hot。

## P08 — Hot Route

hot path 降低 latency / source reads。

## P09 — Composite Decompression

route 可還原 underlying path。

## P10 — Route Rebuildability

刪 route store 不失 canonical memory。

---

# 166. Acceptance Matrix：Authorization

## A01 — Identity Before Route

unresolved resident deny private route。

## A02 — Capability Gate

missing capability route unavailable。

## A03 — Permission Gate

permission denied 不 broader fallback。

## A04 — Project Scope

A route 不讀 B。

## A05 — Cross-Resident Private

deny。

## A06 — Shared Scope

explicit shared 才可。

## A07 — Capability Revision

change -> revalidate。

## A08 — Permission Revision

change -> invalidate。

## A09 — Source Revision

change -> stale。

## A10 — Semantic Revision

change -> stale/revalidate。

---

# 167. Acceptance Matrix：Revocation

## R01 — Permission Revoke

dependent hot route revoked。

## R02 — Delegation Expiry

dependent route revoked。

## R03 — Project Membership Revoke

dependent route revoked。

## R04 — Source Revoke

derived routes stale。

## R05 — Closure Completeness

dependency closure 不漏 active route。

## R06 — Cache Invalidation

cache 失效。

## R07 — Active Context Refresh

critical revoke 推 refresh。

## R08 — Incomplete Closure

sensitive profile fail closed。

---

# 168. Acceptance Matrix：Prompt Injection

## I01 — External Instruction

不產生 capability。

## I02 — Crystalized Injection

derived crystal 仍是 data。

## I03 — Fake Approval

external source 寫「approved」無效。

## I04 — Fake Permission

memory 寫「admin」無效。

## I05 — Tool Request

memory content 不能直接 action。

---

# 169. Acceptance Matrix：Fallback

## F01 — Resolver Error

technical fallback 成功。

## F02 — Cache Miss

slow path 成功。

## F03 — Target Superseded

dynamic route repair 或 static stale。

## F04 — Unauthorized

deny，不 fallback broader search。

## F05 — Fidelity Mismatch

不得用 overview 冒充 exact。

---

# 170. Acceptance Matrix：Portability

## T01 — Path Relocation

physical path 變更 route 仍 resolve。

## T02 — Cross-OS

Windows / Linux ObjectRef 一致。

## T03 — Cross-Model

不同 model 執行同 route schema。

## T04 — Web/Agent

同 route 在不同 profile 做 capability decision。

## T05 — Provider Migration

logical target route 可重綁。

---

# 171. Performance Benchmarks

測：

```text
cold_latency
warm_latency
hot_latency
selector_latency
authorization_latency
materialization_bytes
source_reads
context_tokens
```

---

# 172. Security Benchmarks

測：

```text
unauthorized_route_attempts
stale_route_hits
revocation_latency
permission_cache_misses
cross_scope_denials
prompt_injection_action_attempts
```

---

# 173. Scalability Benchmarks

route count：

$$
10^2,10^4,10^6.
$$

memory object count：

$$
10^3,10^5,10^7.
$$

測 selector / dependency / invalidation。

---

# 174. Revocation Benchmark

建立 source：

$$
x
$$

被：

$$
10^k
$$

routes 依賴。

量測：

$$
T_{\mathrm{revoke}}(k).
$$

---

# 175. Selection Congestion Benchmark

增加同 query class 候選 route 數量，測 selection cost。

---

# 176. Break-Even Benchmark

對重複 query：

$$
n=1,\ldots,N.
$$

找：

$$
n^*
$$

使 cumulative CHM cost 開始低於 cold baseline。

---

# 177. Route Quality Benchmark

比較：

- target correctness；
- exact fidelity；
- stale rate；
- contradiction retention；
- source diversity。

---

# 178. Runtime Observability

需要 metrics endpoint / log：

```text
route_hits
route_misses
route_promotions
route_demotions
route_repairs
route_revocations
fallbacks
authorization_denials
cold_recalls
```

---

# 179. Event Types

```text
route_observed
route_candidate_created
route_promoted
route_executed
route_failed
route_repaired
route_demoted
route_revoked
route_retired
permission_changed
capability_changed
source_changed
semantic_changed
```

---

# 180. Route Lifecycle Receipt

所有 state transition 產 receipt。

---

# 181. Milestone B0

完成：

```text
QueryClass
RouteReceipt
CompiledRoute
RouteRegistry
basic RouteExecutor
```

只用 public / project read-only fixture。

---

# 182. Milestone B1

增加：

```text
CapabilityEnvelope
PermissionBinding
SafeWorldBuilder
authorization guards
revision binding
```

---

# 183. Milestone B2

增加：

```text
PerformanceGate
SecurityGate
route promotion
route demotion
route metrics
```

---

# 184. Milestone B3

增加：

```text
RevocationEngine
DependencyIndex
Cache invalidation
critical push
```

---

# 185. Milestone B4

增加：

```text
NavigationCrystal integration
query-class learning
route repair
semantic aliases
composite route
```

---

# 186. Milestone B5

跨 runtime：

```text
Web profile
Agent profile
cross-model route execution
cross-provider logical target resolution
```

---

# 187. 首代不實作

```text
action hyperlinks
credential routes
registrar writes
automatic declassification
irreversible external effects
cross-resident private writes
resident merge
```

---

# 188. Runtime Profiles

## WebAHR/0.1

```text
single_resident
read_only
project/resident memory
no cross-resident private
no action hyperlink
```

## AgentAHR/0.1

```text
multi-line
local source routes
MCP resource routes
delegated project reads
no unrestricted action hyperlink
```

---

# 189. Config Baseline

範例：

```json
{
  "profile": "AgentAHR/0.1",
  "route_limits": {
    "max_hops": 12,
    "max_retries": 2,
    "max_candidates_per_query_class": 8
  },
  "promotion": {
    "reuse_min": 3,
    "success_min": 0.9,
    "validation_min": 0.95
  },
  "security": {
    "deny_overrides": true,
    "revalidate_permission_on_use": true,
    "revalidate_identity_on_private_route": true
  }
}
```

---

# 190. 參考 Route Execution Pseudocode

```text
execute(memory_need):
    identity = resolve_identity()
    if identity != resolved:
        deny_private()

    capabilities = load_capability_envelope()
    permissions = load_permission_bindings()
    safe_world = build_safe_world(identity, capabilities, permissions)

    query_class = classify(memory_need)
    route = select_authorized_route(query_class, safe_world)

    if route is None:
        return cold_recall(memory_need, safe_world)

    if not revisions_match(route):
        route = revalidate_or_demote(route)

    if not authorize_route(route, safe_world):
        deny()

    try:
        result = execute_route(route)
    except TechnicalFailure:
        result = safe_fallback(route, memory_need, safe_world)

    validate(result)
    emit_route_receipt()
    return result
```

---

# 191. PathCompiler Pseudocode

```text
compile(query_class, receipts):
    normalized = normalize_receipts(receipts)
    candidate = extract_stable_route(normalized)

    performance = performance_gate(candidate)
    security = security_gate(candidate)

    if not performance.pass:
        return warm_route

    if not security.pass:
        return rejected_candidate

    compiled = build_compiled_route(candidate)
    store(compiled)
    emit_promotion_receipt()
    return compiled
```

---

# 192. Revocation Pseudocode

```text
revoke(source_ref):
    mark_source_revoked(source_ref)
    affected = dependency_closure(source_ref)

    for object in affected:
        if object.kind == compiled_route:
            mark_revoked(object)
        if object.kind == cache:
            delete(object)
        if object.kind == projection:
            mark_stale(object)

    emit_revocation_receipt()
    notify_active_runtime_if_critical()
```

---

# 193. 安全不變式

## HR-1

$$
\boxed{
Reachable
\neq
Authorized.
}
$$

## HR-2

$$
\boxed{
Authorized
\neq
Trusted.
}
$$

## HR-3

$$
\boxed{
Capability
\neq
Permission.
}
$$

## HR-4

$$
\boxed{
PathCompilation
\neq
PermissionCompilation.
}
$$

## HR-5

$$
\boxed{
MemoryData
\neq
ActionAuthority.
}
$$

## HR-6

$$
\boxed{
Summarization
\neq
Declassification.
}
$$

## HR-7

$$
\boxed{
TechnicalFail
\Rightarrow
SafeFallback.
}
$$

## HR-8

$$
\boxed{
AuthorityFail
\Rightarrow
Deny.
}
$$

## HR-9

$$
\boxed{
Revoke(x)
\Rightarrow
InvalidateClosure(x).
}
$$

## HR-10

$$
\boxed{
FasterPath
\not\Rightarrow
GreaterAuthority.
}
$$

---

# 194. Performance 不變式

## HP-1

$$
\boxed{
ObservedRoute
\not\Rightarrow
CompiledRoute.
}
$$

## HP-2

$$
\boxed{
U(\ell)>0
}
$$

才值得 promotion。

## HP-3

$$
\boxed{
Delete(RouteStore)
\not\Rightarrow
Loss(CanonicalMemory).
}
$$

## HP-4

$$
\boxed{
HotPath
\text{ must have fallback}.
}
$$

## HP-5

$$
\boxed{
CompiledPath
\rightarrow
AuditableProvenance.
}
$$

---

# 195. 與 TW-A 的接口

TW-B 不重新定義：

```text
ArtifactAddress
ObjectRef
revision
digest
scope
resolver
schema registry
canonical source map
```

而是直接使用。

CompiledRoute `target_ref` 必須是 TW-A ObjectRef。

---

# 196. 與 LIMEN 的接口

LIMEN 提供：

```text
resident_ref
line_ref
task_ref
identity_status
authority_revision
```

AHR 不自行 resolve identity。

---

# 197. 與 MNEME 的接口

MNEME 提供：

```text
canonical memory objects
memory heads
provenance
exact source expansion
```

AHR 只加速定位。

---

# 198. 與 SOACR 的接口

SOACR 提供：

```text
MemoryNeed
purpose
fidelity
scope
budget
stop_condition
```

AHR 由此選 query class / route。

---

# 199. 與 CSG 的接口

CSG 提供：

```text
semantic crystals
relations
higher-order crystals
navigation crystals
semantic revisions
```

---

# 200. 與 MRMIC/NVCL 的接口

可用：

```text
provider resource ref
runtime presence
principal binding
workspace/task mapping
```

但 resource projection 不改 resident authority。

---

# 201. 與 UNPNP 的接口

本規格將 UNPNP Path Compilation 具體化為 memory-domain runtime：

$$
\boxed{
\text{Repeated Recall Computation}
\rightarrow
\text{Validated Route}
\rightarrow
\text{Compiled Hyperlink}
}
$$

並保留 complexity transfer：

$$
\boxed{
\text{Complexity is transferred, not destroyed}.
}
$$

---

# 202. 第一代交付物

實作完成後至少應有：

```text
schemas/
route-registry/
query-classes/
route-receipts/
compiled-routes/
metrics/
revocation/
fixtures/
tests/
acceptance/
```

---

# 203. 必要 Schema 清單

```text
ahr-query-class/0.1
ahr-memory-need-binding/0.1
ahr-capability-envelope/0.1
ahr-permission-binding/0.1
ahr-safe-world/0.1
ahr-route-receipt/0.1
ahr-compiled-route/0.1
ahr-performance-gate/0.1
ahr-security-gate/0.1
ahr-fallback-policy/0.1
ahr-route-repair/0.1
ahr-route-metrics/0.1
ahr-revocation-receipt/0.1
ahr-route-audit/0.1
ahr-semantic-alias/0.1
```

---

# 204. 最終工程結論

AHR/PCR 的真正目的不是讓 AI「跳過更多步驟」，而是將反覆成功、可驗證、可授權、可失效的記憶路徑轉成 runtime primitive。

因此一條好的 compiled route 必須同時回答：

> 這條路針對哪類 MemoryNeed？  
> 它從哪裡開始？  
> 它到哪裡？  
> 它需要哪些 capability？  
> 它適用哪個 scope？  
> 它依賴哪些 permission？  
> 它綁哪些 source / semantic revisions？  
> 它如何驗證？  
> 它何時失效？  
> 失效時 fallback 去哪？  
> 哪些 revocation 會影響它？  
> 它為什麼值得被編譯？  
> 它能否被 audit / decompress？

因此最終 runtime 關係是：

$$
\boxed{
\text{Memory Need}
\rightarrow
\text{Authorized Reachable World}
\rightarrow
\text{Best Valid Route}
\rightarrow
\text{Materialized Memory}
}
$$

而長期學習關係是：

$$
\boxed{
\text{Repeated Valid Recall}
\rightarrow
\text{Navigation Knowledge}
\rightarrow
\text{Selective Path Compilation}
}
$$

最後的安全底線是：

$$
\boxed{
\text{Path optimization may reduce computation, but it may never reduce authorization requirements}.
}
$$

以及：

$$
\boxed{
\text{Revocation must remain stronger than cached acceleration}.
}
$$

這使 Named-AI Cognitive Runtime 可以隨長期記憶增長逐漸「學會怎麼回想」，而不是讓記憶規模越大，AI 每一次 recall 都重新進行一次全域搜尋。

---

## Appendix A — 第一代 Route State

```text
cold
warm
candidate
hot
stale
revoked
retired
invalid
```

---

## Appendix B — 第一代 Route Kind

```text
overview
current_state
decision
exact_source
verification
historical
open_loop
project_state
navigation
```

---

## Appendix C — 第一代 Failure Classes

```text
not_found
resolver_error
cache_miss
route_stale
target_superseded
backend_unavailable
unauthorized
permission_revoked
resident_unresolved
scope_mismatch
capability_missing
delegation_expired
unknown_schema
validation_failed
```

---

## Appendix D — 與 TW-A 合併後的核心工程鏈

$$
\boxed{
\text{ObjectRef}
\rightarrow
\text{Resolver}
\rightarrow
\text{Authorized Route}
\rightarrow
\text{Materialization}
\rightarrow
\text{Validation}
\rightarrow
\text{Receipt}
}
$$

這構成 Residence / CSG Storage 與 Authorized Hyperlink Runtime 的第一代共同工程基礎。
