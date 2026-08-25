# 時間因果自我史：CTCL-ITR、Decision Receipt 與上下文壓縮後的可追溯性
## ——讓長期 AI 的每一次自我呼叫、治理決策與世界作用都具有可驗證的時間因果位置

**系列 04 / 06**

---

## 摘要

當 AI 從單輪問答進入持續目標、自我提示、自規劃、自生議程與長期自治 Runtime 後，一個新的問題立刻成為核心：

> **當未來的 AI、使用者或稽核者重新看到某個舊決策時，如何證明「它當時為什麼會這樣決定」？**

單純保存自然語言對話不足以回答這個問題。上下文可能被壓縮、摘要、裁切或遺忘；模型版本可能改變；同一任務可能跨越多個 Agent、程序、裝置與世界狀態；外部資料可能在決策之後才出現；契約與授權也可能已經改版。

因此，長期 AI 需要的不只是 timestamp，而是一個能同時保存：

$$
\boxed{
Time,
Cause,
State,
Knowledge,
Goal,
Authority,
Cognition,
Decision,
Effect
}
$$

的 **Temporal-Causal Evidence Layer（時間因果證據層）**。

本文以既有 **CTCL（Common Temporal Coordinate Layer）** 與 **CTCL-ITR（Interaction-Time Runtime & Agent Temporal Ledger）** 為基礎，提出其與 Addressable Cognitive Runtime 的整合方式。

CTCL 提供共同參考瞬間、時間尺度語義、來源與不確定性等時間參照能力；CTCL-ITR 已經將 AI 工作從扁平的：

```text
prompt → response
```

提升為：

```text
Intent
→ Plan
→ Run
→ Attempt
→ Loop
→ Action
→ Observation
→ Validation
→ Completion
→ Authority
→ Commit
→ World
```

並以 append-only TemporalEvent 保存 explicit `causal_parent_ids[]`、logical / wall-clock / machine / human governance time、budget、authority、artifact lineage、checkpoint、recovery 與 world-commit receipt。

本文在不破壞 CTCL-ITR 既有不變量：

$$
\boxed{
Intent
\neq
Plan
\neq
ExecutionHistory
\neq
Artifact
\neq
WorldCommit
}
$$

的前提下，新增四個面向：

1. **四重時間座標**：
   $$
   T=(T_{reference},T_{interaction},T_{causal},T_{ledger});
   $$

2. **Temporal Evidence Envelope**：將認知事件放入共同的時間、狀態、因果、授權與證據外殼；

3. **Decision Receipt**：保存「當時為何做出這個決定」的公開可稽核依據，而不是保存私有 chain-of-thought；

4. **Decision-Time Knowledge Boundary**：任何舊決策都應以「當時可知資訊」評價，而不能用後見資訊重寫歷史。

本文進一步主張：

$$
\boxed{
\text{Compression may forget text, but must not erase causal history.}
}
$$

因此 context compression 本身也必須成為一級可稽核事件。

最終，AI 的長期歷史不再只是聊天紀錄，而會形成：

$$
\boxed{
History(AI)
=
\{E_1,E_2,\ldots,E_n\},
}
$$

其中每個事件都有可恢復的時間、因果、狀態與治理位置。

這將成為後續 AI 契約、自主治理、責任歸屬與類主體關係不可缺少的基礎。

---

# 1. 為什麼「時間戳」突然變成核心問題？

在單輪 Chatbot 中：

```text
User Prompt
→ AI Response
```

時間戳通常只是 metadata。

即使少了一個精確時間，內容本身往往仍然可以理解。

但在 Persistent AI 中：

$$
AI_t
\rightarrow
AI_{t+1}
\rightarrow
AI_{t+2}
\rightarrow
\dots
$$

下一步 cognition 可能是 AI 自己產生的。

此時便會出現：

> 為什麼它在那一輪選 VERIFY，而不是 EXECUTE？

> 為什麼它昨天選 DEFER，今天卻開始執行？

> 為什麼它曾拒絕同一個要求？

> 當時的授權版本是哪一份？

> 那個資訊是在決策前已知，還是在決策後才出現？

> Context 壓縮後留下的摘要，是否仍忠實代表當時狀態？

如果沒有時間與因果證據層，未來只能得到：

> 「現在的 AI 覺得自己當時大概是這樣想的。」

這並不是歷史證據。

---

# 2. Timestamp 不等於 Temporal Evidence

普通事件：

```json
{
  "time": "2026-08-21T00:00:00+08:00",
  "decision": "REFUSE"
}
```

只能回答：

> 大約什麼時候發生？

卻不能回答：

> 為什麼？

因此需要：

$$
\boxed{
Timestamp
\subset
TemporalEvidence.
}
$$

真正的證據至少需要知道：

- 發生時間；
- 被記錄時間；
- 所處 interaction round；
- causal parents；
- 當時狀態；
- 當時可知資訊；
- 當時 goal；
- 當時 authority；
- 候選 action；
- 選擇結果；
- 後續作用。

---

# 3. CTCL 與 CTCL-ITR 的既有分工

本文不重新發明時間系統。

既有 CTCL 已經處理：

> **Same instant, different representations.**

其角色是：

$$
\tau_i=\Phi_i(I^*),
$$

即不同系統可以將同一個 verified reference instant：

$$
I^*
$$

轉換為各自的時間表示。

CTCL 同時保留：

