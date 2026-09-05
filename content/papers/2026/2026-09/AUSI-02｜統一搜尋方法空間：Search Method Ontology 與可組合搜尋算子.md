# AI-Native Unified Search Intelligence (AUSI) Series — Paper 02

## 統一搜尋方法空間：Search Method Ontology 與可組合搜尋算子

**English Title:** *A Unified Search Method Space: Search Method Ontology and Composable Search Operators*

**Version:** v0.1  
**Date:** 2026-08-30  
**Status:** Canonical Draft  
**Series:** AI-Native Unified Search Intelligence (AUSI)  
**Predecessor:** Paper 01 — *AI 原生搜尋方法論：從人類資訊搜尋、計算機資訊檢索到自主搜尋智能*  
**Reference Implementation Direction:** `ai-web-research`

---

## 摘要

搜尋方法並非單一技術族。人類資訊搜尋研究已提出 search tactics、berrypicking、exploratory search 等策略模型；資訊檢索發展出 Boolean retrieval、relevance feedback、query expansion、learning-to-rank、dense retrieval 等方法；圖與文獻系統形成 citation searching、snowballing 與關係遍歷；分類與資訊架構形成 faceted search；分散式資訊檢索形成 federated search、resource selection 與 result merging；大型語言模型與 Search Agent 則開始動態產生 query、選擇工具並進行多輪 retrieval。問題在於：這些方法通常被分散於不同學科、不同工具與不同術語體系中，缺少一個可供 AI runtime 直接選擇與組合的共同表示。

本文提出 **Unified Search Method Space（統一搜尋方法空間）** 與 **Search Method Ontology（SMO）**。本文不把搜尋方法整理成一棵互斥分類樹，而是提出多軸、可重疊、可版本化的方法描述空間。每一個 Search Method 被表示為具備語義目的、輸入輸出契約、前置條件、作用方向、資料表示、來源需求、證據效應、成本特徵、失敗模式與組合規則的 typed operator。方法與 provider 被嚴格分離：方法描述「要做什麼搜尋操作」，provider 描述「在哪個系統、資料庫、API 或 corpus 上實現此操作」。

本文進一步提出一組 Search Plan Composition Calculus，包括序列、平行、多來源融合、條件式、迭代、映射與 guarded execution；並指出這些操作不是無條件的純代數，實際可組合性必須由型別相容、狀態前置條件、資料來源能力、授權與風險約束共同決定。本文最後提出 SearchMethodSpec、Method–Provider Compatibility、Method Identity、Search State 與 Search Receipt 的初步形式化，並以學術文獻搜尋、經濟數據搜尋、氣象資料搜尋與專利 prior-art search 說明統一方法空間如何支持跨領域 AI 自主搜尋。

**關鍵詞：** Search Method Ontology、AI-Native Search、Information Retrieval、Search Tactics、Faceted Search、Query Expansion、Citation Searching、Federated Search、Search Planning、Composable Operators、Agentic Search

---

# 1. 問題：搜尋法很多，但 AI 看見的往往只有「工具」

Paper 01 將 AI-Native Search 定義為：AI 不只送出 query，而是依據任務、來源、證據、成本與其他約束，選擇、組合、執行與停止搜尋程序。

這個定義立即產生第二個問題：

> **AI 究竟可以選擇哪些搜尋方法？**

今天的 Agent framework 常把搜尋能力呈現成工具清單：

```text
web_search
vector_search
database_query
browser
fetch_url
```

但這種工具層描述不足以回答下列問題：

- 「找官方最新數值」和「找所有可能反證」是不是同一種搜尋？
- keyword search 與 query expansion 是同一層概念嗎？
- citation searching 是 provider、retrieval algorithm，還是 graph traversal？
- faceted search 應被視為 UI、分類法導航，還是結構化查詢？
- federated search 是一個搜尋方法，還是一個 provider orchestration pattern？
- crawler 是搜尋方法、資料取得工具，還是 source discovery operator？
- semantic search 與 multilingual search 是否互斥？
- 一個方法能不能同時屬於多個類別？

若沒有明確表示，AI 最後仍可能退化成：

$$
\text{Task}
\rightarrow
\text{Generic Search Tool}
\rightarrow
\text{Results}
$$

即使工具數量很多，也不代表 AI 擁有真正的 search-method awareness。

因此本文提出：

$$
\boxed{
\text{Search Intelligence}
\text{ requires }
\text{an explicit Search Method Space}
}
$$

---

# 2. 搜尋方法研究早已存在，但分散在不同傳統

本文不是主張過去沒有搜尋方法論。恰恰相反，問題在於方法論過多且分散。

## 2.1 Human Search Tactics

Bates 在 1979 年提出 information search tactics，將「為推進搜尋而採取的一個 move」作為可研究單位，並整理出 monitoring、file structure、search formulation 與 term 等類型。

這件事對 AI-Native Search 很重要，因為它指出：

> 搜尋策略可以被拆成較小的可重用操作。

也就是說，人類專業搜尋者的行為不必只能被描述成模糊的「經驗」，其中一部分可以被操作化。

## 2.2 Search Intent Taxonomies

Broder 對 Web Search 的經典分類指出，Web query 背後的需求至少可包含 navigational、informational 與 transactional intent。

這證明：

$$
\text{Same Interface}
\not\Rightarrow
\text{Same Search Goal}
$$

即使都輸入文字 query，搜尋目的仍可能不同。

## 2.3 Query Expansion 與 Relevance Feedback

Query expansion 長期研究如何修改原始 query，以提高 retrieval effectiveness。方法可能利用 relevance feedback、pseudo-relevance feedback、corpus statistics、thesauri、ontologies、WordNet 或其他知識來源。

因此 query 本身不是不可變輸入，而可以是一個被方法轉換的搜尋狀態。

## 2.4 Faceted Search

Faceted search 將資料的多個 facet 與 taxonomy 用於 iterative refinement，使搜尋者能在多個分類維度間持續縮小或重組候選空間。

