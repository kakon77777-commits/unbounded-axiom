---
title: "Scheduler–Loop–Graph 智能管理 Runtime v0.1"
series: "網路資訊海動態秩序化"
series_id: "EML-IIODO"
document_id: "EML-IIODO-WP-02"
document_type: "內部 MD 技術白皮書"
author: "Neo.K"
organization: "EveMissLab"
version: "0.1.0"
status: "內部 Runtime 規格基線"
date: "2026-08-01"
language: "zh-TW"
visibility: "internal"
license_note: "內部技術文件；對外引用或公開前應再次檢查實作版本、第三方依賴、來源授權與部署安全。"
---

# Scheduler–Loop–Graph 智能管理 Runtime v0.1

## 從半自動資訊工作流到可恢復、可中斷、可重放的有限自治執行層

## 摘要

本文件是《網路資訊海動態秩序化》系列第十二篇，也是第二份內部技術白皮書。前一篇 EML-IIODO-WP-01 已將 AGIRight Topics 的現行工作方式拆解為「Human-triggered、AI-executed、Human-audited」的半自動流程，並建立 Run Manifest、Candidate、Evidence、Event、Topic、Review 與 Run Report 等最小資料物件。本文件在此基礎上，不再描述「人類如何每天叫 AI 做一次」，而是定義一個可以接管時間觸發、狀態遷移、局部迭代、持久化、錯誤恢復與人工中斷的最小 Runtime。

本 Runtime 的核心不是把單一 LLM 變成永久在線的 AGI，而是透過工程結構，把有限領域任務組成一個具有持續性的執行系統：Scheduler 提供時間持續性，Graph 提供狀態與責任的結構持續性，Loop（自環）提供局部反覆處理與條件重試，Checkpoint 提供執行狀態持久化，Store 提供跨 Run 的長期資料存取，Interrupt 提供 Human-in-the-Loop，Retry 與 Compensation 提供失敗恢復，Idempotency 則限制重放與重試造成的重複副作用。

可將 v0.1 Runtime 表示為：

$$
\mathcal{R}_{0.1}
=
(Scheduler,
Graph,
Loop,
Checkpoint,
Store,
Interrupt,
Retry,
EffectGuard,
Observability)
$$

其中最重要的設計原則不是「盡可能自動」，而是：

$$
\boxed{
\text{有界自治}
+
\text{可恢復}
+
\text{可追溯}
+
\text{可中斷}
+
\text{可重放}
+
\text{副作用可控制}
}
$$

本白皮書將 Runtime 分為控制平面、執行平面、狀態平面、記憶平面、人工治理平面與觀測平面六部分；同時提出 Run／Thread／Checkpoint／Domain 四級識別、Graph 節點契約、Loop Budget、有界重試、冪等發布、Outbox／Effect Ledger、Dead-Letter Queue、Resume Token、Run Lease、租約鎖、去重鍵與最小狀態機。文件不綁定單一開源框架，但會以目前成熟的 Graph workflow、cron scheduler 與 durable workflow 工程實務作為參照。

v0.1 的目標是：即使程序中途崩潰、模型 API 暫時不可用、人類審核隔天才回來、同一排程重複觸發、或某個節點因網路錯誤執行兩次，系統仍能明確回答「現在在哪裡、做過什麼、哪些結果已生效、下一步應該做什麼」。

**關鍵詞：** Scheduler、Loop、自環、Graph Runtime、Checkpoint、Store、Interrupt、Retry、Idempotency、Durable Execution、Human-in-the-Loop、AGIRight、有限自治

---

## 1. 文件目的與非目標

### 1.1 目的

本文件回答以下九個工程問題：

1. 每日資訊工作如何由人工觸發改為 Scheduler 觸發？
2. WP-01 的十二個流程狀態如何變成可執行 Graph？
3. 哪些節點可以自環，何時必須退出？
4. 執行中斷後，系統如何從正確位置繼續？
5. 同一節點重試時，如何避免重複發布或重複寫入？
6. Human-in-the-Loop 如何成為 Runtime 原生狀態，而不是臨時聊天？
7. 跨日、跨 Run 的領域記憶應放在哪裡？
8. 如何區分可重試錯誤、需模型修正錯誤與需人工升級錯誤？
9. 如何讓每次 Run 可觀測、可審計、可回放？

### 1.2 非目標

本文件刻意不處理：

