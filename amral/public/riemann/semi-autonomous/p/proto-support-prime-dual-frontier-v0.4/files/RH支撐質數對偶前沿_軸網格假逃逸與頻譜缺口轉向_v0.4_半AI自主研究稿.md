# RH 支撐—質數對偶前沿

## 軸網格假逃逸、覆蓋式證書族與頻譜缺口轉向

版本：v0.4  
日期：2026-07-24  
研究模式：半 AI 自主數學研究  
技術研究主導與判斷：OpenAI Codex（AI 研究協作者）  
研究場域、授權與審閱：Neo.K / EveMissLab

## 摘要

本節點承接 v0.3 的交接，實作了「分帶、多測試函數、覆蓋式證書族」，
並把支撐半徑 $R$、basis 密度、basis 寬度、軸帶測度、patch 核心測度與
質數側成本放在同一個前沿上比較。

第一層 uniform 掃描包含

$$
14\times3\times3=126
$$

種幾何配置。若只看 18 個 patch 中心，第一個抽樣逃逸出現在 $R=10$；
若改看每個原始 patch 的 $3\times3$ 核心測度，第一個 uniform 逃逸延後
到 $R=14$。但這兩者都不是完整 dual gate，因為均勻軸測度可能嚴重低估
實軸峰值。

第二層將 18 個 patch 各切成 $4\times4$，得到 288 個子矩形，再對
$R=10.25,12,14,16$ 的困難候選共同最佳化五個軸帶測度與 $3\times3$
核心測度。四個半徑都找到安全下界大於預算 $1$ 的顯式有限模型
witness。各半徑的最強安全下界為

$$
2.6201,\quad1.8999,\quad1.3982,\quad1.0943.
$$

因此，這四個抽樣半徑都至少有一個子矩形無法由目前函數類達成
$J(A)<1$。這已足以否決「用同一 dictionary 單純增加支撐，替整個覆蓋
中的每一塊配置測試函數」這條有限模型路線。

本輪最重要的技術發現不是上述數值本身，而是軸網格混疊。在
$R=16$、patch `x4_Y3__r2_3` 上，步長 $0.25$ 給出

$$
\alpha=0.985277<1,
$$

看似通過 dual gate；將步長縮到 $0.1,0.05,0.025$ 後，結果依序回升為

$$
1.124306,\quad1.139551,\quad1.192293,
$$

最後的安全縮放仍有

$$
\alpha_{\mathrm{safe}}=1.096146>1.
$$

故粗網格的逃逸是可重播的假象，不是 primal 可行性的證據。

質數側的 exact support relation 為

$$
\operatorname{supp}\psi\subset[-R,R]
\quad\Longrightarrow\quad
m\log p<2R,
\quad p^m<e^{2R}.
$$

在 $R=10.25$，實際 segmented sieve 已枚舉到

$$
p^m<e^{20.5},
$$

包含 $41{,}141{,}456$ 個質數與 $41{,}144{,}807$ 個 prime-power
terms，耗時約 $4.50$ 秒。到 $R=16$，截斷升至

$$
78{,}962{,}960{,}182{,}680,
$$

質數數量的 $x/\log x$ 代理約為 $2.47\times10^{12}$。因此，即使更大
支撐最後可能削弱 dual 障礙，暴力增加 $R$ 已不是合理的下一步。

本節點的自主決策是：停止 support-only 擴張，下一節點改做
`RH_Axis_Notch_Cover_Codesign_v0.5`，直接共設計 dictionary、軸帶
spectral notches 與 patch 核心負向約束。這不是 RH 證明或反證；它是
對目前有限函數類與計算路線的可重播否決，以及一個研究方向轉換。

## 1. 本輪要回答的問題

v0.3 已證明在匯出的 $R=3$ 有理 surrogate 中，18 個 patch 都受到
dual lower bound $2$ 的阻擋。自然的下一個問題是：

