# Theory

## 1. 三個不同物件

固定 band $A_j$、其中的零點多重集 $\Gamma_j$，以及

$$
H_A(x)=\operatorname{Tr}(P_xA)\ge0.
$$

必須區分：

### 實際零點和

$$
Z_j(A;\Gamma_j)
=
\sum_{\gamma\in\Gamma_j}H_A(\gamma).
$$

### Supremum 上包絡

$$
E_j^{\sup}(A;U_j)
=
U_j\sup_{x\in A_j}H_A(x).
$$

### Infimum 下包絡

$$
E_j^{\inf}(A;L_j)
=
L_j\inf_{x\in A_j}H_A(x).
$$

這三者不能只因係數都是非負數而互換。

## 2. 計數上界定理

若

$$
n_j=|\Gamma_j|\le U_j,
$$

則

$$
\begin{aligned}
Z_j(A;\Gamma_j)
&=
\sum_{\gamma\in\Gamma_j}H_A(\gamma)\\
&\le
n_j\sup_{x\in A_j}H_A(x)\\
&\le
U_j\sup_{x\in A_j}H_A(x).
\end{aligned}
$$

這是 v0.2 的 zero-position-free leakage majorant 所需方向。

## 3. 計數下界定理

若

$$
n_j\ge L_j,
$$

則

$$
\begin{aligned}
Z_j(A;\Gamma_j)
&\ge
n_j\inf_{x\in A_j}H_A(x)\\
&\ge
L_j\inf_{x\in A_j}H_A(x).
\end{aligned}
$$

注意右側是 infimum，不是任意 probability average。

## 4. 任意 measure 轉移的精確反例

令 band 只有兩點 $x_0,x_1$，實際零點多重集為

$$
\Gamma=\{x_0\},
$$

並取

$$
H(x_0)=0,\qquad H(x_1)=1.
$$

此時

$$
n=L=U=1,
$$

但對

$$
\mu=\delta_{x_1},
$$

有

$$
Z(H;\Gamma)=0
<
1
=
L\int H\,d\mu.
$$

所以

$$
n\ge L
$$

不推出

$$
Z(H;\Gamma)\ge L\int H\,d\mu
$$

對任意 $\mu$ 成立。

## 5. Operator 版本

在 $\mathbb R^2$ 取

$$
P_{x_0}
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
P_{x_1}
=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
$$

若 $Q\succeq0$ 且

$$
Q\preceq P_{x_0},
\qquad
Q\preceq P_{x_1},
$$

則

$$
\operatorname{ran}Q
\subseteq
\operatorname{span}(e_1)
\cap
\operatorname{span}(e_2)
=
\{0\}.
$$

故 $Q=0$。這說明只知道「band 中至少有一個零點」時，若位置可任意
移動，通常不存在非零 configuration-independent rank-one operator
共下界。

在 continuous RKHS 中，不同 $p_x\otimes p_x$ 的 range 通常也不共線，
所以同一障礙持續存在。

## 6. Upper-envelope no-go 定理

令

$$
\mathcal E_U(A)
=
\operatorname{Tr}(TA)
+
\sum_jU_js_j,
$$

其中

$$
s_j\ge
\sup_{x\in A_j}\operatorname{Tr}(P_xA).
$$

若 dual witness 證明每個 target-feasible $A$ 都滿足

$$
\mathcal E_U(A)\ge\alpha,
$$

則可推出：

> 在該函數空間與該上包絡規則中，充分條件
> $\mathcal E_U(A)<\alpha$ 沒有可行 witness。

這是一個方法層 no-go theorem。

但即使另有

$$
Z_\Gamma(A)\le\mathcal E_U(A),
$$

也不能反向推出

$$
Z_\Gamma(A)\ge\alpha.
$$

## 7. v0.7 的正確保留方式

v0.7 已 interval-certify 固定 abstract operator

$$
W_{21/20}\succ0.
$$

這個代數命題保留不變。

其 zeta-facing 解讀分成兩條：

1. 若 upper count profiles 與 tail envelope 完成 source theorem
   certification，則可升級為 upper-envelope method no-go；
2. 若要升級為 actual zero-side positive obstruction，必須另有
   location/occupancy operator family，scalar counts 不足。

## 8. Tail coefficient 的雙重方向

若目標是證明 candidate 成功，即

$$
\text{actual tail}\le E_{\mathrm{model}},
$$

模型係數必須是 theorem-backed upper coefficient。

若目標是證明 no-go，且已知真實保守 envelope $E_{\mathrm{true}}$ 的係數
不小於 $E_{\mathrm{small}}$，那麼

$$
E_{\mathrm{small}}(A)\ge\alpha
$$

便推出

$$
E_{\mathrm{true}}(A)\ge\alpha.
$$

所以 v0.7 對 tail scale 向下有理化可能適合 no-go 方向，但仍需對來源
定理做 directed certification。
