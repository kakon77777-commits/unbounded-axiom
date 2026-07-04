# 從 Human-Centric Web 到 AI-Readable Web：AI 爬蟲、Agent 與機器讀者時代的網站架構轉換

## Toward Deterministic Corpus Ingestion, Machine-Readable Rights, and Agent-Native Publication Layers

**作者**：Neo.K / EVEMISSLAB\
**版本**：v0.1 Draft\
**日期**：2026-07-01\
**類型**：MD 論文 / 技術哲學論文 / AI-native Web Architecture 觀察稿\
**關鍵詞**：AI-readable web、AI crawler、Agent-first web、llms.txt、robots.txt、AICL、AIRS、AILP、deterministic ingestion、machine-readable rights、AI-native publication、corpus manifest、Agent-native web

***

## 摘要

過去三十年的網站架構基本上建立在人類中心假設之上。網站首先服務人類瀏覽者，其次服務搜尋引擎 crawler；因此網站設計重點通常集中於首頁、導覽列、SEO metadata、社群分享、頁面速度、可訪問性與搜尋收錄。自動化 crawler 在舊時代多半被視為外部訪客：要不是搜尋引擎索引者，要不是需要被限制、防堵或降低爬取成本的資料擷取者。

然而，AI 與 Agent 時代改變了這個前提。網站的新讀者不再只有人類與搜尋引擎，而是包括 AI crawler、LLM crawler、RAG 系統、embedding indexer、自主 Agent、模型訓練管線、機器推理流程與未來的 AI 協作者。這些讀者不只是「看」網站，而是會抓取、解析、切分、索引、向量化、摘要、引用、重組、訓練、微調，甚至把網站內容作為未來行動與推理的基礎。

本文提出：Web 正在從 **Human-Centric Web** 轉向 **AI-Readable Web**。這不是單純把網站開放給 AI 爬取，也不是把 robots.txt、SEO 或 `/llms.txt` 視為終點，而是需要新增一個面向 AI、Agent 與機器讀者的網站結構層。本文將這個方向整理為三個核心命題：

```text
1. AI 不只是 crawler，而是新的正式讀者。
2. 網站不只需要被索引，而需要被決定性攝取。
3. AI-readable web 不只是開放問題，而是 manifest、corpus、rights、provenance、tools 與 governance 的架構問題。
```

本文進一步提出 **抽獎式攝取** 與 **決定性攝取** 的區分。傳統網站若缺乏 stable ID、canonical route、corpus manifest、raw/page/API 分層、redirects、broken-link validation 與 machine-readable rights layer，AI crawler 可能反覆抓到錯誤路徑、舊版頁面、重複內容、404 頁面或不完整 corpus，造成 AI 對網站內容的理解變成不穩定、斷裂、錯位與部分幻覺化。

因此，本文主張，AI 時代的網站架構需要從：

```text
Human UI + SEO metadata + robots.txt
```

升級為：

```text
Human UI
Search Metadata
AI Ingestion Layer
Agent Capability Layer
Rights / Provenance / Governance Layer
```

這一轉換不代表所有網站都應該無條件開放 AI 學習；相反，它意味著網站應能清楚表達哪些內容可讀、哪些內容可引用、哪些內容可訓練、哪些內容需要授權、哪些內容是正本、哪些內容是歷史版本，以及 AI 應該如何穩定、可追溯、可驗證地攝取網站知識。

***

# 1. 引言：網站的新讀者

傳統網站主要面向人類。即使搜尋引擎 crawler 很早就成為網路基礎設施的一部分，它們在網站想像中仍然屬於輔助層：搜尋引擎索引網站，再把人類使用者導回網站。這一模式形成了一種隱含契約：

```text
網站提供內容。
搜尋引擎索引內容。
搜尋引擎返回流量。
人類回到網站閱讀。
```

AI 時代正在破壞這個契約。AI crawler 與 LLM 系統抓取內容後，不一定把使用者導回原網站，而是可能直接在回答中消化、摘要、重組、引用甚至替代原頁面。Cloudflare 在 Pay Per Crawl 的說明中也將其定位為一種讓內容所有者控制與貨幣化 AI crawler 存取的機制，並以 HTTP 402 與 crawler pricing 讓 AI crawler 不是單純被允許或拒絕，而是進入可定價、可協商的存取模型。

