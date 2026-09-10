# 類全域 AI 世界—計算—觀察統合系列（Paper 07）
## 物理層：從 Machine Projection 到 Physical Projection
### The Physical Layer: From Machine Projection to Physical Projection

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 07 / 12  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** PPOE × PPOS × CPC 2.0 × Physical AI × In-Sensor Computing × Metasurface Optics × Wearable Haptics × Machine-Native Carriers × Closed-Loop Calibration × Cyber-Physical Governance  
**前篇：** Paper 06《投影層：AI 如何自行選擇 Computational Way of Seeing》  
**狀態：** WCO Physical Realization Constitution／工程母規格；不宣稱已完成通用物理投影硬體，也不宣稱任何感官或物理通道可以無損傳達任意資訊

---

## 摘要

Paper 06 已建立 Global Projection State：

$$
\mathfrak P_t^G
$$

以及 Cognitive Projection Compiler 2.0：

$$
\mathsf{CPC}_2.
$$

這使類全域 AI 可以決定：

- 應該把 observation content 投影成什麼 representation；
- 應使用什麼 carrier；
- 哪些 task invariants 必須保留；
- 哪些 projection debt 仍存在；
- 何時應生成新的 carrier requirement。

然而，數學或機器層已選好的 projection：

$$
P^\ast
$$

仍然不是實際物理世界中的光、聲、力、振動、電、熱、機械位移或其他可被 receptor 接收的物理場。

因此：

$$
\boxed{
\text{Machine Projection}
\neq
\text{Physical Projection Execution}.
}
$$

本文承接 Physical Projection–Observation Engineering（PPOE）與 Physical Projection–Observation Stack（PPOS），把它們提升為 WCO 的正式 **Physical Realization Layer**。

其核心不是：

$$
P^\ast
\rightarrow
\text{render}.
$$

而是：

$$
\boxed{
P^\ast
\rightarrow
u
\rightarrow
\Phi
\rightarrow
\widehat P
\rightarrow
e
\rightarrow
\text{recalibration}.
}
$$

本文定義 **WCO Physical Realization State（PRS）**：

$$
\boxed{
\mathsf{PRS}_t
=
\left\langle
\mathsf{PPOS}_t,
\mathfrak C_t^{phys},
\mathfrak M_t^{mat},
\mathfrak F_t^{field},
\mathfrak H_t^{rec},
\Theta_t^{cal},
\mathfrak D_t^{phys},
\mathfrak A_t^{safe},
\mathfrak H_t^{phys},
\mathfrak C_t^{cert}
\right\rangle.
}
$$

其中：

- $\mathsf{PPOS}_t$：physical projection–observation stack；
- $\mathfrak C_t^{phys}$：physical carrier / device family；
- $\mathfrak M_t^{mat}$：material / transducer family；
- $\mathfrak F_t^{field}$：physical-field family；
- $\mathfrak H_t^{rec}$：biological / machine receptor models；
- $\Theta_t^{cal}$：calibration state；
- $\mathfrak D_t^{phys}$：physical projection / observation debt；
- $\mathfrak A_t^{safe}$：safety / authority state；
- $\mathfrak H_t^{phys}$：physical execution history；
- $\mathfrak C_t^{cert}$：physical realization certificates。

在 projection direction，本文定義：

$$
\boxed{
\mathsf{PhysCompile}
:
(
P^\ast,
QCap,
c,
o,
\rho,
\Gamma
)
\rightarrow
(
u_{cand},
\mathsf{SafeReq},
\mathsf{CalReq},
\mathsf{Audit}
).
}
$$

候選控制訊號：

$$
u_{cand}
$$

不能直接進 actuator，而必須經：

$$
\boxed{
u_{cand}
\xrightarrow{\mathsf{Safety}}
u_{safe}
\xrightarrow{\mathsf{Authority}}
u_{auth}.
}
$$

因此：

$$
\boxed{
\text{Semantic Validity}
\neq
\text{Physical Safety}
\neq
\text{Actuation Authority}.
}
$$

真正物理投影為：

$$
\boxed{
P^\ast
\xrightarrow{\mathcal C_{phys}}
u_{auth}
\xrightarrow{\mathcal A_\theta}
\Phi'
\xrightarrow{\mathcal H_o}
\widehat P.
}
$$

其中：

- $\mathcal C_{phys}$：physical signal compiler；
- $u_{auth}$：已授權控制訊號；
- $\mathcal A_\theta$：由 material/device parameters $\theta$ 定義的 actuator / transducer；
- $\Phi'$：真實產生的 physical field；
- $\mathcal H_o$：observer / receptor transfer；
- $\widehat P$：實際 percept / machine-received state。

因此 physical projection 是 inverse design / control problem：

$$
\boxed{
u^\ast
=
\operatorname*{arg\,min}_{u\in\mathcal U_{safe}}
\mathcal L
\left(
P^\ast,
\mathcal H_o
(
\mathcal A_\theta(u)
)
\right).
}
$$

若 device/material 本身可設計：

$$
\boxed{
(u^\ast,\theta^\ast)
=
\operatorname*{arg\,min}_{u,\theta}
\mathcal L
\left(
P^\ast,
\mathcal H_o
(
\mathcal A_\theta(u)
)
\right)
}
$$

subject to：

$$
\theta\in\Theta_{fabricable},
\qquad
u\in\mathcal U_{safe}.
$$

本文同時保留 observation direction：

