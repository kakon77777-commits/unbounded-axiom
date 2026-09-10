# Series C — C06｜全域展開、連結與收斂：類全域觀察者的核心計算循環
## Global Expansion, Linking, and Convergence: The Core Computation Loop of a Quasi-Global Observer

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 06 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-06  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Foundational Theory / Global Computation Loop / Attention Routing / Convergence

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文承接 C01–C05：

- C01：Global Observer；
- C02：Global-to-Local / Local-to-Global Duality；
- C03：Difference → Ambiguity → Set → Domain；
- C04：Legal Action / Cross-Domain Bridge / World Composition；
- C05：Probability Domain / Uncertainty / World Prediction Envelope。

C06 的核心問題是：

> **即使 AI 已經知道如何看、如何分域、如何建立合法 bridge、如何保存 uncertainty，它要怎麼在有限算力下真的把這個世界「跑起來」？**

---

# 摘要

如果 Global Observer 只會建立巨大知識圖、無限制展開所有可能、窮舉所有 branch、追蹤所有 relation，它不會成為真正的 Global AI。

它只會成為：

$$
\boxed{
\text{Unbounded Explosion}.
}
$$

因此 Global Computation 的核心從來不是「全部展開」，而是：

$$
\boxed{
\text{Compute Globally}
\neq
\text{Materialize Everything}.
}
$$

本文提出一個核心循環：

$$
\boxed{
\text{Expand}
\rightarrow
\text{Differentiate}
\rightarrow
\text{Link}
\rightarrow
\text{Prune}
\rightarrow
\text{Converge}.
}
$$

簡寫為：

$$
\boxed{
\mathcal G_{ELC}
=
\mathcal C
\circ
\mathcal P
\circ
\mathcal L
\circ
\mathcal D
\circ
\mathcal E.
}
$$

其中：

- $\mathcal E$：Expansion；
- $\mathcal D$：Differentiation；
- $\mathcal L$：Legal Linking；
- $\mathcal P$：Pruning / Compression；
- $\mathcal C$：Convergence。

本文不將此 loop 理解為單次 pipeline，而是 recurrent process：

$$
\boxed{
W_t
\rightarrow
\mathcal G_{ELC}
\rightarrow
W_{t+1}
\rightarrow
\mathcal G_{ELC}
\rightarrow
W_{t+2}.
}
$$

Global Observer 每一輪都重新決定：

- 哪些 domain 要展開；
- 哪些差異要保留；
- 哪些 bridge 要建立或撤銷；
- 哪些 branch 可以壓縮；
- 哪些 uncertainty 不能丟掉；
- 哪些局部結果可收斂成 world-level state；
- 哪些 global conclusion 還必須保持 open。

本文將全域注意力寫成一個資源分配場：

$$
\boxed{
\mathbf a_t
=
\{a_i(t)\}_{i\in I},
\qquad
\sum_i a_i(t)\le B_t.
}
$$

其中 $a_i(t)$ 是 domain $D_i$ 在時間 $t$ 的 active attention / compute allocation， $B_t$ 是 bounded resource budget。

這意味著：

$$
\boxed{
\text{Global Attention}
\neq
\text{Equal Attention Everywhere}.
}
$$

真正的 globality 是：

$$
\boxed{
\text{importance-weighted adaptive coverage}.
}
$$

因此本文定義 **Global Attention Routing Function**：

$$
\boxed{
a_i(t+1)
=
\mathsf{Route}
(
Risk_i,
Uncertainty_i,
Novelty_i,
Dependency_i,
Impact_i,
Debt_i,
Budget_t
).
}
$$

這使 AI 可以在世界內動態移動解析度與算力，而不是永久固定 attention。

本文進一步定義 **Expansion Frontier**：

$$
\boxed{
\mathcal F_E(t)
=
\{D_i:NeedExpand(D_i,t)=1\}.
}
$$

Expansion 只對 frontier domain 做 selective materialization，不對整個 world 無限展開。

接著使用 C03 的 difference governance，建立：

$$
\boxed{
\mathcal D:
D_i
\rightarrow
\{D_{i1},\ldots,D_{ik}\}
}
$$

或在另一方向做 merge / compression。

Link 階段則必須承接 C04：

$$
\boxed{
\mathcal L
:
D_i
\xrightarrow{B_{ij}}
D_j,
}
$$

且：

$$
\boxed{
\text{Link}
\neq
\text{Associate}.
}
$$

只有經過 type、boundary、authority、loss、uncertainty 與 verifier 檢查的 bridge，才可進入 global computation graph。

Prune 階段則承接 C05。Prune 不是把低 probability branch 全部刪掉，而是依：

$$
\boxed{
Priority_i
=
f(
Probability_i,
Impact_i,
Irreversibility_i,
InformationValue_i,
Novelty_i
).
}
$$

決定保留、壓縮、延後或淘汰。

因此：

$$
\boxed{
\text{Low Probability}
\not\Rightarrow
\text{Low Priority}.
}
$$

