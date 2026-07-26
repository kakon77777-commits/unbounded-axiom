# Trust Boundary

## Established exactly inside the exported surrogate

- `outputs/rational_model.json` defines a finite rational model.
- Its rationalized tail matrix is positive definite under exact
  no-pivot $LDL^{\mathsf T}$.
- All 18 rational witness matrices have 22 strictly positive exact pivots.
- Within that model, PSD self-duality gives the logical implication

$$
A\succeq0,\quad \langle C(z_P),A\rangle\le-1
\quad\Longrightarrow\quad J(A)\ge2.
$$

These are E0 algebraic statements about the serialized surrogate.

## Supported numerically

- The original floating primary witnesses pass all 18 centers.
- They remain positive over the tested quadrature and axis meshes.
- The v0.2 saved primal matrices obey the dual pairing identity.
- The support-radius transition is reproducible for the specified bump-density
  rule.

These are E2 numerical research findings, not interval-certified analytic
theorems.

## Not established

1. No interval enclosure transfers the rationalized transforms to exact
   Fourier integrals.
2. The inherited zero-count coefficient is not packaged as a cited,
   formally checked theorem object.
3. The $t^{-4}$ tail density and constants remain a floating prototype.
4. The result only rejects the stated $R=3$, 24-bump, 22-dimensional
   patchwise finite-model class.
5. Axis-only positivity at $\rho=0$ is not claimed.
6. Center escape at larger $R$ is not a primal feasibility certificate.
7. Unknown off-axis zero regions are not completely budgeted.
8. No argument-principle or winding certificate proves a zero lies in a
   target patch.
9. No local-to-global RH contradiction is closed.
10. Nothing in this package proves RH, disproves RH, or proves an equivalent
    RH criterion.

## Interpretation rule

`current_r3_patchwise_function_class_rejected=true` means only that the
specified finite-model objective cannot be below $1$ while satisfying the
patchwise unit-negativity requirement. It must never be paraphrased as a
statement about all admissible test functions or about RH itself.

`all_exact_ldl_positive=true` means exact positivity of decimal-rational
matrices created by the export convention. It does not certify the numerical
quadrature that generated those decimals.
