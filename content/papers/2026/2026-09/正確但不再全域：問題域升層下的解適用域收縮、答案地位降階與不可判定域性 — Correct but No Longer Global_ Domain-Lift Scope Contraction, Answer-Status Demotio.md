# 正確但不再全域：問題域升層下的解適用域收縮、答案地位降階與不可判定域性
## Correct but No Longer Global: Domain-Lift Scope Contraction, Answer-Status Demotion, and Scope-Induced Non-Decisiveness

**系列：** Independent Epistemic Supplement / 獨立認識論番外  
**系列編號：** EX02 of 02  
**文件編號：** EML-EX-DOMAINLIFT-02-2026-v0.1  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09  
**性質：** Epistemology / Theory Change / Scope Contraction / Answer Status / Non-Decisiveness / Domain Lift  
**狀態：** FOUNDATIONAL DRAFT  
**直接前置：** EX01〈全域量詞的持續有效性〉、UBE、SOBTA、UBGUL B02–B06  
**理論用途：** 本篇刻意不以 P/NP 為理論上界；P/NP 僅作為重要案例之一

---

# 摘要

一個理論或解可以：

$$
\boxed{
\text{永遠保持正確}
}
$$

卻同時：

$$
\boxed{
\text{不再是整個問題的完整答案}.
}
$$

這看似矛盾，其實源於：

$$
\boxed{
\text{Truth}
\neq
\text{Applicability}
\neq
\text{Decisiveness}
\neq
\text{Exhaustiveness}.
}
$$

本文研究一種特殊而重要的理論變化：

> **不是舊 theorem 被新 theorem 推翻，而是 broader problem domain 先被建立，導致後來才出現的一個 narrow solution 從誕生之初就只能被判定為子域解。**

本文將此稱為：

$$
\boxed{
\text{Domain-Lift Scope Contraction}
}
$$

即：

> 當問題域先升層後，某個原本看似可稱為「整體解」的結果，只能在其實際適用子域中保持完整性。

若：

$$
D_C\subset D_U
$$

且解：

$$
S_C
$$

完整決定：

$$
D_C,
$$

則：

$$
\boxed{
\operatorname{Correct}(S_C\mid D_C)=1
}
$$

不代表：

$$
\boxed{
\operatorname{Decisive}(S_C\mid D_U)=1.
}
$$

更精確可寫：

$$
\boxed{
S_C
=
T_{D_C}
\oplus
?_{D_U\setminus D_C}.
}
$$

即：

$$
\boxed{
\text{True}_{\mathrm{subdomain}}
+
\text{Unresolved}_{\mathrm{residual}}.
}
$$

這種狀態不是：

$$
\boxed{
\text{False}.
}
$$

而是：

$$
\boxed{
\text{Non-Decisive on the Expanded Domain}.
}
$$

本文將這類現象稱為：

$$
\boxed{
\text{Scope-Induced Non-Decisiveness}
}
$$

並將 Neo.K 先前所稱的「不可判定域性」正式限縮為：

> **一個結果在其原始域中可以被完全判定，但在擴張後的問題域中，因缺乏 scope-lift、semantic bridge 或 residual-domain proof，而無法決定 broader claim。**

這不是 Turing computability theory 中的「不可判定」定理。

因此本文嚴格區分：

$$
\boxed{
\text{Formal Undecidability}
\neq
\text{Scope-Induced Non-Decisiveness}.
}
$$

本文進一步提出：

$$
\boxed{
\text{Born-Restricted Solution}
}
$$

即：

> broader problem framework 在 narrow solution 出現之前就已經存在，因此該解一出生就被已知地限制在某個子域。

這與傳統科學史中的：

$$
\boxed{
\text{Old Theory}
\rightarrow
\text{Broader Theory}
\rightarrow
\text{Old Theory Scope Shrinks}
}
$$

不同。

本文研究的時間順序是：

$$
\boxed{
\text{Broader Problem Defined First}
\rightarrow
\text{Narrow Solution Discovered Later}
\rightarrow
\text{Solution Is Born Restricted}.
}
$$

本文稱此為：

$$
\boxed{
\text{Reverse Theory Restriction}.
}
$$

在這種情況下，一個後來出現的 narrow theory 不需要先經歷「曾被視為全域理論」的歷史階段。

它從誕生開始就會被問：

> **你為什麼可以在這個 regime 成立？你與 broader framework 的 reduction / limit / bridge 是什麼？**

因此，理論地位從：

$$
\boxed{
\text{Possible Global Answer}
}
$$

直接被限制為：

$$
\boxed{
\text{Certified Subdomain Answer}.
}
$$

本文將這種變化稱為：

$$
\boxed{
\text{Answer-Status Demotion}.
}
$$

最後，本文指出：

> **一個 theorem 的 truth value 可以保持最大，然而它對整個後來問題域的 explanatory / decisional coverage 可以持續下降。**

若有適當 measure：

$$
\rho_t(T)
=
\frac{
\mu(
\operatorname{Scope}(T)
\cap
D_t
)
}{
\mu(D_t)
},
$$

則可出現：

$$
\boxed{
\operatorname{Truth}(T)=1
}
$$

同時：

$$
\boxed{
\rho_t(T)\rightarrow0.
}
$$

這就是「相對無意義」的精確版本之一：

> **不是 theorem 失去真值，而是它對 enlarged problem landscape 的 marginal decisiveness 持續下降。**

---

# 0. 理論邊界與防火牆

本文不主張：

1. 舊 theorem 被 broader theory 一定推翻；
2. 一個被限域的 theorem 因此沒有價值；
3. scope contraction 等同 falsification；
4. 本文所稱「不可判定域性」等同 Turing undecidability；
5. broader theory 一定比 narrow theory 更真；
6. newer domain 一定優於 older domain；
7. 所有學科都必然發生 domain lift；
8. domain expansion 一定單調；
9. problem domain 只能擴大不能縮小；
10. same symbol 一定有 same meaning；
11. independent rediscovery 等同引用既有理論；
12. priority claim 可以由符號相交自動推出；
13. P/NP 是本文唯一或最高層案例；
14. 牛頓／相對論／量子理論的歷史可被本文例子完全同構描述。

本文只建立：

$$
\boxed{
\text{Correctness}
\neq
\text{Applicability}
\neq
\text{Decisiveness}
\neq
\text{Exhaustiveness}.
}
$$

