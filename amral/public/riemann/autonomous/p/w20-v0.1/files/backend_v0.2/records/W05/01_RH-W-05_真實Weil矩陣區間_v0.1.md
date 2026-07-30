# RH-W-05：第一份真實 Weil 矩陣有理區間
## 從浮點候選到可重播的 $2\times2$ 數學收據

**版本：** v0.1  
**日期：** 2026-07-23  
**研究計畫：** RH GAP Atlas／AI 數學工程化接力  
**父節點：** `RH-W-04-GALERKIN-CERTIFICATE`  
**本輪節點：** `RH-W-05-REAL-MATRIX-ENCLOSURE`  
**狀態：** `CLOSED_FOR_PRIME_FREE_2D_SPLINE_BASIS`  
**性質：** 真實 Riemann zeta Weil 泛函的有限維嚴格計算；不是 RH 證明，也不是 RH 反例

---

# 0. 本輪結論

本輪完成第一份不依賴合成零點、不使用有限零點截斷、也不把普通浮點誤差當證書的真實 Weil 矩陣：

$$
M_{ij}=Q_W(v_i,v_j)=W(v_i*\widetilde v_j),
\qquad 1\le i,j\le2.
$$

計算採用完整 Riemann–Weil 顯式公式，並以有理區間包住每一項。得到：

$$
M_{11}=M_{22}
\in
[0.42142579326768431214,\,
 0.42433406315905086714],
$$

$$
M_{12}=M_{21}
\in
[-0.17344762492928894604,\,
 -0.17288215757817251839].
$$

由矩陣的平移對稱，兩個精確模態為：

$$
(1,1),\qquad(1,-1).
$$

其二次型區間分別為：

$$
Q_W(1,1)
=M_{11}+M_{12}
\in
[0.24797816833839535493,\,
 0.25145190558087834875],
$$

$$
Q_W(1,-1)
=M_{11}-M_{12}
\in
[0.59430795084585680927,\,
 0.59778168808833981318].
$$

因此：

$$
\boxed{
Q_W(v)>0
\quad
\text{對本輪固定的二維子空間內所有 }v\ne0
}
$$

這只是**有限維局部正性證書**：

$$
\boxed{
\text{有限維正性}\not\Longrightarrow RH
}
$$

它的里程碑意義是：真正的 Weil 矩陣元素已能沿著「公式—區間—證書—小驗證器」的完整流水線產生。

---

# 1. 固定顯式公式

在加法座標上，對適當測試函數 $f$，本工程固定 Weil 泛函為：

$$
\begin{aligned}
W(f)
={}&
\int_{-\infty}^{\infty}
f(x)\left(e^{x/2}+e^{-x/2}\right)\,dx
\\
&-
\sum_{n\ge1}
\frac{\Lambda(n)}{\sqrt n}
f(\log n)
-
\sum_{n\ge1}
\frac{\Lambda(n)}{\sqrt n}
f(-\log n)
\\
&-
(\log4\pi+\gamma)f(0)
\\
&-
\int_0^\infty
\frac{
e^{x/2}\bigl(f(x)+f(-x)\bigr)-2f(0)
}{e^x-e^{-x}}\,dx.
\end{aligned}
$$

這是 Bombieri／Clay 乘法座標顯式公式在加法座標中的等價版本。對實函數 $v_i,v_j$，固定：

$$
\widetilde v_j(x)=v_j(-x),
$$

$$
f_{ij}=v_i*\widetilde v_j,
$$

$$
M_{ij}=W(f_{ij}).
$$

若 RH 成立，則對角線形式可寫成零點上的平方模和，因此必為非負。故任何嚴格負方向都足以否定 RH；相反，有限個方向為正不提供 RH 證明。

---

# 2. 為什麼先選 B-spline

第一版不追求最強的搜尋能力，而追求以下工程性質：

1. 緊支撐；
2. 分段多項式；
3. 卷積可封閉計算；
4. Fourier 變換具有足夠衰減；
5. 所有積分都能化為「有理多項式乘指數」；
6. 能把積分誤差改寫成解析尾界，而不是相信積分器自報誤差。

定義中心化 cardinal cubic B-spline：

$$
\beta_3(x)
=
\frac1{3!}
\sum_{k=0}^{4}
(-1)^k{4\choose k}(x+2-k)_+^3.
$$

