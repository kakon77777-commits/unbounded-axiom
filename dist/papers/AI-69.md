# 語義偽圖譜：從思維導圖到 AI 可讀架構草案的意圖語言介面

**版本**：v0.1\
**作者**：Neo.K\
**形式**：Markdown 論文 / 技術白皮書草稿\
**定位**：語義偽代碼的圖譜化延伸、Vibe Coding 的架構草案介面、AI Agent 可讀的意圖組織格式

***

## 摘要

在 AI 協作開發、Vibe Coding、意圖語言與 AI Agent 工作流逐漸成熟的背景下，人類與機器之間的溝通形式正在從「編寫程式碼」轉向「描述意圖、組織概念、生成架構、再由 AI 協助實作」。前一階段的核心問題是：自然語言過於模糊，正式程式碼過於具體，因此需要一種介於兩者之間的語義偽代碼，用於描述意圖、輸入、輸出、流程、限制、失敗模式與轉譯目標。然而，單一語義偽代碼函數只能表示局部任務。當系統概念變得更大，當多個語義函數需要組合，當人類需要以更直覺的方式組織 AI 可讀架構時，單純的文本函數庫仍然不足。

本文提出「語義偽圖譜」（Semantic Pseudocode Graph, SPG）作為語義偽代碼的圖譜化延伸。語義偽圖譜是一種介於思維導圖、流程圖、系統架構圖、任務樹與語義函數庫之間的 AI 可讀架構草案格式。它不是正式流程圖，也不是可執行工作流，而是一種以節點與連線組織概念、任務、資料、限制、決策、失敗模式與轉譯目標的圖狀意圖結構。每個節點可以展開為一個語義偽代碼函數、語義模組或規格片段；整張圖則可以被 AI Agent 讀取、解析、重組，並進一步轉譯為產品規格、程式碼架構、Agent Workflow、RAG Pipeline、研究流程、UI 自動化策略或系統設計草案。

本文主張，未來的 AI 協作開發不只需要「語義函數」，也需要能組織語義函數的「語義圖譜」。人類在早期創意階段通常不會直接畫正式流程圖，因為流程圖暗示順序固定、狀態明確、邏輯已定；但人類也不應只停留在散亂自然語言筆記，因為這會讓 AI 過度補完、誤解結構、忽略限制。語義偽圖譜提供一種折衷：對人類而言，它像思維導圖一樣自由；對 AI 而言，它像架構圖一樣可解析；對 Agent 而言，它像任務圖一樣可重組；對工程實作而言，它像系統草案一樣可轉譯。

本文進一步提出語義偽圖譜的節點分類、邊類型、展開機制、Markdown 表示法、網站產品形態、AI 解析流程與安全邊界。本文的核心命題是：語義偽代碼是點，語義偽圖譜是面；語義函數是積木，語義圖譜是積木的組合草案；意圖語言是人類操作這些積木的方式，AI Agent 則是根據圖譜重組並實作的轉譯者。若語義偽代碼是 AI 時代的概念函數庫，那麼語義偽圖譜就是 AI 時代的概念架構圖。

***

## 1. 前言：從語義函數到語義圖譜

語義偽代碼解決的是單一任務的結構化問題。它讓使用者可以把一個概念、流程、功能或任務描述成 AI 可理解的語義函數。例如：

```md
FUNCTION:
  rank_candidate_documents

INTENT:
  根據使用者查詢，排序候選文件，優先返回語義相關、來源可信、時間適當的資料。

INPUT:
  query
  candidate_documents
  ranking_policy

OUTPUT:
  ranked_documents

CONSTRAINTS:
  - 不可只因為文件較新就提高排序。
  - 來源衝突時需標記。
  - 不可捏造 metadata。
```

這種格式能讓 AI 理解一個任務的意圖、輸入、輸出與限制。它不需要直接可執行，也不應該直接可執行。它的價值是作為「意圖到實作」之間的中介層。

然而，真實系統很少只由一個函數構成。無論是 AI 研究助理、Vibe Coding 工具、文件轉網站系統、RAG 搜尋引擎、產品 MVP 產生器，還是 UI 操作 Agent，都不是單一語義函數能完成的。它們需要多個模組共同作用：

```md
interpret_user_query
retrieve_candidate_sources
rank_candidate_documents
detect_source_conflicts
build_argument_structure
generate_answer_with_citations
mark_uncertainty
```

這時候，單一語義偽代碼函數庫仍然不夠。使用者需要知道這些函數如何關聯、如何組合、哪些是前置、哪些是後續、哪些是限制、哪些是決策、哪些是資料、哪些是風險。這就需要圖譜。

傳統上，人類可以使用流程圖、UML、系統架構圖、心智圖、任務樹或資料流圖來表達這些關係。但這些工具各有問題。

流程圖過於正式，容易暗示流程已經確定。\
UML 對非工程背景使用者太重。\
系統架構圖偏技術實作，不適合早期創意。\
普通思維導圖太鬆散，AI 不一定能穩定理解。\
任務樹偏層級，不容易表達多向關係。\
資料流圖偏資料，不一定能表達意圖與限制。

因此，需要一種新的中間形式：既保留思維導圖的自由性，又保留架構圖的可讀性；既不要求流程完全固定，又能讓 AI 辨識節點類型與組合關係。本文稱之為「語義偽圖譜」。

***

## 2. 定義：什麼是語義偽圖譜？

本文將語義偽圖譜定義如下：

> 語義偽圖譜是一種非可執行、參考性、需重新組合的 AI 可讀圖狀意圖結構，用於以節點與連線組織概念、任務、語義函數、資料、限制、決策、失敗模式與轉譯目標，並可作為 AI Agent 生成系統架構、工作流、程式碼或文件的草案基礎。

這個定義包含幾個關鍵部分。

### 2.1 非可執行

語義偽圖譜不是可執行流程圖。它不能被直接當成工作流引擎、狀態機或自動化腳本。即使它有節點與邊，也不代表每一條邊都是固定執行路徑。

