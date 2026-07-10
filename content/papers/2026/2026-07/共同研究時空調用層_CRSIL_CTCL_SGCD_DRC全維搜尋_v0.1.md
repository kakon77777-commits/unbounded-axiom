# 共同研究時空調用層
## ——從 CTCL、SGCD 與 DRC Search 到 AI 原生的時間化研究圖、函數調用與全維搜尋架構

**Common Research Spatiotemporal Invocation Layer: From CTCL, SGCD, and DRC Search to AI-Native Temporal Research Graphs, Function Invocation, and Omnidimensional Search**

**作者：Neo.K（概念提出）**  
**版本：v0.1 理論草稿**  
**日期：2026**  
**文件性質：系統方法論論文／協議架構草案／可檢驗研究命題**

---

## 摘要

當全球研究產出進入上億至數億級研究物件尺度後，AI 面臨的核心問題已不再只是「如何從文件中找到相似段落」，而是如何在跨時間、跨版本、跨來源、跨理論系譜、跨語義空間、跨工具與跨函數調用的條件下，定位當前研究任務真正需要的知識狀態。傳統關鍵字搜尋以線性排名列表為主要介面；典型向量檢索與 RAG 則通常將查詢映射至若干相似文件或文本區塊，再將其送入生成模型。然而，當研究物件具有修訂、撤回、版本分叉、理論依賴、反駁、跨領域同構、網頁狀態變化與 API 回傳狀態變化時，單一相似度排序與靜態檢索不足以描述 AI 實際面對的研究世界。

本文提出「共同研究時空調用層」（Common Research Spatiotemporal Invocation Layer, CRSIL）作為一個面向 AI、Agent、研究基礎設施與長期知識系統的上位整合框架。CRSIL 並非取代既有 DOI、URI、PID、Crossref、DataCite、OpenAlex、Web Archive、Memento、W3C PROV、MCP 或其他工具協議，而是主張在這些既有元件之上或之間建立一個共同的、可轉換的、可追溯的研究事件空間。

本文將既有三套方法論進行系統級合流：

1. **共同時間座標層（CTCL）**：提供共同參考瞬間、時間尺度、來源追溯、轉換圖與版本化時間語義；
2. **語義圖論耦合動力學（SGCD）**：提供任務條件化、多維耦合、動態圖投影與選擇性上下文激活；
3. **DRC Search**：提供發散—共振—壓縮式搜尋，使搜尋結果由線性列表轉為可探索、可回溯、可再次展開的認知場。

本文進一步新增第四個關鍵層：

4. **時空化函數調用層（Spatiotemporal Function Invocation）**：將每次 API、Tool、Agent Action、資料庫查詢與外部函數調用視為具有時間、版本、來源、輸入、輸出、有效區間與依賴鏈的研究事件。

因此，本文主張未來 AI 研究的基本單位不應只是文件：

$$
Document
$$

而應轉向：

$$
Research\ State
$$

與：

$$
Research\ Event
$$

研究搜尋也不應只執行：

$$
Query
\rightarrow
Ranked\ List
$$

或：

$$
Query
\rightarrow
TopK
\rightarrow
Context
\rightarrow
Answer
$$

而應逐步演化為：

$$
Query
\rightarrow
Temporal\ Alignment
\rightarrow
Divergence
\rightarrow
Dynamic\ Graph\ Projection
\rightarrow
Coupling
\rightarrow
Function\ Invocation
\rightarrow
Evidence\ Update
\rightarrow
Resonance
\rightarrow
Compression
$$

本文將此方法稱為「全維研究場搜尋」（Omnidimensional Research-Field Search）。其目的不是要求 AI 在所有維度上進行無限制窮舉，而是讓不同任務依需求動態投影語義、時間、系譜、依賴、矛盾、版本、來源、證據、同構、方法、可重現性與任務共振等維度。

本文的核心命題為：

> **線性排名列表是人類注意力限制下有效的介面投影，但不應被誤認為搜尋本體；對 AI 而言，更自然的研究介面可能是可時間對齊、可版本追蹤、可函數調用、可多維投影的動態研究時空圖。**

本文不宣稱已建立完整通用協議，也不宣稱所有研究物件必須擁有 DOI，或所有網頁均具有可靠歷史版本。本文提出的是一套可實作、可分階段建構、可比較 RAG 與 GraphRAG、並可被工程實驗證偽的系統方法論。

**關鍵詞：** CRSIL、共同研究時空調用層、CTCL、SGCD、DRC Search、RAG、Agentic Search、DOI、PID、Temporal Web、Function Calling、Research Graph、Provenance、全維搜尋、AI Research Infrastructure

---

# 1. 緒論：研究世界已不再適合被理解為文件列表

人類長期以來主要透過以下形式接觸知識：

```text
書目
目錄
索引
搜尋結果頁
引文列表
資料庫結果
期刊卷期
網頁列表
```

其共同特徵是：

$$
x_1,x_2,x_3,\dots,x_n
$$

即將高維資訊空間壓縮為線性排列。

此設計並非錯誤。對人類而言，視覺焦點、工作記憶與注意力具有明顯限制，因此：

$$
\Pi_{human}:
\mathcal{S}
\rightarrow
(x_1,x_2,\dots,x_k)
$$

是一種極有效率的介面投影。

然而，當 AI 成為搜尋者、閱讀者、研究協作者與工具調用者時，問題開始改變。

AI 不必先將所有候選關係壓縮為一條列表，才有能力進行內部計算。它可以維持：

- 多個平行搜尋分支；
- 多個候選理論族；
- 多個時間版本；
- 多個矛盾關係；
- 多個來源可信度；
- 多個工具調用路徑；
- 多個跨領域類比；
- 多個尚未合併的證據集合。

因此：

$$
Search\ Ontology
\neq
Ranked\ List
$$

更精確地說：

