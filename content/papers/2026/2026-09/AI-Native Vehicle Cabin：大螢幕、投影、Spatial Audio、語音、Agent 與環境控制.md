---
title: "AI-Native Vehicle Cabin：大螢幕、投影、Spatial Audio、語音、Agent 與環境控制"
subtitle: "AI-Native Vehicle Cabin: A Multimodal Runtime Architecture for Displays, Projection, Spatial Audio, Agents, and Environmental Control"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Paper / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series B｜Programmable Mobility & Spatial Continuum"
series_number: "B-05"
canonical_source: true
encoding: "UTF-8"
---

# AI-Native Vehicle Cabin：大螢幕、投影、Spatial Audio、語音、Agent 與環境控制

## AI-Native Vehicle Cabin: A Multimodal Runtime Architecture for Displays, Projection, Spatial Audio, Agents, and Environmental Control

**系列：** Series B｜Programmable Mobility & Spatial Continuum  
**編號：** B-05  
**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Paper / Canonical Source  

---

# 摘要

B-01 將交通工具重新定義為 Programmable Mobility Space；B-02 將交通時間拆解為可回收與可配置的活動時間；B-03 定義 Mobility Cognitive Continuity 與 Mobility Resume Capsule；B-04 則建立 Spatial Attention Zones，要求所有車內互動先通過角色、安全、注意力、隱私與權限約束。本篇將前四篇真正組裝成一個可實作的車艙執行層：

# **AI-Native Vehicle Cabin（ANVC）**
## **AI 原生多模態車艙**

本文主張，「AI-native cabin」不是在傳統 infotainment 上多加一個聊天機器人，也不是把所有控制都交給一個 LLM。它是一套把：

- display；
- projection；
- audio；
- microphone；
- speech；
- camera / occupant sensing；
- seat；
- lighting；
- climate；
- privacy devices；
- communication continuity；
- AI agents；
- network / cloud；
- vehicle-safe cabin controls；

統合成可被意圖、活動狀態與 Zone Contract 編排的 runtime。

本文定義：

$$
\boxed{
\mathcal K_t
=
(
D_t,
Q_t,
H_t,
M_t,
E_t,
A_t,
C_t,
Z_t,
P_t,
S_t
)
}
$$

其中：

- $D_t$：display / visual surfaces；
- $Q_t$：projection / augmented visual output；
- $H_t$：audio / spatial sound zones；
- $M_t$：microphone / speech input；
- $E_t$：environment actuators；
- $A_t$：AI / agent runtime；
- $C_t$：communication / continuity state；
- $Z_t$：Spatial Attention Zone contracts；
- $P_t$：privacy / authority；
- $S_t$：safety / vehicle-state boundary。

本文第一個核心命題是：

$$
\boxed{
\text{Cabin Intelligence}
\neq
\text{Driving Authority}.
}
$$

2026 年的產業工程已清楚呈現「車艙 AI」與「駕駛／自動駕駛」可以共存但必須分層：NVIDIA 的 in-vehicle AI agent architecture 明確包含 ASR、orchestrator、LLM/VLM、tool use、TTS、edge / cloud pipeline 與 policy enforcement；Qualcomm Snapdragon Cockpit 平台則提供 multimodal LLM、多高解析度顯示、zonal audio、active noise / echo cancellation、driver monitoring 與 edge AI；Mercedes 2026 年也推進 on-device speech、language understanding 與 reasoning。這些能力證明「車艙本身成為 AI compute / multimodal runtime」已是現代工程方向，但不代表 cabin agent 應直接取得 safety-critical driving control。

本文第二個核心命題是：

$$
\boxed{
\text{Intent}
\rightarrow
\text{Experience Compiler}
\rightarrow
\text{Zone-Constrained Cabin Plan}
\rightarrow
\text{Bounded Actuation}.
}
$$

使用者不需要指定：

> 把第 3 號燈調到 18%，把右後座音響 gain 調多少。

他可以表達：

> 我要休息。

或：

> 我要繼續工作。

Experience Compiler 將高階意圖轉成 Cabin Experience Plan，再由 B-04 的 Zone Contract、安全政策、能力註冊表與 actuator contract 決定哪些控制允許執行。

第三個核心命題是：

$$
\boxed{
\text{Multimodal}
\neq
\text{Everything On}.
}
$$

成熟車艙不應同時把所有 display、speaker、mic、camera、AI notification 全開，而是依 activity、seat、privacy、motion、attention、network 與 safety 選擇最小充分模態。若人在 driver zone，dense PDF 可能被轉成簡短語音或 defer；若在 rear passenger zone，則可恢復完整大螢幕、鍵盤與私有音訊。

第四個核心命題是：

$$
\boxed{
\text{Environment}
=
\text{First-Class Output Surface}.
}
$$

當系統可以控制 lighting、seat posture、temperature、airflow、privacy glass、audio field、display、projection 與 notification 時，UI 已不再只存在於螢幕。車艙環境本身成為一個可程式輸出域。這使 Work、Rest、Entertainment、Social、Creative、Idle 等 activity mode 可以被編譯成不同的 physical / digital state。

本文提出 **Experience Intent、Cabin Capability Registry、Cabin Experience Plan、Cabin Control Contract、Actuation Receipt、Zone Binding、Device Driver Boundary、Edge/Cloud AI Split、Graceful Degradation、Shared-Vehicle Teardown** 等核心規格，並給出 Work、Rest、Entertainment、Social 與 Agent-Only 五個參考 profile。

本文最終將車艙 runtime 收斂為：

$$
\boxed{
Intent
\rightarrow
ActivityState
\rightarrow
MRC
\rightarrow
ZoneDecision
\rightarrow
ExperiencePlan
\rightarrow
CabinActuation
\rightarrow
Evidence.
}
$$

B-06 將在這個技術執行層之上研究 Mobility Hospitality 與 Robotaxi Economy：當車艙不再只是「有沒有冷氣、有沒有司機」，而是具有不同可程式時空品質時，移動服務如何形成新的產品分級、定價與旅程價值。

---

# Abstract

An AI-native vehicle cabin is not merely an infotainment system with a conversational model attached. It is a multimodal runtime that coordinates displays, projection, audio zones, microphones, speech, environmental controls, AI agents, communication continuity, privacy, and vehicle-safe actuators under explicit spatial-attention and safety constraints.

