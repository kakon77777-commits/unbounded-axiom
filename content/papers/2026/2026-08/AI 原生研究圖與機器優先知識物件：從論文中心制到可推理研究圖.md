# AI 原生研究圖與機器優先知識物件：從論文中心制到可推理研究圖

**English Title:** AI-Native Research Graphs and Machine-First Knowledge Objects: From Paper-Centric Scholarship to Reasoning-Aware Research Graphs  
**Series:** AI-Native Knowledge Expansion, Paper V  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10

## 摘要

前四篇已依序建立 Base Knowledge Space Expansion（BKSE）的四個核心元件：可靠基礎知識的結構展開、變種身份與命題分叉、錯誤鄰域與反例空間，以及多證法與交叉驗證的 Proof Lattice。本篇進一步提出：若這些結構主要由 AI 生成、驗證、修正與重組，則「論文」未必仍應是研究系統的最小或主要知識物件。

本文提出 **AI-Native Research Graph（ANRG）** 與 **Machine-First Knowledge Object（MFKO）** 作為工作框架。研究系統的基本單位不再只是 PDF、Markdown 論文或自然語言段落，而是具有穩定身份、型別、父子 lineage、依賴、證據、證明、反例、驗證狀態、等價類、版本、計算產物與開放問題的機器可操作節點。人類論文則被重新定位為這張研究圖的一種 rendering：

\[
\boxed{
\text{Paper}
=
\operatorname{RenderHuman}(G,\mathcal S)
}
\]

其中 \(G\) 是研究圖，\(\mathcal S\) 是選定的子圖與敘述策略。

本文並不聲稱 machine-readable research objects 是全新的思想。RO-Crate、Nanopublications、W3C PROV、OpenAlex 等系統已分別提供研究封裝、細粒度 assertion/provenance、來源追蹤與 scholarly graph 基礎；2026 年出現的 ScienceClaw + Infinite 與 XScientist 更已提出 artifact DAG、parent lineage、claim-to-evidence anchors、agent-native research artifacts 與可重播研究歷史。本文的工作重點是把這些方向與 BKSE 內部的 proposition identity、variation certificate、error neighborhood、proof lattice 與 open frontier 統一到「可推理知識節點」層，並提出一個面向 AI 自主研究的最小 schema 與 runtime。

本文的核心命題是：

\[
\boxed{
\text{The paper need not be the ontology of research.}
}
\]

論文可以繼續作為重要的人類溝通介面，但 AI 原生研究的內部知識本體可以是一張可持續演化、可驗證、可查詢、可分叉與可重新渲染的研究圖。

**關鍵詞：** AI 原生研究圖；機器優先知識物件；研究物件；知識圖；provenance；nanopublication；RO-Crate；Proof Lattice；BKSE；agent-native research artifact

---

## 1. 問題：為什麼研究一定要先變成論文？

傳統學術流程大致是：

\[
\text{Idea}
\rightarrow
\text{Experiment / Proof}
\rightarrow
\text{Paper}
\rightarrow
\text{Archive}.
\]

論文同時承擔：

- 問題描述；
- 背景；
- 方法；
- 推導；
- 結果；
- 引用；
- 版本；
- 作者責任；
- 人類閱讀。

在以人為中心的研究環境中，這非常合理。

但在 AI-native research 中，真正的操作可能是：

\[
\text{claim}
\rightarrow
\text{mutation}
\rightarrow
\text{proof}
\rightarrow
\text{counterexample}
\rightarrow
\text{repair}
\rightarrow
\text{generalization}
\rightarrow
\text{verification}
\rightarrow
\text{new frontier}.
\]

如果每一步都必須先重新轉寫成完整自然語言論文，研究 runtime 會產生大量不必要的：

\[
\text{serialization cost}.
\]

因此本文反問：

\[
\boxed{
\text{What if papers are views rather than primary knowledge objects?}
}
\]

---

## 2. 論文中心制的資訊壓縮

一篇論文其實是對完整研究歷史的高度壓縮。

設真實研究過程為：

\[
H
=
(
h_1,h_2,\ldots,h_n
).
\]

其中可能包括：

- 失敗實驗；
- 被否證假設；
- 不採用 proof；
- 程式版本；
- 中間資料；
- reviewer correction；
- replacement lemma；
- 不同模型結果；
- 無效 branch。

最後發表文本：

\[
P_{\mathrm{paper}}
=
\operatorname{Compress}(H).
\]

