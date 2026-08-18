# TADC-02：動態認知域——領域作為局部座標圖

**英文題名：** Dynamic Cognitive Domains: Domains as Induced Local Charts of Cognitive Space  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-02  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論命題／形式化研究綱領／可證偽模型  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

TADC-01 提出了可變認知空間猜想（VCSC）與注意—空間轉換猜想（ASTC）：高階認知可能不只是於既有候選集合中移動注意，而會改變未來哪些認知對象、關係與路徑成為有效可達。

本文進一步處理一個更基礎的問題：

> **如果認知空間可以動態改變，那「領域」究竟是什麼？**

傳統描述經常預先給定領域，例如 mathematics、psychology、AI、biology，然後把跨領域思考表示為：

$$
D_i\rightarrow D_j.
$$

本文提出另一種可能：外部學科分類未必等於主體實際使用的認知邊界。對認知系統而言，一個有效 domain 可能由當前目標、關係結構、可達性門檻與觀察解析度共同誘導，而非作為固定 partition 先驗存在。

本文提出三個核心猜想：

1. **Domain Induction Conjecture（DIC）**：有效認知域由 goal-conditioned relational accessibility 動態誘導；
2. **Overlapping Domain Conjecture（ODC）**：有效認知域一般不必形成互斥 partition，而更可能形成可重疊 cover；
3. **Boundary Relativity Conjecture（BRC）**：所謂 domain boundary 依賴目標、時間與解析尺度，因此 macro / micro 與 intra-domain / cross-domain 具有觀察者與解析度相對性。

為描述局部認知域，本文引入「局部座標圖」語言。對有效認知域 \(U_\alpha\)，以：

$$
(U_\alpha,\phi_\alpha)
$$

表示其局部 chart，其中 \(\phi_\alpha\) 將高維、異質的關係結構映射到當前任務可操作的有限座標。本文明確聲明：在尚未證明 \(X\) 為拓樸流形、\(\phi_\alpha\) 為 homeomorphism 或 transition maps 滿足相應條件之前，「chart」是具有形式約束的建模裝置，而非宣稱認知空間已構成 smooth manifold。

現有研究已顯示人類能建立 abstract cognitive maps、task-relevant spaces、nested hierarchical maps，以及依 task structure 調整 neural representational geometry。這些結果支持「認知結構具有目標依賴、階層與局部幾何」的鄰接命題，但尚未證明本文的 DIC / ODC / BRC。

本文最後建立固定領域 partition、單一 latent semantic space、task-set mixture 等競爭模型，並提出 goal-remapping、cross-disciplinary distance、overlap transition、boundary perturbation 與 hierarchical re-indexing 五類實驗，使「動態認知域」可以被實證否定。

**關鍵詞：** cognitive domain；cognitive map；task space；local chart；relational cognition；hierarchical representation；context dependence；cognitive boundary；dynamic domain；TADC

---

# 0. 邊界聲明

本文不是神經疾病模型、人格分類、臨床工具或個人認知評估。

本文也不主張：

$$
\boxed{
\text{academic disciplines are unreal}.
}
$$

學科分類具有制度、歷史、教育、方法論與知識管理功能。

本文處理的是另一個問題：

$$
\boxed{
\text{external disciplinary partition}
\stackrel{?}{=}
\text{internal cognitive partition}.
}
$$

本文的答案是一個待驗證猜想：

$$
\boxed{
\text{not necessarily}.
}
$$

同時，本文不宣稱：

$$
\boxed{
\text{cognitive domains form a differentiable manifold}.
}
$$

「chart」「atlas」「overlap」等語言目前作為形式化研究工具使用；後續若不能建立可測 neighborhood、transition structure 與 invariants，必須降級或改名。

---

# 1. 從 TADC-01 出發

TADC-01 定義時間 \(t\) 的最小認知結構：

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

其中：

- \(X_t\)：有效 cognitive objects；
- \(\mathcal R_t\)：typed relations；
- \(\kappa_t(x,y\mid G_t)\)：goal-conditioned accessibility；
- \(\mathcal N_t\)：neighborhood system；
- \(A_t\)：active set；
- \(G_t\)：goal / high-level context。

TADC-01 主要問：

$$
\mathcal C_t
\rightarrow
\mathcal C_{t+1}
$$

是否可能受 attention configuration 因果影響。

但這裡仍留下：

> 在 \(\mathcal C_t\) 中，一個「領域」應該如何定義？

如果我們一開始就把：

$$
X_t
=
D_1\sqcup D_2\sqcup\cdots\sqcup D_n
$$

固定分割，

就等於在理論尚未開始前，先假定 domain boundary 已經存在。

本文拒絕直接做這個假定。

---

# 2. 外部領域與有效認知域

定義外部分類：

$$
\Pi^{\mathrm{ext}}
=
\{
D_1^{\mathrm{ext}},
D_2^{\mathrm{ext}},
\ldots,
D_m^{\mathrm{ext}}
\}.
$$

例如：

$$
D_1^{\mathrm{ext}}
=
\text{mathematics},
$$

