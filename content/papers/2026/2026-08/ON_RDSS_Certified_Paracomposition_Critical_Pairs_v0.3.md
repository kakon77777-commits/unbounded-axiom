# Operator-Native RDSS：Certified Paracomposition、Critical Pairs 與 Normalization
## Working Draft v0.3

**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** 深層形式化工作文件／有限模型驗證  
**前置：** Operator-Native RDSS Primitive Algebra v0.1、Deep Formal Backbone v0.2

---

# 0. 本輪核心結果

本輪將 ON-RDSS 的核心從單純二元部分合成：

$$
\mathcal O_2\diamond\mathcal O_1
$$

進一步修正為：

$$
\boxed{
\text{typed operator words}
+
\text{certified partial reductions}
+
\text{critical-pair analysis}
+
\text{normal-form / residual semantics}.
}
$$

其理由是 ON-RDSS 同時具有兩層部分性：

$$
\boxed{
\text{Partial Action}
}
$$

與：

$$
\boxed{
\text{Partial Composition}.
}
$$

單一算子可能只對部分輸入定義；而兩個合法算子之間也可能因 Type、Bridge、Authority、History、Certificate 等條件而無法合成。

---

# 1. Certified Paracomposition

定義 typed operator word：

$$
\boxed{
W_\Gamma
=
[
\mathcal O_1,
\ldots,
\mathcal O_n
]_\Gamma.
}
$$

定義部分 $n$ 元合成：

$$
\boxed{
\left\langle
\mathcal O_n,\ldots,\mathcal O_1
\right\rangle_\Gamma
\rightharpoonup
\mathcal O_W.
}
$$

Binary $\diamond$ 只是：

$$
\mathcal O_2\diamond\mathcal O_1
:=
\langle
\mathcal O_2,\mathcal O_1
\rangle_\Gamma.
$$

因此 ON-RDSS 的核心不要求所有合法長鏈都必須由預先固定的 binary bracketing 建構。

---

# 2. Certified Reduction

定義：

$$
\boxed{
W
\Rightarrow_{\Gamma,c}
W'
}
$$

其中 $c$ 是本次 reduction 的 certificate。

每個合法 reduction 至少記錄：

$$
\boxed{
c
=
(
Rule,
Location,
TypeCheck,
BridgeRefs,
Authority,
Invariant,
HistoryEffect,
OutputSignature
).
}
$$

因此 reduction 不只是字串重寫，而是：

$$
\boxed{
\text{typed + governed + witnessed rewrite}.
}
$$

---

# 3. Residual Semantics

若某 operator word 無法完全收斂，不直接壓成：

$$
\mathcal O_\bot.
$$

而保留：

$$
\boxed{
NF_\Gamma(W)
=
[
R_1,\ldots,R_k
],
\qquad
k>1.
}
$$

每個不可約鄰接點附：

$$
\boxed{
Obligation(R_i,R_{i+1})
}
$$

例如：

$$
BridgeMissing,
TypeMismatch,
AuthorityMissing,
CertMissing,
HistoryConflict.
$$

所以：

$$
\boxed{
Failure
=
ResidualStructure
+
DiagnosticCertificate.
}
$$

只有已判定不可恢復的終端錯誤才壓成 bottom-like operator。

---

# 4. Normal Form

反覆 reduction：

$$
W
\Rightarrow^\ast
NF_\Gamma(W).
$$

若：

$$
|NF_\Gamma(W)|=1,
$$

稱 fully reducible，並得到封裝高階算子。

若：

$$
|NF_\Gamma(W)|>1,
$$

則：

$$
\boxed{
\text{composition remains open}.
}
$$

這與 RDSS 的 Limbo / BridgeRequired / Missing / Stale 可建立對應。

---

# 5. Critical Pair 六分類

本文件暫定六類核心 critical pair。

## CP-1 Bracketing Critical Pair

$$
(
O_3\diamond O_2
)\diamond O_1
$$

與：

$$
O_3\diamond(
O_2\diamond O_1
).
$$

問題：兩條 reduction path 是否都 defined 且同義？

---

## CP-2 Bridge Critical Pair

若：

$$
B_1,B_2:
X\rightharpoonup Y
$$

皆合法，則比較：

$$
O_2\diamond B_1\diamond O_1
$$

與：

$$
O_2\diamond B_2\diamond O_1.
$$

問題：Bridge choice 是否在指定觀測域可商掉？

---

## CP-3 Projection Critical Pair

比較：

$$
Project\diamond Transform
$$

與：

$$
\overline{Transform}\diamond Project.
$$

問題：先投影是否丟失後續作用所需資訊？

---

## CP-4 History Critical Pair

比較：

$$
O_B\diamond O_A
$$

與：

$$
O_A\diamond O_B.
$$

如果：

$$
H_{AB}\neq H_{BA},
$$

即使當前 observable state 相同，也不得任意交換。

---

## CP-5 Authority Critical Pair

兩個 reduction 都在形式上可執行，但所需 authority 不同。

問題：不同 reduction path 是否偷偷改變誰具有 commit / write 權限？

---

## CP-6 Meta Critical Pair

