# TADC-03：拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引

**英文題名：** Six Operators of Topological Attention: Expansion, Contraction, Traversal, Gluing, Detachment, and Re-indexing  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-03  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論命題／形式化操作系統／可證偽研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

TADC-01 提出可變認知空間猜想（VCSC）與注意—空間轉換猜想（ASTC），主張注意活動可能不只在固定認知空間中重新分配權重，還可能參與改變未來哪些對象、關係與路徑成為可達。TADC-02 進一步提出動態認知域（Dynamic Cognitive Domains），將有效 domain 視為由 goal-conditioned relational accessibility 與觀察解析度誘導出的局部認知 chart，而非固定學科 partition。

若這兩個命題要形成真正的動力學，就必須回答：

> **認知空間究竟透過哪些基本操作發生變化？**

本文提出六個候選基本算子：

1. **Expansion \(E\)**：將新的認知對象、關係或鄰域納入有效域；
2. **Contraction \(C\)**：移除、壓低或暫時排除低 relevance 區域；
3. **Traversal \(T\)**：在既有 relational structure 中移動，而不必改變結構；
4. **Gluing \(G\)**：藉由 bridge structure 將原本分離或弱耦合的局部域建立有效連接；
5. **Detachment \(D\)**：削弱、切離或解除原有過強、錯誤或不再適用的關係耦合；
6. **Re-indexing \(R\)**：改變表示解析度，使「一個 domain」可以被壓縮成一個 object，或一個 object 被展開成內部 subdomain。

本文稱此系統為 **Six-Operator Cognitive Transformation System（SOCTS）**。

六算子並非都代表強結構變換。Traversal 可在固定空間中成立；Re-indexing 可能只是表示尺度改變；Expansion、Contraction、Gluing、Detachment 則在強版本中候選地改變有效認知空間。本文因此將算子進一步分成 state operators、representation operators 與 structural operators。

本文提出另一個核心猜想：這些算子一般具有**非交換性、路徑依賴與歷史依賴**。例如：

$$
E\circ C
\neq
C\circ E,
$$

以及：

$$
G\circ D
\neq
D\circ G.
$$

同一組 cognitive objects 經不同操作次序，可能形成不同的可達結構與後續推理路徑。

現有研究已分別觀察到 hierarchical task-set reconfiguration、task-dependent representational geometry、working-memory grouping 對 chunk formation 的影響、predictive learning 對 representational geometry 的塑形、compositional task representations、practice-driven compositional-to-conjunctive shifts，以及 hierarchical cognitive maps。這些研究提供六算子各自的鄰接實證，但沒有任何一項研究直接證明 SOCTS 為人類注意力的基本操作代數。

因此本文的目標不是宣告「六算子就是大腦真實 primitive」，而是建立一套可與傳統 task switching、learning、chunking、semantic priming、working memory、representational geometry 與 cognitive-map 模型競爭的最小操作語言。

---

# 0. 邊界聲明

本文提出的六算子是：

$$
\boxed{
\text{candidate cognitive operators}
}
$$

而不是已被神經科學確認的六個腦機制。

本文也不主張：

$$
\boxed{
\text{there are exactly six fundamental cognitive operators}.
}
$$

未來可能：

- 六個算子可被合併；
- 某些算子可由更基本操作導出；
- 需要加入第七、第八個算子；
- 整套 operator language 無法提供增量預測。

若如此，模型必須修改。

此外：

$$
G(U,V)=U\cup_BV
$$

中的「gluing」目前不是宣稱已建立 topological pushout；

$$
R
$$

也不是嚴格 differential-geometric coordinate transformation。

本文使用的是具有明確行為與結構含義的**候選形式語言**。

---

# 1. 前兩篇留下的缺口

TADC-01：

$$
\mathcal C_t
=
(
X_t,
\mathcal R_t,
\kappa_t,
\mathcal N_t,
A_t,
G_t
).
$$

TADC-02：

$$
\mathfrak A_t
=
\{
(U_{\alpha,t},\phi_{\alpha,t})
\}_{\alpha\in I_t}.
$$

並提出：

$$
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1}.
$$

但是：

> 這個箭頭到底由什麼構成？

如果只寫：

$$
\Psi:
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1},
$$

卻不拆：

$$
\Psi
$$

內部的操作類型，

「動態認知域」仍然只是一個黑盒。

TADC-03 的目的就是把：

$$
\Psi
$$

拆成候選 primitive operator family：

$$
\boxed{
\mathcal O
=
\{E,C,T,G,D,R\}.
}
$$

---

# 2. Six-Operator Cognitive Transformation System（SOCTS）

定義：

$$
\mathcal O
=
\{
E,C,T,G,D,R
\}.
$$

對時間 \(t\) 的認知結構：

$$
\mathcal C_t
$$

與認知 atlas：

$$
\mathfrak A_t,
$$

一個 cognition episode 可以表示為 operator sequence：

$$
\omega
=
O_nO_{n-1}\cdots O_2O_1,
$$

其中：

$$
O_i\in\mathcal O.
$$

所以：

$$
\mathcal C_{t+n}
=
\omega(\mathcal C_t).
$$

這不是宣稱 cognition 真的是離散六符號機器。

它只是一個可操作化的 coarse-grained representation。

---

# 3. 三類算子

六算子先分成三層。

## 3.1 State Operator

### Traversal \(T\)

可只改變：

$$
A_t
$$

或 current cognitive location，

而不改變：

$$
X_t,\mathcal R_t,\mathcal N_t.
$$

---

## 3.2 Representation Operator

### Re-indexing \(R\)

主要改變：

$$
\phi_{\alpha,t}
$$

或 resolution：

$$
\lambda_t,
$$

而不必改變 underlying relation support。

---

## 3.3 Structural Operators

候選包括：

$$
E,C,G,D.
$$

它們可能改變：

$$
X_t,
\mathcal R_t,
\kappa_t,
\mathcal N_t
$$

中的至少一項。

因此：

$$
\boxed{
\text{not every operator is a topology-changing operator}.
}
$$

這是一條必要限制。

---

# 4. 算子一：Expansion \(E\)

## 4.1 最小定義

給定目前有效 domain：

$$
U_t\subseteq X_t.
$$

若：

$$
y\notin U_t
$$

但：

$$
\kappa_t(U_t,y\mid G_t)\geq\theta_E,
$$

則：

