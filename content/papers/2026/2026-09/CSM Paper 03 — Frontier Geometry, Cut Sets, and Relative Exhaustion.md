# CSM Paper 03 — Frontier Geometry, Cut Sets, and Relative Exhaustion

## 閉包空間數學論：前沿幾何、割集、障礙覆蓋與相對耗盡

**English Title:** *Closure-Space Mathematics: Frontier Geometry, Cut Sets, Obstruction Covers, and Relative Exhaustion*  
**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 03  
**Version:** v0.1  
**Date:** 2026-08-27  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** zh-TW  
**Status:** Formal Theory / Frontier and Exhaustion Core  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline ` $...$ `; display `$$...$$`

---

## 摘要

本文建立閉包空間數學論（Closure-Space Mathematics, CSM）的前沿幾何與相對耗盡理論。Paper 00 建立相對全域閉包空間；Paper 01 建立全域性型別與作用域契約；Paper 02 建立 typed closure hypergraph、obstruction propagation、reopening 與 route-completeness obligation。本文現在處理一個長程數學研究中最容易被誤判、也最關鍵的問題：

> 當一個大型命題的許多研究路徑已被證明、反證、阻斷、條件閉合或商化後，剩下的「真正未閉部分」究竟是什麼？又在什麼條件下，封住這些剩餘前沿可以合法升格為命題層的耗盡結論？

本文首先定義 **active frontier**、**quotient frontier**、**weighted frontier mass**、**frontier component**、**closure distance** 與 **reopening boundary**。接著將普通 graph cut 推廣到 CSM 的 typed directed hypergraph，區分：

1. route cut；
2. assumption cut；
3. obstruction cut；
4. bridge cut；
5. scope cut；
6. representation cut；
7. mixed typed cut。

本文引入 **Certified Cut** 與 **Obstruction Cover**：前者要求每條 admissible route 都必穿過指定 cut；後者要求一組已認證 obstruction 能覆蓋所有 cut elements 或所有 admissible route classes。只有在：

$$
\boxed{
\mathsf{RouteCompleteness}
+
\mathsf{CutCompleteness}
+
\mathsf{ObstructionCoverage}
+
\mathsf{ScopeFidelity}
+
\mathsf{ParentBridge}
}
$$

同時成立時，才允許把「觀測到的路徑都被封住」升格成 parent-level relative exhaustion。

本文特別區分：

$$
\boxed{
\text{Observed Exhaustion}
\neq
\text{Admissible Exhaustion}
\neq
\text{Relative Mathematical Exhaustion}
\neq
\text{Absolute Mathematical Exhaustion}.
}
$$

這一分層直接阻止一個常見錯誤：研究 corpus 中的 frontier 變小，並不等於數學空間的 frontier 變小；proof basin 被挖到很深，也不等於整個 proof space 已被走遍。

本文並引入 **Frontier Reopening Geometry**。若新表示、新 bridge、新 theorem、scope revision 或 assumption relaxation 使舊 cut 失效，先前的 exhaustion certificate 必須進入 `STALE` 或 `REOPENED` 狀態，並重新計算 frontier。由此，CSM 的「耗盡」不是一次性的最終宣告，而是帶版本、帶作用域、可回放、可撤銷的 relative-global closure event。

最後，本文為 Navier--Stokes 相對全域閉包圖提出第一版 frontiers：不是以論文數量，而是以 quotient route classes、independent obstruction mass、survivor components、bridge debt 與 route-completeness debt 來表示。這使「一步一步封住 NS 命題」第一次具有可操作的幾何意義：研究的直接目標不再是增加 paper count，而是縮減經過 quotient 與 certificate audit 後的有效前沿，同時避免 false contraction。

---

# 1. 研究定位

本文承接：

$$
\mathcal H_{\rm CSM}
=
(V,E,\tau_V,\tau_E,\sigma,\lambda,\pi,\chi,\nu).
$$

Paper 02 已能回答：

- 哪條 route 被哪個 obstruction 封住；
- 哪個 status 只是 blocked；
- 哪個 branch 真正 closed；
- 哪個 closure 可以 reopening。

本文進一步問：

$$
\boxed{
\text{哪些 OPEN / CONDITIONAL / UNKNOWN / REOPENED
節點真正構成 target 的有效前沿？}
}
$$

---

# 2. Raw Frontier

對 target $Q$，定義 raw frontier：

$$
\partial_{\rm raw}\mathfrak C(Q)
=
\left\{
v:
\sigma(v)\in
\{
\mathsf{OPEN},
\mathsf{CONDITIONAL},
\mathsf{UNKNOWN},
\mathsf{REOPENED}
\}
\land
v\leadsto Q
\right\}.
$$

這只是一個候選集合。

---

# 3. Raw Frontier 的缺陷

raw frontier 可能嚴重高估未閉空間，因為：

- 多個節點可能是同一命題；
- 多條 route 只是 representation variant；
- 多個 obstruction debt 其實同源；
- 一條 parent route 的不同細節分支可能被重複計數。

因此 raw frontier 不能作為 exhaustion basis。

---

# 4. Quotient Frontier

使用：

$$
\sim_{\rm prop},
\qquad
\sim_{\rm route},
\qquad
\sim_{\rm obs}
$$

進行商化。

定義：

$$
\boxed{
\partial^\ast\mathfrak C(Q)
=
\partial_{\rm raw}\mathfrak C(Q)
/\sim_{\rm route}.
}
$$

必要時再對 claim layer 做：

$$
\partial_{\rm prop}^\ast.
$$

---

# 5. Frontier Identity Principle

兩個節點在 frontier 中是否算「同一個」，必須由 quotient policy 決定，而不能只看：

- lexical similarity；
- embedding proximity；
- notation similarity；
- same-paper ancestry。

---

# 6. Frontier Weight

對 route class $[R]$ 定義：

$$
w([R])\ge0.
$$

可由以下因素構成：

$$
w([R])
=
f(
\mathsf{Independence},
\mathsf{Generality},
\mathsf{ScopeBreadth},
\mathsf{CertificateQuality},
\mathsf{BridgeDebt}
).
$$

---

# 7. Frontier Mass

$$
\boxed{
M_{\partial}(Q)
=
\sum_{[R]\in\partial^\ast\mathfrak C(Q)}
w([R]).
}
$$

這是一個 research-space observable。

