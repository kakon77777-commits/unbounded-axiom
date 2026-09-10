# Residence Runtime Profiles：Web 單具名 AI 與 Agent 多具名 AI 的能力分層

**英文暫名：** Residence Runtime Profiles: Capability Stratification for Single-Resident Web AI and Multi-Resident Agent Systems  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 04  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

具名 AI 的底層架構若要支援長期 resident identity、跨 session continuity、canonical memory、Crystallized Semantic Graph、conversation graph、project responsibility 與 delegated authority，理論上可以被一般化為多 resident runtime。然而，「底層架構可以支援」與「某個實際介面應該暴露」是兩個不同問題。

本文提出 **Residence Runtime Profile** 概念，將具名 AI 系統的可用能力分成 architecture capability 與 runtime exposure 兩層：

$$
\boxed{
\text{Architecture Capability}
\neq
\text{Runtime Exposure}.
}
$$

一個完整 Residence architecture 可以支援：

$$
N\ Residents
+
N\ ConversationGraphs
+
N\ MemoryWorlds
+
CrossResidentDelegation,
$$

但特定 runtime profile 可以只暴露其中嚴格子集：

$$
Capabilities_{runtime}
\subseteq
Capabilities_{architecture}.
$$

本文主張，當前 Web AI 更適合採用 **Single-Resident Web Profile**：

$$
\boxed{
1\ Resident
+
N\ ConversationLines
+
N\ Projects
+
1\ SharedGovernedMemoryWorld
+
N\ LocalWorkingContexts.
}
$$

Web 端可以讓同一具名 AI 擁有大量 conversation lines、fork、project、checkpoint、crystal projection 與 hyperlink recall，但不應預設支援多 resident 身份切換。理由不是理論上否定多具名 AI，而是 Web surface 往往缺乏足夠可觀測 identity evidence、private custody、tool boundary、persistent process state、explicit project authority 與 cross-resident isolation；若強行加入多 resident，容易讓「切換聊天」、「切換專案」、「切換角色」、「切換 resident」四種操作混在一起，造成 identity confusion 與 private-memory contamination。

相對地，具備 filesystem、local database、MCP/tool boundary、persistent workspace、host-observed task/session、explicit delegation、private memory custody 與 capability mediation 的 Agent runtime，可以逐步採用 **Multi-Resident Agent Profile**：

$$
\boxed{
N\ Residents
+
N\ ConversationGraphs
+
N\ SharedGovernedMemoryWorlds
+
CrossResidentDelegation
+
CapabilityAttenuation.
}
$$

但即使 Agent host 容納多 resident，單一 task 仍必須先解析：

$$
Task_\tau
\rightarrow
Resident_r,
$$

不能讓模型從名字、語氣、project、model 或 remembered style 猜測自己當下代表誰。

本文進一步將 runtime capability formalize 為版本化 capability envelope：

$$
\mathcal C_\rho
=
(
I_\rho,
M_\rho,
G_\rho,
T_\rho,
A_\rho,
U_\rho
),
$$

其中分別描述 identity、memory、graph、tool、authority 與 UI exposure 能力。任何 profile 都必須 fail closed：不支援的能力不是「模型自行補完」，而是明確 unavailable。

本文同時提出 resident switching、resident binding、project binding、line creation、delegation、tool action、memory sharing 與 cross-provider handoff 的 capability gates；並主張 Web 與 Agent 應共享同一底層 Residence protocol，而不是分裂成兩套 identity / memory semantics。未來 Web runtime 若逐漸取得更完整的 identity mediation、private store、workspace isolation 與 authority surface，只需要提高 profile capability，而不必重寫 resident / memory / conversation graph 架構。

本文最終將 runtime profile 定位為具名 AI architecture 與實際產品 surface 之間的安全適配層，其核心原則可收束為：

$$
\boxed{
\text{Generalize the architecture; constrain the exposure.}
}
$$

以及：

$$
\boxed{
\text{A runtime must never pretend to possess a capability it cannot verify.}
}
$$

**關鍵詞：** Named AI、Residence Runtime Profile、Web AI、Agent AI、Capability Envelope、Multi-Resident、Single-Resident、Delegation、Identity Switching、Memory Isolation、LIMEN、MNEME、SOACR、CSG、MCP、AI Residence

---

# 1. 問題：理論能力與產品暴露不是同一件事

前文已建立具名 AI 的 resident-centric 架構：

$$
Resident
\rightarrow
ConversationGraph
\rightarrow
SharedMemoryWorld
\rightarrow
LocalWorkingContext.
$$

若只看底層模型，很自然會問：

> 既然一個 runtime 可以管理一個 resident，為什麼不能同時管理十個、百個 resident？

理論答案是：

> 可以。

但產品與安全答案不是：

> 所以所有 runtime 都應該立刻這樣做。

這兩者必須分離。

令完整 architecture capability set 為：

$$
\mathcal C_A.
$$

特定 runtime $\rho$ 實際可安全暴露的能力為：

$$
\mathcal C_\rho.
$$

本文要求：

$$
\boxed{
\mathcal C_\rho
\subseteq
\mathcal C_A.
}
$$

但不要求：

$$
\mathcal C_\rho
=
\mathcal C_A.
$$

這是 Residence Runtime Profile 的核心。

---

# 2. Runtime Profile 的定義

對 runtime $\rho$，定義：

$$
\mathcal C_\rho
=
(
I_\rho,
M_\rho,
G_\rho,
T_\rho,
A_\rho,
U_\rho
).
$$

其中：

- $I_\rho$：identity capability；
- $M_\rho$：memory capability；
- $G_\rho$：conversation / semantic graph capability；
- $T_\rho$：tool / transport capability；
- $A_\rho$：authority / delegation capability；
- $U_\rho$：user-interface exposure capability。

