# Trust Boundary

## 已完成

1. exact two-point countermodel；
2. exact rank-one common-floor countermodel；
3. upper-count、lower-count 與 arbitrary-measure transfer 的邏輯分類；
4. v0.1–v0.7 lineage semantic audit；
5. lower candidate profile 下的 $10$ 層 Galerkin convergence；
6. 三個 time steps 的 direct Green fixed-measure transfer；
7. sampled primal escape diagnostic；
8. 所有 JSON 的重算驗證與 standard-library unit tests。

## E0 exact statements

下列命題不依賴浮點數值：

$$
n\le U
\Longrightarrow
\sum_{\gamma\in\Gamma}H(\gamma)
\le
U\sup H,
$$

$$
n\ge L
\Longrightarrow
\sum_{\gamma\in\Gamma}H(\gamma)
\ge
L\inf H.
$$

以及：

$$
n\ge L
\not\Longrightarrow
\sum_{\gamma\in\Gamma}H(\gamma)
\ge
L\int H\,d\mu
$$

對任意 probability measure $\mu$。

## E2 floating objects

下列物件只是 floating diagnostics：

- Riemann–Siegel theta 與 five-band count profiles；
- SLSQP atomic measure optimization；
- Chebyshev–Gauss Galerkin convergence；
- trapezoid direct Green transfer；
- $101\times101$ core grid primal escape；
- axis step $0.01$ 的 sampled suprema。

## 尚未完成

1. inherited $|S(T)|$ 版本與常數的正式來源封裝；
2. theta、log、log-gamma 與 $\pi$ 的 directed interval enclosure；
3. band endpoint zero conventions；
4. tail density theorem與 tail scale direction certificate；
5. whole-patch continuous primal escape certificate；
6. actual zero-location occupancy certificate；
7. universal uncertain-location Green-Schur family；
8. explicit-formula admissibility與 prime-side transfer；
9. 全域有理矩形覆蓋；
10. RH 證明或反證。

## Prototype restriction

patch

$$
[20.395,20.42]\times[-0.10625,-0.1]
$$

只作 prototype。Platt–Trudgian 已嚴格驗證 RH 至

$$
3\cdot10^{12},
$$

所以本 patch 不是未決的實際 $\zeta$ 偏軸目標。

## Claim flags

```text
exact_semantic_theorems = true
floating_lower_profile_diagnostic = true
abstract_v0_7_interval_certificate_retained = true
upper_envelope_method_nogo_fully_certified = false
actual_zero_side_operator_bridge = false
explicit_formula_transfer = false
global_rh_certificate = false
```