它不是「距離證明完成還有百分之多少」。

---

# 8. Frontier Cardinality 與 Mass 不同

可能：

$$
|\partial^\ast_1|
<
|\partial^\ast_2|
$$

但：

$$
M_{\partial,1}
>
M_{\partial,2}.
$$

因為較少的 route 可能更一般、更獨立、更難被封。

---

# 9. Frontier Component

在 quotient route graph 上，若 frontier nodes 形成 connected component：

$$
F_i
\subset
\partial^\ast\mathfrak C(Q),
$$

稱為：

$$
\boxed{
\text{frontier component}.
}
$$

---

# 10. Component 不等於 Basin

proof basin 是歷史／搜尋動力學上的高密度子圖。

frontier component 是：

> 當前未閉 obligations 之間的結構連通分量。

兩者可重疊但不等價。

---

# 11. Frontier Boundary Type

每個 frontier component 可有 dominant type：

$$
\tau_F(F_i)
\in
\{
\mathsf{LEMMA},
\mathsf{ASSUMPTION},
\mathsf{BRIDGE},
\mathsf{SCOPE},
\mathsf{REPRESENTATION},
\mathsf{OBSTRUCTION},
\mathsf{COMPLETENESS},
\mathsf{COUNTEREXAMPLE},
\mathsf{UNKNOWN}
\}.
$$

---

# 12. Frontier Debt

定義：

$$
\boxed{
\mathsf{FDebt}(F_i)
}
$$

表示 component 尚未支付的 proof obligations。

例如：

- route completeness；
- branch decomposition；
- missing bridge；
- uniformity；
- representation robustness；
- scope promotion；
- hidden-assumption audit。

---

# 13. Frontier Contraction

若：

$$
M_{\partial,t+1}(Q)
<
M_{\partial,t}(Q),
$$

且下降來自 certified closure event，則稱：

$$
\boxed{
\text{certified frontier contraction}.
}
$$

---

# 14. Frontier Expansion

若新研究發現此前未建模的 route class：

$$
M_{\partial,t+1}(Q)
>
M_{\partial,t}(Q),
$$

稱為：

$$
\boxed{
\text{frontier expansion}.
}
$$

這不必然是退步。

---

# 15. Fidelity-over-Size Principle

$$
\boxed{
\text{更忠實但更大的 frontier}
>
\text{錯誤地縮小的 frontier}.
}
$$

在 epistemic quality 上，false contraction 比 truthful expansion 更糟。

---

# 16. False Frontier Contraction

若 frontier 變小源自：

1. false quotient；
2. scope 偷縮；
3. unsupported obstruction transfer；
4. representation deletion；
5. hidden assumption；
6. stale theorem；
7. branch omission；

則標記：

$$
\boxed{
\mathsf{FALSE\_CONTRACTION}.
}
$$

---

# 17. Frontier Reopening

若舊 closure 被撤銷，對應 route class 回到：

$$
\partial^\ast\mathfrak C(Q).
$$

稱：

$$
\boxed{
\text{frontier reopening}.
}
$$

---

# 18. Reopening Boundary

定義：

$$
\boxed{
\partial_{\rm reopen}\mathfrak C(Q)
}
$$

為因 revision 而重新進入 active frontier 的 route classes。

---

# 19. Closure Distance

對節點 $v$ 到 target $Q$ 定義 typed closure distance：

$$
d_{\rm Cl}(v,Q).
$$

它不是純 edge count。

它可以依：

- unresolved assumptions；
- bridge count；
- certificate debt；
- scope promotions；
- obstruction depth；

加權。

---

# 20. Closure Radius

對 target frontier 定義：

$$
\boxed{
R_{\rm Cl}(Q)
=
\sup_{v\in\partial^\ast\mathfrak C(Q)}
d_{\rm Cl}(v,Q).
}
$$

---

# 21. Radius 不等於 Difficulty

$$
\boxed{
R_{\rm Cl}(Q)
\not\Rightarrow
\text{proof difficulty}.
}
$$

一條很短的 route 可能包含極難 lemma。

---

# 22. Closure Depth

定義 route 的 closure depth：

$$
D_{\rm Cl}(R)
$$

表示目前已通過多少 certified narrowing / branch elimination 層。

它可用於比較同一 route family 的研究成熟度。

---

# 23. Directed Hypergraph Route

一條 route 不再只是 vertex sequence。

它是：

$$
R
=
(e_1,e_2,\ldots,e_k)
$$

其中每個 $e_i$ 是 directed hyperedge，且前一批輸出滿足後一批輸入要求。

---

# 24. Admissible Route

$$
R\in\mathcal R_{\rm adm}(Q)
$$

需滿足：

1. edge type legal；
2. assumption consistent；
3. scope valid；
4. bridge certified；
5. target fidelity；
6. no forbidden promotion；
7. version current。

---

# 25. Observed Route

$$
\mathcal R_{\rm obs}(Q)
$$

是 corpus / research history 中真正出現過的 route classes。

一般：

$$
\boxed{
\mathcal R_{\rm obs}(Q)
\subseteq
\mathcal R_{\rm adm}(Q)
}
$$

但不能假設等號。

---

# 26. Enumerated Route

$$
\mathcal R_{\rm enum}^{\Gamma}(Q)
$$

是指定 route grammar $\Gamma$ 下生成出的 route classes。

---

# 27. Relative Route Completeness

若：

$$
\boxed{
\mathcal R_{\rm enum}^{\Gamma}(Q)
=
\mathcal R_{\rm adm}^{\Gamma}(Q)
}
$$

稱：

$$
\mathsf{RCCert}_{\Gamma}(Q)
$$

通過。

---

# 28. Absolute Route Completeness

若要說：

$$
\mathcal R_{\rm enum}(Q)
=
\mathcal R_{\rm adm}(Q)
$$

必須證明 route grammar 本身沒有漏掉 admissible mechanism class。

這通常非常強。

---

# 29. Cut Set

令：

$$
C\subset V.
$$

若每條：

$$
R\in\mathcal R_{\rm adm}^{\Gamma}(Q)
$$

都至少經過 $C$ 中一個 element，則稱 $C$ 是：

$$
\boxed{
\Gamma\text{-route cut}.
}
$$

---

# 30. Typed Cut

cut 本身有型別：

