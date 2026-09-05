---
title: "Travel-Time Reclamation：交通時間回收、活動重配置與時間反彈效應"
subtitle: "Travel-Time Reclamation: Activity Reallocation, Temporal Rebound, and the Governance of Recovered Mobility Time"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Paper / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series B｜Programmable Mobility & Spatial Continuum"
series_number: "B-02"
canonical_source: true
encoding: "UTF-8"
---

# Travel-Time Reclamation：交通時間回收、活動重配置與時間反彈效應

## Travel-Time Reclamation: Activity Reallocation, Temporal Rebound, and the Governance of Recovered Mobility Time

**系列：** Series B｜Programmable Mobility & Spatial Continuum  
**編號：** B-02  
**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Paper / Canonical Source  

---

# 摘要

B-01 已提出 Programmable Mobility Space（PMS）的總論：交通工具可以逐步從單純位移機器轉化為可程式移動空間，旅程中的工作、休息、娛樂、社交、睡眠、創作與 idle 都可成為合法 activity state。本篇進一步研究其中最核心的時間經濟問題：

> **當交通技術、網路、車艙空間、自動駕駛與 AI 降低「必須專心處理交通本身」的時間後，被釋放出來的時間究竟是什麼？它如何被重新分配？又為什麼效率提升可能反而帶來更多工作、更多旅行或新的時間壓力？**

本文將這一過程稱為：

# **Travel-Time Reclamation**
## **交通時間回收**

但「回收」並不是創造新的一小時。對一天固定的時間預算而言，技術改變的是一段既有旅程時間的**活動可行集合**與**注意力配置**。因此：

$$
\boxed{
\text{Reclaimed Time}
\neq
\text{New Clock Time}.
}
$$

更準確地說，若原本的旅程時間為：

$$
T_{\text{travel}},
$$

則可以分成：

$$
\boxed{
T_{\text{travel}}
=
T_F
+
T_S
+
T_W
+
T_R
}
$$

其中：

- $T_F$：forced / unusable time，因駕駛、等待、介面限制、網路斷裂、動暈等而難以自由配置；
- $T_S$：self-directed activity time，由使用者自主分配至休息、娛樂、社交、創作等；
- $T_W$：work / production time；
- $T_R$：reserve / idle time，不必被任何活動填滿。

技術進步真正直接作用的是：

$$
\boxed{
T_F\downarrow.
}
$$

但：

$$
\Delta T_F<0
$$

並不能推出：

$$
\Delta T_W>0.
$$

它也可能變成：

$$
\Delta T_S>0
$$

或：

$$
\Delta T_R>0.
$$

因此本文將「時間可回收」與「時間由誰配置」視為兩個不同問題。

本文第二個核心命題是 **Temporal Rebound Effect（時間反彈效應）**。當旅程時間的負效用下降、工作可行性提高或交通成本在主觀上降低時，人與組織可能改變行為：增加工作、增加旅行距離、接受更長通勤、提高活動密度、延長可回應時間，甚至重新擴張原本被技術節省的時間成本。2025 年的 travel-time-use 系統性研究已強調 travel time use 對 time-use、mode choice、value of travel time savings、travel experience 與 second-order effects 的影響；2026 年針對 autonomous vehicle labour time 的經濟模型更顯示，在更高 AV penetration 與 travel labour 下，福利可先提高，但 congestion second-order effects 會使其邊際改善下降，部分產出與 value-of-time 結果甚至先升後降。

本文第三個核心命題是 **Temporal Capture（時間捕獲）**。若交通中的可用注意力被制度、組織或工作文化默認為「應該工作」，則時間回收可能從選擇權轉化為新的義務。2026 年對 hybrid work / digital connectivity 的研究把 work intensification 與 work extensification 描述為相互強化的時空機制；另一項 2026 年 occupational-health 理論工作則直接把 perpetual connectivity 重新理解為可能的 attentional labour extraction。這些研究不是車載工作研究本身，但為「技術釋放出的可連線時空可能被工作重新占用」提供重要制度錨點。

因此本文提出一條系列治理不變量：

$$
\boxed{
\text{Recovered Capability}
\not\Rightarrow
\text{Recovered Time Belongs to Employer}.
}
$$

並把成熟 PMS 的目標從：

$$
\max T_W
$$

改為：

$$
\boxed{
\max U_{\text{user}}
}
$$

subject to：

$$
Safety,\ Privacy,\ Consent,\ LabourRules,\ Health,\ Cost.
$$

本文最終將交通時間回收拆成五個階段：**Release、Allocation、Utilization、Rebound、Governance**。Series B 後續的 Cognitive Continuity、Spatial Attention Zones、Vehicle Cabin 與 Mobility Hospitality，都將建立在這個時間模型上。

---

# Abstract

Programmable Mobility Space changes not only the physical cabin but also the economic and experiential meaning of travel time. This paper defines Travel-Time Reclamation as the reduction of forced or unusable travel time through improvements in automation, connectivity, interfaces, cabin design, and continuity. Reclamation does not create new clock time; it expands the feasible set of activities that can be performed during an already-existing journey.

The paper decomposes travel time into forced/unusable time, self-directed activity time, work/production time, and reserve/idle time. Technology primarily reduces the forced component. Whether the recovered capacity becomes labour, leisure, rest, social interaction, or deliberately unused time is a separate allocation question.

A Temporal Rebound Effect is introduced to describe second-order responses in which reduced travel disutility or increased in-vehicle productivity leads to longer travel, greater travel demand, higher activity density, extended availability, or new work expectations. This framework is linked to 2025 travel-time-use synthesis, 2026 autonomous-vehicle labour-time modelling, and recent research on digital work intensification and extensification.

