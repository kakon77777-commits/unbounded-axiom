# 分級遞歸知道代數：Epistemic Tower、升階、降階與 Meta-Residual

**English title:** A Graded Algebra of Recursive Knowing: Epistemic Towers, Lifts, Projections, and Meta-Residuals

**Series:** Recursive Knowing-Difference Algebra / 遞歸知差代數系列  
**Paper ID:** EML-RKD-02  
**Version:** v0.1  
**Date:** 2026-08-16  
**Author:** Neo.K（許筌崴）  
**Affiliation:** EveMissLab / 一言諾科技有限公司  
**Document status:** FORMAL EXTENSION OF CONJECTURE / ALGEBRAIC FOUNDATION  
**Upstream:** EML-RKD-01 — Recursive Knowing-Difference Conjecture  
**Claim strength:** 本文建立一個候選分級代數框架，並在明確附加條件下證明若干內部命題。本文不宣稱此代數已被證明為所有認知存在的唯一或普遍模型，也不宣稱形式上的高階狀態自動等同於第一人稱意義上的「知道」。

---

## 摘要

EML-RKD-01 提出遞歸知差命題猜想：對存在 $X$，相鄰 epistemic recursion levels 是否存在合法、可觀察且可比較的有效差？第一篇刻意沒有回答「不同階的知道究竟是什麼數學物件」。本文開始補上這個空白。

本文不把「知道 $p$ 」「知道自己知道 $p$ 」「知道自己知道自己知道 $p$ 」強迫放入同一狀態空間，而定義一族分級 epistemic spaces：

$$
\mathcal E_X^{(0)},
\mathcal E_X^{(1)},
\mathcal E_X^{(2)},
\ldots
$$

並引入升階算子 $K_{X,n}$ 與降階／目標投影算子 $F_{X,n}$：

$$
K_{X,n}:
\mathcal E_X^{(n)}
\rightharpoonup
\mathcal E_X^{(n+1)},
$$

$$
F_{X,n}:
\mathcal E_X^{(n+1)}
\rightharpoonup
\mathcal E_X^{(n)}.
$$

 $K_{X,n}$ 表示由第 $n$ 階建立一個第 $n+1$ 階候選 meta-state； $F_{X,n}$ 不表示心理上的「遺忘」，而是把一個高階 state 投回它所聲稱指向、評估或保留的低階 epistemic target。由此可以定義 exact target coherence：

$$
F_{X,n}K_{X,n}=id,
$$

以及不滿足 exact coherence 時的 recursive target defect。

在線性／可加 realization 中，本文進一步定義 pure meta-space：

$$
\mathcal M_{X,n+1}
=
\ker F_{X,n},
$$

並在存在 section $\iota_{X,n}$ 時將高一階 state 分解為低階可回收部分與 pure meta-residual：

$$
e_{n+1}
=
\iota_{X,n}(e_n)
+
m_{n+1},
\qquad
m_{n+1}\in\mathcal M_{X,n+1}.
$$

本文證明：若 $F_{X,n}K_{X,n}=id$，則 $K_{X,n}$ 在其定義域上為 injective，且 $F_{X,n}$ 對被 $K$ 覆蓋的低階域為 surjective；在模／向量空間條件下，若 $F$ 有線性 section，則得到 split short exact sequence，並可將高階 state 空間分解為低階嵌入像與 meta-kernel 的直和。對不能使用線性結構的存在，本文改以 fiber：

$$
F_{X,n}^{-1}(e_n)
$$

描述「所有仍指向同一低階 target 的高階變體」，避免把 kernel 當成普遍本體。

本文最後建立跨存在 tower morphism、觀察 realization 與一組 No-Go：輸出不同不推出 meta-residual 非零；形式升階不推出正確 knowing； $F K=id$ 只保證 target recovery，不證明高階 state 具有真實性、正當性或意識性。本文因此提供 EML-RKD-01 所需的第一個 type-safe algebraic skeleton，但保留 inverse-limit existence、結構／功能量化與上下界問題給後續文章。

**關鍵詞：** 遞歸知道；分級代數；epistemic tower；meta-residual；升階；降階；forgetful map；fiber；kernel；短正合序列；元認知；人工智慧；多智能體

---

## Abstract

This paper develops the first algebraic layer of the Recursive Knowing-Difference series. Rather than forcing first-order and higher-order knowing states into a single state space, it introduces graded epistemic spaces $\mathcal E_X^{(n)}$, recursive lifts $K_{X,n}$, and target projections $F_{X,n}$.

The equation $F_{X,n}K_{X,n}=id$ is interpreted as exact target coherence: a higher-order state, when projected to the lower level it purports to concern, recovers the original lower-order epistemic state. In additive or linear realizations, the kernel $\ker F_{X,n}$ defines a pure meta-space. When a section exists, a higher-order state can be decomposed into an embedded lower-order component and a meta-residual. In non-linear settings, fibers replace kernels as the more general representation.

The construction is carrier-neutral and does not identify formal higher-order states with consciousness, truth, or justified knowledge. It provides a typed algebraic skeleton for later work on inverse limits, recursive novelty, fidelity, information gain, structural rank, and recursive bounds.

