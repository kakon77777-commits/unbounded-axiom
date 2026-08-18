# T3：Executable Live Paper Format
## 可執行活論文的 Canonical Source、Runtime Sidecar 與 Snapshot Projection 規格

**版本：** v0.1  
**日期：** 2026-08-16  
**目標：** 定義「論文會動」時，什麼才是正式原稿、什麼只是執行狀態、什麼只是渲染快照。

---

# 1. 核心原則

傳統論文：

$$
\text{Source}
\rightarrow
\text{Render}
\rightarrow
\text{Read}.
$$

Live Paper：

$$
\boxed{
\text{Source}
\rightarrow
\text{Parse}
\rightarrow
\text{Compile}
\rightarrow
\text{Execute}
\rightarrow
\text{State}
\rightarrow
\text{Render}.
}
$$

其中：

$$
\boxed{
\text{Rendering View}
\neq
\text{Canonical Source}.
}
$$

---

# 2. 三層資料

## 2.1 Canonical Source Layer

正式 UTF-8 原稿：

```text
paper.md
schemas/
manifest.yaml
```

只允許原始文字／結構化 block。

數學 source 使用 canonical delimiter：

$$
\texttt{\$\$...\$\$}
$$

與：

$$
\texttt{\$...\$}.
$$

不得把渲染後 Unicode 數學字元反向當正式 source。

---

## 2.2 Runtime State Layer

例如：

```text
.runtime/
  events.jsonl
  state.json
  computations.jsonl
  judgments.jsonl
```

這些不是正文。

它們是：

$$
\text{execution state}.
$$

---

## 2.3 Projection Layer

```text
HTML
PDF
static Markdown snapshot
JSON export
interactive web view
```

均由：

$$
\operatorname{Project}(Source,State,t)
$$

產生。

---

# 3. 建議 Package

```text
live-paper/
├─ paper.md
├─ manifest.yaml
├─ schemas/
│  ├─ claim.schema.json
│  ├─ evidence.schema.json
│  └─ judgment.schema.json
├─ data/
│  └─ ...
├─ .runtime/
│  ├─ events.jsonl
│  ├─ state.json
│  └─ ledger/
├─ snapshots/
│  └─ ...
└─ checksums/
   └─ SHA256SUMS
```

---

# 4. Manifest

```yaml
format: eve-live-paper
format_version: "0.1"
source: paper.md
runtime:
  dynamic_logic: true
  aimdc: true
canonical_encoding: utf-8
math_delimiters:
  inline: "$...$"
  display: "$$...$$"
```

---

# 5. Document Frontmatter

```yaml
---
type: live-paper
status: draft
runtime: dynamic-logic
runtime_schema: "0.1"
snapshot_policy: explicit
---
```

---

# 6. Static Prose Remains Static

普通段落：

```markdown
此處為研究背景。
```

不應因 runtime 自動改寫。

第一版原則：

$$
\boxed{
\text{Runtime may change views,
not silently rewrite canonical prose.}
}
$$

---

# 7. Claim Block

```markdown
::: aimd-claim {id="h1"}
statement: "Intervention X improves Y."
scope:
  population: "..."
  time_window: "..."
:::
```

---

# 8. Evidence Block

正文可宣告固定 evidence：

```markdown
::: aimd-evidence {id="e1" claim="@h1" direction="support"}
source_id: study-001
weight: 0.72
verified: true
:::
```

若 evidence 是 runtime 取得，則 block 可以只引用：

```markdown
::: aimd-evidence-view {claim="@h1"}
source: runtime
:::
```

避免自動將外部資料寫回 canonical source。

---

# 9. Judgment Block

```markdown
::: aimd-judgment {id="j1" claim="@h1"}
policy: research-default
projection: triadic
:::
```

runtime 可輸出：

```text
state: generating
projection: Ω
support: 0.68
counterpressure: 0.29
```

---

# 10. Formula Block

沿用 AIMD-C：

```markdown
::: aimd-function {id="posterior"}
...
:::
```

與：

```markdown
::: aimd-view {source="@posterior.value" renderer="formula"}
P(H\mid E_t)
:::
```

因此畫面可顯示：

$$
P(H\mid E_t)=0.68.
$$

---

# 11. Formula AST Version

執行核心不得只保存渲染字串。

應保存：

```json
{
  "formula_id": "posterior",
  "ast_version": 3,
  "source_hash": "...",
  "ast_hash": "..."
}
```

若公式結構重寫：

$$
f_t
\rightarrow
f_{t+1},
$$

