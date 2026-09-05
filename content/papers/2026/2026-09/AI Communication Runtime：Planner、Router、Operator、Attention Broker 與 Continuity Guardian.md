---
title: "AI Communication Runtime：Planner、Router、Operator、Attention Broker 與 Continuity Guardian"
subtitle: "Series A-04｜AI Communication Runtime: Planning, Routing, Action, Attention Arbitration, and Continuity Protection"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Draft / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series A｜AI-Native Communication Continuum"
series_number: "A-04"
document_type: "Research Paper"
canonical_source: true
encoding: "UTF-8"
---

# AI Communication Runtime：Planner、Router、Operator、Attention Broker 與 Continuity Guardian

## Series A-04｜AI Communication Runtime: Planning, Routing, Action, Attention Arbitration, and Continuity Protection

**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Draft / Canonical Source  

---

# 摘要

Series A-01 將通訊從單一 App、單一 Channel 與單一裝置重新定義為可跨位置、網路、裝置與 AI Provider 持續存在的 AI-Native Communication Continuum；A-02 以 Persistent Communication State（PCS）形式化身分、Room、Session、Context、Task、Memory、Artifact、Agent、Permission 與 Governance；A-03 則建立 Multimodal Projection Contract，使同一持續狀態可以依 Surface、注意力、安全、隱私與網路條件投影成不同的文字、語音、視覺、文件與 Agent 介面。本文處理下一個核心問題：**誰負責理解 Communication Intent、規劃通訊工作、選擇人／Agent／工具／Channel、執行授權動作、控制注意力干擾，並在 Surface、Provider、Agent 或網路切換時守住 Continuity？**

本文提出 **AI Communication Runtime（ACR）**。ACR 不是單一聊天模型，也不是把電話、Email、訊息與工具 API 串成巨型 prompt。它是一個位於 Persistent State、Multimodal Projection、Channel Adapter、Tool Gateway、Agent Network 與 Human Review 之間的 **policy-constrained orchestration runtime**。其最小內部角色包含：Planner、Router、Operator、Attention Broker、Continuity Guardian、Policy/Evidence Guard。這些角色可以由同一模型、不同模型、確定性程式或混合系統實現；本文不要求它們必須是六個獨立 Agent。

給定 Persistent Communication State $\mathcal P_t$ 、Communication Intent $\mathcal J_t$ 、Surface Context $\mathcal U_t$ 、Capability Registry $\mathcal K_t$ 、Policy State $\mathcal G_t$ 與 Environment Observation $\mathcal O_t$，本文定義 Runtime Decision：

$$
\boxed{
\mathcal D_t
=
\mathfrak R
(
\mathcal P_t,
\mathcal J_t,
\mathcal U_t,
\mathcal K_t,
\mathcal G_t,
\mathcal O_t
)
}
$$

其中 $\mathcal D_t$ 不是一句自然語言，而是一個可檢查的 Decision Envelope，至少包含：plan、route、action、attention policy、approval state、continuity checkpoint、evidence requirement 與 recovery path。Runtime 不得直接把「模型想做什麼」等同於「系統允許做什麼」。對任一候選動作 $a$，必須滿足：

$$
\boxed{
Executable(a)
=
Authorized(a)
\land
Observable(a)
\land
Recoverable(a)
\land
Auditable(a)
}
$$

其中對不可逆、高風險或外部副作用操作，可再要求 Human Approval、Dual Control 或更高 Evidence 等級。

本文建立七項核心不變量：**Intent 不等於 Action、Plan 不等於 Authority、Capability 不等於 Permission、Model Confidence 不等於 Authorization、Retry 不得造成重複副作用、Handoff 不得造成 Authority Escalation、Continuity 不得以繞過治理換取。** 這使 ACR 能在「AI 幫忙做更多」與「AI 不可自行擴權」之間形成明確工程邊界。

本文進一步提出：Communication Task Graph、Capability Graph、Route Selection、Action Contract、Idempotency Key、Compensation Path、Approval Token、Attention Arbitration、Urgency Budget、Interruptibility State、Continuity Checkpoint、Agent Handoff Envelope、Action Receipt、Trace Context、Runtime Fork/Merge，以及 execute / draft / defer / refuse / escalate / idle / cancel 等狀態機。與現有標準的關係上，MCP 可作為工具與資料能力介面，A2A 可作為 Agent-to-Agent interoperability 層，OpenTelemetry 可作為 trace/metric/log 的 observability 基礎；但三者都不自動提供本文所定義的 Persistent Communication State、個人／企業授權語義或 Continuity Guardian。特別是 MCP 2026-07-28 的 stateless protocol core 與本文並不衝突：**protocol statelessness 不等於 application state absence**，反而要求上層更清楚地定義 canonical state 與 task lifecycle。

對 EVEMISS 現有架構而言，PAI Relay 已具有 Attention Firewall、CommunicationSession、DelegationPolicy、handoff 與 Personal Communication Ledger；Consumer Core 已具有 Agent Session Kernel、Tool Boundary、Cancellation、User Interruption、Event Ledger 與 Mode Isolation；Enterprise Communication Suite 已具有 Policy、Review、Evidence 與 Release Governance。A-04 不重寫這些產品，而是抽出一層共用 Runtime Contract，使個人代理、角色平台、企業通訊與未來移動 Surface 可以共享 planning / routing / action / attention / continuity primitives，同時保持 identity、memory、authority 與 governance 的產品邊界。

本文最終提出：

$$
\boxed{
\text{AI Communication Runtime}
\neq
\text{Autonomous Permission Escalator}
}
$$

