# RH-W-01-D/E/F/G：雙消失矩、相關閉合與 Mellin–Fourier 接口
## Riemann Hypothesis GAP Engineering Note v0.2

**研究計畫：** RH GAP Atlas / AI 數學工程化接力  
**父節點：** `RH-W-01`  
**本輪節點：** `RH-W-01-A/B/C/D/E/F/G/H` 的一個可驗證子族  
**狀態：** `PARTIALLY_CLOSED_BY_GBUMP_FAMILY`  
**日期：** 2026-07-23  
**性質：** 測試函數生成器與作用域證明；不是 RH 證明，不建立 Weil 二次型的新正性結果

---

## 0. 本輪交付物

本文件構造一個非空、可參數化、可計算的函數族

$$
\mathcal G_{\mathrm{bump}}
\subset \mathcal G_{B0},
$$

使每個 $g\in\mathcal G_{\mathrm{bump}}$ 都精確滿足：

$$
\widetilde g(0)=\widetilde g(1)=0,
$$

且其 Weil 相關型

$$
f_g(x)=\int_0^\infty g(xy)\overline{g(y)}\,dy
$$

屬於 $C_c^\infty(0,\infty)\subset\mathcal W$。

本輪因此對這個特定子族關閉：

- `RH-W-01-A`：顯式公式各項合法；
- `RH-W-01-B`：零點和絕對收斂，排序不再造成歧義；
- `RH-W-01-C`：$x=1$ 的表面奇異可消去；
- `RH-W-01-D`：乘法相關函數閉合；
- `RH-W-01-E`：兩個消失矩的精確建構；
- `RH-W-01-G`：乘法 Mellin 與加法 Fourier 表示的明確轉換。

`F` 已建立雙實作一致性測試；`H` 已建立候選 metadata 與驗證器，但尚未形式化至 Lean/Isabelle。

---

# 1. 基礎算子

令

$$
D:=x\frac{d}{dx}
$$

為乘法群 $\mathbb R_+$ 上的 Euler 微分算子，並定義

$$
\mathcal A:=D(D+1).
$$

取種子空間

$$
\mathscr H:=C_c^\infty(0,\infty),
$$

以及生成族

$$
\mathcal G_{\mathrm{bump}}
:=\mathcal A\mathscr H
=\left\{D(D+1)h:h\in C_c^\infty(0,\infty)\right\}.
$$

由於 $D$ 是局部微分算子，對任意 $h\in\mathscr H$：

$$
\operatorname{supp}(\mathcal Ah)
\subseteq\operatorname{supp}(h),
$$

且 $\mathcal Ah\in C_c^\infty(0,\infty)$。

展開後：

$$
\mathcal Ah=x^2h''(x)+2xh'(x).
$$

---

# 2. Mellin 消零定理

B0 Mellin 變換為

$$
\widetilde h(s)=\int_0^\infty h(x)x^s\frac{dx}{x}.
$$

## 定理 2.1

若 $h\in C_c^\infty(0,\infty)$ 且 $g=\mathcal Ah$，則對所有 $s\in\mathbb C$：

$$
\boxed{
\widetilde g(s)=s(s-1)\widetilde h(s)
}.
$$

### 證明

因 $h$ 緊支撐於 $(0,\infty)$，分部積分沒有端點項：

$$
\widetilde{Dh}(s)
=\int_0^\infty xh'(x)x^s\frac{dx}{x}
=\int_0^\infty h'(x)x^s\,dx
=-s\widetilde h(s).
$$

因此：

$$
\widetilde{(D+1)h}(s)=(1-s)\widetilde h(s),
$$

再作用一次 $D$：

$$
\widetilde{D(D+1)h}(s)
=-s(1-s)\widetilde h(s)
=s(s-1)\widetilde h(s).
$$

證畢。

## 推論 2.2：雙消失矩

$$
\boxed{
\widetilde g(0)=\widetilde g(1)=0
}.
$$

亦即：

$$
\int_0^\infty g(x)\frac{dx}{x}=0,
\qquad
\int_0^\infty g(x)\,dx=0.
$$

這兩個零點不是數值調整結果，而是算子因子 $s(s-1)$ 的結構性結果。

## 直接邊界驗證

由