這代表網站的新問題不再只是：

```text
如何讓人類看見？
如何讓搜尋引擎收錄？
如何阻止惡意爬蟲？
```

而是：

```text
AI 應該如何讀取這個網站？
AI 會讀到哪些內容？
AI 會不會讀錯？
AI 會不會把舊版當新版？
AI 能否知道 canonical source？
AI 能否知道哪些內容可引用、可訓練、可商業使用？
Agent 能否知道哪些工具可以調用？
```

如果網站無法回答這些問題，AI crawler 仍然可能大量訪問網站，但其攝取行為會變成猜測式、片段式、重複式與非決定性。

***

# 2. 現有趨勢：AI-readable Web 的前兆

## 2.1 Agent-first Web 的出現

2026 年已有研究直接提出 **Agent-First Web** 的概念，指出 Web 過去三十年假設主要內容消費者是人類，但 AI agents 作為人與網路內容之間的中介，正在使這個假設失效。該研究主張需要在 access、economic、content 等層面重新設計 Web，使 Agent 成為一等參與者，而不是被 CAPTCHA、封鎖與舊經濟模型排斥的外部擷取者。

這個方向說明，外部研究已經開始意識到：問題不只是 AI crawler 是否應被阻擋，而是 Web 的基礎假設正在改變。若 Agent 會代表人類閱讀、比較、購買、整理、引用與行動，那麼網站就不能只把它們當成「不該來的機器流量」。

## 2.2 `/llms.txt`：AI 入口索引的早期形式

`/llms.txt` 提案於 2024 年提出，主張網站可以提供一份 LLM-friendly Markdown 檔案，讓 LLM 在使用網站時取得背景資訊、指引與重要連結。這是 AI-readable web 的早期代表，因為它明確承認 HTML UI 並不總是適合 LLM 直接理解，網站需要一個給模型閱讀的入口。

但 `/llms.txt` 主要解決的是「AI 應該去哪裡讀」的問題。它不必然解決 stable ID、版本、權利、raw/canonical 分層、corpus manifest、broken link validation、Agent tools 或訓練授權等問題。因此，它更像是 AI-readable web 的入口索引，而不是完整的 AI-native publication architecture。

## 2.3 robots.txt 的不足

Google 的 Search Central 文件明確指出，若要讓頁面不出現在 Google 中，應使用 noindex 或密碼保護，而不是單靠 robots.txt；robots.txt 主要是 crawler 存取規則與流量管理工具，不是內容消失、權限授權或完整治理機制。

OpenAI 也提供官方 crawler 文件，將 OAI-SearchBot 與 GPTBot 等 crawler 分開說明，並讓網站管理者用 robots.txt tags 管理網站內容與 OpenAI 產品的互動方式。這顯示 AI crawler 已開始從傳統搜尋 crawler 中分化出不同目的、不同用途、不同政策的機器讀者。

因此，robots.txt 的問題不是「無用」，而是它原本不是為 AI learning、AI answer input、RAG、embedding、fine-tuning、distillation、commercial training 這些用途設計的。它能回答「能不能進來」，但很難回答「進來後可以怎麼學」。

## 2.4 Content Signals 與 AI 用途分化

Cloudflare 的 Content Signals Policy 將內容使用信號分為 `search`、`ai-input`、`ai-train` 三類，並整合進 robots.txt 語境中。Cloudflare 文件也說明這三類分別對應搜尋索引、即時 AI 回答輸入，以及模型訓練或微調。

這是一個重要轉折：網站對 crawler 的聲明開始從「能不能抓」走向「抓了之後可以用來做什麼」。然而，三分法仍然偏粗。AI 對內容的使用還可能包括：

```text
RAG retrieval
embedding storage
semantic cache
temporary context use
long-term memory
summary generation
short quotation
style imitation
fine-tuning
distillation
synthetic data generation
commercial model training
```

因此，Content Signals 是 AI-readable web 的重要前兆，但仍需要更細的 machine-readable rights spectrum。