This paper introduces the AI-Native Vehicle Cabin (ANVC) architecture. It treats the cabin as a set of programmable output and input surfaces governed by an Experience Compiler. High-level human intent such as WORK, REST, ENTERTAINMENT, SOCIAL, or IDLE is compiled into a zone-constrained Cabin Experience Plan. The plan is then translated through bounded device contracts rather than exposing raw vehicle control interfaces directly to an AI model.

The architecture explicitly separates cabin intelligence from driving authority. Current 2026 industry systems already demonstrate many required primitives: agentic multimodal AI pipelines, edge-cloud orchestration, multiple high-resolution displays, zonal audio, active noise control, conversational AI, contextual personalization, and on-device speech / language reasoning. These are treated as engineering anchors, not as proof that a complete programmable mobility space already exists.

The paper defines a Cabin Capability Registry, Experience Intent, Cabin Experience Plan, Cabin Control Contract, Actuation Receipt, edge/cloud execution split, graceful degradation, and shared-vehicle teardown. It also establishes that the physical environment itself is a first-class output surface: lighting, seat posture, climate, airflow, privacy glass, audio fields, and visual surfaces may all participate in a cabin mode.

The resulting runtime composes B-03's Mobility Resume Capsule and B-04's Zone Contract into an executable cabin state. Series B-06 then uses this technical foundation to model Mobility Hospitality and robotaxi service differentiation.

---

# 0. 車艙不是一個 App

傳統思維：

$$
\boxed{
VehicleCabin
=
InfotainmentSystem.
}
$$

本文改寫：

$$
\boxed{
VehicleCabin
=
\text{Programmable Multimodal Environment}.
}
$$

Infotainment 只是其中一個子系統。

---

# 1. AI-Native 不等於裝一個 Chatbot

如果：

```text
Existing IVI
+ Chat Window
```

那只是：

$$
\boxed{
AI-Enhanced Infotainment.
}
$$

真正 AI-native cabin 必須讓 AI Runtime 能理解：

- occupant；
- activity；
- zone；
- privacy；
- network；
- cabin capability；
- safety；
- continuity state。

---

# 2. 車艙狀態

定義：

$$
\boxed{
\mathcal K_t
=
(
D_t,
Q_t,
H_t,
M_t,
E_t,
A_t,
C_t,
Z_t,
P_t,
S_t
).
}
$$

---

# 3. $D_t$ — Display Surfaces

包括：

- center display；
- passenger display；
- rear display；
- foldable display；
- seatback display；
- ceiling display；
- personal display；
- wearable display。

---

# 4. $Q_t$ — Projection / Augmented Visual Surface

包括：

- HUD；
- windshield projection；
- panoramic projection；
- cabin projection；
- AR overlay。

BMW Panoramic iDrive 等現代系統已經展示：

$$
\boxed{
\text{Windshield / Panoramic Visual Surface}
}
$$

不再只是傳統儀表。

---

# 5. $H_t$ — Audio / Spatial Sound

包括：

- multi-channel audio；
- zonal audio；
- headrest speakers；
- spatial audio；
- ANC；
- echo cancellation；
- masking；
- private audio。

Qualcomm Snapdragon Cockpit 目前直接列出：

- premium sound；
- zonal audio；
- active noise / echo cancellation。

---

# 6. $M_t$ — Microphone / Speech

包括：

- cabin microphone；
- seat microphone；
- beamformed microphone；
- wake-word；
- VAD；
- ASR；
- barge-in；
- speech diarization；
- privacy capture policy。

---

# 7. $E_t$ — Environment Actuators

包括：

- lighting；
- seat position；
- seat heating / cooling；
- climate；
- airflow；
- window；
- privacy glass；
- ambient sound；
- display brightness；
- physical partition if available。

---

# 8. $A_t$ — AI / Agent Runtime

包括：

- local model；
- cloud model；
- ASR；
- TTS；
- VLM；
- planner；
- tool router；
- personal agent；
- cabin agent；
- continuity guardian。

---

# 9. $C_t$ — Communication / Continuity

承接 Series A：

- identity；
- session；
- task；
- memory；
- artifact；
- provider；
- network；
- authority。

---

# 10. $Z_t$ — Spatial Attention Zones

承接 B-04。

Zone 決定：

- 哪個 Surface；
- 哪個 modality；
- 哪種 complexity；
- 哪個 authority；

此刻可用。

---

# 11. $P_t$ — Privacy / Authority

包括：

- audience；
- data class；
- local retention；
- personal account；
- cabin sharing；
- control scope；
- teardown。

---

# 12. $S_t$ — Safety Boundary

包括：

- driving state；
- occupant role；
- motion；
- emergency；
- OEM safety policy；
- certified restrictions。

---

# 13. Cabin Intelligence ≠ Driving Authority

本篇最重要：

$$
\boxed{
CabinIntelligence
\neq
DrivingAuthority.
}
$$

即使 vehicle compute 越來越 centralized，

也不代表 software authority 必須合併。

---

# 14. Central Compute ≠ Central Authority

2026 Qualcomm 已展示：

- cockpit；
- driver assistance；
- body；
- connectivity；

跨 domain central compute。

但：

$$
\boxed{
SharedCompute
\neq
SharedAuthority.
}
$$

這是 architecture safety principle。

---

# 15. Why This Matters

如果 cabin agent：

> 幫我快一點。

不能直接：

$$
\rightarrow
ThrottleControl.
$$

它最多形成：

$$
\boxed{
TravelPreferenceIntent.
}
$$

再交由合法 driving / navigation system 處理。

---

# 16. Experience Compiler

定義：

$$
\boxed{
\mathcal C_E:
(
Intent,
Activity,
MRC,
Zone,
Capability
)
\rightarrow
ExperiencePlan.
}
$$

---

# 17. Experience Intent

例如：

```yaml
intent: "REST"
duration_min: 40
privacy: "private"
allow_interruptions:
  emergency: true
  work: false
preferred:
  light: "low"
  audio: "quiet"
  seat: "reclined"
```

---

# 18. Work Intent

```yaml
intent: "WORK"
activity_ref: "paper_17"
resume_capsule: "mrc_123"
preferred:
  display: "large"
  audio: "private"
  input:
    - "voice"
    - "keyboard"
network_priority: "interactive"
```

---

# 19. Experience Plan

Compiler output：

