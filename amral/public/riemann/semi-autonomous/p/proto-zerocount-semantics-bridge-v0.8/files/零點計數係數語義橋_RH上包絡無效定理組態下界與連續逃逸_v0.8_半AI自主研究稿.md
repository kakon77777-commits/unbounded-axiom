# 零點計數係數語義橋

## RH 上包絡無效定理、組態下界與 continuous lower-profile 逃逸

版本：v0.8  
日期：2026-07-25  
研究模式：半 AI 自主數學研究  
技術研究主導與本輪判斷：OpenAI Codex  
研究場域、交接與審閱位置：Neo.K / EveMissLab

## 摘要

v0.7 已完成一張嚴格的 continuous Green-kernel interval certificate：
在固定 rational band coefficients、$58$ 個 axis atoms、$2$ 個 core
atoms 與

$$
\alpha=\frac{21}{20}
$$

下，abstract operator 嚴格正定。該節點同時發現五個 band coefficients
來自 zero-count upper profiles，而非由 inherited absolute-$S$ bound
直接給出的 lower profiles。

本節點原定任務是把上界改成下界、重新最佳化，再尋找 robust witness。
追溯 v0.1–v0.7 的原始不等式後，得到一個更根本的修正：

> 問題不只在 upper 與 lower 的方向；scalar count bound 與
> zero-location operator mass 是不同型別。

對 band $A_j$、其中零點多重集 $\Gamma_j$ 與非負函數

$$
H_A(x)=\operatorname{Tr}(P_xA),
$$

count upper $U_j$ 合法給出

$$
\sum_{\gamma\in\Gamma_j}H_A(\gamma)
\le
U_j\sup_{x\in A_j}H_A(x).
$$

因此 v0.2–v0.7 的 upper coefficients 並非無效；它們合法定義一個
保守的 zero-position-free leakage envelope。對該 envelope 的 dual
lower bound 可以證明「這個充分上界方法在所選函數空間內無法閉合」，
也就是 method-level no-go theorem。

但 count lower $L_j$ 無條件只給出

$$
\sum_{\gamma\in\Gamma_j}H_A(\gamma)
\ge
L_j\inf_{x\in A_j}H_A(x).
$$

它不能改寫為

$$
L_j\int H_A\,d\mu_j
$$

對任意 dual probability measure $\mu_j$ 的下界。本節點以 exact
two-point countermodel 證明該命題一般為假，並以兩個不共線 rank-one
operators 證明 count-only configuration 通常沒有非零共同 PSD floor。

數值方面，本節點仍完成原定 robust stress test。採用 floating
lower candidate profile

$$
(0,0,0,5.069962795568,26.742367141539)
$$

重新最佳化後，joint-dual threshold 從 effective dimension $22$ 的

$$
2.6662663794
$$

下降至 dimension $190$ 的

$$
0.1297047862.
$$

把最後 measures 直接移入 clamped Green RKHS，$\Delta t=0.005$ 的
fixed-measure threshold 為

$$
0.1297031276.
$$

同一 minimum generalized direction 在 $101\times101$ core grid
與 axis step $0.01$ 下給出 sampled primal objective

$$
0.1297069814<1.
$$

因此 lower-profile robust obstruction 不存在於目前高維診斷；低維
$\alpha>1$ 是 Galerkin truncation effect。

本節點保留 v0.7 的 abstract interval theorem，但把 zeta-facing 路徑
拆成兩條：其一是完成 upper-envelope method no-go 的來源定理；其二是
建立帶位置、cell occupancy 與 universal operator-family 量詞的真正
zero-side certificate。scalar $[L_j,U_j]$ 不再被允許跨越這兩條路。

此外，prototype patch 的高度約為 $20.4$。Platt–Trudgian 已以嚴格
interval computation 驗證 RH 至 $3\cdot10^{12}$，所以此 patch 只能
作幾何與算子校準件，不是未決的實際 $\zeta$ 偏軸目標。

本文不是 RH 證明或反證。

## 一、為何本輪必須先停下最佳化

### 1. v0.7 留下的表面問題

v0.7 的五個 stored coefficients 為

$$
\begin{aligned}
&6.797423271048,\\
&7.246636980606,\\
&9.346770522330,\\
&18.367573606596,\\
&40.545362729236.
\end{aligned}
$$

它們符合 inherited $|S(T)|$ profile 所產生的 upper count values。
若把同一計算改用 lower profile，前三帶係數歸零，後兩帶只剩

$$
5.069962795568881
$$

與

$$
26.74236714153946.
$$

固定 v0.7 witness 在這個 substitution 下失去正定性。因此最直接的
下一步看似是重新最佳化 measures。

### 2. 重新追溯原始目標

然而 v0.2 的 primal objective 並不是實際零點和。它是

