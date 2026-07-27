# 區間 Green 核原子證書：RH 抽象連續障礙的有理包絡與二階 Sylvester 判定

版本：v0.7  
日期：2026-07-25  
研究型態：半 AI 自主數學研究內部稿  
節點：`RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7`

## 摘要

本文延續 v0.6 的 Paley–Wiener 軸核極值研究。上一節點已將有限
Chebyshev–Galerkin 現象轉移到 continuous clamped Green RKHS，並找到
一組由 $58$ 個 axis atoms 與 $2$ 個 core atoms 構成的 rationalized
atomic dual witness。在普通浮點重建中，固定 witness 的 threshold 約為

$$
1.13244120,
$$

而在安全目標

$$
\alpha_\star=\frac{21}{20}=1.05
$$

下，最後 $2\times2$ Schur matrix 的最小特徵值約為

$$
0.06988523.
$$

然而浮點正裕量不是證書。本文以 $90$ 位 directed-decimal interval
arithmetic 重新建立：

1. $\pi$、指數、三角與雙曲函數包絡；
2. clamped $D^4$ Green representer 的 closed-form pairings；
3. 兩個 structural zeros 的 interval projection；
4. $60\times60$ positive system family 的 Neumann regularity；
5. 兩個 right-hand sides 的 verified solution enclosure；
6. 最後 $2\times2$ matrix 的 Sylvester positivity。

所得 rigorous bounds 為

$$
\left\|I-\mathcal R A\right\|_\infty
\leq
7.531404753645390\times10^{-15},
$$

$$
\inf T_{11}
>
0.3524279496453903,
$$

以及

$$
\inf\det T
>
0.0636153172597786.
$$

因此，對本文明確定義的 rational abstract continuous model，

$$
W_{21/20}\succ0.
$$

這是研究鏈第一次完成 dictionary-independent、time-grid-independent、
directed-rounding continuous atomic certificate。

但本文同時發現更重要的 zeta-facing 阻塞：父節點五個正向 band
coefficients 是 zero-count upper profiles，而不是目前 $|S(T)|$ bound
能保證的 lower profiles。把一個 upper bound 向下取整，並不會把它變成
lower bound。故本文的區間證書只完成 Layer A，不構成 RH 證明、反證或
實際 zeta zero-region exclusion。

## 一、研究問題的轉變

### 1. 從最佳化轉向合法化

早期節點的核心問題是：

> 能否找到一組測試函數，使某個偏軸 core contribution 被 axis 與 tail
> positivity 阻擋？

到了 v0.6，答案在 floating continuous model 中已經是肯定的。繼續擴張
Galerkin dimension 或搜尋更多 atoms，只會增加數值資料，不會提升命題的
認識論等級。

因此 v0.7 停止最佳化

$$
\alpha
$$

並固定

$$
\alpha_\star=\frac{21}{20}.
$$

本輪唯一主要目標是：

> 證明固定 rational atomic witness 在完整連續 Green model 中確實正定，
> 而非僅在某個離散近似中看似正定。

### 2. 兩層證書

本文沿用兩層區分：

#### Layer A：abstract continuous extremal

把 radius、tail scale、band coefficients、atoms 與 weights 全部視為
明確的 rational model data，證明其 operator positivity。

#### Layer B：zeta-facing theorem transfer

另行證明：

- tail coefficient 的來源定理與單調方向；
- band coefficients 的零點計數語義與上下界方向；
- test-function class 對顯式公式的 admissibility；
- prime-side 與 zero-side 的完整轉移。

Layer A 成功，不會邏輯上自動完成 Layer B。

## 二、連續 Hilbert 模型

### 1. 空間

固定

$$
R=16
$$

與 rational tail scale

$$
\kappa
=
\frac{31794183142988}{10^{18}}.
$$

定義

$$
\mathcal H=
\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t),\
\int_{-R}^{R}\psi(t)\,dt=0,\
\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt=0
\right\}.
$$

內積為

$$
\langle\psi,\phi\rangle_{\mathcal H}
=
\kappa
\int_{-R}^{R}
\psi''(t)\phi''(t)\,dt.
$$

clamped boundary conditions 是

$$
\psi(-R)=\psi'(-R)=\psi(R)=\psi'(R)=0.
$$

Paley–Wiener compact-support framework 提供 entire Fourier transform
的背景；reproducing-kernel representers 則置於 Aronszajn 的標準 RKHS
語境。本文並不宣稱此空間已等同某個特定 de Branges space。

### 2. Evaluation densities

對 axis point $x\in\mathbb R$，

$$
p_x(t)=\cos(xt).
$$

