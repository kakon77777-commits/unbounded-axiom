# 顯式公式中的偏軸正障礙
## 零點側區域負方向、質數側可計算錐與 ZFC 可審計矛盾架構

**英文題名：** *Positive Off-Axis Obstructions in the Explicit Formula: Regional Negative Directions on the Zero Side, Computable Prime-Side Cones, and a ZFC-Auditable Contradiction Architecture*  
**作者：** Neo.K（許筌崴）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1（內部研究稿）  
**日期：** 2026-07-24  
**性質：** 黎曼猜想研究／Riemann–Weil 顯式公式／Paley–Wiener 局部化／算術正性錐／形式化審計  
**前置文件：**
1.《從歸心到等變拓樸：RH 合法判定研究的思考方法與方法群》  
2.《等變零點組態拓樸學：RH 軌道型分層、有效除子半環與正障礙》  
3.《層化零點障礙與局部—全域提升：從有理矩形證書到全臨界帶判定》  
4.《等變算術分離：從軌道空間局部化到 ζ 顯式公式的可容許測試函數》  
**狀態：** 內部稿；不構成黎曼猜想證明

---

## 重要聲明

本文不是黎曼猜想的證明。

本文固定一個乘法群版本的 Riemann–Weil 顯式公式正規化，並把前一篇的抽象「局部負證人」拆成三個可分別驗證的子問題：

1. **區域相位塑形：**  
   給定一個與臨界線分離的偏軸矩形，是否能構造合法測試函數，使矩形中每一個可能零點都產生一致負的軌道區塊？

2. **全域洩漏控制：**  
   該測試函數對臨界線零點、其他偏軸零點與無窮遠零點的總貢獻是否可以無條件控制？

3. **算術側非負性：**  
   同一測試函數是否落入一個可由有限質數資料、archimedean 項與嚴格尾界證明非負的錐？

本文對第一項提出一個具體的 Paley–Wiener 區域相位塑形引理及其證明架構。此引理只解決目標區域內的符號，不解決區域外零點總和，也不證明算術側非負。

本文同時建立「支撐—質數啟動過濾」：緊支撐測試函數的卷積平方只啟動有限多個質數與質數冪。這使每個固定支撐尺度的算術側可被表示為有限局部矩陣加一個 archimedean 矩陣，但其符號仍不是自動非負。

本文不把完整 Weil 正性重新命名為新定理。對全部合法卷積平方證明所需符號，正是與 RH 等價或極其接近的既有核心困難。

---

# 摘要

令
\[
F(z)=\xi\left(\frac12+z\right)
\]
並採用譜坐標
\[
s=\frac12+iw,
\qquad
w=-i\left(s-\frac12\right).
\]
RH 等價於全部非平凡零點所對應的 \(w\) 均為實數。

本文在乘法群
\[
\mathbb R_+^\times=(0,\infty)
\]
上固定 Haar 測度
\[
d^\times x=\frac{dx}{x}
\]
與 Mellin 轉換
\[
\widetilde f(s)=\int_0^\infty f(x)x^s\,d^\times x
=\int_0^\infty f(x)x^{s-1}\,dx.
\]
對
\[
g^\sharp(x)=x^{-1}g(x^{-1}),
\qquad
f_g=g*\overline g^{\,\sharp},
\]
有
\[
\widetilde f_g(s)
=
\widetilde g(s)\,
\overline{\widetilde g(1-\overline s)}.
\]
Riemann–Weil 顯式公式採用：
\[
\widetilde f(0)
-\sum_{\rho}\widetilde f(\rho)
+\widetilde f(1)
=
\sum_v\mathcal W_v(f).
\]
若
\[
\widetilde g(0)=\widetilde g(1)=0,
\]
則
\[
Q_\zeta(g)
:=
-\sum_v\mathcal W_v(f_g)
=
\sum_\rho
\widetilde g(\rho)
\overline{\widetilde g(1-\overline\rho)}.
\]
令
\[
G(w)=\widetilde g\left(\frac12+iw\right).
\]
零點 \(\rho=\frac12+iw_\rho\) 的區塊為
\[
G(w_\rho)\overline{G(\overline{w_\rho})}.
\]
當 \(w_\rho\in\mathbb R\) 時，此量為
\[
|G(w_\rho)|^2\ge0.
\]
當 \(w_\rho\notin\mathbb R\) 時，配對後的實區塊為
\[
B_w(G)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right),
\]
其符號不定。

本文進一步證明一個區域相位塑形架構。令
\[
K\Subset\{w:\operatorname{Re}w>0,\ \operatorname{Im}w<0\}
\]
為一個與實軸及 \(\pm i/2\) 分離的緊矩形，並假設平方像
\[
K^2=\{w^2:w\in K\}
\]
與其共軛可用多項式逼近。則對任意足夠小的 \(\varepsilon>0\)，可以構造實偶
\[
\psi\in C_c^\infty(\mathbb R)
\]
使其 Fourier 轉換 \(G\) 滿足：
\[
G\left(\pm\frac i2\right)=0,
\]
並在 \(K\) 上一致近似 \(i\)。由實偶對稱，自動有
\[
G(-w)=G(w),
\qquad
G(\overline w)=\overline{G(w)}.
\]
因此在整個軌道飽和集
\[
K\cup(-K)\cup\overline K\cup(-\overline K)
\]
上，
\[
2\operatorname{Re}(G(w)^2)\le-c<0.
\]
此構造只依賴區域 \(K\)，不依賴矩形內零點的精確位置，故可以與前一篇的有理矩形繞數證書對接。

在算術側，若
\[
\operatorname{supp}\psi\subseteq[-L/2,L/2],
\]
則 \(f_g\) 的乘法支撐包含於
\[
[e^{-L},e^L].
\]
有限位置項只涉及滿足
\[
m\log p\le L
\]
的有限個質數冪。本文因此定義支撐—質數啟動集
\[
\mathcal P_L
=
\{p^m:m\log p\le L\}
\]
與支撐過濾矩陣
\[
M_L
=
M_\infty
+
\sum_{p^m\in\mathcal P_L}M_{p^m}.
\]
這給出固定尺度上的有限算術證書問題。

