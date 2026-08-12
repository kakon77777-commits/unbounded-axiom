# Operator-Native RDSS：Bounded Backtracking Equivalence 與 Cause-Sensitive Verification
## Runtime Verification Grades between HP and Full HHP

**版本：** v0.14 Working Verification Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS Branch Quotient 的 bounded-backtracking Runtime approximation／Cause-Sensitive HHP 接口  
**前置：** ON-RDSS v0.11–v0.13

---

# 摘要

v0.13 已完成經典：

$$
\boxed{
HP=true,\qquad HHP=false
}
$$

regression，並驗證：

- plain HP forward checker；
- explicit backward HHP checker；
- hereditary downward-closure HHP checker；

能在同一有限 benchmark 上正確分離 HP 與 HHP。

本版進一步建立：

$$
\boxed{
BHHP_k
}
$$

作為 ON-RDSS Runtime 的有限 backtracking verification grade。

本版採用保守命名：

> **ON-RDSS BHHP $_k$ 是受到 bounded-backtracking HP/HHP hierarchy 啟發的 Runtime approximation。**

在尚未逐條形式對照 Fröschle–Hildebrandt 1999 原始 indexing 前，不宣稱本版 $BHHP_k$ 與該論文 bounded bisimulation 的定義完全相同。

第一代定義：

$$
\boxed{
BHHP_0=HP.
}
$$

而：

$$
BHHP_{k+1}
$$

在保持 current-level forward matching 的同時，要求所有沿當前 history mapping 的一階 backward move 必須落入：

$$
BHHP_k.
$$

因此：

$$
\boxed{
BHHP_{k+1}\subseteq BHHP_k.
}
$$

在經典 HP-not-HHP regression 上，checker 得到：

$$
\boxed{
BHHP_0=true,
}
$$

但：

$$
\boxed{
BHHP_1=false.
}
$$

所以該 fixture 只需一層 mapped backtracking 就已被區分。

---

# 1. 外部理論接口

Fröschle–Hildebrandt 研究 HP 與 HHP 之間的差異，並定義 bounded backtracking hierarchy。

其結果包括：

- 每個有限 bounded level 可判定；
- hierarchy 是 strict；
- 所以不存在一個固定有限 bound 可一般替代 full HHP。

因此 ON-RDSS 不應把：

$$
BHHP_1
$$

或任一固定：

$$
BHHP_k
$$

誤稱為 full HHP。

---

# 2. Runtime 為什麼仍需要有限 $k$？

Full HHP 的強度適合：

- formal folding；
- irreversible StateMerge；
- governance-critical quotient；
- offline proof。

但即時 Runtime 常需要：

- bounded cost；
- local decision；
- incremental revalidation；
- budget-aware verification。

所以定義：

$$
\boxed{
VerificationGrade
=
BHHP_k.
}
$$

它不是「比較不真的等價」，而是：

> **在最多 $k$ 層 mapped historical rollback obligation 下通過驗證。**

---

# 3. Base Level

令：

$$
R_0
=
R_{HP}^{\ast}.
$$

也就是所有滿足：

- history/profile isomorphism；
- forward-left matching；
- forward-right matching；

的 greatest fixed point。

因此：

$$
\boxed{
BHHP_0=HP.
}
$$

---

# 4. Recursive Level

假設：

$$
R_k
$$

已定義。

 $R_{k+1}$ 先限制於：

$$
R_k,
$$

再要求：

## Forward

所有 forward extensions 在：

$$
R_{k+1}
$$

內互相匹配。

## Backward-left

若：

$$
(C_1,f,C_2)\in R_{k+1}
$$

且：

$$
C_1\xleftarrow{e_1}C_1',
$$

令：

$$
e_2=f(e_1).
$$

必須：

$$
C_2\xleftarrow{e_2}C_2'
$$

並：

$$
\boxed{
(C_1',f|_{C_1'},C_2')\in R_k.
}
$$

## Backward-right

對稱成立。

---

# 5. 為什麼 Backward Target 是 $R_k$？

這使：

$$
R_{k+1}
$$

比：

$$
R_k
$$

多承擔一層不可重新映射的歷史 obligation。

直覺：

