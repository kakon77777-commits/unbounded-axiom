# 從 CompilableWorld Runtime 到世界狀態機：現況盤點與演化邊界

**系列：** 動態通用世界狀態機：內部架構與演化規格  
**篇次：** 01 / 07  
**版本：** v0.1  
**日期：** 2026-08-01  
**性質：** 內部技術白皮書／工程接手基準  
**基準 Repository：** `kakon77777-commits/compilableworld-runtime-mvp`  
**基準 Runtime：** `CompilableWorld Runtime MVP v0.1.1`

---

# 摘要

本文件不重新發明一套世界狀態機，而是先盤點目前 CompilableWorld Runtime 已經完成的能力，回答兩個問題：

1. 哪些部分已經具有「通用世界狀態 Runtime」的雛形？
2. 哪些部分仍然是遊戲 Domain，應繼續留在 Game Runtime 中演化？

目前 Repository 已經具備 Authoring Layer、Compiled Runtime Package、Entity Registry、State Store、ActionIR、StateDelta、EventIR、ModuleContract、EventBus、Scheduler、Snapshot、Replay、Projection、FunctionIR、ScenarioIR、Studio migration、AMK evidence layer 與 read-only MCP projection 等結構。它已經超過一般單一 FSM，也不再只是傳統 MUD command engine。

其中最重要的現況是：`StateStore`、`ActionIR`、`StateDelta`、`EventIR`、`ModuleContract`、Scheduler 與 Kernel commit pipeline 本身並未被遊戲語義完全綁死；真正明顯的遊戲專用內容主要集中於 Player 建立流程、Combat／Quest／Inventory／Magic／Dialogue 等 Module、遊戲 Authoring Schema 與具體世界內容。

因此後續正確路線不是：

$$
\text{Game Runtime}
\rightarrow
\text{全部推翻}
\rightarrow
\text{Universal Runtime}
$$

而是：

$$
\boxed{
\text{完成 Game World-State Runtime}
\rightarrow
\text{保留為 Executable Reference World}
\rightarrow
\text{逐步抽取可泛化 Core}
}
$$

本篇的主要作用，就是把這條演化邊界釘死。

---

# 1. 現況：目前 CompilableWorld 已經不是普通 FSM

傳統有限狀態機可以表示為：

$$
q_{t+1}=\delta(q_t,e_t)
$$

它主要回答：

> 某個有限離散狀態收到事件後，應轉移到哪個下一狀態？

目前 CompilableWorld 更接近：

$$
W_{t+1}
=
F(
W_t,
A_t,
E_t,
T_t,
P_t
)
$$

其中：

- $W_t$ ：當前 Runtime 世界狀態；
- $A_t$ ：正規化行動；
- $E_t$ ：事件與因果歷史；
- $T_t$ ：Scheduler 與時間；
- $P_t$ ：權限、版本與執行約束。

現有架構流程已經形成：

```text
JSON / CSV / Manifest
        ↓ compiler + validators
Runtime Package
        ↓ loader
World Kernel
        ↓ ActionIR
MSSP Module
        ↓ StateDelta + EventIR
Atomic Commit / Event Log / Projection
```

所以真正核心已經是：

$$
\boxed{
\text{State Runtime}
+
\text{Transition Providers}
+
\text{Event Causality}
+
\text{Execution Governance}
}
$$

這比「大量 FSM 拼在一起」更接近真正世界狀態 Runtime 的定義。

---

# 2. 現有真相來源已經被刻意分層

目前 `AGENTS.md` 的第一條核心不變量就是：

> Authoring Layer、Compiled Package、Runtime State 不可混為同一真實來源。

形式化為：

$$
\boxed{
W_{\mathrm{author}}
\neq
W_{\mathrm{compiled}}
\neq
W_{\mathrm{runtime}}
}
$$

三者分工如下。

## 2.1 Authoring Layer

負責：

- JSON／CSV／Manifest；
- `functions.json`；
- `scenarios.json`；
- Studio World IR；
- mapping；
- 人工與 Agent 可編輯世界來源。

它代表「世界如何被定義」，不是目前正在運行中的真實狀態。

## 2.2 Compiled Runtime Package

負責：

