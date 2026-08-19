# Phase 15 Implementation Report — Authenticated Worker Control Plane + Distributed Artifact Service

**Date:** 2026-08-18  
**Branch:** `feature/phase15`  
**Base:** Phase 14 (`eb3392c5e92d0a67d993b635acd1f7caa966b564`)  
**Status:** Phase 15 implementation and tracked-artifact verification complete.

## 1. Scope

Phase 15 removes the shared-parent-filesystem requirement from the Phase 13/14 worker path by adding a reference authenticated HTTP/JSON control plane and content-addressed artifact transfer service.

It does **not** move Governor, Evidence, Commit, Learning, or TCD authority onto remote workers.

## 2. Added modules

- `wdc.worker_auth` — HMAC-SHA256 scoped bearer credentials bound to worker identity and registry generation.
- `wdc.artifact_service` — SHA-256 addressed artifact metadata/storage service over the existing BlobStore.
- `wdc.worker_control` — durable network task queue, assignment/lease bridge, result validation and parent ingest bridge.
- `wdc.worker_http` — standard-library HTTP reference server.
- `wdc.worker_remote_client` — urllib-based authenticated worker client and one-shot remote execution path.
- `examples.network_worker` — full localhost parent/server/remote-node demonstration.

## 3. Authentication

Credential claims contain:

```text
credential_id
worker_id
worker_generation
scopes
issued_at
expires_at
nonce
```

The token uses canonical JSON plus HMAC-SHA256. Verification uses constant-time signature comparison and checks the current `WorkerRegistry.generation`; re-registering a worker invalidates its old credentials.

Reference scopes:

```text
worker:heartbeat
worker:lease
artifact:read
artifact:write
result:submit
```

Worker-specific routes also enforce that the bearer identity matches the path worker ID.

## 4. Artifact service

Uploads are accepted only when:

```text
SHA256(body) == requested digest
```

Reads re-verify the stored BlobStore digest. HTTP artifact access is additionally bound to an active task lease:

- GET may read only SHA-256 objects declared as inputs of the worker's active assignment.
- PUT requires that the bearer worker currently holds the active lease for the supplied task ID.

The remote worker does not receive or dereference parent filesystem URIs.

## 5. Network control flow

```text
Parent WorldRun
  -> WorkerEnvelope
  -> network task queue
  -> authenticated assignment poll
  -> TaskLease + fencing token
  -> SHA input download
  -> local WorkerRuntime execution on remote node
  -> SHA output upload
  -> WorkerResult submit
  -> parent fence/result/artifact validation
  -> WorkerResultIngestor
  -> WorldRun / Checkpoint / PARENT_INTERNAL Event
```

Transport alone does not create EvidencePacket and does not advance TCD parent historical time.

## 6. Reference HTTP endpoints

```text
GET  /v1/health
POST /v1/workers/{worker_id}/heartbeat
GET  /v1/workers/{worker_id}/assignment
POST /v1/workers/{worker_id}/leases/{lease_id}/renew
PUT  /v1/artifacts/{sha256}
GET  /v1/artifacts/{sha256}
POST /v1/workers/{worker_id}/results
```

The reference server serializes access to the single SQLite connection. `WDCDB` now permits cross-thread use so the localhost server thread can use the same RuntimeContext, while the HTTP layer serializes requests rather than claiming concurrent-database scalability.

## 7. CLI

```text
wdc control credential --secret-file ... --json ...
wdc control submit --json ...
wdc control serve --secret-file ... [--host ... --port ...]
wdc remote-worker once --base-url ... --worker-id ... --token-file ... --work-root ...
wdc demo network-worker
```

`control` is parent/admin-side. `remote-worker` requires only network URL, scoped token, and a worker-local work directory.

## 8. Security hardening verified

- token tamper rejected;
- expired token rejected;
- wrong scope rejected;
- wrong worker identity rejected;
- worker re-registration invalidates prior generation tokens;
- HTTP body size is bounded;
- artifact bytes are content-addressed and reverified;
- artifact read/write is active-task-bound;
- stale/wrong fencing token is rejected before parent ingest;
- duplicate result submission is rejected;
- network transport does not create evidence or TCD history.

## 9. Preliminary verification evidence

```text
full test suite: 167 passed
compileall src/wdc examples: PASS
git diff --check: PASS
source-tree network-worker demo: PASS
wheel build: PASS
clean-venv install: PASS
installed `wdc control --help`: PASS
installed `wdc remote-worker --help`: PASS
installed network-worker demo: PASS
```

Demo evidence:

```text
worker_status = SUCCEEDED
run_status = COMPLETED
shared_parent_task_dir = false
artifact_count = 3
evidence = 0 -> 0
parent_time = 0 -> 0
attempt = 1
fencing_token = 1
```

## 10. Explicit limitations

The Phase 15 reference HTTP server is a protocol implementation for localhost/private-network validation. It does **not** claim:

- TLS termination or mTLS;
- public-internet hardening;
- external identity provider/OAuth integration;
- production-grade secret storage or automatic secret rotation;
- artifact quotas or complete denial-of-service controls;
- HA controller/database operation;
- multi-controller consensus;
- object-store presigned URL support.

Use TLS/mTLS and a production secret/identity layer before exposing this control plane beyond a trusted network boundary.

## 11. Tracked-artifact verification

A tracked-only Source ZIP generated directly from Git HEAD was extracted into a fresh directory and independently verified:

```text
fresh Source ZIP full suite: 167 passed
fresh Source ZIP compileall: PASS
fresh Source ZIP network-worker demo: PASS
fresh Source ZIP wheel build: PASS
fresh Source ZIP clean-venv install: PASS
fresh installed `wdc control --help`: PASS
fresh installed `wdc remote-worker --help`: PASS
fresh installed network-worker demo: PASS
```
