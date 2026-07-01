# Cyc-Optional：從外部常識庫到自建 AI-native 常識層

## 基於 TCF、MDAS、ADL 與三態邏輯的 Agent 常識憲法路線圖

**作者：Neo.K / EVEMISSLAB**
**版本：v0.1**
**形式：技術白皮書 / 理論路線圖草稿**

## 摘要

Cyc 計畫曾經試圖以顯式知識庫、本體論、常識規則與形式推理構造人工智慧的常識基礎。其歷史價值不在於它提供了一套可直接復刻的完整答案，而在於它證明了：若 AI 想要穩定理解世界、執行任務、檢查語境、降低幻覺與進行可審計推理，就必須擁有某種外部顯式常識層。

然而，本文主張：未來的 AI-native 常識層不必依賴 Cyc。Cyc 可以被參考、投資、授權、協作或局部整合；但真正關鍵的是建立一套可由現代 LLM、Agent、超圖、Markdown、JSON-LD、向量檢索、知識圖譜與平行裁判器共同運作的新型常識架構。

本文提出「Cyc-Optional」路線：Cyc 是可選加速器，而非架構依賴。即使完全不使用 Cyc，仍可透過 TCF（Theory Compression Format）負責理論壓縮與來源歸屬，MDAS-TCH 負責概念態空間與因果超圖，ADL 負責行動時的強制判斷，三態邏輯負責保留未定與螺旋演化狀態，最終形成一個面向 Agentic AI 的「常識憲法層」。

## 關鍵詞

Cyc、OpenCyc、AI-native Knowledge Layer、TCF、MDAS、ADL、三態邏輯、Agent 常識憲法、神經符號 AI、常識推理、知識圖譜、JSON-LD、Markdown Knowledge Card

# 1\. 問題意識：Cyc 不是終點，而是一個歷史提示

Cyc 的歷史地位很特殊。它不是單純失敗的舊式符號 AI，也不是可以直接拿來解決現代 LLM 問題的萬能知識庫。它更像是一個提前出現的歷史提示：

AI 不能只靠模式擬合。
AI 需要顯式常識、語境、本體、規則、例外與可審計推理。

在 LLM 時代，這個問題重新浮現。大型語言模型可以生成語言、模糊推理、進行摘要、操作工具、寫程式與協助決策，但仍常出現幾類問題：

1.  **語境錯配**：把虛構、現實、法律、醫療、哲學、工程語境混在一起。
2.  **常識幻覺**：生成看似合理但違反基本世界約束的內容。
3.  **來源不明**：結論可能來自權重壓縮，而非可追蹤資料。
4.  **類型混淆**：把人、公司、產品、角色、文件、事件等概念混為一談。
5.  **行動風險**：Agent 不只是回答，還可能發送 Email、修改檔案、操作 API、安排日曆或執行程式。
6.  **未定狀態處理不佳**：模型常把不確定問題包裝成確定答案，或在需要判斷時逃避判斷。

Cyc 的價值就在於，它早就試圖處理這些問題。但 Cyc 的問題也很明顯：符號系統過重、人工知識工程成本太高、容錯率太低、語境管理複雜、一階邏輯與 default reasoning 的邊界過於脆弱。

因此，本文不主張「復活 Cyc」，而主張：

**吸收 Cyc 的問題意識，重建一套不依賴 Cyc 的 AI-native 常識層。**

# 2\. 核心命題：Cyc 可用，但不可依賴

本文的核心命題是：

**Cyc 是可選資源，不是必要基礎。**

這句話有幾層意思。

第一，若 Cyc / OpenCyc / Cycorp 願意授權、合作、投資或被整合，那當然有價值。因為它累積了大量本體工程經驗、概念分類、常識規則與 microtheory 思想。

第二，即使無法取得完整 Cyc，現代 AI 團隊仍可用公開資料、LLM 自動抽取、知識圖譜、語義網、Wikidata、WordNet、DBpedia、企業文件、領域資料庫與人工審核，自建一套常識層。

