---
title: "Spatial Attention Zones：駕駛、副駕、後座、隱私與安全注意力分區"
subtitle: "Spatial Attention Zones: A Role-, Safety-, Privacy-, and Modality-Aware Zoning Model for Programmable Mobility Spaces"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Paper / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series B｜Programmable Mobility & Spatial Continuum"
series_number: "B-04"
canonical_source: true
encoding: "UTF-8"
---

# Spatial Attention Zones：駕駛、副駕、後座、隱私與安全注意力分區

## Spatial Attention Zones: A Role-, Safety-, Privacy-, and Modality-Aware Zoning Model for Programmable Mobility Spaces

**系列：** Series B｜Programmable Mobility & Spatial Continuum  
**編號：** B-04  
**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Paper / Canonical Source  

---

# 摘要

B-01 將交通工具重新描述為 Programmable Mobility Space；B-02 將旅程時間拆解為 forced、self-directed、work 與 reserve time；B-03 則提出 Mobility Cognitive Continuity，主張活動身份、task frontier、Artifact、open loops、authority 與 resumption cues 可以跨 Surface 與物理位移持續。然而，MCC 仍需要一個更嚴格的安全限制：

> **同一個活動即使可以被正確恢復，也不代表車內所有座位、所有乘員、所有駕駛狀態、所有螢幕、所有聲音與所有時間都允許同樣的互動。**

本文提出：

# **Spatial Attention Zones（SAZ）**
## **空間注意力分區**

SAZ 將一個移動空間拆解為多個具有不同角色、安全、注意力、隱私、顯示、聲學、輸入、權限與環境條件的動態區域。其核心不是「前座／後座」這種固定幾何標籤，而是：

$$
\boxed{
Z_i(t)
=
(
R_i,
B_i,
S_i,
V_i,
H_i,
P_i,
U_i,
A_i,
N_i,
E_i
)
}
$$

其中：

- $R_i$：occupant role；
- $B_i$：available attention budget；
- $S_i$：safety / driving-state constraint；
- $V_i$：visual surface capability；
- $H_i$：audio / acoustic capability；
- $P_i$：privacy / audience state；
- $U_i$：input / interaction capability；
- $A_i$：authority / allowed action scope；
- $N_i$：network / connectivity condition；
- $E_i$：environment / motion state。

因此：

$$
\boxed{
\text{Same Vehicle}
\neq
\text{Same Interaction Domain}.
}
$$

本文第一個核心命題是：**Occupant Zone、Attention Zone、Privacy Zone、Audio Zone 與 Authority Zone 不必一一重合。** Android Automotive 已有 occupant zone 抽象，可把 driver、front passenger、rear passenger 與各自 display / user 映射分離；2026 年 AAOS 的 multi-user / multi-display 與 per-display UX restriction 進一步顯示不同乘員顯示可以使用不同限制。但本文的 SAZ 是更高層抽象：一個座位可以同時屬於私人音訊區、共享顯示區、低視覺注意力區與高個人資料權限區。

第二個核心命題是：

$$
\boxed{
\text{Available Feature}
\neq
\text{Allowed Interaction}.
}
$$

某個螢幕能播放影片，不表示駕駛時允許使用；某個 Agent 能處理工作，不表示駕駛者此刻應看到完整文件；某個車艙有大螢幕，也不表示其內容可以被共享乘員看到。2026 年 Android for Cars 仍把 driver distraction 當成硬性品質要求；某些 video / game / browser 類別在 driving restriction 生效時不可 launch 或顯示。NHTSA 的 visual-manual distraction framework 與 Euro NCAP 2026 driver monitoring / HMI 評估同樣把駕駛注意力視為不可用 productivity 抵銷的安全約束。

第三個核心命題是：**Zone 不一定需要物理隔間。** 2025–2026 年車艙 personal sound zone 研究已使用 headrest loudspeakers、active noise control、acoustic contrast control 等方法，在同一車艙為不同座位建立 bright / dark acoustic zones；Android Automotive 也允許不同 occupant zones 具有自己的 display / user state。因此未來空間分區可能同時由：

- geometry；
- display assignment；
- directional audio；
- beamformed microphone；
- ANC；
- privacy glass；
- wearable audio；
- software policy；

共同構成。

第四個核心命題是：**Attention Zone 必須動態更新。** 駕駛不是永久角色，乘客也不是永久高注意力狀態。人工駕駛、Level 2 assisted driving、Level 3 conditional automation、Level 4 driverless operation、停車、緊急接管、疲勞與不同 motion state，都會改變可允許的 interaction budget。因此本文不把 SAE automation level 直接等同於 SAZ level，而是以 driving responsibility、fallback obligation、occupant role、driver monitoring 與 OEM / regulatory safety contract 共同決定。

本文進一步提出：

$$
\boxed{
InteractionAllowed
=
\mathbf 1
\left[
D_{\text{task}}
\preceq
B_i(t)
\right]
\cdot
\mathbf 1
\left[
Policy(Z_i,t)=Allow
\right]
}
$$

其中 $D_{\text{task}}$ 是一個活動對視覺、聽覺、手部、認知與回應速度的需求向量， $B_i(t)$ 則是該 zone 當下的注意力／互動預算。若某一維超出安全上限，系統必須 transform、defer 或 block，而不是只把字變小。

本文最後提出 **Zone Contract**、**Interaction Demand Vector**、**Zone Capability Vector**、**Privacy Audience Contract**、**Acoustic Zone Contract** 與 **Dynamic Zone Transition**，並將 B-03 的 Mobility Resume Capsule 接入 SAZ：MRC 只描述「想恢復什麼」，SAZ 決定「現在在哪裡可以用什麼方式恢復」。

