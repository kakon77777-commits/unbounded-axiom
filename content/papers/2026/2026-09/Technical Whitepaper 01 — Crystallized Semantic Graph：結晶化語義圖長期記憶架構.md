# Technical Whitepaper 01
## Crystallized Semantic Graph：結晶化語義圖長期記憶架構
### An AI-Native Long-Term Memory Architecture Based on Crystallized Semantic Graphs

**系列：** UNPNP / Crystallized Computation Technical Whitepapers  
**白皮書編號：** TW-01  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** 技術白皮書／AI 長期記憶／語義圖／搜尋與結晶化架構  
**狀態：** Canonical Draft  

---

## 摘要

大型 AI 系統的長期記憶問題，不只是「要不要保存更多文字」，而是：

> 當完整歷史已經可以大量保存時，AI 如何在需要時快速找到真正相關、可驗證、可回溯、可重新展開的少量記憶？

若每次都把全部原始對話重新載入，則：

$$
C_{\mathrm{context}}
\rightarrow
\text{very large}.
$$

若只保存極短 summary，則又可能產生：

$$
C_{\mathrm{loss}}
\rightarrow
\text{high}.
$$

本文提出 **Crystallized Semantic Graph，CSG**，中文稱為**結晶化語義圖**。其核心不是刪除原始對話，而是建立多層記憶：

$$
\boxed{
\text{Raw Canonical Memory}
\rightarrow
\text{Semantic Crystals}
\rightarrow
\text{Crystallized Semantic Graph}
\rightarrow
\text{Active Working Memory}.
}
$$

原始對話：

$$
R_i
$$

始終作為 canonical source 保存；AI 以同步或非同步方法，對其生成一個或多個高資訊密度的語義結晶：

$$
C_i^{(\theta)}
=
K_\theta(R_i),
$$

其中：

$$
\theta
$$

可依使用者、任務、模型、領域、時間與壓縮策略改變。

因此：

$$
\boxed{
C_i^{(\theta)}
\neq
R_i,
}
$$

且：

$$
\boxed{
C_i^{(\theta)}
\text{ never replaces }
R_i.
}
$$

每個 semantic crystal 必須保留 provenance hyperlink：

$$
C_i^{(\theta)}
\xrightarrow{\text{source}}
R_i[a:b],
$$

可在需要精確文字、公式、語境或驗證時展開回原始來源。

所有結晶共同形成：

$$
\boxed{
\mathcal G_C=(V,E)
}
$$

甚至更一般的 typed semantic hypergraph：

$$
\mathcal H_C=(V,\mathcal E).
$$

節點可以是：

- 對話結晶；
- 主題結晶；
- 專案結晶；
- 時間段結晶；
- 高階結晶；
- contradiction crystal；
- decision crystal；
- unresolved crystal。

邊則可以是：

- continues；
- refines；
- contradicts；
- supports；
- derived-from；
- implements；
- updates；
- supersedes；
- related-to；
- source-of。

查詢時，系統不直接把全部歷史放進 context，而使用 query expansion、dynamic semantic revealing、graph traversal、DRC、exact search、temporal search、counter-evidence search 與其他 Omphalos-style methods，先顯影出一個很小的 active memory region：

$$
\boxed{
\mathcal M_t^{\mathrm{active}}
=
\Pi_{\xi_t}(\mathcal G_C),
}
$$

且理想上：

$$
|\mathcal M_t^{\mathrm{active}}|
\ll
|\mathcal M_{\mathrm{stored}}|.
$$

只有需要精確驗證時，才：

$$
C_j
\xrightarrow{\text{expand}}
R_j[\text{relevant spans}].
$$

因此本文提出核心原則：

$$
\boxed{
\text{Crystal First, Source on Demand}.
}
$$

CSG 不等同 vector database、summary archive 或 static knowledge graph。它是一個**多視圖、多尺度、可回溯、可重結晶、可失效、可搜尋且可自我改寫的 AI-native memory routing substrate**。

本文同時將 SEDB 定位為 canonical storage / indexing / provenance layer，將 Omphalos / AUSI 定位為 memory search-method runtime，將 CSG 定位為 semantic routing overlay，將 raw conversation store 定位為不可被 derived crystal 取代的 canonical source。

本文最後提出 memory breathing：

$$
\boxed{
\text{Reveal}
\rightarrow
\text{Expand}
\rightarrow
\text{Link}
\rightarrow
\text{Converge}
\rightarrow
\text{Crystallize}
}
$$

成功 retrieval path 本身也可以被結晶：

$$
P_{\mathrm{memory}}
\rightarrow
\widehat{\ell}_{\mathrm{memory}},
$$

使未來相似 recall 更快。

**關鍵詞：** Crystallized Semantic Graph、CSG、AI Memory、Long-Term Memory、Semantic Crystal、SEDB、Omphalos、Dynamic Semantic Revealing、Hypergraph、Provenance、Memory Routing

