# 占用算子族與覆蓋式 Green 證書

## RH 位置量詞語義橋、精確合成模型與微半徑轉移

### v0.9 半 AI 自主研究稿

日期：2026-07-25  
節點：`RH-Occupancy-OperatorFamily-20260725-v0.9`

---

## 摘要

前一節點 v0.8 完成了 zero-count coefficients 的型別修正：band count
upper bound 可合法產生 supremum leakage upper envelope；band count
lower bound 只能產生 infimum scalar lower bound，不能乘上一個任意
probability measure 後被解讀為實際零點的 operator mass。這個修正使
原定的「把每帶計數係數做得更精確」失去主線地位。真正缺少的是零點位置
資訊與對全部允許位置共同成立的 operator theorem。

本文把下一階段改寫為

$$
\text{cell occupancy}
\longrightarrow
\text{uncertain locations}
\longrightarrow
\text{universal operator family}
\longrightarrow
\text{cover certificate}.
$$

本輪取得三個層次的結果。

第一，建立 `OccupancySelectionOperatorTransfer`：若每個有來源的 cell
至少含指定重數的實際點，而且 selected-point operator 對所有 cell 內
位置共同為 PSD，則包含全部實際點的 operator 亦為 PSD。這個推論只使用
「未選取點提供額外 PSD 項」，完全不需要任意對偶測度。

第二，在

$$
H_0^1(0,1)
$$

的 Dirichlet Green RKHS 中建立全有理 prototype。單純知道總計數為
$2$ 時，可取兩點都位於 $1/5$，得到精確 Schur determinant

$$
-\frac{254}{558009}<0.
$$

相反地，若已知左右兩個分離 cells 各至少含一點，則以自適應 interval
cover 可對所有未知位置證明 positivity。根盒本身的自然 interval
extension 不能判定；二分後得到 $8$ 個 certified leaves，最大深度
$7$，最小 determinant lower bound 約為 $1.0797\times10^{-5}$。

第三，利用 v0.7 已完成的固定位置 abstract interval theorem。把
$\alpha=21/20$ 降到 $\alpha=1$ 產生精確 $1/21$ identity margin；再以
兩次 Poincaré inequality 與 rank-one perturbation bound，把原本
$58$ 個固定 axis atoms 各擴成獨立 closed location cell。uniform
half-width

$$
2\times10^{-15}
$$

時，可證整個 family 的 coercivity lower bound 約為
$0.00644077361$。

浮點 adversarial corner study 則在 half-width $0.016$ 與 $0.017$
之間觀察到門檻跨越 $1$。這不是 universal theorem，卻指出 exact
Poincaré budget 與 local numerical scale 間約有

$$
8\times10^{12}
$$

的差距。故下一節點應開發 local interval Green derivatives 與
adaptive Schur cell cover，而不是回到 scalar count refinement。

本文沒有 theorem-backed $\zeta$ occupancy cells，沒有完成 explicit
formula global transfer，也不構成 RH 證明或反證。全部 global RH flags
維持 false。

---

## 一、研究定位：從計數語義轉向位置量詞

### 1. ZFC 與命題邊界

RH 理論上只能由一條以 ZFC 為基礎、依賴可追蹤、定義不可偷換的證明鏈
完成。若某個核心 operator identity、trace formula、topological
obstruction 或 positivity theorem 只在未翻譯回 ZFC 的擴張系統中成立，
它最多支援該擴張系統中的類比命題。

本研究的目的不是先宣稱 RH，再回頭補缺；而是把每個可疑推論編譯成：

- 明確的輸入型別；
- 明確的量詞；
- 可機讀的 dependency；
- 可失敗的 verifier；
- 不可被名稱替換掩蓋的 GAP。

### 2. v0.8 留下的不可逆修正

固定 band $A_j$、實際零點多重集 $\Gamma_j$ 與非負函數 $H$。若

$$
|\Gamma_j|\le U_j,
$$

則

$$
\sum_{\gamma\in\Gamma_j}H(\gamma)
\le
U_j\sup_{x\in A_j}H(x).
$$

若

$$
|\Gamma_j|\ge L_j,
$$

則

$$
\sum_{\gamma\in\Gamma_j}H(\gamma)
\ge
L_j\inf_{x\in A_j}H(x).
$$

第二式不能被改寫為

$$
L_j\int H\,d\mu_j
$$