$$
BHHP_0
$$

只看 forward。

$$
BHHP_1
$$

問：

> 如果現在退一步，原 mapping 還站得住嗎？

$$
BHHP_2
$$

再問：

> 退一步後的 relation 本身，還能再退一步嗎？

依此類推。

---

# 6. Monotonicity Candidate

由構造：

$$
\boxed{
R_{k+1}\subseteq R_k.
}
$$

所以安全強度單調增加：

$$
\boxed{
BHHP_0
\succeq
BHHP_1
\succeq
BHHP_2
\succeq
\cdots
}
$$

此處 $\succeq$ 表示「前者等價關係較粗」。

---

# 7. Full HHP 的位置

理想極限：

$$
\boxed{
R_\infty
=
\bigcap_{k\ge0}R_k.
}
$$

是否對本定義在一般所選模型類中恰等於 standard HHP，需要另行形式證明。

目前只將：

$$
FullHHP
$$

保留為獨立 exact checker。

所以：

$$
\boxed{
BHHP_k
\neq
FullHHP
}
$$

除非另有證書。

---

# 8. 經典 Fixture

沿用 v0.13：

$$
A=
((a+c)\parallel b)
+
(a\parallel b)
+
(a\parallel(b+c)),
$$

$$
B=
((a+c)\parallel b)
+
(a\parallel(b+c)).
$$

已知：

$$
HP(A,B)=true,
$$

$$
HHP(A,B)=false.
$$

---

# 9. $BHHP_0$

Checker：

$$
\boxed{
BHHP_0(A,B)=true.
}
$$

relation size：

$$
\boxed{
|R_0|=17.
}
$$

---

# 10. $BHHP_1$

加入一層 mapped backward obligation 後：

$$
\boxed{
BHHP_1(A,B)=false.
}
$$

relation size：

$$
\boxed{
|R_1|=10.
}
$$

所以該 fixture 的最低分離層：

$$
\boxed{
k_{\min}=1.
}
$$

---

# 11. 更深層 Relation Size

Checker 得：

$$
|R_0|=17,
$$

$$
|R_1|=10,
$$

$$
|R_2|=4,
$$

$$
|R_3|=0.
$$

之後維持：

$$
0.
$$

驗證：

$$
\boxed{
|R_{k+1}|
\le
|R_k|.
}
$$

---

# 12. 這不代表一層 Backtracking 永遠足夠

原 bounded-backtracking literature 證明 hierarchy strict。

所以必然存在更複雜系統，使：

$$
BHHP_1
$$

不足、

需要更深 historical challenge。

因此經典 fixture 只是：

$$
\boxed{
\text{cheap but meaningful regression}.
}
$$

不是 hierarchy collapse 的證據。

---

# 13. Runtime Verification Grade

建議正式定義：

$$
\boxed{
VG
\in
\{
Obs,
Future,
HP,
BHHP_1,
BHHP_2,
\ldots,
FullHHP,
FullHHP+Gov
\}.
}
$$

---

# 14. Verification Certificate

$$
\boxed{
VQCert
=
(
Mode,
k,
Scope,
SnapshotVersion,
RelationHash,
CheckerVersion,
ProfileRegime,
AuthorityRegime,
ResidualRegime
).
}
$$

若：

$$
Mode=BHHP,
$$

則必須明示：

$$
k.
$$

---

# 15. 不能把 $BHHP_k$ 通過寫成 Full HHP

例如：

$$
BHHP_2(C_1,C_2)=true
$$

只能輸出：

$$
\boxed{
CertifiedEquivalent[
Grade=BHHP_2
].
}
$$

不能輸出：

$$
HHP=true.
$$

---

# 16. Stronger Check Residual

如果 Runtime budget 到：

$$
k=2
$$

就停止，

可以輸出：

$$
\boxed{
Residual[
StrongerHistoryEquivalenceUnchecked(
CurrentGrade=BHHP_2
)
].
}
$$

這符合 ON-RDSS explicit residual semantics。

---

# 17. Verification Budget

定義：

$$
\boxed{
VB
=
(
Grade,
MaxBacktrack,
Scope,
TimeBudget,
MemoryBudget,
CertificateLevel
).
}
$$

