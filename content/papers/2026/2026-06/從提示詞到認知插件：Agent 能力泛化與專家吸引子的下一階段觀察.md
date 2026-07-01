# 從提示詞到認知插件：Agent 能力泛化與專家吸引子的下一階段觀察

**副標題：為什麼未來的 Agent 不是只需要 Skill，而是需要可載入的專家認知結構**

**作者：Neo.K**
**版本：v0.1 / 觀察論文草稿**
**日期：2026 年 6 月**
**類型：AI Agent 生態觀察、認知架構白皮書、技術哲學備忘錄**
**狀態：非定論；保存趨勢；供未來回溯研究**

## 摘要

近期香港、台灣、美國與全球開源社群中的 AI Agent 生態正在快速轉向一個新階段。早期的 AI 使用方式主要依賴提示詞工程，後來進入 Skill、Tool、MCP、Memory、Workflow、Coding Agent 與 Agent Orchestration 的工程化階段。然而，本文觀察到下一個更值得注意的方向：如何讓 Agent 不只是「會用工具」，而是更接近某種高階專家的判斷能力、審美能力、批判能力與工作風格。

本文將這種方向稱為「認知插件」（Cognitive Plugin）或「專家吸引子模組」（Expert Attractor Module）。它不是傳統 prompt，也不是單純 Skill。傳統 prompt 多為一次性語言指令；Skill 多為可重複任務流程；Tool 是外部操作能力；Memory 是歷史與偏好保存；而認知插件則是把某種專家能力拆解成可載入、可執行、可審核、可組合的認知結構。

以「讓 Agent 更接近頂級設計師」為例，真正有效的方式不是寫一句「你是一位世界級設計師」，而是建立一套包含審美先驗、風格語法、案例記憶、反平庸檢測、設計批判迴路、品牌一致性檢查、微文案規則、版面節奏判斷與最後審核協議的專家模組。這種模組會將 Agent 的生成路徑拉入某種專家能力盆地，使其不只是模仿語氣，而是更接近專家的判斷流程。

本文提出一個演化鏈：

Prompt → Skill → Tool → Workflow → Memory → Cognitive Plugin → Expert Attractor → Agent Operating Layer

本文認為，未來真正有價值的開源方向，可能不只是更多 Agent 框架，而是高品質的專家認知插件庫。模型本身會越來越強，工具也會越來越標準化；真正的差異將逐漸轉向：誰能提供更好的專家先驗、更好的批判迴路、更好的記憶結構、更好的工作場域，以及更可靠的專家吸引子。

## 關鍵詞

AI Agent、認知插件、專家吸引子、Skill、Prompt Engineering、Agent OS、設計智能、記憶框架、MCP、長程任務閉環、專家系統、工作流智能

## 0\. 作者聲明：本文不是工具推薦，而是趨勢觀察

本文不是在推薦某個具體框架，也不是在比較哪個 GitHub 專案最好。本文記錄的是一個更底層的趨勢：AI Agent 生態正在從「讓模型能執行工具」轉向「讓模型能接近專家工作方式」。

這個轉向很重要。

因為當模型能力不足時，大家關注的是如何讓它回答得更好。
當模型能回答後，大家關注的是如何讓它調用工具。
當工具調用成熟後，大家關注的是如何讓它記住狀態。
當記憶與工具都逐步補齊後，真正的問題會變成：

如何讓 Agent 具備某種專業判斷結構？

頂級設計師、產品策略師、系統架構師、資安審計員、研究員、法律審查員、品牌總監、投資分析師、編輯、導演、工程主管，這些角色的價值並不只是知識，而是判斷。

而判斷不可能只靠一句 prompt 完成。
判斷需要先驗、案例、偏好、反例、標準、檢查流程、風險意識、失敗檢測與迭代能力。

本文即是為此提出「認知插件」概念。

## 1\. 背景：Agent 生態正在補齊外部認知器官

目前開源社群大量出現幾類專案：

