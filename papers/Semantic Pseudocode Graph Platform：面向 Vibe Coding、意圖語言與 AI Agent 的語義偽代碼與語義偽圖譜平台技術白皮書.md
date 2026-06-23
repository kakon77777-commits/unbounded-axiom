# Semantic Pseudocode Graph Platform：面向 Vibe Coding、意圖語言與 AI Agent 的語義偽代碼與語義偽圖譜平台技術白皮書

**版本**：v0.1\
**作者**：Neo.K\
**文件類型**：技術白皮書 / 產品架構草案 / MVP 開發規格\
**預定開工時間**：2026 年 7 月\
**核心定位**：語義偽代碼函數庫 + 語義偽圖譜 + AI Agent 重組介面\
**狀態聲明**：本文描述之語義偽代碼與語義偽圖譜皆為非可執行、僅供參考、需重新組合之 AI 可讀概念結構，不應被視為正式程式語言或可直接執行工作流。

***

## 0. 執行摘要

本白皮書提出一個面向 Vibe Coding、意圖語言與 AI Agent 協作開發的技術平台構想：**Semantic Pseudocode Graph Platform**。該平台的核心目標，是建立一套由語義偽代碼函數庫與語義偽圖譜組成的 AI 可讀意圖架構系統，使人類可以用較低門檻的方式組織創意、表達任務、建立概念架構，並由 AI Agent 根據具體使用者需求、專案環境、技術棧與安全限制，重新組合為可實作的程式碼、工作流、產品規格、研究流程或系統架構草案。

本平台不是傳統程式碼庫，不是 Prompt Library，也不是可直接執行的流程圖工具。它的核心不是讓使用者複製程式碼，而是讓使用者與 AI 共同建立一種「意圖到實作」之間的中介層。

平台由三個主要部分構成：

```md
1. Semantic Pseudocode Library
   語義偽代碼函數庫，收錄大量不可執行、僅供參考與重組的語義函數。

2. Semantic Pseudocode Graph
   語義偽圖譜，用類思維導圖 / 類流程圖的形式組織語義函數、資料、限制、決策與失敗模式。

3. Agent Recomposition Layer
   Agent 重組層，讓 AI 根據語義函數與圖譜，自動生成 MVP 規格、開發計畫、Agent Workflow、程式碼骨架或文件草案。
```

短期 MVP 可以先以靜態網站與 Markdown 文件庫實現。語義偽代碼函數可由 AI 批量生成後人工篩選，並以分類頁、標籤、搜尋與範例頁呈現。語義偽圖譜可以先用 Markdown / JSON / Mermaid / markmap 之類的方式渲染，後續再使用節點式 UI 框架開發真正可拖曳、可點開、可編輯、可展開為語義函數的互動式圖譜編輯器。

本白皮書主張：網站本身不是難點，圖形 UI 也不是真正核心；真正核心是資料格式、語義節點類型、AI 重組規則與安全邊界。若能先建立穩定的 `Function → Node → Edge → Graph → Agent Recomposition` 模型，該平台可以在短時間內完成可展示原型，並逐步擴展為 AI 時代的語義函數庫與意圖架構圖系統。

***

## 1. 背景：AI 協作開發進入意圖層

AI 協作開發正在改變軟體與知識系統的建立方式。過去，使用者若想建立網站、工具、資料處理流程或自動化系統，通常必須先理解程式語言、框架、資料庫、API、部署與測試流程。現在，使用者可以先用自然語言描述想法，再由 AI 生成程式碼、文件、資料結構或任務流程。

這種方式催生了 Vibe Coding 與意圖語言。使用者不一定從完整規格開始，而是從方向、感覺、功能輪廓、局部需求與逐步修正開始。AI 則負責根據對話內容生成初版實作，再由使用者回饋、修改、擴充。

然而，這種模式存在一個明顯問題：自然語言過於鬆散，正式程式碼又過於具體。自然語言容易導致 AI 過度猜測、誤解需求、忽略限制；程式碼則要求使用者過早進入工程實作細節。兩者之間缺少一個穩定中介層。

語義偽代碼與語義偽圖譜正是為此而設計。

語義偽代碼負責將單一任務封裝為 AI 可理解的語義函數。語義偽圖譜則負責將多個語義函數、資料節點、限制節點與決策節點組織為架構草案。