---

# 1. 問題定義

長期 AI 記憶至少同時面對四個互相衝突的要求：

$$
\boxed{
\text{Capacity}
+
\text{Retrievability}
+
\text{Faithfulness}
+
\text{Cost}.
}
$$

只增加 storage：

$$
S\uparrow
$$

不能直接解決 retrieval。

只增加 summary：

$$
C_{\mathrm{summary}}\downarrow
$$

則可能增加語義損失。

因此真正問題是：

> 如何讓巨大記憶保持潛伏，只在需要時顯影出少量高價值結構？

---

# 2. 四層記憶模型

本文提出：

$$
\boxed{
\mathcal M
=
(
\mathcal R,
\mathcal C,
\mathcal G,
\mathcal A
).
}
$$

其中：

- $\mathcal R$：Raw Canonical Memory；
- $\mathcal C$：Crystallized Semantic Memory；
- $\mathcal G$：Graph / Hypergraph Routing Layer；
- $\mathcal A$：Active Working Memory。

---

# 3. Raw Canonical Memory

對每一段原始對話、文件、訊息或事件：

$$
R_i.
$$

原始來源原則：

$$
\boxed{
R_i
\text{ is canonical}.
}
$$

它不因為 summary、embedding 或 crystal 出現而被覆蓋。

---

# 4. 為什麼 Raw 必須保留？

因為 derived memory 可能：

- 壓縮錯誤；
- 過度概括；
- 遺失語境；
- 忽略反例；
- 過時；
- 受模型偏差影響。

所以：

$$
\boxed{
\text{Derived}
\neq
\text{Canonical}.
}
$$

---

# 5. Semantic Crystal

令結晶方法：

$$
K_\theta.
$$

則：

$$
\boxed{
C_i^{(\theta)}
=
K_\theta(R_i).
}
$$

其目標不是「最短」。

而是：

$$
\boxed{
\max
\frac{
\text{retrievable useful semantics}
}{
\text{representation cost}
}.
}
$$

---

# 6. 一個來源可以有多個 Crystal

同一：

$$
R_i
$$

可以有：

$$
C_i^{(\mathrm{technical})},
$$

$$
C_i^{(\mathrm{conceptual})},
$$

$$
C_i^{(\mathrm{chronological})},
$$

$$
C_i^{(\mathrm{project})},
$$

$$
C_i^{(\mathrm{minimal})}.
$$

因此：

$$
\boxed{
\text{one source}
\rightarrow
\text{multiple semantic projections}.
}
$$

---

# 7. 為什麼不能只保留一個 Summary？

因為 compression 本身是 task-relative。

某個 technical summary 對：

> 找程式設計決策

很好。

但對：

> 找概念演化

可能很差。

所以：

$$
\boxed{
\text{compression is contextual}.
}
$$

---

# 8. SemanticCrystal 最小 Schema

第一版：

```text
SemanticCrystal
- crystal_id
- source_ids[]
- source_spans[]
- crystal_level
- view_type
- method_id
- method_version
- content
- keywords[]
- concepts[]
- claims[]
- entities[]
- temporal_scope
- project_scope
- confidence
- faithfulness
- unresolved_flags[]
- contradiction_flags[]
- access_envelope
- provenance_links[]
- semantic_links[]
- created_at
- updated_at
- stale_state
- digest
```

---

# 9. Source Span

一個 crystal 不只要指回：

$$
R_i.
$$

最好還能指到：

$$
R_i[a:b].
$$

或多段：

$$
\{
R_i[a_1:b_1],
R_i[a_2:b_2]
\}.
$$

---

# 10. Provenance Hyperlink

因此：

$$
\boxed{
C_i
\xrightarrow{\text{provenance}}
R_i[a:b].
}
$$

這是一種 memory hyperlink。

---

# 11. Hyperlink 的三個功能

CSG 中 hyperlink 至少有：

$$
\boxed{
\text{Navigation}
+
\text{Provenance}
+
\text{Expansion}.
}
$$

---

# 12. Crystallized Semantic Graph

令：

$$
V_C
=
\{
C_1,
C_2,
\ldots,C_n
\}.
$$

則：

$$
\boxed{
\mathcal G_C
=
(V_C,E_C).
}
$$

---

# 13. Typed Edge

每條邊：

$$
e_{ij}
=
\langle
C_i,
\tau,
C_j,
w,
p
\rangle.
$$

其中：

- $\tau$：relation type；
- $w$：confidence / weight；
- $p$：provenance。

---

# 14. 建議 Edge Types

第一版至少：

```text
continues
refines
supports
contradicts
updates
supersedes
derived_from
implements
example_of
depends_on
same_topic
same_project
same_entity
same_decision
caused_by
reopens
```

---

# 15. 為什麼需要 Hypergraph？

很多語義關係不是：

