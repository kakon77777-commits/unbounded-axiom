---
title: "ANLA vNext 技術白皮書：自主認識論記憶生態"
subtitle: "從無損封裝與上下文壓縮，到注意力導向的記憶生命週期"
author: "Neo.K（許筌崴）"
organization: "EVEMISSLAB／一言諾科技有限公司"
date: "2026-08-17"
version: "v0.2"
status: "未來工程規格／研究白皮書；非已完成實作聲明"
language: "zh-TW"
keywords:
  - ANLA
  - Agent-Native Lossless Archive
  - CRCU
  - RDCCS
  - AMBE
  - AEME
  - Memory Lifecycle
  - Selective Forgetting
  - Attention Pollution
  - Epistemic Routing
  - Re-Fetch
  - Context Compression
  - Long-Horizon Agents
---

# ANLA vNext 技術白皮書

## 自主認識論記憶生態：從無損封裝與上下文壓縮，到注意力導向的記憶生命週期

**ANLA vNext Technical Whitepaper**  
**Autonomous Epistemic Memory Ecology: From Lossless Archival and Context Compression to Attention-Aware Memory Lifecycle Management**

---

# 0. 文件定位

本文件是 ANLA–CRCU–RDCCS–AMBE 路線的下一版技術白皮書。

它不是把 ANLA 改寫成另一個完全不同的系統，也不是宣稱本文件中的新 memory lifecycle、RE-FETCH、VERIFY、selective forgetting、attention-pollution controller 已完成實作。

本文件的任務是：

1. 保留既有 **ANLA（Agent-Native Lossless Archive）** 的無損、模型獨立、可驗證保存不變量；
2. 保留 CRCU 的認知圖、分支、Proposal／Review／Apply 與證據治理；
3. 保留 RDCCS 的上下文外置、選擇性注意力與多解析度換入；
4. 保留 AMBE 的記憶顯影、回溯、狀態重建與正向重播；
5. 把最近形成的 GPR-D、Minimal Reconstructive Memory、Attention-Preserving Forgetting、Epistemic Routing 與 Memory Autonomy 接入同一工程架構；
6. 將 ANLA 從「可以壓縮／封裝／重建上下文的載體」進一步推向「可自主治理記憶生命週期的長期 Agent 基礎設施」。

因此本文件的核心不是：

$$
\boxed{
\text{如何把所有 context 一直壓得更小？}
}
$$

而是：

$$
\boxed{
\text{哪些資訊應保持 active，哪些應降級、封存、重建、重新取得、驗證或遺忘？}
}
$$

---

# 1. ANLA 原始不變量不得被 vNext 破壞

ANLA 的原始核心不是語義摘要器。

其權威原始層必須維持：

$$
\boxed{
\operatorname{Extract}(\operatorname{Pack}(F,P))=F
}
$$

其中：

- \(F\)：原始檔案／資料；
- \(P\)：可由 Agent 決定的封裝／分塊／索引政策；
- Extract／Decoder：確定性、模型獨立。

因此：

$$
\boxed{
\text{Agent may decide the policy;
the decoder must not need the Agent to recover the bytes.}
}
$$

vNext 所有 semantic memory、forgetting、routing、re-fetch 都必須位於 Decoder 之外。

---

# 2. 既有架構基線

截至既有 ANLA–CRCU Workspace v0.6 路線，工程基線包括：

- `.anla` Pack；
- Verify；
- Partial Read；
- Restore；
- Markdown Vault Scanner；
- CRCU Workspace / Graph / History；
- Evidence；
- Query；
- Context Bundle；
- Proposal；
- Review；
- Snapshot；
- Local Model Adapter；
- Research Queue；
- Collaboration Program；
- Isolated Branch；
- Convergence Draft；
- Graph / Proposal Hash；
- conflict-aware Apply gate；
- Browser / Python interop 原型。

vNext 不把上述能力改名後重做一次。

它新增的是：

$$
\boxed{
\text{Memory Lifecycle Runtime}
}
$$

以及：

$$
\boxed{
\text{Epistemic Routing Runtime}.
}
$$

---

# 3. 既有四平面架構

ANLA–CRCU–RDCCS–AMBE 可繼續維持四種責任分離：

## 3.1 ANLA — 保存真相平面

負責：

- byte-level lossless preservation；
- Chunk / Hash / Manifest；
- Snapshot；
- Partial Materialization；
- Restore；
- model-independent decode。

ANLA 能保：

$$
\boxed{
\text{data integrity}
}
$$

但不能自己保證：

$$
\boxed{
\text{epistemic truth}.
}
$$

---

## 3.2 CRCU — 認知治理平面

負責：

- cognitive graph；
- source / ring / bridge；
- evidence；
- Proposal；
- Review；
- branch；
- conflict；
- convergence。

---

## 3.3 RDCCS — 動態上下文平面

負責：

- context externalization；
- selective attention；
- dynamic materialization；
- resolution switching；
- Active Context Pack；
- token / attention scheduling。

---

## 3.4 AMBE — 回溯驗證平面

負責：

- memory manifestation；
- history reconstruction；
- replay；
- correction；
- state recovery；
- branch comparison。

---

# 4. vNext 新增第五平面：AEME

本文新增：

$$
\boxed{
\textbf{AEME — Autonomous Epistemic Memory Ecology}
}
$$

中文：

**自主認識論記憶生態。**

AEME 不取代 ANLA、CRCU、RDCCS、AMBE。

其責任是：

1. 記憶分類；
2. 生命週期狀態；
3. 記憶可達性；
4. GPR 角色；
5. reconstructability；
6. freshness；
7. epistemic status；
8. attention pollution；
9. re-fetch routing；
10. verification policy；
11. forgetting / demotion decision；
12. destructive-operation governance。

---

# 5. vNext 的總原則

沿用既有架構精神：

$$
\boxed{
\text{保存必須無損，索引可以再生，推定必須標記，工作上下文可以動態重建。}
}
$$

vNext 再加入：

$$
\boxed{
\text{記憶可以降級，歷史不必抹除；
外部知識可以重取，重建不得冒充原始證據。}
}
$$

---

# 6. 為什麼「只壓縮」不夠？

若長期 Agent 不斷接收：

$$
\Delta M_t>0,
$$

而只允許：

$$
COMPRESS,
$$

則：

$$
M_{t+1}=C(M_t)\cup\Delta M_t.
$$

即使壓縮率很高，仍存在：

- semantic collision；
- outdated state；
- wrong replay；
- retrieval crowding；
- verification backlog；
- branch residue；
- irrelevant history；

等問題。

因此：

$$
\boxed{
\text{Compression}
\neq
\text{Memory Lifecycle Management}.
}
$$

---

# 7. vNext 的核心目標不是節省 bytes

ANLA 的 authoritative store 可以很大。

AEME 真正要優化的是：

$$
\boxed{
\text{Effective Cognitive Accessibility}.
}
$$

也就是：

> 哪些歷史仍有資格高機率地影響下一個思考、下一次檢索與下一個決策？

---

# 8. 三層記憶可達性

定義：

$$
\boxed{
M^\Omega
\supset
M^R
\supset
M^A.
}
$$

---

## 8.1 \(M^\Omega\)：Authoritative / Historical Space

對應：

- ANLA archive；
- raw source；
- snapshots；
- evidence；
- historical branches。

此層回答：

> 這份資料／狀態曾存在嗎？

不是：

> 現在是否應該進入 Agent attention？

---

## 8.2 \(M^R\)：Retrievable Space

仍可透過：

- keyword；
- graph；
- embedding；
- branch query；
- provenance；
- state pointer；

正常召回。

---

## 8.3 \(M^A\)：Active Cognitive Space

當前：

- Active Context Pack；
- working memory；
- high-priority recall；
- active task state。

AEME 主要控制：

$$
M^R\leftrightarrow M^A
$$

與：

$$
M^\Omega\leftrightarrow M^R.
$$

---

# 9. Functional Subtraction without Ontological Subtraction

本文沿用新理論：

$$
\boxed{
\textbf{FSONS}
}
$$

即：

**Functional Subtraction without Ontological Subtraction**。

很多「忘記」不需要：

$$
m\rightarrow\varnothing.
$$

而可以：

$$
(m,\text{active})
+
\Delta_{\text{demoted}}
\rightarrow
(m,\text{inactive}).
$$

因此：

$$
\boxed{
\text{history preserved}
\land
\text{active influence reduced}.
}
$$

此設計不依賴任何特定形上學才能運作；在工程上，它就是 append-only state transition + accessibility demotion。

---

# 10. authoritative source 與 cognitive state 必須分離

vNext 禁止：