$$
D_2^{\mathrm{ext}}
=
\text{cognitive science},
$$

$$
D_3^{\mathrm{ext}}
=
\text{AI}.
$$

這是一個由社會、學術制度或資料分類系統提供的 partition / taxonomy。

但是主體在處理某一問題時真正使用的有效關係可能是：

$$
x_{\mathrm{math}}
\mathrel{R^{\mathrm{struct}}}
y_{\mathrm{AI}}
\mathrel{R^{\mathrm{control}}}
z_{\mathrm{cognition}}.
$$

若：

$$
\kappa_t
(
x_{\mathrm{math}},
y_{\mathrm{AI}}
\mid G_t
)
\gg0,
$$

則外部分類距離大：

$$
d_{\mathrm{ext}}
(
x_{\mathrm{math}},
y_{\mathrm{AI}}
)
\gg0
$$

不必意味：

$$
d_{\mathrm{cog}}
(
x_{\mathrm{math}},
y_{\mathrm{AI}}
\mid G_t
)
\gg0.
$$

因此：

$$
\boxed{
d_{\mathrm{ext}}
\neq
d_{\mathrm{cog}}
}
$$

是本文第一個基本區分。

---

# 3. Domain Induction Conjecture（DIC）

本文不把 domain 定義為固定 label，而先從可達性出發。

令 seed：

$$
S_t\subseteq X_t.
$$

給定：

- goal \(G_t\)；
- accessibility threshold \(\theta\)；
- 最大關係深度 \(k\)；
- resolution parameter \(\lambda\)。

定義：

$$
D_t
(
S_t;
G_t,\theta,k,\lambda
)
=
\operatorname{Closure}_{\lambda}
\left[
\operatorname{Reach}_t^{(k)}
(
S_t\mid G_t,\theta
)
\right].
$$

其中 \(\operatorname{Closure}_{\lambda}\) 暫表示在解析尺度 \(\lambda\) 下，將彼此高度可達並具有共同任務角色的 cognitive objects 收納成有效區域。

因此 domain 不再是：

$$
D_i=\text{fixed set}.
$$

而是：

$$
\boxed{
D_t
=
D
(
X_t,
\mathcal R_t,
\kappa_t,
G_t,
\theta,
\lambda
).
}
$$

---

## DIC

**Domain Induction Conjecture：**

> 對部分高階認知活動而言，有效認知域不是預先固定的分類單元，而是由目前目標、關係結構、可達性與解析尺度共同誘導。

形式上：

$$
\boxed{
\frac{\partial D_t}
{\partial G_t}
\neq0,
\qquad
\frac{\partial D_t}
{\partial \kappa_t}
\neq0,
\qquad
\frac{\partial D_t}
{\partial \lambda}
\neq0
}
$$

在至少部分任務條件成立。

---

# 4. 為什麼固定 partition 可能不夠？

固定 partition 要求：

$$
D_i\cap D_j
=
\varnothing,
\qquad
i\neq j.
$$

而且：

$$
\bigcup_iD_i=X.
$$

但高階知識中大量概念天然同時參與多種功能。

例如：

$$
x
=
\text{graph}.
$$

它可能同時位於：

- mathematics；
- computer science；
- network science；
- neuroscience；
- social science。

對外部知識分類而言，可以給它多標籤。

但對 cognition 而言，更重要的不是：

$$
\operatorname{Label}(x),
$$

而是：

$$
\operatorname{Role}(x\mid G_t).
$$

同一物件在不同 goal 下可能扮演完全不同的局部結構角色。

因此：

$$
\boxed{
\text{multi-label taxonomy}
\neq
\text{dynamic cognitive organization}.
}
$$

---

# 5. Overlapping Domain Conjecture（ODC）

本文提出：

$$
\mathcal U_t
=
\{
U_{\alpha,t}
\}_{\alpha\in I_t}
$$

作為有效認知域集合。

不同域允許：

$$
U_{\alpha,t}
\cap
U_{\beta,t}
\neq
\varnothing.
$$

因此：

$$
\mathcal U_t
$$

較接近 cover，而不是 partition。

若：

$$
\bigcup_{\alpha\in I_t}
U_{\alpha,t}
\supseteq
A_t,
$$

則當前 active cognitive region 被一組局部 domain covers 所覆蓋。

ODC 宣稱：

$$
\boxed{
\text{effective cognitive domains are generally allowed to overlap}.
}
$$

這個重疊不是分類失敗，而可能是跨域轉移成立的必要橋樑。

---

# 6. Bridge Objects

若：

$$
b
\in
U_\alpha
\cap
U_\beta,
$$

則稱：

$$
b
$$

為候選 bridge object。

它可以是：

- 一個共同數學結構；
- 一個共享因果模式；
- 一個共同控制問題；
- 一個 analogical relation；
- 一個共同資料表示；
- 一個相同 optimization principle。

定義 bridge strength：

$$
B_t(b;\alpha,\beta)
=
\kappa_t
(
U_\alpha,
b
\mid G_t
)
\,
\kappa_t
(
b,
U_\beta
\mid G_t
).
$$

若：

