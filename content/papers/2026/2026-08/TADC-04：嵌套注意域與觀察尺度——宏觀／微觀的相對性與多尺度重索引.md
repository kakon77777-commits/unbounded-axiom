# TADC-04：嵌套注意域與觀察尺度——宏觀／微觀的相對性與多尺度重索引

**英文題名：** Nested Attentional Domains and Observation Scale: Relative Macro–Micro Structure and Multiscale Re-indexing  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-04  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論命題／多尺度形式化／可證偽研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

TADC-01 提出可變認知空間與注意—空間轉換猜想；TADC-02 將有效認知域描述為由目標、關係、可達性與解析尺度所誘導出的局部 chart；TADC-03 再提出 Expansion、Contraction、Traversal、Gluing、Detachment、Re-indexing 六個候選認知算子。

本文處理由此自然產生的第四個問題：

> **如果認知域可以嵌套，而同一結構又可以在不同解析度下被視為「一個物件」或「一整個域」，那麼 macro 與 micro 是否真的是固定層級？**

本文提出四個核心猜想：

1. **Nested Attentional Domain Conjecture（NADC）**：有效認知域可以形成多層嵌套結構，但一般不必被限制為單一樹狀 hierarchy；
2. **Object–Domain Duality Conjecture（ODDC）**：同一認知結構可在粗解析度下作為單一 object，在細解析度下作為具有內部關係的 domain；
3. **Scale-Relative Macro–Micro Conjecture（SRMMC）**：macro / micro 不是絕對本體分類，而是相對於觀察尺度與當前表示層級的關係；
4. **Cross-Scale Invariance Conjecture（CSIC）**：若多尺度表示不是任意分析產物，應存在部分跨尺度保持的關係、可達性或功能不變量。

本文引入觀察尺度算子：

$$
\mathcal O_\lambda,
$$

粗粒化算子：

$$
P_{\lambda_f\rightarrow\lambda_c},
$$

以及細化／展開算子：

$$
F_{\lambda_c\rightarrow\lambda_f}.
$$

同一認知結構：

$$
U
$$

可在細尺度表示為：

$$
U^{(\lambda_f)}
=
\{x_1,\ldots,x_n;\mathcal R\},
$$

而在粗尺度被壓縮為：

$$
P_{\lambda_f\rightarrow\lambda_c}
(
U^{(\lambda_f)}
)
=
z_U.
$$

因此：

$$
\boxed{
\text{domain at one scale}
\leftrightarrow
\text{object at another scale}.
}
$$

現有研究已顯示人類能形成 nested spatial cognitive maps、學習不同抽象層級的 hierarchical concepts、在 hierarchical cognitive control 中分離 abstract context 與 subordinate task-set updating，並以快速神經序列建構嵌套結構。這些結果支持 multilevel representation 的存在，但尚未證明 macro / micro 必然具有本文所主張的尺度相對性，也未證明一般 cognition 存在可逆的跨尺度 re-indexing operator。

本文進一步提出 scale-consistency diagram、跨尺度可達性、scale-dependent boundary、resolution cost、representation loss 與 coarse-graining invariants，並建立 fixed hierarchy、single-resolution、analyst-only multiscale decomposition 等虛無模型。

本文的目的不是宣稱 cognition 已被證明具有無限嵌套拓樸，而是把「宏觀／微觀可能只是觀察尺度」改寫成一組可被行為、神經表示與模型比較直接擊敗的命題。

**關鍵詞：** nested attention；hierarchy；multiscale cognition；macro–micro relativity；re-indexing；coarse-graining；cognitive maps；hierarchical control；cognitive invariants；TADC

---

# 0. 邊界聲明

本文不是臨床研究、醫療模型或個人認知診斷。

本文亦不主張：

$$
\boxed{
\text{the brain is literally an infinitely nested topological manifold}.
}
$$

本文所稱：

- macro；
- micro；
- scale；
- coarse-graining；
- chart；
- invariant；

皆為候選形式語言。

只有在這些結構能提供超越傳統：

- hierarchical task representation；
- chunking；
- abstraction；
- cognitive map；
- category learning；
- multilevel control；

的增量預測後，才應保留。

本文也明確區分：

$$
\boxed{
\text{observer-relative}
}
$$

與：

$$
\boxed{
\text{arbitrary}.
}
$$

尺度相對不表示任何尺度都同樣合理。

有效解析度必須受到：

$$
\text{behavior},
\text{task},
\text{representation},
\text{prediction}
$$

約束。

---

# 1. 前三篇留下的問題

TADC-01 定義：

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

TADC-02 定義 dynamic cognitive atlas：

$$
\mathfrak A_t
=
\{
(U_{\alpha,t},\phi_{\alpha,t})
\}.
$$

TADC-03 又定義 Re-indexing：

$$
R_\lambda:
\mathfrak A^{(\lambda_1)}
\rightarrow
\mathfrak A^{(\lambda_2)}.
$$

但這立即引出：

> 如果不同 \(\lambda\) 會改變「什麼算一個 object」，那 macro / micro 到底在哪裡？

若：

$$
U
=
\{x_1,\ldots,x_n\}
$$

在某一尺度是一個 domain，

但在另一尺度：

$$
U
\mapsto
z_U,
$$

變成一個單一 object，

那麼：

$$
\boxed{
\text{object}
\quad\text{and}\quad
\text{domain}
}
$$

就不再是絕對互斥類別。

這是本文的起點。

---

# 2. 最小尺度參數

令：

$$
\lambda
$$

表示認知表示或觀察解析度。

本文約定：

$$
\lambda_f
<
\lambda_c
$$

表示：

$$
\lambda_f
$$

較細，

$$
\lambda_c
$$

較粗。

這只是符號慣例。

細尺度：

$$
\mathcal C^{(\lambda_f)}
$$

保留更多內部區分。

粗尺度：

$$
\mathcal C^{(\lambda_c)}
$$

把部分內部差異 coarse-grain。

因此：

$$
\boxed{
\mathcal O_\lambda:
\mathcal C
\mapsto
\mathcal C^{(\lambda)}
}
$$

稱為 observation-scale operator。

---

# 3. 「觀察者」在本文中是什麼？

本文不要求神秘的外部心靈觀察者。

觀察者可以是：

1. 認知主體在某個任務中的 representational policy；
2. 實驗要求形成的 abstraction level；
3. 一個分析模型；
4. 一個神經解碼尺度；
5. 一個外部測量系統。

因此：

