# RH AI 研究起點 v1.8

本整合包保留前序 RH 工程節點，並加入 `RH_W_15_工程包_v0.1`。

## v1.8 核心

$$
\left|d-\frac{893}{5000}\right|\le10^{-7},
\qquad
|\sigma|\le10^{-7}
$$

整個二維矩形均取得：

$$
10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}.
$$

相較 v1.7，每個參數方向擴大 $25{,}000$ 倍。

## 修正紀錄

v1.7／RH-W-14 的全域一階導數界少計 spline 支撐外的阿基米德常數尾。v1.8 已加入 $\operatorname{artanh}(e^{-R})$ 修正並完成回溯重證；v1.7 的結論保留，但原導數常數由修正版取代。

## 新增資料

- RH-W-15 三篇研究文件；
- 四角 Interval–Taylor JSON 證書；
- RH-W-14 修正回溯證書；
- 純有理 verifier；
- 60 位 mpmath 交叉檢查；
- 完整 W-15 工程資料夾。

## 聲明

有限維參數管不推出 RH。RH claim：False。
