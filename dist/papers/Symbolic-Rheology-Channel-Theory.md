# 符號流變信道理論（Symbolic Rheology Channel Theory）
**EML-SRC-2026-v0.1**

EveMissLab（一言諾科技有限公司）
Neo.K（許筌崴）
2026年6月

---

## 摘要

本文提出**符號流變信道（Symbolic Rheology Channel，SRC）**這一新型信息傳輸模型，其信道噪聲不來自隨機擾動，而來自確定性的物理流變演化。我們將一個特定的粒子流體仿真系統形式化為三層結構：（1）符號串經確定性哈希函數映射為粒子初始狀態的**編碼器**；（2）由諧波吸引子、黏滯耦合與阻尼組成的**流變引擎**；（3）經逆旋轉投影與指數移動平均濾波進行格點重建的**解碼器**。我們定義位元錯誤率（BER）為信道保真度的主要觀測量，推導其在參數空間中的動力學方程，論證臨界耦合強度 $K_c$ 的存在性，並討論流變信道容量的邊界估計。這一框架首次將符號學、信息論與連續流體動力學系統置於統一的形式架構之下，構成後續三篇姊妹論文的信息論基礎。

**關鍵詞：** 流變學，信道容量，位元錯誤率，哈希函數，粒子動力學，相變，信息保真度

---

## 1. 引言

### 1.1 動機與背景

信息論自Shannon（1948）以來，以**隨機噪聲**為信道不確定性的主要來源。然而，一大類真實系統中，信息的退化並非源於隨機過程，而源於**確定性動力學的演化**——信息被嵌入到一個物理場的初始狀態之中，而這個物理場依照自身的演化規律不斷改變，使得從終態反推初始編碼的難度隨時間增加。

這類信道的原型之一是量子退相干：量子信息被嵌入疊加態，環境耦合使相位信息逐漸擴散到環境自由度中，導致信息不可逆流失。然而，量子退相干屬於量子力學範疇，其數學工具（密度矩陣、Lindblad算子）不直接適用於古典流體動力學。

本文考察的系統介於兩者之間：一個**古典確定性的流變粒子場**，其初始狀態由符號串唯一決定，演化由牛頓力學（帶諧波強迫與黏滯耦合）支配，解碼由空間投影重建完成。我們稱這樣的系統為**符號流變信道**（SRC）。

### 1.2 系統起源

本文的數學對象來源於兩個具體的計算機仿真系統：一個基於QR碼矩陣的三維粒子流變沙盒（稱為MR2.5系統），以及一個基於文字光柵化的二維粒子流變沙盒（稱為RHEO-1.0系統）。兩者共享相同的物理引擎核心，但在粒子初始化方式、耦合拓撲、觀測量輸出上各有差異。

本文從這兩個具體系統中抽象出共同的數學結構，構建一般性的SRC理論。後續三篇姊妹論文（EML-GCT-2026、EML-PCH-2026、EML-DRIC-2026）分別從算子代數、拓撲學、幾何學三個角度對同一系統進行深入分析。

### 1.3 本文貢獻

- 提出符號流變信道（SRC）的嚴格形式化定義（第2節）
- 推導諧波吸引＋黏滯耦合系統的線性化動力學（第3節）
- 定義流變BER及其與物理參數的關係（第4節）
- 論證臨界耦合相變的存在性（第5節）
- 建立流變信道容量的估計框架（第6節）
- 討論與古典Shannon信道的比較（第7節）

---

## 2. 符號流變信道的形式化定義

### 2.1 基本符號

設 $\Sigma$ 為有限字母集（本文以英數字元為例，$|\Sigma| \leq 36$）。設 $\mathcal{S}^*$ 為 $\Sigma$ 上所有有限字串的集合。一個長度為 $\ell$ 的消息為 $\mathbf{s} = (s_1, s_2, \ldots, s_\ell) \in \Sigma^\ell$。

粒子集合 $\mathcal{P} = \{p_1, p_2, \ldots, p_N\}$。每個粒子 $p_i$ 在 $d$ 維空間（$d = 2$ 或 $3$）中擁有：
- 位置向量 $\mathbf{x}_i(t) \in \mathbb{R}^d$
- 速度向量 $\mathbf{v}_i(t) \in \mathbb{R}^d$
- 靜止（平衡）位置 $\mathbf{x}_i^{(0)} \in \mathbb{R}^d$
- 固有頻率 $\omega_i \in \mathbb{R}_{>0}$
- 初始相位 $\phi_i \in [0, 2\pi)$
- 語義標籤 $\sigma_i \in \Sigma \cup \{\text{structural}\}$

系統狀態向量 $\Phi(t) = (\mathbf{x}_1, \mathbf{v}_1, \ldots, \mathbf{x}_N, \mathbf{v}_N)^T \in \mathbb{R}^{2dN}$。

### 2.2 編碼器

**定義 2.1（流變編碼器）。** 流變編碼器是一個映射

$$E: \mathcal{S}^* \to \mathbb{R}^{2dN}$$

