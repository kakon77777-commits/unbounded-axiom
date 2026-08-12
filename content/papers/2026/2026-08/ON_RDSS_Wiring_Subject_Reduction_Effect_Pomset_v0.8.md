# Operator-Native RDSS：Wiring Subject Reduction 與因果 Effect Pomset
## Boundary-Preserving Encapsulation, Causal Effects, and Recursive Operator Wiring

**版本：** v0.8 Working Proof Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS 由 sequential operator words 推進至 parallel / recursive wiring graphs 的第一代形式化  
**前置：** ON-RDSS v0.3–v0.7

---

# 摘要

ON-RDSS v0.6–v0.7 已在有限 sequential operator words 上建立：

$$
\boxed{
\text{Typed Structural Preservation}
+
\text{Effect Accounting}
+
\text{Explicit Residual Progress}.
}
$$

但真正的 RDSS 不只包含序列。它還需要：

- branching；
- parallelism；
- multi-input / multi-output；
- recursive containers；
- local time；
- cross-container causal coupling。

因此 ordered effect word：

$$
\chi=[e_1,\ldots,e_n]
$$

不足以作為一般效應語義。

本文件將 effect trace 升級為有限 labeled partial order：

$$
\boxed{
\mathcal P_E
=
(E,\prec,\lambda)
}
$$

其中：

- $E$：effect event 集；
- $\prec$：嚴格因果偏序；
- $\lambda:E\to\mathcal E$：effect label。

它是一個 pomset-like effect object。

本文件並發現一個關鍵反例：

> **將具有多條獨立內部支線的 subgraph 粗暴壓成單一 macro event，可能憑空產生不存在的外部因果關係。**

因此 recursive encapsulation 必須保存：

$$
\boxed{
\text{Boundary Port Types}
+
\text{Boundary Causal Reachability}
+
\text{Internal Effect Witness}
+
\text{Authority Obligations}.
}
$$

而不能只保存一個 macro label。

---

# 1. 從 effect word 到 effect partial order

Sequential calculus 中：

$$
\chi
=
[e_1,\ldots,e_n].
$$

隱含：

$$
e_1\prec e_2\prec\cdots\prec e_n.
$$

對 parallel wiring，更一般應寫：

$$
\boxed{
\mathcal P_E
=
(E,\prec,\lambda).
}
$$

若：

$$
e_a\parallel e_b,
$$

表示：

$$
\neg(e_a\prec e_b)
\land
\neg(e_b\prec e_a).
$$

因此並行不必先被強迫線性化。

---

# 2. Pomset-like effect semantics

本版只要求有限 labeled poset：

$$
\boxed{
\mathcal P
=
(E,\le,\lambda).
}
$$

不立即加入完整 event-structure 的 conflict / enabling 結構。

原因是目前主要問題是：

- causality；
- concurrency；
- encapsulation；
- boundary preservation。

若之後要處理：

- mutually exclusive branches；
- nondeterministic choice；
- alternative enabling histories；

可再升級為 event-structure semantics。

---

# 3. Linearization

一條 sequential effect trace：

$$
\chi=[e_1,\ldots,e_n]
$$

可視為 $\mathcal P_E$ 的 linear extension。

因此：

$$
\boxed{
WordTrace
\subset
PomsetTrace.
}
$$

多個不同 effect words 若只是對真正 concurrent events 採不同 linearization，可對應同一 causal pomset。

---

# 4. Typed Wiring Graph

定義：

$$
\boxed{
G
=
(
V,
E_w,
P^{in},
P^{out},
Ty,
Op,
Auth
).
}
$$

其中：

- $V$：operator nodes；
- $E_w$：typed wires；
- $P^{in},P^{out}$：node ports；
- $Ty$：port sort assignment；
- $Op$：node → typed-effect operator；
- $Auth$：node authority obligations。

一條 wire：

$$
e:
(v,p_{out})
\to
(w,p_{in})
$$

只有在：

$$
Ty(v,p_{out})
=
Ty(w,p_{in})
$$

或有合法 bridge elaboration 時成立。

---

# 5. Wiring Typing Judgment

寫：

