# Changelog

## v0.7 — 2026-07-25

### Added

- $90$ 位 directed-decimal interval arithmetic。
- Machin-series $\pi$ enclosure。
- rigorous $\exp$、$\sin$、$\cos$ Taylor enclosures。
- closed-form clamped Green exponential pairings。
- structural $2\times2$ projection certificate。
- projected Gram endpoint hash。
- rational Neumann inverse／solution candidates。
- verified $60\times60$ system family solve。
- final $2\times2$ Sylvester certificate。
- exact serialization audit。
- failure injection test。
- band coefficient orientation audit。
- lower-profile counterstress。

### Promoted

v0.6 的

`continuous_kernel_floating_obstruction`

在固定 abstract coefficients 下提升為

`abstract_continuous_interval_certificate`。

### Not promoted

以下 flags 保持 false：

- `zeta_facing_tail_theorem_certified`
- `zeta_facing_count_coefficients_certified`
- `explicit_formula_admissibility_certified`
- `global_rh_certificate`

### Research correction

確認父節點五個 band coefficients 是 upper-profile majorants。下一節點
由單純 coefficient intervalization 改成 robust count semantics 與
validated lower-count bridge。
