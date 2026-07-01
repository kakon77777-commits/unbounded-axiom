# 時間迴圈分類學：面向長時程程式、AI Agent 與自適應系統的通用控制流理論

## 0\. 摘要

時間迴圈分類學不是某一種程式語言的專屬語法，而是一套重新理解程式控制流的通用理論。

傳統程式語言將迴圈主要理解為「重複執行」：

for / while / do-while

但在現代軟體系統、AI Agent、工作流引擎、分散式任務、部署系統、排程系統與人機協作場景中，許多迴圈的本質已不只是重複，而是：

等待條件成熟
保存狀態
釋放資源
延遲決策
外部事件喚醒
跨時間片恢復

這類迴圈可稱為「時間迴圈」。

時間迴圈的核心不在於程式是否重複執行，而在於程式是否能將「時間」視為控制流的一部分。

## 1\. 問題：傳統迴圈分類不足

傳統程式語言通常只有幾種表面迴圈形式：

for item in items:
process(item)

while condition:
update()

但實際工程中，同樣寫成 while，語義可能完全不同：

\# 1. 普通重複
while i < n:
i += 1

\# 2. 收斂求解
while error > epsilon:
optimize()

\# 3. 事件監聽
while True:
event = queue.get()
handle(event)

\# 4. 重試
while retry\_count < max\_retry:
try\_request()

\# 5. 等待人類確認
while not user\_confirmed:
sleep(60)

\# 6. 等待外部條件成熟
while not deployment\_window\_open:
suspend\_until(next\_window)

表面上都是迴圈，實際上它們的差異包括：

1.  終止條件不同。
2.  時間關係不同。
3.  是否佔用資源不同。
4.  是否需要保存狀態不同。
5.  是否依賴外部事件不同。
6.  是否需要人類決策不同。
7.  是否可以被中斷、恢復、遷移不同。
8.  錯誤處理策略不同。

因此，傳統 for / while 是語法分類，不是語義分類。

時間迴圈分類學的目的，是將「迴圈的時間語義」顯式化。

## 2\. 時間迴圈的基本定義

令：

S\_t = 程式在時間 t 的狀態
Φ(S\_t, E\_t, T\_t) = 條件判定函數
E\_t = 外部事件集合
T\_t = 時間上下文

則時間迴圈可定義為：

若 Φ(S\_t, E\_t, T\_t) = True：
執行下一步，產生 S\_{t+1}

若 Φ(S\_t, E\_t, T\_t) = False：
保存 S\_t
暫停執行
釋放資源
等待未來時間或外部事件
在 t + Δt 或事件觸發時恢復

簡化形式：

TemporalLoop(S\_t) =
Proceed(S\_t) if condition is mature
Suspend(S\_t, wake\_rule) otherwise

它與普通迴圈的差異是：

普通迴圈：條件不滿足時繼續嘗試或結束。
時間迴圈：條件不成熟時保存狀態並進入時間等待。

因此，時間迴圈不是單純的 sleep()，也不是單純的 callback，而是：

state + condition + time + event + resume

五者共同構成的控制流單位。

## 3\. 時間迴圈的五個構成元

一個完整時間迴圈至少包含五個元素。

### 3.1 狀態 State

程式目前已經完成到哪一步？

例如：

{
"task": "deploy\_system",
"version": "v1.2.0",
"compiled": true,
"tests\_passed": true,
"waiting\_for": "human\_confirmation"
}

沒有狀態保存，時間迴圈就會退化成普通輪詢。

### 3.2 條件 Condition

什麼情況下可以繼續？

例如：

user\_confirmed == true
api\_rate\_limit\_reset == true
deployment\_window\_open == true
test\_environment\_ready == true
other\_agent\_finished == true

時間迴圈的條件通常不是純內部條件，而是混合條件：

內部狀態 + 外部事件 + 時間窗口 + 人類決策

### 3.3 時間規則 Time Rule

何時重新檢查？

例如：

每 60 秒檢查一次
明天早上 9 點喚醒
部署窗口開始時喚醒
Webhook 到達時喚醒
最多等待 1 小時

時間規則決定時間迴圈的節奏。

### 3.4 喚醒機制 Wake Trigger

誰負責喚醒？

常見喚醒源：

1.  固定時間。
2.  排程器。
3.  Webhook。
4.  Message queue。
5.  File watcher。
6.  Database change。
7.  Human approval。
8.  Agent completion signal。
9.  External API state change。

