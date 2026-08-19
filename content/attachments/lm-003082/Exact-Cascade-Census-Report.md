# DEST v0.8 — Exact Cascade Census Report

**Date:** 2026-08-14  
**Model:** Fixed-Cost Certificate Cascade Model  
**Parent runtime:** DEST Runtime v0.7-alpha

## Executive result

The v0.7 empirical zero-violation structural signal decomposes into two mathematically distinct objects.

### Theorem region

Pure deterministic cascade utility:

```text
inspection
→ fixed affected closure
→ nonnegative target weights
→ weighted union coverage
```

is a normalized, monotone, submodular set function.

Exact structural census:

- ordered DAGs through `n <= 5`: **1099**
- exact new-coverage inclusion checks: **421861**
- violations: **0**

### Mixed revoke–release region

Exact `n <= 4` census with regression weights `invalid=0.1`, `release=1.0` contains **1098** complete DAG/status models.

Results:

- non-monotone: **537**
- non-submodular: **160**
- models with a valid release node having >=2 invalid blockers: **160**
- such models that are non-submodular: **160**

So for this exact regression census, **160/160** multi-blocker models violate submodularity.

The analytical theorem is stronger and cleaner:

```text
if every positive-release valid node has at most one invalid blocker
→ mixed utility is submodular
```

for arbitrary nonnegative revocation coverage weights.

## Minimal counterexamples

### Non-monotonicity

Minimum size: **2 nodes**

```json
{
  "n": 2,
  "edges": [
    [
      0,
      1
    ]
  ],
  "invalid": [
    0
  ],
  "valid": [
    1
  ],
  "witness": {
    "S": [
      1
    ],
    "e": 0,
    "F_S": 1.0,
    "F_Se": 0.1
  },
  "blockers": {
    "1": [
      0
    ]
  }
}
```

### Non-submodularity

Minimum size: **3 nodes**

```json
{
  "n": 3,
  "edges": [
    [
      0,
      1
    ],
    [
      1,
      2
    ]
  ],
  "invalid": [
    0,
    1
  ],
  "valid": [
    2
  ],
  "witness": {
    "S": [
      2
    ],
    "T": [
      0,
      2
    ],
    "e": 1,
    "delta_S": -0.9,
    "delta_T": 0.0
  },
  "blockers": {
    "2": [
      0,
      1
    ]
  }
}
```

The minimum non-submodular witness is a chain, not a fork:

```text
invalid → invalid → valid-release
```

The last node has two nested blockers.

## Blocker-at-most-one exact regression

- complete models checked through `n <= 4`: **938**
- violations: **0**

This is a computational companion to the analytic proof.

## Scope boundary

The theorem does **not** extend automatically to belief-conditioned probability updates, deadlines, dynamic inspection costs, branch-dependent release values, history-dependent utility, interaction bonuses, or arbitrary quarantine policies.

Those mechanisms change the problem from fixed weighted coverage to a state/history-dependent optimization process.

## Mathematical compression of the Runtime result

The correct v0.8 statement is:

**Fixed deterministic cascade coverage is submodular.**

It is not:

**DEST is submodular.**

And the first deterministic break already appears at:

**two blockers + one positive release.**