1.  Agent framework。
2.  MCP server。
3.  Tool connector。
4.  Memory layer。
5.  Coding agent。
6.  Workflow engine。
7.  Browser agent。
8.  Terminal agent。
9.  Agent sandbox。
10.  Agent permission system。
11.  Multi-agent orchestration。
12.  Agent evaluation framework。

這些方向本質上都在做同一件事：

替 AI 補上外部認知器官。

模型是大腦。
Tool 是手腳。
Browser 是眼睛。
Memory 是海馬迴。
MCP 是神經接口。
Sandbox 是免疫系統。
Permission 是行為邊界。
Workflow 是程序記憶。
Evaluation 是痛覺與考試。
Observability 是內省儀表板。
Human review 是社會制動器。

這些都是必要的。但它們還不是終點。

當 Agent 已經能接工具、讀文件、寫程式、操作 terminal、管理 repo、調用 API，下一個問題就會浮現：

它到底用什麼標準判斷好壞？

這是所有高階工作的核心。

能生成設計，不代表有設計判斷。
能寫程式，不代表懂架構取捨。
能寫文章，不代表懂編輯節奏。
能整理資料，不代表懂研究問題。
能產生策略，不代表懂風險與權力結構。

所以 Agent 的下一階段，不只是工具化，而是判斷結構化。

## 2\. Prompt 的極限

Prompt engineering 是 AI 使用史上的第一個重要階段。它讓使用者發現，模型不是只能被動回答，而可以透過角色設定、指令格式、示例、約束與輸出模板，引導出更穩定的結果。

但 prompt 有幾個先天限制。

### 2.1 Prompt 通常太短

真正的專家能力無法壓縮在幾句話裡。
「你是一位頂級設計師」不能讓模型真的擁有頂級設計師的審美結構。
「請用 Apple 風格」也不能讓模型理解 Apple 設計背後的材料感、留白、比例、層級、文字節奏、產品敘事與商業目標。

### 2.2 Prompt 容易變成語氣模仿

模型很容易學會「像專家那樣說話」，但不一定能「像專家那樣判斷」。這是 persona prompt 的常見陷阱。

例如：

「作為世界級設計師，我認為這個版面需要更多留白。」

這句話聽起來像設計評論，但它可能沒有真正判斷：留白是否服務於資訊層級？是否破壞轉換率？是否符合品牌？是否適合行動端？是否讓 CTA 太弱？

語氣不是能力。

### 2.3 Prompt 缺乏持久性

一次 prompt 可以讓模型暫時進入某種狀態，但長程任務中容易漂移。真正的專家工作需要多輪維持、持續批判、反覆修正與版本記憶。

### 2.4 Prompt 缺乏可審核性

好的專家判斷應該可以被拆開看：它用了什麼標準？參考了什麼案例？排除了什麼方案？風險在哪裡？為什麼這樣改？

Prompt 通常只給結果，較難提供可追蹤的判斷結構。

因此，prompt 是入口，不是終點。

## 3\. Skill 的進步與邊界

Skill 是比 prompt 更進一步的結構。它通常包含一組任務流程、工具使用方式、輸出格式與操作規則。例如：

-   生成 PDF。
-   處理 spreadsheet。
-   製作 slide。
-   搜尋文件。
-   跑測試。
-   發送 email。
-   產生 README。
-   轉換格式。
-   分析 log。
-   修改程式。

Skill 的價值是把可重複任務封裝起來，讓 Agent 不必每次重新理解流程。

但 Skill 仍有邊界。

Skill 通常回答的是：

怎麼做這件事？

而專家認知插件要回答的是：

怎麼判斷這件事做得好不好？
怎麼知道哪個方向更高級？
怎麼知道哪個方案只是看似合理？
怎麼避免平庸、錯配、過度設計或概念漂移？

Skill 偏向流程。
認知插件偏向判準。

Skill 讓 Agent 更會做事。
認知插件讓 Agent 更會判斷。

## 4\. 認知插件的定義

本文定義：

認知插件是可被 Agent 載入、調用、組合與審核的一組專家判斷結構，用以引導模型在特定領域中形成更接近專家工作方式的生成、評估、修正與交付迴路。

認知插件不是單一 prompt。它至少包含以下元素：