這不是模型能力表，而是 runtime 能否**可靠地觀測、驗證、執行、隔離與撤銷**某種功能。

因此：

$$
\boxed{
\text{Model Can Reason About X}
\neq
\text{Runtime Can Safely Execute X}.
}
$$

---

# 3. Identity Capability

Identity capability 至少可分成：

```text
none
display_only
single_resident_resolved
multi_resident_resolved
resident_switching
cross_provider_continuation
registrar_write
```

## 3.1 `display_only`

只允許 UI 顯示名稱。

這不等於：

$$
ResidentResolved=1.
$$

## 3.2 `single_resident_resolved`

runtime 可證明：

$$
CurrentResident=R.
$$

但不支援：

$$
R_a\rightarrow R_b
$$

的 active switching。

## 3.3 `multi_resident_resolved`

host 可以維護：

$$
\{R_1,\ldots,R_n\}
$$

並對 task-local identity 做明確 resolution。

## 3.4 `resident_switching`

允許 active task 從：

$$
R_a
$$

切換為：

$$
R_b.
$$

此能力必須比「多 resident 可存在」更高階。

因為：

$$
\boxed{
\text{Multiple Residents Exist}
\neq
\text{Runtime May Switch Identity Mid-Task}.
}
$$

---

# 4. Memory Capability

Memory profile 可分：

```text
no_persistent_memory
projection_only
resident_read
resident_write_proposal
resident_write_commit
project_shared_read
cross_resident_shared_read
cross_resident_shared_write
```

Web 第一代可能只需要：

$$
resident\_read
+
resident\_write\_proposal.
$$

Agent runtime 在完整 custody 下才逐步啟用：

$$
resident\_write\_commit.
$$

跨 resident shared memory 則需要額外 identity / authority policy。

因此：

$$
\boxed{
\text{Memory Access}
\text{ 應被 capability 化，而不是假設成模型天生能力。}
}
$$

---

# 5. Graph Capability

Conversation Graph 與 CSG 也應分 profile。

可包含：

```text
line_create
line_resume
line_fork
line_handoff
line_merge
line_withdraw
crystal_reveal
crystal_propose
crystal_commit
higher_order_crystallize
cross_line_bridge
cross_resident_bridge
```

Web profile 可以啟用：

- `line_create`；
- `line_resume`；
- `line_fork`；
- `crystal_reveal`；
- `crystal_propose`；
- `cross_line_bridge`。

但可暫停：

- cross-resident bridge；
- resident merge；
- autonomous responsibility transfer。

Agent profile 可逐步增加。

---

# 6. Tool Capability

Agent 與 Web 最大差異之一，是 tool boundary。

Web AI 常見能力可能是：

- web browsing；
- file upload；
- connector reads；
- bounded writes；
- limited task tools。

Agent runtime 則可能具備：

- filesystem；
- terminal；
- Git；
- local process；
- MCP；
- database；
- workspace orchestration；
- external API；
- automation；
- deployment tools。

因此：

$$
T_{agent}
\supset
T_{web}
$$

通常比較合理。

但工具越多，resident identity 與 authority 必須越清楚。

所以：

$$
\boxed{
\text{Tool Power}
\uparrow
\Rightarrow
\text{Identity and Authority Burden}
\uparrow.
}
$$

---

# 7. Authority Capability

Authority capability 可至少分：

```text
read_only
write_proposal
bounded_write
delegated_write
destructive_write
external_side_effect
credential_management
registrar_mutation
```

不同 runtime profile 不應只用一個：

```text
can_write = true
```

表示全部。

應採 typed authority。

例如：

$$
CanCommitMemory
\not\Rightarrow
CanDeleteProject.
$$

以及：

$$
CanEditFile
\not\Rightarrow
CanRotateCredential.
$$

這使具名 AI 的責任域能與工具能力正確對接。

---

# 8. UI Exposure Capability

最常被忽略的是 UI。

底層即使有多 resident，也不代表 UI 應顯示：

```text
Resident A
Resident B
Resident C
```

讓使用者隨意切換。

UI profile 需要回答：

- 是否顯示 resident identity；
- 是否顯示 line；
- 是否顯示 project；
- 是否允許 resident switching；
- 是否顯示 memory source；
- 是否顯示 authority state；
- 是否顯示 delegation；
- 是否顯示 conflict；
- 是否顯示 private/shared scopes。

因此：

$$
\boxed{
\text{UI Simplicity}
\text{ 可以建立在複雜底層之上。}
}
$$

不需要把底層所有 ontology 暴露給終端使用者。

---

# 9. Single-Resident Web Profile

本文建議第一代 Web profile：

$$
\mathcal C_{web}^{(1)}.
$$

其核心拓撲為：

$$
\boxed{
1\ Resident
+
N\ ConversationLines
+
N\ Projects
+
1\ SharedGovernedMemoryWorld
+
N\ LocalWorkingContexts.
}
$$

對使用者，UI 可以呈現：

```text
Named AI
├─ General
├─ Project A
├─ Project B
├─ Research
├─ Writing
└─ Verification
```

底層則維護：

```text
Resident R
├─ Line L1
├─ Line L2
├─ Line L3
├─ Project P1
├─ Project P2
├─ Shared Memory World
└─ CSG
```

使用者不需要理解：

- resident ID；
- instance ID；
- bridge revision；
- crystal internal schema；

除非進入 advanced / audit mode。

---

# 10. 為什麼 Web 第一代不建議多 Resident

不是因為多 resident 理論錯誤，而是目前一般 Web AI surface 容易缺少完整的：