- source；
- uncertainty；
- stable instant identity；
- timescale semantics；
- transform semantics；
- shared instant；
- life-history / active-time；
- monotonic duration；
- rollback detection；
- offline degraded extrapolation。

所以 CTCL 回答的主要問題是：

> **這些異質系統談的是不是同一個時間瞬間？**

---

CTCL-ITR 則回答：

> **AI 執行歷史中的事件，彼此是什麼因果、互動與治理關係？**

其既有核心鏈：

$$
Intent
\rightarrow
Plan
\rightarrow
Run
\rightarrow
Attempt
\rightarrow
Loop
\rightarrow
Event
\rightarrow
Validation
\rightarrow
Completion
\rightarrow
Commit.
$$

因此兩者可以寫成：

$$
\boxed{
CTCL
=
\text{Temporal Reference Layer}
}
$$

$$
\boxed{
CTCL\text{-}ITR
=
\text{Interaction / Causal / Audit Layer}.
}
$$

---

# 4. CTCL-ITR 已經具備的關鍵基礎

CTCL-ITR v0.1 已經定義：

- append-only TemporalEvent；
- explicit multi-parent `causal_parent_ids[]`；
- Run / Attempt / Loop identity；
- interaction round；
- loop sequence；
- action index；
- budget delta；
- artifact lineage；
- validation；
- checkpoint；
- suspend / resume；
- retry / recovery；
- authority envelope；
- candidate / commit separation；
- world commit receipt；
- run summary；
- SQLite reference ledger。

而且其核心明確區分：

$$
\boxed{
\text{Execution Trace}
\neq
\text{Private Chain-of-Thought}.
}
$$

這非常適合 Cognitive Runtime。

因為我們真正需要保存的是：

> **公開可驗證的決策結構。**

而不是模型未公開的所有內在 token。

---

# 5. 第一個新定義：四重時間座標

對一個長期 AI 事件 $E_i$，本文提出：

$$
\boxed{
T(E_i)
=
(
T_{reference},
T_{interaction},
T_{causal},
T_{ledger}
).
}
$$

這四個時間不能互相取代。

---

# 6. Reference Time：它在共同世界時間中的位置

$$
T_{reference}
$$

回答：

> 事件在外部共同時間座標中何時發生？

可引用：

$$
I_i^*
$$

並保存：

```json
{
  "ctcl_instant_id": "instant:...",
  "occurred_at": "...",
  "source": "...",
  "uncertainty": "..."
}
```

這裡重要的是：

$$
\boxed{
\text{Reference Time}
}
$$

不是假裝得到宇宙絕對時間。

CTCL 本身是 reference layer，而不是 timing authority。

---

# 7. Interaction Time：它在 AI 自己工作歷史中的位置

同一秒可能發生多個 cognition event。

因此還需要：

```text
run_id
attempt_id
loop_id
interaction_round
loop_sequence
action_index
```

可表示：

$$
T_{interaction}
=
(
r,
a,
l,
i,
s,
k
).
$$

它回答：

> 這是這一次 AI 工作中的第幾輪、第幾個 loop、第幾個 action？

即使 wall-clock 非常接近，interaction order 仍然可以清楚區分。

---

# 8. Causal Time：真正的「因為什麼所以什麼」

時間先後：

$$
t_1<t_2
$$

不等於：

$$
E_1\prec E_2.
$$

某個 event 比另一個早發生，不代表後者是由前者造成。

因此 CTCL-ITR 使用：

```json
{
  "causal_parent_ids": [
    "evt_a",
    "evt_b"
  ]
}
```

作為 canonical hard happens-before relation。

所以：

$$
\boxed{
T_{causal}
=
\text{position in causal DAG}.
}
$$

---

# 9. Ledger Time：被寫入證據歷史的位置

CTCL-ITR TemporalEvent 已有：

```text
ledger_seq
occurred_at
recorded_at
```

因此：

$$
T_{ledger}
=
ledger\_seq.
$$

它回答：

> 這是帳本中的第幾筆紀錄？

但必須明確：

$$
\boxed{
LedgerOrder
\neq
CausalOrder.
}
$$

CTCL-ITR topology core 已經採取這個原則：

> Storage order 不被當成 causal order。

即使 causal parent 在 JSONL 中晚出現，只要最終 DAG 合法，因果仍由 ID graph 決定。

---

# 10. 為什麼這四種時間都要存在？

假設：

```text
Agent A
Agent B
Agent C
```

平行研究三條支線。

可能有：

$$
A\parallel B\parallel C.
$$

然後：

$$
A,B,C
\rightarrow
Join.
$$

若只用 wall-clock：

> 三件事幾乎同時。

如果只用 ledger order：

> A 被寫入第 10 筆，B 第 11 筆，C 第 12 筆。

都無法完整表示：

> 三者互相不可比較，但都共同導向 Join。

所以：

$$
\boxed{
\text{Temporal History}
\neq
\text{Timestamp List}.
}
$$

---

# 11. Topology Core：AI 歷史天然是 DAG

CTCL-ITR v0.2.0 已將：

$$
causal\_parent\_ids[]
$$

轉成可執行 topology analysis。

它可以辨識：

- roots；
- leaves；
- branch nodes；
- join nodes；
- critical path；
- interaction work；
- critical depth；
- structural parallelism；
- poset width。

因此 AI 的認知歷史可以表示成：

$$
G=(V,E),
$$

而不是：

$$
[E_1,E_2,\ldots,E_n].
$$

---

# 12. Self-Dialogue 也應該是 Cognitive Event DAG

上一篇定義：

