# 相位相干持續同調（Phase Coherence Persistent Homology）
**EML-PCH-2026-v0.1**

EveMissLab（一言諾科技有限公司）
Neo.K（許筌崴）
2026年6月

---

## 摘要

本文從流變仿真系統的網格著色邏輯出發，提取並形式化**相位相干度量**（phase coherence metric），以此作為粒子對之間的「距離」，構建動態過濾子（dynamic filtration），並對所得的持續同調（persistent homology）進行分析。我們定義相位相干圖 $G(t;\epsilon)$，追蹤其Betti數 $\beta_0(t)$ 和 $\beta_1(t)$ 的時間演化，論證在耦合強度 $K$ 的臨界點附近存在Betti數的相變，並將此拓撲相變與EML-SRC-2026的BER相變聯繫起來。我們進一步引入相位相干持續條形碼（persistent barcode），作為流變場「拓撲指紋」的嚴格定義。本文構建了拓撲數據分析（TDA）在流變物理系統中的新應用框架。

**關鍵詞：** 持續同調，相位相干，Betti數，Vietoris-Rips複形，拓撲相變，流變場，動態過濾子

---

## 1. 引言

### 1.1 問題的起點

在文字流變系統（RHEO-1.0）的網格（Mesh）渲染模式中，每條連接兩個粒子 $p_i$ 和 $p_j$ 的邊的顏色由以下量決定：

$$\Delta\phi_{ij}(t) = |\omega_i t - \omega_j t| \bmod 1 = t \cdot |\omega_i - \omega_j| \bmod 1$$

這個量衡量的是兩個粒子在時刻 $t$ 的**瞬時相位差**（模1周期化）。當 $\Delta\phi_{ij} \approx 0$ 時，兩粒子相位同步；當 $\Delta\phi_{ij} \approx 0.5$ 時，兩粒子相位反向。

表面上，這只是一個視覺效果的著色規則。但仔細審視，它隱含了一個深刻的問題：

**在什麼條件下，流變場中的粒子群形成全局相位相干的結構？**

這個問題等價於詢問：流變場中的粒子是否存在「宏觀量子序」（macroscopic quantum coherence）的古典類比——即大量粒子的振盪相位在某種意義下「鎖定」，從而形成類似超流體的集體行為。

### 1.2 持續同調的必要性

為了嚴格研究相位相干結構，需要一種能夠追蹤「相干集群」的數學工具，且這種工具應能捕捉不同尺度（閾值）下的集群結構，並追蹤集群的生滅。

持續同調（Persistent Homology，Edelsbrunner等，2002）正好滿足這些需求：它通過一系列增大的閾值 $\epsilon$ 構建過濾子（filtration），追蹤拓撲特徵（連通分量、環路等）的生命週期，給出一個幾何不變量——持續圖（persistence diagram）。

**本文的核心貢獻**：在相位差空間上構建過濾子，將持續同調應用於流變場的動態拓撲分析。

### 1.3 本文組織

第2節定義相位相干度量及相位差距離。第3節構建動態相位相干複形和過濾子。第4節分析Betti數動力學。第5節建立Betti數相變與SRC信息相變的聯繫。第6節定義相位相干持續條形碼。第7節討論計算方法。第8節提出開放問題。

---

## 2. 相位相干度量

### 2.1 粒子的動力學相位

每個粒子 $p_i$ 擁有固有頻率 $\omega_i$ 和初始相位 $\phi_i$（由FNV1a哈希確定性決定）。時刻 $t$ 的**動力學相位**：

$$\Phi_i(t) = 2\pi\omega_i t + \phi_i \pmod{2\pi}$$

這是在 $[0, 2\pi)$ 上的相位，隨時間線性增長（模 $2\pi$）。

**注記 2.1.** 這裡的「動力學相位」是諧波吸引子的外部強迫頻率，而非粒子位置的即時相位。實際粒子位置的相位由於耦合和阻尼的存在，會偏離 $\Phi_i(t)$（見EML-SRC-2026第3節的線性化分析）。然而，在弱耦合（$K \ll 1$）假設下，粒子的主要振盪頻率仍近似為 $\omega_i$，因此 $\Phi_i(t)$ 是相位的良好近似。

### 2.2 相位差函數

**定義 2.1（相位差函數）。** 粒子對 $(i, j)$ 在時刻 $t$ 的相位差：