$$
\mathcal O_\lambda
$$

真正表示：

$$
\boxed{
\text{which distinctions are retained at scale }\lambda.
}
$$

不同觀察者只要使用相同 discrimination policy，

可以得到近似相同：

$$
\mathcal C^{(\lambda)}.
$$

所以本文的 observer relativity 並不是主觀任意性。

---

# 4. Nested Attentional Domain Conjecture（NADC）

若存在一組 domains：

$$
U_0,U_1,\ldots,U_n
$$

使：

$$
U_0
\subset
U_1
\subset
\cdots
\subset
U_n,
$$

則形成一條 nested chain。

但一般 cognition 不必只有一條 chain。

更一般地：

$$
\mathcal U
=
\{U_\alpha\}
$$

可以形成 partial order：

$$
U_\alpha
\preceq
U_\beta
$$

若：

$$
U_\alpha
$$

在某解析度上被包含或抽象進：

$$
U_\beta.
$$

NADC 宣稱：

$$
\boxed{
\text{effective attentional domains can support
multilevel nested organization}.
}
$$

---

# 5. 為什麼不能直接假定是一棵樹？

樹要求每個 child：

$$
U_i
$$

只有一個 parent。

但 TADC-02 已允許 overlap：

$$
U_A\cap U_B\neq\varnothing.
$$

因此一個局部結構：

$$
U_x
$$

可能同時參與：

$$
U_A
$$

與：

$$
U_B.
$$

所以一般結構可能是：

- tree；
- DAG；
- lattice-like partial order；
- overlapping nested cover；
- heterarchy。

因此：

$$
\boxed{
\text{hierarchical}
\neq
\text{strictly tree-structured}.
}
$$

這是一個必要限制。

---

# 6. 現有 nested-space 證據

Peer 與 Epstein（2025）讓參與者學習一個「庭院中包含建築物」的 virtual environment。

也就是：

$$
U_{\mathrm{building}}
\subset
U_{\mathrm{courtyard}}.
$$

跨 subspace integration 比同一 subspace 內判斷更慢、更不準，且 hippocampus、retrosplenial complex、occipital place area 等區域呈現與 hierarchical organization 相符的神經結果。

這提供直接證據：

$$
\boxed{
\text{humans can form cognitive maps of nested spaces}.
}
$$

但它不證明：

$$
\boxed{
\text{all abstract cognition is nested}.
}
$$

也不證明：

$$
\boxed{
\text{macro/micro is always re-indexable}.
}
$$

---

# 7. Hierarchical Concepts 也具有多層級表示

Mack 等人（2021）研究 hierarchical concept learning，讓 participants 在不同抽象層次學習 category structure。

其結果顯示 hippocampus 與 prefrontal regions 參與 hierarchical conceptual learning，而 cognition 可以在：

$$
\text{superordinate}
$$

與：

$$
\text{subordinate}
$$

層次操作。

這至少支持：

$$
\boxed{
\text{conceptual cognition is not restricted to one fixed level}.
}
$$

但：

$$
\text{multi-level classification}
$$

仍不等於：

$$
\text{dynamic object-domain duality}.
$$

---

# 8. Object–Domain Duality Conjecture（ODDC）

假設：

$$
U
=
(
X_U,
\mathcal R_U
)
$$

是一個具有內部關係的 cognitive domain。

在細尺度：

$$
\mathcal O_{\lambda_f}(U)
=
(
X_U,\mathcal R_U
).
$$

在粗尺度：

$$
\mathcal O_{\lambda_c}(U)
=
z_U.
$$

其中：

$$
z_U
$$

作為單一 functional object。

因此：

$$
\boxed{
U^{(\lambda_f)}
\leftrightarrow
z_U^{(\lambda_c)}.
}
$$

ODDC 宣稱：

> 同一認知結構可以依表示解析度，在一個尺度上作為 domain，在另一個尺度上作為 object。

---

# 9. Objecthood 因此可能是尺度相對的

一般語言常假定：

$$
x
=
\text{object}
$$

是固定事實。

但考慮：

$$
x
=
\text{a theorem}.
$$

在高階規劃中，

整個 theorem 可以是一個 node：

$$
z_{\mathrm{thm}}.
$$

但在 proof construction 中，

它展開成：

$$
U_{\mathrm{thm}}
=
\{
\text{definitions},
\text{lemmas},
\text{dependencies},
\text{proof steps}
\}.
$$

因此：

$$
\boxed{
\text{objecthood}
=
\text{resolution-dependent functional status}.
}
$$

這不是否定客觀物件存在，

而是區分：

$$
\text{physical / semantic identity}
$$

與：

$$
\text{current cognitive objecthood}.
$$

---

# 10. 粗粒化算子 \(P\)

定義：

$$
P_{\lambda_f\rightarrow\lambda_c}:
\mathcal C^{(\lambda_f)}
\rightarrow
\mathcal C^{(\lambda_c)}.
$$

對一個 domain：

$$
U
=
\{x_1,\ldots,x_n\},
$$

粗粒化：

$$
P(U)
=
z_U.
$$

理想 coarse-graining 不是任意刪資料。

它應保留：

$$
\boxed{
\text{task-relevant sufficient structure}.
}
$$

所以：

$$
P
$$

的品質需要用後續行為預測測量。

---

# 11. 細化算子 \(F\)

反方向：

$$
F_{\lambda_c\rightarrow\lambda_f}:
z_U
\mapsto
\widetilde U.
$$

理想情況：

$$
\widetilde U
\approx
U.
$$

但通常：

$$
F(P(U))
\neq
U.
$$

原因包括：

- compression loss；
- forgetting；
- context change；
- abstraction；
- reconstruction error。

因此：

$$
\boxed{
F\neq P^{-1}
}
$$

一般成立。

這延續 TADC-03 的不可逆性。

---

# 12. Re-indexing 的正式拆解

TADC-03 的：

$$
R_\lambda
$$

現在可以拆成：

### Coarse Re-indexing

$$
R^-
=
P_{\lambda_f\rightarrow\lambda_c}.
$$

### Fine Re-indexing

$$
R^+
=
F_{\lambda_c\rightarrow\lambda_f}.
$$

因此：

$$
\boxed{
R
=
\{R^-,R^+\}.
}
$$

這讓「物件 ↔ 域」第一次具有明確雙向操作。

---

# 13. Scale-Relative Macro–Micro Conjecture（SRMMC）

若：

$$
U_i\subset U_j,
$$

則相對於：