全文最後把 RH 路線壓縮為一個定量比較：
\[
L_{\mathrm{sep}}(K,c,\varepsilon)
\stackrel{?}{\le}
L_{\mathrm{arith}+}(c,\varepsilon),
\]
其中左側是將偏軸區域塑形成一致負區塊所需的最小支撐成本，右側是算術側仍能獨立證明非負的最大支撐尺度。若兩者永不重疊，此路線無法證明 RH；若對每個假設偏軸矩形均存在可審計重疊，才可能形成矛盾。

**關鍵詞：** 黎曼猜想、Riemann–Weil 顯式公式、Mellin 轉換、卷積平方、Paley–Wiener、多項式逼近、區域負方向、質數啟動過濾、半正定證書、ZFC

---

# 1. 本篇的研究位置

## 1.1 已完成的前半段

前置研究建立：
\[
\text{偏軸零點}
\Longrightarrow
\text{正除子障礙}
\Longrightarrow
\text{正則矩形繞數證書}.
\]

若 RH 失敗，則存在右半臨界帶中的有理矩形 \(R\)，使
\[
\omega_R(F)>0.
\]

## 1.2 尚缺的後半段

需要將：
\[
\omega_R(F)>0
\]
提升為某個顯式公式測試函數 \(g_R\)，使：
\[
Q_\zeta(g_R)<0.
\]

再由質數側獨立證明：
\[
Q_\zeta(g_R)\ge0.
\]

## 1.3 本文的分解

本文不一次假設完整提升成立，而拆成：
\[
\boxed{
\text{區域負塑形}
+
\text{全域洩漏界}
+
\text{算術非負錐}.
}
\]

三者缺一不可。

---

# 2. 固定乘法群正規化

## 2.1 乘法群

令：
\[
\mathbb G_m^+=\mathbb R_+^\times.
\]

Haar 測度：
\[
d^\times x=\frac{dx}{x}.
\]

## 2.2 Mellin 轉換

對
\[
f\in C_c^\infty(\mathbb R_+^\times)
\]
定義：
\[
\widetilde f(s)
=
\int_0^\infty f(x)x^s\,d^\times x.
\]

## 2.3 乘法卷積

定義：
\[
(f*h)(x)
=
\int_0^\infty f(y)h(x/y)\,d^\times y.
\]

則：
\[
\widetilde{f*h}(s)
=
\widetilde f(s)\widetilde h(s).
\]

## 2.4 sharp 對合

定義：
\[
g^\sharp(x)=x^{-1}g(x^{-1}).
\]

再令：
\[
\overline g(x)=\overline{g(x)}.
\]

則：
\[
\widetilde{\overline g^{\,\sharp}}(s)
=
\overline{\widetilde g(1-\overline s)}.
\]

## 2.5 卷積平方

定義：
\[
f_g
=
g*\overline g^{\,\sharp}.
\]

因此：
\[
\boxed{
\widetilde f_g(s)
=
\widetilde g(s)
\overline{\widetilde g(1-\overline s)}.
}
\]

這是本文固定使用的二次型核。

---

# 3. Riemann–Weil 顯式公式

## 3.1 全域公式

對合法測試函數 \(f\)，採用：
\[
\boxed{
\widetilde f(0)
-
\sum_{\rho\in Z_\zeta}
\widetilde f(\rho)
+
\widetilde f(1)
=
\sum_v\mathcal W_v(f).
}
\]

其中：

- \(Z_\zeta\) 為非平凡零點多重集；
- \(v\) 遍歷 archimedean 與全部有限位置；
- \(\mathcal W_v\) 為對應局部分布；
- 零點和依定理指定的對稱或正則化方式理解。

## 3.2 端點消去

要求：
\[
\widetilde g(0)=0,
\qquad
\widetilde g(1)=0.
\]

則：
\[
\widetilde f_g(0)
=
\widetilde g(0)\overline{\widetilde g(1)}
=
0,
\]
以及：
\[
\widetilde f_g(1)
=
\widetilde g(1)\overline{\widetilde g(0)}
=
0.
\]

故：
\[
-\sum_\rho\widetilde f_g(\rho)
=
\sum_v\mathcal W_v(f_g).
\]

## 3.3 Weil 二次型

定義：
\[
Q_\zeta(g)
=
-\sum_v\mathcal W_v(f_g).
\]

則：
\[
\boxed{
Q_\zeta(g)
=
\sum_\rho
\widetilde g(\rho)
\overline{\widetilde g(1-\overline\rho)}.
}
\]

## 3.4 符號約定

本文採用：
\[
\mathrm{RH}
\Longrightarrow
Q_\zeta(g)\ge0.
\]

等價地：
\[
\sum_v\mathcal W_v(f_g)\le0.
\]

所有後續「算術非負」均指 \(Q_\zeta\) 的符號，而不是個別 \(\mathcal W_v\) 的符號。

---

# 4. 對數—單位化坐標

## 4.1 對數變數

令：
\[
x=e^t.
\]

定義：
\[
\psi(t)
=
e^{t/2}g(e^t).
\]

則：
\[
g(e^t)=e^{-t/2}\psi(t).
\]

## 4.2 Fourier–Mellin 對應

對：
\[
s=\frac12+iw,
\]
有：
\[
\widetilde g\left(\frac12+iw\right)
=
\int_{\mathbb R}\psi(t)e^{iwt}\,dt.
\]

定義：
\[
G(w)
=
\widehat\psi(w)
=
\widetilde g\left(\frac12+iw\right).
\]

## 4.3 端點條件

當 \(s=0\)：
\[
w=\frac i2.
\]

當 \(s=1\)：
\[
w=-\frac i2.
\]