這使得人類可以先以較接近思維導圖的方式表達概念，再讓 AI 根據圖譜理解整體結構，最後轉譯為具體實作。

***

## 2. 平台核心命題

本平台的核心命題可以概括為：

```md
概念先行
語義成形
圖譜組織
Agent 重組
實作後置
```

也就是：

```md
Human Concept
  ↓
Semantic Pseudocode Function
  ↓
Semantic Pseudocode Graph
  ↓
AI Agent Recomposition
  ↓
Concrete Implementation
```

在這個模型中，語義偽代碼不是程式碼，而是意圖函數；語義偽圖譜不是流程圖，而是 AI 可讀架構草案；Agent 不是盲目執行者，而是根據語義結構重新組合並生成具體實作的轉譯者。

因此，平台的核心不是「讓偽代碼可以執行」，而是「讓偽代碼足夠清楚，使 AI 可以理解、重組、轉譯與實作」。

***

## 3. 平台定位

本平台可以被定義為：

> 一個面向 AI 協作開發、Vibe Coding 與意圖語言的語義函數與語義圖譜平台，用於收錄、組織、展示、生成與重組不可直接執行的語義偽代碼與 AI 可讀架構草案。

平台不是：

```md
不是程式語言
不是可執行工作流引擎
不是單純 Prompt Library
不是傳統流程圖工具
不是普通心智圖工具
不是只給工程師使用的 API 文件庫
```

平台是：

```md
語義偽代碼函數庫
意圖函數資料庫
AI 可讀思維圖譜
Vibe Coding 架構草案工具
Agent 重組前置層
概念到實作的中介系統
```

其核心使用者包括：

```md
1. Vibe Coding 使用者
   有產品概念，但不一定會完整寫程式。

2. AI 協作開發者
   需要將模糊需求轉成可實作架構。

3. Agent 工具設計者
   需要可讀、可組合、可審查的任務表示法。

4. 研究者與創作者
   需要把理論、文章、論證、知識結構轉成 AI 可讀節點。

5. 產品設計者
   需要將想法轉成 MVP、使用者流程與功能草案。

6. 工程師
   需要在正式實作前理解使用者意圖與系統邊界。
```

***

## 4. 系統總體架構

平台可分為七層：

```md
1. Content Layer
   語義偽代碼函數、語義圖譜、模板、分類、範例。

2. Schema Layer
   Function Schema、Node Schema、Edge Schema、Graph Schema。

3. Rendering Layer
   Markdown 頁面、心智圖、節點圖、分類頁、搜尋頁。

4. Graph Interaction Layer
   節點拖曳、連線、點開、編輯、展開、折疊。

5. Agent Generation Layer
   AI 生成語義函數、圖譜、分類、補全節點。

6. Agent Recomposition Layer
   AI 根據圖譜生成 PRD、程式碼骨架、工作流與實作計畫。

7. Safety & Governance Layer
   非執行標記、安全節點、人類確認、版本控制、審查規則。
```

其中 MVP 階段不需要全部完成。最小版本只需要：

```md
Content Layer
Schema Layer
Rendering Layer
基本 AI 生成輔助
```

真正互動式圖譜與 Agent 重組可以作為後續版本。

***

## 5. 核心資料模型

平台最小資料模型只需要三種核心實體：

```md
Function
Node
Edge
```

加上一個容器：

```md
Graph
```

### 5.1 Semantic Function

Semantic Function 是單一語義偽代碼函數。

```ts
type SemanticFunction = {
  id: string
  name: string
  category: string
  status: "reference_only"
  executable: false
  recompositionRequired: true

  intent: string
  whenToUse?: string[]
  whenNotToUse?: string[]

  inputs: SemanticInput[]
  outputs: SemanticOutput[]

  process: string[]
  constraints: string[]
  failureModes?: string[]
  composition?: string[]
  translationTargets?: string[]

  usageNote: string
  tags?: string[]
  version?: string
}
```

語義函數的關鍵不是 `process`，而是 `intent`、`constraints` 與 `translationTargets`。因為 AI 實際重組時，最容易出錯的不是不知道流程，而是不知道邊界與落地方向。

### 5.2 Semantic Node

Semantic Node 是圖譜上的節點。