它顯示搜尋不一定要靠「加入更多文字關鍵詞」才能前進。

## 2.5 Citation Searching

Citation searching 利用文獻之間的 citation relation，形成 backward、forward、co-cited、co-citing 與 iterative citation searching 等方法。

這類方法尤其重要，因為它不是主要依靠語義相似度，而是利用顯式關係圖。

## 2.6 Federated Search

Federated search 長期處理多個獨立資料來源的 resource description、resource selection 與 result merging。

這表示「要去哪裡搜」本身就是一個需要最佳化的問題，而不只是 retrieval 之後的細節。

## 2.7 Agentic Search

近年的 Agentic RAG、Deep Search Agent 與 Search Agent 讓動態 retrieval、query generation、planning、reflection 與 tool use 進入 AI runtime。

這使統一 Search Method representation 變得更迫切：

> 當 AI 真正可以選擇行動時，系統必須知道每一種搜尋行動意味著什麼。

---

# 3. 為何不能只建立一棵 Search Method 分類樹

最直覺的方式是建立：

```text
Search
├── Keyword Search
├── Semantic Search
├── Graph Search
├── Citation Search
├── Faceted Search
└── ...
```

但這種分類很快產生問題。

例如 forward citation searching：

- 是 graph search；
- 是 relation traversal；
- 是 outward expansion；
- 是 literature search；
- 可以 iterative；
- 可能作為 supplementary search；
- 主要產生 candidate evidence。

它不應只能被塞入其中一格。

同樣地，multilingual semantic patent search 可能同時具有：

- semantic representation；
- cross-language transformation；
- domain-specific provider；
- high-recall orientation；
- classification-assisted narrowing；
- iterative evidence discovery。

因此本文採用：

> **Multi-Axial Search Method Ontology**

而不是 mutually exclusive taxonomy。

形式上，定義 Search Method Ontology 的方法描述空間：

$$
\Omega_M
=
\mathcal{G}
\times
\mathcal{R}
\times
\mathcal{D}
\times
\mathcal{I}
\times
\mathcal{S}
\times
\mathcal{E}
\times
\mathcal{\Phi}
$$

其中：

- $\mathcal{G}$：goal / epistemic effect；
- $\mathcal{R}$：representation / access structure；
- $\mathcal{D}$：search direction；
- $\mathcal{I}$：interaction / control mode；
- $\mathcal{S}$：source scope；
- $\mathcal{E}$：evidence effect；
- $\mathcal{\Phi}$：operational properties。

因為一個方法可能同時具有多個標籤，更精確可表示為：

$$
\operatorname{Profile}(M_i)
\in
2^{\mathcal{G}}
\times
2^{\mathcal{R}}
\times
2^{\mathcal{D}}
\times
2^{\mathcal{I}}
\times
2^{\mathcal{S}}
\times
2^{\mathcal{E}}
\times
\mathcal{\Phi}
$$

因此 Search Method 不是「屬於哪一類」的單選題，而是一個多維 capability profile。

---

# 4. 第一軸：Goal / Epistemic Effect

搜尋方法首先可以按其希望改變什麼來描述。

定義：

$$
\mathcal{G}
=
\{
g_{\text{locate}},
g_{\text{narrow}},
g_{\text{expand}},
g_{\text{discover}},
g_{\text{relate}},
g_{\text{verify}},
g_{\text{falsify}},
g_{\text{reconcile}},
g_{\text{monitor}}
\}
$$

## 4.1 Locate

找到已知或近似已知的實體、文件、值或位置。

例：

- DOI lookup；
- exact title search；
- patent publication number search；
- dataset series ID lookup。

## 4.2 Narrow

縮小候選集合。

例：

- Boolean filters；
- faceted filtering；
- date range；
- jurisdiction filter；
- field constraints。

## 4.3 Expand

增加候選、術語或來源空間。

例：

- query expansion；
- synonym expansion；
- citation snowballing；
- multilingual expansion。

## 4.4 Discover

尋找原本不知道存在的實體、來源、類別或關係。

Discovery 與 expansion 相近，但不完全相同：

$$
\text{Expand}
=
\text{increase candidate space}
$$

$$
\text{Discover}
=
\text{introduce previously unknown structures}
$$

## 4.5 Relate

尋找兩個或多個實體之間的關係。

例：

- knowledge graph traversal；
- patent family relation；
- citation relation；
- company–subsidiary relation。

## 4.6 Verify

確認候選資訊是否獲得足夠外部支持。

## 4.7 Falsify

主動尋找可以削弱、反駁或限制當前命題的資訊。

## 4.8 Reconcile

處理相互矛盾的版本、來源或數值。

## 4.9 Monitor

針對持續變化的來源進行重新搜尋、變更偵測或條件監控。

---

# 5. 第二軸：Representation / Access Structure

不同搜尋方法依賴不同資料表示。

定義：

$$
\mathcal{R}
=
\{
r_{\text{id}},
r_{\text{lexical}},
r_{\text{semantic}},
r_{\text{structured}},
r_{\text{taxonomy}},
r_{\text{graph}},
r_{\text{temporal}},
r_{\text{spatial}},
r_{\text{multimodal}}
\}
$$

## 5.1 Identifier / Exact

利用穩定 identifier 或完整字串。

例如 DOI、ISBN、patent number、URL、ticker、dataset ID。

它通常具有高 precision，但前提是 identifier 正確。

## 5.2 Lexical

利用 token、phrase、Boolean、BM25、倒排索引等字面訊號。

## 5.3 Semantic

利用 embedding、dense representation、semantic similarity 或其他語義表示。

## 5.4 Structured

利用欄位、schema、SQL、metadata、filter expressions 或 API parameters。

## 5.5 Taxonomy / Classification

利用分類法、facet、IPC/CPC、MeSH、subject heading 或其他 ontology/taxonomy。

## 5.6 Graph / Relation

利用 citation、entity relation、link graph、knowledge graph、dependency graph 等顯式邊。

## 5.7 Temporal