新增 event：

```text
FORMULA_REWRITTEN
```

---

# 12. Inline Dynamic Reference

沿用：

```text
{{ result.area }}
```

可以擴充：

```text
{{ j1.state }}
{{ j1.posterior }}
{{ j1.last_transition }}
```

但這些只是 render substitution。

不能寫回原稿把 placeholder 永久替換成值。

---

# 13. Runtime Event Sidecar

`events.jsonl`：

```json
{"type":"EVIDENCE_ADDED","claim_id":"h1","event_id":"evt1","timestamp":"..."}
{"type":"STATE_REOPENED","claim_id":"h1","event_id":"evt2","timestamp":"..."}
```

採 append-first。

---

# 14. State Cache

`state.json` 可以是可重建 cache：

```json
{
  "event_cursor": 182,
  "claims": {
    "h1": {
      "state": "generating"
    }
  }
}
```

若 cache 遺失：

$$
\operatorname{Replay}(events)
\rightarrow
state.
$$

---

# 15. Ledger 分層

## Computation Ledger

$$
L_C.
$$

記：

- formula；
- input；
- output；
- runtime version。

## Judgment Ledger

$$
L_J.
$$

記：

- claim；
- state transition；
- evidence cursor；
- reason；
- closure policy。

## Source Ledger

$$
L_S.
$$

記：

- source；
- hash；
- timestamp；
- provenance。

---

# 16. Snapshot

建立 snapshot：

```text
snapshots/
  2026-08-16T220000+08/
```

包含：

```text
paper.md
runtime-state.json
event-cursor.txt
rendered.html
optional.pdf
checksums
```

---

# 17. PDF Snapshot

PDF 必須標示：

```text
This PDF is a snapshot of a live paper.
Snapshot time:
Event cursor:
Runtime version:
```

因：

$$
\boxed{
\text{PDF}
=
\operatorname{Projection}(t_s),
}
$$

不是 live current state。

---

# 18. 靜態 MD Export

可以產生：

```text
paper.snapshot.md
```

其中 dynamic block 轉成固定值。

但開頭必須寫：

```yaml
generated_from_live_paper: true
snapshot_time: ...
```

---

# 19. Validation

正式 commit 前至少檢查：

- UTF-8 round-trip；
- math delimiter；
- JSON/YAML schema；
- block id uniqueness；
- reference resolution；
- DAG cycle；
- event ledger parse；
- snapshot cursor consistency。

---

# 20. Commit Rule

$$
\boxed{
\text{Validate}
\rightarrow
\text{Commit}.
}
$$

不得：

$$
\text{Render looks okay}
\Rightarrow
\text{source is valid}.
$$

---

# 21. External Effects

第一代 Live Paper 建議保持：

$$
L1=\text{pure compute}
$$

為主要核心。

若未來加入：

- network；
- filesystem；
- agent action；

必須進 permission layer。

---

# 22. Model Calls

AI analysis block 必須保存：

```text
provider
model
model_version
prompt_version
retrieval
timestamp
```

因：

$$
\text{model output}
$$

不是 eternal source truth。

---

# 23. Dynamic Text

未來可以允許：

```markdown
::: dynamic-section
...
:::
```

但 v0.1 不允許 AI 靜默改寫 canonical narrative。

建議先只動：

- value；
- state；
- graph；
- section projection。

---

# 24. Reproducibility

Live Paper 必須承認：

$$
\text{Executable}
\not\Rightarrow
\text{Reproducible}.
$$

所以 package 可選保存：

```text
runtime lockfile
dependency versions
container manifest
model manifest
data hashes
```

---

# 25. Minimal Example

```markdown
---
type: live-paper
runtime: dynamic-logic
---

# Demo

::: aimd-claim {id="h1"}
statement: "H is supported."
:::

::: aimd-value {id="prior" type="Number"}
0.5
:::

::: aimd-judgment {id="j1" claim="@h1"}
policy: demo
:::

目前狀態：**{{ j1.state }}**

::: aimd-view {source="@j1.posterior" renderer="formula"}
P(H\mid E_t)
:::

::: aimd-history {claim="@h1"}
mode: timeline
:::
```

---

# 26. 最終定義

$$
\boxed{
\text{Live Paper}
=
\text{UTF-8 Canonical Source}
+
\text{Executable Graph}
+
\text{Runtime State}
+
\text{Immutable-enough Ledger}
+
\text{Validated Projections}.
}
$$

這使論文可以動，但正式原稿不被畫面綁架。