$$
B_t
\gg0,
$$

則即使外部 label 顯示：

$$
D_\alpha^{\mathrm{ext}}
\neq
D_\beta^{\mathrm{ext}},
$$

有效 cognitive transition 仍可能非常低成本。

---

# 7. 所謂「跨領域」可能有兩種完全不同情形

## 7.1 真正的 cognitive boundary crossing

若：

$$
d_{\mathrm{cog}}
(
x,y
\mid G
)
\gg0,
$$

則：

$$
x\rightarrow y
$$

需要大幅 context reconstruction。

這可稱：

$$
\boxed{
\text{cognitive domain switch}.
}
$$

---

## 7.2 External-domain crossing without cognitive discontinuity

若：

$$
d_{\mathrm{ext}}(x,y)\gg0
$$

但：

$$
d_{\mathrm{cog}}(x,y\mid G)\approx0,
$$

則外部看似跨領域，

內部可能只是：

$$
\boxed{
\text{local relational traversal}.
}
$$

這就是：

$$
\boxed{
\text{disciplinary switching}
\neq
\text{cognitive switching}.
}
$$

---

# 8. 局部座標圖：為什麼使用 chart 語言？

一個認知域：

$$
U_\alpha
$$

可能包含大量異質關係。

但在某個 task / goal 下，主體通常不需要同時保留所有自由度。

因此定義：

$$
\phi_{\alpha,t}:
U_{\alpha,t}
\rightarrow
Z_{\alpha,t},
$$

其中：

$$
Z_{\alpha,t}
\subseteq
\mathbb R^{d_\alpha}
$$

或更一般的有限 task-coordinate representation。

例如某個 domain 在當前任務下只需要：

$$
\phi_\alpha(x)
=
(
\text{causal role},
\text{cost},
\text{uncertainty},
\text{dependency}
).
$$

另一個 goal 下：

$$
\phi'_\alpha(x)
=
(
\text{semantic similarity},
\text{historical relation}
).
$$

所以：

