# Operator-Native RDSS：Type-and-Effect Safety 第一代證明骨架
## Structural Preservation, Effect Accounting, and Explicit Residual Progress

**版本：** v0.7 Working Proof Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS Type-and-Effect Calculus 的第一代定理—引理—證明骨架  
**前置：** ON-RDSS v0.3–v0.6

---

# 摘要

本文首次把 ON-RDSS 的 Type-and-Effect Calculus 從「候選規則」推進到「可逐 rule 證明的 proof skeleton」。

核心型別 judgment：

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
d
}
$$

其中：

- $\vec\sigma$：輸入 sorts；
- $\tau$：輸出 sort；
- $\chi\in\mathcal E^\ast$：有順序 effect trace；
- $d$：meta-depth。

本文區分：

$$
\boxed{
W\Rightarrow_s W'
}
$$

的 structural reduction，與：

$$
\boxed{
\langle W,\rho,H,\mathfrak A\rangle
\xrightarrow{\eta,c}
\langle W',\rho',H',\mathfrak A'\rangle
}
$$

的 runtime execution。

由此提出三條核心 theorem candidates：

1. **Typed Structural Preservation**；
2. **Effect Accounting**；
3. **Explicit Residual Progress**。

本版並指出：Bridge insertion 不應被當成「零效果 structural rewrite」；它屬於 typed elaboration / residual resolution，必須顯式增加 bridge effect 與 certificate。Meta rewrite 也不能混入固定 Algebra Snapshot 下的 structural reduction。

---

# 1. 基礎資料

## 1.1 Sorts

$$
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
$$

## 1.2 Effects

$$
e\in\mathcal E.
$$

Effect trace：

$$
\boxed{
\chi
=
[e_1,\ldots,e_n]
\in
\mathcal E^\ast.
}
$$

## 1.3 Certified independence

定義：

$$
I_\Gamma
\subseteq
\mathcal E\times\mathcal E.
$$

只有：

$$
(e_a,e_b)\in I_\Gamma
$$

且存在：

$$
CommCert_\Gamma(e_a,e_b)
$$

時，才允許相鄰交換。

---

# 2. Effect Trace Congruence

定義最小 congruence：

$$
\boxed{
\equiv_\Gamma
}
$$

由以下規則生成：

$$
\chi_1\cdot[e_a,e_b]\cdot\chi_2
\equiv_\Gamma
\chi_1\cdot[e_b,e_a]\cdot\chi_2
$$

當且僅當：

$$
(e_a,e_b)\in I_\Gamma
$$

且有 commutation certificate。

再對 reflexive / symmetric / transitive closure 與 concatenation context 閉包。

因此：

$$
\boxed{
\chi_1=\chi_2
\Rightarrow
\chi_1\equiv_\Gamma\chi_2,
}
$$

但反向不必成立。

---

# 3. Operator Interface

定義：

$$
\boxed{
Iface(O)
=
(
In(O),
Out(O),
Depth(O)
).
}
$$

定義完整 typing interface：

$$
\boxed{
TI(O)
=
(
In(O),
Out(O),
Effect(O),
Depth(O)
).
}
$$

---

# 4. Operator Word Typing

對 sequential word：

$$
W=[O_1,\ldots,O_n],
$$

定義：

$$
\Gamma\vdash W:
\vec\sigma\Rightarrow\tau!\chi@d
$$

當：

1. $O_1$ 接受外部輸入 $\vec\sigma$ ；
2. 對每個相鄰 pair：
   $$
   Out(O_i)=In(O_{i+1})
   $$
   或已有明示 typed bridge；
3. 最終：
   $$
   Out(O_n)=\tau;
   $$
4. effect：
   $$
   \chi
   =
   Effect(O_1)\cdots Effect(O_n);
   $$
5. depth：
   $$
   d
   =
   \max_i Depth(O_i).
   $$

---

# 5. Typed Residual

若在位置 $i$：

$$
Out(O_i)=\tau
$$

而：

$$
In(O_{i+1})=\sigma,
$$

且：

$$
\tau\not\sim_\Gamma\sigma
$$

