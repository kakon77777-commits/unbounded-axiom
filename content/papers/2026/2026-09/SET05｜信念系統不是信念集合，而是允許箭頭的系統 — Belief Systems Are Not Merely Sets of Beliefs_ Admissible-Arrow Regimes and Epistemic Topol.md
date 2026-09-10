# SET05｜信念系統不是信念集合，而是允許箭頭的系統
## Belief Systems Are Not Merely Sets of Beliefs: Admissible-Arrow Regimes and Epistemic Topology

**定位：** Selective Truth and Epistemic Topology / Foundation Paper 05 / Relational Belief Structure  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Formal Epistemology / Belief Revision / Argumentation / Causal Graphs / Explanatory Coherence / Belief Networks / Epistemic Topology

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不主張首次把 beliefs、arguments、causal variables 或 attitudes 表示成 graph。相關傳統至少包括 AGM belief revision、Bayesian networks、causal graphs、Dung abstract argumentation、Thagard explanatory coherence、belief network analysis 與近年的 causal-belief elicitation。

本文提出的較窄主張是：**若研究 worldview、ideology、theory framework 或長期信念系統，只記錄「agent 相信哪些命題」通常不足；還需要顯式記錄 agent 允許哪些關係箭頭進入、以什麼類型進入、獲得多少權重、在什麼條件下被撤回，以及新 evidence 如何改寫整個關係結構。**

本文承接 SET04 的：

$$
\boxed{
\text{Sincerity}
\not\Rightarrow
\text{Epistemic Neutrality}
}
$$

並把問題從：

$$
\text{which evidence enters?}
$$

推進到：

$$
\boxed{
\text{which relations are allowed to connect what enters?}
}
$$

---

# 摘要

傳統 belief-revision framework 常以 belief set、belief base 或 epistemic state 表示 agent 的信念；AGM 的經典模型尤其把理想化 agent 的 belief state 表示為在某形式語言中對 logical consequence 封閉的句子集合，並研究 expansion、contraction 與 revision。這一表示法具有深厚的邏輯價值，但若研究真實 worldview 的差異，單純列出 agent 接受哪些 proposition，可能無法捕捉其最重要的結構差異。

其他研究傳統早已顯示 relation 的必要性。Dung abstract argumentation 以 argument set 與 attack relation 組成 directed graph；Thagard explanatory coherence 以 explanation、co-explanation、analogy 與 contradiction 等 relation 共同決定 hypothesis 的整體 coherence；Bayesian networks 以 directed acyclic graph 表示 variable dependence structure，而 causal graph 進一步讓 edge 承擔 direct-cause interpretation 所需的額外假設；近年的 belief network analysis 則以 network structure 研究 ideology、worldview、norm systems 與 political attitudes。2024 年 Belief Miner 更直接蒐集群體對 cause-effect relation 的判斷，並將 crowd causal graph 與 reference relations 比較以定位 potential causal illusions。

本文因此提出 **Epistemic Admissible-Arrow System（EAAS）**。最小形式為：

$$
\mathcal B
=
(V,E,\pi,\Phi)
$$

其中：

- $V$ 是 agent 可承認的 epistemic nodes；
- $E$ 是 agent 當前允許的 typed relations；
- $\pi$ 是 evidence / source selection policy；
- $\Phi$ 是新 evidence 進入後對 nodes、edges 與 weights 的吸收與 revision operator。

為避免把所有 edge 混成同一語意，本文使用擴充形式：

$$
\mathcal B^{+}
=
(V,\mathcal T,\mathfrak A,\omega,\pi,\Phi)
$$

其中：

- $\mathcal T$ 為 arrow-type space；
- $\mathfrak A$ 為 arrow-admission operator；
- $\omega$ 為已允許 arrow 的權重或 confidence assignment。

典型 arrow type 包括：

$$
\mathcal T
=
\{
\text{entails},
\text{supports},
\text{attacks},
\text{causes},
\text{explains},
\text{enables},
\text{precedes},
\text{analogizes},
\text{normatively-justifies}
\}.
$$

本文的核心命題是：

$$
\boxed{
V_1=V_2
\not\Rightarrow
\mathcal B_1=\mathcal B_2
}
$$

兩個 agent 可以接受完全相同的 factual nodes，卻因允許不同 causal、explanatory、evidential 或 normative arrows，而居住在不同的 epistemic topology 中。

本文進一步提出 **Node Agreement（NA）**、**Typed-Edge Agreement（TEA）**、**Topological Divergence（TD）**、**Arrow Revision Elasticity（ARE）**、**Relation-Type Confusion（RTC）** 與 **Topological Escape Capacity（TEC）** 等啟發式量，並建立 **Arrow-Admissibility Audit Protocol（AAAP）**。

本文不把 edge-aware model 宣稱為 belief representation 的唯一正確形式，也不主張 AGM、Bayesian models 或 argumentation frameworks 無法表示關係。本文主張的是一個診斷原則：

$$
\boxed{
\text{If two agents agree on the nodes but systematically disagree on the arrows, a node-only comparison has missed the disagreement}
}
$$

---

# 0　問題起點：同樣的事實，可以連成不同的世界

假設兩個 agent 都接受：