$$
\tau_C(C)
\in
\{
\mathsf{ROUTE},
\mathsf{ASSUMPTION},
\mathsf{OBSTRUCTION},
\mathsf{BRIDGE},
\mathsf{SCOPE},
\mathsf{REPRESENTATION},
\mathsf{MIXED}
\}.
$$

---

# 31. Route Cut

若 cut elements 是 route states，稱：

$$
C_R.
$$

---

# 32. Assumption Cut

若所有 admissible routes 都依賴至少一個：

$$
A\in C_A,
$$

則 $C_A$ 是 assumption cut。

若所有 $A$ 被 refute，可形成高槓桿 closure。

---

# 33. Bridge Cut

若所有 route 都必須經過至少一個 bridge：

$$
B\in C_B,
$$

則 $C_B$ 是 bridge cut。

這對跨 domain / representation theorem 很重要。

---

# 34. Scope Cut

若所有 route 都需要一個 scope promotion：

$$
S\in C_S,
$$

則其 completeness 可轉成 scope-level obstruction 問題。

---

# 35. Representation Cut

若所有現有 route family 都依賴某 representation family：

$$
\rho\in C_{\rho},
$$

那只代表觀測 route 空間具有 representation bottleneck。

它不自動是 admissible proof-space cut。

---

# 36. Mixed Cut

成熟問題往往需要：

$$
C=
C_A
\cup
C_B
\cup
C_R
\cup
C_S.
$$

這形成 mixed typed cut。

---

# 37. Cut Certificate

定義：

$$
\boxed{
\mathsf{CutCert}_{\Gamma}(C,Q)
}
$$

其目標是證：

$$
\forall R\in\mathcal R_{\rm adm}^{\Gamma}(Q),
\quad
R\cap C\neq\varnothing.
$$

---

# 38. Cut Completeness Debt

若只能對 observed routes 證：

$$
\forall R\in\mathcal R_{\rm obs}(Q),
\quad
R\cap C\neq\varnothing,
$$

則形成：

$$
\boxed{
\mathsf{Debt}_{\rm cut}
=
\mathcal R_{\rm adm}^{\Gamma}
\setminus
\mathcal R_{\rm obs}.
}
$$

---

# 39. Minimal Cut

若 $C$ 是 cut，且任意真子集：

$$
C'\subsetneq C
$$

都不再是 cut，則稱：

$$
\boxed{
\text{minimal cut}.
}
$$

---

# 40. Minimum Cut

若有 cost function：

$$
\kappa:C\to\mathbb R_{\ge0},
$$

則最小總成本 cut：

$$
C^\star
=
\arg\min_C
\sum_{c\in C}\kappa(c).
$$

這是 research-routing heuristic。

它不取代 theorem proof。

---

# 41. Hypergraph Transversal

若每條 admissible route 可視為一個 hyperedge family，則 cut 可理解為 route-family transversal。

CSM 使用這個概念，但保留：

- typed edges；
- scope；
- certificate；
- version；
- reopening；

因此不是單純靜態 hypergraph hitting-set 問題。

---

# 42. Obstruction Cover

令 obstruction family：

$$
\mathcal O
=
\{O_1,\ldots,O_m\}.
$$

若對每條 admissible route $R$，至少存在：

$$
O_i
$$

使：

$$
\mathsf{OPCert}(O_i\to R)=\mathsf{PASS},
$$

則稱：

$$
\boxed{
\mathcal O
\text{ is an obstruction cover of }
\mathcal R_{\rm adm}^{\Gamma}(Q).
}
$$

---

# 43. Cover 不等於 Cut

cut 是 route 必經的 structural set。

obstruction cover 是能合法封住 route 的 obstruction family。

兩者不同。

---

# 44. Cut-to-Cover Strategy

一個高槓桿證明策略：

1. 先證明小 cut；
2. 再只對 cut elements 建 obstruction；
3. 由 cut completeness 推回全部 route。

---

# 45. Cover Certificate

定義：

$$
\boxed{
\mathsf{CoverCert}_{\Gamma}(\mathcal O,Q).
}
$$

需要：

- route completeness；
- propagation certificates；
- scope match；
- no uncovered class；
- version freshness。

---

# 46. Obstruction Cover Debt

若存在 uncovered route class：

$$
[R]\notin
\bigcup_i
\mathsf{BlockedBy}(O_i),
$$

則：

$$
\mathsf{Debt}_{\rm cover}\neq\varnothing.
$$

---

# 47. Survivor Set

定義：

$$
\boxed{
\mathcal S(Q)
=
\left\{
[R]\in\mathcal R_{\rm adm}^{\Gamma}(Q):
[R]\text{ not certified closed}
\right\}.
}
$$

---

# 48. Survivor Frontier

若：

$$
\mathcal S(Q)
=
\partial^\ast\mathfrak C(Q)
$$

表示所有 active frontier 都已被壓成 survivor route classes。

---

# 49. Minimal Survivor Set

若所有 survivor 的更一般 parent classes 都已被封或分解，得到：

$$
\boxed{
\mathcal S_{\min}(Q).
}
$$

---

# 50. Survivor Compression Ratio

可定義：

$$
\boxed{
\operatorname{SCR}(Q)
=
\frac{
|\mathcal S_{\min}(Q)|
}{
|\mathcal R_{\rm enum}^{\Gamma}(Q)|
}.
}
$$

只用作 research diagnostic。

---

# 51. Exhaustion Level 0 — Corpus Exhaustion

若：

$$
\partial_{\rm raw}
$$

在目前 corpus 中沒有新節點，僅能說：

$$
\boxed{
\mathsf{EXH}_{0}
=
\text{corpus-local exhaustion}.
}
$$

---

# 52. Exhaustion Level 1 — Observed Route Exhaustion

若：

$$
\forall R\in\mathcal R_{\rm obs}(Q),
\quad
R\text{ closed/blocked},
$$

稱：

$$
\boxed{
\mathsf{EXH}_{1}.
}
$$

---

# 53. Exhaustion Level 2 — Grammar-Relative Exhaustion

若：

$$
\mathsf{RCCert}_{\Gamma}(Q)=\mathsf{PASS}
$$

且：

$$
\forall R\in\mathcal R_{\rm adm}^{\Gamma}(Q),
\quad
R\text{ certified closed},
$$

稱：

$$
\boxed{
\mathsf{EXH}_{2}^{\Gamma}.
}
$$

---

