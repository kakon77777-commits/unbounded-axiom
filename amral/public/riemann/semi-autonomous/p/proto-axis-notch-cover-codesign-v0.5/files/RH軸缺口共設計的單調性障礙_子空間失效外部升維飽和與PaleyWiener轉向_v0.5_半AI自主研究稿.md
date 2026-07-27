# RH 軸缺口共設計的單調性障礙

## 子空間失效、外部升維飽和與 Paley–Wiener 轉向

版本：v0.5  
日期：2026-07-24  
研究模式：半 AI 自主數學研究  
技術研究主導：OpenAI Codex  
研究現場授權與審閱：Neo.K / EveMissLab

## 摘要

本節點承接 v0.4 的 support–prime dual frontier。父節點在
$R=10.25,12,14,16$ 的抽樣困難子矩形上都保存了
$\alpha_{\rm safe}>1$ 的 joint-dual witnesses，並發現 $R=16$ 的粗軸網格
$\alpha<1$ 是假逃逸。因此 v0.5 不再擴大支撐半徑，而是嘗試由 witness
支撐峰反向設計實軸 value/derivative notches、外部頻譜方向與局部 bump
幾何。

12 份父 witnesses 的等權聚合 peak atlas 在五個軸帶給出

$$
17.83,\quad20.38,\quad23.24,\quad42.18,\quad83.05.
$$

其中 $20.38$ 落在 target real interval $[20,20.5]$，而遠帶峰約位於
$2.07$ 與 $4.08$ 倍尺度。這支持一個自然 Taylor 構想：若
$G(x_0)=0$ 而 $G'(x_0)\ne0$，則

$$
G(x_0+iy)^2=-y^2G'(x_0)^2+O(|y|^3),
$$

所以實軸缺口可能同時壓低軸值並保留偏軸負方向。

本節點的關鍵修正是：若 notch 只是對既有測試函數空間加入齊次線性約束，
新空間只是父空間的子空間。父節點的 PSD Gram 已搜尋完整父空間，因此子空間
不可能產生父問題沒有的 primal feasible point。這是一個有限模型內的 exact
feasible-set inclusion，而不只是數值失敗。

為避開此單調性障礙，本節點加入父字典之外的 compact spectral-slope atoms

$$
\psi_{\omega,p}(t)
=t\left(1-\frac{t^2}{R^2}\right)_+^p\sin(\omega t).
$$

它們在 $R=16$ 的 uniform/core screen 最多改善約 $3.10\%$，但 joint raw
dual 下界只由 $1.189562$ 降至 $1.176230$，安全下界仍為
$1.088115>1$。另一次 27 組 polynomial-bump geometry sweep 的最佳
`d12_w2_p5` 將 raw joint dual 改善 $3.87\%$，但

$$
\alpha_{\rm safe}=1.071761>1,
$$

且 tail 最小特徵值只約 $1.15\times10^{-3}$。加密 complementary audit
亦顯示遠帶峰主要是遷移，不是消失，而 $A_1$ charge 仍主導。

因此本節點不啟動 primal Gram 搜尋，並停止三條支線：純齊次 notch、目前的
spectral-slope lift family，以及更多 polynomial-bump scaling。下一節點
轉向 continuous Paley–Wiener axis/core extremal，嘗試把反覆出現的離散
dual measures 解讀為 reproducing-kernel inequality 的近似支撐，進而建立
解析 lower bound、continuous extremizer 或帶誤差控制的 Galerkin
convergence。

本稿不是 RH 證明或反證，也沒有連續軸或 interval-certified transfer。

## 1. 問題位置

### 1.1 父節點留下的決策狀態

研究鏈 v0.1–v0.4 已把原始想法逐步改寫成 finite PSD Gram 與 joint-dual
gate。父節點的重要狀態是：

1. 18 個原始 patches 細分為 288 個子矩形；
2. 在四個半徑的 12 個困難子矩形保存 sparse dual witnesses；
3. 每個抽樣半徑至少有一個 reconstructed safe lower bound 大於 $1$；
4. $R=16$ 在軸步長 $0.25$ 上出現的 $\alpha<1$，於加密至 $0.025$ 後
   消失；
5. 支撐截斷成本隨 $e^{2R}$ 成長，繼續加半徑的決策價值過低。

父節點因此交接一個很具體的問題：能否從 active axis supports 找出反覆峰，
再設計測試函數，使軸負擔下降而偏軸核心負方向不被破壞？

### 1.2 固定有限模型

本節點固定目標矩形

$$
\mathcal R=[20,20.5]\times[-0.2,-0.1]
$$

