# 物理相位、Phase Reduction 與載體變形
## 從 Isochron、Phase Response 到強耦合下的 Phase-Amplitude 有效理論

**英文題名：** Physical Phase, Phase Reduction, and Carrier Deformation: From Isochrons and Phase Response to Phase-Amplitude Effective Theory under Strong Coupling  
**系列：** 相位載體物理實現論（Phase-Carrier Physical Realization Theory, PCPRT）  
**Paper：** 02  
**作者：** Neo.K（許筌崴）  
**機構：** EveMissLab／一言諾科技有限公司  
**理論協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v1.0  
**日期：** 2026-08-14  
**狀態：** Public Theoretical Paper / Physical Phase Foundation

---

## 摘要

PCPRT Paper 01 將 GPC-CS 明確定位為候選有效理論，並建立：

$$
z
\in
\mathcal Z_{\mathrm{phys}},
\qquad
x
=
\Pi(z)
\in
\mathcal X_{\mathrm{GPC}},
$$

以及物理實現交換圖：

$$
\Pi
\circ
\Phi^{\mathrm{phys}}
\approx
\Gamma_{\mathrm{GPC}}
\circ
\Pi.
$$

本文進一步處理「phase」本身，並刻意區分：

$$
\boxed{
\text{physical phase}
\neq
\text{generalized relational phase}
\neq
\text{semantic / cognitive phase}.
}
$$

本文從具有穩定極限環：

$$
\gamma
=
\{
z^\star(t)
\}
$$

的非線性動力系統開始：

$$
\dot z
=
F(z).
$$

若極限環週期為 $T$，自然角頻率：

$$
\omega
=
\frac{2\pi}{T}.
$$

在 basin 中定義 asymptotic phase：

$$
\boxed{
\Theta:
\mathcal B(\gamma)
\rightarrow
S^1
}
$$

使沿未擾動軌跡：

$$
\boxed{
\frac{d}{dt}
\Theta(z(t))
=
\omega.
}
$$

等價地，在足夠光滑條件下：

$$
\boxed{
\nabla\Theta(z)
\cdot
F(z)
=
\omega.
}
$$

等相位集合：

$$
\mathcal I_\theta
=
\{
z:
\Theta(z)=\theta
\}
$$

即 isochrons。這些集合表明「phase」不是任意把狀態投影到圓上，而是由對極限環未來漸近 timing 的等價關係定義。

在弱擾動：

$$
\dot z
=
F(z)
+
\epsilon p(z,t),
\qquad
0<\epsilon\ll1,
$$

下，經典 phase reduction 給出第一階近似：

$$
\boxed{
\dot\theta
=
\omega
+
\epsilon
Z(\theta)
\cdot
p(z^\star(\theta),t)
+
O(\epsilon^2),
}
$$

其中：

$$
Z(\theta)
=
\nabla\Theta
\left(
z^\star(\theta)
\right)
$$

為 infinitesimal phase response curve / phase sensitivity function。對弱耦合 oscillator network，這可進一步平均化成 Kuramoto-like / general phase-coupling equation。本文把這一層視為**真正物理 phase 到低維 phase dynamics 的合法經典入口**。

然而，本文的核心並不是再次介紹 phase reduction，而是指出其物理閉包條件。對受輸入 $u$ 作用的 vector field：

$$
\dot z
=
F_u(z),
$$

只用：

$$
\theta
=
\Theta(z)
$$

作為狀態時，真正 phase velocity 為：

$$
v_\Theta(z,u)
=
D\Theta(z)
F_u(z).
$$

若同一 isochron：

$$
\Theta(z_1)=\Theta(z_2)=\theta
$$

上的不同 amplitude states 具有不同：

$$
v_\Theta(z_1,u)
\neq
v_\Theta(z_2,u),
$$

則不存在精確 memoryless phase-only equation：

$$
\dot\theta
=
f(\theta,u).
$$

本文因此定義 **phase-fiber closure defect**：

$$
\boxed{
\Omega_\Theta(\theta,u)
=
\operatorname{diam}
\left\{
D\Theta(z)F_u(z):
\Theta(z)=\theta
\right\}.
}
$$

並證明：對任意 phase-only candidate $f(\theta,u)$，其在該 phase fiber 上的 worst-case instantaneous error 至少為：

$$
\boxed{
\frac12
\Omega_\Theta(\theta,u).
}
$$

這是 PCPRT Paper 01 fiber-diameter lower bound 在物理相位上的專門化。它給出一條非常直接的判準：

$$
\boxed{
\Omega_\Theta
\approx0
\Rightarrow
\text{phase-only closure plausible};
}
$$

$$
\boxed{
\Omega_\Theta
\text{ large}
\Rightarrow
\text{amplitude / hidden-state dependence cannot be ignored}.
}
$$

這與現代 phase-amplitude reduction、isostable reduction 與 strongly perturbed phase-reduction 文獻具有直接接口。Kurebayashi、Shirasaka、Nakao 等人在 2013 年建立 generalized phase reduction，用慢變強擾動參數化相位；2022 年進一步處理 strongly coupled limit-cycle oscillators，允許 coupling 使 oscillator orbit 顯著變形。Wilson–Moehlis 的 isostable reduction 與 Wilson 2022 的 adaptive phase-amplitude framework 則將 transverse relaxation modes 顯式納入低維模型。

因此本文定義 phase-amplitude carrier state：

$$
\boxed{
q
=
(
\theta,
a_1,\ldots,a_m
),
}
$$

其中 $a_k$ 為 transverse / isostable / amplitude coordinates。最小 phase-amplitude effective model 為：

$$
\boxed{
\dot\theta
=
\omega
+
F_\theta
(
\theta,\mathbf a,u
),
}
$$

$$
\boxed{
\dot{\mathbf a}
=
\Lambda
\mathbf a
+
F_a
(
\theta,\mathbf a,u
),
}
$$

