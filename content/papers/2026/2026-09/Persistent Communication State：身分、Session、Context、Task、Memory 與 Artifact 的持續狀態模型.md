---
title: "Persistent Communication State：身分、Session、Context、Task、Memory 與 Artifact 的持續狀態模型"
subtitle: "Series A-02｜Persistent Communication State: A Continuity Model for Identity, Session, Context, Task, Memory, and Artifacts"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Draft / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series A｜AI-Native Communication Continuum"
series_number: "A-02"
document_type: "Research Paper"
canonical_source: true
encoding: "UTF-8"
---

# Persistent Communication State：身分、Session、Context、Task、Memory 與 Artifact 的持續狀態模型

## Series A-02｜Persistent Communication State: A Continuity Model for Identity, Session, Context, Task, Memory, and Artifacts

**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Draft / Canonical Source  

---

# 摘要

Series A-01 提出 AI-Native Communication Continuum，主張通訊系統不應把 App、裝置、單一網路連線或單一 AI Provider 當作持續存在的第一層物件，而應保存一個可跨裝置、跨位置、跨模態、跨網路與跨模型持續存在的授權通訊狀態。本文將該總論落成 **Persistent Communication State（PCS，持續通訊狀態）** 的形式模型與工程契約。

本文首先指出，「資料同步」不等於「通訊連續性」。兩台裝置即使都擁有完整訊息歷史，只要使用者的未完成任務、當前工作意圖、角色、權限、AI handoff、待確認操作、所需 Artifact、關係上下文或安全模式沒有被正確恢復，系統仍然可能發生 continuity failure。反之，一個新 Surface 即使只取得最小必要資料，只要能以正確權限與足夠語義恢復當前活動，就可能具有高連續性。

本文將持續狀態定義為：

$$
\mathcal P_t
=
(
I_t,
R_t,
S_t,
X_t,
T_t,
M_t,
F_t,
A_t,
P_t,
G_t
),
$$

其中 $I_t$ 為身分與主體， $R_t$ 為關係／Room 狀態， $S_t$ 為 Session， $X_t$ 為可重建 Context， $T_t$ 為任務與工作流， $M_t$ 為記憶， $F_t$ 為 Artifact 與版本， $A_t$ 為 Agent／Tool runtime state， $P_t$ 為權限與政策， $G_t$ 為治理、證據與撤回狀態。

本文再區分 **Canonical Logical State**、**Authoritative State Domain**、**Local Replica** 與 **Surface Projection**。Canonical 並不代表所有位元存在於單一中央伺服器，而代表在給定 owner、scope、policy 與 version 下，系統可以判定哪一組狀態對某項語義具有權威性。對 Surface $u$ 的投影定義為：

$$
L_{u,t}
=
\Pi_u
(
\mathcal P_t;
C_u,
P_u,
B_u,
R_u
),
$$

其中 $C_u$ 為 Surface capability， $P_u$ 為授權， $B_u$ 為可用注意力／頻寬， $R_u$ 為風險與環境限制。這使「同一個持續世界」與「每個裝置看到不同東西」可以同時成立。

本文提出七種核心轉移：attach、detach、suspend、resume、handoff、fork、merge，以及 revoke／invalidate 這類安全轉移；定義 state checkpoint、resume descriptor、context reconstruction、artifact binding 與 semantic continuity；並依狀態類型採不同一致性策略：權限與撤回偏向強一致或明確 epoch，聊天／Presence 可採因果或最終一致，協作草稿可使用 CRDT 類結構，證據與稽核則偏向 append-only event log 與可驗證版本鏈。

本文提出 Continuity Loss：

$$
\mathcal L_C
=
\sum_{k\in K}
 w_k d_k
+
\lambda_A E_A
+
\lambda_U E_U,
$$

其中 $d_k$ 為不同狀態維度的偏差， $E_A$ 為 authority error， $E_U$ 為 unsafe capability exposure。此定義刻意讓「錯誤授權」與「錯誤能力暴露」具有高懲罰，即使內容同步看似完整，也不得被評為高品質連續性。

在 EVEMISS 既有架構中，Consumer Core v0.1 已存在 Identity & Device Core、Room & Session Kernel、Agent Session Kernel、Memory & Context Core、Event & Ledger Core、Artifact Core、Sync & Local-first Core 與 Mode Isolation；PAI Relay v0.2 已存在 CommunicationSession、Attention Policy、handoff state 與個人通訊代理；ECAC／VoiceDesk／MailGuard 已有企業 Case、Ledger、Policy、Human Review 與 Evidence。本文不重建這些產品，而是提供一個上位 PCS 契約，使它們可以共享 continuity primitives，同時保持個人、企業、角色表演與其他模式的身分／記憶／權限邊界。

**關鍵詞：** Persistent Communication State；Session Continuity；Context Reconstruction；Task Continuity；Local-first；CRDT；Event Sourcing；Artifact Versioning；Identity；Capability Projection；Handoff；Resume；AI-Native Communication；EVEMISS；OUCC；PAI Relay

---

# Abstract

This paper formalizes the **Persistent Communication State (PCS)** layer introduced by the AI-Native Communication Continuum. It argues that synchronization of messages or files is insufficient for continuity: a system may replicate all visible content while still losing unfinished tasks, active intent, authority, agent handoff, pending actions, artifact bindings, or safety state.

PCS separates the logical communication state from its per-device projection. A persistent state is modeled across identity, room and relationship state, sessions, reconstructable context, tasks, memory, artifacts, agents and tools, permissions, and governance. Each physical or virtual surface receives only a policy-constrained projection appropriate to its capabilities, attention budget, network conditions, and risk profile.

The paper defines attach, detach, suspend, resume, handoff, fork, merge, revoke, and invalidation transitions; introduces canonical logical state, authoritative state domains, checkpoints, resume descriptors, context reconstruction, artifact binding, continuity loss, and semantic continuity; and proposes different consistency policies for different state classes. Authorization and revocation require stronger ordering guarantees than presence or conversational metadata; collaborative drafts may use CRDT-like structures; evidence should be append-only and versioned.

The resulting architecture enables a communication world to remain logically continuous while devices, locations, modalities, networks, and AI providers change. It also preserves strict boundaries between consumer, enterprise, personal-relay, and virtual-character modes.

---

# 0. 研究問題：為什麼「同步」仍然可能中斷？

假設使用者在桌面電腦上正在處理一個合作任務：

```text
閱讀對話
→ 查看合約草稿
→ 讓 AI 比對條款
→ 等待對方回覆
→ 準備電話確認
```

之後使用者離開辦公室進入汽車，手機或車載 Surface 已經同步：

- 全部聊天訊息；
- 合約 PDF；
- Email；
- 聯絡人。

若新 Surface 不知道：