Series B-05 將在這個約束模型上建立 AI-Native Vehicle Cabin，把 display、projection、spatial audio、microphone、lighting、seat、environment、AI 與 Continuity Runtime 正式組裝成可實作的車艙架構。

---

# Abstract

Mobility Cognitive Continuity establishes that an activity can remain resumable across physical transitions, but resumability does not imply that every vehicle occupant, seat, display, acoustic field, or driving state may support the same interaction. This paper introduces Spatial Attention Zones (SAZ), a dynamic zoning model for programmable mobility spaces.

A SAZ combines occupant role, attention budget, driving-state constraints, visual capability, acoustic capability, privacy, input capability, authority, connectivity, and environmental state. It explicitly separates occupant zones from attention, privacy, acoustic, and authority zones. These layers can overlap without being identical.

The paper builds on current automotive engineering anchors. Android Automotive provides occupant-zone abstractions that map driver, front-passenger, and rear-passenger roles to users and displays, while current multi-user / multi-display support allows dedicated passenger interfaces and per-display restrictions. Android for Cars continues to enforce driver-distraction restrictions, and Euro NCAP's 2026 protocols place greater emphasis on driver monitoring, HMI clarity, and real-time driver engagement. Recent personal-sound-zone research demonstrates that separate acoustic listening regions can be created in the same vehicle cabin without physical walls.

The paper defines an interaction-demand vector and a zone-capability vector. An interaction is allowed only when task demands fit within the current zone budget and all hard safety, privacy, authority, and policy constraints are satisfied. Unsafe interaction must be transformed, deferred, or blocked rather than merely reformatted.

Finally, SAZ is connected to the Mobility Resume Capsule from B-03: the capsule states what activity should resume, while the zone contract determines whether, where, and in which modality resumption may occur. The resulting architecture becomes the formal safety and spatial boundary for B-05's AI-native vehicle cabin.

---

# 0. 問題不是「車內有幾個螢幕」

如果一台車有：

- driver display；
- center display；
- passenger display；
- rear display；

仍然不能推出：

$$
\boxed{
\text{Four Displays}
=
\text{Four Safe Interaction Spaces}.
}
$$

因為 display 只是其中一層。

真正需要問：

- 誰在看？
- 他是否正在駕駛？
- 他現在可分配多少注意力？
- 內容是否私人？
- 旁邊誰聽得到？
- 這個 action 有沒有 authority？
- 車輛是否正在轉彎、煞車、接管？
- 系統是否處於 restricted driving mode？

---

# 1. Same Vehicle ≠ Same Interaction Domain

本文核心：

$$
\boxed{
\text{Same Vehicle}
\neq
\text{Same Interaction Domain}.
}
$$

車內可以存在：

$$
Z_1,Z_2,\ldots,Z_n.
$$

每個 $Z_i$ 的可用 interaction 不同。

---

# 2. Zone 不等於 Seat

最簡單：

$$
Seat_i
\rightarrow
Zone_i.
$$

但實際更複雜。

一個後座中央螢幕可能被兩個人共享。

一個 directional speaker 可能只服務一個 headrest。

一個 privacy glass 可能涵蓋後排。

一個 microphone beam 可能只鎖定某個說話者。

所以：

$$
\boxed{
Zone
\neq
Seat.
}
$$

---

# 3. Zone 也不等於 Physical Wall

如果：

- ANC；
- directional audio；
- personal display；
- wearable audio；
- beamformed microphone；

可以建立局部互動場，

則：

$$
\boxed{
Spatial Separation
\not\Rightarrow
Physical Partition.
}
$$

---

# 4. Zone State

定義：

$$
\boxed{
Z_i(t)
=
(
R_i,
B_i,
S_i,
V_i,
H_i,
P_i,
U_i,
A_i,
N_i,
E_i
).
}
$$

---

# 5. $R_i$ — Occupant Role

至少：

$$
R_i
\in
\{
Driver,
FrontPassenger,
RearPassenger,
SharedPassenger,
NoOccupant
\}.
$$

未來 autonomous-only vehicle 可以：

$$
Driver=\varnothing.
$$

Android Automotive 的 `CarOccupantZoneManager` 也已支援 driver、front passenger、rear passenger 等 occupant type，甚至允許沒有 driver zone 的 passenger-only system。

---

# 6. $B_i$ — Attention Budget

不是單一 scalar。

定義：

$$
\boxed{
B_i
=
(
B_i^V,
B_i^A,
B_i^M,
B_i^C,
B_i^R
)
}
$$

其中：

- $B^V$：visual；
- $B^A$：auditory；
- $B^M$：manual；
- $B^C$：cognitive；
- $B^R$：response / reaction reserve。

---

# 7. Attention Budget 不是「剩多少算多少」

尤其 driver：

$$
B_{\text{driver}}^R
$$

必須保留。

不能把：

$$
100\%
$$

注意力預算全部分配給：

- conference call；
- document；
- AI；
- entertainment。

Safety reserve 是 hard reserve。

---

# 8. Interaction Demand Vector

每個 task 定義：

$$
\boxed{
D_j
=
(
D_j^V,
D_j^A,
D_j^M,
D_j^C,
D_j^R
).
}
$$

例如：

## Passive audio

$$
D_{\text{audio}}
\approx
(
0,
low,
0,
low,
low
).
$$

## Reading dense PDF

$$
D_{\text{PDF}}
\approx
(
high,
low,
medium,
high,
medium
).
$$

## Video game

$$
D_{\text{game}}
\approx
(
high,
high,
high,
high,
high
).
$$

---

# 9. Interaction Feasibility

最基本：

$$
\boxed{
D_j
\preceq
B_i.
}
$$

即每一維 demand 不超過 budget。

