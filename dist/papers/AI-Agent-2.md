# 時空迴圈－切片動力學：面向 AI Agent 的反身圖論式系統控制理論

**Document ID:** TSGD-2026-v0.1  
**Title:** Temporal-Spatial Loop-Slice Dynamics  
**Chinese Title:** 時空迴圈－切片動力學  
**Subtitle:** A Reflexive Graph-Dynamical Control Theory for AI Agents, Program Analysis, and Long-Horizon Tool Runtime  
**Author:** Neo.K / EveMissLab  
**Status:** Theoretical Whitepaper / MD Paper Draft  
**Version:** v0.1  
**Date:** 2026  
**Relation to Previous Work:** Extends Temporal Loop Taxonomy into a spatial-slicing and reflexive graph-dynamical theory.  
**Target Domains:** AI Agent runtime, program analysis, EML/AST/CTS verification, local-first plugin runtime, workflow orchestration, long-horizon computation.

---

## 摘要

時間迴圈分類學指出：現代程式與 AI Agent 的困難不只是「如何重複」，而是如何在條件尚未成熟時保存狀態、釋放資源、等待未來、被事件喚醒並恢復任務。這使得「時間」從低階等待技巧，升級為控制流的一部分。

然而，只有時間維度仍不完整。實際的 AI Agent 在執行任務前，往往會先將問題空間切割成可處理的片段：檔案、模組、函式、AST 節點、測試案例、依賴子圖、UI 元件、語義區塊、權限範圍等。Agent 並不是直接在整個世界中行動，而是在被切割後的局部空間中推進、測試、修復、擴張或收斂。

因此，本文提出「時空迴圈－切片動力學」（Temporal-Spatial Loop-Slice Dynamics, TSGD）：一種面向 AI Agent、程式分析、長任務自動化與工具運行層的反身圖論式系統控制理論。

其核心命題是：

```text
Agent 不是單純的 action loop。
Agent 是在時空切片圖上持續行走、觀測、修正自身路徑的反身系統。
```

TSGD 將 Agent 任務形式化為：

```text
Task = <SpaceSlice, TemporalLoop, Goal, Policy, Feedback, GraphState>
```

其中：

1. **Temporal Loop** 描述任務如何在時間中推進、等待、重試、恢復、降級。
2. **Spatial Slice** 描述任務在哪個空間範圍中行動、觀測、修改、驗證。
3. **Graph State** 描述檔案、函式、AST、測試、依賴、概念與 Agent 狀態之間的關係。
4. **Reflexive Policy** 描述當任務失敗或假設錯誤時，Agent 如何修正自己的切片方式、時間策略與行動路徑。

本文認為，真正的 Agent runtime 不能只是一個迴圈，也不能只是一個工具調用器，而應是一個「反身時空圖動力系統」：它在圖上定位空間，在時間中推進任務，並在失敗時重構自身對問題的切割方式。

---

## 0. 導論：從時間迴圈到時空圖動力學

### 0.1 時間迴圈學的不足

時間迴圈分類學的核心是：

```text
persist state
suspend
wake
reload
validate
resume
timeout / degrade
```

它解決的是：

1. 何時等待。
2. 何時重試。
3. 何時恢復。
4. 何時超時。
5. 何時請人類決策。
6. 何時切換策略。
7. 如何避免 busy waiting。
8. 如何讓長任務跨時間片持續。

這對 AI Agent、工作流系統與程式運行層非常重要。

但在真實 Agent 任務中，另一個同樣關鍵的問題是：

```text
在哪裡行動？
在哪裡觀測？
在哪裡修改？
在哪裡測試？
在哪裡擴大範圍？
在哪裡停止？
```

這就是「空間切片」問題。

---

### 0.2 Agent 的實際工作方式：先切空間，再走迴圈

以程式碼修復任務為例，Agent 通常不會直接修改整個 repo，而是先做：

```text
repo
  → packages
  → files
  → functions
  → AST nodes
  → failing tests
  → error traces
  → minimal patch
```

以網站群維護為例：

```text
site network
  → single site
  → page
  → section
  → component
  → text block
  → metadata
```

以理論白皮書撰寫為例：

```text
theory corpus
  → document
  → section
  → definition
  → proposition
  → example
  → limitation
  → revision
```

這些都是空間切片。

因此，Agent 的真實結構不是：

```text
loop over actions
```

而是：

```text
select space slice
→ act within slice
→ observe result
→ update graph
→ decide whether to keep, shrink, expand, switch, or reflect
→ continue temporal loop
```

這就是本文要建立的理論基礎。

---

### 0.3 本文核心命題

本文提出三個核心命題：

#### 命題一：時間迴圈決定任務如何在時間中推進

```text
Temporal Loop = time-aware control trajectory
```

它回答：

```text
何時行動？
何時等待？
何時重試？
何時恢復？
何時停止？
```

#### 命題二：空間切片決定任務在哪個範圍中生效

```text
Spatial Slice = bounded action-observation field
```

它回答：

```text
在哪裡觀測？
在哪裡修改？
在哪裡驗證？
哪裡是局部？
哪裡是邊界？
哪裡需要擴張？
```

