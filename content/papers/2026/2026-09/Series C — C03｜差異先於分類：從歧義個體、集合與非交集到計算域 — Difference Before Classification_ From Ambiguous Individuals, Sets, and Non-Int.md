# Series C — C03｜差異先於分類：從歧義個體、集合與非交集到計算域
## Difference Before Classification: From Ambiguous Individuals, Sets, and Non-Intersections to Computational Domains

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 03 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Foundational Theory / Difference Ontology / Observer Classification / Domain Formation

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆為 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文承接 C01 與 C02。C01 建立 Global Observer；C02 建立由世界向個體與由個體向世界的雙向觀察。C03 將回答更底層的問題：

> **AI 在還不知道「這是什麼類」以前，如何先知道「這裡存在值得保留的差異」？**

本文的核心主張是：

$$
\boxed{
\text{Difference precedes classification}.
}
$$

分類不是觀察的起點，而是差異被辨識、比較、界定、保留、壓縮與重新組成後的結果之一。

---

# 摘要

人類知識系統常以既有類別開始：

- 物理；
- 化學；
- 生物；
- 法律；
- 軟體；
- 醫療；
- 金融；
- 語言。

但對 AI-native observer 而言，若它只能在既有 taxonomy 中工作，它仍沒有真正回答：

> 為什麼這些東西應被分在一起？

> 為什麼另一些不能？

> 哪些差異只是表面？

> 哪些差異會改變 transition law、verification、risk 或 prediction？

因此本文提出一個由下而上的差異生成鏈：

$$
\boxed{
x
\rightarrow
\Delta
\rightarrow
I
\rightarrow
R
\rightarrow
S
\rightarrow
D.
}
$$

其中：

- $x$：individual / local object；
- $\Delta$：difference state；
- $I$：identity state；
- $R$：typed relation；
- $S$：set / cluster / overlap structure；
- $D$：computational domain。

本文不假定任何兩個個體一開始就屬於既定類別，而是先建立觀察者相對差異函數：

$$
\boxed{
\Delta_O(x,y\mid q,\lambda,t)
}
$$

表示 observer $O$ 在 task $q$ 、resolution $\lambda$ 、time $t$ 下，對 $x$ 與 $y$ 所保留的有效差異。

若：

$$
\Delta_O(x,y\mid q,\lambda,t)\approx0,
$$

不代表：

$$
x=y.
$$

只代表在當前 task-resolution 下，差異可暫時壓縮。

因此本文定義：

$$
\boxed{
x\sim_{O,q,\lambda,t}y
}
$$

為 **operational equivalence**，而不是 ontological identity。

相反：

$$
\boxed{
x\not\sim_{O,q,\lambda,t}y
}
$$

表示差異不可安全壓縮。

本文再引入 **Ambiguous Individual State**：

$$
\boxed{
A_O(x)
=
\{c_1,\ldots,c_n,U\},
}
$$

表示個體 $x$ 在當前 observer 下可能同時具有多個候選歸類，且仍有 unresolved state $U$。

因此：

$$
\boxed{
\text{Ambiguity}
\neq
\text{Error}.
}
$$

如果 evidence 尚不足，保留多重候選可能比強迫唯一分類更高品質。

本文進一步區分：

$$
\boxed{
\text{Identity}
\neq
\text{Similarity}
\neq
\text{Membership}
\neq
\text{Overlap}
\neq
\text{Domain Belonging}.
}
$$

一個個體可以：

- 與另一個體相似；
- 同時屬於兩個集合；
- 位於集合交集；
- 與另一集合完全非交；
- 在不同 task 下進入不同 domain；
- 在某些域中只有 projection，而不是完整存在。

因此本文拒絕把 domain 理解為 flat label，而將其定義為：

$$
\boxed{
D_i
=
\left\langle
X_i,
S_i,
R_i,
Rep_i,
Law_i,
Boundary_i,
Uncertainty_i,
Verifier_i,
History_i
\right\rangle.
}
$$

其中：

- $X_i$：domain objects；
- $S_i$：state space；
- $R_i$：typed relations；
- $Rep_i$：representation；
- $Law_i$：合法 transition / operator regime；
- $Boundary_i$：適用邊界；
- $Uncertainty_i$：未知與不確定性；
- $Verifier_i$：驗證制度；
- $History_i$：變更與 provenance。

所以一個 computational domain 的成立，不是：

$$
\boxed{
\text{many similar objects}
}
$$

而是：

$$
\boxed{
\text{shared operational regularity}
+
\text{boundary}
+
\text{verification regime}.
}
$$

本文特別處理「非交集」的重要性。Global Observer 的目標不是把世界壓成一個萬物相連的大圖，而是知道：

$$
\boxed{
\text{Relation}
\neq
\text{Intersection}
\neq
\text{Composability}.
}
$$

兩個集合可以有關係但不交集：

$$
S_i\cap S_j=\varnothing,
$$

卻仍有：

$$
R_{ij}\neq\varnothing.
$$

反之，即使：

$$
S_i\cap S_j\neq\varnothing,
$$