$$
\boxed{
\phi_{\alpha,t}
\neq
\phi_{\alpha,t'}
}
$$

完全可能。

---

# 9. Chart 不是流形宣告

數學上，manifold chart 通常要求：

$$
\phi_\alpha:
U_\alpha
\rightarrow
V_\alpha\subseteq\mathbb R^n
$$

具備特定 homeomorphic structure。

本文目前**不具備**這個證明。

因此本文中的 chart 僅滿足較弱要求：

1. \(U_\alpha\) 是一個可操作認知區域；
2. \(\phi_\alpha\) 提供局部 task-relevant coordinates；
3. 相同局部結構可在不同 chart 下重新表徵；
4. overlap 上可以定義可檢驗的 translation / correspondence。

所以目前更精確叫：

$$
\boxed{
\text{cognitive local coordinate chart}.
}
$$

而不是：

$$
\boxed{
\text{manifold chart}.
}
$$

如果後續不能建立更嚴格條件，就保持這個弱版本。

---

# 10. Dynamic Cognitive Atlas

若：

$$
\mathfrak A_t
=
\{
(U_{\alpha,t},\phi_{\alpha,t})
\}_{\alpha\in I_t},
$$

則稱：

$$
\mathfrak A_t
$$

為時間 \(t\) 的候選 cognitive atlas。

關鍵是：

$$
\boxed{
\mathfrak A_t
\neq
\mathfrak A_{t+1}
}
$$

可以成立。

變化形式包括：

- 新 chart 出現；
- 舊 chart 消失；
- chart domain 擴張；
- chart domain 收縮；
- overlap 增加；
- overlap 消失；
- coordinate map 改變；
- 多個 charts 被 coarse-grain 成一個高階 chart。

因此認知 atlas 本身可以是動態的。

---

# 11. Chart Transition

若：

$$
U_\alpha\cap U_\beta
\neq
\varnothing,
$$

且兩個 coordinate maps 在 overlap 上具可逆結構，則形式上可以寫：

$$
T_{\alpha\beta}
=
\phi_\beta
\circ
\phi_\alpha^{-1}.
$$

但在人類 cognition 中：

$$
\phi_\alpha^{-1}
$$

不一定存在。

因此更弱地定義：

$$
T_{\alpha\beta}:
Z_{\alpha|\alpha\beta}
\rightsquigarrow
Z_{\beta|\alpha\beta},
$$

其中：

$$
\rightsquigarrow
$$

表示可能是：

- stochastic mapping；
- partial mapping；
- lossy translation；
- many-to-one correspondence。

這一點很重要。

真正跨 domain 的認知成本，可能部分來自：

$$
\boxed{
\text{chart translation loss}.
}
$$

---

# 12. Translation Cost

定義 chart translation cost：

$$
K_{\alpha\beta}
=
K_{\mathrm{retrieval}}
+
K_{\mathrm{recode}}
+
K_{\mathrm{context}}
+
K_{\mathrm{loss}}.
$$

如果：

$$
U_\alpha\cap U_\beta
$$

很大，

而 transition mapping 穩定：

$$
K_{\alpha\beta}\downarrow.
$$

如果兩個 chart 幾乎沒有共享結構：

$$
K_{\alpha\beta}\uparrow.
$$

所以實際 cognitive switching cost 可能更接近：

$$
\boxed{
K_{\mathrm{switch}}
=
f(
\text{overlap},
\text{translation},
\text{goal continuity}
)
}
$$

而不只是：

$$
\boxed{
f(
\text{discipline labels}
).
}
$$

---

# 13. 現有研究提供什麼鄰接證據？

2024 年 Qiu 等人使用 multidimensional abstract navigation task，觀察到 hippocampus、entorhinal cortex、OFC 等區域參與 abstract cognitive-map formation 與使用，並呈現 exploration / exploitation 階段差異。

這支持：

$$
\boxed{
\text{abstract task-relevant spaces can be learned and navigated}.
}
$$

2025 年 Tan 等人進一步顯示，mOFC 與 lOFC 對 task-space cognitive map 有互補角色：mOFC 表徵 hidden task-state components，而 lOFC / dlPFC 編碼跨 task states 的抽象規則。

這支持：

$$
\boxed{
\text{task structure can define a cognitively represented state space}.
}
$$

但它們仍未證明：

$$
\boxed{
\text{domain boundaries are dynamically induced}.
}
$$

---

# 14. Task Structure Tailors Representation

Bhandari 等人的研究比較 flat task 與 hierarchical context-dependent task。

同樣是 task representation 問題，lPFC 並未使用完全相同的幾何，而是形成 task-tailored representational geometries：

- flat task 強化特定 global category axis；
- hierarchy task 抽象表示 higher-level context；
- context-specific local geometry 壓縮 irrelevant information；
- relevant information 被選擇性保留與抽象。

這是一個非常重要的鄰接結果：

$$
\boxed{
\text{representation geometry}
\text{ can depend on task structure}.
}
$$

但該工作目前為 preprint，因此本文只將其視為支持性鄰接證據，不作為 DIC 已成立的定論。

---

# 15. Hierarchical Spaces

Peer 與 Epstein（2025）顯示人類在 nested spatial environment 中會表徵：

$$
\text{subspace}
\subset
\text{larger space}.
$$

跨 subspace 關係處理具有額外成本。

這告訴我們：

$$
\boxed{
\text{one cognitive map need not be flat}.
}
$$

但 TADC-02 的命題更強：

> 不只環境本身可以 hierarchical；「什麼算一個 domain」可能也隨 goal / resolution 改變。

所以：

$$
\text{hierarchical map}
$$

是鄰接模型，

不是完整的 dynamic-domain theory。

---

# 16. Boundary Relativity Conjecture（BRC）

令 domain boundary：

$$
\partial D_t
=
\partial
D(
G_t,\theta,\lambda
).
$$

若：

$$
G_t
\rightarrow
G_{t+1},
$$

或：

$$
\lambda_t
\rightarrow
\lambda_{t+1},
$$

則：

$$
\boxed{
\partial D_t
\neq
\partial D_{t+1}
}
$$

可能發生。

因此：

## BRC

> 有效認知域的邊界並非必然固定，而可能相對於目標、解析尺度與目前可達結構。

這意味著：

$$
\boxed{
\text{domain membership}
}
$$

可以是 context-sensitive relation，

而不是永久布林值。

---

# 17. Soft Membership

因此可定義：

$$
\mu_{D_t}(x)
\in
[0,1].
$$

其中：

$$
\mu_{D_t}(x)
$$

表示：

$$
x
$$

在目前 goal / resolution 下屬於某認知域的有效程度。

同一 object：

$$
x
$$

可以：

$$
\mu_{D_1}(x)=0.9,
$$

$$
\mu_{D_2}(x)=0.8.
$$

這自然允許 overlap。

也比：

$$
x\in D_1
\quad\text{or}\quad
x\in D_2
$$

更符合多功能認知結構。

---

# 18. Resolution Parameter

引入：

$$
\lambda
$$

表示觀察／表示解析尺度。

當：

$$
\lambda\downarrow
$$

時，

可以看見更多局部區分：

$$
D
\rightarrow
\{
D_1,D_2,\ldots,D_n
\}.
$$

當：

$$
\lambda\uparrow
$$

時，

多個局部單位被 coarse-grain：

$$
\{
D_1,D_2,\ldots,D_n
\}
\rightarrow
D^*.
$$

因此：

$$
\boxed{
\text{macro}
\quad\text{and}\quad
\text{micro}
}
$$

不一定是固定本體層級。

它們可能只是：

$$
\boxed{
\lambda\text{-relative descriptions}.
}
$$

這一點將在 TADC-04 正式展開。

---

# 19. Re-indexing

若一個低階 domain：

$$
D_i
$$

在較粗解析度中被視為單一 node：

$$
v_i,
$$

則：

$$
D_i
\mapsto
v_i.
$$

反過來，若提高解析度：

$$
v_i
\mapsto
D_i
=
\{
x_1,\ldots,x_m
\}.
$$

本文稱這種操作：

$$
\boxed{
\text{Re-indexing}.
}
$$

它不是普通 task switching。

它是：

$$
\boxed{
\text{changing what counts as an object}.
}
$$

---

# 20. Domain Expansion

若新 relation 被加入：

$$
(x,y)\in\mathcal R_{t+1}
$$

並使：

$$
y
$$

進入：

$$
\operatorname{Reach}^{(k)}(D_t),
$$

則：

$$
D_t
\subset
D_{t+1}.
$$

稱：

$$
\boxed{
\text{Domain Expansion}.
}
$$

---

# 21. Domain Contraction

若：

$$
\kappa_t(x,y\mid G)
$$

低於 threshold，

或 goal 改變使某區域不再 relevant，

則：

$$
D_{t+1}
\subset
D_t.
$$

稱：

$$
\boxed{
\text{Domain Contraction}.
}
$$

---

# 22. Domain Gluing

若兩個原本低 overlap 的 domains：

$$
U_\alpha,
U_\beta
$$

透過 bridge structure：

$$
B
$$

建立高可達性，

則：

$$
G:
(U_\alpha,U_\beta)
\mapsto
U_{\alpha\beta}.
$$

其中：

$$
U_{\alpha\beta}
=
U_\alpha
\cup_B
U_\beta.
$$

這裡的：

$$
\cup_B
$$

暫時只是 relational gluing notation，

不是已證明的 topological pushout。

嚴格 categorical / topological status 留待後文。

---

# 23. Domain Splitting

反過來：

若：

$$
\kappa_t
$$

在某個 bridge region 大幅下降，

一個原本有效連通 domain：

$$
D
$$

可能分裂：

$$
D
\rightarrow
D_1\cup D_2.
$$

若：

$$
\operatorname{Conn}(D)=1
$$

變成：

$$
\operatorname{Conn}(D_1,D_2)=0,
$$

則稱：

$$
\boxed{
\text{Domain Splitting}.
}
$$

這是未來真正需要 connectivity measure 的地方。

---

# 24. Dynamic Domain State

因此一個 domain 不應只記：

$$
D_t.
$$

可以記：

$$
\mathbf d_t
=
(
|D_t|,
\partial D_t,
\Omega_t,
K_t,
H_t,
\lambda_t
).
$$

其中：

- \(|D_t|\)：有效規模；
- \(\partial D_t\)：boundary；
- \(\Omega_t\)：與其他 domains 的 overlap profile；
- \(K_t\)：internal accessibility / connectivity；
- \(H_t\)：local relational heterogeneity；
- \(\lambda_t\)：resolution。

因此 domain 變化可以直接轉成時間序列：

$$
\mathbf d_t
\rightarrow
\mathbf d_{t+1}.
$$

---

# 25. Null Model 1：Fixed Domain Partition

最簡競爭模型：

$$
\Pi
=
\{
D_1,\ldots,D_n
\}
$$

固定。

goal 只改變：

$$
P(D_i\mid G_t).
$$

也就是主體只是在固定 domains 中切換權重。

如果這個模型就能完整預測：

- behavior；
- reaction time；
- generalization；
- neural geometry；
- switch cost；

則 DIC 沒有必要。

---

# 26. Null Model 2：Single Latent Semantic Space

另一個競爭模型：

所有 concepts 都存在固定 latent space：

$$
Z.
$$

不同 task 只改變：

$$
W_t
$$

或 readout function：

$$
f_t:Z\rightarrow Y_t.
$$

此時：

$$
Z
$$

不變，

只是：

$$
f_t
$$

改變。

如果所有「動態 domain」現象都能由：

$$
\boxed{
\text{fixed latent geometry + dynamic readout}
}
$$

解釋，

則 Dynamic Cognitive Atlas 太複雜。

---

# 27. Null Model 3：Task-Set Mixture

還可以假設大腦已預先學到：

$$
M_1,M_2,\ldots,M_q.
$$

當 context 改變時：

$$
P(M_i\mid G)
$$

改變。

看起來像 domain 被重新生成，

但其實只是：

$$
\boxed{
\text{mixture reweighting}.
}
$$

因此要支持 DIC 的強版本，

必須找出：

$$
\text{pre-existing mixture}
$$

無法解釋的：

- novel overlap；
- novel bridge；
- new effective partition；
- new generalization structure。

---

# 28. 實驗一：Goal Remapping

使用同一 object set：

$$
X
$$

與相同 exposure。

只改變目標：

$$
G_1,
G_2,
G_3.
$$

例如同一組物件要求：

- 找 causal organization；
- 找 semantic organization；
- 找 action organization。

測：

$$
D^{(1)},
D^{(2)},D^{(3)}
$$

的：

- behavioral transition graph；
- similarity matrix；
- generalization；
- memory clustering；
- neural RSA。

若：

$$
\partial D^{(1)}
\neq
\partial D^{(2)}
$$

且不能由 readout-only model 解釋，

支持 BRC / DIC。

---

# 29. 實驗二：Disciplinary Distance vs Cognitive Distance

建立跨學科概念對：

$$
(x_i,y_i).
$$

每一對都有：

$$
d_{\mathrm{ext}}
$$

與：

$$
d_{\mathrm{rel}}
$$

兩種距離。

測：

- transition time；
- inference accuracy；
- spontaneous association；
- return probability；
- working-memory interference。

比較：

$$
M_{\mathrm{discipline}}
$$

與：

$$
M_{\mathrm{relational}}.
$$

若：

$$
\operatorname{PredictiveAccuracy}
(
M_{\mathrm{relational}}
)
>
\operatorname{PredictiveAccuracy}
(
M_{\mathrm{discipline}}
),
$$

則：

$$
\boxed{
\text{disciplinary boundary}
}
$$

不是最好的 cognitive boundary predictor。

---

# 30. 實驗三：Overlap Manipulation

先建立兩個 domains：

$$
U_A,
U_B.
$$

Group 1 學習共同 bridge：

$$
B.
$$

Group 2 只接受相同 exposure，

但不被要求處理 bridge relation。

若 Group 1 後續：

$$
K_{AB}\downarrow,
$$

$$
P(A\rightarrow B)\uparrow,
$$

$$
\text{cross-domain inference}\uparrow,
$$

則支持 overlap / gluing mechanism。

---

# 31. 實驗四：Boundary Perturbation

建立一個有 community structure 的 artificial concept graph。

逐步提高 bridge weights：

$$
w_B:
0
\rightarrow1.
$$

測認知 boundary 是否在某區間發生：

$$
\text{merge}.
$$

若 behavioral / neural clustering 呈現：

$$
D_1,D_2
\rightarrow
D_{12},
$$

則可直接操作化：

$$
\boxed{
\text{domain gluing}.
}
$$

如果結果只是 association strength 線性增加，

沒有任何 clustering / generalization structure change，

則 gluing language 不必要。

---

# 32. 實驗五：Hierarchical Re-indexing

建立：

$$
x_{ijk}
$$

低階 objects。

第一階段：

$$
x_{ijk}
$$

各自作為 items。

第二階段：

將：

$$
\{x_{i1},x_{i2},\ldots\}
$$

視為高階 unit：

$$
U_i.
$$

第三階段：

又要求展開：

$$
U_i
\rightarrow
\{x_{i1},x_{i2},\ldots\}.
$$

測：

- switching；
- interference；
- chunk recall；
- neural abstraction；
- transition kernel。

如果：

$$
U_i
$$

能在不同 resolution 下真正呈現 node / subspace 雙重角色，

支持 re-indexing。

---

# 33. 五個核心預測

## DIC-H1 — Goal-Dependent Domain Induction

在 stimulus exposure 相同下：

$$
G_1\neq G_2
$$

應產生不同有效：

$$
D_t.
$$

---

## DIC-H2 — Overlap Predicts Low-Cost Transition

$$
|U_\alpha\cap U_\beta|\uparrow
$$

應預測：

$$
K_{\alpha\beta}\downarrow.
$$

---

## DIC-H3 — Relational Distance Beats Disciplinary Distance

對實際 transition：

$$
d_{\mathrm{cog}}
$$

應比：

$$
d_{\mathrm{ext}}
$$

具有更高預測力。

---

## DIC-H4 — Resolution Changes Boundary

改變：

$$
\lambda
$$

應系統性改變：

$$
\partial D.
$$

---

## DIC-H5 — Novel Domain Structure

在部分 learning / reasoning episode 後，

最好的 domain model 應包含：

$$
D_{\mathrm{new}}
$$

而不是只調整舊 domains 的 mixture weights。

若永遠不需要新 domain，

DIC 強版失敗。

---

# 34. Boundary Relativity 不等於任意主義

如果 domain boundary 會變，

不代表：

> 任何東西都可以和任何東西是一個領域。

必須受到：

$$
\mathcal R_t
$$

與：

$$
\kappa_t
$$

限制。

因此：

$$
\boxed{
\text{dynamic}
\neq
\text{arbitrary}.
}
$$

若兩個 cognitive regions：

$$
U_A,U_B
$$

缺少：

- semantic relation；
- causal relation；
- analogical structure；
- procedural dependency；
- goal relevance；

則：

$$
\kappa(U_A,U_B)\approx0.
$$

這時硬把它們稱作同一 domain 沒有預測價值。

---

# 35. Domain Coherence

定義 domain coherence：

$$
Q(D)
=
\frac{
\sum_{x,y\in D}
\kappa(x,y\mid G)
}{
|D|(|D|-1)
}.
$$

若：

$$
Q(D)\gg0,
$$

則 domain 內部高度可達。

若：

$$
Q(D)\approx0,
$$

那可能只是任意集合。

可以進一步考慮：

$$
Q_{\mathrm{in}}
-
Q_{\mathrm{out}}.
$$

只有當：

$$
Q_{\mathrm{in}}
>
Q_{\mathrm{out}}
$$

才有理由說某個局部區域形成有效 domain。

---

# 36. Domain 不一定要求高內聚

但也要防止另一個極端。

有些 domain 是 chain-like：

$$
x_1
\rightarrow
x_2
\rightarrow
x_3
\rightarrow\cdots
$$

而非 clique-like。

所以：

$$
Q(D)
$$

不能是唯一指標。

還需：

- connectivity；
- path length；
- betweenness；
- bridge robustness；
- reachability；
- task predictive value。

因此：

$$
\boxed{
\text{domain}
\neq
\text{community detection result alone}.
}
$$

---

# 37. 局部域與世界模型

若認知系統具有很大的世界模型：

$$
W_t,
$$

它不需要在每次思考時完整展開。

而可以只激活：

$$
U_t\subset W_t.
$$

但 TADC 的命題不只是：

$$
U_t
$$

被選中。

更可能：

$$
U_t
$$

在 reasoning 中：

$$
U_t
\rightarrow
U_{t+1}
$$

並改變其與其他局部 chart 的 overlap。

因此：

$$
\boxed{
\text{local domain activation}
\neq
\text{local domain transformation}.
}
$$

這延續 TADC-01 的根區分。

---

# 38. 人工智能與外部認知支架暫不在本文處理

AI、knowledge graph、external memory、agent system 都可能：

$$
K_{\alpha\beta}\downarrow
$$

並保存：

$$
\mathfrak A_t.
$$

但本文先刻意不依賴外部工具。

TADC-07 將另外問：

$$
\boxed{
\text{external systems can alter effective cognitive topology?}
}
$$

如果 TADC-02 在無外部 AI 條件下都不能成立，

則 TADC-07 只能作為工具效應理論，

不能回頭證明一般 cognitive-domain theory。

---

# 39. 與 TADC-01 的統一形式

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
\}.
$$

