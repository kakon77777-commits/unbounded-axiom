# Phase 13 Worker Protocol / Remote World Execution Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Serialize and execute WDC world runs across an isolated worker-process boundary, then validate and ingest returned artifacts without delegating evidence, commit, or TCD authority.

**Architecture:** Parent stages an immutable worker envelope plus content-addressed artifacts. Worker executes a registered handler in a separate process and returns a result manifest plus content-addressed outputs. Parent validates and imports the result, updates run/checkpoint provenance, and only then may a parent evaluator create evidence.

**Tech Stack:** Python 3.12+, stdlib dataclasses/json/hashlib/subprocess/pathlib, existing SQLite/BlobStore/EventLedger/WorldRegistry/CheckpointRepository, pytest.

## Global Constraints

- No new mandatory third-party runtime dependencies.
- Worker must not open parent SQLite DB.
- No worker-created EvidencePacket, CommitRecord, LearningEvent, or TCD update.
- Every artifact must be SHA-256 validated before acceptance.
- Exact `world_id`, `run_id`, and envelope digest matching is mandatory.
- Parent historical time must not advance due to worker execution.

---

### Task 1: Worker protocol objects and deterministic digests

**Files:**
- Create: `src/wdc/worker_protocol.py`
- Test: `tests/test_worker_protocol.py`

**Interfaces:**
- Produces: `ArtifactDescriptor`, `WorkerEnvelope`, `WorkerResult`, `WorkerResultStatus`, `canonical_json_bytes()`.

- [x] Write tests for round-trip serialization, deterministic digest, and tamper detection.
- [x] Run targeted tests and verify RED because `wdc.worker_protocol` does not exist.
- [x] Implement immutable protocol dataclasses and canonical JSON encoding.
- [x] Run targeted tests and full suite; verify GREEN.
- [x] Commit `feat: add worker protocol envelopes`.

### Task 2: Content-addressed worker transport staging

**Files:**
- Create: `src/wdc/worker_transport.py`
- Test: `tests/test_worker_transport.py`

**Interfaces:**
- Consumes: worker protocol artifact descriptors.
- Produces: `WorkerTaskDirectory.stage()`, `load_envelope()`, `put_output()`, `load_result()`.

- [x] Write tests for staged input verification and tampered-file rejection.
- [x] Run targeted tests and verify RED.
- [x] Implement task directory layout and SHA-256 validation.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: add worker artifact transport`.

### Task 3: Worker runtime and reference Python-state handler

**Files:**
- Create: `src/wdc/worker_runtime.py`
- Test: `tests/test_worker_runtime.py`

**Interfaces:**
- Produces: `WorkerHandlerRegistry`, `WorkerRuntime.execute(envelope, task_dir)` and registered `python-state-grid-v1` handler.

- [x] Write tests that execute action sequences and return outcome/trace/checkpoint artifacts.
- [x] Run targeted tests and verify RED.
- [x] Implement handler registry/runtime/reference handler using `PythonStateWorld`.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: add isolated worker runtime`.

### Task 4: Subprocess worker entrypoint and client

**Files:**
- Create: `src/wdc/worker.py`
- Create: `src/wdc/worker_client.py`
- Test: `tests/test_worker_subprocess.py`

**Interfaces:**
- Produces: `python -m wdc.worker execute --task-dir PATH`, `StdioWorkerClient.execute(task_dir)`.

- [x] Write subprocess test from a task directory with no parent DB argument.
- [x] Run targeted tests and verify RED.
- [x] Implement worker CLI entrypoint and subprocess client.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: add subprocess worker client`.

### Task 5: Parent result ingest, run update, checkpoint/event import

**Files:**
- Create: `src/wdc/worker_ingest.py`
- Modify: `src/wdc/worlds.py`
- Test: `tests/test_worker_ingest.py`

**Interfaces:**
- Produces: `WorkerResultIngestor.ingest(...)`, `WorldRegistry.complete_run(...)`.

- [x] Write tests for identity mismatch rejection, artifact digest rejection, run completion, checkpoint import, and parent-internal events.
- [x] Assert evidence packet count stays unchanged and TCD parent time stays unchanged.
- [x] Run targeted tests and verify RED.
- [x] Implement minimal parent-side ingest/update logic.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: ingest remote worker results safely`.

### Task 6: CLI and end-to-end remote-world demo

**Files:**
- Modify: `src/wdc/cli.py`
- Create: `examples/remote_world_execution.py`
- Test: `tests/test_cli_worker.py`
- Test: `tests/test_remote_world_execution.py`
- Modify: `README.md`

**Interfaces:**
- Produces CLI groups `wdc worker stage`, `wdc worker execute`, `wdc worker ingest`, and demo `wdc demo remote-world`.

- [x] Write CLI/integration tests for stage -> subprocess execute -> ingest -> explicit parent EvidencePacket creation.
- [x] Verify worker execution alone produces zero evidence and no TCD time advance.
- [x] Run targeted tests and verify RED.
- [x] Implement CLI handlers and demo dispatch.
- [x] Run full suite, compileall, diff-check, live demo, wheel build/clean-venv installed demo.
- [x] Write `PHASE13_IMPLEMENTATION_REPORT.md`, update README, and commit.

### Completion Gate

- [ ] Full source-tree test suite passes.
- [ ] `python -m compileall -q src/wdc examples` passes.
- [ ] `git diff --check` passes.
- [ ] Source-tree `wdc demo remote-world` passes.
- [ ] Wheel installs in a clean venv and installed `wdc demo remote-world` passes.
- [ ] Tracked-only Source ZIP fresh extraction passes tests + demo.
- [ ] Final Source ZIP, Git bundle, wheel, report, and delivery manifest are generated from final HEAD.
