# RH-W-06 工程包 v0.1

本包完成第一個 **prime-active Riemann–Weil matrix chamber**：支撐嚴格落在 $\log2$ 與 $\log3$ 之間，使 $n=2$ 成為唯一可作用的 von Mangoldt index。

## 核心成果

- $2\times2$ 正交波包：$n=2$ 只作用於 off-diagonal coupling；
- $5\times5$ Toeplitz 矩陣：lag activation pattern 為 `[off, off, on, on, on]`；
- exact rational certificate 證明整個五維 interval matrix family 正定；
- witness $c=(1,1,0,-1,-1)$ 在 artificial prime-free block 上嚴格為負，放回 $n=2$ 後嚴格為正；
- 不宣稱 RH 證明或反例。

## 主要文件

- `01_RH-W-06_第一素數活化與支撐腔室_v0.1.md`
- `02_RH-W-06_五維素數穩定化證書_v0.1.md`

## 證書與契約

- `weil_matrix_prime2_2x2_interval.json`
- `weil_matrix_prime2_5x5_interval.json`
- `prime2_5x5_positive_certificate.json`
- `support_chamber_contract.json`
- `RH-W-06_subgaps_v0.1.csv`
- `RH-W-06_subgaps_v0.1.json`

## 程式

- `build_prime_active_matrix.py`：二維 prime-active matrix builder；
- `build_prime2_matrix_5x5.py`：五維 Toeplitz builder；
- `verify_prime_active_certificates.py`：純有理 exact verifier；
- `crosscheck_mpmath.py`：獨立高精度浮點交叉檢查，不進入證明路徑。

## 重播

```bash
python build_prime_active_matrix.py
python build_prime2_matrix_5x5.py
python verify_prime_active_certificates.py
python crosscheck_mpmath.py
```

## 邏輯邊界

$$
\text{本有限維正性}\not\Longrightarrow RH.
$$

本包只是完成 prime-active 區間矩陣流水線及局部幾何分析。