1.  領域先驗。
2.  判斷標準。
3.  案例記憶。
4.  反例記憶。
5.  工作流程。
6.  批判迴路。
7.  失敗檢測器。
8.  風格壓縮器。
9.  輸出格式。
10.  最終審核協議。
11.  版本化規則。
12.  與工具、記憶、上下文的連接方式。

簡單說，認知插件是：

將專家能力從「人設」轉成「可運行認知結構」。

## 5\. 專家吸引子：比 Persona 更深的概念

Persona 是讓模型扮演某個角色。
Expert Attractor 是讓模型的思考路徑被拉入某種專家能力盆地。

兩者差異很大。

Persona 主要改變語氣：

像設計師說話。
像教授說話。
像律師說話。
像產品經理說話。

Expert Attractor 改變判斷流程：

像設計師那樣看比例、節奏、留白、材質、品牌與使用場景。
像教授那樣檢查概念定義、文獻脈絡、論證缺口與可證偽性。
像律師那樣檢查責任、風險、條款衝突、可執行性與管轄問題。
像產品經理那樣檢查使用者痛點、商業價值、開發成本、優先級與指標。

因此，本文提出：

未來高品質 Agent 的差異，不在於它能不能扮演專家，而在於它能不能被穩定拉入某種專家吸引子。

專家吸引子是一種認知地形。
好的插件會改變模型在這個地形中的落點。

## 6\. 案例：頂級設計師插件不是一句「高級感」

以設計為例。大量使用者會對模型說：

幫我做得高級一點。
做成 Apple 風格。
做得像 Linear。
給我一個頂級設計師版本。
更有質感。
更 premium。

這些指令常常失敗，原因是「高級感」不是單一風格，而是一組結構。

真正的頂級設計師插件至少需要以下模組。

### 6.1 審美先驗

Agent 需要知道：

-   什麼是廉價感。
-   什麼是模板感。
-   什麼是過度設計。
-   什麼是視覺噪音。
-   什麼是節奏失衡。
-   什麼是比例錯誤。
-   什麼是品牌不一致。
-   什麼是太像 AI 生成。
-   什麼是未經選擇的裝飾。
-   什麼是有意識的克制。

### 6.2 設計語法

Agent 需要理解：

-   字體層級。
-   網格系統。
-   留白策略。
-   色彩飽和度。
-   對比關係。
-   動效節奏。
-   icon 一致性。
-   microcopy 語氣。
-   材質與陰影。
-   視覺焦點。
-   CTA 權重。
-   資訊架構。

### 6.3 商業約束

頂級設計不是純藝術。它必須服務於：

-   轉換率。
-   使用者理解。
-   品牌定位。
-   技術成本。
-   行動端適配。
-   無障礙。
-   開發交付。
-   維護成本。
-   市場差異化。
-   使用場景。

如果 Agent 只追求好看，可能會做出無法落地的設計。

### 6.4 案例記憶

設計插件需要案例庫，但不是用來抄襲，而是用來抽象語法。例如：

-   Apple：材質、留白、硬體感、產品神聖化。
-   Linear：低噪音、深色層級、精準 SaaS 介面。
-   Stripe：工程可信感、漸層、開發者友好。
-   Vercel：極簡、黑白、部署效率感。
-   Notion：低壓、文檔感、積木式工作流。
-   Teenage Engineering：玩具感、工業設計、反主流高級感。
-   MUJI：去符號化、日常性、材料誠實。
-   A24：文化感、邊緣美學、策展式品牌敘事。

真正的插件不應說「複製 Apple」，而應說：

此任務需要 Apple 式的產品聚焦，但不能使用 Apple 式過度留白，因為轉換目標需要更高資訊密度。

這才是判斷。

### 6.5 反平庸檢測器

頂級設計插件最重要的不是生成，而是檢測平庸。

它應該自動問：

-   這像模板嗎？
-   這像廉價 SaaS 嗎？
-   這是不是只是在堆 gradient？
-   這個 hero section 是否沒有觀點？
-   這個排版是不是誰都能做？
-   這個文案是否太空泛？
-   這個視覺中心是否不清楚？
-   這個品牌是否有記憶點？
-   這是否只是「看起來現代」，但沒有靈魂？
-   這是否過度依賴流行風格？