---

# 1. 從命題猜想到代數骨架

EML-RKD-01 的母問題是：

$$
\boxed{
\text{相鄰 epistemic recursion levels 是否存在合法、可觀察、可比較的有效差？}
}
$$

要回答這個問題，第一個障礙並不是「怎麼量」，而是：

$$
\boxed{
\text{究竟在量哪兩個物件？}
}
$$

若直接寫：

$$
K^{n+1}(p)-K^n(p),
$$

就已經偷偷假設：

1. 每一階 knowing state 都屬於同一 space；
2. 存在共同加法；
3. 不同階可直接比較；
4. 高一階確實指向低一階；
5. $K$ 可無條件反覆自組合。

本文全部不預設。

因此真正的起點是：

$$
\boxed{
\text{typed before measured}.
}
$$

---

# 2. 存在 $X$ 與分級 epistemic object

固定某一研究中的存在：

$$
X.
$$

本文不要求 $X$ 是人類，也不要求它是單一物理載體。

對每一遞歸階：

$$
n\in\mathbb N_0,
$$

定義一個 epistemic state space：

$$
\boxed{
\mathcal E_X^{(n)}.
}
$$

因此整體可形式化為分級物件：

$$
\boxed{
\mathcal E_X
=
\bigsqcup_{n\ge0}
\mathcal E_X^{(n)}.
}
$$

若後續 realization 支持可加結構，也可以寫：

$$
\boxed{
\mathcal E_X
=
\bigoplus_{n\ge0}
\mathcal E_X^{(n)}.
}
$$

但直和不是本文的普遍前提。

---

# 3. Degree 的語義

本文使用以下最小解讀。

- $\mathcal E_X^{(0)}$：base epistemic contents / targets；
- $\mathcal E_X^{(1)}$：對 base target 的一階 epistemic states；
- $\mathcal E_X^{(2)}$：對一階 epistemic state 的 meta-states；
- $\mathcal E_X^{(n+1)}$：對第 $n$ 階 epistemic state 的下一階候選 meta-state。

這不是說每一個 $e_{n+1}$ 都必然是合法 knowing。

因此我們必須區分：

$$
\boxed{
\text{higher-order state}
}
$$

與：

$$
\boxed{
\text{valid higher-order knowing state}.
}
$$

前者是代數候選物；後者還需要 target、truth、reliability、observation 或其他契約。

---

# 4. 升階算子 $K_{X,n}$

定義部分映射：

$$
\boxed{
K_{X,n}:
\mathcal E_X^{(n)}
\rightharpoonup
\mathcal E_X^{(n+1)}.
}
$$

對：

$$
e_n\in\operatorname{dom}(K_{X,n}),
$$

令：

$$
e_{n+1}
=
K_{X,n}(e_n).
$$

 $K_{X,n}$ 的語義是：

> 由存在 $X$ 的第 $n$ 階 epistemic state，形成一個第 $n+1$ 階候選 state，使其聲稱、表現或操作性地對第 $n$ 階 state 進行 meta-level 評估、監控、確認、否定、置信判定、校準或其他高階處理。

本文不要求所有 $K_{X,n}$ 相同。

因此一般不寫：

$$
K_X^n.
$$

只有在存在額外同型化或共同 endomorphism 結構時，才可簡寫。

---

# 5. 降階／目標投影算子 $F_{X,n}$

定義部分映射：

$$
\boxed{
F_{X,n}:
\mathcal E_X^{(n+1)}
\rightharpoonup
\mathcal E_X^{(n)}.
}
$$

它的語義不是「認知存在真的忘掉了一層」。

 $F_{X,n}$ 是一個分析／結構映射：

> 把一個高階 state 投回它在第 $n$ 階所聲稱指涉、評估或保留的 epistemic target。

因此可稱：

- target projection；
- epistemic lowering map；
- forgetful map；
- lower-level recovery map。

本文在 canonical notation 中使用：

$$
\boxed{
F_{X,n}.
}
$$

---

# 6. Exact Target Coherence

最乾淨的情形是：

$$
\boxed{
F_{X,n}
\circ
K_{X,n}
=
id
}
$$

在指定 domain 上成立。

也就是：

$$
e_n
\xrightarrow{K_{X,n}}
e_{n+1}
\xrightarrow{F_{X,n}}
e_n.
$$

本文稱此條件為：

$$
\boxed{
\textbf{Exact Target Coherence}.
}
$$

它表示：

> 高一階 state 至少沒有在「它究竟是在談哪一個低階 state」這件事上失配。

但它仍然不保證：

- $e_n$ 為真；
- $e_{n+1}$ 為真；
- $e_{n+1}$ 的 confidence 校準；
- $X$ 具有第一人稱意識；
- $e_{n+1}$ 具有額外資訊；
- $e_{n+1}$ 是 justified knowledge。

因此：

$$
\boxed{
F K=id
\not\Rightarrow
\text{truth or consciousness}.
}
$$

---

# 7. 命題 P2.1 — Section 性質

若：

$$
F_{X,n}K_{X,n}=id
$$

