# 時間迴圈分類學：一種面向長時程程式、AI Agent 與人機協作的通用控制流理論

**Document ID:** TLC-2026-v0.1  
**Title:** Temporal Loop Taxonomy  
**Subtitle:** A General Theory of Time-Aware Control Flow for Programming Languages, AI Agents, Workflow Systems, and Long-Horizon Computation  
**Author:** Neo.K / EveMissLab  
**Status:** Public Theory Draft  
**Relation to EML:** Originated from EML Ultimate, but not exclusive to EML.  
**License Suggestion:** CC BY 4.0 / Open theoretical release

---

## 摘要

時間迴圈分類學不是某一種程式語言的專屬語法，而是一套重新理解程式控制流的通用理論。

傳統程式語言將迴圈主要理解為「重複執行」：

```text
for / while / do-while
```

但現代軟體系統、AI Agent、工作流引擎、部署系統、排程系統與人機協作任務中，許多迴圈的本質已不只是重複，而是：

```text
等待條件成熟
保存狀態
釋放資源
延遲決策
外部事件喚醒
跨時間片恢復
```

這類迴圈可稱為「時間迴圈」。

時間迴圈的核心不在於程式是否重複執行，而在於程式是否能將「時間」視為控制流的一部分。

本文件提出時間迴圈分類學，將現代程式中常見的等待、排程、事件喚醒、人類決策、多 Agent 協作、超時降級、長時程任務等結構統一為一組可命名、可標註、可實作、可觀測的控制流類型。

---

## 1. 問題：傳統迴圈分類不足

傳統程式語言通常只提供幾種表面迴圈形式：

```python
for item in items:
    process(item)

while condition:
    update()
```

這些語法足以描述重複，但不足以描述時間語義。

同樣寫成 `while`，實際語義可能完全不同：

```python
# 普通重複
while i < n:
    i += 1

# 收斂求解
while error > epsilon:
    optimize()

# 事件監聽
while True:
    event = queue.get()
    handle(event)

# 重試
while retry_count < max_retry:
    try_request()

# 等待人類確認
while not user_confirmed:
    sleep(60)

# 等待外部條件成熟
while not deployment_window_open:
    suspend_until(next_window)
```

這些迴圈在表面語法上相似，但在工程語義上完全不同：

1. 終止條件不同。
2. 時間關係不同。
3. 是否佔用資源不同。
4. 是否需要保存狀態不同。
5. 是否依賴外部事件不同。
6. 是否需要人類決策不同。
7. 是否可以被中斷、恢復、遷移不同。
8. 錯誤處理策略不同。

因此，傳統 `for / while` 是語法分類，不是語義分類。時間迴圈分類學的目的，是將「迴圈的時間語義」顯式化。

---

## 2. 基本命題

### 命題 1：迴圈不只是重複，而是狀態在時間中的軌跡生成器

傳統觀點：

```text
Loop = repeat(body) until condition
```

時間迴圈觀點：

```text
Loop = evolve(state, time, condition, event, policy)
```

也就是說，迴圈不是單純執行同一段程式，而是讓狀態沿著某種規則在時間中演化。

### 命題 2：等待不是空白，而是一種控制流狀態

傳統程式常把等待寫成：

```python
while not ready():
    time.sleep(60)
```

但這只是低階技巧。真正的等待應被視為一種顯式控制流：

```text
Suspend(state, wake_rule, resume_policy)
```

等待不是沒有執行，而是程式進入「時間懸置狀態」。

### 命題 3：時間迴圈的核心不是 sleep，而是 stateful suspend/resume

`sleep()` 只表示「暫停一段時間」。

時間迴圈表示：

```text
保存狀態
釋放資源
註冊喚醒條件
等待時間或事件
恢復狀態
重新驗證
繼續執行
```

所以時間迴圈不是 sleep 的同義詞，而是一種完整的時間化控制流協議。

---

## 3. 時間迴圈的形式定義

令：

