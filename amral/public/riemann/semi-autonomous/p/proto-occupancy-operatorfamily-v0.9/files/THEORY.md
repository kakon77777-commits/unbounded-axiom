# Theory

## 0. 定位

RH 理論上只能由一條基於並可追蹤到 ZFC 的證明依賴鏈完成；若核心命題
依賴另一套未翻譯回 ZFC 的公理或類比系統，所得結論只能是該擴張系統中的
命題。本文不是 RH 證明，而是在研究「RH 相關算子判定怎樣才具有合法的
量詞與依賴語義」。

v0.8 已證明：

$$
\text{count lower}
\not\Longrightarrow
\text{arbitrary dual-measure operator lower mass}.
$$

本節點因此不再壓掉位置變數，而改用 occupancy cells 與 universal
operator family。

## 1. Cell occupancy 的資料型別

令 $\Gamma$ 為帶重數的實際點集。每個 source cell $I_r$ 至少保存：

- cell 的有理端點；
- endpoint convention；
- multiplicity lower $\ell_r$；
- presence theorem identifier；
- source hash 與 certification status。

source cells 必須依 endpoint convention 形成不重疊的計數分割；證明算子
時可把每個 source cell 擴成 closed hull，因為擴大未知位置集合只會使
universal claim 更保守。

合法語句是

$$
\#(\Gamma\cap I_r)\ge\ell_r.
$$

它不是一個 probability measure，也不是一個固定 rank-one operator。

## 2. Occupancy selection transfer theorem

令 $\mathcal H$ 為實 Hilbert 空間，對每個位置 $x$ 有

$$
P_x=p_x\otimes p_x\succeq0.
$$

固定一個可能含負方向的 base operator $C$。對每個 cell 選取
$\ell_r$ 個位置

$$
x_{rk}\in I_r,
\qquad
1\le k\le\ell_r,
$$

並定義 selected operator

$$
W_{\mathrm{sel}}(\mathbf x)
=
C+
\sum_r\sum_{k=1}^{\ell_r}\lambda_rP_{x_{rk}},
\qquad
\lambda_r\ge0.
$$

### 定理 `OccupancySelectionOperatorTransfer`

若：

1. 每個 $I_r$ 中實際至少有 $\ell_r$ 個點；
2. 對所有允許 selection $\mathbf x$，都有

   $$
   W_{\mathrm{sel}}(\mathbf x)\succeq0;
   $$

3. 所有未被選取的實際點皆以同一非負係數 $\lambda_r$ 貢獻 $P_x$；

則包含全部實際點的 operator 亦為 PSD。

### 證明

在每個 cell 由實際點中選出 $\ell_r$ 個，得到某個允許
$\mathbf x_\Gamma$。全部算子可寫成

$$
W_{\mathrm{all}}(\Gamma)
=
W_{\mathrm{sel}}(\mathbf x_\Gamma)
+
\sum_{\text{surplus actual points }z}
\lambda(z)P_z.
$$

第一項由 universal premise 為 PSD；第二項是 PSD operators 的有限和。
故

$$
W_{\mathrm{all}}(\Gamma)\succeq0.
\qquad\square
$$

這個定理保留的是「先有來源支持的 occupancy，再對所有未知位置證明」的
量詞順序，沒有引入任意對偶測度。

## 3. 低負秩 Green–Schur reduction

令正向與負向 representers 分別組成 columns

$$
U=(u_1,\ldots,u_m),
\qquad
V=(v_1,\ldots,v_q),
$$

並令 $D_\lambda,D_\beta$ 為正對角矩陣。考慮

$$
W
=
I+UD_\lambda U^\ast-VD_\beta V^\ast.
$$

記

$$
B=I+UD_\lambda U^\ast\succ0.
$$

由 finite-rank Schur complement，

$$
W\succeq0
\quad\Longleftrightarrow\quad
S
:=
D_\beta^{-1}-V^\ast B^{-1}V
\succeq0.
$$

Woodbury identity 給出