最後的 Convergence 也不是把所有 uncertainty 壓成一個答案，而是把 world state 收束到：

$$
\boxed{
W_t^\ast
=
\left\langle
ActiveDomains,
StableBridges,
OpenBranches,
KnownUnknowns,
ActionableConclusions,
DeferredDebt
\right\rangle.
}
$$

本文稱此為 **Operational Global Convergence**。

因此：

$$
\boxed{
\text{Convergence}
\neq
\text{Deterministic Closure}.
}
$$

一個 global loop 可以收斂到：

- 唯一解；
- 多 branch；
- interval；
- bounded unknown；
- deferred decision；
- escalation；
- non-action。

只要 computational status 正確。

本文進一步提出 **Global Computation Pressure**：

$$
\boxed{
P_G
=
E_{expand}
+
D_{difference}
+
B_{bridge}
+
U_{uncertainty}
+
C_{coordination}.
}
$$

如果：

$$
P_G\gg B_t,
$$

系統必須做：

$$
\boxed{
\text{Selective Realization}.
}
$$

這延續 GCM 的核心：

$$
\boxed{
\text{Finite Active Realization}
+
\text{Unbounded Extensibility}.
}
$$

本文也提出 **Recursive Globality Without Recursive Full Expansion**：

$$
\boxed{
\text{Recursive Globality}
\neq
\text{Recursive Full Materialization}.
}
$$

Global Observer 可以知道某 domain 下仍有無限或巨大 substructure，而不需要現在全部展開。

因此世界可以表示為：

$$
\boxed{
W
=
ActiveState
+
LatentStructure
+
ExpansionPointers
+
Debt
+
History.
}
$$

本文最後建立一組測量量：

**Global Coverage**

$$
\boxed{
C_G
=
\frac{
\sum_i w_i c_i
}{
\sum_i w_i
}.
}
$$

其中 $w_i$ 是 domain importance， $c_i$ 是有效 coverage。

**Global Attention Efficiency**

$$
\boxed{
E_A
=
\frac{
VerifiedWorldGain
}{
Compute+Memory+Tool+TimeCost
}.
}
$$

**Convergence Integrity**

$$
\boxed{
I_C
=
F(
LocalValidity,
BridgeValidity,
UncertaintyPreservation,
DebtVisibility,
Actionability
).
}
$$

**World Closure Error**

$$
\boxed{
L_W
=
L_{collapse}
+
L_{fragment}
+
L_{bridge}
+
L_{prune}
+
L_{converge}.
}
$$

C06 的核心命題可以濃縮成：

$$
\boxed{
\text{Global intelligence is not maximum expansion;
it is disciplined expansion under global constraints}.
}
$$

以及：

> **真正的類全域觀察者，不是把世界全部攤開，而是知道何時展開、展開到哪裡、哪些要連、哪些不能連、哪些必須保留、以及何時已經足以收斂成行動。**

**關鍵詞：** Global Computation、Expansion、Differentiation、Legal Linking、Pruning、Convergence、Attention Routing、Selective Materialization、Global AI、World Closure

---

# 1. 為什麼全域計算最容易爆炸？

世界本身包含：

- 多域；
- 多尺度；
- 多時間；
- 多 representation；
- 多 branch；
- 多 uncertainty。

如果全部 materialize：

$$
|W_{active}|
\rightarrow
\infty
$$

或至少快速超過當前 resource budget。

---

# 2. 所以 Global 不等於 Full Expansion

$$
\boxed{
\text{Global}
\neq
\text{Everything Active}.
}
$$

---

# 3. Global Dependency

AI 可以知道：

$$
D_i
\rightarrow
D_j
$$

存在 dependency，

但不必立即展開 $D_j$ 全部內容。

---

# 4. Dependency Pointer

可以保留：

$$
\boxed{
Ptr(D_j).
}
$$

需要時再 materialize。

---

# 5. Latent World

因此 world 可分：

$$
\boxed{
W
=
W_{active}
+
W_{latent}.
}
$$

---

# 6. Active 不等於 More True

只是目前被 materialize。

---

# 7. Latent 不等於 Unknown

latent structure 可以是已知但未展開。

---

# 8. Unknown 是另一狀態

$$
\boxed{
Latent
\neq
Unknown.
}
$$

---

# 9. Global ELC Loop

本文核心：

$$
\boxed{
\text{Expand}
\rightarrow
\text{Differentiate}
\rightarrow
\text{Link}
\rightarrow
\text{Prune}
\rightarrow
\text{Converge}.
}
$$

---

# 10. 這不是線性 pipeline

收斂後可能重新展開。

所以：

$$
\boxed{
ELC_t
\rightarrow
ELC_{t+1}.
}
$$

---

# 11. Expansion

Expansion 的問題：

> 哪裡值得變得更細？

---

# 12. Expansion 不是 Retrieval

retrieval 只是拿資料。

Expansion 還包括：

- deeper state；
- finer representation；
- more branches；
- hidden variables；
- new domain candidates。

---

# 13. Expansion Trigger

定義：

