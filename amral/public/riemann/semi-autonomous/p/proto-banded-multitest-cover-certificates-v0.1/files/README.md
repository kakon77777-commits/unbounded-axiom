# RH Banded Multi-Test Cover Certificates v0.1

This package is the first semi-autonomous AI research node after
`RH_Equivariant_Arithmetic_Obstruction_Integration_v1.0`.

It tests a precise question: can an overlapping family of local negative
certificates, assembled from several admissible rank-one test functions,
reduce the global leakage obstruction that defeated the previous
single-window candidate?

The implemented answer is mixed but useful:

- An adaptive anisotropic family of 18 rational rectangles exactly covers
  $[20,20.5]\times[-0.2,-0.1]$.
- A library of 72 candidates is generated without using any known zeta-zero
  ordinate as an optimization constraint or objective sample.
- All 18 aggregated cores pass a $161\times121$ sampled negativity check and
  a floating, deliberately crude $L^1$-Lipschitz sign audit.
- Refining height windows near the symmetry axis reduces the worst coarse-cover
  axis-energy proxy by a factor of about $215.13$, the first-50 holdout mass by
  about $85.83$, and the prototype tail bound by about $479.69$.
- The primary axis-energy LP still selects a single extreme ray. Multi-test
  mixtures help guard shaping, not primary leakage minimization, in this
  diagonal cone.
- Every partial global budget remains negative. This is not an RH proof and
  not a global zero-side certificate.

The result recommends a specific next move: retain the adaptive cover but
replace the diagonal nonnegative cone by a PSD Gram variable with off-diagonal
cross terms.

## Replay

From this directory:

```bash
python run_experiment.py
python run_ablation.py
python -m pytest -q
```

Main outputs:

- `outputs/experiment_summary.json`
- `outputs/ablation_summary.json`
- `outputs/candidate_library.json`
- `outputs/certificate_summary.csv`
- `outputs/certificates/*.certificate.json`

The numerical claims are floating-point research evidence at level E2. See
`TRUST_BOUNDARY.md` before reusing any certificate claim.
