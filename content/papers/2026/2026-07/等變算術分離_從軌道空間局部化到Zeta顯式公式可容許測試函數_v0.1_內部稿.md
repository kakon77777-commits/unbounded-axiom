# 等變算術分離
## 從軌道空間局部化到 ζ 顯式公式的可容許測試函數

**英文題名：** *Equivariant Arithmetic Separation: From Orbit-Space Localization to Admissible Test Functions in the Explicit Formula for the Riemann Zeta Function*  
**作者：** Neo.K（許筌崴）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1（內部研究稿）  
**日期：** 2026-07-24  
**性質：** 黎曼猜想研究／顯式公式／Weil 型二次型／等變拓樸／測試函數／局部化  
**前置文件：**
1.《從歸心到等變拓樸：RH 合法判定研究的思考方法與方法群》  
2.《等變零點組態拓樸學：RH 軌道型分層、有效除子半環與正障礙》  
3.《層化零點障礙與局部—全域提升：從有理矩形證書到全臨界帶判定》  
**狀態：** 內部稿；不構成黎曼猜想證明

---

## 重要聲明

本文不是黎曼猜想的證明。

本文首次進入可能包含實質證明內容的接口，但只建立問題、函數類、二次型、局部化規格與條件式推導。本文沒有證明所需的局部負證人必然存在，也沒有證明顯式公式的質數側對本文全部測試函數具有足夠的無條件非負性。

本文使用 Weil 型顯式公式與正性準則作為已知背景。其重要警告是：

> 若直接證明整個 Weil 型二次型對全部合法測試函數非負，通常已經等價於或足以推出 RH。

因此，本文不能把「證明正性」當成一個顯然較弱的新中間步驟。本文真正研究的是更細的問題：

> **若偏軸零點存在，能否從其局部軌道位置出發，構造一個可進入顯式公式、能壓低該軌道貢獻、控制其他零點洩漏，並保留質數側可計算性的局部負證人？**

若此類負證人可以對任意偏軸軌道構造，而算術側又能獨立排除負值，才可能形成非循環的 RH 證明。

---

# 摘要

令
\[
F(z)=\xi\left(\frac12+z\right),
\qquad
z=\beta+i\gamma,
\]
其中 RH 等價於所有零點均滿足 \(\beta=0\)。前置研究已將偏軸零點表示為右半臨界帶中的正除子障礙，並以有理矩形繞數建立可數局部證書。

本文進一步引入顯式公式自然使用的譜坐標
\[
w=-iz=\gamma-i\beta.
\]
臨界軸 \(\beta=0\) 被映為實軸 \(w\in\mathbb R\)，而偏軸零點被映為水平帶
\[
\mathcal S_{1/2}
=
\left\{
w\in\mathbb C:
|\operatorname{Im}w|<\frac12
\right\}
\]
中的非實點。Klein 四群軌道在此坐標中成為
\[
\{w,-w,\overline w,-\overline w\}.
\]

拓樸上，任意與實軸分離的緊偏軸軌道集都可被連續函數局部化。然而 ζ 顯式公式不能使用任意二維連續函數；它只接受由一維加法或乘法測試函數經 Fourier／Mellin 轉換得到的整函數。這形成本文的核心提升缺口：
\[
\boxed{
\text{拓樸可分離}
\;\dashrightarrow\;
\text{算術可容許分離}.
}
\]

本文以卷積代數中的測試函數 \(g\) 為基本輸入，定義
\[
g^\ast(x)=\overline{g(-x)},
\qquad
f_g=g*g^\ast.
\]
若 \(G=\widehat g\)，則
\[
\widehat{f_g}(w)
=
G(w)\overline{G(\overline w)}.
\]
在實軸上，
\[
\widehat{f_g}(t)=|G(t)|^2\ge0,
\]
而在非實點上，此量不再是模平方。與共軛軌道合併後的區塊貢獻為
\[
B_w(g)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]
它可以具有負號。此差異精確描述：臨界線上的零點自然給出正平方，而偏軸軌道使 Weil 型二次型出現符號不定性。

本文定義「等變局部算術分離性」：對每個緊偏軸軌道集 \(K\)、控制視窗 \(C\) 與容許洩漏 \(\varepsilon\)，存在合法測試函數 \(g\)，使目標軌道區塊具有定量負值，而實軸、非目標零點、Gamma 項、質數項與尾部貢獻皆受到可驗證控制。這不是單純要求存在某個負二次型，而是要求證人具有：

1. 軌道對稱；
2. 空間或頻率支撐規格；
3. 目標局部化；
4. 洩漏上界；
5. 顯式公式合法性；
6. 質數側可計算性；
7. ZFC 可形式化證書。

本文證明一個條件式架構定理：若任意偏軸零點都能產生上述局部負證人，而顯式公式的算術側對同一測試函數類具有獨立的非負下界，則 RH 成立。這個定理本身是邏輯架構；真正未完成的部分是證人構造與算術下界。

本文亦提出有限視窗插值、整函數近似、Paley–Wiener 支撐代價、非目標軌道洩漏與尾部控制的分層研究計畫，並明確說明：任意二維 Urysohn 分離函數不可能直接被視為顯式公式測試函數；完全局部化與有限 Fourier 支撐之間存在不確定性代價；而任何過強的全域正性命題都可能已將 RH 偷渡進假設。

