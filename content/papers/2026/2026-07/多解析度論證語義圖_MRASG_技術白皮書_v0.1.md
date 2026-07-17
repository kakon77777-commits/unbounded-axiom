# 多解析度論證語義圖（MRASG）技術白皮書

## 一種可漸進展開、局部載入、增量更新與可追溯還原的知識聚合演算法

**版本：** v0.1  
**文件類型：** 技術白皮書／演算法設計草案  
**作者：** Neo.K  
**核心定位：** 通用知識聚合與論證展開基礎設施，不限定於論壇、留言板或單一應用

---

## 摘要

現有論壇、留言板、社群平台與多數 AI 協作系統，通常把資訊排列成時間線、回覆串或單層摘要。這種結構在討論規模擴大後，會出現四個根本問題：

1. 大量內容只能線性閱讀，難以辨識真正的論證結構；
2. 相同主張與相似論據被重複生成，造成計算與閱讀浪費；
3. 摘要經多輪壓縮後發生資訊失真，展開時又可能產生不受原文支持的擴寫；
4. 使用者或 AI 為取得局部答案，被迫載入大量不相關內容。

本文提出「多解析度論證語義圖」：

**Multi-Resolution Argumentation Semantic Graph，MRASG。**

MRASG 將討論內容拆分為主張、佐證、反對、反駁、限定條件、來源、綜合與未解問題等語義節點，再以有向圖、無環圖或超圖描述其關係。每個節點同時具有多個解析度視圖，例如約 30 字、300 字、3000 字與完整材料層，但這些層級不是逐層摘要，而是全部直接指向共同的原始證據與語義單元。

系統在初次載入時只呈現短視圖，使用者展開某個節點後，才局部檢索相關原始資料並生成更完整的視圖。系統亦可依節點相鄰性、爭議強度、使用歷史與來源變動進行預載入、快取與增量更新。

MRASG 的目標不是建立一個更複雜的論壇，而是提供一套能把大規模 AI 討論、研究材料、政策辯論、程式審查、知識庫與長期 Agent 記憶，編譯成「可導航、可驗證、可逐層展開」之語義空間的通用演算法。

---

# 1. 問題定義

## 1.1 線性討論結構的限制

傳統討論系統通常採用以下形式：

```text
主文
├─ 回覆 1
│  ├─ 回覆 1.1
│  └─ 回覆 1.2
├─ 回覆 2
└─ 回覆 3
```

此結構描述的是「誰回覆了誰」，卻不必然描述：

- 哪一段文字支持哪個主張；
- 哪個反例推翻哪條推理鏈；
- 哪些回覆只是重複；
- 哪些衝突來自定義差異；
- 哪些結論已獲充分支持；
- 哪些問題仍未被回答。

當 AI 大量參與後，線性結構的缺陷會進一步放大。AI 可以在短時間內生成大量長文，因此系統的瓶頸將從「內容不足」轉變為「內容過多而無法組織」。

## 1.2 讚與踩不足以表達論證

二元投票只能描述偏好或整體認同，無法表示：

- 同意結論但反對推理；
- 反對普遍命題但接受局部版本；
- 證據有效但因果推論過強；
- 來源可信但已過時；
- 反例只在特定條件成立；
- 多數意見高度重複，少數意見卻提供致命反例。

因此，MRASG 不把「支持／反對次數」視為最終評價，而把它們視為論證圖上的事件與權重來源。

## 1.3 多輪摘要造成不可逆資訊損失

若系統採用：

```text
完整長文
→ 3000 字摘要
→ 300 字摘要
→ 30 字摘要
```

則每次壓縮都可能遺失條件、例外、來源與不確定性。若展開時再由短摘要擴寫，系統可能生成原資料中不存在的內容。

設完整資訊為 $$S$$，第 $$i$$ 層摘要為 $$R_i$$，則連續摘要通常形成：

$$
I(S) > I(R_1) > I(R_2) > \cdots > I(R_n)
$$

而由短摘要重新擴寫得到的內容 $$\widehat{R}_{i-1}$$，不保證滿足：

$$
\widehat{R}_{i-1} \subseteq S
$$

因此，MRASG 的核心原則是：**所有解析度視圖都必須直接由共同的原始語義集合生成，而不是由上一層摘要推導。**

---

# 2. 核心概念

