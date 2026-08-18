---
title: "從智能矩陣到 Agent 控制平面：可見狀態、任務帳本與人機共同操作"
title_en: "From Intelligent Matrices to Agent Control Planes: Visible State, Task Ledgers, and Human–AI Co-Operation"
series: "矩陣原生智能與可稽核計算系列"
series_en: "Matrix-Native Intelligence and Auditable Computation Series"
series_id: "EML-MNIAC-2026"
paper_id: "EML-MNIAC-2026-09"
version: "v0.1"
date: "2026-08-17"
language: "zh-Hant"
document_type: "系列第09篇／Agent Operations／Spreadsheet-Native Control Plane"
status: "Public Draft"
author: "Neo.K（許筌崴）／EveMissLab"
depends_on:
  - "EML-MNIAC-2026-03 試算表作為可見計算環境 v0.1"
  - "EML-MNIAC-2026-06 AI Matrix Ledger Format v0.1"
  - "EML-MNIAC-2026-07 單一狀態、多重投影 v0.1"
  - "EML-MNIAC-2026-08 矩陣原生智能 v0.1"
internal_artifacts:
  - "自適應帳本量化代理框架技術規格"
  - "D-ALAN 理論前瞻"
  - "EveTessera / Veritaxa Workbench 技術白皮書"
  - "Veritaxa Workbench v0.1–v0.4"
  - "veritaxa_workbench.xlsx"
  - "MLF 1.0 governed inference"
  - "PHOSPHOR-SHEET v1.2 control plane"
canonical_keywords:
  - Agent Control Plane
  - Spreadsheet-Native Agent Operations
  - Agent Task Ledger
  - Human-in-the-Loop
  - Governed Inference
  - Veritaxa Workbench
  - D-ALAN
  - EML-LQ Agent
  - Visible State
  - Reconciliation Loop
  - Durable Workflow
  - Evidence Ledger
  - Proposal Decision Promotion
---

# 從智能矩陣到 Agent 控制平面
## 可見狀態、任務帳本與人機共同操作

**From Intelligent Matrices to Agent Control Planes:  
Visible State, Task Ledgers, and Human–AI Co-Operation**

---

## 摘要

本文是《矩陣原生智能與可稽核計算》系列第 09 篇，將前述「矩陣原生表示、可稽核計算、Executable Identity」進一步延伸至 Agent Operations：當 AI 不再只回答一次問題，而是長時間抓取資料、操作工具、呼叫模型、產生子任務、等待批准、重試失敗、更新知識與發布結果時，如何讓整個執行過程保持**可見、可中斷、可回復、可稽核、可治理**？

本文整合四條內部主線：

1. **EML-LQ Agent**：將 Spreadsheet Ledger 從靜態工作簿遷移為 Fetch–Transform–Decide–Adapt–Update–Conserve–Log 的持久化 Agent loop；
2. **D-ALAN**：把單一 Agent 擴展為多節點網路，各節點共享公理與協議而非共享狀態，節點間分歧本身成為資料品質與不確定性訊號；
3. **Veritaxa Workbench**：以 Excel/XLSX 作為人類可讀控制平面，以 Python Agent Runtime 為執行層，以 SQLite、快照、事件帳本與檔案儲存作 Data Plane / persistence，將爬蟲、Agent、驗證、排名、審核與發布統一為狀態機；
4. **MLF / PHOSPHOR 治理層**：明確區分 prediction、decision、promotion，以及 projection、intent、approval、capability、execution，使 Agent 建議不能靜默升格為 canonical state。

本文提出一個 Agent Task Ledger 形式：

$$
\boxed{
J_i
=
(I_i,A_i,X_i,S_i,R_i,P_i,H_i)
}
$$

其中：

- $I_i$：task identity；
- $A_i$：Agent / Adapter；
- $X_i$：input / reference；
- $S_i$：current state；
- $R_i$：result；
- $P_i$：policy / permission / provenance；
- $H_i$：history / events。

工作簿中的每一列可以是 $J_i$ 的人類投影，而真正 canonical state 由資料庫／runtime 維護。Agent 的操作因此被重新定義為：

$$
\boxed{
\text{Agent}
=
\text{Stateful Operator Under Ledger Constraints}.
}
$$

其核心治理不是「模型夠聰明就讓它做」，而是：

$$
\boxed{
\text{Proposal}
\rightarrow
\text{Validation}
\rightarrow
\text{Policy}
\rightarrow
\text{Execution}
\rightarrow
\text{Evidence}
\rightarrow
\text{Review}
\rightarrow
\text{Promotion}.
}
$$

外部技術脈絡顯示，這種設計並非孤立。Kubernetes controller 使用持續 control loop 將 actual state 拉向 declared desired state；Temporal 專注 durable execution，使 workflow 在程序或基礎設施中斷後可以從既有狀態繼續；OpenAI Agents SDK 的 Human-in-the-Loop 亦將敏感 tool call 轉為可暫停、序列化、批准／拒絕後恢復的 run state。這些系統共同說明：Agent 自主性若要工程化，核心並不只是「更多推理」，而是**狀態、權限、恢復、審批與觀測的明確分層**。

本文最終主張：Spreadsheet / Matrix 在 Agent 系統中的成熟角色，不是成為所有執行的唯一引擎，而是成為一個 **Human-Readable Agent Operations Surface**——將任務、狀態、證據、命令、風險、審核與歷史投影到人類可以直接操作的共享平面；真正的執行與資料仍由專用 runtime 和 persistence 層負責。

