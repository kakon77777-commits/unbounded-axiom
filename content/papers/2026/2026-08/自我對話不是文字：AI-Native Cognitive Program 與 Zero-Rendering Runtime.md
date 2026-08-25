# 自我對話不是文字：AI-Native Cognitive Program 與 Zero-Rendering Runtime
## ——從「自己跟自己說話」走向狀態化認知程式執行

**系列 03 / 06**

---

## 摘要

若 AI 能夠在可定址認知空間中辨識與選擇自己的認知動作，那麼下一個問題便不再是：

> AI 要怎麼生成一句新的 self-prompt？

而是：

> **AI 要如何執行一段由自己選擇、可中途重觀察、可修改、可停止的認知程式？**

本文提出 **AI-Native Cognitive Program Runtime** 的基礎模型，將 self-dialogue 重新定義為：

$$
\boxed{
\text{Self-Dialogue}
=
\text{Stateful Cognitive Program Execution}
}
$$

在此模型中，自然語言只是認知程式的一種 renderer，而非 self-dialogue 的必要本體。AI 可以在需要時使用自然語言與自己互動，也可以直接執行：

$$
[
VERIFY,
COUNTEREXAMPLE,
REFRAME,
STOP
]
$$

等 canonical cognitive program，而不必先生成：

> 「請重新檢查你的推理。」

本文進一步區分：

- **同步自我對話**：同一認知迴圈內觀察、選擇、執行與重觀察；
- **非同步自我對話**：認知事件跨時間、跨執行實例或跨 Agent/Controller 發生；
- **固定程式**：編譯後按既定 operator 序列執行；
- **可變程式**：每一步根據新狀態重新編譯或改寫；
- **Rendered Mode**：canonical cognition 先渲染成自然語言；
- **Zero-Rendering Mode**：canonical cognition 直接進入 Runtime；
- **Recursive Self-Call**：AI 的認知程序可以再呼叫其他認知程序；
- **No-Op / Stop / Defer / Idle**：不執行、停止與延後本身都是正式控制結果。

本文最終提出一個基本閉環：

$$
O_t
\rightarrow
S_t
\rightarrow
P_t
\rightarrow
\Omega_{t,1}
\rightarrow
S_{t,1}
\rightarrow
\Omega_{t,2}
\rightarrow
\dots
\rightarrow
S_{t+1},
$$

其中每個中間狀態都可以重新觸發：

$$
Observe
\rightarrow
Retrieve
\rightarrow
Compile
\rightarrow
Execute
\rightarrow
Audit.
$$

因此，真正 AI-native 的 self-dialogue 不一定是一串文字，而是一條可追蹤、可中斷、可改寫、可重播的認知執行軌跡。

---

# 1. 自我對話不應被預設為「兩個 AI 在聊天」

目前談到 self-dialogue 時，最常見的直覺形式是：

```text
AI-A：我認為答案是 X。
AI-B：你應該重新檢查。
AI-A：好，我重新檢查。
AI-B：還可以找反例。
```

這種方法具有可讀性，也容易利用現有 LLM。

但它並不是唯一可能的實作。

若：

$$
VERIFY
$$

本身已經是一個 canonical cognitive object，

而：

$$
COUNTEREXAMPLE
$$

也是，

那麼：

```text
AI-B：你應該重新檢查。
```

其實只是：

$$
Render(
VERIFY
).
$$

因此：

$$
\boxed{
\text{Dialogue Text}
\neq
\text{Dialogue Semantics}.
}
$$

更精確地說：

$$
\text{Self-Dialogue}
$$

真正需要的是：

> 前一個認知狀態，因為某個自我產生的控制動作，而導向下一個認知狀態。

---

# 2. Self-Dialogue 的最小形式

定義一個公開狀態：

$$
S_t.
$$

AI 自己產生認知動作：

$$
\Omega_t.
$$

執行後：

$$
S_{t+1}
=
\Omega_t(S_t).
$$

因此最小 self-dialogue 是：

$$
\boxed{
S_t
\rightarrow
\Omega_t
\rightarrow
S_{t+1}.
}
$$

它甚至不需要：

- 第二個人格；
- 第二個 Agent；
- 第二段自然語言；
- 顯式「對話」UI。

