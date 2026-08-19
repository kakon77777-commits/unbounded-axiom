# Phase Canon Audit Batch 03 — Formal Repair Notes
## Generalized Phase, Relational Time, Semantic Matching, and Receiver-Dependent Reconstruction

**版本：** v1.0  
**日期：** 2026-08-14  

---

# R1 — Generalized Phase Admission Test (GPAT)

對任何聲稱為 generalized phase 的模型，先定義：

$$
\boxed{
\mathfrak P
=
(
\mathcal X,
\Phi,
\varphi,
\Delta,
U,
\mathcal K,
H
).
}
$$

其中：

- $\mathcal X$：原始 state space；
- $\Phi$：phase / relation representation space；
- $\varphi:\mathcal X\to\Phi$：表示映射；
- $\Delta:\Phi\times\Phi\to\mathcal D$：typed difference；
- $U$：state / phase evolution；
- $\mathcal K$：coupling / interaction structure；
- $H$：task observable / readout。

一個 PH-5 generalized phase 至少應滿足：

1. **Relation**：不是單一裸值，而是在指定 relation space 中定位；
2. **Difference**：存在非平凡 $\Delta$；
3. **Evolution / Path**：phase state 或 relation 可演化，或其 history 對未來有影響；
4. **Structural Effect**：改變 coupling、routing、selection、update 或 prediction；
5. **Observable Relevance**：移除 phase 後，指定 task 的 prediction / explanation / control 能力下降；
6. **Type Honesty**：若沒有 physical realization map，不得升格成 PH-0。

這不是要求每個 PH-5 都是圓相位。

它只要求：

$$
\boxed{
\text{phase}
>
\text{renamed scalar/state label}.
}
$$

---

# R2 — Renaming-Invariance Proposition

## 命題 R2.1

若 representation：

$$
\varphi
=
r\circ s
$$

只是 ordinary state representation $s$ 的雙射重新命名，而且沒有引入新的：

- difference structure；
- coupling law；
- path dependence；
- invariant；
- task readout；

則把：

$$
s
$$

改叫：

$$
\phi
$$

不改變任何 model prediction 或 computational structure。

因此：

$$
\boxed{
\text{renaming a state as phase does not create phase mechanics}.
}
$$

這是 Batch 03 最重要的反濫用規則。

---

# R3 — Typed Product Phase Space

G3 不應把所有 cognitive variables 強塞進：

$$
(S^1)^N.
$$

改定義：

$$
\boxed{
\Phi
=
\prod_{k=1}^{m}
\Phi_k,
}
$$

其中每個 factor 可以不同：

$$
\Phi_k
\in
\{
S^1,
\mathbb R,
[0,1],
\Delta^n,
\mathcal G,
\mathcal M,
\ldots
\}.
$$

每一型都有自己的 metric / divergence：

$$
d_k:
\Phi_k\times\Phi_k
\rightarrow
\mathbb R_+.
$$

generalized phase difference：

$$
\boxed{
\Delta_\Phi(x,y)
=
\left(
d_1(\varphi_1(x),\varphi_1(y)),
\ldots,
d_m(\varphi_m(x),\varphi_m(y))
\right).
}
$$

若某一維真的具有 circular periodicity，再令：

$$
\Phi_k=S^1.
$$

此處的核心是：

$$
\boxed{
\text{typed relation}
\neq
\text{forced circularization}.
}
$$

---

# R4 — Quantum-Like Modeling Boundary

Hilbert-space、density-matrix、interference、Lindblad 等數學可以用於 cognition，前提是明確標為：

$$
\boxed{
\text{quantum-like mathematical model}
}
$$

而不是：

$$
\boxed{
\text{literal microscopic quantum cognition}.
}
$$

## Density-Matrix Phase Warning

若：

$$
\rho
=
|\psi\rangle\langle\psi|,
$$

global phase：

$$
|\psi\rangle
\rightarrow
e^{i\alpha}
|\psi\rangle
$$

完全消失：

$$
\rho
\rightarrow
\rho.
$$

所以：

$$
\boxed{
\arg(\rho)
}
$$

一般不是 canonical global phase observable。

若使用 density matrices 比較 cognitive states，更自然的候選包括：

- fidelity；
- Bures angle；
- trace distance；
- relative entropy；
- task-specific operator expectation。

