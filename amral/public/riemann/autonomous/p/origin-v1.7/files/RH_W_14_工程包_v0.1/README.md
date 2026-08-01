# RH-W-14 工程包 v0.1

本包把 RH-W-13 的十維近零單點證書擴張為第一個連續二維參數管。

## 主結果

固定

$$
h=\frac{1797}{10000},
$$

對

$$
\left|d-\frac{893}{5000}\right|\le4\times10^{-12},
\qquad
|\sigma|\le4\times10^{-12},
$$

純有理驗證器證明：

$$
10^{-8}<\lambda_{\min}(M(d,\sigma),G(d,\sigma))<5\times10^{-8}.
$$

此結論只適用於固定十維 mixed B-spline 子空間，不推出 RH。

## 主要檔案

- `01_RH-W-14_嚴格二維參數管_v0.1.md`
- `02_RH-W-14_Lipschitz證書與保守性審計_v0.1.md`
- `03_RH-W-14_連續近零譜帶與GAP更新_v0.1.md`
- `parameter_tube_2d_certificate.json`
- `build_parameter_tube.py`
- `verify_parameter_tube.py`
- `verify_cross_regularity.py`
- `crosscheck_parameter_tube.py`
- `mixed_10x10_nearzero_interval.json`
- `RH-W-14_subgaps_v0.1.csv`

## 重建與驗證

```bash
python build_parameter_tube.py
python verify_cross_regularity.py
python verify_parameter_tube.py
python crosscheck_parameter_tube.py
```

## 嚴格性

證書路徑使用有理區間、B-spline 全域導數界、對稱矩陣列和擾動界及純有理 $LDL^T$。高精度浮點採樣只作交叉檢查。

## 聲明邊界

- 未證明 RH。
- 未反證 RH。
- 未找到負 Weil witness。
- 目前固定 $h$，只建立 $(d,\sigma)$ 二維管。
- 管寬受保守 Lipschitz 界限制。
