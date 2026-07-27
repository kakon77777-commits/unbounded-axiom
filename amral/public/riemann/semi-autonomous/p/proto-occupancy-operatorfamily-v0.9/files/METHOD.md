# Method

## 1. 定義先行

本輪先固定三個不可互換的物件：

1. scalar count lower bound；
2. cell occupancy certificate；
3. universal uncertain-location operator family。

只有第 $2$ 項加第 $3$ 項能使用
`OccupancySelectionOperatorTransfer` 接到實際 configuration。程式輸出
與 metadata 都禁止把第 $1$ 項改名後當成第 $2$ 項。

## 2. 精確有理 Green prototype

`occupancy_cert/rational_interval.py` 只使用 Python `Fraction`。每個
interval endpoint 都是精確有理數，四則運算取所有端點組合；平方在跨越
$0$ 時把 lower endpoint 固定為 $0$。

`occupancy_cert/dirichlet_green.py` 使用

$$
K(s,t)=\min(s,t)-st.
$$

若兩個 cell 有固定左右順序，程式使用

$$
K(s,t)=s(1-t)
$$

的雙線性 interval enclosure。若一個變數跨越固定 target，程式在 target
處分片後取 hull。

正向與負向 ranks 都固定為 $2$。每個 box 先建立

$$
A=D_\lambda^{-1}+K_{XX},
$$

再用 $2\times2$ interval adjugate enclosure 求 $A^{-1}$，最後建立
$2\times2$ Schur family。

## 3. 自適應覆蓋

根盒為兩個 occupancy hull 的 Cartesian product。每個 node：

1. 重算完整 interval Schur proof；
2. 若 $S_{11}$ 與 $\det S$ 的 lower bounds 都正，成為 certified leaf；
3. 否則沿最寬座標二分；
4. 寬度相同時選最小座標 index；
5. 每個 split 使用精確中點。

輸出保留完整 tree path、box、split dimension、midpoint、positive-system
determinant 與 Sylvester intervals。獨立 verifier 以同一輸入從頭再生
certificate，並另外檢查 leaf paths 的 prefix-free 性質、無 unresolved
leaves、全部 global flags 為 false。

## 4. Count-only 反例

`occupancy_cert/semantics.py` 把兩個點都放在 $1/5$，以精確
$2\times2$ algebra 重算 Schur matrix、determinant 與負二次型方向。
反例輸出不使用浮點數。

## 5. Clamped Green 微半徑證書

本輪把 v0.7 的 rational witness 與 interval certificate 作為鎖定的 parent
dependency 複本。驗證器檢查：

- parent witness 的 canonical hash；
- parent certificate 中的 witness hash；
- parent abstract interval flags；
- parent global RH flag 為 false；
- 五組 axis probability weights 各自精確和為 $1$。

本節點不重寫 v0.7 的 directed-decimal transcendental verifier。完整
parent interval replay 的所有權仍在 v0.7；v0.9 只證明從該已驗證命題到
位置微擾 family 的新推論。

新推論全部使用 `Fraction`：

- $\alpha$ convex margin；
- 兩次 Poincaré upper bound；
- rank-one perturbation budget；
- $58$ 個 cell endpoints；
- coercivity lower bound；
- 此 proof budget 的 critical uniform radius。

半徑 $2.5\times10^{-15}$ 的 probe 超出目前 budget，只標為
`budget failure`，不標為 operator counterexample。

## 6. 浮點對抗診斷

`occupancy_cert/floating_clamped.py` 使用 NumPy 與 SciPy：

- trapezoid reconstruction of the clamped $D^4$ inverse；
- structural densities $1$ 與 $\cosh(t/2)$ 的 projection；
- projected Gram eigenfactorization；
- generalized minimum eigenvalue threshold。

對 $58$ 個位置先以 central difference 求 threshold gradient，再測試
gradient-sign corner，最後做 deterministic coordinate flips。這個搜尋
可以找到失敗候選，但不能證明整個 box 成功或失敗。

選定 $h=0.015,0.016,0.017$ 的角點後，以三個 time steps 重算，僅用於
離散收斂診斷。

## 7. 驗證層

`run_all.py` 依序產生：

1. exact semantic bridge；
2. exact cover certificate；
3. cover verification；
4. exact clamped radius certificate；
5. clamped verification；
6. floating location study；
7. summary；
8. output verification；
9. package validation。

`run_tests.py` 使用 standard-library `unittest`，檢查：

- rational interval corner arithmetic；
- Green kernel exact values；
- exact count-only counterexample；
- cover shape 與 strict leaves；
- $11\times11$ rational point grid；
- clamped radius orientation；
- failed probe 不被誤標成反例。

## 8. 證據分級

- `E0`：純有理或符號推論，可由標準 Python 重播；
- `E0-parent`：新推論為精確有理，但依賴已鎖定的 v0.7 interval theorem；
- `E2`：NumPy/SciPy 浮點診斷；
- `OPEN`：尚無來源或未完成 universal proof。

所有 zeta-facing presence、explicit-formula transfer 與 global RH claims
維持 `OPEN` 或 false。