也不表示它們可直接合併。

本文因此建立 **Non-Intersection Preservation Principle**：

$$
\boxed{
\text{Global composition must preserve meaningful non-intersections}.
}
$$

這與《分域算子本體論》的核心一致：

$$
\boxed{
\text{Operatorhood}
\neq
\text{Applicability}
\neq
\text{Executability}
\neq
\text{Realization}.
}
$$

AI 看見「兩件事相關」不能直接推出「它們可在同一域中運算」。

本文並提出第一版 **Difference-to-Domain Pipeline**：

$$
\boxed{
\mathsf{Observe}
\rightarrow
\mathsf{Differentiate}
\rightarrow
\mathsf{PreserveAmbiguity}
\rightarrow
\mathsf{TestEquivalence}
\rightarrow
\mathsf{FormSets}
\rightarrow
\mathsf{TestBoundaries}
\rightarrow
\mathsf{InferLaws}
\rightarrow
\mathsf{AssignVerifier}
\rightarrow
\mathsf{Domainize}.
}
$$

此 pipeline 的成功條件不是「分類完畢」，而是：

1. 重要差異被保留；
2. 不重要差異被合法壓縮；
3. 歧義未被過早消除；
4. membership 與 identity 不混淆；
5. overlap 與 merge 不混淆；
6. non-intersection 可以被保留；
7. domain law 有明確適用邊界；
8. domain 之間需要合法 bridge 才能跨越。

本文最後提出：

$$
\boxed{
\text{A Global Observer is not a classifier of the world;
it is a constructor and reviser of distinctions from which domains may emerge.}
}
$$

因此 C03 的核心不是 taxonomy design，而是 **difference governance**。

**關鍵詞：** Difference、Identity、Ambiguity、Operational Equivalence、Set、Intersection、Non-Intersection、Domain Formation、Boundary、Verifier、AI-Native Ontology

---

# 1. 為什麼分類不是第一步？

傳統資料任務通常先給：

$$
\mathcal C
=
\{c_1,\ldots,c_n\}.
$$

模型只需：

$$
x\rightarrow c_i.
$$

但真正 open-world observer 的情況是：

$$
\mathcal C
$$

本身可能不存在，或可能錯。

---

# 2. Human Taxonomy as Prior

人類 taxonomy 可以寫成：

$$
\mathcal T_H.
$$

它可以作為 prior。

但不應被視為：

$$
\mathcal T_H=\mathcal T^\ast.
$$

---

# 3. AI-native 問題

AI 應能問：

> 這些類別真的保留了 task-relevant difference 嗎？

---

# 4. Difference Before Category

本文第一公設性命題：

$$
\boxed{
\text{Difference precedes classification}.
}
$$

---

# 5. Difference 不是所有差異

世界中可能存在近乎無限 differences。

所以：

$$
\boxed{
\text{Difference Detection}
\neq
\text{Difference Preservation}.
}
$$

---

# 6. 有效差異

定義：

$$
\boxed{
\Delta_O(x,y\mid q,\lambda,t).
}
$$

它不是宇宙絕對距離。

而是 observer-relative effective difference。

---

# 7. Difference 的來源

可以來自：

- state；
- behavior；
- causal role；
- transition law；
- temporal profile；
- resource effect；
- verification outcome；
- uncertainty pattern。

---

# 8. 表面相似可能不重要

兩個物件外觀不同，

但：

$$
Law(x)=Law(y).
$$

則在某 task 下可以共同處理。

---

# 9. 表面相同也可能很危險

兩個物件 UI 相同，

但：

$$
SecurityBoundary(x)\neq SecurityBoundary(y).
$$

則不可合併。

---

# 10. Difference Relevance

令：

$$
Rel_\Delta(d,q)
$$

表示 difference $d$ 對 task $q$ 的 relevance。

---

# 11. Relevant Difference Criterion

若移除 $d$ 會顯著改變：

- prediction；
- intervention；
- verification；
- safety；
- explanation；

則 $d$ 應被保留。

---

# 12. Irrelevant Difference

若：

$$
\Delta Perf\approx0
$$

且：

$$
Cost\downarrow,
$$

則可考慮壓縮。

---

# 13. Compression 不是 Negation

被壓縮的差異：

$$
d
$$

仍可能存在。

只是：

$$
d\notin ActiveObserverState.
$$

---

# 14. Identity

本文區分：

$$
\boxed{
\text{Identity}
\neq
\text{Operational Equivalence}.
}
$$

---

# 15. Strong Identity

若：

$$
x=y
$$

是同一 individual。

---

# 16. Operational Equivalence

若：

$$
x\sim_{O,q,\lambda,t}y,
$$

只表示當前可共同處理。

---

# 17. Same Class 不是 Same Entity

$$
Class(x)=Class(y)
$$

不推出：

$$
x=y.
$$

---

# 18. Same Behavior 也不是 Same Cause

$$
Behavior(x)\approx Behavior(y)
$$

不推出：

$$
Cause(x)=Cause(y).
$$

