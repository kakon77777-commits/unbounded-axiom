# RH GAP 狀態更新 v0.3

**日期：** 2026-07-23  
**更新節點：** `RH-W-01`  
**新狀態：** `IN_PROGRESS_PARTIAL_CLOSURE_GBUMP`

## 已關閉的有限作用域

令：

$$
\mathcal G_{\mathrm{bump}}
=
\left\{D(D+1)h:h\in C_c^\infty(0,\infty)\right\},
\qquad
D=x\frac{d}{dx}.
$$

對此族已完成：

$$
\widetilde g(s)=s(s-1)\widetilde h(s),
$$

因此：

$$
\widetilde g(0)=\widetilde g(1)=0.
$$

並證明：

$$
f_g(x)=\int_0^\infty g(xy)\overline{g(y)}dy
\in C_c^\infty(0,\infty)\subset\mathcal W.
$$

同時已固定 Mellin–Fourier 轉換：

$$
\phi(u)=e^{u/2}g(e^u),
$$

$$
e^{v/2}f_g(e^v)
=\int_{\mathbb R}\phi(u+v)\overline{\phi(u)}du.
$$

## 仍未關閉

- `RH-W-02`：選擇完成空間與拓撲；
- `RH-W-03`：負證人的生成族壓縮；
- `RH-W-04`：生成族上的算術分解與可控餘項；
- `RH-W-05`：正性閉包與傳遞；
- Lean／Isabelle 形式化；
- 任何 Weil 正性或 RH 結論。

## 工程意義

本輪將「找一個同時滿足兩個矩條件的函數」從每個代理都要重新解決的人工障礙，轉換成可重用的生成算子。它是第一個被部分閉合並附帶程式回歸測試的 RH GAP 節點。
