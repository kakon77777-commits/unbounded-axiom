---
title: "Multimodal-Native Communication：文字、語音、影像、文件、Agent 與 Surface 的統一投影"
subtitle: "Series A-03｜Multimodal-Native Communication: Unified Projection of Text, Voice, Visual Media, Artifacts, Agents, and Surfaces"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Draft / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series A｜AI-Native Communication Continuum"
series_number: "A-03"
document_type: "Research Paper"
canonical_source: true
encoding: "UTF-8"
---

# Multimodal-Native Communication：文字、語音、影像、文件、Agent 與 Surface 的統一投影

## Series A-03｜Multimodal-Native Communication: Unified Projection of Text, Voice, Visual Media, Artifacts, Agents, and Surfaces

**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Draft / Canonical Source  

---

# 摘要

Series A-01 提出 AI-Native Communication Continuum，將通訊重新定義為可跨裝置、位置、網路、AI Provider 與應用持續存在的授權世界；A-02 進一步以 Persistent Communication State（PCS）形式化身分、Room、Session、Context、Task、Memory、Artifact、Agent、Permission 與 Governance 的持續狀態。本文處理下一個必要問題：**同一持續狀態如何在不同裝置、空間與注意力條件下，以不同模態被安全而有效地呈現、接收與操作？**

本文主張，Multimodal-Native Communication 不等於「同時開啟文字、語音、影像、視訊與所有感測器」，也不等於替每個裝置製作一個獨立版本的 App。其核心是將 **語義／任務狀態** 與 **表達模態** 解耦，讓同一個 Communication Intent 能依 Surface capability、可用注意力、隱私、網路品質、角色、安全限制與使用者偏好，被編譯為不同的輸入／輸出／操作計畫。

本文定義一個 Surface Context：

$$
\mathcal U_{u,t}
=
(
C_u,
B_{u,t},
E_{u,t},
N_{u,t},
H_u,
P_{u,t},
Q_{u,t}
),
$$

其中 $C_u$ 為硬體與介面能力， $B_{u,t}$ 為可用注意力預算， $E_{u,t}$ 為環境狀態， $N_{u,t}$ 為網路條件， $H_u$ 為人因／可及性偏好， $P_{u,t}$ 為授權與政策， $Q_{u,t}$ 為當下品質與風險狀態。給定 A-02 的 Persistent Communication State $\mathcal P_t$ 與 Communication Intent $\mathcal J_t$，Multimodal Projection Operator 定義為：

$$
\boxed{
\mathcal Y_{u,t}
=
\Pi_{MM}
(
\mathcal P_t,
\mathcal J_t;
\mathcal U_{u,t}
)
}
$$

其中 $\mathcal Y_{u,t}$ 不是畫面，而是一個 **Modality Plan**，描述可用輸入、輸出、互動深度、AI 代辦程度、內容降階策略與安全限制。

本文再提出四個不變量。第一，**Semantic Invariance**：跨 Surface 投影可以改變媒介，但不應偷偷改變核心任務語義與授權語義。第二，**Source Preservation**：語音轉錄、影像描述、文件摘要與 AI 壓縮都屬 derivative representation，除非明確指定，不能覆蓋原始 Artifact 或 source-of-record。第三，**Attention-Safety Constraint**：模態選擇必須服從使用者角色與環境的注意力／安全限制，例如車輛駕駛態中不可因為系統「支援大螢幕」就允許高視覺負荷工作。第四，**Privacy-Audience Constraint**：同一資訊在耳機、私人螢幕、客廳電視、車載揚聲器或會議室投影上的可揭露內容不應相同。

本文把 multimodality 拆成五個彼此正交的概念：Modality、Channel、Surface、Transport、Action Plane。文字、語音、圖像與視訊是模態；電話、Room、Email 與即時會議可視為通訊通道；手機、桌面、車載、耳機與會議室是 Surface；5G、Wi-Fi、WebRTC、HTTP/3、衛星或其他網路是 Transport；Agent 代辦、工具執行與環境控制則屬 Action Plane。這種分離避免「語音 = 電話」「車載 = 語音」「視訊 = WebRTC」等產品層綁死。

本文進一步建立：多模態轉譯損失、跨 Surface 分散式組合、media provenance、降階傳輸階梯、attention gating、role-aware projection、driver/passenger separation、accessibility substitution、AI barge-in 與 human takeover、Modality Capability Negotiation、Projection Manifest，以及一組可驗證指標。對 EVEMISS 而言，OUCC 繼續負責 Room、Presence、Messaging 與 Realtime Transport；Consumer Core 提供 Identity、Device、Session、Realtime Media、Memory、Artifact 與 Mode Isolation；PAI Relay 提供 Attention Firewall、CommunicationSession 與接管政策；虛擬角色平台提供多角色 Media Pipeline 與語音互動；VoiceDesk／MailGuard 維持企業治理。A-03 不合併這些產品，而是建立共用的 **Multimodal Projection Contract**。

本文最終提出：

$$
\boxed{
\text{Same State}
\not\Rightarrow
\text{Same Interface},
}
$$

但同時要求：

$$
\boxed{
\text{Different Interface}
\not\Rightarrow
\text{Different Work Identity}.
}
$$

這使桌面、手機、耳機、車載、飛機、會議室與未來空間介面可以成為同一 AI-Native Communication Continuum 的不同投影面，而不是彼此割裂的新世界。

**關鍵詞：** Multimodal-Native Communication；Surface Projection；Modality Plan；Persistent Communication State；Attention Budget；Driver Distraction；Voice；Video；Artifact；WebRTC；WebCodecs；Accessibility；AI Agent；Communication Continuum；EVEMISS

