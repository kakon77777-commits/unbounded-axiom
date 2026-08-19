# Phase 17 Implementation Report — HA Control Plane + Object Store Substrates

Date: 2026-08-18
Branch: `feature/phase17`
Base: Phase 16 final HEAD `d66c260c6c6395c591164e36e405d3ced75e9fe6`
Status: implementation complete; tracked-only archive gate verified; delivery checklist complete.

## Scope

Phase 17 adds deployment-substrate HA/storage mechanics without changing WDC epistemic semantics.

Implemented:

- `ControllerRegistry` with controller identity, heartbeat, leader lease, monotonic controller epoch, renew/release/expiry, and stale-epoch fencing;
- concurrent SQLite reference leader acquisition serialized with `BEGIN IMMEDIATE`;
- `ControlStateBackend` protocol and SQLite namespaced byte state with version/CAS;
- import-safe `PostgresControlStateBackend` using an injected DB-API connection factory;
- PostgreSQL migration/locking SQL including row-lock and `SKIP LOCKED` coordination hooks;
- `RedisCompatibleRequestBackend` with `SET NX` idempotency reservation and a real atomic Lua token-bucket state machine;
- local distributed-request fallback;
- `ObjectStoreBackend` protocol;
- `LocalObjectStoreBackend` with WDC SHA-256 integrity revalidation;
- injected-client `S3ObjectStoreBackend` using SHA-derived keys and `wdc-sha256` metadata;
- provider presigned GET/PUT mapping while retaining WDC SHA-256 as identity;
- `SubstrateConfig` / `SubstrateFactory` reference selection surface;
- `wdc ha ...` and `wdc storage ...` CLI groups;
- `wdc demo ha-control-plane`.

## Critical Invariants

```text
LeaderElection != EpistemicAuthority
SharedDatabase != SharedTruth
ObjectStoreDurability != EvidenceValidity
ControllerFailover != WorldRetry
ControllerEpoch != WorkerFencingToken
ETag != WDCContentIdentity
```

## HA Reference Demo

The demo uses two independent SQLite connections pointing at one shared control DB.

Observed reference result:

```text
leader_before = controller-a
epoch_before = 1
leader_after = controller-b
epoch_after = 2
stale_epoch_rejected = true
idempotency_survived_failover = true
artifact_roundtrip = true
evidence = 0 -> 0
parent_time = 0 -> 0
```

## Concurrency Hardening

Self-review found that the first SQLite reference `acquire()` implementation could permit two concurrent controller threads to both report successful leadership. A regression test reproduced two successes.

The reference acquisition path was changed so the complete transition:

```text
inspect current lease
-> expire if necessary
-> increment controller epoch
-> write new lease
```

runs under one `BEGIN IMMEDIATE` transaction. The concurrent regression now produces exactly one winner and one `ControllerLeadershipError`.

This is a single-host SQLite reference mechanism, not a claim that SQLite is an appropriate multi-host HA database.

## Redis-Compatible Adapter Hardening

Self-review also found the initial Redis token-bucket string was only a placeholder despite fake-client tests exercising the intended behavior. It was replaced with an actual Lua state machine using:

```text
HMGET
HSET
PEXPIRE
```

for atomic token/timestamp update and expiry.

## Production Adapter Status

### Local SQLite / local object store

Status: **live reference tested in this environment**.

### PostgreSQL

Status: **adapter contract tested, live service not tested**.

The adapter is import-safe without psycopg and accepts an injected DB-API connection factory. SQL contracts include `FOR UPDATE` and `SKIP LOCKED` coordination forms.

### Redis-compatible backend

Status: **adapter/Lua contract tested, live Redis service not tested**.

### S3-compatible backend

Status: **adapter contract tested with an injected fake S3 client, live S3 service not tested**.

The adapter intentionally does not use ETag as WDC identity. Downloaded bytes are re-hashed against the requested WDC SHA-256.

## Preliminary Verification

Source tree:

```text
207 passed
compileall: PASS
git diff --check: PASS
```

Source-tree demo:

```text
wdc demo ha-control-plane: PASS
```

Clean-venv installed wheel:

```text
storage backends: PASS
ha controller-register: PASS
ha acquire: PASS
ha-control-plane demo: PASS
```

## Explicit Limitations

Not claimed as live-tested in Phase 17:

- PostgreSQL server connectivity/failover;
- Redis server/cluster execution;
- S3/GCS/Azure live object storage;
- multi-controller shared PostgreSQL deployment;
- cross-controller distributed rate-limit consistency under network partition;
- object-store multipart upload orchestration;
- controller quorum/consensus beyond lease/epoch leadership.

Phase 17 establishes the substrate interfaces and failover semantics needed for those production deployments without changing the Phase 0–16 epistemic model.
## Tracked-Only Archive Verification

A `git archive` source ZIP from the feature HEAD was extracted into a fresh directory and independently verified:

```text
207 passed
compileall: PASS
ha-control-plane demo: PASS
wheel rebuilt from extracted ZIP: PASS
clean-venv installed demo: PASS
```

The final delivery hashes are intentionally recorded outside the repository to avoid artifact self-reference.

## Delivery Checklist

A candidate Source ZIP, Git bundle, wheel, and report were generated from the completed feature branch before the final metadata commit. Final delivery artifacts are rebuilt from the final metadata HEAD and their SHA-256 values are recorded in an external delivery manifest.
