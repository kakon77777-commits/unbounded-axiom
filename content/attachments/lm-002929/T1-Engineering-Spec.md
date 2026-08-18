# T1：可執行動態邏輯 Runtime 規格
## Executable Dynamic Logic Runtime Specification

**版本：** v0.1  
**日期：** 2026-08-16  
**狀態：** Internal Technical Draft  
**對外科普別稱：** 貝葉斯邏輯判斷器（Bayesian Logic Judge）  
**注意：** 對外別稱不是完整技術定義。

---

# 1. 目標

本 Runtime 的目標不是計算一個靜態：

$$
P=\top
$$

或：

$$
P=\bot.
$$

而是持續維護：

$$
\boxed{
J(P,t)
}
$$

及其完整 transition history。

Runtime 最小輸出包括：

```text
current judgment state
support / counterevidence
evidence completeness
closure state
transition reason
history
provenance
```

---

# 2. 核心物件

## 2.1 Claim

```yaml
id: claim-001
statement: "..."
scope: "..."
created_at: "..."
```

形式：

$$
P_i.
$$

## 2.2 Evidence

```yaml
id: evidence-001
claim: claim-001
direction: support
source: "..."
source_type: primary
observed_at: "..."
weight: 0.8
verified: true
```

## 2.3 CounterEvidence

CounterEvidence 不建立成完全不同本體。

其實是：

$$
E_i
$$

帶：

$$
\operatorname{direction}(E_i)=\text{oppose}.
$$

## 2.4 JudgmentState

第一版建議：

```text
open
generating
provisionally_true
provisionally_false
conflicted
blocked
failed
```

對外三態投影：

$$
\Pi_3(S)
=
\begin{cases}
\top,&S=\text{provisionally\_true}\\
\bot,&S=\text{provisionally\_false}\\
\Omega,&\text{otherwise except failed}
\end{cases}
$$

其中 failed 是 runtime error，不是認識論真值。

## 2.5 Transition

```yaml
id: tr-001
claim: claim-001
from: generating
to: provisionally_true
trigger: evidence-004
reason: "closure threshold reached"
runtime_version: "..."
timestamp: "..."
```

## 2.6 Context

$$
\Gamma_t
$$

包含：

```text
domain
rules
thresholds
time window
source policy
risk policy
observer scope
```

## 2.7 Observer

$$
O_t
$$

表示：

- 可見資料；
- 權限；
- 代理角色；
- 模型；
- 利益衝突；
- 可用工具。

## 2.8 Invariant

$$
\mathcal I
$$

例如：

```text
history_must_not_be_erased
source_must_be_traceable
closure_must_be_reopenable
model_version_must_be_recorded
inference_must_not_pose_as_observation
```

---

# 3. Runtime 狀態函數

基本式：

$$
J(P,t)
=
F(
P,
E_{\leq t},
\Gamma_t,
O_t,
M_t,
\mathcal I
).
$$

第一版不要求 $F$ 是單一數學函數。

它可以是：

```text
deterministic rules
+ probabilistic scoring
+ AI evaluator
+ human override
```

但每一層必須可追溯。

---

# 4. Bayesian Layer

對外「貝葉斯邏輯判斷器」可保存：

$$
p_t(H)=P_t(H).
$$

若可合理定義 likelihood：

$$
P(E\mid H),
$$

則使用：

$$
P(H\mid E)
=
\frac{P(E\mid H)P(H)}
{P(E)}.
$$

但 Bayesian posterior 只是 runtime state 的一個欄位：

```yaml
bayesian:
  prior: 0.50
  posterior: 0.68
  likelihood_model: "..."
```

不能直接：

$$
0.68
\Rightarrow
\top.
$$

閉合仍受 policy 控制。

---

# 5. Closure Policy

例：

```yaml
closure:
  min_evidence_quality: 0.70
  min_source_independence: 0.60
  support_threshold: 0.80
  oppose_threshold: 0.20
  max_unresolved_major_conflicts: 0
```

若：

$$
\operatorname{CloseTrue}(S_t,\theta)=1,
$$

則：

$$
S_t
\rightarrow
\text{provisionally\_true}.
$$

注意：

$$
\boxed{
\text{provisionally\_true}
\neq
\text{metaphysically final true}.
}
$$

---

# 6. Reopen Policy

新證據：

$$
e_{new}
$$

進入後計算：

$$
\Delta(e_{new},S_t).
$$

若：

$$
\Delta>\rho,
$$

則：

$$
\text{provisionally\_true}
\rightarrow
\text{generating}.
$$

同理：

$$
\text{provisionally\_false}
\rightarrow
\text{generating}.
$$

---

# 7. Event Ledger

