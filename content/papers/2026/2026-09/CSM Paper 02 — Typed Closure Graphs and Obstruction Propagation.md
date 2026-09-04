# CSM Paper 02 — Typed Closure Graphs and Obstruction Propagation

## 閉包空間數學論：型別閉包圖、阻斷傳播、重開與前沿收縮

**English Title:** *Closure-Space Mathematics: Typed Closure Graphs, Obstruction Propagation, Reopening, and Frontier Contraction*  
**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 02  
**Version:** v0.1  
**Date:** 2026-08-27  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** zh-TW  
**Status:** Formal Theory / Graph-Operational Core  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline ` $...$ `; display `$$...$$`

---

## 摘要

本文建立閉包空間數學論（Closure-Space Mathematics, CSM）的第一個圖論運算核心。Paper 00 已將研究中的命題、路徑、障礙、證書、前沿、債務與帳本組織為相對全域閉包空間；Paper 01 進一步將「全域」拆成量詞作用域與 domain typing，禁止從較窄作用域無證升格到較廣作用域。本文現在處理下一個核心問題：

> 一個大型數學問題中，如何把「這條路被堵住」「這個分支已證明」「這個條件命題成立」「這個障礙只在某些 assumptions 下有效」「後續新 bridge 使舊死路重新開放」全部表示為同一個可稽核圖論系統？

本文主張，普通有向圖不足以承載成熟 proof-space closure。真正需要的是一個帶型別、帶作用域、帶證書、允許多前提、多輸出、條件化與版本化的 **typed directed hypergraph**。在此圖上，我們分別定義：

1. implication closure；
2. equivalence quotient closure；
3. conditional closure；
4. obstruction propagation closure；
5. bridge-mediated closure；
6. reopening operator；
7. frontier contraction operator；
8. debt propagation；
9. closure ledger；
10. relative route-exhaustion certificate。

本文的核心非坍縮原則是：

$$
\boxed{
\mathsf{RouteBlocked}
\neq
\mathsf{ClaimRefuted}
\neq
\mathsf{BranchClosed}
\neq
\mathsf{DomainClosed}.
}
$$

一個 obstruction 只有在其 assumption、scope、representation、bridge 與 target fidelity 全部匹配時，才允許沿合法依賴邊傳播。任何跨作用域、跨表示、跨方程族、跨模型類的 obstruction promotion 都必須附帶傳播證書；否則只能形成局部 blocked state，而不能升格為 theorem-level no-go。

另一方面，CSM 不把 closure 視為永遠單調。當舊 assumption 被移除、新 representation 出現、新 bridge 被證明、obstruction 被限縮、counterexample 被撤銷或 parent theorem 被修訂時，先前 blocked 的 route 可以合法重新成為 OPEN。因此本文引入 **Reopening Operator** 與 **Versioned Closure Ledger**，使 proof-space closure 成為可回放、可修正、可局部逆轉的動態圖演化。

本文最後提出 NS 相對全域閉包圖的最小實例化規則：過去 C1--C6、X72、DCRP、MORP、RFP、FCBP 與其他 proof families 中的 `NO-GO`、`OPEN`、`SURVIVOR`、`CONDITIONAL`、`CLOSED` 不再只是文件標籤，而被編譯成 typed nodes、hyperedges、obstruction certificates 與 frontier states。這使未來「一步一步封住命題」不再是一種研究敘事，而可以成為一個明確的圖論閉包程序。

---

# 1. 研究定位

本文不重新定義 CSM 的全部本體。Paper 00 已建立：

$$
\mathfrak C
=
\left\langle
D,
V,
E,
\tau_V,
\tau_E,
\sim,
\preceq,
\sigma,
\mathfrak O,
\partial\mathfrak C,
\mathsf{Cert},
\mathsf{Debt},
\mathsf{Ledger}
\right\rangle.
$$

Paper 01 已建立 scope contract 與 globality typing。

本文專注於：

$$
\boxed{
\text{如何讓 }\mathfrak C
\text{ 真正執行 closure operations。}
}
$$

---

# 2. 為什麼普通 directed graph 不夠

典型數學推導不是：

$$
A\to B.
$$

而常是：

$$
A_1,\ldots,A_k
\Longrightarrow
B_1,\ldots,B_m.
$$

例如一個 obstruction 可能要求：

$$
A_{\rm regularity}
\land
A_{\rm symmetry}
\land
A_{\rm scale}
\land
A_{\rm boundary}
$$

才推出：

$$
\neg R.
$$

因此 CSM 的 primitive edge 必須允許：

$$
e:
\{v_1,\ldots,v_k\}
\longrightarrow
\{w_1,\ldots,w_m\}.
$$

本文以 directed hyperedge 為基本關係單位。

---

# 3. Typed Closure Hypergraph

定義 CSM 閉包超圖：

$$
\boxed{
\mathcal H_{\rm CSM}
=
(V,E,\tau_V,\tau_E,\sigma,\lambda,\pi,\chi,\nu).
}
$$

其中：

- $V$：節點集合；
- $E$：directed hyperedge 集合；
- $\tau_V$：節點型別；
- $\tau_E$：邊型別；
- $\sigma$：epistemic / closure status；
- $\lambda$：scope label；
- $\pi$：provenance；
- $\chi$：certificate metadata；
- $\nu$：版本資訊。

---

# 4. 節點型別

最小 node type family 定義為：

$$
\tau_V(v)
\in
\{
\mathsf{Problem},
\mathsf{Claim},
\mathsf{Assumption},
\mathsf{Lemma},
\mathsf{RouteState},
\mathsf{Obstruction},
\mathsf{Bridge},
\mathsf{Certificate},
\mathsf{Counterexample},
\mathsf{Domain},
\mathsf{Scope},
\mathsf{Representation},
\mathsf{Frontier},
\mathsf{Debt},
\mathsf{Revision}
\}.
$$

