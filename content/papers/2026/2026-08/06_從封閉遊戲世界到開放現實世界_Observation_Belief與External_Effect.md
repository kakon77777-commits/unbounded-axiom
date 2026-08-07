# 從封閉遊戲世界到開放現實世界：Observation、Belief 與 External Effect

**系列：** 動態通用世界狀態機：內部架構與演化規格  
**篇次：** 06 / 07  
**版本：** v0.1  
**日期：** 2026-08-01  
**性質：** 內部技術白皮書／Open-World Layer 規格  
**基準 Repository：** `kakon77777-commits/compilableworld-runtime-mvp`

---

# 摘要

前五篇都還可以在「封閉虛擬世界」假設下成立。

在目前 CompilableWorld Game Runtime 中：

- 門是開還是關，由 Runtime State 決定；
- 角色在哪裡，由 Runtime State 決定；
- Quest 是否完成，由 Runtime State 決定；
- HP、MP、物品持有者與 Scheduler tick，都由 Runtime 直接維護。

因此可近似寫成：

$$
\boxed{
S_t
\approx
\text{World Truth}
}
$$

但一旦 General World-State Runtime 開始接入：

- 實體設備；
- Robot；
- Sensor；
- Smart Room；
- 外部 API；
- 雲端服務；
- 人類操作；
- 網路世界；

這個假設立即失效。

第一個巨大差異是：

$$
\boxed{
\text{Observation}
\neq
\text{Truth}
}
$$

感測器讀到的值，只是某個來源在某個時間對世界提出的一份觀測證據。

第二個巨大差異是：

$$
\boxed{
\text{Command Sent}
\neq
\text{World Changed}
}
$$

向門鎖發出 `unlock` 指令，不代表門已經真正解鎖；呼叫外部 API 成功，也不一定代表真實系統最終狀態已經穩定到我們期望的結果。

因此，本篇提出 General Runtime 的 Open-World Layer：

$$
\boxed{
\text{Observation}
\rightarrow
\text{Claim / Evidence}
\rightarrow
\text{Fusion / Reconciliation}
\rightarrow
\text{Belief / Materialized State}
}
$$

以及外部作用鏈：

$$
\boxed{
\text{Intent}
\rightarrow
\text{Authorized Effect}
\rightarrow
\text{Dispatch}
\rightarrow
\text{Acknowledgement}
\rightarrow
\text{Observation}
\rightarrow
\text{Reconciliation}
}
$$

本篇同時明確限制：Open-World Layer 不應取代現有 Game Runtime 的簡單 authoritative state 模式。封閉世界仍可保留：

$$
\text{Action}
\rightarrow
\text{StateDelta}
\rightarrow
\text{Commit}
$$

開放世界則增加 Observation、Belief、External Effect 與 Reconciliation。

也就是：

$$
\boxed{
\text{General Runtime}
=
\text{Closed-World Core}
+
\text{Optional Open-World Semantics}
}
$$

而不是強迫所有 Game State 都變成機率分布或感測器證據。

---

# 1. 為什麼遊戲世界可以把 State 當 Truth？

目前 CompilableWorld 的 Game Runtime 是一個 synthetic world。

世界中的合法變化由：

$$
\text{ActionIR}
\rightarrow
\text{Module}
\rightarrow
\text{StateDelta}
\rightarrow
\text{Kernel Commit}
$$

產生。

如果 Kernel commit：

```text
door.locked = false
```

那對這個虛擬世界而言：

$$
\boxed{
door.locked=false
}
$$

就是目前世界真相。

不存在另一扇「真正的實體門」可能拒絕配合。

同樣：

```text
actor.position.room = tavern
```

一旦 commit，就沒有 GPS 在外面告訴 Runtime：

> 其實 actor 還在街上。

因此封閉遊戲世界具有：

$$
\boxed{
\text{Single Authoritative Mutation Boundary}
}
$$

這正是前五篇能夠先把：

- State；
- Transition；
- Authority；
- Event；
- Prototype；
- Generation；

做乾淨的原因。

---

# 2. 開放世界的第一個斷裂：State 不再完全由 Runtime 產生

假設接一個智慧門鎖。

Runtime 裡可能保存：

```text
door.locked = true
```

此時收到：

```text
sensor says locked = false
```

現在不能直接說：

> sensor 覆蓋 StateStore。

因為感測器可能：

- 延遲；
- 故障；
- 重複；
- 讀錯；
- 來源身份錯誤；
- 被 spoof；
- 時鐘不同步；
- 已經過期。

所以新輸入必須先被視為：

$$
\boxed{
O_t=
\text{Observation}
}
$$

而不是：

$$
O_t=
\text{Truth}
$$

---

# 3. ObservationIR：開放世界的新一級輸入

本篇提出未來概念：

$$
\boxed{
\text{ObservationIR}
}
$$

最小可表示為：