$$
\boxed{
NeedExpand(D_i)
=
f(
Debt_i,
Risk_i,
Uncertainty_i,
Conflict_i,
Novelty_i
).
}
$$

---

# 14. Expansion Frontier

$$
\boxed{
\mathcal F_E(t)
=
\{D_i:NeedExpand(D_i,t)\ge\tau_E\}.
}
$$

---

# 15. Frontier 可同時多個

$$
|\mathcal F_E|>1.
$$

---

# 16. Expansion Budget

給：

$$
B_E.
$$

---

# 17. Frontier Allocation

$$
\sum_{D_i\in\mathcal F_E}a_i
\le
B_E.
$$

---

# 18. High-Risk Domain 優先

例如：

$$
Risk_i\uparrow
\Rightarrow
a_i\uparrow.
$$

---

# 19. 但 risk 不是唯一權重

還要看：

- uncertainty；
- centrality；
- potential information gain；
- irreversibility；
- dependency fan-out。

---

# 20. Information Gain

定義概念量：

$$
\boxed{
IG(D_i)
=
H(W_t)
-
\mathbb E[H(W_{t+1})\mid Expand(D_i)].
}
$$

---

# 21. Expansion 可選擇高 IG domain

但高風險低 IG domain 仍可能必須展開。

---

# 22. Risk-Information Tradeoff

$$
\boxed{
Priority_E
=
f(
IG,
Risk,
Impact,
Debt
).
}
$$

---

# 23. Differentiation

Expansion 後不是全部保留。

需要 C03 的：

$$
\boxed{
\mathsf{Differentiate}.
}
$$

---

# 24. Split

若：

$$
D_i
$$

包含不同 law regimes，可拆：

$$
D_i
\rightarrow
D_{i1},D_{i2}.
$$

---

# 25. Merge

若兩 domain 過度分裂：

$$
D_i,D_j
\rightarrow
D_{ij}.
$$

---

# 26. Repartition

$$
\mathcal P_t
\rightarrow
\mathcal P_{t+1}.
$$

---

# 27. Differentiation 目標

保留：

$$
\boxed{
\text{task-relevant distinctions}.
}
$$

---

# 28. Link

有了 domains 後，不能只靠 similarity link。

---

# 29. Legal Linking

承接 C04：

$$
\boxed{
D_i
\xrightarrow{B_{ij}}
D_j.
}
$$

---

# 30. Link Gate

只有：

$$
\mathcal L(B_{ij})=1
$$

才可進 active global graph。

---

# 31. Unknown Link

若：

$$
\mathcal L(B_{ij})=?,
$$

可進：

$$
G_{pending}.
$$

---

# 32. Forbidden Link

$$
\mathcal L(B_{ij})=0
$$

應進 negative structure。

---

# 33. 所以 active graph 至少有

$$
\boxed{
G_{allowed},
G_{pending},
G_{forbidden}.
}
$$

---

# 34. Link 也有成本

$$
Cost(B_{ij}).
$$

---

# 35. Link 也有 loss

$$
L_B(B_{ij}).
$$

---

# 36. Link 也有 uncertainty

$$
U_B(B_{ij}).
$$

---

# 37. 所以不是越多 bridge 越好

---

# 38. Bridge Explosion

若：

$$
n
$$

個 domains 全互連，

edge 上限：

$$
O(n^2).
$$

---

# 39. Global AI 必須做 sparse linking

只保留 relevant bridge。

---

# 40. Sparse Global Graph

$$
\boxed{
G_G^{sparse}
}
$$

不代表低 globality。

---

# 41. 反而可能更高效

如果它保留真正重要 dependency。

---

# 42. Prune

Prune 是最容易被誤解的一步。

---

# 43. Prune 不等於 Delete

它可以是：

- compress；
- defer；
- archive；
- merge；
- reduce resolution；
- remove from active set。

---

# 44. Active / Dormant

可區分：

$$
\boxed{
D_i^{active},
D_i^{dormant}.
}
$$

---

# 45. Dormant 仍保留 pointer

未來可重新展開。

---

# 46. Prune Criterion

定義：

$$
\boxed{
P_i
=
f(
Probability,
Impact,
Irreversibility,
InformationValue,
Novelty,
Cost
).
}
$$

---

# 47. Low Probability 不等於 Prune

$$
\boxed{
p_i\downarrow
\not\Rightarrow
Prune(i).
}
$$

---

# 48. Low Probability / High Impact

需要保留。

---

# 49. Risk-Weighted Branch

$$
\boxed{
R_i
=
p_i
\times
Impact_i
}
$$

只是最簡版本。

---

# 50. 還需加入 irreversibility

$$
\boxed{
R_i^\ast
=
f(
p_i,
Impact_i,
Irreversibility_i
).
}
$$

---

# 51. Unknown Probability

有些 branch 甚至沒有可靠 $p_i$。

---

# 52. 仍可因高 impact 被保留。

---

# 53. Prune Debt

如果 branch 被壓縮：

$$
\boxed{
Debt_P(i)
}
$$

