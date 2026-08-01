# RH Regional Phase Shaping v0.1

本包是「顯式公式中的偏軸正障礙」系列的第一個可執行工程原型。

它接受一個偏軸譜矩形

\[
K=[x_0,x_1]\times i[y_0,y_1],\qquad y_1<0,
\]

以及支撐尺度、基底維度與正則化參數，構造實偶、緊支撐的平滑函數 \(\psi\)，使其 Fourier 轉換

\[
G(w)=\int_{\mathbb R}\psi(t)e^{iwt}\,dt
\]

滿足：

1. \(G(-w)=G(w)\)；
2. \(G(\bar w)=\overline{G(w)}\)；
3. \(G(i/2)=G(-i/2)=0\)；
4. 在目標矩形上盡量逼近 \(i\)；
5. 使偏軸軌道區塊
   \[
   B(w)=2\operatorname{Re}(G(w)^2)
   \]
   在矩形網格上保持負值。

## 重要限制

這是數值原型，不是 RH 證明，也不是區間算術證書。

目前輸出的 `continuous_upper_estimate` 使用解析 Lipschitz 上界配合浮點積分估計，只能作為候選證書強度指標。要成為嚴格證書，仍需：

- MPFI／Arb 類複區間運算；
- 對 bump 積分與 Fourier 評價的外包絡；
- 對整個矩形而非有限網格的嚴格上界；
- 與顯式公式算術矩陣的連接。

## 安裝

```bash
python -m pip install -r requirements.txt
```

## 執行示例

```bash
python run_demo.py --config examples/synthetic_rectangle.json
```

輸出位於 `outputs/`：

- `phase_shaping_result.json`：係數、誤差與符號報告；
- `region_block.csv`：矩形網格上的 \(B(w)\)；
- `phase_shaping.png`：區塊與 Fourier 值的圖；
- `psi_samples.csv`：緊支撐原像樣本。

## 方法

使用實偶的成對平移 bump 基底：

\[
\phi_k(t)=b\!\left(\frac{t-a_k}{\delta}\right)
+b\!\left(\frac{t+a_k}{\delta}\right),
\]

其中

\[
b(u)=
\begin{cases}
\exp\!\left(-\frac1{1-u^2}\right),& |u|<1,\\
0,& |u|\ge1.
\end{cases}
\]

令

\[
\psi=\sum_k c_k\phi_k.
\]

端點條件 \(G(i/2)=0\) 是係數的實線性約束。程式先求此約束的零空間，再在零空間內進行 ridge 最小平方：

\[
\min_c\sum_{w_j\in K}|G_c(w_j)-i|^2+\lambda\|c\|_2^2.
\]

## 下一步

下一工程包將建立固定基底上的：

\[
M_{\mathrm{arith}}(L)=M_\infty+\sum_{m\log p\le L}M_{p,m},
\]

並測試同一係數向量是否同時滿足：

\[
B_K(c)<0,
\qquad
c^TM_{\mathrm{arith}}(L)c\ge0.
\]
