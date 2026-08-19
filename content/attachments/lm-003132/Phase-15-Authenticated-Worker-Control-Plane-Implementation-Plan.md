# Phase 15 Authenticated Worker Control Plane Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an authenticated HTTP/JSON worker control plane and content-addressed artifact service that runs the existing WorkerEnvelope/lease/fencing/result protocol without shared parent filesystem access.

**Architecture:** Add small auth, artifact-service, control-service, HTTP reference server/client modules. Reuse Phase 13/14 WorkerEnvelope, WorkerRuntime, WorkerCoordinator, WorkerRegistry and WorkerResultIngestor. Keep all epistemic authority parent-side.

**Tech Stack:** Python 3.12+ standard library (`hmac`, `hashlib`, `http.server`, `urllib.request`, `sqlite3`) plus existing WDC runtime modules.

## Global Constraints

- No new required third-party runtime dependency.
- Worker identity is bound to credential and worker generation.
- All artifacts are content-addressed SHA-256 objects.
- Remote workers never receive parent DB path/runtime root.
- Remote result submission must pass current lease/attempt/fencing validation before parent ingest.
- HTTP transport must not create EvidencePacket, CommitRecord, LearningEvent or TCD sedimentation on its own.
- Existing Phase 0–14 tests remain green.

---

### Task 1: Worker Credential Authority

**Files:**
- Create: `src/wdc/worker_auth.py`
- Test: `tests/test_worker_auth.py`

**Interfaces:**
- Produces: `WorkerCredentialAuthority.issue(...) -> str`, `verify(token, required_scope, expected_worker_id, now=None) -> WorkerCredentialClaims`.

- [x] **Step 1: Write failing tests** for valid token, tamper rejection, expiry, wrong scope/worker, and worker-generation invalidation.
- [x] **Step 2: Run targeted tests and verify RED.**
- [x] **Step 3: Implement HMAC-SHA256 canonical JSON bearer credentials with constant-time signature comparison.**
- [x] **Step 4: Run targeted and full tests; verify GREEN.**
- [x] **Step 5: Commit.**

### Task 2: Distributed Artifact Service

**Files:**
- Create: `src/wdc/artifact_service.py`
- Test: `tests/test_distributed_artifact_service.py`

**Interfaces:**
- Produces: `DistributedArtifactService.put(expected_sha256, data, mime_type)`, `get(sha256)`, `exists(sha256)`.

- [x] **Step 1: Write failing tests** for upload/download, digest mismatch, missing artifact and corruption detection.
- [x] **Step 2: Verify RED.**
- [x] **Step 3: Implement using existing BlobStore.**
- [x] **Step 4: Run targeted/full tests.**
- [x] **Step 5: Commit.**

### Task 3: Worker Control Service

**Files:**
- Create: `src/wdc/worker_control.py`
- Test: `tests/test_worker_control_service.py`

**Interfaces:**
- Produces: immutable queued task store, `submit_task`, `poll_assignment`, `heartbeat`, `renew`, `submit_result`.
- Consumes: `WorkerRegistry`, `WorkerCoordinator`, `WorkerResultIngestor`, `DistributedArtifactService`.

- [x] **Step 1: Write failing tests** for queued assignment, eligibility, renewal, stale fencing rejection, duplicate result and parent ingest.
- [x] **Step 2: Verify RED.**
- [x] **Step 3: Implement persisted control tasks and result bridge.**
- [x] **Step 4: Run targeted/full tests.**
- [x] **Step 5: Commit.**

### Task 4: Authenticated HTTP Reference Server + Client

**Files:**
- Create: `src/wdc/worker_http.py`
- Create: `src/wdc/worker_remote_client.py`
- Test: `tests/test_worker_http_control_plane.py`

**Interfaces:**
- Produces: `WorkerHTTPServer`, `RemoteWorkerClient`.

- [x] **Step 1: Write failing localhost HTTP tests** for unauthorized, wrong scope, heartbeat, assignment, renew, artifact PUT/GET and result submission.
- [x] **Step 2: Verify RED.**
- [x] **Step 3: Implement standard-library HTTP server and urllib client.**
- [x] **Step 4: Run targeted/full tests.**
- [x] **Step 5: Commit.**

### Task 5: Remote Worker One-Shot Execution

**Files:**
- Modify: `src/wdc/worker_remote_client.py`
- Create: `tests/test_remote_worker_network_execution.py`

**Interfaces:**
- Produces: `RemoteWorkerClient.run_once(worker_runtime, ...)` that polls, downloads inputs, executes existing handler, uploads outputs, submits result.

- [x] **Step 1: Write failing end-to-end localhost test** proving no shared parent filesystem is required and evidence/TCD remain unchanged after transport/ingest.
- [x] **Step 2: Verify RED.**
- [x] **Step 3: Implement one-shot network execution.**
- [x] **Step 4: Run targeted/full tests.**
- [x] **Step 5: Commit.**

### Task 6: CLI + Phase 15 Demo + Packaging

**Files:**
- Modify: `src/wdc/cli.py`
- Create: `examples/network_worker.py`
- Test: `tests/test_cli_worker_control.py`
- Test: `tests/test_network_worker_demo.py`
- Modify: `README.md`
- Create: `PHASE15_IMPLEMENTATION_REPORT.md`

**Interfaces:**
- CLI: `wdc control credential`, `wdc control submit`, `wdc control serve`, `wdc remote-worker once`, `wdc demo network-worker`.

- [x] **Step 1: Write failing CLI/demo tests.**
- [x] **Step 2: Verify RED.**
- [x] **Step 3: Add CLI/demo without duplicating domain logic.**
- [x] **Step 4: Run full suite, compileall, `git diff --check`, source demo.**
- [x] **Step 5: Build wheel and verify installed CLI/demo in clean venv.**
- [x] **Step 6: Produce tracked-only Source ZIP; fresh-extract full tests/demo.**
- [x] **Step 7: Produce final bundle/wheel/report/delivery manifest.**
