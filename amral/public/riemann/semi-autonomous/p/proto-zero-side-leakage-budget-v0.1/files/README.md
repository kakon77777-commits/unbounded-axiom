# RH Zero-Side Leakage Budget v0.1

This package measures why a certified local negative orbit block is not yet a
negative full zero-side sum.

## Run

```bash
python run_leakage_budget.py
```

## Main result

Certified target-region negative margin:

```text
2.2416560599e-06
```

Numerical mass from the first critical-line zero:

```text
0.00535215750176
```

Ratio:

```text
2387.591
```

The present test function therefore cannot make one target rectangle dominate
even the first critical-line contribution. The next optimizer must include
critical-line suppression or a signed global-region design.

This package is a diagnostic prototype, not an RH proof and not a formal
zero-count certificate.