$$
U_j,
$$

可稱：

$$
U_i
$$

為 micro。

但是相對於：

$$
x\in U_i,
$$

則：

$$
U_i
$$

又是 macro。

所以：

$$
\boxed{
\operatorname{Macro}(U_i,U_j)
}
$$

或：

$$
\boxed{
\operatorname{Micro}(U_i,U_j)
}
$$

應該是 binary relation，

而不是 unary property。

形式：

$$
\operatorname{Micro}(A,B)
\iff
A\prec B.
$$

因此不存在無參照物的：

$$
\text{absolute micro}.
$$

---

# 14. Macro / Micro 不是消失，而是關係化

SRMMC 並不是說：

> 宏觀和微觀毫無意義。

而是說：

$$
\boxed{
\text{macro/micro should be relational, not absolute}.
}
$$

就像：

$$
\text{left/right}
$$

需要 reference frame。

macro/micro 也需要：

$$
\lambda
$$

或：

$$
U_{\mathrm{reference}}.
$$

所以更精確寫：

$$
\operatorname{ScaleLevel}
(
U\mid\lambda,G
).
$$

---

# 15. 觀察尺度與認知尺度必須分離

研究者可以使用：

$$
\lambda_{\mathrm{analysis}}.
$$

participant 自己則可能使用：

$$
\lambda_{\mathrm{cog}}.
$$

兩者不必相同。

所以：

$$
\boxed{
\lambda_{\mathrm{analysis}}
\neq
\lambda_{\mathrm{cog}}
}
$$

是一個重要風險。

如果研究者事後把資料切成三層，

並不能證明 participant 真的使用三層 cognition。

真正的 multiscale cognition 證據需要：

- behavioral discontinuity；
- switch cost；
- generalization pattern；
- neural decoding；
- spontaneous grouping；

指向同樣的 scale structure。

---

# 16. Hierarchical Cognitive Control 的鄰接證據

Leach、Chen 與 Hwang（2026）區分：

$$
\text{higher-level context}
$$

與：

$$
\text{subordinate task set}.
$$

其結果顯示：

- subordinate rule switches 較快；
- 更容易受 task-irrelevant perceptual change 影響；
- abstract context switches 較慢但較穩定；
- neural reconfiguration pattern 在不同 hierarchy level 不同。

這支持：

$$
\boxed{
\text{different representational scales have
different updating dynamics}.
}
$$

但它仍可由固定 hierarchy 解釋。

所以對 SRMMC 而言只是必要鄰接證據，

不是充分證據。

---

# 17. 快速建構嵌套結構

2025 年 PNAS 研究《Building hierarchically nested structure by rapid neural sequences》使用 MEG 研究人類建構 hierarchical nested structures。

研究報告快速神經序列執行反覆的 generative operations，使 cognition 能構造 nested hierarchy。

這非常接近：

$$
\boxed{
\text{hierarchy as dynamically constructed structure}.
}
$$

但該研究針對特定 hierarchical structure task。

它並不證明 TADC 所說：

$$
\boxed{
\text{domain/object status is generally scale-relative}.
}
$$

---

# 18. Hierarchy Construction 與 Hierarchy Navigation 必須分離

假設 hierarchy：

$$
H
$$

已經存在。

從：

$$
U_i
$$

走到：

$$
U_j
$$

是：

$$
\boxed{
\text{hierarchy navigation}.
}
$$

而：

$$
H_t
\rightarrow
H_{t+1}
$$

才是：

$$
\boxed{
\text{hierarchy construction / transformation}.
}
$$

TADC 主要關注後者。

因此：

$$
\boxed{
\text{navigating levels}
\neq
\text{changing levels or boundaries}.
}
$$

---

# 19. Scale-Dependent Domain Boundary

TADC-02 定義：

$$
\partial D_t
=
\partial D(
G_t,\theta,\lambda
).
$$

本文進一步強調：

$$
\boxed{
\partial D^{(\lambda_f)}
\neq
\partial D^{(\lambda_c)}
}
$$

可以成立。

例如細尺度看：

$$
D
=
D_1\cup D_2\cup D_3.
$$

粗尺度：

$$
P(D_1,D_2,D_3)
=
D^*.
$$

原來的內部 boundaries：

$$
\partial D_1,
\partial D_2,
\partial D_3
$$

在粗尺度可能消失。

---

# 20. Boundary Disappearance 不等於資訊不存在

如果：

$$
P:
D_1,D_2
\mapsto
D^*,
$$

不表示：

$$
D_1,D_2
$$

物理或記憶上不存在。

只表示：

$$
\boxed{
\text{their distinction is currently suppressed
at scale }\lambda_c.
}
$$

這是 representational suppression，

不是 ontological deletion。

---

# 21. 多尺度可達性

在尺度：

$$
\lambda
$$

定義：

$$
\operatorname{Reach}^{(k)}_\lambda(x).
$$

同一兩個 fine-scale objects：

$$
x,y
$$

可能：

$$
d_{\lambda_f}(x,y)\gg0,
$$

但它們各自 coarse-grain 後：

$$
P(x)\approx P(y).
$$

因此：

$$
d_{\lambda_c}(P(x),P(y))
\ll
d_{\lambda_f}(x,y).
$$

所以：

$$
\boxed{
\text{cognitive distance is scale-dependent}.
}
$$

---

# 22. 跨尺度最短路徑

一個問題的最佳 reasoning path 不必全部在同一尺度。

例如：

$$
x
\overset{R^-}{\longrightarrow}
U
\overset{T}{\longrightarrow}
V
\overset{R^+}{\longrightarrow}
y.
$$

也就是：

1. 把細節 coarse-grain；
2. 在高階 domain 間快速 Traversal；
3. 再展開到細節。

總成本：

$$
K_{\mathrm{multi}}
=
K_{R^-}
+
K_T
+
K_{R^+}.
$$

若：

$$
K_{\mathrm{multi}}
<
K_{\mathrm{fine-only}},
$$

那跨尺度 reasoning 更有效。

這是一個非常直接的可測命題。

---

# 23. Multiscale Routing Conjecture（MRC）

本文增加一個衍生命題：

> 高階 cognition 的有效 trajectory 可以主動跨解析度 routing，而不必在單一 resolution 中完成。

形式：

$$
\boxed{
\gamma
=
(
x^{(\lambda_1)}_1,
x^{(\lambda_2)}_2,
\ldots
)
}
$$

允許：

$$
\lambda_i
\neq
\lambda_{i+1}.
$$