其中：

$$
U_{\alpha,t}
=
D(
S_\alpha,
G_t,
\theta,
k,
\lambda
).
$$

所以：

$$
\boxed{
\mathcal C_t
\Rightarrow
\mathfrak A_t
}
$$

表示：

> 一個大的認知關係空間，在特定 goal / resolution 下誘導出一組局部可操作 domains。

而：

$$
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1}
$$

就是 dynamic-domain evolution。

---

# 40. 最小動力學

可以寫：

$$
\mathfrak A_{t+1}
=
\Psi
(
\mathfrak A_t,
\mathcal C_t,
G_t,
a_t,
m_t,
e_t,
\lambda_t
).
$$

其中：

$$
\Psi
$$

可能包含：

$$
\{
E,C,T,G,S,R
\},
$$

分別代表：

- Expansion；
- Contraction；
- Traversal；
- Gluing；
- Splitting / Detachment；
- Re-indexing。

這就是 TADC-03 要正式處理的六算子入口。

---

# 41. 反證條件

本文必須接受以下失敗條件。

## F1 — Fixed Partition Wins

如果固定 domain labels 對：

- switch cost；
- generalization；
- neural patterns；
- inference；

的 out-of-sample prediction 不弱於 dynamic-domain model，

則 DIC 不值得保留。

