# Results

## 1. Simplified exact extremal

一軸點、一核心點模型具有 closed rank-two formula。對中心 core point

$$
z=20.4075-0.103125i
$$

做每帶 point scan，最細時間步結果為：

| band | best one-point lower bound | $x$ |
|---|---:|---:|
| $A_0$ | $0.111322$ | $17.85$ |
| $A_1$ | $0.261253$ | $20.30$ |
| $A_2$ | $0.111224$ | $23.15$ |
| $A_3$ | $0.111034$ | $35.15$ |
| $A_4$ | $0.111031$ | $70.65$ |

所有單帶值都小於 $1$。因此 v0.5 的 obstruction 不是任一單帶獨立造成，
而是五帶 measure interaction。

## 2. Galerkin convergence

| raw dimension | effective dimension | raw $\alpha$ |
|---:|---:|---:|
| $24$ | $22$ | $7.788239$ |
| $40$ | $38$ | $3.679471$ |
| $64$ | $62$ | $1.588306$ |
| $80$ | $78$ | $1.300399$ |
| $96$ | $94$ | $1.184647$ |
| $120$ | $118$ | $1.159914$ |
| $144$ | $142$ | $1.139122$ |
| $160$ | $158$ | $1.133508$ |
| $176$ | $174$ | $1.132795$ |
| $192$ | $190$ | $1.132475$ |

序列單調下降並開始形成平台。最後一列為

$$
\alpha_{\rm safe}=1.0662376,
$$

$$
\lambda_{\min}(W_{\rm safe})=0.2569999.
$$

但 Galerkin PSD 本身仍不能推出 continuous PSD。

## 3. Independent point-kernel agreement

在 $x=20.4$、中心 core point 的 $A_1$ simplified extremal：

$$
\Lambda_{\rm Galerkin,192}
=0.1124416819495,
$$

$$
\Lambda_{\rm Green,\Delta t=0.0025}
=0.1124416808961.
$$

絕對差為

$$
1.05\times10^{-9}.
$$

Gauss–Legendre orders 1,024 到 2,560 的差異亦只在約
$2.4\times10^{-10}$ 內。

## 4. Direct continuous-kernel atomic transfer

raw dimension 192 measures 包含：

$$
58\ \text{axis atoms}+2\ \text{core atoms}.
$$

同一 measures 在 direct clamped Green solver 中給出：

| $\Delta t$ | raw threshold |
|---:|---:|
| $0.02$ | $1.1324314430$ |
| $0.01$ | $1.1324406087$ |
| $0.005$ | $1.1324411657$ |
| $0.0025$ | $1.1324411997$ |

在 v0.6 safe alpha，

$$
\alpha_{\rm safe}=1.0662376054,
$$

full finite-span minimum eigenvalue 為

$$
0.2568265725,
$$

而等價 $2\times2$ Schur certificate minimum 為

$$
0.0560870811.
$$

這是 dictionary-independent continuous-kernel floating obstruction。

## 5. Rational candidate at $\alpha=21/20$

將 supports 與 weights 有理化後，在

$$
\alpha=\frac{21}{20}=1.05
$$

得到

$$
\lambda_{\min}(W)=0.3122432495,
$$

$$
\lambda_{\min}(S)=0.0698852338.
$$

最後兩級 time steps 的 Schur minimum drift 約

$$
2.68\times10^{-8}.
$$

這個 drift 只是 convergence diagnostic，不是 interval bound。

## 6. Research decision

v0.6 已達到連續化的決策目的：

- obstruction 不再依賴 v0.5 local bump dictionary；
- 不需繼續增加 Galerkin dimension；
- 下一個有價值的工作是 interval-enclose 一個 60-positive-rank、
  2-negative-rank witness；
- certificate target 固定為 $\alpha=1.05$，不再追求更高 floating alpha。

下一節點為
`RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7`。
