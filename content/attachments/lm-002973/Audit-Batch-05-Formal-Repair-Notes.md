# Phase Canon Audit Batch 05 — Formal Repair Notes
## Biological Oscillators, Body-State Monitoring, Acupuncture Mechanisms, and Engineering Phase Coordination

**版本：** v1.0  
**日期：** 2026-08-14  
**安全邊界：** 本文件不提供臨床治療、針刺操作、磁場干預、神經調控或自行診斷建議。

---

# R1 — Biological Phase Evidence Ladder

生物學中的「phase」至少分成四層證據：

## Level B0 — Periodicity

觀察量：

$$
y(t)
$$

具有週期或準週期結構。

這只能支持：

$$
\boxed{
\text{rhythmic observable}.
}
$$

## Level B1 — Oscillator Phase

存在合法：

$$
\Theta:\mathcal Z\rightarrow S^1
$$

且 phase predictability / phase-response 可被估計。

## Level B2 — Coupled / Entrained Phase

外部輸入：

$$
u(t)
$$

改變 phase：

$$
\dot\theta
=
\omega
+
Z(\theta)u(t)
+
\cdots
$$

並可觀察 phase locking / entrainment。

## Level B3 — Functional / Clinical Relevance

phase change 對：

- behavior；
- physiology；
- disease outcome；
- treatment response；

有可重現 causal effect。

因此：

$$
\boxed{
B0\not\Rightarrow B1\not\Rightarrow B2\not\Rightarrow B3.
}
$$

---

# R2 — Endogenous Oscillator vs Zeitgeber

canonical circadian decomposition：

$$
\boxed{
\dot x
=
F_{\mathrm{clock}}(x)
+
G(x,u_{\mathrm{zeitgeber}})
}
$$

其中：

- $F_{\mathrm{clock}}$：endogenous molecular/cellular oscillator；
- $u_{\mathrm{zeitgeber}}$：light, feeding, activity, temperature or other external cues；
- $G$：entrainment/input coupling。

這避免兩個極端：

$$
\text{external cue alone creates rhythm}
$$

與：

$$
\text{external cue is irrelevant}.
$$

對任何 Earth-EM hypothesis，必須測：

$$
\boxed{
\Delta_{\mathrm{EM}}
=
\text{prediction/phase response with EM cue}
-
\text{baseline endogenous model}.
}
$$

---

# R3 — Electromagnetic Coupling Causality Test

「場存在」不等於「功能耦合」。

對外場：

$$
E_{\mathrm{ext}}(t),\quad B_{\mathrm{ext}}(t)
$$

與 biological state：

$$
z(t),
$$

至少需要：

1. coupling mechanism：
   $$
   \mathcal C(E,B,z);
   $$
2. sensitivity；
3. signal-to-noise；
4. dose/field-response；
5. phase-response curve；
6. sham / shielding / alternative-cue controls；
7. replication。

可以定義：

$$
\boxed{
\Gamma_{\mathrm{EM}}
=
\frac{
\text{causal response attributable to EM perturbation}
}{
\text{measurement noise + alternative-cue response}
}.
}
$$

只有：

$$
\Gamma_{\mathrm{EM}}
$$

顯著且可重現，才提升到 B2/B3。

---

# R4 — Frequency Coincidence Is Not Coupling

若兩個系統都有 dominant frequency：

$$
f_A\approx f_B,
$$

只能得到：

$$
\boxed{
\text{spectral proximity}.
}
$$

不能推出：

$$
\boxed{
A\leftrightarrow B
\text{ causal synchronization}.
}
$$

需要測：

- phase coherence beyond common drive；
- transfer / directed influence；
- intervention response；
- field magnitude and sensitivity。

因此：

$$
\boxed{
7.8\text{ Hz proximity}
\neq
\text{Schumann-to-brain entrainment evidence}.
}
$$

---

# R5 — Genetic Timing Memory Repair

區分：

## Genetic clock architecture

基因／分子網路決定：

- intrinsic period；
- phase-response properties；
- oscillator robustness；
- entrainment sensitivity。

## External absolute-phase memory

主張基因直接保存：

