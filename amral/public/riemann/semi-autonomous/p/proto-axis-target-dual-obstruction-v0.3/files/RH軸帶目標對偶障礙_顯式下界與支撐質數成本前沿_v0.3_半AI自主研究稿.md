# RH 軸帶目標對偶障礙

## 顯式下界、$R=3$ 函數類否決與支撐—質數成本前沿

版本：v0.3  
日期：2026-07-24  
研究模式：半 AI 自主數學研究  
技術研究主導與判斷：OpenAI Codex（AI 研究協作者）  
研究場域、授權與審閱：Neo.K / EveMissLab

## 摘要

本節點承接 v0.2 的決策：停止對同一個 primal Gram 模型做無方向的
rank 擴張，轉而尋找實軸帶 $[18,23]$ 所強迫的 dual 下界。結果比原先
預期更簡單，也更具決策力。

對目標矩形

$$
[20,20.5]\times[-0.2,-0.1]
$$

的 18 個覆蓋 patch，本節點在每個 patch 的有理中心 $z_P$ 建立矩陣

$$
W_P=10^{-3}T+M_1+2C(z_P),
$$

其中 $T$ 是尾項矩陣，$M_1$ 是 $[18,23]$ 上 26 點均勻測度所形成的
實軸矩陣，而 $C(z_P)$ 是偏軸核心矩陣。18 張 $W_P$ 在 floating 模型中
全部正定；最小特徵值落在

$$
[3.1042101910,3.1042422675]\times10^{-5}.
$$

將尾矩陣與 transform 向量逐項轉成 12 位十進有理數後，18 張矩陣亦
全部通過 exact rational $LDL^{\mathsf T}$ 正樞軸檢查。因此，在匯出的
有限有理 surrogate 內，任何滿足

$$
A\succeq0,\qquad \langle C(z_P),A\rangle\le-1
$$

的候選，都有分帶目標值

$$
J(A)\ge2.
$$

原目標要求 $J(A)<1$，故目前 $R=3$、24-bump、22 維受限座標的
patchwise 函數類在這個有限模型中被否決。這不是 RH 證明、不是 RH
反證，也不是對所有可容許測試函數的否決。

支撐半徑診斷則顯示：在每單位約 8 個 bumps 的固定密度下，第一個有
patch 逃離尾項單點障礙的抽樣半徑為 $R=5.1$；到抽樣序列的
$R=8.5$ 起，18 個 patch 中心才在後續樣本上穩定全部逃離。相對
$R=3$，其質數截斷代理

$$
e^{2R}
$$

增加約 $e^{11}=59874.14$ 倍。下一節點因此應研究「支撐—質數 dual
frontier」，而不是再做同一支撐下的高 rank 搜尋。

## 1. 問題由來

v0.2 已經把 72 條既有 rank-one rays 擴張成完整 PSD Gram 變數。交叉項
平均改善約 $21.08\%$，但 sampled axis-plus-tail 仍至少是預算的
$64.60$ 倍，而且所有四個代表 patch 的 rank $1,2,4,8$ 搜尋都數值
坍縮回 rank one。更重要的是，$[18,23]$ 在全部 18 個 patch 都是最大
實軸 charge。

這留下兩種可能：

1. primal 搜尋器尚未找到真正好的方向；
2. $R=3$ 的整個受限函數類本身就被實軸與尾項的幾何關係阻擋。

本節點用 dual witness 區分兩者。結果支持第二種解釋。

## 2. 有限 PSD 模型

模型使用 $[-3,3]$ 上 24 個實偶 polynomial bumps，數值積分步長
$0.01$。施加

$$
G(0)=0,\qquad G(i/2)=0
$$

兩個結構條件後，得到 22 維 $C_0$-whitened 座標。已知 zeta 零點縱座標
完全不參與本節點的構造或選擇。

令 $g(z)\in\mathbb C^{22}$ 為 transform row，並定義

$$
C(z)=2\operatorname{Re}\!\left(g(z)g(z)^{\mathsf T}\right).
$$

對 $A\succeq0$，

$$
B_A(z)=\langle C(z),A\rangle
$$

是偏軸核心值。實軸上 $g(x)$ 為實向量，令

$$
P(x)=g(x)g(x)^{\mathsf T},\qquad
H_A(x)=\langle P(x),A\rangle\ge0.
$$

五個實軸帶仍為

$$
[14,18],\ [18,23],\ [23,35],\ [35,70],\ [70,145].
$$

若 $u_j$ majorize 第 $j$ 帶網格上的 $H_A$，有限 primal 目標寫成

$$
J(A)=\langle T,A\rangle+\sum_{j=0}^{4}\widehat N_j u_j,
$$

