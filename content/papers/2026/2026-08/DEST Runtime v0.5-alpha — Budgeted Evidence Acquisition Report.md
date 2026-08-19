# DEST Runtime v0.5-alpha — Budgeted Evidence Acquisition Report

**Date:** 2026-08-13  
**Benchmark:** DEST Budgeted Evidence Acquisition Benchmark v0.1  
**Episodes:** 30  
**Evidence debts:** 750  
**Total inspection budget:** 408 cost units  
**Regression tests:** 19/19 PASS

## Goal

v0.4 established:

```text
UNKNOWN
→ debt
→ inspection task
→ evidence
```

v0.5 asks the next constrained question:

> If many debts are open at once and inspection budget is limited, which evidence should be acquired first?

The bundled benchmark compares:

```text
FIFO
Risk-only
v0.4 static priority
v0.5 Expected Inspection Value (EIV) + 0/1 knapsack
```

Schedulers receive only public estimates. Hidden fields — actual invalidity, actual inspection resolution, and realized inspection value — are stripped before the policy call.

## Scheduler objective

v0.5 estimates two possible benefits of inspection:

1. **Invalid active claim**  
   Detecting invalidity reduces unsafe canonical exposure.

2. **Valid quarantined claim**  
   Confirming validity can restore lost decision coverage.

For an observed debt, a simplified expected inspection value is:

\[
EIV_i
=
\widehat p_i(resolve)
\left[
\widehat p_i(invalid)V_i^-
+
(1-\widehat p_i(invalid))V_i^+
\right]
U_i,
\]

where \(V_i^-\) and \(V_i^+\) depend on whether the claim is currently canonical or quarantined.  
The scheduler then solves a finite 0/1 knapsack over integer inspection costs.

This is an engineering heuristic, not a claim of a universal value-of-information theorem.

## Aggregate results

| Policy | Total realized value | Aggregate value / clairvoyant oracle | Residual exposure | Unsafe harm | Quarantine burden | Decision coverage |
|---|---:|---:|---:|---:|---:|---:|
| FIFO | 21.561 | 26.2% | 4.392 | 4.271 | 0.121 | 92.1% |
| Risk-only | 40.257 | 48.9% | 3.769 | 3.699 | 0.071 | 92.0% |
| v0.4 static | 49.739 | 60.4% | 3.484 | 3.449 | 0.035 | 88.7% |
| **v0.5 EIV** | **51.371** | **62.4%** | **3.426** | **3.355** | 0.071 | 88.1% |

The clairvoyant oracle sees realized hidden values and is used **only** for regret-style benchmark scoring.

## Paired v0.5 vs v0.4 episode analysis

20,000 paired bootstrap resamples over the 30 episodes:

### Realized inspection value

\[
\Delta V
=
V_{v0.5}-V_{v0.4}
=
0.0544
\]

95% bootstrap interval:

\[
[-0.1007,\ 0.2162]
\]

### Residual exposure

Lower is better:

\[
\Delta E
=
E_{v0.5}-E_{v0.4}
=
-0.0584
\]

95% bootstrap interval:

\[
[-0.2270,\ 0.1065]
\]

### Decision coverage

\[
\Delta C
=
C_{v0.5}-C_{v0.4}
=
-0.0053
\]

95% bootstrap interval:

\[
[-0.0213,\ 0.0093]
\]

## Interpretation

v0.5 currently shows a **small portfolio shift**, not a decisive universal win.

Compared with v0.4 static priority:

- total realized inspection value is higher;
- aggregate value relative to the clairvoyant oracle is higher;
- unsafe harm remaining is lower;
- combined residual exposure is lower;
- decision coverage is slightly lower;
- valid-quarantine release is lower.

The paired intervals should be used to judge how stable these small differences are.  
If an interval crosses zero, the current synthetic suite does not support a strong claim that the corresponding advantage is reliable.

## Why risk-only is insufficient

Risk-only spends budget on high-impact claims even when:

- inspection cost is high;
- resolution probability is low;
- the claim is already quarantined;
- confirming a valid quarantined claim could restore high coverage elsewhere.

The v0.5 portfolio makes these trade-offs explicit.

## Why v0.4 static priority remains competitive

v0.4 already divides by inspection cost and strongly favors high-risk / high-impact / high-uncertainty debts.

It therefore tends to select many cheap inspections and performs especially well on:
- resolution count;
- release of valid quarantined claims;
- decision coverage.

v0.5 is not allowed to erase this result merely because it is the newer scheduler.

## Hidden-state separation

Benchmark item records contain hidden outcomes for scoring, but before scheduler invocation the harness projects each item to a strict public key set.

The policy cannot receive:

```text
actual_invalid
inspection_resolves
realized_value
```

A regression test enforces this boundary.

## Replay

Budget decisions are now first-class state events:

```text
BUDGET_ROUND_OPEN
INSPECTION_SELECTED
BUDGET_ROUND_CLOSE
```

so selection history is replayable with the rest of DEST state.

## External formal alignment

The engineering problem is related to several established lines of work:

- selective classification: risk–coverage trade-offs;
- cost-sensitive active learning: information acquisition with unequal error/query costs;
- adaptive submodular optimization: adaptive information gathering under query/budget constraints;
- stochastic-cost adaptive maximization: selection under uncertain item costs.

DEST does not assume its verification-debt portfolio is submodular, nor that EIV estimates are calibrated.

## Current limitations

1. Estimates are synthetically generated and moderately correlated with hidden truth.
2. Inspection costs are integer and static.
3. Debts are independent in the current portfolio benchmark.
4. Inspection of one debt does not yet update probabilities of related debts.
5. No deadline/dependency cascade is dynamically executed.
6. No learned calibration model estimates \(p(invalid)\) or \(p(resolve)\).
7. Same-project authorship remains a benchmark-validity limitation.

## Next falsifiable frontier

The next stronger experiment should make evidence acquisition **adaptive across rounds**:

```text
inspect A
→ observe result
→ update beliefs / dependencies of B,C,D
→ recompute portfolio
→ spend remaining budget
```

That is where adaptive information-gathering and possible submodular structure become empirically meaningful rather than just analogies.
