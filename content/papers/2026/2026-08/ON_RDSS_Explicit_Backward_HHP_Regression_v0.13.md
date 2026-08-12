# Operator-Native RDSS：Explicit Backward HHP 與 HP≠HHP Regression
## From Hereditary Closure to a Forward/Backward Bisimulation Game

**版本：** v0.13 Working Verification Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS Branch Quotient backend 的標準 HP/HHP regression 與 explicit-backward 驗證  
**前置：** ON-RDSS v0.9–v0.12

---

# 摘要

v0.11 的有限 Branch Quotient checker 已使用：

$$
(C_1,f,C_2)
$$

configuration triples、history isomorphism、forward/back matching 與 hereditary closure。

v0.12 又指出，General CEES 必須進一步比較：

$$
\widehat C
=
(C,\pi,\le_\pi,v).
$$

本版本先完成一個重要的 verification milestone：

$$
\boxed{
HP=true,
\qquad
HHP=false
}
$$

的經典 regression 已成功翻譯成有限 event-structure checker。

此外，我們同時實作：

1. **Plain HP greatest-fixed-point checker**：只檢查 forward extensions；
2. **Explicit Backward HHP checker**：除了 forward matching，再強制 matching histories 沿當前 bijection 做 backward moves；
3. **Downward-Closure HHP checker**：要求 relation 對 matched subconfigurations hereditary closed。

在經典 regression 上：

$$
\boxed{
R_{HHP}^{backward}
=
R_{HHP}^{downward}.
}
$$

因此兩種 HHP 實作在這個有限模型中 cross-check 成功。

---

# 1. 外部基準

經典 HP/HHP 文獻區分：

$$
\boxed{
HP
}
$$

與：

$$
\boxed{
HHP.
}
$$

Plain history-preserving bisimulation維持：

- configuration relation；
- event-history bijection；
- label / causal-order preservation；
- forward step matching。

Hereditary history-preserving bisimulation再加入：

> 已匹配 histories 在回退／取合法過去時仍必須保持 relation。

因此：

$$
\boxed{
HHP
\subseteq
HP.
}
$$

而一般為嚴格包含。

---

# 2. 經典 Regression 的 Process Expression

使用文獻給出的標準反例，重新加括號後：

$$
\boxed{
A
=
((a+c)\parallel b)
+
(a\parallel b)
+
(a\parallel(b+c)).
}
$$

而：

$$
\boxed{
B
=
((a+c)\parallel b)
+
(a\parallel(b+c)).
}
$$

其中：

- $+$：nondeterministic choice；
- $\parallel$：parallel composition。

---

# 3. A 的三個 Branch

## Branch A1

$$
(a+c)\parallel b.
$$

事件：

$$
a_1,c_1,b_1.
$$

其中：

$$
a_1\#c_1,
$$

而：

$$
b_1\parallel a_1,
\qquad
b_1\parallel c_1.
$$

---

## Branch A3

$$
a\parallel b.
$$

事件：

$$
a_3,b_3.
$$

且：

$$
\boxed{
a_3\parallel b_3.
}
$$

此 branch 沒有任何 $c$ alternative。

這正是 A 比 B 多出的關鍵 branch。

---

## Branch A2

$$
a\parallel(b+c).
$$

事件：

$$
a_2,b_2,c_2.
$$

其中：

$$
b_2\#c_2,
$$

而：

$$
a_2\parallel b_2,
\qquad
a_2\parallel c_2.
$$

---

# 4. B 的兩個 Branch

B 只有：

$$
(a+c)\parallel b
$$

與：

$$
a\parallel(b+c).
$$

因此 B 的每一個 parallel $a/b$ pair 都與某一邊存在額外 $c$ possibility。

A 的：

$$
a_3\parallel b_3
$$

則沒有。

---

# 5. 為什麼 HP 還是可以騙過去？

關鍵是：

$$
\boxed{
\text{HP matching can depend on the forward run.}
}
$$

如果 A 的 middle branch 先走：

$$
a_3,
$$

可以把它配到 B 第一 branch 的：

$$
a'_1.
$$

然後：

$$
b_3
\leftrightarrow
b'_1.
$$

但如果 A 先走：

$$
b_3,
$$

可以把它配到 B 第二 branch 的：