$$
\boxed{
\Gamma
\vdash
G
:
\vec\sigma
\Rightarrow
\vec\tau
\;!\;
\mathcal P_E
\;@\;
d.
}
$$

其中：

- $\vec\sigma$：external input port signature；
- $\vec\tau$：external output port signature；
- $\mathcal P_E$：effect causal poset；
- $d=\max_{v\in V}Depth(Op(v))$。

---

# 6. Effect Event Generation

每個 node：

$$
v\in V
$$

可產生一個或多個 effect events：

$$
Eff(v)
=
\{e_{v,1},\ldots,e_{v,k}\}.
$$

每個 node 自己的 local effect trace 提供 local order：

$$
e_{v,1}\prec\cdots\prec e_{v,k}.
$$

---

# 7. Wire-Induced Causality

如果 wire：

$$
v\to w
$$

承載 $w$ 執行所需資料／控制依賴，

則加入：

$$
\boxed{
last(Eff(v))
\prec
first(Eff(w)).
}
$$

若 wire 只是 observational reference，不構成 execution dependency，必須明示不同 wire kind。

所以：

$$
\boxed{
Wire
\neq
Automatically\ Causal.
}
$$

第一代 checker 暫將 data-flow wire 視為 causal。

---

# 8. Local Time 與因果偏序

不同 container 可以有：

$$
\mathbb T_i,
\mathbb T_j.
$$

Effect pomset 不要求把兩個 clock 強制映射為 total order。

只需：

$$
e_a\prec_c e_b
$$

在存在因果 witness 時成立。

因此：

$$
\boxed{
CausalOrder
\neq
AdministrativeTotalOrder.
}
$$

---

# 9. Recursive Encapsulation 問題

令：

$$
S\subseteq V
$$

為欲封裝 subgraph。

直覺上希望：

$$
G
\Rightarrow_w
G/S
$$

其中 $S$ 被 macro operator：

$$
M_S
$$

取代。

但：

$$
\boxed{
M_S
}
$$

不能一般地只是一個單一 effect event。

---

# 10. False-Causality Counterexample

考慮：

$$
p\to a
$$

以及：

$$
b\to q
$$

其中：

$$
a,b\in S,
$$

但內部沒有：

$$
a\leadsto b
$$

或：

$$
b\leadsto a.
$$

原系統中：

$$
\boxed{
p\not\prec q.
}
$$

若把：

$$
S=\{a,b\}
$$

粗暴壓成單點：

$$
M,
$$

得到：

$$
p\to M\to q.
$$

於是錯誤導出：

$$
\boxed{
p\prec q.
}
$$

因此：

$$
\boxed{
\text{Naive Single-Event Contraction}
}
$$

一般不保持 causal semantics。

---

# 11. 反例的意義

這表示：

$$
\boxed{
Container
\neq
AtomicEvent.
}
$$

即使 parent layer 把 container 顯示為一個 node，

它在 causal semantics 上仍必須保留足夠的 boundary dependency structure。

---

# 12. Boundary Ports

對 subgraph $S$ 定義：

## Incoming boundary wires

$$
B^-_S
=
\{
e:u\to v
\mid
u\notin S,\;
v\in S
\}.
$$

## Outgoing boundary wires

$$
B^+_S
=
\{
e:v\to u
\mid
v\in S,\;
u\notin S
\}.
$$

---

# 13. Boundary Signature

從 internal port type 得：

$$
\boxed{
Sig_\partial(S)
=
(
In_\partial(S),
Out_\partial(S)
).
}
$$

封裝後 macro：

$$
M_S
$$

必須具有**完全相同 boundary sort signature**。

---

# 14. Boundary Causal Reachability

對：

$$
b_i^-\in B^-_S,
\qquad
b_j^+\in B^+_S
$$

定義：

$$
\boxed{
b_i^-
\rightsquigarrow_S
b_j^+
}
$$

當且僅當 incoming boundary 所進入的 internal node / event 能透過 $S$ 內的 causal path 到達 outgoing boundary 所離開的 internal node / event。

定義矩陣／關係：

$$
\boxed{
R_\partial(S)
\subseteq
B^-_S\times B^+_S.
}
$$

---

# 15. Open Macro Operator