不是所有節點都能互相直接連邊。

---

# 5. 邊型別

最小 edge type family：

$$
\tau_E(e)
\in
\{
\mathsf{IMPLIES},
\mathsf{DEPENDS},
\mathsf{ASSUMES},
\mathsf{REFINES},
\mathsf{EQUIV},
\mathsf{BLOCKS},
\mathsf{REFUTES},
\mathsf{BRIDGES},
\mathsf{REOPENS},
\mathsf{GENERALIZES},
\mathsf{SPECIALIZES},
\mathsf{LIFTS},
\mathsf{PROJECTS},
\mathsf{CERTIFIES},
\mathsf{WEAKENS},
\mathsf{STRENGTHENS},
\mathsf{REVISES},
\mathsf{INHERITS}
\}.
$$

任何 edge type 都必須有 source/target type signature。

---

# 6. Edge Signature

令：

$$
\operatorname{sig}(e)
=
\left(
\tau_V(\operatorname{src}(e)),
\tau_E(e),
\tau_V(\operatorname{tgt}(e))
\right).
$$

若 edge 不符合其 signature，則：

$$
\boxed{
e\notin E_{\rm legal}.
}
$$

例如：

$$
\mathsf{Obstruction}
\xrightarrow{\mathsf{BLOCKS}}
\mathsf{RouteState}
$$

合法。

但：

$$
\mathsf{Representation}
\xrightarrow{\mathsf{REFUTES}}
\mathsf{Claim}
$$

若沒有 theorem-level counterexample bridge，則不合法。

---

# 7. Closure Status

節點 status：

$$
\sigma(v)
\in
\{
\mathsf{OPEN},
\mathsf{CLOSED}^{+},
\mathsf{CLOSED}^{-},
\mathsf{BLOCKED},
\mathsf{CONDITIONAL},
\mathsf{UNKNOWN},
\mathsf{STALE},
\mathsf{REOPENED}
\}.
$$

其中：

$$
\mathsf{CLOSED}^{+}
$$

表示正向證成。

$$
\mathsf{CLOSED}^{-}
$$

表示 theorem-level refutation 或 certified counterexample。

$$
\mathsf{BLOCKED}
$$

表示 route 在目前 scope/assumption/regime 下不能繼續。

---

# 8. 第一非坍縮原則

$$
\boxed{
\mathsf{BLOCKED}
\neq
\mathsf{CLOSED}^{-}.
}
$$

若一條 proof route 被 estimate barrier 阻斷，只能得到：

$$
\sigma(R)=\mathsf{BLOCKED}.
$$

不能得到：

$$
\sigma(Q)=\mathsf{CLOSED}^{-}.
$$

---

# 9. 第二非坍縮原則

$$
\boxed{
\mathsf{BranchClosed}
\neq
\mathsf{ProblemClosed}.
}
$$

一個 route family：

$$
B_i
$$

全部 blocked，不代表：

$$
Q
$$

已無其他 admissible route family。

---

# 10. 第三非坍縮原則

$$
\boxed{
\mathsf{LocalObstruction}
\neq
\mathsf{GlobalObstruction}.
}
$$

任何 obstruction 都必須帶 scope：

$$
\lambda(O).
$$

若：

$$
\lambda(O)=D_0,
$$

則除非另有 promotion certificate，不可自動把：

$$
O
$$

提升至：

$$
D_1\supsetneq D_0.
$$

---

# 11. Assumption Envelope

每個 theorem、route 或 obstruction 帶：

$$
\boxed{
\mathsf{Asm}(x)
=
\{A_1,\ldots,A_n\}.
}
$$

阻斷傳播的第一必要條件：

$$
\boxed{
\mathsf{Asm}(O)
\subseteq
\mathsf{Asm}(R).
}
$$

若不成立，則 obstruction 不可直接作用。

---

# 12. Scope Envelope

每個物件同時帶 scope contract：

$$
\mathsf{Scope}(x).
$$

阻斷傳播需要：

$$
\mathsf{Scope}(R)
\preceq
\mathsf{Scope}(O)
$$

或存在合法的 scope bridge。

這裡 $\preceq$ 表示 obstruction 的作用域至少覆蓋 route 所在作用域。

---

# 13. Representation Envelope

令：

$$
\mathsf{Rep}(x)
$$

表示證明物件使用的 representation class。

若 obstruction 只對：

$$
\rho_1
$$

有效，而 route 轉到：

$$
\rho_2,
$$

則：

$$
\boxed{
O_{\rho_1}
\not\Rightarrow
O_{\rho_2}.
}
$$

除非有：

$$
\mathsf{RepTransferCert}_{\rho_1\to\rho_2}.
$$

---

# 14. Target Fidelity

每個 obstruction 還必須對齊 target：

$$
\mathsf{Target}(O).
$$

若 route 的真正 target 是：

$$
Q',
$$

但 obstruction 證明的是：

$$
\neg Q,
$$

且：

$$
Q'\not\Rightarrow Q,
$$

則 obstruction 不能傳播。

---

# 15. Obstruction Record

定義 obstruction：

$$
\boxed{
O
=
\left\langle
\mathsf{Target},
\mathsf{Asm},
\mathsf{Scope},
\mathsf{Rep},
\mathsf{Mechanism},
\mathsf{Strength},
\mathsf{Cert},
\mathsf{Version}
\right\rangle.
}
$$

---

# 16. Obstruction Strength

$$
\mathsf{Strength}(O)
\in
\{
\mathsf{DIAGNOSTIC},
\mathsf{EMPIRICAL},
\mathsf{CONDITIONAL\_NO\_GO},
\mathsf{FORMAL\_NO\_GO},
\mathsf{COUNTEREXAMPLE},
\mathsf{INDEPENDENCE}
\}.
$$