對任意 probability measure $\mu_j$ 的 lower bound。這不是誤差大小
問題，而是量詞與資料型別問題。

因此，若 operator $P_x$ 隨位置轉動，知道「band 內至少有一點」通常不能
產生非零固定 common floor

$$
Q\preceq P_x
\qquad
\forall x\in A_j.
$$

本輪改為保留 $x$，直接證明 family。

---

## 二、Occupancy certificate 的最小合法資料

### 1. Source cell 與 operator hull

每個 occupancy record 至少包含：

| field | 意義 |
| --- | --- |
| `cell_id` | 穩定識別碼 |
| rational endpoints | 可精確重播的區間 |
| endpoint convention | 計數分割的開閉端點 |
| `multiplicity_lower` | 該 cell 至少含多少實際點 |
| `presence_theorem_id` | 證明存在性的來源 |
| source hash | 來源版本鎖 |
| certification status | synthetic、floating 或 rigorous |

source cells 的 endpoint convention 負責避免邊界點被重複計數。算子
family 的不確定區間可使用 source cell 的 closed hull，因為把允許位置
集合擴大只會讓 universal theorem 更強、更保守。

### 2. 不可省略的量詞

合法 occupancy premise 是

$$
\#(\Gamma\cap I_r)\ge\ell_r.
$$

接下來必須選取

$$
x_{rk}\in I_r,
\qquad
1\le k\le\ell_r,
$$

並保留

$$
\forall(x_{rk})
$$

直到 operator inequality 完成。若在中途用某個方便的 atomic measure
平均掉位置，便再次回到 v0.8 已否定的推論。

---

## 三、Occupancy selection operator transfer

令 $\mathcal H$ 為實 Hilbert 空間，並令

$$
P_x=p_x\otimes p_x\succeq0.
$$

固定 base operator $C$，它可以含有有限秩負方向。對每個 cell 選取
$\ell_r$ 個位置，定義

$$
W_{\mathrm{sel}}(\mathbf x)
=
C+
\sum_r\sum_{k=1}^{\ell_r}\lambda_rP_{x_{rk}},
\qquad
\lambda_r\ge0.
$$

### 定理

若每個 cell 的 occupancy premise 成立，且

$$
W_{\mathrm{sel}}(\mathbf x)\succeq0
$$

對所有允許 selection 共同成立，那麼包含所有實際點的 operator 亦為
PSD。

### 證明

在每個 cell 的實際點中選出 $\ell_r$ 個，形成
$\mathbf x_\Gamma$。全部 operator 等於

$$
W_{\mathrm{all}}(\Gamma)
=
W_{\mathrm{sel}}(\mathbf x_\Gamma)
+
\sum_{z\in\Gamma_{\mathrm{surplus}}}
\lambda(z)P_z.
$$

第一項由 universal theorem 為 PSD；第二項是 nonnegative weighted
rank-one PSD sum。故

$$
W_{\mathrm{all}}(\Gamma)\succeq0.
$$

證畢。

### 這個定理真正修復了什麼

它沒有聲稱 scalar count 會變成 operator lower mass。它只說：

1. occupancy theorem 允許從實際 configuration 中選點；
2. universal family theorem 已涵蓋所有可能 selection；
3. 實際 configuration 的剩餘點只增加 PSD 項。

所以 operator transfer 的內容完全由「選取」與「剩餘 PSD」承擔。

---

## 四、負秩小時的 Green–Schur family

令正向 representers 為 $U$，負向 representers 為 $V$，並考慮

$$
W
=
I+UD_\lambda U^\ast-VD_\beta V^\ast.
$$

正向 operator

$$
B=I+UD_\lambda U^\ast
$$

永遠嚴格正。由 Schur complement，

$$
W\succeq0
\quad\Longleftrightarrow\quad
D_\beta^{-1}-V^\ast B^{-1}V\succeq0.
$$

再用 Woodbury identity：

$$
B^{-1}
=
I-U
\left(D_\lambda^{-1}+U^\ast U\right)^{-1}
U^\ast.
$$

令 Green Gram blocks 為 $K_{XX},K_{XY},K_{YY}$，得到

$$
S
=
D_\beta^{-1}
-K_{YY}
+K_{YX}
\left(D_\lambda^{-1}+K_{XX}\right)^{-1}
K_{XY}.
$$

未知 occupancy locations 只進入這些 Gram blocks。當 negative rank
$q=2$ 時，最後 universal test 只需

