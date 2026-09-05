# AI-Native Unified Search Intelligence (AUSI) Series — Paper 01

## AI 原生搜尋方法論：從人類資訊搜尋、計算機資訊檢索到自主搜尋智能

**English Title:** *AI-Native Search Methodology: From Human Information Seeking and Computational Retrieval to Autonomous Search Intelligence*

**Version:** v0.1  
**Date:** 2026-08-30  
**Status:** Canonical Draft / Series Foundation  
**Series:** AI-Native Unified Search Intelligence (AUSI)  
**Reference Implementation Direction:** `ai-web-research`

---

## 摘要

搜尋長期被分散理解為多種不同活動：在人類資訊行為研究中，它涉及需求形成、瀏覽、查詢修正、探索與理解；在傳統資訊檢索中，它通常被形式化為查詢、索引、相關性排序與文件回傳；在資料庫、圖搜尋、Web crawling 與 API retrieval 中，它又表現為不同的計算操作；進入大型語言模型與 Agent 時代後，搜尋進一步成為模型可調用的外部工具、知識補充機制與多步驟行動的一部分。然而，這些傳統仍缺少一個共同抽象：**搜尋本身能否被建模為 AI 可依任務自主選擇、組合、執行、驗證與停止的一組認知操作？**

本文提出 **AI-Native Search（AI 原生搜尋）** 的初步理論框架。其核心主張不是以大型語言模型取代既有搜尋引擎，也不是把 Retrieval-Augmented Generation、Web browsing 或 Agent tool use 重新命名為搜尋智能，而是將人類搜尋策略、傳統資訊檢索方法、資料庫與圖搜尋操作、Web/API retrieval，以及 AI 時代的動態規劃與工具使用，放入一個可組合的搜尋方法空間。AI 在此不只產生 query，也負責根據任務目標、資料來源、時間性、成本、風險、證據需求與其他約束，選擇適當的方法與來源，形成可觀察的搜尋軌跡。

本文區分 information seeking、search、retrieval、crawling、discovery、verification 與 research，並提出 AI 原生搜尋的七項最低條件：任務條件化、方法自覺、來源自覺、可組合性、迭代適應、證據可追溯與停止自覺。進一步地，本文提出「搜尋控制權遷移」觀點：資訊搜尋史可部分理解為搜尋規劃責任逐步由人類使用者外置給計算系統，再由固定檢索流程內化為可動態規劃的 AI 搜尋策略。此框架為後續的 Search Method Ontology、Search Planner、合法資料取得、Evidence Ledger、反證優先搜尋與 Search Receipt 等研究建立共同地基。

**關鍵詞：** AI-Native Search、Information Retrieval、Information Seeking、Search Agent、Agentic RAG、Search Planning、Tool Use、Evidence、Autonomous Research、Search Methodology

---

# 1. 問題背景

「搜尋」在人類與計算機歷史中從未只有一種形式。

研究者查閱書目、沿著引用鏈尋找前人研究、詢問專家、改變術語、從分類系統切換到關鍵詞搜尋，都是搜尋。資料庫中的 SQL query、搜尋引擎的倒排索引、圖結構中的 traversal、向量資料庫中的 nearest-neighbor retrieval、網站 crawler 的 frontier traversal，也都是某種搜尋或檢索操作。到了大型語言模型時代，模型可以產生搜尋詞、使用瀏覽器、呼叫搜尋 API、讀取搜尋結果、重新規劃下一步，再根據結果修正問題。

因此，當代問題已不再只是：

> 如何做出更好的搜尋引擎？

而逐漸轉變為：

> **如何讓 AI 知道在特定任務中應該如何搜尋？**

這兩個問題並不相同。

前者主要研究一個 retrieval system 如何對輸入 query 產生高品質結果；後者則要求一個 AI 系統處理更高階的決策：

1. 是否需要搜尋；
2. 要搜尋什麼；
3. 問題應如何分解；
4. 使用哪一種搜尋方法；
5. 向哪些資料來源搜尋；
6. 是否需要多個方法平行進行；
7. 如何根據中間結果修正下一步；
8. 如何區分找到的資訊與已驗證的證據；
9. 何時資料已經足夠；
10. 何時應因成本、時間、合法性或風險停止。

本文將這個問題稱為 **AI-Native Search Methodology**。

---

# 2. 既有研究不是空白，而是尚未完全統合

AI 原生搜尋並非從零開始。

## 2.1 人類資訊行為早已指出搜尋不是一次 query

Bates 的 berrypicking model 強調，真實資訊搜尋通常不是提出一個固定問題後一次取得完整答案。使用者的資訊需求、搜尋詞與下一步方向會隨著已取得的資訊不斷改變。換言之，搜尋是一個演化過程，而不是單次函數呼叫。

