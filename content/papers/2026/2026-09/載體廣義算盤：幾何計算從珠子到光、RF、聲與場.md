# 載體廣義算盤：幾何計算從珠子到光、RF、聲與場

**系列：外掛式物理計算機與現場計算設備研究，第 1 篇**  
**英文系列名：External Physical Compute Appliances and Field Computing Systems**  
**英文篇名：Carrier-Generalized Abacus: Geometric Computation from Beads to Light, RF, Sound, and Fields**  
**版本：v0.1**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：2026-08-29**  
**狀態：公開草稿／理論與工程框架**

## 摘要

算盤通常被理解為一種以珠子、桿件與人工作動完成算術的機械計算器。然而，若將珠子、材料與具體尺寸暫時移除，算盤仍保留一個更抽象的計算骨架：一組受幾何與鄰接關係約束的可辨識狀態，在輸入、傳播、累積、閾值、進位與讀出規則下發生狀態轉移。本文將此骨架稱為「載體廣義算盤」（Carrier-Generalized Abacus, CGA），並研究其狀態載體能否由機械珠子推廣到電荷、電壓脈衝、RF 波、聲波、超音波、光脈衝、偏振、相位、波長及其他可控制場模式。

本文不主張任意波動裝置都是算盤，也不主張把珠子換成光便能自動提升通用計算能力。相反地，本文提出一組最低條件：狀態可辨識性、受控傳播、幾何約束、可重複輸入與讀出、重置能力，以及在需要離散進位或條件轉移時可提供足夠的非線性、閾值或閉環回授。只有當新 substrate 對任務結果具有實質因果貢獻時，carrier substitution 才具有計算意義。

在此基礎上，本文提出四階段演化：position coding、mode coding、relation coding 與 dynamical geometry。第一階段以位置或佔據對應數值；第二階段允許時間槽、頻率、波長、偏振或相位等模式在同一幾何通道中多工；第三階段利用波的疊加與干涉，使關係本身成為計算狀態；第四階段則進一步允許耦合矩陣、路由、邊界或拓撲隨時間被重新配置，使計算從「狀態沿固定幾何移動」跨入「狀態與幾何共同演化」。

現有研究已分別證明此方向所需的多個物理片段：Fredkin--Toffoli billiard-ball model 顯示碰撞與路徑可以承載邏輯；metamaterial analog computing 已利用波與空間傳遞函數執行微分、積分與卷積；聲學與超音波 metasurface 系統已被提出用於求解常微分與偏微分方程；2025 年的可程式 RF wave-based analog computing machine 更已實驗展示矩陣運算、矩陣反演、Newton root finding 與 inverse design。這些成果並不等同於本文的 CGA，但共同支持一個保守命題：幾何、邊界、傳播、干涉與可重構耦合本身可以成為實質計算資源。

本文最後提出 CGA 作為 External Physical Compute Appliance 的第一個可觀測祖型。第一代裝置不應追求最高吞吐量，而應優先證明 physical-core non-substitution、雙路驗證、可觀測狀態演化與跨 carrier backend contract。若這些條件成立，算盤便不再只是歷史上的機械計算器，而可被重新理解為一種跨 substrate 的 constrained state-transition geometry。

**關鍵詞：** 載體廣義算盤、幾何計算、物理計算、wave-based analog computing、RF、聲學計算、光子計算、干涉、多工、動態幾何、External Physical Compute Appliance

---

## 1. 問題不是「能不能用雷射做一個算盤」

最直觀的提問是：

> 如果保留算盤的幾何形式，把珠子改成光、雷射脈衝、RF、電荷、聲波、超音波或其他場激發，會發生什麼？

若只從外觀理解，答案可能非常平凡：把每一顆珠子的位置換成一顆 LED、一道光點或一個螢幕動畫即可。

但這種替換沒有改變計算的物理核心。若真正的結果仍由 MCU 或 CPU 先算好，再把答案顯示成「珠子移動」，那麼新 carrier 只是顯示層。

本文研究的是較強的問題：

> 能否保留或抽取算盤的幾何計算關係，讓新的物理 carrier 本身參與狀態傳播、累積、交互作用、閾值與結果生成？

因此要區分：

$$
\text{visual carrier substitution}
$$

與

$$
\text{computational carrier substitution}.
$$

只有後者屬於本文的主題。

---

## 2. 把算盤從材料中抽離

令一個簡化的算盤系統表示為

$$
\mathcal A
=
(V,E,X,U,R,\Theta),
$$

其中：

- $V$：可承載狀態的位置或節點集合；
- $E$：允許狀態傳播或相互影響的關係集合；
- $X$：當前計算狀態；
- $U$：外部輸入與控制操作；
- $R$：讀出映射；
- $\Theta$：進位、借位、閾值、邊界與其他運算規則。

在機械算盤中， $V$ 通常由桿件或槽位的幾何位置給出， $X$ 由珠子的離散位置給出，而 $U$ 則由手指施加。

對第 $i$ 個數位欄，若基數為 $b$，可將邏輯狀態寫成

$$
x_i\in\{0,1,\ldots,b-1\}.
$$

整體數字為

$$
N
=
\sum_{i=0}^{n-1}x_i b^i.
$$

在這個描述中，「珠子」不是數學定義的一部分。珠子只是某一種實現映射：

$$
\mathcal E_{\mathrm{mech}}:
X_L
\rightarrow
X_P,
$$