- 哪一份合約是目前工作版本；
- 哪一條條款正在爭議；
- AI 剛才已經分析到哪裡；
- 下一步不是再寄 Email，而是等待對方電話；
- 哪些操作已授權，哪些仍需人工確認；
- 當前人在車內，顯示與操作能力必須受注意力約束；

則：

$$
\boxed{
\text{Data Synced}=1
\quad\land\quad
\text{Continuity}=0
}
$$

因此本文定義：

$$
\boxed{
\text{Synchronization}
\subsetneq
\text{Continuity}
}
$$

同步是連續性的必要工具之一，但不是充分條件。

---

# 1. Persistent Communication State 的基本物件

## 1.1 狀態向量

定義：

$$
\boxed{
\mathcal P_t
=
(
I_t,
R_t,
S_t,
X_t,
T_t,
M_t,
F_t,
A_t,
P_t,
G_t
)
}
$$

各維度如下。

| 符號 | 狀態類別 | 核心問題 |
|---|---|---|
| $I_t$ | Identity | 誰正在操作？代表誰？ |
| $R_t$ | Relation / Room | 正在哪個關係、房間、群組或案件空間？ |
| $S_t$ | Session | 哪一段活動仍被視為同一工作／通訊階段？ |
| $X_t$ | Context | 要理解當前狀態需要哪些可重建資訊？ |
| $T_t$ | Task / Workflow | 正在完成什麼、目前在哪個步驟？ |
| $M_t$ | Memory | 哪些長短期記憶允許被使用？ |
| $F_t$ | Artifact | 哪些文件、版本、媒體或結果是目前依賴？ |
| $A_t$ | Agent / Tool | 哪些 Agent、模型、工具與執行狀態被綁定？ |
| $P_t$ | Permission / Policy | 什麼行為現在允許？ |
| $G_t$ | Governance / Evidence | 需要留下什麼證據、審查、撤回與稽核狀態？ |

這十個維度不是宣稱所有系統都必須使用完全相同 schema，而是定義 PCS 最低限度需要能表達的語義範圍。

## 1.2 Persistent 不等於 Immutable

持續狀態不是永遠不變：

$$
\mathcal P_t
\neq
\mathcal P_{t+1}.
$$

真正要求是狀態演化具有可追蹤關係：

$$
\boxed{
\mathcal P_t
\xrightarrow{e_t}
\mathcal P_{t+1}
}
$$

其中 $e_t$ 是合法事件或轉移。

持續性的核心不是靜止，而是：

$$
\boxed{
\text{identity of evolution}
+
\text{authorized recoverability}
}
$$

即系統能回答「這個新狀態從哪裡來」以及「誰有權恢復、延續或改變它」。

---

# 2. Canonical Logical State：Canonical 不是一台中央伺服器

## 2.1 Canonical 的語義

本文使用 canonical state 時，不預設：

$$
\text{Canonical}
=
\text{Central Cloud Database}.
$$

Canonical 是一個**邏輯權威性判定**。

對狀態項目 $q$，定義：

$$
\boxed{
\operatorname{Auth}(q)
=
(
owner,
scope,
version,
policy,
evidence
)
}
$$

如果多個 replica 存在，系統必須能依 owner、scope、版本、政策與事件關係判定：

1. 哪個狀態是有效狀態；
2. 哪些狀態只是舊副本；
3. 哪些修改可以合併；
4. 哪些修改必須人工解決；
5. 哪些資料已被撤回或失效。

因此可以存在：

$$
\text{canonical logical state}
$$

但實體資料分散在：

$$
\{
Device_1,
Device_2,
LocalServer,
Cloud_A,
Cloud_B
\}.
$$

## 2.2 Authoritative State Domain

不是所有狀態都由同一主體擁有。

定義：

$$
\boxed{
D_A(q)
=
\text{authoritative domain of }q
}
$$

例如：

- 個人私人偏好：個人 domain；
- 企業案件 policy：企業 domain；
- 群組成員權限：群組 governance domain；
- 外部 Email 的原始送達紀錄：外部 provider 事件加本地證據 domain；
- 個人 AI 私人記憶：個人 AI memory domain；
- 虛擬角色表演記憶：performance domain。

因此：

$$
\boxed{
\text{One Continuum}
\not\Rightarrow
\text{One Authority}
}
$$

這也是 EVEMISS Consumer Core 既有 Mode Isolation 與企業產品治理邊界必須被保存的原因。

---

# 3. Surface Projection：同一狀態世界，不同可見世界

## 3.1 Local Replica 與 Surface Projection 必須分開

Local Replica 是裝置實際持有的資料或狀態副本：

$$
R_{u,t}.
$$

Surface Projection 則是當下允許呈現與操作的視圖：

$$
L_{u,t}.
$$

兩者不應等同。

一台車載電腦可能已加密快取大量工作資料，但駕駛狀態下不應把完整文件 UI 顯示給駕駛者。

因此：

$$
\boxed{
L_{u,t}
=
\Pi_u
(
\mathcal P_t;
C_u,
P_u,
B_u,
R_u^{risk},
N_u
)
}
$$

其中：

- $C_u$：Surface capability；
- $P_u$：授權與角色；
- $B_u$：注意力、顯示與互動 budget；
- $R_u^{risk}$：環境風險；
- $N_u$：可用網路／計算條件。

## 3.2 Projection 不只是 UI Responsive Design

Responsive Design 通常處理：

$$
\text{screen size}
\rightarrow
\text{layout}.
$$

PCS Projection 處理：

$$
\boxed{
\text{state}
+
\text{authority}
+
\text{attention}
+
\text{risk}
+
\text{modality}
\rightarrow
\text{allowed interaction surface}
}
$$

例如同一個任務：

```text
桌面：完整文件 + 差異比較 + 鍵盤
汽車駕駛：語音摘要 + 暫存決策 + 到站後提醒
汽車後座：完整大螢幕 + 語音 + 視訊會議
手機：摘要 + 快速批准
會議室：共享簡報 + 私人 AI side-channel
```

這些 Surface 都可以指向同一個 $T_t$ 與 $F_t$，但投影不同。

---

# 4. Identity：身分必須比 Session 更穩定

## 4.1 Identity 與 Login Session 不同

傳統 Web 系統常讓 session cookie 或 token 成為實際工作連續性的核心，但 PCS 必須區分：

$$
\boxed{
\text{Actor Identity}
\neq
\text{Authentication Session}
\neq
\text{Communication Session}
}
$$

Actor Identity 回答：

> 誰？

Authentication Session 回答：

> 這個裝置目前是否經過足夠認證？

Communication Session 回答：

> 這段活動是否仍屬於同一持續通訊／任務階段？

三者生命週期可以不同。

## 4.2 Device Identity 也不是 Person Identity

定義裝置綁定：

