# DEST Runtime v0.6-alpha — Adaptive Multi-Round Evidence Acquisition Report

**Date:** 2026-08-13  
**Development benchmark:** 40 episodes × 25 debts = 1,000 debts  
**Frozen holdout:** 60 episodes × 25 debts = 1,500 debts  
**Relation calibration set:** 12,000 independently generated groups  
**Regression suite:** 25 tests after final packaging checks

## 1. Research question

v0.5 chooses a complete evidence portfolio once:

```text
initial beliefs
→ one-shot portfolio
→ inspect selected set
```

v0.6 asks whether sequential evidence acquisition helps:

```text
inspect A
→ observe result
→ update beliefs about related B/C/D
→ recompute remaining portfolio
→ inspect next item
```

The key restriction is that hidden validity outcomes never enter the scheduler.

## 2. Runtime changes

New replayed state:

```text
evidence_beliefs
evidence_relations
```

New event types:

```text
BELIEF_INIT
RELATION_INIT
EVIDENCE_OBSERVED
BELIEF_UPDATE
```

The first implementation replayed the entire ledger after every inspection and was caught by the test suite as an O(T²)-style performance misuse. v0.6 now uses an incremental in-memory projection cache while keeping the event log authoritative and validating full replay at the end of each episode.

## 3. First development result: adaptivity initially lost

On the original 40-episode development set:

| Policy | Total realized value | Avg residual exposure |
|---|---:|---:|
| v0.5 static EIV | 83.018 | 4.0580 |
| v0.6 heuristic adaptive | 79.713 | 4.1420 |
| v0.6 calibrated adaptive | 82.299 | 4.0777 |

The raw adaptive update therefore **made the portfolio worse**.

This falsified the naive rule:

\[
\boxed{\text{correlated debts} + \text{adaptivity} \Rightarrow \text{better scheduling}}
\]

The problem was that relation `strength` was being used as an uncalibrated fixed log-odds shift.

## 4. Separate relation calibration

A new calibration set uses seed `6062026` and 12,000 independently generated evidence groups.

It estimates, by relation-strength bin:

\[
P(target\ invalid\mid source\ invalid)
\]

and:

\[
P(target\ invalid\mid source\ valid).
\]

The calibrated runtime converts these conditional rates into a likelihood-ratio adjustment and tempers it by observed evidence reliability.

This calibration data is separate from both the development and frozen holdout episode seeds.

## 5. Frozen holdout result

The Strong-Coupling Gate (`average relation strength >= 0.75`) was locked before generating the new holdout. The holdout uses seed `20260813606`.

| Policy | Total realized value | Avg residual exposure | Invalid-harm recall | Avg rounds |
|---|---:|---:|---:|---:|
| v0.5 static EIV | 135.777 | 3.8995 | 34.44% | 1.00 |
| v0.6 heuristic adaptive | 137.140 | 3.8764 | 34.37% | 7.78 |
| **v0.6 calibrated adaptive** | **139.564** | **3.8374** | **35.53%** | 7.87 |
| v0.6 coupling-gated | 136.224 | 3.8919 | 34.41% | 1.78 |

Relative to static v0.5, calibrated adaptive raises total realized value by:

\[
2.79\%.
\]

Average residual exposure changes by:

\[
-0.0621.
\]

The fixed coupling gate only produced a small improvement over static and substantially underperformed full calibrated adaptivity on this holdout. Therefore the gate is **not** promoted to the canonical scheduler.

## 6. Paired bootstrap on the 60 holdout episodes

30,000 paired bootstrap resamples:

### Realized inspection value

\[
\Delta V=0.0631\quad\text{per episode}
\]

95% interval:

\[
[-0.0339,\ 0.1609]
\]

### Residual exposure

Lower is better:

\[
\Delta E=-0.0621
\]

95% interval:

\[
[-0.1613,\ 0.0374]
\]

### Invalid-harm recall

\[
\Delta R=0.0109
\]

95% interval:

\[
[-0.0151,\ 0.0382]
\]

All three intervals still cross zero.

Therefore the correct conclusion is:

\[
\boxed{\text{calibrated adaptivity shows a positive holdout signal, but no statistically decisive advantage yet.}}
\]

Episode-level realized-value comparison:

```text
adaptive wins : 24
exact ties    : 24
adaptive loses: 12
```

## 7. What did not survive

### Claim A — “Any adaptive update is better than static scheduling”

Rejected by the development benchmark.

### Claim B — “Strong relation coupling alone tells us when to use adaptivity”

Not supported strongly by the frozen holdout. The 0.75 gate barely improved over static and missed gains captured by full calibrated adaptivity.

### Claim C — “Adaptive-submodular theory automatically applies to DEST debts”

Not established. The cited theory provides guarantees only when its structural assumptions actually hold. DEST currently has no proof that verification-debt utility is adaptive monotone/submodular, especially with branch, certificate, and quarantine interactions.

## 8. External formal alignment

- Golovin & Krause (2011) introduce adaptive submodularity for sequential decisions under partial observability and obtain greedy guarantees when the property holds.
- Parthasarathy (2020) studies adaptive submodular maximization with stochastic item costs and knapsack-style constraints.
- Ma & Tzamos (2023) study buying information for stochastic optimization, including an adaptive setting where information can be purchased after actions.

These are structural backends/analogues, not proofs about DEST.

## 9. Current engineering interpretation

The evidence so far supports a narrower architecture:

```text
relation exists
→ estimate/calibrate evidence transfer
→ update only after resolved observation
→ replay every belief change
→ compare against a strong static portfolio
```

Adaptivity should be earned by calibrated evidence structure, not activated because two debts share a label or embedding cluster.

## 10. Next falsifiable frontier

v0.6 still assumes a fixed relation model and fixed inspection costs. The next stronger runtime should introduce:

```text
dependency cascades
+ certificate revocation graph effects
+ changing inspection cost
+ deadlines
+ multi-round budget carryover
```

and then test whether the marginal value of an inspection exhibits any empirical diminishing-return / adaptive-submodular-like structure.

That test should precede any attempt to claim a theoretical greedy guarantee.
