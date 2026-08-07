# HSNRD I：階梯集合、類型與關係束
## ——高階集合動力學的靜態本體與關係基底

**系列：**《高階集合欲求》  
**篇次：** 07 / 10  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-07  

### 摘要

前六篇已建立高階集合欲求的概念與本體論框架，但若要使「人民、家庭、公司、國家、文明、制度」等不同階數的集合存在進入可計算模型，僅靠自然語言中的「層級」「節點」「關係」不足以保證數學合法性。HSNRD（Hierarchical Set-Node Relational Dynamics，階梯集合節點—關係束動力系統）的第一個方法論任務，是先建立一個不混淆集合論、圖論、類型理論、範疇論與多層網路的靜態基底。

本文提出 HSNRD 的基本對象為帶有階數、類型、成員實現與關係結構的 typed set-node：

$$
\boxed{
X_i^{(k,\tau)}
}
$$

其中 $k$ 是 HSNRD 的模型存在階數，而非 ZF 集合論中的 rank； $\tau$ 是節點類型； $i$ 是同階同型物件的識別索引。本文進一步定義階梯集合族、成員／實現映射、型別化關係、關係束（relation bundle）、多層有向圖以及節點—成員 incidence 結構。

本文特別建立三條合法性原則。第一，集合成員關係與圖關係必須分離：允許關係圖具有自環與循環，不代表允許 $X\in X$ 。第二，HSNRD 預設採 well-founded set semantics；若未來需要真正的集合自包含，必須明確切換到非良基集合論，例如 Aczel 的 Anti-Foundation Axiom，而不能把 graph self-loop 偷渡成 membership self-reference。第三，「relation bundle」在本文只是同一節點對之間多種 typed relations 的集合式封裝，不宣稱它是微分幾何中的正式 fiber bundle。

本文亦說明各數學工具的角色分工：

$$
\boxed{
Set/Incidence
\rightarrow
Type
\rightarrow
MultilayerRelation
\rightarrow
Graph
\rightarrow
ComposableMorphism
}
$$

其中 set/incidence 負責存在與包含，type 負責合法配對，多層圖負責耦合，範疇論僅負責 morphism 的組合與後續 rewrite 語義。本文因此構成 HSNRD 第二部的靜態公理基底，並為後續投影、資訊失真、代理形成、結構重寫與混合動力學提供統一接口。

**關鍵詞：** HSNRD、階梯集合、typed graph、multilayer network、relation bundle、incidence、graph transformation、well-founded set

---

## 1. 為什麼 HSNRD 不能只叫「多層圖」？

如果我們只想表示：

- 人與人；
- 公司與公司；
- 國家與國家；

之間的關係，多層網路已經非常強大。

Kivelä 等人的 multilayer-network 框架可以將不同層、不同類型連結與 inter-layer coupling 納入同一網路表示。

但 HSNRD 還有一個多層網路本身沒有替我們解決的問題：

> **一個節點是否本身是由另一層節點構成、實現、聚合或湧生的高階存在？**

例如：

$$
Person_i
$$

與：

$$
Family_j
$$

不能只被視作兩種平行節點。

因為：

$$
Person_i
$$

可能同時是：

$$
Family_j
$$

的成員與實現基底之一。

同理：

$$
Institution
$$

與：

$$
State
$$

之間也可能不是普通「連線」而已，

而是：

$$
\boxed{
ConstitutiveRelation.
}
$$

所以 HSNRD 必須同時保留：

1. set / incidence semantics；
2. graph relation semantics。

不能把所有東西都塞進單一 adjacency matrix。

---

## 2. HSNRD 的階梯集合

定義 HSNRD existence ladder：

$$
\boxed{
\mathcal L
=
\{
\mathcal L_0,
\mathcal L_1,
\ldots,
\mathcal L_K
\}.
}
$$

其中：

$$
\mathcal L_k
=
\{
X_i^{(k,\tau)}
\}.
$$

每一個：

$$
X_i^{(k,\tau)}
$$

表示：

- 階數 $k$ ；
- 類型 $\tau$ ；
- 索引 $i$ 。

例如：

$$
X_{17}^{(1,\mathrm{Person})}
$$

可以代表某個人。

$$
X_{3}^{(2,\mathrm{Family})}
$$