其中 $\Lambda$ 的衰減尺度與 Floquet exponents / transverse relaxation 相關。若 amplitude relaxation 很快， $\mathbf a$ 可以近似被消去；若 relaxation 很慢、擾動很強、耦合改變 orbit，則 $\mathbf a$ 不能被忽略。

本文把「載體變形（carrier deformation）」定義得比 amplitude excursion 更強。假設 coupling / forcing parameter：

$$
\lambda
$$

改變 vector field：

$$
F
\rightarrow
F_\lambda,
$$

且每個 $\lambda$ 對應一個週期軌道：

$$
\gamma_\lambda.
$$

定義 orbit deformation：

$$
\boxed{
D_{\mathrm{orb}}(\lambda)
=
d_H
\left(
\gamma_\lambda,
\gamma_0
\right),
}
$$

其中 $d_H$ 是適當狀態空間中的 Hausdorff distance。若 $D_{\mathrm{orb}}$ 不小，interaction 已不只是把 oscillator 沿原 orbit 推前／推後，而是改變 carrier oscillation 所在的幾何軌道。

更一般地，若 coupling 改變：

- 自然頻率；
- limit-cycle shape；
- Floquet multipliers；
- isochrons；
- phase-response function；
- amplitude relaxation time；

則本文稱 carrier 進入 **deformed phase regime**。在此 regime 中，原始：

$$
\theta_0
=
\Theta_0(z)
$$

可能仍可作為 observation coordinate，但不再應被假定為完整 dynamical state。

本文進一步提出 **physical-phase realization criterion for GPC**。若 GPC effective state：

$$
x
=
\Pi(z)
$$

具有 generalized phase：

$$
\varphi:
\mathcal X
\rightarrow
S^1,
$$

要聲稱它真正對應 physical phase：

$$
\Theta:
\mathcal Z
\rightarrow
S^1,
$$

至少應滿足：

$$
\boxed{
\Theta
=
\varphi
\circ
\Pi
\quad
(\mathrm{mod}\ 2\pi),
}
$$

以及相應 dynamical consistency。若存在：

$$
\Pi(z_1)=\Pi(z_2)
$$

但：

$$
\Theta(z_1)
\neq
\Theta(z_2),
$$

則 GPC coarse state $x$ 無法精確辨識 physical phase。反過來，GPC 中的 generalized relational phase 若沒有任何 $\Theta$ 可滿足此 factorization，也不應被稱為底層 physical phase。

本文最後建立四層 phase hierarchy：

$$
\boxed{
P_0:
\text{physical oscillator phase}
}
$$

$$
\boxed{
P_1:
\text{relative / synchronization phase}
}
$$

$$
\boxed{
P_2:
\text{collective dynamical phase / regime}
}
$$

$$
\boxed{
P_3:
\text{generalized GPC relational phase}.
}
$$

它們可以透過 coarse-graining 與 order parameters 建立映射，但不應直接畫等號。

本文不提供任何操控神經振盪、強制同步、刺激參數、注入方法或控制策略。其目的只是建立一條保守物理橋：

$$
\boxed{
\text{phase-only}
\rightarrow
\text{phase-amplitude}
\rightarrow
\text{carrier deformation}
\rightarrow
\text{generalized effective phase}.
}
$$

**關鍵詞：** 物理相位、極限環、isochron、phase response curve、phase reduction、isostable、phase-amplitude reduction、強耦合、載體變形、同步、有效理論

---

# 0. 文獻定位

Kuramoto 1975 的 coupled-oscillator 工作是同步理論的經典入口，但 Kuramoto phase model 本身並不是所有物理 oscillators 的 microscopic law。標準 phase model 通常是從更高維 stable limit-cycle system 經 weak-coupling / averaging reduction 得到的低維近似。

Kurebayashi、Shirasaka、Nakao 2013 指出，經典 phase reduction 對弱擾動非常有效，但若存在慢變的強擾動，oscillator 的 shape 與 frequency 可以大幅改變，因此提出 parameter-dependent generalized phase reduction。

Kurebayashi、Yamamoto、Shirasaka、Nakao 2022 進一步研究 strongly coupled limit-cycle oscillators，明確允許 strong parametric coupling 大幅改變每個 oscillator 的 orbit。

Wilson–Moehlis 2016 的 isostable reduction 則指出：單純 phase reduction 丟掉了系統回到 periodic orbit 的 transverse information。當 Floquet multipliers 對應的 decay 不夠快時，phase-only description 的實用性下降。

Wilson 2022 再以 adaptive phase-amplitude transformation 擴張 strongly perturbed oscillatory systems 的低維描述。

因此本文不把：

$$
\boxed{
\dot\theta
=
\omega
+
K\sin(\theta_j-\theta_i)
}
$$

當作「相位交流」的普遍底層方程。

PCPRT 更關心：

> 這個 phase equation 是從哪個 physical state space 合法降維而來？在什麼 coupling / relaxation / noise regime 下仍成立？

---

# 1. Stable Limit Cycle

考慮：

$$
\boxed{
\dot z
=
F(z),
}
$$

其中：

$$
z
\in
\mathbb R^n
$$

或一般 smooth state manifold。

假設存在 stable periodic orbit：

$$
\gamma
=
\{
z^\star(t):
t\in[0,T)
\},
$$

滿足：

$$
z^\star(t+T)
=
z^\star(t).
$$

自然頻率：

$$
\boxed{
\omega
=
\frac{2\pi}{T}.
}
$$

---

# 2. 物理 Phase 不是「角度長得像角度」

在極限環上可以定義：

$$
\theta
=
\omega t
\quad
(\mathrm{mod}\ 2\pi).
$$

但離開 orbit 後，phase 的真正延伸需要 asymptotic timing。

定義：

$$
\boxed{
\Theta:
\mathcal B(\gamma)
\rightarrow
S^1.
}
$$

如果：

$$
z_1,z_2
$$

在長時間後趨向 limit cycle 上相同 timing point，則賦予相同 asymptotic phase。

---

