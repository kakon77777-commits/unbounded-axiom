# 物理投影—觀察工程（Paper 01）
## 從數學投影算子到感測、材料、物理場與閉環校正
### Physical Projection–Observation Engineering: From Mathematical Projection Operators to Sensing, Materials, Physical Fields, and Closed-Loop Calibration

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列定位：** 載體投影與內視系列之工程延伸  
**篇次：** Paper 01  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** 計算機架構 × AI × 感測器 × 物理學 × 材料學 × 光學 × 聲學 × 觸覺介面 × HCI × 控制  
**狀態：** 工程框架與研究議程；不宣稱本文已完成通用物理投影裝置，也不宣稱任一感官通道可無損傳達任意資訊

---

## 摘要

數學上的投影通常可以簡潔地寫成：

$$
P=\Pi(M),
$$

其中 $M$ 是模型或高維狀態， $P$ 是投影後的可操作表示。然而，當這個框架被要求真正進入計算機、機器人、XR、人機介面與物理世界時， $\Pi$ 不能只停留在抽象映射。AI 若要「觀察」現實，必須先透過感測材料把光、聲、壓力、溫度、磁場、化學濃度或機械應變轉導為可計算訊號；AI 若要把內部模型「投影」給人類或其他機器，也必須把數學表示轉成控制訊號，再透過光學、聲學、機械、電刺激或其他執行器產生真實物理場，最後由生物或機器 receptor 解碼。

本文提出 **Physical Projection–Observation Engineering（PPOE，物理投影—觀察工程）**，把抽象投影算子擴張為一個完整的跨層工程鏈。觀察方向寫為：

$$
\mathcal{R}
\xrightarrow{\mathcal{S}}
\Phi
\xrightarrow{\mathcal{T}}
a
\xrightarrow{\mathcal{Q}}
d
\xrightarrow{\mathcal{E}}
z
\xrightarrow{\mathcal{F}}
M,
$$

其中 $\mathcal{R}$ 為外部世界， $\Phi$ 為物理場， $\mathcal{S}$ 為選擇性耦合， $\mathcal{T}$ 為材料／裝置轉導， $a$ 為類比訊號， $\mathcal{Q}$ 為量化、事件化或 spike encoding， $d$ 為數位或事件訊號， $\mathcal{E}$ 為編碼， $z$ 為 AI-native representation， $\mathcal{F}$ 為融合與模型更新。

投影方向則寫為：

$$
M
\xrightarrow{\mathsf{CPC}}
P^\ast
\xrightarrow{\mathcal{C}_{phys}}
u
\xrightarrow{\mathcal{A}_{\theta}}
\Phi'
\xrightarrow{\mathcal{H}_o}
\widehat{P},
$$

其中 $\mathsf{CPC}$ 為 Cognitive Projection Compiler， $P^\ast$ 是目標投影， $\mathcal{C}_{phys}$ 是物理訊號編譯器， $u$ 是裝置控制訊號， $\mathcal{A}_{\theta}$ 是由材料與裝置參數 $\theta$ 所決定的 actuator/transducer， $\Phi'$ 是實際產生的光、聲、力、熱、電或其他物理場， $\mathcal{H}_o$ 是觀察者或 receptor 的感知轉換， $\widehat P$ 是最後實際取得的 percept／observation。

因此，真正的投影工程不是 rendering 問題，而是一個 inverse physics 問題：

$$
u^\ast
=
\operatorname*{arg\,min}_{u}
\mathcal{L}
\left(
P^\ast,
\mathcal{H}_o
\left(
\mathcal{A}_{\theta}(u)
\right)
\right).
$$

若材料或裝置本身也可被設計，則：

$$
(u^\ast,\theta^\ast)
=
\operatorname*{arg\,min}_{u,\theta}
\mathcal{L}
\left(
P^\ast,
\mathcal{H}_o
\left(
\mathcal{A}_{\theta}(u)
\right)
\right).
$$

本文進一步提出 **Physical Projection–Observation Stack（PPOS）**，將 canonical model、task/observer model、CPC、representation、physical signal compiler、transducer material、physical field、receptor、percept 與 feedback calibration 分層。該框架允許視覺、聲音、觸覺、XR、電刺激、機器原生事件流與未來未知載體共享同一架構，而不要求所有資訊先被轉成人類 2D/3D 影像。

本文亦強調材料學不是被動末端。現代 in-sensor computing、neuromorphic sensing、metasurface optics、柔性壓電材料、electrotactile interface 與 wearable haptics 已經顯示，感測、編碼、計算與輸出正在逐步向材料與裝置前端融合。未來的投影系統可能不再具有清楚分離的「sensor → processor → display」，而可能形成：

$$
\boxed{
\text{material}
=
\text{sense}
+
\text{encode}
+
\text{compute}
+
\text{respond}.
}
$$

本文最後提出可立即實作的 MVP：以相機／深度感測、AI scene graph、CPC、2D/AR display 與 vibrotactile wearable 組成多載體投影閉環；再以第二階段硬體共設計進入 holographic/metasurface display、neuromorphic sensor、electrotactile/haptic array 與 observer-specific calibration。

核心命題是：