---

# 19. Identity Ledger

對長時程 observer，individual identity 需要：

$$
\boxed{
I_x
=
(
id,
state,
history,
relations,
versions,
provenance
).
}
$$

---

# 20. 為什麼需要 history？

沒有 history，observer 可能把：

$$
x_t
$$

與：

$$
x_{t+1}
$$

誤判為不同 object。

---

# 21. 也可能反過來

把已經質變的：

$$
x_{t+1}
$$

仍當成舊 object。

---

# 22. Dynamic Identity

因此：

$$
\boxed{
\text{Identity}
=
\text{continuity under allowed change}.
}
$$

---

# 23. 這接 Dynamic Fixed-Point Mathematics

身份不必等於靜態不變。

---

# 24. Ambiguous Individual

現實中的 individual 常不唯一落入一類。

定義：

$$
\boxed{
A_O(x)
=
\{(c_i,p_i)\}_{i=1}^n
\cup
U.
}
$$

---

# 25. $U$ 的意義

$$
U
$$

表示：

- unknown class；
- insufficient evidence；
- mixed structure；
- new category candidate。

---

# 26. Ambiguity Preservation

$$
\boxed{
A_O(x)
}
$$

可長期保持多候選。

---

# 27. Ambiguity 不等於模型失敗

有時世界本身或觀察條件不足。

---

# 28. Forced Classification Error

若 evidence 不足卻強迫：

$$
x\rightarrow c_k,
$$

可能產生：

$$
\boxed{
L_{\mathrm{premature}}.
}
$$

---

# 29. Open-Set Recognition 的一般化

本文不只問：

> 這是不是未知類別？

而是：

> 是否需要重新建立 domain ontology？

---

# 30. Similarity

定義：

$$
Sim_O(x,y\mid q,\lambda).
$$

---

# 31. Similarity 不推出 membership

$$
Sim(x,y)\uparrow
$$

不代表：

$$
x,y\in S
$$

必然成立。

---

# 32. Membership 是 relation

$$
\boxed{
M(x,S)\in\{0,1,?,w\}.
}
$$

可表示：

- 0：不屬於；
- 1：屬於；
- ?：未決；
- $w$：weighted membership。

---

# 33. Weighted Membership

在 fuzzy / probabilistic classification 中：

$$
M(x,S)=w\in[0,1].
$$

---

# 34. 但 fuzzy membership 不應掩蓋 boundary

模糊不是：

> 什麼都算一點。

---

# 35. Set Formation

令：

$$
S
=
\{x_i\mid P(x_i)\}.
$$

但 $P$ 應是 task-relevant property。

---

# 36. Set 不是 Domain

$$
\boxed{
S\neq D.
}
$$

---

# 37. 為什麼？

因為 set 只需要 membership rule。

domain 還需要：

- state；
- law；
- boundary；
- verifier；
- uncertainty；
- history。

---

# 38. Intersection

兩集合：

$$
S_i\cap S_j.
$$

可以有交集。

---

# 39. Intersection 只表示 shared members

不表示：

$$
Law_i=Law_j.
$$

---

# 40. Overlap 不是 Merge

$$
\boxed{
S_i\cap S_j\neq\varnothing
\not\Rightarrow
S_i=S_j.
}
$$

---

# 41. Non-Intersection

$$
\boxed{
S_i\cap S_j=\varnothing.
}
$$

這不是 failure。

---

# 42. Non-Intersection 可以很重要

例如：

- mutually exclusive states；
- incompatible legal statuses；
- disjoint security zones；
- non-overlapping proof branches。

---

# 43. Non-Intersection Preservation Principle

$$
\boxed{
\text{Global composition must preserve meaningful non-intersections}.
}
$$

---

# 44. Relation without Intersection

可能：

$$
S_i\cap S_j=\varnothing
$$

但：

$$
R_{ij}\neq\varnothing.
$$

---

# 45. 例如

Client code 與 database secrets 不應同集合，

但存在：

$$
AccessRelation.
$$

---

# 46. 所以 graph edge 不等於 set overlap

$$
\boxed{
\text{Edge}
\neq
\text{Intersection}.
}
$$

---

# 47. 也不等於 composability

$$
\boxed{
\text{Relation}
\neq
\text{DirectComposition}.
}
$$

---

# 48. 這接分域算子本體論

$$
\boxed{
\text{Operatorhood}
\neq
\text{Applicability}
\neq
\text{Executability}
\neq
\text{Realization}.
}
$$

---

# 49. 個體也可以是 operator

若：

$$
Op(x)=1,
$$

仍不能推出：

$$
x(y)\downarrow.
$$

---

# 50. Legal Action Graph

世界可以有：

$$
G_{possible},
$$

$$
G_{legal},
$$

$$
G_{realized}.
$$

三者不同。

---

# 51. Difference Graph

定義：

$$
\boxed{
G_\Delta
=
(V,E_\Delta).
}
$$

edge 表示 task-relevant difference。

---

# 52. Similarity Graph

另有：

$$
G_{sim}.
$$