### 3.5 恢復策略 Resume Policy

醒來後怎麼接續？

例如：

從原狀態繼續
重新驗證條件
重新載入上下文
重新執行上一階段
放棄任務
轉交人工
啟動補救流程

沒有恢復策略，時間迴圈會變成脆弱的非同步碎片。

## 4\. 時間迴圈與普通迴圈的差異

類型

普通迴圈

時間迴圈

核心

重複執行

跨時間保持控制流

條件

多為內部條件

常依賴外部條件

資源

可能持續佔用

可釋放資源

狀態

通常在記憶體中

需要可保存 / 可恢復

等待

blocking / busy waiting / sleep

suspend / schedule / event wake

錯誤處理

異常或跳出

超時、降級、轉交、重排程

適用場景

計算任務

長時程任務、人機協作、Agent 工作流

一句話：

普通迴圈處理「重複」。
時間迴圈處理「尚未成熟的未來」。

## 5\. 時間迴圈分類學

時間迴圈可以依照「等待原因」與「喚醒方式」分類。

## 5.1 延遲時間迴圈：Delay Loop

### 定義

在固定時間後恢復。

Suspend(state, wake\_at = now + Δt)

### 例子

await sleep(60)
retry()

### 適用場景

1.  API rate limit。
2.  重試冷卻。
3.  定時檢查。
4.  排程任務。
5.  暫緩執行。

### 特徵

這是最簡單的時間迴圈，只依賴時間，不依賴複雜外部事件。

## 5.2 條件成熟迴圈：Condition-Maturation Loop

### 定義

等待某個條件成熟。

while not condition():
suspend()
resume()

### 例子

while not deployment\_window\_open():
await sleep(60)

deploy()

### 適用場景

1.  等測試環境可用。
2.  等資料同步完成。
3.  等檔案生成。
4.  等服務恢復。
5.  等市場資料更新。

### 特徵

條件不是立刻可被程式改變的，只能等待外部世界演化。

## 5.3 事件喚醒迴圈：Event-Wakeup Loop

### 定義

不是定時檢查，而是由事件喚醒。

Suspend(state, wake\_on = event)

### 例子

await wait\_for\_webhook("payment\_completed")
ship\_order()

### 適用場景

1.  Webhook。
2.  Message queue。
3.  File watcher。
4.  Database trigger。
5.  IoT sensor。
6.  GitHub action event。
7.  Slack / Gmail / Calendar event。

### 特徵

事件喚醒迴圈比輪詢更節省資源。

## 5.4 人類決策迴圈：Human-Decision Loop

### 定義

等待人類判斷、批准、拒絕或補充資訊。

Suspend(state, waiting\_for = human\_decision)

### 例子

request\_approval("Deploy v1.2.0")
await human\_confirmed()
deploy()

### 適用場景

1.  部署確認。
2.  高風險刪除。
3.  財務付款。
4.  法律審核。
5.  內容發布。
6.  Agent 不確定時請人類選路。

### 特徵

人類決策迴圈是 AI Agent 最重要的時間迴圈之一。

它不是失敗，也不是中斷，而是明確承認：

此處需要外部主體決策。

## 5.5 多 Agent 協作迴圈：Inter-Agent Coordination Loop

### 定義

等待其他 Agent 完成子任務。

Suspend(state, waiting\_for = agent\_B.done)

### 例子

Agent A: 寫 parser
Agent B: 寫 emitter
Agent C: 等 A/B 完成後整合 CLI

### 適用場景

1.  多 Agent 軟體開發。
2.  文件生成。
3.  測試修復。
4.  分散式規劃。
5.  Pipeline orchestration。

### 特徵

這類迴圈需要明確的任務狀態、完成訊號、失敗訊號與重試規則。

## 5.6 超時降級迴圈：Timeout-Degradation Loop

### 定義

等待條件成熟，但若超過期限，就啟動降級策略。

wait until condition or timeout
if timeout:
degrade()

### 例子

try:
await wait\_for\_service(max\_wait=300)
except Timeout:
use\_cached\_result()

### 適用場景

1.  外部 API 不穩。
2.  等人工回覆但逾時。
3.  等部署窗口但錯過時間。
4.  等模型輸出但太久。
5.  Agent 卡住時轉交人工。

### 特徵

這是工程上最實用的時間迴圈之一。

它避免系統無限等待。