其中 $X_L$ 是邏輯狀態， $X_P$ 是具體物理狀態。

因此，真正值得保留的不是木頭、金屬或珠子，而是：

$$
\boxed{
\text{受約束的狀態空間}
+
\text{可控制的轉移規則}
+
\text{可讀出的任務映射}
}
$$

這就是本文所稱的 constrained state-transition geometry。

---

## 3. 定義：載體廣義算盤 CGA

令 substrate family 為

$$
\mathfrak M
=
\{
M_{\mathrm{mech}},
M_{\mathrm{electric}},
M_{\mathrm{RF}},
M_{\mathrm{acoustic}},
M_{\mathrm{photonic}},
M_{\mathrm{field}},
\ldots
\}.
$$

對任意 $m\in\mathfrak M$，令物理編碼映射為

$$
\mathcal E_m:X_L\rightarrow X_m,
$$

物理演化為

$$
X_m(t_0)
\xrightarrow{\mathcal D_m(G_m,U_m)}
X_m(t_1),
$$

讀出為

$$
\mathcal R_m:X_m(t_1)\rightarrow Y.
$$

若給定任務 $\tau$，目標計算映射為

$$
F_\tau:X_L\rightarrow Y_\tau,
$$

而某 substrate $m$ 滿足

$$
d_\tau
\left(
\mathcal R_m
\circ
\mathcal D_m
\circ
\mathcal E_m(x),
F_\tau(x)
\right)
\leq
\varepsilon
$$

對指定輸入域成立，則稱 $m$ 在任務 $\tau$ 、誤差容限 $\varepsilon$ 下實現一個 CGA backend。

可記為

$$
\mathrm{CGA}_{\varepsilon}(m,\tau)=1.
$$

此定義不要求不同 substrate 的內部軌跡相同。

也就是：

$$
\Gamma_{m_1}
\neq
\Gamma_{m_2}
$$

但仍可能有

$$
F_\tau(\Gamma_{m_1})
\approx
F_\tau(\Gamma_{m_2}).
$$

這正是前置系列中跨基底功能實現與有效物理等價在計算設備上的具體化。

---

## 4. Carrier substitution 需要哪些最低條件？

不是任何可以「動」的物理量都適合作為計算 carrier。本文提出六個最低工程條件。

### 4.1 狀態可辨識性

需要存在一組編碼狀態

$$
\Sigma_m
=
\{s_0,s_1,\ldots,s_k\}
$$

使讀出器能在容許錯誤率下區分：

$$
P(\hat s=s\mid s)
\geq
1-\delta.
$$

若不同狀態在物理噪聲中無法穩定區分，便不能可靠承載算盤狀態。

### 4.2 受控傳播

carrier 必須能沿指定幾何或耦合關係傳播：

$$
s_i
\xrightarrow{E_{ij}}
s_j.
$$

若訊號無法被限制在可設計路徑中，算盤式的「欄」、「鄰接」與「進位方向」就失去意義。

### 4.3 受控交互作用

若任務需要累積、碰撞、比較或進位，至少部分狀態必須能互相影響：

$$
(s_i,s_j)
\rightarrow
s_k.
$$

完全彼此獨立、永不耦合的 carrier 只能傳輸，不足以單獨形成更複雜計算。

### 4.4 可重複讀出

需要明確的 readout operator：

$$
y=R(X_m).
$$

若結果只能由設計者「看感覺」解讀，就不適合作為科研計算核心。

### 4.5 初始化與重置

至少應存在

$$
\operatorname{Init}(X_m)
$$

與

$$
\operatorname{Reset}(X_m)
$$

使同一算例可以重複執行，並進行誤差統計與校正。

### 4.6 非線性、閾值或閉環替代

對單純線性轉換而言，線性波系統本身已非常有用；但若要做離散進位、條件分支或狀態保持，通常需要某種

$$
\mathcal N(X)
$$

使系統具有非線性、閾值、飽和、鎖存或 feedback。

如果 physical core 本身缺乏這些能力，也可以由 supervisor 與 sensor loop 提供：

$$
X_P
\rightarrow
R
\rightarrow
S
\rightarrow
U
\rightarrow
X_P'.
$$

因此 CGA 不要求「純物理、零數位輔助」，但要求 physical core 仍具有可辨識的實質計算貢獻。

---

## 5. CGA-0：位置編碼

最接近傳統算盤的形式是 position coding。

令一條 rail 上存在可區分位置

$$
P_i
=
\{p_{i,0},p_{i,1},\ldots,p_{i,b-1}\}.
$$

則數位狀態可直接編碼為

$$
x_i=k
\iff
s_i\text{ 位於 }p_{i,k}.
$$

傳統珠子是最直觀的實現，但 carrier 可以被替換。

例如對光脈衝，可將空間位置映射成到達時間：

$$
p_{i,k}
\mapsto
\tau_{i,k}
=
\tau_{i,0}+k\Delta t.
$$

此時原本的 spatial abacus 轉化為 temporal abacus。

同理，對傳輸線上的電壓或 RF pulse，也可以使用 time-of-flight 或 time-bin position 作為邏輯位置。

因此：

$$
\boxed{
\text{logical position}
\neq
\text{literal macroscopic location}
}
$$

位置可以是物理空間，也可以是可排序的時間位置。

---

## 6. 從空間位置到時間位置：算盤的第一個壓縮

傳統算盤需要用實體距離分離狀態。