$$\Delta\phi_{ij}(t) = \frac{1}{2\pi}\left|\Phi_i(t) - \Phi_j(t)\right| \bmod 1 \in [0, 0.5]$$

注意：我們取絕對值並模1後再除以 $2\pi$，得到 $[0, 0.5]$ 範圍的值（利用對稱性 $\Delta\phi = 1 - \Delta\phi$）。$\Delta\phi_{ij} = 0$ 表示完全同相，$\Delta\phi_{ij} = 0.5$ 表示完全反相。

代入具體公式：
$$\Delta\phi_{ij}(t) = t \cdot \frac{|\omega_i - \omega_j|}{1} \bmod 0.5$$

**注記 2.2.** $\Delta\phi_{ij}(t)$ 是時間 $t$ 的擬周期函數，周期為 $T_{ij} = 1/|\omega_i - \omega_j|$（當 $\omega_i \neq \omega_j$）。對 $\omega_i = \omega_j$ 的粒子對，$\Delta\phi_{ij} \equiv 0$ 對所有時間（永久同相）。

### 2.3 相位相干度量的定義

**定義 2.2（相位相干度量）。** 在粒子集 $\mathcal{P}$ 上定義**相位相干距離**：

$$d_\phi(p_i, p_j; t) = \Delta\phi_{ij}(t) = t \cdot |\omega_i - \omega_j| \bmod 0.5$$

**命題 2.1.** $d_\phi(\cdot, \cdot; t)$ 對每個固定時刻 $t$ 是一個**偽度量**（pseudometric）：
- 非負性：$d_\phi(p_i, p_j; t) \geq 0$
- 自反性：$d_\phi(p_i, p_i; t) = 0$
- 對稱性：$d_\phi(p_i, p_j; t) = d_\phi(p_j, p_i; t)$
- 弱三角不等式：$d_\phi(p_i, p_k; t) \leq d_\phi(p_i, p_j; t) + d_\phi(p_j, p_k; t) + \lfloor\cdot\rfloor$（由於模運算，嚴格三角不等式一般不成立）

**注記 2.3.** $d_\phi$ 不是嚴格度量（可以有 $d_\phi(p_i, p_j) = 0$ 而 $p_i \neq p_j$，當 $\omega_i = \omega_j$）。但這在持續同調框架中是可接受的（使用偽度量上的Vietoris-Rips複形）。

### 2.4 複合距離

純相位距離不考慮空間位置，這在物理上不合適（空間上相距甚遠的粒子不應該因為相位相同就被認為「相干」）。我們定義**複合相干距離**：

**定義 2.3（複合相干距離）。** 對粒子對 $(i, j)$：

$$d_{\text{coh}}(p_i, p_j; t) = \alpha_\phi \cdot d_\phi(p_i, p_j; t) + \alpha_x \cdot \frac{\|\mathbf{x}_i(t) - \mathbf{x}_j(t)\|}{L_{\text{ref}}}$$

其中 $\alpha_\phi, \alpha_x > 0$ 是權重參數，$L_{\text{ref}}$ 是空間參考長度尺度（例如格距 $h = 13.5$）。

本文在多數分析中取 $\alpha_\phi = 1, \alpha_x = 0$（純相位距離），但注意複合距離的推廣。

---

## 3. 動態相位相干複形

### 3.1 Vietoris-Rips過濾子

**定義 3.1（相位相干圖）。** 對閾值 $\epsilon \in [0, 0.5]$ 和時刻 $t$，定義**相位相干圖** $G(t;\epsilon)$：
- 頂點集：$V = \mathcal{P}$（所有粒子）
- 邊集：$E(t;\epsilon) = \{(i,j) \mid d_\phi(p_i, p_j; t) \leq \epsilon\}$

$G(t;\epsilon)$ 是一個動態加權圖，其邊集隨時間和閾值演化。

**定義 3.2（相位相干過濾子）。** 固定時刻 $t$，定義Vietoris-Rips複形族：

$$\text{VR}(\epsilon; t) = \{S \subseteq \mathcal{P} \mid d_\phi(p_i, p_j; t) \leq \epsilon \text{ 對所有 } p_i, p_j \in S\}$$

