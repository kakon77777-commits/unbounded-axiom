# Metastability、Bifurcation 與安全動力學體制
## 從吸引子景觀、Basin Crossing 與 Critical Slowing 到允許動力學 Repertoire

**英文題名：** Metastability, Bifurcation, and Safe Dynamical Regimes: From Attractor Landscapes and Basin Crossing to Critical Slowing and Admissible Dynamical Repertoires  
**系列：** 相位載體物理實現論（Phase-Carrier Physical Realization Theory, PCPRT）  
**Paper：** 05  
**作者：** Neo.K（許筌崴）  
**機構：** EveMissLab／一言諾科技有限公司  
**理論協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v1.0  
**日期：** 2026-08-14  
**狀態：** Public Theoretical Paper / Dynamical-Regime Safety Foundation

---

## 摘要

PCPRT Papers 01–04 已將廣義相位交流重新接回物理層：Paper 01 將 GPC-CS 定位為 coarse-grained effective theory；Paper 02 建立 physical phase、phase-amplitude state 與 carrier deformation；Paper 03 將跨載體 interaction 拆分成 energy、heat、particle、charge、information flow 與 entropy production；Paper 04 則建立可塑性載體：

$$
q
=
(
z,\lambda,\mu
),
$$

其中 interaction 不只改變 fast state，也可改變 coupling parameters 與 plasticity-rule state。

本文進一步處理：

> 當 carrier parameters、coupling、noise 或 external conditions 改變時，整個 dynamical landscape 如何改變？「安全」應該如何在 multistable、metastable、switching 與 bifurcating systems 中定義？

本文的核心立場是：

$$
\boxed{
\text{safe}
\neq
\text{staying near one fixed point}.
}
$$

對 biological、neural、adaptive 與 driven-dissipative carriers，更合理的安全概念是：

$$
\boxed{
\text{remaining inside an admissible dynamical repertoire}.
}
$$

本文首先區分四種常被混稱為「狀態切換」的現象：

1. **Phase slip**：在相同 underlying dynamical regime 中，relative phase 經 $2\pi$ 類跳變或失鎖；
2. **Basin crossing**：vector field / parameters 固定，但 perturbation 或 noise 將 trajectory 推過 basin boundary；
3. **Bifurcation**：parameter variation 改變 invariant sets、stability 或其拓撲／質性結構；
4. **Metastable switching**：trajectory 在多個長壽但非永久 dynamical patterns 間停留與切換，未必要求多個真正 asymptotically stable attractors。

這四者具有不同的物理與安全意義，不能只用「state transition」概括。

對固定參數：

$$
\lambda,
$$

考慮：

$$
\dot z
=
F
(
z;\lambda
).
$$

令：

$$
\mathcal A_\alpha(\lambda)
$$

為 attractor / invariant dynamical set，令：

$$
\mathcal B_\alpha(\lambda)
$$

為其 basin of attraction。本文定義 **basin margin**：

$$
\boxed{
m_{\mathrm{basin}}
(
z;\mathcal A_\alpha,\lambda
)
=
\operatorname{dist}
\left(
z,
\partial
\mathcal B_\alpha(\lambda)
\right).
}
$$

並證明：若 instantaneous perturbation $\delta z$ 在相同 metric 下滿足：

$$
\boxed{
\|\delta z\|
<
m_{\mathrm{basin}},
}
$$

則 perturbation 後 state 仍留在同一 basin。因此「當前 activity 正常」與「離 regime boundary 很遠」是不同量；前者是狀態判定，後者是 resilience margin。

本文接著定義 parameter-space bifurcation margin。令：

$$
\mathcal D_{\mathrm{adm}}
\subseteq
\Lambda
$$

為目前 dynamical regime 維持其 qualitative structure 的 parameter domain，則：

$$
\boxed{
m_{\mathrm{bif}}(\lambda)
=
\operatorname{dist}
\left(
\lambda,
\partial
\mathcal D_{\mathrm{adm}}
\right).
}
$$

即使：

$$
z
$$

當前仍深處某 attractor basin，只要：

$$
m_{\mathrm{bif}}
$$

很小，慢變 plasticity / control parameter 仍可能把整個 attractor landscape 推到 qualitative transition。

本文第三個核心量是 **relaxation margin**。對 stable equilibrium：

$$
z^\star(\lambda),
$$

線性化：

$$
\dot\xi
=
J(\lambda)\xi,
$$

若 dominant stable eigenvalue：

$$
\alpha(\lambda)
=
\max_k
\operatorname{Re}
\lambda_k
<
0,
$$

則局部最慢 relaxation time 量級為：

$$
\boxed{
\tau_{\mathrm{rel}}
\sim
\frac{1}{
|\alpha(\lambda)|
}.
}
$$

本文證明：若在某 smooth parameter path 上：

$$
\alpha(\lambda)
\rightarrow
0^-
$$

而其他假設維持正則，則：

$$
\boxed{
\tau_{\mathrm{rel}}
\rightarrow
\infty.
}
$$

這就是 continuous-time local linear sense 下的 **critical slowing down**。本文明確限制：autocorrelation、variance、skewness 等 early-warning proxies 是否可靠，還需要 noise model、sampling、bifurcation type 與 stationarity assumptions；critical slowing 並不是所有 regime transition 的 universal warning signal。

2010 年 Drake–Griffen 對 Daphnia populations 的控制實驗，提供 critical slowing 在 transcritical-bifurcation extinction transition 中的實證支持。2024 年 hippocampal seizure 研究則以 model、自由移動 mice 與 human iEEG experiment 驗證了神經系統中 excitability、resilience loss、slower recovery 與 fold-bifurcation-like critical transition 的一組特定 dynamical predictions。本文只將它們視為「在特定 system classes 中可被量測的 resilience transition」，而不是把 seizure dynamics 當作所有認知系統的普遍模型。

本文第四個重點是 **metastability 不等於 multistability**。若系統具有多個 stable attractors：

$$
\mathcal A_1,\ldots,\mathcal A_m,
$$

並靠 noise / perturbation 跨 basin，屬於 multistable switching。若 system 自身存在 long-lived transient patterns、heteroclinic-like passages、winnerless competition 或 deterministic slow visits，而不需要多個永久 stable attractors，也可以出現 metastability。Roberts 等人的 whole-brain model 即展示無外部 noise 下多種 wave patterns 依序被訪問，transition 對應 phase-flow reconfiguration 與 nonlinear instabilities。