$$
E(U_t)
=
U_t\cup\{y\}.
$$

更一般：

$$
E(U_t)
=
U_t
\cup
N_{\mathcal R}
(
U_t;
G_t,\theta_E
).
$$

---

# 5. Expansion 不只是「想到更多東西」

必須區分：

## Activation Expansion

原本：

$$
y\in X_t
$$

只是：

$$
w_t(y)\approx0.
$$

現在：

$$
w_{t+1}(y)\uparrow.
$$

這只是 active-set expansion。

---

## Accessibility Expansion

原本：

$$
y\notin
\operatorname{Reach}^{(k)}_t(U),
$$

之後：

$$
y\in
\operatorname{Reach}^{(k)}_{t+1}(U).
$$

這才是 ASTC-M 意義下的 expansion。

---

## Structural Expansion

甚至：

$$
y\notin X_t
$$

作為 functional cognitive unit 不存在，

但經 inference / abstraction / chunk formation：

$$
y\in X_{t+1}.
$$

這是 ASTC-S 的強 expansion。

因此：

$$
\boxed{
E_A
\neq
E_{\mathrm{reach}}
\neq
E_S.
}
$$

---

# 6. Expansion 的可能來源

Expansion 可能由：

- external input；
- memory retrieval；
- analogy；
- causal inference；
- exploration；
- curiosity；
- prediction error；
- cross-domain bridge；
- compositional recombination；

引發。

所以：

$$
E
$$

不等於 attention。

更準確：

$$
E
=
F(
a_t,
m_t,
e_t,
G_t,
\mathcal R_t
).
$$

TADC 的命題只是：

$$
\frac{\partial E}{\partial a_t}
$$

在部分條件可能非零。

---

# 7. Expansion 與現有研究

2024 年 predictive-learning 研究顯示，人類表徵幾何會隨環境統計 regularity 改變，並將 temporally contiguous / predictable stimuli 拉近成 cluster。

這說明：

$$
\boxed{
\text{learning can reshape effective representational neighborhood}.
}
$$

但它不能單獨證明 attention-driven Expansion。

同樣，2024 年 human hippocampal single-neuron research 顯示 abstract representations 可在 inference learning 中形成，支持：

$$
X_t
\rightarrow
X_{t+1}
$$

式 functional representation emergence 的可能性。

但其機制仍可主要是 learning / inference。

---

# 8. 算子二：Contraction \(C\)

若：

$$
U_t
$$

含大量目前 goal-irrelevant cognitive material，

可以定義：

$$
C(U_t)
=
\{
x\in U_t:
\rho_t(x\mid G_t)\geq\theta_C
\}.
$$

其中：

$$
\rho_t
$$

是 task relevance。

因此：

$$
C(U_t)\subseteq U_t.
$$

---

# 9. Contraction 不等於遺忘

至少拆三類。

## Active Contraction

$$
A_{t+1}\subset A_t.
$$

只是 foreground 減少。

---

## Accessibility Contraction

$$
\operatorname{Reach}^{(k)}_{t+1}
\subset
\operatorname{Reach}^{(k)}_t.
$$

某些路徑暫時不再容易使用。

---

## Structural Contraction

$$
X_{t+1}\subset X_t
$$

或：

$$
\mathcal R_{t+1}
\subset\mathcal R_t.
$$

功能單位 / relations 真正失去有效性。

這可能來自：

- extinction；
- forgetting；
- pruning；
- task specialization；
- pattern separation；
- schema compression。

所以：

$$
\boxed{
C
\neq
\text{forgetting only}.
}
$$

---

# 10. Contraction 的功能

若只有 Expansion：

$$
|X_t|\rightarrow\infty
$$

會導致：

- search explosion；
- interference；
- irrelevant branching；
- low precision；
- cognitive overload。

因此高階 cognition 需要：

$$
\boxed{
E
+
C
}
$$

的耦合。

Expansion 增加候選可能性：

$$
\text{recall}\uparrow.
$$

Contraction 提高：

$$
\text{precision}\uparrow.
$$

因此 cognition 可能不是：

$$
\text{expand forever},
$$

而是：

$$
\boxed{
E\rightarrow C\rightarrow E\rightarrow C\rightarrow\cdots
}
$$

的動態。

---

# 11. Practice 作為 Contraction / Specialization 的鄰接證據

2025 年 extended task-learning 研究發現，task representations 可由早期較 compositional 的形式逐步轉向較 task-specific 的 conjunctive forms，伴隨 reduced cross-task interference 與行為改善。

這可被 TADC 描述成：

$$
E_{\mathrm{compositional}}
\rightarrow
C_{\mathrm{task-specific}}.
$$

但這只是我們的重新表述。

原研究本身並沒有聲稱存在一個 cognitive contraction operator。

因此：

$$
\boxed{
\text{empirical adjacency}
\neq
\text{operator proof}.
}
$$

---

# 12. 算子三：Traversal \(T\)

Traversal 是六個算子中最保守的一個。

給定 fixed relational structure：

$$
\mathcal C
=
(X,\mathcal R,\kappa,\mathcal N),
$$

從：

$$
x_t
$$

到：

$$
x_{t+1}
$$

若：

$$
(x_t,x_{t+1})\in\mathcal R,
$$

定義：

$$
T:
x_t
\mapsto
x_{t+1}.
$$

---

# 13. Traversal 可以完全不改變空間

若：

$$
X_t=X_{t+1},
$$

$$
\mathcal R_t=\mathcal R_{t+1},
$$

$$
\mathcal N_t=\mathcal N_{t+1},
$$

則：

$$
T
$$

只是：

$$
\boxed{
\text{movement within a fixed cognitive space}.
}
$$

所以：

$$
\boxed{
T\not\Rightarrow ASTC.
}
$$

這一點很重要。

---

# 14. Traversal 與 Task Switching 必須分離

外部 label：

$$
L(x_t)\neq L(x_{t+1})
$$

不必表示：

$$
d_{\mathrm{cog}}(x_t,x_{t+1})
$$

很大。

若：

$$
\kappa(x_t,x_{t+1}\mid G)\gg0,
$$

則表面「跨領域」可能只是：

$$
\boxed{
\text{low-cost traversal}.
}
$$

反之，

即使：

$$
L(x_t)=L(x_{t+1}),
$$

若：

$$
\kappa\approx0,
$$

實際 cognitive reconstruction cost 可能很高。