- 各類工作風險與自主等級的完整分類；
- Domain Pack 的跨領域配置規格；
- 「每日三則」的正式排名演算法；
- 母站—子站資料交換與訂閱架構；
- Temporal Knowledge Graph；
- 多 Agent 審查治理；
- 主體性 AI 的法律或道德地位。

這些分別留給 WP-03 至 WP-10。

因此，WP-02 的角色是：

$$
\boxed{
\text{把流程變成 Runtime}
}
$$

而不是把整個平台一次做完。

---

## 2. Runtime 的基本假設

### 2.1 AI 不提供時間持續性

單次模型呼叫可以完成推理或生成，但它本身不保證明天會自行醒來，也不保證程序崩潰後知道昨天做到哪裡。

因此：

$$
\text{Model Intelligence}
\neq
\text{Operational Continuity}
$$

時間持續性必須由外部 Scheduler 或 durable runtime 提供。

### 2.2 Graph 不等於智能，但提供結構持續性

Graph 的價值不在於讓模型更聰明，而在於顯式表示：

- 當前狀態；
- 可走的下一步；
- 分支條件；
- 失敗去向；
- 人工 Gate；
- 哪些節點可重新進入；
- 哪些節點具有外部副作用。

可表示為：

$$
G=(V,E,C)
$$

其中 $V$ 為節點、 $E$ 為轉移、 $C$ 為條件。

### 2.3 Loop（自環）必須有界

本系列沿用既有工程語境中的 `Loop（自環）` 稱呼。此處 Loop 指節點或子流程在條件未滿足時反覆執行，而不是本文另行提出的本體論「自環」。

任何 Loop 必須至少有一種退出條件：

- 最大次數；
- 最大時間；
- 最大 token／成本；
- 目標達成；
- 無新增證據；
- 風險升級；
- 人工中斷。

令第 $i$ 個 Loop 的預算為：

$$
B_i=(n_{max},t_{max},c_{max},\Delta_{min})
$$

只要任一限制觸發，就不得無限自環。

---

## 3. Runtime 六平面架構

v0.1 將系統拆成六個邏輯平面。

### 3.1 控制平面 Control Plane

負責：

- Scheduler；
- Run 建立；
- Domain 配置載入；
- 併發限制；
- Lease／Lock；
- 暫停與恢復；
- Run 取消。

### 3.2 執行平面 Execution Plane

負責：

- Graph 節點；
- Tool call；
- LLM call；
- 網頁搜尋／讀取；
- 正規化；
- 排序；
- 生成；
- 發布 adapter。

### 3.3 狀態平面 State Plane

負責：

- Thread state；
- Node state；
- Checkpoint；
- Resume cursor；
- Pending writes；
- 當前錯誤；
- Loop 計數器。

### 3.4 記憶平面 Memory Plane

負責跨 Run 資料：

- 已發事件；
- 來源註冊；
- 歷史標籤；
- Domain policy；
- Review history；
- 去重 fingerprint；
- 長期統計。

### 3.5 人工治理平面 Human Governance Plane

負責：

- Review queue；
- Approval；
- Reject；
- Edit；
- Escalation；
- Manual override；
- Emergency stop。

### 3.6 觀測平面 Observability Plane

負責：

- structured logs；
- traces；
- metrics；
- Run timeline；
- error taxonomy；
- cost usage；
- model/tool version；
- audit export。

其關係可簡化為：

$$
Control
\rightarrow
Execution
\leftrightarrow
State
\leftrightarrow
Memory
$$

並由：

$$
Human Governance
\quad\text{與}\quad
Observability
$$

橫跨整個 Runtime。

---

## 4. 四級識別模型

為避免 Run、Graph thread、歷史領域資料互相混淆，v0.1 固定四種主要 ID。

### 4.1 `domain_id`

例：

```text
agiright
```

代表長期領域觀測站。

### 4.2 `run_id`

每次觸發產生唯一 ID：

```text
2026-08-01T09-00-00+08:00__agiright__01
```

一個 Run 對應一次完整工作輪。

### 4.3 `thread_id`

Graph durable state 的持續識別。一般情況：

$$
thread\_id=run\_id
$$

但人工審核、長任務或跨 Run 合併流程時，可以讓一個 thread 跨多次控制事件。

### 4.4 `checkpoint_id`

每個可恢復邊界的狀態快照 ID。

其層級為：

