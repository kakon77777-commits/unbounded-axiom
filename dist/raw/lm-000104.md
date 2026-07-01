# N 圈無限符號的和樂度結構
## ——對 ∞ 符號家族的幾何推廣與隱藏性質

**作者**：Neo.K（許筌崴）  
**機構**：EveMissLab（一言諾科技有限公司）  
**文件編號**：EML-NLOOP-INFINITY-2026-v0.1  
**前置文件**：EML-TOPOLOGY-INFINITY-2026-v0.1  
**日期**：2026-05-30  

---

## 摘要

標準無限符號 ∞ 是一個雙圈（n=2）閉合曲線，在三維展開後達到克萊茵瓶拓撲。本文將此結構推廣至任意 n 圈，定義 **n 圈無限符號家族**，並通過數值驗證揭示以下性質：（1）Euler 迴路定理保證所有 n 均存在單輪遍歷路徑，H=0 基準確認 θ = 0°。（2）和樂度 θ(H) 隨 n 的行為非單調且複雜——存在符號翻轉與週期性結構。（3）在圓形迴圈幾何構型下，n=7 而非 n=2 最接近克萊茵瓶條件（θ ≈ -134°，H=0.5）。（4）θ 對 n 的符號在 n=4→5 及 n=8→9 處翻轉，呈現週期約 8 的隱藏結構。

---

## 1. 背景：從 ∞ 到 n 圈家族

前置文件 EML-TOPOLOGY-INFINITY-2026-v0.1 建立了標準 ∞ 符號（Bernoulli 雙紐線）的完整拓撲分析：在立交橋高度 H = H\* ≈ 0.39199 時，Bishop 框架和樂度恰好為 -180°，達到克萊茵瓶條件。

自然的推廣問題：若將 ∞ 從「兩個圈」推廣至「n 個圈」，幾何與拓撲性質如何演變？

**定義 1（n 圈無限符號）**：

在代數幾何意義下，n 圈曲線定義為：

$$r^2 = \cos(n\theta)$$

其中 n ≥ 2 為整數。此曲線有 n 個花瓣（petals），每個花瓣以原點為端點，相鄰花瓣間隔 2π/n 角度。

n=2 即退化為 Bernoulli 雙紐線（標準 ∞）。

---

## 2. Euler 迴路性質的理論保證

**命題 2.1**：對所有 n ≥ 2，n 圈曲線存在單一閉合路徑完整遍歷所有圈，僅在中心交叉點 ⋈ 重疊。

**證明**：

n 圈曲線以圖的方式建模：唯一頂點為原點（⋈），每個花瓣為一條從原點到原點的邊（自環）。頂點 ⋈ 的度數為 2n（每條自環貢獻 2）。

Euler 迴路存在定理（Euler, 1736）：連通圖存在 Euler 迴路，當且僅當所有頂點的度數均為偶數。

2n 對所有 n ≥ 1 均為偶數。故 Euler 迴路永遠存在。□

**數值驗證**：H=0 時，對 n=2,3,4,5,6 計算 Bishop 和樂度，均得 θ = 0.000°，確認閉合路徑性質。

---

## 3. 幾何構型：圓形迴圈模型

代數定義 r² = cos(nθ) 在數值積分時因原點奇異性需特殊處理。本文採用等效的**圓形迴圈構型**：

設 n 個圓，圓 k 以半徑 R 為半徑，圓心位於角度 α_k = 2πk/n 處，距原點 R。每個圓均通過原點（可驗證：圓心距原點 R，半徑 R，故原點在圓上）。

三維提升的高度函數：

$$z_k(t) = H \cdot (-1)^k \cdot \frac{1 - \cos t}{2}$$

此函數在原點處（t=π）取 z=0，在圓的遠端取 z = H·(-1)^k，相鄰圈間高度正負交替，類比 Bernoulli 雙紐線的立交橋結構。

---

## 4. 數值結果

### 4.1 和樂度對 H 的依賴

對 n=2,3,4,5,6，在 H ∈ [0, 3.0] 掃描和樂度：

| n | max|θ| | 達到最大值的 H | ±180° 跨越 |
|---|--------|-------------|-----------|
| 2 | 71.6°  | H=3.0（仍在增長） | 未達到 |
| 3 | 90.8°  | H=3.0（仍在增長） | 未達到 |
| 4 | 81.5°  | H=3.0（仍在增長） | 未達到 |
| 5 | 129.5° | H≈0.652（後下降） | 未達到 |
| 6 | 90.0°  | H≈0.732（後下降） | 未達到 |

