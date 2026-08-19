# DEST v0.9 — Breakdown Lattice Exact Report

**Date:** 2026-08-14  
**Parent theorem model:** DEST v0.8 Fixed-Cost Certificate Cascade Model  
**Formal object:** typed regime DAG + property map  
**Property states:** `TRUE / FALSE / CONDITIONAL / NOT_APPLICABLE`

## 1. Canonical property transition table

| Regime | Static set function | Monotone | Submodular | General adaptive-submodular | Order/time invariant | Static feasible family |
|---|---|---|---|---|---|---|
| Pure cascade coverage | TRUE | TRUE | TRUE | N/A | TRUE | TRUE |
| Mixed release, blocker <= 1 | TRUE | FALSE | TRUE | N/A | TRUE | TRUE |
| Mixed release, >= 2 blockers | TRUE | FALSE | FALSE | N/A | TRUE | TRUE |
| Independent modular belief | Conditional | TRUE | TRUE | TRUE | TRUE | TRUE |
| Correlated belief update | Conditional | Conditional | Conditional | FALSE | Conditional | TRUE |
| Deadline value | FALSE | N/A | N/A | N/A | FALSE | Conditional |
| Dynamic cost only | TRUE | Conditional | Conditional | Conditional | Conditional | FALSE |
| Full Runtime | FALSE | N/A | N/A | FALSE | FALSE | FALSE |

The table deliberately distinguishes `FALSE` from `NOT_APPLICABLE`. A deadline/order-dependent objective may cease to be a static set function; that is a type change, not merely another counterexample to a static set-function property.

## 2. Deterministic release boundary

### Monotonicity — minimum witness: 2 nodes

```json
{
  "holds": true,
  "witness": {
    "S": [
      1
    ],
    "e": 0,
    "F_S": 1.0,
    "F_Se": 0.1
  }
}
```

### Static submodularity — minimum witness: 3 nodes

```json
{
  "holds": true,
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
  }
}
```

## 3. Correlated belief update

The exact two-item rational-prior census enumerates all joint binary distributions with denominator D <= 8.

- total joint distributions: **494**
- distributions where P(A=1)>0: **450**
- adaptive diminishing-return violations: **170**
- minimum denominator with a violation: **2**

First witness:

```json
{
  "denominator": 2,
  "counts": {
    "00": 1,
    "01": 0,
    "10": 0,
    "11": 1
  },
  "delta_B_empty": 0.5,
  "delta_B_given_A1": 1.0
}
```

The canonical witness is P(00)=P(11)=1/2. For pointwise modular reward, the expected marginal of B rises from 1/2 before observation to 1 after observing A=1. Correlation alone therefore suffices to break general adaptive submodularity.

## 4. Independent modular special case

The independent-product grid performs **722** conditional marginal comparisons.
Violations: **0**.

The analytic result is stronger: under independence, observing other items does not change the conditional probability of an unobserved modular item, so its expected marginal is constant.

## 5. Deadline / order breakdown

- two-job deadline models checked: **4**
- order-sensitive models: **2**

First witness:

```json
{
  "deadline_A": 1,
  "deadline_B": 2,
  "AB": 2,
  "BA": 1
}
```

A single action plus two clock states already proves time dependence:

```json
{
  "selected_set": [
    "e"
  ],
  "value_at_t0": 1.0,
  "value_at_t1": 0.0,
  "static_set_function_possible": false
}
```

The correct classification is `static set utility -> time/sequence utility`.

## 6. Dynamic cost breakdown

Minimum witness:

```json
{
  "budget": 1,
  "item": "e",
  "cost_t0": 2,
  "cost_t1": 1,
  "feasible_t0": false,
  "feasible_t1": true,
  "static_feasible_family": false
}
```

One item is infeasible at t0 and feasible at t1 under the same budget. The underlying utility may remain submodular; what breaks is the static feasible family.

## 7. Minimum breakdown sizes

| Property/object lost | Minimum witness |
|---|---:|
| Monotonicity | 2 deterministic nodes |
| Static submodularity guarantee | 3 deterministic nodes |
| General adaptive submodularity | 2 stochastic items |
| Static time-invariant set value | 1 action + 2 clock states |
| Order invariance | 2 actions |
| Static feasible family | 1 action + dynamic cost |

## 8. Four different kinds of breakdown

1. **Property loss** — e.g. monotone -> non-monotone.
2. **Guarantee loss** — e.g. one blocker -> two blockers.
3. **Mathematical object-type change** — e.g. set utility -> sequence/time utility.
4. **Constraint-type change** — e.g. fixed knapsack -> dynamic feasibility.

## 9. Status

v0.9 establishes a typed breakdown map, not a theorem that the named regimes form a strict mathematical lattice. `Breakdown Lattice` remains the project name pending a future meet/join closure result.