其中 $T\succeq0$ 是 prototype tail matrix，而 $\widehat N_j$ 是繼承的
floating zero-count majorant。

## 3. 對偶下界

只取第二帶 $A_1=[18,23]$。令

$$
\mathcal G_1=\{18,18.2,\ldots,23\},\qquad |\mathcal G_1|=26,
$$

並將原 floating count $7.113998598824585$ 向下截為

$$
\underline N_1=7.113998598824.
$$

定義

$$
M_1=
\frac{\underline N_1}{26}
\sum_{x\in\mathcal G_1}P(x).
$$

對任意 primal-feasible $A$，因 $u_1$ majorize 全部網格值、
$H_A(x)\ge0$、$\underline N_1\le\widehat N_1$，且
$0<\rho\le1$，有

$$
\begin{aligned}
J(A)
&\ge \rho\langle T,A\rangle+\langle M_1,A\rangle\\
&=\langle \rho T+M_1,A\rangle.
\end{aligned}
$$

現在固定一個 patch $P$ 的有理中心 $z_P$。若存在 $\alpha>0$ 使

$$
W_P=\rho T+M_1+\alpha C(z_P)\succeq0,
$$

則 PSD 錐的自對偶性給出

$$
0\le\langle W_P,A\rangle
=\langle\rho T+M_1,A\rangle
+\alpha\langle C(z_P),A\rangle.
$$

因此，只要 patchwise 候選必須在中心滿足

$$
\langle C(z_P),A\rangle\le-1,
$$

便有

$$
J(A)\ge-\alpha\langle C(z_P),A\rangle\ge\alpha.
$$

這裡只檢查中心不是漏洞：要求整個 patch 都小於等於 $-1$ 的候選必然也
滿足中心約束。對「否決」而言，一個必要條件已足夠。

## 4. 顯式 witness family

本節點採用同一組 axis measure 與 tail fraction：

$$
\rho=10^{-3},\qquad \alpha=2,
$$

並只讓 $C(z_P)$ 隨 18 個 patch 中心改變。故證書族是

$$
\left\{
10^{-3}T+M_1+2C(z_P)
:\ P\in\mathcal P_{18}
\right\}.
$$

這是一個「分帶、多測試函數、覆蓋式證書族」的 dual 化版本：

- 分帶：只需 $[18,23]$ 的非負均勻測度，再加極小尾項；
- 多測試函數：$A\succeq0$ 已同時涵蓋受限空間中任意有限 PSD Gram
  組合，不再侷限於既有 rays；
- 覆蓋式證書族：18 個 patch 各有一張中心 witness。

原計畫考慮 SDP cutting-plane 搜尋。但 runtime 沒有 convex SDP solver，
而直接測試最簡單的均勻帶測度後即得到嚴格正定 witness，故沒有必要用
更複雜的數值最佳化來製造同一結論。

## 5. 驗證結果

### 5.1 Floating matrix check

18 張 primary witness 的最小特徵值範圍為

$$
3.1042101910186086\times10^{-5}
\le\lambda_{\min}(W_P)\le
3.1042422674836540\times10^{-5}.
$$

將 $\rho$ 降到 $10^{-6}$，18 張仍通過，最小特徵值範圍為

$$
[1.6148647147,3.1044753831]\times10^{-8}.
$$

$\rho=0$ 的 axis-only 矩陣則出現

$$
\lambda_{\min}\in
[-1.1127262618\times10^{-6},-2.4418929376\times10^{-17}],
$$

因此本節點不宣稱純 $A_1$ witness；尾項在近零方向上提供必要的
regularization。極小負值究竟有多少來自真實幾何、多少來自病態數值，
留待 interval 或高精度分析。

### 5.2 Exact rational surrogate

匯出的 `outputs/rational_model.json` 保存：

- 12 位十進有理 tail matrix；
- 向下截斷的 $\underline N_1$；
- 26 個實軸 transform vectors；
- 18 個核心 transform 的實部與虛部；
- $\rho=1/1000$ 與 $\alpha=2$。

由向量重新形成

$$
P=gg^{\mathsf T},\qquad
C=2(rr^{\mathsf T}-ii^{\mathsf T}),
$$

再以 Python `Fraction` 執行不選 pivot 的 exact
$LDL^{\mathsf T}$。有理 tail matrix 與 18 張 witness 的 22 個 pivots
全部嚴格為正；全族最小 pivot 的 floating 顯示值為

$$
3.240761260825524\times10^{-5}.
$$

在 6、8、10、12 位十進有理化下也全部通過。這建立的是匯出有限
surrogate 的 exact algebraic positivity；它不自動把數值積分、
zero-count bound 或 tail theorem 升級為形式證明。