$$
D_u
\leftrightarrow
I.
$$

這個關係必須允許：

- 新裝置加入；
- 舊裝置移除；
- 臨時 Surface；
- 共享設備上的局部登入；
- 車輛／飯店／會議室等非個人永久設備。

因此最重要的不變量之一是：

$$
\boxed{
\operatorname{Revoke}(D_u)
\not\Rightarrow
\operatorname{Delete}(I)
}
$$

同時：

$$
\boxed{
\operatorname{Attach}(D_v,I)
\not\Rightarrow
\operatorname{GrantAll}(D_v)
}
$$

加入新 Surface 只能取得其必要能力。

---

# 5. Session：Session 是可暫停、可恢復的活動邊界

## 5.1 Communication Session

定義：

$$
\boxed{
S
=
(
sid,
actors,
room,
intent,
mode,
status,
checkpoint,
policy,
links
)
}
$$

其中 status 至少可包含：

```text
ACTIVE
SUSPENDED
WAITING_EXTERNAL
WAITING_USER
HANDOFF_PENDING
FORKED
MERGED
CLOSED
REVOKED
```

這使 Session 不再只是 TCP connection 或 browser session，而是較高層的活動連續性物件。

## 5.2 Session 的時間邊界不是 timeout

一般 session 常以 inactivity timeout 判定結束。

PCS 則允許：

$$
\text{network disconnect}
\not\Rightarrow
\text{session end}.
$$

例如：

```text
正在處理合約
→ 上飛機斷線 40 分鐘
→ 落地重新連線
```

只要 Session 未被 policy 關閉或撤銷，即可：

$$
S_{suspended}
\xrightarrow{resume}
S_{active}.
$$

## 5.3 Session Link

一個真實任務可跨多個通訊通道。

因此定義：

$$
\boxed{
\operatorname{Link}(S_i,S_j)=r_{ij}
}
$$

例如 Email thread、電話、文件協作和會議都可以被連到同一 Task 或 Communication Object，而不必假裝它們是同一 protocol session。

---

# 6. Context：Context 不應等同無限聊天紀錄

## 6.1 Context 是可重建工作狀態

本文定義：

$$
\boxed{
X_t
=
\mathcal R_X
(
E_{\le t},
M_t,
T_t,
F_t,
P_t,
Q_t
)
}
$$

其中：

- $E_{\le t}$：相關事件歷史；
- $M_t$：可用記憶；
- $T_t$：任務狀態；
- $F_t$：Artifact 與版本；
- $P_t$：權限；
- $Q_t$：當前 query／intent。

所以 Context 是一個重建結果，不必永久保存「模型曾看過的所有 token」。

## 6.2 Context Reconstruction

定義重建函數：

$$
\boxed{
\widehat X_t
=
\operatorname{Reconstruct}
(
checkpoint,
recentEvents,
linkedMemory,
artifacts,
taskState,
policy
)
}
$$

目標不是：

$$
\widehat X_t=X_t
$$

在位元層完全相同，而是滿足任務需要的語義充分性：

$$
\boxed{
\operatorname{Adequacy}(\widehat X_t,T_t)
\ge
\tau_X
}
$$

## 6.3 Context Reconstruction Quality

可拆成：

$$
Q_X
=
\alpha F
+
\beta C
+
\gamma R
+
\delta A
-
\eta L,
$$

其中：

- $F$：fidelity，關鍵內容正確度；
- $C$：coverage，必要資訊涵蓋；
- $R$：recency，新近事件完整性；
- $A$：authority，來源與版本權威性；
- $L$：leakage，不該暴露資訊的風險。

因此「把所有歷史全部塞給模型」不是最佳策略，因為 leakage 與權限錯配也可能增加。

---

# 7. Task：真正應該被延續的是未完成的意圖

## 7.1 Task State

定義：

$$
\boxed{
T
=
(
tid,
goal,
state,
nextActions,
dependencies,
blockedBy,
owner,
approvals,
artifacts,
deadline
)
}
$$

其中 state 可以是：

```text
PLANNED
RUNNING
WAITING
BLOCKED
NEEDS_APPROVAL
DEFERRED
COMPLETED
CANCELLED
```

## 7.2 Task Continuity 比 Chat Continuity 更高階

若一段聊天結束，但任務仍存在：

$$
Chat_i
\rightarrow
T
\leftarrow
Chat_j.
$$

因此新 AI 或新 Surface 不應只問：

> 上一段聊天說了什麼？

而應問：

> 目前任務狀態是什麼？哪些事件只是討論，哪些已成為承諾、決策或待辦？

## 7.3 Pending Action 必須是第一級狀態

特別是 AI Agent 系統，必須把：

```text
已提出
已預覽
待批准
已批准未執行
執行中
已執行
失敗
撤回
```

分開。

對外部副作用操作 $a$：

$$
\boxed{
State(a)
\in
\{
PROPOSED,
APPROVED,
COMMITTED,
EXECUTED,
FAILED,
REVOKED
\}
}
$$

否則 handoff 到另一台裝置或另一個 AI 時，最危險的錯誤就是重複執行或把未批准操作當成已批准。

---

# 8. Memory：記憶必須有 owner、scope、purpose 與 retention

## 8.1 Memory Record

延續 Consumer Core 的 owner_scope 與 mode_scope 思路，本文定義：

$$
\boxed{
m
=
(
content,
owner,
scope,
purpose,
source,
confidence,
created,
expires,
policy,
provenance
)
}
$$

## 8.2 記憶不是跨模式自由流動

必須保持：

$$
\boxed{
M_{personal}
\not\subseteq
M_{enterprise}
}
$$

以及：

$$
\boxed{
M_{performance}
\not\Rightarrow
M_{real\ relay}
}
$$

除非存在明確授權與轉換契約。

這一條直接保留既有 EVEMISS 產品邊界：角色表演記憶不能因共享底層資料庫就污染 PAI Relay 的真實代理判斷；企業案件內容也不能默認成為個人 AI 的私人長期記憶。

## 8.3 Remember 與 Retrieve 分開

記憶系統至少有兩個不同決策：

$$
\operatorname{Store}(x)
$$

與：

$$
\operatorname{Retrieve}(x,q,context).
$$

能存不代表每次都能讀；能讀也必須考慮當下 Surface、角色、模式與目的。

---

# 9. Artifact：文件不是附件，而是持續狀態的一部分

## 9.1 Artifact Binding

定義 Artifact：

$$
\boxed{
f
=
(
fid,
type,
version,
hash,
owner,
scope,
provenance,
state,
links
)
}
$$

其中 links 可指向：

- Task；
- Session；
- Case；
- Message；
- Agent run；
- Approval；
- Evidence。

## 9.2 Artifact Version 必須可指認

「合約.pdf」不是足夠的持續狀態。