```yaml
plan_id: "xp_..."
zone_id: "rear_right"
activity_mode: "WORK"
visual:
  target_display: "rear_private_main"
  layout: "document_focus"
audio:
  zone: "rear_right_headrest"
  mode: "private"
input:
  voice: true
  keyboard: true
environment:
  light: "work_neutral"
  seat: "upright"
  climate: "personal_profile"
notification:
  work: "normal"
  personal: "summary"
```

---

# 20. Plan 不是 Raw Command

Experience Plan：

$$
\boxed{
\text{Declarative}
}
$$

而不是：

```text
GPIO 4 = HIGH
CAN 0x123 = ...
```

---

# 21. Cabin Control Contract

Plan 之下：

$$
\boxed{
ExperiencePlan
\rightarrow
CabinControlContract
}
$$

每個 actuator 必須宣告：

- capability；
- range；
- safety class；
- owner；
- authority；
- rollback；
- evidence。

---

# 22. Capability Registry

例如：

```yaml
capability_id: "seat.recline"
zone_scope:
  - "rear_right"
range:
  min: 0
  max: 35
safety_class: "CABIN_COMFORT"
requires:
  occupant_detected: true
  seatbelt_policy: "compatible"
```

---

# 23. Display Capability

```yaml
capability_id: "display.rear_private_main"
resolution: "4K"
input_modes:
  - "touch"
  - "keyboard"
privacy_class: "PRIVATE"
driver_exposure: "LOW"
```

---

# 24. Audio Capability

```yaml
capability_id: "audio.headrest_rr"
zone: "rear_right"
features:
  - "zonal_playback"
  - "anc"
  - "echo_cancel"
leakage_class: "MEDIUM"
```

---

# 25. AI Capability

```yaml
capability_id: "ai.cabin_agent"
execution:
  - "edge"
  - "cloud"
inputs:
  - "speech"
  - "context"
  - "telemetry"
allowed_actions:
  - "cabin_comfort"
  - "media"
  - "communication_intent"
forbidden_actions:
  - "raw_driving_control"
```

---

# 26. Industry Primitive：Multimodal LLM

Qualcomm Cockpit 目前直接把：

$$
\boxed{
\text{Multimodal LLMs}
}
$$

列為 cockpit capability。

其 personalization 可以結合：

- user；
- context；
- voice；
- touch；
- audio。

---

# 27. Industry Primitive：Multiple High-Res Displays

Snapdragon Cockpit 平台列出：

- front displays；
- rear displays；
- high-resolution graphics。

2026 Leapmotor / Qualcomm centralized solution 甚至支援：

$$
\boxed{
8\ displays.
}
$$

---

# 28. Industry Primitive：18-Channel Audio

同一 2026 platform 宣稱：

$$
\boxed{
18\text{-channel audio}
}
$$

作為 immersive in-car entertainment 的能力。

這不等於 personal sound zone 完成，

但硬體自由度已經很高。

---

# 29. Industry Primitive：Agentic AI

NVIDIA 2026 明確描述：

$$
\boxed{
\text{Rule-Based Command}
\rightarrow
\text{Agentic Multimodal AI}.
}
$$

包含：

- reasoning；
- planning；
- acting；
- memory；
- multimodal；
- proactive；
- personalized。

---

# 30. NVIDIA Agent Pipeline

其代表性 pipeline：

$$
\boxed{
ASR
\rightarrow
Orchestrator
\rightarrow
LLM/VLM
\rightarrow
Tools
\rightarrow
TTS.
}
$$

並可：

$$
Edge
\leftrightarrow
Cloud.
$$

---

# 31. Edge AI Box 的意義

NVIDIA 2026 還提出：

> 既有 IVI 可透過獨立 AI Box 升級 agentic AI。

這對 PMS 很重要。

因為：

$$
\boxed{
\text{Cabin AI Upgrade}
}
$$

不一定要求整台車從零重新設計。

---

# 32. 這與我們早先「舊車也可以」一致

弱版本：

$$
ExistingVehicle
+
Compute
+
Display
+
Network
+
AIBox
$$

就可以建立部分：

$$
ANVC.
$$

---

# 33. 新車則可以 Zonal / Central Architecture

新一代 SDV：

- central compute；
- zonal controllers；
- OTA；
- service-oriented architecture。

更適合：

$$
\boxed{
Capability Registry.
}
$$

---

# 34. Mercedes On-Device AI

2026 Mercedes + Liquid AI：

- on-device speech；
- language understanding；
- reasoning；
- privacy；
- reduced cloud dependence。

所以：

$$
\boxed{
Cabin AI
\neq
Cloud-Only AI.
}
$$

---

# 35. Edge / Cloud Split

定義：

$$
\boxed{
A_t
=
A_t^{edge}
\oplus
A_t^{cloud}.
}
$$

---

# 36. Edge Responsibilities

優先：

- wake word；
- basic ASR；
- privacy-sensitive inference；
- cabin controls；
- low-latency command；
- offline fallback；
- safety-related gating。

---

# 37. Cloud Responsibilities

適合：

- deep research；
- large-model reasoning；
- external search；
- enterprise access；
- long-context analysis；
- cross-device continuity。

---

# 38. Cloud Failure

若：

$$
Cloud=Unavailable,
$$

車艙不能：

$$
\rightarrow
\text{Dead}.
$$

應降階。

---

# 39. Graceful Degradation

例如：

$$
CloudAgent
\rightarrow
EdgeAgent
\rightarrow
RuleBasedControl
\rightarrow
ManualControl.
$$

---

# 40. Modality Degradation

網路差：

$$
Video
\rightarrow
Audio
\rightarrow
Text
\rightarrow
OfflineState.
$$

但：

$$
\boxed{
Authority
}
$$

不能降階。

---

# 41. Multimodal ≠ Everything On

成熟：

$$
\boxed{
\text{Minimum Sufficient Modality}.
}
$$

不是：

$$
\boxed{
\text{Maximum Simultaneous Modality}.
}
$$

---

# 42. Modality Selection

由：

$$
f(
Activity,
Zone,
Attention,
Privacy,
Network,
Motion
)
$$

決定。

---

# 43. Example：Driver

活動：

$$
ReadContract.
$$

Zone：

$$
Driver.
$$

Decision：

$$
Transform
\rightarrow
ShortAudioSummary.
$$

---

# 44. Example：Rear Passenger

同一 activity：

$$
ReadContract.
$$

Zone：

$$
RearPrivate.
$$

Decision：

$$
Allow
\rightarrow
4KDisplay+Keyboard+Voice.
$$

---

# 45. Environment Is First-Class Output

本文核心：