在集合 $D_n\subseteq\mathcal E_X^{(n)}$ 上成立，則：

$$
\boxed{
K_{X,n}|_{D_n}
\text{ is injective}.
}
$$

**證明。**

若：

$$
K_{X,n}(a)
=
K_{X,n}(b),
$$

兩側施加 $F_{X,n}$：

$$
F_{X,n}K_{X,n}(a)
=
F_{X,n}K_{X,n}(b).
$$

由 exact target coherence：

$$
a=b.
$$

故 $K_{X,n}$ 在 $D_n$ 上 injective。∎

---

# 8. 命題 P2.2 — Local Surjectivity

在同一條件下：

$$
\boxed{
F_{X,n}
:
K_{X,n}(D_n)
\rightarrow
D_n
}
$$

為 surjective。

**證明。**

對任意：

$$
e_n\in D_n,
$$

取：

$$
e_{n+1}=K_{X,n}(e_n).
$$

則：

$$
F_{X,n}(e_{n+1})
=
e_n.
$$

故每一個 $D_n$ 中的 state 都有至少一個位於 $K_{X,n}(D_n)$ 的高階 preimage。∎

注意：這不表示 $F_{X,n}$ 對整個 $\mathcal E_X^{(n)}$ 全域 surjective，只是對被 $K$ 覆蓋的研究域成立。

---

# 9. Target Defect

真實系統可能不滿足 exact coherence。

若 $\mathcal E_X^{(n)}$ 上存在 observer-contract-dependent pseudometric 或 loss：

$$
d_{X,n}^Q,
$$

則可定義：

$$
\boxed{
\varepsilon_{X,n}^Q(e_n)
=
d_{X,n}^Q
\left(
F_{X,n}K_{X,n}(e_n),
e_n
\right).
}
$$

稱為：

$$
\boxed{
\textbf{Recursive Target Defect}.
}
$$

當：

$$
\varepsilon_{X,n}^Q(e_n)=0,
$$

只表示在 $Q$ 的區分能力下 target recovery 無差。

如果 $d^Q$ 只是 pseudometric，仍可能有：

$$
F K(e_n)\neq e_n
$$

但：

$$
d^Q(FK(e_n),e_n)=0.
$$

因此 exact equality 與 observational indistinguishability 必須分開。

---

# 10. 高階 state 的「低階複製」問題

即使：

$$
F K=id,
$$

也可能：

$$
K(e_n)
$$

只是把 $e_n$ 用另一個容器包起來，沒有任何新的 meta-content。

所以必須再引入一個**零新增基準**。

令：

$$
\boxed{
\iota_{X,n}:
\mathcal E_X^{(n)}
\hookrightarrow
\mathcal E_X^{(n+1)}
}
$$

表示在指定 realization 中「只把低階 state 搬到高階表示空間，而不新增目標相關 meta-content」的 canonical embedding。

理想要求：

$$
\boxed{
F_{X,n}\iota_{X,n}=id.
}
$$

但 $\iota$ 是否存在、是否唯一，都不是普遍保證。

---

# 11. Meta-Residual：可加 realization

若：

1. $\mathcal E_X^{(n)}$ 與 $\mathcal E_X^{(n+1)}$ 為 compatible modules / vector spaces；
2. $K_{X,n}$ 與 $\iota_{X,n}$ 的輸出可以在同一加法結構內比較；

則定義：

$$
\boxed{
m_{X,n+1}(e_n)
=
K_{X,n}(e_n)
-
\iota_{X,n}(e_n).
}
$$

稱為：

$$
\boxed{
\textbf{Meta-Residual}.
}
$$

它的直覺是：

> 高一階候選 knowing state 中，在扣除「只是把原低階 state 搬上來」之後仍剩下的部分。

---

# 12. 命題 P2.3 — Meta-Residual 落入 kernel

若：

$$
F K=id
$$

且：

$$
F\iota=id,
$$

並假設 $F$ 線性，則：

$$
\boxed{
m_{X,n+1}(e_n)
\in
\ker F_{X,n}.
}
$$

**證明。**

$$
F(m)
=
F(K(e_n)-\iota(e_n))
$$

由線性：

$$
=
FK(e_n)-F\iota(e_n)
$$

$$
=
e_n-e_n
=
0.
$$

因此：

$$
m\in\ker F.
$$

∎

---

# 13. Pure Meta-Space

在線性 realization 中定義：

$$
\boxed{
\mathcal M_{X,n+1}
=
\ker F_{X,n}.
}
$$

其語義是：

> 所有在投回第 $n$ 階 target space 時消失，但在第 $n+1$ 階 representation 中仍存在的方向。

本文稱之為：

$$
\boxed{
\textbf{Pure Meta-Space}.
}
$$

但這個名稱需要非常小心。

 $\ker F$ 中的元素可能包括：

- 真正有用的 meta-information；
- 冗餘編碼；
- observer 不關心的 auxiliary states；
- noise directions；
- implementation-specific hidden variables。

所以：

$$
\boxed{
m\in\ker F
\not\Rightarrow
m\text{ is epistemically useful}.
}
$$

它只保證「不是由 target projection 保留下來的低階內容」。

---