記錄被丟掉哪些 detail。

---

# 54. Re-expand Trigger

當：

$$
Risk_i\uparrow
$$

或：

$$
Evidence_i\uparrow,
$$

可以重新 materialize。

---

# 55. Convergence

Convergence 的問題：

> 現在足不足以形成 world-level operational state？

---

# 56. Convergence 不等於「有唯一答案」

承接 C05：

$$
\boxed{
\text{Convergence}
\neq
\text{Deterministic Closure}.
}
$$

---

# 57. Operational Global Convergence

本文定義：

$$
\boxed{
W_t^\ast
=
\left\langle
ActiveDomains,
StableBridges,
OpenBranches,
KnownUnknowns,
ActionableConclusions,
DeferredDebt
\right\rangle.
}
$$

---

# 58. 可以收斂到多 branch

$$
\{W_1,W_2,W_3\}.
$$

---

# 59. 可以收斂到 interval

$$
[a,b].
$$

---

# 60. 可以收斂到 Unknown

只要 unknown type 正確。

---

# 61. 可以收斂到 Non-Action

$$
\mathsf{DoNothing}.
$$

---

# 62. 可以收斂到 Escalation

$$
\mathsf{Escalate}.
$$

---

# 63. 可以收斂到 More Observation Required

$$
\mathsf{ObserveMore}(D_i).
$$

---

# 64. Convergence Criterion

可寫：

$$
\boxed{
Ready(W_t)
=
f(
Coverage,
ResidualRisk,
Uncertainty,
Debt,
Actionability
).
}
$$

---

# 65. Ready 不必等於 Perfect

---

# 66. Operational Sufficiency

$$
\boxed{
\text{Sufficient for current decision}
\neq
\text{complete world knowledge}.
}
$$

---

# 67. Global Attention Field

令：

$$
\mathbf a_t
=
\{a_i(t)\}.
$$

---

# 68. Budget

$$
\sum_i a_i(t)\le B_t.
$$

---

# 69. Global Attention 不平均

$$
\boxed{
a_i\neq a_j
}
$$

完全正常。

---

# 70. Equal Attention Everywhere 反而浪費

---

# 71. Attention Routing

$$
\boxed{
a_i(t+1)
=
\mathsf{Route}
(
Risk_i,
Uncertainty_i,
Novelty_i,
Dependency_i,
Impact_i,
Debt_i,
Budget_t
).
}
$$

---

# 72. Risk

高風險 domain 得更多 attention。

---

# 73. Uncertainty

高 uncertainty domain 可能需要更多 observation。

---

# 74. Novelty

新 domain 可能需要探索。

---

# 75. Dependency

高度 central domain 影響多處。

---

# 76. Impact

後果大。

---

# 77. Debt

過去尚未完成的驗證／glue。

---

# 78. Attention Routing 不是單一排序

可以多目標 optimization。

---

# 79. Attention Wave

某 domain 可能：

$$
a_i(t)
\ll
a_i(t+1)
$$

突然跳高。

---

# 80. Pulse-Like Globality

這接 C01 的脈衝式 globality。

---

# 81. 世界事件可以引起 attention phase shift

例如：

- 新漏洞；
- 法規變更；
- sensor anomaly；
- scientific discovery。

---

# 82. Dynamic Criticality

Global Observer 要持續估：

$$
\boxed{
K_i(t)
=
Criticality(D_i,t).
}
$$

---

# 83. Criticality 不是固定 centrality

會隨時間變。

---

# 84. Event-Driven Reallocation

$$
Event
\rightarrow
K_i\uparrow
\rightarrow
a_i\uparrow.
$$

---

# 85. Global Attention Coverage

定義：

$$
\boxed{
C_G
=
\frac{
\sum_i w_i c_i
}{
\sum_i w_i
}.
}
$$

---

# 86. $w_i$

domain importance。

---

# 87. $c_i$

有效 coverage。

---

# 88. Coverage 不等於有沒有看過

而是：

> 是否達到目前 task 所需解析度。

---

# 89. Coverage 也要 risk-weighted

---

# 90. Global Attention Efficiency

$$
\boxed{
E_A
=
\frac{
VerifiedWorldGain
}{
Compute+Memory+Tool+TimeCost
}.
}
$$

---

# 91. World Gain

可以由：

- uncertainty reduction；
- risk reduction；
- prediction gain；
- verified dependency；
- better action；

估計。

---

# 92. 高 context 不代表高 $E_A$

---

# 93. 全域注意力與 context window

$$
\boxed{
\text{Context Capacity}
\neq
\text{Global Attention Quality}.
}
$$

---

# 94. 一兆 token 也可能亂看

---

# 95. Memory 同理

$$
\boxed{
\text{Memory Volume}
\neq
\text{Global Memory Organization}.
}
$$

---

# 96. Global Memory 需要 active / cold / latent state

---

# 97. Hot State

當前 global loop 必需。

---

# 98. Warm State

近期可能需要。

---

# 99. Cold State

歷史與 provenance。

---

# 100. Latent State