- 已驗證的 entities／rooms／exits／items；
- quest transitions；
- narrative overlays；
- FunctionIR；
- ScenarioIR；
- player templates；
- schema contract IDs。

它是：

$$
\boxed{
\text{Executable World Definition}
}
$$

## 2.3 Runtime State

由 `StateStore` 與 Kernel 維護。

它回答：

> 此 Runtime instance 現在到底發生了什麼？

這三層分離是未來自適應生成、通用化與多 Domain 共存時最重要的基礎之一，不得被破壞。

---

# 3. StateStore：目前最接近 Domain-Neutral Core 的元件

現有 `StateStore` 使用：

```text
owner :: namespace :: key
```

形成 state path。

最小狀態單元為：

```text
StateCell
  value
  version
```

因此 Kernel 本身不需要理解：

- HP；
- MP；
- Quest；
- Door；
- Battery；
- Temperature；
- Robot Pose。

它只知道：

$$
x=
(
owner,
namespace,
key,
value,
version
)
$$

這一點非常重要。

它表示「遊戲內容」並沒有被硬寫進最底層狀態模型。

現階段應把 StateStore 視為：

$$
\boxed{
\text{Candidate General State Substrate}
}
$$

而不是急著改寫。

---

# 4. StateDelta：世界變化不是任意寫入，而是受治理的提案

目前 Module 不應直接修改 StateStore。

Module 必須產生 `StateDelta`，包含：

- owner；
- namespace；
- key；
- operation；
- value；
- expected_version；
- source_module。

Kernel 再依 `ModuleContract.write` 驗證是否合法。

因此：

$$
\boxed{
\text{Module}
\rightarrow
\text{StateDelta}
\rightarrow
\text{Kernel Validation}
\rightarrow
\text{Atomic Commit}
}
$$

而不是：

$$
\text{Module}
\rightarrow
\text{Direct State Mutation}
$$

這是未來通用 Runtime 最應保留的核心之一。

因為無論未來 Domain 是遊戲、機器人、智慧房間或其他系統，只要都必須經過：

$$
\text{Proposal}
\rightarrow
\text{Validation}
\rightarrow
\text{Commit}
$$

就能持續維持可觀測、可測試、可回放的世界變化。

---

# 5. ActionIR：不同入口共用的行動邊界

目前 `ActionIR` 主要包含：

- `actor_id`
- `verb`
- `target_id`
- `args`
- `action_id`
- `correlation_id`
- `status`
- `authority`
- `proposed_at_tick`

這些欄位沒有把 `attack`、`cast`、`talk`、`move` 寫死進模型。

那些只是 Module 所註冊的 verb。

因此可抽象為：

$$
A_t=
(
actor,
verb,
target,
args,
authority,
correlation
)
$$

未來：

- CLI；
- Web；
- AI；
- MCP；
- Robot Adapter；
- Tool Adapter；

都可以產生相同形式的 Action。

現有 `AGENTS.md` 已明確禁止：

> UI、Intent Parser 與 AI Adapter 直接修改 `StateStore`。

所以長期不變量應是：

$$
\boxed{
\text{External Intent}
\rightarrow
\text{ActionIR}
\rightarrow
\text{Kernel}
}
$$

而不是讓每一種入口都建立自己的寫入旁路。

---

# 6. EventIR：世界的因果歷史已經有正式雛形

目前 `EventIR` 包含：

- `event_type`
- `source`
- `payload`
- `target`
- `event_id`
- `causation_id`
- `correlation_id`
- `timestamp_tick`
- `visibility`
- `authority`
- `version`

因此它已經不是普通 log message。

可以形式化為：

$$
E=
(
id,
type,
source,
target,
cause,
correlation,
time,
visibility,
authority,
payload
)
$$

它同時被用於：

- EventBus；
- EventLog；
- module reaction；
- trace；
- replay；
- MCP projection；
- AMK evidence capture。

目前跨模組協作也已被規定透過 Event，而不是直接呼叫其他模組的 private method。

因此 `EventIR` 可以視為：

$$
\boxed{
\text{World Causality Exchange Primitive}
}
$$

這也是後續世界狀態機真正能擴張的重要原因。

---

# 7. ModuleContract：真正重要的是權限邊界，而不是模組名稱