以 event time、publication time、revision time、validity interval 或 vintage 為主要結構。

## 5.8 Spatial

以地理位置、座標、區域或空間鄰近性為主要結構。

## 5.9 Multimodal

搜尋對象或 query 不只文字，例如圖像、聲音、程式結構、圖形表示或跨模態 embedding。

---

# 6. 第三軸：Search Direction

定義：

$$
\mathcal{D}
=
\{
d_{\text{inward}},
d_{\text{outward}},
d_{\text{forward}},
d_{\text{backward}},
d_{\text{lateral}},
d_{\text{cross-source}},
d_{\text{cross-language}},
d_{\text{cross-modal}}
\}
$$

其中：

- inward：縮小或聚焦；
- outward：擴張候選；
- forward：沿時間或有向關係向前；
- backward：回溯先前來源或前驅；
- lateral：尋找同級、替代或鄰接候選；
- cross-source：切換資料來源；
- cross-language：跨語言；
- cross-modal：跨表示模態。

方向不是物理方向，而是對 Search State 的結構變換。

---

# 7. 第四軸：Interaction / Control Mode

定義：

$$
\mathcal{I}
=
\{
i_{\text{one-shot}},
i_{\text{feedback}},
i_{\text{iterative}},
i_{\text{adaptive}},
i_{\text{continuous}}
\}
$$

## 7.1 One-shot

輸入一次，回傳一次。

## 7.2 Feedback

利用使用者或系統對結果的 relevance judgment 更新下一輪。

## 7.3 Iterative

固定方法可重複執行。

例如 iterative citation searching。

## 7.4 Adaptive

下一步方法本身可以改變：

$$
M_{t+1}
=
\pi(S_{t+1})
$$

## 7.5 Continuous

搜尋任務不以單次完成為終點，而是長期監控資料或條件變化。

---

# 8. 第五軸：Source Scope

定義：

$$
\mathcal{S}
=
\{
s_{\text{local}},
s_{\text{provider}},
s_{\text{domain}},
s_{\text{federated}},
s_{\text{open}},
s_{\text{private}}
\}
$$

其中：

- local：本地 corpus/index；
- provider：單一 provider；
- domain：特定專業領域資料源；
- federated：多個獨立來源；
- open：開放 Web 或未知來源空間；
- private：企業、個人或封閉資料源。

Source scope 與 representation 必須分開。

同一個 lexical search 可以作用於：

- local Lucene index；
- patent database；
- Web search engine；
- internal document repository。

---

# 9. 第六軸：Evidence Effect

搜尋方法不是都產生相同證據。

定義：

$$
\mathcal{E}
=
\{
e_{\text{candidate}},
e_{\text{metadata}},
e_{\text{primary}},
e_{\text{secondary}},
e_{\text{relation}},
e_{\text{corroboration}},
e_{\text{contradiction}},
e_{\text{version}}
\}
$$

例如：

- semantic search 通常產生 candidate；
- official API retrieval 可能取得 primary data；
- citation graph traversal 主要產生 relation + candidate；
- cross-source verification 主要增加 corroboration；
- counter-evidence search 主要尋找 contradiction；
- archival/vintage search 主要提供 version evidence。

這使 AI 可以知道：

> 「我現在缺的是候選，不是更多確認。」

或：

> 「我已經找到候選，但沒有 primary source。」

---

# 10. 第七軸：Operational Properties

前六軸主要描述語義，第七軸描述執行屬性。

定義方法 operational profile：

$$
\Phi(M_i)
=
(
p_i,
r_i,
c_i,
l_i,
f_i,
u_i,
x_i
)
$$

其中：

- $p_i$：precision tendency；
- $r_i$：recall tendency；
- $c_i$：cost；
- $l_i$：latency；
- $f_i$：freshness sensitivity；
- $u_i$：uncertainty / expected failure；
- $x_i$：external constraints。

這些值不一定是固定常數，而可以是 context-dependent estimator：

$$
c_i=c(M_i,T,P,S_t)
$$

---

# 11. Search Method 的正式定義

本文將 Search Method 定義為：

> 對 Search State 執行具有穩定語義目的、明確輸入輸出契約與可描述失敗模式之資訊空間操作。

定義 Search State：

$$
S_t
=
(
T,
X_t,
C_t,
E_t,
U_t,
B_t,
H_t
)
$$

其中：

- $T$：task；
- $X_t$：當前 query、seed、identifier、filter 等搜尋表示；
- $C_t$：candidate set；
- $E_t$：evidence state；
- $U_t$：uncertainty / uncovered regions；
- $B_t$：remaining budget；
- $H_t$：observable search history。

Search Method $M_i$ 在參數 $\theta_i$ 下的抽象作用為：

$$
M_i:
(S_t,\theta_i)
\rightarrow
(\Delta S_i,O_i)
$$

其中：

- $\Delta S_i$：預期 Search State effect；
- $O_i$：方法所要求的可觀察輸出型別。

實際 provider 執行則為：

$$
o_t
=
\operatorname{Execute}
(
P_j,
M_i,
S_t,
\theta_i
)
$$

再由狀態更新器：

$$
S_{t+1}
=
U(S_t,M_i,P_j,\theta_i,o_t)
$$

這使 Method semantics 與 Provider implementation 分離。

---

# 12. SearchMethodSpec

任何可被 AI Planner 使用的方法，至少應具有一個 machine-readable specification。

建議最小結構：

```text
SearchMethodSpec
├── method_id
├── version
├── aliases
├── purpose
├── method_profile
├── input_contract
├── output_contract
├── preconditions
├── postconditions
├── parameter_schema
├── required_provider_capabilities
├── evidence_profile
├── precision_recall_bias
├── cost_model
├── latency_model
├── freshness_profile
├── failure_modes
├── composition_rules
├── policy_constraints
├── receipt_requirements
└── stopping_implications
```

其中最重要的不是 method name，而是其 semantic contract。

---

# 13. Method Identity：名稱不是方法本身