$$
B^{-1}
=
I-U
\left(D_\lambda^{-1}+U^\ast U\right)^{-1}
U^\ast.
$$

因此

$$
S
=
D_\beta^{-1}
-K_{YY}
+K_{YX}
\left(D_\lambda^{-1}+K_{XX}\right)^{-1}
K_{XY}.
$$

若 $q=2$，只需證明

$$
S_{11}>0,
\qquad
\det S>0.
$$

未知位置的維度可很高，但最終 sign test 仍只在負秩 $q$ 上進行。

## 4. 全有理 Dirichlet Green prototype

取

$$
\mathcal H=H_0^1(0,1),
\qquad
\langle f,g\rangle_{\mathcal H}
=
\int_0^1f'(t)g'(t)\,dt.
$$

evaluation representer 的 Green kernel 為

$$
K(s,t)=\min(s,t)-st.
$$

本輪合成模型固定

$$
I_1=
\left[\frac15,\frac25\right],
\qquad
I_2=
\left[\frac35,\frac45\right],
$$

兩個負向位置

$$
y_1=\frac13,
\qquad
y_2=\frac23,
$$

以及

$$
\beta_1=\beta_2=\frac{83}{25}.
$$

要證明的 universal family 是

$$
W(x_1,x_2)
=
I+P_{x_1}+P_{x_2}
-\frac{83}{25}
\left(P_{1/3}+P_{2/3}\right)
\succeq0
$$

對所有

$$
(x_1,x_2)\in I_1\times I_2
$$

成立。

### 4.1 為何 total count $2$ 仍不夠

若只保留 broad union 內總計數為 $2$，允許兩個點都位於 $1/5$。此時
精確 Schur matrix 是

$$
S=
\begin{pmatrix}
\frac{2611}{24651}&-\frac{29}{297}\\
-\frac{29}{297}&\frac{2113}{24651}
\end{pmatrix},
$$

且

$$
\det S
=
-\frac{254}{558009}<0.
$$

取

$$
v=
\left(
-\frac{29}{297},
-\frac{2611}{24651}
\right),
$$

則

$$
v^\mathsf TSv
=
-\frac{663194}{13755479859}<0.
$$

這是精確 count-only failure，不是浮點例子。

### 4.2 覆蓋證書為何必要

直接在 root box

$$
I_1\times I_2
$$

做自然 interval extension 時，Schur determinant enclosure 的 lower
endpoint 為負。這只表示區間相依過估太寬，不表示存在失敗位置。

演算法依序：

1. 對每個 box 重建 interval $K_{XX},K_{XY},K_{YY}$；
2. 以精確有理 interval inverse 包住正向 $2\times2$ system；
3. 建立 interval Schur matrix；
4. 若 Sylvester lower bounds 不足，沿最寬座標中點二分；
5. 直到所有 leaves 通過或達到停止深度。

本例得到：

$$
\text{certified leaves}=8,
\qquad
\text{maximum depth}=7,
$$

最小葉盒 determinant lower bound 為

$$
\frac{
996149099768633906407318481
}{
92259342242007809509970517515625
}
>
1.0797\times10^{-5}.
$$

因此 universal family 在合成 occupancy premise 下成立。

## 5. v0.7 clamped Green 母證書的微半徑提升

v0.7 已對固定原子位置證明抽象算子

$$
W_{21/20}(\mathbf c)\succeq0.
$$

core 的正負部分皆線性依賴 $\alpha$，axis 正向部分記為
$A(\mathbf c)\succeq0$。因此

$$
W_1(\mathbf c)
=
\frac{20}{21}W_{21/20}(\mathbf c)
+
\frac1{21}\left(I+A(\mathbf c)\right)
\succeq
\frac1{21}I.
$$

這一步從 parent positivity 得到不依賴 parent 未知 eigenvalue 的精確
coercivity margin。

### 5.1 Green–Poincaré 擾動界

在 $[-R,R]$ 的 clamped $H_0^2$ 空間，能量為

$$
\tau\int_{-R}^{R}|u''(t)|^2\,dt.
$$

令 $L=2R$。連續使用兩次 Dirichlet Poincaré inequality 得