因此本文用 dwell-time structure 定義 metastable macrostate family：

$$
\boxed{
\mathfrak M
=
\{
M_1,\ldots,M_r
\},
}
$$

每個 $M_i$ 對應一個 coarse dynamical pattern，而不是必然對應 asymptotically stable attractor。若：

$$
\tau_{\mathrm{dwell}}(M_i)
\gg
\tau_{\mathrm{trans}},
$$

則 coarse observer 會看見長時間 dwell + 快速 transition 的 metastable repertoire。

本文第五個核心概念是 **允許動力學 repertoire**。不再只定義 state safe set：

$$
\mathcal S
\subseteq
\mathcal Z,
$$

而定義：

$$
\boxed{
\mathfrak R_{\mathrm{adm}}
=
(
\mathfrak A_{\mathrm{adm}},
\mathfrak M_{\mathrm{adm}},
E_{\mathrm{adm}},
\Lambda_{\mathrm{adm}}
).
}
$$

其中：

- $\mathfrak A_{\mathrm{adm}}$：允許 attractors / invariant sets；
- $\mathfrak M_{\mathrm{adm}}$：允許 metastable macrostates；
- $E_{\mathrm{adm}}$：允許 transition edges；
- $\Lambda_{\mathrm{adm}}$：允許 parameter region。

真正 dynamical safety 要求 trajectory 不只位於某些安全 states，而要：

1. dwell 於允許 regime；
2. transition 只沿允許 edges；
3. parameter drift 不離開允許 regime family；
4. recovery / perturbation response 仍具有足夠 resilience margin。

本文因此定義 **dynamical reserve vector**：

$$
\boxed{
\mathbf m_{\mathrm{dyn}}
=
(
m_{\mathrm{basin}},
m_{\mathrm{bif}},
r_{\mathrm{rec}},
\Delta U_{\mathrm{eff}},
\ldots
),
}
$$

其中：

$$
r_{\mathrm{rec}}
=
\frac1{
\tau_{\mathrm{rel}}
}
$$

可作局部 recovery-rate proxy，而：

$$
\Delta U_{\mathrm{eff}}
$$

只在具有合法 landscape / quasipotential description 的 stochastic systems 中使用。本文不將所有 nonequilibrium systems 強行寫成 scalar potential。

Kramers 1940 的 barrier-crossing theory 提供一個典型但受限的 stochastic metastability model：對受熱噪聲驅動的 metastable well，escape rate 在相應 regime 下呈指數依賴於 barrier height / noise scale。本文只採用其結構啟示：

$$
\boxed{
\text{same attractor label}
\text{ can have very different escape resilience}.
}
$$

並明確指出 driven-dissipative nonequilibrium systems 常需要 landscape + probability/current-flow structure，而不能只靠 potential well 一個 scalar 解釋。2024 年 driven-dissipative nonlinear-system experiment 也已直接量測 energy landscape 與 flow dynamics。

最後，本文把 Paper 04 的 plasticity 接回 bifurcation：

$$
\boxed{
\dot\lambda
=
\varepsilon G(q,u)
}
$$

意味著 carrier 不只在某固定 landscape 上移動，而是：

$$
\boxed{
\text{state evolves on a landscape that itself moves}.
}
$$

因此完整 adaptive carrier 最小模型應寫成：

$$
\boxed{
\dot z
=
F(z;\lambda),
}
$$

$$
\boxed{
\dot\lambda
=
\varepsilon G(z,\lambda,u),
}
$$

並把：

$$
\mathcal A_\alpha(\lambda),
\quad
\mathcal B_\alpha(\lambda),
\quad
m_{\mathrm{basin}},
\quad
m_{\mathrm{bif}}
$$

都視為 time-dependent quantities。

本文不提供任何誘發 seizure、推動 carrier 越過 bifurcation、尋找最低刺激閾值、操控 basin crossing 或優化 regime-transition 方法。所有 seizure、critical-transition 與 oscillator experiments 僅作為 physical dynamical-system examples。

**關鍵詞：** metastability、multistability、bifurcation、basin crossing、critical slowing down、resilience、attractor landscape、dynamical repertoire、phase slip、neural dynamics

---

# 0. 文獻定位

Metastability、multistability、bifurcation 與 critical transitions 是 dynamical-systems / statistical-physics 的成熟概念。

本文不重新發明：

- attractor；
- basin of attraction；
- bifurcation；
- Kramers escape；
- critical slowing down；
- metastability。

PCPRT 的工作是將它們重新組織成 **plastic physical carrier 的 safety language**。

2019 年 Roberts 等人在 human-connectome whole-brain model 中得到多種 metastable wave patterns，其 transition 對應 phase-flow reconfiguration；2024 年 Ocampo-Espindola 等則以 theory + electrochemical oscillator experiments 顯示 strong coupling 下 phase-locked solutions 間可出現不同 criticality 的 synchronization transitions，而且 phase-only reduction 可能漏掉 amplitude-mediated bifurcation structure。

因此：

$$
\boxed{
\text{regime safety}
}
$$

已經可以被接到真實物理與神經 dynamics，

不再只是 GPC 的抽象比喻。

---

# 1. Dynamical Carrier

考慮：

$$
\boxed{
\dot z
=
F
(
z;\lambda
),
}
$$

其中：

- $z\in\mathcal Z$：fast dynamical state；
- $\lambda\in\Lambda$：parameter / coupling / plasticity state。

固定：

$$
\lambda,
$$

得到一個 autonomous dynamical system。

---

# 2. Invariant Set

集合：

$$
\mathcal A
\subseteq
\mathcal Z
$$

若：

$$
\Phi_t(\mathcal A)
=
\mathcal A
$$

對所有適用時間成立，稱為 invariant set。

attractor 還需要：

- invariant；
- attracting；
- 具有某個 attraction neighborhood / basin。

---

# 3. Basin of Attraction

對 attractor：

$$
\mathcal A_\alpha,
$$

定義：

$$
\boxed{
\mathcal B_\alpha
=
\left\{
z:
\operatorname{dist}
(
\Phi_t(z),
\mathcal A_\alpha
)
\rightarrow
0
\right\}.
}
$$

basin boundary：

$$
\boxed{
\partial\mathcal B_\alpha.
}
$$

---

# 4. Multistability

如果固定同一：

$$
F(\cdot;\lambda)
$$