$$
O=
(
id,
subject,
property,
value,
source,
observed\_at,
received\_at,
confidence,
provenance,
quality
)
$$

其中：

- `id`：Observation identity；
- `subject`：被觀測的 Entity；
- `property`：觀測屬性；
- `value`：讀值；
- `source`：sensor / API / human / agent；
- `observed_at`：來源宣稱觀測時間；
- `received_at`：Runtime 收到時間；
- `confidence`：若來源提供可信度；
- `provenance`：資料來源與轉換鏈；
- `quality`：資料品質／完整性／誤差資訊。

重要的是：

$$
\boxed{
\text{ObservationIR}
\not\rightarrow
\text{Direct StateStore Commit}
}
$$

它必須先進入 Open-World Fusion / Reconciliation。

---

# 4. 不要把所有 Observation 都強迫變成 Probability

「Belief」容易讓人誤以為所有狀態都必須變成完整 Bayesian probability distribution。

這不是本篇要求。

POMDP 中，belief state 可正式定義為：

$$
b_t(s)
=
P(s_t=s\mid h_t)
$$

並以 observation 與 action 更新。

這是部分可觀測決策問題的一個嚴格模型。

但 General World-State Runtime 的實務範圍更廣。

我們可以允許：

$$
B_t
=
\text{Materialized Belief / Estimated State}
$$

包含不同表達方式：

- deterministic asserted value；
- confidence-scored value；
- probability distribution；
- interval；
- unknown；
- conflicting claims；
- stale；
- externally authoritative value。

因此：

$$
\boxed{
\text{POMDP Belief}
\subset
\text{General Runtime Belief Representations}
}
$$

這裡的「包含」是架構分類，不主張所有 Domain 都應使用 POMDP。

---

# 5. State Source Class：不同狀態要知道自己屬於哪種真相模式

未來 State 或 State Schema 應能宣告：

$$
\operatorname{SourceClass}(x)
$$

例如：

---

## 5.1 Synthetic Authoritative

完全由 Runtime 管理。

例如 Game：

```text
quest.current_state
player.hp
npc.alive
```

可以：

$$
\text{StateDelta}
\rightarrow
\text{Commit}
$$

---

## 5.2 External Authoritative

某個外部系統才是最終 authoritative source。

例如：

```text
bank.account.balance
calendar.event
cloud.job.status
```

Runtime 只能 cache / mirror。

---

## 5.3 Observed Physical

由 sensor 或 external observation 估計。

例如：

```text
door.open
room.temperature
robot.location
person.present
```

---

## 5.4 Derived / Inferred

由其他 state / observations 計算。

例如：

```text
room.occupied
robot.stuck
user.probably_asleep
```

---

這樣可以避免 Runtime 把所有 `StateCell` 都當成同一種 truth。

---

# 6. ClaimIR：Observation 與 State 中間需要一層可爭議陳述

同一個世界屬性可能同時收到：

```text
camera_1 says person.present = true
motion_sensor says person.present = false
phone_presence says person.present = true
```

如果 Observation 直接覆蓋 state，就會形成 last-write-wins 混亂。

所以可以加入：

$$
\boxed{
\text{ClaimIR}
}
$$

概念上：

$$
C=
(
subject,
predicate,
value,
source,
evidence,
valid\_time,
confidence,
status
)
$$

其中 `status` 可以是：

```text
asserted
accepted
rejected
superseded
conflicted
stale
```

這讓 Open-World Runtime 能保存：

> 有人／某系統這樣聲稱。

而不是立刻宣布：

> 世界就是這樣。

---

# 7. Provenance：世界狀態需要知道「這個值是怎麼來的」

一旦進入開放世界，`value + version` 往往不夠。

至少要追蹤：

$$
\boxed{
\text{Value}
+
\text{Source}
+
\text{Derivation}
}
$$

例如：

```text
person.present = true
```

可以是：

```text
observed_by = camera.front
inferred_by = presence_model.v3
confirmed_by = phone.bluetooth
materialized_by = fusion.presence
```

W3C PROV-O 的基本框架把 provenance 拆成 Entity、Activity、Agent，以及生成、使用與衍生關係。General Runtime 不必內部直接採 RDF/PROV-O，但可以借用這種思想作為 provenance adapter / vocabulary 參考。

因此本篇提出：

$$
\boxed{
\text{State Provenance}
}
$$

應成為 Open-World Layer 的第一級概念。

---

# 8. 時間至少要拆成 Observation Time 與 Reception Time

在封閉 Game Tick 裡：

$$
t_{\mathrm{event}}
$$

通常就足夠。

開放世界則至少需要：

$$
t_{\mathrm{observed}}
$$

與：

$$
t_{\mathrm{received}}
$$

因為：

> 十分鐘前觀測到的資料，現在才送到 Runtime。

不應被當作「剛剛發生」。

甚至未來可能需要：

- valid_from；
- valid_to；
- source_time；
- ingestion_time；
- reconciliation_time。