```ts
type SemanticNode = {
  id: string
  type:
    | "goal_node"
    | "function_node"
    | "data_node"
    | "constraint_node"
    | "decision_node"
    | "failure_node"
    | "agent_action_node"
    | "translation_node"

  label: string
  summary?: string
  expandsTo?: string
  position?: {
    x: number
    y: number
  }
  tags?: string[]
  riskLevel?: "low" | "medium" | "high"
}
```

`expandsTo` 是關鍵欄位。它讓圖譜節點可以連到完整語義偽代碼函數。

例如：

```json
{
  "id": "rank_documents",
  "type": "function_node",
  "label": "Rank Candidate Documents",
  "expandsTo": "rank_candidate_documents"
}
```

### 5.3 Semantic Edge

Semantic Edge 表示節點關係。

```ts
type SemanticEdge = {
  id: string
  source: string
  target: string
  relation:
    | "connects_to"
    | "depends_on"
    | "constrained_by"
    | "may_trigger"
    | "translates_to"
    | "requires_confirmation_for"

  description?: string
}
```

邊不是單純線條，而是語義關係。AI 解析圖譜時，必須理解 `depends_on`、`constrained_by`、`may_trigger` 等關係的差異。

### 5.4 Semantic Graph

Semantic Graph 是節點與邊的集合。

```ts
type SemanticGraph = {
  id: string
  name: string
  status: "reference_only"
  executable: false
  recompositionRequired: true

  intent: string
  nodes: SemanticNode[]
  edges: SemanticEdge[]
  translationTargets?: string[]
  constraints?: string[]
  usageNote: string
  version?: string
}
```

這個資料模型足以支撐 MVP。

***

## 6. 語義偽代碼格式

每個語義偽代碼函數建議使用固定 Markdown 格式：

```md
@semantic_pseudocode
@non_executable
@reference_only
@recomposition_required
@ai_readable

FUNCTION:
  function_name

INTENT:
  此語義函數想完成的任務。

WHEN_TO_USE:
  - 適用場景一
  - 適用場景二

WHEN_NOT_TO_USE:
  - 不適用場景一
  - 不適用場景二

INPUT:
  input_name:
    description:
    type:

OUTPUT:
  output_name:
    description:
    type:

PROCESS:
  1. Step one.
  2. Step two.
  3. Step three.

CONSTRAINTS:
  - Constraint one.
  - Constraint two.

FAILURE_MODES:
  - failure_mode_one
  - failure_mode_two

COMPOSITION:
  Can be combined with:
    - another_semantic_function

TRANSLATION_TARGETS:
  - Python function
  - TypeScript service
  - Agent workflow
  - Markdown checklist
  - API specification

USAGE_NOTE:
  This semantic pseudocode is non-executable. It is provided for reference, understanding, and recomposition only.
```

這個格式可以先由 AI 批量生成，再人工審查。初期不需要追求完美形式化，而要追求一致性、可讀性與可重組性。

***

## 7. 語義偽圖譜格式

語義偽圖譜可以先用 Markdown + YAML-like 結構表示：

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable

GRAPH:
  ai_research_assistant

INTENT:
  建立一個能理解研究問題、檢索資料、排序來源、處理衝突並生成有引用回答的 AI 研究助理架構草案。

NODES:
  - id: interpret_query
    type: function_node
    label: Interpret User Query
    expands_to: interpret_user_query

  - id: retrieve_sources
    type: function_node
    label: Retrieve Candidate Sources
    expands_to: retrieve_candidate_sources

  - id: rank_documents
    type: function_node
    label: Rank Candidate Documents
    expands_to: rank_candidate_documents

  - id: preserve_uncertainty
    type: constraint_node
    label: Preserve Uncertainty
    expands_to: mark_uncertainty

EDGES:
  - from: interpret_query
    to: retrieve_sources
    relation: connects_to

  - from: retrieve_sources
    to: rank_documents
    relation: connects_to

  - from: rank_documents
    to: preserve_uncertainty
    relation: constrained_by

TRANSLATION_TARGETS:
  - RAG pipeline
  - research assistant workflow
  - academic writing assistant

USAGE_NOTE:
  This semantic graph is not an executable workflow. It is an AI-readable architecture draft. Actual implementation requires contextual recomposition.