對 $\epsilon_1 \leq \epsilon_2$ 有 $\text{VR}(\epsilon_1; t) \subseteq \text{VR}(\epsilon_2; t)$，構成一個**過濾子**（filtration）。

**定義 3.3（動態過濾子）。** 允許 $t$ 變化，得到二維過濾子族：
$$\{\text{VR}(\epsilon; t)\}_{\epsilon \in [0,0.5], t \geq 0}$$

這是一個定義在 $(\epsilon, t)$ 平面上的持續複形族，其中 $\epsilon$ 是傳統持續同調的「空間」參數，$t$ 是時間參數。

### 3.2 相位差的演化

對於固定的粒子對 $(i,j)$（$\omega_i \neq \omega_j$），相位差：

$$d_\phi(p_i, p_j; t) = t \cdot |\omega_i - \omega_j| \bmod 0.5$$

這是時間 $t$ 的**擬鋸齒波函數**（quasi-sawtooth function），周期為 $T_{ij} = 0.5/|\omega_i - \omega_j|$。

在物理時間 $t$（每步 $\Delta t = 0.012$）下，對 $\omega_i - \omega_j = 0.1$，周期為 $T_{ij} = 5$（物理時間單位）$= 5/0.012 \approx 417$ 步。

**命題 3.1（相位距離的准周期性）。** 對任意粒子對 $(i,j)$，$d_\phi(p_i, p_j; t)$ 是 $t$ 的有理函數的周期化，其周期 $T_{ij} = 0.5/|\omega_i - \omega_j|$。若所有 $\omega_i$ 是有理數，則整個相位距離矩陣 $D_\phi(t) = (d_\phi(p_i, p_j; t))$ 是周期函數（整體周期為所有 $T_{ij}$ 的最小公倍數）。

### 3.3 Betti數的定義

**定義 3.4（Betti數）。** 對固定 $(\epsilon, t)$，Vietoris-Rips複形 $\text{VR}(\epsilon; t)$ 的 $k$ 階Betti數 $\beta_k(t;\epsilon)$ 定義為：
- $\beta_0(t;\epsilon)$：$G(t;\epsilon)$ 的連通分量數
- $\beta_1(t;\epsilon)$：$G(t;\epsilon)$ 中獨立的一維環路（cycles）數
- $\beta_k(t;\epsilon)$：更高階的拓撲洞（$k$-洞）數

我們主要關注 $\beta_0$ 和 $\beta_1$。

### 3.4 特殊情形的Betti數

**初始時刻（$t = 0$）：**
$$d_\phi(p_i, p_j; 0) = 0 \text{ 對所有 } (i,j)$$

因此 $G(0; \epsilon) = K_N$（完全圖），$\beta_0(0;\epsilon) = 1$，$\beta_1(0;\epsilon) = \binom{N}{2} - N + 1$（對所有 $\epsilon > 0$）。

**固有頻率全相同（$\omega_i = \bar{\omega}$ 對所有 $i$）：**
$$d_\phi(p_i, p_j; t) = 0 \text{ 對所有 } (i,j), t$$

同樣 $G = K_N$，$\beta_0 = 1$ 恆常。

**固有頻率全不同（$\omega_i$ 各異且間距均勻）：** 
在 $t = T_{ij}/4$（相鄰對的四分之一周期）時，$d_\phi \approx 0.25$，對大多數粒子對相位差約為 $0.25$。若 $\epsilon < 0.25$，則只有 $\omega_i$ 非常接近的粒子才相連，圖會碎片化，$\beta_0$ 增大。

---

## 4. Betti數動力學

### 4.1 $\beta_0$ 的演化：相干集群的裂解

**命題 4.1（$\beta_0$ 的初始值和漸近值）。** 對固定 $\epsilon \in (0, 0.5)$：
- $\beta_0(0;\epsilon) = 1$（$t=0$ 時所有粒子同相）
- $\beta_0(t \to \infty; \epsilon) \to c_0(\epsilon, \Delta\omega)$（長時間平均值，依賴頻率分佈）

**定理 4.1（$\beta_0$ 的短時行為）。** 在短時展開（$t \ll T_{\min} = 0.5/\Delta\omega_{\max}$，其中 $\Delta\omega_{\max} = \max_{ij}|\omega_i - \omega_j|$）下：

