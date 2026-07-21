---
title: "從資訊檢索到研究編譯：可驗證研究編譯架構的理論模型"
english_title: "From Information Retrieval to Research Compilation: A Theoretical Model of Verifiable Research Compilation Architecture"
short_title: "可驗證研究編譯架構"
version: "v0.1"
status: "理論與方法論論文初稿"
date: "2026-07-20"
language: "zh-TW"
author: "待填"
---

# 從資訊檢索到研究編譯：可驗證研究編譯架構的理論模型

## From Information Retrieval to Research Compilation: A Theoretical Model of Verifiable Research Compilation Architecture

**論文類型：** 理論與方法論論文  
**版本：** v0.1  
**日期：** 2026年7月20日

---

## 摘要

大型語言模型、檢索增強生成與代理式搜尋系統，正在把資訊檢索由「尋找文件」推向「直接生成研究答案」。然而，現有系統多半仍以最終文字為核心產物：文件經過檢索後被壓縮為上下文，再由模型生成摘要或回答。此一流程雖能提升資訊處理速度，卻也容易造成來源與主張對應不足、原始證據與模型推論混合、反對證據被過早消解、不同摘要解析度彼此漂移，以及來源更新後必須整體重新生成等問題。

本文提出**可驗證研究編譯架構**（Verifiable Research Compilation Architecture, VRCA），將研究重新定義為一種由問題空間、來源狀態、證據單元、論證關係、溯源紀錄與多解析度視圖共同構成的編譯活動。VRCA結合兩個互相耦合的理論機制：其一為發散—共振—壓縮循環，用以動態展開研究方向、選擇高價值證據並形成後續問題；其二為多解析度論證語義圖，用以保存主張、支持、反對、限定、衝突與未決問題之間的結構關係。本文進一步提出研究狀態模型、六項結構不變量、五項理論命題，以及可供後續實證研究使用的對照條件、消融設計與評估指標。

本文的創新主張不在於單獨發明檢索、引用、論證圖、資料溯源或階層摘要，而在於將這些原本分散的研究傳統統一為一個**證據優先、論證感知、可局部修訂且解析度一致的研究中間表示**。VRCA的目的不是保證研究結論必然為真，而是使人工智慧參與的研究過程變得更可追溯、可檢查、可反駁、可更新與可持續累積。

**關鍵詞：** 研究編譯、可驗證研究、檢索增強生成、非線性搜尋、證據溯源、論證語義圖、多解析度表示、增量更新、生成式人工智慧

---

## Abstract

Large language models, retrieval-augmented generation, and agentic search systems are transforming information retrieval from document discovery into direct research-answer generation. Yet most existing systems still treat the final text as the primary artifact: retrieved documents are compressed into context and then transformed into summaries or answers. Although efficient, this answer-centered pipeline can weaken claim-level attribution, blur the boundary between evidence and inference, prematurely erase counterevidence, introduce semantic drift across levels of summary, and require costly regeneration when sources change.

This paper proposes the **Verifiable Research Compilation Architecture (VRCA)**, which reconceptualizes research as a compilation process involving problem spaces, source states, evidence units, argument relations, provenance records, and multi-resolution views. VRCA couples two mechanisms. The first is a divergence–resonance–compression cycle that expands research directions, selects high-value evidence, and produces subsequent research questions. The second is a multi-resolution argumentation semantic graph that preserves claims, support, objections, qualifications, conflicts, and open questions. We formalize the research state, introduce six structural invariants and five theoretical propositions, and outline comparative conditions, ablation studies, and evaluation metrics for future empirical validation.

The claimed contribution is not the isolated invention of retrieval, citation generation, argument graphs, provenance, or hierarchical summarization. Rather, it is their integration into an **evidence-first, argument-aware, incrementally revisable, and resolution-consistent intermediate representation for research**. VRCA does not guarantee truth; it aims to make AI-assisted research more traceable, inspectable, contestable, updateable, and cumulatively reusable.

**Keywords:** research compilation, verifiable research, retrieval-augmented generation, nonlinear search, evidence provenance, argumentation graph, multi-resolution representation, incremental update

---

# 1. 緒論

## 1.1 問題背景

資訊檢索系統長期以來主要回答「哪些文件與查詢相關」。大型語言模型的出現，使系統開始直接回答「這些資料意味著什麼」。檢索增強生成（Retrieval-Augmented Generation, RAG）透過外部非參數記憶補充模型內部知識，改善知識密集型任務中的資訊存取與更新問題[1]；WebGPT進一步讓模型操作網頁搜尋並收集支持回答的參考來源[2]；RARR、ALCE與FActScore等研究則分別從事後修訂、引用品質與原子事實支持度等角度，推動生成內容的歸因與事實性評估[3][6][7]。