只有後三類在適當 scope 下具有 theorem-level closure effect。

---

# 17. Diagnostic Obstruction 不封命題

若：

$$
\mathsf{Strength}(O)=\mathsf{DIAGNOSTIC},
$$

則最多：

$$
R
\mapsto
\mathsf{BLOCKED}.
$$

不得：

$$
Q
\mapsto
\mathsf{CLOSED}^{-}.
$$

---

# 18. Formal No-Go 的局部封路

若：

$$
\mathsf{Strength}(O)=\mathsf{FORMAL\_NO\_GO}
$$

且 propagation contract 滿足，則可有：

$$
O
\xrightarrow{\mathsf{BLOCKS}}
R.
$$

若 $R$ 本身就是完整 claim branch，則：

$$
\sigma(R)=\mathsf{CLOSED}^{-}.
$$

但 parent problem 是否 closed 仍另行判定。

---

# 19. Obstruction Propagation Contract

定義：

$$
\boxed{
\mathsf{OPCert}(O\to R)
}
$$

至少包含：

1. target match；
2. assumption coverage；
3. scope compatibility；
4. representation compatibility；
5. dependency validity；
6. theorem-strength compatibility；
7. version freshness；
8. exception audit；
9. bridge status；
10. provenance reference。

---

# 20. Propagation Rule

若：

$$
\mathsf{OPCert}(O\to R)=\mathsf{PASS},
$$

則：

$$
O\triangleright R.
$$

即 obstruction 可以作用於 route。

若：

$$
\mathsf{OPCert}(O\to R)\neq\mathsf{PASS},
$$

則：

$$
O\ntriangleright R.
$$

---

# 21. Obstruction Propagation Closure

對 obstruction set $\mathfrak O$ 定義：

$$
\boxed{
\operatorname{Cl}_{\rm obs}(S)
=
S
\cup
\left\{
R:
\exists O\in\mathfrak O,
\mathsf{OPCert}(O\to R)=\mathsf{PASS}
\right\}.
}
$$

這不是傳統 topological closure。

它是一個 typed proof-space closure operator family。

---

# 22. Implication Closure

定義：

$$
\boxed{
\operatorname{Cl}_{\Rightarrow}(S)
=
\left\{
q:
S\vdash_{\mathcal H}q
\right\}.
}
$$

其中 hypergraph derivation 必須只使用合法 certified implication edges。

---

# 23. Conditional Closure

若：

$$
A_1,\ldots,A_k
\Rightarrow
Q
$$

已證明，但 $A_i$ 尚未全部 closed，則：

$$
\boxed{
\sigma(Q)=\mathsf{CONDITIONAL}.
}
$$

對應：

$$
\operatorname{Cl}_{\rm cond}(S).
$$

---

# 24. Quotient Closure

已有 equivalence relation：

$$
\sim_{\rm prop},
\qquad
\sim_{\rm route},
\qquad
\sim_{\rm obs}.
$$

定義：

$$
\boxed{
\operatorname{Cl}_{\sim}(S)
=
\bigcup_{x\in S}[x]_{\sim}.
}
$$

但 quotient closure 不刪除 search provenance。

---

# 25. Quotient 不得消滅 genealogy

若：

$$
R_1\sim_{\rm route}R_2,
$$

則數學 identity 可 quotient。

但：

$$
\pi(R_1)\neq\pi(R_2)
$$

仍可保留。

因此：

$$
\boxed{
\text{Mathematical quotient}
\neq
\text{Historical deletion}.
}
$$

---

# 26. Bridge Closure

若：

$$
X
\xrightarrow{\mathsf{Bridge}}
Y
$$

且：

$$
\mathsf{BridgeCert}^{X\to Y}
=
\mathsf{PASS},
$$

則：

$$
Y
$$

可進入：

$$
\operatorname{Cl}_{\rm bridge}(X).
$$

---

# 27. Bridge 不保證 lossless

即使：

$$
\mathsf{BridgeCert}^{X\to Y}
=
\mathsf{PASS},
$$

仍可能：

$$
\mathsf{Loss}(X\to Y)>0.
$$

因此 closure metadata 必須記錄 bridge loss。

---

# 28. Closure Family

CSM 不假設單一 closure operator。

令：

$$
\boxed{
\mathfrak{Cl}
=
\{
\operatorname{Cl}_{\Rightarrow},
\operatorname{Cl}_{\rm cond},
\operatorname{Cl}_{\rm obs},
\operatorname{Cl}_{\sim},
\operatorname{Cl}_{\rm bridge},
\operatorname{Cl}_{\rm reopen}
\}.
}
$$

---

# 29. Heterogeneous Closure Principle

不同 closure operator 的語義不同。

因此：

$$
\boxed{
\operatorname{Cl}_{\Rightarrow}
\neq
\operatorname{Cl}_{\rm obs}
\neq
\operatorname{Cl}_{\sim}.
}
$$

它們不可只因符號都叫 closure 就被同一化。

---

# 30. Closure Composition

某些情況可做：

$$
\operatorname{Cl}_{\rm obs}
\circ
\operatorname{Cl}_{\Rightarrow}.
$$

但不保證：

$$
\operatorname{Cl}_{\Rightarrow}
\circ
\operatorname{Cl}_{\rm obs}
=
\operatorname{Cl}_{\rm obs}
\circ
\operatorname{Cl}_{\Rightarrow}.
$$

---

# 31. Noncommutative Closure

因此一般：

$$
\boxed{
\operatorname{Cl}_i
\circ
\operatorname{Cl}_j
\neq
\operatorname{Cl}_j
\circ
\operatorname{Cl}_i.
}
$$

這是 proof-space order dependence 的正式來源之一。

---

# 32. Closure Schedule

定義 closure schedule：