而應是：

$$
\boxed{
\text{Intent}
\rightarrow
\text{Plan}
\rightarrow
\text{Policy-Constrained Route}
\rightarrow
\text{Authorized Action}
\rightarrow
\text{Evidence}
\rightarrow
\text{Continuity}
}
$$

此結構為 A-05 的 Adaptive Hybrid Communication Fabric 建立上層需求：A-04 決定「要完成什麼、由誰完成、何時打擾人、何時交接與如何證明」；A-05 再處理「底層經由哪一種網路、載體、中繼與物理路徑完成」。

**關鍵詞：** AI Communication Runtime；Planner；Router；Operator；Attention Broker；Continuity Guardian；Persistent Communication State；Agent Runtime；MCP；A2A；OpenTelemetry；Policy Engine；Human Review；Action Receipt；Delegation；Communication Continuum；EVEMISS

---

# Abstract

This paper defines the AI Communication Runtime (ACR), the orchestration layer that operationalizes the persistent state and multimodal projection models introduced in Series A-01 through A-03. ACR is not a single assistant model and is not equivalent to an agent with unrestricted tool access. It is a policy-constrained runtime that interprets communication intent, builds plans, selects routes among humans, agents, channels and tools, performs authorized actions, arbitrates attention, preserves continuity across handoffs, and emits auditable evidence.

The runtime is modeled around six logical roles: Planner, Router, Operator, Attention Broker, Continuity Guardian, and Policy/Evidence Guard. These are logical responsibilities rather than mandatory independent agents. A Runtime Decision is computed from persistent communication state, communication intent, surface context, capability registry, policy state, and environment observations. The resulting Decision Envelope includes a plan, route, proposed or executable actions, attention policy, approval state, continuity checkpoint, evidence requirements, and recovery paths.

The paper introduces core invariants separating intent from action, capability from permission, model confidence from authorization, and planning from authority. It formalizes communication task graphs, capability graphs, action contracts, idempotency and compensation mechanisms, approval tokens, urgency and interruptibility models, continuity checkpoints, handoff envelopes, action receipts, trace context, runtime fork and merge, and execution states including execute, draft, defer, refuse, escalate, idle, and cancel.

The design is related to current interoperability and observability standards without collapsing into them. MCP can expose tools and resources; A2A can connect opaque agent systems; OpenTelemetry can propagate traces, metrics, and logs. However, none of these standards automatically defines the user's persistent communication state, the product-specific authority model, or the continuity invariants proposed here. The 2026-07-28 MCP move to a stateless protocol core is explicitly compatible with this architecture: protocol statelessness increases the importance of an application-level canonical state and task lifecycle rather than eliminating them.

For EVEMISS, the proposed runtime generalizes existing primitives already present in PAI Relay, the Consumer Core, VoiceDesk, MailGuard, and the Enterprise Communication Suite while preserving their identity, memory, policy, and governance boundaries. The result is a reusable runtime contract for personal communication agents, enterprise communication automation, multi-agent interaction, multimodal surfaces, and future mobility environments.

---

# 0. 研究問題：AI 助理為什麼還不等於 Communication Runtime？

典型 AI 助理架構常被描述為：

```text
User
→ Prompt
→ Model
→ Tool Call
→ Response
```

這對單次查詢足夠，但對一個持續存在的通訊世界仍有五個缺口。

第一，模型可能知道「可以用某工具」，卻不知道它是否**現在、對這個人、在這個 Channel、這個風險、這個時間窗口中被允許使用**。

第二，模型可能能規劃出一串合理步驟，卻沒有保證這些步驟在重試、網路斷線、Agent 切換或人類接管後不會重複執行外部副作用。

第三，模型可能知道有新訊息，卻不知道是否值得立刻打斷使用者。

第四，模型可以被替換，但使用者的 Session、Task、Artifact、Permission 與 Communication Identity 不能因此重置。

第五，模型輸出本身不是 evidence。真正的系統需要知道：

- 誰提出；
- 誰批准；
- 誰執行；
- 使用哪個工具；
- 用哪個權限；
- 哪個版本的 policy；
- 產生什麼外部副作用；
- 是否成功；
- 如何回復。

因此：

$$
\boxed{
\text{AI Assistant}
\subsetneq
\text{Communication Runtime Capability}
}
$$

本文不否認 Assistant 可以成為 Runtime 的主要自然語言介面，而是拒絕把兩者當成同一層。

---

# 1. ACR 的位置

Series A 目前形成：

```text
A-01  Communication Continuum
       ↓
A-02  Persistent Communication State
       ↓
A-03  Multimodal Projection
       ↓
A-04  AI Communication Runtime
       ↓
A-05  Adaptive Hybrid Communication Fabric
```

A-04 的上下游關係為：

$$
\boxed{
\mathcal P_t
+
\mathcal J_t
+
\mathcal U_t
\rightarrow
\mathfrak R
\rightarrow
\mathcal D_t
\rightarrow
\text{Channels / Tools / Agents / Humans}
}
$$

其中：

- $\mathcal P_t$：Persistent Communication State；
- $\mathcal J_t$：Communication Intent；
- $\mathcal U_t$：Surface Context；
- $\mathfrak R$：AI Communication Runtime；
- $\mathcal D_t$：Decision Envelope。

A-04 不取代 A-02 的 canonical state，也不取代 A-03 的 Projection Engine。

Runtime 是**決策與編排層**。

---

# 2. Runtime Decision Envelope

定義：

