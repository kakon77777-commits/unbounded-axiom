# RH AI 研究起點 v1.8：Interval–Taylor 參數管

**日期：** 2026-07-23  
**研究節點：** RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION  
**Batch 01 進度：** 15/20

## 本版新增

固定

$$
h=\frac{1797}{10000},
$$

將 RH-W-14 的二維參數管由

$$
\rho_d=\rho_\sigma=4\times10^{-12}
$$

擴大為

$$
\boxed{
\rho_d=\rho_\sigma=10^{-7}
}.
$$

對新矩形中的每一點，純有理 verifier 證明：

$$
\boxed{
10^{-8}<\lambda_{\min}(M(d,\sigma),G(d,\sigma))<5\times10^{-8}.
}
$$

每個方向半徑擴大 $25{,}000$ 倍，面積擴大 $6.25\times10^8$ 倍。

## 方法升級

RH-W-14 把全部一階變化轉成全域絕對值擾動。RH-W-15 改為：

$$
\boxed{
\text{四角嚴格矩陣}
+\text{雙線性凸組合}
+\text{二階 Taylor 餘項}.
}
$$

一階符號、Toeplitz/block 結構與跨正則性抵消由角點矩陣保留，只有曲率餘項被絕對值包住。

## 重要回溯修正

RH-W-14 的阿基米德一階導數界漏掉 spline 支撐外仍存在的 $-2f(0)$ 正規化尾。精確尾為

$$
\int_R^\infty\frac{dx}{e^x-e^{-x}}
=\operatorname{artanh}(e^{-R}).
$$

修正後一階界由

$$
(175,215,253)
$$

更新為

$$
\boxed{(179,218,255)}.
$$

重新執行 exact $LDL^T$ 後，RH-W-14 原參數管結論仍成立；舊推導由修正版取代。

## W-15 二階界

correlation degree $3,5,7$ 的整數二階上界為：

$$
\boxed{2494,3110,3697}.
$$

新管的全矩陣二階 combined row remainder 為

$$
1.0988000004025753\times10^{-9}.
$$

## 腔室

整個新矩形仍保持：

- active prime powers：$\{2,3,4\}$；
- $R_{\max}<\log5$；
- 最小 sample-to-knot margin 約 $0.0212523$；
- spline piece 與 activation graph 不變。

## 聲明邊界

本版只證明固定十維 mixed B-spline 字典上的連續有限維近零正譜帶。它不證明或反證 RH。

## 下一節點

$$
\boxed{
\texttt{RH-W-16-THREE-PARAMETER-TUBE}
}
$$

下一輪加入尺度 $h$，建立第一個 $(h,d,\sigma)$ 三維參數盒，並同步控制 knot 移動、Gram 尺度變化、prime-power 樣本正規化與阿基米德尾。