並不存在已授權 bridge，則：

$$
\boxed{
\Gamma
\vdash
W
\rightsquigarrow
Residual[
TypeMismatch(
i,\tau,\sigma
)
].
}
$$

若存在 bridge type，但未提供 bridge：

$$
\boxed{
Residual[
BridgeRequired(
i,\tau\rightsquigarrow\sigma
)
].
}
$$

如果主要缺的是 certificate：

$$
\boxed{
Residual[
CertificateRequired(
i,rule,scope
)
].
}
$$

---

# 6. Structural Reduction Rules

本版 structural reduction 僅允許「不真正執行外部 effect」的 rewrite。

## 6.1 S-Fold

若：

$$
\Gamma
\vdash
U:
\vec\sigma
\Rightarrow
\tau
!
\chi
@
d,
$$

並註冊 macro：

$$
M_U
$$

且：

$$
TI(M_U)
=
(
\vec\sigma,\tau,\chi,d
),
$$

則：

$$
\boxed{
C[U]
\Rightarrow_s
C[M_U].
}
$$

---

## 6.2 S-Unfold

若 macro 保存原 definition version：

$$
Def(M_U)=U,
$$

則允許：

$$
\boxed{
C[M_U]
\Rightarrow_s
C[U].
}
$$

這是一個 debugging / expansion rule，不表示 runtime 必須實際展開。

---

## 6.3 S-Comm

若：

$$
\Gamma
\vdash
O_a:
\sigma\Rightarrow\sigma!\chi_a@d_a
$$

與：

$$
\Gamma
\vdash
O_b:
\sigma\Rightarrow\sigma!\chi_b@d_b,
$$

並且：

$$
CommCert_\Gamma(O_a,O_b)\downarrow,
$$

要求：

$$
Effect(O_a)\cdot Effect(O_b)
\equiv_\Gamma
Effect(O_b)\cdot Effect(O_a),
$$

以及 side effect / authority / history critical pair 可 join。

則：

$$
\boxed{
C[O_a,O_b]
\Rightarrow_s
C[O_b,O_a].
}
$$

---

# 7. 不屬於 Structural Reduction 的兩類規則

## 7.1 Bridge insertion

若：

$$
O_1:A\to B,
\qquad
O_2:C\to D
$$

而：

$$
B\not\sim C,
$$

新增：

$$
B_{BC}:B\rightharpoonup C
$$

會增加：

- bridge effect；
- loss obligation；
- certificate；
- provenance。

所以：

$$
\boxed{
\text{Bridge insertion}
\neq
\text{effect-neutral structural reduction}.
}
$$

應獨立寫成：

$$
\boxed{
W
\xRightarrow{\mathrm{elab}}
W'
}
$$

的 typed elaboration / residual resolution。

---

## 7.2 Meta rewrite

若：

$$
M:\mathfrak A_t\rightharpoonup\mathfrak A_{t+1},
$$

則：

$$
\boxed{
\mathfrak A_t
\neq
\mathfrak A_{t+1}
}
$$

可能成立。

所以 Meta rewrite 不能出現在固定 Algebra Snapshot 的 structural-preservation theorem 中。

---

# 8. Lemma 1 — Signature Composition

**引理 L1**

若：

$$
\Gamma\vdash
O_1:
\vec\sigma\Rightarrow\tau!\chi_1@d_1
$$

與：

$$
\Gamma\vdash
O_2:
\tau\Rightarrow\upsilon!\chi_2@d_2,
$$

且 composition certificate 成立，則：

$$
\boxed{
\Gamma\vdash
O_2\diamond O_1:
\vec\sigma
\Rightarrow
\upsilon
!
(\chi_1\cdot\chi_2)
@
\max(d_1,d_2).
}
$$

### 證明骨架

由 sequential typing rule：

1. $O_1$ 接受 $\vec\sigma$ ；
2. $O_1$ 輸出 $\tau$ ；
3. $O_2$ 恰接受 $\tau$ ；
4. 所以外部輸入仍是 $\vec\sigma$ ；
5. 最終輸出為 $\upsilon$ ；
6. effect 依執行順序串接；
7. meta-depth 取最大值。

