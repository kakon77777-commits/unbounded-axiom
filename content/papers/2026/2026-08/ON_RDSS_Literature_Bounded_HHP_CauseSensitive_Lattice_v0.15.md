# Operator-Native RDSS：Literature-Bounded HHP 與 Cause-Sensitive Verification Lattice
## Separating Exact Bounded Backtracking Semantics from Runtime Approximation

**版本：** v0.15 Working Verification Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** bounded HHP 定義校正／Cause-Sensitive CBHHP 實作／Verification Grade 多軸化  
**前置：** ON-RDSS v0.13–v0.14

---

# 摘要

v0.14 提出 ON-RDSS Runtime bounded checker：

$$
BHHP_k
$$

並以 recursive rollback-depth 的方式建立：

$$
BHHP_0=HP.
$$

本版重新核對 Fröschle–Hildebrandt 1999 / Hildebrandt dissertation 原始 bounded-backtracking 定義後，進行一個重要命名修正。

文獻中的：

$$
\boxed{
(n)\text{-HHPB}
}
$$

是：

> 將 HHPB 的 backtracking requirement 限制到 run 尾端最近的 $n+1$ transitions。

原文正式條件使用：

$$
last(r,t)\ge |r|-n.
$$

因此：

$$
\boxed{
(0)\text{-HHPB}=HPB.
}
$$

而且：

$$
\boxed{
HHPB
\subseteq
\cdots
\subseteq
(n+1)\text{-HHPB}
\subseteq
(n)\text{-HHPB}
\subseteq
\cdots
\subseteq
HPB.
}
$$

文獻並構造對每個 $n$ 都存在：

$$
(n)\text{-HHPB}
$$

但非：

$$
(n+1)\text{-HHPB}
$$

的有限 nets。

因此本版正式區分：

$$
\boxed{
LitHHP_n
}
$$

與：

$$
\boxed{
RBHHP_k.
}
$$

前者指文獻 bounded semantics；

後者指 ON-RDSS v0.14 的 recursive runtime verification grade。

除非後續完成形式等價證明，不再混用兩者。

---

# 1. 文獻 $(n)$ -HHPB

對 synchronous run：

$$
r
$$

與 backtrack-enabled transition：

$$
t,
$$

文獻 $(n)$ -hereditary condition 要求：

只有當：

$$
\boxed{
last(r,t)\ge |r|-n
}
$$

時才強制 backtracking closure。

也就是只允許檢查 run 尾端最近：

$$
\boxed{
n+1
}
$$

個位置的 removable transitions。

---

# 2. 文獻 indexing

因此：

$$
\boxed{
LitHHP_0=HP.
}
$$

$$
LitHHP_1
$$

比 HP 多一層尾端 backtracking sensitivity。

一般：

$$
\boxed{
LitHHP_{n+1}
\subseteq
LitHHP_n.
}
$$

而：

$$
\boxed{
HHP
=
\bigcap_{n\ge0}
LitHHP_n.
}
$$

---

# 3. Strict Hierarchy

文獻 Figure 6.2 提供一個參數化 net family：

$$
N_n,
N_n'
$$

使：

$$
\boxed{
N_n
\sim_{LitHHP_n}
N_n'
}
$$

但：

$$
\boxed{
N_n
\not\sim_{LitHHP_{n+1}}
N_n'.
}
$$

因此：

$$
\boxed{
LitHHP_n
}
$$

hierarchy 對所有有限 $n$ 都是 strict。

---

# 4. Strictness 的機制

文獻的 generic counterexample 具有：

$$
a_1,\ldots,a_n,
$$

$$
b_1,\ldots,b_n
$$

等長歷史，

在 critical：

$$
a_{n+1}',b_{n+1}'
$$

處可以選兩種匹配方式。

若選一種，

需要回退所有 $a$ histories 才會暴露：

$$
d
$$

mismatch。

若選另一種，

需要回退所有 $b$ histories 才會暴露：

$$
c
$$

mismatch。

 $(n)$ -bounded backtracking 看不到足夠深，

但：

$$
(n+1)
$$

可以。

---

# 5. ON-RDSS v0.14 的 RBHHP

v0.14 定義：

$$
\boxed{
RBHHP_0=HP
}
$$

並以：

> current-level forward matching + 一步 rollback 到前一級 relation

遞迴建立：

$$
RBHHP_{k+1}.
$$

這與「增加可追溯歷史深度」有相同設計直覺，

但目前未證：

$$
\boxed{
RBHHP_k
=
LitHHP_k.
}
$$

---

# 6. 為何保留 RBHHP？

RBHHP 有工程優勢：

- greatest-fixed-point implementation 直接；
- certificate 可以遞迴記錄 level；
- incremental cache 容易；
- 可以與 CauseSensitive mapping 共用 engine。

所以它仍是一個有用 Runtime grade。

但其名稱應保持：

$$
\boxed{
RuntimeBoundedHHP
}
$$

