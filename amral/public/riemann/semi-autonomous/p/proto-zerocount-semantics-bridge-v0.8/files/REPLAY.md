# Replay

## Environment

Required:

- Python $3.11$ or later
- NumPy
- SciPy

The test runner uses only the Python standard library.

## Full replay

From the package root:

```bash
python run_all.py
python run_tests.py
```

`run_all.py` performs:

1. exact semantic bridge;
2. five-band floating profile;
3. lineage and tail-direction audit;
4. ten-dimension lower-profile Galerkin search;
5. direct Green transfer at three time steps;
6. sampled primal escape reconstruction;
7. summary;
8. disk-read output verification;
9. package validation.

Expected runtime is normally below one minute on a current workstation.

## Expected anchors

The last Galerkin row should have approximately

$$
\alpha_{190}
=
0.1297047862.
$$

The $\Delta t=0.005$ direct Green row should have approximately

$$
\alpha_{\mathrm{Green}}
=
0.1297031276.
$$

The sampled primal objective should be approximately

$$
0.1297069814.
$$

Small floating variation is acceptable only within the tolerances encoded in
`verify_outputs.py`.

## Fast checks

```bash
python verify_outputs.py
python validate_package.py
python run_tests.py
```

## Clean extraction replay

After extracting the release ZIP:

```bash
cd RH_ZeroCount_Semantics_Bridge_v0.8
python run_all.py
python run_tests.py
```

No parent package is required. The Galerkin and Green routines needed by v0.8
are included under `bridge/`.

## Failure meaning

- A semantic failure indicates a code or serialization regression.
- A profile mismatch indicates a source-profile or rounding change.
- A Galerkin mismatch may indicate numerical-library drift.
- A direct Green mismatch may indicate quadrature or projection drift.
- None of these failures or passes is an RH proof status.