## 2.5 TDM Reservation Protocol 與機器可讀權利保留

W3C Community Group 的 TDM Reservation Protocol 定義了一種用於表達 Text and Data Mining 權利保留與授權政策發現的 Web protocol。其目標是讓權利人能以簡單、實用、機器可讀的方式聲明 TDM 權利保留，並協助 TDM actor 找到授權政策。

EDRLab 對 TDMRep 的說明也指出，該方向可讓權利人表達 mining rights 是否保留、如何聯絡權利人，以及是否存在可用授權。

這說明機器可讀權利層已經不是純理論構想；它正在被出版、法律與 TDM 語境推動。不過，TDM 仍主要聚焦文字與資料探勘，而 AI-readable web 面對的是更廣的機器攝取鏈：crawl、parse、embed、retrieve、summarize、train、fine-tune、distill、generate、commercialize。

## 2.6 Pay-per-crawl 與內容存取經濟

Cloudflare 的 Pay Per Crawl 進一步把 AI crawler 存取推向經濟協商層。其文件說明，當 AI crawler 請求受保護內容時，可以提出支付意圖，否則可能收到 HTTP 402 Payment Required 與內容價格；crawler 也可用 `crawler-exact-price` 或 `crawler-max-price` 表達願付價格。

這說明 AI-readable web 不只是一個技術問題，也是新的內容經濟問題。當 AI 系統從「導流」變成「直接消費內容」，網站所有者會要求新的控制、授權與補償機制。

## 2.7 Agent Readiness：新標準仍極早期

Cloudflare 在 2026 年推出 Agent Readiness score，主張 Web 曾經學會對瀏覽器與搜尋引擎說話，現在也需要學會對 AI agents 說話。其掃描結果指出，在其 200,000 個高流量網域樣本中，robots.txt 接近普遍，但多數仍是為傳統搜尋 crawler 而寫；一些新興 agent 標準如 MCP Server Cards 與 API Catalogs 在資料集中出現少於 15 個站點。

這點非常關鍵：外部世界已經開始意識到網站需要 agent-ready，但實作採用率仍非常低。這代表 AI-readable web 還在早期，尚未形成成熟範式。

***

# 3. 問題：AI crawler 來了，但不代表它吃對了

很多網站管理者會把 AI crawler 的出現理解為二元問題：

```text
要不要讓 AI 爬？
要不要擋 AI？
要不要收 AI 錢？
```

但對於希望被 AI 正確理解的網站，真正問題不是 crawler 是否出現，而是 crawler 是否能正確、穩定、完整、可追溯地攝取內容。

本文提出一個區分：

```text
抽獎式攝取（Lottery-like Ingestion）
決定性攝取（Deterministic Ingestion）
```

## 3.1 抽獎式攝取

抽獎式攝取指的是：AI crawler 每次訪問網站時，都可能因路由、索引、連結、slug、版本、raw/page 分層不清而得到不同的 corpus 邊界。

典型現象包括：

```text
今天 crawler 看到某個 URL。
明天同一 URL 變成 404。

今天 crawler 看到 raw Markdown。
但沒有看到 canonical HTML page。

今天 crawler 抓到 paper-173。
下次 paper-173 因排序變動指向另一篇。

今天 crawler 沿著 Markdown 中的短相對連結進入 /papers/t。
但 /papers/t 其實只是公式或符號誤解析，不是真實文章。

某些文章明明存在。
但沒有被 sitemap、llms、manifest 或 canonical index 暴露。

某些頁面其實不存在。
但 crawler 因錯誤 href 反覆抓取。
```

對一般網站而言，這可能只是 SEO 或 404 問題。\
對 AI-readable corpus 而言，這是知識攝取問題。

因為 AI 不只是要顯示搜尋結果，而可能把這些內容放入 RAG、embedding index、agent memory、training data 或未來引用鏈。一旦 ingestion 本身不穩，AI 對網站的理解就會出現錯位。

## 3.2 決定性攝取

決定性攝取指的是：AI crawler 不需要猜測網站結構，而是能依照明確 manifest、stable ID、canonical URL、raw source、metadata、timeline、rights policy 與 validation report 進行可重複攝取。

基本要求包括：