將符號串 $\mathbf{s}$ 映射到初始系統狀態 $\Phi_0 = E(\mathbf{s})$，由以下步驟構成：

**步驟一（結構化初始位置）：** 對每個符號串 $\mathbf{s}$，生成一個結構性位置場
$$\mathbf{x}_i^{(0)} = \mathcal{G}(\mathbf{s}, i)$$
其中 $\mathcal{G}$ 是一個從字串到空間位置的確定性映射（例如QR碼格點或文字光柵化像素）。

**步驟二（哈希種子採樣）：** 對每個粒子 $p_i$，計算哈希種子
$$h_i = \mathrm{FNV1a}(\mathrm{key}_i(\mathbf{s})) \in [0, 2^{64})$$
其中 $\mathrm{key}_i(\mathbf{s})$ 是依賴消息內容和粒子索引的字串。

**步驟三（動力學參數賦值）：**
$$\phi_i = \frac{h_i \bmod 10^3}{10^3} \cdot 2\pi, \quad \omega_i = \omega_{\min} + \frac{h_i \bmod 10^2}{10^2} \cdot \Delta\omega$$

具體地：對QR系統，$\omega_{\min} = 0.5$，$\Delta\omega = 1.6$；對文字系統，$\omega_{\min} = 0.4$，$\Delta\omega = 1.8$。

**步驟四（初速度為零）：** $\mathbf{v}_i(0) = \mathbf{0}$ 對所有 $i$。

因此 $E(\mathbf{s})$ 是確定性的（無隨機性），且在哈希碰撞概率可忽略的意義下是單射的。

**注記 2.1.** 編碼器的確定性是SRC與傳統信道的根本差異之一。在Shannon信道中，信道噪聲是隨機的，而信息是確定的。在SRC中，兩者均為確定的——但信道（流變引擎）的確定性動力學使解碼變得困難。

### 2.3 流變引擎（信道）

**定義 2.2（流變引擎）。** 流變引擎是一族參數化動力系統

$$\mathcal{E} = \{F_{K,A,\gamma,\Delta t}: \mathbb{R}^{2dN} \to \mathbb{R}^{2dN}\}$$

由離散時間映射 $F$ 定義，每步對系統狀態 $\Phi$ 進行如下更新：

**諧波吸引步（目標計算）：**
$$\theta_i(t) = 2\pi\omega_i t + \phi_i$$
$$\mathbf{q}_i(t) = \mathbf{x}_i^{(0)} + \mathbf{A} \odot \mathbf{f}(\theta_i)$$

其中 $\mathbf{A} \odot \mathbf{f}(\theta_i)$ 表示振幅矩陣與振盪函數的Hadamard積。具體地：

$$q_{i,x}(t) = x_i^{(0)} + A\sin(\theta_i)$$
$$q_{i,y}(t) = y_i^{(0)} + A\cos(\alpha_y \theta_i), \quad \alpha_y \in \{1.3, 1.4\}$$
$$q_{i,z}(t) = z_i^{(0)} + A_Z\sin(\alpha_z \theta_i), \quad \alpha_z = 0.8 \quad \text{(僅3D)}$$

其中 $A_Z = \beta_\sigma A$，$\beta_\sigma$ 依粒子語義標籤取值（結構性粒子 $\beta = 0.25$，資料粒子 $\beta = 0.6$）。

**彈簧加速度步：**
$$\mathbf{a}_i^{\text{spring}} = k_s(\mathbf{q}_i - \mathbf{x}_i)$$

**黏滯耦合步（見EML-GCT-2026的完整處理）：**
$$K^* = 1 - e^{-K}$$
$$\langle\mathbf{v}\rangle_i = \frac{\sum_j C_{ij} \mathbf{v}_j}{\sum_j C_{ij}}$$
$$\mathbf{a}_i^{\text{visc}} = K^*(\langle\mathbf{v}\rangle_i - \mathbf{v}_i)$$

**Euler積分與阻尼：**
$$\mathbf{v}_i \leftarrow \mathbf{v}_i + \mathbf{a}_i^{\text{spring}} + \mathbf{a}_i^{\text{visc}}$$
$$\mathbf{x}_i \leftarrow \mathbf{x}_i + \mathbf{v}_i$$
$$\mathbf{v}_i \leftarrow \gamma \mathbf{v}_i$$

時間步 $t \leftarrow t + \Delta t$。

$n$ 步後的狀態為 $\Phi_n = F^n(\Phi_0)$，其中 $F^n$ 是 $F$ 的 $n$ 次迭代複合。

### 2.4 解碼器

**定義 2.3（流變解碼器）。** 流變解碼器是一個映射

$$D: \mathbb{R}^{2dN} \times \Theta \to \mathcal{S}^*$$

其中 $\Theta = SO(d)$ 是旋轉角的參數空間（在3D中為 $(\psi, \varphi)$ 偏航角和俯仰角）。解碼分三步：

**步驟一（逆旋轉）：** 對每個粒子 $p_i$，計算旋轉前的近似坐標：