#### 命題三：反身圖動力學決定 Agent 如何修正自己的切片與迴圈策略

```text
Reflexive Graph Dynamics = self-updating task topology
```

它回答：

```text
如果原本切錯了怎麼辦？
如果重試無效怎麼辦？
如果錯誤不在當前檔案怎麼辦？
如果問題其實是依賴、測試、文件、語義或權限層怎麼辦？
```

---

## 1. 基本定義

### 1.1 系統圖

令一個任務系統在時間 `t` 的圖狀態為：

```text
G_t = (V_t, E_t, A_t, M_t)
```

其中：

```text
V_t = 節點集合
E_t = 邊集合
A_t = 節點與邊的屬性集合
M_t = metadata / memory / runtime state
```

在 Agent 工程中，節點可以是：

```text
file
module
function
class
AST node
test case
error trace
dependency
document section
UI component
API endpoint
plugin
tool
agent
human decision
runtime state
```

邊可以是：

```text
imports
calls
depends_on
fails_at
tested_by
generates
modifies
references
blocks
requires_approval
derived_from
contradicts
repairs
```

因此，Agent 面對的不是純文字，而是一個可持續更新的任務圖。

---

### 1.2 空間切片

空間切片定義為圖上的一個可行動子域：

```text
Σ_t ⊆ G_t
```

其中 `Σ_t` 是 Agent 在時間 `t` 選定的作用範圍。

例如：

```text
Σ_t = {parser.ts, parseSumExpression(), case-03-sum.eml, expected-output.py}
```

或者：

```text
Σ_t = dependency neighborhood of failing test case
```

空間切片不是單純的檔案集合，而是一個帶有任務語義的局部圖：

```text
SpaceSlice = <Center, Boundary, Nodes, Edges, Purpose, Risk, ExpansionPolicy>
```

---

### 1.3 時間迴圈

時間迴圈定義為任務在時間中的控制策略：

```text
Τ_t = <LoopType, Condition, WakeRule, ResumePolicy, TimeoutPolicy>
```

例如：

```json
{
  "loopType": "convergent",
  "condition": "parser tests pass",
  "maxAttempts": 8,
  "resumePolicy": "feed_diagnostics_back",
  "timeoutPolicy": "human_decision"
}
```

---

### 1.4 時空任務單位

一個完整 Agent 任務不是單純 prompt，而是：

```text
Ω_t = <G_t, Σ_t, Τ_t, Goal_t, Policy_t, Feedback_t>
```

其中：

```text
G_t = 系統圖
Σ_t = 當前空間切片
Τ_t = 當前時間迴圈
Goal_t = 任務目標
Policy_t = 權限、風險、擴張、終止策略
Feedback_t = 觀測與回饋
```

任務的演化為：

```text
Ω_t → Action_t → Observation_t → Ω_{t+1}
```

若任務順利，Agent 在同一切片內前向推進。

若任務失敗，Agent 可能觸發反身更新：

```text
Σ_t → Σ_{t+1}
Τ_t → Τ_{t+1}
Goal_t → Goal_{t+1}
Policy_t → Policy_{t+1}
```

---

## 2. 空間切片分類學

本文將空間切片分為十類。這些分類不是互斥的，而是可疊加、可轉換、可擴張的。

---

### 2.1 File Slice：檔案切片

#### 定義

以單一檔案或少數檔案為作用範圍。

```text
Σ = {file}
```

#### 例子

```text
packages/parser/src/parser.ts
README.md
eml-grammar.md
```

#### 適用場景

1. 小型 bug fix。
2. 文件修改。
3. 單檔 refactor。
4. 單檔語法錯誤修復。
5. 單一配置修正。

#### 優點

1. 範圍清楚。
2. 風險低。
3. 容易 diff。
4. 容易回滾。

#### 缺點

若錯誤根源不在該檔案，會導致 Agent 在錯誤空間內重試。

---

### 2.2 Module Slice：模組切片

#### 定義

以 package、module、folder 或子系統為範圍。

```text
Σ = module_subgraph(G)
```

#### 例子

```text
packages/parser
packages/transpiler-python
packages/cts-generator
packages/cli
```

#### 適用場景

1. 中型功能開發。
2. 模組內部一致性修正。
3. API 變更。
4. package-level 測試修復。
5. 模組重構。

#### 優點

比 file slice 更完整，可以處理跨檔問題。

#### 缺點

範圍較大，可能造成不必要修改。

---

### 2.3 Function Slice：函式切片

#### 定義

以函式、方法、類別成員或局部程式單元為範圍。

```text
Σ = {function_node + local dependencies}
```

#### 例子

```text
parseExpression()
emitPython()
normalizeSource()
generateCTS()
```

#### 適用場景

1. 精準 bug fix。
2. 單一算法改良。
3. 單一函式測試失敗。
4. 局部性能優化。

#### 優點

1. 高精度。
2. 修改小。
3. 容易驗證。

#### 缺點

可能忽略呼叫者、被呼叫者、資料流與副作用。

