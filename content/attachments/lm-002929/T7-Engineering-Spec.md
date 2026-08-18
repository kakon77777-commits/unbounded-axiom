# T7：EveGlyph Dynamic Logic Reference Implementation Handoff
## 從規格到第一個可執行 Demo 的工程交接

**版本：** v0.1  
**日期：** 2026-08-16  
**目標 Repo：** `kakon77777-commits/eveglyph-editor`

---

# 一、這一輪不要做什麼

不要：

1. 重寫 AIMD-C evaluator；
2. 重寫 dependency graph；
3. 把 Dynamic Logic 塞進 `aimd-assert`；
4. 讓 Markdown 自己被 runtime 反覆覆寫；
5. 一開始就做 Agent 自主網路搜尋；
6. 一開始就做複雜 Bayesian engine。

---

# 二、第一個 MVP 的唯一目標

做出一個畫面，能真實 replay：

$$
\boxed{
\Omega
\rightarrow
\top_p
\rightarrow
\Omega
\rightarrow
\bot_p.
}
$$

而每次 transition 都有 event reason。

只要這個成功，理論就第一次被真正渲染。

---

# 三、建議新模組

```text
src/dynamiclogic/
├─ schemas.js
├─ validate.js
├─ reducer.js
├─ store.js
├─ projection.js
├─ replay.js
├─ render.js
└─ index.js
```

---

# 四、Reducer 是核心

Reducer 必須：

```text
pure-ish
deterministic
versioned
tested
```

概念：

```javascript
function reduceJudgment(state, event, policy) {
  switch (event.type) {
    case "CLAIM_CREATED":
      return ...
    case "EVIDENCE_ADDED":
      return ...
    case "STATE_CLOSED_TRUE":
      return ...
    case "STATE_REOPENED":
      return ...
  }
}
```

---

# 五、不要在 reducer 裡呼叫 LLM

LLM 是 event producer。

Reducer 是 event consumer。

即：

$$
\boxed{
\text{Stochastic Generation}
\rightarrow
\text{Validated Event}
\rightarrow
\text{Deterministic Mutation}.
}
$$

這是整個系統最重要的工程邊界之一。

---

# 六、Store

第一版可以：

```text
workspace/.eveglyph/dynamic-logic/events.jsonl
workspace/.eveglyph/dynamic-logic/state.json
```

event append。

state 是 cache。

---

# 七、Startup

啟動：

```text
read state cache
verify cursor/hash
if invalid:
    replay events
```

不要完全相信 state cache。

---

# 八、Claim Block

Parser 增加：

```text
aimd-claim
```

第一版只讀：

```yaml
id
statement
```

不要一次塞太多。

---

# 九、Evidence Block

增加：

```text
aimd-evidence
```

第一版：

```yaml
id
claim
direction
weight
verified
```

source graph 下一階段再補。

---

# 十、Judgment Block

增加：

```text
aimd-judgment
```

它不自己計算 arithmetic。

它引用：

- event store；
- policy；
- AIMD-C computation result。

---

# 十一、History Block

```text
aimd-history
```

第一版 renderer：

```text
simple vertical timeline
```

不用先做複雜 graph。

---

# 十二、Policy

硬編一份 default policy 也可以，但必須獨立物件：

```javascript
const DEFAULT_POLICY = {
  supportThreshold: 0.8,
  opposeThreshold: 0.2,
  minCompleteness: 0.5,
  reopenThreshold: 0.2
}
```

不能把 threshold 散落 UI。

---

# 十三、第一版 Score

為了 Demo，不需要完整 Bayesian inference。

可以先：

$$
S
=
\frac{\sum w_i^+}
{\sum w_i^+ + \sum w_i^-}
$$

並明確標：

```text
demo support score
not calibrated probability
```

避免假精確。

---

# 十四、Closure

若：

$$
S\geq0.8
$$

且 completeness 過門檻：

$$
G\rightarrow T_p.
$$

若重大 oppose evidence 加入：

$$
\Delta>\rho,
$$

則：

$$
T_p\rightarrow G.
$$