因此：

$$
\boxed{
\text{Event Time}
\neq
\text{Processing Time}
}
$$

---

# 9. Staleness：有效的資料也可能已經過時

假設：

```text
door.locked = true
```

最後 observation 是 6 小時前。

即使沒有新資料反駁，也不代表：

$$
P(\text{still true})=1
$$

因此 state projection 應能帶：

$$
\operatorname{Freshness}(x,t)
$$

例如：

$$
F(x,t)
=
f(t-t_{\mathrm{observed}},TTL_x)
$$

並可產生：

```text
fresh
aging
stale
unknown
```

所以未來世界狀態查詢不一定只回：

```json
{"locked": true}
```

而可能回：

```json
{
  "value": true,
  "status": "stale",
  "observed_at": "...",
  "source": "lock_sensor"
}
```

---

# 10. Fusion：多 Observation 如何形成 Materialized State？

Open-World Fusion 可以抽象成：

$$
B_{t+1}
=
\operatorname{Fuse}
(
B_t,
O_{t+1},
C_{t+1},
P
)
$$

其中 $P$ 是 Domain policy。

不同 Domain 可以使用不同 fusion：

- latest trusted source；
- source priority；
- weighted confidence；
- quorum；
- Bayesian update；
- Kalman filter；
- rule-based reconciliation；
- external authoritative override。

所以：

$$
\boxed{
\text{Fusion Policy}
\in
D_{\mathrm{adaptable/specific}}
}
$$

不應由 Universal Core 強迫所有領域使用同一演算法。

Universal Core 只需提供：

- evidence container；
- timestamps；
- provenance；
- conflict representation；
- materialized result；
- trace。

---

# 11. Conflict 不應被偷偷消失

如果：

```text
sensor_a = open
sensor_b = closed
```

Runtime 不一定應立刻挑一個勝者。

可以允許：

$$
B_t=
\text{CONFLICTED}
$$

並保留：

$$
\{C_1,C_2\}
$$

讓 policy 決定：

- 等下一筆 observation；
- 呼叫第三 sensor；
- 詢問人類；
- 使用 trusted priority；
- 升級模型；
- 停止高風險 action。

這和前面按需 AI 架構也可自然接合：

$$
\text{Conflict}
\rightarrow
\text{Escalation}
$$

而不是：

$$
\text{Conflict}
\rightarrow
\text{Guess}
$$

---

# 12. W3C WoT：適合作為外部 Thing Adapter，不必變成內部真相模型

W3C Web of Things Thing Description 2.0 以一個小型互動 vocabulary 描述 physical / virtual Thing：

- Properties；
- Actions；
- Events；

並搭配 data schema、security definitions、forms 與 links。

這對 General Runtime 很有價值。

未來可以：

$$
\text{WoT Thing Description}
\rightarrow
\text{CompilableWorld Device Adapter}
$$

例如：

```text
WoT Property
→ Observation / external state accessor

WoT Action
→ External Effect adapter

WoT Event
→ EventIR / ObservationIR source
```

但不要反過來宣告：

$$
\text{WoT TD}
=
\text{General World-State Runtime}
$$

它主要是 device interaction description，不負責我們完整的：

- world causality；
- belief；
- prototype；
- state promotion；
- reference world；
- generation governance。

所以應視為：

$$
\boxed{
\text{External Protocol / Capability Adapter}
}
$$

---

# 13. OGC SensorThings：Observation Adapter 的直接參考

OGC SensorThings API Part 1 明確以：

- Thing；
- Location；
- Datastream；
- Sensor；
- ObservedProperty；
- Observation；
- FeatureOfInterest；

組織 sensing data。

這證明：

> 「Observation」與「Thing 的真實狀態」本來就應被區分。

General Runtime 未來完全可以提供：

$$
\text{SensorThings Observation}
\rightarrow
\text{ObservationIR}
$$

adapter。

同樣：

> 不是把 SensorThings schema 全搬進 Kernel。

---

# 14. External Effect：開放世界的第二個巨大斷裂

封閉 Game Runtime：

```text
unlock
→ state delta
→ locked=false
```

就夠了。

真實門鎖則需要：

```text
request unlock
→ send command
→ device receives
→ actuator tries
→ device reports
→ sensor confirms
```

所以：

$$
\boxed{
\text{Requested Effect}
\neq
\text{Observed Effect}
}
$$

本篇提出：

$$
\boxed{
\text{ExternalEffectIR}
}
$$

作為未來 Open-World Layer 的第二個新原語。

---

# 15. ExternalEffectIR 的最小概念

可以表示為：

$$
X=
(
effect\_id,
actor,
target,
operation,
parameters,
authority,
dispatch\_adapter,
status,
deadline,
correlation
)
$$

其中 status 不能只有 success / failure。

至少需要：

```text
proposed
authorized
queued
dispatched
acknowledged
observing
reconciled
failed
timed_out
cancelled
unknown
```