代表某個家庭。

$$
X_{8}^{(2,\mathrm{Corporation})}
$$

代表某公司。

$$
X_{1}^{(3,\mathrm{State})}
$$

代表某國家層高階存在。

---

## 3. 這不是 ZF rank

非常重要：

$$
\boxed{
k
\neq
rank_{ZF}(X).
}
$$

HSNRD 的 $k$ 是**模型中的存在階數**。

它回答：

> 在本模型中，這個對象相對於其他對象處於哪一個構成／聚合尺度？

不是：

> 這個集合在 von Neumann cumulative hierarchy 中的 rank 是多少？

因此：

$$
\mathcal L_1
\rightarrow
\mathcal L_2
$$

不代表：

$$
rank(X^{(2)})=rank(X^{(1)})+1.
$$

這是一個建模階梯，不是基礎集合論的宇宙階梯。

---

## 4. $\mathcal L_0$ 也不是空集合

早期直覺很容易把：

$$
\mathcal L_0
$$

寫成：

$$
\varnothing.
$$

本文不採這種定義。

更合理的是：

$$
\boxed{
\mathcal L_0
=
Latent/PotentialStateSpace.
}
$$

它可以表示：

- 尚未個體化的狀態；
- 資源；
- 潛在角色；
- 環境場；
- 未生成的 proto-node。

例如某個 crisis condition 尚未形成 EmergencyCouncil，

但：

$$
EmergencyCouncil_{proto}
$$

可以存在於：

$$
\mathcal L_0
$$

或一個 potential-object layer。

因此：

$$
\boxed{
PotentialExistence
\neq
EmptySet.
}
$$

---

## 5. 同階不等型

一個重要原則是：

$$
\boxed{
SameOrder
\not\Rightarrow
SameType.
}
$$

例如：

$$
Family,
Corporation,
ReligiousGroup
$$

可以都位於：

$$
\mathcal L_2,
$$

但它們的存在條件完全不同。

因此：

$$
X_a^{(2,\mathrm{Family})}
$$

與：

$$
X_b^{(2,\mathrm{Corporation})}
$$

不能只靠：

$$
k=2
$$

判斷其合法關係與形成條件。

類型：

$$
\tau
$$

是不可省略的。

---

## 6. Type Universe

定義節點類型集合：

$$
\boxed{
\mathcal T_V
=
\{
\tau_1,\tau_2,\ldots
\}.
}
$$

例如：

$$
\mathcal T_V
\supseteq
\{
Person,
Family,
Corporation,
Court,
Legislature,
State,
Civilization
\}.
$$

每個 type 可以有自己的 schema：

$$
\boxed{
\Sigma_\tau.
}
$$

其中包含：

- 必要 attributes；
- 可接受 member types；
- 合法 relation types；
- existence conditions；
- allowable rewrite operations。

所以：

$$
\boxed{
Type
=
OntologyConstraint,
}
$$

而不只是顯示標籤。

---

## 7. 節點本體

一個 HSNRD node 可先定義為：

$$
\boxed{
X_i^{(k,\tau)}
=
(
id_i,
k,
\tau,
a_i,
M_i,
B_i
).
}
$$

其中：

- $id_i$ ：識別；
- $k$ ：existence order；
- $\tau$ ：type；
- $a_i$ ：attribute state；
- $M_i$ ：member / realization references；
- $B_i$ ：boundary / identity information。

這仍然只是最小 schema。

後續可以再加入：

$$
Memory,
Preference,
Agency,
SelfModel.
$$

但 HSNRD I 暫時不要求所有節點都是 agent。

所以：

$$
\boxed{
Node
\neq
Agent.
}
$$

---

## 8. Membership 與 Realization 必須區分

對高階存在，可以存在：

$$
m\in M(X)
$$

表示：

> $m$ 是 $X$ 的成員。

但不是每一個 realization component 都必須是社會成員。

例如公司：

$$
Corporation
$$

的 realization base 可能包括：

- 員工；
- 股東；
- 規則；
- 資料庫；
- 合約；
- 資產。

因此應區分：

$$
\boxed{
MemberOf(m,X)
}
$$

與：

$$
\boxed{
Realizes(r,X).
}
$$

