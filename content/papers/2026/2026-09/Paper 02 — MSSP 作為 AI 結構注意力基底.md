# Paper 02 — MSSP 作為 AI 結構注意力基底

## MSSP as an AI Structural Attention Substrate

**系列：** TDD × MSSP Architecture Backtrace and Fresh Reconstruction  
**系列代號：** ABFR Series  
**文件版本：** v0.1  
**日期：** 2026-08-28  
**作者：** Neo.K / EveMissLab  

---

## 摘要

MSSP（Mother-Set and Subset Paradigm，母集與子集範式）最初處理的是大型軟體與 Agent 專案超出人類工作記憶後的結構性問題：當一個系統包含多種角色、外部工具、風險層級、可替換能力、權限邊界與長期演化狀態時，開發者不再能以「整個系統同時存在於腦中」作為可靠維護方式。MSSP 因此將系統狀態拆成可被觀察、選取、載入、驗證與治理的結構邊界，使人類可以只複查與當前任務相關的 subset，降低全域認知複查成本。

本文提出一個由 AI 工程實務反向揭露的新用途：同一套原本為人類「少看一點」而設計的結構，可能被 AI 用來「有秩序地看完更多」。對 AI 而言，MSSP 不只是一種模組化方法，也可以成為 **structural attention substrate（結構注意力基底）**：AI 不必一次將整個 repository、全部規格、所有執行歷史與權限規則同時塞入有限 context，而可以沿著顯式架構實體、關係、角色、權限、證據、狀態與 governance event 選擇子集，執行局部推理，保留結構化中間結果，再進行跨子集 reconciliation。本文將此過程稱為 **Structured Global Attention（結構化全域注意力）**。

本文不主張 MSSP 發明了 selective context、hierarchical memory、graph memory 或 long-context agent memory management。2025–2026 年的 Agent memory 研究已經明確展示主動記憶操作、依賴結構化 context、階層式資訊隔離、多圖記憶與可學習的記憶管理。本文所主張的研究差異是：MSSP 的 traversal object 不是主要由對話歷史、episodic memory 或語義相似度形成的記憶條目，而是**軟體架構本身的可治理狀態**。這些狀態攜帶 responsibility、authority、dependency、declared/observed/effective distinction、evidence 與 lifecycle semantics，因此 AI 的 context selection 可以被架構不變量約束，也可以產生可重播、可攻擊與可治理的架構推理證據。

本文建立 Human Cognitive Review Reduction 與 AI Structural Attention Traversal 的雙重解釋，提出 context utility density、structural coverage、revisit cost、attention contamination、reconciliation debt 與 traversal completeness 等候選量測；並說明其如何支援 ABFR（Architecture Backtrace and Fresh Reconstruction）的架構回溯與 fresh reconstruction。最後，本文提出可被後續跨 AI 實驗驗證的假說：在大型 repository 上，architecture-guided subset traversal 應能以低於無結構全量複讀的 context 成本，維持或提高 hidden dependency discovery、architecture drift detection 與 fresh replay correctness。

**關鍵詞：** MSSP；AI Agent；Context Management；Structural Attention；Software Architecture；Cognitive Offloading；Long-Horizon Reasoning；Architecture Traversal；ABFR；Structured Global Attention

---

# 1. 從「人腦裝不下整個專案」開始

MSSP 的起點不是模型容量，而是人類工程實務。

一個小型專案的早期狀態通常近似：

$$
K_{\text{project}}
\subseteq
W_{\text{human}}
$$

其中：

- $K_{\text{project}}$ 是維護專案所需的有效知識集合；
- $W_{\text{human}}$ 是當下可動用的人類工作記憶與注意力範圍。

在專案仍小時，作者可以大致知道：

- 哪個檔案做什麼；
- 哪個模組可以替換；
- 哪些規則不能違反；
- 哪個修改可能影響哪裡；
- 哪些操作具有風險；
- 哪些狀態只是暫時的。

但當專案增長後：

$$
|K_{\text{project}}|
\gg
|W_{\text{human}}|
$$

「理解整個專案」開始退化成：

$$
\text{I know the system}
\rightarrow
\text{I remember the region I touched recently}
$$

MSSP Field Manual 對這個轉折點的工作定義非常直接：

> 不是把程式切碎，而是讓狀態的邊界可以被看見與操作。

因此 MSSP 的原始工程收益可表為：

$$
\boxed{
\text{Global Review Burden}
\rightarrow
\text{Relevant Structural Subset}
}
$$

如果當前任務只需要一個能力，Agent 或人類不應被迫載入所有無關能力、所有規則與所有歷史。

MSSP 在 1.x Field Manual 中甚至直接定義了 context utility density：

$$
\rho_q
=
\frac{I_{\text{task relevant}}}
{I_{\text{loaded}}}
$$

理想情況為：

$$
\rho_q \rightarrow 1
$$

這一公式原本描述的是 context 不應被無關資訊稀釋。

本文的核心觀察是：對 AI 而言，這個式子還可以向另一個方向推進。

---

# 2. 原始目的：Human Cognitive Review Reduction

先不討論 AI，MSSP 的第一層價值可以描述成 **Human Cognitive Review Reduction**。

令整個系統為：

$$
S
=
\{
s_1,s_2,\ldots,s_n
\}
$$

某個任務 $q$ 真正需要的結構集合為：

$$
S_q
\subseteq
S
$$

傳統全量複查近似要求：

$$
\operatorname{Review}(q)
=
\operatorname{Load}(S)
$$

MSSP 希望改成：

$$
\operatorname{Review}(q)
=
\operatorname{Load}(S_q)
$$

因此若：

$$
|S_q|
\ll
|S|
$$

則有：

$$
C_{\text{review}}(S_q)
<
C_{\text{review}}(S)
$$

其中 $C_{\text{review}}$ 可以包含：

- 閱讀時間；
- working-memory switching；
- 無關資訊干擾；
- 重新定位 dependency 的成本；
- 規則衝突的誤判；
- 人工回憶歷史決策的成本。