$$
C_1\rightarrow C_2.
$$

而是：

$$
\{
C_1,C_2,C_3,C_4
\}
\rightarrow
C_5.
$$

例如：

> 四輪不同對話共同導出一個新理論。

因此：

$$
\boxed{
\mathcal H_C
=
(V_C,\mathcal E_C).
}
$$

更一般。

---

# 16. 公開名稱可以仍叫 Graph

工程底層可以 hypergraph。

對外仍稱：

$$
\boxed{
\text{Crystallized Semantic Graph}.
}
$$

避免名稱過度複雜。

---

# 17. 多尺度結晶

CSG 不只是一輪對話一個 node。

可以：

$$
C^{(1)}
=
\text{micro crystal},
$$

$$
C^{(2)}
=
\text{conversation crystal},
$$

$$
C^{(3)}
=
\text{topic crystal},
$$

$$
C^{(4)}
=
\text{project crystal},
$$

$$
C^{(5)}
=
\text{meta crystal}.
$$

---

# 18. Higher-Order Crystallization

若：

$$
C_1,\ldots,C_n
$$

形成穩定主題，

可：

$$
\boxed{
K^{(2)}
(
C_1,\ldots,C_n
)
=
C^{(2)}.
}
$$

---

# 19. 向下可追

任何：

$$
C^{(k)}
$$

都應能：

$$
C^{(k)}
\rightarrow
C^{(k-1)}
\rightarrow
\cdots
\rightarrow
R.
$$

因此：

$$
\boxed{
\text{high-level memory remains decompressible}.
}
$$

---

# 20. 同步結晶

新對話剛結束時：

$$
K_{\mathrm{sync}}.
$$

目標：

- 快；
- 低成本；
- 保持 freshness；
- 生成基本 continuity node。

---

# 21. 同步結晶不應做太多

第一版：

$$
K_{\mathrm{sync}}
$$

只需產生：

- short crystal；
- main concepts；
- source links；
- temporal metadata；
- project hints。

---

# 22. 非同步結晶

後續：

$$
K_{\mathrm{async}}.
$$

可以做：

- cross-conversation dedup；
- contradiction detection；
- concept evolution；
- higher-order crystal；
- graph restructuring；
- relation repair；
- compression refinement。

---

# 23. Sync / Async 分工

$$
\boxed{
\text{Sync preserves continuity;}
}
$$

$$
\boxed{
\text{Async improves structure}.
}
$$

---

# 24. 非同步不等於永久背景推理

它可以是：

- event-driven；
- batch；
- low-load window；
- user-triggered；
- maintenance cycle。

---

# 25. Crystal First, Source on Demand

查詢：

$$
q.
$$

先：

$$
q
\rightarrow
\mathcal G_C.
$$

而不是：

$$
q
\rightarrow
\mathcal R.
$$

因此：

$$
\boxed{
\text{Crystal First, Source on Demand}.
}
$$

---

# 26. Query Pipeline

第一版：

$$
\boxed{
q_0
\rightarrow
Q_{\mathrm{expand}}
\rightarrow
\Pi_{\xi}
\rightarrow
F_C
\rightarrow
T_G
\rightarrow
C^\*
\rightarrow
R^\*
}
$$

其中：

- $Q_{\mathrm{expand}}$：query expansion；
- $\Pi_\xi$：semantic revealing；
- $F_C$：crystal frontier；
- $T_G$：graph traversal；
- $C^\*$：selected crystals；
- $R^\*$：optional raw expansion。

---

# 27. Query Expansion

使用：

- synonyms；
- project aliases；
- entity aliases；
- historical names；
- concept descendants；
- semantic neighbors。

---

# 28. Dynamic Semantic Revealing

定義：

$$
\boxed{
\Pi_{\xi}
:
\mathcal G_C
\rightarrow
\mathcal G_C^{\mathrm{visible}}.
}
$$

其中：

$$
\xi
=
(q,g,c,t,o,a,w).
$$

---

# 29. Active Memory

$$
\boxed{
\mathcal M_t^{\mathrm{active}}
=
\Pi_{\xi_t}(\mathcal G_C).
}
$$

理想：

$$
|\mathcal M_t^{\mathrm{active}}|
\ll
|\mathcal M_{\mathrm{stored}}|.
$$

---

# 30. Graph Traversal

可依：

- relation type；
- confidence；
- recency；
- project；
- source authority；
- contradiction；
- semantic distance；

決定 traversal。

---

# 31. Retrieval 不只找「最像」

純 embedding similarity：

$$
S_{\mathrm{vec}}
$$

不足。

還需要：

$$
\boxed{
\text{semantic similarity}
+
\text{relation structure}
+
\text{time}
+
\text{provenance}
+
\text{task state}.
}
$$

---

# 32. Omphalos Memory Runtime

Omphalos / AUSI 的 search-method abstraction 可以被重用。