---

### 2.4 AST Slice：語法樹切片

#### 定義

以 AST node type 或 AST 子樹為切片。

```text
Σ = AST_subtree(node_type)
```

#### 例子

```text
AssignmentStatement
OverlayOperation
SumExpression
RangeExpression
MatrixExpression
ConditionalExpression
```

#### 適用場景

1. 程式語言開發。
2. transpiler 修復。
3. parser 修復。
4. EML / Python / TypeScript AST 轉換。
5. round-trip validator。

#### 優點

1. 不被檔案邊界限制。
2. 對語法轉譯非常精準。
3. 適合 Agent 進行結構化修改。
4. 可與 CTS / symbol table / diagnostics 結合。

#### 缺點

需要 parser 與 AST infrastructure。

---

### 2.5 Dependency Slice：依賴切片

#### 定義

以某個節點的依賴鄰域為切片。

```text
Σ = neighborhood(v, k)
```

其中 `v` 是中心節點，`k` 是圖距離。

#### 例子

```text
parseSumExpression()
  → calls parseExpression()
  → uses TokenType.Sigma
  → tested_by case-03-sum
```

#### 適用場景

1. 跨檔 bug。
2. dependency mismatch。
3. API 變更。
4. 呼叫鏈分析。
5. 測試失敗定位。

#### 優點

能捕捉「錯不在當前檔案」的問題。

#### 缺點

若依賴圖不準，會擴張過度。

---

### 2.6 Test Slice：測試切片

#### 定義

以失敗測試為中心，收集相關 fixture、expected output、source file、runtime trace 與目標程式碼。

```text
Σ = failing_test_centered_subgraph
```

#### 例子

```text
case-03-sum.eml
case-03-sum.expected.py
parser.ts
pythonEmitter.ts
runtime stdout
```

#### 適用場景

1. TDD。
2. Agent 修 bug。
3. regression repair。
4. golden test mismatch。
5. CI fail analysis。

#### 優點

1. 目標明確。
2. 可驗證。
3. 適合 convergent loop。

#### 缺點

若測試本身錯誤，Agent 可能修壞產品以迎合錯誤測試。

---

### 2.7 Runtime Slice：執行切片

#### 定義

以實際執行 trace、CLI pipeline、runtime path 為範圍。

```text
Σ = execution_trace_subgraph
```

#### 例子

```text
eml run sum.eml
  → normalize
  → parse
  → semantic analyze
  → emit Python
  → execute Python
  → stdout
```

#### 適用場景

1. CLI bug。
2. runtime error。
3. toolchain integration。
4. environment mismatch。
5. end-to-end demo。

#### 優點

最貼近真實使用路徑。

#### 缺點

可能較慢，且需要完整環境。

---

### 2.8 Semantic Slice：語義切片

#### 定義

以概念、語義、規則、理論單元為中心，而非檔案或函式。

```text
Σ = semantic_concept_subgraph
```

#### 例子

```text
時間迴圈
空間切片
x^+n 初始化 / 加法語義
CTS symbolTable
round-trip validator
human-decision loop
```

#### 適用場景

1. 白皮書。
2. 理論整理。
3. API design。
4. 語法規範。
5. 文件與程式同步。
6. Agent 生成規格。

#### 優點

適合處理跨文件、跨程式碼、跨設計層的問題。

#### 缺點

語義切片較抽象，需要良好命名與 metadata。

---

### 2.9 UI Slice：界面切片

#### 定義

以畫面、元件、互動流程或 UI region 為範圍。

```text
Σ = UI_component_subgraph
```

#### 例子

```text
Cogni-Editor EML input panel
Python output panel
AST viewer
diagnostics panel
approval modal
plugin permission page
```

#### 適用場景

1. 前端開發。
2. 使用者流程修復。
3. Agent UI automation。
4. demo polish。
5. approval workflow。

#### 優點

貼近使用者體驗。

#### 缺點

常需要視覺與狀態雙重驗證。

---

### 2.10 Governance Slice：治理 / 權限切片

#### 定義

以權限、風險、安全、審批、成本為範圍。

```text
Σ = governance_policy_subgraph
```

#### 例子

```text
workspace permission
shell allowlist
plugin install
API key access
human approval
cost limit
git push policy
```

#### 適用場景

1. LAPR。
2. Agent 插件系統。
3. 本地 daemon。
4. 高風險操作。
5. 安全審計。
6. 人類決策迴圈。

#### 優點

能降低 Agent 高風險操作。

#### 缺點

若過度嚴格，會降低自動化效率。

---

## 3. 時間迴圈與空間切片的耦合

### 3.1 為什麼不能只看時間

單純時間迴圈會說：

```text
重試直到測試通過。
```

但它沒有說：

```text
在哪個範圍內重試？
只改函式嗎？
可以改測試嗎？
可以改 parser 嗎？
可以改 lexer 嗎？
可以改語法規範嗎？
可以改 public API 嗎？
```

因此，如果沒有空間切片，時間迴圈容易變成盲目重試。

---

### 3.2 為什麼不能只看空間

單純空間切片會說：

