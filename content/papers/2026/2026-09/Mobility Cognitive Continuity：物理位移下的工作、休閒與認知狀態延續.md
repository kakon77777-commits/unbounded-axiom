---
title: "Mobility Cognitive Continuity：物理位移下的工作、休閒與認知狀態延續"
subtitle: "Mobility Cognitive Continuity: Preserving Activity Identity, Resumption Cues, and Human–AI State Across Physical Transitions"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Paper / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series B｜Programmable Mobility & Spatial Continuum"
series_number: "B-03"
canonical_source: true
encoding: "UTF-8"
---

# Mobility Cognitive Continuity：物理位移下的工作、休閒與認知狀態延續

## Mobility Cognitive Continuity: Preserving Activity Identity, Resumption Cues, and Human–AI State Across Physical Transitions

**系列：** Series B｜Programmable Mobility & Spatial Continuum  
**編號：** B-03  
**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Paper / Canonical Source  

---

# 摘要

B-01 將交通工具重新定義為可程式移動空間；B-02 則將交通時間拆解為 forced、self-directed、work 與 reserve time，指出技術真正釋放的是既有旅程中的活動可行性與注意力，而不是創造新的時鐘時間。本篇進一步研究下一個問題：

> **即使旅程中的時間已經可以工作、休息、娛樂或社交，為什麼人在換空間、換裝置、換模態、換網路與換 AI 之後，仍然常常必須重新想起「我剛才做到哪裡」？**

本文將此問題稱為：

# **Mobility Cognitive Continuity（MCC）**
## **移動認知連續性**

MCC 不主張機器能直接複製或保存人的完整內在意識、感質或腦狀態。本文研究的是更有限、可工程化、可證偽的命題：

> **系統能否保存一個活動在移動前後所需的外部化目標、次目標、上下文、Artifact、未完成問題、下一步、授權、交互模態與恢復提示，使人或 AI 在新 Surface 上可以以最小重建成本繼續同一活動？**

因此本文明確區分：

$$
\boxed{
\text{Internal Human Cognitive State}
\neq
\text{Externalized Continuity State}.
}
$$

本文只對後者提出工程架構。

一個活動的外部連續狀態可表示為：

$$
\boxed{
\mathcal C^{act}_t
=
(
G_t,
Q_t,
X_t,
F_t,
N_t,
U_t,
K_t,
P_t,
M_t
)
}
$$

其中：

- $G_t$：goal / activity identity；
- $Q_t$：current subgoal / task frontier；
- $X_t$：relevant context；
- $F_t$：canonical artifact / media / world state；
- $N_t$：next intended action；
- $U_t$：unresolved questions / open loops；
- $K_t$：resumption cues；
- $P_t$：permission / privacy / authority state；
- $M_t$：current modality / surface representation。

本文的第一個核心命題是：

$$
\boxed{
\text{Activity Continuity}
\neq
\text{Interface Persistence}.
}
$$

同一份論文可以在桌面上以 PDF + keyboard 呈現，進車後轉為 voice discussion + large display，到目的地後再恢復視覺公式與引用；只要 activity identity、task frontier、artifact identity、open loops 與 authority 沒有漂移，這仍然可以被視為同一活動的延續。

第二個核心命題是：

$$
\boxed{
\text{Continuity}
\neq
\text{Continuous Human Attention}.
}
$$

人可以暫停、休息、睡覺或切換到娛樂；AI Agent 可以在授權範圍內維持 task state、執行背景搜尋或整理，之後再把結果包裝成 resumption cue。真正需要持續的是**可恢復性**，不是要求人類全程 attention-on。

第三個核心命題來自 interruption / task-resumption research。Trafton、Altmann 等人的經典研究顯示，中斷後重新進入原任務存在可量化的 **resumption lag**；預先準備與 contextual cues 能縮短恢復成本。2025 年 Scientific Reports 的新實驗仍顯示 retrieval cues / assistant cues 可改善部分中斷後恢復；2026 年 Displays 的眼動研究也顯示 interruption 增加 task completion cost 與跨區資訊檢查。這些結果支持一個對 mobility system 非常直接的設計原則：

$$
\boxed{
\text{State Transfer}
+
\text{Cue Transfer}
>
\text{Raw Data Transfer Alone}.
}
$$

第四個核心命題是：現代跨裝置系統已經提供弱版本工程先例。Apple Handoff 以 `NSUserActivity` 表示可恢復活動狀態；Android Cross device SDK 提供 multidevice sessions 與 session transfer；Windows Resume 2026 年也以 activity context 讓 Android 上的支援活動在 Windows 繼續。這些系統證明「activity continuation」已是成熟產品問題，但它們通常仍以 application / ecosystem / device continuation 為主；MCC 要再往上抽象到跨產品、跨模態、跨 AI 與跨 mobility surface 的活動身份。

本文提出 **Mobility Resume Capsule（MRC）**：一個在 Surface Transition 時生成的最小可恢復封包，至少包含 activity identity、task frontier、artifact references、last meaningful action、next intended action、open loops、cue bundle、authority epoch、privacy context、source-of-record pointer 與 preferred resumption modality。它的目標不是保存所有歷史，而是讓：

$$
\boxed{
L_{\text{resume}}
\rightarrow
\min
}
$$

其中 $L_{\text{resume}}$ 為 resumption loss。

本文進一步建立六類 transition：Direct Handoff、Pause–Resume、Modality Transformation、Agent Substitution、Deferred Human Review、Environment Rebinding；提出 Continuity Loss、Resumption Lag、Cue Fidelity、Artifact Drift、Authority Drift、Semantic Drift、Mode Drift 等候選指標；並把 work、entertainment、social interaction、rest 與 idle 都納入同一 continuity ontology。

最終，本文將移動認知連續性收斂成：

$$
\boxed{
\text{Suspend}
\rightarrow
\text{Externalize}
\rightarrow
\text{Transfer}
\rightarrow
\text{Rebind}
\rightarrow
\text{Cue}
\rightarrow
\text{Resume}.
}
$$