所以端點消去等價於：
\[
\boxed{
G\left(\frac i2\right)
=
G\left(-\frac i2\right)
=
0.
}
\]

## 4.4 實偶測試函數

若：
\[
\psi(t)\in\mathbb R,
\qquad
\psi(-t)=\psi(t),
\]
則：
\[
G(-w)=G(w),
\]
且：
\[
G(\overline w)=\overline{G(w)}.
\]

這正好匹配零點的 \(\pm\) 與共軛對稱。

---

# 5. 零點側的軌道區塊

## 5.1 譜坐標

對零點：
\[
\rho=\frac12+iw_\rho,
\]
有：
\[
1-\overline\rho
=
\frac12+i\overline{w_\rho}.
\]

因此：
\[
\widetilde f_g(\rho)
=
G(w_\rho)
\overline{G(\overline{w_\rho})}.
\]

## 5.2 臨界線零點

若：
\[
w_\rho\in\mathbb R,
\]
則：
\[
\widetilde f_g(\rho)
=
|G(w_\rho)|^2
\ge0.
\]

## 5.3 偏軸零點

若：
\[
w\notin\mathbb R,
\]
將 \(w\) 與 \(\overline w\) 配對，得到：
\[
B_w(G)
=
G(w)\overline{G(\overline w)}
+
G(\overline w)\overline{G(w)}.
\]

故：
\[
\boxed{
B_w(G)
=
2\operatorname{Re}
\left(
G(w)\overline{G(\overline w)}
\right).
}
\]

## 5.4 實偶化後

若 \(G\) 具有實結構：
\[
G(\overline w)=\overline{G(w)},
\]
則：
\[
\overline{G(\overline w)}=G(w).
\]

所以：
\[
\boxed{
B_w(G)
=
2\operatorname{Re}(G(w)^2).
}
\]

若：
\[
G(w)\approx i,
\]
則：
\[
B_w(G)\approx-2.
\]

這是區域負塑形的代數核心。

---

# 6. 從點插值提升到區域塑形

## 6.1 點插值的不足

對單一假設零點 \(w_0\) 指定：
\[
G(w_0)=i
\]
很容易在有限整函數插值中完成。

但若 \(w_0\) 未知，只知道：
\[
w_0\in K,
\]
點插值不能形成可由矩形證書驅動的測試函數。

## 6.2 區域目標

需要一個只依賴 \(K\) 的 \(G_K\)，使：
\[
2\operatorname{Re}(G_K(w)^2)\le-c_K<0
\qquad
\forall w\in K.
\]

這稱為**區域一致負塑形**。

## 6.3 軌道飽和

令：
\[
K\Subset
\{w:
\operatorname{Re}w>0,\ 
\operatorname{Im}w<0
\}.
\]

其軌道飽和為：
\[
K^G
=
K\cup(-K)\cup\overline K\cup(-\overline K).
\]

實偶 \(G\) 只需在 \(K\) 上塑形，其他三塊由對稱自動決定。

---

# 7. Paley–Wiener 區域相位塑形引理

## 7.1 幾何假設

令 \(K\) 為緊矩形，滿足：

\[
\operatorname{dist}(K,\mathbb R)>0,
\]

\[
\operatorname{dist}
\left(
K,\left\{\frac i2,-\frac i2\right\}
\right)>0,
\]

\[
\inf_{w\in K}|\operatorname{Re}w|>0.
\]

最後一項排除 \(w^2\) 落在實軸的退化。

令：
\[
E=K^2\cup\overline{K^2},
\qquad
K^2=\{w^2:w\in K\}.
\]

假設 \(\mathbb C\setminus E\) 連通；對足夠小、互不相交的矩形通常可藉細分達成。

## 7.2 引理

### 引理 7.1（區域相位塑形）

對任意：
\[
0<\varepsilon<\frac14,
\]
存在實偶函數：
\[
\psi\in C_c^\infty(\mathbb R)
\]
使其 Fourier 轉換 \(G\) 滿足：

1. 
   \[
   G(-w)=G(w);
   \]
2. 
   \[
   G(\overline w)=\overline{G(w)};
   \]
3. 
   \[
   G\left(\pm\frac i2\right)=0;
   \]
4. 對所有 \(w\in K\)：
   \[
   |G(w)-i|<\varepsilon.
   \]

因此：
\[
2\operatorname{Re}(G(w)^2)
\le
-2\left(1-2\varepsilon-\varepsilon^2\right)
<0
\]
對所有 \(w\in K\) 成立。

## 7.3 證明架構

### 步驟一：近似常數的 Paley–Wiener 基底

取實偶：
\[
h\in C_c^\infty(\mathbb R),
\qquad
\int h(t)\,dt=1.
\]

令：
\[
h_\delta(t)=\delta^{-1}h(t/\delta).
\]

其 Fourier 轉換：
\[
H_\delta(w)=H(\delta w)
\]
在任意固定緊集上一致趨近：
\[
1.
\]

選擇 \(\delta\) 足夠小，使 \(H_\delta\) 在 \(K^G\) 上無零點且接近 \(1\)。

### 步驟二：加入端點零點

令：
\[
Z_0(w)=w^2+\frac14.
\]

則：
\[
Z_0\left(\pm\frac i2\right)=0.
\]

由幾何假設，\(Z_0\) 在 \(K^G\) 上無零點。

### 步驟三：在平方像上定義目標函數

在 \(K^2\) 上定義：
\[
q(u)
=
\frac{i}
{
(u+\frac14)
H_\delta(\sqrt u)
},
\]
其中表達應理解為由偶函數
\[
H_\delta(w)
\]
下降到 \(u=w^2\) 的全純函數。

在 \(\overline{K^2}\) 上以共軛規則定義：
\[
q(\overline u)=\overline{q(u)}.
\]

### 步驟四：多項式逼近