同時存在多個 attractors：

$$
\mathcal A_1,
\ldots,
\mathcal A_m,
$$

且：

$$
\mathcal B_i
$$

非空，

則稱 multistability。

此時：

$$
\boxed{
\text{same parameters}
+
\text{different initial conditions}
\rightarrow
\text{different asymptotic regimes}.
}
$$

---

# 5. Basin Crossing

如果：

$$
z
\in
\mathcal B_1,
$$

受到 perturbation：

$$
z^+
=
z+\delta z
$$

後：

$$
z^+
\in
\mathcal B_2,
$$

則發生 basin crossing。

重要的是：

$$
\boxed{
\lambda
\text{ 不需要改變}.
}
$$

vector field 本身可以完全相同。

---

# 6. Basin Margin

定義：

$$
\boxed{
m_{\mathrm{basin}}
(
z;\mathcal A_\alpha,\lambda
)
=
\operatorname{dist}
\left(
z,
\partial
\mathcal B_\alpha(\lambda)
\right).
}
$$

這是當前 state 到 regime boundary 的最短 metric distance。

---

# 7. Basin-Margin Safety Theorem

## 定理 7.1

若：

$$
z
\in
\operatorname{Int}
\mathcal B_\alpha,
$$

且 perturbation：

$$
\delta z
$$

滿足：

$$
\boxed{
\|\delta z\|
<
m_{\mathrm{basin}}
(
z;\mathcal A_\alpha,\lambda
),
}
$$

則：

$$
z+\delta z
\in
\mathcal B_\alpha.
$$

### 證明

由：

$$
m_{\mathrm{basin}}
=
\operatorname{dist}
(
z,
\partial\mathcal B_\alpha
)
$$

定義，

開球：

$$
B
(
z,
m_{\mathrm{basin}}
)
$$

不穿越：

$$
\partial\mathcal B_\alpha.
$$

因：

$$
z
$$

位於 basin interior，

該球內任意點仍與：

$$
z
$$

位於同一 basin connected component。

若：

$$
\|\delta z\|
<
m_{\mathrm{basin}},
$$

則：

$$
z+\delta z
$$

仍在 basin 內。

證畢。

---

# 8. Basin Margin 是 Resilience，而非 Activity

兩個 states 可以有近似相同 observable activity：

$$
H(z_1)
\approx
H(z_2),
$$

但：

$$
m_{\mathrm{basin}}(z_1)
\gg
m_{\mathrm{basin}}(z_2).
$$

因此：

$$
\boxed{
\text{same output}
\not\Rightarrow
\text{same resilience}.
}
$$

---

# 9. Phase Slip

假設兩 coupled oscillators 處於同一 dynamical family。

relative phase：

$$
\Delta\theta
=
\theta_2-\theta_1.
$$

若 noise / perturbation 造成：

$$
\Delta\theta
$$

跨過 phase-locking branch 並發生：

$$
2\pi
$$

等價跳變，

稱 phase slip。

這通常是：

$$
\boxed{
\text{phase-relation transition}
}
$$

而不是 vector-field bifurcation。

---

# 10. Phase Slip 不等於 Basin Crossing

phase slip 可以：

- 發生於 same attractor / noisy locked regime；
- 也可能伴隨 crossing of phase-potential barrier。

具體取決於模型。

因此：

$$
\boxed{
\text{phase slip}
\neq
\text{general basin crossing}
}
$$

作為普遍同義詞。

---

# 11. Bifurcation

現在讓：

$$
\lambda
$$

改變。

若：

$$
F(z;\lambda)
$$

的 invariant sets / stability 在：

$$
\lambda_c
$$

發生 qualitative change，

稱：

$$
\boxed{
\text{bifurcation}.
}
$$

---

# 12. Bifurcation 與 Basin Crossing 的差別

### Basin crossing

$$
F
\text{ 固定},
$$

state 跨 basin。

### Bifurcation

$$
F(\cdot;\lambda)
$$

因：

$$
\lambda
$$

改變，

basin / attractor structure 本身改變。

因此：

$$
\boxed{
\text{state crosses landscape}
\neq
\text{landscape itself changes}.
}
$$

---

# 13. Strong-Coupling Synchronization Transition

PCPRT Paper 02 已指出：

strong coupling 可以改變 amplitude dynamics。

2024 electrochemical-oscillator experiments 更顯示：

- synchrony；
- rotating-wave / splay states；

之間的 transition 可以具有不同 criticality。

而 phase-only description 在 strong coupling 下可能無法正確描述 full-system bifurcation。

因此：

$$
\boxed{
\text{synchronization transition}
}
$$

本身可以是 bifurcation problem，

不只是：

$$
\Delta\theta
\rightarrow0.
$$

---

# 14. Parameter Regime

令：

$$
\mathcal D_\alpha
\subseteq
\Lambda
$$

為 attractor family：

$$
\mathcal A_\alpha(\lambda)
$$

保持某一 qualitative regime 的 parameter domain。

其 boundary：

$$
\partial\mathcal D_\alpha
$$

包含可能的 bifurcation set。

---

# 15. Bifurcation Margin

定義：

$$
\boxed{
m_{\mathrm{bif}}
(
\lambda;\mathcal D_\alpha
)
=
\operatorname{dist}
\left(
\lambda,
\partial
\mathcal D_\alpha
\right).
}
$$

這是 parameter space 中到 qualitative transition boundary 的 distance。

---

# 16. Current Basin Margin 與 Bifurcation Margin 獨立

可以：

$$
m_{\mathrm{basin}}
\gg0,
$$

但：

$$
m_{\mathrm{bif}}
\ll1.
$$

意味：

> state 現在很穩，但 parameter drift 快碰到 bifurcation。

反之也可以：

$$
m_{\mathrm{bif}}
\gg0,
$$

但：

$$
m_{\mathrm{basin}}
\ll1.
$$

意味：

> vector field 結構穩定，但 current state 很靠近 basin boundary。

---

# 17. 兩種 Resilience

因此至少分：

$$
\boxed{
R_{\mathrm{state}}
\sim
m_{\mathrm{basin}},
}
$$

以及：

$$
\boxed{
R_{\mathrm{param}}
\sim
m_{\mathrm{bif}}.
}
$$

前者是 state-space resilience。

後者是 parameter-space resilience。

---

# 18. Plasticity 會改變 Bifurcation Margin

