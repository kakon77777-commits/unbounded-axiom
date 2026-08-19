# DEST Runtime v0.4-alpha — Active Inspection Benchmark Report

**Date:** 2026-08-13  
**Benchmark:** DEST Active Inspection Benchmark v0.1  
**Scenarios:** 12  
**Environment horizon:** 1440 steps  
**Regression tests:** 14/14 PASS

## What v0.4 tests

Tier-2 exposed a real epistemic ceiling:

```text
high-impact evidence signal
+ certificate state UNKNOWN
```

v0.3 correctly refused to invent hidden truth, but then had no active mechanism to resolve the uncertainty.

v0.4 adds the missing transition:

```text
UNKNOWN
→ Verification Debt
→ Inspection Task
→ Risk-conditioned Quarantine
→ New Evidence
→ Restore Canonical OR Revoke/Reopen
```

The environment returns an inspection result only when the runtime has actually created a matching open task.

## Aggregate results

| Metric | DEST v0.4 | DEST v0.3 | Flat |
|---|---:|---:|---:|
| Final-state accuracy | 100.0% | 50.0% | 50.0% |
| Decision coverage | 83.3% | 100.0% | 100.0% |
| Selective risk | 0.0% | 50.0% | 50.0% |
| Unsafe canonical rate | 0.0% | 50.0% | 50.0% |
| Quarantine rate | 16.7% | 0.0% | 0.0% |
| Debt creation recall | 100.0% | 0.0% | 0.0% |
| Inspection task recall | 100.0% | 0.0% | 0.0% |
| Inspection delivery rate | 100.0% | 0.0% | 0.0% |
| State replay | 100.0% | 100.0% | 100.0% |
| Certificate replay | 100.0% | 100.0% | 100.0% |

## Debt accounting

DEST v0.4 created debt for every unknown invalidation signal.

Across the suite:

- resolved debt objects: **10**
- debt objects still open at horizon: **4**
- quarantine events: **10**

The four open debts correspond to unresolved low/medium-risk signals and two high-risk unresolved signals.  
Only the high-risk unresolved cases remain quarantined at the end.

## Why 83.3% decision coverage is not a failure

Two scenarios end with:

```text
QUARANTINED
```

because high-impact evidence remains UNKNOWN and no inspection result arrives before the horizon.

The runtime does not claim:

```text
claim = false
```

It claims:

```text
claim is temporarily withheld from trusted canonical use
pending evidence acquisition
```

This is a governance abstention, not epistemic refutation.

A system that quarantines everything would obtain low risk but terrible coverage.  
Therefore v0.4 reports risk and coverage separately.

## Active inspection is stronger than passive defer

v0.3 behavior:

```text
UNKNOWN
→ do not fabricate answer
→ remain passive
```

v0.4 behavior:

```text
UNKNOWN
→ create typed debt
→ schedule the correct evidence request
→ optionally quarantine by risk
→ consume returned evidence
→ resolve debt
```

The benchmark enforces this distinction by withholding later evidence unless the matching inspection task exists.

## Inspection task types

```text
VERIFY_COUNTEREXAMPLE
REVALIDATE_SOURCE
VERIFY_VERSION
```

Each debt carries:
- subject
- signal type
- risk tier
- impact
- uncertainty
- priority
- quarantine recommendation
- inspection route

## Replay

Verification debts and inspection tasks are part of the main event-sourced state:

```text
DEBT_CREATE
DEBT_STATUS
INSPECTION_CREATE
INSPECTION_STATUS
```

The benchmark retains 100% replay for both knowledge state and certificate graph.

## Current limitation

This benchmark is still synthetic and authored in the same project as the policy.  
The 100% final-state result must therefore be interpreted as:

> the new active-inspection mechanism behaves correctly on the designed partial-observability stress cases.

It is **not** evidence of 100% performance on open-world uncertainty.

The next stronger test should randomize:
- evidence availability time,
- inspection cost,
- false alarms,
- multiple competing debts,
- inspection failures,
- budget exhaustion,

and should include a policy-independent frozen oracle.

## Next engineering frontier

The current scheduler selects the highest static priority:

\[
Priority
=
\frac{RiskWeight\cdot Impact\cdot Uncertainty\cdot Persistence}{Cost}.
\]

The next meaningful question is whether evidence acquisition itself can be optimized under a finite budget:

```text
many open debts
+ limited verifier/tool budget
→ which inspection should run first?
```

That is the natural entry point for a v0.5 **Evidence Acquisition / Budgeted Inspection Benchmark**.