$$
\phi_{\mathrm{Earth}}
$$

或指定地球場絕對 phase。

後者需額外證據。

Canonical hypothesis：

$$
\boxed{
\text{genotype}
\rightarrow
(
\omega_0,
Z(\theta),
\lambda_{\mathrm{entrain}}
)
}
$$

比：

$$
\boxed{
\text{gene}
=
\text{absolute Earth-time memory}
}
$$

更可驗證。

---

# R6 — Disease-Specific Dynamical Repertoire

撤回：

$$
\boxed{
\text{health}
=
\text{maximum global coherence}.
}
$$

對 disease/task：

$$
D
$$

定義：

$$
\boxed{
\mathfrak R_{\mathrm{adm}}^{(D)}
}
$$

可包含：

- acceptable rhythms；
- amplitudes；
- coupling；
- inflammatory states；
- metabolic states；
- autonomic ranges；
- uncertainty。

因此：

$$
\boxed{
\text{synchrony}
\neq
\text{health}.
}
$$

健康可能需要：

- phase locking；
- phase flexibility；
- desynchronization；
- multistability；

依系統而定。

---

# R7 — Meridian / Eigenmode Discriminative Test

若主張：

$$
\boxed{
\text{meridian map}
=
\text{eigenmodes of }W_{\mathrm{body}},
}
$$

必須先定義：

$$
W_{\mathrm{body}}
$$

的：

- nodes；
- edges；
- weights；
- modality；
- time scale；
- measurement method。

計算 eigenvectors：

$$
Wv_k
=
\lambda_kv_k.
$$

然後在未參與 fit 的資料上測：

$$
\boxed{
\operatorname{SpatialMatch}
(
v_k,
M_{\mathrm{meridian}}
)
}
$$

並比較 competing predictors：

- sensory nerve anatomy；
- connective tissue；
- vasculature；
- random spatial controls；
- smoothness-matched nulls。

沒有 out-of-sample superiority：

$$
\boxed{
\text{eigenmode interpretation remains conjectural}.
}
$$

---

# R8 — Deqi / Neural-Phase Hypothesis Repair

主觀事件：

$$
q_{\mathrm{deqi}}
$$

不能直接定義成 phase lock。

可建立 event-related hypothesis：

$$
\boxed{
P(
\Delta C_{\mathrm{phase}}>0
\mid
q_{\mathrm{deqi}}
)
>
P(
\Delta C_{\mathrm{phase}}>0
\mid
\text{control}
).
}
$$

其中：

$$
C_{\mathrm{phase}}
$$

可為預先指定的 neural phase/coherence observable。

同時比較：

- amplitude；
- firing/rate proxy；
- autonomic signals；
- motion/artifact；
- expectation/context。

不預設固定 cutoff；

先估 effect size 與 uncertainty。

---

# R9 — Medical Threshold Rule

任何 clinical / physiological threshold：

$$
\theta^*
$$

若不是：

- independent training cohort；
- preregistered rule；
- validated reference；
- external replication；

所得，

不得稱 canonical threshold。

應報：

$$
\boxed{
\text{sensitivity},
\text{specificity},
\text{calibration},
\text{PPV/NPV},
\text{confidence intervals},
\text{domain}.
}
$$

---

# R10 — Body Latent-State Representation

人體追蹤 Agent 中：

$$
\phi_R
$$

若同時壓縮：

- metabolism；
- proliferation；
- inflammation；
- hypoxia；
- differentiation；

它不是 PH-0 physical phase。

改定義：

$$
\boxed{
z_R(t)
\in
\mathcal Z_R
}
$$

為 regional latent physiological state。

若某 component 真為 oscillatory：

$$
\theta_R(t)
=
\Theta_R(z_R(t)).
$$

因此：

$$
\boxed{
z_R
\neq
\theta_R.
}
$$

---

# R11 — Multiscale Anomaly Detection

區域圖：

$$
\mathcal G
=
(V,E).
$$

每個 region state：

$$
z_i(t).
$$

typed discrepancy：

$$
\boxed{
D_{ij}(t)
=
d(
z_i(t),
z_j(t)
).
}
$$