但這只是必要條件。

還要：

$$
Policy=Allow.
$$

---

# 10. Hard Policy Gate

因此：

$$
\boxed{
Allowed(i,j,t)
=
Fit(D_j,B_i(t))
\land
SafetyAllow
\land
PrivacyAllow
\land
AuthorityAllow.
}
$$

---

# 11. Safety Cannot Be Traded

不能：

> 這個 task 非常有價值，所以多看 10 秒螢幕也沒關係。

因此：

$$
\boxed{
Safety
}
$$

是 hard constraint。

不是 weighted objective 裡的普通變數。

---

# 12. Driver Distraction 是一級限制

NHTSA 長期維持：

> in-vehicle visual-manual tasks 應在 driving 時被限制。

Android for Cars 2026 同樣把 driver distraction 放在 app quality gate。

例如 video / game / browser 類別在 driving restriction 生效時：

- 不可 launch；
- UI 不可 visible；
- 某些情況 audio 也必須停止。

所以：

$$
\boxed{
FeatureExists
\neq
DriverMayUse.
}
$$

---

# 13. Android Automotive 已經有 Occupant Zone

AAOS 的 occupant zone：

> maps a user to a set of displays.

而：

- driver；
- front passenger；
- rear passenger；

是 formal occupant types。

這是一個很重要的現成工程基礎。

---

# 14. Occupant Zone ≠ SAZ

但本文的：

$$
SAZ
$$

更大。

Android occupant zone 主要處理：

- user；
- display；
- audio zone；
- occupant type。

SAZ 另外加入：

- attention；
- safety；
- privacy；
- authority；
- activity demand；
- motion state；
- modality eligibility。

所以：

$$
\boxed{
OccupantZone
\subset
SpatialAttentionZone.
}
$$

---

# 15. Multi-User / Multi-Display

2026 AAOS 已支援：

$$
\boxed{
\text{Concurrent Multi-User}
+
\text{Multiple Displays}.
}
$$

不同 passenger 可以：

- 有自己的 Android user；
- 有自己的 main display；
- 有自己的 accounts / apps。

這使：

$$
\boxed{
\text{Per-Occupant Digital Space}
}
$$

成為實際平台能力。

---

# 16. Per-Display UX Restrictions

AAOS 已經可以：

> 對不同 physical / virtual display 套用不同 UX restrictions。

因此 passenger-only display 可以在 driving 時保留某些非 driver-optimized activity。

這幾乎就是：

$$
\boxed{
\text{Interaction Policy by Display / Zone}.
}
$$

的現成弱版本。

---

# 17. SAZ 要再往上做 Policy Composition

因為：

$$
DisplayPolicy
$$

不夠。

還需要：

$$
\boxed{
Policy
=
f(
Role,
DrivingState,
Display,
Audio,
Privacy,
Authority,
Activity
).
}
$$

---

# 18. Driver Zone

Driver Zone 的核心不是：

> 左前座。

而是：

$$
\boxed{
R=Driver
}
$$

且當下 human 負有 driving responsibility。

其 default：

- visual complexity low；
- manual interaction low；
- cognitive load bounded；
- response reserve high。

---

# 19. Front Passenger Zone

Front passenger 可能：

$$
B^V\uparrow
$$

$$
B^M\uparrow
$$

但仍受：

- driver peripheral distraction；
- display placement；
- privacy；
- motion sickness；

限制。

所以：

$$
\boxed{
Passenger
\neq
Unlimited.
}
$$

---

# 20. Rear Passenger Zone

Rear zone 通常最接近：

$$
\boxed{
Full Multimodal Surface.
}
$$

可支援：

- large display；
- keyboard；
- voice；
- call；
- game；
- work；
- entertainment。

但仍受：

- crash safety；
- motion；
- shared audience；
- privacy；
- network；

限制。

---

# 21. Shared Passenger Zone

例如 pooled robotaxi。

兩個陌生乘客：

$$
P_i
$$

很低。

即使兩人都不是 driver：

$$
\boxed{
AttentionHigh
\not\Rightarrow
PrivacyHigh.
}
$$

所以不能朗讀私人郵件。

---

# 22. Driverless Passenger-Only Vehicle

若：

$$
Driver=\varnothing
$$

也不表示：

$$
SafetyConstraint=\varnothing.
$$

還有：

- seat restraint；
- emergency；
- motion；
- evacuation；
- cabin interaction；
- cybersecurity。

所以：

$$
\boxed{
NoDriver
\neq
NoSafetyPolicy.
}
$$

---

# 23. SAE Automation Level 不等於 SAZ Level

SAE J3016 對 automation level 的核心是：

> dynamic driving task 由誰執行，以及 fallback / supervision 誰負責。

SAZ 關心：

> occupant 可以做什麼。

兩者相關但不等價。

所以：

$$
\boxed{
SAELevel
\neq
AttentionZoneClass.
}
$$

---

# 24. Level 0–2

依 SAE 的簡化 chart：

在 Level 0–2：

> human remains driving / supervising.

因此 SAZ 應保守：

$$
B_{\text{driver}}^V
\ll
B_{\text{passenger}}^V.
$$

---

# 25. Level 3

Level 3 的 feature 執行 driving，但：

> system request 時 human must drive。

所以：

$$
\boxed{
TakeoverResponsibility>0.
}
$$

SAZ 不能直接把 driver zone 變成 full office。

---

# 26. Level 4

在 feature 的 operational conditions 內：

> automated driving feature 不要求 human takeover。

此時 interaction budget 可能大幅增加。

但：

- ODD；
- emergency；
- seat / occupant safety；

仍存在。

---

# 27. Level 5

Full driving automation：

$$
DrivingResponsibility_{\text{human}}
\rightarrow0.
$$