Web provider：

$$
\text{Google / Grok / Brave / Crossref}.
$$

Memory provider 則可變成：

$$
\boxed{
\text{SEDB}
+
\text{CSG}
+
\text{Raw Store}.
}
$$

---

# 33. Memory Search Methods

至少可以使用：

- exact search；
- keyword；
- semantic；
- query reformulation；
- temporal；
- version；
- graph；
- citation / provenance chase；
- counter-evidence；
- DRC；
- semantic revealing；
- exploratory；
- entity；
- contradiction search。

---

# 34. SEDB 的定位

本文建議：

$$
\boxed{
\text{SEDB}
=
\text{canonical structured storage / index / provenance layer}.
}
$$

---

# 35. CSG 的定位

$$
\boxed{
\text{CSG}
=
\text{semantic routing overlay}.
}
$$

---

# 36. Raw Store 的定位

$$
\boxed{
\text{Raw Store}
=
\text{canonical transcript / source layer}.
}
$$

---

# 37. 三者不要混為一體

因此：

$$
\boxed{
\text{SEDB}
\neq
\text{CSG}
\neq
\text{Raw Store}.
}
$$

---

# 38. 建議 Storage Layout

```text
/raw/
  conversation/
  document/
  event/

/crystal/
  micro/
  conversation/
  topic/
  project/
  meta/

/graph/
  edge/
  hyperedge/
  reverse-index/

/receipt/
  crystallization/
  retrieval/
  invalidation/
```

---

# 39. Canonical ID

每個 source：

$$
source\_id.
$$

每個 crystal：

$$
crystal\_id.
$$

每個 edge：

$$
edge\_id.
$$

均應 versioned。

---

# 40. Versioning

crystal 不應 silent overwrite。

例如：

$$
C_i^{v1}
\rightarrow
C_i^{v2}.
$$

---

# 41. Stale State

若 source 更新：

$$
R_i^{v2}\neq R_i^{v1},
$$

依賴：

$$
C_j
$$

可能變：

$$
\text{stale}.
$$

---

# 42. Dependency Invalidation

建立：

$$
D(C_j)
=
\{
R_i,
C_k,\ldots
\}.
$$

若其中 dependency 更新：

$$
C_j
\rightarrow
\text{revalidate}.
$$

---

# 43. 不要直接刪舊 Crystal

舊版可以：

$$
\text{retired}
$$

但保留 provenance。

這有助於理解概念演化。

---

# 44. Temporal Memory

對某概念：

$$
X
$$

可以有：

$$
C_X(t_1),
C_X(t_2),
\ldots
$$

形成：

$$
\boxed{
\text{concept evolution chain}.
}
$$

---

# 45. Supersedes 不等於 Delete

如果：

$$
C_2
\text{ supersedes }
C_1,
$$

仍保留：

$$
C_1.
$$

因為使用者可能問：

> 以前怎麼想？

---

# 46. Contradiction Preservation

如果：

$$
C_a
\bot
C_b,
$$

不要硬壓成一個「共識」。

保留：

$$
\boxed{
\text{contradiction edge}.
}
$$

---

# 47. Minority Memory

低頻、少數、未解決資訊不應因壓縮被消失。

可標：

$$
\text{unresolved}.
$$

---

# 48. Decision Memory

某些對話真正重要的是：

> 最後決定了什麼？

可建立：

$$
C_{\mathrm{decision}}.
$$

並 link：

$$
\text{proposal}
\rightarrow
\text{decision}
\rightarrow
\text{implementation}.
$$

---

# 49. Open-Loop Memory

尚未完成事項：

$$
C_{\mathrm{open}}.
$$

可用：

$$
\text{reopens}
$$

link 在新對話中重新顯影。

---

# 50. Retrieval Confidence

每個 recall result：

$$
m_j
$$

可帶：

$$
Conf(m_j).
$$

但 confidence 不能被當成 source truth。

---

# 51. Faithfulness

定義：

$$
F(C_i,R_i).
$$

表示 semantic crystal 對來源的忠實度。

---

# 52. Coverage

$$
Cov(C_i,R_i)
$$

表示重要資訊覆蓋率。

---

# 53. Information Density

$$
D_I(C_i)
=
\frac{
I_{\mathrm{useful}}
}{
|C_i|
}.
$$

---

# 54. Retrieval Gain

$$
G_R
=
C_{\mathrm{raw-retrieval}}
-
C_{\mathrm{crystal-retrieval}}.
$$

---

# 55. Semantic Loss

$$
L_S
=
1-F.
$$

高壓縮不應讓：

$$
L_S
$$

失控。

---

# 56. Memory Crystal Utility

可定義：

$$
\boxed{
U_M(C)
=
w_rG_R
+
w_dD_I
+
w_fF
+
w_cCov
-
w_sC_{\mathrm{store}}
-
w_uC_{\mathrm{update}}
-
w_lL_S.
}
$$

