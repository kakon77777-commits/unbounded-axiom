# RH-W-01：Weil 路線測試函數空間固定
## Riemann Hypothesis GAP Engineering Note v0.1

**研究計畫：** RH GAP Atlas / AI 數學工程化接力  
**節點：** `RH-W-01`  
**狀態：** `IN_PROGRESS`  
**性質：** 定義與作用域鎖定文件；不是 RH 證明，也不提出新的正性定理  
**日期：** 2026-07-23

---

## 0. 工程目的

Weil 顯式公式與 Weil 判準存在多種等價正規化。若不同 AI、論文或程式在沒有聲明的情況下交換 Mellin/Fourier 慣例、正負號、共軛、卷積、零點求和順序或測試函數空間，後續推導即使每行看似合理，也可能研究的是不同二次型。

本節點的目的不是證明正性，而是先建立一套**不可默默改寫的基準接口**：

$$
\text{輸入函數}
\longrightarrow
\text{Mellin 變換}
\longrightarrow
\text{零點側與算術側}
\longrightarrow
\text{Weil 二次型／符號判準}.
$$

完成標準不是「寫出熟悉公式」，而是所有後續代理都能回答：

1. 函數屬於哪個空間？
2. 每一個和與積分以什麼方式收斂？
3. 採用哪套 Mellin、卷積與對合？
4. 正性／負性的符號如何由該套慣例導出？
5. 若換用另一套慣例，轉換映射是什麼？

---

# 1. 基準版本 B0：Bombieri／Clay 的乘法半群表述

本工程第一階段選定 Clay Mathematics Institute《Millennium Prize Problems》中 Bombieri 的 RH 章節作為 **B0 基準**。此選擇不是宣稱它是唯一或最適合計算的版本，而是因其函數類、Mellin 變換、零點和的取法及 Weil 判準在同一處明確給出。

## 1.1 測試函數類

令 $\mathcal W$ 為正半軸 $\mathbb R_+=(0,\infty)$ 上的複值函數 $f$，滿足：

1. $f$ 連續，且除有限多點外連續可微；
2. 在例外點，$f$ 與 $f'$ 至多具有第一類不連續；
3. 例外點的函數值取左右極限平均；
4. 存在 $\delta>0$，使

$$
f(x)=O(x^\delta),\qquad x\to0^+,
$$

及

$$
f(x)=O(x^{-1-\delta}),\qquad x\to+\infty.
$$

這裡的 $\delta$ 是函數資料的一部分；不同函數可有不同的可用 $\delta$。

## 1.2 Mellin 變換

採用：

$$
\widetilde f(s)
:=
\int_0^\infty f(x)x^s\frac{dx}{x}.
$$

在上述條件下，$\widetilde f$ 至少在帶狀區域

$$
-\delta<\operatorname{Re}(s)<1+\delta
$$

解析。

**工程鎖定：** 本包內符號 $\widetilde f$ 一律表示此 Mellin 慣例，不得在未改版本號的情況下改成 $x^{s-1}dx$ 以外的平移版本。注意兩者在形式上相同，因為 $x^s\,dx/x=x^{s-1}dx$；但程式接口仍以本式為唯一宣告。

## 1.3 von Mangoldt 函數

$$
\Lambda(n)=
\begin{cases}
\log p,&n=p^a,\quad p\text{ 為質數},\ a\geq1,\\
0,&\text{其他}.
\end{cases}
$$

## 1.4 顯式公式 B0

對 $f\in\mathcal W$，取非平凡零點和為

$$
\lim_{T\to+\infty}
\sum_{|\operatorname{Im}(\rho)|<T}\widetilde f(\rho),
$$

則基準顯式公式為：

$$
\widetilde f(0)
-
\sum_\rho\widetilde f(\rho)
+
\widetilde f(1)
=
\sum_{n=1}^\infty\Lambda(n)
\left(
 f(n)+\frac1n f\!\left(\frac1n\right)
\right)
+(\log4\pi+\gamma)f(1)
$$

$$
\qquad+
\int_1^\infty
\left(
 f(x)+\frac1x f\!\left(\frac1x\right)-\frac2x f(1)
\right)
\frac{dx}{x-x^{-1}}.
$$

為避免後續代理把等式兩側任意移項並改變符號，定義：

$$
E_{\mathrm{zero}}(f)
:=
\widetilde f(0)-\sum_\rho\widetilde f(\rho)+\widetilde f(1),
$$