$$
g(x)=\frac{d}{dx}\left(x^2h'(x)\right),
$$

可得：

$$
\int_0^\infty g(x)\,dx
=\left[x^2h'(x)\right]_0^\infty=0.
$$

同時：

$$
\frac{g(x)}x=xh''(x)+2h'(x)
=\frac{d}{dx}\left(xh'(x)+h(x)\right),
$$

所以：

$$
\int_0^\infty g(x)\frac{dx}{x}
=\left[xh'(x)+h(x)\right]_0^\infty=0.
$$

---

# 3. 顯式參數化生成器

定義標準平滑 bump：

$$
\eta(q)=
\begin{cases}
\exp\!\left(-\dfrac1{1-q^2}\right),&|q|<1,\\[6pt]
0,&|q|\geq1.
\end{cases}
$$

參數取：

$$
\theta=(A,\mu,\sigma,\tau),
\qquad
A\in\mathbb C,
\quad\mu,\tau\in\mathbb R,
\quad\sigma>0.
$$

令

$$
h_\theta(x)
=A\,\eta\!\left(\frac{\log x-\mu}{\sigma}\right)
 e^{i\tau\log x}.
$$

其支撐為：

$$
\operatorname{supp}(h_\theta)
\subseteq
\left[e^{\mu-\sigma},e^{\mu+\sigma}\right].
$$

定義：

$$
g_\theta:=D(D+1)h_\theta.
$$

令

$$
q=\frac{\log x-\mu}{\sigma},
$$

則在 $|q|<1$ 時：

$$
\boxed{
 g_\theta(x)
 =A e^{i\tau\log x}
 \left[
 \frac{\eta''(q)}{\sigma^2}
 +\frac{1+2i\tau}{\sigma}\eta'(q)
 +(i\tau-\tau^2)\eta(q)
 \right]
}
$$

而在 $|q|\geq1$ 時 $g_\theta(x)=0$。

有限線性組合仍合法：

$$
g(x)=\sum_{j=1}^m c_jg_{\theta_j}(x),
$$

因為 $\mathcal G_{\mathrm{bump}}$ 是線性空間，雙消失矩與緊支撐平滑性均被保留。

**未宣稱：** 本文件不聲稱此族在最終 Weil 測試空間中稠密，也不聲稱所有負證人皆可由此族逼近。那是 `RH-W-02` 與 `RH-W-05` 的獨立 GAP。

---

# 4. 乘法相關閉合定理

對 $g\in C_c^\infty(0,\infty)$ 定義：

$$
f_g(x)
=\int_0^\infty g(xy)\overline{g(y)}\,dy.
$$

## 定理 4.1：支撐

若

$$
\operatorname{supp}(g)\subseteq[a,b],
\qquad0<a<b<\infty,
$$

則：

$$
\boxed{
\operatorname{supp}(f_g)
\subseteq\left[\frac ab,\frac ba\right]
}.
$$

因為積分非零必須同時存在：

$$
y\in[a,b],
\qquad xy\in[a,b].
$$

對單一 $g_\theta$：

$$
\operatorname{supp}(f_{g_\theta})
\subseteq[e^{-2\sigma},e^{2\sigma}].
$$

值得注意的是，此支撐比值與中心參數 $\mu$ 無關。

## 定理 4.2：平滑閉合

$$
\boxed{
f_g\in C_c^\infty(0,\infty)}.
$$

對每個 $k\geq0$，可在有限支撐上逐項微分：

$$
f_g^{(k)}(x)
=\int_0^\infty y^k g^{(k)}(xy)\overline{g(y)}\,dy.
$$

所有導數連續，且支撐仍落在 $[a/b,b/a]$。因此：

$$
C_c^\infty(0,\infty)\subset\mathcal W,
$$

故 `RH-W-01-D` 對此族關閉。

---

# 5. Mellin 相關恆等式

由 Fubini 與變數替換 $z=xy$：

$$
\boxed{
\widetilde{f_g}(s)
=\widetilde g(s)\,
\overline{\widetilde g(1-\overline s)}
}.
$$

在臨界線 $s=\tfrac12+it$ 上：

$$
\boxed{
\widetilde{f_g}\!\left(\frac12+it\right)
=
\left|
\widetilde g\!\left(\frac12+it\right)
\right|^2
\geq0
}.
$$

這是 Mellin 側的平方模恆等式；它不等於 Weil 算術側整體正性，也不能單獨推出 RH。

因 $\widetilde g(0)=\widetilde g(1)=0$：

$$
\widetilde{f_g}(0)=\widetilde{f_g}(1)=0.
$$

---

# 6. Hermitian 對稱與實值檢查

變數替換 $y=xz$ 給出：

$$
\boxed{
\frac1x f_g\!\left(\frac1x\right)
=\overline{f_g(x)}
}.
$$

因此顯式公式中的成對項為：

$$
f_g(x)+\frac1x f_g\!\left(\frac1x\right)
=2\operatorname{Re}f_g(x).
$$

且：

$$
\boxed{
f_g(1)=\int_0^\infty|g(y)|^2dy\geq0}.
$$

這些恆等式構成 `RH-W-01-F` 的符號與共軛回歸測試基準。

---

# 7. $x=1$ 的表面奇異消去

令

$$
N_f(x)
=f(x)+x^{-1}f(x^{-1})-2x^{-1}f(1),
$$

$$
D_0(x)=x-x^{-1}.
$$

對 $f\in C^1$，有：

$$
N_f(1)=D_0(1)=0.
$$

計算導數：

$$
N_f'(1)=f(1),
\qquad
D_0'(1)=2.
$$

所以：

$$
\boxed{
\lim_{x\to1}
\frac{N_f(x)}{x-x^{-1}}
=\frac{f(1)}2
}.
$$

對本族 $f_g\in C_c^\infty$，該被積函數在 $x=1$ 可連續延拓，故 `RH-W-01-C` 關閉。

---

# 8. 顯式公式各項的合法性

對 $f_g\in C_c^\infty(0,\infty)$：

## 8.1 算術和為有限和

因 $f_g$ 緊支撐，只有有限個整數 $n$ 能使：

$$
f_g(n)\neq0
\quad\text{或}\quad
f_g(1/n)\neq0.
$$

所以 von Mangoldt 和不是條件收斂問題，而是有限和。

## 8.2 阿基米德積分有限

積分只在 $f_g$ 的有限支撐範圍內可能非零；在 $x=1$ 的奇異已由上一節消去。

## 8.3 Mellin 變換垂直快速衰減

令 $x=e^u$，則：

$$
\widetilde f(\sigma+it)
=\int_{\mathbb R}f(e^u)e^{\sigma u}e^{itu}\,du.
$$

右側是緊支撐平滑函數的 Fourier 變換。因此對任意緊緻實部區間 $I\subset\mathbb R$ 與任意 $N$，一致地有：

$$
\sup_{\sigma\in I}
\left|\widetilde f(\sigma+it)\right|
=O_{I,N}\left((1+|t|)^{-N}\right).
$$

非平凡零點的實部位於緊緻帶 $[0,1]$；配合標準 Riemann–von Mangoldt 零點計數，得到：

$$
\sum_\rho|\widetilde f(\rho)|<\infty.
$$

故本族的零點和絕對收斂，B0 的對稱截斷與任何通常重排得到同一值。`RH-W-01-A/B` 對本族關閉。

---

# 9. 加法 Fourier 表示

令：

$$
x=e^v,
\qquad y=e^u,
$$

並定義對稱化函數：

$$
\phi(u):=e^{u/2}g(e^u).
$$

則：

$$
\boxed{
 e^{v/2}f_g(e^v)
 =\int_{\mathbb R}\phi(u+v)\overline{\phi(u)}\,du
}.
$$

也就是乘法相關在對數座標中成為標準加法自相關。

同時：

$$
\widetilde g\!\left(\frac12+it\right)
=\int_{\mathbb R}\phi(u)e^{itu}\,du.
$$

所以 Fourier 自相關定理重新給出：

$$
\widetilde{f_g}\!\left(\frac12+it\right)
=|\widehat\phi(t)|^2.
$$

這裡明確保留了 $e^{u/2}$ 權重；缺少此權重會把 B0 Mellin 臨界線錯誤轉成另一個 Fourier 慣例。

---

# 10. GAP 狀態更新

| ID | v0.1 | v0.2（本族） | 說明 |
|---|---|---|---|
| `RH-W-01-A` | reference / recheck | `CLOSED_FOR_GBUMP` | 各項均合法 |
| `RH-W-01-B` | open alternatives | `CLOSED_FOR_GBUMP` | 零點和絕對收斂 |
| `RH-W-01-C` | open per family | `CLOSED_FOR_GBUMP` | 極限為 $f(1)/2$ |
| `RH-W-01-D` | open | `CLOSED_FOR_GBUMP` | $f_g\in C_c^\infty$ |
| `RH-W-01-E` | open | `CLOSED_FOR_GBUMP` | $s(s-1)$ 精確消零 |
| `RH-W-01-F` | open | `PARTIAL_NUMERIC_CROSSCHECK` | 兩種相關實作已比對 |
| `RH-W-01-G` | open | `CLOSED_FOR_CCINF` | Mellin–Fourier 權重已固定 |
| `RH-W-01-H` | open | `PARTIAL_SCHEMA_VALIDATED` | metadata 與驗證器已建立 |

父節點仍不得標為完全關閉，因為尚未完成：

1. 對更廣泛測試函數類的形式化；
2. Lean／Isabelle 證明物件；
3. 最終閉包拓撲；
4. $Q_{B0}$ 在該拓撲的連續性／可閉性；
5. 負證人到本生成族的壓縮或稠密性。

---

# 11. 本輪沒有證明的事項

本輪沒有證明：

$$
Q_{B0}(g)\geq0.
$$

更沒有證明：

$$
\forall g\in\mathcal G_{B0},\quad Q_{B0}(g)\geq0.
$$

本輪只把「允許送進 Weil 機器的合法輸入」工程化。其價值是：後續 AI 不需要反覆猜測如何同時滿足兩個矩條件，也不能用數值近零冒充精確消失。

---

# 12. 下一個接力節點

推薦下一輪同時處理：

$$
\boxed{
\texttt{RH-W-02-A}:
\text{選擇候選閉包拓撲與完成空間}
}
$$

以及：

$$
\boxed{
\texttt{RH-W-02-B}:
\overline{\operatorname{span}(\mathcal G_{\mathrm{bump}})}^{\,\tau}
\stackrel{?}{=}
\mathcal H_{\mathrm{target}}
}
$$

在此之前不得宣稱 `GBUMP` 能捕捉所有負證人。

---

# 參考基準

1. Enrico Bombieri, “The Riemann Hypothesis,” in *The Millennium Prize Problems*, pp. 121–122：測試函數類、顯式公式與 Weil negativity criterion。
2. Jean-François Burnol, “The Explicit Formula in Simple Terms,” arXiv:math/9810169：乘法卷積、局部項與 Weil 判準的背景。
