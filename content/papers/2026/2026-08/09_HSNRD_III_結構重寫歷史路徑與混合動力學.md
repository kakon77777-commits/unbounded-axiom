# HSNRD III：結構重寫、歷史路徑與混合動力學
## ——從 Birth / Death / Merge / Split / Retype 到 CTMC 與 PDMP

### 摘要

HSNRD I 建立了 typed set-node、階梯集合、incidence 與 relation bundle；HSNRD II 則建立 micro-to-macro projection、資訊失真、dynamical closure 與 causal abstraction。然而，一個真正的高階社會系統不只是在固定拓撲上改變數值。家庭會形成與解散，公司會合併與分拆，機構會被創設、永久化、撤銷或改型；也就是說，高階存在的節點集合、類型與關係拓撲本身會隨歷史改變。

本文將 HSNRD 從 fixed-topology dynamics 推進為 **rewritable hybrid structural dynamics**。首先定義結構狀態為 typed attributed graph $G$ ，並以 partial rewrite rule

$$
\boxed{
\rho:G\dashrightarrow G'
}
$$

表示合法的結構轉換。本文區分 Birth、Death、Merge、Split 與 Retype 五類基本操作，並特別修正一個常見過度簡化：傳統線性 DPO rewriting 適合處理受 gluing / dangling conditions 約束的刪除、保留與新增；SqPO 則自然支援未知 context 中的刪除，而非線性 SqPO 與後續非線性 DPO 理論可進一步表達 cloning 與 fusing。因此：

$$
\boxed{
Birth/Death
\neq
Merge/Split
}
$$

是重要的操作語義區分，但不能被誤寫成「Merge 永遠不可能是 DPO」。

其次，本文將合法 rewrite 系統編譯成一個結構狀態 meta-graph：

$$
\boxed{
\mathcal G_R=(V_R,E_R),
}
$$

其中節點是完整圖狀態，邊是合法 rewrite derivation。歷史不再只是終局狀態，而是：

$$
\boxed{
History
=
RewriteWord
+
MatchHistory
+
EventTimes.
}
$$

這使 path dependence、non-commutativity、critical pairs 與 reachability 可以被明確分析。

第三，本文將 rewrite transitions 配上狀態依賴速率形成 CTMC；再將連續狀態 $x_t$ 與離散結構 $G_t$ 結合為 PDMP：

$$
\boxed{
Z_t=(G_t,x_t).
}
$$

其生成元為：