而非冒充 literature definition。

---

# 7. Literature Grade 與 Runtime Grade

正式分：

$$
\boxed{
VerificationFamily
\in
\{
LiteratureBounded,
RuntimeRecursive,
FullHHP
\}.
}
$$

Certificate 必須說明 family。

---

# 8. Cause-Sensitive CBHHP

General CEES runtime state：

$$
\boxed{
\widehat C
=
(C,\pi,\le_\pi,v).
}
$$

concrete causal realization：

$$
\boxed{
\widetilde e=(e,\kappa,v).
}
$$

本版完成第一個 Cause-Sensitive bounded checker。

---

# 9. Cause-Sensitive Forward Matching

對：

$$
\widehat C_1
\xrightarrow{(e_1,\kappa_1)}
\widehat C'_1,
$$

另一邊需：

$$
\widehat C_2
\xrightarrow{(e_2,\kappa_2)}
\widehat C'_2
$$

並滿足：

$$
\boxed{
Profile(e_1)=Profile(e_2)
}
$$

以及：

$$
\boxed{
f(\kappa_1)=\kappa_2.
}
$$

因此不是只有 output/event label matching。

---

# 10. Cause-Sensitive Backward Matching

只有 causal-maximal occurrence：

$$
\widetilde e
$$

可直接回退。

若 current realization map：

$$
f_r
$$

已建立，

另一邊必須回退：

$$
\boxed{
f_r(\widetilde e).
}
$$

不能重新挑另一個同 surface label occurrence。

---

# 11. $CBHHP_0$

定義：

$$
\boxed{
CBHHP_0
}
$$

為 cause-sensitive forward HP-like relation。

它要求：

- profile-preserving realization history isomorphism；
- chosen witness correspondence；
- forward back-and-forth。

---

# 12. $CBHHP_{k+1}$

ON-RDSS Runtime recursive版本：

$$
\boxed{
CBHHP_{k+1}
}
$$

再加一層沿 realization mapping 的 causal-maximal rollback obligation落入：

$$
CBHHP_k.
$$

---

# 13. Surface vs Cause-Sensitive 分離實驗

General CEES：

$$
\varnothing\vdash a,
$$

$$
\varnothing\vdash b,
$$

$$
\{a\}\vdash c,
$$

$$
\{b\}\vdash c.
$$

兩 histories：

$$
\widehat C_A:
c\text{ uses }\{a\},
$$

$$
\widehat C_B:
c\text{ uses }\{b\}.
$$

兩者 raw surface event set 完全一樣：

$$
\boxed{
C_A=C_B=\{a,b,c\}.
}
$$

---

# 14. 但 Cause 不同

$$
\boxed{
a<_{\pi_A}c,
}
$$

而：

$$
\boxed{
b<_{\pi_B}c.
}
$$

所以：

$$
\boxed{
SameSurfaceState=true,
}
$$

但：

$$
\boxed{
SameCausalOrder=false.
}
$$

---

# 15. Governance-Distinct Sources

若：

$$
Profile(a)
=
(A,source.A),
$$

$$
Profile(b)
=
(B,source.B),
$$

則 checker：

$$
\boxed{
CBHHP_0(\widehat C_A,\widehat C_B)=false.
}
$$

因此：

$$
\boxed{
SurfaceEquality
\not\Rightarrow
CauseSensitiveEquivalence.
}
$$

---

# 16. CauseMode 是非冗餘軸

這直接證明：

$$
\boxed{
CauseMode
\in
\{
Surface,
CauseSensitive
\}
}
$$

不是多餘 metadata。

它真的會改變 equivalence result。

---

# 17. Profile-Relative Cause Quotient

如果刻意令：

$$
Profile(a)=Profile(b),
$$

則兩 histories 可以藉由：

$$
a\leftrightarrow b
$$

互換形成 causal isomorphism。

Checker：

$$
\boxed{
SymmetricProfile\ CBHHP_0=true.
}
$$

因此：

$$
\boxed{
CauseSensitive
}
$$

也仍然 relative to chosen event-profile regime。

---

# 18. 三軸 Verification Grade

目前可以寫：

$$
\boxed{
VG
=
(
HistoryFamily,
CauseMode,
GovernanceMode
).
}
$$

---

# 19. HistoryFamily

$$
\boxed{
HistoryFamily
\in
\{
HP,
LitHHP_n,
RBHHP_k,
FullHHP
\}.
}
$$

---

# 20. CauseMode

$$
\boxed{
CauseMode
\in
\{
Surface,
CauseSensitive
\}.
}
$$

---

# 21. GovernanceMode

$$
\boxed{
GovernanceMode
\in
\{
BehaviourOnly,
Authority,
Authority+Residual,
FullGoverned
\}.
}
$$

---

# 22. Verification Grade 是 Partial Order

例如：

$$
(RBHHP_2,Surface,FullGoverned)
$$

和：