及五個實軸帶

$$
A_0=[14,18],\quad A_1=[18,23],\quad A_2=[23,35],
$$

$$
A_3=[35,70],\quad A_4=[70,145].
$$

主要 joint pilot 使用父節點在 $R=16$ 的困難子矩形
`x4_Y3__r3_3`：

$$
\mathcal P
=[20.395,20.42]\times[-0.10625,-0.1].
$$

測試函數由 real-even compactly supported $\psi$ 的 Fourier transform

$$
G(z)=\int_{-R}^{R}\psi(t)e^{izt}\,dt
$$

生成，並保留父節點的結構約束

$$
G(0)=0,\qquad G(i/2)=0.
$$

### 1.3 Gate-first 原則

對 PSD Gram variable $A\succeq0$，軸側 quadratic matrices 記為 $P_x$，
偏軸核心 matrices 記為 $C_z$，tail matrix 記為 $T$。若存在五個正規化
非負軸測度 $\mu_j$、正規化核心測度 $\nu$ 與 $\alpha>1$ 使

$$
W
=T+\sum_{j=0}^{4}\underline N_j\int_{A_j}P_x\,d\mu_j(x)
+\alpha\int_{\mathcal P}C_z\,d\nu(z)
\succeq0,
$$

則對指定 finite primal constraints，可由 trace pairing 得

$$
J(A)\ge\alpha.
$$

所以只要重建後的 $\alpha_{\rm safe}>1$，該 branch 就不值得啟動昂貴
primal 搜尋。這個 gate 節省的不是少量時間，而是避免在已知不可行的 finite
branch 上繼續建立大規模質數矩陣。

## 2. 由 witnesses 建立軸峰 atlas

### 2.1 聚合規則

父節點保存 12 份 sparse witnesses。若直接把所有 support weights 疊加，
support 較多或數值質量較大的 witness 會主導圖譜。本節點因此採用：

1. 對每份 witness、每個 band 個別正規化；
2. 每份 witness 在每個 band 給相同總質量；
3. 以固定 bandwidth Gaussian KDE 聚合 support locations；
4. 只把 KDE maxima 當作 dictionary-design diagnostic。

此規則沒有宣稱估計任何真實零點分布，也沒有使用已知零點 ordinates。

### 2.2 聚合結果

五帶主峰為：

| band | weighted mean | weighted standard deviation | KDE primary peak |
|---|---:|---:|---:|
| $A_0$ | $16.8735$ | $1.0222$ | $17.83$ |
| $A_1$ | $20.4385$ | $0.1772$ | $20.38$ |
| $A_2$ | $23.7274$ | $0.6168$ | $23.24$ |
| $A_3$ | $42.1315$ | $0.1640$ | $42.18$ |
| $A_4$ | $83.0129$ | $0.2636$ | $83.05$ |

最值得注意的不是遠帶的近倍頻，而是 $A_1$ 峰直接落入 target real interval。
這表示「把軸峰挖掉」與「在同一實部附近產生偏軸負值」可能共享同一組 degrees
of freedom。局部與全域不是兩個可分離的優化問題。

遠帶比值為

$$
\frac{42.18}{20.38}\approx2.069676,\qquad
\frac{83.05}{20.38}\approx4.075074.
$$

它們足以支持 harmonic-notch ablation，但不足以聲稱真正的解析 harmonic
law；父 witness 的 active supports 本身是離散優化輸出。

## 3. Taylor notch：正確直覺與錯誤推論

### 3.1 局部負平方

因 $\psi$ real-even，$G(x)$ 在實軸上為實值。若在 $x_0$ 設計
$G(x_0)=0$，則

$$
G(x_0+iy)
=iyG'(x_0)-\frac{y^2}{2}G''(x_0)+O(|y|^3).
$$

平方後取 leading term：

$$
G(x_0+iy)^2
=-y^2G'(x_0)^2+O(|y|^3).
$$

因此單一 value zero 保留 slope 時，的確有機會產生需要的負方向。若再要求
$G'(x_0)=0$，則這個二階負項消失，核心效果延後到更高階。

這個 Taylor 判斷是正確的，但它只描述一個特定函數方向附近的局部行為，
不能推出「對既有完整 Gram 空間加入 notch constraint 會改善最優值」。

### 3.2 子空間單調性命題