不同領域可能用不同名字描述相近方法。

例如：

- snowballing；
- citation chasing；
- citation tracking；
- pearl growing；
- reference checking。

它們可能部分重疊，但不能僅靠名稱判斷等價。

因此定義 Semantic Method Signature：

$$
\operatorname{Sig}(M)
=
(
G_M,
R_M,
D_M,
I_M,
\operatorname{In}_M,
\operatorname{Out}_M,
E_M,
F_M
)
$$

其中 $F_M$ 為核心 state-transition semantics / failure semantics。

若兩個 implementation 的核心 signature 在定義的容忍範圍內一致，則可稱：

$$
M_a
\equiv_{\text{method}}
M_b
$$

但：

$$
M_a
\equiv_{\text{method}}
M_b
\not\Rightarrow
P_a
\equiv
P_b
$$

即使方法相同，不同 provider 的 coverage、ranking、freshness 與法律條件仍可能不同。

---

# 14. Method 與 Provider 的嚴格分離

這是本文最重要的工程邊界之一。

## 14.1 Method

描述：

> **要執行什麼搜尋行為？**

例如：

- exact identifier lookup；
- lexical high-recall search；
- semantic expansion；
- backward citation search；
- classification narrowing；
- version search；
- counter-evidence search。

## 14.2 Provider

描述：

> **哪個外部或內部系統能提供這種能力？**

例如：

- general web search engine；
- OpenAlex；
- Crossref；
- EPO OPS；
- USPTO；
- local vector index；
- SQL database；
- crawler；
- enterprise search service。

Provider 宣告 capability set：

$$
\operatorname{Cap}(P_j)
$$

Method 宣告 requirements：

$$
\operatorname{Req}(M_i)
$$

基本 capability compatibility 為：

$$
P_j\models M_i
\iff
\operatorname{Req}(M_i)
\subseteq
\operatorname{Cap}(P_j)
$$

但這仍不代表可以執行。

還需要：

$$
\operatorname{Allowed}(M_i,P_j,T,S_t)=1
$$

其中 Allowed 可以包含：

- authentication；
- rate limit；
- license；
- automation permission；
- privacy；
- jurisdiction；
- budget；
- organizational policy。

因此：

$$
\boxed{
\text{Compatible}
\neq
\text{Permitted}
}
$$

---

# 15. Search Operator Families

下面列出第一版 method families。它不是互斥 taxonomy，而是 Registry 的常用 operator templates。

## 15.1 Exact / Identifier Operators

例：

- exact string；
- DOI；
- patent number；
- ticker；
- dataset identifier；
- checksum lookup。

主要 profile：

$$
g_{\text{locate}}
+
r_{\text{id}}
+
d_{\text{inward}}
$$

## 15.2 Lexical / Boolean Operators

例：

- keyword；
- phrase；
- Boolean AND/OR/NOT；
- proximity；
- BM25。

## 15.3 Query Transformation Operators

例：

- synonym expansion；
- relevance feedback；
- pseudo-relevance feedback；
- ontology expansion；
- spelling variation；
- term translation；
- query decomposition。

這類 operator 不一定直接取得文件。

它可以：

$$
X_t
\rightarrow
X_{t+1}
$$

也就是修改 Search State 的 query representation。

## 15.4 Semantic Operators

例：

- embedding similarity；
- dense retrieval；
- semantic reranking；
- concept-based matching。

## 15.5 Structured / Fielded Operators

例：

- SQL；
- field search；
- metadata filters；
- numerical range；
- API parameterized query。

## 15.6 Facet / Classification Operators

例：

- faceted refinement；
- taxonomy traversal；
- IPC/CPC；
- MeSH；
- subject headings。

## 15.7 Graph / Relation Operators

例：

- neighbor expansion；
- path search；
- entity relation traversal；
- link graph；
- dependency traversal。

## 15.8 Citation Operators

例：

- backward citation；
- forward citation；
- co-citation；
- co-citing；
- iterative citation search。

Citation operators 可視為 graph family 的專業化，但保留獨立 family，因其 evidence semantics 與 domain conventions 足夠重要。

## 15.9 Federated / Meta-Search Operators

例：

- provider selection；
- source routing；
- parallel querying；
- result merging；
- rank fusion。

這類方法的作用對象不是只有文件，而可能是 provider set：

$$
\mathcal{P}
\rightarrow
\mathcal{P}'
$$

## 15.10 Crawl / Discovery Operators

例：

- link traversal；
- sitemap discovery；
- domain-scoped BFS；
- frontier expansion；
- structured endpoint discovery。

Crawler 不等於 research strategy，但 crawl 可以是 Search Plan 中的 discovery/acquisition operator。

## 15.11 Temporal / Version Operators

例：

- latest version；
- historical snapshot；
- revision chain；
- publication-before-date；
- vintage data；
- change detection。

## 15.12 Cross-Language / Cross-Modal Operators

例：

- multilingual query expansion；
- machine-translated search；
- cross-lingual embeddings；
- text-to-image retrieval；
- code-to-document search。

## 15.13 Coverage / Diversification Operators

目的不是提高單一結果 score，而是改善候選空間的 coverage。

例：

- source diversification；
- perspective diversification；
- entity coverage；
- jurisdiction coverage；
- time-period coverage。

## 15.14 Verification / Counter-Evidence Operators

例：

- primary-source resolution；
- independent corroboration；
- contradiction search；
- claim verification；
- source independence check。

## 15.15 Monitoring Operators

例：

- scheduled re-query；
- conditional change watch；
- new-citation monitor；
- patent legal-status watch；
- dataset revision watch。

---

# 16. Search Plan Composition Calculus

單一方法不足以描述複雜研究，因此需要 composition。

本文先提出七種基礎 composition construct。

## 16.1 Sequential Composition

$$
M_a
\triangleright
M_b
$$

表示先執行 $M_a$，其結果進入 $M_b$。

只有當：

$$
\operatorname{CompatOutIn}(M_a,M_b)=1
$$

時才可直接組合。

