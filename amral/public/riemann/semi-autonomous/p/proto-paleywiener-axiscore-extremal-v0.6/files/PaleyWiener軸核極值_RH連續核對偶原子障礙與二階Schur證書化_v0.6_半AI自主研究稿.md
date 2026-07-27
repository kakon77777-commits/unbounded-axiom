# Paley–Wiener 軸核極值

## RH 連續核對偶、原子障礙與二階 Schur 證書化

版本：v0.6  
日期：2026-07-25  
研究模式：半 AI 自主數學研究  
技術研究主導：OpenAI Codex  
研究現場授權與審閱：Neo.K / EveMissLab

## 摘要

本節點承接 v0.5 的 axis-notch co-design。父節點證明：若 notch 只以齊次
constraints 縮小既有 finite Gram space，就不可能改善原空間的 primal
feasibility；外部 spectral lifts 與 27 組 local bump geometries 雖有
$1\%$ 至 $4\%$ 改善，joint safe dual bounds 仍大於 $1$。因此 v0.6
不再尋找另一批字典，而是把問題提升到 compact-support entire functions
的連續 Hilbert-space extremal。

本稿選擇 real-even clamped space

$$
\mathcal H_R^0
\subset H_0^2(-R,R;\mathbb R),
$$

以

$$
\langle\psi,\phi\rangle_T
=\kappa_R\int_{-R}^{R}\psi''(t)\phi''(t)\,dt
$$

作為 tail inner product，並施加

$$
G_\psi(0)=G_\psi(i/2)=0.
$$

有限 multi-test Gram matrix被提升為 $\mathcal H_R^0$ 上的 positive
trace-class operator。實軸 evaluation 產生 positive rank-one operator，
偏軸 evaluation 則產生

$$
C_z=2(u_z\otimes u_z-v_z\otimes v_z),
$$

所以五軸帶 supremum 與核心 negativity 的 dual 自然成為 probability
measures。本文證明：若

$$
I+\sum_jN_j\int P_x\,d\mu_j(x)
+\alpha\int C_z\,d\nu(z)\succeq0,
$$

則 continuous primal value 至少為 $\alpha$。這個 weak-duality obstruction
不需要 strong duality。

本節點另導出一軸點、一核心點 extremal 的 rank-two closed form，並給出
clamped bi-Laplacian Green kernel與結構零點投影。數值部分使用兩條獨立
路徑：