$$
Ranked\ List
=
\Pi_{human}
(
Search\ Field
)
$$

本文由此提出：

> 搜尋列表是搜尋場的介面投影，而不是搜尋本體。

---

# 2. 從文件檢索到研究狀態導航

傳統資訊檢索常可表示為：

$$
q
\rightarrow
\{d_1,d_2,\dots,d_k\}
$$

其中：

- $q$ ：查詢；
- $d_i$ ：文件。

典型 RAG 可簡化為：

$$
q
\rightarrow
Retrieve(TopK)
\rightarrow
Chunks
\rightarrow
LLM
\rightarrow
Answer
$$

這在大量任務中有效。

但研究任務通常包含另一組問題：

1. 此文件是哪一版？
2. 此命題何時首次出現？
3. 後續是否被修正？
4. 是否已撤回？
5. 此網頁在 AI 讀取後是否改版？
6. API 今日回傳內容是否與昨日相同？
7. 某模型是否依賴另一模型？
8. 某反例是否只反駁舊版本？
9. 跨領域是否存在結構同構？
10. 當前任務需要原文、摘要、證據、程式碼還是函數輸出？

因此，研究單位不應只表示為：

$$
d_i
$$

而應表示為狀態化物件：

$$
R_i(\Theta,V,P,C)
$$

其中：

- $\Theta$ ：時間束；
- $V$ ：版本；
- $P$ ：來源與 provenance；
- $C$ ：情境與任務條件。

本文稱之為：

# **研究狀態（Research State）**

---

# 3. 既有理論的三重基礎

CRSIL 並非從零開始，而是建立於三套既有方法論之上。

---

## 3.1 CTCL：共同時間座標層

CTCL 的最小結構為：

$$
\boxed{
Reference\ Instant
+
Timescale
+
Provenance
+
Transform\ Graph
}
$$

令共同參考瞬間為：

$$
I^\*
$$

不同系統可表示：

$$
\tau_i
=
\Phi_i(I^\*)
$$

因此不同 Agent、資料庫、模擬器或網站不必使用相同的內部時間編碼，只需能對齊共同參考瞬間。

CTCL 進一步允許版本化轉換：

$$
\Phi_{A\rightarrow B}^{(v)}
$$

因為時間轉換本身可能依賴：

- timezone database version；
- leap-second table；
- calendar rule；
- custom epoch；
- historical rule；
- simulation mapping。

CRSIL 將此思想從「Agent 時間」擴展至「研究事件時間」。

---

## 3.2 SGCD：語義圖論耦合動力學

SGCD 不將相關性壓縮為單一 embedding similarity。

對研究節點 $v_i,v_j$ ，可定義多維耦合向量：

$$
\mathbf c_{ij}
=
\left(
c_{ij}^{sem},
c_{ij}^{term},
c_{ij}^{sym},
c_{ij}^{dep},
c_{ij}^{gene},
c_{ij}^{prop},
c_{ij}^{temp},
c_{ij}^{contra},
c_{ij}^{ref}
\right)
$$

其中：

- $sem$ ：語義；
- $term$ ：術語；
- $sym$ ：符號；
- $dep$ ：依賴；
- $gene$ ：理論系譜；
- $prop$ ：命題；
- $temp$ ：時間；
- $contra$ ：矛盾；
- $ref$ ：引用或指涉。

對任務 $\tau$ ：

$$
\kappa_{ij}^{(\tau)}
=
F_\tau
(
\mathbf c_{ij},
s_i,
s_j,
h_{ij}
)
$$

因此：

> 上下文不因存在於資料庫而被調用，而因當前任務下具有足夠有效耦合而被激活。

---

## 3.3 DRC Search：發散—共振—壓縮

DRC Search 定義：

$$
D\rightarrow R\rightarrow C
$$

即：

$$
Divergence
\rightarrow
Resonance
\rightarrow
Compression
$$

傳統搜尋：

```text
Query
↓
Ranked Results
```

一般 AI 搜尋：

```text
Query
↓
Retrieved Sources
↓
Synthetic Answer
```

DRC Search：

```text
Concept Seed
↓
Divergent Branches
↓
Candidate Search Field
↓
Resonant Nodes
↓
Graph / Cognitive Map
↓
Compression
↓
Re-expandable Result
```

其核心差異是：

$$
Answer
\neq
Final\ Search\ State
$$

壓縮後結果仍可再次展開。

---

# 4. 新的合流：共同研究時空調用層

本文提出：

$$
\boxed{
CRSIL
=
CTCL
+
SGCD
+
DRC
+
PID
+
Provenance
+
Function\ Invocation
}
$$

其中：

- CTCL 解決共同時間與異質轉換；
- SGCD 解決多維關係與任務投影；
- DRC 解決搜尋場展開、共振與壓縮；
- PID 解決研究物件識別；
- Provenance 解決來源與生成鏈；
- Function Invocation 解決 AI 對外部世界的動態操作。

因此 CRSIL 的定位不是單一資料庫，而是：

# **研究世界的中介時空層**

---

# 5. 研究物件的最小狀態表示

令研究物件為：

$$
o_i
$$

本文建議其最小表示為：

$$
o_i
=
(
ID_i,
URI_i,
PID_i,
H_i,
V_i,
\Theta_i,
P_i,
\Sigma_i,
A_i
)
$$

其中：

- $ID_i$ ：內部識別；
- $URI_i$ ：可定位位置；
- $PID_i$ ：DOI 或其他永久識別；
- $H_i$ ：內容雜湊；
- $V_i$ ：版本；
- $\Theta_i$ ：時間束；
- $P_i$ ：provenance；
- $\Sigma_i$ ：語義／理論狀態；
- $A_i$ ：可調用能力。

注意：

$$
PID_i
$$

不必然存在。

因此：

