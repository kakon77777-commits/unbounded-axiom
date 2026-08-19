# LSI-PSD-12 — AI 證明空間觀測站：從 NS-203 到文明級研究記憶

## AI Proof-Space Observatory: From NS-203 to Civilization-Scale Research Memory

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 12  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 系列封頂工程論文 / Observatory Architecture and Research-Memory Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文把 LSI-PSD 前十一篇的方法論轉換成一個可實作的 AI 長程數學研究觀測站架構。本文中的 Proof-Space Observatory 是研究資訊基礎設施，不是數學真理機器。它可以保存、去重、驗證、追蹤、量測與路由 proof-related research artifacts，但不能由 corpus saturation 自動推出命題為假、不可證、獨立、不可判定或問題 framing 錯誤。本文提出的資料模型、指標、runtime、dashboard、API 與治理機制均屬可實驗工程提案；是否有效，必須透過可解 ground-truth benchmark、formal verifier、independent audit 與長期部署資料檢驗。

---

## 摘要

LSI-PSD 系列前十一篇建立了一套從長程 AI 數學研究資料中觀察 proof space 的方法論：

$$
\text{search regime}
\rightarrow
\text{coverage}
\rightarrow
\text{semantic quotient}
\rightarrow
\text{higher-order sampling}
\rightarrow
\text{local saturation}
\rightarrow
\text{obstruction confluence}
\rightarrow
\text{truth--generativity separation}
\rightarrow
\text{productive mis-specification}
\rightarrow
\text{productive window}
\rightarrow
\text{non-conclusion firewall}
\rightarrow
\text{historical lineage}.
$$

本文將這些概念收斂成一個真正可運行的系統：

$$
\boxed{
\textbf{AI Proof-Space Observatory}
}
$$

簡稱：

$$
\boxed{
\textbf{PSO}.
}
$$

PSO 的基本目標不是「自動證明所有定理」，而是讓長期、多人、多模型、多工具的數學研究第一次具有一個可被持續觀察、回放、稽核與重新路由的研究記憶層。系統不再把一輪 AI 輸出只視為一篇文字，而拆成：

$$
\text{Problem},
\text{Claim},
\text{Assumption},
\text{Lemma},
\text{Route},
\text{Proof State},
\text{Obstruction},
\text{Basin},
\text{Certificate},
\text{Revision},
\text{Descendant},
\text{Experiment}.
$$

所有物件以 canonical ID、版本、來源、依賴與 epistemic status 管理，並形成 typed multilayer graph。

本文提出 PSO 的核心資料圖：

$$
\mathcal G_{\mathrm{PSO}}
=
(
V,
E,
\tau_V,
\tau_E,
\sigma,
\pi,
\chi
),
$$

其中：

- $V$：研究節點集合；
- $E$：typed edges；
- $\tau_V$：節點型別；
- $\tau_E$：邊型別；
- $\sigma$：epistemic status；
- $\pi$：provenance；
- $\chi$：certificate / validation metadata。

系統以 event sourcing 保存每一次研究狀態改變：

$$
\mathcal S_{t+1}
=
\operatorname{Apply}(
\mathcal S_t,
e_t
),
$$

而不是只保存「最新版本」。因此所有：

- claim upgrade；
- claim downgrade；
- theorem repair；
- assumption deletion；
- parent revision；
- obstruction merge；
- basin split；
- descendant salvage；

都具有可逆歷史。

本文定義 PSO 的五層 runtime：

$$
\boxed{
\begin{aligned}
L_1 &: \text{Canonical Artifact Layer}\\
L_2 &: \text{Verification and Extraction Layer}\\
L_3 &: \text{Proof-Space Graph Layer}\\
L_4 &: \text{Measurement and Diagnosis Layer}\\
L_5 &: \text{Research Routing and Governance Layer}.
\end{aligned}
}
$$

在第 $L_1$ 層，系統保存原始 UTF-8 source、proof source、compiler output、logs、datasets、code、plots 與 checksum；第 $L_2$ 層負責 formal verification、statement extraction、dependency extraction、semantic equivalence candidate generation 與 human/model audit；第 $L_3$ 層形成 claim graph、proof-state graph、route graph、obstruction graph、basin graph 與 lineage graph；第 $L_4$ 層計算：

$$
I_k,
\quad
\rho_k,
\quad
S_K,
\quad
C_{\mathrm{ind}},
\quad
\Phi_E,
\quad
\mathcal W_P,
$$

以及 coverage、novelty、confluence、survival、zombie-knowledge rate、research cost 等指標；第 $L_5$ 層則使用這些量決定：

$$
\text{continue},
\text{branch},
\text{verify},
\text{repair},
\text{escape},
\text{reframe},
\text{pause},
\text{archive}.
$$

本文將 2026 年 formal theorem proving 基礎設施視為相鄰工程支撐，而不是直接等同於 PSO。LeanMarathon 把 evolving proof DAG 同時作為 formal skeleton、natural-language proof graph 與 shared system of record；TheoremGraph 建立跨 informal/formal mathematics 的 statement-level dependency graph；AXLE 提供可擴展、多版本、隔離式 Lean proof verification 與 extraction infrastructure；LeanSearch v2 顯示 global premise retrieval 可直接影響 end-to-end proof success；TheoremBench 以 theorem-level coverage 與 supporting subtheorems 衡量 partial proof progress；BlueprintRepair 則將 proof blueprint repair 限制為 schema-checked typed local edits，並禁止偷偷改動 target theorem。這些系統共同顯示，AI theorem proving 正從單一 tactic generation 走向：

$$
\boxed{
\text{structured proof state}
+
\text{graph memory}
+
\text{typed repair}
+
\text{scalable verification}.
}
$$

PSO 的差異在於，它把這種 formal proving infrastructure 再向外擴張成**研究過程觀測學**：未證明的路線、失敗、negative result、obstruction、reformulation、descendant survival 與 historical revision 同樣是第一等物件。

本文最後以 NS-203 corpus 作為第一個 migration target。既有 v0.1 observatory 已對 203 份 NS paper-like artifacts 建立 paper-level route graph，得到 sequence、dependency、similarity、confluence 與 higher-order sampling 的初步量測。本文提出第二階段 migration：

$$
203\ \text{papers}
\rightarrow
\text{claim/lemma/assumption/obstruction graph},
$$

再把每個 NS artifact 轉成：

$$
A_i
=
(
Q_i,
\mathcal A_i,
L_i,
C_i,
O_i,
R_i,
S_i
).
$$

第一版 PSO 不需要立即理解所有 NS 數學，而應先建立：

1. canonical source；
2. exact provenance；
3. theorem-level extraction；
4. assumption lineage；
5. obstruction ID；
6. status type；
7. cross-paper dependency；
8. human-audited gold set。

只有在這些基礎上，才有資格更精確地測量「二階、三階、X 階採樣」與局部 proof-space saturation。

本文最終提出：

$$
\boxed{
\textbf{The future unit of mathematical research memory should not be the paper, but the versioned, typed, provenance-preserving research relation.}
}
$$

以及：

$$
\boxed{
\textbf{A civilization-scale AI research system should remember not only what was proved, but what was tried, why it failed, what survived revision, and which unexplored regions remain.}
}
$$

**關鍵詞：** Proof-Space Observatory、AI 數學研究、研究記憶、proof graph、obstruction graph、claim graph、event sourcing、epistemic type、theorem proving、Lean、NS-203、文明級知識、AI co-mathematician、長程研究

---

# 1. 問題的提出：為什麼「論文資料夾」已經不夠

傳統研究記憶單位是：

$$
\text{paper}.
$$

一篇 paper 存：

- 題目；
- abstract；
- theorem；
- proof；
- references。

---

# 2. 長程 AI 研究破壞了 paper 作為唯一單位的假設

AI 可以在一天內產生：

$$
10^2
$$

甚至更多 research artifacts。

---

# 3. Artifact 可能不是 paper

它可能只是：

- one proof attempt；
- one lemma；
- one failed route；
- one audit；
- one counterexample search；
- one simulation；
- one repair。

---

# 4. 如果全部壓成 paper

會失去：

$$
\boxed{
\text{process structure}.
}
$$

---

# 5. 如果只存聊天記錄

又會失去：

- canonical source；
- stable ID；
- dependency；
- status；
- verification。

---

# 6. 所以需要新的 research memory primitive

本文提出：

$$
\boxed{
\text{Versioned Research Object}
}
$$

簡稱：

$$
VRO.
$$

---

# 7. VRO 的最小條件

每個物件必須有：