---

## F2 — Fixed Latent Space Wins

如果：

$$
\text{fixed }Z
+
\text{dynamic readout}
$$

足以解釋所有 goal-dependent differences，

則：

$$
\mathfrak A_t
$$

只是多餘重述。

---

## F3 — No Stable Overlap Effect

若：

$$
|U_\alpha\cap U_\beta|
$$

與：

$$
K_{\alpha\beta}
$$

沒有穩定關係，

則 ODC 的功能意義受損。

---

## F4 — Resolution Is Only Analyst Choice

如果：

$$
\lambda
$$

只能由研究者事後任意選擇，

而 participant behavior / neural data 沒有任何可辨認的 resolution transition，

則 BRC 只是分析方法，不是 cognition mechanism。

---

## F5 — Chart Language Adds No Prediction

如果：

$$
(U_\alpha,\phi_\alpha)
$$

無法提供超越普通：

- task set；
- semantic cluster；
- category；
- latent factor；

的額外預測，

則「chart」應刪除。

---

# 42. 本文的強弱版本

## Weak DIC

不同 goals 會誘導不同有效 grouping / geometry。

這與現有 task-structure literature 最接近。

---

## Medium DIC

這些 grouping 形成可重疊、可轉換、具有不同 translation costs 的局部 domains。