```text
修改 parser.ts。
```

但它沒有說：

```text
要修幾次？
失敗後怎麼辦？
何時擴大範圍？
何時停止？
何時請人類？
何時認定不是 parser 的問題？
```

因此，如果沒有時間迴圈，空間切片會變成一次性定位，而不是持續系統。

---

### 3.3 時空耦合任務

一個完整任務應該同時包含：

```text
Space：在哪裡做
Time：怎麼推進
Goal：做到什麼
Policy：不能做什麼
Feedback：怎麼知道對錯
Reflexivity：錯了怎麼改自己的理解
```

可表示為：

```json
{
  "taskId": "fix_sum_parser",
  "space": {
    "sliceType": "test_slice",
    "center": "tests/fixtures/case-03-sum.eml",
    "scope": "local",
    "expansionPolicy": [
      "function_slice",
      "file_slice",
      "dependency_slice",
      "module_slice"
    ]
  },
  "time": {
    "loopType": "convergent",
    "condition": "case-03-sum passes",
    "maxAttempts": 5,
    "timeoutPolicy": "human_decision"
  },
  "feedback": {
    "forward": "run parser test",
    "reflexive": "if repeated failure, expand slice"
  }
}
```

---

## 4. 前向動力學

前向動力學描述 Agent 在既定切片與迴圈內如何推進。

```text
ForwardStep:
    observe(Σ_t)
    plan(Goal_t, Σ_t)
    act(Σ_t)
    validate(Feedback_t)
    update(G_t)
```

例如：

```text
觀測 parser 測試錯誤
→ 推測 parseSumExpression 有問題
→ 修改 parseSumExpression
→ 跑 case-03-sum
→ 測試通過
→ 更新任務圖
```

前向動力學適合：

1. 問題定位正確。
2. 切片範圍足夠。
3. 測試可信。
4. 目標明確。
5. Agent 有足夠工具。

前向動力學的風險是：若初始切片錯誤，Agent 會在錯誤範圍內反覆修補。

---

## 5. 反身動力學

### 5.1 反身性的定義

反身動力學描述 Agent 如何修正自己的任務模型。

不是只問：

```text
我下一步怎麼做？
```

而是問：

```text
我是不是切錯空間？
我是不是選錯 loop？
我是不是誤解目標？
我是不是缺少依賴？
我是不是應該停止自動修？
```

反身性使 Agent 不只是改變外部世界，也改變自身對任務圖的理解。

---

### 5.2 反身觸發條件

常見觸發條件：

1. 同一錯誤重複出現。
2. 修復造成新錯誤。
3. 測試錯誤與修改區域無關。
4. Agent 無法解釋失敗。
5. 工具輸出與預期不一致。
6. 依賴圖缺失。
7. 權限不足。
8. 成本超限。
9. 高風險操作即將發生。
10. 人類反饋指出方向錯誤。

---

### 5.3 反身操作

反身操作包括：

```text
expand_space_slice
shrink_space_slice
switch_slice_type
switch_loop_type
ask_human
create_diagnostic_report
rebuild_dependency_graph
switch_provider
reduce_goal_scope
pause_task
```

例如：

```text
Attempt 1：function slice
Attempt 2：function slice
Attempt 3：仍失敗 → expand to file slice
Attempt 4：仍失敗 → expand to dependency slice
Attempt 5：發現 lexer normalization 問題 → switch center
Attempt 6：修 lexer → tests pass
```

這不是普通 retry，而是反身空間重構。

---

### 5.4 反身圖更新

形式上：

```text
R: <G_t, Σ_t, Τ_t, Feedback_t> → <G_{t+1}, Σ_{t+1}, Τ_{t+1}>
```

其中 `R` 是反身更新算子。

它可以做：

```text
G_t        → 更新任務圖
Σ_t        → 改變空間切片
Τ_t        → 改變時間迴圈
Policy_t   → 改變風險策略
Goal_t     → 收窄或改寫目標
```

這是 TSGD 與普通 workflow 的核心差異。

---

## 6. 圖論式系統動力學

### 6.1 任務圖

Agent 任務可被視為一個持續更新的有向多重圖：

```text
G_t = (V_t, E_t)
```

節點：

```text
V = Files ∪ Functions ∪ ASTNodes ∪ Tests ∪ Errors ∪ Concepts ∪ Tools ∪ Agents ∪ Humans ∪ States
```

邊：

```text
E = imports ∪ calls ∪ tests ∪ fails ∪ modifies ∪ depends ∪ blocks ∪ approves ∪ derives ∪ repairs
```

這個圖不是靜態文件索引，而是任務過程中的動態狀態。

---

### 6.2 圖的時間演化

每個 action 都可能改變圖：

```text
G_t → G_{t+1}
```

例如：

1. 新增檔案。
2. 修改函式。
3. 測試從 fail 變 pass。
4. 新錯誤出現。
5. 依賴邊被發現。
6. 人類批准某個 patch。
7. Agent 標記某假設失效。
8. 空間切片擴張。

---

### 6.3 前向邊與反身邊