這和 cognitive offloading 的一般思想相容。認知卸載研究長期指出，人類會將原本需要內部維持或操作的資訊外部化，以降低任務的認知需求；近年的回顧也持續把 externalization、working-memory limitation 與 task performance 連結起來。

MSSP 可以被理解為軟體工程中的一種**結構化認知外部化**：

$$
\text{Implicit Architecture in Human Memory}
\rightarrow
\text{Explicit Operable Architecture State}
$$

但 MSSP 比一般文件外部化多了一層要求：

$$
\boxed{
\text{Externalized State}
\neq
\text{Passive Documentation Only}
}
$$

因為其邊界應該能被：

- 選取；
- 載入；
- 執行；
- 驗證；
- 拒絕；
- 比較；
- 演化。

所以真正重要的不是「人不用記住所有資訊」，而是「被外部化的架構狀態仍具有操作語義」。

---

# 3. AI 看見的是另一個問題

對人類而言，MSSP 的自然使用方式是：

$$
S
\rightarrow
S_q
\rightarrow
\text{Inspect}
\rightarrow
\text{Decide}
$$

目的主要是**避免不必要的全域注意力**。

但 AI coding agent 面臨的限制不同。

AI 的問題不是單純「記不住」，而是：

1. context window 有限；
2. context 越長，無關資訊競爭越明顯；
3. 工具輸出與 execution trace 會持續污染 working context；
4. repository-wide 任務經常需要跨多個區域推理；
5. 單次 retrieval 很難保證涵蓋完整 dependency chain；
6. 過度壓縮可能丟失後續才會需要的結構關係；
7. 模型可以重複讀取，但重複讀取有 token、時間與注意力成本。

因此 AI 不一定需要：

$$
\operatorname{Load}(S)
$$

而可以執行：

$$
S_1
\rightarrow
S_2
\rightarrow
\cdots
\rightarrow
S_n
$$

每次只處理有限子集，並把中間結果外部化。

換言之：

$$
\boxed{
\text{Avoid Global Attention}
\rightarrow
\text{Construct Global Understanding by Traversal}
}
$$

這是本文提出的核心反轉。

---

# 4. Structured Global Attention

本文將這種使用模式稱為：

## Structured Global Attention

它不是指 Transformer 中某種新的 attention mechanism，而是系統層的 Agent context orchestration 方法。

定義一個架構圖：

$$
G
=
(V,E)
$$

其中 $V$ 可以包含：

$$
V=
\{
\text{Entity},
\text{Role},
\text{State},
\text{Evidence},
\text{GovernanceEvent},
\ldots
\}
$$

而 $E$ 可以表示：

$$
E=
\{
\text{depends-on},
\text{owns},
\text{reads},
\text{writes},
\text{authorizes},
\text{observes},
\text{replaces},
\text{evidences},
\ldots
\}
$$

Agent 不必一次載入：

$$
G
$$

而可以在第 $t$ 步選擇：

$$
G_t
\subseteq
G
$$

使得：

$$
G_t
=
\operatorname{Select}
(
q,
G,
M_{t-1},
A,
R
)
$$

其中：

- $q$：當前問題；
- $M_{t-1}$：先前 traversal 留下的結構化記錄；
- $A$：authority constraints；
- $R$：架構不變量與 routing rule。

完成局部推理後：

$$
M_t
=
\operatorname{Update}
(
M_{t-1},
\operatorname{Reason}(G_t)
)
$$

接著再決定下一個 subset。

因此整體理解不是由一次 context load 建立，而是：

$$
\boxed{
\text{Select}
\rightarrow
\text{Attend}
\rightarrow
\text{Record}
\rightarrow
\text{Traverse}
\rightarrow
\text{Reconcile}
}
$$

這正是本文所稱的 AI Structural Attention。

---

# 5. 這不是 Long Context 的同義詞

最直接的替代方案似乎是：

> 既然 context window 越來越大，直接把 repository 全塞進去即可。

但兩者處理的是不同問題。

令 context window 容量為：

$$
W
$$

當：

$$
|S| \leq W
$$

也不代表：

$$
\operatorname{Utility}(S)=\operatorname{Utility}(S_q)
$$

因為容量足夠只表示資訊可以被放進去，不表示所有資訊對當前推理都有同等價值。

甚至：

$$
I_{\text{loaded}}
\uparrow
$$

可能導致：

$$
\rho_q
=
\frac{I_{\text{task relevant}}}
{I_{\text{loaded}}}
\downarrow
$$

因此問題不是：

$$
\text{Can the model hold it?}
$$

而是：

$$
\text{What should be active now, and why?}
$$

Structured Global Attention 的目標是把「選什麼」從非結構化 retrieval 變成架構可解釋決策。

---

# 6. 這也不是一般 RAG

RAG 的典型問題是：

$$
q
\rightarrow
\operatorname{Retrieve}(D)
\rightarrow
\operatorname{Generate}
$$

如果 retrieval 主要依賴 lexical 或 semantic similarity，則容易得到「看起來相關」但不是結構上必要的內容。

例如修復一個 deployment bug 時，最相似的文件不一定是：

- 實際授權 deployment 的 policy；
- 產生 config 的 module；
- runtime 中真正 effective 的 environment source；
- 最近一次 governance event；
- 失敗 evidence 所屬的 snapshot。

MSSP / SSD 式 traversal 可以要求：

$$
\text{Relevant}
\neq
\text{Semantically Similar Only}
$$

而是：

$$
\text{Relevant}
=
f(
\text{Dependency},
\text{Authority},
\text{Responsibility},
\text{State},
\text{Evidence},
\text{Lifecycle},
\text{Task}
)
$$

因此它可以和 RAG 結合，但不等同於 RAG。

---

# 7. 與 2025–2026 Agent Memory 研究的關係

這個研究方向必須嚴格承認既有進展。

## 7.1 MemoryOS

MemoryOS 將 Agent 記憶做成短期、中期與長期層級，並透過 storage、updating、retrieval 與 generation 管理跨互動資訊。