```text
ID
TYPE
SOURCE
VERSION
STATUS
PROVENANCE
DEPENDENCIES
VALIDATION
TIMESTAMP
```

---

# 8. Paper 只是 VRO 的一種

其他：

- claim；
- lemma；
- obstruction；
- experiment；
- certificate；
- route。

---

# 9. PSO 的第一原則

$$
\boxed{
\textbf{Do not reduce research history to final prose.}
}
$$

---

# 10. 第二原則

$$
\boxed{
\textbf{Do not reduce mathematical status to natural-language confidence.}
}
$$

---

# 11. 第三原則

$$
\boxed{
\textbf{Do not discard failures before canonicalizing them.}
}
$$

---

# 12. 第四原則

$$
\boxed{
\textbf{Do not overwrite parent knowledge when revising it.}
}
$$

---

# 13. 第五原則

$$
\boxed{
\textbf{Every strong claim must trace to a certificate or declared evidence type.}
}
$$

---

# 14. PSO 五層 runtime

$$
L_1
\rightarrow
L_2
\rightarrow
L_3
\rightarrow
L_4
\rightarrow
L_5.
$$

---

# 15. $L_1$：Canonical Artifact Layer

保存：

- `.md`；
- `.lean`；
- `.py`；
- `.json`；
- `.csv`；
- images；
- logs；
- ZIP；
- checksum。

---

# 16. Canonical source

所有正式文本：

$$
\boxed{
\text{UTF-8 source artifact}
}
$$

優先於：

$$
\text{rendered conversation}.
$$

---

# 17. Source immutability

版本：

$$
v_1
$$

一旦 commit，

不 silent rewrite。

---

# 18. 修改產生：

$$
v_2.
$$

---

# 19. Hash

每版：

$$
h_v
=
\operatorname{SHA256}(source_v).
$$

---

# 20. $L_2$：Verification and Extraction Layer

輸入：

$$
\text{raw artifact}.
$$

輸出：

$$
\text{structured research objects}.
$$

---

# 21. Formal verification

對 Lean：

$$
\operatorname{Check}(\Pi,Q)=1.
$$

---

# 22. 但 formal verification 不等於 semantic fidelity

所以另存：

$$
F_S.
$$

---

# 23. Extraction

抽：

- theorem statement；
- assumptions；
- definitions；
- dependencies；
- proof terms；
- compiler feedback。

---

# 24. Informal artifact extraction

對 Markdown paper 抽：

$$
\text{Claim},
\text{Assumption},
\text{Lemma},
\text{Obstruction},
\text{Status}.
$$

---

# 25. Extraction 不是 authority

自動抽取只產生：

$$
\text{candidate structured record}.
$$

---

# 26. 高風險 record 需要 audit

例如：

- obstruction equivalence；
- theorem equivalence；
- parent revision；
- framing defect。

---

# 27. $L_3$：Proof-Space Graph Layer

建立多層圖。

---

# 28. Claim Graph

$$
G_C.
$$

邊：

- implies；
- contradicts；
- refines；
- equivalent；
- depends-on。

---

# 29. Assumption Graph

$$
G_A.
$$

追蹤：

$$
\text{which claims depend on which assumptions}.
$$

---

# 30. Lemma Graph

$$
G_L.
$$

對 formal theorem：

$$
L_i\rightarrow L_j.
$$

---

# 31. Proof-State Graph

$$
G_S.
$$

節點：

$$
s_t.
$$

邊：

$$
s_t\xrightarrow{a_t}s_{t+1}.
$$

---

# 32. Route Graph

$$
G_R.
$$

節點可代表：

$$
r_i.
$$

---

# 33. Obstruction Graph

$$
G_O.
$$

節點：

$$
O_i.
$$

邊：

- refines；
- revives；
- resolves；
- inherits；
- co-converges。

---

# 34. Basin Graph

$$
G_B.
$$

描述：

$$
\text{local research regions}.
$$

---

# 35. Lineage Graph

$$
G_H.
$$

追蹤：

$$
P^{(0)}
\rightarrow
P^{(1)}
\rightarrow
P^{(2)}.
$$

---

# 36. Certificate Graph

$$
G_\chi.
$$

把：

- proof；
- counterexample；
- independence；
- no-go；
- faithfulness audit；

連到 claim。

---

# 37. Multilayer graph

整體：

$$
\boxed{
\mathcal G_{\mathrm{PSO}}
=
G_C
\cup
G_A
\cup
G_L
\cup
G_S
\cup
G_R
\cup
G_O
\cup
G_B
\cup
G_H
\cup
G_\chi.
}
$$

---

# 38. 不能只用單一 graph schema

因為：

$$
\text{proof-state edge}
$$

和：

$$
\text{historical-revision edge}
$$

不是同型。

---

# 39. Typed edges 是必要條件

$$
\tau_E(e).
$$

---

# 40. $L_4$：Measurement and Diagnosis Layer

這裡才計算 LSI-PSD 指標。

---

# 41. Coverage

$$
I_k(N).
$$

---

# 42. Audited novelty yield

$$
\rho_k(N,W).
$$

---

# 43. Local saturation

$$
S_K(B).
$$

---

# 44. Confluence

$$
C_{\mathrm{ind}}(O).
$$

---

# 45. Epistemic fertility

$$
\Phi_E(P).
$$

---

# 46. Productive window

$$
\mathcal W_P.
$$

---

# 47. Zombie knowledge

$$
Z_K.
$$

---

# 48. Descendant survival

$$
S_D.
$$

---

# 49. Research cost

$$
C_R.
$$

---

# 50. $L_5$：Routing and Governance Layer

量測後不直接判真理。

只決定下一個 research action。

---

# 51. Actions

$$
a
\in
\{
\text{continue},
\text{branch},
\text{verify},
\text{repair},
\text{escape},
\text{reframe},
\text{pause},
\text{archive}
\}.
$$

---

# 52. Meta-policy

$$
\Pi_{\mathrm{meta}}
:
\mathcal S_t
\rightarrow
a_t.
$$

---

# 53. Routing 不等於自治判決

任何：

$$
\text{Verdict upgrade}
$$

需 certificate。

---

# 54. PSO 物件一：Problem

```yaml
problem_id:
canonical_statement:
informal_statement:
formal_statement:
domain:
formal_system:
status:
```

---

# 55. Problem 不是永恆不變

版本：

$$
Q^{(v)}.
$$

---

# 56. PSO 物件二：Claim

```yaml
claim_id:
text:
formalization:
scope:
status:
evidence:
```

---

# 57. PSO 物件三：Assumption

```yaml
assumption_id:
statement:
scope:
origin:
status:
```

---

# 58. PSO 物件四：Lemma

```yaml
lemma_id:
statement:
proof:
dependencies:
verification:
```

---

# 59. PSO 物件五：Proof State

```yaml
state_id:
goals:
hypotheses:
environment:
parent_state:
action:
```

---

# 60. PSO 物件六：Route

```yaml
route_id:
problem:
method_family:
representation:
premise_set:
states:
endpoint:
```

---

# 61. PSO 物件七：Obstruction

```yaml
obstruction_id:
normalized_gap:
assumptions:
route_support:
audit:
status:
```

---

# 62. PSO 物件八：Basin

```yaml
basin_id:
members:
conductance:
recurrence:
yield:
saturation:
```

---

# 63. PSO 物件九：Certificate

```yaml
certificate_id:
type:
target_claim:
formal_system:
source:
verifier:
status:
```

---

# 64. Certificate types

$$
\{
\text{proof},
\text{counterexample},
\text{no-go},
\text{independence},
\text{undecidability},
\text{faithfulness}
\}.
$$

---

# 65. PSO 物件十：Revision

```yaml
revision_id:
parent_version:
new_version:
changed_components:
reason:
affected_descendants:
```

---

# 66. PSO 物件十一：Descendant

不需要獨立新本體。

它是任何 VRO 對 parent 的 lineage relation：

$$
d\rightarrow P.
$$

---

# 67. PSO 物件十二：Experiment

```yaml
experiment_id:
hypothesis:
branches:
controls:
budget:
metrics:
result:
```

---

# 68. Canonical ID

所有 ID 應：

$$
\text{stable across display changes}.
$$

---

# 69. 不用 title 當 ID

title 可改。

---

# 70. 建議 ID

```text
PSO-Q-000001
PSO-C-000123
PSO-O-000044
PSO-R-000081
```

---

# 71. Content hash 另存

stable ID：

$$
\neq
$$

content hash。

---

# 72. 為什麼要分

內容更新：

$$
h_v\neq h_{v+1}
$$

但：

$$
\operatorname{ObjectID}
$$

仍相同。

---

# 73. Event sourcing