PCPRT Paper 04：

$$
\dot\lambda
=
\varepsilon
G(z,\lambda,u).
$$

因此：

$$
\boxed{
\frac{d}{dt}
m_{\mathrm{bif}}
\neq
0
}
$$

一般成立。

也就是：

> carrier 的安全 margin 可以因 learning / adaptation 本身慢慢改變。

---

# 19. Moving Landscape

完整 adaptive carrier：

$$
\boxed{
\dot z
=
F(z;\lambda),
}
$$

$$
\boxed{
\dot\lambda
=
\varepsilon G(z,\lambda,u).
}
$$

因此 attractor：

$$
\mathcal A_\alpha(\lambda_t)
$$

與 basin：

$$
\mathcal B_\alpha(\lambda_t)
$$

都隨時間變。

本文稱：

$$
\boxed{
\text{moving dynamical landscape}.
}
$$

---

# 20. Adiabatic Tracking

若：

$$
\lambda
$$

變得足夠慢，

而：

$$
z
$$

對當前 attractor relaxation 足夠快，

trajectory 可以近似追蹤：

$$
\mathcal A_\alpha(\lambda(t)).
$$

這是 fast–slow adaptive system 的 adiabatic regime。

---

# 21. Tracking Failure

若：

$$
\lambda
$$

變化速度與 relaxation time 可比，

trajectory 可能無法繼續貼住 moving attractor。

因此：

$$
\boxed{
\text{slow parameter drift}
}
$$

相對誰慢很重要。

---

# 22. Relaxation Time

對 stable equilibrium：

$$
z^\star(\lambda),
$$

線性化：

$$
\boxed{
\dot\xi
=
J(\lambda)\xi.
}
$$

令：

$$
\alpha(\lambda)
=
\max_k
\operatorname{Re}
\lambda_k(J).
$$

穩定要求：

$$
\alpha<0.
$$

---

# 23. Local Recovery Rate

定義：

$$
\boxed{
r_{\mathrm{rec}}
=
|\alpha|.
}
$$

最慢 relaxation time scale：

$$
\boxed{
\tau_{\mathrm{rel}}
=
\frac1{
|\alpha|
}
}
$$

作為局部線性近似。

---

# 24. Critical Slowing Theorem

## 定理 24.1

若沿 parameter path：

$$
\lambda
\rightarrow
\lambda_c
$$

有 stable equilibrium：

$$
z^\star(\lambda),
$$

dominant linear eigenvalue：

$$
\alpha(\lambda)
=
\max_k
\operatorname{Re}\lambda_k
<0
$$

且：

$$
\alpha(\lambda)
\rightarrow
0^-,
$$

則 local linear relaxation time：

$$
\boxed{
\tau_{\mathrm{rel}}
=
\frac1{
|\alpha(\lambda)|
}
\rightarrow
\infty.
}
$$

### 證明

由定義直接成立。

證畢。

---

# 25. Critical Slowing 的物理意義

越接近：

$$
\alpha=0,
$$

小 perturbation 的 dominant decay 越慢。

因此：

$$
\boxed{
\text{same perturbation}
\rightarrow
\text{longer recovery}.
}
$$

這就是 resilience loss 的一個局部 dynamical signature。

---

# 26. Early Warning Proxy

在有 stochastic forcing：

$$
d\xi
=
\alpha\xi dt
+
\sigma dW_t
$$

的簡化 Ornstein–Uhlenbeck picture 中，

當：

$$
\alpha\rightarrow0^-,
$$

常可伴隨：

- variance increase；
- autocorrelation increase；
- slower recovery。

但這些 proxy 的可靠性依賴：

- bifurcation class；
- sampling；
- noise；
- nonstationarity；
- external forcing。

---

# 27. Critical Slowing 不是所有 Transition 的 Universal Indicator

例如：

- abrupt forcing；
- noise-induced jump；
- crisis；
- rate-induced tipping；
- some oscillatory / non-normal transitions；

未必展示標準：

$$
\alpha\rightarrow0
$$

型 slowing。

因此：

$$
\boxed{
\text{no CSD signal}
\not\Rightarrow
\text{no transition risk}.
}
$$

---

# 28. Daphnia Experiment

Drake–Griffen 2010 在 controlled deteriorating environments 的 Daphnia populations 中觀察到：

- coefficient of variation；
- skewness；
- autocorrelation；
- spatial correlation；

在 approaching extinction transition 前出現與 critical slowing 相容的變化。

本文只把它當作：

$$
\boxed{
\text{controlled experimental validation in one bifurcation system}.
}
$$

---

# 29. Neural Critical Dynamics

2024 hippocampal study 將：

- model；
- optogenetic mouse experiments；
- human intracranial EEG；

結合，

並以 excitability control 測得：

- resilience；
- perturbation response；
- recovery rate；
- critical transition。

其結果支持 hippocampal seizure onset 可在研究情境中表現出 fold-bifurcation-like critical dynamics。

---

# 30. Neural Example 的邊界

這不表示：

$$
\boxed{
\text{all cognition}
=
\text{seizure bifurcation dynamics}.
}
$$

更不表示健康腦普遍「瀕臨病理臨界點」。

它只證明：

> 真實 neural carrier 的 regime resilience、critical point 與 recovery dynamics 可以被實驗量測。

---

# 31. Metastability

現在考慮另一種 dynamical behavior。

trajectory 長時間停留於某 pattern：

$$
M_i,
$$

再快速轉到：

$$
M_j.
$$

這些 patterns 不一定都是 asymptotically stable attractors。

---

# 32. Metastable Macrostate

定義 coarse macrostate：

$$
\boxed{
M_i
\subseteq
\mathcal Z
}
$$

若 trajectory 在：

$$
M_i
$$

附近 dwell time：

$$
\tau_i^{\mathrm{dwell}}
$$

遠大於 transition duration：

$$
\tau_{ij}^{\mathrm{trans}},
$$

則可把：

$$
M_i
$$

視為 metastable macrostate。

---

# 33. Timescale Criterion

若：

$$
\boxed{
\tau_i^{\mathrm{dwell}}
\gg
\tau_{ij}^{\mathrm{trans}},
}
$$

則 coarse observer 會自然看到：

$$
\boxed{
\text{state}
\rightarrow
\text{rapid transition}
\rightarrow
\text{state}.
}
$$

---

# 34. Metastability 不要求 Multistability