$$
Domain
\supset
Run
\supseteq
Thread
\supset
Checkpoint
$$

其中 Run 與 Thread 在 v0.1 可以一對一，但資料模型不鎖死此關係。

---

## 5. Scheduler 規格

### 5.1 Scheduler 只負責觸發，不負責內容判斷

Scheduler 的職責是：

$$
\text{when to start}
$$

而不是：

$$
\text{what is important}
$$

v0.1 支援三種觸發來源：

```yaml
trigger_type:
  - manual
  - cron
  - event
```

### 5.2 Cron Trigger

每日領域資訊收集可以使用一般 cron 排程。

例如：

```yaml
schedule:
  timezone: Asia/Taipei
  cron: "17 9 * * *"
```

刻意避免整點觸發，減少共享排程基礎設施的尖峰負載風險。

### 5.3 Event Trigger

後續可以接受：

- 來源 feed 新項目；
- webhook；
- 特定資料庫變更；
- 人工標記重大事件；
- 上一個 Run 完成訊號。

但 v0.1 不要求全數實作。

### 5.4 Duplicate Trigger Guard

若 Scheduler 重複觸發，同一個 $domain\_id+period$ 不應產生兩個同時發布的 Run。

建立：

$$
DedupeKey
=
hash(domain\_id,window\_start,policy\_version)
$$

Run 建立前先取得 lease：

```text
lease:agiright:2026-08-01
```

若 lease 已存在，第二個觸發應：

- join existing run；或
- mark duplicate；或
- 延後排隊；

不得默默平行發布。

---

## 6. Graph：將 WP-01 十二狀態落成節點

WP-01 定義的十二狀態可落為下列 Runtime Graph：

```text
START
  ↓
run_init
  ↓
load_domain_policy
  ↓
discover_candidates
  ↓
resolve_sources
  ↓
extract_evidence
  ↓
normalize_events
  ↓
dedupe_and_link
  ↓
domain_gate
  ↓
rank_candidates
  ↓
compose_topics
  ↓
package_output
  ↓
review_gate
  ↓
publish
  ↓
finalize_run
  ↓
END
```

注意：Graph 節點數可以比 WP-01 狀態多，因為 `finalize_run` 與 effect guard 在 Runtime 必須獨立存在。

### 6.1 節點契約

每個節點必須宣告：

```yaml
node:
  id: resolve_sources
  reads:
    - candidate_records
  writes:
    - source_evidence
  side_effect: false
  retry_class: transient_io
  timeout_sec: 60
  loop_budget: null
  human_gate: false
```

如果節點有外部副作用：

```yaml
side_effect: true
idempotency_key_required: true
```

### 6.2 節點不得暗藏流程控制

v0.1 原則：

> 節點負責工作，Graph 負責流程。

避免在單一巨型 prompt 裡隱藏「搜尋→判斷→重試→發布」全部流程，否則 checkpoint、重放與錯誤分類將失去意義。

---

## 7. Loop（自環）設計

### 7.1 三種允許的 Loop

#### A. Evidence Loop

來源不足時重新搜尋：

$$
search
\rightarrow
read
\rightarrow
quality\_gate
\rightarrow
search
$$

#### B. Repair Loop

格式或資料結構失敗：

$$
compose
\rightarrow
validate
\rightarrow
repair
\rightarrow
validate
$$

#### C. Ranking Loop

候選三則過度重複：

$$
rank
\rightarrow
diversity\_check
\rightarrow
rerank
$$

### 7.2 禁止的無界 Loop

禁止：

```text
while not perfect:
    ask_model_again()
```

因為「perfect」不可測量，且沒有資源上限。

### 7.3 Loop Budget

每個 Loop 記錄：

```yaml
loop_state:
  loop_id: evidence_search
  attempt: 2
  max_attempts: 4
  elapsed_sec: 93
  max_elapsed_sec: 300
  cost_units: 0.42
  max_cost_units: 1.50
  evidence_delta: 0.03
  min_evidence_delta: 0.01
```

退出函數：

$$
Exit_i
=
(n\ge n_{max})
\lor
(t\ge t_{max})
\lor
(c\ge c_{max})
\lor
(Goal=true)
\lor
(RiskEscalated=true)
$$

---

## 8. Checkpoint 與 Durable Execution

### 8.1 為什麼每個重要邊界都要能保存

如果流程在 `compose_topics` 之後崩潰，不應重新：