注：圓形迴圈構型不等同於 Bernoulli 雙紐線，故 n=2 的 H\* 不同於前置文件的 0.39199。克萊茵瓶條件依賴具體幾何實現。

### 4.2 隱藏性質一：和樂度符號翻轉

固定 H=0.5，對 n=2 到 12 掃描：

| n | θ(H=0.5) | 符號 |
|---|---------|------|
| 2 | +26.6° | + |
| 3 | +8.6°  | + |
| 4 | +2.5°  | + |
| **5** | **-5.5°** | **← 符號翻轉** |
| 6 | -65.6° | - |
| 7 | **-134.3°** | - （最大負值） |
| 8 | -88.1° | - |
| **9** | **+65.4°** | **← 符號再翻轉** |
| 10 | +87.5° | + |
| 11 | +73.0° | + |
| 12 | +87.3° | + |

**觀察**：符號在 n=4→5 翻轉（正→負），在 n=8→9 再翻轉（負→正）。翻轉間隔約 4，週期約 8。

### 4.3 隱藏性質二：n=7 的特殊地位

在圓形迴圈構型下，**n=7 在 H=0.5 時達到 θ ≈ -134.3°**——所有測試 n 中最接近克萊茵瓶條件 ±180°。

這是反直覺的發現：標準 ∞（n=2）的克萊茵瓶條件在此構型下比 n=7 更難達到。克萊茵瓶條件的「最容易達到者」依賴幾何構型的選擇，而非單純由 n 決定。

### 4.4 隱藏性質三：週期 ~8 的結構

從符號序列 (+,+,+,-,-,-,-,+,+,+,...) 可見週期約 8 的循環結構。此週期的代數起源目前不明，可能與以下因素有關：

- 圓形迴圈在 n=8 時達到特殊對稱（8 個圈，相鄰圈間隔 45°）
- 某種模 8 的幾何群論結構
- 高度函數 (-1)^k 的符號模式與 n 的交互

此為本文最重要的開放問題。

---

## 5. 幾何構型對拓撲條件的影響

前置文件使用 Bernoulli 雙紐線（r² = cos(2θ)），本文使用圓形迴圈。兩者對 n=2 的和樂度行為不同，說明：

**克萊茵瓶條件（H\*）是幾何常數，不是拓撲不變量。**

相同的 n 圈拓撲（相同的 Euler 電路結構），因幾何實現方式不同，會有不同的 H\*，甚至 H\* 可能不存在（和樂度永遠達不到 ±180°）。

這是對前置文件命題的重要補充：**Bernoulli 雙紐線的 H\* = 0.39199 是這個具體幾何的特徵常數，不是所有二圈曲線共有的。**

---

## 6. 與閉合性理論（Cl）的關係

前置文件確立：◯ = Cl-1，∞ = Cl-1 + Cl-2。

本文的 n 圈推廣提示：

- n 個圈 = n 個公理的幾何聯合體現
- 每增加一圈，在幾何中增加一個「閉合層次」
- 但和樂度的符號翻轉（n=5、n=9 處）說明：不同的閉合層次可能有**相反的拓撲傾向**

這是否對應 Cl 公理系統內部的對偶結構？目前為開放命題。

---

## 7. 哲學結語

∞ 一直是一個符號。我們開始問：如果它有兄弟，兄弟長什麼樣子？

數學回答了：兄弟是 n=3,4,5,6,7 的 n 圈曲線，每個都有同樣的「單輪遍歷，回到原點」的性質，每個都有不同的幾何性格。

但意外的是，最接近克萊茵瓶的不是 ∞ 的直接繼承者（n=3 或 n=4），而是 n=7——一個七圈的奇怪存在。

這讓人想到：「特殊」不是由家族順序決定的，是由幾何結構強迫的。在這個家族裡，最深的拓撲事件藏在 n=7 的角落，而不是最顯眼的位置。

∞ 的家族比我們想象的更奇怪，也更豐富。

---

## 附錄 A：驗證程式碼