因此 macro 不應只有：

$$
M_S:
\vec\sigma\to\vec\tau.
$$

而應帶：

$$
\boxed{
M_S
=
(
Sig_\partial,
R_\partial,
\mathcal P_S,
Auth_S,
HistWitness_S,
Cert_S
).
}
$$

其中：

- $Sig_\partial$：boundary types；
- $R_\partial$：boundary causal summary；
- $\mathcal P_S$：opaque internal effect pomset；
- $Auth_S$：internal required authorities；
- $HistWitness_S$：replay/provenance；
- $Cert_S$：encapsulation certificate。

---

# 16. 為什麼同時保留 $R_\partial$ 與 $\mathcal P_S$？

 $R_\partial$ 供 parent layer 快速推理：

> 哪個 external input 可能因果影響哪個 external output？

 $\mathcal P_S$ 則供：

- debugging；
- replay；
- deeper expansion；
- history reconstruction；
- critical-pair analysis。

所以：

$$
\boxed{
BoundarySummary
\neq
InternalHistory.
}
$$

---

# 17. Wiring Structural Reduction

定義：

$$
\boxed{
G
\Rightarrow_w
G[S\mapsto M_S].
}
$$

只有存在：

$$
EncapCert(S,M_S)
$$

才允許。

---

# 18. EncapCert 最小義務

$$
\boxed{
EncapCert
=
TypePres
\land
BoundaryCausalPres
\land
AuthorityPres
\land
HistoryReconstructible
\land
VersionPinned.
}
$$

必要時再加入：

- resource summary；
- QoS；
- failure contract；
- local-time interface。

---

# 19. Lemma W1 — Boundary Type Preservation

若：

$$
EncapCert(S,M_S)\downarrow,
$$

則：

$$
\boxed{
Sig_\partial(S)
=
Sig_\partial(M_S).
}
$$

### 證明骨架

Macro 的 input/output ports 由 crossing wires 對應的 internal boundary ports逐一產生。

因此封裝不改變 external wire endpoint 所要求的 sort。

若需要 bridge，bridge 必須在封裝前或 macro interface 中顯式存在，不得由封裝暗中插入。

---

# 20. Lemma W2 — Boundary Causal Preservation

令：

$$
ExtReach_G
$$

表示 external nodes / boundary observations 間由 $G$ 導出的 causal reachability。

若 macro 的：

$$
R_\partial(M_S)
=
R_\partial(S),
$$

則：

$$
\boxed{
ExtReach_G
=
ExtReach_{G/S}.
}
$$

在忽略 internal identities 的外部觀測域成立。

---

# 21. W2 證明骨架

任一穿越 $S$ 的 external causal path 可唯一拆成：

$$
external\ prefix
+
boundary\ in
+
internal\ causal\ segment
+
boundary\ out
+
external\ suffix.
$$

中間 internal segment：

$$
b_i^-\leadsto_S b_j^+
$$

由：

$$
(b_i^-,b_j^+)
\in R_\partial(S)
$$

表示。

封裝後以 macro boundary dependency 取代 internal segment。

反方向，macro 不允許不存在於：

$$
R_\partial(S)
$$

的 boundary pair。

因此既不遺失真 causal path，也不新增 false causal path。

---

# 22. Naive Contraction 為什麼失敗？

單一 macro event 隱含：

$$
\boxed{
R_\partial^{naive}
=
B^-_S
\times
B^+_S.
}
$$

即：

> 每個 boundary input 都因果影響每個 boundary output。

只有在原 subgraph 確實滿足：

$$
R_\partial(S)
=
B^-_S\times B^+_S
$$

時，單一因果 event contraction 才安全。

---

# 23. Atomic-Encapsulation Criterion

因此得到一個新的判定：

$$
\boxed{
AtomicCausal(S)
\iff
R_\partial(S)
=
B^-_S\times B^+_S.
}
$$

若成立，可安全用單一 causal macro event 表示。

若不成立，只能：

1. 使用 port-sensitive macro；
2. 保存 internal pomset；
3. 或將 subgraph 拆成多個 causal components。

---

# 24. Causal Component Decomposition

令 internal causal graph 的 connected / reachability components 為：