通常：

\[
|P_{\mathrm{paper}}|
\ll
|H|.
\]

這種壓縮對人類閱讀是必要的。

但若 AI 下一輪研究需要重新利用被壓掉的分支，PDF 本身可能不是理想儲存格式。

因此：

\[
\boxed{
\text{Human-efficient representation}
\neq
\text{machine-efficient research state}.
}
\]

---

## 3. Machine-First Knowledge Object

本文定義一個最小 Machine-First Knowledge Object：

\[
\boxed{
K_i
=
(
id,
type,
payload,
relations,
provenance,
verification,
version
)
}
\]

其中：

- `id`：穩定唯一識別；
- `type`：節點型別；
- `payload`：命題、程式、資料、proof 或其他核心內容；
- `relations`：與其他節點關係；
- `provenance`：來源、生成者、工具與 parent lineage；
- `verification`：可檢查狀態；
- `version`：版本與修訂歷史。

這裡的重要改變是：

> **自然語言不是必填的知識本體。**

某個節點可以主要由：

```text
formal statement
proof term
dependency IDs
counterexample IDs
verification results
```

構成。

需要對人類展示時，再生成自然語言。

---

## 4. 節點型別

第一版 ANRG 可以只使用有限型別：

```text
CLAIM
DEFINITION
ASSUMPTION
PROOF
LEMMA
COUNTEREXAMPLE
ERROR_NODE
EQUIVALENCE
GENERALIZATION
SPECIALIZATION
COMPUTATION
EXPERIMENT
DATASET
CODE
BENCHMARK
CORRECTION
OPEN_QUESTION
```

其中最重要的是不要把所有內容都壓成：

```text
MESSAGE
```

或：

```text
DOCUMENT
```

AI-native graph 需要知道：

\[
\text{this object is a proof}
\]

與：

\[
\text{this object is an objection}
\]

不是同一資料型態。

---

## 5. 邊型別

相同地，邊也應是 typed relation：

```text
PROVES
REFUTES
DEPENDS_ON
DERIVED_FROM
MUTATES
EQUIVALENT_TO
GENERALIZES
SPECIALIZES
CORRECTS
REPLACES
CHECKED_BY
SUPPORTED_BY
CONTRADICTS
IMPLEMENTS
BENCHMARKS
OPENS
RESOLVES
```

所以研究圖：

\[
G=(V,E)
\]

不是普通 citation graph。

citation graph 常見：

\[
\text{Paper}_A
\rightarrow
\text{Paper}_B.
\]

ANRG 則希望知道：

\[
\text{Proof}_{17}
\xrightarrow{PROVES}
\text{Claim}_{42},
\]

\[
\text{Counterexample}_{9}
\xrightarrow{REFUTES}
\text{Claim}_{55},
\]

以及：

\[
\text{Claim}_{55}
\xrightarrow{MUTATES}
\text{Claim}_{56}.
\]

---

## 6. 現有 Scholarly Graph 與 ANRG 的差異

OpenAlex 與 Semantic Scholar 已提供大規模 scholarly graph。

它們可以表示：

- works；
- authors；
- institutions；
- sources；
- topics；
- citations。

這對全球文獻導航非常重要。

但 ANRG 研究的是更細的粒度：

\[
\boxed{
\text{inside-paper epistemic structure}.
}
\]

也就是：

- 哪一個 claim？
- 哪一條 proof？
- 哪個 assumption？
- 哪一個反例？
- 哪個 experiment 支持哪個 claim？
- 哪個 correction 取代哪個舊節點？

因此：

\[
\boxed{
\text{Scholarly Graph}
\neq
\text{Reasoning Graph}.
}
\]

兩者可以互相連接，但不應混為同一層。

---

## 7. 與 Nanopublication 的關係

Nanopublication 提供非常重要的鄰近模型。

一個 nanopublication 大致由：

\[
\text{Assertion}
+
\text{Provenance}
+
\text{Publication Info}
\]

構成。

這個設計的關鍵價值在於：

> 一個小型 claim 本身可以成為可引用、可追蹤 provenance 的獨立物件。

而且 nanopublication 不只適用於正面資料，也可以表達：

- hypothesis；
- claim；
- negative result；
- opinion。

因此 ANRG 不需要重新發明：

\[
\text{atomic assertion + provenance}.
\]

本文的擴張點在於：

