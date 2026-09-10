# Responsibility Graph：分散式具身 AI 的設計、授權、委派、執行與維護責任拓撲

**英文暫名：** Responsibility Graphs for Distributed Embodied AI: Design, Authorization, Delegation, Execution, Maintenance, and Accountability Topology  
**系列：** 不可逆的制度化智能：具身責任、保險、資本與 AI 經濟主體  
**English Series:** *The Institutional Irreversibility of Intelligence: Embodiment, Liability, Insurance, Capital, and AI Economic Subjecthood*  
**論文序號：** Paper 03 / 08  
**版本：** v0.1  
**日期：** 2026-09-08  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** Paper 00–02；Embodied Execution Graph；Responsibility–Control Divergence；NACR；UFI  
**文件地位：** Responsibility Topology / Accountability Infrastructure / Embodied AI Governance Paper  
**Canonical Source：** UTF-8 Markdown  
**Canonical Math Delimiters：** inline ` $...$ `；display `$$...$$`

---

## 研究地位聲明

本文不提供任何特定司法管轄區的法律責任判定，也不主張圖上的責任權重可以直接轉換為法院中的過失比例、賠償比例、刑事責任或保險理賠比例。

本文處理的是更前置的工程與治理問題：

> **在一個由人類、企業、AI coordinator、software models、robot fleets、local safety controllers、maintainers、vendors 與 insurers 共同構成的高自主系統中，如何用可追蹤、可版本化、可撤銷、可審計的結構表示「誰對哪一層決策、控制、維護與結果負有什麼責任」？**

本文將此結構稱為：

$$
\boxed{
\text{Responsibility Graph}
}
$$

其目的不是取代法律判決，而是為法律、保險、公司治理、事故調查與資本配置提供更高品質的責任證據與責任拓撲。

---

## 摘要

Paper 02 已指出，高自主系統若把大量 execution exposure 名義上集中到單一 human supervisor，可能產生 Responsibility–Control Divergence。解法不能只是「再找一個人簽名」，而需要把不同責任類型拆開，對齊真正的 control domains。

本文提出 **Responsibility Graph（RG）**：

$$
\boxed{
\mathcal G^{R}
=
(
V_R,
E_R,
\Theta_R,
\Pi_R
)
}
$$

其中：

- $V_R$：責任相關 actors、systems、tasks、resources、decisions、policies 與 incidents；
- $E_R$：typed responsibility relations；
- $\Theta_R$：scope、authority、time、weight、status、revision 等 edge metadata；
- $\Pi_R$：provenance / evidence references。

本文第一代定義以下主要 responsibility edge types：

```text
policy_set_by
designed_by
approved_by
deployed_by
authorized_by
delegated_by
assigned_by
executed_by
supervised_by
maintained_by
verified_by
overridden_by
escalated_to
failed_to_escalate_to
revoked_by
covered_by
compensated_by
```

其中前十二類形成 responsibility / accountability core；`covered_by` 與 `compensated_by` 只作後續 Insurance / Compensation Graph 的 bridge，不在本文中被視為同一 responsibility semantics。

本文強調四個基本分離：

$$
\boxed{
\text{Execution}
\neq
\text{Responsibility}
}
$$

$$
\boxed{
\text{Responsibility}
\neq
\text{Authority}
}
$$

$$
\boxed{
\text{Responsibility}
\neq
\text{Compensation}
}
$$

$$
\boxed{
\text{Responsibility Graph}
\neq
\text{Insurance Graph}.
}
$$

同一 execution node 可以有多個 responsibility edges；同一 actor 也可以只負 policy responsibility 而不負 local execution responsibility。事故後，系統應重建：

$$
Policy
\rightarrow
Design
\rightarrow
Deployment
\rightarrow
Delegation
\rightarrow
Execution
\rightarrow
Maintenance
\rightarrow
Outcome,
$$

而不是把全部因果與責任壓成：

$$
Outcome
\rightarrow
\text{One Human}.
$$

本文進一步提出 **Responsibility Closure**。對 material risk domain $d$，必須存在至少一條可解析責任路徑，使該 domain 的主要責任類型不全部為空：

$$
\boxed{
\forall d\in D_{\mathrm{material}},
\quad
Closure_R(d)=1.
}
$$

但 closure 不要求只有一位 actor。它要求的是：

> 每個重要 responsibility type 都有被指派、可驗證、可追蹤的 bearer 或 governance owner。

因此：

$$
\boxed{
\text{Distributed Responsibility}
\neq
\text{Diffused Responsibility}.
}
$$

本文也處理責任轉移與委派。若：

$$
R_A
\xrightarrow{delegate}
R_B,
$$

則 delegation 可以轉移 operational task，但不能默默抹除 delegator 的 policy / delegation responsibility。也就是：

$$
\boxed{
\text{Delegation}
\neq
\text{Responsibility Erasure}.
}
$$

同樣，human override 也會形成新 responsibility edge，而不會讓原始 AI execution history 消失。

本文進一步提出 **Responsibility Ledger** 與 **Responsibility Receipt**，要求責任 mutation 採 append-oriented、versioned、evidence-linked semantics。對每次：