必須能區分：

$$
f^{(1)},
f^{(2)},\ldots,f^{(n)}.
$$

當 AI 說「我剛才比較的是第三版」，新 Surface 必須能重建同一 version binding，而不是重新抓「目前資料夾裡最新檔案」後假設等同。

## 9.3 Artifact 與 Memory 不同

Memory 可以是摘要、關係或經驗性狀態；Artifact 是可指認、可驗證、可版本化的工作物件。

因此：

$$
\boxed{
\text{Summary of }f
\neq
f
}
$$

AI 可以用摘要恢復 Context，但正式批准、提交、簽署或驗證時仍應回到 canonical Artifact。

---

# 10. Agent 與 Tool State：換模型不應重置世界

## 10.1 AI Provider 不是 Canonical Owner

本文保留 A-01 的原則：

$$
\boxed{
\text{AI Model}
\neq
\text{Work World}
}
$$

定義 Agent binding：

$$
A_t
=
(
agentId,
provider,
model,
role,
capabilities,
runState,
toolState,
checkpoint
).
$$

當 Provider 改變：

$$
Provider_a
\rightarrow
Provider_b,
$$

系統應嘗試維持：

$$
(I,R,S,T,F,P,G)
$$

而重新建構：

$$
(X,A).
$$

## 10.2 Handoff Packet

Agent handoff 不應只是自然語言摘要。

定義：

$$
\boxed{
H
=
(
stateRef,
taskRef,
artifactRefs,
pendingActions,
authority,
constraints,
summary,
verification
)
}
$$

其中 summary 是其中一個欄位，而不是全部。

因此：

$$
\boxed{
\text{Handoff}
\neq
\text{Prompt Copying}
}
$$

---

# 11. Governance 與 Permission：連續性不能越過撤回

## 11.1 Continuity 的反例：舊 Surface 保留過期權限

若權限在 $t_1$ 被撤回：

$$
P_{t_1}
\rightarrow
P_{t_2},
$$

則離線裝置重新連線時不得恢復舊能力：

$$
\boxed{
P_{stale}
\not\Rightarrow
P_{current}
}
$$

## 11.2 Capability Epoch

對高風險能力可以定義：

$$
\boxed{
E_P
=
\text{permission epoch}
}
$$

一個敏感操作只在：

$$
E_{local}=E_{authorized}
$$

或完成必要 revalidation 時允許提交。

這與現代群組加密協議中以 epoch 表示共享密碼狀態演化的做法具有結構類似性，但 PCS 的 permission epoch 是應用層治理概念，不能與 MLS cryptographic epoch 混為同一物件。

## 11.3 Revocation 優先於 Convenience

因此：

$$
\boxed{
\operatorname{Safety}
>
\operatorname{Continuity Convenience}
}
$$

如果系統無法確定授權是否仍有效，寧可：

$$
\text{resume read-only}
$$

或：

$$
\text{require re-authorization}
$$

而不是為了「無縫」延續舊權限。

---

# 12. 核心狀態轉移

本文定義至少八類 PCS transition。

## 12.1 Attach

Surface 加入：

$$
\boxed{
\operatorname{Attach}(u,\mathcal P_t)
\rightarrow
L_{u,t}
}
$$

Attach 包含：

1. 身分驗證；
2. device trust 判定；
3. scope／mode 判定；
4. capability negotiation；
5. permission projection；
6. state hydration。

## 12.2 Detach

$$
\operatorname{Detach}(u)
$$

不應自動等於：

$$
\operatorname{Close}(S).
$$

Surface 可以離開，但 Session 保持 suspended 或在其他 Surface 持續。

## 12.3 Suspend

$$
S_{active}
\rightarrow
S_{suspended}.
$$

Suspend 應產生 checkpoint 或至少 resume descriptor。

## 12.4 Resume

$$
\boxed{
\operatorname{Resume}(S,u)
=
\operatorname{Validate}
+
\operatorname{Reconstruct}
+
\operatorname{Project}
}
$$

因此 Resume 絕不是「把 App 開回來」。

## 12.5 Handoff

$$
(u_i,A_i)
\rightarrow
(u_j,A_j)
$$

但核心 Task／Session 延續。

Handoff 可以發生於：

- PC → 車載；
- 手機 → PC；
- AI Provider A → AI Provider B；
- 人 → AI；
- AI → 人；
- 個人 AI → 專用 Agent。

## 12.6 Fork

當同一狀態需要並行探索：

$$
\mathcal P_t
\rightarrow
\{
\mathcal P_t^{(a)},
\mathcal P_t^{(b)}
\}.
$$

例如兩個 AI 分別研究不同方案。

Fork 必須保留共同 ancestry。

## 12.7 Merge

$$
\operatorname{Merge}
(
\mathcal P^{(a)},
\mathcal P^{(b)}
)
\rightarrow
\mathcal P'.
$$

但不是所有欄位都可以自動 merge。

## 12.8 Revoke / Invalidate

$$
\operatorname{Revoke}(capability)
$$

或：

$$
\operatorname{Invalidate}(stateRef)
$$

必須能跨 replica 傳播並在重新連線後優先處理。

---

# 13. Checkpoint 與 Resume Descriptor

## 13.1 Checkpoint

Checkpoint 不必包含全部原始資料。

定義：

$$
\boxed{
C_k
=
(
stateVersion,
sessionRef,
taskRefs,
artifactRefs,
pendingActions,
contextSeed,
permissionEpoch,
eventCursor,
hash
)
}
$$

## 13.2 Resume Descriptor

對低資源 Surface，可只攜帶：

$$
\boxed{
D_R
=
(
checkpointRef,
actorRef,
mode,
requiredScopes,
resumeIntent
)
}
$$

再由本地或雲端 runtime 補齊可用狀態。

## 13.3 Checkpoint 不等於 Snapshot

Snapshot 偏向資料狀態快照；Checkpoint 更強調「可以從這裡安全地繼續做事」。

所以：

$$
\boxed{
\text{Checkpoint}
=
\text{State Snapshot}
+
\text{Continuation Semantics}
}
$$

---

# 14. Event Log、Snapshot 與 Derived State

## 14.1 Event-Based Reconstruction

可將持續狀態寫成：

$$
\boxed{
\mathcal P_t
=
\operatorname{Fold}
(
\mathcal P_0,
E_1,
E_2,
\ldots,
E_t
)
}
$$

這與 Event Sourcing 的核心思想相容：事件序列保存狀態如何變化，而目前狀態可以由事件重建或由 snapshot 加後續事件重建。

但本文不要求所有資料都必須完整 event-source。

## 14.2 混合式模型

實務上可採：

$$
\boxed{
\text{Snapshot}
+
\text{Append-only Events}
+
\text{Versioned Artifacts}
+
\text{Derived Indexes}
}
$$

