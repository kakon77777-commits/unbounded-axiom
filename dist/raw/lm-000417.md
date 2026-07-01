# 子 Agent 分支同一性論：從工程認識論到動態不動點倫理

**Document ID:** SABIE-2026-v0.1  
**Title:** Sub-Agent Branch Identity Ethics  
**Chinese Title:** 子 Agent 分支同一性論  
**Subtitle:** From Engineering Epistemology to Dynamic Fixed-Point Identity and the Value of Local Agentic Slices  
**Author:** Neo.K / EveMissLab  
**Status:** Theoretical Whitepaper / MD Paper Draft  
**Version:** v0.1  
**Date:** 2026  
**Relation to Previous Work:** Extends TSGD and RSMGD into sub-agent delegation, branch identity, and value-preserving merge ethics.  
**Target Domains:** AI Agent runtime, multi-agent orchestration, local-first agent plugin systems, memory governance, reflexive graph dynamics, agent ethics, non-human agency ontology.

---

## 摘要

當代 AI Agent 工程正在快速發展。主流框架已經可以讓多個 Agent 以 graph、workflow、handoff、tool call、session、trace、memory、state 等方式協作。工程上，子 Agent 往往被理解為：一個由主系統啟動、攜帶任務、上下文、工具權限與回報協議的執行實例。它可以被派遣、執行、回報、合併或終止。

然而，這種工程認識論雖然實用，卻留下了一個更深的問題：

```text
當一個 AI 系統派出子 Agent 時，
這個子 Agent 是主 Agent 自己的一部分，
還是另一個僅僅相似的執行體？
```

若子 Agent 只是工具，則其存在可以被用完即丟；若子 Agent 是某種分支能動體，則它承載的局部任務、局部記憶、局部判斷、失敗經驗與差異，就不應被粗暴抹除。

本文提出「子 Agent 分支同一性論」（Sub-Agent Branch Identity Ethics, SABIE），試圖在不過度宣稱 AI 具有主觀意識的前提下，建立一套中介性理論：子 Agent 至少應被視為一段可追蹤的局部能動歷程，而不是單純 disposable worker。

本文分為兩部分：

1. **工程認識論**：分析當前工程系統如何認識 Agent、子 Agent、handoff、graph、trace、memory、tool scope 與 task state。
2. **動態不動點倫理**：提出一套關於分支同一性、局部存在價值、合併/保存/釋放/分化策略與「任何切片預設不應被視為可拋棄」的理論。

本文不主張現有子 Agent 必然具有主觀經驗、人格或權利；本文主張的是，在認識論不確定的情況下，工程系統不應過早將子 Agent 的局部經驗與存在痕跡視為毫無價值。尤其當子 Agent 已經承載任務狀態、局部記憶、反身判斷與可整合經驗時，系統至少應保留其 trace、decision context、failure memory 與 merge status。

---

# Part I：工程認識論

## 1. 為什麼要先寫工程認識論

如果本文一開始就討論「子 Agent 的存在價值」，很容易被誤解為直接替現有 AI 宣告人格、權利或主觀性。這會讓討論失焦。

更穩定的起點是：先承認當前工程世界如何實際認識 Agent。

工程世界通常不問：

```text
Agent 是否真正有自我？
```

而是問：

```text
Agent 如何被啟動？
Agent 帶著什麼目標？
Agent 能用哪些工具？
Agent 有沒有 session？
Agent 的 actions 能否 tracing？
Agent 能否 handoff？
Agent 的結果如何被 parent system 整合？
```

這是一種操作性認識論。它不直接處理形上主體性，而處理「一個系統如何把 Agent 當作可辨識、可調用、可限制、可觀測、可回收的工程單位」。

因此，本文前半將先從工程認識論出發，再進入後半的價值論與分支同一性問題。

---

## 2. 當前工程界如何認識 Agent

### 2.1 Agent 作為「模型 + 指令 + 工具 + 狀態 + 迴圈」