The paper further defines Temporal Capture: the institutional appropriation of technically recovered time, especially when constant connectivity converts discretionary mobility time into expected labour or availability. It therefore proposes that recovered mobility time should be governed as a user-allocatable resource rather than automatically classified as work time. The design objective of a mature mobility continuum is not maximum productivity but maximum user utility subject to safety, privacy, consent, labour, health, and economic constraints.

---

# 0. 為什麼需要「時間回收」而不是「交通生產力」

最直覺的說法是：

> 自動駕駛讓人可以在車上工作。

但這太窄。

因為同樣的 freed attention 可以拿來：

- 睡；
- 看電影；
- 打遊戲；
- 閱讀；
- 寫作；
- 聊天；
- 處理家務；
- 社交；
- 做白日夢；
- 什麼都不做。

所以真正母概念不是：

$$
\boxed{
\text{Travel Productivity}.
}
$$

而是：

$$
\boxed{
\text{Travel-Time Reclamation}.
}
$$

---

# 1. Reclamation 不等於 Creation

一天仍然只有：

$$
24\text{ hours}.
$$

一小時旅程不會因為 AI 或自動駕駛變成：

$$
2\text{ clock hours}.
$$

改變的是：

$$
\boxed{
\text{Feasible Activity Set During Travel}.
}
$$

定義：

$$
\mathcal A_{\text{travel}}(t)
$$

表示旅程時間 $t$ 可合法、可安全、可實際執行的活動集合。

技術進步可以使：

$$
\boxed{
|\mathcal A_{\text{travel}}|
\uparrow.
}
$$

但：

$$
T_{\text{clock}}
$$

不變。

---

# 2. Travel Time Use 是母集合

2025 年 Transport Reviews 的知識整理明確區分：

- travel time use；
- travel-based multitasking。

本文採：

$$
\boxed{
\text{Travel Time Use}
\supset
\text{Travel-Based Multitasking}.
}
$$

因為睡覺、單純聽音樂、看風景或安靜休息，都可能是 travel time use，但不需要是高負荷 multitasking。

這個區分對 PMS 非常重要。

---

# 3. 交通時間四分模型

本文定義：

$$
\boxed{
T_{\text{travel}}
=
T_F
+
T_S
+
T_W
+
T_R.
}
$$

## $T_F$ — Forced / Unusable

例如：

- 必須駕駛；
- 排隊；
- 高動暈；
- 斷網；
- 無法閱讀；
- 空間過擠；
- 高噪音；
- 注意力被交通安全完全占用。

## $T_S$ — Self-Directed Activity

例如：

- leisure；
- entertainment；
- social；
- creative；
- personal admin；
- reading；
- rest。

## $T_W$ — Work / Production

例如：

- call；
- review；
- coding；
- analysis；
- email；
- planning；
- meeting。

## $T_R$ — Reserve / Idle

例如：

- 發呆；
- 放空；
- 無任務；
- 不連線；
- 不被打擾。

---

# 4. 技術直接降低的是 $T_F$

如果：

$$
Automation\uparrow,
$$

$$
Connectivity\uparrow,
$$

$$
CabinQuality\uparrow,
$$

則某些活動限制下降。

所以第一階：

$$
\boxed{
T_F
\downarrow.
}
$$

但釋出的：

$$
\Delta T_{\text{released}}
=
-\Delta T_F
$$

並沒有天然用途。

---

# 5. Allocation 才決定結果

定義配置向量：

$$
\boxed{
\boldsymbol{\alpha}
=
(
\alpha_S,
\alpha_W,
\alpha_R
)
}
$$

且：

$$
\alpha_S+\alpha_W+\alpha_R=1.
$$

則：

$$
\Delta T_S
=
\alpha_S\Delta T_{\text{released}},
$$

$$
\Delta T_W
=
\alpha_W\Delta T_{\text{released}},
$$

$$
\Delta T_R
=
\alpha_R\Delta T_{\text{released}}.
$$

所以同一套技術可以導致完全不同的社會結果。

---

# 6. 同一台 robotaxi，三種文明結果

如果：

$$
\boldsymbol{\alpha}
=
(0.8,0.1,0.1),
$$

它主要增加 leisure。

如果：

$$
\boldsymbol{\alpha}
=
(0.1,0.8,0.1),
$$

它主要增加 work。

如果：

$$
\boldsymbol{\alpha}
=
(0.1,0.1,0.8),
$$

它主要增加 idle / recovery。

因此：

$$
\boxed{
\text{Technology}
\not\Rightarrow
\text{One Social Outcome}.
}
$$

---

# 7. Allocation Right

本文提出：

# **Temporal Allocation Right**

即：

> 技術釋放出的 travel-time capability，預設應由使用者依合法契約、勞動關係、安全與其他權利自行配置。

可以寫：

$$
\boxed{
Owner_{\text{default}}
(
\Delta T_{\text{released}}
)
=
User.
}
$$

這是規範性架構原則，不是對所有司法管轄區現行勞動法的敘述。

---

# 8. Capability 不等於 Obligation

Series B 的重要不變量：

$$
\boxed{
CanWork
\neq
MustWork.
}
$$

同理：

$$
\boxed{
CanConnect
\neq
MustRespond.
}
$$

$$
\boxed{
CanBeProductive
\neq
ProductivityDuty.
}
$$

這條線非常重要。

---

# 9. Why Work Is Attractive

工作之所以容易捕獲 reclaimed time，是因為：

$$
V_{\text{work}}
$$

對組織可量化：

- output；
- response time；
- revenue；
- coordination；
- billable hours。

而：

$$
V_{\text{idle}}
$$

往往難被組織帳本直接計算。

因此會產生結構性偏差：

$$
\boxed{
MeasuredValue
>
UnmeasuredRecoveryValue.
}
$$

這不代表 idle 沒有價值。

---

# 10. Temporal Capture

本文定義：

# **Temporal Capture**

當：

$$
\Delta T_{\text{released}}
$$

