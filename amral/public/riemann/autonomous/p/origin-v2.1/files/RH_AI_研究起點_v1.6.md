# RH AI 研究起點 v1.6：跨正則性近零譜帶

**日期：** 2026-07-23  
**研究節點：** RH-W-13-CROSS-REGULARITY-CONTINUATION

## 本版新增

RH-W-13 延續 degree-$1/3$ mixed B-spline Weil 字典，完成四項更新：

1. 證明完整通道縮放 $\alpha$ 只是可逆 congruence，不改變廣義譜；
2. 以兩通道相對平移 $\sigma$ 作為真正延拓參數；
3. 發現並排除因 $M/G$ 不一致量化造成的假負候選；
4. 以 derivative-jump 精確尾式，證明十維 mixed spectral bottom 滿足

$$
\boxed{10^{-8}<\lambda_{\min}(M,G)<5\times10^{-8}}.
$$

## 固定候選

$$
h=\frac{1797}{10000},\qquad
 d=\frac{893}{5000},\qquad
 \sigma=0,
$$

每通道五個基底，總維度十。

最大支撐半徑小於 $\log5$，完整 prime-power 集合為

$$
2,3,4.
$$

## 工程修正

廣義譜搜尋必須由同一 canonical parameter object 同時生成 $M$ 與 $G$。本版保留一個可重放的錯誤案例：只量化 $M$、不量化 $G$，會把約 $+8.76\times10^{-8}$ 偽造成約 $-3.32\times10^{-7}$。

## 證書狀態

- mixed lower bound：$\lambda_{\min}>10^{-8}$；
- rational witness upper bound：$\lambda_{\min}<5\times10^{-8}$；
- isolated $m=1$：$\lambda_{\min}>4\times10^{-4}$；
- isolated $m=3$：$\lambda_{\min}>10^{-7}$；
- exact verifier：通過；
- 80 位 mpmath 獨立檢查：通過；
- RH claim：False。

## 聲明邊界

本版只證明固定十維子空間上的嚴格正性與近零譜夾。它不證明 RH，也不提供 RH 反例。

## 下一節點

$$
\boxed{\texttt{RH-W-14-RIGOROUS-PARAMETER-TUBE}}
$$

下一輪將不只證明單一參數點，而是嘗試證明一個有理參數盒

$$
(h,d,\sigma)\in\mathcal B
$$

內的 mixed gap 仍保持正且維持低譜，建立第一個嚴格的「參數管／低譜帶」證書。