若每一個位置間距為 $\Delta x$，一條具有 $b$ 個位置的 rail 大約需要

$$
L\sim b\Delta x.
$$

但在 time-bin 編碼中，幾何長度不必隨狀態數線性增加。邏輯位置可被映射為

$$
\{0,1,\ldots,b-1\}
\rightarrow
\{t_0,t_1,\ldots,t_{b-1}\}.
$$

所以第一個重要轉換是：

$$
\boxed{
\text{spatial geometry}
\rightarrow
\text{spatiotemporal geometry}
}
$$

這並不表示物理空間消失。波導、傳輸線、共振腔或聲學通道仍然存在；但一部分原本必須由宏觀空間承擔的離散結構，被時間自由度吸收。

這是 carrier generalization 帶來的第一個真正計算效益。

---

## 7. CGA-1：模式編碼

波與場相較於機械珠子的第二個重要差異，是一條物理通道可以承載多個可區分模式。

令 carrier state 表示為

$$
s
=
(A,\phi,f,\tau,p,\pi),
$$

其中可分別代表：

- $A$：振幅；
- $\phi$：相位；
- $f$：頻率；
- $\tau$：時間槽；
- $p$：空間模式；
- $\pi$：偏振或其他內部模式標記。

在光學系統中， $f$ 也常以波長 $\lambda$ 表示。

若各模式在實際硬體與讀出條件下近似可獨立使用，單一 physical rail 的有效邏輯通道數可粗略寫成

$$
C_{\mathrm{rail}}
\lesssim
N_t N_f N_\phi N_p N_\pi.
$$

這不是無條件容量定理，因為模式間會受到頻寬、SNR、crosstalk、色散、相干時間與 detector bandwidth 限制；它只是表明同一幾何通道不再必然只對應一條邏輯 rail。

因此：

$$
\boxed{
1\ \text{physical rail}
\not\Rightarrow
1\ \text{logical rail}
}
$$

而可能變成多工的 mode space。

---

## 8. 光學與雷射載體

光學 carrier 的吸引力不只是傳播速度。

它同時提供：

$$
A,
\phi,
\lambda,
\tau,
\text{polarization},
\text{spatial mode}
$$

等可控制自由度，並可利用干涉、繞射、傅立葉轉換、濾波與散射直接實現數學映射。

2014 年 Silva 等人提出 metamaterial analog computing，利用設計過的 metamaterial blocks 使入射波在傳播過程中執行空間微分、積分與卷積。後續 spatial optical analog computing 與 meta-optics 研究則進一步發展 Fourier-domain 與 Green's-function 路線。

因此在 CGA 語言中，光學 backend 不必停在「用光點代替珠子」。

它可以逐步變成：

$$
\text{position}
\rightarrow
\text{time-bin}
\rightarrow
\text{wavelength mode}
\rightarrow
\text{phase relation}
\rightarrow
\text{wave transformation}.
$$

但也必須承認光學工程的代價：相位穩定、熱漂移、耦合損失、detector conversion、非線性實作與 memory 都可能使系統複雜度上升。

所以第一代可觀測 CGA 不必選擇最快的 carrier。

---

## 9. RF 載體

RF 的工程位置很有趣。

它仍然是電磁波，因此可以使用：

$$
A,
\phi,
f,
\tau
$$

等波動自由度；同時它又具有成熟的 transmission line、phase shifter、amplifier、mixer、detector、ADC/DAC 與可程式控制生態。

2025 年 Tzarouchis、Edwards 與 Engheta 展示的 programmable wave-based analog computing machine，即使用 RF waveguide architecture 與可調 multiplier modules 建構 direct complex matrix operation，並進一步處理矩陣反演、Newton root finding 與 inverse design。

這對 CGA 有兩個重要啟示。

第一，wave-based computation 不必只存在於不可重構的被動結構中。

可以有

$$
G
=
G(\theta),
$$

而參數 $\theta$ 可由外部控制器改變。

第二，digital supervisor 與 wave core 可以自然共存：

$$
\boxed{
\text{digital configuration}
+
\text{physical wave computation}
}
$$

不構成概念矛盾。

因此 RF 很適合作為 CGA 第一代實驗 backend 的候選之一，尤其適合驗證可重構路由、相位關係與雙路量測，而不必一開始就處理高密度 photonic integration。

---

## 10. 聲波與超音波載體

聲學系統提供另一種重要路徑。

聲波的速度遠低於光速，這使傳播延遲、駐波、共振與路徑差在較大的實驗尺度上更容易量測與展示。

這不代表人眼可以直接「看見聲波」；真正的可觀測性仍需要 microphone array、pressure sensor、stroboscopic measurement、field reconstruction 或顯示層。但在實驗時間尺度與桌上型裝置尺寸之間，聲學 carrier 往往較容易建立直觀的 propagation map。

2018 年已有利用 labyrinthine metasurfaces 求解高階常微分方程的 acoustic analog computing proposal。2023 年進一步提出基於 ultrasonic metasurfaces 的 compact analog computing system，用於常微分與偏微分方程。

因此在 CGA 中可以建立：

$$
\text{acoustic packet}
\rightarrow
\text{guided propagation}
\rightarrow
\text{interference / filtering}
\rightarrow
\text{readout}.
$$

聲學系統尤其適合「展示優先」與「量測優先」的 MVP，但其速度、尺寸、材料損耗與換能效率也可能限制高性能版本。

這說明 MVP carrier ranking 與最終性能 ranking 可以不同。