它必須明確標記：

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
```

這些標籤的意義是：圖譜只是架構草案，不是程式，也不是正式工作流。AI 讀取它時，必須理解、重組、再實作。

### 2.2 圖狀意圖結構

語義偽圖譜不是普通思維導圖。它的節點不是單純文字，而是有語義類型的節點。例如：

```md
@goal_node
@function_node
@data_node
@constraint_node
@decision_node
@failure_node
@agent_action_node
@translation_node
```

每個節點類型都告訴 AI：這個節點在整體架構中扮演什麼角色。

### 2.3 可展開

語義偽圖譜的核心特徵是：節點可以展開。

圖上看到的可能只是：

```md
Rank Documents
```

但點開後，它對應的是完整語義偽代碼函數：

```md
FUNCTION:
  rank_candidate_documents

INTENT:
  根據查詢意圖排序候選文件。

INPUT:
  query
  candidate_documents
  ranking_policy

OUTPUT:
  ranked_documents

PROCESS:
  1. Interpret query intent.
  2. Evaluate semantic relevance.
  3. Evaluate freshness.
  4. Evaluate source trust.
  5. Return ranked list.

CONSTRAINTS:
  - Do not rank newer documents higher only because they are newer.
  - Mark uncertainty.
  - Preserve source conflict.
```

這使圖譜不只是視覺化，而是一種語義索引介面。

### 2.4 可重組

語義偽圖譜不要求固定順序。它提供的是一組概念關係與建議組合。AI Agent 應根據具體任務、使用者需求、技術環境、安全限制與上下文，重組圖譜並生成實際工作流。

### 2.5 可轉譯

語義偽圖譜可以被轉成不同形式：

```md
產品需求文件
系統架構草案
Agent Workflow
RAG Pipeline
API 設計
資料庫設計
程式碼模組分工
UI 操作策略
研究流程
知識圖譜
教學大綱
```

同一張語義偽圖譜，不一定只對應一種實作。

***

## 3. 為什麼不用正式流程圖？

語義偽圖譜最重要的設計背景之一，是有意避免過度流程圖化。

流程圖很有用，但它有一個隱含語義：流程圖通常表示事情已經被拆解為明確步驟，而且步驟之間具有相對穩定的執行順序。當流程圖出現開始、判斷、分支、結束等圖形時，人類與機器都容易把它理解成可操作流程。

然而，在 Vibe Coding 與意圖語言的早期階段，使用者往往還沒有完全確定流程。他可能只是知道：

```md
這個系統需要讀文件。
它可能要整理概念。
它要生成網站內容。
它應該保留原文結構。
它可能需要讓 AI 重寫。
它最後要輸出 Markdown 或頁面。
```

這時候若強行畫流程圖，就會過早固定順序：

```md
讀文件 → 抽取概念 → 重寫 → 生成頁面 → 發布
```

但真實情況可能是：

```md
有些文件需要先分類。
有些概念需要人工確認。
有些章節不能重寫。
有些輸出要保留原始語氣。
有些內容需要拆成多頁。
有些 metadata 需要另外生成。
有些模組可能重複使用。
```

流程圖在早期容易製造「假確定性」。

語義偽圖譜避免這個問題。它更像思維導圖，允許多個概念同時存在，允許節點彼此關聯，允許流程尚未固定，也允許 AI 後續依上下文重組。

因此，語義偽圖譜的基本態度是：

```md
不是：這就是固定流程。
而是：這是可供 AI 理解與重組的架構草案。
```

流程圖偏向：

```md
Step A -> Step B -> Step C
```

語義偽圖譜偏向：

```md
Goal
  connects_to Function A
  depends_on Data B
  constrained_by Constraint C
  may_trigger Decision D
  can_translate_to Implementation E
```

換句話說，流程圖回答「下一步是什麼」。\
語義偽圖譜回答「這些概念如何關聯」。

***

## 4. 為什麼需要思維導圖式介面？

思維導圖的價值在於，它符合人類早期思考的樣子。人在構思一個系統、一篇論文、一個產品、一套理論或一個工具時，通常不會一開始就線性思考。更常見的是：

```md
中心概念出現
周邊概念擴散
部分概念互相連接
某些概念變成子任務
某些限制突然浮現
某些分支暫時保留
某些節點之後再展開
```

這就是思維導圖擅長的領域。

但普通思維導圖對 AI 來說仍然太鬆散。它通常只包含文字節點，缺少明確類型。AI 可能知道節點內容，但不一定知道：

```md
這是目標？
這是功能？
這是資料？
這是限制？
這是錯誤？
這是使用者操作？
這是轉譯目標？
```

語義偽圖譜就是把普通思維導圖加上語義類型與可展開函數。

因此，它可以被描述為：

```md
Mind Map for Humans
Semantic Graph for AI
Function Library for Agents
Implementation Scaffold for Developers
```

中文可以寫成：

```md
給人類看，是思維導圖。
給 AI 看，是語義圖譜。
給 Agent 用，是函數庫。
給工程實作，是架構草案。
```

這是語義偽圖譜的核心定位。

它不是要取代流程圖，而是要補上流程圖之前的那一層。

***

## 5. 語義偽圖譜的三層結構

語義偽圖譜可以分為三層：

```md
第一層：圖譜層 Graph Layer
第二層：節點層 Node Layer
第三層：函數層 Function Layer
```

### 5.1 圖譜層：整體架構

圖譜層呈現整體關係。它回答：

```md
這個系統有哪些部分？
這些部分如何連接？
哪些是核心目標？
哪些是主要功能？
哪些是資料來源？
哪些是限制？
哪些是風險？
哪些可被轉譯成實作？
```

圖譜層像一張思維導圖，但每個節點都有語義類型。

### 5.2 節點層：語義角色

節點層描述每個節點在圖中的角色。例如：

```md
Goal Node:
  表示系統或任務的最終目的。