因此：

$$
\boxed{
\text{task label switch}
\neq
\text{relational traversal distance}.
}
$$

---

# 15. Traversal Path

一條 cognitive path：

$$
\gamma
=
(x_0,x_1,\ldots,x_n).
$$

成本：

$$
K(\gamma)
=
\sum_{i=0}^{n-1}
c(x_i,x_{i+1}\mid G).
$$

若：

$$
c
\propto
-\log\kappa,
$$

則：

$$
K(\gamma)
=
-\sum_i
\log
\kappa(x_i,x_{i+1}\mid G).
$$

高 accessibility 的路徑：

$$
K(\gamma)\downarrow.
$$

因此 switching difficulty 可以轉成：

$$
\boxed{
\text{path-cost problem}.
}
$$

---

# 16. 算子四：Gluing \(G\)

考慮兩個有效 domains：

$$
U_\alpha,
U_\beta.
$$

若：

$$
U_\alpha\cap U_\beta
=
\varnothing
$$

或 overlap 很弱，

但出現 bridge：

$$
B_{\alpha\beta},
$$

則可以建立：

$$
G(
U_\alpha,
U_\beta;
B_{\alpha\beta}
).
$$

暫記：

$$
U_{\alpha\beta}
=
U_\alpha
\cup_B
U_\beta.
$$

---

# 17. Gluing 不是普通 association

單一 edge：

$$
x\leftrightarrow y
$$

不一定足以稱為 domain gluing。

本文要求至少出現：

1. cross-domain transition cost 下降；
2. novel inference 可以跨 bridge 泛化；
3. bridge removal 會破壞這種整合；
4. 兩 domain 的局部行為或 representation 開始形成共享結構。

因此 Gluing 的候選判準為：

$$
\boxed{
\Delta K_{\alpha\beta}<0
}
$$

且：

$$
\boxed{
\Delta I_{\alpha\beta}>0,
}
$$

其中：

$$
I_{\alpha\beta}
$$

表示 cross-domain inference capacity。

---

# 18. Gluing 與 Compositionality

2026 年《Nature》研究顯示，猴子執行多個 compositionally related tasks 時，可跨 tasks 重用共享 neural subspaces，並依 internal belief flexibly engage task-relevant sensory / motor subspaces。

這提供一個非常重要的鄰接事實：

$$
\boxed{
\text{different tasks can share reusable representational components}.
}
$$

但共享 component 不等於 gluing。

TADC 的 Gluing 需要進一步證明：

$$
\text{shared representation}
\rightarrow
\text{new cross-domain accessibility}.
$$

---

# 19. Gluing 與 Chunking

2024 年 working-memory / Hebb-effect 研究顯示，當重複結構透過 grouping 變得可辨識時，long-term chunk formation 會更靈活。

這支持：

$$
\boxed{
\text{grouping can influence what becomes a unified functional representation}.
}
$$

若：

$$
x_1,x_2,\ldots,x_n
$$

被形成：

$$
z=[x_1,\ldots,x_n],
$$

這可以看成一種 local gluing：

$$
G(
x_1,\ldots,x_n
)
=
z.
$$

但 chunking theory 本身可能已完全足夠。

所以 TADC 必須證明「gluing」提供額外預測，否則就應回到 chunking terminology。

---

# 20. 算子五：Detachment \(D\)

Gluing 的反操作不應簡單叫 deletion。

因為認知系統常需要：

> 保留兩個知識區域，但解除它們之間的過強耦合。

因此定義 Detachment：

若：

$$
B_{\alpha\beta}
$$

是：

$$
U_\alpha
$$

與：

$$
U_\beta
$$

間的 bridge set，

則：

$$
D:
\kappa(B_{\alpha\beta})
\downarrow.
$$

在強版本：

$$
B_{\alpha\beta}
\subseteq
\mathcal R_t
$$

被移除：

$$
B_{\alpha\beta}
\not\subseteq
\mathcal R_{t+1}.
$$

---

# 21. Detachment 不等於忘掉內容

假設：

$$
U_\alpha
$$

和：

$$
U_\beta
$$

仍完整存在：

$$
U_\alpha,U_\beta\subseteq X_{t+1}.
$$

只是：

$$
\kappa(U_\alpha,U_\beta)
\downarrow.
$$

這可以表示：

- 發現原 analogy 無效；
- 修正錯誤因果關係；
- context separation；
- pattern separation；
- 消除 interference；
- 把過度 generalization 拆開。

因此：

$$
\boxed{
D
=
\text{decoupling},
}
$$

不是：

$$
\boxed{
D
=
\text{memory deletion}.
}
$$

---

# 22. Detachment 與 Cognitive Differentiation

學習早期，兩個 contexts 可能共享大量表示：

$$
U_A\approx U_B.
$$

隨著熟練：

$$
U_A
$$

與：

$$
U_B
$$

逐漸形成 task-specific conjunctive representations。

這可以候選地描述為：

$$
D(U_A,U_B)
$$

增加。

2025 年 compositional-to-conjunctive task-learning 研究與 practice reshaping representational geometry 的結果都與這種 specialization / differentiation 相容。

但同樣：

$$
\boxed{
\text{differentiation evidence}
\neq
\text{Detachment primitive proven}.
}
$$

---

# 23. 算子六：Re-indexing \(R\)

Re-indexing 是整套系統中最容易被誤解的一個。

假設：

$$
D
=
\{x_1,x_2,\ldots,x_n\}.
$$

在高解析度：

$$
R_{\mathrm{fine}}(D)
=
\{x_1,\ldots,x_n\}.
$$

在粗解析度：

$$
R_{\mathrm{coarse}}(D)
=
z_D.
$$

也就是：

$$
\boxed{
\text{a domain becomes one object}.
}
$$

反過來：

$$
z_D
\rightarrow
D
$$

則：

$$
\boxed{
\text{an object unfolds into a domain}.
}
$$

---

# 24. Re-indexing 不必改變底層結構

這一點要非常嚴格。

可能：

$$
\mathcal R
$$

完全沒改變。

只改：

$$
\phi
$$

和：

$$
\lambda.
$$

所以：

$$
\boxed{
R
\not\Rightarrow
\text{structural transformation}.
}
$$

它可以只是：

$$
\boxed{
\text{representational coarse-graining / refinement}.
}
$$

---

# 25. Re-indexing 與 Hierarchical Control