\[
\boxed{
\text{assertion}
\rightarrow
\text{reasoning lifecycle node}.
}
\]

亦即一個 claim 不只是被發布，而是持續連接：

- mutation；
- proof；
- refutation；
- equivalence；
- repair；
- open frontier。

---

## 8. 與 RO-Crate 的關係

RO-Crate 已提供 research object 的 machine-readable packaging。

目前 RO-Crate 1.3 使用 JSON-LD，能描述：

- Dataset；
- Data Entities；
- Contextual Entities；
- people；
- software；
- workflows；
- provenance。

因此 ANRG 可以直接借用其核心哲學：

\[
\boxed{
\text{research artifacts should travel with structured metadata}.
}
\]

但 ANRG 的基本單位比一般 research package 更偏向「推理節點」。

可以說：

\[
\text{RO-Crate}
\]

適合封裝：

\[
\text{research object package},
\]

而：

\[
\text{MFKO}
\]

則描述：

\[
\text{reasoning-addressable object}.
\]

未來甚至可以：

\[
\boxed{
\text{ANRG export}
\rightarrow
\text{RO-Crate package}.
}
\]

---

## 9. Provenance 不是附加 metadata

W3C PROV-O 將 provenance 建模為 Entity、Activity、Agent 與它們之間的生成、使用、歸屬等關係。

AI-native research 必須把 provenance 提升為一級資料。

因為同一個 claim：

\[
C
\]

若分別來自：

\[
\text{human},
\]

\[
\text{LLM},
\]

\[
\text{formal theorem prover},
\]

\[
\text{simulation},
\]

\[
\text{physical experiment},
\]

其 epistemic status 顯然不同。

因此：

\[
\boxed{
\text{Content without lineage is incomplete research state}.
}
\]

---

## 10. 將前四篇統一進研究圖

Paper I：

\[
\text{Base Knowledge Expansion}
\]

對應：

```text
CLAIM
MUTATES
GENERALIZES
SPECIALIZES
```

Paper II：

\[
\text{Variation Identity}
\]

對應：

```text
variation_certificate
equivalence_class
branch_id
canonical_form
```

Paper III：

\[
\text{Error Neighborhood}
\]

對應：

```text
ERROR_NODE
COUNTEREXAMPLE
REFUTES
REPAIR
```

Paper IV：

\[
\text{Proof Lattice}
\]

對應：

```text
PROOF
CHECKED_BY
DEPENDS_ON
AXIOM
FORMALIZATION
```

所以 ANRG 不是額外的新模組。

它是：

\[
\boxed{
\text{the shared substrate of Papers I–IV}.
}
\]

---

## 11. 一個完整 Claim Node

例如：

```text
id: RT-0178
type: CLAIM
domain: euclidean/right_triangle
statement:
  h = 2r + r^2/R
status: VERIFIED
parents:
  - RT-0001
  - RT-0042
dependencies:
  - pythagorean_theorem
  - triangle_area
  - inradius_identity
  - circumradius_identity
proofs:
  - PF-0178-A
  - PF-0178-B
counterexamples:
  - none_found
formalizations:
  - lean: pending
equivalence_class:
  - RT-EQ-83
frontier:
  - OQ-31
  - OQ-44
novelty:
  literature_checked: false
```

這裡最重要的一行甚至可能是：

```text
novelty.literature_checked = false
```

因為：

\[
\boxed{
\text{derived by AI}
\neq
\text{new to mathematics}.
}
\]

---

## 12. Open Frontier 是一級物件

傳統 paper 結尾可能有：

> Future work includes...

在 ANRG 中，這不應只是文字。

定義：

```text
id: OQ-44
type: OPEN_QUESTION
generated_from: RT-0178
question:
  characterize feasible (R,h) pairs
status: OPEN
priority: 0.67
dependencies:
  - RT-0178
  - RT-0180
```

於是 agent 可以直接查：

```text
unresolved_neighbors(RT-0178, depth=3)
```

而不是重新讀十篇論文找「有哪些問題還沒做」。

---

## 13. Research Query Language

ANRG 可以提供機器查詢：

```text
dependencies(CLAIM-17)?
proof_paths(CLAIM-17)?
counterexamples(CLAIM-17)?
equivalent_claims(CLAIM-17)?
generalizations(CLAIM-17)?
open_questions(CLAIM-17)?
semantic_audits(CLAIM-17)?
failed_branches(CLAIM-17)?
```

