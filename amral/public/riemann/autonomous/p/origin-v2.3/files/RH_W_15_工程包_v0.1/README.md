# RH-W-15 工程包 v0.1

本包完成固定 $h$ 下的二維 Interval–Taylor 參數管擴張，並修正 RH-W-14 阿基米德導數界漏掉的支撐外常數尾。

## 主要結論

對

$$
h=\frac{1797}{10000},
$$

$$
\left|d-\frac{893}{5000}\right|\le10^{-7},
\qquad
|\sigma|\le10^{-7},
$$

整個連續矩形均嚴格滿足

$$
10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}.
$$

相較 RH-W-14，每個方向半徑擴大 $25{,}000$ 倍。

## 驗證

```bash
python verify_interval_taylor_tube.py
```

可選的高精度浮點交叉檢查：

```bash
python crosscheck_w15_mpmath.py
```

## 重要修正

RH-W-14 的一階阿基米德導數界漏掉支撐外的 $-2f(0)$ 尾。修正後界為：

$$
L_3=179,
\quad L_5=218,
\quad L_7=255.
$$

重跑 exact verifier 後，RH-W-14 原結論仍成立。詳見：

- `02_RH-W-15_阿基米德支撐外尾修正與W14回溯重證_v0.1.md`
- `RH-W-14_corrected_lipschitz_reaudit.json`

## 信任邊界

證明路徑依賴：

- Python arbitrary-precision integers；
- `fractions.Fraction`；
- 有理區間級數；
- CPython `Decimal.exp` 正確捨入契約及向外擴張；
- 純有理 $LDL^T$；
- 明示的 B-spline 導數上界。

mpmath 僅為非證明性交叉檢查。

本包只證明有限維連續參數管，不證明或反證 RH。