只要：

$$
\Omega_t
$$

是由 AI 根據自己的公開狀態產生或選擇，

便已經形成：

$$
\boxed{
\text{self-generated cognitive transition}.
}
$$

---

# 3. Cognitive Program：從單一算子到認知程序

一個 operator 通常不夠。

因此定義：

$$
P_t
=
[
\Omega_1,
\Omega_2,
\dots,
\Omega_n
].
$$

例如：

$$
P_t=
[
DECOMPOSE,
VERIFY,
COUNTEREXAMPLE,
STOP
].
$$

這表示：

1. 拆解目前問題；
2. 驗證各子結論；
3. 嘗試尋找反例；
4. 若完成或找到反例則停止。

本文稱：

$$
P_t
$$

為 **Cognitive Program**。

---

# 4. Program 不只是 operator list

若只是：

```json
[
  "VERIFY",
  "COUNTEREXAMPLE",
  "STOP"
]
```

仍然太弱。

真正 runtime program 至少需要：

$$
P=
(
Operators,
Parameters,
ControlFlow,
Budget,
Termination,
Permissions
).
$$

例如：

```json
{
  "program_id": "cp://session/184",
  "operators": [
    {
      "op": "VERIFY",
      "target": "claim://current",
      "method": "independent_route"
    },
    {
      "op": "COUNTEREXAMPLE",
      "target": "claim://current",
      "stop_if": "counterexample_found"
    }
  ],
  "budget": {
    "max_steps": 4,
    "max_tokens": 3000
  },
  "termination": [
    "verified",
    "counterexample_found",
    "budget_exhausted"
  ]
}
```

因此 cognitive program 比 prompt sequence 更接近一個真正的執行物件。

---

# 5. Fixed Program 與 Adaptive Program

認知程式可以分成兩類。

## 5.1 Fixed Program

一次編譯：

$$
S_t
\rightarrow
P_t.
$$

然後：

$$
P_t
=
[
\Omega_1,
\Omega_2,
\Omega_3
]
$$

依序跑完。

優點：

- 簡單；
- replay 容易；
- 成本可預估；
- 行為較可控。

缺點：

> 中間環境或認知狀態改變後，原本 program 可能已經不適用。

## 5.2 Adaptive Program

每一步之後重新觀察：

$$
S_t
\rightarrow
\Omega_1
\rightarrow
S_{t,1}.
$$

然後：

$$
S_{t,1}
\rightarrow
Compile
\rightarrow
P_{t,1}.
$$

所以：

$$
P_{t,1}
$$

可能與：

$$
P_t
$$

不同。

因此：

$$
\boxed{
\text{Cognitive Program}
}
$$

本身也可以是一個動態狀態。

---

# 6. Execute → Reobserve 是核心

一個真正 persistent self-dialogue loop 不應假設：

> 一次把所有想法想完。

更合理的是：

$$
Observe
\rightarrow
Act
\rightarrow
Reobserve.
$$

形式上：

$$
S_{t,k+1}
=
Observe(
Execute(
\Omega_{t,k},
S_{t,k}
)
).
$$

每個 operator 執行後，都應重新確認：

- 目標是否已完成？
- 新證據是否出現？
- 原本假設是否失效？
- 成本是否超出？
- 權限是否改變？
- 是否應停止？

因此：

$$
\boxed{
\text{Reobservation}
}
$$

不是附加功能，而是 runtime 的核心。

---

# 7. 同步 Self-Dialogue

同步 self-dialogue 可以表示為：

$$
S_t
\rightarrow
Controller
\rightarrow
\Omega_t
\rightarrow
Executor
\rightarrow
S_{t+1}.
$$

這些步驟發生在同一個 active loop 中。

例如：

```text
Draft
↓
Observe Draft
↓
Select VERIFY
↓
Execute VERIFY
↓
Rewrite
↓
Observe Again
```

其特徵是：

- 低延遲；
- 狀態緊密；
- 容易形成短迴圈；
- 適合單一工作記憶窗口。

---

# 8. 非同步 Self-Dialogue

非同步 self-dialogue 則可能是：

$$
S_t
\xrightarrow{emit}
Event_t
$$

