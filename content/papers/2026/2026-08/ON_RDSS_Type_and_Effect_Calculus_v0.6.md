# Operator-Native RDSS Type-and-Effect Calculus
## Formation, Preservation, Effect Accounting, and Explicit Residuals

**版本：** v0.6 Working Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS 第一代型別—效果演算／Subject Reduction 候選定理／有限 checker 驗證

---

# 摘要

本文在 ON-RDSS v0.5 的統一算子形式：

$$
\mathsf{Op}
[
\vec\sigma
\Rightarrow
\tau
\;!\;
\epsilon
\;@\;
d
]
$$

上建立第一代 Type-and-Effect Calculus。

本輪最重要的修正有三項。

第一，effect 不再只是一個無序集合。ON-RDSS 已明確承認 non-commutativity、History 與 reduction-path relevance，因此 effect annotation 若僅使用：

$$
\epsilon_1\cup\epsilon_2
$$

會錯誤地把：

$$
A;B
$$

與：

$$
B;A
$$

視為同一效果。本文改用：

$$
\boxed{
\chi
=
[e_1,\ldots,e_n]
}
$$

作為保序 effect trace，另可從 $\chi$ 提取 effect summary。

第二，Subject Reduction 被拆為：

$$
\boxed{
\text{Structural Preservation}
}
$$

與：

$$
\boxed{
\text{Execution Effect Accounting}.
}
$$

結構 reduction 只做合法封裝／巨集化，不應改變外部型別與 effect trace；真正 execution 則可以消耗 effect，但必須把已執行 effect 寫入 trace / history，使「已執行 + 剩餘」仍可重構原 effect obligation。

第三，傳統 progress 被改為：

$$
\boxed{
\text{Progress or Explicit Residual}.
}
$$

若一個 operator word 無法繼續，不把它變成 $0$ 、False 或假輸出，而必須產生帶型、帶義務的 residual。

---

# 1. 外部數學接口

Type-and-effect systems 的成熟思想是：type 描述計算可產生何種值，而 effect 額外描述計算可能發生的行為。ON-RDSS 採用此分離，但把 effect 擴張為：

- state mutation；
- relation formation；
- projection / loss；
- authority；
- certificate generation；
- history update；
- meta rewrite。

本文不主張發明 type-and-effect system；研究重點是將 effect discipline 與 partial composition、certificates、history、meta-depth 和 residual semantics 接合。

---

# 2. Sorts

第一代 sorts：

$$
\boxed{
\sigma,\tau
::=
State
\mid
Relation
\mid
Family[\sigma]
\mid
View[\sigma]
\mid
Candidate
\mid
Cert
\mid
Evidence
\mid
History
\mid
Algebra[d]
\mid
Residual[\omega].
}
$$

其中：

$$
Residual[\omega]
$$

保存尚未解除的 obligation $\omega$。

---

# 3. Effects

定義 effect alphabet：

$$
\boxed{
\mathcal E
=
\{
realize,
mutate,
relate,
select,
project,
loss,
judge,
witness,
authority,
history,
io,
meta,
rewrite,
\ldots
\}.
}
$$

---

# 4. Effect Trace

不用純集合，而使用：

$$
\boxed{
\chi
\in
\mathcal E^\ast.
}
$$

例如：

$$
\chi
=
[
realize,
mutate,
project
].
$$

順序一般具有語義：

$$
\boxed{
[e_a,e_b]
\not\equiv
[e_b,e_a].
}
$$

---

# 5. Effect Summary

為了快速靜態檢查，可另外定義：

$$
\boxed{
Summary(\chi)
=
\epsilon.
}
$$

例如：

$$
Summary(
[
mutate,
project,
mutate
]
)
=
\{
mutate,
project
\}.
$$

因此：

$$
\boxed{
EffectSummary
\neq
EffectTrace.
}
$$

前者可用於 conservative capability checking；後者保存 history / order。

---

# 6. Certified Effect Commutation

不是所有 effect 都不可交換。

定義 context-relative independence：

$$
\boxed{
I_\Gamma
\subseteq
\mathcal E\times\mathcal E.
}
$$

若：

$$
(e_a,e_b)\in I_\Gamma
$$

並有：

$$
CommCert_\Gamma(e_a,e_b),
$$

才允許：

$$
\boxed{
[\chi_1,e_a,e_b,\chi_2]
\equiv_{\Gamma}
[
\chi_1,e_b,e_a,\chi_2].
}
$$

這建立一種 trace-like partial commutation。

