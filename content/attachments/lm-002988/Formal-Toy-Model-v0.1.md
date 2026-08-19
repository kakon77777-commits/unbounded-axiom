# HIPG Formal Toy Model v0.1

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Phase**: A — Formal Toy Model  
**Version**: v0.1  
**Date**: 2026-08-14  
**Status**: Executable finite toy model / research scaffold

## 0. Purpose

This is the first executable reduction of the eight-paper HIPG series. It does not model general intelligence. It instantiates the pipeline

$$
\boxed{
\mathcal C^\ast
\rightarrow
\widehat{\mathcal Q}_T
\rightarrow
\Pi_t
\rightarrow
\operatorname{Diagnose}
\rightarrow
\{\mathrm{SUCCESS},\mathrm{INFEASIBLE},\mathrm{UNKNOWN}\}.
}
$$

The benchmark deliberately contains both solvable and non-solvable / unresolved cases.

## 1. Finite private worlds

Agent $A$ has a private state space

$$
X_A=\{a_0,\ldots,a_{n-1}\},
$$

while agent $B$ may use a different private representation. A hidden task-semantic quotient is

$$
\mathcal Q_T^\ast=\{q_0,\ldots,q_{m-1}\}.
$$

The sender observes $x\in X_A$ and the receiver must output the correct quotient class $q^\ast(x)$.

## 2. Coupleability gate

Each case supplies the Paper-03 signature

$$
\mathbf K_T=(C,D,F,A,G,\Tau,R).
$$

The toy runtime treats $C=0$, $D=0$, $G=0$, $\Tau=0$, or $R=0$ as structural blockers. Missing feedback does not automatically imply impossibility: when multiple mappings remain observationally equivalent, the status is `UNKNOWN_NONIDENTIFIABLE`.

## 3. Exact information lower bound

If exact one-shot identification of $m$ task classes is required over a binary channel with $b$ bits,

$$
b\ge \lceil\log_2m\rceil.
$$

If the available budget violates this bound, the runtime emits `INFEASIBLE_INFORMATION_BOUND`.

## 4. Protocol state

$$
\Pi_t=
(
E_{A,t},
D_{B,t},
\Sigma_t,
\mathcal H_t
).
$$

The runtime implements a minimal subset of Paper-05 operators:

- `REMAP`: repair a wrong decoder mapping.
- `SPLIT`: allocate or reuse a separate symbol when one symbol conflates task-distinguishable classes.
- `ROLLBACK`: reject a candidate that increases validation error.

## 5. Success criterion

For the finite task set,

$$
\operatorname{Err}_T(\Pi)
=
\frac{\#\text{incorrect states}}{\#\text{states}}.
$$

Success requires

$$
\operatorname{Err}_T(\Pi)\le\delta
$$

within the given bit and adaptation budgets.

## 6. Canonical statuses

The runtime is intentionally forbidden to collapse every failure into “try again”:

- `SUCCESS`
- `INFEASIBLE_STRUCTURAL`
- `INFEASIBLE_INFORMATION_BOUND`
- `UNKNOWN_NONIDENTIFIABLE`
- `UNKNOWN_RESOURCE_LIMIT`

## 7. Four canonical benchmark cases

1. `constructive_repair`: initially wrong / conflated protocol, but feedback, adaptability, and enough capacity exist. Expected `SUCCESS`.
2. `zero_channel`: $C=0$. Expected `INFEASIBLE_STRUCTURAL`.
3. `insufficient_bits`: four exact classes but one bit. Expected `INFEASIBLE_INFORMATION_BOUND`.
4. `no_feedback_ambiguous_mapping`: enough capacity, but the unknown receiver permutation cannot be identified from the available history. Expected `UNKNOWN_NONIDENTIFIABLE`.

## 8. What v0.1 does not yet model

Deferred to v0.2+:

- learned quotient cardinality / partition;
- `MERGE`, `ALIAS`, `COMPOSE`;
- approximate TSSH;
- noisy channels and empirical Fano tests;
- $L_A\leftrightarrow L_F\leftrightarrow L_E\leftrightarrow L_H$ runtime;
- provenance DAG;
- adversarial agents;
- nonstationary tasks;
- multi-agent populations;
- FLP-like timing cases;
- executable undecidability fragments.

## 9. Minimal claim

The only substantive engineering claim of this package is:

$$
\boxed{
\text{The HIPG vocabulary can be instantiated as an executable finite state machine
without collapsing SUCCESS, INFEASIBLE, and UNKNOWN.}
}
$$

This package does **not** prove B-TSDPC.