Function Node:
  表示一個可展開的語義偽代碼函數。

Data Node:
  表示輸入、輸出、資料來源或資料結構。

Constraint Node:
  表示限制、安全邊界、不可推測事項或規則。

Decision Node:
  表示需要判斷、分支或策略選擇的地方。

Failure Node:
  表示錯誤、例外、不確定性或回退條件。

Agent Action Node:
  表示 AI Agent 可執行或需準備執行的操作。

Translation Node:
  表示可轉譯成的具體實作形式。
```

### 5.3 函數層：節點展開內容

函數層是節點背後的完整語義偽代碼。例如圖上有一個 `Prepare UI Action` 節點，點開後可以看到完整函數：

```md
FUNCTION:
  prepare_ui_action

INTENT:
  在 AI Agent 操作 UI 前確認目標、狀態、風險、可逆性與回退方案。

INPUT:
  user_goal
  current_ui_state
  permissions

OUTPUT:
  action_plan
  risk_flags

CONSTRAINTS:
  - 不可在未授權情況下執行不可逆操作。
  - 不可在欄位不確定時提交表單。
  - UI 狀態與預期不符時停止。
```

這種設計讓圖譜與函數庫自然結合。

***

## 6. 節點類型系統

語義偽圖譜需要一套基本節點類型。節點類型的目的不是視覺裝飾，而是讓 AI 能理解每個節點的語義角色。

### 6.1 目標節點 Goal Node

目標節點表示整張圖譜的核心目的。

```md
@goal_node
```

例如：

```md
Answer Research Question
Build AI Document-to-Website Tool
Generate MVP from Product Concept
Automate Safe UI Action
Create Personal Knowledge Assistant
```

目標節點通常是圖譜中心。

### 6.2 函數節點 Function Node

函數節點表示可展開為語義偽代碼的任務模組。

```md
@function_node
```

例如：

```md
interpret_user_query
rank_candidate_documents
decompose_development_task
build_argument_structure
convert_concept_to_mvp
```

每個函數節點都應該有 `expands_to` 欄位，指向完整語義偽代碼函數。

### 6.3 資料節點 Data Node

資料節點表示系統處理的資料來源、輸入、輸出或中間資料。

```md
@data_node
```

例如：

```md
source_documents
user_query
candidate_sources
ranked_results
project_files
ui_state
metadata
```

資料節點可幫助 AI 理解資料流，但不必完全變成正式資料流圖。

### 6.4 限制節點 Constraint Node

限制節點表示規則、禁止事項、安全邊界、權限、法律、隱私或品質要求。

```md
@constraint_node
```

例如：

```md
Preserve uncertainty
Do not infer sensitive attributes
Do not overwrite files without inspection
Require human confirmation before irreversible action
Do not treat newer source as automatically better
```

限制節點是語義偽圖譜的重要特徵。普通思維導圖常常只寫功能，忽略限制；但 AI 協作中，限制往往比功能更重要。

### 6.5 決策節點 Decision Node

決策節點表示需要判斷或分支的地方。

```md
@decision_node
```

例如：

```md
Are sources conflicting?
Is user intent clear?
Is action reversible?
Is metadata sufficient?
Does the project context exist?
```

決策節點不等於正式流程圖分支。它只是告訴 AI：此處存在需要判斷的語義條件，實際實作時要根據上下文處理。

### 6.6 失敗節點 Failure Node

失敗節點表示可能出錯、不確定、缺資料或需要回退的情境。

```md
@failure_node
```

例如：

```md
insufficient_context
source_access_denied
ambiguous_button_label
conflicting_requirements
unsafe_change_detected
```

失敗節點讓 AI 在規劃時提前考慮錯誤，而不是等執行失敗才補救。

### 6.7 Agent 行動節點 Agent Action Node

Agent 行動節點表示 AI Agent 可能執行的操作，例如讀檔、寫檔、點擊、搜尋、產生程式、呼叫 API。

```md
@agent_action_node
```

例如：

```md
read_project_files
modify_code_file
submit_form
open_browser_page
run_test_suite
create_draft_document
```

這類節點應與權限、風險與確認機制連接。

### 6.8 轉譯節點 Translation Node

轉譯節點表示整張圖譜或某個節點可以被轉成什麼形式。

```md
@translation_node
```

例如：

```md
TypeScript backend service
Python script
RAG pipeline
Agent workflow
Markdown document
Database schema
Product requirement document
```

這能幫助 AI 理解圖譜的最終落地方向。

***

## 7. 邊類型：節點之間如何關聯

普通思維導圖的連線通常只是「相關」。語義偽圖譜需要更清楚的邊類型，讓 AI 理解節點間的關係。

### 7.1 connects\_to

表示一般關聯。

```md
A connects_to B
```

例如：

```md
Answer Research Question connects_to Build Argument Structure
```

### 7.2 depends\_on

表示依賴關係。

```md
A depends_on B
```

例如：

```md
Rank Candidate Documents depends_on Candidate Sources
```

### 7.3 constrained\_by

表示受某限制影響。

```md
A constrained_by C
```

例如：

```md
Generate Answer constrained_by Preserve Uncertainty
```

### 7.4 expands\_to

表示節點可展開為語義函數。

```md
Node expands_to semantic_function_name
```

例如：

```md
Rank Documents expands_to rank_candidate_documents
```

### 7.5 may\_trigger

表示可能觸發某決策或失敗模式。

```md
A may_trigger B
```

例如：

```md
Retrieve Sources may_trigger source_access_denied
```

### 7.6 translates\_to

表示可轉譯成某實作。

```md
Graph translates_to Target
```

例如：

```md
AI Research Assistant translates_to RAG Pipeline
```

### 7.7 requires\_confirmation\_for

表示某行動需確認。

```md
Action requires_confirmation_for Risk
```

例如：

```md
Submit Form requires_confirmation_for irreversible_action
```

邊類型不必一開始太多。v0.1 可以保留最小集合：

```md
connects_to
depends_on
constrained_by
expands_to
may_trigger
translates_to
```

這樣已經足夠表達大多數語義關係。

***

## 8. Markdown 表示法提案：SPG v0.1

語義偽圖譜應優先支援 Markdown，因為 Markdown 易讀、易寫、易存、易版本控制，也容易被 AI 讀取。

以下是一個最小格式：

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable

GRAPH:
  ai_research_assistant

INTENT:
  建立一個能回答研究型問題、檢索資料、排序來源、處理衝突並生成有引用回答的 AI 助理架構草案。

NODES:
  - id: answer_research_question
    type: goal_node
    label: Answer Research Question

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

  - id: source_conflict
    type: decision_node
    label: Are Sources Conflicting?
    expands_to: detect_source_conflicts

  - id: uncertainty
    type: constraint_node
    label: Preserve Uncertainty
    expands_to: mark_uncertainty

  - id: generate_answer
    type: function_node
    label: Generate Answer With Citations
    expands_to: generate_answer_with_citations

EDGES:
  - from: answer_research_question
    to: interpret_query
    relation: depends_on

  - from: interpret_query
    to: retrieve_sources
    relation: connects_to

  - from: retrieve_sources
    to: rank_documents
    relation: connects_to

  - from: rank_documents
    to: source_conflict
    relation: may_trigger

  - from: generate_answer
    to: uncertainty
    relation: constrained_by

TRANSLATION_TARGETS:
  - RAG pipeline
  - research assistant workflow
  - academic writing assistant
  - knowledge QA agent

USAGE_NOTE:
  This semantic graph is not an executable workflow. It is an AI-readable architecture draft. Actual implementation requires contextual recomposition.
```