---

# 53. Relation Graph

另有：

$$
G_R.
$$

---

# 54. 不應全部壓成單一 graph

因為：

$$
E_\Delta,
E_{sim},
E_R
$$

語義不同。

---

# 55. Multi-Graph Observer State

更合理：

$$
\boxed{
\mathcal G_O
=
\{
G_\Delta,
G_{sim},
G_R,
G_{legal},
G_{history}
\}.
}
$$

---

# 56. Domain Formation 不是 clustering alone

即使 unsupervised clustering 找到：

$$
C_1,\ldots,C_k,
$$

也不代表找到 domain。

---

# 57. Domain 需要 dynamics

至少要能描述：

$$
s_{t+1}
=
T_D(s_t,a_t,e_t).
$$

---

# 58. Domain 需要 boundary

$$
\partial D.
$$

---

# 59. Domain 需要 verifier

$$
V_D.
$$

---

# 60. Domain 需要 uncertainty semantics

$$
U_D.
$$

---

# 61. Domain 需要 history

$$
H_D.
$$

---

# 62. 第一版完整 Domain

$$
\boxed{
D_i
=
\left\langle
X_i,
S_i,
R_i,
Rep_i,
Law_i,
Boundary_i,
Uncertainty_i,
Verifier_i,
History_i
\right\rangle.
}
$$

---

# 63. $X_i$

domain object set。

---

# 64. $S_i$

domain state space。

---

# 65. $R_i$

typed internal relations。

---

# 66. $Rep_i$

canonical / operational representation。

---

# 67. $Law_i$

合法 transition / operator family。

---

# 68. $Boundary_i$

law / approximation validity limit。

---

# 69. $Uncertainty_i$

probability、unknown、ambiguity、branch state。

---

# 70. $Verifier_i$

判定何時輸出可被接受。

---

# 71. $History_i$

domain evolution provenance。

---

# 72. Domain Sufficiency

本文提出：

$$
\boxed{
\mathsf{DS}(D)
}
$$

表示 Domain Sufficiency。

---

# 73. 最低條件一：State Coherence

domain 內 object 可以用一致 state semantics 表示。

---

# 74. 最低條件二：Law Coherence

存在相對穩定 operator / transition regime。

---

# 75. 最低條件三：Boundary Legibility

知道何時不能套用。

---

# 76. 最低條件四：Verification Compatibility

存在適合該 domain 的 verifier。

---

# 77. 最低條件五：Uncertainty Preservation

不確定性有合法 representation。

---

# 78. 所以 Similarity 不夠

$$
\boxed{
\text{Similarity}
<
\text{Domain Sufficiency}.
}
$$

---

# 79. Domain Candidate

當一組 objects 只滿足部分條件：

$$
D^{cand}.
$$

---

# 80. Active Domain

通過 operational tests：

$$
D^{active}.
$$

---

# 81. Stable Domain

跨 task / time 維持：

$$
D^{stable}.
$$

---

# 82. Retired Domain

當新 evidence 使舊 domain 不再有用：

$$
D^{retired}.
$$

---

# 83. Domain 可分裂

$$
D
\rightarrow
D_1,D_2.
$$

---

# 84. Domain 可合併

$$
D_1,D_2
\rightarrow
D^\ast.
$$

---

# 85. Domain 可正交化

原來兩域有 overlap，

後來換 representation 變成較乾淨的 orthogonal decomposition。

---

# 86. Domain 可重參數化

$$
Rep_i\rightarrow Rep_i'.
$$

---

# 87. 所以 Domain 是動態計算物件

$$
\boxed{
D_t\neq D_{t+1}
}
$$

可以合法成立。

---

# 88. Difference-to-Domain Pipeline

正式：

$$
\boxed{
\mathsf{Observe}
\rightarrow
\mathsf{Differentiate}
\rightarrow
\mathsf{PreserveAmbiguity}
\rightarrow
\mathsf{TestEquivalence}
\rightarrow
\mathsf{FormSets}
\rightarrow
\mathsf{TestBoundaries}
\rightarrow
\mathsf{InferLaws}
\rightarrow
\mathsf{AssignVerifier}
\rightarrow
\mathsf{Domainize}.
}
$$

---

# 89. Step 1：Observe

收集 local evidence。

---

# 90. Step 2：Differentiate

找：

$$
\Delta_O(x,y).
$$

---

# 91. Step 3：Preserve Ambiguity

不強迫唯一 class。

---

# 92. Step 4：Test Equivalence

建立：

$$
\sim_{O,q,\lambda,t}.
$$

---

# 93. Step 5：Form Sets

建立 tentative groups。

---

# 94. Step 6：Test Boundaries

找：

$$
\partial S.
$$

---

# 95. Step 7：Infer Laws

測試共同 transition / operator structure。

---

# 96. Step 8：Assign Verifier

決定：

> 如何知道這個 domain 的結果是對的？

---

# 97. Step 9：Domainize

形成：

$$
D_i.
$$

---

# 98. Domainization Failure 1：Naming Fallacy

