# Theory

## 1. 抽象連續空間

固定 $R=16$ 與

$$
\kappa=
\frac{31794183142988}{10^{18}}>0.
$$

令

$$
\mathcal H=
\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t),\
\int_{-R}^{R}\psi(t)\,dt=0,\
\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt=0
\right\},
$$

配備

$$
\langle\psi,\phi\rangle_{\mathcal H}
=
\kappa\int_{-R}^{R}\psi''(t)\phi''(t)\,dt.
$$

對 rational $x,y$ 定義三種 real-even densities：

$$
p_x(t)=\cos(xt),
$$

$$
u_{x,y}(t)=\cos(xt)\cosh(yt),
$$

$$
v_{x,y}(t)=-\sin(xt)\sinh(yt).
$$

它們分別對應 axis evaluation 與

$$
G_\psi(x+iy)
=
\langle\psi,u_{x,y}\rangle_{L^2}
+i\langle\psi,v_{x,y}\rangle_{L^2}.
$$

## 2. Clamped Green representer

若 density 為 $e^{bt}$ 且 $b\neq0$，其未投影 representer 可寫成

$$
r_b(t)=\frac{e^{bt}}{\kappa b^4}+P_b(t),
$$

其中 $P_b\in\mathbb P_3$ 唯一滿足

$$
r_b(-R)=r_b'(-R)=r_b(R)=r_b'(R)=0.
$$

若 $b=0$，則

$$
r_0(t)=\frac{(t^2-R^2)^2}{24\kappa}.
$$

因此 exponential pairing

$$
\Gamma(a,b)
=
\int_{-R}^{R}e^{at}r_b(t)\,dt
$$

只需要指數矩

$$
I_n(a)=\int_{-R}^{R}t^n e^{at}\,dt.
$$

當 $a\neq0$ 時，

$$
I_0(a)=\frac{e^{aR}-e^{-aR}}{a},
$$

且

$$
I_n(a)
=
\frac{R^n e^{aR}-(-R)^n e^{-aR}}{a}
-\frac{n}{a}I_{n-1}(a).
$$

當 $a=0$ 時，

$$
I_n(0)=
\begin{cases}
0,&n\text{ 為奇數},\\
\dfrac{2R^{n+1}}{n+1},&n\text{ 為偶數}.
\end{cases}
$$

所有 axis、core 與 structural densities 都是有限個 rational complex
exponentials 的線性組合，所以每一個未投影 pairing 都能由上述遞迴
有限計算。

## 3. 結構約束投影

令

$$
c_0(t)=1,\qquad c_1(t)=\cosh(t/2),
$$

以及 structural Gram

$$
M_{ab}=\Gamma(c_a,c_b).
$$

對任意 densities $f,g$，限制到 $\mathcal H$ 後的 reproducing
pairing 為

$$
\Gamma_0(f,g)
=
\Gamma(f,g)
-\mathbf c(f)^\mathsf T
M^{-1}
\mathbf c(g),
$$

其中

$$
\mathbf c(f)=
\begin{pmatrix}
\Gamma(c_0,f)\\
\Gamma(c_1,f)
\end{pmatrix}.
$$

本套件直接區間證明

$$
\inf\det M
>
6.087163164690596\times10^{20},
$$

所以投影公式在整個 enclosure 上都有定義。

## 4. 有限秩 operator

令 $F$ 的 $60$ 個 columns 為：

- $58$ 個 axis representers；
- $2$ 個 core-real representers。

令 $V$ 的 $2$ 個 columns 為 core-imag representers。正負 rational
weights 分別置於 diagonal matrices $D$ 與 $B$。固定

$$
\alpha_\star=\frac{21}{20}
$$

已經吸收到 core weights 中。

定義

$$
K_+=I+FDF^\ast,
$$

以及

$$
W=K_+-VBV^\ast.
$$

設

$$
G=F^\ast F,\qquad
C=F^\ast V,\qquad
H=V^\ast V.
$$

由 Woodbury identity，

$$
K_+^{-1}
=
I-FD(I+GD)^{-1}F^\ast.
$$

因此

$$
Q
=
V^\ast K_+^{-1}V
=
H-C^\mathsf T D(I+GD)^{-1}C.
$$

由正定 Schur complement，

$$
W\succ0
\quad\Longleftrightarrow\quad
T:=B^{-1}-Q\succ0.
$$

所以無限維 operator 的最後判定只剩 $2\times2$。

## 5. Verified Neumann solve

令

$$
A=I+GD.
$$

套件保存一個 finite-decimal rational matrix $\mathcal R$ 作為
$A^{-1}$ 的候選。對整個 interval matrix family 驗證

$$
E=I-\mathcal R A,
$$

以及

$$
\|E\|_\infty
\leq
7.531404753645390\times10^{-15}
<1.
$$

因此每個 $A$ 都可逆。

對保存的 rational approximate solution $X_0$，令

$$
\rho
=
\mathcal R(C-AX_0).
$$

則真解 $X=A^{-1}C$ 滿足

$$
\|X-X_0\|_\infty
\leq
\frac{\|\rho\|_\infty}{1-\|E\|_\infty}.
$$

兩個 right-hand sides 的 componentwise radii 上界分別約為

$$
6.47914\times10^{-16}
$$

與

$$
2.88127\times10^{-16}.
$$

## 6. 最後 Sylvester 判定

最終 interval matrix 為

$$
T\subset
\begin{pmatrix}
[0.3524279496453903,\ 0.3524279496454152]
&
[-0.4286502909903863,\ -0.4286502909903751]
\\
[-0.4286502909903863,\ -0.4286502909903751]
&
[0.7018637127810353,\ 0.7018637127810464]
\end{pmatrix}.
$$

directed arithmetic 給出

$$
\inf T_{11}
>
0.3524279496453903,
$$

與

$$
\inf\det T
>
0.0636153172597786.
$$

由 $2\times2$ Sylvester criterion，

$$
T\succ0,
$$

進而

$$
W_{21/20}\succ0.
$$

## 7. 定理的精確範圍

上述結論是一個 abstract continuous interval theorem。它使用固定的
rational $\kappa$ 與五個 rational band coefficients 作為模型定義。

它沒有證明：

- 這五個 coefficients 是 zeta zero-side 正貢獻的合法下界；
- $\kappa$ 已由來源定理保證低於實際 tail coefficient；
- clamped closure 已滿足顯式公式的全部 admissibility；
- 任一偏軸零點存在；
- RH 的全域量詞已閉合。