`ModuleContract` 目前描述：

- module_id；
- version；
- layer；
- actions；
- events；
- read；
- write；
- requires_kernel。

目前已經真正強制：

$$
\text{write scope}
$$

但 Repository 也明確記錄：

> generalized read-scope 與 action-authority isolation 尚未完整。

因此目前狀態應分成：

### 已完成

$$
\boxed{
\text{Write Authority Enforcement}
}
$$

### 尚未完成

$$
\boxed{
\text{Read Authority Enforcement}
+
\text{Action Authority Isolation}
}
$$

這兩項不是「等通用版再做」。

它們應該先在 Game World-State Runtime v0.2 裡完成。

因為遊戲本身已經足以提供可靠測試場。

---

# 8. Scheduler：目前已有時間，但還不是完整 World Time

Scheduler 已經支援：

- tick；
- delayed Action；
- due tick；
- queue；
- snapshot persistence。

因此至少已經有：

$$
A_t
\xrightarrow{\Delta t}
A_{t+\Delta t}
$$

但尚未形成完整 Temporal Runtime，例如：

- repeating schedule；
- cancellation tree；
- temporal dependency；
- time window；
- world calendar；
- cross-layer scheduled transition。

後面應逐步把 Scheduler 升格為：

$$
\boxed{
\text{World Time Substrate}
}
$$

而不是只視為「延遲執行 command 的工具」。

---

# 9. Snapshot + Event Log + Replay：已形成「現在＋歷史」雙軌

目前 Runtime 已經可以：

- save snapshot；
- load snapshot；
- 保存 scheduler；
- 保存 dynamic entities；
- replay committed state deltas。

因此目前架構不是純 Event Sourcing，也不是純 Snapshot。

它更接近：

$$
\boxed{
\text{Materialized Current State}
+
\text{Causal Event History}
}
$$

這是合理的。

後續不應為追求架構純粹而要求：

> 所有世界都必須從 Genesis Event 重播。

真正需要補的是：

$$
\boxed{
\text{Cross-Version Replay Migration}
}
$$

也就是當：

$$
Runtime_{v1}
\rightarrow
Runtime_{v2}
$$

時，舊 Snapshot／EventIR 如何被顯式 migration，而不是默默失效。

---

# 10. FunctionIR：純計算與世界變化已被正確拆開

現有 FunctionIR 有幾個很好的限制：

- 只允許受限 numeric expression tree；
- 不允許任意 Python；
- 無 I/O；
- 不直接寫 state；
- deterministic；
- cache 可重建、不進 snapshot。

因此：

$$
\boxed{
\text{Pure Calculation}
\neq
\text{World Mutation}
}
$$

這條分界應長期保留。

未來無論新增：

- 遊戲公式；
- 機器人功耗估算；
- 智慧房間舒適度；
- 任務權重；

只要是純函數，都不應自動取得世界狀態修改權。

---

# 11. ScenarioIR：未來生成式約束的測試基底已經存在

ScenarioIR 目前採：

$$
\text{Given}
\rightarrow
\text{When}
\rightarrow
\text{Then}
$$

而 `when` 仍走正常：

$$
\text{ActionIR}
\rightarrow
\text{Kernel}
\rightarrow
\text{EventIR}
$$

管線。

Scenario 不能偷偷形成第二套 rules engine。

這非常重要。

因為未來 AI 生成或適配新的：

- Module；
- Transition；
- State schema；
- Action；
- Domain rule；

都可以先用 ScenarioIR 驗證。

所以後續 constrained generation 的 behavioral constraint，可以直接建立在現有 Scenario 基礎之上。

---

# 12. Studio：世界定義已經開始從 Python Runtime 抽離

現有 Studio 白皮書已經提出：

$$
\boxed{
\text{CompilableWorld Studio}
\rightarrow
\text{Validated World IR}
\rightarrow
\text{Runtime Targets}
}
$$

並明確主張：

> Python Runtime 是第一個參考執行器，而不是世界本身。

這個方向必須保留。

因為未來真正的 Prototype Library、Reference World Anchor、自適應適配與多 Runtime target，都要求：

$$
\text{World Definition}
\neq
\text{Python Classes}
$$