$$
S_1,\ldots,S_k.
$$

若：

$$
k>1,
$$

則將 $S$ 壓成一個 atomic event通常過粗。

可以輸出：

$$
\boxed{
M_S
=
\{
M_{S_1},
\ldots,
M_{S_k}
\}
}
$$

或一個有多 causal zones 的 open macro。

---

# 25. Lemma W3 — Authority Obligation Preservation

定義 subgraph authority requirement：

$$
\boxed{
AuthReq(S)
=
\bigcup_{v\in S}
AuthReq(v).
}
$$

封裝不能因 implementation 被隱藏而刪除：

$$
state.write,
audit.append,
schema.write,
\ldots
$$

等義務。

要求：

$$
\boxed{
AuthReq(M_S)
\succeq
AuthReq(S)
}
$$

其中 $\succeq$ 表示 macro authorization policy 至少能覆蓋所有實際 internal required capabilities。

---

# 26. Authority 不等於向外公開所有權限

Preserve obligation 不代表 parent caller 直接獲得：

$$
AuthReq(S).
$$

應區分：

$$
\boxed{
RequiredAuthority
}
$$

與：

$$
\boxed{
DelegatedAuthority.
}
$$

Macro 可內部持有 capability，但 external contract 只暴露可呼叫接口。

---

# 27. Lemma W4 — History Reconstructibility

封裝後至少保存：

$$
\boxed{
HistWitness(M_S)
}
$$

使在需要 replay / debug 時可以恢復：

$$
\mathcal P_S,
$$

或者取得等價的 execution trace / provenance record。

因此：

$$
\boxed{
Encapsulation
\neq
HistoryErasure.
}
$$

---

# 28. Effect Pomset Preservation

若不展開 internal events，parent-level effect object可表示為：

$$
\boxed{
\mathcal P_{G/S}
=
Contract_\partial(
\mathcal P_G,
\mathcal P_S,
R_\partial(S)
).
}
$$

Contract 的要求不是 event-count preservation，而是：

$$
\boxed{
ExternalCausalReachabilityPreservation.
}
$$

---

# 29. Strong vs Weak Effect Preservation

## Strong

保留完整 internal effect pomset：

$$
\mathcal P_S
$$

作 opaque nested object。

## Weak

只保留：

$$
R_\partial(S)
$$

與 effect summaries。

Strong 適合：

- replay；
- debugging；
- proof。

Weak 適合：

- fast scheduling；
- parent-level planning。

---

# 30. Wiring Subject Reduction Theorem Candidate

**定理 WT1 — Boundary-Preserving Wiring Subject Reduction**

固定：

$$
\Gamma,
\mathfrak A.
$$

若：

$$
\Gamma
\vdash
G:
\vec\sigma
\Rightarrow
\vec\tau
!
\mathcal P_E
@
d
$$

且：

$$
G
\Rightarrow_w
G'
$$

由合法 encapsulation：

$$
S\mapsto M_S
$$

產生，

並滿足：

$$
EncapCert(S,M_S),
$$

則：

$$
\boxed{
\Gamma
\vdash
G':
\vec\sigma
\Rightarrow
\vec\tau
!
\mathcal P_E'
@
d'
}
$$

並有：

$$
\boxed{
d'=d
}
$$

對純 structural encapsulation，

以及：