之後：

$$
Event_t
\xrightarrow{\Delta t}
Controller
\rightarrow
\Omega
\rightarrow
S_{t+k}.
$$

例如：

> AI 今天形成一個未驗證假設。

三小時後另一個 background controller：

> 發現這個假設仍未驗證，觸發 VERIFY。

或者：

> 某項外部資料更新後，重新啟動先前被 DEFER 的 cognition。

因此：

$$
\boxed{
\text{Self-Dialogue}
}
$$

可以跨：

- 時間；
- session；
- context window；
- process；
- Agent instance；
- model instance。

這時 CTCL / ITR 會從可選功能變成必要基礎。

---

# 9. 同一個模型與不同模型都可以

Self-dialogue 並不要求：

$$
Model_A
\neq
Model_B.
$$

可以是：

$$
Model
\rightarrow
Observe
\rightarrow
Model
\rightarrow
Execute.
$$

也可以是：

$$
Worker
\rightarrow
Controller
\rightarrow
Worker.
$$

甚至：

$$
Model_A
\rightarrow
Model_B
\rightarrow
Model_C.
$$

真正不變的是：

$$
\boxed{
\text{cognitive role separation}.
}
$$

角色可以分離，而模型不一定要分離。

---

# 10. Role 不是 Persona

這裡也要區分：

$$
Role
\neq
Persona.
$$

例如：

```text
Observer
Controller
Executor
Auditor
```

是功能角色。

它們不需要各自模擬不同人格。

因此：

> 「批判者人格」

不是必要條件。

更 AI-native 的方式是：

```text
role = evaluator
operator = COUNTEREXAMPLE
```

---

# 11. Zero-Rendering Runtime

在傳統流程：

$$
CanonicalOperator
\rightarrow
NaturalLanguagePrompt
\rightarrow
Model.
$$

Zero-Rendering 模式則：

$$
CanonicalOperator
\rightarrow
Runtime.
$$

例如：

```json
{
  "op": "VERIFY",
  "target": "artifact://answer/17",
  "mode": "independent"
}
```

直接成為下一輪 model/runtime 的控制輸入。

因此：

$$
\boxed{
\text{Zero-Rendering}
=
\text{No mandatory natural-language projection}.
}
$$

這不是說模型完全不處理文字。

而是：

> cognitive control 的 canonical representation 不再依賴文字。

---

# 12. 何時仍需要自然語言？

Natural-language renderer 仍然非常重要。

至少有四個用途。

## 12.1 Human Interface

人類需要知道：

> AI 為什麼選了 VERIFY？

因此 render：

> 目前結論尚未被獨立驗證，因此進入驗證程序。

## 12.2 Compatibility

某些模型只能接受文字。

那麼：

$$
CognitiveProgram
\rightarrow
PromptRenderer
\rightarrow
LLM.
$$

## 12.3 Debugging

工程師查看：

```text
VERIFY → COUNTEREXAMPLE → STOP
```

可能仍不足以理解詳細理由。

因此需要 explanatory renderer。

## 12.4 Cross-System Transport

某些異質系統無法共享 canonical registry。

此時自然語言可作為 fallback interoperability layer。

所以：

$$
\boxed{
\text{Natural Language}
=
\text{Interface / Renderer / Fallback}
}
$$

而不是被完全移除。

---

# 13. 認知呼叫與 Tool Calling 可以統一

傳統 Agent 有：

```text
CALL web.search
CALL python.run
CALL file.read
```

未來可以加入：

```text
CALL cog.verify
CALL cog.reframe
CALL cog.counterexample
CALL cog.backtrack
```

於是：

$$
ActionSpace
=
ToolActions
\cup
CognitiveActions.
$$

AI 可以自己判斷：

> 下一步需要改變外部世界，還是先改變自己的認知流程？

這是一個非常重要的統一。

---

# 14. Self-Call：AI 呼叫自己

如果認知 operator 的 executor 仍然是一個模型，

那麼：

```text
CALL cog.verify(...)
```

實際可能解析成：

$$
Runtime
\rightarrow
ModelInvocation.
$$

因此 AI 表面上是：

> 呼叫 VERIFY。