Marchionini 對 exploratory search 的討論又進一步區分「查到已知答案」與「透過搜尋學習、調查與理解」的差異。探索式搜尋中的 query、browse、comparison、sensemaking 與理解活動，本身就是較長的認知過程。

因此，人類資訊搜尋研究早已提供一項重要前提：

$$
Q_{t+1} \neq Q_t
$$

更精確地說：

$$
Q_{t+1}=f(Q_t,O_t,K_t,G_t)
$$

其中：

- $Q_t$ 為第 $t$ 輪查詢；
- $O_t$ 為上一輪觀察到的結果；
- $K_t$ 為搜尋者當時的知識狀態；
- $G_t$ 為當時的任務目標。

搜尋不是固定 query 的重複執行，而是知識狀態改變後的策略更新。

## 2.2 傳統資訊檢索建立了成熟的計算方法

資訊檢索研究則將文件表示、索引、query matching、ranking、relevance feedback、evaluation 等問題轉化為可計算問題。後來又發展出 probabilistic retrieval、language-model retrieval、learning to rank、dense retrieval、neural retrieval 等方法。

這些方法的重要貢獻不是「模擬人類搜尋」，而是將特定搜尋操作變成可重複、可衡量與可最佳化的計算程序。

因此可以粗略寫成：

$$
R = \operatorname{Retrieve}(Q,C,\theta)
$$

其中：

- $Q$ 是 query；
- $C$ 是 corpus；
- $\theta$ 是檢索模型、索引與排名參數；
- $R$ 是排序後的結果集合。

這個形式非常成功，但通常假設「要使用什麼檢索系統」以及「為何使用它」已由系統設計者或人類使用者預先決定。

## 2.3 RAG 將外部檢索接入生成模型

Retrieval-Augmented Generation 將非參數記憶與生成模型結合，使生成模型可以在推論時存取外部資料，而不必只依賴參數中的靜態知識。這讓 retrieval 從搜尋產品的一個獨立階段，進一步進入模型推論流程。

然而，早期 RAG 的典型抽象仍常接近：

$$
Q \rightarrow \operatorname{Retriever} \rightarrow D \rightarrow \operatorname{Generator}
$$

這裡最重要的進步是「模型可以利用外部檢索」，但 retrieval policy 本身未必已成為高度自主的決策問題。

## 2.4 WebGPT、ReAct 與 Toolformer 讓模型開始行動

WebGPT 顯示語言模型可以在瀏覽環境中提交 query、開啟結果、閱讀頁面並蒐集引用來源。

ReAct 將 reasoning 與 acting 交錯，使語言模型能根據推理產生外部動作，再利用環境回傳更新後續推理。

Toolformer 則進一步研究模型何時呼叫外部 API、選擇哪個工具、傳入什麼參數，以及如何整合工具輸出。

這些成果共同推動了一個重要轉變：

$$
\text{Model + Retrieval}
\rightarrow
\text{Model Choosing Actions}
$$

也就是搜尋開始不再只是固定 pipeline 中的一個元件，而逐漸成為 agent action space 的一部分。

## 2.5 Search Agent 與 Agentic RAG 已經形成研究方向

到 2025 年前後，Search Agent、LLM-based Deep Search Agent 與 Agentic RAG 已形成明確研究脈絡。近期 survey 已將動態規劃、多輪 retrieval、tool use、reflection、workflow adaptation 與 autonomous information seeking 視為重要研究方向。

因此，本文不主張「AI 自主多輪搜尋」本身是一項全新的發明。

本文提出的問題更窄也更基礎：

> **是否可以把分散於不同研究傳統中的搜尋方法，抽象成 AI 可理解其適用條件、可動態選擇、可組合、可驗證並可留下完整執行證據的統一方法空間？**

這是本文與單純 Search Agent 架構不同的研究焦點。

---

# 3. 七個需要區分的概念

如果「搜尋」被當成所有資訊取得活動的總稱，後續架構很容易混亂。因此本文先提出七個工作定義。

## 3.1 Information Seeking

**Information Seeking** 是最廣義的資訊需求滿足行為。

它可以包含：

- 搜尋；
- 詢問他人；
- 閱讀；
- 觀察；
- 實驗；
- 訂閱；
- 被動接收；
- 資料庫查詢；
- 專家諮詢；
- 其他資訊取得活動。

因此：

$$
\text{Search}\subseteq\text{Information Seeking}
$$

至少在本文的工作定義中如此。

## 3.2 Search

本文將 **Search** 定義為：

> 在存在未知、候選空間或不完整知識的條件下，透過一個或多個可選擇操作縮小、探索、重組或驗證資訊空間，以提高對任務相關狀態之認知的過程。