如果真正需要 PH-0-like phase，應在被證明具有 circular structure 的 latent factor 上直接定義。

---

# R5 — Comparison-Base Principle

PDTM 中最值得升格的直覺之一，是：

> A 與 B 的比較，必須先聲明在哪個共同底空間上比較。

Canon 定義：

$$
\boxed{
p_A:
\mathcal X_A
\rightarrow
\mathcal B,
\qquad
p_B:
\mathcal X_B
\rightarrow
\mathcal B.
}
$$

只比較：

$$
p_A(A),
\qquad
p_B(B).
$$

若真的存在 category diagram：

$$
\begin{array}{ccc}
P & \to & \mathcal X_B\\
\downarrow & & \downarrow p_B\\
\mathcal X_A & \xrightarrow{p_A} & \mathcal B
\end{array}
$$

並滿足 universal property，才稱：

$$
P
=
\mathcal X_A
\times_{\mathcal B}
\mathcal X_B
$$

為 fiber product / pullback。

否則應使用：

$$
\boxed{
\text{shared comparison base / common projection space}.
}
$$

---

# R6 — Adaptive Operator Calibration

PDTM 的「算子升級」可合法重寫成 online meta-calibration。

令 operator parameters：

$$
\vartheta_n
$$

與 task loss：

$$
L(\vartheta_n;\mathcal D_n).
$$

更新：

$$
\boxed{
\vartheta_{n+1}
=
\vartheta_n
-
\eta_n
\nabla_\vartheta
L(\vartheta_n;\mathcal D_n).
}
$$

或任意明確 optimizer：

$$
\vartheta_{n+1}
=
\mathcal U(\vartheta_n,\mathcal D_n).
$$

要宣稱 convergence，需說明：

- parameter space；
- loss regularity；
- step-size；
- convexity / contraction / stochastic assumptions；
- held-out evaluation。

超限序數版本在有限/omega-limit模型完成前，不進 operational Canon。

---

# R7 — Internal / Relational Time Repair

區分：

1. physical coordinate / proper time；
2. external experimental clock；
3. internal phase clock；
4. event / causal progress variable；
5. subjective duration estimate。

對系統：

$$
\dot x
=
F(x),
$$

可以定義 internal progress functional：

$$
\boxed{
\tau(t)
=
\int_0^t
\omega(x_s)\,ds
}
$$

或：

$$
\tau
=
Q(x_{[0,t]}).
$$

如果：

$$
\frac{d\tau}{dt}<0,
$$

只表示該 internal order parameter / progress coordinate 回退。

不能直接推出：

$$
\boxed{
\text{physical spacetime time reversal}.
}
$$

---

# R8 — Reflexive Prediction Dynamics

G3「預言會改變未來」可用普通 feedback dynamics 形式化：

$$
\boxed{
\hat y_t
=
P(x_t),
}
$$

$$
\boxed{
a_t
=
\pi(
\hat y_t,
x_t
),
}
$$

$$
\boxed{
x_{t+1}
=
F(x_t,a_t,\xi_t).
}
$$

forecast：

$$
\hat y_t
$$

經 agent policy：

$$
\pi
$$

改變 action，

action 再改變 future state。

因此：

$$
\boxed{
\text{prediction can be performative/reflexive}
}
$$

完全不需要：

- quantum time collapse；
- higher-world observers；
- retrocausality。

可研究：

- self-fulfilling prediction；
- self-defeating prediction；
- Goodhart-like response；
- adversarial adaptation；
- policy-induced distribution shift。

---

# R9 — Cross-Temporal Information Delivery

將 ITT 從「time travel」重寫為 asynchronous persistence：

$$
\boxed{
m_{t_0}
\xrightarrow{\mathrm{store}}
M
\xrightarrow{\mathrm{replicate/maintain}}
M_{t_1}
\xrightarrow{\mathrm{retrieve}(q,c)}
m
\xrightarrow{D_B}
\hat S_B.
}
$$

其中：

- $M$：persistent storage / corpus；
- $q$：future query；
- $c$：future context；
- $D_B$：receiver-dependent decoder。

這是一個完全可實驗的 architecture：

$$
\boxed{
\text{durability}
+
\text{discoverability}
+
\text{context match}
+
\text{reconstruction}.
}
$$

它不是物理時間旅行。

---

# R10 — Semantic Matching and Receiver Decode