若沒有 certificate：

$$
mutate;project
$$

不得因 effect set 相同而交換。

---

# 7. Operator Typing

統一 judgment：

$$
\boxed{
\Gamma
\vdash
O
:
\vec\sigma
\Rightarrow
\tau
\;!\;
\chi
\;@\;
d.
}
$$

其中：

- $\vec\sigma$：輸入 sorts；
- $\tau$：輸出 sort；
- $\chi$：ordered effect trace；
- $d$：meta-depth。

---

# 8. Formation Rule — Realize

$$
\frac{
}{
\Gamma
\vdash
R
:
()
\Rightarrow
State
!
[realize]
@0
}
\;\textsc{T-Realize}
$$

---

# 9. Formation Rule — Transform

$$
\frac{
\Gamma\vdash \sigma\ \mathsf{sort}
\qquad
\Gamma\vdash \tau\ \mathsf{sort}
}{
\Gamma
\vdash
T
:
\sigma
\Rightarrow
\tau
!
[mutate]
@0
}
\;\textsc{T-Transform}
$$

特化 State transition：

$$
State
\Rightarrow
State.
$$

---

# 10. Formation Rule — Relate

$$
\frac{
\Gamma\vdash \sigma_1\ \mathsf{sort}
\qquad
\Gamma\vdash \sigma_2\ \mathsf{sort}
}{
\Gamma
\vdash
L
:
(\sigma_1,\sigma_2)
\Rightarrow
Relation
!
[relate]
@0
}
\;\textsc{T-Relate}
$$

---

# 11. Formation Rule — Select

$$
\frac{
\Gamma\vdash\sigma\ \mathsf{sort}
}{
\Gamma
\vdash
S
:
Family[\sigma]
\Rightarrow
Family[\sigma]
!
[select]
@0
}
\;\textsc{T-Select}
$$

附 side condition：

$$
Supp(S(X))
\subseteq
Supp(X).
$$

---

# 12. Formation Rule — Certify

$$
\frac{
\Gamma\vdash Candidate\ \mathsf{sort}
}{
\Gamma
\vdash
C
:
Candidate
\Rightarrow
Cert
!
[judge,witness]
@0
}
\;\textsc{T-Certify}
$$

Certificate 必須 proof-relevant。

---

# 13. Formation Rule — Meta

$$
\frac{
d\ge0
}{
\Gamma
\vdash
M
:
(Algebra[d],Evidence)
\Rightarrow
Algebra[d+1]
!
[meta,rewrite]
@(d+1)
}
\;\textsc{T-Meta}
$$

第一版採單調 meta-depth。

後續可考慮同層 rewrite 與降階 realization。

---

# 14. Partial Executability Judgment

Typing 不表示可執行：

$$
\Gamma
\vdash
O:
\vec\sigma\Rightarrow\tau!\chi@d
$$

仍需：

$$
\boxed{
\Gamma;\mathcal C
\vdash
O\downarrow.
}
$$

 $\mathcal C$ 可包括：

- authority；
- resource；
- bridge；
- runtime availability；
- certificate；
- freshness。

---

# 15. Sequential Composition Typing

若：

$$
\Gamma
\vdash
O_1
:
\vec\sigma
\Rightarrow
\tau
!
\chi_1
@
d_1
$$

以及 unary continuation：

$$
\Gamma
\vdash
O_2
:
\tau
\Rightarrow
\upsilon
!
\chi_2
@
d_2,
$$

且 composition certificate 成立，則：

$$
\boxed{
\Gamma
\vdash
O_2\diamond O_1
:
\vec\sigma
\Rightarrow
\upsilon
!
(\chi_1\cdot\chi_2)
@
\max(d_1,d_2).
}
$$

其中：

$$
\cdot
$$

是 effect-trace concatenation。

---

# 16. 為什麼不是 $\chi_1\cup\chi_2$？

因：

$$
[mutate,project]
$$

與：

$$
[project,mutate]
$$

可能具有：

$$
Summary(\chi_1)=Summary(\chi_2),
$$

但語義不同。

因此 sequential composition 預設使用：

$$
\boxed{
\chi_1\cdot\chi_2.
}
$$

只有得到 commutation certificate 才能 quotient。

---

# 17. Multi-input Wiring Typing

若：

$$
O:
(\sigma_1,\ldots,\sigma_n)
\Rightarrow
\tau
!
\chi_O
@
d_O
$$

而每一輸入 wiring：

$$
W_i:
\vec\rho_i
\Rightarrow
\sigma_i
!
\chi_i
@
d_i,
$$

