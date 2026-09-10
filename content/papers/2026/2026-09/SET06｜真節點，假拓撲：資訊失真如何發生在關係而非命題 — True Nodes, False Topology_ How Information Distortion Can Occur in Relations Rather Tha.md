# SET06｜真節點，假拓撲：資訊失真如何發生在關係而非命題
## True Nodes, False Topology: How Information Distortion Can Occur in Relations Rather Than Propositions

**定位：** Selective Truth and Epistemic Topology / Foundation Paper 06 / Relation-Level Distortion  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Epistemology / Causal Inference / Narrative Structure / Graph Representation / Relation Verification / Path Compression / Misinformation

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不針對任何特定人物、政黨、宗教、哲學學派、科學學派、媒體、企業或 AI 系統。本文研究的是一般性的 relation-level distortion：**即使敘事中的 factual nodes 全部為真，整體世界表徵仍可能因 fabricated edge、edge retyping、direction reversal、path compression、mediator omission、confounder erasure、branch pruning 或 narrative adjacency 而失真。**

本文承接 SET05 的：

$$
\boxed{
\text{A worldview is not exhausted by its node set}
}
$$

以及：

$$
\boxed{
\text{different arrow types owe different certification burdens}
}
$$

SET06 再提出：

$$
\boxed{
\text{Node Truth}
\not\Rightarrow
\text{Topological Truth}
}
$$

與：

$$
\boxed{
\text{A narrative may preserve every factual node while corrupting the relations among them}
}
$$

---

# 摘要

傳統 fact-checking 往往以 proposition 為主要單位：某事件是否發生、某數字是否正確、某來源是否可靠。然而，大量推理與敘事的決定性內容並不位於節點，而位於節點之間的關係。兩個事件都可以真實發生，但「前者導致後者」仍可能是錯的；兩個研究結果都可以真實存在，但「第二個證明第一個理論」仍可能是錯的；一組主流媒體文章都可以是真實可靠的，卻仍可能被重新拼接進一個誤導性 narrative。

2024 年 McGowan、Gerke 與 Barrett 建立一組 causal quartet：四個資料集具有相同的統計摘要與視覺化，但由 collider、confounder、mediator 與 M-bias 等不同 causal mechanisms 生成，因此真實 causal effect 不同。此結果提供一個極強的結構性示範：

$$
\boxed{
\text{same observable nodes and summaries}
\not\Rightarrow
\text{same causal topology}
}
$$

2025 年 *Nature Human Behaviour* 的 Goel、Green、Lazer 與 Resnik 更從公共資訊生態證明另一側問題：可靠主流來源中的 factually true information 可以被使用者重新利用，以增加 potentially misleading narratives 的可信度與傳播。這說明 source reliability 與 node truth 不能自動保證 narrative topology 的可靠性。

本文提出 **Topological Distortion Framework（TDF）**。令一個 epistemic narrative 表示為：

$$
\mathcal N
=
(V,E,\tau,\omega,\kappa)
$$

其中：

- $V$ 為 factual / conceptual nodes；
- $E$ 為 relations；
- $\tau$ 為 relation-type assignment；
- $\omega$ 為 relation confidence / evidential weight；
- $\kappa$ 為 path-compression rule。

若：

$$
q(v)=1
$$

對所有 $v\in V$ 都成立，但至少存在一支 edge：

$$
e\in E
$$

在 relation type、direction、mechanism、branch structure 或 compression semantics 上未被支持，則 narrative 可以是 **node-true but topologically distorted**。

本文系統化八類失真：

1. Edge Fabrication；
2. Edge Retyping；
3. Direction Reversal；
4. Adjacency Promotion；
5. Mediator Collapse；
6. Confounder Erasure；
7. Branch Pruning；
8. Illicit Path Compression。

本文並區分合法與非法壓縮。宏觀箭頭：

$$
A
\xrightarrow{\mathrm{macro}}
B
$$

可以是：

$$
A
\to
x_1
\to
x_2
\to
\cdots
\to
B
$$

的合法 projection，只要在指定問題 $Q$ 、解析度 $\rho$ 與容許 gap $\epsilon$ 下，展開後不改變該 arrow 的語意類型與決策相關結論。若省略中介狀態會改變 causal interpretation、branch probability、responsibility、intervention choice 或 falsification condition，則 compression debt 未清。

本文建立 **Node Truth Rate（NTR）**、**Typed-Edge Validity（TEV）**、**Mechanism Coverage（MC）**、**Branch Coverage（BC）**、**Compression Debt（CD）**、**Directionality Integrity（DI）** 與 **Topological Integrity Profile（TIP）**，並提出 **Topological Relation Audit Protocol（TRAP）**。

核心結論：

$$
\boxed{
\text{Fact checking is necessary but relation checking is independently necessary}
}
$$

