# RH-W-15：GAP 更新與 Batch 01 進度

## 已關閉節點

### `RH-W-15-ARCH-SUPPORT-EXTERIOR-TAIL`

辨識並修正阿基米德正規化常數在 spline 支撐外留下的尾積分：

$$
\operatorname{artanh}(e^{-R}).
$$

### `RH-W-15-W14-RE-AUDIT`

使用修正後一階導數界重新驗證 RH-W-14；原二維小管結論保留。

### `RH-W-15-SECOND-DERIVATIVE-BOUNDS`

建立 degree-$3/5/7$ Weil 中心二階導數的有理全域界：

$$
2494,
\qquad3110,
\qquad3697.
$$

### `RH-W-15-BILINEAR-TUBE`

建立四角區間矩陣、雙線性凸組合及二階餘項證書，將參數半徑擴大至 $10^{-7}$。

### `RH-W-15-CONTINUOUS-BRACKET`

對整個新矩形證明：

$$
10^{-8}<\lambda_{\min}<5\times10^{-8}.
$$

## 仍開放節點

### `RH-W-15-ANISOTROPIC-MAX-TUBE`

目前採用

$$
\rho_d=\rho_\sigma=10^{-7}.
$$

尚未求得 $d$ 與 $\sigma$ 各方向的最大可證半徑，也未利用 Hessian 的實際 block 稀疏性做非等向擴張。

### `RH-W-15-H-DIRECTION`

尺度 $h$ 尚固定。加入 $h$ 後，spline knot、樣本正規化、端點積分與 Gram 全部同時變動，需要三維 Taylor 證書。

### `RH-W-15-HESSIAN-SIGN-STRUCTURE`

目前二階餘項仍使用元素級絕對值上界。尚未保留 Hessian 矩陣的符號、Toeplitz 與 block 結構。

## Batch 01 進度

第一批固定為：

$$
\texttt{RH-W-01}\sim\texttt{RH-W-20}.
$$

本輪為：

$$
\boxed{15/20}.
$$

剩餘規劃：

1. `RH-W-16`：加入 $h$，建立三維參數盒；
2. `RH-W-17`：腔室感知的自動分割；
3. `RH-W-18`：證書後端統一；
4. `RH-W-19`：對抗性與可重現性審計；
5. `RH-W-20`：Batch 01 統合、網站資料與交棒包。

本輪不改變 RH 總體狀態：

$$
\boxed{\text{RH remains open.}}
$$