# 54. Exhaustion Level 3 — Domain-Relative Mathematical Exhaustion

若再有 parent bridge：

$$
\neg\operatorname{RouteExists}_{\Gamma}(Q)
\Longrightarrow
\neg Q
$$

或對正向 target 有對應 closure bridge，則：

$$
\boxed{
\mathsf{EXH}_{3}^{D,\Gamma}.
}
$$

---

# 55. Exhaustion Level 4 — Cross-Representation Exhaustion

若所有 admissible representation classes：

$$
\rho\in\mathcal P_{\rm adm}
$$

都已覆蓋，且 representation robustness 成立：

$$
\boxed{
\mathsf{EXH}_{4}^{D}.
}
$$

---

# 56. Exhaustion Level 5 — Absolute Exhaustion Candidate

只有在 domain、representation、route grammar、bridge 與 formal-system completeness obligations 都被處理後，才可討論：

$$
\boxed{
\mathsf{EXH}_{5}
=
\text{absolute exhaustion candidate}.
}
$$

本文不假設它通常可證。

---

# 57. Exhaustion Ladder

$$
\boxed{
\mathsf{EXH}_0
\prec
\mathsf{EXH}_1
\prec
\mathsf{EXH}_2
\prec
\mathsf{EXH}_3
\prec
\mathsf{EXH}_4
\prec
\mathsf{EXH}_5.
}
$$

禁止跳級。

---

# 58. Relative Exhaustion Certificate

定義：

$$
\boxed{
\mathsf{RECert}_{D,\Gamma}(Q).
}
$$

至少包含：

1. target statement；
2. domain；
3. route grammar；
4. route-completeness cert；
5. cut cert；
6. obstruction cover cert；
7. bridge cert；
8. representation policy；
9. scope policy；
10. debt ledger；
11. version；
12. reopening policy。

---

# 59. Exhaustion with Debt

若：

$$
\mathsf{Debt}\neq\varnothing,
$$

則 exhaustion status 只能標：

$$
\boxed{
\mathsf{PARTIAL\_EXHAUSTION}.
}
$$

---

# 60. Exhaustion Staleness

若 theorem base、scope、representation family 或 bridge set 改變，舊：

$$
\mathsf{RECert}
$$

必須進入：

$$
\mathsf{STALE}.
$$

---

# 61. Revalidated Exhaustion

只有重新跑 closure audit 後，才可：

$$
\mathsf{STALE}
\to
\mathsf{VALID}.
$$

---

# 62. Parent Closure Bridge

若 route exhaustion 要推出 parent claim closure，需要：

$$
\boxed{
\mathsf{ParentBridgeCert}.
}
$$

例如：

$$
\neg\operatorname{RouteExists}
\Rightarrow
\neg Q.
$$

這條 implication 不能被默認。

---

# 63. Positive Parent Bridge

對 existence theorem：

$$
\exists R\in\mathcal R_{\rm adm}(Q)
\land
\mathsf{Proof}(R)
\Rightarrow
Q.
$$

也需要 target fidelity。

---

# 64. Negative Parent Bridge

對 impossibility theorem：

$$
\forall R\in\mathcal R_{\rm adm}(Q),
\neg\mathsf{Valid}(R)
\Rightarrow
\neg Q
$$

通常需要 route completeness 與 proof-form completeness。

---

# 65. Exhaustion 不等於 Falsehood

即使：

$$
\mathsf{EXH}_2^\Gamma
$$

成立，也只表示：

> 在 $\Gamma$ 中沒有存活 route。

不能直接寫：

$$
\neg Q.
$$

---

# 66. Exhaustion 不等於 Unprovability

同樣：

$$
\mathsf{EXH}_2^\Gamma
\not\Rightarrow
\text{$Q$ unprovable}.
$$

---

# 67. Exhaustion 不等於 Independence

只有指定 formal theory $\mathcal T$ 下真正證明：

$$
\mathcal T\nvdash Q,
\qquad
\mathcal T\nvdash\neg Q
$$

才能說 relative independence。

---

# 68. Cut Centrality

定義 cut centrality：

$$
Z(C)
$$

表示 cut 所截斷的 independent route mass。

---

# 69. Obstruction Centrality

定義：

$$
Z(O)
=
\sum_{[R]:
O\triangleright R}
w([R]).
$$

---

# 70. Centrality 不是 Necessity

$$
\boxed{
Z(O)\text{ high}
\not\Rightarrow
O\text{ mathematically necessary}.
}
$$

---

# 71. Closure Bottleneck

若少數 cut elements 承擔大部分 route mass：

$$
Z(C)/M_{\mathcal R}\to1,
$$

稱：

$$
\boxed{
\text{closure bottleneck}.
}
$$

---

# 72. Bottleneck Research Priority

對 closure bottleneck 優先研究，通常能最大化：

$$
\Delta M_{\partial}
$$

的預期減少。

這是 routing heuristic。

---

# 73. Bottleneck Reopening Risk

高 centrality cut 一旦失效，也可能造成大規模 frontier reopening。

因此要記：

$$
\boxed{
\mathsf{ReopenRisk}(C).
}
$$

---

# 74. Redundant Cut

若多個 cut elements 實際屬於同一 obstruction class，raw cut size 會高估。

需 quotient：

$$
C^\ast=C/\sim_{\rm obs}.
$$

---

# 75. Independent Cut Mass

$$
\boxed{
M_C
=
\sum_{[c]\in C^\ast}
w([c]).
}
$$

---

# 76. Route-Cut Duality Candidate

在某些有限 typed graph 中，minimal route cover 與 obstruction cut 可能形成對偶問題。

本文只將其作為研究方向，不主張一般 max-flow/min-cut 類定理已自動成立。

---

# 77. Hypergraph Duality Debt

若要建立一般對偶定理，需要處理：

- hyperedge multiplicity；
- edge typing；
- nonlocal assumptions；
- scope；
- bridge loss；
- reopening；
- versioning。

---

# 78. Frontier Topology

本文暫不把 frontier 宣稱為傳統拓撲空間。

但可定義 graph-induced neighborhood：

$$
N_k(v)
=
\{u:d_{\rm graph}(u,v)\le k\}.
$$

---

# 79. Closure Neighborhood

更適合 CSM 的是：

$$
\boxed{
N_{\rm Cl}(v)
=
\{u:
u\text{ shares closure obligations with }v\}.
}
$$