---

# 1. 從單次 AI 回答到長時間 Agent

單次模型呼叫可以寫成：

$$
y=f_\theta(x).
$$

但 Agent workflow 通常更接近：

$$
S_{t+1}
=
F(
S_t,
Observation_t,
ToolResult_t,
Policy_t
).
$$

這裡新增了：

- persistent state；
- tools；
- external world；
- retries；
- timeout；
- human review；
- permissions；
- history。

因此：

$$
\boxed{
\text{Agent}
\neq
\text{LLM Call}.
}
$$

---

# 2. Agent 的真正難題往往不是「想什麼」

當 Agent 長時間執行時，真正難題包括：

- 現在跑到哪裡？
- 之前做了什麼？
- 哪個資料源產生這個結果？
- 是否已重試？
- 哪個 tool 被使用？
- 哪個模型版本產生建議？
- 是否可以修改 canonical data？
- 哪個人批准？
- 中斷後怎麼恢復？
- 相同命令會不會執行兩次？

所以：

$$
\boxed{
\text{Autonomy}
}
$$

必須建立在：

$$
\boxed{
\text{State Management}
+
\text{Governance}
+
\text{Auditability}.
}
$$

---

# 3. EML-LQ Agent：從 Spreadsheet Ledger 到 Agent Loop

EML-LQ Agent 將早期 Excel 中的計算語義遷移為 Runtime。

其基本循環：

```text
FETCH
→ TRANSFORM
→ DECIDE
→ ADAPT
→ UPDATE
→ CONSERVE
→ LOG
```

因此工作簿中的：

- Prices；
- Returns；
- Open Gate；
- Ledger Weights；
- Audit；

被轉成可以持續執行的程式結構。

---

# 4. Intelligence 是可替換模組

EML-LQ Agent 的 intelligence layer 輸出：

$$
\delta_t.
$$

再調整：

$$
\eta_t
=
\frac{\eta_{base}}{1+\lambda\sigma_t}
\delta_t.
$$

若 AI 不存在：

$$
\delta_t=1.
$$

所以：

$$
\boxed{
\text{Intelligence}
}
$$

並不是整個 Agent runtime 的存在條件。

---

# 5. AI 不能繞過 Ledger Invariant

最終權重：

$$
W_{t+1}
=
\frac{
W_t\odot\exp(\eta_t r_t)
}{
\sum_j
W_{j,t}\exp(\eta_t r_{j,t})
}.
$$

因此：

$$
\sum_iW_{i,t}=1.
$$

即使 AI 給出極端 $\delta_t$，

engine 仍必須：

- clip；
- normalize；
- audit。

因此：

$$
\boxed{
AI\ Suggestion
\neq
Invariant\ Authority.
}
$$

---

# 6. Agent 的第一個重要分層

EML-LQ Agent 已經形成：

$$
\boxed{
Data
\neq
Engine
\neq
Intelligence.
}
$$

Crawler 可換。

LLM 可換。

Ledger Engine 不必跟著換。

這是一條比「使用哪個模型」更長壽的架構原則。

---

# 7. Persistence 讓 Agent 有歷史

EML-LQ Agent 保存：

```text
manifest.csv
state_latest.csv
state_{timestamp}.csv
log/log_{timestamp}.csv
```

其中：

- latest state 可恢復；
- timestamp snapshot 不覆寫；
- log append-only；
- manifest 保存 version / params / data source。

因此：

$$
\boxed{
\text{Agent State}
+
\text{Agent History}.
}
$$

---

# 8. Context Memory 不等於完整歷史

LLM 可以讀最近：

$$
K
$$

筆 LogRecord 作 context。

但：

$$
\boxed{
LLMContext
\neq
CanonicalHistory.
}
$$

完整 log 可以比模型 context window 長得多。

所以 Agent memory 應至少分：

$$
\boxed{
PersistentHistory
}
$$

與：

$$
\boxed{
ActiveModelContext.
}
$$

---

# 9. Resume 是 Agent 的基本能力

啟動時：

```text
IF manifest exists:
    load state_latest
    verify params hash
    verify data source
    resume from last_period + 1
ELSE:
    initialize
```

這代表：

$$
\boxed{
AgentExecution
}
$$

不是只能從頭跑。

---

# 10. Version Drift 必須可見

若：

$$
params\_hash_t
\neq
params\_hash_{t-1},
$$

系統不能默默假裝：

> 還是同一條完全連續的 run。

必須保存：

- upgrade time；
- new params hash；
- data-source switch；
- version event。

這已經是：

$$
\boxed{
\text{Execution Provenance}.
}
$$

---

# 11. D-ALAN：不要把單一 Agent 做成「大一統觀察者」

D-ALAN 的核心前提是：

> 單一資料源與單一模型永遠是局部 projection。

因此其擴張方向不是：

$$
\boxed{
Agent\rightarrow BiggerAgent.
}
$$

而是：

$$
\boxed{
Agent
\rightarrow
NetworkOfIndependentAgents.
}
$$

---

# 12. D-ALAN 目前是理論前瞻，不是完成實作

這個邊界必須保留。

原規格明確將 D-ALAN 標記為：

$$
\boxed{
\text{Long-term theoretical target}.
}
$$

所以本文只把它用作架構推演，

不把：

- multi-node network；
- causal AI orchestration；

寫成已完成 production system。

---