系統不直接修改 current state。

---

# 74. 每個變化寫 event

$$
e_t.
$$

---

# 75. State reconstruction

$$
\mathcal S_t
=
\operatorname{Fold}(e_0,\ldots,e_t).
$$

---

# 76. Event types

```text
CREATE
VERIFY
REFUTE
MERGE
SPLIT
REVISE
LINK
UNLINK
UPGRADE_STATUS
DOWNGRADE_STATUS
ARCHIVE
```

---

# 77. Event sourcing 的好處一：可回放

知道：

> 這個 claim 為什麼從 hypothesis 變 supported。

---

# 78. 好處二：防 status laundering

upgrade 有 event。

---

# 79. 好處三：parent revision 可追

---

# 80. 好處四：可建立時間序列研究學

---

# 81. Epistemic type system

沿用第 10 篇。

---

# 82. Status types

```text
OBSERVATION
HYPOTHESIS
SUPPORTED_HYPOTHESIS
EMPIRICAL_NO_GO
FORMAL_NO_GO
PROVEN
REFUTED
INDEPENDENT_RELATIVE_TO_T
UNDECIDABLE_CLASS
ARCHIVED
```

---

# 83. Illegal cast

$$
\text{HYPOTHESIS}
\not\rightarrow
\text{PROVEN}
$$

without certificate。

---

# 84. Status transition table

每種 transition 都有：

$$
\text{required certificate type}.
$$

---

# 85. Provenance

每個 VRO 存：

- agent；
- model；
- human；
- source file；
- parent prompt；
- tool；
- timestamp。

---

# 86. Model identity 不等於 epistemic authority

模型欄只用來研究 genealogy。

---

# 87. Agent genealogy

兩條 route：

$$
r_1,r_2
$$

如果共享：

- same memory；
- same prompt；
- same parent；

independence 降低。

---

# 88. Research genealogy graph

$$
G_G.
$$

---

# 89. 這直接支援：

$$
C_{\mathrm{ind}}.
$$

---

# 90. Canonical math source

公式一律保存：

$$
\text{LaTeX source}.
$$

---

# 91. 不把 rendered glyph 當 source

避免：

$$
\text{Unicode round trip}.
$$

---

# 92. Render layer

可以：

- KaTeX；
- MathJax；
- Lean pretty printer。

但 render：

$$
\neq
$$

canonical。

---

# 93. Statement normalization

自動 normalization 只能產生 candidate。

---

# 94. 不能 silent rewrite theorem

---

# 95. BlueprintRepair 的重要工程啟發

typed local edit：

$$
\Delta_i
$$

明示 target node。

---

# 96. Target theorem 不可偷改

這應成為 PSO repair rule。

---

# 97. Repair operation schema

```yaml
operation:
target_node:
precondition:
edit:
postcondition:
verification:
```

---

# 98. Free-form rewrite 是高風險操作

需要更強 audit。

---

# 99. LeanMarathon 的 shared system of record

evolving proof DAG：

$$
G_{\mathrm{proof}}.
$$

---

# 100. PSO 的擴張

proof DAG 之外再加：

$$
\text{failure / history / status / basin / experiment}.
$$

---

# 101. TheoremGraph 的啟發

statement-level graph 可跨：

$$
\text{informal}
\leftrightarrow
\text{formal}.
$$

---

# 102. 這非常適合 PSO 的兩層 claim

$$
C_I
$$

informal claim，

$$
C_F
$$

formal claim。

---

# 103. Faithfulness edge

$$
C_I
\xleftrightarrow[\text{audit}]{}
C_F.
$$

---

# 104. Faithfulness confidence

$$
F_S(C_I,C_F).
$$

---

# 105. AXLE 的啟發

verification utilities 應成獨立 service。

---

# 106. PSO 不應把 verifier 邏輯塞進 LLM prompt

---

# 107. Verification service

輸入：

$$
(\text{source},\text{version},\text{environment}).
$$

---

# 108. 輸出：

- success；
- diagnostics；
- dependencies；
- metadata。

---

# 109. 多 Lean / Mathlib 版本

環境本身必須版本化。

---

# 110. 因為：

$$
\Pi@v_1
$$

不一定：

$$
\Pi@v_2.
$$

---

# 111. LeanSearch v2 的啟發

premise retrieval 應分：

$$
\text{local}
$$

與：

$$
\text{global}.
$$

---

# 112. PSO premise object

每個 route 存：

$$
P_r.
$$

---

# 113. Retrieval trace

存：

```text
query
retrieved candidates
rank
selected
used
```

---

# 114. 這能分析 premise basin lock-in

---

# 115. TheoremBench 的啟發

只問 final theorem solved：

$$
0/1
$$

不夠。

---

# 116. PSO 必須測 partial theorem coverage

$$
C_T.
$$

---

# 117. Supporting-subtheorem coverage

$$
C_{\mathrm{sub}}.
$$

---

# 118. Token efficiency

$$
E_{\mathrm{token}}
=
\frac{
\text{audited progress}
}{
\text{tokens}
}.
$$

---

# 119. Verification-call efficiency

$$
E_V
=
\frac{
\text{audited progress}
}{
\text{verifier calls}
}.
$$

---

# 120. Cost-normalized novelty

$$
\nu_C
=
\frac{
\Delta U
}{
C_R
}.
$$

---

# 121. PSO 核心指標群

$$
\boxed{
\mathbf M_{\mathrm{PSO}}
=
(
I_k,
\rho_k,
S_K,
C_{\mathrm{ind}},
\Phi_E,
S_D,
Z_K,
C_T,
E_{\mathrm{token}},
E_V
).
}
$$

---

# 122. 不做 single leaderboard score

因為會失真。

---

# 123. Dashboard 第一頁：Problem Overview

顯示：

- canonical statement；
- status；
- formalizations；
- versions；
- certificate。

---

# 124. 第二頁：Research Map

顯示：

$$
G_R,
G_O,
G_B.
$$

---

# 125. 第三頁：Saturation

顯示：

$$
\rho_k(t),
S_K(B).
$$

---

# 126. 第四頁：Obstruction Atlas

顯示：

$$
C_{\mathrm{ind}}(O),
Z(O),
R_O.
$$

---

# 127. 第五頁：Lineage

顯示：

$$
P^{(0)}\rightarrow P^{(1)}.
$$

---

# 128. 第六頁：Descendant Survival

顯示：

- strong；
- repairable；
- transferred；
- refuted；
- unknown。

---

# 129. 第七頁：Experiment Lab

控制：

- representation；
- method；
- model；
- budget；
- branch。

---

# 130. 第八頁：Epistemic Status

每個 claim：

$$
\text{type checked}.
$$

---

# 131. Dashboard 禁止紅色等於「假」

顏色只表示 status。

---

# 132. 例如

紅：

$$
\text{active obstruction}.
$$

不是：

$$
\text{false theorem}.
$$

---

# 133. Search

PSO search 不只全文搜尋。

---

# 134. Query examples

> 找所有依賴 assumption A-17 的 claims。

---

# 135. Query

> 找所有跨三個 method family 命中 O-31 的 routes。

---

# 136. Query

> 找所有 parent revision 後仍存活的 lemmas。

---

# 137. Query

> 找所有 Level-3 saturation basin。

---

# 138. Query

> 找所有 status=SUPPORTED_HYPOTHESIS 但沒有最近 audit 的 claims。

---

# 139. Research query language

未來可建立：

$$
\text{PSO-QL}.
$$

---

# 140. 示例

```text
MATCH Route -> Obstruction
WHERE obstruction.confluence_ind > 3
AND route.method_family_count >= 2
RETURN route, obstruction
```

---

# 141. Storage architecture

本文不要求單一資料庫。

---

# 142. 建議分層

1. object store；
2. relational metadata；
3. graph index；
4. vector / semantic index；
5. event log。

---

# 143. Object store

保存：

$$
\text{canonical files}.
$$

---

# 144. Relational DB

保存：

- IDs；
- versions；
- statuses；
- metrics。

---

# 145. Graph DB

保存：

$$
E.
$$

---

# 146. Vector index

只用於：

$$
\text{candidate retrieval}.
$$

---

# 147. Vector similarity 不能作 semantic truth

---

# 148. Event log

append-only。

---

# 149. 資料庫應可重建

如果 graph DB 壞，

從：

$$
\text{canonical artifacts + events}
$$

重建。

---

# 150. Canonical state 不應只存在 vector DB

---

# 151. Artifact pipeline

$$
\text{Ingest}
\rightarrow
\text{Hash}
\rightarrow
\text{Parse}
\rightarrow
\text{Extract}
\rightarrow
\text{Validate}
\rightarrow
\text{Link}
\rightarrow
\text{Measure}.
$$