$$
E_{\mathrm{arith}}(f)
:=
\sum_{n=1}^\infty\Lambda(n)
\left(
 f(n)+\frac1n f\!\left(\frac1n\right)
\right)
+(\log4\pi+\gamma)f(1)
$$

$$
\qquad+
\int_1^\infty
\left(
 f(x)+\frac1x f\!\left(\frac1x\right)-\frac2x f(1)
\right)
\frac{dx}{x-x^{-1}}.
$$

故 B0 的合法等式固定為：

$$
E_{\mathrm{zero}}(f)=E_{\mathrm{arith}}(f).
$$

---

# 2. Weil 判準所需的特殊函數

## 2.1 基準乘法相關型

取 $g\in\mathcal W$，定義

$$
f_g(x)
:=
\int_0^\infty g(xy)\overline{g(y)}\,dy.
$$

並要求兩個消失矩條件：

$$
\int_0^\infty g(x)\frac{dx}{x}=0,
\qquad
\int_0^\infty g(x)\,dx=0.
$$

在 B0 慣例下，Weil 判準可表述為：RH 等價於對所有上述 $g$，顯式公式右側對 $f_g$ 為非正。

因此本工程定義：

$$
Q_{B0}(g):=-E_{\mathrm{arith}}(f_g).
$$

此時判準寫成：

$$
RH
\Longleftrightarrow
\forall g\in\mathcal G_{B0},\quad Q_{B0}(g)\geq0,
$$

其中

$$
\mathcal G_{B0}
:=
\left\{
 g\in\mathcal W:
 \int_0^\infty g(x)\frac{dx}{x}=0,
 \ \int_0^\infty g(x)dx=0,
 \ f_g\in\mathcal W
\right\}.
$$

最後一個條件 $f_g\in\mathcal W$ 在工程上不得默認，必須逐族證明或由更強的輸入空間條件保證。

## 2.2 符號防錯規則

文獻可將同一判準稱為 Weil positivity 或 Weil negativity，差異常來自：

- 把零點側或算術側定義為二次型；
- 把所有項移到等式另一側；
- 在二次型前加負號；
- 採用不同卷積／對合。

所以禁止只寫「Weil 正性」。後續每份文件必須寫出：

$$
Q(g):=\text{完整公式},
$$

再聲明：

$$
Q(g)\geq0
\quad\text{或}\quad
Q(g)\leq0.
$$

---

# 3. `RH-W-01` 子 GAP 分解

## `RH-W-01-A`：函數類作用域證明

**義務：** 對 $\mathcal W$ 的每一條規則，證明顯式公式中所有項有意義。  
**失敗證人：** 找到 $f\in\mathcal W$，使任一項發散或零點和的指定極限不存在。  
**狀態：** `REFERENCE_ESTABLISHED / LOCAL_RECHECK_REQUIRED`

工程上不重新宣稱證明 Bombieri／Weil 的總定理，但對任何新生成族仍須重新檢查其確實落入 $\mathcal W$。

## `RH-W-01-B`：零點和求和規則鎖定

**義務：** 一律採用

$$
\lim_{T\to\infty}\sum_{|\operatorname{Im}\rho|<T}.
$$

若改用按模長、成對對稱或 Hadamard 正則化，必須建立等價性。  
**失敗證人：** 兩種排序給出不同極限或其中一種不收斂。  
**狀態：** `OPEN_FOR_ALTERNATIVE_NORMALIZATIONS`

## `RH-W-01-C`：$x=1$ 的阿基米德積分可積性

積分核在 $x=1$ 形式上具有奇異分母：

$$
x-x^{-1}\to0.
$$

**義務：** 對候選函數族證明分子中的減項

$$
f(x)+x^{-1}f(x^{-1})-2x^{-1}f(1)
$$

提供足夠消去，使積分在 $x=1$ 附近合法。  
**失敗證人：** 局部展開留下不可積的一階奇異。  
**狀態：** `OPEN_PER_GENERATOR_FAMILY`

## `RH-W-01-D`：乘法相關函數閉合

**義務：** 給定候選 $g$，證明

$$
f_g(x)=\int_0^\infty g(xy)\overline{g(y)}dy
$$

存在且屬於 $\mathcal W$。  
**失敗證人：** $f_g$ 在 $0$ 或 $\infty$ 衰減不足、正則性不足，或積分不收斂。  
**狀態：** `OPEN`

## `RH-W-01-E`：兩個消失矩條件的接口

由 B0 Mellin 慣例：

$$
\widetilde g(0)=\int_0^\infty g(x)\frac{dx}{x},
\qquad
\widetilde g(1)=\int_0^\infty g(x)dx.
$$