這種格式有幾個好處。

第一，它可以直接被人閱讀。\
第二，它可以被靜態網站渲染。\
第三，它可以被 AI 解析。\
第四，它可以轉成 Mermaid、JSON、Graphviz、React Flow 或其他圖形介面。\
第五，它保留非執行定位。

若未來需要更機器可讀，也可以轉為 JSON 或 YAML。但 v0.1 保持 Markdown 優先比較符合創意先行的精神。

***

## 9. 圖形介面：像流程圖，但不是流程圖

語義偽圖譜的 UI 可以借用流程圖的圖標與節點形狀，但不應讓使用者誤以為它是正式流程圖。它可以有以下視覺分類：

```md
🎯 Goal Node
⚙️ Function Node
📦 Data Node
🧱 Constraint Node
🔀 Decision Node
⚠️ Failure Node
🤖 Agent Action Node
🧬 Translation Node
```

這些圖標讓使用者快速理解節點類型。

但產品文案要明確說明：

```md
這不是可執行流程圖。
這是 AI 可讀的語義架構草案。
```

使用者操作方式可以像思維導圖：

```md
建立中心目標
向外新增節點
選擇節點類型
連接相關節點
點開節點填寫語義偽代碼
讓 AI 補全缺失欄位
讓 AI 生成整體架構摘要
讓 AI 轉譯成實作草案
```

這種介面對非工程使用者更友善，因為他們不需要先理解 UML、資料流圖、狀態機或正式流程圖。

它對工程使用者也有價值，因為它可以在正式設計之前提供高層架構草案。

***

## 10. 範例一：AI 研究助理語義偽圖譜

以下是一張 AI 研究助理的語義偽圖譜草案：

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable

GRAPH:
  ai_research_assistant

INTENT:
  建立一個能理解使用者研究問題、搜尋資料、排序來源、檢測衝突、生成論證並標記不確定性的 AI 研究助理架構。

NODES:
  - id: goal_answer_research_question
    type: goal_node
    label: Answer Research Question

  - id: query
    type: data_node
    label: User Query

  - id: interpret_query
    type: function_node
    label: Interpret User Query
    expands_to: interpret_user_query

  - id: retrieve_sources
    type: function_node
    label: Retrieve Candidate Sources
    expands_to: retrieve_candidate_sources

  - id: candidate_sources
    type: data_node
    label: Candidate Sources

  - id: rank_documents
    type: function_node
    label: Rank Candidate Documents
    expands_to: rank_candidate_documents

  - id: detect_conflicts
    type: decision_node
    label: Detect Source Conflicts
    expands_to: detect_source_conflicts

  - id: preserve_uncertainty
    type: constraint_node
    label: Preserve Uncertainty
    expands_to: mark_uncertainty

  - id: build_argument
    type: function_node
    label: Build Argument Structure
    expands_to: build_argument_structure

  - id: generate_answer
    type: function_node
    label: Generate Answer With Citations
    expands_to: generate_answer_with_citations

  - id: no_relevant_sources
    type: failure_node
    label: No Relevant Sources

EDGES:
  - from: goal_answer_research_question
    to: query
    relation: depends_on

  - from: query
    to: interpret_query
    relation: connects_to

  - from: interpret_query
    to: retrieve_sources
    relation: connects_to

  - from: retrieve_sources
    to: candidate_sources
    relation: connects_to

  - from: candidate_sources
    to: rank_documents
    relation: connects_to

  - from: rank_documents
    to: detect_conflicts
    relation: may_trigger

  - from: detect_conflicts
    to: preserve_uncertainty
    relation: constrained_by

  - from: rank_documents
    to: build_argument
    relation: connects_to

  - from: build_argument
    to: generate_answer
    relation: connects_to

  - from: retrieve_sources
    to: no_relevant_sources
    relation: may_trigger

TRANSLATION_TARGETS:
  - RAG answer pipeline
  - research assistant agent
  - academic writing assistant
  - source citation workflow

USAGE_NOTE:
  This graph is an architecture draft. It is not a fixed executable pipeline. Actual retrieval, ranking, citation and uncertainty handling must be implemented according to the concrete system.
