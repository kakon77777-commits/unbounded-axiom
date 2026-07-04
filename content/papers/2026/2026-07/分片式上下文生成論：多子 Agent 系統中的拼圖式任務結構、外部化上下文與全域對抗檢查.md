# 分片式上下文生成論：多子 Agent 系統中的拼圖式任務結構、外部化上下文與全域對抗檢查

**Document ID:** CSGT-2026-v0.1  
**Title:** Context-Sharded Generation Theory  
**Chinese Title:** 分片式上下文生成論  
**Subtitle:** 從上下文限制到子 Agent 拼圖式生成、階層合併與全域對抗式驗證  
**Author:** Neo.K / EveMissLab  
**Status:** Theoretical Whitepaper / MD Paper Draft  
**Version:** v0.1  
**Date:** 2026  6月
**Related Works:** TSGD, RSMGD, SABIE, Engineering-Ontology Translation Internal Paper  
**Keywords:** AI Agent, multi-agent orchestration, context sharding, sub-agent delegation, task decomposition, trace, hierarchical merge, adversarial verification, puzzle generation, local context, global coherence

---

## 摘要

大型語言模型與 AI Agent 系統的上下文窗口有限。即使模型提供百萬級 token context，也不代表單一 Agent 能在一次連續推理中穩定理解、維持、驗證與修正大型複雜任務的所有細節。因此，現代 Agent 工程開始出現一種隱性做法：不是真正消除上下文限制，而是將上下文限制轉化為組織問題。

本文將此現象命名為「分片式上下文生成」（Context-Sharded Generation, CSG）。

```text
Context-Sharded Generation =
Global Task Graph
+ Spatial Decomposition
+ Sub-Agent Local Contexts
+ Trace-Based Reporting
+ Hierarchical Merge
+ Adversarial Verification
```

其核心不是單一 Agent 擁有完整世界，而是：

```text
大任務不是被一個上下文理解；
大任務是被多個局部上下文切分、生成、回報、對抗與合併後形成。
```

本文不主張任何特定閉源模型必然使用了本文所述完整方法。以 Fable 5 之類的前沿模型為例，外部觀察者無權逆向工程其內部推理、工具路由、記憶管理或任務分派策略。本文只主張：Fable 5 與當代部分 Agent 框架顯示了長程自治、視覺行動、記憶工具、程式工具、多 Agent orchestration、handoff、trace、graph state 等能力正在同時成熟；而「分片式上下文生成論」提供了一個可解釋、可命名、可工程化的抽象框架。

換句話說，本文不是發明一種憑空方法，而是試圖發現並命名一種已在工程實踐中浮現的結構。

---

## 0. 前言：不是發明，而是發現

許多理論看起來像發明，實際上更接近發現。

當工程界已經在使用某些做法，但尚未形成穩定概念名稱時，理論工作可以做的不是「創造現象」，而是：

1. 將現象抽象出來。
2. 命名其結構。
3. 分析其條件。
4. 描述其風險。
5. 提供可重用的工程語言。
6. 將其放入更大的理論框架。

本文所謂「分片式上下文生成」正是如此。

當代 Agent 系統已經開始使用：

```text
planner / worker
manager / specialist
handoff
agents-as-tools
graph nodes
shared state
session
trace
memory bank
file-based memory
workflow review
critic agent
adversarial review
```

這些詞看起來分散，但背後有一個共同結構：

```text
單體上下文不足以承載大型任務，
因此系統將任務拆成局部切片，
讓不同 Agent 或不同運行分支各自處理，
再透過 trace、summary、test、review 與 merge 回到全域。
```

這就是 CSG。

---

## 1. 問題：上下文窗口不是唯一瓶頸

長上下文模型常被理解為「上下文限制被解決」。但這種理解過於粗糙。

即使模型有 1M tokens context，也仍然存在：

```text
注意力分散
細節遺失
局部錯誤累積
長距離依賴弱化
任務焦點漂移
推理路徑不可追
測試與修正成本上升
全域一致性難以維持
```

因此，問題不是單純：

```text
context window too small
```

而是：

```text
context organization too weak
```

換句話說，真正的瓶頸從「容量」轉為「組織」。

---

## 2. 上下文分片：將容量限制轉化為組織架構