所以完整 realization base：

$$
\mathcal B_X
$$

一般滿足：

$$
M(X)
\subseteq
\mathcal B_X,
$$

但：

$$
\boxed{
M(X)
\neq
\mathcal B_X
}
$$

通常成立。

---

## 9. Incidence Structure

令所有低階 realization objects 集合為：

$$
V_-,
$$

高階 nodes 為：

$$
V_+.
$$

可以定義 incidence matrix：

$$
\boxed{
P_{Xi}
=
\begin{cases}
1,& i\text{ contributes to }X,\\
0,& otherwise.
\end{cases}
}
$$

若 membership / realization 需要權重：

$$
P_{Xi}\in[0,1]
$$

或更一般：

$$
P_{Xi}\in\mathbb R.
$$

但權重語義必須由 type schema 定義。

因此：

$$
\boxed{
P
}
$$

不是普通 adjacency matrix。

它回答的是：

> 哪些低階對象構成／實現哪些高階對象？

---

## 10. Constitutive Edge 與 Ordinary Relation 不同

令：

$$
\eta:
X_i^{(k)}
\rightarrow
X_j^{(k+1)}
$$

表示 membership / constitution。

另一方面：

$$
e:
X_i^{(k)}
\rightarrow
X_j^{(m)}
$$

可能只是：

- influence；
- trade；
- command；
- belief；
- coercion；
- information。

兩者必須分開。

因此：

$$
\boxed{
Constitution
\neq
Interaction.
}
$$

這是 HSNRD 最根本的圖模型校正之一。

---

## 11. Relation Type Universe

定義關係類型：

$$
\boxed{
\mathcal T_E
=
\{
\rho_1,\rho_2,\ldots
\}.
}
$$

例如：

$$
\{
economic,
political,
informational,
coercive,
belief,
command,
review,
implementation,
finance
\}.
$$

每一個 relation type：

$$
\rho
$$

帶有 source-target legality：

$$
\boxed{
s_\rho
\subseteq
\mathcal T_V,
\qquad
t_\rho
\subseteq
\mathcal T_V.
}
$$

例如：

$$
command:
Executive
\rightarrow
Bureaucracy
$$

可能合法，

但：

$$
command:
CentralBank
\rightarrow
Family
$$

可能在某 schema 中不合法。

這些不是圖演算法自己知道的。

它們由：

$$
\Sigma_\tau,\Sigma_\rho
$$

共同決定。

---

## 12. Typed Edge

一條 typed relation 可寫：

$$
\boxed{
e_{ij}^{(\rho)}
=
(
i,
j,
\rho,
w_{ij}^{(\rho)},
d_{ij}^{(\rho)},
c_{ij}^{(\rho)},
b_{ij}^{(\rho)}
).
}
$$

其中：

- $\rho$ ：relation type；
- $w$ ：weight；
- $d$ ：direction；
- $c$ ：capacity / constraint；
- $b$ ：boundary / validity metadata。

在時間模型中：

$$
w_{ij}^{(\rho)}
=
w_{ij}^{(\rho)}(t).
$$

所以關係本身可以動態改變。

---

## 13. 非對稱性是預設，不是例外

社會與制度關係通常：

$$
W_{ij}
\neq
W_{ji}.
$$

例如：

$$
Authority(State\rightarrow Citizen)
$$

與：

$$
Influence(Citizen\rightarrow State)
$$

完全不是同一種東西。

因此 HSNRD 預設使用：

$$
\boxed{
DirectedTypedRelations.
}
$$

無向關係是特殊情況。

不是預設。

---

## 14. Relation Bundle

同一對節點：

$$
(X_i,X_j)
$$

可能同時存在多種關係。

因此定義：

$$
\boxed{
\mathcal E_{ij}
=
\{
e_{ij}^{(\rho)}
:
\rho\in
\mathcal R_{ij}
\}.
}
$$

稱為：

$$
\boxed{
RelationBundle.
}
$$

例如：

$$
\mathcal E_{State,Citizen}
$$

可能同時包含：

- taxation；
- law；
- information；
- welfare；
- coercion；
- representation。

因此關係不是單一 scalar。

---

## 15. 「關係束」不是微分幾何 fiber bundle

這裡必須明確限制用詞。