本文區分兩種邊。

#### 前向邊

描述外部任務推進：

```text
modifies
tests
calls
generates
depends_on
```

#### 反身邊

描述 Agent 對自身模型的修正：

```text
mislocalized
expanded_to
switched_from
hypothesis_invalidated
requires_human_decision
strategy_changed
```

例如：

```json
{
  "edge": "expanded_to",
  "from": "function_slice:parseSumExpression",
  "to": "dependency_slice:lexer+parser",
  "reason": "same test failed after 2 attempts"
}
```

這使系統能記錄：

```text
不只是做了什麼，也記錄為什麼改變做法。
```

---

### 6.4 反身圖動力學

當圖中包含 Agent 自己的任務狀態、切片策略與假設時，系統成為反身圖：

```text
Agent ∈ V_t
Strategy ∈ V_t
Hypothesis ∈ V_t
SlicePolicy ∈ V_t
LoopPolicy ∈ V_t
```

也就是說，圖不只表示外部世界，也表示 Agent 對世界的理解。

這可稱為：

```text
Reflexive Graph Dynamics
反身圖動力學
```

若再加入時間迴圈與空間切片，則得到：

```text
Reflexive Temporal-Spatial Graph Dynamics
反身時空圖動力學
```

---

## 7. TSGD 的任務執行流程

### 7.1 基本流程

```text
1. 建立任務圖 G_0
2. 選擇初始空間切片 Σ_0
3. 選擇時間迴圈 Τ_0
4. 執行前向步驟
5. 收集觀測與回饋
6. 若成功，完成或進入下一 milestone
7. 若失敗，判斷是否在同一切片重試
8. 若重複失敗，觸發反身更新
9. 更新圖、切片、迴圈或策略
10. 持續直到完成、降級、暫停或轉交人類
```

---

### 7.2 Pseudocode

```python
async def run_tsgd_task(task):
    G = build_initial_graph(task)
    space = select_initial_slice(G, task.goal)
    loop = select_temporal_loop(task)

    while True:
        observation = await observe(G, space)
        action = await plan_action(task.goal, space, observation)
        result = await act(action, space)

        G = update_graph(G, action, result)
        feedback = await validate(task, G, space, result)

        if feedback.success:
            return complete_task(task, G, feedback)

        if should_retry_same_slice(loop, feedback):
            loop = update_loop_state(loop, feedback)
            continue

        reflexive_update = reflect(task, G, space, loop, feedback)

        G = reflexive_update.graph
        space = reflexive_update.space
        loop = reflexive_update.loop

        if reflexive_update.requires_human:
            decision = await request_human_decision(task, G, space, feedback)
            if decision.reject:
                return cancel_task(task, decision)
            if decision.revise:
                task = apply_human_revision(task, decision)
```

---

## 8. 與 AI Agent Runtime 的關係

### 8.1 現代 Agent 的隱式 TSGD

即使沒有正式理論，現代 Agent 已經在做 TSGD 的部分行為：

1. 掃描 repo。
2. 選擇相關檔案。
3. 跑測試。
4. 根據錯誤回頭修改。
5. 若失敗，改看別的檔案。
6. 若高風險，請使用者確認。
7. 若上下文不足，要求更多資訊。

但這些多半是隱式的、靠 prompt 與模型推理維持。

TSGD 的目標是把這些行為顯式化、可記錄、可驗證、可控制。

---

### 8.2 Agent 任務應輸出 Space-Time Metadata

Agent 不應只輸出：

```text
我修改了 parser.ts。
```

而應輸出：

```json
{
  "spaceSlice": {
    "type": "function_slice",
    "center": "parseSumExpression",
    "boundary": ["parser.ts", "case-03-sum.eml"]
  },
  "temporalLoop": {
    "type": "convergent",
    "attempt": 2,
    "condition": "case-03-sum passes"
  },
  "reflexiveState": {
    "hypothesis": "sum parser handles range incorrectly",
    "confidence": 0.72,
    "nextIfFail": "expand to lexer normalization"
  }
}
```

這讓 runtime 能理解 Agent 的行動範圍與下一步策略。

---

### 8.3 對 Claude Code / Codex / 本地 Agent 的價值

若 LAPR 或類似系統支援 TSGD，Claude Code / Codex / 本地 Agent 可以被放進更穩定的控制結構中：

```text
AI Provider 負責生成與推理
Plugin Runtime 負責工具能力
Temporal Loop 負責長任務控制
Spatial Slice 負責作用範圍
Graph State 負責任務拓撲
Reflexive Policy 負責失敗後重構
```

這樣 Agent 的錯誤不再只是「模型錯了」，而可以被分類為：

1. 切片錯誤。
2. 迴圈策略錯誤。
3. 依賴圖缺失。
4. 測試錯誤。
5. 權限不足。
6. 目標不清。
7. 反身更新不足。

這使錯誤修復更有結構。

---

## 9. 與 EML / AST / CTS 的關係

### 9.1 EML 提供結構化語義層

EML 的價值不只是高密度語法，而是提供：