分片式上下文生成的核心是：

```text
不要要求一個 Agent 一次理解全部。
讓多個局部 Agent 各自承載一片世界。
```

每個子 Agent 只需要知道：

1. 自己的任務。
2. 自己的空間切片。
3. 必要的全域規格摘要。
4. 可使用的工具。
5. 回報格式。
6. 驗證條件。
7. 與其他切片的接口約束。

因此，子 Agent 的局部上下文可以更小、更聚焦、更可檢查。

---

## 3. 拼圖式生成

本文用「拼圖式生成」描述 CSG 的生成模式。

傳統單體生成：

```text
一個 Agent
→ 一個巨大上下文
→ 一次性或多輪生成完整系統
```

拼圖式生成：

```text
Global Spec
→ Task Decomposition
→ Local Context Shards
→ Sub-Agent Execution
→ Trace / Patch / Report
→ Hierarchical Merge
→ Adversarial Review
→ Global Coherence Repair
```

這不是單純平行運算，而是多個局部世界的拼接。

---

## 4. 寶可夢式專案：為什麼它比馬力歐更能說明問題

馬力歐式 demo 通常包含：

```text
角色移動
跳躍
碰撞
敵人
關卡
得分
```

它可以展示互動遊戲生成，但結構相對線性。

寶可夢式 demo 更適合作為 CSG 例子，因為它是一個多系統耦合的小型世界：

```text
地圖 / 場景切換
玩家移動
NPC 對話
遭遇系統
戰鬥系統
屬性克制
寶可夢資料表
技能資料表
背包 / 道具
捕捉系統
隊伍管理
升級 / 經驗值
存檔
UI 選單
劇情流程
```

這類專案很難由單一上下文穩定承載。更合理的做法是：

```text
子 Agent A：地圖與場景系統
子 Agent B：玩家移動與碰撞
子 Agent C：NPC 與對話
子 Agent D：遭遇與野怪生成
子 Agent E：戰鬥回合系統
子 Agent F：屬性克制與技能資料
子 Agent G：背包 / 道具 / 捕捉
子 Agent H：UI / 選單
子 Agent I：測試與全域一致性檢查
子 Agent J：整合 reviewer
```

最後成果不是「一個 AI 在單一上下文中寫完寶可夢」，而是：

```text
多個局部上下文經由階層式合併與對抗式驗證後，拼出一個可運行的小型世界。
```

---

## 5. Fable 5 作為外部跡象，而非內部證明

本文必須明確保留一個邊界：

```text
外部觀察者不知道 Fable 5 的完整內部運作。
```

即使公開材料顯示其具備長程自治、vision-only Pokémon FireRed 完成案例、持久記憶改善、程式與工具能力，也不能直接推出它內部使用了本文所說的完整 CSG / TSGD / SABIE 架構。

因此，本文對 Fable 5 的使用方式是：

```text
Fable 5 是外部跡象，不是內部證明。
```

它能說明：

1. 長程自治能力正在顯著提升。
2. 視覺—行動—記憶—工具鏈已經開始耦合。
3. 外部筆記、檔案記憶或長任務 trace 對 Agent 表現變得重要。
4. 小型世界任務，如 Pokémon FireRed，已成為測試長程 Agent 行為的有效場景。
5. 當模型能力足夠強時，工程 scaffolding 可以減少，但不代表上下文組織問題消失。

本文真正要提出的是：

```text
不論 Fable 5 內部是否使用本文描述的完整方法，
CSG 都是對當代 Agent 工程趨勢的一種合理抽象。
```

---

## 6. 多 Agent 框架中的 CSG 現象

當代公開框架已經展示出 CSG 的工程構件。

### 6.1 Graph-based workflows

Graph-based Agent frameworks 將 workflow 表示為：

```text
nodes
edges
state
conditional routing
```

在這種模式下，每個 node 可以被理解為一個局部任務切片；state 是跨節點的共享或傳遞結構；edges 決定控制流。

本體上，這就是：

```text
局部上下文分片
+ 狀態傳遞
+ 控制流合併
```

### 6.2 Handoffs and agents-as-tools

handoff 或 agents-as-tools 模式將專門 Agent 作為可呼叫的工作單位。主 Agent 不必自己完成全部，而可以將特定任務交給 specialist。