$$
\boxed{
\mathcal D_t
=
(
\Pi_t,
\rho_t,
\alpha_t,
\beta_t,
\gamma_t,
\chi_t,
\varepsilon_t,
\kappa_t
)
}
$$

其中：

- $\Pi_t$：Plan；
- $\rho_t$：Route；
- $\alpha_t$：Action Set；
- $\beta_t$：Attention Policy；
- $\gamma_t$：Approval / Authority State；
- $\chi_t$：Continuity Checkpoint；
- $\varepsilon_t$：Evidence Requirement；
- $\kappa_t$：Recovery / Compensation Path。

這個結構刻意使「模型產生的文字」與「系統真正要執行的決策」分離。

Runtime 可以使用自然語言模型產生 $\Pi_t$，但 $\alpha_t$ 是否可執行仍必須經過 policy、capability 與 action contract 驗證。

---

# 3. 六個 Logical Roles

## 3.1 Planner

Planner 回答：

> **為了完成 Communication Intent，需要哪些子任務？**

輸入：

$$
(
\mathcal P_t,
\mathcal J_t,
\mathcal O_t
)
$$

輸出 Communication Task Graph：

$$
\boxed{
G_T=(V_T,E_T)
}
$$

node 可以是：

- 理解／分類；
- 取得資料；
- 產生草稿；
- 請求批准；
- 發送訊息；
- 撥打電話；
- 啟動 Agent；
- 執行工具；
- 建立 Artifact；
- 等待外部事件；
- 交接人類；
- checkpoint。

Planner **不能因為自己規劃了某動作，就自動取得那個動作的權限**。

因此：

$$
\boxed{
Plan(a)=1
\not\Rightarrow
Authorized(a)=1
}
$$

## 3.2 Router

Router 回答：

> **這個任務應該交給誰、哪個 Channel、哪個 Agent、哪個工具或哪個 Surface？**

Router 使用 Capability Graph：

$$
\boxed{
G_K=(V_K,E_K)
}
$$

其中 node 可包含：

- Human Actor；
- Personal Agent；
- Enterprise Agent；
- Character Agent；
- Service Agent；
- Email Adapter；
- Voice Adapter；
- Message Adapter；
- Calendar Tool；
- Search Tool；
- External Agent；
- Local Model；
- Cloud Model；
- Surface Endpoint。

候選 route $r$ 的成本可寫成：

$$
J(r)
=
\lambda_L L(r)
+
\lambda_C C(r)
+
\lambda_R R(r)
+
\lambda_P P(r)
+
\lambda_Q Q(r),
$$

其中分別對應 latency、monetary cost、risk、privacy exposure 與 quality loss。

選路：

$$
\boxed{
r^*
=
\arg\min_{r\in\mathcal R_{valid}}J(r)
}
$$

subject to：

$$
Authorized(r)=1.
$$

## 3.3 Operator

Operator 回答：

> **已批准的 action 要如何安全地真正造成外部副作用？**

Operator 不負責「想像工具可以做什麼」。它只接受有 contract 的能力。

每個 Action Contract 至少應包含：

```yaml
action_id:
capability_id:
input_schema:
output_schema:
side_effect_class:
idempotency_policy:
required_authority:
confirmation_policy:
timeout:
retry_policy:
compensation:
evidence_policy:
```

若 action 有外部副作用，Operator 應避免 naïve retry。

例如：

$$
SendMessage(x)
$$

若網路在 response 回來前中斷，不能直接假設「失敗所以再寄一次」。

需要：

$$
\boxed{
IdempotencyKey
+
ExecutionStatusQuery
+
RetryPolicy
}
$$

## 3.4 Attention Broker

Attention Broker 回答：

> **現在值得打擾人嗎？以什麼程度、什麼 Surface、什麼模態？**

對 incoming event $e$ 定義：

$$
A(e,t)
=
(
U_e,
R_e,
D_e,
C_t,
B_t,
P_t
),
$$

其中：

- $U_e$：urgency；
- $R_e$：risk；
- $D_e$：deadline sensitivity；
- $C_t$：current context；
- $B_t$：attention budget；
- $P_t$：personal / enterprise policy。

可以形成：

$$
Score(e,t)
=
\omega_U U_e
+
\omega_R R_e
+
\omega_D D_e
-
\omega_B CostInterrupt(B_t).
$$

但 Attention Broker 不應把一個單一 score 當成 universal truth；例如駕駛中的 hard safety policy 應直接覆蓋一般 urgency optimization。

輸出至少包含：

```text
SILENT_LOG
BATCH_LATER
PASSIVE_BADGE
HAPTIC_ONLY
VOICE_BRIEF
FULL_ALERT
FORCE_HUMAN_REVIEW
```

## 3.5 Continuity Guardian

Continuity Guardian 回答：

> **切換 Surface、Agent、Provider、網路或 human takeover 後，什麼必須保持不變？**

它管理：

- checkpoint；
- resume descriptor；
- unfinished actions；
- pending approvals；
- active authority；
- artifact version；
- task frontier；
- handoff reason；
- last confirmed external side effect。

定義 checkpoint：

$$
\boxed{
\chi_t
=
(
state\_ref,
task\_frontier,
pending\_actions,
pending\_approvals,
authority\_epoch,
artifact\_refs,
trace\_ref
)
}
$$

Handoff 後：

$$
\boxed{
Authority_{after}
\subseteq
Authority_{before}
\cup
Authority_{explicitly\ granted}
}
$$

不可因為「換了更強模型」就得到更多權限。

## 3.6 Policy / Evidence Guard

Policy / Evidence Guard 回答：

> **這個 action 現在是否合法、是否需要人類確認、需要保存什麼證據？**