它證明：

$$
\text{Agent Memory}
\neq
\text{One Flat Context}
$$

這與 MSSP 的 subset / layer intuition 相容，但主要研究對象仍是 Agent memory。

---

## 7.2 AgeMem

AgeMem 將長短期記憶操作直接納入 Agent policy，使 Agent 自己選擇：

$$
\{
\text{store},
\text{retrieve},
\text{update},
\text{summarize},
\text{discard}
\}
$$

並以學習方式優化長期任務中的 context 使用。

這證明主動 context management 已經能成為 Agent 行為的一部分，而不是固定 heuristic。

---

## 7.3 Memory-R1

Memory-R1 同樣讓 Agent 主動管理 external memory，將 ADD、UPDATE、DELETE、NOOP 等操作結構化，說明記憶本身可以被視為可操作狀態。

---

## 7.4 ContextWeaver

ContextWeaver 特別接近本文的部分問題。它指出單純 sliding window、compression 或 retrieval 可能漏掉多步推理所依賴的因果與邏輯結構，因此建立 dependency-structured interaction graph，沿 dependency 選擇未來推理所需 context。

這和 MSSP Structural Attention 的共同點是：

$$
\boxed{
\text{Dependency Structure Matters}
}
$$

差異則在 traversal object。

ContextWeaver 主要構造 reasoning / interaction trace 的 dependency graph。

MSSP / ABFR 關心的是：

$$
\text{Software Structural State}
$$

也就是 repository、module、service、contract、authority、runtime state、evidence 與 governance relation。

---

## 7.5 MAGMA

MAGMA 將 Agent memory 放在多個正交圖上，包括 semantic、temporal、causal 與 entity graph，並以 traversal 建構 context。

這再次說明：

$$
\text{Graph Traversal}
$$

已是 Agent memory 的重要方向。

因此本文不主張 graph traversal 是新概念。

MSSP 的候選新意在於：

$$
\boxed{
\text{Architecture Graph}
+
\text{Governance Semantics}
+
\text{Executable Invariants}
}
$$

被直接作為 coding / architecture Agent 的 context routing substrate。

---

## 7.6 HyMem

HyMem 透過 information isolation 將 long-horizon Agent context 分成不同功能層，避免 detail-heavy execution trace 壓過高階規劃資訊。

這和 MSSP 的基本直覺高度一致：

$$
\text{Different Information Roles}
\Rightarrow
\text{Different Context Treatment}
$$

但 MSSP 更強調角色與權限是架構語義，而不只是 context 儲存層級。

---

# 8. MSSP 的差異：Context Object 是 Architecture State

如果只說：

> MSSP 可以幫 AI 管理 context。

那並不足以構成新的研究命題。

真正需要固定的是：

$$
\boxed{
\text{What is being scheduled?}
}
$$

一般 Agent memory scheduling 的物件可能是：

- message；
- summary；
- fact；
- event；
- episodic memory；
- reasoning step；
- embedding chunk。

MSSP Structural Attention 所排程的是：

$$
\boxed{
\text{Governable Architecture State}
}
$$

其基本 primitive 在 Dynamic MSSP / SSD 中可抽象為：

$$
\{
\text{Entity},
\text{Relation},
\text{Role},
\text{Authority},
\text{Evidence},
\text{State},
\text{GovernanceEvent}
\}
$$

額外可包含：

$$
\{
\text{Compensation},
\text{Burden},
\text{Context},
\text{Snapshot}
\}
$$

這使每次 context selection 都可以回答：

1. 為什麼這個 entity 被載入？
2. 它對當前 task 負責什麼？
3. 它能改什麼？
4. 它依賴誰？
5. 哪個 claim 是 declared？
6. 哪個 fact 是 observed？
7. 哪個 conclusion 是 effective？
8. 證據來自哪個 snapshot / event？
9. 是否存在 unresolved divergence？
10. 下一個應該 traversal 的 structural frontier 在哪裡？

這些問題不是一般 similarity retrieval 自動提供的。

---

# 9. Declared / Observed / Effective 作為 Attention Axis

Dynamic MSSP / SSD 的一個關鍵區分是：

$$
A_d
=
\text{Declared Architecture}
$$

$$
A_o
=
\text{Observed Architecture}
$$

$$
A_e
=
\text{Effective Architecture}
$$

這個區分對 AI context routing 特別重要。

假設某模組宣告：

$$
Role(m)=TMS
$$

但 runtime observation 顯示：

$$
\operatorname{Centrality}(m)
\uparrow
$$

而多個核心 path 都實際依賴它。

若 Agent 只讀 declared layer，它會得到：

$$
m=\text{optional}
$$

若 Agent 只讀 observed layer，又可能錯把暫時 traffic pattern 當成架構決策。

因此 attention 應該同時載入：

$$
\{
A_d(m),
A_o(m),
E(m)
\}
$$

再由 governance semantics 推論：

$$
A_e(m)
$$

所以：

$$
\boxed{
\text{Observed}
\neq
\text{Effective}
}
$$

也表示：

$$
\boxed{
\text{Attention Routing}
\neq
\text{Telemetry Ranking}
}
$$

這對 architecture-wide reasoning 很關鍵。

---

# 10. Evidence 不是附註，而是 Attention Navigation

在一般文件系統中，evidence 經常只是「參考資料」。

但在 MSSP / SSD 中，evidence 可以是結構圖上的一等節點。

若一個 claim $c$ 具有 evidence：

$$
e \rightarrow c
$$

Agent 可以追問：

$$
\operatorname{about}(e)
$$

$$
\operatorname{subject}(e)
$$

$$
\operatorname{snapshot}(e)
$$

$$
\operatorname{time}(e)
$$

從而避免將：

- 舊事件證據；
- 錯誤 subject 的證據；
- 已失效 waiver；
- 不同 snapshot 的 observation；

混成同一個 architecture claim。

因此 Evidence-aware traversal 可以寫成：

