---
title: "AI-Native Communication Continuum：從通道式通訊到持續多模態通訊世界"
subtitle: "Series A-01｜AI-Native Communication Continuum: From Channel-Centric Communication to Persistent Multimodal Communication Worlds"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Draft / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series A｜AI-Native Communication Continuum"
series_number: "A-01"
document_type: "Research Paper"
canonical_source: true
encoding: "UTF-8"
---

# AI-Native Communication Continuum：從通道式通訊到持續多模態通訊世界

## Series A-01｜AI-Native Communication Continuum: From Channel-Centric Communication to Persistent Multimodal Communication Worlds

**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Draft / Canonical Source  

---

# 摘要

現代數位通訊已經具有電話、即時訊息、Email、WebRTC、視訊會議、雲端文件、跨裝置同步與 AI Agent 等大量能力，但其主流產品架構仍高度依賴「通道」「App」「裝置」作為第一層組織單位。使用者從電腦移動到手機、從辦公室進入汽車、從一般網路切換到衛星或其他接取網路、從文字介面切換到語音介面時，往往必須重新建立工作上下文、重新尋找對話、重新選擇工具，甚至重新向 AI 解釋「剛才做到哪裡」。

本文提出 **AI-Native Communication Continuum（AI 原生通訊連續體）** 作為更高層的通訊架構觀：通訊系統的核心持續物件不應是單一 App、單一連線或單一模型工作階段，而應是一個可跨裝置、跨介面、跨網路、跨物理空間及跨 AI Provider 持續存在的通訊狀態世界。

本文定義連續體狀態：

$$
\mathcal C_t
=
(
I_t,
R_t,
S_t,
X_t,
M_t,
A_t,
P_t,
G_t,
N_t,
U_t
),
$$

其中 $I_t$ 為身分， $R_t$ 為 Room／關係結構， $S_t$ 為 Session 狀態， $X_t$ 為任務與上下文， $M_t$ 為記憶與 Artifact， $A_t$ 為可用 Agent／工具， $P_t$ 為權限與政策， $G_t$ 為治理與證據狀態， $N_t$ 為網路與傳輸能力， $U_t$ 為當前互動 Surface 及其可用模態。

本文的核心不變量為：

$$
\boxed{
\text{Change of device, location, modality, network path, or AI provider}
\not\Rightarrow
\text{reset of communication identity and authorized state}
}
$$

其中「不重置」並不表示所有資料必須在所有裝置無條件複製，也不表示權限在所有場景保持相同。相反地，本文主張連續體必須同時維持 **狀態連續性** 與 **能力隔離**：同一個人的通訊世界可以持續存在，但不同裝置、角色、場景、模式與安全條件可以得到不同的投影與能力集合。

在 EVEMISS 既有架構中，OUCC 已處理 Room、Presence、Messaging、WebRTC 與 Transport；Consumer Core v0.1 已定義 Identity & Device、Provider & Secret Broker、Session & Event Kernel、Realtime Media、Memory & Context、Ledger & Artifact、Mode Isolation 與 Local-first Sync；PAI Relay v0.2 已定義個人通訊入口權、Attention Firewall、Call Relay、Message Relay、Relationship Memory 與有限授權；ECAC、VoiceDesk、MailGuard 與 Enterprise Communication Suite v0.7 則已形成企業通訊、語音、郵件、案例、證據與治理的另一條成熟工程線。本文並不合併這些產品，而是在其下方與其之間建立一個新的高階研究層：**Continuity Runtime**。

本文進一步提出 Surface Adaptation、Communication Intent、Continuity Loss、Network Path Abstraction、AI Communication Runtime 與 Sovereign State Boundary 等概念，並將 AI 定位為維持、轉譯、規劃與操作通訊連續體的智能層，而不是把「通訊世界」本身等同於某一個 AI 模型。

**關鍵詞：** AI-Native Communication；Communication Continuum；Persistent State；Multimodal Communication；Personal AI；Agent Communication；Session Continuity；Context Continuity；WebRTC；WebTransport；QUIC；OUCC；PAI Relay；ECAC；Mobility Continuity

---

# Abstract

Modern communication systems provide voice, messaging, email, real-time media, cloud collaboration, cross-device synchronization, and AI agents, yet their dominant architecture remains channel-centric, application-centric, and device-centric. A change of device, location, modality, network path, or AI provider frequently creates a context break even when the user's underlying communication intent and task remain unchanged.

This paper proposes the **AI-Native Communication Continuum**, a persistent communication-state architecture in which identity, authorized context, sessions, memory, artifacts, agents, policies, and communication intent can survive transitions across devices and physical spaces. The system does not require all data or capabilities to be copied everywhere. Instead, it separates continuity of state from projection of capability, allowing each surface to expose only the modalities and permissions appropriate to its current safety, privacy, attention, and network conditions.

The paper introduces a formal continuum state, transition operators, continuity loss, surface adaptation, communication intent routing, network-path abstraction, sovereign state boundaries, and an AI communication runtime. It also positions existing EVEMISS components, including OUCC, Consumer Core, PAI Relay, ECAC, VoiceDesk, MailGuard, and the multi-agent performance platform, as reusable but non-collapsed layers beneath or above the proposed Continuity Runtime.

---

# 0. 研究地位與核心命題

本文首先區分三件不同的事：

1. **通訊能力存在**：系統能否傳文字、語音、影像、資料或事件；
2. **通訊狀態持續**：使用者換設備、換地點或換介面後，先前狀態是否仍然存在；
3. **通訊世界可遷移**：系統能否根據新環境重新選擇適合的模態、網路、Agent 與互動 Surface，而不要求使用者重新建立整個工作世界。