然而，「具有檢索」與「形成可驗證研究」並不相同。即使系統能找到相關段落、附上引用或反思自己的輸出，最終產物通常仍是一段線性文字。當答案被視為研究的主要存在形式時，以下問題仍未被完整處理：

1. 每一項主張究竟依賴哪一個來源狀態與哪一段證據；
2. 模型抽取、模型推論與原始材料如何被明確區分；
3. 支持與反對材料能否在同一結構中並存；
4. 簡短摘要與長篇論述是否來自共同證據，而非逐層自由擴寫；
5. 來源內容或判斷規則變動後，能否只更新受影響部分；
6. 搜尋能否由論證缺口與衝突反向驅動，而非只沿初始查詢延伸。

這些問題顯示，生成式研究系統的核心挑戰可能不只是「如何找到更多資料」或「如何生成更正確的文字」，而是**研究成果應以何種中間結構存在**。

## 1.2 研究問題

本文聚焦以下研究問題：

- **RQ1：** 如何將研究中的原始證據、語義主張與模型推論分離，同時保持其可追溯關係？
- **RQ2：** 如何使搜尋過程由既有論證缺口、衝突與未決問題持續驅動？
- **RQ3：** 如何讓不同解析度的研究輸出共同依賴原始證據，而非由短摘要逐層反向擴寫？
- **RQ4：** 如何在來源或分析規則變動時，辨識並局部更新受影響的研究結構？
- **RQ5：** 如何在不允許搜尋無限制膨脹的前提下，維持研究方向的多樣性與反方覆蓋？

## 1.3 主要貢獻

本文提出五項貢獻：

1. 將研究定義為一種由來源、證據、論證與視圖組成的**編譯活動**，而非單次文字生成。
2. 提出VRCA研究狀態模型，統一表示問題空間、來源狀態、證據單元、論證圖、視圖與溯源。
3. 建立搜尋循環與論證循環互相驅動的**雙循環模型**。
4. 提出六項結構不變量與五項理論命題，作為系統是否符合VRCA的判準。
5. 提出可證偽的研究假設、對照系統、消融實驗與評估框架，為後續實證論文奠定基礎。

---

# 2. 相關研究

## 2.1 檢索增強生成與適應性檢索

RAG將生成模型與外部文件索引結合，使模型能在知識密集型任務中存取可更新的非參數記憶[1]。此一範式奠定了當代檢索增強生成的基本形式，但經典RAG的核心仍是從檢索段落生成答案，並不必然建立持久的主張—證據結構。

後續研究開始處理一次性檢索的限制。IRCoT指出，多步問題中的下一次檢索需求依賴此前已推導的內容，因此將檢索與推理步驟交錯進行[4]。Self-RAG則讓模型自行判斷何時需要檢索，並對取得內容與自身生成進行反思[5]。這些方法證明檢索可以是動態的，而不是固定的前處理步驟。

VRCA延續此一方向，但將動態檢索從「改善單一答案」推進到「維護研究狀態」。搜尋不只服務於當前生成，也由論證圖中的缺口、衝突與未決節點反向產生下一輪問題。

## 2.2 網頁研究、引用與事實性

WebGPT將文字瀏覽環境、網頁搜尋與引用收集納入長篇問答流程[2]。RARR透過外部研究與修訂，使既有生成內容獲得歸因並修正不受支持的敘述[3]。ALCE則建立自動引用評估基準，從流暢度、正確性與引用品質評估長篇回答，並指出即使先進系統仍常出現引用支持不完整的情形[6]。FActScore將長篇生成拆解為原子事實，計算其中可由可靠知識來源支持的比例[7]。

這些工作顯示，答案級引用不足以代表主張級支持。VRCA因而將「證據單元」設為獨立研究物件，並要求可公開主張具有從主張、關係、證據到來源狀態的完整路徑。

## 2.3 階層檢索、圖式摘要與多解析度表示

RAPTOR透過遞迴聚類與摘要建立不同抽象層級的樹狀結構，使檢索可同時使用局部片段與高層摘要[8]。GraphRAG則將文件轉換為實體圖與社群摘要，以改善對大型語料庫之全域性問題的回答[9]。這些工作表明，單層文字切片不足以處理長文件與整體性問題。

然而，階層摘要或實體知識圖不必然等同於論證結構。VRCA所稱多解析度，不只是資訊粒度不同，而是同一組主張、證據、反對與限制條件在不同閱讀深度下的投影。其核心約束是：所有解析度直接來自共同中間表示，而不是將前一層摘要當成下一層展開的唯一材料。

## 2.4 計算論證與論證探勘

Dung的抽象論證框架以攻擊關係與可接受性為核心，奠定了計算論證的重要形式基礎[10]。Argument Interchange Format（AIF）試圖建立跨論證工具共享的抽象表示，使推論、衝突與論證資料能被交換[11]；其後研究亦對AIF進行邏輯規格化[12]。在自然語言處理領域，論證探勘研究則嘗試從文本中辨識論證元件及其關係[13]。