---

## 11. 電荷、電壓脈衝與電場載體

若 carrier 改為電荷、電壓或電流脈衝，算盤的幾何形式會迅速接近 transmission-line computing、analog circuit、FPGA routing 與傳統數位電路。

可寫為

$$
x_i
\leftrightarrow
V_i(t)
$$

或

$$
x_i
\leftrightarrow
Q_i.
$$

電性 backend 的最大優勢不是「新奇」，而是閾值、鎖存、feedback、memory 與 switching 都有非常成熟的工程元件。

例如基數 $b$ 的進位規則可抽象為

$$
x_i\geq b
\Rightarrow
\begin{cases}
x_i' = x_i-b,\\
x_{i+1}' = x_{i+1}+1.
\end{cases}
$$

這需要一個 threshold event：

$$
\Theta(x_i-b).
$$

電子系統非常適合實現這類非線性轉移。

所以如果 CGA 的研究目標是先驗證「幾何算盤可跨 carrier 實現」，電子／低頻 electrical backend 可能是最容易建立 reference platform 的選項；如果目標是證明 wave relation 本身可以計算，RF、聲學或光學則更具有研究區辨度。

---

## 12. CGA-2：關係編碼

真正的相變發生在「狀態不只存在於 carrier 本身，而存在於 carrier 之間的關係」。

對兩個相干波：

$$
\psi
=
\psi_1+\psi_2.
$$

可觀測強度為

$$
I
=
|\psi_1+\psi_2|^2.
$$

展開得到

$$
I
=
|\psi_1|^2
+
|\psi_2|^2
+
2\operatorname{Re}(\psi_1^*\psi_2).
$$

最後一項不是單一 carrier 的獨立屬性，而取決於兩者的相位與複數關係。

因此在 wave system 中，計算狀態可以從

$$
X
=
\{x_1,x_2,\ldots,x_n\}
$$

擴張為

$$
X'
=
(X,R_X),
$$

其中 $R_X$ 表示 pairwise 或 higher-order relation。

這導致：

$$
\boxed{
\text{state-on-node}
\rightarrow
\text{state-on-node}
+
\text{state-on-relation}
}
$$

對傳統算盤而言，珠子之間通常不透過相干疊加形成新的數值自由度；對波式 CGA 而言，干涉項本身就可以成為演算的一部分。

因此 CGA-2 已不只是「更快的算盤」。它開始進入 relational physical computing。

---

## 13. 為什麼干涉不是免費的計算能力？

relation coding 很強，但不能把干涉描述成免費無限平行計算。

首先，能被可靠使用的 mode 數受到：

$$
\text{bandwidth},
\text{SNR},
\text{coherence},
\text{loss},
\text{crosstalk},
\text{detector resolution}
$$

限制。

其次，若需要從一個複雜波場讀出 $n$ 個獨立結果，讀出成本可能重新成為瓶頸。

第三，線性波動的強項通常是線性轉換：

$$
y=Ax,
$$

或 convolution、Fourier filtering、Green's-function mapping 等。

若要實現一般的條件分支與離散狀態機，仍需非線性或閉環控制。

所以 performance 應比較完整鏈路：

$$
T_{\mathrm{total}}
=
T_{\mathrm{encode}}
+
T_{\mathrm{configure}}
+
T_{\mathrm{physical}}
+
T_{\mathrm{read}}
+
T_{\mathrm{refine}}.
$$

能量也應比較：

$$
E_{\mathrm{total}}
=
E_{\mathrm{source}}
+
E_{\mathrm{control}}
+
E_{\mathrm{physical}}
+
E_{\mathrm{sense}}
+
E_{\mathrm{digital}}.
$$

若只比較 $T_{\mathrm{physical}}$，很容易高估 wave backend 的實際優勢。

---

## 14. 進位是 CGA 的關鍵測試

算盤之所以適合作為祖型，不只是因為它「有位置」，而是因為它明確暴露 carry propagation。

對基數 $b$：

$$
x_i+x_i^{\mathrm{in}}
=
y_i+b c_{i+1},
$$

其中

$$
y_i
=
(x_i+x_i^{\mathrm{in}})\bmod b
$$

以及

$$
c_{i+1}
=
\left\lfloor
\frac{x_i+x_i^{\mathrm{in}}}{b}
\right\rfloor.
$$

如果一個 carrier-generalized demonstrator 只能讓 pulse 沿 rail 移動，但 carry 最後完全由 CPU 在背景中算出，它仍只是 transport visualization。

更強的 MVP 應要求 carry event 至少部分由 physical state 觸發。

例如抽象地：

$$
q_i
\geq
q_{\mathrm{th}}
\Rightarrow
\text{trigger}_{i+1}=1.
$$

這個 threshold 可以來自 physical nonlinearity，也可以來自 sensor--supervisor--actuator loop。

但兩種模式必須在 provenance 中標明：

$$
\text{native physical carry}
$$

與

$$
\text{supervised physical carry}.
$$

這能避免把不同強度的實現混為一談。

---

## 15. 碰撞計算提供一個歷史上的理論橋樑

Fredkin 與 Toffoli 的 billiard-ball model 提供了一個非常適合本篇的先例。

在理想化模型中，資訊由某條路徑上是否存在球來表示；路徑相當於 wire；球的彈性碰撞改變後續軌跡，因而形成邏輯操作。

可以抽象為：

