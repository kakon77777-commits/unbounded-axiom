# Phase 15 — Authenticated Worker Control Plane + Distributed Artifact Service Design

## Goal

Replace the Phase 13/14 shared-filesystem worker transport with a reference authenticated network control plane while preserving the existing `WorkerEnvelope`, lease/fencing, `WorkerResult`, parent ingest, evidence, and TCD boundaries.

## Chosen approach

Use a zero-third-party-dependency reference stack based on Python standard-library HTTP/JSON. The protocol is deliberately transport-neutral: HTTP is the reference transport, not a new semantic layer. A future gRPC/FastAPI implementation can reuse the same auth, artifact, lease, result, and parent-ingest contracts.

Alternatives considered:

1. **FastAPI/Pydantic immediately** — convenient API ergonomics, but introduces hard dependencies and a second schema authority. Rejected for v0.1.
2. **gRPC/protobuf immediately** — strong typed transport, but too much generated/tooling surface before the protocol stabilizes. Deferred.
3. **Standard-library HTTP/JSON reference implementation** — smallest auditable surface and easiest clean-wheel verification. Selected.

## Architecture

```text
Parent Runtime
  ├─ WorkerCredentialAuthority
  ├─ DistributedArtifactService
  ├─ WorkerControlService
  │    ├─ WorkerRegistry
  │    ├─ WorkerCoordinator
  │    └─ queued WorkerEnvelope records
  ├─ Reference HTTP Server
  └─ Parent WorkerResultIngestor

Remote Worker
  ├─ WorkerCredential
  ├─ RemoteWorkerClient
  ├─ fetch assignment
  ├─ download input artifacts by SHA-256
  ├─ execute existing WorkerRuntime handler
  ├─ upload output artifacts by SHA-256
  └─ submit WorkerResult + attempt/fencing token
```

## Authentication

Use HMAC-SHA256 signed bearer credentials with:

```text
credential_id
worker_id
worker_generation
scopes
issued_at
expires_at
nonce
```

The signed token is verified with constant-time comparison. Verification additionally checks the current `WorkerRegistry.generation`; re-registering the same worker therefore invalidates old credentials without requiring a separate revocation service.

Reference scopes:

```text
worker:heartbeat
worker:lease
artifact:read
artifact:write
result:submit
```

A credential for worker A cannot act as worker B.

## Artifact service

Artifacts are addressed only by SHA-256. Upload requires the URL/path digest to equal the actual body digest. Download verifies the stored content digest before returning bytes.

The remote worker never receives a parent filesystem path. `ArtifactDescriptor.storage_uri` is treated as metadata; remote transfer is keyed only by `sha256`.

## Control service

The parent stores queued network tasks as immutable envelope JSON plus status. A worker polls for an assignment. The control service uses the Phase 14 `WorkerCoordinator` to acquire leases and fencing tokens.

Worker-visible assignment:

```text
WorkerEnvelope
lease_id
attempt
fencing_token
lease_expires_at
```

Heartbeat and lease renewal are separate operations.

## Result submission

A worker uploads output artifacts first, then submits the immutable `WorkerResult` together with `attempt` and `fencing_token`.

The parent must, before ingest:

1. authenticate worker identity;
2. validate current lease holder;
3. validate attempt and fencing token;
4. validate result digest and envelope binding;
5. ensure every output artifact exists and matches digest/size;
6. materialize a parent-local temporary task representation or call a direct parent ingest bridge;
7. call existing parent-side `WorkerResultIngestor`;
8. only then complete the lease.

The worker cannot directly insert `EvidencePacket`, `CommitRecord`, learning state, or TCD sedimentation.

## HTTP reference endpoints

```text
POST /v1/workers/{worker_id}/heartbeat
GET  /v1/workers/{worker_id}/assignment
POST /v1/workers/{worker_id}/leases/{lease_id}/renew
PUT  /v1/artifacts/{sha256}
GET  /v1/artifacts/{sha256}
POST /v1/workers/{worker_id}/results
GET  /v1/health
```

Task submission and credential issuance remain parent/admin-side library/CLI operations in Phase 15; they are not exposed as unauthenticated public HTTP endpoints.

## Security boundaries

```text
Remote Worker != Governor
Remote Worker != Evidence Authority
Remote Worker != Commit Authority
Remote Worker != TCD Authority
Bearer Credential != Host Credential
Artifact URL != Filesystem Path
```

The reference HTTP server is suitable for localhost/private-network protocol validation. It does not claim TLS termination, mTLS, internet exposure hardening, DDoS protection, or production secret management.

## Failure handling

- expired credential -> 401;
- wrong scope / wrong worker identity -> 403;
- stale fencing token -> 409;
- missing/corrupt artifact -> 409/422;
- no assignment -> 204;
- duplicate accepted result -> 409;
- unknown route -> 404.

## Testing

TDD must cover:

- token signature, expiry, generation invalidation, scope and identity;
- artifact upload/download/tamper;
- authenticated heartbeat/assignment/renew;
- remote worker full localhost HTTP round-trip;
- stale attempt/fencing rejection;
- duplicate result submission;
- no evidence/TCD mutation from transport alone;
- clean-wheel installed server/client/demo.

## Explicit deferrals

- TLS/mTLS and certificate rotation;
- external identity provider/OAuth;
- multi-controller consensus;
- object-store presigned URLs;
- distributed SQL/HA control-plane database;
- production network policy and DDoS controls.