真正的高階資訊驗證，不只問：

> 這些節點是真的嗎？

還要問：

> **這些節點憑什麼以這種方式連在一起？**

---

# 0　最小例子：每一句都是真的，結論仍然可以是假的

假設：

$$
A=\text{true}
$$

代表事件 A 發生。

$$
B=\text{true}
$$

代表事件 B 發生。

再給：

$$
t(A)<t(B).
$$

即 A 先於 B。

如果 narrative 寫成：

$$
A
\xrightarrow{\text{causes}}
B,
$$

那麼新增的不是一個 factual node。

新增的是：

$$
e=(A,\text{causes},B).
$$

所以即使：

$$
q(A)=q(B)=1,
$$

仍然可能：

$$
q(e)=0.
$$

這是 SET06 的最小結構：

$$
\boxed{
\text{true endpoints can be connected by a false relation}
}
$$

---

# 1　從 proposition verification 到 topology verification

令 narrative：

$$
\mathcal N=(V,E).
$$

傳統 fact-checking 近似檢查：

$$
q_V:V\to\{0,1\}.
$$

如果：

$$
q_V(v)=1
$$

對所有 node 成立，可能得到：

> 本文沒有 factual error。

但完整 narrative 還需要：

$$
q_E:E\to\{0,1,\mathrm{underdetermined}\}.
$$

更精確地，typed edge：

$$
e=(u,t,v)
$$

需要 relation-specific audit。

因此：

$$
\boxed{
q_V(V)=1
\not\Rightarrow
q_E(E)=1
}
$$

---

# 2　2024 Causal Quartet：相同資料表面，不同 causal mechanism

McGowan、Gerke 與 Barrett 的 *Causal Inference Is Not Just a Statistics Problem* 建立四組刻意設計的資料。

四個 dataset：

- summary statistics 相同；
- visualization 相同；

但 data-generating mechanisms 分別包含：

- collider；
- confounder；
- mediator；
- M-bias。

結果是：

$$
\text{observational appearance}
$$

相同，

但：

$$
\text{true causal effect}
$$

不同。

可表示為：

$$
O_1=O_2=O_3=O_4
$$

在指定 observation summary 下成立，

卻：

$$
G_1\neq G_2\neq G_3\neq G_4.
$$

這正是 SET06 所需的硬示範：

$$
\boxed{
\text{observable equivalence}
\not\Rightarrow
\text{causal-topology equivalence}
}
$$

---

# 3　Causal DAG 是假設圖，不是因果真理圖

Bulbulia 2024 對 causal diagrams 的方法論說明強調：causal inference 需要 counterfactual contrast、明確問題、識別假設與系統性 workflow。Causal DAG 可以幫助研究者檢查：

- reverse causation；
- confounding；
- mediator；
- collider；
- timing；
- adjustment strategy。

但 graph 可以被誤用。

所以：

$$
\boxed{
\text{drawing an arrow}
\neq
\text{identifying a causal effect}
}
$$

圖是：

$$
\text{assumption representation}
$$

而不是：

$$
\text{causal certificate}.
$$

---

# 4　八類 Topological Distortion

## 4.1 Edge Fabrication

nodes 真實：

$$
A=\text{true},
\quad
B=\text{true},
$$

但無充分 relation evidence 卻加入：

$$
A
\xrightarrow{t}
B.
$$

---

## 4.2 Edge Retyping

原本只有：

$$
A
\xrightarrow{\text{correlates}}
B,
$$

卻重寫為：

$$
A
\xrightarrow{\text{causes}}
B.
$$

或：

$$
E
\xrightarrow{\text{supports}}
H
$$

被重寫為：

$$
E
\xrightarrow{\text{proves}}
H.
$$

---

## 4.3 Direction Reversal

真實機制：

$$
B
\xrightarrow{\text{causes}}
A,
$$

敘事卻是：

$$
A
\xrightarrow{\text{causes}}
B.
$$

節點沒有任何 falsity。

方向本身錯。

---

## 4.4 Adjacency Promotion

A 與 B 在時間或文字上鄰接：

$$
A
\xrightarrow{\text{precedes}}
B.
$$

卻因 adjacency 被升格為：

$$
A
\xrightarrow{\text{explains}}
B
$$

甚至：

$$
A
\xrightarrow{\text{causes}}
B.
$$

---

## 4.5 Mediator Collapse

真實路徑：

$$
A
\to
M
\to
B.
$$

敘事壓縮：

$$
A
\to
B.
$$

這有時完全合法。

但若 $M$ 對：

- mechanism；
- intervention；
- responsibility；
- boundary condition；

是必要的，直接刪掉 $M$ 就改變了 arrow semantics。

---

## 4.6 Confounder Erasure

真實結構：

$$
C
\to
A,
$$