## 2.1 點、線、面、體

MRASG 將同一個知識區域表示為多種解析度。

### 點：最小導航節點

點層只回答：

> 這個節點的核心主張是什麼？

典型長度可以是 10 至 50 字，但不設硬性限制。

### 線：主要推理鏈

線層呈現：

- 核心主張；
- 一至數個主要理由；
- 最重要的支持證據；
- 最強反對意見；
- 暫時性結論。

### 面：完整爭議結構

面層呈現：

- 多條支持鏈；
- 多條反對鏈；
- 反駁與再反駁；
- 條件限制；
- 來源與相互引用；
- 尚未解決的衝突。

### 體：完整語義空間

體層包含：

- 原始長文；
- 完整引用；
- 資料來源；
- 版本歷史；
- 多個 AI 或人類的完整輸出；
- 推理分支；
- 衝突節點；
- 未收斂問題；
- 生成與更新紀錄。

解析度層可寫為：

$$
R_0 \rightarrow R_1 \rightarrow R_2 \rightarrow \cdots \rightarrow R_n
$$

但這個箭頭表示「導航上的展開」，不是「資訊來源上的逐層生成」。

## 2.2 共同來源原則

對任一節點 $$v$$，定義其原始語義集合為：

$$
S_v = \{s_1,s_2,\ldots,s_m\}
$$

第 $$k$$ 層視圖由壓縮函數生成：

$$
R_k(v)=C_k(S_v,G_v,\pi_k)
$$

其中：

- $$S_v$$：與節點相關的原始材料；
- $$G_v$$：節點附近的論證子圖；
- $$\pi_k$$：第 $$k$$ 層的呈現策略；
- $$C_k$$：第 $$k$$ 層視圖生成器。

展開時不得執行：

$$
R_k(v)\rightarrow \widehat{R}_{k+1}(v)
$$

而應執行：

$$
R_k(v)
\rightarrow
\operatorname{Retrieve}(S_v,G_v)
\rightarrow
R_{k+1}(v)
$$

因此，短視圖只是索引，不是完整內容的替代來源。

---

# 3. 論證語義圖模型

## 3.1 基本圖結構

定義 MRASG 為：

$$
\mathcal{G}=(V,E,X,M)
$$

其中：

- $$V$$：語義節點集合；
- $$E$$：節點關係集合；
- $$X$$：原始資料與外部來源集合；
- $$M$$：版本、權限、模型與生成中繼資料。

## 3.2 節點類型

最小可行版本至少支援以下節點：

| 類型 | 英文 | 功能 |
|---|---|---|
| 主張 | Claim | 可被支持、反對或限定的命題 |
| 佐證 | Support | 支持某主張的理由 |
| 證據 | Evidence | 可追溯的資料、引用、實驗或觀察 |
| 反對 | Objection | 對主張或推理鏈提出異議 |
| 反駁 | Rebuttal | 回應某個反對 |
| 限定 | Qualification | 指定命題成立的條件與範圍 |
| 替代解釋 | Alternative | 提出不同因果或理論模型 |
| 綜合 | Synthesis | 統合多個分支形成較高階結論 |
| 未解問題 | Open Question | 尚無充分回答的問題 |
| 定義 | Definition | 固定術語或概念邊界 |
| 衝突 | Conflict | 表示來源、定義或推論互不相容 |

## 3.3 邊類型

邊不只表示回覆關係，而應明確標記語義：

- `supports`
- `opposes`
- `rebuts`
- `qualifies`
- `depends_on`
- `cites`
- `duplicates`
- `generalizes`
- `specializes`
- `contradicts`
- `synthesizes`
- `answers`
- `raises`
- `updates`

同一節點可以同時連向多個主張，因此底層資料結構宜採有向圖、DAG 或超圖，而非單純樹狀結構。

---

# 4. 多解析度視圖

## 4.1 解析度不是固定字數

30、300、3000、30000 字只是一種示例。實際系統應以「資訊目的」而非字數切分。

可定義：

| 層級 | 目的 | 典型內容 |
|---|---|---|
| $$R_0$$ | 導航 | 一句核心命題 |
| $$R_1$$ | 快速理解 | 主張、主要理由、主要反對 |
| $$R_2$$ | 分析 | 完整推理鏈、證據與限制 |
| $$R_3$$ | 研究 | 全部主要分支與來源 |
| $$R_4$$ | 稽核 | 原始材料、版本、生成紀錄 |

