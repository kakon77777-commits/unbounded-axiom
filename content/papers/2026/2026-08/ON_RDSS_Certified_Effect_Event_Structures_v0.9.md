# Operator-Native RDSS：Certified Effect Event Structures
## Conflict, Disjunctive Enabling, Branch History, and Boundary Behaviour

**版本：** v0.9 Working Proof Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS 由 Effect Pomset 推進到 Branching / Conflict / Alternative Cause 的第一代事件結構語義  
**前置：** ON-RDSS v0.3–v0.8

---

# 摘要

ON-RDSS v0.8 已將 sequential effect trace：

$$
\chi=[e_1,\ldots,e_n]
$$

升級為 effect pomset：

$$
\mathcal P_E=(E,\prec,\lambda),
$$

從而允許：

$$
e_a\parallel e_b.
$$

但 pomset 只足以表達：

- causality；
- concurrency；
- partial order。

它一般不能單獨充分表達：

- mutually exclusive alternatives；
- conflict；
- disjunctive causation；
- alternative enabling histories；
- branch-dependent future capability。

因此本版提出兩層事件語義：

## Prime Certified Effect Event Structure

$$
\boxed{
\mathcal E_P
=
(E,\le,\#,\lambda,\Theta,Auth,Cert,Ver).
}
$$

適合每個事件具有明確必要因果歷史的子域。

## General Certified Effect Event Structure

$$
\boxed{
\mathcal E_G
=
(E,Con,\vdash,\lambda,\Theta,Auth,Cert,Ver).
}
$$

其中：

- $E$：effect events；
- $Con$：有限一致性族；
- $\vdash$：enabling relation；
- $\lambda$：effect label；
- $\Theta$：event / sort / operator typing；
- $Auth$：authority obligations；
- $Cert$：event / enabling / encapsulation certificates；
- $Ver$：Operator Algebra / Event Semantics version。

一般版本可以直接表達：

$$
\{a\}\vdash c,
\qquad
\{b\}\vdash c,
$$

即「 $a$ 或 $b$ 任一者都足以啟用 $c$ 」。

---

# 1. 為什麼 Pomset 不夠？

Pomset：

$$
(E,\le,\lambda)
$$

能表示：

$$
a<b,
$$

或：

$$
a\parallel b.
$$

但若：

$$
a\# b,
$$

代表：

> $a$ 與 $b$ 不能出現在同一合法執行 configuration。

單純 partial order 沒有這個資訊。

更進一步，若：

$$
c
$$

可由：

$$
a
$$

或：

$$
b
$$

任一者啟用，

把它硬寫成：

$$
a<c,
\qquad
b<c
$$

通常會被讀成：

> $c$ 需要 $a$ 與 $b$ 皆先發生。

所以「替代原因」不能由單一必要前驅偏序完整表示。

---

# 2. Prime CEES

第一代 Prime Certified Effect Event Structure：

$$
\boxed{
\mathcal E_P
=
(
E,
\le,
\#,
\lambda,
Ty,
Auth,
Cert,
Ver
).
}
$$

要求：

1. $\le$ 是 causal partial order；
2. $\#$ 是 irreflexive symmetric conflict；
3. conflict 對 causality 向後繼承；
4. event typing / authority / certificate 均版本化。

Configuration：

$$
\boxed{
C\subseteq E
}
$$

需：

- downward closed；
- conflict-free。

---

# 3. General CEES

為了直接處理 alternative causes，採：

$$
\boxed{
\mathcal E_G
=
(
E,
Con,
\vdash,
\lambda,
Ty,
Auth,
Cert,
Ver
).
}
$$

其中：

$$
Con
\subseteq
\mathcal P_{fin}(E)
$$

是 downward-closed consistency family。

Enabling：

$$
X\vdash e
$$

表示：

> 在一致 configuration $X$ 下，事件 $e$ 可被啟用。

第一代採 monotone enabling：

$$
X\vdash e
\land
X\subseteq Y\in Con
\Rightarrow
Y\vdash e.
$$

---

# 4. Configuration

有限 configuration：

$$
\boxed{
C=\{e_1,\ldots,e_n\}
}
$$

若存在 enumeration：

$$
e_{\pi(1)},\ldots,e_{\pi(n)}
$$

使每個 prefix：

$$
C_k
=
\{e_{\pi(1)},\ldots,e_{\pi(k)}\}
$$

都一致，且：

$$
C_{k-1}\vdash e_{\pi(k)}.
$$

這使 configuration 同時保存：

- consistency；
- enabling；
- realizable execution history。

---

# 5. Conflict

對 prime profile：

$$
\boxed{
e_a\# e_b
}
$$

表示：

$$
\forall C\in Config(\mathcal E_P),
\qquad
\neg(
e_a\in C
\land
e_b\in C
).
$$

在 general profile 中，conflict 可由 consistency family 表達：

$$
\boxed{
\{e_a,e_b\}\notin Con.
}
$$

---

# 6. Concurrency

Prime profile：

$$
e_a\parallel e_b
$$

要求：

- 不互相 causally ordered；
- 不 conflict。

General profile 中更適合直接以 configuration possibility 表達：

存在：

$$
C
$$

使兩者皆可從某 common past 狀態獨立加入，且最終 joint configuration 一致。

---

# 7. Disjunctive Enabling

若：

$$
\boxed{
\{a\}\vdash c,
\qquad
\{b\}\vdash c,
}
$$

則：

$$
c
$$

具有至少兩個替代 enabling histories。

定義：

$$
\boxed{
Alt(c)
=
\min_{\subseteq}
\{
X\in Con
\mid
X\vdash c
\}.
}
$$

若：

$$
|Alt(c)|>1,
$$

則存在 disjunctive / alternative cause。

---

# 8. 為什麼 Prime Causality 可能失真？

若把：

$$
Alt(c)
=
\{
\{a\},
\{b\}
\}
$$

壓成：

$$
a\le c,
\qquad
b\le c,
$$

會把必要條件誤成：

$$
\{a,b\}\vdash c.
$$

所以 Prime CEES 只適合：

> 每個 event 有單一必要因果 past

或已經選定 branch history 的局部子域。

---

# 9. Branch

定義 branch：

$$
\boxed{
B_i
}
$$

為一個 maximal / task-relevant compatible configuration family。

更實作化地，可把 branch identity 寫成：

$$
\boxed{
BranchID(C)
=
Hash(
MinimalChoices(C),
AlgebraVersion
).
}
$$

Branch 不是一定需要全域永久 ID；只有當 future capability、authority 或 replay 依賴 branch 時才升格保存。

---

# 10. 同結果不等於同 Branch

考慮：

$$
C_A
=
\{a,r_a\},
$$

$$
C_B
=
\{b,r_b\}.
$$

若 projection：

$$
\Pi(r_a)
=
\Pi(r_b)
=
r,
$$

則：

$$
\Pi(C_A)
=
\Pi(C_B).
$$

但若：

$$
Enabled(C_A)
=
\{f_a\},
$$

$$
Enabled(C_B)
=
\{f_b\},
$$

則：

$$
\boxed{
Future(C_A)
\neq
Future(C_B).
}
$$

因此：

$$
\boxed{
SameCurrentObservation
\not\Rightarrow
SafeHistoryQuotient.
}
$$

---

# 11. Future-Capability Equivalence

定義 task-relative：

$$
\boxed{
C_1
\simeq_Q^{future}
C_2
}
$$

至少要求：

1. current projection 等價；
2. enabled operator/effect profile 等價；
3. future reachable observation classes 等價；
4. authority obligations 等價；
5. residual obligations 等價。

只有 current output 一樣不夠。

---

# 12. Branch Quotient Certificate

若希望把：

$$
C_1,C_2
$$

封裝成 parent-level same state：

$$
S_P,
$$

必須有：

$$
\boxed{
BranchQuotientCert_Q(C_1,C_2).
}
$$

至少驗證：

$$
C_1
\simeq_Q^{future}
C_2.
$$

否則 branch choice 必須保留於 history。

---

# 13. Boundary Causal Reachability 已經不夠

v0.8 定義：

$$
R_\partial(S)
\subseteq
B^-_S\times B^+_S.
$$

它回答：

> 哪個 boundary input 可以因果到哪個 boundary output？

但若：

$$
o_a\# o_b,
$$

只有：

$$
R_\partial
$$

並不會阻止 parent system 同時啟用：

$$
o_a,o_b.
$$

所以：

$$
\boxed{
BoundaryCausalSummary
}
$$

只是 derived index，不再是完整 authoritative boundary semantics。

---

# 14. Boundary Configuration Semantics

定義：

$$
\boxed{
Config_\partial(S)
=
\{
\Pi_\partial(C)
\mid
C\in Config(S)
\}.
}
$$

其中：

$$
\Pi_\partial
$$

只保留 boundary-visible events / ports / outcomes。

這直接保存：

- 哪些 boundary event combinations 可能；
- 哪些 combination 永遠不可能；
- 哪些 branch 可以共同出現。

---

# 15. Boundary Consistency

由：

$$
Config_\partial(S)
$$

抽取：

$$
\boxed{
Con_\partial(S).
}
$$

若：

$$
\{o_a,o_b\}
\notin
Con_\partial(S),
$$

則 parent macro 不得允許兩者同時出現。

---

# 16. Conflict-Erasure Counterexample

內部：

$$
choose_a\# choose_b.
$$

Branch A：

$$
choose_a\vdash o_a.
$$

Branch B：

$$
choose_b\vdash o_b.
$$

因此合法 boundary configurations：

$$
\boxed{
\varnothing,
\{o_a\},
\{o_b\}.
}
$$

但 naive macro 若只暴露兩個 output ports 且不保存 conflict，會錯誤增加：

$$
\boxed{
\{o_a,o_b\}.
}
$$

所以：

$$
\boxed{
\text{Encapsulation may not invent joint possibilities.}
}
$$

---

# 17. Boundary Enabling Semantics

只保存 consistency 還不夠。

對 output event / port：

$$
o\in B^+_S
$$

定義最小 boundary enabling family：

$$
\boxed{
En_\partial(o)
=
\min_{\subseteq}
\{
X\subseteq B^-_S
\mid
X\vdash_S o
\}.
}
$$

例如：

$$
\boxed{
En_\partial(c)
=
\{
\{a\},
\{b\}
\}.
}
$$

這表示：

> $a$ 或 $b$ 任一 boundary cause 都能啟用 $c$。

---

# 18. Boundary Behaviour Contract

因此 v0.9 的 authoritative macro contract 升級為：

$$
\boxed{
BC_S
=
(
Sig_\partial,
Con_\partial,
En_\partial,
Auth_\partial,
Residual_\partial,
Version
).
}
$$

其中：

- $Sig_\partial$：port sorts；
- $Con_\partial$：visible consistency；
- $En_\partial$：alternative enabling；
- $Auth_\partial$：authority obligations；
- $Residual_\partial$：可能的 open obligations；
- $Version$：event/algebra semantics snapshot。

---

# 19. $R_\partial$ 變成衍生 Index

可以從：

$$
En_\partial
$$

或：

$$
Config_\partial
$$

導出較快的：

$$
R_\partial.
$$

因此：

$$
\boxed{
BC_S
\to
R_\partial(S)
}
$$

像：

$$
Authority
\to
Index.
$$

這與 RDSS Runtime 先前的：

$$
Authority\neq Index
$$

原則一致。

---

# 20. 宏算子的完整事件版本

因此 container / macro operator 可寫：

$$
\boxed{
M_S
=
(
Sig_\partial,
BC_S,
\mathcal E_S,
AuthReq_S,
HistWitness_S,
Cert_S
).
}
$$

其中：

$$
\mathcal E_S
$$

可作 strong nested event semantics。

Parent layer 可以只查：

$$
BC_S
$$

而 deeper expansion 再打開：

$$
\mathcal E_S.
$$

---

# 21. Event-Structure Encapsulation Certificate

定義：

$$
\boxed{
ES-EncapCert
=
TypePres
\land
ConfigPres
\land
EnablingPres
\land
AuthorityPres
\land
HistoryReconstructible
\land
VersionPinned.
}
$$

比 v0.8 的：

$$
BoundaryCausalPres
$$

更強。

---

# 22. Lemma E1 — Boundary Configuration Preservation

若：

$$
ES-EncapCert(S,M_S)
$$

成立，則：

$$
\boxed{
Config_\partial(S)
=
Config_\partial(M_S).
}
$$

在指定 boundary observation domain 下成立。

這直接禁止：

- inventing impossible joint branch；
- deleting possible visible branch。

---

# 23. Lemma E2 — Boundary Enabling Preservation

對每個 visible output：

$$
o,
$$

要求：

$$
\boxed{
En_\partial^S(o)
=
En_\partial^{M_S}(o)
}
$$

或在指定 equivalence 下有證書等價。

因此 disjunctive cause 不因封裝而變成 conjunctive cause。

---

# 24. Lemma E3 — Causal Reachability Derived Preservation

若 E1、E2 成立，

則對由 boundary enabling導出的 task-relevant reachability：

$$
\boxed{
R_\partial^S
\simeq
R_\partial^{M_S}.
}
$$

所以 v0.8 的 causal-preservation theorem 成為 v0.9 更強 boundary behaviour theorem 的推論候選。

---

# 25. Theorem Candidate ET1 — Boundary Behaviour Preservation

固定：

$$
\Gamma,
\mathfrak A.
$$

若：

$$
G
\Rightarrow_{ES}
G[S\mapsto M_S]
$$

並有：

$$
ES-EncapCert(S,M_S),
$$

則 parent-visible：

$$
\boxed{
Sig_\partial
+
Config_\partial
+
En_\partial
+
Auth_\partial
+
Residual_\partial
}
$$

皆被保存。

這比「只保存 causal reachability」更完整。

---

# 26. Configuration Execution

General CEES execution state：

$$
\boxed{
C_t\in Config(\mathcal E_G).
}
$$

若：

$$
C_t\vdash e
$$

且：

$$
C_t\cup\{e\}\in Con,
$$

則：

$$
\boxed{
C_t
\xrightarrow{e,c}
C_{t+1}
=
C_t\cup\{e\}.
}
$$

 $c$ 是 event execution certificate。

---

# 27. Conflict Progress

若兩個候選：

$$
e_a,e_b
$$

都 individual enabled，

但：

$$
\{e_a,e_b\}\notin Con,
$$

則系統不能把兩者當 parallel batch。

應輸出：

$$
\boxed{
BranchChoice[
e_a\# e_b
].
}
$$

---

# 28. Limbo 與 Unresolved Branch

若：

- 多個 branch 都合法；
- 沒有 policy 可以安全選；
- caller 未要求任意選擇；

則：

$$
\boxed{
Residual[
BranchDecisionRequired(
\{B_1,\ldots,B_k\}
)
].
}
$$

因此 Limbo 再次不是 error。

---

# 29. Select 與 Branch

原 Select profile：

$$
Family[\sigma]
\Rightarrow
Family[\sigma].
$$

在 event semantics 下，可進一步分：

## Filter

刪除不合法候選。

## Choose

從互斥 branch 中承諾一個 configuration extension。

所以：

$$
\boxed{
Filter
\neq
CommitChoice.
}
$$

CommitChoice 必須寫入 history。

---

# 30. Branch Choice History

若：

$$
C
\xrightarrow{e_a}
C_a
$$

與：

$$
C
\xrightarrow{e_b}
C_b
$$

互斥，

一旦選：

$$
e_a,
$$

History 必須保存：

$$
\boxed{
ChoiceWitness(
C,
e_a,
Alternatives=\{e_b,\ldots\},
Policy,
Cert
).
}
$$

這是 future replay / governance 所需資料。

---

# 31. Same Outcome / Different Choice

即使：

$$
\Pi_Q(C_a)
=
\Pi_Q(C_b),
$$

仍應檢查：

$$
EnabledFuture(C_a)
\stackrel{?}{\simeq}
EnabledFuture(C_b).
$$

若不同：

$$
\boxed{
ChoiceHistory
}
$$

不可丟。

---

# 32. History-Preserving Quotient

若要合併兩個 event-history states，

較合理的標準不是普通 state-output equality，而是某種 history-preserving behavioural equivalence。

ON-RDSS 暫時不自造完整 bisimulation theory。

先定義工程級：

$$
\boxed{
HPQ_Q(C_1,C_2)
}
$$

要求：

- observable equivalence；
- future enabling equivalence；
- conflict profile equivalence；
- authority equivalence；
- recursive branch correspondence。

---

# 33. Dynamic Causality 與 Meta

一般 event structure 的：

$$
Con,
\vdash
$$

通常固定於一個 semantics snapshot。

但 ON-RDSS 允許：

$$
\mathcal M_t:
\mathfrak A_t
\to
\mathfrak A_{t+1}.
$$

因此：

$$
\boxed{
\mathcal E_t
\neq
\mathcal E_{t+1}
}
$$

可能成立。

例如 Meta event 可以：

- add enabling；
- remove enabling；
- add conflict；
- resolve conflict；
- change branch policy。

---

# 34. Event Semantics Versioning

執行 trace 必須保存：

$$
\boxed{
EventSemanticsVersion.
}
$$

因為同一：

$$
C
$$

在：

$$
\mathcal E_t
$$

與：

$$
\mathcal E_{t+1}
$$

下可能具有不同：

$$
Enabled(C).
$$

---

# 35. Dynamic Causality 不是普通事件

若事件：

$$
m
$$

的 effect 是：

$$
modify(\vdash)
$$

或：

$$
modify(Con),
$$

則：

$$
\boxed{
Meta(m)=1.
}
$$

並需：

$$
MetaCert.
$$

不能讓普通 runtime event 靜默改寫 event semantics。

---

# 36. Branch Critical Pairs

新增：

## BCP-1 Alternative Cause

同一事件：

$$
c
$$

可由：

$$
A\vdash c,
\qquad
B\vdash c.
$$

不同 cause witness 是否可商掉？

## BCP-2 Conflict Choice

$$
e_a\# e_b.
$$

選不同 branch 是否 future-equivalent？

## BCP-3 Projection Erasure

projection 把：

$$
e_a,e_b
$$

都映成同一 observable label，是否錯誤合併 branch？

## BCP-4 Meta-Conflict

Meta 改變：

$$
Con
$$

後，原本互斥事件可能變可共存，或反之。

## BCP-5 Enabling Rewrite

Meta 改變：

$$
Alt(e).
$$

Replay 是否仍能重現舊 branch？

---

# 37. Event Structure Residuals

新增：

$$
\boxed{
Residual[
Conflict(
e_a,e_b
)
]
}
$$

$$
\boxed{
Residual[
BranchDecisionRequired
]
}
$$

$$
\boxed{
Residual[
EnablingMissing(
X,e
)
]
}
$$

$$
\boxed{
Residual[
EventVersionMismatch
]
}
$$

$$
\boxed{
Residual[
HistoryQuotientUnsafe
]
}
$$

---

# 38. Event Progress Candidate

對有限、固定 version、可判定 CEES configuration：

至少一項成立：

$$
\boxed{
Terminal
\lor
EnabledEvent
\lor
ParallelStep
\lor
BranchChoice
\lor
TypedResidual.
}
$$

其中 ParallelStep 要求新增 event set：

$$
A
$$

整體 consistency 與 enabling 合法。

---

# 39. Parallel Step

對：

$$
A\subseteq E\setminus C,
$$

允許：

$$
C\xrightarrow{A}C\cup A
$$

至少要求：

1. $C\cup A\in Con$ ；
2. 每個 $e\in A$ 的 enabling predecessors 已在 $C$ 或此次 step 的合法 internal dependency closure 中；
3. authority / certificates 全部成立。

第一版可先限制為所有 $e\in A$ 已由 $C$ 各自 enabled。

---

# 40. CEES Type Safety 候選

由 v0.7 / v0.8 擴張：

$$
\boxed{
Safety_{CEES}
=
BoundaryBehaviourPreservation
+
ConfigurationConsistency
+
EnablingPreservation
+
EffectAccounting
+
ExplicitBranchResidual
+
MetaVersionSafety.
}
$$

---

# 41. 有限 Checker：Conflict Erasure

Checker 建立互斥 outcomes：

$$
o_a\# o_b.
$$

真正 boundary configurations：

$$
\boxed{
\varnothing,
\{o_a\},
\{o_b\}.
}
$$

Naive macro 額外允許：

$$
\boxed{
\{o_a,o_b\}.
}
$$

結果：

$$
\boxed{
conflict\_erasure\_detected=true.
}
$$

---

# 42. 有限 Checker：Disjunctive Enabling

建立：

$$
\{a\}\vdash c,
$$

$$
\{b\}\vdash c.
$$

Checker 確認：

$$
\{a,c\}
$$

可達，

以及：

$$
\{b,c\}
$$

可達。

若誤壓成：

$$
\{a,b\}\vdash c,
$$

兩個單因 branch 都消失。

所以：

$$
\boxed{
OR\ Cause
\neq
AND\ Cause.
}
$$

---

# 43. 有限 Checker：Same Observation / Different Future

兩個 configuration：

$$
C_A=\{a,r_a\},
$$

$$
C_B=\{b,r_b\}.
$$

Projection 都是：

$$
r.
$$

但：

$$
Enabled(C_A)=\{f_a\},
$$

$$
Enabled(C_B)=\{f_b\}.
$$

結果：

$$
\boxed{
observational\_projection\_same=true,
}
$$

但：

$$
\boxed{
future\_capability\_differs=true.
}
$$

這直接驗證「現在看起來一樣」不足以安全商掉 history。

---

# 44. 有限 Checker：Boundary Enabling Summary

對 output：

$$
c
$$

得到最小 enabling family：

$$
\boxed{
En_\partial(c)
=
\{
\{a\},
\{b\}
\}.
}
$$

因此 macro boundary 需要「enabling alternatives family」，不能只存一組 predecessors。

---

# 45. 這一輪對 v0.8 的修正

v0.8：

$$
M_S
=
(
Sig_\partial,
R_\partial,
\mathcal P_S,
Auth,
Hist,
Cert
).
$$

v0.9 改成：

$$
\boxed{
M_S
=
(
Sig_\partial,
BC_S,
\mathcal E_S,
Auth,
Hist,
Cert
)
}
$$

而：

$$
BC_S
=
(
Con_\partial,
En_\partial,
Residual_\partial,
Version
).
$$

$$
R_\partial
$$

降為 derived index。

---

# 46. 新的 Authority / Index 類比

完整 boundary behaviour：

$$
\boxed{
BC_S
}
$$

像 canonical authority。

快速 causal reachability：

$$
\boxed{
R_\partial
=
Index(BC_S).
}
$$

因此：

$$
\boxed{
BoundaryBehaviour
\neq
BoundaryReachabilityIndex.
}
$$

這再次與 RDSS Runtime 的單一 authority / rebuildable index 原則同構。

---

# 47. 下一步

下一輪最值得處理：

1. **Certified Effect Event Structure 的正式 formation rules**；
2. configuration typing；
3. conflict inheritance；
4. enabling certificate；
5. branch quotient safety；
6. history-preserving behavioural equivalence；
7. dynamic causality Meta transitions；
8. event-structure encapsulation theorem proof skeleton；
9. event-structure minimisation / folding interface；
10. CEES checker 由 toy pairwise conflict 升級 general consistency family。

---

# 48. 暫定結論

ON-RDSS 的 effect semantics 現在走過：

$$
\boxed{
EffectWord
}
$$

$$
\longrightarrow
$$

$$
\boxed{
EffectPomset
}
$$

$$
\longrightarrow
$$

$$
\boxed{
CertifiedEffectEventStructure.
}
$$

對應能力：

$$
\boxed{
Sequence
}
$$

$$
\to
$$

$$
\boxed{
Concurrency
}
$$

$$
\to
$$

$$
\boxed{
Concurrency
+
Conflict
+
AlternativeCause
+
BranchHistory.
}
$$

而 recursive container 的安全封裝條件也從：

$$
\boxed{
BoundaryType
+
BoundaryCausality
}
$$

升級為：

$$
\boxed{
BoundaryType
+
BoundaryConsistency
+
BoundaryEnabling
+
Authority
+
History
+
Version.
}
$$

所以目前最重要的新原則是：

> **封裝不只不能創造不存在的因果；它也不能創造不存在的共同可能性、不能刪除合法替代原因，也不能把具有不同未來能力的歷史分支只因當前輸出相同就商成同一狀態。**