```

這個格式有四個優點：

```md
1. 人類可讀
2. AI 可解析
3. 可被網站渲染
4. 可轉成 JSON 或圖形 UI
```

後續若要做互動式圖譜，可將此格式轉為 graph JSON。

***

## 8. 節點類型規格

平台應固定八種核心節點：

```md
@goal_node
目標節點：表示系統或任務最終想完成什麼。

@function_node
函數節點：可展開為語義偽代碼函數。

@data_node
資料節點：表示輸入、輸出、資料來源或中間資料。

@constraint_node
限制節點：表示安全、權限、法律、品質、語義或邏輯限制。

@decision_node
決策節點：表示需要判斷、分支或策略選擇的地方。

@failure_node
失敗節點：表示錯誤、例外、不確定性與回退條件。

@agent_action_node
Agent 行動節點：表示 AI Agent 可能執行的操作。

@translation_node
轉譯節點：表示可轉成哪些實作形式。
```

MVP 可以先支援：

```md
goal_node
function_node
data_node
constraint_node
failure_node
translation_node
```

等互動式圖譜成熟後，再加入更細節的 decision\_node 與 agent\_action\_node。

***

## 9. 邊類型規格

平台應固定基本邊類型：

```md
connects_to
一般關聯。

depends_on
依賴關係。

constrained_by
受某限制約束。

may_trigger
可能觸發某決策、錯誤或分支。

translates_to
可轉譯為某實作目標。

requires_confirmation_for
某行動需要人類確認。
```

MVP 可先支援：

```md
connects_to
depends_on
constrained_by
may_trigger
```

這已足以表達多數早期圖譜。

***

## 10. 技術選型建議

### 10.1 MVP 網站層

建議使用：

```md
Next.js 或 Astro
Markdown / MDX
Tailwind CSS
本地 JSON / YAML / Markdown content collection
全文搜尋
靜態部署
```

原因：

```md
1. 開發快速
2. 靜態內容容易管理
3. Markdown 適合語義偽代碼格式
4. 後續可接入 AI 生成與圖譜渲染
5. 適合快速展示概念
```

若以速度優先，Astro 或 Docusaurus 類型的文檔網站非常快。若預期後續要做互動式圖譜、登入、儲存、AI 生成、編輯器，Next.js 彈性較高。

### 10.2 語義偽圖譜渲染層

初期可以用三種方案：

```md
1. Mermaid
   適合文字轉圖、文件內嵌、快速展示。

2. markmap
   適合 Markdown 心智圖，符合「思維導圖」體感。

3. 簡單自製 graph renderer
   用 JSON nodes/edges 生成卡片式節點圖。