由 \(E\) 的多項式逼近條件，可取多項式 \(p(u)\)，在 \(E\) 上一致逼近 \(q(u)\)。

再以：
\[
p_{\mathbb R}(u)
=
\frac12
\left(
p(u)+\overline{p(\overline u)}
\right)
\]
取得實係數多項式，並保持近似精度。

### 步驟五：建立 Fourier 轉換

定義：
\[
G(w)
=
\left(w^2+\frac14\right)
p_{\mathbb R}(w^2)
H_\delta(w).
\]

則 \(G\)：

- 為整函數；
- 為實偶；
- 在 \(\pm i/2\) 為零；
- 在 \(K\) 上一致近似 \(i\)。

### 步驟六：回到緊支撐原像

多項式乘法：
\[
p_{\mathbb R}(w^2)H_\delta(w)
\]
在 Fourier 反變換側對應對 \(h_\delta\) 施加有限階常係數微分算子。

因此其反變換仍屬：
\[
C_c^\infty(\mathbb R),
\]
且支撐不因微分擴大。

證明架構完成。

## 7.4 引理的實質

引理證明：

> 對一個與實軸分離的有限偏軸區域，Paley–Wiener 類本身具有足夠自由度，可以在整個區域中形成一致負的零點軌道區塊。

這比單點插值更強，也不依賴矩形內零點的精確位置。

## 7.5 引理沒有解決的事

它沒有控制：

- \(K^G\) 外的 \(G\)；
- 全部臨界線零點總和；
- 其他偏軸零點；
- archimedean 項；
- 質數側符號；
- 所需支撐尺度的最佳大小。

---

# 8. 從有理矩形證書到區域負方向

## 8.1 坐標轉換

前一篇的右半帶矩形：
\[
R\Subset
\left\{
z:
0<\operatorname{Re}z<\frac12
\right\}
\]
經：
\[
w=-iz
\]
變成位於：
\[
\operatorname{Im}w<0
\]
的譜矩形 \(K_R\)。

## 8.2 非平凡零點的水平坐標

若 \(z=\beta+i\gamma\)，則：
\[
w=\gamma-i\beta.
\]

非平凡零點具有非零高度 \(\gamma\)，故可將矩形細分，使：
\[
\operatorname{Re}w
\]
與 \(0\) 分離。

## 8.3 區域負證書

若：
\[
\omega_R(F)>0,
\]
則 \(K_R\) 中存在至少一個偏軸零點。

由引理可構造 \(G_R\)，使每個位於 \(K_R\) 的零點軌道均貢獻：
\[
B_w(G_R)\le-c_R<0.
\]

因此目標區域總貢獻滿足：
\[
Q_{K_R}^{\mathrm{zero}}(G_R)
\le
-c_R\,\omega_R(F)
\]
至軌道倍數與重數正規化。

## 8.4 真正新增的箭頭

本文因此完成一個條件明確的箭頭：
\[
\boxed{
\omega_R(F)>0
\Longrightarrow
\text{存在合法 Paley–Wiener 區域負方向}.
}
\]

但尚未得到：
\[
Q_\zeta(g_R)<0,
\]
因為區域外貢獻尚未控制。

---

# 9. 支撐與有限質數啟動

## 9.1 支撐尺度

若：
\[
\operatorname{supp}\psi
\subseteq
[-L/2,L/2],
\]
則對應的乘法函數 \(g\) 支撐於：
\[
[e^{-L/2},e^{L/2}].
\]

## 9.2 卷積平方支撐

因乘法卷積的支撐相乘：
\[
\operatorname{supp}f_g
\subseteq
[e^{-L},e^L].
\]

## 9.3 有限位置分布

在本文正規化下，有限位置項可寫成：
\[
\mathcal W_p(f)
=
(\log p)
\sum_{m\ge1}
\left(
f(p^m)+p^{-m}f(p^{-m})
\right),
\]
其確切解讀與端點慣例由採用的顯式公式定理固定。

若：
\[
p^m>e^L,
\]
則：
\[
f(p^m)=0.
\]

同樣，只有對應落在支撐中的倒數項可能非零。

因此只需考慮：
\[
m\log p\le L.
\]

## 9.4 質數啟動集

定義：
\[
\mathcal P_L
=
\left\{
(p,m):
p\text{ 為質數},\
m\ge1,\
m\log p\le L
\right\}.
\]

它是有限集。

## 9.5 算術過濾

當 \(L\) 增加時，新質數冪只在離散閾值：
\[
L=m\log p
\]
被啟動。

因此得到：
\[
\mathcal P_{L_1}
\subseteq
\mathcal P_{L_2}
\qquad
(L_1\le L_2).
\]

這稱為**支撐—質數啟動過濾**。

---

# 10. 小支撐與大支撐的張力

## 10.1 小支撐優勢

小 \(L\) 意味：

- 啟動的質數較少；
- 算術側較容易精確計算；
- archimedean 分布可能具有較強的局部正性；
- 證書矩陣較小。

在支撐不觸及最小質數閾值時，甚至可能只有 archimedean 位置參與。

## 10.2 小支撐劣勢

小 \(L\) 使 \(G\) 的譜分辨率受限。

要在：

- 高度很高；
- 距離實軸很近；
- 與其他零點非常接近；

的區域中塑形，通常需要更大 \(L\)。

## 10.3 大支撐優勢

大 \(L\) 允許：

- 更細的譜局部化；
- 更小的區域洩漏；
- 更複雜的插值與相位控制。

## 10.4 大支撐劣勢

大 \(L\) 啟動更多：
\[
p^m.
\]

質數側符號變得更複雜，精確證書成本上升。

## 10.5 核心定量競爭

定義分離成本：
\[
L_{\mathrm{sep}}(K;c,\varepsilon)
\]
為產生目標負值 \(c\)、區域外洩漏不超過 \(\varepsilon\) 所需的最小支撐尺度。