**關鍵詞：** 黎曼猜想、顯式公式、Weil 正性、等變分離、測試函數、Paley–Wiener、軌道空間、卷積平方、局部負證人、算術提升

---

# 1. 從局部零點證書到算術證人

## 1.1 前置結果

前一篇建立：

\[
\mathrm{RH}
\iff
\omega_R(F)=0
\]

對所有右半臨界帶中的正則有理矩形 \(R\) 成立。

若 RH 失敗，則存在矩形 \(R\Subset X^+\) 使：

\[
\omega_R(F)>0.
\]

這是偏軸零點存在的局部正證書。

## 1.2 新問題

繞數證書告訴我們：

\[
R\text{ 中存在偏軸零點}.
\]

但它沒有告訴我們如何從質數資料導出矛盾。

因此需要建立：

\[
\boxed{
\text{局部偏軸證書}
\longrightarrow
\text{顯式公式中的符號證人}.
}
\]

## 1.3 為何不能直接使用矩形指示函數

矩形指示函數是二維函數：

\[
\mathbf 1_R(\beta,\gamma).
\]

而 ζ 的傳統顯式公式通常使用一維測試函數 \(g(x)\)，或其 Fourier／Mellin 轉換 \(G(w)\)。

因此：

\[
\mathbf 1_R
\]

不能直接代入顯式公式。

這不是技術小問題，而是定義域不相同：

\[
C_c(X^+)
\not\subset
\mathcal H_{\mathrm{explicit}}.
\]

---

# 2. 譜坐標與等變軌道

## 2.1 坐標變換

對歸心零點：

\[
z=\beta+i\gamma,
\]

定義：

\[
w=-iz=\gamma-i\beta.
\]

反變換為：

\[
z=iw.
\]

## 2.2 臨界線

若：

\[
\beta=0,
\]

則：

\[
w=\gamma\in\mathbb R.
\]

所以 RH 等價於全部譜點 \(w_\rho\) 為實數。

## 2.3 臨界帶

因：

\[
|\beta|<\frac12,
\]

所以：

\[
|\operatorname{Im}w|<\frac12.
\]

定義譜帶：

\[
\mathcal S
=
\left\{
w\in\mathbb C:
|\operatorname{Im}w|<\frac12
\right\}.
\]

## 2.4 群作用的轉換

在 \(z\)-坐標中：

\[
a(z)=-z,
\qquad
b(z)=\overline z,
\qquad
j(z)=-\overline z.
\]

在 \(w=-iz\) 坐標中：

\[
a_w(w)=-w,
\]

\[
b_w(w)=-\overline w,
\]

\[
j_w(w)=\overline w.
\]

因此臨界反射變成普通複共軛，其固定集為：

\[
\operatorname{Fix}(j_w)=\mathbb R.
\]

一般偏軸軌道為：

\[
\mathcal O(w)
=
\{w,-w,\overline w,-\overline w\}.
\]

## 2.5 軌道空間

令：

\[
Y=\mathcal S/G.
\]

實軸軌道形成：

\[
Y_{\mathrm{axis}},
\]

非實軌道形成：

\[
Y_{\mathrm{off}}.
\]

RH 等價於譜除子的下降測度完全支撐於 \(Y_{\mathrm{axis}}\)。

---

# 3. 拓樸分離

## 3.1 緊偏軸軌道集

令：

\[
K\subset Y_{\mathrm{off}}
\]

為緊集。

其逆像：

\[
\widetilde K\subset\mathcal S
\]

是 \(G\)-不變、與實軸分離的緊集。

因此存在：

\[
d(K,\mathbb R)>0.
\]

## 3.2 連續分離

在正常拓樸空間中，可找到連續 \(G\)-不變函數：

\[
u_K:\mathcal S\to[0,1]
\]

使：

\[
u_K|_{\widetilde K}=1,
\]

並在實軸某鄰域中：

\[
u_K=0.
\]

## 3.3 拓樸分離的意義

若偏軸零點測度 \(\nu_F\) 在 \(K\) 上有正質量，則：

\[
\int u_K\,d\nu_F>0.
\]

所以拓樸上可以定位偏軸質量。

## 3.4 拓樸分離的不足

\(u_K\) 通常：

- 不是全純函數；
- 不是一維 Fourier 轉換；
- 不具所需衰減；
- 不具有顯式公式允許的解析延拓；
- 不能自然轉換成質數和。

因此拓樸分離只建立目標規格，不建立算術證人。

---

# 4. 可容許測試函數類

## 4.1 基本測試代數

令：

\[
\mathcal G
\]

為一個待精確選定的複值測試函數代數，例如：

- \(C_c^\infty(\mathbb R)\)；
- 某個 Schwartz 子空間；
- 具有指定指數權重的平滑緊支撐函數；
- 顯式公式定理所允許的其他核空間。

不同正規化會改變細節，但本文要求 \(\mathcal G\) 至少滿足：

1. 對卷積封閉；
2. 對 involution 封閉；
3. Fourier 或 Mellin 轉換可延拓至包含 \(\mathcal S\) 的區域；
4. 零點和、質數和與 Gamma 項均良定義；
5. 可使用顯式公式；
6. 可進行有限線性組合與近似。

## 4.2 involution

定義：

\[
g^\ast(x)
=
\overline{g(-x)}.
\]

卷積平方：

\[
f_g
=
g*g^\ast.
\]

## 4.3 Fourier 轉換

採用某一固定慣例：