```text
source
→ AST
→ CTS
→ symbol table
→ cross reference
→ round-trip validator
```

這些都是空間切片的基礎。

例如：

```text
AST Slice = EML AST node subset
Semantic Slice = CTS concept subset
Dependency Slice = CTS crossRefTable neighborhood
Test Slice = fixture + expected output + related AST
```

因此，EML 可以成為 TSGD 的結構化 substrate。

---

### 9.2 CTS 作為圖資料

CTS 可以被視為任務圖的一種投影：

```json
{
  "symbolTable": [],
  "commentTable": [],
  "crossRefTable": [],
  "temporalLoopTable": [],
  "spaceSliceTable": []
}
```

若加入 TSGD，可以新增：

```json
{
  "spaceSliceTable": [
    {
      "id": "slice_sum_expression",
      "type": "ast_slice",
      "center": "SumExpression",
      "nodes": [
        "AST:SumExpression",
        "Function:parseSumExpression",
        "Test:case-03-sum"
      ],
      "edges": [
        ["Test:case-03-sum", "AST:SumExpression", "tests"],
        ["Function:parseSumExpression", "AST:SumExpression", "produces"]
      ],
      "risk": "medium"
    }
  ]
}
```

這讓 PHOSPHOR 或其他可視化工具能顯示 Agent 正在哪個空間切片中工作。

---

### 9.3 Round-trip Validator 作為反身回饋

Round-trip validator 可作為 TSGD 的 feedback source。

例如：

```text
EML → Python → EML
```

若結果不一致，可能表示：

1. 語法轉譯有損。
2. AST emit 錯誤。
3. Python subset 不可逆。
4. EML representation 不足。
5. 需要擴大切片到 semantic layer。

這可觸發反身更新：

```text
AST slice → semantic slice
convergent loop → human decision loop
```

---

## 10. 與 LAPR 的關係

LAPR 是本地優先 Agent 插件運行層。若加入 TSGD，Task Model 可升級為：

```json
{
  "taskId": "task_001",
  "title": "Fix EML parser golden tests",
  "workspace": "/path/to/EML",
  "provider": "claude-code",
  "plugin": "eml-dev-agent",
  "goal": "Fix parser tests without changing documented grammar.",
  "space": {
    "sliceType": "test_slice",
    "center": "case-03-sum",
    "boundary": {
      "include": [
        "tests/fixtures/case-03-sum.eml",
        "packages/parser/src/parser.ts",
        "packages/transpiler-python/src/pythonEmitter.ts"
      ],
      "exclude": [
        "docs/",
        "examples/experimental/"
      ]
    },
    "expansionPolicy": [
      "function_slice",
      "file_slice",
      "dependency_slice",
      "module_slice"
    ]
  },
  "time": {
    "loopType": "convergent",
    "condition": "pnpm test parser passes",
    "maxAttempts": 8,
    "timeoutPolicy": "human_decision"
  },
  "reflexivePolicy": {
    "onRepeatedFailure": "expand_space_slice",
    "onUnexpectedDiff": "request_human_review",
    "onPermissionRisk": "human_decision_loop",
    "onAmbiguousSemantics": "switch_to_semantic_slice"
  }
}
```

這樣 LAPR 就不是普通 task runner，而是具備時空圖控制能力的 Agent runtime。

---

## 11. 空間擴張與收縮策略

### 11.1 為什麼需要擴張

若 Agent 在過小切片內重試，會形成局部過擬合：

```text
一直修同一個函式
但錯誤其實在 lexer
```

因此需要擴張策略：

```text
function → file → dependency → module → runtime → semantic
```

---

### 11.2 為什麼需要收縮

若切片過大，Agent 會失去焦點：

```text
看完整 repo
改太多檔案
製造新 bug
```

因此需要收縮策略：

```text
module → dependency → file → function → AST node
```

---

### 11.3 擴張規則

```text
若同一錯誤重複 N 次：
    expand slice

若新錯誤出現在依賴模組：
    expand to dependency slice

若輸出與規格衝突：
    expand to semantic slice

若 CLI end-to-end 失敗：
    expand to runtime slice

若操作涉及權限：
    add governance slice
```

---

### 11.4 收縮規則

```text
若 failing test 已定位到單一函式：
    shrink to function slice

若 diff 過大：
    shrink boundary

若 Agent 修改非相關檔案：
    enforce slice boundary

若測試通過但變更太廣：
    request human review
```

---

## 12. TSGD 的錯誤分類

TSGD 可以將 Agent 失敗分成幾類。

### 12.1 Spatial Mislocalization：空間定位錯誤

Agent 選錯切片。

```text
以為是 parser 問題，其實是 lexer 問題。
```

處理：

```text
expand or switch slice
```

---

### 12.2 Temporal Strategy Error：時間策略錯誤

Agent 用錯 loop。

```text
需要 human decision，卻一直自動 retry。
```

處理：

```text
switch loop type
```

---

### 12.3 Graph Incompleteness：圖不完整

依賴、測試、引用或上下文缺失。

```text
不知道 parseExpression 被哪些測試依賴。
```

處理：

