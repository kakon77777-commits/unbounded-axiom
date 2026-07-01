# 環面幾何預處理框架：週期性資料的拓撲正確處理方法

**Toroidal Geometric Preprocessing Framework: Topologically Correct Treatment of Periodic Data**

作者：Neo.K（許筌崴）× Theia  
隸屬：EveMissLab（一言諾科技有限公司）  
日期：2026 年 4 月 25 日（v2 修訂：去除未驗證的深度學習實驗聲明）  
文件編號：EML-AI-2026-ToroidalGTC-Preprocessing-v2  
分類：幾何資料處理 · 訊號處理 · 拓撲預處理

---

## 摘要

現有資料處理框架普遍假設資料定義在歐氏空間 ℝⁿ 上，這對天然具有週期性的資料（全景影像、地球表面資料、可平鋪紋理、週期性時間序列）造成系統性的邊界錯誤。本文基於幾何環面微積分（Geometric Toroidal Calculus, GTC）提出一個統一的預處理框架，核心主張為：**週期性資料的正確幾何表示是環面 T² = S¹ × S¹，而非歐氏空間 ℝ²**。

本框架的貢獻分為兩層：

其一，理論層：從 GTC 第一性原理出發，證明對週期性資料使用歐氏邊界處理（zero padding、reflect padding 等）是拓撲錯誤的。環面表示不是一種工程選擇，而是資料幾何的必然要求。

其二，實作層：提供 circular FFT 分析、toroidal 距離計算、週期性插值等具體工具，適用於任何下游方法——統計分析、傳統機器學習、或深度學習——無需針對特定架構設計。

本文的數值驗證基於可執行的數學計算（詳見附錄一）。針對真實資料集（ERA5 氣候數據、全景影像、可平鋪紋理）的完整對比分析，留待附錄二補充（待資料獲取後完成）。

**關鍵字**：幾何環面微積分 · 週期性資料預處理 · 拓撲正確性 · circular FFT · toroidal 距離 · GTC

---

## 1. 問題陳述

### 1.1 週期性資料的系統性錯誤

下表列出常見週期性資料及傳統處理方式造成的具體錯誤：

| 資料類型 | 週期維度 | 真實拓撲 | 傳統錯誤 |
|:---------|:--------|:--------|:--------|
| 全景影像（360°） | 水平方向 | 圓柱 S¹×ℝ | 左右邊界被視為不連續 |
| 地球氣候場 | 經度方向 | 球面 S²（經度週期） | 0°/360° 插值/分析斷裂 |
| 可平鋪紋理 | 雙向 | 環面 T² | 四邊界偽影 |
| 日週期時間序列 | 時間 | 圓 S¹ | 0:00/23:59 統計斷裂 |
| 晶體 k 空間 | 三維 | 三維環面 T³ | 布里淵區邊界錯誤 |

這些錯誤不因使用更複雜的模型而消失，而是以系統性偏差的形式持續存在於下游結果中。

### 1.2 核心主張

本文的主張可以用一句話表達：

> **當資料的生成過程在週期邊界處是連續的，任何在該邊界處引入不連續性的預處理都是錯誤的。**

這不是一個效能主張（「準確率提升 X%」），而是一個拓撲主張：邊界條件的選擇不是工程上的調參，而是對資料幾何本質的陳述。

---

## 2. 理論基礎：GTC 框架

### 2.1 環面流形

**定義 2.1（二維環面）**

$$T^2 = S^1 \times S^1 = \{(\theta_1, \theta_2) \mid \theta_1, \theta_2 \in [0, 2\pi)\}$$

關鍵拓撲性質：

- **無邊界**：$\partial T^2 = \emptyset$，即環面上不存在「邊緣」
- **緊致性**：有界且閉合
- **基本群**：$\pi_1(T^2) = \mathbb{Z} \times \mathbb{Z}$，表示兩個獨立的環形纏繞方向

**定義 2.2（環面上的函數）**

函數 $f: T^2 \to \mathbb{R}$ 的雙週期條件：