$$
\text{presence / absence}
+
\text{trajectory}
+
\text{collision rule}
\rightarrow
\text{logic}.
$$

這個模型與算盤不同，但共同顯示：

$$
\boxed{
\text{geometry and dynamics can themselves encode computation}
}
$$

而不必先假定 Boolean gate 必須是某種特定電子元件。

CGA 將這個思想轉向另一個方向：不是從 billiard-ball collision 建構通用邏輯，而是從一個已有明確人類可讀語義的幾何計算祖型出發，逐步替換 carrier，觀察計算類型何時發生相變。

---

## 16. CGA-3：動態幾何

在前幾級中，幾何 $G$ 大致固定：

$$
X_t
\xrightarrow{G}
X_{t+1}.
$$

但若 waveguide routing、coupling strength、phase shift、boundary condition、metasurface state 或 switch topology 可被重新配置，則

$$
G
\rightarrow
G_t.
$$

更進一步，若當前計算狀態影響下一步幾何配置：

$$
X_t
\rightarrow
G_{t+1},
$$

同時幾何又控制下一步狀態：

$$
G_t
\rightarrow
X_{t+1},
$$

則完整演化變成

$$
\boxed{
(X_t,G_t)
\rightarrow
(X_{t+1},G_{t+1}).
}
$$

此時「桿子」本身已經成為計算狀態。

因此 CGA 的概念演化可以寫成：

$$
\boxed{
\text{position coding}
\rightarrow
\text{mode coding}
\rightarrow
\text{relation coding}
\rightarrow
\text{dynamical geometry}.
}
$$

最後一級已經超出普通算盤的直觀定義，但仍保留其系譜：計算始終由受約束狀態與可控制幾何關係共同產生。

---

## 17. 何時「算盤」應該停止被叫做算盤？

這是一個重要的概念邊界。

若系統只使用：

$$
\text{rail}
+
\text{ordered state}
+
\text{carry}
$$

那麼稱為 generalized abacus 很自然。

但如果系統已經大量使用：

$$
\text{matrix-valued coupling},
\text{phase interference},
\text{Fourier transform},
\text{reconfigurable topology},
\text{feedback dynamics},
$$

它的實際計算能力便不再由傳統算盤語義描述。

因此本文將 CGA 視為一個「祖型與研究座標」，而不是要求所有後代設備永久保留 abacus 名稱。

可以寫成：

$$
\text{Abacus}
\rightarrow
\text{Carrier-Generalized Abacus}
\rightarrow
\text{Wave / Field Computer}.
$$

這是一條生成路徑，而不是本體同一宣稱。

前置理論中的區分再次適用：

$$
\boxed{
\text{same ancestry}
\not\Rightarrow
\text{same final computational class}.
}
$$

---

## 18. 不同 carrier 的第一輪比較

下表只作研究選型，不代表固定排名。

| Carrier | 主要可用自由度 | 優勢 | 主要困難 | 第一代角色 |
| --- | --- | --- | --- | --- |
| 機械 | 位置、速度、碰撞 | 最直觀、容易解釋 | 慢、磨耗、密度低 | reference / teaching |
| 電性 | 電壓、電荷、時間、閾值 | switching、memory、feedback 成熟 | 容易退化成普通電子計算 | reference backend |
| RF | 振幅、相位、頻率、時間、路由 | 可重構、量測成熟、波效應清楚 | 尺寸、類比誤差、I/O | MVP 強候選 |
| 聲學／超音波 | 壓力、相位、頻率、延遲、共振 | 傳播與共振容易量測、展示友善 | 速度、換能、損耗、尺寸 | demonstrator 強候選 |
| 光學／光子 | 振幅、相位、波長、偏振、時間、空間模式 | 高頻寬、多工、低傳播延遲 | 對準、熱漂移、非線性、讀出、memory | 長期高性能 backend |
| 可重構場／metastructure | 邊界、耦合、散射、transfer function | 幾何本身直接參與計算 | calibration、fabrication、任務專用性 | CGA-2/3 研究核心 |

真正的選型目標不是最大化單一指標，而是對任務 $\tau$ 最大化：

$$
J(m,\tau)
=
\alpha P
+
\beta O
+
\gamma R
+
\delta V
-
\eta C,
$$

其中可以分別表示 performance、observability、repeatability、verifiability 與 cost。

第一代 demonstrator 應給 $O$ 、 $R$ 、 $V$ 較高權重；產品級 accelerator 才逐步提高 $P$ 的權重。

---

## 19. 可觀測性不是肉眼可見

本系列強調 observable physical computation，但「可觀測」不能被誤解為一定要用肉眼直接看到 carrier。

令物理軌跡為

$$
\Gamma
=
[X(t)]_{t_0}^{t_1}.
$$

觀測系統為

$$
y(t)
=
M_O(X(t))+\eta(t).
$$

只要存在足夠獨立、可校正、可重複的 measurement operator $M_O$，便可以使中間狀態對研究者可檢查。

因此：

$$
\boxed{
\text{observable}
\neq
\text{visible to naked eye}.
}
$$

但對教育與展示型 CGA，可以另外建立 rendering layer：

$$
M_O(X(t))
\rightarrow
\text{human-scale visualization}.
$$

關鍵是 rendering layer 不應替代原始 physical evidence，而應保留兩者對應關係。

---

## 20. CGA 與 External Physical Compute Appliance 的接口

Paper 00 將 EPCA 定義為：

