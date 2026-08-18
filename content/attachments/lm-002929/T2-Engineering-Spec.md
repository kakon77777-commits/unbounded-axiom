# T2：EveGlyph Dynamic Logic Integration Spec
## 從 AIMD-C Computable Document 到 Executable Dynamic Logic Paper

**版本：** v0.1  
**日期：** 2026-08-16  
**目標專案：** `kakon77777-commits/eveglyph-editor`  
**原則：** 擴充既有 AIMD-C，不另造第二套計算核心。

---

# 1. 既有能力

截至 2026-08-16，EveGlyph AIMD-C 已具有：

```text
aimd-value
aimd-function
aimd-compute
aimd-assert
aimd-table
aimd-view
```

並具有：

- expression tokenizer / parser；
- recursive-descent evaluator；
- arithmetic；
- comparisons；
- Boolean operators；
- IF；
- named variables；
- assignment；
- cross-block references；
- dependency DAG；
- cycle detection；
- type checking；
- full-document live re-evaluation；
- computation ledger；
- inline reference substitution；
- formula / number / table / chart renderer。

因此：

$$
\boxed{
\text{Computable Document Core}
\text{ 已存在。}
}
$$

---

# 2. 不要重寫 evaluator

現有：

```text
src/aimdc/evaluator.js
```

應作為 L1 expression engine。

Dynamic Logic 不應另建第二套 evaluator 去重複：

- arithmetic；
- Boolean；
- variables；
- reference resolution。

新增層應位於 AIMD-C graph/evaluation 之上。

---

# 3. 建議新模組

```text
src/dynamiclogic/
├─ claim.js
├─ evidence.js
├─ state.js
├─ transition.js
├─ policy.js
├─ runtime.js
├─ replay.js
├─ projection.js
└─ ledger.js
```

---

# 4. 新 Block Types

## 4.1 `aimd-claim`

```markdown
::: aimd-claim {id="claim-demo"}
statement: "The intervention improves outcome."
initial_state: generating
:::
```

## 4.2 `aimd-evidence`

```markdown
::: aimd-evidence {id="ev-01" claim="@claim-demo" direction="support"}
source: "study-001"
weight: 0.72
verified: true
:::
```

## 4.3 `aimd-judgment`

```markdown
::: aimd-judgment {id="judge-01" claim="@claim-demo"}
policy: default
renderer: live
:::
```

## 4.4 `aimd-history`

```markdown
::: aimd-history {claim="@claim-demo"}
mode: timeline
:::
```

---

# 5. 第一版不要讓 Markdown 自己一直改寫

第一版的 canonical source：

```text
Markdown source
+
runtime event ledger
```

分離。

不要每來一筆 evidence 就自動修改正文。

因此：

$$
\boxed{
\text{Source}
\neq
\text{Runtime State}.
}
$$

這與 EveGlyph 現有「buffer 與 Runtime State 分離」的工程原則相容。

---

# 6. Runtime State

可新增：

```text
.eveglyph/runtime/dynamic-logic/
```

內容：

```text
events.jsonl
claims.json
snapshots/
```

---

# 7. Event Format

```json
{
  "event_id": "evt-...",
  "type": "EVIDENCE_ADDED",
  "claim_id": "claim-demo",
  "timestamp": "...",
  "payload": {},
  "runtime_version": "0.1.0"
}
```

---

# 8. State Projection

`projection.js` 將 runtime state 投影回 Preview。

例如：

```html
<div class="dynamic-judgment state-generating">
  ...
</div>
```

而不是把執行狀態寫回 Markdown。

---

# 9. 與 AIMD-C DAG 的接口

已有 graph：

$$
G_{AIMD}.
$$

Dynamic Logic 建立：

$$
G_J.
$$

第一版不必合成單一超圖。

只需要允許：

$$
G_J
\rightarrow
G_{AIMD}
$$

引用計算結果。

例如 evidence weight 可以來自：

```text
@meta-analysis.posterior
```

因此：

$$
\text{AIMD-C Compute}
\rightarrow
\text{Dynamic Judgment Evidence}.
$$

---

# 10. Formula View 動態化

現有：

```markdown
::: aimd-view {source="@result.area" renderer="formula"}
area
:::
```

已能生成：

$$
area=value.
$$

下一步新增：

```markdown
::: aimd-view {source="@judge-01.posterior" renderer="formula"}
P(H\mid E_t)
:::
```

render：

$$
P(H\mid E_t)=0.68.
$$

當 evidence 改變後：

$$
0.68
\rightarrow
0.74.
$$

---

# 11. 真正需要新增的是時間

目前 AIMD-C 每次 render 都重算，但沒有 first-class：

$$
t.
$$

需增加：