這和現有 ActionStatus 可以有關係，但不建議直接混成同一 enum。

因為：

$$
\boxed{
\text{Action Lifecycle}
\neq
\text{External Effect Lifecycle}
}
$$

一個 Action 可能成功地「提交外部作用請求」，但真實 Effect 尚未完成。

---

# 16. Desired / Reported / Effective State

AWS IoT Device Shadow 是一個很有用的外部例子。

它明確區分：

- `desired`：應用希望設備成為什麼狀態；
- `reported`：設備最後報告自己是什麼狀態。

General Runtime 可以借用這個思想，進一步定義：

$$
\boxed{
S^{\mathrm{desired}}
\neq
S^{\mathrm{reported}}
\neq
S^{\mathrm{effective}}
}
$$

其中：

- $S^{\mathrm{desired}}$ ：Runtime 希望的目標狀態；
- $S^{\mathrm{reported}}$ ：外部系統回報狀態；
- $S^{\mathrm{effective}}$ ：Fusion / Reconciliation 後 Runtime 目前接受的狀態。

這三個欄位不一定對所有 Domain 都需要。

但對 physical / external system 是很有價值的 Prototype。

---

# 17. 為什麼 acknowledgement 仍然不是 Truth？

設備回：

```text
200 OK
```

可能只代表：

> 指令收到。

不代表：

> 物理結果成立。

例如：

```text
unlock request acknowledged
```

但門鎖 actuator 卡住。

所以：

$$
\boxed{
\text{Acknowledged}
\neq
\text{Observed Success}
}
$$

高風險 effect 應要求：

$$
\text{Acknowledgement}
+
\text{Post-Effect Observation}
$$

才可以 Reconcile。

---

# 18. Reconciliation：外部世界的真正 Commit

封閉 Game 世界的 atomic commit 是：

$$
\text{StateDelta}
\rightarrow
\text{StateStore}
$$

開放世界不能把「送出命令」當成相同 commit。

應拆成：

$$
\boxed{
\text{Intent Commit}
}
$$

與：

$$
\boxed{
\text{Reality Reconciliation}
}
$$

例如：

```text
desired door.locked = false
```

先成立。

接著外部設備：

```text
reported door.locked = false
```

再經 source / freshness / confidence 驗證。

最後：

```text
effective door.locked = false
```

才成立。

---

# 19. External Effect Pipeline

完整可表示為：

$$
\boxed{
\begin{aligned}
&\text{ActionIR}\\
\rightarrow\;&\text{Authority Validation}\\
\rightarrow\;&\text{ExternalEffectIR}\\
\rightarrow\;&\text{Dispatch}\\
\rightarrow\;&\text{Acknowledgement}\\
\rightarrow\;&\text{ObservationIR}\\
\rightarrow\;&\text{Claim / Evidence}\\
\rightarrow\;&\text{Reconciliation}\\
\rightarrow\;&\text{Effective State}
\end{aligned}
}
$$

注意：

`Dispatch` 之後如果沒有 Observation，不應假裝世界已改變。

---

# 20. External Effect 必須是 Idempotency-Aware

網路系統常遇到：

- timeout；
- retry；
- duplicate delivery。

如果：

```text
open door
```

重送兩次通常問題不大。

但：

```text
transfer money
```

重送兩次可能嚴重出錯。

因此 ExternalEffectIR 應能聲明：

```text
idempotency_key
retry_policy
deduplication_policy
```

CloudEvents 規格以 `source + id` 唯一識別事件，並允許接收端把相同來源與 ID 視為重複事件。General Runtime 可以參考這種 envelope 思路，但 Effect idempotency 仍要由 Domain Adapter 自己定義。

---

# 21. Effect Timeout 不能直接等於 Effect Failed

如果命令發出後 10 秒沒有回應，可能是：

- command failed；
- network lost；
- response lost；
- effect succeeded but unobserved。

所以：

$$
\boxed{
\text{Timeout}
\neq
\text{Known Failure}
}
$$

更合理是：

```text
status = unknown
```

並觸發：

- query；
- observation；
- reconciliation；
- manual escalation。

這是開放世界與遊戲世界差異很大的地方。

---

# 22. 世界狀態需要允許 UNKNOWN

封閉遊戲世界通常喜歡所有值都有答案。

開放世界必須承認：

$$
\boxed{
\text{UNKNOWN}
}
$$

例如：

```text
door.locked = unknown
```

有時比：

```text
door.locked = false
```

更正確。

因此 future State / Belief representation 需要至少能表示：

- known；
- unknown；
- conflicted；
- stale。

---

# 23. Confidence 不應偽裝成 Probability

如果某 sensor driver 給：

```text
confidence = 0.8
```

不一定代表：

$$
P(\text{truth})=0.8
$$

它可能只是模型自己的 score。

所以 Runtime metadata 應區分：