Roberts 等 2019 的 whole-brain model 中，

多個 wave patterns 在固定參數下依序被訪問，

而 transition 可以在無 noise / external input 下自發發生。

作者將此與 multistability 區分，

因後者通常需要 perturbation 把 system 從一個 attractor 踢到另一個 attractor。

因此：

$$
\boxed{
\text{metastability}
\neq
\text{multistability}.
}
$$

---

# 35. Multistable Switching

對真正 multistable system：

$$
\mathcal A_1,
\mathcal A_2,
$$

transition 可能由：

- external perturbation；
- noise；
- parameter drift；

造成 basin crossing。

這類 transition 的 dwell time 可以由 escape statistics 描述。

---

# 36. Kramers Metastability

對受熱噪聲驅動的 particle：

$$
\dot x
=
-
U'(x)
+
\sqrt{2D}
\,\eta(t),
$$

如果存在 potential well 與 barrier：

$$
\Delta U,
$$

Kramers theory 在其適用 regime 中給出 escape rate 具有：

$$
\boxed{
k_{\mathrm{esc}}
\propto
e^{-\Delta U/D}
}
$$

或 thermal notation 下：

$$
\boxed{
k_{\mathrm{esc}}
\propto
e^{-\Delta U/k_BT}.
}
$$

prefactor 依 friction / curvature 等條件而定。

---

# 37. Barrier Height 是 Resilience，但只在相應模型中

如果 gradient-like stochastic model 合法，

$$
\Delta U
$$

可作 regime escape margin。

但 general driven-dissipative system：

$$
\boxed{
\text{need not admit a single equilibrium potential }U.
}
$$

---

# 38. Nonequilibrium Landscape + Flow

對 nonequilibrium stationary stochastic systems，

除了 probability landscape，

還可能存在 nonzero probability current：

$$
\mathbf J_{\mathrm{ss}}
\neq
0.
$$

因此 dynamics 由：

$$
\boxed{
\text{landscape}
+
\text{flow}
}
$$

共同決定。

2024 driven-dissipative experiment 直接量測了 energy landscape 與 flow dynamics，

顯示這不是單純概念提醒。

---

# 39. Potential Metaphor 的限制

所以 PCPRT 不使用：

$$
\boxed{
\text{brain = ball rolling in one universal potential landscape}
}
$$

作為普遍真理。

「landscape」只能在：

- model 定義清楚；
- state coordinates 合法；
- noise / current structure已知；

時具體化。

---

# 40. Dynamical Repertoire

本文定義：

$$
\boxed{
\mathfrak R
=
(
\mathfrak A,
\mathfrak M,E,\Lambda
).
}
$$

其中：

- $\mathfrak A$：attractor family；
- $\mathfrak M$：metastable macrostate family；
- $E$：allowed transition graph；
- $\Lambda$：parameter regime。

---

# 41. Admissible Dynamical Repertoire

安全版本：

$$
\boxed{
\mathfrak R_{\mathrm{adm}}
=
(
\mathfrak A_{\mathrm{adm}},
\mathfrak M_{\mathrm{adm}},
E_{\mathrm{adm}},
\Lambda_{\mathrm{adm}}
).
}
$$

這比：

$$
\mathcal S
\subseteq
\mathcal Z
$$

更適合描述「必須動」的 biological carrier。

---

# 42. State-Safe vs Regime-Safe

### State-safe

$$
z_t
\in
\mathcal S.
$$

### Regime-safe

$$
\boxed{
\text{trajectory belongs to an allowed dynamical regime and transition structure}.
}
$$

因此：

$$
\boxed{
\text{state-safe}
\not\Rightarrow
\text{regime-safe}.
}
$$

---

# 43. Transition Edge

定義 coarse regime label：

$$
r_t
\in
\mathcal R_{\mathrm{label}}.
$$

transition：

$$
r_i
\rightarrow
r_j
$$

若：

$$
(r_i,r_j)
\in
E_{\mathrm{adm}}
$$

則為允許 transition。

例如 biological cycle 本來就可能要求：

$$
r_1
\rightarrow
r_2
\rightarrow
r_3.
$$

禁止所有 transition 反而不合理。

---

# 44. Safe Dynamics 不是 Static Dynamics

對：

- neural oscillation；
- sleep–wake transition；
- locomotor central pattern generator；
- endocrine cycles；
- adaptive networks；

正常 function 本來就是 trajectory / cycle。

因此：

$$
\boxed{
\text{safe}
\neq
\text{stationary}.
}
$$

---

# 45. Repertoire Safety

本文定義一條 trajectory：

$$
z(t)
$$

為 repertoire-safe，若：

1. 所屬 macrostate 均在：
   $$
   \mathfrak A_{\mathrm{adm}}
   \cup
   \mathfrak M_{\mathrm{adm}};
   $$
2. 每次 coarse transition 屬於：
   $$
   E_{\mathrm{adm}};
   $$
3. carrier parameters：
   $$
   \lambda(t)
   \in
   \Lambda_{\mathrm{adm}}.
   $$

---

# 46. Repertoire-Safety Proposition

## 命題 46.1

若 coarse regime map：

$$
R:
\mathcal Z
\times
\Lambda
\rightarrow
\mathcal R_{\mathrm{label}}
$$

使所有實際 trajectory：

$$
(z(t),\lambda(t))
$$

皆滿足：

$$
R(z(t),\lambda(t))
\in
R_{\mathrm{adm}},
$$

且所有 consecutive regime transitions 皆位於：

$$
E_{\mathrm{adm}},
$$

則 trajectory 為 repertoire-safe。

這是一個定義型充分條件。

---

# 47. Repertoire Safety 仍需物理 Grounding

不能任意說：

$$
R_{\mathrm{adm}}
$$

是安全。

必須由：

- physiology；
- task function；
- hardware tolerance；
- survival / homeostasis；
- formal specification；

建立。

因此：

$$
\boxed{
\text{dynamical repertoire}
}
$$

是 safety representation，

不是 safety truth 本身。

---

# 48. Dynamical Reserve Vector

本文定義：

$$
\boxed{
\mathbf m_{\mathrm{dyn}}
=
(
m_{\mathrm{basin}},
m_{\mathrm{bif}},
r_{\mathrm{rec}},
m_{\mathrm{esc}},
m_{\mathrm{cap}},
\ldots
).
}
$$

其中：