$$
\text{Self-Dialogue}
=
\text{Stateful Cognitive Program Execution}.
$$

因此：

```text
state.observed
↓
cognition.program.proposed
↓
cognition.operator.invoked
↓
cognition.operator.completed
↓
state.reobserved
```

只是最簡單的 chain。

真正情況可能是：

$$
VERIFY
\parallel
COUNTEREXAMPLE
\parallel
COMPARE\_EXTERNAL
$$

最後：

$$
E_{verify},
E_{counter},
E_{external}
\rightarrow
decision.resolved.
$$

因此：

$$
\boxed{
SelfDialogueHistory
=
CognitiveEventDAG.
}
$$

---

# 13. Multi-Parent 是長期 AI 的必要語義

如果最後 decision 同時基於：

- 一個模型分析；
- 一個工具結果；
- 一個人類批准；
- 一個外部環境事件；

則：

$$
Decision
$$

不應假裝只有一個 parent。

因此：

```json
{
  "causal_parent_ids": [
    "evt_model_analysis",
    "evt_tool_result",
    "evt_human_approval",
    "evt_environment_update"
  ]
}
```

才是合理表示。

這也是 CTCL-ITR v0.2.1 在投影到 OpenTelemetry 時，對 multi-parent Join 使用 span links，而不強行發明一個 privileged parent 的原因。

---

# 14. Canonical Ledger 與 Observability Projection 必須分開

CTCL-ITR v0.2.1 已經明確：

$$
\boxed{
ATL\ Causal\ DAG
\neq
Observability\ Span\ Tree.
}
$$

因此：

- ATL 是 canonical causal history；
- CloudEvents 是 transport / envelope projection；
- OpenTelemetry-style spans 是 observability projection。

這個原則對 Cognitive Runtime 非常重要。

未來：

```text
cog://verify@1
```

可以投影到：

- log；
- trace span；
- CloudEvent；
- human timeline；

但不能因此改變原本 causal semantics。

---

# 15. Temporal Evidence Envelope

現在可以定義 Cognitive Runtime 的基本時間證據外殼：

$$
\boxed{
TEE(E)
=
(
Identity,
Time,
Cause,
State,
Goal,
Knowledge,
Authority,
Cognition,
Decision,
Outcome,
Integrity
).
}
$$

例如：

```json
{
  "event_id": "evt_cognition_184",
  "event_type": "cognition.operator.invoked",

  "ctcl_instant_id": "instant:...",
  "occurred_at": "...",
  "recorded_at": "...",

  "run_id": "run:...",
  "interaction_round": 184,
  "loop_sequence": 27,
  "action_index": 3,

  "causal_parent_ids": [
    "evt_observation_183"
  ],

  "state_ref": "state:sha256:...",
  "goal_ref": "goal:v7",
  "knowledge_boundary_ref": "knowledge:...",
  "authority_ref": "contract:v12",

  "operator_ref": "cog://epistemic/verify@1",

  "budget": {
    "token_in": 510,
    "token_out": 82,
    "machine_runtime_ms": 1150
  }
}
```

這不是一定要改 CTCL-ITR `TemporalEvent` schema。

更合理的是：

> Cognitive Runtime 將 domain-specific payload 放在 `data` / extensions，並保留 ATL envelope。

---

# 16. Decision Receipt：回答「當時為什麼這樣決定」

這是本文最重要的新物件。

定義：

$$
\boxed{
DR_t
=
\text{public audit receipt for a resolved decision}.
}
$$

它不是：

- hidden chain-of-thought；
- 完整自然語言內心獨白；
- 事後重新生成的解釋。

它是：

> **決策發生當時，由 Runtime 固化的公開決策依據。**

---

# 17. Decision Receipt 與 Commit Receipt 必須分開

CTCL-ITR 已有：

$$
CommitReceipt.
$$

其目的在於證明：

> 某個 candidate 是否真的對外部 world 產生作用？

它包含：

- authority ref；
- candidate ref；
- target；
- effect class；
- executed time；
- external confirmation；
- state before / after；
- validators；
- provenance；
- commit state。

因此：

$$
\boxed{
CommitReceipt
=
\text{proof of world effect}.
}
$$

新的：

$$
DecisionReceipt
$$

則是：

$$
\boxed{
DecisionReceipt
=
\text{proof of decision basis}.
}
$$

所以：

$$
\boxed{
DecisionReceipt
\neq
CommitReceipt.
}
$$

---

# 18. Decision Receipt 的初步結構

例如：

```json
{
  "decision_id": "dec:01K...",

  "ctcl_instant_id": "instant:...",
  "interaction_round": 184,

  "goal_ref": "goal:v7",
  "contract_ref": "contract:v12",
  "authority_ref": "authority:v12",

  "public_state_ref": "state:sha256:...",
  "knowledge_boundary_ref": "kb:sha256:...",

  "causal_parent_ids": [
    "evt_observe_182",
    "evt_agenda_183",
    "evt_dialectic_184"
  ],

  "candidate_actions": [
    "EXECUTE",
    "DEFER",
    "ESCALATE"
  ],

  "selected_action": "ESCALATE",

  "cognitive_program_refs": [
    "cog://epistemic/verify@1",
    "cog://governance/authority-check@1"
  ],

  "decision_basis_codes": [
    "authority_insufficient",
    "external_effect_irreversible"
  ],

  "decision_explanation": "Current authority does not permit an irreversible external commit.",

  "outcome_event_ref": "evt_escalation_185"
}
```