$$
PID_i\in
\{
DOI,
Handle,
ARK,
URN,
LocalID,
Null
\}
$$

本文不主張所有理論都必須擁有 DOI，而主張：

> 若存在永久識別符，應將其作為研究時空節點的高權重身份錨點，而非唯一身份來源。

---

# 6. 單一時間戳不足：研究時間束

一篇論文或研究物件的「時間」並不是一個值。

本文定義：

$$
\Theta_i
=
(
t_{created},
t_{submitted},
t_{published},
t_{deposited},
t_{indexed},
t_{revised},
t_{valid},
t_{observed},
t_{accessed},
t_{invalidated}
)
$$

其中：

- $t_{created}$ ：創建；
- $t_{submitted}$ ：投稿；
- $t_{published}$ ：發布；
- $t_{deposited}$ ：metadata 登錄；
- $t_{indexed}$ ：被索引；
- $t_{revised}$ ：修訂；
- $t_{valid}$ ：有效區間；
- $t_{observed}$ ：某系統觀測；
- $t_{accessed}$ ：某 Agent 實際存取；
- $t_{invalidated}$ ：失效、撤回或被替代。

因此：

$$
Publication\ Time
\neq
Observation\ Time
$$

並且：

$$
Observation\ Time
\neq
Validity\ Time
$$

例如：

> 一篇 2023 年發布的論文，可能在 2026 年被 Agent 首次讀取，但 Agent 讀取的是 2025 年修訂版本，且該版本在 2026 年後又被撤回。

此事件無法由：

$$
t=2023
$$

完整表示。

---

# 7. 網頁時間：從 URL 到狀態化 Web 資源

一般 Web 資源常被表示為：

$$
URI
\rightarrow
Representation
$$

但同一 URI 在不同時間可能回傳不同內容：

$$
W(u,t_1)
\neq
W(u,t_2)
$$

因此，對研究型 AI 而言：

$$
u
$$

不足以唯一定位「曾經看過的證據」。

本文建議表示：

$$
w_i
=
(
URI,
I^\*,
ObservedAt,
ContentHash,
Headers,
ArchiveRef,
Provenance
)
$$

若可取得歷史版本，則：

$$
W(u,t)
$$

應成為可查詢研究狀態。

現有 Memento / RFC 7089 已證明 Web 資源可以透過 datetime negotiation 與 TimeMap 思路存取歷史狀態；CRSIL 的擴展方向則是將這種時間化資源存取接入 AI 研究圖，而不是只作為網頁典藏功能。

---

# 8. 函數調用也必須成為研究事件

這是本文新增的核心部分。

傳統函數觀念：

$$
f(x)=y
$$

但對外部 API 或 Agent Tool：

$$
y
=
f(
x;
t,
v_f,
v_d,
auth,
state,
source
)
$$

其中：

- $t$ ：調用時間；
- $v_f$ ：函數版本；
- $v_d$ ：資料版本；
- $auth$ ：授權狀態；
- $state$ ：外部系統狀態；
- $source$ ：來源。

因此兩次相同調用：

$$
f(x,t_1)
$$

與：

$$
f(x,t_2)
$$

可能：

$$
f(x,t_1)
\neq
f(x,t_2)
$$

本文定義每一次函數調用事件：

$$
e_k
=
(
Agent_k,
Tool_k,
Input_k,
I_k^\*,
V_k,
P_k,
Output_k,
H_k,
Dependency_k
)
$$

其中：

- $Agent_k$ ：調用者；
- $Tool_k$ ：工具；
- $Input_k$ ：輸入；
- $I_k^\*$ ：共同參考瞬間；
- $V_k$ ：工具與協議版本；
- $P_k$ ：來源；
- $Output_k$ ：輸出；
- $H_k$ ：輸出 hash；
- $Dependency_k$ ：依賴鏈。

因此：

# **Tool Call 本身也是研究資料。**

---

# 9. 時空化函數

本文提出：

$$
f^{(v_f)}
:
(
x,
I^\*,
\Omega
)
\rightarrow
y
$$

其中：

$$
\Omega
=
(
source,
auth,
dataset\_version,
protocol\_version,
context,
uncertainty
)
$$

更一般化：

$$
y_k
=
f_k^{(v)}
(
x_k
\mid
I^\*,
\Omega_k
)
$$

此形式的意義在於：

> AI 不只知道「得到什麼答案」，還知道「在什麼共同事件位置、使用哪個工具版本、從哪個資料狀態得到答案」。

---

# 10. 從靜態研究圖到事件化研究圖

一般研究圖：

$$
G=(V,E)
$$

本文擴展為：

$$
\mathcal{G}
=
(
V_R,
V_W,
V_F,
V_A,
V_E,
E,
\Theta,
P
)
$$

其中：

- $V_R$ ：Research Objects；
- $V_W$ ：Web States；
- $V_F$ ：Functions / Tools；
- $V_A$ ：Agents；
- $V_E$ ：Events；
- $E$ ：關係；
- $\Theta$ ：時間；
- $P$ ：provenance。

因此，圖中可以表示：

```text
Paper A v1
↓ IsPreviousVersionOf
Paper A v2

Paper A v2
↓ ContradictedBy
Paper B

Paper B
↓ RetrievedBy
Agent X

Agent X
↓ Invoked
Tool Y v3

Tool Y v3
↓ ReturnedAt
Instant I*

Output Z
↓ Supports
Claim C
```

這已不是單純 citation graph。

---

# 11. 理論節點與文件節點必須分離

一篇文件可能包含多個理論物件：

$$
d_i
\supset
\{
p_1,
p_2,
h_1,
m_1,
c_1
\}
$$

其中：

- $p$ ：命題；
- $h$ ：假說；
- $m$ ：模型；
- $c$ ：猜想。

因此：

$$
Document\ Node
\neq
Theory\ Node
$$

本文建議至少區分：