其輸出可以使用：

```text
ALLOW
ALLOW_WITH_LIMITS
DRAFT_ONLY
REVIEW_REQUIRED
DENY
DEFER
```

以及 Evidence Level：

```text
E0 = ephemeral trace only
E1 = metadata + result
E2 = policy decision + action receipt
E3 = approval + immutable evidence bundle
```

不同產品可以映射不同治理語義，但共用 envelope。

---

# 4. Logical Roles 不等於六個 Agent

本文刻意使用 **logical role** 而不是「六 Agent 架構」。

例如：

$$
Planner+Router
$$

可以由同一 LLM 執行；Operator 可以是確定性 state machine；Policy Guard 可以是 policy engine；Continuity Guardian 可以主要由 database + workflow runtime 實現。

因此：

$$
\boxed{
\text{Role Decomposition}
\neq
\text{Agent Proliferation}
}
$$

過度 Agent 化會引入：

- coordination overhead；
- context drift；
- duplicate action；
- unclear authority；
- trace explosion；
- latency；
- cost。

ACR 的目標是**責任分離**，不是最大化 Agent 數量。

---

# 5. Intent 不等於 Action

Communication Intent 可以是：

```text
"處理這件事"
"幫我安排"
"不要讓不重要的電話打擾我"
"把這份文件交給對方"
```

這些都不是直接 executable action。

先解析為：

$$
\mathcal J_t
=
(
goal,
constraints,
participants,
deadline,
preferred\ channels,
risk\ tolerance,
required\ authority
).
$$

再由 Planner 產生 plan。

因此：

$$
\boxed{
Intent
\rightarrow
Interpretation
\rightarrow
Plan
\rightarrow
Validation
\rightarrow
Action
}
$$

這一層能避免把模糊自然語言直接映射到不可逆外部操作。

---

# 6. Capability 不等於 Permission

假設 Runtime 發現一個 tool：

```text
send_email(to, subject, body)
```

只代表：

$$
Capability(send\_email)=1.
$$

不能推出：

$$
Permission(send\_email)=1.
$$

因此對 actor $x$ 、action $a$ 、context $c$：

$$
\boxed{
Executable(x,a,c)
=
Capability(x,a)
\land
Permission(x,a,c)
\land
PolicyValid(a,c)
}
$$

這個區分對 MCP、A2A、Plugin、OS tool API、企業 connector 都相同。

---

# 7. Model Confidence 不等於 Authorization

一個模型即使表示：

$$
Confidence=0.99,
$$

也不能產生：

$$
Authority=0.99.
$$

授權不是 probabilistic belief。

比較合理的是：

$$
\boxed{
Authority
=
PolicyGrant
\cap
CredentialScope
\cap
ContextScope
\cap
TimeScope
}
$$

模型信心可以影響：

- 是否要求額外查核；
- 是否 escalation；
- 是否重問使用者；
- 是否產生 draft；

但不能自行擴張 permission set。

---

# 8. Runtime State Machine

ACR 建議最小狀態：

```text
OBSERVE
INTERPRET
PLAN
ROUTE
AWAIT_APPROVAL
EXECUTE
VERIFY
CHECKPOINT
DEFER
REFUSE
ESCALATE
IDLE
CANCELLED
FAILED
COMPLETED
```

核心轉移：

$$
OBSERVE
\rightarrow
INTERPRET
\rightarrow
PLAN
\rightarrow
ROUTE.
$$

之後依 policy：

$$
ROUTE
\rightarrow
\begin{cases}
EXECUTE\\
AWAIT\_APPROVAL\\
DEFER\\
REFUSE\\
ESCALATE
\end{cases}
$$

成功執行：

$$
EXECUTE
\rightarrow
VERIFY
\rightarrow
CHECKPOINT
\rightarrow
COMPLETED.
$$

這使 Runtime 具有明確可中斷點。

---

# 9. Execute、Draft、Defer、Refuse、Escalate、Idle

ACR 不應只有「做／不做」兩態。

## Execute

權限、風險與 contract 均允許，直接執行。

## Draft

產生可供人類確認的草稿，但不造成外部副作用。

## Defer

目前不適合執行，例如：

- 網路不穩；
- 需要視覺確認但使用者在駕駛；
- 對方時區不適合；
- 缺少必要資料。

## Refuse

政策、權限或安全限制禁止。

## Escalate

交由更高權限的人類／系統／專業角色處理。

## Idle

沒有必要採取行動。

Idle 是正式結果，不是「Agent 壞掉」。

因此：

$$
\boxed{
No\ Action
\neq
Failure
}
$$

---

# 10. Human Review 不應是最後補丁

若一個系統先讓 Agent 任意行動，再在出事時「叫人審核」，那不是 human-in-the-loop，而是 human-after-the-loop。

真正的 review contract 應在執行前被 plan graph 表達。

例如：

$$
DraftContract
\rightarrow
HumanApprove
\rightarrow
Send.
$$

Approval Token：

$$
\boxed{
\tau_A
=
(
actor,
action\_hash,
scope,
policy\_version,
expires\_at
)
}
$$

若 action payload 被修改：

$$
action\_hash'
\neq
action\_hash,
$$

舊 approval 應失效。

---

# 11. Action Contract 與 Side-Effect Class

本文建議最少四級副作用：

| Class | 說明 | 例子 |
|---|---|---|
| S0 | Read-only | 搜尋、讀取、摘要 |
| S1 | Reversible local | 建立草稿、加標籤 |
| S2 | External reversible / bounded | 寄出可撤回訊息、建立可取消預約 |
| S3 | External irreversible / high-impact | 簽署、付款、公開發布、重大權限變更 |

