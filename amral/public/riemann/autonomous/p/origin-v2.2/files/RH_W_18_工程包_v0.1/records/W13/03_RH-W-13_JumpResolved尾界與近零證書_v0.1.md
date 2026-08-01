# RH-W-13：Jump-Resolved 尾界與近零證書

## 1. 舊尾界的限制

對 degree-$r$ 相關核，舊方法在分部積分後，以

$$
|R(a)|\le \frac{\|F^{(r)}\|_\infty}{a^{r+1}}
$$

包住整個 top-derivative 餘項。對 degree $3$ 通道，當 $d\approx h$ 時，某些 spline knot 非常接近零；粗絕對值 majorant 無法解析 $10^{-8}$ 級廣義譜底。

## 2. 精確 jump 表示

令

$$
F(x)=f(x)+f(-x),\qquad x\ge0,
$$

且 $F$ 是 compactly supported、degree-$r$ 的分段多項式。因為 $F^{(r)}$ 分段常數，完整分部積分可寫成

$$
\int_0^\infty e^{-ax}F(x)\,dx
=
\sum_{j=0}^{r-1}\frac{F^{(j)}(0)}{a^{j+1}}
+
\frac{F^{(r)}(0^+)+\sum_\ell \Delta F^{(r)}(x_\ell)e^{-ax_\ell}}{a^{r+1}}.
$$

這不是漸近式，而是對該 piecewise-polynomial 核的精確有限表示。

## 3. 指數 jump 尾界

令

$$
a_k=2k+\frac12.
$$

對每個 $x>0$，有

$$
0\le
\sum_{k=K}^\infty\frac{e^{-a_kx}}{a_k^p}
\le
\frac{e^{-a_Kx}}{a_K^p(1-e^{-2x})}.
$$

因此 spline knot 距離一旦為正，top-derivative jump 的尾項會獲得額外指數衰減，而不再只依賴 $K^{-r}$。

## 4. 本輪 cutoff

使用：

$$
K_3=4000,
$$

$$
K_5=1500,
$$

$$
K_7=700.
$$

各 block-lag 的最大區間寬度約為：

- degree $3$：$1.94\times10^{-12}$；
- degree $5$：$9.68\times10^{-13}$；
- degree $7$：$6.45\times10^{-13}$。

完整十維矩陣的最大列半徑為

$$
\epsilon\approx2.91\times10^{-12}.
$$

## 5. 證書

下界：

$$
C-10^{-8}G-\epsilon I\succ0.
$$

上界：存在整數向量 $c$ 使

$$
c^TMc<5\times10^{-8}c^TGc.
$$

所以

$$
\boxed{10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}}.
$$

## 6. 信任邊界

證書路徑使用：

- Python `int`；
- `fractions.Fraction`；
- rational interval arithmetic；
- rational atanh/arctan/log series；
- integer square-root enclosure；
- documented outward-rounded `Decimal.exp`；
- exact rational $LDL^T$。

80 位 mpmath 積分只作交叉檢查，不屬於證明路徑。

標籤為：

$$
\boxed{\texttt{RIGOROUS\_NUMERICAL\_CERTIFICATE UNDER DOCUMENTED SOFTWARE CONTRACT}}.
$$

尚未轉寫至 Lean、Coq 或其他形式化證明器。