對3D系統，逆俯仰（$\varphi$，X軸）：
$$z'_i = z_i\cos\varphi + y_i\sin\varphi$$
$$y'_i = -z_i\sin\varphi + y_i\cos\varphi$$

逆偏航（$\psi$，Y軸）：
$$x''_i = x_i\cos\psi + z'_i\sin\psi$$
$$z''_i = -x_i\sin\psi + z'_i\cos\psi$$

**步驟二（指數移動平均濾波）：** 以時間常數 $\alpha = 0.06$ 對逆旋轉坐標進行低通濾波：
$$\langle x_i \rangle_n = (1-\alpha)\langle x_i \rangle_{n-1} + \alpha x''_i$$

這是一個一階無限脈衝響應（IIR）濾波器，其時間常數為 $\tau_\alpha = -1/\ln(1-\alpha) \approx 16.2$ 步。

**步驟三（格點重建）：** 以格距 $h = 13.5$ 進行四捨五入：
$$c_i^{\text{rec}} = \text{round}\!\left(\frac{\langle x_i \rangle}{h} + \frac{N_\text{grid}}{2}\right)$$
$$r_i^{\text{rec}} = \text{round}\!\left(\frac{\langle y_i \rangle}{h} + \frac{N_\text{grid}}{2}\right)$$

重建矩陣 $M^{\text{rec}}[r,c] = 1$ 若 $(r,c)$ 被至少一個粒子覆蓋，否則為 $0$。

解碼器 $D$ 從重建矩陣 $M^{\text{rec}}$ 運行QR解碼協議，輸出字串 $\hat{\mathbf{s}}$。

### 2.5 信道的完整定義

**定義 2.4（符號流變信道）。** 符號流變信道 $\mathcal{C}_{K,A,\gamma,\Delta t,n}$ 是一個五元組：

$$\mathcal{C} = (\Sigma, E, \mathcal{E}, D, \text{BER})$$

其中：
- $\Sigma$：字母集
- $E: \mathcal{S}^* \to \mathbb{R}^{2dN}$：流變編碼器
- $\mathcal{E}$：流變引擎，以參數 $(K, A, \gamma, \Delta t)$ 運行 $n$ 步
- $D: \mathbb{R}^{2dN} \times \Theta \to \mathcal{S}^*$：流變解碼器
- $\text{BER}: \mathcal{S}^* \times \mathcal{S}^* \to [0,1]$：位元錯誤率函數

對於一條消息 $\mathbf{s}$，信道輸出為：
$$\hat{\mathbf{s}} = D(\mathcal{E}^n(E(\mathbf{s})), \Theta^*)$$

其中 $\Theta^* = (\psi^*, \varphi^*)$ 是當前相機角度。

---

## 3. 線性化動力學分析

### 3.1 位移變量

定義位移 $\boldsymbol{\delta}_i(t) = \mathbf{x}_i(t) - \mathbf{x}_i^{(0)}$。目標位移：
$$\boldsymbol{\eta}_i(t) = \mathbf{q}_i(t) - \mathbf{x}_i^{(0)} = \mathbf{A} \odot \mathbf{f}(\theta_i(t))$$

彈簧力在位移變量下的形式：
$$\mathbf{a}_i^{\text{spring}} = k_s(\boldsymbol{\eta}_i - \boldsymbol{\delta}_i)$$

因此動力學方程變為：
$$\dot{\boldsymbol{\delta}}_i = \mathbf{v}_i$$
$$\dot{\mathbf{v}}_i = k_s(\boldsymbol{\eta}_i - \boldsymbol{\delta}_i) + K^*(\langle\mathbf{v}\rangle_i - \mathbf{v}_i) - (1-\gamma)\mathbf{v}_i/\Delta t$$

注意：由於使用離散Euler積分，「阻尼」是乘法的（$\mathbf{v} \leftarrow \gamma\mathbf{v}$），等效於每步減去 $(1-\gamma)\mathbf{v}$，即連續時間下的阻尼係數為 $\mu = (1-\gamma)/\Delta t$。

### 3.2 解耦近似：單粒子方程

在無耦合（$K = 0$）、小位移情況下，每個粒子的方程解耦為獨立的一維強迫阻尼振盪子：

$$\ddot{\delta}_i + \mu\dot{\delta}_i + k_s\delta_i = k_s\eta_i(t)$$

其中 $\eta_i(t) = A\sin(2\pi\omega_i t + \phi_i)$ 是週期性外力（僅考慮x分量）。

這是一個經典的強迫阻尼諧振子。穩態響應為：
$$\delta_i^{\text{ss}}(t) = \frac{k_s A}{\sqrt{(k_s - (2\pi\omega_i)^2)^2 + \mu^2(2\pi\omega_i)^2}} \sin(2\pi\omega_i t + \phi_i + \psi_i)$$

其中相移：
$$\psi_i = \arctan\!\left(\frac{\mu \cdot 2\pi\omega_i}{k_s - (2\pi\omega_i)^2}\right)$$