$$
G_{t+1}
=
\operatorname{Expand}
(
G_t,
\text{unresolved claims},
\text{evidence edges}
)
$$

這使「下一步要讀什麼」不只由語義相關性決定，而由**尚未閉合的架構主張**決定。

---

# 11. Authority 也是 Context Boundary

對 coding agent 而言，知道某件事與有權執行某件事是不同概念。

因此：

$$
\text{Knowledge}
\neq
\text{Authority}
$$

MSSP 的 SCL 與後續 SSD Authority primitive 允許：

$$
\operatorname{CanRead}(a,x)=1
$$

同時：

$$
\operatorname{CanWrite}(a,x)=0
$$

這件事對 Structural Attention 有兩層意義。

第一，Agent 可以讀取完整架構知識，但仍受到操作邊界限制。

第二，context routing 本身也可以被 authority 限制：

$$
G_t
\subseteq
G_{\text{visible}(a)}
$$

所以 attention substrate 不只是「幫 AI 找資料」，而是：

$$
\boxed{
\text{Context Selection}
+
\text{Authority-Constrained Action}
}
$$

這讓它更接近 architecture runtime，而不是 retrieval plugin。

---

# 12. 從 Subset Loading 到 Architecture Traversal

MSSP Field Manual 的一個核心要求是：可替換能力應能在最小核心下被單獨載入與測試。

早期可以寫成：

$$
SMS
+
TMS_i
$$

並要求：

$$
TMS_j
\notin
\operatorname{LoadedSet},
\quad
j\neq i
$$

這原本是 isolation test。

但對 AI 而言，可以將它提升為 traversal primitive。

例如：

$$
L_1
=
SMS+TMS_1
$$

$$
L_2
=
SMS+TMS_2
$$

$$
\vdots
$$

$$
L_n
=
SMS+TMS_n
$$

Agent 可以逐一：

$$
\operatorname{Inspect}(L_i)
$$

並建立：

$$
M_i=
\{
\text{dependencies},
\text{authority},
\text{invariants},
\text{evidence},
\text{failures}
\}
$$

最後：

$$
M_G
=
\operatorname{Reconcile}
(
M_1,\ldots,M_n
)
$$

因此原本用來降低單次複查成本的 subset isolation，成為建立 global architecture understanding 的遍歷單位。

---

# 13. AI Structural Attention 的五階段模型

本文提出 v0.1 五階段模型：

## Stage 1 — Select

根據 task、architecture frontier 與 unresolved claim 選擇下一個 subset。

$$
S_t
=
\operatorname{Select}(q,F_t)
$$

其中 $F_t$ 為 traversal frontier。

---

## Stage 2 — Attend

將：

$$
S_t
$$

及其必要 dependency / authority / evidence 載入 active context。

要求盡量最大化：

$$
\rho_q
$$

同時避免遺失 structural necessity。

---

## Stage 3 — Record

把局部推理結果外部化為結構化記錄，而非只留在聊天 context。

例如：

$$
R_t=
\{
\text{claim},
\text{evidence},
\text{dependency},
\text{divergence},
\text{next frontier}
\}
$$

---

## Stage 4 — Traverse

依：

$$
R_t
$$

選擇下一個必要 subset，而不是回到 repository root 重新搜尋。

---

## Stage 5 — Reconcile

當局部 traversal 足夠後，比較：

$$
A_d,
A_o,
A_e
$$

並建立全域 structural summary。

如果存在衝突：

$$
A_d
\neq
A_o
$$

則不能只做摘要，而必須產生 unresolved governance item。

---

# 14. 不是「把所有摘要加起來」

一個重要風險是將 Structured Global Attention 誤解成：

$$
\text{Global Understanding}
=
\sum_i
\text{Local Summary}_i
$$

這通常不成立。

因為跨 subset relation 可能只在 reconciliation 時出現。

例如：

$$
TMS_A
\rightarrow
SMS
\leftarrow
TMS_B
$$

分別閱讀 $TMS_A$ 與 $TMS_B$ 都可能看起來完全正常。

但如果實際存在：

$$
TMS_A
\rightarrow
TMS_B
$$

hidden coupling 只有在：

$$
\operatorname{Compare}(A,B)
$$

或 dependency graph reconciliation 時才會出現。

因此：

$$
\boxed{
\text{Traversal}
+
\text{Reconciliation}
>
\text{Independent Summarization}
}
$$

這也是 ABFR 能利用 MSSP 的原因。

---

# 15. Structural Attention 與 Architecture Backtrace

Paper 01 定義 ABFR 的第一個方向：

$$
P
\rightarrow
A_e
\rightarrow
A_o
\rightarrow
A_d
$$

若沒有 Structural Attention substrate，AI 進行 architecture backtrace 時可能只能：

1. 全量讀取 repository；
2. 反覆 grep；
3. 依語義搜尋找可能相關檔案；
4. 在有限 context 中維持大量中間依賴；
5. 多輪後重新讀取已經看過的區域。

MSSP Structural Attention 則可以提供：

$$
G_{\text{architecture}}
$$

以及：

$$
F_0
=
\text{target output / failure / claim}
$$

然後：

$$
F_{t+1}
=
\operatorname{Parents}
(
F_t
)
\cup
\operatorname{Evidence}
(
F_t
)
\cup
\operatorname{Authority}
(
F_t
)
$$

直到：

$$
F_t
=
\varnothing
$$

或達到指定 structural closure criterion。

因此：

$$
\boxed{
\text{ABFR Backtrace}
\text{ can be implemented as }
\text{governed architecture traversal}
}
$$

---

# 16. Structural Attention 與 Fresh Reconstruction

ABFR 的另一半是 fresh reconstruction。

假設已回溯得到最小充分結構：

$$
S^*
$$

Fresh Reconstruction 不再需要重新把整個 repository 語義化理解一次，而可以依：

$$
S^*
$$

建立 reconstruction plan：

$$
S^*
\rightarrow
\{
\text{required source},
\text{required config},
\text{required authority},
\text{required state},
\text{required tests}
\}
$$