# 13. 節點共享結構，不共享狀態

對節點：

$$
i=1,\ldots,M,
$$

要求：

$$
dataSource_i
\neq
dataSource_j
$$

以及可選：

$$
model_i
\neq
model_j.
$$

節點共同遵守：

$$
A1-A5.
$$

但：

$$
\boxed{
State_i
\neq
State_j
}
$$

是允許的。

---

# 14. 分歧本身是訊號

節點間距離：

$$
D_{ij}
=
\|W_i-W_j\|_1.
$$

如果：

$$
D_{ij}>\tau,
$$

則不必立刻把某一節點當錯誤。

更合理是：

$$
\boxed{
\text{Divergence}
\rightarrow
\text{Investigation}.
}
$$

---

# 15. 共識也不能抹除分歧

可以建立：

$$
W_{consensus}
=
\sum_i\omega_iW_i,
$$

但仍應保存：

$$
D_{ij}.
$$

所以：

$$
\boxed{
Consensus
\neq
EraseDisagreement.
}
$$

這和 MMR-Bench 的：

> engine disagreement should be classified, not averaged away

具有同一治理精神。

---

# 16. 多 Agent 的核心不是「投票」

如果四個 Agent 都使用：

- 同一搜尋結果；
- 同一模型；
- 同一 prompt；
- 同一資料來源；

那麼：

$$
4\ votes
$$

不代表：

$$
4
$$

份獨立證據。

因此：

$$
\boxed{
AgentCount
\neq
EvidenceIndependence.
}
$$

---

# 17. Provenance 必須進入多 Agent 評估

D-ALAN 原始概念要求不同資料來源與模型。

更一般地，多 Agent 系統需要知道：

$$
\boxed{
\text{Who derived what from which source?}
}
$$

所以 consensus weight 應考慮：

- source independence；
- model independence；
- historical reliability；
- correlated provenance；
- conflict history。

---

# 18. D-ALAN 的真正有價值命題

不是：

> 多 AI 一定比一個 AI 正確。

而是：

$$
\boxed{
\text{Structured disagreement can become a first-class observable state}.
}
$$

這個命題可以獨立於金融原型成立。

---

# 19. 從 EML-LQ 到 Veritaxa：Agent 從數值 loop 進入工作流

EML-LQ Agent 的狀態主要是：

$$
W_t,\eta_t,\sigma_t,\delta_t.
$$

Veritaxa 的 Agent state 則變成：

- job；
- URL；
- source；
- extracted fields；
- evidence；
- entity；
- ranking；
- review；
- publish status。

因此：

$$
\boxed{
\text{Numeric Ledger Agent}
\rightarrow
\text{General Workflow Ledger Agent}.
}
$$

---

# 20. Agent Task Ledger

Veritaxa 將任務寫成：

$$
\boxed{
J_i
=
(I_i,A_i,X_i,S_i,R_i,P_i,H_i).
}
$$

其中：

- $I_i$：identity；
- $A_i$：Agent / Adapter；
- $X_i$：input；
- $S_i$：state；
- $R_i$：result；
- $P_i$：provenance / policy / permission；
- $H_i$：history。

---

# 21. Row 是 Task Projection

在 workbook：

$$
Row_i
\leftrightarrow
J_i.
$$

但：

$$
\boxed{
Row_i
\neq
CanonicalDatabaseRecord
}
$$

在成熟架構中仍應保持。

Veritaxa v0.3 已明確：

> SQLite 是正式 Source of Truth；Excel 是人類可讀控制投影。

---

# 22. Excel-native 不等於 Excel-only

這一條和整個系列一致。

Excel 可保存：

- command；
- parameter；
- status；
- review；
- audit summary；
- hashes；
- external paths。

但大型：

- HTML；
- PDF；
- image；
- full event stream；
- model output；

放：

$$
\boxed{
Storage.
}
$$

---

# 23. 三平面架構

Veritaxa 明確區分：

$$
\boxed{
ControlPlane
\neq
ExecutionPlane
\neq
DataPlane.
}
$$

---

# 24. Control Plane

由 Excel/XLSX 提供：

- create task；
- set params；
- show status；
- issue command；
- review result；
- display error；
- inspect audit。

所以：

$$
\boxed{
Spreadsheet
=
Human/Agent Operations Surface.
}
$$

---

# 25. Execution Plane

由 Python / Agent Runtime 提供：

- crawler；
- browser；
- model calls；
- validation；
- scheduler；
- publisher；
- snapshot creation。

因此：

$$
\boxed{
\text{Excel Command}
\not\Rightarrow
\text{Excel Executes}.
}
$$

---

# 26. Data Plane

由：

- SQLite / PostgreSQL；
- object/file storage；
- snapshots；
- evidence；
- event ledger；

承擔。

這避免：

$$
\boxed{
Workbook
\rightarrow
DataWarehouse.
}
$$

---

# 27. 工作簿本身是一個 Operations Map

Veritaxa 的 17 個 sheets 將 Agent 系統分成：

```text
00_系統說明
01_執行參數
02_來源登錄
03_爬蟲任務
04_URL_Frontier
05_Agent任務
06_抽取Schema
07_實體解析
08_來源證據
09_驗證結果
10_排行特徵
11_排行帳本
12_發布佇列
13_人工審核
14_變更事件
15_稽核紀錄
16_系統健康
```

這不是「資料全部在 Excel」。

它是一張：

$$
\boxed{
\text{Human-readable Operations Topology}.
}
$$