Studio／World IR 因此不是 UI 附件，而是未來通用化的上游基礎。

---

# 13. AMK：記憶沒有被誤認為世界真相

現有規約已經定義：

> AMK Raw／Clean 是 Runtime Event Log 與 State 的外部證據層，不可冒充或覆蓋世界真實來源。

因此：

$$
\boxed{
\text{Memory}
\neq
\text{Runtime Truth}
}
$$

合理方向是：

$$
\text{World State/Event Log}
\rightarrow
\text{Memory Evidence Capture}
$$

而不是：

$$
\text{Model Memory}
\rightarrow
\text{Direct State Override}
$$

這條邊界未來非常重要。

因為到了 Open-World Layer，還會加入：

- observation；
- inference；
- belief；
- external evidence。

如果連 Memory 與 Runtime State 都沒有分開，後面一定會失控。

---

# 14. MCP：外部 Agent 的讀取界面已經開始建立

2026-07-15 的 read-only MCP 提交已建立：

- `list_worlds`
- `open_world_session`
- `get_world_status`
- `get_current_scene`
- `get_recent_events`
- `close_world_session`

同時規定：

- MCP Adapter 不取得 `StateStore.commit()` 或 `seed()`；
- MCP Session 不屬於 Runtime State；
- Session open/close 不產生世界事件；
- Event output 必須依 visibility / actor / role filter；
- unknown visibility 採 fail-closed。

這代表：

$$
\boxed{
\text{External Access}
\neq
\text{World Mutation Authority}
}
$$

這個方向是正確的。

未來就算加入 write-capable MCP，也應走：

$$
\text{MCP Request}
\rightarrow
\text{ActionIR}
\rightarrow
\text{Kernel}
$$

而不是提供 direct state write。

---

# 15. 哪些部分目前已高度接近通用核心？

以下不是宣告「Universal v1.0 已完成」，而是判斷其抽象方向已足夠乾淨，可以作為 General Runtime Candidate Core：

- Entity Registry
- StateStore
- StateCell version
- StateDelta
- ActionIR
- EventIR
- EventBus
- EventLog
- Scheduler
- Snapshot / Replay
- ModuleContract
- FunctionIR
- ScenarioIR
- Projection boundary
- Compiler / Runtime separation
- read-only external access boundary

可以暫時記為：

$$
\boxed{
C_{\mathrm{candidate}}
}
$$

注意：

> Candidate 不代表現在就要抽成另一個 repo。

先完成遊戲 Runtime，比提早切包更重要。

---

# 16. 哪些部分明顯仍然是 Game Domain？

目前 `WorldRuntime.create_player()` 會直接建立與 seed：

- `position`
- `combat`
- `health`
- `status`
- `magic`
- `wallet`
- `quest`

這就是 Game-specific semantics。

同樣：

- CombatModule；
- MagicModule；
- QuestModule；
- InventoryModule；
- Dialogue；
- Room／Movement；
- player generation；
- game canon；
- HP / MP / FP；
- phase tier；

都不應直接被宣布為 Universal Core。

未來合理的邏輯形式應是：

$$
\boxed{
\text{Game World}
=
\text{General Runtime Core}
+
\text{Game Domain Pack}
}
$$

但這是一個未來抽取方向，不是現在要立刻重構完成的要求。

---

# 17. 目前 Repository 明確存在的結構缺口

## 17.1 單程序、單世界

目前仍是：

$$
\boxed{
\text{Single Process}
+
\text{Single World Instance}
}
$$

還沒有：

- account；
- multiplayer consistency；
- distributed lock；
- multi-runtime coordination。

---

## 17.2 階層狀態已有，但跨層 transition 尚未完整

現有架構文件已經定義：

$$
\mathcal M=
\{
M_{\mathrm{world}},
M_{\mathrm{region}},
M_{\mathrm{scene}},
M_{\mathrm{entity}},
M_{\mathrm{system}},
M_{\mathrm{action}}
\}
$$

但 Repository 也明確標記：

> world／region／scene 的初始階層狀態已進 State Store，跨層事件轉移規則留待後續。

這是 Game World-State Runtime v0.2 最重要的工作之一。

---

## 17.3 Read scope 與 Action authority 尚未全面強制