Series B-04 將接著研究這套 continuity 如何受到 Driver / Passenger / Rear-seat 等不同 Spatial Attention Zone 的安全、隱私與注意力限制。

---

# Abstract

Programmable mobility is not complete merely because travel time becomes usable. Users must also be able to continue the same activity across changes in physical location, device, interface modality, connectivity, and AI provider without repeatedly reconstructing where they left off.

This paper introduces Mobility Cognitive Continuity (MCC), a deliberately bounded engineering concept. MCC does not claim to preserve a person's complete internal cognitive or conscious state. Instead, it concerns the externalizable state required to resume an activity: goal identity, current subgoal, relevant context, canonical artifact state, next intended action, unresolved questions, resumption cues, authority, and current representation.

The paper builds on task-interruption research showing measurable resumption costs and the benefit of preparatory and contextual cues. It also relates MCC to modern activity-continuation mechanisms such as Apple Handoff, Android Cross-device Sessions, and Windows Resume. These systems provide important implementation precedents but generally remain application- or ecosystem-scoped; MCC abstracts the problem to cross-surface mobility.

A Mobility Resume Capsule (MRC) is proposed as the minimum transferable structure required to resume an activity on another mobility surface. The paper defines direct handoff, pause-resume, modality transformation, agent substitution, deferred human review, and environment rebinding. It proposes measurable continuity losses including resumption lag, cue loss, semantic drift, artifact drift, authority drift, and mode drift.

MCC applies not only to work but also to entertainment, social interaction, creativity, rest, and idle states. Continuity therefore means resumability and identity preservation, not perpetual human attention. The paper concludes with a transition architecture that becomes the formal input to Series B-04 on spatial attention zoning.

---

# 0. 問題不是「資料有沒有同步」

最常見的假設是：

> 文件已經同步到雲端，所以工作可以繼續。

但實際上：

$$
\boxed{
\text{Data Sync}
\neq
\text{Activity Continuity}.
}
$$

你可能已經有同一個檔案，卻不知道：

- 剛才看到哪；
- 為什麼停在這；
- 下一步是什麼；
- 哪個假設有問題；
- 哪個版本是 source-of-record；
- 哪個 Agent 在做背景工作；
- 哪個外部 action 尚未執行；
- 哪個 approval 已過期。

這就是 continuity gap。

---

# 1. Mobility Transition 是一種高階 interruption

從辦公桌起身：

$$
Desktop
\rightarrow
Walk
\rightarrow
Car.
$$

這不一定是典型 cognitive experiment 裡的 interruption。

但結構上包含：

1. task suspension；
2. context change；
3. interface change；
4. attention reallocation；
5. possible delay；
6. task resumption。

因此可以把 mobility transition 視為：

$$
\boxed{
\text{Interruption}
+
\text{Context Migration}
+
\text{Surface Migration}.
}
$$

---

# 2. Resumption Lag

經典 task-interruption research 使用：

$$
\boxed{
L_R
=
t_{\text{first resumed action}}
-
t_{\text{interruption end}}.
}
$$

即 resumption lag。

它測量：

> 中斷結束後，要多久才能真正重新開始原任務？

對 mobility system，可以擴張為：

$$
\boxed{
L_R^{mob}
=
t_{\text{meaningful continuation}}
-
t_{\text{new surface available}}.
}
$$

---

# 3. Resume 不等於 Open App

如果：

```text
Phone
→ Windows PC
```

成功把同一 app 打開，

但人仍要：

- 找 conversation；
- 找 document；
- 找 page；
- 找 paragraph；
- 想下一步；

則：

$$
\boxed{
AppResume
\neq
TaskResume.
}
$$

---

# 4. Task Identity

本文定義 activity identity：

$$
\boxed{
ID_{act}
}
$$

它不等於：

$$
ApplicationID.
$$

同一 activity 可能跨：

- PDF reader；
- voice assistant；
- browser；
- notebook；
- coding environment；
- car display。

所以：

$$
\boxed{
Activity
>
Application.
}
$$

---

# 5. Externalized Continuity State

定義：

$$
\boxed{
\mathcal C^{act}_t
=
(
G_t,
Q_t,
X_t,
F_t,
N_t,
U_t,
K_t,
P_t,
M_t
).
}
$$

## $G_t$ — Goal

我要完成什麼？

## $Q_t$ — Current Frontier

現在做到哪一個 subgoal？

## $X_t$ — Context

目前理解所需的 relevant context。

## $F_t$ — Artifact / World State

正式文件、遊戲狀態、媒體播放點、conversation state。

## $N_t$ — Next Action

下一步最可能要做什麼？

## $U_t$ — Open Loops

尚未回答的問題、疑點、待確認事項。

## $K_t$ — Cue Bundle

幫助快速恢復的提示。

## $P_t$ — Authority / Privacy

哪些 action 還被允許？

## $M_t$ — Current Representation

目前使用什麼 Surface / modality？

---

# 6. 這不是完整「腦狀態」

本文刻意拒絕：

$$
\boxed{
\mathcal C^{act}_t
=
\text{Human Mind}.
}
$$

人的：

- 情緒；
- 感質；
- 隱性記憶；
- 身體狀態；
- 未外化聯想；

不可能被本文完整表示。

所以更準確：

$$
\boxed{
\mathcal C^{act}_t
=
\text{Resumption-Relevant External State}.
}
$$

---

# 7. Mobility Cognitive Continuity 的弱定義

若一個活動從 $t_0$ 到 $t_1$ 滿足：

$$
ID_{act}(t_0)=ID_{act}(t_1),
$$

且：

$$
Goal(t_0)\simeq Goal(t_1),
$$

$$
Artifact(t_0)\simeq Artifact(t_1),
$$

$$
Authority(t_1)
$$

有效，

則可稱為：

$$
\boxed{
\text{Weak Activity Continuity}.
}
$$