```

### 10.3 互動式節點編輯器

互動式版本建議使用：

```md
React Flow / xyflow
```

用途：

```md
節點拖曳
連線
自訂節點 UI
點擊節點打開詳情
節點類型樣式
邊類型樣式
儲存 graph JSON
```

每個節點可以是自訂 React component，例如：

```md
GoalNode
FunctionNode
DataNode
ConstraintNode
FailureNode
TranslationNode
```

FunctionNode 點開後顯示完整語義偽代碼函數。

### 10.4 大型圖譜與分析層

若未來需要更大的知識圖譜、關係分析與網路視覺化，可評估：

```md
Cytoscape.js
Sigma.js
Graphology
```

但 MVP 不需要一開始使用大型圖分析庫。除非圖譜節點數量很大，或需要做圖演算法、社群偵測、關聯探索，否則 React Flow 類型的 node editor 更適合產品原型。

***

## 11. MVP 開發路線

### Phase 0：內容與格式定義

目標：先把內容與格式定下來。

工作項目：

```md
1. 確定語義偽代碼模板
2. 確定語義偽圖譜模板
3. 確定節點類型
4. 確定邊類型
5. 確定分類系統
6. 生成第一批語義函數
7. 生成第一批圖譜範例
```

第一批分類建議：

```md
Vibe Coding
Agent Workflow
RAG / Search
Writing / Research
Product Design
UI Automation
AI Safety
Knowledge Management
Data Processing
Document Transformation
```

第一批函數數量：

```md
50 到 100 個
```

第一批圖譜數量：

```md
5 到 10 張
```

### Phase 1：靜態網站

目標：建立可瀏覽、可搜尋的網站。

功能：

```md
首頁
核心理念頁
語義偽代碼規格頁
語義偽圖譜規格頁
函數分類頁
函數詳情頁
圖譜分類頁
圖譜詳情頁
搜尋
標籤
警告聲明
```

此階段不需要登入，不需要資料庫，不需要互動編輯器。

### Phase 2：只讀圖譜渲染

目標：讓圖譜可以被視覺化。

功能：

```md
Markdown graph → 視覺圖
節點類型圖標
點擊 function_node → 對應函數頁
圖譜下方顯示原始 SPG Markdown
支援 Mermaid / markmap 或自製 renderer
```

這一版就能展示核心概念：

```md
圖上是語義節點
點開是語義偽代碼函數
整張圖是 AI 可讀架構草案
```

### Phase 3：AI 生成語義函數

目標：讓 AI 根據使用者概念生成語義偽代碼函數。

輸入：

```md
使用者描述一個功能、任務或概念
```

輸出：

```md
完整 semantic_pseudocode 模板
```

Agent 行為：

```md
1. 判斷分類
2. 生成 function name
3. 補全 intent
4. 補全 input/output
5. 補全 process
6. 補全 constraints
7. 補全 failure modes
8. 標記 translation targets
```

### Phase 4：AI 生成語義偽圖譜

目標：讓 AI 根據使用者概念生成一張 SPG。

輸入：

```md
我想做一個 AI 論文網站生成器
```

輸出：

```md
document_to_website_pipeline 語義偽圖譜
```

Agent 需要生成：

```md
Goal Node
Function Nodes
Data Nodes
Constraint Nodes
Failure Nodes
Translation Nodes
Edges
Usage Note
```

### Phase 5：互動式圖譜編輯器

目標：讓使用者可以拖曳、連接、編輯節點。

功能：

```md
新增節點
選擇節點類型
拖曳節點
連接節點
設定 edge relation
點開節點
編輯節點 summary
選擇 expands_to function
儲存 graph JSON
匯出 Markdown
```

### Phase 6：Agent 重組器

目標：讓 AI 根據圖譜生成實作草案。

輸出類型：

```md
PRD
技術架構
開發任務清單
Agent Workflow
RAG Pipeline
程式碼骨架
資料庫 schema 草案
Markdown 文件
測試計畫
```

這是平台真正進入生產力工具的階段。

***

## 12. Agent 工作流設計

平台中的 Agent 可分為五種：

### 12.1 Function Generator Agent

負責生成語義偽代碼函數。

```md
Input:
  使用者描述的任務或功能

Output:
  semantic_pseudocode function
```

### 12.2 Graph Generator Agent

負責生成語義偽圖譜。

```md
Input:
  使用者描述的系統、產品或流程

Output:
  semantic_graph
```

### 12.3 Graph Interpreter Agent

負責讀取語義偽圖譜並產生架構摘要。

```md
Input:
  semantic_graph

Output:
  architecture_summary
  node_explanation
  missing_information
```

### 12.4 Recomposition Agent

負責根據圖譜與上下文生成實作草案。

```md
Input:
  semantic_graph
  semantic_functions
  implementation_context

Output:
  PRD / workflow / code scaffold / technical plan
```

### 12.5 Safety Review Agent

負責檢查高風險節點與不應執行的操作。

```md
Input:
  graph
  generated_plan

Output:
  risk_flags
  required_confirmations
  blocked_actions