$$
\boxed{
Environment
=
OutputSurface.
}
$$

---

# 46. Work Profile

可能：

- seat upright；
- neutral light；
- private display；
- focused audio；
- high network priority；
- reduced entertainment notifications。

---

# 47. Rest Profile

- reclined seat；
- low light；
- display off；
- DND；
- low audio；
- emergency-only interrupt。

---

# 48. Entertainment Profile

- large display；
- spatial audio；
- ambient light；
- game input；
- lower work notification。

---

# 49. Social Profile

- shared display；
- shared audio；
- conversation priority；
- AI low-interruption。

---

# 50. Creative Profile

- drawing / writing surface；
- voice capture；
- camera if allowed；
- AI co-creation；
- artifact persistence。

---

# 51. Idle Profile

最重要之一：

```text
Do nothing.
```

System：

- 不推薦工作；
- 不拉起任務；
- 不主動最佳化；
- 只保留安全 / emergency。

---

# 52. Agent-Only Profile

B-02：

$$
Mode=AGENT\_ONLY.
$$

車艙可以：

- human rests；
- agent researches；
- no work UI；
- arrival review packet。

---

# 53. Environment Compiler

可分：

$$
\boxed{
ExperienceCompiler
=
DigitalPlanner
+
PhysicalPlanner.
}
$$

Digital：

- app；
- display；
- media；
- communication。

Physical：

- light；
- seat；
- climate；
- audio field。

---

# 54. Physical Planner Must Be Bounded

所有 physical output：

$$
\boxed{
BoundedByCapability.
}
$$

例如 seat：

不能超過 hardware / safety range。

---

# 55. Cabin Actuation

定義：

$$
\boxed{
u_t^{cabin}
=
(
u_{display},
u_{audio},
u_{light},
u_{seat},
u_{climate},
u_{privacy}
).
}
$$

---

# 56. Raw Actuation Is Not Semantic Intent

所以：

$$
\boxed{
Intent
\neq
u_t^{cabin}.
}
$$

需要 compiler / controller。

---

# 57. Actuation Receipt

每次重要狀態變更：

```yaml
receipt_id: "cabin_rcpt_..."
plan_id: "xp_..."
zone_id: "rear_right"
capability_id: "seat.recline"
requested: 20
applied: 20
status: "SUCCEEDED"
safety_policy: "seat-v4"
```

---

# 58. Why Evidence Matters

AI 說：

> 已經調暗燈光。

不等於燈真的調暗。

所以：

$$
\boxed{
ModelClaim
\neq
ActuationEvidence.
}
$$

---

# 59. Cabin State Feedback

控制後：

$$
Sense
\rightarrow
Verify.
$$

例如：

- seat sensor；
- climate state；
- display status。

---

# 60. Closed-Loop Cabin Control

$$
\boxed{
Plan
\rightarrow
Actuate
\rightarrow
Observe
\rightarrow
Correct.
}
$$

不是：

$$
Prompt
\rightarrow
AssumeDone.
$$

---

# 61. Display Orchestration

多 display：

需要：

- ownership；
- privacy；
- zone；
- content type；
- driver exposure；
- priority。

---

# 62. Main Display ≠ Global Display

一個中心大螢幕：

可能只適合：

- navigation；
- shared control。

私人內容應：

$$
\rightarrow
PersonalDisplay.
$$

---

# 63. Projection Orchestration

windshield / HUD：

$$
\boxed{
SafetyCriticalVisualSurface.
}
$$

不能拿來播放任意工作內容。

---

# 64. Passenger Projection

rear / side projection：

可更自由。

所以：

$$
\boxed{
ProjectionSurface
}
$$

也必須有 Zone Contract。

---

# 65. Audio Orchestration

音訊可以是：

- shared；
- zone；
- headset；
- safety channel；
- assistant channel。

---

# 66. Audio Priority

可定義：

$$
Priority:
Safety>Navigation>Communication>Entertainment.
$$

但 user policy 可微調非 safety 類。

---

# 67. Safety Audio Ducking

若：

$$
SafetyAlert=1,
$$

則：

$$
EntertainmentVolume\downarrow.
$$

但私人敏感內容不應因此播到 shared speaker。

---

# 68. Microphone Orchestration

Mic：

- wake；
- communication；
- cabin command；
- safety sensing。

不同用途應不同 data policy。

---

# 69. Mic Purpose Binding

$$
\boxed{
MicAccess
=
Purpose
+
Scope
+
Retention.
}
$$

---

# 70. Camera / Vision

Cabin vision 可以支援：

- occupant detection；
- gesture；
- attention；
- safety；
- personalization。

但：

$$
\boxed{
CameraExists
\not\Rightarrow
UnlimitedRecording.
}
$$

---

# 71. On-Device Privacy

Mercedes 2026 on-device AI 與 NVIDIA edge-first architecture 都支持：

$$
\boxed{
PrivacySensitiveInference
\rightarrow
Edge
}
$$

作為合理方向。

---

# 72. Local Memory Cache

shared vehicle：

只能保存：

$$
\boxed{
MinimumNecessaryCache.
}
$$

Ride end：

清除。

---

# 73. Shared Vehicle Teardown

正式：

$$
\boxed{
RideEnd
\Rightarrow
DetachIdentity
+
InvalidateSession
+
EraseLocalSecrets
+
ClearPrivateCache
+
ResetCabinProfile.
}
$$

---

# 74. Personal Car Teardown

私人車不同。

可以保留：

- profile；
- preferences；
- trusted device；

但仍應：

- encrypted；
- revocable；
- exportable。

---

# 75. Driver vs Passenger Account

同一車：

$$
Account_{driver}
\neq
Account_{rear}.
$$

不能共用：

- mail；
- AI memory；
- history。

---

# 76. Multi-User AI

可以：

$$
A_1,A_2,\ldots,A_n.
$$

每個 occupant 有：

- own agent；
- own context；
- own permission。

---

# 77. Cabin Agent

另有：

$$
A_{cabin}.
$$

它是 shared system agent。

---

# 78. Personal Agent vs Cabin Agent

Personal Agent：

- knows user；
- owns personal context；
- plans tasks。

Cabin Agent：

- knows vehicle capability；
- manages cabin environment；
- enforces zone-safe execution。

---

# 79. Agent Separation

因此：

$$
\boxed{
PersonalAgent
\neq
CabinAgent
\neq
DrivingAgent.
}
$$

---

# 80. Agent-to-Agent Intent