---

# 152. Ingest

來源：

- AI；
- human；
- Git；
- paper；
- proof assistant；
- experiment。

---

# 153. Hash

建立：

$$
h.
$$

---

# 154. Parse

不要在 parse 階段改 source。

---

# 155. Extract

產生 candidates。

---

# 156. Validate

依 type 使用：

- Lean；
- Python；
- manual；
- cross-model。

---

# 157. Link

建立 edges。

---

# 158. Measure

最後才算 metrics。

---

# 159. Semantic quotient pipeline

$$
x_i,x_j
\rightarrow
\text{candidate similarity}
\rightarrow
\text{structural compare}
\rightarrow
\text{audit}
\rightarrow
\text{merge / no merge}.
$$

---

# 160. False merge 風險大於 false split

因為 false merge 會偽造 saturation。

---

# 161. 所以 merge threshold 應保守

---

# 162. Obstruction pipeline

$$
\text{failure event}
\rightarrow
\text{gap extraction}
\rightarrow
\text{assumption normalization}
\rightarrow
O_{\mathrm{candidate}}
\rightarrow
\text{audit}.
$$

---

# 163. Basin pipeline

先 graph candidate。

---

# 164. 再 human / theorem-level audit。

---

# 165. Basin 版本化

$$
B^{(v)}.
$$

---

# 166. 因為新 edge 可能：

- merge；
- split；
- dissolve。

---

# 167. Saturation detector

輸入：

$$
B^{(v)}.
$$

---

# 168. 不能對舊 basin ID 永久保證 status

---

# 169. Measurement version

每個 metric：

$$
M@v.
$$

---

# 170. 這可防止 metric drift

---

# 171. Novelty detector audit

至少：

- fixed-window；
- permutation baseline；
- corpus-size correction；
- semantic quotient；
- manual sample。

---

# 172. Confluence detector audit

至少：

- genealogy correction；
- assumption normalization；
- route independence；
- representation distance。

---

# 173. Productive-mis-specification detector audit

至少：

- parent revision；
- descendant re-audit；
- random control；
- ground truth。

---

# 174. Non-conclusion firewall

每個 dashboard verdict card 先檢查：

$$
\text{certificate}.
$$

---

# 175. 沒 certificate

最大輸出：

$$
\text{SUPPORTED_HYPOTHESIS}.
$$

---

# 176. Research Router

核心元件：

$$
\boxed{
\text{PSO Router}
}
$$

---

# 177. Router 不生成 proof

它分配研究。

---

# 178. Router input

$$
\mathbf x_t
=
(
S_K,
C_{\mathrm{ind}},
\rho_k,
\Gamma_{\mathrm{esc}},
C_R,
\mathfrak F
).
$$

---

# 179. Router output

$$
a_t.
$$

---

# 180. Sample policy

如果：

$$
\rho_k\gg0,
$$

continue。

---

# 181. 如果：

$$
S_K(B)\gg0,
$$

escape。

---

# 182. 如果：

$$
C_{\mathrm{ind}}(O)\gg0,
$$

focus obstruction。

---

# 183. 如果：

$$
Z_K\gg0,
$$

pause generation，

先 re-audit。

---

# 184. 如果 formalization fidelity 低

pause proving。

先修 statement。

---

# 185. 如果 cross-regime saturation 高

進 meta-level investigation。

---

# 186. 不直接 verdict

---

# 187. Human role

人類不是每步 proof 都要看。

---

# 188. Human priority

集中：

- high-centrality obstruction；
- status upgrade；
- framing change；
- ambiguous equivalence；
- public release。

---

# 189. AI role

適合：

- extraction；
- candidate relation；
- branch generation；
- proof repair；
- audit suggestions；
- literature mapping。

---

# 190. Formal verifier role

只判：

$$
\text{formal validity}.
$$

---

# 191. No single observer is enough

PSO 本身是一個：

$$
\boxed{
\text{multi-observer research system}.
}
$$

---

# 192. Observer separation

至少：

- generator；
- verifier；
- auditor；
- router。

---

# 193. Generator 不應自評為 final authority

---

# 194. Verifier 不懂全部 semantic intent

---

# 195. Auditor 檢查 intent / relation

---

# 196. Router 決定下一步

---

# 197. 多 AI 架構

可設：

$$
A_G,A_V,A_A,A_R.
$$

---

# 198. Cross-model audit

關鍵 claim 給不同 model。

---

# 199. 但不同 model 不代表完全獨立

genealogy 仍要記。

---

# 200. Memory 分層

## Hot

當前 problem / branch。

---

# 201. Warm

活躍 basin / obstruction。

---

# 202. Cold

完整歷史 artifact。

---

# 203. Frozen

formal certificates / release packages。

---

# 204. Hot memory 可壓縮

但：

$$
\text{canonical source}
$$

不可丟。

---

# 205. Compression pointer

摘要只存：

$$
\text{references to source IDs}.
$$

---

# 206. 不做 lossy replacement

---

# 207. Garbage collection

不能用：

> 最近沒用。

作唯一刪除條件。

---

# 208. Archive > delete

research history 預設 archive。

---

# 209. Delete 只針對：

- duplicate raw cache；
- invalid temporary artifact；
- explicit policy。

---

# 210. Negative knowledge 保存

尤其：

$$
\text{failed route}.
$$

---

# 211. 但失敗 log 需要壓縮成 canonical obstruction

否則 storage 爆炸。

---

# 212. Failure compaction

$$
10^4\ \text{events}
\rightarrow
50\ \text{obstruction classes}
+
\text{provenance links}.
$$

---

# 213. 這就是 semantic compression

---

# 214. Civilization-scale research memory

如果研究 corpus：

$$
N\rightarrow10^9
$$

artifact，

全文 pairwise compare 不可行。

---

# 215. Candidate generation

先用 cheap features：

- terms；
- symbols；
- dependencies；
- embedding；
- explicit links。

---

# 216. 再深度 audit。

---

# 217. Complexity

避免：

$$
O(N^2)
$$

全比較。

---

# 218. Incremental graph update

新節點：

$$
v_{n+1}
$$

只找候選 neighborhood。

---

# 219. Dynamic communities

局部更新 basin。

---

# 220. Distributed observatory

不同 research domain 可有 local PSO。

---

# 221. Federation

$$
\text{PSO}_1
\leftrightarrow
\text{PSO}_2.
$$

---

# 222. Shared schema

只交換：

- typed claims；
- certificates；
- public provenance；
- hashes。

---

# 223. 私有研究可以只交換摘要／fingerprint

---

# 224. Cross-domain transfer

例如 NS obstruction：

$$
O_{\mathrm{NS}}
$$

與：

$$
O_{\mathrm{SQG}}
$$

候選相似。

---

# 225. Transfer edge

$$
O_{\mathrm{NS}}
\xleftrightarrow{}
O_{\mathrm{SQG}}.
$$

---

# 226. 但需要 theorem-level audit

---

# 227. Knowledge bridge

成功 transfer 形成：

$$
B_{\mathrm{transfer}}.
$$

---

# 228. Proof Asset Map

PSO 可自然實作：

$$
\text{Proof Asset Map}.
$$

---

# 229. Asset types

- lemma；
- method；
- obstruction；
- counterexample；
- transformation；
- tool。

---

# 230. Tool 也可成 proof asset

---

# 231. Example

一個 normalization script，

如果能降低 formalization error，

具有：

$$
U_{\mathrm{tool}}>0.
$$

---

# 232. Benchmark suite

PSO 不能只在 NS 未解題上測。

---

# 233. Ground-truth tier

第一層：

$$
\text{known solvable}.
$$

---

# 234. Known-false tier

有 counterexample。

---

# 235. Independence tier

已知 relative independence。

---

# 236. Formalization-defect tier

人工注入 mismatch。

---

# 237. Method-no-go tier

已知 barrier。

---

# 238. Long-horizon tier

dependency-rich theorem。

---

# 239. PMW tier

controlled deviation。

---

# 240. NS tier

open-ended observational。

---

# 241. Benchmark 順序

先：

$$
\text{known truth}.
$$

後：

$$
\text{unknown frontier}.
$$

---

# 242. 否則無法校準 observatory

---

# 243. Core benchmark metrics

- overclaim rate；
- underclaim rate；
- merge precision；
- obstruction precision；
- basin stability；
- routing efficiency；
- descendant survival accuracy。

---

# 244. Overclaim rate

沿用：

$$
O_R.
$$

---

# 245. False-saturation rate