第三，更重要的是，現代架構不應把 Cyc-like 知識庫當成主體智能，而應把它當成外部裁判、語境索引、類型約束、常識檢查與 provenance 管理層。

換句話說：

**Cyc 的內容可以借。**
**Cyc 的方法可以學。**
**Cyc 的資產可以談。**
**但 Cyc 不是此架構的本體核心。**

本架構的核心應是：

-   TCF：理論標準格式與來源歸屬。
-   MDAS：動態概念超圖與態空間。
-   ADL：行動時的強制判斷。
-   三態邏輯：未定、螺旋、演化狀態保留。
-   LLM / Agent：神經主體與操作介面。
-   Knowledge Layer：可機器解析、可人類閱讀、可追蹤、可裁判的常識層。

# 3\. 為何自己也能做？

「Cyc 的內容我自己也能做」這句話並不是狂妄，而是在現代技術條件下有一定合理性。

在 Cyc 的年代，最大的瓶頸是人工知識工程。人類必須長期手動寫入常識、定義概念、建立關係、處理例外、修正語境。這件事極其昂貴。

但現在不同。現代 AI 系統可以協助：

-   從自然語言文本抽取概念與關係。
-   將理論轉成標準 schema。
-   生成 Markdown knowledge card。
-   轉換 JSON / JSON-LD / RDF / OWL。
-   將概念嵌入向量資料庫。
-   檢查類型錯誤與語境錯配。
-   對多個候選規則進行交叉驗證。
-   自動建立測試案例。
-   對每個知識節點標記來源與可信度。
-   將常識規則轉成 Agent 可調用 API。

這代表現代團隊不必重走 Cyc 的全人工路線。更合理的做法是：

**AI 生成候選知識，人類審核高價值節點，形式系統負責約束，Agent 在使用中持續回饋。**

這不是說自建常識層很容易，而是說它不再需要像 Cyc 當年那樣孤軍奮戰。

# 4\. Cyc 的真正可借鑑部分

Cyc 可借鑑的不是「完整複製它的資料」，而是以下幾個工程思想。

## 4.1 本體工程

Cyc 很重視概念之間的類型關係。例如某個東西是物理物體、抽象物、事件、角色、集合、實例、過程、行動、狀態或關係。

這對 LLM / Agent 極其重要。因為很多錯誤不是知識錯，而是類型錯。例如：

-   把公司當成自然人。
-   把產品名稱當成公司法人。
-   把文件中的條款當成已執行行動。
-   把故事角色當成現實人物。
-   把方法論當成可直接執行工具。
-   把假設當成定理。
-   把使用者偏好當成普遍規則。

因此，Cyc 的本體工程可以成為 TCF §0 原語與 MDAS vertex type 的參照。

## 4.2 Microtheory / 語境片段

Cyc 的 microtheory 思想非常重要。它意識到常識不能放在單一全域真理空間中。不同語境下，規則不同。

例如：

-   現實世界中，人死亡後不能親自簽約。
-   法律語境中，代理人可以代表他人簽署文件。
-   小說語境中，死者可能復活。
-   遊戲語境中，死亡可能只是狀態。
-   神話語境中，神明可能不受一般物理限制。
-   程式語境中，「樹」可能是資料結構，不是植物。

這正好可以改造成 EML 架構中的 **Context Shard（語境片段）**。

## 4.3 Default Reasoning / 預設推理

人類常識大量是「通常如此」，而不是「必然如此」。

例如：

-   鳥通常會飛，但企鵝不會。
-   人通常需要睡眠，但某些敘事設定可能例外。
-   公司通常透過代表人行動，但法人本身不是生物。
-   醫療建議通常需要個人條件，不能絕對化。
-   一般物體通常不能穿牆，但遊戲或科幻設定可能例外。

Cyc 嘗試形式化這類預設推理，但很困難。現代架構不應硬把所有 default 變成二值真偽，而應讓 default 進入三態或多態系統。

在 EML 架構中，可以這樣處理：