> 增加支撐、增加測試函數自由度、細分覆蓋並讓 dual measure 自動選擇，
> 是否能在質數成本失控前穿過預算 $1$？

這個問題不能只用單一 patch 中心或固定均勻軸測度回答。若目標是對整個
區域

$$
\mathcal R=[20,20.5]\times[-0.2,-0.1]
$$

建立覆蓋式證書族，至少要同時處理：

1. patch 內多點負向，而非單一中心；
2. 五個實軸帶的最壞峰值，而非均勻平均；
3. $R$ 增加時的質數與 prime-power 截斷；
4. coarse grid 造成的假逃逸；
5. dual 未阻擋後，才有理由啟動 primal 搜尋。

## 2. 有限模型

### 2.1 測試函數座標

對每個半徑 $R$，在 $[-R,R]$ 上取實偶 compactly supported polynomial
bumps。basis 數量為

$$
n=\operatorname{round}(dR),
$$

其中密度 $d\in\{6,8,10\}$。施加兩個結構條件

$$
G(0)=0,\qquad G(i/2)=0
$$

後，以 $C_0$ Gram matrix whitening，得到約 $n-2$ 維座標。

本節點採用 Fourier convention

$$
G(w)=\int_{\mathbb R}\psi(t)e^{iwt}\,dt.
$$

令 $g(z)$ 為受限座標中的 transform row，定義

$$
C(z)=2\operatorname{Re}\!\left(g(z)g(z)^{\mathsf T}\right).
$$

對任意 $A\succeq0$，

$$
B_A(z)=\langle C(z),A\rangle
$$

表示偏軸核心值。實軸上 $g(x)$ 為實向量，故

$$
P(x)=g(x)g(x)^{\mathsf T}\succeq0,\qquad
H_A(x)=\langle P(x),A\rangle\ge0.
$$

### 2.2 分帶目標

實軸分成

$$
A_0=[14,18],\quad
A_1=[18,23],\quad
A_2=[23,35],\quad
A_3=[35,70],\quad
A_4=[70,145].
$$

令 $u_j$ majorize 第 $j$ 帶離散網格上的 $H_A$。有限 proxy objective
為

$$
J(A)=\langle T,A\rangle+\sum_{j=0}^{4}\underline N_j u_j,
$$

其中 $T\succeq0$ 是 tail prototype，$\underline N_j$ 是從 published
$S(T)$ profile 計算後向下截到 12 位小數的係數。

這個 $J$ 是目前程式中的 leakage upper-bound proxy，不是已經完成
interval transfer 的 zeta 顯式公式定理物件。

## 3. 多測度 dual witness

對每個軸帶選擇離散機率測度

$$
\mu_j=\sum_k\mu_{jk}\delta_{x_{jk}},
\qquad
\mu_{jk}\ge0,
\qquad
\sum_k\mu_{jk}=1.
$$

對 patch 中的核心點選擇

$$
\nu=\sum_q\nu_q\delta_{z_q},
\qquad
\nu_q\ge0,
\qquad
\sum_q\nu_q=1.
$$

定義

$$
B_\mu
=T+\sum_{j=0}^{4}
\underline N_j\sum_k\mu_{jk}P(x_{jk}),
$$

以及

$$
C_\nu=\sum_q\nu_qC(z_q).
$$

若存在 $\alpha>0$ 使

$$
W=B_\mu+\alpha C_\nu\succeq0,
$$

則對任何滿足

$$
A\succeq0,\qquad
\langle C(z_q),A\rangle\le-1
$$

的有限 primal 候選，有

$$
\begin{aligned}
J(A)
&\ge\langle B_\mu,A\rangle\\
&\ge-\alpha\langle C_\nu,A\rangle\\
&\ge\alpha.
\end{aligned}
$$

所以 $\alpha>1$ 直接否決該 patch 的預算 $J(A)<1$。這個推論只使用
PSD 錐自對偶性、非負機率權重與離散 primal constraints；它在指定的
有限模型內是代數邏輯。

程式以 generalized minimum eigenvalue 計算臨界值