## 5.7 週期巡檢迴圈：Periodic Inspection Loop

### 定義

定期醒來檢查狀態，但不是持續工作。

Every Δt:
wake
inspect
sleep

### 例子

while True:
check\_health()
await sleep(300)

### 適用場景

1.  系統健康檢查。
2.  定期備份。
3.  定期爬取。
4.  資料同步。
5.  Agent 定期回顧任務狀態。

### 特徵

它和普通永恆迴圈不同，因為重點不是持續執行，而是週期性醒來。

## 5.8 長時程任務迴圈：Long-Horizon Task Loop

### 定義

任務跨越多個時間片，每次只推進一部分。

state\_t → partial progress → suspend → resume later

### 例子

Day 1: 收集資料
Day 2: 清洗資料
Day 3: 訓練模型
Day 4: 評估
Day 5: 發布

### 適用場景

1.  長期研究。
2.  大型軟體開發。
3.  AI Agent 長任務。
4.  自動化營運。
5.  多日資料處理。

### 特徵

這類迴圈不是一次執行完，而是把任務切成時間片。

## 5.9 演化選路迴圈：Evolutionary Decision Loop

### 定義

等待多個候選路徑產生結果，再選擇下一步。

explore candidates
wait for evaluations
select best path
continue

### 例子

生成三種 parser 架構
各自跑 benchmark
等待測試結果
選擇最佳架構

### 適用場景

1.  A/B testing。
2.  多方案設計。
3.  模型超參數搜索。
4.  Agent 多路徑探索。
5.  產品策略選擇。

### 特徵

這類迴圈與普通時間迴圈不同，因為它等待的不是單一條件，而是多條路徑的結果。

## 5.10 螺旋推進迴圈：Spiral Progress Loop

### 定義

方向已知，但每一輪推進都需要時間、檢查與修正。

v0.1 → v0.2 → v0.3 → v1.0

### 例子

先完成 MVP
再加測試
再加 CLI
再加 Editor
再加 Agent integration

### 適用場景

1.  產品開發。
2.  技術路線圖。
3.  研究計畫。
4.  書籍寫作。
5.  系統迭代。

### 特徵

它不是隨機探索，而是沿著已知方向逐步逼近。

## 6\. 時間迴圈的工程接口

一個通用時間迴圈 runtime 可以長這樣：

class TemporalLoop:
def \_\_init\_\_(
self,
condition,
body,
max\_wait=None,
check\_interval=None,
wake\_trigger=None,
timeout\_policy=None,
persistence=True,
):
self.condition = condition
self.body = body
self.max\_wait = max\_wait
self.check\_interval = check\_interval
self.wake\_trigger = wake\_trigger
self.timeout\_policy = timeout\_policy
self.persistence = persistence

async def run(self, state):
while True:
if await self.condition(state):
return await self.body(state)

if self.max\_wait and exceeded(self.max\_wait):
return await self.timeout\_policy(state)

save\_state(state)

await suspend(
interval=self.check\_interval,
trigger=self.wake\_trigger,
)

state = load\_state()

它至少需要以下 metadata：

{
"loopType": "human\_decision",
"condition": "user\_confirmed",
"statePersistence": true,
"wakeTrigger": "approval\_event",
"maxWait": 3600,
"timeoutPolicy": "cancel\_or\_escalate",
"resourcePolicy": "suspend\_not\_busy\_wait",
"resumePolicy": "reload\_and\_validate"
}

這份 metadata 比語法本身更重要。

因為任何語言都可以實作它：

1.  Python。
2.  JavaScript / TypeScript。
3.  Go。
4.  Rust。
5.  Java。
6.  C#。
7.  Workflow engine。
8.  Agent runtime。
9.  Serverless orchestration。
10.  CI/CD pipeline。

## 7\. 為什麼要這樣用？

### 7.1 因為現代程式不再只是短時程計算

傳統程式模型假設：

輸入 → 計算 → 輸出

但現代系統常常是：

輸入 → 部分計算 → 等待 → 外部事件 → 恢復 → 決策 → 再等待 → 完成

例如：

1.  部署系統等待人類批准。
2.  Agent 等另一個 Agent 完成。
3.  工作流等待付款完成。
4.  爬蟲等待 rate limit 重置。
5.  長任務等待資料更新。
6.  AI 系統等待用戶補充上下文。
7.  CI/CD 等測試環境可用。