這就是設計判斷的核心。

### 6.6 批判迴路

設計插件應該強制 Agent 進行多輪自我批判：

1.  先生成初稿。
2.  判斷是否過度模板化。
3.  檢查資訊層級。
4.  檢查品牌一致性。
5.  檢查使用者行動路徑。
6.  檢查視覺噪音。
7.  壓縮元素。
8.  強化焦點。
9.  重新生成。
10.  最終審核。

這比「請再高級一點」有效得多。

## 7\. 認知插件的基本文件結構

一個高品質認知插件可以用資料夾形式保存：

/designer-attractor/
README.md
domain-priors.md
taste-rubric.md
anti-cheapness-checklist.md
reference-grammar.md
failure-patterns.md
critique-loop.md
workflow.md
output-templates.md
review-protocol.md
memory-schema.md
tool-bindings.md
eval-cases.md

每個文件都有不同功能。

### 7.1 domain-priors.md

保存該領域的基本先驗，例如：

-   好設計通常是選擇，不是堆疊。
-   版面節奏比單點美感更重要。
-   品牌記憶點比短期炫技更重要。
-   不同產品階段需要不同設計密度。
-   使用者理解成本是設計的一部分。

### 7.2 taste-rubric.md

保存審美評分標準，例如：

-   比例。
-   留白。
-   層級。
-   一致性。
-   記憶點。
-   商業適配。
-   技術可落地性。
-   品牌準確度。
-   情緒溫度。
-   反模板程度。

### 7.3 anti-cheapness-checklist.md

保存廉價感檢查：

-   過度漸層。
-   過多陰影。
-   無意義 icon。
-   假高級文案。
-   模板化 hero。
-   無節奏卡片。
-   亂用 glassmorphism。
-   過度圓角。
-   無品牌差異。
-   過度使用 buzzwords。

### 7.4 reference-grammar.md

不是保存案例圖片，而是保存設計語法：

-   某品牌如何使用留白。
-   某產品如何建立可信感。
-   某網站如何引導視線。
-   某介面如何降低認知負擔。
-   某設計如何用少量元素形成記憶點。

### 7.5 critique-loop.md

定義自我批判流程：

Generate → Diagnose → Remove → Refine → Compare → Stress-test → Finalize

### 7.6 memory-schema.md

定義插件應保存什麼記憶：

-   使用者審美偏好。
-   品牌長期語氣。
-   過去接受過的版本。
-   過去被拒絕的方向。
-   常見錯誤。
-   專案約束。
-   目標受眾。
-   競品風格。
-   設計禁忌。

### 7.7 eval-cases.md

定義測試案例，檢查插件是否真的有效：

-   低成本 SaaS landing page 重構。
-   AI 生成感設計去除。
-   過度花俏版面收斂。
-   高級但不可用設計修正。
-   品牌不一致設計診斷。
-   手機端資訊層級修復。

## 8\. 認知插件與 Agent OS 的關係

認知插件本身還不是完整系統。它需要 Agent OS 調度。

Agent OS 應負責：

1.  載入不同認知插件。
2.  根據任務選擇插件。
3.  管理插件版本。
4.  管理插件記憶。
5.  管理工具權限。
6.  管理輸出審核。
7.  管理插件衝突。
8.  管理多插件協作。
9.  記錄任務軌跡。
10.  讓人類可回溯決策。

例如，一個產品 landing page 任務可能同時需要：

-   Designer Attractor。
-   Copywriter Attractor。
-   Product Strategist Attractor。
-   Frontend Engineer Attractor。
-   Conversion Analyst Attractor。
-   Brand Director Attractor。

這些插件不能各自亂跑。它們需要一個協調層。

這就是 Agent OS 的價值。

Prompt 是指令。
Skill 是能力。
Tool 是手段。
Memory 是歷史。
Cognitive Plugin 是專家判斷。
Agent OS 是調度與治理層。