新的 AI session 可以被限制只接收 canonical structural state，再逐步載入必要 subset。

因此 Fresh Replay 同時測兩件事：

$$
\text{Architecture Reconstructibility}
$$

與：

$$
\text{Attention Route Sufficiency}
$$

若新的 Agent 必須額外詢問作者：

> 還有哪個檔案？

或：

> 原來這裡還需要上一個 workspace 的 cache？

則表示：

$$
S^*
$$

並不充分。

---

# 17. 候選量測一：Context Utility Density

沿用 MSSP 既有：

$$
\rho_q
=
\frac{I_{\text{task relevant}}}
{I_{\text{loaded}}}
$$

但若要做跨 AI 實驗，必須把 relevance 操作化。

可以暫定：

$$
I_{\text{task relevant}}
=
\sum_{x\in C}
w(x)\cdot \mathbf{1}[x\in G^*]
$$

其中：

- $C$：實際載入 context；
- $G^*$：事後確認對任務必要或具有效用的 structural set；
- $w(x)$：資訊權重。

因此：

$$
\rho_q
=
\frac{
\sum_{x\in C}
w(x)\mathbf{1}[x\in G^*]
}{
\sum_{x\in C}w(x)
}
$$

這只是第一版，不能把 relevance 當成容易取得的 ground truth；但可以用人工標註、dependency trace 或 controlled benchmark 近似。

---

# 18. 候選量測二：Structural Coverage

Context 很乾淨不代表架構理解完整。

因此還需要：

$$
\kappa_s
=
\frac{
|G_{\text{visited}}\cap G^*|
}{
|G^*|
}
$$

其中：

- $G_{\text{visited}}$：Agent 實際 traversal 到的必要 structural items；
- $G^*$：benchmark 已知的 target structural set。

理想情況是：

$$
\rho_q
\uparrow
$$

同時：

$$
\kappa_s
\uparrow
$$

若只有 $\rho_q$ 高而 $\kappa_s$ 低，Agent 可能只是讀得很少，但漏掉重要結構。

---

# 19. 候選量測三：Revisit Cost

Agent 在 long-horizon coding 任務中常出現：

> 前面讀過，但現在又要重新讀。

令某 structural item $x$ 被重新載入的次數為：

$$
r(x)
$$

則：

$$
C_{\text{revisit}}
=
\sum_x
\max(0,r(x)-1)\cdot c(x)
$$

其中 $c(x)$ 可以是 token 或 wall-clock cost。

若 Structured Record 有效，應有：

$$
C_{\text{revisit}}
\downarrow
$$

但不能以犧牲 correctness 為代價。

---

# 20. 候選量測四：Attention Contamination

若 active context 中包含與當前 task 不相關、且可能產生錯誤 steering 的規則或歷史，可定義 contamination：

$$
\chi_q
=
\frac{
I_{\text{irrelevant or conflicting}}
}{
I_{\text{loaded}}
}
$$

理想上：

$$
\chi_q
\rightarrow 0
$$

並有：

$$
\rho_q+\chi_q
\not\equiv 1
$$

因為某些資訊可能中性、備援或 relevance 未知。

這避免把所有「暫時沒用到」的資訊都直接分類成污染。

---

# 21. 候選量測五：Reconciliation Debt

如果 AI 做了很多局部 summary，卻沒有處理跨 subset 衝突，就會累積：

$$
D_R
$$

本文稱為 Reconciliation Debt。

令 unresolved cross-subset claims 集合為：

$$
U
$$

每一個 claim 的風險權重為：

$$
w(u)
$$

則：

$$
D_R
=
\sum_{u\in U}w(u)
$$

一個 traversal 可以 context 很省、局部答案都正確，仍然因：

$$
D_R
\gg 0
$$

而不能稱為全域架構理解完成。

---

# 22. 候選量測六：Traversal Completeness

對 architecture task $q$，若存在預先定義 structural frontier expansion rule：

$$
\Phi
$$

則可以測：

$$
\tau_q
=
\frac{
|\text{resolved required frontier}|
}{
|\text{required frontier}|
}
$$

在 controlled benchmark 中， $\tau_q$ 可以由 injected dependency / known mutation 決定。

在真實 repository 中，只能用近似值，不應假裝能知道絕對完整的 architecture ground truth。

---

# 23. 一個更完整的效用函數

因此 AI Structural Attention 的效用不能只最佳化 token。

可以暫寫成：

$$
U_{\text{SAT}}
=
\alpha\rho_q
+
\beta\kappa_s
+
\gamma\tau_q
-
\delta C_{\text{revisit}}
-
\epsilon\chi_q
-
\zeta D_R
$$

其中：

$$
\alpha,\beta,\gamma,\delta,\epsilon,\zeta
\geq 0
$$

不同任務可以有不同權重。

例如 security / authority audit 應提高：

$$
\beta,\gamma,\zeta
$$

而快速小型修復可能更重視：

$$
\alpha,\delta
$$

本文不主張這個效用函數已經成熟；它的作用是指出：

$$
\boxed{
\text{Context Efficiency}
\neq
\text{Minimum Tokens Only}
}
$$

---

# 24. Human 與 AI 的成本函數不同

這個反轉之所以會被忽略，是因為 MSSP 最初面向的成本函數偏人類。

人類進行完整 architecture-wide review 的成本可近似寫成：

$$
C_H
=
C_{\text{reading}}
+
C_{\text{switching}}
+
C_{\text{working memory}}
+
C_{\text{reconstruction}}
+
C_{\text{fatigue}}
$$

而 AI 的成本近似：

$$
C_A
=
C_{\text{tokens}}
+
C_{\text{tool calls}}
+
C_{\text{latency}}
+
C_{\text{context degradation}}
+
C_{\text{revisit}}
$$

這兩者不是誰「比較聰明」的直接比較，而是工作特性的差異。

AI 特別適合：

$$
\boxed{
\text{Repeated Structured Traversal}
}
$$

因為它可以多次：

$$
\operatorname{Load}
\rightarrow
\operatorname{Compare}
\rightarrow
\operatorname{Record}
$$