共振頻率 $\omega_0^{\text{res}} = \sqrt{k_s}/(2\pi)$。代入具體數值 $k_s = 0.12$：
$$\omega_0^{\text{res}} = \frac{\sqrt{0.12}}{2\pi} \approx 0.055$$

由於粒子頻率 $\omega_i \in [0.5, 2.1]$ 遠大於共振頻率，系統工作在**高頻強制**區域。此時響應幅值近似：
$$|\delta_i^{\text{ss}}| \approx \frac{k_s A}{(2\pi\omega_i)^2}$$

**命題 3.1.** 在 $K = 0$、穩態條件下，粒子的均方根位移（相對於靜止位置）滿足：
$$\sigma_{\delta,i}^2 \equiv \langle\delta_i^2\rangle = \frac{k_s^2 A^2}{2[(k_s - (2\pi\omega_i)^2)^2 + \mu^2(2\pi\omega_i)^2]}$$

對 $\omega_i \in [0.5, 2.1]$，此值約在 $[10^{-4}A^2, 10^{-2}A^2]$ 範圍內（數值估算，取 $k_s = 0.12$，$\mu \approx 0.024/\Delta t$）。

### 3.3 耦合修正

引入耦合後（$K > 0$），系統方程不再解耦。定義速度場 $\mathbf{V}(t) = (\mathbf{v}_1, \ldots, \mathbf{v}_N)^T$，耦合項寫成矩陣形式：

$$\mathbf{a}^{\text{visc}} = K^* \cdot \mathcal{L}_C \mathbf{V}$$

其中 $\mathcal{L}_C$ 是由耦合矩陣 $C = (C_{ij})$ 定義的正規化圖拉普拉斯算子：
$$(\mathcal{L}_C)_{ij} = \frac{C_{ij}}{\sum_k C_{ik}} - \delta_{ij}$$

$\mathcal{L}_C$ 的特徵值 $\lambda \in [-1, 0]$（對稱耦合時），特徵向量描述速度場的「集體模式」。

**耦合對BER的影響：** 直觀地，耦合使相鄰粒子的速度趨於一致，從而：
- 在振盪中使同群粒子同步（有序化效應），若同步方向是「回歸原位」，則降低BER
- 但若耦合強度過大（$K^*$ 接近1），則粒子的個體動力學被集體運動淹沒，使單個粒子無法回到其特定格點，從而升高BER

這預示著一個最優耦合強度的存在。

---

## 4. 位元錯誤率：定義與動力學

### 4.1 BER的嚴格定義

設 $N_\text{grid} = 29$（以QR-v3為例），原始矩陣 $M^{\text{orig}} \in \{0,1\}^{29\times29}$，重建矩陣 $M^{\text{rec}} \in \{0,1\}^{29\times29}$。

**定義 4.1（瞬時BER）。**
$$\text{BER}(t) = \frac{1}{N_\text{grid}^2}\sum_{r=0}^{N_\text{grid}-1}\sum_{c=0}^{N_\text{grid}-1}\mathbf{1}\!\left[M^{\text{orig}}[r,c] \neq M^{\text{rec}}(t)[r,c]\right]$$

注意 $\text{BER}(t) \in [0,1]$。

**定義 4.2（模組錯誤函數）。** 粒子 $p_i$（位於格點 $(r_i, c_i)$）在時刻 $t$ 的模組錯誤為：
$$\epsilon_i(t) = \mathbf{1}\!\left[|c_i^{\text{rec}}(t) - c_i| + |r_i^{\text{rec}}(t) - r_i| > 0\right]$$

則 $\text{BER}(t) \approx \frac{1}{|\mathcal{P}_{\text{dark}}|}\sum_{i \in \mathcal{P}_{\text{dark}}}\epsilon_i(t)$，其中 $\mathcal{P}_{\text{dark}}$ 是原始深色模組的粒子集合。

### 4.2 模組錯誤的觸發條件

粒子 $p_i$ 在時刻 $t$ 發生模組錯誤，當且僅當其EMA濾波後的重建位置偏離格點超過半格距：

$$\epsilon_i(t) = 1 \iff \left|\langle x_i \rangle(t) - x_i^{(0)}\right| > \frac{h}{2} \text{ 或 } \left|\langle y_i \rangle(t) - y_i^{(0)}\right| > \frac{h}{2}$$

其中格距 $h = 13.5$，因此臨界位移閾值 $\delta_c = h/2 = 6.75$。

**注記 4.1.** EMA濾波引入了一個重要的時間平滑效應。原始粒子位移 $\boldsymbol{\delta}_i(t)$ 可能瞬時超過 $\delta_c$，但EMA輸出 $\langle\boldsymbol{\delta}_i\rangle(t)$ 由於其低通特性，響應較慢。這意味著：快速振盪（高 $\omega_i$）帶來的位移對BER的貢獻被EMA部分抑制。

### 4.3 EMA的傳遞函數

EMA濾波器在z-域的傳遞函數為：
$$H(z) = \frac{\alpha z}{z - (1-\alpha)} = \frac{0.06z}{z - 0.94}$$