---

# Abstract

This paper formalizes the multimodal projection layer of the AI-Native Communication Continuum. It argues that multimodal-native communication is not the simultaneous activation of every available medium. Instead, it separates persistent semantic and task state from the modalities through which that state is rendered, captured, and acted upon.

For each interaction surface, the paper defines a Surface Context consisting of hardware capabilities, available attention, environmental state, network conditions, human-factor and accessibility preferences, permission state, and quality or risk constraints. A Multimodal Projection Operator maps Persistent Communication State and Communication Intent into a Modality Plan that specifies allowed input and output modes, interaction depth, AI delegation, degradation behavior, and safety constraints.

The model introduces four core invariants: semantic invariance across projections, preservation of source artifacts and provenance, attention and safety constraints, and privacy-aware audience constraints. It explicitly distinguishes modality, communication channel, surface, network transport, and action plane, preventing architectural coupling such as treating speech as equivalent to telephony or treating a vehicle surface as inherently voice-only.

The paper further defines multimodal translation loss, role-aware projection, distributed surface composition, provenance-preserving renditions, graceful degradation under constrained networks, accessibility substitution, agent and human takeover paths, modality capability negotiation, projection manifests, and evaluation metrics. It maps the model onto existing EVEMISS components without collapsing the governance boundaries among PAI Relay, virtual-character systems, VoiceDesk, MailGuard, and other communication products.

The resulting architecture allows the same persistent communication state to move across desktop, mobile, headset, vehicle, aircraft, meeting-room, and future spatial surfaces while changing its interface safely and intentionally rather than resetting the work or communication identity.

---

# 0. 研究問題：為什麼「支援很多媒體」仍然不等於 Multimodal-Native？

今日大量通訊產品已經支援：

- 文字；
- 語音訊息；
- 電話；
- 視訊；
- 圖片；
- 文件；
- 螢幕分享；
- 表情與反應；
- AI 摘要。

但典型系統仍然是：

```text
text feature
voice feature
video feature
file feature
AI feature
```

它們只是被放在同一 App 裡。

真正的 Multimodal-Native 應該回答：

> **當同一個人、同一個 Session、同一個任務與同一組 Artifact 從桌面轉移到手機、耳機、汽車、飛機或會議室時，系統如何知道哪些資訊要改成語音、哪些必須保留視覺、哪些應該延後、哪些可以交給 AI、哪些必須禁止？**

若系統只是把桌面 UI 縮小到車載螢幕，或把完整 PDF 用 TTS 從頭念到尾，都不能稱為真正的 multimodal-native adaptation。

因此本文第一個命題是：

$$
\boxed{
\text{Multimedia Feature Set}
\neq
\text{Multimodal-Native Architecture}
}
$$

---

# 1. 五個概念必須分開：Modality、Channel、Surface、Transport、Action Plane

## 1.1 Modality

Modality 是資訊被感知或表達的形式。

輸入模態可包含：

$$
\mathcal M_{in}
=
\{
text,
speech,
touch,
gesture,
camera,
screen,
document,
sensor
\}.
$$

輸出模態可包含：

$$
\mathcal M_{out}
=
\{
text,
audio,
speech,
image,
video,
projection,
haptic,
spatial\ audio
\}.
$$

模態描述「怎麼被表達／接收」，不是「從哪條網路走」。

## 1.2 Channel

Channel 是社會或應用層通訊路徑，例如：

- Room；
- 電話；
- Email；
- 即時訊息；
- 視訊會議；
- agent-to-agent session。

同一個 Channel 可以使用多個 Modality。

例如一場即時會議可以同時有：

$$
text+audio+video+screen+artifact.
$$

## 1.3 Surface

Surface 是人或 Agent 當下實際互動的介面／空間載體。

例如：

$$
\mathcal S
=
\{
Desktop,
Phone,
Headset,
Vehicle,
Aircraft,
MeetingRoom,
TV,
AR,
Wearable
\}.
$$

Surface 不等於 Device ID。

一台汽車裡可能同時存在：

- driver surface；
- passenger surface；
- rear-seat display；
- private headset；
- shared cabin audio。

因此 Surface 是一個 **interaction scope**，而不只是硬體名稱。

## 1.4 Transport

Transport 是資料如何在網路或本地路徑中傳遞。

例如：

$$
\mathcal T
=
\{
WiFi,
5G,
Satellite,
Ethernet,
WebRTC,
QUIC,
HTTP,
LocalIPC
\}.
$$

A-03 刻意規定：

$$
\boxed{
Modality
\perp
Transport
}
$$

即兩者在架構上應可獨立替換。

語音不必綁定 PSTN；文字不必綁定 HTTP；視訊不必綁定單一 Provider。

## 1.5 Action Plane

AI 時代還需要第五層：

$$
\boxed{
\text{Action Plane}
}
$$

例如：

- AI 代為撥號；
- 建立會議；
- 打開 Artifact；
- 將畫面投影到後座螢幕；
- 將訊息改成耳機私密播放；
- 暫停高注意力工作；
- 保存 checkpoint；
- 在授權下執行工具。

Agent action 不是「又一種媒體」。

它是：

$$
\text{Communication State}
\rightarrow
\text{Authorized Operation}.
$$

---

# 2. Communication Intent：先保留意圖，再選模態

傳統通訊介面常把使用者動作直接綁在媒體上：

```text
打電話
傳訊息
開視訊
寄 Email
```

Multimodal-Native Runtime 更適合保存一個較高階的 Communication Intent：

$$
\boxed{
\mathcal J_t
=
(
g,
target,
content,
urgency,
privacy,
interaction,
deadline,
authority
)
}
$$