---

# 8. 強一點的定義

若另外：

$$
L_R^{mob}<\tau_R,
$$

$$
D_{\text{semantic}}<\tau_S,
$$

$$
D_{\text{artifact}}=0,
$$

$$
D_{\text{authority}}=0,
$$

則：

$$
\boxed{
\text{Operational Mobility Continuity}.
}
$$

---

# 9. Continuity Equivalence

可定義活動狀態等價關係：

$$
\mathcal C^{act}_{t_0}
\sim_{\epsilon}
\mathcal C^{act}_{t_1}
$$

若：

$$
D(
\mathcal C^{act}_{t_0},
\mathcal C^{act}_{t_1}
)
<\epsilon.
$$

但 distance 不是每個欄位平均。

Authority mismatch 必須 hard fail。

---

# 10. Hard Invariants

不可漂移：

- principal identity；
- canonical artifact identity；
- permission epoch；
- external action receipt；
- activity identity。

因此：

$$
\boxed{
D_{\text{authority}}>0
\Rightarrow
ContinuityFail.
}
$$

即使 summary 很漂亮也不算成功。

---

# 11. Soft Variables

可以改變：

- modality；
- visual layout；
- wording；
- audio voice；
- screen size；
- summary granularity。

所以：

$$
\boxed{
RepresentationChange
\not\Rightarrow
ActivityChange.
}
$$

---

# 12. Same Activity, Different Surface

Desktop：

$$
PDF
+
Keyboard
+
References.
$$

Vehicle：

$$
VoiceDiscussion
+
LargeDisplay
+
ShortGlance.
$$

Arrival：

$$
PDF
+
Notes
+
CitationGraph.
$$

只要：

$$
ID_{act}
$$

不變，就是同一 activity。

---

# 13. Same Interface, Different Activity

反過來：

同一個 chat window：

$$
ChatUI
$$

可以先談：

$$
Task_A
$$

後談：

$$
Task_B.
$$

所以：

$$
\boxed{
SameUI
\not\Rightarrow
SameActivity.
}
$$

---

# 14. 經典 interruption research 的第一個啟示

Trafton et al. 2003 顯示：

> 在 interruption 前有短暫準備時間，可以讓人更快恢復。

這表示：

$$
\boxed{
\text{Prepare-to-Resume}
}
$$

本身可以被系統化。

---

# 15. Interruption Lag

定義：

$$
L_I
=
t_{\text{interruption start}}
-
t_{\text{warning}}.
$$

在 mobility：

> 車要到了。

> 飛機要登機了。

> 五分鐘後到站。

這些都可以形成：

$$
\boxed{
\text{Preparation Window}.
}
$$

---

# 16. Preparation Window 的 AI 用途

系統可以在 transition 前：

- checkpoint；
- summarize；
- capture next action；
- store open loops；
- close unsafe UI；
- migrate media；
- save source position；
- verify authority。

所以：

$$
\boxed{
MobilityWarning
\rightarrow
ResumePreparation.
}
$$

---

# 17. Contextual Cues

Hodgetts & Jones 2006 指出：

> context at suspension and retrieval is critical to efficient interruption recovery.

因此：

$$
\boxed{
Resume
\neq
Only State.
}
$$

還需要：

$$
\boxed{
ResumeCue.
}
$$

---

# 18. Cue Bundle

本文定義：

$$
\boxed{
K_t
=
(
LastAction,
NextAction,
CurrentObject,
OpenLoop,
VisualAnchor,
TemporalAnchor
).
}
$$

例如：

```text
你剛讀到第 4.2 節。
上一個動作：標記 Eq. 17。
下一步：檢查假設 A3 是否與 Appendix B 衝突。
未解問題：作者沒有解釋邊界條件。
```

這比：

> 檔案已同步。

有用得多。

---

# 19. Cue Fidelity

定義：

$$
\boxed{
F_K
=
1-
D(K_{\text{suspend}},K_{\text{resume}}).
}
$$

若 resume cue 錯誤：

$$
F_K\downarrow.
$$

它甚至可能比沒有 cue 更危險。

---

# 20. 明顯 Cue 可能比隱晦 Cue 有效

2005 的 environmental-cue study 顯示 blatant cue 比 subtle cue 更能縮短 resumption。

所以設計上：

> 不要只在角落放一個「已恢復」。

應直接告訴人：

- 你剛在哪；
- 接下來是什麼。

---

# 21. 2025 assistant cue research

2025 Scientific Reports 研究在 concurrent multitasking 中比較 retrieval cue / assistant cue。

結果支持：

$$
\boxed{
External Support
}
$$

可以在部分條件下降低恢復成本。

這直接支持 AI Continuity Guardian 的設計。

---

# 22. 2026 eye-tracking evidence

2026 Displays 的 programming-task interruption study 顯示：

- interruption 增加 task-completion cost；
- 增加跨區資訊檢查；
- resumption eye movement 能反映個體差異。

這提醒：

$$
\boxed{
ResumeCost
}
$$

不只是「多花幾秒」。

它可能包含：

- re-search；
- verification；
- context reconstruction。

---

# 23. Resumption Reconstruction Cost

定義：

$$
\boxed{
C_{\text{reconstruct}}
=
T_{\text{search}}
+
T_{\text{verify}}
+
T_{\text{re-read}}
+
T_{\text{re-plan}}.
}
$$

這比單一 resumption lag 更完整。

---

# 24. Mobility Continuity Loss

本文提出：

$$
\boxed{
L_{MCC}
=
w_RL_R
+
w_XD_X
+
w_FD_F
+
w_KD_K
+
w_PD_P
+
w_MD_M.
}
$$

其中：

- $L_R$：resumption lag；
- $D_X$：context drift；
- $D_F$：artifact drift；
- $D_K$：cue loss；
- $D_P$：permission / authority drift；
- $D_M$：mode / modality mismatch。

Authority drift 可設為 hard penalty。

---