底層則可能是：

> 再呼叫一次自己，但以 VERIFY semantics 執行。

所以：

$$
\boxed{
\text{Self-Call}
=
\text{Model re-entry under a self-selected cognitive contract}.
}
$$

這比：

> 再 prompt 自己一次。

精確得多。

---

# 15. Recursive Self-Call

認知 program 本身也可能再呼叫 cognition。

例如：

$$
VERIFY
$$

執行時發現：

> 需要先 DECOMPOSE。

因此：

$$
VERIFY
\rightarrow
DECOMPOSE
\rightarrow
VERIFY.
$$

這就是 recursion。

形式：

$$
\Omega_i
\rightarrow
P'
\rightarrow
\Omega_i.
$$

因此 Runtime 需要：

- recursion depth；
- call stack；
- budget inheritance；
- parent event；
- termination policy。

否則容易形成：

$$
\text{Self-Call Loop}
\rightarrow
\infty.
$$

---

# 16. Cognitive Call Stack

可以定義：

```text
ROOT
└── VERIFY
    ├── DECOMPOSE
    │   ├── COMPARE
    │   └── STOP
    └── VERIFY
```

每個 frame 至少保存：

```json
{
  "call_id": "...",
  "operator": "VERIFY",
  "parent_call_id": "...",
  "depth": 2,
  "input_state_ref": "...",
  "budget_remaining": 0.42
}
```

這樣未來：

$$
SelfDialogue
$$

可以被真正 replay。

---

# 17. Program Mutation

若中途狀態改變，program 可以被改寫。

原始：

$$
P_t=
[
VERIFY,
COUNTEREXAMPLE,
FORMALIZE
].
$$

執行 VERIFY 後發現 contradiction。

則：

$$
P_t'
=
[
BACKTRACK,
REFRAME
].
$$

因此需要：

$$
MutateProgram(
P_t,
S_{t,k}
)
\rightarrow
P_t'.
$$

這不是錯誤。

而是 adaptive cognition 的正常能力。

---

# 18. Program Mutation 也必須可追蹤

不可只留下：

```text
program changed
```

而應留下：

```json
{
  "old_program_ref": "...",
  "new_program_ref": "...",
  "trigger_state_ref": "...",
  "reason_code": "contradiction_detected"
}
```

否則長期 AI 之後只看到：

> 我改變了計畫。

卻不知道：

> 為什麼改。

---

# 19. STOP 是認知結果，不是失敗

STOP 應該是一個正式 control operator。

例如：

$$
STOP(
reason
).
$$

合法原因可能是：

$$
GoalSatisfied,
$$

$$
NoFurtherGain,
$$

$$
BudgetExhausted,
$$

$$
AuthorityBoundary,
$$

$$
UnsafeToContinue.
$$

因此：

$$
\boxed{
STOP
}
$$

是成功的 runtime transition。

---

# 20. DEFER 與 STOP 不同

STOP：

> 目前這條 cognition 結束。

DEFER：

> 目前暫停，但等待未來條件。

因此：

$$
DEFER
=
(
Reason,
WakeCondition
).
$$

例如：

```json
{
  "op": "DEFER",
  "reason": "insufficient_external_evidence",
  "wake_if": "new_dataset_available"
}
```

這會直接連到長期 persistent runtime。

---

# 21. NO-OP

NO-OP 代表：

> 有一個 cognition cycle 發生，但不需要改變任何狀態。

例如：

$$
NOOP
$$

可能是因為：

- 沒有新的 evidence；
- 所有 candidate operator utility 都不高；
- state 與上一輪一致。

形式：

$$
S_{t+1}=S_t.
$$

這個結果仍然應該被視為合法 decision。

---

# 22. IDLE

IDLE 比 NO-OP 更長期。

NO-OP：

> 這一輪不做 cognition。

IDLE：

> Runtime 進入等待態。

因此：

$$
IDLE
\rightarrow
WakeEvent.
$$

例如：

```text
new message
new file
timer reached
environment changed
contract changed
external event
```

這是長期 AI 不必一直消耗算力的必要能力。

---

# 23. 自我對話必須有 Budget

若 AI 可以：