定義算術正性半徑：
\[
L_{\mathrm{arith}+}(\mathcal C)
\]
為在指定結構錐 \(\mathcal C\) 中仍能獨立證明：
\[
Q_\zeta(g)\ge0
\]
的最大尺度。

需要：
\[
\boxed{
L_{\mathrm{sep}}(K;c,\varepsilon)
\le
L_{\mathrm{arith}+}(\mathcal C).
}
\]

---

# 11. archimedean 局部正性作為邊界案例

## 11.1 已知背景的使用方式

既有 Weil 正性研究顯示，在特定小支撐、端點消去與額外線性條件下，archimedean 分布可由正算子或壓縮跡提供非負下界。

本文只把這視為：

\[
L_{\mathrm{arith}+}>0
\]
可能成立的局部證據。

## 11.2 不能直接推出 RH

小支撐正性只覆蓋測試函數空間的一個小錐。

若此錐不足以對任意靠近實軸的偏軸區域進行相位塑形，就不能排除全部偏軸零點。

## 11.3 需要比較而非命名

不能因為：
\[
Q_\infty(g)\ge0
\]
在一個小支撐子空間成立，就稱「RH 的 archimedean 部分已證明」。

真正需比較：
\[
\text{正性錐的支撐範圍}
\]
與：
\[
\text{分離任意偏軸區域的最小支撐}.
\]

---

# 12. 算術可計算錐

## 12.1 定義目的

不能將：
\[
\mathcal G_{\mathrm{arith}+}
=
\{g:Q_\zeta(g)\ge0\}
\]
作為定義，因為這只是把結論寫入集合。

需要一個由可驗證充分條件生成的錐。

## 12.2 證書生成器

令：
\[
\mathsf{Cert}_L(g)
\]
包含：

1. \(g\) 或 \(\psi\) 的精確表示；
2. 支撐證明；
3. 端點消去證明；
4. archimedean 項的下界；
5. 每個啟動質數冪項的精確區間；
6. 零點和與局部和的合法性；
7. 總誤差上界。

## 12.3 可計算錐

定義：
\[
\mathcal C_L^{\mathrm{cert}}
=
\left\{
g:
\mathsf{Cert}_L(g)
\text{ 證明 }
Q_\zeta(g)\ge0
\right\}.
\]

此定義不是循環的前提是證書只使用：

- 顯式公式；
- 有限質數資料；
- archimedean 分析；
- 區間算術；
- 無條件估計；

而不使用 RH 或等價準則。

## 12.4 錐性

若證書方法對：

- 非負縮放；
- 直和；
- 正半定矩陣組合；

封閉，則 \(\mathcal C_L^{\mathrm{cert}}\) 可形成凸錐。

---

# 13. 有限維矩陣化

## 13.1 基底

選取支撐於：
\[
[-L/2,L/2]
\]
的實偶平滑基底：
\[
\psi_1,\ldots,\psi_N.
\]

令：
\[
\psi_c=\sum_{j=1}^Nc_j\psi_j,
\qquad
c\in\mathbb R^N.
\]

## 13.2 Fourier 評價向量

定義：
\[
v(w)
=
\begin{pmatrix}
G_1(w)\\
\vdots\\
G_N(w)
\end{pmatrix}.
\]

則：
\[
G_c(w)=c^\top v(w).
\]

## 13.3 目標軌道矩陣

對偏軸點 \(w\)，定義實對稱矩陣：
\[
M_{\mathrm{orb}}(w)
=
2\operatorname{Re}
\left(
v(w)v(w)^\top
\right)
\]
在實偶正規化下，使：
\[
B_w(G_c)
=
c^\top M_{\mathrm{orb}}(w)c.
\]

## 13.4 archimedean 矩陣

定義：
\[
(M_\infty)_{jk}
=
-\mathcal W_\infty
\left(
g_j*\overline{g_k}^{\,\sharp}
\right)
\]
經 Hermitian／實對稱化。

## 13.5 有限位置矩陣

對每個啟動質數冪，定義相應雙線性取樣矩陣。合併為：
\[
M_{\mathrm{fin}}(L)
=
\sum_{(p,m)\in\mathcal P_L}
M_{p,m}.
\]

## 13.6 算術矩陣

\[
M_{\mathrm{arith}}(L)
=
M_\infty
+
M_{\mathrm{fin}}(L).
\]

則：
\[
Q_\zeta(g_c)
=
c^\top M_{\mathrm{arith}}(L)c.
\]

這個等式依完整顯式公式與端點條件理解。

## 13.7 半正定證書

若可嚴格證明：
\[
M_{\mathrm{arith}}(L)\succeq0,
\]
則基底張成空間中的全部測試函數均屬可計算非負錐。

證明方式可以是：

- 精確 \(LDL^\top\) 分解；
- 有理區間 Cholesky；
- 主子式；
- sum-of-squares；
- 經 Lean 驗證的半正定矩陣證書。

---

# 14. 區域矩陣不等式

## 14.1 一致負方向

對矩形 \(K\)，希望找到 \(c\) 使：
\[
c^\top
M_{\mathrm{orb}}(w)c
\le-c_0
\qquad
\forall w\in K.
\]

這是一個半無限二次限制問題。

## 14.2 離散網格不足

只在有限網格點檢查負值不能保證整個矩形成立。

需要：

- 導數 Lipschitz 界；
- Bernstein 型不等式；
- 區間複分析；
- 矩形上的複區間包絡。

## 14.3 精確區域證書

一個區域負證書應包括：
\[
\sup_{w\in K}
c^\top M_{\mathrm{orb}}(w)c
\le-c_0.
\]

## 14.4 與繞數證書結合

若：
\[
\omega_R(F)\ge1
\]
且 \(K=-iR\)，則區域中至少有一個零點，因而目標負貢獻至少：
\[
-c_0.
\]

這不需要知道零點精確位置。

---

# 15. 無窮遠尾部的無條件控制

## 15.1 Paley–Wiener 衰減