\[
G(w)
=
\widehat g(w)
=
\int_{\mathbb R}
g(x)e^{iwx}\,dx.
\]

則：

\[
\widehat{g^\ast}(w)
=
\overline{G(\overline w)}.
\]

故：

\[
\widehat{f_g}(w)
=
G(w)\overline{G(\overline w)}.
\]

## 4.4 臨界線上的正性

若：

\[
w=t\in\mathbb R,
\]

則：

\[
\widehat{f_g}(t)
=
|G(t)|^2
\ge0.
\]

這是 Weil 型二次型在 RH 下出現正性的基本代數原因。

## 4.5 偏軸的符號不定性

若：

\[
w\notin\mathbb R,
\]

則：

\[
G(w)\overline{G(\overline w)}
\]

不必為實數，也不必非負。

將共軛軌道配對後得到實區塊：

\[
B_w(g)
=
G(w)\overline{G(\overline w)}
+
G(\overline w)\overline{G(w)}
\]

\[
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right).
\]

此量可能為正、零或負。

---

# 5. 等變對稱化

## 5.1 為何需要對稱

零點以：

\[
\{w,-w,\overline w,-\overline w\}
\]

成軌道出現。

測試函數若不尊重此對稱，可能：

- 產生不必要複數值；
- 重複計算同一軌道；
- 將符號問題與座標選擇混合。

## 5.2 偶化

對 \(g\in\mathcal G\)，定義：

\[
g_{\mathrm{ev}}(x)
=
\frac12(g(x)+g(-x)).
\]

若 \(\mathcal G\) 封閉，則：

\[
g_{\mathrm{ev}}\in\mathcal G.
\]

其 Fourier 轉換滿足：

\[
G_{\mathrm{ev}}(-w)=G_{\mathrm{ev}}(w).
\]

## 5.3 實結構

可再取：

\[
g_{\mathbb R}(x)
=
\frac12
\left(
g_{\mathrm{ev}}(x)
+
\overline{g_{\mathrm{ev}}(x)}
\right).
\]

使 \(g_{\mathbb R}\) 為實偶函數，並有：

\[
G(-w)=G(w),
\]

\[
G(\overline w)=\overline{G(w)}.
\]

## 5.4 注意

若 \(G(\overline w)=\overline{G(w)}\)，則：

\[
G(w)\overline{G(\overline w)}
=
G(w)^2.
\]

共軛區塊成為：

\[
B_w(g)=2\operatorname{Re}(G(w)^2).
\]

這仍可能為負。

例如若：

\[
G(w)\approx i\alpha,
\]

則：

\[
\operatorname{Re}(G(w)^2)\approx-\alpha^2.
\]

因此局部負證人的目標可被理解為：

> 在目標偏軸點上，使 \(G(w)\) 的相位接近純虛數，同時控制其他譜點與算術側代價。

---

# 6. Weil 型二次型

## 6.1 抽象顯式公式

對適當測試函數 \(f\)，ζ 顯式公式可抽象寫成：

\[
\mathcal Z_\zeta(f)
=
\mathcal A_\infty(f)
+
\mathcal P_\zeta(f)
+
\mathcal N(f),
\]

其中：

- \(\mathcal Z_\zeta\)：非平凡零點側；
- \(\mathcal A_\infty\)：Gamma 因子與無窮遠位置；
- \(\mathcal P_\zeta\)：質數與質數冪側；
- \(\mathcal N\)：正規化、極點或端點項。

確切常數、符號與 Fourier 慣例需在形式化版本中固定。

## 6.2 二次型

對：

\[
f_g=g*g^\ast,
\]

定義 Weil 型二次型：

\[
Q_\zeta(g)
=
\mathcal W_\zeta(f_g),
\]

其中 \(\mathcal W_\zeta\) 是採用固定正規化後的顯式公式泛函。

零點側具有形式：

\[
Q_\zeta^{\mathrm{zero}}(g)
=
\sum_{\rho}
G(w_\rho)
\overline{G(\overline{w_\rho})},
\]

以對稱或正則化方式求和。

## 6.3 RH 下的零點側

若 RH 成立，所有：

\[
w_\rho\in\mathbb R.
\]

因此：

\[
Q_\zeta^{\mathrm{zero}}(g)
=
\sum_\rho
|G(w_\rho)|^2
\ge0.
\]

## 6.4 偏軸區塊

若存在非實軌道 \(\mathcal O(w)\)，其合併貢獻具有形式：

\[
m_w B_w(g),
\]

其中：

\[
B_w(g)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]

並再依 \(\pm w\) 對稱與正規化加入相應倍數。

此區塊可能為負。

## 6.5 已知正性準則的地位

在適當測試函數空間與正規化下，Weil 型二次型對所有測試函數非負，是 RH 的已知等價或充分必要形式之一。

因此本文不把：

\[
Q_\zeta(g)\ge0
\qquad
\forall g
\]

當作已被降低難度的新目標。

本文改研究：

\[
\text{偏軸局部資料}
\Longrightarrow
\text{可定位的 }g\text{ 與負區塊}.
\]

---

# 7. 局部軌道負證人

## 7.1 目標軌道

令：

\[
w_0=\gamma_0-i\beta_0,
\qquad
\beta_0\ne0.
\]

其軌道：

\[
\mathcal O_0
=
\{w_0,-w_0,\overline{w_0},-\overline{w_0}\}.
\]

## 7.2 理想局部條件

希望構造 \(g\in\mathcal G\)，使：