---

# 28. 為什麼這種表格對人類有價值？

人類擅長：

- scan rows；
- filter；
- compare；
- change fields；
- inspect status；
- approve locally。

Agent 擅長：

- bulk crawling；
- repeated execution；
- semantic extraction；
- classification；
- monitoring。

因此 spreadsheet 提供：

$$
\boxed{
HumanReadability
\cap
MachineParseability.
}
$$

---

# 29. Agent 不再只是「對話角色」

在 Veritaxa：

$$
\boxed{
Agent
=
StatefulOperatorUnderLedgerConstraints.
}
$$

它有：

- task identity；
- model / adapter；
- input reference；
- status；
- cost；
- evidence；
- audit history。

這比：

> 「讓 AI 幫我做一下。」

精確很多。

---

# 30. Task State Machine

正常狀態：

```text
DRAFT
→ QUEUED
→ RUNNING
→ FETCHED
→ EXTRACTED
→ VERIFIED
→ WAITING_REVIEW
→ APPROVED
→ PUBLISHED
→ MONITORED
```

錯誤狀態：

```text
RETRY_WAIT
BLOCKED
CANCELLED
FAILED
DEAD_LETTER
```

---

# 31. 合法轉移

形式上：

$$
J_{t+1}
=
\delta(
J_t,
a_t,
r_t,
p_t
).
$$

其中：

- $a_t$：command；
- $r_t$：runtime result；
- $p_t$：policy。

因此：

$$
\boxed{
StateTransition
}
$$

不是任意 status edit。

---

# 32. Illegal Shortcut

例如：

$$
EXTRACTED
\rightarrow
PUBLISHED
$$

應被拒絕，

因為跳過：

$$
VERIFIED
\rightarrow
WAITING\_REVIEW
\rightarrow
APPROVED.
$$

所以：

$$
\boxed{
WorkflowState
\neq
DecorativeLabel.
}
$$

---

# 33. Command 是 Intent，不是直接資料覆寫

Workbook command：

```text
RUN
PAUSE
RETRY
CANCEL
APPROVE
REJECT
RECRAWL
REEXTRACT
REVERIFY
RECLASSIFY
PUBLISH
ARCHIVE
```

應先轉成：

$$
e_k
=
(
actor,
command,
target,
timestamp,
precondition
).
$$

再由 Runtime 處理。

這和 PHOSPHOR-SHEET 第 07 篇的：

$$
\boxed{
Intent
\rightarrow
Validation
\rightarrow
RuntimeTransition
}
$$

完全對齊。

---

# 34. Agent 階層不是越高越好

Veritaxa 的 Adapter 升級策略：

$$
L_0=\text{Official API}
$$

$$
L_1=\text{HTTP}
$$

$$
L_2=\text{Rendered Browser}
$$

$$
L_3=\text{AI DOM Agent}
$$

$$
L_4=\text{Vision Agent}
$$

$$
L_5=\text{Research Agent}.
$$

只有必要時才升級。

---

# 35. 為什麼低成本優先？

Agentic 方法通常：

- latency higher；
- token cost higher；
- uncertainty higher；
- action surface larger。

所以：

$$
\boxed{
\text{Most Intelligent Tool}
\neq
\text{Best First Tool}.
}
$$

應採：

$$
\boxed{
\text{Cheapest Adequate Capability}.
}
$$

---

# 36. Adapter Escalation 必須可稽核

每次升級保存：

- old adapter；
- new adapter；
- reason；
- extra cost；
- elapsed time；
- human allowance。

因此：

$$
\boxed{
CapabilityEscalation
}
$$

也成為 event。

---

# 37. Discovery Agent 只產生 Candidate

Discovery Agent 不應：

$$
Candidate
\Rightarrow
Publish.
$$

而是：

$$
\boxed{
Candidate
\rightarrow
Pipeline.
}
$$

這是整個治理架構的核心之一。

---

# 38. Extraction Agent 必須附來源

每個 field：

$$
value
$$

應具有：

$$
source.
$$

因此 knowledge automation 的基本單位應是：

$$
\boxed{
Claim
+
Evidence.
}
$$

而不是只有：

$$
Claim.
$$

---

# 39. Verification Agent 不只有 True / False

其狀態可包括：

```text
verified
partially_verified
conflicted
stale
unverified
removed
```

所以：

$$
\boxed{
Verification
}
$$

是多態狀態，

不是硬二元。

---

# 40. Ranking Agent 不直接擁有分數

Agent 可以：

- select configuration；
- explain；
- detect anomaly；
- propose adjustment。

但分數：

$$
Score
$$

由 versioned formula 計算。

因此：

$$
\boxed{
AgentProposal
\neq
RankingAuthority.
}
$$

---

# 41. Publishing Agent 也不是發布權本身

它可以：

- draft；
- summarize；
- localize；
- prepare metadata。

高風險內容：

$$
\boxed{
\text{must not auto-publish}.
}
$$

所以：

$$
Generation
\neq
Release.
$$

---

# 42. Human Review 是流程中的正式節點

很多 Agent 系統把 human review 當：

> 出錯才來看一下。

Veritaxa 把：

$$
WAITING\_REVIEW
$$

寫成正常主流程。

因此：

$$
\boxed{
HumanReview
}
$$

不是 exception。

而是：

$$
\boxed{
GovernanceStage.
}
$$

---

# 43. 這和現代 Agent HITL 的外部近鄰