對 core point $z=x+iy$，real-even domain 上的 real 與 imaginary
evaluation densities 為

$$
u_{x,y}(t)
=
\cos(xt)\cosh(yt),
$$

$$
v_{x,y}(t)
=
-\sin(xt)\sinh(yt).
$$

因此

$$
G_\psi(x+iy)
=
\int_{-R}^{R}\psi(t)u_{x,y}(t)\,dt
+i
\int_{-R}^{R}\psi(t)v_{x,y}(t)\,dt.
$$

### 3. 固定 atomic witness

五帶 axis measures 各自是 probability measure。所有權重以 denominator

$$
10^{12}
$$

精確序列化，且每帶 numerators 的總和精確等於 denominator。core
measure 亦然。

固定 operator 可寫成

$$
W_\alpha
=
I
+\sum_{j=0}^{4}
N_j
\sum_{k}
\mu_{jk}\,
p_{x_{jk}}\otimes p_{x_{jk}}
+2\alpha
\sum_{\ell}
\nu_\ell
\left(
u_\ell\otimes u_\ell
-v_\ell\otimes v_\ell
\right).
$$

本文在

$$
\alpha=\frac{21}{20}
$$

下判定它。

## 三、從 Green kernel 到有限 exponential calculus

### 1. 為什麼不直接包住網格誤差

v0.6 的 direct Green solver 使用 time-grid trapezoid integration。其收斂
表現很好，但若要把它改成真正 rigorous quadrature，就必須同時控制：

- 高頻 trigonometric derivatives；
- cumulative ODE integration error；
- structural projection cancellation；
- $62\times62$ pairings 的一致誤差。

這不是不可能，但證書會龐大且難審。

更好的做法是利用所有 densities 都是有限 exponential sums。

### 2. Exponential decomposition

例如

$$
\cos(xt)
=
\frac12e^{ixt}
+\frac12e^{-ixt}.
$$

而

$$
\cos(xt)\cosh(yt)
$$

是四個

$$
e^{(\pm y\pm ix)t}
$$

的 rational linear combination。相同地，

$$
-\sin(xt)\sinh(yt)
$$

也是四個 exponential terms 的 rational complex linear combination。

因此只需處理一般 density

$$
e^{bt}.
$$

### 3. Clamped representer

representer $r_b$ 滿足

$$
\kappa r_b^{(4)}(t)=e^{bt}
$$

與四個 clamped conditions。

若 $b\neq0$，取 particular solution

$$
\frac{e^{bt}}{\kappa b^4}.
$$

再加入唯一的 cubic polynomial $P_b$ 消去兩端 value 與 slope：

$$
r_b(t)
=
\frac{e^{bt}}{\kappa b^4}
+P_b(t).
$$

若 $b=0$，則閉式解是

$$
r_0(t)
=
\frac{(t^2-R^2)^2}{24\kappa}.
$$

### 4. Moment recurrence

令

$$
I_n(a)
=
\int_{-R}^{R}
t^n e^{at}\,dt.
$$

當 $a\neq0$，

$$
I_0(a)
=
\frac{e^{aR}-e^{-aR}}{a},
$$

以及

$$
I_n(a)
=
\frac{R^n e^{aR}-(-R)^n e^{-aR}}{a}
-\frac{n}{a}I_{n-1}(a).
$$

當 $a=0$，moments 是 exact rationals。故每個 Green pairing

$$
\Gamma(a,b)
=
\int_{-R}^{R}
e^{at}r_b(t)\,dt
$$

只需要有限次有理運算與 endpoint exponentials。

### 5. 自伴對稱的雙向檢查

Green operator 自伴，故

$$
\Gamma(a,b)=\Gamma(b,a).
$$

程式分別以 $b$ 作 source 與以 $a$ 作 source 計算兩個 interval，然後
取交集。若兩者不重疊，計算立即停止。這不是普通的 symmetry
post-processing，而是對兩種 boundary correction formula paths 的
交叉檢查。

## 四、超越函數的 directed enclosure

### 1. 不依賴外部 interval package

執行環境沒有預裝 Arb 或 FLINT。本文沒有退回普通 arbitrary-precision
floating point，而是使用 Python `Decimal` 的 directed contexts：

- lower endpoint 朝 $-\infty$；
- upper endpoint 朝 $+\infty$；
- precision 固定為 $90$ 位。

### 2. $\pi$ 的有理包絡

使用

$$
\pi
=
16\arctan\left(\frac15\right)
-4\arctan\left(\frac1{239}\right).
$$

對