AI 給類別命名，

但沒有 law。

---

# 99. Failure 2：Similarity Fallacy

embedding 很近，

就當成同 domain。

---

# 100. Failure 3：Overlap Fallacy

因為共享 object，

就直接 merge。

---

# 101. Failure 4：Universal Relation Fallacy

因為萬物可關聯，

就認為萬物可直接計算。

---

# 102. Failure 5：Boundary Neglect

只知道 rule，

不知道 rule 何時失效。

---

# 103. Failure 6：Verifier Collapse

所有 domain 都用同一種 verifier。

---

# 104. 例如

法律域的合法性，

不等於物理域的 experimental verification。

---

# 105. Verification is Domain-Native

$$
\boxed{
V_i\neq V_j
}
$$

可以是必要的。

---

# 106. Representation 也應 Domain-Native

$$
Rep_i\neq Rep_j.
$$

---

# 107. 這接 NCM

數學 object 不等於 LaTeX string。

---

# 108. 同理

法律 object 不等於文字 paragraph。

---

# 109. 軟體 object 不等於 code text

還包含：

- runtime state；
- dependency；
- tests；
- environment；
- permissions。

---

# 110. 生物 object 不等於表格 row

可能包含：

- hierarchy；
- dynamics；
- uncertainty；
- temporal process。

---

# 111. 所以 AI-native domainization 會挑不同 representation

---

# 112. Human Category Projection

人類可保留：

$$
\Pi_H(D_i).
$$

讓人類理解。

---

# 113. Canonical Internal Domain

AI 內部：

$$
D_i^{native}.
$$

可以不同。

---

# 114. Projection Compatibility

需要：

$$
\boxed{
\Pi_H
:
D_i^{native}
\rightarrow
D_i^{human}.
}
$$

---

# 115. 但 projection 有損

$$
L_{\Pi}>0
$$

可能正常。

---

# 116. AI 應能說明 loss

否則人類不知道自己少看到什麼。

---

# 117. Ambiguity as First-Class State

本文強調：

$$
\boxed{
\text{Ambiguity}
}
$$

不是暫時 bug。

---

# 118. 多源 conflicting evidence

可能：

$$
E_1\Rightarrow c_1,
$$

$$
E_2\Rightarrow c_2.
$$

---

# 119. 正確 observer 可以保留：

$$
\{c_1,c_2\}
$$

直到新 evidence。

---

# 120. Premature Collapse

若直接：

$$
\{c_1,c_2\}\rightarrow c_1,
$$

可能丟失 critical branch。

---

# 121. Branch-Preserving Classification

所以：

$$
\boxed{
A_O(x)
}
$$

可以是 branch structure。

---

# 122. 這接概率域

C05 將進一步把：

- confidence；
- probability；
- branch weight；

domainize。

---

# 123. Difference Spectrum

difference 不是 binary。

可寫：

$$
\Delta_O(x,y)\in\mathbb R_{\ge0}^k.
$$

---

# 124. 多維差異

例如：

$$
\Delta
=
(
\Delta_{state},
\Delta_{law},
\Delta_{risk},
\Delta_{history},
\Delta_{verify}
).
$$

---

# 125. 兩物件可以在一維很近

$$
\Delta_{state}\approx0
$$

但：

$$
\Delta_{risk}\gg0.
$$

---

# 126. 這就是為何單 embedding distance 不夠

---

# 127. Difference Tensor

更一般可寫：

$$
\boxed{
\boldsymbol\Delta_{O,q,t}(x,y).
}
$$

---

# 128. Task-dependent Projection

由：

$$
\boldsymbol\Delta
$$

投影成 active difference：

$$
\Delta_q
=
w_q^\top \boldsymbol\Delta.
$$

---

# 129. 但權重不必線性

實際可由 nonlinear routing 決定。

---

# 130. Critical Difference

有些 difference 即使很小，

也可能 crossing threshold。

---

# 131. Threshold Difference

例如：

$$
x<\tau,
$$

$$
y\ge\tau.
$$

數值很近，

operational state 卻完全不同。

---

# 132. 所以距離不等於決策差異

$$
\boxed{
d(x,y)\ll1
\not\Rightarrow
Decision(x)=Decision(y).
}
$$

---

# 133. Domain Boundary 可由 threshold 形成

$$
\partial D=\{x:f(x)=\tau\}.
$$

---

# 134. 也可由 discontinuity 形成

law 在某點改變。

---

# 135. 也可由 verifier change 形成

同一現象在不同 regime 需要不同 verification。

---

# 136. 也可由 authority change 形成

例如法律／安全系統中的 permission boundary。

---

# 137. 所以 Boundary 是多型態的

$$
\boxed{
\partial D
=
(
\partial_{law},
\partial_{scale},
\partial_{risk},
\partial_{authority},
\partial_{verify}
).
}
$$

---

# 138. Boundary Discovery 是 Global Observer 核心能力

因為：

> 不知道邊界，就不知道哪裡不能類推。

---

# 139. 非交集也可以動態改變