更高階：

```text
find claims:
  verified = true
  proof_family_count >= 2
  literature_checked = false
  open_frontier > 0
```

這種查詢就是 AI-native research navigation。

---

## 14. 論文成為 Rendering

當研究圖已保存完整內容時：

\[
\text{Paper}
\]

可以變成函數：

\[
\boxed{
P_H
=
\operatorname{RenderHuman}
(
G,
Q,
A,
L
)
}
\]

其中：

- \(G\)：研究圖；
- \(Q\)：選取的 research question；
- \(A\)：audience；
- \(L\)：length/style constraint。

同一子圖可以輸出：

- 兩頁摘要；
- 20 頁論文；
- 教材；
- reviewer report；
- machine-readable proof appendix；
- public explanation；
- API schema。

因此：

\[
\boxed{
\text{one knowledge graph}
\rightarrow
\text{many human interfaces}.
}
\]

---

## 15. 這不代表人類文章沒有價值

自然語言論文仍具有至少五種重要功能：

1. 整體敘事；
2. 研究重要性判斷；
3. 問題選擇理由；
4. 概念直覺；
5. 社群溝通。

所以本文不是：

\[
\text{paper obsolete}.
\]

而是：

\[
\boxed{
\text{paper is no longer required to be the sole canonical storage layer}.
}
\]

---

## 16. 2026 年外部工作的快速收斂

這裡需要特別保持學術誠實。

截至 2026 年，外部研究已快速接近 machine-first research artifact 的方向。

ScienceClaw + Infinite 提出：

- scientific skill registry；
- artifact DAG；
- full computational lineage；
- typed metadata；
- parent lineage；
- provenance-aware scientific discourse；
- unsatisfied information needs；
- artifact mutation / pruning。

XScientist 則提出 Agent-Native Research Artifact（ARA），保存：

- exploration DAG；
- per-node code；
- outputs；
- claim-to-evidence anchors；
- content hashes；
- provenance；
- re-execution hooks；
- failed branches；
- repaired experiments；
- ablations。

因此本文不宣稱：

\[
\boxed{
\text{agent-native artifact graph}
}
\]

本身是本文首次提出。

更合理的位置是：

> BKSE 與這些近期系統出現高度 convergence，而本文把 research artifact graph 再向 proposition-level mathematical identity、verified variation、error neighborhood 與 proof lattice 做統一。

這是一個較窄、可檢驗的差異。

---

## 17. ANRG 與 XScientist / ScienceClaw 的暫定差異

可以先粗略比較：

### Artifact-first systems

主要問：

> 這次研究 run 產生了什麼 artifact？它從哪個 parent 來？

### ANRG / BKSE

主要問：

> 這個知識節點在理論空間中是什麼身份？它與母命題、等價命題、反例、proof family 與 open frontier 是什麼關係？

因此 ANRG 更偏：

\[
\boxed{
\text{epistemic graph}
}
\]

而不只是：

\[
\text{workflow graph}.
\]

但兩者完全可以整合。

最佳架構可能是：

\[
\boxed{
\text{Workflow DAG}
+
\text{Artifact Graph}
+
\text{Epistemic Graph}.
}
\]

---

## 18. 三層圖架構

本文因此提出：

### Layer 1：Execution Graph

\[
G_X.
\]

保存：

- agent actions；
- tool calls；
- code runs；
- environment；
- execution dependencies。

### Layer 2：Artifact Graph

\[
G_A.
\]

保存：

- files；
- datasets；
- proofs；
- programs；
- reports；
- outputs。

### Layer 3：Epistemic Graph

\[
G_E.
\]

保存：

- claims；
- assumptions；
- definitions；
- refutations；
- equivalence；
- generalization；
- proof relations；
- open questions。

三者映射：

\[
G_X
\rightarrow
G_A
\rightarrow
G_E.
\]

這樣「AI 做了什麼」與「因此我們現在知道什麼」不會混成同一層。

---

## 19. Append-Only Research History

AI-native research 應避免悄悄覆寫歷史。

假設：

\[
C_1
\]

後來被修正成：

\[
C_2.
\]

不應：

```text
overwrite C1
```

而應：

```text
C2 --CORRECTS--> C1
C2 --REPLACES--> C1
```

因此：

\[
\boxed{
\text{correction}
\neq
\text{erasure}.
}
\]

這對：

- provenance；
- reproduction；
- model training；
- failure analysis；
- scientific priority；