$$
\boxed{
\Sigma_{\rm Cl}
=
(C_1,C_2,\ldots,C_n).
}
$$

同一 initial graph 在不同 schedule 下可能得到不同 intermediate state。

---

# 33. Stable Closure State

若某 graph state $G^\star$ 滿足：

$$
C_i(G^\star)=G^\star
$$

對所有當前 active closure operator 成立，則稱：

$$
\boxed{
G^\star
\text{ is locally closure-stable}.
}
$$

這不代表 absolute mathematical completeness。

---

# 34. Frontier

定義 active frontier：

$$
\boxed{
\partial\mathfrak C(Q)
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
}
$$

其中 $v\leadsto Q$ 表示存在合法 route 或 bridge reachability。

---

# 35. Quotient Frontier

定義：

$$
\boxed{
\partial^\ast\mathfrak C(Q)
=
\partial\mathfrak C(Q)/\sim_{\rm route}.
}
$$

這比 raw frontier size 更接近真正獨立 route mass。

---

# 36. Frontier Mass

可定義：

$$
\boxed{
M_{\partial}(Q)
=
\sum_{[r]\in\partial^\ast\mathfrak C(Q)}
w([r]).
}
$$

其中 $w([r])$ 可反映 route independence、generality 或 certificate quality。

---

# 37. Frontier Contraction

若一個合法 closure step 使：

$$
M_{\partial,t+1}(Q)
<
M_{\partial,t}(Q),
$$

稱為：

$$
\boxed{
\text{frontier contraction}.
}
$$

但 frontier contraction 不等於 theorem progress，除非被 closure certificates 支持。

---

# 38. False Contraction

若 frontier 變小只是因：

- over-aggressive quotient；
- assumption 偷換；
- scope 偷縮；
- representation deletion；
- unsupported obstruction propagation；

則稱：

$$
\boxed{
\text{false contraction}.
}
$$

---

# 39. Frontier Expansion

新 representation、新 theorem、新 bridge 或 assumption relaxation 可能使：

$$
M_{\partial,t+1}(Q)
>
M_{\partial,t}(Q).
$$

這不一定是退步。

它可能表示研究空間變得更忠實。

---

# 40. Reopening Principle

若某 route $R$ 曾：

$$
\sigma_t(R)=\mathsf{BLOCKED},
$$

但後續：

- obstruction 被限縮；
- assumption 被移除；
- representation 改變；
- bridge 出現；
- theorem 被修訂；

則允許：

$$
\boxed{
\sigma_{t+1}(R)=\mathsf{REOPENED}.
}
$$

---

# 41. Reopening Operator

定義：

$$
\boxed{
\operatorname{Cl}_{\rm reopen}^{-1}
}
$$

不是傳統 inverse closure。

它表示：

> 對過去 closure decision 做版本化重新稽核，撤銷不再有效的 blocked/closed inheritance。

---

# 42. Reopening Certificate

$$
\boxed{
\mathsf{ReopenCert}(R)
}
$$

至少包含：

1. previous closure event；
2. invalidated premise；
3. changed scope/representation/bridge；
4. surviving dependencies；
5. new status；
6. provenance；
7. version reference。

---

# 43. Closure 不必全域單調

在固定 theorem base 與固定 assumptions 下，某些 closure operator 可單調。

但在研究系統中：

$$
\boxed{
\mathfrak C_t
\subseteq
\mathfrak C_{t+1}
}
$$

不是普遍真理。

因為 revision 可撤銷舊 closure。

---

# 44. Monotone Evidence / Nonmonotone Status

更精確地：

$$
\boxed{
\text{Evidence Ledger may be monotone,
while Closure Status may be nonmonotone}.
}
$$

舊證據不刪除，但舊結論可以被修正。

---

# 45. Closure Ledger

定義：

$$
\boxed{
\mathsf{Ledger}_{\rm Cl}
=
\{
e_1,e_2,\ldots
\}
}
$$

每個 closure event：

$$
e_t
=
\left\langle
\mathsf{Object},
\mathsf{OldStatus},
\mathsf{NewStatus},
\mathsf{Cause},
\mathsf{Cert},
\mathsf{Scope},
\mathsf{Version},
\mathsf{Time}
\right\rangle.
$$

---

# 46. Event-Sourced Closure

系統狀態：

$$
\boxed{
\mathcal S_{t+1}
=
\operatorname{Apply}(\mathcal S_t,e_t).
}
$$

任何 reopening 都是新 event，不是抹去舊 history。

---

# 47. Closure Debt

若 closure decision 缺少部分 proof obligation，定義：

$$
\boxed{
\mathsf{Debt}_{\rm Cl}(x).
}
$$

例如：

- missing scope proof；
- missing bridge proof；
- missing route-completeness proof；
- missing representation robustness；
- missing target fidelity；
- missing independence audit。

---

# 48. Debt Propagation

若：

$$
A\Rightarrow B
$$

但 $A$ 帶未償 debt，則：

$$
B
$$

不能自動被標記成 debt-free。

可定義：

$$
\boxed{
\mathsf{Debt}(B)
\supseteq
\mathsf{TransferDebt}(A\to B).
}
$$

---

# 49. Closure with Debt

允許：

$$
\boxed{
\sigma(Q)=\mathsf{CONDITIONAL}
\quad
\text{with}
\quad
\mathsf{Debt}(Q)\neq\varnothing.
}
$$

這比硬分 PASS/FAIL 更符合長程研究。

---

# 50. Route Exhaustion

令：

$$
\mathcal R_{\rm adm}(Q)
$$

為 admissible route classes。

若：

$$
\forall [R]\in\mathcal R_{\rm adm}(Q),
\quad
\sigma([R])\in
\{
\mathsf{CLOSED}^{-},
\mathsf{BLOCKED}
\},
$$