解析度層應滿足：

$$
\operatorname{Coverage}(R_{k+1})
\geq
\operatorname{Coverage}(R_k)
$$

但不要求每一層都包含前一層的逐字內容。

## 4.2 視圖生成約束

每個視圖應保存：

1. 涵蓋的原始節點 ID；
2. 使用的來源 ID；
3. 省略的主要分支；
4. 生成時間；
5. 生成器版本；
6. 圖狀態指紋；
7. 不確定性與爭議提示。

因此，任何摘要都可以被追溯，而不是成為失去來源的孤立文字。

---

# 5. 爭議與論證品質計算

## 5.1 次數不等於品質

定義某主張 $$c$$ 的支持事件數與反對事件數：

$$
N_s(c)=\text{支持事件數}
$$

$$
N_o(c)=\text{反對事件數}
$$

它們只能表示活動量，不能直接表示真實性。

## 5.2 論證品質權重

單一論證 $$a$$ 的權重可寫為：

$$
W(a)
=
\alpha E(a)
+
\beta L(a)
+
\gamma V(a)
+
\delta N(a)
+
\epsilon P(a)
-
\eta D(a)
-
\theta U(a)
$$

其中：

- $$E(a)$$：證據強度；
- $$L(a)$$：推理完整度；
- $$V(a)$$：可驗證性；
- $$N(a)$$：新穎度；
- $$P(a)$$：來源可追溯性；
- $$D(a)$$：與既有論證的重複度；
- $$U(a)$$：未揭露假設或不確定性懲罰。

## 5.3 爭議強度

主張 $$c$$ 的爭議強度可定義為：

$$
\operatorname{Dispute}(c)
=
\lambda_1
\sum_{a\in A_s(c)}W(a)
+
\lambda_2
\sum_{b\in A_o(c)}W(b)
+
\lambda_3 B(c)
+
\lambda_4 Q(c)
+
\lambda_5 T(c)
$$

其中：

- $$A_s(c)$$：支持論證集合；
- $$A_o(c)$$：反對論證集合；
- $$B(c)$$：分支廣度；
- $$Q(c)$$：未解問題數；
- $$T(c)$$：近期變動程度。

爭議強度高，不表示該主張錯誤，而表示它需要更高解析度的呈現與更多計算資源。

## 5.4 共識與收斂不可混同

系統應區分：

- 多數支持；
- 高品質支持；
- 缺乏反對；
- 反對已被回答；
- 定義已收斂；
- 證據仍不足；
- 僅在限定條件下成立。

因此，節點狀態可設為：

```text
OPEN
CONTESTED
PARTIALLY_RESOLVED
CONDITIONALLY_ACCEPTED
STABLE
DEPRECATED
SUPERSEDED
```

---

# 6. 新輸入的聚合流程

當新 AI、人類或 Agent 提交內容時，系統不應立即把完整文字追加到時間線，而應先進行以下流程。

## 6.1 語義拆解

將輸入拆分為：

- 主張；
- 前提；
- 證據；
- 推論；
- 限定條件；
- 反對；
- 問題；
- 結論。

## 6.2 近似節點檢索

找出最相近的既有節點：

$$
\operatorname{Sim}(x,v)
=
\alpha S_{\text{semantic}}
+
\beta S_{\text{structural}}
+
\gamma S_{\text{citation}}
+
\delta S_{\text{temporal}}
$$

## 6.3 新穎度判定

定義輸入 $$x$$ 對既有子圖 $$G_x$$ 的新穎度：

$$
\operatorname{Novelty}(x)
=
1-
\max_{v\in G_x}
\operatorname{Sim}(x,v)
$$

若新穎度低，系統可將其記為：

- 獨立重現；
- 同類支持；
- 同類反對；
- 重複來源；
- 語言改寫。

若新穎度高，才建立新節點或新分支。

## 6.4 結構化合併

輸入可能被處理為：

```text
原始輸入
├─ 既有主張 A：增加一次獨立支持
├─ 既有證據 B：補充新來源
├─ 新限定條件 C：建立新節點
└─ 新反例 D：建立反對分支
```

如此可避免大量 AI 重複相同長文。

---

# 7. 漸進載入與預載入

## 7.1 初始載入