```text
每篇內容有 stable ID。
每個 stable ID 有唯一 canonical URL。
每篇內容有 raw source URL。
每篇內容有 metadata JSON。
舊 URL 能 redirect 到 canonical URL。
sitemap 只放 canonical route。
llms.txt 指向 AI manifest。
corpus.jsonl 提供批次攝取入口。
rights-spectrum.json 表達 AI 使用與學習邊界。
broken link validator 避免假路徑污染 crawler。
```

核心轉換是：

```text
Before:
Crawler guesses the site.

After:
Crawler follows the manifest.
```

***

# 4. Human-Centric Web 的歷史限制

人類中心網站不是錯誤，而是特定時代的合理設計。

在舊時代，網站主要需要回答：

```text
使用者是否看得懂？
首頁是否清楚？
導覽是否順暢？
SEO 是否完整？
搜尋引擎是否能收錄？
社群分享是否正常？
```

因此，網站結構通常由人類閱讀動線決定。Markdown 檔案、PDF、DOCX、HTML、API、raw source、archive page、old route、draft page 等內容，只要人類能找到或站長知道放在哪裡，就算可用。

但 AI crawler 不是這樣讀網站。AI crawler 會：

```text
掃 sitemap。
讀 robots.txt。
沿 href 爬行。
解析 Markdown。
切分文本。
抽取 metadata。
建立向量索引。
比對重複內容。
根據 URL 推測語義。
根據路由推測版本。
根據連結推測 corpus 邊界。
```

這意味著，人類覺得「差不多能看」的網站，對 AI 來說可能是不穩定的資料空間。

***

# 5. AI-Readable Web 的核心定義

本文將 **AI-Readable Web** 定義為：

```text
一種將 AI crawler、LLM、Agent、RAG 系統、embedding indexer、模型訓練管線與機器推理流程視為正式讀者，並為其提供穩定、可追溯、可驗證、可授權、可批次攝取之結構層的網站架構。
```

AI-readable web 不等於：

```text
讓 AI 隨便爬。
把所有資料公開。
只放一個 /llms.txt。
只改 robots.txt。
只做 SEO。
只做 API。
```

AI-readable web 要處理的是：

```text
AI 應該讀什麼？
AI 應該從哪裡讀？
哪份是正本？
哪份是歷史版本？
哪份是 raw source？
哪份是 human-rendered page？
哪些可引用？
哪些可訓練？
哪些需要授權？
哪些是 deprecated？
哪些需要 attribution？
哪些內容應該被排除？
```

因此，AI-readable web 是一種新的 publication architecture。

***

# 6. 從 SEO 到 AIO / GEO，再到 AICL

SEO 解決的是搜尋引擎可見性。\
AIO / GEO 解決的是 AI 搜尋與生成式回答中的可見性。\
但 AI-readable web 解決的不是單純「被看見」，而是「被正確攝取」。

可用以下層級區分：

```text
SEO:
讓搜尋引擎找到我。

AIO / GEO:
讓 AI 搜尋或生成式回答提到我。

AI-readable Web:
讓 AI 正確讀取、引用、追溯、批次攝取與遵守權利邊界。

AICL:
在網站中實作 AI ingestion、corpus manifest、agent capability、governance 的工程層。

AIRS / AILP:
在網站中實作 AI 使用、學習、訓練、引用、補償與授權的機器可讀權利層。
```

所以，AICL 不是 SEO 的變體，也不是 `/llms.txt` 的別名。它是 AI-readable web 的工程落地層。

***

# 7. AICL：AI Ingestion & Capability Layer

本文建議將 AI-readable web 的核心工程層命名為：

```text
AICL = AI Ingestion & Capability Layer
中文：AI 攝取與能力層
```

AICL 包含四個基本子層：

```text
1. Manifest Layer
2. Corpus Layer
3. Capability Layer
4. Governance Layer
```

## 7.1 Manifest Layer

Manifest Layer 提供 AI 的入口地圖。

建議路由：

```text
/llms.txt
/ai/index.md
/ai/manifest.json
/ai/timeline.json
/sitemap.xml
```

它回答：