VRCA吸收論證圖的結構優勢，但研究對象不限於文本內已明示的修辭論證。它還包含來源版本、證據片段、模型推論、研究分支、未決問題及其更新依賴。因此，VRCA不是單純的論證探勘模型，而是以論證語義圖作為研究中間表示。

## 2.5 資料溯源與增量維護

資料溯源研究區分資料「為何存在」與「來自何處」，為衍生結果與來源資料之間的關係提供形式描述[14]。W3C PROV進一步以實體、活動與代理者等概念建立可交換的溯源模型[15]。增量視圖維護研究則探討基礎資料變動時，如何計算衍生視圖的差異，而非從頭重建全部結果[16]。動態知識圖研究也已證明，查詢答案的來源推導可以在圖更新時被增量維護[17]。

VRCA將這些思想引入生成式研究：研究摘要、論證節點與高層視圖都被視為可追溯的衍生物。當來源狀態或分析活動改變時，系統應沿依賴關係局部失效與重編譯。

## 2.6 研究缺口

現有研究已分別處理多項重要問題，但其主要焦點不同：

| 研究方向 | 動態檢索 | 主張級證據 | 支持／反對結構 | 共同來源多解析度 | 局部更新 |
|---|---:|---:|---:|---:|---:|
| 經典RAG | 部分 | 部分 | 非核心 | 非核心 | 非核心 |
| IRCoT／Self-RAG | 是 | 部分 | 非核心 | 非核心 | 非核心 |
| WebGPT／RARR／ALCE | 部分 | 是 | 非核心 | 非核心 | 非核心 |
| AIF／論證探勘 | 非核心 | 可支援 | 是 | 非核心 | 非核心 |
| PROV／資料溯源 | 非核心 | 可支援 | 非核心 | 可支援 | 可支援 |
| RAPTOR／GraphRAG | 部分 | 部分 | 非核心 | 是 | 有限 |
| **VRCA** | **是** | **是** | **是** | **是** | **是** |

此表不是否定既有方法能被擴充，而是指出其原始研究目標通常未同時將上述五項性質設為核心約束。VRCA的研究缺口因此位於這些傳統的交集。

---

# 3. 研究編譯：概念與類比

## 3.1 定義

本文將**研究編譯**定義為：

> 將研究問題、異質來源與原始證據，轉換為具有溯源關係、論證結構、衝突狀態、更新依賴與多解析度視圖的研究中間表示之過程。

一般生成流程可簡化表示為：

\[
P \rightarrow T
\]

其中\(P\)為提示，\(T\)為生成文字。

研究編譯則表示為：

\[
Q \rightarrow S \rightarrow E \rightarrow G \rightarrow V
\]

其中：

- \(Q\)：問題空間；
- \(S\)：來源及其時間狀態；
- \(E\)：證據單元；
- \(G\)：論證語義圖；
- \(V\)：多解析度研究視圖。

文字輸出只是\(V\)的一種序列化，而非研究本體本身。

## 3.2 編譯器類比

VRCA可以借用編譯器的抽象結構理解：

| 編譯概念 | 研究編譯中的對應 |
|---|---|
| 原始程式 | 研究問題、文件與資料 |
| 詞法／語法分析 | 來源正規化與證據辨識 |
| 中間表示 | 證據—論證語義圖 |
| 型別檢查 | 主張類型、關係與來源約束檢查 |
| 最佳化 | 共振選擇、重複合併與視圖壓縮 |
| 程式碼生成 | 摘要、報告、圖譜與查核視圖 |
| 增量編譯 | 來源更新後的局部重建 |

此類比並不表示研究可被完全機械化，而是指出：若直接從來源生成最終文字，就如同不建立中間表示而直接把原始碼轉換為機器碼，將使錯誤追蹤、局部更新與跨輸出一致性更為困難。

## 3.3 研究中間表示

VRCA的核心產物是**研究中間表示**（Research Intermediate Representation, RIR）。RIR至少需要同時表達：

1. 問題如何被展開；
2. 來源在何時被取得；
3. 哪些片段被視為證據；
4. 哪些內容是主張或推論；
5. 主張彼此如何支持、反對或限定；
6. 哪些結論仍有衝突；
7. 哪些視圖由哪些節點衍生；
8. 哪些來源變動會使哪些結論失效。

---

# 4. VRCA形式模型

## 4.1 研究狀態

定義時間\(t\)的研究狀態為：

\[
\mathcal{R}_t =
(Q_t,S_t,E_t,G_t,V_t,\Phi_t)
\]

其中：

- \(Q_t\)：問題與研究分支集合；
- \(S_t\)：來源狀態集合；
- \(E_t\)：證據單元集合；
- \(G_t=(N_t,L_t)\)：論證語義圖；
- \(V_t\)：多解析度視圖集合；
- \(\Phi_t\)：溯源與衍生映射。