$$
\mathcal M
=
\mathcal P
\oplus
\mathcal S
\oplus
\mathcal I
\oplus
\mathcal O
\oplus
\mathcal N
\oplus
\mathcal U
\oplus
\mathcal E.
$$

CGA 可以作為其中第一種 $\mathcal P$：

$$
\mathcal P
=
\mathcal P_{\mathrm{CGA}}.
$$

具體資料流可以寫成

$$
x
\xrightarrow{\mathcal I}
\operatorname{Encode}_m(x)
\xrightarrow{\mathcal P_{\mathrm{CGA}}}
X_m(t_1)
\xrightarrow{\mathcal O}
y_P.
$$

同時 supervisor 可以運行 reference path：

$$
x
\xrightarrow{\mathcal S_{\mathrm{ref}}}
y_D.
$$

最後得到

$$
\Delta
=
d(y_P,y_D).
$$

這形成 Paper 02 將進一步處理的雙路驗證架構。

---

## 21. Physical-Core Non-Substitution 在 CGA 中的具體判準

若 CGA 只是漂亮動畫，停用 physical core 後不會改變結果。

因此令完整結果為

$$
Q_{\mathrm{full}}
=
Q(\mathcal P_{\mathrm{CGA}},\mathcal S).
$$

停用物理路徑後為

$$
Q_{\mathrm{sup}}
=
Q(\varnothing,\mathcal S).
$$

在物理計算模式中，至少應存在一個判準 $B$，使

$$
Q_{\mathrm{full}}\in B
$$

而

$$
Q_{\mathrm{sup}}\notin B,
$$

或至少讓 physical core removal 造成可量測的性能、功能或證據差異。

例如：

- physical result 無法生成；
- 某一 wave transform 無法完成；
- latency、energy 或 parallelism 顯著改變；
- provenance 中缺少關鍵物理狀態證據。

因此一台 CGA demonstrator 也應接受「拔掉 physical core」的消融測試。

---

## 22. 第一代 MVP 不應從最複雜的數學開始

第一代 CGA 應驗證的是設備類別，而不是展示所有可能算法。

本文建議分四級算例。

### Test A：狀態搬運

證明 carrier 可以可靠表示與傳播離散狀態：

$$
s_i(t_0)
\rightarrow
s_j(t_1).
$$

### Test B：累積與比較

證明兩個以上輸入可以在 physical core 中形成可量測組合：

$$
(x_1,x_2)
\rightarrow
y_P.
$$

### Test C：進位或閾值事件

證明至少一個離散轉移由物理狀態或 physical-supervisor loop 真正觸發：

$$
x\geq\theta
\Rightarrow
c=1.
$$

### Test D：波特有運算

若 backend 是 RF、聲學或光學，應加入一個傳統機械算盤不自然具備的操作，例如：

$$
\text{interference},
\quad
\text{filtering},
\quad
\text{matrix transform},
\quad
\text{Fourier-domain operation}.
$$

這個 Test D 很重要，因為它證明 carrier substitution 不只是模仿舊算盤，而確實打開新的有效計算自由度。

---

## 23. 第一代 MVP 的 backend contract

如果未來要從 RF 換成 acoustic 或 photonic core，supervisor 不應重寫整套系統。

因此可先定義抽象 contract：

$$
\mathcal B_m
=
(
\mathrm{Caps},
\mathrm{Encode},
\mathrm{Configure},
\mathrm{Execute},
\mathrm{Observe},
\mathrm{Read},
\mathrm{Reset},
\mathrm{Calibrate}
).
$$

其中：

- $\mathrm{Caps}$：宣告可支援的操作與精度；
- $\mathrm{Encode}$：把邏輯輸入轉為 carrier state；
- $\mathrm{Configure}$：設定幾何、頻率、路由或參數；
- $\mathrm{Execute}$：啟動物理運算；
- $\mathrm{Observe}$：回傳中間狀態；
- $\mathrm{Read}$：取得輸出；
- $\mathrm{Reset}$：恢復初始狀態；
- $\mathrm{Calibrate}$：建立校正狀態。

只要不同 carrier 都能實現同一高層 contract，EPCA 就可以把 CGA backend 視為可替換模組。

這也是 Paper 05 多基底 Compute Backplane 的前置接口。

---

## 24. 計算容量不等於自由度數量

波與場具有很多自由度，很容易誘發一個錯誤推論：

> 自由度越多，計算能力就必然越高。

這不成立。

令 raw physical degrees of freedom 為

$$
D_{\mathrm{raw}}.
$$

真正可控制、可辨識、可重複且可讀出的有效自由度為

$$
D_{\mathrm{eff}}.
$$

通常只有

$$
D_{\mathrm{eff}}
\leq
D_{\mathrm{raw}}.
$$

並且可用計算容量還受到控制成本與讀出成本限制：

$$
C_{\mathrm{useful}}
=
F(
D_{\mathrm{eff}},
\mathrm{SNR},
B,
R,
T,
E
).
$$

因此 CGA 的研究重點不是「找到自由度最多的 carrier」，而是找到：

$$
\boxed{
\text{可控制}
+
\text{可辨識}
+
\text{可重複}
+
\text{可讀出}
}
$$

的自由度組合。

這與前置系列的 Dynamic Constraint Domain 直接相接：真正的工程問題是哪些原本只是物理可能的自由度，能被技術轉化為 controllable degrees of freedom。

---