---

## Strong DIC

認知活動可以生成新的 domain organization：

$$
\mathfrak A_t
\rightarrow
\mathfrak A_{t+1}
$$

且不能由固定 latent space + dynamic readout / mixture model 完整解釋。

只有 Strong DIC 真正構成 TADC 的高風險部分。

---

# 43. 本文最小貢獻

本文真正提出的不是：

> 所有知識都是相通的。

那是一個過度寬泛且不可證偽的說法。

本文提出的是：

$$
\boxed{
\text{the cognitively effective boundary between domains
may be induced rather than fixed}.
}
$$

因此，「跨領域」至少應拆成：

$$
\boxed{
\text{external category crossing}
}
$$

與：

$$
\boxed{
\text{internal cognitive-boundary crossing}.
}
$$

這兩個不必相等。

---

# 44. 結論

本文從 TADC-01 的可變認知空間出發，提出：

$$
\boxed{
\textbf{DIC — Domain Induction Conjecture}
}
$$

有效認知域由：

$$
(
\mathcal R_t,
\kappa_t,
G_t,
\theta,
\lambda
)
$$

共同誘導，而非必然先驗固定。

接著提出：

$$
\boxed{
\textbf{ODC — Overlapping Domain Conjecture}
}
$$

有效 domains 一般允許：