現代系統已大量完成第一項，部分完成第二項，但第三項仍缺乏一致架構。

本文因此提出：

$$
\boxed{
\text{Communication Continuity}
\neq
\text{mere message synchronization}
}
$$

一個真正的通訊連續體必須至少保存：

$$
\boxed{
\text{Identity}
+
\text{Session}
+
\text{Context}
+
\text{Intent}
+
\text{Policy}
+
\text{Memory}
+
\text{Artifact}
+
\text{Agent State}
}
$$

同時允許底層：

$$
\text{Device},
\text{Surface},
\text{Carrier},
\text{Network},
\text{Model}
$$

發生變化。

本文不是聲稱所有平台今日都已提供完整連續體能力，也不是聲稱 AI 是持續通訊的必要條件。沒有 AI 的系統也可以透過雲端帳號、同步、VoIP、遠端桌面及持續 Session 建立部分連續性。AI 的新作用在於：它可以把「狀態同步」進一步提升為「狀態理解、介面轉譯、任務延續與通道規劃」。

---

# 1. 從通道中心到連續體中心

## 1.1 傳統通訊架構的第一層通常是通道

傳統產品常以以下物件分類：

```text
Phone
Email
Chat
Video Meeting
File Sharing
Calendar
Social Platform
```

這些分類在工程與商業上仍然有用，但它們把同一件人類活動拆成多個彼此獨立的入口。

例如一個「與某合作方完成合約確認」的真實任務，可能經歷：

```text
Email
→ 即時訊息
→ 電話
→ 視訊會議
→ 文件修改
→ 電子簽署
→ 行事曆安排
```

若每個通道各自保存自己的狀態，則系統看到的是七個不同應用中的七段歷史；人類看到的卻是一個持續事件。

因此本文把真正的上層物件改成：

$$
\boxed{
\mathcal O
=
\text{Communication Object / Intent Object}
}
$$

通道只是其執行方法：

$$
\mathcal O
\rightarrow
\{
\text{voice},
\text{text},
\text{video},
\text{email},
\text{agent},
\text{file},
\text{meeting}
\}.
$$

## 1.2 App 不應等同工作世界

現有系統常隱含：

$$
\text{App}
\rightarrow
\text{Session}
\rightarrow
\text{Task}.
$$

本文主張反轉為：

$$
\boxed{
\text{Task / Intent}
\rightarrow
\text{Continuity Runtime}
\rightarrow
\text{Best Available Surface and Channel}
}
$$

因此，一個任務不應因為從桌面切到汽車語音、從 Wi-Fi 切到 5G、或從雲端模型切到本地模型而被視為新任務。

---

# 2. 既有 EVEMISS 架構不是被推翻，而是被重新分層

本文以既有文件作為前置工程來源，而不是重新發明相同元件。

## 2.1 OUCC：通訊底層

既有 Consumer Core 文件將 OUCC 定位為更底層、開放、可自架的通訊核心，主要承擔：

- Room；
- Presence；
- Messaging；
- WebRTC；
- Transport；
- 通用事件傳輸；
- 開放通訊協定及未來聯邦能力。

因此 OUCC 仍然位於 Continuum 的通訊基礎層，而非被 Continuity Runtime 取代。

## 2.2 Consumer Core：消費端共用狀態骨架

Consumer Core v0.1 已經包含：

```text
Identity & Device
Provider & Secret Broker
Session & Event Kernel
Realtime Media
Memory & Context
Ledger & Artifact
Cost & Quota
Mode Isolation & Consumer Governance
Sync & Local-first
Observability
```

其中最值得注意的是，該文件已把「跨裝置無縫狀態」列為後續版本，而不是否認其必要性。

本文的工作，就是把這個先前延後的能力提升為新的研究中心。

## 2.3 PAI Relay：個人通訊邊界

PAI Relay v0.2 已經把個人通訊從「所有來訊直接打擾本人」改寫為：

$$
\text{External Contact}
\rightarrow
\text{Personal Communication Boundary}
\rightarrow
\text{Policy / Risk / Intent}
\rightarrow
\text{Human or Agent Action}.
$$

它已有 Call Relay、Message Relay、Personal Mail Shield、Schedule／Task Relay、Relationship Memory 與 Attention Firewall。

因此 PAI Relay 在本系列中的角色不是被 Continuum 吞掉，而是成為：

$$
\boxed{
\text{Personal Communication Policy Surface}
}
$$

## 2.4 ECAC、VoiceDesk、MailGuard 與 Enterprise Communication Suite

企業線已經形成另一套治理主體：

$$
\text{Tenant}
\rightarrow
\text{Role}
\rightarrow
\text{Policy}
\rightarrow
\text{Workflow}.
$$

其中 VoiceDesk 處理語音與任務執行，MailGuard 處理郵件與風險治理，Suite Gateway 處理跨產品案例、證據與發布治理。

本文保留既有原則：

$$
\boxed{
\text{Shared technology}
\not\Rightarrow
\text{shared governance identity}
}
$$

企業租戶不能因為共用通訊核心就被當成個人使用者模式；角色娛樂模式也不能因為共用模型與語音 Provider 就取得現實代理權。

## 2.5 虛擬角色多智能體平台

虛擬角色平台已經證明同一通訊底座可以支援非工作型活動：自由聊天、表演、共同創作、語音、多角色互動與持續 Room。

