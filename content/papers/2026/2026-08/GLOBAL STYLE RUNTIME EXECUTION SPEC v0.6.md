# GLOBAL STYLE RUNTIME EXECUTION SPEC v0.6

## 1. 目標

v0.6 的目標，是在 v0.5 Runtime MVP 的基礎上，進一步補齊真正進入執行階段所需要的核心規格：

$$
Intent \to Search \to Compile \to Bind \to Package \to Queue \to Run \to Log \to Evaluate
$$

也就是正式把系統從：

```text
可組裝的 runtime 結構
```

推進到：

```text
可排程、可執行、可追蹤、可回饋的 execution runtime
```

---

## 2. 本版新增的核心問題

v0.5 已經回答：

- query 怎麼進來
- style search 怎麼做
- prompt 怎麼編譯
- GAR 怎麼綁定
- task packet 怎麼組

v0.6 要回答的，是更底層的執行問題：

1. **真正送出去跑的是什麼 packet？**
2. **不同 backend 怎麼共用統一中介格式？**
3. **queue / runner 怎麼排程？**
4. **結果怎麼記錄？**
5. **lineage 怎麼追蹤？**
6. **失敗與回饋怎麼回流？**

---

## 3. 統一執行包

本版引入 **Unified Execution Packet**，記為：

$$
E_u = (I, S, C, G, T, B, L, F)
$$

其中：

- $I$：Identity block
- $S$：Search block
- $C$：Compiled prompt block
- $G$：GAR binding block
- $T$：Task constraints block
- $B$：Backend target block
- $L$：Lineage block
- $F$：Feedback hooks

這個包不直接等於 ComfyUI 或 Diffusers 的原生格式，而是系統內部統一中介層。

---

## 4. Execution Runtime 模組

v0.6 建議在 v0.5 的六模組之外，再把 execution runtime 展開為六個執行模組：

### Module G — Packet Normalizer
把 AADS / Searcher / Compiler / GAR 的輸出整理成單一 packet。

### Module H — Backend Resolver
依照 backend profile 把統一包映射成：
- ComfyUI packet
- Diffusers config
- Internal AADS render task

### Module I — Queue Manager
負責：
- priority
- concurrency
- retry
- timeout
- cancellation

### Module J — Runner
真正將 packet 投遞給 backend，並輪詢或接收結果。

### Module K — Lineage Logger
記錄：
- input lineage
- packet lineage
- execution lineage
- output lineage

### Module L — Feedback Evaluator
負責把：
- success / failure
- user rating
- anti-homogenization score
- divergence score
- output metadata

再送回系統，用於之後的 refinement。

---

## 5. Queue 規格

Queue 的最小狀態建議為：

```text
queued
running
succeeded
failed
cancelled
retry_waiting
```

任一任務的執行狀態可表示為：

$$
q_t \in Q = \{queued, running, succeeded, failed, cancelled, retry\_waiting\}
$$

並建議至少支援：

- `priority`
- `retry_count`
- `max_retries`
- `timeout_seconds`
- `backend_affinity`
- `created_at`
- `updated_at`

---

## 6. Backend 映射原則

### 6.1 ComfyUI
映射成 workflow seed 或 workflow patch：
- model
- positive prompt
- negative prompt
- sampler
- seed
- adapter slots
- control slots

### 6.2 Diffusers
映射成 config template：
- model identifier
- prompt
- negative prompt
- steps
- guidance scale
- seed
- width / height
- optional adapters

### 6.3 AADS Internal
映射成內部 agent 任務：
- task id
- packet id
- target capability
- routing target
- result sink

---

## 7. Lineage 設計

Lineage 不是附屬功能，而是核心設計之一。因為這整套系統如果沒有 lineage，就很難回答：

- 這張圖是從哪個 query 來的？
- 用了哪個 style kernel？
- 哪個 prompt compiler 版本？
- 綁了哪個 model profile？
- 經過哪次 retry？
- 哪個 backend 產出？

因此本版建議每一個輸出都要能追溯到：

$$
(query, search, compile, bind, packet, execution, output)
$$

---

## 8. Feedback Loop

回饋迴路至少要收：

1. execution status
2. latency
3. output artifact metadata
4. user acceptance / rejection
5. anti-homogenization score
6. style divergence score
7. optional human notes

後續可以形成：

$$
Generate \to Observe \to Score \to Refine
$$

---

## 9. 失敗處理

v0.6 建議失敗不只記一個 `failed`，而要做失敗分類：

- `backend_timeout`
- `backend_reject`
- `invalid_packet`
- `missing_asset`
- `adapter_conflict`
- `quality_rejected`
- `unknown_error`

如此後續才能做：
- 自動 retry
- 自動 fallback backend
- 自動降低複雜度
- 自動更換 model profile

---

## 10. 成功條件

v0.6 的成功條件是：

1. 可以產生 unified execution packet。
2. 可以映射到至少 3 種 backend 目標格式。
3. 可以進入 queue。
4. 可以追蹤 execution state。
5. 可以記錄 lineage。
6. 可以回收 feedback metadata。

---

## 11. 後續 v0.7 方向

當 v0.6 完成後，v0.7 最自然的是：

- Runtime Benchmark Protocol
- Style Stability Metrics
- Output Scoring Pipeline
- Automatic Recompile / Rebind Loop
- Adaptive Backend Selection

也就是正式進入：

$$
Search \to Compile \to Run \to Evaluate \to Recompile
$$

---

## 12. 總結

v0.6 的重點，不只是把 packet 再細拆，而是讓整個系統真的具備：

```text
可送出
可執行
可排程
可追蹤
可回流
```

這樣你前面整套風格域、約束域、風格導航與 agentic control，才真正有一個工程上的執行底座。