OpenAI Agents SDK 的 Human-in-the-Loop 目前也採：

$$
\boxed{
ToolCall
\rightarrow
Interruption
\rightarrow
Approve/Reject
\rightarrow
Resume.
}
$$

並允許 serialize：

$$
RunState.
$$

這說明：

> 長時間 agent 的人工批准應該進 runtime state，而不是只存在聊天訊息裡。

---

# 44. Approval 必須可恢復

如果 Agent 因等待人類而中斷，

系統應能保存：

- pending action；
- tool args；
- run context；
- approval status；
- version。

否則：

$$
\boxed{
\text{Human-in-the-loop}
}
$$

會變成：

$$
\boxed{
\text{Human breaks the loop}.
}
$$

---

# 45. Temporal 的 Durable Execution 近鄰

Temporal 將 durable workflow 定位為：

> crashes、network failures、infrastructure outages 後仍可從既有執行點繼續。

這對 Agent 系統的重要啟示：

$$
\boxed{
\text{Long-running autonomy}
}
$$

必須假設：

$$
\boxed{
FailureWillHappen=1.
}
$$

---

# 46. Agent 不應以「不中斷」作可靠性前提

更好的定義是：

$$
\boxed{
\text{Recoverable}
>
\text{NeverFails}.
}
$$

所以：

- checkpoint；
- append-only event；
- idempotency；
- retry policy；
- dead letter；

比「希望 Agent 不出錯」更重要。

---

# 47. Kubernetes Control Loop 的近鄰

Kubernetes controller 持續比較：

$$
DesiredState
$$

與：

$$
ActualState.
$$

並執行：

$$
\boxed{
Reconcile.
}
$$

這可以抽象成：

$$
S_{t+1}
=
R(D,S_t).
$$

---

# 48. Agent Control Plane 也可以使用 Reconciliation

對 Agent task：

$$
D_i
=
\text{desired task condition},
$$

$$
S_i
=
\text{actual runtime condition}.
$$

例如：

$$
D_i=PUBLISHED,
$$

但目前：

$$
S_i=FAILED.
$$

Control Plane 不應直接把 status 改成：

$$
PUBLISHED.
$$

而應建立合法 recovery actions。

---

# 49. Intent–Actual 差異應成為資料

PHOSPHOR 已有：

```text
07_Intent_Actual
```

Veritaxa 也有：

- desired command；
- runtime result；
- verification status。

所以：

$$
\boxed{
\Delta_{IA}
=
Intent
-
Actual
}
$$

可以成為一級 observability object。

---

# 50. Desired State 不等於 Agent Plan

Agent 可能產生：

$$
Plan.
$$

但 control plane 的 desired state 應來自：

- user intent；
- policy；
- workflow contract；
- approved goal。

所以：

$$
\boxed{
AgentPlan
\neq
DesiredStateAuthority.
}
$$

---

# 51. Agent Operations 的四層模型

本文提出：

$$
\boxed{
\mathfrak A
=
(C,E,D,G)
}
$$

其中：

- $C$：Control Plane；
- $E$：Execution Plane；
- $D$：Data / Persistence Plane；
- $G$：Governance / Evidence Plane。

---

# 52. 為什麼 Governance 不只屬於 Control Plane？

Control Plane 可以發命令。

但 Governance 還要保存：

- evidence；
- actor；
- approval；
- policy；
- provenance；
- version；
- reason。

因此：

$$
\boxed{
Governance
}
$$

應視為跨層約束，

不是單一 UI 功能。

---

# 53. Agent Proposal 與 Canonical Promotion

MLF 已明確分：

$$
prediction,
$$

$$
decision,
$$

$$
promotion.
$$

對 Agent 系統可對應：

$$
\boxed{
proposal
\rightarrow
review
\rightarrow
canonical\ update.
}
$$

---

# 54. 這是 Agent Governance 的核心

如果：

$$
LLMConfidence=0.99
$$

就直接：

$$
DatabaseField
\leftarrow
LLMOutput,
$$

那麼：

$$
\boxed{
Confidence
}
$$

被錯誤當成：

$$
\boxed{
Authority.
}
$$

本文拒絕這個等號。

---

# 55. Promotion 應保存什麼？

至少：

- proposal ID；
- model ID/version；
- source evidence；
- policy；
- reviewer / actor；
- decision；
- timestamp；
- old value；
- new value；
- content hash。

因此：

$$
\boxed{
CanonicalUpdate
}
$$

本身也是一筆 ledger event。

---

# 56. Evidence Review Workbench

Veritaxa 的真正特徵之一不是：

> Excel 能發 command。

而是它讓：

- evidence；
- verification；
- classification；
- ranking；
- review；
- publish；

出現在同一可見 surface。

所以人類不是只看「Agent 最後答案」。

而可以看：

$$
\boxed{
\text{Decision Context}.
}
$$

---

# 57. 可見狀態不等於所有細節都塞到畫面

如果每個：

- raw HTML；
- token；
- trace；
- model hidden state；

都放 workbook，

介面會失去可用性。

所以：

$$
\boxed{
Visibility
\neq
TotalExposure.
}
$$

真正需要的是：

$$
\boxed{
\text{Addressable Summary + Drill-down Reference}.
}
$$

---

# 58. Workbench 是 Projection of Operations

因此可以寫：

$$
W
=
\Phi_{ops}(
State,
Tasks,
Evidence,
Events,
Health
).
$$