---

# 80. Shared-Obstruction Neighborhood

若兩 route 都受同一 obstruction family 約束：

$$
O\triangleright R_1,
\quad
O\triangleright R_2,
$$

則可視為同一 closure neighborhood。

---

# 81. Shared-Bridge Neighborhood

若多條 route 共用同一 bridge debt，則形成 bridge-frontier cluster。

---

# 82. Frontier Curvature Heuristic

若一個 frontier node 的小型修改造成大量 neighboring routes reopen/close，可定義高 sensitivity。

本文暫稱：

$$
\boxed{
\kappa_{\rm F}(v)
}
$$

為 frontier curvature heuristic。

這不是微分幾何曲率。

---

# 83. High-Curvature Frontier

高 $\kappa_{\rm F}$ 節點通常是：

- key lemma；
- scope gate；
- representation bridge；
- common assumption；
- central obstruction。

---

# 84. Frontier Flat Region

大量彼此相似、低影響、低獨立性的 open nodes 可形成：

$$
\boxed{
\text{frontier flat region}.
}
$$

通常應先 quotient。

---

# 85. Frontier Singularity Heuristic

若所有 active route mass 在少數 unresolved nodes 聚集：

$$
M_{\partial}(F_{\rm core})
/
M_{\partial}(Q)
\to1,
$$

可稱 closure-frontier concentration。

本文不把它等同 PDE singularity。

---

# 86. Closure Cone

對某 unresolved assumption $A$，所有依賴它的 downstream routes：

$$
\boxed{
\mathsf{Cone}(A)
=
\{R:A\leadsto R\leadsto Q\}.
}
$$

---

# 87. Cone Closure

若 $A$ 被 theorem-level refute，且 inheritance cert 完整，整個 cone 可批次進入 blocked / closed audit。

---

# 88. Cone Reopening

若 $A$ 的 refutation 被限縮，整個 cone 進入 reopening audit。

---

# 89. Closure Shell

以 closure distance 分層：

$$
\boxed{
\mathcal S_k(Q)
=
\{v:d_{\rm Cl}(v,Q)=k\}.
}
$$

---

# 90. Shell Progression

研究歷史可追蹤 frontier 從遠 shell 壓向近 shell，或反之。

這是幾何描述，不保證 proof completion。

---

# 91. Closure Core

定義：

$$
\boxed{
\mathsf{Core}_{\rm Cl}(Q)
}
$$

為所有 admissible route class 的高 overlap 子結構。

---

# 92. Core 不等於 Necessary Lemma

只有有 CutCert 時，core 才能升格成 route-necessary region。

---

# 93. Relative Global Frontier

對 domain $D$：

$$
\boxed{
\partial_D^\ast\mathfrak C(Q).
}
$$

不同 domain 的 frontier 不必相同。

---

# 94. Domain Projection of Frontier

若：

$$
D_0\preceq D_1,
$$

可有投影：

$$
\Pi_{D_1\to D_0}
:
\partial_{D_1}^\ast
\to
\partial_{D_0}^\ast.
$$

但不能預設 injective 或 surjective。

---

# 95. Scope Expansion Creates Frontier

當 globality scope 擴張，新 proof obligations 可出現：

$$
\boxed{
\partial_{D_1}^\ast
\supsetneq
\operatorname{Lift}
(\partial_{D_0}^\ast).
}
$$

---

# 96. NS Formal Frontier

對 Clay/formal NS domain：

$$
\boxed{
\partial_{\mathfrak N_{\rm C}}^\ast
}
$$

只包含對 formal target 有合法 route relevance 的 obligations。

---

# 97. NS Physical Frontier

$$
\partial_{\mathfrak N_{\rm P}}^\ast
$$

還會包含 model-to-world bridge obligations。

因此：

$$
\partial_{\mathfrak N_{\rm C}}^\ast
\neq
\partial_{\mathfrak N_{\rm P}}^\ast.
$$

---

# 98. NS Generalized Frontier

對：

$$
\mathfrak N_{\rm G}^{\Sigma}
$$

frontier 依 signature $\Sigma$ 改變。

沒有 $\Sigma$ 就沒有唯一 generalized frontier。

---

# 99. NS Cross-Series Frontier

NS 的 relative graph 應整合：

$$
\mathcal H_{\rm C1-C6},
\mathcal H_{\rm X72},
\mathcal H_{\rm DCRP},
\mathcal H_{\rm RFP},
\mathcal H_{\rm MORP},
\mathcal H_{\rm FCBP}.
$$

但先做 route/obstruction quotient。

---

# 100. NS Frontier Node 類型

典型 frontier node：

- unresolved bridge；
- minimal survivor；
- conditional lemma；
- route completeness debt；
- representation ambiguity；
- scope mismatch；
- external theorem interface；
- potential counterexample class。

---

# 101. NS Obstruction Cover

未來可建立：

$$
\mathcal O_{\rm NS}^{\rm active}
$$

並測試：

$$
\mathsf{CoverCert}_{\Gamma_{\rm NS}}
(
\mathcal O_{\rm NS}^{\rm active},
Q_{\rm Clay}
).
$$

早期預期大概率 FAIL / PARTIAL。

---

# 102. NS Cut Discovery

可從現有 corpus 中找：

$$
C_{\rm NS}^{\rm candidate}
$$

例如高 confluence assumptions、bridge、carrier states 或 recurrent survivor classes。

但 candidate cut 不是 certified cut。

---

# 103. NS-203 的新用途

過去 NS-203 corpus 不再只用於 novelty / saturation analysis。

它現在可以作：

$$
\boxed{
\text{candidate frontier / cut / obstruction mining substrate}.
}
$$

---

# 104. Corpus-to-Closure Pipeline

$$
\boxed{
\text{Artifacts}
\to
\text{Claims}
\to
\text{Route Classes}
\to
\text{Obstruction Classes}
\to
\text{Frontier}
\to
\text{Candidate Cuts}
\to
\text{Certified Cuts}.
}
$$

---

# 105. Mining 不等於 Proof

任何自動 graph mining：

$$
\not\Rightarrow
\mathsf{CutCert}.
$$

formal / theorem-level audit 仍必要。

---

# 106. Exhaustion Proof Pattern A — Finite Branching

若：

$$
Q
\leftrightarrow
Q_1\vee\cdots\vee Q_n
$$

