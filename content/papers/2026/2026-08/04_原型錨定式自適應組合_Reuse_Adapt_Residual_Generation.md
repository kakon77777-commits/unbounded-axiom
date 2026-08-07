# 原型錨定式自適應組合：Reuse → Adapt → Residual Generation

**系列：** 動態通用世界狀態機：內部架構與演化規格  
**篇次：** 04 / 07  
**版本：** v0.1  
**日期：** 2026-08-01  
**性質：** 內部技術白皮書／自適應組合規格  
**基準 Repository：** `kakon77777-commits/compilableworld-runtime-mvp`

---

# 摘要

前三篇已經完成三個基礎判斷：

1. CompilableWorld 現有 Runtime 是 Game World-State Runtime Prototype，而非尚未存在的「通用完成版」；
2. Game Runtime 應保留為 Executable Reference World，而不是通用化後被淘汰；
3. 未來世界狀態語義應拆成 Universal Core、Parameterized Prototype 與 Domain-Specific Semantics 三層。

本篇開始處理真正的「動態」問題：

> **當一個新的世界需求進來時，系統究竟要如何先找既有原型、判斷可重用程度、組合多個 Prototype、處理衝突，再只對剩餘缺口進行受約束生成？**

核心原則是：

$$
\boxed{
\text{Reuse}
>
\text{Adapt}
>
\text{Constrained Synthesis}
>
\text{From-Scratch Generation}
}
$$

但本篇進一步修正一個容易過度簡化的概念：不能只依一個模糊的 `reuse_score` 決定「抄不抄」。真正的適配判斷至少需要同時比較：

- structural fit；
- semantic fit；
- authority fit；
- temporal fit；
- evidence quality；
- conflict risk；
- adaptation cost。

因此 Prototype Matching 應是多維判斷，而不是單一相似度。

本篇提出一條未來自適應組合流程：

$$
\boxed{
\text{RequirementIR}
\rightarrow
\text{Prototype Retrieval}
\rightarrow
\text{Compatibility Analysis}
\rightarrow
\text{Composition Plan}
\rightarrow
\text{Adaptation Map}
\rightarrow
\text{Residual Spec}
\rightarrow
\text{Generated Patch}
\rightarrow
\text{Compiler / Scenario / Regression}
\rightarrow
\text{Candidate World Package}
}
$$

其中 AI 可以參與檢索、語義對齊、adapter 生成與 residual synthesis，但不能直接把生成結果裝入 live StateStore。真正的世界修改仍必須回到 CompilableWorld 已建立的 Compiler、Contract、Scenario 與 Runtime 邊界。

---

# 1. 現況：目前 Repository 已有「驗證端」，但還沒有「自適應組合端」

現有 CompilableWorld 已經具備很多組合引擎未來需要依賴的下游能力：

- Authoring Layer；
- Runtime Package；
- Schema contracts；
- Studio World IR；
- Studio mapping；
- FunctionIR；
- ScenarioIR；
- ModuleContract；
- Compiler semantic validation；
- ActionIR；
- StateDelta；
- EventIR；
- Snapshot / Replay；
- Runtime diagnostics。

2026-07-15 的最新兩個主要提交仍維持這條方向：一個整合 Studio authoring contracts、AMK、snapshot restore 與 regression；另一個加入 read-only MCP、world projection、event visibility 與外部存取邊界。

因此目前系統已經比較擅長回答：

> 「這個世界定義是否合法、能不能編譯、能不能執行？」

但還不會回答：

> 「新需求應該優先重用哪一批既有世界結構？」

所以本篇提出的 Prototype Retrieval／Composition／Residual Generation 全部屬於**後續架構提案**，不是目前 repo 已實作能力。

---

# 2. 自適應組合的輸入不能只是 Prompt

如果輸入只有：

> 「幫我建立一個智慧房間世界。」

模型很容易直接從語言想像生成整套 architecture。

這正是本系列要避免的。

未來應先把自然語言需求正規化為：