例如：

$$
M_{\text{query-expand}}
\triangleright
M_{\text{lexical-retrieve}}
$$

## 16.2 Parallel Composition

$$
M_a
\parallel
M_b
$$

表示在同一 Search State 或等價 snapshot 上平行執行。

例如：

$$
M_{\text{lexical}}
\parallel
M_{\text{semantic}}
$$

目的是降低單一表示的 blind spot。

## 16.3 Fusion

$$
M_a
\oplus
M_b
$$

表示對多個候選或 evidence stream 做 deduplication、normalization、rank fusion 或 evidence union。

Fusion 本身也是 method，而不是「自然發生的合併」。

## 16.4 Conditional Composition

$$
M_a
\xrightarrow{\gamma}
M_b
$$

表示在 guard $\gamma$ 成立時才執行 $M_b$。

例如：

$$
M_{\text{official-lookup}}
\xrightarrow{\text{missing}}
M_{\text{open-web-discovery}}
$$

## 16.5 Iterative Composition

$$
M^{*}_{\sigma}
$$

表示重複 $M$ 直到 stopping predicate $\sigma$ 成立。

例如 iterative citation searching：

$$
M_{\text{citation}}^{*}_{\text{no-new-eligible}}
$$

## 16.6 Map Composition

$$
\operatorname{Map}(M,\{x_1,\ldots,x_n\})
$$

表示對多個 seed、entity、jurisdiction、language 或 provider 分別執行同一方法。

## 16.7 Guarded Execution

$$
\operatorname{Guard}(\lambda,M)
$$

其中 $\lambda$ 不是搜尋成功條件，而是 policy / legality / resource constraint。

例如：

$$
\lambda=
\text{API access permitted}
\land
\text{budget available}
$$

---

# 17. 為何這不是普通的純代數

Search Operator composition 不能假設一般數學函數的所有性質。

例如：

$$
(M_a\triangleright M_b)\triangleright M_c
$$

與：

$$
M_a\triangleright(M_b\triangleright M_c)
$$

在 stateful search 中不一定等價。

原因可能包括：

- provider ranking 隨時間變化；
- API quota；
- intermediate deduplication；
- adaptive query generation；
- evidence state 改變；
- stochastic retrieval；
- rate limiting；
- external world change。

因此本文使用「Composition Calculus」而不是宣稱完整 algebraic structure。

每個 rewrite rule 都必須在明確前提下成立。

---

# 18. 搜尋方法的前置條件與失敗模式

AI 要會選方法，就必須知道方法何時失敗。

定義：

$$
\operatorname{Pre}(M_i,S_t)
$$

與：

$$
\operatorname{Fail}(M_i)
=
\{f_1,\ldots,f_n\}
$$

例如 exact identifier search 的失敗模式包括：

- identifier 不存在；
- identifier 格式錯誤；
- provider 不收錄；
- identifier 已 superseded。

Semantic search 的失敗模式包括：

- embedding domain mismatch；
- false semantic neighborhood；
- index stale；
- high similarity but wrong relation。

Citation searching 的失敗模式包括：

- seed 本身選錯；
- citation graph coverage 不完整；
- field citation culture bias；
- recent work 尚未累積 citation；
- iterative expansion 爆炸。

Query expansion 的失敗模式包括 query drift。

Federated search 的失敗模式包括 resource selection error 與 result-merging distortion。

因此一個 method registry 若只有：

```text
name
description
```

是不足的。

Planner 需要看到 failure semantics。

---

# 19. Precision / Recall 不應被當成方法的固定標籤

可以說某方法通常「偏 precision」或「偏 recall」，但不應視為固定常數。

定義：

$$
\operatorname{PRBias}(M,T,P,S_t)
$$

例如：

- exact identifier lookup 通常 precision 很高；
- broad synonym expansion 通常提高 recall，但可能降低 precision；
- classification search 在某些專業資料庫可能同時提高 precision 與 recall；
- semantic search 是否提高 recall 取決於 embedding 與 corpus；
- citation searching 對難以文字描述的主題可能具有高增益，但不代表所有主題都如此。

因此 Planner 不應把 heuristics 當成 universals。

---

# 20. Search Method 的可學習性

SearchMethodSpec 提供的是顯式先驗。

實際使用後，系統還可以學習：

$$
P(
\text{success}
\mid
M_i,T,P_j,S_t
)
$$

以及：

$$
\mathbb{E}
[
\Delta I
\mid
M_i,T,P_j,S_t
]
$$

其中 $\Delta I$ 可代表資訊增益、coverage gain、evidence gain 或 uncertainty reduction。

因此 Search Method Registry 不應只是靜態字典，而可以逐步加入 empirical profile：

```text
method prior
+
provider performance
+
task history
+
domain history
=
adaptive method estimate
```

這將在 Paper 07 的 Search Receipt 與搜尋經驗學習中完整處理。

---

# 21. Composition Example A：學術文獻搜尋

假設任務是：

> 尋找某一跨領域研究問題的主要方法、反對證據與近年進展。

一個可能 Search Plan：

$$
M_{\text{term-diverge}}
\triangleright
(
M_{\text{lexical}}
\parallel
M_{\text{semantic}}
)
\triangleright
M_{\text{dedup}}
\triangleright
M_{\text{seed-select}}
$$

接著：

$$
\operatorname{Map}
(
M_{\text{backward-citation}}
\parallel
M_{\text{forward-citation}},
\text{Seeds}
)
$$

再：

$$
M_{\text{coverage-check}}
\triangleright
M_{\text{counter-evidence}}
\triangleright
M_{\text{primary-source-resolve}}
$$

這裡至少同時使用：

- query transformation；
- lexical retrieval；
- semantic retrieval；
- citation graph traversal；
- coverage assessment；
- counter-evidence；
- verification。

若只把它描述成「用了 Google Scholar」，大量方法資訊都會消失。

---

# 22. Composition Example B：經濟數據搜尋

任務：

> 取得某國某經濟指標的最新數值，並確認歷史 revision。