這一點對 Continuum 很重要，因為連續體的目的不是把所有可用時間轉換成工作時間，而是讓使用者在不同時空中持續選擇：

$$
\boxed{
\text{Work}
\cup
\text{Communication}
\cup
\text{Entertainment}
\cup
\text{Social}
\cup
\text{Rest}
}
$$

---

# 3. AI-Native Communication Continuum 的正式定義

定義某使用者或授權主體在時間 $t$ 的通訊連續體狀態為：

$$
\mathcal C_t
=
(
I_t,
R_t,
S_t,
X_t,
M_t,
A_t,
P_t,
G_t,
N_t,
U_t
).
$$

其中：

- $I_t$：Identity State，包括人、Agent、裝置、服務與 Provider 身分；
- $R_t$：Relational / Room State，包括 Room、Participants、Presence、關係與 Thread；
- $S_t$：Session State，包括當前 Session、Turn、媒體與中斷位置；
- $X_t$：Context / Task State，包括意圖、任務圖、未完成工作與當前焦點；
- $M_t$：Memory / Artifact State，包括可授權記憶、文件、錄音、摘要與版本；
- $A_t$：Agent / Tool State，包括可用 Agent、工具、連接器、模型與執行能力；
- $P_t$：Policy State，包括權限、模式、注意力、關係與行為限制；
- $G_t$：Governance / Evidence State，包括帳本、稽核、同意、風險與證據；
- $N_t$：Network State，包括可用接取、延遲、頻寬、可靠性、成本與安全；
- $U_t$：Surface State，包括顯示器、語音、攝影機、鍵盤、車艙、耳機等可用互動表面。

這個狀態不是要求所有內容永遠同時存在於每一台裝置。

更準確地說，系統維持的是一個可授權的 canonical state，並對不同 Surface 產生投影：

$$
\Pi_u:
\mathcal C_t
\rightarrow
\mathcal C_t^{(u)}.
$$

其中 $\mathcal C_t^{(u)}$ 是 Surface $u$ 在當前政策下可見、可操作的局部狀態。

因此：

$$
\boxed{
\mathcal C_t^{(phone)}
\neq
\mathcal C_t^{(vehicle)}
\neq
\mathcal C_t^{(office)}
}
$$

並不代表三者屬於三個不同世界。

---

# 4. Continuity Runtime

本文將新的中間層稱為：

**Continuity Runtime**

其位置為：

```text
Applications
PAI Relay | Virtual Character Stage | VoiceDesk | MailGuard | Future Apps
                         |
Adaptive Surface Layer
PC | Mobile | Vehicle | Aircraft | Room | AR | Headset
                         |
Continuity Runtime
Identity | Session | Context | Intent | Memory | Agent | Policy | Handoff
                         |
Consumer Core / ECAC Shared Low-Level Components
                         |
OUCC / Communication Fabric
Room | Presence | Messaging | WebRTC | Transport | Relay
                         |
Physical / Network Backends
Fiber | Ethernet | Wi-Fi | Cellular | Satellite | Other Relays
```

Continuity Runtime 至少執行六類工作。

## 4.1 State Binding

把不同裝置上的局部狀態綁定到同一個 authorized continuum：

$$
B(d_i,\mathcal C)=1.
$$

但只有經過裝置身分與政策驗證後才能加入。

## 4.2 Session Resumption

不是只恢復 TCP／QUIC 連線，而是恢復應用層與認知層的 Session：

$$
S_{t^-}
\rightarrow
S_{t^+}.
$$

## 4.3 Context Reconstruction

當新 Surface 無法直接顯示全部舊狀態時，Runtime 建立適合新介面的最小上下文：

$$
X_{t^+}^{(u)}
=
\Gamma(
X_{t^-},
U_{t^+},
P_{t^+},
A_{t^+}
).
$$

## 4.4 Modality Translation

相同任務可以從視覺切換到語音、從語音切換到大螢幕、從完整互動切換成摘要。

$$
\mathcal T
\xrightarrow{u_1}
R_1
$$

$$
\mathcal T
\xrightarrow{u_2}
R_2
$$

其中 $\mathcal T$ 不變，而 $R_1$ 、 $R_2$ 是不同表示。

## 4.5 Communication Routing

使用者不必先指定「我要用哪一個 App」。

系統可將高階意圖：

$$
\operatorname{Communicate}(target,intent,constraints)
$$

映射為合法執行通道：

$$
\rho:
\operatorname{Intent}
\rightarrow
\{
\text{call},
\text{message},
\text{email},
\text{meeting},
\text{agent-to-agent}
\}.
$$

## 4.6 Safety-Preserving Downgrade

當網路、AI 或裝置能力下降時，Continuity Runtime 不應失去全部功能，而應降級：

```text
full multimodal
→ voice + text
→ text + summary
→ metadata + queue
→ offline local state
→ later reconciliation
```

降級不能擴權。

---

# 5. 狀態連續性不等於能力連續性

這是本系列最重要的不變量之一。

假設同一使用者在辦公室、汽車與公開空間登入同一 Continuum。

我們允許：

$$
Identity_{office}
=
Identity_{vehicle}
=
Identity_{public}.
$$

但不能推出：

$$
Capability_{office}
=
Capability_{vehicle}
=
Capability_{public}.
$$

能力必須由條件函數決定：

$$
K_t
=
F(
I_t,
U_t,
P_t,
G_t,
Attention_t,
Risk_t,
Network_t
).
$$

例如：