例如：

## UI state grouping

$$
VB=(HP,0,local,low).
$$

## planner cache merge

$$
VB=(BHHP_1,1,local,medium).
$$

## governance state merge

$$
VB=(FullHHP,\infty,affected-subgraph,high).
$$

---

# 18. Adaptive Verification

可以先：

$$
HP.
$$

若 parent state 後續要：

- write；
- commit；
- delete；
- schema change；

才逐步提升：

$$
HP
\to
BHHP_1
\to
BHHP_2
\to
FullHHP.
$$

因此 verification strength 可以按 decision risk 動態加碼。

---

# 19. 不同 Grade 的 State Identity

Parent-state registry 可寫：

$$
\boxed{
StateIdentity
=
(
ClassID,
Q,
Version,
Grade,
CertID
).
}
$$

因此：

$$
SameClassID
$$

但：

$$
Grade=HP
$$

與：

$$
Grade=HHP
$$

仍是不同 verification claims。

---

# 20. Meta 造成 Grade 失效

若：

$$
\mathfrak E_v
\to
\mathfrak E_{v+1},
$$

原：

$$
BHHP_k^v
$$

certificate 應標：

$$
Stale.
$$

然後重新驗證：

$$
BHHP_k^{v+1}.
$$

Meta 不可直接繼承舊 relation。

---

# 21. Cause-Sensitive HHP 的資料接口

v0.12：

$$
\widehat C
=
(C,\pi,\le_\pi,v).
$$

因此 bounded checker 未來應由：

$$
(C_1,f,C_2)
$$

升級成：

$$
\boxed{
(
\widehat C_1,
f_r,
\widehat C_2
).
}
$$

---

# 22. Causal Realization

每次具體 event occurrence：

$$
\boxed{
\widetilde e
=
(e,\kappa,v).
}
$$

其中：

- $e$：surface event；
- $\kappa$：chosen enabling witness；
- $v$：semantics version。

---

# 23. Cause-Sensitive Forward Move

$$
\widehat C
\xrightarrow{\widetilde e}
\widehat C'.
$$

若：

$$
\widetilde e_1
$$

要匹配：

$$
\widetilde e_2,
$$

至少要求：

$$
Profile(e_1)=Profile(e_2)
$$

並且 chosen causes 在現有 mapping 下對應：

$$
\boxed{
f_r(\kappa_1)
\simeq
\kappa_2.
}
$$

---

# 24. Cause-Sensitive Backward Move

只有 concrete causal history 中 maximal occurrence 可回退：

$$
\boxed{
\widehat C
\xleftarrow{\widetilde e}
\widehat C'.
}
$$

另一邊必須回退：

$$
f_r(\widetilde e).
$$

不能只找任意：