其中：

- $g$：目標；
- $target$：對象；
- $content$：欲傳達或處理的內容；
- $urgency$：時間敏感度；
- $privacy$：隱私需求；
- $interaction$：需要同步、非同步、確認或談判；
- $deadline$：截止條件；
- $authority$：允許 AI 做到哪一層。

例如：

```text
目標：確認合約第 7 條
對象：對方窗口
時限：今天 17:00 前
互動：需要對方明確確認
權限：AI 可整理與草擬，不可代表本人承諾
```

Runtime 才決定：

$$
\text{Email}
\rightarrow
\text{Message}
\rightarrow
\text{Voice Call}
\rightarrow
\text{Meeting}
$$

哪一條最適合。

A-03 不要求系統永遠自動決定通道，而是要求 **Intent 與 Modality / Channel 解耦**。

---

# 3. Surface Context：同一個人不是永遠有同樣的介面能力

對 Surface $u$，定義：

$$
\boxed{
\mathcal U_{u,t}
=
(
C_u,
B_{u,t},
E_{u,t},
N_{u,t},
H_u,
P_{u,t},
Q_{u,t}
)
}
$$

## 3.1 Capability $C_u$

例如：

- display size；
- microphone；
- camera；
- speaker；
- headset；
- keyboard；
- touch；
- projector；
- haptics；
- spatial audio；
- secure enclave；
- local compute；
- sensor availability。

## 3.2 Attention Budget $B_{u,t}$

注意力不是固定常數。

可以抽象為：

$$
B_{u,t}
=
(
b_v,
b_a,
b_m,
b_c
),
$$

其中：

- $b_v$：可用視覺注意力；
- $b_a$：可用聽覺注意力；
- $b_m$：可用手部／操作資源；
- $b_c$：可用認知複雜度預算。

同一個人在辦公桌前與駕駛中， $B_{u,t}$ 完全不同。

## 3.3 Environment $E_{u,t}$

例如：

- private room；
- public transport；
- moving vehicle；
- meeting room；
- aircraft cabin；
- noisy environment；
- shared display environment。

## 3.4 Network $N_{u,t}$

至少包含：

$$
N_{u,t}
=
(
bandwidth,
latency,
jitter,
loss,
continuity,
cost
).
$$

## 3.5 Human Factors $H_u$

包含使用者明確設定的：

- 字級；
- 語音速度；
- captions；
- transcript；
- 色彩／對比；
- 輸入偏好；
- accessibility needs；
- 語言與翻譯偏好。

這些不應被 AI 當成可隨意推測的個人屬性；應由使用者設定、裝置能力與合法可用的輔助資訊決定。

## 3.6 Permission $P_{u,t}$

「裝置有相機」不等於「這個 Session 可以開相機」。

因此：

$$
Capability=1
\not\Rightarrow
Permission=1.
$$

## 3.7 Quality / Risk $Q_{u,t}$

包含：

- ASR confidence；
- speaker identification confidence；
- environment privacy confidence；
- device trust；
- role certainty；
- safety state；
- media quality。

---

# 4. Multimodal Projection Operator

給定 A-02 的 Persistent Communication State：

$$
\mathcal P_t
=
(
I_t,R_t,S_t,X_t,T_t,M_t,F_t,A_t,P_t,G_t
),
$$

以及 Communication Intent $\mathcal J_t$ 與 Surface Context $\mathcal U_{u,t}$，定義：

$$
\boxed{
\mathcal Y_{u,t}
=
\Pi_{MM}
(
\mathcal P_t,
\mathcal J_t;
\mathcal U_{u,t}
)
}
$$

其中：

$$
\mathcal Y_{u,t}
=
(
M^{in},
M^{out},
D,
A,
K,
\Gamma
)
$$

- $M^{in}$：允許輸入模態；
- $M^{out}$：允許輸出模態；
- $D$：互動深度；
- $A$：AI delegation／action plan；
- $K$：降階／替代策略；
- $\Gamma$：安全、隱私、權限與品質約束。

所以一個 Surface Profile 不是「介面主題」，而是：

$$
\boxed{
\text{Current Interaction Contract}
}
$$

---

# 5. Same State 不代表 Same Interface

假設同一個任務狀態是：

```text
正在審閱一份合約
爭議點：第 7 條付款條件
AI 已比對兩版差異
下一步：取得本人確認後才可回覆
```

桌面 Surface 可以投影為：

```text
雙欄 diff
原始 PDF
AI 分析
歷史對話
可編輯回覆草稿
```

耳機 Surface 可以投影為：

```text
15 秒摘要
逐條語音問答
必要時播讀原句
不可顯示版面資訊
```

車輛 passenger Surface 可以是：

```text
大螢幕 diff + 語音操作 + private audio
```

駕駛 Surface 則可能只能：

```text
高層摘要
延後視覺內容
只允許低風險語音命令
```

因此：

$$
\boxed{
\mathcal P_t=\text{constant}
\quad\not\Rightarrow\quad
\mathcal Y_{u,t}=\text{constant}
}
$$

這正是 continuum 的必要條件，而不是例外。

---

# 6. Semantic Invariance：投影可以變，核心語義不可偷偷漂移

定義原始工作語義：

$$
\Sigma_t
=
Sem(
\mathcal P_t,
\mathcal J_t
).
$$

Surface 投影後的可恢復語義為：

$$
\hat{\Sigma}_{u,t}
=
Sem(
\mathcal Y_{u,t}
).
$$

要求：

$$
\boxed{
d_{sem}
(
\Sigma_t,
\hat{\Sigma}_{u,t}
)
\le
\epsilon_{u,t}
}
$$

