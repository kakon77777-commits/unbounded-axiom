# Phase 14 Worker Registry / Lease / Heartbeat / Retry / Remote Launchers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add durable worker liveness, task leases, fencing/retry coordination, and protocol-aware local/Ray/Kubernetes launchers around the Phase 13 WorkerEnvelope execution model.

**Architecture:** Parent owns WorkerRegistry and WorkerCoordinator. Workers receive time-bounded assignments with attempt/fencing metadata. Launchers execute the existing WorkerEnvelope protocol, while coordinator validation fences stale results before Phase 13 parent ingest. Local launch is fully executable; Ray/Kubernetes remain optional dependency-gated adapters.

**Tech Stack:** Python 3.12+, stdlib dataclasses/enum/datetime/sqlite3/subprocess/pathlib/json, existing WDC DB/worker/scheduler modules, optional Ray/kubectl, pytest.

## Global Constraints

- No new mandatory third-party runtime dependencies.
- Registry/lease/launcher code must not create EvidencePackets, CommitRecords, LearningEvents, or TCD updates.
- Only one ACTIVE lease may exist per task.
- Lease is bound to exact task/envelope/worker/attempt/fencing metadata.
- Fencing token must increase monotonically across retries.
- Late/stale attempt results must be rejected before WorkerResultIngestor imports artifacts.
- Kubernetes writes remain disabled by default.
- Ray/Kubernetes live execution may not be claimed verified unless dependencies/cluster are actually available.

---

### Task 1: Worker registry and heartbeat persistence

**Files:**
- Create: `src/wdc/worker_registry.py`
- Test: `tests/test_worker_registry.py`

**Interfaces:**
- Produces: `WorkerStatus`, `WorkerRecord`, `WorkerRegistry.register()`, `heartbeat()`, `mark_stale()`, `get()`, `list_workers()`.

- [x] Write failing tests for registration, heartbeat renewal, stale transition, stale-to-active recovery, and capacity fields.
- [x] Run targeted tests; verify RED because registry module does not exist.
- [x] Implement immutable records plus SQLite tables/queries.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: add worker registry and heartbeats`.

### Task 2: Task leases, attempts, fencing, and retry directives

**Files:**
- Modify: `src/wdc/worker_registry.py`
- Test: `tests/test_worker_leases.py`

**Interfaces:**
- Produces: `TaskLeaseStatus`, `TaskLease`, `RetryDirective`, registry methods `acquire_lease()`, `renew_lease()`, `expire_leases()`, `complete_lease()`, `active_lease_for_task()`.

- [x] Write failing tests for one-active-lease invariant, wrong-worker renewal rejection, expiry, monotonic attempts/fencing, and retry directive creation.
- [x] Run targeted tests; verify RED.
- [x] Implement lease/retry persistence and deterministic expiry logic.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: add fenced task leases and retry directives`.

### Task 3: Worker coordinator and stale-result fencing

**Files:**
- Create: `src/wdc/worker_coordinator.py`
- Test: `tests/test_worker_coordinator.py`

**Interfaces:**
- Produces: `WorkerAssignment`, `AssignmentResult`, `WorkerCoordinator.assign()`, `heartbeat()`, `sweep()`, `accept_result()`.
- Consumes: `WorkerEnvelope`, `WorkerResult`, `WorkerRegistry`.

- [x] Write failing tests for assignment eligibility, assignment attempt/fence metadata, expired-attempt result rejection, wrong-worker result rejection, and accepted-result lease completion.
- [x] Run targeted tests; verify RED.
- [x] Implement coordinator logic without artifact ingest/evidence/TCD side effects.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: coordinate workers with fencing tokens`.

### Task 4: Lease-aware local launcher and parent ingest integration

**Files:**
- Create: `src/wdc/worker_launcher.py`
- Test: `tests/test_worker_launcher_local.py`

**Interfaces:**
- Produces: `WorkerLauncher` protocol, `LocalWorkerLauncher.launch_and_ingest(...)`.
- Consumes: Phase 13 `WorkerTaskDirectory`, `StdioWorkerClient`, `WorkerResultIngestor`, `WorkerCoordinator`.

- [x] Write failing end-to-end tests for stage -> assign -> execute -> accept -> ingest -> complete lease.
- [x] Assert registry/launcher activity creates zero evidence and no TCD time advance.
- [x] Add stale late-result test using expired attempt then retry.
- [x] Run targeted tests; verify RED.
- [x] Implement local launcher with coordinator validation before ingest.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: add lease-aware local worker launcher`.

### Task 5: Optional Ray/Kubernetes worker launchers

**Files:**
- Create: `src/wdc/worker_launcher_ray.py`
- Create: `src/wdc/worker_launcher_kubernetes.py`
- Test: `tests/test_worker_launchers_distributed.py`

**Interfaces:**
- Produces: `RayWorkerLauncher.render()/launch()`, `KubernetesWorkerLauncher.render_job()`, `render_lease()`, dependency/default-deny live launch methods.

- [x] Write failing tests for Ray import-safe render, dependency error, Kubernetes Job/Lease manifests, `backoffLimit=0`, deadline/TTL mapping, assignment labels, and default-deny cluster writes.
- [x] Run targeted tests; verify RED.
- [x] Implement minimal optional adapters using current Phase 12 scheduler mappings.
- [x] Run targeted/full tests; verify GREEN.
- [x] Commit `feat: add protocol-aware remote worker launchers`.

### Task 6: CLI, retry demo, packaging, and reports

**Files:**
- Modify: `src/wdc/cli.py`
- Create: `examples/worker_leases.py`
- Test: `tests/test_cli_worker_registry.py`
- Test: `tests/test_worker_leases_demo.py`
- Modify: `README.md`
- Create: `PHASE14_IMPLEMENTATION_REPORT.md`

**Interfaces:**
- Produces CLI commands `wdc workers register`, `heartbeat`, `list`, `assign`, `sweep`, `lease`, `render-launch`, plus demo `wdc demo worker-leases`.

- [x] Write failing CLI/integration tests for registration, heartbeat, lease assignment, expiry/retry, stale-result fencing, and demo output.
- [x] Run targeted tests; verify RED.
- [x] Implement CLI handlers and end-to-end demo.
- [x] Run full suite, compileall, diff-check, live demo, wheel build and clean-venv installed demo.
- [x] Write/update report and README; commit.

### Completion Gate

- [x] Full source-tree test suite passes.
- [x] `python -m compileall -q src/wdc examples` passes.
- [x] `git diff --check` passes.
- [x] Source-tree `wdc demo worker-leases` passes.
- [x] Wheel installs in a clean venv and installed `wdc demo worker-leases` passes.
- [x] Tracked-only Source ZIP fresh extraction passes tests + demo.
- [ ] Final Source ZIP, Git bundle, wheel, report, and delivery manifest are generated from final HEAD.
