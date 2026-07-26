# Replay

Use Python 3.12 or newer with NumPy, SciPy, and pytest installed.

```bash
python run_experiment.py
python run_ablation.py
python -m pytest -q
```

Expected structural outcomes:

- `patch_count = 18`;
- `candidate_count = 72`;
- exact rational cover audit passes;
- all 18 dense sampled cores pass;
- all 18 crude floating Lipschitz sign audits pass;
- no partial or global budget passes;
- coarse continuous-sign pass fraction is $0.5$;
- adaptive continuous-sign pass fraction is $1.0$.

The exact floating coefficients may vary at the last digits across BLAS,
LAPACK, and SciPy builds. Any material change in active rays, sign status, or
order-of-magnitude budget must be investigated rather than normalized away.