$$f(\theta_1 + 2\pi, \theta_2) = f(\theta_1, \theta_2), \quad f(\theta_1, \theta_2 + 2\pi) = f(\theta_1, \theta_2)$$

這不是約束，而是定義——在 $T^2$ 上，$(0, \theta_2)$ 和 $(2\pi, \theta_2)$ 是同一個點。

### 2.2 環面上的積分與 Stokes 定理

**定理 2.1（環面積分的自動閉合性）**

對任意 $f \in L^2(T^2)$，其純振盪分量（零均值 Fourier 模式）的環面積分自動為零：

$$\iint_{T^2} f(\theta_1, \theta_2)\, d\theta_1 d\theta_2 = 0 \quad \text{（若 } f \text{ 無零頻分量）}$$

**推論（Stokes 定理的拓撲必然性）**

由於 $\partial T^2 = \emptyset$，Stokes 定理給出：

$$\oint_{\partial T^2} \omega = 0$$

這意味著在環面上，沒有「邊界項」。任何假設存在邊界項的處理方式（如 zero padding 引入的人工不連續）都與環面的拓撲結構矛盾。

### 2.3 環面 Fourier 分析

**定理 2.2（環面的 Fourier 展開）**

$T^2$ 上的函數可展開為：

$$f(\theta_1, \theta_2) = \sum_{m,n \in \mathbb{Z}} c_{mn} e^{i(m\theta_1 + n\theta_2)}$$

係數 $c_{mn} = \frac{1}{4\pi^2} \iint_{T^2} f(\theta_1, \theta_2) e^{-i(m\theta_1 + n\theta_2)} d\theta_1 d\theta_2$

**計算意涵**：對週期性資料直接應用標準 FFT（假設週期邊界）是正確的。若資料實際上是週期的，則 circular FFT 在頻譜分析上不產生 Gibbs 現象；zero-padding FFT 則在邊界不連續處引入虛假的高頻成分。

### 2.4 GTC 作為 Peter-Weyl 定理在 $T^n$ 上的特例

GTC 的 Fourier 分析在代數層面有更深的根基：它是 **Peter-Weyl 定理**在交換緊緻 Lie 群 $T^n$ 上的特殊情形。本節明示這個關係，並以此劃定 GTC 的適用邊界。

**定理 2.3（Peter-Weyl，緊緻 Lie 群版本）**

設 $G$ 為緊緻 Lie 群，$L^2(G)$ 為其上的平方可積函數空間。則 $L^2(G)$ 可分解為所有不可約么正表示（IRR）的直和：

$$L^2(G) \cong \bigoplus_{\rho \in \hat{G}} V_\rho \otimes V_\rho^*$$

其中 $\hat{G}$ 為 $G$ 的對偶（所有 IRR 的等價類）。

**推論 2.1（$T^n$ 的特例）**

$T^n = (S^1)^n$ 是交換緊緻 Lie 群，其所有 IRR 均為一維。$T^n$ 的對偶群為 $\hat{T}^n \cong \mathbb{Z}^n$，每個 IRR 對應一個特徵標：

$$\chi_{\mathbf{k}}(\boldsymbol{\theta}) = e^{i \mathbf{k} \cdot \boldsymbol{\theta}}, \quad \mathbf{k} \in \mathbb{Z}^n$$

Peter-Weyl 定理在此退化為：

$$L^2(T^n) = \overline{\bigoplus_{\mathbf{k} \in \mathbb{Z}^n} \mathbb{C} \cdot e^{i\mathbf{k} \cdot \boldsymbol{\theta}}}$$

這正是 $T^n$ 上的多重 Fourier 展開。

**GTC 操作的表示論對應**：

| GTC 操作 | 表示論語言 |
|:--------|:---------|
| Fourier 基底 $e^{in\theta}$ | $S^1$ 的不可約表示（IRR） |
| Parseval 定理（能量守恆） | IRR 的正交性（Schur 引理） |
| 卷積定理（頻域逐點乘積） | 群代數上的特徵標乘法 |
| circular padding 的正確性 | 群作用的等變性（equivariance） |
| 無邊界項（$\partial T^n = \emptyset$） | 緊緻群上積分的不變性 |