$$
(RBHHP_1,CauseSensitive,BehaviourOnly)
$$

不能單靠一個整數說誰更強。

因此：

$$
\boxed{
VG
}
$$

應視為多軸偏序。

---

# 23. Grade Certificate

$$
\boxed{
VQCert
=
(
Family,
Depth,
CauseMode,
GovernanceMode,
Scope,
EventVersion,
OperatorVersion,
CheckerVersion,
WitnessHash
).
}
$$

---

# 24. Forget Cause

若：

$$
Surface(\widehat C_1)
=
Surface(\widehat C_2)
$$

但：

$$
CauseSensitiveEq=false,
$$

則：

$$
\boxed{
ForgetCause
}
$$

不能是 silent operation。

需：

$$
\boxed{
ForgetCauseCert.
}
$$

---

# 25. Cause-Sensitive Residual

若 Runtime 只做 surface quotient，

但 caller 要求 causal provenance，

可輸出：

$$
\boxed{
Residual[
CauseEquivalenceUnchecked
].
}
$$

若 causal check 直接失敗：

$$
\boxed{
Residual[
CauseHistoriesDiverge
].
}
$$

---

# 26. Meta 與 CauseMode

Meta 可能改：

$$
Alt_v(e).
$$

所以舊：

$$
CBHHP_k^v
$$

certificate 在：

$$
v+1
$$

必須 stale。

因為 causal realization space：

$$
Real_v(C)
$$

本身已改變。

---

# 27. Maximal Causes 與 Runtime Index

文獻的 bounded-HHP decidability proof 指出：

> 要維持新增 event 後的 pomset isomorphism，不必永遠保存全部過去；保存可作為新事件 maximal causes 的最近歷史即可。

這對 ON-RDSS 很重要。

可以定義：

$$
\boxed{
CauseFrontier(C)
=
\text{potential maximal causes}.
}
$$

作為快速 index。

---

# 28. CauseFrontier 不等於 Full History

$$
\boxed{
CauseFrontier
=
Index(History).
}
$$

它有利於：

- incremental type/effect check；
- future event matching；
- bounded verification。

但 authority source 仍是完整 history / certificate ledger。

---

# 29. 與 GCMS / History Compression 類型問題的接口

抽象來說，history memory 可壓成：

$$
M_t
$$

只要對指定 query / verification mode 保持足夠資訊。

對 bounded HHP，

一個自然 query 就是：

> 哪些 past events 仍可能成為未來 extension 的 maximal causes或 backtracking targets？

因此可研究：

$$
\boxed{
HistoryCompression_{VG}
}
$$

相對 verification grade 的最小充分記憶。

---

# 30. 文獻 Strict-Hierarchy Fixture Family

下一步不需要再自行猜 $k=2$ fixture。

文獻已給：

$$
\boxed{
Fixture_n^{Lit}
}
$$

使：

$$
LitHHP_n=true,
$$

$$
LitHHP_{n+1}=false.
$$

所以應把 Figure 6.2 的參數化 net family正式翻譯成 machine-readable benchmark。

---

# 31. Figure 6.2 翻譯工作的限制

目前文字解析已足以確認：

- generic $a_i,b_i$ history；
- critical $a_{n+1},b_{n+1}$ / alternative matching；
- backtrack all $a$ exposes $d$ ；
- backtrack all $b$ exposes $c$ ；
- strictness theorem。

但圖的精確 place/arc 拓撲仍需可靠讀圖／人工轉錄後再寫 checker。

在完成此步前，不自行捏造 Petri-net arcs。

---

# 32. 新的 Verification Backend 分層

## Fast Index

- current projection；
- profile hash；
- CauseFrontier；
- bounded future summary。

## Runtime Strong Check

- RBHHP $_k$ ；
- CBHHP $_k$。

## Literature-Compatible Formal Check

- LitHHP $_n$ ；
- full HHP。

## Offline Proof

- event-structure / Petri-net theorem prover；
- future Lean/Coq formalization。

---

# 33. 暫定結論

本版最重要的不是再增加一個 $k$。

而是把「bounded history equivalence」拆成兩個不能混淆的東西：

$$
\boxed{
LitHHP_n
}
$$

是有明確文獻定義與 strict hierarchy theorem 的 bounded-backtracking semantics。

$$
\boxed{
RBHHP_k
}
$$

是 ON-RDSS 為 Runtime 設計的 recursive verification grade。

同時：

$$
\boxed{
CBHHP_k
}
$$

證明 CauseMode 是一條真正獨立的 verification axis。

所以 ON-RDSS 的 state-equivalence certificate 現在最合理的形式不是：

$$
Equivalent=true.
$$

而是：

$$
\boxed{
Equivalent[
Family,
Depth,
CauseMode,
GovernanceMode,
Scope,
Version,
Cert
].
}
$$

這讓「同一個 State」從一個含糊判斷，變成一個可追溯的、分域的、分強度的驗證聲明。