$$
\arctan x
=
\sum_{n=0}^{\infty}
\frac{(-1)^n x^{2n+1}}{2n+1}
$$

使用 alternating remainder theorem。兩個級數分別取 $96$ 與 $40$
項，產生 width

$$
10^{-89}
$$

的 $\pi$ interval。

### 3. 三角函數

對 rational angle $\theta$，選整數 $k$ 並令

$$
r=\theta-k\frac{\pi}{2}.
$$

程式驗證整個 $r$ interval 的絕對值小於 $0.8$。在此區域用 $44$ 項
Taylor polynomial 與 Lagrange remainder enclosure $\sin r$ 與
$\cos r$，再依 $k$ 的模 $4$ 類回復象限。

### 4. 實指數

對 $e^x$ 先將 argument 除以 $2^m$，直到

$$
\left|\frac{x}{2^m}\right|
\leq
\frac1{16}.
$$

在 reduced interval 使用 $48$ 項 Taylor polynomial，並以

$$
e^{|\xi|}<2
$$

給出 remainder bound；最後反覆 interval squaring。

### 5. 包絡寬度

完整 projected Gram 的最大 interval width 為

$$
3.71216\times10^{-84}.
$$

這個寬度遠小於後續 Neumann 與 Sylvester margins。

## 五、Structural-zero projection

令

$$
c_0(t)=1,
\qquad
c_1(t)=\cosh(t/2).
$$

未約束 Green Gram 為

$$
M=
\begin{pmatrix}
\Gamma(c_0,c_0)&\Gamma(c_0,c_1)\\
\Gamma(c_1,c_0)&\Gamma(c_1,c_1)
\end{pmatrix}.
$$

對任意 densities $f,g$，約束子空間的 pairing 為

$$
\Gamma_0(f,g)
=
\Gamma(f,g)
-\mathbf c(f)^\mathsf T
M^{-1}
\mathbf c(g).
$$

本輪證明

$$
\inf\det M
>
6.087163164690596\times10^{20}.
$$

故整個 structural inverse interval 合法。這一步關閉 v0.6 的
structural projection gap。

## 六、從無限維 operator 到 $2\times2$

### 1. 正負因子

將 $58$ 個 axis representers 與 $2$ 個 core-real representers 組成
$F$。將 $2$ 個 core-imag representers 組成 $V$。

正負 weights 分別置入 $D$ 與 $B$。則

$$
K_+=I+FDF^\ast,
$$

$$
W=K_+-VBV^\ast.
$$

因 $D\succ0$，

$$
K_+\succ0.
$$

### 2. 無平方根公式

設

$$
G=F^\ast F,\qquad
C=F^\ast V,\qquad
H=V^\ast V.
$$

令

$$
A=I+GD.
$$

Woodbury identity 給出

$$
K_+^{-1}
=
I-FD A^{-1}F^\ast.
$$

故

$$
Q
=
V^\ast K_+^{-1}V
=
H-C^\mathsf T D A^{-1}C.
$$

原先可使用

$$
I-B^{1/2}QB^{1/2}
$$

作 Schur matrix，但這會額外引入 square-root intervals。本文改用 congruent
matrix

$$
T=B^{-1}-Q.
$$

由

$$
B^{1/2}TB^{1/2}
=
I-B^{1/2}QB^{1/2},
$$

可知

$$
W\succ0
\quad\Longleftrightarrow\quad
T\succ0.
$$

## 七、Verified Neumann solve

### 1. Candidate 不是證明

先用普通 NumPy 產生 $A^{-1}$ 的 approximate candidate，再把每一個 entry
序列化為 finite decimal rational，記為 $\mathcal R$。

證明階段完全不信任原浮點 inverse，而是重新計算

$$
E=I-\mathcal R\mathbf A,
$$

其中 $\mathbf A$ 是完整 interval matrix family。

### 2. Regularity

directed row-sum norm 給出

$$
\|E\|_\infty
\leq
7.5314047536453899529795284724
\times10^{-15}.
$$

因為此值嚴格小於 $1$，Neumann series 證明每個

$$
A\in\mathbf A
$$

皆可逆。

### 3. Solution enclosure

對保存的 approximate solution $X_0$，

$$
\rho
=
\mathcal R(C-AX_0).
$$

真解滿足

$$
X-X_0
=
(I-E)^{-1}\rho.
$$

故

$$
\|X-X_0\|_\infty
\leq
\frac{\|\rho\|_\infty}{1-\|E\|_\infty}.
$$

兩個 columns 的 componentwise radius upper bounds 為

$$
6.479135069600651\times10^{-16}
$$

與

$$
2.881263499141683\times10^{-16}.
$$