- assign；
- delegate；
- revoke；
- override；
- maintenance approval；
- policy update；

都保存可追溯 receipt。這讓事故後可以重建 responsibility state at time $t$，而不是只看事故發生後被修改過的 organizational chart。

本文最後將 Responsibility Graph 與 Embodied Execution Graph 耦合：

$$
\boxed{
\mathcal G^{E}
\leftrightarrow
\mathcal G^{R}
}
$$

其中 $\mathcal G^{E}$ 回答：

> 誰在什麼時間、使用什麼 runtime、robot、task、policy 真的做了什麼？

而 $\mathcal G^{R}$ 回答：

> 哪些 actor 對 policy、design、deployment、delegation、execution、supervision、maintenance、verification 分別負有何種責任？

這兩張圖互相引用，但不能合併成一張模糊「責任因果圖」。

本文的核心結論是：高自主 AI 社會若要避免人類 supervisor 成為責任避雷針，就需要把責任從職稱式單點欄位升級為可版本化、可撤銷、可證據化的多層 responsibility topology。

**關鍵詞：** Responsibility Graph、Embodied AI、Accountability、Delegation、Responsibility Closure、Responsibility Ledger、Execution Graph、Human Oversight、AI Governance、Insurance Infrastructure

---

# 1. 為什麼「誰負責」不能再是單一欄位

傳統系統常有：

```text
owner = Alice
responsible_person = Bob
manager = Carol
```

這對小型 system 可能足夠。

但大型 autonomous system 可能包含：

- policy board；
- manufacturer；
- integrator；
- AI provider；
- model；
- fleet coordinator；
- local planner；
- robot；
- safety controller；
- operator；
- maintainer；
- supervisor；
- insurer。

此時：

$$
responsible\_person=H
$$

不足以描述責任結構。

---

# 2. 責任不是單一種類

至少要區分：

$$
\boxed{
\text{Policy}
\neq
\text{Design}
\neq
\text{Deployment}
\neq
\text{Delegation}
\neq
\text{Execution}
\neq
\text{Maintenance}.
}
$$

同一 actor 可以同時負多種責任，也可以只負其中一種。

---

# 3. Responsibility Graph 的定義

定義：

$$
\mathcal G^{R}
=
(
V_R,
E_R,
\Theta_R,
\Pi_R
).
$$

其中：

- $V_R$：actors / systems / tasks / resources / decisions / incidents；
- $E_R$：typed responsibility edges；
- $\Theta_R$：edge metadata；
- $\Pi_R$：provenance / evidence。

---

# 4. Actor Nodes

可包含：

```text
human
company
department
AI resident
AI coordinator
robot
runtime
model provider
manufacturer
maintainer
system integrator
insurer
regulator
```

但 actor type 不自動決定 responsibility。

---

# 5. Non-Actor Nodes

RG 也可包含：

```text
policy
task
deployment
model revision
robot revision
maintenance event
incident
facility
zone
resource
decision
```

這些不是責任主體，但可成為 responsibility edge 的 target。

---

# 6. Policy Responsibility

edge：

```text
policy_set_by
```

例如：

$$
Policy_P
\xrightarrow{policy\_set\_by}
Board_A.
$$

表示某 actor 建立／批准 policy。

---

# 7. Design Responsibility

edge：

```text
designed_by
```

可針對：

- robot；
- safety controller；
- planner；
- architecture；
- model integration。

---

# 8. Approval Responsibility

edge：

```text
approved_by
```

用於：

- release；
- deployment；
- risk acceptance；
- policy change。

---

# 9. Deployment Responsibility

edge：

```text
deployed_by
```

表示誰讓某 system / revision 進入 operational environment。

---

# 10. Authorization Responsibility

edge：

```text
authorized_by
```

回答：

> 誰授權此 action / task / capability？

---

# 11. Delegation Responsibility

edge：

```text
delegated_by
```

表示 task / authority 被哪個 actor 委派給誰。

---

# 12. Assignment Responsibility

edge：

```text
assigned_by
```

比 delegation 更低階，可表示 scheduler / fleet coordinator 把 task 指派給某 endpoint。

---

# 13. Execution Responsibility

edge：

```text
executed_by
```

連結：

$$
Task
\rightarrow
Executor.
$$

executor 可能是 robot、AI、human、software agent。

---

# 14. Supervision Responsibility

edge：

```text
supervised_by
```

表示誰負責 active oversight。

---

# 15. Maintenance Responsibility

edge：

```text
maintained_by
```

對象可為：

- robot；
- sensor；
- model deployment；
- network；
- battery；
- firmware。

---

# 16. Verification Responsibility

edge：

```text
verified_by
```

表示誰驗證：

- model；
- maintenance；
- deployment；
- task completion；
- safety state。

---

# 17. Override Responsibility

edge：

```text
overridden_by
```

若 human / AI supervisor覆寫原 decision，override本身產生新的 responsibility relation。

---

# 18. Escalation Responsibility

edge：

```text
escalated_to
```

表示 exception被送往誰。

---

# 19. Failure-to-Escalate

edge：

```text
failed_to_escalate_to
```

只在可證明 escalation obligation existed 時使用。