$$
A=\text{true},
$$

$$
B=\text{true},
$$

$$
C=\text{true}.
$$

因此 node-level comparison 得到：

$$
V_1=V_2=\{A,B,C\}.
$$

但 Agent 1 接受：

$$
A
\xrightarrow{\text{causes}}
B
\xrightarrow{\text{explains}}
C.
$$

Agent 2 只接受：

$$
A
\xrightarrow{\text{precedes}}
B,
$$

並拒絕：

$$
A
\xrightarrow{\text{causes}}
B.
$$

對兩者而言，沒有任何 factual node 需要改變。

真正不同的是：

$$
E_1\neq E_2.
$$

如果研究只問：

> 你相信 A 嗎？

> 你相信 B 嗎？

> 你相信 C 嗎？

我們可能錯誤得到：

> 兩人的 worldview 幾乎一致。

但他們真正的 explanatory world 已經不同。

---

# 1　AGM 的重要性，以及本文不應誇大的地方

AGM belief revision 是 belief-change theory 的核心傳統之一。

在其經典理想化中，belief state 通常以 belief set $K$ 表示，即形式語言中的一組句子，常假定對 logical consequence 封閉。

三種基本 change operation 為：

$$
\text{expansion},
$$

$$
\text{contraction},
$$

以及：

$$
\text{revision}.
$$

若輸入新命題 $\varphi$，revision 可概念化為：

$$
K
\mapsto
K * \varphi.
$$

本文不能錯誤宣稱：

> AGM 不能表示關係。

因為：

$$
\text{Causes}(A,B)
$$

本身也可以被寫成一個 proposition 放入 belief language。

所以 SET05 的問題不是 expressive impossibility。

真正問題是 representation emphasis：

$$
\boxed{
\text{a relation encoded as another sentence can remain diagnostically hidden as a relation}
}
$$

若研究目標是：

- 哪些 relation type 被允許；
- 哪些 arrow 被反證刪除；
- 哪些 edge 被 retype；
- 哪些局部 topology 使其他 belief 得以存活；

則顯式 graph representation 可能比單純 belief-set listing 更具診斷力。

---

# 2　Dung：arguments 本身不夠，attack relation 會改變可接受集合

Dung 的 abstract argumentation framework 提供一個直接例子。

其基本形式為：

$$
AF=(A,R),
$$

其中：

- $A$ 為 arguments；
- $R$ 為 attack relation。

如果只保留 $A$ 而刪除 $R$：

$$
AF
\mapsto
A,
$$

我們就失去：

- 誰攻擊誰；
- 誰防禦誰；
- 哪些集合 conflict-free；
- 哪些 arguments admissible；
- 哪些 extension 可以成立。

因此：

$$
\boxed{
\text{argument inventory}
\neq
\text{argumentation structure}
}
$$

這與 SET05 的核心直覺同構。

---

# 3　Bayesian Networks：同一批 nodes，不同 DAG 就是不同模型

Bayesian network 的基本圖結構為 directed acyclic graph：

$$
G=(V,E).
$$

graph structure 配合 conditional probability tables 表示 joint distribution 的 factorization。

同一個 variable set：

$$
V
$$

若使用不同 DAG：

$$
G_1=(V,E_1),
$$

$$
G_2=(V,E_2),
$$

可能編碼不同 conditional-independence assumptions。

因此：

$$
V_1=V_2
$$

不使：

$$
G_1=G_2.
$$

在 causal interpretation 下，問題更尖銳。

若 parent-child edge 被解讀為 direct causal relation，則：

$$
X
\xrightarrow{\text{cause}}
Y
$$

不是圖形裝飾，而是一個可受攻擊的 causal commitment。

所以 SET05 借用的不是 Bayesian network 的全部 formal semantics，而是這個非常基本的提醒：

$$
\boxed{
\text{edges carry model commitments}
}
$$

---

# 4　Thagard：explanatory coherence 本來就是 relation-sensitive

Thagard 的 explanatory-coherence theory 不是只問 hypothesis 是否出現在集合中。

propositions 之間可以因：

- explanation；
- co-explanation；
- analogy；

形成 coherence，也可以因 contradiction 形成 incoherence。

hypothesis 最後是否被接受，取決於整個 constraint structure，而非單一 proposition 的孤立真值。

因此：

$$
\boxed{
\text{what a proposition means for a theory depends partly on what it is allowed to connect to}
}
$$

這對 SET05 很重要。

同一個 observation：

$$
O
$$

可以在 Theory 1 中是：

$$
O
\xrightarrow{\text{supports}}
H_1,
$$

但在 Theory 2 中只被允許：

$$
O
\xrightarrow{\text{compatible-with}}
H_1.
$$

兩支 arrow 的 epistemic force 完全不同。

---

# 5　Belief Network Analysis：worldview 的結構已經是實證研究對象

Boutyline 與 Vaisey 的 Belief Network Analysis 將 political attitude systems 模型化為 interrelated network，讓研究者分析 belief centrality 與 network organization。

2024 年 ResIN 方法進一步將 belief network approach 推向 ideology、worldview 與 norm systems 的結構分析。