\[
B_{w_0}(g)\le-c
\]

對某個 \(c>0\)。

同時對控制區內其他零點軌道 \(w\)：

\[
|B_w(g)|\le\varepsilon.
\]

並控制：

\[
|\mathcal A_\infty(f_g)|,
\qquad
|\mathcal P_\zeta(f_g)|,
\qquad
|\mathcal N(f_g)|.
\]

## 7.3 不能要求完全零洩漏

若 \(G\) 為整函數，要求它在具有聚點的非目標集合上完全為零，通常會迫使：

\[
G\equiv0.
\]

因此合法目標不是：

\[
G=0
\quad
\text{於所有非目標位置},
\]

而是定量近似：

\[
\sum_{\text{非目標}}
|B_w(g)|
\le
\varepsilon.
\]

## 7.4 證人定義

稱 \(g\) 為目標軌道 \(\mathcal O_0\) 的

\[
(c,\varepsilon,C)
\text{-局部負證人},
\]

若：

1. \(g\in\mathcal G\)；
2. \(g\) 滿足指定對稱；
3. 目標區塊
   \[
   B_{w_0}(g)\le-c;
   \]
4. 控制視窗 \(C\) 中非目標零點的總洩漏至多 \(\varepsilon\)；
5. 視窗外尾部有明確上界；
6. 顯式公式各項絕對或對稱收斂；
7. 質數側可由有限資料加尾界計算；
8. 全部誤差小於 \(c\) 的指定比例。

## 7.5 證書形式

\[
\mathsf{Witness}
=
\left(
g,
G,
\mathcal O_0,
c,
\varepsilon,
C,
E_{\mathrm{tail}},
E_{\mathrm{prime}},
E_{\infty}
\right).
\]

若能驗證：

\[
c
>
\varepsilon
+
E_{\mathrm{tail}}
+
E_{\mathrm{prime}}
+
E_{\infty},
\]

則總二次型符號由目標負區塊支配。

---

# 8. 有限視窗插值

## 8.1 有限譜集合

令：

\[
\Sigma
=
\{w_1,\ldots,w_N\}
\subset\mathcal S
\]

為有限且在 \(\pm\) 與共軛下封閉的集合。

## 8.2 純整函數插值

對符合對稱的有限目標值：

\[
v_k,
\]

可使用多項式或整函數插值，構造 \(G\) 使：

\[
G(w_k)=v_k.
\]

再以平均方式保證：

\[
G(-w)=G(w),
\]

\[
G(\overline w)=\overline{G(w)}.
\]

## 8.3 局部相位配置

可為目標偏軸點指定：

\[
G(w_0)=i,
\]

\[
G(\overline{w_0})=-i,
\]

使：

\[
B_{w_0}(g)
=
2\operatorname{Re}(i^2)
=
-2.
\]

並對有限非目標集合指定小值。

## 8.4 此結果仍不足

任意插值整函數未必是某個：

\[
g\in\mathcal G
\]

的 Fourier 轉換。

它可能：

- 增長過快；
- 在實軸不衰減；
- 使質數和發散；
- 不具有限指數型；
- 不符合顯式公式假設。

因此：

\[
\text{有限整函數插值}
\not\Rightarrow
\text{算術可容許證人}.
\]

---

# 9. Paley–Wiener 提升問題

## 9.1 有限支撐與指數型

若：

\[
g\in C_c^\infty([-L,L]),
\]

則其 Fourier 轉換 \(G\) 為整函數，具有受 \(L\) 控制的指數型。

反之，適當的指數型與實軸衰減條件可對應緊支撐測試函數。

## 9.2 局部化代價

要使 \(G\) 在譜空間中高度局部化，通常需要讓 \(g\) 的支撐擴大。

這是 Fourier 不確定性的表現：

\[
\text{譜局部化提高}
\Longrightarrow
\text{算術變數支撐擴大}.
\]

在顯式公式中，這意味需要更多質數與質數冪資料。

## 9.3 算術成本

若 \(g\) 的支撐受限於：

\[
[-L,L],
\]

質數側通常只涉及：

\[
\log n\le L
\]

或與此相應的有限範圍。

因此 \(L\) 同時控制：

- 譜分辨率；
- 所需質數範圍；
- 計算證書大小；
- 尾部誤差。

## 9.4 核心優化問題

給定：

\[
w_0,\quad c,\quad\varepsilon,
\]

尋找最小支撐半徑：

\[
L_{\min}(w_0;c,\varepsilon)
\]

使存在：

\[
g\in C_c^\infty([-L,L])
\]

滿足局部負證人條件。

這是本文提出的定量「算術分離成本」。

---

# 10. 等變局部算術分離性

## 10.1 定義

稱 ζ 的顯式公式測試系統具有**等變局部算術分離性**，若對每個：

- 緊偏軸軌道集 \(K\subset Y_{\mathrm{off}}\)；
- 緊控制視窗 \(C\supset K\)；
- 容許誤差 \(\varepsilon>0\)；

只要零點除子在 \(K\) 上有正質量，就存在：

\[
g\in\mathcal G
\]

使：

1. 目標軌道總貢獻至多 \(-c_K<0\)；
2. \(C\setminus K\) 中零點總洩漏小於 \(\varepsilon\)；
3. \(C\) 外零點尾部小於 \(\varepsilon\)；
4. archimedean 與正規化誤差可顯式計算；
5. 質數側只依賴有限範圍資料與可證尾界；
6. 總誤差小於 \(c_K\)。

