# RH AI 研究起點 v1.5：混合階字典與跨正則性抵消

- 日期：2026-07-23
- 原始研究構想：Neo.K
- 數學工程：Aletheia（GPT-5.6 Thinking）
- 狀態：非證明研究工程；不宣稱 RH 已解決

---

## 1. 本版里程碑

`v1.4` 建立核階數的對偶律：低階 B-spline 具有較高 prime-boundary 靈敏度，高階 B-spline 具有較佳阿基米德尾界與證書條件。

`v1.5` 第一次把兩種正則性放入同一個真實 Weil 測試空間：

$$
v^{(1)}_j=h^{-1/2}\beta_1((x-t_j)/h),
\qquad
v^{(3)}_j=h^{-1/2}\beta_3((x-t_j)/h).
$$

由卷積閉合：

$$
1\times1\to\beta_3,
\qquad
1\times3\to\beta_5,
\qquad
3\times3\to\beta_7.
$$

因此同一個矩陣同時攜帶：

$$
\varepsilon^3,\qquad\varepsilon^5,\qquad\varepsilon^7
$$

三種算術啟動尺度。

---

## 2. 第一個混合階嚴格腔室

固定：

$$
h=\frac3{20},\qquad d=\frac9{40},\qquad N=5\text{ per channel}.
$$

總維度為 $10$，最大相關半徑為 $3/2<\log5$，故完整 von Mangoldt 集合正好為：

$$
\{2,3,4\}.
$$

三種 block 具有不同的支撐視野，形成多距離算術感測器，而不是同一張活化圖的重複副本。

---

## 3. exact 譜夾

全 mixed interval family 的純有理 $LDL^T$ 證明：

$$
\lambda_{\min}^{\rm mixed}>\frac1{2000}.
$$

有理整數 witness 則證明：

$$
\lambda_{\min}^{\rm mixed}<\frac1{1000}.
$$

因此：

$$
\boxed{
5\times10^{-4}
<\lambda_{\min}^{\rm mixed}
<10^{-3}
}.
$$

同時，隔離通道 exact 下界為：

$$
\lambda_{\min}^{(m=3)}>\frac1{250}=0.004,
$$

$$
\lambda_{\min}^{(m=1)}>\frac1{20}=0.05.
$$

所以 mixed 低模態不是任一單獨通道的延伸。

---

## 4. 跨正則性抵消模態

對 exact witness：

$$
Q(c)=Q_{11}(c_1)+2Q_{13}(c_1,c_3)+Q_{33}(c_3).
$$

驗證器證明：

$$
Q_{11}>0,
\qquad
Q_{33}>0,
\qquad
2Q_{13}<0,
\qquad
Q(c)>0.
$$

cross-block 抵消約 $93.4\%$ 的兩個 self-block 能量，留下約：

$$
9.7385\times10^{-4}
$$

的廣義 Rayleigh 值。

因此正式命名：

$$
\boxed{\text{跨正則性抵消模態}}
$$

它說明混合核不是「感測器加證書器」，而是會產生單核空間不存在的新譜幾何。

---

## 5. 工程閉合

本版完成：

- degree $3,5,7$ 通用 B-spline correlation core；
- 三種 degree-specific 阿基米德尾界；
- block-wise prime-power 支撐編譯；
- exact mixed Gram；
- exact mixed 下界；
- exact rational witness 上界；
- exact self/cross 符號分解；
- 80 位 mpmath 獨立交叉檢查。

---

## 6. 邊界與下一節點

本版仍是有限維證書：

$$
\text{mixed 10D positivity}\centernot\Longrightarrow RH.
$$

未找到真實 Weil 負 witness。

下一節點：

$$
\boxed{\texttt{RH-W-13-CROSS-REGULARITY-CONTINUATION}}.
$$

將沿 mixed witness 自適應調整：

$$
h,\qquad d,\qquad \alpha
$$

其中 $\alpha$ 控制兩通道的相對尺度或預條件，目標是分離：

- 真正的 Weil 能量下降；
- Gram 近線性依賴；
- prime-power block 對抵消方向的貢獻；
- 穩定低譜帶與偶然單點抵消。