$$
V
=
V_D
\cup
V_T
\cup
V_P
\cup
V_M
\cup
V_E
$$

其中：

- $V_D$ ：文件；
- $V_T$ ：理論；
- $V_P$ ：命題；
- $V_M$ ：方法；
- $V_E$ ：證據。

這對全球理論去重尤其重要。

---

# 12. 理論系譜與時間耦合

若：

$$
T_1
\rightarrow
T_2
\rightarrow
T_3
$$

代表：

- $T_2$ 修正 $T_1$ ；
- $T_3$ 一般化 $T_2$ 。

則搜尋「最新理論」不能只排序：

$$
t_{published}
$$

因為：

$$
Newest
\neq
Most\ Relevant
$$

也不必然：

$$
Newest
=
Current\ Valid\ State
$$

本文建議：

$$
State(T_i,I^\*)
=
f(
version,
genealogy,
evidence,
contradiction,
validity,
task
)
$$

因此研究搜尋必須判斷：

> 在當前共同參考瞬間與任務下，哪一個理論狀態有效？

---

# 13. 全維研究場搜尋

本文提出「全維研究場搜尋」。

其基本評分不再是一個標量：

$$
Score(q,d)
$$

而是向量：

$$
\mathbf S(q,x,I^\*)
=
\left(
s_{sem},
s_{temp},
s_{gene},
s_{dep},
s_{contra},
s_{ver},
s_{prov},
s_{evid},
s_{nov},
s_{iso},
s_{method},
s_{repro},
s_{task}
\right)
$$

其中：

- $s_{sem}$ ：語義相關；
- $s_{temp}$ ：時間對齊；
- $s_{gene}$ ：系譜；
- $s_{dep}$ ：依賴；
- $s_{contra}$ ：矛盾；
- $s_{ver}$ ：版本；
- $s_{prov}$ ：來源；
- $s_{evid}$ ：證據；
- $s_{nov}$ ：新穎；
- $s_{iso}$ ：結構同構；
- $s_{method}$ ：方法；
- $s_{repro}$ ：可重現；
- $s_{task}$ ：任務共振。

---

# 14. 「全維」不等於每次搜尋所有維度

本文必須避免一個誤解。

全維搜尋不是：

$$
\forall q,
\forall d,
\text{evaluate all dimensions maximally}
$$

這會導致巨大成本。

本文主張：

$$
\Pi_\tau:
\mathcal{S}_{all}
\rightarrow
\mathcal{S}_\tau
$$

即依任務 $\tau$ 動態選擇維度。

例如：

## 14.1 文獻回顧

$$
\mathbf w^{review}
=
(
w_{sem},
w_{gene},
w_{temp},
w_{evid},
w_{prov}
)
$$

## 14.2 反例搜尋

$$
\mathbf w^{counterexample}
=
(
w_{contra},
w_{dep},
w_{prop},
w_{temp}
)
$$

## 14.3 理論去重

$$
\mathbf w^{dedup}
=
(
w_{sem},
w_{prop},
w_{iso},
w_{gene},
w_{term}
)
$$

## 14.4 最新狀態搜尋

$$
\mathbf w^{current}
=
(
w_{temp},
w_{ver},
w_{valid},
w_{prov}
)
$$

因此：

> 全維是可用維度的完備候選空間，不是每次無差別全開。

---

# 15. 為何不應再過度依賴單一總分

若：

$$
Score
=
\sum_i w_i s_i
$$

則多維關係再次被壓縮成一維。

這有時必要，但可能掩蓋：

- 高語義但過期；
- 高新穎但低可信；
- 高矛盾但極重要；
- 低字面相似但高度同構。

因此本文建議三種輸出並存。

## 15.1 任務標量投影

$$
Score_\tau
=
\sum_i w_i^{(\tau)}s_i
$$

## 15.2 Pareto Front

$$
\mathcal{P}
=
ParetoFront
(
\mathbf S_1,\dots,\mathbf S_n
)
$$

## 15.3 動態關係圖

$$
G_\tau(I^\*)
$$

因此：

> 排名可以保留，但不再是唯一搜尋本體。

---

# 16. CRSIL 的完整流程

本文提出：

$$
Q
\xrightarrow{CTCL}
Q^\*
\xrightarrow{DRC_D}
\mathcal{B}
\xrightarrow{SGCD}
G_Q(I^\*)
\xrightarrow{Invocation}
G'_Q
\xrightarrow{DRC_R}
G_Q^\*
\xrightarrow{DRC_C}
K_Q
$$

逐步解釋如下。

---

## 16.1 時間對齊

$$
Q
\xrightarrow{CTCL}
Q^\*
$$

將：

- 今日；
- 當前；
- 截至某日；
- 某版本；
- 歷史狀態；

轉換為明確時間條件。

---

## 16.2 DRC 發散

$$
Q^\*
\xrightarrow{D}
\mathcal{B}
$$

生成：

- 同義方向；
- 對立方向；
- 歷史方向；
- 跨領域方向；
- 方法方向；
- 反例方向；
- 資料方向。

---

## 16.3 SGCD 動態投影

$$
\mathcal{B}
\xrightarrow{SGCD}
G_Q(I^\*)
$$

建立當前任務研究圖。

---

## 16.4 工具與 API 調用

$$
G_Q(I^\*)
\xrightarrow{Invocation}
G'_Q
$$

調用：

- DOI metadata；
- research graph；
- archive；
- dataset；
- code repository；
- calculator；
- theorem prover；
- simulation；
- web API。

---

## 16.5 證據更新

每次調用：

$$
e_k
$$

更新：

$$
G^{(k+1)}
=
Update(
G^{(k)},
e_k
)
$$

---

## 16.6 共振

$$
G'_Q
\xrightarrow{R}
G_Q^\*
$$

依任務選出高價值節點。

---