## 10.2 強版本

強版本要求：

\[
c_K
\]

可由：

- \(K\) 到實軸距離；
- \(K\) 中最小重數；
- 控制視窗大小；
- 測試函數支撐；

給出明確下界。

## 10.3 弱版本

弱版本只要求存在某個負證人，不要求有效估計。

弱版本接近已知全域正性準則的反否命題；強版本則要求可定位、可構造、可計算的證書。

## 10.4 本文主張

本文不宣稱已證明強版本或弱版本。

本文主張它們是拓樸框架與顯式公式之間最精確的提升問題之一。

---

# 11. 算術非負性接口

## 11.1 算術側泛函

顯式公式將二次型寫為：

\[
Q_\zeta(g)
=
Q_{\mathrm{prime}}(g)
+
Q_{\infty}(g)
+
Q_{\mathrm{norm}}(g).
\]

具體符號依正規化而異。

## 11.2 所需命題

要從局部負證人推出矛盾，需要獨立證明：

\[
Q_\zeta(g)\ge0
\]

至少對所有由分離構造產生的 \(g\) 成立。

## 11.3 為何不能直接假設全類非負

若假設：

\[
Q_\zeta(g)\ge0
\qquad
\forall g\in\mathcal G,
\]

在標準 Weil 型設定中，這可能已等價於 RH。

因此合法研究應尋找：

- 一個由算術結構自然生成的較小子類；
- 一個可直接證明非負的結構性錐；
- 或一個不同於完整 Weil 正性的局部估計。

## 11.4 分離類與正性類的交集

令：

\[
\mathcal G_{\mathrm{sep}}
\]

為可產生局部負證人的測試函數類。

令：

\[
\mathcal G_{\mathrm{arith}+}
\]

為可由質數側獨立證明：

\[
Q_\zeta(g)\ge0
\]

的測試函數類。

真正需要的是：

\[
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\ne\varnothing
\]

對每個假設偏軸軌道成立。

這個交集問題比籠統地「證明 Weil 正性」更精確。

---

# 12. 條件式排除定理

## 12.1 定理架構

### 定理 12.1（條件式）

假設：

1. \(F\) 的零點除子具有已知 \(G\)-對稱；
2. 任意偏軸緊軌道集都滿足強等變局部算術分離性；
3. 每個由該分離程序產生的測試函數 \(g\) 都滿足無條件算術下界：
   \[
   Q_\zeta(g)\ge0;
   \]
4. 顯式公式、所有求和、極限與誤差界均合法。

則 RH 成立。

## 12.2 證明

反設 RH 不成立。

則存在偏軸零點軌道。取只包含有限個偏軸軌道、且與實軸分離的緊集 \(K\)。

由條件 2，存在局部負證人 \(g\)，其目標負貢獻嚴格超過所有非目標與誤差貢獻，因此：

\[
Q_\zeta(g)<0.
\]

但由條件 3：

\[
Q_\zeta(g)\ge0.
\]

矛盾。

故不存在偏軸零點，RH 成立。證畢。

## 12.3 定理的地位

此定理只是邏輯分解。

條件 2 與條件 3 都是重大未解內容。

不能將條件式定理本身宣稱為 RH 進展，除非其中至少一個非平凡條件被獨立證明。

---

# 13. 局部證書到負證人的分層流程

## 13.1 第一步：矩形證書

找到：

\[
R\Subset X^+
\]

使：

\[
\omega_R(F)>0.
\]

在反證法中，這由假設偏軸零點存在而得到。

## 13.2 第二步：軌道飽和

將 \(R\) 在 \(G\) 下飽和，得到譜坐標中的目標緊集：

\[
K_R
=
G\cdot(-iR).
\]

## 13.3 第三步：拓樸分離

構造：

\[
u_R
\]

在 \(K_R\) 上大、在實軸鄰域為零。

## 13.4 第四步：解析近似

尋找整函數或 Paley–Wiener 函數 \(G_R\)，使其產生的軌道區塊近似所需符號形狀。

注意不是近似 \(u_R\) 本身，而是近似一個可由：

\[
2\operatorname{Re}
\left(
G_R(w)\overline{G_R(\overline w)}
\right)
\]

表達的符號核。

## 13.5 第五步：反 Fourier 提升

證明：

\[
G_R=\widehat{g_R}
\]

對某個：

\[
g_R\in\mathcal G.
\]

## 13.6 第六步：誤差分解

將總二次型分成：

\[
Q_\zeta(g_R)
=
Q_K
+
Q_{C\setminus K}
+
Q_{\mathrm{tail}}
+
Q_{\mathrm{prime}}
+
Q_\infty
+
Q_{\mathrm{norm}}.
\]

## 13.7 第七步：符號支配

證明：

\[
Q_K
<
-
\left(
|Q_{C\setminus K}|
+
|Q_{\mathrm{tail}}|
+
|Q_{\mathrm{prime}}|
+
|Q_\infty|
+
|Q_{\mathrm{norm}}|
\right).
\]

則：

\[
Q_\zeta(g_R)<0.
\]

---

# 14. 主要分析障礙

## 14.1 全純剛性

任意連續二維分離函數不能被全純函數任意精確且全域地複製。

## 14.2 最大值與唯一延拓

若要求整函數在過大的集合上完全消失，可能迫使其恆為零。

## 14.3 不確定性原理