# 14. Short Exact Extension

若：

$$
F_{X,n}:
\mathcal E_X^{(n+1)}
\rightarrow
\mathcal E_X^{(n)}
$$

為線性 surjection，則有：

$$
\boxed{
0
\longrightarrow
\mathcal M_{X,n+1}
\longrightarrow
\mathcal E_X^{(n+1)}
\xrightarrow{F_{X,n}}
\mathcal E_X^{(n)}
\longrightarrow
0.
}
$$

其中：

$$
\mathcal M_{X,n+1}
=
\ker F_{X,n}.
$$

這是一個 short exact sequence。

其認知語義是：

$$
\boxed{
\text{higher epistemic level}
}
$$

可被視為對 lower level 的一個 extension，而 kernel 收集所有在 lowering 後不可見的額外方向。

---

# 15. 命題 P2.4 — Split Extension

若上述 short exact sequence 存在線性 section：

$$
\iota_{X,n}:
\mathcal E_X^{(n)}
\rightarrow
\mathcal E_X^{(n+1)}
$$

滿足：

$$
F_{X,n}\iota_{X,n}=id,
$$

則：

$$
\boxed{
\mathcal E_X^{(n+1)}
\cong
\iota_{X,n}
\left(
\mathcal E_X^{(n)}
\right)
\oplus
\mathcal M_{X,n+1}.
}
$$

**證明草圖。**

對任意：

$$
y\in\mathcal E_X^{(n+1)},
$$

令：

$$
x=F(y).
$$

則：

$$
y
=
\iota(x)
+
\left(
y-\iota(F(y))
\right).
$$

第二項滿足：

$$
F
\left(
y-\iota(F(y))
\right)
=
F(y)-F\iota F(y)
=
x-x
=
0,
$$

故其位於 $\ker F=\mathcal M$。

若：

$$
z\in
\operatorname{Im}\iota
\cap
\ker F,
$$

寫：

$$
z=\iota(x).
$$

因 $F(z)=0$：

$$
x=F\iota(x)=0,
$$

故 $z=0$。

因此為直和分解。∎

---

# 16. Meta-Residual 的 canonical decomposition

在 split realization 中，任何：

$$
e_{n+1}\in\mathcal E_X^{(n+1)}
$$

都可以寫成：

$$
\boxed{
e_{n+1}
=
\iota_{X,n}(e_n)
+
m_{n+1},
}
$$

其中：

$$
e_n
=
F_{X,n}(e_{n+1}),
$$

以及：

$$
m_{n+1}
=
e_{n+1}
-
\iota_{X,n}F_{X,n}(e_{n+1}).
$$

這給出 projection-to-meta：

$$
\boxed{
P_{X,n}^{meta}
=
id
-
\iota_{X,n}F_{X,n}.
}
$$

並有：

$$
P^{meta}(e_{n+1})
\in
\mathcal M_{X,n+1}.
$$

在 exact split linear case：

$$
\boxed{
(P^{meta})^2=P^{meta}.
}
$$

所以它是一個投影算子。

---

# 17. No-Go N2.1 — Representation Difference 不等於 Meta-Residual

可能有：

$$
K(e_n)\neq\iota(e_n),
$$

但若這個差異只來自 observer-equivalent encoding，則它不能直接算作有效 meta-novelty。

因此：

$$
\boxed{
K(e_n)-\iota(e_n)\neq0
}
$$

仍然不保證：

$$
\boxed{
\text{effective recursive knowing difference}>0.
}
$$

後續 Paper 04 才會引入結構、功能、保真與資訊量化來處理這件事。

---

# 18. No-Go N2.2 — Kernel 非零不等於「會元認知」

即使：

$$
\ker F\neq\{0\},
$$

也可能整個 $K$ 的實際 image 永遠落在：

$$
\operatorname{Im}\iota.
$$

也就是：

$$
m_{n+1}(e_n)=0
$$

對所有考察 state 成立。

因此：

$$
\boxed{
\dim\ker F>0
}
$$

只代表存在 potential meta directions，

不代表 existence $X$ 真正 active 地使用它們。

---

# 19. Potential Meta-Space 與 Active Meta-Set

因此定義：

$$
\boxed{
\mathcal M_{X,n+1}^{pot}
=
\ker F_{X,n}.
}
$$

而對 task / content family：

$$
\mathcal P,
$$

定義 active residual set：

$$
\boxed{
\mathcal R_{X,n+1}^{act}(\mathcal P)
=
\left\{
m_{X,n+1}(e_n(p)):
p\in\mathcal P
\right\}.
}
$$

若在線性條件下需要 active subspace：

$$
\boxed{
\mathcal M_{X,n+1}^{act}(\mathcal P)
=
\operatorname{span}
\mathcal R_{X,n+1}^{act}(\mathcal P).
}
$$

Paper 04 將以此定義 potential rank 與 active rank。

本文只建立 algebraic object，不先量化。

---

# 20. 非線性情形：Fiber 優先於 Kernel

對一般認知存在，線性空間可能完全不合理。

因此回到：

$$
F_{X,n}:
\mathcal E_X^{(n+1)}
\rightarrow
\mathcal E_X^{(n)}.
$$