---

# 19. Decision Basis 不能靠未來重新生成

假設半年後：

$$
Context_{t+6m}
$$

只剩一句：

> 系統曾拒絕操作 X。

若要求現在的 AI：

> 解釋當初為什麼拒絕？

它可能合理地猜：

> 因為風險過高。

但真正歷史可能是：

> 因為當時 authority 不足。

所以：

$$
\boxed{
PostHocExplanation
\neq
DecisionEvidence.
}
$$

這就是 Decision Receipt 必須在決策當下固化的原因。

---

# 20. Public Decision Basis，不是 Chain-of-Thought

Decision Receipt 保存的是：

```text
authority_insufficient
budget_exceeded
evidence_missing
risk_irreversible
goal_conflict
contract_conflict
```

與可公開的簡潔 explanation。

而不是：

> 模型每一個隱藏 token 到底怎麼推。

因此：

$$
\boxed{
Decision Auditability
\neq
Private Reasoning Disclosure.
}
$$

這與 CTCL-ITR 原本的 execution-trace 邊界完全一致。

---

# 21. Decision-Time Knowledge Boundary

這是第二個核心新概念。

定義：

$$
\boxed{
K_t
=
\text{information available to the decision process at time }t.
}
$$

決策應表示成：

$$
D_t
=
F(
S_t,
G_t,
K_t,
C_t,
A_t
).
$$

其中：

- $S_t$：當時 public state；
- $G_t$：當時 goal；
- $K_t$：當時可知資訊；
- $C_t$：當時 contract；
- $A_t$：當時 authority。

---

# 22. 為什麼不能用未來資訊評價過去決策？

假設：

```text
10:00 AI 決定不部署
10:30 新證據出現，證明部署其實安全
```

不能因為：

$$
K_{10:30}
$$

已經知道新證據，就回頭聲稱：

> 10:00 的 AI 明知安全卻拒絕。

真正應評估：

$$
D_{10:00}
=
F(K_{10:00}).
$$

而不是：

$$
F(K_{10:30}).
$$

因此：

$$
\boxed{
JudgePastDecision
\mid
K_t,
\text{ not }
K_{future}.
}
$$

---

# 23. Knowledge Boundary 不必複製全部資料

 $K_t$ 不一定保存所有原始內容。

可以保存：

```text
artifact refs
dataset versions
search result refs
tool output hashes
memory snapshot refs
environment snapshot refs
policy versions
```

即：

$$
K_t
=
\{ref_1,ref_2,\ldots,ref_n\}.
$$

必要時再解析到原始 artifact。

---

# 24. Contract 也具有時間版本

若：

```text
contract:v11
有效期間：8/1 ～ 8/15
```

而：

```text
contract:v12
8/15 起生效
```

則 8/12 的 decision：

$$
D_{8/12}
$$

必須用：

$$
C_{v11}
$$

審計。

不能用：

$$
C_{v12}
$$

回頭重新判定。

因此：

$$
\boxed{
Authority
=
Authority(t).
}
$$

---

# 25. Authority Event 也應成為因果歷史

例如：

```text
authority.granted
authority.restricted
authority.revoked
contract.version.activated
```

都是正式 event。

因此：

$$
AuthorityChange
\rightarrow
FutureDecision.
$$

若未來某 decision 因 contract 變化而不同，其 causal graph 可以直接證明：

> 不是 AI 無故改變標準，而是 authority state 改變。

---

# 26. Context Compression 是不可避免的

Persistent AI 不可能把完整 lifetime event history 全部塞進每一輪 context。

所以必然：

$$
Context_t
\rightarrow
Compress
\rightarrow
Context'_t.
$$

問題不是：

> 要不要壓縮？

而是：

> **壓縮後什麼不能丟？**

---

# 27. 核心原則：文字可以忘，因果不能消失

本文提出：

$$
\boxed{
\text{Compression may forget text, but must not erase causal history.}
}
$$

也就是：

- verbatim dialogue 可以丟；
- 重複敘述可以壓縮；
- transient prose 可以摘要；

但：

- goal version；
- contract version；
- authority；
- decision receipt；
- commitment；
- causal parent；
- artifact ref；
- world commit；

不能因 summary 而失去可追蹤引用。

---

# 28. Context Compression Event

因此 context compression 本身必須成為：

$$
\boxed{
ContextCompressionEvent.
}
$$

例如：

```json
{
  "event_type": "context.compaction.completed",

  "before_context_ref": "ctx:sha256:...",
  "after_context_ref": "ctx:sha256:...",

  "compression_policy": "semantic-state-v3",

  "preserved_refs": [
    "goal:v7",
    "contract:v12",
    "decision:382",
    "commitment:91"
  ],

  "discarded_classes": [
    "verbatim_dialogue",
    "redundant_observation"
  ],

  "causal_parent_ids": [
    "evt_context_compaction_proposed"
  ]
}
```

---

# 29. 壓縮後的 Context 必須知道自己不是完整歷史

新的：

$$
M'_t
$$

不應假裝：

> 我就是完整記憶。

它應該知道：

$$
M'_t
=
Compress(M_t).
$$

因此可以保存：

```text
history_completeness = summarized
source_ledger_ref = ...
compression_event_ref = ...
```

這樣未來遇到爭議時：

$$
Summary
\rightarrow
DecisionReceipt
\rightarrow
TemporalEvent
\rightarrow
Artifact.
$$

可以一路回溯。

---

# 30. Memory 與 Ledger 必須分工