---

# 十五、Demo Event Sequence

準備四步：

### Event 1

建立 claim：

$$
S_0=O.
$$

### Event 2

加入兩個支持 evidence：

$$
O\rightarrow G.
$$

### Event 3

顯式 closure：

$$
G\rightarrow T_p.
$$

### Event 4

加入重大反證：

$$
T_p\rightarrow G.
$$

### Event 5

重新閉合：

$$
G\rightarrow F_p.
$$

---

# 十六、Replay UI

只要：

```text
[<] [Play] [>]  Event 3 / 5
```

以及 timeline。

不要先做華麗 animation。

---

# 十七、Formula View

沿用現有：

```text
aimd-view renderer="formula"
```

只需要讓 dynamic judgment state 可被 resolver 引用。

例如：

```text
@judge.posterior
```

---

# 十八、Reference Namespace

目前 AIMD-C：

```text
@id.field
```

可沿用。

Dynamic Logic block 需要暴露：

```text
@judge.state
@judge.projection
@judge.support
@judge.counterpressure
@judge.completeness
```

---

# 十九、Ledger

不要把既有 computation ledger 拆掉。

新增 judgment ledger。

連接：

```text
judgment event
  depends_on_computation: ledger-id
```

---

# 二十、錯誤處理

若 event invalid：

```text
do not append
show diagnostics
```

若 replay invalid：

```text
runtime_status = error
judgment state remains last known valid state
```

不能：

$$
\mathrm{ERROR}
\rightarrow\bot.
$$

---

# 二十一、Tests

至少：

```text
test_claim_created
test_evidence_moves_open_to_generating
test_close_true_requires_policy
test_reopen_true
test_close_false
test_error_not_omega
test_replay_same_state
test_model_output_replay_uses_committed_payload
```

---

# 二十二、Replay Golden Test

固定：

```text
fixtures/demo-events.jsonl
```

預期：

```text
final-state.json
```

每次改 reducer 跑：

$$
Replay(events)=expected.
$$

這是最重要的 regression test。

---

# 二十三、Backward Compatibility

AIMD-C 舊文件沒有 Dynamic Logic block 時：

$$
\text{behavior}_{new}
=
\text{behavior}_{old}.
$$

不能因新 runtime 破壞現有文件。

---

# 二十四、Feature Toggle

建議沿用 World Studio 經驗。

Settings：

```text
Enable Dynamic Logic
```

預設可先關閉。

避免基本 Markdown 使用者被複雜 UI 淹沒。

---

# 二十五、Monitor

新增：

```text
Dynamic Logic
```

diagnostics：

- event invalid；
- replay mismatch；
- stale state cache；
- broken claim ref；
- unsupported schema version。

---

# 二十六、MCP

第一版不用立刻新增 MCP write tool。

等 reducer 與 schema 穩定後，再暴露：

```text
get_claim_state
append_evidence
replay_claim
```

寫操作必須正確標示 destructive / readOnly hints。

---

# 二十七、Definition of Done

MVP 完成條件：

1. Demo 文件可開；
2. Claim 可渲染；
3. Event sequence 可載入；
4. Current state 正確；
5. Replay 可前後移動；
6. $\Omega\rightarrow\top_p\rightarrow\Omega\rightarrow\bot_p$ 可重播；
7. formula view 隨 replay state 改變；
8. reload 後 state 一致；
9. invalid event fail closed；
10. 舊 AIMD-C demo regression 無破壞。

---

# 二十八、後續再做

MVP 後：

```text
v0.2 evidence graph
v0.3 source independence
v0.4 Bayesian calibrated model
v0.5 hypothesis split
v0.6 multi-model lineage
v0.7 responsibility ledger
v1.0 public Bayesian Logic Judge
```

---

# 二十九、交接總式

$$
\boxed{
\text{不要先做一個「聰明 AI 判斷器」；
先做一個「永遠說得清楚自己為什麼變成現在這樣」的判斷 Runtime。}
}
$$

只要這個地基成立，AI 能力之後可以一直換。