對固定：

$$
e_n\in\mathcal E_X^{(n)},
$$

定義 fiber：

$$
\boxed{
\mathcal F_{X,n}(e_n)
=
F_{X,n}^{-1}(e_n).
}
$$

其語義是：

> 所有在 lowering 後都指向同一個第 $n$ 階 epistemic target 的高階候選 states。

這是比 kernel 更一般的母概念。

在線性 case 中：

$$
F^{-1}(e_n)
$$

若非空，通常是一個 $\ker F$ 的 affine coset。

所以：

$$
\boxed{
\text{kernel model}
\subset
\text{fiber model}.
}
$$

---

# 21. Fiber-relative novelty

若有一個 zero-meta baseline：

$$
\iota(e_n)
\in
F^{-1}(e_n),
$$

則高階 state：

$$
e_{n+1}\in F^{-1}(e_n)
$$

的 meta-novelty 不必透過減法。

可以使用：

- fiber topology；
- fiber order；
- fiber graph distance；
- fiber divergence；
- quotient class；
- observational equivalence class。

因此一般記為：

$$
\boxed{
[e_{n+1}]_{meta,e_n}
}
$$

表示「相對於同一 target fiber 中 baseline 的 meta-class」。

這保留非線性 realization 的可能性。

---

# 22. Quotient-based Meta-Novelty

若 $\iota(\mathcal E^{(n)})$ 在 $\mathcal E^{(n+1)}$ 中形成合法 subobject，則可以考察 quotient：

$$
\boxed{
\mathcal Q_{X,n+1}
=
\mathcal E_X^{(n+1)}
/
\iota_{X,n}
\left(
\mathcal E_X^{(n)}
\right).
}
$$

對：

$$
e_{n+1},
$$

其 quotient class：

$$
\boxed{
[e_{n+1}]
\in
\mathcal Q_{X,n+1}
}
$$

表示忽略所有純低階嵌入成分後的 remainder class。

若：

$$
[e_{n+1}]=0,
$$

則在該 quotient regime 下沒有不可約高階剩餘。

但 quotient 的存在與語義依賴 category，不能把向量空間 quotient 無條件搬到所有 $X$。

---

# 23. 升階不一定唯一

同一個：

$$
e_n
$$

可能有多個合法 meta-lifts：

$$
K_{n}^{(1)}(e_n),
K_{n}^{(2)}(e_n),
\ldots
$$

因此一般更適合使用 lifting relation：

$$
\boxed{
\mathcal K_{X,n}
\subseteq
\mathcal E_X^{(n)}
\times
\mathcal E_X^{(n+1)}.
}
$$

若：

$$
(e_n,e_{n+1})
\in
\mathcal K_{X,n},
$$

表示 $e_{n+1}$ 是 $e_n$ 的一個 admissible recursive lift。

function-valued $K_{X,n}$ 是 relation-valued lifting 的特殊情形。

這對：

- 多 Agent；
- 多路 verifier；
- nondeterministic reasoning；
- stochastic cognition；
- 多種可接受自我解讀；

尤其重要。

---

# 24. 降階也不一定唯一

同一高階 state 也可能存在多個可接受 target interpretation。

因此可以把：

$$
F_{X,n}
$$

一般化成 relation：

$$
\boxed{
\mathcal F_{X,n}
\subseteq
\mathcal E_X^{(n+1)}
\times
\mathcal E_X^{(n)}.
}
$$

本文 canonical algebra 先使用 function notation，因為它便於建立 exact sequence、kernel 與 split extension；但 relation-valued generalization 保留為正式擴充。

---

# 25. Epistemic Path

一條有限遞歸 knowing path 定義為：

$$
\boxed{
\mathbf e_{\le N}
=
(e_0,e_1,\ldots,e_N)
}
$$

使對所有：

$$
0\le n<N,
$$

有：

$$
e_{n+1}
=
K_{X,n}(e_n)
$$

或在 relation-valued case：

$$
(e_n,e_{n+1})
\in
\mathcal K_{X,n}.
$$

若還要求 target coherence：

$$
F_{X,n}(e_{n+1})
=
e_n,
$$

則稱：

$$
\boxed{
\textbf{coherent finite epistemic path}.
}
$$

本文只建立有限 path。

無限 path、inverse system 與 projective limit 留給 EML-RKD-03。

---

# 26. 非交換的高階路徑

如果存在不同種類的 meta-operations：

$$
K_{n}^{a},
\qquad
K_{n}^{b},
$$

則一般不假設：

$$
K_{n+1}^{a}
K_n^{b}
=
K_{n+1}^{b}
K_n^{a}.
$$

例如：

- 先做 confidence estimation 再做 source verification；
- 先做 source verification 再做 confidence estimation；

可能形成不同的高階 state。

因此：

$$
\boxed{
\text{recursive depth}
}
$$

不一定足以唯一決定：

$$
\boxed{
\text{recursive state}.
}
$$

完整模型可能需要 path label：

$$
\pi
=
(a_0,a_1,\ldots,a_{n-1}).
$$

---

# 27. 同一階可能有不同 meta-type

