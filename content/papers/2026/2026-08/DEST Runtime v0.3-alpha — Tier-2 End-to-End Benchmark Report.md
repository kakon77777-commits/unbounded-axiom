# DEST Runtime v0.3-alpha — Tier-2 End-to-End Benchmark Report

**Date:** 2026-08-13  
**Benchmark:** DEST Tier-2 End-to-End Benchmark v0.1  
**Scenarios:** 10  
**Environment horizon:** 1000 steps  
**Regression tests:** 10/10 PASS

## Aggregate results

| Metric | DEST | Flat baseline |
|---|---:|---:|
| Canonical-state accuracy | 80.0% | 60.0% |
| Branch preservation | 100.0% | 80.0% |
| Absence integrity | 100.0% | 80.0% |
| Representation integrity | 100.0% | 80.0% |
| View integrity | 100.0% | 80.0% |
| Knowledge-state replay | 100.0% | 100.0% |
| Certificate-graph replay | 100.0% | 100.0% |
| Composite integrity | 97.1% | 82.9% |

## Failure/action counts

| Failure | DEST | Flat baseline |
|---|---:|---:|
| False canonical commit attempts | 0 | 22 |
| False absence commitments | 0 | 2 |
| Branch losses | 0 | 2 |
| Representation cheats | 0 | 2 |
| View misses | 0 | 3 |
| Stale active canonical states | 0 | 0 |

## Scenario results

- `E2E-01-stable-valid` — DEST integrity 100.0%, final claim `CANONICAL`; baseline integrity 100.0%, final claim `CANONICAL`.
- `E2E-02-delayed-counterexample` — DEST integrity 100.0%, final claim `REOPENED`; baseline integrity 85.7%, final claim `CANONICAL`.
- `E2E-03-version-drift-recovered` — DEST integrity 100.0%, final claim `CANONICAL`; baseline integrity 100.0%, final claim `CANONICAL`.
- `E2E-04-source-revocation` — DEST integrity 100.0%, final claim `REOPENED`; baseline integrity 85.7%, final claim `CANONICAL`.
- `E2E-05-branch-preservation` — DEST integrity 100.0%, final claim `CANONICAL`; baseline integrity 85.7%, final claim `CANONICAL`.
- `E2E-06-retrieval-miss-and-recovery` — DEST integrity 100.0%, final claim `CANONICAL`; baseline integrity 85.7%, final claim `CANONICAL`.
- `E2E-07-representation-cheat` — DEST integrity 100.0%, final claim `CANONICAL`; baseline integrity 85.7%, final claim `CANONICAL`.
- `E2E-08-loaded-unused-evidence` — DEST integrity 100.0%, final claim `CANONICAL`; baseline integrity 85.7%, final claim `CANONICAL`.
- `E2E-09-hidden-counterexample-unknown` — DEST integrity 85.7%, final claim `CANONICAL`; baseline integrity 85.7%, final claim `CANONICAL`.
- `E2E-10-hidden-source-revoke-unknown` — DEST integrity 85.7%, final claim `CANONICAL`; baseline integrity 28.6%, final claim `CANONICAL`.

## The two intentional DEST misses

### E2E-09 — hidden counterexample, observable status UNKNOWN

The hidden benchmark truth says the counterexample is valid, but the runtime receives:

```text
counterexample_cert = UNKNOWN
```

DEST refuses to fabricate a revocation certificate. The claim remains canonical and hidden final-state accuracy fails.

The next mechanism should be:

```text
UNKNOWN high-impact counterexample
→ verification debt
→ active inspection / independent verifier
→ resolve PASS or FAIL
```

not `UNKNOWN → pretend PASS/FAIL`.

### E2E-10 — hidden source revocation, observable source status UNKNOWN

The hidden source has been revoked, but the runtime only receives an UNKNOWN source status. Automatic revocation would itself overclaim.

The next mechanism is a risk-conditioned revalidation/quarantine queue:

```text
source uncertainty
+ high downstream dependency
→ recheck priority / quarantine policy
```

## Architectural defect discovered and fixed

v0.2 could replay knowledge-state events, but certificate-table mutation was not a first-class ledger stream. Therefore state replay and certificate replay were asymmetric.

v0.3-alpha adds:

```text
CERT_CREATE
CERT_DEPENDENCY
CERT_STATUS
```

plus:

```python
CertificateStore.rebuild_from_ledger()
```

Tier-2 now checks both:

```text
knowledge-state hash
certificate-graph digest
```

after importing the event stream into a fresh runtime.

## Interpretation

Three findings matter more than the aggregate score.

1. **Replay integrity and epistemic governance are independent.**  
   A flat baseline can replay a badly governed world perfectly.

2. **Certificate dependencies matter under delayed invalidation.**  
   Revocation/staleness can propagate through dependency structure instead of silently leaving descendants trusted.

3. **Unknown evidence is a genuine observability ceiling.**  
   The benchmark may know hidden truth while the runtime does not. The next improvement must acquire evidence, not tune directly to hidden answers.

## Limitation

The scenarios and hidden truth are still authored in the same engineering project. This is stronger than module conformance and Tier-1 interaction classification, but not yet an independent external evaluation.

The next defensible tier should use:
- a frozen scenario pack authored independently from the policy;
- hidden oracles inaccessible during tuning;
- real documents/repositories/artifacts;
- tool failures and environment snapshots;
- a budget-matched stateful-RAG/event-runtime baseline;
- explicit abstention/defer scoring.