```

這張圖的功能不是告訴 AI 「照這個固定順序執行」，而是告訴 AI：這個研究助理系統有哪些語義部件、它們如何關聯、哪些地方需要注意不確定性、哪些地方可能失敗。

***

## 11. 範例二：Vibe Coding 專案生成圖譜

Vibe Coding 場景更適合語義偽圖譜，因為使用者通常先有概念，再慢慢生成程式。

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable

GRAPH:
  vibe_coding_project_builder

INTENT:
  將使用者的自然語言產品想法轉換為可逐步實作、可檢查、可測試的軟體專案草案。

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

  - id: project_context
    type: data_node
    label: Project Context

  - id: inspect_project
    type: function_node
    label: Inspect Project Structure
    expands_to: inspect_project_structure

  - id: propose_implementation
    type: function_node
    label: Propose Minimal Implementation
    expands_to: propose_minimal_implementation

  - id: avoid_overbuild
    type: constraint_node
    label: Avoid Overbuilding

  - id: generate_tests
    type: function_node
    label: Generate Test Plan
    expands_to: generate_test_plan

  - id: validate_output
    type: function_node
    label: Validate Output Against Constraints
    expands_to: validate_output_against_constraints

  - id: missing_context
    type: failure_node
    label: Missing Project Context

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
    to: project_context
    relation: depends_on

  - from: project_context
    to: inspect_project
    relation: connects_to

  - from: inspect_project
    to: propose_implementation
    relation: connects_to

  - from: propose_implementation
    to: avoid_overbuild
    relation: constrained_by

  - from: propose_implementation
    to: generate_tests
    relation: connects_to

  - from: generate_tests
    to: validate_output
    relation: connects_to

  - from: project_context
    to: missing_context
    relation: may_trigger

TRANSLATION_TARGETS:
  - product requirement document
  - coding agent plan
  - GitHub issue list
  - MVP implementation roadmap
  - Cursor / VS Code AI task plan

USAGE_NOTE:
  This graph helps convert vague product ideas into structured implementation planning. It must not be treated as a complete specification without project inspection and human review.
```

這種圖譜對 Vibe Coding 很有用，因為它讓使用者從「感覺」進入「結構」，但不會太早變成正式工程文件。

***

## 12. 範例三：文件轉網站系統圖譜

這個範例接近知識庫、論文網站、AI 可讀文庫與內容發布系統。

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable

GRAPH:
  document_to_website_pipeline

INTENT:
  將原始文件、論文或知識材料轉換為可發布、可搜尋、可被人類與 AI 閱讀的網站內容。

NODES:
  - id: source_document
    type: data_node
    label: Source Document

  - id: parse_structure
    type: function_node
    label: Parse Document Structure
    expands_to: parse_document_structure

  - id: extract_concepts
    type: function_node
    label: Extract Core Concepts
    expands_to: extract_core_concepts

  - id: preserve_author_intent
    type: constraint_node
    label: Preserve Author Intent

  - id: generate_web_sections
    type: function_node
    label: Generate Web Sections
    expands_to: generate_web_sections

  - id: create_metadata
    type: function_node
    label: Create Metadata
    expands_to: create_content_metadata

  - id: semantic_links
    type: function_node
    label: Build Semantic Links
    expands_to: build_semantic_links

  - id: publishable_markdown
    type: data_node
    label: Publishable Markdown

  - id: uncertain_interpretation
    type: failure_node
    label: Uncertain Interpretation

  - id: translation_targets
    type: translation_node
    label: Translation Targets

EDGES:
  - from: source_document
    to: parse_structure
    relation: connects_to

  - from: parse_structure
    to: extract_concepts
    relation: connects_to

  - from: extract_concepts
    to: preserve_author_intent
    relation: constrained_by

  - from: extract_concepts
    to: uncertain_interpretation
    relation: may_trigger

  - from: extract_concepts
    to: generate_web_sections
    relation: connects_to

  - from: generate_web_sections
    to: create_metadata
    relation: connects_to

  - from: create_metadata
    to: semantic_links
    relation: connects_to

  - from: semantic_links
    to: publishable_markdown
    relation: connects_to

  - from: publishable_markdown
    to: translation_targets
    relation: translates_to

TRANSLATION_TARGETS:
  - Markdown website
  - Next.js content system
  - Astro documentation site
  - AI-readable knowledge base
  - searchable theory archive

USAGE_NOTE:
  This graph does not define a fixed CMS implementation. It organizes the semantic transformation from document to web content and must be adapted to the actual publishing platform.
```

這張圖展示了語義偽圖譜如何處理知識發布。它不只關心「把文件轉成網頁」，也關心作者意圖、語義連結、不確定解釋與 metadata。

***

## 13. 語義偽圖譜如何被 AI 讀取？

語義偽圖譜的價值在於它可以被 AI 讀取並轉譯。AI 讀取圖譜時，不應把它當成固定腳本，而應經過以下步驟：

```md
1. 讀取整體 INTENT。
2. 辨識所有節點類型。
3. 辨識節點之間的關係。
4. 找出核心目標節點。
5. 找出必要資料節點。
6. 找出可展開的函數節點。
7. 找出限制與失敗模式。
8. 根據使用者需求與上下文重組執行順序。
9. 生成具體實作草案。
10. 標記仍需人類確認或補充的部分。
```

這可以寫成一個語義函數：

```md
@semantic_pseudocode
@non_executable
@reference_only
@recomposition_required

FUNCTION:
  interpret_semantic_graph

INTENT:
  讀取一張語義偽圖譜，理解其目標、節點、關係、限制與可轉譯方向，並生成適合當前上下文的架構摘要或實作計畫。

INPUT:
  semantic_graph
  user_goal
  implementation_context

OUTPUT:
  interpreted_architecture
  recomposition_plan
  missing_information

PROCESS:
  1. Parse graph-level intent.
  2. Identify all nodes by type.
  3. Identify edge relations.
  4. Locate goal nodes and primary function nodes.
  5. Expand function nodes if semantic pseudocode definitions are available.
  6. Preserve constraints and failure modes.
  7. Recompose graph into a context-specific plan.
  8. Mark missing information.
  9. Return interpreted_architecture and recomposition_plan.