則在 port / authority / bridge certificates 完整時：

$$
\boxed{
O\circ(W_1,\ldots,W_n)
:
(\vec\rho_1,\ldots,\vec\rho_n)
\Rightarrow
\tau
!
\chi_{\mathrm{wire}}
@
\max(d_O,d_1,\ldots,d_n).
}
$$

 $\chi_{\mathrm{wire}}$ 不預設只是任意線性化；並行 wiring 的 effect order 需由 causal / commutation semantics 決定。

---

# 18. Structural Reduction

定義：

$$
\boxed{
W
\Rightarrow_s
W'
}
$$

表示純 structural / macro reduction。

它：

- 不真正執行 effect；
- 不修改 authority；
- 不消耗 runtime resource；
- 只把 typed subword 封裝為等價 macro operator。

---

# 19. Structural Preservation 候選定理

**命題 SR-S**

若：

$$
\Gamma
\vdash
W:
\vec\sigma
\Rightarrow
\tau
!
\chi
@
d
$$

且：

$$
W
\Rightarrow_s
W',
$$

則存在：

$$
\chi'
$$

使：

$$
\Gamma
\vdash
W':
\vec\sigma
\Rightarrow
\tau
!
\chi'
@
d
$$

且：

$$
\boxed{
\chi'
\equiv_\Gamma
\chi.
}
$$

即：

- external input sorts 保持；
- output sort 保持；
- meta-depth 保持；
- effect trace 至少在 certified commutation congruence 下保持。

---

# 20. 強 Structural Preservation

若 structural reduction 不包含 effect reordering，則：

$$
\boxed{
\chi'
=
\chi.
}
$$

這是本輪 toy checker 實際驗證的版本。

---

# 21. Runtime Execution Step

另定義：

$$
\boxed{
\langle O,\rho,H\rangle
\xrightarrow{e,c}
\langle O',\rho',H'\rangle.
}
$$

其中：

- $\rho$：runtime environment/state；
- $e$：此次真正執行的 effect；
- $c$：execution certificate / trace record。

這與 structural reduction 分離。

---

# 22. Effect Accounting

若原 operator effect trace：

$$
\chi
=
[e_1,\ldots,e_n],
$$

執行 prefix：

$$
\chi_{done}
=
[e_1,\ldots,e_k],
$$

剩餘：

$$
\chi_{rem}
=
[e_{k+1},\ldots,e_n],
$$

要求：

$$
\boxed{
\chi
=
\chi_{done}
\cdot
\chi_{rem}.
}
$$

若允許 certified commutation：

$$
\boxed{
\chi
\equiv_\Gamma
\chi_{done}
\cdot
\chi_{rem}.
}
$$

---

# 23. Execution Preservation / Accounting 候選定理

**命題 SR-E**

若：

$$
\Gamma
\vdash
O:
\sigma
\Rightarrow
\tau
!
\chi
@
d
$$

且：

$$
\langle O,\rho,H\rangle
\xrightarrow{\chi_{done},c}
\langle O',\rho',H'\rangle,
$$

則：

$$
\Gamma
\vdash
O':
\sigma'
\Rightarrow
\tau
!
\chi_{rem}
@
d'
$$

並要求：

$$
\boxed{
\chi
\equiv_\Gamma
\chi_{done}\cdot\chi_{rem},
}
$$

同時：

$$
\boxed{
H'
=
H
\oplus
Trace(\chi_{done},c).
}
$$

這不是傳統「effect 完全不變」，而是 effect obligation 的保守會計。

---

# 24. Meta Execution 的額外條件

若：

$$
meta\in\chi_{done},
$$

則允許：

$$
d'
\neq d
$$

或：

$$
\mathfrak A'
\neq
\mathfrak A.
$$

但必須產生：

$$
\boxed{
AlgebraVersionTransitionCertificate.
}
$$

非 Meta execution 不得任意改變：

$$
\mathfrak A.
$$

---

# 25. Typed Residual

若某一步 composition 期待：

$$
\sigma
$$

卻收到：

$$
\tau,
\qquad
\tau\not\sim_\Gamma\sigma,
$$

不輸出普通 value。

而輸出：

$$
\boxed{
Residual[
TypeMismatch(
actual=\tau,
expected=\sigma,
location=i
)
].
}
$$

---

# 26. Bridge Residual

若 type 可透過 bridge 修正但 bridge 尚缺：