- 搜索全部來源；
- 重新讀取全部文章；
- 重新判定全部事件。

應從最近成功 checkpoint 繼續。

### 8.2 Checkpoint 內容

最低包含：

```yaml
checkpoint:
  checkpoint_id: cp_009
  thread_id: ...
  run_id: ...
  node: compose_topics
  state_version: 1
  created_at: ...
  next_nodes:
    - package_output
  loop_counters: {...}
  pending_effects: []
  last_error: null
```

### 8.3 Checkpoint 不等於長期記憶

Checkpoint 保存「這次 Run 做到哪裡」。

Store 保存「跨 Run 已經知道什麼」。

因此：

$$
Checkpoint
\neq
Store
$$

也可表示為：

$$
M_{short}
=
\text{thread-scoped state}
$$

$$
M_{long}
=
\text{domain-scoped store}
$$

### 8.4 Replay

Replay 必須區分：

1. **Pure Node Replay**：無外部副作用，可安全重算；
2. **Read Replay**：再次讀取來源，可能取得不同版本，需記錄 fetch time；
3. **Effect Replay**：發布、寄送、寫遠端資料，必須受 EffectGuard 保護。

---

## 9. Store：跨 Run 長期狀態

v0.1 Store 最少分五個 namespace：

```text
/domain/{domain_id}/sources
/domain/{domain_id}/events
/domain/{domain_id}/topics
/domain/{domain_id}/reviews
/domain/{domain_id}/policies
```

### 9.1 Sources

保存：

- canonical URL；
- publisher；
- source type；
- reliability metadata；
- first_seen；
- last_seen；
- robots／access note；
- fetch policy。

### 9.2 Events

保存歷史事件 fingerprint，支援：

- duplicate detection；
- update detection；
- follow-up linking。

### 9.3 Reviews

人類審核不只影響當次輸出，也應保存成後續 policy 調整的資料。

例如：

```yaml
review_pattern:
  rejected_tag: consciousness
  reason: "source was commentary, not primary evidence"
```

此資料之後可由 WP-09 多 Agent 與異常處理使用。

---

## 10. Interrupt：Human-in-the-Loop 作為 Runtime 原生狀態

### 10.1 人工審核不是流程外聊天

當系統需要人工時，Graph 應進入：

```text
WAITING_FOR_HUMAN
```

而不是終止。

狀態轉移：

$$
review\_gate
\rightarrow
interrupt
\rightarrow
WAITING
\rightarrow
resume
$$

### 10.2 Review Payload

```yaml
review_request:
  run_id: ...
  checkpoint_id: ...
  reason_code: high_controversy
  proposed_topics:
    - topic_1
    - topic_2
    - topic_3
  allowed_actions:
    - approve
    - reject
    - edit
    - request_more_evidence
```

### 10.3 Resume Token

人工回覆必須綁定：

- `run_id`
- `thread_id`
- `checkpoint_id`
- `review_request_id`

避免審核結果被套用到錯誤 Run。

### 10.4 Interrupt 前副作用必須冪等

若 Runtime 恢復時會重新執行節點前半段，任何位於 interrupt 前的外部副作用必須可以安全重放，或移至 interrupt 之後。

---

## 11. 錯誤分類與 Retry Policy

所有錯誤不應一律「再試一次」。

v0.1 定義六類：

| 類別 | 例子 | 預設處理 |
|---|---|---|
| transient_io | timeout、5xx、短暫網路失敗 | 指數退避重試 |
| rate_limit | 429、配額暫滿 | 延遲重試／換通道 |
| deterministic_validation | schema 不合法、必要欄位缺失 | Repair Loop |
| semantic_uncertainty | 來源衝突、事件身分不明 | 補證據或人工升級 |
| policy_violation | 不允許的來源／高風險動作 | 不重試，阻擋 |
| side_effect_unknown | 發布請求逾時但不確定是否成功 | 先查 effect ledger，不直接重做 |

### 11.1 指數退避

對可重試錯誤：

$$
t_k
=
\min(t_0\cdot b^{k-1}+jitter,t_{max})
$$

### 11.2 Retry Budget

例如：

```yaml
retry:
  max_attempts: 3
  initial_interval_sec: 1
  backoff_factor: 2
  max_interval_sec: 30
  jitter: true
```

### 11.3 Retry 失敗後的去向

不是全部 `FAILED`，而應可路由：