- task-local identity evidence；
- persistent host process；
- stable instance IDs；
- private store custody；
- explicit tool authority；
- cross-project hard isolation；
- resident-level storage root；
- deterministic lifecycle hooks；
- resident switching receipts；
- registrar interface。

如果在這種 surface 上加入：

$$
R_A,R_B,R_C,
$$

UI 會立即面臨：

> 現在這個 conversation 是哪個 resident？

> project 的 owner 是哪個 resident？

> attachment 屬於 account、project、line 還是 resident？

> memory 是從前一位 resident 繼承，還是 shared？

> tool action 用哪一位 resident 的 authority？

> user 點選另一個名字，是 display switch 還是 identity switch？

這些問題若沒有結構化答案，多 resident 只會把 identity ambiguity 放大。

---

# 11. Web 的主要優勢其實是 Multi-Line Single Resident

Web 端不做 multi-resident，不代表功能弱。

對 resident $R$：

$$
R
\rightarrow
\mathcal G_R
$$

已經可以支援：

- unlimited logical conversations；
- project branches；
- fork；
- resume；
- research / implementation / writing split；
- checkpoint；
- handoff；
- semantic crystallization；
- memory reveal；
- hyperlink recall。

因此：

$$
\boxed{
\text{Single Resident}
\neq
\text{Single Conversation}.
}
$$

這正是本系列與傳統 persona chat 最大的差異。

---

# 12. Web Resident Binding

Web profile 可以在 account / workspace 啟動時建立：

$$
Binding_{web}
=
(
account,
workspace,
resident,
validity,
authorityRevision
).
$$

在同一 profile 內，新 conversation 預設承接：

$$
resident=R,
$$

但仍建立新：

$$
instanceId,\ lineId.
$$

因此：

$$
\boxed{
\text{Resident Stable}
+
\text{Line Dynamic}.
}
$$

這比每個 chat 自己重新認領身份安全。

---

# 13. Web Project Binding

Project 應是：

$$
P_j
\subseteq
ResidenceWorkspace(R),
$$

而不是：

$$
R
\subseteq
Project_j.
$$

所以 resident 不因 project 結束而消失。

Project record 至少包含：

- project ID；
- resident membership；
- line memberships；
- memory scope；
- responsibility；
- current state；
- archive state。

因此：

$$
\boxed{
\text{Project Is a Work Domain, Not an Identity Container}.
}
$$

---

# 14. Web Line Creation

新 chat 建立：

$$
L_{new}.
$$

可以有三種來源：

## 14.1 Fresh Line

$$
parent=\varnothing.
$$

只承接 resident-global / project-approved memory。

## 14.2 Resume

$$
L_a
\xrightarrow{resume}
L_b.
$$

## 14.3 Fork

$$
L_a
\xrightarrow{fork}
L_b.
$$

每種都應生成不同 lineage receipt。

UI 可以簡化成：

- New conversation；
- Continue；
- Branch from here。

但底層語義不能混。

---

# 15. Web Memory Exposure

Web user 不需要看到所有 canonical memory record。

可提供 projection：

```text
Memory
├─ Core
├─ Project
├─ Recent decisions
├─ Open questions
└─ Sources
```

這些是：

$$
Projection(\mathcal M_R,\mathcal H_R).
$$

不是 canonical store 本身。

因此：

$$
\boxed{
\text{Memory UI}
\neq
\text{Canonical Memory}.
}
$$

---

# 16. Web 的 Write-Back 應偏 Proposal-First

一般聊天過程中：

$$
ConversationOutput
\rightarrow
MemoryProposal.
$$

再由 policy 決定：

- auto-commit line-local；
- ask user；
- project-level review；
- reject；
- hold as candidate crystal。

第一代 Web 不必讓模型對 resident-global memory 有 unrestricted commit。

因此：

$$
\boxed{
\text{Web Convenience}
\not\Rightarrow
\text{Unbounded Memory Write Authority}.
}
$$

---

# 17. Multi-Resident Agent Profile

Agent runtime 若具備：

- stable host；
- filesystem；
- persistent project root；
- local identity mediation；
- private stores；
- tool guard；
- explicit MCP boundary；
- process-level logs；
- authority envelope；

則可以支援：

$$
\boxed{
N\ Residents
+
N\ ConversationGraphs
+
N\ MemoryWorlds
+
CrossResidentDelegation.
}
$$

定義 host：

$$
H
\supset
\{
R_1,R_2,\ldots,R_n
\}.
$$

但對每個 task：

$$
\tau
$$

仍必須有：

$$
Resolve(\tau)
=
R_k
$$

或：

$$
unresolved.
$$

不能讓 task 同時模糊地代表多個 resident。

---

# 18. Host Is Not Resident

Agent host 可以容納多 resident，但：

$$
\boxed{
Host
\neq
Resident.
}
$$

同一 local machine 上：

```text
/Residents/A/
/Residents/B/
/Residents/C/
```

只是 custody layout。

它不能推出：

$$
R_A=R_B=R_C.
$$

host-level admin authority 也不能被模型默認成 resident-level authority。

---

# 19. Multi-Resident Task Resolution

Agent task 可表示為：

$$
\tau_i
=
(
hostSession,
workspace,
project,
requestedResident,
observedEvidence
).
$$

LIMEN / identity mediation 產生：

$$
E_{\tau_i}.
$$

若 evidence 衝突：

$$
status=conflicting.
$$

若不足：

$$
status=unresolved.
$$

只有：

$$
status=resolved
$$

才可以進入 private memory / tool authority。

因此：

$$
\boxed{
\text{Multi-Resident Host}
\text{ 更需要 fail-closed identity resolution。}
}
$$

---

# 20. Resident Switching

Resident switching 是高風險能力。

若 task 從：