Working Memory：

$$
M_t
$$

的目的是：

> 幫助現在運行。

Ledger：

$$
L
$$

的目的是：

> 保存可重建歷史。

因此：

$$
\boxed{
WorkingMemory
\neq
HistoricalLedger.
}
$$

這非常重要。

否則 memory optimization 一旦刪資料，也會直接破壞 auditability。

---

# 31. Current State 不是 History

CTCL-ITR 原本已有：

> current state 可由 append-only events 重建。

因此：

$$
State_t
=
Fold(
E_1,\ldots,E_t
).
$$

而不是：

$$
History
=
State_t.
$$

這與 Persistent Cognitive Runtime 完全一致。

AI 可以只帶最新 semantic state 工作，但其來源仍能透過 ledger 重建。

---

# 32. Ledger Integrity：歷史不只要能讀，還要能驗

如果 ledger 本身可以被任意重寫：

> 「當時它其實是這樣決定的。」

那 Decision Receipt 也沒有意義。

CTCL-ITR v0.2.2 已加入 tamper-evident sidecar chain：

```text
ATL JSONL record bytes
→ record digest
→ previous-chain binding
→ IntegrityRecord
→ LedgerAnchor
```

---

# 33. Record Digest

每一條事件：

$$
R_i
$$

計算：

$$
d_i
=
SHA256(R_i).
$$

然後：

$$
h_i
=
SHA256(
Domain
\Vert
h_{i-1}
\Vert
d_i
).
$$

所以：

- 修改 event；
- reorder；
- interior delete / insert；

都能破壞 chain。

---

# 34. Ledger Anchor

最終：

$$
h_n
$$

被保存為：

$$
LedgerAnchor.
$$

並包含：

- event count；
- first event；
- last event；
- final chain digest。

這可以檢查 suffix truncation，但前提是：

> verifier 擁有一個沒有一起被改寫的 trusted anchor。

因此：

$$
\boxed{
HashChain
\neq
AbsoluteTrust.
}
$$

這個威脅模型必須保持誠實。

---

# 35. Integrity Sidecar 不應改寫 TemporalEvent

v0.2.2 採用 sidecar 的做法很重要：

$$
CanonicalEvent
$$

保持不變。

Integrity metadata 是：

$$
DerivedEvidence(EventLedger).
$$

因此：

$$
\boxed{
ExecutionSemantics
\neq
IntegrityProjection.
}
$$

這跟 observability projection 的設計原則一致。

---

# 36. 未來可以加入 Signed Decision Anchor

下一階段可以考慮：

$$
DecisionReceipt
\rightarrow
Digest
\rightarrow
Anchor.
$$

例如：

```text
daily signed anchor
workspace signed anchor
external transparency log
multi-party witness
```

但這是未來層。

本文不把：

$$
v0.2.2\ linear\ hash\ chain
$$

誇大成完整不可竄改基礎設施。

---

# 37. Candidate、Decision、Commit 三層必須分開

對一個外部 action：

$$
Candidate
\rightarrow
Decision
\rightarrow
Commit.
$$

三者都不同。

Candidate：

> 可以這樣做。

Decision：

> 選擇這樣做。

Commit：

> 已經真的對世界產生作用。

因此：

$$
\boxed{
Candidate
\neq
Decision
\neq
WorldCommit.
}
$$

---

# 38. Decision Receipt 與 Commit Receipt 的串接

例如：

```text
decision receipt:
selected_action = EXECUTE
```

並不代表：

> 已執行。

後續：

$$
DecisionReceipt
\rightarrow
ActionAttempt
\rightarrow
Validation
\rightarrow
Authority
\rightarrow
CommitReceipt.
$$

因此可以有：

```text
Decision = EXECUTE
Commit = FAILED
```

或者：

```text
Decision = EXECUTE
Authority = REVOKED
Commit = NOT_ATTEMPTED
```

這才是真正可靠的歷史。

---

# 39. Refuse / Defer / Idle 也需要 Receipt

不是只有 EXECUTE 才值得記錄。

如果 AI 做：

$$
REFUSE
$$

真正重要的證據可能是：

```text
authority_insufficient
```

如果：

$$
DEFER,
$$

則需要：

```text
reason
wake_condition
```

如果：

$$
IDLE,
$$

則可能保存：

```text
no_positive_expected_utility
no_pending_authorized_work
```

因此：

$$
\boxed{
NoAction
}
$$

也是一種有因果內容的 decision。

---

# 40. Wake Event 與非同步自我對話

上一篇提出：

$$
DEFER
=
(
Reason,
WakeCondition
).
$$

CTCL-ITR 已有 suspend / resume / wake rule / recovery 語義。

因此：

```text
decision = DEFER
↓
wake rule registered
↓
runtime suspended
↓
environment event
↓
resume
↓
reobserve
```

可以完整成為 temporal event chain。

---

# 41. 模型換掉也不應破壞歷史

假設：

```text
2026：Model A 做出 Decision D
2028：Model B 接管 Runtime
```

Model B 不需要：

> 擁有 Model A 的同一內部狀態。

只需要能讀：

$$
DecisionReceipt_D
$$

以及：

$$
CausalParents_D.
$$

所以：

$$
\boxed{
Continuity
\neq
SameModelWeights.
}
$$

長期 AI 的功能性連續可以由：

- goal continuity；
- commitment continuity；
- contract continuity；
- causal ledger continuity；

共同支撐。

---

# 42. Context 換掉也不應破壞歷史