可以使用：

$$
M_{\text{indicator-id}}
\triangleright
M_{\text{official-provider-select}}
\triangleright
M_{\text{structured-api}}
$$

接著：

$$
M_{\text{vintage-search}}
\parallel
M_{\text{metadata-verify}}
$$

最後：

$$
M_{\text{version-reconcile}}
\triangleright
M_{\text{provenance-record}}
$$

這與一般 Web Search 完全不同。

主要 method axes 是：

- identifier；
- structured；
- temporal/version；
- official-source；
- verification。

---

# 23. Composition Example C：氣象與氣候資料

任務：

> 查詢指定地點與時間區間的觀測資料，並確認 station / dataset metadata。

一個可能流程：

$$
M_{\text{spatial-resolve}}
\triangleright
M_{\text{station-discovery}}
\triangleright
M_{\text{temporal-filter}}
\triangleright
M_{\text{structured-retrieval}}
$$

再：

$$
M_{\text{metadata-validation}}
\parallel
M_{\text{missingness-check}}
$$

必要時：

$$
M_{\text{alternate-station}}
\oplus
M_{\text{alternate-dataset}}
$$

因此「搜尋」在科學資料情境中常表現為 structured + spatial + temporal + verification operators。

---

# 24. Composition Example D：Patent Prior-Art Search

任務：

> 對一個軟體功能進行初步 prior-art discovery。

Search Plan 可能包含：

$$
M_{\text{feature-term-expand}}
\parallel
M_{\text{classification-expand}}
\parallel
M_{\text{semantic-search}}
$$

然後：

$$
M_{\text{candidate-fusion}}
\triangleright
M_{\text{family-resolve}}
\triangleright
M_{\text{priority-date}}
$$

再對主要 seed：

$$
M_{\text{backward-citation}}
\parallel
M_{\text{forward-citation}}
$$

並加入：

$$
M_{\text{multilingual}}
\parallel
M_{\text{counter-path}}
$$

最後：

$$
M_{\text{claim-oriented-filter}}
\triangleright
M_{\text{coverage-report}}
$$

這說明專利搜尋不是「一個更強的 keyword search」，而是多個 Search Method 的專業組合。

---

# 25. Search Method 與 Domain Pack

通用 Registry 不代表所有領域都使用相同方法優先級。

本文提出：

$$
\mathcal{M}_{\text{global}}
$$

作為通用方法空間。

每個 domain 定義：

$$
D_k
=
(
\mathcal{M}_k,
\mathcal{P}_k,
\mathcal{C}_k,
\mathcal{V}_k
)
$$

其中：

- $\mathcal{M}_k$：推薦/專用方法；
- $\mathcal{P}_k$：專業 providers；
- $\mathcal{C}_k$：domain constraints；
- $\mathcal{V}_k$：domain-specific validation rules。

例如：

```text
Economic Domain Pack
Meteorological Domain Pack
Patent Intelligence Domain Pack
Academic Literature Domain Pack
Standards / Regulation Domain Pack
```

Domain Pack 是 Search Intelligence 上的專業化，而不是重新建立一套搜尋引擎。

---

# 26. Ontology 不應與實作綁死

Search Method Ontology 的生命週期應長於特定 API。

因此：

$$
\operatorname{Lifetime}(\text{MethodSpec})
>
\operatorname{Lifetime}(\text{ProviderAdapter})
$$

應是一個工程目標，而不是形式定理。

Google API 可以改版。

某個向量資料庫可以被替換。

某個 patent API 可以停止。

但：

- backward citation search；
- classification search；
- version search；
- counter-evidence search；

這些方法概念仍存在。

因此系統架構不應：

```text
GoogleSearchMethod
EPO_Search_Method
LocalVectorMethod
```

而應：

```text
Method
    ↓
Capability Requirement
    ↓
Provider Resolver
    ↓
Provider Adapter
```

---

# 27. Search Method Registry 的最小查詢能力

AI Planner 至少應能問 Registry：

```text
methods_for(goal)
methods_for(domain)
methods_accepting(input_type)
methods_producing(evidence_type)
methods_supported_by(provider)
methods_within(cost_budget)
methods_allowed(policy)
methods_composable_after(previous_method)
methods_good_for(coverage_gap)
methods_good_for(counter_evidence)
```

因此 Registry 不是單純 plugin list。

它是一個可被 planner 查詢的 capability graph。

形式上：

$$
\mathcal{R}_M
=
(
V_M,
E_{\text{compat}},
E_{\text{specialize}},
E_{\text{compose}},
E_{\text{alternative}}
)
$$

其中 method 本身也可形成 graph。

---

# 28. Planner 如何使用 Method Ontology

Paper 03 將完整研究 Search Planner；本文先給出最小介面。

給定 task：

$$
T
$$

Search State：

$$
S_t
$$

候選方法：

$$
\mathcal{M}'_t
=
\{
M_i
\in
\mathcal{M}
\mid
\operatorname{Pre}(M_i,S_t)=1
\}
$$

再加入 provider 與 policy 約束：

$$
\mathcal{A}_t
=
\{
(M_i,P_j)
\mid
M_i\in\mathcal{M}'_t,
P_j\models M_i,
\operatorname{Allowed}(M_i,P_j,T,S_t)=1
\}
$$

Planner 才在 $\mathcal{A}_t$ 中選擇行動：

$$
a_t^*
=
\arg\max_{(M_i,P_j)\in\mathcal{A}_t}
U(M_i,P_j,T,S_t)
$$

其中 utility $U$ 可以綜合：

- expected coverage；
- expected evidence gain；
- uncertainty reduction；
- freshness；
- source authority；
- cost；
- latency；
- risk。

這就是 Method Ontology 與自主搜尋規劃之間的接口。

---

# 29. Search Method Ontology 的核心不變量

本文提出七個初步 invariant。

## I1 — Method–Provider Separation

$$
M\neq P
$$

## I2 — Search Result–Evidence Separation