$$
\boxed{
\text{A physical projection operator is not a picture generator.}
}
$$

$$
\boxed{
\text{It is a closed-loop transduction system that compiles model structure into physically realizable, observer-decodable fields.}
}
$$

**關鍵詞：** physical projection、observation operator、transduction、inverse design、in-sensor computing、metasurface、haptics、electrotactile、neuromorphic sensing、Cognitive Projection Compiler、closed-loop calibration

---

# 0. 研究問題

前一系列已經回答：

> 一個 AI 或人類應該用哪一種 projection 理解某個世界模型？

但還剩下一個更底層的工程問題：

> 數學上選好的 projection，如何真正穿過計算機、電路、材料與物理場，最後變成一個人或機器能取得的 observation？

因此本文不再只研究：

$$
P=\Pi(M).
$$

而研究：

$$
\boxed{
M
\rightarrow
P
\rightarrow
u
\rightarrow
\Phi
\rightarrow
\widehat P.
}
$$

---

# 1. 數學投影與物理投影不是同一件事

數學 projection 可以是：

$$
\Pi:\mathcal{M}\rightarrow\mathcal{P}.
$$

但物理系統不能直接執行抽象集合映射。它必須經過記憶體、數位電路、DAC／ADC、驅動器、感測材料、光學元件、機械元件、電極與生物 receptor。

因此：

$$
\boxed{
\text{Mathematical Projection}
\neq
\text{Physical Projection Execution}.
}
$$

---

# 2. 觀察不是直接讀世界

AI 常被描述成：

> camera 看見世界。

更精確地：

$$
\mathcal{R}
\rightarrow
\Phi
\rightarrow
a
\rightarrow
d
\rightarrow
z
\rightarrow
M.
$$

世界先與 sensor 發生物理耦合，再逐層轉成可計算狀態。

---

# 3. Physical Field 是第一個真正被 Sensor 接觸的對象

令：

$$
\Phi
\in
\{
\Phi_{\mathrm{EM}},
\Phi_{\mathrm{acoustic}},
\Phi_{\mathrm{thermal}},
\Phi_{\mathrm{mechanical}},
\Phi_{\mathrm{chemical}},
\Phi_{\mathrm{magnetic}},
\ldots
\}.
$$

不同 sensor 其實選擇不同世界切片。

---

# 4. Observation Operator 首先是 Coupling Selection

定義：

$$
\mathcal{S}_{c}
:
\mathcal{R}
\rightarrow
\Phi_c.
$$

因此 AI 的 observation 並不是對完整世界的取樣，而是：

$$
\boxed{
\text{channel-bounded physical coupling}.
}
$$

---

# 5. 材料的第一個角色：Transduction

定義：

$$
\mathcal{T}_{\theta}
:
\Phi
\rightarrow
a.
$$

 $\theta$ 可以表示 composition、geometry、doping、thickness、microstructure、temperature、bias、polarization response 與 mechanical boundary condition。

---

# 6. 典型轉導

光：

$$
\text{photon flux}
\rightarrow
\text{photo-generated charge}.
$$

聲音：

$$
\text{pressure}
\rightarrow
\text{membrane displacement}
\rightarrow
V.
$$

壓力／應變：

$$
\epsilon
\rightarrow
\Delta R
$$

或：

$$
\epsilon
\rightarrow
Q_{\mathrm{piezo}}.
$$

磁場：

$$
B
\rightarrow
V_{\mathrm{Hall}}.
$$

---

# 7. Sensor 本身就是一個物理投影器

Sensor 不只是「收資料」。因為：

$$
\Phi
\rightarrow
a
$$

已經決定 sensitivity、resolution、bandwidth、saturation、noise 與 nonlinear response。

所以：

$$
\boxed{
\text{sensor physics}
=
\text{part of projection semantics}.
}
$$

---

# 8. Observation Debt 從材料層就開始

$$
\mathbf{D}_{sensor}
=
\left(
D_{\mathrm{band}},
D_{\mathrm{noise}},
D_{\mathrm{sat}},
D_{\mathrm{nonlinear}},
D_{\mathrm{drift}},
D_{\mathrm{cross}}
\right).
$$

---

# 9. Quantization 不是中性步驟

$$
\mathcal{Q}:a\rightarrow d.
$$

可包括 ADC、threshold、eventization、spike encoding 與 compression。

---

# 10. Event Camera 的概念意義

傳統 frame-based vision：

$$
I(x,y,t_k).
$$

事件式表示：

$$
e_i=(x_i,y_i,t_i,p_i).
$$

兩者不是同一資料格式的不同包裝，而是不同 observation contract。

---

# 11. AI-Native Sensing

AI-native sensor 的目標不一定是產生「人類好看的 image」，而是：

$$
\boxed{
\text{physical input}
\rightarrow
\text{AI-optimized representation}.
}
$$

---

# 12. In-Sensor Computing

現代研究已讓 sensor 前端直接執行 feature enhancement、spike encoding、temporal integration、filtering 與 convolution-like operations。

因此：

$$
\boxed{\text{Sensor}+\text{Encode}+\text{PartialCompute}}
$$

正在融合。

---

# 13. Sensor–Algorithm Co-Design

如果 sensor 輸出：