$$
\boxed{
Residual[
BridgeRequired(
\tau\rightsquigarrow\sigma
)
].
}
$$

這不是 terminal failure。

未來加入：

$$
B:\tau\rightharpoonup\sigma
$$

後可 resume reduction。

---

# 27. Certificate Residual

若形式作用可能成立，但缺證書：

$$
\boxed{
Residual[
CertificateRequired(
rule,
scope,
authority
)
].
}
$$

---

# 28. Explicit Residual Progress

傳統 progress 常寫：

> well-typed closed term 不是 value，就是能繼續一步。

ON-RDSS 需要更寬版本。

**候選命題 PR-R**

對一個 well-formed operator word $W$，在固定 Algebra Snapshot 與有限檢查條件下，以下至少一項成立：

1. $W$ 已是 executable normal form；
2. 存在 certified structural reduction：
   $$
   W\Rightarrow_s W';
   $$
3. 存在 runtime execution step；
4. 產生明確 typed residual：
   $$
   Residual[\omega].
   $$

因此：

$$
\boxed{
Progress
\lor
ExplicitResidual.
}
$$

---

# 29. Residual 不是 Type Error 的遮羞布

只有在：

$$
\omega
$$

包含完整：

- expected sort；
- actual sort；
- failed rule；
- bridge possibility；
- required cert；
- AlgebraSnapshotID；

時才算 typed residual。

否則：

$$
\boxed{
UnknownFailure
}
$$

不能被包裝成合法 Limbo。

---

# 30. Subject Reduction 的證明策略

正式證明可按 reduction rule 歸納。

對每個 structural rule：

$$
r:
W_l
\Rightarrow_s
W_r,
$$

都需證：

## Interface preservation

$$
In(W_l)=In(W_r).
$$

## Output preservation

$$
Out(W_l)=Out(W_r).
$$

## Meta-depth preservation

$$
Depth(W_l)=Depth(W_r).
$$

## Effect preservation

$$
Effect(W_l)
\equiv_\Gamma
Effect(W_r).
$$

## Obligation preservation

$$
Obl(W_r)
\subseteq
Closure(Obl(W_l)\cup Cert(r)).
$$

---

# 31. Critical Pair 與 Type Preservation

即使每個 reduction rule individually preserves typing，不同 path：

$$
W\Rightarrow^\ast N_1,
$$

$$
W\Rightarrow^\ast N_2
$$

仍可能：

$$
Effect(N_1)
\not\equiv
Effect(N_2).
$$

因此 type preservation 不推出 confluence。

需要另外證：

$$
\boxed{
CriticalPairJoinability.
}
$$

---

# 32. Subject Reduction 與 History

若兩條路徑都保持：

$$
\sigma\Rightarrow\tau,
$$

卻：

$$
\chi_1\not\equiv\chi_2,
$$

則：

$$
\boxed{
\text{same type}
\neq
\text{same computation}.
}
$$

這正是 ON-RDSS 不把 subject reduction 誤當成 process equality 的原因。

---

# 33. Effect Trace 與部分交換

若：

$$
I_\Gamma
$$

是一個 certified independence relation，

可以將 effect words 依：

$$
ab\sim ba
\quad
\text{when }(a,b)\in I_\Gamma
$$

商化。

這與 partially commutative trace / trace-monoid 的數學語言相鄰。

ON-RDSS 不預設所有 effects 的 independence；Independence 本身需要 Cert。

---

# 34. 本輪 Toy Checker

本輪有限 checker 使用：

```text
Sig(
  inputs,
  output,
  ordered effects,
  meta_depth
)
```

建立：

$$
R:
()
\Rightarrow
State
!
[realize]
@0,
$$

$$
T:
State
\Rightarrow
State
!
[mutate]
@0.
$$

---

# 35. Structural Preservation 實測

原 word：

$$
R;T;T
$$

得到：

$$
()
\Rightarrow
State
!
[realize,mutate,mutate]
@0.
$$

先 reduction：

$$
T;T
\Rightarrow
T_2,
$$

得到：

$$
R;T_2.
$$

再封裝：

$$
R;T_2
\Rightarrow
RT_2.
$$

兩輪結果都保持：

- inputs = $()$ ；
- output = State；
- effect trace =
  $[realize,mutate,mutate]$ ；
- meta-depth = 0。

因此 toy model：

$$
\boxed{
StructuralPreservation=true.
}
$$

---

# 36. Explicit Residual 實測

建立：

$$
R;P;T
$$

其中：

$$
P:
State
\Rightarrow
View
!
[project].
$$

