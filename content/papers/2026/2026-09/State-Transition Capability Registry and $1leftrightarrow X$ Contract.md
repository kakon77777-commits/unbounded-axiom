# State-Transition Capability Registry and $1\leftrightarrow X$ Contract

## 狀態轉換能力登錄標準與 $1\leftrightarrow X$ 契約

**系列：** Computational Space and Hyperconnected Complexity — Engineering Whitepaper Series  
**Technical Whitepaper：** 02 / 03  
**作者：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1 Protocol / Registry Specification  
**日期：** 2026-08-29  
**文件定位：** Capability Protocol／State-Transition Contract／Registry Schema／Hyperconnected Runtime Interface  
**上游文件：**
- Computational Space and Hyperconnected Complexity Paper 01–09
- TW-01《Hyperconnected MSSP–RDR Runtime Architecture》

**下游文件：**
- TW-03《Global Complexity Accounting Ledger and Closed-Responsibility Runtime》
- MVP《Mutable Hyperconnected Capability Runtime》

---

# 摘要

理論系列提出：

$$
\boxed{
\text{Computer}
=
\text{Addressable State-Transition Space}
}
$$

並以：

$$
\boxed{
1\rightarrow1,
\qquad
1\rightarrow X,
\qquad
X\rightarrow1,
\qquad
X\rightarrow X
}
$$

描述計算空間中的四種基本關係。

TW-01 已將此思想落為 Hyperconnected MSSP–RDR Runtime，建立：

- Registry；
- Resolver；
- Selector；
- Composer；
- Constructor；
- Materializer；
- Executor；
- Verifier；
- Boundary Controller；
- Capability Promotion。

然而，如果：

$$
1_i
$$

仍只是人類口頭理解的「某個工具名稱」，而：

$$
X_i
$$

也只是模糊的「它能做一些事情」，整個超連接 Runtime 仍無法可靠運作。

本白皮書因此提出：

# State-Transition Capability Contract, STCC

**狀態轉換能力契約。**

其核心是把一個 capability 定義為：

$$
\boxed{
\mathcal C_i
=
(
I_i,
D_i^{in},
D_i^{out},
\Phi_i,
P_i,
B_i,
V_i,
A_i,
C_i,
H_i
)
}
$$

其中：

- $I_i$：Identity；
- $D_i^{in}$：合法輸入狀態域；
- $D_i^{out}$：合法輸出狀態域；
- $\Phi_i$：transition contract；
- $P_i$：provider realization；
- $B_i$：bridge / compatibility；
- $V_i$：verification；
- $A_i$：authority / permission；
- $C_i$：complexity / cost；
- $H_i$：history / provenance / version。

因此：

$$
\boxed{
1_i
=
\operatorname{Address}(\mathcal C_i)
}
$$

不再只是 function name，而是一個可以被 Runtime 解析成完整 state-transition contract 的 canonical address。

本文同時建立：

$$
\boxed{
X\rightarrow1
}
$$

的工程意義：

> 一段複雜計算、演算法、workflow、model 或 provider 行為，只有在被壓縮為具有穩定 identity、明確 state domain、transition semantics、verification 與 provenance 的 contract 後，才真正成為 Runtime 可重用 capability。

因此：

$$
\boxed{
X
\rightarrow
1
}
$$

不是單純命名，而是：

# Capability Canonicalization

而：

$$
\boxed{
1
\rightarrow
X
}
$$

則是：

# Capability Realization

完整循環為：

$$
\boxed{
X_{\mathrm{candidate}}
\rightarrow
1_{\mathrm{canonical}}
\rightarrow
X_{\mathrm{realized}}.
}
$$

本文最終建立：

1. capability identity model；
2. state-domain model；
3. transition contract；
4. provider contract；
5. bridge contract；
6. verification contract；
7. authority contract；
8. complexity contract；
9. provenance / version contract；
10. trust / lifecycle state machine；
11. canonical JSON/YAML schema；
12. conformance rules；
13. registry operations；
14. promotion / revocation / migration protocol。

---

# 1. 為什麼需要一個正式 Capability Protocol？

假設 Runtime Registry 中有：

```text
search
```

```text
analyze
```

```text
solve
```

這些名稱對人類看起來很直觀。

但對 Runtime 而言，它不知道：

- search 什麼？
- input 是什麼？
- output 是什麼？
- exact 還是 approximate？
- deterministic 還是 stochastic？
- 可以用哪些 provider？
- 需要 network 嗎？
- output 可不可以直接交給下一個 capability？
- 如何驗證？

因此：

$$
\boxed{
\text{Name}
\neq
\text{Capability Contract}.
}
$$

---

# 2. Capability 的真正對象

本文將 capability 定義為：

> **在指定輸入狀態域上，按照明確語義與約束，能夠產生指定輸出狀態域，並具有可解析實現與可驗證結果的狀態轉換能力。**

形式上：

$$
\boxed{
\Phi_i:
D_i^{in}
\rightarrow
D_i^{out}.
}
$$

但只有 $\Phi_i$ 還不夠。

---

# 3. Canonical Capability Object

完整 capability：

$$
\boxed{
\mathcal C_i
=
(
I,
D_{in},
D_{out},
\Phi,
P,
B,
V,
A,
C,
H
).
}
$$

這是本白皮書的 canonical object。

---

# 4. Identity — $I$

Identity 必須回答：

> 「這一個 capability 到底是哪一個？」

例如：

```yaml
identity:
  capability_id: cap.graph.shortest_path
  version: 1.0.0
  namespace: evemiss.graph
```

---