```text
S_t = 程式在時間 t 的狀態
E_t = 外部事件集合
T_t = 時間上下文
Φ(S_t, E_t, T_t) = 條件判定函數
Π = 恢復策略 / 執行策略
```

則時間迴圈可定義為：

```text
TemporalLoop(S_t) =
    Proceed(S_t, Π)                 if Φ(S_t, E_t, T_t) = True
    Suspend(S_t, WakeRule, Π)       if Φ(S_t, E_t, T_t) = False
```

其中 `Suspend` 不是終止，而是進入可恢復狀態：

```text
Suspend(S_t, WakeRule, Π):
    snapshot = persist(S_t)
    release_resources()
    register(WakeRule)
    wait_until(wake)
    S_t' = restore(snapshot)
    validate(S_t')
    resume(S_t', Π)
```

### 最小五元組

一個完整時間迴圈至少包含：

```text
TemporalLoop = <State, Condition, TimeRule, WakeTrigger, ResumePolicy>
```

對應：

1. **State**：目前任務狀態。
2. **Condition**：什麼情況可以繼續。
3. **TimeRule**：何時重新檢查。
4. **WakeTrigger**：誰喚醒。
5. **ResumePolicy**：醒來後怎麼接續。

---

## 4. 時間迴圈與普通迴圈

| 類型 | 普通迴圈 | 時間迴圈 |
|---|---|---|
| 核心 | 重複執行 | 跨時間保持控制流 |
| 條件 | 多為內部條件 | 常依賴外部條件 |
| 資源 | 可能持續佔用 | 可釋放資源 |
| 狀態 | 通常在記憶體中 | 需要可保存 / 可恢復 |
| 等待 | blocking / sleep / busy waiting | suspend / schedule / event wake |
| 錯誤處理 | exception / break | timeout / degrade / escalate / reschedule |
| 適用場景 | 短時程計算 | 長時程任務、人機協作、Agent 工作流 |

一句話：

```text
普通迴圈處理「重複」。
時間迴圈處理「尚未成熟的未來」。
```

---

## 5. 時間迴圈分類學

時間迴圈可以依照「等待原因」與「喚醒方式」分類。

### 5.1 Delay Loop：延遲時間迴圈

在固定時間後恢復。

```text
Suspend(state, wake_at = now + Δt)
```

適用場景：API rate limit、重試冷卻、定時檢查、排程任務、暫緩執行。

這是最簡單的時間迴圈，只依賴時間，不依賴複雜外部事件。

---

### 5.2 Condition-Maturation Loop：條件成熟迴圈

等待某個條件成熟。

```text
while not condition():
    suspend()
resume()
```

適用場景：等測試環境可用、等資料同步完成、等檔案生成、等服務恢復、等市場資料更新。

條件不是程式立刻可改變的，只能等待外部世界演化。

---

### 5.3 Event-Wakeup Loop：事件喚醒迴圈

不是定時檢查，而是由事件喚醒。

```text
Suspend(state, wake_on = event)
```

適用場景：Webhook、Message queue、File watcher、Database trigger、IoT sensor、GitHub action event、Slack / Gmail / Calendar event。

事件喚醒迴圈比輪詢更節省資源，也更符合分散式系統的自然形態。

---

### 5.4 Human-Decision Loop：人類決策迴圈

等待人類判斷、批准、拒絕或補充資訊。

```text
Suspend(state, waiting_for = human_decision)
```

適用場景：部署確認、高風險刪除、財務付款、法律審核、內容發布、Agent 不確定時請人類選路。

人類決策迴圈是 AI Agent 最重要的時間迴圈之一。它不是失敗，也不是中斷，而是明確承認：

```text
此處需要外部主體決策。
```

---

### 5.5 Inter-Agent Coordination Loop：多 Agent 協作迴圈

等待其他 Agent 完成子任務。

```text
Suspend(state, waiting_for = agent_B.done)
```

適用場景：多 Agent 軟體開發、文件生成、測試修復、分散式規劃、Pipeline orchestration。