仍不能立刻說：

$$
Q
$$

被反證。

因為 route space 本身可能不完備。

---

# 51. Route-Completeness Certificate

定義：

$$
\boxed{
\mathsf{RCCert}(Q,\mathcal G_R).
}
$$

其目標是證：

$$
\boxed{
\mathcal R_{\rm enum}(Q)
=
\mathcal R_{\rm adm}(Q)
}
$$

相對指定 route grammar / mechanism class。

---

# 52. Relative Route Completeness

通常只能證：

$$
\boxed{
\mathcal R_{\rm enum}^{\Gamma}(Q)
=
\mathcal R_{\rm adm}^{\Gamma}(Q)
}
$$

其中 $\Gamma$ 是明確 route grammar。

這仍然是相對完備。

---

# 53. Exhaustion Theorem Pattern

若：

1. $\mathsf{RCCert}(Q,\Gamma)=\mathsf{PASS}$ ；
2. 每個 admissible route class 都被 certified obstruction 排除；
3. obstruction propagation 全部 scope-valid；

則可得到：

$$
\boxed{
\Gamma
\vdash
\neg\operatorname{RouteExists}(Q).
}
$$

---

# 54. Route Exhaustion 不等於 Claim Refutation

若 $Q$ 本身不是「存在某 route」的命題，而是外部數學命題，仍需要 bridge：

$$
\neg\operatorname{RouteExists}(Q)
\Longrightarrow
\neg Q.
$$

該 bridge 也必須有 certificate。

---

# 55. Positive Exhaustion

反之，若 claim 可被分解為有限或可控 branch family：

$$
Q
\Longleftrightarrow
Q_1\vee\cdots\vee Q_n,
$$

且某 $Q_i$ 被證成，則：

$$
Q
$$

正閉合。

若所有 $Q_i$ 都被反證，則：

$$
Q
$$

負閉合。

---

# 56. Branch Decomposition Certificate

定義：

$$
\boxed{
\mathsf{BDCert}
\left(
Q
\leftrightarrow
\bigvee_iQ_i
\right).
}
$$

沒有 branch decomposition certificate，就不能把 branch closure 推到 parent closure。

---

# 57. Hypergraph Cut

對 target $Q$ 定義 cut set：

$$
C\subset V
$$

使得每條 admissible route 到 $Q$ 都通過 $C$。

若：

$$
C
$$

被完整 certified closure，則可能形成高槓桿 obstruction boundary。

---

# 58. Certified Cut

若：

$$
\mathsf{CutCert}(C,Q)=\mathsf{PASS},
$$

且：

$$
\forall c\in C,
\quad
\sigma(c)=\mathsf{CLOSED}^{-},
$$

則：

$$
Q
$$

的所有 route 被截斷。

但仍需 parent bridge 判定是否推出 $\neg Q$。

---

# 59. Obstruction Centrality

定義：

$$
Z(O)
$$

表示 obstruction 在 route graph 中截斷的獨立 route mass。

這不是 theorem truth score。

---

# 60. High-Centrality Obstruction

若：

$$
Z(O)\gg0,
$$

表示：

$$
O
$$

值得優先研究。

但：

$$
\boxed{
Z(O)\gg0
\not\Rightarrow
O
\text{ is globally necessary}.
}
$$

---

# 61. Obstruction Confluence

若不同 route quotient class：

$$
[R_i]_{\rm route}
$$

都命中同一 obstruction class：

$$
[O^\star]_{\rm obs},
$$

則形成：

$$
\boxed{
\text{obstruction confluence}.
}
$$

---

# 62. False Confluence

若不同 route 其實共享同一 hidden premise 或只是 notation variant，則 confluence 強度必須降權。

因此：

$$
C_{\rm raw}(O)
\neq
C_{\rm ind}(O).
$$

---

# 63. Closure Robustness

可定義：

$$
\boxed{
\mathsf{RobustCl}(O)
=
f(
C_{\rm ind},
C_B,
C_M,
C_L,
\mathsf{Scope},
\mathsf{CertQuality}
).
}
$$

但它仍是 research metric，不是 proof substitute。

---

# 64. Survivor

若一個 route family 經過當前所有合法 obstruction propagation 後仍 OPEN，稱：

$$
\boxed{
\mathsf{Survivor}(R).
}
$$

Survivor 不代表 route 可成功。

它只表示目前尚未被封。

---

# 65. Minimal Survivor

若：

$$
R
$$

是 survivor，且所有更弱或更一般的 sibling routes 都被封，則：

$$
\boxed{
\mathsf{MinimalSurvivor}(R).
}
$$

這是下一輪研究的高槓桿 target。

---

# 66. Survivor Compression

一個成熟研究流程會反覆：

$$
\text{many routes}
\to
\text{few survivors}
\to
\text{refined decomposition}
\to
\text{new obstruction audit}.
$$

這就是 closure-space dynamics 的第一個基本循環。

---

# 67. Reopening 與 Survivor 的互動

舊 survivor 可以被新 obstruction 封閉。

舊 blocked route 也可以被新 bridge 重開。

因此 graph frontier 是：

$$
\boxed{
\text{dynamic boundary},
}
$$

不是靜態清單。

---

# 68. NS 編譯規則：文件標籤到圖狀態

NS 過去文件常用：

- `CLOSED`；
- `OPEN`；
- `NO-GO`；
- `SURVIVOR`；
- `CONDITIONAL`；
- `STOP-*`。

CSM 不直接把這些文字當 theorem status。

每一筆都必須先編譯成：

$$
\boxed{
\mathsf{StatusRecord}
=
\langle
\mathsf{Object},
\mathsf{Claim},
\mathsf{Scope},
\mathsf{Asm},
\mathsf{CertType},
\mathsf{Status}
\rangle.
}
$$

---