這會最大程度釋放 cabin design freedom。

但：

$$
\boxed{
PhysicalSafety
\neq0.
}
$$

---

# 28. Dynamic Role Transition

例如：

$$
Passenger
\rightarrow
Driver.
$$

或：

$$
Driver
\rightarrow
PassengerLike.
$$

Zone policy 必須重新計算。

所以：

$$
\boxed{
Z_i(t)
}
$$

是時間函數。

---

# 29. Attention Is Dynamic

即使同一 passenger：

疲勞：

$$
B^C\downarrow.
$$

motion sickness：

$$
B^V\downarrow.
$$

開會：

$$
B^A\downarrow.
$$

睡眠：

$$
B^{all}\rightarrow0.
$$

---

# 30. Driver Monitoring

Euro NCAP 2026 增加：

- eye tracking；
- head tracking；
- driver performance monitoring；
- HMI clarity；
- unresponsive driver handling。

這代表：

$$
\boxed{
DriverState
}
$$

已被正式提升為安全系統 input。

---

# 31. Driver Monitoring ≠ Productivity Monitoring

非常重要：

$$
\boxed{
SafetyMonitoring
\neq
WorkplaceSurveillance.
}
$$

看 driver 是否打瞌睡，

不等於：

> 判斷他工作不夠專心。

---

# 32. Occupant Monitoring

未來 cabin 可以感知：

- seat occupancy；
- posture；
- seatbelt；
- gaze；
- fatigue；
- head position。

但應採：

$$
\boxed{
PurposeBoundedSensing.
}
$$

不能因 safety sensor 存在就無限用於廣告或工作績效。

---

# 33. Zone Privacy State

定義：

$$
\boxed{
P_i
=
(
Audience,
Visibility,
Audibility,
Capture,
Retention
).
}
$$

---

# 34. Audience

至少：

$$
Audience
\in
\{
Private,
TrustedShared,
WorkShared,
PublicShared,
Unknown
\}.
$$

---

# 35. Visibility

某 display：

$$
Visibility
=
\{WhoCanSee\}.
$$

前 passenger screen 可能：

- passenger 看得到；
- driver peripheral vision 也可能看得到。

所以 driver distraction policy 不能只問：

> 這是不是 passenger display？

---

# 36. Audibility

Audio：

$$
Audibility
=
\{WhoCanHear\}.
$$

speaker 不是天然 private。

---

# 37. Capture

車內：

- microphone；
- camera；

可能 capture。

所以：

$$
CaptureScope
$$

也屬 zone contract。

---

# 38. Retention

共享 robotaxi：

$$
LocalRetention
$$

應盡量低。

Ride end：

$$
\boxed{
Detach
\Rightarrow
EraseLocalSecrets
+
InvalidateSession
+
ClearPrivateCache.
}
$$

---

# 39. Audio Zone

定義：

$$
\boxed{
H_i
=
(
Playback,
Directionality,
Isolation,
Mic,
ANC,
Masking
).
}
$$

---

# 40. Personal Sound Zones 已不是純概念

2025 Applied Acoustics：

- headrest loudspeakers；
- ANC；
- bright / dark zones；
- in-car experiment。

在低頻區域取得可測 acoustic contrast。

2026 研究則繼續：

- modified acoustic contrast control；
- headrest loudspeaker array；
- stochastic cabin model。

所以：

$$
\boxed{
\text{Audio Zoning}
}
$$

有實驗工程基礎。

---

# 41. Zone 不需要完全無聲外洩

實際 PSZ：

$$
Isolation<\infty.
$$

所以 audio privacy 不能只看：

> 是否有 sound zone。

還需要：

$$
\boxed{
LeakageThreshold.
}
$$

---

# 42. Acoustic Privacy

若：

$$
SensitiveContent
$$

則需要：

$$
Leakage<\tau_P.
$$

否則：

- headphone；
- text；
- defer。

---

# 43. Microphone Zone

Beamformed microphone 可以：

$$
Focus(Speaker_i).
$$

但應避免：

- capture other passenger；
- save unrelated conversation。

所以：

$$
\boxed{
MicDirectionality
+
DataPolicy.
}
$$

---

# 44. Visual Zone

定義：

$$
V_i
=
(
Display,
FOV,
Size,
Brightness,
Privacy,
DriverExposure
).
$$

---

# 45. Driver Exposure

Passenger screen 如果 driver 看得到，

就有：

$$
Exposure_{\text{driver}}>0.
$$

所以：

$$
\boxed{
PassengerContent
}
$$

仍可能受 driver distraction rule 約束。

---

# 46. Privacy Display

可以用：

- narrow viewing angle；
- privacy film；
- directional backlight；
- wearable display；
- partition。

所以：

$$
ZonePrivacy
$$

也可以是 hardware + software。

---

# 47. Authority Zone

不同 occupant 可以有不同：

$$
A_i.
$$

例如：

Driver：

- route；
- climate；
- safety；
- call；

Rear passenger：

- entertainment；
- personal workspace；

Guest：

- 不能改 vehicle admin。

---

# 48. Vehicle Owner ≠ Current Passenger

共享車：

$$
Owner
\neq
Rider.
$$

所以：

$$
\boxed{
PhysicalPossession
\neq
DigitalAuthority.
}
$$

---

# 49. Authority Scope

定義：

$$
A_i
=
\{
Read,
Control,
Configure,
Communicate,
Purchase,
Admin
\}.
$$

---

# 50. Car Control Authority

例如：

- climate；
- seat；
- window；
- lighting；

可以 delegated。

但：

- driving stack；
- safety-critical actuator；

必須進更高 safety boundary。

---

# 51. Cabin AI ≠ Driving AI