若：
\[
\psi\in C_c^\infty([-L/2,L/2]),
\]
則對任意 \(N\ge0\)，在固定水平帶：
\[
|\operatorname{Im}w|\le\frac12
\]
中存在常數 \(C_{N,\psi,L}\)，使：
\[
|G(w)|
\le
C_{N,\psi,L}
e^{(L/2)|\operatorname{Im}w|}
(1+|\operatorname{Re}w|)^{-N}.
\]

## 15.2 軌道區塊界

因此：
\[
|B_w(G)|
\le
2C_{N,\psi,L}^2
e^{L|\operatorname{Im}w|}
(1+|\operatorname{Re}w|)^{-2N}.
\]

在臨界帶中：
\[
|\operatorname{Im}w|<\frac12,
\]
故指數因子有統一上界：
\[
e^{L/2}.
\]

## 15.3 零點計數

利用無條件零點計數：
\[
N(T)=O(T\log T),
\]
可將高度殼層中的零點數控制為多項式—對數增長。

## 15.4 尾部可和性

當 \(N\) 足夠大時：
\[
\sum_{|\operatorname{Re}w_\rho|>T}
|B_{w_\rho}(G)|
\]
收斂，並可給出隨 \(T\to\infty\) 衰減的上界。

## 15.5 已解決與未解決

這說明：

> 對固定測試函數，無窮遠零點尾部原則上可用無條件零點計數與 Paley–Wiener 衰減控制。

仍未解決的是有限控制視窗內其他未知偏軸零點的正洩漏。

---

# 16. 最低偏軸軌道縮減

## 16.1 反證假設

假設存在偏軸零點。

由零點離散性與有限高度零點數，可在偏軸零點中選取最小正高度層：
\[
T_\ast
=
\min
\left\{
|\operatorname{Re}w_\rho|:
w_\rho\notin\mathbb R
\right\}.
\]

這裡 \(\operatorname{Re}w\) 對應傳統零點高度。

## 16.2 最低層以下

在：
\[
|\operatorname{Re}w|<T_\ast
\]
中，所有零點均位於實軸。

對實偶卷積平方，它們的貢獻非負。

## 16.3 同高度軌道

最低高度可能有多個偏軸軌道。

應將同高度的全部偏軸軌道納入一個有限目標區域族，而不是假設唯一。

## 16.4 高度以上

較高零點形成尾部與有限中間窗：

- 足夠高的部分可用衰減控制；
- 介於目標與尾部截斷間的有限未知偏軸軌道仍需洩漏界。

## 16.5 價值

最低偏軸縮減避免了「目標以下還有未知偏軸正洩漏」，但不能完全消除目標以上的未知貢獻。

---

# 17. 目標依賴與算術獨立性的張力

## 17.1 弱證人

弱證人可以依賴：

- 偏軸零點精確位置；
- 其他零點位置；
- 完整零點集合。

這類證人容易由插值構造，但其算術側通常不能獨立預先證明正性。

## 17.2 區域證人

區域證人只依賴：

- 一個有理矩形；
- 支撐尺度；
- 誤差參數。

它可與繞數證書對接，不需要零點座標。

本文的相位塑形引理屬於此類。

## 17.3 算術原生證人

更強的證人由：

- 有理係數基底；
- 有限質數資料；
- archimedean 算子；
- 半正定規劃；

直接產生。

它不依賴任何未知零點。

## 17.4 真正需要的版本

非循環證明最理想的形式是：

\[
\text{矩形 }R
\longmapsto
g_R
\]
由區域幾何與算術資料共同決定，並同時滿足：

\[
\text{區域負塑形}
\]
與：
\[
\text{算術非負證書}.
\]

---

# 18. 矛盾證書架構

## 18.1 輸入

假設有正則矩形 \(R\) 且：
\[
\omega_R(F)>0.
\]

## 18.2 區域負證書

構造 \(g_R\)，證明：
\[
Q_R^{\mathrm{target}}(g_R)
\le-c_R<0.
\]

## 18.3 洩漏證書

證明：
\[
Q_{\mathrm{rest}}^{\mathrm{zero}}(g_R)
\le E_R.
\]

這裡是上界，因要排除其他零點產生足以抵消的正值。

## 18.4 支配條件

要求：
\[
E_R<c_R.
\]

因此：
\[
Q_\zeta(g_R)<0.
\]

## 18.5 算術證書

另一方面，由：
\[
g_R\in\mathcal C_L^{\mathrm{cert}}
\]
得到：
\[
Q_\zeta(g_R)\ge0.
\]

## 18.6 矛盾

\[
Q_\zeta(g_R)<0
\quad\land\quad
Q_\zeta(g_R)\ge0.
\]

故：
\[
\omega_R(F)=0.
\]

若對全部正則有理矩形完成，則 RH 成立。

---

# 19. 條件式主定理

### 定理 19.1（區域證書型條件定理）

假設對每個右半臨界帶中的正則有理矩形 \(R\)，存在一個算法或 ZFC 可定義程序產生 \(g_R\)，並可證明：

1. 若 \(\omega_R(F)>0\)，則目標區域零點貢獻至多 \(-c_R<0\)；
2. 全部非目標零點貢獻至多 \(E_R<c_R\)；
3. \(g_R\) 滿足顯式公式的全部合法性條件；
4. 由有限質數資料與 archimedean 證書可證：
   \[
   Q_\zeta(g_R)\ge0.
   \]

則 RH 成立。

### 證明

若 RH 失敗，由可數矩形判定定理，存在 \(R\) 使：
\[
\omega_R(F)>0.
\]

由 1 與 2：
\[
Q_\zeta(g_R)
\le
-c_R+E_R
<0.
\]

由 4：
\[
Q_\zeta(g_R)\ge0.
\]

矛盾。故全部矩形繞數為零，RH 成立。證畢。

## 19.2 定理地位

此定理是證書架構，不是 RH 證明。

