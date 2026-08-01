# RH-W-12 Mixed-Order Dictionary v0.1

本包建立第一個 $m=1/3$ 混合 B-spline 真實 Weil 區間矩陣。

## 核心結果

$$
\frac1{2000}<\lambda_{\min}^{\rm mixed}<\frac1{1000},
$$

同時：

$$
\lambda_{\min}^{(m=3)}>\frac1{250},
\qquad
\lambda_{\min}^{(m=1)}>\frac1{20}.
$$

有理 witness 證明兩個 self-block 均為正、cross-block 為負，形成跨正則性抵消模態。

## 執行

```bash
python build_mixed_dictionary.py
python verify_mixed_dictionary.py
python crosscheck_mixed_mpmath.py
```

## 主要檔案

- `01_RH-W-12_混合階字典與交叉抵消模態_v0.1.md`
- `02_RH-W-12_證書架構與信任邊界_v0.1.md`
- `mixed_10x10_interval.json`
- `build_mixed_dictionary.py`
- `verify_mixed_dictionary.py`
- `crosscheck_mixed_mpmath.py`
- `mixed_order_core.py`
- `mixed_activation_graph.csv`
- `mixed_mode_attribution.json`
- `RH-W-12_subgaps_v0.1.csv`

## 限制

`CERTIFIED_POSITIVE_ON_THIS_MIXED_SUBSPACE` 不等於 RH。浮點特徵值與模態歸因只用於探索；正式狀態由有理區間與 exact $LDL^T$ 決定。