- $m_{\mathrm{basin}}$：state-space basin margin；
- $m_{\mathrm{bif}}$：parameter-space bifurcation margin；
- $r_{\mathrm{rec}}$：local recovery rate；
- $m_{\mathrm{esc}}$：stochastic escape barrier proxy；
- $m_{\mathrm{cap}}$：capacity reserve。

---

# 49. Margin Vector 不宜壓成單一分數

兩 systems 可以：

- basin margin 大；
- bifurcation margin 小。

另一個反之。

因此：

$$
\boxed{
\mathbf m_{\mathrm{dyn}}
}
$$

更適合 Pareto / multi-risk comparison。

---

# 50. Recovery Rate 是動態 Resilience Indicator

如果：

$$
r_{\mathrm{rec}}
$$

下降，

表示小 perturbation 回到 local regime 的速度下降。

它可以在：

$$
m_{\mathrm{basin}}
$$

尚未很小時就出現改變。

因此：

$$
\boxed{
\text{distance margin}
\neq
\text{recovery-rate margin}.
}
$$

---

# 51. Safe Output Can Hide Resilience Loss

2024 hippocampal critical-dynamics experiment 的重要結構之一是：

> 系統 observable state 在逼近 critical point 時仍可看似 baseline-like，但 response to probing perturbation 逐步增加、recovery 變慢、resilience 下降。

因此：

$$
\boxed{
\text{normal output}
\not\Rightarrow
\text{normal resilience}.
}
$$

---

# 52. Passive vs Active Observation

passive time-series statistics：

- variance；
- autocorrelation；
- skewness；

可以提供 warning evidence。

但 active small perturbation response 直接估：

$$
r_{\mathrm{rec}}
$$

或 response gain，

在某些 systems 中可能更直接。

本文不提供任何 intervention protocol。

---

# 53. GPC Observability Interface

GPC-CS Paper 10：

$$
H(x)
$$

可能看不見：

$$
m_{\mathrm{basin}},
m_{\mathrm{bif}}.
$$

因此物理 carrier observability 應加入：

$$
\boxed{
H_{\mathrm{dyn}}
:
(z,\lambda)
\rightarrow
\text{resilience observables}.
}
$$

---

# 54. Metastable Transition Graph

對 metastable macrostates：

$$
M_1,\ldots,M_r,
$$

可以估計 transition matrix：

$$
\boxed{
P_{ij}
=
P
(
M_{t+\Delta}=M_j
\mid
M_t=M_i
).
}
$$

這是 coarse stochastic dynamics。

---

# 55. Transition Matrix 不是 Microscopic Law

$$
P_{ij}
$$

只是 coarse-grained regime-transition statistic。

它可能來自：

- deterministic chaos；
- noise；
- hidden variables；
- parameter drift。

因此：

$$
\boxed{
P_{ij}
\neq
\text{fundamental transition force}.
}
$$

---

# 56. Dwell-Time Distribution

每個 metastable state：

$$
M_i
$$

可有：

$$
\boxed{
p_i(\tau_{\mathrm{dwell}}).
}
$$

如果 tail 很長，

表示 long-lived metastability。

如果接近 exponential，

可能與 memoryless escape approximation 相容，

但不是必然。

---

# 57. Metastability 可以有功能

2019 expectation-driven sensory-coding study 顯示，

gustatory cortex metastable dynamics 的 transition timing 可被 expectation 調節，並加快 stimulus coding。

因此 metastability 不只是「不穩定」。

它可以是：

$$
\boxed{
\text{functional dynamical organization}.
}
$$

---

# 58. 因此安全不能消滅所有 Metastability

如果 biological computation 依賴 regime switching，

把 safety 定義成：

$$
\text{never switch}
$$

會直接殺死 function。

所以：

$$
\boxed{
\text{safe metastability}
}
$$

是必要概念。

---

# 59. Multistable Memory

離散 attractor dynamics 也可以支援：

- working memory；
- decision state；
- learned state。

因此：

$$
\boxed{
\text{multiple attractors}
\neq
\text{pathology}.
}
$$

---

# 60. Attractor Count 不是 Safety 指標

有很多 attractors 不一定好或壞。

重要的是：

- basin geometry；
- transition accessibility；
- functional assignment；
- parameter robustness。

---

# 61. Basin Volume

對 stochastic / uncertain initial states，

basin volume：

$$
\boxed{
V_\alpha
=
\mu
(
\mathcal B_\alpha
)
}
$$

可以影響 attractor accessibility。

但 volume 依 measure：

$$
\mu
$$

選擇。

因此不是 absolute property。

---

# 62. Basin Boundary Geometry

fractal / riddled basin boundaries 可以讓：

$$
m_{\mathrm{basin}}
$$

對 state 極度敏感。

此時 small perturbation outcome 很難預測。

因此：

$$
\boxed{
\text{same basin label}
}
$$

仍不代表相同 robustness。

---

# 63. Non-Normal Transient 與 Regime Safety

GPC-CS Paper 09 已指出：

$$
\rho(J)<1
$$

不保證 finite-time amplification 小。

因此即使 asymptotically 回到 attractor，

transient excursion 仍可能越出 physiological / hardware safety limits。

所以 regime-safe 還應檢查：

$$
\boxed{
\text{transient corridor}.
}
$$

---

# 64. Safe Basin 不等於 Safe Trajectory

即使：

$$
z_0,z_\infty
\in
\mathcal B_\alpha,
$$

trajectory 中途仍可能進入不允許：

$$
\mathcal U.
$$

因此：

$$
\boxed{
\text{basin membership}
\neq
\text{path safety}.
}
$$

這接回 GPC-CS Paper 06。

---

# 65. Basin-Safe Core

定義：

$$
\boxed{
\mathcal B_\alpha^{\mathrm{safe}}
=
\left\{
z\in
\mathcal B_\alpha:
\Phi_t(z)
\in
\mathcal S
\quad
\forall t\ge0
\right\}.
}
$$

這比普通 basin 更嚴格。

---

# 66. Plasticity Can Move Basin Boundaries

如果：

$$
\dot\lambda\neq0,
$$

那：

$$
\partial\mathcal B_\alpha(\lambda_t)
$$

本身在移動。

因此固定-time：

$$
m_{\mathrm{basin}}
$$

只是 instantaneous margin。

---

# 67. Dynamic Basin Margin

定義：

