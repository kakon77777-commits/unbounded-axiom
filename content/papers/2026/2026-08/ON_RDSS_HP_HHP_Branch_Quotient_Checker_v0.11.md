# Operator-Native RDSS：有限 hp/hhp-like Branch Quotient Checker
## Configuration Triples, History Isomorphism, Hereditary Closure, and Versioned Quotient Certificates

**版本：** v0.11 Working Proof/Checker Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS Branch Quotient Certificate 由 bounded-signature proxy 升級為有限 configuration-relation checker  
**前置：** ON-RDSS v0.9–v0.10

---

# 摘要

v0.10 的 Branch Quotient Safety 使用：

- current observation；
- history profile；
- bounded future signature；

作為有限 proxy。

本版進一步改用 event-structure concurrency theory 中更標準的 configuration-triple 形式：

$$
\boxed{
(C_1,f,C_2)
}
$$

其中：

$$
f:C_1\cong C_2
$$

必須保存：

- event profile；
- causal order；
- configuration history structure。

本文在 finite prime-event-structure 子域上實作：

1. hp-like greatest-fixed-point checker；
2. hhp-like checker，額外要求 relation 對 matched subconfigurations hereditary downward closed；
3. ON-RDSS profile equality，把 label 之外的 type / authority / residual 一起納入 matching。

本版不宣稱已得到 general CEES / general event structure 的完整 hp/hhp solver。

---

# 1. 為什麼從 Signature Proxy 升級？

v0.10 toy criterion：

$$
CurrentSig(C_1)=CurrentSig(C_2),
$$

$$
HistorySig(C_1)=HistorySig(C_2),
$$

$$
FutureSig_k(C_1)=FutureSig_k(C_2)
$$

可以抓到很多反例，

但它仍可能：

- 因 bounded depth 漏掉遠期差異；
- 沒有明示保存歷史事件對應；
- 沒有真正以 configuration extension 做 back-and-forth；
- 無法表達 hereditary closure。

所以：

$$
\boxed{
SignatureSimilarity
\neq
HistoryPreservingBisimulation.
}
$$

---

# 2. 有限 Prime Event Structure 子域

本 checker 暫時使用：