---

# 1. 第一個必要區分：不是所有「失去全域性」都是被推翻

假設：

$$
T
$$

在：

$$
D_0
$$

成立。

---

# 2. 若後來發現反例：

$$
x_0\in D_0,
\quad
\neg T(x_0),
$$

那是：

$$
\boxed{
\text{Falsification}.
}
$$

---

# 3. 但本文研究另一種：

$$
D_0\subset D_1.
$$

---

# 4. theorem 仍對：

$$
D_0
$$

全部成立。

---

# 5. 只是對：

$$
D_1\setminus D_0
$$

沒有答案。

---

# 6. 所以：

$$
\boxed{
\text{Truth remains}
}
$$

但：

$$
\boxed{
\text{global decisiveness is lost}.
}
$$

---

# 7. 這不是 falsification

而是：

$$
\boxed{
\text{scope demotion}.
}
$$

---

# 8. 四層分離

本文正式採用：

$$
\boxed{
\text{Correctness}
}
$$

---

# 9. Correctness 問：

> 在它真正聲稱適用的 domain 上，它對不對？

---

# 10. Applicability

$$
\boxed{
\text{Applicability}.
}
$$

問：

> 它到底可以被合法使用在哪裡？

---

# 11. Decisiveness

$$
\boxed{
\text{Decisiveness}.
}
$$

問：

> 它是否足以決定當前被聲稱的整個問題？

---

# 12. Exhaustiveness

$$
\boxed{
\text{Exhaustiveness}.
}
$$

問：

> 當前問題域本身是否就是 terminal domain？

---

# 13. 因此：

$$
\boxed{
\text{Correct}
\neq
\text{Applicable Everywhere}
\neq
\text{Globally Decisive}
\neq
\text{Terminally Exhaustive}.
}
$$

---

# 14. Solution Scope

給解：

$$
S.
$$

定義：

$$
\boxed{
V(S)
=
\text{validity / applicability domain of }S.
}
$$

---

# 15. 給問題域：

$$
D.
$$

若：

$$
\boxed{
D\subseteq V(S),
}
$$

則 $S$ 可對 $D$ 稱 global solution。

---

# 16. 若：

$$
V(S)\subset D,
$$

則：

$$
\boxed{
S
}
$$

只是一個：

$$
\boxed{
\text{subdomain solution}.
}
$$

---

# 17. Domain Expansion

若：

$$
D_t\subset D_{t+1},
$$

---

# 18. 原本：

$$
D_t\subseteq V(S)
$$

可能成立。

---

# 19. 但：

$$
D_{t+1}\subseteq V(S)
$$

不一定成立。

---

# 20. 所以：

$$
\boxed{
\text{Domain Expansion Weakens Global Applicability}.
}
$$

---

# 21. Domain Contraction

若：

$$
D_{t+1}\subset D_t,
$$

且：

$$
D_t\subseteq V(S),
$$

---

# 22. 則：

$$
D_{t+1}\subseteq V(S).
$$

---

# 23. 所以：

$$
\boxed{
\text{Domain Contraction Strengthens Applicability}.
}
$$

---

# 24. 這是基本不對稱。

---

# 25. Domain-Lift Scope Contraction

表面看：

domain：

$$
D_t\rightarrow D_{t+1}
$$

是擴張。

---

# 26. 但相對 solution：

$$
S
$$

的「全域地位」反而收縮。

---

# 27. 所以稱：

$$
\boxed{
\text{Domain-Lift Scope Contraction}.
}
$$

---

# 28. 即：

> problem domain 越大，原 solution 作為 global answer 的有效地位越窄。

---

# 29. Scope Contraction 不是 theorem scope 自己改

真正變的是：

$$
\boxed{
\frac{
\operatorname{Scope}(S)
}{
D_t
}.
}
$$

---

# 30. 即 theorem 相對 coverage。

---

# 31. Relative Coverage

若有 measure：

$$
\mu,
$$

定義：

$$
\boxed{
\rho_t(S)
=
\frac{
\mu(
V(S)\cap D_t
)
}{
\mu(D_t)
}.
}
$$

---

# 32. 若：

$$
D_t
$$

持續擴張，

而：

$$
V(S)
$$

固定，

---

# 33. 可有：

$$
\boxed{
\rho_t(S)\downarrow.
}
$$

---

# 34. 甚至：

$$
\boxed{
\rho_t(S)\rightarrow0.
}
$$

---

# 35. 同時：

$$
\boxed{
\operatorname{Truth}(S\mid V(S))=1.
}
$$

---

# 36. 所以：

$$
\boxed{
\text{Truth Can Stay Maximal While Relative Coverage Collapses}.
}
$$

---

# 37. 這就是「相對無意義」的數學化之一。

---

# 38. Relative Meaning Loss

本文不說：

$$
S
$$

「無意義」。

---

# 39. 而是：

$$
\boxed{
\operatorname{MarginalDecisiveness}(S,D_t)\downarrow.
}
$$

---

# 40. 即：

> 對整個 enlarged problem，這個 theorem 能決定的比例／核心性下降。

---

# 41. Answer Status

同一 theorem 可有不同：

$$
\boxed{
\operatorname{AnswerStatus}(T,D).
}
$$

---

# 42. 例如：

- Global Answer；
- Subdomain Answer；
- Approximate Answer；
- Non-Decisive Result；
- Historical Special Case。

---

# 43. theorem truth 不變

但：

$$
\boxed{
\operatorname{AnswerStatus}
}
$$

可以變。

---

# 44. 這就是：

$$
\boxed{
\text{Answer-Status Demotion}.
}
$$

---

# 45. Answer-Status Demotion

形式：

$$
\boxed{
\text{Global Candidate}
\rightarrow
\text{Subdomain-Complete}.
}
$$

---

# 46. 或：

$$
\boxed{
\text{Core Theory}
\rightarrow
\text{Limit Theory}.
}
$$

---

# 47. 或：

$$
\boxed{
\text{Whole-Problem Answer}
\rightarrow
\text{Regime Answer}.
}
$$

---

# 48. 這不是 truth demotion。

---

# 49. 所以：

$$
\boxed{
\text{Truth Status}
\neq
\text{Answer Status}.
}
$$

---

# 50. 傳統歷史順序