而不必要求一個人類工程師在每個 milestone 都重新完整複查數百個結構節點。

因此最值得研究的命題不是：

> AI 能做人做不到的架構審查。

而是：

> AI 能否把人類理論上做得到、但成本高到不會高頻執行的架構複查，降成 routine engineering operation。

---

# 25. 從 Rare Architecture Audit 到 Routine Revalidation

傳統 architecture review 經常發生在：

- 系統重大重構；
- production incident；
- ownership transition；
- security audit；
- 技術債爆發；
- migration；
- 新架構師接手。

原因不是 review 沒價值，而是：

$$
C_H
$$

太高。

如果 Structural Attention 能降低 AI 的 architecture-wide traversal cost，則：

$$
\text{Rare Architecture Audit}
\rightarrow
\text{Routine Structural Revalidation}
$$

就可能成為現實。

這正好與 Paper 01 的 ABFR gate 接軌：

$$
\text{TDD}
\rightarrow
\text{Structural Traversal}
\rightarrow
\text{Architecture Backtrace}
\rightarrow
\text{Fresh Reconstruction}
$$

AI 不是只負責寫 code，而是負責重複驗證：

$$
\text{What system did we actually build?}
$$

---

# 26. MSSP Structural Attention 的最低條件

為避免把任何「AI 讀很多檔案」都叫 MSSP Structural Attention，本文提出 v0.1 最低條件。

## SA-1 Explicit Structural Units

系統必須存在可識別 architecture units。

不要求使用 FMS/SMS/TMS 名稱，但不能只有一堆無結構 chunk。

---

## SA-2 Explicit Relations

至少一部分 dependency、authority、responsibility 或 evidence relation 必須可查詢。

---

## SA-3 Selective Loading

Agent 可以只載入 task-relevant subset。

若每次都必須載入整個系統，則沒有 structural scheduling。

---

## SA-4 Structured Record

局部 traversal 結果必須外部化，不能只存在模型暫時 context。

---

## SA-5 Reconciliation

多個 subset 結果必須能被比較、合併與標記衝突。

---

## SA-6 Evidence Traceability

非顯然的 architecture claim 應能指向 evidence 或標示 unresolved。

---

## SA-7 Authority Separation

知道某結構不自動授予修改它的權力。

---

## SA-8 Replayability

同一 structural route 至少應能被另一執行者重新走過，否則它仍只是一次性的模型行為。

---

# 27. 失敗模式

Structural Attention 也可能失敗。

## F1. Over-Partitioning

subset 太碎：

$$
|S_i|\rightarrow 1
$$

導致 relation reconstruction cost 暴增。

---

## F2. Under-Partitioning

subset 太大：

$$
S_i\approx S
$$

失去 selective loading 的意義。

---

## F3. Stale Structural Map

架構圖仍是舊狀態。

$$
A_d
\neq
A_o
$$

但 Agent 只依 $A_d$ routing。

---

## F4. Retrieval Myopia

只沿一種 relation，例如 import graph，漏掉 authority、runtime state 或 external dependency。

---

## F5. Summary Collapse

局部 record 過度壓縮，使後續 reconciliation 無法重建關鍵因果。

---

## F6. Reconciliation Starvation

Agent 一直 traversal 新 subset，卻從不回頭解跨 subset 衝突。

---

## F7. Evidence Drift

證據存在，但不是關於目前 snapshot / subject / event。

---

## F8. Authority Confusion

Agent 把「知道怎麼做」誤判為「被允許做」。

---

## F9. Context Echo

結構化 record 被反覆重新摘要，逐輪產生資訊漂移。

---

## F10. False Globality

Agent traversal 很多 subset，卻沒有 predefined coverage / frontier semantics，最後以主觀感覺宣稱「全域理解完成」。

---

# 28. 與 MSSP 原始 Context Utility Density 的延伸關係

MSSP 1.x 已經把 context 視為：

- 有容量；
- 有成本；
- 有注意力競爭；
- 有污染風險。

因此：

$$
\rho_q
=
\frac{I_{\text{task relevant}}}
{I_{\text{loaded}}}
$$

不是 Paper 02 事後附會的概念，而是 MSSP 原始 Agent 時代定位的一部分。

本文真正新增的是：

$$
\boxed{
\rho_q
\text{ can be optimized locally while }
\kappa_s
\text{ is accumulated globally}
}
$$

即：

$$
\text{Local Context Efficiency}
+
\text{Global Structural Coverage}
$$

可以同時存在。

這可以寫成：

$$
\boxed{
\text{Structured Global Attention}
=
\text{High Local Utility Density}
+
\text{Cumulative Structural Coverage}
+
\text{Cross-Subset Reconciliation}
}
$$

這比「把更多 token 放進 context」更接近本文想研究的對象。

---

# 29. 與 ABFR 的直接整合

Paper 01 提出：

$$
G_{\text{architecture}}
=
C_B
\land
C_S
$$

其中：

$$
C_B
=
\text{Behavioral Closure}
$$

而：

$$
C_S
=
\text{Structural Reconstruction Closure}
$$

Paper 02 補上的問題是：

> AI 要怎麼以可控制成本完成 $C_S$ 所需的 architecture-wide backtrace？

本文回答：

$$
\boxed{
\text{MSSP Structural Attention}
}
$$

可以作為第一個候選 substrate。

因此：

$$
\text{TDD}
\rightarrow
\text{MSSP Structural Traversal}
\rightarrow
\text{ABFR Backtrace}
\rightarrow
\text{Fresh Reconstruction}
\rightarrow
\text{Replay}
$$

更完整地：

$$
\boxed{
\text{Behavioral Validation}
+
\text{Structured Architecture Attention}
+
\text{Reconstruction Validation}
}
$$

形成下一階段方法論的主軸。

---

# 30. 可證偽假說

Paper 02 不應只停在概念美感，因此提出以下候選假說。

## H1 — Context Efficiency

在相同 repository 與 architecture task 下：