# 69. NS 的 NO-GO 編譯

若某文件說：

> scalar additive budget NO-GO

則不能直接生成：

$$
\mathsf{CLOSED}^{-}(\text{Navier--Stokes blow-up}).
$$

應生成：

$$
\boxed{
O_{\rm scalar-budget}
\xrightarrow{\mathsf{BLOCKS}}
R_{\rm scalar-budget}.
}
$$

---

# 70. NS 的 SURVIVOR 編譯

若某 route 仍存活，例如 shear/polarization survivor，則建立：

$$
\sigma(R_{\rm sh/pol})
=
\mathsf{OPEN}.
$$

它不是：

$$
\mathsf{PROVEN}.
$$

---

# 71. NS 的 STOP 編譯

`STOP-D105` 不是 claim refutation。

應編譯為：

$$
\boxed{
\mathsf{FrontierNode}
(
\text{first-order solvability / spectral drift}
).
}
$$

這是一個 active boundary node。

---

# 72. NS 的相對全域 closure graph

最小模型：

$$
\boxed{
\mathcal H_{\rm NS}^{\rm rel}
=
\mathcal H_{\rm C1-C6}
\cup
\mathcal H_{\rm X72}
\cup
\mathcal H_{\rm DCRP}
\cup
\mathcal H_{\rm RFP}
\cup
\mathcal H_{\rm MORP}
\cup
\mathcal H_{\rm FCBP}
\cup
\mathcal H_{\rm bridge}.
}
$$

---

# 73. Cross-Series Bridge

不同 NS 系列只有在 claim/assumption/scope 對齊時才可共用 obstruction。

因此必須有：

$$
\mathsf{SeriesBridgeCert}.
$$

---

# 74. Cross-Series False Merge

若兩篇都說：

> carrier escape

但一篇指 spatial carrier，另一篇指 spectral carrier，則：

$$
\boxed{
O_1\not\sim_{\rm obs}O_2
}
$$

除非另有 formal mapping。

---

# 75. Closure Graph 的研究目標

NS closure graph 的第一目標不是證明 Clay。

而是：

$$
\boxed{
\text{把已知 route、obstruction、survivor、debt
轉成可查詢、可傳播、可重開的相對全域圖。}
}
$$

---

# 76. Closure Graph 的第二目標

計算：

$$
\partial^\ast\mathfrak C_{\rm NS}(Q_{\rm Clay})
$$

即 quotient 後的 active independent frontier。

---

# 77. Closure Graph 的第三目標

尋找：

$$
\boxed{
\text{high-centrality certified cuts}.
}
$$

它們可能比盲目新增 paper 更有研究槓桿。

---

# 78. Closure Graph 的第四目標

檢查哪些 blocked route 可被：

- assumption relaxation；
- new representation；
- new external theorem；
- bridge proof；
- domain retyping；

合法重開。

---

# 79. Closure-Space Update

定義：

$$
\boxed{
\mathfrak C_{t+1}
=
\mathfrak U(
\mathfrak C_t,
\Delta\mathsf{Claim},
\Delta\mathsf{Cert},
\Delta\mathsf{Bridge},
\Delta\mathsf{Obstruction},
\Delta\mathsf{Revision}
).
}
$$

---

# 80. Closure Fixed Point

若在固定 corpus、固定 theorem base、固定 bridge set 下：

$$
\mathfrak U(\mathfrak C^\star)=\mathfrak C^\star,
$$

稱局部 closure fixed point。

---

# 81. Fixed Point 不等於數學完備

$$
\boxed{
\mathfrak C^\star
\text{ locally stable}
\not\Rightarrow
\mathfrak C^\star
=
\Omega^{\rm math}.
}
$$

---

# 82. Closure Expansion

新 theorem 或 representation 可使：

$$
\mathfrak C^\star
\to
\mathfrak C^{\star\prime}
$$

並重新出現 frontier。

因此 CSM 的 closure 是可再展開閉包。

---

# 83. Closure-Space Conservation of History

本文要求：

$$
\boxed{
\text{No closure event may erase its provenance history.}
}
$$

即使 route 被重新打開，舊 obstruction event 仍保留。

---

# 84. Proof Object 與 Search Event 雙身份

同一 artifact 同時具有：

$$
\boxed{
\text{Mathematical Identity}
}
$$

與：

$$
\boxed{
\text{Search-Historical Identity}.
}
$$

數學上 quotient 不代表歷史上刪除。

---

# 85. Closure-Space Auditability

任何 status 必須可回答：

1. 誰把它關閉？
2. 用哪個 theorem？
3. assumptions 是什麼？
4. scope 是什麼？
5. 是否跨 representation？
6. 是否存在 bridge？
7. 是否有 debt？
8. 是否曾 reopen？
9. 哪個版本有效？
10. 哪些 descendants 繼承此 status？

---

# 86. Claim-Level Closure Certificate

定義：

$$
\boxed{
\mathsf{ClaimClCert}(Q)
}
$$

包括：

- theorem proof / counterexample reference；
- branch decomposition；
- route completeness；
- obstruction propagation；
- scope fidelity；
- version；
- debt status。

---

# 87. Relative-Global Closure Certificate

對 domain $D$：

$$
\boxed{
\mathsf{RGClCert}_{D}(Q).
}
$$

它表示：

> 在指定 domain、route grammar、theorem base、representation policy 與 bridge policy 下， $Q$ 的 closure status 已完整稽核。

---

# 88. Relative-Global 不等於 Absolute

$$
\boxed{
\mathsf{RGClCert}_{D}(Q)
\not\Rightarrow
\mathsf{AbsoluteClosure}(Q).
}
$$

---

# 89. Local-to-Absolute Gate

若要升格：

$$
\mathsf{RGClCert}_{D}(Q)
\to
\mathsf{AbsoluteClosure}(Q),
$$

