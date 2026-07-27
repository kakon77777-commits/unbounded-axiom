# Results

## Peak atlas

12 份父 witness 的五帶主峰為：

| band | interval | primary peak |
|---|---:|---:|
| $A_0$ | $[14,18]$ | $17.83$ |
| $A_1$ | $[18,23]$ | $20.38$ |
| $A_2$ | $[23,35]$ | $23.24$ |
| $A_3$ | $[35,70]$ | $42.18$ |
| $A_4$ | $[70,145]$ | $83.05$ |

$A_1$ 主峰與目標實部區間重疊，說明軸負擔與偏軸核心不是彼此獨立的設計
問題。

## 齊次 notch screen

在 $R=16$，baseline 的 optimized-core / uniform-axis threshold 為
$0.251927$；只加入 patch-center value notch 後為 $0.252055$，沒有改善。
同時要求 value 與 derivative notch 時，anchor derivative Frobenius norm
降至約 $1.07\times10^{-12}$，threshold 升至 $33.845656$。

在 $R=10.25$，`anchor_flat` 更升至 $691.837880$。這些數值不是單調性定理
的證明，而是其預期後果的實驗性核對。

## 外部 lift

uniform/core screen：

| radius | baseline | 6-direction lift |
|---:|---:|---:|
| $10.25$ | $0.999424$ | $0.979093$ |
| $16$ | $0.251927$ | $0.245526$ |

在 $R=16$ 擴到 21 個頻率時，15 個方向在約束與 whitening 後保持有效，
threshold 改善 $3.10\%$。但 joint dual 只從

$$
\alpha=1.189562
$$

降到

$$
\alpha=1.176230,\qquad
\alpha_{\rm safe}=1.088115>1.
$$

raw improvement 為 $1.12\%$，沒有穿越 gate。

## Polynomial-bump geometry

27 組 screen 中最佳為 `d12_w2_p5`：

$$
\text{dimension}=190,\qquad
\text{screen threshold}=0.236986.
$$

其 tail 最小特徵值只有約 $1.15\times10^{-3}$，表示改善伴隨近零方向。
joint dual 結果為

| geometry | raw $\alpha$ | safe $\alpha$ | safe $\lambda_{\min}$ | raw improvement |
|---|---:|---:|---:|---:|
| baseline | $1.189562$ | $1.094781$ | $0.114990$ | — |
| `d10_w2_p4` | $1.146055$ | $1.073027$ | $0.005438$ | $3.66\%$ |
| `d12_w2_p5` | $1.143522$ | $1.071761$ | $0.001151$ | $3.87\%$ |

四個保存的 joint objects 全部以序列化 measures 重建並保持
$\alpha_{\rm safe}>1$ 與 PSD；重建最小特徵值的最大絕對差約
$5.15\times10^{-16}$。

## Dense complementary audit

四個 rank-one complementary objectives 為：

$$
1.275147,\quad1.254665,\quad1.265481,\quad1.263246,
$$

全部大於 $1$。最佳 lift 將遠帶峰由約 $42.3,82.9$ 移到
$41.275,81.875$；最佳幾何則移到 $36.325,73.575$。$A_1$ charge 仍占主導。
這符合父節點的停止規則：不能把 peak migration 當成全域負擔消失。

## 決策

- 停止純齊次 value/derivative notch。
- 停止目前的 spectral-slope atom family。
- 停止更多 polynomial-bump density/width/power scaling。
- 因所有 safe dual bounds 仍大於 $1$，不啟動 primal Gram search。
- 下一節點轉向 `RH-PaleyWiener-AxisCoreExtremal-20260724-v0.6`。

這些結論只適用於明確列出的 finite dictionaries、patch、軸網格與 floating
matrices；不排除其他外部字典，也不構成連續函數空間 obstruction。