# 3. Isochron

定義：

$$
\boxed{
\mathcal I_\theta
=
\{
z
\in
\mathcal B(\gamma):
\Theta(z)=\theta
\}.
}
$$

 $\mathcal I_\theta$ 稱為 isochron。

isochron 的物理意義是：

> 多個不同 amplitude / transverse states，雖然當下空間位置不同，未擾動時長期會以相同 asymptotic phase 靠近 limit cycle。

因此：

$$
\boxed{
\text{same phase}
\not\Rightarrow
\text{same physical state}.
}
$$

這是本文後續所有 phase-only closure 問題的根。

---

# 4. Phase Function PDE

若：

$$
\Theta
$$

足夠光滑，沿未擾動軌跡：

$$
\frac{d}{dt}
\Theta(z(t))
=
\nabla\Theta(z)
\cdot
F(z).
$$

由 phase definition：

$$
\boxed{
\nabla\Theta(z)
\cdot
F(z)
=
\omega.
}
$$

這是一個 phase function 的局部 characterization。

---

# 5. Infinitesimal Phase Response Curve

在 limit cycle 上：

$$
z^\star(\theta),
$$

定義：

$$
\boxed{
Z(\theta)
=
\nabla\Theta
\left(
z^\star(\theta)
\right).
}
$$

 $Z(\theta)$ 表示 infinitesimal perturbation 對 phase 的一階敏感度。

它不是語義權重。

它是：

$$
\boxed{
\text{physical state perturbation}
\rightarrow
\text{timing shift}
}
$$

的局部導數。

---

# 6. Weakly Perturbed Oscillator

考慮：

$$
\dot z
=
F(z)
+
\epsilon p(z,t),
$$

其中：

$$
0<\epsilon\ll1.
$$

phase derivative：

$$
\dot\theta
=
D\Theta(z)
\left[
F(z)
+
\epsilon p(z,t)
\right].
$$

由：

$$
D\Theta(z)F(z)=\omega,
$$

得到：

$$
\dot\theta
=
\omega
+
\epsilon
D\Theta(z)
p(z,t).
$$

若 trajectory 持續足夠接近 limit cycle，可用：

$$
z
\approx
z^\star(\theta)
$$

得到第一階 phase reduction：

$$
\boxed{
\dot\theta
=
\omega
+
\epsilon
Z(\theta)
\cdot
p
\left(
z^\star(\theta),t
\right)
+
O(\epsilon^2).
}
$$

---

# 7. Phase Reduction 是條件式有效理論

上式依賴至少以下近似：

- stable limit cycle；
- perturbation 對 orbit 的偏離受控；
- transverse modes 足夠快 relaxation；
- phase coordinate 對研究目標足夠；
- higher-order coupling 不支配。

因此：

$$
\boxed{
\text{phase reduction}
\neq
\text{unconditional law}.
}
$$

---

# 8. 弱耦合 Oscillator Pair

兩個 physical oscillators：

$$
\dot z_1
=
F_1(z_1)
+
\epsilon C_{12}(z_1,z_2),
$$

$$
\dot z_2
=
F_2(z_2)
+
\epsilon C_{21}(z_2,z_1).
$$

經 phase reduction：

$$
\dot\theta_1
=
\omega_1
+
\epsilon
Z_1(\theta_1)
\cdot
C_{12}
\left(
z_1^\star(\theta_1),
z_2^\star(\theta_2)
\right),
$$

$$
\dot\theta_2
=
\omega_2
+
\epsilon
Z_2(\theta_2)
\cdot
C_{21}
\left(
z_2^\star(\theta_2),
z_1^\star(\theta_1)
\right).
$$

再經適當 averaging，才可能得到只依賴相位差的 coupling function。

---

# 9. Kuramoto 類模型的位置

若系統進一步滿足近似條件，可得到：

$$
\boxed{
\dot\theta_i
=
\omega_i
+
\sum_j
K_{ij}
H_{ij}
(
\theta_j-\theta_i
).
}
$$

Kuramoto sine coupling：

$$
H(\Delta\theta)
=
\sin(\Delta\theta)
$$

只是其中一個重要特例。

因此 PCPRT 把 Kuramoto model 放在：

$$
\boxed{
\text{physical high-D oscillator}
\rightarrow
\text{phase reduction}
\rightarrow
\text{averaging}
\rightarrow
\text{Kuramoto-like model}.
}
$$

不是底層第一層。

---

# 10. Phase Fiber Closure Problem

現在考慮一般受輸入／耦合作用的 vector field：

$$
\boxed{
\dot z
=
F_u(z).
}
$$

保留原 phase coordinate：

$$
\theta
=
\Theta(z).
$$

瞬時 phase velocity：

$$
\boxed{
v_\Theta(z,u)
=
D\Theta(z)
F_u(z).
}
$$

如果希望存在精確 phase-only equation：

$$
\dot\theta
=
f(\theta,u),
$$

則相同：

$$
\theta
$$

上的所有 physical states 必須具有同一 phase velocity。

---

# 11. Exact Phase-Only Closure Theorem

## 定理 11.1

存在函數：

$$
f:
S^1
\times
\mathcal U
\rightarrow
\mathbb R
$$

使：

$$
\boxed{
D\Theta(z)F_u(z)
=
f(\Theta(z),u)
}
$$

對研究域內所有 $(z,u)$ 成立，當且僅當：

$$
\boxed{
\Theta(z_1)
=
\Theta(z_2)
\Rightarrow
D\Theta(z_1)F_u(z_1)
=
D\Theta(z_2)F_u(z_2)
}
$$

對所有相同 $u$ 成立。

### 證明

若 $f$ 存在，兩個相同 phase 的 states 代入右側皆為：

$$
f(\theta,u),
$$

因此 phase velocities 相同。

反之，若 phase velocity 在每一個 phase fiber 上為常數，定義：

$$
f(\theta,u)
=
D\Theta(z)F_u(z)
$$

其中任取：