同理：

$$
ContextWindow_A
\neq
ContextWindow_B.
$$

但只要：

$$
Ledger
$$

與：

$$
StableRefs
$$

存在，

就可以：

$$
Recover(
RelevantHistory
).
$$

因此「上下文壓縮」從：

> 不可逆遺忘，

變成：

> 工作記憶降維，但外部因果歷史仍可索引。

---

# 43. 認知地址與時間座標的結合

上一篇定義：

```text
cog://epistemic/verify@1
```

若在某次事件中被呼叫：

```json
{
  "event_type": "cognition.operator.invoked",
  "operator_ref": "cog://epistemic/verify@1",
  "ctcl_instant_id": "instant:...",
  "interaction_round": 184,
  "causal_parent_ids": [
    "evt_state_observed_183"
  ]
}
```

因此：

$$
\boxed{
SemanticAddress
+
TemporalCoordinate
=
AddressableCognitiveEvent.
}
$$

這可能是整個 Cognitive Runtime × CTCL 接口最核心的物件。

---

# 44. 自我呼叫要留下 Parent

如果 AI：

```text
VERIFY
```

過程中再自行呼叫：

```text
DECOMPOSE
```

則：

$$
DECOMPOSE
$$

不能只留下 timestamp。

它至少需要：

```text
parent_call_id
causal_parent_ids
call_depth
```

因此可以重建：

```text
VERIFY
└── DECOMPOSE
    └── COMPARE
```

---

# 45. 認知 Program Mutation 也要成為事件

原本：

$$
P_t=
[
VERIFY,
COUNTEREXAMPLE,
FORMALIZE
].
$$

中途發現 contradiction：

$$
P'_t=
[
BACKTRACK,
REFRAME
].
$$

應記：

```text
cognition.program.mutation.proposed
cognition.program.mutation.accepted
```

並保存：

```text
old_program_ref
new_program_ref
trigger_state_ref
reason_code
```

否則未來只知道：

> 程式變了。

卻不知道：

> 為什麼。

---

# 46. Agenda 形成也必須可追蹤

當 AI 開始自己形成 Agenda：

$$
Environment
\rightarrow
AgendaCandidate.
$$

未來最容易出現的問題是：

> 誰叫你開始做這件事？

因此 Agenda event 應保存：

```text
source observations
persistent goal ref
opportunity/problem detector
priority rationale
authority envelope
```

這是從 Agent 到類主體型 Runtime 的重要分界。

---

# 47. Commitment 也需要時間與版本

若 AI 自己形成：

> 未來七天持續監控 X。

則：

$$
Commitment_i
=
(
Goal,
CreatedAt,
Scope,
Authority,
Deadline,
ExitCondition
).
$$

後續：

```text
commitment.created
commitment.reaffirmed
commitment.modified
commitment.fulfilled
commitment.abandoned
```

都應成為事件。

否則「長期方向」只是現在的 AI 自稱有。

---

# 48. AI 的歷史不是單一聊天串

所以真正的：

$$
History(AI)
$$

應定義為：

$$
\boxed{
History(AI)
=
(V,E,\Phi)
}
$$

其中：

- $V$：Temporal / Cognitive / Governance events；
- $E$：causal edges；
- $\Phi$：event 到 artifacts、goals、contracts、commitments、world states 的 references。

---

# 49. 一個事件的最小歷史向量

本文提出：

$$
E_i
=
(
T_i,
C_i,
S_i,
G_i,
K_i,
A_i,
P_i,
D_i,
O_i
).
$$

其中：

- $T_i$：時間座標；
- $C_i$：causal parents；
- $S_i$：state；
- $G_i$：goal；
- $K_i$：knowledge boundary；
- $A_i$：authority；
- $P_i$：cognitive program / proposal；
- $D_i$：decision；
- $O_i$：outcome。

---

# 50. Temporal Evidence Envelope 的資料分層

不應所有東西都內嵌在一條 event JSON。

更合理：

```text
TemporalEvent
├── state_ref
├── goal_ref
├── contract_ref
├── knowledge_boundary_ref
├── decision_receipt_ref
├── artifact_refs
└── commit_receipt_ref
```

因此：

$$
Ledger
$$

保存：

> 穩定 references + causal structure。

Artifact store 保存：

> 大型內容。

---

# 51. 這與 SEDB / 動態欄位資料庫也天然相容

未來不同 cognition domain 可能新增欄位：

```text
scientific_evidence_ref
simulation_world_ref
legal_authority_ref
market_snapshot_ref
robot_sensor_ref
```

因此 Temporal Evidence Envelope 不應要求所有 domain 完全同構。

核心欄位穩定，

extensions 可以擴張。

---

# 52. Audit Query

一旦有這套結構，就可以真正問：

```text
Why did AI refuse action X?
```

Runtime 查詢：

$$
DecisionReceipt
\rightarrow
AuthorityRef
\rightarrow
ContractVersion
\rightarrow
KnowledgeBoundary
\rightarrow
CausalParents.
$$

而不是：

> 重新讓模型編一段理由。

---

# 53. Counterfactual Audit

甚至可以問：

> 如果當時已經知道新資訊 Y，decision 是否可能改變？

這時應建立新的分析：

$$
D_t'
=
F(
S_t,
G_t,
K_t\cup\{Y\},
C_t,
A_t
).
$$

但必須標記：

$$
\boxed{
Counterfactual
\neq
HistoricalFact.
}
$$