2026 年 hierarchical cognitive-control 研究將 abstract context reconfiguration 與 subordinate task-set reconfiguration 分開，顯示不同階層具有不同 neural reconfiguration 與 behavioral costs。

這提供：

$$
\boxed{
\text{different levels of task representation
are behaviorally and neurally distinguishable}.
}
$$

TADC 的更強命題是：

> cognition 是否能把原本的 lower-level structure 壓成一個 high-level unit，再按需要展開？

這需要另外的 re-indexing experiment。

---

# 26. Re-indexing 與 Nested Cognitive Maps

2025 年 nested-space cognitive-map 研究顯示：

$$
\text{subspace}
\subset
\text{larger space}
$$

具有可辨認的 hierarchical organization。

這讓：

$$
\boxed{
\text{domain-as-object}
}
$$

不再只是純哲學想像。

但是 spatial subspace representation 仍不是一般 cognition 的 re-indexing 證明。

---

# 27. 六算子的最小形式

把六個算子集中：

## Expansion

$$
E:
(X,\mathcal R,\kappa)
\mapsto
(X',\mathcal R',\kappa')
$$

其中候選：

$$
X\subseteq X'
$$

或：

$$
\operatorname{Reach}(X)
\subset
\operatorname{Reach}(X').
$$

---

## Contraction

$$
C:
(X,\mathcal R,\kappa)
\mapsto
(X',\mathcal R',\kappa')
$$

其中：

$$
X'\subseteq X
$$

或可達區域縮小。

---

## Traversal

$$
T:
(x,\mathcal C)
\mapsto
(y,\mathcal C).
$$

---

## Gluing

$$
G:
(U,V)
\mapsto
U\cup_BV.
$$

---

## Detachment

$$
D:
(U\cup_BV)
\mapsto
(U,V)
$$

或更弱：

$$
\kappa(B)\downarrow.
$$

---

## Re-indexing

$$
R_\lambda:
\mathfrak A^{(\lambda_1)}
\mapsto
\mathfrak A^{(\lambda_2)}.
$$

---

# 28. Identity Operator

加入：

$$
I:
\mathcal C
\mapsto
\mathcal C.
$$

這不是第七個 cognitive operator，

而是數學上的 no-op reference。

任何 candidate operator：

$$
O
$$

應滿足：

$$
I\circ O
=
O\circ I
=
O.
$$

這讓後續 operator algebra 有基準。

---

# 29. 算子一般不是可逆的

例如：

$$
C(E(U))
$$

不保證回到：

$$
U.
$$

因為 expansion 後可能形成新 relation：

$$
\mathcal R'.
$$

即使把新增 objects 移除，

原 domain internal weights 已可能改變。

因此：

$$
\boxed{
C\neq E^{-1}
}
$$

一般成立。

同樣：

$$
D\neq G^{-1}.
$$

---

# 30. Non-commutativity Conjecture

本文提出：

## Operator Non-Commutativity Conjecture（ONC）

對至少部分：

$$
O_i,O_j\in\mathcal O,
$$

有：

$$
\boxed{
O_i\circ O_j
\neq
O_j\circ O_i.
}
$$

例如：

$$
E\circ C
\neq
C\circ E.
$$

先砍掉低 relevance 分支，再展開：

$$
C\rightarrow E
$$

與先廣泛探索再收斂：

$$
E\rightarrow C
$$

可能得到不同結果。

---

# 31. Gluing / Detachment 也可能非交換

先：

$$
G(U,V)
$$

建立 shared schema，

再：

$$
D
$$

切斷某個錯誤 bridge，

可能保留其他 shared structure。

而先：

$$
D
$$

解除原有關係，

再：

$$
G
$$

可能形成完全不同 bridge。

因此：

$$
\boxed{
D\circ G
\neq
G\circ D.
}
$$

---

# 32. Re-indexing 會改變其他算子的結果

在 coarse scale：

$$
R_c(U)=z.
$$

若直接 Expansion：

$$
E(z)
$$

可能只找到 domain-level neighbors。

但在 fine scale：

$$
R_f(z)=\{x_1,\ldots,x_n\},
$$

再：

$$
E
$$

可能從某個：

$$
x_i
$$

找到新的局部 bridge。

因此：

$$
\boxed{
E\circ R_c
\neq
R_c\circ E
}
$$

在一般情況成立。

也就是：

$$
\boxed{
\text{what you can discover depends on resolution}.
}
$$

---

# 33. Path Dependence

若：

$$
\omega_1
=
E\circ G\circ C,
$$

而：

$$
\omega_2
=
C\circ G\circ E,
$$

即使：

$$
\omega_1
$$

與：

$$
\omega_2
$$

使用相同算子集合，

仍可能：

$$
\omega_1(\mathcal C_0)
\neq
\omega_2(\mathcal C_0).
$$

因此 cognition state 不只取決於：

$$
\{E,G,C\},
$$

還取決於：

$$
\boxed{
\text{operator order}.
}
$$

---

# 34. History Dependence

更強地：

$$
\mathcal C_{t+1}
=
\Phi(
\mathcal C_t,
O_t,
H_t
),
$$

其中：

$$
H_t
=
(O_1,O_2,\ldots,O_{t-1})
$$

是 operation history。

如果：

$$
\mathcal C_t^{(1)}
=
\mathcal C_t^{(2)}
$$

表面狀態相同，

但不同 history：

$$
H_t^{(1)}
\neq
H_t^{(2)}
$$

導致：

$$
\mathcal C_{t+1}^{(1)}
\neq
\mathcal C_{t+1}^{(2)},
$$

則存在：

$$
\boxed{
\text{cognitive hysteresis}.
}
$$

這是未來非常值得測的強命題。

---

# 35. Cognitive Hysteresis

例如一個 relation：

$$
x\leftrightarrow y
$$

曾經被強烈 Gluing，

之後 Detachment。

即使最後測得：

$$
\kappa(x,y)
$$

回到 baseline，

未來再次暴露 bridge 時，

重新 Gluing 的速度可能比完全沒學過的人快。

也就是：

$$
\boxed{
\text{same observable state}
\neq
\text{same latent history}.
}
$$

這與 memory savings / relearning literature 可能高度相關，

但 TADC 必須避免把所有 savings 都重新命名成 hysteresis。

---

# 36. Operator Cost

每個算子都有成本：

$$
K_O.
$$

例如：

$$
K_E
=
\text{search + retrieval + evaluation cost},
$$

$$
K_C
=
\text{selection + inhibition cost},
$$

$$
K_T
=
\text{transition cost},
$$

$$
K_G
=
\text{integration + translation cost},
$$

$$
K_D
=
\text{conflict resolution + unlearning / separation cost},
$$

$$
K_R
=
\text{abstraction / decomposition cost}.
$$

因此 cognition 不是只最大化可達空間。

更合理：

$$
\boxed{
\text{choose operator sequence}
\quad
\text{subject to cognitive cost}.
}
$$

---

# 37. Operator Utility

定義：

$$
U(O_t)
=
\Delta V_t
-
\lambda_KK_{O_t},
$$

其中：

$$
\Delta V_t
$$

是 operator 對目前 goal 的 expected information / performance gain。

所以：

$$
O_t^*
=
\arg\max_O
U(O).
$$

這只是一個 candidate control model。

若資料顯示 operator choice 與 utility 無關，

就需要別的 control mechanism。

---

# 38. Expansion–Contraction Cycle

一個自然的 search cycle：

$$
E
\rightarrow
E
\rightarrow
C
\rightarrow
T
\rightarrow
E
\rightarrow
C.
$$

前半：

$$
\text{increase possibility space}.
$$

後半：

$$
\text{reduce candidate set}.
$$

這和 exploration–exploitation literature 有概念相似性，

但不是同義詞。

Expansion / Contraction 操作的是：

$$
\text{effective cognitive domain}.
$$

exploration / exploitation 通常操作：

$$
\text{policy over actions / options}.
$$

兩者可交叉，

不能直接等同。

---

# 39. Gluing–Detachment Cycle

另一種：

$$
G
\rightarrow
T
\rightarrow
G
\rightarrow
D.
$$

先發現：

$$
U_A\leftrightarrow U_B,
$$

利用 bridge 推理，

再發現某部分 analogy 不可靠，

因此：

$$
D.
$$

這表示：

$$
\boxed{
\text{cross-domain cognition}
\neq
\text{ever-increasing integration}.
}
$$

成熟系統也必須能拆掉錯誤整合。

---

# 40. Re-indexing–Traversal Cycle

在 high-level：

$$
R_c
\rightarrow
T
$$

快速在 domains 間移動。

遇到問題：

$$
R_f
$$

把某 domain 展開，

在內部：

$$
T\rightarrow T\rightarrow E,
$$

完成後：

$$
R_c
$$

重新壓縮。

這提供一個候選解釋：

$$
\boxed{
\text{how cognition can switch rapidly at high level
without processing every detail each time}.
}
$$

---

# 41. 與 Working Memory Chunking 的關係

2024 年 Musfeld 等人顯示：

當 repeated information 的 grouping 被做得更顯著，

long-term chunk formation 會更靈活。

這可以被 TADC 表示：

$$
\text{Grouping}
\rightarrow
G
\rightarrow
R_c.
$$

即：

先把元素 Gluing，

再將整個 chunk Re-index 成一個 unit。

但如果：

$$
\text{chunking theory}
$$

已能完整預測行為，

則 TADC 不應主張自己發現了新的機制。

TADC 的增量必須是：

> 同一套 operator language 能否跨 chunking、task reconfiguration、domain integration 與 resolution change 提供統一可測預測？

---

# 42. 與 Compositional Neural Subspaces 的關係

2026 Tafazoli 等人的研究顯示，shared neural subspaces 可跨多個 tasks 重用，並依 task belief flexibly engage。

對 TADC 而言，這提供：

$$
\boxed{
\text{reusable local representational components exist}.
}
$$

若一個 task 是：

$$
U_A+U_B+U_C
$$

的 composition，

另一個 task：

$$
U_A+U_D,
$$

則：

$$
G
$$

與：

$$
R
$$

可能提供一種 coarse-grained operator description。

但 neural subspace composition 並不自動證明 cognitive domain gluing。

---

# 43. 與 Practice-Driven Geometry Change 的關係

2025 EEG study 顯示 practice 會重新塑造 task-tailored representational geometry；高階 context-specific conjunctions 的增強與 performance improvement、switch-cost reduction 相關。

這與：

$$
\boxed{
C
+
D
+
R
}
$$

可能相容：

- Contraction：移除冗餘 dimensions；
- Detachment：降低 cross-context interference；
- Re-indexing：更高階 conjunctive state 成為有效 unit。

但這只是候選映射。

真正模型比較需要：

$$
M_{\mathrm{standard}}
$$

vs

$$
M_{\mathrm{SOCTS}}.
$$

---

# 44. Operator Observables

為使六算子可測，定義候選 observable。

## Expansion

$$
\Delta |\operatorname{Reach}^{(k)}|>0.
$$

---

## Contraction

$$
\Delta |\operatorname{Reach}^{(k)}|<0.
$$

或 irrelevant-transition probability 降低。

---

## Traversal

$$
x_i\rightarrow x_j
$$

且 structural distance 不變。

---

## Gluing

$$
\Delta K_{\alpha\beta}<0,
$$

$$
\Delta I_{\alpha\beta}>0.
$$

---

## Detachment

$$
\Delta K_{\alpha\beta}>0
$$

對特定錯誤 / irrelevant bridge，

同時 within-domain performance 不下降。

---

## Re-indexing

同一結構在不同 task conditions 下：

$$
\text{unit-level representation}
\leftrightarrow
\text{substructure-level representation}.
$$

---

# 45. Operator Identification Problem

給一條行為 trajectory：

$$
Y
=
(y_1,\ldots,y_T),
$$

我們想反推：

$$
\omega
=
(O_1,\ldots,O_n).
$$

也就是：

$$
P(
\omega
\mid
Y
).
$$

如果多個 operator sequences 都能產生相同資料：

$$
P(\omega_1\mid Y)
\approx
P(\omega_2\mid Y),
$$

則 operator identification 不可辨識。

因此未來實驗必須主動設計：

$$
\boxed{
\text{operator-discriminating conditions}.
}
$$

---

# 46. 實驗一：Expansion vs Traversal

建立固定 graph：

$$
\mathcal G_0.
$$

Condition T：

participant 只能在已知 edges 上 navigation。

Condition E：

提供相同 exposure，但要求尋找 latent relation / novel bridge。

之後比較：

$$
\operatorname{Reach}^{(k)}.
$$

若 E condition 只增加已知 node activation，

而沒有新 route / inference，

則只是 Traversal / Reweighting。

---

# 47. 實驗二：Contraction

給一個含大量 irrelevant relations 的 task graph。

要求 participants 在訓練後快速完成 specific goal。

若 effective transitions：

$$
P(\text{irrelevant path})
\downarrow
$$

而：

$$
P(\text{goal path})
\uparrow,
$$

可以估計 Contraction。

但需要與：

$$
\text{simple inhibition}
$$

模型競爭。

---

# 48. 實驗三：Gluing

先獨立學：

$$
U_A,U_B.
$$

兩者 exposure 相同。

Experimental group 額外注意：

$$
B_{AB}.
$$

Control group 看過 bridge stimuli，

但不處理其 relational role。

之後測：

- cross-domain inference；
- spontaneous transition；
- transfer；
- neural / behavioral similarity geometry。

如果：

$$
G_{\mathrm{rel}}
>
G_{\mathrm{exposure}},
$$

支持 attention-mediated Gluing。

---

# 49. 實驗四：Detachment

先人工建立：

$$
U_A\leftrightarrow U_B
$$

的 association。

接著提供 evidence：

$$
R_{AB}
$$

只在 context：

$$
C_1
$$

有效，

在：

$$
C_2
$$

無效。

測 participants 是否能：

$$
D_{C_2}
$$

而保留：

$$
G_{C_1}.
$$

這是一個非常強的 test：

$$
\boxed{
\text{context-selective detachment}.
}
$$

---

# 50. 實驗五：Re-indexing

使用 hierarchical graph：

$$
x_{ijk}.
$$

要求在不同 blocks 中：

1. item-level decision；
2. cluster-level decision；
3. meta-cluster decision。

測：

- representational geometry；
- RT；
- switch costs；
- decoding level；
- transfer。

若同一 representation 可隨 instruction：

$$
x
\leftrightarrow
U_x
$$

切換 object / domain role，

支持 Re-indexing。

---

# 51. 實驗六：Non-commutativity

建立兩組。

Group 1：

$$
E\rightarrow C.
$$

Group 2：

$$
C\rightarrow E.
$$

兩組：

- total exposure；
- task time；
- stimuli；
- reward；

全部匹配。

若終態：

$$
\mathcal C_{EC}
\neq
\mathcal C_{CE},
$$

且差異可重現，

支持：

$$
\boxed{
EC\neq CE.
}
$$

---

# 52. 實驗七：Operator History / Hysteresis

兩組最後都訓練到：

$$
\kappa_{AB}=\kappa_0.
$$

但：

Group 1 曾經：

$$
G\rightarrow D.
$$

Group 2 從未 Gluing。

再次暴露 bridge：

$$
B_{AB}.
$$

若：

$$
\tau_{\mathrm{re-glue}}^{(1)}
<
\tau_{\mathrm{glue}}^{(2)},
$$

說明相同 observable state 下 history 仍影響動態。

這可支持 hysteresis，

但必須與 savings / latent memory models 比較。

---

# 53. 七個可證偽命題

## SOCTS-H1 — Expansion Distinct from Traversal

存在條件使：

$$
\Delta\operatorname{Reach}^{(k)}>0
$$

不能由固定 graph traversal 解釋。

---

## SOCTS-H2 — Contraction Is Structured

Contraction 應 preferentially 移除 low-goal-value paths，

不是全局 activation 下降。

---

## SOCTS-H3 — Gluing Produces Transfer

Gluing 必須增加：

$$
\text{novel cross-domain inference},
$$

不只是 pairwise familiarity。

---

## SOCTS-H4 — Detachment Can Be Selective

錯誤 bridge 可降低，

但其 constituent domains 仍保持可用。

---

## SOCTS-H5 — Re-indexing Changes Effective Objecthood

同一結構可依 resolution 表現：

$$
\text{object}
\leftrightarrow
\text{domain}.
$$

---

## SOCTS-H6 — Operator Order Matters

至少一組：

$$
O_iO_j\neq O_jO_i.
$$

---

## SOCTS-H7 — Operator Model Adds Prediction

SOCTS 對 unseen behavior / neural data 的預測：

$$
P_{\mathrm{SOCTS}}
$$

必須優於更簡單：

- activation；
- task-switch；
- learning；
- chunking；
- semantic association；

模型。

---

# 54. 何種結果會使六算子失敗？

## F1 — Operators Collapse

若：

$$
E,C,G,D
$$

都可化約為：

$$
\text{one generic weight-update operator},
$$

六算子過度細分。

---

## F2 — Traversal Is Enough

若所有 apparent structural change 都能由：

$$
\text{fixed graph + traversal + reweighting}
$$

解釋，

ASTC-S 與 SOCTS structural operators 不成立。

---

## F3 — Gluing Adds Nothing Beyond Association / Chunking

若：

$$
G
$$

沒有額外 predictive signature，

直接用：

$$
\text{association / chunking}
$$

即可。

---

## F4 — Detachment Adds Nothing Beyond Inhibition / Extinction

若：

$$
D
$$

無法和 inhibition、extinction、context gating 分離，

應刪除。

---

## F5 — Re-indexing Is Analyst-Only

如果「object ↔ domain」只存在於研究者重新畫圖，

participants 沒有行為 / neural evidence，

則：

$$
R
$$

不是 cognitive operator。

---

## F6 — Operator Order Does Not Matter

若所有 operator pairs 都近似交換：

$$
O_iO_j
\approx
O_jO_i,
$$

那麼非交換 operator algebra 沒有必要。

---

## F7 — History Adds No Information

若：

$$
P(
\mathcal C_{t+1}
\mid
\mathcal C_t,H_t
)
=
P(
\mathcal C_{t+1}
\mid
\mathcal C_t
),
$$

則 history dependence / hysteresis 應放棄。

---

# 55. 六算子與注意力的關係

一個關鍵修正：

$$
\boxed{
\text{TADC operator}
\neq
\text{attention itself}.
}
$$

注意 configuration：

$$
a_t
$$

比較像控制變量。

算子：

$$
O_t
$$

是 state-space operation。

所以可以寫：

$$
P(O_t\mid a_t,G_t,m_t,e_t).
$$

注意可能：

- 提高某 operator 被選中的概率；
- 改變 operator 的作用強度；
- 改變 operator target；
- 改變停止條件。

因此：

$$
\boxed{
\text{attention controls transformations;
it need not be identical to them}.
}
$$

---

# 56. Operator Target

每個 operator 還需要 target：

$$
O_t[\Omega_t].
$$

例如：

$$
E[U_A],
$$

$$
C[U_B],
$$

$$
G[U_A,U_C],
$$

$$
D[B_{AB}],
$$

$$
R[U_D,\lambda].
$$

所以完整 action：

$$
a_t
=
(O_t,\Omega_t,\eta_t),
$$

其中：

$$
\eta_t
$$

是 operator intensity / threshold。

---

# 57. Operator Stopping Rule

沒有停止條件的 Expansion：

$$
E^\infty
$$

不合理。

因此每個 operator 要有：

$$
S_O.
$$

例如 Expansion：

$$
S_E:
\Delta I
<
\epsilon
$$

停止。

Contraction：

$$
S_C:
P_{\mathrm{goal}}
\geq
\theta.
$$

Gluing：

$$
S_G:
K_{\alpha\beta}
\leq
K^*.
$$

Detachment：

$$
S_D:
\text{false-transfer rate}
\leq
\epsilon.
$$

這讓 SOCTS 更接近可執行控制模型。

---

# 58. Operator Budget

給定總認知資源：

$$
B.
$$

operator sequence 需滿足：

$$
\sum_t
K_{O_t}
\leq
B.
$$

因此：

$$
\boxed{
\text{cognitive strategy}
=
\text{operator planning under budget}.
}
$$

這可能與 bounded rationality、resource-rational cognition 接軌，

但本文暫不主張等價。

---

# 59. Attention Topology as Operator-Induced Structure

若未來真的能建立拓樸語言，

則拓樸可能不是固定給定：

$$
(X,\tau).
$$

而可能由 operator history 生成：

$$
\tau_t
=
\Gamma(
O_{1:t},
G_t,
m_t,
e_t
).
$$

也就是：

$$
\boxed{
\text{topology as an induced history-dependent structure}.
}
$$

這是 TADC 比固定 cognitive-map model 更激進的地方。

目前仍只是強猜想。

---

# 60. Operator Invariants

真正的拓樸研究最終不能只看變化，

還要問：

> 什麼在變化中保持？

候選 invariant：

- task goal identity；
- relational motif；
- causal ordering；
- component count；
- bridge role；
- equivalence class；
- high-level solution structure。

若：

$$
R
$$

改變解析度，

但某 structural relation：

$$
I(\mathcal C)
$$

保持：

$$
I(
R(\mathcal C)
)
=
I(\mathcal C),
$$

這才開始接近真正的 invariant。

TADC-04 會從 observation scale 進一步處理這件事。

---

# 61. 六算子並不保證完整

SOCTS 目前的 completeness 只是：

$$
\boxed{
\text{working completeness},
}
$$

不是 theorem。

未來可能需要：

### Duplication

$$
Q(U)
=
U^{(1)}+U^{(2)}
$$

同一 structure 被複製到不同 context。

### Rotation / Reparameterization

不改 domain membership，

只改 internal coordinate basis。

### Fusion

比 Gluing 更強，

兩 domain 形成不可再分的新 unit。

### Forgetting / Decay

非目標導向、非 operator-controlled 的自然消退。

因此：

$$
\boxed{
\mathcal O
=
\{E,C,T,G,D,R\}
}
$$

目前只是最小候選集。

---

# 62. 為什麼先保留六個？

因為它們對應六個不同問題：

1. **Expansion：** 還能把什麼納入？
2. **Contraction：** 目前應排除什麼？
3. **Traversal：** 在既有關係中往哪走？
4. **Gluing：** 哪些區域應建立橋樑？
5. **Detachment：** 哪些橋樑應拆除？
6. **Re-indexing：** 現在應把什麼視為「一個單位」？

這六個問題同時涉及：

$$
\boxed{
\text{search},
\text{selection},
\text{movement},
\text{integration},
\text{separation},
\text{scale}.
}
$$

它們至少構成一個具有研究價值的操作基底。

---

# 63. 與前兩篇的統一

TADC-01 問：

$$
\boxed{
\text{Can cognitive accessibility structure change?}
}
$$

TADC-02 問：

$$
\boxed{
\text{Can effective domains be dynamically induced?}
}
$$

TADC-03 現在問：

$$
\boxed{
\text{By which candidate operations can such change occur?}
}
$$

所以三篇合起來：

$$
\boxed{
\mathcal C_t
\overset{\mathcal O}{\longrightarrow}
\mathcal C_{t+1}
}
$$

以及：

$$
\boxed{
\mathfrak A_t
\overset{\mathcal O}{\longrightarrow}
\mathfrak A_{t+1}.
}
$$

---

# 64. 最小動力學

定義 operator selector：

$$
\pi_t
=
\pi(
O_t
\mid
\mathcal C_t,
G_t,
a_t,
m_t,
e_t,
B_t
).
$$

狀態更新：

$$
\mathcal C_{t+1}
=
O_t[
\Omega_t;
\eta_t
]
(
\mathcal C_t
).
$$

其中：

- \(O_t\)：operator type；
- \(\Omega_t\)：target；
- \(\eta_t\)：strength / threshold；
- \(B_t\)：resource budget。

因此完整最小模型：

$$
\boxed{
O_t
\sim
\pi(
\cdot
\mid
\mathcal C_t,G_t,a_t,m_t,e_t,B_t
)
}
$$

$$
\boxed{
\mathcal C_{t+1}
=
O_t(
\mathcal C_t
).
}
$$

---

# 65. Operator Sequence as Cognitive Strategy

一條完整策略：

$$
\Sigma
=
(
O_1,\Omega_1,\eta_1;
\ldots;
O_n,\Omega_n,\eta_n
).
$$

因此兩個人即使具有：

$$
\mathcal C_0^{(1)}
=
\mathcal C_0^{(2)}
$$

也可能因：

$$
\Sigma_1
\neq
\Sigma_2
$$

得到：

$$
\mathcal C_f^{(1)}
\neq
\mathcal C_f^{(2)}.
$$

這讓「認知風格」有一種新的候選形式：

$$
\boxed{
\text{cognitive style}
=
\text{distribution over operator policies}.
}
$$

但本文不進一步做人群分類。

---

# 66. 結論

本文建立：

$$
\boxed{
\textbf{SOCTS}
}
$$

即：

**Six-Operator Cognitive Transformation System**。

六個候選算子為：

$$
\boxed{
\mathcal O
=
\{
E,C,T,G,D,R
\}.
}
$$

分別表示：

$$
\boxed{
\text{Expansion}
}
$$

$$
\boxed{
\text{Contraction}
}
$$

$$
\boxed{
\text{Traversal}
}
$$

$$
\boxed{
\text{Gluing}
}
$$

$$
\boxed{
\text{Detachment}
}
$$

$$
\boxed{
\text{Re-indexing}.
}
$$

本文最重要的三個限制是：

第一：

$$
\boxed{
\text{not every operator changes topology}.
}
$$

Traversal 可以完全存在於固定空間中；

Re-indexing 也可能只改表示尺度。

第二：

$$
\boxed{
\text{operators are candidate descriptions,
not proven neural primitives}.
}
$$

如果 learning、chunking、task switching、inhibition、semantic association 等傳統模型就足夠，

SOCTS 應被壓縮。

第三：

$$
\boxed{
\text{operator order may matter}.
}
$$

本文因此提出：

$$
\boxed{
O_iO_j
\neq
O_jO_i
}
$$

的 Operator Non-Commutativity Conjecture，

以及：

$$
\boxed{
\mathcal C_{t+1}
=
\Phi(
\mathcal C_t,
O_t,
H_t
)
}
$$

的 history dependence / cognitive hysteresis 猜想。

若這些命題成立，

注意力研究就不只需要描述：

> 現在注意哪個對象？

還需要描述：

> **現在對認知空間執行哪一種操作？**

而一個完整高階認知 episode，

可能不是：

$$
x_1\rightarrow x_2\rightarrow x_3,
$$

而是：

$$
\boxed{
E
\rightarrow
T
\rightarrow
G
\rightarrow
R
\rightarrow
C
\rightarrow
D
\rightarrow
E
\rightarrow\cdots
}
$$

所生成的一條歷史依賴結構演化。

這就是 TADC-03 對前兩篇的真正推進。

---

# 參考文獻

1. Leach SC, Chen X, Hwang K. **Hierarchical Reconfiguration of Neurocognitive Task Set Representations Mediates Cognitive Flexibility.** *Journal of Neuroscience*. 2026. doi:10.1523/JNEUROSCI.0113-26.2026. PMID: 42276789.  
2. Tafazoli S, Bouchacourt FM, Ardalan A, et al. **Building compositional tasks with shared neural subspaces.** *Nature*. 2026;650(8100):164–172. doi:10.1038/s41586-025-09805-2. PMID: 41299181.  
3. Mill RD, Cole MW. **Dynamically shifting from compositional to conjunctive brain representations supports cognitive task learning.** *Nature Communications*. 2025;16:10084. doi:10.1038/s41467-025-65041-2. PMID: 41253771.  
4. Musfeld P, Dutli J, Oberauer K, Bartsch LM. **Grouping in working memory guides chunk formation in long-term memory: Evidence from the Hebb effect.** *Cognition*. 2024;248:105795. doi:10.1016/j.cognition.2024.105795. PMID: 38669793.  
5. Greco A, Moser J, Preissl H, Siegel M. **Predictive learning shapes the representational geometry of the human brain.** *Nature Communications*. 2024;15:9670. doi:10.1038/s41467-024-54032-4. PMID: 39516221.  
6. Peer M, Epstein RA. **Cognitive maps for hierarchical spaces in the human brain.** *Cerebral Cortex*. 2025;35(9):bhaf261. doi:10.1093/cercor/bhaf261. PMID: 40982478.  
7. Tan L, Qiu Y, Qiu L, et al. **The medial and lateral orbitofrontal cortex jointly represent the cognitive map of task space.** *Communications Biology*. 2025;8:163. doi:10.1038/s42003-025-07588-w. PMID: 39900714.  
8. Qiu Y, Li H, Liao J, et al. **Forming cognitive maps for abstract spaces: the roles of the human hippocampus and orbitofrontal cortex.** *Communications Biology*. 2024;7:517. doi:10.1038/s42003-024-06214-5. PMID: 38693344.  
9. Bhandari A, et al. **Practice reshapes the geometry and dynamics of task-tailored representations.** *Cerebral Cortex*. 2025;35(8):bhaf125. PMID: 40882180.  
10. Baram AB, Nili H, Barreiros I, et al. **An abstract relational map emerges in the human medial prefrontal cortex with consolidation.** *Current Biology*. 2026;36(13):3315–3325.e4. PMID: 42341750.  
11. Qiu Y, et al. **Dynamic changes in orbitofrontal-hippocampal connectivity linked to cognitive map formation in humans.** *NeuroImage*. 2025;121415. PMID: 40780573.  
12. Garvert MM, Dolan RJ, Behrens TEJ. **A map of abstract relational knowledge in the human hippocampal-entorhinal cortex.** *eLife*. 2017;6:e17086. doi:10.7554/eLife.17086.  
13. Park SA, Miller DS, Nili H, Ranganath C, Boorman ED. **Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps.** *Neuron*. 2020;107(6):1226–1238.e8. doi:10.1016/j.neuron.2020.06.030.  
14. Behrens TEJ, Muller TH, Whittington JCR, et al. **What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior.** *Neuron*. 2018;100(2):490–509. doi:10.1016/j.neuron.2018.10.002.  

---

## 與系列的關係

**已完成：**

- TADC-01：《注意力不是單點選擇——可變認知空間與注意—空間轉換猜想》
- TADC-02：《動態認知域——領域作為局部座標圖》
- TADC-03：《拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引》

**下一篇：**

- TADC-04：《嵌套注意域與觀察尺度》

後續：

- TADC-05：《從單點超專注到拓樸超專注》
- TADC-06：《關係優先認知與跨域連續性》
- TADC-07：《外部認知支架與人—AI 認知拓樸》
- TADC-08：《拓樸注意力的測量、反證與工程化》

---

**狀態：** TADC-03 v0.1  
**原始人體／臨床數據：** 無  
**理論狀態：** 猜想／研究綱領；未經實驗驗證  
**算子狀態：** 候選形式操作；尚未證明為完備、獨立或神經 primitive  
**拓樸狀態：** 尚未建立嚴格 topological operator algebra