$$
\boxed{
\mathcal R
\xrightarrow{\mathcal S}
\Phi
\xrightarrow{\mathcal T_\theta}
a
\xrightarrow{\mathcal Q}
d
\xrightarrow{\mathcal E}
z
\xrightarrow{\mathcal F}
W_t.
}
$$

這表示 sensor 不是透明地「讀取現實」，而是 channel-bounded physical coupling。sensor physics 本身已經決定 bandwidth、sensitivity、noise、saturation、nonlinearity、cross-talk 與 drift，因此：

$$
\boxed{
\text{Sensor Physics}
=
\text{Part of Observation Semantics}.
}
$$

本文特別保留 PPOE 的非對偶性：

$$
\boxed{
\mathcal T
\neq
\mathcal A^{-1}.
}
$$

camera 不需要是 display 的逆元；microphone 不需要是 loudspeaker 的逆元；human tactile receptor 也不需要是 haptic actuator 的逆元。

因此：

$$
\boxed{
\text{Observation Channel}
\neq
\text{Projection Channel}^{-1}.
}
$$

本文並把 PPOE 原有三重 calibration 擴成 **四重 Calibration**：

$$
\boxed{
\Theta^{cal}
=
\Theta_{device}
+
\Theta_{material}
+
\Theta_{observer}
+
\Theta_{environment}.
}
$$

原因是同一 device、material、observer，在不同 ambient light、temperature、skin hydration、posture、fatigue、background noise 或 electromagnetic environment 下，都可能得到不同 realized projection。

Physical projection 因而不是 one-shot compilation：

$$
\boxed{
\text{Physical Projection}
=
\text{Continuous Closed-Loop Control}.
}
$$

本文定義 physical error：

$$
\boxed{
e_t
=
d(
P^\ast,
\widehat P_t
).
}
$$

並允許：

$$
u_{t+1}
=
\mathcal U_{device}(u_t,e_t),
$$

$$
\theta_{t+1}
=
\mathcal U_{material}(\theta_t,e_t),
$$

$$
\eta_{o,t+1}
=
\mathcal U_{observer}(\eta_{o,t},e_t),
$$

$$
\xi_{env,t+1}
=
\mathcal U_{environment}(\xi_{env,t},e_t).
$$

本文進一步把 Physical Projection Debt 擴張為：

$$
\boxed{
\mathbf D_{phys}
=
(
D_{model},
D_{compile},
D_{device},
D_{material},
D_{field},
D_{receptor},
D_{environment},
D_{calibration},
D_{latency},
D_{safety},
D_{provenance}
).
}
$$

任何 physical carrier 都只有自己的 reachable projection set：

$$
\boxed{
\mathcal P_{phys}(c,o,\xi)
=
\left\{
\mathcal H_{o,\xi}
(
\mathcal A_{\theta,\xi}(u)
):
u\in\mathcal U_{safe}
\right\}.
}
$$

若：

$$
P^\ast
\notin
\mathcal P_{phys},
$$

正確行為不是強迫 hardware「畫出來」，而是：

$$
\boxed{
\text{Reproject}
\quad
\text{or}
\quad
\text{Change Carrier}
\quad
\text{or}
\quad
\text{Declare Physically Unreachable}.
}
$$

因此 CPC 2.0 與 PPOS 必須雙向耦合：

$$
\boxed{
\mathsf{CPC}_2
\leftrightarrow
\mathsf{PPOS}.
}
$$

本文最後將 PPOE 的 Cognitive Material 概念嵌入 WCO，但保留嚴格語義：如果某 material/device local substrate 同時承擔 sensing、transduction、event encoding、limited computation 與 response，則它可以是 projection–observation runtime 的一部分；這不表示材料具有主觀意識。

本文的最終命題為：

$$
\boxed{
\text{A physical projection is not a picture generator.}
}
$$

而是：

$$
\boxed{
\text{a governed closed-loop transduction system
that compiles qualified machine representations
into physically realizable,
observer-decodable,
safe and auditable fields.}
}
$$

**關鍵詞：** Physical Projection、PPOE、PPOS、Physical Signal Compiler、Transduction、In-Sensor Computing、Metasurface、Haptics、Electrotactile、Calibration、Physical Debt、Cognitive Material、Cyber-Physical AI

---

# 0. Paper 06 留下的 Physical Carrier Requirement

Paper 06 可以產生：

$$
CarrierRequirement.
$$

但：

$$
\boxed{
CarrierRequirement
\neq
PhysicalCarrierAvailable.
}
$$

Paper 07 處理兩者之間的工程落差。

---

# 1. Machine Projection 不等 Physical Execution

Machine projection 可以是：

$$
P^\ast
\in
\text{memory / graph / tensor / symbolic state}.
$$

physical projection 則必須產生：

$$
\Phi'.
$$

---

# 2. 物理系統沒有「抽象映射」按鈕

$$
\Pi:
M\rightarrow P
$$

在 hardware 中必須經過：

- memory；
- electronics；
- DAC / PWM / event control；
- transducer；
- material；
- physical field；
- receptor。

---

# 3. Projection Direction

$$
\boxed{
P^\ast
\rightarrow
u
\rightarrow
\Phi'
\rightarrow
\widehat P.
}
$$

---

# 4. Observation Direction

$$
\boxed{
\mathcal R
\rightarrow
\Phi
\rightarrow
a
\rightarrow
d
\rightarrow
z
\rightarrow
W.
}
$$