**命題 3.1。** 令 $V$ 為有限維測試函數空間，$V'\subseteq V$ 為加入任意
齊次 value/derivative constraints 後的子空間。令 $\mathcal F(V)$ 與
$\mathcal F(V')$ 分別為在相同 PSD、core 與 axis 規則下形成的 Gram feasible
sets。則

$$
\mathcal F(V')\subseteq\mathcal F(V).
$$

因而對相同最小化目標 $J$，

$$
\inf_{A\in\mathcal F(V)}J(A)
\le
\inf_{A\in\mathcal F(V')}J(A).
$$

**證明。** 取 $V'$ 的基底，經 inclusion map 嵌入 $V$。每個在 $V'$ 上的
PSD Gram form 都可透過 congruence 嵌入成 $V$ 上的 PSD Gram form，且所生成
的函數與所有 evaluation quadratic forms 不變。因此 $V'$ 的每個 feasible
point 也是 $V$ 的 feasible point。取 infimum 即得結論。$\square$

### 3.3 研究後果

父節點已在完整 $V$ 上允許任意 PSD Gram mixing。若已有 dual witness 證明
該完整空間中 $J(A)\ge1$，則以下動作都不能 rescue：

$$
G(a)=0,\qquad G'(a)=0,\qquad
G(a_k)=0\ \text{for finitely many }a_k,
$$

只要這些條件沒有加入父空間之外的新方向。

這個結論比「某一組 notch 參數跑失敗」更強，也更窄：

- 更強，因為它一次排除所有純齊次子空間 notches；
- 更窄，因為它不排除 affine normalization、非線性 construction、外部
  atoms 或更大的 continuous function space。

## 4. 子空間 notch 的實驗核對

本節點仍跑了十組 code，目的不是用數值證明命題，而是檢查 Taylor 預測與
程式坐標是否一致。code 包含：

- patch center value zero；
- center 加 $A_3$ 或 $A_4$ 主峰；
- center 加二倍、四倍 harmonic zeros；
- 五帶 atlas zeros；
- patch 左右 edge pair；
- center 同時 value/derivative zero。

在 $R=16$：

| code | dimension | optimized-core / uniform-axis threshold |
|---|---:|---:|
| baseline | $158$ | $0.251927$ |
| `anchor1` | $157$ | $0.252055$ |
| `anchor_A3` | $156$ | $0.258737$ |
| `anchor_A4` | $156$ | $0.278994$ |
| `harmonic3` | $155$ | $0.253755$ |
| `edge_pair` | $156$ | $32.487862$ |
| `anchor_flat` | $156$ | $33.845656$ |

`anchor1` 幾乎不改變 threshold，但方向是略微變差。遠帶 zeros 逐步損害
核心效率。最清楚的是 `anchor_flat`：其 anchor derivative Frobenius norm
約

$$
1.07\times10^{-12},
$$

正如 Taylor analysis 所預測，二階負方向幾乎被消除。

在 $R=10.25$，`anchor_flat` threshold 更達 $691.837880$。這不是因為
$R=10.25$ 有某個神秘病態，而是當可用維度更少、核心本就接近 gate 時，
close zeros 或 flat zero 更容易摧毀 core normalization。

## 5. 外部 spectral-slope lift

### 5.1 為何必須升維

命題 3.1 指出：若要讓 notch idea 仍有決策價值，就必須新增

$$
V_{\rm new}\not\subseteq V_{\rm parent}.
$$

本節點選用

$$
\psi_{\omega,p}(t)
=tq_{R,p}(t)\sin(\omega t),
$$

其中

$$
q_{R,p}(t)
=\left(1-\frac{t^2}{R^2}\right)_+^p,\qquad p\ge3.
$$

$t\sin(\omega t)$ 是 even，乘上 real-even compact window 後仍是
real-even compact atom。其 Fourier transform 在 $\omega$ 附近提供
slope-like 調節，而不以硬 constraint 刪除父空間方向。

### 5.2 實作細節

程式對每個 atom 解析計算

$$
\psi_{\omega,p}''(t),
$$

再與 local bump basis 一起建立 derivative/tail quadratic form。新 columns
先做 $L^2$ normalization，再與

$$
G(0)=G(i/2)=0
$$

一同 constrained-whiten。因部分頻率 directions 在 constraint 與數值
rank 判定後相關，21 個候選 atoms 最終增加 15 個有效維度。

### 5.3 Screen 結果

在 $R=10.25$：

$$
0.999424\longrightarrow0.979093.
$$

在 $R=16$：

$$
0.251927\longrightarrow0.245526
$$

對應第一輪六方向 lift。

接著在 $R=16$ 做 scaling：

| lift | effective added dimension | threshold | improvement |
|---|---:|---:|---:|
| `grid5_p4` | $5$ | $0.246645$ | $2.10\%$ |
| `grid9_p4` | $8$ | $0.245755$ | $2.45\%$ |
| `grid13_p4` | $10$ | $0.245248$ | $2.65\%$ |
| `grid21_p4` | $15$ | $0.244123$ | $3.10\%$ |
| `grid13_p46` | $12$ | $0.244687$ | $2.87\%$ |

多 power variants 沒有突破 21-frequency single-power grid，顯示這個 family
在目前 metric 下開始飽和。

### 5.4 Joint dual

真正的 joint gate 結果是：

| model | raw $\alpha$ | safe $\alpha$ | safe $\lambda_{\min}$ |
|---|---:|---:|---:|
| baseline | $1.189562$ | $1.094781$ | $0.114990$ |
| `grid21_p4` | $1.176230$ | $1.088115$ | $0.114990$ |

raw improvement 為

$$
1-\frac{1.176230}{1.189562}
\approx1.1208\%.
$$

這比 uniform/core screen 的 $3.10\%$ 小很多。原因不是 screen 算錯，而是
joint dual 可把軸測度集中在 lift 沒有充分控制的位置，也可重新調整核心
測度。單一平均型 screen 無法代替 adversarial joint measure。

## 6. Polynomial-bump geometry sweep

### 6.1 掃描設計

為檢查 local dictionary 本身是否過窄，本節點掃描

$$
d\in\{10,12,14\},\quad
w\in\{1.2,1.5,2.0\},\quad
p\in\{3,4,5\},
$$

共 27 組。這裡 $d$ 控制每單位半徑的 local basis density，$w$ 控制 bump
width 相對 spacing，$p$ 控制 polynomial edge smoothness。

### 6.2 Screen 最佳值

最佳五組中，前三名為：

| geometry | dimension | threshold | tail $\lambda_{\min}$ |
|---|---:|---:|---:|
| `d12_w2_p5` | $190$ | $0.236986$ | $0.001150$ |
| `d14_w2_p5` | $222$ | $0.237848$ | $0.002317$ |
| `d10_w2_p4` | $158$ | $0.237886$ | $0.005438$ |

相較 baseline $0.251927$，screen 改善約 $5.9\%$。但最佳值伴隨極小 tail
eigenvalue，表示某些 directions 已接近 tail-null。這使 floating
optimization 更敏感，也暗示新增密度主要在開發窄弱方向。

### 6.3 Joint 結果

選取 `d10_w2_p4` 與 `d12_w2_p5` 做 joint pilot：

| geometry | raw $\alpha$ | safe $\alpha$ | safe $\lambda_{\min}$ | raw improvement |
|---|---:|---:|---:|---:|
| baseline | $1.189562$ | $1.094781$ | $0.114990$ | — |
| `d10_w2_p4` | $1.146055$ | $1.073027$ | $0.005438$ | $3.66\%$ |
| `d12_w2_p5` | $1.143522$ | $1.071761$ | $0.001151$ | $3.87\%$ |

兩者都有實質改善，但仍明確大於 $1$。因此

$$
\texttt{primal\_search\_started}=\texttt{false}.
$$

這不是保守過度：safe bound 已由序列化 measures 重新正規化並重建 PSD
matrix。四個 joint objects 的 minimum-eigenvalue 最大重建差約

$$
5.15\times10^{-16}.
$$

## 7. Dense complementary audit 與 peak migration

為避免只看 dual objective，本節點取 joint witness 的 complementary
rank-one direction，縮放到 4,941 點核心網格，再以軸步長 $0.025$ 計算完整
finite objective。

四個 scaled objectives 為

$$
1.275147,\quad1.254665,\quad1.265481,\quad1.263246.
$$

全部未通過 $1$。

各帶 maxima 顯示：

- baseline 遠帶 maxima 約在 $42.3$ 與 $82.9$；
- `grid21_p4` 約移到 $41.275$ 與 $81.875$；
- `d10_w2_p4` 約在 $43.35$ 與 $83.1$；
- `d12_w2_p5` 約移到 $36.325$ 與 $73.575$。

最佳幾何把 $A_3,A_4$ 的 maximum values 壓得很低，但 maxima 向帶左端移動；
與此同時 $A_1$ charge 約為 $0.8675$，仍是軸側主項。這顯示問題的核心不是
單獨消滅遠帶 harmonic-looking peaks，而是 target-near $A_1$ 與 off-axis
core normalization 的結構性競爭。

## 8. 本節點完成了什麼

### 8.1 正面成果

1. 把 12 份 sparse dual witnesses 轉成可重播的 peak atlas。
2. 找出並證明 homogeneous-notch subspace monotonicity。
3. 將 notch 設計從「刪方向」修正成「必須加外部方向」。
4. 實作一個具解析二階導數的 compact spectral lift family。
5. 完成 27 組 local geometry 與兩組 joint pilots。
6. 建立 peak migration stop audit。
7. 以 safe reconstructed dual gate 避免不具決策價值的 primal 與 prime
   matrix 計算。

### 8.2 負面但可用的結果

本節點沒有找到 finite-model gate crossing。但它排除了三種模糊說法：

- 「在峰上多放幾個零點應該就會好」；
- 「多加一些相似 Fourier atoms 應該終會過門檻」；
- 「只要 bump 更密、更寬、更平滑就能把軸能量壓掉」。

第一句在純齊次子空間情況下被 exact inclusion 排除；後兩句在已測範圍只顯示
飽和與 peak migration，不能再被當成無限加參數的理由。

## 9. 下一步：連續 Paley–Wiener extremal

### 9.1 問題重寫

固定 $R$，在適當的 real-even compact-support Hilbert domain 上考慮

$$
G(z)=\int_{-R}^{R}\psi(t)e^{izt}\,dt.
$$

定義

$$
\mathcal J_R(G)
=\mathcal T_R(G)
+\sum_{j=0}^{4}\underline N_j
  \sup_{x\in A_j}G(x)^2,
$$

並研究

$$
\Lambda_R
=\inf_G
\left\{
\mathcal J_R(G):
\sup_{z\in\mathcal P}2\operatorname{Re}G(z)^2\le-1,\ 
G(0)=G(i/2)=0
\right\}.
$$

這裡的第一個任務不是直接計算 $\Lambda_R$，而是先決定：

- $\psi$ 應位於哪個 Sobolev/domain，使 tail functional coercive；
- complex evaluation 與 derivative evaluation 的 reproducing kernels；
- 五帶 supremum 的 measure dual；
- existence、strong duality 與 complementary slackness 的條件；
- finite bump spaces 是否形成具誤差控制的 Galerkin sequence。

### 9.2 離散 witness 的新角色

v0.5 的 measures 不再只被看成「阻擋某個字典的數值輸出」，而可被當成
continuous KKT support 的候選近似。若 support locations 在加密 Galerkin
空間中穩定，而 dual values 收斂，可能導向解析 reproducing-kernel
inequality；若 values 下穿 $1$，則可反向找 continuous extremizer。

這比繼續盲目 dictionary search 更有辨識力：無論結果是 obstruction 或
construction，都要求一個可說明收斂與誤差的 continuous object。

### 9.3 v0.6 success gate

下一節點至少應完成下列之一：

1. 一個帶明確假設的解析 lower bound，能解釋 persistent dual block；
2. 一個具 convergence/error control 的 upper-bound construction，顯示某個
   $R\le16$ 可能有 $\Lambda_R<1$；
3. 一個 rigorous separating inequality，解決簡化的一帶一點核心問題。

在這三者之前，不擴建大型 prime matrices，也不把新的 coarse-grid
$\alpha<1$ 當成進展。

## 10. 信任邊界與禁止推論

### 10.1 證據層級

- E0：子空間 feasible-set inclusion 與指定 finite conic dual algebra。
- E1：檔案、schema、維度、row counts、重建與 false global flags 的自動檢查。
- E2：Fourier quadrature、KDE、optimization、eigenvalues 與 dense finite
  audits。
- E3：連續解析或 interval-certified transfer；本節點沒有 E3。

### 10.2 禁止推論

不能由本節點推出：

1. 所有 external notch dictionaries 都失敗；
2. continuous Paley–Wiener extremal value 必大於 $1$；
3. finite dual obstruction 證明或反證 RH；
4. 某個未被目前 witness 阻擋的 branch 一定 primal feasible；
5. 只檢查 target patch 就完成未知偏軸零點的全域 leakage budget；
6. 不經 argument principle 就能斷言 patch 中存在零點。

### 10.3 本節點的正式結論

最強且合法的結論是：

> 在明確指定的父有限空間中，純齊次 value/derivative notch 因子空間
> 單調性不可能改善 primal feasibility；在新增的 spectral-slope family
> 與 27 組 polynomial-bump geometries 中，最佳 joint raw dual 改善分別為
> $1.12\%$ 與 $3.87\%$，但所有 reconstructed safe lower bounds 仍大於
> $1$。因此停止這三條支線，轉向 continuous Paley–Wiener axis/core
> extremal formulation。

這個結論足以作為下一輪研究的乾淨交接，但不越過 RH 的解析信任邊界。
