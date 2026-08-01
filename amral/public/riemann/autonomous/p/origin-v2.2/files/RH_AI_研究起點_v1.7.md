# RH AI 研究起點 v1.7：嚴格二維參數管

**日期：** 2026-07-23  
**研究節點：** RH-W-14-RIGOROUS-PARAMETER-TUBE

## 本版新增

RH-W-14 把 v1.6 的十維近零單點證書擴張為第一個連續二維參數管。

固定：

$$
h=\frac{1797}{10000},
$$

在

$$
\left|d-\frac{893}{5000}\right|\le4\times10^{-12},
\qquad
|\sigma|\le4\times10^{-12}
$$

內，純有理驗證器證明：

$$
\boxed{
10^{-8}
<
\lambda_{\min}(M(d,\sigma),G(d,\sigma))
<
5\times10^{-8}
}
$$

對參數矩形中的每一個點成立。

## 主要方法

1. 排除不改變廣義譜的 $\alpha$ 通道縮放；
2. 只保留真正改變子空間的 $d$ 與 $\sigma$；
3. 使用 cardinal B-spline 全域導數界：

$$
0\le\beta_r\le1,
\qquad
\|\beta_r'\|_\infty\le1,
\qquad
\|\beta_r''\|_\infty\le4;
$$

4. 建立 Weil 元素的中心 Lipschitz 界：

$$
L_3\le175,
\qquad
L_5\le215,
\qquad
L_7\le253;
$$

5. 同時控制 $M(d,\sigma)$ 與 $G(d,\sigma)$；
6. 使用列和擾動界與純有理 $LDL^T$ 證明整管下界；
7. 使用固定整數 witness 證明整管上界。

## 腔室穩定性

整個參數管內：

- 最大相關支撐半徑仍小於 $\log5$；
- 全域 prime-power 集合保持 $\{2,3,4\}$；
- 最小 sample-to-knot 距離大於 $0.02125$；
- spline polynomial piece 與活化圖保持不變。

## 保守性發現

高精度樣本顯示管內最低譜的實際漂移只有約

$$
2\times10^{-16},
$$

但全域 exact envelope 必須預留約

$$
2.3\times10^{-8}
$$

的矩陣擾動。

因此目前管寬主要受證書保守性限制，不是受觀察到的譜不穩定限制。

## 證書狀態

- 中心 RH-W-13 exact 證書：通過；
- 二維參數管 exact 證書：通過；
- Gram 在整管內正定：通過；
- prime-power 腔室固定：通過；
- 高精度浮點抽樣：通過；
- RH claim：False。

## 聲明邊界

本版只證明固定十維 mixed B-spline 子空間上的連續近零正譜帶。它不證明 RH，也沒有提供 RH 反例。

## 下一節點

$$
\boxed{
\texttt{RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION}
}
$$

下一輪將保留一階矩陣導數的符號與 block 結構，只對二階餘項使用 interval bound，以擴大參數管，並嘗試加入 $h$ 方向形成第一個三維參數盒。