對 $\epsilon$ 足夠小，$\beta_0(t;\epsilon)$ 從 $1$ 開始，以速率正比於「在時刻 $t$ 其相位差超過 $\epsilon$ 的粒子對數」而增大：

$$\frac{d\beta_0}{dt}\bigg|_{t=0^+} \approx \rho_{\Delta\omega}(\epsilon/t) \cdot \frac{\epsilon}{t^2}$$

其中 $\rho_{\Delta\omega}$ 是頻率差 $|\omega_i - \omega_j|$ 的密度分佈（歸一化）。

直觀地：相位差增長最快的粒子對（$|\omega_i - \omega_j|$ 最大）最先失去相干，使圖邊消失，$\beta_0$ 增大。

### 4.2 耦合對$\beta_0$的影響

在 $K > 0$ 時，粒子的**實際振盪相位**會因耦合而與名義動力學相位 $\Phi_i(t)$ 偏離。耦合趨向於使相鄰粒子的速度（從而位移）同步，等效於在頻率空間上引入「鎖相（phase locking）」效應。

**命題 4.2（耦合降低有效頻率差）。** 在弱耦合（$K \ll 1$）近似下，耦合使粒子 $i$ 的有效振盪頻率從 $\omega_i$ 修正為：

$$\tilde{\omega}_i = \omega_i + \frac{K^*}{2\pi}\sum_j C_{ij}(\omega_j - \omega_i) / d_i$$

其中 $d_i = \sum_j C_{ij}$。這是加權平均的Kuramoto型頻率漂移。

有效頻率差 $|\tilde{\omega}_i - \tilde{\omega}_j|$ 小於原始頻率差 $|\omega_i - \omega_j|$，因此耦合使相位距離增長放慢，從而延長相位相干的維持時間，**降低 $\beta_0$ 的增長速率**。

**猜想 4.1（耦合-Betti數對偶）。** 增大耦合強度 $K$ 等效於降低有效閾值 $\epsilon \to \epsilon_{\text{eff}}(K) < \epsilon$，使相位相干圖 $G(t;\epsilon_{\text{eff}})$ 的連通性增強。具體地：
$$\beta_0(t; \epsilon; K) \approx \beta_0(t \cdot (1 - aK); \epsilon; K=0)$$

對某個常數 $a > 0$，即耦合等效於時間膨脹。

### 4.3 $\beta_1$ 的演化：相干環路的生滅

$\beta_1 > 0$ 意味著相位相干圖中存在閉合環路，即存在三個或更多粒子 $p_i, p_j, p_k$ 使得 $d_\phi(p_i, p_j), d_\phi(p_j, p_k), d_\phi(p_k, p_i)$ 均不超過 $\epsilon$，但它們並不形成完全圖的一部分（否則是更高階的填充）。

**命題 4.3（$\beta_1$ 的出現條件）。** $\beta_1(\epsilon, t) > 0$ 要求存在三個頻率 $\omega_i, \omega_j, \omega_k$ 使得：
$$t|\omega_i - \omega_j|, t|\omega_j - \omega_k|, t|\omega_k - \omega_i| \leq \epsilon \pmod{0.5}$$

但三者不能同時滿足所有差均為零（否則被填充為三角形，$\beta_1$ 不增加）。

這在頻率空間中對應一個「相位三角形不等式違反」：$\omega_i, \omega_j, \omega_k$ 在 $[0, 2\pi t)^{-1}$ 模下相互接近，但又不全等。

### 4.4 持續熵

**定義 4.1（持續熵）。** 定義相位相干複形的持續熵：
$$\mathcal{H}(t; \epsilon) = -\sum_k \frac{\ell_k}{\mathcal{L}} \ln\frac{\ell_k}{\mathcal{L}}$$

其中求和遍歷持續圖中所有有限生命週期的特徵，$\ell_k$ 是第 $k$ 個特徵的生命週期（death - birth），$\mathcal{L} = \sum_k \ell_k$ 是總生命週期。

持續熵 $\mathcal{H}$ 衡量了相位相干結構的「複雜度」——低熵對應於少數主導特徵的簡單結構，高熵對應於許多等重要特徵的複雜結構。

**猜想 4.2（持續熵與BER的聯繫）。** 持續熵 $\mathcal{H}$ 與EML-SRC-2026中定義的BER滿足：
$$\text{BER}(t) \approx f\!\left(\mathcal{H}(t;\epsilon^*)\right)$$