Personal Agent：

> Neo.K 想休息 40 分鐘。

Cabin Agent：

- checks zone；
- checks capability；
- builds plan；
- actuates allowed environment。

---

# 81. Cabin Agent Does Not Need Personal History

它只需要：

$$
\boxed{
Minimum Intent Contract.
}
$$

而不是：

> 把整個個人 memory 丟給車。

---

# 82. Privacy by Contract Minimization

傳輸：

```yaml
intent: "REST"
temperature_preference: 23
light: "low"
```

而不是：

```text
full personal profile
full email history
full AI memory
```

---

# 83. AI Memory Boundary

車艙本地 AI 可以有：

$$
CabinSessionMemory.
$$

Ride end：

$$
CabinSessionMemory\rightarrow0.
$$

除非明確保存。

---

# 84. Continuity Memory Remains External

正式 personal continuity state：

$$
\boxed{
OutsideSharedVehicle.
}
$$

車只拿 temporary projection。

---

# 85. Source-of-Record Boundary

車上看到／聽到的：

- summary；
- visualization；
- TTS；

都只是：

$$
Rendition.
$$

Canonical artifact 在 Series A state domain。

---

# 86. Vehicle Surface as Ephemeral Renderer

shared robotaxi 可視為：

$$
\boxed{
EphemeralTrustedSurface.
}
$$

不是：

$$
PersonalComputer.
$$

---

# 87. Surface Attestation

更高階可以要求：

- device attestation；
- software version；
- privacy mode；
- local erase capability。

再決定是否投影 D3 / D4 content。

---

# 88. Network Orchestration

車上：

- 5G；
- Wi-Fi；
- satellite；
- tethering；

都可以進 Series A AHCF。

Cabin Runtime 只要求：

$$
FlowRequirement.
$$

---

# 89. Work Flow Requirement

例如：

```yaml
class: "INTERACTIVE_WORK"
latency: "medium"
bandwidth: "high"
privacy: "high"
fallback:
  - "audio"
  - "offline_draft"
```

---

# 90. Entertainment Flow Requirement

```yaml
class: "STREAMING"
bandwidth: "high"
latency: "medium"
fallback:
  - "lower_resolution"
```

---

# 91. Network-Aware Experience

若 bandwidth 降：

4K：

$$
\rightarrow
1080p
\rightarrow
audio.
$$

但 activity identity 不變。

---

# 92. Compute-Aware Experience

edge compute limited：

$$
LargeVLM
\rightarrow
Cloud.
$$

cloud down：

$$
SmallLocalModel.
$$

---

# 93. Model-Aware Experience

不同 AI provider：

能力不同。

Experience Compiler 只應要求：

$$
Capability.
$$

不鎖 provider。

---

# 94. Cabin Profile Portability

使用者 profile：

```text
REST:
seat 20°
temp 23
light low
audio private
```

應該：

$$
\boxed{
PortableAcrossCompatibleVehicles.
}
$$

這會直接接 B-06 service economy。

---

# 95. Capability Matching

不同車：

$$
Capability_A
\neq
Capability_B.
$$

Profile compiler：

$$
\boxed{
DesiredExperience
\rightarrow
BestAvailableConfiguration.
}
$$

---

# 96. Graceful Profile Degradation

如果車沒有：

- privacy glass；

則：

$$
PrivacyMode
\rightarrow
PersonalDisplay+Headphones.
$$

---

# 97. If Capability Insufficient

如果：

$$
RequiredPrivacy
>
AvailablePrivacy,
$$

則：

$$
\boxed{
DeferSensitiveActivity.
}
$$

---

# 98. Motion-Aware Cabin

急彎：

- visual reading 可能暫停；
- screen layout simplification；
- game pause。

---

# 99. Motion Input

Cabin Runtime 可以使用：

- acceleration；
- turn；
- road roughness；
- route phase。

但只做：

$$
ExperienceAdaptation.
$$

不取得 driving control。

---

# 100. Motion Sickness Adaptation

若偵測：

$$
MotionSicknessRisk\uparrow,
$$

可：

- reduce visual motion；
- shrink immersive display；
- switch to audio；
- change seat orientation if allowed；
- pause activity。

---

# 101. Environment as Feedback

若乘員說：

> 太亮。

AI 不只 reply：

> 好的。

而是：

$$
LightCommand.
$$

但仍需要：

- capability；
- authority；
- receipt。

---

# 102. Natural Language to Environment

這就是：

$$
\boxed{
Language
\rightarrow
ExperienceIntent
\rightarrow
CabinPlan.
}
$$

不是直接 physical field control。

---

# 103. B-05 與 SPFC 的界線

雖然先前 SPFC 探索 semantic-to-physical field compilation，

但 ANVC v0.1 不需要：

$$
SPFC.
$$

只需要普通：

- vehicle API；
- actuator；
- controller；
- cabin service。

---

# 104. Existing Technology Is Enough for v0.1

因此：

$$
\boxed{
ANVC_{v0.1}
}
$$

可以建立在：

- existing displays；
- existing audio；
- WebRTC；
- automotive APIs；
- central / zonal compute；
- edge AI；
- cloud AI。

---

# 105. Retrofit Path

舊車：

$$
\boxed{
Tablet/LargeDisplay
+
AIBox
+
Mic
+
Audio
+
Network
}
$$

就可以做：

- communication continuity；
- rear work；
- entertainment；
- AI agent。

---

# 106. Retrofit Limitation

但舊車可能沒有：

- seat API；
- lighting API；
- privacy glass；
- zonal HVAC。

所以：

$$
PMSLevel
$$

較低。

---

# 107. New Vehicle Path

新車可以：

- service-oriented cabin control；
- zonal architecture；
- OTA；
- multi-user；
- multi-display；
- more sensors。

---

# 108. Vehicle API Abstraction

ANVC 不應綁某 OEM。

定義：

$$
\boxed{
CabinHAL.
}
$$

---

# 109. CabinHAL

接口例如：

```text
display.set_layout
audio.set_zone
seat.set_profile
climate.set_profile
lighting.set_scene
privacy.set_mode
```

---

# 110. HAL ≠ Raw Bus

CabinHAL 不暴露：

- arbitrary CAN；
- raw ECU write。

---

# 111. Safety Domain Boundary

更高層：

```text
CabinHAL
```

只包含：

$$
\boxed{
Allowed Cabin Domain.
}
$$

---

# 112. Safety-Critical Boundary

