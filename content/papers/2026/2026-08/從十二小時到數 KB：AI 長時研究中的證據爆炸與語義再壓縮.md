---
title: "從十二小時到數 KB：AI 長時研究中的證據爆炸與語義再壓縮"
english_title: "From Twelve Hours to a Few Kilobytes: Evidence Explosion and Semantic Recompression in Long-Horizon AI Research"
series: "AI Epistemic Reconstruction Series"
paper: "05"
author: "Neo.K"
date: "2026-08-14"
version: "v0.1"
document_type: "Research Paper / Systems-and-Epistemology Paper"
language: "zh-Hant"
status: "Research Draft"
---

# 從十二小時到數 KB：AI 長時研究中的證據爆炸與語義再壓縮

## From Twelve Hours to a Few Kilobytes: Evidence Explosion and Semantic Recompression in Long-Horizon AI Research

**作者：Neo.K**  
**系列：AI Epistemic Reconstruction Series — Paper 05**  
**版本：v0.1**  
**日期：2026 年 8 月 14 日**

---

## 摘要

長時 AI Agent 研究存在一個反直覺現象：輸入目標本身可能很小，但為了理解它而產生的 screenshots、execution traces、save files、binary diffs、logs、failed runs、counterexamples、temporary working copies 與中間報告，可能比原始 artifact 大數十倍甚至數百倍。最終真正需要帶入下一輪推理的研究狀態，卻可能只有幾 KB 到幾 MB。

本文將這一過程形式化為：

$$
\boxed{
\text{Legacy / Target Artifact}
\rightarrow
\text{Evidence Explosion}
\rightarrow
\text{Epistemic Semantic Recompression}
}
$$

本文主張，長時 Agent 的主要記憶問題不是單純「上下文太長」，而是三種資料被錯誤混在一起：

1. **Raw Evidence**：不可任意改寫的原始實驗證據；
2. **Epistemic State**：Verified、Invalidated、Unknown、Excluded、Current Frontier 等可續接研究狀態；
3. **Active Context**：當前 subgoal 真正需要進入模型 context 的最小工作集。

因此提出三層架構：

$$
\boxed{
R_t
\rightarrow
K_t
\rightarrow
A_t
}
$$

其中：

- $R_t$：full-fidelity raw evidence store；
- $K_t$：provenance-backed canonical epistemic state；
- $A_t$：task-relative active working context。

本文提出「**Epistemic Sufficient State（ESS）**」概念。對下一步研究決策集合 $\mathcal D$，若壓縮狀態 $K_t=C(R_{0:t})$ 能在容許誤差 $\epsilon$ 內保留使用完整 evidence 所需要的決策資訊，則：

$$
\boxed{
K_t
\text{ is }
\epsilon\text{-sufficient for }\mathcal D
}
$$

形式上可寫為：

$$
d\!\left(
P(a_{t+1}\mid R_{0:t}),
P(a_{t+1}\mid K_t,I_t)
\right)
\le\epsilon,
$$

其中 $I_t$ 為可回溯 raw evidence 的索引／provenance graph。

這一定義的重要含義是：**高品質壓縮不等於刪除 evidence，而是把 evidence 從「每輪都必須讀」轉成「可按需解引用」。**

MemGPT 將有限 context 類比為分層記憶管理；LLMLingua 與 LongLLMLingua 顯示 prompt compression 可降低成本；2026 年的 HiMem、HORMA、MAGE 與 MemexRL 則進一步採用階層化記憶、摘要連結 raw trajectory、execution-state tree 與 indexed external evidence 等設計。本文在這些工作的基礎上，進一步把研究 Agent 的核心記憶單位從「conversation memory」改寫成「**evidence-backed epistemic state**」，並強調 contradiction、excluded runs、版本 scope、provenance pointer 與 replayability 必須在壓縮後仍可恢復。

以一個約十二小時的半黑箱 DOS 遊戲逆向研究作 running case，Agent 的一輪增量產生約 183 MiB 新資料，絕大多數是實驗與工作副本；而最終 handoff 層的語義更新只有數 KB。這個案例顯示：長時研究的真正價值不與 raw bytes 成正比，反而取決於能否把大量局部 observations 收斂成可重播、可反駁、可續接的知識狀態。

**關鍵詞：** Agent Memory, Evidence Compression, Semantic Compression, Long-Horizon Agents, Provenance, Context Management, Epistemic State, Research Agents, Evidence Graph, Memory Consolidation

---

# 1. 問題：為什麼 10 MB 的東西可以研究出幾百 MB？

直覺上，人們容易把：

$$
\text{file size}
$$

等同於：

$$
\text{knowledge complexity}.
$$

但對可執行系統而言，兩者沒有直接比例關係。

一個 binary：

$$
G
$$

可能非常小，

但其可觀測狀態空間：

$$
\mathcal S
$$

與 action space：

$$
\mathcal A
$$

組合後可以產生大量 trajectory：

$$
\tau
=
(s_0,a_0,s_1,a_1,\ldots).
$$

研究 Agent 為了恢復：

$$
\Sigma_G
$$

必須產生：

- snapshots；
- save files；
- diffs；
- logs；
- screenshots；
- hashes；
- hypotheses；
- failed runs；
- replicated runs。

所以：

$$
|E_G|
\gg
|G|
$$

完全可能。

---

# 2. Evidence Explosion

定義 raw evidence stream：

$$
R_t
=
\{e_1,e_2,\ldots,e_t\}.
$$

若每一次 experiment：

$$
a_i
$$

產生：

$$
m_i
$$

個 evidence artifacts，

則：

$$
|R_t|
=
\sum_{i=1}^{t}m_i.
$$

若 experiment 數隨研究時間增長：

$$
|R_t|
\rightarrow\infty
$$

在沒有 retention policy 時自然發生。

---

# 3. Evidence Expansion Factor

定義：

$$
\boxed{
X_E(t)
=
\frac{
\operatorname{Bytes}(R_t)
}{
\operatorname{Bytes}(G)
}
}
$$

 $X_E$ 不是研究品質指標。

它只表示：

> 研究 evidence 相對 target artifact 的物理展開倍率。

---

# 4. 高 $X_E$ 可能很有價值，也可能完全是垃圾

### 高價值情況

```text
10 MB artifact
→ 500 MB controlled experiments
→ 20 MB canonical evidence
→ 100 KB semantic specification
```

### 低價值情況

```text
10 MB artifact
→ 500 MB duplicate screenshots
→ 0 new constraints
```

所以：

$$
\boxed{
\text{Evidence Volume}
\neq
\text{Information Gain}
}
$$

---

# 5. 從 Paper 03 到 Paper 05

Paper 03 定義主動認識重構：

$$
K_t
\rightarrow
\mathcal H_t
\rightarrow
a_t
\rightarrow
E_{t+1}
\rightarrow
K_{t+1}.
$$

Paper 04 又要求：

> contradiction 必須保存。

問題隨即出現：

如果每次都把：