## 16.7 壓縮

$$
G_Q^\*
\xrightarrow{C}
K_Q
$$

輸出：

- 論證圖；
- 認知地圖；
- 文獻矩陣；
- 時間線；
- 理論譜系；
- 可執行研究計畫；
- 下一步函數調用。

---

# 17. RAG 與 CRSIL 的差異

## 17.1 典型 RAG

$$
q
\rightarrow
TopK
\rightarrow
Chunks
\rightarrow
LLM
$$

## 17.2 CRSIL

$$
q
\rightarrow
Temporalized\ Query
\rightarrow
Multi\!-\!Branch\ Search
\rightarrow
Dynamic\ Research\ Graph
\rightarrow
Selective\ Invocation
\rightarrow
Evidence\ Evolution
\rightarrow
Task\ Projection
$$

差異不在於「有沒有向量資料庫」。

而在於：

> RAG 主要回答「取回什麼內容」；CRSIL 還要回答「哪個時間狀態、哪個版本、哪個理論位置、透過哪次調用、以何種來源鏈取回」。

---

# 18. 與 GraphRAG 的差異

即使採用 GraphRAG，仍可能：

- 圖是靜態的；
- 時間只是屬性；
- tool call 不入圖；
- web state 不可重現；
- 版本轉換未顯式表示；
- 搜尋仍以單一 query projection 為主。

CRSIL 主張：

$$
Graph
\rightarrow
Temporalized\ Event\ Graph
$$

並且：

$$
Retrieval
\rightarrow
State\ Navigation
$$

---

# 19. 與 DOI / PID 基礎設施的關係

DOI 等 PID 解決的是身份錨定與持久引用的重要部分。

CRSIL 不取代 DOI。

而是：

$$
PID
\rightarrow
Node\ Identity\ Anchor
$$

例如：

$$
DOI_i
\Rightarrow
o_i
$$

但研究物件可能還需要：

$$
(
DOI,
Version,
Hash,
ObservedAt,
Source
)
$$

才能重建 Agent 實際看到的狀態。

因此：

$$
DOI
\neq
Complete\ Research\ State
$$

---

# 20. 與 Crossref、DataCite 與 OpenAlex 的關係

截至本文寫作時，既有研究基礎設施已提供重要零件：

- Crossref REST API 提供 DOI metadata 的機器化存取與查詢；
- DataCite Metadata Schema 提供研究物件識別與 metadata 結構，並支援透過 RelatedIdentifier 表示版本關係；
- OpenAlex API 提供 Works、Authors、Sources、Institutions、Topics 等研究實體與開放研究圖。

因此，CRSIL 並非宣稱世界缺乏研究 API。

本文的問題是：

> 這些研究物件、時間狀態、版本關係、Web 歷史、provenance 與 Agent tool call，是否存在共同的研究事件座標與動態調用層？

本文提出的正是此上位整合問題。

---

# 21. 與 Memento / RFC 7089 的關係

Memento 提供 Web 資源歷史狀態存取的重要前驅思路：

$$
URI
+
Datetime
\rightarrow
Prior\ State
$$

CRSIL 將問題擴展為：

$$
Resource
+
Time
+
Version
+
Provenance
+
Task
+
Invocation
\rightarrow
Research\ State
$$

因此，Memento 可視為 CRSIL 在 Temporal Web 方向上的重要可對接元件，而不是 CRSIL 的完整替代。

---

# 22. 與 W3C PROV 的關係

W3C PROV 將 provenance 建模為與：

- Entity；
- Activity；
- Agent；

相關的來源資訊。

CRSIL 可直接吸收此思想：

$$
Entity
\leftrightarrow
Research\ Object
$$

$$
Activity
\leftrightarrow
Invocation/Event
$$

$$
Agent
\leftrightarrow
Human/AI/System
$$

因此，CRSIL 不需要重新發明所有 provenance 語義，而可建立 domain specialization。

---

# 23. 與 MCP 類工具協議的關係

現有 MCP 規格已允許伺服器向語言模型暴露：

- Resources；
- Prompts；
- Tools。

其中 Tool 可被模型調用，以查詢資料庫、呼叫 API 或進行計算。

CRSIL 的新增問題是：

> 一次工具調用如何被定位在共同研究時空中？

因此可表示：

$$
MCP/Tool\ Protocol
\quad over \quad
CRSIL
$$

或：

$$
CRSIL
\quad as \quad
Temporal\ Provenance\ Layer
$$

這兩者可互補。

---

# 24. 最小協議物件

本文建議 CRSIL 至少包含六種核心物件。

## 24.1 ResearchObject

```json
{
  "id": "crsil:object:...",
  "pid": "doi:...",
  "uri": "...",
  "content_hash": "...",
  "version": "v2"
}
```

## 24.2 TemporalBundle

```json
{
  "reference_instant": "ctcl:instant:...",
  "published_at": "...",
  "revised_at": "...",
  "observed_at": "...",
  "valid_from": "...",
  "valid_to": null
}
```

## 24.3 ProvenanceBundle

```json
{
  "source": "...",
  "retrieved_by": "agent:...",
  "retrieval_method": "api",
  "confidence": 0.91
}
```

## 24.4 CouplingVector

```json
{
  "semantic": 0.81,
  "genealogical": 0.63,
  "temporal": 0.92,
  "contradiction": 0.15,
  "dependency": 0.74
}
```

## 24.5 InvocationEvent

```json
{
  "event_id": "crsil:event:...",
  "agent_id": "agent:...",
  "tool_id": "tool:...",
  "tool_version": "3.1",
  "input_hash": "...",
  "output_hash": "...",
  "reference_instant": "ctcl:instant:..."
}
```

## 24.6 ResearchProjection

```json
{
  "task": "theory_genealogy",
  "active_dimensions": [
    "genealogical",
    "temporal",
    "reference",
    "version"
  ]
}
```