例如：

- steering；
- braking；
- powertrain；
- airbag；

不在普通 cabin HAL。

---

# 113. Shared Functions

有些功能：

- seat；
- window；

可能和 safety 相關。

因此需：

$$
\boxed{
SafetyMediator.
}
$$

---

# 114. Experience Compiler Architecture

可以拆：

1. Intent Parser；
2. Activity Resolver；
3. MRC Loader；
4. Zone Evaluator；
5. Capability Matcher；
6. Modality Planner；
7. Environment Planner；
8. Safety / Privacy Validator；
9. Execution Orchestrator；
10. Receipt Collector。

---

# 115. Intent Parser

不直接執行。

輸出：

$$
StructuredIntent.
$$

---

# 116. Activity Resolver

知道：

- work；
- rest；
- entertainment；
- social；
- idle。

---

# 117. MRC Loader

需要 continuity 才載入。

---

# 118. Zone Evaluator

取得：

$$
B04\ ZoneDecision.
$$

---

# 119. Capability Matcher

看車有哪些能力。

---

# 120. Modality Planner

決定：

- visual；
- audio；
- voice；
- keyboard；
- touch。

---

# 121. Environment Planner

決定：

- light；
- seat；
- climate；
- audio scene。

---

# 122. Validator

套：

- safety；
- privacy；
- authority。

---

# 123. Orchestrator

執行 bounded commands。

---

# 124. Receipt Collector

確認：

$$
AppliedState.
$$

---

# 125. Experience Plan State

定義：

$$
\boxed{
X_t^{cab}
=
(
Activity,
Zone,
Modalities,
Environment,
Network,
AI,
Policy
).
}
$$

---

# 126. Plan Transition

$$
X_t^{cab}
\rightarrow
X_{t+1}^{cab}
$$

可能因：

- user；
- route；
- network；
- safety；
- fatigue；
- arrival。

---

# 127. Arrival Transition

距離目的地：

$$
10\ min.
$$

Work profile 可以：

- save；
- summarize；
- lower complexity；
- prepare exit。

---

# 128. Departure Transition

上車：

- attach Surface；
- authenticate；
- load profile；
- privacy check；
- MRC resume。

---

# 129. Ride-End Transition

shared vehicle：

- checkpoint；
- detach；
- teardown；
- local wipe；
- evidence。

---

# 130. Persistent Experience ≠ Persistent Vehicle State

使用者 profile 可持續。

但 shared car local state：

$$
\boxed{
Ephemeral.
}
$$

---

# 131. Reference Profile：WORK

```yaml
mode: "WORK"
requirements:
  visual: "high"
  privacy: "high"
  network: "medium_high"
preferred:
  display: "private_large"
  audio: "private_zone"
  input:
    - "voice"
    - "keyboard"
environment:
  seat: "upright"
  light: "neutral"
fallback:
  - "voice_summary"
  - "offline_draft"
```

---

# 132. Reference Profile：REST

```yaml
mode: "REST"
interruptions: "emergency_only"
visual: "off"
audio: "quiet"
seat: "reclined_if_safe"
light: "low"
network: "background_only"
```

---

# 133. Reference Profile：ENTERTAINMENT

```yaml
mode: "ENTERTAINMENT"
visual: "immersive_if_allowed"
audio: "spatial"
work_notifications: "blocked"
```

---

# 134. Reference Profile：SOCIAL

```yaml
mode: "SOCIAL"
display: "shared"
audio: "shared"
personal_ai: "low_intrusion"
privacy: "group_scope"
```

---

# 135. Reference Profile：AGENT_ONLY

```yaml
mode: "AGENT_ONLY"
human_work_ui: "off"
agent_background_tasks: "allowed_by_policy"
external_side_effects: "approval_required"
arrival_review_packet: true
```

---

# 136. Personalization Layer

Profile 可以記：

- preferred temp；
- seat；
- light；
- audio；
- DND；
- accessibility。

但：

$$
\boxed{
Personalization
\neq
UnlimitedProfiling.
}
$$

---

# 137. Accessibility

AI-native cabin 應支援：

- speech；
- caption；
- high contrast；
- screen reader；
- hearing assistance；
- physical accessibility；
- alternative input。

---

# 138. Accessibility Is Not Optional Luxury

如果 Mobility Hospitality 未來普及，

accessibility 應為：

$$
\boxed{
Core Capability.
}
$$

---

# 139. Family Mode

兒童：

- content；
- safety；
- account；
- privacy；

不同。

AI 不應把成人 personal context 投影給 child zone。

---

# 140. Enterprise Mode

商務車：

- enterprise login；
- VPN；
- work artifact；
- private meeting；
- policy。

但：

$$
EnterpriseContext
$$

ride end 必須 teardown。

---

# 141. Meeting Mode

可能：

- camera；
- mic；
- private audio；
- display；
- notes agent。

若 shared ride privacy 不足：

$$
\boxed{
MeetingMode=DEFER.
}
$$

---

# 142. Call Mode

PAI Relay 可以：

$$
\text{Contact Intent}
\rightarrow
VoiceCall.
$$

但 zone：

- driver；
- passenger；

決定 interaction complexity。

---

# 143. AI as Communication Operator

車內 AI 可以：

- summarize messages；
- prepare reply；
- schedule；
- call；
- join meeting。

這承接 Series A。

---

# 144. AI as Environment Operator

另外：

- seat；
- light；
- climate；
- audio。

這是 B-05 新增。

---

# 145. AI as Safety Bypass Is Forbidden

明確：

$$
\boxed{
AI
\not\Rightarrow
SafetyBypass.
}
$$

---

# 146. AI as Experience Orchestrator

最準確：

$$
\boxed{
AI
=
\text{Experience Orchestrator}.
}
$$

---

# 147. Fallback Without AI

AI down：

使用者仍可：

- manual light；
- manual seat；
- normal media；
- normal navigation。

所以：

$$
\boxed{
AI Failure
\neq
Cabin Failure.
}
$$

---

# 148. UX Principle：Predictable Control

AI control 必須：

- reversible；
- explainable；
- visible；
- interruptible。

---

# 149. User Override

任何非 safety cabin automation：

$$
\boxed{
UserOverride.
}
$$

---

# 150. Undo

若 AI 調錯：

> 恢復剛才。

系統需：

$$
\boxed{
RollbackToPreviousCabinState.
}
$$

---

# 151. Cabin State History

保留：