---

# 5. 兩個方向不能強迫成對偶

$$
\boxed{
Observation
\neq
Projection^{-1}.
}
$$

---

# 6. Physical Field Family

$$
\mathfrak F^{field}
=
\{
\Phi_{EM},
\Phi_{acoustic},
\Phi_{mechanical},
\Phi_{thermal},
\Phi_{chemical},
\Phi_{magnetic},
\ldots
\}.
$$

---

# 7. Sensor 首先選擇 Coupling Channel

$$
\mathcal S_c:
\mathcal R
\rightarrow
\Phi_c.
$$

---

# 8. 所以 Sensor 並沒有「觀察完整世界」

$$
\boxed{
\text{Physical Observation}
=
\text{Channel-Bounded Coupling}.
}
$$

---

# 9. Transduction

$$
\mathcal T_\theta:
\Phi
\rightarrow
a.
$$

---

# 10. Material Parameters

$$
\theta
$$

可以包含 composition、geometry、thickness、microstructure、temperature、bias、polarization response、mechanical constraints。

---

# 11. Sensor Physics 是 Observation Semantics

因為 material/device 已決定：

- sensitivity；
- bandwidth；
- noise；
- saturation；
- nonlinear response；
- hysteresis；
- cross-talk。

---

# 12. Sensor Debt

$$
\boxed{
\mathbf D_{sensor}
=
(
D_{band},
D_{noise},
D_{sat},
D_{nonlinear},
D_{drift},
D_{cross},
D_{sampling}
).
}
$$

---

# 13. Quantization 不是 Neutral Step

$$
\mathcal Q:
a
\rightarrow
d.
$$

可以是：

- ADC；
- threshold；
- eventization；
- spike encoding；
- compression。

---

# 14. Frame 與 Event 是不同 Observation Contract

Frame：

$$
I(x,y,t_k).
$$

Event：

$$
e_i
=
(x_i,y_i,t_i,p_i).
$$

---

# 15. AI-Native Sensing

$$
\boxed{
\text{Physical Input}
\rightarrow
\text{AI-Optimized Representation}.
}
$$

不必先生成 human-friendly image。

---

# 16. In-Sensor Computing

sensor frontend 可直接執行：

- filtering；
- temporal integration；
- feature extraction；
- event encoding；
- convolution-like operation。

---

# 17. Sensor–Algorithm Co-Design

$$
\boxed{
\text{Sensor Representation}
\leftrightarrow
\text{AI Architecture}.
}
$$

---

# 18. AI Observation Stack

$$
\boxed{
\mathcal O_{AI}^{phys}
=
\mathcal F
\circ
\mathcal E
\circ
\mathcal Q
\circ
\mathcal T
\circ
\mathcal S.
}
$$

---

# 19. Physical Input Layer 也要 Provenance

$$
W_t
\neq
z_t
\neq
d_t
\neq
a_t
\neq
\Phi_t.
$$

---

# 20. Physical Signal Compiler

$$
\boxed{
\mathcal C_{phys}
:
P^\ast
\rightarrow
u.
}
$$

---

# 21. $u$ 是 Device-Executable Control State

可以是：

- voltage；
- current；
- phase；
- amplitude；
- frequency；
- actuator displacement；
- pulse sequence；
- MEMS state；
- pneumatic pressure；
- optical control state。

---

# 22. Candidate Physical Signal

$$
u_{cand}.
$$

---

# 23. Candidate 不等 Authorized Signal

$$
\boxed{
u_{cand}
\neq
u_{auth}.
}
$$

---

# 24. Safety Gate

$$
Safe(u,\theta,o,\xi)=1.
$$

---

# 25. Authority Gate

$$
Authorize(u,o,\Gamma)=1.
$$

---

# 26. Physical Signal Path

$$
\boxed{
u_{cand}
\rightarrow
u_{safe}
\rightarrow
u_{auth}
\rightarrow
\mathcal A_\theta
\rightarrow
\Phi'.
}
$$

---

# 27. Semantic Correct 不等 Physical Safe

$$
\boxed{
SemanticCorrectness
\neq
PhysicalSafety.
}
$$

---

# 28. Verified 不等 Authorized

$$
\boxed{
VerifiedProjection
\neq
AuthorizedActuation.
}
$$

---

# 29. Physical Realization 不等 Epistemic Upgrade

投影真的亮出來：

$$
\boxed{
PhysicallyRealized
\not\Rightarrow
MoreTrue.
}
$$

---

# 30. Actuator / Transducer

$$
\mathcal A_\theta:
u
\rightarrow
\Phi'.
$$

---

# 31. Optical Carrier

輸出實際是：

$$
E(x,y,z,\lambda,t),
$$

而不是 image matrix。

---

# 32. Acoustic Carrier

$$
u
\rightarrow
p(x,t).
$$

---

# 33. Haptic Carrier

可控制：

- vibration；
- pressure；
- displacement；
- thermal；
- pneumatic；
- electrotactile patterns。

---

# 34. Machine-Native Physical Carrier

machine receptor 也可直接接收：

- electrical event；
- optical signal；
- networked sensor packet；
- encoded pulse；
- machine-readable field state。

---

# 35. Physical Projection 是 Inverse Problem

$$
\boxed{
u^\ast
=
\arg\min_{u\in\mathcal U_{safe}}
\mathcal L
(
P^\ast,
\mathcal H_o(\mathcal A_\theta(u))
).
}
$$