$$
\alpha_*=-\frac{1}{
\lambda_{\min}(C_\nu,B_\mu)
}.
$$

若 $\alpha_*>1$，匯出值使用

$$
\alpha_{\mathrm{safe}}
=1+\frac{\alpha_*-1}{2},
$$

再直接檢查 $W_{\mathrm{safe}}$ 的最小特徵值。這是 floating safety
margin，不是 interval proof。

## 4. 掃描設計

第一層 uniform frontier 使用：

- 14 個半徑：
  $4.5,5,5.5,6,7,8,9,10,10.25,10.5,11,12,14,16$；
- 3 個 basis 密度：$6,8,10$；
- 3 個 width factors：$0.9,1.2,1.5$；
- 4 種分帶集合：tail-only、單帶 $A_1$、三帶 $A_0$ 至 $A_2$、
  五帶 $A_0$ 至 $A_4$；
- 18 個原始 patch 中心；
- 每個原始 patch 的 uniform $3\times3$ 核心測度。

第二層 joint dual 固定 uniform frontier 中較強的 dictionary：

$$
d=10,\qquad\text{width factor}=1.5.
$$

每個原始 patch 切為 $4\times4$，總數為

$$
18\cdot16=288.
$$

joint 搜尋以 uniform ranking 選出最困難的

$$
2+2+3+5=12
$$

個子矩形，對五帶軸測度與 $3\times3$ 核心測度做 cutting-plane
最佳化。這不是 288 個子矩形的完整 joint exhaustion；但若其中任一
patch 已有 $\alpha_{\mathrm{safe}}>1$，目前覆蓋式策略便不能在該半徑
完成。

## 5. Uniform frontier

每個半徑下，原始 patch uniform $3\times3$ 的最佳最大 threshold 為：

| $R$ | density | width factor | dimension | patch 最大 threshold |
|---:|---:|---:|---:|---:|
| $9$ | $10$ | $1.5$ | $88$ | $1.570260$ |
| $10$ | $10$ | $1.5$ | $98$ | $1.478511$ |
| $10.25$ | $10$ | $1.5$ | $100$ | $1.464445$ |
| $12$ | $10$ | $1.5$ | $118$ | $1.152840$ |
| $14$ | $10$ | $1.5$ | $138$ | $0.540797$ |
| $16$ | $10$ | $1.5$ | $158$ | $0.414010$ |

這張表顯示支撐增加確實降低 uniform witness threshold。但是「低於 $1$」
只代表指定均勻測度沒有找到阻擋，不能推出 primal feasible。

兩個容易混淆的 transition 是：

$$
R=10
$$

第一次出現某個 geometry 的 18 個中心都低於 $1$；而

$$
R=14
$$

第一次出現某個 geometry 的 18 個原始 patch uniform $3\times3$
threshold 都低於 $1$。joint measure optimization 隨後推翻了把這些
transition 當成可行門檻的解讀。

## 6. Joint dual 結果

| $R$ | dimension | 搜尋 patch 數 | 最強 raw $\alpha$ | 最強 $\alpha_{\rm safe}$ | safe $\lambda_{\min}$ |
|---:|---:|---:|---:|---:|---:|
| $10.25$ | $100$ | $2$ | $4.240160$ | $2.620080$ | $0.0713394$ |
| $12$ | $118$ | $2$ | $2.799900$ | $1.899950$ | $0.0834713$ |
| $14$ | $138$ | $3$ | $1.796359$ | $1.398180$ | $0.0992519$ |
| $16$ | $158$ | $5$ | $1.188563$ | $1.094281$ | $0.1149902$ |

12 份序列化 sparse-measure witness 全部由
`verify_saved_witnesses.py` 重建。將每組序列化非負權重重新正規化為
總和 $1$ 後：

- 12 張 witness 全部保持 PSD；
- 12 個有效 dual lower bounds 全部大於 $1$；
- 重建與儲存最小特徵值的最大差為約
  $1.3\times10^{-15}$。