但 $\epsilon_{u,t}$ 不可能永遠為零。

例如：

- 圖表轉語音會失去部分空間資訊；
- 音訊轉 transcript 會失去部分韻律、重音與音色；
- 長文件轉摘要會失去細節；
- 影像描述無法保證重建所有視覺關係。

因此 Multimodal Runtime 必須知道：

$$
\boxed{
\text{Modality Conversion is potentially lossy.}
}
$$

如果預估損失過高，正確動作可能不是「努力轉換」，而是：

$$
\boxed{
DEFER
}
$$

例如：

> 「這一段需要看圖與公式。已保存到 checkpoint；抵達可使用螢幕的 Surface 後再繼續。」

這是一個成功的 continuity 行為，不是功能失敗。

---

# 7. Source Preservation：Transcript、Summary 與 Description 都不是原始物件

A-03 定義每一個多媒體資訊單位至少可有：

$$
\boxed{
O_j
=
(
source,
derivatives,
provenance,
confidence,
rights,
policy
)
}
$$

例如一段真人語音：

```text
source_audio.wav
├─ transcript.txt
├─ summary.md
├─ translated_text.txt
└─ embeddings / derived features
```

其中：

$$
source\ audio
\neq
transcript.
$$

同理：

$$
PDF
\neq
AI\ summary,
$$

$$
Image
\neq
AI\ description.
$$

因此系統不得因為 Surface 目前只能使用文字，就把 transcript 當成原始語音的 canonical replacement。

A-03 使用兩個概念：

- **Source-of-record**：原始或具有正式證據地位的 Artifact；
- **Rendition**：為特定 Surface 生成的表示。

定義：

$$
\rho_{j,u,m}
=
Render
(
O_j,
Surface_u,
Modality_m
).
$$

Rendition 必須保留：

- source_ref；
- transform_type；
- model / tool provenance；
- generated_at；
- confidence（若適用）；
- reversibility / loss note。

---

# 8. 多模態轉譯損失

對模態轉換：

$$
T_{a\rightarrow b}
:
M_a
\rightarrow
M_b,
$$

定義：

$$
\boxed{
\mathcal L_{a\rightarrow b}
=
\alpha L_{sem}
+
\beta L_{structure}
+
\gamma L_{provenance}
+
\delta L_{timing}
}
$$

其中：

- $L_{sem}$：語義內容損失；
- $L_{structure}$：空間、版面、關係結構損失；
- $L_{provenance}$：來源與證據鏈損失；
- $L_{timing}$：時間與節奏資訊損失。

因此「能轉成語音」不代表「應該轉成語音」。

對高精度工作，系統應允許：

$$
\mathcal L_{a\rightarrow b}
>
\tau
\Rightarrow
\text{Defer / Request Better Surface}.
$$

---

# 9. Multimodal-Native 不等於 All-Modal

定義所有可用模態：

$$
\mathcal M_{avail}.
$$

真正啟用集合應為：

$$
\boxed{
\mathcal M^*_{u,t}
\subseteq
\mathcal M_{avail}
}
$$

並由下式決定：

$$
\mathcal M^*_{u,t}
=
\arg\max_{\mathcal M}
\left[
U_{task}
+
U_{experience}
+
U_{access}
-
C_{attention}
-
C_{privacy}
-
C_{network}
\right]
$$

subject to：

$$
Risk(\mathcal M)
\le
R_{max},
$$

$$
Permission(\mathcal M)=1.
$$

這裡最重要的是 hard constraint。

如果一種模態安全上不可用：

$$
Permission(visual)=0,
$$

則再高的工作效率都不能把它重新加回去。

---

# 10. Attention-Safety Constraint

## 10.1 注意力是一種 runtime resource

A-03 將注意力視為有限資源：

$$
\boxed{
B_{att}(t)
<
\infty
}
$$

因此 Multimodal Runtime 的任務不是最大化刺激量，而是配置注意力。

## 10.2 車輛只是最明顯案例

現代車載平台已經將 driver-distraction restrictions 當作正式平台限制；例如 Android Automotive OS 對 parked app 與 driving state 使用不同 UX restriction，並要求在駕駛限制生效時阻止不合適活動。A-03 不把任何特定平台規則提升為普世標準，但採納其背後工程原則：

$$
\boxed{
\text{Surface capability}
\neq
\text{current usable capability}
}
$$

因此同一塊螢幕：

```text
vehicle parked       → rich visual interaction may be allowed
vehicle passenger    → passenger surface policy
vehicle driver active→ strict distraction policy
```

必須是不同的 Projection Contract。

## 10.3 Driver / Passenger role 不可混淆

A-03 要求：

$$
\boxed{
Role(driver)
\neq
Role(passenger)
}
$$

而且系統不能只靠「人在車裡」判斷。

應結合：

- 明確座位／使用者角色；
- 車輛運行狀態；
- 平台 safety signal；
- UI scope；
- policy gate。

若角色不確定，應採保守策略。

這一部分只建立通訊投影契約；完整 Spatial Attention Zones 留待 Series B-04。

---

# 11. Privacy-Audience Constraint

同一個 Session 的 Surface 可能從私人桌面轉到公共空間。

定義當前可感知受眾：

$$
Audience_{u,t}.
$$

要求：

$$
\boxed{
Disclosure
(
\mathcal Y_{u,t}
)
\subseteq
AuthorizedAudience
(
\mathcal P_t
)
}
$$

例如：

- 私人耳機可播敏感語音；
- 車內共享揚聲器不可自動播報敏感 Email；
- 會議室投影不能自動顯示私人通知；
- 公共場所手機可以降階成震動＋摘要；
- 共享電視應預設更嚴格的內容過濾。