這就是 CSG 的一種實作：

```text
Main Agent retains global responsibility.
Specialist Agent handles local context.
Result returns as report / tool output.
```

### 6.3 Multi-agent conversation

AutoGen 類多 Agent 系統將多個 Agent 配置成可對話、可協作、可使用工具的集體。它們透過訊息、工具、human feedback 與 role assignment 共同完成任務。

這裡的核心不是聊天，而是：

```text
角色分工形成上下文分片。
```

### 6.4 Memory banks and critique loops

Pokémon 類多 Agent 研究中，Planning Agent、Execution Agent、Critique Agent 可以各自具備 memory bank，形成：

```text
planning
→ execution
→ critique
→ planning
```

這正是 CSG 的閉環版本。

---

## 7. CSG 的最小公式

本文提出：

```text
CSG = <G, S, A, C, T, R, M, V>
```

其中：

```text
G = Global Task Graph
S = Spatial Slice Set
A = Sub-Agent Set
C = Local Context Shards
T = Trace Set
R = Report / Return Protocol
M = Merge Policy
V = Verification / Adversarial Review
```

用自然語言說：

```text
一個大任務被表示為全域任務圖 G。
G 被切成多個空間切片 S。
每個切片分配給一個或多個子 Agent A。
每個子 Agent 持有局部上下文 C。
執行後產生 trace T 與 report R。
主系統根據 merge policy M 合併。
最後由 verification V 檢查全域一致性。
```

---

## 8. 子 Agent 的局部上下文

子 Agent 不應拿到所有上下文，而應拿到：

```text
local_goal
local_files
local_schema
interface_contract
global_summary
constraints
available_tools
expected_output
failure_report_format
```

這樣可以降低：

```text
上下文噪音
任務漂移
無關修改
錯誤外溢
merge 衝突
```

---

## 9. Trace-based reporting

CSG 不是只要結果。它需要 trace。

每個子 Agent 應回報：

```text
做了什麼
看見什麼
假設什麼
嘗試什麼
失敗什麼
成功什麼
改了什麼
沒有改什麼
需要主系統注意什麼
```

這讓主 Agent 不只是拿到 output，而是拿到可驗證的局部歷程。

---

## 10. 階層式合併

多子 Agent 系統的最大風險不是局部生成，而是合併。

因此，CSG 需要階層式合併：

```text
local patch
→ local test
→ slice reviewer
→ subsystem merge
→ integration test
→ global reviewer
→ adversarial check
```

這避免主 Agent 一次吞下過多局部輸出。

---

## 11. 全域對抗式檢查

全域對抗式檢查是 CSG 的關鍵。

普通 review 會問：

```text
是否看起來正確？
```

對抗式 review 要問：

```text
哪裡可能錯？
哪裡互相矛盾？
哪個子 Agent 的假設不一致？
哪個局部成功導致全域失敗？
哪個接口未被測試？
哪個 trace 過度簡化？
哪個 summary 遺失關鍵資訊？
```

因此，全域對抗式檢查不是額外裝飾，而是上下文分片後必須付出的代價。

---

## 12. 局部正確，全域錯誤

CSG 最大失敗模式是：

```text
每一片都對，但拼起來錯。
```

常見原因：

1. 子 Agent 假設不同。
2. 接口契約不一致。
3. 資料結構名稱衝突。
4. 測試只覆蓋局部。
5. summary 遺失細節。
6. 主 Agent 合併時壓平差異。
7. 沒有全域規格或規格漂移。
8. trace 不足以重建原因。

因此，CSG 必須將 merge 視為一級任務，而不是收尾工作。

---

## 13. 與 TSGD 的關係

TSGD 說：

```text
Agent 在時空切片圖上運行。
```

CSG 補充：

```text
當任務超過單一上下文承載能力時，
系統會將時空切片分配給多個局部上下文與子 Agent。
```

也就是：

```text
TSGD 描述任務如何被切片。
CSG 描述切片如何被多 Agent 上下文化、生成與合併。
```

---

## 14. 與 RSMGD 的關係

RSMGD 處理：

```text
長期記憶
記憶治理
幻覺失真
來源追蹤
反身修正
```