# 25. Cross-Device Research：Task Migration

2024 CHI Extended Abstract：

**Opportunistic Nudges for Task Migration Between Personal Devices**

直接指出：

> moving from one device to another requires re-establishing context and can be cumbersome.

這正是 MCC 的 device-level 子問題。

---

# 26. Cross-Device Search

Wu & Dong 的 cross-device search research 將：

$$
\text{Task Preparation}
+
\text{Task Resumption}
$$

視為兩個階段。

這與本文：

$$
Suspend
\rightarrow
Resume
$$

的拆分一致。

---

# 27. Apple Handoff 是弱版 Activity Capsule

Apple 的 `NSUserActivity` 被定義為：

> app state at a moment in time.

Handoff 要求 app：

1. represent activity；
2. update activity；
3. send / receive；
4. restore activity。

這已經非常接近：

$$
\boxed{
\text{Activity State Transfer}.
}
$$

---

# 28. Apple 還要求 Minimal Restorable State

官方文件甚至建議：

> only transfer the minimal userInfo needed to recreate the activity.

這與本文的：

$$
\boxed{
Mobility Resume Capsule
}
$$

方向高度一致。

但 MCC 要跨越 app / ecosystem 邊界。

---

# 29. Android Cross Device Sessions

Android Cross device SDK 2026 Developer Preview 提供：

- device discovery；
- authorization；
- secure transfer；
- multidevice sessions；
- session transfer / shared session。

並明確列舉：

> seamless switching between devices in productivity apps.

所以：

$$
\boxed{
SessionMigration
}
$$

已是 platform-level 問題。

---

# 30. Windows Resume

Windows 2026 Cross-device Resume：

- Android activity；
- PC taskbar resume badge；
- PC 繼續 activity。

截至 2026 年 1 月支援的例子包括：

- Spotify；
- vivo Browser；
- WhatsApp。

這證明 continuation 不只限於 work。

---

# 31. Spotify 是重要例子

如果音樂：

$$
Track
+
Position
+
Queue
$$

可以跨裝置繼續，

那：

$$
\boxed{
EntertainmentContinuity
}
$$

與 Work Continuity 本質上同屬：

$$
ActivityContinuity.
$$

---

# 32. WhatsApp 也是重要例子

conversation：

$$
\mathcal R_t
$$

可以從 phone：

$$
\rightarrow
PC.
$$

這是：

$$
\boxed{
SocialContinuity.
}
$$

所以 MCC 不是企業工作專案。

---

# 33. Activity Types

本文至少定義：

$$
A
\in
\{
Work,
Entertainment,
Social,
Creative,
Rest,
Idle,
AgentTask
\}.
$$

每種 continuity 的 required state 不同。

---

# 34. Work Continuity

需要：

- task；
- artifact；
- source refs；
- open loops；
- next action；
- authority；
- agent state。

---

# 35. Entertainment Continuity

例如影片：

$$
MediaID,
Position,
Subtitle,
AudioTrack,
DeviceState.
$$

遊戲：

$$
WorldState,
QuestState,
Inventory,
Checkpoint.
$$

故事：

$$
NarrativePosition,
CharacterState,
ChoiceState.
$$

---

# 36. Social Continuity

需要：

- participant；
- conversation；
- relationship scope；
- unread / pending；
- privacy；
- social mode。

---

# 37. Rest Continuity

這個很容易被忽略。

如果：

$$
Mode=REST
$$

從車到飯店，

continuity 應該保留：

- DND；
- music / ambience；
- work block；
- wake-up rule。

所以：

$$
\boxed{
RestCanBeContinuous.
}
$$

---

# 38. Idle Continuity

如果：

$$
Mode=IDLE,
$$

上車後不應：

> 偵測你閒著，所以幫你打開工作。

所以：

$$
\boxed{
IdleState
}
$$

也有 activity identity。

---

# 39. Continuity 不等於一直做

最重要的一條：

$$
\boxed{
\text{Continuity}
=
\text{Resumability},
}
$$

不等於：

$$
\boxed{
\text{Continuous Attention}.
}
$$

---

# 40. Pause Is a First-Class Operation

定義：

$$
\boxed{
Pause(Activity)
\rightarrow
Checkpoint.
}
$$

不是：

> 關掉 App。

---

# 41. Suspend Packet

Suspend 時生成：

- canonical ref；
- frontier；
- next action；
- cue；
- authority epoch；
- mode；
- privacy；
- expected resume context。

這就是 MRC 的來源。

---

# 42. Mobility Resume Capsule

定義：

$$
\boxed{
MRC
=
(
ID,
Goal,
Frontier,
Artifacts,
Last,
Next,
Open,
Cues,
Authority,
Privacy,
Mode,
SurfaceHint
).
}
$$

---

# 43. MRC 不是完整聊天紀錄

不應：

$$
MRC
=
\text{All History}.
$$

因為：

- 太大；
- 太慢；
- 洩漏；
- 雜訊；
- provider lock-in。

它應是：

$$
\boxed{
\text{Minimum Sufficient Resumption State}.
}
$$

---

# 44. Minimum Sufficient Resumption State

形式化：

找最小：

$$
MRC^*
$$

使：

$$
P(
\text{correct resume}
\mid
MRC^*
)
\ge\tau.
$$

同時：

$$
Size(MRC^*)
$$

盡量小。

---

# 45. Transition Type 1：Direct Handoff

例如：

$$
Desktop
\rightarrow
Vehicle.
$$

使用者幾乎立即繼續。

目標：

$$
L_R^{mob}\rightarrow0.
$$

---

# 46. Transition Type 2：Pause–Resume

例如：

$$
Work
\rightarrow
Lunch
\rightarrow
Work.
$$

中間不要求 agent 延續工作。

只要求：

$$
\boxed{
ResumeCorrectly.
}
$$

---

# 47. Transition Type 3：Modality Transformation

例如：

$$
VisualDocument
\rightarrow
VoiceDiscussion.
$$