Runtime 採 event-sourced 優先設計。

事件：

```text
CLAIM_CREATED
EVIDENCE_ADDED
EVIDENCE_INVALIDATED
COUNTEREVIDENCE_ADDED
CONTEXT_CHANGED
MODEL_CHANGED
STATE_CLOSED_TRUE
STATE_CLOSED_FALSE
STATE_REOPENED
HYPOTHESIS_SPLIT
HYPOTHESIS_MERGED
FORMULA_REWRITTEN
RUNTIME_FAILED
```

canonical state 可由：

$$
S_t
=
\operatorname{Fold}
(
S_0,
e_1,\ldots,e_t
)
$$

重建。

---

# 8. Hypothesis Split

假說不是 immutable。

原命題：

$$
H
$$

可能因證據分裂：

$$
H
\rightarrow
\{
H_1,H_2,H_3
\}.
$$

事件：

```yaml
type: HYPOTHESIS_SPLIT
source: H
targets: [H1, H2, H3]
reason: "..."
```

這是本 Runtime 與普通 probability gauge 的重要差別。

---

# 9. Formula Rewrite

公式 AST 也可以有版本：

$$
f_t
\rightarrow
f_{t+1}.
$$

例如：

$$
J(P,t)=f(E_t)
$$

被修正為：

$$
J(P,t)=f(E_t,O_t,\Gamma_t).
$$

必須保存：

```text
old_ast
new_ast
rewrite_reason
author/agent
timestamp
```

---

# 10. Replay

任一 claim 必須支援：

```text
play
pause
step
rewind
jump-to-event
```

Replay 展示：

$$
S_0
\rightarrow
S_1
\rightarrow
\cdots
\rightarrow
S_t.
$$

---

# 11. Snapshot

靜態 MD／HTML／PDF 是：

$$
\operatorname{Snapshot}
(
J,
t_s
).
$$

Snapshot 必須標示：

```text
snapshot_time
runtime_version
source_hash
event_cursor
```

以免使用者把舊快照誤認為 current state。

---

# 12. Public Projection

科普模式：

```text
目前判定：仍在生成
支持度：67%
反證壓力：31%
證據完整度：54%
最後更新：...
```

進階模式：

```text
J(P,t)
Evidence Graph
Counterevidence
Bayesian state
Context
Transition History
Reopen Policy
Model Version
```

---

# 13. 錯誤與未知分離

必須區分：

$$
\Omega
$$

與：

$$
\mathrm{ERROR}.
$$

$\Omega$ 是合法認識狀態。

ERROR 是 runtime execution failure。

因此：

```text
generating != failed
conflicted != failed
blocked != false
```

---

# 14. 最小 API

```text
POST /claims
GET  /claims/{id}
POST /claims/{id}/evidence
POST /claims/{id}/context
POST /claims/{id}/evaluate
POST /claims/{id}/reopen
POST /claims/{id}/split
GET  /claims/{id}/history
GET  /claims/{id}/snapshot
GET  /claims/{id}/replay
```

---

# 15. 最小 CLI

```bash
dlj claim add
dlj evidence add
dlj evaluate <claim-id>
dlj state <claim-id>
dlj reopen <claim-id>
dlj history <claim-id>
dlj replay <claim-id>
dlj snapshot <claim-id>
```

---

# 16. Persistence

初期：

```text
SQLite + JSON/JSONL event log
```

建議表：

```text
claims
evidence
contexts
judgment_states
transitions
event_ledger
formula_versions
model_runs
snapshots
```

---

# 17. Deterministic / AI Boundary

能 deterministic 的：

- hash；
- timestamp；
- threshold；
- DAG；
- state transition validation；
- replay；
- schema validation；

不得交給 LLM 自由決定。

LLM 適合：

- evidence interpretation；
- alternative hypothesis generation；
- causal explanation；
- source summarization；
- conflict detection。

---

# 18. Inference / Evidence Boundary

核心不變量：

$$
\boxed{
\text{Inference}
\neq
\text{Evidence}.
}
$$

任何 AI 新生成假說：

```yaml
source_type: inference
```

不得偽裝：

```yaml
source_type: observation
```

---

# 19. MVP

第一個 MVP 只需要：

1. 一個 claim；
2. support / oppose evidence；
3. 三態 projection；
4. closure；
5. reopen；
6. event ledger；
7. replay；
8. formula/number live view。

即足以讓使用者直接看到：

$$
\boxed{
\text{判斷正在發生。}
}
$$

---

# 20. 與後續文件關係

T2：接 EveGlyph AIMD-C。  
T3：定義 Live Paper source format。  
T4：定義 visual renderer。  
T5：定義 Bayesian Logic Judge 科普 UI。