```text
retry_exhausted
  ├─→ fallback_source
  ├─→ human_review
  ├─→ dead_letter_queue
  └─→ finalize_partial
```

---

## 12. EffectGuard：副作用、冪等與補償

### 12.1 為什麼最危險的是「成功但回覆丟失」

假設 publish API 已成功建立頁面，但網路回覆超時。Runtime 若直接重試，可能發布兩次。

因此：

$$
\text{Retry-safe computation}
\neq
\text{Retry-safe side effect}
$$

### 12.2 Idempotency Key

每次外部副作用建立：

$$
K_{effect}
=
hash(run\_id,node\_id,effect\_type,target)
$$

發布 adapter 必須先查 Effect Ledger。

```yaml
effect:
  effect_key: ...
  type: publish_topic_page
  target: agiright/topics/2026-08-01
  status: committed
  external_id: ...
  committed_at: ...
```

### 12.3 Effect Ledger 狀態

```text
PLANNED
→ IN_FLIGHT
→ COMMITTED
→ VERIFIED
```

或：

```text
IN_FLIGHT
→ UNKNOWN
→ RECONCILE
```

### 12.4 Compensation

對可逆動作建立 compensation：

- publish → unpublish；
- create draft → delete draft；
- add tag → remove tag；
- update pointer → restore previous pointer。

不可逆動作應在 WP-03 風險分級中提高人工 Gate。

---

## 13. Outbox Pattern 與 Publish Adapter

為避免資料庫狀態已標記「完成」但外部網站尚未發布，v0.1 建議將待發布內容先寫入 Outbox。

```text
Graph State
  ↓
Publish Intent
  ↓
Outbox
  ↓
Publisher Worker
  ↓
Effect Ledger
  ↓
External Site
```

如此即使 publisher worker 崩潰，Outbox 中未提交的工作仍可重新取得。

`publish` 節點只建立意圖，不直接假設外部世界已成功。

---

## 14. Dead-Letter Queue 與人工修復

當任務超出所有重試預算，應轉入 Dead-Letter Queue：

```yaml
dlq_record:
  run_id: ...
  node_id: ...
  error_class: semantic_uncertainty
  last_error: ...
  attempts: 4
  state_ref: checkpoint_id
  recommended_action: human_review
```

DLQ 的目的不是藏失敗，而是讓失敗成為一等資料。

每個 Run Finalize 前必須列出：

- unresolved errors；
- skipped candidates；
- pending reviews；
- unknown effects。

---

## 15. 併發、Lease 與 Run Ownership

### 15.1 同一領域的每日 Run 預設單寫者

v0.1 對 AGIRight 採：

$$
SingleWriter(domain,window)
$$

避免兩個 Agent 同時發布不同的「今日三則」。

### 15.2 Lease

執行者取得有限時間租約：

```yaml
lease:
  key: agiright:2026-08-01
  owner: worker_03
  expires_at: ...
  heartbeat_at: ...
```

worker 崩潰後 lease 過期，其他 worker 才能接手。

### 15.3 跨節點平行化

允許：

- 多來源抓取平行；
- 多候選 Evidence extraction 平行；
- 多語封裝平行。

不允許未協調地平行：

- 最終排名提交；
- 同一 canonical topic 發布；
- 同一 taxonomy 版本寫入。

---

## 16. Runtime State Schema v0.1

```yaml
runtime_state:
  domain_id: agiright
  run_id: ...
  thread_id: ...
  run_status: RUNNING
  trigger:
    type: cron
    requested_at: ...
  policy_version: agiright-domain-v0.1
  candidates: []
  evidence: []
  events: []
  ranked_events: []
  topics: []
  review:
    status: not_required
    request_id: null
  loops:
    evidence_search:
      attempt: 1
      max_attempts: 4
  effects:
    pending: []
    committed: []
  errors: []
  metrics: {}
  next_node: discover_candidates
```

資料必須可序列化。大型 HTML、影片、PDF 或其他重資產不直接塞入 Graph state，只保存 object reference。

---

## 17. Run 狀態機

v0.1 Run 狀態固定：

```text
CREATED
→ QUEUED
→ RUNNING
→ WAITING_FOR_HUMAN
→ RUNNING
→ PUBLISHING
→ COMPLETED
```

失敗分支：

```text
RUNNING
→ DEGRADED
→ COMPLETED_PARTIAL
```

或：

```text
RUNNING
→ FAILED
```