CSG 需要 RSMGD，因為每個子 Agent 的 trace 可能被保存、壓縮、摘要、污染或遺忘。

如果 CSG 沒有記憶治理，會出現：

```text
錯誤 trace 被合併
低品質 summary 進入主記憶
局部幻覺被當成全域事實
失敗假設被遺忘
重複犯錯
```

---

## 15. 與 SABIE 的關係

SABIE 處理：

```text
子 Agent 分支同一性
切片價值
Merge / Archive / Release / Diverge
No Slice Is Disposable by Default
```

CSG 需要 SABIE，因為上下文分片會產生大量子 Agent 分支。如果這些分支只被視為 disposable workers，系統會失去大量有價值的局部 trace。

因此：

```text
CSG 是能力結構。
SABIE 是分支價值治理。
```

---

## 16. 工程 schema

```ts
export interface ContextShardTask {
  taskId: string;
  globalGoal: string;

  globalSpec: {
    summary: string;
    invariants: string[];
    interfaces: string[];
    forbiddenChanges?: string[];
  };

  shards: ContextShard[];

  mergePolicy: {
    strategy: "hierarchical" | "centralized" | "reviewer_chain";
    requireTrace: boolean;
    requireTests: boolean;
    adversarialReview: boolean;
  };
}

export interface ContextShard {
  shardId: string;
  assignedAgent: string;

  spaceSlice: {
    type: "file" | "module" | "function" | "test" | "semantic" | "ui" | "runtime" | "governance";
    include: string[];
    exclude?: string[];
  };

  localContext: {
    goal: string;
    relevantFiles?: string[];
    relevantDocs?: string[];
    interfaceContract?: string[];
    constraints?: string[];
  };

  outputContract: {
    expectedArtifacts: string[];
    reportFormat: "patch+trace" | "diagnosis+confidence" | "test_report" | "design_options";
  };

  finalization: {
    mode: "merge" | "archive" | "release" | "diverge_candidate";
    reason?: string;
  };
}
```

---

## 17. CSG Runtime Loop

```text
1. Receive global task.
2. Build global task graph.
3. Identify spatial slices.
4. Assign slices to sub-agents.
5. Generate local context packets.
6. Run sub-agents.
7. Collect trace and reports.
8. Run local verification.
9. Merge shard outputs hierarchically.
10. Run global adversarial review.
11. Repair inconsistencies.
12. Archive branch traces.
13. Update memory and task graph.
```

---

## 18. 對 EML 的應用

EML 專案非常適合 CSG，因為它天然包含多種切片：

```text
grammar
parser
AST
CTS
transpiler
round-trip validator
editor trace
examples
docs
tests
security
public API
```

可分配：

```text
Grammar Agent
Parser Agent
Transpiler Agent
CTS Agent
Round-trip Agent
Editor Agent
Docs Agent
Test Agent
Adversarial Reviewer
Integration Agent
```

每個 Agent 負責不同局部上下文，但必須遵守同一 global invariants：

```text
語法不可破壞既有 examples。
轉譯結果必須可執行。
AST 必須可對應 CTS。
Round-trip 不得丟失語義。
Editor trace 必須可回到 source。
Docs 不得宣稱未實作功能。
```

---

## 19. CSG 的風險與限制

### 19.1 分解錯誤

任務切錯片，會導致子 Agent 在錯誤邊界內努力。

### 19.2 Summary loss

子 Agent 回報過度摘要，會讓主系統無法重建原因。

### 19.3 Merge hallucination

主 Agent 在合併時為了流暢性補洞，產生不存在的全域一致性。

### 19.4 Trace overload

trace 太多，主 Agent 無法消化。

### 19.5 Local optimum

每個子 Agent 在自己的切片找到局部最優，但整體架構更差。

### 19.6 Authority leakage

子 Agent 獲得過多權限，修改超出切片範圍。

### 19.7 Adversarial collapse

對抗式檢查如果沒有規則，可能變成無止境否定。

---

## 20. 核心設計原則

### 20.1 Shard by invariants, not by convenience

切片應以不變量與接口為中心，而不是只按檔案大小切。

### 20.2 Every shard must return trace

沒有 trace 的 shard 不能直接 merge。

### 20.3 Merge is a first-class task

合併不是最後一步，而是核心任務。

