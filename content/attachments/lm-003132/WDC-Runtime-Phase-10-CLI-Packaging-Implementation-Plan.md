# WDC Runtime Phase 10 CLI / Packaging Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Phase 0–9 WDC kernel installable and operable through a JSON-first local CLI without changing existing cognitive semantics.

**Architecture:** Add one workspace/bootstrap context, one JSON serialization/input helper, and one `argparse` dispatcher. Every CLI handler delegates to existing Phase 0–9 services. Package it through `[project.scripts]`, then verify from a fresh virtual environment outside the repository.

**Tech Stack:** Python 3.11+, stdlib `argparse/json/pathlib/dataclasses`, existing SQLite/blob runtime, setuptools, pytest.

## Global Constraints

- No new runtime dependencies.
- Use `python -m pytest`, not bare `pytest`, because the repository uses a `src/` layout and the current pytest launcher does not add the project root consistently.
- CLI complex inputs support inline JSON and `@file.json`.
- CLI stdout is JSON on success; expected domain failures use JSON stderr and exit code 2.
- `WorldSpec != WorldRun`, History Firewall, Commit Gate, learning source gates and all Phase 0–9 invariants remain unchanged.
- Commands must call existing services instead of duplicating domain logic.

---

### Task 1: Runtime Workspace Context

**Files:**
- Create: `src/wdc/runtime.py`
- Test: `tests/test_runtime_context.py`

**Interfaces:**
- Produces: `RuntimeContext.open(root: str | Path) -> RuntimeContext`
- Produces fields: `root`, `db_path`, `blob_root`, `db`, `blobs`
- Consumes: `WDCDB`, `BlobStore`

- [x] **Step 1: Write failing bootstrap/reopen tests**
- [x] **Step 2: Run `python -m pytest tests/test_runtime_context.py -q` and verify missing module/API failure**
- [x] **Step 3: Implement minimal `RuntimeContext` with deterministic workspace paths**
- [x] **Step 4: Run targeted and full tests**
- [x] **Step 5: Commit `feat: add runtime workspace context`**

### Task 2: JSON CLI Helpers and Parser Skeleton

**Files:**
- Create: `src/wdc/cli_json.py`
- Create: `src/wdc/cli.py`
- Create: `src/wdc/__main__.py`
- Test: `tests/test_cli_core.py`

**Interfaces:**
- Produces: `load_json_arg(value: str) -> Any`
- Produces: `to_jsonable(value: Any) -> Any`
- Produces: `build_parser() -> argparse.ArgumentParser`
- Produces: `main(argv: Sequence[str] | None = None) -> int`

- [x] **Step 1: Write failing tests for inline JSON, `@file`, `init`, `status`, help, and machine-readable errors**
- [x] **Step 2: Verify RED**
- [x] **Step 3: Implement JSON normalization and top-level parser/dispatch**
- [x] **Step 4: Verify targeted and full suite**
- [x] **Step 5: Commit `feat: add json cli shell`**

### Task 3: TCD, Candidate and World Commands

**Files:**
- Modify: `src/wdc/cli.py`
- Test: `tests/test_cli_tcd_world.py`

**Interfaces:**
- CLI: `tcd init/show/assimilate/sediment`
- CLI: `candidate create/list`
- CLI: `world create/show/run-create`
- Consumes: `TCDStateManager`, `FutureCandidate`, `WorldRegistry`, `WorldSpec`

- [x] **Step 1: Write failing end-to-end command tests in one temporary workspace**
- [x] **Step 2: Verify RED**
- [x] **Step 3: Implement thin handlers using existing service methods**
- [x] **Step 4: Verify targeted and full suite**
- [x] **Step 5: Commit `feat: expose tcd candidate and world cli`**

### Task 4: Evidence, Governor and Portfolio Commands

**Files:**
- Modify: `src/wdc/cli.py`
- Test: `tests/test_cli_evidence_governor.py`

**Interfaces:**
- CLI: `evidence claim-create/packet-add/aggregate/counterexamples`
- CLI: `governor state/allocate/kill/promote`
- CLI: `portfolio route`
- Consumes existing `EvidenceEngine`, `WorldGovernor`, `DeficitRouter`

- [x] **Step 1: Write failing command tests covering dependence-aware aggregate and budgeted Governor state**
- [x] **Step 2: Verify RED**
- [x] **Step 3: Implement handlers without inventing new aggregation/allocation rules**
- [x] **Step 4: Verify targeted and full suite**
- [x] **Step 5: Commit `feat: expose evidence governor portfolio cli`**

### Task 5: Commit and Learning Commands

**Files:**
- Modify: `src/wdc/cli.py`
- Test: `tests/test_cli_commit_learning.py`

**Interfaces:**
- CLI: `commit assess/show/sandbox-execute`
- CLI: `learning component-init/active/source-anchor/propose/validate/rollback/health`
- Consumes existing `CommitGate`, `ExternalToolProxy`, `LearningCoordinator`

- [x] **Step 1: Write failing tests proving authority/source/validation gates still apply through CLI**
- [x] **Step 2: Verify RED**
- [x] **Step 3: Implement thin handlers**
- [x] **Step 4: Verify targeted and full suite**
- [x] **Step 5: Commit `feat: expose commit and learning cli`**

### Task 6: Demo Surface

**Files:**
- Modify: `src/wdc/cli.py`
- Test: `tests/test_cli_demos.py`

**Interfaces:**
- CLI: `demo branching-grid|governed-evidence|tri-temporal|learning`
- Consumes existing example `run_demo()` functions

- [x] **Step 1: Write failing tests for all four demo names and isolated demo roots**
- [x] **Step 2: Verify RED**
- [x] **Step 3: Implement demo dispatch**
- [x] **Step 4: Verify targeted and full suite**
- [x] **Step 5: Commit `feat: expose runtime demos through cli`**

### Task 7: Installable Packaging and Fresh-Venv Verification

**Files:**
- Modify: `pyproject.toml`
- Modify: `README.md`
- Create: `PHASE10_IMPLEMENTATION_REPORT.md`
- Test: `tests/test_cli_packaging_contract.py`

**Interfaces:**
- Console script: `wdc = wdc.cli:main`
- Module entry: `python -m wdc`

- [x] **Step 1: Write failing packaging-contract test for project script metadata and module entry point**
- [x] **Step 2: Verify RED**
- [x] **Step 3: Add `[project.scripts]`, CLI docs, report, and versioned packaging notes**
- [x] **Step 4: Run full tests, `compileall src/wdc examples`, and `git diff --check`**
- [x] **Step 5: Build the wheel with the known-good system build environment, install that wheel into a clean venv without system-site-packages, then run `wdc --help`, `python -m wdc --help`, initialize a workspace and run `wdc demo learning` from outside repo**
- [x] **Step 6: Commit `feat: package wdc runtime cli`**

### Completion Gate

- [x] Full test suite passes on final HEAD.
- [x] `python -m compileall -q src/wdc examples` passes.
- [x] `git diff --check` passes.
- [x] Final workspace demo works through installed `wdc` console command.
- [x] Final ZIP is created from Git-tracked files only.
- [x] Fresh extraction installs in a new venv and repeats tests/help/demo successfully.