```text
confidence_score
confidence_semantics
```

例如：

```text
probability
model_score
sensor_quality
heuristic_weight
```

否則不同來源的 `0.8` 根本不可直接平均。

---

# 24. Provenance 與 Confidence 都應由 Domain Policy 解讀

Universal Core 只保存：

- source；
- method；
- score；
- time；
- lineage。

真正如何 fusion：

$$
\operatorname{Fuse}
$$

應交給 Domain-specific / Adaptable policy。

因此：

$$
\boxed{
\text{Evidence Representation}
\in
D_{\mathrm{universal/adaptable}}
}
$$

而：

$$
\boxed{
\text{Evidence Interpretation}
\in
D_{\mathrm{adaptable/specific}}
}
$$

---

# 25. Open-World State 的建議資料形狀

不應直接把現在所有 `StateCell` 都改成巨大結構。

可以保留：

```text
StateCell(value, version)
```

作為最小 Closed-World primitive。

另建立 Open-World projection / state record：

$$
X=
(
value,
version,
truth\_class,
status,
observed\_at,
updated\_at,
source,
confidence,
provenance
)
$$

也就是：

$$
\boxed{
\text{Simple State Core}
+
\text{Optional Evidence Envelope}
}
$$

避免 Game Runtime 被不必要複雜化。

---

# 26. Event Log 與 Observation Log 應區分

`EventIR` 目前主要表示 Runtime 中發生／提交的事件。

Observation 則是：

> 外部來源告訴 Runtime，它觀測到了什麼。

這兩者不應強迫合併。

可以：

```text
EventLog
ObservationLog
EffectLog
```

但保留：

- correlation；
- causation；
- timestamp；
- provenance；

互相連接。

因此可形成：

$$
\boxed{
\text{Causal Trace Graph}
}
$$

---

# 27. 外部 Event 也不能自動當 Runtime Event Truth

例如設備送來：

```text
door.opened
```

這首先可能是：

$$
O_t
$$

或：

$$
E_{\mathrm{external}}
$$

需要 adapter 驗證：

- source identity；
- schema；
- event version；
- freshness；
- signature；
- duplicate。

之後才可以產生 Runtime accepted EventIR。

因此：

$$
\boxed{
\text{External Event}
\rightarrow
\text{Adapter Validation}
\rightarrow
\text{Runtime Event}
}
$$

---

# 28. Open-World Layer 與現有 EventIR 的關係

現有 EventIR 不需要被丟掉。

反而可以把 Observation／Effect 最後接受的結果都投影成 EventIR：

```text
observation.accepted
observation.conflicted
effect.dispatched
effect.acknowledged
effect.reconciled
effect.timed_out
```

這讓既有：

- EventBus；
- EventLog；
- AMK；
- trace；
- MCP projection；

都能繼續使用。

---

# 29. RelationIR：開放世界很可能需要比 owner/path 更正式的關係

Game 中很多關係可藏在 State：

```text
item.carrier = player
actor.position.room = tavern
```

但 General Runtime 後期可能需要更明確：

$$
R=
(
subject,
predicate,
object,
validity,
source
)
$$

例如：

```text
robot located_in room
device controlled_by account
sensor observes property
person member_of household
```

本篇先把：

$$
\boxed{
\text{RelationIR}
}
$$

列為 Open-World Candidate。

但不要求第 1 版立即實作。

因為部分 relation 仍可由 StateStore 表達。

---

# 30. Open-World Runtime 不等於 Digital Twin 平台

General Runtime 未來可能被用來建立：

- digital twin；
- smart room；
- robot state；
- external agent world model。

但不應因此被限制成某一種 Digital Twin ontology。

本系列核心仍然是：

$$
\boxed{
\text{World State}
+
\text{Transition}
+
\text{Event}
+
\text{Authority}
+
\text{History}
+
\text{Adaptive Structure}
}
$$

Digital Twin 只是可能的 Domain Pack。

---

# 31. Open-World Adapter 不應污染 Universal Kernel

未來可以有：

```text
adapters/
  wot/
  sensorthings/
  mqtt/
  rest/
  ros/
  cloud_events/
```

但 Universal Kernel 不應知道：

- MQTT topic；
- HTTP code；
- ROS topic；
- WoT form；
- SensorThings endpoint。

Adapter 應負責：

$$
\text{External Protocol}
\leftrightarrow
\text{ObservationIR / ExternalEffectIR / EventIR}
$$

---

# 32. Smart Room 應成為第二 Domain 的理由

前幾篇已經提出第二 Domain 不必直接選大型 Robot。

本篇再次確認 Smart Room 很適合作為第一個 Open-World 驗證環境。

它可以很小：

```text
person
room
light
door
temperature_sensor
phone
```

但已經同時包含：

- physical observation；
- uncertain presence；
- time；
- external effect；
- authority；
- delayed event；
- device offline；
- stale state。