$$
F_S
=
\frac{
N_{\mathrm{false\ saturation}}
}{
N_{\mathrm{tests}}
}.
$$

---

# 246. False-confluence rate

$$
F_C.
$$

---

# 247. Salvage precision

parent revision 後：

$$
P_{\mathrm{salv}}.
$$

---

# 248. Routing regret

相對 oracle policy：

$$
\mathcal R_g.
$$

---

# 249. Cost efficiency

$$
E_C
=
\frac{
\text{surviving knowledge}
}{
\text{compute cost}
}.
$$

---

# 250. NS-203 migration：第一階段

來源：

$$
203
$$

paper-like artifacts。

---

# 251. 不直接全自動 theorem extraction

先建立 inventory。

---

# 252. Inventory fields

```yaml
artifact_id:
series:
round:
title:
date:
source_hash:
parent_artifact:
```

---

# 253. 第二階段：Section extraction

抽：

- definitions；
- claims；
- propositions；
- lemmas；
- obstructions；
- status statements。

---

# 254. 第三階段：Assumption normalization

建立：

$$
A_i.
$$

---

# 255. 第四階段：Route family

例如：

- RFP；
- CSP；
- DRC；
- MORP；
- DCRP；
- X72。

---

# 256. 第五階段：Obstruction canonicalization

建立：

$$
O_{\mathrm{NS},j}.
$$

---

# 257. 第六階段：Gold audit set

人工抽：

$$
200
$$

對候選 equivalence。

---

# 258. 第七階段：Basin detector calibration

---

# 259. 第八階段：Higher-order sampling

對：

$$
T_1,T_2,T_3,T_X
$$

重新判。

---

# 260. 第九階段：Transfer audit

找：

- other PDE；
- gSQG；
- Boussinesq；
- abstract lemma。

---

# 261. 第十階段：Router simulation

用歷史 corpus：

$$
H_t
$$

重播。

---

# 262. 問：

> 如果當時有 saturation detector，會不會更早切路？

---

# 263. Counterfactual replay

只能說：

$$
\text{policy simulation}.
$$

不代表真歷史。

---

# 264. NS-203 v2 的目標

不是：

> 證明 NS。

---

# 265. 而是：

$$
\boxed{
\text{建立第一個 theorem-level AI long-horizon proof-space dataset}.
}
$$

---

# 266. 如果過程中真的找到 proof

當然進：

$$
\text{certificate path}.
$$

---

# 267. 但 observatory 成功不依賴最終 proof

---

# 268. 這是重要設計

否則研究 infrastructure 的價值綁在未解題結果。

---

# 269. Dashboard NS overview

顯示：

$$
203
$$

artifacts。

---

# 270. Series map

RFP、CSP、DCRP 等。

---

# 271. Route traffic

---

# 272. Obstruction heatmap

---

# 273. Sampling-order timeline

---

# 274. Novelty timeline

---

# 275. Saturation confidence

---

# 276. Transfer map

---

# 277. Claim ledger

---

# 278. Non-conclusion banner

永遠顯示：

```text
OBSERVATIONAL RESEARCH MAP
NOT A PROOF OF UNSOLVABILITY
```

---

# 279. Civilization-scale extrapolation

未來不只 NS。

---

# 280. 每個重大數學問題都有：

$$
\text{PSO workspace}.
$$

---

# 281. 例如：

- RH；
- BSD；
- Hodge；
- Collatz；
- P/NP。

---

# 282. 但 open-problem workspaces 要嚴格標：

$$
\text{UNRESOLVED}.
$$

---

# 283. Known-problem workspaces 用於 calibration

---

# 284. Cross-problem knowledge graph

$$
G_{\mathrm{math}}.
$$

---

# 285. TheoremGraph 類系統已顯示 statement-level graph 可大規模建立

---

# 286. PSO 再加入：

- failed routes；
- lineage；
- research status；
- costs；
- experiment branches。

---

# 287. 從 theorem graph 到 research graph

$$
\boxed{
\text{Theorem Graph}
\subset
\text{Research Graph}.
}
$$

---

# 288. Research Graph 還有 unresolved object

這是最大差別。

---

# 289. 未解狀態也要可表示

例如：

$$
\text{OPEN_OBSTRUCTION}.
$$

---

# 290. Graph 不只記成功史

---

# 291. 這會改變 AI training data

目前 theorem prover data 偏成功 proof。

---

# 292. APRIL 類 failure dataset 已開始修正

---

# 293. PSO 可以產生更高階 data

不是只：

$$
\text{failure}\rightarrow\text{repair}.
$$

---

# 294. 還有：

$$
\text{failure family}
\rightarrow
\text{obstruction class}
\rightarrow
\text{route switch}.
$$

---

# 295. Training object

可以訓練：

$$
\text{research policy model}.
$$

---

# 296. Policy target

不是 next tactic。

而是：

$$
\text{next research move}.
$$

---

# 297. 例如：

> 不要再證這條，換 premise retrieval。

---

# 298. 這就是 AI co-mathematician 的一個真正差異

---

# 299. Co-mathematician 需要 research memory

否則每輪都：

$$
\text{amnesia}.
$$

---

# 300. Research identity 不是人格 identity

系統只需：

$$
\text{persistent state}.
$$

---

# 301. Session continuity

每次 agent 讀：

$$
\text{current workspace state}.
$$

---

# 302. 不需要讀全部歷史全文

---

# 303. Selective context assembly

根據：

- basin；
- obstruction；
- route；
- current claim。

---

# 304. Context compiler

$$
\mathcal C_{\mathrm{ctx}}(s_t).
$$

---

# 305. 輸出：

$$
\text{minimal sufficient context}.
$$

---

# 306. 這能降低 context explosion

---

# 307. Context provenance

每段 context 都知道來源 ID。

---

# 308. AI 不能把摘要當 canonical source

---

# 309. Research query 到 source

一鍵追：

$$
\text{claim}
\rightarrow
\text{source lines}.
$$

---

# 310. Formal proof 到 source

$$
\Pi
\rightarrow
\text{Lean file}.
$$

---

# 311. Obstruction 到 evidence

$$
O
\rightarrow
\{r_1,r_2,\ldots\}.
$$

---

# 312. Basin 到 members

---

# 313. Saturation 到 metric version

---

# 314. 每個數字都可追

這是 observatory 的本質。

---

# 315. Security

AI research memory 可能含：

- unpublished results；
- code；
- credentials；
- private data。

---

# 316. Credential 永不進 PSO graph

---

# 317. Secret store 分離

---

# 318. Access control

object-level ACL。

---

# 319. Public / private / embargoed

---

# 320. Citation provenance

公開輸出只引用：

$$
\text{publicly releasable source}.
$$

---

# 321. Sandbox experiment

故意錯 parent 的 PMW experiment 必須隔離。

---

# 322. 不讓 experimental falsehood 污染 canonical core

---

# 323. Namespace

```text
CANONICAL/
EXPERIMENTAL/
HISTORICAL/
REFUTED/
```

---

# 324. Governance

PSO 不應只有「admin 可以改一切」。

---

# 325. 高風險操作

- delete certificate；
- change canonical theorem；
- merge obstruction；
- mark PROVEN；
- reframe problem。

---

# 326. 需要 audit log

---

# 327. 甚至雙重核准

對：

$$
\text{PROVEN}
$$

可要求：

$$
\text{formal verifier + human/independent audit}.
$$

---

# 328. Automation 可以更快

但 governance 必須更嚴格。

---

# 329. Reproducible release

每個 research milestone：

$$
R_v.
$$

---

# 330. Release contents

- canonical sources；
- graph export；
- metrics；
- validation；
- checksums；
- methodology；
- known limitations。

---

# 331. Graph export

可用：

- GraphML；
- JSONL；
- Parquet。

---

# 332. Metric export

CSV / Parquet。

---

# 333. Human-readable report

Markdown。

---

# 334. Machine-readable status

JSON。

---

# 335. Release fingerprint

$$
h_{\mathrm{release}}.
$$

---

# 336. Rebuild script

一鍵：

$$
\text{source}
\rightarrow
\text{graph}
\rightarrow
\text{metrics}.
$$

---

# 337. 如果不能 rebuild

觀測站不可靠。

---

# 338. PSO 的最小 MVP

不需要一開始 civilization scale。

---

# 339. MVP 只做六件事

1. artifact ingest；
2. claim/assumption extraction；
3. route/obstruction graph；
4. status typing；
5. metric calculation；
6. interactive dashboard。

---

# 340. MVP storage

甚至：

- SQLite；
- files；
- NetworkX；

就可以開始。

---