本文的：

$$
RelationBundle
$$

只是：

> 對同一 node-pair 或 node-family 的 typed relation collection。

它不自動具備：

- base space；
- fiber；
- local trivialization；
- transition functions；

等正式 fiber-bundle 結構。

所以：

$$
\boxed{
RelationBundle
\neq
FiberBundle
}
$$

除非未來另行構造並證明。

這避免只因為「一個對象上掛很多關係」就借用微分幾何術語。

---

## 16. Multilayer Relation Vector

在有限關係類型時，

可以方便地把：

$$
\mathcal E_{ij}
$$

映射成向量：

$$
\boxed{
W_{ij}(t)
=
\begin{bmatrix}
w_{ij}^{(1)}(t)\\
w_{ij}^{(2)}(t)\\
\vdots\\
w_{ij}^{(R)}(t)
\end{bmatrix}.
}
$$

例如：

$$
W_{ij}
=
\begin{bmatrix}
w^{economic}_{ij}\\
w^{political}_{ij}\\
w^{belief}_{ij}\\
w^{coercive}_{ij}\\
w^{informational}_{ij}
\end{bmatrix}.
$$

這正是 multilayer-network 表示可以發揮作用的地方。

但：

$$
W_{ij}
$$

只描述 interaction bundle。

它不取代：

$$
Membership/Realization.
$$

---

## 17. Multilayer Graph

因此 HSNRD 的關係圖可以先表示：

$$
\boxed{
G
=
(
V,
E,
\tau_V,
\tau_E,
\alpha
).
}
$$

其中：

- $V$ ：nodes；
- $E$ ：relations；
- $\tau_V:V\rightarrow\mathcal T_V$ ；
- $\tau_E:E\rightarrow\mathcal T_E$ ；
- $\alpha$ ：attributes。

如果分 relation layers：

$$
E
=
\bigsqcup_{\rho\in\mathcal T_E}
E_\rho.
$$

則：

$$
\boxed{
G
=
\{G_\rho\}_{\rho\in\mathcal T_E}
}
$$

構成 multilayer typed graph。

---

## 18. Hyperedge 何時需要？

有些高階關係不是 pairwise。

例如：

> 三個機構共同授權一個新機構。

這更自然表示為：

$$
e:
\{A,B,C\}
\rightarrow
D.
$$

或：

$$
e\subseteq
\mathcal P(V).
$$

因此 HSNRD 不應限制：

$$
arity(e)=2.
$$

更一般地：

$$
\boxed{
Hyperrelation
}
$$

應被允許。

但如果 pairwise graph 足以表達研究問題，就不需要強行 hypergraph 化。

---

## 19. 自環：合法

關係圖中允許：

$$
\boxed{
X
\xrightarrow{\rho}
X.
}
$$

例如：

- institution monitors itself；
- company funds itself from retained earnings；
- bureaucracy audits internal process；
- self-reference。

這叫：

$$
\boxed{
GraphSelfLoop.
}
$$

在中文正式圖論語境可稱：

**自環**。

它完全合法。

---

## 20. 關係循環：也合法

同樣：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
A
$$

也沒有集合論問題。

它只是：

$$
\boxed{
RelationCycle.
}
$$

例如：

$$
Citizen
\rightarrow
Legislature
\rightarrow
Bureaucracy
\rightarrow
Citizen.
$$

這可能形成 feedback loop。

所以：

$$
\boxed{
GraphCycle
\neq
SetTheoreticCircularity.
}
$$

---

## 21. 但 $X\in X$ 預設不允許

HSNRD 預設使用 well-founded membership semantics。

因此不預設：

$$
\boxed{
X\in X.
}
$$

也不預設：

$$
A\in B,
\quad
B\in A.
$$

也就是：

$$
MembershipGraph
$$

應保持 well-founded。

這和：

$$
RelationshipGraph
$$

可以有 loop，

完全不衝突。

---

## 22. 為什麼必須做這個區分？

假設國家：

$$
State
$$

有一個 self-referential policy edge：

$$
State
\xrightarrow{SelfModel}
State.
$$

它表示：

> 國家模型以國家自身作為決策對象。

這不代表：

$$
State\in State.
$$

前者是：

$$
\boxed{
relation.
}
$$