```text
rebuild graph / inspect dependencies
```

---

### 12.4 Feedback Misinterpretation：回饋誤讀

Agent 誤解錯誤訊息。

```text
把 expected output 錯看成 actual output。
```

處理：

```text
create diagnostic summary / compare structured outputs
```

---

### 12.5 Over-expansion：過度擴張

Agent 看太大範圍，造成不必要修改。

處理：

```text
shrink slice / enforce diff limit
```

---

### 12.6 Reflexive Failure：反身失敗

Agent 重複失敗但不改變策略。

處理：

```text
force reflection checkpoint
```

---

## 13. TSGD Runtime Metadata

TSGD runtime 可使用以下 metadata：

```json
{
  "taskId": "task_001",
  "graphState": {
    "version": 3,
    "nodes": [],
    "edges": []
  },
  "spaceSlice": {
    "id": "slice_001",
    "type": "test_slice",
    "center": "case-03-sum",
    "scope": "local",
    "nodes": [],
    "edges": [],
    "risk": "medium",
    "expansionLevel": 1
  },
  "temporalLoop": {
    "type": "convergent",
    "attempt": 2,
    "maxAttempts": 8,
    "condition": "test_passed",
    "timeoutPolicy": "human_decision"
  },
  "reflexiveState": {
    "currentHypothesis": "SumExpression parsing error",
    "failedHypotheses": [],
    "nextIfFail": "expand_to_dependency_slice",
    "requiresHuman": false
  }
}
```

---

## 14. TSGD 與人類協作

TSGD 並不排除人類，反而明確定義人類介入點。

人類應在以下情況介入：

1. 空間切片多次擴張仍失敗。
2. 語義切片存在爭議。
3. 修改高風險。
4. 測試與規格衝突。
5. Agent 不確定是否要改 public API。
6. 權限或安全操作。
7. 成本超限。
8. 產品方向選擇。

此時系統進入：

```text
Human-Decision Loop + Governance Slice
```

例如：

```json
{
  "loopType": "human_decision",
  "spaceSlice": {
    "type": "governance_slice",
    "center": "public API change"
  },
  "question": "Agent proposes changing EML grammar. Approve?"
}
```

這使人類不再只是最後驗收者，而是系統圖中的決策節點。

---

## 15. 應用場景

### 15.1 AI 程式修復

```text
Failing test
→ test slice
→ convergent loop
→ patch
→ test
→ if fail, expand dependency slice
→ if high-risk, human decision
```

---

### 15.2 中小型專案轉譯

```text
Source repo
→ module slices
→ AST slices
→ semantic slices
→ target emit
→ round-trip validation
→ convergent repair
```

---

### 15.3 EML 工具鏈開發

```text
EML grammar
→ AST slice
→ transpiler slice
→ CTS slice
→ runtime slice
→ Cogni-Editor UI slice
```

---

### 15.4 網站群維護

```text
site network
→ site slice
→ page slice
→ component slice
→ metadata slice
→ SEO / AI crawler feedback loop
```

---

### 15.5 本地 Agent 插件系統

```text
plugin manifest
→ permission slice
→ provider slice
→ task loop
→ event graph
→ approval loop
```

---

### 15.6 理論白皮書生成

```text
theory corpus
→ concept slice
→ definition slice
→ proposition slice
→ critique slice
→ revision loop
```

---

## 16. 與傳統理論的關係

TSGD 與以下概念有關，但不等同：

1. Program slicing。
2. Graph theory。
3. Control flow analysis。
4. Data flow analysis。
5. Workflow orchestration。
6. Cybernetics。
7. Feedback control。
8. Agent loop。
9. State machine。
10. Actor model。
11. Task planning。
12. Reflective systems。

TSGD 的獨特性在於將以下三者合併：

```text
Temporal loop
+ Spatial slice
+ Reflexive graph update
```

其重點不是單純分析程式，也不是單純控制流程，而是描述 AI Agent 如何在任務圖中持續定位、行動、驗證與自我修正。

---

## 17. 最小工程實作

### 17.1 MVP 支援

第一版只需要支援：

```text
Space Slice:
    file_slice
    test_slice
    function_slice
    dependency_slice

Temporal Loop:
    convergent
    human_decision
    timeout_degradation

Reflexive Policy:
    expand_space_slice
    ask_human
    create_report
```

---

### 17.2 MVP Task Runner

```python
class TSGDRunner:
    async def run(self, task):
        graph = await self.build_graph(task.workspace)
        space = await self.select_initial_slice(graph, task)
        loop = task.loop

        while True:
            result = await self.agent.act(task, graph, space)
            feedback = await self.validate(task, result)

            graph = await self.update_graph(graph, result, feedback)

            if feedback.success:
                return await self.complete(task, graph)

            if loop.can_retry_same_slice(feedback):
                loop.record_failure(feedback)
                continue

            update = await self.reflect(task, graph, space, loop, feedback)
            space = update.space
            loop = update.loop

            if update.requires_human:
                decision = await self.ask_human(task, graph, space, feedback)
                if decision.cancel:
                    return await self.cancel(task)
```