```

這五種 Agent 不一定要一開始全部實作。MVP 可以先由同一個 AI 對話流程模擬。

***

## 13. 內容生成策略

平台初期內容可以大量使用 AI 生成，但不能完全無審查發布。

建議流程：

```md
1. 人類定義分類
2. AI 生成每類 10 個語義函數
3. 人類篩選與修改
4. AI 生成對應圖譜
5. 人類檢查節點與邊是否合理
6. 發布為 reference only
```

第一批函數建議：

```md
clarify_user_intent
decompose_development_task
inspect_project_structure
propose_minimal_implementation
validate_output_against_constraints
generate_test_plan
rank_candidate_documents
retrieve_candidate_sources
detect_source_conflicts
generate_answer_with_citations
prepare_ui_action
classify_action_risk
request_human_confirmation
convert_concept_to_mvp
build_argument_structure
extract_core_concepts
transform_document_to_web_content
create_content_metadata
build_semantic_links
mark_uncertainty
```

第一批圖譜建議：

```md
AI Research Assistant Graph
Vibe Coding Project Builder Graph
Document-to-Website Pipeline Graph
Product MVP Generator Graph
Safe UI Agent Graph
Personal Knowledge Base Graph
RAG Answer Pipeline Graph
Writing Assistant Graph
```

***

## 14. 安全設計與誤用控制

平台必須明確防止一件事：

```md
AI 或使用者誤以為語義偽代碼與語義偽圖譜可以直接執行。
```

因此，所有函數與圖譜都應包含：

```md
@non_executable
@reference_only
@recomposition_required
```

每個頁面也應顯示聲明：

```md
本內容不是可執行程式碼，也不是正式工作流。
它僅供理解、參考與重新組合。
實際使用時，必須依照具體技術棧、使用者需求、系統限制與安全要求重新設計與實作。
```

高風險節點應標記：

```md
@safety_sensitive
@human_review_required
@irreversible_action_possible
```

高風險操作包括：

```md
刪除資料
覆寫檔案
付款
提交表單
發送訊息
公開發布
帳號操作
個資處理
醫療建議
法律建議
金融決策
資安測試
```

Agent 重組時必須遵守：

```md
1. 不得忽略 constraint_node
2. 不得把 failure_node 當作普通節點
3. 不得直接執行 agent_action_node
4. 不得將 graph 視為固定流程圖
5. 不得在缺少上下文時生成確定性實作
```

***

## 15. MVP 技術實作建議

### 15.1 專案結構

```md
/spg-platform
  /content
    /functions
      /vibe-coding
      /agent-workflow
      /rag-search
      /ui-automation
      /product-design
      /writing-research
    /graphs
      ai-research-assistant.md
      vibe-coding-project-builder.md
      document-to-website.md

  /src
    /components
      FunctionCard.tsx
      GraphCard.tsx
      NodeBadge.tsx
      SemanticGraphViewer.tsx
      FunctionDetail.tsx

    /lib
      parseSemanticFunction.ts
      parseSemanticGraph.ts
      graphToMermaid.ts
      graphToJson.ts

    /app
      /functions
      /graphs
      /docs
```

### 15.2 先做的功能

```md
1. 首頁
2. 函數列表
3. 函數詳情
4. 圖譜列表
5. 圖譜詳情
6. 基本搜尋
7. 標籤
8. 圖譜節點點擊跳轉函數頁
```

### 15.3 暫時不做的功能

```md
1. 登入系統
2. 雲端儲存
3. 多人協作
4. 複雜權限
5. 完整 graph editor
6. 自動執行 workflow
```

先避免工程過度膨脹。

***

## 16. 開發時間估算

若目標是 MVP 展示版，時間可以壓得很短。

### 16.1 一日原型

可以完成：

```md
網站殼
首頁
幾個分類頁
10 到 20 個語義函數頁
3 張圖譜頁
基本樣式
```

### 16.2 三日原型

可以完成：

```md
完整分類
50 個函數
5 張圖譜
圖譜轉 Mermaid / markmap
節點點擊跳轉
搜尋
基礎資料模型
```

### 16.3 一週 MVP

可以完成：

```md
100 個函數
10 張圖譜
較完整 UI
Graph JSON schema
AI 生成 prompt / workflow
函數與圖譜互相引用
初步匯出
```

### 16.4 兩到四週 Alpha

可以完成：

```md
互動式圖譜編輯器
節點拖曳與連線
AI 生成語義函數
AI 生成語義圖譜
AI 重組成 PRD / 技術規格
使用者可保存草稿
```

實際時間取決於是否要做帳號系統、雲端儲存、多人協作與正式部署。

***

## 17. 產品頁核心文案

首頁可以使用以下文案：

```md
Semantic Pseudocode Graph Platform 收錄的不是可執行程式碼，也不是固定流程圖。

它是一個面向 AI 協作開發、Vibe Coding 與意圖語言的語義函數與語義圖譜平台。

在這裡，每個語義偽代碼函數都是一塊可理解、可參考、可重組的概念積木；每張語義偽圖譜則將多個積木組織成 AI 可讀的架構草案。

