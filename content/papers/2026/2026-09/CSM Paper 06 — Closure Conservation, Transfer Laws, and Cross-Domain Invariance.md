# CSM Paper 06 — Closure Conservation, Transfer Laws, and Cross-Domain Invariance

## 閉包空間數學論：閉包守恆、傳遞律與跨域不變性

**English Title:** *Closure-Space Mathematics: Closure Conservation, Transfer Laws, and Cross-Domain Invariance*  
**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 06  
**Version:** v0.1  
**Date:** 2026-08-27  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** zh-TW  
**Status:** Formal Theory / Cross-Domain Transfer Core  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline ` $...$ `; display `$$...$$`

---

## 摘要

本文建立閉包空間數學論（Closure-Space Mathematics, CSM）的跨域傳遞核心。Paper 00–05 已依序建立相對全域閉包空間、全域性型別、typed closure hypergraph、frontier / cut / exhaustion、closure dynamics，以及 projection / attention / static-dynamic compilation。當一個 closure conclusion 從某個數學 domain、representation 或 proof regime 被搬運到另一個 domain 時，新的核心問題是：

> 哪些 closure 結論可以保存？哪些只能保守降格？哪些會因 scope、assumption、representation、solution notion、model interpretation 或 physical realization 的改變而失去傳遞權限？

本文將跨域轉換記為：

$$
\boxed{
\mathcal T_{A\to B}:
\mathfrak C_A
\rightharpoonup
\mathfrak C_B.
}
$$

箭頭使用部分映射，因為不是所有 closure object 都有合法 target image。

本文提出 **Closure Transfer Contract**：

$$
\boxed{
\mathsf{TContract}_{A\to B}
=
\left\langle
\mathsf{DomainMap},
\mathsf{ObjectMap},
\mathsf{InvariantMap},
\mathsf{StatusMap},
\mathsf{Bridge},
\mathsf{Loss},
\mathsf{Debt},
\mathsf{Version}
\right\rangle.
}
$$

並將 transfer 分成三類：

1. **Conservative Transfer**：closure-critical invariants 與 theorem authority 被保存；
2. **Lossy Transfer**：部分 invariant 被保留，但 closure authority 必降格；
3. **Non-Transferable**：沒有足夠 bridge / scope / semantic mapping，禁止升格。

本文核心非坍縮是：

$$
\boxed{
\text{Transferable Structure}
\neq
\text{Transferable Closure Authority}.
}
$$

一個 lemma、operator、graph pattern、estimate 或 obstruction 可以在形式上被搬到另一個 domain，但不表示它原本的 theorem status、scope 或 no-go authority 自動跟著搬過去。

本文定義 **Closure Conservation Profile**：

$$
\boxed{
\mathfrak K_{A\to B}
=
(
K_{\rm id},
K_{\rm target},
K_{\rm scope},
K_{\rm asm},
K_{\rm status},
K_{\rm cert},
K_{\rm debt},
K_{\rm bridge},
K_{\rm frontier},
K_{\rm version}
).
}
$$

只有在 transfer 所需的不變量被保存時，才允許相應 closure conclusion 跨域。

本文特別處理 Navier--Stokes 三域：

$$
\mathfrak N_{\rm C},
\qquad
\mathfrak N_{\rm G}^{\Sigma},
\qquad
\mathfrak N_{\rm P}.
$$

其中 formal / Clay NS 的定理可以被用作 generalized NS-like family 的 **special-case anchor**，但不得無證升格成 equation-family theorem；同樣，formal NS theorem 可以支援 physical modeling，但不得被自動稱為 physical law proof。由此得到：

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm G}^{\Sigma})
}
$$

以及：

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm P}).
}
$$

但本文不只停在禁止傳遞。更重要的是建立「合法可傳遞的部分」：例如一個 obstruction mechanism、local estimate、spectral decomposition、compactness lemma 或 route split，可以帶著明確 scope 作為 cross-domain transfer asset，只要其 transfer contract 說清楚什麼被保存、什麼被削弱、什麼被留下成 debt。

本文最後提出 **Cross-Domain Closure Ledger**：所有 transfer event 都必須記錄 source authority、target authority、invariant preservation、loss、debt、bridge、版本與可逆性，使跨域研究不再是模糊類比，而成為可稽核的 closure operation。

---

# 1. 研究定位

Paper 05 已建立：

$$
\mathfrak C^{\rm nat}
\xrightarrow{\Pi}
\mathcal V.
$$

本文處理另一種轉換：

$$
\boxed{
\mathfrak C_A
\xrightarrow{\mathcal T_{A\to B}}
\mathfrak C_B.
}
$$

這不是 view projection，而是 domain / representation / regime 之間的 closure transfer。

# 2. Domain

令 $A,B$ 表示兩個 closure domains。domain 可以差在 equation family、parameter family、solution notion、regularity class、boundary condition、dimension、geometry、representation、formal system、model interpretation 或 physical realization。

# 3. Transfer Operator

$$
\boxed{
\mathcal T_{A\to B}:
\mathfrak C_A
\rightharpoonup
\mathfrak C_B.
}
$$