若最佳 path：

$$
\gamma^*
$$

經常包含：

$$
R^-,
R^+,
$$

則 Re-indexing 不是附帶現象，而是 reasoning strategy 的核心部分。

---

# 24. 認知解析度成本

細尺度保留更多資訊，

但成本高。

定義：

$$
K(\lambda)
$$

使：

$$
\lambda\downarrow
\Rightarrow
K(\lambda)\uparrow
$$

作為候選關係。

成本來源：

- working memory；
- search；
- representation；
- interference；
- update；
- serialization。

因此 cognition 可能在：

$$
\boxed{
\text{detail}
\quad\text{vs}\quad
\text{cost}
}
$$

之間選擇解析度。

---

# 25. Resolution Utility

定義：

$$
U(\lambda)
=
V_{\mathrm{task}}(\lambda)
-
\beta K(\lambda)
-
\gamma L(\lambda),
$$

其中：

$$
L(\lambda)
$$

是 coarse-graining information loss。

最佳尺度：

$$
\lambda^*
=
\arg\max_\lambda
U(\lambda).
$$

這不是已證明模型，

但提供一個可測的 bounded multiscale cognition framework。

---

# 26. 太粗與太細都可能失敗

若：

$$
\lambda
$$

太粗：

$$
L(\lambda)\uparrow
$$

造成：

- critical distinction 消失；
- false equivalence；
- bad transfer；
- causal detail 遺失。

若太細：

$$
K(\lambda)\uparrow
$$

造成：

- overload；
- slow reasoning；
- interference；
- search explosion。

所以 cognition 可能需要：

$$
\boxed{
\text{adaptive resolution}.
}
$$

---

# 27. Scale Transition Cost

Re-indexing 不是免費。

定義：

$$
K_R(
\lambda_i
\rightarrow
\lambda_j
).
$$

若：

$$
|\lambda_i-\lambda_j|
\uparrow,
$$

通常：

$$
K_R
$$

可能增加。

但如果已形成穩定 chunk / schema：

$$
K_R\downarrow.
$$

因此 expertise 可能部分表現在：

$$
\boxed{
\text{lower cross-scale re-indexing cost}.
}
$$

這是待驗證命題。

---

# 28. 專家與新手的多尺度差異

新手可能：

$$
R^-:
U
\rightarrow
z_U
$$

非常不可靠，

因為還不知道哪些 detail 可以安全省略。

專家則可能形成：

$$
\boxed{
\text{high-fidelity coarse-graining}.
}
$$

也就是：

$$
P_{\mathrm{expert}}(U)
$$

雖然壓縮，

仍保留 task-relevant invariants。

因此 expert advantage 不一定只來自：

$$
\text{more knowledge}.
$$

可能還包括：

$$
\boxed{
\text{better multiscale representation policy}.
}
$$

本文不宣稱這已被證明。

---

# 29. Cross-Scale Invariance Conjecture（CSIC）

如果：

$$
P
$$

只是任意壓縮，

那 TADC 的 multiscale language 沒有深度。

因此必須問：

> 哪些結構在尺度改變後保持？

定義 invariant：

$$
I(\mathcal C).
$$

若：

$$
I(
P_{\lambda_f\rightarrow\lambda_c}
(
\mathcal C^{(\lambda_f)}
)
)
=
I(
\mathcal C^{(\lambda_f)}
),
$$

則：

$$
I
$$

是候選 coarse-graining invariant。

---

# 30. 候選不變量

可能包括：

### Goal identity

$$
I_G.
$$

### Causal ordering

$$
x\prec y.
$$

### Reachability class

$$
[x]_{\mathrm{reach}}.
$$

### Critical bridge identity

$$
B^*.
$$

### Solution equivalence class

$$
[\sigma].
$$

### Component relation

$$
\operatorname{Conn}(U,V).
$$

這些都只是候選。

真正不變量必須透過不同 task / scale 驗證。

---

# 31. Scale Consistency Diagram

若 fine-scale dynamics：

$$
\Phi_f:
\mathcal C_f
\rightarrow
\mathcal C_f'
$$

以及 coarse-scale dynamics：

$$
\Phi_c:
\mathcal C_c
\rightarrow
\mathcal C_c',
$$

理想 scale-consistency 要求：

$$
P\circ\Phi_f
\approx
\Phi_c\circ P.
$$

圖式：

$$
\begin{array}{ccc}
\mathcal C_f & \xrightarrow{\Phi_f} & \mathcal C_f'\\
\downarrow P &  & \downarrow P\\
\mathcal C_c & \xrightarrow{\Phi_c} & \mathcal C_c'
\end{array}
$$

若：

$$
P\Phi_f
=
\Phi_cP,
$$

稱強尺度一致。

若只近似：

$$
P\Phi_f
\approx
\Phi_cP,
$$

稱 approximate scale consistency。

---

# 32. 為什麼這個交換圖很重要？

因為如果粗尺度模型完全預測錯：

$$
P\Phi_f
\not\approx
\Phi_cP,
$$

那 coarse representation：

$$
\mathcal C_c
$$

不是有效 abstraction。

也就是：

$$
\boxed{
\text{good coarse-graining
must preserve enough dynamics}.
}
$$

這使「macro representation」變成可驗證概念，

而不是研究者方便畫圖。

---

# 33. Scale-Dependent Dynamics

但是並不要求：

$$
\Phi_c
$$

與：

$$
\Phi_f
$$

形式完全一樣。

粗尺度可能：

$$
\Phi_c
$$

非常簡單，

細尺度：

$$
\Phi_f
$$

非常複雜。

真正要求的是：

$$
\boxed{
\text{coarse dynamics reproduce
task-relevant fine outcomes}.
}
$$

這和物理 coarse-graining / effective theory 有類比，

但本文不宣稱使用 renormalization group。

---

# 34. 不要偷渡 Renormalization Group

如果要叫：

$$
\text{renormalization},
$$

需要：

- scale transformation；
- parameter flow；
- fixed points；
- universality；
- well-defined coarse-graining map。

目前 TADC 尚未建立。

所以本文只使用：

$$
\boxed{
\text{coarse-graining}
}
$$

與：

$$
\boxed{
\text{multiscale re-indexing}.
}
$$

不使用 RG 作為正式機制。

---

# 35. Scale Change 與 TADC-03 六算子

Re-indexing：

$$
R
$$

直接改變尺度。

但其他算子也可能是 scale-dependent。

例如：