---

# 36. Material Co-Design

$$
\boxed{
(u^\ast,\theta^\ast)
=
\arg\min_{u,\theta}
\mathcal L
(
P^\ast,
\mathcal H_o(\mathcal A_\theta(u))
).
}
$$

---

# 37. Fabricability Constraint

$$
\theta
\in
\Theta_{fabricable}.
$$

---

# 38. Safety Constraint

$$
u
\in
\mathcal U_{safe}.
$$

---

# 39. 多解是正常的

可能存在：

$$
\mathcal U^\ast
=
\{
u:
\mathcal L(P^\ast,\widehat P(u))
\le
\varepsilon
\}.
$$

---

# 40. 多解後再優化

$$
u^\ast
=
\arg\min_{u\in\mathcal U^\ast}
(
Energy(u)
+
\lambda Risk(u)
+
\mu Cost(u)
).
$$

---

# 41. Material 直接進 Projection Operator

metasurface、waveguide、piezoelectric、soft actuator、electrode geometry 等都會改變：

$$
\mathcal A_\theta.
$$

---

# 42. Carrier 不是 Passive Container

$$
\boxed{
Carrier
\neq
PassiveContainer.
}
$$

---

# 43. Dynamic Carrier

$$
c_t
\neq
c_{t+1}.
$$

例如 reconfigurable array、tunable optics、adaptive haptics。

---

# 44. Material Memory

若：

$$
\Phi_t
=
F(u_t,h_{t-1}),
$$

則 carrier 本身具有 history dependence。

---

# 45. Material History 必須進 Runtime State

不能每次假設 memoryless transfer。

---

# 46. Human Receptor 不是透明 Decoder

$$
\mathcal H_o:
\Phi'
\rightarrow
\widehat P.
$$

---

# 47. Observer Variance

同一 field：

$$
\Phi'
$$

可有：

