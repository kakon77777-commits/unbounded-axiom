# RH Separation–Positivity Intersection Prototype v0.1

This package merges the previous regional phase-shaping and arithmetic-matrix prototypes into one shared coordinate system.

For the **same real coefficient vector** `c`, it tests

\[
\max_{w\in K} 2\operatorname{Re}(G_c(w)^2)<0
\]

on a finite spectral grid while enforcing

\[
c^T M_{\mathrm{arith}}(R)c\ge\delta,
\qquad
c^T C_0c=1,
\qquad
G_c(i/2)=G_c(0)=0.
\]

## Run

```bash
python run_demo.py --config examples/intersection_scan.json --output outputs
pytest -q
```

## Main outputs

- `intersection_scan.csv`
- `intersection_scan_result.json`
- `separation_margin.png`
- `arithmetic_margin.png`
- `selected_region_block.png`
- `normalization_audit.json`

## Status

This is a floating-point finite-dimensional research prototype. A negative dense grid is not a continuous-region proof, and a positive floating-point quadratic value is not an interval PSD certificate. It does not prove the Riemann hypothesis.

## Included v0.1 result

The supplied example found a common coefficient vector at every scanned support radius `R=1.5,...,4.0`. See `RESULTS.md` for the numerical table and audit.
