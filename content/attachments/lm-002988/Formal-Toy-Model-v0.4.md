# HIPG Formal Toy Model v0.4 — Active Causal Quotient Discovery

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Phase**: Formal Toy Runtime  
**Version**: v0.4  
**Date**: 2026-08-14  
**Status**: Executable finite research scaffold

---

# 0. v0.4 target

v0.3 could actively choose which semantic probe to inspect, but its learner still received a noisy task-class label $Y_T$.

v0.4 removes that rich label in its new active-causal mode. The learner receives only:

$$
oxed{
(v_t,r_t),
\qquad
v_t\in\{0,1\},
\quad
r_t\in\{0,1\}
}
$$

where $v_t$ is the selected probe observation and $r_t$ is binary task reward.

The constructor chooses both a surface probe and an intervention policy:

$$
oxed{
(p^\ast,\pi_a^\ast)
=
\arg\max_{p,\pi_a}
\mathbb E[
\operatorname{InformationGain}
\mid p,\pi_a,H_t
].
}
$$

This is the first HIPG runtime step from **active semantic probing** toward **active causal quotient discovery**.

---

# 1. Bayesian task/partner hypothesis state

The learner maintains a joint posterior over:

1. a finite task hypothesis $h$;
2. a surface-probe permutation $\rho$ supplied by a heterogeneous partner.

$$
\boxed{
P(h,\rho\mid H_t).
}
$$

The canonical task hypothesis family is:

$$
\mathcal H
=
\{H_E,H_J,H_O,H_{J\oplus O}\}.
$$

The partner exposes three opaque surface probes:

$$
\{p_0,p_1,p_2\}
$$

whose mapping to canonical features $(E,J,O)$ is unknown.

To make partner mappings statistically identifiable in this toy model, canonical features use distinct base rates:

$$
P(E=1)=0.2,
\quad
P(J=1)=0.5,
\quad
P(O=1)=0.8.
$$

This is a deliberate finite-model assumption, not a claim about real intelligence.

---

# 2. Action/intervention policies

The intervention policy may be:

```text
CONST0
CONST1
IDENTITY
FLIP
```

where the action is conditioned on the observed probe value $v$.

Reward is stochastic:

$$
P(r=1\mid a=y)=p_{good},
$$

$$
P(r=1\mid a\neq y)=p_{bad}.
$$

The learner never receives $y$ directly.

---

# 3. Expected information gain

For experiment:

$$
e=(p,\pi_a),
$$

and possible observation:

$$
o=(v,r),
$$

the learner computes:

$$
\operatorname{EIG}(e)
=
H[P(h,\rho\mid H_t)]
-
\mathbb E_o
H[P(h,\rho\mid H_t,o,e)].
$$

It then runs the highest-EIG experiment.

No evaluator-provided class label or evaluator-provided "correct probe" is given to the constructor.

---

# 4. Bayesian quotient state

v0.4 no longer stores only a hard partition.

For two canonical states $x,y$, define:

$$
\boxed{
P(x\sim_Ty\mid H_t)
=
\sum_h
P(h\mid H_t)
\mathbf 1[h(x)=h(y)].
}
$$

Thus quotient membership can remain uncertain while evidence accumulates.

A hard quotient is derived only from the MAP task hypothesis for benchmark evaluation.

---

# 5. OOD partner transfer

The `active_causal_ood_partner_permutation` benchmark changes the partner's surface-probe permutation.

The constructor is not given the permutation. It jointly infers:

$$
(h,\rho).
$$

This is a finite OOD surface-ontology test, not yet cross-model generalization.

---

# 6. Counterfactual impossibility diagnostics

v0.4 adds a finite counterfactual relaxation engine.

For an infeasible configuration it evaluates relaxations such as:

- increase channel bits;
- reduce task distinctions;
- enable feedback;
- pre-share mapping;
- increase latency budget;
- strengthen verifier.

It searches for the lowest-cost sparse relaxation set that moves the toy configuration into the feasible region.

The output remains **INFEASIBLE** under current assumptions. A proposed relaxation does not silently mutate the assumptions.

This preserves the Paper 07 invariant:

$$
\boxed{
\text{hard obstruction remains terminal until assumptions change.}
}
$$

---

# 7. Certificate validation and hash lineage

Every result is upgraded to `HIPG-CERT-0.4` and validated against:

```text
certificate_schema_v0.4.json
```

Each certificate includes hash-linked lineage:

$$
\text{input case hash}
\rightarrow
\text{result artifact hash}
\rightarrow
\text{certificate self hash}.
$$

Schema validity and self-hash integrity are independently recorded.

---

# 8. Restricted typed contract DSL

v0.4 adds the first actually machine-checkable formal bridge fragment.

Example:

```text
CONTRACT HIPG_SCOPE_V0_4
ACTION inspect_file
TARGET_PREFIX /workspace/
PERMISSION read_only
MUTATION false
CONFIDENCE_MIN 0.70
END
```

The parser rejects malformed fields, invalid enum values, invalid booleans, and the contradiction:

```text
PERMISSION read_only
MUTATION true
```

A native candidate is checked against the parsed contract. Permission/scope drift is rejected before repair.

This is a deliberately restricted typed DSL, not a proof assistant.

---

# 9. v0.4 new canonical benchmarks

1. `active_causal_binary_reward_identity_partner`
2. `active_causal_ood_partner_permutation`
3. `counterfactual_information_relaxation`
4. `counterfactual_multi_constraint`
5. `typed_contract_permission_scope`

All v0.3 canonical cases remain as regression tests.

---

# 10. What v0.4 still does not prove

v0.4 does not prove B-TSDPC.

It does not establish a universal causal-discovery algorithm.

It assumes:

- a finite known task-hypothesis family;
- a finite known partner-permutation family;
- independent Bernoulli feature priors;
- a known stochastic reward model;
- finite action policies.

Therefore the actual result is narrower:

$$
\boxed{
\text{HIPG can be instantiated as an active Bayesian experiment-selection loop
without task-class labels, while retaining explicit impossibility/unknown branches.}
}
$$