- 駕駛狀態可以保留 Session，但禁止高視覺負荷操作；
- 後座乘客可以獲得完整大螢幕、鍵盤及視訊能力；
- 公開空間可以隱藏敏感 Artifact；
- 離線模式可以保留本地摘要但不能執行需要即時授權的外部操作；
- 角色表演模式可以存取 Lorebook，但不能取得 PAI Relay 的聯絡人與現實代理權。

因此本系列採用：

$$
\boxed{
\text{Continuity of identity and state}
+
\text{contextual discontinuity of capability}
}
$$

而不是無條件同步一切。

---

# 6. Surface：設備不是工作世界，而是投影表面

本文把可互動載體統一稱為 Surface。

Surface 可以是：

$$
U
\in
\{
PC,
Phone,
Vehicle,
Aircraft,
Room,
TV,
AR,
Headset,
Kiosk
\}.
$$

每個 Surface 有一個能力描述：

$$
U_i
=
(
D_i,
V_i,
A_i,
C_i,
H_i,
Q_i,
Z_i
),
$$

其中：

- $D_i$：Display capability；
- $V_i$：Voice / audio capability；
- $A_i$：Attention budget；
- $C_i$：Compute capability；
- $H_i$：Human input capability；
- $Q_i$：Privacy / security condition；
- $Z_i$：Spatial zone / role condition。

這使 UI 從固定頁面變成：

$$
\boxed{
Interface_t
=
F(
Intent_t,
Surface_t,
Attention_t,
Safety_t,
Privacy_t,
Network_t
)
}
$$

這個定義將在 Series B 的 Mobility / Spatial Continuum 中進一步展開。

---

# 7. Continuity Transition 與 Continuity Loss

定義一次 Surface／位置／網路遷移：

$$
\tau:
(\mathcal C_t,U_i,N_i)
\rightarrow
(\mathcal C_{t+1},U_j,N_j).
$$

理想目標不是要求所有位元狀態完全相同，而是要求與當前意圖相關的資訊不被不必要地遺失。

因此定義 Continuity Loss：

$$
L_C(\tau)
=
w_S L_S
+
w_X L_X
+
w_M L_M
+
w_P L_P
+
w_A L_A
+
w_H L_H,
$$

其中：

- $L_S$：Session loss；
- $L_X$：Context / task loss；
- $L_M$：Memory / artifact accessibility loss；
- $L_P$：Policy mismatch；
- $L_A$：Agent / tool availability loss；
- $L_H$：Human re-orientation cost。

研究目標為：

$$
\min L_C(\tau)
$$

subject to：

$$
Security(\tau)\ge\theta_S,
$$

$$
Privacy(\tau)\ge\theta_P,
$$

$$
Safety(\tau)\ge\theta_H.
$$

這意味著「越無縫越好」不是無條件目標。若無縫遷移必須犧牲安全或隱私，系統應選擇顯式重新授權。

---

# 8. 多模態不是功能清單，而是狀態的多種投影

常見產品把多模態理解為：

```text
聊天 + 語音 + 圖片 + 視訊
```

本文提出更強定義：

$$
\boxed{
\text{Multimodality}
=
\text{multiple valid representations of the same continuing intent state}
}
$$

例如同一份合約檢閱任務：

辦公室：

$$
\mathcal T
\rightarrow
\text{document + annotations + side-by-side AI}
$$

汽車後座：

$$
\mathcal T
\rightarrow
\text{large display + voice + call + AI notes}
$$

駕駛模式：

$$
\mathcal T
\rightarrow
\text{voice summary + deferred visual items}
$$

抵達會議室：

$$
\mathcal T
\rightarrow
\text{shared screen + meeting room + signed artifact}
$$

如果系統只是重新打開同一個 App，還不算完整 Continuum；只有當它理解「同一任務需要在不同 Surface 上被重新表達」時，才進入 AI-native 階段。

---

# 9. AI 的角色：不是通訊世界本身，而是 Runtime Intelligence

本文拒絕：

$$
\text{AI Model}
=
\text{User Communication World}.
$$

因為模型可能：

- 被更換；
- 被停用；
- 在本地或雲端之間切換；
- 因成本或隱私被降級；
- 由不同專門 Agent 分工；
- 因故障而不可用。

因此應採：

$$
\boxed{
\mathcal C
\not\subseteq
\text{Model Memory}
}
$$

而是：

$$
\boxed{
AI_1,AI_2,\ldots,AI_n
\rightarrow
\mathcal C
}
$$

AI 的主要職責包括：

1. **State Interpreter**：理解目前正在發生什麼；
2. **Context Compiler**：為新 Surface 編譯最小充分上下文；
3. **Modality Translator**：文字、語音、影像、文件及事件之間轉譯；
4. **Communication Planner**：選擇合法通道與接觸策略；
5. **Attention Broker**：依人類可用注意力決定通知、延遲、摘要或接管；
6. **Tool / Agent Router**：選擇模型、Agent、工具與 Provider；
7. **Continuity Guardian**：避免遷移造成未授權資料洩漏或狀態污染；
8. **Recovery Operator**：網路或 Provider 故障後恢復可驗證狀態。

---

# 10. Communication Intent：把「打電話」降階成執行方法

傳統操作：

```text
打開電話 App
→ 找人
→ 撥號
```

AI-native 層可以先表示：

$$
q
=
(
Target,
Intent,
Urgency,
Privacy,
Evidence,
Deadline,
HumanPresence
).
$$

然後求通道：

$$
ch^*
=
\arg\min_{ch\in\mathcal H}
J(ch\mid q,N_t,U_t,P_t).
$$