$$
\mathcal H_{o_1}(\Phi')
\neq
\mathcal H_{o_2}(\Phi').
$$

---

# 48. Observer Model 可以包含

- eye geometry；
- hearing threshold；
- skin mechanics；
- sensory acuity；
- adaptation；
- prior learning；
- attention。

---

# 49. Environment 也改變 Transfer Function

$$
\mathcal H_{o,\xi}.
$$

---

# 50. Environment State

$$
\xi
=
(
AmbientLight,
Temperature,
Noise,
Humidity,
Posture,
Fatigue,
SkinState,
EMContext,
\ldots
).
$$

---

# 51. 四重 Calibration

$$
\boxed{
Calibration
=
Device
+
Material
+
Observer
+
Environment.
}
$$

---

# 52. Device Calibration

更新：

$$
u_{k+1}
=
\mathcal U_{device}(u_k,e_k).
$$

---

# 53. Material Calibration

$$
\theta_{k+1}
=
\mathcal U_{material}(\theta_k,e_k).
$$

---

# 54. Observer Calibration

$$
\eta_{o,k+1}
=
\mathcal U_{observer}(\eta_{o,k},e_k).
$$

---

# 55. Environment Calibration

$$
\xi_{k+1}
=
\mathcal U_{environment}(\xi_k,e_k).
$$

---

# 56. Desired Projection 不等 Realized Projection

$$
\boxed{
P^\ast
\neq
\widehat P
}
$$

通常是正常狀態。

---

# 57. Feedback Error

$$
\boxed{
e
=
d(P^\ast,\widehat P).
}
$$

---

# 58. Continuous Closed Loop

$$
\boxed{
PhysicalProjection
=
ContinuousClosedLoopControl.
}
$$

---

# 59. PPOS 2.0

本文將 PPOS 升級為：

$$
\boxed{
\mathsf{PPOS}_2
=
(L_0,\ldots,L_{11}).
}
$$

---

# 60. L0 — Qualified Projection Input

$$
L_0
=
(P^\ast,QCap).
$$

---

# 61. L1 — Observer / Task / Risk

$$
L_1
=
(o,\tau,b,\rho).
$$

---

# 62. L2 — Physical Capability Resolver

$$
L_2
=
Cap(c).
$$

---

# 63. L3 — Physical Signal Compiler

$$
L_3
=
\mathcal C_{phys}.
$$

---

# 64. L4 — Safety / Authority Gate

$$
L_4
=
(\mathsf{Safe},\mathsf{Authorize}).
$$

---

# 65. L5 — Transducer / Actuator Material

$$
L_5
=
\mathcal A_\theta.
$$

---

# 66. L6 — Physical Field

$$
L_6
=
\Phi'.
$$

---

# 67. L7 — Environment

$$
L_7
=
\xi.
$$

---

# 68. L8 — Biological / Machine Receptor

$$
L_8
=
\mathcal H_{o,\xi}.
$$

---

# 69. L9 — Realized Percept

$$
L_9
=
\widehat P.
$$

---

# 70. L10 — Verification / Error

$$
L_{10}
=
(e,\mathsf{PhysCert}).
$$

---

# 71. L11 — Feedback / Recalibration

$$
L_{11}
=
\mathcal U.
$$

---

# 72. PPOS 2.0 Full Chain

$$
\boxed{
(P^\ast,QCap)
\rightarrow
Cap(c)
\rightarrow
\mathcal C_{phys}
\rightarrow
u_{cand}
\rightarrow
u_{auth}
\rightarrow
\mathcal A_\theta
\rightarrow
\Phi'
\rightarrow
\mathcal H_{o,\xi}
\rightarrow
\widehat P
\rightarrow
e
\rightarrow
\mathcal U.
}
$$

---

# 73. Physical Capability Descriptor

$$
\boxed{
Cap(c)
=
(
Range,
Resolution,
Latency,
Bandwidth,
Energy,
Safety,
Calibration,
EnvironmentSensitivity,
Persistence,
Debt
).
}
$$

---

# 74. Reachable Projection Set

$$
\boxed{
\mathcal P_{phys}(c,o,\xi)
=
\{
\mathcal H_{o,\xi}
(
\mathcal A_{\theta,\xi}(u)
):
u\in\mathcal U_{safe}
\}.
}
$$

---

# 75. Physically Unreachable Projection

若：

$$
P^\ast
\notin
\mathcal P_{phys},
$$

不得強迫 compile。

---

# 76. 合法回應

$$
\boxed{
Reproject
\;|\;
ChangeCarrier
\;|\;
ReduceTarget
\;|\;
PhysicallyUnreachable.
}
$$

---

# 77. CPC 2.0 與 PPOS 2.0 雙向

$$
\boxed{
CPC_2
\leftrightarrow
PPOS_2.
}
$$

---

# 78. Projection Planning 是 Cyber-Physical Planning

$$
\boxed{
ProjectionPlanning
=
RepresentationPlanning
+
PhysicalCapabilityPlanning.
}
$$

---

# 79. Multi-Carrier Physical Projection

同一 qualified content 可分配：

$$
I
=
I_v
\cup
I_a
\cup
I_h
\cup
I_m.
$$

---

# 80. Visual / Audio / Haptic 不必重複全部資訊

每個 channel 可以負責最適 subset。

---

# 81. Cross-Modal Routing

$$
c_i^\ast
=
\arg\max_c
Q(x_i,c,o,\tau,\xi).
$$

---

# 82. Temporal Pattern 可能適合 Audio

不是所有資料都應 visualized。

---

# 83. Urgent Warning 可能適合 Haptic

因為視覺 attention 可能已被其他 task 佔用。

---

# 84. Precise Symbolic Value 可能適合 Text

carrier choice 是 task-relative。

---

# 85. AI-to-AI 不必 Humanize

$$
\boxed{
AI
\rightarrow
AI
}
$$

可以 machine-native。

---

# 86. Humanization 是 Optional Interface

$$
P_H
=
\Pi_{AI\rightarrow H}(P_{AI}).
$$

---

# 87. Machine Receptor 不需模仿人類

$$
\mathcal H_{machine}
$$

可以直接對 machine code / event stream 有定義。

---

# 88. Physical Projection Debt

$$
\boxed{
\mathbf D_{phys}
=
(
D_{model},
D_{compile},
D_{device},
D_{material},
D_{field},
D_{receptor},
D_{environment},
D_{calibration},
D_{latency},
D_{safety},
D_{provenance}
).
}
$$

---

# 89. Latency Debt

若：

$$
T_{sense}
+
T_{infer}
+
T_{compile}
+
T_{actuate}
+
T_{feedback}
>
T_{max},
$$

projection 即使正確也可能 stale。

---

# 90. Energy Constraint

$$
E
\le
E_{budget}.
$$

wearable / mobile system 尤其重要。

---

# 91. Bandwidth Constraint

$$
B_{carrier}
$$

限制 physical information throughput。

---

# 92. Material Drift

$$
\theta(t+\Delta t)
\neq
\theta(t).
$$

---

# 93. Manufacturing Variance

同設計：

$$
\theta_1
\neq
\theta_2.
$$

---

# 94. Observer Variance

$$
o_1
\neq
o_2.
$$

---

# 95. Environment Variance

$$
\xi_1
\neq
\xi_2.
$$

---

# 96. Robust Physical Design

可以優化：

$$
\mathbb E_{\delta\theta,\delta o,\delta\xi}
[
\mathcal L
].
$$

---

# 97. Frozen / Calibratable / Adaptive Parameters

$$
\theta_{frozen},
\quad
\theta_{calibratable},
\quad
\theta_{adaptive}.
$$

---

# 98. 不假設所有 Hardware 都能 Online Adapt

這是 physical realism 的基本要求。

---

# 99. Physical Realization Certificate

$$
\boxed{
PhysCert
=
\left\langle
ProjectionId,
QCap,
Carrier,
Device,
Material,
Control,
Safety,
Authority,
Calibration,
Environment,
MeasuredOutput,
Debt,
Timestamp,
Provenance
\right\rangle.
}
$$

---

# 100. Physical History

$$
H_t^{phys}
$$

保存：

- control signal；
- device version；
- material state；
- calibration；
- environment；
- measured field；
- observer response；
- fault；
- safety event。

---

# 101. Physical History 不能只保留 Final Image

因為相同 percept 可以由不同 stimulus 產生。

---

# 102. 多對一 Percept

可能：

$$
\Phi_1
\neq
\Phi_2
$$

但：

$$
\mathcal H_o(\Phi_1)
\approx
\mathcal H_o(\Phi_2).
$$

---

# 103. 所以 Inverse Synthesis 可以多解

這與非對偶性一致。

---

# 104. Observation Transduction 也可能多對一

$$
\mathcal T(\Phi_1)
=
\mathcal T(\Phi_2).
$$

---

# 105. Sensor Observation 不可唯一重建 Reality

$$
\boxed{
SensorOutput
\neq
CompleteRealityState.
}
$$

---

# 106. Cognitive Material

本文保留長期工程概念：

$$
\boxed{
Material
=
Sense
+
Encode
+
Compute
+
Respond
}
$$

作為可能的局部 projection–observation substrate。

---

# 107. Cognitive Material 不等 Conscious Material

$$
\boxed{
CognitiveMaterial
\neq
ConsciousMaterial.
}
$$

---

# 108. Material-Level Computation

若材料元件承擔：

$$
\mathcal S
+
\mathcal T
+
\mathcal Q
+
\mathcal E
+
\mathcal A,
$$

它已是 runtime participant。

---

# 109. In-Sensor Computing 的意義

它把：

$$
Sensor
+
Encode
+
PartialCompute
$$

往物理前端融合。

---

# 110. Metasurface / Waveguide 的意義

它們顯示 material geometry 可以直接決定 optical projection transfer。

---

# 111. Wearable Haptics 的意義

flexible、skin-conforming material 直接限制可用 spatial resolution、amplitude、frequency、energy 與 comfort。

---

# 112. Electrotactile 的意義

machine variable 可編碼成 learned tactile symbols。

但需要：

- observer calibration；
- safety；
- confusion measurement；
- retention study。

---

# 113. Physical Realization 不應偷偷變成 Qualification Laundering

一個 simulation projection 即使透過高品質 XR 顯示：

$$
\boxed{
SIM
\neq
REAL.
}
$$

---

# 114. Presence 不等 Reality Status

$$
\boxed{
Presence
\neq
Reality.
}
$$

---

# 115. Higher Fidelity 不等 Higher Epistemic Status

$$
\boxed{
PhysicalFidelity
\neq
EpistemicQualification.
}
$$

---

# 116. Safety 也不等 Truth

$$
\boxed{
Safe
\neq
True.
}
$$

---

# 117. Truth 也不等 Safe

$$
\boxed{
True
\neq
SafeToActuate.
}
$$

---

# 118. WCO Physical Realization State

$$
\boxed{
\mathsf{PRS}_t
=
\left\langle
\mathsf{PPOS}_t,
\mathfrak C_t^{phys},
\mathfrak M_t^{mat},
\mathfrak F_t^{field},
\mathfrak H_t^{rec},
\Theta_t^{cal},
\mathfrak D_t^{phys},
\mathfrak A_t^{safe},
\mathfrak H_t^{phys},
\mathfrak C_t^{cert}
\right\rangle.
}
$$

---

# 119. WCO 六層主鏈

至此：

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}
\rightarrow
\mathfrak P_t^G
\rightarrow
\mathsf{PRS}_t.
}
$$