## 9\. 為什麼這比 Skill 更進一步

Skill 解決的是任務可重複性。
認知插件解決的是專家可遷移性。

兩者差異如下：

類型

核心問題

主要內容

風險

Prompt

這次要怎麼回答？

指令、角色、格式

易漂移、短期

Skill

這類任務怎麼做？

流程、工具、模板

偏機械

Tool

要操作什麼？

API、CLI、browser、file

權限風險

Memory

要記住什麼？

偏好、歷史、狀態

污染、過期

Cognitive Plugin

怎麼判斷好壞？

先驗、標準、批判、案例

偽專家化

Expert Attractor

要靠近哪種能力形態？

判斷盆地、工作風格、審核迴路

過度固定

Agent OS

如何調度全部？

權限、版本、工作區、回溯

複雜度

Skill 是「會做」。
認知插件是「會看」。
專家吸引子是「會以某種專家方式看與做」。

## 10\. 高品質認知插件的判準

未來若出現大量認知插件，如何判斷好壞？

本文提出十個標準。

### 10.1 是否有明確領域邊界

好的插件知道自己適用在哪裡，不適用在哪裡。

### 10.2 是否有可檢查的判準

不能只說「高級」「專業」「有質感」，必須有具體判準。

### 10.3 是否包含反例

只有好案例不夠，還需要失敗模式與反例。

### 10.4 是否有批判迴路

插件必須能讓 Agent 檢查自己的輸出，而不是只生成一次。

### 10.5 是否能與記憶系統連接

專家判斷需要累積使用者偏好與專案歷史。

### 10.6 是否能與工具連接

設計插件應能接設計工具、截圖、色彩檢查、可訪問性工具、前端框架。
工程插件應能接 repo、test、CI、linter、deployment。

### 10.7 是否有評估案例

沒有 eval 的插件容易變成玄學 prompt。

### 10.8 是否能被版本化

專家標準會更新，插件必須可版本管理。

### 10.9 是否能被人類審核

插件不應黑箱化。人類需要知道它如何判斷。

### 10.10 是否避免偽專家化

最危險的是插件讓 Agent 更會裝專家，而不是更接近專家判斷。

## 11\. 風險：認知插件也可能製造新問題

認知插件不是萬能解法。它也有風險。

### 11.1 偽專家化

Agent 可能學會專家語氣與表面標準，但缺乏真實判斷。這比普通錯誤更危險，因為它更有說服力。

### 11.2 品味洗白

設計插件可能把某些流行審美包裝成「高級」，導致全球設計趨同。

### 11.3 專家偏見固化

插件會保存某種專家先驗。如果先驗錯誤、過時或過度狹窄，Agent 會系統性偏向錯誤方向。

### 11.4 案例庫污染

若插件吸收低品質案例，會污染判斷。

### 11.5 權威幻覺

使用者可能因為插件名叫「頂級設計師」就過度相信輸出。

### 11.6 多插件衝突

產品策略插件可能要求高轉換率，設計插件要求克制，品牌插件要求差異化，工程插件要求低成本。沒有協調層會互相打架。

### 11.7 過度模板化

認知插件若設計不好，最後會讓所有 Agent 產出同一種「看似高級」的模板。

因此，認知插件必須搭配審核、版本化、反例庫與多樣性機制。

## 12\. 與記憶框架的關係

記憶是認知插件的燃料。

沒有記憶，設計插件每次都重新猜使用者喜好。
有記憶，它可以知道：

-   使用者偏好極簡還是張力。
-   使用者討厭什麼風格。
-   某品牌過去的視覺方向。
-   某專案已經否決哪些版本。
-   哪些文案語氣曾被接受。
-   哪些設計策略曾有效。
-   哪些限制不可違反。

但記憶也需要治理。記憶不能只是堆資料，必須分類：

1.  穩定偏好。
2.  專案暫時狀態。
3.  已否決方向。
4.  可重用案例。
5.  禁忌規則。
6.  風格演化。
7.  使用者回饋。
8.  插件自我修正紀錄。

記憶若沒有治理，會變成污染。
記憶若有治理，會變成養成式能力。