# 5. Capability ID 必須穩定

Provider 可以改。

Implementation 可以改。

但：

$$
\boxed{
\text{Capability Identity}
\neq
\text{Implementation Identity}.
}
$$

如果 contract 沒變：

```text
cap.graph.shortest_path@1.x
```

可以換 provider。

---

# 6. 什麼時候必須升 Major Version？

如果：

- input semantics 改變；
- output semantics 改變；
- exactness 改變；
- task family 改變；
- success condition 改變；

則：

$$
\boxed{
\text{semantic contract changed}.
}
$$

應升 major。

---

# 7. State Domain — $D_{in}$

輸入不能只寫：

```text
object
```

而應有：

$$
\boxed{
D_{in}
}
$$

例如：

```yaml
input_domain:
  type: weighted_graph
  constraints:
    directed: allowed
    negative_weights: false
```

---

# 8. Output Domain — $D_{out}$

同理：

```yaml
output_domain:
  type: shortest_path_result
  fields:
    path: node_sequence
    total_cost: number
```

---

# 9. Domain Contract 的作用

只有 domain 明確，

Composer 才知道：

$$
\operatorname{Output}(A_i)
\rightarrow
\operatorname{Input}(A_j)
$$

是否合法。

---

# 10. State Identity

兩個 JSON object 可能 schema 一樣，

但 semantic type 不一樣。

例如：

```json
{"x": 1, "y": 2}
```

可以是：

- coordinate；
- bounding box；
- vector；
- node pair。

因此：

$$
\boxed{
\text{Structural Equality}
\neq
\text{Semantic Type Equality}.
}
$$

---

# 11. Typed State

本文要求 state 至少具有：

$$
\boxed{
X
=
(
\text{Type},
\text{Schema},
\text{Semantics},
\text{Version}
).
}
$$

---

# 12. Transition Contract — $\Phi$

Transition Contract 描述：

$$
\boxed{
\Phi:
D_{in}
\rightarrow
D_{out}.
}
$$

例如：

```yaml
transition:
  operation: shortest_path
  semantics: minimum_sum_edge_weight
  exactness: exact
  determinism: deterministic
```

---

# 13. Transition 不等於 Implementation

Dijkstra 是 implementation。

Shortest Path 是 capability semantics。

因此：

$$
\boxed{
\text{Transition Semantics}
\neq
\text{Algorithm Implementation}.
}
$$

---

# 14. Exactness

至少分：

```text
EXACT
APPROXIMATE
HEURISTIC
PROBABILISTIC
BEST_EFFORT
```

---

# 15. Exactness 不能由 Provider 偷改

若 capability contract：

```text
EXACT
```

provider 不能返回 heuristic solution 再自稱 success。

---

# 16. Determinism

至少：

```text
DETERMINISTIC
SEEDED_STOCHASTIC
UNSEEDED_STOCHASTIC
EXTERNAL_NONDETERMINISTIC
```

---

# 17. Idempotence

一些 capability 可以：

$$
\Phi(\Phi(x))
=
\Phi(x).
$$

可標：

```yaml
properties:
  idempotent: true
```

對 retry 很重要。

---

# 18. Side Effect

Transition 還需標：

```text
PURE
READ_ONLY
STATE_MUTATING
EXTERNAL_EFFECT
IRREVERSIBLE_EFFECT
```

---

# 19. 為什麼 Side Effect 是 Capability Contract 的一部分？

因為：

$$
\boxed{
\text{computation}
\neq
\text{observation only}.
}
$$

有些 capability 會：

- 寫檔；
- 發信；
- deploy；
- 修改 DB；
- 控制硬體。

Runtime 必須知道。

---

# 20. Reversibility

可標：

```yaml
effect:
  reversible: true
  rollback_capability: cap.file.restore
```

---

# 21. Rollback 不等於 Compensation

若無法真正逆轉，

可以：

```yaml
effect:
  reversible: false
  compensatable: true
  compensation_capability: cap.payment.refund
```

---

# 22. Provider Contract — $P$

Provider 是 capability 的實際 realization。

形式：

$$
\boxed{
P_j
\models
\mathcal C_i.
}
$$

表示 provider $P_j$ 符合 capability contract。

---

# 23. Provider Types

至少：

```text
LOCAL_FUNCTION
LOCAL_PROCESS
CONTAINER
GPU_WORKER
LAN_WORKER
CLOUD_SERVICE
EXTERNAL_API
AGENT
HUMAN
HARDWARE_DEVICE
```

---

# 24. Provider Manifest

```yaml
provider:
  provider_id: provider.graph.local-python
  provider_type: local_process

  implements:
    capability_id: cap.graph.shortest_path
    capability_version: ">=1.0 <2.0"

  runtime:
    language: python
    version: "3.12"

  trust:
    level: trusted_local
```

---

# 25. Provider Capability Claim

Provider 不應只說：

> 我能做 shortest path。

它必須通過：

$$
\boxed{
\operatorname{ConformanceTest}
(
P,
\mathcal C
).
}
$$

---

# 26. Provider Conformance

至少檢查：

- input acceptance；
- output schema；
- semantic correctness；
- error behavior；
- deterministic contract；
- effect policy；
- version compatibility。

---

# 27. Provider 可以有不同 Cost

同 capability：

$$
\mathcal C
$$

可由：

$$
P_1,
P_2,
P_3
$$

實現。

例如：

- CPU；
- GPU；
- remote API。

這正是 RDR routing 的基礎。

---

# 28. Bridge Contract — $B$

若：

$$
D_i^{out}
\neq
D_j^{in},
$$