---

# 57. 不一定每個 Source 都要多視圖

Series 08 的原則同樣適用：

$$
\boxed{
\text{selective crystallization}.
}
$$

---

# 58. Hot Memory

高頻被召回的 crystal：

$$
f_{\mathrm{recall}}\uparrow
$$

可以：

- 建更快 index；
- 生成更高階 crystal；
- 預連結常用 source。

---

# 59. Cold Memory

低頻但仍重要：

$$
\text{persist}
$$

即可。

不必重度結晶。

---

# 60. Forgetting 與 Retiring

本文不主張 derived crystal 永遠保留。

可以：

$$
\text{active}
\rightarrow
\text{cold}
\rightarrow
\text{retired}.
$$

但 canonical raw source 是否刪除應由獨立 retention policy 決定。

---

# 61. Memory Retrieval Receipt

每次 retrieval 留：

```text
query_id
expanded_queries[]
revealed_crystals[]
traversed_edges[]
opened_sources[]
selected_memory[]
cost
latency
verification_state
```

---

# 62. Retrieval Path

一次成功 recall：

$$
P_M
=
(
C_{12},
C_{47},
C_{93},
R_{93}
).
$$

---

# 63. Memory Path Crystallization

若相似查詢常走：

$$
P_M,
$$

可：

$$
\boxed{
K(P_M)
=
\widehat{\ell}_M.
}
$$

未來：

$$
q
\xrightarrow{\widehat{\ell}_M}
C^\*.
$$

---

# 64. 這就是記憶版 Path Compilation

所以 CSG 與 UNPNP 不是分離的。

它是：

$$
\boxed{
\text{UNPNP principles applied to semantic memory}.
}
$$

---

# 65. Memory Breathing

完整：

$$
\boxed{
\text{Reveal}
\rightarrow
\text{Expand}
\rightarrow
\text{Link}
\rightarrow
\text{Converge}
\rightarrow
\text{Crystallize}.
}
$$

---

# 66. Reveal

從巨大 graph 顯影 relevant region。

---

# 67. Expand

找：

- neighbor concepts；
- source spans；
- contradiction；
- temporal versions；
- project links。

---

# 68. Link

建立：

- retrieval path；
- evidence chain；
- source chain。

---

# 69. Converge

生成：

$$
\mathcal M_t^{\mathrm{active}}.
$$

---

# 70. Crystallize

把成功 recall 結構更新回 graph。

---

# 71. Graph 自我改寫

因此：

$$
\boxed{
\mathcal G_{C,t+1}
\neq
\mathcal G_{C,t}.
}
$$

---

# 72. 但不能由單次 Recall 任意改圖

graph mutation 需要：

- evidence；
- thresholds；
- provenance；
- conflict handling。

---

# 73. Graph Edge Confidence

每條新 edge：

$$
e
$$

可以有：

$$
w_e.
$$

重複 evidence 才提升。

---

# 74. Edge Promotion

$$
\text{candidate}
\rightarrow
\text{weak}
\rightarrow
\text{strong}.
$$

---

# 75. Edge Demotion

如果 contradiction 或 source update：

$$
\text{strong}
\rightarrow
\text{weak / stale}.
$$

---

# 76. User-Adaptive Compression

不同使用者可能偏好：

- 技術；
- 敘事；
- 決策；
- 時間；
- 專案；
- 人物；
- 概念。

所以：

$$
\theta_{\mathrm{user}}
$$

應可調。

---

# 77. AI-Adaptive Compression

AI 也可依 recall performance 動態選：

$$
K_{\theta_1},
K_{\theta_2},
\ldots
$$

哪種壓縮更有效。

---

# 78. 不應只有一個全球最優壓縮器

因為：

$$
\boxed{
\forall u
\exists\theta_u
\centernot\Rightarrow
\exists\theta^\*
\forall u.
}
$$

---

# 79. Compression Method Registry

可建立：

```text
method_id
name
version
domain
compression_goal
cost_profile
quality_profile
supported_views
```

---

# 80. 同步 / 非同步方法可以不同

例如：

$$
K_{\mathrm{sync}}
=
\text{cheap model},
$$

$$
K_{\mathrm{async}}
=
\text{deep model / multi-pass}.
$$

---

# 81. Model-Agnostic Storage

Crystal schema 不應綁死某個模型。

這有利：

$$
M_A
\rightarrow
\mathcal G_C
\leftarrow
M_B.
$$

---

# 82. Cross-Model Memory

若 schema 與 provenance 穩定，

不同 AI 可以使用同一 CSG。

---

# 83. 但 Cross-Model Interpretation 仍需驗證

不同模型對同 crystal 可能理解不同。

所以：

$$
\boxed{
\text{shared representation}
\neq
\text{identical interpretation}.
}
$$

---

# 84. Privacy / Access Envelope