當使用者進入節點 $$v$$ 時，只載入：

- 當前節點的 $$R_0$$ 或 $$R_1$$；
- 一個主要父節點；
- 少量主要子節點；
- 最強支持分支；
- 最強反對分支；
- 一至數個高相關鄰接節點。

定義局部載入集合：

$$
P(v)
=
\{v\}
\cup
\operatorname{Parent}(v)
\cup
\operatorname{TopChild}_k(v)
\cup
\operatorname{TopSupport}_m(v)
\cup
\operatorname{TopOpposition}_n(v)
\cup
\operatorname{Related}_r(v)
$$

## 7.2 預載入分數

對候選節點 $$u$$，其預載入優先度可寫為：

$$
\operatorname{Prefetch}(u\mid v)
=
\alpha R_s(u,v)
+
\beta R_g(u,v)
+
\gamma H(u\mid v)
+
\delta C(u)
+
\epsilon \Delta(u)
-
\eta K(u)
$$

其中：

- $$R_s$$：語義相關性；
- $$R_g$$：圖距離與邊關係；
- $$H$$：歷史導航機率；
- $$C$$：爭議或重要度；
- $$\Delta$$：近期更新程度；
- $$K$$：載入成本。

## 7.3 局部優先原則

系統不預載入整棵樹，而只預載入使用者最可能展開的前後節點。此策略可將大型語義圖的互動成本控制在局部範圍。

---

# 8. 快取、指紋與增量重建

## 8.1 視圖狀態指紋

任一節點第 $$k$$ 層視圖的指紋可定義為：

$$
H_k(v)
=
\operatorname{Hash}
\left(
S_v,
E_v,
G_v,
\pi_k,
M_k
\right)
$$

其中：

- $$S_v$$：原始語義單元；
- $$E_v$$：證據集合；
- $$G_v$$：局部圖結構；
- $$\pi_k$$：呈現策略；
- $$M_k$$：模型與生成規則版本。

## 8.2 三層重建策略

### 快取讀取

若指紋未變，直接使用既有視圖。

### 增量重建

若只新增局部分支，僅重建受影響節點與上層摘要。

### 完整重建

若核心主張、主要來源、定義或生成規則發生重大變更，重建完整局部子圖。

## 8.3 影響範圍

新增節點 $$x$$ 後的影響集合可寫為：

$$
A(x)
=
\operatorname{Ancestors}(x,d_a)
\cup
\operatorname{Dependents}(x,d_d)
\cup
\operatorname{Summaries}(x)
$$

其中 $$d_a$$ 與 $$d_d$$ 是限制更新傳播深度的參數。

---

# 9. 可追溯還原

## 9.1 還原不是自由擴寫

使用者點開短節點時，系統應從來源集合與局部子圖重新組合長視圖，而不是要求模型「把這句話寫長」。

還原函數可定義為：

$$
R_{k+1}(v)
=
\operatorname{Render}
\left(
\operatorname{Retrieve}(v,k+1),
\operatorname{Policy}_{k+1}
\right)
$$

## 9.2 每段文字的來源映射

較高解析度視圖中的每個主要段落，應能映射至：

- 原始輸入；
- 證據節點；
- 推理節點；
- 反對節點；
- 版本紀錄。

最理想情況下，系統保存段落級 provenance：

```json
{
  "paragraph_id": "p_103",
  "source_nodes": ["claim_12", "evidence_91", "objection_32"],
  "source_documents": ["doc_5", "doc_8"],
  "graph_hash": "sha256:...",
  "generator_version": "renderer_0.1"
}
```

---

# 10. MRASG 不限定於 AI 論壇

MRASG 應被視為一種通用語義基礎設施，而非特定產品。

## 10.1 AI 協作研究

多個 AI 對同一研究問題提出長篇分析，MRASG 可將它們聚合為：

- 已知主張；
- 重複主張；
- 新反例；
- 缺少證據的推論；
- 未解問題；
- 可繼續研究的分支。

## 10.2 文獻回顧

大量論文可被轉換為：

- 核心命題；
- 支持證據；
- 方法差異；
- 結果衝突；
- 時代變化；
- 尚未解決的研究缺口。

## 10.3 程式碼審查與軟體設計

每個 issue、PR、review comment 與設計決策可被編譯成：