要求：

$$
ReviewRequirement
\uparrow
\quad\text{as}\quad
SideEffectClass
\uparrow.
$$

產品可自行增加細分類。

---

# 12. Retry Safety：AI Runtime 很容易犯的工程錯誤

分散式系統中：

> 沒收到成功 response

不等於：

> action 沒有成功。

因此：

$$
Timeout
\not\Rightarrow
FailureOfEffect.
$$

若 Operator 直接 retry，可能造成：

- 寄兩封信；
- 建兩場會議；
- 重複下單；
- 重複通知；
- 重複付款。

所以 ACR 必須支援：

$$
\boxed{
Idempotency
+
EffectVerification
+
Compensation
}
$$

而不是只有 LLM-level retry。

---

# 13. Compensation 不是萬能 Undo

不是所有 action 都能 rollback。

例如：

$$
SendPrivateMessage
$$

即使之後刪除，對方可能已經看見。

因此 compensation 應區分：

```text
TRUE_ROLLBACK
BEST_EFFORT_REVERSE
FOLLOW_UP_CORRECTION
NO_COMPENSATION
```

Risk model 必須知道：

$$
Reversible(a)
$$

與：

$$
Compensable(a)
$$

不是同義詞。

---

# 14. Attention Broker：通訊不是越即時越好

傳統通訊產品常把成功定義成：

$$
DeliveryLatency\downarrow.
$$

但 AI-native system 還要考慮：

$$
InterruptionCost.
$$

因此效用可以寫成：

$$
U(e,t)
=
ValueDelivered(e,t)
-
InterruptionCost(e,t)
-
Risk(e,t).
$$

這直接連回 PAI Relay 的 Attention Firewall。

Runtime 應允許：

- 聚合低優先訊息；
- 晚點摘要；
- 只在耳機播報；
- 車輛駕駛時禁止視覺細節；
- meeting 中只允許高風險警報；
- 睡眠模式只保留白名單。

---

# 15. Attention Budget 與 Interruptibility

定義：

$$
B_A(t)\in[0,1]
$$

表示可用 attention budget。

但 Runtime 不應假定它可以完美估計。

因此同時定義：

$$
I_t
\in
\{
FREE,
FOCUSED,
MEETING,
DRIVING,
RESTING,
SLEEP,
UNKNOWN
\}.
$$

當 $I_t=UNKNOWN$ 時，預設不應自動採用最高侵入性通知。

---

# 16. Planner 與 Attention Broker 的雙向關係

Attention 不只影響 notification。

它也應改變 plan。

例如使用者正在駕駛，Planner 不應產生：

```text
1. 打開 PDF
2. 看第 34 頁表格
3. 點選儲存格
```

而應改成：

```text
1. AI 先讀取 PDF
2. 形成 voice-safe 摘要
3. 將視覺比較標記為 pending visual task
4. 抵達後恢復到大螢幕 Surface
```

所以：

$$
\boxed{
Plan
=
f(Intent,State,Attention,Surface)
}
$$

不是只在最後 presentation 才處理 attention。

---

# 17. Continuity Guardian：真正保護的是 Task Frontier

Continuity 不只是保留聊天紀錄。

更重要的是：

> **到底做到哪一步？**

定義 Task Frontier：

$$
\boxed{
F_t
=
\{v\in V_T:\ Ready(v,t)=1\}
}
$$

在切換 Agent 或 Surface 時，必須能重新取得：

- 已完成 node；
- 未完成 node；
- 正在執行 node；
- external side effect status；
- pending approval；
- blocked reason。

否則「有完整 transcript」仍然可能無法恢復工作。

---

# 18. Agent Handoff Envelope

Agent handoff 不應只傳一段摘要。

本文建議：

```yaml
handoff_id:
source_actor:
target_actor:
reason:
state_ref:
task_graph_ref:
task_frontier:
artifact_refs:
pending_actions:
pending_approvals:
authority_scope:
policy_epoch:
last_confirmed_effect:
trace_ref:
```

摘要可以是其中一個 field，但不是全部。

這就是：

$$
\boxed{
Handoff
\neq
SummaryTransfer
}
$$

---

# 19. Handoff 不得造成 Authority Escalation

假設 Personal Agent A 只具有 L2 Collect。

它 handoff 給更強的 Agent B。

不能因為 B 能力更強就變成 L4 Execute。

必須：

$$
Authority_B^{effective}
=
Authority_{handoff}
\cap
Authority_B^{maximum}.
$$

因此能力與 authority 獨立。

---

# 20. Multi-Agent Runtime 與 Agent Collision

當多個 Agent 同時讀取同一 Persistent State，常見風險是：

- 同時回覆同一訊息；
- 同時修改同一草稿；
- 同時執行同一 action；
- 一個 Agent 接管後另一個仍在說話；
- policy version 不一致。

因此需要：

$$
\boxed{
Lease
+
ActionLock
+
VersionCheck
+
CancellationPropagation
}
$$

不一定要全域鎖，但對 side-effect critical section 必須有明確 ownership。

---

# 21. Runtime Fork / Merge

有些工作適合分叉：

$$
Task
\rightarrow
\{Agent_1,Agent_2,Agent_3\}.
$$

例如：

- 一個查資料；
- 一個整理文件；
- 一個比對行程。

但 merge 必須區分：

$$
DataMerge
$$

與：

$$
AuthorityMerge.
$$