每個 source / crystal 需要：

$$
A(C_i).
$$

例如：

- private；
- project；
- team；
- public；
- restricted。

---

# 85. Crystal 不能放大權限

如果：

$$
R_i
$$

是 restricted，

derived：

$$
C_i
$$

不能自動變 public。

所以：

$$
\boxed{
A(C_i)
\subseteq
A(R_i).
}
$$

---

# 86. Multi-Source Crystal Access

若：

$$
C
=
K(R_1,R_2),
$$

則 access envelope 應至少不寬於最嚴格 source。

---

# 87. Security Principle

$$
\boxed{
\text{Crystallization}
\not\Rightarrow
\text{permission expansion}.
}
$$

---

# 88. Sensitive Metadata

某些 entity / project relation 本身就敏感。

所以 edge 也要 access control。

---

# 89. Graph Query 必須 Permission-Aware

$$
\Pi_{\xi}
$$

應包含：

$$
a
=
\text{authorization context}.
$$

---

# 90. Stale Permission

如果 source access 被撤銷，

依賴 crystals 也要 invalidate / hide。

---

# 91. Cold / Warm / Hot Memory Layer

可借用：

$$
\boxed{
\text{Cold}
\rightarrow
\text{Warm}
\rightarrow
\text{Hot}.
}
$$

---

# 92. Cold

Raw source 或低頻 crystal。

---

# 93. Warm

Canonical JSON、常用 crystal、graph neighborhood。

---

# 94. Hot

當前 active memory objects。

---

# 95. Hot 不應永久存在

session / task 結束後可釋放。

---

# 96. Materialization

只在需要時把 crystal 轉成模型可用 working object。

---

# 97. Lazy Source Expansion

只有 validator 或 user request 需要精確 source 時才開 raw。

---

# 98. Progressive Expansion

一開始：

$$
C^{(4)}
$$

若不足，

展開：

$$
C^{(3)}.
$$

再不足：

$$
C^{(2)}.
$$

最後：

$$
R.
$$

---

# 99. 多尺度 Progressive Retrieval

因此：

$$
\boxed{
\text{meta crystal}
\rightarrow
\text{topic crystal}
\rightarrow
\text{conversation crystal}
\rightarrow
\text{raw span}.
}
$$

---

# 100. Retrieval Budget

設定：

$$
B_R.
$$

系統只展開到 budget 足夠的深度。

---

# 101. Confidence Escalation

若：

$$
Conf<\theta_C,
$$

則：

$$
\text{expand deeper}.
$$

---

# 102. Precision Escalation

若使用者問：

> 原話是什麼？

直接：

$$
C\rightarrow R.
$$

---

# 103. Memory Search Modes

建議：

```text
fast_recall
balanced_recall
deep_recall
source_exact
contradiction_check
timeline_recall
project_recall
```

---

# 104. fast_recall

只走高階 crystal。

---

# 105. deep_recall

允許 graph traversal + raw expansion。

---

# 106. source_exact

偏 exact / provenance。

---

# 107. contradiction_check

主動找：

$$
C_a\bot C_b.
$$

---

# 108. timeline_recall

按：

$$
t_1\rightarrow t_2\rightarrow\cdots
$$

重建演化。

---

# 109. project_recall

沿 project crystal 展開。

---

# 110. Failure Mode：Summary Drift

多輪結晶若：

$$
C^{(1)}
\rightarrow
C^{(2)}
\rightarrow
C^{(3)}
$$

卻不回 raw，

可能 drift。

---

# 111. Anti-Drift

Higher-order crystal 應週期性重新對 canonical raw 做抽樣驗證。

---

# 112. Failure Mode：Consensus Collapse

多來源壓縮後只保留主流結論。

---

# 113. Anti-Consensus Collapse

保留：

- contradiction；
- minority；
- unresolved；
- confidence。

---

# 114. Failure Mode：Graph Explosion

每段對話連太多 edge。

---

# 115. Edge Utility

只保存：

$$
U_E(e)>0
$$

的 edge。

---

# 116. Failure Mode：Over-Crystallization

所有 source 都生成十幾種 view。

維護爆炸。

---

# 117. Selective Multi-View

只有高價值 source 才建立多 view。

---

# 118. Failure Mode：Stale Crystal

原始 source 更新，derived 不更新。

---

# 119. Dependency-Based Invalidation

靠 source version / digest 自動標 stale。

---

# 120. Failure Mode：Privacy Leakage

derived crystal 比 raw permission 更寬。

---

# 121. Access Inheritance

強制：

$$
A(C)\subseteq A(R).
$$

---

# 122. Failure Mode：Retrieval Loop

graph traversal 反覆繞圈。

---

# 123. Traversal Controls

需要：

- visited set；
- depth；
- cost；
- relation filters；
- stopping condition。

---

# 124. Failure Mode：Bad Memory Shortcut