這正是 Agent 從工具走向長期協作者的核心。

## 13\. 與 MCP / Tool 生態的關係

MCP 和工具生態解決的是「Agent 能碰到什麼世界」。
認知插件解決的是「Agent 如何理解與判斷碰到的世界」。

以設計任務為例，工具可以讓 Agent：

-   讀取 Figma。
-   產生 CSS。
-   修改 React component。
-   檢查 contrast ratio。
-   產生 screenshot。
-   跑視覺 regression test。
-   部署 preview。

但工具本身不會告訴 Agent：

-   這個畫面有沒有廉價感。
-   這個品牌是否有記憶點。
-   這個動效是否過度。
-   這個 CTA 是否太弱。
-   這個排版是否不像目標客群。
-   這個設計是否只是套模板。

所以未來的完整結構應該是：

Tool gives action.
Memory gives history.
Skill gives procedure.
Cognitive Plugin gives judgment.
Agent OS gives governance.

## 14\. GitHub 生態的下一波可能方向

本文預測，未來 GitHub 上會逐漸出現以下類型專案。

### 14.1 Expert Plugin Library

各種專家插件庫：

-   Designer plugin。
-   Product manager plugin。
-   Researcher plugin。
-   Security auditor plugin。
-   Legal reviewer plugin。
-   Brand strategist plugin。
-   Architect plugin。
-   Data scientist plugin。
-   Editor plugin。
-   UX researcher plugin。

### 14.2 Taste Dataset / Judgment Dataset

不只是資料集，而是判斷資料集：

-   好設計 vs 壞設計。
-   好架構 vs 壞架構。
-   好文案 vs 壞文案。
-   好研究問題 vs 平庸研究問題。
-   好 PR vs 壞 PR。
-   好產品策略 vs 假策略。

### 14.3 Critique Loop Framework

專門讓 Agent 自我批判與互相批判的框架。

### 14.4 Attractor Runtime

可以載入不同專家吸引子，讓 Agent 在不同認知模式中工作。

### 14.5 Memory-Governed Expert Agent

把記憶治理與專家插件結合。

### 14.6 Expert Eval Benchmarks

測試 Agent 是否真的接近專家判斷，而不是只會說專家語氣。

### 14.7 Agent Style Transfer Beyond Aesthetics

不只是風格遷移，而是認知風格遷移。例如：

-   從工程師思維轉到設計師思維。
-   從設計師思維轉到產品策略思維。
-   從研究員思維轉到審稿人思維。
-   從創作者思維轉到編輯思維。

### 14.8 Multi-Attractor Collaboration

讓多個專家插件協作，形成類似專家小組。

## 15\. 認知插件與「頂級能力」的關係

頂級能力不是單一答案品質，而是穩定判斷結構。

頂級設計師不只是能做漂亮畫面。
頂級工程師不只是能寫正確程式。
頂級研究員不只是能看很多文獻。
頂級產品人不只是能列 roadmap。
頂級策略家不只是能講宏觀敘事。

頂級能力通常包含：

1.  看見問題本質。
2.  排除假問題。
3.  找到關鍵約束。
4.  建立判斷標準。
5.  在多個壞選項中取捨。
6.  知道什麼不用做。
7.  知道什麼看似好但其實錯。
8.  在局部與全局之間切換。
9.  維持風格與目標一致。
10.  把結果推向可交付狀態。

認知插件的目標，不是讓 Agent 變成真正的人類大師，而是讓它在某些任務中更接近這種判斷路徑。

## 16\. 從 Prompt Engineering 到 Cognitive Architecture Packaging

本文認為，Prompt Engineering 的下一階段不是更長的 prompt，而是 Cognitive Architecture Packaging。

也就是：

把某種認知能力包裝成可載入、可調度、可檢查、可版本化的結構。

過去大家分享 prompt。
未來大家可能分享認知包。

一個 prompt 可能是：

You are a world-class designer. Make this landing page more premium.

一個認知包則是：

