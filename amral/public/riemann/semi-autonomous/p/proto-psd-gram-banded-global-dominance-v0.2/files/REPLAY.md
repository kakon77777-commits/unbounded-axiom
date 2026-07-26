# Replay

Use Python $3.11$ or newer with NumPy and SciPy.

## Full experiment

```bash
python run_experiment.py
```

This reruns:

- four representative rank sweeps at ranks $1,2,4,8$;
- the 72-ray diagonal LP on all 18 patches;
- the factorized 22-dimensional Gram search on all 18 patches;
- dense-grid exchange, guard shaping, and output serialization.

The search is deterministic for the stored seed `20260724`, subject to
platform-level floating optimizer differences.

## Refresh continuity audits

```bash
python refresh_audits.py
```

This reloads saved Gram matrices and recomputes the refined core and axis
continuity audits without rerunning optimization.

## Rebuild diagnostics

```bash
python build_diagnostics.py
```

## Tests

```bash
python -m unittest discover -s tests -v
```

Expected result: 9 tests, all passing.

## Key input boundary

The `data/` directory contains the inherited 72-ray library, the 18 parent
certificates, the parent summary, and the first 50 ordinates. The ordinates are
loaded to build holdout matrices, but no optimizer objective or constraint
uses them.
