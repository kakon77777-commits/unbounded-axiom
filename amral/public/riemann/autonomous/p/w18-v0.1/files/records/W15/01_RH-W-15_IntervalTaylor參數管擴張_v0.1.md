# RH-W-15：Interval–Taylor 參數管擴張

**版本：** v0.1  
**日期：** 2026-07-23  
**定位：** 有限維 Weil 二次型工程；不證明或反證黎曼猜想。

## 摘要

RH-W-14 在固定尺度

$$
h=\frac{1797}{10000}
$$

下，利用全域一階 Lipschitz 絕對值包絡，證明了半徑僅為

$$
\rho_d=\rho_\sigma=4\times10^{-12}
$$

的二維近零正譜參數管。本輪改用四角矩陣的 tensor-product 線性插值，保留參數變化的一階符號與 block 結構，僅將二階餘項區間化。

最終證明：對整個矩形

$$
\boxed{
\left|d-\frac{893}{5000}\right|\le10^{-7},
\qquad
|\sigma|\le10^{-7}
}
$$

均有

$$
\boxed{
10^{-8}<\lambda_{\min}(M(d,\sigma),G(d,\sigma))<5\times10^{-8}.
}
$$

每個參數方向的半徑擴大 $25{,}000$ 倍，矩形面積擴大

$$
(25{,}000)^2=625{,}000{,}000
$$

倍。

---

## 1. 字典與真參數

兩個基底通道分別使用 degree-$1$ 與 degree-$3$ centered cardinal B-spline：

$$
v_j^{(1)}(x)=h^{-1/2}\beta_1\!\left(\frac{x-t_j^{(1)}}h\right),
$$

$$
v_j^{(3)}(x)=h^{-1/2}\beta_3\!\left(\frac{x-t_j^{(3)}}h\right).
$$

中心為

$$
t_j^{(1)}=(j-2)d-\frac\sigma2,
\qquad
t_j^{(3)}=(j-2)d+\frac\sigma2,
$$

每通道五維，總維度十。

$d$ 控制同通道間距，$\sigma$ 控制兩通道相對平移；兩者都真正改變測試子空間。整體通道縮放 $\alpha$ 仍只屬換基底規範，不納入參數維度。

---

## 2. 四角線性插值

令

$$
\Theta=[d_0-\rho_d,d_0+\rho_d]
\times[-\rho_\sigma,\rho_\sigma].
$$

對任一矩陣元素 $F(d,\sigma)$，以四個角點值建立 tensor-product 線性插值 $B_F(d,\sigma)$。此插值在矩陣層級是四個角點矩陣的凸組合。

若四個角點的修正矩陣都正定，則其任意凸組合仍正定。因此，不需要把一階變化全部轉成絕對值 row radius；只需控制真函數與其雙線性插值之間的二階餘項。

對中心形式

$$
c_{ij}^{ab}=(i-j)d+b_{ab}\sigma,
$$

其中同通道 $b_{ab}=0$、跨通道 $|b_{ab}|=1$。若

$$
\left|\frac{d^2}{dc^2}W_r(c)\right|\le L_r^{(2)},
$$

則

$$
|W_r-B_{W_r}|
\le
\frac{L_r^{(2)}}2
\left((i-j)^2\rho_d^2+b_{ab}^2\rho_\sigma^2\right).
$$

Gram 元素同理，使用

$$
\left|\frac{d^2}{dc^2}G_r(c)\right|
\le\frac4{h^2}.
$$

---

## 3. 修正後的二階全域界

利用 cardinal B-spline 有限差分關係：

$$
\|\beta_r''\|_\infty\le4,
\qquad
\|\beta_r'''\|_\infty\le8,
$$

並分別控制端點、常數、prime-power 與阿基米德部分。

本輪特別保留了 spline 支撐外的阿基米德常數尾：

$$
\int_R^\infty\frac{dx}{e^x-e^{-x}}
=\operatorname{artanh}(e^{-R}).
$$

得到 correlation degree $3,5,7$ 的二階上界：

$$
L_3^{(2)}<2494,
\qquad
L_5^{(2)}<3110,
\qquad
L_7^{(2)}<3697.
$$

證書採用整數上界

$$
\boxed{2494,3110,3697}.
$$

完整二階餘項的最大列界為

$$
\boxed{
\epsilon_{\mathrm{Taylor}}
=1.0988000004025753\times10^{-9}.
}
$$

Gram 餘項最大列界為

$$
4.0257536752808504\times10^{-11}.
$$

---

## 4. 四角 exact 正定

四個角點為：

$$
(d_0\pm10^{-7},\ \pm10^{-7}).
$$

每個角點均重新組裝完整十維 Weil 區間矩陣，包含：

- 阿基米德背景；
- 常數項；
- 端點項；
- prime-power $2,3,4$；
- exact Gram 矩陣。

對每個角點建立

$$
C_v-10^{-8}G_v-
(\epsilon_{v,\mathrm{point}}+\epsilon_{\mathrm{Taylor}})I.
$$

純有理 $LDL^T$ 的十個 pivot 全部嚴格為正。由正定錐的凸性，四角修正矩陣的所有雙線性凸組合都正定，再由二階餘項界推出整個矩形內

$$
M(d,\sigma)-10^{-8}G(d,\sigma)\succ0.
$$

因此

$$
\lambda_{\min}>10^{-8}.
$$

---

## 5. 全參數管上界

沿用 RH-W-13 的整數 witness：

$$
\begin{aligned}
c={}&(
68190193,
137154794,
187700175,
137154794,
68190193,\\
&-3577963013,
-7569824004,
-10000000000,
-7569824004,
-3577963013)^T.
\end{aligned}
$$

先取四角 Rayleigh 分子與分母的凸包，再加入二階餘項的 quadratic envelope。得到整個管內：

$$
\frac{c^TM(d,\sigma)c}{c^TG(d,\sigma)c}
<4.02178\times10^{-8}
<5\times10^{-8}.
$$

所以

$$
\lambda_{\min}<5\times10^{-8}.
$$

---

## 6. 腔室穩定性

整個新參數管的最大相關支撐半徑仍滿足

$$
R_{\max}<\log5.
$$

因此全域 active von Mangoldt set 保持為

$$
\boxed{2,3,4}.
$$

所有 $\pm\log n$ 樣本到最近 spline knot 的最小嚴格距離為

$$
\boxed{
2.125231944005469\times10^{-2}.
}
$$

遠大於參數管尺度，故不存在：

- prime power 進場或退場；
- 樣本跨 knot；
- polynomial piece 身分改變；
- activation graph 改變。

---

## 7. 方法論意義

RH-W-14 使用的是

$$
\text{一階全域絕對值界}.
$$

RH-W-15 改為

$$
\boxed{
\text{四角嚴格矩陣}
+\text{凸性}
+\text{二階餘項}.
}
$$

一階變化不再被當成敵對擾動，而由角點矩陣自身保留其方向、符號與 block 抵消。只有真正無法由線性插值描述的曲率被轉成絕對值誤差。

這解釋了為何在相同近零譜帶下，半徑可一次放大 $25{,}000$ 倍。

---

## 8. 聲明邊界

本輪證明的是固定十維混合字典在一個連續二維參數矩形中的有限維正性與近零譜夾：

$$
10^{-8}<\lambda_{\min}<5\times10^{-8}.
$$

它不推出完整 Weil 判準，不證明 RH，也不構成 RH 的反例。