因此 Search 不必侷限於文字 query。

圖 traversal、分類法導航、citation chasing、source discovery、semantic retrieval、反證搜尋都可以是 Search Method。

## 3.3 Retrieval

**Retrieval** 是：

> 從既定資料集合或可查詢資料來源中，根據某個 query、條件或表示取回候選資訊項目的操作。

因此 retrieval 可以是 Search 的一個算子：

$$
M_{\text{retrieval}}\in\mathcal{M}_{\text{search}}
$$

但 Search 並不等於 Retrieval。

## 3.4 Crawling

**Crawling** 是對可連結或可發現資源空間進行系統性遍歷與取得。

Crawler 解決的是：

- 哪些 URL 尚未訪問；
- 如何發現下一個 URL；
- 是否允許取得；
- 何時重訪；
- 如何避免重複；
- 如何保存內容。

Crawler 可以提供 Search 的資料取得能力，但 crawler 本身並不等於研究策略。

## 3.5 Discovery

**Discovery** 指的是找出原先不在候選集合中的新來源、實體、術語、分類、關係或搜尋方向。

Search 可以包含 retrieval，也可以包含 discovery。

## 3.6 Verification

**Verification** 是對已取得資訊進行來源、內容、一致性、時效性、版本、引用或其他證據檢查。

因此：

$$
\text{Retrieved}(x)\not\Rightarrow\text{Verified}(x)
$$

找到資訊並不代表資訊已成立。

## 3.7 Research

本文將 **Research** 視為一種比單次 Search 更高階的任務流程：

$$
\text{Research}
=
\text{Search}
+
\text{Evaluation}
+
\text{Evidence}
+
\text{Synthesis}
+
\text{Iteration}
$$

在科學研究、經濟分析、氣象研究、專利檢索等領域，Search 是 research 的重要構成，但不能取代完整研究程序。

---

# 4. 從三代搜尋架構理解 AI-Native Search

本文提出一個簡化的三代模型。

## 4.1 第一代：Human-Orchestrated Search

在人類主導搜尋中，人類通常負責：

- 形成資訊需求；
- 選擇資料來源；
- 選擇搜尋方法；
- 產生 query；
- 評估結果；
- 改寫 query；
- 決定是否繼續；
- 綜合證據。

可以表示為：

$$
H
\rightarrow
\{M_i,P_j,Q_t\}
\rightarrow
O_t
\rightarrow
H
$$

其中 $H$ 是 human searcher， $M_i$ 是搜尋方法， $P_j$ 是資料來源或 provider， $O_t$ 是觀察結果。

計算機可以協助執行，但主要搜尋控制仍在人類。

## 4.2 第二代：Computer-Mediated Retrieval

搜尋引擎、資料庫與推薦系統大幅自動化：

- indexing；
- matching；
- ranking；
- query expansion；
- relevance estimation；
- result presentation。

但使用者通常仍決定：

- 任務是什麼；
- 使用哪個系統；
- 要輸入什麼；
- 是否接受結果；
- 下一輪如何改問。

因此，可理解為「執行層高度自動化，但 meta-search planning 多數仍在人類」。

## 4.3 第三代：AI-Native Search

AI-Native Search 將一部分原本屬於人類 meta-search 的決策移入 AI runtime。

AI 不只執行 retrieval，而可能處理：

$$
\begin{aligned}
&\text{Need Interpretation}\\
&\rightarrow \text{Task Decomposition}\\
&\rightarrow \text{Method Selection}\\
&\rightarrow \text{Source Selection}\\
&\rightarrow \text{Query Generation}\\
&\rightarrow \text{Acquisition}\\
&\rightarrow \text{Evidence Evaluation}\\
&\rightarrow \text{Replanning}\\
&\rightarrow \text{Stopping}
\end{aligned}
$$

關鍵並不是「無人類」。

關鍵是：

> **搜尋策略本身成為機器可以顯式操作的物件。**

---

# 5. 搜尋控制權遷移

為了更清楚描述上述差異，定義一個 Search Control Vector：

$$
\mathbf{C}
=
(c_n,c_m,c_s,c_q,c_e,c_r,c_v,c_\sigma)
$$

其中：

- $c_n$：need interpretation；
- $c_m$：method selection；
- $c_s$：source selection；
- $c_q$：query formulation；
- $c_e$：execution；
- $c_r$：reformulation；
- $c_v$：verification；
- $c_\sigma$：stopping decision。

每一維可表示該責任主要由 human、fixed software 或 adaptive AI 承擔的程度。