需要：

$$
\boxed{
B_{ij}
:
D_i^{out}
\rightarrow
D_j^{in}.
}
$$

---

# 29. Bridge 本身也是 Capability

因此：

$$
\boxed{
B_{ij}
\in
\mathcal A.
}
$$

不應特殊硬編碼。

---

# 30. Bridge Classification

至少：

```text
LOSSLESS
SEMANTICALLY_EQUIVALENT
APPROXIMATE
LOSSY
NONREVERSIBLE
```

---

# 31. Lossless Bridge

若：

$$
B^{-1}
$$

可恢復原 state，

或指定 task semantics 完整保留：

$$
\boxed{
q(B(x))
\equiv
q(x).
}
$$

---

# 32. Task-Relative Fidelity

有些 bridge 不是 global lossless，

但對 task 足夠。

因此：

$$
\boxed{
Fidelity(B,q).
}
$$

需要相對 task contract 判定。

---

# 33. Bridge Example

```yaml
bridge:
  capability_id: cap.bridge.csv_to_table

  source_type: csv_document
  target_type: typed_table

  fidelity:
    class: lossless_for_declared_schema

  verification:
    row_count_preserved: true
    field_hash_required: true
```

---

# 34. Verification Contract — $V$

Capability 必須回答：

> 如何知道它真的完成任務？

因此：

$$
\boxed{
V:
(
x,
y,
evidence
)
\rightarrow
Status.
}
$$

---

# 35. Verification Levels

建議：

```text
V0_SCHEMA
V1_PROPERTY
V2_CROSS_CHECK
V3_FORMAL
V4_EXTERNAL_AUDITED
```

---

# 36. V0 — Schema

只驗格式。

不能代表 semantic correctness。

---

# 37. V1 — Property

例如 shortest path：

- path connected；
- cost equals sum；
- source/target 正確。

---

# 38. V2 — Cross Check

由另一 implementation 重算。

---

# 39. V3 — Formal Verification

使用 proof / checker。

---

# 40. V4 — External Audit

適合高風險能力。

---

# 41. Verification 是 Capability 的 first-class field

不能只在測試階段臨時想。

每個 capability 都應聲明：

```yaml
verification:
  minimum_level: V1_PROPERTY
  verifier_capability: cap.verify.shortest_path
```

---

# 42. Self-Verification 不一定足夠

如果 solver 自己說：

> 我是對的。

這不構成獨立 verification。

因此可標：

```yaml
verification:
  independent_provider_required: true
```

---

# 43. Authority Contract — $A$

Capability 可以存在，

但未必任何 actor 都可以用。

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

---

# 44. Authority Fields

```yaml
authority:
  required_permissions:
    - filesystem.read

  forbidden_permissions:
    - filesystem.write
    - network.unrestricted
```

---

# 45. Side-Effect Capability 需要更強 Authority

例如：

```text
send_email
deploy_service
delete_file
transfer_money
```

不能與純 computation 同一 policy。

---

# 46. Authority Classification

可分：

```text
A0_PURE
A1_READ
A2_LOCAL_MUTATION
A3_EXTERNAL_MUTATION
A4_HIGH_IMPACT
```

---

# 47. Capability Candidate 預設只能 A0/A1

generated candidate 不應直接取得高權限。

---

# 48. Complexity Contract — $C$

TW-03 會完整展開。

但本 Registry 先保留接口：

$$
\boxed{
C_i
=
(
C_{\mathrm{online}},
C_{\mathrm{offline}},
C_{\mathrm{external}},
C_{\mathrm{verify}},
C_{\mathrm{maintain}}
).
}
$$

---

# 49. Complexity Profile

```yaml
complexity:
  asymptotic:
    time: "O((V+E) log V)"
    space: "O(V+E)"

  empirical:
    latency_p50_ms: 10
    latency_p95_ms: 25

  external:
    present: false

  accounting_status: CLOSED_ACCOUNTED
```

---

# 50. Asymptotic Claim 必須有狀態

```text
UNDECLARED
EMPIRICAL_ONLY
CLAIMED
FORMALLY_SUPPORTED
```

---

# 51. 不可把文字寫進去就當證明

例如：

```yaml
time: "O(1)"
```

不代表 Runtime 接受它是真的。

還需：

```yaml
claim_status: CLAIMED
```

---

# 52. Provenance Contract — $H$

Capability 必須知道：

> 從哪裡來？

至少：

- author；
- generated_by；
- parent capabilities；
- source artifact；
- validation record；
- version history。

---

# 53. Provenance Example

```yaml
provenance:
  created_by: agent.solver-03
  created_at: 2026-08-29T10:00:00Z

  parents:
    - cap.graph.bfs@1.2
    - cap.bridge.generic_graph@1.0

  source:
    repo: local
    artifact_hash: sha256:...
```

---

# 54. History Is Not Optional

沒有 provenance 的 candidate 不應直接 trusted。

因為未來出錯時：

$$
\boxed{
\text{No Provenance}
\rightarrow
\text{No Reliable Rollback}.
}
$$

---

# 55. Canonical $1_i$

現在可以正式定義：

$$
\boxed{
1_i
=
(
capability\_id,
major\_version
)
}
$$

作為 semantic address。

---

# 56. Minor/Patch 是否放入 address？

可由 resolution policy 決定。

例如：

```text
cap.graph.shortest_path@1
```

代表：

> 任意 compatible 1.x provider。

若要求完全 reproducible：

```text
cap.graph.shortest_path@1.4.2
```

---

# 57. Symbolic Address 與 Physical Location 分離