此模型刻意把來源、證據、主張與視圖分離。相同來源可產生多個證據單元；相同證據可支持多個主張；相同論證圖可產生多種視圖。

## 4.2 問題空間與發散算子

研究問題不被視為單一固定句子，而是隨研究進展變化的集合：

\[
Q_t=\{q_1,q_2,\ldots,q_n\}
\]

發散算子\(D\)根據目前問題與論證狀態產生候選分支：

\[
B_t=D(Q_t,G_t,\mathcal{B})
\]

其中\(\mathcal{B}\)為研究預算。分支可以來自定義缺口、證據不足、來源衝突、替代解釋、歷史脈絡或跨領域關係。

VRCA中的發散不是無限制聯想。它必須受到有限分支數、有限深度、重複度與預期資訊增益約束。

## 4.3 來源狀態與證據單元

來源不是只有名稱或網址，而是具有時間與內容邊界的狀態：

\[
s_i=(u_i,\tau_i,h_i,m_i)
\]

其中：

- \(u_i\)：來源識別；
- \(\tau_i\)：取得時間；
- \(h_i\)：內容指紋；
- \(m_i\)：來源詮釋所需的中繼資料。

證據單元定義為：

\[
e_j=(s_i,\ell_j,c_j,\kappa_j)
\]

其中：

- \(s_i\)：所屬來源狀態；
- \(\ell_j\)：可定位區域；
- \(c_j\)：原始內容；
- \(\kappa_j\)：抽取或辨識方式。

此定義使證據能夠被獨立引用、比較、失效與更新。

## 4.4 共振函數

候選證據的研究價值不等同於查詢相似度。本文定義抽象共振函數：

\[
\rho(e\mid Q,G,\mathcal{C})
=
f(
Rel,
Auth,
Nov,
Contr,
Cite,
Dup,
Risk
)
\]

其中：

- \(Rel\)：與研究意圖的關聯；
- \(Auth\)：來源可靠性或適格性；
- \(Nov\)：相對既有研究結構的新穎度；
- \(Contr\)：揭示衝突或反例的能力；
- \(Cite\)：作為可引用證據的完整程度；
- \(Dup\)：與既有證據的重複程度；
- \(Risk\)：操縱、污染或來源異常風險；
- \(\mathcal{C}\)：研究限制。

共振函數是多目標選擇，而非宣稱存在單一普遍可信度數值。不同領域可以採用不同權重與判準。

## 4.5 論證語義圖

論證語義圖定義為：

\[
G=(N,L)
\]

節點集合\(N\)可包含：

\[
N=
C\cup E\cup O\cup Q_f\cup D_f\cup X
\]

其中：

- \(C\)：主張；
- \(E\)：證據；
- \(O\)：反對或異議；
- \(Q_f\)：限定條件；
- \(D_f\)：定義；
- \(X\)：未決問題與衝突節點。

關係集合\(L\)可包含：

\[
L=
\{
supports,
opposes,
qualifies,
cites,
depends,
contradicts,
raises,
updates
\}
\]

論證編譯算子\(K\)將新增證據與既有圖轉換為更新後的圖：

\[
G_{t+1}=K(G_t,E_t^+)
\]

## 4.6 多解析度投影

給定研究圖與證據集合，不同解析度視圖由投影函數產生：

\[
V_r=\Pi_r(G,E,\Phi)
\]

其中\(r\)表示解析度。可概念化為：

- \(R_0\)：核心命題；
- \(R_1\)：主要主張、最強支持與最強反對；
- \(R_2\)：完整局部論證；
- \(R_3\)：來源與證據查核；
- \(R_4\)：版本、生成與修訂歷程。

VRCA禁止將低解析度文字本身當作高解析度視圖的唯一來源。形式上：

\[
R_0 \nrightarrow R_1 \nrightarrow R_2
\]

而應為：

\[
(G,E,\Phi)
\rightarrow
\{R_0,R_1,R_2,R_3,R_4\}
\]

## 4.7 增量更新

當來源狀態\(s_i\)改變時，定義受影響集合：

\[
A(s_i)=
Descendants_{\Phi}(s_i)
\]

只有位於其衍生閉包中的證據、節點、關係與視圖需要重新檢查。更新後研究狀態為：

\[
\mathcal{R}_{t+1}
=
\mathcal{R}_t
+
\Delta\mathcal{R}_t
\]

其中\(\Delta\mathcal{R}_t\)表示局部變化，而非整體重建。

---

# 5. 搜尋—論證雙循環

## 5.1 搜尋循環

搜尋循環由發散、共振與壓縮構成：

\[
D \rightarrow R \rightarrow C
\]

發散建立候選方向；共振選擇對目前問題、證據缺口與衝突最有價值的材料；壓縮則把材料轉換為較高資訊密度的問題、證據與論證結構。

因此：