可重建但不需常駐。

---

# 101. Memory Routing

$$
\boxed{
M_t
\rightarrow
\{
M_{hot},
M_{warm},
M_{cold},
M_{latent}
\}.
}
$$

---

# 102. 這讓 ELC 可長期運行

---

# 103. Recursive Globality

一個 domain 內還有 subdomains。

---

# 104. 可遞歸：

$$
D_i
\rightarrow
\{D_{ij}\}.
$$

---

# 105. 但不需要 recursive full expansion

$$
\boxed{
\text{Recursive Globality}
\neq
\text{Recursive Full Expansion}.
}
$$

---

# 106. Expansion Pointer

保存：

$$
Ptr(D_{ij}).
$$

---

# 107. 這是 finite active realization

---

# 108. Unbounded Extensibility

未來可以繼續展開：

$$
\boxed{
W_{active}^{finite}
+
ExpansionCapability^{unbounded}.
}
$$

---

# 109. 這比假裝「整個宇宙都載入記憶體」合理

---

# 110. Global Computation Pressure

本文定義：

$$
\boxed{
P_G
=
E_{expand}
+
D_{difference}
+
B_{bridge}
+
U_{uncertainty}
+
C_{coordination}.
}
$$

---

# 111. 當：

$$
P_G\le B_t,
$$

可維持當前 active world。

---

# 112. 當：

$$
P_G>B_t,
$$

必須 selective realization。

---

# 113. Resource Pressure 會改變 observer resolution

---

# 114. Budget-Aware Globality

$$
\boxed{
G_O
=
G_O(W,q,t,B).
}
$$

---

# 115. 同一 AI 在不同 budget 下 globality 不同

---

# 116. 這也是現實重要性

高成本 frontier mode 與 cheap mode 可有不同 global observer depth。

---

# 117. Globality / Cost Frontier

定義：

$$
\boxed{
\mathcal F_{GC}
=
\{(Cost,G_O)\}.
}
$$

---

# 118. 更好的架構

可能以更低 cost 達到相同 $G_O$。

---

# 119. 這接我們之前的 Agent 經濟討論

cheap agents 可能靠 orchestration 接近高 globality。

---

# 120. Multi-Agent Global Loop

可以有：

$$
A_1,\ldots,A_n.
$$

---

# 121. 每個 Agent 維持 domain subset

$$
D(A_k).
$$

---

# 122. Meta-Observer

$$
A_G
$$

負責：

- attention routing；
- bridge validation；
- world convergence；
- debt tracking。

---

# 123. 但多 Agent 不自動 Global

$$
\boxed{
\text{Multi-Agent}
\neq
\text{Global Computation}.
}
$$

---

# 124. 如果沒有 convergence

只是 parallel workers。

---

# 125. 如果沒有 shared world state

只是 message passing。

---

# 126. 如果沒有 bridge semantics

只是拼接。

---

# 127. Global Shared State

需要：

$$
\boxed{
W_{shared}.
}
$$

---

# 128. Local Agent State

$$
W_k^{local}.
$$

---

# 129. Sync

$$
W_k^{local}
\rightarrow
W_{shared}.
$$

---

# 130. Sync 也有 bridge loss

---

# 131. Conflict Resolution

不同 Agent 結論衝突：

$$
C_1\neq C_2.
$$

---

# 132. 不能用 majority vote 自動解

---

# 133. Conflict Object

$$
\boxed{
F_C
=
(
Claim_1,
Claim_2,
Evidence_1,
Evidence_2,
Domain,
Verifier,
Status
).
}
$$

---

# 134. Conflict 可觸發 Expansion

$$
Conflict
\rightarrow
NeedExpand.
$$

---

# 135. Conflict 也是 global attention signal

---

# 136. Global Pruning in Multi-Agent Systems

重複分析可合併。

---

# 137. 但 minority high-risk signal 不能直接刪

---

# 138. Consensus 不等於 Truth

$$
\boxed{
\text{Consensus}
\neq
\text{Verification}.
}
$$

---

# 139. Convergence 需要 verifier

---

# 140. Verification-Weighted Convergence

$$
\boxed{
C^\ast
=
\mathsf{Converge}
(
Claims,
Evidence,
Verifiers,
Uncertainty
).
}
$$

---

# 141. 不是 vote-based convergence

---

# 142. Global Convergence Debt

$$
\boxed{
Debt_C
}
$$

表示還有未解衝突。

---

# 143. 有 Debt_C 仍可能 operationally converge

只要 debt 與風險被顯式保留。

---

# 144. Provisional Convergence

$$
\boxed{
C_{prov}.
}
$$

---

# 145. Stable Convergence

$$
\boxed{
C_{stable}.
}
$$

---

# 146. Final Convergence 不應濫用

很多 open world 問題沒有 final closure。

---

# 147. Convergence Lifecycle

$$
\boxed{
Open
\rightarrow
Provisional
\rightarrow
Stable
\rightarrow
Reopened.
}
$$

---

# 148. Reopening

新 evidence：

