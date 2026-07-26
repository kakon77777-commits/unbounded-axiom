# Trust Boundary

## What is established inside the floating model

- The saved Gram matrices are of the form $A=LL^{\mathsf T}$ up to floating
  reconstruction error and have minimum eigenvalue at least
  $-1.3\times10^{-14}$.
- All 18 dense core checks are negative.
- All 18 refined sampled-gradient plus Hessian-envelope core audits remain
  negative, with upper values from $-0.9923$ to $-0.9606$.
- The arithmetic values, band charges, tails, holdouts, guards, and comparison
  statistics recompute from the saved JSON data.
- Nine automated tests pass under Python’s standard `unittest` runner.

These statements are E2 numerical research evidence.

## What is not established

1. No convex SDP optimum is certified. The factorization $A=LL^{\mathsf T}$
   guarantees PSD but makes the SLSQP search nonconvex.
2. No interval arithmetic encloses the transform integrals, arithmetic
   quadratic form, count profile, axis suprema, or Hessian corrections.
3. The inherited zero-count profile is a floating prototype, not a formal
   theorem object in this package.
4. The $t^{-4}$ tail is a floating majorant prototype.
5. Unknown off-axis zero contributions are omitted from the partial gap.
6. The target rectangles have no positive winding, argument-principle, or
   zero-presence certificate.
7. The package does not close the explicit-formula contradiction in ZFC.
8. No result here proves RH, disproves RH, or proves an equivalent criterion.

## Interpretation rule

“Pass” refers only to the named local numerical audit. In particular:

- `core_refined_continuous_sign_pass` does not mean global certificate pass;
- `sampled_partial_budget_pass` omits unknown off-axis terms;
- `global_certificate_pass` is deliberately false in every output.

The first 50 known zeta-zero ordinates are holdout diagnostics only. They are
not used to fit, select, or optimize a candidate.