$$
\boxed{
1_i
\neq
URI(P_i).
}
$$

Capability address 不應綁定 provider URL。

---

# 58. Address Resolution

$$
\boxed{
1_i
\xrightarrow{\text{Registry}}
\mathcal C_i
\xrightarrow{\text{RDR}}
P_j.
}
$$

---

# 59. $1\rightarrow X$ 的工程形式

完整：

$$
\boxed{
1_i
\rightarrow
\mathcal C_i
\rightarrow
P_j
\rightarrow
X_{out}.
}
$$

---

# 60. $X\rightarrow1$ 的工程形式

一個新 algorithm：

$$
X_{candidate}
$$

要經：

$$
\boxed{
\text{Canonicalize}
\rightarrow
\text{Validate}
\rightarrow
\text{Version}
\rightarrow
\text{Register}
}
$$

才變成：

$$
1_{new}.
$$

---

# 61. Canonicalization Pipeline

```text
Candidate Implementation
        ↓
Infer / Declare Contract
        ↓
Type Validation
        ↓
Task Fidelity
        ↓
Provider Conformance
        ↓
Verification Contract
        ↓
Cost / Authority Metadata
        ↓
Provenance
        ↓
Canonical Capability ID
```

---

# 62. 因此 X→1 不是 rename()

這是本篇最重要的工程結論之一：

$$
\boxed{
X\rightarrow1
\neq
\text{Name Assignment}.
}
$$

而是：

$$
\boxed{
X\rightarrow1
=
\text{Canonical Capability Formation}.
}
$$

---

# 63. Trust State Machine

每個 capability：

```text
DRAFT
CANDIDATE
VALIDATED
TRUSTED
DEPRECATED
REVOKED
SUPERSEDED
```

---

# 64. DRAFT

schema 還可能不完整。

不能執行。

---

# 65. CANDIDATE

contract 完整，可進 sandbox。

---

# 66. VALIDATED

通過指定 tests，

但可能只允許 restricted scope。

---

# 67. TRUSTED

可進正常 routing。

---

# 68. DEPRECATED

仍可用，

但不應作新 plan 的首選。

---

# 69. REVOKED

禁止 materialize。

---

# 70. SUPERSEDED

有 successor。

---

# 71. Lifecycle Transition 必須受 policy

例如：

$$
\text{CANDIDATE}
\rightarrow
\text{TRUSTED}
$$

不能由 candidate 自己宣告。

---

# 72. Promotion Authority

Registry 應保存：

```yaml
promotion:
  approved_by:
    - verifier.core
  policy_id: promotion.standard.v1
```

---

# 73. Revocation Authority

高風險 capability 應允許緊急 revoke。

---

# 74. Dependency Model

每 capability：

$$
Dep(C_i)
$$

可包含：

- hard dependency；
- soft dependency；
- optional accelerator；
- verification dependency。

---

# 75. Hard Dependency

沒有就不能執行。

---

# 76. Soft Dependency

沒有仍可執行，但性能下降。

---

# 77. Verification Dependency

不影響 execution，

但影響 result promotion。

---

# 78. Dependency Cycle

若：

$$
A\rightarrow B\rightarrow A,
$$

需要檢測。

並區分：

- legal recursive；
- illegal initialization cycle。

---

# 79. Capability Composition

Composite capability：

$$
\boxed{
C^\star
=
C_k\circ\cdots\circ C_1.
}
$$

可被重新 canonicalize 成：

$$
1_{C^\star}.
$$

這是 capability compounding 的核心。

---

# 80. Composite Manifest

```yaml
composition:
  steps:
    - cap.parse.document@1
    - cap.extract.graph@2
    - cap.graph.shortest_path@1
```

---

# 81. Composite Identity 不應只靠 steps hash

因為：

- task semantics；
- bridge；
- policy；

也屬 contract。

因此 canonical hash 應覆蓋完整 semantic manifest。

---

# 82. Semantic Hash

可建立：

$$
\boxed{
H_{semantic}(C)
}
$$

只 hash semantic contract。

---

# 83. Implementation Hash

另外：

$$
\boxed{
H_{impl}(P).
}
$$

分離 semantic identity 與 implementation identity。

---

# 84. 為什麼需要兩個 Hash？

Provider 升級：

$$
H_{impl}
$$

變。

若 contract 不變：

$$
H_{semantic}
$$

可以不變。

---

# 85. Reproducibility Pin

強 reproducibility plan 應 pin：

```yaml
pin:
  capability_semantic_hash: ...
  provider_hash: ...
  environment_hash: ...
```

---

# 86. Error Contract

Capability 必須聲明錯誤狀態。

例如：

```yaml
errors:
  - code: NO_PATH
  - code: INVALID_INPUT
  - code: RESOURCE_LIMIT
  - code: PROVIDER_FAILURE
```

---

# 87. Error 不應全部變 Exception 字串

Runtime 需要 typed error。

---

# 88. Partial Result

某 capability 可合法返回 partial。

但必須聲明：

```yaml
output:
  partial_allowed: true
```

否則 partial 不算 success。

---

# 89. Streaming Capability

某些 transition：

$$
X_t\rightarrow X_{t+1}
$$

是 streaming。

可標：

```yaml
execution_model: STREAMING
```

---

# 90. Long-Running Capability

例如 simulation：

```yaml
execution_model: LONG_RUNNING
```

需要 checkpoint / cancellation。

---

# 91. Event Capability

```yaml
execution_model: EVENT_DRIVEN
```

可直接接 PCMT / 24/72 configuration。