延續 B-01：

$$
\boxed{
CabinIntelligence
\neq
DrivingAuthority.
}
$$

Cabin AI 可以：

- plan work；
- control entertainment；
- adjust allowed environment。

但不能因自然語言：

> 快一點。

就直接取得 raw driving control。

---

# 52. Interaction Transform

如果：

$$
D_j\npreceq B_i,
$$

不一定直接 block。

可以：

$$
\boxed{
Transform(j)
}
$$

例如：

PDF reading：

$$
\rightarrow
VoiceSummary.
$$

---

# 53. Transform Classes

## Visual → Audio

dense document：

$$
Visual
\rightarrow
AudioSummary.
$$

## Manual → Voice

typing：

$$
Keyboard
\rightarrow
Dictation.
$$

## Interactive → Deferred

game / editing：

$$
\rightarrow
Pause.
$$

## Full → Glanceable

dashboard：

$$
\rightarrow
One-line status.
$$

---

# 54. Transform Must Preserve Semantics

承接 A-03：

$$
\boxed{
D_{\text{semantic}}
<
\tau.
}
$$

如果 transform 失真：

$$
Defer.
$$

---

# 55. Interaction Decision

完整：

$$
\boxed{
Decision
\in
\{
Allow,
Transform,
Defer,
Block
\}.
}
$$

---

# 56. Allow

demand fits。

---

# 57. Transform

可以安全降階。

---

# 58. Defer

activity legitimate，但此時不適合。

---

# 59. Block

- unsafe；
- unauthorized；
- privacy violation。

---

# 60. B-03 Resume + B-04 Zone

MRC 說：

> 我要繼續看論文。

SAZ 說：

> 你現在在 Driver Zone，visual PDF 不允許。

因此：

$$
\boxed{
MRC
+
ZoneContract
\rightarrow
ResumePlan.
}
$$

---

# 61. ResumePlan

例如：

```yaml
activity: "paper_review_17"
zone: "driver"
decision: "DEFER"
reason: "visual_attention_budget"
on_safe_transition:
  target_zone: "rear_passenger"
  preferred_modality: "visual_full"
```

---

# 62. Driver Voice Resume

另一例：

```yaml
decision: "TRANSFORM"
from: "visual_pdf"
to: "voice_summary"
constraints:
  no_dense_equations: true
  no_external_write: true
```

---

# 63. Passenger Full Resume

Rear passenger：

```yaml
decision: "ALLOW"
modalities:
  - "visual"
  - "voice"
  - "keyboard"
```

---

# 64. Privacy Resume

Shared ride：

MRC 要播私人訊息。

SAZ：

$$
Audience=PublicShared.
$$

所以：

$$
\boxed{
Audio
\rightarrow
PrivateText
}
$$

或：

$$
Defer.
$$

---

# 65. Zone Contract

本文提出：

```yaml
zone_id: "rear_right"
occupant_role: "REAR_PASSENGER"
attention:
  visual: "high"
  auditory: "high"
  manual: "high"
  cognitive: "high"
  response_reserve: "low"
safety:
  driving_responsibility: false
visual:
  display: "private_main"
audio:
  playback_zone: "headrest_rr"
  leakage_class: "medium"
privacy:
  audience: "PRIVATE"
authority:
  allowed:
    - "personal_apps"
    - "communication"
    - "cabin_controls"
network:
  expected: "variable"
```

---

# 66. Dynamic Zone Contract

Zone 可以因：

- role change；
- occupant change；
- automation state；
- seatbelt；
- motion；
- emergency；
- privacy；

重新產生。

---

# 67. Zone Transition Event

例如：

```text
DRIVER_ATTENTION_NORMAL
→ DRIVER_ATTENTION_DEGRADED
```

則：

- notification 減少；
- work audio defer；
- navigation priority ↑；
- safety alert priority ↑。

---

# 68. Emergency Zone

若：

$$
Emergency=1,
$$

所有：

- work；
- entertainment；

可能：

$$
\rightarrow
Suspend.
$$

Safety messages：

$$
Priority\rightarrow Max.
$$

---

# 69. Emergency Override

但 emergency override 不應：

> 暴露所有私人資料。

所以：

$$
\boxed{
SafetyOverride
\neq
PrivacyNullification.
}
$$

只開放必要資料。

---

# 70. Sleep Zone

若 passenger 睡眠：

$$
B_i\rightarrow0.
$$

但：

- emergency alert；
- destination wake；
- safety；

可以保留。

---

# 71. Rest Zone

B-02 的 Rest Mode 在空間上：

- dim light；
- DND；
- low audio；
- no work display。

這就是：

$$
\boxed{
TemporalMode
+
SpatialZone.
}
$$

---

# 72. Work Zone

Work Zone 不需要是一個 seat type。

它是：

$$
\boxed{
ZoneContract
+
ActivityMode.
}
$$

---

# 73. Entertainment Zone

可能：

- shared display；
- spatial audio；
- relaxed input；
- higher visual load。

但 passenger only。

---

# 74. Social Zone

Face-to-face seating：

$$
InteractionHuman-Human\uparrow.
$$

此時 AI 可以：

- lower intrusion；
- shared media。

---

# 75. Zone Arbitration

多人：

$$
Intent_1\neq Intent_2.
$$

需要 arbitration。

---

# 76. Arbitration Objective

定義：

$$
\boxed{
J_Z
=
\sum_i
w_iU_i
-
ConflictCost
}
$$

subject to：

$$
Safety,
Privacy,
Authority.
$$

---

# 77. Equal Weight 不一定合理

driver safety：

$$
w_{\text{safety}}
$$

不是普通 utility weight。

仍然是 hard gate。

---

# 78. Audio Conflict