$$
z
\in
\Theta^{-1}(\theta).
$$

由 fiber constancy， $f$ 良定義。

證畢。

---

# 12. Phase-Fiber Closure Defect

定義：

$$
\boxed{
\Omega_\Theta(\theta,u)
=
\operatorname{diam}
\left\{
D\Theta(z)F_u(z):
\Theta(z)=\theta
\right\}.
}
$$

如果：

$$
\Omega_\Theta(\theta,u)
=
0
$$

對所有 $(\theta,u)$ 成立，phase-only closure 精確可行。

如果：

$$
\Omega_\Theta
$$

大，phase-only deterministic closure 有 intrinsic ambiguity。

---

# 13. Phase-Only Error Lower Bound

## 定理 13.1

對任意 phase-only candidate：

$$
f(\theta,u),
$$

有：

$$
\boxed{
\sup_{
z:
\Theta(z)=\theta
}
\left|
D\Theta(z)F_u(z)
-
f(\theta,u)
\right|
\ge
\frac12
\Omega_\Theta(\theta,u).
}
$$

### 證明

取 phase fiber 中兩個 phase velocity：

$$
v_1,
v_2
$$

使：

$$
|v_1-v_2|
$$

任意接近：

$$
\Omega_\Theta(\theta,u).
$$

對任意 scalar center：

$$
c=f(\theta,u),
$$

至少一個：

$$
|v_1-c|,
\quad
|v_2-c|
$$

不小於：

$$
\frac12
|v_1-v_2|.
$$

取 supremum 即得。

證畢。

---

# 14. Phase-Only Failure 的物理來源

造成：

$$
\Omega_\Theta>0
$$

的來源可能包括：

- amplitude dependence；
- slow transverse relaxation；
- strong forcing；
- state-dependent coupling；
- coupling-induced orbit deformation；
- hidden parameter drift；
- noise-state coupling；
- multi-timescale dynamics。

因此：

$$
\boxed{
\Omega_\Theta
}
$$

是一個 physical diagnostic，而不是哲學符號。

---

# 15. Floquet Relaxation

對 stable limit cycle，其 transverse perturbations 的一階演化可由 Floquet theory 描述。

若非平凡 Floquet exponents：

$$
\lambda_k
$$

滿足：

$$
\operatorname{Re}\lambda_k<0,
$$

則對應 transverse mode 以：

$$
e^{\lambda_k t}
$$

尺度衰減。

定義最慢 amplitude relaxation time：

$$
\boxed{
\tau_{\mathrm{amp}}
\sim
\frac{1}{
\min_k
|
\operatorname{Re}\lambda_k
|
}.
}
$$

這只是量級表示。

---

# 16. Fast Amplitude Relaxation

如果：

$$
\tau_{\mathrm{amp}}
\ll
\tau_{\mathrm{forcing}},
$$

被 perturbation 推離 orbit 的 amplitude deviation 會很快回落。

此時：

$$
\boxed{
\text{phase-only approximation}
}
$$

通常更可信。

---

# 17. Slow Amplitude Relaxation

如果：

$$
\tau_{\mathrm{amp}}
\sim
\tau_{\mathrm{forcing}},
$$

甚至：

$$
\tau_{\mathrm{amp}}
>
\tau_{\mathrm{forcing}},
$$

amplitude state 會跨多個 interaction cycles 持續存在。

此時：

$$
\boxed{
\text{phase is not a sufficient state variable}.
}
$$

這與 Wilson–Moehlis 的 isostable reduction 動機一致。

---

# 18. Isostable / Amplitude Coordinates

除 phase：

$$
\theta,
$$

再引入 transverse coordinates：

$$
a_1,\ldots,a_m.
$$

最小有效狀態：

$$
\boxed{
q
=
(
\theta,
\mathbf a
).
}
$$

近 limit cycle 可寫成：

$$
\boxed{
\dot\theta
=
\omega
+
F_\theta
(
\theta,\mathbf a,u
),
}
$$

$$
\boxed{
\dot{\mathbf a}
=
\Lambda\mathbf a
+
F_a
(
\theta,\mathbf a,u
).
}
$$

---

# 19. Phase-Amplitude Closure

Phase-amplitude model 的目標不是永久保留所有微觀自由度。

它只是比 phase-only 多保留：

> 對未來 timing / response 仍有顯著作用的 slow transverse modes。

因此 PCPRT Paper 01 的 coarse-graining 層級變成：

$$
\boxed{
z
\rightarrow
(
\theta,\mathbf a
)
\rightarrow
\theta.
}
$$

第二次 coarse-graining：

$$
(
\theta,\mathbf a
)
\rightarrow
\theta
$$

只有在 amplitude 可消去時才合理。

---

# 20. Strong Perturbation 不等於必然不能做 Phase Reduction

Kurebayashi 等 2013 的重要貢獻正是：

> 在特定條件下，即使 perturbation 強，只要可以拆成相對 amplitude relaxation 慢變的強分量與其餘弱 fluctuation，仍可定義 parameter-dependent generalized phase。

因此：

$$
\boxed{
\text{strong input}
\not\Rightarrow
\text{phase theory impossible}.
}
$$

更準確的是：

> standard fixed-orbit phase coordinate 可能不夠。

---

# 21. Parameterized Phase

令慢變參數：

$$
\lambda(t)
$$

改變 vector field：

$$
\dot z
=
F(z;\lambda(t)).
$$

若每個固定：

$$
\lambda
$$

都有 stable periodic orbit：

$$
\gamma_\lambda,
$$

可以定義 parameterized phase：

$$
\boxed{
\Theta(z;\lambda).
}
$$

因此：

$$
\theta(t)
=
\Theta
(
z(t);
\lambda(t)
).
$$

此時 phase coordinate 本身隨 carrier regime 改變。

---

# 22. Orbit Deformation

選擇 baseline：

$$
\lambda_0.
$$

對應：

$$
\gamma_0
=
\gamma_{\lambda_0}.
$$