至少必須解決：

- domain completeness；
- route grammar completeness；
- representation completeness；
- theorem-base adequacy；
- hidden assumption absence；
- bridge completeness；
- undecidability/independence status。

---

# 90. Closure No-Go 1

$$
\boxed{
\text{Many blocked routes}
\not\Rightarrow
\text{claim false}.
}
$$

---

# 91. Closure No-Go 2

$$
\boxed{
\text{Many surviving routes}
\not\Rightarrow
\text{claim true}.
}
$$

---

# 92. Closure No-Go 3

$$
\boxed{
\text{Frontier shrinking}
\not\Rightarrow
\text{proof nearing completion}.
}
$$

---

# 93. Closure No-Go 4

$$
\boxed{
\text{One central obstruction}
\not\Rightarrow
\text{global obstruction}.
}
$$

---

# 94. Closure No-Go 5

$$
\boxed{
\text{One representation fails}
\not\Rightarrow
\text{all equivalent representations fail}.
}
$$

---

# 95. Closure No-Go 6

$$
\boxed{
\text{One domain is closed}
\not\Rightarrow
\text{all generalized domains are closed}.
}
$$

---

# 96. Closure No-Go 7

$$
\boxed{
\text{Research graph stable}
\not\Rightarrow
\text{mathematical reality exhausted}.
}
$$

---

# 97. Minimal Machine Record

```yaml
closure_record:
  object_id:
  object_type:
  target_id:
  scope_id:
  assumptions: []
  representation_id:
  old_status:
  new_status:
  cause_type:
  cause_ids: []
  certificate_id:
  debt_ids: []
  version:
  provenance:
  reopen_of:
```

---

# 98. Obstruction Machine Record

```yaml
obstruction:
  obstruction_id:
  target_pattern:
  assumptions: []
  scope:
  representation:
  mechanism:
  strength:
  certificate:
  exceptions: []
  bridge_requirements: []
  version:
  active: true
```

---

# 99. Propagation Machine Record

```yaml
obstruction_propagation:
  obstruction_id:
  target_route_id:
  target_match: PASS
  assumption_coverage: PASS
  scope_compatibility: PASS
  representation_compatibility: PASS
  dependency_validity: PASS
  theorem_strength: PASS
  version_freshness: PASS
  exception_audit: PASS
  bridge_status: PASS
  result: BLOCKED
```

---

# 100. Reopening Machine Record

```yaml
reopening:
  route_id:
  previous_closure_event:
  invalidated_premise:
  changed_scope:
  changed_representation:
  new_bridge:
  new_certificate:
  result: REOPENED
```

---

# 101. Validation Scenario A — Local estimate barrier

Route:

$$
R_1
$$

在：

$$
L^p
$$

estimate 下失敗。

若沒有 theorem 證明所有 admissible norms 都失敗，則：

$$
\sigma(R_1)=\mathsf{BLOCKED}.
$$

Parent claim 保持 OPEN。

---

# 102. Validation Scenario B — Counterexample

若有合法 counterexample：

$$
c\models\neg Q,
$$

則：

$$
\sigma(Q)=\mathsf{CLOSED}^{-}.
$$

這不是 route-level blocked，而是 claim-level refutation。

---

# 103. Validation Scenario C — Conditional theorem

若：

$$
A\Rightarrow Q
$$

已證明，但：

$$
\sigma(A)=\mathsf{OPEN},
$$

則：

$$
\sigma(Q)=\mathsf{CONDITIONAL}.
$$

---

# 104. Validation Scenario D — Representation reopening

若：

$$
R_{\rho_1}
$$

被 obstruction $O_{\rho_1}$ 阻斷，但：

$$
R_{\rho_2}
$$

不受該 obstruction，則：

$$
R_{\rho_2}
$$

仍 OPEN。

若兩者是同一 route 的 representation variants，可記錄：

$$
\mathsf{REOPENED}.
$$

---

# 105. Validation Scenario E — Scope promotion forbidden

若 obstruction 對：

$$
D_0
$$

成立，但 target route 位於：

$$
D_1\supsetneq D_0,
$$

且無 promotion certificate，則：

$$
O\ntriangleright R_{D_1}.
$$

---

# 106. Validation Scenario F — Branch exhaustion

若：

$$
Q
\leftrightarrow
Q_1\vee Q_2\vee Q_3
$$

有 $\mathsf{BDCert}$，且三個 branch 全部 theorem-level refuted，則：

$$
\sigma(Q)=\mathsf{CLOSED}^{-}.
$$

---

# 107. Validation Scenario G — Route grammar incomplete

若所有已列 route 都 blocked，但沒有 $\mathsf{RCCert}$，則：

$$
\sigma(Q)\neq\mathsf{CLOSED}^{-}
$$

僅能說：

$$
\text{observed route space exhausted}.
$$

---

# 108. Validation Scenario H — Obstruction superseded

若 theorem $T_1$ 被更強 theorem $T_2$ 修訂，使舊 obstruction scope 縮小，則所有依賴舊 scope 的 closure event 進入 re-audit。

---

# 109. Validation Scenario I — False quotient

若兩 route 只因 lexical similarity 被合併，但 assumptions 不同，應拆回不同 route class。

避免 false frontier contraction。

---

# 110. Validation Scenario J — NS scalar budget no-go

若 scalar/additive budget route 被正式 NO-GO，則：

$$
R_{\rm scalar}
\mapsto
\mathsf{BLOCKED}
$$

而：

$$
Q_{\rm NS}
$$

仍 OPEN。

---

# 111. Validation Scenario K — NS survivor

若 DCRP shear/polarization branch 尚未被 theorem-level no-go 排除，則：

$$
\sigma(R_{\rm sh/pol})=\mathsf{OPEN}.
$$