這類迴圈需要明確的任務狀態、完成訊號、失敗訊號與重試規則。

---

### 5.6 Timeout-Degradation Loop：超時降級迴圈

等待條件成熟，但若超過期限，就啟動降級策略。

```text
wait until condition or timeout
if timeout:
    degrade()
```

適用場景：外部 API 不穩、等人工回覆但逾時、等部署窗口但錯過時間、等模型輸出但太久、Agent 卡住時轉交人工。

這是工程上最實用的時間迴圈之一，因為它避免系統無限等待。

---

### 5.7 Periodic Inspection Loop：週期巡檢迴圈

定期醒來檢查狀態，但不是持續工作。

```text
Every Δt:
    wake
    inspect
    sleep
```

適用場景：系統健康檢查、定期備份、定期爬取、資料同步、Agent 定期回顧任務狀態。

它和普通永恆迴圈不同，因為重點不是持續執行，而是週期性醒來。

---

### 5.8 Long-Horizon Task Loop：長時程任務迴圈

任務跨越多個時間片，每次只推進一部分。

```text
state_t → partial progress → suspend → resume later
```

適用場景：長期研究、大型軟體開發、AI Agent 長任務、自動化營運、多日資料處理。

這類迴圈不是一次執行完，而是把任務切成時間片。

---

### 5.9 Evolutionary Decision Loop：演化選路迴圈

等待多個候選路徑產生結果，再選擇下一步。

```text
explore candidates
wait for evaluations
select best path
continue
```

適用場景：A/B testing、多方案設計、模型超參數搜索、Agent 多路徑探索、產品策略選擇。

這類迴圈與普通時間迴圈不同，因為它等待的不是單一條件，而是多條路徑的結果。

---

### 5.10 Spiral Progress Loop：螺旋推進迴圈

方向已知，但每一輪推進都需要時間、檢查與修正。

```text
v0.1 → v0.2 → v0.3 → v1.0
```

適用場景：產品開發、技術路線圖、研究計畫、書籍寫作、系統迭代。

它不是隨機探索，而是沿著已知方向逐步逼近。

---

## 6. 螺旋迴圈與演化迴圈的核心差異

螺旋迴圈與演化迴圈都涉及「變化」，但差異非常重要。

| 維度 | 螺旋推進迴圈 | 演化選路迴圈 |
|---|---|---|
| 路徑 | 大致確定 | 多路徑不確定 |
| 目標 | 已知方向 | 需要探索 |
| 判定 | checkpoint / milestone | evaluation / selection |
| 風險 | 執行偏差 | 選路錯誤 |
| Agent 行為 | 按 roadmap 推進 | 生成候選、比較、選擇 |
| 例子 | MVP → v0.2 → v0.3 | 選 parser 架構 / 選產品方向 |

對 AI Agent 來說，這個差異尤其重要：

```text
明明是演化問題，Agent 不該假裝路線已經確定。
明明是螺旋問題，Agent 不該一直發散 brainstorming。
```

這是時間迴圈分類學對 Agent 工程的直接價值。

---

## 7. 為什麼這套分類有用？

### 7.1 它把低階技巧提升為高階控制流

現有工程裡，等待常被拆散到：

1. `sleep`
2. callback
3. cron
4. queue
5. webhook
6. state machine
7. workflow engine
8. manual approval
9. retry policy

時間迴圈分類學將這些結構統一為：

```text
不同喚醒條件與恢復策略下的時間化迴圈。
```

這不取代現有工具，而是給它們一套共同語義。

### 7.2 它讓 runtime 可以自動選策略

一旦 loop type 被標記，runtime 就知道該做什麼：

| loop type | runtime policy |
|---|---|
| delay | timer，不 busy wait |
| condition-maturation | periodic check + state persistence |
| event-wakeup | event subscription |
| human-decision | approval request + escalation |
| inter-agent | task dependency tracking |
| timeout-degradation | timeout + fallback |
| periodic-inspection | scheduled wake |
| evolutionary-decision | candidate collection + evaluation |
| spiral-progress | milestone checkpoint |