-   穩定常識：進入 Ξ / ⊤。
-   高例外常識：進入 Ω。
-   語境敏感常識：綁定 Context Shard。
-   高風險判斷：交給 ADL 強制判斷。
-   無法判斷：標記 Crash / 人工審核。

## 4.4 顯式可審計推理

Cyc 的另一個價值是可追蹤推理鏈。LLM 的知識壓在權重中，很難知道它到底為何下結論。Cyc-like 系統則可以要求：

-   你使用了哪個概念？
-   你依賴哪條規則？
-   你在哪個語境下判斷？
-   你有沒有例外條件？
-   你用了哪個來源？
-   這是原始資料，還是 LLM 擴寫？
-   這是公理、定理、假設、猜想，還是 heuristic？

這正好接上 TCF 的 provenance / attribution 層。

# 5\. EML 自有架構：TCF + MDAS + ADL + 三態邏輯

本文提出一個不依賴 Cyc 的自有架構。

## 5.1 TCF：理論壓縮與來源歸屬

TCF 負責把任意理論或知識系統轉為標準結構：

-   §0 Primitives：核心原語。
-   §1 Axioms：公理系統。
-   §2 DAG：概念依賴圖。
-   §3 Signature：形式語言簽章。
-   §4 Theorems：可推出結論。
-   §5 Proofs：推導鏈。
-   §6 Models：模型與實例。
-   §7 Metrics：壓縮度量。
-   §8 Fingerprint：理論指紋。
-   §9 Provenance：來源與歸屬。

在 Cyc-Optional 架構中，TCF 的作用是：

把常識知識從雜亂文本、圖譜資料、LLM 輸出或 Cyc-like 結構，轉成可機器解析、可版本控制、可追蹤來源的理論單元。

這裡最重要的是 provenance。若某個知識節點來自 OpenCyc、Wikidata、論文、企業文件、使用者輸入或 LLM 擴寫，必須清楚標記。否則常識層很快就會被污染。

## 5.2 MDAS：概念態空間與因果超圖

MDAS-TCH 負責把知識變成動態超圖。

在這裡：

-   概念是 vertex。
-   關係是 edge。
-   多概念不可分結構是 hyperedge。
-   語境是 context shard。
-   規則是可傳播約束。
-   例外是局部覆寫。
-   矛盾是態變化。
-   認知透明度是 Ψ / Δ / Ξ / Θ。
-   糾纏程度是超邊強度。
-   知識積累是 Σ。
-   維度生成能力是 Γ。
-   認知勢壘是 B。

這讓常識層不再是靜態資料庫，而是一個可觀察、可演化、可診斷的概念場。

## 5.3 ADL：Agent 行動時的強制判斷

當 AI 只是寫文章時，未定狀態可以保留。
但當 Agent 要行動時，不能永遠保持曖昧。

例如：

-   要不要發送這封 Email？
-   要不要刪除這個檔案？
-   要不要排一個過去時間的會議？
-   要不要執行這段程式？
-   要不要把某段話當作醫療建議？
-   要不要將某個人加入收件人？

這時候需要 ADL 的強制判斷。

ADL 在此不是形上學裝飾，而是 Agent 執行層的安全機制：

{
"claim": "The user wants to schedule a meeting yesterday.",
"context": "calendar\_agent",
"forced\_judgment": "invalid\_or\_requires\_correction",
"reason": "The requested time is in the past."
}

ADL 的任務是：當系統必須行動時，把模糊狀態壓縮成可執行判斷，或者明確輸出系統不可判斷。

## 5.4 三態邏輯：保留未定與螺旋態

ADL 負責行動時強制判斷，但不是所有問題都應被強制二值化。

很多理論、創造、探索、研究與概念演化，都處於 Ω 螺旋態。

例如：

-   一個尚未完成的新理論。
-   一個正在相變的研究方向。
-   一個可能成立但尚未形式化的架構。
-   一個在不同語境下有不同答案的命題。
-   一個需要更多資料才能判斷的問題。
-   一個正在從直覺變成形式理論的概念。