使用者可以先用接近思維導圖的方式整理概念，再讓 AI Agent 根據具體需求、技術棧與安全限制，重新組合成產品規格、Agent Workflow、程式碼骨架或系統設計。

本站的核心不是複製程式碼，而是理解意圖、組織概念、生成實作。
```

***

## 18. 成功標準

MVP 成功不應以「功能多」衡量，而應以以下標準衡量：

```md
1. 使用者是否能看懂語義偽代碼不是程式碼？
2. 使用者是否能看懂節點點開後就是語義函數？
3. AI 是否能根據圖譜生成合理架構摘要？
4. AI 是否不會把圖譜誤當可執行流程？
5. constraint_node 是否能在重組時保留？
6. failure_node 是否能在重組時被處理？
7. 同一張圖譜是否能轉成不同輸出？
```

真正的驗證方式：

```md
輸入一個產品概念
  ↓
生成語義偽圖譜
  ↓
展開節點為語義偽代碼
  ↓
讓 AI 轉成 MVP 規格
  ↓
讓 AI 轉成技術開發計畫
  ↓
檢查結果是否保留原意與限制
```

若這條鏈跑得通，平台就成立。

***

## 19. 主要風險

### 19.1 內容品質不穩

AI 批量生成函數可能品質不一。

解法：

```md
模板固定
分類固定
人工審查
版本標記
高品質示範頁
```

### 19.2 圖譜變成普通心智圖

若節點沒有類型與 expands\_to，圖譜會退化成普通思維導圖。

解法：

```md
強制節點 type
function_node 必須支援 expands_to
edge 必須有 relation
```

### 19.3 AI 把圖譜當流程圖

AI 可能直接依節點順序執行。

解法：

```md
non_executable 標記
recomposition_required 標記
usage note
Agent 解析規則
```

### 19.4 使用者誤以為可直接使用

解法：

```md
每頁顯示 Reference Only
匯出時也加入警告
生成實作時要求 review
```

### 19.5 互動式圖譜過早開發

一開始投入太多在 UI editor，可能拖慢核心驗證。

解法：

```md
先做只讀圖譜
先驗證資料格式
再做互動編輯器
```

***

## 20. 長期願景

長期來看，本平台可以演化成：

```md
AI 時代的語義函數庫
AI 可讀心智圖譜平台
Vibe Coding 架構草案工具
Agent Workflow 前置設計器
概念到實作的中介層
AI 協作開發的語義 npm
```

傳統 npm / PyPI 收錄的是可執行程式包。\
本平台收錄的是不可直接執行、但可被 AI 理解與重組的語義包。

傳統開發者 import code。\
未來使用者可能 call intent。

例如：

```md
CALL clarify_user_intent
CALL decompose_development_task
CALL rank_candidate_documents
CALL prepare_ui_action
CALL convert_concept_to_mvp
```

AI Agent 看到這些語義函數後，不是直接執行，而是理解任務類型，再根據實際環境生成程式碼、文件、流程或操作計畫。

這就是本平台最終想建立的東西：

```md
不是程式碼庫
而是意圖函數庫

不是流程圖
而是語義架構圖

不是 Prompt Library
而是 AI 可讀的概念重組系統
```

***

## 21. 結論

Semantic Pseudocode Graph Platform 的核心價值在於，它將人類創意、語義偽代碼、圖譜組織與 AI Agent 重組能力連接起來，形成一條從概念到實作的新路徑。

網站本身可以快速完成，初期甚至只需要 Markdown、分類頁、搜尋與基本圖譜渲染。真正需要設計的是語義資料模型與 AI 重組規則。只要 `Function → Node → Edge → Graph → Recomposition` 這條鏈穩定，平台就能快速建立原型，並逐步擴展為真正的意圖語言工具。

本平台的最小可行策略是：

```md
先做網站殼
再做語義偽代碼函數庫
再做只讀語義偽圖譜
再做 AI 生成
最後做互動式圖譜編輯器與 Agent 重組器
```

這條路線能避免過度工程化，也能快速驗證核心概念。

最終，本平台不是為了讓偽代碼直接執行，而是為了讓 AI 更好地理解人類意圖；不是為了把思維導圖變成流程圖，而是為了把思維導圖升級成 AI 可讀架構草案；不是為了取代工程，而是為了讓工程在更穩定的語義基礎上開始。

其核心精神可以收束為一句話：

```md
讓人類用概念思考，讓 AI 用語義理解，讓 Agent 依圖譜重組，讓系統在最後成真。
```

***

## 附錄 A：MVP Todo List

```md
[ ] 確定產品名稱
[ ] 建立首頁文案
[ ] 建立語義偽代碼模板
[ ] 建立語義偽圖譜模板
[ ] 建立節點類型規格
[ ] 建立邊類型規格
[ ] 生成第一批 50 個 semantic functions
[ ] 生成第一批 5 張 semantic graphs
[ ] 建立 functions 分類頁
[ ] 建立 graphs 分類頁
[ ] 建立函數詳情頁
[ ] 建立圖譜詳情頁
[ ] 建立基本搜尋
[ ] 建立標籤系統
[ ] 建立 graph to Mermaid / markmap renderer
[ ] 建立 function_node 跳轉
[ ] 建立 AI generation prompt
[ ] 建立 AI recomposition prompt
[ ] 建立警告與使用聲明
[ ] 部署第一版
```

***

## 附錄 B：核心資料鏈

```md
Semantic Function
  ↓ expands_to
