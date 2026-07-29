# RH-W-09 工程包 v0.1

本包完成第一條「固定網格候選 → 自適應局部延拓 → prime-power 邊界追蹤 → $10^{-9}$ 嚴格廣義正裕度證書」流水線。

## 固定結果

候選：

$$
h=\frac{87}{400},
\qquad
d=\frac{117}{512},
\qquad N=15.
$$

探索性最低廣義特徵值約為：

$$
1.32\times10^{-9}.
$$

純有理驗證器證明：

$$
Q(c)>10^{-9}c^TGc
$$

對該固定十五維空間中所有非零 $c$ 成立。

這只是有限維正性，不構成 RH 證明。

## 主要檔案

- `01_RH-W-09_自適應腔室延拓_v0.1.md`
- `02_RH-W-09_十億分之一正裕度證書_v0.1.md`
- `03_RH-W-09_精度升級與信任邊界_v0.1.md`
- `adaptive_continuation.py`
- `adaptive_continuation_path.csv/json`
- `rigorous_refinement_tools.py`
- `build_continuation_certificate.py`
- `continuation_15x15_interval.json`
- `verify_continuation_certificate.py`
- `RH-W-09_subgaps_v0.1.csv`

## 重播

```bash
python adaptive_continuation.py
python build_continuation_certificate.py
python verify_continuation_certificate.py
```

探索器需要 NumPy 與 SciPy。exact verifier 只使用 Python 標準庫中的整數與 `Fraction`。

## 來源定位

數學背景使用經典 Weil 顯式公式與 Weil 判準。當代有限區間／Galerkin 背景可參照：

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096.
- Akiva Groskin, *A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, arXiv:2607.02828.
- Enrico Bombieri, *The Riemann Hypothesis*, Clay Millennium Prize Problems.
- NIST DLMF §5.11：Gamma／digamma 漸近展開與餘項背景。

本包的 adaptive continuation policy、B-spline prime-boundary tracker、rational tail continuation 與十五維證書是本研究計畫的工程組裝；不宣稱上述來源支持本包的具體數值。