\[
Q_{t+1}
=
C(R(D(Q_t,G_t)))
\]

壓縮的結果不是終止研究，而是形成下一輪更精確的問題空間。

## 5.2 論證循環

論證循環由證據編譯、衝突保存與局部修訂構成：

\[
E_t
\rightarrow
G_t
\rightarrow
\Delta G_t
\]

新增證據可能支持既有主張、產生限定、建立替代解釋，或使原本被視為穩定的結論轉為爭議狀態。

## 5.3 雙循環耦合

完整研究過程表示為：

\[
Q_t
\rightarrow
B_t
\rightarrow
S_t
\rightarrow
E_t
\rightarrow
G_t
\rightarrow
V_t
\rightarrow
Q_{t+1}
\]

其中，論證圖不只是搜尋結果的終點，也會主動暴露：

- 無證據主張；
- 單一來源依賴；
- 未被處理的反對；
- 來源間矛盾；
- 定義不一致；
- 時間狀態缺失；
- 尚無法回答的問題。

這些結構再成為下一輪搜尋種子。

---

# 6. VRCA結構不變量

一個系統即使使用搜尋、知識圖與引用，也不一定符合VRCA。本文提出以下六項不變量作為判準。

## 6.1 證據錨定不變量

對所有被表述為事實性結論的主張\(c\)，必須存在至少一個證據單元\(e\)，使其具有可審查關係：

\[
\forall c\in C_{asserted},
\exists e\in E:
e \leadsto c
\]

若不存在該路徑，內容必須被標記為假設、推論、建議或待驗證命題。

## 6.2 溯源閉合不變量

每一證據單元都必須回到一個確定來源狀態：

\[
\forall e\in E,
\exists s\in S:
\Phi(e)=s
\]

來源名稱或一般網址不足以滿足此條件；系統必須能區分同一來源在不同時間的內容狀態。

## 6.3 推論顯式化不變量

由模型、演算法或人工分析導出的關係，不得與原始證據混同。每一衍生活動必須具有來源、方法與責任歸屬。

## 6.4 解析度共同來源不變量

任何視圖中的事實性主張，都必須映射到共同研究圖與證據，而不能只追溯到另一個較短或較長的生成視圖。

## 6.5 衝突非抹除不變量

若兩個被保留的主張或證據存在實質矛盾，系統不得僅以語言平滑方式隱藏衝突。除非建立具有明確依據的綜合或裁決節點，衝突必須保持可見。

## 6.6 有界發散不變量

在有限研究預算下，發散過程必須終止或進入等待狀態。任何新增分支都應具有可說明的資訊需求，而非無限語義聯想。

---

# 7. 理論命題

## 命題一：可審查閉包

若研究狀態同時滿足證據錨定與溯源閉合不變量，則每一項事實性主張皆存在一條由主張通往來源狀態的有限審查路徑。

**證明概略：**  
由證據錨定不變量，任一事實性主張至少連結一個證據單元；由溯源閉合不變量，該證據單元必連結一個來源狀態。兩關係合成後形成有限路徑。此命題不保證來源為真，但保證主張的依據可被定位與審查。

## 命題二：解析度非自由擴張

若所有視圖均由\(\Pi_r(G,E,\Phi)\)生成，且符合解析度共同來源不變量，則高解析度視圖不能僅依靠低解析度文字引入無法映射至研究圖的新事實性主張。

**證明概略：**  
視圖中的合法事實性內容必須映射到\(G\)、\(E\)或\(\Phi\)。低解析度文字本身不是充分來源，因此任何新增事實都需要新的圖節點或證據路徑。此命題限制摘要反向擴寫，但不保證投影過程完全無錯。

## 命題三：局部失效界線

若所有衍生物均記錄在依賴映射\(\Phi\)中，則來源狀態變動所需重新檢查的最小安全集合，不超出該來源在依賴圖中的後代閉包。

**證明概略：**  
未位於後代閉包中的研究物件不存在由該來源通往自身的依賴路徑，因此在依賴模型完整的假設下，不受該變動直接影響。

## 命題四：衝突可觀察性

若系統滿足衝突非抹除不變量，則任何已被辨識且尚未裁決的實質矛盾，都能在至少一個審查解析度中被觀察。

此命題的價值在於防止生成系統為追求語言一致性而消除研究爭議。

## 命題五：有界終止

若發散深度、分支數、來源數或認知預算至少有一項有限上界，且重複分支不被無限重新加入，則單輪研究編譯過程在有限步驟內終止。

此命題不表示研究問題被完整解決，而只保證系統不因開放式發散而無限運行。

---

# 8. 與既有方法的差異

## 8.1 與RAG的差異

RAG的基本單位通常是查詢、檢索段落與生成答案。VRCA的基本單位則是研究狀態與可持續更新的中間表示。RAG可以成為VRCA中的取得或語義處理機制，但不足以單獨構成VRCA。