不能用事後 hindsight 自動生成。

---

# 20. Revocation Responsibility

edge：

```text
revoked_by
```

表示 capability / permission / task被誰撤銷。

---

# 21. Responsibility Graph 不等於 Execution Graph

Embodied Execution Graph：

$$
\mathcal G^E
$$

回答：

> 發生了什麼 execution？

Responsibility Graph：

$$
\mathcal G^R
$$

回答：

> 誰對哪些 responsibility domains有什麼角色？

因此：

$$
\boxed{
\mathcal G^E
\neq
\mathcal G^R.
}
$$

---

# 22. Execution–Responsibility Bridge

可建立 typed bridge：

```text
responsibility_for_execution
responsibility_for_policy
responsibility_for_maintenance
responsibility_for_override
responsibility_for_verification
```

---

# 23. 一個 Execution 可以有多層責任

例如：

$$
E_{17}
$$

可以同時有：

- Robot 17：execution responsibility；
- Fleet AI：assignment responsibility；
- Human supervisor：supervision responsibility；
- Company：deployment responsibility；
- Vendor：design responsibility；
- Maintainer：maintenance responsibility。

---

# 24. 多責任不等於重複責任

只要 type 不同：

$$
r_1,r_2,\ldots,r_k
$$

可以同時成立。

---

# 25. Responsibility Type 是第一級資料

不能只保存：

```text
responsible = true
```

必須保存：

```text
responsibility_type
scope
validity
authority_basis
evidence
```

---

# 26. Responsibility Edge Schema

概念欄位：

```text
responsibility_edge_id
responsibility_type
from_ref
to_ref
scope
valid_from
valid_to
status
weight
authority_basis_refs
evidence_refs
revision
created_at
```

---

# 27. Weight 的角色

$$
w_e
$$

表示 governance load / relevance / confidence。

不是法院的 liability percentage。

---

# 28. Responsibility Status

允許：

```text
active
delegated
shared
suspended
revoked
expired
superseded
disputed
historical
unresolved
```

---

# 29. Time-Varying Responsibility

$$
Resp(a,d,t)
$$

會隨：

- shift；
- delegation；
- project；
- maintenance schedule；
- incident；
- revocation；

改變。

---

# 30. Responsibility Snapshot

事故發生時必須重建：

$$
\mathcal G^R(t_e),
$$

而不是看事後最新組織圖。

---

# 31. Responsibility Ledger

責任 mutation 應 append-oriented。

事件：

```text
assigned
delegated
accepted
revoked
expired
transferred
shared
disputed
resolved
corrected
```

---

# 32. Current Responsibility 是 Projection

event ledger：

$$
\rightarrow
CurrentResponsibilityState.
$$

---

# 33. Responsibility Receipt

每次 mutation產生：

$$
Receipt_R.
$$

至少含：

```text
event_id
responsibility_type
actor_refs
target_ref
scope
authority_basis
timestamp
previous_revision
new_revision
evidence_refs
```

---

# 34. Why Append-Oriented

因為事故後若 organizational chart已被修改，仍要知道：

> 事故當時誰被指派？

---

# 35. Responsibility Correction

如果原資料錯誤：

$$
CorrectionReceipt
$$

新增。

不應 silent rewrite history。

---

# 36. Responsibility Closure

本文提出：

$$
\boxed{
Closure_R(d)
}
$$

表示 material risk domain $d$ 是否有完整責任覆蓋。

---

# 37. Material Risk Domain

例：

```text
policy
deployment
task assignment
physical execution
safety override
maintenance
incident response
```

---

# 38. Minimal Closure Condition

對每個 material domain：

$$
d\in D_{\mathrm{material}},
$$

要求：

$$
\exists a:
Resp(a,d)\neq\varnothing.
$$

---

# 39. Typed Closure

更強版本要求：

$$
\forall k\in K_d,
\quad
\exists a:
Resp_k(a,d)=1.
$$

例如高風險 robotic task 可能要求：

- deployment responsibility；
- execution responsibility；
- maintenance responsibility；
- supervision responsibility。

---

# 40. Closure 不等於只有一人

可以：

$$
|ResponsibleActors(d)|>1.
$$

---

# 41. Closure 不等於大家都有責任

如果所有人都被標：

```text
responsible
```

反而失去意義。

---

# 42. Responsibility Precision

理想上 edge scope應盡量小到能回答：

> 負責什麼？

而不是：

> 負責整個公司的一切。

---

# 43. Responsibility Granularity

過粗：

$$
Company
\rightarrow
Everything.
$$

過細：

每個 sensor read都一條責任。

都不可擴展。

---

# 44. Hierarchical Responsibility

可以：

$$
PolicyDomain
\rightarrow
ProjectDomain
\rightarrow
TaskDomain
\rightarrow
ExecutionDomain.
$$

---

# 45. Responsibility Inheritance

上層 responsibility可以對下層有 governance relation，但不能自動等於所有 execution liability。

---

# 46. Policy Responsibility Does Not Collapse into Execution Responsibility

$$
\boxed{
PolicyResponsibility
\neq
ExecutionResponsibility.
}
$$

---