CONSTRAINTS:
  - Do not treat the graph as executable workflow.
  - Do not ignore constraint nodes.
  - Do not assume missing function definitions.
  - Do not collapse failure modes into normal steps.
  - Preserve ambiguity when the graph is incomplete.

FAILURE_MODES:
  - missing_goal_node
  - undefined_function_node
  - conflicting_edges
  - insufficient_context
  - unsafe_translation_target

TRANSLATION_TARGETS:
  - architecture summary
  - implementation plan
  - agent workflow draft
  - product specification
  - code generation scaffold

USAGE_NOTE:
  This function interprets semantic graphs as architecture drafts, not as executable pipelines.
```

這表示語義偽圖譜可以反過來成為 AI Agent 的輸入協議。

***

## 14. 語義偽圖譜與 Agent OS

若未來存在一種 Agent OS，讓 AI 能管理文件、瀏覽器、程式碼、應用程式、工作流與使用者記憶，那麼 Agent 需要一種方式理解任務架構。語義偽圖譜可以成為 Agent OS 的高層任務表示法。

在 Agent OS 中，使用者可能輸入：

```md
我想做一個能讀取我的論文、整理理論節點、生成網站頁面，並且讓 AI 之後能讀懂的知識系統。
```

Agent 可以把它轉成圖譜：

```md
Goal:
  Build AI-readable theory website

Nodes:
  Source Documents
  Parse Structure
  Extract Theory Nodes
  Preserve Author Intent
  Generate Semantic Pages
  Build Cross Links
  Create Metadata
  Publish Website
  Enable AI Retrieval

Constraints:
  Do not distort theory
  Mark uncertain interpretation
  Preserve canonical terminology
  Keep human-editable Markdown

Translation Targets:
  Next.js site
  Markdown knowledge base
  RAG corpus
  semantic graph index
```

接著 Agent OS 可以根據圖譜規劃：

```md
需要哪些工具？
需要讀哪些檔案？
需要生成哪些資料結構？
哪些步驟要使用者確認？
哪些可自動執行？
哪些需要測試？
```

這比直接讓 Agent 根據一句自然語言開始行動更安全，也更穩定。

***

## 15. 語義偽圖譜與知識圖譜的差異

語義偽圖譜容易被誤解為知識圖譜。但兩者不同。

知識圖譜通常表示事實、概念、實體與關係。例如：

```md
Paris is_capital_of France
Newton discovered Gravity
Paper A cites Paper B
Concept X is_part_of Theory Y
```

語義偽圖譜則表示意圖、任務、函數與架構。例如：

```md
Rank Documents depends_on Candidate Sources
Generate Answer constrained_by Preserve Uncertainty
Prepare UI Action requires Human Confirmation
```

知識圖譜偏向「世界是什麼」。\
語義偽圖譜偏向「任務如何被理解與組織」。

知識圖譜服務於知識檢索與推理。\
語義偽圖譜服務於 AI 協作、任務重組與實作生成。

當然，兩者可以結合。語義偽圖譜可以引用知識圖譜作為資料來源；知識圖譜也可以被語義偽圖譜中的函數節點處理。

例如：

```md
extract_core_concepts
  depends_on
theory_knowledge_graph
```

但它們不是同一件事。

***

## 16. 語義偽圖譜與系統架構圖的差異

系統架構圖通常描述實際技術組件，例如：

```md
Frontend
Backend API
Database
Cache
Queue
Authentication Service
Storage
```

語義偽圖譜不一定描述技術組件，而是描述任務語義。它可以在技術架構之前存在。

例如同一個產品概念，語義偽圖譜可以先寫：

```md
User Intent
Document Parsing
Concept Extraction
Content Transformation
Metadata Generation
Publishing
AI Retrieval
```

之後才轉成技術架構：

```md
Next.js Frontend
FastAPI Backend
PostgreSQL
Vector Database
Object Storage
Markdown Parser
Embedding Service
```

因此，語義偽圖譜是「前架構」。它位於產品概念與技術架構之間。

可以表示為：

```md
Product Idea
  ↓
Semantic Pseudocode Graph
  ↓
System Architecture
  ↓
Implementation
```

這是語義偽圖譜的關鍵位置。

***

## 17. 語義偽圖譜與流程圖的差異

流程圖偏向程序。語義偽圖譜偏向關係。

流程圖問：

```md
第一步做什麼？
第二步做什麼？
條件成立走哪邊？
流程何時結束？
```

語義偽圖譜問：

```md
哪些概念存在？
哪些任務相關？
哪些資料被使用？
哪些限制必須保留？
哪些節點可以展開？
哪些地方可能失敗？
哪些實作可以生成？
```

流程圖適合流程已明確的任務。\
語義偽圖譜適合概念尚在形成、需要 AI 協助重組的任務。

這不是說語義偽圖譜不能轉成流程圖。相反，當概念成熟後，AI 可以根據語義偽圖譜生成流程圖。但在早期，不應強迫它成為流程圖。

***

## 18. 語義偽圖譜與思維導圖的差異

思維導圖偏向人類思考。語義偽圖譜則是 AI 可讀的思維導圖。

普通思維導圖：

```md
主題
  - 子題
  - 子題
  - 子題
```

語義偽圖譜：

```md
Goal Node
  connects_to Function Node
  depends_on Data Node
  constrained_by Constraint Node
  may_trigger Failure Node
  translates_to Implementation Target
```

思維導圖中的連線通常只是視覺關聯。語義偽圖譜中的連線有語義類型。

思維導圖中的節點通常只是文字。語義偽圖譜中的節點可以展開成語義偽代碼函數。

所以語義偽圖譜可以被視為：

```md
帶有函數展開能力與語義邊類型的 AI 可讀思維導圖。
```

***

## 19. 語義偽圖譜的網站產品形態

若要做成網站，可以採用以下產品邏輯：

### 19.1 首頁

首頁說明：

```md
本網站收錄的不是可執行流程圖，也不是正式程式碼。