$$
\boxed{
P
=
(E,\le,\#,\Lambda).
}
$$

其中：

- $E$：有限事件；
- $\le$：causal partial order；
- $\#$：conflict；
- $\Lambda$：ON-RDSS event profile。

Configuration：

$$
C\subseteq E
$$

需：

- conflict free；
- downward closed。

---

# 3. ON-RDSS Event Profile

傳統 hp/hhp matching 常首先要求 label-preserving。

本版將 label 擴充為 profile：

$$
\boxed{
\Lambda(e)
=
(
Label,
Type,
Authority,
Residual
).
}
$$

因此兩事件只有：

$$
\Lambda(e_1)=\Lambda(e_2)
$$

才可直接匹配。

這是 ON-RDSS-specific strengthening，不是 hp/hhp 的普遍定義。

---

# 4. History Isomorphism

給：

$$
C_1\in Conf(P_1),
\qquad
C_2\in Conf(P_2).
$$

映射：

$$
\boxed{
f:C_1\to C_2
}
$$

必須為 bijection，並滿足：

## Profile preservation

$$
\Lambda_1(e)
=
\Lambda_2(f(e)).
$$

## Causal-order preservation and reflection

$$
\boxed{
e\le_{C_1}e'
\iff
f(e)\le_{C_2}f(e').
}
$$

因此：

$$
(C_1,f,C_2)
$$

保存的是 configuration history 的 labeled poset structure。

---

# 5. Posetal Product State Space

定義候選 triple space：

$$
\boxed{
\mathcal T(P_1,P_2)
=
\{
(C_1,f,C_2)
\mid
f:C_1\cong C_2
\}.
}
$$

有限 checker 先枚舉所有合法 triples。

---

# 6. Event Extension

若：

$$
C\xrightarrow{e}C'
$$

表示：

$$
C'=C\cup\{e\}
$$

且 $C'$ 仍是 configuration。

對 triple：

$$
(C_1,f,C_2)
$$

若：

$$
C_1\xrightarrow{e_1}C_1',
$$

希望找到：

$$
C_2\xrightarrow{e_2}C_2'
$$

使：

$$
\Lambda_1(e_1)=\Lambda_2(e_2)
$$

並延伸：

$$
\boxed{
f'
=
f[e_1\mapsto e_2].
}
$$

要求：

$$
(C_1',f',C_2')
$$

仍在 relation。

反向亦然。

---

# 7. hp-like Greatest Fixed Point

令初始：

$$
R_0
=
\mathcal T(P_1,P_2).
$$

反覆刪除無法滿足 forward/back extension matching 的 triples：

$$
R_0
\supseteq
R_1
\supseteq
R_2
\supseteq\cdots
$$

直到固定：

$$
\boxed{
R_{hp}^{\ast}.
}
$$

若：

$$
(C_1,f,C_2)\in R_{hp}^{\ast},
$$

本 checker 稱它們 hp-related。

---

# 8. hhp-like Hereditary Closure

在 hp 條件外，再要求：

對：

$$
(C_1,f,C_2)\in R
$$

以及任意 matched subconfiguration：

$$
D_1\subseteq C_1,
$$

令：

$$
D_2=f(D_1),
$$

以及 restricted map：

$$
f|_{D_1}.
$$

只要 $D_1,D_2$ 都是 configurations，就要求：

$$
\boxed{
(D_1,f|_{D_1},D_2)\in R.
}
$$

因此 relation 對歷史刪除保持 hereditary closure。

---

# 9. hhp-like Greatest Fixed Point

同樣從全部 history-isomorphic triples 開始，

同時反覆施加：

- forward matching；
- backward matching；
- hereditary subconfiguration closure。

固定點：

$$
\boxed{
R_{hhp}^{\ast}.
}
$$

---

# 10. BQCert 的新核心

v0.10：

$$
BQCert
=
Observation
+
HistoryProxy
+
FutureProxy
+
Authority
+
Residual
+
Version.
$$

v0.11 改成：

$$
\boxed{
BQCert_{Q,v}^{hhp}
=
(
TripleRelation,
HistoryIso,
BackForthWitness,
HereditaryWitness,
ONProfileScope,
Version
).
}
$$

工程上仍可額外帶：

- authority review；
- residual review；
- scope；
- evidence refs。

---

# 11. Branch Quotient Rule

如果存在：

$$
f
$$

使：

$$
\boxed{
(C_1,f,C_2)
\in
R_{hhp}^{\ast}
}
$$

並且 ON-RDSS 的 version/scope certificate 成立，

才允許：

$$
\boxed{
[C_1]_{Q,v}
=
[C_2]_{Q,v}.
}
$$

---

# 12. hp 與 hhp 的角色差異

hp 要求：

> 當前歷史 correspondence 可被未來事件 forward/back 延伸。

hhp 再要求：

> 這個 correspondence 往回限制到可匹配的過去 configurations 時仍保持 relation。

因此 hhp 對：

$$
\boxed{
\text{history-preserving folding}
}
$$

更適合作為保守 reference。

這不表示 ON-RDSS 永遠必須用最強 hhp；

可依 domain 提供：

$$
\boxed{
QuotientMode
\in
\{
Obs,
Future,
HP,
HHP
\}.
}
$$

---

# 13. Quotient Mode

## Obs

只比較 current projection。

最便宜、最危險。

## Future

比較 bounded / symbolic future capability。

## HP

保留 configuration history isomorphism 與 forward/back extension。

## HHP

再加入 hereditary historical restriction。

治理關鍵 parent state 預設應偏向 HHP 或更強 ON-specific profile equivalence。

---

# 14. ON-specific Strengthening

即使兩事件普通 label 相同：

$$
label(e_1)=label(e_2),
$$

若：

$$
Auth(e_1)\neq Auth(e_2),
$$

則 ON profile 不同。

同理：

$$
Residual(e_1)\neq Residual(e_2)
$$

也阻止直接匹配。

所以：

$$
\boxed{
BehaviouralLabelEquality
}
$$

與：

$$
\boxed{
GovernedProfileEquality
}
$$

分離。

---

# 15. Experiment A — Symmetric Branches

結構：

$$
a\to r_a\to f_a,
$$

$$
b\to r_b\to f_b
$$

且兩條 branch profiles 對稱。

比較：

$$
C_A=\{a,r_a\},
$$

$$
C_B=\{b,r_b\}.
$$

Checker 找到 history map：

$$
\boxed{
f(a)=b,
\qquad
f(r_a)=r_b.
}
$$

結果：

$$
\boxed{
HP=true,
}
$$

$$
\boxed{
HHP=true.
}
$$

---

# 16. Experiment B — Same Present, Different Future Profile

保留：

$$
C_A,C_B
$$

當前 history profile 對稱，

但把：

$$
f_b
$$

改成不同：

- label；
- authority。

Checker：

$$
\boxed{
HP=false,
}
$$

$$
\boxed{
HHP=false.
}
$$

因為 branch A 的 future extension 找不到 profile-preserving match。

---

# 17. Experiment C — Meta Breaks Equivalence

v1：

$$
C_A
\sim
C_B.
$$

v2 只對 branch A 新增：

$$
r_a\to x_a
$$

且：

$$
Auth(x_a)=special.
$$

結果：

$$
\boxed{
HP_{v2}(C_A,C_B)=false,
}
$$

$$
\boxed{
HHP_{v2}(C_A,C_B)=false.
}
$$

這再次驗證：

$$
\boxed{
BQCert^v
}
$$

必須版本化。

---

# 18. Experiment D — Structure Renaming

兩個 event structures：

$$
x\to y
$$

與：

$$
u\to v
$$

profiles 分別對應：

$$
x\leftrightarrow u,
$$

$$
y\leftrightarrow v.
$$

Checker 從空 configurations 找到：

$$
\boxed{
HP=true,
\qquad
HHP=true.
}
$$

表示 event identifier 不必相同，只要 history structure / profile 可對應。

---

# 19. Checker 實作方式

有限演算法：

1. 枚舉 configurations；
2. 對等 cardinality configurations 枚舉 bijections；
3. 保留 profile + causal-poset isomorphisms；
4. 得到所有 triple candidates；
5. greatest-fixed-point elimination 求 hp；
6. 再加入 hereditary subconfiguration elimination 求 hhp。

因此是 exponential / combinatorial toy checker，不是大型 Runtime 解法。

---

# 20. 複雜度警告

Configuration 數量本身可能指數成長，

配置間 bijection 還有 factorial factor。

所以：

$$
\boxed{
\text{exact HHP checking}
}
$$

不適合作為所有大型 RDSS parent-state comparison 的即時計算。

工程上需要：

- bounded scope；
- local quotient candidates；
- signatures / invariants 預篩；
- incremental certificates；
- cached fold registry。

---

# 21. Two-Tier Quotient Checking

建議：

## Tier 1 — Cheap Candidate Filter

使用：

- current profile；
- boundary contract；
- bounded future signature；
- authority/residual hash。

只有通過才進 Tier 2。

## Tier 2 — Exact / Strong Checker

對小型局部 event substructure 執行 hp/hhp-like checker。

所以：

$$
\boxed{
FastIndex
\neq
StrongQuotientAuthority.
}
$$

---

# 22. BQCert 作為可重建 Authority

真正 parent-state merge authority：

$$
\boxed{
BQCert
}
$$

可包含：

- candidate pair；
- event semantics version；
- hp/hhp mode；
- relation triples；
- history maps；
- proof/checker version；
- scope；
- profile equality regime。

快速：

$$
QuotientIndex
$$

可以由它生成。

---

# 23. Meta Revalidation

若：

$$
\mathfrak E_v
\to
\mathfrak E_{v+1},
$$

所有受影響：

$$
BQCert^v
$$

標記：

$$
\boxed{
Stale.
}
$$

重新 checker：

$$
Recheck_{v+1}(C_1,C_2).
$$

若失敗：

$$
\boxed{
SplitRequired.
}
$$

---

# 24. State Merge / Split 現在有更正式的依據

State merge：

$$
\boxed{
C_1
\stackrel{HHP/ON}{\sim}
C_2
\Rightarrow
MergeCandidate.
}
$$

State split：

$$
\boxed{
BQCert^v
\text{ valid}
\land
BQCert^{v+1}
\text{ invalid}
\Rightarrow
SplitRequired.
}
$$

---

# 25. Folding Map Verification

事件 folding：

$$
F:E\to\widehat E
$$

可以轉化成：

> folding 前後 event structures 是否由 hp/hhp-like relation 連接？

因此 bounded checker 可成為 fold regression tool。

但完整 event-structure minimisation 仍應優先利用既有 folding 理論，而不是 ON-RDSS 自行重建全部 minimisation mathematics。

---

# 26. hhp 與 General CEES 的缺口

本 checker 是 finite PES。

v0.9 General CEES：

$$
(E,Con,\vdash,\ldots)
$$

允許：

- disjunctive enabling；
- general consistency；
- dynamic causality。

其 history poset 不一定像 prime event structure 一樣由一個固定全域 causal order直接取得。

因此要做 general CEES 的 hhp，需要先明確定義：

$$
\boxed{
HistoryOrder(C,\pi)
}
$$

或 configuration-specific causal witness。

---

# 27. General CEES 下一版候選

一個 configuration 可能需要攜帶 proving sequence / enabling witness：

$$
\boxed{
\widehat C
=
(
C,
\pi,
\le_\pi
).
}
$$

然後 hp/hhp 比較的不是裸：

$$
C
$$

而是：

$$
\widehat C.
$$

這才能處理同一 event set 具有不同 causal history 的系統。

---

# 28. Causal Ambiguity

若同一 configuration：

$$
C
$$

可由不同 enabling choices 得到不同 causal explanations，

則：

$$
\boxed{
SetOfEvents
}
$$

本身不足以代表 history。

ON-RDSS 必須保留：

$$
\boxed{
Configuration
+
EnablingWitness.
}
$$

這和 v0.9 disjunctive causation 的問題直接相連。

---

# 29. 對 Parent State 定義的再精化

v0.10：

$$
State
=
VersionedHistoryPreservingQuotient(Configuration).
$$

v0.11 更精確：

$$
\boxed{
State_{parent}^{Q,v}
=
Quotient(
\text{History-Decorated Configurations}
\mid
BQCert_{Q,v}
).
}
$$

在 prime 子域，history decoration 可由 causal configuration poset 隱式給出。

在 general CEES，可能需要 explicit enabling witness。

---

# 30. 第一個正式 BQCert Verification Rule

Prime finite 子域暫定：

$$
\frac{
(C_1,f,C_2)\in R_{hhp}^{\ast}
\qquad
Version(C_1)=Version(C_2)=v
\qquad
Scope(f)\subseteq Q
}{
\boxed{
BQCert_{Q,v}(C_1,C_2)\downarrow
}
}
$$

實際 ON-RDSS 還要加入：

- certificate checker version；
- authority regime；
- residual policy。

---

# 31. No Silent Merge

即使 checker 找到：

$$
HHP(C_1,C_2),
$$

也不代表 Runtime 必須自動 merge。

應區分：

$$
\boxed{
MergeSafe
}
$$

與：

$$
\boxed{
MergeAuthorized.
}
$$

前者是形式判定，

後者是治理決策。

---

# 32. No Silent Split

同樣：

$$
BQCert
$$

失效表示：

$$
SplitRequired.
$$

不表示 Runtime 必須立即破壞所有 live references。

還需要：

- migration；
- aliases；
- versioned routing；
- graceful split。

---

# 33. hp/hhp Checker 與 Certificate

Checker 結果不是數學證明助理證書。

第一代只能產生：

$$
\boxed{
FiniteModelCheckCertificate.
}
$$

其中包括：

- model hash；
- relation size；
- matching maps；
- checker version；
- exact finite scope。

未來若 Lean / Coq formalize，再提升證書級別。

---

# 34. 有限結果

本版實測：

## Symmetric branch

$$
HP=true,
\qquad
HHP=true.
$$

## Different future / authority

$$
HP=false,
\qquad
HHP=false.
$$

## Meta-added one-sided future

$$
HP=false,
\qquad
HHP=false.
$$

## Isomorphic renamed structures

$$
HP=true,
\qquad
HHP=true.
$$

---

# 35. 本輪沒有找到 hp / hhp 分離案例

本輪幾個有限模型中：

$$
R_{hp}^{\ast}
=
R_{hhp}^{\ast}
$$

在測試案例上恰好相同。

這不代表兩種 equivalence 一般相同。

它只表示目前 toy cases 沒有命中需要 hereditary condition 才能區分的結構。

後續應特別構造或搜尋：

$$
\boxed{
HP=true,
\qquad
HHP=false
}
$$

的最小反例，作為 checker regression。

---

# 36. 下一步

1. 找 hp / hhp 最小分離模型；
2. 把 checker 從 PES 推到 stable / general configuration structures；
3. 加入 proving-sequence / enabling witness；
4. 定義 hp/hhp over dynamic-version snapshots；
5. 加入 fold-map validator；
6. BQCert 生成完整 witness package；
7. 接 StateSplit / StateMerge Runtime；
8. 對大型模型加入 quotient candidate index；
9. 研究 exact checker 的 complexity boundary；
10. Lean formalize prime finite core。

---

# 37. 暫定結論

ON-RDSS 的 Branch Quotient 已經從：

$$
\boxed{
\text{看起來一樣}
}
$$

逐步推進到：

$$
\boxed{
\text{bounded future/profile same}
}
$$

再推進到：

$$
\boxed{
\text{configuration-history isomorphism}
+
\text{forward/back matching}
+
\text{hereditary closure}.
}
$$

因此 parent state 越來越不應被理解成「同值」。

更合理的是：

$$
\boxed{
State_{parent}
=
\text{Governed Quotient Class under a Versioned History-Preserving Behavioural Relation}.
}
$$

而 ON-RDSS 在既有 hp/hhp/folding 理論上真正新增的責任是：

$$
\boxed{
Authority
+
Residual
+
Certificate
+
Version
+
MetaRevalidation.
}
$$