譜空間的高解析度需要算術變數中的大支撐。

## 14.4 零點未知性

非目標零點的位置未知，不能在構造證人時假設已掌握全部零點。

## 14.5 軸上零點洩漏

軸上零點數量無限。即使每個單點貢獻很小，總和仍可能不可忽略。

## 14.6 Gamma 項

archimedean 項可能具有與目標負值同階的貢獻。

## 14.7 質數側符號

質數和通常不是逐項自動非負，必須依測試函數結構重新分析。

## 14.8 尾部正則化

零點側往往需要對稱求和或正則化，局部分解必須與求和順序相容。

---

# 15. 圓錐而非線性空間

## 15.1 為何使用正錐

要證明非負性，測試函數不應只被視為線性空間，而應考慮卷積平方錐：

\[
\mathcal C
=
\left\{
g*g^\ast:
g\in\mathcal G
\right\}.
\]

## 15.2 臨界線正錐

在 RH 下，零點側對此錐為：

\[
\sum_\rho|G(w_\rho)|^2.
\]

## 15.3 偏軸破壞

偏軸軌道使相同錐上的零點側變為不定二次型。

因此 RH 可以理解為：

> ζ 的零點評價泛函在卷積平方錐上保持正性。

這是已知 Weil 型觀點的等變組態詮釋。

## 15.4 本文的新分解

本文將全域正錐問題拆成：

\[
\text{局部負方向的構造}
+
\text{算術正錐的獨立辨認}.
\]

---

# 16. 有限維矩陣原型

## 16.1 基底測試函數

選取：

\[
g_1,\ldots,g_N\in\mathcal G.
\]

令：

\[
g=\sum_{k=1}^Nc_kg_k.
\]

則：

\[
Q_\zeta(g)
=
c^\ast M c
\]

對某個 Hermitian 矩陣 \(M\)。

## 16.2 零點軌道矩陣

目標偏軸軌道給出矩陣：

\[
M_K.
\]

其他貢獻給出：

\[
M_{\mathrm{rest}},
\quad
M_{\mathrm{prime}},
\quad
M_\infty.
\]

總矩陣：

\[
M
=
M_K
+
M_{\mathrm{rest}}
+
M_{\mathrm{prime}}
+
M_\infty.
\]

## 16.3 有限維負證人

若存在向量 \(c\) 使：

\[
c^\ast M_Kc<0
\]

且負值超過其他矩陣的算子範數上界，則得到有限維負證書。

## 16.4 價值

此原型可以：

- 數值搜尋測試函數；
- 估計所需支撐；
- 發現無法控制的洩漏；
- 產生形式化候選證書；
- 不直接宣稱證明 RH。

## 16.5 風險

有限維空間中沒有找到負方向，不代表無限維中不存在。

找到數值負方向也必須完成精確誤差證明。

---

# 17. 形式化的分離成本

## 17.1 成本向量

定義證人成本：

\[
\mathfrak C(g)
=
\left(
L,
N_p,
P,
E_{\mathrm{tail}},
E_{\mathrm{axis}},
E_\infty,
E_{\mathrm{arith}}
\right),
\]

其中：

- \(L\)：實變數支撐半徑；
- \(N_p\)：所需質數資料上限；
- \(P\)：數值精度；
- \(E_{\mathrm{tail}}\)：零點尾部誤差；
- \(E_{\mathrm{axis}}\)：軸上洩漏；
- \(E_\infty\)：Gamma 項誤差；
- \(E_{\mathrm{arith}}\)：質數側尾界。

## 17.2 距軸距離

預期：

\[
|\beta_0|\downarrow0
\]

時，區分偏軸點與實軸所需成本上升。

即：

\[
L_{\min}
\to\infty
\]

或誤差控制惡化。

## 17.3 高度成本

當：

\[
|\gamma_0|\to\infty,
\]

需要處理更多鄰近零點與更大的算術資料範圍。

## 17.4 分離複雜度

定義概念性複雜度：

\[
\operatorname{SepCost}(w_0;c,\varepsilon)
=
\inf_g
\mathfrak C(g),
\]

其中 infimum 依某個偏序或加權成本函數解釋。

此量可成為後續計算實驗的主要觀測值。

---

# 18. 循環性審計

## 18.1 禁止使用的假設

構造 \(g\) 時不能假設：

- 全部其他零點在臨界線；
- 目標軌道是唯一偏軸軌道；
- 未知零點尾部具有 RH 下的界；
- Weil 二次型已對全部測試函數非負；
- 某個與 RH 等價的正性條件已成立。

## 18.2 可使用的資料

可使用：

- 功能方程；
- 零點對稱；
- 已知零點計數漸近；
- 無條件零點自由區；
- 已證顯式公式；
- 已驗證有限高度資料；
- 無條件 Gamma 與質數和估計；
- 測試函數自身的解析界。

## 18.3 依賴標記

每個局部負證人必須標記：

\[
\mathsf{Deps}(g)
=
\left(
\mathsf{Analytic},
\mathsf{Arithmetic},
\mathsf{Numerical},
\mathsf{Axiomatic}
\right).
\]

若任何估計使用 RH 或等價命題，該證人只能作條件性實驗。

---

# 19. 與已知正性準則的關係

## 19.1 非新等價式聲明

本文承認：

- Weil 型正性；
- Li 型係數非負；
- 某些 Hilbert 空間或跡公式表述；

