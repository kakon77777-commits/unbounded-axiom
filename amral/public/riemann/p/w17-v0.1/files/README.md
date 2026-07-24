# RH-W-17 工程包 v0.1

本包建立第一個跨越 spline knot 事件面的腔室感知 Weil 參數證書。

## 核心結果

固定

$$
h=0.1797,\qquad\sigma=0,
$$

在

$$
d\in[0.17328669,0.17328690]
$$

內跨越

$$
4d=\log2.
$$

系統切分為左腔室、事件薄層、右腔室，並證明全部閉區間上

$$
\lambda_{\min}(M(d),G(d))>10^{-8}.
$$

## 重放

```bash
python verify_chamber_subdivision.py
```

可選高精度交叉檢查：

```bash
python crosscheck_w17_mpmath.py
```

重新生成四個 endpoint matrices 的成本較高，但支援逐點 JSON 快取：

```bash
python build_chamber_subdivision.py
```

## 主要檔案

- `01_RH-W-17_腔室感知切分與事件薄層_v0.1.md`
- `02_RH-W-17_多正則性中央結事件_v0.1.md`
- `03_RH-W-17_GAP更新與Batch01進度_v0.1.md`
- `chamber_subdivision_certificate.json`
- `chamber_adjacency_graph.json`
- `event_surface_catalog.csv`
- `local_chamber_spectrum.csv`
- `build_chamber_subdivision.py`
- `verify_chamber_subdivision.py`
- `crosscheck_w17_mpmath.py`

## 聲明

本包只證明固定十維子空間上的局部有限維正性，不證明或反證黎曼猜想。