$$
\mathcal E_U(A)
=
\langle T,A\rangle
+
\sum_jU_j
\sup_{x\in A_j}H_A(x),
$$

用來 upper-bound unknown critical-line leakage 的 conservative
envelope。

v0.3 的 dual witness 證明的是：

$$
\mathcal E_U(A)\ge\alpha
$$

對所有 finite target-feasible $A$ 成立。v0.4–v0.6 把相同 epigraph
problem 擴張到 measure dual 與 continuous Green RKHS。v0.7 再把一個
固定 continuous operator interval-certify。

所以真正要問的是：

1. upper-profile dual lower bound 對哪個命題合法？
2. 若換成 lower profile，是否就自動變成 actual zero-side lower bound？

第二問的答案是否定的。

## 二、三個不可混用的 band object

固定一個 band $A_j$。令其中實際零點多重集為

$$
\Gamma_j
=
\{\gamma_{j1},\ldots,\gamma_{jn_j}\}.
$$

對 $A\succeq0$，定義

$$
H_A(x)
=
\operatorname{Tr}(P_xA)
\ge0.
$$

### 1. Actual zero sum

$$
Z_j(A;\Gamma_j)
=
\sum_{k=1}^{n_j}H_A(\gamma_{jk}).
$$

它依賴零點位置與重數。

### 2. Supremum envelope

若 $n_j\le U_j$，則

$$
Z_j(A;\Gamma_j)
\le
U_j\sup_{x\in A_j}H_A(x).
$$

右側只依賴 band、count upper 與測試函數。它是合法的
zero-position-free upper bound。

### 3. Infimum minorant

若 $n_j\ge L_j$，則

$$
Z_j(A;\Gamma_j)
\ge
L_j\inf_{x\in A_j}H_A(x).
$$

若 $H_A$ 在 band 中可以有零點，這個 configuration-free lower bound
可能退化為零。

### 4. Probability average 不是第四個免費物件

對任意 probability measure $\mu_j$，

$$
\inf_{x\in A_j}H_A(x)
\le
\int H_A\,d\mu_j
\le
\sup_{x\in A_j}H_A(x).
$$

因此

$$
L_j\int H_A\,d\mu_j
$$

一般比合法的 infimum minorant 大。除非 $\mu_j$ 與實際零點位置之間另有
domination theorem，否則它不能充當 $Z_j$ 的下界。

## 三、exact two-point countermodel

令 band 只有兩點

$$
A=\{x_0,x_1\},
$$

實際零點多重集為

$$
\Gamma=\{x_0\},
$$

且

$$
H(x_0)=0,
\qquad
H(x_1)=1.
$$

此時

$$
n=L=U=1.
$$

actual sum 為

$$
Z(H;\Gamma)=0.
$$

upper envelope 正確：

$$
Z(H;\Gamma)
=0
\le
1
=U\sup_AH.
$$

infimum minorant 也正確：

$$
Z(H;\Gamma)
=0
\ge
0
=L\inf_AH.
$$

但若取

$$
\mu=\delta_{x_1},
$$

則

$$
L\int H\,d\mu=1,
$$

所以

$$
Z(H;\Gamma)
<
L\int H\,d\mu.
$$

這個反例全部使用 exact rationals。它證明「有至少 $L$ 個零點」與
「任意挑一個 probability measure」之間沒有合法箭頭。

## 四、rank-one operator 的共同下界障礙

在 $\mathbb R^2$ 令

$$
p_{x_0}=e_1,
\qquad
p_{x_1}=e_2,
$$

所以

$$
P_{x_0}
=e_1e_1^{\mathsf T},
\qquad
P_{x_1}
=e_2e_2^{\mathsf T}.
$$

若 $Q\succeq0$ 且同時

$$
Q\preceq P_{x_0},
\qquad
Q\preceq P_{x_1},
$$

正算子序給出

$$
\operatorname{ran}Q
\subseteq
\operatorname{span}(e_1)
\cap
\operatorname{span}(e_2).
$$

右側為 $\{0\}$，故 $Q=0$。

在 Green RKHS 中，evaluation representers $p_x$ 隨 $x$ 改變，通常不
共線。若 count certificate 允許所有零點集中在任意位置，任何 uniform
operator floor 都必須同時落在所有 rank-one ranges 中，通常只能是零。

這說明下一輪不能只把 scalar lower counts 做得更精確。即使 exact
$L_j$ 已知，也未必產生有用 operator mass。

## 五、upper coefficients 的合法保留

### 1. Method-level no-go

定義

$$
\mathcal E_U(A)
=
\operatorname{Tr}(TA)
+
\sum_jU_js_j,
$$

其中

$$
s_j\ge H_A(x)
\qquad
\forall x\in A_j.
$$