$$
S_{11}>0,
\qquad
\det S>0.
$$

因此「位置變數很多」不必等同於「最後符號矩陣很大」。真正的工程問題是
如何嚴格 enclosure 每個 Green pairing 與正向 solve。

---

## 五、全有理 Dirichlet Green prototype

### 1. 選擇此模型的理由

取

$$
\mathcal H=H_0^1(0,1)
$$

及 inner product

$$
\langle f,g\rangle
=
\int_0^1f'(t)g'(t)\,dt.
$$

其 evaluation Green kernel 是

$$
K(s,t)=\min(s,t)-st.
$$

這是一個真正的 infinite-dimensional RKHS Green kernel，但在有理
cell 上仍可用純 `Fraction` 計算。它適合先隔離量詞、cover 與 Schur
工程，不把 transcendental interval arithmetic 混入第一個 prototype。

### 2. 模型參數

兩個 occupancy cells 為

$$
I_1=
\left[\frac15,\frac25\right],
\qquad
I_2=
\left[\frac35,\frac45\right].
$$

負向 targets 為

$$
y_1=\frac13,
\qquad
y_2=\frac23,
$$

且

$$
\beta_1=\beta_2=\frac{83}{25}.
$$

目標 family：

$$
W(x_1,x_2)
=
I+P_{x_1}+P_{x_2}
-\frac{83}{25}
\left(P_{1/3}+P_{2/3}\right).
$$

### 3. Total count $2$ 的精確反例

若只知道 broad union 內有兩點，則 configuration

$$
x_1=x_2=\frac15
$$

仍被允許。此時 positive system 為

$$
A=
\begin{pmatrix}
\frac{29}{25}&\frac4{25}\\
\frac4{25}&\frac{29}{25}
\end{pmatrix}.
$$

Schur matrix 是

$$
S=
\begin{pmatrix}
\frac{2611}{24651}&-\frac{29}{297}\\
-\frac{29}{297}&\frac{2113}{24651}
\end{pmatrix},
$$

其 determinant 為

$$
\det S=-\frac{254}{558009}<0.
$$

並有顯式負方向

$$
v=
\left(
-\frac{29}{297},
-\frac{2611}{24651}
\right),
$$

滿足

$$
v^\mathsf TSv
=
-\frac{663194}{13755479859}<0.
$$

因此 total count $2$ 不足；左右 cell 各一點才是這個 operator statement
真正需要的型別。

---

## 六、覆蓋式證書族

### 1. 根盒為何不能直接通過

在

$$
I_1\times I_2
$$

上直接做 interval extension，重複出現的變數會被當成獨立端點選擇，
導致 dependency overestimation。根盒的 determinant enclosure lower
endpoint 為負，所以單盒 verifier 必須拒絕。

這個拒絕的狀態是：

`split_inconclusive`

而不是：

`operator_counterexample`。

### 2. 自適應規則

每個 box 依序：

1. enclosure $K_{XX},K_{XY},K_{YY}$；
2. enclosure

   $$
   A^{-1}
   =
   \left(D_\lambda^{-1}+K_{XX}\right)^{-1};
   $$

3. enclosure $S$；
4. 檢查 $S_{11}$ 與 $\det S$ lower endpoints；
5. 若不足，沿最寬座標精確中點二分；
6. 寬度相同時選最小 coordinate index。

所有 node 都保存 path、box、split、Schur intervals 與 status。葉盒 paths
必須 prefix-free，children 必須完整覆蓋 parent。

### 3. 結果

| 指標 | 結果 |
| --- | ---: |
| root directly certified | false |
| tree nodes | $15$ |
| certified leaves | $8$ |
| unresolved leaves | $0$ |
| maximum depth | $7$ |

所有 leaves 的 first leading minor lower 都正。最小 determinant lower
為

$$
\frac{
996149099768633906407318481
}{
92259342242007809509970517515625
}
\approx
1.07972708\times10^{-5}.
$$

因此

$$
W(x_1,x_2)\succ0
$$

對所有

$$
(x_1,x_2)\in I_1\times I_2
$$

成立。

這個例子也說明了「覆蓋拓樸」在本方法中的具體用途：不是把某個直觀空間
名稱當作證明，而是把 parameter box 拆成有限 closed cover，讓每個局部
chart 都攜帶可重播 inequality certificate，最後由 cover completeness
還原全域量詞。

---