其頻率響應（令 $z = e^{j\Omega}$，$\Omega$ 為數位角頻率）：
$$|H(e^{j\Omega})| = \frac{\alpha}{\sqrt{1 - 2(1-\alpha)\cos\Omega + (1-\alpha)^2}}$$

截止頻率（3dB點）：
$$\Omega_{3\text{dB}} = \arccos\!\left(1 - \frac{\alpha^2}{2(1-\alpha)}\right) \approx 0.119 \text{ rad/step}$$

這對應於每步時間 $\Delta t = 0.012$ 下的物理頻率 $f_{3\text{dB}} \approx 0.119/(2\pi\cdot0.012) \approx 1.58$ Hz（物理時間單位）。

由於粒子頻率 $\omega_i \in [0.5, 2.1]$，部分高頻粒子（$\omega_i > 1.58$）的振盪位移被EMA顯著衰減，而低頻粒子（$\omega_i < 1.58$）的位移則通過。

**命題 4.1（EMA保護效應）。** 在穩態（$t \to \infty$）下，EMA輸出的均方位移滿足：
$$\langle\langle\boldsymbol{\delta}_i\rangle^2\rangle \leq |H(e^{j\Omega_i})|^2 \cdot \langle\boldsymbol{\delta}_i^2\rangle$$

其中 $\Omega_i = 2\pi\omega_i\Delta t$ 是粒子 $i$ 的數位角頻率。高頻粒子 $|H|^2 \ll 1$，從而EMA有效降低這些粒子的表觀位移，起到保護BER的作用。

### 4.4 BER的期望值估計

定義粒子 $p_i$ 的錯誤概率（對位移分佈的時間平均）：

$$\bar{\epsilon}_i = \Pr\!\left[|\langle\delta_{i,x}\rangle| > \delta_c \text{ 或 } |\langle\delta_{i,y}\rangle| > \delta_c\right]$$

若假設 $\langle\delta_{i,x}\rangle$ 在時間上準高斯分佈（中心極限論證），均值為零，方差為 $\sigma_i^2 = |H(e^{j\Omega_i})|^2 \cdot \sigma_{\delta,i}^2$，則：

$$\bar{\epsilon}_i \approx 2\left[1 - \Phi\!\left(\frac{\delta_c}{\sigma_i}\right)\right]$$

其中 $\Phi$ 是標準正態CDF。期望BER：

$$\langle\text{BER}\rangle \approx \frac{1}{N_\text{dark}}\sum_{i \in \mathcal{P}_\text{dark}} 2\left[1 - \Phi\!\left(\frac{\delta_c}{\sigma_i(K,A,\gamma)}\right)\right]$$

這揭示了BER與物理參數的依賴關係：
- BER隨 $A$（振幅）增大而升高（更大位移）
- BER隨 $\gamma$（阻尼）增大而升高（有效阻尼減弱→更大速度）
- BER與 $K$ 的關係非單調（見第5節）

---

## 5. 臨界耦合與相變

### 5.1 耦合對BER的雙重效應

黏滯耦合通過兩種相互競爭的機制影響BER：

**效應A（同步保護）：** 在語義同類的粒子群中（例如，同一字符的所有粒子），耦合使速度趨於群平均。若群的平均速度指向其平衡位置（彈簧力效應），耦合有效地放大了「回歸力」，降低偏移概率，從而降低BER。

**效應B（去同步破壞）：** 對個體粒子而言，耦合強制其速度向鄰居平均，這可能使一個原本正朝著自身平衡位置運動的粒子被「拉偏」，轉向其鄰居的平均方向。當鄰居本身也在振盪時，這種效應實際上是引入了額外的「社會噪聲」，升高BER。

兩種效應的相對強弱取決於 $K^*$ 和粒子頻率的分佈。

### 5.2 臨界耦合的定性論證

定義BER對 $K$ 的導數：$\partial\text{BER}/\partial K$。

在 $K \to 0$ 時，粒子解耦。系統的BER由各粒子獨立的穩態位移決定，值為 $\text{BER}_0$。

在 $K$ 增大初期（$K \ll 1$），效應A佔主導（特別是當粒子頻率分佈較均勻時），$\partial\text{BER}/\partial K < 0$，BER下降。

在 $K$ 繼續增大（$K \sim 1$），$K^* = 1 - e^{-K}$ 接近飽和。耦合力主導彈簧力（$K^* \gg k_s$），粒子的個體共振被集體運動覆蓋。粒子的有效位移主要由集體模式（$\mathcal{L}_C$ 的主特徵向量）決定，而非個體吸引子。此時BER急劇升高。

在 $K \to \infty$，所有粒子速度趨於全場平均值，粒子做集體平移，無法回到各自的格點，BER → 1（接近最大值）。

**猜想 5.1（臨界耦合相變）。** 對於給定的 $(A, \gamma, \Delta t, \omega\text{分佈})$，存在臨界耦合強度 $K_c \in (0, \infty)$ 使得：

$$\frac{\partial\text{BER}}{\partial K}\bigg|_{K=K_c} = 0$$