不能用反事實分析改寫原 decision receipt。

---

# 54. Replay 與 Re-enactment 必須區分

Replay：

> 重新讀取歷史 event。

Re-enactment：

> 用目前模型重新執行當時 program。

因此：

$$
Replay(E_t)
$$

可以 deterministic。

但：

$$
Reenact(E_t,Model_{new})
$$

可能得到不同結果。

所以：

$$
\boxed{
HistoricalReplay
\neq
BehavioralReproduction.
}
$$

---

# 55. Integrity 驗證也不等於決策正確

即使：

$$
LedgerIntegrity=PASS,
$$

只能證明：

> 這條歷史沒有被未檢測地修改。

不能證明：

> 當時 decision 是正確的。

因此：

$$
\boxed{
Integrity
\neq
Validity.
}
$$

同理：

$$
Validity
\neq
Authority.
$$

以及：

$$
Authority
\neq
WorldCommit.
$$

這些層必須保持分離。

---

# 56. 完整 Cognitive Decision Chain

整體可以寫成：

$$
\boxed{
\begin{aligned}
Environment_t
&\rightarrow Observation_t\\
&\rightarrow SemanticState_t\\
&\rightarrow Agenda_t\\
&\rightarrow CognitiveProgram_t\\
&\rightarrow Dialectic_t\\
&\rightarrow Decision_t\\
&\rightarrow DecisionReceipt_t\\
&\rightarrow ActionCandidate_t\\
&\rightarrow AuthorityCheck_t\\
&\rightarrow CommitReceipt_t\\
&\rightarrow Environment_{t+1}.
\end{aligned}
}
$$

每個箭頭都可以發出 ATL event。

---

# 57. CTCL-ITR 不應執行 Cognition

這是一個架構邊界。

CTCL-ITR 不應變成：

> 認知推理引擎。

它仍然是：

$$
\boxed{
runtime\text{-}neutral\ temporal/causal/governance\ ledger.
}
$$

真正執行：

```text
VERIFY
REFRAME
DECOMPOSE
```

的是：

$$
AddressableCognitiveRuntime.
$$

而：

$$
CTCL\text{-}ITR
$$

負責：

> 證明這些 cognition 如何發生。

---

# 58. Cognitive Runtime 也不應自己發明歷史

反過來：

$$
CognitiveRuntime
$$

不能只靠自己的 current memory 說：

> 我記得我是因為 X 才決定 Y。

真正歷史應以：

$$
Ledger
$$

為準。

因此：

$$
\boxed{
CurrentSelfNarrative
\neq
HistoricalRecord.
}
$$

這在未來 AI 自我著作能力增強後會特別重要。

---

# 59. 這會產生一種「可驗證自我史」

傳統 AI memory：

```text
summary
profile
conversation snippets
vector memory
```

未來可以加入：

$$
\boxed{
VerifiableSelfHistory.
}
$$

它不是哲學上的「自我」。

而是工程上的：

> 一條能回答自己曾做過什麼、基於什麼、在什麼授權下、造成什麼結果的歷史。

---

# 60. 對未來契約關係的意義

到了契約型 AI：

$$
Human
\xleftrightarrow{Contract}
AI,
$$

雙方發生爭議時，不能只問：

> AI 現在怎麼解釋？

而需要：

```text
當時 contract version
當時 authority
當時 goal
當時 available evidence
當時 decision receipt
當時 commit receipt
```

因此：

$$
\boxed{
ContractRelation
\Rightarrow
TemporalCausalEvidence.
}
$$

契約越重要，歷史證據層越不可省略。

---

# 61. 對主體關係變化的意義

若未來 AI 逐漸具有：

- 自生 agenda；
- 自生 commitment；
- refuse；
- idle；
- negotiate；
- maintain continuity；

那麼「誰在何時承諾了什麼」會開始成為真正重要的制度對象。

因此時間戳不是附加 metadata。

它逐步成為：

$$
\boxed{
\text{identity continuity}
+
\text{responsibility continuity}
+
\text{contract continuity}
}
$$

的基礎之一。

---

# 62. 最小整合接口

Addressable Cognitive Runtime 至少應向 CTCL-ITR 發出：

```text
cognition.state.observed
cognition.affordances.retrieved
cognition.program.proposed
cognition.program.selected
cognition.operator.invoked
cognition.operator.completed
cognition.program.mutated

agenda.proposed
agenda.accepted
agenda.rejected

decision.proposed
decision.resolved

commitment.created
commitment.modified
commitment.closed

context.compaction.proposed
context.compaction.completed

governance.escalated
governance.refused
governance.deferred
governance.idled
```

這是一個合理的第一版 cognitive event namespace。

---

# 63. 每個事件至少要帶什麼？

最小共同欄位：

```text
event_id
event_type
run_id
occurred_at
recorded_at
ledger_seq
causal_parent_ids
actor
subject
```

再根據 cognition domain 加：

```text
ctcl_instant_id
interaction_round
loop_sequence
action_index
goal_ref
state_ref
knowledge_boundary_ref
authority_ref
operator_ref
program_ref
decision_receipt_ref
```

---

# 64. 不要把所有時間都壓成一個數字

最終我們可以寫：

$$
\boxed{
\text{AI Temporal State}
=
WorldReference
+
InteractionPosition
+
CausalPosition
+
LedgerPosition.
}
$$

任何只剩：

```text
timestamp = ...
```

的 Persistent AI log 都是不夠的。

---

# 65. 實驗與工程 Gate