1. nested clamped-even Chebyshev–Galerkin spaces；
2. 直接解 $\kappa_Rk''''=f$ 的 Green ODE solver。

在 simplified point test 中，raw-dimension-192 Galerkin 值與 direct Green
值只差約 $1.05\times10^{-9}$。五帶 joint dual 從 effective dimension
$22$ 時的 $7.7882$ 單調下降，在 dimension $190$ 時到
$1.132475$。更關鍵的是：最後的 58 個軸原子與 2 個核心原子被直接移入
continuous Green RKHS 後，dictionary-independent floating threshold
收斂到

$$
1.1324411997.
$$

在

$$
\alpha_{\rm safe}=1.0662376054
$$

時，continuous-kernel finite-span matrix 的 minimum eigenvalue 約
$0.2568266$。

由於核心測度只有兩個原子，將 60 個 positive directions 吸收後，無限維
PSD 判定等價於一個 $2\times2$ Schur matrix PSD。最後再把 supports、
weights 與 target alpha 有理化，固定

$$
\alpha_\star=\frac{21}{20}=1.05.
$$

此 rational candidate 的 floating Schur minimum 為

$$
0.0698852338.
$$

因此 v0.6 停止 dictionary 與 Galerkin expansion。下一節點只需對顯式
Green-kernel pairings、positive $60\times60$ solve 與 final $2\times2$
Schur matrix 做 interval enclosure。

本節點建立的是 continuous-kernel floating obstruction，不是
interval-certified analytic certificate，更不是 RH 證明或反證。

## 1. 從有限字典障礙到連續問題

### 1.1 v0.5 留下的真正問題

v0.5 的最強結論不是某一組 notch 失敗，而是有限空間內的單調性：

$$
V'\subseteq V
\Longrightarrow
\mathcal F(V')\subseteq\mathcal F(V).
$$

若父 PSD Gram 已搜尋完整 $V$，那麼加入

$$
G(a)=0,\qquad G'(a)=0
$$

只會刪除 directions，不會創造新 feasible point。這迫使研究路線做出
選擇：

- 繼續加入外部 atoms，但無法判斷何時才足夠；
- 或直接定義包含所有 admissible directions 的 continuous space。

v0.6 選擇後者。這不是把數值問題抽象化後逃離計算，而是要回答最核心的
可辨識問題：

> v0.5 的 $\alpha>1$ 是 local bump dictionary 的人工障礙，還是 compact
> support 與 axis/core geometry 本身已在連續空間形成 separation？

### 1.2 為何使用 clamped $H_0^2$

compact support 的 Fourier transform自然進入 Paley–Wiener-type entire
function framework。另一方面，父研究鏈的 tail penalty 由
$\psi''$ quadratic form 控制。因此選擇

$$
H_0^2(-R,R)
$$

有三個直接優點：

1. 以零延拓後保留 value/slope boundary compatibility；
2. $\|\psi''\|_{L^2}$ 在 clamped domain 上是 norm；
3. tail quadratic form 可直接變成 Hilbert identity。

本稿不是宣稱所定義空間等同某個未加權標準 $PW_R^2$。更精確地說，它是
compact-support Sobolev domain 經 Fourier transform所得的
Paley–Wiener-type Hilbert space。

## 2. Continuous tail space

固定 $R=16$。令

$$
\mathcal H_R
=\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t)
\right\}.
$$

clamped traces 為

$$
\psi(\pm R)=\psi'(\pm R)=0.
$$

定義

$$
\langle\psi,\phi\rangle_T
=\kappa_R\int_{-R}^{R}
\psi''(t)\phi''(t)\,dt,
$$

其中 $\kappa_R$ 沿用父研究鏈的 floating tail scale：

$$
\kappa_R=2R\,\tau_R.
$$

由 clamped Poincaré inequality，$\|\psi''\|_2$ 控制
$\|\psi\|_2$ 與 $\|\psi'\|_2$。因此對 fixed $z=x+iy$，

$$
\left|
\int_{-R}^{R}\psi(t)e^{izt}\,dt
\right|
\le
C(R,z)\|\psi\|_{\mathcal H_R}.
$$

所以

$$
G_\psi(z)
=\int_{-R}^{R}\psi(t)e^{izt}\,dt
$$

是 bounded linear functional，並由 compact support 生成 exponential
type 至多 $R$ 的 entire function。

結構零點定義 closed subspace

$$
\mathcal H_R^0
=\left\{
\psi\in\mathcal H_R:
G_\psi(0)=G_\psi(i/2)=0
\right\}.
$$

因 $\psi$ even，

$$
G_\psi(0)=\int_{-R}^{R}\psi(t)\,dt,
$$

$$
G_\psi(i/2)
=\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt.
$$

## 3. Evaluation operators

### 3.1 Real axis

由 Riesz representation，對每個 real $x$ 存在唯一
$p_x\in\mathcal H_R^0$，使

$$
\langle\psi,p_x\rangle_T=G_\psi(x).
$$

令

$$
P_x=p_x\otimes p_x.
$$

則

$$
\langle\psi,P_x\psi\rangle_T
=G_\psi(x)^2\ge0.
$$

### 3.2 Off-axis core

對 $z=x+iy$，even symmetry 給出

$$
\operatorname{Re}G_\psi(z)
=\int_{-R}^{R}
\psi(t)\cos(xt)\cosh(yt)\,dt,
$$

$$
\operatorname{Im}G_\psi(z)
=-\int_{-R}^{R}
\psi(t)\sin(xt)\sinh(yt)\,dt.
$$

令 $u_z,v_z$ 為兩個 real Riesz representers。則

$$
2\operatorname{Re}G_\psi(z)^2
=2\left[
\langle\psi,u_z\rangle_T^2
-\langle\psi,v_z\rangle_T^2
\right].
$$

所以核心 operator 恰為

$$
C_z
=2\left(
u_z\otimes u_z-v_z\otimes v_z
\right).
$$

這個 rank-two identity 是整個 continuous reduction 的核心：偏軸負方向
不是一個大型未知 operator，而只來自 imaginary evaluation representer。

## 4. Positive trace-class primal

有限 PSD Gram matrix可視為 finite-rank positive operator。連續化後考慮

$$
A\succeq0,\qquad
A\in\mathcal S_1(\mathcal H_R^0).
$$

固定五帶

$$
\mathcal A_0=[14,18],\quad
\mathcal A_1=[18,23],\quad
\mathcal A_2=[23,35],
$$

$$
\mathcal A_3=[35,70],\quad
\mathcal A_4=[70,145],
$$

以及 v0.5 困難 patch

$$
\mathcal P
=[20.395,20.42]\times[-0.10625,-0.1].
$$

引入 epigraph variables $s_j$，定義 primal：

$$
\begin{aligned}
\Lambda_R=\inf\quad&
\operatorname{Tr}(A)
+\sum_{j=0}^{4}N_js_j\\
\text{subject to}\quad&
\operatorname{Tr}(P_xA)\le s_j
\quad\forall x\in\mathcal A_j,\\
&
\operatorname{Tr}(C_zA)\le-1
\quad\forall z\in\mathcal P,\\
&A\succeq0.
\end{aligned}
$$

$\operatorname{Tr}(A)$ 就是 tail objective，因為 tail quadratic form 已被
內積化。

## 5. Measure dual weak theorem

令 $\mu_j$ 為 $\mathcal A_j$ 上的 probability measures，$\nu$ 為
$\mathcal P$ 上的 probability measure。假設存在 $\alpha>0$ 使

$$
W_\alpha
=I+\sum_{j=0}^{4}N_j
\int_{\mathcal A_j}P_x\,d\mu_j(x)
+\alpha
\int_{\mathcal P}C_z\,d\nu(z)
\succeq0.
$$

對每個 primal-feasible $A$，

$$
0\le\operatorname{Tr}(W_\alpha A).
$$

又因 probability normalization 與 primal inequalities，

$$
\begin{aligned}
\operatorname{Tr}(W_\alpha A)
&=\operatorname{Tr}(A)
+\sum_jN_j
\int\operatorname{Tr}(P_xA)\,d\mu_j(x)\\
&\quad+\alpha
\int\operatorname{Tr}(C_zA)\,d\nu(z)\\
&\le
\operatorname{Tr}(A)+\sum_jN_js_j-\alpha.
\end{aligned}
$$

因此

$$
\Lambda_R\ge\alpha.
$$

這個定理只使用 weak duality。即使 infinite-dimensional strong duality
尚未建立，一個 dual-feasible witness 仍足以排除
$\Lambda_R<\alpha$。

這也解釋為何 dual axis grid 沒有 v0.4 primal coarse-grid false escape 的
同一問題：一個 atomic $\mu_j$ 在任意合法實軸位置都是真正的 continuous
probability measure；它不需要覆蓋整個 band 才能提供 lower bound。

## 6. 一軸點、一核心點閉式模型

### 6.1 Generalized rank-two eigenvalue

固定 $x,z,N$。令

$$
B=I+Np_x\otimes p_x.
$$

考慮

$$
\inf_{A\succeq0}
\left\{
\operatorname{Tr}(BA):
\operatorname{Tr}(C_zA)\le-1
\right\}.
$$

令

$$
\widehat u=B^{-1/2}u_z,\qquad
\widehat v=B^{-1/2}v_z
$$

及

$$
a=\|\widehat u\|^2,\quad
b=\|\widehat v\|^2,\quad
c=\langle\widehat u,\widehat v\rangle.
$$

因

$$
B^{-1/2}C_zB^{-1/2}
=2\left(
\widehat u\otimes\widehat u
-\widehat v\otimes\widehat v
\right),
$$

其非零 eigenvalues 為

$$
\lambda_\pm
=(a-b)\pm
\sqrt{(a+b)^2-4c^2}.
$$

若 $\lambda_-<0$，最佳 PSD operator 可取 most-negative eigendirection
上的 rank one，因此

$$
\Lambda(x,z;N)
=-\frac1{\lambda_-}.
$$

亦即

$$
\Lambda(x,z;N)
=
\frac1{
\sqrt{(a+b)^2-4c^2}-(a-b)
}.
$$

### 6.2 六個 kernel numbers

Sherman–Morrison 給出

$$
B^{-1}
=I-\frac{N}{1+N\|p_x\|^2}
p_x\otimes p_x.
$$

所以

$$
a
=\|u_z\|^2
-\frac{N\langle p_x,u_z\rangle^2}
{1+N\|p_x\|^2},
$$

$$
b
=\|v_z\|^2
-\frac{N\langle p_x,v_z\rangle^2}
{1+N\|p_x\|^2},
$$

$$
c
=\langle u_z,v_z\rangle
-\frac{
N\langle p_x,u_z\rangle
\langle p_x,v_z\rangle
}{
1+N\|p_x\|^2
}.
$$

因此 simplified problem 完全由

$$
\|p\|^2,\ \|u\|^2,\ \|v\|^2,\
\langle u,v\rangle,\
\langle p,u\rangle,\
\langle p,v\rangle
$$

決定。

### 6.3 數值結論

固定 patch center

$$
z_c=20.4075-0.103125i.
$$

對五帶逐點掃描後，最佳 single-point lower bounds 為

$$
0.111322,\quad
0.261253,\quad
0.111224,\quad
0.111034,\quad
0.111031.
$$

全部低於 $1$。$A_1$ 的確最強，但它單獨不足以產生 obstruction。v0.5
反覆看到的阻擋必須來自多帶聯合，而不是單一 target-near peak。

## 7. Clamped Green kernel

### 7.1 Explicit kernel

令

$$
L=2R,\quad
\xi=s+R,\quad
\eta=t+R,
$$

$$
a=\min(\xi,\eta),\quad
b=\max(\xi,\eta).
$$

對未施加結構零點的 clamped space，

$$
K_{\rm cl}(s,t)
=\frac{
a^2(L-b)^2
\left[3bL-(L+2b)a\right]
}{
6L^3\kappa_R
}.
$$

它在 $s=t$ 前後是 cubic polynomial，前三階匹配到
$K,K',K''$，而第三導數 jump 使

$$
\kappa_R\partial_s^4K_{\rm cl}(s,t)
=\delta_t(s).
$$

兩端滿足

$$
K_{\rm cl}=0,\qquad
\partial_sK_{\rm cl}=0.
$$

### 7.2 Structural projection

令

$$
c_0(t)=1,\qquad
c_1(t)=\cosh(t/2).
$$

以 $k_f$ 表示 density $f$ 的 clamped representer。結構 Gram 為

$$
M_{ij}
=\langle k_{c_i},k_{c_j}\rangle_T.
$$

對任意兩個 densities $f,g$，投影到
$G(0)=G(i/2)=0$ subspace 後，

$$
\Gamma(f,g)
=\langle k_f,k_g\rangle_T
-b_f^\mathsf TM^{-1}b_g,
$$

其中

$$
b_f
=\begin{pmatrix}
\langle k_{c_0},k_f\rangle_T\\
\langle k_{c_1},k_f\rangle_T
\end{pmatrix}.
$$

所以所有 continuous inner products 都被化為顯式 Green integrals與一個
$2\times2$ projection。

### 7.3 Independent ODE evaluation

程式沒有直接建立巨大 Green matrix，而是對 density $f$ 解

$$
\kappa_Rk''''=f.
$$