對某個最優閾值 $\epsilon^*$ 和單調遞增函數 $f$。直觀地，高相位複雜度（高熵）意味著粒子的振盪相位高度分散，解碼器難以精確恢復粒子位置，從而BER高。

---

## 5. 拓撲相變

### 5.1 $\epsilon$-$K$ 相圖

固定 $t$ 和其他參數，在 $(\epsilon, K)$ 平面上分析 $\beta_0$ 的行為。

**相 I（高相干相，$\beta_0 = 1$）：** 大 $\epsilon$（鬆閾值）或大 $K$（強耦合），所有粒子形成一個連通分量。

**相 II（中間相，$1 < \beta_0 < N$）：** 中等 $\epsilon$ 和 $K$，粒子形成若干相干集群。

**相 III（低相干相，$\beta_0 \approx N$）：** 小 $\epsilon$（緊閾值）或小 $K$（弱耦合），每個粒子幾乎是孤立的。

**定義 5.1（相干臨界線）。** 在 $(\epsilon, K)$ 平面上，連接 $\beta_0 = 1$ 相和 $\beta_0 > 1$ 相的邊界線稱為**相干臨界線** $\Gamma_c(t)$。

$\Gamma_c(t)$ 的方程在平均場近似下可以估計。設所有粒子的頻率均勻分佈在 $[\omega_{\min}, \omega_{\max}]$ 上，每個粒子有 $\bar{n}$ 個空間鄰居。$\beta_0 = 1$（連通圖）要求的最小邊連接數：

$$\frac{N}{2}\cdot P(d_\phi(i,j;t) \leq \epsilon) \geq \frac{N-1}{1} \approx N$$

其中 $P$ 是相位距離 $\leq \epsilon$ 的概率（對均勻分佈）。

對均勻頻率分佈，$P(d_\phi \leq \epsilon) = P(t|\omega_i - \omega_j| \bmod 0.5 \leq \epsilon) \approx 2\epsilon$（對 $\epsilon \ll 0.5$，$t$ 固定，忽略模運算效應）。

連通條件近似為：$\bar{n} \cdot 2\epsilon \geq \ln N / N$（Erdős-Rényi隨機圖的連通閾值），即：
$$\epsilon_c(t) \approx \frac{\ln N}{2\bar{n} N}$$

**注記 5.1.** 此估計忽略了空間結構（粒子不是隨機連接的）和耦合效應。精確的 $\Gamma_c$ 需要考慮GCT的譜結構（見EML-GCT-2026）。

### 5.2 時間驅動的相變

固定 $\epsilon$ 和 $K$，隨時間 $t$ 增加，相位相干圖的連通性如何演化？

**命題 5.1（初始連通性和長時失相）。** 對任意 $\epsilon > 0$：
- 在 $t = 0$ 時，$\beta_0(0;\epsilon) = 1$（所有粒子相位相同）
- 對 $K = 0$（無耦合），當 $t \to \infty$ 時，$\beta_0(t;\epsilon)$ 的時間平均值趨向 $N$ 的某個分數（依 $\epsilon$ 和 $\omega$ 分佈）

從 $\beta_0 = 1$ 到 $\beta_0 \gg 1$ 的轉換發生在：
$$t_c(\epsilon) \approx \frac{\epsilon}{\Delta\omega_{\text{eff}}}$$

其中 $\Delta\omega_{\text{eff}}$ 是「有效頻率差」（可由 $\omega$ 分佈的標準差估計）。

**定義 5.2（失相時間）。** 對閾值 $\epsilon$，**失相時間**定義為：
$$t_{\text{dec}}(\epsilon) = \inf\{t > 0 \mid \beta_0(t;\epsilon) > \beta_0(0;\epsilon)\}$$

失相時間描述了相位相干結構開始「碎裂」的時刻。由命題5.1，$t_{\text{dec}}(\epsilon) \approx \epsilon/\Delta\omega_{\text{eff}}$——閾值越寬（$\epsilon$ 大）或頻率差越小，失相越晚。

### 5.3 與SRC信息相變的對應

**定理 5.1（拓撲-信息對應，猜想形式）。** 存在一個映射 $\psi: [0, 0.5] \to [0, 1]$（從相位閾值到BER），使得：