使用部分映射 $\rightharpoonup$ 表示某些 object 可能沒有合法 image。

# 4. Transfer Object

可被 transfer 的 object：

$$
x_A\in
\{
\mathsf{Claim},
\mathsf{Lemma},
\mathsf{Route},
\mathsf{Obstruction},
\mathsf{Certificate},
\mathsf{Debt},
\mathsf{Frontier},
\mathsf{Cut},
\mathsf{Representation}
\}.
$$

# 5. Structure Transfer

如果只搬運 formal shape：

$$
x_A\mapsto x_B,
$$

稱 $\mathsf{StructureTransfer}$。

# 6. Authority Transfer

若連 theorem / closure authority 也搬運：

$$
\sigma_A(x)
\mapsto
\sigma_B(x'),
$$

稱 $\mathsf{AuthorityTransfer}$。

# 7. First Noncollapse

$$
\boxed{
\mathsf{StructureTransfer}
\neq
\mathsf{AuthorityTransfer}.
}
$$

# 8. Second Noncollapse

$$
\boxed{
\text{Formal similarity}
\neq
\text{Semantic transferability}.
}
$$

# 9. Third Noncollapse

$$
\boxed{
\text{Semantic transferability}
\neq
\text{Theorem-authority transferability}.
}
$$

# 10. Transfer Contract

$$
\boxed{
\mathsf{TContract}_{A\to B}
=
\left\langle
\mathsf{DomainMap},
\mathsf{ObjectMap},
\mathsf{InvariantMap},
\mathsf{StatusMap},
\mathsf{Bridge},
\mathsf{Loss},
\mathsf{Debt},
\mathsf{Version}
\right\rangle.
}
$$

# 11. Domain Map

 $\mathsf{DomainMap}_{A\to B}$ 說明 source domain、target domain、shared structure、changed structure、omitted structure 與 added structure。

# 12. Object Map

$$
\mathsf{ObjectMap}_{A\to B}(x_A)=x_B.
$$

若無合法 image：

$$
\boxed{
\mathcal T_{A\to B}(x_A)=\mathsf{UNDEFINED}.
}
$$

# 13. Invariant Map

$$
\mathsf{InvariantMap}_{A\to B}:
\mathfrak I_A\to\mathfrak I_B.
$$

# 14. Status Map

$$
\mathsf{StatusMap}_{A\to B}:
\sigma_A\rightharpoonup\sigma_B.
$$

status 可能保留、降格或 undefined。

# 15. Bridge

任何非平凡跨域 transfer 必須帶：

$$
\boxed{
\mathsf{BridgeCert}_{A\to B}.
}
$$

# 16. Loss

$$
\boxed{
\mathsf{Loss}_{A\to B}
}
$$

記錄 semantic、scope、assumption、representation、certificate 與 completeness loss。

# 17. Transfer Debt

若 transfer 後尚缺 uniformity、target fidelity、physical interpretation、solution compatibility 或 representation robustness，建立：

$$
\boxed{
\mathsf{Debt}_{A\to B}.
}
$$

# 18. Transfer Classes

$$
\tau_{\mathcal T}
\in
\{
\mathsf{CONSERVATIVE},
\mathsf{LOSSY},
\mathsf{NONTRANSFERABLE}
\}.
$$

# 19. Conservative Transfer

若 closure-critical invariants 全保存，且 authority transfer 有 theorem-level support：

$$
\boxed{
\mathsf{Conservative}_{A\to B}.
}
$$

# 20. Lossy Transfer

若只保存部分 structure：

$$
\boxed{
\mathsf{Lossy}_{A\to B}.
}
$$

target status 必降格。

# 21. Non-Transferable

若沒有合法 bridge：

$$
\boxed{
\mathsf{NonTransferable}_{A\to B}.
}
$$

不能以 analogy 取代 transfer proof。

# 22. Closure Conservation Profile

$$
\boxed{
\mathfrak K_{A\to B}
=
(
K_{\rm id},K_{\rm target},K_{\rm scope},K_{\rm asm},K_{\rm status},K_{\rm cert},K_{\rm debt},K_{\rm bridge},K_{\rm frontier},K_{\rm version}
).
}
$$

# 23. Identity Conservation

 $K_{\rm id}=1$ 表示 target object 可追溯回 source identity。

# 24. Target Conservation

 $K_{\rm target}=1$ 表示 formal target 沒有被偷偷換掉。

# 25. Scope Conservation

 $K_{\rm scope}=1$ 表示 source theorem 的量詞作用域在 target 中被合法保存。

# 26. Assumption Conservation

 $K_{\rm asm}=1$ 表示 target theorem 仍滿足 source assumptions，或 assumptions 有 certified translation。

# 27. Status Conservation

 $K_{\rm status}=1$ 表示 theorem-level closure status 可保持。

# 28. Certificate Conservation

 $K_{\rm cert}=1$ 表示 source certificate 在 target 中仍可驗證或有 target-side reconstruction。

# 29. Debt Conservation

Debt 不是應保持數值不變的量，但 transfer 必須：

$$
\boxed{
\mathsf{Debt}_B
\supseteq
\mathsf{MappedDebt}_A.
}
$$

不得消失。

# 30. Bridge Conservation

跨 multiple transfers 時，bridge lineage 必須保留。

# 31. Frontier Conservation

source frontier 映射後，target 可能出現額外 frontier。因此：

$$
\boxed{
\mathcal T(\partial_A^\ast)
\subseteq
\partial_B^\ast
}
$$

最多是候選關係，不保證等號。

# 32. Version Conservation

所有 transfer conclusion 必標 $(\nu_A,\nu_B)$。

# 33. Strong Conservation

若 $K_i=1$ 對 declared invariant family 全成立，稱 strong conservative transfer。

# 34. Partial Conservation

若只保存 subset：

$$
\mathfrak K'\subsetneq\mathfrak K,
$$

則 authority 必 purpose-relative。

# 35. Transfer Authority Level

$$
\mathsf{TAuthority}
\in
\{
\mathsf{ANALOGY},
\mathsf{STRUCTURE},
\mathsf{LEMMA},
\mathsf{OBSTRUCTION},
\mathsf{THEOREM},
\mathsf{DOMAIN}
\}.
$$

# 36. Analogy Authority

最低層：形式相似，可作研究啟發，不能封路。

# 37. Structure Authority

可搬運 graph pattern、operator decomposition、proof skeleton，但不能搬 theorem truth。

# 38. Lemma Authority

若 lemma assumptions 在 target 中完整成立，可 transfer lemma。

# 39. Obstruction Authority

若 obstruction propagation contract 在 target 中 PASS，才可封 target route。

# 40. Theorem Authority

若 theorem statement、scope、assumptions、proof object 全部 transfer-valid，可保持 theorem status。

# 41. Domain Authority

最高級：整個 source closure conclusion 對 target domain 仍成立，要求最強。

# 42. Authority Ladder

$$
\boxed{
\mathsf{ANALOGY}
\prec
\mathsf{STRUCTURE}
\prec
\mathsf{LEMMA}
\prec
\mathsf{OBSTRUCTION}
\prec
\mathsf{THEOREM}
\prec
\mathsf{DOMAIN}.
}
$$

# 43. Authority Cannot Jump

禁止 $\mathsf{ANALOGY}\to\mathsf{THEOREM}$ 無證跳級。

# 44. Transfer as Typed Promotion

每次 authority 升級都需要：

$$
\boxed{
\mathsf{PromotionCert}.
}
$$

# 45. Representation Transfer

若 $\rho_1\to\rho_2$ 只是 representation change，不應改 mathematical identity。

# 46. Representation-Equivalent Transfer

若有：

$$
\mathsf{RepEquivCert}_{\rho_1\leftrightarrow\rho_2},
$$

則 theorem authority 可保留。

# 47. Representation-Sensitive Search

即使 theorem identity 不變，search success rate 可不同。因此：

$$
\boxed{
\text{mathematical conservation}
\neq
\text{search-behavior conservation}.
}
$$

# 48. Search-Regime Transfer

從 prover / model / method family $R_1$ 到 $R_2$：

$$
\mathcal T_{R_1\to R_2}.
$$

研究失敗不可自動 transfer。

# 49. Failure Nontransfer

$$
\boxed{
\operatorname{Fail}_{R_1}(Q)
\not\Rightarrow
\operatorname{Fail}_{R_2}(Q).
}
$$

# 50. Proof Transfer

若 proof object 可在 target formal system replay，則可建立 proof transfer cert。

# 51. Formal-System Transfer

$$
\mathcal T_{\mathcal F_1\to\mathcal F_2}
$$

需要 syntax / semantics / axiom / theorem bridge。

# 52. Conservative Formal Translation

若 source proof 在 target system 保持 theorem semantics：

$$
\boxed{
\mathsf{ConservativeFormalTransfer}.
}
$$

# 53. Non-Conservative Formal Translation

若 target 新 axioms 使 theorem 變容易，不能回推 source。

# 54. Transfer Directionality

一般：

$$
\boxed{
\mathcal T_{A\to B}
\neq
\mathcal T_{B\to A}.
}
$$

# 55. Transfer Inversion

只有有 inverse transfer cert 才可雙向。

# 56. Transfer Composition

$$
\mathcal T_{A\to C}
\stackrel{?}{=}
\mathcal T_{B\to C}\circ\mathcal T_{A\to B}.
$$

不自動成立。

# 57. Transfer Composition Certificate

$$
\boxed{
\mathsf{TCompCert}_{A\to B\to C}.
}
$$

# 58. Composition Loss

即使兩段各自合法， $\mathsf{Loss}_{A\to C}$ 可能大於單段 loss 的簡單相加。

# 59. Nontransitive Transfer

 $A\to B$ 且 $B\to C$ 不保證 $A\to C$。

# 60. Transfer Coherence

多條 transfer path 到同一 target 時，應檢查 target status 是否 coherent。

# 61. Coherence Failure

若兩條 path 產生不同 authority / scope，標：

$$
\boxed{
\mathsf{TRANSFER\_COHERENCE\_DEBT}.
}
$$

# 62. Transfer Ledger

每個 transfer event：

$$
e_{\mathcal T}
=
\left\langle
A,B,x_A,x_B,\mathfrak K,\mathsf{Loss},\mathsf{Debt},\mathsf{Cert},\nu
\right\rangle.
$$

# 63. Transfer Replay

跨域 closure conclusion 必可由 transfer ledger 重放。

# 64. Transfer Diff

不同 transfer policy 可比較：

$$
\Delta\mathcal T.
$$

# 65. Scope Transfer

從 scope $D_0$ 到 $D_1$，若 $D_1$ 更廣，通常是 promotion，不是 conservation。

# 66. Scope Narrowing

從廣到窄通常較容易 conservative。

# 67. Scope Widening

從窄到廣需要：

$$
\boxed{
\mathsf{UniformityCert}
}
$$

或其他 globality bridge。

# 68. Parameter Transfer

若 theorem 對 $\theta=\theta_0$ 成立，不自動 transfer 到 $\theta\in\Theta$。

# 69. Uniformity Debt

$$
\boxed{
\mathsf{Debt}_{\rm uniform}
}
$$

是最常見 cross-parameter debt。

# 70. Dimension Transfer

2D theorem 不自動 transfer 3D。

# 71. Geometry Transfer

periodic domain、whole space、bounded domain 之間都需要 boundary / function-space bridge。

# 72. Boundary Transfer

boundary condition 改變可能改變 energy identity、spectrum、pressure representation、compactness 與 regularity。

# 73. Solution-Notion Transfer

weak solution、mild solution、strong solution、ancient solution 等不可混用。

# 74. Regularity Transfer

從 $H^s$ 到 $C^\alpha$ 需要 embedding / regularity theorem。

# 75. Operator Transfer

formal operator 可在 domain change 後保留 algebraic form，但 analytic properties 可能改變。

# 76. Estimate Transfer

一個 estimate 的 constant 可能依 domain / parameter 爆炸。因此：

$$
\boxed{
\text{same inequality form}
\neq
\text{uniform transferable estimate}.
}
$$

# 77. Obstruction Transfer

source obstruction $O_A$ 只有在 target：

$$
\mathsf{OPCert}_B(O_B\to R_B)=\mathsf{PASS}
$$

時才可封路。

# 78. Obstruction Downgrade

若 source 是 FORMAL_NO_GO，但 target 只保留部分 assumptions，可降為 DIAGNOSTIC 或 CONDITIONAL_NO_GO。

# 79. Survivor Transfer

source survivor 不代表 target survivor。

# 80. Survivor Lift

只有當 target 新 constraints 不封 route 時，才可 transfer survivor。

# 81. Frontier Transfer

source minimal survivor 可變成 target 的 survivor、blocked、irrelevant、split frontier 或 undefined。

# 82. Cut Transfer

source cut $C_A$ 不自動是 target cut。需要：

$$
\boxed{
\mathsf{CutTransferCert}_{A\to B}.
}
$$

# 83. Cover Transfer

source obstruction cover 到 target 必重新檢查 uncovered route classes。

# 84. Exhaustion Transfer

$$
\mathsf{EXH}_{k,A}
$$

不自動 transfer 到 $\mathsf{EXH}_{k,B}$。

# 85. Exhaustion Downgrade by Transfer

跨域後常見：

$$
\mathsf{EXH}_{3,A}
\to
\mathsf{EXH}_{1,B}
$$

或只保留 structure-level conclusion。

# 86. Debt Transfer Law

source debt 不能消失。target 還可能新增：

$$
\mathsf{Debt}_B
=
\mathsf{MappedDebt}_A
\cup
\mathsf{NewTransferDebt}.
$$

# 87. Debt Cancellation No-Go

除非 target theorem 真正 discharge source debt，不能因 domain change 把 debt 刪掉。

# 88. Certificate Transfer

source certificate 可以 replay、translate、wrap 或 invalidate。

# 89. Certificate Replay

若 target 系統可直接重驗 source proof，這是最強 transfer。

# 90. Certificate Translation

若 proof language 不同，可做 verified translation。

# 91. Certificate Wrapping

若 source theorem 作 target assumption，只能保留 source authority，不等於 target theorem proof。

# 92. Certificate Invalidation

若 target assumptions 不滿足，source cert 只能保留歷史價值。

# 93. Conservative Extension

若 target theory 是 source 的 conservative extension，source theorem status 可保留。

# 94. Nonconservative Extension

若 target 加強 axioms，target proof 不能反推 source。

# 95. Closure Conservation Law Candidate

在某 conservative transfer family 中，可以研究：

$$
\boxed{
\sigma_A(x)
=
\sigma_B(\mathcal T(x)).
}
$$

這是 status conservation law candidate。

# 96. Closure Monotonicity Candidate

若 $B$ 是 restriction of $A$，可能有 closure authority 從 $A$ 向 $B$ 保留，但仍需 theorem-specific 檢查。

# 97. Closure Quantity Warning

本文不主張存在 universal scalar $E_{\rm closure}$ 像物理能量般全域守恆。

# 98. Conservation Is Typed

本文「守恆」是指定 invariant family 在指定 transfer contract 下保持，不是一個神秘總量。

# 99. Conservative Transfer Invariant

$$
\boxed{
\mathcal T^\ast(\mathfrak I_B)=\mathfrak I_A
}
$$

是可能的形式化方向之一。

# 100. Loss Profile

$$
\boxed{
\mathbf L_{A\to B}
=
(
L_{\rm scope},L_{\rm asm},L_{\rm cert},L_{\rm rep},L_{\rm completeness},L_{\rm interpretation}
).
}
$$

# 101. Zero Loss

 $\mathbf L=0$ 是 conservative candidate。

# 102. Partial Loss

若 $\mathbf L\neq0$，authority 必降格或附 debt。

# 103. Irreversible Transfer

如果 loss 無法 reconstruct，稱 irreversible transfer。

# 104. Reversible Transfer

若存在 $\mathcal T^{-1}$ 使 closure-equivalent recovery，稱 reversible。

# 105. Reversible Structure vs Authority

structure 可逆仍不代表 theorem authority 可逆。

# 106. Cross-Domain Closure Graph

將 domain 當 node：

$$
\boxed{
\mathcal G_D=(V_D,E_{\mathcal T}).
}
$$

# 107. Domain Node

例如：

$$
\mathfrak N_{\rm C},
\quad
\mathfrak N_{\rm G}^{\Sigma},
\quad
\mathfrak N_{\rm P}.
$$

# 108. Domain Edge

每條 $A\xrightarrow{\mathcal T}B$ 帶 transfer type、authority level、invariants、loss、debt、cert 與 version。

# 109. Domain SCC Warning

即使 domain graph 形成 strongly connected component，也不表示 domains theorem-equivalent。

# 110. Bidirectional Bridge

只有雙向 theorem-level conservative transfer 才可能支持 stronger equivalence claim。

# 111. NS Formal Domain

$$
\boxed{
\mathfrak N_{\rm C}
}
$$

為指定 formal NS target family。

# 112. NS Generalized Domain

$$
\boxed{
\mathfrak N_{\rm G}^{\Sigma}
}
$$

必須先宣告 signature $\Sigma$。

# 113. NS Physical Domain

$$
\boxed{
\mathfrak N_{\rm P}
}
$$

包含 model-to-world interpretation、measurement 與 physical applicability。

# 114. Formal-to-Generalized Transfer

$$
\mathcal T_{\rm C\to G}.
$$

最安全地先視為：

$$
\boxed{
\text{special-case embedding}.
}
$$

# 115. Special-Case Anchor

若 $\mathfrak N_{\rm C}$ 是 $\mathfrak N_{\rm G}^{\Sigma}$ 的一個合法 member，formal theorem 可成為 generalized family 的一個 case。但：

$$
\boxed{
\text{one case}
\neq
\text{family theorem}.
}
$$

# 116. Generalized-to-Formal Restriction

若 generalized theorem 真正涵蓋 formal NS，則可 restriction 到 formal domain。

# 117. Formal-to-Physical Transfer

$$
\mathcal T_{\rm C\to P}
$$

需要 model interpretation bridge。

# 118. Mathematical Truth vs Physical Adequacy

$$
\boxed{
\text{formal theorem correctness}
\neq
\text{physical model adequacy}.
}
$$

# 119. Physical-to-Formal Feedback

實驗可能提示 model discrepancy、parameter correction、missing mechanism，但不能直接改 formal theorem truth。

# 120. Physical Feedback Event

可生成：

$$
\boxed{
\mathsf{MODEL\_REVISION\_CANDIDATE}
}
$$

而不是 theorem refutation。

# 121. Generalized-to-Physical Transfer

$$
\mathcal T_{\rm G\to P}
$$

需要 parameter identification、observables、scale mapping、physical validity regime。

# 122. NS Three-Domain Firewall

$$
\boxed{
\mathfrak N_{\rm C}
\neq
\mathfrak N_{\rm G}^{\Sigma}
\neq
\mathfrak N_{\rm P}.
}
$$

# 123. NS Transfer Triangle

$$
\boxed{
\begin{array}{ccc}
&\mathfrak N_{\rm G}^{\Sigma}&\\
\swarrow&&\searrow\\
\mathfrak N_{\rm C}&&\mathfrak N_{\rm P}
\end{array}
}
$$

每條 edge 有不同 bridge semantics。

# 124. Clay Theorem Transfer Limit

即使 Clay formal problem 被解：

$$
\mathsf{CLOSED}^{+}_{\mathfrak N_{\rm C}},
$$

最多直接得到 formal-domain closure。

# 125. Generalized Family Debt

要升到：

$$
\mathsf{CLOSED}^{+}_{\mathfrak N_{\rm G}^{\Sigma}}
$$

需要 equation-family uniformity / signature completeness。

# 126. Physical Domain Debt

要升到：

$$
\mathsf{CLOSED}^{+}_{\mathfrak N_{\rm P}}
$$

需要 model-to-world adequacy，不只是 PDE proof。

# 127. NS Obstruction Transfer Example

若 formal NS 中某 scalar additive budget 被證明不足，它可以作 generalized family 的 method-level warning，但不能自動變成 generalized global no-go。

# 128. NS Spectral Lemma Transfer Example

某 Fourier / Riesz lemma 若 target family 保留相同 operator structure，可 transfer lemma。

# 129. NS Ancient-Profile Transfer Example

ancient solution rigidity 結果若 target equation family 改 nonlinear term，通常不能直接 transfer theorem authority。

# 130. NS Survivor Transfer Example

DCRP survivor 可作 generalized mechanism candidate，但不是 generalized blow-up existence proof。

# 131. Cross-Series Transfer

X72、C6、DCRP 之間也可視為 subdomain / representation transfer。

# 132. Series Transfer Contract

每個 cross-series merge 需要：

$$
\boxed{
\mathsf{SeriesTContract}.
}
$$

# 133. Same Word No Transfer

兩系列都用 carrier 不代表同一 object。

# 134. Same Equation No Full Transfer

即使都研究同一 NS equation，不同 route scope / assumptions 也可使 obstruction 不可直接 transfer。

# 135. Transfer Firewall for NO-GO

$$
\boxed{
\text{NO-GO}_A
\not\Rightarrow
\text{NO-GO}_B
}
$$

除非 OPCert + TContract 都 PASS。

# 136. Transfer Firewall for SURVIVOR

$$
\boxed{
\text{SURVIVOR}_A
\not\Rightarrow
\text{SURVIVOR}_B.
}
$$

# 137. Transfer Firewall for CLOSED

$$
\boxed{
\mathsf{CLOSED}_A
\not\Rightarrow
\mathsf{CLOSED}_B.
}
$$

# 138. Transfer Firewall for EXHAUSTION

$$
\boxed{
\mathsf{EXH}_{k,A}
\not\Rightarrow
\mathsf{EXH}_{k,B}.
}
$$

# 139. Transfer Firewall for FIXED POINT

$$
\boxed{
\mathfrak C_A^\star
\not\Rightarrow
\mathfrak C_B^\star.
}
$$

# 140. Transfer Frontier

定義跨域 transfer 後新增 frontier：

$$
\boxed{
\partial_{\mathcal T}
=
\partial_B^\ast
\setminus
\mathcal T(\partial_A^\ast).
}
$$

# 141. Transfer-Induced Frontier

這些是 source domain 不存在、但 target domain 新出現的 obligations。

# 142. Transfer-Induced Debt

$$
\boxed{
\mathsf{Debt}_{\mathcal T}
=
\mathsf{Debt}_B
\setminus
\mathsf{MappedDebt}_A.
}
$$

# 143. Conservative Transfer Test

若 target statement 對齊、scope preserved、assumptions preserved、cert replayable、no new frontier、no new debt，則 conservative candidate。

# 144. Lossy Transfer Test

若 structure 可搬但 scope narrower、cert not replayable、new debt 出現，則 lossy。

# 145. Nontransferability Test

若 target semantics 無可靠 mapping：

$$
\boxed{
\mathcal T=\mathsf{UNDEFINED}.
}
$$

# 146. Transfer Validation Stack

$$
\boxed{
\mathsf{TVStack}
=
(
\mathsf{Semantic},
\mathsf{Scope},
\mathsf{Assumption},
\mathsf{Representation},
\mathsf{Certificate},
\mathsf{Authority},
\mathsf{Debt}
).
}
$$

# 147. Transfer Staleness

source theorem 或 bridge revision 時，target transfer cert 進 $\mathsf{STALE}$。

# 148. Transfer Revalidation

跨域 transfer 需要 version-aware replay。

# 149. Transfer Reopening Wave

若 high-centrality source theorem 被修訂，所有 target descendants 也可能 reopen。

# 150. Cross-Domain Reopening

$$
\boxed{
W_{\rm reopen}^{A\to B}
}
$$

衡量 transfer lineage 造成的 reopening mass。

# 151. Transfer Fragility

高 authority transfer 若依賴少數 fragile bridges，需標高 fragility。

# 152. Transfer Robustness

若多種 independent bridge / representation 都支持同一 transfer，可提高 robustness。

# 153. Robustness Not Truth

$$
\boxed{
\text{transfer robustness}
\neq
\text{absolute truth}.
}
$$

# 154. Closure Transfer Fixed Point

若 repeated transfer / revalidation 後 target status 穩定，可稱 transfer-relative fixed point。

# 155. Transfer Fixed Point Nonclaim

它不表示 domains globally equivalent。

# 156. Transfer Cycle

$$
A\to B\to C\to A
$$

可能形成 transfer cycle。

# 157. Cycle Consistency

若回到 $A$ 後 authority / scope 改變，表示 cycle 有 loss 或 gain。

# 158. Authority Gain No-Go

無證情況下：

$$
\boxed{
\text{cycle cannot create theorem authority from nothing}.
}
$$

# 159. Authority Conservation Principle

對 conservative cycle：

$$
\boxed{
\mathsf{Authority}_{\rm out}
=
\mathsf{Authority}_{\rm in}.
}
$$

# 160. Debt Conservation Principle

跨 cycle：

$$
\boxed{
\mathsf{Debt}_{\rm out}
\supseteq
\mathsf{MappedDebt}_{\rm in}
}
$$

除非有 explicit discharge。

# 161. Machine Record — Transfer Contract

```yaml
transfer_contract:
  transfer_id:
  source_domain:
  target_domain:
  transfer_type:
  authority_level:
  domain_map:
  object_map:
  preserved_invariants: []
  lost_invariants: []
  bridge_certificate:
  transfer_debt_ids: []
  version:
  status:
```

# 162. Machine Record — Conservation Profile

```yaml
conservation_profile:
  transfer_id:
  identity: PASS
  target: PASS
  scope:
  assumptions:
  status:
  certificate:
  debt:
  bridge:
  frontier:
  version:
```

# 163. Machine Record — Transfer Event

```yaml
transfer_event:
  event_id:
  transfer_id:
  source_object_id:
  target_object_id:
  source_status:
  target_status:
  authority_before:
  authority_after:
  loss_profile:
  debt_added: []
  debt_discharged: []
  provenance:
  version:
```

# 164. Machine Record — NS Transfer Triangle

```yaml
ns_transfer_triangle:
  formal_domain: N_C
  generalized_domain: N_G_Sigma
  physical_domain: N_P
  edges:
    - formal_to_generalized
    - generalized_to_formal
    - formal_to_physical
    - physical_to_formal_feedback
    - generalized_to_physical
  all_edges_require_certificates: true
```

# 165. Validation Scenario A — Conservative restriction

廣 domain theorem restriction 到較窄 domain。expected: theorem authority preserved。

# 166. Validation Scenario B — Invalid widening

single parameter theorem 擴張全 parameter family。expected: uniformity debt，THEOREM transfer FAIL。

# 167. Validation Scenario C — Representation equivalence

verified representation equivalence。expected: theorem status preserved。

# 168. Validation Scenario D — Search failure transfer

one prover failed。expected: failure does not transfer。

# 169. Validation Scenario E — Obstruction downgrade

formal no-go assumptions target 不完整。expected: downgrade to diagnostic/conditional。

# 170. Validation Scenario F — Cut transfer

source cut 在 target 有新 routes。expected: CutTransferCert FAIL。

# 171. Validation Scenario G — Exhaustion transfer

source EXH3，target route grammar 更廣。expected: downgrade / new completeness debt。

# 172. Validation Scenario H — Formal NS to generalized NS

formal theorem as special case anchor。expected: STRUCTURE/THEOREM-on-subcase，not DOMAIN theorem。

# 173. Validation Scenario I — Formal NS to physical NS

formal theorem transferred to model interpretation。expected: physical adequacy debt。

# 174. Validation Scenario J — Physical feedback

experiment suggests missing mechanism。expected: model revision candidate，not theorem refutation。

# 175. Validation Scenario K — Cross-series NO-GO

same label, different scope。expected: no merge without SeriesTContract。

# 176. Validation Scenario L — Transfer cycle

authority after cycle exceeds input without discharge/promote cert。expected: FAIL。

# 177. Core No-Go 1

$$
\boxed{
\text{same equation form}
\not\Rightarrow
\text{same closure domain}.
}
$$

# 178. Core No-Go 2

$$
\boxed{
\text{same operator}
\not\Rightarrow
\text{same analytic theorem}.
}
$$

# 179. Core No-Go 3

$$
\boxed{
\text{same proof skeleton}
\not\Rightarrow
\text{same theorem authority}.
}
$$

# 180. Core No-Go 4

$$
\boxed{
\text{same obstruction name}
\not\Rightarrow
\text{same obstruction class}.
}
$$

# 181. Core No-Go 5

$$
\boxed{
\text{source closure}
\not\Rightarrow
\text{target closure}.
}
$$

# 182. Core No-Go 6

$$
\boxed{
\text{source exhaustion}
\not\Rightarrow
\text{target exhaustion}.
}
$$

# 183. Core No-Go 7

$$
\boxed{
\text{formal theorem}
\not\Rightarrow
\text{physical law proof}.
}
$$

# 184. Core No-Go 8

$$
\boxed{
\text{special-case theorem}
\not\Rightarrow
\text{family theorem}.
}
$$

# 185. Paper 06 核心命題一

## Conservative Transfer Principle

若 target statement、scope、assumptions、certificate、representation semantics 與 version 均被保存，則 source theorem authority 可在 target 中保持。

# 186. Paper 06 核心命題二

## Lossy Transfer Downgrade Principle

若 transferable structure 存在但 closure-critical invariant 有 loss，則 target authority 必降格，並建立 transfer debt。

# 187. Paper 06 核心命題三

## Debt Persistence Principle

跨域 transfer 不得使 unresolved debt 無證消失。

# 188. Paper 06 核心命題四

## Cross-Domain Frontier Expansion Principle

即使 source closure complete，target domain 也可能因新增 scope / model / representation obligations 產生新的 frontier。

# 189. Paper 06 核心命題五

## Authority Noncreation Principle

transfer composition / cycle 不得在沒有 explicit theorem / promotion certificate 的情況下增加 closure authority。

# 190. Paper 06 核心命題六

## NS Three-Domain Separation Principle

formal NS、generalized NS-like family、physical NS realization 必須以 typed transfer bridge 連接，不得以「都是 NS」為理由做 closure collapse。

# 191. 與 Paper 00–05 的整合

Paper 00：relative-global closure object。  
Paper 01：domain / globality typing。  
Paper 02：obstruction propagation。  
Paper 03：frontier / cut / exhaustion。  
Paper 04：versioned dynamics / reopening。  
Paper 05：projection / invariant preservation。  
Paper 06：cross-domain transfer / conservation / authority。

# 192. 與 UCT 的關係

UCT 的 Bridge Theory 在本文被具體化為 mathematical closure transfer laws，但 CSM 不把所有 bridge 強制還原成同一 formalism。

# 193. 與 LSI-PSD 的關係

LSI-PSD 提供 representation sensitivity、route quotient、obstruction confluence。本文要求這些跨 series / domain 的合併都必通過 transfer contract。

# 194. 與一般 category / logic translation 的關係

本文可使用 institution morphism、functor、interpretation、conservative extension 等工具作 backend。CSM 不宣稱發明這些一般形式。

# 195. CSM 的新增焦點

新增焦點是：

$$
\boxed{
\text{closure authority itself becomes a typed transferable resource}.
}
$$

並且：

$$
\boxed{
\text{loss and debt travel with the transfer}.
}
$$

# 196. Paper 07 路線

下一篇應處理：

$$
\boxed{
\textbf{Closure Calculus, Composition Rules, and Proof-Carrying Operators}
}
$$

也就是把 Papers 00–06 的 object、closure、transfer、projection、reopening、debt、certificate 收斂成更緊的運算 calculus：operator signatures、legal composition、proof-carrying closure operators、algebraic normal forms、no-go composition、runtime-executable semantics、NS closure graph compiler interface。

# 197. 結論

一個大型數學研究體系不可能永遠只存在單一 domain。我們會不斷換 representation、function space、equation family、parameter regime，從 formal mathematics 走向 model interpretation，從 local theorem 走向 generalized family。

真正危險的不是 transfer 本身，而是無證 transfer。

因此 CSM 將 cross-domain reuse 改寫成：

$$
\boxed{
\text{typed transfer}
+
\text{invariant conservation}
+
\text{authority control}
+
\text{loss accounting}
+
\text{debt propagation}.
}
$$

最重要的原則是：

$$
\boxed{
\text{Transferable Structure}
\neq
\text{Transferable Closure Authority}.
}
$$

而對 Navier--Stokes：

$$
\boxed{
\mathfrak N_{\rm C}
\neq
\mathfrak N_{\rm G}^{\Sigma}
\neq
\mathfrak N_{\rm P}.
}
$$

formal NS 被證明，仍只直接關閉 formal target；generalized family 與 physical realization 需要自己的 bridge、scope、uniformity 與 interpretation obligations。

另一方面，formal NS 中累積的 lemma、obstruction、route decomposition、spectral structure、negative result 與 proof asset 也不必因此被困在單一 domain。只要 transfer contract 足夠清楚，它們可以合法成為其他 domain 的研究資產，而不被誇大為相同 theorem。

這使 CSM 真正做到：

$$
\boxed{
\text{reuse without collapse,
transfer without authority inflation,
and generalize without erasing debt}.
}
$$

---

## 附錄 A — Paper 06 核心不變量

1. structure transfer 不等於 authority transfer；
2. analogy 不等於 semantic transfer；
3. semantic transfer 不等於 theorem transfer；
4. conservative transfer 必須保存 closure-critical invariants；
5. lossy transfer 必須降格 authority；
6. nontransferable mapping 不得以 analogy 替代；
7. debt 不得跨域消失；
8. transfer composition 不保證 transitive；
9. transfer cycle 不得無證創造 authority；
10. source cut 不等於 target cut；
11. source exhaustion 不等於 target exhaustion；
12. formal theorem 不等於 physical adequacy proof；
13. special case 不等於 family theorem；
14. transfer certificate 必須 versioned；
15. target 可因 transfer 產生新增 frontier。

---

## 附錄 B — 系列依賴

### Paper 00
- Relative-Global Closure Space

### Paper 01
- Domain / Globality Typing

### Paper 02
- Typed Closure Graph / Obstruction

### Paper 03
- Frontier / Cut / Exhaustion

### Paper 04
- Dynamic Versioning / Reopening

### Paper 05
- Projection / Invariant Preservation

### Paper 06
- Transfer Laws
- Closure Conservation
- Authority Transfer
- Cross-Domain Invariance
- NS Three-Domain Transfer Triangle

---

**END OF CSM PAPER 06 v0.1**