Semantic Node
  ↓ connects_to / depends_on / constrained_by
Semantic Edge
  ↓ composed_as
Semantic Graph
  ↓ interpreted_by
AI Agent
  ↓ recomposes_into
Implementation Draft
```

***

## 附錄 C：核心標籤

```md
@semantic_pseudocode
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable
@context_dependent
@safety_sensitive
@human_review_required
@irreversible_action_possible
```

***

## 附錄 D：最小語義函數範例

```md
@semantic_pseudocode
@non_executable
@reference_only
@recomposition_required
@ai_readable

FUNCTION:
  clarify_user_intent

INTENT:
  在使用者需求模糊時，將自然語言描述轉換為較清楚的任務目標、限制、輸入輸出與缺失資訊。

INPUT:
  user_request:
    description: 使用者原始需求
    type: natural_language_text

OUTPUT:
  clarified_intent:
    description: 澄清後的任務意圖
    type: structured_intent

  missing_information:
    description: 尚需補充的資訊
    type: question_list

PROCESS:
  1. Identify the user's primary goal.
  2. Extract implied constraints.
  3. Detect missing context.
  4. Separate confirmed intent from assumptions.
  5. Return clarified_intent and missing_information.

CONSTRAINTS:
  - Do not over-assume missing requirements.
  - Do not turn vague ideas into fixed specifications too early.
  - Preserve ambiguity when it is real.
  - Mark assumptions explicitly.

FAILURE_MODES:
  - user_goal_unclear
  - conflicting_requirements
  - insufficient_context

TRANSLATION_TARGETS:
  - Agent planning step
  - Product requirement clarification
  - Vibe Coding task setup
  - UX research prompt

USAGE_NOTE:
  This semantic pseudocode is non-executable. It is provided for reference, understanding, and recomposition only.
```

***

## 附錄 E：最小語義圖譜範例

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable

GRAPH:
  vibe_coding_starter_graph

INTENT:
  將使用者的初始產品想法轉換為可被 AI Agent 理解與重組的開發草案。

NODES:
  - id: product_idea
    type: data_node
    label: Product Idea

  - id: clarify_intent
    type: function_node
    label: Clarify User Intent
    expands_to: clarify_user_intent

  - id: define_mvp
    type: function_node
    label: Convert Concept to MVP
    expands_to: convert_concept_to_mvp

  - id: decompose_task
    type: function_node
    label: Decompose Development Task
    expands_to: decompose_development_task

  - id: avoid_overbuild
    type: constraint_node
    label: Avoid Overbuilding

EDGES:
  - from: product_idea
    to: clarify_intent
    relation: connects_to

  - from: clarify_intent
    to: define_mvp
    relation: connects_to

  - from: define_mvp
    to: decompose_task
    relation: connects_to

  - from: decompose_task
    to: avoid_overbuild
    relation: constrained_by

TRANSLATION_TARGETS:
  - MVP specification
  - Agent development plan
  - GitHub issue list
  - product roadmap draft

USAGE_NOTE:
  This semantic graph is not an executable workflow. It is an AI-readable architecture draft that requires contextual recomposition.
```