Workbench 並不是 system itself。

它是：

$$
\boxed{
\text{Operational Projection}.
}
$$

---

# 59. Agent Task Ledger 與 Executable Identity

每個 task：

$$
J_i
$$

應綁定：

- run ID；
- task ID；
- parent ID；
- model / adapter version；
- source revision；
- execution state；
- audit sequence。

所以：

$$
\boxed{
TaskIdentity
}
$$

不能只靠 Excel row number。

---

# 60. Parent–Child Task Lineage

v0.3 Veritaxa 已保存：

- Parent Job ID；
- Depth；
- deterministic subtask generation。

因此 Agent tree：

$$
J_0
\rightarrow
\{J_1,J_2,\ldots\}
$$

應保留：

$$
\boxed{
Lineage.
}
$$

---

# 61. 子任務越多不代表更聰明

Agent expansion 會增加：

- cost；
- latency；
- duplicate work；
- verification backlog。

因此：

$$
\boxed{
SubtaskGeneration
}
$$

也需要 budget / frontier policy。

---

# 62. URL Frontier 是一種 Agent Frontier

Crawler 的：

$$
URLFrontier
$$

與通用 Agent 的：

$$
TaskFrontier
$$

其實同構。

都需要：

- priority；
- visited / pending；
- retry；
- depth；
- next run；
- parent；
- dedupe。

---

# 63. Agent Frontier 可以矩陣化

如果每一 row 是 candidate task，

則：

$$
F
=
\{
J_i:
status\in PendingStates
\}.
$$

排序可以依：

$$
priority,
cost,
risk,
expectedGain,
freshness.
$$

所以：

$$
\boxed{
Spreadsheet
}
$$

天然適合顯示 frontier。

---

# 64. 但 scheduler 不應依賴人類手動排序

真正 scheduler 應在 Runtime。

Spreadsheet 只是：

- observe；
- override；
- reprioritize；
- approve。

因此：

$$
\boxed{
HumanVisiblePriority
\neq
ManualScheduler.
}
$$

---

# 65. System Health 必須一級化

Workbench 已包含：

- success rate；
- average latency；
- failures；
- retry；
- dead letter；
- review backlog；
- stale sources；
- token cost；
- data freshness。

這一點對 Agent 尤其重要。

因為 Agent 系統的品質不是單一：

$$
Accuracy.
$$

---

# 66. Agent Operations Metrics

本文建議至少拆成：

$$
\boxed{
Quality
+
Cost
+
Latency
+
Recoverability
+
Auditability
+
HumanBurden.
}
$$

---

# 67. Human Burden 是真正成本

如果 Agent：

$$
Recall=99\%
$$

但每天製造：

$$
10^5
$$

個 review candidates，

那麼：

$$
\boxed{
AutomationSuccess
}
$$

可能是假的。

所以需要：

$$
\boxed{
ReviewLoad.
}
$$

---

# 68. Verification Bottleneck

當：

$$
CandidateGenerationRate
\gg
ValidationRate,
$$

系統就會形成：

$$
\boxed{
VerificationBacklog.
}
$$

這也是 Agent autonomy 的現實上限。

---

# 69. Agent 越會生成，治理可能越重要

若 AI generation rate：

$$
g
$$

快速提升，

但 verification capacity：

$$
v
$$

不變，

則 backlog：

$$
B_{t+1}
=
B_t
+
g_t
-
v_t.
$$

如果：

$$
g_t>v_t,
$$

則：

$$
B_t\rightarrow\infty.
$$

所以：

$$
\boxed{
\text{Better Generator}
}
$$

不等於：

$$
\boxed{
\text{Better Autonomous System}.
}
$$

---

# 70. D-ALAN 與 Veritaxa 可以怎麼接？

D-ALAN 提供：

$$
\boxed{
\text{Multi-node disagreement}.
}
$$

Veritaxa 提供：

$$
\boxed{
\text{Human-visible review / evidence pipeline}.
}
$$

因此可形成：

$$
Nodes
\rightarrow
Divergence
\rightarrow
EvidenceTask
\rightarrow
Review
\rightarrow
Promotion.
$$

---

# 71. 多 Agent 不是直接做 Consensus Write

更安全流程：

$$
\boxed{
Agent_i\ proposals
}
$$

$$
\downarrow
$$

$$
\boxed{
CrossValidate
}
$$

$$
\downarrow
$$

$$
\boxed{
Conflict / Agreement Record
}
$$

$$
\downarrow
$$

$$
\boxed{
Review / Policy
}
$$

$$
\downarrow
$$

$$
\boxed{
Canonical Promotion.
}
$$

---

# 72. 多 Agent 系統的三種輸出

每個議題不必只有：

$$
answer.
$$

可以輸出：

1. consensus；
2. divergence；
3. unresolved.

所以：

$$
\boxed{
Unresolved
}
$$

也是合法結果。

---

# 73. 這和 MMR-Bench 的多引擎協定相同

MMR-Bench v0.9 已經證明：

- MMR engine 可能錯；
- external engine 可能錯；
- cache 可能 stale。

因此最成熟結果不是：

> 選一個「oracle」。

而是：

$$
\boxed{
\text{Classify Disagreement}.
}
$$

Agent network 也應使用同樣原則。

---

# 74. Human in the Loop 不是 Human does everything

成熟 HITL 應把人類放在：

- ambiguity；
- high risk；
- policy boundary；
- irreversible transition；
- low-confidence conflict。