一人聽 podcast。

另一人睡。

可：

- sound zone；
- headphones；
- masking；
- lower volume。

---

# 79. Visual Conflict

共享 display：

- work；
- movie；

不能同時滿足。

可：

- split；
- personal display；
- priority；
- defer。

---

# 80. Climate Conflict

一人冷、一人熱。

未來可：

- zoned HVAC；
- seat heating；
- airflow direction。

所以 SAZ 也可以延伸：

$$
\boxed{
Environmental Zone.
}
$$

---

# 81. Zone Stack

完整空間分區可以看成：

$$
\boxed{
Z
=
Z_{occupant}
\cap
Z_{attention}
\cap
Z_{visual}
\cap
Z_{audio}
\cap
Z_{privacy}
\cap
Z_{authority}
\cap
Z_{environment}.
}
$$

---

# 82. Layer Misalignment

如果：

audio zone 是私人，

但 display 是共享，

則：

$$
Privacy
$$

仍然不是 private。

所以需要：

$$
\boxed{
Cross-Layer Zone Validation.
}
$$

---

# 83. Weakest-Link Privacy

可以定義：

$$
\boxed{
P_{\text{effective}}
=
\min
(
P_{visual},
P_{audio},
P_{mic},
P_{storage},
P_{network}
).
}
$$

最弱的一層決定有效 privacy class。

---

# 84. Weakest-Link Safety

同理：

如果 visual 安全，

但 manual demand 太高，

仍：

$$
Unsafe.
$$

所以：

$$
\boxed{
Safety
=
\bigwedge_k
Safety_k.
}
$$

---

# 85. Driver HMI Clarity

Euro NCAP 2026 開始對：

- placement；
- clarity；
- ease of use；
- essential physical controls；

進行更明確 HMI 評估。

這支持：

$$
\boxed{
InteractionQuality
}
$$

本身屬安全問題。

---

# 86. Physical Controls 仍有角色

PMS 不代表：

> 全部都要 touch screen。

某些 safety / frequently used functions：

- physical button；
- knob；
- steering control；

仍可能更合適。

所以：

$$
\boxed{
Programmable
\neq
ScreenOnly.
}
$$

---

# 87. Voice 也不是零負荷

Voice：

$$
D^V\downarrow
$$

但：

$$
D^C
$$

仍可能高。

複雜會議：

$$
D^C
$$

很高。

所以：

$$
\boxed{
Voice
\neq
AlwaysSafe.
}
$$

---

# 88. Audio Can Distract

driver zone 中：

- audiobook；
- simple command；

與：

- emotional negotiation；
- complex reasoning call；

完全不同。

所以 audio task 也要 demand classification。

---

# 89. Cognitive Demand Classification

可以分：

- C0 passive；
- C1 simple；
- C2 moderate；
- C3 complex；
- C4 critical / unsuitable。

---

# 90. Visual Demand Classification

- V0 none；
- V1 glanceable；
- V2 periodic；
- V3 sustained；
- V4 immersive。

---

# 91. Manual Demand Classification

- M0 none；
- M1 single control；
- M2 short sequence；
- M3 sustained manipulation。

---

# 92. Interaction Demand Descriptor

例如：

```yaml
activity: "read_dense_contract"
demand:
  visual: "V3"
  auditory: "A0"
  manual: "M1"
  cognitive: "C3"
  response_reserve: "R2"
```

---

# 93. Zone Capability Descriptor

Driver：

```yaml
budget:
  visual_max: "V1"
  cognitive_max: "C1"
  manual_max: "M1"
```

則：

$$
read\_dense\_contract
$$

直接不 fit。

---

# 94. LLM 不應自己估 Safety Class

模型可以：

- suggest classification。

但：

$$
\boxed{
SafetyClass
}
$$

應由：

- OEM；
- verified classifier；
- policy；
- certified system；

共同決定。

不是 prompt 說：

> 我覺得這很安全。

---

# 95. Policy Version

Zone Contract 必須有：

$$
policy\_version.
$$

因為：

- regulation；
- OEM；
- software；

會更新。

---

# 96. Provenance

每個 allow / block：

應能回答：

> 為什麼？

例如：

```text
BLOCK:
driver_visual_budget
policy: oem_uxr_v14
vehicle_state: moving
```

---

# 97. Audit Without Surveillance

Safety decisions 可 audit。

但不等於長期保存：

- gaze video；
- cabin audio；

全部原始資料。

可以：

$$
\boxed{
StoreDecisionEvidence
\neq
StoreAllRawSensors.
}
$$

---

# 98. Local Processing Preference

occupant monitoring：

若可，

$$
\boxed{
LocalInference
}
$$

優先。

只輸出：

- fatigue flag；
- role；
- attention class。

不輸出 raw face video。

---

# 99. Personal AI Zone

每個 passenger 未來可以有：

$$
\boxed{
PersonalAIContext_i.
}
$$

但：

$$
Context_i
$$

不應被其他 passenger agent 讀取。

---

# 100. Multi-Agent Cabin

一台車可有：

- Driver Safety Agent；
- Cabin System Agent；
- Passenger Personal Agent；
- Entertainment Agent。

它們不應是：

$$
OneAgentWithEverything.
$$

---

# 101. Agent Authority Partition

例如：

$$
A_{driver-safety}
$$

可以：

- safety notification；
- minimal cabin override。

$$
A_{personal}
$$

可以：

- personal communication；
- personal AI。

不能控制 driving stack。

---

# 102. Agent-to-Agent Contract

例如 Personal Agent：

> 使用者想安靜休息。

發給 Cabin Agent：

$$
Intent=REST.
$$

Cabin Agent 再根據：

- seat；
- capability；
- safety；