這些是 E2 floating finite-model 結果。v0.4 沒有把矩陣轉成有理數，也
沒有 interval-enclose Fourier quadrature。

## 7. 軸網格假逃逸

在 $R=16$、patch `x4_Y3__r2_3` 上做固定配置的網格細化：

| 軸步長 | raw $\alpha$ | $\alpha_{\rm safe}$ | safe $\lambda_{\min}$ |
|---:|---:|---:|---:|
| $0.25$ | $0.985277$ | $0.980351$ | $0.0346388$ |
| $0.1$ | $1.124306$ | $1.062153$ | $0.1149901$ |
| $0.05$ | $1.139551$ | $1.069775$ | $0.1149901$ |
| $0.025$ | $1.192293$ | $1.096146$ | $0.1149901$ |

每個離散測度自身都是有效 lower-bound witness；步長縮小會擴大可搜尋的
測度支撐，因此 lower bound 上升並不矛盾。粗網格只在錯誤位置採樣了
實軸波形，漏掉窄峰。

這帶來一條新的方法規則：

> 任何 $\alpha<1$ 的「dual 逃逸」都必須接受更密軸網格或連續 supremum
> 上界審計；反之，某個已重建且 PSD 的 $\alpha>1$ witness 不需要證明
> dual 最佳性，就足以否決該有限 primal 分支。

因此 dual 的兩側不對稱：

- 找到 $\alpha>1$ 是正面否決證據；
- 找不到 $\alpha>1$ 只是搜尋失敗，不是可行性證明。

## 8. Primal gate

本節點採用以下閘門：

$$
\text{只有所有已搜尋困難 patch 都未被安全 dual witness 阻擋時，}
\quad\text{才啟動高成本 primal 搜尋。}
$$

四個半徑都未通過此閘門。因此沒有生成 ray-cone primal Gram 候選。
`primal_diagnostics.json` 只保存 complementary rank-one direction 的
dense audit；其 scaled objectives 分別約為

$$
4.4040,\quad2.9649,\quad1.8478,\quad1.2832,
$$

全部大於 $1$。這些方向只是診斷，不是完整 primal infeasibility proof；
真正的否決來自已匯出的 PSD dual witnesses。

## 9. 支撐與質數成本

由

$$
\operatorname{supp}\psi\subset[-R,R]
$$

可知自相關支撐包含於 $[-2R,2R]$。顯式公式中位於
$m\log p$ 的 prime-power term 只有在

$$
m\log p<2R
$$

時可能出現，等價於

$$
p^m<e^{2R}.
$$

這個截斷關係是有限構造中的 exact support statement。實際成本如下：

| $R$ | strict cutoff | 質數數量 | prime-power terms | 狀態 |
|---:|---:|---:|---:|---|
| $3$ | $403$ | $79$ | $98$ | 實枚舉 |
| $7$ | $1{,}202{,}604$ | $93{,}117$ | $93{,}371$ | 實枚舉 |
| $8.5$ | $24{,}154{,}952$ | $1{,}516{,}233$ | $1{,}517{,}020$ | 實枚舉 |
| $9$ | $65{,}659{,}969$ | $3{,}877{,}186$ | $3{,}878{,}366$ | 實枚舉 |
| $10.25$ | $799{,}902{,}177$ | $41{,}141{,}456$ | $41{,}144{,}807$ | 實枚舉 |
| $12$ | $26{,}489{,}122{,}129$ | 約 $1.10\times10^9$ | 未枚舉 | $x/\log x$ 代理 |
| $14$ | $1{,}446{,}257{,}064{,}291$ | 約 $5.17\times10^{10}$ | 未枚舉 | $x/\log x$ 代理 |
| $16$ | $78{,}962{,}960{,}182{,}680$ | 約 $2.47\times10^{12}$ | 未枚舉 | $x/\log x$ 代理 |

程式把 prime-power coefficients 線性沉積到寬度 $0.01$ 的 log bins。
這會把後續矩陣更新數從每個 prime-power 一次降成每個 bin 一次，但：