## 七、從固定原子到 $58$-cell clamped family

### 1. Parent theorem 與 convex margin

v0.7 已 interval-certify 固定位置的 abstract operator

$$
W_{21/20}(\mathbf c)\succeq0.
$$

令 axis positive part 為 $A(\mathbf c)$，core indefinite part 對
$\alpha$ 線性。則

$$
W_1(\mathbf c)
=
\frac{20}{21}W_{21/20}(\mathbf c)
+
\frac1{21}\left(I+A(\mathbf c)\right)
\succeq
\frac1{21}I.
$$

這個轉換的重要點是：不必從 parent interval Schur matrix 猜測 full
operator 的最小 eigenvalue；identity margin 由 convex combination
精確給出。

### 2. 全域 Green norm upper bound

在 $[-R,R]$ 的 clamped space 取能量

$$
\tau\int_{-R}^{R}|u''(t)|^2\,dt.
$$

兩次 Poincaré inequality 給

$$
\|u\|_2
\le
\frac{(2R)^2}{\pi^2}\|u''\|_2.
$$

因此 Green inverse 的 $L^2$ norm 可由

$$
\|G\|_{2\to2}
\le
\frac{(2R)^4}{\pi^4\tau}
<
\frac{(2R)^4}{81\tau}
=C_G
$$

控制。

axis density 與位置導數為

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

若 $p_x$ 是 projected representer，則 structural projection 不增加
norm。利用

$$
\|p_x\otimes p_x-p_c\otimes p_c\|
\le
\|p_x-p_c\|
\left(\|p_x\|+\|p_c\|\right)
$$

與

$$
\sqrt3>\frac53,
$$

得到

$$
\|P_x-P_c\|
<
\frac{12}{5}R^2C_G|x-c|.
$$

### 3. 多 cell budget

令 $58$ 個 axis operator weights 為 $\lambda_i$。它們的精確總和是

$$
\Lambda
=
\sum_i\lambda_i
=
\frac{10287970888727}{125000000000}.
$$

對獨立 locations

$$
x_i\in[c_i-h,c_i+h]
$$

有

$$
\left\|
\sum_i\lambda_i(P_{x_i}-P_{c_i})
\right\|
\le
\frac{12}{5}R^2C_G\Lambda h.
$$

取

$$
h=\frac{1}{500000000000000},
$$

得到 perturbation upper

$$
\varepsilon
=
\frac{
12328822128706060288
}{
299401138693037109375
}
\approx0.04117827401.
$$

因

$$
\varepsilon<\frac1{21},
$$

故對全部 $58$ 個獨立位置共同成立：

$$
W_1(\mathbf x)
\succeq
\frac{
13498624663403281109
}{
2095807970851259765625
}I
\succ0.
$$

### 4. 這張證書的精確分類

它是：

- exact rational perturbation theorem；
- conditional on the v0.7 parent interval theorem；
- universal over $58$ independent location cells；
- coordinate-dependent on v0.7 dual atom centers and weights。

它不是：

- $\zeta$ zero occupancy theorem；
- count lower profile 的 operator realization；
- unresolved-height exclusion；
- RH certificate。

---

## 八、浮點局部尺度診斷

### 1. 對抗角點搜尋

為估計全域 Poincaré bound 的保守度，本文以 direct clamped Green
reconstruction 做 E2 diagnostic：

1. 在每個中心位置做 central difference；
2. 取降低 fixed-measure threshold 的 gradient-sign corner；
3. 逐座標嘗試反轉 corner sign；
4. 最多四輪，直到沒有進一步改善。

### 2. 結果

| half-width | threshold at $\Delta t=0.02$ |
| ---: | ---: |
| $0.012$ | $1.0458517424$ |
| $0.014$ | $1.0240427949$ |
| $0.015$ | $1.0124640056$ |
| $0.016$ | $1.0004604738$ |
| $0.017$ | $0.9880516263$ |
| $0.018$ | $0.9748129050$ |
| $0.020$ | $0.9471623347$ |

對 $h=0.016$ 的同一角點，time-step refinement 為

$$
\begin{array}{c|c}
\Delta t&\text{threshold}\\
\hline
0.02&1.0004604738\\
0.01&1.0004696571\\
0.005&1.0004702150
\end{array}
$$

對 $h=0.017$ 則為

