# wdc-runtime

Local reference implementation for **World-Domain Cognitive Runtime v0.1**.

Current scope: **Phase 0–2** only — ledger kernel, immutable `WorldSpec` / separate `WorldRun`, deterministic `PythonStateWorld`, exact checkpoints, and an acyclic fork lineage graph.

## Run tests

```bash
python -m pytest -q
```

## Run the Branching Grid demo

```bash
PYTHONPATH=src:. python examples/branching_grid.py /tmp/wdc-branching-grid
```

The demo creates one parent world, checkpoints it, forks two child worlds from the same exact prefix, applies divergent actions, persists fork events, and prints divergent terminal states.

## Hard invariants already implemented

- `WorldSpec != WorldRun`
- three clock fields are explicit in the event envelope
- exact checkpoints preserve state, local time, and RNG state
- each fork creates a new world ID
- fork provenance records parent run, checkpoint, delta, and seed policy
- lineage cycles are rejected
- event payloads are persisted as snapshots
- blobs are content-addressed and integrity-checked

See `docs/specs/` for the implementation contracts and `docs/superpowers/plans/` for the Phase 0–2 execution plan.