取左端為 $a=-R$，particular solution 為

$$
k_p(t)
=\frac1{6\kappa_R}
\int_a^t(t-s)^3f(s)\,ds.
$$

再加

$$
c_2(t-a)^2+c_3(t-a)^3
$$

以滿足右端 value/slope zero。integral 由四個 cumulative moments

$$
\int_a^t s^mf(s)\,ds,\qquad m=0,1,2,3
$$

重建。

這條路徑與 Chebyshev–Galerkin 的基底、whitening 與 generalized
eigensolver 不相同，因此可作真正的 cross-check。

## 8. Nested Galerkin convergence

### 8.1 Basis family

令 $u=t/R$，採

$$
\phi_n(t)
=\left(1-u^2\right)^2T_{2n}(u).
$$

window 使 value 與 slope 在兩端為零，even Chebyshev polynomials使空間
nested。每個 raw space 投影兩個 structural rows 後，effective dimension
減 2。

### 8.2 Joint sequence

計算結果：

| effective dimension | raw joint $\alpha$ |
|---:|---:|
| $22$ | $7.788239$ |
| $38$ | $3.679471$ |
| $62$ | $1.588306$ |
| $78$ | $1.300399$ |
| $94$ | $1.184647$ |
| $118$ | $1.159914$ |
| $142$ | $1.139122$ |
| $158$ | $1.133508$ |
| $174$ | $1.132795$ |
| $190$ | $1.132475$ |