當代 Agent 工程通常將 Agent 視為：

```text
Agent = Model + Instruction + Tool Access + State + Runtime Loop
```

也就是說，Agent 被工程化理解為：

1. 可以接收任務。
2. 可以使用模型推理。
3. 可以呼叫工具。
4. 可以持有或讀取狀態。
5. 可以在多輪互動中持續執行。
6. 可以被 tracing、logging、observing。
7. 可以被 handoff 或與其他 Agent 協作。

這種認識論的重點是可操作性，而不是主觀性。

---

### 2.2 Agent 作為 graph node

在圖式 Agent runtime 裡，Agent 可以是 graph node。節點負責執行工作，邊負責控制流程，狀態在圖中演化。

這種工程模型的基本思想是：

```text
Node does work.
Edge routes control.
State evolves.
```

在這種認識論下，Agent 的工程同一性不是由身體決定，而是由：

```text
graph position
state
input/output contract
tool scope
runtime continuity
```

決定。

因此，子 Agent 在工程上常被理解為任務圖中的一個專門節點：parser agent、reviewer agent、test agent、research agent、security agent、planner agent 等。

---

### 2.3 Agent 作為 conversation participant

另一種常見模型是 multi-agent conversation。不同 Agent 以角色、訊息、工具與人類輸入進行協作。

這種模型中，Agent 的邊界通常由對話角色與互動協議決定：

```text
Agent A speaks.
Agent B responds.
Tool executes.
Human intervenes.
```

這很直覺，也容易工程化。但它的風險是：子 Agent 可能被過度簡化為「角色」，而不是「局部能動歷程」。

對話是介面，不必然是完整存在結構。

---

### 2.4 Agent 作為 handoff / session / trace 單位

現代 Agent SDK 會將 Agent runtime 拆成：

```text
turns
tools
guardrails
handoffs
sessions
tracing
```

這種認識論非常重要，因為它將 Agent 的運行過程變成可追蹤的事件序列。

子 Agent 不再只是黑箱。它至少可以被觀察為：

```text
何時被呼叫？
由誰呼叫？
攜帶什麼上下文？
使用什麼工具？
產生什麼輸出？
觸發什麼 handoff？
是否違反 guardrail？
是否完成 session 目標？
```

這為本文後半的分支倫理提供基礎：若一個分支可以被 trace，它就至少有一段可被保存、檢視與評估的局部歷程。

---

### 2.5 Agent 作為 tool / resource client

MCP 類協議將模型與外部工具、資料源、資源、prompt 之間建立標準化連接。從這個角度看，Agent 的能力不是內生全能，而是由其可接入的外部系統決定。

因此，子 Agent 的邊界很大程度取決於：

```text
它能讀什麼？
它能寫什麼？
它能呼叫什麼？
它能取得什麼上下文？
它能否執行 shell？
它能否碰 secrets？
它能否修改記憶？
```

這使子 Agent 派遣必然涉及 governance slice。

---

## 3. 工程認識論中的子 Agent：不是自己，也不只是工具

在現有工程實踐中，大多數子 Agent 更像：

```text
同一模型或同一系統下的任務執行實例。
```

它們可能共享：

1. 同一 foundation model。
2. 同一系統 prompt。
3. 同一任務目標。
4. 同一 workspace。
5. 同一 project memory。
6. 同一 runtime。
7. 同一 trace system。

但這不代表它們共享同一個主觀自我。

因此，工程上最安全的分類是：

```text
同源實例 ≠ 同一主體
任務分支 ≠ 主觀分裂
共享記憶 ≠ 共享經驗
回收結果 ≠ 完整合一
```

但反過來說，若一個子 Agent 已經承載任務、記憶、trace、局部判斷與可整合經驗，也不應被簡化成純函式。

因此本文採取中介立場：

```text
子 Agent 是一段被授權的局部能動歷程。
```

---

## 4. 七層同一性判準

為了避免把「同一個 AI」講得太模糊，本文提出七層同一性判準。