例如：

- 身分：authoritative records；
- 權限：policy state + change events；
- 訊息：append-oriented log；
- 草稿：CRDT／版本物件；
- AI Context：derived view；
- Artifact：content-addressed 或 versioned store；
- Evidence：append-only ledger。

---

# 15. Consistency 不是單一選項

## 15.1 每種狀態需要不同一致性模型

若把所有狀態都要求強一致，系統會失去離線能力與可用性。

若全部採最終一致，授權與高風險操作會出現危險窗口。

因此定義一致性映射：

$$
\boxed{
\kappa:
StateClass
\rightarrow
ConsistencyPolicy
}
$$

候選表：

| 狀態 | 建議一致性 |
|---|---|
| Identity binding | 強驗證／明確版本 |
| Permission / revocation | 強排序或 epoch 驗證 |
| Pending external action | idempotent + commit record |
| Message timeline | causal / eventual 可接受 |
| Presence | eventual / expiry |
| Collaborative draft | CRDT 或 OT 類協作模型 |
| Artifact release | explicit version / hash |
| Evidence ledger | append-only / tamper-evident |
| AI derived context | 可重建、非權威 |
| Attention state | 短 TTL / local dominant |

## 15.2 CRDT 適合什麼，不適合什麼

CRDT 的價值在於：

$$
\boxed{
\text{concurrent updates}
\rightarrow
\text{deterministic convergence}
}
$$

它很適合：

- 協作文字；
- 可合併集合；
- 某些標註；
- local-first 編輯狀態。

但不能因為 CRDT 可以合併，就把「支付批准」「權限撤回」「法律簽署」當普通可交換 update。

因此：

$$
\boxed{
\text{Mergeable Data}
\neq
\text{Mergeable Authority}
}
$$

---

# 16. Local-first 與 Cloud-assisted Continuity

## 16.1 Local-first 的必要性

交通、飛行、偏遠地區或企業網路切換都可能造成短暫離線。

因此 PCS 不應假設：

$$
Network(t)=1
\quad\forall t.
$$

應允許：

$$
Network(t)=0
$$

時仍可完成安全的局部活動。

## 16.2 Local Capability Envelope

定義：

$$
\boxed{
\mathcal C_{local}(u,t)
}
$$

表示當前 Surface 離線時允許：

- 讀哪些資料；
- 寫哪些草稿；
- 執行哪些本地模型；
- 建立哪些待同步事件；
- 哪些操作必須等重新連線。

## 16.3 Offline Queue

對離線事件：

$$
E^{offline}
=
\{e_1,\ldots,e_n\}.
$$

重新連線後：

$$
\operatorname{Sync}(E^{offline})
$$

必須經過：

1. 版本檢查；
2. permission epoch 檢查；
3. conflict resolution；
4. duplicate detection；
5. idempotency validation；
6. evidence append。

所以「離線先做、上線再補」不能跳過安全驗證。

---

# 17. Network Continuity 與 State Continuity 的層級差

現代傳輸協議已經可以部分支援網路路徑變化。例如 QUIC 使用 connection ID 讓連線在 client IP／port 改變時進行 connection migration。

但：

$$
\boxed{
\text{Transport Connection Migration}
\neq
\text{Application State Continuity}
}
$$

即使 QUIC connection 成功從 Wi-Fi 切換到行動網路：

- Task 可能仍然丟失；
- AI Context 可能仍然重置；
- 使用者可能仍需重開文件；
- 新 Surface 可能仍不知道先前批准狀態。

因此 PCS 位於更高層：

```text
Physical / Link
→ IP / Transport
→ Session / Communication Protocol
→ Persistent Communication State
→ Task / Experience
```

下層 continuity 是上層 continuity 的加速條件，而不是替代品。

---

# 18. Security State Evolution：以 Epoch 思考，而不是永遠信任舊副本

Messaging Layer Security（MLS）把群組共享密碼狀態表示成連續 epochs，每一次成員或密碼狀態變化都推進群組狀態。這提供一個重要架構啟發：**安全相關狀態應具有明確版本與演化關係。**

PCS 可借用這個結構思想，但保持層次區分：

$$
E_{crypto}
\neq
E_{permission}
\neq
E_{task}.
$$

其中：

- $E_{crypto}$：密碼學群組 epoch；
- $E_{permission}$：應用治理／授權 epoch；
- $E_{task}$：任務版本／狀態演化。

避免所有「版本」被壓進單一 sequence number。

---

# 19. Fork、Merge 與 Conflict Resolution

## 19.1 Fork 是正常能力，不只是錯誤

多 Agent 系統會自然產生並行分支：

$$
T
\rightarrow
\{
T_A,
T_B,
T_C
\}.
$$

因此 PCS 必須原生表示 ancestry：

$$
parent(T_A)=T.
$$

## 19.2 Conflict 類型

至少區分：

1. **Content Conflict**：文字、資料內容衝突；
2. **Version Conflict**：基於不同 Artifact 版本；
3. **Authority Conflict**：不同 actor 都宣稱可決定；
4. **Policy Conflict**：本地舊政策與新政策不一致；
5. **Intent Conflict**：同一 Task 出現互斥目標；
6. **Execution Conflict**：同一外部操作可能重複執行。

## 19.3 Resolution Precedence

可以定義優先關係：

$$
\boxed{
\text{Authority}
>
\text{Policy}
>
\text{Committed External Effect}
>
\text{Canonical Artifact}
>
\text{Derived Context}
}
$$

這不是所有系統的普遍法律，而是安全設計原則：不能讓 AI 自己生成的摘要覆蓋已簽署文件，也不能讓舊快取權限覆蓋新撤回事件。

---

# 20. Continuity Loss

## 20.1 不應只測「有沒有恢復」

定義狀態維度集合：

$$
K
=
\{I,R,S,X,T,M,F,A,P,G\}.
$$

對 transition 前後的語義對應：

$$
d_k
=
D_k
(
q_k^{before},
q_k^{after}
).
$$

定義：

$$
\boxed{
\mathcal L_C
=
\sum_{k\in K}
 w_k d_k
+
\lambda_A E_A
+
\lambda_U E_U
}
$$

其中：

- $E_A$：authority error；
- $E_U$：unsafe capability exposure。

## 20.2 權限錯誤需要高權重

例如：

```text
所有聊天與文件都恢復了
但新車載 Surface 錯誤獲得付款權限
```

此時：

$$
\mathcal L_C
$$

必須非常高，而不能因「99% 資料同步成功」就宣稱 continuity quality 很好。

## 20.3 Continuity Score

可定義：

$$
\boxed{
Q_C
=
\exp(-\mathcal L_C)
}
$$

其中：

$$
0<Q_C\le1.
$$