已提供 RH 的等價或密切相關判準。

本文不把它們重新命名為新證明。

## 19.2 本文的差異

本文關心的是：

\[
\text{全域正性失敗}
\]

是否可以被分解為：

\[
\text{某個局部偏軸軌道}
\longrightarrow
\text{一個局部化負方向}.
\]

## 19.3 新研究目標

已知等價準則通常說：

\[
\mathrm{RH\ false}
\Longrightarrow
\exists g,\ Q_\zeta(g)<0.
\]

本文追問更強的構造問題：

\[
\mathrm{RH\ false}
+
\text{指定偏軸軌道 }K
\Longrightarrow
\exists g_K
\]

並且 \(g_K\) 的：

- 支撐；
- 相位；
- 誤差；
- 算術成本；
- 目標軌道歸屬；

全部可控制。

這是「存在負方向」到「定位負證書」的提升。

---

# 20. 計算實驗規格

## 20.1 目的

計算實驗不試圖證明 RH，而用於判斷局部算術分離是否實際可行。

## 20.2 人工偏軸組態

先建立具有：

- 已知軸上譜點；
- 一個人工偏軸四元軌道；
- 可控重數；

的有限模型。

## 20.3 測試基底

可使用：

- 緊支撐 B-spline；
- 平滑 bump 函數；
- Hermite／Gaussian 原型；
- prolate spheroidal 型基底；
- 有限 Fourier 組合。

若某基底不屬於最終顯式公式類，只能作探索。

## 20.4 優化目標

最小化：

\[
B_{w_0}(g)
+
\lambda_1 E_{\mathrm{axis}}
+
\lambda_2 E_{\mathrm{rest}}
+
\lambda_3 E_{\mathrm{support}}.
\]

## 20.5 輸出

每次實驗輸出：

- 目標負區塊；
- 軸上洩漏；
- 其他偏軸洩漏；
- 支撐成本；
- 數值條件數；
- 誤差敏感度；
- 是否可轉為精確證書。

---

# 21. 形式化計畫

## 21.1 譜坐標模組

```text
CenteredZero
SpectralCoordinate
SpectralStrip
SpectralKleinAction
AxisOrbit
OffAxisOrbit
```

## 21.2 測試函數代數

```text
AdmissibleTestFunction
Convolution
StarInvolution
ConvolutionSquare
FourierTransformInStrip
```

核心定理：

\[
\widehat{g*g^\ast}(w)
=
G(w)\overline{G(\overline w)}.
\]

## 21.3 軌道區塊

```text
OrbitBlock
AxisBlockNonnegative
OffAxisBlockReal
OffAxisBlockSignIndefinite
```

## 21.4 顯式公式接口

不應立即完整重建全部 ζ 顯式公式，可先定義抽象接口：

```text
ExplicitFormulaFunctional
ZeroSide
PrimeSide
ArchimedeanSide
NormalizationSide
ExplicitFormulaIdentity
```

## 21.5 證人模組

```text
LocalizedNegativeWitness
TargetOrbitContribution
LeakageBound
TailBound
PrimeComputability
WitnessDominatesErrors
```

## 21.6 條件式定理

```text
localized_separation_and_arithmetic_nonnegativity_implies_RH
```

該定理必須清楚保留所有未證假設，不得以公理形式隱藏。

---

# 22. 失敗條件

本研究路線若出現下列情況，必須降級或改線：

1. 可容許測試函數無法局部化單一偏軸軌道；
2. 任意局部化都造成無法控制的軸上總洩漏；
3. Paley–Wiener 支撐成本無限大；
4. 質數側對分離函數沒有可用符號或界；
5. Gamma 項必然抵消目標負值；
6. 目標軌道與其他未知偏軸軌道無法分離；
7. 所需算術非負性本身與完整 RH 等價；
8. 有限維負方向不能提升至合法無限維函數；
9. 尾部估計不可無條件完成；
10. 形式化顯示某個核心映射型別不合法。

即使此路線失敗，前兩篇建立的組態、正障礙、層與證書框架仍然有效。

---

# 23. 本文完成的內容

本文完成：

1. 將歸心零點轉換到顯式公式譜坐標；
2. 將偏軸四元軌道表示為非實譜軌道；
3. 分離任意拓樸測試函數與算術可容許測試函數；
4. 建立卷積平方在實軸與非實點上的符號差異；
5. 定義偏軸軌道區塊；
6. 定義局部負證人；
7. 定義等變局部算術分離性；
8. 建立條件式 RH 排除定理；
9. 提出 Paley–Wiener 分離成本；
10. 建立有限維矩陣原型；
11. 建立循環性與形式化審計規格。

---

# 24. 本文未完成的內容

本文沒有證明：

\[
\forall K\subset Y_{\mathrm{off}},
\quad
\exists g_K\in\mathcal G
\]

滿足局部負證人條件。

本文也沒有證明：

\[
Q_\zeta(g)\ge0
\]

對分離程序產生的全部 \(g\) 無條件成立。

因此本文尚未排除任何實際偏軸零點，也沒有證明 RH。

---

# 25. 下一階段

下一篇預定為：

# 《顯式公式中的偏軸正障礙》
## 零點側局部負方向、質數側可計算錐與 ZFC 可審計矛盾架構

其任務包括：