需要：

$$
\boxed{
Semantic Preservation.
}
$$

不是 byte preservation。

---

# 48. Modality Transformation Loss

定義：

$$
\boxed{
D_M
=
D(
Sem(R_{source}),
Sem(R_{target})
).
}
$$

如果 voice summary 漏掉關鍵條件：

$$
D_M\uparrow.
$$

---

# 49. Transition Type 4：Agent Substitution

人離開 activity：

$$
Human
\rightarrow
Agent.
$$

例如：

- 搜尋；
- background analysis；
- compilation。

Agent 不繼承全部 authority。

所以：

$$
\boxed{
TaskHandoff
\not\Rightarrow
AuthorityHandoff.
}
$$

---

# 50. Transition Type 5：Deferred Human Review

Agent 做：

$$
SafeSubtask.
$$

人到達後：

$$
Review.
$$

這是 B-02 `AGENT_ONLY` 的 continuity 版本。

---

# 51. Transition Type 6：Environment Rebinding

同一 activity 進入新空間：

$$
Office
\rightarrow
Car
\rightarrow
Aircraft
\rightarrow
Hotel.
$$

需要重新綁定：

- display；
- audio；
- privacy；
- network；
- input；
- DND；
- local hardware。

---

# 52. Environment Rebinding 不得改 Activity Identity

所以：

$$
\boxed{
Rebind(Environment)
\not\Rightarrow
Fork(Activity).
}
$$

除非使用者真的建立 fork。

---

# 53. Fork 是另一種合法行為

有時使用者想：

> 這份文件的車上版我先探索另一條方向。

那應顯式：

$$
\boxed{
Fork(Activity).
}
$$

而不是讓 system 默默造成 drift。

---

# 54. Fork / Merge

定義：

$$
A_0
\rightarrow
\{
A_1,A_2
\}.
$$

之後：

$$
Merge(A_1,A_2)
$$

必須處理：

- artifact；
- decision；
- authority；
- conflict；
- provenance。

---

# 55. Artifact Identity

Artifact continuity 最重要：

$$
\boxed{
ArtifactID
}
$$

與：

$$
Version.
$$

不能只傳：

> 一段 summary。

Formal source 仍需 canonical artifact。

---

# 56. Source-of-Record

這承接 A-03：

$$
\boxed{
Rendition
\neq
SourceOfRecord.
}
$$

車上聽到的 summary 不是論文原稿。

---

# 57. Last Meaningful Action

MRC 必須保存：

$$
\boxed{
LastMeaningfulAction.
}
$$

不是最後一個 mouse click。

例如：

> 已經否決假設 H2。

比：

> 最後點了第 18 頁。

更有恢復價值。

---

# 58. Next Intended Action

同樣：

$$
\boxed{
NextIntendedAction.
}
$$

是非常強的 cue。

例如：

> 下一步比較 Table 4 與 Appendix C。

這能直接降低 reconstruction。

---

# 59. Open Loops

未完成問題：

$$
U_t
=
\{u_1,u_2,\ldots,u_n\}.
$$

例如：

- 這個來源還沒驗證；
- 公式 B 尚未推完；
- 對方還沒回覆；
- 需要 approval。

如果 open loops 丟失：

$$
ContinuityQuality\downarrow.
$$

---

# 60. Negative State 也要保存

不只「做了什麼」。

還要：

- 已排除什麼；
- 不要做什麼；
- 哪個假設失敗；
- 哪個 action 禁止 retry。

所以 MRC 應有：

$$
\boxed{
Constraints / Rejections.
}
$$

---

# 61. Resume Cue 不應生成幻覺

AI 若不確定：

> 我記得你剛才好像要……

就可能造成：

$$
FalseCue.
$$

因此 cue 需要：

- provenance；
- confidence；
- source refs。

---

# 62. Cue Provenance

例如：

```yaml
next_action:
  value: "compare appendix C"
  source: "user_explicit"
  source_event: "evt_123"
```

比：

```yaml
next_action: "compare appendix C"
```

可靠。

---

# 63. Cue Classes

可分：

## Explicit

使用者明確說：

> 記得下一步做 X。

## Derived

系統從 task graph 推得。

## Environmental

screen position / selected object。

## Temporal

deadline / arrival。

## Social

conversation / pending reply。

---

# 64. Cue Priority

Resume 不應丟 30 個提示。

可以排序：

$$
\boxed{
Score(K_i)
=
Relevance
+
Reliability
+
Urgency
-
Noise.
}
$$

---

# 65. Warm Resume

一種 UX：

```text
你剛才在處理：
1. 主題
2. 做到哪
3. 未完成
4. 下一步
```

使用者：

> 繼續。

這是：

$$
\boxed{
Warm Resume.
}
$$

---

# 66. Silent Resume

對低風險 entertainment：

例如 Spotify：

直接：

$$
PlaybackResume.
$$

不需要提示。

所以：

$$
\boxed{
ResumeUX
=
f(ActivityType,Risk,Complexity).
}
$$

---

# 67. Review Resume

高風險 work：

先顯示：

- artifact；
- last action；
- pending external action；
- authority。

再允許繼續。

這是：

$$
\boxed{
Review Resume.
}
$$

---

# 68. Driver Resume

若人在駕駛：

不應顯示完整 work resume。

可以：

$$
\boxed{
DeferredResume.
}
$$

例如：

> 我已保存工作狀態，抵達後恢復。

這直接接 B-04。

---

# 69. Passenger Resume

Passenger：

可以：

- voice；
- screen；
- keyboard；
- AI。

所以：

$$
ResumeMode
$$

更完整。

---

# 70. Shared Vehicle Resume

Shared robotaxi 還要：

- temporary surface trust；
- local cache；
- privacy；
- teardown。

所以 MCC 必須承接 A-06 sovereignty。

---

# 71. Resume Authority Refresh

MRC 裡可以保存：

$$
permission\_epoch=42.
$$

