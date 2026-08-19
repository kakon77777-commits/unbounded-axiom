# HIPG Formal Toy v0.2

This is the second executable scaffold for the eight-paper HIPG series.

Run everything:

```bash
python hipg_toy_v0_2.py
```

Run unit tests:

```bash
python -m unittest -v test_hipg_v0_2.py
```

Primary outputs:

- `results.json`
- `bridge_results.json`
- `fano_results.json`
- `VALIDATION.json`
- `RUN_LOG.txt`

Canonical benchmark target: **9/9 PASS**.

This package does not prove B-TSDPC. It instantiates a richer finite model with quotient inference, SPLIT↔MERGE, approximate TSSH, a noisy-channel Fano comparison, and a four-layer bridge.