$$
z_{\mathrm{event}},
$$

後端卻只接受：

$$
z_{\mathrm{RGB}},
$$

仍會增加轉換成本。

因此：

$$
\boxed{
\text{sensor representation}
\leftrightarrow
\text{AI architecture}
}
$$

需要 co-design。

---

# 14. AI Observation Stack

$$
\boxed{
\mathcal{O}_{AI}
=
\mathcal{F}
\circ
\mathcal{E}
\circ
\mathcal{Q}
\circ
\mathcal{T}
\circ
\mathcal{S}.
}
$$

---

# 15. Fusion

多 sensor：

$$
z_1,\ldots,z_n
$$

經：

$$
M_t
=
\mathcal{F}(z_1,\ldots,z_n,M_{t-1}).
$$

這才進入 world model。

---

# 16. World Model 不是 Sensor Data

$$
\boxed{
M_t
\neq
z_t
\neq
d_t
\neq
a_t
\neq
\Phi_t.
}
$$

每一層都需要 provenance。

---

# 17. 反方向：AI 如何把模型投影出去？

數學表示：

$$
P^\ast
=
\mathsf{CPC}(M,o,c,\tau,b,\rho).
$$

但 $P^\ast$ 仍然只是 target representation。

---

# 18. Physical Signal Compiler

定義：

$$
\boxed{
\mathcal{C}_{phys}
:
P^\ast
\rightarrow
u.
}
$$

 $u$ 是裝置可執行控制量。

---

# 19. 視覺載體的控制量

可以是 pixel voltage、LED current、laser intensity、SLM phase、DMD state、MEMS angle 或 tunable optical state。

---

# 20. 聲學載體

$$
u
=
\{A(t),f(t),\phi(t),\ldots\}.
$$

經 transducer：

$$
u
\rightarrow
p(x,t).
$$

---

# 21. Haptic 載體

 $u$ 可以控制 vibration amplitude、frequency、pressure、displacement、temperature、electrotactile pulse 或 pneumatic pressure。

---

# 22. Actuator／Transducer

定義：

$$
\mathcal{A}_{\theta}
:
u
\rightarrow
\Phi'.
$$

 $\Phi'$ 是真正進入物理世界的輸出場。

---

# 23. 視覺 Projection 最終是光場問題

對 near-eye display：

$$
u
\rightarrow
E(x,y,z,\lambda,t).
$$

真正到人眼的不是 image matrix，而是電磁場的空間／頻譜結構。

---

# 24. Holographic Projection

若希望建立目標 wavefront：

$$
E^\ast,
$$

需要求控制相位：

$$
\phi^\ast(x,y).
$$

這已經是一個 inverse problem。

---

# 25. Metasurface

meta-atom geometry：

$$
\theta_{\mathrm{meta}}
$$

可以控制 phase、amplitude、polarization 與 diffraction efficiency。

因此材料與微結構本身就進入 projection operator。

---

# 26. Inverse-Designed AR 是早期完整示範

2024–2025 的研究已經把 metasurface、waveguide physics、AI holography、inverse design 與 camera feedback 放進同一 near-eye display pipeline。

這說明：

$$
\boxed{
\text{projection}
=
\text{computation}
+
\text{physics}
+
\text{materials}
+
\text{calibration}.
}
$$

---

# 27. Desired Projection 不等於 Realized Projection

$$
P^\ast
\neq
\widehat P
$$

通常是正常狀態。

---

# 28. Inverse Physical Projection Problem

$$
\boxed{
u^\ast
=
\operatorname*{arg\,min}_u
\mathcal{L}
\left(
P^\ast,
\mathcal{H}_o
(
\mathcal{A}_\theta(u)
)
\right).
}
$$

---

# 29. Material Co-Design

$$
\boxed{
(u^\ast,\theta^\ast)
=
\operatorname*{arg\,min}_{u,\theta}
\mathcal{L}
\left(
P^\ast,
\mathcal{H}_o
(
\mathcal{A}_\theta(u)
)
\right).
}
$$

---

# 30. AI × Physics × Materials 的真正接口

AI 可以執行 inverse design、control optimization、calibration、compensation、fault adaptation 與 observer personalization。

---

# 31. Human Receptor 也不是透明讀取器

$$
\mathcal{H}_o:
\Phi'
\rightarrow
\widehat P.
$$

 $o$ 取決於 eye geometry、hearing threshold、skin mechanics、neural adaptation、prior learning 與 attention。

---

# 32. 同一物理場，不同觀察者可有不同 percept

$$
\Phi'_1=\Phi'_2
$$

但：