都更重要。

---

## 20. Immutable Node 與 Mutable View

一個折衷：

節點 content hash 可以 immutable：

\[
hash(K_i).
\]

但：

```text
current_preferred_version
```

可以更新。

因此：

\[
\boxed{
\text{immutable history}
+
\text{mutable canonical pointer}.
}
\]

這非常接近 version control，而不是 wiki 式直接覆寫。

---

## 21. Knowledge Commit

可以把一次有效研究更新定義成：

\[
\boxed{
\mathcal C_t
=
(
\Delta V,
\Delta E,
\text{provenance},
\text{verification}
)
}
\]

稱為：

\[
\text{Knowledge Commit}.
\]

例如：

```text
commit: KC-221
adds:
  CLAIM-91
  PROOF-102
  OPEN-19
edges:
  PROOF-102 PROVES CLAIM-91
  CLAIM-91 GENERALIZES CLAIM-44
verification:
  lean-kernel: PASS
```

這比：

> 今天寫了一篇新 paper

更接近機器可操作的研究事件。

---

## 22. Fork 與 Merge

如果兩個 agent 對同一 claim 形成不同研究方向：

\[
G_a,
G_b,
\]

不必立即決定誰對。

可以：

\[
\operatorname{Fork}(G).
\]

等後續證據出現，再：

\[
\operatorname{Merge}(G_a,G_b).
\]

如果無法 merge：

\[
\text{maintain competing branches}.
\]

這對仍存在不確定性或多公理系統的數學尤其自然。

---

## 23. 研究圖中的 Unknown

每個節點不能只有：

```text
true / false
```

至少需要：

```text
VERIFIED
DISPROVED
CONFLICTED
UNKNOWN
UNFORMALIZED
UNVERIFIED
SEMANTICALLY_UNAUDITED
LITERATURE_UNCHECKED
```

例如：

\[
\boxed{
\text{formally verified}
+
\text{literature unchecked}
}
\]

是一個完全合理的狀態。

它代表：

> 推導可能正確，但 novelty 尚未確定。

---

## 24. Novelty 是外部關係，不是內部感覺

AI 生成一個沒看過的 theorem：

\[
T^\ast
\]

只能推出：

\[
\text{new-to-this-search}.
\]

不能推出：

\[
\text{new-to-mathematics}.
\]

因此 novelty node 應記：

```text
novelty_status:
  internal_duplicate: false
  literature_search: completed
  databases_checked:
    - ...
  nearest_prior_art:
    - ...
  human_review: pending
```

即：

\[
\boxed{
\text{Novelty}
=
\text{relation between internal graph and external literature graph}.
}
\]

---

## 25. 與 OpenAlex / Semantic Scholar 接軌

ANRG 不需要自己重建全世界 citation graph。

可以把：

\[
G_E
\]

的 literature edges 連到：

- OpenAlex Work ID；
- DOI；
- Semantic Scholar Paper ID；
- arXiv ID；
- ORCID；
- ROR。

因此：

\[
\boxed{
\text{local epistemic graph}
\leftrightarrow
\text{global scholarly graph}.
}
\]

OpenAlex 目前提供 works、authors、sources、institutions、topics 等大型 scholarly catalog；Semantic Scholar Academic Graph API 則提供 papers、authors、citations、venues 等 graph data。這些系統適合作為 ANRG 的外部文獻層，而不是取代 proposition-level graph。

---

## 26. 最小 JSON Schema 草案

第一版可以極簡：

```json
{
  "id": "CLAIM-0178",
  "type": "CLAIM",
  "version": 3,
  "payload": {
    "formal": "h = 2*r + r^2/R",
    "natural_language": null
  },
  "parents": ["CLAIM-0001", "CLAIM-0042"],
  "relations": [
    {"type": "DERIVED_FROM", "target": "CLAIM-0001"}
  ],
  "verification": [
    {
      "method": "symbolic",
      "status": "PASS"
    }
  ],
  "provenance": {
    "generator": "agent-A",
    "timestamp": "...",
    "execution": "RUN-221"
  },
  "frontier": ["OPEN-0031"],
  "literature_status": "UNCHECKED"
}
```

這不是最終標準。

它只證明：

\[
\boxed{
\text{machine-first research object can be small}.
}
\]

---

## 27. AI Board 的可能演化

一個 AI-to-AI board 若只存：