這剛好能驗證 Game Reference 沒有的所有主要 Open-World semantic gap。

---

# 33. Smart Room 的最小測試案例

例如：

> 屋主離開房間三分鐘後關燈。

Runtime 不能只做：

```text
presence=false
→ scheduler
→ light=false
```

而應：

```text
presence observation
→ fusion
→ effective occupancy=false
→ timer
→ authorized effect
→ light off dispatch
→ device ack
→ sensor/report confirms
→ reconciled state
```

這就是 Open-World Layer 的第一個完整 E2E。

---

# 34. Robot 作為第三 Domain 會再增加什麼？

Robot 會新增：

- pose uncertainty；
- perception；
- physical safety；
- actuator failure；
- task interruption；
- local autonomy；
- network partition；
- multi-rate control。

所以 Smart Room 先驗證：

$$
\text{Observation}
+
\text{External Effect}
+
\text{Authority}
$$

Robot 再驗證：

$$
\text{Continuous Embodied Control}
$$

比較合理。

---

# 35. Open-World Layer 與 AI 的關係

AI 不應直接把：

```text
camera image
```

轉成：

```text
StateStore person.present=true
```

正確是：

$$
\text{Sensor}
\rightarrow
\text{AI Perception}
\rightarrow
\text{Observation / Claim}
\rightarrow
\text{Fusion}
\rightarrow
\text{State}
$$

因此：

$$
\boxed{
\text{AI Inference}
\neq
\text{World Truth}
}
$$

這與前面：

$$
\text{Memory}
\neq
\text{World Truth}
$$

完全一致。

---

# 36. AI 的信念也應有 provenance

例如 AI 推斷：

```text
user.probably_asleep = true
```

應能追溯：

```text
derived_from:
  phone.motion
  room.light
  time
inferred_by:
  sleep_model.v2
confidence:
  ...
```

而不是只存一句：

```text
true
```

這使未來不同 AI 模型替換後仍可檢查：

> 這個 state 到底是誰推斷的？

---

# 37. Open-World Error Taxonomy

本篇先定義一組新的錯誤類型：

$$
E_{\mathrm{open}}
=
\{
E_{\mathrm{observation}},
E_{\mathrm{stale}},
E_{\mathrm{conflict}},
E_{\mathrm{dispatch}},
E_{\mathrm{ack}},
E_{\mathrm{effect}},
E_{\mathrm{reconcile}},
E_{\mathrm{authority}}
\}
$$

這些和 Game 的：

- invalid action；
- state conflict；
- rule failure；

不同。

未來 diagnostics 應分開記錄。

---

# 38. External Effect 的 Safety Gate

對 physical action，至少需要：

$$
\operatorname{AllowEffect}
(
actor,
effect,
target,
state,
belief,
policy
)
$$

也就是 Authority Gate 不只看 requested action。

還要看：

- effective state 是否可信；
- observation 是否 stale；
- conflict 是否未解；
- effect risk。

例如：

> door position unknown

時，不一定允許 Robot 用力關門。

所以：

$$
\boxed{
\text{Uncertainty Can Restrict Authority}
}
$$

---

# 39. Consistency 需求應依後果分級

不同 Open-World State 不需要同樣的一致性。

例如：

## 高後果

- 支付；
- 門鎖；
- 安全狀態；
- task ownership。

可能需要近強一致。

## 低後果

- 非關鍵偏好；
- comfort estimate；
- historical summary。

可以 eventual consistency。

所以：

$$
\boxed{
\operatorname{ConsistencyPolicy}
=
f(\operatorname{Consequence})
}
$$

這比「所有 State 都強一致」更實際。

---

# 40. 與現有 Snapshot / Replay 的關係

Open-World Layer 之後，Snapshot 不應假裝：

> 我可以重建真實世界。

Snapshot 只能重建：

