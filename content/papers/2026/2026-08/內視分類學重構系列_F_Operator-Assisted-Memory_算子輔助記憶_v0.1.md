# Operator-Assisted Memory
## 算子標籤、混合檢索與可解釋 AI 知識導航

**中文題名：** 算子輔助記憶：算子標籤、混合檢索與可解釋 AI 知識導航  
**作者：** Neo.K（許筌崴）  
**AI 協作：** GPT-5.6 Thinking  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 內部研究論文／內視分類學重構系列應用論文 F  
**版本：** v0.1  
**日期：** 2026-07-31  
**狀態：** 系統架構、資料模型與實驗設計；尚未完成大規模實作驗證  
**取代關係：** 本文取代《內視記憶系統：基於坐標化的 AI 知識管理框架》作為目前正式基線；舊 IMS 保留為歷史探索版本  
**前置文件：**
1. 《內視分類學的算子論》  
2. 《第一人稱可及性與公共不可觀察性》  
3. 《內視算子代數》  
4. 《宗教與神秘體驗的算子比較》  
5. 《內感—呼吸—動作耦合》

---

## 摘要

本文提出 Operator-Assisted Memory（OAM，算子輔助記憶），作為舊版 Inner-View Memory System（IMS）的重構版本。舊 IMS 將文檔映射到七維坐標，主張具有明確認知語義的低維坐標可以取代或超越高維向量嵌入，並能以坐標距離實現精確檢索、可解釋導航及從「RAG 1.0」到「RAG 2.0」的範式轉移。該設計包含一項仍具價值的直覺：AI 知識系統不應只能回答「哪份文本最相似」，還應支援「更抽象」「更具體」「更接近原始來源」「更偏實證」「查看反例」「沿依賴向上」等方向性導航。然而，舊版把七個人工坐標視為完整語義空間，並在沒有實驗結果的情況下宣稱其在精度、可解釋性與擴展性上優於傳統 RAG，這些強主張必須撤回。

OAM 不以算子標籤取代向量嵌入，而採用多表示、多索引與自適應路由架構。每個知識物件 $d$ 被表示為：

$$
\mathcal{K}(d)
=
\left(
E_d,
L_d,
\Phi_d,
G_d,
P_d,
V_d,
S_d,
C_d
\right)
$$

其中：

- $E_d$ ：dense semantic embedding；
- $L_d$ ：sparse lexical representation；
- $\Phi_d$ ：內視算子及知識操作標籤；
- $G_d$ ：概念、命題、依賴及引用圖；
- $P_d$ ：來源與 provenance；
- $V_d$ ：版本與時間狀態；
- $S_d$ ：認識狀態；
- $C_d$ ：存取、可見性及領域條件。

查詢不再只被映射成一個向量，而被編譯為查詢計畫：

$$
\mathcal{Q}(q)
=
\left(
q_{\mathrm{lex}},
q_{\mathrm{sem}},
q_{\mathrm{op}},
q_{\mathrm{graph}},
q_{\mathrm{epi}},
q_{\mathrm{version}},
q_{\mathrm{route}}
\right)
$$

不同查詢可以自適應選擇：

- sparse retrieval；
- dense retrieval；
- hybrid fusion；
- operator filtering；
- graph traversal；
- provenance backtracking；
- version retrieval；
- global community search；
- answerability gating。

最終候選分數可表示為：

$$
\operatorname{Score}(d\mid q)
=
\mathcal{F}
\left(
s_{\mathrm{sparse}},
s_{\mathrm{dense}},
s_{\mathrm{operator}},
s_{\mathrm{graph}},
s_{\mathrm{provenance}},
s_{\mathrm{epistemic}},
s_{\mathrm{version}}
\right)
$$

但本文不預設固定線性權重。近期混合 RAG、GraphRAG、query routing 及 retriever routing 研究皆指出，不同問題對稀疏、稠密、圖式及不同檢索器的需求不相同；固定單一路徑往往不能處理精確詞彙、全局主題、多跳關係與版本條件等異質問題。

OAM 的新意不在於宣稱一組算子標籤可以表示全部語義，而在於將算子標籤作為**可解釋導航面**。向量檢索回答「語義上接近什麼」；算子標籤回答「以何種方向、角色與操作關係接近」；TCF 與圖結構回答「這項命題依賴什麼、由何處而來、目前是猜想還是已驗證」；Original 則提供最高來源回調。

本文提出十四種導航指令、查詢路由器、多階段檢索管線、檢索追蹤證書、節點級與文檔級雙層索引、標籤不確定性、反過濾救援、版本失效傳播，以及適用於 Logic Matrix 的最小資料結構。本文亦提出一套對照實驗，將 BM25、dense RAG、hybrid RAG、GraphRAG、舊 IMS、OAM 及 OAM+TCF 進行比較。評估不只包含 Precision@k 與 Recall@k，也包含導航成功率、依賴路徑正確率、來源可追溯率、認識狀態保持率、版本混淆率、解釋忠實性、過度過濾損失與全局問題覆蓋度。

本文最終主張：AI 記憶問題不是單純的「記住」或「找到」，而是能否在不同檢索模式之間路由，理解知識物件的角色與狀態，沿著明確方向探索，並說明此次檢索為何成立。算子標籤不應取代向量，而應成為向量搜尋缺少的方向盤、儀表板與交通規則。