**結論**：GTC 框架在 $T^n$（即 $S^1$ 的 $n$ 次乘積）上的所有操作，均可從 Peter-Weyl 定理嚴格導出。GTC 不是獨立的公設系統，而是表示論在交換緊緻群上的微積分語言。

**非交換推廣（留待未來工作）**

當封閉系統的對稱群為**非交換緊緻 Lie 群**時，Peter-Weyl 定理仍然成立，但 IRR 不再是一維的：

| 群 $G$ | IRR 維度 | Fourier 類比 | 應用 |
|:------|:--------|:-----------|:-----|
| $S^1, T^n$ | 1（交換） | 標準 Fourier 分析 | GTC 現有框架 |
| $SO(3)$ | $2l+1$（$l \in \mathbb{N}$） | 球諧函數 $Y_l^m$ | 球面資料 |
| $SE(3)$ | 無窮維（矩陣值） | Wigner D-矩陣 | 剛體運動 |
| 一般緊緻 $G$ | 有限維（Schur） | Peter-Weyl 展開 | 一般封閉流形 |

對這些情形，卷積核必須是矩陣值函數，Fourier 分析需要 Clebsch-Gordan 係數處理表示的張量積。本文的 GTC 框架不處理非交換情形。附錄三的猜想 C.1 在 $S^1$ 和 $T^n$ 結構的系統上嚴格成立；對具有非交換對稱群的系統，推廣有效性依賴上述非交換表示論的建立，留待未來工作。

---

## 3. 預處理框架

### 3.1 框架結構

GTC 預處理框架的輸入-輸出定義如下：

**輸入**：具有已知週期結構的原始資料（影像、時間序列、場數據等）  
**輸出**：保持週期拓撲的表示，可直接送入任意下游分析方法

框架由三個操作層組成：

**層一：拓撲識別**——判斷資料哪些維度具有週期性，確定對應的 $S^1$ 結構。

**層二：環面表示**——在周期維度上應用 circular 邊界條件，確保所有操作（插值、梯度估計、卷積、FFT）都在 $T^2$ 上進行。

**層三：度量修正**——在週期維度上使用 toroidal 距離而非歐氏距離：

$$d_T(\theta_a, \theta_b) = \min(|\theta_a - \theta_b|, 2\pi - |\theta_a - \theta_b|)$$

### 3.2 具體工具

**工具 A：Circular FFT 分析**

對週期維度直接使用 `numpy.fft.fft`（隱式假設週期邊界）。禁止在分析前對週期方向做 zero-padding 延伸，否則引入虛假的邊界頻譜。

應用場景：全景影像的水平方向頻譜分析、氣候場的經向 Fourier 分解。

**工具 B：環面插值**

對週期維度 $\theta$ 的插值，使用 $\cos\theta, \sin\theta$ 的線性插值後還原角度，而非直接對 $\theta$ 線性插值。這避免了 $0$ 和 $2\pi$ 附近的插值跳躍。

**工具 C：Toroidal 相似度度量**

計算兩個週期樣本的距離時，使用 $d_T$ 替換歐氏距離。適用於 k-NN、聚類、核方法等任何依賴距離的下游方法。

**工具 D：Circular Padding（應用於空間卷積）**

若下游使用卷積操作，在週期維度上使用 circular padding 而非 zero/reflect padding。詳見附錄一的驗證。

### 3.3 適用範圍

本框架的適用條件：**資料的生成過程在週期邊界處物理上連續**。

不適用情形：人為切割的影像邊界（如一張普通照片的邊緣）、非週期的時間序列終點。

錯誤使用的代價：引入在邊界處集中的系統性偏差，在頻譜上表現為虛假的高頻成分，在空間分析上表現為邊界附近的估計偏差。

---

## 4. 驗證方式

### 4.1 已完成的數學驗證（見附錄一）

以下命題已通過數值計算驗證（誤差 $< 10^{-10}$）：