$$
C
\to
B.
$$

敘事只保留：

$$
A
\leftrightarrow
B,
$$

再推成：

$$
A
\to
B.
$$

這是 topology-level omission。

---

## 4.7 Branch Pruning

完整可能世界：

$$
A
\to
\{B,C,D\}.
$$

敘事只畫：

$$
A
\to
B.
$$

如果原句只是：

> B 是一個可能結果，

可以合法。

若改成：

> 下一步就是 B，

就把：

$$
\text{possible successor}
$$

升格成：

$$
\text{unique successor}.
$$

---

## 4.8 Illicit Path Compression

真實可達路徑：

$$
A
\to
x_1
\to
x_2
\to
x_3
\to
B.
$$

敘事：

$$
A
\to
B.
$$

如果 macro-arrow 沒有標記 compression scope，就可能把：

$$
\text{eventually reachable}
$$

誤讀成：

$$
\text{immediate transition}.
$$

---

# 5　Narrative 為什麼天然具有 causal topology

Chen 與 Bornstein 2024 的 review 指出，narratives 的關鍵結構之一就是跨時間的 causal connections，而 causal structure 會影響 narrative comprehension 與 episodic memory。

因此 narrative 不是：

$$
\text{unordered bag of true facts}.
$$

而是近似：

$$
\text{ordered and causally structured representation}.
$$

這表示：

$$
\boxed{
\text{changing the relations can change what the same facts mean and what is remembered}
}
$$

而不必改任何 node。

---

# 6　2025 Narrative and Causality：故事中的「原因」本身有多種形式

Álvarez Arias 2025 對 narrative causality 的分析指出，historical narrative 會透過不同形式把 events 連起來，包括：

- regularity-based causal sequence；
- contributory causation；
- remote causation；
- retrospective relation；
- influence。

這提供一個重要限制。

歷史中的：

$$
A
\xrightarrow{\text{influences}}
B
$$

不必滿足自然科學中那種：

$$
A
\xrightarrow{\text{sufficient-cause}}
B.
$$

所以 SET06 不能把所有「弱因果語言」都當錯誤。

真正問題是：

$$
\boxed{
\text{relation type must match the evidential burden actually available}
}
$$

---

# 7　可靠來源也可以被拼進誤導 narrative

Goel、Green、Lazer 與 Resnik 2025 在 *Nature Human Behaviour* 研究 mainstream news 與 misinformation co-sharing。

研究的關鍵不是：

> 主流新聞本身都是假的。

而是：

> 可靠來源中的 factually true information 可以被重新利用，以增加 potentially misleading narratives 的 credibility 與 reach。

這與 SET01 的 selective truth 直接接軌，但 SET06 的焦點更深：

$$
\text{reliable source nodes}
$$

被抽出後重新嵌入：

$$
G_{\mathrm{misleading}}.
$$

因此：

$$
\boxed{
\text{source truth can be preserved while narrative topology changes}
}
$$

---

# 8　Topological Corruption Operator

定義原始較完整 graph：

$$
G=(V,E,\tau,\omega).
$$

定義 topology corruption / transformation operator：

$$
\mathcal C_G.
$$

若：