$$
R_q=
(
E,
S,
A,
V,
T,
P,
C,
N
)
$$

其中：

- $E$ ：需要哪些 entity / entity category；
- $S$ ：需要哪些 state capability；
- $A$ ：需要哪些 actions；
- $V$ ：需要哪些 events；
- $T$ ：time / scheduling requirement；
- $P$ ：authority / permission requirement；
- $C$ ：semantic / operational constraints；
- $N$ ：non-functional constraints，例如 latency、offline、safety。

這裡暫稱：

$$
\boxed{
\text{RequirementIR}
}
$$

它的作用不是取代 World IR，而是成為：

> **Prototype Retrieval 與 Composition 的需求側中介表示。**

---

# 3. RequirementIR 的第一個原則：描述能力，不預設實作

例如新需求：

> 智慧房間內有人進入時開燈，夜間離開三分鐘後關燈；門鎖只有屋主可遠端解鎖。

不要一開始寫：

```text
use MQTT module
use FSM class X
use table Y
```

而應正規化成：

```yaml
entities:
  - person
  - room
  - light
  - door

capabilities:
  - occupancy
  - timed_transition
  - binary_device_state
  - remote_action
  - authorization

constraints:
  - owner_only_remote_unlock
  - delayed_light_off
```

這樣 Retrieval 才有機會從既有 Prototype 找：

- location / occupancy；
- timed state；
- authority；
- lockable door；
- action precondition。

---

# 4. Prototype Retrieval：找的是結構，不只是名稱

假設 Prototype Library 有：

```text
prototype.location.occupancy
prototype.door.lockable
prototype.task.transition
prototype.status.timed_effect
prototype.action.authorized_write
prototype.resource.depletion
```

新 Requirement 寫的是：

```text
presence
lock
delayed shutoff
owner authorization
```

若只做 keyword matching，很容易漏掉。

因此 Retrieval 至少需要兩條路。

## 4.1 Symbolic Retrieval

根據：

- capability tags；
- required state shape；
- action signature；
- event signature；
- authority template；
- dependency；
- semantic layer；

直接查 registry。

## 4.2 Semantic Retrieval

模型或 embedding 可以協助理解：

```text
timed_effect
```

與：

```text
delayed occupancy timeout
```

可能有結構相似性。

但 AI 只負責：

$$
\text{Candidate Discovery}
$$

不是直接決定：

$$
\text{Safe Reuse}
$$

所以：

$$
\boxed{
\text{Semantic Similarity}
\neq
\text{Compatibility}
}
$$

---

# 5. Matching 不應只有一個 Reuse Score

前一篇曾用：

$$
R(P_i,D)
$$

表示 reuse score。

本篇把它展開。

對 Prototype $P_i$ 與 Requirement $R_q$ ，應建立：

$$
M_i=
(
m_s,
m_\sigma,
m_a,
m_t,
m_e,
m_c
)
$$

其中：

- $m_s$ ：semantic fit；
- $m_\sigma$ ：structural / schema fit；
- $m_a$ ：authority fit；
- $m_t$ ：temporal fit；
- $m_e$ ：evidence strength；
- $m_c$ ：composition compatibility。

這些維度不應簡單平均。

某些是 hard gate。

例如：

$$
m_a=0
$$

代表 authority model 完全不相容，即使語義很像也不能直接 reuse。

所以真正決策更像：

$$
\operatorname{ReuseClass}(P_i,R_q)
=
F(M_i,\Gamma)
$$

其中 $\Gamma$ 是 hard constraints。

---

# 6. 四級適配分類

經過 Compatibility Analysis 後，每個候選 Prototype 可分類為四級。

---

## L0：Direct Reuse

不改變核心 contract 與 invariants 即可使用。

例如：

- event identity；
- versioned state；
- scheduler ordering；
- causation chain；
- snapshot metadata。

形式上：

$$
P_i'
=
P_i
$$

---

## L1：Parameterized Adaptation

結構與 invariants 可直接保留，只替換參數。

例如：

```text
game.location.room
→ smartroom.occupancy.zone
```