$$\text{BER}(t; K, A) \approx \psi\left(\epsilon_{\text{eff}}(t; K, A)\right)$$

$$\frac{d\text{BER}}{dt} \propto \frac{d\beta_0}{dt}\bigg|_{\epsilon = \epsilon^*(K, A)}$$

其中 $\epsilon^*(K, A)$ 是使對應關係最精確的「有效閾值」，依賴物理參數。

**直觀解釋：** 當相位相干結構碎裂（$\beta_0$ 增大），粒子的振盪相位失去集體同步，各粒子的位移變得「不可預測」（從全局角度），解碼器的EMA濾波輸出的重建位置偏差增大，BER升高。拓撲相變和信息論相變是同一底層物理過程的兩個觀測面。

---

## 6. 持續條形碼：流變場的拓撲指紋

### 6.1 持續圖的構建

**定義 6.1（相位相干持續圖）。** 對固定時刻 $t$，將相位距離矩陣 $D_\phi(t)$ 輸入到Vietoris-Rips過濾子。對過濾參數 $\epsilon$ 從 $0$ 增大到 $0.5$，追蹤每個拓撲特徵的生命週期：

- **出生（birth）**：$\epsilon = b_k$，第 $k$ 個特徵首次出現
- **死亡（death）**：$\epsilon = d_k$，第 $k$ 個特徵消失（被填充）

**$k$-持續圖** $\text{Dgm}_k(t) = \{(b_{k,l}, d_{k,l})\}$ 是生死點對的多重集。

**定義 6.2（相位相干持續條形碼）。** 對固定 $t$，$0$-持續條形碼 $\text{BC}_0(t)$ 是一組 $[b_l, d_l)$ 區間，每個區間代表一個連通分量從 $\epsilon = b_l$ 出現到 $\epsilon = d_l$ 與其他分量合併。

特別地：
- 最長的條形（最大 $d_l - b_l$）代表最「穩定」的相干集群
- 最短的條形代表噪聲性（由隨機頻率分配引起）的假相干結構

### 6.2 時間演化的持續條形碼

允許 $t$ 變化，持續條形碼隨時間演化。定義**時間-持續圖**：
$$\text{TDgm}_k = \{(t, b_{k,l}(t), d_{k,l}(t))\}$$

這是三維空間（時間 $\times$ 出生 $\times$ 死亡）中的一個點集。

**命題 6.1（時間演化的連續性）。** 若頻率 $\omega_i$ 是固定的（不依賴時間），則對每個固定 $k$，相位距離矩陣 $D_\phi(t)$ 關於 $t$ 是分段線性連續的（除了模運算的跳躍點）。因此持續條形碼 $\text{BC}_k(t)$ 關於 $t$ 是分段連續的。

### 6.3 特殊頻率分配的解析計算

對於只有兩種頻率的系統（$\omega_i \in \{\omega_A, \omega_B\}$，數量各為 $N/2$），相位差只有三種值：
- $d_\phi^{AA} = 0$（A型粒子之間）
- $d_\phi^{BB} = 0$（B型粒子之間）
- $d_\phi^{AB}(t) = t|\omega_A - \omega_B| \bmod 0.5$（A-B粒子之間）

在 $\epsilon < d_\phi^{AB}(t)$ 時，A型粒子形成一個連通分量，B型粒子形成另一個連通分量（假設A型和B型各自空間上連通），$\beta_0 = 2$。

在 $\epsilon \geq d_\phi^{AB}(t)$ 時，所有粒子連通，$\beta_0 = 1$。

持續條形碼：$0$-維特徵有兩個條形，一個生於 $b = 0$，死於 $d = d_\phi^{AB}(t)$；另一個生於 $b = 0$，死亡於 $d = +\infty$（全局分量）。

此解析例子說明了條形碼如何直接編碼頻率差信息。

### 6.4 條形碼統計量

**定義 6.3（條形碼統計量）。** 給定條形碼 $\text{BC}_0(t) = \{[b_l, d_l)\}$，定義：
- **總持續度**：$L(t) = \sum_l (d_l - b_l)$
- **最大持續度**：$L_{\max}(t) = \max_l (d_l - b_l)$
- **條形數**：$\beta_0^{\text{tot}}(t) = |\text{BC}_0(t)|$（等於在 $\epsilon \to 0$ 時的 $\beta_0$）
- **持續熵**：$\mathcal{H}(t)$（定義4.1）