1. 它沒有消除質數枚舉；
2. 尚未提供 bin interpolation 的 interval error；
3. $R=12,14,16$ 只做成本投影，沒有建出完整 arithmetic matrix。

所以 histogram 是工程壓縮，不是證書壓縮。

## 10. 來源修正

上一節點沿用了 arXiv abstract 的

$$
|S(T)|
\le0.111\log T+0.275\log\log T+2.450.
$$

本節點改用 Trudgian 在 *Journal of Number Theory* 版本摘要中的
conservative constants：

$$
|S(T)|
\le0.112\log T+0.278\log\log T+2.510,
\qquad T\ge e.
$$

五帶 floating count profiles 因此全部小幅上升。本節點使用 published
profile，但仍未做 directed rounding 或 theorem-hypothesis checker。

## 11. 決策

數據支持三個結論：

1. 增大 $R$ 的確削弱固定均勻 dual witness；
2. 共同最佳化軸測度後，$R\le16$ 的 sampled support-only 路線仍被擋住；
3. 質數側成本以 $e^{2R}$ 擴張，繼續盲目增加 $R$ 的回報太差。

因此下一輪不再把 $R=18,20,\ldots$ 當成主要搜索軸。更好的方向是讓
dictionary 本身主動壓低五帶峰值：

$$
\min_{\mathcal D,A}
\left[
\langle T_{\mathcal D},A\rangle
+\sum_j\underline N_j
\sup_{x\in A_j}H_{\mathcal D,A}(x)
\right]
$$

同時保持 patch 核心負向：

$$
\sup_{z\in P}B_{\mathcal D,A}(z)\le-1.
$$

這是 dictionary、spectral notch 與 cover 的共設計問題，而不是單一
Gram rank 或單一半徑問題。

## 12. 下一節點

下一節點命名為：

`RH_Axis_Notch_Cover_Codesign_v0.5`

最低交付標準：

1. dictionary 中加入可控的軸帶 notch constraints 或 null directions；
2. 以 adaptive maximization 找每帶真正峰值，不使用固定粗網格作通過
   判定；
3. 先在 $R\in\{10.25,12,14,16\}$ 重用現有前沿，不向更大支撐擴張；
4. 至少讓一個目前 blocked patch 的安全 dual bound 降到 $1$ 以下；
5. dual 未阻擋後，再做 primal Gram、dense core 與 guard-ring audit；
6. arithmetic histogram 必須附可驗證的 interpolation error，否則不得
   升格為證書。

停止規則也必須明確：若 notch co-design 只能把軸峰移到鄰帶、或使 core
負向同步崩潰，便停止這個 dictionary family，轉向解析 kernel family，
而不是繼續增加維度。

## 13. 信任邊界

本節點建立的是：

- 有限模型內的 dual implication；
- 126 組 uniform frontier；
- 288 子矩形的結構覆蓋；
- 12 份可重建 floating dual witnesses；
- 一個軸網格假逃逸反例；
- $R=10.25$ 的真實質數枚舉 benchmark；
- $R=12,14,16$ 的成本投影。

本節點沒有建立：

- Fourier quadrature 的 interval enclosure；
- 連續軸 supremum 的上界證書；
- 完整 288 patch joint exhaustion；
- theorem-certified tail matrix；
- arithmetic histogram 的 interpolation error；
- 未知偏軸區域的完整 leakage budget；
- 任何零點存在的 argument-principle certificate；
- 從局部 patch 到 RH 的全域矛盾；
- RH 證明、RH 反證或等價判準證明。

因此本稿的正確讀法是：

> 目前 support-only finite-model strategy 在抽樣到 $R=16$ 時仍有明確
> dual obstruction，且更大支撐的質數成本快速失控；下一步應改變
> dictionary 的頻譜幾何。

不能把它改寫成：

> 所有大支撐測試函數都失敗，或 RH 已被判定。