1. $S^1$ 上純振盪函數的積分為零：$\oint \sin\theta\, d\theta = 0$
2. $T^2$ 上可分離週期函數的積分為零：$\iint \sin\theta_1 \cos\theta_2\, d\theta_1 d\theta_2 = 0$
3. Parseval 定理在 $S^1$ 上成立（能量守恆）
4. Circular padding 在週期邊界的邊緣檢測上給出正確結果，zero padding 在同一位置給出錯誤結果（$8 \times 8$ 數值範例）

### 4.2 待完成的資料集驗證（見附錄二，待補）

以下對比實驗待真實資料獲取後完成：

| 資料集 | 驗證目標 | 方法 |
|:-------|:--------|:-----|
| ERA5 氣候場 | 經度方向頻譜分析：circular vs. zero-padded FFT 的 Gibbs 現象對比 | Fourier 分析 |
| 全景影像 | 水平邊界處特徵連續性：toroidal vs. 歐氏距離的跨邊界匹配率 | 特徵匹配 |
| 可平鋪紋理 | 邊界偽影的定量測量 | 像素級差值統計 |

這些實驗不依賴任何神經網路訓練，計算量小，結果可在獲取資料後快速完成。

---

## 5. 討論

### 5.1 這個框架的位置

GTC 預處理框架處在資料處理管線的最前端，在任何模型或分析方法之前。它的作用是確保輸入的幾何表示與資料的物理現實一致。

這意味著它的效益不取決於下游使用何種方法：無論是傳統統計、機器學習、深度學習，或直接的信號分析，錯誤的邊界處理都會注入系統性偏差，正確的邊界處理都能消除它。

深度學習是其中一個應用場景（見附錄一中的 ToroidalConv2d 實作），但不是框架的核心。

### 5.2 與現有工作的關係

本框架的理論主張（circular boundary conditions 對週期數據是拓撲正確的）與計算物理中的週期邊界條件（PBC）、球諧 CNN 的球面處理、以及環面量子場論的邊界處理在精神上一致。

GTC 的貢獻在於：提供一個統一的微積分語言，使這些不同領域中分散的週期性處理實踐得以在同一個框架下理解和推廣。

### 5.3 誠實的局限性聲明

本文不聲明具體的效能提升數字（如「準確率提升 X%」）。這類數字依賴於具體任務、資料集、基準模型的選擇，在沒有完整實驗的情況下，任何具體數字都是估計，不應作為可重現的結果呈現。

本文的核心聲明是拓撲性的，不是效能性的：對週期性資料，環面表示在幾何上是正確的，歐氏表示在幾何上是錯誤的。這個主張不需要實驗來證明——它是定義的必然結果。

---

## 6. 結論

週期性資料的拓撲結構是環面 $T^n$，不是歐氏空間 $\mathbb{R}^n$。在資料處理的任何環節中引入與此不符的邊界假設，都是幾何錯誤，而非可調的工程參數。

GTC 框架提供了識別、表示和操作週期性資料的統一語言。其核心工具——circular FFT、toroidal 距離、circular padding——計算代價低，且適用於任何下游分析方法。

對週期性資料，選擇正確的幾何表示不是最佳化問題，而是正確性問題。

---

## 附錄一：基礎數學驗證（可執行）

> **狀態**：已驗證。所有數值結果可通過附錄代碼直接重現。

### A.1 S¹ 上的積分閉合性

```python
import numpy as np
from scipy import integrate

# ∮ sin(θ) dθ = 0
result, _ = integrate.quad(np.sin, 0, 2*np.pi)
assert abs(result) < 1e-10, f"Failed: {result}"
print(f"∮ sin(θ) dθ = {result:.2e}  ✓")

# ∮ cos(2θ) dθ = 0
result, _ = integrate.quad(lambda t: np.cos(2*t), 0, 2*np.pi)
assert abs(result) < 1e-10
print(f"∮ cos(2θ) dθ = {result:.2e}  ✓")

# ∮ 3 dθ = 6π
result, _ = integrate.quad(lambda t: 3.0, 0, 2*np.pi)
assert abs(result - 6*np.pi) < 1e-6
print(f"∮ 3 dθ = {result:.6f} ≈ 6π = {6*np.pi:.6f}  ✓")
```

