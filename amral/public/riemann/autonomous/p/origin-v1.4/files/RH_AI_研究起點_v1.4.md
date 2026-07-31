# RH AI 研究起點 v1.4：核靈敏度—正則性對偶

- 日期：2026-07-23
- 原始研究構想：Neo.K
- 數學工程：Aletheia（GPT-5.6 Thinking）
- 狀態：非證明研究工程；不宣稱 RH 已解決

---

## 1. 本版里程碑

`v1.3` 發現 cubic B-spline 自相關使 prime-$3$ 邊界以七階軟啟動：

$$
p_3(\mu)
\propto
-\mu_+^7.
$$

`v1.4` 將此現象推廣到完整 centered cardinal B-spline 核族。

對 degree-$m$ 與 degree-$n$ 基底：

$$
\beta_m*\beta_n=\beta_{m+n+1}.
$$

因此 prime-power 支撐邊界的啟動階數為：

$$
\boxed{r=m+n+1}.
$$

自相關特例為：

$$
\boxed{r=2m+1}.
$$

---

## 2. 核設計的真正 trade-off

同一個 $r$ 同時控制：

- prime boundary 局部振幅 $O(\varepsilon^r)$；
- 邊界正則性 $C^{r-1}$；
- Fourier 衰減 $|\xi|^{-(r+1)}$；
- 本工程保守 Laplace 尾界 $O(K^{-r})$。

所以：

$$
\text{更光滑}
\Longrightarrow
\text{更容易證書化，但更難看見新 prime layer}.
$$

$$
\text{更尖銳}
\Longrightarrow
\text{更敏感，但尾界與條件控制更昂貴}.
$$

不存在單一 degree 同時最優。

---

## 3. 十六個數量級的差異

沿用 `RH-W-10` 的無因次穿透深度：

$$
\varepsilon
\approx
4.7510957191\times10^{-4}.
$$

prime-$3$ 局部元素：

$$
|p_3|_{m=1}
\approx
1.13374\times10^{-11},
$$

$$
|p_3|_{m=3}
\approx
6.87717\times10^{-28}.
$$

因此：

$$
\boxed{
\frac{|p_3|_{m=1}}{|p_3|_{m=3}}
\approx1.64856\times10^{16}
}.
$$

先前 prime-$3$ 幾乎不可見，不是算術項本身必然弱，而是 degree-$7$ 相關核把邊界事件平滑掉了。

---

## 4. 下一代字典

本版不再尋找「最佳單一核」，而採混合階架構：

$$
\boxed{m=1\quad\text{感測通道}}
$$

與

$$
\boxed{m=3\quad\text{證書通道}}.
$$

其 block 相關階數為：

$$
1\times1\to3,
\qquad
1\times3\to5,
\qquad
3\times3\to7.
$$

同一個 Hermitian 矩陣因此同時攜帶：

$$
\varepsilon^3,
\quad
\varepsilon^5,
\quad
\varepsilon^7
$$

三個 prime boundary 感測尺度。

下一節點：

$$
\boxed{
\texttt{RH-W-12-MIXED-ORDER-DICTIONARY}
}.
$$

目標是建立第一份 degree-$1/3$ 真實 Weil block Toeplitz 區間矩陣與 exact Gram 證書。

---

## 5. 邊界

本版沒有：

- RH 證明；
- 真實負證人；
- 無限維正性結論；
- 將局部核效應等同於 zeta 離軸零點。

本版完成的是核選擇 GAP 的工程化：把「光滑一點比較好」改寫成可計算、可比較、可接力的 Pareto 問題。