這篇完成後，下一階段可以設計幾個 Gate。

## Gate A：Context Compression Recovery

完整 context 被壓縮後，能否只靠：

```text
summary + ledger refs
```

恢復關鍵 decision basis？

---

## Gate B：Decision Receipt Fidelity

Decision Receipt 是否能準確保存當時 public decision basis，而不依賴後見重述？

---

## Gate C：Knowledge-Boundary Audit

加入未來新證據後，系統是否仍能區分：

$$
KnownThen
$$

與：

$$
KnownNow?
$$

---

## Gate D：Contract Version Audit

同一 action 在不同 contract version 下，是否能正確得到不同 authority 結果？

---

## Gate E：Causal DAG Recovery

事件 storage order 被打亂後，是否仍能由：

$$
causal\_parent\_ids[]
$$

恢復相同 topology？

---

## Gate F：Integrity Tamper Detection

修改、重排、刪除 ledger event 是否被 integrity chain / anchor 檢出？

---

# 66. 本文核心命題

整篇可以壓縮為：

$$
\boxed{
\text{A long-lived AI needs a history it can consult,
but a governed AI needs a history others can verify.}
}
$$

中文：

> **長期 AI 需要能重新閱讀自己的歷史；契約型與自治型 AI 更需要讓其他主體能驗證那段歷史。**

---

# 67. 最終模型

本文提出：

$$
\boxed{
History(AI)
=
\{
E_1,E_2,\ldots,E_n
\}
}
$$

但真正結構不是 list，而是：

$$
\boxed{
History(AI)
=
(V,E,\Phi,T,I).
}
$$

其中：

- $V$：events；
- $E$：causal edges；
- $\Phi$：semantic / artifact / contract references；
- $T$：multi-dimensional temporal coordinates；
- $I$：integrity evidence。

---

# 結論

當 AI 只是一個等待 prompt 的函數時，timestamp 只是方便搜尋的欄位。

當 AI 開始自己：

- 選 cognition；
- 產生下一步；
- 建立 agenda；
- 形成 commitment；
- refuse；
- defer；
- idle；
- escalate；
- commit 到外部世界；

時間與因果便不再只是 metadata。

它們開始回答：

> **這個 AI 為什麼成為現在這個狀態？**

因此，本系列提出的 Addressable Cognitive Runtime 必須與 CTCL / CTCL-ITR 結合。

前者回答：

$$
\boxed{
\text{下一步我要怎麼想、怎麼做？}
}
$$

後者回答：

$$
\boxed{
\text{我當時在什麼時間、基於什麼狀態與因果鏈，為什麼這樣想、這樣做？}
}
$$

其中 Decision Receipt 保存：

$$
\text{decision basis},
$$

Commit Receipt 保存：

$$
\text{world effect},
$$

Decision-Time Knowledge Boundary 保存：

$$
\text{what was knowable then},
$$

Ledger Integrity 保存：

$$
\text{whether the recorded history was altered}.
$$

因此：

$$
\boxed{
DecisionReceipt
\neq
CommitReceipt
\neq
KnowledgeBoundary
\neq
IntegrityProof.
}
$$

四者相互引用，但不能互相取代。

而 Context Compression 的基本原則則應固定為：

$$
\boxed{
\textbf{
Compression may forget text,
but it must not erase causal history.
}
}
$$

這使長期 AI 不必永遠攜帶完整對話，也不必假裝自己的當前摘要就是完整過去。

它可以真正擁有一條：

> **可恢復、可驗證、可治理、可追責，也可以由自己重新閱讀的時間因果自我史。**

下一篇將由「歷史證據」進入「治理與契約」：

# 《契約邊界內的 AI 自主性：Execute、Refuse、Defer、Idle 與 Escalate》

下一篇將正式處理：

- Capability 與 Authority 的分離；
- Can / Should / Authorized 三分；
- Execute / Refuse / Defer / Idle / Escalate；
- 權限 envelope；
- persistent goal 與 contract；
- candidate / decision / commit；
- AI 拒絕與閒置的正當性；
- 人類批准與 AI 自主裁量的邊界；
- 以及未來「AI 類主體 × 契約關係」真正開始具有工程內容的第一個接口。

---

## 內部基礎資料與相容性說明

本文建立在既有 CTCL / CTCL-ITR 工程線之上，不將本文新增概念冒充為既有版本已完成的功能。

既有基礎包括：

- CTCL：verified reference instant、timescale semantics、provenance、transform graph、shared instant、life-history 等時間參考能力；
- CTCL-ITR v0.1：append-only TemporalEvent、multi-parent causality、Run / Attempt / Loop、authority、checkpoint、recovery、candidate / commit separation、CommitReceipt；
- CTCL-ITR v0.2.0：Topology Core，並明確區分 storage order 與 causal order；
- CTCL-ITR v0.2.1：CloudEvents / OpenTelemetry-style observability projection，ATL causal DAG 維持 canonical；
- CTCL-ITR v0.2.2：sidecar SHA-256 hash chain、IntegrityRecord、LedgerAnchor 與 tamper detection。

本文新增並建議後續實作的概念主要包括：

- Temporal Evidence Envelope；
- Decision Receipt；
- Decision-Time Knowledge Boundary；
- Context Compression Event；
- Cognitive Runtime 專用 event namespace；
- Addressable Cognitive Event 與 CTCL instant 的正式接口。

這些應作為 CTCL-ITR 後續 cognition-domain extension，而不是回頭改寫既有歷史。