不是主要由使用者自主配置，而是被制度、雇主、平台、群體規範或 always-on culture 轉化成新的 availability / labour expectation，則：

$$
\boxed{
T_{\text{capture}}
>0.
}
$$

---

# 11. Capture Ratio

定義：

$$
\boxed{
\rho_C
=
\frac{T_{\text{externally imposed}}}
{T_{\text{released}}}.
}
$$

其中：

$$
0\le\rho_C\le1.
$$

如果：

$$
\rho_C=0,
$$

表示 released time 完全由使用者決定。

如果：

$$
\rho_C\rightarrow1,
$$

則時間回收幾乎全部變成外部義務。

---

# 12. 自願工作不等於 Capture

如果一個創業者自己決定：

> 這兩小時車程我要繼續研究。

這是：

$$
T_W
$$

但不必然是：

$$
T_{\text{capture}}.
$$

所以：

$$
\boxed{
Work
\neq
Capture.
}
$$

Capture 的核心是：

$$
\boxed{
\text{Loss of Allocation Autonomy}.
}
$$

---

# 13. Work Intensification

2026 年 Work, Employment and Society 的研究把 digital connectivity 下的 intensification 描述為：

> 在既定時間內提高 effort / task density。

可表示：

$$
\boxed{
D_W
=
\frac{\text{Work Demand}}
{\text{Time}}.
}
$$

若：

$$
D_W\uparrow,
$$

則工作密度上升。

這與「工作時間變長」是兩件不同的事。

---

# 14. Work Extensification

同一研究把 extensification 描述為 work 在時間與空間上的擴散。

可寫：

$$
\boxed{
\Omega_W
=
\text{Reach of Work Across Time and Space}.
}
$$

如果工作從辦公室擴張到：

- 家；
- 晚上；
- 週末；
- 火車；
- 汽車；
- 飛機；

則：

$$
\Omega_W\uparrow.
$$

---

# 15. Intensification × Extensification

兩者可能形成：

$$
\boxed{
D_W\uparrow
\quad\land\quad
\Omega_W\uparrow.
}
$$

也就是：

> 不只每小時做更多，連「什麼地方算工作場所、什麼時間算工作時間」都一起擴張。

PMS 如果沒有治理，非常容易加入這個機制。

---

# 16. Perpetual Connectivity

2026 年 Frontiers in Public Health 的概念研究進一步把 perpetual connectivity 視為可能的 digital labour exposure。

本文不直接採用其所有規範結論，但取其重要區分：

$$
\boxed{
\text{Being Connected}
\neq
\text{Being Free}.
}
$$

因為即使沒有實際執行 task：

$$
\text{AvailabilityExpectation}
$$

本身也可能占用 attention。

---

# 17. Availability Load

定義：

$$
\boxed{
L_A
=
f(
ExpectedResponse,
InterruptProbability,
Monitoring,
SocialNorm
).
}
$$

即使：

$$
T_W=0,
$$

如果：

$$
L_A>0,
$$

使用者也不一定真正處於休息。

因此：

$$
\boxed{
\text{No Active Task}
\neq
\text{No Work Load}.
}
$$

---

# 18. Reserve Time 的價值

 $T_R$ 不是「沒有被最佳化的浪費」。

它可以提供：

- cognitive recovery；
- spontaneous thought；
- emotional transition；
- boredom；
- reflection；
- decompression。

本文不需要證明每一分鐘 idle 都有高價值。

只需要拒絕：

$$
\boxed{
T_R=0
}
$$

作為效率最大化的默認目標。

---

# 19. Minimum Reserve Policy

PMS 可以允許：

```text
REST
IDLE
OFFLINE
DO_NOT_DISTURB
```

成為 first-class runtime states。

Series A 的 Agent Commons / Workspace 早已把 rest / offline / refuse / wait 視為正式狀態；Series B 將同一原則延伸到 human mobility time。

---

# 20. Temporal Rebound Effect

本文定義：

$$
\boxed{
\mathcal R_T
=
\text{Second-order increase in time demand caused by lower effective travel-time cost}.
}
$$

例子：

- 願意住更遠；
- 願意搭更慢但舒適的交通；
- 增加旅行；
- 增加工作；
- 增加 meeting；
- 增加即時回應；
- 增加 activity fragmentation。

---

# 21. Rebound 不是只有工作

Temporal rebound 可以流向：

$$
Work,
Travel,
Leisure,
Consumption,
Social.
$$

例如：

> 車上能看電影，所以我願意搭更久的車。

這也是 rebound。

因此：

$$
\boxed{
TemporalRebound
\supset
LabourRebound.
}
$$

---

# 22. Labour Rebound

其中：

$$
\boxed{
\mathcal R_L
\subset
\mathcal R_T.
}
$$

表示：

> 可工作 travel time 增加後，工作需求或工作供給反過來增加。

2026 年 AV labour-time 模型正是在研究這條線。

---

# 23. AV Labour-Time Model 的意義

該研究把：

- consumption；
- leisure；
- labour；
- travel utility；
- labour while travelling；

放進微觀經濟模型，再接 CGE 與 transport model。

最重要的不是某一個 Sydney 數值。

而是：

$$
\boxed{
\text{Travel-Time Productivity}
}
$$

已經足以影響：

$$
\text{Labour Supply}
+
\text{Household Budget}
+
\text{Congestion}
+
\text{Welfare}.
$$

---

# 24. 二階壅塞效應

如果 AV 讓 travel time 感覺「沒那麼貴」，可能：

$$
TravelDemand\uparrow.
$$

進而：

$$
Congestion\uparrow.
$$

所以：

$$
\boxed{
\text{Lower Individual Time Cost}
\not\Rightarrow
\text{Lower System Time Cost}.
}
$$

這是一個典型反彈。

---

# 25. Individual Utility vs System Utility

個人：

$$
U_i\uparrow.
$$