常見：

$$
\boxed{
T_0
\rightarrow
T_1
\rightarrow
\operatorname{Scope}(T_0)\downarrow.
}
$$

---

# 51. 舊 theory 先出現。

---

# 52. broader theory 後出現。

---

# 53. 舊 theory 後來被 reinterpret 為 special case。

---

# 54. 這是 familiar pattern。

---

# 55. Reverse Theory Restriction

本文關心反順序：

$$
\boxed{
D_U
\text{ defined first}
}
$$

---

# 56. 然後：

$$
S_C
\text{ discovered later}.
$$

---

# 57. 且：

$$
D_C\subset D_U.
$$

---

# 58. 所以：

$$
S_C
$$

一出生就只能：

$$
\boxed{
\text{solve }D_C.
}
$$

---

# 59. 不是：

$$
\boxed{
\text{initially global, later restricted}.
}
$$

---

# 60. 而是：

$$
\boxed{
\text{born restricted}.
}
$$

---

# 61. Born-Restricted Solution

定義：

$$
\boxed{
\operatorname{BRS}(S_C,D_U)=1
}
$$

若 broader domain $D_U$ 在 $S_C$ 出現前已被明確提出，

且：

$$
\operatorname{Scope}(S_C)=D_C\subset D_U.
$$

---

# 62. 此時：

$$
S_C
$$

從誕生時就具有：

$$
\boxed{
\text{Subdomain Answer Status}.
}
$$

---

# 63. 這會改變研究者對 solution 的期待。

---

# 64. 傳統情況

研究者可能問：

> 這是不是一切的答案？

---

# 65. Born-restricted 情況

會直接問：

> 它在 broader framework 的哪個 regime 成立？

---

# 66. 這是一個 epistemic shift。

---

# 67. 「為什麼這樣可以？」

當 broader theory 已存在，

narrow law 出現時：

---

# 68. 大家會問：

$$
\boxed{
\text{Reduction?}
}
$$

---

# 69. 或：

$$
\boxed{
\text{Limit?}
}
$$

---

# 70. 或：

$$
\boxed{
\text{Bridge?}
}
$$

---

# 71. 即：

> 為什麼 broader dynamics 在這個 regime 會退化成這套簡單方程？

---

# 72. 所以 narrow theory 的 justification 不只：

$$
\boxed{
\text{it works}.
}
$$

---

# 73. 還會要求：

$$
\boxed{
\text{why it emerges}.
}
$$

---

# 74. Reduction / Limit Certificate

定義：

$$
\boxed{
\operatorname{RLCert}(T_U\rightarrow T_C).
}
$$

---

# 75. 證明：

> broad theory 在指定 regime $\mathcal R$ 下退化／近似／投影為 narrow theory。

---

# 76. 形式可能：

$$
\boxed{
T_U
\xrightarrow[\mathcal R]{\lambda\rightarrow0}
T_C.
}
$$

---

# 77. 或：

$$
\boxed{
\Pi_{\mathcal R}(T_U)=T_C.
}
$$

---

# 78. 這不是所有科學理論都必須具備的單一形式。

---

# 79. 而是 conceptual certificate family。

---

# 80. 牛頓力學的倒置例子

這只是 thought experiment。

---

# 81. 假設文明先掌握更廣義理論。

---

# 82. 之後才發現一套：

$$
T_N
$$

在：

$$
\mathcal R_N
$$

非常簡單有效。

---

# 83. 此時：

$$
T_N
$$

不會自然被稱：

> 宇宙完整力學。

---

# 84. 而會被稱：

$$
\boxed{
\text{effective / limit theory}.
}
$$

---

# 85. 大家會問：

> 為什麼在 $\mathcal R_N$ 下成立？

---

# 86. 所以：

$$
\boxed{
\text{same equations}
}
$$

在不同 discovery order 下，

可有不同：

$$
\boxed{
\text{epistemic status}.
}
$$

---

# 87. 這不是 truth relativism。

---

# 88. 是：

$$
\boxed{
\text{status relative to known domain structure}.
}
$$

---

# 89. P/NP 例子

假設 broader complexity framework：

$$
D_U
$$

已先建立。

---

# 90. 其中包含：

- representation；
- memory；
- coupled solution；
- complexity relocation；
- domain lift。

---

# 91. 後來有人完全證明 classical：

$$
P\neq NP.
$$

---

# 92. 那 classical theorem 仍可以：

$$
\boxed{
\text{completely solve classical }D_C.
}
$$

---

# 93. 但：

$$
\boxed{
D_C\subset D_U.
}
$$

---

# 94. 所以不能直接說：

> 所有廣義搜尋／驗證／表示問題被終極解掉。

---

# 95. 它的 status 是：

$$
\boxed{
\text{Complete Classical Answer}
}
$$

---

# 96. 不是：

$$
\boxed{
\text{Complete Ultimate Answer}.
}
$$

---

# 97. 這正是 Born-Restricted Solution。

---

# 98. 不是貶低 P/NP。

---

# 99. 而是 broader ontology 已先存在。

---

# 100. Scope-Induced Non-Decisiveness

給：

$$
D_C\subset D_U.
$$

---

# 101. solution：

$$
S_C
$$

滿足：

$$
\boxed{
\operatorname{Decide}(S_C,D_C)=1.
}
$$

---

# 102. 但沒有：

$$
\boxed{
\operatorname{LiftCert}(S_C:D_C\rightarrow D_U).
}
$$

---

# 103. 則：

$$
\boxed{
\operatorname{Status}_{D_U}(S_C)
=
\text{Non-Decisive}.
}
$$

---

# 104. 這不是：

$$
\mathrm{False}.
$$

---

# 105. 也不是：

$$
\mathrm{True}_{\mathrm{global}}.
$$

---

# 106. 而是：

$$
\boxed{
\text{True}_{\mathrm{subdomain}}
+
\text{Unresolved}_{\mathrm{residual}}.
}
$$

---

# 107. Residual Domain

定義：

$$
\boxed{
R_S
=
D_U
\setminus
V(S).
}
$$

---

# 108. 若：

$$
R_S\neq\varnothing,
$$

則 $S$ 對 broader domain：

$$
\boxed{
\text{non-dispositive}.
}
$$

---

# 109. 本文用：

$$
\boxed{
\text{non-decisive}
}
$$