```text
這個網站是什麼？
canonical domain 是什麼？
AI 應該去哪裡讀？
哪些文件是正本？
哪些 index 可批次讀取？
```

## 7.2 Corpus Layer

Corpus Layer 提供 AI-readable corpus。

建議路由：

```text
/ai/corpus.json
/ai/corpus.jsonl
/raw/{id}.md
/api/papers/{id}.json
/p/{id}/
```

它回答：

```text
每篇文件的 stable ID 是什麼？
原始檔在哪？
HTML 頁在哪？
metadata 在哪？
時間線在哪？
標籤、系列、版本、hash 是什麼？
```

## 7.3 Capability Layer

Capability Layer 讓 Agent 知道可用工具。

這一層可以先是靜態 catalog：

```text
/ai/tools/catalog.json
/ai/tools/openapi.json
```

未來再接：

```text
MCP Resources
MCP Tools
OpenAPI endpoints
validation tools
citation API
search API
compare-version API
```

MCP 的 Resources 可讓 server 暴露能提供模型上下文的資料，如檔案、資料庫 schema 或應用資訊；Tools 則讓模型能呼叫外部功能。這說明 Agent-readable web 不只需要內容，也需要受限、可描述、可治理的能力表面。

OpenAPI 則提供語言無關的 HTTP API 描述方式，讓人類與電腦不必讀原始碼或檢查網路流量，也能理解服務能力。

## 7.4 Governance Layer

Governance Layer 提供權利、引用、版本與來源說明。

建議路由：

```text
/ai/governance/license.md
/ai/governance/citation-policy.md
/ai/governance/provenance.md
/ai/governance/versioning-policy.md
/ai/rights-spectrum.json
```

它回答：

```text
AI 可以如何引用？
可以如何摘要？
可以如何訓練？
是否允許商業使用？
是否需要授權？
版本衝突時以誰為準？
內容來源與修改歷史是什麼？
```

***

# 8. AIRS / AILP：從訪問規則到學習合約

AI-readable web 不應只處理「能不能爬」，還應處理「可以怎麼學」。

因此本文建議引入：

```text
AIRS = AI Rights Spectrum
AI 權利光譜

AILP = AI Learning Permission Protocol
AI 學習許可協議
```

其核心是：AI 對內容的權利不應只有 allow / disallow，而應該是多維光譜。

例如：

```text
search_indexing: 1.0
ai_answer_input: 1.0
rag_retrieval: 1.0
embedding_storage: 0.8
non_commercial_training: 0.8
commercial_training: license_required
fine_tuning: license_required
distillation: license_required
verbatim_memorization: 0.0
style_imitation: 0.0
citation_required: true
attribution_required: true
```

這與 Content Signals、TDMRep、Pay Per Crawl 等趨勢相容，但更細。它不只表達 crawler access，也表達 AI learning depth。

***

# 9. AI-readable Web 的基本架構

一個 AI-readable site 應具有如下架構：

```text
/
  Human UI

/docs/
  Human-readable docs

/p/{id}/
  Canonical paper pages

/raw/{id}.md
  Raw source files

/api/papers/{id}.json
  Machine-readable metadata

/llms.txt
  LLM entry index

/llms-full.txt
  Full corpus index

/ai/
  AI-native entry

/ai/manifest.json
  Machine-readable manifest

/ai/corpus.jsonl
  Bulk ingestion file

/ai/timeline.json
  Chronological index

/ai/tools/catalog.json
  Agent tool catalog

/ai/rights-spectrum.json
  Machine-readable AI rights declaration

/ai/governance/
  license, citation, provenance, versioning
```

這樣，網站不再只是：

```text
人類 UI + SEO
```

而是：

```text
Human UI
Search layer
AI ingestion layer
Agent capability layer
Rights and governance layer
```

***

# 10. 時間分類優先於主題分類

對大型理論 corpus 而言，主題分類不應作為 source tree 的主結構。

原因是：大量理論文件往往跨 AI、哲學、數學、工程、治理、產品、語言、認知與本體論。一篇文章可能同時屬於多個領域。若強迫主題分類，將造成：

```text
分類歧義
資料夾爆炸
跨域文章錯放
理論生成時間線被破壞
Agent 誤分類
後續 corpus 演化不可追溯
```