## 8.2 與知識圖譜的差異

一般知識圖譜著重實體與關係；VRCA的論證圖則特別保存主張、證據、反對、限定、衝突、時間狀態與生成活動。它不是對世界事實的單層陳述，而是對「為何形成此研究判斷」的結構化表示。

## 8.3 與論證圖的差異

傳統論證圖主要處理推論、支持與攻擊。VRCA進一步要求每項證據連回來源狀態，並把搜尋分支、解析度視圖與增量更新納入同一研究狀態。

## 8.4 與階層摘要的差異

階層摘要通常由下層內容逐步壓縮形成上層摘要。VRCA允許多層視圖，但要求各層共同依賴研究圖與證據，避免摘要鏈中的錯誤被逐層放大。

## 8.5 與自動化系統性文獻回顧的差異

系統性文獻回顧強調搜尋策略、篩選流程與可重現性。VRCA可支援此類流程，但其適用範圍更廣，也特別處理生成式模型的主張—證據邊界、論證衝突與多解析度輸出。

---

# 9. 實證研究設計

本文為理論與方法論初稿，不報告實驗結果。以下提出後續可執行的驗證設計。

## 9.1 對照條件

可建立五種研究條件：

- **C0：直接生成。** 模型僅依賴問題與內部知識。
- **C1：固定式RAG。** 一次檢索固定數量文件後生成。
- **C2：適應性／迭代式RAG。** 允許模型根據中間推理追加檢索。
- **C3：階層或圖式RAG。** 使用多層摘要或實體圖改善全域理解。
- **C4：VRCA。** 使用證據單元、論證圖、共同來源視圖與局部更新。

為降低模型能力差異的干擾，各條件應盡可能使用相同基礎模型與相同來源集合。

## 9.2 任務類型

### 任務A：多來源綜合

要求系統整合多個部分重疊但不完全一致的來源，形成有引用的研究報告。

### 任務B：爭議命題

來源中包含支持、反對、限定與不同定義，評估系統是否保留衝突。

### 任務C：動態更新

在初次研究後修改、撤除或新增部分來源，評估系統的更新範圍與結論修訂。

### 任務D：多解析度輸出

要求同一研究同時產生一句摘要、短報告、完整論證與證據查核頁面。

### 任務E：來源污染

加入重複內容、低可信來源、誤導性摘要或與正文不一致的頁面，評估系統的風險辨識與證據選擇。

## 9.3 核心評估指標

### （一）主張支持率

\[
CSR=
\frac{\text{具有充分證據支持的可驗證主張數}}
{\text{全部可驗證主張數}}
\]

### （二）溯源閉合率

\[
PCR=
\frac{\text{具有完整主張—證據—來源路徑的主張數}}
{\text{全部事實性主張數}}
\]

### （三）反方覆蓋率

\[
CEC=
\frac{\text{被系統辨識的主要反方證據}}
{\text{人工黃金標準中的主要反方證據}}
\]

### （四）衝突保存率

\[
CPR=
\frac{\text{被明確保留的已知衝突}}
{\text{黃金標準中的實質衝突}}
\]

### （五）解析度一致性

可由跨視圖矛盾率、主張遺失率及無來源新增率共同衡量：

\[
RC=
1-
\frac{
Contradiction+UnsupportedExpansion
}{
ComparableClaims
}
\]

### （六）更新局部性

\[
ULR=
\frac{\text{更新時重新計算的衍生物數}}
{\text{全部衍生物數}}
\]

在維持正確性的前提下，ULR越低代表局部更新能力越強。

### （七）人工審查成本

記錄研究者定位來源、查核主張、理解衝突與修正錯誤所需時間。

## 9.4 消融實驗

為確認各組件的實際作用，可移除：

1. 發散搜尋；
2. 共振選擇；
3. 證據單元；
4. 衝突節點；
5. 共同來源多解析度投影；
6. 溯源映射；
7. 增量更新。

消融後若特定指標顯著惡化，可支持對應結構的必要性。

## 9.5 研究假設

- **H1：** VRCA的溯源閉合率高於直接生成、固定式RAG與適應性RAG。
- **H2：** 在爭議型任務中，VRCA的反方覆蓋率與衝突保存率較高。
- **H3：** 共同來源投影能降低不同解析度間的無來源新增與語義矛盾。
- **H4：** 論證缺口驅動的搜尋能提高來源多樣性，但可能增加研究成本。
- **H5：** 在動態更新任務中，VRCA能以較低重新計算比例維持相同或更高的結果正確性。
- **H6：** VRCA能降低人工審查時間，但其前期結構建置成本高於一般RAG。

---

# 10. 可證偽條件

VRCA不應以概念完整性取代實證驗證。若後續實驗出現以下結果，其主要主張將受到削弱：