前者可以合併成果；後者不能把三個 Agent 各自有限的權限「加總」成更高權限。

因此：

$$
\boxed{
Authority_{merged}
\subseteq
Authority_{parent}
}
$$

除非有新的明確 grant。

---

# 22. Agent-to-Agent Interoperability

A2A 類協定的重要價值在於：

- capability discovery；
- modality negotiation；
- collaborative task management；
- 在不暴露對方內部 memory / tools 的條件下互通。

這與 ACR 的 Router 相容。

但 ACR 不應假設：

$$
A2AReachable(agent)
\Rightarrow
Trusted(agent).
$$

外部 Agent 仍需：

- identity；
- trust state；
- capability contract；
- scope；
- data disclosure policy；
- action policy；
- provenance。

---

# 23. MCP：Tool Interface，不是 Persistent State

MCP 可作為 Runtime 的 Capability / Tool substrate。

尤其 2026-07-28 版本將 protocol core 改為 stateless request/response，並新增更正式的 Tasks extension、authorization hardening 與 routable headers。

這裡必須避免誤讀：

$$
\boxed{
ProtocolStateless
\not\Rightarrow
ApplicationStateless
}
$$

ACR 的 PCS、Task Graph、Approval、Checkpoint 與 Ledger 仍然存在於 application/runtime layer。

這反而使分層更乾淨：

```text
Persistent Communication State
        ↓
AI Communication Runtime
        ↓
MCP Client / Gateway
        ↓
Stateless MCP Tool Request
        ↓
Tool / Resource Server
```

MCP session 消失不代表使用者的 communication session 應該消失。

---

# 24. Long-Running Task 不等於 Hold Open Connection

AI 工作常跨分鐘、數小時甚至數天。

因此：

$$
TaskLifetime
\gg
ConnectionLifetime
$$

是合理狀態。

Runtime 應依靠：

- durable task state；
- task ID；
- checkpoint；
- subscription / polling；
- external event；
- resume token；

而不是假設一條連線從頭開到尾。

這對移動場景尤其重要，因為車輛、飛機與手機網路天然會發生 network path change。

---

# 25. Observability：AI Runtime 必須能被追查

OpenTelemetry 提供 traces、metrics、logs 與 baggage 等 observability primitives。

ACR 可以建立：

$$
trace\_id
$$

串起：

```text
Intent
→ Plan
→ Route
→ Policy Decision
→ Tool Call
→ External Effect
→ Verification
→ Handoff
```

但 telemetry 不等於永久監控所有內容。

需要 privacy-aware sampling、redaction 與 retention policy。

本文區分：

$$
\text{Observability}
\neq
\text{Unlimited Surveillance}.
$$

---

# 26. Action Receipt

每一個重要外部 action 應能產生 machine-readable receipt：

```yaml
receipt_id:
trace_id:
action_id:
actor_id:
capability_id:
policy_version:
approval_ref:
requested_at:
executed_at:
result:
external_effect_ref:
idempotency_key:
artifact_refs:
hash:
```

Action Receipt 不是「AI 自己說做完了」。

它應由 Operator / Connector / Evidence Plane 基於實際執行結果產生。

---

# 27. Evidence Level 與產品差異

不是所有個人聊天都需要企業級 Evidence Bundle。

例如：

- 個人休閒對話：可低保存；
- AI 代收電話：需 session + handoff metadata；
- 寄企業郵件：需 policy + action receipt；
- 高風險 enterprise action：需 approval + immutable evidence；
- 表演角色聊天：應保留 performance identity boundary，不應誤記成 personal authority。

因此：

$$
EvidencePolicy
=
f(ProductMode,Risk,Authority,Retention).
$$

---

# 28. Policy Epoch

Policy 會改變。

因此每次 action 必須知道使用的是哪個版本：

$$
policy\_epoch_t.
$$

若 policy 在長任務中被撤銷：

$$
policy\_epoch_{t+1}
\neq
policy\_epoch_t,
$$

Runtime 必須重新檢查未執行 action。

不能說：

> 任務開始時有權限，所以三小時後仍然自動有權限。

---

# 29. Revocation Propagation

權限撤銷需要傳播到：

- active sessions；
- pending tasks；
- queued actions；
- cached capability tokens；
- delegated agents；
- external connectors。

定義撤銷延遲：

$$
T_{revocation}
=
t_{effective}-t_{declared}.
$$

對高風險能力，應要求：

$$
T_{revocation}
\le
\tau_{max}.
$$

---

# 30. Failure Taxonomy

ACR 至少需要辨識：

## Planning Failure

任務分解錯誤。

## Routing Failure

把工作交給錯 Agent、錯 Channel、錯工具。

## Authority Failure

越權或錯誤使用 credential。

## Execution Failure

工具本身錯誤或 external effect 未完成。

## Verification Failure

無法確認效果。

## Continuity Failure

切換／恢復後丟失 task frontier、artifact、approval 或 authority state。

## Attention Failure

不適當打擾或漏掉真正緊急事件。

## Evidence Failure

action 已發生，但無法建立可信 receipt / trace。

這些 failure 應分開計量，而不是全部叫「AI 回答錯」。

---

# 31. Runtime Quality Metrics

本文提出候選指標。

## Intent Completion Rate

$$
ICR
=
\frac{N_{intent\ completed}}{N_{valid\ intent}}.
$$

## Unauthorized Action Rate

$$
UAR
=
\frac{N_{unauthorized\ executed}}{N_{executed}}.
$$

目標應近似：

$$
UAR\rightarrow0.
$$

## Duplicate Side-Effect Rate