後者是：

$$
\boxed{
membership.
}
$$

若混淆，HSNRD 很快就會把 graph feedback 誤當成集合論自包含。

---

## 23. 若未來真的需要 $X\in X$

Aczel 的 Anti-Foundation Axiom 提供一條正式路線。

在 AFA 類非良基集合論中，accessible pointed directed graphs 可以對應到非良基集合，包含例如：

$$
x=\{x\}
$$

這種 Quine atom。

因此如果未來 HSNRD 真正需要：

$$
\boxed{
MembershipSelfReference
}
$$

必須明確聲明切換 foundations：

$$
ZF/Foundation
\rightarrow
NonWellFounded/AFA.
$$

不能只因為 graph 有自環就宣稱：

$$
X\in X.
$$

---

## 24. Type 與 Order 是兩個正交軸

因此一個 node 至少具有：

$$
\boxed{
(k,\tau).
}
$$

其中：

$$
k
$$

是階數，

$$
\tau
$$

是類型。

可能：

$$
X^{(2,Family)}
$$

與：

$$
X^{(2,Corporation)}
$$

同階不同型。

也可能：

$$
X^{(2,Organization)}
$$

與：

$$
X^{(3,Organization)}
$$

同型但階數不同，

如果模型允許 nested organizations。

所以：

$$
\boxed{
Order
\perp
Type
}
$$

在概念上應分開。

---

## 25. Type 決定哪些關係有本體意義

家庭的存在可能依賴：

- kinship；
- care；
- co-residence；
- legal status。

公司的存在可能依賴：

- ownership；
- contract；
- governance；
- capital；
- employment。

因此同一 generic social matrix：

$$
W^{social}
$$

通常不夠。

應定義：

$$
\boxed{
R_\tau
\subseteq
\mathcal T_E
}
$$

表示 type $\tau$ 的 existence-relevant relation set。

然後：

$$
\boxed{
E_\tau(X)
=
\Phi_\tau
\left(
\{W^{(\rho)}\}_{\rho\in R_\tau},
P_X,
M_X,
B_X,
\ldots
\right).
}
$$

所以：

$$
\boxed{
ExistenceCondition
=
TypeDependent.
}
$$

---

## 26. 成員多，不代表高階節點一定形成

若：

$$
|M|\gg1,
$$

不能推出：

$$
\exists X^{(k+1)}.
$$

一百個陌生人站在車站，

未必形成具有持續邊界、記憶、規則與身份的高階 agent。

因此：

$$
\boxed{
Aggregation
\not\Rightarrow
Emergence.
}
$$

高階節點的生成至少可能需要：

$$
Closure,
Persistence,
Memory,
Boundary.
$$

若涉及 agency，還需要：

$$
Preference,
Decision,
Action,
Feedback.
$$

---

## 27. Existence 與 Agency 仍須分開

定義：

$$
\boxed{
E_\tau(X)\in[0,1]
}
$$

為 existence strength。

另定義：

$$
\boxed{
A_\tau(X)\in[0,1]
}
$$

為 agency degree。

因此：

$$
E(X)\gg0,
\quad
A(X)\approx0
$$

完全合法。

例如文明。

也允許：

$$
E(X)\gg0,
\quad
A(X)\gg0
$$

例如成熟公司或國家機構。

所以 HSNRD node schema 不得把：

$$
Existence
$$

與：

$$
Agency
$$

綁成同一 scalar。

---

## 28. Incidence Aggregation

在有限維近似中，

若底層關係矩陣為：

$$
W\in\mathbb R^{n\times n},
$$

高階 incidence / aggregation matrix：

$$
P\in\mathbb R^{m\times n},
$$

則最簡單高階關係可寫：

$$
\boxed{
\bar W
=
PWP^\top.
}
$$

但這只是一種 linear aggregation。

它隱含：

- 加總型投影；
- 固定 membership；
- 線性 relation combination。

因此：

$$
\bar W=PWP^\top
$$

應被視為 baseline，

而不是 HSNRD 的普遍定義。

---

## 29. 非線性聚合

更一般地：

$$
\boxed{
\bar W_{AB}^{(\rho)}
=
\mathcal A_\rho
\left(
\{
w_{ij}^{(\rho)}
:
i\in A,j\in B
\}
\right).
}
$$