執行到：

$$
P;T
$$

時：

$$
actual=View,
$$

$$
expected=State.
$$

checker 不輸出假 State，而得到：

$$
\boxed{
Residual[
TypeMismatch(
View,
State
)
].
}
$$

---

# 37. Effect Accounting 實測

對：

$$
\chi
=
[realize,mutate,mutate],
$$

消耗第一個 effect：

$$
\chi_{done}
=
[realize],
$$

$$
\chi_{rem}
=
[mutate,mutate],
$$

實測：

$$
\chi
=
\chi_{done}\cdot\chi_{rem}.
$$

再消耗兩個亦成立。

---

# 38. Certified Commutation 實測

toy independence relation 只允許：

$$
read_a
\parallel
read_b.
$$

因此：

$$
[read_a,read_b]
\Rightarrow
[read_b,read_a]
$$

成立。

但：

$$
[mutate,project]
$$

沒有 commutation certificate，

所以不能交換。

這驗證：

$$
\boxed{
\text{effect order preserved by default}.
}
$$

---

# 39. 目前第一個真正的 theorem candidate

因此 ON-RDSS 現在最值得正式證的是：

## Typed Structural Preservation Theorem

對固定：

$$
\Gamma,\mathfrak A
$$

若：

$$
\Gamma
\vdash
W:
\vec\sigma
\Rightarrow
\tau
!
\chi
@
d
$$

且：

$$
W
\Rightarrow_s
W',
$$

則：

$$
\boxed{
\Gamma
\vdash
W':
\vec\sigma
\Rightarrow
\tau
!
\chi'
@
d
}
$$

且：

$$
\boxed{
\chi'
\equiv_\Gamma\chi.
}
$$

---

# 40. 第二個 theorem candidate

## Effect Accounting Theorem

對 certified execution：

$$
W
\xrightarrow{\chi_{done}}
W',
$$

若初始 effect：

$$
\chi,
$$

則存在剩餘：

$$
\chi_{rem}
$$

使：

$$
\boxed{
\chi
\equiv_\Gamma
\chi_{done}\cdot\chi_{rem}.
}
$$

且：

$$
\boxed{
H'
=
H\oplus Trace(\chi_{done}).
}
$$

---

# 41. 第三個 theorem candidate

## Explicit Residual Progress

對 fixed algebra snapshot 中的 well-formed finite operator word：

$$
\boxed{
Executable
\lor
Reducible
\lor
ExecutableStep
\lor
TypedResidual.
}
$$

這將「停住」本身變成可分析結果。

---

# 42. 三個 theorem 之間的關係

$$
\boxed{
Preservation
}
$$

保證 reduction 不亂掉 type/effect interface。

$$
\boxed{
EffectAccounting
}
$$

保證真正執行不偷丟 side effects / history。

$$
\boxed{
ExplicitResidualProgress
}
$$

保證無法前進時不是 silent failure。

三者共同才比較接近 ON-RDSS 的 type safety。

---

# 43. ON-RDSS Type Safety 暫定式

可暫寫：

$$
\boxed{
\text{TypeSafety}_{ON}
=
Preservation
+
EffectAccounting
+
ExplicitResidualProgress.
}
$$

再加 governance：

$$
\boxed{
+
CertificateSoundness
+
MetaVersionSafety.
}
$$

---

# 44. 下一輪需要補的東西

1. 正式 sort formation；
2. subtyping / subeffect relation；
3. effect trace equivalence；
4. residual typing rules；
5. bridge insertion typing；
6. wiring typing；
7. structural subject-reduction proof skeleton；
8. execution accounting induction；
9. explicit residual progress proof；
10. Meta step 的 version-preservation rule。

---

# 45. 暫定結論

ON-RDSS 現在已經從：

$$
\text{萬物皆算子}
$$

往前推到：

$$
\boxed{
\text{萬物皆可用同一算子 schema 形式化，}
}
$$

但每個算子必須帶：

$$
\boxed{
\text{Sort}
+
\text{Arity}
+
\text{Ordered Effect Trace}
+
\text{MetaDepth}
+
\text{Certificate Obligations}.
}
$$

而每次計算不是只問：

> 有沒有 output？

而同時問：

> 型別是否保持？  
> effect 有沒有被完整會計？  
> 歷史是否被保存？  
> 不能繼續時留下的是什麼 residual？  
> 這次作用憑什麼合法？

因此 Type-and-Effect Calculus 開始成為 ON-RDSS 真正可驗證的形式核心。