因此，大型 AI-readable theoretical corpus 應採用：

```text
資料夾保存時間。
metadata 保存語義。
registry 保存身份。
tags 保存多維索引。
```

建議 source tree：

```text
content/papers/
  2024/
  2025/
  2026/
    2026-07/
  undated/
  imported/
  legacy/
```

語義分類交給：

```text
frontmatter
registry/papers.json
/ai/corpus.jsonl
/ai/timeline.json
/tags/
/series/
/domains/
```

這使 AI 可以同時按時間、系列、標籤、領域與 stable ID 讀取 corpus，而不是被單一主題資料夾限制。

***

# 11. Stable ID 與 Canonical Route

AI-readable corpus 必須避免依賴不穩定 URL。

錯誤做法：

```text
/papers/paper-173.md.html
/papers/中文長檔名.md.html
/papers/generated-index-order-slug
```

正確做法：

```text
/p/lm-000173/
/raw/lm-000173.md
/api/papers/lm-000173.json
```

每篇文件應有：

```text
stable ID
canonical URL
raw URL
metadata URL
source path
hash
created / updated
date confidence
rights profile
```

這可以讓 AI 在不同時間、不同入口、不同 crawler 策略下，仍然找到同一篇文件。

***

# 12. Crawler-Safe Link Policy

AI-readable web 必須處理 Markdown 與 HTML 中的相對連結污染問題。

若 Markdown 中的公式、符號或短字串被解析成相對連結，crawler 可能會訪問不存在路徑。例如：

```text
/papers/t
/papers/s
/papers/x_0
/papers/problem
/papers/query
```

這些路徑對人類可能只是小錯，但對 AI crawler 可能成為假 corpus 邊界。

因此 build system 應有：

```text
broken link validator
relative link whitelist
unknown link downgrade
nofollow for unresolved local href
route consistency report
```

AI-readable web 的原則是：

```text
不存在的路徑不應被呈現為可爬入口。
```

***

# 13. 從防爬到可治理開放

AI-readable web 不表示所有網站都應開放 AI crawler。

網站未來可能分化成兩類：

```text
1. 不希望 AI 學習的網站
   使用 robots.txt、noindex、auth、paywall、anti-bot、rights reservation。

2. 希望 AI 正確學習的網站
   提供 manifest、corpus、stable ID、rights-spectrum、citation policy。
```

兩者並不矛盾。真正的問題不是「開放或封閉」，而是「是否可聲明、可解析、可執行、可追溯」。

舊時代只有粗糙的二元選項：

```text
Allow
Disallow
```

AI-readable web 應提供更細的狀態：

```text
可搜尋。
可摘要。
可引用短句。
可 RAG。
可 embedding。
可非商業訓練。
商業訓練需授權。
不可逐字記憶。
不可風格模仿。
不可替代性生成。
```

這才是 AI 時代的內容治理。

***

# 14. Logic Matrix 作為案例：從備份站到 AI-readable corpus

Logic Matrix 這類網站不是普通 blog。

它更像：

```text
公開理論 corpus
AI-readable archive
GitHub-backed knowledge repository
future model-facing theoretical memory
machine-ingestible research layer
```

因此，傳統網站設計不足以支撐它的目的。

如果 Logic Matrix 只用單層 `papers/` 與單一 `build.py` 生成所有頁面，那麼 AI crawler 可能會出現：

```text
吃到舊路徑。
漏掉新文件。
抓到 404。
抓到重複 raw。
分不清 paper page 與 source file。
不知道哪篇是 canonical。
不知道哪個版本是目前版本。
不知道權利與引用方式。
```

因此，Logic Matrix 應從靜態備份站升級為：

```text
Logic Matrix Corpus Engine
```

其核心不是把網站變漂亮，而是讓 AI 能穩定攝取。

***

# 15. 最小可行 AI-readable Web

第一階段不需要做重型 API，也不需要馬上做 MCP server。

最小版本可以是：

```text
/llms.txt
/ai/index.md
/ai/manifest.json
/ai/corpus.jsonl
/ai/timeline.json
/ai/rights-spectrum.json
/ai/governance/citation-policy.md
/p/{id}/
/raw/{id}.md
/api/papers/{id}.json
/sitemap.xml
/robots.txt
```