因此 privacy 不只是「資料有沒有加密」，還包括：

$$
\boxed{
\text{Who can perceive this rendering right now?}
}
$$

---

# 12. 多 Surface 組合：一個 Session 可以同時跨多個 Surface

Multimodal-Native 不能假設：

$$
1\ user
=
1\ device
=
1\ surface.
$$

實際上可以：

```text
Laptop        → visual document
Headset       → private audio
Phone         → authentication / haptic
Room display  → shared presentation
AI agent      → background analysis
```

所以同一時間的有效投影可寫成：

$$
\boxed{
\mathcal Y_t
=
\bigcup_{u\in U_t}
\mathcal Y_{u,t}
}
$$

但 union 並不代表所有 Surface 都能看到相同資料。

每個 Surface 仍各自受：

$$
P_{u,t},
Audience_{u,t},
B_{u,t}
$$

約束。

這使「大螢幕 + 耳機 + 手機」可以成為一個完整 interaction composition，而不用把全部功能塞進單一裝置。

---

# 13. Surface Profiles

以下 Profile 是研究基線，不是硬編碼產品清單。

## 13.1 Desktop Surface

典型特徵：

$$
B_v\uparrow,
\quad
B_m\uparrow,
\quad
Display\uparrow.
$$

適合：

- 長文；
- 文件 diff；
- 多窗格；
- 複雜視覺；
- 精細編輯；
- 多 Agent observability。

## 13.2 Mobile Surface

特徵：

- 可攜；
- 小螢幕；
- touch / voice；
- camera；
- 高環境變動。

適合短週期控制、身份確認、訊息、拍攝與 handoff。

## 13.3 Headset / Earbud Surface

主要能力：

$$
Audio
+
VoiceInput
+
OptionalHaptic.
$$

適合：

- 低視覺負荷；
- 私密語音；
- 摘要；
- 即時指令；
- continuity prompt。

但不適合高密度圖表／版面精讀。

## 13.4 Vehicle Driver Surface

核心原則：

$$
\boxed{
Safety
\succ
Productivity
}
$$

應由平台／車輛狀態限制：

- 允許的視覺負荷；
- 互動步驟；
- 輸入長度；
- 通知優先級；
- 是否可啟動某類工作。

## 13.5 Vehicle Passenger / Rear Surface

如果乘客與駕駛已被可靠區分，後座 Surface 可以具有完全不同的 capability policy：

- large display；
- projection；
- keyboard；
- full video；
- private audio；
- work / entertainment mode。

這正是 Series B 將繼續研究的 programmable cabin。

## 13.6 Meeting Room Surface

特徵是：

$$
Audience>1.
$$

所以核心不是「螢幕大」，而是：

- participant binding；
- shared / private separation；
- presenter role；
- transcript consent；
- shared artifact scope。

## 13.7 Aircraft / Long-Duration Mobility Surface

若具有穩定網路與私人座位，可接近工作 Surface；若網路不穩，則需更強 offline cache、checkpoint 與 degradation plan。

---

# 14. Voice-Native 不是 Voice-Only

EVEMISS 既有 Realtime Media Core 已包含：

- Audio Input；
- VAD；
- Streaming ASR；
- Streaming TTS；
- Audio Queue；
- Mark / Clear；
- Barge-in；
- First Audio Latency；
- Provider Rollover；
- Session Statistics。

A-03 在其上增加的不是另一套語音引擎，而是 **voice projection semantics**。

## 14.1 Voice Input

語音輸入事件至少應區分：

$$
\boxed{
\text{Raw Audio}
\rightarrow
\text{Transcript}
\rightarrow
\text{Interpretation}
\rightarrow
\text{Intent}
}
$$

四層不能混為同一物件。

## 14.2 Barge-in

使用者插話時，系統可能需要：

```text
stop current TTS
preserve source response
mark playback offset
capture user speech
replan turn
```

不能直接把「停止播放」等同「刪掉回答」。

## 14.3 Voice Confirmation

高風險操作不能因為語音自然就降低確認門檻。

例如：

$$
\text{Speech Ease}
\not\Rightarrow
\text{Authority Expansion}.
$$

---

# 15. Image、Video、Screen 與 Document 不應被壓成同一種「視覺」

## 15.1 Image

Image 可以：

- 作為 source Artifact；
- 被 AI 描述；
- 被標註；
- 被局部裁切；
- 在不同 Surface 降解析度。

但 image description 是 derivative。

## 15.2 Video

Video 包含時間結構。

因此：

$$
Video
\neq
SequenceOfIndependentImages.
$$

若 Surface 無法播放視訊，可以改為：

- audio-only；
- keyframe summary；
- transcript；
- defer。

但必須標註 loss。

## 15.3 Screen Share

Screen share 具有額外的 privacy risk。

A-03 建議 Surface Runtime 支援：

- window-level share；
- region share；
- privacy redaction；
- notification suppression；
- shared cursor / annotation；
- explicit stop state。

## 15.4 Document

文件不是「很多文字」。

它可能包含：

$$
text
+
layout
+
figures
+
tables
+
formulas
+
comments
+
version\ semantics.
$$

因此 document-to-speech 最多只是 projection，不是等價替代。

---

# 16. Accessibility Substitution：多模態不是奢侈功能，而是可及性基礎

多模態架構天然支持 substitution：

$$
Audio
\leftrightarrow
Text,
$$

$$
Visual
\leftrightarrow
Description,
$$

$$
SpeechInput
\leftrightarrow
Keyboard,
$$

$$
NotificationSound
\leftrightarrow
Haptic.
$$