$$
b'_2,
$$

然後：

$$
a_3
\leftrightarrow
a'_2.
$$

因此 forward-only game 可以依線性化順序採不同 history mapping。

---

# 6. Checker 實際找到的兩種 HP Mapping

對：

$$
C_A=\{a_3,b_3\},
$$

HP relation 中存在：

$$
\boxed{
a_3\mapsto a'_1,
\qquad
b_3\mapsto b'_1
}
$$

以及：

$$
\boxed{
a_3\mapsto a'_2,
\qquad
b_3\mapsto b'_2.
}
$$

因此：

$$
\boxed{
HP(A,B)=true.
}
$$

---

# 7. Explicit Backward Transition

對 configuration：

$$
C
$$

定義：

$$
\boxed{
C
\xleftarrow{e}
C\setminus\{e\}
}
$$

當：

$$
C\setminus\{e\}
$$

仍是合法 configuration。

在 prime causal model 中，這等同刪除 causal-maximal event。

---

# 8. Backward Matching 不是重新選 Mapping

如果：

$$
(C_1,f,C_2)
$$

已在 relation 中，

且：

$$
C_1
\xleftarrow{e_1}
C'_1,
$$

HHP backward move 必須回退：

$$
\boxed{
e_2=f(e_1)
}
$$

而不能現在才重新挑另一個同 label event。

要求：

$$
C_2
\xleftarrow{e_2}
C'_2
$$

並且：