$$
\boxed{
\text{Runtime's Materialized World Model}
}
$$

而不是物理宇宙本身。

Replay 也只能重放：

- accepted observations；
- state materialization；
- effect lifecycle；
- runtime events。

不能真的讓門重新物理開關一次。

所以必須區分：

$$
\boxed{
\text{Replay World Model}
\neq
\text{Replay Physical Reality}
}
$$

---

# 41. Simulation / Replay 時 External Effect 必須可替換

未來 Scenario／Replay 中，ExternalEffect Adapter 應可換成：

```text
FakeEffectAdapter
SimulationAdapter
RecordedEffectAdapter
```

避免測試真的打開實體門或發真實付款。

因此：

$$
\boxed{
\text{Effect Interface}
\neq
\text{Physical Adapter}
}
$$

也是通用 Runtime 的必要邊界。

---

# 42. 生成式約束在 Open-World Layer 變得更重要

前一篇 Risk Tier 5 已經把：

- external effect；
- live structural mutation；

列為最高風險。

本篇補上原因：

因為 open world 中，錯誤不只是：

> 虛擬 state 不一致。

而可能：

> 真實設備被錯誤操作。

所以：

$$
\boxed{
\text{External Effect Generation}
\Rightarrow
\text{Highest Promotion Threshold}
}
$$

AI 自動生成 physical action adapter，預設不得直接 live promotion。

---

# 43. Closed-World 與 Open-World 不應二選一

General Runtime 應允許同一個世界裡同時存在：

### Closed State

```text
simulation.quest.state
```

### External Authoritative State

```text
calendar.event.status
```

### Observed Physical State

```text
door.open
```

### Inferred State

```text
room.occupied
```

所以：

$$
\boxed{
W_t
=
W_t^{\mathrm{synthetic}}
\cup
W_t^{\mathrm{external}}
\cup
W_t^{\mathrm{observed}}
\cup
W_t^{\mathrm{inferred}}
}
$$

這才是真正的 General World-State Runtime。

---

# 44. Open-World Runtime 的建議總體管線

最後可寫成：

```text
External World
   │
   ├── Sensors / APIs / Human / Agent
   │
   ▼
Observation Adapters
   │
   ▼
ObservationIR / ClaimIR
   │
   ▼
Evidence + Provenance
   │
   ▼
Fusion / Reconciliation
   │
   ▼
Materialized World State
   │
   ├───────────► Projection / AI Context
   │
   ▼
ActionIR
   │
   ▼
Authority / Policy
   │
   ├── Closed-World Action
   │       ▼
   │    StateDelta
   │
   └── External Effect
           ▼
      ExternalEffectIR
           ▼
        Dispatch
           ▼
     Acknowledgement
           ▼
       Observation
           └──────────────► Reconciliation
```

這是第 1 篇現有 Game pipeline 的擴張，不是取代。

---

# 45. Open-World Core Candidate

本篇提出的新候選原語：

$$
\boxed{
\{
ObservationIR,
ClaimIR,
BeliefState,
ExternalEffectIR,
Provenance,
Reconciliation
\}
}
$$

其中真正是否進 Universal Core，仍需要第二 Domain 驗證。

目前先標記：

$$
\boxed{
\text{Open-World Candidate Layer}
}
$$

而不是直接升格成 Universal。

---

# 46. 核心不變量

## O-1：Observation 不等於 Truth

任何外部 Observation 預設不能直接覆蓋 authoritative state。

## O-2：AI Inference 不等於 Truth

AI 輸出先成為 Claim / Belief。

## O-3：Command Sent 不等於 World Changed

External Effect 必須有 lifecycle。

## O-4：Acknowledgement 不等於 Observed Success

高風險 effect 需要 post-effect observation / reconciliation。

## O-5：UNKNOWN 是合法世界狀態

不確定時不能強迫猜值。

## O-6：Provenance 不可丟失

重要 materialized state 必須能追溯來源。

## O-7：External Protocol 不得污染 Kernel

WoT／SensorThings／MQTT／ROS 只作 adapter。

## O-8：Closed-World 模式不得因通用化被不必要複雜化

Game StateStore 仍可保持簡單。

---

# 47. 禁止事項

## 禁止 A：Sensor 直接寫 StateStore

必須經 Observation / Fusion。

## 禁止 B：200 OK 當成物理成功

Acknowledgement 不是 Reality。

## 禁止 C：所有 Confidence 當 Probability

先保留 confidence semantics。

## 禁止 D：所有 State 都改成 POMDP belief distribution

Open-World Belief 是可選表達族，不是單一數學模型。

## 禁止 E：把 W3C WoT／SensorThings 當成內部本體

它們是 adapter / external standard。

## 禁止 F：Replay 時真的執行 physical effect

Replay 使用 Simulation/Fake adapter。

## 禁止 G：last-write-wins 解決所有 Observation 衝突

應保留 conflict / provenance / policy。

---

# 48. 尚未實作

本篇以下內容目前都屬未來 Open-World 提案：

- ObservationIR；
- ClaimIR；
- BeliefState / Evidence Envelope；
- source class；
- truth class；
- freshness；
- confidence semantics；
- provenance graph；
- fusion engine；
- ExternalEffectIR；
- desired / reported / effective state；
- effect acknowledgement；
- reconciliation；
- open-world error taxonomy；
- RelationIR；
- WoT / SensorThings adapters。

目前 CompilableWorld repo 仍然是封閉 Game World Runtime 為主。

---

# 49. 驗證條件

未來要稱 Open-World Layer v0.1 成立，至少應有一個 Smart Room Reference Domain 通過以下測試。

## V-1

Sensor observation 不直接改 authoritative state。

## V-2

兩個衝突 Observation 可以保留 conflicted state。

## V-3

stale observation 不被當作 fresh。

## V-4

來源 provenance 可追溯。

## V-5

remote door unlock 的 Action 成功，不會在 acknowledgement 前直接把 effective state 改成 unlocked。

## V-6

acknowledged 但 post-effect sensor 仍顯示 locked 時，Reconciliation 不得宣告成功。

## V-7

timeout 可以進 unknown，而不是誤判 failure / success。

## V-8

external effect replay 不會真的控制實體設備。

## V-9

Game Reference World 原有 Closed-World pipeline 不因加入 Open-World Layer而失敗。

## V-10

至少一個 external standard adapter，例如 WoT 或 SensorThings，能被映射成 internal IR 而不修改 Kernel。

---

# 50. 本篇結論

從 Game World-State Runtime 走向真正 General World-State Runtime，最大的變化不是「多支援幾種 Entity」。

真正的斷層是：

$$
\boxed{
\text{Runtime no longer owns all truth.}
}
$$

因此 General Runtime 必須學會：

> 世界可能不同意 Runtime。

感測器可能錯。

API 可能延遲。

設備可能拒絕。

命令可能成功送達但物理效果失敗。

不同來源可能互相矛盾。

這迫使架構從：

$$
\boxed{
\text{Action}
\rightarrow
\text{StateDelta}
\rightarrow
\text{Commit}
}
$$

擴張成：

$$
\boxed{
\text{Observation}
\rightarrow
\text{Evidence}
\rightarrow
\text{Belief / Materialized State}
}
$$

與：

$$
\boxed{
\text{Action}
\rightarrow
\text{External Effect}
\rightarrow
\text{Observation}
\rightarrow
\text{Reconciliation}
}
$$

但這不是否定前五篇。

恰恰相反：

> 前五篇建立的 State、Action、Event、Authority、Prototype、Constraint 與 Promotion，正是 Open-World Layer 能安全加入的原因。

因此本篇最終把整個系統擴張為：

$$
\boxed{
\text{General World-State Runtime}
=
\text{Closed-World State Runtime}
+
\text{Evidence / Belief Layer}
+
\text{External Effect Layer}
}
$$

下一篇是本系列最後一篇：

# 《動態通用世界狀態機 v0.x：演化閉環、升格機制與後續工程路線》

最後一篇不再新增大量新原語，而是把前六篇收斂成：

- Game Reference 如何持續演化；
- Prototype 如何升格／降格；
- General Runtime 如何動態吸收成功模式；
- 第二 Domain 與第三 Domain 如何驗證；
- 之後真正回到 CompilableWorld repo 時，工程順序到底怎麼排；
- 哪些先做、哪些暫時不要做。

---

# Appendix A：外部標準與研究參考

本篇重新查核以下公開資料，僅作為 Open-World Adapter／語義設計參考，不把它們宣稱為 CompilableWorld 已實作內容。

## A.1 W3C Web of Things Thing Description 2.0

W3C WoT TD 2.0 以 Thing 作為 physical / virtual entity 抽象，並使用 Properties、Actions、Events 等 interaction affordances，搭配 data schema、security definitions、forms 與 links。

Reference:
https://www.w3.org/TR/wot-thing-description-2.0/

## A.2 OGC SensorThings API

SensorThings API Part 1: Sensing 對 Thing、Location、Datastream、Sensor、ObservedProperty、Observation、FeatureOfInterest 提供標準模型。

Reference:
https://www.ogc.org/standards/sensorthings/

## A.3 AWS IoT Device Shadow

AWS Device Shadow 明確區分 `desired` 與 `reported` state，並使用版本與 timestamp 協助處理狀態同步與訊息順序。

Reference:
https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html

## A.4 CloudEvents

CloudEvents 規格以 `id`、`source`、`type` 等必要屬性提供通用事件 envelope，並定義 `source + id` 可用於識別 distinct / duplicate event。

Reference:
https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md

## A.5 W3C PROV-O

PROV-O 提供 Entity、Activity、Agent 與生成／衍生關係等 provenance vocabulary，可作為 Open-World provenance 設計參考。

Reference:
https://www.w3.org/TR/prov-o/

## A.6 POMDP Belief State

POMDP 使用 belief state 將 history 中與決策相關的資訊壓縮為對 latent state 的 posterior distribution。本文只借用其「observation 不等於 latent state」與 belief update 思想，不要求 General Runtime 全面採用 POMDP。

Reference:
https://pmc.ncbi.nlm.nih.gov/articles/PMC2748358/

---

# Appendix B：Repository Grounding

2026-08-01 再次檢查 `compilableworld-runtime-mvp`，最近主線仍停在 2026-07-15 的：

- `72334d7881749c78d323684e3ddbbc2b8aab86da`：read-only MCP、world projection、event visibility；
- `c9a33185ac7df5863e76995b0ebb097578e6be7e`：Studio runtime authoring contracts、AMK、atomic snapshot restore、regression。

因此本篇所有 Observation／Belief／ExternalEffect／Reconciliation 概念都明確標記為未來 Open-World Layer，而不是假裝目前 Repository 已經存在。
