# RH-W-16 工程包 v0.1

本包建立第一個混合階 Weil 字典的三參數近零正譜管：

$$
|h-0.1797|\le10^{-8},\qquad
|d-0.1786|\le10^{-7},\qquad
|\sigma|\le10^{-7}.
$$

對整個連續盒 exact 證明：

$$
10^{-8}<\lambda_{\min}<5\times10^{-8}.
$$

## 主要檔案

- `01_RH-W-16_三參數近零譜管_v0.1.md`：數學主文件。
- `02_RH-W-16_尺度曲率證書與計算架構_v0.1.md`：尺度導數與證書設計。
- `03_RH-W-16_GAP更新與Batch01進度_v0.1.md`：GAP 狀態。
- `three_parameter_tube_certificate.json`：八角完整區間證書。
- `build_three_parameter_tube.py`：證書生成器。
- `verify_three_parameter_tube.py`：結構與 exact verifier。
- `crosscheck_w16_mpmath.py`：獨立高精度抽查。
- `corner_spectrum_observation.csv`：非嚴格角點譜觀察。

## 重放

```bash
python verify_three_parameter_tube.py
```

完整重建八角矩陣：

```bash
python build_three_parameter_tube.py
```

完整重建較慢，因為需要重新生成八套 jump-resolved 阿基米德矩陣。

## 聲明

這是固定十維子空間上的嚴格數值證書，不證明或反證 RH。