$$
E_{\lambda_f}
\neq
E_{\lambda_c}.
$$

細尺度 Expansion：

可能找到 local relation。

粗尺度 Expansion：

可能找到 whole-domain bridge。

因此：

$$
\boxed{
O^{(\lambda_f)}
\neq
O^{(\lambda_c)}
}
$$

一般成立。

---

# 36. Operator–Scale Non-Commutativity

可能：

$$
R^-E
\neq
ER^-.
$$

先 Expansion 再 coarse-grain：

$$
R^-(
E(U)
)
$$

與先 coarse-grain 再 Expansion：

$$
E(
R^-(U)
)
$$

可能得到不同結果。

同樣：

$$
R^-G
\neq
GR^-.
$$

所以 TADC-03 的 non-commutativity 現在增加一個新來源：

$$
\boxed{
\text{operator order}
+
\text{observation scale}.
}
$$

---

# 37. Scale Hysteresis

從：

$$
\lambda_f
\rightarrow
\lambda_c
\rightarrow
\lambda_f
$$

未必回到同一 representation。

即：

$$
F(P(U))
\neq
U.
$$

如果第一次 coarse-graining 已改變：

- memory；
- weighting；
- chunking；
- relation strength；

那回到 fine scale：

$$
\widetilde U
$$

可能不同。

這就是：

$$
\boxed{
\text{scale hysteresis}.
}
$$

仍需和一般 memory reconstruction 區分。

---

# 38. Nested Domains 不代表無限嵌套

理論上可以寫：

$$
U_0
\subset
U_1
\subset
U_2
\subset\cdots.
$$

但實際 cognition 受限於：

$$
B
=
\text{finite cognitive budget}.
$$

所以實際有效 nesting depth：

$$
L_{\mathrm{eff}}
$$

應有限。

因此：

$$
\boxed{
\text{conceptual unbounded nesting}
\neq
\text{simultaneously represented infinite nesting}.
}
$$

這是必要的 boundedness 條件。

---

# 39. Effective Nesting Depth

定義：

$$
L_{\mathrm{eff}}
=
\max
\left\{
n:
U_0\prec U_1\prec\cdots\prec U_n
\text{ is behaviorally distinguishable}
\right\}.
$$

這是一個可測量概念。

不同任務、訓練程度與個體：

$$
L_{\mathrm{eff}}
$$

可能不同。

---

# 40. Nested Breadth 與 Nested Depth

兩個不同維度：

$$
B_{\mathrm{nest}}
=
\text{number of siblings / parallel subdomains},
$$

$$
D_{\mathrm{nest}}
=
\text{maximum nesting depth}.
$$

因此：

$$
\boxed{
\text{broad cognition}
\neq
\text{deeply nested cognition}.
}
$$

一個系統可以 breadth 高、depth 低；

也可以 breadth 低、depth 高。

---

# 41. Vertical 與 Horizontal Attention

因此可以暫定：

### Horizontal Traversal

同尺度：

$$
\lambda_i=\lambda_j.
$$

### Vertical Re-indexing

跨尺度：

$$
\lambda_i\neq\lambda_j.
$$

所以一條 trajectory：

$$
\gamma
$$

可以分成：

$$
\gamma_H
+
\gamma_V.
$$

高階 cognition 可能同時需要：

$$
\boxed{
\text{horizontal mobility}
+
\text{vertical mobility}.
}
$$

---

# 42. 「高速切換」也可能其實是高階水平遍歷

如果 subject 已將：

$$
D_1,D_2,D_3
$$

在 coarse scale 壓成三個 objects：

$$
z_1,z_2,z_3,
$$

那：

$$
z_1\rightarrow z_2\rightarrow z_3
$$

可以非常快。

外部研究者若用 fine-grained discipline labels 看，

可能以為：

$$
\text{large domain switching}.
$$

但 subject 的 internal scale：

$$
\lambda_c
$$

可能只是在同一 high-level chart 中 horizontal traversal。

因此：

$$
\boxed{
\text{observed switching cost depends on
which scale is treated as the unit}.
}
$$

這提供了一個很重要的 measurement warning。

---

# 43. 反過來：同一個「領域」內也可能需要巨大 vertical cost

外部 label：

$$
D_{\mathrm{math}}
$$

保持不變，

但 subject 從：

$$
\text{theorem-level}
$$

切到：

$$
\text{symbol-level proof audit}
$$

可能需要：

$$
R^+.
$$

這可能比從 theorem A 跳 theorem B 更昂貴。

因此：

$$
\boxed{
\text{same disciplinary domain}
\not\Rightarrow
\text{same cognitive scale}.
}
$$

---

# 44. Scale–Goal Coupling

最佳尺度依 goal：

$$
\lambda^*
=
\lambda^*(G).
$$

例如：

### Planning

$$
\lambda^*\uparrow
$$

偏粗。

### Verification

$$
\lambda^*\downarrow
$$

偏細。

### Exploration

可能需要：

$$
\lambda_c
\leftrightarrow
\lambda_f
$$

頻繁切換。

因此：

$$
\boxed{
\text{attention scope}
\neq
\text{fixed personal trait only}.
}
$$

它也可能是 task policy。

---

# 45. Attention Depth 與 Attention Scope

本文將：

$$
d_A
=
\text{attention depth},
$$

$$
s_A
=
\text{attention scope}
$$

分離。

高 depth：

$$
d_A\uparrow
$$

不一定代表：

$$
s_A\downarrow.
$$

一個 nested domain 中可以同時：

$$
d_A\uparrow
$$

且：

$$
s_A\uparrow
$$

如果高階 object 已經 coarse-grain 多個 subdomains。

因此：

$$
\boxed{
\text{deep attention}
\neq
\text{necessarily narrow attention}.
}
$$

這將對 TADC-05 的 hyperfocus 分析非常重要。

---

# 46. 多尺度注意配置

定義：

$$
\mathbf a_t
=
(
\lambda_t,
d_t,
s_t,
\nu_H,
\nu_V
),
$$

其中：

- \(\lambda_t\)：current resolution；
- \(d_t\)：depth；
- \(s_t\)：scope；
- \(\nu_H\)：horizontal traversal rate；
- \(\nu_V\)：vertical re-indexing rate。

因此：

$$
\boxed{
\text{attention state}
}
$$

不應只用：

$$
\text{focus intensity}
$$

描述。

---

# 47. Null Model 1：Fixed Hierarchy Model

假設：

$$
H
$$