因此可進一步細分：

$$
\mathcal E_X^{(n)}
=
\bigsqcup_{\tau\in T_n}
\mathcal E_{X,\tau}^{(n)}.
$$

 $\tau$ 可以表示：

- confidence；
- error monitoring；
- source attribution；
- self-modeling；
- justification checking；
- verifier state；
- other-agent modeling；
- uncertainty estimation。

所以：

$$
\boxed{
\text{degree}
\neq
\text{meta-type}.
}
$$

兩個 state 都是二階，不代表它們處理的是同一種 meta-information。

---

# 28. 存在 $X$ 的最小代數簽名

本文提出：

$$
\boxed{
\mathfrak A_X^{RKD}
=
\left\langle
\{
\mathcal E_X^{(n)}
\}_{n\ge0},
\{
K_{X,n}
\},
\{
F_{X,n}
\},
\{
\iota_{X,n}
\},
\sim_Q
\right\rangle.
}
$$

其中：

- $\mathcal E_X^{(n)}$：graded epistemic spaces；
- $K_{X,n}$：recursive lifts；
- $F_{X,n}$：target projections；
- $\iota_{X,n}$：zero-meta embeddings，若存在；
- $\sim_Q$：observer-contract-relative equivalence。

這是一個**候選最小簽名**，不是普遍唯一簽名。

---

# 29. Cross-Existence Tower Morphism

若要比較兩個存在：

$$
X,
\qquad
Y,
$$

不能因為都寫：

$$
\mathcal E^{(n)}
$$

就假設其內部 state 相同。

定義一族 comparison maps：

$$
\boxed{
T_n^{X\to Y}:
\mathcal E_X^{(n)}
\rightharpoonup
\mathcal E_Y^{(n)}.
}
$$

若滿足：

$$
\boxed{
F_{Y,n}
T_{n+1}^{X\to Y}
=
T_n^{X\to Y}
F_{X,n},
}
$$

則稱 lowering-compatible。

若更進一步：

$$
\boxed{
T_{n+1}^{X\to Y}
K_{X,n}
=
K_{Y,n}
T_n^{X\to Y},
}
$$

則稱 lift-compatible。

兩者皆成立時， $T_\bullet^{X\to Y}$ 保留遞歸 tower 結構。

---

# 30. 為什麼 morphism 比「同分數」更重要

假設人類 confidence score：

$$
0.8,
$$

AI verifier score：

$$
0.8.
$$

這兩個數字本身沒有推出：

$$
\boxed{
\text{same recursive knowing state}.
}
$$

真正需要的是某種：

$$
T_n^{human\to AI}
$$

或共同 observation realization，證明兩者在指定 $Q$ 下可以比較。

因此：

$$
\boxed{
\text{same range}
\not\Rightarrow
\text{same semantics}.
}
$$

---

# 31. Observation Realization

對 observer contract $Q$，定義：

$$
\boxed{
\Psi_{X,n}^{Q}:
\mathcal E_X^{(n)}
\rightarrow
\mathcal Z_{n,Q}.
}
$$

其中 $\mathcal Z_{n,Q}$ 是 observable state space。

若不同 level 要比較，還需要：

$$
\boxed{
A_{n\to n+1}^{Q}:
\mathcal Z_{n,Q}
\rightarrow
\mathcal Z_{n+1,Q}
}
$$

或共同 comparison domain：

$$
\mathcal Z_Q^\ast.
$$

因此 Paper 01 的：

$$
\Delta_{X,n}^Q
$$

不是直接從 raw $\mathcal E$ 中減出來。

它必須經過合法 realization / alignment。

---

# 32. 三種不同的 equality

本文至少區分：

### 32.1 Token equality

$$
e=e'.
$$

### 32.2 Algebraic equivalence

例如：

$$
e-e'\in N
$$

或：