## 八、最終 Sylvester 證書

計算得到

$$
T_{11}
\in
[
0.3524279496453903261,\
0.3524279496454151611
],
$$

$$
T_{12}=T_{21}
\in
[
-0.4286502909903862159,\
-0.4286502909903751717
],
$$

$$
T_{22}
\in
[
0.7018637127810353025,\
0.7018637127810463962
].
$$

並且

$$
\det T
\in
[
0.0636153172597786300,\
0.0636153172598094386
].
$$

因此

$$
\inf T_{11}>0
$$

且

$$
\inf\det T>0.
$$

由 $2\times2$ Sylvester criterion，

$$
T\succ0.
$$

最終得到本文主定理：

> 對保存的 rational atoms、weights、tail scale 與 band coefficients，
> 在 real-even clamped structural-zero continuous Hilbert model 中，
> $W_{21/20}$ 嚴格正定。

配合父節點的 abstract weak duality，可在同一抽象模型中推出

$$
\Lambda_{16}
\geq
\frac{21}{20}
>
1.
$$

## 九、驗證架構

### 1. 完整重算

`verify_certificate.py` 從磁碟讀回 witness 與 certificate，重新建立：

- $\pi$ interval；
- exponential and trigonometric enclosures；
- all Green pairings；
- structural projection；
- projected Gram hash；
- Neumann proof；
- final Sylvester proof。

所有 checks 皆為 true。

### 2. 精確序列化審計

`audit_certificate.py` 把 finite decimal endpoints 轉成 exact `Fraction`，
再次驗證：

$$
0\leq q<1,
$$

$$
\inf T_{11}>0,
$$

$$
\inf\det T>0,
$$

所有 probability sums，以及全部 trust-boundary flags。

### 3. Failure injection

測試將 inverse candidate 改成零矩陣。此時

$$
\left\|I-\mathcal R A\right\|_\infty=1,
$$

驗證器正確拒絕該 candidate。

### 4. 與 v0.6 的交叉比對

將新 interval midpoint 轉回 v0.6 的 scaled Schur convention，得到

$$
\lambda_{\min}
\approx
0.06988523568969546.
$$

v0.6 最細 time-grid 值為

$$
0.06988523379762435.
$$

兩者相差約

$$
1.8921\times10^{-9}.
$$

此結果支持兩條獨立路徑一致，但不參與 rigorous proof。

## 十、Coefficient orientation audit

### 1. 意外發現

完成 Layer A 後，下一個自然步驟原本是把五個 band coefficients 的來源
定理也區間化。然而審查父節點 code 時發現，函數名稱已明確稱為
`count_majorant`，而公式也確實是 upper-count profile。

對 band $[a,b]$，在標準 endpoint convention 下，

$$
N(b)-N(a)
=
\frac{\theta(b)-\theta(a)}{\pi}
+S(b)-S(a).
$$

Trudgian 的 inherited bound 是

$$
|S(T)|
\leq
B(T)
:=
0.112\log T
+0.278\log\log T
+2.510
$$

對 $T\geq e$。

所以由此資料直接得到的 lower 與 upper profiles 分別是

$$
L_{a,b}
=
\max\left(
0,\
\frac{\theta(b)-\theta(a)}{\pi}
-B(a)-B(b)
\right),
$$

以及

$$
U_{a,b}
=
\max\left(
0,\
\frac{\theta(b)-\theta(a)}{\pi}
+B(a)+B(b)
\right).
$$

### 2. 五帶比較

既有 coefficients 為：

| band | stored | direct lower from $|S|$ | classification |
|---|---:|---:|---|
| $[14,18]$ | $6.797423271048$ | $0$ | upper profile |
| $[18,23]$ | $7.246636980606$ | $0$ | upper profile |
| $[23,35]$ | $9.346770522330$ | $0$ | upper profile |
| $[35,70]$ | $18.367573606596$ | $5.069962795569$ | upper profile |
| $[70,145]$ | $40.545362729236$ | $26.742367141539$ | upper profile |

五個 stored values 全部貼著 $U_{a,b}$ 的 downward-rounded values，且
沒有一個被目前 $L_{a,b}$ 保證。

### 3. 為什麼這不是小誤差

若一個正半定 axis operator 以

$$
+N_jP_j
$$

進入 witness，則 operator 對 $N_j$ 單調遞增。要保證真實 operator
不小於 certified operator，通常需要

$$
N_j^{\mathrm{cert}}
\leq
N_j^{\mathrm{true}}.
$$

upper majorant 的方向相反。

把

$$
U_j
$$