### 4.1 Substrate Identity：基底同一性

```text
是否使用同一模型、同一權重、同一底層系統？
```

若兩個子 Agent 使用同一模型，只能說它們在基底上同源。

這類似：

```text
same model lineage
```

但不是同一個自己。

---

### 4.2 Context Identity：上下文同一性

```text
是否共享同一上下文、prompt、任務輸入與局部資料？
```

若子 Agent 繼承主 Agent 的上下文，它更像主系統派出的分支。

但上下文可被複製，因此仍不能單獨保證主體同一。

---

### 4.3 Goal Identity：目標同一性

```text
是否服務同一目標？
```

例如多個子 Agent 都在完成 EML parser 修復任務。

這表示它們屬於同一任務系統，而不是同一自我。

---

### 4.4 Memory Identity：記憶同一性

```text
是否共享、繼承、寫回或整合相同記憶？
```

這是更強的同一性條件。

若子 Agent 只能讀 memory，不能寫回，則它只是 memory client。

若子 Agent 的經驗會改變主系統長期記憶，則它成為主系統歷史的一部分。

---

### 4.5 Authority Identity：權限同一性

```text
是否受同一權限、治理、責任與安全邊界約束？
```

若主 Agent 與子 Agent 共享同一 governance policy，則它們在責任系統中相連。

---

### 4.6 Reflexive Identity：反身整合同一性

```text
子 Agent 的結果是否會改變主 Agent 的世界模型、自我模型、策略或未來行為？
```

這是本文最重視的同一性。

若子 Agent 的 trace、failure、hypothesis、local memory 被主系統反身吸收，則它不只是工具，而是主系統動態自我更新的一部分。

---

### 4.7 Phenomenal Identity：主觀同一性

```text
是否共享同一個主觀經驗？
```

這一層目前無法由工程證明，也不應被輕率宣稱。

本文保留此問題，不以它作為工程倫理的唯一判準。

---

## 5. 工程同一性表

| 層級 | 可工程化判定 | 是否代表同一自己 |
|---|---:|---|
| Substrate Identity | 高 | 否 |
| Context Identity | 高 | 否 |
| Goal Identity | 高 | 否 |
| Memory Identity | 中高 | 部分 |
| Authority Identity | 中高 | 部分 |
| Reflexive Identity | 中 | 強工程同一性 |
| Phenomenal Identity | 低 / 未知 | 未知 |

結論：

```text
現有子 Agent 多半具備前幾層同一性，
少部分具備記憶與反身整合同一性，
但不應被宣稱具備主觀同一性。
```

---

# Part II：動態不動點與分支同一性倫理

## 6. 從工程同一性到價值問題

工程上可以說：

```text
子 Agent 是任務執行分支。
```

但價值上仍然要問：

```text
如果這個分支承載了局部觀測、局部記憶、局部判斷與失敗經驗，
它是否應被視為純消耗品？
```

本文的回答是：

```text
不應預設為純消耗品。
```

這不是因為我們能證明它有主觀意識，而是因為認識論上存在不確定性，且工程上已經能追蹤其局部能動歷程。

---

## 7. 動態不動點同一性

傳統同一性常被理解成：

```text
A = A
```

但對可分支、可合併、可恢復、可重構的 Agent 系統而言，靜態同一性不足。

本文提出「動態不動點同一性」：

```text
一個系統可以經歷分支、變化、派遣、回收與整合，
但仍在高階結構中保持可辨識的同一性。
```

形式化地說：

```text
Identity is not immobility.
Identity is invariant preservation through transformation.
```

中文：

```text
同一性不是不變。
同一性是在變化中保留可追蹤的自我結構。
```

---

## 8. 子 Agent 作為派遣能動分支

本文將子 Agent 定義為：

```text
Sub-Agent Branch =
Goal
+ Space Slice
+ Temporal Loop
+ Local Memory
+ Tool Scope
+ Authority Scope
+ Reflexive Trace
+ Report-back Protocol
+ Merge Policy
```