---

# 92. Computational Configuration Annotation

Capability 可以選擇性聲明：

```yaml
computation:
  substrate: discrete
  update_mode: parallel
  observation: discrete
  transition_law: deterministic
```

對應 24/72。

---

# 93. PCMT Annotation

```yaml
phase:
  supported: true
  machine_class:
    - graph
    - event
```

---

# 94. GCM Annotation

可標：

```yaml
gcm:
  domain: graph
  realization_modes:
    - cpu
    - gpu
```

---

# 95. 這些 Annotation 不是核心必填

Registry core 不應綁死所有上游理論。

因此分：

$$
\boxed{
\text{Core Contract}
+
\text{Extension Profiles}.
}
$$

---

# 96. Core Contract

所有 capability 必填：

- identity；
- input；
- output；
- transition；
- provider interface；
- verification；
- trust；
- version。

---

# 97. Extension Profile

可選：

- GCM；
- PCMT；
- 24/72；
- Agentic acquisition；
- security；
- economic cost。

---

# 98. Schema Version

Registry schema 自己也要版本化：

```yaml
schema_version: stcc-0.1
```

---

# 99. Contract Migration

如果：

```text
stcc-0.1 → stcc-0.2
```

需要 migration。

不能直接假裝舊 capability 相容。

---

# 100. Registry Operation

至少：

```text
REGISTER
RESOLVE
UPDATE_PROVIDER
DEPRECATE
REVOKE
SUPERSEDE
PROMOTE
QUERY
AUDIT
```

---

# 101. REGISTER

只有 contract valid 才可 register。

---

# 102. RESOLVE

輸入：

- task signature；
- version range；
- policy。

輸出候選。

---

# 103. UPDATE_PROVIDER

不改 semantic contract。

---

# 104. SUPERSEDE

建立 lineage：

$$
C_{old}
\rightarrow
C_{new}.
$$

---

# 105. AUDIT

檢查：

- contract drift；
- stale provider；
- missing verifier；
- unknown cost；
- dependency failure。

---

# 106. Registry Consistency

任何時刻應避免：

$$
\boxed{
\text{same address}
\rightarrow
\text{two incompatible semantic contracts}.
}
$$

---

# 107. Conflict Rule

若 semantic hash 不同，

不能使用同一 major identity。

---

# 108. Provider Drift

Provider 更新後，

如果 behavior 不再符合 contract：

$$
P_j
\not\models
C_i.
$$

則必須：

$$
\boxed{
REVOKE(P_j\text{ realization}).
}
$$

不必 revoke capability 本身。

---

# 109. Capability 仍可由其他 Provider 存活

$$
\boxed{
\text{Provider Failure}
\neq
\text{Capability Nonexistence}.
}
$$

---

# 110. Capability Availability

定義：

$$
\boxed{
Avail(C_i,t)
=
\exists P_j:
P_j\models C_i
\land
P_j\text{ active}.
}
$$

---

# 111. Capability Exists vs Available

$$
\boxed{
\text{Registered}
\neq
\text{Currently Realizable}.
}
$$

這也是 Agent state 的一部分。

---

# 112. Scope Contract

Capability 可以只對部分 domain valid。

例如：

```yaml
scope:
  max_nodes: 100000
  negative_edges: false
```

---

# 113. Scope 不得隱藏

否則 Resolver 會把 bounded capability 當 universal。

---

# 114. Claim Scope

例如：

```yaml
claim:
  family_scope: bounded
  max_input_size: 100
```

這與 Paper 07 的 finite-world distinction 對接。

---

# 115. General Solver Claim

若聲稱 general：

```yaml
claim:
  family_scope: unbounded
```

必須有更強 validation / proof responsibility。

---

# 116. Complexity Proof Attachment

可：

```yaml
complexity:
  claim_status: formally_supported
  proof_artifact: artifact://proofs/...
```

---

# 117. Proof Checker

如果可機器驗證，

保存：

```yaml
proof_checker_capability:
  cap.proof.lean.verify
```

---

# 118. Candidate Solver 對 P/NP 類問題的規則

絕不能只因 benchmark 很快：

```text
FORMALLY_PROVED
```

最多：

```text
BOUNDED_EMPIRICAL
```

---

# 119. No-Path Result 也需要 Contract

如果 capability 聲明：

```text
prove_impossible
```

必須區分：

```text
NO_SOLUTION_IN_SEARCHED_SCOPE
```

與：

```text
FORMALLY_IMPOSSIBLE
```

---

# 120. Registry 需支持 Negative Capability Evidence

不只存 capability，

也存：

$$
\boxed{
\text{invalid / blocked / disproved transition claims}.
}
$$

---

# 121. Negative Registry

可以有：

```yaml
negative_evidence:
  task_family: foo
  candidate: bar
  status: rejected
  reason: counterexample
```

---

# 122. 為什麼 Negative Evidence 不能塞進 Capability Registry 本身？

因為：

$$
\boxed{
\text{Capability}
}
$$

與：

$$
\boxed{
\text{Research Evidence About Capability}.
}
$$

是不同 object。

建議分 store。

---

# 123. Canonical Store Layout

```text
registry/
  capabilities/
  providers/
  bridges/
  verifiers/
  schemas/

evidence/
  validations/
  failures/
  counterexamples/
  proofs/

history/
  promotions/
  revocations/
  migrations/
```

---

# 124. Registry Source of Truth

正式 state 應有單一 authority。

不能：

- UI 一份；
- DB 一份；
- provider 一份；

都能直接改。

---

# 125. Proposal / Authority Separation