$$
\mathcal{H}_{o_1}(\Phi')
\neq
\mathcal{H}_{o_2}(\Phi').
$$

---

# 33. Observer Calibration

$$
\boxed{
\text{Projection Calibration}
=
\text{device calibration}
+
\text{observer calibration}.
}
$$

---

# 34. 視覺校準

可包含 eye position、interpupillary distance、aberration、focus 與 color response。

---

# 35. Haptic 校準

可包含 body location、skin impedance、pressure threshold、sensory acuity 與 adaptation rate。

---

# 36. Electrotactile 是重要的新型輸出通道

electrotactile stimulation 可透過皮膚電極建立 machine-to-human code。

因此：

$$
\boxed{
\text{machine variable}
\rightarrow
\text{learned tactile symbol}.
}
$$

---

# 37. 它不必只模擬自然觸摸

可以直接編碼 direction、warning、confidence、speed、state class 與 navigation instruction。

---

# 38. Haptic Projection

$$
\Pi_{\mathrm{data}\rightarrow\mathrm{skin}}
:
x
\rightarrow
u_{\mathrm{haptic}}
\rightarrow
\Phi_{\mathrm{skin}}
\rightarrow
\widehat P_H.
$$

---

# 39. Wearable Haptics 的材料族

可包括 electromagnetic、piezoelectric、polymeric、pneumatic、fluidic、thermal 與 electrotactile。

---

# 40. Flexible Materials

wearable interface 要求 conformability、durability、low mass、stretchability、low power 與 stable skin contact。

所以材料學直接決定可用 carrier geometry。

---

# 41. Piezoelectric Materials

感測：

$$
\epsilon
\rightarrow
Q.
$$

致動：

$$
E
\rightarrow
\epsilon.
$$

因此特別適合 sense–actuate integration。

---

# 42. Material Duality 不是必要條件

一種材料可以只 sensing，另一種只 actuation。

因此：

$$
\boxed{
\text{observation material}
\not\equiv
\text{projection material}.
}
$$

---

# 43. Sonification

高維狀態：

$$
x\in\mathbb{R}^n
$$

可以映射到 pitch、timbre、rhythm、volume 與 spatialization。

---

# 44. 聲音不是視覺的降級版

它可能對 temporal pattern、anomaly、rhythm 與 continuous monitoring 更合適。

---

# 45. Multi-Carrier Projection

同一狀態可以同時產生：

$$
P_{\mathrm{visual}},
P_{\mathrm{audio}},
P_{\mathrm{haptic}}.
$$

---

# 46. 多載體不是重複資訊

最佳策略可能是：

$$
I
=
I_v
\cup
I_a
\cup
I_h,
$$

把不同資訊分配到不同通道。

---

# 47. Cross-Modal Allocation

對每個資訊變量 $x_i$：

$$
c_i^\ast
=
\operatorname*{arg\,max}_c
Q(x_i,c,o,\tau).
$$

---

# 48. Physical Projection–Observation Stack

本文正式提出：

$$
\boxed{
\mathsf{PPOS}
=
(L_0,\ldots,L_9).
}
$$

---

# 49. PPOS L0：Canonical World / Model

$$
L_0=M.
$$

---

# 50. PPOS L1：Task & Observer Model

$$
L_1=(o,\tau,b,\rho).
$$

---

# 51. PPOS L2：Cognitive Projection Compiler

$$
L_2=\mathsf{CPC}.
$$

---

# 52. PPOS L3：Target Representation

$$
L_3=P^\ast.
$$

---

# 53. PPOS L4：Physical Signal Compiler

$$
L_4=\mathcal{C}_{phys}.
$$

---

# 54. PPOS L5：Transducer / Actuator Material

$$
L_5=\mathcal{A}_{\theta}.
$$

---

# 55. PPOS L6：Physical Field

$$
L_6=\Phi'.
$$

---

# 56. PPOS L7：Biological / Machine Receptor

$$
L_7=\mathcal{H}_o.
$$

---

# 57. PPOS L8：Percept / Observation

$$
L_8=\widehat P.
$$

---

# 58. PPOS L9：Feedback / Recalibration

$$
L_9=\mathcal{V}+\mathcal{U}.
$$

---

# 59. PPOS 完整鏈

$$
\boxed{
M
\xrightarrow{\mathsf{CPC}}
P^\ast
\xrightarrow{\mathcal{C}_{phys}}
u
\xrightarrow{\mathcal{A}_{\theta}}
\Phi'
\xrightarrow{\mathcal{H}_o}
\widehat P
\xrightarrow{\mathcal{V}}
e
\xrightarrow{\mathcal{U}}
(u',\theta',M').
}
$$

---

# 60. Feedback Error

$$
e
=
d(P^\ast,\widehat P).
$$

---

# 61. Device Calibration Loop

$$
u_{k+1}
=
\mathcal{U}_{device}(u_k,e_k).
$$

---

# 62. Material Calibration

$$
\theta_{k+1}
=
\mathcal{U}_{mat}(\theta_k,e_k).
$$

---

# 63. Observer Calibration

$$
\eta_{o,k+1}
=
\mathcal{U}_{obs}(\eta_{o,k},r_k).
$$

---

# 64. 三重 Calibration

$$
\boxed{
\text{calibration}
=
\text{device}
+
\text{material}
+
\text{observer}.
}
$$

---

# 65. Physical Projection Debt

$$
\mathbf{D}_{phys}
=
\left(
D_{\mathrm{model}},
D_{\mathrm{compile}},
D_{\mathrm{device}},
D_{\mathrm{material}},
D_{\mathrm{field}},
D_{\mathrm{receptor}},
D_{\mathrm{latency}}
\right).
$$

---

# 66. Material Drift

$$
\theta(t+\Delta t)
\neq
\theta(t).
$$

即使 $P^\ast$ 不變， $\widehat P$ 也可能改變。

---

# 67. Manufacturing Variance

同設計：

$$
\theta_1\neq\theta_2.
$$

因此需要 per-device calibration。

---

# 68. Human Variance

同設備：

$$
o_1\neq o_2.
$$

因此需要 per-observer calibration。

---

# 69. Context Variance

同一觀察者在 fatigue、ambient light、skin hydration 等條件下也可能改變。

---

# 70. Projection 不是一次性編譯

$$
\boxed{
\text{physical projection}
=
\text{continuous control problem}.
}
$$

---

# 71. Real-Time Constraint

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
\leq
T_{max}.
$$

---

# 72. Latency Debt

如果：

$$
T>T_{max},
$$

投影可能正確但過時。

---

# 73. Bandwidth Constraint

$$
B_{channel}
$$

限制能投影的資訊量。

---

# 74. Energy Constraint

wearable system 要受：

$$
E_{budget}
$$

限制。

---

# 75. Safety Gate

$$
\operatorname{Actuate}
\iff
\operatorname{Safe}(u,\theta,o,c)=1.
$$

---

# 76. Representation Correct 不代表 Physical Output Safe

$$
\boxed{
\text{semantic correctness}
\neq
\text{physical safety}.
}
$$

---

# 77. Candidate vs Authorized Signal

$$
u_{candidate}
\neq
u_{authorized}.
$$

---

# 78. Machine Receptor

如果 receiver 是另一台機器：

$$
\mathcal{H}_{machine}
$$

不需要模仿 human sensory response。

---

# 79. Humanization 不是必需階段

$$
\boxed{
AI\rightarrow AI
}
$$

可以直接使用 machine-native carrier。

---

# 80. 同一 Model 多 Physical Branch

$$
M
\rightarrow
\begin{cases}
P_H\\
P_{AI}\\
P_{robot}\\
P_{XR}
\end{cases}
$$

---

# 81. Material-Level Computation

未來 sensor、memory、compute 可能在同一器件或局部硬體融合。

---

# 82. Memristive / Neuromorphic Interface

這類元件允許 analog state、memory、event response 與 local computation，因此材料結構可逐步承擔 computational semantics。

---

# 83. 認知材料

本文提出長期工程概念：**Cognitive Material**。

若材料／器件局部同時實現：

$$
\mathcal{S}
+
\mathcal{T}
+
\mathcal{Q}
+
\mathcal{E}
+
\mathcal{A},
$$

則它不再只是 sensor 或 actuator，而是部分 projection–observation runtime。

---

# 84. 認知材料不是「有意識材料」

這裡 cognitive 只表示 information transduction and task-relevant computation，不表示 subjective consciousness。

---

# 85. 最小可行產品：不需要新材料

第一代完全可以使用現成：

- RGB／depth camera；
- microphone；
- IMU；
- GPU/NPU；
- scene graph；
- CPC；
- 2D display；
- AR headset；
- vibrotactile band。

---

# 86. MVP Canonical Model

$$
M
=
G_{scene}.
$$

包含 object、relation、position、hazard、confidence 與 provenance。

---

# 87. MVP Projection Routing

精確文字：

$$
\rightarrow \text{2D}.
$$

空間 hazard：

$$
\rightarrow \text{AR}.
$$

高優先級 warning：

$$
\rightarrow \text{haptic}.
$$

AI detailed reasoning state：

$$
\rightarrow \text{machine-native graph}.
$$

---

# 88. MVP 核心不是多媒體

而是：

$$
\boxed{
\text{one canonical model}
\rightarrow
\text{task-routed heterogeneous projections}.
}
$$

---

# 89. 第二階段：Optical Co-Design

可進入 microLED、SLM、holographic waveguide、metasurface 與 camera-in-loop calibration。

---

# 90. 第二階段：Haptic Co-Design

可進入 piezo array、soft actuator、electrotactile array 與 thermal haptics。

---

# 91. 第二階段：Neuromorphic Sensing

可加入 event camera、in-sensor compute、tactile event sensor 與 spiking encoder。

---

# 92. 第三階段：Material–Algorithm Co-Design

聯合優化：

$$
\theta_{material},
\quad
\theta_{device},
\quad
\theta_{algorithm}.
$$

---

# 93. Hardware–Algorithm Co-Design Objective

$$
\mathcal{J}
=
Q_{task}
-
\lambda_E E
-
\lambda_T T
-
\lambda_D D
-
\lambda_C C.
$$

---

# 94. Material Constraint

$$
\theta
\in
\Theta_{fabricable}.
$$

inverse design 不能產生無法製造的材料幾何。

---

# 95. Robust Design

考慮 fabrication variation：

$$
\delta\theta.
$$

目標可包含：

$$
\mathbb E_{\delta\theta}
[
\mathcal L(\theta^\ast+\delta\theta)
].
$$

---

# 96. Observer-Robust Projection

若：

$$
o\sim p(o),
$$

可優化：

$$
\mathbb E_o[
\mathcal L(P^\ast,\widehat P_o)
].
$$

---

# 97. Frozen／Calibratable／Adaptive Parameters

區分：

$$
\theta_{frozen},
\quad
\theta_{calibratable},
\quad
\theta_{adaptive}.
$$

避免假設所有硬體參數都能 online 更新。

---

# 98. Physical Projection Compiler 的完整輸出

$$
\boxed{
\mathsf{PhysCompile}(P^\ast)
=
(u,Safety,Calibration,Audit).
}
$$

---

# 99. Projection Failure Modes

$$
\mathcal{F}
=
\{
F_{semantic},
F_{hardware},
F_{material},
F_{calibration},
F_{observer},
F_{safety}
\}.
$$

---

# 100. PPOE 核心設計規則

$$
\boxed{
\text{semantic validity}
+
\text{physical realizability}
+
\text{observer decodability}
+
\text{safety}.
}
$$

---

# 101. Reachable Projection Set

$$
\mathcal{P}_{phys}
=
\left\{
\mathcal{H}_o(\mathcal{A}_{\theta}(u)):
u\in\mathcal{U}_{safe}
\right\}.
$$

若：

$$
P^\ast
\notin
\mathcal{P}_{phys},
$$

CPC 就必須換 carrier 或降低 projection target。

---

# 102. CPC 與 PPOS 必須雙向耦合

$$
\boxed{
\mathsf{CPC}
\leftrightarrow
\mathsf{PPOS}.
}
$$

CPC 問：最適表示是什麼？

PPOS 回答：這個載體實際能做到什麼？

---

# 103. Physical Capability Descriptor

$$
\mathsf{Cap}(c)
=
\left(
Range,
Resolution,
Latency,
Bandwidth,
Energy,
Safety,
Calibration,
Debt
\right).
$$

---

# 104. Projection Planning 是 Cyber-Physical Planning

$$
\boxed{
\text{Projection Planning}
=
\text{representation planning}
+
\text{physical capability planning}.
}
$$

---

# 105. Dynamic Carrier

若載體本身可調：

$$
c_t\neq c_{t+1}.
$$

例如 tunable metasurface、reconfigurable haptic array 或 programmable material。

---

# 106. Material Memory

若材料有 history dependence：

$$
\Phi_t
=
F(u_t,h_{t-1}).
$$

則 projection runtime 必須維護 carrier state。

---

# 107. 載體不是靜態容器

$$
\boxed{
\text{carrier}
\neq
\text{passive container}.
}
$$

它可能是動態物理計算參與者。

---

# 108. Observation 與 Projection 不要求對偶

$$
\boxed{
\mathcal{T}
\neq
\mathcal{A}^{-1}.
}
$$

Camera 與 display 本來就不是嚴格逆元。

---

# 109. 多對一 Observation

可能存在：

$$
\mathcal{T}(\Phi_1)
=
\mathcal{T}(\Phi_2).
$$

因此 observation inverse problem 不唯一。

---

# 110. 多對一 Percept

不同 stimulus：

$$
\Phi_1\neq\Phi_2
$$

也可能：

$$
\mathcal{H}_o(\Phi_1)
\approx
\mathcal{H}_o(\Phi_2).
$$

---

# 111. Projection Synthesis 可以有多解

$$
\mathcal{U}^\ast
=
\left\{
u:
\mathcal{L}(P^\ast,\widehat P(u))
\leq\epsilon
\right\}.
$$

---

# 112. 多解後再優化 Energy 與 Safety

$$
u^\ast
=
\operatorname*{arg\,min}_{u\in\mathcal{U}^\ast}
\left(
E(u)
+
\lambda R_{safety}(u)
\right).
$$

---

# 113. 可實驗研究一：Visual–Haptic Routing

同一 navigation task 比較 visual-only、haptic-only、visual+haptic 與 CPC adaptive。

測：

$$
T,
Error,
Load,
MissRate.
$$

---

# 114. 可實驗研究二：Device Closed-Loop Calibration

建立 $P^\ast$，量測 $\widehat P$，迭代更新 $u$，比較 closed-loop 與 open-loop projection error。

---

# 115. 可實驗研究三：Observer-Specific Calibration

比較 global mapping 與 personalized mapping。

---

# 116. 可實驗研究四：AI-Native Sensor

同一 robotic task 比較 RGB frame、event stream、in-sensor feature 與 mixed sensor。

測：

$$
Accuracy,
Latency,
Energy,
Bandwidth.
$$

---

# 117. 可實驗研究五：Projection Debt Across Physical Stack

依序注入 sensor noise、quantization、device drift 與 observer variation，測量：

$$
D_{total}.
$$

---

# 118. 可實驗研究六：Learned Haptic Code

把機器變量映射成 haptic icon，研究 learnability、retention、confusion matrix 與 channel capacity。

---

# 119. 資訊理論接口

如果通道容量：

$$
C_c,
$$

資訊需求：

$$
I_\tau,
$$

需滿足：

$$
I_\tau\leq C_c
$$

或進行壓縮與分流。

---

# 120. 但 Shannon Capacity 不是全部

$$
\boxed{
\text{channel capacity}
\neq
\text{cognitive usability}.
}
$$

還涉及 learning、attention、semantics、fatigue 與 discrimination threshold。

---

# 121. Psychophysics 是 PPOE 的必要工程層

物理 stimulus 與 percept 的 mapping 需要實驗量測，不能只靠裝置規格。

---

# 122. Device Resolution 不等於 Effective Resolution

$$
\boxed{
R_{device}
\neq
R_{effective,o}.
}
$$

---

# 123. Material–Device–Algorithm–Observer Co-Design

$$
\boxed{
\text{material}
\leftrightarrow
\text{device}
\leftrightarrow
\text{algorithm}
\leftrightarrow
\text{observer}.
}
$$

---

# 124. Projection Contract

$$
\mathsf{PContract}
=
\left\langle
Target,
Carrier,
Signal,
Device,
Material,
Observer,
Safety,
Debt,
Calibration,
Validation
\right\rangle.
$$

---

# 125. Physical Provenance

$$
\operatorname{Prov}_{phys}
=
\left(
Model,
Compiler,
Firmware,
Device,
Material,
Calibration,
ObserverProfile,
Time
\right).
$$

---

# 126. Reproducibility

一個物理 projection experiment 至少要能重建：

$$
(M,P^\ast,u,\theta,o,Cal).
$$

---

# 127. 可反駁性

若抽象 projection 不需要材料、裝置與 observer transfer function 就能精確預測實際 percept，本文的物理分層就過度複雜。

若 in-sensor computing 在廣泛任務中沒有 latency／energy／bandwidth 優勢，其適用域就應縮小。

若 observer calibration 對 task performance 無系統影響，個人化層應降級為選配。

若 multi-carrier routing 無法優於固定單一載體，CPC routing 的工程價值應重新評估。

---

# 128. 現有技術接口

## 128.1 AI-Native In-Sensor Vision

2026 的 AI-native robotic vision review 系統整理 synaptic、neuronal 與 hierarchical in-sensor computing，指出 sensor 前端可直接執行 feature enhancement、spike encoding 與 convolution-like operations，降低傳輸與前處理成本。

## 128.2 AI + Metasurface + Holographic AR

2024 年全彩 3D holographic AR 工作把 inverse-designed metasurface gratings、waveguide physics、AI holography 與 camera-feedback calibration 共設計，提供「desired projection → physical device → measured output → learned correction」的實體範例。

## 128.3 Achromatic Metasurface Waveguide

2025 年 metasurface waveguide prototype 使用 inverse-designed metasurface couplers 與 high-index waveguide，在單層結構實現全彩 AR，說明材料幾何與光學 projection quality 可以共同優化。

## 128.4 Wearable Haptics

2025 wearable multi-sensory haptics review 系統整理 vibration、skin stretch、pressure、temperature 與 polymeric、fluidic 等 actuator，並指出人體位置、接觸力學與個體差異會影響 perceptual performance。

## 128.5 Electrotactile Machine-to-Human Communication

2026 review 已明確把 electrotactile stimulation 定位成 machine-to-human communication channel，同時指出 skin dependency、neural adaptation 與一致 encoding framework 仍是限制。

---

# 129. 本文不主張什麼

本文不主張：

1. 所有 AI observation 都應使用 neuromorphic sensor；
2. in-sensor computing 一定優於傳統 camera pipeline；
3. metasurface 是 XR 唯一正確材料；
4. electrotactile 應取代視覺或聽覺；
5. 人類 receptor 可以無損接收任意高維資訊；
6. physical projection 可以取消 representation debt；
7. inverse design 一定有唯一解；
8. observer-specific calibration 等於讀心；
9. cognitive material 具有主觀意識；
10. material–algorithm co-design 意味所有層必須共同訓練；
11. AI 可以無限制直接控制物理刺激；
12. 物理可實現代表語義正確；
13. 語義正確代表物理安全；
14. Paper 01 已完成通用投影硬體；
15. 未來新材料可以取消世界重新驗證的必要性。

---

# 130. 核心命題總結

## 命題 A：Observation 是跨物理與計算的複合算子

$$
\boxed{
\mathcal{O}_{AI}
=
\mathcal{F}
\circ
\mathcal{E}
\circ
\mathcal{Q}
\circ
\mathcal{T}
\circ
\mathcal{S}.
}
$$

## 命題 B：物理 Projection 不是 Rendering

$$
\boxed{
\text{Physical Projection}
\neq
\text{Rendering}.
}
$$

## 命題 C：真正投影是 Inverse Physics Problem

$$
\boxed{
u^\ast
=
\operatorname*{arg\,min}_u
\mathcal{L}
\left(
P^\ast,
\mathcal{H}_o
(
\mathcal{A}_\theta(u)
)
\right).
}
$$

## 命題 D：材料是 Projection Semantics 的一部分

$$
\boxed{
\text{material transfer function}
\subset
\text{projection operator}.
}
$$

## 命題 E：Device 與 Observer 都要 Calibration

$$
\boxed{
\text{Projection Calibration}
=
\text{device}
+
\text{material}
+
\text{observer}.
}
$$

## 命題 F：Sensor、Encode、Compute 可逐步融合

$$
\boxed{
\text{AI-native sensing}
=
\text{sensing with task-oriented representation generation}.
}
$$

## 命題 G：語義、物理、可解碼與安全必須同時成立

$$
\boxed{
\text{semantic validity}
+
\text{physical realizability}
+
\text{observer decodability}
+
\text{safety}.
}
$$

## 命題 H：Observation 與 Projection 不要求對偶

$$
\boxed{
\mathcal{T}
\neq
\mathcal{A}^{-1}.
}
$$

## 命題 I：載體可以成為動態計算參與者

$$
\boxed{
\text{carrier}
\neq
\text{passive container}.
}
$$

---

# 131. 結論：讓數學投影真正穿過物理世界

數學上：

$$
P=\Pi(M)
$$

非常漂亮。

但真正的機器不能靠這一行就讓人「看見」或「感覺到」某個模型。

需要：

$$
\boxed{
\text{model}
\rightarrow
\text{representation}
\rightarrow
\text{control signal}
\rightarrow
\text{material response}
\rightarrow
\text{physical field}
\rightarrow
\text{receptor}
\rightarrow
\text{percept}.
}
$$

反方向也同樣如此：

$$
\boxed{
\text{world}
\rightarrow
\text{physical field}
\rightarrow
\text{sensor material}
\rightarrow
\text{signal}
\rightarrow
\text{encoding}
\rightarrow
\text{AI model}.
}
$$

所以真正的 AI 投影—觀察系統是一個雙向、非必然對偶、閉環校正的 cyber-physical transduction runtime。

其核心不是把一個抽象圖「顯示出來」。而是回答：

> 哪個物理通道可以承載這個結構？

> 哪種材料與裝置可以產生這個通道？

> AI 要控制哪些變量？

> 真實裝置會如何偏離理想模型？

> 觀察者實際能解碼多少？

> 如何量測誤差？

> 如何重新校準？

因此本文最終提出：

$$
\boxed{
\text{Physical Projection}
=
\text{Representation Compilation}
+
\text{Inverse Physics}
+
\text{Material Transduction}
+
\text{Observer Decoding}
+
\text{Closed-Loop Calibration}.
}
$$

而未來真正先進的投影硬體，很可能不再只是 sensor、processor、display 三個互相獨立的盒子，而會逐漸走向：

$$
\boxed{
\text{material}
=
\text{sense}
+
\text{encode}
+
\text{compute}
+
\text{respond}.
}
$$

但即使到了那一步，本文仍保留最重要的邊界：

$$
\boxed{
\text{physically realized projection}
\neq
\text{world itself}.
}
$$

材料與計算可以讓不可直接感知的東西變得可操作；它們不能取消 projection 與 reality 之間仍需被驗證的距離。

---

# 132. Paper 02 接口

下一篇將處理：

# 《模擬世界族執行時：AI 對多重虛擬世界的非對偶、非對稱觀察與控制》

從單一：

$$
W\rightarrow P
$$

進一步轉向：

$$
\boxed{
\mathfrak{W}
=
\{W_0,W_1,\ldots,W_n\}.
}
$$

並研究 world fork、nested simulation、asymmetric observation、asymmetric authority、non-invertible projection、world-family pruning／merge／branch，以及 AI 對多個 actual／simulated／counterfactual world 的並行觀察。

---

# 參考文獻

1. Kim, D., Kwon, J. I., Kim, Y., et al. (2026). AI-native robotic vision systems enabled by in-sensor computing. *npj Unconventional Computing*, 3, 2. DOI: 10.1038/s44335-025-00047-z.
2. Gopakumar, M., Lee, G.-Y., Choi, S., et al. (2024). Full-colour 3D holographic augmented-reality displays with metasurface waveguides. *Nature*, 629, 791–797. DOI: 10.1038/s41586-024-07386-0.
3. Tian, Z., Zhu, X., Surman, P. A., et al. (2025). An achromatic metasurface waveguide for augmented reality displays. *Light: Science & Applications*, 14, 94. DOI: 10.1038/s41377-025-01761-w.
4. Jang, C., Bang, K., Chae, M., et al. (2024). Waveguide holography for 3D augmented reality glasses. *Nature Communications*, 15, 66. DOI: 10.1038/s41467-023-44032-1.
5. Fleck, J. J., Zook, Z. A., Clark, J. P., et al. (2025). Wearable multi-sensory haptic devices. *Nature Reviews Bioengineering*, 3, 288–302. DOI: 10.1038/s44222-025-00274-w.
6. Chen, Z., Huang, Y., Zhang, B., et al. (2026). Deformable materials and structures in wearable haptic interfaces. *Nature Reviews Materials*, 11, 266–285. DOI: 10.1038/s41578-025-00877-0.
7. Parsnejad, S., Brascamp, J. W., Pelled, G., & Mason, A. J. (2026). A review of electrotactile stimulation for machine-to-human communication. *IEEE Transactions on Biomedical Engineering*. DOI: 10.1109/TBME.2026.3661416.
8. Neo.K (2026). 《載體投影與內視系列（B08）：超越人類眼睛——AI、XR 與新型認知載體》.
9. Neo.K (2026). *HDUS Architecture Constitution v0.1*.

---

**Paper 01 狀態：COMPLETE v0.1**  
**下一篇：Paper 02 — 模擬世界族執行時**  
**Canonical source format：** UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。
