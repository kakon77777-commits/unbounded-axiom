# DEST Runtime v0.7-alpha — Dependency Cascades, Deadlines, Dynamic Costs, and Diminishing-Returns Diagnostic

**Date:** 2026-08-14  
**Frozen holdout:** 60 episodes × 24 certificate/debt nodes = 1,440 nodes  
**Rounds per episode:** 18  
**Diminishing-return comparisons:** 30,000 per diagnostic layer  
**Regression suite:** 30/30 PASS

## 1. Research question

v0.6 established only a calibrated adaptive signal; it did **not** establish adaptive submodularity.

v0.7 asks two different questions:

1. Does explicit certificate dependency structure improve evidence scheduling under deadlines and changing inspection cost?
2. Which parts of the resulting utility exhibit empirical diminishing returns, and which parts break it?

## 2. Runtime additions

New replayed state:

```text
cascade_nodes
cascade_edges
deadline_states
dynamic_costs
adaptive_rounds
```

New event classes:

```text
CASCADE_NODE_INIT
CASCADE_EDGE_INIT
CASCADE_STATUS
DEADLINE_SET
DEADLINE_MISS
DYNAMIC_COST_SET
ADAPTIVE_ROUND_OPEN
ADAPTIVE_ROUND_EVENT
ADAPTIVE_ROUND_CLOSE
```

Each node also receives a real `VERIFICATION` certificate in the existing CertificateStore. Parent→child DAG edges are mirrored into the certificate dependency graph. If an inspected certificate is invalid and revoked, descendant certificates become stale through the normal revocation propagation mechanism.

## 3. Benchmark world

Each episode uses a three-layer DAG:

```text
4 roots
→ 8 middle certificates
→ 12 leaf certificates
```

with overlapping parents.

Every debt has:

- risk / impact / leverage;
- uncertainty;
- current quarantine state;
- deadline;
- base inspection cost;
- dynamic cost profile (`FLAT`, `RISING`, `FALLING`, `U_SHAPE`);
- estimated invalidity and resolution probabilities;
- certificate ancestors / descendants.

Hidden benchmark state contains actual local/effective invalidity and whether inspection resolves. Policies never receive those hidden fields.

Inspection budget arrives gradually and unused budget carries forward.

## 4. Important runtime correction

An early v0.7 implementation removed a debt from the exposure world when inspection itself failed.

That is wrong:

```text
inspection failed
!=
debt resolved
```

The final runtime keeps failed-inspection debts exposed while marking them as attempted so the same task is not retried within the benchmark horizon.

## 5. Holdout scheduler results

| Policy | Avg cumulative exposure ↓ | Avg exposure reduction ↑ | Avg deadline misses ↓ | Avg cascade closures |
|---|---:|---:|---:|---:|
| v0.6 EIV | 11.2597 | 61.79% | 6.27 | 6.25 |
| Deadline-only | 10.6093 | 63.81% | 6.02 | 6.35 |
| Cascade-risk | 9.9367 | 64.64% | 5.20 | 7.78 |
| **v0.7 combined** | **9.6651** | **65.85%** | **5.22** | **7.65** |

Replay audit on a fixed 5-episode v0.7 sample:

```text
knowledge state: True
certificate graph: True
```

## 6. Paired holdout statistics

### v0.7 vs v0.6 EIV

Cumulative exposure difference (lower is better):

\[
\Delta E=-1.5946
\]

95% paired bootstrap interval:

\[
[-2.8335,\ -0.5090]
\]

Deadline-miss difference:

\[
\Delta D=-1.0500
\]

95% interval:

\[
[-1.7667,\ -0.4167]
\]

Exposure-reduction-ratio improvement:

\[
\Delta R=0.0406
\]

95% interval:

\[
[0.0083,\ 0.0767]
\]

These three intervals do not cross zero.

### v0.7 vs Cascade-risk

Exposure difference:

\[
\Delta E=-0.2716
\]

95% interval:

\[
[-0.7933,\ 0.2026]
\]

This interval crosses zero.

Therefore the strongest current conclusion is:

> **Explicit dependency-cascade awareness has a stable benefit over the v0.6 direct-EIV baseline on this holdout. The additional advantage of the full deadline-aware v0.7 score over a simpler cascade-aware scheduler is not yet established.**

## 7. Diminishing-returns diagnostic

The diagnostic intentionally separates three notions.

### A. Pure structural cascade affected-set utility

For sampled \(S\subset T\) and candidate inspection \(e\):

\[
\Delta(e\mid S)\stackrel{?}{\ge}\Delta(e\mid T).
\]

Observed:

```text
violations = 0 / 30000
rate       = 0.0000%
```

This is consistent with a weighted coverage / overlapping-cascade substructure on the sampled worlds, but it is **not a formal proof**.

### B. Belief-conditioned expected marginal score

After resolved evidence changes related invalidity estimates:

```text
violations = 1963 / 30000
rate       = 6.54%
```

So additional observations sometimes **increase** the estimated marginal value of another inspection.

### C. Deadline + dynamic-cost adjusted marginal score

```text
violations = 20309 / 30000
rate       = 67.70%
```

This is a direct empirical counterexample to treating the full runtime objective as globally diminishing-return.

Deadlines can make a later inspection more urgent; falling/rising tool costs can also change its net value. Therefore:

\[
\boxed{
\text{submodular-like cascade core}
\not\Rightarrow
\text{globally adaptive-submodular DEST runtime}
}
\]

## 8. Engineering interpretation

The current evidence supports a decomposition:

```text
certificate cascade / affected-set coverage
    → strong diminishing-return-like signal

belief transfer
    → occasional complementarity / marginal-value increase

deadline + dynamic cost
    → frequent nonstationary marginal-value increase
```

This means a future proof effort should not target the entire Runtime at once.

A more defensible mathematical program is:

1. isolate a fixed-cost / no-deadline certificate-cascade utility;
2. prove or disprove submodularity there;
3. treat belief updates, deadlines, and dynamic costs as separate extensions;
4. derive approximation guarantees only under explicit conditions.

## 9. External formal alignment

- Golovin & Krause formalize adaptive submodularity as a diminishing-returns property under partial observability and obtain greedy guarantees only when the property holds.
- Parthasarathy studies adaptive submodular maximization under stochastic item costs and stochastic knapsack constraints.
- Stochastic scheduling literature shows that release/due dates and time-dependent feasibility can fundamentally change scheduling objectives.

These are formal comparison points, not proofs about DEST.

## 10. Next falsifiable frontier

v0.8 should stop adding scheduler adjectives and instead isolate the mathematical core:

```text
Fixed-Cost Certificate Cascade Model
```

Then create:

- an exact finite utility function;
- exhaustive small-DAG submodularity checks;
- counterexample search;
- monotonicity check;
- conditions under which cascade utility is provably weighted coverage;
- explicit constructions showing where belief/deadline extensions break those conditions.

That would be the correct bridge from Runtime experiments back into theorem-style mathematics.