若存在 dual witness 證明

$$
\mathcal E_U(A)\ge\alpha
$$

對全部 target-feasible $A$ 成立，則可以嚴格推出：

> 在這個 test-function space 中，任何要求
> $\mathcal E_U(A)<\alpha$ 的 sufficient leakage-budget method 都無解。

這是有內容的 no-go theorem。它能排除一種證明技術，而不需要宣稱實際
零點和本身大於 $\alpha$。

### 2. 不能反向穿過 upper bound

即使另有

$$
Z_\Gamma(A)\le\mathcal E_U(A),
$$

由

$$
\mathcal E_U(A)\ge\alpha
$$

不能推出

$$
Z_\Gamma(A)\ge\alpha.
$$

上界很大可能只是 envelope 過度保守。

### 3. v0.7 的修正分類

所以 v0.7 的 coefficient orientation blocker 應細分為：

- 對 actual zero-side positive obstruction：確實是 blocker；
- 對 upper-envelope method no-go：upper coefficients 正是所需方向。

v0.7 interval operator 本身不撤回。它仍證明固定 abstract data 下

$$
W_{21/20}\succ0.
$$

尚缺的是把 abstract upper profile 與 tail coefficient 連到一個完整、
directed、theorem-backed envelope。

## 六、五帶 typed profile

本節點沿用 conservative floating profile

$$
|S(T)|
\le
0.112\log T
+
0.278\log\log T
+
2.510.
$$

由

$$
N(b)-N(a)
=
\frac{\theta(b)-\theta(a)}{\pi}
+S(b)-S(a)
$$

形式上得到

$$
L_{a,b}
=
\max\left(
0,
\frac{\theta(b)-\theta(a)}{\pi}
-B(a)-B(b)
\right),
$$

$$
U_{a,b}
=
\max\left(
0,
\frac{\theta(b)-\theta(a)}{\pi}
+B(a)+B(b)
\right).
$$

浮點結果為：

| band | $L$ candidate | $U$ candidate |
|---|---:|---:|
| $[14,18]$ | $0$ | $6.797423271049$ |
| $[18,23]$ | $0$ | $7.246636980607$ |
| $[23,35]$ | $0$ | $9.346770522331$ |
| $[35,70]$ | $5.069962795569$ | $18.367573606597$ |
| $[70,145]$ | $26.742367141539$ | $40.545362729237$ |

本節點故意把每列標成 theorem object，而非 certified theorem：

- source bound 版本需固定；
- theta、$\pi$、對數與 log-gamma 尚未 directed-enclose；
- endpoint 若恰為 zero ordinate 時的 convention 尚未封裝；
- scalar lower 不能被誤標為 operator lower。

## 七、lower-profile robust experiment

### 1. 模型

固定

$$
R=16
$$

與 structural constraints

$$
G(0)=G(i/2)=0.
$$

使用 clamped even Chebyshev family，raw dimensions 為

$$
24,40,64,80,96,120,144,160,176,192.
$$

prototype patch 為

$$
\mathcal P
=
[20.395,20.42]
\times
[-0.10625,-0.1].
$$

lower candidate profile 向下截為

$$
\mathbf L
=
(0,0,0,5.069962795568,26.742367141539).
$$

### 2. Galerkin convergence

| raw | effective | optimized $\alpha$ |
|---:|---:|---:|
| $24$ | $22$ | $2.6662663794$ |
| $40$ | $38$ | $1.0616159317$ |
| $64$ | $62$ | $0.4565992248$ |
| $80$ | $78$ | $0.3168124263$ |
| $96$ | $94$ | $0.2363398270$ |
| $120$ | $118$ | $0.1705859126$ |
| $144$ | $142$ | $0.1394428108$ |
| $160$ | $158$ | $0.1301510855$ |
| $176$ | $174$ | $0.1297049092$ |
| $192$ | $190$ | $0.1297047862$ |

在 effective dimension $38$ 時仍有

$$
\alpha>1.
$$

但 dimension $62$ 已降到

$$
0.4565992248.
$$

所以若只跑低維模型，會得到完全相反的研究判斷。

### 3. Direct Green transfer

最後 atomic measures 直接放入 clamped Green RKHS：

| $\Delta t$ | threshold |
|---:|---:|
| $0.02$ | $0.1296980713$ |
| $0.01$ | $0.1297028387$ |
| $0.005$ | $0.1297031276$ |

最後 direct 值與 dimension $190$ Galerkin 值的差約為

$$
1.66\times10^{-6}.
$$

這支持目前觀察不是 Chebyshev dictionary 偶然。

### 4. Sampled primal escape

取 dimension $190$ 的 minimum generalized direction，在

$$
101\times101
$$