$$
U_\alpha\cap U_\beta\neq\varnothing,
$$

並且 overlap 可能降低 chart translation cost。

最後提出：

$$
\boxed{
\textbf{BRC — Boundary Relativity Conjecture}
}
$$

domain boundary 可能相對於：

$$
G_t,
\lambda_t,
t
$$

而變化。

因此：

$$
\boxed{
\text{disciplinary boundary}
\neq
\text{cognitive boundary}.
}
$$

在最強版本中，認知系統並不是在一組永久固定的領域之間跳躍，而可能不斷產生：

$$
\mathfrak A_t
=
\{
(U_{\alpha,t},\phi_{\alpha,t})
\},
$$

一套依任務與尺度更新的 dynamic cognitive atlas。

這也意味著：

$$
\boxed{
\text{「跨域」有時可能不是跳離一個空間，
而是在同一個更高階關係空間內換用局部座標圖。}
}
$$

但這句只有在 chart-overlap、translation cost、goal-dependent boundary 與 dynamic-atlas model 都取得實證增量後，才有資格從比喻升級成理論。

因此 TADC-02 的最終風險條件仍然是：

$$
\boxed{
\text{If fixed domains predict cognition just as well,
dynamic domains should be abandoned.}
}
$$

---

# 參考文獻

1. Qiu Y, Li H, Liao J, et al. **Forming cognitive maps for abstract spaces: the roles of the human hippocampus and orbitofrontal cortex.** *Communications Biology*. 2024;7:517. doi:10.1038/s42003-024-06214-5. PMID: 38693344.  
2. Tan L, Qiu Y, Qiu L, et al. **The medial and lateral orbitofrontal cortex jointly represent the cognitive map of task space.** *Communications Biology*. 2025;8:163. doi:10.1038/s42003-025-07588-w. PMID: 39900714.  
3. Peer M, Epstein RA. **Cognitive maps for hierarchical spaces in the human brain.** *Cerebral Cortex*. 2025;35(9):bhaf261. doi:10.1093/cercor/bhaf261. PMID: 40982478.  
4. Leach SC, Chen X, Hwang K. **Hierarchical Reconfiguration of Neurocognitive Task Set Representations Mediates Cognitive Flexibility.** *Journal of Neuroscience*. 2026. doi:10.1523/JNEUROSCI.0113-26.2026. PMID: 42276789.  
5. Bhandari A, Keglovits H, Buyukyazgan D, Badre D. **Task structure tailors the geometry of neural representations in human lateral prefrontal cortex.** bioRxiv preprint. Updated 2025. doi:10.1101/2024.03.06.583429. PMID: 38496680. **Preprint; not peer reviewed at the cited version.**  
6. Beck DW, Heaton CN, Davila LD, et al. **A decision-space model explains context-specific decision-making.** *Nature Communications*. 2025;16:7437. doi:10.1038/s41467-025-61466-x.  
7. Qiu Y, et al. **Dynamic changes in orbitofrontal-hippocampal connectivity linked to cognitive map formation in humans.** *NeuroImage*. 2025;121415. doi:10.1016/j.neuroimage.2025.121415. PMID: 40780573.  
8. Garvert MM, Dolan RJ, Behrens TEJ. **A map of abstract relational knowledge in the human hippocampal-entorhinal cortex.** *eLife*. 2017;6:e17086. doi:10.7554/eLife.17086.  
9. Park SA, Miller DS, Nili H, Ranganath C, Boorman ED. **Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps.** *Neuron*. 2020;107(6):1226–1238.e8. doi:10.1016/j.neuron.2020.06.030.  
10. Behrens TEJ, Muller TH, Whittington JCR, et al. **What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior.** *Neuron*. 2018;100(2):490–509. doi:10.1016/j.neuron.2018.10.002.  

---

## 與系列的關係

**已完成：**

- TADC-01：《注意力不是單點選擇——可變認知空間與注意—空間轉換猜想》
- TADC-02：《動態認知域——領域作為局部座標圖》

**下一篇：**

- TADC-03：《拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引》

後續：

- TADC-04：《嵌套注意域與觀察尺度》
- TADC-05：《從單點超專注到拓樸超專注》
- TADC-06：《關係優先認知與跨域連續性》
- TADC-07：《外部認知支架與人—AI 認知拓樸》
- TADC-08：《拓樸注意力的測量、反證與工程化》

---

**狀態：** TADC-02 v0.1  
**原始人體／臨床數據：** 無  
**理論狀態：** 猜想／研究綱領；未經實驗驗證  
**拓樸狀態：** 尚未證明為嚴格拓樸空間或流形；chart / atlas 為受約束的候選形式語言