---

# 120. 但 Physical Layer 也會反向更新 World

實際 sensor / feedback：

$$
\widehat P
\rightarrow
E_{real}
\rightarrow
W_{t+1}.
$$

---

# 121. 因此 Physical Layer 是 Reality Re-entry Interface

$$
\boxed{
\text{Physical Layer}
=
\text{projection exit}
+
\text{observation re-entry}.
}
$$

---

# 122. WCO Physical Loop

$$
\boxed{
W_t
\rightarrow
P^\ast
\rightarrow
\Phi'
\rightarrow
\widehat P
\rightarrow
E_{real}
\rightarrow
W_{t+1}.
}
$$

---

# 123. MVP：不需要新材料

第一代可以使用：

- RGB / depth camera；
- microphone；
- IMU；
- GPU/NPU；
- scene graph；
- CPC 2.0；
- 2D display；
- AR headset；
- vibrotactile band。

---

# 124. MVP Canonical World

$$
W_t
=
G_{scene}.
$$

---

# 125. MVP Projection Routing

precise textual state：

$$
\rightarrow
2D.
$$

spatial hazard：

$$
\rightarrow
AR.
$$

urgent alert：

$$
\rightarrow
\text{haptic}.
$$

AI-native state：

$$
\rightarrow
\text{machine graph}.
$$

---

# 126. MVP 不是 Multimedia Demo

核心是：

$$
\boxed{
\text{one qualified canonical world}
\rightarrow
\text{task-routed physical projections}.
}
$$

---

# 127. MVP Safety Fence

所有 physical output：

$$
u_{cand}
$$

都必須經：

$$
Safety
+
Authority.
$$

---

# 128. MVP Calibration

至少做：

- device；
- observer；
- environment baseline。

---

# 129. MVP Feedback

量測：

$$
P^\ast
$$

與：

$$
\widehat P.
$$

---

# 130. Experiment 1 — Open Loop vs Closed Loop

比較 physical projection error。

---

# 131. Experiment 2 — Observer-Specific Calibration

global mapping vs personalized mapping。

---

# 132. Experiment 3 — Environment Robustness

ambient condition 改變時測 projection degradation。

---

# 133. Experiment 4 — AI-Native Sensor

RGB frame、event stream、in-sensor feature、mixed sensing 比較：

- accuracy；
- latency；
- energy；
- bandwidth。

---

# 134. Experiment 5 — Visual / Haptic Routing

比較：

- visual-only；
- haptic-only；
- hybrid；
- CPC adaptive。

---

# 135. Experiment 6 — Learned Haptic Code

測：

- learnability；
- retention；
- confusion；
- channel capacity。