- plan；
- actuation；
- rollback；

但不必保存所有私人語音。

---

# 152. Evidence Minimization

記：

```text
light changed
```

不一定記：

> 使用者說了完整私人句子。

---

# 153. Security Threats

## T1 Prompt → Unsafe Actuation

## T2 Personal Context Leakage

## T3 Shared-Vehicle Residual Data

## T4 Cabin/Driving Authority Confusion

## T5 Malicious Device Capability

## T6 Compromised Cloud Agent

## T7 Fake Actuation Success

## T8 Zone Misclassification

## T9 Driver Distraction Escalation

## T10 Persistent Microphone Overcapture

---

# 154. Threat T1 Mitigation

Intent parser 不直接 actuator。

---

# 155. T2

Data class + Zone privacy。

---

# 156. T3

Teardown contract。

---

# 157. T4

Separate agent / HAL boundary。

---

# 158. T5

Capability attestation / allowlist。

---

# 159. T6

Edge policy guard。

---

# 160. T7

Actuation receipt。

---

# 161. T8

Conservative fallback。

---

# 162. T9

B-04 ZoneDecision。

---

# 163. T10

Purpose-bound mic access。

---

# 164. ANVC MVP

第一版可以非常保守。

只做：

- rear-seat simulator；
- large display；
- voice；
- AI agent；
- audio zone simulation；
- light / seat virtual actuator；
- Continuity Runtime；
- Zone Contract。

---

# 165. MVP 不先控制真車

先：

$$
\boxed{
DigitalTwinCabin.
}
$$

---

# 166. Digital Twin Cabin

模擬：

- seat；
- display；
- light；
- audio；
- zone；
- motion；
- network。

---

# 167. Why Simulator First

可以驗證：

- Experience Compiler；
- MRC resume；
- ZoneDecision；
- profile；
- teardown；

不用碰 safety-critical hardware。

---

# 168. MVP Scenario 1：Desktop → Rear Cabin Work

```text
Desktop paper
→ MRC
→ rear passenger zone
→ private display
→ voice + keyboard
→ continue
```

---

# 169. MVP Scenario 2：Driver Transform

```text
same paper
→ driver zone
→ visual blocked
→ short voice cue
→ defer full resume
```

---

# 170. MVP Scenario 3：Rest

```text
REST intent
→ display off
→ DND
→ low light
→ agent-only background task
```

---

# 171. MVP Scenario 4：Network Degradation

```text
4K + cloud agent
→ bandwidth drops
→ local summary + offline notes
```

---

# 172. MVP Scenario 5：Ride End

```text
checkpoint
→ detach
→ wipe local session
→ resume on desktop
```

---

# 173. Evaluation Metrics

## Experience Compile Success

$$
S_C.
$$

## Zone Compliance

$$
C_Z.
$$

## Actuation Success

$$
S_A.
$$

## Privacy Leakage

$$
L_P.
$$

## Continuity Loss

$$
L_{MCC}.
$$

## User Override Rate

$$
R_O.
$$

---

# 174. Latency

speech interaction：

$$
Latency
$$

必須低。

NVIDIA 2026 對 on-device agentic assistant 甚至以：

$$
<500\ ms
$$

作為其 production architecture 例示的 response-time challenge。

這是工程參考，不是本文 universal requirement。

---

# 175. Edge Token Throughput

同一 NVIDIA 例示：

$$
>30\ tokens/s
$$

作為 advanced local experience challenge。

這再次說明車艙 AI 已經變成 serious edge-compute workload。

---

# 176. Compute Isolation

Cabin AI workload 不應：

> 影響 safety-critical compute deadline。

所以：

$$
\boxed{
ComputeShared
\not\Rightarrow
DeadlineShared.
}
$$

---

# 177. Mixed-Criticality

未來 centralized platform 可能共享硬體。

但必須：

- partition；
- priority；
- isolation；
- certification boundary。

---

# 178. B-05 不定義 ADAS Safety Architecture

本文只定：

$$
CabinSideBoundary.
$$

真正 ADAS / ADS safety architecture 仍屬專門領域。

---

# 179. Current Industry Status

截至 2026：

已存在：

- multiple displays；
- panoramic / windshield UI；
- zonal audio；
- spatial audio；
- multimodal LLM；
- agentic AI；
- on-device AI；
- edge-cloud pipeline；
- driver monitoring；
- centralized / zonal compute；
- conversational vehicle control。

---

# 180. 尚未成熟為統一 PMS

仍缺：

- cross-provider canonical continuity；
- portable cabin profile；
- universal Zone Contract；
- activity-aware Experience Compiler；
- shared-vehicle privacy teardown standard；
- agent / cabin / driving authority common model；
- cross-OEM experience portability。

這就是本文研究空間。

---

# 181. ANVC Maturity

## ANVC-L0

Fixed infotainment。

## ANVC-L1

Connected multimodal cockpit。

## ANVC-L2

Context-aware AI cabin。

## ANVC-L3

Zone-aware programmable cabin。

## ANVC-L4

Continuity-native, portable, multi-agent programmable mobility cabin。

---

# 182. ANVC ≠ Automation Level

仍：

$$
\boxed{
ANVCLevel
\neq
SAELevel.
}
$$

---

# 183. Luxury Car Can Be High ANVC, Low Automation

有司機的車：

- rear office；
- AI；
- display；
- network；

可能 ANVC 高。

---

# 184. Robotaxi Can Be Low ANVC

一台 driverless pod：

- only transport；
- tiny UI；

可能 SAE automation 高，但 ANVC 低。

---

# 185. Product Implication

因此 robotaxi differentiation 不只：

$$
Autonomy.
$$

還有：

$$
\boxed{
CabinCapability.
}
$$

這直接進 B-06。

---

# 186. Cabin Capability Score

可定義：

$$
\boxed{
C_{cab}
=
f(
Display,
Audio,
Privacy,
Environment,
AI,
Continuity,
Zone,
Accessibility
).
}
$$

---

# 187. User Experience Score

但：

$$
C_{cab}
$$

高不代表：

$$
U_{\text{user}}
$$

高。

還要：

- activity match；
- comfort；
- motion；
- privacy。

---

# 188. Best Cabin Is Contextual

所以：

$$
\boxed{
BestCabin
=
f(UserIntent,Trip,Occupants).
}
$$

---

# 189. B-06 Interface

B-05 輸出：

- capability class；
- experience profiles；
- privacy class；
- zone class；
- continuity support；
- AI support。