$$
\boxed{
(
C'_1,
f|_{C'_1},
C'_2
)
\in R.
}
$$

這正是 HP run-dependent remapping 自由被封鎖的地方。

---

# 9. Explicit HHP Game

本版定義 relation：

$$
R
\subseteq
Conf(P_1)
\times
Iso
\times
Conf(P_2).
$$

對每個：

$$
(C_1,f,C_2)\in R
$$

同時要求：

## Forward-left

每個：

$$
C_1\xrightarrow{e_1}C'_1
$$

都有 matched：

$$
C_2\xrightarrow{e_2}C'_2.
$$

## Forward-right

反方向亦然。

## Backward-left

每個：

$$
C_1\xleftarrow{e_1}C'_1
$$

都必須由：

$$
e_2=f(e_1)
$$

匹配。

## Backward-right

反方向亦然。

---

# 10. Greatest Fixed Point

與 HP checker 一樣，先從全部合法 history-isomorphic triples：

$$
R_0
$$

開始。

反覆刪除任何無法滿足 forward/backward clauses 的 triple：

$$
R_0
\supseteq
R_1
\supseteq
\cdots
$$

直到：

$$
\boxed{
R^{\ast}_{FB}.
}
$$

若：

$$
(\varnothing,\varnothing,\varnothing)
\in
R^{\ast}_{FB},
$$

才判 HHP-equivalent。

---

# 11. Regression 結果

有限 event structures 的 configuration 數：

$$
|Conf(A)|=14,
$$

$$
|Conf(B)|=11.
$$

Plain HP：

$$
\boxed{
(\varnothing,\varnothing,\varnothing)
\in
R_{HP}^{\ast}.
}
$$

所以：

$$
\boxed{
HP=true.
}
$$

---

# 12. Explicit Backward HHP 結果

Explicit backward fixed point：

$$
\boxed{
(\varnothing,\varnothing,\varnothing)
\notin
R_{FB}^{\ast}.
}
$$

實驗結果甚至得到：

$$
\boxed{
|R_{FB}^{\ast}|=0.
}
$$

因此：

$$
\boxed{
HHP=false.
}
$$

---

# 13. Regression Assertion

最重要結果：

$$
\boxed{
HP=true
\land
HHP=false.
}
$$

即：

$$
\boxed{
ExpectedRegression=true.
}
$$

我們終於得到一個真正能防止 checker 把 HP/HHP 寫成同一件事的標準 fixture。

---

# 14. 與 Downward-Closure 實作 Cross-Check

另一個 HHP checker 不直接跑 backward game，

而要求：

$$
(C_1,f,C_2)\in R
$$

時，

所有 matched legal subconfigurations：

$$
(D_1,f|_{D_1},D_2)
$$

也必須在：

$$
R.
$$

本 benchmark 上：

$$
\boxed{
R_{FB}^{\ast}
=
R_{Down}^{\ast}.
}
$$

Checker：

$$
\boxed{
same\_relation=true.
}
$$

---

# 15. 這個 Cross-Check 的意義

它不是一般 theorem proof。

但至少顯示：

- explicit backward implementation；
- hereditary downward-closure implementation；

在這個 finite regression 上沒有產生互相矛盾的結果。

未來任何一邊改 code，只要 regression 破掉就能立即發現。

---

# 16. 對 ON-RDSS BQCert 的直接影響

以前：

$$
BQCert
$$

可能只寫：

$$
HHP=true.
$$

現在更合理要帶：

$$
\boxed{
BQCert
=
(
Mode,
RelationHash,
HistoryMaps,
ForwardWitness,
BackwardWitness,
ProfileRegime,
Version,
CheckerVersion
).
}
$$

其中：

$$
Mode\in\{HP,HHP\}.
$$

---

# 17. HP Mode 與 HHP Mode 不能混

對低風險 coarse planning：

$$
Mode=HP
$$

可能足夠。

但如果 parent state 會影響：

- irreversible governance；
- rollback；
- history audit；
- authority；
- causal explanation；

則更保守應使用：

$$
\boxed{
Mode=HHP.
}
$$

---

# 18. 新的 State-Merge Safety Spectrum

可以定義：

$$
\boxed{
MergeStrength
=
Obs
<
Future
<
HP
<
HHP
<
HHP+Governance.
}
$$

最後一個還要求：

- authority；
- residual；
- version；
- certificate scope。

所以 parent-state equivalence不是單一布林標準。

---

# 19. General CEES 的 Explicit Backward Move

v0.12 已經指出：

$$
\widehat C
=
(C,\pi,\le_\pi,v).
$$

因此 general CEES backward move 不應只寫：

$$
C\setminus\{e\}.
$$

而是：

$$
\boxed{
\widehat C
\xleftarrow{\widetilde e}
\widehat C'
}
$$

其中：

$$
\widetilde e=(e,\kappa,v).
$$

---

# 20. 可回退 Occurrence

只有：

$$
e
$$

在 concrete history：

$$
(C,\le_\pi)
$$

中是 maximal，

才能直接撤回：

$$
\boxed{
\nexists e',
\quad
e\prec_\pi e'.
}
$$

刪除時同時移除：

- event occurrence；
- enabling witness $\kappa$ ；
- realization identity；
- incident induced causal edges。

---

# 21. General Backward Mapping

若：

$$
f:
\widehat C_1
\cong
\widehat C_2,
$$

回退：

$$
\widetilde e_1
$$

時，

另一邊必須回退：

$$
\boxed{
f(\widetilde e_1)
}
$$

對應的 causal realization，

而不是只找任何同名 surface event。

這比 prime HHP 更嚴。

---

# 22. Surface Mapping vs Realization Mapping

因此 general CEES 有兩種 map：

## Surface map

$$
f_s:e_1\mapsto e_2.
$$

## Realization map

$$
\boxed{
f_r:
(e_1,\kappa_1,v_1)
\mapsto
(e_2,\kappa_2,v_2).
}
$$

HHP-grade BQCert 應主要保存：

$$
f_r.
$$

---

# 23. Why Surface HHP Is Not Enough

可能：

$$
q(\widetilde e_1)=q(\widetilde e_2)=e,
$$

但：

$$
Cause(\widetilde e_1)\neq Cause(\widetilde e_2).
$$

若 backward capabilities / future branching 因 cause 不同，

surface event mapping 會丟資訊。

所以：

$$
\boxed{
SurfaceHHP
\not\Rightarrow
CauseSensitiveHHP.
}
$$

---

# 24. Cause-Abstract HHP

若 domain 不在乎 cause difference，

可以定義：

$$
\boxed{
HHP/Q_{cause}
}
$$

但必須有：

$$
ForgetCauseCert.
$$

因此「忽略原因」仍是一個顯式 quotient policy。

---

# 25. Bounded Backtracking

經典 HP/HHP 研究也引入 bounded backtracking hierarchy。

這對 ON-RDSS 工程特別有用：

$$
\boxed{
HHP_k
}
$$

表示只檢查最多 $k$ 層 backtracking。

可形成：

$$
HP
=
HHP_0
\preceq
HHP_1
\preceq
HHP_2
\preceq
\cdots
\preceq
HHP.
$$

注意此處符號只表安全強度直覺；正式包含關係仍需依採用的定義校正。

---

# 26. 為什麼 HHP_k 很適合 Runtime？

Exact HHP 很昂貴。

所以 Runtime 可以：

1. Cheap profile filter；
2. HP；
3. HHP $_1$ ；
4. HHP $_k$ ；
5. full HHP / offline proof。

這形成可調 verification budget。

---

# 27. Verification Budget

定義：

$$
\boxed{
VB
=
(
Mode,
k,
Scope,
Timeout,
CertificateLevel
).
}
$$

例如普通 UI projection：

$$
VB=(HP,\text{local},low).
$$

而 schema merge：

$$
VB=(HHP,\text{full affected subgraph},high).
$$

---

# 28. 不可把 Verification Budget 當真理等級

較弱模式通過只表示：

$$
\boxed{
\text{Passed under the selected verification strength}.
}
$$

不能寫成：

> 已證明 full HHP-equivalent。

Certificate 必須記錄 Mode。

---

# 29. Regression Fixture 的正式地位

此經典 HP-not-HHP structure 應永久加入：

$$
\boxed{
ONRDSSFormalTestSuite.
}
$$

至少測：

1. HP = true；
2. explicit HHP = false；
3. downward HHP = false；
4. explicit / downward HHP 結果一致；
5. middle $a_3/b_3$ 至少存在兩種 HP match contexts。

---

# 30. Anti-Regression Principle

任何未來 optimization：

- quotient indexing；
- memoization；
- event ID normalization；
- profile compression；

都不得讓此 fixture 變成：

$$
HHP=true.
$$

否則表示 optimizer 偷偷把 history-mapping dependence 壓掉。

---

# 31. 對 State Identity 的再修正

現在 parent state identity 可以附：

$$
\boxed{
EquivalenceGrade.
}
$$

例如：

$$
StateID
=
(
QuotientClass,
Q,
Version,
Grade
).
$$

其中：

$$
Grade\in
\{
Obs,
Future,
HP,
HHP,
HHP+Gov
\}.
$$

---

# 32. 同一 State Value 可以有不同 Grade

$$
\boxed{
Value(S_1)=Value(S_2)
}
$$

不代表：

$$
Grade(S_1)=Grade(S_2).
$$

這讓 parent layer 可以知道：

> 這個合併只是 UI 等價，還是已通過 history-preserving verification？

---

# 33. Version + Grade

完整：

$$
\boxed{
QuotientIdentity
=
(
ClassID,
ScopeQ,
EventSemanticsVersion,
EquivalenceGrade,
CertID
).
}
$$

這開始接近真正可工程實作的 State Registry。

---

# 34. 下一步

下一階段有兩條直接路線。

## 路線 A — General CEES Explicit Backtracking

把：

$$
(C,f,C')
$$

升級成：

$$
(\widehat C,f_r,\widehat C').
$$

實作：

- witness-sensitive forward；
- maximal realization backward；
- cause-sensitive matching；
- ForgetCause quotient。

## 路線 B — Bounded HHP Runtime

實作：

$$
HHP_k.
$$

並測經典 regression 在何個最小 $k$ 被區分。

這會直接產生 runtime verification cost / strength curve。

---

# 35. 暫定結論

v0.13 得到一個很重要的正式里程碑：

$$
\boxed{
HP
\neq
HHP
}
$$

不再只是文獻上「我們知道它們不同」。

ON-RDSS 自己的有限 checker 已經具有一個可重複 regression：

$$
\boxed{
HP(A,B)=true,
}
$$

$$
\boxed{
HHP(A,B)=false.
}
$$

而且 HHP 的：

$$
\boxed{
explicit\ backward\ game
}
$$

與：

$$
\boxed{
hereditary\ downward\ closure
}
$$

在此模型中給出相同固定點。

因此 `BQCert` 現在可以真正區分：

> **只在 forward histories 上相似**

與：

> **連回退歷史後仍保持同一 causal correspondence。**

這正是 ON-RDSS 要安全地做 StateMerge / Container Folding 時不能再忽略的差異。