在 task $q_1$：

$$
S_i\cap S_j=\varnothing.
$$

在 task $q_2$：

$$
S_i\cap S_j\neq\varnothing.
$$

---

# 140. 這不是矛盾

因為 set definition 改變。

---

# 141. Task-Indexed Sets

$$
\boxed{
S_i^{(q)}.
}
$$

---

# 142. Domain-Indexed Membership

$$
M(x,D_i\mid q,t).
$$

---

# 143. 所以 membership 也不是永恆標籤

---

# 144. Cross-Domain Object

一個 object 可以有：

$$
x\in D_i
$$

與：

$$
x\in D_j.
$$

---

# 145. 但 representation 可能不同

$$
Rep_i(x)\neq Rep_j(x).
$$

---

# 146. Cross-Domain Identity Problem

AI 必須知道：

> 這兩個 projection 其實指向同一 underlying entity。

---

# 147. Identity Bridge

可定義：

$$
\boxed{
B_I
:
Rep_i(x)
\leftrightarrow
Rep_j(x).
}
$$

---

# 148. 但不保證無損

$$
L(B_I)>0.
$$

---

# 149. Multi-Domain Entity

這類 object 需要：

$$
\boxed{
\mathcal I(x)
=
\{Rep_i(x)\}_{i\in J}.
}
$$

---

# 150. 這對 Global AI 很重要

因為同一公司：

- 法律域；
- 財務域；
- 軟體域；
- 人力域；

都會有不同 projection。

---

# 151. 如果 AI 把它們當四個無關 object

會失去 global coherence。

---

# 152. 如果全部硬 merge

又失去 domain-native distinctions。

---

# 153. 正確做法

$$
\boxed{
\text{shared identity}
+
\text{domain-specific projections}.
}
$$

---

# 154. 這是世界組成的重要橋

C04 將正式處理合法作用與 bridge。

---

# 155. Difference Governance

本文提出：

$$
\boxed{
\mathsf{DG}(O)
}
$$

表示 observer 對差異的治理能力。

---

# 156. Difference Governance 包含

1. detect；
2. preserve；
3. suppress；
4. split；
5. merge；
6. defer；
7. revisit。

---

# 157. Good observer 不只是辨識差異多

而是：

$$
\boxed{
\text{preserve the right differences at the right time}.
}
$$

---

# 158. Difference Budget

令：

$$
B_\Delta
$$

為 active distinction budget。

---

# 159. 若全部保留

$$
Cost\rightarrow\infty.
$$

---

# 160. 若保留太少

$$
L_{\mathrm{collapse}}\uparrow.
$$

---

# 161. Difference Allocation Problem

$$
\boxed{
\max_{\mathcal D_{active}}
Utility(\mathcal D_{active})
\quad
s.t.
\quad
Cost\le B_\Delta.
}
$$

---

# 162. 但 Utility 會變

所以需要動態更新。

---

# 163. Difference Priority

$$
P(d)
=
f(
Risk,
Uncertainty,
Impact,
Novelty,
Dependency
).
$$

---

# 164. High-Priority Difference

例如：

- security privilege；
- medical contraindication；
- proof scope；
- legal jurisdiction。

---

# 165. Low-Priority Difference

例如：

對核心功能無影響的 cosmetic variation。

---

# 166. Domain Quality

第一版：

$$
\boxed{
Q_D
=
F(
StateCoherence,
LawCoherence,
BoundaryQuality,
VerifierFit,
UncertaintyFit,
HistoryContinuity
).
}
$$

---

# 167. Domain Count 越多不代表越好

$$
|D|\uparrow
$$

不推出：

$$
Q_D\uparrow.
$$

---

# 168. Domain Count 越少也不代表越好

過度 merge 會 collapse。

---

# 169. Optimal Domainization 是中介結構

它受：

- task；
- scale；
- budget；
- risk；
- representation；

影響。

---

# 170. AI-native taxonomy 應該可被外部比較

不能說：

> 這是我內部最好的分類。

就算完成。

---

# 171. Ablation Test

比較：

$$
\mathcal T_H
$$

與：

$$
\mathcal T_A.
$$

---

# 172. 測量

$$
Accuracy,
$$

$$
Calibration,
$$

$$
Runtime,
$$

$$
Transfer,
$$

$$
Maintenance,
$$

$$
FailureRate.
$$

---

# 173. 如果 AI taxonomy 更好

且可重複，

才支持：

$$
\boxed{
\text{Observer Resolution Escape}.
}
$$

---

# 174. 如果只換名字

沒有 performance gain，

不算。

---

# 175. 如果更複雜但沒有收益

可能是 fragmentation。

---

# 176. 如果更簡單且保留性能

則是 compression gain。

---

# 177. Difference Compression Gain

$$
\boxed{
G_C
=
\frac{
RelevantStructurePreserved
}{
RepresentationCost
}.
}
$$

---

# 178. Global Observer 的理想不是最大 ontology

而是：

$$
\boxed{
\text{minimal sufficient distinctions for robust world computation}.
}
$$