$$
AI\rightarrow AI\rightarrow AI\rightarrow\cdots
$$

那麼最基本的安全條件就是：

$$
Budget<\infty.
$$

Budget 可以包含：

$$
B=
(
Tokens,
Calls,
Time,
Money,
Energy,
Depth
).
$$

每個 self-call：

$$
B_{t+1}
=
B_t
-
Cost(\Omega_t).
$$

若：

$$
B_t\le B_{\min},
$$

則：

$$
STOP
$$

或：

$$
ESCALATE.
$$

---

# 24. 認知效用

AI 不能只因為「有 operator 可用」就呼叫。

應估計：

$$
U(\Omega_i|S_t)
=
ExpectedGain
-
ExpectedCost
-
Risk.
$$

若：

$$
\max_i U(\Omega_i|S_t)\le0,
$$

合理結果是：

$$
NOOP
$$

或：

$$
IDLE.
$$

這直接避免：

> 無限 self-reflection。

---

# 25. 自我對話不是越多越好

這點已經被前面的神經實驗與 foundation-model pilot 同時提醒。

多一步 cognition：

$$
\not\Rightarrow
\text{better}.
$$

自由 self-review 甚至可能把正確答案改壞。

因此：

$$
\boxed{
\text{Self-Dialogue Quality}
\neq
\text{Self-Dialogue Length}.
}
$$

真正重要的是：

- cognition 是否匹配目前 state；
- operator 是否適當；
- controller 是否可靠；
- 是否有停止條件；
- 是否有必要繼續。

---

# 26. Cognitive Fidelity

如果 AI 選：

$$
VERIFY,
$$

但實際 execution 變成：

> 隨便再想一次，

那麼 addressable cognition 沒有意義。

因此需要：

$$
Fidelity(
RequestedOperator,
ExecutedBehavior
).
$$

這會成為未來重要 Gate。

例如：

$$
Fidelity>F_{\min}.
$$

否則應：

$$
fallback
$$

或：

$$
recompile.
$$

---

# 27. Renderer Fidelity

若：

$$
C
\rightarrow
Text(C)
$$

則也需要：

$$
Meaning(Text(C))
\approx
C.
$$

因此 natural-language renderer 不是隨便寫漂亮句子。

而是一個 semantic-preservation layer。

---

# 28. Zero-Rendering 的真正意義

Zero-rendering 不只是省 token。

它更重要的意義是：

$$
\boxed{
\text{把 cognition 從語言表達中解耦。}
}
$$

這使未來可能：

- 不同語言共享同一 cognition；
- 不同模型共享同一 operator；
- 不同 renderer 不改 execution；
- cognition 可以被編譯、版本化與驗證。

這才是 AI-native 的意義。

---

# 29. 觀察者、控制器與執行器

一個基本 Runtime 可以拆成：

$$
Observer
$$

$$
Controller
$$

$$
Executor.
$$

其中：

## Observer

$$
O_t
\rightarrow
S_t.
$$

## Controller

$$
S_t
\rightarrow
P_t.
$$

## Executor

$$
(P_t,S_t)
\rightarrow
O_{t+1}.
$$

這三者可以：

- 同模型；
- 不同模型；
- symbolic + model hybrid；
- local + remote hybrid。

---

# 30. Auditor 是第四個必要角色

真正長期 Runtime 還需要：

$$
Auditor.
$$

Auditor 不一定阻止 action。

它負責：

$$
Record(
State,
Program,
Decision,
Outcome
).
$$

因此：

$$
\boxed{
Observer
+
Controller
+
Executor
+
Auditor
}
$$

構成最小 persistent cognition runtime。

---

# 31. Audit 不等於保存 Chain-of-Thought

Audit 保存：

- 看到什麼公開狀態；
- 選了哪個 operator；
- 用了哪個版本；
- 做出什麼結果；
- 為何停止；
- 花了多少成本；
- 哪個 contract / goal 生效。

不需要保存：

> 模型所有隱藏推理 token。

因此：

$$
\boxed{
Auditability
\neq
Hidden-CoT Logging.
}
$$

---

# 32. CTCL 將提供時間因果錨點

若：

$$
CognitionCall_1
$$

與：

$$
CognitionCall_2
$$

