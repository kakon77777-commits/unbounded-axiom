# WDC Runtime Phase 10 Implementation Report

Date: 2026-08-17  
Branch: `feature/phase10`

## Scope

Phase 10 turns the Phase 0–9 Python kernel into an installable local runtime surface without adding new cognition semantics.

Implemented surface:

- `RuntimeContext.open(root)` with stable `wdc.sqlite3` and `blobs/` paths;
- JSON-first `argparse` CLI;
- inline JSON and `@file.json` payload loading;
- JSON success/error output;
- `tcd`, `candidate`, `world`, `evidence`, `governor`, `portfolio`, `commit`, and `learning` command groups;
- four existing reference demos exposed as `wdc demo ...`;
- `python -m wdc` module entry point;
- installable `wdc` console script;
- explicit packaging of both `wdc` and the existing `examples` package.

## Semantic Boundary

Phase 10 is intentionally a thin surface. It does not create alternate domain logic. CLI handlers call the existing Phase 0–9 services, so the following gates remain authoritative:

- `WorldSpec != WorldRun`;
- evidence-family dependence is preserved;
- Commit Gate authority and exact-action matching are preserved;
- world evidence cannot mutate parent-real history;
- WORLD-only learning cannot self-promote to REALITY_FACING;
- REAL/EXTERNAL learning anchors require registered provenance;
- holdout validation and rollback remain mandatory for activation.

## Command Families

```text
wdc init / status
wdc tcd ...
wdc candidate ...
wdc world ...
wdc evidence ...
wdc governor ...
wdc portfolio ...
wdc commit ...
wdc learning ...
wdc demo ...
```

## Packaging Contract

The project exposes:

```toml
[project.scripts]
wdc = "wdc.cli:main"
```

The wheel includes both:

```text
src/wdc
examples
```

so `wdc demo ...` works after installation outside the source checkout.

## Preliminary Packaging Verification

Before final archival, the project was built as `wdc_runtime-0.1.0-py3-none-any.whl` with the system build environment and installed into a clean virtual environment with no system-site-packages.

The installed artifact was verified from outside the source repository with:

```text
wdc --help
python -m wdc --help
wdc --root <workspace> init
wdc --root <workspace> demo learning
```

The installed wheel contained both `wdc/` and `examples/`, and the learning demo preserved the expected Phase 9 source gate and parent-time behavior.

A container-specific packaging note: a `--system-site-packages` venv in this environment exposes an incomplete Debian `setuptools` namespace that lacks `setuptools.build_meta`; therefore the final verification builds the wheel using the known-good system build environment and installs the resulting wheel into a clean runtime venv. This isolates build-tool availability from runtime package correctness.

## Current-HEAD Verification Before Final Archive

The current feature HEAD was verified before final archival with:

```text
python -m pytest -q                     -> 77 passed
python -m compileall -q src/wdc examples -> PASS
git diff --check                       -> PASS
```

A wheel was rebuilt from that HEAD and installed into a clean venv without system-site-packages. From outside the source tree, all of the following passed:

```text
wdc --help
python -m wdc --help
wdc --root <workspace> init
wdc --root <workspace> demo learning
```

The installed module paths resolved under the clean venv `site-packages` for both `wdc` and `examples`. The wheel built at this verification point had SHA-256:

```text
89c45d631b7efb6aa8ea4dae13907ee72091d022e144fc990534c733adbe45bd
```

This hash is a pre-final-archive verification artifact; final delivery hashes are recorded only after the completion document commit and fresh-extraction verification.

## Fresh-Archive Completion Gate

A Git-tracked-only source archive was created from the verified feature HEAD and extracted into a fresh directory. The extracted source independently passed:

```text
python -m pytest -q                       -> 77 passed
python -m compileall -q src/wdc examples -> PASS
wheel build from extracted source         -> PASS
clean-venv wheel install                  -> PASS
wdc --help                                -> PASS
python -m wdc --help                      -> PASS
wdc --root <workspace> init               -> PASS
wdc --root <workspace> demo learning      -> PASS
```

The installed learning demo again preserved the Phase 9 invariants: Generator learning applied, WORLD-only reality-facing WorldModel learning was rejected, and parent historical time remained at the already-sedimented value rather than advancing due to learning itself.

The final delivery artifacts are rebuilt from the documentation-complete commit after this report update and reverified before handoff.