$$
q(\widetilde e')
=
q(\widetilde e).
$$

---

# 25. Surface HHP 與 Cause-Sensitive HHP

定義：

$$
\boxed{
SurfaceHHP
}
$$

只保存 surface event identity / history。

而：

$$
\boxed{
CauseHHP
}
$$

保存 causal realization：

$$
(e,\kappa,v).
$$

一般：

$$
\boxed{
CauseHHP
\Rightarrow
SurfaceHHP
}
$$

但反向不應預設成立。

---

# 26. ForgetCause Certificate

若想把：

$$
CauseHHP
$$

降為：

$$
SurfaceHHP,
$$

需要：

$$
\boxed{
ForgetCauseCert.
}
$$

也就是所有 task-relevant causal realizations在 quotient scope 中可被安全商掉。

---

# 27. Cause-Sensitive $BHHP_k$

自然定義：

$$
\boxed{
CBHHP_k
}
$$

其中：

$$
CBHHP_0
=
\text{cause-sensitive forward HP},
$$

而每增加一層：

$$
k+1
$$

都要求沿：

$$
f_r
$$

回退一個 concrete causal realization後落入：

$$
CBHHP_k.
$$

---

# 28. Verification Grade 二維化

因此最終 Grade 不一定只是一條軸。

可以寫：

$$
\boxed{
Grade
=
(
HistoryStrength,
CauseMode
).
}
$$

其中：

$$
HistoryStrength
\in
\{
HP,
BHHP_k,
HHP
\},
$$

$$
CauseMode
\in
\{
Surface,
CauseSensitive
\}.
$$

---

# 29. Grade 範例

$$
(HP,Surface)
$$

最便宜。

$$
(BHHP_2,Surface)
$$

加入有限 rollback。

$$
(BHHP_2,CauseSensitive)
$$

有限 rollback + 原因保真。

$$
(HHP,CauseSensitive)
$$

最強、最昂貴。

---

# 30. Governance 再成第三軸

若再加：

$$
GovernanceMode
\in
\{
BehaviourOnly,
Auth,
Auth+Residual,
FullGoverned
\},
$$

完整 Verification Grade：

$$
\boxed{
VG
=
(
HistoryStrength,
CauseMode,
GovernanceMode
).
}
$$

這開始像真正可調 Runtime verification lattice。

---

# 31. Verification Lattice

不是一條單線：

$$
HP<HHP.
$$

而更像多軸偏序。

例如：

$$
(BHHP_1,CauseSensitive)
$$

與：

$$
(BHHP_2,Surface)
$$

未必可直接說誰「絕對更強」。

前者更保 cause，

後者更深 backtracking。

因此：

$$
\boxed{
VerificationGrade
}
$$

應該是 partial order，而不是單一整數。

---

# 32. 這和 RDSS 的判定域吻合

驗證結果必須綁定：

$$
\boxed{
Domain
+
Scope
+
Grade.
}
$$

不能離開判定域後說：

> 這兩個 states 就是同一個。

正確是：

> 在 $Q$ 、version $v$ 、grade $g$ 下，這兩個 histories 被證明可安全商化。

---

# 33. 下一步：Strict-Hierarchy Regression Family

既有文獻說 bounded hierarchy strict。

所以 ON-RDSS test suite 不應只有：

$$
k_{\min}=1.
$$

未來需要建立：

$$
\boxed{
Fixture_k
}
$$

使：

$$
BHHP_{k-1}=true,
$$

$$
BHHP_k=false.
$$

至少做：

$$
k=1,2,3
$$

作 regression family。

---

# 34. 下一步：General CEES Checker

把 prime structure 的：

$$
forward\_events,
backward\_events
$$

替換成 decorated history：

$$
forward(\widehat C)
$$

與：

$$
backward(\widehat C).
$$

然後直接重用：

$$
BHHP_k
$$

greatest-fixed-point engine。

---

# 35. 下一步：Certificate Cost Curve

記錄：

$$
Cost(BHHP_k)
$$

包括：

- triple count；
- mapping count；
- fixed-point rounds；
- memory；
- elapsed time。

建立：

$$
\boxed{
Strength
\leftrightarrow
VerificationCost.
}
$$

這會直接用於 Runtime adaptive verification。

---

# 36. 有限實驗結果

經典 fixture：

| Grade | Initial Related | Relation Size |
|---|---:|---:|
| $BHHP_0$ | Yes | 17 |
| $BHHP_1$ | No | 10 |
| $BHHP_2$ | No | 4 |
| $BHHP_3$ | No | 0 |

所以：

$$
\boxed{
k_{\min}=1.
}
$$

而 relation size 單調下降。

---

# 37. 暫定結論

ON-RDSS 現在不必在：

$$
HP
$$

與：

$$
FullHHP
$$

之間二選一。

可以建立：

$$
\boxed{
HP
=
BHHP_0
\supseteq
BHHP_1
\supseteq
BHHP_2
\supseteq
\cdots
}
$$

作 Runtime 有限歷史驗證層。

同時，v0.12 的 causal realization 又提供第二條 verification axis：

$$
\boxed{
Surface
\to
CauseSensitive.
}
$$

所以真正的 ON-RDSS verification grade 更像：

$$
\boxed{
VG
=
(
BacktrackingDepth,
CauseSensitivity,
GovernanceStrength,
Scope,
Version
).
}
$$

這代表：

> **「這兩個 State 是否相同」不再只有 Yes/No，而是必須同時回答：在哪個觀測域、哪個版本、保留多少因果歷史、允許回退多深、是否保留具體原因、以及治理義務檢查到哪一層。**