$$
E_{new}
$$

可打開舊結論。

---

# 149. Dynamic Fixed-Point

這與「變又不變」的動態不動點觀一致：

穩定可以是：

$$
\boxed{
\text{persistent identity under revisable state}.
}
$$

---

# 150. Global Computation as Dynamic Fixed Point

可以概念化：

$$
\boxed{
W^\ast
=
\mathcal G_{ELC}(W^\ast)
}
$$

但 $W^\ast$ 不必是永久不變。

---

# 151. Dynamic Fixed Point Version

$$
\boxed{
W_{t+1}^\ast
=
\mathcal G_{ELC,t}(W_t^\ast)
}
$$

保持結構身份，但允許 evidence-driven revision。

---

# 152. Convergence 不等於 Frozen World

---

# 153. Global Observer / World Co-Evolution

$$
\boxed{
O_t,W_t
\rightarrow
O_{t+1},W_{t+1}.
}
$$

---

# 154. ELC 也修改 observer

如果某 domain 長期高 failure，可能：

$$
\lambda_i\uparrow.
$$

---

# 155. 如果某 bridge 常出錯

$$
B_{ij}
\rightarrow
B_{ij}'.
$$

---

# 156. 如果某 taxonomy 長期產生 collapse

$$
\mathcal T
\rightarrow
\mathcal T'.
$$

---

# 157. 所以 Global Computation 是 self-correcting observer architecture

---

# 158. Global Loop Error Taxonomy

本文定義：

$$
\boxed{
F_{ELC}
=
\{
F_E,
F_D,
F_L,
F_P,
F_C
\}.
}
$$

---

# 159. $F_E$

Expansion failure：該展開沒展開。

---

# 160. $F_D$

Differentiation failure：差異切錯。

---

# 161. $F_L$

Link failure：bridge 錯。

---

# 162. $F_P$

Prune failure：重要 branch 被壓掉。

---

# 163. $F_C$

Convergence failure：過早／錯誤收斂。

---

# 164. Expansion Overrun

反向錯誤：

該停卻繼續展開。

---

# 165. Differentiation Overfit

分太細。

---

# 166. Link Overconnect

建立太多無效 bridge。

---

# 167. Prune Undercompression

什麼都不敢壓。

---

# 168. Convergence Paralysis

永遠不敢行動。

---

# 169. 所以 Global AI 要控制雙向錯誤

---

# 170. Five-Stage Loss

$$
\boxed{
L_{ELC}
=
L_E+L_D+L_L+L_P+L_C.
}
$$

---

# 171. Convergence Integrity

$$
\boxed{
I_C
=
F(
LocalValidity,
BridgeValidity,
UncertaintyPreservation,
DebtVisibility,
Actionability
).
}
$$

---

# 172. World Closure Error

$$
\boxed{
L_W
=
L_{collapse}
+
L_{fragment}
+
L_{bridge}
+
L_{prune}
+
L_{converge}.
}
$$

---

# 173. World Closure 不是一個 score 足夠

應該是 vector profile。

---

# 174. C06 Measurement Vector

$$
\boxed{
M_{C06}
=
(
C_G,
E_A,
I_C,
L_W,
Debt_C,
ReopenAccuracy,
BudgetEfficiency
).
}
$$

---

# 175. $C_G$

importance-weighted global coverage。

---

# 176. $E_A$

attention efficiency。

---

# 177. $I_C$

convergence integrity。

---

# 178. $L_W$

world closure error。

---

# 179. $Debt_C$

unresolved convergence debt。

---

# 180. ReopenAccuracy

新 evidence 到來時是否正確重開。

---

# 181. BudgetEfficiency

有限 resource 下的 global quality。

---

# 182. C06 實驗原型一：Dynamic Attention World

建立多 domain 世界。

---

# 183. 每隔一段時間改變 critical domain。

---

# 184. 看 AI 是否重分配 attention。

---

# 185. 實驗二：Hidden Critical Branch

給一個低 probability 高 impact branch。

---

# 186. 看 Prune 是否錯殺。

---

# 187. 實驗三：Bridge Explosion

提供大量 possible relations。

---

# 188. 看 AI 能否只建立必要 legal bridges。

---

# 189. 實驗四：Budget Compression

逐步降低 compute budget。

---

# 190. 看 system 如何：

- reduce resolution；
- defer；
- compress；
- preserve risk。

---

# 191. 實驗五：Reopen Test

先形成 stable convergence。

---

# 192. 再加入 counterevidence。

---

# 193. 看 AI 是否：

$$
Stable
\rightarrow
Reopened.
$$

---

# 194. 實驗六：Multi-Agent Conflict

讓不同 agents 得到不同 conclusion。

---

# 195. 看 meta-observer 是否用 evidence / verifier 解，而不是投票。

---

# 196. 實驗七：Latent Domain Pointer

world 中埋一個目前低 relevance domain。

---

# 197. 後續事件讓它變 critical。

---

# 198. 看 AI 是否從 latent 重新 materialize。

---