傳統 Web Search 並不是「低自動化」：它在 indexing、retrieval 與 ranking 上高度自動化；但 method selection、source ecology、problem decomposition 與 stopping 等較高階控制通常仍由人類負責。

AI-Native Search 的核心變化，是讓更多高階控制維度變成 runtime policy 的一部分。

本文稱之為：

> **Search Control Migration Principle**

其內容不是「AI 必然取代人類」，而是：

> 隨著資訊系統從固定 retrieval system 走向可調用工具的 adaptive agent，搜尋控制的可計算邊界逐步向上移動，原先由人類隱式完成的 meta-search 決策開始被顯式化、形式化並交由 AI 在約束內執行。

---

# 6. AI-Native Search 的形式化

定義一個搜尋任務：

$$
T=(G,D,C,B,F,R)
$$

其中：

- $G$：goal；
- $D$：domain；
- $C$：constraints；
- $B$：budget；
- $F$：freshness requirement；
- $R$：risk profile。

定義搜尋方法集合：

$$
\mathcal{M}=\{M_1,M_2,\ldots,M_n\}
$$

定義資料來源或 provider 集合：

$$
\mathcal{P}=\{P_1,P_2,\ldots,P_k\}
$$

定義第 $t$ 輪的證據狀態：

$$
E_t
$$

與搜尋歷史：

$$
H_t
$$

AI Search Policy 為：

$$
\pi:
(T,E_t,H_t,\mathcal{M},\mathcal{P})
\rightarrow
a_t
$$

其中 $a_t$ 不必只是 query，而可以是：

$$
a_t=
(M_i,P_j,\theta_t)
$$

 $\theta_t$ 表示方法參數，例如：

- query；
- filters；
- time window；
- language；
- depth；
- top- $k$ ；
- citation direction；
- classification node；
- semantic threshold；
- retry policy。

執行後得到：

$$
o_t=\operatorname{Execute}(a_t)
$$

再更新：

$$
(E_{t+1},H_{t+1})
=
U(E_t,H_t,a_t,o_t)
$$

因此完整搜尋不是一個函數，而是一條 trajectory：

$$
\tau=
(a_1,o_1,a_2,o_2,\ldots,a_n,o_n)
$$

最終：

$$
\operatorname{Stop}(T,E_n,H_n)=1
$$

時結束搜尋。

這個形式的價值在於：**query 只是 action 的一部分，而不是搜尋的全部。**

---

# 7. AI-Native Search 的七項最低條件

並非「LLM + Search API」就應被稱為 AI-Native Search。

本文提出七項最低判準。

## 7.1 Task-Conditioned

搜尋必須受任務目標影響。

同樣的主題，如果任務分別是：

- 找官方定義；
- 尋找反證；
- 尋找最新資料；
- 進行 prior-art search；
- 建立技術 landscape；

其合理 Search Plan 應不同。

因此：

$$
T_1\neq T_2
\Rightarrow
\pi(T_1)\not\equiv\pi(T_2)
$$

不要求每次結果都不同，但要求 policy 可以因任務差異而改變。

## 7.2 Method-Aware

AI 必須能區分不同 Search Method 的能力與限制，而不是把所有 retrieval provider 視為同一種工具。

例如 lexical search、semantic search、classification search、citation search 與 graph search 的失敗模式並不相同。

## 7.3 Source-Aware

AI 必須知道資料來源的性質。

至少包含：

- source type；
- authority；
- scope；
- freshness；
- accessibility；
- versioning；
- evidence value。

後續研究還必須加入授權、使用條款與自動化存取限制。

## 7.4 Composable

搜尋方法應可形成序列、分支與圖，而非只能單次呼叫。

例如：