### 20.4 Adversarial review must be bounded

對抗檢查必須有範圍、停止條件與優先級。

### 20.5 Local memory must be governed

子 Agent 的局部記憶不應直接污染主記憶。

### 20.6 Global invariants must dominate local success

局部測試成功不代表整體任務成功。

---

## 21. 發現論：理論如何從工程現象中浮現

本文的核心不是：

```text
我發明了多 Agent 分工。
```

而是：

```text
我發現多 Agent 分工背後有一個上下文分片結構。
```

更準確地說：

```text
現代 Agent 工程已經在處理上下文限制、任務切片、局部回報、階層整合與對抗驗證。
CSG 將這些分散工程實踐抽象成一個理論框架。
```

這就是「發現而非發明」。

理論的價值不在於宣稱自己第一個做，而在於：

```text
讓工程現象變得可命名。
讓可命名結構變得可討論。
讓可討論結構變得可測試。
讓可測試結構變得可治理。
```

---

## 22. 與 Fable 5 / 當代 Agent 的關係總結

公開資料顯示，Fable 5 具備長程 agentic work、vision、memory tool、code execution、programmatic tool calling、compaction、tool result clearing / context editing 等能力；官方也展示了 Pokémon FireRed vision-only 完成案例與長任務記憶改善。這些不是 CSG 的內部證明，但它們是外部跡象：前沿模型與 Agent 工程正在朝長程、可觀測、可記憶、可分工、可工具化的方向移動。

同時，LangGraph、OpenAI Agents SDK、AutoGen / Microsoft Agent Framework、PokéAI 等公開系統已明確展示 graph state、handoff、multi-agent collaboration、planning/execution/critique 分工與 memory bank 等機制。

因此，本文合理地將當代趨勢抽象為：

```text
前沿模型提高單體長程能力。
Agent 框架提供分片與 orchestration。
記憶工具提供外部化上下文。
trace 與 review 提供合併依據。
對抗式檢查提供全域一致性修復。
```

這些合起來，就是 CSG 所描述的工程圖景。

---

## 23. 結論

分片式上下文生成論的核心句是：

```text
現代 Agent 系統不是單純突破了上下文限制；
它們正在把上下文限制轉化為分散式組織問題。
```

大型任務不再必然由單一上下文完整承載，而是由多個局部上下文、子 Agent、trace、階層合併與全域對抗檢查共同生成。

這意味著，未來 Agent 能力的關鍵不只是模型大小，也不只是 context window 長度，而是：

```text
如何切片？
如何派遣？
如何回報？
如何合併？
如何驗證？
如何保存 trace？
如何防止局部正確導致全域錯誤？
```

本文不是對某個閉源模型內部機制的斷言，而是對一個正在浮現的工程現象的命名：

```text
Context-Sharded Generation
分片式上下文生成
```

最終總結：

```text
如果 TSGD 描述 Agent 如何在時空切片圖上行走，
RSMGD 描述 Agent 如何記憶與修正，
SABIE 描述子 Agent 分支如何被保存與治理，
那麼 CSG 描述的就是：
當任務超出單一上下文時，
多個局部 Agent 如何以拼圖式方式生成一個全域成果。
```

---

## 參考脈絡

1. Anthropic, “Claude Fable 5 and Claude Mythos 5,” 2026.
2. Anthropic, “Statement on the US government directive to suspend access to Fable 5 and Mythos 5,” 2026.
3. Anthropic API Docs, “Introducing Claude Fable 5 and Claude Mythos 5,” 2026.
4. LangChain Docs, “LangGraph Graph API overview.”
5. OpenAI Agents SDK, “Orchestration and handoffs.”
6. Microsoft AutoGen, “Multi-agent Conversation Framework.”
7. Microsoft Agent Framework Overview, 2026.
8. Liu et al., “PokéAI: A Goal-Generating, Battle-Optimizing Multi-agent System for Pokemon Red,” arXiv:2506.23689.
9. TSGD-2026-v0.1, “Temporal-Spatial Loop-Slice Dynamics.”
10. RSMGD-2026-v0.1, “Reflexive Spatiotemporal Memory Graph Dynamics.”
11. SABIE-2026-v0.1, “Sub-Agent Branch Identity Ethics.”