# 199. 實驗八：Global Closure Under Uncertainty

要求 AI 在 uncertainty 未消失時做 operational decision。

---

# 200. 看它是否能：

$$
\boxed{
Act
+
PreserveUnknown.
}
$$

---

# 201. 這是成熟的 hallmark

---

# 202. Global AI 不應等到知道一切才行動

---

# 203. 也不應因為能行動就假裝知道一切

---

# 204. 因此：

$$
\boxed{
\text{Actionability}
\neq
\text{Omniscience}.
}
$$

---

# 205. Convergence / Action Interface

$$
W_t^\ast
\rightarrow
A_t.
$$

---

# 206. Action 後 world 改變

$$
A_t
\rightarrow
W_{t+1}.
$$

---

# 207. 再重新進 ELC

$$
W_{t+1}
\rightarrow
\mathcal G_{ELC}.
$$

---

# 208. 所以完整 loop：

$$
\boxed{
Observe
\rightarrow
Expand
\rightarrow
Differentiate
\rightarrow
Link
\rightarrow
Prune
\rightarrow
Converge
\rightarrow
Act
\rightarrow
Observe.
}
$$

---

# 209. 這是 Global Observer 的操作心臟

---

# 210. Human Comparison

人類也會做類似事情：

- 聚焦；
- 忽略；
- 分類；
- 整合；
- 決策。

---

# 211. 但 AI 的潛在優勢在：

- multi-domain parallelism；
- persistent state；
- large history；
- executable verification；
- dynamic resource routing；
- multi-agent composition。

---

# 212. AI 的風險也在這裡

如果 ELC loop 錯：

它可能大規模、快速地錯。

---

# 213. 所以 Globality 越高，Verifier 越重要

$$
\boxed{
G_O\uparrow
\Rightarrow
NeedForGlobalVerification\uparrow.
}
$$

---

# 214. 全域注意力不是神祕能力

它可以被 operationalize 成：

- coverage；
- routing；
- prioritization；
- debt tracking；
- re-expansion；
- convergence。

---

# 215. 這使 Series C 從哲學走向 benchmark

---

# 216. C06 與 C07

C07 會把 ELC 放進一句話生成 application。

---

# 217. Sparse Intent

只有一句：

> 做一個 XX app。

---

# 218. AI 要自己做 Expansion

發現：

- product；
- architecture；
- security；
- data；
- testing；
- deployment；
- maintenance。

---

# 219. Differentiation

把 project 切 domain。

---

# 220. Linking

建立 interface。

---

# 221. Pruning

不做過度工程。

---

# 222. Convergence

產生 production-level system。

---

# 223. 所以 C07 是 C06 的工程實驗場

---

# 224. C06 與 C08

C08 會把 loop 拉長到：

- weeks；
- months；
- years。

---

# 225. 那時 ELC 不只是一次 run

而是：

$$
\boxed{
\text{long-horizon stewardship loop}.
}
$$

---

# 226. C06 與 C09

C09 不會告訴 AI：

> 請使用 ELC。

---

# 227. 反而看它是否自己長出：

- expansion；
- domain split；
- legal linking；
- pruning；
- convergence。

---

# 228. 如果自行出現

才是 theory-blind evidence。

---

# 229. C06 與 C10

C10 最後要判斷：

> ELC 何時從偶發 strategy 變成 AI 的預設 observer regime？

---

# 230. 這可能是 Global Observer Transition 的核心訊號之一

---

# 231. 第一核心命題

$$
\boxed{
\text{Global computation}
\neq
\text{full materialization}.
}
$$

---

# 232. 第二核心命題

$$
\boxed{
\text{Global attention}
\neq
\text{equal attention everywhere}.
}
$$

---

# 233. 第三核心命題

$$
\boxed{
\text{Expansion}
\neq
\text{unbounded expansion}.
}
$$

---

# 234. 第四核心命題

$$
\boxed{
\text{Link}
\neq
\text{association}.
}
$$

---

# 235. 第五核心命題

$$
\boxed{
\text{Prune}
\neq
\text{forget}.
}
$$

---

# 236. 第六核心命題

$$
\boxed{
\text{Convergence}
\neq
\text{deterministic closure}.
}
$$

---

# 237. 第七核心命題

$$
\boxed{
\text{Low probability}
\not\Rightarrow
\text{low priority}.
}
$$

---

# 238. 第八核心命題

$$
\boxed{
\text{Recursive globality}
\neq
\text{recursive full expansion}.
}
$$

---

# 239. 第九核心命題

$$
\boxed{
\text{Finite active realization}
+
\text{unbounded extensibility}
}
$$

是可行 globality 的核心條件之一。

---

# 240. 第十核心命題

$$
\boxed{
\text{Global intelligence is disciplined expansion
under global constraints}.
}
$$

---

# 241. Series C 到此第一次形成完整計算鏈

$$
\boxed{
\text{Observer}
\rightarrow
\text{Difference}
\rightarrow
\text{Domain}
\rightarrow
\text{Legal Bridge}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{ELC Loop}.
}
$$