但系統：

$$
\sum_j T_j
$$

可能增加。

因此政策層需要：

$$
\boxed{
\text{Private Benefit}
\neq
\text{Social Benefit}.
}
$$

---

# 26. Longer Commute Acceptance

若：

$$
U_{\text{journey}}\uparrow,
$$

人可能接受：

$$
T_{\text{travel}}\uparrow.
$$

這可能影響：

- housing；
- urban form；
- office location；
- labour market catchment；
- road demand。

這就是 travel-time-use 的 second-order effect。

---

# 27. Distance Rebound

定義：

$$
\boxed{
\mathcal R_D
=
\frac{\Delta D_{\text{travel}}}
{-\Delta C_{\text{effective travel}}}.
}
$$

不是說一定為正。

而是提供一個研究量：

> 有效 travel cost 每下降一單位，平均距離是否增加？

---

# 28. Activity Density Rebound

如果：

$$
T_F\downarrow,
$$

可能出現：

$$
N_{\text{activities per day}}
\uparrow.
$$

於是：

$$
\boxed{
D_A
=
\frac{N_A}{T_{\text{day}}}
}
$$

增加。

這可能令人覺得：

> 我做更多事了。

也可能導致：

- fragmentation；
- switching cost；
- fatigue。

---

# 29. 2025 Time-Use Patterns Review

2025 Journal of Transport Geography 的 systematic review 指出：

- multitasking；
- flexibility；
- activity fragmentation；

可能中介 digital engagement、telework、AV 對 travel behaviour 的影響。

這支持：

$$
\boxed{
\text{Technology}
\rightarrow
\text{Time-Use Pattern}
\rightarrow
\text{Travel Behaviour}.
}
$$

而不是：

$$
\text{Technology}
\rightarrow
\text{One Direct Outcome}.
$$

---

# 30. Fragmentation

定義：

$$
\boxed{
F_A
=
\text{Number / frequency of activity splits and transitions}.
}
$$

PMS 可以降低某些 transition cost。

但也可能讓人：

- 一路切 task；
- 回 message；
- 開 meeting；
- 看文件；
- 再切娛樂。

所以：

$$
\boxed{
Continuity
\not\Rightarrow
\text{No Fragmentation}.
}
$$

---

# 31. Continuity 可以降低切換成本，也能增加切換次數

這是很有趣的雙面性。

如果：

$$
Cost_{\text{switch}}\downarrow,
$$

可能：

$$
SwitchCount\uparrow.
$$

因此總 switching burden：

$$
B_S
=
Cost_{\text{switch}}
\times
SwitchCount
$$

不一定下降。

這是另一種 rebound。

---

# 32. Travel Productivity Index

定義一個研究量：

$$
\boxed{
P_T
=
\frac{UsefulOutputDuringTravel}
{T_{\text{travel}}}.
}
$$

但 $P_T$ 只適用工作 activity。

不能拿來評估：

- sleep；
- leisure；
- recovery。

所以 PMS 不能只看 $P_T$。

---

# 33. Journey Utility Index

更完整：

$$
\boxed{
J_U
=
w_W U_W
+
w_S U_S
+
w_R U_R
+
w_C U_C
-
w_F C_F
}
$$

其中權重由使用者／研究情境決定。

---

# 34. Reclamation Efficiency

可定義：

$$
\boxed{
\eta_R
=
1-
\frac{T_F^{after}}
{T_F^{before}}.
}
$$

如果：

$$
\eta_R=0,
$$

沒有回收 forced time。

若：

$$
\eta_R\rightarrow1,
$$

表示大量 forced/unusable time 被解除。

注意：

$$
\eta_R
$$

不是 productivity score。

---

# 35. Autonomy Score

定義：

$$
\boxed{
A_T
=
1-\rho_C.
}
$$

其中 $\rho_C$ 是 capture ratio。

所以一個系統可以：

$$
\eta_R\uparrow
$$

但：

$$
A_T\downarrow.
$$

也就是：

> 技術非常有效，人的時間自主性反而下降。

---

# 36. 這就是真正的效率悖論

若只看：

$$
\eta_R,
$$

我們會說系統進步。

若加入：

$$
A_T,
$$

結果可能不同。

因此成熟評估至少是：

$$
\boxed{
Score
=
f(
Reclamation,
Utility,
Autonomy,
Health,
Safety
).
}
$$

---

# 37. Temporal Sovereignty

本文提出：

# **Temporal Sovereignty**

它不是法律上絕對所有權。

而是一個設計／治理概念：

> 使用者對被技術釋放出的活動可能性，應保有可理解、可設定、可拒絕、可中斷與可重新分配的控制權。

可表示：

$$
\boxed{
\mathcal T_S
=
(
Choose,
Refuse,
Pause,
Disconnect,
Reallocate,
Audit
).
}
$$

---

# 38. 與 Personal Communication Sovereignty 的關係

A-06 問：

> communication state 誰控制？

B-02 問：

> mobility time 的活動配置誰控制？

所以：

$$
\boxed{
\text{Data / Communication Sovereignty}
+
\text{Temporal Sovereignty}
}
$$

是未來 Continuum governance 的兩個不同維度。

---

# 39. Employer Policy Boundary

企業版本的 vehicle work mode 必須能區分：

- employee voluntary use；
- required work；
- paid work；
- on-call；
- commuting；
- business travel；
- break / rest。

本文不替不同司法區直接判定勞動法結果。

但架構必須保留：

$$
\boxed{
\text{Activity Classification Metadata}.
}
$$

否則未來無法治理。

---

# 40. Activity Classification

例如：

```yaml
activity_class: "WORK"
initiator: "USER"
required_by_employer: false
compensation_scope: "none"
interruptibility: "user_controlled"
```

或：

```yaml
activity_class: "WORK"
initiator: "EMPLOYER"
required_by_employer: true
compensation_scope: "contractual"
```