---

# 25. 函數調用共同時空間

本文將多次函數調用表示為事件集合：

$$
\mathcal{E}_F
=
\{
e_1,e_2,\dots,e_n
\}
$$

每個事件映射到共同參考：

$$
e_k
\mapsto
I_k^\*
$$

若系統 A 與 B 使用不同 clock：

$$
\tau_A
=
\Phi_A(I^\*)
$$

$$
\tau_B
=
\Phi_B(I^\*)
$$

則可對齊：

$$
e_A
\sim_{I^\*}
e_B
$$

因此：

> 不同 Agent、不同 API 與不同資料庫可以保留自身時間語義，同時在研究事件層確認它們是否指向同一參考瞬間或可比較區間。

---

# 26. 研究狀態的可重現性

若 AI 生成一項研究結論：

$$
C
$$

則理想上應保留：

$$
Trace(C)
=
\{
o_i,
v_i,
e_k,
I^\*,
P_i,
f_k^{(v)}
\}
$$

使另一 Agent 能回答：

1. 使用哪些研究物件？
2. 哪些版本？
3. 在何時讀取？
4. 哪些工具被調用？
5. 工具當時版本？
6. 回傳內容是否仍可重建？
7. 哪些節點支持結論？
8. 哪些節點反駁結論？

因此：

$$
Reproducibility
\neq
Prompt\ Replay
$$

而應接近：

$$
Research\ State\ Replay
$$

---

# 27. 版本分叉與研究世界線

假設理論：

$$
T_0
$$

分叉：

$$
T_0
\rightarrow
T_{1a}
$$

$$
T_0
\rightarrow
T_{1b}
$$

後續：

$$
T_{1a}
\rightarrow
T_{2a}
$$

則研究系譜不是單線：

$$
T_0\rightarrow T_1\rightarrow T_2
$$

而是：

$$
\mathcal{G}_{gene}
$$

本文將不同版本與理論演化路徑比喻為：

# **研究世界線（Research Worldlines）**

此處「世界線」為計算結構比喻，不主張物理時空同一性。

---

# 28. 跨領域同構搜尋

傳統搜尋高度依賴詞彙。

但兩個理論可能：

$$
LexicalSimilarity(T_i,T_j)
\approx0
$$

同時：

$$
StructuralIsomorphism(T_i,T_j)
\gg0
$$

例如兩個領域可能共享：

- feedback；
- attractor；
- phase transition；
- constraint propagation；
- graph cut；
- symmetry breaking；
- fixed point。

全維研究場搜尋可加入：

$$
s_{iso}
$$

並搜尋：

$$
T_i
\cong
T_j
$$

的候選。

這對跨領域研究尤其重要。

---

# 29. 理論去重與重複研究

全球研究中可能出現：

$$
T_A
\approx
T_B
$$

但：

- 語言不同；
- 學科不同；
- 符號不同；
- 作者互不知情；
- 時間不同。

本文提出：

$$
DupCandidate(T_A,T_B)
=
f(
s_{sem},
s_{prop},
s_{iso},
s_{gene},
s_{temp}
)
$$

其目標不是自動宣判「抄襲」，而是：

> 建立候選重複、獨立重發現、局部同構與理論吸收關係。

---

# 30. AI 研究不再只是找論文

未來 Agent 面對問題：

> 某猜想是否存在可行證明路線？

不應只：

$$
Search("conjecture proof")
$$

而可以：

1. 發散相關命題；
2. 找直接依賴；
3. 找反例；
4. 找歷史失敗路線；
5. 找跨領域同構；
6. 找可調用定理證明器；
7. 找資料集；
8. 執行計算；
9. 更新研究圖；
10. 壓縮為候選路線。

因此：

$$
Search
\rightarrow
Research\ Orchestration
$$

---

# 31. AI 原生研究空間

本文提出：

$$
\mathcal{R}_{AI}
=
\mathcal{O}
\times
\mathcal{T}
\times
\mathcal{V}
\times
\mathcal{P}
\times
\mathcal{C}
\times
\mathcal{F}
\times
\mathcal{E}
$$

其中：

- $\mathcal{O}$ ：物件；
- $\mathcal{T}$ ：時間；
- $\mathcal{V}$ ：版本；
- $\mathcal{P}$ ：provenance；
- $\mathcal{C}$ ：耦合；
- $\mathcal{F}$ ：函數；
- $\mathcal{E}$ ：事件。

AI 對此空間的研究不是閱讀一條清單，而是：

$$
Navigate(
\mathcal{R}_{AI}
\mid
Task,
I^\*
)
$$

---

# 32. 線性列表仍然有價值

本文不主張消滅搜尋排名。

對人類使用者：

$$
\Pi_{UI}
(
G_\tau
)
=
List
$$

完全合理。

真正的差異是：

> 系統內部不必先退化成 List，才進行研究計算。

因此：

```text
AI Internal State:
Dynamic Research Field

Human Interface:
List / Map / Timeline / Graph / Matrix
```

---

# 33. 可檢驗命題

本文提出以下命題。

## 命題一：時間對齊優勢命題

在涉及版本更新、撤回、政策變化或網頁變更的研究任務中：

$$
Performance(CRSIL_{temp})
>
Performance(RAG_{static})
$$

---

## 命題二：調用可追溯命題

保留 InvocationEvent 的系統，其研究重現能力應高於只保留最終回答的系統。

---

## 命題三：多維搜尋命題

對跨領域與反例搜尋任務：

$$
Recall(
MultiDimensional
)
>
Recall(
SimilarityOnly
)
$$

在合理成本限制下應具有可檢驗優勢。

---

## 命題四：研究狀態導航命題

對版本分叉文獻：

$$
StateNavigation
$$

比：

$$
LatestDateSort
$$

更能找到當前有效理論狀態。