## 25. 動態約束域：為什麼今天很難不等於原理上不行

對 carrier $m$，令當前工程能力狀態為

$$
K_t
=
(\mathcal K_t,\mathcal I_t,\mathcal M_t,\mathcal E_t,\mathcal F_t,\mathcal C_t,\mathcal Q_t).
$$

可實現的 CGA 設計集合為

$$
\mathcal R_{m,t}^{\mathrm{CGA}}.
$$

某一種動態 geometry 或高密度 mode multiplexing 今天若不在

$$
\mathcal R_{m,t}^{\mathrm{CGA}},
$$

只能說它超出當前控制、製造、量測或資源能力；不能直接推出它在物理律下不可能。

反過來，也不能因為某自由度物理上存在，就宣稱它一定可以被工程有效利用。

因此：

$$
\boxed{
\text{physical degree of freedom}
\neq
\text{engineering control variable}.
}
$$

CGA 的長期進步，很可能主要來自這個轉換：

$$
\text{constraint}
\rightarrow
\text{measurable parameter}
\rightarrow
\text{controllable parameter}
\rightarrow
\text{computational resource}.
$$

---

## 26. 跨 substrate 等價應以任務與誤差定義

機械 CGA、RF CGA 與 photonic CGA 不可能在所有物理層面相同。

因此比較必須寫成 task-relative equivalence。

令兩個 backend 為 $m_1,m_2$，任務為 $\tau$，則若

$$
d_\tau
\left(
F_\tau(m_1),
F_\tau(m_2)
\right)
\leq
\varepsilon,
$$

只表示它們在指定輸入域、精度與 readout convention 下近似功能等價。

不能推出：

$$
m_1=m_2.
$$

更不能推出它們具有相同：

$$
\text{energy},
\text{latency},
\text{noise},
\text{failure mode},
\text{physical history}.
$$

這種區分能避免「用光做出加法，所以光與電子完全等價」之類過強結論。

---

## 27. 一個重要的設計原則：保留兩條路徑

對展示與科研版本，本文建議保留：

$$
\text{Visible / Observable Path}
$$

以及

$$
\text{Fast / Utility Path}.
$$

第一條優先最大化：

$$
O,
R,
V,
$$

即 observability、repeatability、verifiability。

第二條優先最大化：

$$
P,
E^{-1},
L^{-1},
$$

即 performance、energy efficiency 與低 latency。

兩條路徑甚至可以使用不同 carrier，但共享相同 logical task description 與 evidence schema。

這使 EPCA 不必在「漂亮展示機」與「實用加速器」之間二選一。

---

## 28. CGA 的科研價值不只在加速

即使第一代 CGA 完全沒有速度優勢，它仍然可以有研究價值。

原因是它提供一個可控制的平台，研究：

1. 同一邏輯映射如何跨 substrate 實現；
2. 不同 carrier 的 error surface 如何改變；
3. 哪些演算法結構天然匹配某種物理動力；
4. 幾何、邊界與 coupling 如何從 constraint 轉成 control variable；
5. relation coding 何時真正提供額外計算效益；
6. physical trajectory 能否形成可重複、可驗證的 evidence；
7. supervisor 應做到哪裡，才不會吞掉 physical core 的計算角色。

因此第一代 CGA 更接近：

$$
\boxed{
\text{Physical Computation Observatory}
}
$$

而不只是 accelerator benchmark。

---

## 29. 可證偽性與失敗模式

本文的核心命題應接受以下反例。

### 29.1 Carrier substitution 只剩顯示效果

若物理 carrier 不參與結果生成，則它不是 computational substitution。

### 29.2 所有有用的非線性都由 supervisor 完成

若 physical core 只傳遞輸入，而所有實質計算皆由數位核心完成，則 CGA 應被降級為 sensor/display system。

### 29.3 I/O 成本吞掉物理收益

若

$$
T_{\mathrm{encode}}
+
T_{\mathrm{read}}
\gg
T_{\mathrm{digital}},
$$

則該 carrier 可能只適合展示或特定科研，不適合 accelerator。

### 29.4 多工自由度無法可靠解碼

若 mode crosstalk 隨通道數快速增加，使

$$
P_{\mathrm{error}}
\rightarrow
1,
$$

則理論 mode count 沒有實際工程價值。

### 29.5 動態幾何配置成本過高

若每次重構 $G_t$ 的成本遠高於直接數位計算，CGA-3 可能只適合重複使用同一配置的 workload。

### 29.6 跨 carrier contract 無法維持

如果每一 substrate 都需要完全不同的 task semantics，則 CGA 只能作為概念族譜，而不能形成工程統一 backend。

這些都不否定物理計算本身，但會限制本文提出的設備化方向。

---

## 30. 本篇的保守主張

本文只主張以下幾點。

### 第一

算盤可以被抽象為 constrained state-transition geometry，而不必把機械珠子視為其唯一物理本體。

### 第二

對指定任務而言，若 carrier 具備可辨識、可控制、可傳播、可交互作用、可讀出與可重置能力，則存在跨 substrate 實現算盤式計算關係的合理工程空間。

### 第三

波與場提供 time、frequency、phase、wavelength、polarization、spatial mode 等自由度，使 position coding 可以擴張成 mode coding。

### 第四

相干疊加與干涉使 relation 本身進入可觀測輸出，因此 wave backend 可從 node-state computation 跨向 relational computation。

### 第五

若幾何、邊界或 coupling 可被動態配置，則計算可由