$$
\mathcal C_G
:
(V,E,\tau,\omega)
\mapsto
(V,E',\tau',\omega'),
$$

且：

$$
V'=V,
$$

但：

$$
(E',\tau',\omega')
\neq
(E,\tau,\omega),
$$

則這是一個 **node-preserving topology transformation**。

注意：

$$
\mathcal C_G
$$

不必然是惡意。

科學抽象、教學簡化、工程設計都會轉換 topology。

因此還要再問：

$$
\text{is the transformation semantics-preserving for the target question?}
$$

---

# 9　合法壓縮與非法壓縮

設完整 path：

$$
P_{AB}
=
(A,x_1,x_2,\ldots,x_n,B).
$$

macro representation：

$$
A
\xrightarrow{\mathrm{macro}}
B.
$$

壓縮合法與否不能脫離問題。

令：

- $Q$：當前問題；
- $\rho$：解析度；
- $\epsilon$：可接受 unresolved gap；
- $\sigma$：arrow semantic type。

定義概念條件：

$$
\operatorname{CompressValid}
(P_{AB}\mid Q,\rho,\epsilon,\sigma)=1
$$

若展開 path 後：

1. 不改變 $\sigma$ ；
2. 不改變 $Q$ 的核心判定；
3. 不隱藏 decision-relevant branch；
4. 不隱藏會逆轉 intervention 的 mediator / confounder；
5. residual gap 不超過 $\epsilon$。

---

# 10　一步不是一步：Reachable 不等於 Adjacent

令：

$$
A
\xRightarrow{*}
B
$$

表示可達。

而：

$$
A
\to
B
$$

表示 immediate transition。

則：

$$
\boxed{
A\xRightarrow{*}B
\not\Rightarrow
A\to B
}
$$

如果存在：

$$
Z
$$

使：

$$
A\xRightarrow{*}Z
$$

且：

$$
Z\xRightarrow{*}B,
$$

那：

$$
A\to B
$$

至少需要說明它是 macro-arrow，不能自動稱「下一步」。

這與 FF01 的 path-compression / possible-worlds 問題形成直接接口。

---

# 11　「下一步」必須相對於解析度

如果要求世界中：

$$
\text{absolutely no intermediate physical state},
$$

幾乎所有宏觀 transition 都失去 immediate-next status。

所以合理形式是：

$$
\boxed{
\text{next relative to }(Q,\rho)
}
$$

例如：

$$
A
\xrightarrow{\mathrm{next}\mid Q,\rho}
B.
$$

表示：

> 在指定問題與解析度下，不存在另一個需要獨立表示、且足以改變當前判斷的中介 state class。

這不是 metaphysical immediacy。

而是：

$$
\text{resolution-relative adjacency}.
$$

---

# 12　Compression Debt

若 macro-arrow：

$$
A
\xrightarrow{\mathrm{macro}}
B
$$

省略 path：

$$
P_{AB},
$$

定義概念性 **Compression Debt（CD）**：

$$
\mathrm{CD}(A,B)
=
D_Q
\left(
P_{AB},
A\xrightarrow{\mathrm{macro}}B
\right),
$$

其中 $D_Q$ 衡量在問題 $Q$ 下壓縮前後的 decision-relevant information loss。

若：

$$
\mathrm{CD}\approx0,
$$

壓縮近似語意保持。

若：

$$
\mathrm{CD}\gg0,
$$

macro-arrow 會讓 receiver 誤判 mechanism、branch 或 causal responsibility。

---

# 13　Node Truth Rate

定義：

$$
\mathrm{NTR}
=
\frac{
|\{v\in V:q(v)=1\}|
}{
|V|
}.
$$

一個 narrative 可以：

$$
\mathrm{NTR}=1
$$

仍然嚴重失真。

因此 NTR 是必要但不充分指標。

---

# 14　Typed-Edge Validity

令每支 edge：

$$
e=(u,t,v).
$$

若 relation-specific evidence 支持其：

- existence；
- direction；
- type；

則：

$$
q_T(e)=1.
$$

定義：

$$
\mathrm{TEV}
=
\frac{
\sum_{e\in E}w(e)q_T(e)
}{
\sum_{e\in E}w(e)+\epsilon
}.
$$

其中 $w(e)$ 可依 decision relevance 加權。

所以：

$$
\mathrm{NTR}\approx1,
\quad
\mathrm{TEV}\ll1
$$

正是：

$$
\boxed{
\text{true nodes, false topology}
}
$$

---

# 15　Mechanism Coverage

對宣稱 causal / transition arrow 的集合：

$$
E_M,
$$

定義每支 edge 是否具有足以回答當前問題的 mechanism specification。

概念性：

$$
\mathrm{MC}
=
\frac{
\sum_{e\in E_M}w(e)m(e)
}{
\sum_{e\in E_M}w(e)+\epsilon
},
$$

其中：

$$
m(e)\in[0,1].
$$

低 MC 不證明 causal relation 為假。

只代表：

$$
\boxed{
\text{mechanism debt remains open}
}
$$

---

# 16　Branch Coverage

完整 candidate successor / explanation branches：

$$
\mathcal B_A.
$$

narrative 顯示：

$$
\hat{\mathcal B}_A.
$$

定義：

$$
\mathrm{BC}
=
\frac{
\sum_{b\in\hat{\mathcal B}_A}w(b)
}{
\sum_{b\in\mathcal B_A}w(b)+\epsilon
}.
$$

若只保留最符合敘事的一支 branch：

$$
\mathrm{BC}\ll1.
$$

這與 SET01 的 information sampling 同構，但作用對象從 fact pool 轉成 path pool。

---

# 17　Directionality Integrity

令有方向關係集合：

$$
E_D.
$$

定義：

$$
\mathrm{DI}
=
\frac{
|\{e\in E_D:\operatorname{dir}(e)=\operatorname{dir}^*(e)\}|
}{
|E_D|
}.
$$

其中 $\operatorname{dir}^*$ 來自目前最佳可得的 reference / identified structure。

若 reference 本身不確定，DI 應標 uncertainty，而不是硬評分。

---

# 18　Topological Integrity Profile

本文不建議把所有東西壓成一個總分。

因此提出 profile：

$$
\mathrm{TIP}
=
\langle
\mathrm{NTR},
\mathrm{TEV},
\mathrm{MC},
\mathrm{BC},
\mathrm{CD},
\mathrm{DI}
\rangle.
$$

一個 narrative 可能：

$$
\mathrm{NTR}\uparrow,
$$

$$
\mathrm{TEV}\downarrow,
$$

$$
\mathrm{BC}\downarrow.
$$

這種結構比「真假二分」更能表達：

> 每個 fact 都能 fact-check 通過，但整體故事仍有問題。

---

# 19　Confounder Erasure：刪掉一個 node，可能創造一支假箭頭

真實結構：

$$
C
\to
A,
$$

$$
C
\to
B.
$$

若 narrative 省略 $C$，receiver 只看到：

$$
A,
\quad
B.
$$

加上 association：

$$
A\sim B.
$$

便容易形成：

$$
A\to B.
$$

這說明 node omission 與 edge fabrication 可以聯動。

所以：

$$
\boxed{
\text{missing nodes can induce false edges among remaining true nodes}
}
$$

---

# 20　Collider：多放一個 node，也可能創造假關係

反過來，資訊越多也不必然越好。

若：

$$
A\to C,
$$

$$
B\to C,
$$

而分析錯誤地 conditioning on collider $C$，可能在：

$$
A
$$

與：

$$
B
$$

之間製造 non-causal association。

所以：

$$
\boxed{
\text{more variables}
\not\Rightarrow
\text{better topology}
}
$$

問題不是 node count。

而是：

$$
\text{structural role}.
$$

---

# 21　Mediator：刪除與控制都可能改變問題

若：

$$
A
\to
M
\to
Y,
$$

而研究問題是 total effect，

控制 $M$ 可能把 causal pathway 切掉。

若研究問題是 direct / mediated effect，又必須更精細區分。

Qin 2024 的 causal mediation review 特別強調 treatment-mediator、treatment-outcome、mediator-outcome confounding 與 identification assumptions。

所以：

$$
\boxed{
\text{the same node can be relevant, irrelevant, mediator, confounder, or collider depending on the causal question}
}
$$

這再次證明：

$$
\text{node identity}
$$

不足以決定：

$$
\text{topological role}.
$$

---

# 22　Topological Truth 必須問題相對化

不存在一個對所有問題都同樣完美的 graph。

因為：

$$
Q_1
$$

可能只需要：

$$
A
\xrightarrow{\mathrm{total-effect}}
Y.
$$

而：

$$
Q_2
$$

需要展開：

$$
A
\to
M_1
\to
M_2
\to
Y.
$$

所以：

$$
\boxed{
\text{topological adequacy is question-relative}
}
$$

而不是：

$$
\text{more detailed graph is always better}.
$$

---

# 23　Narrative Adjacency：文字順序本身就是隱形箭頭

自然語言常不需要明寫：

> A 導致 B。

只要排列：

> A 發生。接著 B 出現。最後 C 惡化。

receiver 就可能建立：

$$
A
\to
B
\to
C.
$$

因此 narrative order 可以形成 implicit edge。

SET06 稱：

$$
\boxed{
\text{Implicit Adjacency Edge}
}
$$

它不必出現在文字字面上，卻可能出現在 receiver 的 reconstructed graph。

---

# 24　同樣 true facts，排序也能改變 topology

給定：

$$
V=\{A,B,C,D\}.
$$

Narrative 1：

$$
A,B,C,D.
$$

Narrative 2：

$$
C,A,D,B.
$$

若 receiver 有 adjacency-to-causality prior，兩個 sequence 可能生成：

$$
\hat G_1\neq\hat G_2.
$$

所以：

$$
\boxed{
\text{ordering is an edge-selection device}
}
$$

即使所有 node content 完全相同。

---

# 25　從 misinformation 到 mis-topology

常見 misinformation 定義強調 false / misleading content。

SET06 提議再區分：

$$
\text{node misinformation}
$$

與：

$$
\text{topological misinformation}.
$$

前者改：

$$
V.
$$

後者主要改：

$$
E,
\quad
\tau,
\quad
\omega,
\quad
\kappa.
$$

Goel 等 2025 的 mainstream-news co-sharing work 顯示，真實資訊能支撐誤導 narratives，正適合被理解為：

$$
\text{truthful-node reuse under misleading narrative structure}.
$$

---

# 26　Reliable Source Laundering

若某 narrative 使用：

$$
s_1,s_2,\ldots,s_n
$$

皆為可靠來源。

receiver 可能偷渡：

$$
\text{reliable sources}
\Rightarrow
\text{reliable narrative}.
$$

但真正需要的是：

$$
\boxed{
\text{source reliability}
+
\text{relation validity}
+
\text{selection representativeness}
}
$$

三者共同成立。

所以：

$$
\boxed{
\text{reliable-node provenance does not certify cross-node inference}
}
$$

---

# 27　Path Compression 與 Future Framing

在 future / policy / technology narrative 中，最常見結構：

$$
A
\to
B
\to
C
\to
D
$$

被壓成：

$$
A
\to
D.
$$

若真正存在：

$$
B\in\{B_1,B_2,B_3\},
$$

$$
C\in\{C_1,C_2,C_3\},
$$

則 macro-arrow 可能把一棵 possible-world tree 壓成一條線。

所以：

$$
\boxed{
\text{path compression can silently erase possible worlds}
}
$$

這是 SET06 與 FF01 至 FF03 的直接橋接點。

---

# 28　合法的 Macro Arrow

不是所有：

$$
A\to D
$$

都要展開到微觀世界。

例如地圖說：

> 台北到高雄。

不需要列出每一公尺。

真正合法條件是：

$$
\operatorname{Invariant}_Q
\left(
P_{AD},
A\xrightarrow{\mathrm{macro}}D
\right)
\approx1.
$$

即對當前問題 $Q$，展開與壓縮後保留關鍵語意與決策。

所以 SET06 不是 anti-abstraction。

而是：

$$
\boxed{
\text{anti-unmarked semantic loss}
}
$$

---

# 29　Topological Relation Audit Protocol（TRAP）

## Step 1：Freeze the Nodes

列出所有 factual nodes：

$$
V.
$$

分開 fact truth 與 relation claim。

---

## Step 2：Extract Explicit and Implicit Edges

抽出：

- 「因此」；
- 「導致」；
- 「證明」；
- 「支持」；
- 「使得」；
- 「接著」；
- 排序形成的 implicit edge。

建立：

$$
E_{\mathrm{candidate}}.
$$

---

## Step 3：Type Every Relation

不接受模糊：

> 有關。

要求：

$$
\tau(e).
$$

---

## Step 4：Assign Arrow-Type Debt

對每支：

$$
e=(u,t,v)
$$

問：

> 這個 relation type 需要哪種 evidence？

---

## Step 5：Search Hidden Structure

主動搜尋：

- mediator；
- confounder；
- collider；
- reverse causation；
- omitted branch；
- alternative mechanism；
- common cause；
- temporal ambiguity。

---

## Step 6：Expand Compressed Paths

對：

$$
A\xrightarrow{\mathrm{macro}}B
$$

至少建立一條候選展開：

$$
A
\to
x_1
\to
\cdots
\to
B.
$$

若完全展不開，標：

$$
\text{open mechanism debt}.
$$

---

## Step 7：Construct Rival Topologies

在同一 node set：

$$
V
$$

上建立：

$$
G_1,G_2,\ldots,G_k.
$$

真正比較：

$$
\text{which graph survives discriminating evidence?}
$$

---

## Step 8：Counterfactual / Intervention Check

對 causal edge 問：

> 若 $A$ 不發生， $B$ 會怎樣？

> 若 intervention 改變 $A$， $B$ 是否改變？

用來區分：

$$
\text{association}
$$

與：

$$
\text{causal commitment}.
$$

---

## Step 9：Check Branch Completeness

問：

> 除了 B，A 還有什麼重要 successor？

如果存在高權重：

$$
C,D,
$$

卻被完全省略，登記 branch debt。

---

## Step 10：Report a Profile, Not a Binary Verdict

輸出：

$$
\mathrm{TIP}
=
\langle
\mathrm{NTR},
\mathrm{TEV},
\mathrm{MC},
\mathrm{BC},
\mathrm{CD},
\mathrm{DI}
\rangle.
$$

避免把：

> 每句真話

誤成：

> 整體真。

---

# 30　實驗一：Same Nodes, Different Edges

給所有 participants 完全相同的 node facts。

只改 narrative connectors：

Condition 1：

$$
A
\xrightarrow{\text{precedes}}
B.
$$

Condition 2：

$$
A
\xrightarrow{\text{causes}}
B.
$$

Condition 3：

$$
A
\xrightarrow{\text{supports}}
B.
$$

測：

- causal judgment；
- prediction；
- intervention；
- responsibility；
- confidence。

若結果不同，表示 relation type 具有獨立行為效應。

---

# 31　實驗二：Implicit Adjacency

完全不使用 causal word。

只改 facts 的順序。

測 receiver 自行重建的：

$$
\hat E.
$$

若 sequence 改變 relation inference，支持 adjacency-topology mechanism。

---

# 32　實驗三：Compression Expansion

給：

$$
A
\xrightarrow{\mathrm{macro}}
D.
$$

一組只看 macro。

另一組看：

$$
A
\to
B
\to
C
\to
D.
$$

第三組再加入 branch：

$$
B
\to
E.
$$

測：

- inevitability judgment；
- causal strength；
- forecast confidence；
- responsibility；
- perceived alternatives。

若 branch 展開大幅改變判斷，表示 macro-arrow 隱藏了 decision-relevant topology。

---

# 33　實驗四：True Mainstream Sources, Different Narrative Assembly

使用相同一組已驗證 true articles。

Group A 依來源原 context 閱讀。

Group B 依某預設 narrative 重新排序與摘錄。

控制：

$$
V_A=V_B.
$$

測：

$$
\hat G_A
$$

與：

$$
\hat G_B.
$$

如果 node accuracy 相同但 relation beliefs 明顯不同，直接支持 SET06。

---

# 34　實驗五：Causal Quartet Comprehension

使用 McGowan 等 causal quartet 類設計。

給受試者相同 summary / visualization，但不同生成機制資訊。

測：

- causal effect estimate；
- adjustment choice；
- confidence；
- graph reconstruction。

這可以測：

$$
\text{surface-data equivalence}
$$

與：

$$
\text{mechanism-sensitive causal reasoning}.
$$

---

# 35　AI Relation Hallucination Benchmark

AI benchmark 不只問：

> facts 正確嗎？

而應建立：

$$
\mathcal D
=
\{
(V,E^*,\tau^*)
\}.
$$

模型輸出：

$$
\hat E,\hat\tau.
$$

評估：

$$
\text{Node Accuracy},
$$

$$
\text{Edge Precision},
$$

$$
\text{Edge Recall},
$$

$$
\text{Type Accuracy},
$$

$$
\text{Direction Accuracy},
$$

$$
\text{Compression Debt}.
$$

模型完全可能：

$$
\text{Node Accuracy}\approx1
$$

但：

$$
\text{Edge Precision}\ll1.
$$

這就是 relation hallucination。

---

# 36　這不是要求世界永遠有唯一 topology

很多 domain 存在：

$$
G_1,
G_2,\ldots,G_k
$$

都與目前 evidence 相容。

例如 observational causal inference 本來就可能欠缺 identification。

因此 SET06 不要求 AI 或人：

> 選一張唯一真圖。

更合理的是：

$$
\boxed{
\text{represent a set of admissible rival topologies}
}
$$

並標：

$$
P(G_i\mid E)
$$

或：

$$
\text{supported / unresolved / rejected}.
$$

---

# 37　Underdetermination 不是失敗

若目前 evidence 只能得到：

$$
G\in\{G_1,G_2,G_3\},
$$

正確輸出就是：

> 尚未識別。

而不是：

$$
G=G_1
$$

只因它敘事最好看。

因此：

$$
\boxed{
\text{topological uncertainty is preferable to fabricated connectivity}
}
$$

---

# 38　什麼結果會削弱 SET06？

若以下結果穩定成立，SET06 應縮小：

1. relation-type manipulation 對下游推理幾乎無影響；
2. narrative ordering 不改變 receiver relation reconstruction；
3. node-only fact checking 已能預測幾乎全部誤導判斷；
4. graph / edge audit 不提高 misinformation detection；
5. path expansion 不改變 forecast、responsibility 或 causal judgments；
6. branch omission 對 decision 幾乎無影響；
7. reliable-source reassembly 不改變 narrative interpretation；
8. AI 的 edge errors 幾乎完全可由 node errors解釋；
9. relation typing reliability 太低，無法成為穩定研究單位；
10. topology-aware models 不比 simpler proposition models 提供更高 discriminative value。

如果如此，SET06 應降格為特定 causal / narrative domain 的方法，而不是一般 epistemic framework。

---

# 39　自反性：畫 topology 也可以製造新的假拓撲

SET06 最容易犯的錯就是：

> 因為批評別人亂連箭頭，所以自己畫一張更漂亮的 graph，便以為是真的。

這完全不成立。

Graph representation 本身可以：

- 過度離散化；
- 錯分 relation type；
- 假裝 direction 已知；
- 隱藏 latent variables；
- 強迫 hierarchy；
- 把 continuous process 切成 fake states；
- 把 epistemic relation 誤當 ontological relation。

因此本文必須接受：

$$
\boxed{
\text{graph clarity}
\neq
\text{graph truth}
}
$$

AAAP 與 TRAP 都只是 audit protocol，不是 ontology generator。

---

# 40　與 SET05 的差異

SET05 問：

$$
\boxed{
\text{Which arrows does a worldview permit?}
}
$$

SET06 問：

$$
\boxed{
\text{Which of those arrows are actually supported, omitted, retyped, compressed, or reversed?}
}
$$

SET05 是：

$$
\text{admissibility regime}.
$$

SET06 是：

$$
\text{topological integrity}.
$$

兩者合起來：

$$
\text{worldview}
=
\text{node commitments}
+
\text{arrow constitution}
+
\text{arrow validity}.
$$

---

# 41　與 SET07 的接口

如果一個 belief system 遇到任何反證都能：

- retype edge；
- 新增 auxiliary node；
- 移除 threatening branch；
- 把 causal failure 改成 influence；
- 把 prediction failure 改成 compatibility；
- 把 counterexample 改成 exception；

而整體 topology 永遠維持核心 conclusion，

則：

$$
\Phi(\mathcal B,E_{\mathrm{new}})
\approx
\mathcal B.
$$

這將進入 SET07：

$$
\boxed{
\text{Epistemic Attractors and Self-Sealing Systems}
}
$$

也就是：

> 系統可以吸收無限資訊，卻幾乎不改變自己的 topology。

---

# 42　結論

資訊失真不一定需要虛構一個節點。

一個更難辨認的世界是：

$$
q(v)=1
$$

對所有 factual nodes 都成立，

但：

$$
q(e)
$$

大量未被證成。

於是：

$$
\boxed{
\mathrm{NTR}\approx1
}
$$

卻：

$$
\boxed{
\mathrm{TEV}\ll1
}
$$

故事裡的每個人、事件、數字、來源都是真的。

問題只是：

> 他們沒有證據以那種方式彼此相連。

因此 SET06 最後留下五條原則：

$$
\boxed{
\text{True endpoints do not certify the arrow between them}
}
$$

$$
\boxed{
\text{Reliable sources do not certify the narrative assembled from them}
}
$$

$$
\boxed{
\text{Reachability is not adjacency}
}
$$

$$
\boxed{
\text{Compression is valid only when its omitted structure is irrelevant to the declared question}
}
$$

以及：

$$
\boxed{
\text{Fact checking verifies nodes; epistemic auditing must also verify topology}
}
$$

真正值得追問的，不只是：

> 這句是真的嗎？

而是：

> **從這一句到下一句，中間那支箭頭，到底是誰畫上去的？它欠的證據還清了嗎？**

---

# References

1. McGowan, L. D., Gerke, T., & Barrett, M. (2024). Causal Inference Is Not Just a Statistics Problem. *Journal of Statistics and Data Science Education*, 32(2), 150-155. https://doi.org/10.1080/26939169.2023.2276446

2. Bulbulia, J. A. (2024). Methods in Causal Inference. Part 1: Causal Diagrams and Confounding. *Evolutionary Human Sciences*, 6, e40. https://doi.org/10.1017/ehs.2024.35

3. Qin, X. (2024). An Introduction to Causal Mediation Analysis. *Asia Pacific Education Review*, 25, 703-717. https://doi.org/10.1007/s12564-024-09962-5

4. Chen, J., & Bornstein, A. M. (2024). The Causal Structure and Computational Value of Narratives. *Trends in Cognitive Sciences*, 28(8), 769-781. https://doi.org/10.1016/j.tics.2024.04.003

5. Álvarez Arias, S. (2025). Narrative and Causality. *Synthese*, 206, 190. https://doi.org/10.1007/s11229-025-05261-7

6. Goel, P., Green, J., Lazer, D., & Resnik, P. S. (2025). Using Co-Sharing to Identify Use of Mainstream News for Promoting Potentially Misleading Narratives. *Nature Human Behaviour*, 9, 1843-1860. https://doi.org/10.1038/s41562-025-02223-4

7. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

8. Hernán, M. A., & Robins, J. M. (2020). *Causal Inference: What If*. Chapman & Hall/CRC.

9. Halpern, J. Y., & Pearl, J. (2005). Causes and Explanations: A Structural-Model Approach. Part I: Causes. *British Journal for the Philosophy of Science*, 56(4), 843-887.

10. Thagard, P. (1989). Explanatory Coherence. *Behavioral and Brain Sciences*, 12(3), 435-467. https://doi.org/10.1017/S0140525X00057046

11. Salim, S., Hoque, M. N., & Mueller, K. (2024). Belief Miner: A Methodology for Discovering Causal Beliefs and Causal Illusions from General Populations. *Proceedings of the ACM on Human-Computer Interaction*, 8(CSCW1), Article 21. https://doi.org/10.1145/3637298

---

## 系列位置

**Selective Truth and Epistemic Topology**

- SET01：高明的謊言不需要假話：選擇性真實、資訊抽樣與失真世界
- SET02：聽者的不可識別問題：當客觀評估與策略性真話產生相同表面訊息
- SET03：張力控制與策略性讓步：可信度如何被工程化
- SET04：真誠的人也能產生選擇性世界：Sincere Selection Bias
- SET05：信念系統不是信念集合，而是允許箭頭的系統
- **SET06：真節點，假拓撲：資訊失真如何發生在關係而非命題**
- SET07：認識論吸引子與自我封閉：吸收無限資訊而幾乎不學習

---

*SET06 / Selective Truth and Epistemic Topology / EveMissLab / v0.1 / 2026-09-07*