成本函數可以包含：

$$
J
=
\alpha L
+
\beta C
+
\gamma R
+
\delta A
+
\epsilon F,
$$

其中 $L$ 為延遲， $C$ 為成本， $R$ 為風險， $A$ 為注意力需求， $F$ 為失敗機率。

系統因此可以選擇：

- 直接通知本人；
- AI 先收集來意；
- 文字訊息；
- Email；
- 語音通話；
- 視訊會議；
- AI-to-AI 預協調；
- 延後處理；
- 草稿後請本人批准。

這裡的關鍵不是讓 AI 無限代替人，而是把「通訊方式」從 UI 選單變成受政策約束的執行規劃問題。

---

# 11. 網路路徑不應成為上層工作狀態的身份

現代即時通訊已經存在多種底層技術。WebRTC 提供瀏覽器與裝置間即時媒體與資料能力；QUIC 提供多路串流、低延遲建立與 network path migration；HTTP/3 建立在 QUIC 上；2026 年 7 月的 W3C WebTransport Candidate Recommendation Snapshot 已把可靠／不可靠資料、雙向／單向多串流能力帶到新的瀏覽器到伺服器介面；3GPP 的 ATSSS 持續處理多接取下的 traffic steering、switching 與 splitting。[R1][R2][R3][R4][R5]

因此 Continuum 的網路觀應為：

$$
\boxed{
\text{Application State}
\not\equiv
\text{Single Network Path}
}
$$

更高層可以表示：

$$
N_t
=
\{
n_1,n_2,\ldots,n_k
\},
$$

其中每條 path 具有：

$$
n_i
=
(
Bandwidth,
Latency,
Loss,
Cost,
Trust,
Mobility,
Energy
).
$$

Runtime 可以選擇、切換、拆分或等待，而上層 Session 盡量保持。

本文不主張所有網路都能做到完全 seamless handoff，也不主張有線與無線已沒有工程差異。本文只主張：**有線／無線／衛星／局域接取不應直接等同使用者的通訊身份與工作狀態。**

---

# 12. Event、Ledger 與 Canonical State

跨裝置 Continuum 若只依賴「把資料庫最新值同步過去」，會遇到衝突、刪除、權限、來源及重播問題。

Consumer Core 既有設計已使用接近 CloudEvents 的 Event Envelope，並區分 Event 與 Ledger。這個方向應保留。[R6]

本文增加一個原則：

$$
\boxed{
\text{Rendering State}
\neq
\text{Canonical State}
}
$$

UI 上看到的聊天、摘要、語音轉錄或工作卡片只是 projection。

Canonical state 應至少能回答：

- 這個狀態由誰建立；
- 來自哪一個 Session；
- 依哪個政策授權；
- 哪些資料是原始、哪些是推論；
- 哪個 Surface 可以看；
- 哪個 Agent 可以用；
- 是否被撤回；
- 是否被刪除；
- 是否存在新版本；
- 是否需要重新授權。

因此建議將 Continuity Event 寫成：

```json
{
  "type": "continuum.surface.transitioned",
  "continuum_id": "cc_...",
  "session_id": "ses_...",
  "from_surface": "desktop_...",
  "to_surface": "vehicle_...",
  "intent_ref": "intent_...",
  "policy_snapshot_ref": "policy_...",
  "context_revision": 42,
  "capability_profile": "VEHICLE_PASSENGER",
  "network_profile": "multi_access_...",
  "result": "RESUMED_WITH_ADAPTATION"
}
```

這不是規定最終 Schema，而是說明 Continuity 必須成為可觀察、可稽核的系統事件，而不能只是一個 UX 動畫。

---

# 13. Sovereign State Boundary：真正屬於人的應該是連續體狀態

如果通訊連續體全部存在某個單一模型供應商的聊天記錄裡，則：

$$
\text{Provider Failure}
\Rightarrow
\text{World Failure}.
$$

這不是好的基礎架構。

本文因此提出 **Sovereign State Boundary**：

$$
\boxed{
\mathcal C_{user}
\text{ must be logically separable from }
AIProvider
}
$$

其最低要求為：

- 身分不由單一 AI 模型定義；
- Session 可匯出或重建；
- Artifact 有獨立版本；
- Policy 是平台／使用者資料，而非 prompt 暗示；
- 長期記憶具有來源、scope 與刪除能力；
- Provider token / key 不進入事件原文；
- AI 可以替換而不抹除使用者狀態；
- 本地與雲端之間有明確同步與衝突政策。

這與 PAI Relay 的個人通訊入口權、Consumer Core 的 Local-first 與 Mode Isolation 可以直接接合。

---

# 14. 安全：連續體最大的風險正是「太連續」

Continuum 若設計錯誤，最大的危險不是斷線，而是把不該跨越的東西一起帶過去。

因此本文定義五個硬性隔離面。

## 14.1 Identity Isolation

角色身分、個人代理身分、企業服務身分不得因共用 Session Kernel 自動互換。

## 14.2 Memory Isolation

$$
Memory_{PERSONAL}
\not\rightarrow
Memory_{PERFORMANCE}
$$

除非存在顯式共享政策。

## 14.3 Capability Isolation

同一 AI 在不同 Surface 可以看到同一任務，但不代表擁有同一工具權限。

## 14.4 Attention Isolation

使用者在駕駛、睡眠、會議、休息與工作模式下的可打擾性不同。

PAI Relay 既有 Attention Firewall 因此可以升級成 Continuum 的通用 attention policy source，而非只服務電話與訊息。