$$
C_{\text{tokens}}^{\text{MSSP-guided}}
<
C_{\text{tokens}}^{\text{global reread}}
$$

且 correctness 不降低。

---

## H2 — Hidden Dependency Detection

在注入已知 hidden coupling 的 benchmark 中：

$$
P_{\text{detect}}^{\text{structural traversal}}
>
P_{\text{detect}}^{\text{semantic retrieval only}}
$$

---

## H3 — Reduced Revisit Cost

若 traversal result 被結構化記錄：

$$
C_{\text{revisit}}^{\text{recorded}}
<
C_{\text{revisit}}^{\text{chat-context only}}
$$

---

## H4 — Better Fresh Replay

以 architecture-guided reconstruction plan 執行 fresh replay 時：

$$
P_{\text{fresh success}}^{\text{structured}}
>
P_{\text{fresh success}}^{\text{unstructured handoff}}
$$

---

## H5 — Cross-Agent Transfer

不同模型在只接受相同 canonical MSSP state 時，應能獨立走出高度重疊的必要 structural frontier。

令兩個 Agent 的必要節點集合為：

$$
V_A,V_B
$$

可測：

$$
J(A,B)
=
\frac{|V_A\cap V_B|}
{|V_A\cup V_B|}
$$

但高 overlap 不是唯一目標；更重要的是是否都覆蓋 injected critical nodes。

---

## H6 — MSSP Taxonomy Independence

若把 FMS/SMS/TMS 等名稱換成另一個 semantic-compatible profile，但保留：

$$
\{
\text{Entity},
\text{Relation},
\text{Responsibility},
\text{Authority},
\text{Evidence},
\text{State}
\}
$$

則 Structural Attention 應仍能運作。

若失敗，表示本文方法仍過度依賴特定 taxonomy。

---

# 31. 後續實驗設計

Paper 05 與 Spec B 將正式定義跨 AI protocol；本文先固定最重要的 control。

至少比較：

$$
G_0=\text{Full / naïve repository reread}
$$

$$
G_1=\text{Semantic retrieval}
$$

$$
G_2=\text{Dependency retrieval}
$$

$$
G_3=\text{MSSP structural traversal}
$$

並控制：

- 同一 repository；
- 同一 task；
- 同一 test baseline；
- 同一 fresh session policy；
- 相同工具權限；
- 相同輸出要求。

主要量測：

$$
\{
\rho_q,
\kappa_s,
C_{\text{revisit}},
\chi_q,
D_R,
\tau_q
\}
$$

再加上最終工程結果：

- hidden dependency detection；
- architecture drift detection；
- fresh reconstruction success；
- replay pass rate；
- mutation kill rate；
- required human intervention count。

---

# 32. 為什麼這個發現容易被作者忽略

這個方法論反轉具有一個一般性的設計現象。

系統作者通常以原始痛點定義工具效用。

若原始痛點為：

$$
C_{\text{human review}}
\gg 0
$$

自然會把 MSSP 看成：

$$
\text{Cognitive Reduction Tool}
$$

但 AI 使用者面對的是不同成本函數。

AI 看見的不是：

> 我怎麼少讀一點？

而可能是：

> 既然每一塊都已經能單獨被識別、載入、驗證與記錄，我能不能把所有必要的塊依結構順序重新走完？

這是一個典型的 affordance inversion：

$$
\boxed{
\text{Designed Affordance}
\rightarrow
\text{Discovered Secondary Affordance}
}
$$

原始 affordance：

$$
\text{Reduce Review Scope}
$$

次級 affordance：

$$
\text{Enable Systematic Global Traversal}
$$

兩者來自完全相同的結構性質。

---

# 33. 對「AI 很聰明」的技術化描述

本文不需要把這個發現人格化。

更精確地說，某些 AI coding agent 已經能進行：

$$
\boxed{
\text{Methodological Composition}
}
$$

也就是從環境中已有的兩個方法：

$$
M_1=\text{TDD}
$$

$$
M_2=\text{MSSP}
$$

推導出：

$$
M_3=
\operatorname{Compose}(M_1,M_2)
$$

其中 $M_3$ 的使用方式並未被 $M_1$ 或 $M_2$ 的作者預先完整寫出。

Paper 01 處理的是：

$$
\text{TDD}
+
\text{MSSP Replay}
\rightarrow
\text{Architecture-Level Revalidation}
$$

Paper 02 則解釋為什麼這個組合對 AI 特別自然：

$$
\text{MSSP Subsets}
\rightarrow
\text{AI Traversal Units}
$$

也就是 AI 把人類的 cognitive offloading structure 重新投影成自己的 attention orchestration structure。

---

# 34. 不宣稱事項

本文明確不宣稱：

1. MSSP 是第一個 selective-context architecture。
2. MSSP 發明 hierarchical memory。
3. MSSP 發明 graph traversal。
4. AI Agent 必須使用 MSSP 才能管理大型 repository。
5. 更大 context window 沒有價值。
6. RAG、graph memory 或 learned memory policy 可以被 MSSP 取代。
7. Structured Global Attention 是新的 Transformer attention mechanism。
8. AI 可以取得完整、無遺漏的 global architecture ground truth。
9. 所有 structural state 都應進入 persistent memory。
10. 任意 subset traversal 都會比 full-context reading 更好。
11. 已有一個 Agent 的成功案例足以證明通用方法成立。
12. Human Cognitive Review Reduction 與 AI Structural Attention 的效益已被同一組實驗證明。

本文真正提出的是一個待驗證命題：

$$
\boxed{
\text{An architecture representation designed for human cognitive reduction may also serve as an AI traversal substrate.}
}
$$

---

# 35. 下一步

Paper 03 將把本文的 traversal substrate 接到 ABFR 的正式方法核心：

## Architecture Backtrace and Fresh Reconstruction

其重點包括：

- Architecture State Model；
- declared / observed / effective formal relation；
- Minimal Sufficient Reconstruction Set；
- backtrace frontier；
- reconstruction boundary；
- replay equivalence；
- unresolved claim semantics；
- failure taxonomy；
- freshness contract。