Load Designer Attractor v0.4.
Use anti-cheapness checklist.
Apply brand memory.
Compare against reference grammar.
Run critique loop twice.
Generate three directions.
Score each by taste rubric.
Select one with highest brand-fit and lowest template-risk.
Produce final layout spec and implementation notes.

這是完全不同的層級。

前者是語句。
後者是認知作業系統的一部分。

## 17\. 對 Noema / Agent OS 的啟示

若要把這個方向接入 Noema / Agent OS，可以這樣設計。

### 17.1 認知插件作為模組

每個插件是一個資料夾，可被 Agent 載入。

### 17.2 插件有 metadata

包括：

-   名稱。
-   版本。
-   適用任務。
-   不適用任務。
-   所需工具。
-   所需記憶。
-   風險等級。
-   評估方法。
-   更新紀錄。

### 17.3 插件有 memory scope

不同插件只讀取相關記憶，避免污染。

### 17.4 插件有 critique loop

每個插件都必須定義自我檢查。

### 17.5 插件有 eval cases

確保不是玄學 prompt。

### 17.6 插件可組合

例如：

Designer + Product Strategist + Frontend Engineer

### 17.7 插件可衝突仲裁

由 Agent OS 判斷哪個插件在當前任務中優先。

這會讓 Agent OS 從工具調度器升級為認知調度器。

## 18\. 結論：未來的差異在專家吸引子

AI 模型會越來越強。
工具會越來越標準。
MCP 會越來越多。
記憶框架會越來越成熟。
Coding Agent 會越來越普及。

當這些逐漸變成基礎設施後，真正的差異會轉向：

誰能讓 Agent 更接近高階專家的判斷結構？

這就是認知插件與專家吸引子的價值。

未來的 Agent 不是只需要更多工具，而是需要更好的認知地形。
不是只要更長 prompt，而是要可保存的專家先驗。
不是只要更多 Skill，而是要能泛化到不同任務的判斷模組。
不是只要會生成，而是要會批判、會取捨、會檢查、會壓縮、會交付。

因此，本文的核心結論是：

Prompt 是語言指令。
Skill 是任務流程。
Tool 是外部能力。
Memory 是歷史狀態。
Cognitive Plugin 是專家判斷結構。
Expert Attractor 是模型行為的認知盆地。
Agent OS 則是這一切的調度與治理層。

下一代開源 Agent 生態，可能不只會比誰接了更多工具，而是比誰能提供更好的專家吸引子。

這才是提示詞之後、Skill 之後，真正值得觀察的泛化插件方向。

## 附錄 A：認知插件最小規格

name: designer-attractor
version: 0.1.0
type: cognitive-plugin
domain: design
use\_cases:
\- landing\_page\_design
\- ui\_review
\- brand\_direction
\- visual\_critique
requires:
tools:
\- browser
\- file\_editor
\- screenshot\_viewer
memory:
\- user\_design\_preferences
\- brand\_history
\- rejected\_directions
modules:
\- domain-priors.md
\- taste-rubric.md
\- anti-cheapness-checklist.md
\- reference-grammar.md
\- critique-loop.md
\- review-protocol.md
evals:
\- landing\_page\_rewrite
\- cheap\_design\_detection
\- brand\_fit\_scoring
risk:
\- style\_homogenization
\- pseudo\_expertise
\- reference\_overfitting

## 附錄 B：頂級設計師插件的輸出流程

1\. Read task brief.
2\. Identify product category and target audience.
3\. Load brand memory.
4\. Extract design constraints.
5\. Generate initial direction.
6\. Run anti-cheapness checklist.
7\. Run information hierarchy check.
8\. Run brand-fit check.
9\. Compare with reference grammar.
10\. Remove unnecessary elements.
11\. Strengthen one memorable design move.
12\. Produce final design spec.
13\. Produce implementation notes.
14\. Produce self-critique.

## 附錄 C：一句話版本

下一代 Agent 插件不只是 Skill，而是 Cognitive Plugin：一種把專家先驗、判斷標準、案例記憶、批判迴路與失敗檢測封裝起來的泛化認知模組，用來把 Agent 拉入某種專家吸引子，使其不只是會做任務，而是更接近專家式判斷。