兩個 Meta-Operators：

$$
M_1,
M_2
$$

都要修改同一 operator algebra：

$$
\mathfrak A_t.
$$

比較：

$$
M_2(M_1(\mathfrak A))
$$

與：

$$
M_1(M_2(\mathfrak A)).
$$

若不等價，就形成真正的 schema-history branch。

---

# 6. Confluence

若：

$$
W\Rightarrow^\ast N_1,
$$

$$
W\Rightarrow^\ast N_2,
$$

且存在：

$$
N_1\Rightarrow^\ast N,
$$

$$
N_2\Rightarrow^\ast N,
$$

則在該 word 上 confluent。

若：

$$
N_1\not\simeq N_2
$$

且不能再合流：

$$
\boxed{
\text{Reduction path is semantically relevant}.
}
$$

因此提出候選命題：

$$
\boxed{
\text{Non-Confluence}
\Rightarrow
\text{Historical Relevance}
}
$$

更精確地說：

若不同 certified reduction paths 得到在指定等價關係下不可合流的 normal forms，則 reduction history 不能被無損商掉。

這是單向候選命題，不主張所有 history dependence 都必須來自 rewriting non-confluence。

---

# 7. Observational Confluence

有時：

$$
N_1\neq N_2
$$

但：

$$
Project_Q(N_1)
=
Project_Q(N_2).
$$

則可稱：

$$
\boxed{
N_1
\simeq_Q
N_2.
}
$$

此時 full-state rewriting 非合流，但 task-relative observation 合流。

因此需要區分：

$$
\boxed{
StrongConfluence
}
$$

與：

$$
\boxed{
ObservationalConfluence_Q.
}
$$

---

# 8. Bridge Confluence

定義：

$$
\boxed{
BridgeConfluent_\Gamma(B_1,B_2)
}
$$

若兩條合法 Bridge chain 最後滿足：

$$
Result(B_1)
\simeq_\Gamma
Result(B_2).
$$

若不成立，Bridge choice 必須寫入：

$$
History.
$$

---

# 9. ECV Normalization

對 E/C/V 三類宏算子指定 rank：

$$
r(E)=0,
\qquad
r(C)=1,
\qquad
r(V)=2.
$$

若 operator word 中存在逆序 pair，且有 commutation certificate，允許交換：

$$
O_iO_j
\Rightarrow
O_jO_i
$$

使 rank inversion 減少。

定義：

$$
Inv(W)
=
\#\{
(i,j)
:
i<j,\;
r(O_i)>r(O_j)
\}.
$$

若每次 ECV normalization rewrite 都滿足：

$$
Inv(W')
<
Inv(W),
$$

因：

$$
Inv(W)\in\mathbb N,
$$

則：

$$
\boxed{
\text{Certified ECV sorting terminates}.
}
$$

這只證明 termination，不證明 unique normal form。

---

# 10. ECV Confluence Conditions

若要存在唯一 ECV normal form，至少需要：

1. 所有需要的合法 swap 有 certificate；
2. 所有 local critical pairs 可 join；
3. Bridge choices observationally confluent；
4. Project 不提前刪除後續所需資訊；
5. History-sensitive operators 的交換已證等價；
6. Side-effects 可交換；
7. Authority effect 不依 reduction path；
8. Meta-Operators 在 normalization 期間固定，或版本被鎖定。

因此：

$$
\boxed{
Termination
\neq
Confluence.
}
$$

---

# 11. ECV-reducible 子域

定義：

$$
\boxed{
\mathfrak D_{ECV}
=
\{
W\in\mathcal W(\mathfrak P)
:
NF_{ECV}(W)
\text{ exists with certificate}
\}.
}
$$

ECV 是可正規化子域，而不是 universal ontology theorem。

---

# 12. 有限 checker 結果

本輪實作一個有限 certified rewriting toy checker。

## Experiment 1 — ECV sorting

起始：

$$
[
V,E,C,E,V,C
].
$$

起始 inversion：

$$
6.
$$

允許三種 certified swaps：

$$
CE\Rightarrow EC,
$$

$$
VE\Rightarrow EV,
$$

$$
VC\Rightarrow CV.
$$

結果唯一：

$$
\boxed{
[
E,E,C,C,V,V
].
}
$$

探索到 18 個中間 words。

每一個 rewrite 都嚴格降低 inversion count。

因此此有限系統驗證 ECV sorting termination intuition。

---

# 13. Experiment 2 — Missing Bridge

起始 chain 經局部 reduction 後得到：

$$
\boxed{
[
AB,
CD
].
}
$$

系統沒有提供：

$$
AB\rightsquigarrow CD
$$

所需 bridge。

因此不輸出單一 bottom，而保留：

$$
\boxed{
Residual=[AB,CD].
}
$$

這直接展示：

$$
\boxed{
\text{irreducible}
\neq
\text{meaningless}.
}
$$

---

# 14. Experiment 3 — Observationally Confluent Bridges

有兩條：

$$
NeedBridge\Rightarrow B_1,
$$

$$
NeedBridge\Rightarrow B_2.
$$

但兩條路徑均可 reduction 到：

$$
\boxed{
ObservedSame.
}
$$

因此：

$$
\boxed{
BridgeChoice
}
$$

在此觀測語義下可被商掉。

---

# 15. Experiment 4 — History-Preserving Non-Confluence

同樣有：

$$
B_1,B_2.
$$

但結果分別為：

$$
[
Result,H:B_1
]
$$

與：

$$
[
Result,H:B_2
].
$$

得到兩個不可再 reduction 的 normal forms。

所以有限模型中：

$$
\boxed{
BridgeChoice
\Rightarrow
DistinctHistory
\Rightarrow
NonConfluence.
}
$$

這正是 ON-RDSS History-as-State 的 rewriting 版本。

---

# 16. Operator Algebra Version

定義當期代數：

$$
\boxed{
\mathfrak A_t
=
(
\mathfrak P_t,
\Sigma_t,
Rules_t,
Bridge_t,
Cert_t,
Equiv_t
).
}
$$

Meta：

$$
\boxed{
\mathcal M_t:
\mathfrak A_t
\rightharpoonup
\mathfrak A_{t+1}.
}
$$

因此：

$$
NF_{\mathfrak A_t}(W)
$$

與：

$$
NF_{\mathfrak A_{t+1}}(W)
$$

可能不同。

Replay 因而必須保存：

$$
\boxed{
OperatorAlgebraVersion.
}
$$

---

# 17. Algebra Lock

若正在 normalization：

$$
W
\Rightarrow^\ast
NF(W),
$$

而同時：

$$
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1},
$$