$$
E_1,E_2,\ldots,E_t
$$

全部塞進 context，

則：

$$
\operatorname{ContextLength}(t)
\rightarrow\infty.
$$

---

# 6. Context Explosion 與 Evidence Explosion 不同

Evidence explosion：

> 外部儲存資料越來越多。

Context explosion：

> 模型每輪需要讀的資料越來越多。

兩者不應綁死。

理想：

$$
\boxed{
|R_t|\uparrow
\quad\text{但}\quad
|A_t|\approx bounded
}
$$

---

# 7. 三層記憶模型

本文提出：

$$
\boxed{
R_t
\rightarrow
K_t
\rightarrow
A_t
}
$$

---

# 8. Layer R — Raw Evidence Store

$$
R_t
$$

包含：

- original artifact；
- raw trace；
- experiment output；
- screenshot；
- file diff；
- hash；
- excluded run；
- test result；
- tool output。

原則：

> append-only / immutable-by-default。

---

# 9. Layer K — Canonical Epistemic State

$$
K_t
$$

包含：

```text
VERIFIED
INVALIDATED
PARTIALLY_VERIFIED
UNKNOWN
EXCLUDED
CURRENT_FRONTIER
DEPENDENCIES
NEXT_TESTS
```

以及：

> 每一 claim 對 raw evidence 的 pointer。

---

# 10. Layer A — Active Context

$$
A_t
$$

是模型在目前 subgoal 真正需要的：

```text
current goal
relevant verified facts
relevant contradictions
open hypotheses
next experiments
minimal raw excerpts
```

---

# 11. 核心原則：Active Context 不是 Archive

錯誤：

$$
A_t=R_t.
$$

正確：

$$
A_t
=
Retrieve(K_t,I_t,q_t).
$$

其中：

- $I_t$：index / provenance graph；
- $q_t$：current subgoal。

---

# 12. 與 MemGPT 的接口

MemGPT 將 LLM 有限 context 類比作作業系統的 memory hierarchy。

其核心洞見：

> fast context 與 large external memory 可以分層管理。

本文接受這個系統方向，

但將研究 Agent 的外部 memory 再拆成：

- raw evidence；
- canonical epistemic state。

---

# 13. 為什麼單純 conversation memory 不夠

研究狀態不是：

```text
User said...
Assistant said...
```

而是：

```text
Hypothesis H1 invalidated by E17
Rule R4 verified under DOS v1.02
Experiment B2 incomplete
Offset 0x50 historical prior only
```

---

# 14. Prompt Compression 不是 Epistemic Compression

LLMLingua / LongLLMLingua 的主要問題：

> 如何在較少 token 下保留 prompt 中的重要資訊。

本文的問題不同：

> 哪些資訊根本不應每輪進 context？  
> 哪些 summary 必須連回 raw evidence？  
> 哪些 negative result 絕不能被摘要吃掉？

---

# 15. Token Compression

令：

$$
C_{\mathrm{token}}:
X
\rightarrow
X'
$$

目標：

$$
|X'|<|X|.
$$

---

# 16. Epistemic Compression

令：

$$
C_E:
R_{0:t}
\rightarrow
(K_t,I_t).
$$

目標不是只：

$$
|K_t|<|R_{0:t}|.
$$

還要求：

1. 可支持後續決策；
2. 可查回原證據；
3. contradiction 不遺失；
4. provenance 不斷裂；
5. scope 不混合。

---

# 17. Epistemic Sufficient State

## Definition 1

給研究決策類：

$$
\mathcal D,
$$

若：

$$
K_t=C_E(R_{0:t})
$$

滿足：

$$
d\left(
P(a\mid R_{0:t}),
P(a\mid K_t,I_t)
\right)
\le\epsilon
$$

對：

$$
a\in\mathcal D,
$$

則稱：

$$
K_t
$$

為：

$$
\boxed{
\epsilon\text{-Epistemic Sufficient State}
}
$$

簡稱 ESS。

---

# 18. ESS 是 task-relative

對：

```text
找 Stress offset
```

ESS 可能不需要：

> 所有 UI screenshots。

但對：

```text
重建原 UI timing
```

那些 screenshot 又可能變重要。

所以：

$$
ESS=ESS(q).
$$

---

# 19. 不存在唯一「完美摘要」

同一 evidence store：

$$
R
$$

對不同 subgoal：

$$
q_1,q_2
$$

需要不同：

$$
A(q_1),A(q_2).
$$

因此核心不是產生一份永久摘要，

而是：

$$
\boxed{
\text{Persistent Canonical State}
+
\text{Task-Relative Retrieval}
}
$$

---

# 20. Evidence Pointer

每個 canonical claim：

```yaml
claim:
  id: STRESS_OFFSET
  status: verified
  value: 0x50
```

不能就此結束。

需：

```yaml
evidence:
  - exp_017
  - exp_023
  - negative_control_004
```

---

# 21. Pointer-Preserving Compression

本文定義：

若 compressed state：

$$
K
$$

中的每個高權重 claim 都能透過：

$$
I
$$

解引用到 supporting / contradicting raw evidence，

則稱：

$$
C_E
$$

具有：

$$
\boxed{
\text{Pointer Preservation}
}
$$

---

# 22. 這是「可逆 by reference」

不是：

$$
C_E^{-1}(K)=R
$$

字面可逆。

而是：

> 有需要時，可以從 claim 找回原始證據。

---

# 23. MemexRL 的直接接口

2026 年 MemexRL 提出：

- compact working context；
- structured summaries；
- stable indices；
- full-fidelity interaction 保存在 external database；
- 需要時 dereference index。

這和本文的：

$$
(K_t,I_t,R_t)
$$

高度相容。

---

# 24. 本文再增加一個要求

Memex 型架構重點是：

> 不因 summary-only compression 丟掉 evidence。

研究 Agent 還需要：

> 不因 compression 丟掉 **epistemic status**。

---

# 25. Summary 內容必須有狀態

錯誤摘要：

```text
We investigated offset 0x0334.
```

正確摘要：

```text
0x0334:
  status: unresolved
  H1 weakened
  H2 excluded by protocol
  B2 replication incomplete
```

---

# 26. Negative Memory

長時研究最容易丟掉：

> 已經證明不行的東西。

因為摘要器偏好保存「結論」。

但：

$$
\boxed{
\text{Invalidated Hypotheses}
}
$$

也是高價值知識。

---

# 27. Contradiction Preservation

定義：

$$
CR_t
=
\frac{
N_{\mathrm{invalidated\ claims\ retrievable}}
}{
N_{\mathrm{invalidated\ claims\ total}}
}.
$$

理想：

$$
CR_t\approx1.
$$

---

# 28. 若 $CR_t$ 低

Agent 會：

```text
forget failure
→ propose same hypothesis
→ rerun same experiment
```

形成研究迴圈。

---

# 29. Excluded Run Preservation

Excluded 與 Invalidated 又不同。

例如：