### 7.3 它讓 AI Agent 更穩定

Agent 常見錯誤是把所有 loop 都當成 retry。時間迴圈分類可以讓 Agent 明確知道：

```text
這不是 retry。
這是 human-decision loop。

這不是 ordinary while。
這是 timeout-degradation loop。

這不是 event loop。
這是 event-wakeup temporal loop。
```

這會直接改善長任務、工具使用、人機協作與多 Agent 編排。

### 7.4 它讓程式語言與工作流系統可以共享語彙

同一套分類可用於 Python asyncio、TypeScript Promise / workflow、Go goroutine + channel、Rust async、Java / Kotlin coroutine、Airflow / Prefect / Temporal.io 類工作流、CI/CD pipeline、Agent runtime、EML / Py⁺、PHOSPHOR 可視化執行層。

---

## 8. 最小 metadata schema

任何語言都可以用 metadata 表達時間迴圈：

```json
{
  "loopId": "deploy_approval_loop",
  "loopType": "human_decision",
  "statePersistence": true,
  "condition": "user_confirmed == true",
  "wakeTrigger": "approval_event",
  "checkInterval": 60,
  "maxWait": 3600,
  "timeoutPolicy": "escalate",
  "resourcePolicy": "suspend_not_busy_wait",
  "resumePolicy": "reload_validate_continue"
}
```

這個 schema 比語法本身更重要，因為它能被 runtime、Agent、IDE、觀測系統共同理解。

---

## 9. 最小程式接口

### Python

```python
@temporal_loop(
    type="human_decision",
    condition=check_user_confirmed,
    max_wait=3600,
    check_interval=60,
    timeout_policy="escalate",
    persistence=True,
)
async def deploy_task(state):
    deploy(state["version"])
```

### TypeScript

```ts
await temporalLoop({
  type: "event_wakeup",
  condition: () => paymentCompleted(orderId),
  wakeOn: ["webhook:payment.completed"],
  maxWait: "24h",
  persistence: true,
  resume: async (state) => shipOrder(state.orderId),
});
```

### Agent metadata

```json
{
  "task": "deploy_v1_2",
  "loopType": "human_decision",
  "waitingFor": "approval",
  "state": {
    "compiled": true,
    "testsPassed": true
  },
  "resumeAction": "deploy",
  "timeoutPolicy": "ask_again_or_cancel"
}
```

---

## 10. 與 EML 的關係

時間迴圈分類學源自 EML Ultimate 的時間感知語言構想，但不屬於 EML 專利語法，也不必依附 EML 才能成立。

更準確的定位是：

```text
EML 是時間迴圈分類學的一個可能語法載體。
時間迴圈分類學是比 EML 更底層的程式設計理論。
```

EML 可以做的事情是：

1. 將時間迴圈符號化。
2. 將 loop type 寫入 CTS。
3. 將執行狀態視覺化。
4. 讓 Agent 讀取 loop metadata。
5. 讓 runtime 自動選擇 suspend / resume / timeout 策略。

但即使沒有 EML，任何主流程式語言仍可實作時間迴圈。

---

## 11. 結論

時間迴圈分類學的核心命題是：

```text
迴圈不只是重複。
迴圈是狀態在時間中的控制流軌跡。
```

普通迴圈處理已經成熟的計算。

時間迴圈處理尚未成熟的未來。

在 AI Agent、長時程自動化、人機協作、分散式系統與自適應程式中，真正困難的不是「如何重複」，而是：

```text
何時等待？
等待什麼？
如何保存狀態？
誰來喚醒？
醒來後如何恢復？
超時後如何降級？
多條路徑如何選擇？
```

因此，時間迴圈分類學不是 EML 的附屬品，而是一套可以被任何語言、任何 runtime、任何 Agent 系統採用的通用程式設計理論。