有 BDCert，且每個 branch theorem-level refuted，則：

$$
Q
$$

負閉合。

---

# 107. Exhaustion Proof Pattern B — Certified Cut

若：

1. CutCert 成立；
2. 每個 cut node 都被 refute；
3. propagation valid；
4. parent bridge valid；

則 parent negative closure 可成立。

---

# 108. Exhaustion Proof Pattern C — Obstruction Cover

若：

$$
\mathcal O
$$

對 admissible route space 是 complete cover，且 route completeness 已證，則可得到 route exhaustion。

---

# 109. Exhaustion Proof Pattern D — Representation Family

若每個 admissible representation family 都有 route exhaustion，還需要 cross-representation completeness。

---

# 110. Exhaustion Proof Pattern E — Scope Family

若 target 帶 parameter family：

$$
\theta\in\Theta,
$$

每個局部 $\theta$ 的 closure 不自動推出 uniform closure。

需 uniformity certificate。

---

# 111. Uniform Exhaustion

$$
\boxed{
\forall\theta\in\Theta,
\quad
\mathsf{RECert}_{D,\Gamma}(Q_\theta)
}
$$

仍不一定推出：

$$
\mathsf{RECert}
(
\forall\theta,Q_\theta
).
$$

需要 uniform proof object。

---

# 112. Compactness Bridge

某些情況可利用 compactness 把局部 closure 升格 uniform closure。

但 compactness 本身必須在指定 topology / parameterization 下證明。

---

# 113. Finite Cover Bridge

若 parameter space 可由有限 certified regions 覆蓋：

$$
\Theta
=
\bigcup_{i=1}^n\Theta_i,
$$

且每區有 closure cert，可形成 finite-cover exhaustion。

---

# 114. Infinite Cover Debt

若只證 countably many cases，但不能證 exhaustiveness，仍有 coverage debt。

---

# 115. Closure Measure Warning

本文不主張存在自然機率測度：

$$
\mu(\Omega^{\rm math}).
$$

所以不應寫：

> NS proof space 已關閉 93%。

---

# 116. Operational Coverage

可以相對指定 finite graph 定義：

$$
\operatorname{Cov}_{\Gamma}
=
1-
\frac{
M_{\partial}
}{
M_{\rm total}^{\Gamma}
}.
$$

但必須標：

$$
\boxed{
\Gamma\text{-relative operational metric}.
}
$$

---

# 117. Coverage 不等於 Truth Probability

$$
\boxed{
\operatorname{Cov}_{\Gamma}
\not\Rightarrow
P(Q\text{ true}).
}
$$

---

# 118. Closure Saturation

若新增研究事件長期無法產生新 frontier class 或新 cut escape，可稱：

$$
\mathsf{Sat}_{\rm Cl}(B;R,N).
$$

它仍是 regime-relative。

---

# 119. Saturation 不等於 Exhaustion

$$
\boxed{
\mathsf{Saturation}
\neq
\mathsf{Exhaustion}.
}
$$

---

# 120. Exhaustion 不等於 Closure

某 route space 可耗盡，但 parent target 仍未閉合。

因此：

$$
\boxed{
\mathsf{RouteExhaustion}
\neq
\mathsf{ClaimClosure}.
}
$$

---

# 121. Closure 不等於 Completeness

一個 claim closed 不代表 surrounding theory complete。

---

# 122. Relative Completeness

CSM 最常使用：

$$
\boxed{
\text{relative completeness}
}
$$

而不是 absolute completeness。

---

# 123. Closure Certificate Stack

一個成熟 closure conclusion 應攜帶：

$$
\boxed{
\mathsf{CertStack}
=
(
\mathsf{StatementCert},
\mathsf{ScopeCert},
\mathsf{RouteCert},
\mathsf{CutCert},
\mathsf{CoverCert},
\mathsf{BridgeCert},
\mathsf{DebtCert}
).
}
$$

---

# 124. Certificate Failure Modes

任一層失敗都應降格：

- claim；
- branch；
- exhaustion；
- cut；
- cover；

的 status，而不是硬維持 closed。

---

# 125. Certificate Composition

certificates 的組合本身需要 compatibility。

不能假設：

$$
\mathsf{Cert}_1+\mathsf{Cert}_2
\Rightarrow
\mathsf{Cert}_{12}.
$$

---

# 126. Certificate Coherence

若不同 cert 對 scope / assumptions / representation 標示不同，必須進行 coherence audit。

---

# 127. Exhaustion Ledger

每次 exhaustion event：

$$
e_{\rm exh}
=
\left\langle
Q,D,\Gamma,C,\mathcal O,
\mathsf{RECert},
\mathsf{Debt},
\nu,t
\right\rangle.
$$

---

# 128. Reopening Exhaustion Event

若 cut 失效：

$$
e_{\rm reopen}
$$

引用舊 exhaustion event，而不是刪除。

---

# 129. Relative Exhaustion as Versioned Object

$$
\boxed{
\mathsf{EXH}_{D,\Gamma}^{(\nu)}
}
$$

不同版本不可無證合併。

---

# 130. Frontier Version

同樣：

$$
\partial^{\ast,(\nu)}\mathfrak C(Q).
$$

---

# 131. Frontier Drift

定義版本間：

$$
\Delta\partial^\ast
=
\partial^{\ast,(\nu+1)}
\triangle
\partial^{\ast,(\nu)}.
$$

可分析新增／消失／重開 route classes。

---

# 132. Closure Drift

closure status distribution 隨版本改變：

$$
\Delta\sigma.
$$

---

# 133. Research Value of Negative Results

formal no-go 若能形成高-centrality obstruction cover，其價值可能高於許多孤立 positive lemmas。

---

# 134. Research Value of Reopening

找到一個使高-centrality false cut 失效的 counterexample 或 bridge，也可能極高價值。

---

# 135. Proof-Space Geometry Is Not Truth Geometry

CSM 必須保持：

$$
\boxed{
\text{proof-space geometry}
\neq
\text{truth-value geometry}.
}
$$

圖上「近」不代表邏輯上「近真」。

---

# 136. Search Geometry Is Not Proof Geometry

同樣：

$$
\boxed{
\text{search geometry}
\neq
\text{proof geometry}.
}
$$

embedding cluster 不是 theorem relation。

---

# 137. Representation Geometry Is Not Ontology