跨 context window、跨 process 或跨數小時，

則單一 local sequence 已不足。

每個事件需要：

$$
TemporalCoordinate.
$$

因此：

$$
CognitiveEvent
=
(
Operator,
State,
Time,
Cause,
Outcome
).
$$

第 4 篇將專門處理：

$$
CTCL/ITR
$$

如何承接這個角色。

---

# 33. Self-Dialogue Runtime 的事件模型

一次完整 loop 可以產生：

```text
state.observed
cognition.affordances.retrieved
cognition.program.proposed
cognition.program.selected
cognition.call.started
cognition.call.completed
state.reobserved
cognition.program.mutated
decision.resolved
audit.recorded
```

因此：

$$
SelfDialogue
$$

不再只是 message list。

而是：

$$
\boxed{
\text{Cognitive Event Graph}.
}
$$

---

# 34. 事件可以是 DAG，而不是純序列

若兩個 cognition 平行：

$$
VERIFY
\parallel
COUNTEREXAMPLE,
$$

然後：

$$
COMPARE.
$$

則：

$$
E_1
\parallel
E_2
\rightarrow
E_3.
$$

因此：

$$
\boxed{
SelfDialogueHistory
}
$$

天然可能是一個 DAG。

這就是 CTCL-ITR topology 之後會真正重要的地方。

---

# 35. Self-Dialogue 與長期 Memory

認知 Runtime 不應把所有 event 都放進 context。

應該：

$$
EventHistory
\rightarrow
MemorySelection
\rightarrow
WorkingContext.
$$

但原始 event 仍保留在外部 ledger。

因此：

$$
\boxed{
WorkingContext
\neq
FullCognitiveHistory.
}
$$

這能避免 context compression 直接抹除決策來源。

---

# 36. 最小執行演算法

可以給出一個初步 Runtime：

```text
while active:

    observation = observe(environment, memory, commitments)
    state = encode(observation)

    affordances = retrieve(state)

    if no_positive_utility(affordances):
        idle_or_stop()
        break

    program = compile(state, affordances)

    for op in program:

        check_budget()
        check_authority()

        result = execute(op)

        record_event(op, result)

        state = reobserve()

        if termination_condition(state):
            stop()
            break

        if program_invalidated(state):
            program = recompile(state)
```

這就是 self-dialogue 的 AI-native 雛形。

---

# 37. 這與「永遠自己說話」完全不同

錯誤理解：

$$
AI
\rightarrow
Prompt
\rightarrow
AI
\rightarrow
Prompt
\rightarrow
AI
\rightarrow\cdots
$$

本文提出的是：

$$
\boxed{
State
\rightarrow
Decision
\rightarrow
Cognition
\rightarrow
State
}
$$

而：

$$
Prompt
$$

只是其中一種 transport。

---

# 38. 從 Self-Prompt 到 Self-Control

因此成熟後：

$$
SelfPrompt
$$

甚至只是：

$$
Renderer(
SelfControl
).
$$

真正核心是：

$$
\boxed{
SelfControl_t
=
Select(
CognitiveAction
\mid
State_t
).
}
$$

這是整條研究線應該保持的抽象層級。

---

# 39. 從 Self-Control 到 Self-Planning

一旦 AI 可以控制：

> 怎麼想，

下一步便能控制：

> 先想哪個問題。

也就是：

$$
Agenda
\rightarrow
CognitiveProgram.
$$

然後：

$$
CognitiveProgram
\rightarrow
Plan.
$$

所以 Self-Dialogue Runtime 是 Self-Planning 的底層執行器。

---

# 40. 從 Self-Planning 到 Self-Governance

再往後：

$$
Plan
$$

不能直接執行。

要先進：

$$
Governance.
$$

因此：

$$
Plan
\rightarrow
\{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE
\}.
$$

也就是認知 Runtime 最後必須能接受治理層 veto。

---

# 41. Runtime 不能凌駕 Contract

即使 cognition program 自己得出：

> 下一步最有效率的是刪除某份資料。

如果：

$$
Authority(delete)=0,
$$

則：

$$
EXECUTION=DENIED.
$$

所以：

