# Trust Boundary

## 已嚴格驗證

- Fraction-based interval arithmetic；
- Dirichlet Green kernel 的 piecewise rational enclosure；
- count-only exact counterexample；
- adaptive cover tree 與全部 leaf Sylvester inequalities；
- occupancy selection transfer 的代數推論；
- v0.7 parent hashes、classification 與 probability normalization；
- 從 parent positivity 到 $\alpha=1$ 的 convex coercivity margin；
- clamped Green 全域 Poincaré 擾動 budget；
- $58$ 個 independent closed cells 的精確微半徑 family。

## 條件式依賴

clamped $58$-cell 結論以 v0.7 的
`abstract_continuous_interval_certificate = true` 為 parent theorem。
v0.9 鎖定 parent witness 與 certificate bytes，並重算新推論；完整
directed-decimal Green replay 仍由 v0.7 套件負責。

因此此結論的正確標籤是：

`conditional_abstract_operator_family_certificate = true`。

## 僅為浮點診斷

- clamped trapezoid reconstruction；
- threshold gradient；
- adversarial corner selection；
- coordinate-flip search；
- $0.016$ 到 $0.017$ 的 observed transition bracket。

這些結果沒有 interval enclosure，也沒有窮盡所有 corners 或 interiors。
`threshold < 1` 的 floating candidate 不是形式 operator counterexample。

## 尚未提供

- 真實 $\zeta$ 零點的 cell-by-cell presence theorem；
- argument principle 或 Turing certificate 的 source hash；
- 未解高度區間的 occupancy family；
- local interval trigonometric/exponential Green derivatives；
- explicit-formula admissible test-function theorem；
- prime-side nonnegative cone certificate；
- local-to-global exhaustion；
- RH proof 或 disproof。

## 永久 false flags

本節點以下 flags 必須保持 false：

- `zeta_facing_occupancy_certificate`；
- `actual_zero_occupancy_certificate`；
- `explicit_formula_global_transfer`；
- `global_rh_certificate`。

任何後續 AI 若要改成 true，必須新增可重播依賴，不得只改欄位名稱、移除
限定詞或把 synthetic premise 改稱 theorem。