```text
runtime_clock
event_time
evaluation_time
snapshot_time
```

使：

$$
J(P,t)
$$

可以被 replay。

---

# 12. 真正需要新增的是 history

現有 AIMD-C ledger 已記：

```text
block
runtime
runtime_version
source_hash
input_hash
output_hash
deterministic
effects
```

這是一個很好的 seed。

Dynamic Logic ledger 再增加：

```text
event_id
claim_id
old_state
new_state
trigger
reason
model
evidence_cursor
```

---

# 13. 不要破壞既有 Computation Ledger

兩個 ledger 可先分層：

$$
L_C
=
\text{Computation Ledger},
$$

$$
L_J
=
\text{Judgment Ledger}.
$$

並以 reference 連接：

$$
L_J.event
\rightarrow
L_C.entry.
$$

---

# 14. Assertion 與 Judgment 不同

現有：

```text
aimd-assert
```

回答：

$$
\operatorname{Eval}(\phi)\in\{\text{true},\text{false}\}.
$$

新的：

```text
aimd-judgment
```

回答：

$$
J(P,t)\in\mathcal S_J.
$$

因此不能用 assert block 硬充 judgment。

---

# 15. `failed` 與 $\Omega$ 必須分開

現有 renderer 有：

```text
completed
failed
blocked
verified
```

Dynamic Logic 新增：

```text
generating
conflicted
provisionally_true
provisionally_false
reopened
```

其中：

$$
\Omega
$$

只能投影：

```text
generating
conflicted
reopened
```

等合法狀態。

不能：

$$
\mathrm{failed}
\mapsto
\Omega.
$$

---

# 16. Preview Modes

## Paper View

維持目前 Markdown Preview。

## Live Logic View

顯示：

```text
claim
current state
evidence
posterior
transition
```

## Replay View

時間滑桿：

$$
t_0,t_1,\ldots,t_n.
$$

---

# 17. 最小視覺元件

```text
JudgmentBadge
EvidenceStream
PosteriorMeter
ConflictMeter
TransitionTimeline
ReplaySlider
FormulaLiveView
```

---

# 18. 對外 Bayesian Logic Judge

可新增一個簡化 tab：

```text
Bayesian Judge
```

顯示：

```text
支持度
反證壓力
證據完整度
當前判定
```

Advanced：

```text
Open Dynamic Logic Inspector
```

---

# 19. MVP 開發順序

## Phase 1

- `aimd-claim`
- `aimd-evidence`
- runtime state
- judgment projection

## Phase 2

- closure policy
- reopen
- judgment ledger

## Phase 3

- replay view
- formula live view

## Phase 4

- Bayesian scoring
- multi-model judgment

## Phase 5

- hypothesis split
- formula AST rewrite
- evidence graph

---

# 20. 測試

至少包含：

## Test 1

初始：

$$
\Omega
$$

加入支持證據後仍：

$$
\Omega.
$$

## Test 2

跨 threshold：

$$
\Omega
\rightarrow
\top_p.
$$

## Test 3

重大反證：

$$
\top_p
\rightarrow
\Omega.
$$

## Test 4

重新閉合：

$$
\Omega
\rightarrow
\bot_p.
$$

## Test 5

runtime error：

$$
\mathrm{ERROR}
$$

不得投影成 $\bot$ 或 $\Omega$。

## Test 6

reload 後 replay history 完整一致。

---

# 21. Static Export

輸出 PDF 時：

$$
\operatorname{Snapshot}(t_s)
$$

固定。

PDF 頁腳或 metadata 應記：

```text
Dynamic Logic Snapshot
snapshot_time
runtime_version
event_cursor
```

避免把 snapshot 當成 current live state。

---

# 22. Canonical Source

正式資料來源：

$$
\boxed{
\text{UTF-8 Source}
+
\text{Runtime Event Ledger}
+
\text{Versioned Schema}.
}
$$

不能要求使用者從 Preview 或 PDF 反向複製作為 canonical source。

---

# 23. 與現有 EveGlyph 原則一致

目前 EveGlyph 已經存在：

- Preview；
- Runtime；
- World；
- Studio；
- Monitor；
- MCP；
- Visual IR；
- computation ledger。

Dynamic Logic 最適合作為：

$$
\boxed{
\text{新的 Runtime／Visual IR 能力層},
}
$$

而不是一個外掛式完全獨立產品。

---

# 24. 最終定義

$$
\boxed{
\text{EveGlyph Dynamic Logic}
=
\text{AIMD-C}
+
\text{Event-Sourced Judgment State}
+
\text{Replayable History}.
}
$$

當這一層成立時，EveGlyph 的文件不只會「算」。

它開始會：

> **形成判斷、改變判斷、解釋為何改變，並保存自己曾經如何判斷。**