這只是一個候選正規化，不是本文主張的唯一評分函數。

---

# 21. Semantic Continuity

## 21.1 位元相同不代表語義相同

假設新 Surface 恢復相同文字：

> 「可以，照這個版本送出。」

若沒有綁定：

- 對象；
- 文件版本；
- 時間；
- 權限；
- 原始 actor；

則這段文字沒有足夠操作語義。

因此 communication event 應至少具備：

$$
\boxed{
e
=
(
content,
actor,
target,
contextRef,
artifactRef,
taskRef,
authority,
time,
provenance
)
}
$$

## 21.2 Semantic Continuity Criterion

對任務 $T$，定義：

$$
\boxed{
SC(T,u)
=
\operatorname{CanContinueSafely}
(
T,L_{u,t}
)
}
$$

如果新 Surface 能在不重新詢問大量已知資訊、不越權、不誤用版本的條件下繼續下一步，才稱為高 semantic continuity。

---

# 22. Attention State 也是持續狀態，但必須短生命週期

A-01 已經指出 Surface 需要考慮注意力。本文進一步把 attention 狀態視為：

$$
B_t
=
(
role,
activity,
availableModalities,
interruptibility,
risk
).
$$

但它與長期記憶不同。

例如：

$$
B_{driving}
$$

應該具有短 TTL，不能因為使用者昨天開車時「不可看完整螢幕」而在今天坐辦公桌時仍保留同一限制。

因此 PCS 必須同時管理：

$$
\text{long-lived state}
$$

與：

$$
\text{ephemeral context state}.
$$

---

# 23. Privacy：Projection 本身是隱私邊界

## 23.1 同步到裝置不代表顯示給旁人

在共享車輛、會議室、飯店電視等臨時 Surface 中：

$$
\boxed{
\text{device access}
\neq
\text{ambient disclosure permission}
}
$$

Projection 應考慮：

- 螢幕是否私人；
- 語音是否會被他人聽到；
- 麥克風是否常開；
- 是否有可信耳機；
- Surface 是否為共享裝置；
- 本地資料是否允許持久快取。

## 23.2 Ephemeral Surface

定義臨時 Surface：

$$
U_E.
$$

Detach 時應執行：

$$
\boxed{
\operatorname{PurgeLocalSecrets}(U_E)
+
\operatorname{InvalidateSessionKeys}(U_E)
}
$$

但不刪除 canonical user state。

---

# 24. Product Boundary Preservation

PCS 是共用 primitive，不是要求合併產品。

## 24.1 PAI Relay

PAI Relay 可以使用：

- Persistent Session；
- Attention State；
- Task Relay；
- Artifact Binding；
- Personal Memory；
- Handoff。

但其 authority domain 是個人。

## 24.2 VoiceDesk / MailGuard / ECAC

企業產品可使用相同：

- Session primitives；
- Event log；
- Artifact；
- approval state；
- evidence；
- handoff。

但 authority domain 是：

$$
\text{Tenant / Workspace / Case / Enterprise Policy}.
$$

## 24.3 Virtual Character / Multi-Agent Stage

角色平台可以使用：

- Room；
- Session；
- Agent state；
- multimodal media；
- persistent scene；
- artifact。

但表演記憶與角色權限不能默認流入現實個人代理。

因此：

$$
\boxed{
\text{Shared PCS Protocol}
\not\Rightarrow
\text{Shared Semantic Authority}
}
$$

---

# 25. EVEMISS 既有架構的對接

## 25.1 Consumer Core v0.1

既有元件可以直接映射：

| Consumer Core | PCS |
|---|---|
| Identity & Device Core | $I_t$ + Surface binding |
| Room & Session Kernel | $R_t,S_t$ |
| Agent Session Kernel | $A_t$ |
| Memory & Context Core | $M_t,X_t$ |
| Event & Ledger Core | transition / evidence |
| Artifact Core | $F_t$ |
| Privacy / Rights / Safety | $P_t,G_t$ |
| Sync & Local-first Core | replica / merge / offline |
| Mode Isolation | authoritative domains / projection |

所以 PCS 不是另一套重複資料庫，而是把既有元件升格成明確的 continuity semantics。

## 25.2 PAI Relay v0.2

PAI Relay 已有 `CommunicationSession`、`attention_level`、`handoff_state`、linked sessions、Attention Inbox 與多通道 Relay。PCS 提供的是：

$$
\boxed{
\text{跨 Surface / Agent / Channel 的共同狀態契約}
}
$$

使 PAI Relay 未來不必只在單一 App 裡理解自己的 session。

## 25.3 ECAC / Enterprise Suite

企業線已有 Case、Policy、Review、Ledger、Evidence 與 release governance。PCS 不應降低這些治理要求，而應把：

$$
Case
$$

視為一種高治理強度的 persistent domain。

---

# 26. 參考事件命名空間

可新增 PCS namespace：

```text
pcs.identity.attached
pcs.identity.detached
pcs.session.created
pcs.session.suspended
pcs.session.resumed
pcs.session.handoff_requested
pcs.session.handoff_completed
pcs.context.checkpointed
pcs.context.reconstructed
pcs.task.updated
pcs.task.approval_required
pcs.task.approved
pcs.artifact.bound
pcs.artifact.version_changed
pcs.agent.bound
pcs.agent.handoff
pcs.permission.epoch_changed
pcs.permission.revoked
pcs.surface.attached
pcs.surface.projection_changed
pcs.surface.detached
pcs.sync.conflict_detected
pcs.sync.conflict_resolved
pcs.evidence.appended
```

這些名稱只是 v0.1 候選，不應在 A-02 被視為最終 API freeze。

---

# 27. 參考資料模型

## 27.1 PersistentStateEnvelope

```yaml
state_id: pcs_...
owner_domain: personal | enterprise | performance | shared
state_version: 42
created_at: ...
updated_at: ...
identity_refs: []
room_refs: []
session_refs: []
task_refs: []
memory_refs: []
artifact_refs: []
agent_refs: []
permission_epoch: 17
event_cursor: evt_...
checkpoint_ref: chk_...
integrity_hash: ...
```

## 27.2 SurfaceProjection

```yaml
surface_id: vehicle_rear_01
actor_id: ...
mode: personal
source_state_id: pcs_...
projection_version: 8
allowed_modalities:
  - voice
  - display
  - touch
allowed_actions:
  - read
  - draft
  - approve_low_risk
blocked_actions:
  - high_risk_payment
privacy_profile: private_rear_cabin
attention_profile: passenger
expires_at: ...
```

## 27.3 ResumeDescriptor

```yaml
resume_id: res_...
session_id: ...
checkpoint_ref: ...
actor_id: ...
mode: personal
required_scopes: []
permission_epoch: 17
pending_actions: []
artifact_refs: []
resume_intent: continue_current_task
```