$$
\boxed{
ExtReach(\mathcal P_E)
=
ExtReach(\mathcal P_E').
}
$$

此外：

$$
\boxed{
AuthObligation_G
\simeq
AuthObligation_{G'}
}
$$

在 capability accounting 意義下成立。

---

# 31. WT1 不要求什麼？

不要求：

$$
|\mathcal P_E|
=
|\mathcal P_E'|.
$$

封裝本來就可以減少 parent-level visible events。

不要求 internal event identity 在 parent view 直接可見。

只要求：

- boundary types；
- observable causal structure；
- authority obligations；
- replay witness；

保持。

---

# 32. Wiring Progress / Residual

若 wiring edge type mismatch：

$$
\tau\not\sim\sigma,
$$

則：

$$
\boxed{
Residual[
WireTypeMismatch(
edge,\tau,\sigma
)
].
}
$$

若缺 bridge：

$$
Residual[
WireBridgeRequired
].
$$

若形成 causal cycle，而該 operator profile 禁止 cycle：

$$
Residual[
CausalCycle
].
$$

若 authority 不足：

$$
Residual[
AuthorityRequired
].
$$

---

# 33. Feedback 不能直接當 cycle error

某些 wiring 語義合法允許 feedback。

因此：

$$
\boxed{
GraphCycle
\neq
AutomaticallyInvalid.
}
$$

需區分：

- combinational illegal cycle；
- delayed/stateful feedback；
- fixed-point feedback；
- recursive call；
- causal loop prohibited by domain。

所以 cycle legality 本身是 profile / certificate 問題。

---

# 34. Wiring Critical Pairs

新的 wiring 層 critical pairs 包括：

## WCP-1 Overlapping Encapsulation

兩個 subgraphs：

$$
S_1\cap S_2\neq\varnothing.
$$

封裝順序是否影響 boundary summary？

## WCP-2 Parallel Encapsulation

$$
S_1\cap S_2=\varnothing.
$$

兩個 independent encapsulation 是否 commute？

## WCP-3 Bridge-vs-Encapsulation

先補 Bridge 再封裝，與先封裝再在 macro boundary 補 Bridge 是否等價？

## WCP-4 Meta-vs-Encapsulation

封裝途中 Operator Algebra version 改變。

## WCP-5 Projection-vs-Encapsulation

先 coarse-grain internal events，是否破壞 boundary causality？

---

# 35. 有限反例 Checker：Example A

原 wiring：

$$
p\to a,
$$

$$
b\to q,
$$

而：

$$
a\parallel b.
$$

封裝：

$$
S=\{a,b\}.
$$

原 external reachability：

$$
\boxed{
\varnothing.
}
$$

Naive single macro：

$$
p\to M\to q
$$

產生：

$$
\boxed{
\{(p,q)\}.
}
$$

因此 checker：

$$
\boxed{
naive\_introduces\_false\_p\_to\_q=true.
}
$$

---

# 36. Example A：Boundary Summary

因 $a$ 無法到 $b$，

所以：

$$
R_\partial(S)
=
\varnothing.
$$

使用 boundary summary 封裝後：

$$
ExtReach_{summary}
=
\varnothing.
$$

checker：

$$
\boxed{
boundary\_summary\_preserves=true.
}
$$

---

# 37. 有限 Checker：Example B

真正 sequential internal path：

$$
p\to a\to b\to q.
$$

此時：

$$
R_\partial(S)
=
\{
(in_0,out_0)
\}.
$$

原：

$$
p\prec q.
$$

summary encapsulation 後仍：

$$
p\prec q.
$$

checker：

$$
\boxed{
preserved=true.
}
$$

---

# 38. Boundary Type 實測

兩個例子的 visible boundary signature 都可以是：

$$
Input:X,
\qquad
Output:W.
$$

但它們的：

$$
R_\partial
$$

不同。

這直接證明：

$$
\boxed{
SameBoundaryTypes
\not\Rightarrow
SameCausalSemantics.
}
$$

所以 macro interface 若只有 input/output types 仍然不夠。

---

# 39. Authority 實測

內部 subgraph：

$$
x,y
$$

分別需要：

$$
state.write,
$$

$$
audit.append.
$$

封裝後至少仍需記：

$$
\boxed{
AuthReq(M)
=
\{
state.write,
audit.append
\}
}
$$

作為內部 capability obligations。

封裝不能因 parent view 看不到內部 node 就把 authority debt 消掉。

---

# 40. 與 Wiring Diagram / Open Systems 數學的接口

Wiring-diagram operads 已有成熟方法描述：

- typed boxes；
- ports；
- hierarchical nesting；
- recursive plug-and-play composition。

Open-system cospan 方法則把 boundary interface 作為組合核心。

ON-RDSS 不需要重新發明「有 boundary 的 compositional graph」概念。

本框架新增研究重點在：

$$
\boxed{
\text{partial legality}
+
\text{effect causality}
+
\text{certificates}
+
\text{authority}
+
\text{history}
+
\text{meta-version}.
}
$$

---

# 41. 與 Pomset / Event-Structure 語義的接口

Pomset 將 word 的 total order 放寬成 partial order，適合表示真正並行 effect。

Event structures 進一步能表示：

- causal dependency；
- consistency / conflict；
- alternative enabling。

因此本版採 pomset-like effect object作為第一步。

若 ON-RDSS 下一步處理 nondeterministic branch / conflicting choices，應升級：

$$
\boxed{
EffectPomset
\rightarrow
CertifiedEffectStructure.
}
$$

---

# 42. 與 Graph Rewriting Concurrency 的接口

既有 graph rewriting 已有 concurrency theorem 類結果，研究兩個 sequential rewrites 在何種條件下可以等價組成 concurrent rule，並研究 associativity。

ON-RDSS 的 wiring structural reduction 可利用這些結果作後端。

但 ON-RDSS 需要額外檢查：

- operator type；
- effect pomset；
- authority；
- certificate；
- history；
- dynamic algebra version。

---

# 43. 新的 Effect Safety

Sequential v0.7：

$$
EffectTrace
=
\chi\in\mathcal E^\ast.
$$

Wiring v0.8：

$$
\boxed{
EffectTrace
=
\mathcal P_E
=
(E,\prec,\lambda).
}
$$

因此 Effect Accounting 也升級成：

$$
\boxed{
ExecutedConfiguration
\cup
RemainingConfiguration
}
$$

而不只是 prefix / suffix。

---

# 44. Configuration

對 effect pomset $\mathcal P_E$，

一個已執行 configuration：

$$
C\subseteq E
$$

至少應 downward-closed：

$$
\boxed{
e\in C
\land
e'\prec e
\Rightarrow
e'\in C.
}
$$

這代表不能執行 effect 卻漏掉其 causal predecessors。

---

# 45. Parallel Effect Accounting

若：

$$
C_{done}
$$

為已執行 downward-closed configuration，

剩餘：

$$
E_{rem}
=
E\setminus C_{done}.
$$

History 記：

$$
\boxed{
H'
=
H
\oplus
Trace(
C_{done},
\mathcal P_E,
Cert
).
}
$$

所以 sequential prefix accounting 是這個概念的特殊情形。

---

# 46. 下一個 theorem candidate

## WT2 — Configuration Effect Accounting

若：

$$
C_{done}
$$

是 effect pomset 的合法 configuration，

則所有已執行 event 的 causal predecessors 均已 accounting，

而 remaining effect structure由：

$$
\mathcal P_E\restriction(E\setminus C_{done})
$$

加上 boundary cause obligations表示。

這會成為 parallel Runtime effect safety 的核心。

---

# 47. 下一輪真正要做的事

1. 正式定義 effect configuration；
2. 處理 conflict / nondeterministic branch；
3. 由 pomset 升級 event structure；
4. 實作 wiring encapsulation checker 完整版；
5. 自動計算 $R_\partial(S)$ ；
6. 自動檢測 false causality；
7. 實作 overlapping encapsulation critical pairs；
8. 證 WT1 的圖論 proof skeleton；
9. 建立 WT2 configuration accounting；
10. 將 recursive container 的 parent projection 改成 boundary causal contract。

---

# 48. 暫定結論

ON-RDSS 到本版完成一個重要跨越：

$$
\boxed{
Sequential\ Operator\ Word
}
$$

正式推進為：

$$
\boxed{
Typed\ Recursive\ Operator\ Wiring.
}
$$

同時：

$$
\boxed{
Ordered\ Effect\ Word
}
$$

推進為：

$$
\boxed{
Causal\ Effect\ Pomset.
}
$$

而最重要的新原則是：

$$
\boxed{
\text{Encapsulation may hide structure, but may not invent causality.}
}
$$

以及：

$$
\boxed{
\text{Encapsulation may hide implementation, but may not erase type, authority, history, or causal obligations.}
}
$$

這使 RDSS 原先「狀態／容器／程序在不同尺度可互換」的命題第一次得到一個嚴格限制：

> **只有當跨尺度封裝保存 boundary typing 與 boundary causal semantics 時，Container 才能在父層安全地被當成一個高階 operator node。**