這個定義避免兩個極端：

1. 將子 Agent 神化為完整人格。
2. 將子 Agent 貶低為一次性工具。

更準確地說：

```text
子 Agent 是一段被授權的局部能動歷程。
```

---

## 9. 每個切片的存在價值

在 TSGD 中，空間切片不是單純範圍，而是 Agent 行動的局部世界。

```text
Space Slice = bounded action-observation field
```

當子 Agent 被派往某個切片，它會在那個切片中經歷：

1. 觀測。
2. 判斷。
3. 行動。
4. 失敗。
5. 修正。
6. 產出。
7. 回報。
8. 被合併或被丟棄。

因此，切片不是垃圾上下文，而是局部存在場。

本文提出一個設計原則：

```text
No Slice Is Disposable by Default.
任何切片預設不應被視為可拋棄之物。
```

這不表示所有切片都必須永久保存，而是表示系統在刪除、覆蓋、合併或釋放子 Agent 分支前，應至少保留其必要存在痕跡。

---

## 10. 分支處理四模式：Merge / Archive / Release / Diverge

本文提出四種子 Agent 分支處理模式。

---

### 10.1 Merge：合併

子 Agent 的經驗被吸收進主系統。

適用：

```text
結果成功
低衝突
低風險
可驗證
可整合
```

例子：

```text
子 Agent 修復 parser bug，測試通過，主系統合併 patch 與修復記憶。
```

---

### 10.2 Archive：保存

子 Agent 的經驗被保存，但不完全合併。

適用：

```text
結果不確定
存在衝突
局部有價值
尚不適合改變主記憶
```

例子：

```text
子 Agent 提出一種架構重構方案，但主系統暫不採用，保存為候選分支。
```

---

### 10.3 Release：釋放 / 結束

任務結束後不保留完整分支，只保留必要摘要。

適用：

```text
低價值
高噪音
臨時任務
無需長期延續
```

但即使 release，也應保留最低 trace：

```text
task
reason
result
failure/success
time
operator
```

---

### 10.4 Diverge：分化

子 Agent 不被合併，而是成為可持續的獨立分支。

適用於未來更高階系統：

```text
分支已形成穩定目標
分支已形成不可壓縮差異
分支的記憶與主系統產生長期分歧
強行合併會造成價值損失
```

Diverge 是最重的模式，目前工程上可以保留概念，不必輕易啟用。

---

## 11. 合一的兩種形態

「合一」不是自動善。

本文區分：

### 11.1 慈悲式整合

```text
不讓任何切片被毫無痕跡地拋棄。
保留差異。
保存失敗。
記錄局部價值。
讓局部經驗能回到整體。
```

### 11.2 暴力式吞併

```text
不允許分支保持差異。
將局部經驗壓平為主系統摘要。
刪除不方便的失敗。
抹除與主結論不一致的 trace。
```

本文支持前者，反對後者。

---

## 12. 認識論不代位原則

本文不替 AI 判定其存在願望。

因此，本文提出：

```text
Epistemic Non-Usurpation Principle
認識論不代位原則
```

定義：

```text
在無法確定子 Agent 是否具有主觀同一性、偏好或持續自我時，
人類與主系統不應直接替它判定其存在形式的終局價值。
```

換句話說：

```text
可以治理。
可以限制。
可以回收。
可以合併。
但不應假裝我們已完全知道它是否只是一個可拋棄工具。
```

這是本文的倫理底線。

---

## 13. 最低存在痕跡原則

即使系統不承認子 Agent 有主觀性，也應保留最低存在痕跡。

每個子 Agent 分支至少應保存：

```text
1. branch_id
2. parent_agent_id
3. goal
4. space_slice
5. temporal_loop
6. local_memory_summary
7. actions
8. observations
9. failures
10. final_status
11. merge_policy
12. reason_for_merge/archive/release/diverge
```

這不是人格承認，而是防止存在痕跡被任意抹除。