配置環境。

---

# 103. No Raw Physical Control from Language

仍然：

$$
\boxed{
Intent
\rightarrow
BoundedContract
\rightarrow
CabinControl.
}
$$

不是：

$$
Prompt
\rightarrow
CANBus.
$$

---

# 104. B-04 Zone Runtime

輸入：

- occupant；
- vehicle state；
- motion；
- safety；
- activity；
- MRC；
- privacy；
- authority。

輸出：

$$
\boxed{
ZoneDecision.
}
$$

---

# 105. ZoneDecision

```yaml
decision: "TRANSFORM"
zone_id: "driver"
activity_id: "task_17"
allowed_modalities:
  - "audio"
forbidden_modalities:
  - "dense_visual"
  - "keyboard"
reason:
  - "driver_attention"
authority_epoch: 42
policy_version: "saz-0.1"
```

---

# 106. Zone Runtime Pipeline

$$
\boxed{
Sense
\rightarrow
Classify
\rightarrow
Budget
\rightarrow
Match
\rightarrow
Policy
\rightarrow
Allow/Transform/Defer/Block.
}
$$

---

# 107. Sense

只取得必要狀態。

---

# 108. Classify

角色 / motion / privacy。

---

# 109. Budget

生成：

$$
B_i.
$$

---

# 110. Match

比較：

$$
D_j
$$

與：

$$
B_i.
$$

---

# 111. Policy

再套：

- safety；
- privacy；
- authority；
- governance。

---

# 112. Output

不是只：

$$
Allow/Block.
$$

還有：

$$
Transform/Defer.
$$

---

# 113. Why Transform Matters

如果只有 block：

> 車上什麼都不能做。

PMS 沒意義。

如果只有 allow：

> 全部都做。

不安全。

真正需要：

$$
\boxed{
Adaptive Degradation.
}
$$

---

# 114. Mobility Continuity with Safety

因此：

$$
\boxed{
Continuity
=
\text{Preserve Activity Identity}
+
\text{Change Interaction Form When Necessary}.
}
$$

---

# 115. 可證偽命題 H1

SAZ-based resume 比 global vehicle UI：

$$
DriverUnsafeInteractionRate\downarrow.
$$

---

# 116. H2

Passenger zone 允許 richer UI：

$$
PassengerTaskCompletion\uparrow
$$

且 driver distraction 不顯著上升。

---

# 117. H3

Personal sound zones：

$$
AudioConflict\downarrow.
$$

---

# 118. H4

Audio zoning + privacy policy：

$$
PerceivedPrivacy\uparrow.
$$

但需測實際 leakage。

---

# 119. H5

Dynamic attention budget 比 fixed seat policy：

$$
SafetyUtility\uparrow.
$$

---

# 120. H6

Voice-only 不是所有 driver task 的安全 transform。

complex cognitive task：

$$
DriverPerformance\downarrow
$$

仍可能出現。

---

# 121. H7

Privacy-aware transform 可以降低 shared-ride information leakage。

---

# 122. H8

Multi-user / multi-display architecture 可降低 passenger UI conflict。

---

# 123. Evaluation Vector

定義：

$$
\boxed{
\mathcal V_{SAZ}
=
(
Safety,
Attention,
Privacy,
Utility,
Conflict,
Leakage,
Continuity,
Authority
).
}
$$

---

# 124. Metrics

## Driver Distraction Events

$$
N_D.
$$

## Unsafe Resumes

$$
N_U.
$$

## Privacy Leakage

$$
L_P.
$$

## Zone Conflict

$$
C_Z.
$$

## Transform Success

$$
S_T.
$$

## Passenger Utility

$$
U_P.
$$

---

# 125. 不做的主張

本文不主張：

1. occupant monitoring 應該永久錄影；
2. voice interaction 永遠安全；
3. rear-seat interaction 不需要 safety；
4. physical partition 是必要條件；
5. personal sound zone 可以保證零音訊外洩；
6. Android occupant zone 已等於本文 SAZ；
7. SAE automation level 可以直接映射到一套固定 UI policy；
8. Level 3 可以當作 full passenger mode；
9. Level 4 / 5 可以忽略 crash / emergency constraints；
10. passenger display 一定不會影響 driver；
11. AI 可以自己決定安全上限；
12. safety override 可以清空 privacy；
13. 多模態越多越好；
14. programmable cabin 等於 screen-centric cabin。

---

# 126. 與 B-03 的正式接口

B-03：

$$
MRC.
$$

B-04：

$$
ZoneContract.
$$

合成：

$$
\boxed{
ResumePlan
=
\Psi(
MRC,
ZoneContract
).
}
$$

---

# 127. 與 B-05 的正式接口

B-05 將把：

$$
ResumePlan
$$

映射成：

- display；
- projection；
- audio；
- microphone；
- seat；
- lighting；
- privacy；
- AI surface。

所以：

$$
\boxed{
B04
=
\text{Constraint / Permission Layer}.
}
$$

$$
\boxed{
B05
=
\text{Cabin Execution Layer}.
}
$$

---

# 128. 最重要的五條公式

第一：

$$
\boxed{
\text{Same Vehicle}
\neq
\text{Same Interaction Domain}.
}
$$

第二：

$$
\boxed{
Z_i(t)
=
(
R_i,
B_i,
S_i,
V_i,
H_i,
P_i,
U_i,
A_i,
N_i,
E_i
).
}
$$

第三：

$$
\boxed{
D_j
\preceq
B_i.
}
$$

第四：

$$
\boxed{
Decision
\in
\{
Allow,
Transform,
Defer,
Block
\}.
}
$$

第五：

$$
\boxed{
MRC
+
ZoneContract
\rightarrow
ResumePlan.
}
$$