### A.2 T² 上的積分閉合性

```python
from scipy.integrate import dblquad

# ∬ sin(θ₁)cos(θ₂) dθ₁dθ₂ = 0
result, _ = dblquad(lambda t2, t1: np.sin(t1)*np.cos(t2),
                    0, 2*np.pi, 0, 2*np.pi)
assert abs(result) < 1e-8
print(f"∬ sin(θ₁)cos(θ₂) = {result:.2e}  ✓")

# ∬ 1 dθ₁dθ₂ = 4π²
result, _ = dblquad(lambda t2, t1: 1.0,
                    0, 2*np.pi, 0, 2*np.pi)
assert abs(result - 4*np.pi**2) < 1e-6
print(f"∬ 1 = {result:.6f} ≈ 4π² = {4*np.pi**2:.6f}  ✓")
```

### A.3 Parseval 定理（能量守恆）

```python
N = 256
theta = np.linspace(0, 2*np.pi, N, endpoint=False)
f = np.sin(3*theta) + 0.5*np.cos(7*theta) + 0.3*np.sin(11*theta)

E_time = np.sum(f**2) / N
coeffs = np.fft.fft(f) / N
E_freq = np.sum(np.abs(coeffs)**2)

assert abs(E_time - E_freq) < 1e-12
print(f"時域能量: {E_time:.10f}")
print(f"頻域能量: {E_freq:.10f}")
print(f"差值: {abs(E_time-E_freq):.2e}  ✓")
```

### A.4 週期邊界邊緣檢測對比

```python
import numpy as np
import torch
import torch.nn.functional as F

# 8×8 週期影像：左半=1，右半=0（右邊界應能看到左半的邊緣）
img = torch.zeros(1, 1, 8, 8)
img[0, 0, :, :4] = 1.0

kernel = torch.tensor([[[[1., 0., -1.]]]])  # 水平邊緣檢測

# Zero padding（拓撲錯誤）
out_zero = F.conv2d(F.pad(img, (1,1,0,0), mode='constant', value=0),
                    kernel, padding=0)
# Circular padding（拓撲正確）
out_circ = F.conv2d(F.pad(img, (1,1,0,0), mode='circular'),
                    kernel, padding=0)

print("最右欄 col=7（應檢測到左→右的週期邊緣）：")
print(f"  Zero padding:    {out_zero[0,0,:,7].tolist()}")  # 全0，偵測失敗
print(f"  Circular padding:{out_circ[0,0,:,7].tolist()}")  # 全-1，正確偵測
```

### A.5 ToroidalConv2d 實作（已修正版本）

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class ToroidalConv2d(nn.Module):
    """環面卷積層——使用 circular padding 實現週期邊界"""
    
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, bias=True):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride
        self.weight = nn.Parameter(
            torch.randn(out_channels, in_channels, kernel_size, kernel_size)
        )
        self.bias = nn.Parameter(torch.zeros(out_channels)) if bias else None
        nn.init.kaiming_uniform_(self.weight, a=2**0.5)
    
    def forward(self, x):
        pad = self.kernel_size // 2
        x = F.pad(x, (pad, pad, pad, pad), mode='circular')
        return F.conv2d(x, self.weight, self.bias, stride=self.stride, padding=0)


class ToroidalMaxPool2d(nn.Module):
    """環面最大池化層（修正版）
    
    修正說明：non-overlapping pooling（stride >= kernel_size）
    在環面上不需要 circular pad——週期邊界對不重疊窗口無意義。
    原版對 kernel=2 加 pad=1，導致 32→17 而非 32→16。
    """
    
    def __init__(self, kernel_size, stride=None):
        super().__init__()
        self.kernel_size = kernel_size
        self.stride = stride or kernel_size
    
    def forward(self, x):
        if self.stride >= self.kernel_size:
            # Non-overlapping：不需要 circular pad
            return F.max_pool2d(x, self.kernel_size, self.stride, padding=0)
        else:
            # Overlapping：pad 必要部分
            pad = self.kernel_size - self.stride
            x = F.pad(x, (pad, pad, pad, pad), mode='circular')
            return F.max_pool2d(x, self.kernel_size, self.stride, padding=0)