Paper 04 再加入：

$$
C_D
=
\text{Discriminative Closure}
$$

要求任何 architecture validator 不只會通過 canonical state，也必須能被已知 mutation 證明會失敗。

最後 Paper 05 與 Cross-AI Protocol 才真正回答：

> 這是不是只有某一個 AI 偶然想到、偶然做得到？

或：

> 其他 AI 在 fresh condition 下，也能否把 MSSP 當成 architecture-wide structural attention substrate？

---

# 36. 結論

MSSP 最初處理的是一個很實際的人類問題：

$$
|K_{\text{project}}|
\gg
|W_{\text{human}}|
$$

因此它將大型系統的狀態邊界外部化，使：

$$
\text{Global System}
\rightarrow
\text{Relevant Subset}
$$

成為可操作的工程行為。

對人類而言，這降低認知複查成本。

但對 AI 而言，同一結構可以被重新使用：

$$
S_1
\rightarrow
S_2
\rightarrow
\cdots
\rightarrow
S_n
\rightarrow
\operatorname{Reconcile}
$$

於是：

$$
\boxed{
\text{Human Cognitive Reduction}
\rightarrow
\text{AI Structured Global Attention}
}
$$

這裡的「Global」並不表示一次把全部資訊放進 context，而是透過高效的局部 attention 與累積 structural coverage，建立可重播的全域理解。

因此本文提出：

$$
\boxed{
\text{Structured Global Attention}
=
\text{Selective Structural Loading}
+
\text{Persistent Structured Record}
+
\text{Governed Traversal}
+
\text{Cross-Subset Reconciliation}
}
$$

MSSP 的潛在第二生命週期，也因此不只是「幫 Agent 少讀一些文件」。

它可能成為：

$$
\boxed{
\text{AI Architecture Attention Substrate}
}
$$

使 AI 能把過去對人類而言成本過高、通常只在重大事故或重構時才進行的全域架構複查，逐步轉換成 milestone-level 的 routine structural revalidation。

如果這個假說在跨 AI、跨 repository、跨架構 profile 的 fresh experiments 中成立，那麼 MSSP 的價值就會從「複雜度管理方法」再向前推一步：

> 它不只讓大型系統可以被局部理解，也可能讓大型系統可以被機器有秩序地重新理解。

---

# 參考文獻

[1] Risko, E. F., & Gilbert, S. J. (2016). *Cognitive Offloading*. Trends in Cognitive Sciences, 20(9), 676–688. DOI: 10.1016/j.tics.2016.07.002.

[2] Skulmowski, A. (2023). *The Cognitive Architecture of Digital Externalization*. Educational Psychology Review, 35, Article 101. DOI: 10.1007/s10648-023-09818-1.

[3] Guo, Y., & Ye, Q. (2026). *Meta-cognitive insights into cognitive offloading: mechanisms, interventions, and educational implications*. Humanities and Social Sciences Communications, 13, Article 772.

[4] Chen, O., Allen, R., Waterman, A., et al. (2026). *The Relationship Between Cognitive Offloading and the Transient Information Effect*. Educational Psychology Review, 38, Article 35. DOI: 10.1007/s10648-026-10132-9.

[5] Kang, J., Ji, M., Zhao, Z., & Bai, T. (2025). *Memory OS of AI Agent*. Proceedings of EMNLP 2025.

[6] Yu, Y., Yao, L., Xie, Y., Tan, Q., Feng, J., Li, Y., & Wu, L. (2026). *Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents*. Proceedings of ACL 2026, 21457–21483. DOI: 10.18653/v1/2026.acl-long.981.

[7] Yan, S., Yang, X., Huang, Z., Nie, E., Ding, Z., Li, Z., Ma, X., Bi, J., Kersting, K., Pan, J. Z., Schuetze, H., Tresp, V., & Ma, Y. (2026). *Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning*. Proceedings of ACL 2026.

[8] Wu, Y., Zhang, Y., Ghosh, S., Basu, S., Deoras, A., Huan, J., & Gupta, G. (2026). *ContextWeaver: Selective and Dependency-Structured Memory Construction for LLM Agents*. arXiv:2604.23069.

[9] Jiang, D., Li, Y., Li, G., & Li, B. (2026). *MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents*. Proceedings of ACL 2026.

[10] Wang, X., Xiao, J., Cui, S., Zhang, H., Wang, Y., Zhang, Q., & Xu, B. (2026). *HyMem: Hierarchical Context Management for Long-Horizon Agents via Information Isolation*. arXiv:2608.15703.

[11] Neo.K / EveMissLab. (2026). *MSSP Field Manual 01 — 從這裡開始*. MSSP 1.x public field manual, thisoneisneok.com, accessed 2026-08-28.

[12] Neo.K / EveMissLab. (2026). *MSSP Field Manual 02 — 架構與模式*. MSSP 1.x public field manual, thisoneisneok.com, accessed 2026-08-28.

[13] Neo.K / EveMissLab. (2026). *MSSP Field Manual 06 — 迭代授權：SSD / Dynamic MSSP 工程規格與 MVP v0.1*. thisoneisneok.com, accessed 2026-08-28.

[14] Neo.K / EveMissLab. (2026). *MSSP 開發日誌*. thisoneisneok.com, accessed 2026-08-28.

---

## Canonical status

本文為 **ABFR Series Paper 02 v0.1**。

目前狀態：

- Conceptual model: complete for v0.1.
- Human cognitive reduction interpretation: grounded in existing MSSP design and cognitive-offloading literature.
- AI structural attention interpretation: proposed.
- Cross-AI validation: pending.
- Repository benchmark validation: pending.
- Structural-attention metric validation: pending.
- Generalization beyond MSSP taxonomy: pending.

後續若實驗顯示 Structured Global Attention 無法穩定降低 context / revisit cost，或不能提高 structural coverage，應修改或拒絕本文相關假說；不得因方法由 MSSP 推導而預設其成立。