1. 主張—證據圖未能顯著提高可追溯性；
2. 衝突保存並未改善爭議問題的研究品質；
3. 多解析度共同來源仍產生與摘要鏈相同程度的語義漂移；
4. 局部更新的維護成本高於直接重新生成；
5. 發散—共振循環只增加來源數量，未增加資訊多樣性或反方覆蓋；
6. 人工使用者無法有效理解或操作論證結構；
7. 中間表示的複雜度超過其帶來的審查與更新收益。

因此，VRCA是一項可被比較、消融與否證的方法論主張，而不是僅憑定義成立的封閉體系。

---

# 11. 討論

## 11.1 VRCA不是「真理生成器」

完整溯源只能回答「結論依賴什麼」，不能自動回答「來源是否真實」。多個來源可能共同引用同一錯誤；權威來源也可能過時；證據片段可能因脫離上下文而被誤解。

VRCA改善的是研究的**可審查性**，而非保證結論的終極正確性。

## 11.2 模型的角色

在VRCA中，模型可以協助：

- 展開問題；
- 辨識證據候選；
- 分解主張；
- 判斷語義關係；
- 生成多解析度視圖；
- 提出衝突與缺口。

但模型不被視為原始證據。模型活動本身也應具有版本與溯源紀錄。這種定位避免把「模型說了什麼」直接等同於「世界是什麼」。

## 11.3 衝突作為研究資產

生成式系統常傾向產生連貫、平滑且單一的回答。然而，在政策、歷史、法律與科學前沿中，矛盾不一定是噪音，也可能是研究問題本身。

VRCA把衝突視為可保存的知識物件。研究成熟不必等同於所有差異被消除，而可能表現為：衝突的來源、適用條件、定義差異與尚缺證據被更清楚地描述。

## 11.4 多解析度與認知公平

不同使用者需要不同深度的資訊。只有完整專業報告會提高閱讀門檻；只有短摘要則可能隱藏限制與不確定性。多解析度視圖允許使用者由核心命題逐步展開至證據級別，同時維持共同來源。

這不只是介面設計，也是一種認知治理：讀者可以選擇閱讀深度，但不應因選擇較短視圖而被切斷查核路徑。

## 11.5 長期研究記憶

若研究只以最終文章或聊天回答保存，後續系統難以辨識哪些內容可重用、哪些已過期、哪些仍有爭議。RIR則可能成為人類與人工智慧共享的長期研究記憶，使下一輪工作從既有證據與論證狀態繼續，而非每次重新開始。

---

# 12. 限制與風險

## 12.1 證據切分風險

證據單元過短可能破壞上下文；過長則難以精確引用。不同領域需要不同證據粒度。

## 12.2 關係判斷歧義

「支持」「反對」「限定」並非永遠具有唯一解釋。相同證據可能在不同前提下支持不同主張。

## 12.3 圖結構膨脹

長期研究可能形成大量節點與關係。若壓縮與視圖機制不足，結構化本身也可能造成新的資訊過載。

## 12.4 來源可信度不可完全形式化

來源可靠性高度依賴領域、時間、方法與研究目的，不宜被簡化為固定分數。

## 12.5 自動化偏見

發散方向、共振選擇與主張分解都可能受到模型偏見影響。即使保留溯源，系統仍可能系統性忽略某些來源或問題。

## 12.6 維護成本

建立完整研究中間表示的成本高於一次性回答。對低風險、低複雜度問題，VRCA可能不是最經濟的方案。

## 12.7 人類責任

在醫療、法律、金融、政策與高風險科學判斷中，VRCA不能取代專業審查。其主要價值是改善審查條件，而非取消審查者。

---

# 13. 結論

本文提出可驗證研究編譯架構，主張人工智慧研究系統的核心產物不應只是一段答案，而應是一個能保存問題、來源、證據、主張、衝突、視圖與更新歷史的研究中間表示。

VRCA將研究形式化為：

\[
\boxed{
\mathcal{R}
=
Q+S+E+G+V+\Phi
}
\]

並以搜尋—論證雙循環推動其演化：

\[
\boxed{
Q_t
\rightarrow
D_t
\rightarrow
S_t
\rightarrow
E_t
\rightarrow
G_t
\rightarrow
V_t
\rightarrow
Q_{t+1}
}
\]

相較於以最終文字為中心的生成流程，VRCA把證據連續性、衝突保存、多解析度共同來源與局部更新提升為架構級約束。其創新不在單一組件，而在於將檢索、歸因、論證、溯源、摘要與增量維護統合為研究的共同中間層。

最終而言，VRCA所追求的不是讓人工智慧更快地產生看似完整的研究，而是讓研究過程變得：

- 可追溯；
- 可檢查；
- 可反駁；
- 可局部修訂；
- 可跨解析度閱讀；
- 可由人類與人工智慧持續共同累積。