core grid 與 axis step $0.01$ 上重算。縮放至

$$
\max_{\mathrm{core\ grid}}B=-1
$$

後，得到

$$
\mathcal E_L^{\mathrm{sampled}}
=
0.1297069814.
$$

高帶 sampled maxima 為

$$
\sup_{A_3}H
\approx
1.00123\times10^{-5},
$$

$$
\sup_{A_4}H
\approx
2.95980\times10^{-8}.
$$

這個 candidate 的主要成本幾乎全是 tail norm，而不是 $A_3,A_4$。

這仍是 E2 diagnostic：core continuum 尚未 interval-certify。但它已足以
否定「只需稍微重新加權 v0.7 atoms，就能在 lower profile 保持
$\alpha>1$」的研究期待。

## 八、prototype patch 的實際地位

本研究鏈選擇高度約 $20.4$ 的 patch，原意是用低成本數值模型測試
phase shaping、cover 與 dual geometry。它從未附帶 argument-principle
winding certificate。

Platt 與 Trudgian 已以 interval arithmetic 嚴格驗證：所有

$$
0<\gamma\le3\cdot10^{12}
$$

的非平凡 $\zeta$ 零點都位於臨界線。故本 patch 不可能是未決的實際
$\zeta$ 偏軸零點位置。

因此所有 v0.1–v0.8 low-height 結果的正確角色是：

- 測試證書結構；
- 找出係數與量詞錯誤；
- 校準 continuous kernel geometry；
- 建立可重播失敗標準。

它們不是對低高度 $\zeta$ 零點的新排除。

## 九、下一個正確研究物件

### 1. 不再只存 count interval

下一節點不應只輸出

$$
[L_j,U_j].
$$

至少需要：

- band 與 endpoint convention；
- 一族有理 location cells $I_{jk}$；
- 每個 cell 的 multiplicity 或 occupancy statement；
- argument-principle、Turing method 或其他存在性來源；
- 位置不確定性下的 universal operator-family inequality；
- source theorem 與 interval proof hash。

### 2. 不強迫不存在的固定 operator floor

由 rank-one common-floor obstruction，下一節點不應要求每個 cell 都產生
固定

$$
Q_{jk}\preceq P_x
\qquad
\forall x\in I_{jk},
$$

因為這個 $Q_{jk}$ 可能只能是零。

更自然的證書是保留位置變數：

$$
x_{jk}\in I_{jk},
$$

並直接證明

$$
W_\alpha(\{x_{jk}\})
\succeq0
$$

對全部允許位置共同成立。

在 Green-kernel reduction 中，這可轉成 finite Schur matrix 的 interval
family，而不是先壓成一張位置無關 rank-one lower matrix。

### 3. 兩條可並行但不可混寫的路

下一研究階段分成：

#### Track A：完成 method no-go

把 v0.7 的 upper profiles、tail coefficient 與 epigraph semantics
全部 theorem-certify，得到：

> 在固定 $R=16$ continuous space 中，該 conservative supremum
> leakage proof strategy 無法達到 budget $1$。

#### Track B：actual zero-side occupancy

建立位置 cells 與 universal operator family，研究真實零點和，而非
worst-case supremum envelope。

Track A 的成功不等於 Track B；Track B 也不能靠 scalar lower counts
取代位置資訊。

## 十、研究判斷

本節點得到的最重要進展不是新的大門檻，而是一個型別修正：

$$
\text{count upper}
\longrightarrow
\text{supremum envelope upper bound},
$$

$$
\text{count lower}
\longrightarrow
\text{infimum scalar lower bound},
$$

但

$$
\text{count lower}
\not\longrightarrow
\text{arbitrary dual measure operator mass}.
$$

這個修正保留了 v0.7 的 interval achievement，也防止把它超譯成
zero-side positivity。

lower-profile 重算則提供第二個決策：

$$
\alpha_{\mathrm{continuous\ diagnostic}}
\approx
0.129703
\ll1.
$$

因此目前不值得再花算力搜尋同型 robust witness。下一步的資訊增益來自
occupancy/location quantifiers，而不是更多 scalar count precision 或
更高 Galerkin dimension。

## 結論

v0.8 完成了三件事：

1. 對 v0.1–v0.7 的 coefficient semantics 做 exact repair；
2. 以 exact countermodel 證明 scalar lower count 不能支配任意 dual
   measure；
3. 以 high-dimensional Galerkin、direct Green 與 sampled primal 三重
   診斷確認 lower-profile obstruction 消失。

因此下一節點定為：

> `RH-Occupancy-OperatorFamily-20260725-v0.9`

其核心不是更多 band counts，而是可驗證的 cell occupancy 與對所有位置
共同成立的 Green-Schur operator family。

本文保留全部 global RH flags 為 false。