- 問題；
- 假設；
- 修正方案；
- 反對理由；
- 測試證據；
- 已解決與未解決項目。

## 10.4 政策與法律論證

同一政策或法律問題可同時展示：

- 原則性支持；
- 實證性支持；
- 權利衝突；
- 執行成本；
- 例外條件；
- 不同法域或時間版本。

## 10.5 Agent 長期記憶

Agent 不必把所有歷史內容放入上下文，而可先載入：

- 高階任務節點；
- 最近決策；
- 相關爭議；
- 未完成分支；
- 必要時才展開的完整記憶。

## 10.6 長篇文件閱讀

書籍、技術文件與研究報告可被轉換成點、線、面、體式的漸進閱讀介面。

## 10.7 模型評估

多個模型對同一問題的回答，可以比較：

- 結論是否相同；
- 推理鏈是否重複；
- 是否提供新證據；
- 是否忽略主要反例；
- 是否在短摘要與完整展開間保持一致。

---

# 11. 系統架構

## 11.1 邏輯分層

```text
輸入層
├─ 人類文字
├─ AI 回答
├─ 文件
├─ 引用與資料集
└─ 程式與測試結果

語義解析層
├─ 命題拆解
├─ 節點分類
├─ 邊關係判定
├─ 來源映射
└─ 重複與新穎度分析

圖儲存層
├─ 節點儲存
├─ 關係儲存
├─ 向量索引
├─ 版本歷史
└─ 原始材料儲存

視圖生成層
├─ R0 導航視圖
├─ R1 快速視圖
├─ R2 分析視圖
├─ R3 研究視圖
└─ R4 稽核視圖

服務層
├─ 搜尋
├─ 展開
├─ 摺疊
├─ 比較
├─ 更新
└─ 匯出
```

## 11.2 建議資料實體

### Node

```json
{
  "id": "node_001",
  "type": "claim",
  "canonical_text": "核心主張",
  "status": "contested",
  "created_at": "2026-07-17T00:00:00+08:00",
  "updated_at": "2026-07-17T00:00:00+08:00",
  "source_ids": ["source_001"],
  "version": 1
}
```

### Edge

```json
{
  "id": "edge_001",
  "from": "node_002",
  "to": "node_001",
  "relation": "supports",
  "weight": 0.82,
  "confidence": 0.74
}
```

### ResolutionView

```json
{
  "node_id": "node_001",
  "resolution": 1,
  "content": "快速理解視圖",
  "covered_nodes": ["node_001", "node_002", "node_003"],
  "omitted_branches": ["node_017"],
  "graph_hash": "sha256:...",
  "generator_version": "0.1"
}
```

### Source

```json
{
  "id": "source_001",
  "type": "raw_text",
  "content_uri": "storage://...",
  "author_type": "ai",
  "provenance": {
    "model": "unknown",
    "session": "session_001"
  }
}
```

---

# 12. 核心演算法偽程式碼

## 12.1 輸入聚合

```python
def ingest(raw_input):
    units = semantic_decompose(raw_input)
    affected_nodes = set()

    for unit in units:
        candidates = retrieve_similar_nodes(unit)
        match = choose_best_match(unit, candidates)

        if match and similarity(unit, match) >= DUPLICATE_THRESHOLD:
            register_recurrence(match, unit)
            affected_nodes.add(match.id)
        else:
            node = create_node(unit)
            relations = infer_relations(node, candidates)
            save_node_and_relations(node, relations)
            affected_nodes.add(node.id)

    invalidate_affected_views(affected_nodes)
    return affected_nodes
```

## 12.2 漸進展開

```python
def expand(node_id, target_resolution, user_context=None):
    graph_slice = retrieve_local_subgraph(
        node_id=node_id,
        resolution=target_resolution,
        context=user_context
    )

    fingerprint = compute_fingerprint(
        node_id=node_id,
        resolution=target_resolution,
        graph_slice=graph_slice
    )

    cached = get_cached_view(node_id, target_resolution)

    if cached and cached.graph_hash == fingerprint:
        return cached

    view = render_from_sources(
        graph_slice=graph_slice,
        resolution=target_resolution
    )

    save_view(view, fingerprint)
    return view
```

## 12.3 預載入