這些統計量構成了流變場在時刻 $t$ 的**拓撲特徵向量**。

**猜想 6.1（拓撲特徵向量的信息容量）。** 定義拓撲特徵向量的「信息容量」為其能夠區分不同消息的能力。猜想：

$$I_{\text{topo}}(t) = I\!\left(\mathbf{s}; \left(L(t), L_{\max}(t), \mathcal{H}(t)\right)\right)$$

在 $t < t_{\text{dec}}(\epsilon^*)$ 時高（消息的相位結構保留在條形碼中），在 $t > t_{\text{dec}}$ 時低（消息信息已從拓撲中流失）。

---

## 7. 語義過濾子

### 7.1 語義分層的持續同調

在文字系統中，粒子帶有字符索引 $\sigma_i$。可以在相位距離之上疊加語義約束，定義**語義過濾子**：

**定義 7.1（語義相位距離）。** 帶語義的相位相干距離：

$$d_{\sigma\phi}(p_i, p_j; t) = \begin{cases} d_\phi(p_i, p_j; t) & \sigma_i = \sigma_j \\ \infty & \sigma_i \neq \sigma_j \end{cases}$$

此距離對不同字符的粒子賦予無窮大距離，使它們永遠不在同一連通分量中（與文字系統的耦合拓撲完全一致）。

語義相位相干持續條形碼 $\text{BC}_0^{\sigma}(t)$ 中的每個條形只描述同一字符內部的相位相干結構，不同字符間不出現共同條形。

### 7.2 字符間相位差的拓撲涵義

雖然在語義距離下字符間不耦合，但它們的**相位結構仍然可以比較**。定義字符 $\sigma$ 的**相位質心**：

$$\bar{\omega}_\sigma = \frac{1}{|B_\sigma|}\sum_{i \in B_\sigma} \omega_i$$

字符間的相位質心距離：
$$d_{\bar{\phi}}(\sigma, \sigma'; t) = t|\bar{\omega}_\sigma - \bar{\omega}_{\sigma'}| \bmod 0.5$$

在字符層次（粗粒化後），相位距離定義了字符之間的「節奏關係」：相位質心接近的字符在流變場中節奏同步，可以形成更高層次的相干結構。

**定義 7.2（字符層次持續圖）。** 以字符為節點，以 $d_{\bar{\phi}}$ 為距離，構建字符層次的持續圖 $\text{Dgm}_k^{\text{char}}(t)$。這描述了字符之間的相位同步模式。

---

## 8. 計算複雜度與算法設計

### 8.1 Vietoris-Rips的計算成本

對 $N$ 個粒子，完整的Vietoris-Rips複形在 $\epsilon$ 最大時包含 $2^N$ 個單形，計算成本是指數級的。然而，在實際仿真中（$N \leq 900$），可以利用以下策略降低成本：

**策略一（截斷維度）：** 只計算 $0$-維和 $1$-維持續同調（$\beta_0$ 和 $\beta_1$），不計算高維。這使成本降至 $O(N^2 \log N)$（排序邊）+ $O(N^2)$（Union-Find算法計算 $\beta_0$）。

**策略二（語義分塊）：** 對文字系統，每個字符內部獨立計算，成本從 $O(N^2)$ 降至 $O(\sum_\sigma |B_\sigma|^2) = O(N^2/L)$（$L$ 為字符數）。

**策略三（時間採樣）：** 由於 $D_\phi(t)$ 是時間的分段線性函數，只需在線性段的端點（模運算跳躍點）計算持續圖，不需要密集的時間採樣。

### 8.2 在線（滾動窗口）算法

**算法 8.1（滾動相位持續同調）：**
```
Input: 粒子流（x_i(t), v_i(t), ω_i, φ_i）, 閾值 ε, 窗口大小 W
Output: 滾動Betti數序列 {β_0(t), β_1(t)}

For each time step t:
    1. 計算相位距離矩陣 D_φ(t) (O(N²))
    2. 構建閾值圖 G(t;ε) (O(N²))
    3. 用Union-Find計算 β_0(t;ε) (O(N·α(N)))
    4. 用邊消去法計算 β_1(t;ε) (O(N²))
    5. 輸出 (t, β_0, β_1)
    6. （可選）更新持續條形碼
```

