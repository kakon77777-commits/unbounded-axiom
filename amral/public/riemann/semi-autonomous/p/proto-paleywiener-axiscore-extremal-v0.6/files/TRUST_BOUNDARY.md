# Trust Boundary

## E0：本節點內的解析結果

1. clamped tail space 是 Hilbert space，compact-support Fourier evaluations
   為 bounded functionals。
2. positive trace-class primal 與 probability-measure dual 的 weak duality。
3. 一軸點、一核心點 extremal 的 rank-two closed form。
4. clamped bi-Laplacian Green kernel公式。
5. 兩個結構零點的 finite-rank kernel projection。
6. finite atomic witness 的 Woodbury–Schur PSD equivalence。
7. 兩個 core atoms 使最終 negative Schur rank 恰為 2。

## E1：自動結構與重播檢查

- nested Galerkin dimension list 與 row counts。
- 每個 axis/core probability numerator 精確加總到 $10^{12}$。
- rational atom counts 為 58 與 2。
- 所有 cutting-plane final gradient gaps 為 0。
- rational target 為 $\alpha=21/20$。
- 所有 global、interval flags 保持 false。

## E2：floating continuous-kernel evidence

- Chebyshev–Galerkin optimization。
- Gauss–Legendre Fourier quadrature。
- direct Green ODE representers。
- Galerkin-to-Green atomic measure transfer。
- $60\times60$ positive solve 與 $2\times2$ Schur matrix。
- time-step、quadrature-order 與 dimension convergence。

## 重要進展

v0.6 已消除「只在某個 finite dictionary 中 blocked」這個主要歧義。固定
atomic measures 被直接放入 continuous clamped Green RKHS，所得 safe PSD
margin 明顯為正。

但這仍是 floating reconstruction。`continuous_kernel_floating_obstruction`
不能寫成 `continuous_kernel_interval_certificate`。

## 尚未建立

1. 沒有 directed-rounding enclosure of Green-kernel integrals。
2. 沒有 interval enclosure of structural $2\times2$ projection。
3. 沒有 interval linear solve for the positive $60\times60$ system。
4. 沒有 interval eigenvalue proof for the final $2\times2$ Schur matrix。
5. inherited tail multiplier 尚未封裝成 theorem-backed lower interval。
6. count coefficients 尚未以完整 endpoint hypotheses 與 directed rounding
   驗證。
7. 尚未證明此 $H_0^2$ continuous model 與全部 explicit-formula admissibility
   假設之間的解析轉移。
8. 沒有完整 288 refined patches 的 continuous obstruction family。
9. 沒有未知偏軸區域的 global leakage closure。
10. 沒有 zero presence、winding 或 local-to-global RH closure。

## 合法解讀

若 v0.7 成功證明 rational witness 在 abstract continuous model 中
$W_{21/20}\succeq0$，則可推出：

$$
\Lambda_{16}\ge\frac{21}{20}>1
$$

於指定 patch、五帶、係數與 clamped structural-zero domain。

這會排除該 continuous model 的 primal branch，但仍不等於 RH 證明或反證；
zeta-facing coefficient theorems、其他區域與全域量詞仍須獨立閉合。