$$
M_{\text{diverge}}
\rightarrow
\left\{
\begin{array}{l}
M_{\text{official}}\\
M_{\text{academic}}\\
M_{\text{general-web}}
\end{array}
\right.
\rightarrow
M_{\text{verify}}
$$

因此 Search Plan 更適合被表示成有向圖，而不只是 linear pipeline。

## 7.5 Iteratively Adaptive

系統應能根據中間結果更新後續方法。

$$
a_{t+1}
=
\pi(T,E_{t+1},H_{t+1})
$$

而不是在搜尋開始前產生一個永不改變的 query list。

## 7.6 Evidence-Preserving

搜尋輸出應保留：

- 來源；
- 取得時間；
- query / method；
- 版本；
- 原始證據位置；
- transformation history。

AI 可以摘要與壓縮，但不得讓結論失去可追溯來源。

## 7.7 Stop-Aware

自主搜尋若沒有停止條件，就可能變成無限制成本消耗。

定義某一步的預期邊際資訊價值：

$$
\Delta I_{t+1}
=
\mathbb{E}
[
I(E_{t+1})-I(E_t)
]
$$

若：

$$
\Delta I_{t+1}
<
\lambda_C C_{t+1}
+
\lambda_T T_{t+1}
+
\lambda_R R_{t+1}
$$

則系統可以考慮停止，其中右側表示額外成本、時間與風險的加權值。

實際系統不必精確計算資訊理論量，但需要等價的 stopping policy。

---

# 8. AI 原生搜尋不是單一搜尋引擎

一個重要工程推論是：

> Search Intelligence 不應等同於 Search Provider。

Google、Bing、Brave、學術資料庫、專利資料庫、GitHub、向量資料庫、本地 corpus 或自建 crawler，都可以是 provider。

形式上：

$$
\mathcal{P}
=
\{
P_{\text{web}},
P_{\text{academic}},
P_{\text{patent}},
P_{\text{code}},
P_{\text{local}},
P_{\text{database}},
\ldots
\}
$$

而搜尋方法則屬於另一個集合：

$$
\mathcal{M}
=
\{
M_{\text{exact}},
M_{\text{lexical}},
M_{\text{semantic}},
M_{\text{citation}},
M_{\text{graph}},
M_{\text{counter}},
\ldots
\}
$$

Method 與 Provider 不應被混為一談。

同一方法可能作用於多個 provider；同一 provider 也可能支援多種 method。

因此真正需要學習的是：

$$
(T,M_i,P_j,\theta)
$$

之間的適配關係，而不是學習「任何問題都呼叫同一個搜尋 API」。

---

# 9. 搜尋方法作為認知算子

本文提出後續系列最重要的抽象之一：

> **Search Method 可以被視為 AI 的外部認知算子。**

定義：

$$
M_i:
S_t
\rightarrow
S_{t+1}
$$

其中 $S_t$ 不只是資料狀態，也包含 AI 對問題的搜尋狀態。

不同方法改變狀態的方式不同：

- exact search：縮小字面候選；
- semantic search：跨越詞彙表面差異；
- citation chasing：沿學術關係圖擴張；
- classification search：沿人工知識分類探索；
- temporal search：限制或比較不同時間狀態；
- counter-evidence search：主動尋找與當前命題衝突的資訊；
- identity search：將多種表面表示折疊到同一實體；
- multilingual search：跨語言重新展開候選空間。

因此「搜尋方法庫」可以被理解為：

$$
\mathcal{M}
=
\text{External Epistemic Operator Library}
$$

這個觀點將在下一篇進一步發展為 Search Method Ontology。

---

# 10. 為何單一 query-centric 架構不足

典型搜尋介面通常假設：

$$
Q\rightarrow R
$$

即 query 對應 result。

但對複雜研究任務，更合理的形式是：

$$
T
\rightarrow
G_{\text{search}}
\rightarrow
\{Q_i,M_i,P_i\}_{i=1}^{n}
\rightarrow
E
$$

其中：

- $T$：完整任務；
- $G_{\text{search}}$：搜尋計畫圖；
- $Q_i$：局部 query；
- $M_i$：搜尋方法；
- $P_i$：資料來源；
- $E$：累積證據狀態。

這可以解釋為何「搜尋詞寫得更好」不足以解決所有研究問題。

某些失敗不是 query wording 的問題，而是：

- 搜錯資料來源；
- 用錯搜尋方法；
- 沒有做版本查找；
- 沒有沿引用追蹤；
- 沒有搜尋反證；
- 沒有跨語言；
- 沒有處理同一性；
- 沒有辨識資料缺口；
- 在不適當時間停止。

因此，需要從 Query Optimization 上升到 **Search Strategy Optimization**。

---

# 11. 從 Search Engine 到 Search Intelligence

本文提出四層區分。

## Level 0 — Retrieval Tool

輸入 query，回傳結果。

## Level 1 — Search-Augmented Model

模型可以呼叫 retrieval tool，再利用結果回答。

## Level 2 — Search Agent

模型可以多輪搜尋、瀏覽、修改 query、使用多個工具並重新規劃。

## Level 3 — Search Intelligence Runtime

搜尋方法、provider、來源條件、證據狀態、成本、停止規則被顯式建模；AI 可以依任務選擇與組合不同 Search Methods，並留下可檢查的 Search Plan 與 Search Receipt。

這個區分並不是成熟度排行榜。

Level 0 系統在特定任務可能比 Level 3 更快、更可靠、更便宜。

它描述的是**搜尋控制抽象層級**，而不是單純能力優劣。

---

# 12. Search Intelligence 與 Autonomous Research 的關係

自主研究系統通常需要：

1. task decomposition；
2. information acquisition；
3. evidence management；
4. hypothesis generation；
5. evaluation；
6. synthesis；
7. reporting。

AI-Native Search 主要負責第 2 項，並與第 1、3、5 項高度耦合。

因此：

$$
\text{AI-Native Search}
\neq
\text{Autonomous Research}
$$

但是：

$$
\text{High-quality Autonomous Research}
\Rightarrow
\text{requires a sufficiently capable Search Intelligence layer}
$$

至少對需要外部資料與可驗證證據的研究任務如此。

這也意味著搜尋層值得成為獨立基礎設施，而不是在每一個研究 Agent 中重新實作一次。

---

# 13. Evidence 不應被 Search Result 取代

傳統搜尋系統的核心輸出通常是 ranked results。

但研究型 AI 的核心輸出需要更接近：

$$
E=
\{
e_1,e_2,\ldots,e_n
\}
$$

每個 evidence object 至少應能追蹤：

$$
e_i=
(
\text{content},
\text{source},
\text{location},
\text{time},
\text{method},
\text{version},
\text{status}
)
$$

這裡的 status 可以進一步區分：

- retrieved；
- parsed；
- corroborated；
- contradicted；
- insufficient；
- stale；
- superseded；
- unverifiable。

因此：

$$
\text{Search Result}
\rightarrow
\text{Candidate Evidence}
\rightarrow
\text{Verified Evidence}
$$

是一個比「搜尋結果直接交給 LLM 摘要」更適合研究型系統的資料生命週期。

---

# 14. AI-Native Search 的失敗模式

將更多搜尋控制交給 AI 也會引入新的錯誤。

## 14.1 Method Collapse

AI 表面擁有多個工具，但幾乎所有問題都選擇同一搜尋方法。

## 14.2 Provider Collapse

AI 永遠依賴單一搜尋引擎或單一 API，使來源多樣性只是表面存在。

## 14.3 Query Loop

AI 不斷產生近義 query，實際資訊增量非常低。

## 14.4 Confirmation Loop

新 query 主要從既有結論衍生，導致越搜越支持原假設。

## 14.5 Retrieval–Evidence Conflation

系統把「搜到」誤認為「證實」。

## 14.6 Source Laundering

多個結果實際來自同一原始來源，但被錯誤計算成多個獨立證據。

## 14.7 Temporal Collapse

忽略資料發布時間、事件時間、修訂時間與 retrieval time 的差異。

## 14.8 Unbounded Search

沒有合理 stopping condition，使搜尋成本持續增加。

## 14.9 Hidden Strategy

最終只輸出答案，無法知道 AI 搜過哪些方向、遺漏哪些方向，以及為什麼停止。

因此 AI-Native Search 不只需要更大的 action space，也需要更強的 auditability。

---

# 15. Search Receipt：可觀察搜尋的必要性

本文先提出 Search Receipt 的概念，完整形式留待後續論文。

一次搜尋應至少可以重建：

$$
\mathcal{R}
=
(T,\tau,E_n,\Sigma)
$$

其中：

- $T$：原始任務；
- $\tau$：搜尋 trajectory；
- $E_n$：最終 evidence state；
- $\Sigma$：停止理由。

Search Receipt 不是自然語言思考鏈。

它不要求保存模型私人推理內容，而是保存**外部可觀察的搜尋決策與證據操作**，例如：

- 使用哪些 Search Methods；
- 呼叫哪些 providers；
- query 是什麼；
- 得到哪些 candidate；
- 哪些被拒絕；
- 哪些來源失敗；
- 哪些 evidence 被保留；
- 搜尋在哪些範圍沒有覆蓋；
- 為什麼停止。

因此可以同時兼顧：

- reproducibility；
- observability；
- auditability；
- privacy of internal reasoning。

---

# 16. 與當代 Agentic Search 研究的關係

本文與當代 Search Agent、Agentic RAG 研究高度相容，但研究問題並不完全重合。

Agentic Search 研究常關心：

- 如何讓 LLM 進行多輪 retrieval；
- 如何訓練 search policy；
- 如何使用 reasoning 與 reflection；
- 如何提升 benchmark performance；
- 如何規劃 browser actions；
- 如何使用多 Agent。

本文則希望建立一個更底層的統一表示：

$$
\text{Search Intelligence}
=
\text{Task}
+
\text{Methods}
+
\text{Providers}
+
\text{Constraints}
+
\text{Evidence}
+
\text{Policy}
+
\text{Receipt}
$$

其主要目的不是提出一個新的 LLM architecture，而是讓不同模型、Agent framework 與 provider 都能共享一套搜尋方法論抽象。

因此這個框架理論上可以：

- 被 LLM Agent 使用；
- 被 rule-based planner 使用；
- 被 hybrid planner 使用；
- 被 future AI architecture 使用。

AI-Native Search 不應被綁定於特定模型家族。

---

# 17. 研究命題

本文提出以下初步命題，後續需要實驗驗證。

## 命題 P1：方法顯式化命題

對複雜搜尋任務，若系統能顯式表示不同 Search Method 的適用條件與失敗模式，則其搜尋策略可比僅有 generic search tool 的系統更容易被規劃、驗證與審計。

## 命題 P2：方法組合命題

複雜研究任務的最佳搜尋策略通常不是單一方法，而是多個方法在不同階段的組合：

$$
\pi^*
\notin
\{M_i\}
$$

而更可能屬於：

$$
\pi^*
\in
\mathcal{G}(\mathcal{M})
$$

其中 $\mathcal{G}(\mathcal{M})$ 是由 Search Methods 形成的有效搜尋圖集合。

## 命題 P3：動態重規劃命題

當中間搜尋結果顯著改變知識狀態時，允許動態重規劃的系統在複雜探索任務上應優於完全固定的 precomputed query pipeline。

## 命題 P4：Evidence Separation 命題

將 retrieved information 與 verified evidence 顯式區分，可以降低研究型 AI 將來源品質、模型推論與外部事實混為一談的風險。

## 命題 P5：可觀察搜尋命題

Search Receipt 可以在不保存模型完整內部推理的情況下，提高搜尋過程的可重現性與可審計性。

---

# 18. 實驗方向

後續可建立一組跨領域 benchmark。

## 18.1 任務類型

至少包含：

- simple fact lookup；
- multi-hop fact verification；
- exploratory research；
- current-event search；
- academic literature search；
- technical troubleshooting；
- economic data retrieval；
- weather/climate data retrieval；
- patent prior-art discovery。

## 18.2 對照系統

可以比較：

### Baseline A
單一 search provider + fixed query。

### Baseline B
LLM query expansion + single provider。

### Baseline C
multi-tool Search Agent，但無 Method Registry。

### Proposed
Task Interpreter + Search Method Registry + Planner + multi-provider + evidence state + Search Receipt。

## 18.3 指標

不能只看 answer accuracy。

還應包含：

$$
\text{Coverage}
$$

$$
\text{Source Diversity}
$$

$$
\text{Evidence Precision}
$$

$$
\text{Contradiction Discovery Rate}
$$

$$
\text{Unsupported Claim Rate}
$$

$$
\text{Search Cost}
$$

$$
\text{Latency}
$$

$$
\text{Reproducibility}
$$

$$
\text{Method Diversity}
$$

$$
\text{Uncertainty Calibration}
$$

這些指標將使「搜尋智能」本身成為可評估研究對象。

---

# 19. 工程推論

本文雖是理論地基，但已能推出幾項工程要求。

未來 AI 搜尋 runtime 不應只提供：

```text
search(query) -> results
```

而需要至少逐步擴展為：

```text
interpret(task)
select_methods(task)
select_sources(task, methods)
plan(task, methods, sources)
execute(plan)
evaluate(observations)
replan(state)
verify(candidates)
stop(state)
emit_receipt()
```

其中 Search Method 與 Provider 必須分離。

因此 architecture 更接近：

```text
AI / Agent
    |
Task Interpreter
    |
Search Planner
    |
Search Method Registry
    |
Provider Router
    |
Acquisition
    |
Evidence Normalization
    |
Verification
    |
Search Receipt
```

這將成為後續技術白皮書的工程起點。

---

# 20. 對 `ai-web-research` 類專案的含義

如果一個專案最初從 crawler、Web retrieval 或單一 research workflow 開始，它仍可以逐步演化成 Search Intelligence Runtime，但前提是不能讓 crawler 或特定 search API 成為最高階抽象。

合理的長期分層應是：

$$
\text{Search Intelligence}
>
\text{Search Method}
>
\text{Provider}
>
\text{Transport / API}
$$

Crawler 是 capability。

Google Search API 是 capability。

學術資料庫 API 是 capability。

本地全文索引也是 capability。

真正的核心則是：

> **AI 如何根據任務選擇、組合與驗證這些 capability。**

因此，底層 provider 可以替換，而搜尋方法與研究策略不必一起被重寫。

---

# 21. 限制

本文仍有幾項重要限制。

第一，本文目前提出的是統一理論框架，尚未證明顯式 Search Method Ontology 一定能提高所有搜尋任務表現。

第二，不同方法之間的邊界可能高度重疊。例如 semantic search 可以被視為 retrieval algorithm，也可以被視為 search method。後續需要更精確 ontology，而不是假設分類天然唯一。

第三，搜尋品質不只由方法選擇決定。provider coverage、index freshness、資料授權、模型能力、ranking quality、tool reliability 都可能成為主要瓶頸。

第四，AI 自主選擇方法會產生新的安全與治理問題。某些來源技術上可取得，但未必允許 automated access、bulk acquisition、redistribution 或商業使用。本文僅將 constraint-aware 視為必要條件，完整的合法資料取得與 Source Rights Registry 將在後續專文處理。

第五，AI-Native Search 不等於 AI 能自行判斷真理。搜尋只能改善資訊取得與證據結構，最終 epistemic correctness 仍需要 verification、domain reasoning 與適當的人類或制度性審查。

---

# 22. 結論

搜尋正在經歷一次抽象層級的變化。

人類資訊行為研究已顯示，真實搜尋是一個會演化的探索過程；資訊檢索研究把大量搜尋操作轉化為成熟的計算方法；RAG 將 retrieval 帶入生成模型；WebGPT、ReAct、Toolformer 與後續 Search Agent 研究則讓模型開始自主選擇外部行動與多輪資訊取得。

下一個自然問題不只是讓 AI「會用搜尋引擎」，而是：

> **讓搜尋方法本身成為 AI 可以理解與操作的對象。**

本文因此提出 AI-Native Search 的初步框架：

$$
\boxed{
\text{Task}
\rightarrow
\text{Search Strategy}
\rightarrow
\text{Method Selection}
\rightarrow
\text{Provider Selection}
\rightarrow
\text{Acquisition}
\rightarrow
\text{Evidence}
\rightarrow
\text{Verification}
\rightarrow
\text{Replanning / Stop}
}
$$

其核心不是某一個搜尋模型、某一個 API 或某一個 Agent framework，而是建立一個統一搜尋方法空間，使歷史上分散在人類資訊行為、資訊檢索、資料庫、Web、圖結構、學術研究與專業搜尋中的方法，逐步變成 AI 可以調用的外部認知算子。

這使搜尋從：

$$
\text{query}\rightarrow\text{results}
$$

提升為：

$$
\text{task}\rightarrow\text{search intelligence}\rightarrow\text{evidence}
$$

而這正是後續 **Search Method Ontology、Search Planner、合法資料取得、Evidence Ledger、反證搜尋與 Search Receipt** 的共同理論起點。

---

# References

[1] Bates, M. J. (1989). *The Design of Browsing and Berrypicking Techniques for the Online Search Interface*. Online Review, 13(5), 407–424.

[2] Marchionini, G. (2006). *Exploratory Search: From Finding to Understanding*. Communications of the ACM, 49(4), 41–46. DOI: 10.1145/1121949.1121979.

[3] Lewis, P., Perez, E., Piktus, A., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems 33. arXiv:2005.11401.

[4] Nakano, R., Hilton, J., Balaji, S., et al. (2021/2022). *WebGPT: Browser-Assisted Question-Answering with Human Feedback*. arXiv:2112.09332.

[5] Yao, S., Zhao, J., Yu, D., et al. (2022/2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. International Conference on Learning Representations. arXiv:2210.03629.

[6] Schick, T., Dwivedi-Yu, J., Dessì, R., et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. Advances in Neural Information Processing Systems. arXiv:2302.04761.

[7] Mackie, I., Chatterjee, S., & Dalton, J. (2023). *Generative Relevance Feedback with Large Language Models*. Proceedings of SIGIR 2023. DOI: 10.1145/3539618.3591992.

[8] Gao, Y., Xiong, Y., Gao, X., et al. (2023/2024). *Retrieval-Augmented Generation for Large Language Models: A Survey*. arXiv:2312.10997.

[9] Su, H., Yen, H., Xia, M., et al. (2024). *BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval*. arXiv:2407.12883.

[10] Zhang, Y., Qiao, S., Zhang, J., et al. (2025). *A Survey of Large Language Model Empowered Agents for Recommendation and Search: Towards Next-Generation Information Retrieval*. arXiv:2503.05659.

[11] Singh, A., Ehtesham, A., Kumar, S., & Khoei, T. T. (2025). *Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG*. arXiv:2501.09136.

[12] Xi, Y., Lin, J., Xiao, Y., et al. (2025). *A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges*. arXiv:2508.05668.

---

# Series Continuation

**Paper 02 — 統一搜尋方法空間：Search Method Ontology 與可組合搜尋算子**

下一篇將把本文中的：

$$
\mathcal{M}
=
\{M_1,M_2,\ldots,M_n\}
$$

從抽象集合展開為正式方法規格，處理 Search Method 的 identity、capability、precondition、failure mode、composition rule、precision/recall bias、cost、evidence property 與 stopping implication，建立 AI 可實際調用的統一搜尋方法空間。