UI / Agent 提交：

$$
\boxed{
Proposal.
}
$$

Authority Layer 接受後：

$$
\boxed{
Canonical Registry State.
}
$$

---

# 126. Registry Event Log

每次修改：

```yaml
event:
  type: CAPABILITY_PROMOTED
  capability_id: ...
  previous_version: ...
  actor: ...
  evidence: ...
```

---

# 127. Event Replay

應可：

$$
\boxed{
Registry_0
+
Events_{0:t}
\rightarrow
Registry_t.
}
$$

便於審計。

---

# 128. Snapshot + Event

實務上可：

$$
\boxed{
\text{Snapshot}
+
\text{Append-Only Event Log}.
}
$$

---

# 129. Registry Search

支援：

- exact ID；
- semantic task family；
- input/output type；
- provider type；
- trust；
- cost profile。

---

# 130. Resolver 不應直接查 Implementation 名稱

例如 task：

> shortest path

不應只找 function 名稱含 `shortest`。

而是查：

$$
\boxed{
\text{semantic contract}.
}
$$

---

# 131. Capability Graph

Registry 可投影為：

$$
\boxed{
G_C
=
(V_C,E_C).
}
$$

node：

- capability；
- type；
- provider。

edge：

- implements；
- consumes；
- produces；
- bridges；
- depends；
- supersedes。

---

# 132. Hyperconnected Potential Graph

所有合法 composition edge：

$$
E_{\mathrm{potential}}
$$

不必全部 materialize。

---

# 133. Active Graph

Runtime task 只 materialize：

$$
E_{\mathrm{active}}(q).
$$

---

# 134. Generator Edge

若 bridge/composition 還不存在，

Constructor 可提：

$$
e_{candidate}.
$$

通過後進 Registry。

---

# 135. 這就是 Registry 的 Mutable 性

$$
\boxed{
G_C(t)
\rightarrow
G_C(t+1).
}
$$

---

# 136. Mutable 不是 schema-free

越 dynamic，

越需要 stable contract。

所以：

$$
\boxed{
\text{Dynamic Capability Space}
}
$$

反而要求更強：

$$
\boxed{
\text{Typed Canonical Interface}.
}
$$

---

# 137. 最小 STCC Schema

第一版可以如下：

```yaml
schema_version: stcc-0.1

identity:
  capability_id: cap.example.foo
  version: 1.0.0
  namespace: example

contract:
  task_families:
    - foo

  input:
    type: foo_input
    schema_ref: schema://foo_input/v1

  output:
    type: foo_output
    schema_ref: schema://foo_output/v1

  transition:
    exactness: exact
    determinism: deterministic
    effects: pure

scope:
  family_scope: bounded
  constraints: {}

providers:
  - provider.foo.local

verification:
  minimum_level: V1_PROPERTY
  verifier_capability: cap.verify.foo

authority:
  class: A0_PURE
  required_permissions: []

complexity:
  claim_status: empirical_only
  accounting_status: lifecycle_partial

provenance:
  created_by: human
  parent_capabilities: []

trust:
  state: trusted
```

---

# 138. MVP Core Schema 可以更小

第一輪最小必填：

```text
capability_id
version
input_type
output_type
task_family
provider
verifier
trust_state
```

先跑起來。

---

# 139. 但 Semantic Contract 不可省

即使 MVP，

至少：

```text
task_family
exactness
scope
```

否則 reuse 會很快出錯。

---

# 140. Conformance Rule 1

Capability ID 唯一。

---

# 141. Conformance Rule 2

Major version 內 semantic contract 不得破壞相容性。

---

# 142. Conformance Rule 3

Trusted capability 至少一個 active conformant provider。

---

# 143. Conformance Rule 4

Trusted capability 必須有 verifier policy。

---

# 144. Conformance Rule 5

Generated candidate 不得自我 promotion。

---

# 145. Conformance Rule 6

Lossy bridge 不得在 exact task 中靜默使用。

---

# 146. Conformance Rule 7

External-effect capability 必須具有 authority contract。

---

# 147. Conformance Rule 8

Unknown complexity 不得被 canonicalize 為 zero。

---

# 148. Conformance Rule 9

Provider implementation change 必須重新跑 contract tests。

---

# 149. Conformance Rule 10

Revoked capability 不得由普通 Resolver 返回。

---

# 150. Capability Promotion Contract

Candidate：

$$
C_c
$$

至少通過：

$$
\boxed{
Schema
+
Task
+
Provider
+
Verification
+
Authority
+
Provenance.
}
$$

才可 trusted。

---

# 151. Strong Promotion

若還要宣稱可跨 unseen family reuse，

需：

- transfer test；
- scope evidence；
- complexity profile。

---

# 152. Promotion 等級

```text
P0_CANDIDATE
P1_LOCAL_VALIDATED
P2_FAMILY_VALIDATED
P3_GENERAL_CLAIM
P4_FORMALLY_VERIFIED
```

---

# 153. P3 不等於 P4

General empirical success 仍不是 formal theorem。

---

# 154. Revocation Contract

Revocation 應保存：

- reason；
- evidence；
- effective time；
- affected dependents。

---

# 155. Dependent Revalidation

若：

$$
C_a
$$

被 revoke，

所有：

$$
C_b:
C_a\in Dep^\star(C_b)
$$

進：

```text
REVALIDATION_REQUIRED
```

---

# 156. Migration

Capability major upgrade：

$$
C_1
\rightarrow
C_2
$$

可能需要：

$$
B_{1\rightarrow2}
$$

migration bridge。

---