這個 sequence 的下降很重要。低維 $\alpha=7.79$ 顯然不是 continuous
結論；空間放大後 primal freedom 增加，dual obstruction 必須下降。到
dimension $174$、$190$ 時下降量開始縮小，但仍不能只靠平台外推。

### 8.3 Point-kernel convergence

在 $x=20.4$、$z=z_c$：

$$
\Lambda_{40}=0.8789952,
$$

$$
\Lambda_{96}=0.2017878,
$$

$$
\Lambda_{160}=0.1135563,
$$

$$
\Lambda_{192}=0.11244168195.
$$

direct Green solver在 $\Delta t=0.0025$ 給出

$$
0.11244168090.
$$

兩者絕對差約

$$
1.05\times10^{-9}.
$$

這顯示 raw dimension 192 已解析 target-near high-frequency direction；
v0.6 後續不必靠盲目增維猜測。

## 9. Atomic transfer to the continuous kernel

### 9.1 Frozen measures

dimension 190 的 optimized measures 有：

$$
22,\ 5,\ 14,\ 9,\ 8
$$

個五帶 axis atoms，合計 58。core measure 只支撐在

$$
(20.395,-0.1),\qquad
(20.42,-0.1),
$$

weights 約為

$$
0.5917914068,\qquad
0.4082085932.
$$

