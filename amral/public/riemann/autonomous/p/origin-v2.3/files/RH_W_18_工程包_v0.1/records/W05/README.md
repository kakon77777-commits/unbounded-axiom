# RH-W-05 工程包 v0.1

本包產生第一份真實 Riemann zeta Weil $2\times2$ 有理區間矩陣。

## 結果

```text
M11 ∈ [0.4214257932676843, 0.4243340631590509]
M12 ∈ [-0.1734476249292889, -0.1728821575781725]
M22 = M11
```

偶、奇模態的嚴格下界均大於零，因此只證明固定二維子空間上的正性。

## 執行

```bash
python build_rigorous_matrix.py
python verify_matrix_certificate.py
python crosscheck_mpmath.py
```

## 主要檔案

- `01_RH-W-05_真實Weil矩陣區間_v0.1.md`：數學推導與 GAP 更新；
- `02_RH-W-05_證書與信任邊界_v0.1.md`：嚴格性層級；
- `build_rigorous_matrix.py`：有理區間生成器；
- `weil_matrix_2x2_interval.json`：完整證書；
- `verify_matrix_certificate.py`：小型 exact verifier；
- `crosscheck_mpmath.py`：獨立非嚴格交叉檢查；
- `VALIDATION.txt`、`EXACT_VERIFY.txt`、`CROSSCHECK.txt`：執行快照；
- `RH-W-05_subgaps_v0.1.csv/json`：GAP 登錄。

## 邊界

這不是 RH 證明，也沒有找到負證人。下一節點為支撐跨過 $\log2$ 的 `RH-W-06-PRIME-ACTIVE-MATRIX`。