但 resume 時：

$$
\boxed{
RefreshAuthority.
}
$$

不能直接信舊 epoch。

---

# 72. Pending External Actions

最危險：

```text
Send Email
```

在 transition 時 timeout。

MRC 必須知道：

$$
Status
\in
\{
Pending,
Succeeded,
Failed,
Unknown
\}.
$$

Unknown 不能 blind retry。

---

# 73. Continuity Guardian

Series A A-04 的 Continuity Guardian 在 B-03 變成 mobility transition manager。

責任：

1. detect transition；
2. checkpoint；
3. create MRC；
4. verify target surface；
5. rebind modality；
6. refresh authority；
7. generate cues；
8. observe resume。

---

# 74. Transition Detection

trigger 可以是：

- device proximity；
- calendar；
- vehicle arrival；
- Bluetooth；
- ride session；
- boarding；
- manual command；
- location；
- network change。

但自動偵測要受 privacy 控制。

---

# 75. User-Initiated Transition

最安全：

> 移到車上繼續。

生成：

$$
TransitionRequest.
$$

---

# 76. Predictive Transition

例如：

> 5 分鐘後 Uber 到。

AI 預先：

- checkpoint；
- prepare voice summary。

但不應擅自：

- send；
- modify；
- close irreversible task。

---

# 77. Transition Readiness Score

可定義：

$$
\boxed{
R_T
=
f(
Checkpoint,
Artifact,
Cue,
Authority,
Surface,
Network
).
}
$$

如果：

$$
R_T<\tau,
$$

就不要承諾「無縫」。

---

# 78. Continuity Score

定義：

$$
\boxed{
C_{MCC}
=
w_GC_G
+
w_QC_Q
+
w_FC_F
+
w_KC_K
+
w_PC_P
+
w_MC_M.
}
$$

但 authority：

$$
C_P
$$

可設為 hard gate。

---

# 79. Resume Accuracy

定義：

$$
\boxed{
A_R
=
P(
\text{first resumed action is appropriate}
).
}
$$

不是只看速度。

---

# 80. Fast Wrong Resume Is Worse

如果：

$$
L_R\downarrow
$$

但：

$$
A_R\downarrow,
$$

那不是改善。

所以：

$$
\boxed{
\text{Resume Quality}
\neq
1/L_R.
}
$$

---

# 81. Cognitive Reconstruction Effort

可測：

- eye movement；
- re-reading；
- search；
- repeated query；
- repeated file opening；
- self-report。

這讓 MCC 可實驗。

---

# 82. Person-Specific Continuity

不同人：

$$
CueNeed_i
$$

不同。

2026 eye-tracking study 的個體差異提醒：

$$
\boxed{
OneResumeUI
\neq
OptimalForAll.
}
$$

---

# 83. Adaptive Cue Density

疲勞高：

$$
CueDensity\uparrow
$$

可能更好。

熟悉 task：

$$
CueDensity\downarrow.
$$

需要實驗。

---

# 84. MCC for Long Interruptions

2021 dynamic-task research 顯示 interruption length 增加，resumption lag 與 accuracy cost 加重。

所以長途 flight：

$$
PauseDuration\uparrow
$$

更需要：

- richer cue；
- stronger checkpoint；
- summary；
- artifact diff。

---

# 85. Short Handoff vs Long Resume

## Short

Desktop → car in 2 min。

MRC 可以很薄。

## Long

Work → 8-hour flight → destination。

需要：

- session summary；
- changed external state；
- new messages；
- stale authority；
- task revalidation。

---

# 86. Staleness

定義：

$$
\boxed{
S_t
=
t_{\text{resume}}
-
t_{\text{checkpoint}}.
}
$$

若：

$$
S_t\uparrow,
$$

必須增加：

$$
Revalidation.
$$

---

# 87. External World Drift

你停下時：

$$
World=W_0.
$$

八小時後：

$$
W_1\neq W_0.
$$

所以：

$$
\boxed{
Resume
=
RestoreOldState
+
ReconcileNewWorld.
}
$$

不是單純 restore snapshot。

---

# 88. Social Conversation Drift

如果 conversation 中間：

- 對方又發 10 則；
- meeting time 改了；

resume 不能只停在舊訊息。

需要：

$$
\boxed{
CatchUp.
}
$$

---

# 89. Artifact Drift

若同事修改同文件：

$$
Version_{remote}>Version_{checkpoint}.
$$

resume 要：

- compare；
- merge；
- notify。

不能默默覆寫。

---

# 90. Agent Drift

Agent 背景工作可能：

- 完成；
- 失敗；
- 產生新 branch。

所以 human resume 時：

$$
\boxed{
AgentDelta
}
$$

必須進 cue。

---

# 91. Agent Review Packet

可包含：

```text
我離開後：
- 找到 4 個來源
- 排除 2 個
- 修改草稿 1 處
- 沒有執行任何外部副作用
- 有 1 個問題需要你判斷
```

這就是：

$$
\boxed{
Agent-to-Human Continuity.
}
$$

---

# 92. Human-to-Agent Continuity

人離開前：

```text
下一步找 2026 年的反例。
不要改正式稿。
不要發信。
```

MRC 把：

- goal；
- constraints；
- authority；

交給 agent。

---

# 93. Bi-Directional Handoff

最終：

$$
\boxed{
Human
\leftrightarrow
Agent
\leftrightarrow
Surface.
}
$$

其中每次 handoff 都要：

- state；
- authority；
- evidence。

---

# 94. Work Continuity Example

```text
Office:
read paper section 4

Transition:
checkpoint + open loop

Vehicle:
voice discussion on section 4

Agent:
find counterexamples

Arrival:
display sources + restore equation view
```

整體：

$$
ID_{act}
$$

不變。

---

# 95. Entertainment Continuity Example

```text
Home TV:
watch episode

Car:
audio recap / continue audio

Hotel:
resume video at correct scene
```

如果使用者不想 audio version：