---

### 17.3 TypeScript Interface

```ts
export interface SpaceSlice {
  id: string;
  type:
    | "file_slice"
    | "module_slice"
    | "function_slice"
    | "ast_slice"
    | "dependency_slice"
    | "test_slice"
    | "runtime_slice"
    | "semantic_slice"
    | "ui_slice"
    | "governance_slice";

  center: string;
  nodes: string[];
  edges?: [string, string, string][];
  scope: "local" | "module" | "global";
  risk: "low" | "medium" | "high";
  expansionLevel: number;
}

export interface TemporalLoopState {
  type:
    | "convergent"
    | "human_decision"
    | "timeout_degradation"
    | "inter_agent_coordination"
    | "long_horizon_task"
    | "spiral_progress"
    | "evolutionary_decision";

  attempt: number;
  maxAttempts?: number;
  condition: string;
  timeoutPolicy?: string;
}

export interface ReflexivePolicy {
  onRepeatedFailure?: "expand_space_slice" | "ask_human" | "create_report";
  onUnexpectedDiff?: "shrink_space_slice" | "human_review";
  onAmbiguousSemantics?: "switch_to_semantic_slice";
  onPermissionRisk?: "human_decision_loop";
}

export interface TSGDTask {
  taskId: string;
  goal: string;
  workspace: string;
  space: SpaceSlice;
  time: TemporalLoopState;
  reflexivePolicy: ReflexivePolicy;
}
```

---

## 18. 設計原則

### 18.1 顯式化

Agent 的切片、迴圈、假設與反身策略都應顯式記錄。

### 18.2 局部優先

先在小切片內行動，再逐步擴張。

### 18.3 可觀測

每次切片變化、loop attempt、反身更新都應輸出事件。

### 18.4 可回滾

每次 action 應保留 diff / state snapshot。

### 18.5 可轉交

當 Agent 無法可靠決策，應進入 human-decision loop。

### 18.6 可組合

空間切片與時間迴圈應可自由組合。

### 18.7 反身節制

反身不是無限懷疑，而是在明確觸發條件下改變策略。

---

## 19. 限制與風險

### 19.1 圖構建成本

完整任務圖可能成本高。MVP 應從局部圖開始。

### 19.2 切片錯誤

如果 initial slice 錯誤，Agent 會走錯方向。需依靠反身策略修正。

### 19.3 過度理論化

TSGD 若直接全量實作會太重。工程上應先做 metadata 與 runtime policy。

### 19.4 Agent 解釋不可靠

Agent 對自己切片理由的解釋可能不完全可靠。需結合測試與圖證據。

### 19.5 人類決策瓶頸

過多 human-decision loop 會降低自動化效率。需要風險分級。

---

## 20. 路線圖

### v0.1：理論與 metadata

1. 定義 SpaceSlice。
2. 定義 TemporalLoopState。
3. 定義 ReflexivePolicy。
4. 定義 TSGDTask。
5. 在 LAPR task model 中加入 space/time/reflexive metadata。

### v0.2：局部工程實作

1. file_slice。
2. function_slice。
3. test_slice。
4. dependency_slice。
5. convergent loop。
6. human-decision loop。
7. repeated failure → expand slice。

### v0.3：EML / CTS 整合

1. AST slice。
2. semantic slice。
3. CTS spaceSliceTable。
4. round-trip feedback。
5. PHOSPHOR visualization。

### v0.4：反身圖 runtime

1. graph state store。
2. graph event log。
3. failed hypothesis tracking。
4. slice expansion history。
5. loop switch history。

### v0.5：多 Agent 系統

1. agent node。
2. inter-agent coordination loop。
3. task dependency graph。
4. agent role slice。
5. cross-agent handoff。

---

## 21. 結論

時間迴圈分類學說明了 Agent 如何在時間中等待、重試、恢復與演化。

但真實 Agent 不只在時間中行走，也在空間中切片。

Agent 需要知道：

```text
在哪裡看？
在哪裡改？
在哪裡測？
在哪裡等待？
在哪裡重試？
失敗時要不要擴大空間？
要不要換切片？
要不要換 loop？
要不要請人類？
```

因此，本文提出「時空迴圈－切片動力學」：

```text
Temporal Loop
+ Spatial Slice
+ Reflexive Graph Dynamics
= Temporal-Spatial Loop-Slice Dynamics
```

其核心結論是：

```text
Agent 不是單純的 action loop。
Agent 是在時空切片圖上持續行走、觀測、修正自身路徑的反身系統。
```

這套理論可作為 AI Agent runtime、LAPR、本地插件系統、EML/AST/CTS 驗證、PHOSPHOR 可視化、程式轉譯、長任務自動化與多 Agent 協作的通用控制模型。

若時間迴圈處理「尚未成熟的未來」，那麼空間切片處理「尚未定位的世界」。

而 TSGD 處理的是：

```text
一個 Agent 如何在尚未完全定位的世界中，
跨時間推進任務，
並在失敗時反身修正自己的定位方式。
```

這才是面向 AI Agent 時代的圖論式系統動力學。