### 9.2 Higher-space reconstruction

不重新最佳化 measures，只把同一 witness 放入更高 Galerkin spaces：

| raw dimension | fixed-measure threshold |
|---:|---:|
| $192$ | $1.13247521$ |
| $208$ | $1.13247311$ |
| $224$ | $1.13246577$ |
| $256$ | $1.13245246$ |
| $288$ | $1.13244239$ |

下降持續但已很小。

### 9.3 Direct Green reconstruction

完全移除 Galerkin dictionary 後：

| time step | direct Green threshold |
|---:|---:|
| $0.02$ | $1.1324314430$ |
| $0.01$ | $1.1324406087$ |
| $0.005$ | $1.1324411657$ |
| $0.0025$ | $1.1324411997$ |

因此 fixed atomic measure 在 continuous Green kernel中的 floating threshold
穩定於

$$
1.1324412.
$$

在

$$
\alpha_{\rm safe}=1.0662376054
$$

時，

$$
\lambda_{\min}(W_{\rm safe})
=0.2568265725.
$$

這已不是某個 finite dictionary 的 PSD，而是顯式 Green pairings所定義的
continuous-kernel finite-rank operator 的 floating PSD。

## 10. Infinite PSD to a $2\times2$ Schur test

### 10.1 Positive and negative directions

對 finite atomic witness，把 58 個 axis vectors 與兩個 core-real vectors
乘上 coefficient/weight square roots後放入 $U$。令兩個 core-imag vectors
放入 $V$。則

$$
W_\alpha
=I+UU^\ast-VV^\ast.
$$

令

$$
B_\alpha=I+UU^\ast\succ0.
$$

則

$$
W_\alpha\succeq0
$$

等價於

$$
I-V^\ast B_\alpha^{-1}V\succeq0.
$$

由 Woodbury identity，

$$
B_\alpha^{-1}
=I-U(I+U^\ast U)^{-1}U^\ast.
$$

因此 final certificate matrix 為

$$
S_\alpha
=I-\left[
V^\ast V
-V^\ast U
(I+U^\ast U)^{-1}
U^\ast V
\right].
$$

注意相鄰 factors 依序相乘；括號內第二項完整地是

$$
V^\ast U(I+U^\ast U)^{-1}U^\ast V.
$$

因 $V$ 只有兩個 columns，

$$
S_\alpha\in\mathbb R^{2\times2}.
$$

### 10.2 Floating Schur margin

在 $\alpha_{\rm safe}$：

$$
S_{\rm safe}
\approx
\begin{pmatrix}
0.42967760&-0.44911051\\
-0.44911051&0.59598368
\end{pmatrix},
$$

且

$$
\lambda_{\min}(S_{\rm safe})
\approx0.05608708.
$$

這個 reduction 比直接 interval-check 一個抽象 infinite operator簡單得多：
v0.7 只需要 enclosure kernel Gram、positive $60\times60$ solve 與最後的
$2\times2$ matrix。

## 11. Rational witness

### 11.1 Why lower alpha

本節點不把 floating optimum $1.13244$ 當作 certification target。選擇

$$
\alpha_\star=\frac{21}{20}=1.05
$$