$$
Pause
$$

也仍然 continuity。

---

# 96. Game Continuity Example

```text
Desktop:
strategy game

Vehicle:
AI gives world-state briefing
or no play

Destination:
resume exact save
```

activity 不要求始終 interactive。

---

# 97. Rest Continuity Example

```text
Car:
REST + DND

Hotel:
continue DND
ambient audio
no work resurfacing
```

這是：

$$
\boxed{
IntentContinuity.
}
$$

---

# 98. Idle Continuity Example

```text
Vehicle:
IDLE

Arrival:
do not auto-resume work
```

直到使用者：

> 繼續工作。

這非常重要。

---

# 99. Physical Presence Transition

有時到達的目的就是：

- meeting；
- dinner；
- signing；
- site visit。

所以 arrival 可能：

$$
WorkDigital
\rightarrow
PhysicalSocial.
$$

這仍然可屬同一 higher-level activity。

---

# 100. Hierarchical Activity Identity

定義：

$$
Activity
=
\{
Goal,
Subactivities
\}.
$$

例如：

$$
DealClosing
=
\{
Review,
Call,
Travel,
Meeting,
Signing
\}.
$$

交通不是 interruption。

它可能是：

$$
\boxed{
Subactivity.
}
$$

---

# 101. 這改變「交通中斷工作」的語言

如果 higher-level activity 是：

$$
Goal=CloseDeal,
$$

那：

$$
Travel
$$

可以是流程的一部分。

不是：

$$
Work
\rightarrow
Break
\rightarrow
Work.
$$

而是：

$$
\boxed{
Activity
\rightarrow
Activity
\rightarrow
Activity.
}
$$

---

# 102. Mobility as State Transition

可寫：

$$
\boxed{
\mathcal A_{t+1}
=
\Phi(
\mathcal A_t,
Surface,
Motion,
Network,
Attention,
Intent
).
}
$$

這是 B-03 的核心 state-transition view。

---

# 103. MCC 不要求零 transition cost

完全：

$$
L_{MCC}=0
$$

很可能不現實。

目標是：

$$
\boxed{
L_{MCC}\rightarrow\min.
}
$$

同時不破壞：

- safety；
- privacy；
- autonomy。

---

# 104. Sometimes Interruption Is Good

有些 task：

> 就應該停。

例如：

- 疲勞；
- complex visual work during driving；
- emotional overload。

所以：

$$
\boxed{
ContinuitySystem
\neq
AlwaysResumeSystem.
}
$$

---

# 105. Resume Eligibility

定義：

$$
E_R
=
f(
Safety,
Attention,
Privacy,
Motion,
TaskRisk,
UserIntent
).
$$

如果：

$$
E_R=0,
$$

就：

$$
Defer.
$$

---

# 106. B-04 的接口

B-04 將回答：

> 哪個座位／角色／空間現在有多少 interaction budget？

所以 B-03 輸出：

- activity；
- MRC；
- desired modality；
- resume urgency；
- privacy；
- task risk。

B-04 回傳：

- allowed modalities；
- attention budget；
- safety class；
- zone privacy。

---

# 107. B-05 的接口

B-05 的 Cabin Runtime 將根據：

$$
MRC
+
ZoneContract
$$

配置：

- display；
- projection；
- audio；
- mic；
- lighting；
- agent surface。

---

# 108. B-06 的接口

Mobility Hospitality 可以把：

$$
\text{continuity quality}
$$

變成付費服務的一部分。

例如：

- Work Continuity；
- Quiet Continuity；
- Family Continuity；
- Entertainment Continuity。

---

# 109. 可證偽命題 H1

提供 explicit next-action cue：

$$
L_R^{mob}\downarrow.
$$

可在 simulated vehicle transition 中測。

---

# 110. H2

只同步 raw artifact，不同步 open loops：

$$
C_{\text{reconstruct}}
\uparrow.
$$

---

# 111. H3

MRC + cue：

$$
ResumeAccuracy\uparrow
$$

相比：

$$
FileSyncOnly.
$$

---

# 112. H4

Modality transformation 若保留 activity frontier：

$$
D_{\text{semantic}}
$$

可以維持低值。

---

# 113. H5

AGENT_ONLY handoff 可以：

$$
HumanAttentionLoad\downarrow
$$

且：

$$
TaskProgress\uparrow
$$

而不提高 external side-effect rate。

---

# 114. H6

長 interruption 的最佳 cue bundle 應比短 interruption 更豐富。

---

# 115. H7

共享 vehicle 若 privacy context 未納入 MRC：

$$
PrivacyIncidentRate\uparrow.
$$

---

# 116. H8

Resume 系統若只最小化速度：

$$
L_R,
$$

可能提高：

$$
ResumeError.
$$

因此多目標最佳化優於單目標。

---

# 117. MCC Evaluation Vector

定義：

$$
\boxed{
\mathcal V_{MCC}
=
(
L_R,
A_R,
C_{\text{reconstruct}},
D_X,
D_F,
D_P,
D_M,
F_K
).
}
$$

---

# 118. Product KPI

應追蹤：

- resume success；
- resume accuracy；
- context reconstruction time；
- repeated search count；
- artifact drift；
- stale-authority block；
- false cue rate；
- user-cancelled auto-resume；
- privacy-safe transition；
- agent handoff completion。

---

# 119. Anti-KPI

不要只看：

> 幾次成功自動恢復。

如果人一直：

> 不要再自動打開工作。

那系統其實失敗。

所以：

$$
\boxed{
AutoResumeRate
\neq
ContinuityQuality.
}
$$

---

# 120. Canonical MCC Pipeline

最後收斂：

$$
\boxed{
Suspend
\rightarrow
Externalize
\rightarrow
Transfer
\rightarrow
Rebind
\rightarrow
Cue
\rightarrow
Resume.
}
$$

## Suspend

合法停止。

## Externalize

保存 resumption-relevant state。

## Transfer