## 14.5 Evidence Isolation

帳本可以保存決策與 hash reference，但不能因為要追蹤 Continuity 就永久複製所有原始私人內容。

此外，AI 風險治理可參照 NIST AI RMF 與 Generative AI Profile 對 Govern、Map、Measure、Manage 的框架，但 Continuum 必須把這些抽象治理要求落到實際的身份、政策、Surface、Session、Agent、工具與證據邊界。[R7]

---

# 15. 端對端安全與群組通訊

持續通訊世界若包含多人、多 Agent 與跨裝置 Room，群組加密與成員變更會成為重要問題。

IETF MLS RFC 9420 提供可擴展的非同步群組金鑰建立，並以 forward secrecy 與 post-compromise security 為主要安全目標；RFC 9750 進一步描述 MLS 架構及安全／隱私取捨。[R8][R9]

本文不宣稱 EVEMISS 現有產品已完成 MLS 整合，但提出：

$$
\boxed{
\text{Continuity membership}
\neq
\text{permanent decryption authority}
}
$$

換裝置、移除裝置、離開 Room、撤回 Agent 或切換模式時，都必須重新評估 cryptographic membership 與 application capability。

---

# 16. 與 AI-to-AI Communication 的關係

未來通訊不只有：

$$
Human_A
\leftrightarrow
Human_B.
$$

還會出現：

$$
Human_A
\leftrightarrow
Agent_A
\leftrightarrow
Agent_B
\leftrightarrow
Human_B.
$$

但 AI-to-AI 不能被理解為「兩個模型自由聊天」即可。

真正需要傳遞的是：

$$
\boxed{
\text{Identity}
+
\text{Intent}
+
\text{Authority}
+
\text{Scope}
+
\text{Evidence}
+
\text{Result Contract}
}
$$

例如 Agent A 可以被授權詢問 Agent B：

> 下週二下午是否存在雙方都可接受的會議時間？

但這不代表 Agent A 自動取得對方完整行事曆，也不代表 Agent B 可以替本人承諾其他事項。

因此 A2A communication 應是 Continuum 上的一種受契約約束的 channel，而不是新的無邊界人格代理。

---

# 17. 與工作、休閒及移動空間的關係

本文刻意不把 Communication Continuum 定義成 Work Continuum。

因為同一基礎設施可以支持：

$$
\mathcal E_t
\in
\{
WORK,
REST,
ENTERTAINMENT,
SOCIAL,
CREATOR,
PERSONAL\_RELAY
\}.
$$

當人在交通工具中移動，Continuum 只提供「活動可持續」的能力，不規定該活動必須是工作。

因此：

$$
\boxed{
\text{Capability to continue}
\neq
\text{obligation to continue working}
}
$$

這也形成與 Series B 的清楚接口：Series A 定義數位／通訊世界如何持續；Series B 研究汽車、飛機、robotaxi、房間等物理空間如何成為可程式化 Surface。

---

# 18. 三個核心不變量

## 18.1 Continuity Invariant

$$
\boxed{
\Delta Device
\lor
\Delta Location
\lor
\Delta Modality
\lor
\Delta Network
\lor
\Delta AIProvider
\not\Rightarrow
\operatorname{Reset}(I,S,X,P)
}
$$

除非政策明確要求重新驗證或重建。

## 18.2 Sovereignty Invariant

$$
\boxed{
\text{User-authorized canonical state}
\not\equiv
\text{single provider state}
}
$$

## 18.3 Isolation Invariant

$$
\boxed{
\text{Shared infrastructure}
\not\Rightarrow
\text{shared identity, memory, authority, or governance}
}
$$

這三條應成為整個 Series A 後續論文與工程的驗證錨點。

---

# 19. 研究假說

本文提出下列可驗證假說。

## H1：降低 Surface Transition Loss 能降低重新定向成本

若 Continuity Runtime 能保存任務、上下文及 Session，則從裝置 $u_i$ 切換到 $u_j$ 後，使用者重新進入有效狀態所需時間應下降。

定義：

$$
T_R
=
\text{time to resume meaningful interaction}.
$$

假說：

$$
T_R^{continuum}
<
T_R^{app\ silo}.
$$

## H2：模態自適應比介面複製更能降低注意力成本

若駕駛或低視覺 Surface 只把桌面 UI 原樣縮放，注意力成本不一定下降。

假說：

$$
A_C^{adaptive}
<
A_C^{screen\ mirroring}.
$$

## H3：Provider 可替換性提高長期狀態韌性

若 canonical state 與模型 Provider 解耦，則 Provider 故障或切換時的狀態損失較低。

## H4：顯式 Mode / Capability Isolation 能降低跨場景權限污染

例如 Personal Relay 與 Performance 使用不同 capability profile，應降低角色 Agent 誤取得現實代理權的概率。

## H5：通道意圖抽象可降低跨通道操作成本

當使用者以 Intent 而非 App 選擇來描述需求時，AI Communication Planner 可以減少重複步驟，但前提是高風險行動仍保留批准與可稽核性。

---

# 20. 評估框架

未來原型至少應測量以下指標。

## 20.1 Continuity Metrics

- Resume Time $T_R$ ；
- Context Recovery Accuracy；
- Session Preservation Rate；
- Artifact Availability Rate；
- Cross-device Conflict Rate；
- User Re-explanation Count。

## 20.2 Surface Adaptation Metrics

- Attention Cost；
- Task Completion Rate；
- Modality Switch Success；
- Unsafe Interaction Attempt Rate；
- Manual UI Navigation Count。