---

# 136. Experiment 7 — Physical Debt Injection

依序注入：

- sensor noise；
- quantization；
- device drift；
- material variation；
- environment change；
- observer variation。

---

# 137. Experiment 8 — Unreachable Projection

故意要求超出 device capability 的 target。

runtime 必須 reproject 或 refuse。

---

# 138. Experiment 9 — Safety / Authority Separation

建立：

- semantically correct but unsafe；
- safe but unauthorized；
- authorized but stale；

三種 case。

---

# 139. Experiment 10 — Carrier Change

同一 information：

$$
\text{visual}
\rightarrow
\text{audio}
\rightarrow
\text{haptic}
$$

比較 task-relative performance。

---

# 140. 可反駁性

本文會被削弱，如果：

1. closed-loop calibration 對 physical projection error 沒有穩定改善；
2. observer/environment calibration 在代表性 human-interface tasks 中沒有實際價值；
3. carrier capability planning 不降低 impossible / unsafe projection requests；
4. physical debt vector 無法預測 realized projection failure；
5. multi-carrier routing 比固定 carrier 沒有 task-relative優勢；
6. in-sensor / AI-native sensing 在控制成本後沒有任何收益；
7. physical history / provenance 對 fault diagnosis 無價值；
8. simpler renderer-centric architecture 在代表性 cyber-physical tasks 上完全等效。

---

# 141. 外部研究接口

近年的 in-sensor computing 研究已把 sensing、encoding 與部分 computation 往 sensor 前端融合，並提出更適合 AI 處理的 sensing representation。

metasurface / waveguide AR 研究則顯示 optical material geometry、inverse design、wave propagation 與 output uniformity本身就是 projection pipeline 的一部分。

wearable haptics 的近年綜述顯示柔性、可變形與貼膚材料正在成為 tactile interface 的核心工程限制與能力來源。

electrotactile machine-to-human communication 研究也說明人機資訊通道不必只模擬傳統視覺／聽覺，而可以把 machine state 編碼成可學習 tactile patterns。

本文不宣稱取代 optics、materials science、sensor design、haptics、control 或 HCI。WCO Physical Layer 的新增問題是：

> 如何把這些異質 physical technologies 放入同一個 qualification-aware、projection-aware、authority-bounded、closed-loop AI runtime？

---

# 142. 本文不主張什麼

本文不主張：

1. physical projection 可以無損傳達任意資訊；
2. sensor 可以直接讀取完整 reality；
3. camera 與 display 必須互逆；
4. observation material 與 projection material 必須相同；
5. haptic 是 visual 的降級替代；
6. electrotactile 可無限制編碼任意 machine state；
7. higher physical fidelity 等於 higher truth；
8. XR presence 等於 reality；
9. semantic correctness 等於 physical safety；
10. verification 等於 actuation authority；
11. AI 可自行繞過 hardware safety gate；
12. all device parameters 可 online adapt；
13. material memory 可忽略；
14. cognitive material 具有 consciousness；
15. AI-native sensor 一定優於 RGB sensor；
16. metasurface 一定是未來唯一 display technology；
17. haptics 一定適合所有 users / tasks；
18. observer personalization 可以改寫 evidence semantics；
19. PPOS 2.0 已完成 production implementation；
20. WCO Physical Layer 已完成 universal physical interface。

---

# 143. 核心非同一性

$$
\boxed{
MachineProjection
\neq
PhysicalProjectionExecution.
}
$$

$$
\boxed{
SensorOutput
\neq
Reality.
}
$$

$$
\boxed{
ObservationChannel
\neq
ProjectionChannel^{-1}.
}
$$

$$
\boxed{
SemanticValidity
\neq
PhysicalSafety
\neq
ActuationAuthority.
}
$$

$$
\boxed{
DesiredProjection
\neq
RealizedProjection.
}
$$

$$
\boxed{
Carrier
\neq
PassiveContainer.
}
$$

$$
\boxed{
PhysicalFidelity
\neq
EpistemicQualification.
}
$$

$$
\boxed{
Presence
\neq
Reality.
}
$$

$$
\boxed{
CognitiveMaterial
\neq
ConsciousMaterial.
}
$$

---

# 144. 核心母式一：Physical Compiler

$$
\boxed{
\mathsf{PhysCompile}
:
(
P^\ast,
QCap,
c,
o,
\rho,
\Gamma
)
\rightarrow
(
u_{cand},
SafeReq,
CalReq,
Audit
).
}
$$

---

# 145. 核心母式二：Physical Projection

$$
\boxed{
P^\ast
\xrightarrow{\mathcal C_{phys}}
u_{auth}
\xrightarrow{\mathcal A_\theta}
\Phi'
\xrightarrow{\mathcal H_{o,\xi}}
\widehat P.
}
$$

---

# 146. 核心母式三：Physical Observation

$$
\boxed{
\mathcal R
\xrightarrow{\mathcal S}
\Phi
\xrightarrow{\mathcal T_\theta}
a
\xrightarrow{\mathcal Q}
d
\xrightarrow{\mathcal E}
z
\xrightarrow{\mathcal F}
W_t.
}
$$

---

# 147. 核心母式四：四重 Calibration

$$
\boxed{
Calibration
=
Device
+
Material
+
Observer
+
Environment.
}
$$

---

# 148. 核心母式五：Physical Debt