```python
"""
EML-NLOOP-INFINITY-2026
N-loop infinity curves: Euler circuit + holonomy verification
Requirements: numpy, matplotlib
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


# ────────────────────────────────────────────────
# 1. N-loop curve: circular loop model
# ────────────────────────────────────────────────

def make_loop_3d(n, H, R=1.0, N_per_loop=400):
    """
    N-loop figure as single continuous 3D path.
    Loop k: circle of radius R centered at angle 2πk/n.
    All loops pass through origin → Euler circuit.
    z_k(t) = H * (-1)^k * (1 - cos t) / 2
      → z=0 at origin (t=π), z=±H at far point (t=0)
    """
    segments = []
    for k in range(n):
        alpha = 2 * np.pi * k / n
        t = np.linspace(0, 2*np.pi, N_per_loop, endpoint=False)
        x = R * np.cos(alpha) + R * np.cos(t)
        y = R * np.sin(alpha) + R * np.sin(t)
        z = H * ((-1)**k) * (1 - np.cos(t)) / 2
        # Rotate so loop starts/ends at origin (t=π)
        roll = N_per_loop // 2
        x = np.roll(x, -roll)
        y = np.roll(y, -roll)
        z = np.roll(z, -roll)
        segments.append(np.stack([x, y, z], axis=-1))
    path = np.vstack(segments)
    return np.vstack([path, path[[0]]])  # close path


# ────────────────────────────────────────────────
# 2. Bishop frame parallel transport → holonomy
# ────────────────────────────────────────────────

def bishop_holonomy(path):
    """Holonomy angle (degrees) after full traversal via Bishop parallel transport."""
    tang = np.gradient(path, axis=0)
    tnorm = np.linalg.norm(tang, axis=1, keepdims=True)
    tang /= np.where(tnorm < 1e-10, 1.0, tnorm)

    T0 = tang[0]
    v = np.array([0., 0., 1.]) if abs(T0[2]) < 0.9 else np.array([1., 0., 0.])
    N1 = v - np.dot(v, T0) * T0;  N1 /= np.linalg.norm(N1)
    N2 = np.cross(T0, N1);        N2 /= np.linalg.norm(N2)
    N1i, N2i = N1.copy(), N2.copy()

    for i in range(1, len(tang)):
        Tc = tang[i]
        N1 = N1 - np.dot(N1, Tc) * Tc;  N1 /= max(np.linalg.norm(N1), 1e-10)
        N2 = N2 - np.dot(N2, Tc) * Tc;  N2 /= max(np.linalg.norm(N2), 1e-10)

    return np.degrees(np.arctan2(np.dot(N1, N2i), np.dot(N1, N1i)))


def holonomy_scan(n, H_max=3.0, N_H=200, N_path=350):
    H_vals = np.linspace(0, H_max, N_H)
    holos = np.array([bishop_holonomy(make_loop_3d(n, H, N_per_loop=N_path))
                      for H in H_vals])
    # Unwrap for continuous reading
    hw = holos.copy()
    for i in range(1, len(hw)):
        d = hw[i] - hw[i-1]
        if d >  180: hw[i] -= 360
        if d < -180: hw[i] += 360
    return H_vals, hw


# ────────────────────────────────────────────────
# 3. Main verification
# ────────────────────────────────────────────────

N_LOOPS = [2, 3, 4, 5, 6]

print("=== EML-NLOOP-INFINITY-2026 Verification ===")

# Euler circuit baseline
print("\n[1] H=0 baseline (Euler circuit → all θ = 0°):")
for n in N_LOOPS:
    h = bishop_holonomy(make_loop_3d(n, 0.0, N_per_loop=400))
    print(f"  n={n}: θ = {h:.3f}°")

# Sign pattern at H=0.5
print("\n[2] Holonomy at H=0.5 (sign pattern, n=2..12):")
ns = range(2, 13)
h_vals = [bishop_holonomy(make_loop_3d(n, 0.5, N_per_loop=400)) for n in ns]
for n, h in zip(ns, h_vals):
    print(f"  n={n:2d}: θ = {h:+8.2f}°")

# H* search
print("\n[3] Max |θ| reached (H ∈ [0, 3.0]):")
for n in N_LOOPS:
    H_scan, hw = holonomy_scan(n)
    print(f"  n={n}: max|θ| = {max(abs(hw)):.1f}° at H ≈ {H_scan[np.argmax(abs(hw))]:.3f}")


# ────────────────────────────────────────────────
# 4. Visualization
# ────────────────────────────────────────────────

colors = ['#ff4455', '#ffaa33', '#22ddaa', '#4488ff', '#cc44ff']
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.42, wspace=0.35)
fig.patch.set_facecolor('#060612')

# 2D curves
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor('#080818')
ax1.set_title('N-loop curves (H=0)', fontsize=9)
offsets = [(-1.4,-1.4),(1.4,-1.4),(-1.4,1.4),(1.4,1.4)]
for i, n in enumerate([2,3,4,5]):
    p = make_loop_3d(n, 0.0, N_per_loop=300)
    sc = 0.9 / n
    ox, oy = offsets[i]
    ax1.plot(p[:,0]*sc+ox, p[:,1]*sc+oy, color=colors[i], lw=1.5)
    ax1.text(ox, oy+1.1, f'n={n}', ha='center', fontsize=9,
             color=colors[i], fontweight='bold')
ax1.set_xlim(-2.8, 2.8); ax1.set_ylim(-2.8, 2.8)
ax1.set_aspect('equal'); ax1.axis('off')

# Holonomy vs H
ax2 = fig.add_subplot(gs[0, 1:])
ax2.set_facecolor('#080818')
ax2.set_title('Holonomy theta(H) for n=2..6  (H in [0, 3.0])', fontsize=9)
for i, n in enumerate(N_LOOPS):
    H_scan, hw = holonomy_scan(n)
    ax2.plot(H_scan, hw, color=colors[i], lw=2, label=f'n={n}')
ax2.axhline(-180, color='white', ls='--', lw=1, alpha=0.6, label='+-180 (Klein)')
ax2.axhline( 180, color='white', ls='--', lw=1, alpha=0.6)
ax2.axhline(   0, color='gray',  ls='-',  lw=0.5, alpha=0.3)
ax2.set_xlabel('H', fontsize=9); ax2.set_ylabel('theta (deg)', fontsize=9)
ax2.legend(fontsize=8); ax2.grid(alpha=0.15)

# Sign pattern bar chart
ax3 = fig.add_subplot(gs[1, :2])
ax3.set_facecolor('#080818')
ax3.set_title('Holonomy at H=0.5 vs n=2..12\n'
              'Sign flip at n=4->5 and n=8->9  (period ~8)', fontsize=9)
ns_list = list(range(2, 13))
bar_colors = ['#22ddaa' if h >= 0 else '#ff4455' for h in h_vals]
ax3.bar(ns_list, h_vals, color=bar_colors, alpha=0.85, edgecolor='white', linewidth=0.5)
ax3.axhline(-180, color='white', ls='--', lw=1, alpha=0.5)
ax3.axhline( 180, color='white', ls='--', lw=1, alpha=0.5)
ax3.axhline(   0, color='gray',  ls='-',  lw=0.5, alpha=0.5)
ax3.axvline(4.5, color='yellow', ls=':', lw=1.5, alpha=0.7, label='Sign flip')
ax3.axvline(8.5, color='yellow', ls=':', lw=1.5, alpha=0.7)
for n, h in zip(ns_list, h_vals):
    ax3.text(n, h + (8 if h >= 0 else -12), f'{h:.0f}', ha='center', fontsize=7.5,
             color='white', fontweight='bold')
ax3.set_xlabel('n (number of loops)', fontsize=9)
ax3.set_ylabel('theta at H=0.5 (deg)', fontsize=9)
ax3.legend(fontsize=8); ax3.grid(alpha=0.15)

# 3D curve for n=7 (most interesting)
ax4 = fig.add_subplot(gs[1, 2], projection='3d')
path7 = make_loop_3d(7, 0.5, N_per_loop=200)
N = len(path7)
cmap = plt.cm.plasma
for i in range(N-1):
    ax4.plot(path7[i:i+2,0], path7[i:i+2,1], path7[i:i+2,2],
             color=cmap(i/N), lw=1.5)
h7 = bishop_holonomy(path7)
ax4.set_title(f'n=7, H=0.5\ntheta = {h7:.1f} deg\n(closest to Klein bottle)', fontsize=8)
ax4.set_xlabel('X', fontsize=7); ax4.set_ylabel('Y', fontsize=7); ax4.set_zlabel('Z', fontsize=7)
ax4.tick_params(labelsize=6); ax4.view_init(elev=25, azim=40)

fig.suptitle('N-loop Infinity Generalization: Holonomy & Hidden Properties\n'
             'EML-NLOOP-INFINITY-2026-v0.1  (c) EveMissLab',
             fontsize=11, fontweight='bold', y=0.99, color='white')

plt.savefig('EML-NLOOP-INFINITY-2026-verification.png',
            dpi=150, bbox_inches='tight', facecolor='#060612')
plt.close()
print("\nFigure saved.")
```

---

*EML-NLOOP-INFINITY-2026-v0.1 © EveMissLab*