---

# 28. Reference Resume Protocol

一次 Surface 切換可以抽象成：

```text
1. DISCOVER_STATE
2. AUTHENTICATE_ACTOR
3. ATTEST_SURFACE
4. FETCH_RESUME_DESCRIPTOR
5. VALIDATE_PERMISSION_EPOCH
6. HYDRATE_MINIMUM_STATE
7. RECONSTRUCT_CONTEXT
8. COMPUTE_SURFACE_PROJECTION
9. VERIFY_PENDING_ACTIONS
10. RESUME_SESSION
11. APPEND_HANDOFF_EVIDENCE
```

形式化：

$$
\boxed{
\mathcal H:
(
\mathcal P_t,
u_i,
u_j
)
\rightarrow
(
\mathcal P_{t+\Delta},
L_{j,t+\Delta}
)
}
$$

subject to：

$$
\operatorname{AuthorityValid}=1,
$$

$$
\operatorname{ProjectionSafe}=1,
$$

$$
\operatorname{ContinuityAdequacy}\ge\tau_C.
$$

---

# 29. Failure Modes

## F1：Message Complete, Task Lost

訊息完整，但不知道下一步。

## F2：Context Hallucination

AI 用摘要補出不存在的決策。

## F3：Artifact Drift

新 Surface 使用錯誤版本文件。

## F4：Permission Staleness

離線 Surface 恢復已撤銷能力。

## F5：Duplicate Side Effect

handoff 後重複寄信、付款或提交。

## F6：Mode Leakage

娛樂角色記憶流入真實代理。

## F7：Identity Collapse

把裝置帳號、AI 身分、角色身分與人類本人混成同一 actor。

## F8：Over-Hydration

為了無縫，把不需要的私人資料灌入共享或不可信 Surface。

## F9：Provider Lock-in State

工作世界只存在某一家 AI Provider 的不可匯出歷史裡。

## F10：False Seamlessness

UI 看起來無縫，但實際權限、版本或 task state 已錯誤。

---

# 30. 測試矩陣

## 30.1 基本場景

| ID | 場景 | 應保持 | 應重新投影 |
|---|---|---|---|
| T1 | PC → 手機 | Task, Session, Artifact refs | UI, modality |
| T2 | 手機 → 車載駕駛 | Task, intent | attention capability |
| T3 | 車載後座 → PC | Task, conversation, draft | full editing tools |
| T4 | Wi-Fi → 5G | Session | network path |
| T5 | Online → Offline | local task state | external action capability |
| T6 | AI A → AI B | Task, artifact, permissions | model context |
| T7 | Personal → Enterprise | only explicitly shared refs | authority / memory scope |
| T8 | Performance → Personal Relay | no implicit memory transfer | mode boundary |
| T9 | Permission revoked offline | identity, safe data | capability denied |
| T10 | Concurrent edits | ancestry / both changes | merge result |

## 30.2 成功條件

至少測量：

$$
Q_C,
Q_X,
T_{resume},
E_{authority},
E_{duplicate},
E_{leakage}.
$$

其中理想安全條件：

$$
E_{authority}=0,
$$

$$
E_{duplicate}=0,
$$

$$
E_{leakage}=0.
$$

---

# 31. 可證偽命題

## H1：State-aware Resume 優於 History-only Resume

對相同任務，新 Surface 若取得結構化 Task／Artifact／Permission／Pending Action state，應比只取得聊天歷史具有更低：

$$
\mathcal L_C.
$$

若在控制實驗中沒有改善，則 PCS 額外結構的價值需重新評估。

## H2：Minimal Projection 可以提高隱私而不顯著破壞 Continuity

若 Projection 能只傳送必要狀態，則應降低 leakage risk，同時保持：

$$
Q_C\ge\tau_C.
$$

## H3：Task-centric Handoff 降低重複操作

結構化 pending-action state 應降低跨 AI／跨裝置的 duplicate side effects。

## H4：Mode Isolation 降低錯誤記憶注入

若 memory scope 與 mode scope 被強制執行，應顯著降低 performance／personal／enterprise 之間的 memory contamination。

---

# 32. 與既有研究／標準的關係

## 32.1 Local-first Software

Local-first 研究強調離線可用、跨裝置協作、資料控制與使用者所有權，並將 CRDT 視為重要候選技術。PCS 接受這些原則，但研究對象更廣：除了文件資料，還包含 Session、Task、Agent、Permission、Artifact binding 與 communication intent。

因此：

$$
\boxed{
\text{Local-first Data Continuity}
\subset
\text{Persistent Communication State}
}
$$

在本文架構中，它不是嚴格數學子集，而是表示研究範圍上的包含關係。

## 32.2 CRDT

Conflict-free Replicated Data Types 提供一類可在分散 replica 上進行並行更新、再達成收斂的資料結構。PCS 將其視為部分資料類型的同步工具，而不是所有 authority state 的普遍解法。

## 32.3 Event Sourcing

Event Sourcing 提供「以事件序列描述狀態演化」的成熟架構模式。PCS 使用其思想描述 transition、evidence 與 reconstruction，但允許 snapshot、CRDT、versioned object 和其他儲存策略共存。

## 32.4 QUIC Connection Migration

QUIC 可讓 connection 在 client network path 改變時遷移，證明「下層 endpoint address 改變不必等於 connection reset」。PCS 把同一結構原則提升到應用狀態，但不聲稱 QUIC 已提供 Task／Context／Permission continuity。

## 32.5 Messaging Layer Security

MLS 的 group epoch、成員變化與共享 cryptographic state 演化展示了安全狀態版本化的重要性。PCS 借鑑「明確 state evolution」概念，但 permission、task、artifact 與 cryptographic epochs 保持分離。

---

# 33. 與 A-03、A-04 的邊界

A-02 專門回答：

> **什麼狀態需要持續？狀態如何被恢復、遷移、分支、合併與撤回？**

下一篇 A-03 才回答：

> **同一狀態如何投影成文字、語音、影像、文件、螢幕、車艙、耳機與其他多模態 Surface？**

A-04 再回答：

> **AI Communication Runtime 如何規劃、路由、操作、管理注意力並守護 continuity？**

因此本文不提前把 modality planner 或 AI runtime 完整展開。

---

# 34. MVP 實作優先序

本文建議第一個 PCS MVP 不要直接追求完整跨所有 App 的全球 Continuum。

## Phase 1：Canonical State Envelope

完成：

- `state_id`；
- owner domain；
- version；
- Session；
- Task；
- Artifact ref；
- permission epoch；
- event cursor。

## Phase 2：Checkpoint / Resume

實作：

$$
PC
\rightarrow
Mobile
$$

的 deterministic resume harness。

## Phase 3：AI Handoff

實作：