## 20.3 Network Metrics

- Path Switch Recovery Time；
- Packet / media interruption；
- offline queue durability；
- reconnection success；
- cross-access session survival。

## 20.4 Governance Metrics

- Unauthorized Memory Exposure；
- Capability Boundary Violation；
- Wrong-mode Action Rate；
- Ledger Completeness；
- Revocation Propagation Time；
- Human Takeover Success。

可以定義綜合連續性分數：

$$
Score_C
=
\lambda_1 Q_{resume}
+
\lambda_2 Q_{context}
+
\lambda_3 Q_{session}
+
\lambda_4 Q_{safety}
+
\lambda_5 Q_{privacy}
-
\lambda_6 C_{human\ reorientation}.
$$

但正式 benchmark 應避免用單一總分掩蓋安全與隱私失敗，因此安全類指標應保留硬性門檻。

---

# 21. 第一版參考架構

本文建議 Series A 的工程參考架構暫定為：

```text
[Application Layer]
PAI Relay
Virtual Character Stage
VoiceDesk
MailGuard
Future Personal Office / Solo Relay

[Adaptive Surface Layer]
Desktop Adapter
Mobile Adapter
Vehicle Adapter
Aircraft Adapter
Room / Display Adapter
Voice-only Adapter

[Continuity Runtime]
Continuum Identity
Intent Graph
Session Resume
Context Compiler
Modality Adapter
Attention Broker
Capability Binder
Agent / Tool Router
Transition Ledger
Conflict Resolver

[State & Governance]
Consumer Core
ECAC-compatible low-level services
Memory / Artifact
Policy / Rights
Ledger / Evidence
Local-first Sync

[Communication Core]
OUCC
Room / Presence
Messaging
Realtime Media
WebRTC / WebTransport-capable transports

[Network / Physical Layer]
Ethernet / Fiber
Wi-Fi
Cellular
Satellite
Relay / Hybrid Networks
```

這是一個研究參考分層，不代表所有模組都必須成為獨立微服務。

相反地，延續既有虛擬角色平台與 Consumer Core 的工程原則，第一版原型應優先採 **modular monolith + clear contracts**，等負載、團隊與部署需求真的要求時再拆分。

---

# 22. 與既有產品的責任矩陣

| 模組 | 主要責任 | 是否被 Continuity Runtime 取代 |
|---|---|---:|
| OUCC | Room、Presence、Messaging、WebRTC、Transport | 否 |
| Consumer Core | Identity、Device、Provider、Session、Memory、Ledger、Mode | 否 |
| PAI Relay | 個人入口權、Attention、Delegation、Call/Message Relay | 否 |
| ECAC | 企業 Tenant、Policy、Risk、Ledger、Human Control | 否 |
| VoiceDesk | 企業語音任務執行 | 否 |
| MailGuard | 企業郵件風險治理 | 否 |
| Enterprise Suite | 跨產品案例、證據、發布治理 | 否 |
| Virtual Character Stage | 角色、導演、舞台、表演 Runtime | 否 |
| Continuity Runtime | 跨 Surface 狀態、上下文、模態與 Session 延續 | 新增 |

因此本文的架構策略是：

$$
\boxed{
\text{Add a missing continuity layer}
\neq
\text{collapse all products into one system}
}
$$

---

# 23. 與既有網路標準的相容策略

Series A 不應重新發明成熟的 transport protocol。

建議採：

- 即時點對點／媒體優先使用 WebRTC 相容技術；[R1]
- 新型 browser-to-server 低延遲資料流可評估 WebTransport，但必須依其標準成熟度與實作狀態逐版驗證；[R4]
- transport 層可利用 QUIC 的 path migration 與 multiplexing 能力，但不可把 application continuity 誤等同於 QUIC connection continuity；[R2]
- event envelope 可延續 CloudEvents-like 結構，但 EVEMISS 的 mode、privacy、trace、continuum 等欄位應由自己的版本化 Schema 定義；[R6]
- 群組端對端安全可評估 MLS，而不是自創未審查的群組金鑰協定；[R8][R9]
- 多接取與 network steering 應把 3GPP ATSSS 等現有機制視為可利用 backend，而非假定由應用層自行取代電信網路控制。[R5]

---

# 24. 本文不主張的事情

為避免理論膨脹，本文明確不主張：

1. 所有通訊 App 都應被消滅；
2. 所有網路都已經能做到零中斷 handoff；
3. AI 是通訊連續性的必要條件；
4. AI 應該自動讀取使用者所有私人資料；
5. 同一帳號代表所有裝置擁有相同權限；
6. 同一 Room 代表所有 Agent 共享完整記憶；
7. 角色人格可以自動成為現實代理；
8. AI-to-AI communication 可以繞過本人授權；
9. WebRTC、WebTransport、QUIC、MLS 或 ATSSS 中任何一項單獨等同本文架構；
10. 「無縫」的重要性高於安全、隱私與人類主權。

---

# 25. Series A 後續論文位置

本篇只建立母架構與研究問題。後續六篇依序展開：

**A-02｜Persistent Communication State**  
正式定義 Identity、Session、Context、Task、Memory、Artifact 與跨裝置 canonical state。

**A-03｜Multimodal-Native Communication**  
研究文字、語音、視訊、文件、Agent、螢幕與空間介面的統一表示與投影。

**A-04｜AI Communication Runtime**  
研究 AI 如何成為 planner、router、operator、attention broker 與 continuity guardian。