從頭到尾固定。

cognition 只是在：

$$
H
$$

上切換 node。

如果這就能完整解釋：

- switch cost；
- abstraction；
- behavior；
- neural decoding；
- generalization；

則：

$$
\boxed{
\text{dynamic re-indexing is unnecessary}.
}
$$

---

# 48. Null Model 2：Single-Resolution Model

假設所有 task behavior 都可以在同一 latent representation：

$$
Z
$$

中解釋。

不同「尺度」只是研究者後處理。

如果：

$$
M_{\mathrm{single}}
$$

與 multiscale model：

$$
M_{\mathrm{multi}}
$$

預測力相同，

則 SRMMC 沒必要。

---

# 49. Null Model 3：Chunking Only

object–domain duality 可能完全是：

$$
\boxed{
\text{chunking}.
}
$$

如果一個 chunk：

$$
z_U
$$

只是在 working memory / long-term memory 中形成一個單位，

就可以解釋所有 coarse-scale behavior，

則：

$$
\text{ODDC}
$$

不需獨立存在。

TADC 只有在：

- nested relations；
- cross-scale routing；
- scale-dependent operators；
- invariants；

提供額外預測時才有增量。

---

# 50. Null Model 4：Analyst-Only Hierarchy

研究者總能對任何資料做 clustering：

$$
\mathcal D
\rightarrow
\text{hierarchy}.
$$

所以找到「多尺度結構」本身幾乎沒有意義。

真正證據必須要求：

$$
\boxed{
\text{participant behavior predicts the same hierarchy}.
}
$$

或：

$$
\boxed{
\text{neural representation independently recovers it}.
}
$$

---

# 51. 實驗一：Object ↔ Domain Re-indexing

建立人工 hierarchy：

$$
U_i
=
\{x_{i1},x_{i2},x_{i3},x_{i4}\}.
$$

Block A：

只問：

$$
U_i
$$

間的 high-level relations。

Block B：

要求進入：

$$
U_i
$$

內處理：

$$
x_{ij}.
$$

Block C：

再回 high-level。

測：

- RT；
- switch cost；
- memory precision；
- neural decoding；
- generalization；
- hierarchical error pattern。

如果：

$$
U_i
$$

能在 A / C 呈現 unit-like behavior，

而在 B 展開成 internal relational domain，

支持 ODDC。

---

# 52. 實驗二：Scale-Specific Switching

比較：

### Horizontal switch

$$
U_A^{(\lambda_c)}
\rightarrow
U_B^{(\lambda_c)}.
$$

### Vertical switch

$$
U_A^{(\lambda_c)}
\rightarrow
x_{A1}^{(\lambda_f)}.
$$

匹配 sensory / motor demand。

若：

$$
K_H
\neq
K_V,
$$

且 neural reconfiguration pattern 不同，

支持 horizontal / vertical operation distinction。

---

# 53. 實驗三：Coarse-Graining Fidelity

participants 學習 fine graph：

$$
\mathcal G_f.
$$

之後要求產生 coarse summary：

$$
\mathcal G_c.
$$

再只依 coarse representation 預測新情境。

定義 fidelity：

$$
F_P
=
\operatorname{PredictiveAccuracy}
(
\mathcal G_c
\rightarrow
Y_f
).
$$

如果 experts / trained participants：

$$
F_P\uparrow,
$$

可測「高品質 coarse-graining」。

---

# 54. 實驗四：Cross-Scale Routing Advantage

Task A 強迫：

$$
\lambda_f
$$

一路完成。

Task B 允許：

$$
\lambda_f
\rightarrow
\lambda_c
\rightarrow
\lambda_f.
$$

比較：

$$
K,
$$

$$
T,
$$

$$
Accuracy.
$$

若：

$$
K_{\mathrm{multi}}
<
K_{\mathrm{fine-only}}
$$

且 accuracy 不下降，

支持 MRC。

---

# 55. 實驗五：Scale-Consistency Test

建立 fine-scale dynamic task：

$$
\Phi_f.
$$

由 participant 自己形成 coarse categories。

測：

$$
P\Phi_f
$$

與：

$$
\Phi_cP.
$$

若：

$$
P\Phi_f
\approx
\Phi_cP,
$$

代表 coarse model 具有動態有效性。

如果完全不一致：

$$
\mathcal C_c
$$

只是壓縮描述，

不是有效 cognitive model。

---

# 56. 實驗六：Nested Depth

建立：

$$
L=1,2,3,4,\ldots
$$

不同 nesting depths。

測：

- accuracy；
- RT；
- memory；
- neural representation；
- re-indexing cost。

估計：

$$
L_{\mathrm{eff}}.
$$

若 behavior 完全不區分 hierarchy depth，

NADC 的 functional significance 受損。

---

# 57. 實驗七：Scale Hysteresis

流程：

$$
\lambda_f
\rightarrow
\lambda_c
\rightarrow
\lambda_f.
$$

比較最終：

$$
\widetilde{\mathcal C}_f
$$

與原：

$$
\mathcal C_f.
$$

如果：

$$
\widetilde{\mathcal C}_f
\neq
\mathcal C_f,
$$

再測差異是否超越普通 forgetting / reconstruction。

只有在 history-specific pattern 存在時，

才支持 scale hysteresis。

---

# 58. 七個核心可證偽命題

## TADC4-H1 — Nested Representation

至少部分 cognition 能形成：

$$
U_1\prec U_2\prec\cdots
$$

且 hierarchy level 可由 behavior / neural representation 獨立辨識。

---

## TADC4-H2 — Object–Domain Duality

同一：

$$
U
$$

可在不同 task scale 呈現：

$$
\text{unit-like}
$$

與：

$$
\text{domain-like}
$$

雙重功能。

---

## TADC4-H3 — Horizontal / Vertical Cost Difference

$$
K_H
\neq
K_V
$$

在適當匹配條件下可重現。

---

## TADC4-H4 — Multiscale Routing Advantage

至少某類 hierarchical task：

$$
P_{\mathrm{multi}}
>
P_{\mathrm{single-scale}}.
$$

---

## TADC4-H5 — Coarse-Graining Preserves Invariants

存在：

$$
I
$$

使：

$$
I(P(\mathcal C_f))
\approx
I(\mathcal C_f).
$$

---

## TADC4-H6 — Scale-Dependent Operator Effects

至少一個：

$$
O
$$

滿足：

$$
O^{(\lambda_f)}
\neq
O^{(\lambda_c)}.
$$