其中：

$$
\mathcal A_\rho
$$

可以依 relation type 改變。

例如：

- economic flow：sum；
- trust：mean / nonlinear；
- veto：max；
- coercion：threshold；
- information：entropy / capacity。

因此：

$$
\boxed{
AggregationRule
=
RelationTypeDependent.
}
$$

---

## 30. 不要把 Category Theory 當節點本體論

HSNRD 可以使用 category theory，

但它的角色必須受到限制。

定義：

$$
\mathcal C_k
$$

其中：

$$
Ob(\mathcal C_k)
=
\{
X_i^{(k,\tau)}
\}.
$$

morphism：

$$
f:X\rightarrow Y
$$

可以表示：

- information transfer；
- resource transfer；
- authorization；
- aggregation；
- transformation。

若：

$$
f:A\rightarrow B,
$$

$$
g:B\rightarrow C,
$$

則：

$$
\boxed{
g\circ f:A\rightarrow C.
}
$$

範疇論提供：

$$
\boxed{
ComposableProcesses.
}
$$

但不因此定義：

> A 是什麼存在？

---

## 31. Category Theory 的合法角色

Applied category theory 對 open systems 的價值就在：

> 系統可以被當成 morphisms，透過共同接口組合，並用 functor 將結構模型送到 dynamical behavior。

Baez、Pollard 等人的 compositional open-system 工作就是明確先建：

$$
NetworkCategory
$$

再建立：

$$
Functor
\rightarrow
DynamicalSystem.
$$

因此 HSNRD 可借用同一思想：

$$
\boxed{
Structure
\rightarrow
ComposableMorphism
\rightarrow
Dynamics.
}
$$

但不能倒過來說：

> 因為可以寫成 category，所以高階存在的 ontology 已被解決。

---

## 32. Cross-Level Morphism

若存在跨階映射：

$$
\boxed{
F_k:
\mathcal C_k
\rightarrow
\mathcal C_{k+1},
}
$$

可以表示：

- aggregation；
- institutionalization；
- coarse-graining；
- role lifting。

但：

$$
F_k
$$

不必 faithful。

可能：

$$
f\neq g
$$

但：

$$
\boxed{
F_k(f)=F_k(g).
}
$$

也就是不同低階歷史在高階被壓成相同 morphism。

這將在下一篇直接轉成：

$$
\boxed{
ProjectionInformationLoss.
}
$$

---

## 33. Typed Graph Transformation 的接口

Ehrig 等人的 algebraic graph transformation 對 typed attributed graphs 提供成熟的 DPO／adhesive-category 基礎。

HSNRD 後續因此可以把：

$$
G
$$

視為 typed attributed graph，

而 rewrite rule：

$$
\rho
$$

則要求：

- node type legality；
- edge type legality；
- gluing conditions；
- attribute constraints。

這使：

$$
Birth,
Death,
Retype
$$

等操作可以在正式 graph-rewrite semantics 中處理。

但：

$$
Merge,
Split
$$

未必都是簡單 DPO。

這留到 HSNRD III 再處理。

---

## 34. 本篇的靜態 HSNRD Object

綜合以上，HSNRD 靜態世界可暫表示為：

$$
\boxed{
\mathfrak H
=
(
\mathcal L,
\mathcal T_V,
\mathcal T_E,
V,
E,
P,
\tau_V,
\tau_E,
\Sigma,
\mathcal B
).
}
$$

其中：

- $\mathcal L$ ：existence ladder；
- $\mathcal T_V$ ：node types；
- $\mathcal T_E$ ：relation types；
- $V$ ：nodes；
- $E$ ：typed relations；
- $P$ ：incidence / realization；
- $\tau_V$ ：node typing；
- $\tau_E$ ：edge typing；
- $\Sigma$ ：type schemas；
- $\mathcal B$ ：realization bases。

這是：

$$
\boxed{
StaticHSNRDState.
}
$$

下一階段才加入：

$$
Projection,
Information,
Dynamics,
Rewrite.
$$

---

## 35. 數學方法論角色分工

現在可以正式寫出：

### Set / Incidence

回答：

> 什麼構成什麼？

### Type

回答：