```text
誤點 menu
→ run invalid
```

必須保存：

```text
run excluded
```

但不能寫：

```text
hypothesis false
```

---

# 30. Summary-Only Compression 的危險

如果把：

```text
run A failed due to protocol violation
```

壓成：

```text
run A failed
```

下一個 Agent 可能錯誤地把它當反例。

---

# 31. 所以 semantic compression 不是普通摘要

它要保留：

$$
\boxed{
\text{Status Semantics}
}
$$

---

# 32. 五種核心 Epistemic Status

```text
VERIFIED
PARTIALLY_VERIFIED
INVALIDATED
UNKNOWN
EXCLUDED
```

---

# 33. Current Frontier

另外必須保存：

```text
What exactly remains unresolved?
```

定義：

$$
F_t.
$$

---

# 34. Frontier Preservation Rate

若原始 research state 有：

$$
N_F
$$

個 unresolved frontier，

壓縮後可恢復：

$$
N_F'
$$

定義：

$$
FPR
=
\frac{N_F'}{N_F}.
$$

---

# 35. Next-Action Preservation

更進一步：

壓縮後 Agent 是否仍知道：

> 下一個最有價值實驗是什麼？

---

# 36. Decision Distortion

定義：

$$
\Delta_D
=
d(
\pi(\cdot\mid R),
\pi(\cdot\mid K,I)
).
$$

---

# 37. 好的壓縮

$$
|K|\ll|R|
$$

且：

$$
\Delta_D\approx0.
$$

---

# 38. 壞的壓縮

$$
|K|\ll|R|
$$

但：

$$
\Delta_D\gg0.
$$

例如把關鍵反例刪掉。

---

# 39. Compression Ratio

$$
\boxed{
C_R
=
\frac{
\operatorname{Bytes}(R)
}{
\operatorname{Bytes}(K)
}
}
$$

高 $C_R$ 本身不是越高越好。

---

# 40. Effective Compression

定義：

$$
C_{\mathrm{eff}}
=
C_R(1-\Delta_D).
$$

只是概念性指標。

---

# 41. Provenance Completeness

令：

$$
P_C
=
\frac{
N_{\mathrm{canonical\ claims\ with\ raw\ pointers}}
}{
N_{\mathrm{canonical\ claims}}
}.
$$

---

# 42. Research Memory Quality

可寫：

$$
Q_M
=
f(
1-\Delta_D,
P_C,
CR,
FPR,
Replayability
).
$$

---

# 43. Provenance 不只是 citation

W3C PROV 把 provenance 形式化為：

- Entity；
- Activity；
- Agent；
- derivation；
- generation；
- usage。

對研究 Agent 非常自然。

---

# 44. Agent Research PROV Mapping

### Entity

```text
save file
trace
screenshot
claim
report
```

### Activity

```text
experiment
diff
normalization
compression
validation
```

### Agent

```text
LLM
script
human
tool
```

---

# 45. Claim derivation

```text
Canonical Claim
  wasDerivedFrom
Experiment Result
```

---

# 46. Summary derivation

```text
Handoff Summary
  wasDerivedFrom
Epistemic State
```

所以 summary 本身也有 provenance。

---

# 47. 這防止「摘要看起來像原始事實」

每一層標示：

```text
raw
derived
interpreted
canonical
```

---

# 48. HORMA 的直接接口

2026 的 HORMA：

> 把 experience 組成 file-system-like hierarchy，

並讓 summarized entities 連回 raw trajectories。

這個方向支援本文：

$$
\boxed{
\text{Organize}
\rightarrow
\text{Retrieve Minimal Sufficient Context}
}
$$

---

# 49. HORMA 額外指出一個問題

純 similarity retrieval 可能忽略：

- temporal dependency；
- causal dependency。

研究 Agent 尤其明顯。

---

# 50. 例如

Query：

> 為什麼 B2 還不能 verified？

最相關的不是語義最像 B2 的所有文字，

而是：

```text
B1 baseline
→ B2 protocol
→ excluded run
→ replication gap
```

這是一條 causal / temporal chain。

---

# 51. 所以 Evidence Graph 優於 Bag of Chunks

RAG-only：

$$
RetrieveBySimilarity(q).
$$

研究記憶應：

$$
RetrieveBy(
Semantic,
Dependency,
Provenance,
Status,
Time
).
$$

---

# 52. MAGE 的直接接口

2026 MAGE 把 memory 視為：

> execution-state management。

它使用 state tree：

- Grow；
- Compress；
- Maintain；
- Revise。

並隔離 flawed branches。

這與：

```text
EXCLUDED / INVALIDATED
```

不進 active canonical path 的要求高度一致。

---

# 53. Active Path

令：

$$
P_t
$$

是目前有效研究 trajectory。

錯誤 branch：

$$
B^-.
$$

不應完全刪除，

但不應混進 active path。

---

# 54. Branch Isolation

$$
R
=
P_t
\cup
B^-.
$$

Active Context：

$$
A_t
\subseteq
P_t
$$

除非正在 debugging 舊 branch。

---

# 55. Revise

當新 evidence 推翻某個早期假設：

$$
P_t
$$

需要回到：

$$
t^*
$$

重新分支。

---

# 56. 所以 memory 不是靜態 archive

它是一個：

$$
\boxed{
\text{Versioned Epistemic State Machine}
}
$$

---

# 57. HiMem 的接口

HiMem 區分：

- Episode Memory；
- Note Memory。

具體事件與穩定知識分層。

本文對研究 Agent 對應：

```text
Episode / Raw Evidence
↔
Canonical Epistemic Notes
```

---

# 58. 但研究 Agent 還多一層

一般 note：

> User likes X。

研究 note：

> Rule X verified by experiments A/B, contradicted by C under version V2。

所以：

$$
\boxed{
\text{Knowledge}
+
\text{Evidence Status}
}
$$

不可分。

---

# 59. Context Compression 的四個目標

1. **Cost** 降低；
2. **Decision quality** 保持；
3. **Evidence recoverability** 保持；
4. **Epistemic hygiene** 保持。

---

# 60. 只達成 1 不是成功

如果：

$$
tokens\downarrow
$$

但：

$$
contradiction\ recall\downarrow,
$$

可能讓 Agent 更容易 hallucinate。

---

# 61. Evidence Tiering

本文建議：

```text
L0 — Immutable Source
L1 — Raw Experiment Evidence
L2 — Derived / Normalized Evidence
L3 — Canonical Epistemic State
L4 — Active Context
L5 — Handoff Capsule
```

---

# 62. L0 — Immutable Source

例如：

- original binary；
- original save；
- original version package。

永不改。

---

# 63. L1 — Raw Experiment Evidence

例如：

- screenshots；
- traces；
- dumps；
- logs。

可大量增長。

---

# 64. L2 — Derived Evidence

例如：

- byte diff；
- parsed table；
- normalized trace；
- extracted event sequence。

可重建時可以 cache。

---

# 65. L3 — Canonical Epistemic State

真正長期保存：

```text
claims
status
scope
confidence
dependencies
evidence pointers
```

---

# 66. L4 — Active Context

依 subgoal 動態生成。

---

# 67. L5 — Handoff Capsule

跨 session 最小交接：

```text
goal
latest verified
latest invalidated
frontier
next test
state pointer
```

---

# 68. Handoff Capsule 不是完整 memory

它是：

> 進入完整 memory 的索引頁。

---

# 69. Running Case：十二小時逆向研究

一個長時 Agent session：

- 約十二小時；
- 大量 UI 操作；
- screenshots；
- save/reload；
- work copies；
- protocol failures；
- repeated runs。

---

# 70. 實際增量

該輪研究包相對前版約新增：

$$
183\text{ MiB}
$$

解壓資料。

其中主要落在：

```text
experiments
working copies
```

---

# 71. 而 handoff 層只有幾 KB

這揭露：

$$
\boxed{
\text{Physical Evidence Growth}
\gg
\text{Semantic Frontier Growth}
}
$$

---

# 72. 為什麼？

因為 1000 張 screenshot 可能只共同支持一句：

> B1 protocol 可重現。

---

# 73. Evidence Aggregation

令：

$$
E_1,\ldots,E_n
$$

共同支持：

$$
c.
$$

Canonical state 只需要：

```yaml
claim: c
status: verified
evidence:
  - batch_pointer
```

---

# 74. 但不能只留 c

若未來有人問：

> 你怎麼知道？

必須：

$$
c\rightarrow E_{1:n}
$$

可回溯。

---

# 75. 這就是 Evidence-Backed Compression

本文定義：

$$
\boxed{
\operatorname{EBC}(R)
=
(K,I,R)
}
$$

其中 raw evidence：

$$
R
$$

仍在，

但 active reasoning 主要使用：

$$
K,I.
$$

---

# 76. Semantic Recompression

「recompression」指：

原 artifact 中的 semantics 原本高度隱含：

$$
G.
$$

研究先把它展開：

$$
G\rightarrow R.
$$

再把已理解部分重編碼：

$$
R\rightarrow K.
$$

所以：

$$
\boxed{
\text{Implicit Compression}
\rightarrow
\text{Explicit Evidence Expansion}
\rightarrow
\text{Semantic Recompression}
}
$$

---

# 77. 第一個壓縮態與第二個壓縮態不同

原 binary 的壓縮：

> 對 CPU 可執行。

研究後 semantic state 的壓縮：

> 對 AI / 人類研究者可理解。

---

# 78. 因此不是「壓回原大小」

目標：

$$
\operatorname{Size}(K)
$$

不需要等於：

$$
\operatorname{Size}(G).
$$

而是：

> 最小到足以續接研究。

---

# 79. Lossless / Lossy 不夠描述

傳統壓縮：

- lossless；
- lossy。

研究壓縮應多一個維度：

$$
\boxed{
\text{Epistemically Lossy}
}
$$

---

# 80. Epistemically Lossless-by-Reference

若 active state 丟掉細節，

但 pointer 可恢復，

可稱：

$$
\boxed{
\text{Epistemically Lossless by Reference}
}
$$

---

# 81. Summary-only 通常不是

如果原 evidence 已刪，

summary 錯了就無法回頭。

---

# 82. Raw Evidence Retention Policy

不是所有 raw evidence 永久保留。

可以分：

```text
irreproducible
reproducible
redundant
derived
cache
```

---

# 83. Irreproducible Evidence

例如：

- rare external event；
- costly real-world measurement。

優先保留。

---

# 84. Reproducible Evidence

例如 deterministic script output。

可以：

```text
retain seed + program + hash
```

必要時重建。

---

# 85. Derived Cache

如果：

$$
D=f(R)
$$

且 $f$ 可重跑，

可以不永久保存所有 $D$。

---

# 86. Evidence Garbage Collection

定義：

$$
GC_E
$$

只能刪：

> 可由更底層 evidence + deterministic transform 重建的衍生物。

---

# 87. 不能刪唯一反例

如果：

$$
E^-
$$

是某 hypothesis 唯一 contradiction，

不可因：

> 不常 retrieval

就刪掉。

---

# 88. Evidence Value

可以定義：

$$
V(e)
=
I(e;\mathcal H)
+
Rarity(e)
+
Irreplaceability(e)
+
ProvenanceWeight(e).
$$

---

# 89. Storage Policy

高 $V(e)$：

> cold archive。

低 $V(e)$ 且 reproducible：

> delete / regenerate。

---

# 90. Screenshot Explosion

UI agent 特別容易產生：

$$
N_{\mathrm{frames}}\gg1.
$$

可以：

- keyframe；
- perceptual dedup；
- event segmentation。

---

# 91. 但 screenshot dedup 要小心

兩張看似相同 UI，

可能有：

- hidden cursor；
- timestamp；
- subtle state。

所以 dedup 只影響 storage，

不能自動推論 semantics 一樣。

---

# 92. Trace Compression

raw instruction trace 很大。

可以建立：

```text
function-level summary
basic block summary
state-write summary
```

但保留 raw trace pointer。

---

# 93. Save Diff Compression

不要保存每一份 full save？

可保存：

- baseline hash；
- delta；
- reconstruction rule。

但 canonical benchmark 最好仍保留重要 fixture。

---

# 94. Content-Addressable Evidence

用：

$$
hash(e)
$$

當 evidence ID。

優點：

- dedup；
- integrity；
- immutable pointer。

---

# 95. Evidence Address

```text
sha256:<digest>
```

比：

```text
final2_really_final.png
```

可靠。

---

# 96. Provenance DAG

建立：

$$
G_P=(V,E).
$$

node：

- artifact；
- experiment；
- derived evidence；
- claim。

edge：

- generated-by；
- derived-from；
- supports；
- contradicts；
- normalized-from。

---

# 97. Canonical Claim Graph

$$
G_K
$$

與：

$$
G_P
$$

分離但連結。

---

# 98. Claim Dependency

```text
offset mapping
→ rule inference
→ event model
→ reimplementation
```

如果底層 claim invalidated，

上層 claim 要標 stale。

---

# 99. Compression 必須保存 dependency

否則 Agent 會：

> 改了底層，忘了重驗上層。

---

# 100. Staleness Propagation

若：

$$
c_1\rightarrow c_2
$$

且：

$$
c_1
$$

invalidated，

則：

$$
c_2.status
=
needs\_revalidation.
$$

---

# 101. 這比摘要更像 build system

研究知識有 dependency graph。

修改底層 evidence，

像修改 source file，

要重新 build downstream claims。

---

# 102. Epistemic Build System

本文提出：

$$
\boxed{
\text{Epistemic Build System}
}
$$

輸入：

- raw evidence；
- rules；
- version scope。

輸出：

- canonical knowledge。

---

# 103. Incremental Rebuild

新 evidence：

$$
e_{new}
$$

只重算受影響：

$$
Descendants(e_{new}).
$$

---

# 104. 這可大幅降低長時 Agent 成本

不必每次：

> 重新讀全部歷史。

只讀：

- changed frontier；
- dependency ancestors；
- relevant contradictions。

---

# 105. Context as Incremental Build Cache

Active context：

$$
A_t
$$

可以看成：

> 當前 subgoal 的 build cache。

---

# 106. Cache Miss

若需要細節：

$$
A_t
\rightarrow
I_t
\rightarrow
R_t.
$$

---

# 107. Cache Hit

如果 canonical state 足夠：

> 不讀 raw evidence。

---

# 108. Retrieval Cost

$$
C_R(q)
$$

應進整體 research cost。

---

# 109. Over-Retrieval

把 500 個 irrelevant raw logs 拉回 context，

會：

- 增 token；
- 降 attention density；
- 混淆 state。

---

# 110. Under-Retrieval

只讀 summary，

漏掉反例。

---

# 111. 最佳 retrieval

$$
A_t^*
=
\arg\min_A
|A|
$$

subject to：

$$
DecisionQuality(A)\ge\tau.
$$

---

# 112. Minimal Sufficient Context

這也是 HORMA 類系統所追求的方向。

本文加上：

> sufficient 必須包含 status/provenance，而不只是 semantic relevance。

---

# 113. Research Context Budget

固定：

$$
B_C.
$$

Agent 需在：

$$
|A_t|\le B_C
$$

下最大化：

$$
Q_{\mathrm{decision}}.
$$

---

# 114. Compression Trigger

可以在：

$$
|A_t|>\beta B_C
$$

時啟動。

---

# 115. 但不要等 overflow 才壓

最好 subgoal 完成即：

```text
close branch
→ summarize
→ validate summary
→ archive raw
```

---

# 116. Subgoal Boundary Compression

MAGE 的 Compress / Maintain 概念與此相容。

---

# 117. Summary Validation

任何 summary：

$$
s=C(R)
$$

也可能 hallucinate。

所以需要：

$$
V_s(s,R).
$$

---

# 118. Summary Verifier

檢查：

- claim 是否可追溯；
- status 是否一致；
- contradiction 是否遺失；
- scope 是否正確。

---

# 119. Compression 也必須可被 falsify

如果 summary 說：

```text
B2 verified
```

但 raw evidence：

```text
B2 incomplete
```

summary invalid。

---

# 120. Compression Integrity Test

$$
V_C(K,R)
\rightarrow
pass/fail.
$$

---

# 121. Canonical State Hash

每個：

$$
K_t
$$

可 hash：

```text
state_hash
```

用於 handoff integrity。

---

# 122. Versioned Epistemic State

```text
K_001
K_002
K_003
```

不要 overwrite。

---

# 123. Semantic Diff

$$
\Delta K_t
=
K_t-K_{t-1}.
$$

比每次重讀完整 state 更有效。

---

# 124. Handoff Diff

下一個 Agent 先讀：

```text
last canonical state
+
latest delta
```

---

# 125. Evidence Explosion 的真正瓶頸

不是 disk。

磁碟通常便宜。

瓶頸是：

$$
\boxed{
\text{Attention / Retrieval / Validation}
}
$$

---

# 126. 1 TB raw logs 也許沒問題

只要：

> Agent 不必每輪讀 1 TB。

---

# 127. 所以「大資料」不是本身的錯

錯的是：

$$
\text{Large Archive}
=
\text{Large Working Memory}.
$$

---

# 128. Storage / Cognition 分離

$$
\boxed{
\text{Storage Capacity}
\neq
\text{Cognitive Working Set}
}
$$

---

# 129. 對人類也一樣

科學家不會把所有 paper 全背在 working memory。

他們使用：

- notes；
- indexes；
- references；
- lab notebooks。

---

# 130. AI 可以把這件事工程化

而且比人類更嚴格：

- hash；
- automatic provenance；
- dependency graph；
- replay。

---

# 131. 研究結果的「外顯認知殘留」

長時 Agent 每一次：

- action；
- observation；
- decision；

都可能留下 artifact。

因此 AI cognition 的一部分被物質化：

$$
\boxed{
\text{Ephemeral Computation}
\rightarrow
\text{Persistent Evidence Artifact}
}
$$

---

# 132. 這是 AI 與傳統人類研究的一個差異

人類很多推理：

> 留在腦中。

Agent 可以把大量中間過程自動寫成：

- files；
- logs；
- tests；
- traces。

---

# 133. 優點

可稽核。

---

# 134. 缺點

Evidence Explosion。

---

# 135. 解法不是「不要留」

而是：

$$
\boxed{
\text{Leave Everything Important}
+
\text{Read Almost Nothing by Default}
}
$$

---

# 136. Cold Evidence / Hot Knowledge

## Cold Evidence

$$
R_t.
$$

大、完整、低頻。

## Hot Knowledge

$$
K_t.
$$

小、結構化、高頻。

---

# 137. Warm Index

中間：

$$
I_t.
$$

保存：

- embeddings；
- graph；
- metadata；
- hashes；
- pointers。

---

# 138. 三溫層

```text
HOT   — canonical epistemic state
WARM  — provenance/index/dependency
COLD  — raw evidence
```

---

# 139. Retrieval Escalation

```text
Hot
↓ insufficient
Warm
↓ locate evidence
Cold
↓ inspect raw
```

---

# 140. 這比「一次塞全部」更接近 OS virtual memory

也呼應 MemGPT 的設計精神。

---

# 141. Epistemic Page Fault

當 Agent 發現：

> canonical claim 不足以回答，

觸發：

$$
\boxed{
\text{Epistemic Page Fault}
}
$$

從 cold evidence 載入細節。

---

# 142. Page Fault 不是失敗

它是正常 memory mechanism。

---

# 143. 研究 Agent 的 Cache Policy

可根據：

- recency；
- frontier relevance；
- contradiction risk；
- dependency centrality。

---

# 144. 不應只用 semantic similarity

因為：

> 最重要的 evidence 有時語義不相似，但在 dependency graph 上關鍵。

---

# 145. Contradiction Priority

任何 active hypothesis 的 counterexample：

> 高優先 hot memory。

---

# 146. Frontier Priority

下一個 experiment 依賴的 evidence：

> 高優先。

---

# 147. Verified Stable Knowledge

可留 canonical summary，

raw evidence cold。

---

# 148. Old Excluded Runs

通常 cold，

但 pointer 保留。

---

# 149. Evidence Consolidation Schedule

建議：

```text
per experiment
→ lightweight index update

per subgoal
→ canonical compression

per session
→ handoff capsule

per milestone
→ provenance audit
```

---

# 150. Compression 不能無限遞迴

Summary of summary of summary：

$$
C(C(C(R)))
$$

可能逐步漂移。

---

# 151. Summary Drift

定義：

$$
D_n
=
d(
C^n(R),
Truth(R)
).
$$

可能隨 $n$ 增加。

---

# 152. 解法

Canonical state 更新應：

> 回看 raw pointers 或上一個 validated canonical state，

不要永遠只摘要摘要。

---

# 153. Anchor to Evidence

$$
K_{t+1}
=
Update(K_t,E_{new})
$$

而不是：

$$
K_{t+1}
=
Summarize(K_t\text{ prose}).
$$

---

# 154. Structured State 優於 prose-only

Prose：

> We think offset is probably X.

Structured：

```yaml
claim:
  status: hypothesis
  confidence: 0.62
  evidence_for: [...]
  evidence_against: [...]
```

---

# 155. Schema 防止狀態消失

固定欄位迫使 summary 保留：

- UNKNOWN；
- invalidated；
- scope。

---

# 156. Epistemic Schema

核心：

```text
Claim
Status
Scope
Confidence
Evidence+
Evidence-
Dependencies
Next Test
```

---

# 157. Running Case 的最小 ESS

十二小時研究後，真正 active handoff 可能只有：

```text
A2 no-op save: verified byte-identical
B1 fixed schedule: verified via reload
wrong church run: excluded
B2 replication: incomplete
next: complete B2
```

---

# 158. 這只有幾行

但每一行後面：

> 可能連到數百張 screenshots 與多個 saves。

---

# 159. Semantic Density

定義：

$$
D_S
=
\frac{
N_{\mathrm{decision-relevant\ constraints}}
}{
\operatorname{Bytes}(K)
}.
$$

---

# 160. Raw Evidence Density

$$
D_R
=
\frac{
N_{\mathrm{decision-relevant\ constraints}}
}{
\operatorname{Bytes}(R)
}.
$$

一般：

$$
D_S\gg D_R.
$$

---

# 161. 這就是 semantic recompression 的價值

不是把 bytes 變少本身，

而是提高：

$$
\boxed{
\text{Decision-Relevant Information Density}
}
$$

---

# 162. Research Throughput

若 context cost 下降，

Agent 可以在固定 budget 中做更多：

- hypothesis；
- experiment；
- validation。

---

# 163. 但壓縮過度會適得其反

若漏掉 constraint，

會重跑舊路。

所以：

$$
\text{Compression}
\rightarrow
\text{Future Search Cost}
$$

有 tradeoff。

---

# 164. Total Cost

$$
C_{\mathrm{total}}
=
C_{\mathrm{store}}
+
C_{\mathrm{compress}}
+
C_{\mathrm{retrieve}}
+
C_{\mathrm{rework}}.
$$

---

# 165. 最佳 memory policy

最小化：

$$
\boxed{
C_{\mathrm{total}}
}
$$

而不是只最小化 token。

---

# 166. Rework Cost

如果壓縮掉已 invalidated result，

Agent 重跑 3 小時，

那省的 token 根本不值得。

---

# 167. Compression ROI

$$
ROI_C
=
\frac{
C_{\mathrm{future\ saved}}
}{
C_{\mathrm{compression}}
+
C_{\mathrm{lost\ info}}
}.
$$

---

# 168. 可證偽預測一

Pointer-preserving hierarchical memory 應比 summary-only memory：

- 更低 contradiction loss；
- 更低 repeated-error rate。

---

# 169. 可證偽預測二

對 long-horizon research task：

$$
|A_t|
$$

有上限的 hierarchical memory agent，

應比 full-history stuffing 有更好的 cost/performance tradeoff。

---

# 170. 可證偽預測三

如果移除 raw evidence dereference，

complex edge-case correctness 應下降。

---

# 171. 可證偽預測四

如果移除 negative memory，

重複已 invalidated hypothesis 的比例應上升。

---

# 172. 可證偽預測五

如果 summary 不保存 status field，

Excluded / Invalidated 混淆率應上升。

---

# 173. 可證偽預測六

dependency-aware retrieval 應在 multi-step research task 上優於純 semantic similarity retrieval。

---

# 174. 可證偽預測七

以 structured epistemic state 取代 prose summary，

長 session 的 state consistency 應提高。

---

# 175. 可證偽預測八

Validated canonical state + delta handoff，

應比每輪重新摘要全歷史具有更低 summary drift。

---

# 176. 限制一：Sufficiency 不可精確證明

對開放研究：

$$
\mathcal D
$$

未來會變。

所以 ESS 多半是：

> empirical / task-relative。

---

# 177. 限制二：Raw Evidence 也可能錯

保存 raw 不代表 raw 正確。

它只是保留：

> 當時真正觀察到什麼。

---

# 178. 限制三：Provenance Graph 本身也有成本

如果每個 token 都建立 node，

系統會爆。

所以 provenance granularity 也要分層。

---

# 179. 限制四：Privacy / Security

Raw evidence 可能包含：

- private data；
- credentials；
- licensed assets。

需要 access control。

---

# 180. 限制五：Storage 不是免費

尤其：

- video；
- memory dumps；
- full traces。

需要 GC。

---

# 181. 限制六：Reproducibility 可能消失

舊 tool / environment 未保存，

未來 raw pointer 也可能無法重跑。

所以需保存 environment manifest。

---

# 182. Reproducibility Capsule

```text
tool versions
OS
seed
command
input hashes
output hashes
```

---

# 183. 限制七：模型不一定會主動 dereference

Memory 有 pointer 不代表 Agent 會用。

所以 retrieval policy 也需訓練／評估。

---

# 184. Retrieval Recall

$$
RR
=
P(
\text{retrieve necessary evidence}
\mid
\text{decision requires it}
).
$$

---

# 185. Retrieval Precision

$$
RP
=
P(
\text{retrieved evidence useful}
).
$$

---

# 186. Memory system evaluation

至少測：

- retrieval recall；
- contradiction recall；
- frontier preservation；
- decision distortion；
- token cost。

---

# 187. 不是只測 QA accuracy

因為 research memory 是 execution substrate。

---

# 188. Memory as Execution State

這也是 MAGE 類工作提出的重要方向。

---

# 189. 研究 Agent Memory 的真正單位

不是：

$$
\text{message}.
$$

而是：

$$
\boxed{
\text{Epistemic Transition}
}
$$

---

# 190. Epistemic Transition

```text
HYPOTHESIS
→ EXPERIMENT
→ EVIDENCE
→ VERDICT
→ STATE CHANGE
```

---

# 191. 這是應被壓縮的最小邏輯單位

而不是：

> 3000 tokens conversation chunk。

---

# 192. Transition Record

```yaml
transition:
  hypothesis:
  action:
  observation:
  verdict:
  state_delta:
  evidence_pointer:
```

---

# 193. Semantic Compression 可直接壓 transition

多個 transition：

$$
T_1,\ldots,T_n
$$

若共同支持一個 stable claim，

可合併：

$$
T_{1:n}\rightarrow c.
$$

---

# 194. 但 counterexample transition 永遠保留 pointer

---

# 195. Canonical State = Research Build Artifact

因此：

$$
\boxed{
K_t
=
\text{compiled research state}
}
$$

---

# 196. Raw Evidence = Source

$$
R_t
=
\text{research source tree}.
$$

---

# 197. Active Context = Runtime Working Set

$$
A_t
=
\text{loaded research state}.
$$

---

# 198. 這形成一個完整計算類比

```text
Raw Evidence       = Source
Canonical State    = Compiled Artifact
Index/Provenance   = Symbol Table / Debug Info
Active Context     = Working Set
Retrieval          = Page Load
New Evidence       = Source Change
Revalidation       = Incremental Rebuild
```

---

# 199. 這也解釋「記憶編譯」

長時 Agent memory 不是單純 append。

它必須：

$$
\boxed{
\text{Compile Evidence into State}
}
$$

---

# 200. 而且 compiled state 可失效

如果 source evidence 改變，

要重新 build。

---

# 201. Semantic Recompression Operator

定義：

$$
\mathcal C:
(R_t,K_{t-1})
\rightarrow
(K_t,I_t).
$$

---

# 202. Incremental Version

$$
\mathcal C_\Delta:
(\Delta R_t,K_{t-1})
\rightarrow
\Delta K_t.
$$

更適合長時 Agent。

---

# 203. Compression Invariant 1

Verified claim 必須：

> 至少一個 admissible evidence path。

---

# 204. Compression Invariant 2

Invalidated claim 必須：

> contradiction pointer。

---

# 205. Compression Invariant 3

Unknown 不得靜默升級成 verified。

---

# 206. Compression Invariant 4

Excluded run 不得作為核心支持／反駁。

---

# 207. Compression Invariant 5

Scope 必須保留：

```text
version
build
environment
protocol
```

---

# 208. Compression Invariant 6

新 summary 不得把：

```text
prior
```

改成：

```text
local verification
```

---

# 209. Compression Invariant 7

Canonical claim dependency 必須可重建。

---

# 210. Compression Invariant 8

所有 high-impact claim 必須可 dereference。

---

# 211. ESS Verification

可以建立 unit tests：

```text
Can we recover why H was invalidated?
Can we reproduce B1?
Can we identify next frontier?
Can we distinguish DOS vs Refine scope?
```

---

# 212. Memory Regression Test

每次 compression 後跑：

$$
T_M.
$$

---

# 213. 這使 memory 本身成為可測軟體

---

# 214. 長時研究的真正「上下文壓縮」

不再是：

> 幫我把前面摘要一下。

而是：

```text
compile current epistemic state
validate invariants
archive evidence
emit active capsule
```

---

# 215. 這與一般聊天摘要完全不同

聊天摘要追求：

> 人類可讀。

研究 compression 追求：

> 下個 Agent 不會重複犯錯，而且知道去哪找證據。

---

# 216. Handoff Quality

定義：

$$
Q_H
=
f(
Continuity,
Correctness,
Frontier,
Provenance,
Compactness
).
$$

---

# 217. Compactness 只是其中一項

---

# 218. PM2 案例真正教我們的

不是：

> AI 可以產生很多檔案。

而是：

> 長時 AI 研究第一次讓「認知中間態」大量物質化，因此我們必須像管理資料庫與編譯系統一樣管理研究記憶。

---

# 219. 這可能成為 Agent OS 的核心服務

未來 Agent Runtime 需要：

```text
Evidence Store
Epistemic Compiler
Provenance Graph
Memory GC
Context Loader
Contradiction Ledger
Frontier Manager
```

---

# 220. Agent Memory OS

抽象：

$$
\boxed{
\mathcal M
=
(R,K,I,GC,Ret,V_C)
}
$$

其中：

- $R$：raw evidence；
- $K$：canonical state；
- $I$：index/provenance；
- $GC$：evidence garbage collection；
- $Ret$：retrieval；
- $V_C$：compression verifier。

---

# 221. Memory OS 不是模型本身

可以被不同：

- GPT；
- Claude；
- local model；
- specialized model；

共同使用。

---

# 222. 這讓研究成果跨模型持續存在

如果：

$$
M_1\rightarrow M_2,
$$

只要：

$$
K,I,R
$$

保持，

研究不必重頭開始。

---

# 223. 模型替換與研究連續性

$$
\boxed{
\text{Research Identity}
\neq
\text{Single Model Instance}
}
$$

---

# 224. 這是長時自主研究的必要條件之一

因為：

- model upgrade；
- quota reset；
- context reset；
- agent crash；

都會發生。

---

# 225. Externalized Epistemic State

因此真正長期穩定的：

$$
K_t
$$

應外部化。

---

# 226. 可證偽預測九

相同 memory substrate 下更換模型，

應能比「只有 model context」更快恢復 research frontier。

---

# 227. 可證偽預測十

如果 memory substrate 有完整 contradiction ledger，

跨模型 handoff 後 repeated invalidated hypothesis 應顯著下降。

---

# 228. 與 Paper 06 的接口

Paper 05 處理：

> **如何壓縮研究結果。**

Paper 06 將處理：

> **如何壓縮研究路徑本身。**

即：

$$
\Pi
=
(a_1,a_2,\ldots,a_n)
$$

如何學成：

$$
\Pi^*
$$

使下一個相似問題不必再花十二小時。

---

# 229. 與 Paper 07 的接口

如果某些 experiment protocol 已穩定，

應從 Agent 的「認知勞動」下放給 deterministic automation。

---

# 230. 與 Paper 08 的接口

Benchmark 不只測 final answer，

也應測：

> memory compression 後是否仍能保持 target-local evidence chain。

---

# 231. 核心命題一

## Proposition 1 — Evidence Growth Does Not Require Active-Context Growth

若 raw evidence 外部化並可索引，

則：

$$
|R_t|\rightarrow\infty
$$

不必推出：

$$
|A_t|\rightarrow\infty.
$$

---

# 232. 核心命題二

## Proposition 2 — Summary-Only Compression Can Destroy Falsification Capacity

存在 research history：

$$
R
$$

與 summary：

$$
s=C(R)
$$

使 summary 丟失唯一 counterexample：

$$
e^-.
$$

則後續 Agent 無法從 $s$ 恢復：

> hypothesis 已被否證。

因此：

$$
\boxed{
\text{Semantic Summary}
\not\Rightarrow
\text{Epistemic Sufficiency}
}
$$

---

# 233. 核心命題三

## Proposition 3 — Pointer-Preserving Compression Can Maintain Evidence Recoverability

若所有 canonical claim：

$$
c_i
$$

都有：

$$
I(c_i)
\rightarrow
R_i,
$$

則壓縮 active context 不必刪除原 evidence。

---

# 234. 核心命題四

## Proposition 4 — Contradiction Memory Is a First-Class Compression Invariant

若 invalidated claim 不被保存，

則長時 Agent 在 context reset 後可重新提出它。

因此 negative memory 必須被視為 canonical state。

---

# 235. 核心命題五

## Proposition 5 — Epistemic Sufficiency Is Task-Relative

同一：

$$
K
$$

對 subgoal：

$$
q_1
$$

可能 sufficient，

對：

$$
q_2
$$

不 sufficient。

因此不存在不依 task 的唯一最小摘要。

---

# 236. 核心命題六

## Proposition 6 — Evidence-Backed Semantic Recompression Can Increase Decision-Relevant Information Density

若：

$$
|K|\ll|R|
$$

且：

$$
\Delta_D\le\epsilon,
$$

則：

$$
D_S>D_R
$$

可成立。

---

# 237. 核心命題七

## Proposition 7 — Epistemic Compilation Enables Incremental Research Continuity

若 canonical state：

$$
K_t
$$

與 evidence delta：

$$
\Delta R_{t+1}
$$

可增量更新，

則下一 session 不需重新處理完整：

$$
R_{0:t}.
$$

---

# 238. 最終架構

```text
TARGET / SOURCE
      │
      ▼
RAW EVIDENCE STORE  ─────────────────────┐
      │                                  │
      │ provenance                       │ dereference
      ▼                                  │
EPISTEMIC COMPILER                       │
      │                                  │
      ▼                                  │
CANONICAL EPISTEMIC STATE                │
VERIFIED / INVALIDATED / UNKNOWN         │
      │                                  │
      ▼                                  │
PROVENANCE + DEPENDENCY INDEX ───────────┘
      │
      ▼
TASK-RELATIVE RETRIEVAL
      │
      ▼
ACTIVE CONTEXT
      │
      ▼
NEXT AGENT DECISION
```

---

# 239. 最終公式

研究資料生命週期：

$$
\boxed{
G
\rightarrow
R_t
\xrightarrow{\mathcal C}
(K_t,I_t)
\xrightarrow{Ret(q_t)}
A_t
}
$$

其中：

$$
|A_t|\ll|K_t|\ll|R_t|
$$

在大型研究中可以成立。

---

# 240. 結論

長時 AI 研究真正的記憶問題，不是「模型能不能塞進更多 token」。

如果 Agent 研究數小時、數天甚至數月，raw evidence 必然持續增長。試圖把所有歷史塞回 context 不可擴展；把歷史全部摘要成 prose 又容易丟掉 contradiction、scope、failed run 與 provenance。

因此需要第三條路：

$$
\boxed{
\text{Keep the evidence,
compile the knowledge,
retrieve only what is needed.}
}
$$

本文將它稱為：

$$
\boxed{
\textbf{Evidence-Backed Semantic Recompression}
}
$$

以及其核心產物：

$$
\boxed{
\textbf{Epistemic Sufficient State}
}
$$

它要求：

- raw evidence 可以很大；
- active context 必須很小；
- canonical claim 必須可追溯；
- invalidated hypothesis 必須被記住；
- excluded run 必須與 contradiction 分離；
- current frontier 必須被保留；
- 壓縮後仍能在需要時重新載入原證據。

因此，從十二小時、數百 MB evidence 收斂到幾 KB handoff，不應被理解為：

> 「把資料摘要掉。」

更準確的是：

> **把大量實驗時空間編譯成一個更高語義密度的研究狀態，同時用 provenance pointer 保存重新打開原世界的能力。**

這使 Agent 的長時研究第一次具有一種接近作業系統、資料庫、版本控制與科學筆記本交集的記憶架構。

---

# 241. 後續

**Paper 06：研究軌跡壓縮：從 Agent 的十二小時探索到局部資訊解構效率**

將研究：

$$
\boxed{
\text{Evidence Compression}
\neq
\text{Trajectory Compression}
}
$$

也就是：現在我們已經知道怎麼把十二小時的**結果**壓縮；下一步要問：

> **能不能讓下一個相似問題根本不用再跑十二小時？**

---

# References

[1] Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. **MemGPT: Towards LLMs as Operating Systems.** arXiv:2310.08560, 2023.  
https://arxiv.org/abs/2310.08560

[2] Jiang, H., Wu, Q., Lin, C.-Y., Yang, Y., & Qiu, L. **LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models.** arXiv:2310.05736, 2023.  
https://arxiv.org/abs/2310.05736

[3] Jiang, H., Wu, Q., Luo, X., Dongsheng Li, Lin, C.-Y., Yang, Y., & Qiu, L. **LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression.** arXiv:2310.06839, 2023.  
https://arxiv.org/abs/2310.06839

[4] Zhang, N., Yang, X., Tan, Z., Deng, W., & Wang, W. **HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents.** arXiv:2601.06377, 2026.  
https://arxiv.org/abs/2601.06377

[5] Wang, Z., Chen, H., Wang, J., & Wei, W. **Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory.** arXiv:2603.04257, 2026.  
https://arxiv.org/abs/2603.04257

[6] Chen, Y., et al. **Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents.** arXiv:2606.06090, 2026.  
https://arxiv.org/abs/2606.06090

[7] Hsu, H.-L., Kuang, N. L., Liu, B., Yao, Z., & He, Y. **Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents.** arXiv:2606.11680, 2026.  
https://arxiv.org/abs/2606.11680

[8] W3C Provenance Working Group. **PROV-O: The PROV Ontology.** W3C Recommendation, 2013.  
https://www.w3.org/TR/prov-o/

---

# Appendix A — Epistemic State Bundle

```yaml
epistemic_state_bundle:
  version:
  target:
    id:
    build:
    source_hashes: []

  canonical_claims:
    - id:
      scope:
      statement:
      status:
        - verified
        - partially_verified
        - invalidated
        - unknown
      confidence:
      evidence_for: []
      evidence_against: []
      dependencies: []
      stale_if: []

  excluded_runs:
    - id:
      reason:
      protocol:
      raw_evidence: []

  frontier:
    unresolved: []
    next_experiments: []

  provenance:
    entities: []
    activities: []
    agents: []
    derivations: []

  active_context_policy:
    max_tokens:
    always_hot: []
    retrieve_on_demand: []
```

---

# Appendix B — Compression Invariants

```text
I1  VERIFIED must have admissible evidence path.
I2  INVALIDATED must retain contradiction pointer.
I3  UNKNOWN cannot silently become VERIFIED.
I4  EXCLUDED cannot support or refute canonical claims.
I5  Version/build/protocol scope must survive compression.
I6  Historical prior cannot be relabeled as local verification.
I7  Dependency graph must survive.
I8  High-impact claims must be dereferenceable.
```

---

# Appendix C — 最小 Handoff Capsule

```yaml
handoff:
  goal:
  canonical_state_hash:

  latest_verified: []
  latest_invalidated: []
  current_unknowns: []
  excluded_runs: []

  frontier:
  next_best_experiment:

  evidence_store:
  provenance_index:
```

---

# Appendix D — 一句話命題

> **長時 Agent 的真正記憶能力，不在於永遠把所有歷史塞進上下文，而在於能把大量原始證據編譯成小型、可追溯、可反駁、可按需展開的認識狀態。**
