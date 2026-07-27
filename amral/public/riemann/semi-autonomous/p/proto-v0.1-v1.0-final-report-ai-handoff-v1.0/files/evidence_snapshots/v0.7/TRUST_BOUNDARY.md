# Trust Boundary

## 已證明

### E0：解析結構

1. clamped $D^4$ representer 的 exponential-plus-cubic 公式。
2. exponential moments 的 finite recurrence。
3. 兩個 structural constraints 的 finite-rank projection。
4. positive rank $60$、negative rank $2$ 的 Woodbury reduction。
5. $B^{-1}-Q$ 與原 infinite-dimensional operator 的 Schur equivalence。
6. Neumann residual enclosure theorem。

### E3-A：抽象模型的 directed certificate

1. $\pi$、$\exp$、$\sin$、$\cos$ 的 directed enclosure。
2. 全部 unprojected Green pairings。
3. structural Gram determinant 與 inverse。
4. 全部 projected pairings。
5. 整個 $60\times60$ interval system family 的 regularity。
6. 兩個 right-hand sides 的 verified solution enclosure。
7. 最終 $2\times2$ Sylvester strict positivity。

因此

$$
W_{21/20}\succ0
$$

在固定 rational coefficients 所定義的 abstract model 中成立。

## 已否定的舊式模糊性

- 結論不依賴 Chebyshev dictionary。
- 結論不依賴 time-grid quadrature。
- 結論不依賴 ordinary floating eigenvalue 的正負號。
- 結論不依賴 unverified $60\times60$ solve。

## 新確認的阻塞

既有 band coefficients 是 upper-profile majorants。若 zeta-facing
operator 的正向 axis 項需要 lower counts，這些係數不能直接使用。

特別是：

$$
\operatorname{floor}_{12}(U)
$$

仍然只是一個略低於 $U$ 的數，不會因此成為真實 count 的 lower
bound。

## 尚未證明

1. 原始顯式公式推導中 band coefficient 的正確 inequality direction。
2. 五帶的 validated lower zero counts。
3. band endpoints 不落在零點上的 interval 證書或一致 convention。
4. rational tail scale 的 theorem-backed lower enclosure。
5. clamped $H_0^2$ closure 到顯式公式 admissible class 的 density 與
   limit exchange。
6. prime-side cone 的完整 directed evaluation。
7. 其他偏軸 patches 的 continuous interval certificate family。
8. 未知 leakage regions 的全域 budget。
9. target patch 的 zeta zero presence 或 winding。
10. local-to-global RH closure。

## 合法敘述

可以說：

> 固定 rational model 的連續 atomic dual 在
> $\alpha=21/20$ 有可重播的 interval positivity certificate。

不可以說：

> 這已排除 zeta 的某個實際零點區域。

更不可以說：

> RH 已被證明或反證。

## Flags

- `abstract_continuous_interval_certificate = true`
- `zeta_facing_tail_theorem_certified = false`
- `zeta_facing_count_coefficients_certified = false`
- `explicit_formula_admissibility_certified = false`
- `global_rh_certificate = false`