證畢。

---

# 9. Lemma 2 — Effect Congruence Is Context-Closed

**引理 L2**

若：

$$
\chi_a\equiv_\Gamma\chi_b,
$$

則對任意 effect contexts：

$$
\chi_L,\chi_R,
$$

有：

$$
\boxed{
\chi_L\cdot\chi_a\cdot\chi_R
\equiv_\Gamma
\chi_L\cdot\chi_b\cdot\chi_R.
}
$$

### 證明骨架

 $\equiv_\Gamma$ 被定義為由 certified adjacent swaps 生成、並對 concatenation context 閉包的最小 congruence。

故直接由定義成立。

---

# 10. Lemma 3 — Macro Interface Preservation

**引理 L3**

若 macro $M_U$ 按 definition 建立為：

$$
TI(M_U)=TI(U),
$$

則：

$$
\boxed{
TI(C[M_U])
\equiv_\Gamma
TI(C[U]).
}
$$

### 證明骨架

對 context $C$ 的 sequential composition 結構歸納。

Base：

$$
C=[\;].
$$

由 macro 定義直接成立。

Induction：

對左／右追加的 well-typed operator，使用 L1 保持外部 input/output/depth，使用 L2 保持 effect congruence。

---

# 11. Lemma 4 — Certified Commutation Preservation

**引理 L4**

若：

$$
C[O_a,O_b]
\Rightarrow_s
C[O_b,O_a]
$$

由 S-Comm 產生，

則：

$$
\boxed{
Iface(C[O_a,O_b])
=
Iface(C[O_b,O_a])
}
$$

且：

$$
\boxed{
Effect(C[O_a,O_b])
\equiv_\Gamma
Effect(C[O_b,O_a]).
}
$$

### 證明骨架

S-Comm 的 side conditions 已要求：

$$
O_a,O_b:
\sigma\Rightarrow\sigma
$$

所以交換不改變 context 所看見的 intermediate sort。

effect 則由：

$$
CommCert_\Gamma(O_a,O_b)
$$

與 L2 得到 context-closed equivalence。

authority/history 等額外義務由 critical-pair join certificate 提供。

---

# 12. Lemma 5 — Residual Typing Completeness for Local Mismatch

**引理 L5**

對有限 sequential word $W$，若第一個無法型別接續的位置為 $i$，且 type compatibility / bridge registry / certifier 均可判定，則演算法能輸出唯一的第一個 local residual obligation：

$$
\boxed{
Residual[\omega_i].
}
$$

### 證明骨架

有限 word 可從左至右檢查。

在位置 $i$：

1. 若 exact type match，繼續；
2. 若有已授權 bridge，進入 elaborated word；
3. 若 bridge type 存在但缺 instance，輸出 BridgeRequired；
4. 若無合法 bridge，輸出 TypeMismatch；
5. 若只缺 certificate，輸出 CertificateRequired。

由第一失敗位置定義，local diagnostic 唯一。

注意：這是算法層 local completeness，不等於所有未來修復方案唯一。

---

# 13. Theorem 1 — Typed Structural Preservation

**定理 T1**

固定：

$$
\Gamma,
\mathfrak A
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

則存在 $\chi'$ 使：

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
\chi'\equiv_\Gamma\chi.
}
$$

---

# 14. T1 證明骨架

對：

$$
W\Rightarrow_sW'
$$

的 derivation 最後一條規則分情況。

## Case S-Fold

由 L3。

## Case S-Unfold

由 macro definition equality 及 L3 反向。

## Case S-Comm

由 L4。

## Case Context Closure

若：

$$
U\Rightarrow_sU'
$$

而：

$$
W=C[U],
\qquad
W'=C[U'],
$$

由歸納假設：