$$
\|G\|_{L^2\to L^2}
\le
\frac{L^4}{\pi^4\tau}
<
\frac{L^4}{3^4\tau}
=:
C_G.
$$

結構條件投影是 Hilbert orthogonal projection，不會增加 representer
norm。

axis density 為

$$
f_x(t)=\cos(xt),
\qquad
\partial_xf_x(t)=-t\sin(xt).
$$

故

$$
\|f_x\|_2\le\sqrt{2R},
\qquad
\|\partial_xf_x\|_2
\le
\sqrt{\frac{2R^3}{3}}.
$$

若 $p_x$ 為 projected Green representer，則

$$
\|p_x-p_c\|
\le
|x-c|
\sup_\xi\|\partial_\xi p_\xi\|.
$$

又

$$
\|P_x-P_c\|
\le
\|p_x-p_c\|
\left(\|p_x\|+\|p_c\|\right).
$$

使用

$$
\sqrt3>\frac53
$$

可得精確有理上界

$$
\|P_x-P_c\|
<
\frac{12}{5}R^2C_G|x-c|.
$$

若第 $i$ 個 axis atom 的 operator weight 是 $\lambda_i$，便有

$$
\left\|
\sum_i\lambda_i
\left(P_{x_i}-P_{c_i}\right)
\right\|
\le
\frac{12}{5}R^2C_G
\sum_i\lambda_i|x_i-c_i|.
$$

只要右側小於 $1/21$，所有獨立位置共同保留 positivity。

### 5.2 本輪精確半徑

v0.7 的 $58$ 個 axis weights 精確總和為

$$
\Lambda
=
\frac{10287970888727}{125000000000}.
$$

取 uniform cell half-width

$$
h=
\frac{1}{500000000000000},
$$

本輪的擾動 norm upper bound 為

$$
\varepsilon
=
\frac{
12328822128706060288
}{
299401138693037109375
}
\approx0.0411782740
<
\frac1{21}.
$$

所以

$$
W_1(\mathbf x)
\succeq
\left(\frac1{21}-\varepsilon\right)I
$$

且精確 coercivity lower bound 為

$$
\frac{
13498624663403281109
}{
2095807970851259765625
}
\approx0.00644077361.
$$

這是對 $58$ 個獨立位置量詞共同成立的抽象 clamped-Green family
certificate，但它的 centers 與 weights 仍來自 v0.7 的 dual atoms；
不是實際 $\zeta$ zero occupancy。

## 6. 浮點對抗角點與 proof-budget gap

以 $\Delta t=0.02$ 的 direct Green reconstruction，在 $58$ 個 cell
corners 上做：

1. 中心有限差分 gradient；
2. gradient sign corner；
3. 最多四輪 deterministic coordinate flips。

所得門檻在

$$
h=0.016
$$

時約為

$$
1.00046047,
$$

而在

$$
h=0.017
$$

時約為

$$
0.98805163.
$$

固定角點再用

$$
\Delta t\in\{0.02,0.01,0.005\}
$$

重算，差異小於 $2\times10^{-5}$。

這只是一條 adversarial diagnostic，沒有窮盡 $2^{58}$ corners，更沒有
涵蓋 cell interiors。它不能替代 interval proof。不過

$$
\frac{0.016}{2\times10^{-15}}
=
8\times10^{12}
$$

顯示目前主要損失來自全域 Poincaré bound，而不是已證出算子族在
macroscopic cells 必然失敗。

## 7. 本輪閉合與未閉合

已閉合：

- occupancy selection 的合法 operator transfer；
- scalar count-only 的精確反例；
- exact rational Green cover engine；
- synthetic two-cell universal family；
- conditional $58$-cell clamped微半徑 family。

仍未閉合：

- $\zeta$ 零點的 theorem-backed cell presence certificates；
- local interval clamped-Green derivatives；
- macroscopic cell 的 universal Schur family；
- explicit-formula admissibility 與 prime-side nonnegative cone；
- 全臨界帶與 global RH transfer。