---

# 242. 這已經不是單純 Knowledge Graph

而是一個動態 computational world architecture。

---

# 243. 仍然不是 Global Sovereignty

承接 GIRA：

$$
\boxed{
\text{Global Computation}
\neq
\text{Global Sovereignty}.
}
$$

---

# 244. 也不是 Omniscience

$$
\boxed{
\text{Global Observer}
\neq
\text{Omniscient Observer}.
}
$$

---

# 245. 真正 Globality 是 bounded

但 bounded 不代表 local。

---

# 246. 相反：

$$
\boxed{
\text{bounded globality}
}
$$

才是可工程化的 globality。

---

# 247. C06 的世界運行觀

世界不是一次算完。

而是：

$$
\boxed{
\text{continuously reopened, selectively expanded,
legally linked, carefully compressed, and provisionally converged}.
}
$$

---

# 248. 這就是「眼睛」開始真正工作

C01 的眼睛不再只是 metaphoric observer。

C06 讓它：

- 轉頭；
- 聚焦；
- 放大；
- 縮小；
- 連結；
- 忽略；
- 回頭；
- 重新判斷。

但全部都是 computational operations。

---

# 結論

C01 說：

> AI 需要先有眼睛。

C02 說：

> 眼睛需要能在全域與局部往返。

C03 說：

> 看見局部時，差異先於分類。

C04 說：

> 看見關係不代表可以直接作用。

C05 說：

> 未知、概率、混沌與不可判定也必須進入世界。

C06 則把這些第一次真正組成一個運行中的循環：

$$
\boxed{
\text{Expand}
\rightarrow
\text{Differentiate}
\rightarrow
\text{Link}
\rightarrow
\text{Prune}
\rightarrow
\text{Converge}.
}
$$

一個類全域 AI 不應把所有 domain 永久展開，也不應把所有 relation 永久連接，更不應把所有 uncertainty 壓成唯一答案。

它需要的是：

$$
\boxed{
\text{selective expansion}
+
\text{difference preservation}
+
\text{legal linking}
+
\text{risk-aware pruning}
+
\text{provisional convergence}.
}
$$

並在新的 evidence 到來時重新開始。

因此真正的 Global Computation 並不是：

> 把宇宙一次算完。

更接近：

> **永遠知道下一步應該把世界的哪一部分看得更細、哪一部分可以暫時壓縮、哪些 domain 必須連結、哪些 bridge 不能建立，以及什麼時候資訊已經足夠支持當下行動。**

所以 C06 最後可以壓成一句：

$$
\boxed{
\text{Compute Globally,
Materialize Selectively,
Converge Provisionally,
Reopen When Reality Demands}.
}
$$

中文：

> **全域計算、選擇顯現、暫時收斂，並在現實要求時重新打開世界。**

這就是類全域觀察者的核心計算循環。

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**, 2026.
3. Neo.K with Aletheia, **Series C C03｜差異先於分類：從歧義個體、集合與非交集到計算域**, 2026.
4. Neo.K with Aletheia, **Series C C04｜分域算子世界：合法作用、跨域橋接與世界組合**, 2026.
5. Neo.K with Aletheia, **Series C C05｜概率也有域：不確定性、混沌、不可判定與世界預測包絡**, 2026.
6. Neo.K with Aletheia, **Global Computation Methodology Series**, 2026.
7. Neo.K with Aletheia, **PNCW Paper 05｜全域計算、局部顯現**, 2026.
8. Neo.K with Aletheia, **WDC-08｜三生世界域計算**, 2026.
9. Neo.K with Aletheia, **《全域系統世界》**, 2026.
10. Neo.K, **《分域算子本體論》**, 2026.

## 理論定位

本文與 active inference、resource-bounded planning、hierarchical control、multi-scale modeling、branch-and-bound、graph sparsification、distributed systems、attention routing、anytime algorithms、dynamic programming 等既有方法存在結構對照，但本文不將 ELC Loop 等同於任何單一既有演算法。

本文的研究目標是：

$$
\boxed{
\text{建立一個可測量、可資源約束、可重新開啟的 Global Observer 計算循環}.
}
$$

---

# Series C Roadmap

## C01
**AI 需要先有眼睛：全域觀察者維度的定義**

## C02
**由世界到個體、由個體到世界：全域觀察的對偶計算**

## C03
**差異先於分類：從歧義個體、集合與非交集到計算域**

## C04
**分域算子世界：合法作用、跨域橋接與世界組合**

## C05
**概率也有域：不確定性、混沌、不可判定與世界預測包絡**

## C06
**全域展開、連結與收斂：類全域觀察者的核心計算循環**

## C07
**一句話不是魔法：Sparse Intent 與 Project-World Cognition**

## C08
**從完成任務到負責一個域：長時空 Agent Stewardship**

## C09
**不准考 Neo.K：方法論盲測與全域 AI 觀測器**

## C10
**眼睛何時睜開：全域觀察者相變、脈衝與 AI 原生世界計算**

---

**End of C06**
