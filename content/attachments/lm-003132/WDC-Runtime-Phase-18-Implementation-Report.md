# WDC Runtime Phase 18 Implementation Report

**Phase:** 18 — Live Production Service Integration Harness  
**Date:** 2026-08-18  
**Branch:** `feature/phase18`  
**Base:** Phase 17 (`c42215058ec3c214f84668d5c38aa691c8516951`)

## 1. Scope

Phase 18 turns the Phase 17 PostgreSQL/Redis/S3-compatible adapter contracts into an executable integration harness for real services while preserving all existing WDC semantic boundaries.

It adds:

- `integration/compose.yaml` for PostgreSQL 18, Redis 8, and MinIO;
- `IntegrationEnvironment` and `ComposeFaultController`;
- PostgreSQL pool lifecycle, health checks, checksum migrations;
- Redis lifecycle/health/reopen wrapper;
- S3-compatible bucket health, multipart upload, bounded per-part retry, abort, and SHA-256 verification;
- optional live-integration pytest suite;
- wheel-embedded compose/migration resources;
- `wdc integration ...` CLI and `wdc demo live-integration`.

## 2. Permanent boundaries

Phase 18 does not change:

```text
Evidence
TCD
Commit
Learning
Governor
Worker protocol
Worker lease/fencing
Controller epoch semantics
```

Infrastructure failure remains distinct from world/scientific failure.

## 3. PostgreSQL harness

`PostgresService` supports:

- optional Psycopg 3 / psycopg_pool loading;
- min/max pool sizing;
- startup `wait()`;
- pooled `SELECT 1` health checks;
- acquisition/reconnect/idle/lifetime configuration;
- close/reopen lifecycle;
- checksum-tracked migration application.

The packaged migration creates Phase 17 control-state/controller-lease tables. A changed migration with the same ID is rejected by checksum.

Reference basis: PostgreSQL 18 documentation and Psycopg 3 pool documentation (`wait`, health check callback, reconnect timeout).

## 4. Redis harness

`RedisService` supports:

- optional redis-py loading;
- connection URL;
- connect/command timeouts;
- `health_check_interval`;
- retry-on-timeout configuration;
- PING health;
- close/reopen;
- direct construction of the Phase 17 Redis-compatible distributed request backend.

Reference basis: current redis-py production/connect documentation covering connection pools, health checks, timeouts, and retries.

## 5. S3-compatible harness

`S3IntegrationBackend` supports:

- optional boto3 loading;
- bucket health/creation;
- single PUT below threshold;
- multipart upload above threshold;
- bounded retry of only the failed part;
- abort on terminal multipart failure;
- `wdc-sha256` metadata;
- download-time full SHA-256 verification.

WDC content identity remains SHA-256. ETag is provider metadata only.

Reference basis: Amazon S3 multipart upload and checksum documentation.

## 6. Live tests

The test suite includes four live integration tests:

```text
PostgreSQL pool / migration / reopen persistence
Redis health / idempotency / rate limit
S3 small + multipart roundtrip
Compose PostgreSQL/Redis restart recovery
```

All require `WDC_LIVE_INTEGRATION=1`; destructive compose failure injection also requires `WDC_LIVE_COMPOSE=1`.

### Status in this build environment

The build environment had:

```text
Docker: unavailable
Docker Compose: unavailable
PostgreSQL service/client: unavailable
Redis service/client: unavailable
MinIO service/client: unavailable
boto3: available in build environment only
```

Therefore the default full suite reports the four live tests as **explicit skips**. This report does not claim live PostgreSQL/Redis/S3 execution.

## 7. Local verification completed before final archive gate

```text
full source suite: 227 passed, 4 skipped
compileall: PASS
source live-integration demo: PASS
wheel contains compose resource: PASS
wheel contains PostgreSQL migration resource: PASS
clean-venv install: PASS
installed integration capabilities: PASS
installed compose render: PASS
installed integration smoke: PASS
installed live-integration demo: PASS
```

The installed clean-venv demo correctly reported:

```text
live_status = SKIPPED
live_services_tested = []
epistemic_state_mutated = false
```

## 8. What remains for a real service execution environment

Phase 18 deliberately does not claim completion of:

- live PostgreSQL pool/failover testing;
- live Redis reconnect testing;
- live MinIO/S3 multipart testing;
- Docker Compose stop/start/restart fault injection;
- production credentials/TLS for the reference compose services;
- production service HA.

The harness is designed so these tests can be enabled without changing source code once Docker or externally managed service endpoints are available.

## 9. Tracked-source archive gate

A Git-tracked-only candidate Source ZIP was created from the committed Phase 18 tree and extracted into a fresh directory.

Fresh extraction verification:

```text
227 passed, 4 skipped
compileall: PASS
live-integration demo: PASS
live_status: SKIPPED
epistemic_state_mutated: false
```

A delivery candidate ZIP, Git bundle, wheel, and report were also produced before the final metadata commit, so completion metadata is based on existing artifacts rather than anticipated artifacts.

## 10. Delivery interpretation

For Phase 18, the four skipped tests are an intentional part of the result. They mean the harness has live-test wiring but the build host had no live PostgreSQL/Redis/S3/Compose environment. They must not be read as successful live-service tests.

## 11. Final delivery verification

Final source commit:

```text
branch = feature/phase18
HEAD   = 635a03a7e269eb8f717ac449abaffdc1ddbc6fc0
```

Final source-tree verification:

```text
227 passed, 4 skipped
compileall: PASS
git diff --check: PASS
working tree: clean
```

Final Source ZIP fresh extraction:

```text
227 passed, 4 skipped
compileall: PASS
live-integration demo: PASS
live_status: SKIPPED
epistemic_state_mutated: false
```

Final wheel clean-venv verification:

```text
install: PASS
wdc integration capabilities: PASS
wdc integration compose --action render: PASS
wdc integration smoke: PASS
wdc demo live-integration: PASS
```

The four skipped tests are the live PostgreSQL, Redis, S3, and destructive compose failover tests. They remain skipped because the build host had no Docker/PostgreSQL/Redis/MinIO services. They are not counted as successful live-service verification.
