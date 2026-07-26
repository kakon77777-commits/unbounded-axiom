# RH PSD Gram Banded Global Dominance v0.2

This semi-autonomous AI research node tests the move recommended by
`RH_Banded_MultiTest_Cover_Certificates_v0.1`: keep the adaptive 18-patch
cover, but replace the diagonal cone of 72 inherited rank-one rays by a PSD
Gram variable with unrestricted cross terms in the full 22-dimensional
constrained coordinate space.

The answer is decisive enough to change direction:

- Constructive PSD Gram search reduces the sampled zero-position-free
  axis-plus-tail majorant by $10.89\%$ to $28.66\%$, with mean reduction
  $21.08\%$, against the diagonal 72-ray baseline.
- The optimized direction is genuinely new: its nearest inherited ray is
  $29.22^\circ$ to $70.15^\circ$ away in the $C_0$-whitened metric.
- Every one of the 18 Gram candidates remains negative on the whole patch
  under the floating sampled-gradient plus Hessian-envelope audit.
- Requested ranks $1,2,4,8$ on four representative patches all collapse to
  numerical rank one, with objective variation below $2.0\times10^{-9}$.
- The sampled partial majorant is still $64.60$ to $142.73$ against target
  budget $1$; after the floating continuity correction it is $89.77$ to
  $354.16$.
- The real-axis band $[18,23]$ is the dominant charge on all 18 patches and
  contributes on average $61.73\%$ of the sampled objective.

This is not an RH proof and not a global zero-side certificate. No convex SDP
solver was available: the package uses the constructive factorization
$A=LL^{\mathsf T}$ with multi-start SLSQP and claims neither global SDP
optimality nor interval certification.

The next node should therefore stop enlarging the same primal rank family and
build a dual axis-target transfer certificate focused on $[18,23]$. See
`metadata/handoff.json`.

## Replay

From this directory:

```bash
python run_experiment.py
python refresh_audits.py
python build_diagnostics.py
python -m unittest discover -s tests -v
```

The full optimization is the expensive step. `refresh_audits.py` recomputes
continuity diagnostics from saved Gram matrices without rerunning SLSQP.

Main outputs:

- `outputs/experiment_summary.json`
- `outputs/diagnostics.json`
- `outputs/comparison.csv`
- `outputs/diagonal_results.json`
- `outputs/gram_results.json`
- `outputs/rank_study.json`
- `outputs/patches/*.json`

Read `TRUST_BOUNDARY.md` before reusing any mathematical claim.