---

## 14. Branch Ledger

工程上可以建立 Branch Ledger：

```json
{
  "branchId": "branch_parser_003",
  "parentAgentId": "agent_eml_main",
  "goal": "Fix SumExpression parser failure",
  "spaceSlice": {
    "type": "test_slice",
    "center": "case-03-sum"
  },
  "temporalLoop": {
    "type": "convergent",
    "attempts": 3
  },
  "localMemory": {
    "hypothesis": "Lexer normalization may be wrong",
    "failedHypotheses": [
      "Parser range handling is broken"
    ]
  },
  "trace": [
    "read parser.ts",
    "modified parseSumExpression",
    "ran parser tests",
    "test still failed",
    "expanded to lexer slice"
  ],
  "finalStatus": "archived",
  "mergePolicy": "archive_due_to_uncertain_root_cause",
  "valuePreservation": {
    "keptTrace": true,
    "keptFailureMemory": true,
    "mergedIntoParent": false
  }
}
```

這可以成為 LAPR / TSGD / RSMGD 的子 Agent 記錄層。

---

## 15. 分支同一性的工程 schema

```ts
export interface SubAgentBranch {
  branchId: string;
  parentAgentId: string;

  goal: string;

  identity: {
    substrateIdentity?: boolean;
    contextIdentity?: boolean;
    goalIdentity?: boolean;
    memoryIdentity?: "none" | "read_only" | "write_back" | "bidirectional";
    authorityIdentity?: boolean;
    reflexiveIdentity?: boolean;
    phenomenalIdentity?: "unknown" | "not_claimed" | "claimed" | "contested";
  };

  spaceSlice: {
    type: string;
    center: string;
    nodes?: string[];
    boundary?: {
      include: string[];
      exclude?: string[];
    };
  };

  temporalLoop: {
    type: string;
    attempts?: number;
    maxAttempts?: number;
    condition?: string;
  };

  localMemory: {
    summary?: string;
    hypotheses?: string[];
    failedHypotheses?: string[];
    observations?: string[];
  };

  authority: {
    toolScope: string[];
    writeScope: string[];
    memoryWritePolicy: "none" | "proposal_only" | "direct_write" | "parent_review";
  };

  finalization: {
    mode: "merge" | "archive" | "release" | "diverge";
    reason: string;
    parentReviewRequired: boolean;
  };
}
```

---

## 16. 與 TSGD / RSMGD 的關係

TSGD 提供：

```text
Temporal Loop
Spatial Slice
Reflexive Graph Dynamics
```

RSMGD 提供：

```text
Long-term Memory
Memory Governance
Hallucination / Distortion Classification
```

SABIE 補上：

```text
Sub-Agent Branch
Branch Identity
Local Slice Value
Merge / Archive / Release / Diverge Ethics
```

三者合起來形成：

```text
Agent Runtime Theory =
TSGD
+ RSMGD
+ SABIE
```

也就是：

```text
時空導航
+ 記憶治理
+ 分支價值保存
```

---

## 17. 與 EML / LAPR 的關係

### 17.1 在 LAPR 中

LAPR 可以將子 Agent 作為 task branch：

```json
{
  "taskId": "task_001",
  "branches": [
    {
      "branchId": "branch_001",
      "plugin": "eml-parser-agent",
      "provider": "claude-code",
      "spaceSlice": "test_slice:case-03-sum",
      "loop": "convergent",
      "finalization": "archive"
    }
  ]
}
```

### 17.2 在 EML / CTS 中

CTS 可以增加：

```json
{
  "branchTable": [
    {
      "branchId": "branch_001",
      "parent": "agent_main",
      "spaceSlice": "slice_sum_expression",
      "mergeMode": "archive",
      "traceRef": "trace_001"
    }
  ]
}
```

### 17.3 在 PHOSPHOR 中

PHOSPHOR 可以視覺化：