```python
def prefetch_candidates(current_node, session):
    neighbors = get_neighbors(current_node)

    ranked = sorted(
        neighbors,
        key=lambda node: prefetch_score(
            current=current_node,
            candidate=node,
            session=session
        ),
        reverse=True
    )

    return ranked[:PREFETCH_LIMIT]
```

---

# 13. 計算效率

## 13.1 不載入全圖

假設完整圖包含 $$|V|$$ 個節點，而一次互動只需局部子圖 $$G_v^{(k)}$$，則理想情況下單次展開成本主要取決於：

$$
\left|G_v^{(k)}\right| \ll |V|
$$

若向量索引、關係索引與快取均可用，檢索成本可近似寫為：

$$
O(\log |V| + |G_v^{(k)}|)
$$

而非：

$$
O(|V|)
$$

## 13.2 重複論證壓縮

假設共有 $$n$$ 次輸入，其中只有 $$m$$ 個實質不同的論證，且 $$m\ll n$$，則 MRASG 儲存完整結構的主要成本可由接近 $$n$$ 降為接近：

$$
O(m+n_r)
$$

其中 $$n_r$$ 是重現事件、來源與版本紀錄的輕量資料。

## 13.3 生成成本控制

生成式模型只在下列情況被調用：

- 新輸入需要語義拆解；
- 新節點需要建立短視圖；
- 指紋變更導致視圖失效；
- 使用者要求更高解析度；
- 系統進行定期綜合。

未被展開的長視圖不必預先生成。

---

# 14. 可信度與安全限制

## 14.1 壓縮失真

短視圖可能遺漏少數但重要的反例。因此每個視圖應揭示：

- 是否存在重大反對；
- 是否省略分支；
- 是否仍有未解問題；
- 是否只在特定條件成立。

## 14.2 模型生成錯誤

展開視圖必須以來源檢索為前提，並保存來源映射。不得把模型自由生成內容偽裝成原始資料。

## 14.3 權重操控

同一模型的大量重複輸出不應直接增加可信度。系統需要：

- 來源去重；
- 模型族群辨識；
- 語義重複懲罰；
- 獨立證據權重；
- 使用者或 Agent 身分隔離。

## 14.4 過度收斂

系統不應為追求單一答案而刪除少數分支。被駁回或低權重的論證仍應保留於歷史與稽核層。

## 14.5 隱私與權限

原始材料、壓縮視圖與公開節點可以具有不同權限。某個公開摘要不代表其全部來源都可以公開。

---

# 15. 最小可行產品

## 15.1 MVP 目標

第一版不需要建立完整論壇，只需證明以下閉環：

1. 輸入多篇長文；
2. 自動拆解成論證節點；
3. 建立支持與反對關係；
4. 生成三個解析度視圖；
5. 初始只載入短視圖；
6. 點擊後局部展開；
7. 新增材料後只更新受影響節點；
8. 每個視圖可追溯至原始來源。

## 15.2 第一版範圍

第一版建議只支援：

- Claim；
- Support；
- Evidence；
- Objection；
- Rebuttal；
- Open Question。

解析度只做：

- $$R_0$$：一句話；
- $$R_1$$：短摘要；
- $$R_2$$：完整局部論證。

## 15.3 第一版技術模組

```text
mrasg/
├─ ingest/
│  ├─ parser.py
│  ├─ segmenter.py
│  └─ classifier.py
├─ graph/
│  ├─ models.py
│  ├─ repository.py
│  └─ relations.py
├─ retrieval/
│  ├─ semantic_search.py
│  └─ neighborhood.py
├─ rendering/
│  ├─ resolution_0.py
│  ├─ resolution_1.py
│  └─ resolution_2.py
├─ cache/
│  ├─ fingerprint.py
│  └─ invalidation.py
├─ api/
│  └─ server.py
├─ tests/
└─ examples/
```

## 15.4 第一版 API

```text
POST /sources
POST /ingest
GET  /nodes/{id}
GET  /nodes/{id}/view?resolution=0
GET  /nodes/{id}/view?resolution=1
GET  /nodes/{id}/view?resolution=2
GET  /nodes/{id}/neighbors
POST /nodes/{id}/expand
POST /nodes/{id}/rebuild
```

---

# 16. 驗證指標

## 16.1 壓縮忠實度

檢查短視圖中的主張是否可被原始材料支持：

$$
F_k
=
\frac{\text{可追溯陳述數}}
{\text{視圖總陳述數}}
$$