向下取到十二位小數，只能得到略低於 $U_j$ 的數，不能推出它低於真實
count。

### 4. Stress test

為量化問題，保留整個 witness 幾何，只把五個 coefficients 換成
$L_j$。所得 floating Schur eigenvalues 約為

$$
-5.53605304212116
$$

與

$$
0.942631731149592.
$$

所以固定 witness 不會在這個 lower profile 下存活。

這個 stress test 不證明其他 atoms 或其他 measures 也必然失敗；它只
證明不能把 v0.7 的 abstract certificate 直接貼到目前的 zeta count
argument 上。

## 十一、研究判斷與下一節點

### 1. v0.7 真正完成了什麼

本文關閉：

- finite dictionary ambiguity；
- time-grid ambiguity；
- floating Green pairing ambiguity；
- unverified structural inverse；
- unverified $60\times60$ solve；
- floating $2\times2$ eigenvalue sign。

這是一個實質進步。抽象模型內的 obstruction 現在是 theorem object，
而非 numerical suggestion。

### 2. v0.7 沒有完成什麼

本文沒有完成：

- zeta zero-count coefficient legitimacy；
- tail coefficient theorem transfer；
- explicit-formula admissibility；
- prime-side directed cone；
- zero presence；
- cover family；
- global RH closure。

### 3. v0.8 的正確方向

下一節點改為

`RH-RobustBandCounts-ZetaBridge-20260725-v0.8`。

首先重建原不等式，確認 count majorant 究竟應位於 positive term、
negative budget 還是 normalization。若 positive term 需要 lower
counts，則建立

$$
N_j\in[L_j,U_j]
$$

的 robust coefficient polytope，並在 worst-case vector

$$
L=(L_0,\ldots,L_4)
$$

重新最佳化。

由於前 $3$ 帶僅靠現有 $|S|$ bound 得到的 lower endpoints 為 $0$，
v0.8 可能必須加入：

- interval argument-principle counts；
- Turing method certificates；
- validated zero presence；
- 或不依賴前 $3$ 帶的全新 robust witness。

### 4. 何時回到覆蓋式證書族

原先的長期方向仍然正確：

$$
\text{分帶}
\;+\;
\text{多測試函數}
\;+\;
\text{覆蓋式證書族}.
$$

但順序必須是：

$$
\text{single-patch abstract certificate}
\to
\text{coefficient semantics}
\to
\text{robust zeta-facing certificate}
\to
\text{cover family}.
$$

否則只會把一個未合法化的 coefficient orientation 大規模複製到更多
patches。

## 十二、結論

本輪得到一個雙重結論。

第一，固定 rational model 的 continuous atomic obstruction 已被真正
區間化：

$$
W_{21/20}\succ0.
$$

第二，這個成功沒有掩蓋下一個錯誤，反而使 coefficient direction 的
問題更清楚。數值上最困難的 Green／Schur 部分已經合法；現在阻塞點轉移
到 theorem semantics：

$$
\text{一個係數是上界還是下界，}
$$

比多保留幾十位小數更重要。

因此本文既不是 RH 證明，也不是研究失敗。它把「連續核證書是否存在」
變成肯定答案，同時把「該證書能否進入 zeta」精確縮約為下一輪可檢驗的
係數方向與零點計數問題。

## 參考資料

1. R. E. A. C. Paley and N. Wiener,
   *Fourier Transforms in the Complex Domain*,
   AMS Colloquium Publications $19$,
   <https://bookstore.ams.org/coll-19>.
2. N. Aronszajn,
   “Theory of Reproducing Kernels,”
   *Transactions of the American Mathematical Society* $68$,
   DOI `10.1090/S0002-9947-1950-0051437-7`,
   <https://doi.org/10.1090/S0002-9947-1950-0051437-7>.
3. T. S. Trudgian,
   “An improved upper bound for the argument of the Riemann zeta-function
   on the critical line II,”
   *Journal of Number Theory* $134$, $2014$,
   DOI `10.1016/j.jnt.2013.07.017`,
   <https://openresearch-repository.anu.edu.au/items/2484efc1-7e1b-4a99-821a-ffb0bcbe5697>.
4. Python documentation, `decimal` fixed-point and floating-point arithmetic,
   <https://docs.python.org/3.11/library/decimal.html>.

## 附錄：證書狀態

- `abstract_continuous_interval_certificate = true`
- `abstract_operator_strictly_positive = true`
- `zeta_facing_tail_theorem_certified = false`
- `zeta_facing_count_coefficients_certified = false`
- `explicit_formula_admissibility_certified = false`
- `global_rh_certificate = false`