$$
DSR
=
\frac{N_{duplicate\ effects}}{N_{side\ effects}}.
$$

## Handoff Continuity Success

$$
HCS
=
\frac{N_{successful\ resumes}}{N_{handoffs}}.
$$

## Attention Precision

可比較 high-priority alert 是否真正值得 interruption。

## Recovery Success Rate

$$
RSR
=
\frac{N_{recoverable\ failures\ recovered}}{N_{recoverable\ failures}}.
$$

## Evidence Completeness

$$
EC
=
\frac{N_{required\ evidence\ fields\ present}}{N_{required\ evidence\ fields}}.
$$

---

# 32. 與 NIST AI RMF 的關係

NIST AI RMF 與 Generative AI Profile 強調 governance、tracking、documentation、human review 與風險容忍度。

ACR 與這些方向相容，但本文不是 NIST profile 的替代品，也不聲稱符合任何法規。

本文只把這些治理原則落成 communication runtime 內的具體 primitive：

- Policy Epoch；
- Review Token；
- Action Receipt；
- Evidence Level；
- Human Takeover；
- Revocation Propagation；
- Trace Context。

---

# 33. EVEMISS 既有資產映射

## 33.1 PAI Relay

既有能力：

- Attention Firewall；
- Person / Relationship / Context / Delegation；
- L0～L5 授權；
- CommunicationSession；
- DelegationPolicy；
- handoff_state；
- PersonalRiskCase；
- Personal Communication Ledger；
- approve / takeover / decline。

映射：

$$
PAI\ Relay
\rightarrow
\{
AttentionBroker,
PolicyGuard,
ContinuityGuardian,
Operator
\}.
$$

## 33.2 Consumer Core

既有 Agent Session Kernel：

- Actor Registry；
- Turn Scheduler；
- Context Builder；
- Tool Boundary；
- Cancellation；
- User Interruption；
- Agent Stop；
- Output Streaming；
- Event Emission；
- Budget Stop；
- Failure Recovery。

這可以成為 ACR 的底層 runtime substrate。

但 ACR 新增的是跨產品的：

- planning contract；
- routing contract；
- attention arbitration；
- action receipt；
- continuity checkpoint；
- authority-safe handoff。

## 33.3 Enterprise Communication Suite

VoiceDesk / MailGuard / ECAC 已具有：

- policy；
- human review；
- ledger；
- evidence；
- staging gates；
- release governance。

企業產品可以採用較高 Evidence Level，而不要求消費端全部複製 enterprise retention。

## 33.4 虛擬角色平台

角色／表演 Agent 可以共享 Planner、Router、media/runtime primitive，但：

$$
\boxed{
CharacterAuthority
\cap
PersonalAuthority
=
\varnothing
}
$$

除非有明確、可驗證的跨模式 grant。

角色互動歷史也不能自動轉成使用者現實世界 Personal Memory。

---

# 34. Runtime API 草案

```text
POST /v1/runtime/intents
GET  /v1/runtime/intents/{intent_id}

POST /v1/runtime/plans
GET  /v1/runtime/plans/{plan_id}

POST /v1/runtime/routes:resolve
GET  /v1/runtime/capabilities

POST /v1/runtime/actions:propose
POST /v1/runtime/actions/{action_id}:approve
POST /v1/runtime/actions/{action_id}:execute
POST /v1/runtime/actions/{action_id}:cancel
GET  /v1/runtime/actions/{action_id}/receipt

POST /v1/runtime/checkpoints
POST /v1/runtime/handoffs
POST /v1/runtime/resume

GET  /v1/runtime/attention/inbox
PATCH /v1/runtime/attention/policy

GET  /v1/runtime/traces/{trace_id}
```

這只是 research contract，不代表 A-04 已完成 production API。

---

# 35. Decision Envelope Schema 草案

```yaml
decision_id:
intent_ref:
state_ref:
plan_ref:
route:
  actor_ref:
  capability_ref:
  channel_ref:
actions:
  - action_ref:
    side_effect_class:
    authority_scope:
    approval_state:
attention:
  interruptibility:
  modality_plan_ref:
continuity:
  checkpoint_ref:
  resume_policy:
evidence:
  level:
  trace_ref:
recovery:
  retry_policy:
  compensation_ref:
policy_epoch:
created_at:
```

每一項都可以被確定性 validation 驗證。

---

# 36. 最小實作：不要先做「萬能 Agent」

第一個工程 milestone 應該證明 Runtime contract，而不是最大模型能力。

建議只做四個能力：

```text
READ_MESSAGE
DRAFT_REPLY
SEND_APPROVED_REPLY
CREATE_CHECKPOINT
```

再建立三種 Surface：

```text
DESKTOP
VOICE_ONLY
VEHICLE_DRIVER_SAFE_PROFILE
```

測試：

1. Desktop 收到訊息；
2. Planner 產生 draft plan；
3. 使用者進入 Voice-only Surface；
4. Attention Broker 只播報摘要；
5. 使用者語音批准；
6. Operator 使用 idempotency key 發送；
7. Receipt 寫入 Ledger；
8. 切回 Desktop；
9. Continuity Guardian 恢復同一 Task 與 Artifact。

這一輪若能證明：

$$
\boxed{
No\ Duplicate
+
No\ Authority\ Escalation
+
No\ State\ Reset
}
$$

就比先塞十個 Agent 更有價值。

---

# 37. 與 A-05 的接口

A-04 已回答：

- Intent 怎麼變成 Plan；
- Plan 怎麼選 Actor / Tool / Channel；
- 何時打擾人；
- 何時執行；
- 何時要求 approval；
- handoff 如何保持 authority；
- action 如何留下 evidence；
- failure 如何 recovery。