定義：

$$
\boxed{
D_{\mathrm{orb}}(\lambda)
=
d_H
(
\gamma_\lambda,
\gamma_0
).
}
$$

 $D_{\mathrm{orb}}$ 描述 periodic orbit 的幾何變形。

它不是 phase shift。

如果：

$$
D_{\mathrm{orb}}>0,
$$

說明 oscillator 的運動軌道本身改變。

---

# 23. Carrier Deformation

本文把「載體變形」定義成一組比單一 orbit distance 更廣的變化。

定義 carrier dynamical descriptor：

$$
\boxed{
\mathcal D_\lambda
=
(
\gamma_\lambda,
\omega_\lambda,
\Theta_\lambda,
Z_\lambda,
\Lambda_\lambda
).
}
$$

其中包括：

- periodic orbit；
- natural frequency；
- isochrons / phase function；
- phase response function；
- transverse relaxation spectrum。

carrier deformation 可以定義為：

$$
\boxed{
\Delta_{\mathrm{car}}
(
\lambda,\lambda_0
)
=
d_{\mathcal D}
(
\mathcal D_\lambda,
\mathcal D_{\lambda_0}
).
}
$$

 $d_{\mathcal D}$ 必須依具體系統定義。

---

# 24. Interaction 不只改 Phase

因此：

$$
\boxed{
\theta
\rightarrow
\theta'
}
$$

只是最弱情況。

更一般：

$$
\boxed{
(
\theta,
\mathbf a,
\lambda
)
\rightarrow
(
\theta',
\mathbf a',
\lambda'
).
}
$$

其中：

$$
\lambda'
\neq
\lambda
$$

表示 interaction 已經改變 carrier dynamical parameters。

這為下一篇的 plastic carrier 建立物理接口。

---

# 25. Strong Coupling Regime

兩個 oscillators：

$$
\dot z_i
=
F_i
(
z_i;
\lambda_i
)
+
C_i
(
z_i,z_j
).
$$

若：

$$
C_i
$$

不再是 $O(\epsilon)$ 小量，

不能直接把 coupling 當成沿固定 limit cycle 的微小 phase push。

2022 的 strongly coupled phase-reduction 工作正是允許：

$$
\boxed{
\gamma_i
\rightarrow
\gamma_i^{\mathrm{coupled}}
}
$$

大幅變形後再建立 self-consistent phase description。

---

# 26. Strong Coupling 可造成質變

2024 年的 coupled-oscillator 研究顯示，強耦合可以伴隨不同 phase-locked solutions 之間的 abrupt synchronization transitions。

因此 coupling strength 不只控制：

$$
\text{同步快慢}.
$$

它還可能改變：

$$
\boxed{
\text{available dynamical regimes}.
}
$$

這將在 PCPRT 後續 metastability / bifurcation paper 正式處理。

---

# 27. Higher-Order Phase Interactions

即使 coupling 還算 moderate，第一階 pairwise phase model 也可能不足。

高階 phase reduction 可以生成：

$$
\boxed{
\text{nonpairwise / multibody phase terms}.
}
$$

例如：

$$
H
(
\theta_i,
\theta_j,
\theta_k
).
$$

因此：

$$
\boxed{
\text{pairwise phase network}
\neq
\text{most general reduced phase network}.
}
$$

這與 GPC-CS Paper 09 的高階 network dependence 很契合。

---

# 28. Noise 也會進入 Phase Reduction

真實 oscillator 常有：

$$
d z
=
F(z)dt
+
G(z)dW_t.
$$

noise 經 phase reduction 後並不只變成簡單 additive white phase noise。

其形式會依：

- noise interpretation；
- amplitude relaxation；
- correlation time；
- phase sensitivity；

而變。

Teramae–Nakao–Ermentrout 2009 明確指出 stochastic phase equation 受 noise correlation time 與 amplitude relaxation time 的比例影響。

---

# 29. Noise 不是單純 Error

因此 PCPRT 對 noise 的立場是：

$$
\boxed{
\text{noise}
=
\text{dynamical input}.
}
$$

它可以：

- broadening phase distribution；
- induce phase slips；
- change entrainment；
- under some systems contribute to synchronization。

安全判斷不能把所有 noise 自動分類成 damage。

---

# 30. Phase Slip

若 relative phase：

$$
\delta
=
\theta_2-\theta_1
$$

在 locked regime 附近受 noise / perturbation 作用，

可能越過 phase-lock basin 的 separatrix，造成：

$$
\delta
\rightarrow
\delta+2\pi
$$

型 phase slip。

phase slip 是：

$$
\boxed{
\text{phase relation transition},
}
$$

不是 carrier identity change。

---

# 31. Physical Phase 與 Relative Phase

單一 oscillator physical phase：

$$
\theta_i
=
\Theta_i(z_i).
$$

relative phase：

$$
\boxed{
\Delta_{ij}
=
\operatorname{wrap}
(
\theta_j-\theta_i
).
}
$$

這是第二層：

$$
P_1.
$$

它已經不是單一 carrier 的 intrinsic coordinate，而是 relational variable。

---

# 32. Collective Order Parameter

對 oscillator population：

$$
\theta_1,\ldots,\theta_N,
$$

可定義 Kuramoto order parameter：

$$
\boxed{
re^{i\psi}
=
\frac1N
\sum_{j=1}^{N}
e^{i\theta_j}.
}
$$

其中：

$$
r
$$

表示 phase coherence，

$$
\psi
$$

為 collective phase。

這是第三種 coarse-graining：

$$
\boxed{
\{
\theta_i
\}_{i=1}^{N}
\rightarrow
(r,\psi).
}
$$

---

# 33. Collective Phase 不等於 Individual Phase

即使：

$$
\psi
$$

存在，

它是 population order parameter 的 angle。

它不等於任一：

$$
\theta_i.
$$

因此：

$$
\boxed{
\text{collective phase}
\neq
\text{single-carrier phase}.
}
$$