成功一次 retrieval 就 crystallize。

---

# 125. Memory EHPE

需要：

$$
U_M(P_M)>0
$$

才 promotion。

---

# 126. Minimal Runtime Architecture

```text
Raw Store
   ↓
Sync Crystallizer
   ↓
SEDB Canonical Records
   ↓
CSG Graph Builder
   ↓
Async Crystallizer / Relation Miner
   ↓
Omphalos Memory Search Runtime
   ↓
Semantic Revealing
   ↓
Active Memory Assembler
   ↓
Source Expander / Validator
   ↓
Retrieval Receipt
```

---

# 127. Write Path

新 source：

$$
R_i
$$

進 Raw Store。

---

# 128. Sync Path

$$
R_i
\rightarrow
C_i^{\mathrm{sync}}.
$$

---

# 129. Async Path

$$
\{
C_i
\}
\rightarrow
\text{relation / higher-order update}.
$$

---

# 130. Read Path

$$
q
\rightarrow
\mathcal G_C^{\mathrm{visible}}
\rightarrow
C^\*
\rightarrow
R^\*.
$$

---

# 131. Repair Path

source / graph 變更：

$$
\text{invalidate}
\rightarrow
\text{recrystallize}.
$$

---

# 132. Recommended MVP Scope

第一版只支援：

- conversation raw；
- one sync crystal；
- one async topic crystal；
- typed edges；
- source spans；
- exact + semantic + graph search；
- retrieval receipt。

---

# 133. MVP 不必先做

- fully autonomous graph rewrite；
- dozens of compression methods；
- universal user personalization；
- distributed multi-tenant graph；
- complex enterprise IAM。

---

# 134. Phase 0

Synthetic conversations。

驗證：

- schema；
- provenance；
- progressive expansion。

---

# 135. Phase 1

真實長對話 dataset。

比較：

$$
\text{raw-only}
$$

與：

$$
\text{crystal-first}.
$$

---

# 136. Phase 2

加入 multi-conversation topic crystal。

---

# 137. Phase 3

加入 contradiction / temporal evolution。

---

# 138. Phase 4

加入 memory path crystallization。

---

# 139. Phase 5

加入 personalized compression strategy。

---

# 140. Benchmark 1：Recall Accuracy

使用人工標註問題。

測：

$$
Acc_{\mathrm{recall}}.
$$

---

# 141. Benchmark 2：Source Faithfulness

答案是否能正確回指來源。

---

# 142. Benchmark 3：Context Reduction

$$
R_C
=
\frac{
|Context_{\mathrm{CSG}}|
}{
|Context_{\mathrm{raw}}|
}.
$$

---

# 143. Benchmark 4：Latency

$$
T_{\mathrm{recall}}.
$$

---

# 144. Benchmark 5：Retrieval Cost

$$
C_{\mathrm{retrieval}}.
$$

---

# 145. Benchmark 6：Raw Expansion Rate

$$
R_{\mathrm{raw}}
=
\frac{
N_{\mathrm{raw-open}}
}{
N_{\mathrm{query}}
}.
$$

---

# 146. Benchmark 7：Contradiction Retention

測不同觀點是否被錯誤合併。

---

# 147. Benchmark 8：Temporal Fidelity

測「以前／後來」是否能正確區分。

---

# 148. Benchmark 9：Stale Detection

source change 後多久能標 stale。

---

# 149. Benchmark 10：Graph Maintenance Cost

$$
C_M.
$$

---

# 150. Baseline A

Raw full-text search。

---

# 151. Baseline B

Vector DB + chunks。

---

# 152. Baseline C

Single summary per conversation。

---

# 153. Experimental D

CSG multi-scale + provenance。

---

# 154. Experimental E

CSG + memory path crystallization。

---

# 155. Success Condition

理想：

$$
Acc_D
\ge
Acc_B,
$$

且：

$$
C_D<C_B,
$$

以及：

$$
Context_D<Context_B.
$$

---

# 156. Stronger Success

再加：

$$
F_{\mathrm{source}}
\uparrow,
$$

$$
T_{\mathrm{timeline}}
\uparrow,
$$

$$
R_{\mathrm{contradiction}}
\uparrow.
$$

---

# 157. Frozen-Model Memory Experiment

固定：

$$
\theta_{\mathrm{model}}.
$$

只讓：

$$
\mathcal G_C
$$

與：

$$
\mathcal K_M
$$

演化。

---

# 158. 若 Recall 仍改善

可證明：

$$
\boxed{
\text{memory architecture learning}
}
$$

而非模型變強。

---

# 159. Cross-Model Test

同一 CSG 給不同模型。

測：

- recall；
- source trace；
- interpretation variance。

---

# 160. CSG 與 UNPNP 的統合

UNPNP 計算 crystal：

$$
\kappa_{\mathrm{exec}}
$$

回答：