$$
\boxed{
m_{\mathrm{basin}}(t)
=
\operatorname{dist}
\left(
z_t,
\partial
\mathcal B_\alpha(\lambda_t)
\right).
}
$$

這才是 plastic carrier 的真正 state-space reserve。

---

# 68. Dynamic Bifurcation Margin

同樣：

$$
\boxed{
m_{\mathrm{bif}}(t)
=
\operatorname{dist}
\left(
\lambda_t,
\partial
\mathcal D_{\mathrm{adm}}
\right).
}
$$

可以因 slow plasticity 持續下降。

---

# 69. Safe Adaptation vs Dangerous Drift

如果：

$$
m_{\mathrm{bif}}
$$

下降但：

$$
m_{\mathrm{basin}}
$$

上升，

代表 system 可能在短期更穩、長期更靠 parameter transition。

因此 adaptation 的安全評估天然是 multi-timescale。

---

# 70. Critical Slowing 與 Plasticity

當：

$$
\lambda_t
$$

慢慢靠近：

$$
\lambda_c,
$$

如果：

$$
\alpha(\lambda_t)
\rightarrow0^-,
$$

則 recovery time 增長。

因此：

$$
\boxed{
\text{plastic parameter drift}
\rightarrow
\text{resilience drift}.
}
$$

---

# 71. Metaplasticity Can Move Criticality

PCPRT Paper 04 有：

$$
\dot\mu
\neq0.
$$

如果：

$$
\mu
$$

改變：

$$
G
$$

或：

$$
F
$$

的 effective parameters，

那麼 critical boundary 本身可以受更慢 history 調節。

所以：

$$
\boxed{
\text{criticality can be history-dependent}.
}
$$

---

# 72. Carrier Regime State

本文因此建議 physical carrier full state 至少分：

$$
\boxed{
Q
=
(
z,
\lambda,
\mu,
r
),
}
$$

其中：

$$
r
$$

不是新的 microscopic variable，

而是 coarse regime label：

$$
r
=
R(z,\lambda).
$$

---

# 73. Regime Label 是 Derived Variable

$$
r
$$

應該由：

- attractor identity；
- metastable cluster；
- phase pattern；
- functional mode；

等 observables / model 定義。

因此：

$$
\boxed{
r
\neq
\text{fundamental state variable}.
}
$$

---

# 74. Repertoire Transition

當：

$$
r_i
\rightarrow
r_j,
$$

需要問：

1. 是 phase slip？
2. 是 basin crossing？
3. 是 bifurcation？
4. 是 metastable deterministic switching？
5. 是 noise escape？
6. 是 topology / plasticity change？

同一表象 transition 可以有不同機制。

---

# 75. Mechanism Identifiability

只看到：

$$
r_i
\rightarrow
r_j
$$

不能唯一知道 underlying cause。

因此：

$$
\boxed{
\text{transition label}
\neq
\text{transition mechanism}.
}
$$

這是 Paper 10 observability 的 regime 版本。

---

# 76. Safety 需要 Mechanism-Sensitive Model

因為不同機制需要不同 margin：

- basin crossing： $m_{\mathrm{basin}}$ ；
- bifurcation： $m_{\mathrm{bif}}$ ；
- critical slowing： $r_{\mathrm{rec}}$ ；
- noise escape： $\Delta U$ / quasipotential；
- non-normal transient： $A_H$ ；
- topology shift：network margin。

---

# 77. 單一「壓力值」不足

因此 biological carrier stress 不應只用：

$$
s
\in
\mathbb R
$$

一個值。

更自然：

$$
\boxed{
\mathbf m_{\mathrm{dyn}}
}
$$

是多維 resilience state。

---

# 78. PCPRT Dynamical Safety Definition

本文提出：

> 一個 physical carrier 在時間區間 $[0,T]$ 內 dynamical-safe，若其 trajectory、parameter path 與 coarse regime sequence 均位於事先由具體 system 定義的 admissible dynamical repertoire，且所有必要 safety margins 未跨越指定最低界。

形式化：

$$
\boxed{
Q(t)
\in
\mathfrak R_{\mathrm{adm}}
\quad
\forall
t\in[0,T].
}
$$

---

# 79. 這不是 Universal Biology Definition

不同 carrier：

- neuron；
- whole brain；
- cell；
- molecular motor；
- computer oscillator；
- AI hardware network；

有完全不同：

$$
\mathfrak R_{\mathrm{adm}}.
$$

所以 PCPRT 只提供 framework。

---

# 80. 可證偽性

## 80.1 State-safe set 已足夠

若實際 carrier 的 function / risk 完全由 instantaneous state 決定，

且 attractor / transition structure 不增加預測力，

repertoire safety 可簡化回普通：

$$
\mathcal S.
$$

## 80.2 Basin margin 無預測力

若：

$$
m_{\mathrm{basin}}
$$

與 perturbation outcome 無關，

則其 resilience interpretation 失效。

## 80.3 Bifurcation margin 無法識別

若 parameter-space critical set 不可穩定定義，

$$
m_{\mathrm{bif}}
$$

只能保留為特定 model quantity。

## 80.4 Critical slowing absent

若 transition 不經 eigenvalue approach：

$$
\alpha\rightarrow0,
$$

CSD theorem 不適用。

## 80.5 Metastable coarse states 無時間尺度分離

若：

$$
\tau_{\mathrm{dwell}}
\sim
\tau_{\mathrm{trans}},
$$

metastable macrostate description 沒有良好 coarse-graining。

---

# 81. 本文的十個主命題

## 命題 A：Phase slip、basin crossing、bifurcation、metastable switching 必須分開

它們改變的是不同 dynamical object。

## 命題 B：Basin margin 提供固定 vector field 下的 state-space resilience

$$
\boxed{
m_{\mathrm{basin}}
=
\operatorname{dist}
(
z,\partial\mathcal B
).
}
$$

## 命題 C：Bifurcation margin 提供 parameter-space resilience

$$
\boxed{
m_{\mathrm{bif}}
=
\operatorname{dist}
(
\lambda,\partial\mathcal D
).
}
$$

## 命題 D：Approaching a zero-real-part eigenvalue produces local critical slowing

由定理 24.1。

## 命題 E：Critical slowing 不是所有 critical transition 的 universal warning sign

其 observational proxy 是 model-dependent。

## 命題 F：Metastability 不等於 multistability

長壽 transient / sequential dynamics 可在沒有多個 stable attractors 時存在。

