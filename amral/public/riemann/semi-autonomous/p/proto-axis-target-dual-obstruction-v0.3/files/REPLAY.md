# Replay

Use Python $3.11$ or newer with NumPy and SciPy.

## Rebuild primary witnesses

```bash
python run_dual_experiment.py
```

This reconstructs the $R=3$ transform model, the 18 patch-center witnesses,
the v0.2 primal cross-check, the rational payload, and the summary files.

## Recheck exact rational positivity

```bash
python verify_rational_witnesses.py
```

The verifier reads `outputs/rational_model.json`, rebuilds every rational
outer product, and runs exact `Fraction` $LDL^{\mathsf T}$.

## Rebuild sensitivity study

```bash
python run_sensitivity.py
```

This reruns quadrature, axis-grid, tail-fraction, decimal-rationalization, and
support-radius sweeps. It is the slowest replay step.

## Unit tests and package validation

```bash
python -m unittest discover -s tests -v
python validate_package.py
```

Expected result: 10 tests, all passing, followed by
`metadata/validation_report.json` with `validation_pass=true`.

## Inputs

The `data/` directory contains copied v0.2 summaries, diagnostics, handoff,
and Gram results. No known zeta-zero ordinate file is included or used.

Floating eigenspectra may vary slightly by BLAS/LAPACK implementation. Exact
rational verification is deterministic for the serialized payload.