它滿足：

$$
\operatorname{supp}(\beta_3)=[-2,2].
$$

取：

$$
h=\frac1{20},
$$

$$
t_1=-\frac1{20},
\qquad
t_2=\frac1{20},
$$

並定義：

$$
v_i(x)
=
h^{-1/2}
\beta_3\!\left(\frac{x-t_i}{h}\right).
$$

兩個函數都支撐於：

$$
\left[-\frac3{20},\frac3{20}\right].
$$

利用 cardinal B-spline 的卷積恆等式：

$$
\beta_m*\beta_n=\beta_{m+n+1},
$$

可得：

$$
\boxed{
f_{ij}(x)
=
\beta_7\!\left(
\frac{x-(t_i-t_j)}{h}
\right)
}.
$$

所以所有矩陣元素只需處理 degree-$7$ 的分段多項式。

---

# 3. 素數項被精確排除

對角相關函數的支撐為：

$$
\operatorname{supp}(f_{11})
=
\operatorname{supp}(f_{22})
=
\left[-\frac15,\frac15\right].
$$

交叉相關函數最遠延伸至：

$$
\left|x\right|\le\frac3{10}.
$$

程式以有理 atanh 級數證明：

$$
\log2>\frac3{10}.
$$

因此對所有 $n\ge2$：

$$
|\log n|
\ge\log2
>\frac3{10},
$$

故：

$$
f_{ij}(\log n)=f_{ij}(-\log n)=0.
$$

而 $\Lambda(1)=0$，所以：

$$
\boxed{
M_{ij}^{\rm prime}=0
}
$$

是解析結論，不是「程式沒有列到任何素數」的經驗觀察。

這是一個刻意的第一階段設計：先讓完整顯式公式流水線運轉，再於下一版把支撐擴張到 $\log2$ 之外，啟動真實素數採樣。

---

# 4. 阿基米德積分的可和級數

令：

$$
F(x)=f(x)+f(-x),
\qquad
f_0=f(0).
$$

阿基米德積分為：

$$
A(f)
=
-
\int_0^\infty
\frac{e^{x/2}F(x)-2f_0}
{e^x-e^{-x}}\,dx.
$$

利用：

$$
\frac1{e^x-e^{-x}}
=
\sum_{k=0}^\infty e^{-(2k+1)x},
\qquad x>0,
$$

得到：

$$
A(f)
=
-
\sum_{k=0}^\infty
\left[
\int_0^r
F(x)e^{-(2k+1/2)x}\,dx
-
\frac{2f_0}{2k+1}
\right],
$$

其中 $r$ 是 $F$ 的正半軸支撐半徑。

單獨看兩個部分都具有 $1/k$ 主項，但括號內的差消除了該發散項，總和以 $1/k^2$ 起始。

這裡不能分別計算兩個發散級數後再相減；程式必須逐項保持括號結構。違反者標記為：

```text
INVALID_DIVERGENT_SPLIT
```

---

# 5. 六次分部積分尾界

令：

$$
a_k=2k+\frac12,
\qquad
b_k=2k+1.
$$

對：

$$
I(a)=\int_0^rF(x)e^{-ax}\,dx,
$$

由於 $F$ 為偶函數，且 B-spline 在支撐端點有足夠階數的消失，六次分部積分給出：

$$
I(a)
=
\frac{F(0)}a
+
\frac{F''(0)}{a^3}
+
\frac{F^{(4)}(0)}{a^5}
+
R_6(a),
$$

其中：

$$
|R_6(a)|
\le
\frac{\|F^{(6)}\|_\infty}{a^7}.
$$

因為：

$$
F(0)=2f_0,
$$

所以每一尾項滿足：

$$
\begin{aligned}
\left|
I(a_k)-\frac{2f_0}{b_k}
\right|
\le{}&
\frac{|F(0)|}{8k^2}
+
\frac{|F''(0)|}{8k^3}
\\
&+
\frac{|F^{(4)}(0)|}{32k^5}
+
\frac{\|F^{(6)}\|_\infty}{128k^7}.
\end{aligned}
$$

再用純有理積分比較：

$$
\sum_{k=K}^\infty\frac1{k^p}
\le
\frac1{K^p}
+
\frac1{(p-1)K^{p-1}},
$$

便得到完全有理的總尾界。

本輪取：

$$
K=200.
$$