$$
R_{\text{search}}
\neq
E_{\text{verified}}
$$

## I3 — Multi-Axial Identity

方法不能只由單一 category 決定。

## I4 — Explicit Preconditions

任何可自動調用方法都必須有可檢查前置條件。

## I5 — Observable External Effects

方法執行必須能留下 Search Receipt 所需的外部操作記錄。

## I6 — Policy-Bounded Execution

技術能力不能覆蓋合法、授權、隱私與風險約束。

## I7 — Versioned Semantics

SearchMethodSpec 必須版本化，避免同名方法在行為改變後仍被視為同一契約。

---

# 30. 失敗模式：Method Ontology 本身也可能失敗

## 30.1 Taxonomy Capture

把多軸 ontology 又實作成僵硬單繼承樹。

## 30.2 Name Proliferation

每出現一個工具就新增一個 method，最後 Registry 只是 API 名單。

## 30.3 Over-Abstraction

把所有方法抽象成：

```text
transform(input) -> output
```

導致 planner 看不出差異。

## 30.4 Under-Abstraction

每個 provider implementation 都成為獨立方法，無法跨 provider reuse。

## 30.5 False Equivalence

因輸入輸出格式相同，就誤認為兩種方法語義相同。

## 30.6 Hidden Composition

實際 pipeline 中進行 query expansion、reranking、deduplication，但 Receipt 與 Planner 不知道。

## 30.7 Ontology Stagnation

方法空間被當成一次性標準，不能新增新方法或修訂 failure semantics。

因此 Search Method Ontology 必須是：

> **open-world、versioned、machine-readable、empirically revisable。**

---

# 31. 與既有研究的差異

本文的貢獻不是取代既有 taxonomy。

Bates 研究 human search tactics。

Broder 研究 Web search intent。

Query expansion 文獻研究 query reformulation。

Faceted search 研究 classification-based navigation。

Citation-searching 方法學研究 relation-based supplementary searching。

Federated search 研究 distributed resources 的 selection 與 merging。

Agentic RAG / Search Agent 研究動態 retrieval 與 agent planning。

本文提出的是它們上方的一個 runtime abstraction：

$$
\boxed{
\text{How can heterogeneous search methods be represented
as AI-selectable and AI-composable operators?}
}
$$

因此 Search Method Ontology 是一個 **meta-method representation layer**。

---

# 32. 初步研究命題

## 命題 P2.1 — Multi-Axial Representation Hypothesis

相較於互斥分類樹，多軸方法 profile 更適合表示具有多重搜尋性質的方法，並能減少 duplicate method definitions。

## 命題 P2.2 — Explicit Failure Semantics Hypothesis

若 Planner 可以存取 Search Method 的 preconditions 與 failure modes，其方法選擇應比僅存取自然語言 tool description 更容易避免不適用方法。

## 命題 P2.3 — Provider Independence Hypothesis

將 Method 與 Provider 分離，可以提高 provider substitution 與 cross-provider plan reuse。

## 命題 P2.4 — Typed Composition Hypothesis

將 Search Plan 限制在 type-compatible 與 policy-valid 的 method composition，可降低無效工具序列與不可執行搜尋計畫。

## 命題 P2.5 — Evidence-Effect Hypothesis

如果每個 Method 明確標記其主要 evidence effect，Planner 可以更有效區分「增加候選」與「提高證據強度」兩類行動。

---

# 33. 實驗設計

可建立 Method-Aware Search Planning benchmark。

## 33.1 任務集

跨領域包含：

- exact fact；
- broad exploratory；
- current data；
- historical version；
- literature survey；
- contradiction discovery；
- patent prior art；
- structured scientific data；
- multi-provider search。

## 33.2 Baselines

### B0 — Single Tool

只有 generic `search()`。

### B1 — Multi-Tool

有多個 provider/tool description，但無 Method Ontology。

### B2 — Flat Method Registry

方法有名稱與說明，但無 typed spec。

### Proposed — Multi-Axial Typed Registry

Method Profile + preconditions + evidence effect + composition + provider mapping。

## 33.3 評估指標

$$
\text{Plan Validity Rate}
$$

$$
\text{Method Selection Accuracy}
$$

$$
\text{Provider Substitution Success}
$$

$$
\text{Coverage Gain}
$$

$$
\text{Evidence Gain}
$$

$$
\text{Invalid Composition Rate}
$$

$$
\text{Method Collapse Rate}
$$

$$
\text{Cost per Verified Finding}
$$

---

# 34. 工程落地：第一個真正該寫的核心

若將本文轉為 reference implementation，第一輪不應先接更多 Search API，而應先完成：

```text
search_methods/
    spec.py
    registry.py
    profiles.py
    compatibility.py
    composition.py

providers/
    base.py
    registry.py

planning/
    state.py
    plan.py
    validators.py
```

並先建立少量 canonical methods：

```text
exact_lookup
lexical_search
query_expansion
semantic_search
structured_filter
classification_search
backward_citation
forward_citation
federated_search
crawl_discovery
temporal_version_search
counter_evidence_search
```

現有 crawler、identity search、DRC divergence、MCP tools 與未來 Google/其他 Search API 都應逐步掛到此能力層，而不是反過來成為 architecture root。

---

# 35. 限制

第一，本文提出的是 ontology framework，而不是宣稱已枚舉人類與計算機歷史上的所有 Search Methods。

第二，method boundaries 並不天然唯一。不同領域可能合理地選擇不同粒度；例如 citation search 可以是 graph search 的 specialization，也可以是獨立 operator family。

第三，multi-axis ontology 會增加 metadata 與維護成本。若 SearchMethodSpec 過度複雜，開發者可能拒絕正確填寫。

第四，很多 operational properties 依 provider、task 與 corpus 而變，因此不能只靠靜態 method metadata。

第五，composition calculus 目前只提供 plan constructs，尚未建立完整形式語義或證明 rewrite properties。

第六，合法資料存取、license、automation permission 與 source governance 只在本文作為 policy constraint 出現，將由後續專文完整處理。