即使其他 sibling branches 已封。

---

# 112. Validation Scenario L — Cross-series merge

若 X72 與 DCRP obstruction 經 semantic/assumption/scope audit 確認同一，才允許：

$$
O_{\rm X72}
\sim_{\rm obs}
O_{\rm DCRP}.
$$

---

# 113. CSM 與 LSI-PSD 的關係

LSI-PSD 主要回答：

> 我們如何觀測、去重、分 basin、衡量 recurrence 與 obstruction confluence？

CSM 進一步問：

> 一旦這些物件被建立，closure status 如何成為可運算、可傳播、可撤銷、可稽核的圖論對象？

因此：

$$
\boxed{
\text{LSI-PSD}
\subset
\text{CSM methodological substrate}.
}
$$

這裡的 $\subset$ 是架構用途上的包含，不主張歷史或理論本體完全等價。

---

# 114. CSM 與 UCT 的關係

UCT 提供：

- typed non-collapse；
- bridge certificate；
- debt；
- ledger；
- relative-global gate。

CSM 將其具體化到 mathematical proof-space。

因此：

$$
\boxed{
\text{UCT}
\to
\text{CSM proof-space instantiation}.
}
$$

但 CSM 不等於 UCT 全部。

---

# 115. CSM 的第一個主要研究命題

$$
\boxed{
\textbf{Closure Propagation Conjecture}
}
$$

在一個 typed finite or finitely generated closure hypergraph 中，若所有 edge signatures、scope contracts、obstruction certificates 與 revision events 都可判定，則 relative-global closure status 可被演算法性重建與重放。

這是 runtime 層未來要實作的核心。

---

# 116. 第二主要研究命題

$$
\boxed{
\textbf{Frontier Fidelity Conjecture}
}
$$

若 quotient policy、route grammar、scope typing 與 obstruction propagation 全部通過 audit，則：

$$
\partial^\ast\mathfrak C(Q)
$$

比 raw paper count 或 raw route count 更接近「目前真正尚未封閉的獨立 proof obligations」。

本文不主張它等於 absolute proof frontier。

---

# 117. 第三主要研究命題

$$
\boxed{
\textbf{Certified Exhaustion Principle}
}
$$

只有：

$$
\mathsf{BranchDecomposition}
+
\mathsf{RouteCompleteness}
+
\mathsf{CertifiedObstructionClosure}
+
\mathsf{ScopeFidelity}
$$

同時成立時，route exhaustion 才能安全升格成 parent-level closure conclusion。

---

# 118. 第四主要研究命題

$$
\boxed{
\textbf{Reopenability Principle}
}
$$

在非固定 theorem base、非固定 representation、非固定 scope 的長程研究系統中，blocked-route status 應預設為可重審，而不是永久終態。

---

# 119. 對 NS 的直接意義

NS 現有大量工作最有價值的部分，不只是「某次沒證出來」。

真正價值是：

$$
\boxed{
\text{我們已經累積大量可編譯的 obstruction、survivor、branch split、scope correction 與 reopening evidence。}
}
$$

CSM 使這些結果可以第一次被組裝成一個相對全域 closure space。

---

# 120. 下一階段

Paper 03 應處理：

$$
\boxed{
\textbf{Frontier Geometry, Cut Sets, and Relative Exhaustion}
}
$$

即：

- frontier topology / graph geometry；
- minimal cut；
- obstruction cover；
- route-completeness；
- exhaustion certificate；
- closure radius；
- reopened frontier；
- global-vs-relative proof boundary。

---

# 121. 結論

本文將「封路」從研究敘事轉為型別圖論運算。

其核心結論可濃縮為：

$$
\boxed{
\mathsf{RouteBlocked}
\neq
\mathsf{ClaimRefuted}.
}
$$

$$
\boxed{
\mathsf{BranchClosed}
\neq
\mathsf{ProblemClosed}.
}
$$

$$
\boxed{
\mathsf{LocalObstruction}
\neq
\mathsf{GlobalObstruction}.
}
$$

$$
\boxed{
\mathsf{RelativeClosure}
\neq
\mathsf{AbsoluteClosure}.
}
$$

以及：

$$
\boxed{
\text{closure status must be typed, scoped, certified, versioned, and reopenable}.
}
$$

當這些條件被滿足後，一個大型未解問題的長程研究史才可能被轉成真正可運算的閉包空間，而不只是文件堆積。

---

## 附錄 A — CSM Paper 02 最小不變量

1. blocked 不等於 refuted；
2. branch closure 不等於 problem closure；
3. obstruction 必須有 assumption envelope；
4. obstruction 必須有 scope envelope；
5. representation-specific obstruction 不得無證跨 representation；
6. cross-domain propagation 必須有 bridge；
7. quotient 不刪 provenance；
8. closure status 可 nonmonotone；
9. evidence ledger 不刪除；
10. reopening 必須有 certificate；
11. frontier contraction 必須防 false contraction；
12. route exhaustion 必須有 route-completeness certificate；
13. local closure 不得偷升 absolute closure；
14. machine record 必須保存 version；
15. 所有 closure event 必須可 replay。

---

## 附錄 B — CSM Series Dependencies

### Paper 00

提供：

- Relative-Global Closure Space；
- typed research objects；
- closure status；
- frontier；
- debt；
- ledger；
- route-completeness obligation。

### Paper 01

提供：

- Globality Typing Principle；
- scope contract；
- domain stratification；
- globality promotion certificate；
- NS formal / physical / generalized domain separation。

### Paper 02

新增：

- typed closure hypergraph；
- obstruction propagation contract；
- closure family；
- noncommutative closure schedule；
- reopening operator；
- frontier contraction；
- branch decomposition certificate；
- route exhaustion machinery；
- NS graph compilation rules。

---

**END OF CSM PAPER 02 v0.1**