---

## TADC4-H7 — Multiscale Model Adds Prediction

$$
M_{\mathrm{multi}}
$$

對 unseen behavior / neural patterns 的預測必須穩定優於：

$$
M_{\mathrm{fixed-hierarchy}}
$$

與：

$$
M_{\mathrm{single-resolution}}.
$$

---

# 59. 什麼會真正殺掉本篇？

## F1 — No Cognitive Scale Effect

若所有 scale manipulations 只改 task difficulty，

沒有獨立 representational effect，

SRMMC 失敗。

---

## F2 — Object–Domain Duality Collapses to Chunking

若：

$$
\text{chunking model}
$$

完整解釋所有 unit/domain behavior，

ODDC 無增量。

---

## F3 — No Horizontal / Vertical Distinction

若：

$$
K_H
\approx
K_V
$$

且 neural reconfiguration 也無差異，

multiscale switching language 被削弱。

---

## F4 — Coarse Models Have No Predictive Validity

若：

$$
P\Phi_f
\not\approx
\Phi_cP
$$

普遍成立，

則 coarse macro-domain 只是方便描述。

---

## F5 — No Invariant

若所有：

$$
I
$$

都在 scale change 後崩解，

沒有任何 task-relevant structure 保持，

「同一結構跨尺度」這個說法需要重寫。

---

## F6 — Hierarchy Is Always Fixed

如果所有資料都由固定：

$$
H
$$

上的 node switching 解釋，

dynamic re-indexing 不需要。

---

## F7 — Scale Exists Only in Analyst Choice

若 participant / neural data 不支持任何特定：

$$
\lambda,
$$

則本文的尺度結構只是分析框架，

不是 cognitive mechanism。

---

# 60. Macro / Micro 的三種意義必須分開

本文最後特別區分：

## 60.1 Physical Macro / Micro

例如 neural population vs whole brain network。

---

## 60.2 Representational Macro / Micro

例如：

$$
\text{feature}
\subset
\text{object}
\subset
\text{task}
\subset
\text{context}.
$$

---

## 60.3 Goal-Relative Macro / Micro

同一 object 在不同 goal 中可能被提升或下降尺度。

TADC-04 主要研究：

$$
\boxed{
\text{representational}
+
\text{goal-relative macro/micro}.
}
$$

不能拿來直接推論物理腦尺度。

---

# 61. Scale Relativity 與 Observer Relativity

若：

$$
\mathcal O_{\lambda_1}
\neq
\mathcal O_{\lambda_2},
$$

則：

$$
\mathcal C^{(\lambda_1)}
\neq
\mathcal C^{(\lambda_2)}.
$$

所以：

$$
\boxed{
\text{same underlying cognitive process
can admit different valid descriptions}.
}
$$

但有效描述必須滿足：

1. 可重現；
2. 可預測；
3. 和 behavior / neural data 對應；
4. scale transition 有明確規則。

因此：

$$
\boxed{
\text{observer-relative}
\neq
\text{truth-relative}.
}
$$

---

# 62. 一個重要結果：宏觀鎖定與微觀切換可能是同一件事的不同投影

假設 coarse scale：

$$
\mathcal O_{\lambda_c}(\gamma)
$$

顯示 trajectory 長期留在：

$$
U^*.
$$

所以：

$$
P(
U^*
)
\rightarrow1.
$$

但 fine scale：

$$
\mathcal O_{\lambda_f}(\gamma)
$$

可能看到：

$$
x_1\rightarrow x_7\rightarrow x_{13}\rightarrow x_{22}\rightarrow\cdots
$$

高速切換。

因此：

$$
\boxed{
\text{macro persistence}
+
\text{micro mobility}
}
$$

可以不是矛盾，

而只是：

$$
\boxed{
\text{one trajectory observed at two resolutions}.
}
$$

這個結果將直接成為 TADC-05 的入口。

---

# 63. 深度專注與高切換率也不必矛盾

如果：

$$
x_i
$$

全部屬於：

$$
U^*,
$$

則：

$$
\nu_{\mathrm{fine}}
\uparrow
$$

可以同時：

$$
P(U^*)\uparrow.
$$

所以：

$$
\boxed{
\text{high micro-switching}
\not\Rightarrow
\text{low macro-focus}.
}
$$

但這只在：

$$
x_i
$$

具有高 domain coherence 時成立。

若切換是：

$$
U^*
\rightarrow
V_{\mathrm{irrelevant}},
$$

則是另一種現象。

---

# 64. TADC-05 的自然入口：Topological Hyperfocus

如果 hyperfocus 只定義：

$$
P(x^*)\rightarrow1,
$$

那高速 internal mobility 無法被表示。

但若：

$$
P(U^*)\rightarrow1
$$

而：

$$
H(
X\mid U^*
)
$$

仍很高，

則可能存在：

$$
\boxed{
\text{domain-level persistence
with high internal entropy}.
}
$$

TADC-05 將正式比較：

- pointwise hyperfocus；
- domain hyperfocus；
- topological hyperfocus。

本文只建立 multiscale 基礎。

---

# 65. 與現有文獻的最保守整合

目前已有研究支持：

$$
\boxed{
\text{nested cognitive maps exist in specific tasks}
}
$$

（Peer & Epstein, 2025）。

已有研究支持：

$$
\boxed{
\text{hierarchical concept levels are neurally represented}
}
$$

（Mack et al., 2021）。

已有研究支持：

$$
\boxed{
\text{hierarchical control levels show distinct
reconfiguration dynamics}
}
$$

（Leach et al., 2026）。

已有研究支持：

$$
\boxed{
\text{nested structures can be dynamically constructed
through rapid neural sequences}
}
$$

（2025 PNAS）。

但目前仍沒有充分證據直接支持：

$$
\boxed{
\text{all macro/micro cognitive distinctions
are scale-relative re-indexings}.
}
$$

這仍是本文自己的強猜想。

---

# 66. 系列統一

TADC-01：

$$
\boxed{
\mathcal C_t
\text{ can change?}
}
$$

TADC-02：

$$
\boxed{
D_t
\text{ can be dynamically induced?}
}
$$

TADC-03：

$$
\boxed{
\mathcal O
=
\{E,C,T,G,D,R\}
}
$$

TADC-04：

$$
\boxed{
\mathcal O_\lambda
\text{ determines which distinctions count as objects/domains.}
}
$$

因此目前最小總模型：