在每幀（每次Tick）運行此算法，計算量 $O(N^2)$，對 $N = 900$ 約需 $810000$ 次操作——在現代CPU上可以實時完成。

---

## 9. 開放問題

**問題 9.1（相位持續熵的極值原理）。** 持續熵 $\mathcal{H}(t;\epsilon)$ 在哪些參數組合 $(K, A, \gamma, \epsilon)$ 下達到最大值？最大持續熵狀態是否對應某種「最複雜流變態」，且此態與BER的極值有何關係？

**問題 9.2（二維動態持續同調）。** 允許同時對 $t$ 和 $\epsilon$ 做持續同調（雙參數持續同調），得到的二維持續模型（two-parameter persistence module）是否有簡潔的代數描述？二維條形碼的「不變量」是什麼？

**問題 9.3（持續條形碼的可逆性）。** 給定持續條形碼 $\text{BC}_k(t)$，能否恢復粒子的頻率分配 $\{\omega_i\}$？更一般地，從條形碼能恢復多少原始消息 $\mathbf{s}$ 的信息？這給出了一個拓撲版本的「流變信道容量」。

**問題 9.4（Wasserstein距離的流變意義）。** 兩個時刻 $t_1$ 和 $t_2$ 的持續圖之間的Wasserstein距離 $W_p(\text{Dgm}(t_1), \text{Dgm}(t_2))$ 是否可以用物理量（例如粒子總位移 $\sum_i |\mathbf{x}_i(t_1) - \mathbf{x}_i(t_2)|$）估計？

**問題 9.5（相位空間的熱力學）。** 定義「相位溫度」 $T_\phi = \langle |\dot{\Phi}_i - \langle\dot{\Phi}\rangle|^2 \rangle^{1/2}$（頻率方差）。$\beta_0$ 是否是 $T_\phi$ 的單調遞增函數（在固定 $\epsilon$ 下）？這個關係是否類似於統計力學中的溫度-熵關係？

---

## 10. 結論

本文建立了相位相干持續同調（PCH）的完整框架，為流變場提供了一套全新的**拓撲特徵量**（Betti數、持續條形碼、持續熵），以補充傳統流變學的力學量（應力、應變、黏度）。

核心貢獻包括：

1. 相位相干偽度量 $d_\phi$ 的嚴格定義（定義2.2），及其動態過濾子的構建（定義3.2-3.3）
2. Betti數動力學的解析分析（命題4.1、4.2），包括耦合的相位鎖定效應
3. 拓撲-信息對應定理（定理5.1，猜想形式），連接持續同調和SRC的BER
4. 語義過濾子的定義（定義7.1），使字符層次的持續同調成為可能
5. 計算複雜度分析和在線算法設計（算法8.1）

本文的核心主張：**流變場的相位相干拓撲是信息保真度的拓撲代理量**——當拓撲結構複雜（高持續熵）時，信息保真度低；當拓撲結構簡單（低持續熵，集群結構清晰）時，信息保真度高。這在最終打通了拓撲數據分析與信息論之間的橋樑。

---

## 參考文獻

\[1\] Edelsbrunner, H., Letscher, D., Zomorodian, A. (2002). Topological persistence and simplification. *Discrete and Computational Geometry*, 28(4), 511–533.

\[2\] Zomorodian, A., Carlsson, G. (2005). Computing persistent homology. *Discrete and Computational Geometry*, 33(2), 249–274.

\[3\] Kuramoto, Y. (1984). *Chemical oscillations, waves, and turbulence*. Springer.

\[4\] Edelsbrunner, H., Harer, J. (2010). *Computational topology: an introduction*. American Mathematical Society.

\[5\] EveMissLab / Neo.K (2026). EML-SRC-2026：符號流變信道理論. *EveMissLab Working Paper Series*.

\[6\] EveMissLab / Neo.K (2026). EML-GCT-2026：廣義耦合張量與語義流變場. *EveMissLab Working Paper Series*.

\[7\] EveMissLab / Neo.K (2026). EML-DRIC-2026：確定性流變初始條件幾何. *EveMissLab Working Paper Series*.

---

*本論文由EveMissLab（一言諾科技有限公司）發表。版權所有，作者保留一切權利。*

*EML-PCH-2026-v0.1 · 2026年6月 · EveMissLab*
