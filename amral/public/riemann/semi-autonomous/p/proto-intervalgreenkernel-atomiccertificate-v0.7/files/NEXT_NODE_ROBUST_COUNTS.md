# Next Node: Robust Band Counts and Zeta Coefficient Bridge v0.8

## Node

`RH-RobustBandCounts-ZetaBridge-20260725-v0.8`

## Why this node changed

原計畫是在 Layer A 成功後直接 interval-certify tail 與五個 count
coefficients。但 v0.7 證明既有 coefficients 是 upper profiles，而非
目前 argument bound 能保證的 lower profiles。

因此 v0.8 不能只做 directed rounding；它必須先確認不等式方向。

## Primary question

在原始 explicit-formula／separation 推導中，band coefficient $N_j$ 究竟
扮演：

1. positive contribution 的 guaranteed lower multiplicity；
2. adverse contribution 的 upper budget；
3. normalized probability mass 的 scaling surrogate；
4. 或前幾輪中混合了不同語義？

沒有完成這個 theorem-object audit 前，不允許重用 `count_majorant`
名稱下的數值。

## Robust formulation

對每一帶建立

$$
N_j\in[L_j,U_j].
$$

若 axis operators $P_j\succeq0$ 且以正號進入，

$$
W(N)
=
I+\sum_j N_jP_j+\alpha C,
$$

則

$$
W(N)\succeq W(L).
$$

因此 robust worst case 是 lower endpoint vector $L$，而不是 upper
endpoint vector $U$。

## Three branches

### Branch A：證明 upper profile 的方向其實合法

逐行重建原 separation inequality。若 band majorant 位於一個需要上界的
負向或 error-budget term，建立明確的 operator monotonicity theorem，
不得只靠變數名稱推測。

### Branch B：建立 validated lower counts

若 positive axis term 確實需要 lower multiplicity，則需取得：

- endpoint nonzero certificates；
- interval Riemann–Siegel $\theta$；
- interval $S(T)$ bounds；
- 或直接的 argument-principle／Turing zero-count certificate。

前 $3$ 帶僅靠目前 absolute-$S$ bound 得不到正下界，可能必須加入
validated zero presence。

### Branch C：重新設計 dual

若不希望依賴 known zero ordinates，尋找對

$$
N_0=N_1=N_2=0
$$

仍可達成的 robust multi-test witness，或改變 bands、core measures 與
tail allocation。

v0.7 的固定 witness 在目前 lower profile 下不存活，因此需要重新最佳化，
不能只換係數。

## Tail track

tail coefficient 可平行處理，但不得掩蓋 count direction blocker：

1. 封裝來源 theorem 與適用條件；
2. interval-evaluate finite shells；
3. 對 improper continuation 給解析上／下界；
4. 證明 rational $\kappa$ 的正確單調方向。

## Deliverables

1. `coefficient_semantics_theorem.md`
2. 每帶的 `count_interval_certificate.json`
3. endpoint convention 與 nonzero status
4. robust lower-endpoint optimizer
5. robust interval Schur certificate 或正式失敗證書
6. tail theorem object
7. 更新後的 gap dependency graph

## Stop rules

- 不把 upper count majorant 當 lower count。
- 不以向下取整修補 inequality direction。
- 不使用未驗證 zero tables。
- 不在 robust single-patch bridge 成立前擴張完整 cover family。
- 不把 Layer A theorem 寫成 RH 結論。

## Return to the original program

只要 v0.8 建立 zeta-facing robust single-patch certificate，下一階段再回到：

$$
\text{分帶}
\;+\;
\text{多測試函數}
\;+\;
\text{覆蓋式證書族}.
$$