$$
\boxed{
\mathcal C_t^{(\lambda_t)}
=
\mathcal O_{\lambda_t}
(
\mathcal C_t
)
}
$$

以及：

$$
\boxed{
\mathcal C_{t+1}^{(\lambda_{t+1})}
=
R_{\lambda_t\rightarrow\lambda_{t+1}}
\circ
O_t
(
\mathcal C_t^{(\lambda_t)}
).
}
$$

---

# 67. 結論

本文提出四個主要猜想。

第一：

$$
\boxed{
\textbf{NADC}
}
$$

有效認知域可以形成嵌套的多層結構，

但一般不必限制為單一 tree。

第二：

$$
\boxed{
\textbf{ODDC}
}
$$

同一結構：

$$
U
$$

可在細尺度是：

$$
\text{domain},
$$

在粗尺度是：

$$
\text{object}.
$$

因此：

$$
\boxed{
\text{object/domain}
}
$$

可能是表示尺度相對的功能身份。

第三：

$$
\boxed{
\textbf{SRMMC}
}
$$

macro / micro 應被定義成：

$$
\operatorname{Micro}(A,B),
$$

而不是絕對屬性。

第四：

$$
\boxed{
\textbf{CSIC}
}
$$

若 multiscale cognition 具有理論內容，

則不同尺度之間必須存在某些可測的：

$$
\text{invariants}
$$

或：

$$
\text{scale-consistent dynamics}.
$$

因此：

$$
\boxed{
P\circ\Phi_f
\approx
\Phi_c\circ P
}
$$

成為本篇最重要的跨尺度判準之一。

這讓「宏觀／微觀只是相對的」從哲學敘述轉成可以被實驗擊敗的命題。

若：

- participant 沒有真正 scale-sensitive representation；
- object/domain duality 完全等同 ordinary chunking；
- coarse-graining 沒有 predictive validity；
- 沒有任何 cross-scale invariant；
- fixed hierarchy 就能完整解釋資料；

那麼 TADC-04 的強版本必須被拒絕。

反之，如果：

$$
\boxed{
\text{同一認知結構確實能在不同尺度間被穩定重索引，
並以跨尺度不變量維持其功能身份，}
}
$$

則注意力研究就需要新增一個問題：

> **目前注意的不只是「哪個對象」，而是「目前把世界切在哪一個解析尺度」。**

這也使 TADC 的核心由：

$$
\text{attention allocation}
$$

進一步變成：

$$
\boxed{
\text{attention allocation}
+
\text{space transformation}
+
\text{scale selection}.
}
$$

而下一篇 TADC-05 將直接處理這個結果的極端情形：

$$
\boxed{
\text{如果一個人長期鎖定的不是單一點，
而是一個可以持續展開、收斂與內部遍歷的連通認知域，
那還應不應把它叫作「超專注」？}
}
$$

---

# 參考文獻

1. Peer M, Epstein RA. **Cognitive maps for hierarchical spaces in the human brain.** *Cerebral Cortex*. 2025;35(9):bhaf261. doi:10.1093/cercor/bhaf261. PMID: 40982478.  
2. Leach SC, Chen X, Hwang K. **Hierarchical Reconfiguration of Neurocognitive Task Set Representations Mediates Cognitive Flexibility.** *Journal of Neuroscience*. 2026. doi:10.1523/JNEUROSCI.0113-26.2026. PMID: 42276789.  
3. Mack ML, Preston AR, Love BC. **Learning and Representation of Hierarchical Concepts in Hippocampus and Prefrontal Cortex.** *Journal of Neuroscience*. 2021. PMID: 34330775.  
4. **Building hierarchically nested structure by rapid neural sequences.** *Proceedings of the National Academy of Sciences*. 2025;122(50):e2507417122. PMID: 41379999.  
5. Tan L, Qiu Y, Qiu L, et al. **The medial and lateral orbitofrontal cortex jointly represent the cognitive map of task space.** *Communications Biology*. 2025;8:163. doi:10.1038/s42003-025-07588-w. PMID: 39900714.  
6. Qiu Y, Li H, Liao J, et al. **Forming cognitive maps for abstract spaces: the roles of the human hippocampus and orbitofrontal cortex.** *Communications Biology*. 2024;7:517. doi:10.1038/s42003-024-06214-5. PMID: 38693344.  
7. **Two-dimensional neural geometry underpins hierarchical organization of sequence in human working memory.** *Nature Human Behaviour*. 2025;9(2):360–375. PMID: 39511344.  
8. Qiu Y, et al. **Dynamic changes in orbitofrontal-hippocampal connectivity linked to cognitive map formation in humans.** *NeuroImage*. 2025;318:121415. PMID: 40780573.  
9. Garvert MM, Dolan RJ, Behrens TEJ. **A map of abstract relational knowledge in the human hippocampal-entorhinal cortex.** *eLife*. 2017;6:e17086. doi:10.7554/eLife.17086.  
10. Park SA, Miller DS, Nili H, Ranganath C, Boorman ED. **Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps.** *Neuron*. 2020;107(6):1226–1238.e8. doi:10.1016/j.neuron.2020.06.030.  
11. Behrens TEJ, Muller TH, Whittington JCR, et al. **What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior.** *Neuron*. 2018;100(2):490–509. doi:10.1016/j.neuron.2018.10.002.  
12. Theves S, Fernández G, Doeller CF. **The hippocampal-entorhinal system represents nested hierarchical relations between words during concept learning.** *Hippocampus*. 2021. PMID: 33675679.  

---

## 與系列的關係

**已完成：**

- TADC-01：《注意力不是單點選擇——可變認知空間與注意—空間轉換猜想》
- TADC-02：《動態認知域——領域作為局部座標圖》
- TADC-03：《拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引》
- TADC-04：《嵌套注意域與觀察尺度——宏觀／微觀的相對性與多尺度重索引》

**下一篇：**

- TADC-05：《從單點超專注到拓樸超專注》

後續：

- TADC-06：《關係優先認知與跨域連續性》
- TADC-07：《外部認知支架與人—AI 認知拓樸》
- TADC-08：《拓樸注意力的測量、反證與工程化》

---

**狀態：** TADC-04 v0.1  
**原始人體／臨床數據：** 無  
**理論狀態：** 猜想／研究綱領；未經實驗驗證  
**尺度狀態：** \(\lambda\) 為候選認知／表示解析度，不是已確認神經尺度  
**拓樸狀態：** 尚未證明存在嚴格跨尺度拓樸不變量；CSIC 為待驗證猜想