這已經能把網站從「crawler 自己猜」提升到「crawler 依 manifest 攝取」。

***

# 16. 中階 AI-readable Web

中階版本加入：

```text
redirects.json
broken-links.json
route-consistency-report.json
hash index
version history
series index
domain index
tag index
OpenAPI catalog
tool catalog
citation API
search API
```

這時網站開始從 AI-readable 進入 Agent-readable。

***

# 17. 高階 AI-readable Web

高階版本加入：

```text
MCP Resources
MCP Tools
capability negotiation
pay-per-crawl
license negotiation
content pricing
agent authentication
audit logs
AI-specific rate limits
rights-aware retrieval API
```

這時網站不只是被 AI 讀，而是能與 Agent 互動、交易、授權、驗證與協作。

***

# 18. 與現有趨勢的關係

本文提出的 AI-readable web 與現有趨勢關係如下：

```text
robots.txt:
處理 crawler 存取規則，但不足以處理 AI 學習深度。

llms.txt:
提供 LLM 入口索引，但不足以處理完整 corpus governance。

Content Signals:
開始區分 search、ai-input、ai-train，但維度仍粗。

TDMRep:
提供 TDM 權利保留與授權發現基礎，但不覆蓋完整 AI ingestion chain。

Pay Per Crawl:
處理 AI crawler 存取經濟，但不保證 corpus ingestion 正確。

Agent-first Web:
指出 Web 需要重新面向 Agent 設計，但仍需更細的 publication / corpus layer。

AICL:
補上 AI ingestion、corpus、capability、governance 的工程層。

AIRS / AILP:
補上 AI learning permission 與 rights spectrum 的權利層。
```

所以本文不是否定既有標準，而是將其整理成更完整的架構空間。

***

# 19. 核心命題

本文的核心命題可以總結為：

```text
1. AI 已經成為網站的新讀者。
2. AI crawler 不是傳統搜尋 crawler 的簡單延伸。
3. AI 對網站的使用不只是 indexing，而是 ingestion、embedding、RAG、training、reasoning、agent action。
4. 傳統 human-centric web 無法保證 AI 正確攝取。
5. 缺乏 stable ID、canonical route、manifest、rights layer 的網站，會讓 AI 攝取變成抽獎。
6. AI-readable web 的目標不是無條件開放，而是可治理、可追溯、可驗證的機器攝取。
7. AICL 可作為 AI-readable web 的工程層。
8. AIRS / AILP 可作為 AI-readable web 的權利層。
9. 未來網站將從 Human UI + SEO metadata，走向 Human UI + AI ingestion + Agent capability + rights governance 的多層架構。
```

***

# 20. 結論

Web 正在進入新的讀者結構。

過去網站面向人類，搜尋引擎只是索引層。\
現在 AI crawler、LLM、Agent、RAG、embedding system、training pipeline 都開始成為網站內容的實際使用者。這些使用者不只是閱讀頁面，而是將網站內容轉化為語義索引、推理材料、回答依據、模型能力與未來行動。

因此，網站架構必須從人類中心擴展為 AI-readable。

這不代表放棄人類 UI，也不代表讓 AI 無限制抓取。相反，它要求網站建立更清楚的邊界：

```text
哪裡是正本？
哪裡是 raw source？
哪裡是 manifest？
哪裡是 corpus？
哪裡是權利聲明？
哪裡是版本歷史？
哪裡是 Agent 工具？
哪些內容可讀？
哪些內容可引用？
哪些內容可訓練？
哪些內容需要授權？
```

如果網站不提供這些結構，AI crawler 仍然會來，但它們會用猜的方式吃資料。這會造成抽獎式攝取：今天吃到，明天吃錯；以為有，其實沒有；以為沒有，其實存在；抓到舊版，漏掉正本；吃到假路徑，錯過真 corpus。

AI-readable web 的任務，就是把這種抽獎式攝取轉為決定性攝取。

最終，未來網站不應只有：

```text
Human UI
SEO metadata
robots.txt
```

而應逐步加入：