$$
\boxed{
\mathbf D_{phys}
=
(
D_{model},
D_{compile},
D_{device},
D_{material},
D_{field},
D_{receptor},
D_{environment},
D_{calibration},
D_{latency},
D_{safety},
D_{provenance}
).
}
$$

---

# 149. 核心母式六：PRS

$$
\boxed{
\mathsf{PRS}_t
=
\left\langle
\mathsf{PPOS}_t,
\mathfrak C_t^{phys},
\mathfrak M_t^{mat},
\mathfrak F_t^{field},
\mathfrak H_t^{rec},
\Theta_t^{cal},
\mathfrak D_t^{phys},
\mathfrak A_t^{safe},
\mathfrak H_t^{phys},
\mathfrak C_t^{cert}
\right\rangle.
}
$$

---

# 150. 結論：類全域 AI 最終必須碰到真實物理限制

在純軟體架構裡，AI 很容易產生：

$$
P^\ast.
$$

它可以說：

> 用 AR。

> 用 haptic。

> 用新的 carrier。

但只要真正進入 physical world，就立刻遇到：

- bandwidth；
- energy；
- material；
- latency；
- calibration；
- safety；
- receptor variability；
- environment；
- manufacturing；
- irreversible physical effects。

因此：

$$
\boxed{
\text{Representation Feasibility}
\neq
\text{Physical Feasibility}.
}
$$

這也是 Paper 07 的真正位置。

WCO 前六篇逐步回答：

> 世界是什麼？

> 怎麼算？

> 怎麼觀察？

> 有什麼資格？

> 怎麼投影？

Paper 07 加入：

> **這個投影在物理上真的做得到嗎？**

如果做得到：

> **什麼 signal、device、material、field、receptor 與 calibration 才能把它可靠地做出來？**

如果做不到：

> **系統能否知道自己做不到，而不是用 software fantasy 強迫 physical world 配合？**

因此本文的核心不是讓 AI「控制更多物理裝置」。

相反地，它要求每一個 physical projection 都必須經過：

$$
\boxed{
Qualification
+
PhysicalFeasibility
+
Safety
+
Authority
+
Calibration
+
Feedback.
}
$$

類全域 AI 的 physical interface 因而應是一個：

$$
\boxed{
\text{closed-loop,
carrier-aware,
material-aware,
observer-aware,
environment-aware,
authority-bounded
projection–observation system}.
}
$$

最終：

$$
\boxed{
\text{A physical projection is not a picture generator.}
}
$$

而是：

$$
\boxed{
\text{a governed closed-loop transduction system
that compiles qualified machine representations
into physically realizable,
observer-decodable,
safe and auditable fields.}
}
$$

至此 WCO 的主鏈形成：

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}
\rightarrow
\mathfrak P_t^G
\rightarrow
\mathsf{PRS}_t.
}
$$

下一篇：

# Paper 08
## 記憶層：從資訊海到可重建世界與世界族

將把：

- long-term memory；
- provenance；
- world reconstruction；
- branch memory；
- failure memory；
- OAM；
- SEDB；
- Global Knowledge Convergence；

正式接進 WCO。

---

# 151. 下一篇接口

Paper 08 將處理：

- memory != context；
- memory object identity；
- provenance；
- world-state reconstruction；
- branch memory；
- observation memory；
- computation history；
- certificate memory；
- failure memory；
- multi-representation memory；
- OAM；
- semantic / graph / operator memory；
- global knowledge convergence；
- memory-to-world compilation；
- world-family regeneration；
- stale / invalidated memory；
- forgetting vs pruning；
- dynamic fixed-point continuity。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K × Aletheia，《PPOE Paper 01：物理投影—觀察工程》，2026。
2. Neo.K × Aletheia，《載體投影與內視系列 B08：超越人類眼睛》，2026。
3. Neo.K × Aletheia，《WCO Paper 06：投影層》，2026。
4. Neo.K × Aletheia，《PNCW Series》，2026。
5. Neo.K × Aletheia，《Global Observer Series C》，2026。
6. Neo.K × Aletheia，《投影計算論》，2026。
7. Neo.K × Aletheia，《WCO Paper 01–05》，2026。

## External Research Interfaces

8. Kim, D., Kwon, J. I., Kim, Y., et al. (2026). *AI-native robotic vision systems enabled by in-sensor computing*. npj Unconventional Computing, 3, 2.
9. Tian, Z., Zhu, X., Surman, P. A., et al. (2025). *An achromatic metasurface waveguide for augmented reality displays*. Light: Science & Applications, 14, 94.
10. Chen, Z., Huang, Y., Zhang, B., et al. (2026). *Deformable materials and structures in wearable haptic interfaces*. Nature Reviews Materials, 11, 266–285.
11. Parsnejad, S., Brascamp, J. W., Pelled, G., & Mason, A. J. (2026). *A review of electrotactile stimulation for machine-to-human communication*. IEEE Transactions on Biomedical Engineering.
12. Fleck, J. J., et al. (2025). *Wearable multi-sensory haptic devices*. Nature Reviews Bioengineering.
13. Gopakumar, M., et al. (2024). *Full-colour 3D holographic augmented-reality displays with metasurface waveguides*. Nature.
14. Jang, C., et al. (2024). *Waveguide holography for 3D augmented reality glasses*. Nature Communications.

---

**Paper 07 狀態：COMPLETE v0.1**  
**下一篇：Paper 08 — 記憶層：從資訊海到可重建世界與世界族**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