---

# 34. Dynamical Regime Phase

某些跨學科使用「phase」指：

- synchronized phase；
- incoherent phase；
- ordered phase；
- chaotic phase；
- metastable regime。

這裡的 phase 更接近：

$$
\boxed{
\text{phase of matter / dynamical regime}.
}
$$

它不是 $S^1$ 上的 oscillator angle。

因此 PCPRT 將其放在：

$$
P_2.
$$

---

# 35. 四層 Phase Hierarchy

本文提出：

## $P_0$ — Physical Oscillator Phase

$$
\Theta(z)
\in
S^1.
$$

## $P_1$ — Relational Phase

$$
\Delta_{ij}
=
\theta_j-\theta_i.
$$

## $P_2$ — Collective / Dynamical Phase

例如：

$$
r,
\psi,
\text{regime label}.
$$

## $P_3$ — Generalized GPC Phase

表示高層 carrier-state relation、alignment、phase-like structural coordinate。

因此：

$$
\boxed{
P_0
\rightarrow
P_1
\rightarrow
P_2
\rightarrow
P_3
}
$$

是一條可能的 coarse-graining chain，不是同義詞鏈。

---

# 36. GPC Physical-Phase Factorization

令：

$$
x
=
\Pi(z)
$$

為 GPC state。

假設 GPC 定義：

$$
\varphi:
\mathcal X
\rightarrow
S^1.
$$

若聲稱：

$$
\varphi
$$

就是 physical phase 的 effective representation，至少需要：

$$
\boxed{
\Theta(z)
=
\varphi(\Pi(z))
\quad
(\mathrm{mod}\ 2\pi).
}
$$

---

# 37. Physical Phase Identifiability Theorem

## 定理 37.1

存在：

$$
\varphi:
\Pi(\mathcal Z)
\rightarrow
S^1
$$

使：

$$
\boxed{
\Theta
=
\varphi
\circ
\Pi
}
$$

當且僅當：

$$
\boxed{
\Pi(z_1)=\Pi(z_2)
\Rightarrow
\Theta(z_1)=\Theta(z_2).
}
$$

### 證明

與 PCPRT Paper 01 的 fiber factorization criterion 同型。

若 factorization 存在，fiber 上 phase 必相同。

反之，若 $\Theta$ 在每個 $\Pi$ -fiber 上常數，定義：

$$
\varphi(x)
=
\Theta(z)
$$

其中任取：

$$
z\in\Pi^{-1}(x).
$$

即得。

證畢。

---

# 38. 這個定理限制 GPC 的 Phase 用語

如果：

$$
\Pi(z_1)=\Pi(z_2)
$$

卻：

$$
\Theta(z_1)\neq\Theta(z_2),
$$

那麼目前的：

$$
x
$$

不足以知道 physical phase。

此時 GPC 的：

$$
\varphi(x)
$$

最多是一個 generalized effective coordinate。

不能宣稱是 physical oscillator phase。

---

# 39. Dynamic Consistency 還需要第二個條件

即使：

$$
\Theta
=
\varphi\circ\Pi,
$$

仍須檢查：

$$
\boxed{
\frac{d}{dt}
\varphi(x_t)
}
$$

是否與 physical phase dynamics 一致。

因此 phase realization 至少需要：

### State factorization

$$
\Theta
=
\varphi\circ\Pi.
$$

### Dynamic consistency

$$
\dot\varphi
\approx
f_{\mathrm{phase}}
(
\varphi,\ldots
).
$$

只有第一項不夠。

---

# 40. Generalized Phase 可以比 Physical Phase 更廣

GPC 中可以有：

$$
\varphi_{\mathrm{GPC}}
$$

描述：

- alignment；
- reconstruction regime；
- semantic relation；
- functional state relation。

這些 variable 若沒有物理 $S^1$ oscillator phase 對應，也可以作為有效理論變量。

因此 PCPRT 並不是：

> 把所有 generalized phase 都淘汰。

而是：

$$
\boxed{
\text{label the level correctly}.
}
$$

---

# 41. Carrier Deformation 與 GPC State Update

GPC-CS 的：

$$
x
\rightarrow
x'
$$

到了 physical oscillator carrier 可以至少分成：

$$
\boxed{
\Delta\theta
}
$$

$$
\boxed{
\Delta\mathbf a
}
$$

$$
\boxed{
\Delta\lambda.
}
$$

三者分別表示：

- timing shift；
- transverse state change；
- carrier dynamical parameter change。

這三者是完全不同的物理效應。

---

# 42. Weak Phase Interaction

最弱 regime：

$$
\Delta\lambda
\approx0,
$$

$$
\mathbf a
\approx0.
$$

interaction 主要表現：

$$
\boxed{
\theta
\rightarrow
\theta'.
}
$$

這是 phase-only GPC 最容易物理實現的區域。

---

# 43. Phase-Amplitude Interaction

中間 regime：

$$
\Delta\lambda
\approx0,
$$

但：

$$
\mathbf a
\not\approx0.
$$

interaction 改變：

$$
\boxed{
(\theta,\mathbf a).
}
$$

需要 phase-amplitude model。

---

# 44. Carrier-Deforming Interaction

更強 regime：

$$
\Delta\lambda
\not\approx0.
$$

interaction 改變：

$$
\boxed{
\mathcal D_\lambda.
}
$$

這時連 phase function、PRC、relaxation spectrum 都可能改變。

這才是本文最嚴格意義的：

$$
\boxed{
\text{carrier deformation}.
}
$$

---

# 45. Carrier Deformation 不等於 Damage

如果：

$$
\lambda
$$

改變，

不代表：

$$
\text{unsafe}.
$$

例如 adaptive biological oscillator 本來就可能改變：

- coupling；
- frequency；
- sensitivity；
- plasticity state。

因此：

$$
\boxed{
\text{deformation}
\neq
\text{damage}.
}
$$

安全與否仍須由 admissible dynamical repertoire 判定。

---