技術上兩者都叫「在車上寄 Email」。

制度上完全不同。

---

# 41. Work Mode 不應偷偷啟用

PMS 進入 Work Mode 應該是：

$$
\boxed{
Explicit
\lor
ClearlyDelegated.
}
$$

而不是：

> 系統看到你有空就自動推公司工作。

這是重要 anti-capture rule。

---

# 42. Rest Mode 必須是 Hard Mode

Rest 不能只是 UI theme。

若：

$$
Mode=REST,
$$

則：

- work notifications deny；
- employer agent blocked except allowed emergency；
- work context hidden；
- work tools unavailable or deferred；
- private entertainment / rest allowed。

這與 Series A 的 mode isolation 相容。

---

# 43. Idle Mode 必須存在

甚至：

$$
Mode=IDLE
$$

也是合法。

含義：

> 不要幫我最佳化。

這是一個非常重要的產品功能。

---

# 44. Notification Budget

定義：

$$
\boxed{
B_N(t)
=
\text{Allowed Notification Load}.
}
$$

在 Rest / Idle：

$$
B_N\downarrow.
$$

在 Work：

$$
B_N\uparrow
$$

但仍受 attention / safety 限制。

---

# 45. Mobility DND

未來 PMS 應有：

```text
DND_WORK
DND_ALL
EMERGENCY_ONLY
PRIVATE_MODE
OFFLINE_MODE
```

而不是只有：

> mute audio。

---

# 46. Temporal Contract

一次 ride 可以帶：

```yaml
time_policy:
  mode: "REST"
  work_interruptions: "deny"
  emergency_contacts: "allow"
  personal_messages: "summary_only"
  auto_resume_task_on_arrival: true
```

這把 temporal sovereignty 變成 machine-readable contract。

---

# 47. Arrival 不應自動延長捕獲

如果使用者在車上 Work Mode：

$$
RideEnd
$$

不應默認：

$$
WorkMode\rightarrow Home.
$$

Arrival Transition 應重新確認：

$$
\boxed{
ModeAfterArrival.
}
$$

---

# 48. 交通時間的心理邊界

通勤 historically 也可能具有 transition function：

$$
Work
\rightarrow
Commute
\rightarrow
Home.
$$

若 PMS 把 commute 完全填滿：

$$
Work
\rightarrow
Work
\rightarrow
Home,
$$

就可能失去心理轉換空間。

所以：

$$
\boxed{
TransitionUtility
}
$$

也應納入模型。

---

# 49. Transition Utility

定義：

$$
\boxed{
U_X
=
\text{Utility of psychological / role transition during travel}.
}
$$

它可能來自：

- silence；
- music；
- walking；
- scenery；
- decompression。

效率系統不應假設：

$$
U_X=0.
$$

---

# 50. Reclamation 可以故意保留 Transition

例如：

```text
First 20 min: Work
Last 15 min: Decompression
```

這是一種：

$$
\boxed{
\text{Temporal Zoning}.
}
$$

未來甚至可與 B-04 Spatial Zoning 接合。

---

# 51. Temporal Zoning

定義 ride：

$$
[0,T]
$$

切成：

$$
\boxed{
Z_T
=
\{z_1,z_2,\ldots,z_n\}.
}
$$

每個 zone 有：

- activity；
- interruption policy；
- modality；
- environment；
- privacy；
- attention。

例如：

$$
z_1=Work,
$$

$$
z_2=Rest.
$$

---

# 52. Dynamic Temporal Zoning

不一定固定時間。

可以依：

- ETA；
- motion；
- fatigue；
- meeting；
- arrival；
- network；
- user state；

動態切換。

例如：

> 距離目的地 10 分鐘，自動停止深度工作並整理摘要。

---

# 53. Handoff to Arrival

Continuity Runtime 可以：

$$
WorkInVehicle
\rightarrow
Checkpoint
\rightarrow
ArrivalSummary
\rightarrow
DesktopResume.
$$

因此最後 10 分鐘不需要繼續「硬做」。

AI 可以幫忙收尾。

---

# 54. AI 可以降低 Transition Cost，而不是提高 Work Density

這是一個非常重要的 alternative design。

AI 可以用 freed time 來：

- summarize；
- organize；
- queue；
- defer；
- prepare next context。

而不是：

- 塞更多任務。

所以：

$$
\boxed{
AIValue
\supset
\text{Work Intensification}.
}
$$

---

# 55. Deferred Execution

例如使用者開車。

AI 收到複雜工作：

$$
Task.
$$

不是要求人立刻處理。

而是：

$$
\boxed{
AIExecuteSafeParts
\rightarrow
QueueHumanReview
\rightarrow
ResumeLater.
}
$$

這也是時間回收。

---

# 56. Travel Time Reclamation Without Human Attention

更進一步：

$$
T_{\text{travel}}
$$

可以被 AI 用來執行：

- background search；
- compilation；
- rendering；
- indexing；
- draft；
- simulation。

人不用一直 attention-on。

所以：

$$
\boxed{
\text{Recovered Compute Time}
\neq
\text{Recovered Human Labour Time}.
}
$$

這是 AI 時代非常重要的新區分。

---

# 57. Human vs Agent Reclamation

定義：

$$
T_R^{H}
$$

與：

$$
T_R^{A}.
$$

其中：

- $T_R^{H}$：人可以自主利用的 travel time；
- $T_R^{A}$：Agent 可在旅途中持續利用的 runtime window。

理想系統可以：

$$
T_R^{A}\uparrow
$$

而不要求：

$$
T_W^{H}\uparrow.
$$

---

# 58. 這是避免「工作狂架構」的關鍵

真正成熟的 AI-native mobility 可以是：

> 人休息，Agent 工作。

而不是：

> AI 讓人可以一直工作。

所以：