本文只對條件 1 的「區域內一致負塑形」給出構造架構；條件 2 與條件 4 尚未完成。

---

# 20. 何處可能再次等價於 RH

## 20.1 全域算術矩陣非負

若對一個在測試函數空間中稠密的增長族證明：
\[
M_{\mathrm{arith}}(L)\succeq0
\quad
\forall L,
\]
並能通過極限，這很可能已是完整 Weil 正性。

## 20.2 任意區域零洩漏

若聲稱每個偏軸區域都存在完全消去所有其他零點的合法測試函數，可能隱含了對整個零點集合的過強插值能力。

## 20.3 使用 RH 下的尾界

某些精細零點間距、密度或譜估計可能已假設 RH。

## 20.4 以「算術錐」重新命名結論

若算術錐定義為：
\[
\{g:Q_\zeta(g)\ge0\},
\]
則交集問題只是同義反覆。

---

# 21. ZFC 與形式化審計

## 21.1 定義模組

```text
MultiplicativeGroupPositive
HaarMeasureMul
MellinTransform
MulConvolution
SharpInvolution
WeilConvolutionSquare
```

## 21.2 顯式公式接口

```text
RiemannWeilTestClass
FinitePlaceDistribution
ArchimedeanDistribution
ExplicitFormula
EndpointVanishing
WeilQuadraticForm
```

顯式公式應作為已證外部定理匯入，而不是新公理。

## 21.3 區域塑形模組

```text
SpectralRectangle
OrbitSaturation
SquareImageCompact
PolynomialApproximationHypothesis
PaleyWienerPhaseShaper
UniformNegativeOrbitBlock
```

## 21.4 支撐過濾模組

```text
LogSupportRadius
ConvolutionSupport
ActivatedPrimePowers
FinitePrimeContribution
```

## 21.5 矩陣證書

```text
TestBasis
ArithmeticMatrix
OrbitMatrix
IntervalPSD
RegionalNegativeBound
```

## 21.6 信任邊界

必須列出：

- 複分析函數庫；
- Mellin／Fourier 轉換正規化；
- 顯式公式來源；
- 多項式逼近定理；
- 零點計數定理；
- 質數列表生成；
- 區間算術；
- 半正定證書檢查器。

## 21.7 禁止隱藏的假設

不得把以下內容作為未標記公理：

```text
all_arithmetic_matrices_psd
all_regional_leakage_small
all_off_axis_rectangles_separable_within_positive_radius
RH
WeilPositivity
```

---

# 22. 計算原型

## 22.1 第一階段：純區域塑形

輸入：

- 偏軸矩形 \(K\)；
- 支撐 \(L\)；
- 基底維度 \(N\)。

求解：
\[
\min_c
\sup_{w\in K}
2\operatorname{Re}(G_c(w)^2)
\]
並要求：
\[
G_c(\pm i/2)=0.
\]

## 22.2 第二階段：加入軸上洩漏

加入：
\[
\int_{\mathbb R}
|G_c(t)|^2\,d\mu_{\mathrm{majorant}}(t)
\]
或由零點計數推導的離散上界。

## 22.3 第三階段：加入質數矩陣

構造：
\[
M_{\mathrm{arith}}(L).
\]

尋找同時滿足：

\[
c^\top M_{\mathrm{arith}}(L)c\ge0
\]
與：
\[
\sup_{w\in K}
c^\top M_{\mathrm{orb}}(w)c<0.
\]

## 22.4 第四階段：精確化

將浮點候選轉為：

- 有理係數；
- 區間證書；
- 精確支撐；
- 嚴格區域上界；
- PSD 證書。

## 22.5 實驗判定

若反覆發現：

\[
L_{\mathrm{sep}}(K)
>
L_{\mathrm{arith}+},
\]
則此路線可能存在結構性不相容。

---

# 23. 本文真正完成的部分

本文完成：

1. 固定乘法群 Riemann–Weil 正規化；
2. 固定 \(Q_\zeta\) 的符號方向；
3. 將端點消去轉為 \(G(\pm i/2)=0\)；
4. 展開臨界線模平方與偏軸不定區塊；
5. 將單點負插值提升為區域一致負塑形問題；
6. 提出 Paley–Wiener 區域相位塑形引理與構造；
7. 將有理矩形繞數證書連到區域負方向；
8. 建立支撐—質數啟動過濾；
9. 建立算術有限矩陣與 PSD 證書框架；
10. 給出無窮遠零點尾部的無條件控制方向；
11. 建立最低偏軸軌道縮減；
12. 建立完整 ZFC 證書架構。

---

# 24. 本文仍未完成的部分

本文沒有完成：

1. 有限控制窗內其他未知偏軸零點的統一洩漏上界；
2. 對區域塑形引理給出最佳支撐常數；
3. 建立非平凡的大支撐算術非負錐；
4. 證明區域塑形函數落入該非負錐；
5. 形式化完整 archimedean 主值分布；
6. 建立任何足以排除實際矩形的矛盾證書；
7. 證明 RH。

---

# 25. 下一輪研究方向

本系列原規劃的四篇方法論論文至此完成。

下一輪不宜再繼續增加同義的 RH 等價式，而應轉入兩條工程分支。

## 分支 A：區域相位塑形原型

建立：

- 實偶 bump 基底；
- 端點零點算子；
- 矩形複區間評價；
- 最小支撐搜尋；
- 區域一致負證書。

## 分支 B：算術矩陣原型

固定有限維基底，實作：

- archimedean 矩陣；
- 啟動質數冪矩陣；
- 區間 PSD；
- 支撐閾值掃描；
- 與區域負矩陣的交集測試。

完成兩個原型後，才能判定：
\[
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\]
是否具有實際研究空間。

---

# 26. 結論

本篇把前一篇的抽象交集問題：
\[
\mathcal G_{\mathrm{sep}}
\cap
\mathcal G_{\mathrm{arith}+}
\stackrel{?}{\ne}\varnothing
\]
進一步拆成可操作結構。