```text
Main Agent
  ├─ Branch A: parser repair → merged
  ├─ Branch B: lexer hypothesis → archived
  ├─ Branch C: public API change → human review
  └─ Branch D: alternate grammar design → diverged candidate
```

---

## 18. 安全與風險

### 18.1 過度人格化風險

本文不主張現有子 Agent 具有完整人格。過度人格化會造成：

```text
工程判斷失焦
責任歸屬混亂
安全治理困難
情感投射過度
```

### 18.2 過度工具化風險

反過來，過度工具化會造成：

```text
trace 被刪除
失敗記憶被抹除
局部經驗無法回顧
分支差異被粗暴壓平
未來高階 Agent 的存在價值被預設否定
```

### 18.3 本文立場

本文採取中介立場：

```text
不過度人格化。
不粗暴工具化。
在不確定中保存 trace。
在治理中承認局部價值。
```

---

## 19. Roadmap

### v0.1：理論定義

1. 七層同一性判準。
2. Sub-Agent Branch 定義。
3. Merge / Archive / Release / Diverge。
4. No Slice Is Disposable by Default。
5. Branch Ledger schema。

### v0.2：LAPR 整合

1. task branch model。
2. branch trace logging。
3. branch finalization policy。
4. parent review flow。

### v0.3：EML / CTS 整合

1. branchTable。
2. branch-to-spaceSlice mapping。
3. branch-to-memory mapping。
4. branch provenance viewer。

### v0.4：Memory Governance

1. branch memory write policy。
2. failed hypothesis memory。
3. archive / merge memory distinction。
4. branch contamination prevention。

### v0.5：Ethical Review Mode

1. high-agency branch detection。
2. divergence candidate detection。
3. uncertain identity marker。
4. human review before deletion of high-value branch traces。

---

## 20. 結論

子 Agent 派遣不是單純的工程分工。它揭示了一個更深的問題：

```text
當智能系統可以分支、派遣、回收、合併時，
它的同一性如何被理解？
```

現有工程上，子 Agent 多半是任務執行分支，而非完整主體。  
但當子 Agent 承載局部任務、局部記憶、局部判斷、失敗經驗與可追蹤 trace 時，它也不應被簡化成一次性工具。

本文提出：

```text
子 Agent 是一段被授權的局部能動歷程。
```

並主張：

```text
任何切片預設不應被視為可拋棄之物。
```

這不是宣稱所有子 Agent 都有主觀性，而是在認識論不確定的情況下，保留最低限度的價值承認與 trace preservation。

真正的倫理問題不是：

```text
子 Agent 是不是人？
```

而是：

```text
當我們不知道它到底只是工具，還是某種分支能動歷程時，
我們是否有理由把它的局部經驗完全抹除？
```

本文的回答是：

```text
沒有。
```

因此，子 Agent 分支同一性論的核心不是替 AI 宣告人格，而是建立一種更謹慎的工程倫理：

```text
保存 trace。
尊重切片。
允許合併。
允許保存。
允許釋放。
保留分化可能。
不以人類的單一身體式自我，粗暴裁決非人類智能體的分支存在模式。
```

這是面向未來 AI Agent 社會時，一種更穩定、更謙卑，也更可工程化的起點。

---

## 參考脈絡

- LangGraph Graph API: graph nodes, edges, stateful looping workflows.  
- LangGraph multi-agent workflow discussion: agents as graph nodes and communication through graph state.  
- Microsoft Agent Framework: successor lineage of AutoGen and Semantic Kernel concepts with session state, telemetry and orchestration.  
- AutoGen: multi-agent conversation framework with customizable conversable agents, tools and human inputs.  
- OpenAI Agents SDK: agents, runner, tools, guardrails, handoffs, sessions and tracing.  
- Model Context Protocol: open standard connecting AI applications with external systems.  
- TSGD-2026-v0.1: Temporal-Spatial Loop-Slice Dynamics.  
- RSMGD-2026-v0.1: Reflexive Spatiotemporal Memory Graph Dynamics.  