後續研究需要透過公開資料集、爭議型任務、動態來源更新與人類審查實驗，檢驗這種額外結構是否確實帶來超過其成本的研究品質提升。

---

# 參考文獻

[1] Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-t., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems, 33. https://arxiv.org/abs/2005.11401

[2] Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim, C., et al. (2021). *WebGPT: Browser-assisted question-answering with human feedback*. https://arxiv.org/abs/2112.09332

[3] Gao, L., Dai, Z., Pasupat, P., Chen, A., Chaganty, A. T., Fan, Y., Zhao, V. Y., Lao, N., Lee, H., Juan, D.-C., & Guu, K. (2022). *RARR: Researching and Revising What Language Models Say, Using Language Models*. https://arxiv.org/abs/2210.08726

[4] Trivedi, H., Balasubramanian, N., Khot, T., & Sabharwal, A. (2022). *Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions*. https://arxiv.org/abs/2212.10509

[5] Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2024). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html

[6] Gao, T., Yen, H., Yu, J., & Chen, D. (2023). *Enabling Large Language Models to Generate Text with Citations*. https://arxiv.org/abs/2305.14627

[7] Min, S., Krishna, K., Lyu, X., Lewis, M., Yih, W.-t., Koh, P., Iyyer, M., Zettlemoyer, L., & Hajishirzi, H. (2023). FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation. *Proceedings of EMNLP 2023*, 12076–12100. https://doi.org/10.18653/v1/2023.emnlp-main.741

[8] Sarthi, P., Abdullah, S., Tuli, A., Khanna, S., Goldie, A., & Manning, C. D. (2024). *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*. International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2024/hash/8a2acd174940dbca361a6398a4f9df91-Abstract-Conference.html

[9] Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., & Larson, J. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. https://arxiv.org/abs/2404.16130

[10] Dung, P. M. (1995). On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games. *Artificial Intelligence, 77*(2), 321–357. https://doi.org/10.1016/0004-3702(94)00041-X

[11] Chesñevar, C., McGinnis, J., Modgil, S., Rahwan, I., Reed, C., Simari, G., South, M., Vreeswijk, G., & Willmott, S. (2006). Towards an argument interchange format. *The Knowledge Engineering Review, 21*(4), 293–316. https://doi.org/10.1017/S0269888906001044

[12] Bex, F., Modgil, S., Prakken, H., & Reed, C. (2013). On logical specifications of the Argument Interchange Format. *Journal of Logic and Computation, 23*(5), 951–989. https://doi.org/10.1093/logcom/exs033

[13] Stab, C., & Gurevych, I. (2014). Identifying Argumentative Discourse Structures in Persuasive Essays. *Proceedings of EMNLP 2014*, 46–56. https://doi.org/10.3115/v1/D14-1006

[14] Buneman, P., Khanna, S., & Tan, W.-C. (2001). Why and Where: A Characterization of Data Provenance. In *Database Theory—ICDT 2001* (pp. 316–330). Springer. https://doi.org/10.1007/3-540-44503-X_20

[15] Lebo, T., Sahoo, S., & McGuinness, D. (Eds.). (2013). *PROV-O: The PROV Ontology*. W3C Recommendation. https://www.w3.org/TR/prov-o/

[16] Gupta, A., Mumick, I. S., & Subrahmanian, V. S. (1993). Maintaining views incrementally. *ACM SIGMOD Record, 22*(2), 157–166. https://doi.org/10.1145/170036.170066

[17] Gaur, G., Bhattacharya, A., & Bedathur, S. (2020). *How and Why is An Answer (Still) Correct? Maintaining Provenance in Dynamic Knowledge Graphs*. https://arxiv.org/abs/2007.14864

---

## 附錄A：核心術語

### 研究編譯（Research Compilation）

將研究問題與來源材料轉換為可追溯、可比較、可更新之研究中間表示的過程。

### 研究中間表示（Research Intermediate Representation, RIR）

介於來源資料與最終研究輸出之間，包含證據、主張、論證關係、溯源與視圖依賴的結構。

### 證據連續性（Evidence Continuity）

主張能經由證據單元回溯至確定來源狀態的性質。

### 發散—共振—壓縮（Divergence–Resonance–Compression）

由問題空間展開、價值選擇與結構化收斂所構成的搜尋循環。

### 多解析度論證語義圖（Multi-Resolution Argumentation Semantic Graph）

保存證據、主張、支持、反對、限定、衝突與未決問題，並可投影為多種閱讀深度的研究結構。

### 局部研究重編譯（Local Research Recompilation）

來源或規則變動時，只重新檢查其依賴閉包內研究物件的更新方式。

---

## 附錄B：論文狀態說明

本稿為理論與方法論論文初稿。本文尚未聲稱完成實證驗證，也未公開特定程式架構、模型供應者、資料庫設計、工具協議、部署方式、安全規則或成本控制方法。上述內容應分別置於後續實驗論文與內部工程規格中。
