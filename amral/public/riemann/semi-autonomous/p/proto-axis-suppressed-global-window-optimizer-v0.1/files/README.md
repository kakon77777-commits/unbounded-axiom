# RH Axis-Suppressed Global-Window Optimizer v0.1

This package extends the local separation/positivity experiments with:

1. finite-dimensional annihilation constraints at the first `q` stored
   critical-line ordinates;
2. a paired compact-bump basis on `[-3,3]`;
3. a target-region minimax problem;
4. an exchange-style finite off-axis control-window optimizer;
5. a scan of the arithmetic-positive eigendimension as `q` grows.

## Selected diagnostic candidate

The stored `q=12` candidate satisfies in the floating finite-dimensional model:

- finite-model constraint residual: `1.7333621857e-16`;
- `C0` normalization: `1`;
- arithmetic quadratic value: `5.00000000001e-05`;
- dense target maximum: `-2.64607989612e-08`;
- remaining first-50 axis mass: `0.000154365729672`;
- dense control-window maximum: `0.267543612562`.

Thus finite axis annihilation, target negativity, and arithmetic positivity can
coexist, but full control-window nonpositivity was not obtained.

## Run

```bash
python verify_selected_candidate.py
python run_scan.py
pytest
```

The scan is non-convex and floating-point. Results may vary slightly across
SciPy and BLAS versions.

This package does not prove the Riemann hypothesis.