保留

$$
0.05
$$

的 lower-bound margin，同時增加 PSD buffer。

### 11.2 Exact finite data

每一組 probability weights 轉成 denominator

$$
10^{12}
$$

的 integers，並用 largest-remainder rule 使每組 numerators 精確加總。
axis/core locations 轉成 decimal rationals。兩個 core points 為

$$
\left(\frac{4079}{200},-\frac1{10}\right),
$$

$$
\left(\frac{1021}{50},-\frac1{10}\right).
$$

core weights 為

$$
\frac{591791406771}{10^{12}},
\qquad
\frac{408208593229}{10^{12}}.
$$

### 11.3 Rationalized floating audit

在 $\alpha_\star=1.05$：

$$
\lambda_{\min}(W_{\alpha_\star})
\approx0.3122432495,
$$

$$
\lambda_{\min}(S_{\alpha_\star})
\approx0.0698852338.
$$

time step $0.005\to0.0025$ 時，Schur minimum 的變動約

$$
2.68\times10^{-8}.
$$

這個變動只是實驗性 convergence indicator，不是 directed error bound。

## 12. 研究判定

### 12.1 已解決的問題

v0.6 已回答父節點的主要懷疑：

> obstruction 不是 local bump dictionary 的假象。

證據不是只靠「換了一個更大的 basis 仍失敗」，而是：

1. nested spaces 顯示 obstruction 隨維度下降；
2. point extremal 與 direct Green solver 對到 $10^{-9}$；
3. frozen atomic measures 在更高 dimensions 持續穩定；
4. 同一 measures 在 explicit continuous Green kernel中仍給
   $\alpha>1$；
5. infinite PSD 被精確降為有限 kernel Gram 與 $2\times2$ Schur test。

### 12.2 尚未解決的問題

仍不能把 floating result 寫成 theorem instance，因為：

- Green integrals 未做 directed rounding；
- structural projection 未 interval-enclose；
- positive solve 未 verified；
- tail/count coefficients 未完成 theorem-backed interval transfer；
- $H_0^2$ model 到 zeta explicit-formula admissibility 的完整接口未證明。

### 12.3 Stop decision

因此：

- 停止 notch dictionary search；
- 停止 external lift scaling；
- 停止更多 Galerkin dimensions；
- 不重跑 primal construction；
- 保存 rational 58+2 atomic witness；
- 下一節點固定驗證 $\alpha=21/20$。

## 13. v0.7 證書路徑

下一節點：

`RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7`

工作分兩層。

### 13.1 Layer A：abstract continuous extremal

以 exact rational finite data 與明確 continuous kernel，interval-enclose

$$
S_{21/20}.
$$

目標是證明

$$
\lambda_{\min}(S_{21/20})>0.
$$

一旦完成，continuous weak duality 即給

$$
\Lambda_{16}\ge\frac{21}{20}.
$$

### 13.2 Layer B：zeta-facing coefficients

必須另行驗證：

1. $\kappa_R$ 真的是合法、保守的 tail coefficient；
2. $N_j$ 是帶完整假設的 count lower coefficients；
3. explicit-formula admissible tests與 $\mathcal H_R^0$ domain 的關係；
4. target patch 外所有 leakage regions；
5. local object 到 global RH statement 的全部量詞。

Layer A 是一個重要 analytic obstruction，但不能替代 Layer B。

## 14. Trust boundary

本節點的正式結論是：

> 在指定 clamped $H_0^2$ continuous axis/core model 中，trace-class primal
> 具有 probability-measure weak dual；一軸點、一核心點模型可精確降為
> rank two。nested Galerkin 與獨立 Green solver 一致顯示，一個 58-axis、
> 2-core atomic measure 的 continuous-kernel floating threshold 為
> $1.1324412$。將資料有理化並固定 $\alpha=21/20$ 後，continuous PSD
> 可精確降為 $2\times2$ Schur certificate，其 floating minimum 為
> $0.0698852$。因此下一步應做 interval certification，而非繼續擴大
> dictionary。

不能由本節點推出：

- interval-certified continuous obstruction 已完成；
- 所有 RH test-function architectures 都不可行；
- target patch 中存在 zeta zero；
- 未知偏軸零點的 global budget 已閉合；
- RH 成立或不成立。

這一輪完成的是「從有限字典探索到可區間化連續核證書」的轉換，而不是 RH
終局。