跨 Surface / provider / network。

## Rebind

對新環境重新綁定 representation。

## Cue

提供適當恢復提示。

## Resume

恢復同一 activity 或明確 defer。

---

# 121. 最核心的四條不變量

第一：

$$
\boxed{
\text{Activity Continuity}
\neq
\text{Interface Persistence}.
}
$$

第二：

$$
\boxed{
\text{Continuity}
\neq
\text{Continuous Human Attention}.
}
$$

第三：

$$
\boxed{
\text{State Transfer}
+
\text{Cue Transfer}
>
\text{Raw Data Transfer Alone}.
}
$$

第四：

$$
\boxed{
\text{Task Handoff}
\not\Rightarrow
\text{Authority Handoff}.
}
$$

---

# 122. 結論

移動空間真正困難的問題不是：

> 車上到底能不能放螢幕？

也不是：

> 能不能連上雲端？

這些能力早已部分存在。

真正長期被低估的是：

> **人在位置、裝置、介面與注意力條件改變後，要付出多少成本才能重新成為「剛才那個正在做同一件事的人」？**

經典 interruption research 早已顯示 task resumption 具有 measurable cost，而 contextual cue 與 prepare-to-resume 能降低其中一部分。現代 Apple Handoff、Android Cross-device Sessions 與 Windows Resume 則說明 activity continuation 已經從研究問題進入產品平台。

MCC 將這兩條線再向 mobility 展開：

$$
\boxed{
\text{Mobility Transition}
}
$$

不應只搬移資料。

它應搬移：

$$
\boxed{
\text{Activity Identity}
+
\text{Task Frontier}
+
\text{Artifact State}
+
\text{Open Loops}
+
\text{Authority}
+
\text{Resumption Cues}.
}
$$

而且 continuity 最重要的不是要求人一直 attention-on。

人可以：

- 暫停；
- 休息；
- 睡；
- 娛樂；
- 讓 Agent 繼續；
- 到目的地再回來。

真正應該持續的是：

$$
\boxed{
\text{The Possibility of Correct Resumption}.
}
$$

因此：

$$
\boxed{
\text{Physical Transition}
\not\Rightarrow
\text{Activity Reset}.
}
$$

這就是 B-03 的核心。

下一篇 B-04 將進一步限制這個命題：即使 activity 可以被正確恢復，也不代表每個位置、每個座位、每個駕駛狀態都允許同樣的 modality 與 attention load。真正的 mobility system 必須把 continuity 放進 Spatial Attention Zones 之中。

---

# 參考文獻與技術錨點

1. Trafton, J. G., Altmann, E. M., Brock, D. P., & Mintz, F. E. (2003). **Preparing to resume an interrupted task: effects of prospective goal encoding and retrospective rehearsal.** International Journal of Human-Computer Studies, 58(5), 583–603.  
   DOI: `10.1016/S1071-5819(03)00023-5`

2. Altmann, E. M., & Trafton, J. G. (2004). **Task Interruption: Resumption Lag and the Role of Cues.** Proceedings of the Cognitive Science Society.

3. Hodgetts, H. M., & Jones, D. M. (2006). **Contextual cues aid recovery from interruption: the role of associative activation.** Journal of Experimental Psychology: Learning, Memory, and Cognition, 32(5), 1120–1132.  
   DOI: `10.1037/0278-7393.32.5.1120`

4. **The effects of cues on task interruption recovery in a concurrent multitasking environment.** Scientific Reports, 2025.  
   DOI: `10.1038/s41598-025-09358-4`

5. Wen, Z., Ba, J., Yang, J., & Zhou, Y. (2026). **Understanding user resumption behavior after task interruptions: An eye-tracking-based empirical study.** Displays.  
   DOI: `10.1016/j.displa.2026.103618`

6. Wu, D., & Dong, J. (2020). **Understanding task preparation and resumption behaviors in cross-device search.** Journal of the Association for Information Science and Technology.  
   DOI: `10.1002/asi.24307`

7. Joshi, N., et al. (2024). **Opportunistic Nudges for Task Migration Between Personal Devices.** Extended Abstracts of the 2024 CHI Conference on Human Factors in Computing Systems.  
   Microsoft Research: `https://www.microsoft.com/en-us/research/publication/opportunistic-nudges-for-task-migration-between-personal-devices/`

8. Apple Developer Documentation. **Implementing Handoff in Your App.**  
   `https://developer.apple.com/documentation/foundation/implementing-handoff-in-your-app`

9. Android Developers. **Cross device SDK.** Last updated 2026-05-07 UTC on the checked page.  
   `https://developer.android.com/guide/topics/connectivity/cross-device-sdk/overview`

10. Microsoft Learn / Support. **Windows Resume / Cross-device Resume Feature.** 2026 documentation.  
    `https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/cross-device-resume-overview`  
    `https://support.microsoft.com/windows/cross-device-resume-feature-9ada0c0b-f70f-4806-abac-b7126fa6a053`

11. **Resuming a Dynamic Task Following Increasingly Long Interruptions: The Role of Working Memory and Reconstruction.** Frontiers in Psychology, 2021.  
    DOI: `10.3389/fpsyg.2021.659451`

---

# 內部依賴

1. `B01_Programmable_Mobility_Space_General_Theory_v0.1.md`
2. `B02_Travel_Time_Reclamation_v0.1.md`
3. `DEPENDENCY_MAP_A_to_B.md`
4. Series A A-02 Persistent Communication State
5. Series A A-03 Multimodal-Native Communication
6. Series A A-04 AI Communication Runtime
7. Series A A-06 Personal Communication Sovereignty
8. Series A A-07 EVEMISS Communication Continuum Architecture

---

# 文件狀態

**Series：** B｜Programmable Mobility & Spatial Continuum  
**Number：** B-03  
**Version：** v0.1  
**Status：** Research Paper / Canonical Source  
**Series B progress：** 3/7  
**Overall 15-document progress：** 10/15  