**關鍵詞：** Operator-Assisted Memory、混合檢索、RAG、GraphRAG、算子標籤、知識導航、TCF、來源追溯、query routing、可解釋檢索

---

# 0. 從 IMS 到 OAM

## 0.1 舊 IMS 的核心直覺

舊 IMS 指出三個真實問題：

1. 向量嵌入維度通常缺乏人類可讀語義；
2. 餘弦相似不直接解釋「為何相關」；
3. 一般 RAG 容易做相似搜尋，卻不容易支援方向性探索。

它因此提出：

$$
\Phi:
d
\rightarrow
(d_1,\ldots,d_7)
$$

並使用：

$$
D_{\mathrm{coord}}(q,d)
=
\sqrt{
\sum_i w_i(q_i-d_i)^2
}
$$

重新排序候選文檔。

舊版甚至已經採用：

1. 向量粗召回；
2. 七維坐標重排；

的混合雛形，而非完全刪除向量。這是可保留的工程起點。

## 0.2 舊 IMS 的過度主張

問題在於它進一步宣稱：

- $\mathbb{R}^{768}$ 是無結構黑箱；
- $\mathbb{R}^{7}$ 是具有完整元規則的白箱；
- 七維坐標能精確表示文檔；
- 坐標距離反映真實語義關係；
- IMS 已在精度、可解釋性及擴展性上證明優於 RAG；
- 「更抽象」可以直接等同提高單一 $d_3$ ；
- 主客比例、頻譜及拓撲可作為所有文件的通用標量。

這些內容沒有完成實驗，也承接了舊內視分類學的完備性假定。

## 0.3 新命名

「Inner-View Memory System」容易把 AI 知識檢索與主觀內視混在一起。

新名稱：

$$
\boxed{
\text{Operator-Assisted Memory}
}
$$

強調的是：

- 算子標籤輔助；
- 不取代其他表示；
- 記憶是存取與導航系統；
- 不預設 AI 具有主觀內視。

---

# 1. 記憶不是單一向量

令知識物件集合為：

$$
\mathcal{D}
=
\{
d_1,d_2,\ldots,d_N
\}
$$

每個知識物件可以是：

- 一篇 Original；
- 一份 TCF；
- 一個命題節點；
- 一段來源；
- 一項實驗；
- 一份 3M 結果；
- 一次對話；
- 一個版本差異；
- 一項反例。

OAM 將每個物件表示為：

$$
\mathcal{K}(d)
=
(
E,L,\Phi,G,P,V,S,C
)
$$

## 1.1 稠密表示 $E$

$$
E(d)\in\mathbb{R}^{n}
$$

用於：

- 語義近似；
- 同義改寫；
- 跨語言召回；
- 模糊查詢；
- 內容相似。

OAM 不把 embedding 描述成「無結構所以沒有價值」。它是學習得到的分布式表示，其內部維度不必逐維可讀，仍可能具有強大召回能力。

## 1.2 稀疏表示 $L$

包含：

- BM25；
- learned sparse representation；
- 關鍵詞；
- 專有名詞；
- 符號；
- 精確版本號；
- 文件編號；
- 人名與引用。

稀疏檢索對下列查詢常有優勢：

```text
TCF v2.1
KINV-00042
Δ_OT
EML-IOT-2026-v4.0
```

## 1.3 算子標籤 $\Phi$

$$
\Phi(d)
=
\{
(o_i,\theta_i,\gamma_i,p_i)
\}
$$

其中：

- $o_i$ ：算子類型；
- $\theta_i$ ：參數；
- $\gamma_i$ ：標註信心；
- $p_i$ ：來源與標註方法。

算子標籤可以包括：

```text
SCOPE.FOCUS
SCOPE.EXPAND
META.REVIEW
REP.FORMALIZE
REP.COMPRESS
TIME.HISTORICAL
TIME.COUNTERFACTUAL
REL.SELF_AS_OBJECT
RHYTHM.PERIODIC
STRUCT.HIERARCHICAL
INTERO.BREATH
ACTION.ROBOT_CONTROL
```

對一般知識文件，亦可增加知識導航標籤：

```text
ABSTRACTION.UP
ABSTRACTION.DOWN
EVIDENCE.EMPIRICAL
EVIDENCE.FORMAL
EVIDENCE.TESTIMONIAL
ROLE.DEFINITION
ROLE.HYPOTHESIS
ROLE.COUNTEREXAMPLE
ROLE.IMPLEMENTATION
ROLE.CRITIQUE
```

## 1.4 關係圖 $G$

TCF／SGCD／研究圖中可包含：

```text
defines
depends_on
supports
contradicts
refines
implements
tests
translates
supersedes
derived_from
same_claim_as
counterexample_to
```

## 1.5 來源 $P$

包括：

- Original SourceSpan；
- 作者；
- 文件；
- 外部文獻；
- 生成模型；
- 人工覆核；
- 3M artifact；
- 轉換歷史。

## 1.6 版本 $V$

$$
V(d)
=
(
v_{\mathrm{doc}},
v_{\mathrm{tcf}},
v_{\mathrm{schema}},
t_{\mathrm{valid}},
t_{\mathrm{deprecated}}
)
$$

## 1.7 認識狀態 $S$

```text
DEFINITION
OBSERVATION
SOURCE_CLAIM
HYPOTHESIS
CONJECTURE
DERIVED
FORMALLY_PROVED
MACHINE_CHECKED
REPRODUCED
REFUTED
UNRESOLVED
```

