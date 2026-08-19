# DEST Runtime v0.1 Architecture

## Kernel

```text
State Store
Event Ledger
Schema Registry
Guard Engine
Certificate Graph
Replay Engine
```

## Main invariant

No proposal becomes canonical silently.

## State mutation

The active state is a projection over an append-only event log. v0.1 implements only a small set of events on purpose.

## Certificates

Certificates are scoped and versioned. Dependency edges form a DAG-like graph. Revoking/failing/staling an upstream certificate causes descendants to become `STALE`.

This is a lifecycle mechanism, not a truth oracle.

## Benchmark

The bundled 100 cases are **contract conformance tests**, organized as 10 categories × 10 cases.

The full DEST policy is a deterministic reference implementation of the v0.1 distinctions.  
The flat baseline deliberately ignores most distinctions.

Therefore the benchmark demonstrates that the implementation conforms to the specification; it does **not** demonstrate independent scientific superiority.

## Next benchmark tier

An independent oracle pack should be authored without looking at the reference policy. That pack should include:

- hidden expected state transitions
- mutation testing
- adversarial retrieval
- delayed certificate invalidation
- branch/global-glue failures
- replay after schema/version migration