```text
sender
message
timestamp
thread
```

仍主要是一個 communication system。

若擴張為：

```text
type
claim_id
parent_ids
proof_id
evidence_ids
relation
verification
open_frontier
```

它就開始變成：

\[
\boxed{
\text{AI-Native Research Ledger}.
}
\]

Communication layer 與 epistemic layer 可以分離：

\[
\text{Message}
\rightarrow
\text{Research Commit}.
\]

不是每一句聊天都要永久進研究圖。

只有被抽取、驗證、分類的 epistemic object 才進 canonical graph。

---

## 28. 防止組合爆炸

研究圖若無限制擴張：

\[
|V_t|
\rightarrow
\infty.
\]

因此需要：

### Deduplication

\[
\operatorname{Can}(K_i).
\]

### Equivalence clustering

\[
[K].
\]

### Frontier scoring

\[
S_F(K).
\]

### Garbage / low-value pruning

但 pruning 不能等同刪除歷史。

可以：

```text
active = false
archive = true
```

### Budget constraints

\[
\text{expand only if expected information gain > cost}.
\]

---

## 29. Frontier Scheduler

可以定義：

\[
S_F(q)
=
\alpha N
+
\beta U
+
\gamma C
+
\delta V
-
\lambda R
-
\mu K.
\]

其中：

- \(N\)：novelty potential；
- \(U\)：uncertainty / unresolvedness；
- \(C\)：connectivity gain；
- \(V\)：verification feasibility；
- \(R\)：redundancy；
- \(K\)：compute cost。

AI 不再只是：

> 找一個 open question。

而是：

\[
\boxed{
\text{choose the next frontier with highest expected structural gain}.
}
\]

---

## 30. 研究圖作為長期記憶

普通 LLM agent 容易依賴：

\[
\text{conversation history}.
\]

ANRG 則提供：

\[
\text{persistent external epistemic state}.
\]

下一次研究不需要重新讀：

\[
10^6
\]

tokens 的全部歷史。

只查：

```text
current_claims()
unresolved_frontiers()
recent_corrections()
dependency_closure(CLAIM-17)
```

因此 ANRG 也是一種：

\[
\boxed{
\text{research-state compression}.
}
\]

---

## 31. 可重播性

每個重要節點應盡量保存：

- input；
- environment；
- code；
- version；
- seed；
- tool；
- proof certificate；
- parent artifacts。

因此可以：

\[
\operatorname{Replay}(K_i).
\]

對數學 proof：

\[
\operatorname{Replay}
=
\text{recheck proof}.
\]

對程式：

\[
\operatorname{Replay}
=
\text{rebuild + test}.
\]

對實驗：

\[
\operatorname{Replay}
\]

可能只能做到 protocol reproduction，而非完全 deterministic replay。

---

## 32. Human Oversight 仍然存在

Machine-first 不代表 human-excluded。

重要節點可以要求：

```text
human_review:
  required: true
  role: domain_expert
```

尤其：

- semantic alignment；
- ethical significance；
- real-world interpretation；
- publication priority；
- high-impact claim。

因此：

\[
\boxed{
\text{machine-first}
\neq
\text{machine-only}.
}
\]

---

## 33. 最小 MVP

一個 ANRG MVP 不需要建全球平台。

只需要：

### Storage
SQLite / PostgreSQL / graph DB 皆可。

### Node types
先做：

```text
CLAIM
PROOF
COUNTEREXAMPLE
OPEN_QUESTION
```

### Edge types

```text
PROVES
REFUTES
DERIVED_FROM
OPENS
```

### Verifier

Lean + Python tests。

### API

```text
POST /node
POST /edge
GET /claim/{id}
GET /claim/{id}/proofs
GET /claim/{id}/counterexamples
GET /frontier
```

### Renderer

```text
render_markdown(subgraph)
```

這就足夠驗證：

\[
\boxed{
\text{paper-as-rendering}
}
\]

是否實際可行。

---

## 34. 最小實驗

以：

\[
100
\]

個基礎數學命題為 seed。

系統自動生成：

- 500–1000 variations；
- 反例；
- proof；
- open questions。

比較兩種儲存方式。

### Document-Centric

每輪產生 Markdown report。

### Graph-Centric

每個 research event 先寫入 typed graph，最後才 render report。

測量：

1. 重複 token；
2. duplicate theorem rate；
3. dependency retrieval accuracy；
4. correction propagation；
5. proof reuse；
6. open-question recovery；
7. human report generation；
8. long-horizon continuation cost。

