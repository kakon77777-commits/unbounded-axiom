# RH AI 研究起點 v1.9

本整合包保留前序 RH 工程節點，並加入 `RH_W_16_工程包_v0.1`。

## v1.9 核心

建立第一個 $(h,d,\sigma)$ 三維近零正譜盒：

$$
|h-0.1797|\le10^{-8},\qquad
|d-0.1786|\le10^{-7},\qquad
|\sigma|\le10^{-7}.
$$

整盒取得：

$$
10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}.
$$

## 新增資料

- RH-W-16 三篇研究文件；
- 八角三維 JSON 證書；
- 尺度二階曲率界；
- 純有理 verifier；
- 80 位 mpmath 交叉檢查；
- 八角 midpoint 譜觀察；
- 自包含 Python 共用模組。

## Batch 01

目前完成 `RH-W-16 / RH-W-20`，尚餘四輪。

## 聲明

有限維三維參數盒不推出 RH。`RH_CLAIM=False`。