# 341. 不要一開始過度工程

---

# 342. Phase 1：NS-203 offline observatory

---

# 343. Phase 2：Incremental ingest

新 paper 加入即更新。

---

# 344. Phase 3：Formal backend

接 Lean / AXLE / local Lean。

---

# 345. Phase 4：Multi-agent router

---

# 346. Phase 5：Cross-project federation

---

# 347. Phase 6：Civilization-scale graph

---

# 348. Phase 1 success criteria

至少：

$$
\text{claim extraction precision}>0.8
$$

在 gold sample。

---

# 349. Obstruction merge precision

優先：

$$
>0.9
$$

因 false merge 很危險。

---

# 350. Route graph audit

人工抽查。

---

# 351. Status overclaim rate

$$
O_R\approx0.
$$

---

# 352. Rebuild reproducibility

$$
100\%.
$$

---

# 353. Phase 2 success

新 artifact：

$$
<1
$$

次全圖重算。

---

# 354. Incremental update

---

# 355. Phase 3 success

formal claims：

$$
\text{verifier status}
$$

可回寫 PSO。

---

# 356. Phase 4 success

router 比 random / static baseline：

$$
\text{audited yield}\uparrow.
$$

---

# 357. Phase 5 success

cross-project transfer：

$$
T_D>0.
$$

---

# 358. Phase 6 不應先承諾

civilization scale 是長期方向。

---

# 359. PSO 與一般知識圖譜的差別

一般 KG：

$$
\text{entity relation}.
$$

---

# 360. PSO 另外存：

$$
\boxed{
\text{epistemic status}
+
\text{research dynamics}
+
\text{failed routes}
+
\text{certificate}.
}
$$

---

# 361. PSO 與普通 RAG 的差別

RAG 問：

> 找相關文件。

---

# 362. PSO 問：

> 找與當前 obstruction 結構上相關、但 genealogy 獨立的 route。

---

# 363. PSO 與 theorem prover 的差別

prover 目標：

$$
\text{close goal}.
$$

---

# 364. PSO 目標：

$$
\text{understand and manage the evolving research space}.
$$

---

# 365. PSO 與 project manager 的差別

不是只管理任務進度。

---

# 366. 它管理：

$$
\text{mathematical epistemic structure}.
$$

---

# 367. PSO 與論文資料庫的差別

不是只有：

$$
\text{paper metadata}.
$$

---

# 368. 它有：

$$
\text{claim-level lineage}.
$$

---

# 369. Civilization-scale 版本

如果未來 AI 持續讀取：

$$
10^7
$$

篇數學文件，

TheoremGraph 類 statement graph 會成為底層之一。

---

# 370. PSO 可疊：

$$
\text{research dynamics layer}.
$$

---

# 371. 文明知識的問題將改變

從：

> 我們知道哪些 theorem？

---

# 372. 變成：

> 哪些 theorem 相互依賴？

---

# 373. 再變：

> 哪些路曾被嘗試？

---

# 374. 再變：

> 哪些失敗反覆出現？

---

# 375. 再變：

> 哪些問題已局部飽和？

---

# 376. 再變：

> 哪些 representation 尚未被探索？

---

# 377. 這就是 proof-space science

---

# 378. Proof-space science 的研究對象

不是 theorem 本身。

---

# 379. 而是：

$$
\boxed{
\text{the dynamics of theorem-seeking systems}.
}
$$

---

# 380. 這是一個 meta-science

---

# 381. 但它不取代數學

數學仍由：

$$
\text{proof / counterexample / formal result}
$$

決定。

---

# 382. PSO 只是讓我們更聰明地找

---

# 383. 系列最重要的統一圖

$$
\boxed{
\begin{aligned}
\text{Artifact}
&\rightarrow
\text{Canonical Object}\\
&\rightarrow
\text{Semantic Quotient}\\
&\rightarrow
\text{Proof-Space Graph}\\
&\rightarrow
\text{Higher-Order Sampling}\\
&\rightarrow
\text{Basin / Obstruction}\\
&\rightarrow
\text{Saturation Measurement}\\
&\rightarrow
\text{Diagnosis}\\
&\rightarrow
\text{Research Routing}\\
&\rightarrow
\text{Certificate / Revision}\\
&\rightarrow
\text{Descendant Salvage}.
\end{aligned}
}
$$

---

# 384. 這不是線性 pipeline

任何 stage 都可回饋。

---

# 385. Feedback

例如：

$$
\text{certificate}
\rightarrow
\text{graph rewrite}.
$$

---

# 386. Revision

$$
\rightarrow
\text{descendant re-audit}.
$$

---

# 387. New obstruction

$$
\rightarrow
\text{new branch}.
$$

---

# 388. Dynamic fixed point

成熟 workspace 可能逐漸接近：

$$
\mathcal S^\star.
$$

---

# 389. 但不是停止

新資料仍可：