anomaly score：

$$
\boxed{
A_i(t)
=
f(
z_i,
\{D_{ij}\}_{j\in N(i)},
\dot z_i,
\text{history},
\text{uncertainty}
).
}
$$

coarse-to-fine：

$$
\boxed{
\text{global monitor}
\rightarrow
\text{flag region}
\rightarrow
\text{local high-resolution expansion}.
}
$$

benchmark：

- AUROC / AUPRC；
- false alarms；
- early-detection lead time；
- compute；
- calibration；
- domain shift。

---

# R12 — Clinical Boundary for Phase Agents

沒有 prospective clinical validation 前：

$$
\boxed{
\text{phase agent}
=
\text{research / visualization / anomaly exploration tool}.
}
$$

不得自動變成：

- diagnosis；
- treatment recommendation；
- medication change；
- acupuncture protocol；
- neurostimulation protocol。

任何升級需：

1. defined intended use；
2. reference standard；
3. prospective validation；
4. safety analysis；
5. regulatory / clinical governance。

---

# R13 — Power-Phase Taxonomy

工程供電中的 phase 至少分：

## PWR-0 — Switching phase

$$
\phi_k
=
\frac{2\pi k}{N}
$$

多相 converter 的週期時序。

## PWR-1 — Relative/interleaving phase

多通道 ripple cancellation / current sharing。

## PWR-2 — Resonant phase/frequency tracking

針對 LC / inductive power transfer 等 resonant system。

## PWR-3 — Scheduling phase

工作負載／power-state stage，不一定是 $S^1$。

## PWR-X — Quantum phase

只有在 coherent quantum state：

$$
|\psi\rangle
$$

的相位真正參與 power/control mechanism 時才使用。

因此：

$$
\boxed{
\text{multiphase VRM}
\neq
\text{quantum phase coordination}.
}
$$

---

# R14 — Canonical PDN Transient Model

負載端主要看：

$$
\boxed{
Z_{\mathrm{PDN}}(f)
=
\frac{V(f)}{I(f)}
}
$$

與：

$$
\boxed{
Z_{\mathrm{target}}
=
\frac{
\Delta V_{\mathrm{allow}}
}{
\Delta I_{\mathrm{step}}
}.
}
$$

簡化 transient droop：

$$
\boxed{
\Delta V(t)
\approx
\Delta I R
+
L\frac{dI}{dt}
+
\frac1C
\int_0^t
\Delta I(\tau)d\tau.
}
$$

這取代：

$$
\boxed{
\text{CPU waits for remote electricity propagation}.
}
$$

---

# R15 — Multiphase / Predictive Power Benchmark

DPCPS 類 architecture 應報：

$$
\boxed{
\mathbf M_{\mathrm{power}}
=
(
\Delta V_{\max},
\eta,
T_{\max},
Z_{\mathrm{PDN}},
t_{\mathrm{settle}},
R_{\mathrm{fault}},
P_{\mathrm{app}}
).
}
$$

比較：

- fixed-phase baseline；
- conventional phase shedding；
- predictive phase management；
- near-load distribution。

任何 app-level performance gain：

$$
\Delta P_{\mathrm{app}}
$$

只能在 power/thermal constraint actually active 時解讀。

---

# R16 — Quantum-Phase Claim Gate

工程文件若出現：

- quantum interference；
- coherent phase；
- wavefunction reinforcement；
- quantum phase locking；

必須回答：

1. quantum state 是什麼？
2. coherence time？
3. Hamiltonian / channel？
4. phase observable？
5. measurement？
6. classical alternative 是否已排除？

若無：

$$
\boxed{
\text{use classical timing / resonant phase terminology}.
}
$$

---

# R17 — Batch 05 Canonical Rule

本批最高規則：

$$
\boxed{
\text{Biological phase}
\neq
\text{medical efficacy}
\neq
\text{universal body phase field}.
}
$$

以及：

$$
\boxed{
\text{Engineering phase}
\neq
\text{quantum phase}.
}
$$

真正允許跨層提升的唯一方式仍是：

$$
\boxed{
\text{No type jump without a map.}
}
$$