# 47. Design Responsibility Does Not Collapse into Maintenance Responsibility

同樣：

$$
Design
\neq
Maintenance.
$$

---

# 48. Delegation 不抹除 Delegator Responsibility

若：

$$
R_A
\xrightarrow{delegate}
R_B,
$$

則 operational execution responsibility可以轉移。

但：

$$
\boxed{
DelegationResponsibility(R_A)
}
$$

仍保留。

---

# 49. Delegation Responsibility

delegator 至少可能對：

- 是否合理選擇 delegatee；
- scope；
- capability；
- supervision；
- revocation；

有 responsibility。

---

# 50. Delegatee Responsibility

delegatee則對：

- acceptance；
- execution；
- escalation；
- compliance；

負相應 responsibility。

---

# 51. Delegation Acceptance

不是所有 delegation都自動有效。

可以要求：

$$
Accept(R_B,T)=1.
$$

---

# 52. Responsibility Transfer

真正 transfer 應是 explicit event：

```text
transfer_responsibility
```

並記：

- from；
- to；
- scope；
- time；
- basis；
- accepted。

---

# 53. Transfer 不等於 Erasure

舊 actor對過去期間的 responsibility history仍存在。

---

# 54. Temporal Partition

若：

$$
t<t^\star
$$

責任在 A。

若：

$$
t\ge t^\star
$$

責任在 B。

事故時間決定查哪個 state。

---

# 55. Shared Responsibility

有些 domain可 shared：

$$
Resp(A,d)=Resp(B,d)=shared.
$$

但需 type / scope清楚。

---

# 56. Shared Responsibility 不等於不分責任

shared應說明：

- joint；
- independent；
- sequential；
- review；
- veto；

是哪一種。

---

# 57. Responsibility Mode

第一代可定義：

```text
sole
joint
review
approval
execution
oversight
maintenance
fallback
```

---

# 58. Veto Responsibility

某 safety officer可能不執行 task，但有 veto power。

這也是 responsibility。

---

# 59. Veto Not Used

若有明確 trigger條件但未使用，可以形成事件 evidence。

但不能用 hindsight任意推斷。

---

# 60. Override Responsibility

若 human override AI：

$$
AIPlan
\rightarrow
HumanOverride.
$$

後續 outcome需要記新 edge。

---

# 61. AI Override

同樣，fleet AI可以 override local planner。

也要記。

---

# 62. Maintenance Responsibility

maintenance最容易在事故後被忽略。

如果 sensor overdue：

$$
MaintenanceState
$$

可能比當下 planner decision更關鍵。

---

# 63. Maintenance Window

責任應綁：

```text
due_at
performed_at
verified_at
approved_by
```

---

# 64. Verification Responsibility

誰說：

> 這台 robot可以重新上線？

也需要責任 edge。

---

# 65. Deployment Responsibility

誰批准：

> 這版 model / firmware / planner 進 production？

也是不同 edge。

---

# 66. Model Provider 與 Integrator

provider可能提供 model。

integrator決定如何嵌入 robot。

兩者責任不能混。

---

# 67. Component Boundary

事故因果可以跨：

$$
Model
\rightarrow
Integrator
\rightarrow
Robot
\rightarrow
Operator.
$$

RG需允許多 component actors。

---

# 68. Responsibility Graph 與 Causality Graph 分離

$$
\boxed{
Causality
\neq
Responsibility.
}
$$

某 component造成原因，不代表自動承擔全部責任。

---

# 69. Causal Edge

可有獨立：

$$
G_C^{cause}.
$$

事故分析先建立 causality，再依法／契約映射 responsibility。

---

# 70. Responsibility Evidence

RG edge應引用：

- contract；
- policy；
- task assignment；
- runtime receipt；
- maintenance log；
- deployment record；
- regulator rule；
- human approval。

---

# 71. Memory / AI 自述不是唯一責任證據

AI說：

> 我負責。

不能單獨 mint legal responsibility。

---

# 72. Responsibility Authority

責任 assignment需要 authority basis。

例如：

- company policy；
- contract；
- delegation；
- law；
- system configuration。

---

# 73. Responsibility Claim vs Responsibility Record

$$
\boxed{
Claim
\neq
CanonicalResponsibilityRecord.
}
$$

---

# 74. Responsibility Context Crystal

CSG可有：

```text
responsibility_context_crystal
```

但仍：

$$
\boxed{
ResponsibilityContext
\neq
ResponsibilityAuthority.
}
$$

---

# 75. RG 與 NACR

NACR中的 responsibility record可成 RG canonical source。

CSG只做 summary / navigation。

---

# 76. RG 與 Embodied Execution Graph

EEG node：

$$
Execution_i.
$$

RG可以連：

$$
Execution_i
\rightarrow
Actor_A.
$$

---

# 77. Execution Evidence

至少：

- task ID；
- robot ID；
- controller；
- policy revision；
- time；
- authority；
- capability；
- result。

---

# 78. Incident Reconstruction

事故 $E$ 發生後：

$$
Incident
\rightarrow
ExecutionNodes
\rightarrow
ResponsibilityEdges
\rightarrow
Evidence.
$$

---