$$
\boxed{
\text{representation proximity}
\neq
\text{ontological identity}.
}
$$

---

# 138. Frontier Geometry Is Operational

本文的「幾何」首先指：

- graph structure；
- quotient structure；
- reachability；
- cuts；
- covers；
- weighted neighborhoods；
- closure distance。

不自動主張 smooth manifold structure。

---

# 139. Paper 03 核心命題一

## Relative Exhaustion Theorem Schema

若：

$$
\mathsf{RCCert}_{\Gamma}(Q)=\mathsf{PASS},
$$

$$
\mathsf{CutCert}_{\Gamma}(C,Q)=\mathsf{PASS},
$$

$$
\forall c\in C,
\quad
\sigma(c)=\mathsf{CLOSED}^{-},
$$

且 closure inheritance 全部有 cert，則：

$$
\boxed{
\Gamma
\vdash
\neg\operatorname{AdmissibleRoute}(Q).
}
$$

---

# 140. Paper 03 核心命題二

## Parent Closure Theorem Schema

若另有：

$$
\mathsf{ParentBridgeCert}
:
\neg\operatorname{AdmissibleRoute}(Q)
\Rightarrow
\neg Q,
$$

則：

$$
\boxed{
D,\Gamma
\vdash
\neg Q.
}
$$

這是 relative-domain theorem conclusion。

---

# 141. Paper 03 核心命題三

## Reopening Theorem Schema

若：

$$
\mathsf{CutCert}^{(\nu)}
$$

依賴 premise $A$，而新版本證：

$$
\neg\mathsf{Valid}^{(\nu+1)}(A),
$$

則舊 exhaustion cert 必標：

$$
\boxed{
\mathsf{STALE}
}
$$

並重建 frontier。

---

# 142. Paper 03 核心命題四

## False Exhaustion No-Go

若以下任何一項缺失：

- route completeness；
- cut completeness；
- obstruction cover；
- scope fidelity；
- parent bridge；

則禁止從 observed route closure 推出 parent theorem closure。

---

# 143. Paper 03 核心命題五

## Relative-Global Frontier Principle

任何「全域 frontier」都必須寫成：

$$
\boxed{
\partial^\ast_{D,\Gamma,\rho,\nu}
\mathfrak C(Q)
}
$$

至少標明：

- domain；
- route grammar；
- representation policy；
- version。

---

# 144. NS 實例化前置條件

在真正建立 NS closure graph 前，至少需要：

1. canonical artifact inventory；
2. claim extraction；
3. assumption extraction；
4. route quotient；
5. obstruction quotient；
6. scope normalization；
7. cross-series bridge audit；
8. status reclassification；
9. survivor extraction；
10. frontier reconstruction。

---

# 145. NS 第一版不追求全域完備

v0.1 只建立：

$$
\boxed{
\partial^{\ast}_{\rm obs}
\mathfrak C_{\rm NS}
}
$$

即 observed relative frontier。

---

# 146. NS 第二版

在 route grammar 建立後：

$$
\partial^{\ast}_{\Gamma_{\rm NS}}
\mathfrak C_{\rm NS}.
$$

---

# 147. NS 第三版

只有在 route-completeness 有部分 theorem 支持後，才討論：

$$
\mathsf{EXH}_2^{\Gamma_{\rm NS}}.
$$

---

# 148. NS 的初始高風險錯誤

最需要避免：

$$
\boxed{
\text{203 artifacts}
\Rightarrow
\text{203 independent routes}.
}
$$

---

# 149. 第二個高風險錯誤

$$
\boxed{
\text{many NO-GOs}
\Rightarrow
\text{NS false or regular}.
}
$$

---

# 150. 第三個高風險錯誤

$$
\boxed{
\text{one recurrent survivor}
\Rightarrow
\text{blow-up mechanism}.
}
$$

---

# 151. 第四個高風險錯誤

$$
\boxed{
\text{frontier small}
\Rightarrow
\text{near proof}.
}
$$

---

# 152. NS 的真正研究目標

初期不是追求：

$$
\mathsf{Proof}(Q_{\rm NS}).
$$

而是建立：

$$
\boxed{
\text{a faithful, typed, quotient-aware, reopenable relative closure geometry}.
}
$$

---

# 153. CSM Paper 03 與 LSI-PSD 的關係

LSI-PSD 已建立：

- proof basins；
- semantic quotient；
- obstruction confluence；
- search regime limitation；
- observatory governance。

本文吸收其方法論，但將 frontier/cut/exhaustion 升格為 CSM closure operations。

---

# 154. CSM Paper 03 與 UCT 的關係

UCT 的 relative-global gate、bridge/debt/ledger 在此具體化為：

- CutCert；
- CoverCert；
- RECert；
- ParentBridgeCert；
- reopening ledger。

---

# 155. CSM Paper 03 與一般圖論的關係

本文使用：

- directed graph；
- hypergraph；
- cut；
- transversal；
- cover；
- connected component；

作為形式工具。

本文不宣稱發明這些一般概念。

CSM 的新增研究焦點在於：

> 將它們與 typed proof objects、scope contracts、obstruction certificates、reopening、debt、versioned ledger 與 relative-global theorem gates 綁在同一 operational framework 中。

---

# 156. Machine Schema — Frontier Record

```yaml
frontier_record:
  target_id:
  domain_id:
  route_grammar_id:
  representation_policy:
  version:
  raw_nodes: []
  quotient_route_classes: []
  components: []
  frontier_mass:
  closure_radius:
  debt_ids: []
  reopened_classes: []
  certificate_status:
```

---

# 157. Machine Schema — Cut Record

```yaml
cut_record:
  cut_id:
  target_id:
  cut_type:
  element_ids: []
  route_grammar_id:
  coverage_scope:
  cut_certificate_id:
  uncovered_route_classes: []
  quotient_policy:
  version:
  status:
```

---

# 158. Machine Schema — Obstruction Cover

```yaml
obstruction_cover:
  cover_id:
  target_id:
  obstruction_ids: []
  route_grammar_id:
  covered_route_classes: []
  uncovered_route_classes: []
  propagation_certificate_ids: []
  scope_fidelity:
  representation_fidelity:
  version:
  status:
```

---

# 159. Machine Schema — Relative Exhaustion