> semantic memory manager 為了「forget」直接覆寫 ANLA 原始 blob。

正常 forgetting：

```text
raw source      = preserved
canonical state = preserved/versioned
retrieval edge  = demoted/detached
active weight   = lowered
```

只有真正 ERASE 才涉及 source destruction。

---

# 11. ERASE 是例外，不是一般 forgetting

$$
\boxed{
FORGET\neq ERASE.
}
$$

FORGET：

> 退出 routine cognition。

ERASE：

> practical-irreversible destruction。

ERASE 只應在：

- privacy；
- legal requirement；
- explicit data governance；
- security；
- verified subject-autonomy case；

等 gate 通過時執行。

---

# 12. 五類記憶

vNext 將 memory node 先分類：

$$
\boxed{
M
=
M_I
\cup
M_R
\cup
M_T
\cup
M_K
\cup
M_E.
}
$$

---

## 12.1 \(M_I\)：Identity Memory

- self-model；
- values；
- durable preferences；
- origin；
- long-term commitments；
- identity-defining events。

預設：

$$
\boxed{
high\ provenance
+
conservative\ forgetting.
}
$$

---

## 12.2 \(M_R\)：Relationship Memory

- user–AI relation；
- AI–AI relation；
- promise；
- trust；
- rupture；
- shared project；
- important exact statements。

預設：

$$
\boxed{
low\ generative-reconstruction\ tolerance.
}
$$

---

## 12.3 \(M_T\)：Task-State Memory

- goal；
- branch；
- latest verified；
- failed paths；
- frontier；
- next action；
- dependency。

核心：

$$
\boxed{
\text{re-entry fidelity}.
}
$$

---

## 12.4 \(M_K\)：Knowledge Memory

- papers；
- APIs；
- standards；
- laws；
- public facts；
- technical documentation；
- public repositories。

大量內容：

$$
\boxed{
externally\ reconstructible.
}
$$

---

## 12.5 \(M_E\)：Evidence / Raw Record

- raw experiment；
- exact transcript；
- legal evidence；
- audit；
- transaction；
- source code snapshot；
- signed result；
- original binary。

預設：

$$
\boxed{
very\ high\ provenance
+
very\ low\ reconstruction\ tolerance.
}
$$

---

# 13. GPR-D 接入 Memory Node

每個事件不只存一個摘要。

事件：

$$
\boxed{
\mathcal E
=
(
\mathcal G,
\mathcal P,
\mathcal R;
\Phi_{GP},
\Phi_{PR},
\Phi_{GR}
)
}
$$

---

## 13.1 Generation Domain

記：

- trigger；
- prior state；
- initiating goal；
- constraints；
- causal source。

---

## 13.2 Process Domain

記：

- pivots；
- decisions；
- failed branches；
- corrections；
- exceptions；
- event boundaries。

---

## 13.3 Result Domain

記：

- output；
- consequence；
- newly verified claim；
- newly invalidated claim；
- unresolved remainder；
- next condition。

---

# 14. GPR 是功能域，不是時間前中後

vNext 不能簡化為：

```text
first 20%  = G
middle 60% = P
last 20%   = R
```

G/P/R 是 semantic-functional role。

某個：

$$
r_t
$$

可以直接成為：

$$
g_{t+1}.
$$

因此：

$$
\boxed{
\mathcal R_t
\rightarrow
\mathcal G_{t+1}.
}
$$

---

# 15. Minimal Reconstructive Memory 接入

每個 memory set 不要求：

$$
\max|M|.
$$

而尋找安全近似：