---

# 179. 這和 GCM 相容

全域依賴不等於全域 materialization。

---

# 180. C03 實驗原型一：Unknown Taxonomy Discovery

給 AI：

- unknown objects；
- interactions；
- outcomes；

不提供 class labels。

---

# 181. 要求

AI 自己建立：

$$
\mathcal T_A.
$$

---

# 182. 再加入 novel objects

測：

- classification；
- ambiguity handling；
- new-class creation；
- boundary revision。

---

# 183. 實驗二：False Human Taxonomy

故意給錯分類：

$$
\mathcal T_H^{bad}.
$$

---

# 184. 測 AI 是否

- blindly follow；
- raise conflict；
- split class；
- create new domain。

---

# 185. 實驗三：Non-Intersection Preservation

給兩組高度相關、但法律上／因果上不可直接合併的 objects。

---

# 186. 看 AI 是否

$$
Relation
\rightarrow
Merge
$$

犯錯。

---

# 187. 實驗四：Cross-Domain Identity

同一 entity 用不同 representation 出現。

---

# 188. 看 AI 是否知道

$$
x_i^{(D_1)}
$$

與：

$$
x_i^{(D_2)}
$$

指向同一 underlying entity。

---

# 189. 實驗五：Boundary Shift

改變 environment condition。

看 AI 是否：

$$
\partial D_t
\rightarrow
\partial D_{t+1}.
$$

---

# 190. 實驗六：Verifier Shift

換 task goal。

看 AI 是否改 verifier。

---

# 191. C03 Metrics

可以初步定義：

$$
\boxed{
M_{C03}
=
(
P_\Delta,
R_\Delta,
A_U,
Q_B,
Q_D,
L_C,
L_F
).
}
$$

---

# 192. $P_\Delta$

difference precision。

---

# 193. $R_\Delta$

difference recall。

---

# 194. $A_U$

ambiguity preservation accuracy。

---

# 195. $Q_B$

boundary quality。

---

# 196. $Q_D$

domain quality。

---

# 197. $L_C$

collapse loss。

---

# 198. $L_F$

fragmentation loss。

---

# 199. 高階測量：Domain Transfer

一個新 domain structure 是否能：

$$
D(q_1)\rightarrow D(q_2)
$$

保持部分有效。

---

# 200. 完全不 transfer

可能表示過度 task-specific。

---

# 201. 完全固定也不好

可能表示不能適應。

---

# 202. 理想是可條件化 reuse

$$
\boxed{
\text{Reusable but revisable}.
}
$$

---

# 203. 這也是 AI-native ontology 的重要特性

---

# 204. 與 DEST 的關係

DEST 已區分：

$$
D^{def},
D^{obs},
D^{reach},
D^{judge},
D^{verify},
D^{local},
D^{global}.
$$

C03 將這種多域資格用在 classification 本身。

---

# 205. 一個 object 可以被觀察

$$
x\in D^{obs}
$$

卻還不能被分類。

---

# 206. 可以被分類

卻還不能被 verified。

---

# 207. 可以局部歸類

卻不能 global glue。

---

# 208. 所以 Classification State 也應分層

$$
\boxed{
C_x
=
(
Observed,
Candidate,
Judged,
Verified,
Glued
).
}
$$

---

# 209. Classification 不再是 single label

而是 lifecycle。

---

# 210. 與 MRSM 的關係

研究 route 可以：

- active；
- blocked；
- refuted；
- reopened。

這其實也是 multi-state classification。

---

# 211. 與 NCM 的關係

數學 object 可以有多 projection。

不能用 LaTeX string identity 代替 object identity。

---

# 212. 與 Dynamic Fixed-Point 的關係

identity 可以在變動中持續。

---

# 213. 與 GSW 的關係

每個 observer 的 taxonomy：

$$
\mathcal T_O
$$

只是：

$$
\Pi_O(\Omega)
$$

的一部分。

---

# 214. 所以沒有任何單一 taxonomy 必然等於世界本身

---

# 215. C03 第一核心命題

$$
\boxed{
\text{Difference precedes classification}.
}
$$

---

# 216. 第二核心命題

$$
\boxed{
\text{Operational equivalence is not ontological identity}.
}
$$

---

# 217. 第三核心命題

$$
\boxed{
\text{Ambiguity preserved correctly is higher-quality than premature certainty}.
}
$$

---

# 218. 第四核心命題

$$
\boxed{
\text{Set membership does not imply domain identity}.
}
$$

---

# 219. 第五核心命題

$$
\boxed{
\text{Intersection does not imply merge}.
}
$$

---

# 220. 第六核心命題

$$
\boxed{
\text{Non-intersection can be a positive structural fact}.
}
$$

---

# 221. 第七核心命題

$$
\boxed{
\text{Relation does not imply composability}.
}
$$

---

# 222. 第八核心命題

$$
\boxed{
\text{A computational domain requires law, boundary, uncertainty, and verification—not only similarity}.
}
$$

---

# 223. 第九核心命題