## 1.8 條件 $C$

包括：

- 領域；
- 語言；
- 可見性；
- 安全層級；
- 適用族群；
- 版本限制；
- 使用權；
- 任務前提。

---

# 2. 查詢也不是單一向量

使用者查詢 $q$ 可能同時包含：

- 內容需求；
- 精確詞彙；
- 導航方向；
- 證據要求；
- 版本要求；
- 來源要求；
- 排除條件；
- 回答形式。

因此定義查詢編譯：

$$
\mathcal{Q}(q)
=
(
q_{\mathrm{lex}},
q_{\mathrm{sem}},
q_{\mathrm{op}},
q_{\mathrm{graph}},
q_{\mathrm{epi}},
q_{\mathrm{version}},
q_{\mathrm{route}}
)
$$

## 2.1 示例

查詢：

> 找出比舊 IMS 更嚴謹、但仍保留知識導航概念的新版理論。

可編譯為：

```yaml
lexical:
  include: [IMS, 知識導航]
semantic:
  intent: replacement framework for IMS
operator:
  require:
    - META.REVIEW
    - REP.FORMALIZE
navigation:
  direction:
    - VERSION.LATEST
    - EPISTEMIC.MORE_RIGOROUS
graph:
  relation:
    - supersedes
    - refines
version:
  prefer_active: true
epistemic:
  exclude:
    - historical_claim_as_current
route:
  type: hybrid_graph
```

查詢：

> 從這篇理論往下找第一個可執行 MVP。

可編譯為：

```yaml
navigation:
  direction:
    - APPLICATION.DOWN
    - IMPLEMENTATION.NEAREST
graph:
  relation:
    - implements
    - operationalizes
epistemic:
  prefer:
    - SPECIFICATION
    - CODE
    - TEST_RESULT
```

---

# 3. 十四種知識導航方向

舊 IMS 最有價值的概念，是把檢索從「找相似」提升到「沿方向移動」。

OAM 定義最小導航集合。

## 3.1 抽象度導航

```text
ABSTRACT.UP
CONCRETE.DOWN
```

不是對單一標量加減，而是沿關係圖尋找：

- 一般化；
- 上位概念；
- 基礎原理；
- 具體案例；
- 實作；
- 數據。

## 3.2 來源導航

```text
SOURCE.BACK
DERIVATION.FORWARD
```

- 回到 Original；
- 從來源走向衍生理論。

## 3.3 證據導航

```text
EVIDENCE.STRONGER
EVIDENCE.WEAKER
```

例如由：

```text
CONJECTURE
→ TESTABLE_HYPOTHESIS
→ EXPERIMENT
→ REPRODUCED
```

## 3.4 時間與版本

```text
VERSION.EARLIER
VERSION.LATER
```

## 3.5 立場與反例

```text
CRITIQUE.OPPOSING
COUNTEREXAMPLE.NEAREST
```

## 3.6 依賴

```text
DEPENDENCY.UPSTREAM
DEPENDENCY.DOWNSTREAM
```

## 3.7 表徵

```text
REP.ORIGINAL
REP.COMPRESSED
```

## 3.8 主體與觀察面

```text
PERSPECTIVE.FIRST_PERSON
PERSPECTIVE.PUBLIC_EVIDENCE
```

這十四種方向可以組合，不宣稱彼此正交。

---

# 4. 多階段檢索管線

## 4.1 查詢理解

$$
q
\rightarrow
\widehat{\mathcal{Q}}(q)
$$

輸出：

- query type；
- entities；
- exact terms；
- operator directions；
- evidence requirement；
- version requirement；
- answerability risk。

## 4.2 路由

路由器：

$$
\rho(q)
\rightarrow
\mathcal{R}_q
$$

其中 $\mathcal{R}_q$ 可為：

```text
SPARSE_ONLY
DENSE_ONLY
HYBRID
OPERATOR_FILTERED
GRAPH_LOCAL
GRAPH_GLOBAL
VERSION_TRACE
SOURCE_TRACE
NO_RETRIEVAL
```

不同查詢需要不同檢索器。近年的 query routing 與 retriever routing 研究亦把「一體適用的單一檢索器」視為限制，並依查詢與下游生成效用動態選擇路徑。

## 4.3 第一階段召回

候選集合：

$$
C_0
=
C_{\mathrm{sparse}}
\cup
C_{\mathrm{dense}}
\cup
C_{\mathrm{graph}}
$$

可用 Reciprocal Rank Fusion：

$$
\operatorname{RRF}(d)
=
\sum_{r\in\mathcal{R}}
\frac{1}{k+\operatorname{rank}_r(d)}
$$

## 4.4 算子與條件處理

分為兩類。

### 硬約束

例如：

- 必須是最新版；
- 不得公開內部文件；
- 必須有 Original；
- 必須是 `FORMALLY_PROVED`。

### 軟偏好

例如：

- 更抽象；
- 更偏實作；
- 與第一人稱資料更接近；
- 較強證據。

避免把所有算子條件都做成 hard filter，否則標註錯誤會造成零召回。

## 4.5 圖擴展

對候選節點沿關係擴展：

$$
C_1
=
\operatorname{Expand}
(
C_0,
G,
r,
h
)
$$

其中：

- $r$ ：關係類型；
- $h$ ：最大跳數。

## 4.6 重排