可以寫成：

$$
P_i'
=
P_i(\theta_D)
$$

其中 $\theta_D$ 是 Domain parameter set。

---

## L2：Structural Adaptation

只能保留：

- transition skeleton；
- authority pattern；
- scenario skeleton；
- trace shape；

但 state schema 或 semantics 需要重構。

例如：

```text
quest dependency
→ maintenance workflow dependency
```

此時：

$$
P_i'
=
\operatorname{Transform}(P_i,\mu_D)
$$

其中 $\mu_D$ 是 mapping / transformation。

---

## L3：Residual Novelty

既有 Prototype 無法合理承載。

例如從 Game 走向 Physical World 時第一次需要：

- sensor provenance；
- uncertain observation；
- external acknowledgement；
- reconciliation。

這才產生：

$$
G_{\mathrm{residual}}
$$

---

# 7. Composition Plan：不是選一個 Prototype，而是組一張圖

真實需求通常需要多個 Prototype。

例如智慧門可能需要：

$$
P_{\mathrm{lifecycle}}
\oplus
P_{\mathrm{location}}
\oplus
P_{\mathrm{authority}}
\oplus
P_{\mathrm{timed}}
$$

因此 Composition 應建成圖：

$$
G_P=(V_P,E_P)
$$

其中：

- $V_P$ ：selected prototypes；
- $E_P$ ：dependency / conflict / precedence relations。

edge type 至少可以有：

```text
requires
provides
conflicts
overrides
observes
writes
emits
subscribes
```

這比簡單 list 更適合世界狀態機。

---

# 8. Composition 前必須做 Namespace Collision 檢查

如果：

```text
prototype.lifecycle
```

想寫：

```text
status.current
```

而：

```text
prototype.device_availability
```

也想寫：

```text
status.current
```

可能產生模糊 ownership。

因此在產生 Runtime Package 之前，要檢查：

$$
W(P_i)\cap W(P_j)
$$

若交集非空，必須判斷：

- 是否允許共同寫；
- 是否有明確 owner；
- 是否需要 merge function；
- 是否需要 precedence；
- 是否應直接拒絕。

未來應優先：

$$
\boxed{
\text{Compile-Time Conflict Detection}
}
$$

而不是讓兩個 Module 在 live Runtime 裡搶 state。

---

# 9. Action Collision 也必須檢查

現有 `WorldRuntime.module_for()` 已要求：

> 同一 verb 必須恰好有一個 Module provider。

這本身就是非常好的 Composition invariant。

所以 Prototype Composition 必須保留：

$$
\left|
\operatorname{Provider}(verb)
\right|=1
$$

除非未來明確設計：

- router action；
- namespaced verb；
- dispatch policy。

否則兩個 Prototype 都宣告：

```text
open
```

不能靠來源順序決定誰贏。

---

# 10. Event Collision 與 Event Semantics

Event 名稱相同，也不代表語義相同。

例如：

```text
state.changed
```

如果不同 Prototype payload 不一致，會形成隱性錯誤。

所以 Prototype 應描述：

$$
E_i=
(
type,
payload\ schema,
visibility,
authority,
version
)
$$

Composition 必須檢查：

- event type duplicate；
- payload compatibility；
- event ownership；
- subscriber expectation；
- visibility policy。

現有 EventIR 已有 `version`，未來可以利用它建立更正式的 Event Contract。

---

# 11. Authority Compatibility 應該是 Hard Gate

如果某個 Prototype 原本允許：

```text
player → unlock door
```

而新 Domain 是：

```text
remote guest → physical front door
```

即使 action 結構完全一樣，也不能因為 reuse score 高就直接套用。

所以：

$$
\boxed{
\text{Authority Fit}
}
$$

必須是硬限制之一。

可以定義：

$$
\operatorname{CompatibleAuthority}(P,R_q)
\in
\{0,1\}
$$

若為 0：

$$
\text{Direct Reuse}
\rightarrow
\text{Forbidden}
$$

只能進入重新適配或客製。

---