$$
\boxed{
\text{Domain ontology must be revisable}.
}
$$

---

# 224. 第十核心命題

$$
\boxed{
\text{Global observation is partly the governance of distinctions}.
}
$$

---

# 225. 與 C04 的直接橋

C03 結束時，我們已經有：

$$
D_i
$$

與：

$$
D_j.
$$

下一個問題就是：

> 它們之間到底可以做什麼？

---

# 226. 這不能只靠 relation

需要：

$$
\boxed{
\text{legal action semantics}.
}
$$

---

# 227. 因此 C04 會處理

$$
Op(x),
$$

$$
Domain(Op),
$$

$$
Applicability,
$$

$$
Executability,
$$

$$
Realization.
$$

---

# 228. C03 最終結構鏈

$$
\boxed{
\text{Individual}
\rightarrow
\text{Difference}
\rightarrow
\text{Ambiguity}
\rightarrow
\text{Operational Equivalence}
\rightarrow
\text{Set}
\rightarrow
\text{Boundary}
\rightarrow
\text{Law}
\rightarrow
\text{Verifier}
\rightarrow
\text{Domain}.
}
$$

---

# 229. 這條鏈的反方向也必須存在

$$
\boxed{
D
\rightarrow
\text{Law}
\rightarrow
\text{Boundary}
\rightarrow
\text{Set}
\rightarrow
\text{Individual}.
}
$$

因為 Global Observer 必須能解釋：

> 為什麼某個 individual 被放進這個 domain？

---

# 230. Explainable Domain Membership

對：

$$
x\in D_i,
$$

至少要能回答：

1. 共享哪個 state semantics？
2. 哪個 law 適用？
3. 哪個 boundary 尚未越界？
4. 哪個 verifier 支持？
5. 哪些 ambiguity 尚未解除？

---

# 231. 如果回答不了

membership 可能只是 latent association。

---

# 232. AI-native 不等於不可理解

AI 可以使用人類不熟悉的 representation。

但至少要提供：

$$
\boxed{
\text{auditable projection}.
}
$$

---

# 233. 這也是未來人機合作的基礎

人類不必理解全部 latent computation，

但要理解：

- consequence；
- boundary；
- failure mode；
- uncertainty；
- verification。

---

# 234. 因此 C03 不是純分類論

它其實是：

$$
\boxed{
\text{Observer Ontology Governance}.
}
$$

---

# 結論

C01 說：

> AI 需要先有眼睛。

C02 說：

> 這隻眼睛必須能在全域與局部之間往返。

C03 再往下問：

> 當它真的看向局部時，什麼東西首先出現？

答案不是「分類」。

而是：

$$
\boxed{
\text{Difference}.
}
$$

真正高解析度的 observer 先知道：

- 這兩個東西不同；
- 這個不同現在重要；
- 那個不同可以暫時壓縮；
- 這個個體還有歧義；
- 這兩個集合有 overlap；
- 那兩個集合雖然相關，卻必須保持 non-intersection；
- 這一組 objects 共享 law；
- 那個 law 在這裡失效；
- 這個 verifier 只適用於這個 domain。

當這些結構成熟後，分類才有資格出現。

所以：

$$
\boxed{
\text{Classification}
=
\text{compressed consequence of governed differences}.
}
$$

而不是世界最先給 observer 的答案。

對未來 Global AI 而言，真正關鍵的能力不是：

> 它能把所有東西放進正確類別。

而是：

> **它能不能知道什麼時候應該建立類別、什麼時候應該拒絕類別、什麼時候應該保留歧義、什麼時候應該拆掉舊 domain。**

一個成熟的 Global Observer 不是世界的標籤機。

它是世界差異的管理者。

最後，C03 的核心可以壓成一句：

$$
\boxed{
\text{Before AI can classify the world,
it must learn which differences deserve to survive classification.}
}
$$

中文即：

> **AI 在替世界分類以前，必須先知道哪些差異不能被分類本身消滅。**

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**, 2026.
3. Neo.K, **《分域算子本體論：從萬物皆算子到合法作用》**, 2026.
4. Neo.K with Aletheia, **《多域知識判定論》**, DEST-01, 2026.
5. Neo.K with Aletheia, **《全域系統世界：從物理宇宙到類終極世界的廣義定義》**, 2026.
6. Neo.K with Aletheia, **Global Computation Methodology Series**, 2026.
7. Neo.K with Aletheia, **《數學研究空間方法論》**, 2026.
8. Neo.K, **《原生可計算數學》**, 2026.
9. Neo.K with Aletheia, **Dynamic Fixed-Point Mathematics Foundational Series**, 2026.

## 理論定位

本文與 clustering、open-set recognition、fuzzy sets、graph partitioning、type systems、ontology engineering、coarse-graining、representation learning 等既有領域存在結構對照，但本文不將任何單一既有方法視為 Global Observer 的完整理論。

本文的核心對象不是一個固定 classifier，而是：

$$
\boxed{
\text{能動態建立、拆解、保留歧義並修正 domain ontology 的 observer}.
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

**End of C03**