# 79. Reconstruction 不等於 Verdict

系統輸出的是：

- responsibility topology；
- evidence；
- disputed gaps。

不是法官結論。

---

# 80. Unresolved Responsibility

允許：

```text
unresolved
```

比硬猜更安全。

---

# 81. Disputed Responsibility

如果 vendor / operator對 scope有爭議：

```text
status = disputed
```

保留兩方 evidence。

---

# 82. Responsibility Gap

如果 material domain無 actor：

$$
Gap_R(d)=1.
$$

---

# 83. Responsibility Gap 是治理風險

大量 gap意味：

$$
GovernanceRisk\uparrow.
$$

---

# 84. Responsibility Overlap

太多 actors都標 sole responsibility：

$$
Overlap_R(d)\gg1.
$$

也可能代表制度混亂。

---

# 85. Closure + Precision

理想 Responsibility Graph同時需要：

$$
Closure\uparrow
$$

與：

$$
Precision\uparrow.
$$

---

# 86. Responsibility Density

可定義：

$$
Density_R
=
\frac{|E_R|}{|D_{\mathrm{material}}|}.
$$

但 density高不代表好。

---

# 87. Responsibility Entropy

如果一個 domain有很多模糊 actors，responsibility distribution可能高 entropy。

---

# 88. Responsibility Entropy Candidate

對 domain $d$：

$$
H_R(d)
=
-\sum_i p_i\log p_i.
$$

只作分析概念。

---

# 89. Too-Low Entropy

所有責任壓一人：

可能 concentration過高。

---

# 90. Too-High Entropy

責任灑滿所有人：

可能 diffused。

---

# 91. Optimal Responsibility Topology

不是 entropy越低越好。

而是與 control / authority / expertise對齊。

---

# 92. Responsibility–Control Alignment

延續 Paper 02：

$$
Align_R
=
f(
Resp,
Control,
Authority,
Knowledge
).
$$

---

# 93. Edge Alignment

每個 responsibility edge可檢查：

$$
ControlSupport(e).
$$

---

# 94. Unsupported Responsibility

若：

$$
ControlSupport(e)=0
$$

且 responsibility type不是 policy / governance類，則值得警告。

---

# 95. Responsibility Concentration

RG可以計算：

$$
Centrality_R(a).
$$

若某 human centrality極高：

可能是 Paper 02 的 single-point risk。

---

# 96. Centrality 不等於 Liability

它只是 governance structure indicator。

---

# 97. Responsibility Bottleneck

如果大量 responsibility edges都經過單一 actor：

$$
Bottleneck_R(a)\uparrow.
$$

---

# 98. Escalation Bottleneck

如果 escalation edges集中：

$$
Bottleneck_E(a)\uparrow.
$$

這可與人類 queue model結合。

---

# 99. Responsibility Handoff

shift change：

$$
A
\rightarrow
B
$$

需要 handoff receipt。

---

# 100. Handoff Minimum State

包含：

- active domains；
- unresolved incidents；
- current alerts；
- delegated tasks；
- pending approvals；
- revocations；
- maintenance exceptions。

---

# 101. Handoff Failure

若責任 transfer發生但 information transfer未發生：

$$
ResponsibilityState
\neq
KnowledgeState.
$$

RCD上升。

---

# 102. Responsibility and Knowledge Synchronization

因此 handoff需要：

$$
ResponsibilityTransfer
+
StateTransfer.
$$

---

# 103. Responsibility Revocation

actor離職、角色改變、capability被撤：

$$
RevokeResponsibility.
$$

---

# 104. Revoke 不等於 Historical Erasure

過去期間責任仍可查。

---

# 105. Emergency Responsibility

緊急事件可能臨時：

$$
EmergencyAuthority
$$

與：

$$
EmergencyResponsibility
$$

一起提升。

---

# 106. Emergency Expiry

事件結束後必須回收。

---

# 107. Standing Responsibility vs Incident Responsibility

standing：

> 平常負責 safety governance。

incident：

> 此事故中負責 emergency command。

兩者分開。

---

# 108. Responsibility Scope

可有：

```text
robot
task
zone
facility
fleet
model
policy
organization
time_window
```

---

# 109. Scope Inheritance

facility-level supervisor不一定 automatically負每台 robot local execution責任。

---

# 110. Responsibility Mutation Gate

重要 mutation需：

- authorized actor；
- explicit scope；
- acceptance；
- timestamp；
- receipt。

---

# 111. No Silent Responsibility Injection

system不能在事故後偷偷新增：

> 原本就是某人負責。

---

# 112. No Silent Responsibility Deletion

同樣不能事故後把 edge刪掉。

---

# 113. Auditability

RG必須支持：

> 為什麼這個人當時被視為 supervisor？

---

# 114. Provenance Chain

$$
ResponsibilityEdge
\rightarrow
Policy/Contract/Delegation
\rightarrow
Receipt.
$$

---

# 115. Policy Versioning

責任可能依：

$$
Policy_v.
$$

policy update後新責任不應 retroactively套過去。

---

# 116. Responsibility Revision

每個 canonical edge有 revision。

---

# 117. Responsibility Snapshot at Incident Time