# 12. Temporal Compatibility 不能忽略

Game 中：

```text
3 exchanges
```

與智慧房間：

```text
180 seconds
```

都可以叫「duration」。

但兩者的 clock semantics 不同。

所以 Prototype 要聲明：

```text
clock_domain
duration_unit
pause_policy
resume_policy
expiry_policy
```

否則 `timed_status` 很容易被錯誤通用化。

本篇因此新增一條判斷：

$$
\boxed{
\text{Temporal Similarity}
\neq
\text{Temporal Compatibility}
}
$$

---

# 13. Gap Detection：真正要生成的是覆蓋不到的集合

若 Requirement capability set 為：

$$
C_R
$$

已選 Prototype 覆蓋：

$$
C_P
=
\bigcup_i
C(P_i)
$$

則 Residual：

$$
\boxed{
C_G
=
C_R-C_P
}
$$

但還要扣除：

- 被 adaptation 補足的；
- 被 policy 解決的；
- 被 existing domain module 提供的。

最後才得到：

$$
G_{\mathrm{residual}}
$$

這才是 AI 可以生成的主要範圍。

---

# 14. Generation Budget 應加入風險，而不只是覆蓋率

前一篇提出：

$$
B_g=1-R_{\mathrm{coverage}}
$$

本篇保留這個直覺，但加入 risk weight。

更合理可以寫成：

$$
B_g
=
\sum_{c\in C_G}
w(c)
$$

其中：

- projection gap：低權重；
- pure function gap：較低；
- new state schema：中；
- new transition：中高；
- new authority path：高；
- external physical effect：非常高。

所以同樣只有 $10\%$ residual：

> 少一個顯示 projection

和：

> 少一條 physical actuator authority path

完全不是同樣的 generation risk。

---

# 15. Minimum Novelty Principle

本篇正式提出：

$$
\boxed{
\text{Minimum Novelty Principle}
}
$$

在滿足 Requirement 的前提下，Composition Planner 應盡量最小化：

$$
J_{\mathrm{novel}}
=
\alpha N_{\mathrm{schema}}
+
\beta N_{\mathrm{module}}
+
\gamma N_{\mathrm{transition}}
+
\delta N_{\mathrm{authority}}
+
\epsilon N_{\mathrm{event}}
$$

也就是不要因為 AI 能生成，就創造：

- 更多 namespace；
- 更多 module；
- 更多 transition；
- 更多 authority；
- 更多 event type。

越少的新語義面積，越容易驗證。

---

# 16. Generated Output 不應是 Live Runtime Mutation

這是整篇最重要的安全邊界之一。

AI 產出的結果應該是：

$$
\boxed{
\text{Proposed World Patch}
}
$$

例如：

- new Authoring diff；
- Prototype parameter set；
- mapping；
- FunctionIR；
- ScenarioIR；
- Module contract proposal。

而不是：

$$
\text{AI}
\rightarrow
\text{StateStore.commit()}
$$

也不是：

$$
\text{AI}
\rightarrow
\text{直接修改 live module code}
$$

因此完整流程：

$$
\boxed{
\text{Generated Patch}
\rightarrow
\text{Compiler}
\rightarrow
\text{Validation}
\rightarrow
\text{Scenario}
\rightarrow
\text{Regression}
\rightarrow
\text{Candidate Package}
}
$$

---

# 17. 「動態生成」需要分三種，不應混為一談

未來提到 Dynamic World State Runtime 時，至少要分：

---

## Mode A：Authoring-Time Dynamic Composition

AI／Composer 動態組合新世界，但完成後仍：

$$
\text{Compile}
\rightarrow
\text{Deploy}
$$

這應是第一階段主要模式。

---

## Mode B：Staged Runtime Extension

Runtime 運行中產生新候選內容，但先進：

```text
shadow package
candidate module
sandbox scenario
```

驗證後才切換。

這是較後期能力。

---

## Mode C：Live Structural Mutation

直接在 live world 中新增：

- schema；
- module；
- transition；
- authority contract。