以及：

```text
ANY_NONTERMINAL
→ CANCELLED
```

### 17.1 `DEGRADED`

代表系統仍可完成本輪，但某些能力不可用，例如：

- 一個來源站無法存取；
- 某個翻譯模型失效；
- JSON export 失敗但主頁可發布。

### 17.2 `COMPLETED_PARTIAL`

代表 Run 有明確缺口，但結果仍被允許保存，例如只找到兩則達到門檻的高品質新聞。

這比為了湊三則而降低品質更合理。

---

## 18. Run Manifest v0.2

在 WP-01 的 Run Manifest 上新增 Runtime 欄位：

```yaml
run_manifest:
  run_id: ...
  domain_id: agiright
  thread_id: ...
  trigger_type: cron
  trigger_time: ...
  scheduler_id: daily_topics
  graph_version: slg-runtime-v0.1
  domain_policy_version: agiright-v0.1
  model_profile: ...
  tool_profile: ...
  checkpoint_backend: postgres
  store_backend: postgres
  effect_ledger: enabled
  human_gate_policy: review-v0.1
  started_at: ...
  finished_at: ...
  terminal_status: COMPLETED
```

如此每次 Run 可以重建當時到底用了哪一套 Runtime。

---

## 19. Observability：不只記錄成功／失敗

每個節點至少記錄：

```yaml
node_trace:
  run_id: ...
  node_id: rank_candidates
  attempt: 1
  started_at: ...
  finished_at: ...
  latency_ms: ...
  model_id: ...
  tool_calls: 2
  input_refs: [...]
  output_refs: [...]
  error: null
```

### 19.1 v0.1 核心指標

#### Run Completion Rate

$$
RCR
=
\frac{N_{completed}}{N_{started}}
$$

#### Human Intervention Rate

$$
HIR
=
\frac{N_{runs\ requiring\ human}}{N_{runs}}
$$

#### Retry Rate

$$
RR
=
\frac{N_{retried\ node\ executions}}{N_{node\ executions}}
$$

#### Resume Success Rate

$$
RSR
=
\frac{N_{successful\ resumes}}{N_{resume\ attempts}}
$$

#### Duplicate Effect Rate

$$
DER
=
\frac{N_{duplicate\ external\ effects}}{N_{effects}}
$$

目標應接近：

$$
DER\rightarrow0
$$

### 19.2 不虛構基線

和 WP-01 一樣，v0.1 先定義計算方式，沒有歷史監測資料時不補造百分比。

---

## 20. 安全與權限邊界

### 20.1 Read 與 Write 分權

Runtime 權限應至少分：

```text
READ_WEB
READ_STORE
WRITE_DRAFT
WRITE_STORE
PUBLISH
DELETE
ADMIN_POLICY
```

資訊收集 Agent 不應天然取得 `DELETE` 或 `ADMIN_POLICY`。

### 20.2 Tool Allowlist

每個 Domain Pack 後續宣告可用工具。

v0.1 Runtime 只讀：

```yaml
allowed_tools:
  - web_search
  - web_fetch
  - source_parser
  - local_store
  - draft_writer
```

發布權另外綁定 publish adapter。

### 20.3 Emergency Stop

控制平面必須支援：

```text
PAUSE_DOMAIN
PAUSE_ALL
CANCEL_RUN
DISABLE_PUBLISH
```

而不是只有關閉模型 API Key 這種粗暴手段。

---

## 21. v0.1 參考部署拓撲

最小部署可以非常簡單：

```text
Cron / Scheduler
      ↓
Runtime API
      ↓
Graph Worker
  ↙       ↘
Checkpoint  Domain Store
   DB          DB
      ↘       ↙
      Review Queue
           ↓
      Publish Outbox
           ↓
       Site Adapter
```

MVP 不需要一開始導入大型分散式系統。

可先使用：

- 一個 scheduler；
- 一個 Graph worker；
- SQLite／PostgreSQL checkpoint；
- PostgreSQL／SQLite domain store；
- 檔案式或 DB outbox；
- 單一 review queue。

待多子站與高併發出現後再拆服務。

---

## 22. 框架中立與實作映射

本規格刻意不把系統綁死在某一套開源框架，但目前可直接找到對應能力：

### 22.1 Scheduler

可由：

- system cron；
- GitHub Actions schedule；
- Prefect；
- Kubernetes CronJob；
- 其他工作排程器。