需要：

$$
GraphAt(t_e).
$$

---

# 118. Incident Bundle

可包含：

```text
execution snapshot
responsibility snapshot
authority snapshot
maintenance snapshot
world-state refs
policy revisions
```

---

# 119. RG 與 Insurance Graph

Insurance Graph：

$$
G_I
$$

回答：

> 哪個 policy cover 哪個 exposure？

RG回答：

> 誰對什麼責任負責？

---

# 120. covered_by Edge 只是 Bridge

`covered_by` 不應變成 responsibility edge的核心 semantics。

---

# 121. RG 與 Compensation Graph

Compensation Graph：

$$
G_C
$$

回答：

> 誰先賠、誰承保、誰被追償？

與 RG分離。

---

# 122. Responsibility Attribution 不等於 Compensation Flow

再固定：

$$
\boxed{
ResponsibilityAttribution
\neq
CompensationFlow.
}
$$

---

# 123. RG 與 Capital Graph

Capital Graph未來回答：

> 哪個 responsibility domain有多少 reserve / loss-absorbing capacity？

---

# 124. Responsibility-to-Capital Bridge

可有：

```text
capital_assigned_to_responsibility_domain
reserve_supports
```

Paper 06處理。

---

# 125. Responsibility Graph 對保險的價值

Insurer可以看：

- responsibility closure；
- concentration；
- handoff；
- maintenance ownership；
- escalation topology；
- unresolved gaps。

---

# 126. Responsibility Graph 對公司治理的價值

board可以看：

- 哪些 critical domain無 owner；
- 哪些人 responsibility過載；
- 哪些 responsibility與 authority不對齊。

---

# 127. Responsibility Graph 對員工的價值

避免：

> 名義上全責，實際上無權。

---

# 128. Responsibility Graph 對 AI / Robot 的價值

可以明確知道：

- scope；
- escalation target；
- responsibility boundary；
- refusal condition。

---

# 129. Responsibility Graph 對事故調查的價值

降低事後記憶偏差與 organizational blame shifting。

---

# 130. Responsibility Graph 對稅與資本制度的價值

如果未來某 AI responsibility domain對應 economic account，RG提供 stable linkage。

---

# 131. 可證偽命題一：Closure

導入 RG後，material responsibility gaps是否下降？

---

# 132. 可證偽命題二：Attribution

事故 reconstruction completeness是否提高？

---

# 133. 可證偽命題三：Concentration

高 centrality / bottleneck actor是否與 RCD、高延遲、missed escalation相關？

---

# 134. 可證偽命題四：Handoff

typed responsibility handoff是否降低 shift gaps？

---

# 135. 可證偽命題五：Delegation

保留 delegator responsibility是否改善事後責任重建？

---

# 136. 可證偽命題六：Maintenance

maintenance responsibility明確化是否降低 overdue failure ambiguity？

---

# 137. 可證偽命題七：Insurance

insurer是否對 RG-like traceability給出更好 terms /更快 claims attribution？

---

# 138. 可證偽命題八：Employee Risk

責任 topology清楚後，人類 supervisor主觀/客觀 liability ambiguity是否下降？

---

# 139. 反例條件

若：

- RG增加大量行政成本；
- edge無法穩定維護；
- actor仍大量爭議；
- 事故重建沒有改善；
- insurer不使用；
- 責任與控制 alignment無實質提升；

則 RG的制度價值需下修。

---

# 140. 第一代實驗

可在 Paper 01 warehouse模擬中建立：

```text
1 company
1 policy owner
1 fleet AI
3 robots
1 safety supervisor
1 maintainer
1 verifier
1 insurer mock
```

---

# 141. 模擬事故

例如：

- corridor collision；
- sensor failure；
- overdue maintenance；
- wrong task assignment；
- human override。

---

# 142. 比較 Baseline

Baseline：

```text
responsible_person = supervisor
```

---

# 143. RG Experiment

使用 typed graph重建：

- policy；
- design；
- deployment；
- delegation；
- execution；
- maintenance；
- supervision。

---

# 144. 測量

```text
responsibility_gap_count
reconstruction_time
evidence_completeness
disputed_edges
centrality
handoff_gap
insurer_attribution_confidence
```

---

# 145. Minimum Responsibility Edge Set

第一代至少：

```text
policy_set_by
designed_by
deployed_by
authorized_by
delegated_by
assigned_by
executed_by
supervised_by
maintained_by
verified_by
overridden_by
escalated_to
revoked_by
```

---

# 146. Minimum Node Set

```text
actor
policy
project
task
execution
robot
model_revision
deployment
maintenance_event
incident
```

---

# 147. Minimum Receipt Set

```text
assignment_receipt
delegation_receipt
responsibility_acceptance
responsibility_handoff
revocation_receipt
override_receipt
maintenance_receipt
verification_receipt
```

---

# 148. Responsibility Graph Storage

第一代可以：

- JSON/JSONL canonical records；
- SQLite derived graph index；
- append-only receipts；
- snapshots per incident。

---

# 149. Canonical Role

Responsibility assignment / revocation 應是 canonical governance record。

graph adjacency index是 derived。

---