這是最高風險模式。

第一批 General Runtime 不應把它當預設能力。

所以：

$$
\boxed{
A
\rightarrow
B
\rightarrow
C
}
$$

應該是成熟順序。

---

# 18. Runtime State 的動態變化與 Runtime Structure 的動態生成必須分開

現在 Game Runtime 已允許：

- state change；
- dynamic player entity；
- scheduler；
- action；
- quest transition。

這些是：

$$
\boxed{
\text{Dynamic State}
}
$$

但未來自適應組合談的是：

- 新 Prototype；
- 新 Schema；
- 新 Module；
- 新 Contract。

這是：

$$
\boxed{
\text{Dynamic Structure}
}
$$

兩者不能混用同一權限。

可以表示：

$$
\text{State Mutation Authority}
\neq
\text{Structure Mutation Authority}
$$

這一條應成為未來 General Runtime 的核心治理原則。

---

# 19. AI 應該是 Planner / Adapter，不是唯一 Matching Oracle

Prototype Retrieval 可以使用 LLM。

但最終 Composition 不應只相信：

> 「我覺得這兩個東西很像。」

應該混合：

$$
\boxed{
\text{Symbolic Contract Matching}
+
\text{Schema Comparison}
+
\text{Scenario Evidence}
+
\text{Semantic Model Assistance}
}
$$

也就是：

> 模型幫忙找到候選，Contract 幫忙決定能不能用。

---

# 20. Provenance：每一個 Adaptation 都要知道自己從哪裡來

未來生成的新 World IR 或 Module 應保存：

```text
derived_from:
  - prototype.task.transition@0.2
  - reference_world.game@0.5

adaptation:
  mapping: ...
  generated_fields: ...
  overridden_invariants: ...
```

可以抽象成：