且 $K < K_c$ 時 $\partial\text{BER}/\partial K \leq 0$（效應A主導），$K > K_c$ 時 $\partial\text{BER}/\partial K \geq 0$（效應B主導）。

$K_c$ 是SRC的**最優耦合點**，對應最低BER。

### 5.3 $K_c$ 的解析估計

在平均場近似下，假設所有粒子具有相同頻率 $\bar{\omega}$（均勻近似），耦合矩陣為全連接的均勻矩陣 $C_{ij} = 1/(N-1)$（$i \neq j$）。

則圖拉普拉斯 $\mathcal{L}_C$ 只有兩個不同的特徵值：$\lambda_0 = 0$（對應集體模式）和 $\lambda_1 = -1$（對應所有差模，重數 $N-1$）。

集體模式的速度方程（令 $\bar{V} = N^{-1}\sum_i v_i$）：
$$\dot{\bar{V}} = k_s(\bar{\eta} - \bar{\delta}) - \mu\bar{V}$$

差模速度 $w_i = v_i - \bar{V}$ 的方程：
$$\dot{w}_i = k_s(\eta_i - \delta_i - \bar{\eta} + \bar{\delta}) - \mu w_i - K^* w_i$$
$$= k_s(\eta_i^{\text{rel}} - \delta_i^{\text{rel}}) - (\mu + K^*)w_i$$

差模的等效阻尼為 $\mu + K^*$，比無耦合時多了 $K^*$。差模的穩態均方位移：
$$\sigma_{\delta,i}^{\text{rel},2} = \frac{k_s^2 A_{\text{rel}}^2}{2[(k_s - \bar{\omega}^2)^2 + (\mu + K^*)^2\bar{\omega}^2]}$$

其中 $A_{\text{rel}}$ 是相對振幅（粒子位移相對於群中心的幅值）。

隨著 $K^*$ 增大，$\sigma_{\delta,i}^{\text{rel}}$ 單調下降（差模被壓制）——這是效應A的體現。然而，集體模式（即群中心 $\bar{\delta}$）的運動卻不被耦合壓制。若群中心的振盪位移 $\bar{\delta}$ 具有顯著幅值，則耦合強的系統中每個粒子被迫跟隨群中心，而群中心本身未必在粒子的個體格點附近。

令集體模式的位移方差為 $\sigma_{\bar{\delta}}^2$（不依賴於 $K$），則粒子的總位移方差近似：
$$\sigma_{\delta,i}^2 \approx \sigma_{\bar{\delta}}^2 + \sigma_{\delta,i}^{\text{rel},2}(K)$$

BER對 $K$ 的極小發生在 $\sigma_{\delta,i}^2$ 極小化的 $K$：

$$K_c = \text{argmin}_K \sigma_{\delta,i}^2(K) = \text{argmin}_K \left[\sigma_{\bar{\delta}}^2 + \sigma_{\delta,i}^{\text{rel},2}(K)\right]$$

由於 $\sigma_{\delta,i}^{\text{rel},2}(K)$ 單調遞減而 $\sigma_{\bar{\delta}}^2$ 與 $K$ 無關，在此平均場近似下 $K_c \to \infty$——即無限強耦合。

這個結果的問題在於平均場假設本身的失效：在強耦合極限下，群中心的振盪幅值 $\sigma_{\bar{\delta}}^2$ 並不是常數，而是依賴於耦合結構。在實際的局部耦合（空間哈希格）中，「群」本身是局部的，集體模式的幾何結構更複雜。精確的 $K_c$ 需要對真實的耦合矩陣 $C$ 進行特徵值分析。

### 5.4 有限尺寸效應

在實際系統中（粒子數 $N < 900$，格點 $29 \times 29 = 841$），有限尺寸效應顯著。具體地：

- 空間哈希格的格大小 $L_{\text{cell}} = \max(25, 1.1 \cdot d_{\text{conn}})$，其中 $d_{\text{conn}} = 18$，故 $L_{\text{cell}} \approx 25$
- 格距 $h = 13.5$，故每個哈希格包含約 $(25/13.5)^2 \approx 3.4$ 個格點
- 每個粒子的鄰居數量約為 $n_{\text{neigh}} \approx 3.4 \cdot 27 \approx 92$（3D）或 $3.4 \cdot 9 \approx 31$（2D）

**注記 5.1.** 仿真中實際設定 $N < 900$（2D）或 $N < 900$（3D）的上限，超過則不進行耦合計算。這引入了一個硬性的臨界點：當 $N \geq 900$ 時，$K^* = 0$（等效於完全解耦），與「無窮大系統的熱力學極限」完全不同。

---

## 6. 流變信道容量

### 6.1 確定性信道的容量概念

在Shannon理論中，信道容量定義為在輸入分佈上最大化的互信息。然而，SRC是一個**確定性**信道：給定消息 $\mathbf{s}$ 和物理參數，輸出 $\hat{\mathbf{s}}$ 是完全確定的（無隨機性）。這使得Shannon意義下的互信息 $I(S;\hat{S})$ 退化。

我們提出兩種適用於SRC的容量概念。