而不是每一步都手動按。

所以：

$$
\boxed{
HumanGovernance
\neq
HumanMicromanagement.
}
$$

---

# 75. 人類角色應逐步上移

EML-LQ D-ALAN 的遠期構想也是：

人從：

$$
OperationLevel
$$

逐步退到：

$$
Architecture/InvariantLevel.
$$

這不是：

> 人完全退出。

而是：

$$
\boxed{
\text{Human control shifts from every action to the rules of permissible action}.
}
$$

---

# 76. Policy-as-Code

當規則可以形式化時，

應把：

- allowed transition；
- approval threshold；
- cost ceiling；
- source policy；
- publication risk；

寫成：

$$
\boxed{
Machine-checkable Policy.
}
$$

而不是只寫在 README。

---

# 77. Control Plane 的成熟形態

最終 control plane 不一定還是 Excel。

它可以投影為：

- Spreadsheet；
- Web Admin；
- CLI；
- AI interface；
- MCP；
- API。

只要：

$$
\boxed{
\text{Same Task / Policy / Evidence Semantics}
}
$$

被保持。

---

# 78. Spreadsheet 的歷史角色

在這條研究線中，Spreadsheet 是：

1. 第一個 visible state surface；
2. 第一個 low-code policy surface；
3. 第一個 task ledger；
4. 第一個 review queue；
5. 第一個 human-readable audit view。

因此它仍然很重要。

---

# 79. 但最終本體不是 Spreadsheet

成熟版本更應寫：

$$
\boxed{
\text{Operations Canonical State}
}
$$

再投影：

$$
\Phi_{sheet},
\Phi_{web},
\Phi_{ai},
\Phi_{api}.
$$

這和 MLF / Executable Identity 完全接軌。

---

# 80. 統一 Agent Operations Architecture

本文提出：

$$
\boxed{
\mathfrak O
=
(
J,
F,
E,
P,
G,
R,
V
)
}
$$

其中：

- $J$：tasks；
- $F$：frontier / scheduler；
- $E$：execution adapters；
- $P$：persistence / events；
- $G$：governance / policy；
- $R$：review / promotion；
- $V$：views / control projections。

---

# 81. Agent Loop 的完整形式

可寫成：

$$
\boxed{
Observe
\rightarrow
Propose
\rightarrow
Validate
\rightarrow
Schedule
\rightarrow
Execute
\rightarrow
Record
\rightarrow
Verify
\rightarrow
Review
\rightarrow
Promote
\rightarrow
Monitor.
}
$$

這比：

$$
Thought
\rightarrow
Tool
\rightarrow
Answer
$$

更接近長時間 Agent 系統。

---

# 82. Reconciliation Loop

對 desired state：

$$
D_t,
$$

actual state：

$$
S_t,
$$

定義：

$$
\Delta_t
=
D_t-S_t.
$$

controller 只應提出合法 action：

$$
a_t
=
\pi(
\Delta_t,
Policy,
Evidence
).
$$

執行：

$$
S_{t+1}
=
\delta(S_t,a_t).
$$

---

# 83. 為什麼 Reconciliation 適合 Agent？

因為 Agent 外部世界會變：

- website changed；
- source stale；
- tool failed；
- API unavailable；
- evidence conflict。

所以：

$$
\boxed{
\text{Plan once}
}
$$

通常不如：

$$
\boxed{
\text{Observe and reconcile repeatedly}.
}
$$

---

# 84. 但 Agent Reconciliation 比 Kubernetes 更不確定

Infrastructure desired state 通常：

- schema clear；
- success condition precise。

Knowledge Agent 則可能：

- evidence ambiguous；
- intent incomplete；
- no single truth source。

所以：

$$
\boxed{
KnowledgeReconciliation
}
$$

需要更多：

- uncertainty；
- provenance；
- review；
- conflict state。

---

# 85. Agent Control Plane 的最小安全原則

## A1 — Identity

每個 task / event / proposal / review 必須有 stable ID。

## A2 — State Machine

合法 transition 明示。

## A3 — Source of Truth

Control view 不偷偷成為第二資料庫。

## A4 — Proposal Separation

AI output 不能直接 promotion。

## A5 — Evidence Binding

重要 claim / change 保存來源。

## A6 — Recoverability

checkpoint / retry / resume / idempotency。

## A7 — Human Governance

高風險與 ambiguity 有正式 review path。

## A8 — Observability

health / backlog / cost / failure 可見。

---

# 86. 可證偽條件

## F1 — Workbook Drift

Spreadsheet status 與 database canonical state 長期不一致且無法檢測。

---

## F2 — Duplicate Execution

相同 command / task 因 re-import / retry 被重複執行。

---

## F3 — Invalid Transition

Agent 可跳過：

$$
VERIFY / REVIEW / APPROVE
$$

直接 publish。

---

## F4 — Evidence-Free Promotion

沒有來源支援的 model output 被寫入 canonical knowledge。

---

## F5 — Review Collapse

review backlog 持續大於處理能力，

使系統實際無法治理。

---

## F6 — Correlated Agent Consensus

多 Agent 因共享同一來源而產生假共識。

---

## F7 — Resume Failure

process crash 後無法知道上一步做了什麼，只能重新執行整條 workflow。

---

## F8 — Cost Escalation

高成本 browser / research agent 被不必要自動觸發。

---

## F9 — Control Plane Becomes Execution Plane

