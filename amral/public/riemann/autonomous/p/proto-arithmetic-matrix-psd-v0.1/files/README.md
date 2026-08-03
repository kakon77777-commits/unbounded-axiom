# RH Arithmetic Matrix / PSD Prototype v0.1

本包是「顯式公式中的偏軸正障礙」系列的第二個可執行工程原型。

它在實偶緊支撐基底上建立：

\[
M_{\mathrm{arith}}(R)
=
M_\infty(R)+M_{\mathrm{fin}}(R),
\]

其中 \(R\) 是對數座標測試函數 \(\psi\) 的支撐半徑。

## 已實作的正規化

令

\[
G(t)=\int_{\mathbb R}\psi(x)e^{itx}\,dx.
\]

archimedean 項以緊支撐時域顯式核為主計算；頻譜交叉檢查採用

\[
2\theta'(t)
=
\operatorname{Re}\psi_0\!\left(\frac14+\frac{it}{2}\right)-\log\pi,
\]

其中 \(\psi_0\) 是 digamma 函數。頻譜式僅作交叉檢查；主矩陣由時域相關核在有限區間上計算。

若 \(\operatorname{supp}\psi\subset[-R,R]\)，卷積平方支撐位於 \([-2R,2R]\)。有限位置只啟動

\[
m\log p<2R
\]

的質數冪，並以

\[
-2(\log p)p^{-m/2}
\int\psi_j(x)\psi_k(x-m\log p)\,dx
\]

加入本文符號下的 \(Q_\zeta\) 矩陣。

## 約束

預設投影到同時滿足

\[
G(i/2)=0,
\qquad
G(0)=0
\]

的係數子空間。第一個條件消去顯式公式端點；第二個條件對接已知的小支撐 archimedean 正性框架。

## 執行

```bash
python -m pip install -r requirements.txt
python run_demo.py --config examples/support_scan.json
python run_sensitivity.py
pytest -q
```

## 輸出

- `arithmetic_scan_result.json`：完整掃描與最小特徵向量；
- `support_scan.csv`：支撐半徑、啟動質數冪與最小特徵值；
- `activated_prime_powers.csv`：逐尺度啟動清單；
- `support_scan.png`：archimedean／有限位置／總矩陣最小特徵值；
- `selected_matrices.png`：指定尺度的三個矩陣；
- `selected_matrix_*.csv`：矩陣原始數據；
- `quadrature_sensitivity.csv`：三個支撐尺度的時域網格收斂掃描。

## 重要限制

這不是 RH 證明，也不是嚴格 PSD 證書。

目前仍使用：

- 時域相關與核積分的浮點離散化；
- 質數冪位置上的相關矩陣插值；
- 浮點零空間與特徵值；
- 尚未區間化的可移奇點處理。

有限頻率 digamma 積分只作交叉檢查，不決定 `numerical_psd`。

所以 `numerical_psd=true` 只表示目前離散化下未發現負特徵值。

## 主要參考正規化

- Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771。
- Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068。
