# RH-W-14：Lipschitz 證書與保守性審計

**版本：** v0.1  
**日期：** 2026-07-23

---

## 1. 為什麼先做微小參數管

RH-W-13 的最低廣義譜值只有約

$$
4\times10^{-8}.
$$

要證明連續參數區域，不能只在幾個角點採樣，也不能假設特徵值在盒內單調。必須同時控制：

- Weil 矩陣的連續變化；
- Gram 度量的連續變化；
- prime-power 活化圖；
- spline polynomial piece；
- 固定 witness 的 Rayleigh 上界。

因此本輪先使用全域 Lipschitz envelope 建立一個尺寸很小、但數學上真正連續的參數管。

---

## 2. 證書不是角點插值

證書沒有使用：

$$
\text{「所有角點為正」}\Rightarrow\text{盒內為正}
$$

這種一般情況下不成立的推論。

真正使用的是：

$$
M(\theta)-\delta G(\theta)
=
C-\delta G_0+E(\theta),
$$

並對所有 $\theta\in\mathcal T$ 證明：

$$
\|E(\theta)\|_2
\le
\|E(\theta)\|_\infty
\le
\epsilon.
$$

然後 exact $LDL^T$ 驗證：

$$
C-\delta G_0-\epsilon I\succ0.
$$

這才推出整個參數管內的正性。

---

## 3. 為何 $M$ 與 $G$ 必須一起變動

RH-W-13 已經發現：若 $M$ 使用量化參數，而 $G$ 使用未量化參數，可能把正值偽造成負值。

本輪從一開始就以同一參數盒控制：

$$
M(d,\sigma)
\quad\text{與}\quad
G(d,\sigma).
$$

下界中使用的是：

$$
\Delta M-\delta\Delta G,
$$

而不是只控制 $\Delta M$。

上界 witness 同樣同時使用：

$$
q_{\max}
=
q_0+\Delta q,
$$

$$
g_{\min}
=
g_0-\Delta g.
$$

只有在

$$
q_{\max}<Ug_{\min}
$$

時，才接受整個參數管的 Rayleigh 上界。

---

## 4. 嚴格界與實際變化差距很大

80 位高精度浮點抽樣得到：

| 樣本 | $\lambda_0$ |
|---|---:|
| 中心 | $3.995905931516698\times10^{-8}$ |
| $d$ 下端 | $3.995905917800754\times10^{-8}$ |
| $d$ 上端 | $3.995905930007202\times10^{-8}$ |
| $\sigma$ 下端 | $3.995905936390289\times10^{-8}$ |
| $\sigma$ 上端 | $3.995905925255308\times10^{-8}$ |
| 一個負角點 | $3.995905938391824\times10^{-8}$ |
| 一個正角點 | $3.995905926204950\times10^{-8}$ |

樣本最大與最小之差只有約：

$$
2.06\times10^{-16}.
$$

但嚴格下界使用的全矩陣 combined row bound 是：

$$
2.30\times10^{-8}.
$$

這不是矛盾。前者只是少量高精度樣本的實際譜漂移；後者是對所有矩陣元素、所有參數點、所有向量方向同時成立的全域絕對值上界。

它揭示下一個明確瓶頸：

$$
\boxed{
\text{目前可證明的參數管寬度，主要受保守擾動界限制，}
\text{而不是受觀察到的譜不穩定限制。}
}
$$

---

## 5. 為什麼不能把浮點平穩性直接當成大管證書

即使高精度樣本顯示最低譜幾乎不動，仍可能存在：

- 樣本間的局部彎曲；
- 更高階交叉項；
- Gram 條件數放大；
- 支撐或 knot 邊界附近的導數變化；
- 數值求解器漏掉的極窄異常。

因此本輪只宣稱由 exact Lipschitz envelope 涵蓋的矩形。

---

## 6. 本輪信任邊界

### 嚴格證書路徑

- Python `int` 與 `Fraction`；
- 有理級數的 $\log$、$\pi$、$\gamma$ 區間；
- 有理平方根區間；
- 有文件化 outward expansion 的 `Decimal.exp`；
- B-spline 全域導數不等式；
- 對稱矩陣列和擾動界；
- 純有理 $LDL^T$；
- 固定整數 Rayleigh witness。

### 僅交叉檢查

- mpmath 55 位積分；
- SciPy 廣義特徵值；
- 七個中心、邊界與角點樣本。

浮點抽樣不參與 exact 證書。

---

## 7. 下一個工程方向

全域界

$$
\|\beta_r'\|_\infty\le1,
\qquad
\|\beta_r''\|_\infty\le4
$$

非常穩健，但沒有利用：

- 每個元素實際位於哪個 spline piece；
- 導數的符號；
- 不同元素間的 Toeplitz／block 結構；
- 最低模態的方向；
- 一階項可能互相抵消；
- 二階 Taylor 餘項通常遠小於全域 Lipschitz 界。

因此下一輪應建立：

$$
\boxed{
\texttt{RH-W-15-INTERVAL-TAYLOR-TUBE-EXPANSION}
}
$$

把逐元素全域 Lipschitz，升級成：

$$
M(\theta)
=
M_0+
\sum_a \partial_aM_0\,\Delta\theta_a+
R_M(\theta),
$$

$$
G(\theta)
=
G_0+
\sum_a \partial_aG_0\,\Delta\theta_a+
R_G(\theta),
$$

並對一階矩陣保留符號與結構，只對二階餘項使用絕對值界。

目標不是繼續壓低中心譜值，而是把已證明的參數管擴大數個數量級。