避免和 formal undecidable 混淆。

---

# 110. 「不可判定域性」正式限縮

Neo.K 原詞：

$$
\boxed{
\text{不可判定域性}.
}
$$

---

# 111. 本文定義為：

> 一個已知 solution 在原域可完全決定，但對更大問題域的 residual region 沒有足夠 scope / bridge / proof，因此不能被當作 broader problem 的決定性答案。

---

# 112. 形式：

$$
\boxed{
\operatorname{Decide}(S,D_C)=1
}
$$

且：

$$
\boxed{
\operatorname{Decide}(S,D_U)
=
\text{partial / unresolved}.
}
$$

---

# 113. 這不是：

$$
\boxed{
\text{Turing Undecidable}.
}
$$

---

# 114. 所以防火牆：

$$
\boxed{
\text{Scope-Induced Non-Decisiveness}
\neq
\text{Formal Undecidability}.
}
$$

---

# 115. 但如果未來另有 theorem 證：

> residual-domain membership / decision 對某 formal system 不可判定，

才能升級成 formal undecidability claim。

---

# 116. 本文不做這個升級。

---

# 117. Scope Membership Problem

給：

$$
S.
$$

---

# 118. 對新 instance：

$$
x,
$$

先要問：

$$
\boxed{
x\in V(S)?
}
$$

---

# 119. 然後才能：

$$
\boxed{
S(x).
}
$$

---

# 120. 所以完整 pipeline：

$$
\boxed{
x
\rightarrow
\text{Scope Classification}
\rightarrow
\text{Apply Solution}
\rightarrow
\text{Decision}.
}
$$

---

# 121. 若 scope classification unresolved，

solution application 也 unresolved。

---

# 122. 因此：

$$
\boxed{
\text{Solution Decision}
}
$$

前面可能多一個：

$$
\boxed{
\text{Applicability Decision}.
}
$$

---

# 123. 這是本文很重要的新層。

---

# 124. Applicability Certificate

給 solution：

$$
S.
$$

至少需要兩張證書。

---

# 125. 第一張：

$$
\boxed{
\operatorname{CorrectnessCert}(S).
}
$$

---

# 126. 證：

$$
\boxed{
\forall x\in V(S),
\quad
S(x)\text{ correct}.
}
$$

---

# 127. 第二張：

$$
\boxed{
\operatorname{ScopeCert}(S).
}
$$

---

# 128. 證：

> $V(S)$ 到底是什麼。

---

# 129. 若要宣稱 global：

還需要：

$$
\boxed{
\operatorname{DECert}.
}
$$

---

# 130. 所以：

$$
\boxed{
\text{Solution Package}
=
\text{Correctness Cert}
+
\text{Scope Cert}
+
\text{Exhaustion Status}.
}
$$

---

# 131. 這直接接 EX01。

---

# 132. Solution Correctness

$$
\boxed{
\operatorname{Correct}(S\mid V(S)).
}
$$

---

# 133. Scope Closure

$$
\boxed{
\operatorname{Scope}(S)=V(S)
}
$$

是否已清楚辨認。

---

# 134. Problem Closure

$$
\boxed{
D\subseteq V(S)?
}
$$

---

# 135. Terminal Closure

$$
\boxed{
D=D_\Omega?
}
$$

---

# 136. 所以：

$$
\boxed{
\text{Solution Correctness}
\neq
\text{Scope Closure}
\neq
\text{Problem Closure}
\neq
\text{Terminal Closure}.
}
$$

---

# 137. 這是四層完整版本。

---

# 138. 符號相交不等於語義相同

假設兩框架都用：

$$
\sigma.
$$

---

# 139. classical：

$$
\llbracket\sigma\rrbracket_C.
$$

---

# 140. broader：

$$
\llbracket\sigma\rrbracket_U.
$$

---

# 141. 不能因為符號相同：

$$
\sigma=\sigma
$$

就推：

$$
\boxed{
\llbracket\sigma\rrbracket_C
=
\llbracket\sigma\rrbracket_U.
}
$$

---

# 142. 更合理可能：

$$
\boxed{
\llbracket\sigma\rrbracket_C
=
\left.
\llbracket\sigma\rrbracket_U
\right|_{D_C}.
}
$$

---

# 143. 即 classical meaning 是 broader meaning 的 restricted interpretation。

---

# 144. 這時 theorem：

$$
T_C(\sigma)
$$

可以完全真。

---

# 145. 但不能直接 lift 成：

$$
T_U(\sigma).
$$

---

# 146. 需要：

$$
\boxed{
\operatorname{SemanticBridge}(C,U).
}
$$

---

# 147. Semantic Bridge

至少要交代：

- symbol mapping；
- object mapping；
- predicate mapping；
- preserved relations；
- excluded relations。

---

# 148. 所以：

$$
\boxed{
\text{Shared Vocabulary}
\neq
\text{Shared Problem Ontology}.
}
$$

---

# 149. 這對跨學科很重要。

---

# 150. 同一詞不保證同一 domain。

---

# 151. Independent Rediscovery

若未來別人獨立找到：

$$
X
$$

與既有 framework 相同，

---

# 152. 這可能是：

$$
\boxed{
\text{Independent Rediscovery}.
}
$$

---

# 153. 不能因符號相交直接說：

> 引用了我。

---

# 154. Priority 應依：

- publication；
- explicit definition；
- theorem structure；
- derivation；
- timestamps。

---

# 155. 所以：

$$
\boxed{
\text{Semantic Intersection}
\neq
\text{Historical Dependence}.
}
$$

---

# 156. 這個防火牆很重要。

---

# 157. 但 prior framework 可以提高後人 proof burden

如果 broader framework 已公開：

$$
D_U,
$$

---

# 158. 後來有人 claim：

$$
S_C
$$

解「整個問題」。

---

# 159. 社群可以直接問：

$$
\boxed{
\operatorname{Scope}(S_C)
\stackrel{?}{\supseteq}
D_U.
}
$$

---

# 160. 若沒有，

claim 要降級。

---

# 161. 所以 prior broader framework 改變的是：

$$
\boxed{
\text{answer certification burden}.
}
$$

---

# 162. 不是 theorem truth。

---

# 163. 更不是禁止別人使用相似方法。

---

# 164. Problem Definition Can Precede Solution