## 命題 G：安全應由 admissible dynamical repertoire 描述

$$
\boxed{
\mathfrak R_{\mathrm{adm}}
}
$$

包含允許 regimes 與 transitions。

## 命題 H：正常輸出不代表 resilience margin 仍高

需要 dynamical observation。

## 命題 I：Plasticity 使 attractor landscape 與 safety margins 成為時間依賴量

$$
\boxed{
\mathcal A(\lambda_t),
\mathcal B(\lambda_t),
m_{\mathrm{bif}}(t).
}
$$

## 命題 J：生物安全不是「不變」，而是「允許範圍內的穩定變化」

這是 PCPRT 從 static safety 轉向 dynamical-regime safety 的核心。

---

# 82. 下一篇

PCPRT Paper 06 將進入：

$$
\boxed{
\text{神經相位與認知路由：Phase-Dependent Gating、Communication 與 Plasticity}.
}
$$

下一篇將重新搜尋一手文獻，並特別維持以下限制：

1. neural phase 不等於 semantic meaning；
2. phase-dependent communication 不等於 direct mind transfer；
3. phase locking 不等於 cognition identity；
4. 要分清 excitability gating、communication-through-coherence、sequence coding、phase-dependent plasticity；
5. 要接實驗資料而不是只靠振盪模型。

---

# 83. 結論

如果 carrier 是 biological / neural / adaptive physical system，

安全幾乎不可能被簡化成：

$$
z
=
z^\star.
$$

因為正常功能本身需要：

- oscillation；
- switching；
- learning；
- metastability；
- homeostasis；
- regime transition。

所以本文把安全重新放到：

$$
\boxed{
\mathfrak R_{\mathrm{adm}}.
}
$$

首先，

$$
m_{\mathrm{basin}}
$$

告訴我們當前 state 離 basin boundary 多遠。

其次，

$$
m_{\mathrm{bif}}
$$

告訴我們 carrier parameters 離 qualitative dynamical transition 多遠。

第三，

$$
r_{\mathrm{rec}}
=
|\alpha|
$$

告訴我們 local perturbation 回復速度。

在 gradient-like stochastic metastability 中，

barrier height：

$$
\Delta U
$$

又提供另一種 escape resilience。

這些量彼此不同。

因此真正 dynamical safety 更像：

$$
\boxed{
\mathbf m_{\mathrm{dyn}}
=
(
m_{\mathrm{basin}},
m_{\mathrm{bif}},
r_{\mathrm{rec}},
m_{\mathrm{esc}},
\ldots
).
}
$$

而不是一個：

$$
\text{safe/unsafe}
$$

單一瞬時 label。

最重要的是：

$$
\boxed{
\text{same current state}
\not\Rightarrow
\text{same dynamical future}.
}
$$

carrier 可能：

- 更靠 basin boundary；
- 更靠 bifurcation；
- recovery 更慢；
- noise escape 更容易；

即使 observable output 暫時完全正常。

所以 PCPRT 對「安全」的物理版本現在可以正式寫成：

$$
\boxed{
\text{Safety}
=
\text{remaining within an admissible dynamical repertoire with sufficient resilience margins}.
}
$$

這也讓下一步從物理自然進入認知科學：

> 如果 brain function 本來就利用 metastable regimes、phase relations 與 dynamical transitions，那麼 neural phase 在 information routing 中究竟扮演什麼角色？

這正是 Paper 06 的問題。

---

# 參考文獻

1. Kramers, H. A. (1940). Brownian motion in a field of force and the diffusion model of chemical reactions. *Physica*, 7(4), 284–304. DOI: 10.1016/S0031-8914(40)90098-2.
2. Drake, J. M., & Griffen, B. D. (2010). Early warning signals of extinction in deteriorating environments. *Nature*, 467, 456–459. DOI: 10.1038/nature09389.
3. Roberts, J. A., Gollo, L. L., Abeysuriya, R. G., Roberts, G., Mitchell, P. B., Woolrich, M. W., & Breakspear, M. (2019). Metastable brain waves. *Nature Communications*, 10, 1056. DOI: 10.1038/s41467-019-08999-0.
4. Mazzucato, L., La Camera, G., & Fontanini, A. (2019). Expectation-induced modulation of metastable activity underlies faster coding of sensory stimuli. *Nature Neuroscience*, 22, 787–796. DOI: 10.1038/s41593-019-0364-9.
5. Maturana, M. I., et al. (2020). Critical slowing down as a biomarker for seizure susceptibility. *Nature Communications*, 11, 2172. DOI: 10.1038/s41467-020-15908-3.
6. Ocampo-Espindola, J. L., Kiss, I. Z., Bick, C., & Wedgwood, K. C. A. (2024). Strong coupling yields abrupt synchronization transitions in coupled oscillators. *Physical Review Research*, 6, 033328. DOI: 10.1103/PhysRevResearch.6.033328.
7. Dumont, V., Bestler, M., Catalini, L., Margiani, G., Zilberberg, O., & Eichler, A. (2024). Energy landscape and flow dynamics measurements of driven-dissipative systems. *Physical Review Research*, 6, 043012. DOI: 10.1103/PhysRevResearch.6.043012.
8. Lepeu, G., van Maren, E., Slabeva, K., Friedrichs-Maeder, C., Fuchs, M., Z’Graggen, W. J., Pollo, C., Schindler, K. A., Adamantidis, A., Proix, T., et al. (2024). The critical dynamics of hippocampal seizures. *Nature Communications*, 15, 6945. DOI: 10.1038/s41467-024-50504-9.
9. [Primary network metastability study] (2025). Metastability in networks of stochastic integrate-and-fire neurons. *Physical Review E*, 111, 064402.
10. [Network critical-transition prediction study] (2024). Early Predictor for the Onset of Critical Transitions in Networked Dynamical Systems. *Physical Review X*, 14, 031009.

---

# 系列狀態

**Series:** Phase-Carrier Physical Realization Theory  
**Paper:** 05  
**Version:** v1.0  
**Canonical source encoding:** UTF-8  
**Canonical mathematics delimiters:** ` $...$ ` and `$$...$$` only  
**Operational regime-transition induction details:** Excluded  
**Depends on:** PCPRT Papers 01–04; GPC-CS Papers 01, 04, 05, 06, 09, 10  
**Next:** Paper 06 — 神經相位與認知路由：Phase-Dependent Gating、Communication 與 Plasticity