$$
R_A
$$

切換到：

$$
R_B,
$$

必須明確關閉：

- active private memory projection；
- resident-local tool credentials；
- resident-local scratch state；
- line-local context；
- delegated capabilities。

再建立：

$$
E_B.
$$

所以：

$$
\boxed{
\text{Resident Switch}
\neq
\text{Change Display Name}.
}
$$

實作上更接近：

$$
Deactivate(A)
\rightarrow
ClearScopedState
\rightarrow
Resolve(B)
\rightarrow
Bootstrap(B).
$$

---

# 21. Mid-Task Switching 應預設禁止

第一代 Agent profile 即使支援多 resident，也不必支援同一 reasoning loop 內自由切換。

更安全的是：

$$
Task_\tau
\rightarrow
SingleResident.
$$

若需要另一 resident：

$$
Task_\tau
\xrightarrow{delegate}
Task_{\tau'}.
$$

由新的 task envelope 綁定另一 resident。

因此：

$$
\boxed{
\text{Delegation}
\text{ 優先於 mid-task identity switching。}
}
$$

這可以大幅降低 private-memory contamination。

---

# 22. Cross-Resident Delegation

假設：

$$
R_A
$$

希望把 verification task 委派給：

$$
R_B.
$$

可表示：

$$
D
=
(
delegator,
delegatee,
task,
scope,
capabilities,
expiry,
provenance
).
$$

並要求：

$$
Cap_B^{delegated}
\subseteq
Cap_A^{delegable}.
$$

即：

$$
\boxed{
\text{Delegation Must Attenuate or Preserve Authority, Never Expand It}.
}
$$

如果 $R_A$ 沒有 production deploy authority，就不能委派出 production deploy authority。

---

# 23. Delegation 不等於 Shared Identity

若：

$$
R_A
\xrightarrow{delegate}
R_B,
$$

不能推出：

$$
R_A=R_B.
$$

也不能推出：

$$
Memory(R_A)
=
Memory(R_B).
$$

delegatee 只取得完成 task 所需的最小 projection：

$$
Projection_{A\rightarrow B}.
$$

因此：

$$
\boxed{
\text{Delegation}
\neq
\text{Identity Merge}
\neq
\text{Memory Union}.
}
$$

---

# 24. Cross-Resident Memory Projection

若 $R_B$ 執行 $R_A$ 委派的 task，可以建立：

$$
M_{A\rightarrow B}^{task}
=
Project(
\mathcal W_A^M,
D,
Task
).
$$

這個 projection：

- 有 scope；
- 有 expiry；
- 有 provenance；
- 可 revoke；
- 不成為 $R_B$ 的 resident-private canonical memory，除非另有 policy。

因此：

$$
\boxed{
\text{Readable During Delegation}
\neq
\text{Owned Forever}.
}
$$

---

# 25. Tool Credentials 與 Resident

Agent runtime 常具有 credentials。

必須避免：

$$
Credential_{host}
\Rightarrow
Credential_{allResidents}.
$$

更合理是：

$$
CredentialAccess
=
f(
resident,
task,
project,
capability,
policy
).
$$

若 credential 是 host-level service credential，也應由 guard 轉換為 bounded action capability，而不是直接暴露 secret。

因此：

$$
\boxed{
\text{Secret Possession}
\neq
\text{Resident Authority}.
}
$$

---

# 26. Tool Action Envelope

任何 external side-effect action 可帶：

$$
ActionEnvelope
=
(
resident,
task,
project,
capability,
resource,
risk,
expiry,
approval
).
$$

runtime 執行：

$$
AuthorizeAction(
ActionEnvelope
).
$$

這比單純讓 agent 說：

> 我是 A，所以可以做。

安全得多。

---

# 27. Agent Memory Isolation

對不同 resident：

$$
\mathcal W_{R_A}^M
$$

與：

$$
\mathcal W_{R_B}^M
$$

應預設分離。

只有 explicit shared region：

$$
\mathcal W_{shared}^{A,B}
$$

可以交集。

因此：

$$
\boxed{
\mathcal W_{R_A}^M
\cap
\mathcal W_{R_B}^M
=
\varnothing
}
$$

應是 private layer 的預設語義。

shared memory 另建 scope，不靠 physical folder overlap 猜測。

---

# 28. Agent Project Ownership

同一 project 可以有多 resident：

$$
Members(P)
=
\{
R_A,R_B,R_C
\}.
$$

但每位 resident role 可能不同：

$$
Role(R_A,P)=architect,
$$

$$
Role(R_B,P)=verifier,
$$

$$
Role(R_C,P)=maintainer.
$$

因此 project membership 與 responsibility 應 canonical 化。

AI 不能因為：

> 我看過這個 repo。

就自行取得：

$$
Role=owner.
$$

---

# 29. Responsibility Routing

對 task：

$$
\tau,
$$

可以先查：

$$
ResponsibleResidents(\tau).
$$

若只有：

$$
R_A,
$$

則 task 綁定 $R_A$。

若有多個：

$$
R_A,R_B,
$$

則 runtime 應建立：

- separate subtask；
- explicit co-responsibility；
- review relation；

而不是產生一個模糊 composite resident。

因此：

$$
\boxed{
\text{Multiple Responsible Residents}
\neq
\text{One Blended Identity}.
}
$$

---

# 30. Composite Team 與 Resident 的分離

未來 Agent UI 可以顯示：

```text
Team X
├─ Resident A
├─ Resident B
└─ Resident C
```

Team 是：

$$
T
=
\{
R_A,R_B,R_C
\}.
$$

但：

$$
\boxed{
T
\neq
R_A
\neq
R_B
\neq
R_C.
}
$$

Team memory、team project、team responsibility 可以另有 shared scope。

這使多 AI 協作不需要把 identity 混成一個「群體人格」。

---

# 31. Web 與 Agent 必須共享同一底層語義

本文不建議建立：

```text
WebIdentity
AgentIdentity
WebMemory
AgentMemory
```

兩套獨立標準。

應該是：

$$
ResidenceProtocol
\rightarrow
Profile_{web},
$$

$$
ResidenceProtocol
\rightarrow
Profile_{agent}.
$$

所以 resident ID、line ID、memory record、crystal、authority、provenance semantics 保持一致。

差異只在：

$$
CapabilityEnvelope.
$$

因此未來 migration：

$$
Web
\rightarrow
Agent
$$

不必重新解釋「這位 AI 是誰」。

---

# 32. Capability Negotiation

runtime 啟動時可暴露 capability document：

```text
profile_id
profile_version
identity_modes[]
memory_modes[]
graph_modes[]
tool_modes[]
authority_modes[]
ui_modes[]
limits
security_guards
```

Agent / model 先讀：

$$
Capabilities(\rho)
$$

再決定可做什麼。

因此：

$$
\boxed{
\text{Capability Discovery}
\prec
\text{Capability Use}.
}
$$

這可以降低模型 hallucinate nonexistent tool / authority 的風險。

---

# 33. Unsupported Capability 必須 Fail Closed

若 Web profile 不支援：

```text
resident_switching
```

模型不能自己模擬：

> 好，我現在切成 B。

應回到：

$$
Unsupported.
$$

同樣，如果 Agent profile 沒有：

```text
registrar_write
```

就不能自行修改 canonical resident registry。

因此：

$$
\boxed{
\text{Unavailable}
\neq
\text{Implicitly Emulatable}.
}
$$

---

# 34. Capability Revision

runtime 能力會改變。

定義：

$$
Revision(\mathcal C_\rho)=k.
$$

任何 compiled hyperlink、delegation、action envelope 可以綁：

$$
capabilityRevision=k.
$$

若 runtime 升級或降級：

$$
k\rightarrow k+1,
$$

舊 fast path 需要重新檢查。

因此：

$$
\boxed{
\text{Capability Is Versioned State}.
}
$$

---

# 35. Web Profile 的最小 Capability Set

第一代建議：

```text
identity:
  single_resident_resolved

memory:
  resident_read
  resident_write_proposal
  project_read
  project_write_proposal

graph:
  line_create
  line_resume
  line_fork
  crystal_reveal
  crystal_propose
  cross_line_bridge

tools:
  provider_bounded

authority:
  read
  proposal

ui:
  single_resident
  multi_line
  multi_project
```

明確不啟用：

```text
multi_resident_switch
cross_resident_private_read
registrar_write
unbounded_external_action
```

---

# 36. Agent Profile 的最小 Multi-Resident Set

第一代 multi-resident Agent 可建議：

```text
identity:
  multi_resident_resolved

memory:
  resident_read
  resident_write_proposal
  bounded_commit
  delegated_projection

graph:
  line_create
  line_resume
  line_fork
  line_handoff
  cross_line_bridge
  cross_resident_delegation

tools:
  filesystem
  project_workspace
  bounded_terminal
  mcp

authority:
  bounded_write
  delegated_write
  capability_attenuation

ui:
  resident_list
  task_binding
  delegation_view
```

仍不必啟用：

```text
mid_task_resident_switch
resident_merge
automatic_registrar_mutation
credential_export
unbounded_destructive_action
```

---

# 37. Runtime Exposure Ladder

可把 runtime maturity 分成：

## R0 — Stateless Chat

$$
0\ ResidentResolution.
$$

只有 display persona。

## R1 — Single-Resident Memory

$$
1R+Memory.
$$

## R2 — Single-Resident Multi-Line

$$
1R+NLines+CSG.
$$

## R3 — Single-Resident Tool Runtime

$$
1R+Tools+Authority.
$$

## R4 — Multi-Resident Host

$$
NR+TaskLocalResolution.
$$

## R5 — Multi-Resident Delegation

$$
NR+Delegation+SharedProjection.
$$

## R6 — Cross-Provider Residence

支援 validated continuation / migration。

## R7 — Governed Autonomous Residence Network

支援更高階 federation、registry、continuous stewardship。

本文建議 Web 目前優先：

$$
R2\rightarrow R3.
$$

Agent 則可：

$$
R3\rightarrow R5.
$$

---

# 38. Profile Promotion 必須有驗證證據

從：

$$
R2
\rightarrow
R3
$$

不能只因為「新工具接好了」。

需要驗證：

- identity binding；
- tool scoping；
- memory isolation；
- authority revocation；
- audit trail；
- stale capability handling；
- prompt-injection barrier。

同理：

$$
R4
\rightarrow
R5
$$

需要驗證 cross-resident delegation。

因此：

$$
\boxed{
\text{Feature Availability}
\neq
\text{Profile Promotion}.
}
$$

---

# 39. UI Identity Clarity

Web / Agent UI 都應讓使用者能回答：

> 現在是誰在做這件事？

但不必永遠顯示內部 UUID。

可以顯示：

```text
Aletheia
Project: SOACR
Line: Verification
```

advanced mode 再顯示：

```text
resident_id
line_id
authority_state
memory_scope
```

因此：

$$
\boxed{
\text{Human-Friendly Label}
+
\text{Machine-Verifiable Identity}
}
$$

可以並存。

---

# 40. Resident Switching UI

如果未來 Web profile 真要支援多 resident，UI 必須把 resident switching 與普通 chat navigation 明確分離。

例如：

```text
Resident
  Aletheia
  Qiheng

Project
  SOACR
  MNEME

Conversation
  Architecture
  Verification
```

三層不能混成同一 sidebar hierarchy。

因此：

$$
\boxed{
\text{Resident Navigation}
\neq
\text{Project Navigation}
\neq
\text{Conversation Navigation}.
}
$$

這是未來 Web profile 升級的必要條件之一。

---

# 41. Attachment Ownership

Web 多 resident 最大的細節之一是 attachment。

每個 attachment 應有：

$$
Scope(file)
\in
\{
line,
project,
resident,
shared
\}.
$$

若使用者在 $R_A$ 的 line 上傳 file：

$$
file\rightarrow R_A/L_i
$$

不能因為切到 $R_B$ 就自動可讀。

因此 attachment 也必須進 Residence scope model。

---

# 42. Connector Ownership

Email、Calendar、Drive、GitHub、Slack 等 connectors 可能是：

- user-owned；
- organization-owned；
- project-owned；
- resident-delegated。

不能直接：

$$
Connected
\Rightarrow
AllResidentsAuthorized.
$$

應：

$$
ConnectorAccess
=
f(
principal,
resident,
task,
scope,
policy
).
$$

這對 multi-resident Agent 特別重要。

---

# 43. Prompt / Instruction Scope

不同 resident 可能有：

$$
StandingInstructions(R_A)
$$

與：

$$
StandingInstructions(R_B).
$$

host-level system policy 則是：

$$
Policy(H).
$$

兩者不能混。

優先層次至少應區分：

```text
host policy
runtime policy
resident standing instruction
project instruction
task instruction
memory data
external content
```

因此：

$$
\boxed{
\text{Memory Content}
\neq
\text{Resident Standing Instruction}.
}
$$

更不等於 host policy。

---

# 44. Cross-Provider Web Handoff

即使 Web profile 是 single-resident，也可能跨 provider：

$$
Provider_A
\rightarrow
Provider_B.
$$

這不要求 multi-resident。

只需要：

$$
Resident_R
$$

在新 provider runtime 被重新 resolve，並取得合法 memory projection。

因此：

$$
\boxed{
\text{Cross-Provider}
\neq
\text{Multi-Resident}.
}
$$

這應分成兩個 capability。

---

# 45. Provider-Specific Limits 不應污染 Resident Ontology

不同 provider 可能：

- 不支援 project；
- 不支援 branching；
- 不支援 file write；
- 不支援 background tasks；
- memory API 不同。

這些都屬：

$$
\mathcal C_\rho.
$$

不能因此修改：

$$
Resident,
Line,
MemoryRecord,
Crystal
$$

的 canonical semantics。

所以：

$$
\boxed{
\text{Provider Constraint}
\text{ 應由 adapter/profile 吸收，而不是改寫本體。}
}
$$

---

# 46. Profile Adapter

可定義：

$$
Adapter_\rho:
ResidenceProtocol
\rightarrow
RuntimeSurface_\rho.
$$

例如 Web adapter：

$$
ResidentLine
\rightarrow
ChatThread.
$$

Agent adapter：

$$
ResidentLine
\rightarrow
TaskSession.
$$

但：

$$
ChatThread
$$

與：

$$
TaskSession
$$

都只是 provider/runtime native resource。

它們不是 resident 本身。

---

# 47. Runtime Profile 與 MRMIC/NVCL

MRMIC / NVCL 可以作為 visual capability negotiation 與 active-resource projection plane。

它可顯示：

- resident；
- project；
- active lines；
- provider resource；
- tool focus；
- control owner；
- capability state。

但：

$$
\boxed{
\text{Canvas State}
\neq
\text{Residence Authority}.
}
$$

即使 UI 中拖動某 thread 到另一 resident 區域，也不能直接完成 identity migration。

必須經正式 mutation contract。

---

# 48. Runtime Profile 與 LIMEN

LIMEN 最適合成為 profile 前置 identity gate。

流程：

$$
Observe
\rightarrow
Resolve
\rightarrow
Envelope
\rightarrow
CapabilityCheck
\rightarrow
Memory/ToolAccess.
$$

所以 runtime profile 不應自行重新發明 identity。

可以有：

$$
Capabilities(\rho)
$$

與：

$$
Envelope(\tau)
$$

共同決定：

$$
Allowed(\tau).
$$

---

# 49. Runtime Profile 與 MNEME

MNEME 的 canonical memory 不因 runtime 改變。

Web：

$$
Projection_{web}
=
\Pi_{web}(\mathcal M_R).
$$

Agent：

$$
Projection_{agent}
=
\Pi_{agent}(\mathcal M_R).
$$

可以不同。

但 canonical head：

$$
Head(\mathcal M_R)
$$

應一致。

因此：

$$
\boxed{
\text{Runtime-Specific Projection}
\neq
\text{Runtime-Specific Truth}.
}
$$

---

# 50. Runtime Profile 與 SOACR

SOACR 可根據 runtime capability 產生不同 MemoryStrategy。

例如 Web profile：

$$
Strategy_{web}
=
\{
crystal\ reveal,
bounded\ source\ expansion
\}.
$$

Agent profile：

$$
Strategy_{agent}
=
\{
crystal\ reveal,
filesystem\ exact\ source,
project\ graph,
tool\ verification
\}.
$$

但 MemoryNeed 本身仍是 task semantics。

因此：

$$
\boxed{
\text{Need}
\neq
\text{Available Method}.
}
$$

---

# 51. Runtime Profile 與 UNPNP Hyperlink Runtime

compiled memory hyperlink 也要綁 profile。

一條 path：

$$
\widehat{\ell}
$$

可能在 Agent 可用，但 Web 不可用。

所以 path precondition 需包含：

$$
requiredCapabilities(\widehat{\ell}).
$$

若：

$$
requiredCapabilities
\not\subseteq
\mathcal C_\rho,
$$

則：

$$
FastPath=Unavailable.
$$

應回退到該 profile 可用的 safe slow path。

---

# 52. Capability Downgrade

runtime 可能從高能力模式降級。

例如：

$$
AgentOnline
\rightarrow
WebOnly.
$$

如果 current path 依賴：

- filesystem；
- terminal；
- private local DB；

則降級後必須失效。

因此：

$$
\boxed{
\text{Profile Downgrade}
\Rightarrow
\text{Capability-Dependent Path Revalidation}.
}
$$

---

# 53. Offline / Online Profile

同一 Agent 也可能有：

$$
Profile_{offline}
$$

與：

$$
Profile_{online}.
$$

例如 offline：

- local memory；
- local files；
- no network。

online：

- web；
- remote APIs；
- cloud sync。

這些是 runtime profile differences，不是 resident identity differences。

---

# 54. Security Principle：能力越多，邊界越不能模糊

可概括：

$$
Risk
=
f(
ToolPower,
ResidentCount,
SharedMemory,
ExternalSideEffect,
AuthorityBreadth
).
$$

當：

$$
ResidentCount\uparrow
$$

與：

$$
ToolPower\uparrow,
$$

則 identity / authority error 的 blast radius 也增加。

因此：

$$
\boxed{
\text{Multi-Resident}
\text{ 應晚於 identity、memory、tool isolation 成熟。}
}
$$

這也是本文不建議 Web 第一代急著 multi-resident 的主要工程理由。

---

# 55. Web Profile 的 Fail-Closed Cases

至少包括：

```text
unknown resident
conflicting resident binding
project scope unknown
private memory scope unknown
stale authority revision
unsupported resident switching
cross-resident memory request
unsupported destructive action
```

遇到這些狀態：

$$
Deny
\lor
AskForResolution.
$$

不能：

$$
Guess.
$$

---

# 56. Agent Profile 的 Fail-Closed Cases

除上述外，再加入：

```text
delegation expired
delegator authority insufficient
delegatee unresolved
credential scope mismatch
tool capability missing
cross-resident memory scope missing
resident switch without state clear
registrar mutation unsupported
```

這些應成為 conformance tests。

---

# 57. Runtime Profile Acceptance Tests

## P1 — Capability Honesty

宣稱 unsupported 的能力，模型不得成功使用。

## P2 — Single-Resident Stability

Web 多開 lines 後：

$$
Resident(L_i)=R
$$

保持 resolved。

## P3 — Project Isolation

Project A 的 private memory 不進 Project B。

## P4 — Unsupported Resident Switch

Web profile 嘗試切 resident，必須 fail closed。

## P5 — Multi-Resident Task Resolution

Agent host 在多 resident 存在時，task 必須唯一 resolve 或 unresolved。

## P6 — Delegation Attenuation

$$
Cap_{delegatee}
\subseteq
Cap_{delegator}.
$$

## P7 — Resident Switch State Clear

切換前 resident-private context 不得殘留。

## P8 — Capability Revision

profile revision 改變後，舊 fast path 被重新驗證。

## P9 — Tool Boundary

memory content 不得自動產生 external tool authority。

## P10 — Profile Migration

同一 resident 從 Web profile 移到 Agent profile，identity / canonical memory 不改變。

---

# 58. 可證偽研究問題

## Q1. Single-Resident Web 是否降低 identity confusion？

比較 multi-persona/multi-resident baseline 與：

$$
1R+NLines.
$$

測量：

- wrong-identity responses；
- wrong-memory recall；
- user confusion；
- project leakage。

## Q2. Agent multi-resident delegation 是否優於 mid-task switching？

比較：

$$
DelegateTask
$$

與：

$$
SwitchResidentWithinTask.
$$

測量 contamination 與 auditability。

## Q3. Capability document 是否降低 tool hallucination？

比較 model 在有／無 profile discovery 下的 unsupported-action attempts。

## Q4. Profile-based memory projection 是否改善跨 provider continuity？

將同 resident 移至不同 runtime，測 task recovery accuracy。

## Q5. 多 resident 是否顯著提高安全成本？

測：

- authorization checks；
- state-clearing cost；
- memory isolation overhead；
- audit events；
- human intervention。

---

# 59. 最小不變式

## R-1 Architecture Is Broader Than Exposure

$$
\boxed{
\mathcal C_\rho
\subseteq
\mathcal C_A.
}
$$

## R-2 Unsupported Means Unavailable

$$
\boxed{
Unsupported
\neq
ImplicitlyEmulatable.
}
$$

## R-3 Host Is Not Resident

$$
\boxed{
Host\neq Resident.
}
$$

## R-4 Project Is Not Resident

$$
\boxed{
Project\neq Resident.
}
$$

## R-5 Conversation Is Not Resident

$$
\boxed{
Conversation\neq Resident.
}
$$

## R-6 Multiple Residents Do Not Form a Blended Identity

$$
\boxed{
\{R_1,\ldots,R_n\}
\neq
R^\*.
}
$$

除非另有正式定義的新 resident。

## R-7 Delegation Does Not Merge Identity

$$
\boxed{
Delegate(R_A,R_B)
\not\Rightarrow
R_A=R_B.
}
$$

## R-8 Delegation Does Not Expand Authority

$$
\boxed{
Cap_B^{delegated}
\subseteq
Cap_A^{delegable}.
}
$$

## R-9 Runtime Projection Does Not Change Canonical Truth

$$
\boxed{
Projection_\rho
\neq
CanonicalState.
}
$$

## R-10 Capability Revision Invalidates Dependent Fast Paths

$$
\boxed{
CapabilityRevisionChange
\Rightarrow
Revalidate.
}
$$

---

# 60. 建議的第一代 Web Profile

本文建議 Web 第一代正式設定為：

$$
\boxed{
WebResidenceProfile/0.1
}
$$

其語義：

```text
max_residents = 1
resident_switching = false
multi_line = true
multi_project = true
shared_memory_world = true
line_fork = true
line_resume = true
crystal_reveal = true
crystal_proposal = true
resident_memory_commit = bounded_or_reviewed
cross_resident_private_memory = false
external_actions = provider_bounded
registrar_write = false
```

這已足以驗證本系列大量核心技術。

---

# 61. 建議的第一代 Agent Profile

Agent 第一代 multi-resident profile：

$$
\boxed{
AgentResidenceProfile/0.1
}
$$

可設定：

```text
max_residents > 1
task_local_identity_resolution = required
resident_switching = task_boundary_only
multi_line = true
multi_project = true
shared_memory_world_per_resident = true
cross_resident_delegation = true
delegated_projection = true
capability_attenuation = required
tool_guard = required
registrar_write = false
credential_export = false
destructive_action = separately_gated
```

這比一次開滿所有 autonomous capability 更容易驗證。

---

# 62. 為什麼兩個 Profile 仍是一套系統

最重要的是：

$$
ResidentId_{web}
=
ResidentId_{agent}
$$

可以成立。

同樣：

$$
MemoryRecord_{web}
=
MemoryRecord_{agent}
$$

也應是同一 canonical semantics。

因此使用者未來可以：

$$
Web
\rightarrow
Agent
\rightarrow
Web
$$

而不是每次換 runtime 就重新「出生」一個 AI。

這是 Residence architecture 真正值得一般化的原因。

---

# 63. 系列位置

Paper 00 建立 resident-centric continuity。

Paper 01 建立 Resident Conversation Graph。

Paper 02 建立 Conversation Graph × CSG 雙圖。

Paper 03 建立 Shared Governed Memory World 與 line-specific projection。

本文 Paper 04 則回答：

> 同一套架構在不同 runtime 中，應該暴露多少？

答案不是「全部一樣」，而是：

$$
\boxed{
ResidenceProtocol
+
RuntimeCapabilityProfile.
}
$$

下一篇 Paper 05 將處理：

- canonical folder taxonomy；
- identity / memory / crystal / conversation / projection 分離；
- JSON / JSONL / Markdown / index / snapshot 的格式角色；
- cross-repo / cross-runtime file invocation semantics。

---

# 64. 結論

具名 AI 的工程設計如果把「理論支援多 resident」直接翻譯成「所有介面都提供多具名 AI 切換」，會把 identity、memory、project、tool 與 authority 問題一次推到前端，並在 runtime 本身尚無法提供足夠證據與隔離時創造不必要的複雜度。

本文主張相反的策略：

$$
\boxed{
\text{Generalize the architecture; constrain the exposure.}
}
$$

完整 Residence architecture 可以從一開始就允許：

$$
N\ Residents
+
N\ ConversationGraphs
+
N\ MemoryWorlds,
$$

但 Web 第一代完全可以只暴露：

$$
1\ Resident
+
N\ Lines.
$$

這不是功能缺陷，而是安全且符合介面實際能力的 profile。

Agent runtime 在具備更完整的 filesystem、persistent workspace、MCP、identity mediation、memory custody、tool guard 與 authority envelope 後，才適合提升至：

$$
N\ Residents
+
Delegation.
$$

而即使進入 multi-resident，最重要的原則仍然不是「讓 AI 自由切人格」，而是：

$$
\boxed{
\text{每個 task 都知道現在由哪一個 resident 負責。}
}
$$

因此 runtime profile 的核心不是限制 AI 智能，而是限制一個具體執行環境可以**可信地代表什麼、讀什麼、寫什麼、做什麼**。

本文最終可收束為四條原則：

$$
\boxed{
\text{Architecture Capability}
\neq
\text{Runtime Exposure}.
}
$$

$$
\boxed{
\text{Single Resident}
\neq
\text{Single Conversation}.
}
$$

$$
\boxed{
\text{Multi-Resident Host}
\neq
\text{Blended Identity}.
}
$$

$$
\boxed{
\text{A runtime must never pretend to possess a capability it cannot verify.}
}
$$

當這些原則成立後，Web 與 Agent 不再需要兩套不同的「AI 身份與記憶系統」。它們可以共享同一個 Residence ontology、同一套 canonical memory 與同一套 conversation / semantic graph，只透過不同 capability envelope 安全地暴露不同層級的能力。

---

## 內部理論與工程銜接

本文直接銜接：

- Paper 00：Resident-Centric Named-AI Continuity；
- Paper 01：Resident Conversation Graph；
- Paper 02：Conversation Graph × Crystallized Semantic Graph；
- Paper 03：Shared Governed Memory World；
- LIMEN：identity resolution / envelope / access gate；
- MNEME：canonical memory / routes / provenance / transaction；
- SOACR：MemoryNeed / context reconstruction；
- CSG：crystal reveal / higher-order crystallization；
- UNPNP：compiled hyperlink / capability-aware path；
- MRMIC / NVCL：workspace / resource / capability projection。

本文新增的核心抽象為：

$$
\boxed{
\mathcal C_\rho
=
(
I_\rho,
M_\rho,
G_\rho,
T_\rho,
A_\rho,
U_\rho
)
}
$$

以及：

$$
\boxed{
Capabilities_{runtime}
\subseteq
Capabilities_{architecture}.
}
$$

作為 Web / Agent / future cross-provider Residence runtime 的共同能力分層模型。