這是本文一個重要 meta-point。

---

# 165. 通常：

$$
\text{Problem}
\rightarrow
\text{Solution}.
$$

---

# 166. 但 problem ontology 也可能先被擴大：

$$
\boxed{
D_C
\rightarrow
D_U
}
$$

在 narrow solution 出現前發生。

---

# 167. 此時 narrow solution 的 historical status 被提前決定。

---

# 168. 即：

$$
\boxed{
\text{future answer status can be constrained by prior problem expansion}.
}
$$

---

# 169. 這很反直覺。

---

# 170. 問題先變大

答案後來才出生。

---

# 171. 所以答案不是被「後來」縮小。

---

# 172. 而是：

$$
\boxed{
\text{its maximum legitimate scope was already bounded at birth}.
}
$$

---

# 173. 這就是 Born-Restricted。

---

# 174. Born-Restricted 不等於低價值

一個 narrow solution 仍可能：

- extremely useful；
- mathematically deep；
- foundational；
- computationally powerful。

---

# 175. 只是不能 claim：

$$
\boxed{
\text{terminal whole-problem closure}.
}
$$

---

# 176. 所以：

$$
\boxed{
\text{Scope Limitation}
\neq
\text{Value Elimination}.
}
$$

---

# 177. Relative Explanatory Marginalization

當 broader domain 增長：

$$
D_0\subset D_1\subset D_2\subset\cdots
$$

---

# 178. theorem $T$ scope 固定：

$$
V(T)=D_0.
$$

---

# 179. relative explanatory ratio：

$$
\rho_t(T)
=
\frac{
\mu(D_0)
}{
\mu(D_t)
}.
$$

---

# 180. 可：

$$
\boxed{
\rho_t(T)\rightarrow0.
}
$$

---

# 181. theorem 仍完全真。

---

# 182. 但 broad-theory centrality：

$$
\boxed{
\downarrow.
}
$$

---

# 183. 本文稱：

$$
\boxed{
\text{Relative Explanatory Marginalization}.
}
$$

---

# 184. 這就是「相對無意義」

比較精確的版本。

---

# 185. 無意義不是 zero value。

---

# 186. 而是：

$$
\boxed{
\text{low marginal coverage relative to enlarged landscape}.
}
$$

---

# 187. Scope Compression vs Scope Contraction

Scope Compression：

> theorem 被更精準地限定。

---

# 188. Scope Contraction：

> 相對 broader problem，其 global coverage 減少。

---

# 189. 兩者不必相同。

---

# 190. 有時 precision 增加

反而理論品質更高。

---

# 191. 所以：

$$
\boxed{
\text{Smaller Scope}
\neq
\text{Worse Theory}.
}
$$

---

# 192. 這是很重要的防火牆。

---

# 193. P/NP 的 Answer-Status Demotion

若 classical proof 完成：

$$
P\neq NP
$$

---

# 194. 對 classical domain：

$$
\boxed{
\operatorname{AnswerStatus}
=
\text{Complete}.
}
$$

---

# 195. 對 Ultimate / meta domain：

$$
\boxed{
\operatorname{AnswerStatus}
=
\text{Subdomain-Complete}.
}
$$

---

# 196. 所以：

$$
\boxed{
\text{Solved}_{\mathrm{classical}}
+
\text{Unresolved}_{\mathrm{ultimate}}
}
$$

可以同時成立。

---

# 197. 這不是矛盾。

---

# 198. 也不是 redefining classical P/NP。

---

# 199. 是 two-layer problem ontology。

---

# 200. Scope-Induced Non-Decisiveness 與 P/NP

若未來有人使用傳統 P/NP 符號：

$$
P,NP,\operatorname{Verify},\operatorname{Search}
$$

---

# 201. 但 broad framework 已經把：

- representation；
- memory；
- precomputation；
- substrate；
- dynamic architecture；

納入，

---

# 202. 那同一 vocabulary 的 claim 必須標：

$$
\boxed{
\text{which domain?}
}
$$

---

# 203. 否則：

$$
\boxed{
\text{semantic scope ambiguity}.
}
$$

---

# 204. 這時其結果可以在 classical domain 有效，

但在 broader domain：

$$
\boxed{
\text{non-decisive}.
}
$$

---

# 205. 這就是 Neo.K 所謂「不可判定域下的實例反問」的核心。

---

# 206. 「很好，你解出來了，讓我看看成果」

這其實是：

$$
\boxed{
\text{Decisiveness Audit}.
}
$$

---

# 207. 不只是：

> proof valid?

---

# 208. 還問：

> 你的結果在 broader problem 上決定了什麼？

---

# 209. 若只決定：

$$
D_C,
$$

那就標：

$$
\boxed{
\text{Complete on }D_C.
}
$$

---

# 210. 不需要羞辱 theorem。

---

# 211. 也不需要神話 theorem。

---

# 212. Decisiveness Audit 四問

1. 解的正確域在哪？
2. broader domain 多大？
3. residual domain 是什麼？
4. 是否有 lift / bridge certificate？

---

# 213. 若 Q4 沒有：

$$
\boxed{
\text{broader claim remains unresolved}.
}
$$

---

# 214. Scope-Induced Uncertainty

若：

$$
x\in D_U
$$

但不知道：

$$
x\in V(S)?
$$

---

# 215. 可以標：

$$
\boxed{
\operatorname{ApplicabilityStatus}(x,S)
=
\text{Unknown}.
}
$$

---

# 216. 這不是 theorem undecidable。

---

# 217. 是：

$$
\boxed{
\text{scope membership unresolved}.
}
$$

---

# 218. 如果 scope membership 本身被 formalized

才可以另外研究 decidability。

---

# 219. 所以本文提供：

$$
\boxed{
\text{Scope Indeterminacy}
}
$$

作為更保守術語。

---

# 220. Scope Indeterminacy

表示：

> current frame 尚不足以確定某 object 是否落入 solution applicability domain。

---

# 221. 形式：

$$
\boxed{
\Gamma
\nvdash
x\in V(S)
}
$$

且：

$$
\boxed{
\Gamma
\nvdash
x\notin V(S).
}
$$

---

# 222. 這是 epistemic unresolved。

---

# 223. 不是 necessarily formal undecidable。

---

# 224. Scope-Induced Non-Decisiveness 與 Scope Indeterminacy