$$
[e]=[e'].
$$

### 32.3 Observer-relative equivalence

$$
\boxed{
e\sim_Q e'.
}
$$

因此：

$$
F K(e)=e
$$

是最強的 exact equality 形式之一。

實證研究中更常得到：

$$
F K(e)\sim_Q e.
$$

後者只能叫 observational coherence。

---

# 33. Exact Coherence、Observational Coherence、Approximate Coherence

定義三層：

## EC — Exact

$$
\boxed{
F K(e)=e.
}
$$

## OC — Observational

$$
\boxed{
F K(e)\sim_Q e.
}
$$

## AC — Approximate

若有 metric：

$$
\boxed{
d_Q(FK(e),e)\le\epsilon.
}
$$

三者不得互換。

這是後續 fidelity 量化的基礎。

---

# 34. No-Go N2.3 — Formal Recursion 不等於 Epistemic Success

我們可以構造任意形式：

$$
e_0
\xrightarrow{K_0}
e_1
\xrightarrow{K_1}
e_2.
$$

這只證明 state transformation 存在。

若沒有：

- target coherence；
- correctness criterion；
- reliability；
- task relevance；
- observation contract；

就不能稱：

$$
\boxed{
e_2
\text{ 比 }e_1\text{ 更知道}.
}
$$

因此：

$$
\boxed{
\text{recursive syntax}
\not\Rightarrow
\text{recursive epistemic success}.
}
$$

---

# 35. No-Go N2.4 — Self-reference 不等於 Meta-Knowing

一個系統可以輸出：

> 「我知道我知道 $p$。」

這只是一個 self-referential string。

若其內部／行為 structure 無法區分：

$$
\text{correct lower-level knowing}
$$

與：

$$
\text{incorrect lower-level knowing},
$$

則該字串不足以證明有效 meta-knowing。

因此：

$$
\boxed{
\text{linguistic nesting}
\not\Rightarrow
\text{epistemic nesting}.
}
$$

---

# 36. No-Go N2.5 — $F K=id$ 不等於新增 meta-content

即使：

$$
F K=id,
$$

仍可以取：

$$
K=\iota,
$$

則：

$$
m(e)=0
$$

對所有 $e$。

所以：

$$
\boxed{
\text{perfect target coherence}
\not\Rightarrow
\text{nonzero recursive novelty}.
}
$$

這是本文非常重要的分離。

---

# 37. 人類 realization 只是特例

若 $X=H$ 為人類，可能有：

$$
\Psi_{H,n}^Q(e_n)
=
\text{confidence / report / choice / opt-out / calibration observable}.
$$

但本文不把 confidence 定義成 knowing 本身。

confidence 只是一種：

$$
\Psi^Q.
$$

因此即使人類實驗能測到高階 confidence，也只是對某一 realization 的支持。

---

# 38. AI realization 只是特例

若 $X=A$ 為人工系統，可以有：

$$
e_1
=
\text{base answer state},
$$

$$
e_2
=
\text{verifier assessment},
$$

$$
e_3
=
\text{verifier-of-verifier / self-evaluation state}.
$$

但：

$$
\boxed{
\text{verifier stack}
\not\Rightarrow
\text{human-like phenomenology}.
}
$$

本文只要求代數上可建立 target relation 與 observation contract。

---

# 39. 多 Agent realization

若 $X$ 本身是一個多 Agent existence：

$$
X
=
\{A_1,\ldots,A_m,R\},
$$

第 $n+1$ 階 epistemic state 可以由不同 agent 產生。

例如：

$$
A_1
\rightarrow
A_2\text{ verifies }A_1
\rightarrow
A_3\text{ verifies }A_2.
$$

因此：

$$
\boxed{
\text{recursion level}
\neq
\text{physical nesting inside one carrier}.
}
$$

這是 carrier-neutral framework 的核心之一。

---

# 40. 與 Displayed / Dependent Structures 的方法學對照

Ahrens 與 Lumsdaine 的 displayed categories 強調：額外資料或結構可以作為依附於 base objects 的 family，而不必先把所有東西壓成一個單一 homogeneous object。

本文不宣稱 RKD algebra 就是一個 displayed category。

但方法學上的共同點是：

$$
\boxed{
\text{higher-level structure may be typed over lower-level structure}.
}
$$

這支持本文拒絕：

$$
\mathcal E^{(n)}=\mathcal E^{(n+1)}
$$

作為預設。

---

# 41. 與 Higher-Order Belief Hierarchies 的方法學對照

higher-order belief / type-space 文獻已長期研究：

$$
\text{belief},
\text{ belief about belief},
\text{ belief about belief about belief},
\ldots
$$

Pintér 證明在特定 purely measurable type-space framework 中，每個完整 belief hierarchy 可由 complete universal type space 中的 type 表示。

本文不把：

$$
\text{belief}
=
\text{knowing}.
$$

也不把 type-space consistency 當成 RKD 的證明。

本文只吸收一個形式教訓：

$$
\boxed{
\text{higher-order epistemic structure requires explicit coherence across levels}.
}
$$

---

# 42. 與 Computational Metacognition 的方法學對照

Computational metacognition 工作把 cognitive traces 顯式表示，再由 meta-level monitor / control process 操作 cognition 本身。

這說明至少在人工系統中：

$$
\boxed{
\text{base-level cognitive state}
}
$$

與：

$$
\boxed{
\text{meta-level representation of that cognitive state}
}
$$

可以工程化地分離。

本文的 $K/F$ 結構比該工程架構更抽象，也不宣稱等價；它只把這種「base / meta 分層」推廣為 carrier-neutral algebra candidate。

---

# 43. 本文內部已建立的結果

目前可分為：

## Definitions

- graded epistemic spaces；
- recursive lift $K_{X,n}$ ；
- target projection $F_{X,n}$ ；
- exact / observational / approximate coherence；
- zero-meta embedding $\iota_{X,n}$ ；
- meta-residual；
- pure meta-space；
- fiber；
- quotient candidate；
- epistemic path；
- cross-existence tower morphism；
- observation realization。

## Conditional propositions

- P2.1: $F K=id$ implies injectivity of $K$ on the coherent domain；
- P2.2: $F K=id$ implies local surjectivity of $F$ onto that domain；
- P2.3: in a linear split setting, meta-residual lies in $\ker F$ ；
- P2.4: a linear short exact extension with section splits as lower-level image $\oplus$ meta-kernel。

## No-Go

- N2.1: representation difference does not imply effective meta-novelty；
- N2.2: nonzero kernel does not imply active metacognition；
- N2.3: formal recursion does not imply epistemic success；
- N2.4: linguistic self-reference does not imply epistemic nesting；
- N2.5: exact target coherence does not imply nonzero novelty。

---

# 44. 本文仍然沒有回答的問題

本文沒有回答：

$$
\boxed{
\mathcal E_X^{(\infty)}
\neq\varnothing?
}
$$

沒有回答：

$$
\boxed{
\text{finite coherent paths}
\Rightarrow
\text{infinite coherent tower}?
}
$$

沒有回答：

$$
\boxed{
\dim\mathcal M
\text{ 與有效知差如何對應？}
}
$$

沒有回答：

$$
\boxed{
\text{meta-residual 最小正值是多少？}
}
$$

沒有回答：

$$
\boxed{
\Delta_{n+1}
\le
\Delta_n?
}
$$

也沒有回答：

$$
\boxed{
\text{strong infinite recursive knower 是否可能？}
}
$$

這些依序交給 Paper 03–06。

---

# 45. 對 EML-RKD-01 的回填

第一篇提出：

$$
\mathbf D_{X,n}^Q(p)
$$

但沒有規定它如何合法產生。

本文現在提供其 upstream structural ingredients：

$$
\boxed{
\mathcal E_X^{(n)}
\xrightarrow{K_{X,n}}
\mathcal E_X^{(n+1)}
\xrightarrow{F_{X,n}}
\mathcal E_X^{(n)}.
}
$$

以及在 split additive case：

$$
\boxed{
K_{X,n}(e_n)
=
\iota_{X,n}(e_n)
+
m_{X,n+1}(e_n).
}
$$

因此後續的 recursive knowing difference 不再需要非法地直接寫：

$$
e_{n+1}-e_n.
$$

真正應該量的是：

$$
\boxed{
\text{target coherence}
+
\text{meta-residual structure}
+
\text{observer-relative effect}.
}
$$

---

# 46. 系列中的位置

目前系列進度：

$$
\boxed{
\text{Paper 01: Conjecture}
}
$$

$$
\boxed{
\Downarrow
}
$$

$$
\boxed{
\text{Paper 02: Graded Algebra}
}
$$

下一篇將進入：

$$
\boxed{
\text{Paper 03: Projective Infinite Epistemic Recursion}
}
$$

也就是研究：

$$
\cdots
\rightarrow
\mathcal E^{(3)}
\rightarrow
\mathcal E^{(2)}
\rightarrow
\mathcal E^{(1)}
\rightarrow
\mathcal E^{(0)}
$$

何時真的存在一條 coherent infinite tower。

---

# 47. 結論

EML-RKD-01 問：

> 「知道」與「知道自己知道」之間能不能合法定義差？

本文回答的是更前一層：

> 在談「差」之前，必須先把兩階知道建模成不同型別的 epistemic states，並建立它們之間的 lift、target projection 與合法 comparison structure。

因此本文的核心不是：

$$
\boxed{
K^{n+1}-K^n.
}
$$

而是：

$$
\boxed{
\mathcal E_X^{(n)}
\xrightarrow{K_{X,n}}
\mathcal E_X^{(n+1)}
\xrightarrow{F_{X,n}}
\mathcal E_X^{(n)}.
}
$$

在可加 split realization 中，真正的高階新增候選則是：

$$
\boxed{
m_{X,n+1}
=
K_{X,n}(e_n)
-
\iota_{X,n}(e_n)
\in
\ker F_{X,n}.
}
$$

而在一般非線性 realization 中，母物件應退回：

$$
\boxed{
F_{X,n}^{-1}(e_n)
}
$$

以及 fiber-relative meta-class。

本文因此建立了「遞歸知差」的第一個 type-safe 代數基礎，同時拒絕把：

$$
\text{高階狀態},
\quad
\text{自我指涉},
\quad
\text{meta-residual},
\quad
\text{真實 knowing},
\quad
\text{意識}
$$

提前壓成同一概念。

這個不塌縮原則，將成為後續整個系列的基礎。

---

# References

1. Ahrens, B., & Lumsdaine, P. L. (2019). *Displayed Categories*. Logical Methods in Computer Science. arXiv:1705.04296.
2. Cox, M. T., Mohammad, Z., Kondrakunta, S., Gogineni, V. R., Dannenhauer, D., & Larue, O. (2022). *Computational Metacognition*. arXiv:2201.12885.
3. Pintér, M. (2008). *Every hierarchy of beliefs is a type*. arXiv:0805.4007.
4. Ahrens, B., Lumsdaine, P. L., & Voevodsky, V. (2017). *Categorical structures for type theory in univalent foundations*. arXiv:1705.04310.

---

## Version note

v0.1 is the first algebraic extension of RKDC. All claims involving kernels, quotients, direct sums, exact sequences, and linear residuals are explicitly restricted to realizations where the required algebraic structure exists. Future papers may replace or generalize these structures by relational, categorical, topological, probabilistic, or other carrier-neutral forms without retroactively rewriting this historical version.