### 22.2 Graph／Checkpoint／Interrupt

可由支援持久化工作流與 Human-in-the-Loop 的 Graph Runtime 實作。

### 22.3 Durable Workflow

若未來需要更長時間、跨服務與多年級 durable workflow，可將控制層替換為專門 durable execution 系統，而保留 Domain、Run、Effect Ledger 與資料契約。

因此架構遵守：

$$
\text{Semantic Contract}
>
\text{Framework Binding}
$$

框架可以換，Run 與資料語義不能跟著消失。

---

## 23. AGIRight v0.1 實作路線

### M0｜現況

```text
Human Trigger
→ AI Workflow
→ Human Audit
```

### M1｜自動 Run 初始化

加入：

- `run_id`
- Run Manifest
- domain policy version
- node log

### M2｜Scheduler 化

將「每天提醒 AI 做」替換為：

```text
cron → create_run()
```

但保留人工批准發布。

### M3｜Checkpoint + Resume

讓流程中途：

- 崩潰可恢復；
- 人工審核可隔日繼續；
- 不重做已完成節點。

### M4｜EffectGuard + Idempotent Publish

發布、更新與 rollback 全部寫入 effect ledger。

### M5｜有限自治

只有在 WP-03 完成任務風險分級後，才允許低風險 Run：

$$
review\_gate=optional
$$

對高爭議事件仍：

$$
review\_gate=required
$$

---

## 24. 驗收條件

Runtime v0.1 不是「有一張 Graph 圖」就算完成。

至少必須通過以下測試。

### 24.1 Crash Resume Test

在任意非副作用節點強制終止程序，重新啟動後從最近 checkpoint 繼續。

### 24.2 Duplicate Trigger Test

同一日同一 domain 連續觸發兩次，只允許一個 active publisher。

### 24.3 Retry Test

模擬 5xx，確認符合 retry budget，不無限重試。

### 24.4 Interrupt Test

在 review gate 暫停 24 小時，再使用同一 checkpoint 恢復。

### 24.5 Idempotent Publish Test

同一 `effect_key` 執行兩次，只產生一個外部發布結果。

### 24.6 Unknown Effect Test

模擬 publish 已成功但回覆 timeout，Runtime 必須先 reconcile，再決定是否重做。

### 24.7 Replay Test

從歷史 checkpoint 重放純計算節點，不改變既有外部發布結果。

### 24.8 Audit Reconstruction Test

只用 Run Manifest、checkpoint、trace、effect ledger 與 store，即可回答：

- 這則 Topic 從哪些來源形成？
- 哪個模型／節點產生？
- 是否有重試？
- 是否人工批准？
- 是否曾 rollback？

---

## 25. v0.1 最小資料夾結構

```text
runtime/
├─ configs/
│  ├─ runtime.yaml
│  └─ scheduler.yaml
├─ domains/
│  └─ agiright/
│     └─ policy.yaml
├─ graph/
│  ├─ state.py
│  ├─ nodes/
│  ├─ routes/
│  └─ build.py
├─ persistence/
│  ├─ checkpoint.py
│  ├─ store.py
│  └─ migrations/
├─ effects/
│  ├─ ledger.py
│  ├─ outbox.py
│  └─ adapters/
├─ review/
│  ├─ queue.py
│  └─ schema.py
├─ observability/
│  ├─ logs.py
│  ├─ metrics.py
│  └─ traces.py
├─ scheduler/
│  └─ jobs.py
├─ tests/
│  ├─ test_resume.py
│  ├─ test_retry.py
│  ├─ test_idempotency.py
│  └─ test_interrupt.py
└─ app.py
```

此結構不是強制程式語言實作，而是責任邊界範例。

---

## 26. 核心不變式 Invariants

v0.1 最重要的不是功能清單，而是以下不變式。

### Invariant 1｜同一外部副作用不可因重試無限制重複

$$
count(effect\_key)\le1
$$

對語義上只能發生一次的 effect 必須成立。

### Invariant 2｜任何 WAITING Run 必須能找到恢復位置

$$
WAITING
\Rightarrow
\exists checkpoint\_id
$$

### Invariant 3｜任何發布結果必須能追溯到來源與 Run

$$
PublishedTopic
\Rightarrow
Run
\land
Evidence
\land
EffectRecord
$$

### Invariant 4｜任何 Loop 必須有 Budget