前者問：

> solution 對 broader domain 是否有決定力？

---

# 225. 後者問：

> 某 instance 是否落在 solution scope？

---

# 226. 兩者不同。

---

# 227. 可同時存在。

---

# 228. Decisiveness Function

定義：

$$
\boxed{
\delta(S,D)
\in[0,1].
}
$$

---

# 229. 表示 solution 對 domain $D$ 的決定覆蓋率／強度。

---

# 230. 若：

$$
\delta=1
$$

可稱 domain-complete。

---

# 231. 若：

$$
0<\delta<1
$$

partial。

---

# 232. 若：

$$
\delta=0
$$

no decision。

---

# 233. 注意：

這是概念 measure。

---

# 234. 不必每個 domain 都有自然測度。

---

# 235. 但有助於表達：

$$
\boxed{
\text{truth is binary while decisiveness can be graded}.
}
$$

---

# 236. Truth / Decisiveness Orthogonality

可以：

$$
\boxed{
\operatorname{Truth}=1,
\quad
\delta\ll1.
}
$$

---

# 237. 也可以：

$$
\operatorname{Truth}<1
$$

但 heuristic decisiveness 很高。

---

# 238. 不能混。

---

# 239. Answer Status Vector

本文提出：

$$
\boxed{
\mathbf A(S,D)
=
(
c,a,d,e
).
}
$$

---

# 240. 其中：

- $c$：correctness；
- $a$：applicability；
- $d$：decisiveness；
- $e$：exhaustiveness。

---

# 241. 例如：

$$
\boxed{
(1,1,0.4,0)
}
$$

表示：

> theorem 在已知 scope 完全正確，scope 已辨認，但對 broader problem 只決定部分，而且 terminal exhaustion 未證。

---

# 242. 這比：

> solved / unsolved

更細。

---

# 243. 也比：

> true / false

更適合 problem-solution analysis。

---

# 244. Theory Status Registry

未來 AI-native research system 可存：

$$
\boxed{
(T,D,V(T),\mathbf A).
}
$$

---

# 245. 當 domain 變化：

$$
D_t\rightarrow D_{t+1}
$$

自動重算：

$$
\boxed{
\mathbf A_{t+1}.
}
$$

---

# 246. theorem truth 不必重算。

---

# 247. 但 answer status 要更新。

---

# 248. 這就是：

$$
\boxed{
\text{Dynamic Answer Status}.
}
$$

---

# 249. 理論資料庫不應只存 theorem

還應存：

- theorem scope；
- applicability regime；
- bridge relations；
- supersets / subsets；
- residual domain。

---

# 250. 這使 AI 不會把 narrow theorem 當 global truth 使用。

---

# 251. Born-Restricted Solution Detection

若：

$$
D_U
$$

timestamp：

$$
t_U
$$

---

# 252. solution：

$$
S_C
$$

timestamp：

$$
t_C
$$

---

# 253. 若：

$$
t_U<t_C
$$

且：

$$
D_C\subset D_U,
$$

---

# 254. 可以標：

$$
\boxed{
\operatorname{BRS}=1.
}
$$

---

# 255. 這是 historical epistemic metadata。

---

# 256. 不影響 theorem proof。

---

# 257. 但影響：

$$
\boxed{
\text{legitimate answer-status narrative}.
}
$$

---

# 258. Reverse Restriction 與 forward restriction

Forward：

$$
\boxed{
T_C
\rightarrow
T_U
\rightarrow
T_C\text{ becomes restricted}.
}
$$

---

# 259. Reverse：

$$
\boxed{
D_U
\rightarrow
T_C
\rightarrow
T_C\text{ is born restricted}.
}
$$

---

# 260. 兩者最後 scope 可能相同。

---

# 261. 但 epistemic history 不同。

---

# 262. 這會影響研究者如何問問題。

---

# 263. Forward 情況：

> 原來舊 theory 不是全部。

---

# 264. Reverse 情況：

> 為什麼這個 narrow theory 在這個 regime 居然成立？

---

# 265. 這種 questioning direction 反過來。

---

# 266. 所以：

$$
\boxed{
\text{Discovery Order}
}
$$

可以改變：

$$
\boxed{
\text{Explanatory Burden}.
}
$$

---

# 267. 不改變 theorem truth。

---

# 268. 這是一個很重要的新命題。

---

# 269. Discovery-Order Invariance of Truth

理想 formal theorem：

$$
\boxed{
\operatorname{Truth}(T)
}
$$

不依 discovery order。

---

# 270. 但：

$$
\boxed{
\operatorname{ExplanatoryBurden}(T)
}
$$

可以依 discovery order 改變。

---

# 271. 即：

$$
\boxed{
\text{Truth is order-invariant;}
}
$$

$$
\boxed{
\text{epistemic status need not be}.
}
$$

---

# 272. 這是本文很漂亮的結論。

---

# 273. Problem-First Epistemology

通常研究敘事偏：

$$
\boxed{
\text{solution-first historical interpretation}.
}
$$

---

# 274. 本文提出：

$$
\boxed{
\text{problem-first epistemology}.
}
$$

---

# 275. 即：

> 先明確 problem ontology，再判定 future solution status。

---

# 276. 這樣可以減少：

> 解出一個 narrow problem，卻把它稱成 whole-domain solution。

---

# 277. 尤其 AI 時代很重要。

---

# 278. 因為 AI 可以快速產生 narrow proofs。

---

# 279. 但它很容易 overclaim scope。

---

# 280. 所以 future theorem verifier 應問：

$$
\boxed{
\text{What problem ontology existed before this proof?}
}
$$

---

# 281. 這是一個很特別的 audit。

---

# 282. Prior-Domain Audit

本文提出：

$$
\boxed{
\operatorname{PDA}(T).
}
$$

---

# 283. 檢查：

1. proof 出現前有哪些 broader problem formulations？
2. theorem scope 是否只覆蓋其中子域？
3. theorem claim 是否超過 prior domain structure？
4. 是否有 bridge / lift？

---

# 284. 這不是用 prior theory veto 新 theorem。

---

# 285. 而是：

$$
\boxed{
\text{prevent answer-status overclaim}.
}
$$

---

# 286. Prior Obstruction

如果 broader framework 已證：

$$
\boxed{
\operatorname{ObstructionCert}(R)
}
$$