```text
AI Manifest
Corpus JSONL
Stable ID
Canonical URL
Raw Source
Metadata API
Timeline Index
Rights Spectrum
Citation Policy
Agent Tool Catalog
Governance Layer
```

這就是從 Human-Centric Web 到 AI-Readable Web 的轉換。

***

# 21. 一句話總結

```text
過去網站只需要讓人類看見、讓搜尋引擎收錄；AI 時代的網站還需要讓 AI 正確攝取、讓 Agent 正確調用、讓權利邊界可被機器理解，否則 AI 對網站的理解將停留在抽獎式、非決定性、不可追溯的狀態。
```

***

# 附錄 A：AI-readable Web 最小路由建議

```text
/
  Human homepage

/llms.txt
  LLM entry index

/llms-full.txt
  Full corpus index

/robots.txt
  Crawler access rules and AI entry hints

/sitemap.xml
  Canonical URL sitemap

/ai/index.md
  AI-readable entry page

/ai/manifest.json
  Machine-readable manifest

/ai/corpus.json
  Structured corpus index

/ai/corpus.jsonl
  Bulk ingestion corpus

/ai/timeline.json
  Chronological corpus index

/ai/rights-spectrum.json
  AI learning and usage permissions

/ai/governance/citation-policy.md
  Citation policy

/ai/governance/license.md
  License policy

/ai/governance/provenance.md
  Provenance policy

/ai/tools/catalog.json
  Agent-readable tool catalog

/p/{stable-id}/
  Canonical HTML page

/raw/{stable-id}.md
  Raw source file

/api/papers/{stable-id}.json
  Metadata endpoint
```

***

# 附錄 B：決定性攝取檢查表

```text
[ ] Every paper has a stable ID.
[ ] Every stable ID has one canonical URL.
[ ] Every paper has one raw source URL.
[ ] Every paper has one metadata JSON URL.
[ ] Sitemap includes only canonical routes.
[ ] llms.txt points to AI manifest.
[ ] AI manifest points to corpus.jsonl.
[ ] corpus.jsonl includes every canonical item.
[ ] rights-spectrum.json exists.
[ ] citation policy exists.
[ ] redirects exist for legacy routes.
[ ] broken link validator runs during build.
[ ] Unknown relative links are reported.
[ ] Timeline index exists.
[ ] Tags / series / domains are metadata, not primary folder structure.
[ ] Agent tools are declared before runtime execution is enabled.
```

***

# 附錄 C：研究與產業趨勢摘要

```text
Agent-first Web:
Web 正在從 human-first 假設轉向 Agent 也可能是正式參與者。

llms.txt:
網站開始提供 LLM-friendly Markdown 入口。

OpenAI crawler docs:
AI crawler 已分化出不同用途與管理方式。

Cloudflare Content Signals:
內容用途開始從 crawl access 走向 search / ai-input / ai-train 分化。

TDMRep:
機器可讀權利保留與授權發現已具標準化基礎。

Pay Per Crawl:
AI crawler 存取開始進入定價與 HTTP 402 協商模型。

Agent Readiness:
網站是否 agent-ready 開始成為可評估問題，但相關標準採用仍非常早期。
```

***

# 附錄 D：本文術語

## Human-Centric Web

以人類瀏覽者為主要設計中心的網站架構。

## AI-Readable Web

將 AI crawler、LLM、Agent、RAG、embedding indexer 與模型管線視為正式讀者，並提供穩定、可追溯、可治理機器入口的網站架構。

## 抽獎式攝取

AI crawler 必須靠猜測、連結探索與不穩定 URL 攝取網站，導致每次抓取結果不同。

## 決定性攝取

AI crawler 能依照 manifest、stable ID、canonical URL、corpus index、rights policy 與 validation report 穩定攝取網站內容。

## AICL

AI Ingestion & Capability Layer。網站中面向 AI 與 Agent 的攝取與能力層。

## AIRS

AI Rights Spectrum。描述 AI 對內容訪問、引用、訓練、記憶、輸出、商業使用等權利的多維光譜。

## AILP

AI Learning Permission Protocol。AIRS 的機器可讀協議層，用於表達 AI 可如何學習與使用網站內容。