**A-05｜Adaptive Hybrid Communication Fabric**  
研究 fiber、RF、Wi-Fi、cellular、satellite、relay、frequency / phase / carrier abstraction，並與 FARHP、SPAL、FAL-MCI、SPFC 的物理／語義通訊研究線接合。

**A-06｜Personal Communication Sovereignty**  
研究 canonical state、個人記憶、權限、加密、可攜性、Provider independence 與可撤回性。

**A-07｜EVEMISS Communication Continuum Architecture**  
技術白皮書，將 OUCC、Consumer Core、PAI Relay、ECAC、VoiceDesk、MailGuard、Virtual Character Stage 與 Continuity Runtime 映射為實作 roadmap。

Series B 將另處理 Programmable Mobility & Spatial Continuum；Bridge-01 再建立兩系列的統一接口。

---

# 26. 結論

本文最核心的轉換可以濃縮為：

$$
\boxed{
\text{Communication}
:
\text{Channel-Centric}
\rightarrow
\text{State-Centric}
\rightarrow
\text{Continuum-Centric}
}
$$

第一階段的通訊系統解決「如何把訊息送出去」。

第二階段的雲端系統解決「如何讓資料在多裝置可取得」。

AI-native 階段需要進一步解決：

> **當人、Agent、設備、網路與物理位置持續變動時，如何讓一個被授權的通訊世界仍然保持可辨識、可恢復、可轉譯、可治理與可接管？**

因此本文提出：

$$
\boxed{
\text{Physical or technical transition}
\not\Rightarrow
\text{communication-world reset}
}
$$

但同時必須成立：

$$
\boxed{
\text{Continuity}
\not\Rightarrow
\text{universal access}
}
$$

真正成熟的 Communication Continuum 不是「所有資料到處流動」，而是：**屬於人的通訊狀態可以持續存在，而每一個新場景只取得當下合法、必要且安全的投影。**

這也是本文與既有 EVEMISS 通訊工程之間的最重要關係：OUCC、Consumer Core、PAI Relay、ECAC、VoiceDesk、MailGuard 與多智能體平台已經提供大量可回收的底層與上層能力；現在缺少的不是另一個聊天 App，而是一個把這些能力跨時空維持起來的 Continuity Runtime。

---

# 參考文獻

## 外部標準與公開資料

[R1] W3C, *WebRTC: Real-Time Communication in Browsers*, W3C Recommendation, 13 March 2025. https://www.w3.org/TR/webrtc/

[R2] J. Iyengar and M. Thomson, *QUIC: A UDP-Based Multiplexed and Secure Transport*, RFC 9000, IETF, May 2021. https://www.rfc-editor.org/rfc/rfc9000.html

[R3] M. Bishop, *HTTP/3*, RFC 9114, IETF, June 2022. https://www.rfc-editor.org/rfc/rfc9114.html

[R4] W3C, *WebTransport*, Candidate Recommendation Snapshot, 30 July 2026. https://www.w3.org/TR/2026/CR-webtransport-20260730/

[R5] 3GPP, *TS 23.501 — System architecture for the 5G System*, ATSSS related work and Release 18/19 updates. https://portal.3gpp.org/

[R6] Cloud Native Computing Foundation, *CloudEvents Specification v1.0.2*. https://github.com/cloudevents/spec

[R7] NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1, July 2024, updated publication record 2026. https://doi.org/10.6028/NIST.AI.600-1

[R8] R. Barnes et al., *The Messaging Layer Security Protocol*, RFC 9420, IETF, July 2023. https://www.rfc-editor.org/rfc/rfc9420.html

[R9] B. Beurdouche et al., *The Messaging Layer Security Architecture*, RFC 9750, IETF, April 2025. https://www.rfc-editor.org/rfc/rfc9750.html

## EVEMISS 前置文件

[E1] `EVEMISS_企業通訊智能產品線_v0.1`，2026-07-30。

[E2] `EVEMISS_ECAC_MVP_v0.1`，2026-07-30。

[E3] `EVEMISS_Enterprise_Communication_Suite_Integration_v0.7`，2026-07-31。

[E4] `EVEMISS_VoiceDesk_Production_Operations_Governance_v0.6`，2026-07-31。

[E5] `EVEMISS_MailGuard_Authorized_Staging_Calibration_v0.6`，2026-07-31。

[E6] `EVEMISS_PAI_Relay_個人AI通訊代理技術白皮書_v0.2`，2026-07-31。

[E7] `EVEMISS_消費端通訊與角色智能共用核心_架構規劃_v0.1`，2026-07-31。

[E8] `EVEMISS_虛擬角色多智能體表演與交流平台_產品定位與系統邊界_v0.1`，2026-07-31。

[E9] `EVEMISS_虛擬角色多智能體表演與交流平台_技術白皮書_v0.1`，2026-07-31。

[E10] `EVEMISS_虛擬角色多智能體表演與交流平台_MVP實作規劃_v0.1`，2026-07-31。

[E11] `EMPSL_v0.1_論文與統一編碼規格包`，2026-07-31。

[E12] `LRC-COL_Special_II_SPAL_Spectral-Phase_Acoustic_AI-Native_Language_v0.2_UBE_Corrected_2026-08-21.md`。

[E13] `LRC-COL_Special_III_Frequency-Agile_Language_and_Machine-Capability_Inheritance_v0.1_2026-08-21.md`。

[E14] `LRC-COL_Hidden_Special_SPFC_Semantic-to-Physical_Field_Compilation_Conjecture_v0.1_2026-08-21.md`。

---

**A-01 結束。**