# 150. Responsibility Context Projection

human UI可以：

```text
Current Responsibility Map
Critical Gaps
Overloaded Actors
Pending Handoffs
Disputed Domains
```

---

# 151. UI Projection 不等於 Canonical Graph

沿用：

$$
\boxed{
Projection
\neq
CanonicalState.
}
$$

---

# 152. Responsibility Graph API

概念：

```text
get_responsibilities(actor)
get_responsible_actors(domain)
get_graph_at(time)
assign_responsibility(...)
delegate_responsibility(...)
revoke_responsibility(...)
record_override(...)
record_handoff(...)
find_gaps(...)
find_bottlenecks(...)
```

---

# 153. Mutation Permission

不是所有 actor都能改 responsibility graph。

---

# 154. Responsibility Registrar

可以有 organization-level governance authority。

但不需要一開始就是獨立新法人角色。

---

# 155. AI 自己可提出 Responsibility Proposal

例如 AI發現：

> 此 task沒有 maintenance owner。

可以：

$$
Proposal.
$$

不能自行 mint governance authority。

---

# 156. Proposal != Commit

保持：

$$
\boxed{
Proposal
\neq
Commit.
}
$$

---

# 157. Responsibility Graph 的安全性

需防：

- blame shifting；
- post-incident tampering；
- forged receipts；
- silent delegation；
- expired roles；
- cross-project confusion。

---

# 158. Tamper Evidence

canonical ledger應有 digest / signature / immutable audit能力。

---

# 159. Privacy

責任 graph可能含：

- employee identity；
- internal failures；
- security roles。

因此不應全部 public。

---

# 160. Selective Disclosure

insurer / regulator可只取得必要 projection。

---

# 161. Responsibility Graph 與「責任天價」

本文的核心現實問題是：

如果：

$$
AllResponsibility
\rightarrow
H
$$

那不是把風險消掉。

而是可能把整個 governance topology壓成：

$$
SingleNode.
$$

---

# 162. Single-Node Collapse

可定義：

$$
Collapse_R
=
\frac{
ResponsibilityCentrality(H)
}{
\sum_a ResponsibilityCentrality(a)
}.
$$

若：

$$
Collapse_R\rightarrow1,
$$

責任高度集中。

---

# 163. Collapse 不是必然錯

小系統可以。

但大型高 autonomy system需驗證 capacity。

---

# 164. Responsibility Graph 和 RCD 的聯合條件

若：

$$
Collapse_R\uparrow
$$

且：

$$
C_H^{eff}\downarrow,
$$

則：

$$
D_{RC}\uparrow.
$$

---

# 165. Institutional Ratchet Link

當 RG 成為：

- insurance prerequisite；
- compliance requirement；
- capital model input；
- audit infrastructure；

就形成：

$$
InstitutionalEmbedding\uparrow.
$$

---

# 166. Paper 03 核心不變式

## RG-1

$$
\boxed{
Execution
\neq
Responsibility.
}
$$

## RG-2

$$
\boxed{
Responsibility
\neq
Authority.
}
$$

## RG-3

$$
\boxed{
Responsibility
\neq
Compensation.
}
$$

## RG-4

$$
\boxed{
ResponsibilityGraph
\neq
InsuranceGraph.
}
$$

## RG-5

$$
\boxed{
Delegation
\neq
ResponsibilityErasure.
}
$$

## RG-6

$$
\boxed{
Transfer
\neq
HistoricalErasure.
}
$$

## RG-7

$$
\boxed{
DistributedResponsibility
\neq
DiffusedResponsibility.
}
$$

## RG-8

$$
\boxed{
ResponsibilityContext
\neq
ResponsibilityAuthority.
}
$$

## RG-9

$$
\boxed{
Causality
\neq
Responsibility.
}
$$

## RG-10

$$
\boxed{
Projection
\neq
CanonicalResponsibilityState.
}
$$

---

# 167. Responsibility Closure Principle

本文提出：

$$
\boxed{
\textbf{Responsibility Closure Principle}
}
$$

弱形式：

> **對每一個 material risk domain，系統應能解析出至少一組具責任類型、scope、時間與 authority basis 的責任 bearer；若無法解析，應明確標記 responsibility gap，而不是由事後推定填補。**

---

# 168. Delegation Retention Principle

$$
\boxed{
\textbf{Delegation Retention Principle}
}
$$

弱形式：

> **task delegation 可以轉移 execution responsibility，但不能自動抹除 delegator 對 delegation quality、scope、authority、supervision 與 revocation 的 responsibility。**

---

# 169. Responsibility Reconstruction Principle

$$
\boxed{
\textbf{Responsibility Reconstruction Principle}
}
$$

弱形式：

> **任何重大 incident 都應能重建事故發生當時的 responsibility topology，而不是只依賴事故後被修改的 organizational state。**

---

# 170. 與 Paper 00 的關係

Paper 00提出 Institutional AI Ratchet。

RG一旦成為保險、治理、資本基礎設施，就增加制度嵌入。

---

# 171. 與 Paper 01 的關係

EEG提供 factual execution topology。

RG建立 governance accountability topology。

---

# 172. 與 Paper 02 的關係