W3C WCAG 對 captions、media alternatives 與 audio description 的要求提供一個既有工程錨點：不同使用者需要不同方式取得相同或足夠等價的資訊。

A-03 不宣稱自動 AI 轉換必然滿足 accessibility conformance。

相反地，系統必須保留：

- 人工 caption；
- verified transcript；
- accessibility metadata；
- human override；
- source provenance。

AI 可以降低轉換成本，但不能以「有 AI 描述」取代所有可及性責任。

---

# 17. Network-Aware Graceful Degradation

多模態 continuity 必須接受網路不是永遠足夠。

假設需求：

$$
video
+
audio
+
screen
+
artifact\ sync.
$$

當 $N_{u,t}$ 惡化時，不應直接：

$$
Session\ Reset.
$$

而應啟動降階階梯：

```text
4K video
→ lower bitrate video
→ audio + low-rate keyframes
→ audio only
→ text / transcript
→ asynchronous queue
→ checkpoint + offline
```

定義 degradation path：

$$
K
=
(m_0,m_1,\ldots,m_n).
$$

要求：

$$
Utility(m_{i+1})
<
Utility(m_i),
$$

但：

$$
Continuity(m_{i+1})
\approx
Continuity(m_i)
$$

在可接受語義範圍內盡量維持。

這個模型與 A-05 的 Adaptive Hybrid Communication Fabric 相接，但 A-03 只處理「網路變差時模態如何降階」。

---

# 18. AI 作為 Projection Planner，而不是另一個聊天視窗

AI 在 A-03 的角色可以包含：

- Context summarizer；
- Modality converter；
- Attention-aware renderer；
- privacy-aware redactor；
- task decomposer；
- channel advisor；
- speech interface；
- background operator。

但它不應直接擁有全部 authority。

因此：

$$
\boxed{
AI\ Projection\ Authority
\subseteq
User\ Granted\ Authority
}
$$

例如 AI 可以決定：

> 「這個圖表目前不適合用語音解釋，先存到稍後。」

但不能因此自行決定：

> 「我替你簽了。」

Projection Planner 與 Action Authority 必須分層。

---

# 19. Projection Manifest

每次重要 Surface attach / handoff 可以生成一個最小 Projection Manifest：

```yaml
projection_id: prj_...
session_id: ses_...
surface_id: srf_...
actor_id: act_...
role: passenger
surface_profile: vehicle_rear
input_modalities:
  - voice
  - touch
  - keyboard
output_modalities:
  - large_display
  - private_audio
  - text
attention_budget:
  visual: high
  audio: high
  manual: medium
privacy:
  audience: private
  shared_speaker: false
network_profile:
  class: variable_broadband
fallback_order:
  - video
  - audio
  - text
blocked_capabilities:
  - external_commit_without_confirmation
source_preservation: required
```

這個 Manifest 不是永久個人設定，而是當下 runtime contract。

---

# 20. Surface Attach / Handoff Protocol

A-03 建議最小流程：

```text
1. Surface discovered
2. Device / actor authentication
3. Role binding
4. Capability negotiation
5. Environment / audience classification
6. Attention / safety gate
7. Permission evaluation
8. PCS resume descriptor load
9. Modality plan compile
10. User-visible handoff cue
11. Projection activate
12. Continuous re-evaluation
```

形式化：

$$
\mathcal P_t
\xrightarrow{attach(u)}
\mathcal U_{u,t}
\xrightarrow{compile}
\mathcal Y_{u,t}.
$$

若 Surface 狀態變動，例如車子從 parked 轉為 moving：

$$
\mathcal U_{u,t}
\neq
\mathcal U_{u,t+1},
$$

則必須重新編譯：

$$
\boxed{
\mathcal Y_{u,t+1}
=
\Pi_{MM}
(
\mathcal P_{t+1},
\mathcal J_{t+1};
\mathcal U_{u,t+1}
)
}
$$

而不是沿用舊 UI。

---

# 21. Modality Switching 不是 Session Switching

一個重要 invariant：

$$
\boxed{
\Delta Modality
\not\Rightarrow
\Delta Session
}
$$

例如：

```text
text chat
→ voice conversation
→ video call
→ document review
→ text summary
```

都可以屬於同一 Session，前提是：

- actor identity 連續；
- room / relation 連續；
- task identity 連續；
- authority 連續或可解釋演化；
- artifact lineage 連續。

反之，即使還在同一個 App 裡，只要上述關係被切斷，也可能已經是新的 Session。

---

# 22. Cross-Modal Event Model

A-03 建議 event 不以 rendering 作為唯一 identity。

例如：

$$
EventID=e_{1024}
$$

可以有：

```text
semantic event
├─ original voice artifact
├─ transcript rendition
├─ text summary rendition
├─ translated rendition
└─ screen card rendition
```

所以：

$$
\boxed{
1\ semantic\ event
\rightarrow
N\ renditions
}
$$

每個 rendition 可以獨立：

- generated；
- cached；
- deleted；
- regenerated；
- re-rendered；

但不能因此破壞原 event 的 identity 與 evidence linkage。

---

# 23. Human Takeover 與 AI Handoff

PAI Relay 已有 handoff state；VoiceDesk 亦有人工接管概念。

A-03 將其一般化。

AI 可以在某 Surface 主導低風險互動：

$$
AI\ Active.
$$

當使用者接管：

$$
AI\ Active
\rightarrow
Human\ Takeover.
$$

Runtime 必須保留：

- last committed event；
- AI pending draft；
- media playback position；
- external party state；
- permission state；
- tool action state。

不能把 handoff 簡化成「關閉 AI 麥克風」。

---

