# Next Node: Interval Green-Kernel Atomic Certificate v0.7

## Node

`RH-IntervalGreenKernel-AtomicCertificate-20260725-v0.7`

## Fixed target

不再最佳化 alpha。固定

$$
\alpha_\star=\frac{21}{20}=1.05.
$$

輸入固定為 `outputs/rational_atomic_witness.json`：

- 58 axis atoms；
- 2 core atoms；
- 每組 weight denominator $10^{12}$；
- rational supports；
- 5 個 rationalized count coefficients；
- rationalized downward tail-scale candidate。

## Exact certification path

1. 對 clamped Green kernel的 elementary polynomial–trigonometric–
   hyperbolic integrals做 ball/interval evaluation。
2. interval-enclose structural Gram

   $$
   M=
   \begin{pmatrix}
   \Gamma(c_0,c_0)&\Gamma(c_0,c_1)\\
   \Gamma(c_1,c_0)&\Gamma(c_1,c_1)
   \end{pmatrix}
   $$

   並驗證 invertibility。
3. enclosure all projected pairings $\Gamma(f_i,f_j)$。
4. 建立 positive $60\times60$ system

   $$
   I+U^\ast U
   $$

   的 verified interval solve。
5. enclosure final

   $$
   S_{\alpha_\star}
   =I-\left[
   V^\ast V
   -V^\ast U(I+U^\ast U)^{-1}U^\ast V
   \right].
   $$

6. 用 directed eigenvalue／Sylvester criterion 證明

   $$
   S_{\alpha_\star}\succ0.
   $$

## Two-layer certificate

### Layer A：abstract continuous extremal

以 rational coefficients 與明確 $\kappa_R$ 定義 abstract model，完成

$$
W_{21/20}\succeq0.
$$

### Layer B：zeta-facing coefficient legitimacy

獨立驗證：

- tail scale lower bound 的來源定理與 endpoint hypotheses；
- 五帶 count lower coefficients 的 directed evaluation；
- explicit-formula admissibility 與 $H_0^2$ closure 的轉移。

Layer A 成功不能替代 Layer B。

## Certification budget

v0.6 floating diagnostics at $\alpha=1.05$：

$$
\lambda_{\min}(W)\approx0.31224325,
$$

$$
\lambda_{\min}(S)\approx0.06988523.
$$

最後兩級 time-step drift 約

$$
2.68\times10^{-8}.
$$

margin 足以優先採 correctness-first interval arithmetic，不必再壓縮 alpha。

## Stop rules

- 不回到 dictionary search。
- 不繼續提高 Galerkin dimension。
- 不用普通高精度浮點冒充 interval enclosure。
- 不在 Layer A 完成前擴大到其他 patches。
- 不把 abstract continuous obstruction 寫成 RH 結論。
