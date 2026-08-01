# RH AI 研究起點 v1.9：三參數近零譜管

**日期：** 2026-07-24  
**研究節點：** RH-W-16-THREE-PARAMETER-TUBE  
**Batch 01 進度：** 16/20

## 本版新增

在 RH-W-15 的 $(d,\sigma)$ 二維管上加入真正改變字典的核尺度 $h$，建立：

$$
\boxed{
\left|h-\frac{1797}{10000}\right|\le10^{-8},\qquad
\left|d-\frac{893}{5000}\right|\le10^{-7},\qquad
|\sigma|\le10^{-7}
}.
$$

對盒內每一點，純有理 verifier 證明：

$$
\boxed{
10^{-8}<\lambda_{\min}(M(h,d,\sigma),G(h,d,\sigma))<5\times10^{-8}.
}
$$

## 方法

本版使用：

$$
\boxed{
\text{八角真實 Weil 區間矩陣}
+
\text{三線性凸插值}
+
\text{center／scale 純二階餘項}
}.
$$

尺度二階 Weil 整數界為：

$$
\boxed{17279,\,40860,\,78886}
$$

分別對應 correlation degree $3,5,7$。

完整三維合併列餘項為：

$$
1.1287365004114011\times10^{-9}.
$$

## 腔室

整個三維盒保持：

- active prime powers：$\{2,3,4\}$；
- $R_{\max}=1.43320054<\log5$；
- 最小 sample-to-knot margin 約 $0.02125231944$；
- spline piece 與 activation graph 不變。

## 可重現性

v1.9／RH-W-16 完整納入共用 interval、B-spline 與 jump-tail 模組，工程包解壓後可獨立執行 verifier，不再依賴未封裝的外部 Python 檔案。

## 聲明邊界

這只是固定十維混合階字典上的有限維連續近零正譜體積，不證明或反證 RH。

## 下一節點

$$
\boxed{
\texttt{RH-W-17-CHAMBER-AWARE-SUBDIVISION}
}
$$

下一輪將允許大參數盒接近或跨越 spline knot／prime-power 邊界，自動切分成固定腔室子盒並建立鄰接圖與逐盒證書。
