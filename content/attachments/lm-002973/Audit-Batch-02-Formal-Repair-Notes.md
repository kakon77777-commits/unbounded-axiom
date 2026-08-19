# Phase Canon Audit Batch 02 — Formal Repair Notes

**版本：** v1.0  
**日期：** 2026-08-14

---

# R1 — Correct Circular Phase Pseudometric

令 phase map：

$$
\Theta:\mathcal P\rightarrow S^1.
$$

圓周測地距離：

$$
\boxed{
d_{S^1}(\theta,\phi)
=
\min_{k\in\mathbb Z}
|\theta-\phi+2\pi k|.
}
$$

拉回粒子集：

$$
\boxed{
d_\Theta(p_i,p_j)
=
d_{S^1}(\Theta(p_i),\Theta(p_j)).
}
$$

則 $d_\Theta$ 是 pseudometric。不同粒子可以因同 phase 而距離為零，但三角不等式仍成立。原先「mod 0.5 且三角不等式一般不成立」的量只能稱 dissimilarity。

---

# R2 — Time-Varying PCH

固定 physical time $t$：

$$
\epsilon\mapsto\operatorname{VR}(\epsilon;t)
$$

是普通一參數 filtration。

若時間演化讓 simplices 可加入也可移除，使用：

$$
K_0\leftrightarrow K_1\leftrightarrow K_2\leftrightarrow\cdots
$$

的 zigzag persistence，或逐時刻 persistence diagram 的 vineyard / trajectory。只有對 $(\epsilon,t)$ 真正具有偏序單調 inclusion 時，才稱 multiparameter filtration。

---

# R3 — PCH Signature Rule

$$
\mathcal T_{\mathrm{PCH}}(X)
=
Dgm\left(\operatorname{VR}(X,d_\Theta)\right)
$$

可作 phase-coherence topological descriptor，但不是一般 underlying state 或 homotopy type 的 complete fingerprint。

---

# R4 — Phase-Edge Renaming Rule

沒有明確 phase coordinate / velocity / potential 時：

- phase-edge attractor → boundary-regime / edge-attractor hypothesis；
- phase escape velocity → transition barrier / switching threshold / migration margin；
- phase memory → hysteresis / path dependence。

---

# R5 — Correct Winding Structure on $T^\infty$

令：

$$
T^\infty=\prod_{i=1}^\infty S^1.
$$

閉路：

$$
\gamma:S^1\rightarrow T^\infty
$$

逐座標得到：

$$
\gamma_i:S^1\rightarrow S^1,
\qquad
n_i=\deg(\gamma_i)\in\mathbb Z.
$$

自然拓樸資料是：

$$
\boxed{
\mathbf n(\gamma)=(n_1,n_2,\ldots).
}
$$

一般 real weights $h_i$ 的 $\sum_i h_i n_i$ 不必為整數，所以不能自動稱 integer topological charge。

---

# R6 — Weighted Infinite Energy Absolute-Convergence Theorem

## 定理 R6.1

若：

$$
h_i\ge0,
\qquad
\sum_i h_i=1,
$$

且：

$$
|\epsilon_i|\le E_0,
\qquad
|K_{ij}V_{ij}|\le M,
$$

則：

$$
E=
\sum_i h_i\epsilon_i
+
\sum_{i<j}h_i h_j K_{ij}V_{ij}
$$

絕對收斂，並有：

$$
\boxed{
\sum_i h_i|\epsilon_i|
\le E_0
}
$$

與：

$$
\boxed{
\sum_{i<j}
h_i h_j|K_{ij}V_{ij}|
\le
\frac M2
\left(
1-\sum_i h_i^2
\right)
\le
\frac M2.
}
$$

證明使用：

$$
\sum_{i<j}h_i h_j
=
\frac12
\left[
\left(\sum_i h_i\right)^2-\sum_i h_i^2
\right].
$$

因此原文 exponential coupling decay 是可用的更強 locality assumption，但對這個基本 boundedness theorem 並非必要。

---

# R7 — Lagrangian to Kuramoto: Correct Route

若：

$$
L=
\sum_i h_i\frac12\dot\theta_i^2
-
V(\boldsymbol\theta),
$$

Euler–Lagrange 給：

$$
\boxed{
h_i\ddot\theta_i
=
-\frac{\partial V}{\partial\theta_i}.
}
$$

這是二階 inertial phase dynamics。

加入 damping：

$$
m_i\ddot\theta_i+\gamma_i\dot\theta_i
=
F_i(\boldsymbol\theta).
$$

在 overdamped regime 中忽略慣性後，才可得到一階 Kuramoto-like phase equation。

---

# R8 — Canonical Topology-to-Phase Bridge

任意 topology 並不存在自然唯一「拓樸空間 ↔ phase field」同構。

成熟的嚴格橋是：

$$
\boxed{
\text{data}
\rightarrow
H^1_{\mathrm{persistent}}
\rightarrow
[\alpha]
\rightarrow
f_\alpha:X\rightarrow S^1.
}
$$

也就是利用 persistent cohomology 找出顯著一維 cohomology class，再構造 circle-valued coordinate。

---

# R9 — Betti Numbers vs Phase Defects

$$
\beta_k(X)=\operatorname{rank}H_k(X)
$$

是 homology rank。

phase vortex / winding 來自：

$$
f:X\setminus D\rightarrow S^1
$$

的 degree / homotopy / defect structure。

所以：

$$
\boxed{
\beta_1(X)\neq \#\text{vortices}
}
$$

一般不成立。特殊 physical phase fields 中可以有額外定理把兩者聯繫，但必須逐模型證明。

---

# R10 — Complexity Accounting Rule

任何 phase/topology algorithm 應拆成：

$$
\boxed{
T_{\mathrm{total}}
=
T_{\mathrm{encode}}
+
T_{\mathrm{preprocess}}
+
T_{\mathrm{query}}
+
T_{\mathrm{verify}}
+
T_{\mathrm{update}}.
}
$$

hash lookup 可以 expected $O(1)$，但不能把隱藏在 `detect_topological_features` 中的 topology computation 算成 $O(1)$。

---

# R11 — Persistence Completeness Rule

一參數 persistence barcode 在適當 interval-decomposable setting 中描述 persistence module 的區間分解；它不是 underlying topological space 的 complete homotopy invariant。

Canonical wording：

$$
\boxed{
\text{persistent homology is stable, informative, and generally incomplete}.
}
$$

---

# R12 — Continuous-State Computability Rule

state space 不可數，不代表 machine 能精確存取任意不可數 state。

若宣稱 analog / topological hypercomputation，必須先指定：

- finite representation；
- precision model；
- BSS / real-RAM / oracle / computable-analysis assumptions。

---

# R13 — Turing Embedding Rule

將 Turing-machine state set 賦離散拓撲，可讓 transition map continuous，因此：

$$
\boxed{
\text{TM can be embedded in a topological dynamical representation}.
}
$$

但：

$$
\boxed{
\text{embedding}\not\Rightarrow\text{strict computational superiority}.
}
$$