第七，Planner 是否真的能利用此 ontology 提升搜尋品質，仍需要 benchmark 與 ablation experiment 驗證。

---

# 36. 結論

搜尋方法的歷史遠比「關鍵詞搜尋」豐富。

人類專業搜尋者有 tactics；資訊檢索有 relevance feedback、query expansion 與各種 retrieval models；資訊架構有 faceted navigation；學術研究有 citation searching；分散式 IR 有 federated search；Web 系統有 crawling 與 link traversal；現代 AI 又開始進行多輪、動態、工具化 Search Planning。

問題不再是有沒有這些方法，而是：

> **如何讓 AI 把它們當成同一個可操作方法空間中的不同認知算子。**

本文因此提出：

$$
\boxed{
\text{Search Method}
=
\text{Typed, Multi-Axial, Provider-Independent Search Operator}
}
$$

並以：

$$
\Omega_M
=
\mathcal{G}
\times
\mathcal{R}
\times
\mathcal{D}
\times
\mathcal{I}
\times
\mathcal{S}
\times
\mathcal{E}
\times
\mathcal{\Phi}
$$

描述方法空間。

進一步地：

$$
\boxed{
\text{Search Plan}
=
\text{Policy-valid composition of Search Methods over Search State}
}
$$

這使未來 AI 不再只有：

```text
Which tool should I call?
```

而能處理更精確的問題：

```text
What search effect is currently required?
Which method can produce it?
Which provider can legally and reliably implement that method?
What should run before, after, or in parallel?
What new evidence state will this operation create?
```

Paper 01 將搜尋提升為 AI 可規劃的認知行為；本文則建立那個行為所需的「方法詞彙表與組合法」。

下一步自然進入：

> **Paper 03 — 任務驅動的自主搜尋規劃：AI Search Planner、動態方法選擇與 Search Plan Optimization**

也就是研究 AI 如何真正從 $\mathcal{M}$ 中選出下一步。

---

# References

[1] Bates, M. J. (1979). *Information Search Tactics*. Journal of the American Society for Information Science, 30(4), 205–214. DOI: 10.1002/asi.4630300406.

[2] Bates, M. J. (1989). *The Design of Browsing and Berrypicking Techniques for the Online Search Interface*. Online Review, 13(5), 407–424.

[3] Broder, A. (2002). *A Taxonomy of Web Search*. ACM SIGIR Forum, 36(2), 3–10. DOI: 10.1145/792550.792552.

[4] Marchionini, G. (2006). *Exploratory Search: From Finding to Understanding*. Communications of the ACM, 49(4), 41–46. DOI: 10.1145/1121949.1121979.

[5] Hearst, M. A. (2006). *Design Recommendations for Hierarchical Faceted Search Interfaces*. ACM SIGIR Workshop on Faceted Search, 1–5.

[6] Wei, B., Liu, J., Zheng, Q., Zhang, W., Fu, X., & Feng, B. (2013). *A Survey of Faceted Search*. Journal of Web Engineering, 12(1–2), 41–64.

[7] Carpineto, C., & Romano, G. (2012). *A Survey of Automatic Query Expansion in Information Retrieval*. ACM Computing Surveys, 44(1), Article 1. DOI: 10.1145/2071389.2071390.

[8] Azad, H. K., & Deepak, A. (2019). *Query Expansion Techniques for Information Retrieval: A Survey*. Information Processing & Management, 56(5), 1698–1735. DOI: 10.1016/j.ipm.2019.05.009.

[9] Garba, A., Wu, S., & Khalid, S. (2023). *Federated Search Techniques: An Overview of the Trends and State of the Art*. Knowledge and Information Systems, 65, 5065–5095. DOI: 10.1007/s10115-023-01922-6.

[10] Hirt, J., Nordhausen, T., Fuerst, T., Ewald, H., Appenzeller-Herzog, C., & TARCiS Study Group. (2024). *Guidance on Terminology, Application, and Reporting of Citation Searching: The TARCiS Statement*. BMJ, 385, e078384. DOI: 10.1136/bmj-2023-078384.

[11] Haddaway, N. R., Grainger, M. J., & Gray, C. T. (2022). *Citationchaser: A Tool for Transparent and Efficient Forward and Backward Citation Chasing in Systematic Searching*. Research Synthesis Methods, 13(4), 533–545. DOI: 10.1002/jrsm.1563.

[12] Lewis, P., Perez, E., Piktus, A., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems 33. arXiv:2005.11401.

[13] Yao, S., Zhao, J., Yu, D., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. International Conference on Learning Representations. arXiv:2210.03629.

[14] Singh, A., Ehtesham, A., Kumar, S., Khoei, T. T., & Vasilakos, A. V. (2025/2026). *Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG*. arXiv:2501.09136, revised 2026.

[15] Xi, Y., Lin, J., Xiao, Y., et al. (2025). *A Survey of LLM-based Deep Search Agents: Paradigm, Optimization, Evaluation, and Challenges*. arXiv:2508.05668.

[16] Li, X., Dong, G., Jin, J., et al. (2025). *Search-o1: Agentic Search-Enhanced Large Reasoning Models*. Proceedings of EMNLP 2025, 5420–5438. DOI: 10.18653/v1/2025.emnlp-main.276.

---

# Series Continuation

**Paper 03 — 任務驅動的自主搜尋規劃：AI Search Planner、動態方法選擇與 Search Plan Optimization**

下一篇將以本文的：

$$
\mathcal{M}
=
\{M_1,\ldots,M_n\}
$$

與：

$$
\mathcal{A}_t
=
\{
(M_i,P_j)
\mid
\operatorname{Pre}(M_i,S_t)=1,
P_j\models M_i,
\operatorname{Allowed}=1
\}
$$

作為基礎，正式研究 Planner 如何將任務轉成 Search Graph、如何計算下一個搜尋行動、何時平行化、何時反證、如何控制 cost / latency / coverage，以及如何決定停止。