message representation：

$$
z
=
E_A(S_A).
$$

receiver context：

$$
c_B
=
(
B_B,
H_{AB},
C,
T
).
$$

定義 task-relative match：

$$
\boxed{
M_T(z,c_B)
\in
[0,1]
}
$$

或 typed vector：

$$
\mathbf M_T(z,c_B).
$$

但理解結果仍是：

$$
\boxed{
\hat S_B
=
D_B(z,c_B).
}
$$

所以：

$$
\boxed{
M_T\text{ high}
\not\Rightarrow
\hat S_B=S_A.
}
$$

需要 calibration：

$$
P(
\text{task success}
\mid
M_T
).
$$

---

# R11 — Diachronic Semantic Resonance

歷史文本：

$$
m
$$

在不同時代：

$$
t_1,t_2
$$

由不同 context：

$$
c_{t_1},
c_{t_2}
$$

解碼：

$$
\boxed{
y_t
=
D(
m,c_t
).
}
$$

context alignment 可以定義：

$$
\boxed{
R(t_1,t_2)
=
\operatorname{sim}
(
c_{t_1},
c_{t_2}
).
}
$$

若：

$$
R
$$

可以提升：

- interpretation similarity；
- lexical shift prediction；
- retrieval relevance；
- reader response prediction；

則「歷史共鳴」獲得可驗證 effective meaning。

不需要 Born rule：

$$
|\langle\phi_{t_1}|\phi_{t_2}\rangle|^2
$$

除非使用明確 Hilbert statistical model 並實證比較優勢。

---

# R12 — Concept Address Repair

concept address 不等於 concept。

Canonical structure：

$$
\boxed{
a
\mapsto
(
G_v,
\sigma_v,
P_v,
U_v
).
}
$$

其中：

- $a$：stable identifier；
- $G_v$：versioned structured representation / knowledge graph；
- $\sigma_v$：schema / type；
- $P_v$：provenance；
- $U_v$：uncertainty / open-boundary metadata。

receiver：

$$
\boxed{
\hat S_B
=
D_B(
a,
G_v,
B_B,
C
).
}
$$

因此 concept-address 的真正工程價值是：

- stable identity；
- explicit versioning；
- no silent semantic drift；
- cross-system mappings；
- provenance；
- open relations。

不是：

$$
\boxed{
\text{address = complete concept itself}.
}
$$

---

# R13 — Task-Relative Semantic Distortion

撤回：

$$
\boxed{
\text{language always loses infinite information}.
}
$$

改定義 sender target state：

$$
S_A
$$

與 receiver reconstruction：

$$
\hat S_B.
$$

對 task：

$$
T
$$

定義：

$$
\boxed{
D_T(
S_A,
\hat S_B
).
}
$$

$D_T$ 可以是：

- task loss；
- semantic similarity error；
- decision discrepancy；
- factual omission；
- reconstruction graph distance；
- human comprehension score。

於是：

$$
\boxed{
\text{communication quality is task- and receiver-relative}.
}
$$

---

# R14 — G3 → GPC Canonical Migration

G3 的「相位交流」現行 canonical successor：

$$
\boxed{
x'_B
=
F_B
\left(
x_B,
D_B
\left(
T_{A\to B}
(
E_A(x_A)
),
x_B
\right)
\right).
}
$$

這個版本保留了 G3 最重要的直覺：

- sender state；
- receiver state；
- relation；
- transmission；
- reconstruction；
- history；
- carrier update。

同時撤回：

- direct concept identity；
- zero-loss address transfer；
- quantum semantic collapse；
- universal phase ontology。

因此：

$$
\boxed{
\text{G3 generalized phase}
\rightarrow
\text{PH-5 carrier relation}
\rightarrow
\text{GPC-CS}.
}
$$

---

# R15 — Generalized Phase Necessity Test

對 phase-augmented model：

$$
M_\phi
$$

與 phase-free baseline：

$$
M_0,
$$

定義 task score：

$$
S(M).
$$

phase 只有在：

$$
\boxed{
S(M_\phi)
-
S(M_0)
>
\delta_{\min}
}
$$

且 improvement 在：

- held-out data；
- alternative baselines；
- ablation；
- uncertainty intervals；

下穩定時，才獲得「功能必要性」證據。

這是 G3 從 metaphor 走向 science 的最重要 benchmark。