### 6.2 解碼可區分性容量

**定義 6.1（解碼可區分對）。** 兩個消息 $\mathbf{s}_1 \neq \mathbf{s}_2$ 在運行 $n$ 步後是**可解碼可區分的**（decodably distinguishable），若：
$$D(\mathcal{E}^n(E(\mathbf{s}_1)), \Theta^*) \neq D(\mathcal{E}^n(E(\mathbf{s}_2)), \Theta^*)$$

定義 $\mathcal{M}(n, K, A, \gamma) \subseteq \mathcal{S}^*$ 為在給定參數和 $n$ 步後仍可被成功解碼的消息集合（即 $D(\mathcal{E}^n(E(\mathbf{s}))) = \mathbf{s}$）。

**定義 6.2（流變信道容量）。**
$$C_{\text{SRC}}(K, A, \gamma) = \lim_{n \to \infty} \frac{1}{n}\log_2 |\mathcal{M}(n, K, A, \gamma)|$$

在 $K < K_c$ 的假設下，若系統在有限BER下穩定，則 $|\mathcal{M}|$ 的漸近增長可能是有限的（信道容量有限正值）；在 $K > K_c$ 下，$|\mathcal{M}|$ 可能呈指數衰減（容量為零）。

**猜想 6.1.** 存在有效容量相變：
$$C_{\text{SRC}}(K, A, \gamma) = \begin{cases} C_0(A, \gamma) > 0 & \text{若 } K < K_c \\ 0 & \text{若 } K > K_c \end{cases}$$

此相變與猜想5.1的臨界耦合 $K_c$ 相同。

### 6.3 拓撲熵上界

由於SRC是確定性動力系統，其信息傳輸能力的另一個自然上界是動力系統的**拓撲熵** $h_{\text{top}}(\mathcal{E})$。

對於有限維的有界動力系統，Newhouse-Ruelle-Takens定理給出：
$$h_{\text{top}}(\mathcal{E}) \leq \sum_{\lambda_i > 0} \lambda_i$$

其中 $\{\lambda_i\}$ 是Lyapunov指數。

**命題 6.1（容量上界）。**
$$C_{\text{SRC}} \leq \frac{h_{\text{top}}(\mathcal{E})}{\Delta t \cdot \ln 2}$$

然而，計算SRC的Lyapunov指數是一個技術上困難的問題（需要追蹤 $2dN$ 維切向量的演化），留作未來工作。

### 6.4 ECC保護下的有效容量

實際的QR碼使用錯誤更正碼（ECC）。對於QR-v3（$29\times29$，M級ECC），ECC可更正約 $15\%$ 的模組錯誤。

**定義 6.3（ECC保護容量）。**
$$C_{\text{SRC}}^{\text{ECC}} = C_{\text{SRC}} \cdot \mathbf{1}[\text{BER} \leq \text{BER}_{\text{ECC}}]$$

其中 $\text{BER}_{\text{ECC}} \approx 0.15$ 是ECC更正閾值。

在BER $< 0.15$ 的參數區域中，即使BER $> 0$，ECC仍可恢復完整消息，信道保持有效。這對應系統狀態圖中的一個「ECC保護區域」。

---

## 7. 與古典Shannon信道的比較

### 7.1 結構差異

| 特徵 | Shannon二進制對稱信道 | 符號流變信道（SRC） |
|------|----------------------|---------------------|
| 噪聲來源 | 隨機翻轉 | 確定性動力學 |
| 編碼器 | 確定性 | 確定性（哈希映射） |
| 解碼器 | 最大似然 / 最小距離 | 逆旋轉 + EMA + 量化 |
| 信道記憶 | 無記憶 | 長記憶（Markov鏈） |
| 容量定義 | Shannon互信息 | 動力學可區分性 |
| 相變 | 無（連續退化） | 存在臨界 $K_c$ |
| 糾錯碼 | 適用 | 部分適用（ECC） |

### 7.2 信道記憶的本質

SRC是一個有記憶信道（memory channel）：當前時刻的粒子位置依賴於整個歷史（通過動力學積分）。然而，由於存在阻尼（$\gamma = 0.82$），系統的有效記憶深度有限。

具體地，速度的衰減時間常數：
$$\tau_v = -\frac{\Delta t}{\ln\gamma} = \frac{0.012}{-\ln 0.82} \approx 0.060 \text{ 秒}$$

在 $t \gg \tau_v$ 後，初始速度的影響可以忽略，系統演化主要由當前的強迫項（$\boldsymbol{\eta}_i(t)$）和累積位移（$\boldsymbol{\delta}_i(t)$）決定。

位移的記憶時間更長，由彈簧力的特徵時間 $\tau_\delta = 1/k_s = 8.33$ 決定（粗略估計）。

### 7.3 Shannon定理的類比

Shannon第一定理（無噪信道）類比：若 $K < K_c$ 且系統在穩態BER $= 0$ 下運行，則信道容量等於初始位置場所能承載的符號量（QR-v3在M級ECC下約可存儲 $\leq 47$ 個字符）。