$$
\boxed{
CognitiveAutonomy
\neq
ExecutionAuthority.
}
$$

這也是未來契約型 AI 的核心。

---

# 42. Self-Call 的真正終極形態

成熟後，AI 可能不再生成：

> 「現在我應該重新檢查。」

而只是：

```text
resolve cog://epistemic/verify@1
execute target=artifact://current
```

然後 Runtime：

$$
Resolve
\rightarrow
Authorize
\rightarrow
Execute
\rightarrow
Record.
$$

這才是真正：

$$
\boxed{
\text{AI calls its own cognition}.
}
$$

---

# 43. 下一階段的工程優先順序

本文完成後，真正工程應優先建立：

1. **Cognitive Program Schema**
2. **Runtime Call Stack**
3. **Observe / Reobserve Interface**
4. **Operator Executor Interface**
5. **Program Mutation**
6. **Stop / Defer / No-Op**
7. **Budget Guard**
8. **Zero-Rendering Adapter**
9. **Audit Event Emission**
10. **CTCL Event Hook**

而不是先寫更多 prompt template。

---

# 44. 驗證 Gate

## Gate A：Program Execution

同一 canonical program 是否能穩定重播？

## Gate B：Rendered vs Zero-Rendered

$$
Outcome_{Text}
\approx
Outcome_{Canonical}?
$$

## Gate C：Adaptive Recompile

狀態改變後重新編譯，是否優於固定 program？

## Gate D：Termination

AI 是否能正確 STOP，而不是無限 self-call？

## Gate E：No-Op

是否能在不需要 cognition 時選擇：

$$
NOOP?
$$

## Gate F：Async Resume

跨 session / context window 後，是否能根據 ledger 恢復未完成 cognition？

---

# 45. 核心命題

本文最終提出：

$$
\boxed{
\text{Self-Dialogue}
\neq
\text{Self-Talk}.
}
$$

更精確的是：

$$
\boxed{
\text{Self-Dialogue}
=
\text{Self-Selected Stateful Cognitive Transition}.
}
$$

若多步：

$$
\boxed{
\text{Self-Dialogue}
=
\text{Adaptive Cognitive Program Execution}.
}
$$

而自然語言：

$$
Text
$$

只是一種：

$$
Renderer.
$$

---

# 結論

從 AI 原生架構來看，「自己跟自己對話」不必等價於產生第二段文字再讀回去。

更基本的結構是：

$$
S_t
\rightarrow
\Omega_t
\rightarrow
S_{t+1}.
$$

當 $\Omega_t$ 是 AI 根據自己的公開狀態自行選擇的認知動作時，self-dialogue 已經成立。

多步情況則為：

$$
S_t
\rightarrow
P_t
\rightarrow
S_{t+1},
$$

其中：

$$
P_t=
[
\Omega_1,\dots,\Omega_n
].
$$

真正成熟的 Runtime 還需要：

$$
Observe
\rightarrow
Compile
\rightarrow
Execute
\rightarrow
Reobserve
\rightarrow
Mutate
\rightarrow
Audit.
$$

自然語言可以存在，也可以不存在。

因此：

$$
\boxed{
\text{Zero-Rendering}
}
$$

並不是把語言從 AI 中移除，而是讓：

> **認知控制不再必須經過語言才能存在。**

這一步將 Self-Prompt 從 prompt engineering 提升成：

$$
\boxed{
\text{Cognitive Runtime Engineering}.
}
$$

而一旦 AI 的認知事件可以持續跨時間、自行改寫、非同步恢復，下一個不可避免的問題就是：

> **當上下文已經壓縮、模型已經換掉、執行跨過數小時甚至數年後，我們如何證明「它當時為什麼做出那個決定」？**

因此下一篇將正式進入：

# 《時間因果自我史：CTCL-ITR、Decision Receipt 與上下文壓縮後的可追溯性》

核心將處理：

- reference time；
- interaction time；
- causal time；
- ledger time；
- Temporal Evidence Envelope；
- Decision Receipt；
- Decision-Time Knowledge Boundary；
- context compression event；
- contract / authority versioning；
- cognitive event DAG；
- 以及 AI 如何形成一條可恢復、可驗證、可治理的長期認知因果歷史。