# 24. EVEMISS 既有架構映射

A-03 不建立全新的產品內核，而是把既有元件分工正式化。

## 24.1 OUCC

持續負責：

- Room；
- Presence；
- Messaging；
- WebRTC / realtime communication；
- transport-facing primitives。

## 24.2 Consumer Core

既有：

- Identity & Device；
- Session & Event Kernel；
- Realtime Media；
- Agent Session Kernel；
- Memory & Context；
- Artifact；
- Mode Isolation。

A-03 建議新增共用 contract：

```text
Surface Registry
Capability Profile
Projection Manifest
Rendition Metadata
Attention / Safety Signal Interface
Audience / Privacy Scope
Modality Degradation Policy
```

## 24.3 PAI Relay

保留：

- Attention Firewall；
- CommunicationSession；
- handoff state；
- Delegation Policy；
- Relationship Memory；
- PersonalRiskCase。

A-03 為它提供跨 Surface projection，而不把私人代理政策下放給其他產品。

## 24.4 Virtual Character / Multi-Agent Platform

既有 Media Pipeline、voice mapping、session interruption 與多角色演出能力可重用底層 media primitives。

但：

$$
\boxed{
Performance\ Identity
\neq
Personal\ Relay\ Identity
}
$$

角色語音、表演記憶與娛樂權限不得因共用 Multimodal Runtime 自動進入現實代理域。

## 24.5 VoiceDesk / MailGuard

企業產品可重用 Surface／Rendition／handoff primitives，但企業：

- tenant；
- RBAC；
- Case；
- Evidence；
- release governance；

仍由 ECAC 與各自產品治理，不被 Consumer Core 取代。

---

# 25. 既有標準如何支撐這個方向，但不等於本文架構

## 25.1 WebRTC

W3C 於 2025-03-13 發布更新的 WebRTC Recommendation，提供瀏覽器間即時媒體與 application data 的標準 API。它證明 audio／video／data 已可在共同 realtime framework 中協同，但 WebRTC 本身不定義本文的 Persistent State、Surface Projection 或 Attention Policy。

## 25.2 Media Capture and Streams

W3C Media Capture and Streams 將 microphone、camera 等 local media capture 與 MediaStream 抽象化。這為 capability-based media handling 提供成熟底層，但不負責「何時應該啟用何種模態」。

## 25.3 WebCodecs

W3C WebCodecs 在 2026 年持續更新 Working Draft，提供 audio、video、image codec 的低階介面。這支持應用更精細地控制 media pipeline，但同樣不是 multimodal intent runtime。

## 25.4 Android for Cars

2026 年 Android for Cars 文件仍明確區分 parked app 與 driving restrictions，並以 UX restriction 防止不適合駕駛時操作的功能。A-03 將其視為「context-dependent capability gating」的實際工程例證，而不是把 Android 規則直接複製為跨平台標準。

## 25.5 WCAG 2.2

WCAG 2.2 對 captions、media alternatives 與 audio description 的規範顯示，一份資訊需要多種表示才能服務不同感知需求。A-03 將 accessibility 視為 Multimodal-Native 的核心需求之一，而非事後補丁。

---

# 26. 評估指標

A-03 提出至少七組指標。

## 26.1 Semantic Projection Fidelity

$$
F_{sem}
=
1-d_{sem}
(
\Sigma_t,
\hat{\Sigma}_{u,t}
).
$$

## 26.2 Projection Adaptation Latency

$$
L_{adapt}
=
t_{usable\ projection}
-
t_{surface\ attach}.
$$

## 26.3 Modality Conversion Loss

$$
L_{modal}
=
\mathcal L_{a\rightarrow b}.
$$

## 26.4 Attention Violation Rate

$$
V_{att}
=
\frac{
\#\ unsafe\ or\ over-budget\ projections
}{
\#\ projection\ decisions
}.
$$

理想目標：

$$
V_{att}\rightarrow0.
$$

## 26.5 Privacy Exposure Rate

$$
V_{priv}
=
\frac{
\#\ unauthorized\ audience\ exposures
}{
\#\ rendered\ sensitive\ events
}.
$$

## 26.6 Handoff Continuity

$$
F_{handoff}
=
1-
\mathcal L_C
(
Before,
After
).
$$

其中 $\mathcal L_C$ 延續 A-02 Continuity Loss。

## 26.7 Source Traceability

每個 derivative rendition 應能追到 source：

$$
Traceable(\rho_j)
\in
\{0,1\}.
$$

正式工作流應要求：

$$
Traceable(\rho_j)=1.
$$

---

# 27. 可證偽命題

## 命題 A03-P1

若任務狀態與表達模態解耦，則跨 Surface handoff 的 task-resume time 應低於重新開啟獨立 App 與人工重建 context 的基線。

## 命題 A03-P2

若 Projection Runtime 同時使用 attention budget 與 environment policy，則在不降低必要訊息到達率的條件下，unsafe interaction attempts 應低於固定 UI 基線。

## 命題 A03-P3

若 source-of-record 與 derivative rendition 被分離，則 AI 摘要／轉錄造成的 provenance confusion rate 應顯著下降。

## 命題 A03-P4

在變動網路下，具有 modality degradation ladder 的 Session，其 continuity completion rate 應高於「媒體品質不足即斷線／重啟」基線。

## 命題 A03-P5

對需要 accessibility substitution 的使用者，Surface-aware multimodal projection 應能降低完成同一任務所需的額外人工轉換步驟。

這些都是可測試命題，不是本文已經完成的人體實驗結論。

---

# 28. 最小實作建議

A-03 不要求第一版就支援所有 Surface。

最小實作可以只做：