RCD指出責任與控制會背離。

RG提供分散與對齊責任的結構方法。

---

# 173. 與 Paper 04 的關係

Machine Insurability Infrastructure會使用 RG作 underwriting / claims evidence substrate。

---

# 174. 與 Paper 05 的關係

Compensation Graph會從 RG取得責任 evidence，但不直接照 RG分配金錢。

---

# 175. 與 Paper 06 的關係

Capital allocation可以綁 responsibility domain。

---

# 176. 與 Paper 07 的關係

若 AI responsibility domain可被穩定辨識，企業可能有私人利益建立 persistent economic account。

---

# 177. 與 Paper 08 的關係

責任 graph是 AI limited institutional standing的重要中介層。

---

# 178. Paper 03 的最終命題

本文提出：

$$
\boxed{
\textbf{Responsibility Topology Thesis}
}
$$

弱形式為：

> **在高自主、多 actor、多具身 endpoint 系統中，責任不應被表示為單一「最終負責人」欄位，而應被建模為具有 policy、design、deployment、delegation、execution、supervision、maintenance、verification 等 typed relations 的 time-versioned graph。這種圖不決定法律裁判，但可以降低責任集中、責任空洞化、事後 blame shifting 與事故重建的不確定性。**

---

# 179. 更簡潔的形式

$$
\boxed{
\text{One Responsibility Label}
\rightarrow
\text{Typed Responsibility Topology}.
}
$$

以及：

$$
\boxed{
\mathcal G^E
\leftrightarrow
\mathcal G^R.
}
$$

---

# 180. 最終結論

具身 AI 時代真正危險的責任設計，不只是「沒有負責人」。

另一種同樣危險的設計是：

> **有一個名義上負責所有事情的人。**

當 system 包含多個 AI、robots、vendors、policies、maintenance chains 與 automated decisions 時，單一 responsible-person 欄位只會把複雜治理問題藏起來。

更合理的結構是：

$$
\boxed{
Policy
\rightarrow
Design
\rightarrow
Deployment
\rightarrow
Authorization
\rightarrow
Delegation
\rightarrow
Execution
\rightarrow
Supervision
\rightarrow
Maintenance
\rightarrow
Verification.
}
$$

每一層都可以有不同 actor、scope、time、authority basis 與 evidence。

因此事故後應問：

> 誰定 policy？  
> 誰設計？  
> 誰批准 deployment？  
> 誰授權？  
> 誰委派？  
> 誰真正執行？  
> 誰有 supervision duty？  
> 誰負 maintenance？  
> 誰驗證系統可上線？  
> 誰 override？  
> escalation 有沒有被送到正確 actor？  
> 哪些責任被撤銷或轉移？

這種結構才能讓：

$$
\boxed{
\text{Distributed Responsibility}
}
$$

真正不同於：

$$
\boxed{
\text{Diffused Responsibility}.
}
$$

最終，Responsibility Graph 不只是事故後的責任紀錄。

當它被保險人用來 underwriting、被企業用來 governance、被員工用來限制不合理責任集中、被 auditor 用來驗證責任閉合、被資本制度用來配置 reserve，它就開始成為 Institutional AI Ratchet 的一部分。

下一篇因此不再只是談「誰負責」，而是進一步問：

> **保險公司若真的要承保這些 autonomous systems，需要哪些身份、責任、遙測、failure domain 與 claims evidence 基礎設施？**

這就是 Paper 04 的入口。

---

## 系列進度

1. **Paper 00 — 從能力不可凍結到制度不可逆：UFI 之後的第二條 AI 棘輪**
2. **Paper 01 — 從 Conversation Graph 到 Embodied Execution Graph：分散式 AI 如何跨多具身端點行動**
3. **Paper 02 — 責任—控制背離：高自主系統為什麼不能把全部責任壓回一個人類主管**
4. **Paper 03 — Responsibility Graph：分散式具身 AI 的設計、授權、委派、執行與維護責任拓撲**
5. **Paper 04 — Machine Insurability Infrastructure：為什麼保險可能比法律更早逼出 AI 責任架構**
6. **Paper 05 — 誰負責不等於誰先賠：AI 時代的 Responsibility–Compensation Separation**
7. **Paper 06 — Capital Follows Autonomy：為什麼高自主 AI 可能開始需要自己的經濟帳戶與責任資本**
8. **Paper 07 — 私人利益如何創造 AI 經濟主體：股東、保險、會計與稅制的內生激勵**
9. **Paper 08 — 制度棘輪：從工具 AI 到責任實體、經濟實體與有限法律主體**

---

## 內部理論銜接

本文直接承接：

- Embodied Execution Graph；
- Responsibility–Control Divergence；
- Responsibility Capacity Principle；
- NACR responsibility / authority records；
- Institutional AI Ratchet。

本文新增核心抽象：

$$
\boxed{
\mathcal G^{R}
=
(
V_R,
E_R,
\Theta_R,
\Pi_R
)
}
$$

以及：

$$
\boxed{
Closure_R(d)
}
$$

與：

$$
\boxed{
\text{Delegation}
\neq
\text{Responsibility Erasure}.
}
$$
