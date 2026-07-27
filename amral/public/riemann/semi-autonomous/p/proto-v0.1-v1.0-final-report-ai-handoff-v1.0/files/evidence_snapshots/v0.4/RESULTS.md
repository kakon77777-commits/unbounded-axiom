# Results

## 結論

目前 support-only dictionary 在抽樣到 $R=16$ 仍未通過 dual gate。
四個候選半徑都至少有一個困難子矩形被安全 lower bound 阻擋。

| $R$ | dimension | 最強 $\alpha_{\rm safe}$ | PSD margin |
|---:|---:|---:|---:|
| $10.25$ | $100$ | $2.620080$ | $0.0713394$ |
| $12$ | $118$ | $1.899950$ | $0.0834713$ |
| $14$ | $138$ | $1.398180$ | $0.0992519$ |
| $16$ | $158$ | $1.094281$ | $0.1149902$ |

`outputs/witness_verification.json` 重建 12 份序列化 witness，全部保持
PSD 且有效 lower bound 大於 $1$。

## 粗網格假逃逸

固定 $R=16$ 與 patch `x4_Y3__r2_3`：

| axis step | raw $\alpha$ | safe $\alpha$ |
|---:|---:|---:|
| $0.25$ | $0.985277$ | $0.980351$ |
| $0.1$ | $1.124306$ | $1.062153$ |
| $0.05$ | $1.139551$ | $1.069775$ |
| $0.025$ | $1.192293$ | $1.096146$ |

所以 coarse-grid pass 不可作為 primal 可行證據。

## Uniform frontier

- 126 組：14 半徑 × 3 密度 × 3 width factors。
- 第一個 sampled center-only uniform escape：$R=10$。
- 第一個 sampled original-patch uniform $3\times3$ escape：$R=14$。
- joint measure optimization 將上述樂觀 transition 重新阻擋。

## Prime cost

在 $R=10.25$，實際枚舉得到：

$$
\pi(799{,}902{,}177)=41{,}141{,}456
$$

以及 $41{,}144{,}807$ 個 prime-power terms。到 $R=16$，strict
cutoff 為

$$
78{,}962{,}960{,}182{,}680,
$$

$x/\log x$ 質數代理約 $2.47\times10^{12}$。

## 決策

不再以增加 $R$ 作主要方向。下一節點共設計 axis notches、dictionary
與 cover，並要求任何 $\alpha<1$ 結果接受 dense-axis audit。