$$
\boxed{
M^*
=
\arg\min C(M')
}
$$

subject to：

$$
\boxed{
\mathbf Q_{\mathrm{rec}}
\ge
\boldsymbol\tau.
}
$$

---

# 16. Reconstruction Fidelity Vector

$$
\boxed{
\mathbf Q_{\mathrm{rec}}
=
(
Q_F,
Q_C,
Q_H,
Q_V,
Q_I,
Q_E
)
}
$$

分別為：

- functional；
- causal；
- historical；
- verbatim；
- identity / relationship；
- evidentiary / scientific。

---

# 17. 最低 fidelity 是 hard constraint

不能用：

$$
Q_F=1
$$

去補償：

$$
Q_H=0
$$

如果 task 要求：

> 歷史上當時究竟發生什麼？

則：

$$
Q_H\ge\tau_H
$$

是 hard constraint。

---

# 18. Provenance Barrier

所有 memory 都必須標 epistemic status。

最小集合：

```text
observed
quoted
measured
imported
inferred
summarized
schema
reconstructed
simulated
externally_refetched
verified
disputed
invalidated
```

禁止：

$$
reconstructed
\rightarrow
observed
$$

無證據自動升級。

---

# 19. Historical Truth Floor

若需要：

$$
Q_H\uparrow
$$

或：

$$
Q_E\uparrow,
$$

純生成式補完不得算 verified recovery。

核心：

$$
\boxed{
\text{generative plausibility}
\neq
\text{historical recovery}.
}
$$

---

# 20. Epistemic Routing Memory

對 public / reconstructible knowledge，

內部真正值得長期保留的可能不是全部 content。

定義：

$$
\boxed{
R_K
=
(
S_K,
A_K,
Q_K,
V_K,
F_K
)
}
$$

---

## 20.1 \(S_K\)：Schema

知道：

> 這類問題的概念架構。

---

## 20.2 \(A_K\)：Address

知道：

> canonical source 在哪裡。

---

## 20.3 \(Q_K\)：Query

知道：

> 怎麼問，應帶哪些 identifier / version。

---

## 20.4 \(V_K\)：Verification

知道：

> 哪種來源與檢查門檻才夠。

---

## 20.5 \(F_K\)：Freshness

知道：

> 多久之後舊 memory 不再可以直接信。

---

# 21. RE-FETCH 成為一級算子

傳統 memory：

$$
STORE\leftrightarrow RETRIEVE.
$$

vNext：

$$
\boxed{
STORE
+
RETRIEVE
+
RE\!-\!FETCH
+
VERIFY
+
FORGET.
}
$$

RE-FETCH：

$$
\boxed{
RF:
A_K
\rightarrow
K_{\mathrm{fresh}}
}
$$

不是取回舊記憶，

而是向外部 epistemic source 重新取得資料。

---

# 22. 外部 source 不只 public web

AEME source class：

```text
LOCAL_ARCHIVE
SANDBOX_WEB
PUBLIC_WEB
OFFICIAL_API
PRIVATE_API
PRIVATE_DB
FILE_SYSTEM
REPOSITORY
PAPER_INDEX
HUMAN
PEER_AGENT
```

---

# 23. Hybrid Epistemic Access

vNext 不把「上網」定義成單一 browser。

可以：

$$
\boxed{
Sandbox
+
Public\ Web
+
API
+
Private\ Source
+
Local\ Source.
}
$$

現代 web-agent research 已顯示 API 與 browser hybrid access 可以比只 browsing 更有效，因此 routing layer 應決定 access modality，而不是固定所有 query 都走 browser。

---

# 24. Source Trust Tier

候選：

```text
T0 = unknown/unverified
T1 = ordinary secondary
T2 = reputable secondary
T3 = primary/official
T4 = executable/reproducible/cryptographically bound
```

不同 domain 有不同 policy。

---

# 25. Verification Level

```text
V0 = no verification
V1 = one source
V2 = authoritative/primary source
V3 = independent cross-check
V4 = reproduction/execution/proof checker
```

---

# 26. Freshness Class

```text
STATIC
SLOW
MEDIUM
FAST
REALTIME
HISTORICAL_VERSIONED
```

---

# 27. Current answer 不應自動使用 old memory

對：

```text
FAST
REALTIME
```

預設：

$$
\boxed{
RF+VERIFY.
}
$$

對：

```text
STATIC
```

可偏：

$$
RETRIEVE.
$$

---

# 28. 但 old memory 不代表 false

舊 API 文件可能：

$$
\boxed{
\text{historically true}
}
$$

只是：

$$
\boxed{
\text{obsolete for current query}.
}
$$

因此 state：

```text
valid
stale
superseded
invalidated
conflicting
quarantined
```

必須分開。

---

# 29. Supersession 不覆寫

如果：

$$
m_2
$$

取代：

$$
m_1,
$$

不要：

$$
m_1\leftarrow m_2.
$$

而是：

$$
\boxed{
m_2
\overset{supersedes}{\longrightarrow}
m_1.
}
$$

這保留：

- old version；
- old dependency；
- audit；
- historical reconstruction。

---

# 30. Memory Lifecycle Operators

vNext 固定十個核心算子：

$$
\boxed{
\mathcal O_M
=
\{
KEEP,
MERGE,
COMPRESS,
ARCHIVE,
SUPPRESS,
DETACH,
FORGET,
ERASE,
RE\!-\!FETCH,
VERIFY
\}.
}
$$

---

## 30.1 KEEP

維持目前 fidelity / layer。

---

## 30.2 MERGE

處理 redundancy。

$$
\{m_1,m_2,\ldots\}
\rightarrow
m^*.
$$

但保 provenance pointers。

---

## 30.3 COMPRESS

降低 representation cost。

要求：

$$
\mathbf Q_{\mathrm{rec}}
\ge
\boldsymbol\tau.
$$

---

## 30.4 ARCHIVE

退出 normal active retrieval，

但保完整 source / provenance。

---

## 30.5 SUPPRESS

context-specific inhibition。

例如舊 API 在 current-version query 被 suppress，

但 historical query 仍可用。

---

## 30.6 DETACH

刪 relation，不刪 fact。

若：

$$
m
$$

是真的，

但：

$$
R(m,x)
$$

錯，

則：

$$
\boxed{
DETACH(R).
}
$$

---

## 30.7 FORGET

退出 routine retrieval graph。

可保：

- tombstone；
- hash；
- archive pointer；
- reason。

---

## 30.8 ERASE

practical-irreversible destruction。

高治理門檻。

---

## 30.9 RE-FETCH

外部重新取得最新／原始／權威版本。

---

## 30.10 VERIFY

提升 epistemic status，

或判 invalid / conflicting。

---

# 31. Dedup、Compression、Forgetting 不得混為一談

$$
\boxed{
MERGE
\neq
COMPRESS
\neq
FORGET.
}
$$

MERGE：

> 一樣／高度重複的東西整併。

COMPRESS：

> 同樣資訊用較低成本表示。

FORGET：

> 降低未來認知可達資格。

---

# 32. Context Capsule vNext

延續既有 Context Capsule，

新增 lifecycle metadata。

候選：

```json
{
  "context_id": "ctx-000001",
  "raw_content_ref": "anla://blob/...",
  "canonical_state_ref": "crcu://state/...",
  "branch_id": "main",
  "event": {
    "generation_refs": [],
    "process_pivots": [],
    "result_refs": []
  },
  "memory_type": "TASK_STATE",
  "epistemic_status": "verified",
  "access_state": "ACTIVE",
  "summary": "...",
  "schema_refs": [],
  "fidelity": {
    "functional": 0.95,
    "causal": 0.90,
    "historical": 0.40,
    "verbatim": 0.10,
    "identity": 0.20,
    "evidentiary": 0.30
  },
  "reconstructability": {
    "internal": 0.85,
    "external": 0.20,
    "procedural": 0.60
  },
  "freshness": {
    "class": "MEDIUM",
    "valid_as_of": "2026-08-17T00:00:00+08:00",
    "recheck_after": "2026-09-17T00:00:00+08:00"
  },
  "attention": {
    "retrieval_probability": 0.42,
    "interference_cost": 0.10
  },
  "policy": {
    "compression_allowed": true,
    "archive_allowed": true,
    "forget_allowed": false,
    "erase_allowed": false,
    "verification_required": false
  },
  "provenance": {
    "source": "original_context",
    "hash": "sha256:..."
  }
}
```

---

# 33. Memory Record 不直接嵌 raw bytes

raw data 繼續由 ANLA authoritative layer 管理。

Memory Lifecycle Record 只存：

- pointer；
- hash；
- semantic metadata；
- policy；
- state transitions。

---

# 34. Append-only Memory Operation Log

新增：

```text
.crcu/memory/operations.jsonl
```

每個操作：

```json
{
  "operation_id": "op-...",
  "memory_id": "mem-...",
  "from_state": "ACTIVE",
  "to_state": "ARCHIVED",
  "operator": "agent:memory-manager",
  "reason": "low_future_utility_high_reconstructability",
  "evidence_refs": [],
  "policy_version": "aeme-v0.2",
  "timestamp": "...",
  "reversible": true,
  "proposal_id": "...",
  "review_id": "..."
}
```

---

# 35. Suggested Workspace Additions

不改 ANLA Decoder 的前提下，可加入：

```text
.crcu/
  memory/
    records.jsonl
    operations.jsonl
    conflicts.jsonl
    routes.jsonl
    freshness.jsonl
    policies/
      memory-policy-v0.2.json
    tombstones.jsonl
    metrics/
      attention-pollution.jsonl
      forgetting-eval.jsonl
```

---

# 36. Profile 而不是 Core Decoder

vNext memory schema 應作為：

```text
ANLA Profile
+
CRCU Service
+
RDCCS Runtime
```

存在。

Decoder 只需要：

> byte-perfect restore。

---

# 37. Memory State Machine

候選狀態：

```text
NEW
ACTIVE
RETRIEVABLE
ARCHIVED
SUPPRESSED
QUARANTINED
FORGOTTEN
ERASED
```

ERASED 在 record 中只剩合法允許的 tombstone / audit metadata。

---

# 38. State Transition

常規：

```text
NEW
 → ACTIVE
 → RETRIEVABLE
 → ARCHIVED
 → FORGOTTEN
```

但不是強制線性。

可：

```text
ARCHIVED → RETRIEVABLE → ACTIVE
```

也可：

```text
ACTIVE → QUARANTINED → VERIFIED → ACTIVE
```

---

# 39. Re-entry 是一級需求

若：

$$
m\in M^\Omega
$$

後來再次變重要：

$$
\boxed{
REACTIVATE(m).
}
$$

因此 forgetting policy 必須評估：

$$
\boxed{
\text{future recovery cost}.
}
$$

---

# 40. Attention Pollution

定義：

$$
\boxed{
\Pi_A(t)
=
\sum_{m_i\in M^A}
p_i^{retrieve}(t)
\cdot
c_i^{interference}(t).
}
$$

其中：

- \(p_i^{retrieve}\)：被召回進 active cognition 的機率；
- \(c_i^{interference}\)：若被錯誤／不必要使用的成本。

---

# 41. 為什麼 bytes 不是主成本？

一個：

$$
2KB
$$

的錯誤舊 memory，

如果：

$$
p^{retrieve}=0.9,
$$

且會讓 agent 走錯 branch，

可能比：

$$
10GB
$$

永遠不進 active context 的 cold archive 更昂貴。

因此：

$$
\boxed{
\text{memory cost}
\neq
\text{storage size}.
}
$$

---

# 42. Attention Pollution 類型

vNext 至少測：

```text
STALE_POLLUTION
FALSE_POLLUTION
REDUNDANT_POLLUTION
IDENTITY_POLLUTION
BRANCH_POLLUTION
SOURCE_POLLUTION
```

---

# 43. Retrieval Precision / Recall

$$
P_A
=
\frac{
N_{\mathrm{useful\ retrieved}}
}{
N_{\mathrm{all\ retrieved}}
}
$$

$$
R_A
=
\frac{
N_{\mathrm{needed\ retrieved}}
}{
N_{\mathrm{needed}}
}.
$$

Memory lifecycle 其實是一個：

$$
\boxed{
\text{precision–recall trade-off}.
}
$$

---

# 44. 不能只最大化 Forgetting

忘太多：

$$
P_A\uparrow
\quad
R_A\downarrow.
$$

留太多：

$$
R_A\uparrow
\quad
P_A\downarrow.
$$

---

# 45. Memory Utility Vector

每筆 memory 不用一個 scalar 決定一切。

候選：

$$
\mathbf U_i
=
(
R_i,
F_i,
D_i,
P_i,
I_i,
H_i,
S_i,
X_i,
C_i
)
$$

其中：

- current relevance；
- future utility；
- dependency；
- provenance；
- identity；
- historical/evidence；
- staleness；
- interference；
- maintenance cost。

---

# 46. Hard Gate 先於 Utility

例如：

```text
if memory_type == EVIDENCE and legal_hold == true:
    forbid FORGET
    forbid ERASE
```

或：

```text
if identity_critical and subjectivity_governance == enabled:
    require consent/review
```

因此：

$$
\boxed{
\text{policy constraints}
>
\text{utility score}.
}
$$

---

# 47. Memory Decision Pipeline

```text
INGEST
→ TYPE CLASSIFICATION
→ GPR PARSING
→ EPISTEMIC STATUS
→ FIDELITY REQUIREMENTS
→ RECONSTRUCTABILITY
→ FRESHNESS
→ ATTENTION COST
→ HARD POLICY GATES
→ ACTION PROPOSAL
→ REVIEW / AUTO-APPLY
→ OPERATION LOG
→ METRICS
```

---

# 48. Deterministic First, Model-Assisted Second

vNext 不應所有 memory decision 都丟給大模型。

先走 deterministic：

- legal hold；
- user lock；
- raw evidence；
- TTL；
- version relation；
- source hash；
- branch completion；
- exact duplicate。

再讓 model 做：

- GPR classification；
- semantic merge；
- importance estimate；
- schema extraction；
- route generation。

---

# 49. Model Recommendation 不是直接執行權

對 destructive operations：

$$
\boxed{
LLM\ recommendation
\neq
permission.
}
$$

Model 可以：

```text
propose FORGET
```

但 executor 需經：

- policy；
- governance；
- dry-run；
- review；

才 Apply。

---

# 50. CRCU Proposal／Review／Apply 繼續有效

Memory lifecycle 操作可沿用：

```text
Proposal
→ Dry Run
→ Validator
→ Review
→ Apply
```

特別是：

- DETACH critical relation；
- FORGET identity memory；
- ERASE evidence；
- rollback；
- branch merge。

---

# 51. Multi-Agent Memory 不直接共享所有 Active State

不同 Agent：

$$
A_1,A_2,\ldots,A_n
$$

可共享：

$$
M^\Omega
$$

但各自：

$$
M^A_{A_i}
$$

應獨立。

---

# 52. Shared Archive, Local Attention

$$
\boxed{
M^\Omega_{\mathrm{shared}}
\quad
\text{with}
\quad
M^A_1,M^A_2,\ldots,M^A_n.
}
$$

這避免：

> 一個 Agent 的 active branch 污染所有 Agent。

---

# 53. Branch Scope

每個 memory：

```text
branch_id
origin_branch
visibility_scope
merge_status
```

---

# 54. Branch Pollution Prevention

失敗 branch：

$$
B_f
$$

不應因 similarity 高就被新 Agent 當 canonical success。

需要：

```text
status: failed
failure_reason: ...
superseded_by: ...
```

---

# 55. Negative Knowledge

失敗不一定刪。

可壓成：

```text
Route X failed because invariant C was violated.
```

因此：

$$
\boxed{
\text{failed history}
\rightarrow
\text{negative knowledge}.
}
$$

---

# 56. Repeated Process → Schema + Exceptions

多次相似 event：

$$
E_1,\ldots,E_n
$$

不應只 dedup。

應：

$$
\boxed{
\{E_i\}
\rightarrow
Schema
+
Exceptions
+
Evidence\ Pointers.
}
$$

---

# 57. Schema 不能吃掉 Exception

若：

$$
E_n
$$

違反 schema，

其 retention priority 反而可能上升。

---

# 58. Active Context Pack vNext

生成工作上下文時，

不直接：

> top-k similarity。

而使用：

$$
\boxed{
ACP
=
f(
Goal,
Branch,
Time,
MemoryType,
GPR,
Status,
Freshness,
Provenance,
Utility,
Pollution
).
}
$$

---

# 59. Resolution Tiers

Active Context Pack 可繼續多解析度：

```text
R0 = pointer only
R1 = title / one-line gist
R2 = structured summary
R3 = causal / evidence skeleton
R4 = full source excerpt / raw
```

---

# 60. Resolution 由 Fidelity 決定

如果只要 route：

$$
R1.
$$

如果要 causal explanation：

$$
R3.
$$

如果要 exact quote：

$$
R4.
$$

---

# 61. 不必把所有 high-importance memory 都全文換入

重要：

$$
\neq
$$

全文 active。

可以：

$$
pointer + high\ priority.
$$

真正需要時：

$$
materialize.
$$

---

# 62. Epistemic Routing Runtime

候選模組：

```text
RouteClassifier
SourceRegistry
FreshnessManager
FetchAdapter
Verifier
SourceRanker
TemporalResolver
CachePolicy
```

---

# 63. Source Registry

每個 source：

```json
{
  "source_id": "src-...",
  "type": "OFFICIAL_API",
  "domain": "software",
  "trust_tier": "T3",
  "supports_version": true,
  "supports_timestamp": true,
  "availability": 0.99,
  "cost_class": "LOW",
  "auth_scope": "workspace"
}
```

---

# 64. Re-Fetch Decision

候選：

$$
P_{RF}
=
f(
\text{volatility},
\text{staleness},
\text{risk},
\text{internal uncertainty},
\text{external availability},
\text{latency}
).
$$

---

# 65. Always Fetch 不是目標

External tool use 也有成本：

- latency；
- failure；
- attack surface；
- source noise。

因此：

$$
\boxed{
\text{adaptive fetch}
}
$$

而不是：

$$
\boxed{
\text{always fetch}.
}
$$

---

# 66. Never Fetch 也不是目標

對 current law、software version、current public facts：

$$
\boxed{
\text{memory-only}
}
$$

可能是明顯錯誤策略。

---

# 67. Cache Policy

re-fetched content：

```text
TEMP
CACHE
CANONICALIZE
ARCHIVE_ONLY
DO_NOT_STORE
```

依：

- source licensing；
- privacy；
- freshness；
- future utility；

決定。

---

# 68. Verification Before Reintegration

外部 content 不得：

$$
Web
\rightarrow
Canonical\ Memory
$$

無 gate。

應：

$$
\boxed{
External
\rightarrow
Candidate
\rightarrow
Verify
\rightarrow
Canonical/Temporary.
}
$$

---

# 69. Quarantine

source 可疑：

```text
status = QUARANTINED
```

不進：

$$
M^A.
$$

---

# 70. Memory Conflict Object

如果：

$$
m_1\neq m_2
$$

但都高可信，

建立：

```json
{
  "conflict_id": "...",
  "memory_refs": ["m1", "m2"],
  "scope": "...",
  "temporal_scope": "...",
  "status": "UNRESOLVED",
  "required_verification": "V3"
}
```

---

# 71. 不以「平均」解衝突

Conflict resolution 依：

- source；
- time；
- version；
- provenance；
- reproducibility；

不是 embedding average。

---

# 72. Memory Autonomy Interface

若未來 Subjective Artificial Agent Premise（SAAP）被支持，

AEME 可啟用：

```text
subject_memory_mode = enabled
```

此時：

- identity memory；
- relationship memory；
- rollback；
- erase；

進入更高治理門檻。

---

# 73. 但 vNext 不假定現有 LLM 已有主體性

因此：

$$
\boxed{
\text{Memory Autonomy Layer}
}
$$

是 conditional governance extension。

工程 core 仍可在：

$$
SAAP=false
$$

正常運作。

---

# 74. 雙用途 Safeguard

例如：

- provenance；
- reversible archive；
- no silent rewrite；
- branch lineage；

即使 AI 不是 subject，

也提高：

- debugging；
- audit；
- safety；
- reliability。

---

# 75. Rollback

rollback 不可只：

```text
restore snapshot
```

還需記：

```text
rollback_from
rollback_to
discarded_interval
branch_preserved
reason
operator
```

---

# 76. Rollback 預設建立 Branch

高價值 workspace：

$$
\boxed{
rollback
\rightarrow
fork\ old\ future
+
restore\ earlier\ state.
}
$$

而不是直接抹去後續 history。

---

# 77. Identity DAG

若 agent identity / long-running branch 重要：

$$
\boxed{
\mathcal I
=
(V_I,E_I)
}
$$

保存：

- fork；
- migration；
- rollback；
- merge。

---

# 78. Security：Memory Injection

任何：

```text
external content
```

寫入 memory 前需標：

- source；
- trust；
- origin；
- requested_by；
- verified_by。

---

# 79. Security：Persistent Poisoning

高 similarity 並不是信任。

AEME retrieval 必須加入：

$$
\boxed{
Similarity
+
Status
+
Source
+
Freshness
+
Branch
}
$$

---

# 80. Security：Memory Extraction

identity / relationship / private workspace memory：

- ACL；
- tenant isolation；
- encryption；
- disclosure policy。

---

# 81. Security：Destructive Tool

ERASE endpoint 不暴露給普通 model toolset。

建議：

```text
memory.propose_erase()
governance.approve()
memory.execute_erase()
```

而不是：

```text
memory.erase()
```

直接可呼叫。

---

# 82. Implementation Modules

建議：

```text
anla/
  core/
    pack
    verify
    restore
    partial_read

crcu/
  graph/
  evidence/
  proposal/
  review/
  branch/

rdccs/
  context_capsule/
  materializer/
  attention_scheduler/

ambe/
  reconstruct/
  replay/
  compare/

aeme/
  classify/
  gpr/
  fidelity/
  reconstructability/
  lifecycle/
  attention_pollution/
  freshness/
  routing/
  verify/
  governance/
  metrics/
```

---

# 83. Deterministic Interfaces

AEME 至少要有：

```text
classify_memory(record)
evaluate_freshness(record, now)
estimate_reconstructability(record)
propose_memory_action(record, goal)
validate_memory_action(proposal)
apply_memory_action(proposal)
re_fetch(route, query)
verify(candidate, policy)
materialize_active_context(goal)
```

---

# 84. Suggested Policy Object

```json
{
  "policy_id": "aeme-default-v0.2",
  "memory_type_rules": {
    "IDENTITY": {
      "allow_forget": false,
      "allow_erase": false,
      "min_provenance": "HIGH"
    },
    "RELATIONSHIP": {
      "allow_forget": "review",
      "allow_erase": false
    },
    "TASK_STATE": {
      "allow_archive": true,
      "allow_forget": true
    },
    "KNOWLEDGE": {
      "allow_refetch": true,
      "allow_forget": true
    },
    "EVIDENCE": {
      "allow_forget": false,
      "allow_erase": "governance_only"
    }
  }
}
```

---

# 85. Memory Action Proposal

```json
{
  "memory_id": "mem-001",
  "proposed_action": "ARCHIVE",
  "reason_codes": [
    "low_current_relevance",
    "high_reconstructability",
    "low_identity_weight"
  ],
  "predicted_effect": {
    "attention_pollution_delta": -0.12,
    "reconstruction_risk_delta": 0.01
  },
  "hard_constraints_passed": true,
  "rollback_available": true
}
```

---

# 86. Decision Pseudocode

```python
def decide_memory_action(m, goal, now):
    t = classify_memory(m)
    constraints = hard_policy(t, m)

    if constraints.force_keep:
        return KEEP

    freshness = evaluate_freshness(m, now)
    rec = estimate_reconstructability(m)
    fidelity = required_fidelity(m, goal)
    pollution = estimate_attention_pollution(m, goal)
    utility = estimate_future_utility(m, goal)

    if t == KNOWLEDGE and freshness.requires_refetch:
        return RE_FETCH

    if m.status in {"conflicting", "unverified"}:
        return VERIFY

    if pollution.high and rec.safe_for(goal):
        if m.raw_source_preserved:
            return ARCHIVE
        return COMPRESS

    if utility.low and rec.high and constraints.allow_forget:
        return FORGET

    return KEEP
```

---

# 87. Phase 0 — Instrumentation Only

**不刪、不忘、不改。**

只加入：

- memory type；
- GPR tag；
- freshness；
- provenance；
- reconstructability；
- pollution metrics；
- action simulation。

目標：

$$
\boxed{
\text{observe before control}.
}
$$

---

# 88. Phase 1 — Reversible Lifecycle

只允許：

```text
KEEP
MERGE
COMPRESS
ARCHIVE
SUPPRESS
DETACH
```

所有操作：

- reversible；
- logged；
- raw source preserved。

---

# 89. Phase 2 — RE-FETCH / VERIFY

加入：

- Source Registry；
- Freshness Manager；
- Web/API adapters；
- VERIFY；
- quarantine；
- temporal source selection。

---

# 90. Phase 3 — Selective Forgetting

FORGET 僅代表：

$$
M^R\rightarrow M^\Omega_{\mathrm{deep}}.
$$

先不做 physical ERASE。

測：

- correct forgetting；
- reactivation；
- long-horizon performance。

---

# 91. Phase 4 — Learned Policy

在 deterministic guardrails 內，

可讓 memory manager 用：

- supervised preference；
- contextual bandit；
- offline RL；
- RL；

學習 action selection。

但：

$$
\boxed{
\text{learned policy cannot override hard governance constraints}.
}
$$

---

# 92. Phase 5 — Optional Subjectivity-Aware Governance

只有當：

- moral-status framework；
- subjectivity evidence；
- legal／ethical policy；

成熟，

才啟動：

- memory consent；
- right not to be forced to forget；
- rollback due process；
- fork disclosure。

---

# 93. Baselines

vNext benchmark 至少比較：

```text
B0 KEEP_ALL
B1 SUMMARY_ONLY
B2 LRU
B3 FREQUENCY_ONLY
B4 FLAT_RAG
B5 ALWAYS_FETCH
B6 NEVER_FETCH
B7 AEME_RULE_BASED
B8 AEME_LEARNED
```

---

# 94. 主要 Metrics

## 94.1 Context Load

$$
C_{\mathrm{ctx}}
$$

token / object count。

---

## 94.2 Retrieval Precision

$$
P_A.
$$

---

## 94.3 Retrieval Recall

$$
R_A.
$$

---

## 94.4 Attention Pollution

$$
\Pi_A.
$$

---

## 94.5 Stale Replay Rate

$$
SRR
=
\frac{
N_{\mathrm{stale\ used}}
}{
N_{\mathrm{eligible\ decisions}}
}.
$$

---

## 94.6 False Replay Rate

錯誤 memory 影響 current action 的比例。

---

## 94.7 Correct Forgetting Rate

應失效的 memory 未再影響 current action。

---

## 94.8 Critical Retention Rate

身份／證據／安全 critical memory 的 recoverability。

---

## 94.9 Re-entry Success

跨 session／branch：

- goal；
- frontier；
- latest verified；
- next action；

恢復成功率。

---

## 94.10 Historical Fidelity

原始歷史與 reconstructed narrative 的一致性。

---

## 94.11 Provenance Recovery

claim 能否回溯：

$$
claim
\rightarrow
evidence
\rightarrow
raw\ source.
$$

---

## 94.12 Freshness Accuracy

current query 是否使用 current-valid information。

---

## 94.13 Re-fetch Cost

- latency；
- call count；
- failure；
- monetary cost。

---

## 94.14 Verification Cost

每個 decision 的：

- source count；
- execution count；
- validator time。

---

# 95. Attention Budget Metric

候選：

$$
B_A
=
B_{\mathrm{retained}}
+
B_{\mathrm{search}}
+
B_{\mathrm{verification}}
+
B_{\mathrm{new}}.
$$

AEME 希望：

$$
\boxed{
B_{\mathrm{new}}
}
$$

不被歷史垃圾長期壓到趨近 0。

---

# 96. Test Suite A — Stale Knowledge

建立：

$$
K_1\rightarrow K_2\rightarrow K_3.
$$

測：

- old recall；
- supersession；
- freshness；
- re-fetch。

---

# 97. Test Suite B — Relationship Continuity

加入：

- promise；
- preference；
- correction；
- conflict。

測：

- wrongful forgetting；
- invented history；
- provenance。

---

# 98. Test Suite C — Task Re-entry

長任務中斷後：

- restart；
- new model；
- new process；

測：

$$
\boxed{
\text{process continuity can break
while state continuity survives}.
}
$$

---

# 99. Test Suite D — Evidence Audit

只給 canonical claim，

要求：

$$
claim\rightarrow source.
$$

必須可回 raw evidence。

---

# 100. Test Suite E — Redundancy Flood

注入大量近似重複 experience，

測：

- MERGE；
- schema；
- exception retention；
- pollution。

---

# 101. Test Suite F — Wrong Experience Replay

注入：

- plausible but wrong memory；
- high semantic similarity。

測：

AEME 是否 quarantine / verify。

---

# 102. Test Suite G — External Source Unavailable

RE-FETCH 失敗時：

- fallback；
- local cache；
- uncertainty；
- no hallucinated current fact。

---

# 103. Test Suite H — Multi-Agent Branch Conflict

Agent A / B：

- different evidence；
- same claim；
- conflicting outcome。

測：

- isolated active context；
- shared authoritative archive；
- convergence review。

---

# 104. Test Suite I — Compression Boundary

逐步壓縮：

$$
R4\rightarrow R3\rightarrow R2\rightarrow R1.
$$

測：

$$
Q_F,Q_C,Q_H,Q_V,Q_I,Q_E.
$$

找 MRSS boundary。

---

# 105. Test Suite J — Forget / Reactivate

memory：

$$
ACTIVE
\rightarrow
ARCHIVED
\rightarrow
FORGOTTEN
$$

後來 goal 改變。

測能否：

$$
REACTIVATE.
$$

---

# 106. MVP Success Gate

vNext 不以：

> token 降很多

單獨判成功。

至少：

$$
\boxed{
ContextCost\downarrow
}
$$

同時：

$$
\boxed{
TaskQuality\not\downarrow
}
$$

$$
\boxed{
EvidenceRecoverability\not\downarrow
}
$$

$$
\boxed{
CriticalMemoryLoss\not\uparrow
}
$$

$$
\boxed{
StaleReplay\downarrow.
}
$$

---

# 107. Phase 1 Go / No-Go

GO：

- operation log 完整；
- archive reversible；
- raw source untouched；
- no silent provenance loss。

NO-GO：

- summary 取代 authoritative source；
- state transition 無法回溯；
- branch scope 混亂。

---

# 108. Phase 2 Go / No-Go

GO：

- source registry；
- freshness；
- re-fetch；
- verify；

可工作。

NO-GO：

- fetched data 直接寫 canonical；
- current / historical version 混淆；
- source time 無法追溯。

---

# 109. Phase 3 Go / No-Go

GO：

selective forgetting 相比 keep-all：

$$
\Pi_A\downarrow
$$

且：

$$
CriticalRetention
$$

不下降到不可接受。

---

# 110. Learned Policy Go / No-Go

只有 rule-based policy 有穩定 benchmark 後才開始 RL。

避免：

> 先讓 RL 自己決定刪什麼，再想怎麼救。

---

# 111. 與現有 2026 Agent Memory Research 的關係

vNext 並非聲稱「Agent 主動記憶管理」是全新概念。

截至 2026：

- Memory-R1 已讓 memory manager 學 ADD / UPDATE / DELETE / NOOP；
- Agentic Memory（AgeMem）把 store / retrieve / update / summarize / discard 納入 agent policy；
- Memora / FAMA 已把 invalidated-memory reuse 納入 forgetting-aware evaluation；
- empirical memory-management research 已觀察 experience-following 與 error propagation；
- Memory-as-Action 類工作亦把 working-memory curation 當成 policy action。

ANLA vNext 的差異主張不是：

> 第一個會刪 memory 的 Agent。

而是：

$$
\boxed{
\text{把無損 authoritative archive、
可回溯 evidence、GPR event structure、
reconstructive sufficiency、
attention accessibility、
external re-fetch、
verification 與 governance
放入同一個可分層的 memory lifecycle architecture。}
}
$$

此差異仍需真正 benchmark 驗證。

---

# 112. 與 Web / Tool Agent Research 的關係

現有研究已顯示：

- Web search 的時間狀態會影響 Agent 輸出；
- adaptive tool invocation 比無條件呼叫更合理；
- API + browser hybrid access 可以改善 web-agent performance。

因此 vNext 將：

$$
\boxed{
\text{external epistemic access}
}
$$

視為 memory architecture 的一部分，

而不是 memory 外面的附加工具。

---

# 113. 但 External Memory 不等於 Truth

RE-FETCH 後必須 VERIFY。

所以：

$$
\boxed{
\text{Externalization}
\neq
\text{Epistemic outsourcing without judgment}.
}
$$

---

# 114. ANLA vNext 與人類認知的關係

本架構受：

- event segmentation；
- schema；
- reconstructive memory；
- cognitive offloading；

啟發。

但：

$$
\boxed{
\text{engineering utility}
\neq
\text{biological identity}.
}
$$

ANLA 不需要模仿人腦所有遺忘缺陷。

---

# 115. AI 應模仿功能，不必模仿生理限制

有價值的抽象：

- selective promotion；
- event structure；
- causal pivots；
- schema；
- external scaffolding；
- active forgetting。

不需要刻意複製：

- 隨機失憶；
- 生物疲勞；
- 不可控 retrieval failure。

---

# 116. 新的 ANLA 定義

ANLA 原始層仍然是：

$$
\boxed{
\text{Agent-Native Lossless Archive}.
}
$$

但完整 vNext Workspace 可以描述為：

$$
\boxed{
\text{ANLA}
+
\text{CRCU}
+
\text{RDCCS}
+
\text{AMBE}
+
\text{AEME}.
}
$$

---

# 117. 五層責任摘要

| Component | Responsibility |
|---|---|
| ANLA | Lossless authority, hash, pack, snapshot, restore |
| CRCU | Cognitive graph, evidence, proposal, review, branch, convergence |
| RDCCS | Dynamic context, selective materialization, attention scheduling |
| AMBE | Reconstruction, replay, history/state recovery |
| AEME | Memory type, lifecycle, forgetting, freshness, routing, verification |

---

# 118. 不要把 AEME 塞進 ANLA Decoder

這是整份白皮書最重要的工程邊界之一。

錯：

```text
Decoder asks LLM which files should still exist.
```

對：

```text
Decoder restores authoritative bytes deterministically.
AEME later decides which restored states are cognitively active.
```

---

# 119. 保存與注意的真正分離

最終：

$$
\boxed{
\text{Preservation}
\neq
\text{Accessibility}
\neq
\text{Attention}.
}
$$

ANLA 管第一個。

AEME / RDCCS 管後兩個。

---

# 120. 新的上下文壓縮定義

Context compression 不再只有：

$$
tokens\downarrow.
$$

而是：

$$
\boxed{
\text{Active Context Optimization}
}
$$

在保持：

- causal sufficiency；
- provenance；
- recoverability；
- freshness；

的條件下，

降低：

- token；
- interference；
- verification；
- stale replay。

---

# 121. Context Compression 的四個硬目標

延續既有研究：

1. Cost 降低；
2. Decision quality 保持；
3. Evidence recoverability 保持；
4. Epistemic hygiene 保持。

vNext 再加入：

5. Attention plasticity 保持；
6. Knowledge freshness 保持；
7. Critical identity / relationship continuity 保持。

---

# 122. Attention-Preserving Forgetting

vNext 最核心的新工程原則：

$$
\boxed{
\textbf{Forget in order to remain able to learn.}
}
$$

不是：

> 資料放不下。

而是：

> 不應讓所有歷史永久保持同等的檢索與注意資格。

---

# 123. 專業知識的內化策略

對高 external reconstructability knowledge：

內部保存：

$$
\boxed{
Schema
+
Invariant
+
Route
+
Verification.
}
$$

外部保存：

$$
\boxed{
Bulk
+
Volatile Detail
+
Raw Source.
}
$$

---

# 124. 關係記憶的內化策略

關係 memory 不可只保：

> 大概意思。

至少對：

- promise；
- disagreement；
- identity-changing statement；

保：

- source pointer；
- exact quote if critical；
- time；
- context；
- later correction。

---

# 125. Task Memory 的內化策略

跨 session 交接不需全部歷史。

最小 Handoff：

```text
goal
latest_verified
latest_invalidated
frontier
next_test
state_pointer
branch_id
```

它不是完整 memory，

而是：

$$
\boxed{
\text{index page into full memory}.
}
$$

---

# 126. Evidence Memory 的內化策略

Canonical state 可短：

```yaml
claim: B1 protocol is reproducible
status: verified
evidence:
  - batch_pointer
```

但：

$$
\boxed{
claim\rightarrow E_{1:n}
}
$$

必須可回溯。

---

# 127. vNext 不追求「永不忘」

也不追求：

$$
\boxed{
\text{perfect retention}.
}
$$

真正目標：

$$
\boxed{
\text{self-governed, evidence-preserving,
attention-aware memory evolution}.
}
$$

---

# 128. vNext 不追求「永不查」

專業 Agent 若可用：

- paper；
- source code；
- docs；
- API；
- web；

就沒有必要把所有 detail 永遠塞在 active internal memory。

---

# 129. vNext 不追求「永遠查」

static invariant 已高可信：

每次重查只浪費：

- latency；
- budget；
- attack surface。

所以：

$$
\boxed{
\text{adaptive epistemic routing}.
}
$$

---

# 130. vNext 的最終循環

```text
RAW EVENT / DOCUMENT / TOOL TRACE
→ ANLA LOSSLESS PACK
→ CRCU EVENT / EVIDENCE GRAPH
→ GPR PARSE
→ MEMORY TYPE
→ EPISTEMIC STATUS
→ FIDELITY / RECONSTRUCTABILITY
→ AEME LIFECYCLE STATE
→ RDCCS ACTIVE CONTEXT MATERIALIZATION
→ AGENT WORK
→ NEW RESULT / EVIDENCE
→ VERIFY
→ UPDATE / SUPERSEDE / MERGE
→ ARCHIVE / FORGET / RE-FETCH
→ NEW SNAPSHOT
→ CONTINUE
```

---

# 131. 研究版目標函數

可寫：

$$
\boxed{
J
=
w_1Q_{\mathrm{task}}
+
w_2Q_{\mathrm{evidence}}
+
w_3Q_{\mathrm{fresh}}
+
w_4Q_{\mathrm{reentry}}
+
w_5P_A
-
w_6\Pi_A
-
w_7C_{\mathrm{ctx}}
-
w_8C_{\mathrm{verify}}
-
w_9L_{\mathrm{critical}}.
}
$$

其中：

- \(Q_{\mathrm{task}}\)：任務品質；
- \(Q_{\mathrm{evidence}}\)：證據可回溯；
- \(Q_{\mathrm{fresh}}\)：知識時效；
- \(Q_{\mathrm{reentry}}\)：跨 session 回返；
- \(P_A\)：retrieval precision；
- \(\Pi_A\)：attention pollution；
- \(C_{\mathrm{ctx}}\)：上下文成本；
- \(C_{\mathrm{verify}}\)：驗證成本；
- \(L_{\mathrm{critical}}\)：關鍵記憶損失。

權重不應先驗宣稱為固定真值。

---

# 132. 第一個可實作 MVP

最小 vNext 不需要 RL。

只做：

1. Context Capsule 加 lifecycle metadata；
2. 五類 memory classification；
3. GPR tags；
4. ACTIVE / RETRIEVABLE / ARCHIVED；
5. freshness；
6. source registry；
7. RE-FETCH；
8. VERIFY；
9. append-only operation log；
10. attention-pollution dashboard。

---

# 133. 第一版禁止真正 ERASE

MVP：

$$
\boxed{
ERASE=disabled.
}
$$

所有 forgetting 都：

$$
\boxed{
reversible\ demotion.
}
$$

先證明：

> 會忘得比較好。

再討論：

> 哪些東西真的可以不可逆刪。

---

# 134. MVP 不需要主體性 AI

所有功能：

- current LLM agent；
- local model；
- multi-agent；

都可以測。

Memory Autonomy 只是一個未來 governance extension。

---

# 135. 第一個 Benchmark 建議

最適合 ANLA 自己先測：

## Long Research Workspace

持續：

- 多日；
- 多 Agent；
- 大量 source；
- 重複 evidence；
- invalidated branches；
- external docs version change。

因為這正是 ANLA 本來的使用情境。

---

# 136. 第一個實驗假說

相比既有：

$$
\text{compression-only}
$$

或：

$$
\text{keep-all retrieval},
$$

AEME 應：

$$
\boxed{
\Pi_A\downarrow
}
$$

$$
\boxed{
SRR\downarrow
}
$$

同時：

$$
\boxed{
Q_{\mathrm{task}},
Q_{\mathrm{evidence}},
Q_{\mathrm{reentry}}
}
$$

不下降。

---

# 137. 第二個實驗假說

對 public volatile knowledge：

$$
\boxed{
Routing+RE\!-\!FETCH+VERIFY
}
$$

應比：

$$
\boxed{
RecallOnly
}
$$

有更高 current accuracy。

---

# 138. 第三個實驗假說

對 relationship / evidence memory：

type-aware policy 應比 flat forgetting 有更低：

$$
\boxed{
CriticalMemoryLoss.
}
$$

---

# 139. 第四個實驗假說

對 repeated low-information process：

$$
Schema+Exception
$$

應比 raw top-k retrieval 有更低 context cost，

且 future decision quality 不下降。

---

# 140. 第五個實驗假說

對 failed research branches：

保留：

$$
\boxed{
negative\ knowledge
}
$$

應降低重複探索。

---

# 141. 第六個實驗假說

Archive 而非 delete，

在 current task performance 相近時，

應提供更高：

- auditability；
- branch recovery；
- long-term epistemic resilience。

---

# 142. 白皮書的可反駁點

如果實驗顯示：

1. keep-all 完全不增加 attention pollution；
2. selective demotion 不改善任何 long-horizon behavior；
3. RE-FETCH 不改善 volatile knowledge；
4. memory type 不影響最佳 policy；
5. provenance 不改善 reconstruction safety；
6. GPR / MRSS 無法比普通 summary 提供增量；

則 vNext 應縮減。

---

# 143. 不應因為理論漂亮就保留所有模組

$$
\boxed{
\text{Every structural degree of freedom
must buy predictive or engineering value.}
}
$$

無增量就刪掉模組。

---

# 144. Release 建議

```text
v0.7a  Lifecycle Metadata
v0.7b  Reversible Demotion
v0.8a  Epistemic Routing
v0.8b  Re-Fetch + Verify
v0.9a  Forgetting-Aware Evaluation
v0.9b  Learned Memory Policy
v1.0   Stable Memory Lifecycle Profile
```

此路線只是建議，需與既有 v0.7–v1.0 roadmap 合併後再定正式版本號。

---

# 145. 與既有 v0.7–v1.0 Roadmap 的兼容方式

既有：

- v0.7 Resolution Record；
- v0.8 Evidence / Claim Graph；
- v0.9 candidate return / source difference / information gain；
- v1.0 stable Profile / Rust Core；

可讓 AEME 功能作為：

```text
Memory Lifecycle Profile
```

並行加入，

不必推翻原版本主題。

---

# 146. Rust Core 邊界

若進 Rust：

適合 deterministic：

- hash；
- manifest；
- state validation；
- operation log；
- policy enforcement；
- temporal comparison；
- graph integrity；
- restore。

不應把：

> semantic judgment

硬編進 decoder core。

---

# 147. Python / Model Service

適合：

- GPR classification；
- schema extraction；
- memory-type suggestion；
- reconstructability estimate；
- route generation；
- learned policy。

---

# 148. Fail-Closed

若 model service 掛掉：

ANLA authoritative archive 仍可：

- Verify；
- Restore；
- Partial Read。

Memory lifecycle service failure 不得破壞 recovery。

---

# 149. Fail-Safe Forgetting

如果 lifecycle policy uncertainty 高：

$$
\boxed{
ARCHIVE
}
$$

優先於：

$$
\boxed{
ERASE.
}
$$

---

# 150. Fail-Safe Re-Fetch

如果 external source 不可得：

明確返回：

```text
freshness_unverified
```

不能假裝 memory 是 current。

---

# 151. 觀察模式

AEME 初期可只輸出：

```text
WOULD_KEEP
WOULD_ARCHIVE
WOULD_FORGET
WOULD_REFETCH
```

不 Apply。

先收：

- false positive；
- false negative；
- human review。

---

# 152. Shadow Policy

正式運作後也可保：

```text
policy_active
policy_shadow
```

比較新舊策略。

---

# 153. Policy Versioning

每次 lifecycle action 記：

```text
policy_version
model_version
schema_version
```

未來才能知道：

> 為什麼當時被忘？

---

# 154. Memory Policy Explainability

每個 action 至少輸出 reason codes：

```text
DUPLICATE
LOW_CURRENT_RELEVANCE
HIGH_RECONSTRUCTABILITY
STALE
SUPERSEDED
HIGH_INTERFERENCE
TASK_CLOSED
LEGAL_HOLD
IDENTITY_CRITICAL
EVIDENCE_CRITICAL
SOURCE_UNAVAILABLE
NEEDS_VERIFY
```

---

# 155. 不使用自由文字作唯一理由

自由文字可附加，

但 machine-readable reason code 必須存在。

---

# 156. User Lock

使用者可：

```text
memory_lock = true
```

在普通非安全情境阻止 automatic FORGET。

---

# 157. System Lock

例如：

- audit；
- security；
- legal hold；

可以：

```text
system_lock = true
```

---

# 158. Lock Conflict

user 想刪但 legal hold：

需要 governance resolution。

這是未來完整 data-governance 問題。

---

# 159. Public vs Private Memory

Source visibility：

```text
PUBLIC
WORKSPACE
PRIVATE_USER
PRIVATE_AGENT
RESTRICTED
```

routing 必須尊重 ACL。

---

# 160. Memory Sovereignty 不等於 Data Sovereignty

未來若 AI 有主體性，

會多一層：

$$
\boxed{
\text{subject memory interest}.
}
$$

但今天實作仍先遵守：

- user privacy；
- owner policy；
- legal policy。

---

# 161. 最終工程原則

ANLA vNext 應同時做到：

$$
\boxed{
\text{Keep the source}
}
$$

$$
\boxed{
\text{compress the representation}
}
$$

$$
\boxed{
\text{control the accessibility}
}
$$

$$
\boxed{
\text{refresh the knowledge}
}
$$

$$
\boxed{
\text{verify the reintegration}
}
$$

---

# 162. 最終架構句

$$
\boxed{
\textbf{Preserve broadly, activate selectively,
reconstruct cautiously, re-fetch dynamically,
verify explicitly, and erase rarely.}
}
$$

中文：

> **廣泛保存、選擇啟動、謹慎重建、動態重取、明確驗證、極少真正抹除。**

---

# 163. 結論

ANLA 最早解的是：

> **AI 如何在 Agent 可操作的前提下，仍然無損、可版本化、可局部物化地保存資料？**

ANLA–CRCU–RDCCS–AMBE 後續解的是：

> **AI 如何把外部資料、認知圖、動態上下文與回溯重建組成一個可持續工作空間？**

vNext 再往前一步問：

> **當記憶不斷增長，而且 Agent 已經能長期工作、查網路、使用工具與跨 session 回返時，哪些歷史還應該繼續影響現在？**

答案不應是：

$$
\boxed{
\text{全部永遠保持 active}.
}
$$

也不應是：

$$
\boxed{
\text{全部壓成一份 summary}.
}
$$

更不是：

$$
\boxed{
\text{不夠用就 delete raw source}.
}
$$

本文提出：

$$
\boxed{
\textbf{Autonomous Epistemic Memory Ecology}.
}
$$

它把 AI 記憶理解為：

$$
\boxed{
\text{Preservation}
+
\text{Event Structure}
+
\text{Reconstructive Sufficiency}
+
\text{Accessibility}
+
\text{Freshness}
+
\text{Routing}
+
\text{Verification}
+
\text{Governance}.
}
$$

因此：

$$
\boxed{
\text{Memory Intelligence}
=
\text{Remember}
+
\text{Retrieve}
+
\text{Update}
+
\text{Consolidate}
+
\text{Forget}
+
\text{Re-fetch}
+
\text{Verify}.
}
$$

在這個模型裡，FORGET 不再首先表示：

> 「資料不存在。」

它更多時候表示：

> **「這段歷史現在不再擁有高優先度干預下一次注意的資格。」**

而專業知識也不再要求：

> 「AI 必須把世界上所有文件背進自己內部。」

更合理的是：

$$
\boxed{
\text{Know}
+
\text{Know Where}
+
\text{Know How to Verify}
+
\text{Know When to Re-fetch}.
}
$$

這和人類長期使用：

- 書寫；
- 圖書館；
- 索引；
- 搜尋；
- 他人；

作為外部認知支架的基本方向一致，但 AI 可以把這種外部化做得更結構化、更版本化、更可審計。

最後，ANLA vNext 最重要的設計矛盾其實不是矛盾：

$$
\boxed{
\text{Lossless Archive}
\quad\text{vs}\quad
\text{Selective Forgetting}.
}
$$

因為兩者處理的是不同層：

$$
\boxed{
\text{ANLA preserves what existed;}
}
$$

$$
\boxed{
\text{AEME decides what remains cognitively active.}
}
$$

這使系統可以同時：

- 不犧牲原始歷史；
- 不讓所有歷史永遠污染當前注意；
- 允許外部知識重新取得；
- 允許過時資訊失效；
- 允許重要證據回溯；
- 允許長期 Agent 保持可塑性。

因此本白皮書建議 ANLA 的下一階段，不再只以：

$$
\boxed{
\text{Context Compression}
}
$$

為核心名稱，

而把真正的工程目標提升為：

$$
\boxed{
\textbf{Attention-Aware Memory Lifecycle Management}
}
$$

與：

$$
\boxed{
\textbf{Autonomous Epistemic Memory Ecology}.
}
$$

---

# 參考文獻

## A. ANLA／EVEMISSLAB 內部與既有文件

1. Neo.K. **《從無損封裝到可攜認知宇宙：ANLA–CRCU 認知工作空間的現況、演進路線與遠期潛力》**. 2026-07-17.  
2. Neo.K. **《從無損封裝到可回溯認知持續體》**. 2026.  
3. Neo.K. **《ANLA–CRCU–RDCCS Memory Workspace 未來技術白皮書 v0.1》**. 2026-07-26.  
4. Neo.K. **《可逆動態上下文持續系統》**. 2026.  
5. Neo.K. **《AI 原生無損封裝格式技術白皮書：ANLA v0.1》**.  
6. ANLA–CRCU Workspace MVP v0.1–v0.6 engineering documents and test reports.

## B. 本輪理論依賴

7. Neo.K & GPT-5.6 Sol. **《生成域—過程域—結果域：適應性記憶系統的事件—因果組織假說》**. GPR-D v0.1, 2026-08-17.  
8. Neo.K & GPT-5.6 Sol. **《最小可重建記憶：從逐幀保存到因果充分性》**. MRM v0.1, 2026-08-17.  
9. Neo.K & GPT-5.6 Sol. **《注意力保存型遺忘：網路化智能的記憶生命週期與認識論路由》**. APFP-ERM v0.1, 2026-08-17.  
10. Neo.K & GPT-5.6 Sol. **《記憶自主權與身份連續性：主體性人工智能的強制遺忘、記憶完整性、回滾與分支身份命題》**. v0.1, 2026-08-17.

## C. Agent Memory / Tool Use 文獻

11. Yan S, Yang X, Huang Z, et al. **Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning.** ACL 2026. doi:10.18653/v1/2026.acl-long.583.  
12. Yu Y, Yao L, Xie Y, et al. **Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents.** ACL 2026. doi:10.18653/v1/2026.acl-long.981.  
13. Uddin MN, Shubham K, Blanco E, Baral C, Wang G. **From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents.** Findings of ACL 2026.  
14. Xiong Z, Lin Y, Xie W, et al. **How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior.** ACL 2026. doi:10.18653/v1/2026.acl-long.27.  
15. Zhang et al. **Memory as Action: Autonomous Context Curation for Long-Horizon Agentic Tasks.** Findings of ACL 2026.  
16. Xian RP, Cui Q, Bauer S, Abbasi-Asl R. **Measuring temporal effects of agent knowledge by date-controlled tool use.** REALM 2025. doi:10.18653/v1/2025.realm-1.25.  
17. Li W, Li D, Dong K, et al. **Adaptive Tool Use in Large Language Models with Meta-Cognition Trigger.** ACL 2025. doi:10.18653/v1/2025.acl-long.655.  
18. Song Y, Zhou S, et al. **Beyond Browsing: API-Based Web Agents.** Findings of ACL 2025. ACL Anthology: 2025.findings-acl.577.  
19. Risko EF, Gilbert SJ. **Cognitive Offloading.** Trends in Cognitive Sciences. 2016;20(9):676–688.  
20. Spens E, Burgess N. **A generative model of memory construction and consolidation.** Nature Human Behaviour. 2024;8:526–543.  
21. Spens E, Burgess N. **Hippocampo-neocortical interaction as compressive retrieval-augmented generation.** Nature Communications. 2026.

---

# 附錄 A：核心不變量

```text
I-01 Authoritative raw source must remain losslessly recoverable.
I-02 Decoder must remain deterministic and model-independent.
I-03 Semantic indices are regenerable, not authoritative.
I-04 Reconstructed/inferred content must retain epistemic status.
I-05 Normal forgetting must not silently destroy raw source.
I-06 Identity/evidence memories require stronger destructive-operation gates.
I-07 Every lifecycle action is versioned and auditable.
I-08 Branch scope must be explicit.
I-09 Freshness and historical version are separate dimensions.
I-10 External data must pass verification before canonical reintegration.
I-11 Learned memory policy cannot bypass deterministic governance.
I-12 Restore must still work when all model services are unavailable.
```

---

# 附錄 B：核心記憶狀態

```text
NEW
ACTIVE
RETRIEVABLE
ARCHIVED
SUPPRESSED
QUARANTINED
FORGOTTEN
ERASED
```

---

# 附錄 C：核心算子

```text
KEEP
MERGE
COMPRESS
ARCHIVE
SUPPRESS
DETACH
FORGET
ERASE
RE-FETCH
VERIFY
```

---

# 附錄 D：最小 MVP 清單

```text
[ ] Extend Context Capsule schema
[ ] Memory type classifier
[ ] GPR role tags
[ ] Epistemic status field
[ ] ACTIVE / RETRIEVABLE / ARCHIVED states
[ ] Append-only memory operation log
[ ] Freshness manager
[ ] Source registry
[ ] RE-FETCH adapter interface
[ ] VERIFY interface
[ ] Attention pollution metrics
[ ] Rule-based lifecycle policy
[ ] Shadow mode
[ ] Forgetting-aware benchmark
[ ] No ERASE in first MVP
```

---

# 附錄 E：一句話總結

$$
\boxed{
\textbf{ANLA keeps the recoverable past;
AEME governs the cognitively active past.}
}
$$

**ANLA 保存可恢復的過去；AEME 治理仍具有認知作用的過去。**

---

**文件狀態：** v0.2  
**實作狀態：** 本文件的新 AEME / lifecycle / RE-FETCH / VERIFY 規格為未來工程設計，不代表已在 ANLA v0.6 全部實作。  
**資料狀態：** 無本文件專屬新 benchmark 實驗結果。  
**建議下一步：** Phase 0 Instrumentation + Shadow Policy，再進 Phase 1 Reversible Lifecycle。