ModuleContract 已有 `read` 與 `write`。

但目前真正 enforce 的重點仍在 write。

後續必須補：

$$
\text{who may read what}
$$

以及：

$$
\text{who may propose which action}
$$

否則未來 AI／MCP／multi-agent 一接上，權限邊界會失去可信度。

---

## 17.4 Replay migration 尚未完成

Replay 可處理 committed Delta。

但：

$$
EventIR_{v1}
\rightarrow
Runtime_{v2}
$$

仍需要正式 migration registry。

---

## 17.5 Temporal model 還很簡單

Scheduler 有了，但尚未統一：

- 重複事件；
- 長期 workflow；
- interrupt；
- timeout；
- temporal condition；
- world calendar。

這些應在 Game Runtime 先驗證。

---

# 18. 後續演化正式分成三層

## Layer A：Game World-State Runtime

近期主線。

目的：

> 先把一個封閉、可驗證、authoritative 的遊戲世界狀態 Runtime 做完整。

允許持續發展：

- Combat；
- Quest；
- Magic；
- Dialogue；
- Game Time；
- NPC；
- Game-specific schema。

它不是暫時垃圾，也不會在通用化後被刪除。

---

## Layer B：General Runtime Candidate Core

從 Game Runtime 中逐步辨識：

- 跨機制共用；
- 不依賴遊戲語義；
- 在其他 Domain 仍能保持相同不變量；

的結構。

目前候選大致是：

$$
\boxed{
State
+
Entity
+
Action
+
Event
+
Time
+
Authority
+
Transition
+
History
+
Projection
}
$$

但「候選」不等於「先驗通用」。

真正的升格需要後續 Domain 重用證據。

---

## Layer C：Future Open-World Layer

這一層目前只定義邊界，不提前硬塞進 Game Kernel。

未來才處理：

- ObservationIR；
- Claim / Evidence；
- confidence；
- provenance；
- valid time；
- staleness；
- belief；
- external effect；
- acknowledgement；
- reconciliation；
- distributed state。

因此：

$$
\boxed{
\text{Open-World Semantics}
\not\subset
\text{Game v0.2 的立即必做項}
}
$$

---

# 19. 本系列第一批核心不變量

## I-1：Projection 不得反向成為世界真相

$$
\text{Projection}
\not\rightarrow
\text{Direct State Mutation}
$$

## I-2：AI 不能繞過 Kernel

$$
\text{AI}
\rightarrow
\text{ActionIR}
\rightarrow
\text{Kernel}
$$

AI 若是修改世界定義，則必須走：

$$
\text{AI Authored Diff}
\rightarrow
\text{Compiler}
\rightarrow
\text{Validation}
\rightarrow
\text{Runtime Package}
$$

## I-3：Memory 不等於 State

$$
\text{Memory}
\neq
\text{StateStore}
$$

## I-4：Module 透過 Event 協作，不直接互改內部狀態

$$
M_i
\rightarrow
E
\rightarrow
M_j
$$

## I-5：Pure Function 不等於 Transition

$$
\text{FunctionIR}
\neq
\text{State Mutation}
$$

## I-6：Game Runtime 必須持續可執行

$$
\boxed{
W_{\mathrm{game}}
\text{ 必須持續可執行、可測試、可回歸}
}
$$

通用化不得以破壞現有 Reference World 為代價。

---

# 20. 禁止事項

## 禁止 A：先建立巨大 Universal Ontology

目前沒有足夠跨 Domain 驗證，不應先定義：

- 所有人；
- 所有公司；
- 所有設備；
- 所有機器人；
- 所有市場；
- 所有天氣；

的統一 Schema。

## 禁止 B：為了通用化重寫已驗證 Kernel

除非實際 Domain 驗證證明某抽象錯誤，否則優先：

$$
\text{extract / wrap / adapt}
$$

而不是：

$$
\text{rewrite everything}
$$

## 禁止 C：AI 生成後直接熱安裝

任何動態生成至少必須經：

$$
\text{Syntax}
\rightarrow
\text{Schema}
\rightarrow
\text{Semantic Validation}
\rightarrow
\text{Authority}
\rightarrow
\text{Scenario}
\rightarrow
\text{Promotion}
$$