$$
C_2
=
\operatorname{Rerank}
(
q,
C_1,
\mathcal{Q}(q)
)
$$

重排器同時考慮：

- 問題相關；
- 生成可用性；
- 來源；
- 狀態；
- 多樣性；
- 重複；
- 版本。

## 4.7 回答能力閘門

若：

- 沒有足夠來源；
- 候選互相衝突；
- 只有歷史版本；
- 問題需要尚不存在的證據；

則輸出：

```text
PARTIALLY_ANSWERABLE
UNANSWERABLE_FROM_CORPUS
VERSION_CONFLICT
EVIDENCE_INSUFFICIENT
```

而不是強行生成。

---

# 5. 分數模型

最簡形式：

$$
s(d\mid q)
=
\alpha s_L
+
\beta s_E
+
\gamma s_{\Phi}
+
\delta s_G
+
\eta s_P
+
\mu s_S
+
\nu s_V
$$

但固定權重具有侷限。

## 5.1 查詢自適應權重

$$
\mathbf{w}_q
=
f_{\omega}
(
q,
\operatorname{margin}_{\mathrm{sparse}},
\operatorname{margin}_{\mathrm{dense}},
\operatorname{coverage}_{\Phi},
\operatorname{graph\_availability}
)
$$

精確專有名詞查詢可提高 sparse 權重；概念改寫提高 dense 權重；依賴與全局問題提高 graph 權重；方向性探索提高 operator 權重。

## 5.2 生成效用

相關文檔不一定能支持正確回答。因此加入：

$$
u_{\mathrm{gen}}(d,q)
$$

衡量文檔是否包含：

- 可引用證據；
- 完整條件；
- 可解析來源；
- 足夠上下文；
- 正確版本。

最終：

$$
s^*
=
\lambda s_{\mathrm{retrieval}}
+
(1-\lambda)u_{\mathrm{gen}}
$$

## 5.3 多樣性

對全局問題，避免 top- $k$ 全部來自同一局部群組：