$$
\boxed{
\text{Automation}
\rightarrow
\text{Human Attention Decoupling}.
}
$$

這其實比傳統 productivity 更有價值。

---

# 59. Agent Handoff During Travel

例如：

```text
Human starts task
→ enters vehicle
→ agent continues research
→ human rests
→ agent creates review packet
→ arrival
→ human reviews
```

工作 continuity 存在。

但：

$$
HumanWorkContinuity
$$

不等於：

$$
HumanContinuousAttention.
$$

---

# 60. Attention Reclamation

真正可以定義：

$$
\boxed{
A_R
=
A_{\text{transport before}}
-
A_{\text{transport after}}.
}
$$

也就是：

> 交通本身需要的人類 attention 下降多少？

這與 clock time 不同。

---

# 61. Attention Is the Scarce Resource

某些情況：

$$
T_{\text{travel}}
$$

沒變。

但：

$$
A_{\text{transport}}
\downarrow.
$$

所以真正被回收的是：

$$
\boxed{
\text{Attention Capacity}.
}
$$

這更接近我們最初從駕駛想到的問題。

---

# 62. Attention Allocation Vector

定義：

$$
\boldsymbol{\beta}
=
(
\beta_{\text{safety}},
\beta_{\text{work}},
\beta_{\text{leisure}},
\beta_{\text{rest}},
\beta_{\text{social}}
).
$$

不同 automation state 對：

$$
\beta_{\text{safety}}
$$

有不同硬下限。

B-04 會專門處理。

---

# 63. Self-Driving 的真正時間效應

不是：

$$
TimeCreated.
$$

而是：

$$
\boxed{
\text{Attention Constraint Relaxation}.
}
$$

所以：

$$
\mathcal A_{\text{feasible}}
\uparrow.
$$

---

# 64. Chauffeur 是歷史上的 Attention Outsourcing

有司機時：

$$
A_{\text{driving}}^{passenger}
\approx0.
$$

因此總裁、乘客早就可以在車上：

- work；
- read；
- call；
- rest。

再次證明：

> self-driving 不是第一個 reclaim travel attention 的方法。

---

# 65. Public Transport 也一直在做時間回收

火車的優勢之一就是：

$$
A_{\text{driving}}=0.
$$

因此：

- reading；
- laptop；
- sleep；
- phone；

更早就成立。

所以 B-02 是跨交通模式理論。

---

# 66. Mode Choice 會被 Activity Support 改變

如果兩個 mode：

$$
M_1,M_2
$$

travel time 不同，但 activity support 不同：

$$
Q_A(M_1)\neq Q_A(M_2),
$$

則：

$$
\boxed{
ModeChoice
\neq
f(Time,Price)\text{ only}.
}
$$

2025 travel-time-use review 正是把 mode choice 視為受影響維度之一。

---

# 67. Value of Travel Time Savings 也會改變

如果人在旅途中可以做高價值活動：

$$
Disutility(T_{\text{travel}})
\downarrow.
$$

因此：

$$
VOTTS
$$

可能改變。

但不是所有 activity 都會改善旅程。

2026 SAV field experiment 顯示：

- work-related NDRTs 可改善部分 SAV travel-time perception；
- full NDRT engagement 反而可讓某些 car travel perception 更負面。

所以：

$$
\boxed{
MoreActivity
\neq
LessDisutility.
}
$$

---

# 68. Quality Matters

同樣「可以工作」：

$$
Workability
$$

還取決於：

- seat；
- screen；
- motion；
- noise；
- network；
- privacy；
- interruption。

所以：

$$
\boxed{
ActivityAvailability
\neq
ActivityQuality.
}
$$

---

# 69. Productivity ≠ Comfort

一個空間可能：

$$
P_{\text{work}}\uparrow
$$

但：

$$
U_{\text{journey}}\downarrow.
$$

例如太擠、太暈、太吵。

因此不能只用 output 評估。

---

# 70. The Full Reclamation Function

本文提出：

$$
\boxed{
R_T
=
f(
Automation,
Connectivity,
Cabin,
Interface,
Continuity,
Motion,
Privacy,
Attention
).
}
$$

而使用後效用：

$$
\boxed{
U_T
=
g(
R_T,
Allocation,
Autonomy,
Health,
Safety,
SocialContext
).
}
$$

---

# 71. Rebound Function

反彈：

$$
\boxed{
B_T
=
h(
R_T,
WorkNorm,
TravelDemand,
UrbanForm,
Price,
Availability,
PersonalPreference
).
}
$$

因此：

$$
R_T\uparrow
$$

不必然讓：

$$
T_{\text{total travel}}\downarrow.
$$

---

# 72. Net Temporal Benefit

可定義：

$$
\boxed{
NTB
=
U_{\text{reclaimed}}
-
C_{\text{capture}}
-
C_{\text{rebound}}
-
C_{\text{fatigue}}
-
C_{\text{fragmentation}}.
}
$$

這比：

$$
MinutesSaved
$$

更接近 PMS 的總體價值。

---

# 73. Policy / Product 要避免錯誤 KPI

如果 KPI 只有：

- minutes productive；
- messages sent；
- meetings completed；

系統會自然推：

$$
T_W\uparrow.
$$

如果 KPI 加入：

- user-chosen allocation；
- rest adherence；
- interruption rate；
- fatigue；
- journey satisfaction；
- privacy；
- DND compliance；

才比較接近：

$$
\max U_{\text{user}}.
$$

---

# 74. Temporal Reclamation KPI

建議：

## Reclamation

$$
\eta_R.
$$

## Autonomy

$$
A_T.
$$

## Capture

$$
\rho_C.
$$

## Journey Utility

$$
J_U.
$$

## Fragmentation

$$
F_A.
$$

## Attention Load

$$
L_A.
$$

## Work Density

$$
D_W.
$$

---

