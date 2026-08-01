# RH-W-11 工程包 v0.1

本包完成 centered cardinal B-spline 核族的「靈敏度—正則性對偶」。

核心公式：

$$
\beta_m*\beta_n=\beta_{m+n+1},
$$

以及 prime-power 支撐邊界的局部啟動律：

$$
p_{p^k;m,n}(\varepsilon)
=-\frac{\log p}{\sqrt{p^k}}
\frac{\varepsilon_+^{m+n+1}}{(m+n+1)!}.
$$

主要結果：

1. 自相關啟動階數為 $2m+1$；
2. 交叉相關啟動階數為 $m+n+1$；
3. 同一階數同時控制邊界正則性、Fourier 衰減與保守尾界階數；
4. 在 `RH-W-10` 的穿透深度下，$m=1$ 的 prime-$3$ 響應比 $m=3$ 大超過 $10^{16}$；
5. 沒有單一最佳核，下一步改用 $m=1/3$ 混合階字典。

## 主要文件

- `01_RH-W-11_核靈敏度與正則性對偶_v0.1.md`
- `02_RH-W-11_混合階字典與Pareto設計_v0.1.md`
- `kernel_sensitivity_certificate.json`
- `kernel_pareto.csv`
- `mixed_order_ladder.csv`

## 執行

```bash
python build_kernel_sensitivity.py
python verify_kernel_sensitivity.py
python validate_kernel_family.py
```

## 驗證層級

- `verify_kernel_sensitivity.py`：有理區間重算局部縮放律；
- `validate_kernel_family.py`：獨立浮點卷積回歸，只作實作檢查；
- 沒有 RH 證明或無限維正性主張。