```text
Surface Registry
├─ desktop
├─ mobile
└─ headset / voice

Projection Engine
├─ text → text
├─ text → speech
├─ speech → transcript
├─ document → summary + source link
└─ network degradation policy
```

再加：

```text
role
attention_level
privacy_scope
source_ref
rendition_ref
handoff_checkpoint
```

第一輪測試應先證明：

$$
Desktop
\rightarrow
Mobile
\rightarrow
Voice
\rightarrow
Desktop
$$

過程中同一 Session、Task、Artifact 與 authority 不會被重置。

車載 Surface 可以先使用 emulator／policy profile，不需要一開始就取得真車硬體。

---

# 29. 與 A-04 的接口

A-03 已經定義：

- Persistent State 的多模態投影；
- Surface Context；
- Communication Intent；
- Modality Plan；
- Attention／Privacy／Safety constraints；
- degradation；
- handoff；
- source preservation。

但尚未完整回答：

> **誰負責在多個可用通道、Agent、工具與 Surface 之間做規劃？**

因此 A-04 將進入：

# **AI Communication Runtime**

並正式拆出：

- Planner；
- Router；
- Operator；
- Attention Broker；
- Continuity Guardian；
- Escalation / Human Review；
- Tool and Channel Policy。

A-03 提供 Projection Contract；A-04 提供真正執行該 Contract 的智能 runtime。

---

# 30. 限制與研究邊界

本文不主張：

1. 所有資訊都可以無損跨模態轉換；
2. AI 可以可靠推斷所有人的注意力、隱私或 accessibility needs；
3. 車載語音就一定安全；
4. 語音比螢幕天然更低認知負荷；
5. 所有裝置都應長時間保持在線；
6. 所有媒體都應交給雲端 AI 處理；
7. WebRTC、WebCodecs 或 Android Automotive 已經等價於本文架構；
8. 多模態投影可以繞過作業系統、道路安全、隱私、錄音或企業治理規則；
9. transcript、summary 或 AI description 可以無條件取代 source artifact；
10. Continuum 的價值等於要求使用者隨時工作。

本文只提出一個工程方向：

$$
\boxed{
\text{Persistent State}
+
\text{Surface-Aware Projection}
+
\text{Policy-Constrained Multimodality}
}
$$

可以比「每個裝置一個 App、每個媒體一個功能」更適合作為 AI 時代通訊軟體的上層架構。

---

# 結論

A-01 將通訊從 App／Channel 拉到持續世界；A-02 將這個世界落成 Persistent Communication State；A-03 再回答：同一個世界如何在不同物理與數位介面上被看見、聽見、操作與安全地延續。

本文最核心的兩個式子是：

$$
\boxed{
\text{Same State}
\not\Rightarrow
\text{Same Interface}
}
$$

以及：

$$
\boxed{
\text{Different Interface}
\not\Rightarrow
\text{Different Work Identity}
}
$$

桌面適合視覺密集工作；手機適合快速接管；耳機適合低視覺負荷；車載駕駛 Surface 必須服從安全限制；後座或長途交通 Surface 可以成為完整工作／娛樂介面；會議室則需要多人 Audience 與 shared/private 分離。真正的 Multimodal-Native Communication 不是強迫所有空間長成同一個 UI，而是讓同一個 Persistent Communication State 根據 Surface Context 被重新編譯。

因此本文將 AI-native communication 的介面層從：

$$
\text{App}
\rightarrow
\text{Fixed UI}
$$

推進為：

$$
\boxed{
\text{Persistent State}
\rightarrow
\text{Communication Intent}
\rightarrow
\text{Multimodal Projection Runtime}
\rightarrow
\text{Surface-Specific Experience}
}
$$

這個結構也為 Series B 的移動時空研究建立必要橋樑：未來汽車、飛機與其他交通空間不需要成為新的資訊孤島；它們只需要成為同一 Continuum 中新的 Surface。

---

# 參考文獻與標準錨點

1. W3C, **WebRTC: Real-Time Communication in Browsers**, Recommendation, 13 March 2025. `https://www.w3.org/TR/webrtc/`
2. W3C, **Media Capture and Streams**, Candidate Recommendation Draft, 9 October 2025. `https://www.w3.org/TR/mediacapture-streams/`
3. W3C, **WebCodecs**, Working Draft, 8 July 2026. `https://www.w3.org/TR/webcodecs/`
4. Android Developers, **Build parked apps for cars / Android Automotive OS driver distraction requirements**, current documentation checked 2026-08-24. `https://developer.android.com/training/cars/parked`
5. Android Developers, **Car app quality / Driver Distraction**, current documentation checked 2026-08-24. `https://developer.android.com/docs/quality-guidelines/car-app-quality`
6. W3C, **Web Content Accessibility Guidelines (WCAG) 2.2**. `https://www.w3.org/TR/WCAG22/`
7. EVEMISS, **消費端通訊與角色智能共用核心：架構規劃 v0.1**, 2026-07-31.
8. EVEMISS, **PAI Relay：個人 AI 通訊代理技術白皮書 v0.2**.
9. EVEMISS, **虛擬角色多智能體表演與交流平台：技術白皮書 v0.1**.
10. EVEMISS, **Enterprise Communication Suite Integration v0.7**.
11. EVEMISS, **A-01 AI-Native Communication Continuum v0.1**, 2026-08-24.
12. EVEMISS, **A-02 Persistent Communication State v0.1**, 2026-08-24.

---

# 文件狀態

本文件為 Series A-03 v0.1 canonical research source。

下一篇：

**A-04｜AI Communication Runtime：Planner、Router、Operator、Attention Broker 與 Continuity Guardian**。