2025 年 Bentall 等人以 2,058 位英國成人資料研究 political belief networks，發現政治光譜兩端的 belief networks 在其資料中比中間組更高度 interconnected，並辨識出具有不同 centrality 的 attitudes。

這些工作的重要性在於：

$$
\boxed{
\text{belief-system structure is empirically measurable}
}
$$

但 SET05 必須保持一個限制：

BNA / network psychometrics 的 edge 往往是：

$$
\text{statistical association}
$$

或 partial correlation。

它不自動等於：

$$
\text{an individual's consciously admissible causal or explanatory arrow}.
$$

因此 SET05 不能把 population-level correlation network 偷換成 individual epistemic topology。

---

# 6　Belief Miner：causal belief 本身可以被當作 edge elicitation

2024 年 Salim、Hoque 與 Mueller 的 Belief Miner 直接讓參與者表達 cause-effect relations，並將群體 causal-relation network 與 reference credibility structure 比較。

這說明一件很關鍵的事：

我們不一定只能問：

> 你相信這個節點嗎？

也可以問：

> 你相信這兩個節點之間有什麼關係？

因此：

$$
\boxed{
\text{edge elicitation}
}
$$

本身可以成為 empirical object。

這也讓 SET05 不必停留在純哲學比喻。

---

# 7　從 Belief Set 到 Admissible-Arrow Regime

本文提出最小表示：

$$
\mathcal B
=
(V,E,\pi,\Phi).
$$

其中：

## 7.1 Node Set

$$
V
$$

可以包含：

- observations；
- propositions；
- hypotheses；
- entities；
- events；
- values；
- norms；
- models；
- predictions。

---

## 7.2 Edge Set

$$
E
$$

不是單一關係，而是 typed edges。

更正式地：

$$
E
\subseteq
V
\times
\mathcal T
\times
V.
$$

一支 edge：

$$
e=(u,t,v)
$$

表示：

$$
u
\xrightarrow{t}
v.
$$

---

## 7.3 Selection Policy

$$
\pi
$$

承接 SET01 至 SET04：

決定哪些 evidence、nodes 與 sources 進入當前系統。

---

## 7.4 Revision Operator

$$
\Phi
$$

決定新 evidence 進入後：

- node 是否新增；
- node confidence 是否改變；
- edge 是否新增；
- edge 是否刪除；
- edge type 是否改變；
- edge weight 是否更新；
- admissibility rule 是否改變。

---

# 8　擴充形式：Epistemic Admissible-Arrow System

為了把「什麼箭頭可以進來」本身顯式化，定義：

$$
\mathcal B^{+}
=
(V,\mathcal T,\mathfrak A,\omega,\pi,\Phi).
$$

其中：

$$
\mathfrak A:
V\times\mathcal T\times V\times C
\to
\{-1,0,1\}.
$$

可解讀為：

$$
-1=\text{reject},
$$

$$
0=\text{suspend},
$$

$$
1=\text{admit}.
$$

 $C$ 表示 context、evidence、domain rules 與背景條件。

當：

$$
\mathfrak A(u,t,v\mid C)=1,
$$

則候選 arrow：

$$
u\xrightarrow{t}v
$$

被納入當前 epistemic topology。

這個結構稱為 **Epistemic Admissible-Arrow System（EAAS）**。

---

# 9　Arrow Type 不能偷換

至少需要區分：

$$
\mathcal T
=
\{
t_{\mathrm{entail}},
t_{\mathrm{support}},
t_{\mathrm{attack}},
t_{\mathrm{cause}},
t_{\mathrm{explain}},
t_{\mathrm{enable}},
t_{\mathrm{precede}},
t_{\mathrm{analogy}},
t_{\mathrm{norm}}
\}.
$$

因為下列箭頭不是同一件事。

$$
A
\xrightarrow{\text{precedes}}
B
$$

不等於：

$$
A
\xrightarrow{\text{causes}}
B.
$$

$$
E
\xrightarrow{\text{supports}}
H
$$

不等於：

$$
E
\xrightarrow{\text{entails}}
H.
$$

$$
M
\xrightarrow{\text{explains}}
O
$$

不等於：

$$
M
\xrightarrow{\text{proves}}
O.
$$

因此很多 worldview disagreement 可能根本不是 node disagreement，而是：

$$
\boxed{
\text{relation-type disagreement}
}
$$

---

# 10　Arrow-Type Debt：不同關係欠不同證明

若一支箭頭被標成：

$$
A
\xrightarrow{\text{causes}}
B,
$$

它欠的是 causal evidence 與 identification assumptions。

若被標成：

$$
A
\xrightarrow{\text{entails}}
B,
$$

它欠的是 formal derivation。

若：

$$
A
\xrightarrow{\text{supports}}
B,
$$

它欠的是 evidential relevance 與 weight。

若：

$$
A
\xrightarrow{\text{normatively-justifies}}
B,
$$

它欠的是 normative bridge。

所以不能用：

$$
\text{same evidence standard}
$$

檢查所有 edge type。

本文稱之為：

$$
\boxed{
\text{Arrow-Type Debt}
}
$$

即每一種 relation type 都有自己的 certification burden。

---

# 11　Arrow-Type Confusion：很多錯誤其實是 edge retyping

最常見的結構性錯誤之一不是 node fabrication，而是：

$$
t_1
\mapsto
t_2.
$$

例如：

$$
\text{precedes}
\mapsto
\text{causes},
$$

$$
\text{correlates}
\mapsto
\text{causes},
$$

$$
\text{compatible}
\mapsto
\text{predicted},
$$

$$
\text{explains}
\mapsto
\text{proves},
$$

$$
\text{possible}
\mapsto
\text{probable},
$$

$$
\text{is}
\mapsto
\text{ought}.
$$

所有 factual nodes 都可以保持不變。

失真只發生在 arrow label。

這將在 SET06 進一步展開。

---

# 12　Node-Equivalent Worldviews

定義兩個 worldview：

$$
\mathcal B_1,
\quad
\mathcal B_2.
$$

若其 node truth assignment 相同：

$$
V_1=V_2
$$

且：

$$
q_1(v)=q_2(v)
$$

對所有共同 node 成立，則稱兩者 **node-equivalent**。

但若：

$$
E_1\neq E_2,
$$

則為：

$$
\boxed{
\text{node-equivalent but topologically divergent}
}
$$

這是 SET05 最核心的對象。

---

# 13　同樣 evidence，為什麼不同 theory 會得到不同 meaning？

設 observation：

$$
O.
$$

Theory 1 允許：

$$
O
\xrightarrow{\text{supports}}
H_1.
$$

Theory 2 認為存在 confounder：

$$
C
\xrightarrow{\text{causes}}
O
$$

因此拒絕：

$$
O
\xrightarrow{\text{supports}}
H_1
$$

的高權重版本。

兩者都看到 $O$。

差別不是：

$$
\text{observation access}.
$$

而是：

$$
\text{edge admissibility}.
$$

所以：

$$
\boxed{
\text{same evidence}
\not\Rightarrow
\text{same evidential role}
}
$$

---

# 14　背景理論本身就是 Arrow Gate

對候選 arrow：

$$
e=(u,t,v),
$$

agent 不會每次從零判斷。

他會利用：

- background theory；
- trusted methodology；
- ontology；
- domain conventions；
- causal assumptions；
- value commitments；
- prior graph。

因此：

$$
\mathfrak A(e\mid C)
$$

本身受到當前：

$$
\mathcal B_t
$$

影響。

可寫成：

$$
\mathfrak A_t(e)
=
G(e,\mathcal B_t,C_t).
$$

因此 belief system 不只儲存 edge。

它也參與決定：

> 下一支 edge 有沒有資格進來。

這就是 **admissible-arrow regime**。

---

# 15　Arrow Gate 可以是健康的

「拒絕某類 arrow」不必然是 bias。

科學方法本來就建立 gate。

例如：

$$
\text{correlation}
\not\Rightarrow
\text{causation}.
$$

形式邏輯也有 gate：

$$
\text{premises}
\not\vdash
\text{conclusion}
$$

時，就不能畫 entailment arrow。

好的 gate 不是什麼都接受。

而是：

$$
\boxed{
\text{arrow admission is constrained by relation-specific evidence}
}
$$

所以 SET05 不鼓勵：

> 對所有可能關係保持開放。

那會變成 topology explosion。

真正目標是：

$$
\boxed{
\text{admit, suspend, reject, and revise arrows under explicit rules}
}
$$

---

# 16　Arrow Gate 也可以自我封閉

危險出現在：

$$
\mathfrak A_B(e^-)= -1
$$

不是因為 $e^-$ 的 evidence quality 低，

而只是因為：

$$
e^-
$$

會破壞當前 worldview。

更進一步：

$$
e^-
\text{ rejected}
\Rightarrow
\text{evidence supporting }e^-\text{ also downgraded}.
$$

此時 topology 開始保護自己。

這是 SET07 的前兆。

---

# 17　Belief Revision 不只是 node surgery，而是 graph surgery

傳統 belief-change 語言常聚焦：

$$
K
\mapsto
K'.
$$

EAAS 則把 change event 拆成至少七種。

## 17.1 Node Addition

$$
V'
=
V\cup\{v\}.
$$

---

## 17.2 Node Removal

$$
V'
=
V\setminus\{v\}.
$$

---

## 17.3 Edge Addition

$$
E'
=
E\cup\{e\}.
$$

---

## 17.4 Edge Deletion

$$
E'
=
E\setminus\{e\}.
$$

---

## 17.5 Edge Retyping

$$
(u,t_1,v)
\mapsto
(u,t_2,v).
$$

---

## 17.6 Edge Reweighting

$$
\omega(e)
\mapsto
\omega'(e).
$$

---

## 17.7 Gate Revision

$$
\mathfrak A
\mapsto
\mathfrak A'.
$$

最後一種最深。

因為它改變的是：

> 未來哪些關係可以進來？

而不是只改現在這一支 edge。

---

# 18　更新同一 node，也可能只是 topology 改變

假設原本：

$$
A
\xrightarrow{\text{causes}}
B.
$$

新研究未否定：

$$
A
$$

也未否定：

$$
B.
$$

它只發現：

$$
C
$$

是共同原因。

於是：

$$
C
\xrightarrow{\text{causes}}
A,
$$

$$
C
\xrightarrow{\text{causes}}
B,
$$

並刪除：

$$
A
\xrightarrow{\text{causes}}
B.
$$

node truth 幾乎沒變。

但 explanatory world 已經大幅改變。

所以：

$$
\boxed{
\text{major belief revision can occur with minimal node revision}
}
$$

---

# 19　Node Agreement

對兩個 systems 的共同 candidate node set $V^*$，定義啟發式：

$$
\mathrm{NA}
=
\frac{
|\{v\in V^*:q_1(v)=q_2(v)\}|
}{
|V^*|
}.
$$

若：

$$
\mathrm{NA}\rightarrow1,
$$

表示 node-level agreement 高。

但它不能表示 edge agreement。

---

# 20　Typed-Edge Agreement

令 typed-edge universe 為：

$$
E^*.
$$

定義：

$$
\mathrm{TEA}
=
\frac{
|E_1\cap E_2|
}{
|E_1\cup E_2|+\epsilon
}.
$$

其中 edge identity 包含：

$$
(u,t,v).
$$

因此：

$$
(u,\text{precedes},v)
$$

與：

$$
(u,\text{causes},v)
$$

視為不同 typed edge。

可能出現：

$$
\mathrm{NA}\approx1
$$

但：

$$
\mathrm{TEA}\ll1.
$$

這就是 node-equivalent topological divergence。

---

# 21　Topological Divergence

定義：

$$
\mathrm{TD}
=
1-\mathrm{TEA}.
$$

更完整版本可以加入 edge weight：

$$
\mathrm{TD}_{\omega}
=
D(E_1,\omega_1;E_2,\omega_2).
$$

本文不指定唯一 distance metric。

因為不同 domain 可能需要：

- Jaccard distance；
- graph edit distance；
- spectral distance；
- typed-edge weighted distance；
- causal structural distance。

核心只是：

$$
\boxed{
\text{worldview distance should not be reduced to node disagreement alone}
}
$$

---

# 22　Relation-Type Confusion

若 agent 在 matched tasks 中把 $t_i$ 系統性當成 $t_j$，定義候選：

$$
\mathrm{RTC}(t_i,t_j)
=
P(\hat t=t_j\mid t=t_i).
$$

例如：

$$
\mathrm{RTC}
(
\text{precedes},
\text{causes}
).
$$

RTC 可以用於：

- 人類 reasoning；
- AI reasoning；
- scientific communication；
- media interpretation；
- education。

其價值是把「推理錯了」再細分成：

> node 錯，還是 arrow type 錯？

---

# 23　Arrow Revision Elasticity

令 evidence $E_e$ 專門針對 edge $e$。

edge confidence 原為：

$$
\omega_t(e).
$$

新 evidence 後：

$$
\omega_{t+1}(e).
$$

定義概念性：

$$
\mathrm{ARE}(e)
=
\frac{
|\omega_{t+1}(e)-\omega_t(e)|
}{
\mathrm{Strength}(E_e)+\epsilon
}.
$$

過低可能表示：

$$
\text{edge rigidity}.
$$

過高則可能表示：

$$
\text{edge instability}.
$$

健康狀態不是越高越好，而是：

$$
\boxed{
\text{edge change should be proportionate to discriminative evidence}
}
$$

---

# 24　Topological Escape Capacity

SET04 提出 Epistemic Escape Capacity。

SET05 進一步提出 **Topological Escape Capacity（TEC）**：

> 一個 worldview 是否有能力撤除、反轉或 retype 自己的核心 arrows？

概念上：

$$
\mathrm{TEC}\in[0,1].
$$

測量問題包括：

1. 是否能指出核心 edge？
2. 是否能指定什麼 evidence 會刪除該 edge？
3. 是否能接受 rival relation type？
4. 是否能在 node 不變時修改 explanation？
5. 是否允許 independent graph reconstruction？
6. 核心 edge 被刪除後，是否只是新增 ad hoc edge 立即補回？

低 TEC 意味：

$$
\text{topology itself is becoming self-protective}.
$$

---

# 25　Arrow-Admissibility Audit Protocol（AAAP）

## Step 1：Freeze the Nodes

先固定雙方共同接受的 facts：

$$
V_{\mathrm{shared}}.
$$

避免爭論一直滑回：

> 你連事實都不承認。

---

## Step 2：Extract the Arrows

要求各方畫出：

$$
E.
$$

至少標示：

- source；
- target；
- relation type；
- confidence；
- evidence；
- boundary conditions。

---

## Step 3：Type Every Arrow

不准使用模糊的：

> 有關。

要求回答：

$$
\text{what kind of relation?}
$$

是：

- cause；
- support；
- explanation；
- entailment；
- analogy；
- temporal order；
- norm？

---

## Step 4：Assign Arrow-Type Debt

對每支 edge 問：

> 這種類型的箭頭欠什麼證據？

例如 causal edge 不能用純 temporal order 還債。

---

## Step 5：Construct Rival Graphs

在相同 node set 上建立：

$$
G_1,
G_2,\ldots,G_k.
$$

要求 competing topology 都解釋同一批 shared facts。

---

## Step 6：Find Discriminating Edges

找：

$$
e^*
$$

使：

$$
e^*\in E_1
$$

但：

$$
e^*\notin E_2.
$$

再設計 evidence：

$$
D(e^*)
$$

專門區分兩種 topology。

---

## Step 7：Blind Relation Review

可行時隱去：

- theory name；
- author；
- ideology；
- institution；
- model identity。

只給：

$$
(u,t,v,E_e).
$$

測 reviewer 是否仍允許 edge。

---

## Step 8：Run Edge Revision

若 evidence 達門檻，要求：

$$
E
\mapsto
E'.
$$

不允許只在文字上承認：

> 這是一個限制。

卻讓 topology 完全不變。

---

# 26　實驗一：Node-Matched, Edge-Different

給兩組 participants 完全相同的 nodes。

只改變 relation training：

Group A 學到：

$$
A
\xrightarrow{\text{cause}}
B.
$$

Group B 學到：

$$
A
\xrightarrow{\text{correlates}}
B.
$$

之後給新 evidence。

測：

- prediction；
- intervention choice；
- explanation；
- confidence；
- transfer。

若行為顯著不同，支持：

$$
\text{edge structure has independent explanatory value}.
$$

---

# 27　實驗二：Arrow Retyping Without Node Change

固定：

$$
A=\text{true},
$$

$$
B=\text{true}.
$$

操縱：

$$
A
\xrightarrow{\text{precedes}}
B
$$

與：

$$
A
\xrightarrow{\text{causes}}
B.
$$

測 receiver 是否對：

- counterfactual prediction；
- intervention；
- responsibility；
- forecast

產生不同判斷。

這能直接測：

$$
\text{relation type}
$$

是否比 node truth 更能預測下游 reasoning。

---

# 28　實驗三：Graph Revision versus Belief-Set Revision

給新 evidence $E$，它不否定任何既有 factual node，只否定一支 core edge。

比較：

1. node-only belief report；
2. edge-aware graph report。

若 node-only measure 顯示「幾乎沒有 belief change」，但 edge-aware measure 能預測下游決策變化，則支持 SET05 的診斷價值。

---

# 29　實驗四：Independent Graph Reconstruction

讓不同 evaluator 在相同 primary evidence 上盲建 graph：

$$
G_1,\ldots,G_n.
$$

比較：

$$
\mathrm{NA}
$$

與：

$$
\mathrm{TEA}.
$$

若：

$$
\mathrm{NA}\gg\mathrm{TEA},
$$

表示 disagreement 主要發生在 arrows。

若兩者高度相近，SET05 在該 domain 的額外價值較小。

---

# 30　實驗五：Arrow Gate Symmetry

提供結構相同、方向相反的 candidate relations。

例如：

$$
e^+
$$

支持當前 theory，

$$
e^-
$$

削弱當前 theory。

控制 evidence quality 後比較：

$$
\mathfrak A(e^+)
$$

與：

$$
\mathfrak A(e^-).
$$

若存在穩定不對稱，可能是 topology-protective gate。

---

# 31　SET05 與「下一步就是下一步」的接口

一支：

$$
A
\to
B
$$

到底代表：

- immediate transition；
- reachability；
- causal transition；
- explanatory compression；
- narrative adjacency；

完全不同。

所以「下一步」本身就是 arrow-type claim。

如果真正過程是：

$$
A
\to
x_1
\to
x_2
\to
B,
$$

卻被畫成：

$$
A
\to
B,
$$

這可能只是合法的 macro-compression，也可能是關鍵 mechanism omission。

SET05 只負責建立：

$$
\boxed{
\text{arrow type must be explicit}
}
$$

而 SET06 將進一步研究：

$$
\boxed{
\text{true nodes can be connected by false, compressed, omitted, or retyped topology}
}
$$

---

# 32　「信念系統是箭頭系統」不是字面排除 nodes

本篇標題：

> 信念系統不是信念集合，而是允許箭頭的系統

是一個強調性命題，不應被誤讀成：

$$
V\text{ 不重要}.
$$

更精確地說：

$$
\boxed{
\text{A belief system is not exhausted by its node set}
}
$$

它至少包含：

$$
\text{nodes}
+
\text{relations}
+
\text{admission rules}
+
\text{revision rules}.
$$

因此本文不是：

$$
V
\mapsto
E
$$

的取代論。

而是：

$$
V
\mapsto
(V,E,\mathfrak A,\Phi)
$$

的擴充論。

---

# 33　與 Belief Network Analysis 的差異

BNA 常以 survey-item association 建立 statistical network。

SET05 的 EAAS 則更接近：

$$
\text{agent-endorsed typed relational commitments}.
$$

因此：

$$
\text{BNA edge}
$$

與：

$$
\text{EAAS edge}
$$

不能直接互換。

可能出現：

$$
\text{population correlation edge}
$$

但個體不相信任何直接關係。

也可能個體強烈相信：

$$
A
\xrightarrow{\text{causes}}
B
$$

但 population data 不支持。

兩者的 discrepancy 本身反而值得研究。

---

# 34　與 causal graphs 的差異

EAAS 不是 causal DAG。

原因是：

$$
\mathcal T
$$

允許多種 relation type，而且：

- explanation 可以成 cycle；
- normative justification 未必是 causal；
- attack relation 未必 acyclic；
- analogy relation 可以 symmetric；
- support relation 可以 probabilistic；
- temporal relation可能只表示 order。

因此 EAAS 更接近 typed directed multigraph：

$$
G_{\mathrm{EAAS}}
=
(V,E,\mathcal T,\omega).
$$

在特定 domain，才投影成：

$$
G_{\mathrm{causal}},
$$

$$
G_{\mathrm{argument}},
$$

$$
G_{\mathrm{explanatory}}.
$$

---

# 35　與正式邏輯的關係

若：

$$
A
\xrightarrow{\text{entails}}
B,
$$

則此 edge 可對應：

$$
A\vdash B
$$

或更完整 premise set：

$$
\Gamma\vdash B.
$$

但不是所有 epistemic edge 都是 entailment。

把：

$$
\text{supports}
$$

偷換成：

$$
\text{entails}
$$

正是一種常見 relation-type inflation。

所以 EAAS 並不取代 formal logic。

它反而要求：

> 只有標成 entailment 的箭頭，才欠 formal entailment 的 debt。

---

# 36　與科學理論的關係

科學理論的巨大變化有時並不是觀測節點突然全部改變。

歷史上，同一批 observations 可以被不同 theoretical topology 組織。

Thagard 對 continental drift 等科學史案例的 explanatory-coherence 分析正展示：同一 hypothesis 在不同背景知識網路下可以呈現不同 coherence。

所以 theory change 可以部分理解為：

$$
\boxed{
\text{reorganization of explanatory arrows over partially shared observations}
}
$$

而不是單純：

$$
\text{old facts}
\mapsto
\text{new facts}.
$$

---

# 37　與政治、宗教、哲學、數學立場的關係

SET05 不需要選任何具體陣營做靶。

只要存在：

$$
V
$$

與：

$$
E,
$$

就可能研究 admissible-arrow regime。

例如：

- 政治理論允許哪些 institutional cause；
- 哲學 ontology 允許哪些 dependence relation；
- 宗教 worldview 允許哪些 metaphysical explanation；
- 數學哲學允許哪些 existence / proof / ontology relation；
- 科學主義允許哪些 explanatory source；
- 反科學主義允許哪些 evidence rejection；
- Bayesian methodology 允許哪些 likelihood structure；
- formalism 允許哪些 proof relation。

本文採對稱原則：

$$
\boxed{
\text{No worldview receives automatic exemption from arrow audit}
}
$$

但這不表示所有 worldview 的 arrow quality 相同。

---

# 38　AI 系統的 Arrow Problem

AI 很容易輸出：

$$
A\to B
$$

因為自然語言中的：

> 因此

> 所以

> 這導致

> 這說明

> 這意味著

本質上都在建立 edge。

所以 AI hallucination 之外還有：

$$
\boxed{
\text{relation hallucination}
}
$$

即 nodes 都正確，但關係錯誤。

例如：

$$
A=\text{true},
$$

$$
B=\text{true},
$$

但：

$$
A
\xrightarrow{\text{causes}}
B
$$

未被支持。

AI evaluation 因此應分：

$$
\text{node verification}
$$

與：

$$
\text{edge verification}.
$$

---

# 39　AI 也可以成為 Arrow Auditor

如果要求 AI：

> fact-check 這段話。

它可能只檢查 nodes。

更好的 protocol 是要求：

1. extract nodes；
2. extract relation phrases；
3. type each edge；
4. demand edge-specific evidence；
5. generate rival topology；
6. identify discriminating observation；
7. mark unresolved arrow debt。

因此：

$$
\boxed{
\text{fact checking}
+
\text{relation checking}
}
$$

才較接近完整 audit。

---

# 40　什麼結果會削弱 SET05？

若以下結果跨 domain 穩定成立，SET05 應縮小：

1. node-only models 對 prediction、decision、belief revision 的預測力與 edge-aware models 幾乎相同；
2. 同 node set 的 edge manipulation 不改變任何下游推理；
3. participants 無法穩定 elicitate relation type；
4. independent graph reconstruction 的 reliability 極低到無法成為研究對象；
5. edge-aware representation 只增加 complexity，沒有帶來 discriminative value；
6. worldview disagreement 幾乎全部可由 node valence / confidence 解釋；
7. arrow-type audit 不提高錯誤偵測；
8. graph revision 不比 belief-set revision 更能預測後續行為。

若如此，EAAS 應被降格成特定 domain 的 visualization tool，而非一般認識論框架。

---

# 41　自反性：EAAS 自己也只是一種 admissible topology

本篇最大的風險是：

> 因為我們開始談箭頭，就開始把一切都看成箭頭。

那會讓 EAAS 自己變成另一個 worldview gate。

所以本文必須承認：

1. 有些 belief difference 用 scalar confidence 就足夠；
2. 有些 relation 太模糊，不適合強行 type；
3. 有些 cognitive structure 未必是 graph-like；
4. hypergraph、dynamic system、tensor representation 或 latent-space model 可能更適合某些 domain；
5. graph representation 是 epistemic projection，不等於 mind 的 literal architecture；
6. arrows 本身仍然需要 evidence，不能因為畫出 graph 就取得真實性。

因此：

$$
\boxed{
\text{EAAS is a diagnostic representation proposal, not an ontology of mind}
}
$$

---

# 42　結論

信念系統不是只回答：

> 你相信哪些東西？

它還回答：

> 哪些東西可以解釋哪些東西？

> 哪些 evidence 可以支持哪些 hypothesis？

> 哪些事件可以被說成原因？

> 哪些相似性足以形成 analogy？

> 哪些 fact 可以通往 normative conclusion？

> 哪些反證具有攻擊核心 edge 的資格？

因此：

$$
\boxed{
\text{Belief systems are not exhausted by belief inventories}
}
$$

更完整地：

$$
\boxed{
\text{worldview}
=
\text{nodes}
+
\text{typed arrows}
+
\text{admission rules}
+
\text{revision rules}
}
$$

兩個人可以：

$$
\mathrm{NA}\approx1
$$

卻：

$$
\mathrm{TEA}\ll1.
$$

他們同意世界裡發生了什麼，

卻不同意：

> **世界是怎麼連起來的。**

而真正深層的 worldview，往往就藏在這裡。

SET05 因此留下最後一條核心命題：

$$
\boxed{
\text{A worldview is not only a map of what exists; it is also a constitution governing which arrows may legally connect what exists}
}
$$

下一步不再只是問：

> 節點是真的嗎？

而是：

> **這支箭頭憑什麼存在？**

這正是 SET06 的入口。

---

# References

1. Alchourron, C. E., Gardenfors, P., & Makinson, D. (1985). On the Logic of Theory Change: Partial Meet Contraction and Revision Functions. *The Journal of Symbolic Logic*, 50(2), 510-530. https://doi.org/10.2307/2274239

2. Hansson, S. O. (2026). Logic of Belief Revision. *The Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/logic-belief-revision/

3. Dung, P. M. (1995). On the Acceptability of Arguments and Its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games. *Artificial Intelligence*, 77(2), 321-357. https://doi.org/10.1016/0004-3702(94)00041-X

4. Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*. Morgan Kaufmann.

5. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

6. Thagard, P. (1989). Explanatory Coherence. *Behavioral and Brain Sciences*, 12(3), 435-467. https://doi.org/10.1017/S0140525X00057046

7. Thagard, P. (2006). Evaluating Explanations in Law, Science, and Everyday Life. *Current Directions in Psychological Science*, 15(3), 141-145. https://doi.org/10.1111/j.0963-7214.2006.00424.x

8. Boutyline, A., & Vaisey, S. (2017). Belief Network Analysis: A Relational Approach to Understanding the Structure of Attitudes. *American Journal of Sociology*, 122(5), 1371-1442. https://doi.org/10.1086/691274

9. Carpentras, D., Lueders, A., & Quayle, M. (2024). Response Item Network (ResIN): A Network-Based Approach to Explore Attitude Systems. *Humanities and Social Sciences Communications*, 11, 589. https://doi.org/10.1057/s41599-024-03037-x

10. Salim, S., Hoque, M. N., & Mueller, K. (2024). Belief Miner: A Methodology for Discovering Causal Beliefs and Causal Illusions from General Populations. *Proceedings of the ACM on Human-Computer Interaction*, 8(CSCW1), Article 21. https://doi.org/10.1145/3637298

11. Bentall, R. P., Zavlis, O., Hyland, P., McBride, O., Bennett, K., & Hartman, T. K. (2025). The Structure of Mass Political Belief Systems: A Network Approach to Understanding the Left-Right Spectrum. *PLOS ONE*, 20(10), e0333595. https://doi.org/10.1371/journal.pone.0333595

12. Bulbulia, J. A. (2024). Methods in Causal Inference. Part 1: Causal Diagrams and Confounding. *Evolutionary Human Sciences*, 6, e40. https://doi.org/10.1017/ehs.2024.35

13. Bochman, A. (2000). A Foundationalist View of the AGM Theory of Belief Change. *Artificial Intelligence*, 116(1-2), 237-263. https://doi.org/10.1016/S0004-3702(99)00092-2

14. Fouillard, V., Taha, S., Boulanger, F., & Sabouret, N. (2021). Belief Revision Theory. *Archive of Formal Proofs*. https://isa-afp.org/entries/Belief_Revision.html

---

## 系列位置

**Selective Truth and Epistemic Topology**

- SET01：高明的謊言不需要假話：選擇性真實、資訊抽樣與失真世界
- SET02：聽者的不可識別問題：當客觀評估與策略性真話產生相同表面訊息
- SET03：張力控制與策略性讓步：可信度如何被工程化
- SET04：真誠的人也能產生選擇性世界：Sincere Selection Bias
- **SET05：信念系統不是信念集合，而是允許箭頭的系統**
- SET06：真節點，假拓撲：資訊操縱如何發生在關係而非命題
- SET07：認識論吸引子與自我封閉：吸收無限資訊而幾乎不學習

---

*SET05 / Selective Truth and Epistemic Topology / EveMissLab / v0.1 / 2026-09-07*