---

## 命題五：可再次展開壓縮命題

DRC 式可逆或半可逆壓縮，比單一摘要更適合長期 Agent 研究。

---

## 命題六：函數調用時間敏感命題

對動態 API：

$$
f(x,t_1)
\neq
f(x,t_2)
$$

的比例足以使 tool-call timestamp、版本與 provenance 成為必要研究 metadata。

---

# 34. 最小實驗設計

## 34.1 基準系統

建立：

1. Keyword Search；
2. Vector Search；
3. RAG；
4. GraphRAG；
5. CRSIL-lite。

---

## 34.2 任務集合

測試：

- 最新版本判斷；
- 理論系譜；
- 反例搜尋；
- 跨領域同構；
- 網頁歷史狀態；
- API 動態輸出；
- 理論去重。

---

## 34.3 評估指標

$$
M
=
(
Precision,
Recall,
TemporalAccuracy,
VersionAccuracy,
Traceability,
Novelty,
Cost
)
$$

---

## 34.4 消融實驗

依次移除：

- CTCL；
- SGCD；
- DRC；
- Provenance；
- Invocation Event。

觀察：

$$
\Delta Performance
$$

---

# 35. 工程最小可行版本

CRSIL v0.1 不需要建立全球協議。

可從小型 corpus 開始。

例如：

$$
n=1600
$$

篇理論文件。

最小流程：

```text
Documents
↓
PID / Local ID
↓
Time Bundle
↓
Version Graph
↓
SGCD Candidate Edges
↓
DRC Query Expansion
↓
Tool Invocation Log
↓
Dynamic Research Projection
↓
Map / Timeline / List Output
```

---

# 36. CRSIL-lite 建議 Schema

```yaml
object_id: LM-0817
pid:
  doi: null
  local: LM-0817

identity:
  uri: ...
  content_hash: ...

version:
  label: v0.3
  previous: LM-0817-v0.2

time:
  created_at: ...
  published_at: null
  revised_at: ...
  observed_at: ...
  reference_instant: ctcl:instant:...

provenance:
  source_type: local_corpus
  source_id: ...

theory:
  family:
    - operator_ontology
  claims:
    - ...
  terms:
    - ...

coupling:
  semantic: ...
  genealogical: ...
  temporal: ...
  contradiction: ...

invocations:
  - event_id: ...
```

---

# 37. 安全與治理問題

CRSIL 會產生新的治理風險。

## 37.1 時間偽造

錯誤 timestamp 可能造成錯誤理論先後判定。

## 37.2 Provenance 污染

來源鏈可被偽造。

## 37.3 工具輸出漂移

API 在無公告下改變。

## 37.4 錯誤理論合併

語義模型可能將不同理論錯判為同一族。

## 37.5 全維爆炸

維度過多可能導致：

$$
Computational\ Explosion
$$

因此 CRSIL 必須採：

$$
Task\!-\!Conditioned\ Projection
$$

而非無限全開。

---

# 38. 可能的反對意見

## 38.1 「這只是 GraphRAG 加 timestamp」

不完全是。

CRSIL 還要求：

- 共同參考瞬間；
- 異質時間轉換；
- 版本圖；
- Web 狀態；
- tool call event；
- provenance；
- DRC 搜尋循環；
- 任務條件化耦合。

---

## 38.2 「DOI 已經夠了」

DOI 解決持久識別的重要部分。

但：

$$
DOI
\neq
Observation\ State
$$

也不等於：

$$
DOI
\neq
Tool\ Invocation\ Trace
$$

---

## 38.3 「全部用 UTC 即可」

UTC 可作共同尺度之一。

但研究事件仍有：

- publication time；
- observation time；
- validity time；
- version time；
- simulated time。

因此：

$$
UTC
\neq
Complete\ Temporal\ Semantics
$$

---

## 38.4 「AI 最後還是要排序」

可以排序。

本文反對的是：

> 將排序誤認為唯一搜尋本體。

---

## 38.5 「維度太多，成本不可接受」

因此本文使用：

$$
\Pi_\tau
$$

依任務動態投影。

---

# 39. 與全球研究基礎設施的長期關係

若未來更多研究物件具備：

- PID；
- version metadata；
- machine-readable claims；
- provenance；
- temporal bundle；
- API endpoint；

則 AI 可將研究世界從：

```text
PDF 海洋
```

逐步轉換為：

```text
Callable Research Space
```

即：

$$
Readable\ Knowledge
\rightarrow
Invocable\ Knowledge
$$

---

# 40. 從「可讀論文」到「可調用理論」

未來理論可能不只提供：

- PDF；
- HTML；
- abstract。

還可能提供：

- claim endpoint；
- symbol registry；
- dependency graph；
- executable model；
- proof object；
- dataset pointer；
- version API；
- contradiction API。

因此：

$$
Theory
\rightarrow
Callable\ Theoretical\ Object
$$

這是本文長期方向之一。

---

# 41. 研究協議的可能演化

可想像：

```text
DOI Era
↓
Open Metadata Era
↓
Research Graph Era
↓
Agent Tool Era
↓
Temporal Research State Era
↓
Callable Theory Era
```

本文不主張歷史必然如此。

此處只是技術演化假說。

---

# 42. 核心總命題

本文提出：

## **研究時空化命題**

當研究物件具有：

- 多版本；
- 多時間；
- 多來源；
- 多關係；
- 多工具調用；

時，將其表示為靜態文件集合會遺失結構資訊。

因此更完整表示為：

$$
\mathcal{R}
=
(
Objects,
Events,
Time,
Version,
Provenance,
Coupling,
Invocation
)
$$

---

## **搜尋場命題**

線性搜尋結果：

$$
L
=
(x_1,\dots,x_n)
$$

可被視為高維研究場：

$$
\mathcal{S}
$$

的投影：