結果可能失去重播性。

因此引入：

$$
\boxed{
\mathcal O_{\mathrm{AlgebraLock}}
}
$$

它不一定是 global lock，而可能只鎖定：

- reduction rule version；
- type signature version；
- bridge registry version；
- certifier version；
- equivalence version。

一次 trace 必須記：

$$
\boxed{
AlgebraSnapshotID.
}
$$

---

# 18. 12 Primitive Completeness

對 RDSS-relative operator $\mathcal O$，若存在 primitive word / wiring：

$$
W(\mathfrak P)
$$

使：

$$
W(\mathfrak P)
\Rightarrow^\ast
\mathcal O
$$

且有：

$$
Cert_{\mathrm{derive}},
$$

則稱 $\mathcal O$ 被 12 原語表示。

若 RDSS 01–09 的全部核心 operator 皆如此，得到：

$$
\boxed{
\text{RDSS-relative expressive completeness}.
}
$$

不延伸為 universal mathematical completeness。

---

# 19. Primitive Independence

逐個移除：

$$
P_i\in\mathfrak P.
$$

若仍能由：

$$
\mathfrak P\setminus\{P_i\}
$$

導出：

$$
P_i,
$$

則它只是方便 macro，不是不可約 primitive。

因此下一輪需要建立：

$$
\boxed{
\text{Primitive Elimination Test}.
}
$$

---

# 20. 新的 ON-RDSS 深層總式

不再把每一步都強行壓成單一 composite operator。

更一般表示：

$$
\boxed{
(
W_t,
\mathfrak A_t,
H_t
)
\xRightarrow[\Gamma_t,Cert_t]{\ast}
(
NF_t(W_t),
\mathfrak A_t,
H_t'
)
\xrightarrow{\mathcal M_t}
(
W_{t+1},
\mathfrak A_{t+1},
H_{t+1}
).
}
$$

若：

$$
|NF_t(W_t)|=1,
$$

則：

$$
NF_t(W_t)
=
[
\mathbb O_{t+1}
].
$$

若：

$$
|NF_t(W_t)|>1,
$$

則保留：

$$
\boxed{
\text{open computational residual}.
}
$$

這比強迫所有計算必須立即得到單一 output 更符合 RDSS 的動態／Limbo／歷史依賴思想。

---

# 21. 下一步

下一階段可正式進入：

1. **Certified Paracomposition Axioms v1**；
2. **Critical Pair Taxonomy** 的形式定義；
3. **Newman-style conditional confluence route**：在 terminating 子域中，研究 local confluence 是否足以導出 confluence；
4. **Primitive elimination checker**；
5. **Typed wiring graph checker**；
6. **ECV normal-form 子域 benchmark**。

---

# 22. 暫定結論

ON-RDSS 的數學中心已經從：

$$
\text{State Machine}
$$

一路移到：

$$
\boxed{
\text{Certified Partial Operator Rewriting}.
}
$$

目前最適合的層級化定位為：

$$
\boxed{
\text{Restriction-like local partiality}
}
$$

$$
+
$$

$$
\boxed{
\text{Certified paracomposition}
}
$$

$$
+
$$

$$
\boxed{
\text{Typed wiring / recursive bundling}
}
$$

$$
+
$$

$$
\boxed{
\text{Versioned meta-evolution}.
}
$$

真正需要證明的不再是「萬物是不是算子」，而是：

> **在部分作用、部分合成、橋接選擇、歷史、證書與規則自我改寫同時存在時，哪些子域仍具有終止性、合流性、可重播性與局部正規形？**