1. 固定一個精確的 Guinand–Weil 型顯式公式正規化；
2. 固定測試函數空間；
3. 展開零點軌道區塊；
4. 展開 Gamma 項；
5. 展開質數與質數冪項；
6. 定義可由質數側證明非負的測試函數錐；
7. 研究該錐與局部分離類的交集；
8. 建立有限維與函數空間原型；
9. 判斷此交集問題是否只是 RH 的再次等價化。

---

# 26. 結論

前兩篇完成了：

\[
\text{偏軸零點}
\longrightarrow
\text{正除子障礙}
\longrightarrow
\text{局部繞數證書}.
\]

本文建立下一條待跨越的箭頭：

\[
\boxed{
\text{局部偏軸證書}
\;\dashrightarrow\;
\text{顯式公式中的局部負證人}.
}
\]

譜坐標：

\[
w=-iz
\]

將臨界線化為實軸。卷積平方測試函數滿足：

\[
\widehat{g*g^\ast}(t)
=
|G(t)|^2
\ge0
\qquad
(t\in\mathbb R),
\]

而偏軸軌道產生：

\[
B_w(g)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]

其符號不定。

這揭示了 Weil 型正性的局部等變來源：

> **軸上零點形成模平方；偏軸零點破壞模平方結構。**

但知道符號可以變負，並不等於能構造一個合法、局部、可計算且足以壓過所有其他項的負證人。

因此，本篇的核心研究命題是：

\[
\boxed{
\begin{aligned}
&\text{給定任意偏軸零點軌道，}\\
&\text{是否存在一個顯式公式可容許的卷積平方測試函數，}\\
&\text{使該軌道產生定量負值，}\\
&\text{並使軸上零點、其他軌道、Gamma 項、質數項與尾部誤差皆可控制？}
\end{aligned}
}
\]

若答案為否，拓樸局部化不能提升為算術分離，此路線止於判定框架。

若答案為是，仍需第二個獨立結果：

\[
\boxed{
\text{同一測試函數類的算術側不能產生負值。}
}
\]

只有兩者同時完成，才會得到真正的矛盾：

\[
Q_\zeta(g)<0
\quad\text{且}\quad
Q_\zeta(g)\ge0.
\]

因此，本輪沒有證明 RH，但已將「拓樸如何真正參與 RH 證明」壓縮為一個具體、可失敗、可計算、可形式化的交集問題：

\[
\boxed{
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\stackrel{?}{\ne}
\varnothing
}
\]

對每一個假設偏軸軌道是否成立。

這是本系列第一次從等價重述正式進入可能產生實質證明內容的技術缺口。

---

# 附錄 A：主要符號

| 符號 | 意義 |
|---|---|
| \(z=\beta+i\gamma\) | 歸心零點坐標 |
| \(w=-iz\) | 顯式公式譜坐標 |
| \(\mathcal S\) | 水平譜帶 |
| \(Y=\mathcal S/G\) | 軌道空間 |
| \(K\) | 緊偏軸軌道集 |
| \(\mathcal G\) | 可容許測試函數代數 |
| \(g^\ast\) | involution \(\overline{g(-x)}\) |
| \(f_g\) | 卷積平方 \(g*g^\ast\) |
| \(G\) | \(\widehat g\) |
| \(B_w(g)\) | 偏軸軌道區塊 |
| \(Q_\zeta(g)\) | Weil 型二次型 |
| \(\mathcal G_{\mathrm{sep}}\) | 可局部分離的測試函數類 |
| \(\mathcal G_{\mathrm{arith}+}\) | 算術側可證非負的函數類 |
| \(\operatorname{SepCost}\) | 局部算術分離成本 |

---

# 附錄 B：邏輯地位表

| 命題 | 地位 |
|---|---|
| 臨界線在 \(w\)-坐標中為實軸 | 直接變換 |
| 卷積平方在實軸為模平方 | Fourier 代數恆等式 |
| 偏軸區塊可符號不定 | 代數事實 |
| 拓樸上可分離偏軸緊集與實軸 | 一般拓樸事實 |
| 任意拓樸分離可提升為可容許測試函數 | 未證 |
| 任意偏軸軌道存在局部負證人 | 未證 |
| 算術側對分離類非負 | 未證 |
| 完整 Weil 型正性與 RH 的關係 | 已知背景；不可偷渡 |
| 條件 2＋條件 3推出 RH | 條件式邏輯定理 |

---

# 附錄 C：參考背景

1. A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, 1998/1999.  
2. A. Connes and C. Consani, *Weil positivity and Trace formula, the archimedean place*, 2020.  
3. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, 2004.  
4. M. Suzuki, *Li coefficients as norms of functions in a model space*, 2023.  
5. 經典 Guinand–Weil 顯式公式、Weil 正性準則與 Paley–Wiener 理論之相關文獻，待正式公開版統一補齊版本、頁碼與正規化。

---

# 附錄 D：版本邊界

v0.1 已完成：

- 譜坐標與等變軌道；
- 拓樸分離／算術分離區分；
- 可容許測試函數抽象規格；
- 卷積平方軌道區塊；
- 局部負證人定義；
- 等變局部算術分離性；
- 條件式排除定理；
- Paley–Wiener 分離成本；
- 有限維矩陣原型；
- 循環性審計；
- 形式化計畫。

v0.1 尚未完成：

- 固定唯一顯式公式正規化；
- 強局部分離定理；
- 無條件質數側非負錐；
- 軸上與尾部洩漏的統一界；
- Lean 4 實作；
- 數值原型；
- 任何 RH 證明。