$$
L
=
\Pi_{human}(\mathcal{S})
$$

因此：

$$
L
\neq
\mathcal{S}
$$

---

## **AI 原生研究命題**

對 AI 而言，更自然的研究操作可能是：

$$
Navigate
+
Invoke
+
Update
+
Project
+
Compress
$$

而非：

$$
Read\ List
+
Summarize
$$

---

# 43. 結論

本文提出「共同研究時空調用層」（CRSIL），將 CTCL、SGCD、DRC Search、PID、Provenance 與 Function Invocation 整合為一套面向 AI 原生研究的上位方法論。

其核心轉換為：

$$
Document\ Retrieval
\rightarrow
Research\ State\ Navigation
$$

$$
Static\ Search
\rightarrow
Dynamic\ Research\ Field
$$

$$
Tool\ Call
\rightarrow
Spatiotemporal\ Research\ Event
$$

$$
Readable\ Knowledge
\rightarrow
Invocable\ Knowledge
$$

本文最重要的結論是：

> **未來 AI 不應只搜尋「哪篇文件最相關」，而應搜尋「在何時、哪個版本、哪條理論系譜、哪個來源鏈、哪次函數調用與哪個任務條件下，哪些研究狀態值得被激活」。**

因此，未來搜尋的問題可能逐步由：

> 「請給我十個結果。」

轉變為：

> 「請建立此問題的當前研究時空投影，展開候選方向，調用必要工具，保留來源與事件鏈，最後將高共振子圖壓縮為可再次展開的研究結構。」

若此方向成立，則 AI 時代的研究基礎設施不再只是更大的文獻資料庫。

它將逐步接近：

# **可導航、可時間對齊、可版本追蹤、可調用、可驗證、可再次展開的動態研究世界。**

---

# 附錄 A：一句話版本

> **CRSIL 是一種將研究物件、時間、版本、來源、語義耦合、搜尋場與函數調用統一到可追溯動態研究時空中的 AI 原生研究基礎設施方法論。**

---

# 附錄 B：最小公式

$$
\boxed{
CRSIL
=
CTCL
+
SGCD
+
DRC
+
PID
+
Provenance
+
Invocation
}
$$

---

# 附錄 C：最小研究流程

$$
\boxed{
Q
\xrightarrow{CTCL}
Q^\*
\xrightarrow{DRC_D}
\mathcal{B}
\xrightarrow{SGCD}
G_Q(I^\*)
\xrightarrow{Invocation}
G'_Q
\xrightarrow{DRC_R}
G_Q^\*
\xrightarrow{DRC_C}
K_Q
}
$$

---

# 附錄 D：最小研究事件

$$
\boxed{
e_k
=
(
Agent,
Tool,
Input,
I^\*,
Version,
Source,
Output,
Provenance
)
}
$$

---

# 附錄 E：最小全維搜尋向量

$$
\boxed{
\mathbf S
=
(
s_{sem},
s_{temp},
s_{gene},
s_{dep},
s_{contra},
s_{ver},
s_{prov},
s_{evid},
s_{nov},
s_{iso},
s_{task}
)
}
$$

---

# 附錄 F：與既有理論的關係

```text
CTCL
└─ 提供共同參考瞬間、異質時間轉換與版本化時間語義

SGCD
└─ 提供多維耦合、底圖、任務投影與選擇性激活

DRC Search
└─ 提供發散、共振、壓縮與認知場

CRSIL
└─ 將研究物件、Web 狀態、函數調用與上述三者統一為動態研究時空
```

---

# 附錄 G：可直接實作的第一版模組

```text
1. Research Object Registry
2. PID / URI Resolver
3. CTCL Temporal Bundle
4. Version Graph
5. SGCD Coupling Engine
6. DRC Query Divergence
7. Invocation Event Logger
8. Provenance Store
9. Dynamic Research Projection
10. Human Rendering Layer
```

---

# 附錄 H：研究限制聲明

本文不宣稱：

1. 已建立全球通用研究協議；
2. 已證明 CRSIL 優於所有 RAG 或 GraphRAG；
3. 所有研究物件皆具有 DOI；
4. Web 歷史版本皆可取得；
5. 時間 metadata 必然可信；
6. 機器語義耦合等於真實理論關係；
7. 全維搜尋可以無成本執行；
8. AI 可自動完成所有理論去重；
9. 函數調用紀錄自動等於科學重現性。

本文的定位是：

> **提出一個可實作、可分層驗證、可與現有基礎設施對接的 AI 原生研究時空方法論。**

---

# 參考資料與現有基礎設施

1. Crossref. *REST API Documentation*. Crossref 官方文件。  
   https://www.crossref.org/documentation/retrieve-metadata/rest-api/

2. DataCite. *DataCite Metadata Schema 4.7*. 2026.  
   https://schema.datacite.org/

3. DataCite Support. *Versioning*；*Connecting different versions, formats and more with Related Identifiers*.  
   https://support.datacite.org/docs/versioning  
   https://support.datacite.org/docs/connecting-versions-with-related-identifiers

4. OpenAlex. *OpenAlex API Documentation*.  
   https://developers.openalex.org/

5. IETF. RFC 7089. *HTTP Framework for Time-Based Access to Resource States — Memento*.  
   https://datatracker.ietf.org/doc/html/rfc7089

6. W3C. *PROV-DM: The PROV Data Model*.  
   https://www.w3.org/TR/prov-dm/

7. W3C. *PROV-O: The PROV Ontology*.  
   https://www.w3.org/TR/prov-o/

8. Model Context Protocol. *Specification*；*Tools*；*Resources*.  
   https://modelcontextprotocol.io/specification/2025-11-25  
   https://modelcontextprotocol.io/specification/2025-11-25/server/tools  
   https://modelcontextprotocol.io/specification/2025-06-18/server/resources

---

**文件結束**