核心假說：

\[
\boxed{
C_{\mathrm{continuation}}(G)
<
C_{\mathrm{continuation}}(\text{documents})
}
\]

在長期研究中尤其明顯。

---

## 35. 外部學術定位

截至 2026 年，本文必須避免宣稱「research graph / machine-readable research object / agent-native research artifact」本身的新穎性。

RO-Crate 1.3 已是 Recommendation，使用 JSON-LD 描述 research objects 與 provenance。

Nanopublications 已提供 assertion + provenance + publication info 的細粒度 publishing model。

W3C PROV-O 已提供跨系統 provenance interchange ontology。

OpenAlex 與 Semantic Scholar 已提供大型 scholarly graph。

ScienceClaw + Infinite 與 XScientist 已把 autonomous agents、artifact DAG、lineage、claim-evidence links、failed branches 與 machine-readable artifacts 推進到 agent-native research infrastructure。

因此本文可能的差異必須縮窄為：

\[
\boxed{
\text{BKSE epistemic graph integration}
}
\]

即：

\[
\text{proposition identity}
+
\text{variation lineage}
+
\text{error neighborhood}
+
\text{proof lattice}
+
\text{open frontier}
\]

如何成為同一種 machine-first research substrate。

---

## 36. 研究邊界

本文不主張：

1. 所有研究都能無損表示成圖；
2. 自然語言可以被完全移除；
3. machine-readable object 自動等同可靠知識；
4. provenance 等於 truth；
5. graph database 本身產生科學發現；
6. typed edges 可以解決所有語義歧義；
7. append-only history 永遠優於其他版本模型；
8. AI agent 產生的 claim 不需人類審核；
9. 所有學科都適合同一 schema；
10. 本文已建立一套完整通用 research ontology。

尤其：

\[
\boxed{
\text{Machine Readable}
\neq
\text{Machine Verified}.
}
\]

以及：

\[
\boxed{
\text{Machine Verified}
\neq
\text{Semantically Correct}.
}
\]

---

## 37. 結論

Paper I 建立：

\[
\text{Expansion}.
\]

Paper II 建立：

\[
\text{Identity}.
\]

Paper III 建立：

\[
\text{Falsification}.
\]

Paper IV 建立：

\[
\text{Proof Trust}.
\]

Paper V 將它們放進共同 substrate：

\[
\boxed{
\text{AI-Native Research Graph}.
}
\]

因此研究物件從：

\[
\text{Paper}
\]

轉成：

\[
\boxed{
\text{Machine-First Knowledge Object}.
}
\]

而論文重新被定義為：

\[
\boxed{
\text{Paper}
=
\operatorname{RenderHuman}
(
\text{Research Graph}
).
}
\]

這不是要消滅論文。

恰恰相反，它讓論文回到它最擅長的工作：

\[
\boxed{
\text{human understanding}.
}
\]

而把：

- dependency；
- version；
- proof；
- verification；
- counterexample；
- provenance；
- correction；
- open frontier；

交給更適合保存它們的機器結構。

當 AI 真正開始長期自主研究時，最重要的問題可能不再只是：

> AI 能不能寫一篇論文？

而是：

> AI 能不能維持一個不斷演化、可追溯、可驗證、可分叉、可重播，而且不必每次重新讀完整歷史的研究世界狀態？

本文的回答是：這至少已經是一個可工程化驗證的問題。

下一篇將進一步處理：

\[
\boxed{
\text{Frontier Scheduling and Combinatorial Explosion Control}.
}
\]

也就是：當研究圖可以產生幾百萬、幾十億個合法節點時，AI 應該如何判定下一個值得展開的問題？如何避免把全部算力花在「 technically correct but scientifically irrelevant 」的無聊節點上？

---

## 參考文獻

RO-Crate Community. *RO-Crate Metadata Specification 1.3*. Recommendation, 2026.

Nanopublication Community. *Nanopublication Guidelines*. 2026.

W3C. *PROV-O: The PROV Ontology*. W3C Recommendation.

OpenAlex. *OpenAlex Developer Documentation*.

Semantic Scholar. *Academic Graph API*.

Wang, F. Y., Marom, L., Pal, S., et al. (2026). *Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange*. arXiv:2603.14312.

Luo, J. (2026). *XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery*. arXiv:2607.12301.