B-06 可以拿來：

- service tier；
- pricing；
- matching；
- fleet segmentation。

---

# 190. 最重要的六條不變量

第一：

$$
\boxed{
CabinIntelligence
\neq
DrivingAuthority.
}
$$

第二：

$$
\boxed{
Intent
\rightarrow
ExperienceCompiler
\rightarrow
BoundedActuation.
}
$$

第三：

$$
\boxed{
Multimodal
\neq
EverythingOn.
}
$$

第四：

$$
\boxed{
Environment
=
FirstClassOutputSurface.
}
$$

第五：

$$
\boxed{
SharedCompute
\neq
SharedAuthority.
}
$$

第六：

$$
\boxed{
PersonalAgent
\neq
CabinAgent
\neq
DrivingAgent.
}
$$

---

# 191. 結論

AI-native vehicle cabin 真正的意義不是：

> 車上終於有一個可以聊天的 AI。

而是：

> **車艙本身開始變成一個由 activity、continuity、zone、安全、隱私與使用者意圖共同編排的多模態 runtime。**

現代汽車產業已經擁有大量必要 primitive：

- 多螢幕；
- windshield / panoramic interfaces；
- multi-channel / zonal audio；
- ANC；
- speech；
- multimodal LLM；
- agentic AI；
- on-device AI；
- cloud agents；
- centralized / zonal compute；
- OTA；
- context-aware personalization。

因此問題已經不是：

> 這些硬體能不能被放進車？

而是：

> **它們能不能被組成一個真正以活動與人為中心，而不是以單一 infotainment app 為中心的系統？**

本文的答案是 Experience Compiler。

它讓：

$$
\boxed{
Intent
}
$$

成為上層。

而：

$$
Display,
Audio,
Light,
Seat,
Climate,
AI,
Network
$$

成為 backend capability。

再由：

$$
\boxed{
ZoneContract
+
Safety
+
Privacy
+
Authority
}
$$

限制。

因此：

$$
\boxed{
Intent
\rightarrow
ActivityState
\rightarrow
MRC
\rightarrow
ZoneDecision
\rightarrow
ExperiencePlan
\rightarrow
CabinActuation
\rightarrow
Evidence.
}
$$

這是一條從人的意圖一路落到物理車艙，又不讓 AI 越過安全與主權邊界的完整鏈。

B-06 接下來將回答另一個問題：

> 當不同車輛可以提供不同 quality 的私人／工作／休息／娛樂時空，乘客到底在買什麼？

那時交通服務就會正式從：

$$
\text{Ride}
$$

進入：

$$
\boxed{
\text{Mobility Hospitality}.
}
$$

---

# 參考文獻與技術錨點

1. NVIDIA Technical Blog. **How to Build In-Vehicle AI Agents with NVIDIA: From Cloud to Car.** 2026-05-05.  
   `https://developer.nvidia.com/blog/how-to-build-in-vehicle-ai-agents-with-nvidia-from-cloud-to-car/`

2. Qualcomm. **Snapdragon Cockpit Platform.** Current product documentation checked 2026-08-24.  
   `https://www.qualcomm.com/automotive/solutions/cockpit`

3. Qualcomm. **Leapmotor and Qualcomm Debuts World's First Automotive Central Computer Powered by Snapdragon Cockpit Elite and Snapdragon Ride Elite Platforms.** 2026-01-05.  
   `https://www.qualcomm.com/news/releases/2026/01/leapmotor-and-qualcomm-debuts-world-s-first-automotive-central-c`

4. Qualcomm. **Qualcomm Drives the Future of Mobility with Strong Snapdragon Digital Chassis Momentum and Agentic AI for Major Global Automakers Worldwide.** 2026-01-05.  
   `https://www.qualcomm.com/news/releases/2026/01/qualcomm-drives-the-future-of-mobility-with-strong-snapdragon-di`

5. Mercedes-Benz Group. **Next Generation in-car intelligence.** 2026-04-23.  
   `https://group.mercedes-benz.com/technology/innovation/collaboration/liquid-ai.html`

6. Qualcomm / Mercedes-Benz. **Snapdragon Cockpit Platforms Power Smart, Intuitive AI-Driven Experiences in New All-Electric Mercedes-Benz Vehicles.** 2025-09.  
   `https://www.qualcomm.com/news/releases/2025/09/qualcomm-s-snapdragon-cockpit-platforms-power-smart--intuitive-a`

7. BMW Group. **BMW Panoramic iDrive: Four Key Elements.** 2025 investor / analyst materials.  
   `https://www.bmwgroup.com/content/dam/grpw/websites/bmwgroup_com/ir/downloads/en/2025/investor-and-analyst-days-2025/BMW-Group-Investor-Analyst-Days-2025-UI-UX-Software.pdf`

8. Qualcomm / BMW Group. **Qualcomm Named BMW Group’s Lead Compute Silicon Provider for Digital Cockpit and Automated Driving Through the Next Decade.** 2026-07-29.  
   `https://www.qualcomm.com/news/releases/2026/07/qualcomm-named-bmw-group-s-lead-compute-silicon-provider-for-dig`

9. Android Automotive / Android for Cars documentation cited in B-04 for multi-user / multi-display / occupant zones / UX restrictions.

10. Personal sound-zone literature cited in B-04 for headrest loudspeakers, acoustic contrast, ANC and in-car zonal audio.

---

# 內部依賴

1. `B01_Programmable_Mobility_Space_General_Theory_v0.1.md`
2. `B02_Travel_Time_Reclamation_v0.1.md`
3. `B03_Mobility_Cognitive_Continuity_v0.1.md`
4. `B03_Mobility_Resume_Capsule.schema.json`
5. `B04_Spatial_Attention_Zones_v0.1.md`
6. `B04_Spatial_Attention_Zone.schema.json`
7. `B04_Zone_Decision.schema.json`
8. Series A A-03 Multimodal-Native Communication
9. Series A A-04 AI Communication Runtime
10. Series A A-05 Adaptive Hybrid Communication Fabric
11. Series A A-06 Personal Communication Sovereignty
12. Series A A-07 EVEMISS Communication Continuum Architecture

---

# 文件狀態

**Series：** B｜Programmable Mobility & Spatial Continuum  
**Number：** B-05  
**Version：** v0.1  
**Status：** Research Paper / Canonical Source  
**Series B progress：** 5/7  
**Overall 15-document progress：** 12/15  