$$
TI(U)\equiv_\Gamma TI(U'),
$$

再由 L1 / L2 得：

$$
TI(C[U])\equiv_\Gamma TI(C[U']).
$$

各 case 成立，故 T1 成立。

---

# 15. T1 尚未覆蓋什麼？

目前不包括：

- wiring graph parallel reduction；
- bridge elaboration；
- runtime effect execution；
- meta rewrite；
- dynamic algebra-version switch；
- probabilistic effect；
- infinite operator words。

所以這是：

$$
\boxed{
\text{finite sequential structural subsystem}
}
$$

上的 proof skeleton。

---

# 16. Execution Configuration

定義：

$$
\boxed{
\mathcal K
=
\langle
W,
\rho,
H,
\mathfrak A,
v
\rangle
}
$$

其中：

- $W$：operator word / current macro；
- $\rho$：runtime state/environment；
- $H$：history；
- $\mathfrak A$：Operator Algebra Snapshot；
- $v$：authority/version context。

---

# 17. Execution Step

$$
\boxed{
\langle
W,\rho,H,\mathfrak A,v
\rangle
\xrightarrow{\eta,c}
\langle
W',\rho',H',\mathfrak A',v'
\rangle.
}
$$

 $\eta$ 是本步已實現 effect trace。

 $c$ 是 execution certificate。

---

# 18. Lemma 6 — Prefix Accounting

在純 sequential execution semantics 中，若：

$$
\chi
=
\eta\cdot\chi_{rem},
$$

則：

$$
\boxed{
\chi
\equiv_\Gamma
\eta\cdot\chi_{rem}.
}
$$

若允許 certified commuting effects，可先在 $\equiv_\Gamma$ 下找到一個代表：

$$
\chi'
=
\eta\cdot\chi_{rem}.
$$

因此：

$$
\boxed{
\chi
\equiv_\Gamma
\eta\cdot\chi_{rem}.
}
$$

---

# 19. Theorem 2 — Effect Accounting

**定理 T2**

若：

$$
\Gamma
\vdash
W:
\vec\sigma\Rightarrow\tau!\chi@d
$$

且 execution：

$$
\mathcal K
\xrightarrow{\eta,c}
\mathcal K',
$$

在非 Meta step 中要求存在：

$$
\chi_{rem}
$$

使：

$$
\boxed{
\chi
\equiv_\Gamma
\eta\cdot\chi_{rem}.
}
$$

同時：

$$
\boxed{
H'
=
H
\oplus
Trace(\eta,c,\mathfrak A,v).
}
$$

且：

$$
\boxed{
\mathfrak A'=\mathfrak A,
\qquad
v'=v
}
$$

除非 effect 明示包含合法 authority transition。

---

# 20. T2 證明骨架

對 execution derivation 長度歸納。

## Base

零步：

$$
\eta=[]
$$

且：

$$
\chi_{rem}=\chi.
$$

成立。

## Step

假設：

$$
\chi
\equiv
\eta_1\cdot\chi_1
$$

而下一步消耗：

$$
\eta_2
$$

使：

$$
\chi_1
\equiv
\eta_2\cdot\chi_2.
$$

由 effect congruence 與 concatenation：

$$
\chi
\equiv
\eta_1\cdot\eta_2\cdot\chi_2.
$$

history 由 append associativity：

$$
H''
=
H\oplus Trace(\eta_1)\oplus Trace(\eta_2).
$$

因此成立。

---

# 21. Meta Execution Rule

若：

$$
meta\in Summary(\eta),
$$

則允許：

$$
\mathfrak A'\neq\mathfrak A
$$

但必須：

$$
\boxed{
MetaCert(
\mathfrak A,
\mathfrak A',
c
)\downarrow.
}
$$

並保存：

$$
\boxed{
ParentAlgebraVersion(\mathfrak A')
=
Id(\mathfrak A).
}
$$

Replay trace 必須記兩個版本。

---

# 22. Meta-Version Isolation Lemma

**引理 L7**

若 execution effect 不含 `meta`，且不含具有 algebra-write authority 的 effect，則：

$$
\boxed{
\mathfrak A'=\mathfrak A.
}
$$

這不是從純型別自動推出，而是 ON-RDSS execution semantics 的治理公理。

---

# 23. Explicit Residual Progress 前提

我們不能無條件對任意開放世界宣稱 progress。

暫時限制：

1. $W$ 有限；
2. Algebra Snapshot 固定；
3. type compatibility 可判定；
4. bridge registry 查詢可終止；
5. certificate precheck 可終止；
6. structural rule matching 可終止。

在這些條件下建立算法性 progress。

---

# 24. Theorem 3 — Explicit Residual Progress

**定理 T3**

對符合上述有限性／可判定條件的 well-formed operator word $W$，恰有以下至少一類結果可被算法識別：

$$
\boxed{
Normal
\lor
StructuralStep
\lor
ExecutionReady
\lor
TypedResidual.
}
$$

---

# 25. T3 證明骨架

由有限 decision procedure：

1. 檢查 $W$ 是否已為 executable normal form；
2. 否則搜尋 finite structural rules；
3. 若有合法 structural match，回傳 StructuralStep；
4. 否則檢查 head executable operator / runtime gate；
5. 若 executable，回傳 ExecutionReady；
6. 否則由 L5 產生第一個 typed residual。

因所有檢查在前提下終止，所以算法必定返回上述其中之一。

注意這是「顯式診斷 progress」，不是傳統 lambda-calculus progress 的原樣複製。

---

# 26. Residual Preservation

若：

$$
W
\rightsquigarrow
Residual[\omega],
$$

則 residual 本身有 sort：

$$
\boxed{
\Gamma
\vdash
Residual[\omega]
:
Residual[\omega].
}
$$

它不是普通 $\tau$ 值。

因此不能把 residual 當成成功 output。

---

# 27. Bridge Resolution Rule

若：

$$
Residual[
BridgeRequired(
i,\tau\rightsquigarrow\sigma
)
]
$$

且之後加入合法：

$$
B:\tau\rightharpoonup\sigma
$$

與：

$$
BridgeCert(B),
$$

則：

$$
\boxed{
ResolveBridge:
Residual[\omega]
\rightsquigarrow
W[B/i].
}
$$

新 word 必須重新 type-check，並新增 bridge effect / loss obligation。

---

# 28. Certificate Resolution Rule

類似：

$$
Residual[
CertificateRequired(r)
]
$$

取得：

$$
c_r
$$

後：

$$
\boxed{
ResolveCert:
Residual[\omega]
\rightsquigarrow
W'
}
$$

但 certificate 不得自行擴大 authority scope。

---

# 29. Preservation 不推出 Confluence

即使：

$$
W\Rightarrow_s^\ast N_1
$$

及：

$$
W\Rightarrow_s^\ast N_2
$$

都由 T1 得到同一外部型別，

仍可能：

$$
Effect(N_1)
\not\equiv_\Gamma
Effect(N_2),
$$

或：

$$
HistoryObligation(N_1)
\neq
HistoryObligation(N_2).
$$

因此：

$$
\boxed{
Preservation
\not\Rightarrow
Confluence.
}
$$

Critical Pair Calculus 仍是獨立必要層。

---

# 30. Confluence 不推出治理等價

甚至：

$$
N_1\simeq_{obs}N_2
$$

也可能：

$$
AuthorityEffect(N_1)
\neq
AuthorityEffect(N_2).
$$

所以 ON-RDSS 需要多層等價：

$$
\boxed{
\simeq_{type},
\simeq_{effect},
\simeq_{obs},
\simeq_{history},
\simeq_{authority}.
}
$$

---

# 31. Type-and-Effect Safety 第一代定義

暫定：

$$
\boxed{
Safety_{ON}
=
T1
+
T2
+
T3
+
CertificateSoundness
+
MetaVersionSafety.
}
$$

其中：

- T1：Structural Preservation；
- T2：Effect Accounting；
- T3：Explicit Residual Progress。

---

# 32. 有限模型驗證

本輪建立有限 checker：

alphabet：

$$
\{
R,T,P,V,Q,Q2
\}.
$$

最大 word length：

$$
4.
$$

窮舉得到：

$$
324
$$

個 well-typed words，

以及：

$$
1230
$$

個 explicit residual words。

---

# 33. Structural Reduction 實測

總 structural reduction steps：

$$
354.
$$

包括：

- typed macro folding；
- certified independent read commutation。

結果：

$$
\boxed{
PreservationFailures=0.
}
$$

即在此有限模型中，所有被 checker 接受的 structural rewrite 都保持：

- external input sort；
- output sort；
- meta-depth；
- effect trace modulo certified commutation。

---

# 34. Residual Shape 實測

對 1230 個不能完整 type 的 finite words，

所有第一 local residual 都至少保存：

- actual；
- expected；
- location。

結果：

$$
\boxed{
ResidualShapeFailures=0.
}
$$

---

# 35. Effect Accounting 實測

測試多組 ordered effect traces 的所有 prefix consumption。

結果：

$$
\boxed{
\eta\cdot\chi_{rem}
=
\chi
}
$$

全部通過。

此實驗只驗證 sequential-prefix accounting，不涵蓋一般 concurrent partial orders。

---

# 36. 有限驗證的意義與限制

這些結果支持：

$$
\boxed{
\text{proof skeleton consistency}
}
$$

但不是一般性 theorem proof。

未驗證：

- 無限 words；
- arbitrary wiring graphs；
- dynamic bridge insertion；
- concurrent effects；
- Meta rewrite；
- dependent types；
- subtyping；
- effect polymorphism；
- certificate soundness 本身。

---

# 37. 與既有 Type-and-Effect Soundness 的關係

既有 type-and-effect meta-theory通常以 progress 與 subject reduction / preservation 作為 type-and-effect soundness 的核心組件，並研究不同 effect representation 滿足何種 safety conditions。

ON-RDSS 的差異是：

1. composition 本身可能 partial；
2. 不可執行狀態可以成為 typed residual；
3. effect 必須保留順序／部分交換資訊；
4. certificate 與 authority 是 effect/governance 義務；
5. Meta 可以版本化改寫 type/effect algebra 本身。

因此 ON-RDSS 應被視為對這些成熟方法的特化與擴展研究問題，而不是重新發明 type safety。

---

# 38. 下一個最關鍵的正式化缺口

T1 現在真正的缺口不是 sequential word。

而是：

$$
\boxed{
\text{Wiring Subject Reduction}.
}
$$

對：

$$
G_O
=
(
V,E,Ports,Types
)
$$

若某個 subgraph 被封裝成 macro operator，

是否：

- boundary port types 保持；
- causal partial order 保持；
- effect partial order 保持；
- authority boundary 保持；
- history witness 可重構？

這將是 ON-RDSS 從 word calculus 走向真正 recursive container / multi-agent runtime 的關鍵。

---

# 39. 另一個缺口：Effect 由 Word 升到 Partial Order

目前：

$$
\chi\in\mathcal E^\ast.
$$

適合 sequential runtime。

但真正並行 wiring 更合理：

$$
\boxed{
\mathcal ETrace
=
(E,\prec_c)
}
$$

即 effect events 與 causal partial order。

線性 word 只是其中一個 linearization。

這會讓：

$$
e_a\parallel e_b
$$

不必先強行決定順序。

---

# 40. 暫定結論

到本版，ON-RDSS 第一代 proof architecture 已經形成：

$$
\boxed{
\text{Typing}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Structural Preservation}
}
$$

$$
+
$$

$$
\boxed{
\text{Effect Accounting}
}
$$

$$
+
$$

$$
\boxed{
\text{Explicit Residual Progress}
}
$$

$$
+
$$

$$
\boxed{
\text{Critical-Pair / Confluence Analysis}
}
$$

$$
+
$$

$$
\boxed{
\text{Meta-Version Governance}.
}
$$

真正下一層應由 sequential words 推進到 typed wiring graphs，並將 ordered effect trace 推進成 causal effect partial order。

這將使原 RDSS 的：

$$
\text{recursive container}
+
\text{local time}
+
\text{parallel subsystem}
$$

第一次真正進入 ON-RDSS 的 type-safety theorem。