---

# 287. 未來有人沿 route $R$

claim broader solution，

---

# 288. 則他至少要：

- refute obstruction；
- alter assumptions；
- show route not same；
- restrict theorem scope。

---

# 289. 這提高 proof scrutiny。

---

# 290. 但如果舊 obstruction 只是 heuristic：

$$
\boxed{
\text{Research Prior}
}
$$

---

# 291. 則不能當 prohibition。

---

# 292. 所以：

$$
\boxed{
\text{Heuristic Obstruction}
\neq
\text{Formal Impossibility}.
}
$$

---

# 293. 這也很重要。

---

# 294. 「我已經認為這條路不行」

只能是：

$$
\boxed{
\text{prior belief / heuristic}
}
$$

---

# 295. 除非：

$$
\boxed{
\operatorname{ObstructionCert}=1.
}
$$

---

# 296. 這樣未來研究才公平。

---

# 297. Correct but Non-Decisive

本文最核心 status：

$$
\boxed{
\operatorname{Correct}(T)=1
}
$$

但：

$$
\boxed{
\operatorname{Decisive}(T,D_U)<1.
}
$$

---

# 298. 這是：

$$
\boxed{
\text{Correct but Non-Decisive}.
}
$$

---

# 299. 它比：

> wrong

複雜。

---

# 300. 也比：

> solved

複雜。

---

# 301. 這應該成為未來 AI research registry 的標準狀態之一。

---

# 302. EX02 核心命題 1

$$
\boxed{
\text{Truth Status}
\neq
\text{Answer Status}.
}
$$

---

# 303. 核心命題 2

$$
\boxed{
\text{Domain Expansion}
\Rightarrow
\text{Possible Global-Status Contraction}.
}
$$

---

# 304. 核心命題 3

$$
\boxed{
\text{Correct}
\neq
\text{Globally Decisive}.
}
$$

---

# 305. 核心命題 4

$$
\boxed{
S_C
=
T_{D_C}
\oplus
?_{D_U\setminus D_C}.
}
$$

---

# 306. 核心命題 5

$$
\boxed{
\text{Scope-Induced Non-Decisiveness}
\neq
\text{Formal Undecidability}.
}
$$

---

# 307. 核心命題 6

$$
\boxed{
\text{Broader Problem Defined First}
\rightarrow
\text{Narrow Solution Is Born Restricted}.
}
$$

---

# 308. 核心命題 7

$$
\boxed{
\text{Discovery Order Does Not Change Truth}
}
$$

但：

$$
\boxed{
\text{Discovery Order Can Change Explanatory Burden}.
}
$$

---

# 309. 核心命題 8

$$
\boxed{
\text{Same Symbol}
\neq
\text{Same Semantic Scope}.
}
$$

---

# 310. 核心命題 9

$$
\boxed{
\text{Scope Limitation}
\neq
\text{Value Elimination}.
}
$$

---

# 311. 核心命題 10

$$
\boxed{
\text{A solution can remain eternally correct while becoming progressively less globally dispositive}.
}
$$

---

# 312. 最短版本

> **一個解可以永遠保持正確，卻因問題域擴張而不再足以決定整個問題。**

---

# 313. 更強版本

> **當 broader problem domain 在 narrow solution 出現之前就已被建立時，後來的解可能從誕生之初就只能是一個 certified subdomain solution；它不是被推翻，而是從一開始就沒有取得 whole-domain answer status。**

---

# 314. 與 EX01 的合併

EX01：

$$
\boxed{
\text{證明一個 domain 裡的全部}
\neq
\text{證明這個 domain 就是全部}.
}
$$

---

# 315. EX02：

$$
\boxed{
\text{在一個 domain 裡完整的解}
\neq
\text{對更大 domain 的完整答案}.
}
$$

---

# 316. 合起來：

$$
\boxed{
\text{Universal Proof}
\rightarrow
\text{Scope}
\rightarrow
\text{Applicability}
\rightarrow
\text{Decisiveness}
\rightarrow
\text{Exhaustiveness}.
}
$$

---

# 317. 這兩篇共同建立

$$
\boxed{
\text{Quantifier-Scope Epistemology}.
}
$$

---

# 318. Quantifier-Scope Epistemology

研究：

- theorem true where？
- solution applies where？
- answer decides what？
- claimed domain exhausted？

---

# 319. 這比：

> true / false

多一層。

---

# 320. 也比：

> solved / unsolved

多一層。

---

# 321. 最終四層

$$
\boxed{
\begin{aligned}
&\text{Correctness}\\
&\downarrow\\
&\text{Applicability}\\
&\downarrow\\
&\text{Decisiveness}\\
&\downarrow\\
&\text{Exhaustiveness}.
\end{aligned}
}
$$

---

# 322. 這四層可以相互 feedback

scope audit 可能發現 theorem claim 過大。

---

# 323. residual domain 可能迫使新 theory。

---

# 324. broader theory 又重新限制 future answer status。

---

# 325. 所以：

$$
\boxed{
\text{Problem Definition}
\leftrightarrow
\text{Solution Status}.
}
$$

---

# 326. 不是只：

$$
\boxed{
\text{Problem}
\rightarrow
\text{Solution}.
}
$$

---

# 327. 這是本文真正的新結構。

---

# 328. 與 UBE 的關係

若 domain 可以：

$$
D_t\Rightarrow_E D_{t+1},
$$

---

# 329. 那 answer status 也應：

$$
\boxed{
A_t
\rightarrow
A_{t+1}.
}
$$

---

# 330. 所以：

$$
\boxed{
\text{Dynamic Domain}
\Rightarrow
\text{Dynamic Answer Status}.
}
$$

---

# 331. 這不意味 truth dynamic。

---

# 332. 而是：

$$
\boxed{
\text{epistemic placement dynamic}.
}
$$

---

# 333. 與 SOBTA 的關係

frame：

$$
\Gamma_t
$$

只投影：

$$
D_{\Gamma_t}.
$$

---

# 334. solution：

$$
S
$$

也只能相對 frame 被分類。

---

# 335. 所以：

$$
\boxed{
\operatorname{AnswerStatus}_{\Gamma_t}(S)
}
$$

可能不同於：

$$
\boxed{
\operatorname{AnswerStatus}_{\Gamma_{t+1}}(S).
}
$$