```

---

## 附錄二：真實資料集完整對比分析

> **狀態**：待補。資料獲取後完成。

### 計畫實驗

**實驗 B.1：ERA5 氣候場頻譜分析**

資料來源：ERA5 全球再分析資料（公開）  
實驗設計：對經度方向分別使用 circular FFT 與 zero-padded FFT，比較邊界附近（0°/360°）的 Gibbs 振盪強度。  
預期輸出：兩者的功率譜密度圖、邊界附近的均方誤差。

**實驗 B.2：全景影像跨邊界特徵匹配**

資料來源：公開全景影像資料集  
實驗設計：提取跨越左右邊界的特徵點，比較 toroidal 距離與歐氏距離在匹配率上的差異。  
預期輸出：匹配精確率、召回率對比。

**實驗 B.3：可平鋪紋理邊界偽影**

資料來源：公開紋理資料集  
實驗設計：對可平鋪紋理在四邊拼接後測量縫隙處的像素值不連續性（zero-padding 處理 vs. circular 處理）。  
預期輸出：邊界不連續性的定量統計。

---

## 附錄三：猜想——GTC 框架在封閉性循環類物體的普遍適用性

> **狀態**：理論動機充分，未經實驗驗證。以猜想形式存檔。

**猜想 C.1（封閉性循環類物體的 GTC 適用性）**

設系統 $S$ 的狀態空間或參數空間包含至少一個拓撲封閉維度（即含 $S^1$ 因子），且 $S$ 的觀測數據沿此維度循環生成。則對 $S$ 的任何頻譜分析、距離計算或插值操作，使用 GTC 框架（circular 邊界條件、toroidal 距離度量）在拓撲上是正確的，使用歐氏邊界假設在拓撲上是錯誤的。

**猜想的理論依據**：命題直接由環面 $T^n$ 的無邊界性（$\partial T^n = \emptyset$）推出，與具體物理機制無關。只要系統的封閉結構成立，GTC 適用性即成立。

**可能的適用對象**：

| 領域 | 封閉結構來源 | 拓撲 |
|:----|:-----------|:-----|
| Floquet 量子系統（含時間晶體） | 準能量 Brillouin 區由 Floquet 定理定義 | $S^1$ |
| 生物節律（晝夜律、心跳、細胞週期） | 相位空間中的吸引子軌道 | $S^1$ |
| 化學振盪器（BZ 反應等） | 濃度空間中的極限環 | $S^1$ |
| 耦合振盪系統 | 雙相位空間 | $T^2$ |
| 旋轉機械（引擎、渦輪） | 轉角的物理封閉性 | $S^1$ |
| 動力系統的極限環 | 吸引子的拓撲定義 | $S^1$ |
| 週期性經濟指標 | 時間維度的人為週期折疊 | $S^1$（弱） |

**注意**：最後一項（經濟週期）的 $S^1$ 結構是近似的而非物理定義的，GTC 的拓撲主張在此較弱，適用性需個案評估。

**驗證路徑**：選取上表中拓撲結構最明確的系統（如 Floquet 系統的準能量譜，或生物節律的相位數據），對比 circular FFT 與 zero-padded FFT 在邊界附近的頻譜偽影，可作為最小驗證單元。

---

**文件編號**：EML-AI-2026-ToroidalGTC-Preprocessing-v2  
**版本**：v2.0  
**完成時間**：2026 年 4 月 25 日  
**修訂說明**：v2 從 v1 移除未實際執行的深度學習對比實驗數字，將框架定位從「環面 CNN」調整為「週期性資料的 GTC 預處理框架」。ToroidalMaxPool2d 的 pooling bug 已修正。附錄三新增封閉性循環類物體的 GTC 適用性猜想。