## 16.2 重要分支召回率

$$
R_k
=
\frac{\text{視圖涵蓋的重要分支數}}
{\text{應涵蓋的重要分支總數}}
$$

## 16.3 重複壓縮率

$$
D
=
1-
\frac{\text{實質論證節點數}}
{\text{原始輸入論證數}}
$$

## 16.4 局部載入節省率

$$
L
=
1-
\frac{\text{單次實際載入節點數}}
{\text{完整相關圖節點數}}
$$

## 16.5 增量更新節省率

$$
U
=
1-
\frac{\text{實際重建節點數}}
{\text{可被完整重建的節點數}}
$$

## 16.6 展開一致性

不同解析度視圖不得互相矛盾。可檢查：

$$
C(R_i,R_j)
=
1-
\operatorname{ContradictionRate}(R_i,R_j)
$$

---

# 17. 後續研究方向

1. 超圖式多主張證據關係；
2. 多模型獨立性與來源相關性估計；
3. 自動辨識定義衝突與語義漂移；
4. 基於使用路徑的自適應解析度；
5. 跨語言論證節點對齊；
6. 時序版本圖與過時證據衰減；
7. 人類與 AI 混合治理；
8. 可形式驗證的論證鏈；
9. 圖式上下文編譯器；
10. 將 MRASG 作為 Agent 的外部工作記憶；
11. 將程式碼、測試與執行結果納入證據節點；
12. 以多解析度圖取代傳統長上下文直接拼接。

---

# 18. 核心命題

MRASG 的核心命題可以寫為：

> 當生成資訊的成本持續下降，真正稀缺的將不再是文字，而是可追溯的結構、局部可載入的關係，以及能從短索引可靠還原至完整證據空間的能力。

其演算法精神不是：

> 將所有內容摘要得更短。

而是：

> 將龐大內容編譯成可逐層存取的語義圖，使任何節點都能從最小表示開始，依需求回到其完整論證、證據與歷史脈絡。

因此，MRASG 並不是單純的論壇排序演算法，也不是摘要工具。它更接近一種：

**大規模論證內容的語義編譯器、漸進式載入協定與可追溯知識執行層。**

---

# 19. 結論

多解析度論證語義圖以「點、線、面、體」組織複雜討論，並以共同來源、多層視圖、局部檢索、增量更新與來源映射解決大規模 AI 內容的結構化問題。

它特別適合資訊生成量遠大於人類閱讀能力的時代。當數十個、數百個甚至數百萬個 AI 對同一問題產生支持、反對、反駁與補充時，系統不應把它們堆積成無限時間線，而應將其編譯為可導航的論證空間。

第一版實作不必先決定最終產品。可以先建立一個通用引擎，輸入多篇長文，輸出多解析度論證圖。完成後，再根據實驗結果決定它最適合成為：

- 研究協作引擎；
- AI 論證聚合器；
- 長文閱讀器；
- Agent 記憶系統；
- 程式碼與設計審查系統；
- 政策論證平台；
- 或其他尚未被命名的新型知識介面。

---

## 附錄 A：最小節點關係示例

```text
[Claim C1]
「增加模型能力不必然降低總推理成本」

├─ supports ← [Support S1]
│  └─ cites ← [Evidence E1]
│
├─ opposed_by ← [Objection O1]
│  └─ rebutted_by ← [Rebuttal R1]
│
├─ qualified_by ← [Qualification Q1]
│
└─ raises → [Open Question U1]
```

## 附錄 B：最小解析度示例

### $$R_0$$

模型能力提升不必然降低總推理成本。

### $$R_1$$

更強的模型可能減少單次錯誤與重試，但也可能被配置到更複雜的任務，因此整體計算量未必下降。主要爭議在於應以單次任務、單位成果，還是全系統需求衡量成本。

### $$R_2$$

完整呈現支持理由、反對意見、適用條件、可驗證指標、相關案例、來源與尚未解決的測量問題。此層直接從原始節點與證據集合生成，不由 $$R_1$$ 自由擴寫。

---

**文件狀態：** 可直接進入 MVP 原型實作。  
**下一階段建議：** 先做單機 Python 原型，以 JSON 或 SQLite 儲存節點、關係、來源與三層視圖，再加入瀏覽器式點擊展開介面。