### 5.3 Parent primal cross-check

把 v0.2 的 18 張已存 Gram matrices 代回 witness：

- 18 個 $\langle W_P,A_P\rangle$ 全部非負；
- 對偶子目標全部至少為 $2$；
- pairing 範圍為 $[9.51235,28.15543]$；
- 恆等式殘差絕對值最大為 $1.07\times10^{-14}$。

這說明 v0.2 大幅超支不是該非凸搜尋器偶然漏掉一個低成本 rank；它與
本節點辨識出的錐幾何障礙一致。

## 6. 穩定性與支撐半徑診斷

Primary witness 在下列擾動全部保持 18/18 通過：

- transform quadrature step：$0.02,0.015,0.01,0.0075$；
- axis grid step：$0.2,0.1,0.05,0.025,0.0125$；
- 十進有理化：6、8、10、12 位。

這支持「$R=3$ rejection 不是單一 mesh 偶然」的 E2 判斷。

接著保持每單位約 8 個 bumps，掃描 $R\in[2,10]$，計算只靠 tail
matrix 的單點最佳 dual threshold。結果：

| 診斷事件 | 抽樣半徑 | $e^{2R}$ 代理 | 相對 $R=3$ |
|---|---:|---:|---:|
| 全部 patch 仍被 tail 單點障礙殺死 | $R=5.0$ | $22026.47$ | $54.60$ |
| 首次有 patch 逃離 | $R=5.1$ | $26903.19$ | $66.69$ |
| 後續抽樣中 18 中心穩定全逃離 | $R=8.5$ | $24154952.75$ | $59874.14$ |

$R=8.4$ 曾短暫全通過、$R=8.45$ 又反彈，顯示固定 bump 密度的 basis
discretization 仍會造成非單調性。因此 $R=8.5$ 不是臨界常數，只是目前
抽樣序列的穩定轉折點。即使中心 tail bound 小於 $1$，也不代表已找到
patchwise primal 可行解；它只表示這個特定單點 dual obstruction 已退去。

## 7. 研究判斷

本節點給出三個明確決策。

第一，v0.2 所用的 $R=3$ 函數類應退休。更高 rank 無法繞過一張直接作用
在整個 PSD 錐上的 witness。

第二，擴大支撐確實可能鬆動障礙，但代價不是免費的。若顯式公式的質數側
工作量隨 $e^{2R}$ 增長，從 $R=3$ 到診斷上的 $R=8.5$ 會把截斷代理放大
約六萬倍。

第三，下一個問題不應只問「哪個 $R$ 可行」，而應同時問：

$$
\text{dual lower bound}
\quad\text{vs.}\quad
\text{prime-side cost}
\quad\text{vs.}\quad
\text{theorem-certification cost}.
$$

因此下一節點定為

`RH_Support_Prime_Dual_Frontier_v0.4`。

它應先在 $R\in[4.5,9]$ 建立多 basis-density、多字典的 parametric dual
frontier；只有通過 dual gate 的半徑才啟動昂貴 primal 與質數側計算。
同時把 $A_1$ count 與 tail prototype 替換成具來源、可 interval
enclose 的 theorem objects。這比盲目擴張 rank 或直接衝到大質數截斷更
節省資訊成本。

## 8. 信任邊界

本節點成立的最強敘述是：

> 在匯出的十進有理有限 surrogate 中，18 個 patch 中心各有 exact
> rational PSD dual witness，迫使有限目標至少為 $2$；對原 floating
> discretization，網格與精度擾動提供一致的 E2 支持。

本節點沒有建立：

- exact Fourier integral 與匯出有理 transform 的 interval transfer；
- theorem-backed zero-count majorant；
- theorem-backed tail inequality；
- 未知偏軸零點區域的完整符號預算；
- patch 內零點存在性或 winding certificate；
- 局部到全臨界帶的 ZFC 邏輯閉合；
- RH 證明、RH 反證或等價判準的證明。

詳細聲明見 `TRUST_BOUNDARY.md`、`metadata/claim_register.json` 與
`metadata/gap_ledger.json`。

## 9. 可重播物件

主要機器可讀輸出為：

- `outputs/experiment_summary.json`
- `outputs/witness_summary.csv`
- `outputs/witnesses/*.witness.json`
- `outputs/rational_model.json`
- `outputs/rational_verification.json`
- `outputs/sensitivity.json`

核心程式為：

- `run_dual_experiment.py`
- `verify_rational_witnesses.py`
- `run_sensitivity.py`
- `validate_package.py`

本節點的技術研究選擇、數學詮釋與下一節點決策均歸屬 AI 研究判斷；
Neo.K / EveMissLab 提供研究場域、授權與審閱脈絡。