# 75. 一個成熟 PMS 可以效率很高但不「一直工作」

例如：

- Agent background task；
- 人看電影；
- arrival 前 AI 產生摘要；
- 到辦公室再 review。

那麼：

$$
SystemProductivity\uparrow
$$

同時：

$$
HumanWorkTime
\not\uparrow.
$$

這是值得追求的型態。

---

# 76. 甚至可以 Human Work Time 下降

如果 AI 在 travel time 執行更多低價值工作：

$$
T_W^H\downarrow.
$$

所以 technology 有可能：

$$
\boxed{
\text{Improve Output}
+
\text{Reduce Human Work}.
}
$$

是否發生取決於 allocation / governance。

---

# 77. Reclamation Modes

PMS 可以提供：

```text
WORK
REST
ENTERTAINMENT
SOCIAL
CREATIVE
IDLE
AGENT_ONLY
```

其中 `AGENT_ONLY` 很有意思：

> 人不處理工作，但 agent 可以在背景完成已授權任務。

---

# 78. AGENT_ONLY Mode

定義：

$$
Mode=AGENT\_ONLY.
$$

人類：

$$
Attention_{work}=0.
$$

Agent：

$$
TaskExecution>0.
$$

但：

- 不得執行未授權外部副作用；
- 必須遵守 authority；
- arrival 時提供 review packet。

---

# 79. Work Capture 防護

可以設：

```yaml
mobility_time_policy:
  default_mode: "REST"
  allow_employer_interrupt: false
  allow_agent_background_work: true
  require_user_activation_for_work_mode: true
```

這不是「反工作」。

是把工作變成 explicit state。

---

# 80. 個人也可能自我捕獲

Capture 不只來自雇主。

有些人自己會：

> 每一分鐘都塞工作。

因此：

$$
\boxed{
SelfCapture
}
$$

也存在。

但產品不應強行矯正人格。

它可以提供：

- time report；
- fatigue signal；
- explicit policy；
- idle mode。

最終仍由成人使用者選擇。

---

# 81. Reclamation Dashboard

未來可以顯示：

```text
This month:
Travel time: 34h
Forced/unusable: 8h
Self-directed: 12h
Work: 7h
Reserve/idle: 7h
Work interruptions during rest: 3
```

這會讓 time governance 可觀察。

---

# 82. Privacy of Time Data

但 time-use data 本身非常敏感。

它可能揭露：

- 工作模式；
- 私人活動；
- 通勤；
- location；
- sleep；
- social rhythm。

因此：

$$
\boxed{
TemporalAnalytics
\in
\text{Sensitive Personal State}.
}
$$

必須承接 A-06 sovereignty。

---

# 83. 不應用來監控員工

企業 dashboard 不能默認看到：

- 員工在車上是不是在工作；
- 員工休息多久；
- 員工是否看娛樂。

除非有明確合法契約與必要性。

所以：

$$
\boxed{
TemporalOptimization
\neq
EmployeeSurveillance.
}
$$

---

# 84. Research Hypothesis H1

若：

$$
T_F\downarrow,
$$

且 autonomy 不下降，則平均：

$$
J_U\uparrow.
$$

需要實驗。

---

# 85. H2

若：

$$
T_F\downarrow
$$

且：

$$
\rho_C\uparrow
$$

到高值，則：

$$
J_U
$$

可能先上升後下降。

即：

$$
\boxed{
\text{Inverted-U Capture Hypothesis}.
}
$$

---

# 86. H3

若 Work Mode 為 user-initiated：

$$
U_W
$$

可能高於 employer-imposed mobility work。

可測：

- satisfaction；
- stress；
- productivity；
- willingness-to-pay。

---

# 87. H4

若有 `AGENT_ONLY`：

$$
HumanAttentionLoad\downarrow
$$

且：

$$
TaskProgress\uparrow.
$$

這是 AI mobility 很有價值的實驗。

---

# 88. H5

若 Journey Utility 提高：

$$
AcceptedTravelTime\uparrow.
$$

這會產生 distance / congestion rebound。

需交通模型驗證。

---

# 89. H6

若 switching cost 降低：

$$
ActivityFragmentation\uparrow
$$

可能抵銷部分 continuity benefit。

---

# 90. B-02 與 B-03 的接口

B-02 定義：

> 時間怎麼被釋放與配置。

B-03 將定義：

> 活動狀態怎麼跨物理位移不中斷。

所以：

$$
\boxed{
B02
=
\text{Temporal Allocation}
}
$$

$$
\boxed{
B03
=
\text{State Continuity}.
}
$$

---

# 91. B-02 與 B-04 的接口

B-02 有：

$$
AttentionCapacity.
$$

B-04 將把 attention 映射到：

- driver；
- passenger；
- front；
- rear；
- shared cabin。

所以：

$$
\boxed{
\text{Temporal Reclamation}
\rightarrow
\text{Spatial Attention Allocation}.
}
$$

---

# 92. B-02 與 B-06 的接口

若：

$$
J_U
$$

可以提高，

那平台就可以賣：

$$
\boxed{
\text{Journey Quality}.
}
$$

這就是 Mobility Hospitality 的時間經濟基礎。

---

# 93. 強版本與弱版本

## 弱版本

交通時間可以支援更多活動。

已有大量歷史與現代證據。

## 中版本

可程式車艙與 continuity 會顯著改變 travel-time utility 與 mode choice。

需要更多實證。

## 強版本

大量 travel disutility 被消除，進而重構都市、勞動、居住與交通經濟。

目前仍是研究命題。

---

# 94. 不做的主張

本文不主張：