# 46. 物理安全應包含 Regime

對 oscillator carrier，安全不一定是一個 state ball。

更適合定義：

$$
\boxed{
\mathcal R_{\mathrm{adm}}
=
\{
\text{admissible limit cycles, amplitudes, phases, transitions}
\}.
}
$$

如果 carrier deformation 仍停留在：

$$
\mathcal R_{\mathrm{adm}},
$$

可視為正常適應。

如果跨越：

$$
\partial\mathcal R_{\mathrm{adm}},
$$

才構成 regime-level safety violation。

---

# 47. Bifurcation 是後續關鍵

如果 parameter：

$$
\lambda
$$

穿過 critical value：

$$
\lambda_c,
$$

可能發生：

- limit cycle disappearance；
- new attractor creation；
- synchronization transition；
- amplitude death；
- multistability；
- abrupt phase-lock switch。

因此 carrier deformation 與 safety 的真正交界通常不是：

$$
|\Delta\theta|
$$

本身，

而是：

$$
\boxed{
\text{distance to bifurcation / basin boundary}.
}
$$

這會在後續 paper 正式研究。

---

# 48. Phase Slip 與 Bifurcation 不是同一件事

phase slip 可以在同一 underlying oscillator regime 中發生。

bifurcation 則改變 dynamical structure。

因此：

$$
\boxed{
\text{phase relation change}
\neq
\text{dynamical-system structural change}.
}
$$

---

# 49. 多尺度 Carrier

真實載體可以同時有：

$$
\theta
$$

快變，

$$
\mathbf a
$$

中速 relaxation，

$$
\lambda
$$

慢速 plasticity。

因此最自然的多尺度模型是：

$$
\boxed{
\dot\theta
=
f_\theta
(
\theta,\mathbf a,\lambda,u
),
}
$$

$$
\boxed{
\dot{\mathbf a}
=
f_a
(
\theta,\mathbf a,\lambda,u
),
}
$$

$$
\boxed{
\dot\lambda
=
\epsilon_\lambda
f_\lambda
(
\theta,\mathbf a,\lambda,u
),
\qquad
\epsilon_\lambda\ll1.
}
$$

這個三層結構將成為 PCPRT Paper 04「可塑性載體」的重要入口。

---

# 50. Phase Memory

若：

$$
\lambda_t
$$

受到歷史輸入改變，

則即使當前：

$$
\theta
$$

相同，

未來 response 也可能不同。

因此：

$$
\boxed{
\text{plastic phase carrier}
}
$$

天然具有 history dependence。

這把 PCPRT 與 GPC-CS Paper 06 接起來。

---

# 51. Phase Response 本身可以漂移

若：

$$
Z
=
Z(\theta;\lambda),
$$

而：

$$
\lambda_t
$$

變化，

那麼：

$$
\boxed{
Z_t(\theta)
}
$$

本身也是 dynamical object。

因此同一 perturbation 在不同 carrier histories 下可以產生不同 phase response。

這是「載體會改變自己如何接收未來輸入」的最小物理形式。

---

# 52. 可反證性

本文的 physical-phase bridge 可被下列結果削弱。

## 52.1 無穩定振盪結構

若某 carrier 根本沒有 stable periodic / oscillatory structure，

 $P_0$ physical oscillator phase 不適用。

## 52.2 Phase fiber defect 長期很大

若：

$$
\Omega_\Theta
$$

在 relevant regime 始終大，

phase-only GPC physical mapping 不成立。

## 52.3 沒有可辨識 amplitude modes

若 phase-amplitude augmentation 仍不能有效預測 dynamics，

需要更高維 effective state。

## 52.4 Strong coupling 使 oscillator identity 消失

若 coupling 後已無法合理辨認個別 oscillator orbit，

individual-phase reduction 必須被 collective description 取代。

## 52.5 GPC generalized phase 不 factor through physical phase

那麼它只能保留為高層 relational variable。

---

# 53. 本文的九個主命題

## 命題 A：Physical phase 必須從 dynamical system 結構定義

$$
\boxed{
\Theta:
\mathcal B(\gamma)
\rightarrow
S^1.
}
$$

不是任意角度 label。

## 命題 B：標準 phase reduction 是弱擾動有效理論

其 validity 依賴 orbit proximity 與 transverse relaxation。

## 命題 C：Phase-only closure 有 intrinsic fiber criterion

$$
\boxed{
\Omega_\Theta=0
}
$$

是 exact memoryless phase closure 的必要充分條件。

## 命題 D：Phase-fiber diameter 給出 phase-only model 的 unavoidable error floor

$$
\boxed{
e_{\mathrm{phase}}
\ge
\frac12
\Omega_\Theta.
}
$$

## 命題 E：Amplitude relaxation 慢或 strong perturbation 時 phase-amplitude state 更自然

$$
\boxed{
q=(\theta,\mathbf a).
}
$$

## 命題 F：Strong coupling 可以改變 periodic orbit 本身

因此：

$$
\boxed{
\text{interaction}
\neq
\text{phase shift only}.
}
$$

## 命題 G：Carrier deformation 包含 orbit、frequency、isochrons、PRC 與 transverse spectrum 的變化

$$
\boxed{
\mathcal D_\lambda
=
(
\gamma_\lambda,
\omega_\lambda,
\Theta_\lambda,
Z_\lambda,
\Lambda_\lambda
).
}
$$

## 命題 H：Physical phase 與 GPC generalized phase 之間需要 factorization + dynamical consistency

不能靠名稱相同就認定同一物理量。

## 命題 I：Phase、amplitude、carrier parameters 應被視為不同時間尺度的 state components

這提供神經可塑性與 adaptive carrier 的後續物理接口。

---

# 54. 系列下一步

PCPRT Paper 03 將進入：

$$
\boxed{
\text{跨載體轉導的能量、耗散與資訊流}.
}
$$

核心將研究：