## 禁止 D：把 Game State 等同現實 Observation

遊戲現在可以假設：

$$
\text{State}=\text{Truth}
$$

未來現實世界不能直接沿用這個假設。

---

# 21. Game World-State Runtime v0.2 建議核心清單

之後重新啟動工程時，優先做：

1. Hierarchical cross-layer event transition
2. Transition priority / ambiguity diagnostics
3. Module read-scope enforcement
4. Action authority isolation
5. Temporal rule / scheduler extension
6. Replay migration registry
7. State / event / transition trace
8. SCC / cycle diagnostics
9. Scenario property tests
10. Reference-world regression suite

這一階段仍然是：

$$
\boxed{
\text{Game First}
}
$$

不是先做 Smart Home、Robot 或 Universal Runtime。

---

# 22. 驗證條件

## V-1：同一 StateStore 可承載不同 namespace

新增新型狀態不需要修改 Kernel 專門理解該 Domain。

## V-2：新 Module 只靠 Contract + Action + Delta + Event 即可接入

若每增加一個 Game Mechanism 都必須改 Kernel，表示核心仍不夠乾淨。

## V-3：拔掉 AI Adapter 後 Runtime 仍然可運作

這已是現有設計原則。

## V-4：拔掉 Web／CLI／MCP Projection 後 Runtime State 不受影響

Projection 不能成為真相來源。

## V-5：Snapshot／Replay 可重建世界狀態

未來加入 migration 後，還要能跨版本驗證。

## V-6：Game-specific 模組能被整體辨識

Combat／Magic／Quest 可以被視為 Game Domain Pack，而不污染 StateStore／ActionIR／EventIR 的抽象。

---

# 23. 結論

目前 CompilableWorld 最值得保留的不是某個 MUD 功能，而是它已形成：

$$
\boxed{
\text{Authoring}
\rightarrow
\text{Compile}
\rightarrow
\text{Action}
\rightarrow
\text{Module}
\rightarrow
\text{Delta}
\rightarrow
\text{Commit}
\rightarrow
\text{Event}
\rightarrow
\text{Projection}
}
$$

並配有：

$$
\text{State Version}
+
\text{Authority Boundary}
+
\text{Scheduler}
+
\text{Snapshot}
+
\text{Replay}
+
\text{Scenario}
+
\text{Memory Boundary}
+
\text{External Read Boundary}
$$

因此目前最準確的定位是：

$$
\boxed{
\text{Game World-State Runtime Prototype}
}
$$

而不是只把它理解成 MUD Engine。

但同時也不應提前宣告它已是通用世界狀態機。

更準確的說法是：

$$
\boxed{
\text{Game Runtime 已經形成 General World-State Runtime 的第一個可執行參考錨點。}
}
$$

下一篇將正式處理：

# 《可執行參考世界：以遊戲世界狀態機作為通用系統的虛擬錨點》

下一篇的核心問題包括：

- Reference World Anchor 是什麼；
- 為什麼 Game Runtime 不應在通用化後被淘汰；
- 如何把已驗證世界變成 Prototype Library；
- 怎麼讓 AI 未來「先抄、再改、最後才生成」；
- 如何讓非通用 Reference World 與 General Runtime 雙向共演化。

---

# Appendix A：Repository Grounding

本篇主要依據目前 repository 中以下實作／文件：

- `README.md` — CompilableWorld Runtime MVP v0.1.1
- `AGENTS.md`
- `src/compilableworld/kernel.py`
- `src/compilableworld/models.py`
- `docs/whitepapers/05-hierarchical-state-machine-mud.md`
- `docs/whitepapers/07-evennia-to-mssp-runtime.md`
- MSSP × RDR 階層狀態機整合提案
- `docs/whitepapers/09-compilableworld-studio-mssp-rdr-visual-world-ide-v0.1.md`
- 2026-07-15 commit `c9a33185ac7df5863e76995b0ebb097578e6be7e`
- 2026-07-15 commit `72334d7881749c78d323684e3ddbbc2b8aab86da`

本篇刻意沒有把尚未存在於 Repository 的 Observation／Belief／External Effect 機制寫成「已實作」。它們只屬於後續 Open-World Layer。