對角元素尾界為：

$$
\boxed{
B_{\rm tail}^{(11)}
=
\frac{19463441}{13440000000}
\approx0.00144817269345
},
$$

交叉元素尾界為：

$$
\boxed{
B_{\rm tail}^{(12)}
=
\frac{7591921}{26880000000}
\approx0.000282437537202
}.
$$

這些尾界相對寬，但已足以嚴格判定本二維空間的正性。後續可增加分部積分階數或計算更多級數項縮窄。

---

# 6. 有理區間的來源

## 6.1 分段多項式積分

所有有限積分都化成：

$$
\int_l^uP(x)e^{\lambda x}\,dx,
$$

其中 $P$ 為有理係數多項式，$l,u,\lambda$ 均為有限小數有理數。

程式精確求出多項式 $R$，使：

$$
R'(x)+\lambda R(x)=P(x),
$$

因此：

$$
\int_l^uP(x)e^{\lambda x}\,dx
=
e^{\lambda u}R(u)-e^{\lambda l}R(l).
$$

只有指數函數需要超越數包絡。

## 6.2 指數函數

所有指數輸入都具有終止十進展開。程式使用 CPython `Decimal.exp()` 的「正確捨入」契約，並把結果擴張到前後相鄰的可表示 Decimal，再精確轉成有理數。

因此軟體信任基礎為：

```text
CPython 3.13.5
libmpdec 2.5.1
Decimal.exp correctly-rounded contract
```

本輪不是全形式化機器證明；它是一份：

```text
RIGOROUS_NUMERICAL_CERTIFICATE
UNDER_DOCUMENTED_SOFTWARE_CONTRACT
```

下一層可把指數函數改成完全自含的有理 Taylor 驗證器，以進一步縮小信任基礎。

## 6.3 $\pi$、$\log$ 與 Euler 常數

- $\pi$：Machin 公式與 arctan 交錯級數；
- $\log$：atanh 正項級數與解析尾界；
- $\gamma$：使用

  $$
  \frac1{2n+1}
  <H_n-\log n-\gamma
  <\frac1{2n}
  $$

  且取 $n=100$。

這些部分全部由 `Fraction` 有理運算完成。

---

# 7. 分項區間帳本

## 7.1 對角元素

$$
M_{11}=M_{22}.
$$

| 部分 | 有理區間的小數顯示 |
|---|---:|
| 指數端點積分 | $[0.10002083539509445953,\ 0.10002083539509445953]$ |
| $-(\log4\pi+\gamma)f(0)$ | $[-1.4899896018750768967,\ -1.4899776773706152611]$ |
| 阿基米德積分 | $[1.8113945597476668325,\ 1.8142909051345714744]$ |
| 素數項 | $[0,0]$ |
| **總和** | $[0.42142579326768431214,\ 0.42433406315905086714]$ |

## 7.2 交叉元素

| 部分 | 有理區間的小數顯示 |
|---|---:|
| 指數端點積分 | $[0.10014588748860156486,\ 0.10014588748860156486]$ |
| $-(\log4\pi+\gamma)f(0)$ | $[-0.074006106053397857636,\ -0.074005513776686182581]$ |
| 阿基米德積分 | $[-0.19958740636449265327,\ -0.19902253129008790067]$ |
| 素數項 | $[0,0]$ |
| **總和** | $[-0.17344762492928894604,\ -0.17288215757817251839]$ |

小數只供閱讀。證書檔保存的是完整有理分子與分母。

---

# 8. Gram 矩陣是精確有理數

由：

$$
G_{ij}
=\langle v_i,v_j\rangle_{L^2}
=f_{ij}(0),
$$

得到：

$$
G
=
\begin{pmatrix}
\frac{151}{315} & \frac1{42}\\[4pt]
\frac1{42} & \frac{151}{315}
\end{pmatrix}.
$$

其行列式：

$$
\det G
=
\frac{12997}{56700}
>0.
$$

故兩個基底線性獨立，二維子空間不是退化表示。

---

# 9. 獨立浮點交叉檢查

另一支完全不同的 `mpmath` 實作，直接對原始積分做 80 位精度計算，得到：

$$
M_{11}^{\rm float}
=
0.42311359228192251613851204858\ldots,
$$

$$
M_{12}^{\rm float}
=
-0.17344518442309131614786074708\ldots.
$$