1. interaction current 如何攜帶 energy / matter / charge / information；
2. stochastic thermodynamics 中 subsystem entropy balance 與 information flow；
3. Landauer principle 正確與不正確的使用邊界；
4. signal fidelity 與 energetic cost 是否存在一般 tradeoff；
5. 為什麼 information flow 不能被粗暴等同 energy flow；
6. GPC 的 $T,D,O$ 如何在 physical current level 實現。

---

# 55. 結論

本文完成了 PCPRT 第一個真正的「phase physics」定位。

如果 physical carrier 是 stable limit-cycle oscillator，

它可以具有：

$$
\boxed{
\Theta(z)
}
$$

這種真正 dynamical phase。

經 weak perturbation reduction：

$$
\boxed{
\dot\theta
=
\omega
+
\epsilon Z(\theta)\cdot p
+
O(\epsilon^2).
}
$$

但真正重要的是：

$$
\boxed{
\text{same phase}
\neq
\text{same physical state}.
}
$$

因此 phase-only description 是否閉合，必須檢查整個 isochron fiber。

本文用：

$$
\boxed{
\Omega_\Theta(\theta,u)
}
$$

量化同一 phase 下 unresolved amplitude states 對未來 phase velocity 的差異，

並得到：

$$
\boxed{
e_{\mathrm{phase}}^{\min}
\ge
\frac12\Omega_\Theta.
}
$$

這使「phase 不夠」不再只是模糊直覺。

當 phase-only 不夠時，

下一層不是放棄 phase，

而是：

$$
\boxed{
(\theta,\mathbf a).
}
$$

當 interaction 進一步改變：

$$
\gamma,
\omega,
\Theta,
Z,
\Lambda,
$$

我們進入：

$$
\boxed{
\text{carrier deformation regime}.
}
$$

於是物理交流的層級可以正式寫成：

$$
\boxed{
\text{phase shift}
\rightarrow
\text{phase-amplitude change}
\rightarrow
\text{carrier deformation}.
}
$$

這條鏈正是 GPC-CS 中「交流會改變載體」第一次得到真正 dynamical-systems 物理實現。

而對 generalized GPC phase，本文留下最重要的限制：

$$
\boxed{
\text{same word "phase"}
\not\Rightarrow
\text{same physical object}.
}
$$

只有在：

$$
\boxed{
\Theta
=
\varphi\circ\Pi
}
$$

並且 dynamics 也相容時，

高層 GPC phase 才能合法地說是 physical phase 的 effective realization。

這是 PCPRT 後續所有物理—生物—認知跨尺度工作的 phase 語義地基。

---

# 參考文獻

1. Kuramoto, Y. (1975). Self-entrainment of a population of coupled non-linear oscillators. In *International Symposium on Mathematical Problems in Theoretical Physics*, Lecture Notes in Physics 39, 420–422. Springer.
2. Kurebayashi, W., Shirasaka, S., & Nakao, H. (2013). Phase Reduction Method for Strongly Perturbed Limit Cycle Oscillators. *Physical Review Letters*, 111, 214101. DOI: 10.1103/PhysRevLett.111.214101.
3. Teramae, J.-N., Nakao, H., & Ermentrout, G. B. (2009). Stochastic Phase Reduction for a General Class of Noisy Limit Cycle Oscillators. *Physical Review Letters*, 102, 194102. DOI: 10.1103/PhysRevLett.102.194102.
4. Wilson, D., & Moehlis, J. (2016). Isostable reduction of periodic orbits. *Physical Review E*, 94, 052213. DOI: 10.1103/PhysRevE.94.052213.
5. Shirasaka, S., Kurebayashi, W., & Nakao, H. (2017). Phase reduction theory for hybrid nonlinear oscillators. *Physical Review E*, 95, 012212. DOI: 10.1103/PhysRevE.95.012212.
6. León, I., & Pazó, D. (2019). Phase reduction beyond the first order: The case of the mean-field complex Ginzburg-Landau equation. *Physical Review E*, 100, 012211. DOI: 10.1103/PhysRevE.100.012211.
7. León, I., & Pazó, D. (2020). Quasi phase reduction of all-to-all strongly coupled lambda-omega oscillators near incoherent states. *Physical Review E*, 102, 042203. DOI: 10.1103/PhysRevE.102.042203.
8. Wilson, D. (2022). An Adaptive Phase-Amplitude Reduction Framework without O(epsilon) Constraints on Inputs. *SIAM Journal on Applied Dynamical Systems*, 21(1), 204–230. DOI: 10.1137/21M1391791.
9. Kurebayashi, W., Yamamoto, T., Shirasaka, S., & Nakao, H. (2022). Phase reduction of strongly coupled limit-cycle oscillators. *Physical Review Research*, 4, 043176. DOI: 10.1103/PhysRevResearch.4.043176.
10. Wilson, D., & Sun, K. (2024). Reduced Order Characterization of Nonlinear Oscillations Using an Adaptive Phase-Amplitude Coordinate Framework. *SIAM Journal on Applied Dynamical Systems*, 23(1), 470–504. DOI: 10.1137/23M1551699.
11. *Strong coupling yields abrupt synchronization transitions in coupled oscillators*. *Physical Review Research*, 6, 033328 (2024). DOI: 10.1103/PhysRevResearch.6.033328.
12. Setoyama, W., & Hasegawa, Y. (2024). Lie Algebraic Quantum Phase Reduction. *Physical Review Letters*, 132, 093602. DOI: 10.1103/PhysRevLett.132.093602.

---

# 系列狀態

**Series:** Phase-Carrier Physical Realization Theory  
**Paper:** 02  
**Version:** v1.0  
**Canonical source encoding:** UTF-8  
**Canonical mathematics delimiters:** ` $...$ ` and `$$...$$` only  
**Operational synchronization/control details:** Excluded  
**Depends on:** PCPRT Paper 01; GPC-CS Papers 02, 04, 05, 06, 09, 10  
**Next:** Paper 03 — 跨載體轉導的能量、耗散與資訊流