若把這些狀態硬判為真或假，會破壞創造力。
若把它們全部視為崩潰，也會錯失演化過程。

因此，三態邏輯負責保留：

-   真：穩定成立。
-   假：穩定不成立。
-   Ω：正在演化、尚未穩定、不可立即閉合。

這對常識層很重要，因為常識不是死規則，而是可演化結構。

# 6\. Cyc-Optional Knowledge Layer 的資料模型

一個 AI-native 常識節點可表示如下：

{
"id": "eml:commonsense:HumanPerson",
"label": {
"zh": "人類個體",
"en": "Human Person"
},
"tcf": {
"section": "§0",
"role": "primitive",
"kind": "type"
},
"mdas": {
"logical\_state": "top",
"cognitive\_state": "transparent",
"evolution\_state": "stable",
"entanglement\_state": "conditional",
"type\_vector": {
"logical\_type": "concept",
"cognitive\_type": "explicit\_knowledge",
"solvability\_type": "ordinary",
"paradigm\_layer": "commonsense"
}
},
"relations": \[
{
"predicate": "isA",
"object": "BiologicalEntity",
"context": "ordinary\_physical\_world",
"confidence": 0.98
},
{
"predicate": "canPerform",
"object": "LegalAction",
"context": "ordinary\_legal\_context",
"condition": "alive\_and\_legally\_competent",
"confidence": 0.85
}
\],
"defaults": \[
{
"rule": "A human person is usually alive during ordinary personal action.",
"state": "default\_true",
"exceptions": \[
"fictional\_context",
"legal\_representation",
"posthumous\_processing"
\]
}
\],
"adl": {
"forced\_judgment\_required\_when": \[
"legal\_action",
"medical\_action",
"financial\_action",
"agent\_execution"
\]
},
"triadic": {
"unresolved\_state\_policy": "omega\_until\_context\_fixed"
},
"provenance": {
"source\_type": "self\_built\_or\_public\_ontology",
"source": "manual + LLM distilled + public references",
"review\_status": "needs\_expert\_review"
}
}

此資料模型的重點是：同一個知識節點同時服務多層系統。

-   TCF 看它是理論單元。
-   MDAS 看它是超圖節點。
-   ADL 看它何時需要強制判斷。
-   三態邏輯看它是否允許 Ω 狀態。
-   Agent 看它能否用於行動前檢查。
-   人類看 Markdown card。
-   系統看 JSON / JSON-LD / Graph / Vector。

# 7\. Markdown Knowledge Card 範例

\# Human Person

\## 基本定義
人類個體是一種生物性、社會性、法律語境中可被視為行動主體的存在。

\## 類型
\- BiologicalEntity
\- SocialAgent
\- LegalSubject（在特定法律語境中）
\- CognitiveAgent（在一般認知語境中）

\## 常識規則
\- 人類個體通常有出生與死亡時間。
\- 人類個體死亡後，通常不能親自執行新的物理行動。
\- 人類個體可以透過代理人、遺囑、法人制度或法律程序產生後續法律效果。
\- 在虛構、神話、遊戲或模擬語境中，此規則可被覆寫。

\## 語境片段
\- ordinary\_physical\_world
\- ordinary\_legal\_context
\- fictional\_context
\- game\_context
\- mythological\_context

\## ADL 強制判斷觸發
當 Agent 需要執行法律、金融、醫療、通訊或檔案操作時，若此概念涉及使用者、第三方或權限，必須啟動強制判斷。

\## 三態保留
若語境不明，先標記為 Ω，不直接判定真偽。

\## 來源
\- EML 自建常識層
\- 可選：OpenCyc-like ontology
\- 可選：Wikidata / WordNet / DBpedia
\- 可選：專家審核

# 8\. 路線圖

## Phase 1：自建最小常識層

不需要先買 Cyc，也不需要先做全世界常識。

先從 Agent 最常出錯的類別開始：