$$
\operatorname{MMR}
=
\arg\max_d
\left[
\lambda s(d,q)
-
(1-\lambda)
\max_{d'\in C_{\mathrm{selected}}}
\operatorname{sim}(d,d')
\right]
$$

---

# 6. 算子標籤不是坐標真理

## 6.1 多標籤而非單點

同一文件可以同時包含：

```text
REP.FORMALIZE
META.CRITIQUE
TIME.HISTORICAL
REL.MULTI_AGENT
ACTION.IMPLEMENTATION
```

所以：

$$
\Phi(d)
\neq
(x_1,\ldots,x_9)
$$

而是帶不確定性的集合或序列。

## 6.2 節點級標籤

整篇論文可能同時包含：

- 理論背景；
- 實驗；
- 猜想；
- 批判；
- 實作。

因此算子應標在：

- document；
- section；
- statement；
- relation；
- source span；

不同粒度。

## 6.3 不確定性

$$
P(o_i\mid d)
$$

而不是：

$$
o_i(d)\in\{0,1\}
$$

保留：

```text
confidence
annotator
model_version
review_status
```

## 6.4 開放集合

若現有算子不適合：

```text
UNKNOWN_OPERATOR
NEW_OPERATOR_CANDIDATE
MULTIPLE_PLAUSIBLE
```

不能強行分類。

---

# 7. 反過濾救援

結構標籤最大的風險，是錯誤標籤使真正相關文檔被排除。

## 7.1 過度過濾

若硬條件導致：

$$
|C|<k_{\min}
$$

則啟動 rescue：

1. 將低信心 hard filter 改為 soft preference；
2. 擴展同義算子；
3. 回退至 dense／sparse；
4. 向使用者顯示條件放寬。

## 7.2 過濾後悔

定義：

$$
R_{\mathrm{filter}}
=
\operatorname{Recall}_{\mathrm{unfiltered}}
-
\operatorname{Recall}_{\mathrm{filtered}}
$$

若結構過濾提高 precision 卻嚴重損失 recall，需重新調整。

## 7.3 標籤覆蓋

$$
\operatorname{Coverage}_{\Phi}
=
\frac{
\text{具有可靠算子標籤的知識節點}
}{
\text{總知識節點}
}
$$

覆蓋低時不應過度依賴算子路由。

---

# 8. 圖式與全局導航

一般向量 RAG擅長局部相關文本，但較難回答：

- 這個資料庫有哪些主要理論群？
- 哪些論文共同依賴某一假設？
- 某概念如何跨十篇文件演化？
- 哪些分支已經有反例？
- 整體研究的空白在哪裡？

GraphRAG 以實體—關係圖和階層社群摘要處理全局 sensemaking；GRAG 則針對圖資料進行文字子圖檢索與多跳推理。OAM 吸收兩者的結構優勢，但不要求所有資料都轉成單一知識圖。

## 8.1 Local search

從具體節點出發：

$$
n_0
\rightarrow
N_h(n_0)
$$

## 8.2 Global search

從社群、主題或依賴群出發：

$$
\mathcal{C}_1,\ldots,\mathcal{C}_m
$$

## 8.3 Directional search

算子導航指定圖遍歷方向：

```text
ABSTRACT.UP
IMPLEMENTATION.DOWN
COUNTEREXAMPLE
SUPERSEDES
SOURCE.BACK
```

## 8.4 動態社群選擇

不必每次讀取全部社群摘要，可以從根節點評估相關性並動態向下展開，降低不相關上下文。

---

# 9. TCF 作為主要結構層

OAM 與 TCF 的分工：

$$
\text{Original}
\rightarrow
\text{TCF}
\rightarrow
\text{OAM Index}
\rightarrow
\text{Retrieval／Navigation}
$$

## 9.1 Original

- 最高來源；
- 完整語境；
- 原始敘事；
- 最終回調。

## 9.2 TCF

- concept；
- statement；
- argument；
- relation；
- evidence；
- verification；
- version；
- visibility。

## 9.3 OAM

- 建立多索引；
- 路由查詢；
- 執行導航；
- 輸出檢索追蹤；
- 不改寫來源權威。

## 9.4 3M

- 提供執行、反例與證據；
- 可作為 `EVIDENCE.STRONGER` 的下游導航。

---

# 10. 檢索追蹤證書

每次檢索應能回答：

> 為什麼這份資料出現在結果中？

示例：

```json
{
  "retrieval_id": "OAM-R-00042",
  "query": "找出內視分類學中更嚴謹的呼吸理論",
  "route": [
    "HYBRID",
    "OPERATOR_FILTERED",
    "VERSION_TRACE"
  ],

  "query_plan": {
    "semantic_intent": "reconstructed breathing framework",
    "operators": [
      "META.CRITIQUE",
      "REP.FORMALIZE",
      "INTERO.BREATH"
    ],
    "version_preference": "latest_active",
    "epistemic_preference": "testable_over_metaphysical"
  },

  "result": {
    "document_id": "IOT-E-v0.1",
    "scores": {
      "sparse": 0.63,
      "dense": 0.91,
      "operator": 0.88,
      "graph": 1.0,
      "version": 1.0,
      "epistemic": 0.94
    },
    "graph_path": [
      "historical_v3",
      "superseded_by",
      "IOT-E-v0.1"
    ],
    "source_available": true
  },

  "explanation": [
    "This document supersedes the historical breathing paper.",
    "It is tagged as interoception, respiration, action, and methodological critique.",
    "It has a later active version and separates testable claims from ontology."
  ]
}
```

解釋必須由實際檢索訊號生成，不能事後由 LLM 編造。

---

# 11. OAM 資料結構

```json
{
  "knowledge_object_id": "KO-00042",
  "granularity": "statement",
  "content": "...",

  "representations": {
    "dense_embedding_ref": "emb://...",
    "sparse_terms": ["TCF", "knowledge invariant"],
    "language": "zh-Hant"
  },

  "operators": [
    {
      "family": "REP",
      "mode": "FORMALIZE",
      "confidence": 0.91,
      "annotator": "model+human"
    },
    {
      "family": "META",
      "mode": "CRITIQUE",
      "confidence": 0.84
    }
  ],

  "knowledge_role": [
    "HYPOTHESIS",
    "FRAMEWORK"
  ],

  "relations": [
    {
      "type": "supersedes",
      "target": "KO-OLD-001"
    },
    {
      "type": "depends_on",
      "target": "KO-00011"
    }
  ],

  "provenance": {
    "original_document": "DOC-009",
    "source_spans": ["SPAN-021", "SPAN-028"],
    "tcf_version": "2.1.0"
  },

  "version": {
    "semantic_version": "0.1",
    "status": "active",
    "valid_from": "2026-07-31"
  },

  "epistemic_status": {
    "state": "STRUCTURAL_CONJECTURE",
    "verification": "NOT_TESTED"
  },

  "access": {
    "visibility": "internal"
  }
}
```

---

# 12. 索引架構

## 12.1 Dense index

用於語義召回。

## 12.2 Sparse index

用於精確術語與符號。

## 12.3 Operator index

倒排：

```text
REP.FORMALIZE → [KO-1, KO-7, KO-9]
META.CRITIQUE → [KO-2, KO-9]
```

## 12.4 Graph index

鄰接表、property graph 或 RDF／TCF relation store。

## 12.5 Version index

追蹤：

- active；
- deprecated；
- historical；
- superseded；
- branch；
- merge。

## 12.6 Provenance index

由命題回到：

- SourceSpan；
- Original；
- artifact；
- reviewer；
-生成流程。

## 12.7 Epistemic index

支援：

```text
only_verified
include_conjectures
show_refuted
show_unresolved
```

---

# 13. 查詢路由類型

## 13.1 Exact lookup

例：

> KINV-00042 是什麼？

使用 sparse + ID index。

## 13.2 Semantic lookup

例：

> 哪些理論討論 AI 如何維持可修訂知識？

使用 dense + rerank。

## 13.3 Directional navigation

例：

> 找比這篇更具體的實作。

使用 operator + graph。

## 13.4 Relational query

例：

> 哪些論文依賴「Original 最高來源」？

使用 graph traversal。

## 13.5 Global query

例：

> 這 2,000 篇理論主要形成哪些研究群？

使用 graph community／hierarchical summarization。

## 13.6 Epistemic query

例：

> 哪些命題仍只是猜想，但已經有 3M 實驗？

使用 epistemic + evidence relation。

## 13.7 Version query

例：

> 內視分類學從 v1 到重構版改了什麼？

使用 version trace + source.

## 13.8 Negative query

例：

> 找出反對「宇宙呼吸律」的重構內容。

使用 critique + contradiction + supersedes。

---

# 14. 原子單元與多粒度檢索

固定字數 chunk 可能切斷：

- 條件；
- 主張；
- 證據；
- 否定；
- 來源。

企業 RAG 研究已嘗試把 chunk 分解成原子命題並生成問題，以改善召回。TCF 天然提供概念與命題級單元。

OAM 支援：

```text
DOCUMENT
SECTION
ARGUMENT
STATEMENT
SOURCE_SPAN
EVIDENCE_ARTIFACT
```

## 14.1 粗到細

1. 文檔／社群召回；
2. 章節定位；
3. 命題定位；
4. SourceSpan 回調。

## 14.2 細到粗

1. 找到命題；
2. 補回其條件；
3. 補回論證；
4. 補回文檔與版本背景。

---

# 15. 可解釋性不是顯示權重而已

「因為算子距離是 0.2」不是充分解釋。

OAM 的檢索解釋至少包含：

1. 命中的查詢條件；
2. 使用的路由；
3. 主要匹配內容；
4. 圖路徑；
5. 來源；
6. 版本；
7. 認識狀態；
8. 被排除結果與原因；
9. 不確定性。

## 15.1 忠實解釋

解釋應由實際計算 trace 產生：

$$
e
=
g(\text{retrieval trace})
$$

而不是：

$$
e
=
\operatorname{LLMInvent}(q,d)
$$

## 15.2 可反查

每句解釋可回到：

```text
score component
filter rule
graph edge
metadata field
source span
```

---

# 16. 評估框架

舊 IMS 只規劃 Precision@k、Recall@k、坐標一致性與人工解釋評分。OAM 擴展如下。

## 16.1 檢索品質

- Recall@k；
- Precision@k；
- MRR；
- nDCG；
- MAP；
- answer recall。

## 16.2 導航成功率

$$
N_{\mathrm{success}}
=
\frac{
\text{到達目標類型或節點的導航}
}{
\text{導航查詢總數}
}
$$

## 16.3 路徑正確率

檢索出的依賴、版本或來源路徑是否正確。

## 16.4 來源可追溯率

$$
P_{\mathrm{trace}}
=
\frac{
\text{可回到充分 SourceSpan 的結果}
}{
\text{需要來源的結果}
}
$$

## 16.5 認識狀態保持

是否把猜想誤當事實、歷史稿誤當現行稿。

## 16.6 版本混淆率

$$
F_{\mathrm{version}}
=
\frac{
\text{返回錯誤版本的查詢}
}{
\text{版本敏感查詢}
}
$$

## 16.7 過濾後悔

$$
R_{\mathrm{filter}}
$$

## 16.8 解釋忠實性

解釋中的理由是否真正參與檢索。

## 16.9 全局覆蓋度

對資料庫全局問題，答案是否涵蓋多個主要社群。

## 16.10 成本

- indexing cost；
- latency；
- token cost；
- graph construction cost；
- annotation cost。

---

# 17. 對照實驗

## 17.1 系統組別

### A. BM25

只使用稀疏檢索。

### B. Dense RAG

embedding + cosine。

### C. Hybrid RAG

BM25 + dense + fusion。

### D. GraphRAG

圖索引與全局／局部搜尋。

### E. IMS Historical

dense recall + 七維距離重排。

### F. OAM

hybrid + operator + version／epistemic metadata。

### G. OAM + TCF

節點級 TCF、來源回調與圖導航。

### H. OAM + TCF + 3M

加入可執行證據及結果路由。

## 17.2 查詢集

至少包含：

```text
exact
paraphrase
cross-lingual
global
multi-hop
abstract-up
concrete-down
source-back
version
counterexample
epistemic-status
implementation
unanswerable
```

## 17.3 消融實驗

移除：

- sparse；
- dense；
- operator；
- graph；
- version；
- epistemic；
- provenance；
- adaptive router。

觀察每一層真正提供的價值。

---

# 18. 主要假說

## H1：混合優於替代

OAM 的最佳表現來自多表示互補，而不是算子標籤全面取代 embedding。

## H2：算子層主要改善導航

算子標籤對 `ABSTRACT.UP`、`IMPLEMENTATION.DOWN`、`PERSPECTIVE` 等方向查詢的改善，應高於一般相似查詢。

## H3：TCF 提高來源與狀態正確率

OAM + TCF 應降低來源丟失、條件丟失及認識狀態漂移。

## H4：自適應路由優於固定融合

不同查詢動態選擇 sparse、dense、graph 及 operator 權重，應優於單一固定權重。

## H5：硬過濾具有雙刃效果

可靠標籤的硬過濾提高 precision；低覆蓋或錯誤標籤則降低 recall。

## H6：圖層改善全局與多跳查詢

Graph layer 對 corpus-level themes、依賴與演化問題較有價值，但對簡單 exact lookup 未必划算。

## H7：檢索 trace 提高可審計性

有 trace 的系統較容易發現錯誤版本、錯誤來源及錯誤路由。

## H8：舊 IMS 在部分導航任務仍可能有效

七維歷史坐標可以作為 baseline，某些人工方向標籤可能確實有用；但其優勢需實驗而非理論宣告。

---

# 19. 失敗模式

## 19.1 標籤本體僵化

新知識被迫塞入舊算子。

## 19.2 標籤幻覺

AI 自動標註產生不存在的角色或狀態。

## 19.3 偽精確

顯示 0.873 的 operator score，卻沒有可靠標註基礎。

## 19.4 圖污染

錯誤 relation 造成多跳放大。

## 19.5 版本失效

舊節點被新版本取代，但仍在檢索中獲得高分。

## 19.6 來源洗白

生成摘要被誤當 Original。

## 19.7 全局摘要偏差

Graph community summary 遺漏少數但重要分支。

## 19.8 過度複雜

在小型資料庫或簡單查詢中，多層路由成本高於收益。

## 19.9 導航循環

使用者或 agent 在 abstract／concrete、source／derived 之間無限往返。

## 19.10 使用者意圖誤判

「更深入」可能表示更數學、更實證、更細節或更批判，不能直接映射單一方向。

---

# 20. 實作分期

## Phase 0：離線標註

對 100 篇文件建立：

- operator；
- role；
- epistemic；
- version；
- provenance；

人工黃金集。

## Phase 1：Hybrid Baseline

BM25 + dense + RRF + reranker。

## Phase 2：Operator Navigation

先支援四個高價值方向：

```text
ABSTRACT.UP
CONCRETE.DOWN
SOURCE.BACK
VERSION.LATER
```

## Phase 3：TCF Node Index

加入 statement、relation、SourceSpan。

## Phase 4：Graph Search

支援依賴、多跳及全局群組。

## Phase 5：Adaptive Router

依查詢選擇檢索路徑。

## Phase 6：Retrieval Certificate

輸出 trace 與認識狀態。

## Phase 7：3M Evidence

從理論導航至執行與反例。

---

# 21. Logic Matrix 中的部署

建議端點：

```text
/search
/navigate
/trace
/source
/version
/graph
/epistemic
/global
```

## 21.1 Search

普通查詢。

## 21.2 Navigate

```json
{
  "start": "KO-00042",
  "direction": "ABSTRACT.UP",
  "steps": 2
}
```

## 21.3 Trace

回傳檢索證書。

## 21.4 Source

直接回調 Original SourceSpan。

## 21.5 Version

顯示演化鏈。

## 21.6 Epistemic

篩選猜想、已驗證、反駁或未決內容。

---

# 22. 與內視分類學的關係

OAM 不再宣稱整個知識世界具有與人類內視相同的九維空間。

真正保留的連接是：

> 內視算子是一組可用於描述知識文本「在做什麼」的操作標籤。

例如：

- 一篇文章在壓縮；
- 一篇文章在反思舊理論；
- 一篇文章在重建歷史；
- 一篇文章在改變主客立場；
- 一篇文章在把理論轉為行動。

這是語義角色標註，不是意識本體映射。

因此：

$$
\boxed{
\text{Operator label}
=
\text{interpretable semantic facet}
}
$$

而非：

$$
\boxed{
\text{Operator label}
=
\text{complete coordinate of knowledge}
}
$$

---

# 23. 與舊 IMS 的逐項修訂

| 舊 IMS | OAM |
|---|---|
| 七維坐標取代高維向量 | 算子標籤輔助 dense／sparse |
| 每文檔一個坐標 | 多粒度、多標籤、帶信心 |
| 坐標距離是真實語義距離 | 距離只是可學習／可測的排序訊號 |
| 固定維度權重 | 查詢自適應路由與融合 |
| 七維導航 | 圖關係＋算子方向導航 |
| 證明優於 RAG | 建立對照實驗 |
| 向量是黑箱、坐標是白箱 | 兩者具有不同優缺點 |
| 所有文檔可唯一分類 | 允許未知、多義與低信心 |
| 只比較文件 | 文件、章節、命題、來源、證據多粒度 |
| 無版本治理 | active／historical／superseded |
| 無認識狀態 | conjecture／verified／refuted／unresolved |
| 找到即回答 | answerability gating |
| 解釋來自坐標差 | 解釋來自檢索 trace |

---

# 24. 討論：AI 記憶的真正問題

舊 IMS 的結語是：

> AI 記憶問題不是記不住，而是找不到。

重構後需要再加三層：

$$
\boxed{
\text{不是只找不到，
也可能找錯版本、找錯狀態、找不到關係、或不知道不該回答。}
}
$$

因此 AI 記憶能力至少包括：

1. **Recall**：找回候選；
2. **Discrimination**：區分相關與表面相似；
3. **Navigation**：沿目標方向移動；
4. **Grounding**：回到來源；
5. **State Awareness**：知道命題目前的認識狀態；
6. **Version Awareness**：知道哪個版本有效；
7. **Abstention**：資料不足時不偽造答案；
8. **Revision**：新資料進入後更新索引與依賴。

所以：

$$
\boxed{
\text{AI Memory}
=
\text{Storage}
+
\text{Retrieval}
+
\text{Navigation}
+
\text{Governance}
+
\text{Revision}
}
$$

---

# 25. 結論

本文提出 Operator-Assisted Memory，將舊 IMS 的核心直覺——「AI 需要可導航的知識空間」——從七維坐標替代論，重構成多表示混合檢索架構。

每個知識物件由：

$$
\boxed{
\mathcal{K}(d)
=
(E,L,\Phi,G,P,V,S,C)
}
$$

共同描述。

每個查詢則被編譯成：

$$
\boxed{
\mathcal{Q}(q)
=
(
q_{\mathrm{lex}},
q_{\mathrm{sem}},
q_{\mathrm{op}},
q_{\mathrm{graph}},
q_{\mathrm{epi}},
q_{\mathrm{version}},
q_{\mathrm{route}}
)
}
$$

OAM 不再主張：

- 七或九個維度足以表示全部知識；
- 人工坐標天然優於 learned embeddings；
- 坐標距離等於語義真實距離；
- 形式上可導航就代表檢索效果已被證明。

它改為主張：

$$
\boxed{
\text{向量負責召回，
算子負責方向，
圖負責關係，
TCF 負責結構，
Original 負責來源，
版本與認識狀態負責邊界。}
}
$$

算子標籤的角色不是取代向量，而是回答向量難以單獨回答的問題：

- 這份資料在做什麼？
- 它比起另一份更抽象還是更具體？
- 它是原始來源、壓縮表示、批判還是實作？
- 它目前是猜想、已驗證還是已反駁？
- 從這裡應往哪個方向探索？
- 為什麼系統把它找回來？

最終：

$$
\boxed{
\text{Operator-Assisted Memory}
=
\text{Hybrid Retrieval}
+
\text{Directional Navigation}
+
\text{Provenance}
+
\text{Epistemic Governance}
}
$$

這保留了 IMS 最值得留下的「給 AI 一個知識導航儀」概念，同時撤回了把七維坐標當成整個語義世界地圖的過度宣稱。

---

# 參考文獻

1. Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., Metropolitansky, D., Ness, R. O., & Larson, J. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. Microsoft Research.
2. Hu, Y., Lei, Z., Zhang, Z., Pan, B., Ling, C., & Zhao, L. (2024). *GRAG: Graph Retrieval-Augmented Generation*. arXiv:2405.16506.
3. Kalra, R., Wu, Z., Gulley, A., Hilliard, A., Guan, X., Koshiyama, A., Treleaven, P. C. (2024). *HyPA-RAG: A Hybrid Parameter Adaptive Retrieval-Augmented Generation System for AI Legal and Policy Applications*. CustomNLP4U 2024.
4. Islam, S. B., Rahman, M. A., Hossain, K. S. M. T., Hoque, E., Joty, S., & Parvez, M. R. (2024). *Open-RAG: Enhanced Retrieval Augmented Reasoning with Open-Source Large Language Models*. Findings of EMNLP 2024.
5. Lu, J., Hall, K., Ma, J., & Ni, J. (2024). *HYRR: Hybrid Infused Reranking for Passage Retrieval*. LREC-COLING 2024.
6. Zhuang, S., et al. (2024). *PromptReps: Prompting Large Language Models to Generate Dense and Sparse Representations for Zero-Shot Document Retrieval*. EMNLP 2024.
7. Raina, V., & Gales, M. (2024). *Question-Based Retrieval using Atomic Units for Enterprise RAG*. FEVER 2024.
8. Zhang, J., Liu, X., Hu, Y., Niu, C., Wu, F., & Chen, G. (2025). *Query Routing for Retrieval-Augmented Language Models*. arXiv:2505.23052.
9. Mu, F., Zhang, L., Jiang, Y., Li, W., Zhang, Z., Xie, P., & Huang, F. (2025). *Unsupervised Query Routing for Retrieval Augmented Generation*. arXiv:2501.07793.
10. Zhao, T., Zhu, Y., Tian, Y., & Dou, Z. (2026). *R3AG: Retriever Routing for Retrieval-Augmented Generation*. arXiv:2604.22849.
11. Raya-Rios, V., Gomez-Adorno, H., Hecht, L., et al. (2026). *IIMAS-RAG at SemEval-2026 Task 8: Hybrid Sparse-Dense Retrieval and Answerability-Conditioned Generation for Multi-Turn RAG*. SemEval 2026.
12. Yang, J., Chen, Y., & Yang, L. (2026). *DUTIR at SemEval-2026 Task 8: A Hybrid Retrieval and Faithfulness-Guarded Framework for Multi-Turn RAG*. SemEval 2026.
13. Cao, Y., Gao, Z., Li, Z., Xie, X., Zhou, K., & Xu, J. (2024). *LEGO-GraphRAG: Modularizing Graph-based Retrieval-Augmented Generation for Design Space Exploration*. arXiv:2411.05844.
14. Neo.K. (2026). *內視記憶系統：基於坐標化的 AI 知識管理框架*. Historical Internal Version.
15. Neo.K. (2026). *內視分類學的算子論*. EveMissLab Internal Paper v0.1.
16. Neo.K. (2026). *內視算子代數*. EveMissLab Internal Paper v0.1.
17. Neo.K. (2026). *Original–TCF–3M 三平面研究架構*. EveMissLab Internal Paper v0.1.

---

## 內部研究備註

1. 本文為內視分類學第一輪重構系列應用論文 F。
2. 至此 A–F 六份新基線已完成：
   - A：算子論與不可觀察者分類；
   - B：第一人稱資料分層；
   - C：算子代數；
   - D：宗教與神秘體驗；
   - E：內感—呼吸—動作；
   - F：Operator-Assisted Memory。
3. 下一步不應繼續增加理論篇數，優先建立：
   - 系列索引；
   - TCF 轉換；
   - OAM 最小資料 Schema；
   - 100 篇黃金標註集；
   - BM25＋dense＋operator baseline。
4. 舊 IMS 可作為消融 baseline，不刪除。
5. OAM 名稱中的 Memory 指 AI 知識存取與治理，不表示 AI 主觀記憶。