1. travel time 可以完全變成 usable time；
2. automation 一定提高 welfare；
3. 在車上工作一定比辦公室有效；
4. reclaimed time 一定應該拿來休閒；
5. reclaimed time 一定應該拿來工作；
6. 所有 perpetual connectivity 都等同剝削；
7. 所有 self-selected work 都是 capture；
8. employer mobility work 在所有司法區都違法；
9. idle time 一定有高經濟產值；
10. AV 一定讓通勤變長；
11. congestion rebound 一定抵消全部利益；
12. time-use analytics 可以不受 privacy 約束。

---

# 95. 五階段時間模型

本文最終將 Travel-Time Reclamation 收斂成：

$$
\boxed{
Release
\rightarrow
Allocation
\rightarrow
Utilization
\rightarrow
Rebound
\rightarrow
Governance.
}
$$

## Release

哪些 constraint 被解除？

## Allocation

使用者把可用時間分到哪？

## Utilization

實際 activity quality 如何？

## Rebound

行為與制度是否因成本下降而擴張？

## Governance

誰控制 allocation、interrupt 與 data？

---

# 96. 最終時間狀態模型

定義：

$$
\boxed{
\Theta_t
=
(
T_F,
T_S,
T_W,
T_R,
A_T,
\rho_C,
F_A,
L_A,
J_U
).
}
$$

它包含：

- forced time；
- self-directed time；
- work time；
- reserve time；
- autonomy；
- capture；
- fragmentation；
- availability load；
- journey utility。

這是後續 Series B 可共用的 temporal state。

---

# 97. 核心治理式

成熟 PMS 不應：

$$
\max T_W.
$$

而應：

$$
\boxed{
\max U_{\text{user}}
}
$$

subject to：

$$
\boxed{
Safety,
Privacy,
Consent,
LabourRules,
Health,
Cost.
}
$$

若使用者自己的 utility 明確偏好工作，那：

$$
T_W
$$

可以很高。

這與 temporal sovereignty 不矛盾。

---

# 98. 結論

交通技術最直觀的目標一直是：

> 減少從 $A$ 到 $B$ 所需的時間。

但 AI、自動駕駛、持續網路與可程式車艙帶來另一條不同的路：

> 即使物理旅程沒有縮短，也降低其中必須被交通本身占用的注意力與活動限制。

因此：

$$
\boxed{
\text{Travel-Time Reclamation}
}
$$

不是「創造時間」。

而是：

$$
\boxed{
\text{Reduce Forced Use of Existing Time}.
}
$$

其價值取決於釋放後的配置。

若使用者用它工作，可以增加 productivity。

若用它休息，可以增加 recovery。

若用它娛樂，可以增加 journey utility。

若讓 AI 在背景繼續工作，甚至可能：

$$
SystemOutput\uparrow
$$

而：

$$
HumanWorkAttention\downarrow.
$$

真正危險的是把：

$$
\text{Capability}
$$

偷偷改寫成：

$$
\text{Obligation}.
$$

所以本篇最重要的制度命題不是：

> 人類應該把所有交通時間利用起來。

而是：

$$
\boxed{
\text{Recovered Mobility Time Should Remain Allocatable}.
}
$$

技術真正應該消除的是「被迫不能做別的事」。

不是「被允許什麼都做之後，再禁止人什麼都不做」。

---

# 參考文獻與外部研究錨點

1. de Sá, A. L. S., Lavieri, P. S., Pawlak, J., Sivakumar, A., & Thompson, R. G. (2025). **The effects of travel time use on activity-travel behaviour: knowledge consolidation and research agenda for current and future transport options.** Transport Reviews, 45(6), 869–896.  
   DOI: `10.1080/01441647.2025.2517210`

2. Xue, Q., Pudāne, B., & Kroesen, M. (2025). **How emerging time-use patterns explain travel behaviour: A systematic review.** Journal of Transport Geography, 128, 104307.  
   DOI: `10.1016/j.jtrangeo.2025.104307`

3. **Assessing the economic impacts of labour time in autonomous vehicles.** Multimodal Transportation, 5(1), 2026, 100235.  
   DOI: `10.1016/j.multra.2025.100235`

4. Öztürker, M., Nordhoff, S., Hoogendoorn-Lanser, S., van Arem, B., & Homem de Almeida Correia, G. (2026). **Use of travel time in a shared automated vehicle for work and leisure: Results from a field experiment with a Wizard-of-Oz simulator-on-wheels vehicle.** Transportation Research Part C, 188, 105646.  
   DOI: `10.1016/j.trc.2026.105646`

5. Marks, A., Bösehans, G., & Mallett, O. (2026). **The Intensification–Extensification Dynamic: Hybrid Work and Digital Connectivity.** Work, Employment and Society.  
   DOI: `10.1177/09500170261424133`

6. **Perpetual connectivity as digital labor: a conceptual reframing of the always-on work culture.** Frontiers in Public Health, 14, 2026.  
   DOI: `10.3389/fpubh.2026.1867925`

7. Quan, J., van Dierendonck, D., Wu, Z., & Feng, T. (2025). **Constrained by work: Linking daily work connectivity behavior after-hours to next-day employee job performance.** Journal of Business Research, Article 115640.  
   DOI: `10.1016/j.jbusres.2025.115640`

8. Rasulova, D., & Tanova, C. (2025). **The constant ping: Examining the effects of after-hours work connectivity on employee turnover intention.** Acta Psychologica, 254, 104789.  
   DOI: `10.1016/j.actpsy.2025.104789`

---

# 內部依賴

1. `B01_Programmable_Mobility_Space_General_Theory_v0.1.md`
2. `DEPENDENCY_MAP_A_to_B.md`
3. Series A A-06：Personal Communication Sovereignty
4. Series A A-07：EVEMISS Communication Continuum Architecture

---

# 文件狀態

**Series：** B｜Programmable Mobility & Spatial Continuum  
**Number：** B-02  
**Version：** v0.1  
**Status：** Research Paper / Canonical Source  
**Series B progress：** 2/7  
**Overall 15-document progress：** 9/15  