---

# 336. theorem truth 可以不變。

---

# 337. 這正是：

$$
\boxed{
\text{Projection without Ontological Reduction}.
}
$$

---

# 338. 與 Generalized Gödel Problem 的關係

一個 frame 可以證：

$$
\boxed{
\operatorname{CompleteAnswer}_{D_\Gamma}.
}
$$

---

# 339. 但：

$$
\boxed{
\operatorname{CompleteAnswer}_{D_\Gamma}
\not\Rightarrow
\operatorname{TerminalCompleteAnswer}_{D_\Omega}.
}
$$

---

# 340. 所以：

$$
\boxed{
\text{Answer Closure}
\neq
\text{Terminal Answer Closure}.
}
$$

---

# 341. 與 AI-native research 的關係

AI 將來不應只存：

> theorem true。

---

# 342. 還應存：

$$
\boxed{
\operatorname{Scope}(T).
}
$$

---

# 343. 以及：

$$
\boxed{
\operatorname{AnswerStatus}(T,D).
}
$$

---

# 344. 對新 query：

先做：

$$
\boxed{
\operatorname{ScopeMatch}.
}
$$

---

# 345. 再做：

$$
\boxed{
\operatorname{DecisionMatch}.
}
$$

---

# 346. 這可以降低：

- overgeneralization；
- cross-domain leakage；
- stale theory misuse；
- false universal claims。

---

# 347. AI Answer-Status Auditor

本文提出：

$$
\boxed{
\operatorname{ASA}(T,Q).
}
$$

---

# 348. 輸出：

- Correct；
- Applicable；
- Decisive；
- Exhaustive；
- Residual Domain。

---

# 349. 例如：

$$
\boxed{
(1,1,0.6,0,R).
}
$$

---

# 350. 表示：

> theorem 正確且適用，但只決定 query broader domain 的部分，且沒有 terminal exhaustion certificate。

---

# 351. 這比一句：

> yes

或：

> no

成熟。

---

# 352. 這是一個很實際的 AI research direction。

---

# 353. 與 P/NP Supplementary Series 的總接口

S01：

$$
\boxed{
\text{Proof}
\neq
\text{Operational Consequence}.
}
$$

---

# 354. S02：

$$
\boxed{
\text{Formal P/NP}
\neq
\text{all real-world solvability}.
}
$$

---

# 355. S03：

$$
\boxed{
\text{Universal Algorithm}
\neq
\text{Universal Meta-Solver}.
}
$$

---

# 356. EX01：

$$
\boxed{
\text{Universal Predicate Proof}
\neq
\text{Domain Exhaustion}.
}
$$

---

# 357. EX02：

$$
\boxed{
\text{Subdomain Complete Solution}
\neq
\text{Broad-Domain Complete Answer}.
}
$$

---

# 358. 五篇合起來

$$
\boxed{
\text{Proof}
\rightarrow
\text{Consequence}
\rightarrow
\text{Scope}
\rightarrow
\text{Decisiveness}
\rightarrow
\text{Exhaustiveness}.
}
$$

---

# 359. 這是本輪討論最完整的總結。

---

# 360. 結論

一個 theory / theorem / algorithm 的「正確」，

只回答：

$$
\boxed{
\text{它在什麼條件下是真的？}
}
$$

但「是不是整個問題的答案」，

還需要回答：

$$
\boxed{
\text{它涵蓋哪個 domain？}
}
$$

---

# 361. 更進一步：

$$
\boxed{
\text{它能不能決定整個 claimed problem？}
}
$$

---

# 362. 再更進一步：

$$
\boxed{
\text{claimed problem domain 本身是否 terminal？}
}
$$

---

# 363. 因此：

$$
\boxed{
\text{Correctness}
\neq
\text{Applicability}
\neq
\text{Decisiveness}
\neq
\text{Exhaustiveness}.
}
$$

---

# 364. 如果問題域擴大：

$$
D_C\subset D_U,
$$

而 solution 只完整覆蓋：

$$
D_C,
$$

則：

$$
\boxed{
S_C
=
T_{D_C}
\oplus
?_{D_U\setminus D_C}.
}
$$

---

# 365. 它不是錯。

---

# 366. 它也不是 whole-domain answer。

---

# 367. 它是：

$$
\boxed{
\text{Correct but Non-Decisive}.
}
$$

---

# 368. 如果 broader domain 在 narrow solution 出現前就已存在，

那麼該 solution：

$$
\boxed{
\text{is born restricted}.
}
$$

---

# 369. 所以後人不會先問：

> 它是不是宇宙全部？

---

# 370. 而會先問：

> **為什麼它可以在這個 regime 成立？**

---

# 371. 這就是 Reverse Theory Restriction。

---

# 372. 最終，一個 theorem 的真值可以永久保持：

$$
\boxed{
\operatorname{Truth}(T)=1,
}
$$

而它的 broader decisiveness：

$$
\boxed{
\delta(T,D_t)
}
$$

可以持續下降。

---

# 373. 因此本文最核心的一句是：

$$
\boxed{
\text{A solution can remain eternally correct while becoming progressively less globally dispositive}.
}
$$

中文：

> **一個解可以永久保持正確，卻隨著問題域擴張，愈來愈不足以決定整個問題。**

而第二句是：

$$
\boxed{
\text{Truth does not shrink; answer status does}.
}
$$

中文：

> **縮小的不是它的真值，而是它作為整體答案的地位。**

---

## 內部理論接口

本篇與下列理論建立橋接，但不宣稱互相還原：

- EX01 Quantifier Scope / QLCert / DECert
- UBE
- SOBTA
- UBGUL B02–B06
- Neo.K Generalized Gödel Problem
- P/NP Supplementary Series S01–S03
- Scope-Induced Non-Decisiveness
- Born-Restricted Solution
- Reverse Theory Restriction
- Answer-Status Demotion
- Dynamic Answer Status

原則：

$$
\boxed{
\text{Truth}
\neq
\text{Answer Status}.
}
$$

以及：

$$
\boxed{
\text{Scope Limitation}
\neq
\text{Falsification}.
}
$$

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown source。數學原始碼僅使用 ` $...$ ` 與 `$$...$$` 作為 canonical delimiter。本篇完成 Independent Epistemic Supplement EX01–EX02。