故兩矩條件即：

$$
\widetilde g(0)=\widetilde g(1)=0.
$$

**義務：** 所有生成器構造必須顯式保存這兩條件，不能事後以數值近似 $0$ 代替精確等式。  
**失敗證人：** 任一生成器僅近似消失，或投影修正破壞其他條件。  
**狀態：** `OPEN_FOR_CONSTRUCTIVE_PARAMETERIZATION`

## `RH-W-01-F`：正負號與共軛一致性

**義務：** 驗證程式、自然語言與形式化版本均使用同一：

- $f_g$ 定義；
- 複共軛位置；
- $Q_{B0}=-E_{\mathrm{arith}}$；
- 判準 $Q_{B0}\geq0$。

**失敗證人：** 對同一 $g$，兩個模組輸出相反符號但都宣稱「通過」。  
**狀態：** `OPEN_UNTIL_CROSS_IMPLEMENTATION_TEST`

## `RH-W-01-G`：替代表示轉換器

**義務：** 建立 B0 與加法變數

$$
x=e^u
$$

下 Fourier 型公式的明確轉換，包含測度：

$$
\frac{dx}{x}=du,
$$

以及函數重標度。  
**失敗證人：** 轉換後遺失 $e^{u/2}$ 類權重、平移 Mellin 參數或共軛。  
**狀態：** `OPEN`

## `RH-W-01-H`：機器可判定的合法性前置條件

**義務：** 把「正則、衰減、矩消失、閉合、積分可積」轉成可被 CAS、數值程式或 Lean/Isabelle 前端檢查的 metadata。  
**失敗證人：** 代理只憑函數外觀判斷合法，未提供界或證明物件。  
**狀態：** `OPEN`

---

# 4. 本輪已固定與尚未固定

## 4.1 已固定

- 正半軸乘法表述；
- 測試函數類 $\mathcal W$ 的 B0 規則；
- Mellin 慣例；
- 非平凡零點和的截斷方式；
- 顯式公式的兩側命名；
- $f_g$ 的相關型；
- 兩個消失矩；
- 本工程二次型 $Q_{B0}$ 的符號。

## 4.2 尚未固定

- 最適合 AI 搜尋的生成族 $\mathcal G$；
- $\mathcal W$ 上後續閉包所用拓撲；
- $Q_{B0}$ 是否在該拓撲連續或可閉；
- 負證人能否壓縮至可計算生成族；
- B0 到 Schwartz／Paley–Wiener／加法 Fourier 版本的完整互譯；
- 形式化函數空間庫是否足以直接承載所有條件。

這些分別進入 `RH-W-02` 至 `RH-W-05`，不得在 `RH-W-01` 中偷渡完成。

---

# 5. AI 任務接口

任何代理提交候選 $g$ 時，必須附：

```yaml
candidate_id: string
formula: exact symbolic expression
domain: (0, infinity)
regularity_proof: reference_or_derivation
bound_at_zero: "|g(x)| <= C x^a"
bound_at_infinity: "|g(x)| <= C x^{-1-a}"
vanishing_mellin_0: exact_proof
vanishing_mellin_1: exact_proof
correlation_exists: proof_or_bound
correlation_in_W: proof_or_bound
sign_convention: Q_B0 = -E_arith
numerical_checks: optional_only
unproved_items: explicit_list
```

缺少任一必填欄，候選不得進入正性測試，只能標為：

`INADMISSIBLE_PENDING_DOMAIN_CHECK`。

---

# 6. 工程判定

`RH-W-01` 尚未完全關閉，但已從一個含糊句子：

> 「取適當測試函數空間。」

轉換成八個可接力的子 GAP。第一個版本的價值不是解決 RH，而是阻止後續 AI 在不知不覺中更換問題。

目前工程狀態：

$$
\boxed{
\texttt{RH-W-01: IN\_PROGRESS}
}
$$

下一個推薦工作單位不是 `RH-W-02` 的全體，而是：

$$
\boxed{
\texttt{RH-W-01-D/E}:
\text{構造一個可參數化、精確滿足兩矩消失且閉合於 }f_g\text{ 的生成族。}
}
$$

---

# 參考來源

1. Enrico Bombieri, “The Riemann Hypothesis,” in *The Millennium Prize Problems*, Clay Mathematics Institute / Cambridge University Press, section 5, pp. 121–122.  
   https://www.claymath.org/library/monographs/MPPc.pdf
2. Jean-François Burnol, “The Explicit Formula in Simple Terms,” arXiv:math/9810169.  
   https://arxiv.org/abs/math/9810169