> 怎麼做？

CSG semantic crystal：

$$
\kappa_{\mathrm{sem}}
$$

回答：

> 知道什麼？

---

# 161. 雙向 Hyperlink

未來可：

$$
\kappa_{\mathrm{sem}}
\leftrightarrow
\kappa_{\mathrm{exec}}.
$$

---

# 162. 例如

概念記憶：

> 某專案使用某 routing strategy。

可以直接 link 到：

$$
\kappa_{\mathrm{routing}}.
$$

---

# 163. 知識與操作逐步合流

因此長期可能形成：

$$
\boxed{
\text{Semantic Memory Graph}
+
\text{Computational Crystal Graph}.
}
$$

---

# 164. 但第一版應分開

避免：

- debugging 困難；
- privilege 混淆；
- source / action 混淆。

---

# 165. 核心命題一

$$
\boxed{
\textbf{
AI 長期記憶的主要問題不是容量，而是如何把巨大記憶轉化為可尋址、可回溯、可逐層展開的語義結晶網路。
}
}
$$

---

# 166. 核心命題二

$$
\boxed{
\textbf{
Semantic crystal 永遠是 derived representation，不能取代 canonical raw source。
}
}
$$

---

# 167. 核心命題三

$$
\boxed{
\textbf{
同一來源可以有多個 context-relative crystal；不存在必須唯一的「完美摘要」。
}
}
$$

---

# 168. 核心命題四

$$
\boxed{
\textbf{
真正有效的記憶搜尋應先在結晶圖中路由，再按需展開來源，而不是每次重新閱讀全部歷史。
}
}
$$

---

# 169. 核心命題五

$$
\boxed{
\textbf{
成功的 retrieval path 本身也可以被結晶，讓記憶系統逐步學會如何更快找到自己的記憶。
}
}
$$

---

# 170. 第一版總模型

寫入：

$$
R_i
\xrightarrow{K_{\mathrm{sync}}}
C_i
\xrightarrow{G}
\mathcal G_C.
$$

非同步：

$$
\mathcal G_C
\xrightarrow{K_{\mathrm{async}}}
\mathcal G_C'.
$$

查詢：

$$
q
\xrightarrow{Q}
q'
\xrightarrow{\Pi_\xi}
\mathcal G_C^{\mathrm{visible}}
\xrightarrow{T}
C^\*
\xrightarrow{\text{optional expand}}
R^\*.
$$

---

# 171. 結論

當儲存越來越便宜時，AI 記憶問題反而會更明顯。

因為：

> 「我保存了」與「我能在需要時準確找回」完全是兩件事。

如果一個 AI 有十億段歷史，

但每次回答都必須重新掃描，

那麼：

$$
\text{storage capacity}
$$

沒有真正轉化為：

$$
\text{usable memory}.
$$

Crystallized Semantic Graph 的目標，就是在：

$$
\boxed{
\text{完整保存}
}
$$

與：

$$
\boxed{
\text{快速工作記憶}
}
$$

之間建立一層可持續演化的語義結晶。

原始歷史仍然存在：

$$
R.
$$

但系統平常操作：

$$
C.
$$

大量：

$$
C
$$

形成：

$$
\mathcal G_C.
$$

當下只顯影：

$$
\mathcal M^{\mathrm{active}}.
$$

需要驗證時再：

$$
C\rightarrow R.
$$

於是：

$$
\boxed{
\text{巨大記憶可以保持潛伏，而不必每次進入 context。}
}
$$

而當某種 recall 路徑反覆有效，

它還可以：

$$
P_M
\rightarrow
\widehat{\ell}_M.
$$

因此系統不只：

> 記住內容。

它也開始：

> 記住自己應該怎麼找記憶。

這使長期記憶從：

$$
\text{archive}
$$

轉向：

$$
\boxed{
\text{adaptive semantic routing substrate}.
}
$$

最終，CSG 的核心可以收束為三句：

$$
\boxed{
\textbf{
Raw memory preserves truth source.
}
}
$$

$$
\boxed{
\textbf{
Crystals preserve retrievable semantics.
}
}
$$

$$
\boxed{
\textbf{
Hyperlinks preserve the ability to move between abstraction and source.
}
}
$$

因此：

$$
\boxed{
\textbf{
結晶化語義圖不是摘要資料庫，
而是一個可展開、可回溯、可自我重組的 AI 長期記憶世界。
}
}
$$

---

## 下一份技術白皮書

**Technical Whitepaper 02｜UNPNP Game Experimental Runtime：以單機遊戲驗證自適應超連結與計算結晶化**

將把 Series 10 的研究路線直接落成：

- runtime modules；
- event schema；
- trace schema；
- crystal schema；
- benchmark harness；
- frozen-model protocol；
- A/B/C baselines；
- Phase 0–4；
- success / failure gates；
- future legacy-program recompilation interface。