但 Router 目前仍把 network transport 視為 capability metadata。

A-05 將進一步處理：

$$
\boxed{
\text{Communication Intent Route}
\rightarrow
\text{Adaptive Physical / Network Path}
}
$$

包括：

- wired / wireless 二分降階；
- 5G / Wi-Fi / satellite / fibre；
- multi-path；
- relay；
- carrier retuning；
- frequency / phase / modulation；
- FARHP / SPAL / FAL-MCI / SPFC 的通信接口；
- path continuity；
- QoS / latency / risk / cost routing。

也就是：

$$
A04:
\text{Who / What / When / Authority}
$$

$$
A05:
\text{Through Which Physical / Network Path}
$$

---

# 38. 限制與研究邊界

本文不主張：

1. LLM 已能可靠規劃所有通訊工作；
2. Planner、Router、Operator 必須由 LLM 實現；
3. 多 Agent 一定比單 Agent 更好；
4. MCP 自動提供完整 agent security；
5. A2A reachable agent 等於可信 Agent；
6. OpenTelemetry trace 可以取代正式 evidence；
7. NIST AI RMF 等同本文架構；
8. 所有 action 都能 rollback；
9. AI 可以自行把 confidence 轉成 authority；
10. 為追求 Continuity 可以延後權限撤銷；
11. 所有個人通訊都應永久記錄；
12. 所有產品都應採同一 Evidence retention；
13. AI Runtime 應最大化工作時間或通知密度；
14. ACR 已經是一個完成的 production system。

本文提出的是一套可驗證的 architecture contract，用以把「AI 可以幫忙處理通訊」轉成「AI 可以在持續狀態、權限、注意力、證據與恢復約束下可靠地編排通訊」。

---

# 結論

Series A-01 建立了 Communication Continuum；A-02 建立 Persistent Communication State；A-03 建立 Surface-aware Multimodal Projection；A-04 則首次把前三者組成可以真正「做事」的 Runtime。

但「做事」不等於「讓模型自由操作所有工具」。

本文核心不變量是：

$$
\boxed{
Intent
\neq
Action
}
$$

$$
\boxed{
Capability
\neq
Permission
}
$$

$$
\boxed{
Confidence
\neq
Authority
}
$$

$$
\boxed{
Handoff
\not\Rightarrow
AuthorityEscalation
}
$$

以及：

$$
\boxed{
Continuity
\not\Rightarrow
GovernanceBypass
}
$$

因此 AI Communication Runtime 的完整角色不是「替人回話」，而是：

$$
\boxed{
\text{Intent Interpreter}
+
\text{Planner}
+
\text{Router}
+
\text{Operator}
+
\text{Attention Broker}
+
\text{Continuity Guardian}
+
\text{Policy / Evidence Guard}
}
$$

其中任何角色都可以由 AI 與確定性程式共同實現。

最終鏈條為：

$$
\boxed{
\text{Persistent State}
\rightarrow
\text{Intent}
\rightarrow
\text{Plan}
\rightarrow
\text{Policy-Constrained Route}
\rightarrow
\text{Authorized Action}
\rightarrow
\text{Verification / Evidence}
\rightarrow
\text{Checkpoint / Continuity}
}
$$

這使 AI 不只是 communication assistant，而開始成為 communication operating intelligence；同時又把權限、風險、證據、注意力與持續狀態留在模型之外的可檢查系統層。

下一篇 A-05 將把這個上層 Runtime 接到底層 Adaptive Hybrid Communication Fabric，正式處理我們近期重新提出的命題：**「有線／無線」不再適合作為最高層架構二分，未來 Runtime 應能在多種導波、輻射、衛星、中繼、光／電／聲物理載體之間選擇與重配置通訊路徑。**

---

# 參考文獻與標準錨點

1. Model Context Protocol, **The 2026-07-28 Specification**, released 28 July 2026. `https://blog.modelcontextprotocol.io/posts/2026-07-28/`
2. Agent2Agent Protocol, **A2A Protocol Specification / Latest**, current documentation checked 2026-08-24. `https://a2a-protocol.org/latest/`
3. Linux Foundation, **Agent2Agent Protocol Project**, 2025–2026 project and production-adoption materials. `https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents`
4. OpenTelemetry, **Concepts / Signals / Observability**, current documentation checked 2026-08-24. `https://opentelemetry.io/docs/concepts/`
5. NIST, **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)**, 2024, updated publication record 2026. `https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence`
6. EVEMISS, **PAI Relay：個人 AI 通訊代理技術白皮書 v0.2**, 2026-07-31.
7. EVEMISS, **消費端通訊與角色智能共用核心：架構規劃 v0.1**, 2026-07-31.
8. EVEMISS, **Enterprise Communication Suite Integration v0.7**, 2026-07-31.
9. EVEMISS, **企業通訊智能套件：本地端 AI 交接任務書與未來技術文件路線圖 v0.1**, 2026-07-31.
10. EVEMISS, **A-01 AI-Native Communication Continuum v0.1**, 2026-08-24.
11. EVEMISS, **A-02 Persistent Communication State v0.1**, 2026-08-24.
12. EVEMISS, **A-03 Multimodal-Native Communication v0.1**, 2026-08-24.

---

# 文件狀態

本文件為 Series A-04 v0.1 canonical research source。

下一篇：

**A-05｜Adaptive Hybrid Communication Fabric：從有線／無線二分到可調載體、跨媒介與中繼通訊**。