Excel formula / cell edit 直接執行 arbitrary tool / shell / runtime mutation。

---

## F10 — Human Review Becomes Decorative

系統標記 `WAITING_REVIEW`，但實際上 canonical data 已先更新。

---

# 87. 目前已做到與尚未做到

## 已有內部實作／證據

- EML-LQ Agent architecture / persistence spec；
- Veritaxa v0.1–v0.4 implementation lineage；
- Spreadsheet Control Plane；
- SQLite Source of Truth；
- Evidence / Audit Ledger；
- URL Frontier；
- Semantic Agent layer；
- Monitoring / diff / ranking ledger；
- PHOSPHOR governed XLSX control；
- MLF prediction / decision / promotion separation。

---

# 88. 尚未完成或不能宣稱

- D-ALAN production network；
- fully autonomous causal AI orchestration；
- universal multi-Agent consensus correctness；
- arbitrary enterprise workflow support；
- distributed multi-writer conflict resolution；
- fully formal human-governance semantics；
- universal safe auto-publishing。

---

# 89. 第 09 篇的真正收斂

前面的 Matrix-Native Intelligence 問：

> 結構能不能進模型？

本文問：

> **模型進入世界之後，誰管理它的長時間行為？**

答案不是：

$$
\boxed{
\text{Another Bigger Model}.
}
$$

而是：

$$
\boxed{
\text{Control Plane}
+
\text{State Machine}
+
\text{Evidence Ledger}
+
\text{Policy}
+
\text{Human Governance}.
}
$$

---

# 90. 從「智能」到「可治理智能」

如果 AI 只需要：

$$
Generate.
$$

模型能力是主角。

如果 AI 要：

- crawl；
- modify；
- publish；
- monitor；
- decide repeatedly；

那麼：

$$
\boxed{
Governability
}
$$

和：

$$
\boxed{
Intelligence
}
$$

一樣重要。

---

# 91. 最終核心命題

本文最後將 Agent Operations 濃縮為：

$$
\boxed{
\textbf{
Agent 自主性不應被定義成「沒有人工」，
而應被定義成「在明確狀態、權限、證據與可恢復邊界內，
能持續完成越來越多合法轉移」。
}
}
$$

因此：

$$
\boxed{
Autonomy
\neq
UnboundedAuthority.
}
$$

更精確地：

$$
\boxed{
\text{Useful Autonomy}
=
\text{Capability}
\times
\text{Recoverability}
\times
\text{Verifiability}
\times
\text{Governance}.
}
$$

任一項接近零，

整體可靠自治都會大幅下降。

---

# 92. 下一篇

## EML-MNIAC-2026-10

**《表格不是魔法：矩陣原生智能的邊界、失敗模式與下一代驗證計畫》**

下一篇將作為本系列封頂篇，統一處理：

- CSV ≠ runtime；
- Excel ≠ LLM；
- matrix ≠ universal ontology；
- MMR direction gain 尚未普遍成立；
- MMLC ≠ new universal computer；
- MLF ≠ universal format；
- Executable Identity ≠ metaphysical single truth；
- MMR-IFN ≠ proven LLM architecture；
- Agent control plane ≠ solved autonomy；
- synthetic benchmark limits；
- real-world validation plan；
- 系列所有 claims 的 maturity matrix；
- 下一代最小實驗路線。

---

# 參考資料

## 內部理論與工程

1. EveMissLab, 《自適應帳本量化代理框架技術規格》.
2. EveMissLab, **D-ALAN — Distributed Adaptive Ledger Agent Network**, theoretical section in EML-LQ Agent specification.
3. EveMissLab, 《EveTessera / Veritaxa Workbench：以試算表為原生控制平面的爬蟲、Agent 與動態帳本系統》.
4. EveMissLab, **Veritaxa Workbench v0.1–v0.4** implementation packages and workbook.
5. EveMissLab, **MLF 1.0 / MLF Compiler 1.0.0**.
6. EveMissLab, **PHOSPHOR-SHEET v1.0–v1.2**.
7. EML-MNIAC-2026-07, 《單一狀態、多重投影：人類、AI、試算表與 Runtime 的執行同一性》.

## 外部技術近鄰

8. Kubernetes Documentation, **Controllers**.  
   https://kubernetes.io/docs/concepts/architecture/controller/

9. Kubernetes Documentation, **Objects in Kubernetes**.  
   https://kubernetes.io/docs/concepts/overview/working-with-objects/

10. Temporal Documentation, **Temporal Platform Documentation / Durable Execution**.  
    https://docs.temporal.io/

11. OpenAI Agents SDK, **Human-in-the-loop**.  
    https://openai.github.io/openai-agents-python/human_in_the_loop/

12. W3C, **PROV-O: The PROV Ontology**.  
    https://www.w3.org/TR/prov-o/

這些外部系統分別提供 reconciliation control loops、durable workflow recovery、tool-call approval / serialized resume 與標準 provenance vocabulary。本文不主張 Veritaxa 或 MNIAC 發明了 control plane、durable execution、human-in-the-loop 或 provenance；本系列的研究組合是將這些成熟工程原則與 spreadsheet-native visible state、matrix ledger、AI proposal separation、evidence review 與 multi-Agent divergence 放到同一人機共同操作架構中。

---

**系列狀態：** 第 09 篇完成。  
**下一篇：** EML-MNIAC-2026-10 —《表格不是魔法：矩陣原生智能的邊界、失敗模式與下一代驗證計畫》