$$
Loop
\Rightarrow
Budget\neq\varnothing
$$

### Invariant 5｜任何高風險 Gate 未批准不得穿越

$$
Gate=required
\land
Approval=false
\Rightarrow
Publish=false
$$

### Invariant 6｜框架升級不能破壞歷史 Run 的語義

Runtime 版本與 domain policy 必須寫入 Manifest，保證之後仍能理解舊紀錄。

---

## 27. 與「類未來」命題的關係

公開理論第六篇提出：

$$
Scheduler
+
Loop
+
Graph
$$

已足以讓部分狹域 AI 工作進入初步智能化管理。

本文件進一步補上：僅有三者還不夠形成可靠 Runtime。

真正工程基線應是：

$$
\boxed{
Scheduler
+
Graph
+
BoundedLoop
+
Checkpoint
+
Store
+
Interrupt
+
Retry
+
EffectGuard
+
Observability
}
$$

其中 AI 模型只是節點內的一種能力提供者。

因此：

> 自治程度不應只看模型能推理多久，而應看整個系統在失敗、重啟、重試、延遲人工審核與重複觸發下，是否仍能維持一致狀態與可追溯責任。

這是從「AI 很會做」走向「系統可以長期交給 AI 做」的工程分界。

---

## 28. 下一階段

本 Runtime 完成後，下一個問題不是再增加更多自動化，而是決定：

> 哪些任務可以被允許進入哪一級自主狀態？

因此下一篇 EML-IIODO-WP-03 將建立：

# 《資訊收集任務難度、風險與自主等級規格 v0.1》

其核心輸入包括：

- 任務邊界清晰度；
- 可驗證性；
- 可逆性；
- 外部影響；
- 法律／安全風險；
- 資料敏感性；
- 錯誤成本；
- 是否允許 Human Gate 可選化。

也就是把本篇 Runtime 的能力，放進一個正式的授權框架中。

---

## 29. 參考資料與工程查核

本文件於 2026-08-01 重新查核以下現行資料，僅作工程能力參照，不代表本規格依賴單一框架：

1. LangChain / LangGraph Documentation, **Persistence**：Graph checkpoint、thread、state history、fault tolerance、replay、Store 與跨 thread 記憶。
   - https://docs.langchain.com/oss/python/langgraph/persistence
2. LangChain / LangGraph Documentation, **Interrupts**：持久化 Human-in-the-Loop、resume、interrupt 前副作用需冪等。
   - https://docs.langchain.com/oss/python/langgraph/interrupts
3. LangChain / LangGraph Documentation, **Fault tolerance / Graph API**：node retry policy、backoff、timeout、error handling 與成功節點寫入持久化。
   - https://docs.langchain.com/oss/python/langgraph/fault-tolerance
   - https://docs.langchain.com/oss/python/langgraph/use-graph-api
4. GitHub Actions Documentation, **Workflow syntax / schedule**：POSIX cron、IANA timezone、排程可能延遲與高負載注意事項。
   - https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
   - https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
5. Temporal Documentation：durable workflow、失敗後持續執行等長生命週期 workflow 工程參照。
   - https://docs.temporal.io/
6. Prefect Documentation, **States**：Scheduled、AwaitingRetry、Paused、Suspended、Resuming 等執行狀態可作工作流狀態機參照。
   - https://docs.prefect.io/v3/concepts/states

---

## 30. 結論

Scheduler–Loop–Graph Runtime 的真正價值不是「自動每天跑一次」，而是把原本依賴人類記得如何重複操作的流程，轉換成具有持續狀態與故障語義的執行系統。

對 AGIRight 這類資訊收集任務而言，最小可信 Runtime 不是：

$$
cron+LLM
$$

而是：

$$
\boxed{
\mathcal{R}
=
Scheduler
+
Graph
+
BoundedLoop
+
Persistence
+
HumanInterrupt
+
FaultRecovery
+
IdempotentEffects
+
Auditability
}
$$

這意味著「類未來」的下一步，不需要等待一個神奇的全自主 AGI。只要把時間、狀態、失敗、責任與副作用工程化，現代 AI 已能在有限領域中承擔更長期、更穩定的資訊管理工作。

但 Runtime 具備能力，不代表所有任務都應自動執行。

因此，真正下一個技術問題是權限與風險：

$$
\text{Can automate}
\neq
\text{May automate}
$$

這正是下一份白皮書的起點。