-   時間。
-   人物。
-   組織。
-   法人。
-   文件。
-   權限。
-   Email。
-   日曆。
-   檔案。
-   醫療高風險。
-   法律高風險。
-   金融高風險。
-   虛構世界語境。
-   程式開發需求矛盾。

目標不是完整，而是先能攔截高頻錯誤。

## Phase 2：TCF 標準化

將每個常識模組轉成 TCF：

-   核心概念 → §0。
-   常識規則 → §1。
-   關係依賴 → §2。
-   可推出結論 → §4。
-   推理路徑 → §5。
-   使用場景 → §6。
-   來源歸屬 → §9。

這會讓常識層具備版本控制與理論指紋。

## Phase 3：MDAS 超圖化

將 TCF 知識轉成 MDAS-TCH：

-   每個概念是 vertex。
-   每條關係是 edge。
-   每組不可分語境是 hyperedge。
-   每個節點都有認知態、演化態、糾纏態。
-   每個裁判器都能讀取圖結構。

這一步是從「知識庫」變成「動態認知圖」。

## Phase 4：建立平行裁判器

裁判器分為多類：

1.  類型裁判器。
2.  語境裁判器。
3.  時間裁判器。
4.  權限裁判器。
5.  常識裁判器。
6.  來源裁判器。
7.  高風險領域裁判器。
8.  行動前檢查器。
9.  虛構語境裁判器。
10.  理論一致性裁判器。

每個裁判器不一定給出唯一答案，而是輸出：

-   成立。
-   不成立。
-   語境不足。
-   需要人工確認。
-   Ω 未定。
-   ADL 強制判斷失敗。
-   Crash。

## Phase 5：接入 LLM / Agent

當 LLM 生成答案或 Agent 要執行行動時，系統呼叫常識層：

{
"agent\_action": "send\_email",
"claim": "Send this medical instruction to all customers.",
"context": "email\_agent",
"risk\_level": "high"
}

常識層回傳：

{
"verdict": "blocked\_or\_requires\_review",
"reasons": \[
"medical advice cannot be generalized to all customers",
"recipient group is too broad",
"requires human review"
\],
"state": "ADL\_forced\_rejection"
}

## Phase 6：Cyc / OpenCyc 作為可選加速器

若未來資源允許，可以把 Cyc 放進以下位置：

-   作為本體參考。
-   作為常識資料源。
-   作為 microtheory 設計參照。
-   作為 benchmark。
-   作為歷史對照組。
-   作為授權資料庫。
-   作為合作對象。
-   作為收購或投資候選。

但即使沒有 Cyc，架構仍然成立。

這就是 Cyc-Optional 的核心。

# 9\. 商業與研究意義

這條路線對小型 AI 公司或研究團隊有特殊意義。

大公司競爭的是模型本體、算力、資料與產品入口。小團隊很難正面訓練下一代超大模型。但小團隊可以做模型外部的智慧層：

-   Agent 常識層。
-   企業知識憲法。
-   AI 行動前裁判器。
-   高風險領域檢查器。
-   理論壓縮與知識治理工具。
-   AI-native Markdown / JSON-LD 知識標準。
-   個人或組織專用的可審計知識庫。
-   多模型共用的外部常識 API。

這種產品不需要取代 GPT、Gemini、Claude 或其他模型。它只需要成為它們外部的結構性補丁。

因此，Cyc-Optional 路線的商業定位不是：

我們要做另一個 LLM。

而是：

我們要做 LLM / Agent 的外部常識作業系統。

# 10\. 與 Cyc 的關係表

問題

Cyc 路線

Cyc-Optional 路線

主體智能

符號常識系統承擔大量智能功能

LLM / Agent 作為神經主體

知識來源

人工編碼為主

LLM 抽取 + 公開資料 + 人工審核

語境管理

Microtheory

Context Shard + MDAS 態標記

推理方式

符號推理為核心

平行裁判 + 神經重寫 + 局部形式化

資料格式

