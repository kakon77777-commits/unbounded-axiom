# Phase 12 Distributed Runtime Adapters Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Add a scheduler abstraction, executable local scheduler, optional Ray/Kubernetes adapters, CLI surface, and integration demo without changing WDC epistemic semantics.

**Architecture:** `wdc.scheduler` owns common workload/resource types and scheduler persistence. `LocalScheduler` executes synchronously; Ray/Kubernetes adapters are optional and render side-effect-free plans, with Kubernetes writes default-denied.

**Tech Stack:** Python 3.11+, standard library, SQLite; optional Ray at runtime; optional `kubectl` for explicitly enabled Kubernetes writes.

## Global Constraints

- Core `dependencies = []` remains unchanged.
- Governor/evidence/TCD/commit/learning semantics must not be modified.
- Use `python -m pytest`, not bare `pytest`, for verification.
- Kubernetes cluster writes are default-deny.
- Ray/Kubernetes adapters must import successfully when dependencies/tools are absent.
- Every production behavior follows RED -> verify RED -> GREEN -> full suite -> commit.

---

### Task 1: Scheduler Core and Persistence

**Files:**
- Create: `src/wdc/scheduler.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_scheduler_core.py`

**Interfaces:**
- Produces `ResourceBundle`, `PlacementStrategy`, `WorkloadSpec`, `Reservation`, `WorkloadHandle`, `WorkloadStatus`, `SchedulerCapabilities`, `SchedulerAdapter`, and `SchedulerStore`.

- [x] **Step 1: Write failing tests** for resource validation, persisted reservation/workload round trips, and infrastructure records not touching evidence/TCD tables.
- [x] **Step 2: Run** `python -m pytest tests/test_scheduler_core.py -q` and verify failure because `wdc.scheduler` is missing.
- [x] **Step 3: Implement minimal core types/tables/store** with immutable dataclasses and JSON persistence.
- [x] **Step 4: Run targeted and full suites** and verify green.
- [x] **Step 5: Commit** `feat: add scheduler core and persistence`.

### Task 2: Local Scheduler

**Files:**
- Modify: `src/wdc/scheduler.py`
- Test: `tests/test_local_scheduler.py`

**Interfaces:**
- Produces `LocalScheduler(capacity, store=None)` implementing the common adapter.

- [x] **Step 1: Write failing tests** for feasibility, reservation accounting, release, synchronous command execution, return code/stdout/stderr, timeout failure, and status persistence.
- [x] **Step 2: Verify RED** with targeted pytest.
- [x] **Step 3: Implement minimal LocalScheduler** using `subprocess.run`, logical resource reservations, and store updates.
- [x] **Step 4: Run targeted/full suites**.
- [x] **Step 5: Commit** `feat: add local scheduler adapter`.

### Task 3: Ray Adapter

**Files:**
- Create: `src/wdc/scheduler_ray.py`
- Test: `tests/test_ray_scheduler_adapter.py`

**Interfaces:**
- Produces `RaySchedulerAdapter` with import-safe `capabilities`, `render`, and optional execution path.

- [x] **Step 1: Write failing tests** that render CPU/GPU/memory/custom resource bundles and placement strategy without Ray installed, and verify execution raises a clear dependency error when Ray is absent.
- [x] **Step 2: Verify RED**.
- [x] **Step 3: Implement render-first adapter** using documented placement-group mapping; import Ray only inside execution methods.
- [x] **Step 4: Run targeted/full suites**.
- [x] **Step 5: Commit** `feat: add optional ray scheduler adapter`.

### Task 4: Kubernetes Adapter

**Files:**
- Create: `src/wdc/scheduler_kubernetes.py`
- Test: `tests/test_kubernetes_scheduler_adapter.py`

**Interfaces:**
- Produces `KubernetesSchedulerAdapter(allow_cluster_writes=False, kubectl='kubectl')`.

- [x] **Step 1: Write failing tests** for `batch/v1 Job`, requests/limits, priorityClassName, runtimeClassName, labels, restart policy, and default-deny submit.
- [x] **Step 2: Verify RED**.
- [x] **Step 3: Implement manifest renderer and guarded kubectl submit** with no Kubernetes Python dependency.
- [x] **Step 4: Run targeted/full suites**.
- [x] **Step 5: Commit** `feat: add kubernetes job scheduler adapter`.

### Task 5: Scheduler CLI

**Files:**
- Modify: `src/wdc/cli.py`
- Test: `tests/test_cli_scheduler.py`

**Interfaces:**
- Adds `scheduler adapters`, `scheduler render`, and `scheduler local-run`.

- [x] **Step 1: Write failing CLI tests** for adapter listing, side-effect-free render, and local-run persistence/output.
- [x] **Step 2: Verify RED**.
- [x] **Step 3: Implement CLI handlers/parsers** that only translate JSON to scheduler service calls.
- [x] **Step 4: Run targeted/full suites**.
- [x] **Step 5: Commit** `feat: expose scheduler adapters through cli`.

### Task 6: Distributed Runtime Integration Demo

**Files:**
- Create: `examples/distributed_runtime.py`
- Modify: `src/wdc/cli.py`
- Test: `tests/test_phase12_distributed_runtime.py`

**Interfaces:**
- Adds `wdc demo distributed-runtime`.

- [x] **Step 1: Write failing integration test** covering Governor allocation -> WorkloadSpec -> LocalScheduler run -> Ray/Kubernetes render, while asserting evidence count and TCD parent time do not change.
- [x] **Step 2: Verify RED**.
- [x] **Step 3: Implement demo using existing world/governor APIs and new scheduler adapters**.
- [x] **Step 4: Run targeted/full suites + compileall + live demo**.
- [x] **Step 5: Commit** `feat: add distributed runtime integration demo`.

### Task 7: Documentation, Packaging, and Delivery Verification

**Files:**
- Modify: `README.md`
- Create: `PHASE12_IMPLEMENTATION_REPORT.md`
- Modify: this plan checklist only after verification evidence exists.

- [x] **Step 1: Document adapter boundary and optional dependency status**; cite current Ray/Kubernetes API assumptions in the report.
- [x] **Step 2: Run** `git diff --check`, `python -m pytest -q`, `python -m compileall -q src/wdc examples`, and live scheduler/demo commands.
- [x] **Step 3: Build wheel** and install into a clean venv; verify `wdc scheduler adapters`, `wdc scheduler render --adapter ray`, `wdc scheduler render --adapter kubernetes`, and `wdc demo distributed-runtime`.
- [x] **Step 4: Create tracked-only Source ZIP, Git bundle, wheel, report, and delivery manifest from final HEAD**.
- [x] **Step 5: Extract final Source ZIP into a fresh directory and rerun full tests + demo**.