$$
\boxed{
(\mathcal L f)(G,x)
=
\nabla_x f(G,x)\cdot F_G(x)
+
\sum_{\rho,m}
\lambda_{\rho,m}(G,x)
\left[
f\!\left(G_{\rho,m}',R_{\rho,m}(G,x)\right)
-f(G,x)
\right].
}
$$

因此 HSNRD 的完整動力不再只是「圖上跑 ODE」，而是：

$$
\boxed{
ContinuousFlow
\rightarrow
StateDependentHazard
\rightarrow
TypedRewrite
\rightarrow
TopologyChange
\rightarrow
NewFlow.
}
$$

此框架構成下一篇 Feedback、Reachability 與 Safe Intervention 的必要數學基礎。

**關鍵詞：** HSNRD、graph rewriting、DPO、SqPO、rule algebra、CTMC、PDMP、path dependence、structural dynamics

---

## 1. 固定拓撲不夠

許多網路模型假設：

$$
G=(V,E)
$$

固定，

只有：

$$
x_t
$$

隨時間變化：

$$
\dot x=F_G(x).
$$

這適合：

- 固定人口；
- 固定機構；
- 固定連線；

下的 state dynamics。

但高階社會系統真正困難的地方是：

$$
\boxed{
V=V(t),\qquad E=E(t),\qquad \tau=\tau(t).
}
$$

也就是：

- 新節點出生；
- 舊節點死亡；
- 節點合併；
- 節點分裂；
- 節點改型；
- 關係新增與刪除。

所以 HSNRD 必須同時描述：

$$
\boxed{
StateDynamics
+
StructuralDynamics.
}
$$

---

## 2. 結構狀態

沿用 HSNRD I，

定義 typed attributed graph：

$$
\boxed{
G
=
(
V,E,
\tau_V,
\tau_E,
\alpha
).
}
$$

其中：

- $V$ ：typed nodes；
- $E$ ：typed relations；
- $\tau_V$ ：node typing；
- $\tau_E$ ：edge typing；
- $\alpha$ ：attributes。

完整結構狀態還可包含：

$$
\boxed{
\mathbf H
=
(
G,
\Sigma,
\mathcal B,
\Pi
)
}
$$

其中：

- $\Sigma$ ：type / relation schemas；
- $\mathcal B$ ：realization bases；
- $\Pi$ ：cross-level projections。

這些資料決定一個 rewrite 是否合法。

---

## 3. Rewrite rule 是 partial map

一條規則不是對所有圖都可用。

因此：

$$
\boxed{
\rho:
\mathbf H
\dashrightarrow
\mathbf H'
}
$$

是 partial transformation。

其 domain：

$$
Dom(\rho)
$$

由：

- pattern matching；
- type constraints；
- application conditions；
- gluing conditions；
- attribute guards；

共同決定。

所以：

$$
\boxed{
RuleExists
\not\Rightarrow
RuleApplicable.
}
$$

---

## 4. 傳統線性 DPO

經典 Double-Pushout rule 通常寫成 span：

$$
\boxed{
L
\xleftarrow{\,l\,}
K
\xrightarrow{\,r\,}
R.
}
$$

其中：

- $L$ ：左側 pattern；
- $K$ ：被保留的 interface；
- $R$ ：rewrite 後 pattern。

對 match：

$$
m:L\rightarrow G,
$$

若 pushout complement 存在，

就得到：

$$
G
\Rightarrow_\rho
H.
$$

操作直觀上是：

1. 找到 $L$ ；
2. 刪除 $L-K$ ；
3. 保留 $K$ ；
4. 加入 $R-K$ 。

---

## 5. Dangling condition

傳統 injective DPO deletion 的一個核心限制是 dangling condition。

若一個 node：

$$
v\in L-K
$$

將被刪除，

但 host graph 中存在：

$$
e\notin m(L)
$$

仍 incident to：

$$
m(v),
$$

則直接刪除會留下 dangling edge。

因此該 match 不合法。

概念上：

$$
\boxed{
DeleteNode
\Rightarrow
HandleAllIncidentEdges.
}
$$

這也是 DPO rewrite 的「context-preserving deletion」特性之一。

---

## 6. Birth 與 Death

### Birth

建立新節點：

$$
\boxed{
\mathfrak B:
G
\rightarrow
G+X_{new}.
}
$$

若：

- type 合法；
- required relations 可建立；

則一般能自然表示成線性 DPO 的 addition。

### Death

刪除節點：

$$
\boxed{
\mathfrak D:
G
\rightarrow
G-X.
}
$$

若 incident edges 被規則明確處理，並滿足 gluing / dangling conditions，

也能進入線性 DPO 語義。

因此：

$$
\boxed{
Birth/Death
}
$$

是最接近 classical add/delete rewrite 的兩類。

---

## 7. Retype

Retype 表示：

$$
\boxed{
\mathfrak T:
X^{(k,\tau_1)}
\rightarrow
X^{(k,\tau_2)}.
}
$$

例如：

$$
EmergencyCouncil
\rightarrow
PermanentEmergencyAdministration.
$$

若 type 是 attribute，

可以使用 attributed graph rewrite。

若 type 是 categorical typing morphism 的一部分，

則需確保：

- 新 type schema 合法；
- incident edge types 仍合法；
- 不合法 edges 同步轉型或刪除。

因此：

$$
\boxed{
Retype
\neq
RenameLabel.
}
$$

它可能要求 incident-relation transformation。

---

## 8. Merge 與 Split 比 add/delete 更難

考慮：

$$
\boxed{
\mathfrak M:
(X_1,X_2)
\rightarrow
X_{12}.
}
$$

若 $X_1,X_2$ 原本各有 incident relations，

合併後必須決定：

- edge redirect；
- duplicate collapse；
- attribute fusion；
- relation retyping；
- identity semantics。

所以：

$$
\boxed{
Merge
=
NodeIdentification
+
IncidentRelationTransformation
+
AttributeFusion.
}
$$

這不是普通「刪一個、改另一個名字」即可概括。

---

## 9. Split

Split：

$$
\boxed{
\mathfrak S:
X
\rightarrow
(X_1,X_2,\ldots)
}
$$

需要決定原節點 incident relations 如何分配：

- 複製到所有新節點？
- 只分給其中一個？
- 按 attribute rule 分流？
- 建立新 inter-node relations？

所以：

$$
\boxed{
Split
=
NodeCloning/Decomposition
+
RelationRedistribution.
}
$$

這正是 SqPO / non-linear rewriting 類語義較自然處理的地方。

---

## 10. DPO 與 SqPO：不能做過度二分

需要修正一個過度簡化：

> 「Merge 不是 DPO，Split 是 SqPO。」

這不夠精確。

較安全的說法是：

### Classical linear DPO

擅長：

$$
Delete/Preserve/Add
$$

且 deletion 受 dangling / gluing constraints。

### SqPO

以 final pullback complement 加 pushout 為核心，

自然處理 unknown context deletion，

並在適當非線性設定中支援 cloning / fusing。

### Non-linear DPO / SqPO

後續理論允許：

$$
\boxed{
Fusing
+
Cloning
}
$$

進入更廣的 algebraic rewrite semantics。

因此：

$$
\boxed{
ClassicalLinearDPO
\subsetneq
PossibleRewriteSemantics.
}
$$

---

## 11. HSNRD 的保守策略

所以 HSNRD 不把所有 structural operator 都宣稱成同一種 rewrite。

每條規則應標註：

$$
\boxed{
Semantics(\rho)
}
$$

例如：

| Operator | 建議初始語義 |
|---|---|
| Birth | linear DPO-compatible |
| Death | linear DPO-compatible if gluing legal |
| Retype | attributed typed rewrite |
| Merge | quotient / non-linear DPO or SqPO candidate |
| Split | cloning / non-linear SqPO candidate |

這不是最終唯一選擇，

而是：

$$
\boxed{
SemanticTypingOfRules.
}
$$

---

## 12. 不應把工程 shortcut 說成抽象定理

若 MVP 中用 Python 函數：

```text
merge(A,B)
```

完成：

- node deletion；
- edge redirect；
- attribute averaging；

這只證明：

> 一個特定 operational semantics 可執行。

它不證明：

$$
\boxed{
AbstractCategoricalMerge
}
$$

已被形式化。

因此：

$$
\boxed{
ExecutableRewrite
\neq
ProvedRewriteSemantics.
}
$$

這是 HSNRD 方法論必須保留的界線。

---

## 13. Rewrite System

定義規則集合：

$$
\boxed{
\mathcal P
=
\{
\rho_1,\ldots,\rho_R
\}.
}
$$

結構狀態集合：

$$
\boxed{
\mathcal H.
}
$$

定義直接 derivation：

$$
\boxed{
H
\xRightarrow[\rho,m]{}
H'
}
$$

表示規則 $\rho$ 透過 admissible match $m$ 將 $H$ 轉成 $H'$ 。

因此 rewrite system：

$$
\boxed{
\mathfrak R
=
(
\mathcal H,
\mathcal P,
\Rightarrow
).
}
$$

---

## 14. Match 不能被省略

同一規則：

$$
\rho
$$

在同一 graph：

$$
G
$$

可能有多個合法 matches：

$$
m_1,m_2,\ldots,m_q.
$$

所以真正的 event identity 應是：

$$
\boxed{
(\rho,m).
}
$$

而不只是：

$$
\rho.
$$

這對 stochastic rewriting 特別重要。

因為 event rate 可以是：

$$
\lambda_{\rho,m}.
$$

---

## 15. 結構狀態 meta-graph

把所有可達 canonical states 當成節點：

$$
\boxed{
V_R
=
\{
[G]
\}
}
$$

其中：

$$
[G]
$$

是 graph isomorphism class / chosen canonical form。

若存在：

$$
G
\xRightarrow[\rho,m]{}
G',
$$

建立 meta-edge：

$$
[G]
\rightarrow
[G'].
$$

得到：

$$
\boxed{
\mathcal G_R
=
(
V_R,E_R
).
}
$$

這是一張：

# **Rewrite Reachability Meta-Graph**

---

## 16. History 是 meta-graph 上的 path

因此歷史：

$$
\boxed{
History
=
Path(\mathcal G_R).
}
$$

更完整地：

$$
\boxed{
h_n
=
(
G_0,
(\rho_1,m_1),
G_1,
\ldots,
(\rho_n,m_n),
G_n
).
}
$$

這比只保存：

$$
G_n
$$

資訊更多。

所以：

$$
\boxed{
FinalState
\neq
History.
}
$$

---

## 17. Same Final Graph, Different History

可能：

$$
G_0
\xrightarrow{\rho_a}
G_1
\xrightarrow{\rho_b}
G_f
$$

以及：

$$
G_0
\xrightarrow{\rho_c}
G_2
\xrightarrow{\rho_d}
G_f.
$$

若 canonical graph 相同：

$$
G_f^{(1)}
\cong
G_f^{(2)},
$$

仍不能推出：

- legitimacy history 相同；
- memory 相同；
- path cost 相同；
- event timing 相同；
- hidden attributes 相同。

因此：

$$
\boxed{
SameCanonicalGraph
\neq
SameHistoricalState
}
$$

除非 state definition 已包含全部歷史 relevant variables。

---

## 18. Rule composition

若：

$$
\rho_1
$$

之後可以合法接：

$$
\rho_2,
$$

可考慮 sequential composition：

$$
\boxed{
\rho_2\circ_m\rho_1.
}
$$

DPO concurrency theory 與 rule-algebra framework 表明，在適當 adhesive / $\mathcal M$-adhesive 條件下，rule composition 可以具有自然 associativity。

但這個 associativity 是：

$$
\boxed{
WithinAFormalRewriteTheory.
}
$$

不是：

> 任意 Python rewrite functions 混在一起也自動形成 associative algebra。

---

## 19. Rule Algebra

在適當 rewrite category 中，

可以構造以規則 isomorphism classes 為 basis 的向量空間：

$$
\boxed{
\mathcal R
=
span\{
|\rho\rangle
\}.
}
$$

乘法：

$$
|\rho_2\rangle
*
|\rho_1\rangle
$$

對所有 admissible overlaps 的 composite rules 求和。

其意義是：

$$
\boxed{
RuleComposition
}
$$

被編碼成 algebraic product。

這為：

- concurrency；
- stochastic mechanics；
- moment equations；

提供工具。

---

## 20. Mixed Semantics 的限制

HSNRD 可能同時使用：

- linear DPO birth；
- attributed retype；
- non-linear SqPO split；
- custom quotient merge。

此時不能直接宣稱：

$$
\boxed{
AllRulesFormOneProvedRuleAlgebra.
}
$$

除非找到共同 categorical setting 並證明其 closure / associativity。

因此早期有限狀態 operator representation：

$$
R_\rho
$$

最多表示：

$$
\boxed{
FiniteStateActionRepresentation.
}
$$

不是抽象 rewrite algebra 已被完全證明。

---

## 21. Finite-state rule operators

若可達 state space 有限：

$$
\mathcal H
=
\{
G_1,\ldots,G_N
\},
$$

定義：

$$
\mathcal V
=
span\{
|G_1\rangle,\ldots,|G_N\rangle
\}.
$$

一條 deterministic canonical rule 可表示成 linear operator：

$$
\boxed{
R_\rho:
\mathcal V
\rightarrow
\mathcal V.
}
$$

如果 rule 在某 state 不可用，

可以：

- 映為 0；
- 或保留 state；
- 或另定 partial representation。

語義必須顯式指定。

---

## 22. Non-commutativity 與 path dependence

兩條 rule operators：

$$
R_a,R_b
$$

若：

$$
R_aR_b
\neq
R_bR_a,
$$

則：

$$
\boxed{
[R_a,R_b]
=
R_aR_b-R_bR_a
\neq0.
}
$$

這表示：

> rule order 會改變結果或可達域。

因此：

$$
\boxed{
RewriteNonCommutativity
\Rightarrow
PotentialPathDependence.
}
$$

但 nonzero commutator 不是社會科學上的所有「歷史依賴」之完整定義。

它是有限 operator representation 中的一個 structural diagnostic。

---

## 23. Critical Pairs

若兩條規則：

$$
\rho_a,\rho_b
$$

競爭相同 graph context，

可能得到：

$$
G
\xrightarrow{\rho_a}
G_a
$$

與：

$$
G
\xrightarrow{\rho_b}
G_b.
$$

接著問：

$$
\exists H:
G_a\Rightarrow^* H
\land
G_b\Rightarrow^* H?
$$

若不能 join，

可能形成 non-confluent branch。

因此：

$$
\boxed{
CriticalPairAnalysis
}
$$

是結構 path dependence 的另一種正式工具。

---

## 24. Reachability

定義：

$$
\boxed{
Reach(G,G')
=
1
}
$$

若：

$$
G\Rightarrow^*G'.
$$

對集合：

$$
A\subseteq\mathcal H,
$$

則：

$$
\boxed{
Reach(G,A)
}
$$

問是否存在路徑進入 $A$ 。

這讓：

- exit；
- death；
- reform；
- permanence；

都可以轉成 structural reachability 問題。

---

## 25. Reachability 不等於 Probability

如果：

$$
Reach(G,G')=1,
$$

只表示：

> 存在至少一條合法 rewrite path。

它不表示：

$$
P(G_t=G')\gg0.
$$

因此：

$$
\boxed{
Possible
\neq
Likely
\neq
Realized.
}
$$

這正是要引入 stochastic rewriting 的原因。

---

## 26. Stochastic rewriting

給每一 admissible event：

$$
(\rho,m)
$$

一個 hazard：

$$
\boxed{
\lambda_{\rho,m}(G)\ge0.
}
$$

若同一 rule 有多個 matches，

rule-level aggregate hazard：

$$
\boxed{
\Lambda_\rho(G)
=
\sum_{m\in M_\rho(G)}
\lambda_{\rho,m}(G).
}
$$

總離開率：

$$
\boxed{
\Lambda(G)
=
\sum_{\rho}
\Lambda_\rho(G).
}
$$

---

## 27. CTMC generator

若 state space 離散，

定義 transition rate：

$$
q(G,G')
=
\sum_{\rho,m:
G_{\rho,m}'=G'}
\lambda_{\rho,m}(G).
$$

採 column-vector convention：

$$
p_G(t)
=
P(G_t=G),
$$

則 generator：

$$
\boxed{
H_{G',G}
=
q(G,G'),
\qquad
G'\neq G,
}
$$

而：

$$
\boxed{
H_{G,G}
=
-\sum_{G'\neq G}
q(G,G').
}
$$

所以：

$$
\boxed{
\dot p
=
Hp.
}
$$

---

## 28. Generator 的基本守恆

column convention 下：

$$
\boxed{
\mathbf 1^\top H=0.
}
$$

因此：

$$
\frac{d}{dt}
\mathbf 1^\top p(t)
=
0.
$$

也就是總機率保存。

如果：

$$
p(0)
$$

是 probability vector，

則：

$$
\boxed{
p(t)=e^{tH}p(0).
}
$$

---

## 29. CTMC history 不只有 rule word

在 stochastic rewriting 中，

兩條歷史即使 rule sequence 相同：

$$
\rho_1,\rho_2,\rho_3
$$

若 event times 不同，

在 coupled continuous system 中可能得到不同結果。

因此完整歷史應寫：

$$
\boxed{
History
=
(
RewriteWord,
MatchSequence,
EventTimes
).
}
$$

其中：

$$
0<\tau_1<\tau_2<\cdots.
$$

---

## 30. 為什麼 CTMC 還不夠？

如果制度結構在 jump 之間仍有：

- legitimacy；
- authority；
- citizen preference；
- policy；
- financial state；
- memory strength；

等 continuous dynamics，

則只用：

$$
G_t
$$

不夠。

需要：

$$
\boxed{
x_t\in\mathbb R^d.
}
$$

並令：

$$
\boxed{
Z_t=(G_t,x_t).
}
$$

---

## 31. Piecewise Deterministic Markov Process

PDMP 的核心就是：

> jump 之間 deterministic flow，jump 時 stochastic structural change。

對固定 graph：

$$
G,
$$

連續狀態滿足：

$$
\boxed{
\dot x
=
F_G(x).
}
$$

下一 jump 的 hazard 由：

$$
\lambda_{\rho,m}(G,x)
$$

決定。

jump 後：

$$
G
\rightarrow
G_{\rho,m}',
$$

同時 continuous state 可以 reset：

$$
\boxed{
x
\rightarrow
R_{\rho,m}(G,x).
}
$$

---

## 32. HSNRD Hybrid State

因此完整 state：

$$
\boxed{
Z_t
=
(
G_t,x_t
).
}
$$

若 schema / projection 本身也動態，

可以再擴充：

$$
Z_t
=
(
G_t,x_t,\Sigma_t,\Pi_t
).
$$

但最小 PDMP 版本採：

$$
(G_t,x_t).
$$

---

## 33. PDMP generator

對適當 test function：

$$
f(G,x),
$$

HSNRD generator：

$$
\boxed{
(\mathcal L f)(G,x)
=
\nabla_x f(G,x)
\cdot
F_G(x)
+
\sum_{\rho}
\sum_{m\in M_\rho(G)}
\lambda_{\rho,m}(G,x)
\left[
f(
G_{\rho,m}',
R_{\rho,m}(G,x)
)
-
f(G,x)
\right].
}
$$

第一項：

$$
\boxed{
ContinuousFlow.
}
$$

第二項：

$$
\boxed{
StochasticStructuralJump.
}
$$

---

## 34. 這個 generator 的語義

整個閉環：

$$
\boxed{
x
\rightarrow
\lambda_{\rho,m}(G,x)
\rightarrow
Rewrite
\rightarrow
G'
\rightarrow
F_{G'}
\rightarrow
x'.
}
$$

所以 continuous state 影響：

$$
StructureChange.
$$

而 structure 又反過來改變：

$$
ContinuousDynamics.
$$

這就是：

$$
\boxed{
HybridStructuralFeedback.
}
$$

---

## 35. State-dependent hazard

例如 EmergencyCouncil birth hazard：

$$
\lambda_{Birth}(G,x)
$$

可以依賴：

- crisis level；
- legitimacy；
- political support；
- legal authorization。

Death hazard：

$$
\lambda_{Death}(G,x)
$$

可以依賴：

- emergency decay；
- sunset rule；
- institutional age。

所以：

$$
\boxed{
RewriteTiming
}
$$

不是外生固定參數。

它可以被 state endogenously 調節。

---

## 36. Reset 也很重要

Birth 不是只增加 graph node。

它可能同時：

$$
Authority\uparrow,
$$

$$
Oversight\downarrow,
$$

$$
Legitimacy\rightarrow L_{new}.
$$

所以：

$$
\boxed{
StructuralJump
\Rightarrow
ContinuousStateReset
}
$$

完全可能。

如果忽略 reset，

會漏掉 rewrite 對 state 的 immediate effect。

---

## 37. Compile Structure, Run Dynamics

HSNRD 可分兩階段。

### Compile time

檢查：

- type legality；
- DPO / SqPO conditions；
- admissible matches；
- rewrite targets。

得到：

$$
\boxed{
Compiled(G)
=
\{
(\rho,m,G')
\}.
}
$$

### Runtime

對每一合法 event 計算：

$$
\lambda_{\rho,m}(G,x),
$$

然後：

- integrate flow；
- sample jump；
- apply reset；
- switch graph。

因此：

$$
\boxed{
CompileStructure
\rightarrow
RunDynamics.
}
$$

---

## 38. Exact PDMP 與數值近似要分開

理論 PDMP jump time滿足 cumulative hazard：

$$
\boxed{
\int_0^{T}
\Lambda(
G,\phi_G(s,x)
)
ds
=
E,
}
$$

其中：

$$
E\sim Exp(1).
$$

數值模擬若用固定步長：

$$
\Delta t
$$

累積 hazard，

只是 approximate event localization。

所以：

$$
\boxed{
FixedStepSimulation
\neq
ExactPDMP.
}
$$

論文與工程報告必須分開聲明。

---

## 39. Non-explosion

若 jump rate 無界或規則能無限快速生成新結構，

可能出現：

$$
\tau_n
\rightarrow
\tau_\infty<\infty.
$$

即 finite-time explosion。

因此實際 HSNRD PDMP 需檢查：

- rate boundedness；
- Lyapunov conditions；
- population growth；
- structural explosion。

所以：

$$
\boxed{
WellDefinedRewriteRules
\not\Rightarrow
NonExplosiveProcess.
}
$$

---

## 40. Stationarity 不能亂說

對 CTMC / PDMP，

即使 generator：

$$
H
$$

存在，

也不能直接說：

> 系統有唯一 stationary distribution。

可能：

- 多個 closed classes；
- absorbing states；
- non-ergodicity；
- no invariant probability。

所以：

$$
\boxed{
GeneratorExists
\not\Rightarrow
UniqueStationarity.
}
$$

必須另外證明 irreducibility / recurrence / ergodicity 類條件。

---

## 41. Graph Rewrite 對高階存在的語義

現在可以重新看 Birth：

$$
\boxed{
Proto
\rightarrow
Institution.
}
$$

不是：

> 一個數值超過 threshold。

而是：

$$
\boxed{
OntologyChanges.
}
$$

同理 Death：

$$
Institution
\rightarrow
Absent.
$$

Retype：

$$
Temporary
\rightarrow
Permanent.
$$

Merge：

$$
A+B
\rightarrow
C.
$$

Split：

$$
C
\rightarrow
A+B.
$$

這些都改變：

$$
\boxed{
WhatEntitiesExist.
}
$$

---

## 42. Birth Condition 不等於 Persistence Condition

若 birth threshold：

$$
\theta_B
$$

與 death threshold：

$$
\theta_D
$$

滿足：

$$
\boxed{
\theta_D<\theta_B,
}
$$

則產生 hysteresis。

也就是：

$$
\boxed{
BirthCondition
\neq
PersistenceCondition.
}
$$

一個制度形成後，

即使原始形成條件消失，

仍可能持續。

這是高階存在最重要的歷史效應之一。

---

## 43. Retype 不是 Persistence

如果 temporary institution：

$$
EC
$$

轉成：

$$
PermanentAdministration,
$$

則：

$$
\boxed{
Retype
}
$$

不同於：

$$
\boxed{
LongPersistence.
}
$$

前者：

> ontology/type 改變。

後者：

> 同一 type 持續存在。

所以：

$$
\boxed{
TemporalPersistence
\neq
OntologicalRetyping.
}
$$

---

## 44. Merge 也不是「兩個節點數值加起來」

若：

$$
A+B\rightarrow C,
$$

需要重新決定：

$$
\mathcal B_C,
$$

也就是 realization base，

以及：

$$
\Pi_C.
$$

因此：

$$
\boxed{
Merge
}
$$

甚至可能改變 micro-to-macro projection。

所以：

$$
\boxed{
StructuralRewrite
\Rightarrow
ProjectionRewrite
}
$$

有時必須一起發生。

---

## 45. Split 同樣改變代理結構

如果：

$$
StateAgency
$$

原本由：

$$
C
$$

形成，

Split：

$$
C\rightarrow C_1+C_2
$$

可能改變：

- decision closure；
- authority；
- feedback；
- memory ownership。

因此：

$$
\boxed{
Split
}
$$

不只是 topology operation。

也可能造成：

$$
\boxed{
AgencyDecomposition.
}
$$

---

## 46. Structural History 與 Agency History

因此：

$$
\boxed{
History
}
$$

至少有兩層：

### Structural history

$$
G_0\Rightarrow G_1\Rightarrow\cdots
$$

### Agency history

$$
A_0\rightarrow A_1\rightarrow\cdots
$$

兩者耦合：

$$
\boxed{
G_t
\leftrightarrow
Agency_t.
}
$$

相同 graph topology 也可能因 memory / state 不同而具有不同 agency。

---

## 47. Leviathan Reversal 的 rewrite 表示

第五篇的：

$$
ExitLoss
$$

現在可以表示成：

$$
\boxed{
\lambda_{Death}\downarrow,
\quad
\lambda_{RetypeExit}\downarrow,
\quad
Reach(G,\mathcal A_{alternative})\downarrow.
}
$$

Downward Reshaping 則進入：

$$
F_G(x)
$$

與：

$$
R_{\rho,m}(x).
$$

所以 Leviathan Reversal 不再只是概念比喻，

而可以嵌入：

$$
\boxed{
PDMPOnRewriteStateSpace.
}
$$

---

## 48. Feedback Dormancy 的結構基礎

如果系統已進入：

$$
G_{locked}
$$

且：

$$
M_\rho(G_{locked})=\varnothing
$$

對所有 exit rules 成立，

那麼：

$$
\lambda_{exit}=0.
$$

此時沒有 active feedback loop，

也可能只是：

$$
\boxed{
NoAvailableRewrite.
}
$$

所以：

$$
\boxed{
NoEvent
\neq
NoConstraint.
}
$$

這就是 locked dormancy 的 rewrite 基礎。

---

## 49. HSNRD III 的核心公理／限制

### Axiom R1 — Structural State Is Explicit

$$
\boxed{
G=G(t).
}
$$

### Axiom R2 — Rules Are Partial

$$
\boxed{
\rho:G\dashrightarrow G'.
}
$$

### Axiom R3 — Match Matters

事件 identity 是：

$$
\boxed{
(\rho,m).
}
$$

### Axiom R4 — Rewrite Semantics Must Be Typed

每條 rule 必須標註：

$$
Semantics(\rho).
$$

### Axiom R5 — Classical DPO Is Not Universal

$$
\boxed{
LinearDPO
\neq
AllStructuralRewrite.
}
$$

### Axiom R6 — Executability Is Not Formal Proof

$$
\boxed{
ExecutableRewrite
\neq
ProvedCategoricalSemantics.
}
$$

### Axiom R7 — Reachability Is Not Probability

$$
\boxed{
Reachable
\neq
Likely.
}
$$

### Axiom R8 — Final State Is Not History

$$
\boxed{
FinalState
\neq
RewriteHistory.
}
$$

### Axiom R9 — CTMC Requires Rates

rewrite graph alone不構成 stochastic process。

### Axiom R10 — PDMP Couples Structure and State

$$
\boxed{
x
\leftrightarrow
G.
}
$$

### Axiom R11 — Stationarity Requires Additional Proof

$$
Generator
\not\Rightarrow
UniqueStationaryDistribution.
$$

---

## 50. 完整 HSNRD 動力鏈

到此，前八篇的：

$$
Set,
Type,
Relation,
Projection
$$

終於真正動起來。

完整鏈變成：

$$
\boxed{
Set
\rightarrow
TypedGraph
\rightarrow
Projection
\rightarrow
RewriteGrammar
\rightarrow
ReachabilityGraph
\rightarrow
StochasticRewrite
\rightarrow
CTMC
\rightarrow
PDMP.
}
$$

但這仍然缺最後一層：

> 哪些 feedback 真正重要？

> 哪些節點是 path gate？

> 切斷 loop 為什麼可能反而把系統推進 absorbing trap？

> 怎麼設計安全 intervention？

這就是下一篇的任務。

---

## 51. 結論

HSNRD III 的核心改變是：

$$
\boxed{
Topology
}
$$

不再只是 dynamics 的固定背景。

它自己就是：

$$
\boxed{
DynamicState.
}
$$

高階存在可以：

$$
Birth,
Death,
Merge,
Split,
Retype.
$$

而每個 structural event 都必須具有：

- 合法 match；
- type semantics；
- rewrite semantics；
- stochastic hazard；
- possible continuous reset。

因此：

$$
\boxed{
History
=
RewriteWord
+
MatchHistory
+
EventTimes.
}
$$

而：

$$
\boxed{
Possible
\neq
Likely
\neq
Realized.
}
$$

在 continuous state 也參與時，

完整 HSNRD state 為：

$$
\boxed{
Z_t=(G_t,x_t),
}
$$

生成元：

$$
\boxed{
(\mathcal L f)(G,x)
=
\nabla_x f\cdot F_G(x)
+
\sum_{\rho,m}
\lambda_{\rho,m}(G,x)
[
f(G'_{\rho,m},R_{\rho,m}(G,x))-f(G,x)
].
}
$$

所以 HSNRD 的動力本質是：

$$
\boxed{
State
\rightarrow
Hazard
\rightarrow
Rewrite
\rightarrow
Topology
\rightarrow
NewFlow
\rightarrow
State.
}
$$

這使高階存在的「出生、歷史、制度化、固著與死亡」進入同一個數學框架。

下一篇，也是全系列最後一篇，將處理：

# **HSNRD IV：Feedback、Reachability 與安全介入**

並把 v0.7–v1.0 的 feedback graph、loop polarity、gate importance、counterfactual intervention 與 safe optimizer 收斂成完整方法論。

---

## 參考文獻

Behr, N. (2021). “On Stochastic Rewriting and Combinatorics via Rule-Algebraic Methods.” arXiv:2102.02364.

Behr, N. (2019). “Sesqui-Pushout Rewriting: Concurrency, Associativity and Rule Algebra Framework.” arXiv:1904.08357.

Behr, N., Harmer, R., & Krivine, J. (2021). “Concurrency Theorems for Non-linear Rewriting Theories.” arXiv:2105.02842.

Behr, N., & Sobociński, P. (2020). “Rule Algebras for Adhesive Categories.” *Logical Methods in Computer Science*, 16(3).

Behr, N., Bello, B. S., Ehmes, S., & Heckel, R. (2021). “Stochastic Graph Transformation for Social Network Modeling.” EPTCS 350.

Czapla, D. (2024). “On the Existence and Uniqueness of Stationary Distributions for Some Piecewise Deterministic Markov Processes with State-Dependent Jump Intensity.” *Results in Mathematics*, 79, 177.

Davis, M. H. A. (1984). “Piecewise-Deterministic Markov Processes: A General Class of Non-Diffusion Stochastic Models.” *Journal of the Royal Statistical Society, Series B*, 46(3), 353–376.

Davis, M. H. A. (1993). *Markov Models and Optimization*. Chapman & Hall.

Danos, V., Harmer, R., & Honorato-Zimmer, R. (2015). “Thermodynamic Graph-Rewriting.” *Logical Methods in Computer Science*, 11(2).

Ehrig, H., Ehrig, K., Prange, U., & Taentzer, G. (2006). *Fundamentals of Algebraic Graph Transformation*. Springer.

---

## 本篇核心命題表

| 編號 | 命題 |
|---|---|
| R1 | $StateDynamics\neq StructuralDynamics$ |
| R2 | $RuleExists\not\Rightarrow RuleApplicable$ |
| R3 | $Birth/Death\neq Merge/Split$ |
| R4 | $ClassicalLinearDPO\neq AllStructuralRewrite$ |
| R5 | $ExecutableRewrite\neq ProvedRewriteSemantics$ |
| R6 | $FinalState\neq History$ |
| R7 | $SameCanonicalGraph\neq SameHistoricalState$ |
| R8 | $RewriteNonCommutativity\Rightarrow PotentialPathDependence$ |
| R9 | $Reachable\neq Likely\neq Realized$ |
| R10 | $History=(RewriteWord,MatchSequence,EventTimes)$ |
| R11 | $FixedStepSimulation\neq ExactPDMP$ |
| R12 | $GeneratorExists\not\Rightarrow UniqueStationarity$ |
| R13 | $BirthCondition\neq PersistenceCondition$ |
| R14 | $TemporalPersistence\neq OntologicalRetyping$ |
| R15 | $StructuralRewrite$ may require $ProjectionRewrite$ |
| R16 | $Topology$ is itself a dynamic state variable |

---

**系列：高階集合、欲求與 Leviathan / HSNRD 完整数學方法論**  
**第二部：HSNRD 完整数學方法論**  
**篇次：09 / 10**