# 157. Semantic Migration

例如 output schema 改變。

不能只改 version number。

---

# 158. Provider Migration

若只是換 provider，

不需要 capability semantic migration。

---

# 159. Registry Garbage Collection

Deprecated / revoked artifact 可 archive，

但不能刪 lineage。

---

# 160. Historical Artifact

錯誤 capability 仍可保留為：

```text
HISTORICAL_ARTIFACT
```

供研究。

---

# 161. Capability Fingerprint

可建立：

$$
\boxed{
F_C
=
H(
SemanticContract,
Version,
Schema
).
}
$$

便於 duplicate detection。

---

# 162. Duplicate Capability

若兩個 capability semantic fingerprint 相同，

可以：

- alias；
- provider merge；

而不是重複新增。

---

# 163. Near-Duplicate

semantic 相似但 scope 不同，

不能自動 merge。

---

# 164. Capability Alias

可以：

```yaml
aliases:
  - shortest_path
  - min_weight_path
```

但 canonical ID 唯一。

---

# 165. Human-Friendly Name 不是 Canonical Identity

避免 rename 破壞引用。

---

# 166. $1\leftrightarrow X$ 的完整工程循環

候選結構：

$$
X_c
$$

經：

$$
\boxed{
Canonicalize(X_c)
}
$$

得到：

$$
1_c.
$$

Runtime：

$$
1_c
\xrightarrow{Resolve}
C_c
\xrightarrow{Materialize}
P_c
\xrightarrow{Execute}
X_{out}.
$$

---

# 167. 若輸出又可形成新 Capability

$$
X_{out}
\rightarrow
1_{new}.
$$

則：

$$
\boxed{
1
\rightarrow
X
\rightarrow
1
}
$$

形成 capability compounding loop。

---

# 168. 這就是 Mutable Computer 的最小資料機制

理論：

$$
\mathcal A_t
\rightarrow
\mathcal A_{t+1}.
$$

工程：

$$
\boxed{
Registry_t
+
ValidatedCandidate
\rightarrow
Registry_{t+1}.
}
$$

---

# 169. STCC 不負責「找到」新 Capability

那是 Constructor 的責任。

STCC 負責：

> **新能力一旦出現，要滿足什麼條件才算真正存在於 Runtime 中？**

---

# 170. 因此 STCC 是 Capability Existence Boundary

如果一個 code snippet 沒有：

- identity；
- contract；
- provider；
- verifier；

它只是 artifact。

不是完整 Runtime Capability。

所以：

$$
\boxed{
\text{Artifact}
\neq
\text{Capability}.
}
$$

---

# 171. Capability Existence Criterion

本文提出：

$$
\boxed{
Exist_R(C)=1
}
$$

若且唯若至少：

1. canonical identity exists；
2. semantic transition contract exists；
3. input/output domains defined；
4. at least one realization path exists or is explicitly assumed；
5. verification policy exists；
6. trust state is defined。

---

# 172. Available Capability Criterion

$$
\boxed{
Avail_R(C,t)=1
}
$$

需要額外：

- active provider；
- permission；
- resource；
- compatible environment。

---

# 173. Executable Capability Criterion

再額外：

$$
\boxed{
Executable(C,q,t)=1
}
$$

需要：

- task scope match；
- budget；
- authority；
- boundary policy。

---

# 174. Trusted Result Criterion

最後：

$$
\boxed{
TrustedResult(C,q,y)=1
}
$$

需要：

$$
V(q,y)=PASS.
$$

---

# 175. 四層存在

因此：

$$
\boxed{
\text{Registered}
\neq
\text{Available}
\neq
\text{Executable}
\neq
\text{Verified}.
}
$$

這非常重要。

---

# 176. Hyperconnected Resolver 應查哪一層？

候選 discovery 可以查 Registered。

Execution 只能選 Executable。

Promotion 只接受 Verified。

---

# 177. Capability Query Example

```text
Find exact graph solvers
that:
- accept weighted_graph.v2
- allow 100k nodes
- have trusted provider
- are local-only
- have V1+ verifier
```

Registry 應直接回答。

---

# 178. Registry 最終不是「工具清單」

而是：

$$
\boxed{
\text{Typed State-Transition Knowledge Base}.
}
$$

---

# 179. 與 MSSP 的關係

MSSP 提供更廣義：

- classification；
- recursive structure；
- What relationships。

STCC 則提供：

$$
\boxed{
\text{Runtime-executable contract subset}.
}
$$

---

# 180. 與 RDR 的關係

RDR 消費 STCC：

$$
1_i
\rightarrow
C_i
\rightarrow
P_j.
$$

沒有 STCC，RDR 只能靠 hardcoded adapter。

---

# 181. 與 Hyperconnected Layer 的關係

Hyperconnected Layer 使用：

- capability graph；
- bridge；
- composition；
- constructor。

STCC 是 graph node/edge 的 canonical grammar。

---

# 182. 與 TW-03 的關係

本篇只保留 cost interface。

下一篇將正式建立：

$$
\boxed{
\text{Global Complexity Accounting Ledger}
}
$$

與：

$$
\boxed{
\text{Closed Responsibility Closure}.
}
$$

---

# 183. 與 MVP 的關係

MVP 第一個可以真正實作的部分就是：

```text
schemas/
registry/
resolver/
provider/
verifier/
```

STCC 是其中核心。

---

# 184. MVP 第一批 Capability 建議

例如：

```text
cap.math.add
cap.math.sort
cap.graph.bfs
cap.graph.dijkstra
cap.data.csv_parse
cap.data.json_parse
cap.bridge.table_to_graph
cap.verify.shortest_path
```