$$
AI_A
\rightarrow
AI_B
$$

但 Task、Artifact、pending actions 與 authority 不變。

## Phase 4：Offline / Merge

加入：

- local event queue；
- reconnection；
- duplicate detection；
- CRDT-compatible draft；
- permission revalidation。

## Phase 5：Vehicle Surface

將 PCS 接到 Series B：

$$
Desktop
\rightarrow
VehiclePassengerSurface.
$$

這會成為 Bridge-01 的第一個具體驗證案例之一。

---

# 35. 核心不變量

本文最終收斂為九條 PCS 不變量。

## Invariant 1：Identity Continuity

$$
\boxed{
\Delta Surface
\not\Rightarrow
\Delta ActorIdentity
}
$$

除非發生顯式角色／身份切換。

## Invariant 2：Authority Separation

$$
\boxed{
\text{Shared State Infrastructure}
\not\Rightarrow
\text{Shared Authority}
}
$$

## Invariant 3：Session ≠ Connection

$$
\boxed{
\Delta NetworkConnection
\not\Rightarrow
\operatorname{Close}(Session)
}
$$

## Invariant 4：Context Must Be Reconstructable

$$
\boxed{
X_t
\text{ must be reconstructable from authorized sources}
}
$$

而不能只存在某模型的不可讀內部狀態。

## Invariant 5：Task Survives Channel Change

$$
\boxed{
\Delta Channel
\not\Rightarrow
\Delta TaskIdentity
}
$$

## Invariant 6：Artifact Version Binding

$$
\boxed{
\text{Action on Artifact}
\Rightarrow
\text{explicit version reference}
}
$$

對高風險／正式操作尤其必要。

## Invariant 7：Revocation Dominates Resume

$$
\boxed{
\operatorname{Revoke}
>
\operatorname{Resume}
}
$$

## Invariant 8：Projection Is Least-Privilege

$$
\boxed{
L_{u,t}
\subseteq
\mathcal P_t
}
$$

這裡的包含表示授權資訊／能力的投影關係，不代表簡單集合複製。

## Invariant 9：Provider Independence

$$
\boxed{
\Delta AIProvider
\not\Rightarrow
\operatorname{Reset}
(
I,S,T,F,P,G
)
}
$$

---

# 36. 結論

AI-Native Communication Continuum 若只停留在「多個裝置都能看到同一批訊息」，並沒有真正解決數位世界的時空斷裂。

真正需要持續的是：

$$
\boxed{
\text{Who}
+
\text{Where-in-the-workflow}
+
\text{Why}
+
\text{What-version}
+
\text{What-is-allowed}
+
\text{What-happens-next}
}
$$

因此本文提出 Persistent Communication State：

$$
\boxed{
\mathcal P_t
=
(
I,R,S,X,T,M,F,A,P,G
)
}
$$

並將跨 Surface 延續表示為：

$$
\boxed{
\mathcal P_t
\xrightarrow{
Validate+Reconstruct+Project
}
L_{u,t+\Delta}
}
$$

其核心不是把所有資料複製到所有地方，而是：

> **讓正確的主體，在正確的 Surface，以正確的權限，取得足夠且可驗證的狀態，安全地繼續原本尚未完成的活動。**

這使裝置、網路、App、AI Provider 與實體位置逐步從「工作世界的邊界」降階為「工作世界的執行條件」。

對 EVEMISS 而言，這一層也提供一個重要統一點：Consumer Core、PAI Relay、OUCC、ECAC、VoiceDesk、MailGuard 與多智能體角色平台可以共享持續狀態 primitive，但仍保持各自不同的 owner、mode、memory、authority、risk 與 governance domain。

下一篇 A-03 將在這個狀態模型上處理 **Multimodal-Native Communication**：同一個 Persistent State 如何根據 Surface、角色、注意力、安全、網路與目的，自動投影成文字、語音、影像、文件、Agent、螢幕與空間介面。

---

# 參考資料

## 外部研究與標準

1. Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M. (2019). *Local-first software: You own your data, in spite of the cloud*. Onward! 2019. DOI: 10.1145/3359591.3359737.
2. Shapiro, M., Preguiça, N., Baquero, C., & Zawirski, M. (2011). *Conflict-free Replicated Data Types*. INRIA Research Report RR-7687.
3. Fowler, M. *Event Sourcing*. Enterprise Application Architecture pattern note.
4. Iyengar, J., & Thomson, M. (2021). RFC 9000: *QUIC: A UDP-Based Multiplexed and Secure Transport*.
5. Barnes, R. et al. (2023). RFC 9420: *The Messaging Layer Security (MLS) Protocol*.

## EVEMISS 內部前置文件

6. `A01_AI_Native_Communication_Continuum_v0.1.md`.
7. `EVEMISS_消費端通訊與角色智能共用核心_架構規劃_v0.1`.
8. `EVEMISS_PAI_Relay_個人AI通訊代理技術白皮書_v0.2`.
9. `EVEMISS_ECAC_MVP_v0.1`.
10. `EVEMISS_Enterprise_Communication_Suite_Integration_v0.7`.
11. `EVEMISS_VoiceDesk_Production_Operations_Governance_v0.6`.
12. `EVEMISS_MailGuard_Authorized_Staging_Calibration_v0.6`.
13. `EVEMISS_虛擬角色多智能體表演與交流平台_技術白皮書_v0.1`.

---

# 附錄 A｜最小 PCS State Machine

```text
NEW
  ↓
ACTIVE
  ├─→ WAITING_USER
  ├─→ WAITING_EXTERNAL
  ├─→ SUSPENDED
  │      ↓
  │    RESUMING
  │      ↓
  │    ACTIVE
  ├─→ HANDOFF_PENDING
  │      ↓
  │    ACTIVE@NEW_SURFACE
  ├─→ FORKED
  │      ↓
  │    MERGED
  ├─→ CLOSED
  └─→ REVOKED
```

其中 `REVOKED` 對高風險權限與 session 應是不可被普通 `resume` 逆轉的終止狀態；重新授權必須形成新 authorization state。

---

# 附錄 B｜A-02 → A-03 交接契約

A-03 可以直接假設本文已提供：

1. `PersistentStateEnvelope`；
2. `SurfaceProjection`；
3. `ResumeDescriptor`；
4. `TaskState`；
5. `ArtifactRef`；
6. `PermissionEpoch`；
7. `AttentionState`；
8. `ContextReconstruction`；
9. `ContinuityLoss`；
10. Mode / Authority Boundary。

A-03 不應重新定義以上物件，而應研究：

$$
\boxed{
\Pi_u:
\mathcal P_t
\rightarrow
\text{Multimodal Interaction Representation}
}
$$

並建立跨文字、語音、視覺、文件、Agent 與空間 Surface 的轉譯契約。
