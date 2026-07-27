# Method

## 1. 父節點與固定幾何

父節點為 `RH-SupportPrime-DualFrontier-20260724-v0.4`。本節點直接保存其
12 份 sparse joint-dual witnesses，並固定目標矩形

$$
\mathcal R=[20,20.5]\times[-0.2,-0.1].
$$

主要 joint pilot 使用 $R=16$ 的困難子矩形 `x4_Y3__r3_3`：

$$
x\in[20.395,20.42],\qquad
y\in[-0.10625,-0.1].
$$

軸側仍分為五帶：

$$
A_0=[14,18],\quad A_1=[18,23],\quad A_2=[23,35],
$$

$$
A_3=[35,70],\quad A_4=[70,145].
$$

## 2. Witness peak atlas

每份 witness 的每一帶先將非負 support weights 正規化為機率測度；每份
witness 在每一帶獲得相同總權重，再以固定 bandwidth 的 Gaussian KDE
聚合。這只是一個探索性 atlas，不是連續軸極值證書。

得到的主峰為

$$
(17.83,\ 20.38,\ 23.24,\ 42.18,\ 83.05).
$$

其中 $A_1$ 主峰落在目標矩形的實部區間內，而

$$
\frac{42.18}{20.38}\approx2.0697,\qquad
\frac{83.05}{20.38}\approx4.0751.
$$

## 3. Taylor 缺口直覺

對實軸上為實值的 entire transform $G$，若 $G(x_0)=0$，則

$$
G(x_0+iy)
=iyG'(x_0)+O(y^2),
$$

所以

$$
G(x_0+iy)^2
=-y^2G'(x_0)^2+O(|y|^3).
$$

這說明「value notch 保留 slope」可能在偏軸核心產生局部負方向；
相反地，同時要求 $G'(x_0)=0$ 會消除這個二階負項。

## 4. 子空間單調性

令 $V$ 是父節點的有限測試函數空間，$\mathcal F(V)$ 是使用 $V$ 所形成的
PSD Gram feasible set。加入齊次 value 或 derivative notch 後得到
$V'\subseteq V$，因而

$$
\mathcal F(V')\subseteq\mathcal F(V).
$$

對同一個最小化目標 $J$，

$$
\inf_{A\in\mathcal F(V)}J(A)
\le
\inf_{A\in\mathcal F(V')}J(A).
$$

因此，若完整 $V$ 已經被 dual witness 證明 $J(A)\ge1$，只用齊次約束縮小
到 $V'$ 不可能解除該 obstruction。這是有限模型內的 exact inclusion
statement，不依賴浮點實驗。

## 5. 外部 spectral-slope lift

要避開上述障礙，必須加入父空間之外的新方向。本節點測試

$$
\psi_{\omega,p}(t)
=t\left(1-\frac{t^2}{R^2}\right)_+^p\sin(\omega t),
\qquad p\ge3.
$$

它是 real、even、compactly supported，且其 Fourier transform 在
$\omega$ 附近提供可調 slope-like 行為。程式使用解析二階導數建立 tail
matrix，避免對新 atom 做數值微分。

## 6. 幾何與 dual gate

測試三類 density、三類 width factor 與三類 bump power：

$$
d\in\{10,12,14\},\quad
w\in\{1.2,1.5,2.0\},\quad
p\in\{3,4,5\},
$$

共 27 組。uniform/core screen 只用來排序；真正的停止條件來自 joint
dual witness。若正規化非負軸測度 $\mu_j$ 與核心測度 $\nu$ 使

$$
W
=T+\sum_j\underline N_j\int P_x\,d\mu_j(x)
+\alpha\int C_z\,d\nu(z)
\succeq0,
$$

則對指定 finite primal feasible $A$，

$$
J(A)\ge\alpha.
$$

序列化後採保守係數 $\alpha_{\rm safe}$ 重新建矩陣。只有
$\alpha_{\rm safe}<1$ 且通過加密軸審計時，才允許啟動 primal Gram
搜尋。本節點所有 joint candidates 都不通過這個 gate。

## 7. Peak migration audit

對 baseline、最佳 lift 與兩個最佳幾何，另取 complementary rank-one
方向，在 4,941 個核心點與軸步長 $0.025$ 上重算。審計同時記錄各帶最大值
位置，以偵測「壓低一個峰、卻把能量移到鄰帶或帶邊界」的假進展。