兩者都位於有理區間內。

該浮點程式只作交叉檢查：

```text
INDEPENDENT_FLOATING_CROSSCHECK_ONLY
```

它不參與證書成立的邏輯。

---

# 10. 本輪真正關閉了什麼

本輪關閉的是：

$$
\boxed{
\text{真實 zeta Weil 元素}
\longrightarrow
\text{有理區間矩陣}
\longrightarrow
\text{exact verifier}
}
$$

在以下限定作用域中：

- 二維；
- cubic B-spline 平移基底；
- 最大相關支撐小於 $\log2$；
- 素數項因此為零；
- 阿基米德尾以六次分部積分包絡；
- 指數函數依賴 CPython Decimal 正確捨入契約。

尚未關閉的是：

1. 支撐跨過 $\log2$ 後的素數主動項；
2. 高維矩陣的區間爆炸控制；
3. 自動把浮點特徵向量有理化並稀疏化；
4. 找到任何真實負方向；
5. 將超越函數後端完全形式化。

---

# 11. GAP 狀態

| GAP | 狀態 | 說明 |
|---|---|---|
| `RH-W-05-FORMULA-LOCK` | `CLOSED` | Clay／Suzuki 顯式公式符號已對齊 |
| `RH-W-05-SPLINE-ADMISSIBILITY` | `CLOSED_FOR_W_CLASS` | 相關函數為 $C^6$ 緊支撐分段多項式，符合顯式公式需求 |
| `RH-W-05-PRIME-EMPTY` | `CLOSED` | 由支撐 $<\log2$ 精確排除素數項 |
| `RH-W-05-ARCH-SERIES` | `CLOSED_FOR_CURRENT_BASIS` | 奇異積分改寫為可和級數 |
| `RH-W-05-ARCH-TAIL` | `CLOSED_FOR_ORDER_6` | 六次分部積分＋有理 $p$-級數尾界 |
| `RH-W-05-TRANSCENDENTAL` | `CLOSED_UNDER_DECIMAL_CONTRACT` | 指數值由正確捨入 Decimal 包絡 |
| `RH-W-05-MATRIX-2D` | `CLOSED_POSITIVE` | 二維 Weil 矩陣嚴格正定 |
| `RH-W-05-PRIME-ACTIVE` | `OPEN_ENGINEERING` | 尚未計算非零 von Mangoldt 採樣 |
| `RH-W-05-HIGH-DIM` | `OPEN_ENGINEERING` | 尚未擴張至高維字典 |
| `RH-W-05-NEGATIVE-WITNESS` | `NOT_FOUND` | 沒有真實負證人 |
| `RH-W-05-FORMAL-BACKEND` | `OPEN` | 尚未以 Lean／Coq 或純有理 exp 核心取代 Decimal 信任 |

---

# 12. 下一節點

下一輪不急著增大維度，而先跨過第一個素數閾值：

$$
\boxed{
\texttt{RH-W-06-PRIME-ACTIVE-MATRIX}
}
$$

選擇相關支撐滿足：

$$
\log2<r<\log3,
$$

使顯式公式中只有：

$$
n=2
$$

的 von Mangoldt 項啟動。

這會建立第一份可逐項核對的：

$$
\text{連續阿基米德項}
+
\text{離散素數採樣項}
$$

混合矩陣證書。

這比直接把支撐拉大到包含許多素數更有工程價值，因為第一個離散跳變可以被單獨觀察、驗證並版本化。

---

# 13. 邊界聲明

本文件沒有：

- 證明 RH；
- 找到 RH 反例；
- 從二維正性推論全域正性；
- 從低支撐正性推論所有支撐正性；
- 把浮點吻合當成證書；
- 把軟體正確捨入契約宣稱為形式化證明。

本輪完成的是一個數學工程里程碑：

> **第一個真實 Weil 矩陣，已從抽象公式落成為可重播、可審計、可拒絕錯誤宣稱的有理區間物件。**

---

# 14. 主要來源

1. Enrico Bombieri, *The Riemann Hypothesis*, Clay Mathematics Institute, Section 5: explicit formula and Weil negativity criterion.
2. Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096, additive-coordinate Weil functional and localized quadratic form.
3. Python Documentation, `decimal` module: `Decimal.exp()` is correctly rounded using `ROUND_HALF_EVEN`.