本網站提供語義偽圖譜與語義偽代碼函數，用於幫助人類與 AI 共同組織創意、架構任務、理解限制、重組流程並生成實作草案。

圖譜僅供參考與理解，實際使用必須由 AI Agent 或開發者依具體情境重新組合。
```

### 19.2 圖譜庫

收錄各類語義偽圖譜：

```md
AI Research Assistant Graph
Vibe Coding Project Builder Graph
Document-to-Website Graph
Product MVP Graph
UI Automation Safety Graph
Personal Knowledge Base Graph
RAG Pipeline Graph
Writing Assistant Graph
Agent Task Execution Graph
```

### 19.3 函數庫

每個圖譜節點可連到語義偽代碼函數頁面。例如：

```md
rank_candidate_documents.md
clarify_user_intent.md
prepare_ui_action.md
convert_concept_to_mvp.md
build_argument_structure.md
```

### 19.4 圖形編輯器

使用者可以建立自己的語義偽圖譜：

```md
新增中心目標
新增節點
選擇節點類型
連接節點
點開節點填寫語義函數
AI 補全缺失欄位
匯出 Markdown
轉成架構草案
```

### 19.5 AI 重組器

使用者可以對 AI 說：

```md
根據這張語義偽圖譜，幫我生成一份 MVP 技術規格。
```

或：

```md
根據這張語義偽圖譜，幫我轉成 Next.js + PostgreSQL 的開發計畫。
```

或：

```md
根據這張語義偽圖譜，幫我生成 Agent Workflow。
```

這會讓網站不只是資料庫，而是意圖語言工具。

***

## 20. 安全與誤用控制

語義偽圖譜既然可能被 AI Agent 用於任務規劃，就必須防止誤用。

### 20.1 不可直接執行

每張圖譜都應標記：

```md
@non_executable
@reference_only
@recomposition_required
```

並在圖譜下方提示：

```md
This graph is not an executable workflow.
It is an AI-readable architecture draft.
Actual implementation requires contextual recomposition and human review where appropriate.
```

### 20.2 高風險節點標記

涉及以下操作的節點應標記高風險：

```md
資料刪除
檔案覆寫
付款
發送訊息
公開發布
帳號操作
醫療建議
法律建議
金融決策
資安測試
個資處理
```

使用標籤：

```md
@safety_sensitive
@human_review_required
@irreversible_action_possible
```

### 20.3 限制節點不可被忽略

AI 解析圖譜時，Constraint Node 必須被視為優先約束，而不是普通節點。

例如：

```md
Generate Answer constrained_by Preserve Uncertainty
```

這表示生成回答時必須保留不確定性，而不是可選建議。

### 20.4 失敗節點需要處理

Failure Node 不應被當成旁支。它代表實作計畫必須考慮的錯誤情境。

例如：

```md
source_access_denied
metadata_missing
ambiguous_user_goal
unsafe_action_detected
```

AI 生成實作草案時應為這些情境提供處理方式。

***

## 21. 語義偽圖譜的評估標準

語義偽圖譜品質可以從以下方向評估。

### 21.1 可理解性

人類能否快速看懂這張圖想做什麼？

```md
核心目標是否明確？
節點名稱是否清楚？
圖譜是否過度複雜？
```

### 21.2 AI 可解析性

AI 能否辨識節點類型、邊類型與展開函數？

```md
節點是否有 type？
邊是否有 relation？
函數節點是否有 expands_to？
限制與失敗是否清楚標記？
```

### 21.3 可重組性

圖譜是否允許根據不同情境生成不同實作？

```md
是否過早固定流程？
是否保留轉譯目標？
是否避免綁死技術棧？
```

### 21.4 邊界完整性

圖譜是否包含限制與失敗模式？

```md
是否只有功能節點？
是否缺少 Constraint Node？
是否缺少 Failure Node？
是否標記高風險操作？
```

### 21.5 可展開性

重要節點是否能展開為語義偽代碼函數？

```md
Function Node 是否有對應函數？
函數內容是否包含 INTENT、INPUT、OUTPUT、PROCESS、CONSTRAINTS？
```

### 21.6 可轉譯性

AI 能否根據圖譜生成不同形式的實作草案？

```md
產品規格
技術架構
程式碼模組
Agent workflow
RAG pipeline
文件大綱
```

***

## 22. 語義偽圖譜的最小可行產品

一個最小可行版本可以這樣做：

### 22.1 文件優先

先不做複雜編輯器，只用 Markdown 文件定義圖譜與函數。

```md
/graphs/ai-research-assistant.md
/graphs/vibe-coding-project-builder.md
/functions/rank-candidate-documents.md
/functions/clarify-user-intent.md
```

### 22.2 靜態網站

用靜態網站展示：

```md
圖譜頁
函數頁
分類頁
搜尋頁
使用說明
標籤索引
```

### 22.3 簡單圖形渲染

可以先用 Mermaid 或其他圖形工具將節點關係渲染出來，但保留原始 Markdown 作為主格式。

### 22.4 AI 輔助生成

讓使用者輸入概念後，AI 產生初版語義偽圖譜：

```md
輸入：我想做一個 AI 論文網站生成器。
輸出：一張 document_to_website_pipeline 語義偽圖譜。
```

### 22.5 匯出

支援匯出為：

```md
Markdown
JSON
Mermaid
Agent workflow draft
Product requirement document
```

這樣就能快速驗證使用價值。

***

## 23. 語義偽圖譜與未來意圖語言

意圖語言的核心問題是：人類如何用不等於程式碼的方式，穩定地表達自己想讓系統完成什麼。

語義偽代碼提供了單一意圖函數。\
語義偽圖譜提供了多個意圖函數的組織方式。

兩者合起來，可以形成意圖語言的基礎。

使用者不需要直接說：

```md
請幫我寫一個完整系統。
```

而可以逐步操作：

```md
建立 Goal Node
加入 Function Node
加入 Constraint Node
加入 Data Node
連接節點
展開函數
讓 AI 補全
讓 AI 轉譯
```

這是一種更穩定的人機協作方式。

意圖語言不是單純自然語言，也不是程式語言。它是一種介於兩者之間的操作層。

語義偽圖譜可以成為這個操作層的視覺介面。

***

## 24. 長期願景：從概念地圖到 AI 可執行前草案

語義偽圖譜的長期願景，不是讓人類畫更多圖，而是讓圖成為 AI 可理解的概念架構。

未來可能的流程是：

```md
人類提出概念
  ↓