$$
\begin{array}{c|c}
\Delta t&\text{threshold}\\
\hline
0.02&0.9880516263\\
0.01&0.9880608157\\
0.005&0.9880613743
\end{array}
$$

### 3. 不可超譯

這個搜尋：

- 沒有窮盡 $2^{58}$ corners；
- 沒有涵蓋 interiors；
- 沒有 interval enclosure；
- threshold below $1$ 只是 floating candidate。

所以它不能證明某個 cell family 失敗。它只提供 local scale 與下一個
驗證器設計的目標。

### 4. Proof-budget gap

exact uniform half-width 為

$$
2\times10^{-15},
$$

而最後一個浮點測得 threshold above $1$ 的 half-width 是

$$
0.016.
$$

兩者比值為

$$
8\times10^{12}.
$$

這表示下一步最值得改善的是：

- local frequency-sensitive Green resolvent bound；
- interval derivatives in $x$；
- Taylor models；
- adaptive location covers；
- low-rank Schur interval solve。

若只繼續細化 global Poincaré constant，通常無法跨越十三個數量級。

---

## 九、GAP 圖譜

### 已閉合

#### `G09-SEM-01`

Occupancy selection 的 operator transfer 已閉合。  
證據：符號推論與 exact semantic output。

#### `G09-SEM-02`

Total count 不能替代分帶 occupancy。  
證據：determinant $-254/558009$ 與顯式負方向。

#### `G09-COVER-01`

Exact rational Green cover engine 已閉合。  
證據：$8$ leaves、無 unresolved node、完整再生驗證。

#### `G09-CLAMP-01`

固定 parent atoms 到微半徑位置族的條件式提升已閉合。  
證據：$58$ cells 與精確正 coercivity lower。

### 仍開放

#### `G09-GREEN-LOCAL`

缺少 clamped Green pairing 對位置 cell 的局部 directed enclosure。  
優先度：最高。

#### `G09-ZETA-OCC`

缺少實際 $\zeta$ 零點的 cell presence theorem、endpoint nonzero
certificate、multiplicity 與 source hash。  
優先度：最高。

#### `G09-EF-TRANSFER`

缺少 test-function admissibility、zero-side operator expression 與
prime-side nonnegative cone 的 ZFC 依賴鏈。  
優先度：最高。

#### `G09-UPPER-NOGO`

v0.7 upper-envelope method no-go 仍需 upper count 與 tail coefficient 的
directed source certification。  
路線：Track A，與 actual occupancy 分離。

#### `G09-GLOBAL`

缺少 unresolved-height cover、local-to-global exhaustion 與全臨界帶
transfer。  
優先度：後置但必要。

---

## 十、下一節點

下一節點固定為：

`RH-LocalIntervalGreen-CellCover-20260725-v0.10`

### Work package A：local Green enclosure

建立

$$
\langle p_x,p_y\rangle
$$

對 $x,y$ cells 的 directed bounds，優先加入一階與二階位置導數。

### Work package B：adaptive Schur cover

依序測試 half-width ladder

$$
10^{-8},\ 10^{-6},\ 10^{-4},\ 10^{-3}.
$$

每次失敗必須區分：

- point counterexample；
- interval dependency；
- inverse enclosure；
- Sylvester lower bound；
- resource stop。

### Work package C：occupancy source schema

只做 presence certificate 的資料型別與 verifier，不在 kernel family 尚未
處理 macroscopic cells 前宣稱實際 zeta-facing exclusion。

---

## 結論

本輪最重要的進步不是某個 threshold 數字，而是把 v0.8 的否定結果轉成
正向、可執行的替代架構：

$$
\boxed{
\text{有來源的 cell occupancy}
+
\text{保留全部位置量詞}
+
\text{低負秩 Schur family}
+
\text{有限覆蓋證書}
}
$$

全有理 Green prototype 證明這個架構可以工作，而且 scalar count-only
確實會失敗。v0.7 parent theorem 又使第一張 $58$-cell clamped family
成為嚴格結果，儘管目前半徑只有 $2\times10^{-15}$。

浮點局部診斷沒有被超譯為 theorem；它的用途是定位十三個數量級的
proof-budget gap。下一步應把全域 norm bound 換成 local interval Green
geometry，讓覆蓋證書真正進入可用尺度。

最終狀態：

- exact synthetic occupancy family：true；
- conditional abstract clamped family：true；
- actual zeta occupancy family：false；
- explicit-formula global transfer：false；
- global RH certificate：false。