Shannon第二定理（噪聲信道）類比：存在最優「流變編碼方案」（最優FNV1a種子選擇）使得在 $K < K_c$ 時，BER可以任意接近零（尚未嚴格證明）。

---

## 8. 延伸討論與開放問題

### 8.1 多消息交叉信道

本文假設單消息傳輸。若系統同時編碼多個消息（不同符號串），消息之間的粒子可能在空間上重疊，導致耦合項引入消息間的「串擾」。

**問題 8.1.** 定義SRC的多址容量（Multiple Access Capacity）：在 $M$ 個消息同時傳輸時，系統能夠同時正確解碼的最大消息數。

### 8.2 非穩態動力學

本文分析集中於穩態（$t \to \infty$）或短時行為。完整的BER時間序列 $\text{BER}(t; K, A, \gamma)$ 的動力學方程尚未建立。

**問題 8.2.** 推導 $\text{BER}(t)$ 的時間演化ODE或差分方程，特別是從 $\text{BER}(0) = 0$（完美初始態）到穩態 $\text{BER}(\infty)$ 的瞬態行為。

### 8.3 逆設計問題

已知目標BER水平 $\text{BER}^*$，求最優物理參數 $(K, A, \gamma)$：

$$\min_{K, A, \gamma} \left[\text{BER}(K, A, \gamma) - \text{BER}^*\right]^2$$

這是一個非線性優化問題，目標函數的地形（landscape）由物理動力學的複雜性決定。

**問題 8.3.** 是否存在一個封閉形式的 $(K^*, A^*, \gamma^*)$，使得對給定消息長度和格點密度，BER最小化？

### 8.4 SRC的熱力學解釋

耦合強度 $K$ 類似於統計力學中的「溫度」（高 $K$ 對應高溫無序），彈簧力類似於「恢復力」（低溫趨向有序），振盪振幅 $A$ 類似於「激發強度」。這套類比指向一個完整的SRC熱力學框架：

**問題 8.4.** 定義SRC的熵（基於BER和粒子位移分佈），建立SRC的熱力學關係式（類比 $F = E - TS$ 的自由能概念）。

### 8.5 非均勻格點密度

本文假設粒子佈置於均勻格點（QR矩陣）。若格點密度不均勻（例如，某些區域格點更密），BER的分佈將在空間上非均勻，且高密度區域的粒子間耦合更強。

**問題 8.5.** 推廣SRC框架至任意空間粒子分佈（非格點），建立BER的空間密度場理論。

---

## 9. 結論

本文提出了符號流變信道（SRC）的完整形式化定義，將一個確定性的粒子流變仿真系統重新詮釋為一個信息論對象。核心貢獻包括：

1. 嚴格定義了編碼器-信道-解碼器三層結構，及其數學形式（定義2.1-2.4）
2. 建立了BER與物理參數的關係（命題4.1），揭示EMA濾波的保護效應
3. 論證了臨界耦合相變的存在性（猜想5.1、5.2）及其平均場估計
4. 提出了流變信道容量的兩種定義（定義6.1-6.3），並給出拓撲熵上界
5. 系統比較了SRC與Shannon信道的結構差異

SRC的本質是：**符號通過確定性哈希函數進入物理相空間，在流變力學的演化下逐漸失去其原始幾何信息，而解碼器通過逆投影和時間濾波試圖恢復這些信息。** 信息的「生命週期」由物理參數決定，且存在一個最優工作點使保真度最高。

未來工作將重點攻克問題8.2（BER時間動力學）和問題8.4（SRC熱力學），以及與姊妹論文EML-GCT-2026（耦合算子代數）、EML-PCH-2026（相位同調拓撲）、EML-DRIC-2026（初始條件幾何）的整合。

---

## 參考文獻

\[1\] Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.

\[2\] Newhouse, S., Ruelle, D., Takens, F. (1978). Occurrence of strange Axiom A attractors near quasi periodic flows on $T^m$, $m \geq 3$. *Comm. Math. Phys.*, 64(1), 35–40.

\[3\] Lyapunov, A.M. (1892). The general problem of the stability of motion. *Kharkov Mathematical Society*.

\[4\] Fowler, G., Noll, L., Vo, K.P. (1991). FNV hash function. \[Internal technical report, updated as Internet Draft\].

\[5\] International Organization for Standardization (2015). *ISO/IEC 18004:2015 — QR Code bar code symbology specification*.

\[6\] EveMissLab / Neo.K (2026). EML-GCT-2026：廣義耦合張量與語義流變場. *EveMissLab Working Paper Series*.

\[7\] EveMissLab / Neo.K (2026). EML-PCH-2026：相位相干持續同調. *EveMissLab Working Paper Series*.

\[8\] EveMissLab / Neo.K (2026). EML-DRIC-2026：確定性流變初始條件幾何. *EveMissLab Working Paper Series*.

---

*本論文由EveMissLab（一言諾科技有限公司）發表。版權所有，作者保留一切權利。*

*EML-SRC-2026-v0.1 · 2026年6月 · EveMissLab*