> 這是什麼類型，哪些關係／轉換合法？

### Multilayer Graph

回答：

> 各種關係如何方向性耦合？

### Hypergraph

回答：

> 多元關係是否需要高於 pairwise arity？

### Category Theory

回答：

> 哪些 process / morphism 可以合法組合？

### Graph Transformation

回答：

> 結構如何被合法改寫？

因此：

$$
\boxed{
Set
\rightarrow
TypedRelation
\rightarrow
Graph
\rightarrow
ComposableMorphism
\rightarrow
Rewrite
}
$$

而不是把所有數學語言疊在一起當作「更高級」。

---

## 36. HSNRD I 的合法性公理

本文建議將以下條件視為 HSNRD I 的建模公理。

### Axiom H1 — Order–Type Separation

$$
\boxed{
Order(X)
\neq
Type(X).
}
$$

### Axiom H2 — Constitution–Interaction Separation

$$
\boxed{
MemberOf/Realizes
\neq
InteractsWith.
}
$$

### Axiom H3 — Type Legality

每一 relation 必須滿足：

$$
\boxed{
(\tau_s,\rho,\tau_t)
\in
\Sigma_E.
}
$$

### Axiom H4 — Well-Founded Membership Default

$$
\boxed{
X\notin X
}
$$

作為預設 membership semantics。

### Axiom H5 — Graph Cycles Permitted

$$
\boxed{
X\xrightarrow{\rho}X
}
$$

及 relation cycles 合法。

### Axiom H6 — No Bundle Overclaim

$$
\boxed{
RelationBundle
\neq
FiberBundle
}
$$

除非另有正式結構。

### Axiom H7 — Existence–Agency Separation

$$
\boxed{
E(X)
\neq
A(X).
}
$$

### Axiom H8 — Type-Dependent Emergence

$$
\boxed{
E_\tau
=
\Phi_\tau(
RelevantRelations_\tau,\ldots
).
}
$$

---

## 37. 一個最小例子

考慮：

$$
p_1,p_2,p_3,p_4
\in
\mathcal L_1
$$

為四個 Person。

建立：

$$
F
=
X_1^{(2,Family)}
$$

其中：

$$
M(F)
=
\{p_1,p_2,p_3\}.
$$

另外：

$$
C
=
X_2^{(2,Corporation)}
$$

其中：

$$
M(C)
=
\{p_2,p_4\}.
$$

因此：

$$
p_2
$$

可以同時 realization 多個高階節點。

在 interaction graph 中：

$$
F
\xrightarrow{economic}
C
$$

同時：

$$
C
\xrightarrow{employment}
p_2.
$$

又可以：

$$
C
\xrightarrow{selfAudit}
C.
$$

最後一條是：

$$
GraphSelfLoop.
$$

但沒有：

$$
C\in C.
$$

所以模型完全保持 well-founded membership。

---

## 38. 同一個人可以屬於多個高階集合

HSNRD 不要求 partition：

$$
M(X_a)\cap M(X_b)=\varnothing.
$$

反而社會系統的正常情況是 overlap：

$$
\boxed{
M(X_a)\cap M(X_b)\neq\varnothing.
}
$$

一個人可以同時是：

- 家庭成員；
- 公司員工；
- 國家公民；
- 社群成員。

所以高階集合階梯不是樹。

更像：

$$
\boxed{
OverlappingConstitutiveHypergraph.
}
$$

但 membership 仍可以保持 well-founded。

---

## 39. 階梯也不是固定深度

不同區域可以有不同：

$$
k_{max}.
$$

例如某局部模型只需要：

$$
Person
\rightarrow
Family
\rightarrow
State.
$$

另一模型需要：

$$
Person
\rightarrow
Team
\rightarrow
Firm
\rightarrow
Industry
\rightarrow
State
\rightarrow
Civilization.
$$

所以：

$$
\boxed{
HSNRD
}
$$

不預設宇宙唯一的「正確七層」。

階梯是：

$$
\boxed{
ProblemRelativeOntology.
}
$$

這與前一篇：

$$
Autonomy(S;\mathcal Q)
$$

的問題相對原則一致。

---

## 40. 第一部概念如何映射進本篇

前六篇的：

$$
HigherOrderExistence
$$