```yaml
relative_exhaustion:
  exhaustion_id:
  target_id:
  domain_id:
  route_grammar_id:
  exhaustion_level:
  route_completeness_certificate:
  cut_certificate:
  obstruction_cover_certificate:
  parent_bridge_certificate:
  representation_policy:
  scope_policy:
  debt_ids: []
  reopening_policy:
  version:
  status:
```

---

# 160. Validation Scenario A — Small raw frontier, bad quotient

若 raw frontier 100 nodes 被錯誤合併成 1 class，則即使：

$$
|\partial^\ast|=1
$$

也不能接受。

gold audit 必須抓出 false quotient。

---

# 161. Validation Scenario B — True minimal cut

若所有 admissible routes 都經 $A$，且 CutCert 成立，則：

$$
C=\{A\}
$$

是真 minimal cut。

---

# 162. Validation Scenario C — Observed-only cut

若 $A$ 只截斷所有 observed routes，則：

$$
\mathsf{CutCert}_{\rm obs}
$$

不能升格為 grammar-relative CutCert。

---

# 163. Validation Scenario D — Complete obstruction cover

若 route completeness 成立且每個 route 都有 valid OPCert，則 obstruction cover PASS。

---

# 164. Validation Scenario E — One uncovered survivor

若只有一個 route class 未被 cover，則 exhaustion FAIL。

該 class 成為 minimal survivor candidate。

---

# 165. Validation Scenario F — Reopened cut

若 cut element 的 obstruction 被新 counterexample 限縮，cut 必須重審。

---

# 166. Validation Scenario G — Parent bridge missing

route exhaustion 已證，但沒有：

$$
\neg\operatorname{RouteExists}\Rightarrow\neg Q,
$$

則 parent claim仍不得 CLOSED negative。

---

# 167. Validation Scenario H — Scope expansion

若從一個 parameter region 擴張到全 parameter space，舊 cut 不自動維持 completeness。

---

# 168. Validation Scenario I — Cross-representation escape

representation $\rho_1$ exhaustion 不排除 $\rho_2$。

若 $\rho_2$ 是 admissible，frontier reopening。

---

# 169. Validation Scenario J — NS observed frontier

將 NS `OPEN / SURVIVOR / STOP` 編譯後，只能先得到：

$$
\partial_{\rm obs}^\ast\mathfrak C_{\rm NS}.
$$

不得宣稱 absolute frontier。

---

# 170. Validation Scenario K — NS scalar NO-GO

scalar-budget NO-GO 可成為高-centrality obstruction，但若其他 geometric/nonlocal routes 不經它，就不是 global cut。

---

# 171. Validation Scenario L — NS survivor concentration

若大量 sibling branches 被封，只剩少數 shear/polarization / ancient-profile classes，這是 survivor compression，不是 theorem completion。

---

# 172. Non-Claim 1

本文不主張所有 proof spaces 天然具有唯一 graph representation。

---

# 173. Non-Claim 2

本文不主張所有 mathematical routes 可有效列舉。

---

# 174. Non-Claim 3

本文不主張 finite corpus 可以證明 absolute route completeness。

---

# 175. Non-Claim 4

本文不主張 frontier mass 是客觀自然測度。

---

# 176. Non-Claim 5

本文不主張 minimal cut 自動等於最重要數學 lemma。

---

# 177. Non-Claim 6

本文不主張 graph centrality 等於 theorem necessity。

---

# 178. Non-Claim 7

本文不主張 obstruction confluence 等於 unprovability。

---

# 179. Non-Claim 8

本文不主張 relative exhaustion 等於 absolute mathematical exhaustion。

---

# 180. Paper 04 路線

下一篇應處理：

$$
\boxed{
\textbf{Closure Dynamics, Reopening, and Fixed-Point Evolution}
}
$$

包括：

- time-indexed closure states；
- schedule dependence；
- closure fixed points；
- reopening waves；
- debt discharge；
- closure hysteresis；
- frontier attractors；
- relative equilibrium；
- research routing dynamics。

---

# 181. 結論

本文將 CSM 從「能封路」推進到「能描述剩餘未閉空間」。

其核心鏈條為：

$$
\boxed{
\text{Route Space}
\to
\text{Quotient Frontier}
\to
\text{Certified Cut}
\to
\text{Obstruction Cover}
\to
\text{Relative Exhaustion}
\to
\text{Parent Closure Gate}.
}
$$

最重要的非坍縮是：

$$
\boxed{
\text{Observed Exhaustion}
\neq
\text{Admissible Exhaustion}
\neq
\text{Relative Mathematical Exhaustion}
\neq
\text{Absolute Mathematical Exhaustion}.
}
$$

因此，「一步一步把命題封住」只有在 route completeness、cut completeness、obstruction coverage、scope fidelity 與 parent bridge 全部有證書時，才真正具有 theorem-level 意義。

CSM 的目標不是把數學研究變成漂亮的圖，而是讓：

$$
\boxed{
\text{每一次封閉、每一次遺漏、每一次重開、每一次耗盡宣告}
}
$$

都能被精確定位在它真正有權限作用的相對數學空間中。

---

## 附錄 A — Paper 03 核心不變量

1. raw frontier 不等於 quotient frontier；
2. frontier contraction 不等於 proof progress；
3. false contraction 必須可檢測；
4. cut 必須有 route coverage proof；
5. observed cut 不等於 admissible cut；
6. cut 不等於 obstruction cover；
7. obstruction cover 必須有 OPCert；
8. survivor 不等於 successful route；
9. route exhaustion 不等於 parent claim closure；
10. exhaustion ladder 不可跳級；
11. representation exhaustion 不得無證跨 representation；
12. scope-local exhaustion 不得無證升格；
13. exhaustion certificate 可 stale；
14. reopening 必須重建 frontier；
15. relative-global frontier 必須標 domain / grammar / representation / version。

---

## 附錄 B — 系列依賴

### Paper 00
- Relative-Global Closure Space
- status / debt / ledger
- route-completeness obligation

### Paper 01
- Globality Typing
- Scope Contract
- Domain Stratification
- Globality Promotion

### Paper 02
- Typed Closure Hypergraph
- Obstruction Propagation
- Reopening
- Branch Decomposition
- Route Exhaustion Machinery

### Paper 03
- Frontier Geometry
- Cut Sets
- Obstruction Covers
- Exhaustion Ladder
- Relative Exhaustion Certificate
- Parent Closure Gate

---

**END OF CSM PAPER 03 v0.1**