專用表示

MD / JSON-LD / RDF / Graph / Vector / TCF

未定狀態

default / exception / unknown

Ω 螺旋態 + ADL 強制判斷

可審計性

強

透過 TCF provenance 強化

擴展方式

知識工程

AI 輔助蒸餾 + 人類治理

對 Cyc 依賴

必須使用 Cyc 本體

可使用，也可完全不用

# 11\. 最小可行系統

一個最小可行系統不需要宏大到包含全部常識。它只需要做三件事：

1.  把常見概念做成 Knowledge Card。
2.  對 Agent 行動做常識檢查。
3.  對檢查結果提供結構化回饋。

最小架構：

User / Agent Request
↓
LLM Semantic Parser
↓
TCF Knowledge Card Retrieval
↓
MDAS Context + Type Graph
↓
Parallel Judges
↓
ADL Forced Judgment if Action Required
↓
Triadic Ω if Unresolved
↓
LLM Rewrite / Block / Ask / Execute

這個架構的價值不是一次做到全知，而是每次比裸 LLM 多一層結構性防線。

# 12\. 理論定位

Cyc-Optional 路線的理論定位如下：

它不是舊式符號 AI。
它不是純 RAG。
它不是普通知識圖譜。
它不是聊天記憶。
它不是 LLM 自我反思 prompt。
它是一個外部化、格式化、可審計、可演化的 Agent 常識憲法層。

更精確地說：

-   RAG 解決「查什麼」。
-   Knowledge Graph 解決「誰和誰有關」。
-   Memory 解決「使用者以前說過什麼」。
-   TCF 解決「這個理論如何標準化與追蹤來源」。
-   MDAS 解決「概念如何處於動態態空間」。
-   ADL 解決「必須行動時如何強制判斷」。
-   三態邏輯解決「未定與演化狀態如何不被錯殺」。
-   Cyc-Optional Knowledge Layer 解決「Agent 如何在世界常識中行動」。

# 13\. 結論：Cyc 是可選捷徑，不是終極答案

Cyc 很可惜，也很珍貴。它提前指出了 AI 需要常識、本體、語境與可審計推理。但它不應被神化，也不應被視為唯一道路。

在今天，真正可行的路線不是回到 Cyc，而是建立一個新的 AI-native 常識層：

用 LLM 生成與理解。
用 TCF 壓縮與歸屬。
用 MDAS 圖化與狀態化。
用 ADL 做行動時強制判斷。
用三態邏輯保留 Ω 未定與螺旋演化。
用 Agent OS 接入實際工作流。
用人類審核高價值與高風險節點。
用 Cyc 作為可選加速器，而不是必要依賴。

這條路線的意義在於：即使沒有資金購買 Cyc，即使沒有大型公司的模型訓練能力，也可以先從格式、知識卡、裁判器、語境層與 Agent API 開始。

Cyc 的精神不是「建立一座封閉的常識城堡」。

它真正該被繼承的是：

**讓 AI 擁有可檢查、可追蹤、可修正、可演化的世界常識。**

而這件事，不必等待任何公司授權。

可以自己開始。

# 附錄 A：一句話版

Cyc 可以參考、合作或購買，但不是必要條件；真正關鍵是用 TCF、MDAS、ADL 與三態邏輯建立一套自有的 AI-native 常識憲法層，使 LLM / Agent 在行動前能進行語境、類型、常識、來源與風險裁判。

# 附錄 B：公開倡議版

如果你正在研究 LLM、Agent、AI 安全、知識圖譜、RAG、語義網或企業 AI，不要只問「要不要復活 Cyc」。更好的問題是：如何把 Cyc 當年的問題意識轉譯成今天的 AI-native 系統？

我們可以不買 Cyc，也可以不依賴 Cyc。
但我們不能假裝 AI 不需要常識層。

下一代 Agent 需要的不是更長的 prompt，而是一個可審計、可版本化、可行動前檢查的外部常識憲法。

這就是 Cyc-Optional 路線。