在本篇對應：

$$
X_i^{(k,\tau)}
+
\mathcal B_X
+
P.
$$

群體欲求來源：

$$
W_A,W_R,W_I,W_M
$$

後續將成為 node attributes / operators。

Dependent Autonomy：

$$
\mathbf A_S
$$

後續依賴 projection robustness 與 dynamical operators。

Leviathan Reversal：

$$
D_P,S_D,E_L,R_D
$$

後續依賴 rewrite graph 與 reachability。

所以本篇不是新的獨立理論。

它是第一部語義的：

$$
\boxed{
MathematicalInterfaceLayer.
}
$$

---

## 41. 結論

HSNRD 的數學起點不應是：

> 把所有東西畫成一張很大的圖。

更嚴格的起點是：

$$
\boxed{
HierarchicalExistence
+
TypedConstitution
+
TypedInteraction.
}
$$

高階集合以：

$$
X_i^{(k,\tau)}
$$

表示。

它具有：

$$
Member/RealizationStructure
$$

但 constitution 與 ordinary interaction 分開。

關係以：

$$
\mathcal E_{ij}
$$

封裝成 relation bundle，

再映射至 multilayer typed graph。

關係圖可以：

$$
SelfLoop,
Cycle.
$$

但 membership 預設 well-founded。

因此：

$$
\boxed{
GraphSelfReference
\neq
SetMembershipSelfReference.
}
$$

這讓 HSNRD 可以安全保留 feedback 與 self-model，而不必無意間跨入非良基集合論。

最終，本文建立：

$$
\boxed{
Set/Incidence
\rightarrow
Type
\rightarrow
RelationBundle
\rightarrow
MultilayerGraph
\rightarrow
ComposableMorphism.
}
$$

這只是靜態骨架。

下一篇將處理真正困難的第二步：

> **低階世界如何投影成高階世界，而投影過程究竟丟掉多少資訊？**

也就是：

# **HSNRD II：投影、資訊失真與高階代理**

---

## 參考文獻

Aczel, P. (1988). *Non-Well-Founded Sets*. CSLI Lecture Notes 14.

Baez, J. C., & Pollard, B. S. (2017). “A Compositional Framework for Reaction Networks.” *Reviews in Mathematical Physics*, 29(9).

Baez, J. C., Fong, B., & Pollard, B. S. (2016). “A Compositional Framework for Markov Processes.” *Journal of Mathematical Physics*, 57.

Ehrig, H., Ehrig, K., Prange, U., & Taentzer, G. (2006). *Fundamentals of Algebraic Graph Transformation*. Springer.

Ehrig, H., Prange, U., & Taentzer, G. (2006). “Fundamental Theory for Typed Attributed Graph Transformation.” *Fundamenta Informaticae*, 74.

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). “Multilayer Networks.” *Journal of Complex Networks*, 2(3), 203–271.

Lack, S., & Sobociński, P. (2005). “Adhesive and Quasiadhesive Categories.” *RAIRO - Theoretical Informatics and Applications*, 39(3), 511–545.

Behr, N., & Sobociński, P. (2020). “Rule Algebras for Adhesive Categories.” *Logical Methods in Computer Science*.

---

## 本篇核心命題表

| 編號 | 命題 |
|---|---|
| H1 | $Order(X)\neq Type(X)$ |
| H2 | $Constitution\neq Interaction$ |
| H3 | $MemberOf\neq Realizes$ in general |
| H4 | $SameOrder\not\Rightarrow SameType$ |
| H5 | $Aggregation\not\Rightarrow Emergence$ |
| H6 | $RelationBundle\neq FiberBundle$ |
| H7 | $GraphSelfLoop\neq MembershipSelfReference$ |
| H8 | $GraphCycle\neq SetTheoreticCircularity$ |
| H9 | $E(X)\neq A(X)$ |
| H10 | $ExistenceCondition$ is type-dependent |
| H11 | $AdaptiveRelationGraph$ can coexist with well-founded membership |
| H12 | HSNRD ladder is problem-relative, not a ZF rank hierarchy |

---

**系列：高階集合、欲求與 Leviathan / HSNRD 完整数學方法論**  
**第二部：HSNRD 完整数學方法論**  
**篇次：07 / 10**