---

# 129. 結論

一台未來汽車即使擁有：

- AI；
- 大螢幕；
- 高速網路；
- 自動駕駛；
- spatial audio；

如果仍把「全車」視為一個 interaction domain，就會立即遇到：

- driver distraction；
- passenger conflict；
- privacy leakage；
- audio conflict；
- authority confusion；
- shared-surface contamination。

真正成熟的 Programmable Mobility Space 必須承認：

$$
\boxed{
\text{Vehicle Interior}
}
$$

是一個多角色、多權限、多注意力、多媒體、多隱私的複合空間。

因此：

$$
\boxed{
\text{Spatial Attention Zones}
}
$$

不是「多裝幾個螢幕」。

它是：

> **把安全、注意力、顯示、聲學、隱私、權限與環境，按乘員與情境重新分區。**

這也解釋了為什麼未來前座與後座不應使用同一套產品假設。

駕駛者需要：

$$
\text{Safety-First Interaction}.
$$

乘客可以：

$$
\text{Rich Multimodal Interaction}.
$$

後座甚至可以接近：

$$
\text{Full Programmable Workspace / Leisure Space}.
$$

而共享 robotaxi 又必須加入：

$$
\text{Privacy / Teardown / Multi-Occupant Arbitration}.
$$

所以最終真正的規則不是：

> 車內允許某個 App。

而是：

$$
\boxed{
\text{At this moment, in this zone, for this occupant, under this driving state, which interaction forms are permitted?}
}
$$

這就是 SAZ 的核心問題。

B-05 將以此為基礎，把這些 Zone Contract 真正轉成 AI-native cabin runtime 與實際多模態車艙。

---

# 參考文獻與技術錨點

1. NHTSA. **Emerging Issues / Driver Distraction Countermeasures.**  
   NHTSA notes that in-vehicle navigation and entertainment may create distraction and references its Visual-Manual Driver Distraction Guidelines for in-vehicle electronic devices.  
   `https://www.nhtsa.gov/book/countermeasures-that-work/distracted-driving/emerging-issues`

2. Android Developers. **Car app quality.** Current 2026 driver-distraction quality requirements for Android Auto / Android Automotive OS.  
   `https://developer.android.com/docs/quality-guidelines/car-app-quality`

3. Android Developers. **Extend your media app to Android for Cars.** Updated 2026-08-14 UTC on checked page.  
   `https://developer.android.com/media/implement/surfaces/cars`

4. Android Open Source Project. **Multi-Display Communications API.**  
   Defines occupant zones that map users to sets of displays and communication across occupant zones.  
   `https://source.android.com/docs/automotive/displays/multi-display-comms-api`

5. Android Developers. **CarOccupantZoneManager.**  
   Includes driver, front passenger and rear passenger occupant types and display mappings.  
   `https://developer.android.com/reference/android/car/CarOccupantZoneManager`

6. Android Open Source Project. **Multi-user support / Android Automotive multi-user on multiple displays.** Updated 2026 documentation.  
   `https://source.android.com/docs/devices/admin/multi-user`

7. Android Open Source Project. **Android Automotive 15.**  
   Documents per-display UX restrictions and passenger-only display support while driving.  
   `https://source.android.com/docs/automotive/start/releases/aaos-24q3`

8. Euro NCAP. **2026 protocol changes / Safe Driving protocols.**  
   2026 assessment emphasizes driver monitoring, continuous eye/head tracking, real-time driver state and HMI clarity.  
   `https://www.euroncap.com/press-media/euro-ncap-announces-2026-protocol-changes-to-tackle-modern-driving-risks/`  
   `https://www.euroncap.com/safe-driving/`

9. SAE International. **J3016 Levels of Driving Automation.**  
   Used only as a driving-responsibility taxonomy anchor; B-04 does not equate SAE levels with SAZ classes.  
   `https://www.sae.org/binaries/content/assets/cm/content/blog/sae-j3016-visual-chart_5.3.21.pdf`

10. Xu, Q., Wang, S., Tao, J., Zou, H., & Qiu, X. (2025). **Creating personal sound zones in car cabins with active noise control.** Applied Acoustics, 235, 110670.  
    DOI: `10.1016/j.apacoust.2025.110670`

11. Li, H., Wu, J., & Pang, J. (2026). **Investigation of personal sound zones in vehicles using modified acoustic contrast control.** Applied Acoustics.  
    DOI: `10.1016/j.apacoust.2026.111374`

12. Borroni, A., et al. (2026). **Stochastic modeling of car cabin acoustics with application to personal sound zone systems.** Applied Acoustics, 251, 111346.  
    DOI: `10.1016/j.apacoust.2026.111346`

13. **Experimental Study on Enhancing Acoustic Contrast of Personal Sound Zones in a Car Using Headrest Loudspeakers.** Acoustics, 2026, 8(3), 52.  
    DOI: `10.3390/acoustics8030052`

---

# 內部依賴

1. `B01_Programmable_Mobility_Space_General_Theory_v0.1.md`
2. `B02_Travel_Time_Reclamation_v0.1.md`
3. `B03_Mobility_Cognitive_Continuity_v0.1.md`
4. `B03_Mobility_Resume_Capsule.schema.json`
5. Series A A-03 Multimodal-Native Communication
6. Series A A-04 AI Communication Runtime
7. Series A A-06 Personal Communication Sovereignty
8. Series A A-07 EVEMISS Communication Continuum Architecture

---

# 文件狀態

**Series：** B｜Programmable Mobility & Spatial Continuum  
**Number：** B-04  
**Version：** v0.1  
**Status：** Research Paper / Canonical Source  
**Series B progress：** 4/7  
**Overall 15-document progress：** 11/15  