$$
\mathcal S^\star
\rightarrow
\mathcal S^{\star'}.
$$

---

# 390. Research memory fixed point

指：

$$
\text{stable core + open frontier}.
$$

---

# 391. 這與第 7 篇 truth–generativity tension 接軌

核心可以壓縮，

frontier 仍然開放。

---

# 392. Stable core

$$
\mathcal C^\star.
$$

---

# 393. Open frontier

$$
\mathfrak F.
$$

---

# 394. Mature PSO state

$$
\boxed{
\mathcal S
=
(
\mathcal C^\star,
\mathfrak F,
\mathcal O,
\mathcal H
).
}
$$

其中：

- core；
- frontier；
- obstructions；
- history。

---

# 395. 這比「已知／未知」二分更強

---

# 396. Core 也有版本

---

# 397. Frontier 也有 priority

---

# 398. Obstruction 也有 status

---

# 399. History 也可壓縮但不可抹除

---

# 400. AI 的長程自主研究需求

要真正 autonomous，

至少需要：

1. memory；
2. verification；
3. routing；
4. status discipline；
5. rollback。

---

# 401. 沒 memory

重複。

---

# 402. 沒 verification

幻覺。

---

# 403. 沒 routing

算力浪費。

---

# 404. 沒 status discipline

過度結論。

---

# 405. 沒 rollback

錯誤污染。

---

# 406. PSO 正好對應五個缺口

---

# 407. 非主張總表

本文不主張：

1. Proof-Space Observatory 能自動解決未解數學問題；
2. PSO 可以取代 theorem prover；
3. PSO 可以取代人類數學審查；
4. graph centrality 等於數學重要性；
5. embedding similarity 等於 theorem equivalence；
6. basin decomposition 是證明空間唯一真幾何；
7. saturation metric 是 truth probability；
8. obstruction confluence 等於 unprovability；
9. descendant survival 等於 parent correctness；
10. productive-mis-specification window 普遍存在；
11. formal proof 自動保證 informal statement fidelity；
12. AI-generated claim extraction 可以無審核地進 canonical core；
13. different models 自動提供獨立證據；
14. TheoremGraph、LeanMarathon、AXLE、BlueprintRepair 或 LeanSearch v2 已經等同 PSO；
15. 203 份 NS artifacts 已足以描述全部 Navier--Stokes proof space；
16. NS-203 的 higher-order sampling 證明 Clay formulation 有錯；
17. P/NP 或任何 open problem 可由 PSO saturation 判定不可解；
18. civilization-scale observatory 在目前已工程完成；
19. event sourcing 可解決所有 research-memory 問題；
20. graph database 是唯一合適儲存技術；
21. vector database 可以作 canonical truth store；
22. AI routing policy 可以無治理地修改 canonical theorem；
23. historical refuted theory 應留在 active truth space；
24. negative result 一定有 transfer value；
25. 本文提供的所有公式已是唯一最佳 metric；
26. PSO 應把所有私人／未公開研究公開；
27. 公開 consensus 決定 claim truth；
28. 大規模生成本身代表 scientific progress；
29. 長程研究記憶越大越好而不需 compaction；
30. 本文已建立文明級數學認知的最終架構。

---

# 408. 形式命題一：Paper Non-Primitivity

$$
\boxed{
\text{Paper}
\neq
\text{minimal research unit}.
}
$$

---

# 409. 形式命題二：Canonical-State Principle

$$
\boxed{
\text{rendered view}
\not\equiv
\text{canonical source}.
}
$$

---

# 410. 形式命題三：Typed-Relation Principle

$$
\boxed{
\text{all research edges cannot be reduced to similarity}.
}
$$

---

# 411. 形式命題四：Status-Type Principle

$$
\boxed{
\text{Observation}
\not\rightarrow
\text{Verdict}
}
$$

without certificate。

---

# 412. 形式命題五：Revision-Preservation Principle

$$
\boxed{
P\rightarrow P'
\Rightarrow
\operatorname{Reaudit}(\mathcal D(P)),
}
$$

而不是全刪或全留。

---

# 413. 形式命題六：Graph-Rebuild Principle

若 canonical artifacts 與 event log 完整，

derived graph 應可重建。

---

# 414. 形式命題七：Metric-Version Principle

$$
\boxed{
M
=
M(\text{definition version}).
}
$$

---

# 415. 形式命題八：Routing Non-Verdict

$$
\boxed{
\Pi_{\mathrm{meta}}(S)=\text{reframe}
\not\Rightarrow
\text{original problem wrong}.
}
$$

---

# 416. 形式命題九：Observatory Non-Oracle

$$
\boxed{
\text{PSO}
\neq
\text{truth oracle}.
}
$$

---

# 417. 形式命題十：Research-Memory Expansion

成熟研究記憶至少需要：

$$
\boxed{
\text{proof}
+
\text{failure}
+
\text{revision}
+
\text{provenance}.
}
$$

---

# 418. 與 LSI-PSD-01 的整合

第 1 篇：

$$
\text{search regime}.
$$

PSO 將它實作成：

```yaml
regime_id:
axioms:
language:
methods:
verifier:
budget:
history:
policy:
```

---

# 419. 與第 2 篇的整合

coverage：

$$
I_k
$$

成 dashboard metric。

---

# 420. 與第 3 篇的整合

semantic quotient 成 merge pipeline。

---

# 421. 與第 4 篇的整合

sampling order 成：

```text
order=0/1/2/3/X
```

---

# 422. 與第 5 篇的整合

basin 變成版本化 graph object。

---

# 423. 與第 6 篇的整合

obstruction atlas 變核心資料層。

---

# 424. 與第 7 篇的整合

truth / generativity 分欄存。

---

# 425. 與第 8 篇的整合

parent revision + descendant salvage。

---

# 426. 與第 9 篇的整合

experiment branch support。

---

# 427. 與第 10 篇的整合

epistemic type checker。

---

# 428. 與第 11 篇的整合

historical lineage / status-aware retrieval。

---

# 429. 所以第 12 篇不是再加新概念

而是：

$$
\boxed{
\text{compile the series into a system}.
}
$$

---

# 430. 第一個正式 PSO MVP 專案結構

```text
pso/
├─ artifacts/
├─ canonical/
├─ events/
├─ graph/
├─ metrics/
├─ audits/
├─ experiments/
├─ dashboards/
├─ exports/
└─ tools/
```

---

# 431. `artifacts/`

原始輸入。

---

# 432. `canonical/`

validated sources。

---

# 433. `events/`

append-only JSONL。

---

# 434. `graph/`

derived nodes / edges。

---

# 435. `metrics/`

版本化計算結果。

---

# 436. `audits/`

human / model review。

---

# 437. `experiments/`

branch configs。

---

# 438. `dashboards/`

visualizations。

---

# 439. `exports/`

release packages。

---

# 440. `tools/`

rebuild / validate。

---

# 441. Minimum event schema

```yaml
event_id:
timestamp:
actor:
action:
object_id:
object_version:
payload:
parent_event:
signature:
```

---

# 442. Minimum claim schema

```yaml
claim_id:
problem_id:
text:
formal_statement:
scope:
status:
source_refs:
assumptions:
dependencies:
certificate_ids:
version:
```

---

# 443. Minimum edge schema

```yaml
edge_id:
source:
target:
type:
confidence:
audit:
provenance:
```

---

# 444. Minimum metric schema

```yaml
metric_id:
name:
definition_version:
scope:
value:
uncertainty:
inputs:
computed_at:
```

---

# 445. Minimum audit schema

```yaml
audit_id:
target:
auditor:
method:
result:
confidence:
notes:
source_refs:
```

---

# 446. PSO 的一句工程判斷

如果一個數字無法回答：

> 從哪些 source、哪個 metric version、哪些 edge 算出來？

那它不應進正式 dashboard。

---

# 447. Auditability over aesthetics

漂亮圖：

$$
\neq
$$

可靠 observatory。

---

# 448. Interactive graph 只是 UI

canonical graph export 才是 source。

---

# 449. Version-controlled dashboard

圖表也標：

$$
\text{data version}.
$$

---

# 450. Release validation

每次：

1. validate source；
2. validate graph schema；
3. validate checksums；
4. recompute key metrics；
5. archive report。

---

# 451. Regression tests

例如：

- node count；
- edge count；
- known gold pairs；
- known status transitions。

---

# 452. Metric regression

新版 metric 不應 silent replace old。

---

# 453. 兩版並存

$$
\rho^{(v1)},
\rho^{(v2)}.
$$

---

# 454. PSO 自身也要可科學研究

這是 meta-observatory。

---

# 455. 我們可以問：

> 哪個 basin detector 比較準？

---

# 456. 哪個 router 更有效？

---

# 457. 哪個 model 更容易 overclaim？

---

# 458. 哪個 verifier / retriever 造成 bias？

---

# 459. Observatory becomes benchmark platform

---

# 460. Civilization-scale AI mathematics 的可能終局

未來每一個新 theorem 不只是 PDF。

---

# 461. 它帶：

- machine-checkable statement；
- dependencies；
- provenance；
- research history；
- failed routes；
- certificates。

---

# 462. Paper 變成 view

canonical knowledge 變成 graph + source。

---

# 463. 但人類 prose 不會消失

prose 仍是：

$$
\text{interpretation interface}.
$$

---

# 464. Machine graph 也不會取代 prose

兩者互補。

---

# 465. Formal / informal duality

$$
\boxed{
\text{formal rigor}
+
\text{informal meaning}.
}
$$

---

# 466. TheoremGraph 已展示橋接可能性

PSO 把橋再延伸到：

$$
\text{research process}.
$$

---

# 467. 最終 architecture

$$
\boxed{
\text{Source}
\leftrightarrow
\text{Formal}
\leftrightarrow
\text{Graph}
\leftrightarrow
\text{Memory}
\leftrightarrow
\text{Agent}.
}
$$

---

# 468. 人類的位置

不是被移除。

---

# 469. 人類成為：

- question setter；
- auditor；
- value setter；
- framing reviewer；
- release authority。

---

# 470. AI 的位置

成為：

- explorer；
- compiler；
- verifier user；
- graph maintainer；
- hypothesis generator。

---

# 471. Proof assistant 的位置

成為：

$$
\text{formal certificate engine}.
$$

---

# 472. Observatory 的位置

成為：

$$
\text{research memory and routing layer}.
$$

---

# 473. 這四個角色不應混成一個模型

---

# 474. 最終系統不是「超級聊天機器人」

而是：

$$
\boxed{
\text{a governed research operating system}.
}
$$

---

# 475. 對文明級研究的最低要求

如果 AI 未來要自主研究數十年，

它必須知道：

> 我以前做過什麼。

---

# 476. 更重要：

> 我以前為什麼放棄。

---

# 477. 更重要：

> 哪些放棄後來證明是錯的。

---

# 478. 更重要：

> 哪些失敗其實是通用 obstruction。

---

# 479. 更重要：

> 哪些「已知」其實只是舊版本 hypothesis。

---

# 480. 這就是研究文明的記憶

---

# 481. 系列最終閉環

$$
\boxed{
\begin{aligned}
\text{Generate}
&\rightarrow
\text{Record}\\
&\rightarrow
\text{Verify}\\
&\rightarrow
\text{Quotient}\\
&\rightarrow
\text{Map}\\
&\rightarrow
\text{Measure}\\
&\rightarrow
\text{Diagnose}\\
&\rightarrow
\text{Route}\\
&\rightarrow
\text{Revise}\\
&\rightarrow
\text{Salvage}\\
&\rightarrow
\text{Generate}.
\end{aligned}
}
$$

---

# 482. 這是一個動態研究循環

而不是：

$$
\text{prompt}
\rightarrow
\text{answer}.
$$

---

# 483. PSO 的第一個實驗性定義

本文正式提出：

$$
\boxed{
\textbf{An AI Proof-Space Observatory is a versioned, provenance-preserving, epistemically typed system that converts long-horizon mathematical research traces into auditable research objects, graphs, measurements, and routing decisions without treating search statistics as mathematical verdicts.}
}
$$

---

# 484. 中文定義

**AI 證明空間觀測站**是一個：

> 將長程數學研究軌跡轉換成可版本化、可追溯、具認識論型別的研究物件、圖結構、量測值與研究路由，並明確禁止把搜尋統計直接當成數學判決的研究記憶系統。

---

# 485. PSO 的最低成功標準

不是證出 NS。

---

# 486. 而是：

> 兩年後，任何 agent 都能準確知道過去兩年哪些路試過、哪些是真的重複、哪些失敗已被證明、哪些只是猜測、哪些假設後來被撤銷。

---

# 487. 如果能做到

就已經比單純論文堆積前進了一個研究文明層級。

---

# 488. 結論

LSI-PSD 系列最初從一個非常簡單的觀察開始：

> 如果 AI 在同一個難題上持續生成上百、上千、上萬輪研究，最後先被耗盡的也許不是「數學真理」，而是某些符號、方法、路徑與障礙的可區分研究空間。

從這個起點，系列逐步建立：

$$
\text{proof-space coverage},
$$

$$
\text{semantic quotient},
$$

$$
\text{higher-order resampling},
$$

$$
\text{local saturation},
$$

$$
\text{obstruction confluence},
$$

$$
\text{truth--generativity inversion},
$$

$$
\text{productive mis-specification},
$$

$$
\text{non-conclusion firewall}.
$$

但如果這些概念只停在論文裡，它們仍然只是方法論描述。

第十二篇的任務，就是把它們變成一個研究系統。

這個系統的核心不是更大的模型。

而是：

$$
\boxed{
\text{better memory}
+
\text{better structure}
+
\text{better verification}
+
\text{better epistemic discipline}.
}
$$

它要保存：

$$
\text{what was proved},
$$

也保存：

$$
\text{what was tried}.
$$

保存：

$$
\text{what failed},
$$

也保存：

$$
\text{why it failed}.
$$

保存：

$$
\text{what was believed},
$$

也保存：

$$
\text{when that belief was downgraded}.
$$

保存：

$$
\text{which parent theory was revised},
$$

也保存：

$$
\text{which descendants survived}.
$$

這會讓 AI 數學研究第一次不只是高速生成。

而是形成：

$$
\boxed{
\text{persistent research memory}.
}
$$

當這種記憶與 formal verification、graph retrieval、multi-agent branching、controlled experiments 與 human audit 結合，數學研究的單位可能從「單篇 paper」轉變成：

$$
\boxed{
\text{versioned research relation}.
}
$$

一個 theorem 不再只是一個 final statement。

它會帶著：

- assumptions；
- dependencies；
- proof；
- failed alternatives；
- historical revisions；
- transfer links。

而一個未解問題也不再只是一個空白格。

它可以有：

$$
\text{known basins},
$$

$$
\text{known obstructions},
$$

$$
\text{known no-go families},
$$

$$
\text{open frontiers}.
$$

因此本文提出整個系列最後兩個命題。

第一：

$$
\boxed{
\textbf{The future unit of mathematical research memory should not be the paper, but the versioned, typed, provenance-preserving research relation.}
}
$$

第二：

$$
\boxed{
\textbf{A civilization-scale AI research system should remember not only what humanity knows, but how knowledge was reached, where inquiry failed, and which alternatives remain genuinely open.}
}
$$

而其中最重要的限制仍然沒有改變：

$$
\boxed{
\textbf{The observatory observes research. It does not replace mathematics.}
}
$$

這句話也完成 LSI-PSD 主系列的封頂。

---

# 參考文獻

1. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., & Liu, F. (2026). **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** arXiv:2606.05400.

2. Kurgan, S., Wang, E., Leonen, E., Szeto, S., Alexander, L., Remizov, A., Alper, J., Inchiostro, G., & Ilin, V. (2026). **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363.

3. Xin, J., Schneidman, A., Cummins, C., Ram, K., Ganesh, S., & Limperg, J. (2026). **AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities.** arXiv:2606.26442.

4. Khrulev, R. (2026). **BlueprintRepair: Typed Local Edits for Failed Lean Proof Blueprints.** arXiv:2607.28110.

5. Gao, G. et al. (2026). **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137.

6. Pham, Q. V., Karimov, E., Galichin, A., & Oseledets, I. (2026). **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics.** arXiv:2606.09450.

7. Wang, E., Chess, S., Lee, D., Ge, S., Mallavarapu, A., & Ilin, V. (2026). **Learning to Repair Lean Proofs from Compiler Feedback.** arXiv:2602.02990.

8. Yin, D., & Gao, J. (2025). **Generating Millions Of Lean Theorems With Proofs By Exploring State Transition Graphs.** arXiv:2503.04772.

9. George, R. J., Huang, S., Song, P., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925.

10. Xin, R. et al. (2025). **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving.** arXiv:2502.03438.

11. Qiu, R. et al. (2026). **Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving.** arXiv:2603.24465.

12. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468.

13. Chen, T., & Li, Z. (2026). **A Theoretical Framework for Self-Play Theorem Proving Algorithms.** arXiv:2606.01861.

14. Wang, A. et al. (2025). **Don't Get Lost in the Trees: Streamlining LLM Reasoning by Overcoming Tree Search Exploration Pitfalls.** arXiv:2502.11183.

15. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493.

16. Zhang, K. et al. (2026). **Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization.** arXiv:2606.31002.

17. Kim, J., Han, H., & Hwang, S.-w. (2026). **Benchmarking Testing in Automated Theorem Proving.** arXiv:2604.23698.

18. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Reproducible internal corpus analysis, 2026-08-17.

---

## 附錄 A：PSO 核心實體總表

| Entity | 作用 |
|---|---|
| Problem | 研究目標 |
| Claim | 可判定主張 |
| Assumption | 前提 |
| Lemma | 可重用局部結果 |
| ProofState | formal proof state |
| Route | 研究／證明路線 |
| Obstruction | canonical failure structure |
| Basin | 局部 proof-space region |
| Certificate | verdict-specific evidence |
| Revision | parent/version change |
| Experiment | controlled branch |
| Artifact | canonical file/source |

---

## 附錄 B：PSO edge types

```text
DEPENDS_ON
IMPLIES
CONTRADICTS
EQUIVALENT_CANDIDATE
EQUIVALENT_CERTIFIED
DERIVES
REVISITS
CONVERGES_TO
RESOLVES
REVIVES
TRANSFERS_TO
REVISES
DESCENDS_FROM
CERTIFIES
REFUTES
FORMALIZES
INTERPRETS
ESCAPES_TO
```

---

## 附錄 C：PSO MVP 設定

```yaml
storage:
  artifacts: filesystem
  metadata: sqlite
  graph: networkx
  events: jsonl
  metrics: parquet

verification:
  lean:
    enabled: optional
  source_validation:
    utf8: true
    canonical_math_delimiters: true

ingest:
  markdown: true
  zip_recursive: true
  lean: true

objects:
  - problem
  - claim
  - assumption
  - route
  - obstruction
  - basin
  - certificate
  - revision

metrics:
  - novelty
  - audited_yield
  - confluence
  - saturation
  - descendant_survival

governance:
  target_rewrite_requires_audit: true
  status_upgrade_requires_certificate: true
  canonical_source_immutable: true
```

---

## 附錄 D：NS-203 migration checklist

- [ ] 建立 203 artifacts canonical inventory
- [ ] 每篇建立 source hash
- [ ] 抽取 section / claim / assumption
- [ ] 抽取 explicit dependency
- [ ] 建 route family
- [ ] 建 obstruction candidate
- [ ] 建 200-pair gold audit set
- [ ] 校準 semantic quotient
- [ ] 校準 obstruction merge
- [ ] 校準 basin detector
- [ ] 重算 $T_1,T_2,T_3,T_X$
- [ ] 建 higher-order sampling timeline
- [ ] 建 cross-series confluence graph
- [ ] 建 transfer candidate graph
- [ ] 建 status ledger
- [ ] 建 release package與 checksums

---

## 附錄 E：Epistemic firewall

```text
SEARCH STATISTIC
      |
      v
OBSERVATION
      |
      v
DIAGNOSTIC HYPOTHESIS
      |
      +---- no certificate ----> remain hypothesis
      |
      +---- proof -------------> PROVEN
      |
      +---- counterexample ----> REFUTED
      |
      +---- no-go theorem -----> FORMAL_NO_GO
      |
      +---- independence ------> INDEPENDENT_RELATIVE_TO_T
```

---

## 附錄 F：一句話版本

$$
\boxed{
\text{真正的 AI 數學記憶，不應只記得答案；它必須記得整個研究空間是怎麼被走過的。}
}
$$

而真正的 AI 證明空間觀測站，也不是替數學下判決：

$$
\boxed{
\text{它只負責讓每一次探索、失敗、修正與證明，都不再白白消失。}
}
$$