AI 協助生成語義偽圖譜
  ↓
人類調整圖譜節點
  ↓
AI 展開節點為語義偽代碼函數
  ↓
AI 根據技術環境重組
  ↓
生成產品規格 / 架構圖 / 程式碼 / Agent workflow
  ↓
人類審查
  ↓
系統實作
```

這使得創意可以先圖譜化，再工程化。

在這個模型中：

```md
自然語言是原始概念。
語義偽圖譜是概念地圖。
語義偽代碼是節點內容。
AI Agent 是重組器。
程式碼是最終實作之一。
```

這就是從概念到實作的新路徑。

***

## 25. 風險與限制

語義偽圖譜也有自身限制。

### 25.1 圖譜過度膨脹

如果節點太多，圖會變得不可讀。\
解法是分層、分頁、模組化。

### 25.2 節點類型混亂

若使用者亂用節點類型，AI 解析會不穩。\
解法是提供模板與 AI 輔助分類。

### 25.3 過早架構化

太早圖譜化也可能限制創意。\
解法是允許草稿模式，不要求一開始完整。

### 25.4 AI 過度執行

AI 可能把圖譜當成工作流直接執行。\
解法是強制標記 `@non_executable` 與 `@recomposition_required`。

### 25.5 缺少上下文

圖譜本身不包含所有實作細節。\
解法是讓 AI 在轉譯前產生 missing\_information。

### 25.6 高風險自動化

若圖譜涉及 UI 操作、資料刪除或帳號行為，需要更嚴格的人類確認。

***

## 26. 結論

語義偽代碼解決了單一意圖函數的問題，而語義偽圖譜解決了多個意圖函數如何組織成架構草案的問題。

在 AI 協作開發時代，人類不一定要從正式程式碼開始，也不一定要一開始就畫嚴格流程圖。人類可以先用接近思維導圖的方式組織概念，再透過語義節點、語義邊、可展開函數與限制標記，讓 AI 理解整體架構。

語義偽圖譜的核心價值是：

```md
它給人類自由。
它給 AI 結構。
它給 Agent 任務邊界。
它給工程實作草案。
```

如果語義偽代碼是 AI 時代的概念函數庫，那麼語義偽圖譜就是 AI 時代的概念架構圖。它讓創意不必直接跳到程式碼，也不必停留在散亂自然語言，而是能先成為可被 AI 識別、展開、重組與轉譯的語義地圖。

最終，語義偽圖譜追求的不是把思維導圖變成流程圖，而是把思維導圖升級成 AI 可讀的架構草案。它不是正式執行圖，而是實作之前的意圖圖；不是流程的終點，而是創意到系統之間的橋樑。

***

## 附錄 A：SPG v0.1 最小模板

```md
@semantic_graph
@non_executable
@reference_only
@recomposition_required
@ai_readable

GRAPH:
  graph_name

INTENT:
  Describe the purpose of this semantic graph.

NODES:
  - id: node_id
    type: goal_node | function_node | data_node | constraint_node | decision_node | failure_node | agent_action_node | translation_node
    label: Human-readable node label
    expands_to: optional_semantic_function_name

EDGES:
  - from: source_node_id
    to: target_node_id
    relation: connects_to | depends_on | constrained_by | expands_to | may_trigger | translates_to

TRANSLATION_TARGETS:
  - target_one
  - target_two

USAGE_NOTE:
  This semantic graph is non-executable. It is provided for reference, understanding, and recomposition only.
```

***

## 附錄 B：節點類型速查

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

***

## 附錄 C：邊類型速查

```md
connects_to
一般關聯。

depends_on
依賴關係。

constrained_by
受某限制約束。

expands_to
可展開為某語義函數。

may_trigger
可能觸發某決策、錯誤或分支。

translates_to
可轉譯為某實作目標。

requires_confirmation_for
某行動需要人類確認。
```

***

## 附錄 D：語義偽圖譜首頁宣言

```md
Semantic Pseudocode Graph Archive 收錄的不是可執行流程圖，也不是正式程式碼。

它提供面向 AI 協作開發、Vibe Coding、意圖語言與 AI Agent 的語義圖譜範例。

每張圖譜都用節點與連線組織目標、任務、資料、限制、決策、失敗模式與轉譯方向；每個重要節點可以展開為語義偽代碼函數。

本站內容僅供理解、參考與重新組合。實際使用時，必須由人類、AI 或 Agent 根據具體需求、技術棧、系統環境與安全限制重新設計與實作。

本站的核心不是畫流程圖，而是建立 AI 可讀的意圖架構草案。
```

***

## 附錄 E：核心關係總結

```md
Semantic Function = 單一語義積木
Semantic Pseudocode = 積木的文字格式
Semantic Graph = 多個積木的架構圖
Intent Language = 人類操作積木與圖譜的語言
AI Agent = 依圖譜重組並實作的轉譯者
Implementation = 最終生成的程式碼、工作流、文件或系統
```

最簡模型：

```md
Human Concept
  ↓
Intent Mind Graph
  ↓
Semantic Pseudocode Functions
  ↓
AI Agent Recomposition
  ↓
Concrete Implementation
  ↓
Human Review / Testing / Deployment
```