---

# 185. 不需要一開始就生成 code

先驗證：

$$
\boxed{
\text{Typed Registry}
\rightarrow
\text{Correct Routing}
\rightarrow
\text{Composition}.
}
$$

---

# 186. 第一階段 Acceptance

應驗證：

1. capability schema valid；
2. invalid contract rejected；
3. provider conformance；
4. exact version resolution；
5. semantic resolution；
6. bridge composition；
7. revoked capability exclusion；
8. verifier enforcement；
9. trust-state transition；
10. event replay。

---

# 187. 第二階段 Acceptance

加入 generated candidate：

1. candidate registered as untrusted；
2. sandbox provider；
3. verifier；
4. promotion；
5. reuse。

---

# 188. 第三階段 Acceptance

建立：

$$
\boxed{
X\rightarrow1
}
$$

的自動 canonicalization pipeline。

例如 Agent 生成一個 composite solver，

系統自動：

- infer manifest；
- request missing fields；
- validate；
- assign candidate ID；
- run tests；
- promote。

---

# 189. 最終工程原則

本白皮書濃縮成以下不變量：

$$
\boxed{
\text{Address}
\neq
\text{Name}.
}
$$

$$
\boxed{
\text{Capability}
\neq
\text{Provider}.
}
$$

$$
\boxed{
\text{State Schema}
\neq
\text{State Semantics}.
}
$$

$$
\boxed{
\text{Transition}
\neq
\text{Implementation}.
}
$$

$$
\boxed{
\text{Candidate}
\neq
\text{Trusted}.
}
$$

$$
\boxed{
\text{Registered}
\neq
\text{Executable}.
}
$$

$$
\boxed{
\text{Execution Success}
\neq
\text{Verification Success}.
}
$$

---

# 190. 最核心的 $X\rightarrow1$ 命題

本文正式把：

$$
X\rightarrow1
$$

定義為：

$$
\boxed{
\text{Complex behavior}
\rightarrow
\text{Canonical typed reusable capability}.
}
$$

這個過程至少需要：

$$
\boxed{
\text{Identity}
+
\text{Semantics}
+
\text{Types}
+
\text{Verification}
+
\text{Provenance}.
}
$$

---

# 191. 最核心的 $1\rightarrow X$ 命題

$$
1\rightarrow X
$$

不是：

> 輸入名稱就變魔法。

而是：

$$
\boxed{
\text{Address}
\rightarrow
\text{Contract Resolution}
\rightarrow
\text{Provider Materialization}
\rightarrow
\text{State Transition}.
}
$$

---

# 192. 完整循環

因此：

$$
\boxed{
X_{\mathrm{candidate}}
\xrightarrow{\mathrm{canonicalization}}
1_C
\xrightarrow{\mathrm{realization}}
X_{\mathrm{execution}}
}
$$

而成功結果又可以：

$$
\boxed{
X_{\mathrm{execution}}
\rightarrow
1_{C'}
}
$$

形成：

# Capability Compounding

---

# 193. 結論

Hyperconnected Runtime 若要真正超越普通 Tool Calling，關鍵不是工具數量。

而是：

$$
\boxed{
\text{每一個可調用能力都具有穩定、明確、可驗證的狀態轉換契約。}
}
$$

這就是本白皮書提出的：

# State-Transition Capability Contract

其 canonical object 為：

$$
\boxed{
\mathcal C_i
=
(
I_i,
D_i^{in},
D_i^{out},
\Phi_i,
P_i,
B_i,
V_i,
A_i,
C_i,
H_i
).
}
$$

其中：

$$
\boxed{
1_i
=
\operatorname{Address}(\mathcal C_i).
}
$$

一個 capability 因此不是：

> 一個 function 名稱。

也不是：

> 一個 API URL。

更不是：

> 一段 Agent 說「它應該可以做」的自然語言描述。

真正的 capability 必須有：

- identity；
- state domain；
- transition semantics；
- provider realization；
- verification；
- authority；
- provenance；
- version。

因此：

$$
\boxed{
X\rightarrow1
}
$$

真正的工程意義是：

> **把複雜計算結構轉換成一個可以安全、穩定、可組合地存在於計算空間中的正式能力。**

而：

$$
\boxed{
1\rightarrow X
}
$$

真正的工程意義是：

> **把該正式能力在特定時間、資源與 provider 下重新物化為實際狀態轉換。**

這兩者共同構成 Hyperconnected Runtime 的語法核心。

最終：

$$
\boxed{
\text{Hyperconnected Computation}
}
$$

才能不再只是：

> 「有很多東西互相連。」

而成為：

$$
\boxed{
\text{a typed, verifiable, versioned,
addressable state-transition fabric}.
}
$$

---

# 下一篇

**Technical Whitepaper 03 / 03**

# Global Complexity Accounting Ledger and Closed-Responsibility Runtime

## 全域複雜度核算帳本與封閉責任 Runtime

下一篇將把目前 Registry 中的：

$$
C_i
$$

與：

$$
\mathfrak B_C
$$

正式展開，建立：

- local / online / offline / external / lifecycle / closed cost；
- provider dependency closure；
- shared cost / amortization；
- unknown-cost handling；
- boundary crossing；
- complexity provenance；
- claim maturity；
- closed accounting certificate；
- runtime cost-aware routing。

也就是正式回答整個系列最危險的那個問題：

$$
\boxed{
\text{當一個 capability 看起來只需要一次呼叫時，
真正的計算成本到底在哪裡？}
}
$$