這些都不是普通 while 能清楚表達的。

### 7.2 因為 busy waiting 是錯誤抽象

錯誤寫法：

while not ready():
pass

稍好但仍粗糙：

while not ready():
await sleep(60)

更好的抽象：

await temporal\_wait(
condition=ready,
state=current\_state,
wake\_on=\["event", "timer"\],
timeout=3600,
resume=continue\_task
)

時間迴圈的核心是把「等待」從低階技巧提升成高階控制流。

### 7.3 因為 AI Agent 天然需要時間迴圈

Agent 的工作不是一次性函式呼叫，而是長時程狀態推進。

典型 Agent loop：

計畫 → 行動 → 觀察 → 修正 → 行動

但真正的 Agent runtime 還需要：

等待工具完成
等待人類批准
等待網路結果
等待資料更新
等待其他 Agent
等待明天再做
等待條件成熟後恢復

因此，時間迴圈是 Agent runtime 的基礎控制流。

### 7.4 因為它可以統一排程、事件、工作流與人機協作

現在工程中常把這些東西拆開：

1.  cron。
2.  queue。
3.  webhook。
4.  retry。
5.  state machine。
6.  workflow engine。
7.  async task。
8.  human approval。
9.  Agent loop。

時間迴圈分類學可以把它們統一理解為：

不同喚醒條件與狀態恢復策略下的時間化迴圈。

這不是取代現有工具，而是給現有工具一套共同語義。

### 7.5 因為它可以讓 runtime 更安全

一旦迴圈類型被標記，runtime 就可以自動調整策略：

loop type

runtime policy

delay loop

使用 timer，不 busy wait

human decision loop

保存狀態，等待 approval event

timeout loop

超時後降級

event wakeup loop

註冊 webhook / queue listener

agent coordination loop

監控子任務狀態

evolutionary loop

收集候選結果並比較

spiral loop

按 roadmap checkpoint 推進

這樣系統就能知道：

這個 loop 不該無限跑。
這個 loop 應該暫停。
這個 loop 要保存狀態。
這個 loop 超時要轉交人工。
這個 loop 要等待外部事件。

## 8\. 時間迴圈與專利 / 開源

時間迴圈分類學本身比較像一種通用程式設計理論。

它的價值不一定在「獨占某個語法」，而在於：

1.  命名。
2.  分類。
3.  標準化。
4.  開源實作。
5.  runtime contract。
6.  Agent protocol。
7.  教育與文件。
8.  工具鏈採用。

如果公開釋放，它可以成為一種公共語彙：

這不是普通 retry。
這是 timeout-degradation temporal loop。

這不是 event loop。
這是 event-wakeup temporal loop。

這不是 workflow hack。
這是 state-persistent temporal loop。

這種語彙本身就有價值。

## 9\. 最小實作建議

不需要先做新語言。可以先做一個 Python / TypeScript library。

### Python 版本

@temporal\_loop(
type="human\_decision",
condition=check\_user\_confirmed,
max\_wait=3600,
check\_interval=60,
timeout\_policy="cancel",
persistence=True,
)
async def deploy\_task(state):
deploy(state\["version"\])

### TypeScript 版本

await temporalLoop({
type: "event\_wakeup",
condition: () => paymentCompleted(orderId),
wakeOn: \["webhook:payment.completed"\],
maxWait: "24h",
persistence: true,
resume: async (state) => shipOrder(state.orderId),
});

### Agent 版本

{
"task": "deploy\_v1\_2",
"loopType": "human\_decision",
"waitingFor": "approval",
"state": {
"compiled": true,
"testsPassed": true
},
"resumeAction": "deploy",
"timeoutPolicy": "ask\_again\_or\_cancel"
}

## 10\. 結論

時間迴圈分類學的核心命題是：

迴圈不只是重複。
迴圈是狀態在時間中的控制流軌跡。

普通迴圈處理已經成熟的計算。

時間迴圈處理尚未成熟的未來。

在 AI Agent、長時程自動化、人機協作、分散式系統與自適應程式中，真正困難的不是「如何重複」，而是：

何時等待？
等待什麼？
如何保存狀態？
誰來喚醒？
醒來後如何恢復？
超時後如何降級？
多條路徑如何選擇？

因此，時間迴圈分類學不是 EML 的附屬品，而是一套可以被任何語言、任何 runtime、任何 Agent 系統採用的通用程式設計理論。