$$
X_t\rightarrow X_{t+1}
$$

提升為

$$
(X_t,G_t)
\rightarrow
(X_{t+1},G_{t+1}).
$$

### 第六

上述跨越不保證更快、更省電或更通用；完整效益必須包含 encoding、configuration、calibration、readout 與 refinement 成本。

---

## 31. 下一篇的接口：可觀測物理計算

Paper 01 解決的是：

> 計算 carrier 可以如何從珠子推廣到波、脈衝與場？

但它還沒有充分回答：

> 我們怎麼證明眼前看到的結果真的由 physical core 算出來，而不是 supervisor 算完後再播放？

因此 Paper 02 將正式定義 Observable Physical Computation，並建立至少四層證據：

$$
\text{state evidence},
$$

$$
\text{causal intervention evidence},
$$

$$
\text{ablation evidence},
$$

$$
\text{cross-path verification evidence}.
$$

CGA 因而是 EPCA 的第一個物理祖型；Observable Computation 則是它從思想實驗進入科研儀器的第一個驗證門檻。

---

## 32. 結論：算盤的真正遺產可能不是珠子

算盤最容易被記住的是珠子與桿件。

但從計算結構來看，它更深的遺產可能是：

$$
\boxed{
\text{geometry constrains state transition}
}
$$

以及

$$
\boxed{
\text{state transition realizes computation}.
}
$$

一旦把這個關係抽離出來，珠子就只是一種 carrier。

carrier 可以是：

$$
\text{matter},
\quad
\text{charge},
\quad
\text{voltage pulse},
\quad
\text{RF wave},
\quad
\text{sound},
\quad
\text{photon},
\quad
\text{field mode}.
$$

而 carrier 一旦具有更多可控制自由度，計算也可能依序跨過：

$$
\boxed{
\text{position coding}
\rightarrow
\text{mode coding}
\rightarrow
\text{relation coding}
\rightarrow
\text{dynamical geometry}.
}
$$

因此本文並不是主張「未來電腦應該回去做算盤」。

相反地，它主張算盤可以被當成一個乾淨的理論起點，用來重新觀察一件在現代通用電腦中很容易被遮蔽的事：

$$
\boxed{
\text{計算首先是一個受物理定律支配的狀態演化過程。}
}
$$

External Physical Compute Appliance 所要做的，就是把這個過程重新封裝成一台可獨立使用、可觀測、可驗證、可替換 carrier，並最終可進入工程與科研現場的計算設備。

---

## 參考文獻

1. Fredkin, E., & Toffoli, T. (1982). *Conservative logic*. International Journal of Theoretical Physics, 21, 219-253. DOI: 10.1007/BF01857727.
2. Toffoli, T., & Margolus, N. (1987). *Cellular Automata Machines: A New Environment for Modeling*. MIT Press.
3. Silva, A., Monticone, F., Castaldi, G., Galdi, V., Alu, A., & Engheta, N. (2014). *Performing mathematical operations with metamaterials*. Science, 343(6167), 160-163. DOI: 10.1126/science.1242818.
4. Zuo, S., Wei, Q., Tian, Y., Cheng, Y., & Liu, X. (2018). *Acoustic analog computing system based on labyrinthine metasurfaces*. Scientific Reports, 8, 10103. DOI: 10.1038/s41598-018-27741-2.
5. Abdollahramezani, S., Hemmatyar, O., & Adibi, A. (2020). *Meta-optics for spatial optical analog computing*. Nanophotonics, 9(13), 4075-4095. DOI: 10.1515/nanoph-2020-0285.
6. Wright, L. G., Onodera, T., Stein, M. M., et al. (2022). *Deep physical neural networks trained with backpropagation*. Nature, 601, 549-555. DOI: 10.1038/s41586-021-04223-6.
7. Uy, R. F., & Bui, V. P. (2023). *Solving ordinary and partial differential equations using an analog computing system based on ultrasonic metasurfaces*. Scientific Reports, 13, 13471. DOI: 10.1038/s41598-023-38718-1.
8. Tzarouchis, D. C., Edwards, B., & Engheta, N. (2025). *Programmable wave-based analog computing machine: a metastructure that designs metastructures*. Nature Communications, 16, 908. DOI: 10.1038/s41467-025-56019-1.
9. Vinay, M. L. (2025). *A reconfigurable metastructure for wave-based matrix maths*. Nature Reviews Electrical Engineering, 2, 154. DOI: 10.1038/s44287-025-00159-5.
10. Hua, S., Divita, E., Yu, S., et al. (2025). *An integrated large-scale photonic accelerator with ultralow latency*. Nature, 640, 361-367. DOI: 10.1038/s41586-025-08786-6.

---

## 前置系列銜接

- 《跨尺度構成與動態約束域研究》v0.1：有效物理等價、多重實現、構成復現、Dynamic Constraint Domain 與 controllable degree of freedom。
- 《認知功能體的物理實現與自然可觀測性研究》v0.1：關係--結構--動力--功能、跨 substrate 功能實現與 task-relative functional equivalence。
- 《外掛式物理計算機與現場計算設備研究》Paper 00：EPCA、Local Execution Closure、Physical-Core Non-Substitution、Supervisor Separation 與 Evidence-Bearing Result。

本篇將上述抽象框架落到第一個具體計算祖型：把算盤由「機械珠子裝置」重新表述為「跨 carrier 的受約束狀態轉移幾何」。