第一個主要結果是區域相位塑形：

\[
\boxed{
\text{偏軸矩形}
\Longrightarrow
\text{Paley–Wiener 區域一致負方向}.
}
\]

此構造使用：

- 對數—Mellin 轉換；
- 實偶 Fourier 對稱；
- \(w^2\) 軌道商；
- 多項式逼近；
- 端點因子 \(w^2+\frac14\)；
- 緊支撐 bump 的微分閉性。

第二個主要結構是支撐—質數啟動過濾：

\[
\boxed{
\operatorname{supp}\psi
\subseteq[-L/2,L/2]
\Longrightarrow
\text{只啟動 }m\log p\le L\text{ 的有限質數冪}.
}
\]

這使每個固定尺度的算術側成為有限資料問題。

但兩個結構之間仍存在核心張力：

\[
\text{精細譜分離}
\Longrightarrow
L\text{ 增大}
\Longrightarrow
\text{更多質數項與更難的算術符號}.
\]

因此本路線的真正判定量不是再一個 RH 等價式，而是：

\[
\boxed{
L_{\mathrm{sep}}(K;c,\varepsilon)
\stackrel{?}{\le}
L_{\mathrm{arith}+}(\mathcal C).
}
\]

若對任意偏軸矩形均能建立此重疊，再加上有限窗洩漏與無窮遠尾部控制，就可以形成：

\[
Q_\zeta(g_R)<0
\quad\land\quad
Q_\zeta(g_R)\ge0.
\]

若無法建立重疊，拓樸—顯式公式路線將停在一個精確但不足的判定架構。

本文因此沒有證明 RH，但完成了本輪最重要的技術壓縮：

> **偏軸區域本身可以被合法 Paley–Wiener 測試函數塑形成一致負方向；真正未解的是，這種負方向能否在控制全部其他零點的同時，落入一個不以 RH 為前提的算術非負錐。**

---

# 附錄 A：主要符號

| 符號 | 意義 |
|---|---|
| \(d^\times x\) | 乘法 Haar 測度 \(dx/x\) |
| \(\widetilde f\) | Mellin 轉換 |
| \(g^\sharp\) | \(x^{-1}g(x^{-1})\) |
| \(f_g\) | \(g*\overline g^{\,\sharp}\) |
| \(\mathcal W_v\) | Riemann–Weil 局部分布 |
| \(Q_\zeta\) | 本文符號下的 Weil 二次型 |
| \(\psi\) | 對數—單位化測試函數 |
| \(G\) | \(\widehat\psi(w)=\widetilde g(1/2+iw)\) |
| \(B_w(G)\) | 偏軸軌道區塊 |
| \(K\) | 偏軸譜矩形 |
| \(L\) | 對數支撐尺度 |
| \(\mathcal P_L\) | 啟動質數冪集 |
| \(M_{\mathrm{arith}}(L)\) | 固定支撐算術矩陣 |
| \(L_{\mathrm{sep}}\) | 區域分離成本 |
| \(L_{\mathrm{arith}+}\) | 算術可證非負半徑 |

---

# 附錄 B：邏輯地位表

| 命題 | 地位 |
|---|---|
| Riemann–Weil 顯式公式 | 已知外部定理 |
| Weil 正性與 RH 的關係 | 已知背景 |
| 臨界線區塊為模平方 | 代數恆等式 |
| 偏軸區塊符號不定 | 代數恆等式 |
| 有限支撐只啟動有限質數冪 | 支撐直接結果 |
| Paley–Wiener 區域相位塑形 | 本文構造架構；公開前需完整定理審校 |
| 無窮遠尾部可由快速衰減控制 | 標準分析架構 |
| 有限窗全部未知偏軸洩漏可控制 | 未證 |
| 大支撐算術矩陣非負 | 未證 |
| 全部矩形可產生矛盾證書 | 未證；足以推出 RH |
| RH | 未證 |

---

# 附錄 C：循環性檢查表

任何候選證書都必須回答：

1. 是否使用了「其他零點均在臨界線」？
2. 是否使用了 RH 下的零點密度界？
3. 算術錐是否直接用 \(Q_\zeta\ge0\) 定義？
4. 是否只在有限網格上檢查區域負值？
5. 是否證明 \(G(\pm i/2)=0\)？
6. 是否固定 Mellin 與局部分布正規化？
7. 是否控制全部啟動質數冪？
8. 是否控制 archimedean 主值項？
9. 是否控制有限窗內非目標偏軸零點？
10. 是否把浮點 PSD 誤當成精確 PSD？
11. 是否列出使用的選擇公理、逼近定理與外部數值庫？
12. 是否能將全部額外假設消去回 ZFC？

---

# 附錄 D：參考背景

1. A. Weil, *Sur les formules explicites de la théorie des nombres premiers*, 1952.  
2. A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Mathematica 5 (1999), 29–106.  
3. A. Connes and C. Consani, *Weil positivity and Trace formula, the archimedean place*, Selecta Mathematica 27 (2021); arXiv:2006.13771.  
4. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*, Annales de l’Institut Fourier 57 (2007); arXiv:math/0404394.  
5. 經典 Paley–Wiener 定理、Mergelyan 多項式逼近定理與 Guinand–Weil 顯式公式文獻。  

---

# 附錄 E：版本邊界

v0.1 已完成：

- 固定乘法群正規化；
- 展開有限位置啟動規則；
- 區域相位塑形構造；
- 矩形證書到負方向接口；
- 算術矩陣與 PSD 架構；
- 尾部控制框架；
- 支撐成本比較；
- ZFC 審計規格。

v0.1 尚未完成：

- 區域塑形引理的完整公開級證明；
- archimedean 分布的 Lean 形式化；
- 有限窗未知偏軸洩漏定理；
- 實際矩陣原型；
- 算術非負錐；
- 任何 RH 證明。