$$
L(P')
=
(
source,
version,
mapping,
generated,
validated
)
$$

這就是 Prototype Lineage。

沒有 lineage，未來出 bug 時會不知道：

> 是原 Prototype 有問題，還是 adaptation 時引入的？

---

# 21. Example：智慧房間如何「抄」Game Reference World

假設需求：

> 人進入房間後自動開燈；離開三分鐘後關燈；屋主可以遠端解鎖門；訪客不能。

先抽 RequirementIR。

---

## 21.1 可直接重用

Universal Core：

- Entity；
- State version；
- ActionIR；
- EventIR；
- Scheduler；
- ModuleContract；
- Snapshot；
- Projection。

---

## 21.2 可參數化原型

從 Game Reference 抽：

### Location / Occupancy

```text
room membership
→ physical room occupancy
```

### Timed Status

```text
effect duration
→ occupancy timeout
```

### Lockable Door

```text
locked/unlocked
→ physical lock state
```

### Authorized Action

```text
actor authority
→ homeowner / visitor role
```

---

## 21.3 結構類比但不能直接抄

Game 中：

```text
unlock action commits state
```

Physical world 不行。

因為：

$$
\text{Command Sent}
\neq
\text{Door Actually Unlocked}
$$

這一段就形成：

$$
G_{\mathrm{residual}}
$$

需要未來 Open-World Layer 的：

- effect dispatch；
- acknowledgement；
- observation；
- reconciliation。

所以不是：

> 遊戲 Door Prototype 沒用。

而是：

> 它覆蓋了狀態、authority、transition 的一部分；只剩 physical effect semantics 需要新生。

這正是 Residual Generation 的意義。

---

# 22. Example：Robot Task 也不是從零開始

假設：

> 家用機器人接到「把水拿來」任務。

可以從 Game Reference 重用／適配：

- Entity；
- location；
- item ownership/custody；
- task transition；
- scheduler；
- resource；
- authority；
- action precondition。

真正新增的可能是：

- perception uncertainty；
- navigation confidence；
- actuator acknowledgement；
- physical grasp verification。

所以：

$$
\boxed{
\text{Robot Domain}
\neq
\text{Game Domain}
}
$$

但：

$$
\boxed{
\text{Robot Domain}
\not\Rightarrow
\text{From Scratch}
}
$$

---

# 23. Composition Failure Modes

本篇列出第一批需要防止的失敗模式。

## F-1：Semantic Overfit

因為名字相似就硬套 Prototype。

## F-2：Namespace Collision

多 Prototype 搶同一 state path。

## F-3：Verb Collision

兩個 Module 提供同一 action。

## F-4：Event Drift

同 event type 但 payload semantics 不同。

## F-5：Authority Escalation

Adaptation 後意外擴大權限。

## F-6：Temporal Mismatch

把 turn／tick／wall-clock 混在一起。

## F-7：Hidden Novelty

表面 reuse，實際上大量行為已被偷偷生成。

## F-8：Prototype Cascade

為了解決一個需求自動拉入大量 Prototype，最後變成巨大依賴圖。

## F-9：False Generalization

為了提高 reuse 強迫 Domain 改變自己的真實語義。

---

# 24. Composition Planner 應能選擇「不要重用」

這點非常重要。

最好的 Adaptation Planner 不一定永遠選 reuse。

若：

$$
C_{\mathrm{adapt}}
>
C_{\mathrm{custom}}
$$

或者 adaptation 會造成：

- semantic distortion；
- authority confusion；
- excessive dependencies；
- hard-to-test behavior；

那應該選：

$$
\boxed{
\text{Custom Domain Module}
}
$$

因此：

> 「可以抄的就抄」的前提是「抄了仍然是對的」。

---

# 25. 與 RDR 的關係

Prototype Composition 與 RDR 不應混成同一層。

Prototype Composition 主要處理：

$$
\text{世界結構如何被建立}
$$

RDR 未來主要處理：

$$
\text{大量規則在 Runtime 中如何有效派發}
$$

因此：

$$
\boxed{
\text{Composition Time}
\neq
\text{Dispatch Time}
}
$$

當 AI 生成的宏／中／微規則量真的膨脹後，RDR 的 memoization、reified dispatch、SCC diagnostics 才會進入 Runtime execution optimization。

---

# 26. 第一版 Composer 不需要「全自動」

如果未來真的實作 v0.1，我會建議先做：

```text
RequirementIR
→ retrieve candidates
→ produce Composition Report
→ human/agent review
→ generate mapping draft
→ compile
```

先不要做：

```text
Prompt
→ auto-compose
→ auto-deploy
```

原因是目前 Game World-State Runtime v0.2 本身都還沒有完成。

所以 Composer 第一版應是：

$$
\boxed{
\text{Decision Support Tool}
}
$$

而不是 autonomous deployment system。

---

# 27. 建議的 Composition Report

未來可輸出：

```yaml
requirement_id: smart_room.v1

selected:
  - prototype.location.occupancy
  - prototype.status.timed_effect
  - prototype.action.authorized_write

direct_reuse:
  - event.identity
  - state.version

adapt:
  - from: prototype.door.lockable
    mapping: ...

residual:
  - physical_effect_ack
  - sensor_observation

conflicts: []

risk:
  authority: high
  state: medium
  projection: low

generation_budget:
  weighted_residual: 0.31
```

這比直接生成 code 更適合作為內部審查資產。

---

# 28. 核心不變量

## A-1：Reuse 不得跳過 Validation

$$
\text{Reused}
\neq
\text{Automatically Trusted}
$$

## A-2：Semantic Similarity 不等於 Compatibility

AI 相似度只能產生候選。

## A-3：Structure Mutation Authority 高於 State Mutation Authority

新增 Module／Schema／Authority 的權限必須更嚴格。

## A-4：Residual Generation 必須最小化新語義面積

遵守 Minimum Novelty Principle。

## A-5：所有生成結果必須可追溯

Prototype lineage 不可丟失。

## A-6：Composer 不能成為第二個 Runtime

它只能輸出 authoring / mapping / candidate package，不可直接擁有 live StateStore mutation path。

---

# 29. 尚未實作

本篇以下內容全部屬於未來設計：

- RequirementIR；
- Prototype Registry；
- Prototype Retrieval；
- multidimensional compatibility analysis；
- Composition Graph；
- Generation Budget；
- Minimum Novelty objective；
- Prototype Lineage；
- Composition Report；
- staged runtime extension；
- structural mutation authority。

目前 repo 仍主要提供：

> 可供這些能力未來驗證的 Compiler／Runtime／Scenario／Contract 基底。

---

# 30. 驗證條件

未來若實作第一版自適應組合器，至少應通過：

## V-1

同一 Requirement 在固定 Prototype Registry 下可產生可重現的 candidate set。

## V-2

存在 hard authority conflict 時不得進 Direct Reuse。

## V-3

Prototype namespace / verb / event collision 能在 compile 前被偵測。

## V-4

Residual Spec 能明確區分「已覆蓋」與「真正新需求」。

## V-5

Generated Patch 不直接修改 live StateStore。

## V-6

所有 adaptation 保留 lineage。

## V-7

Candidate Package 必須通過原 Reference World regression 與新 Domain Scenario。

## V-8

當 Custom Module 比 adaptation 更乾淨時，Planner 能合法選擇不 reuse。

---

# 31. 本篇結論

動態通用世界狀態機的「動態」不應被理解為：

> AI 隨時在 live Runtime 裡自由生成新規則。

第一階段更合理的定義是：

$$
\boxed{
\text{Dynamic}
=
\text{Requirement-Driven Adaptive Composition}
}
$$

也就是根據新世界需求，動態決定：

- 哪些 Core 直接重用；
- 哪些 Prototype 參數化；
- 哪些結構需要轉換；
- 哪些衝突必須解決；
- 哪些剩餘部分才允許新生成。

完整流程收斂為：

$$
\boxed{
\text{RequirementIR}
\rightarrow
\text{Retrieve}
\rightarrow
\text{Match}
\rightarrow
\text{Compose}
\rightarrow
\text{Adapt}
\rightarrow
\text{Gap Detect}
\rightarrow
\text{Residual Generate}
\rightarrow
\text{Validate}
}
$$

其中最重要的兩條原則是：

$$
\boxed{
\text{Generate Only the Residual}
}
$$

與：

$$
\boxed{
\text{Minimum Novelty Principle}
}
$$

這使 AI 的生成能力不再被取消，而是從「世界的自由作者」改成：

> **Reference-Anchored Adapter、Planner 與 Residual Synthesizer。**

下一篇將進一步把「Validate」展開：

# 《生成式約束：動態世界結構如何生成而不退化成 AI 亂寫》

下一篇會正式定義：

- Syntax Constraint；
- Schema Constraint；
- Semantic Constraint；
- Authority Constraint；
- Behavioral Constraint；
- Risk Tier；
- Generated Diff Review；
- Scenario Gate；
- Promotion / Rollback；

也就是回答：

> **即使只生成 Residual，我們還要如何保證 AI 生成出來的世界結構不能直接越過系統邊界？**

---

# Appendix A：Repository Grounding

本篇重新檢查 2026-08-01 時該 repository 的最近提交；最新仍為：

- `72334d7881749c78d323684e3ddbbc2b8aab86da` — read-only MCP / world projection / event visibility；
- `c9a33185ac7df5863e76995b0ebb097578e6be7e` — Studio runtime authoring contracts / AMK / atomic snapshot restore / regression。

因此本篇沒有假設七月中之後已經出現新的 Prototype Composer 實作。

本篇沿用 repo 已存在的幾項關鍵 invariant：

- 同 verb 不應存在模糊多 provider；
- Module write scope 由 Kernel 強制；
- AI / UI 不直接修改 StateStore；
- Authoring / Compiled / Runtime 分離；
- Scenario 走正常 ActionIR / Kernel / EventIR；
- Studio mapping / preview 不直接改 Runtime State。

本篇新增的 RequirementIR、Prototype Retrieval、Composition Graph、Residual Spec 與 Generation Budget 均屬後續架構提案。
