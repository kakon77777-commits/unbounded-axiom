# HIPG Formal Toy v0.8 — v0.9 Handoff

## Verified v0.8 additions

- finite behavioral operator invention independent of AST shape;
- joint reward+dynamics task-value discovery;
- unlabeled HMM observation model recovery up to latent permutation;
- explicit $[(\rho,h,\iota)]_{\equiv}$ runtime object;
- raw-action active splitting with terminal permanent equivalence class;
- external grounding as an identifiability resource;
- diagnostic bundle with theorem anchors + learned likelihood + OOD support + abstention;
- explicit finite-state temporal checker with witnesses/counterexamples;
- task-drift operator retirement.

---

# v0.9 Priority A — learn the intervention language itself

v0.8 still assumes exactly three raw actions and a permutation relation to three latent toggles.

Next, permit:

- interventions that affect multiple latent variables;
- non-invertible interventions;
- interventions with stochastic effects;
- newly proposed composite interventions.

The model class should contain intervention operators:

$$
\iota_a:X\to\mathcal P(X)
$$

rather than only permutations.

---

# Priority B — quantify the grounding requirement

v0.8 shows:

$$
72\to6
$$

without grounding and:

$$
12\to1
$$

with two anchors.

v0.9 should ask:

$$
\boxed{
G^\ast
=
\min\{|A|:\text{anchors }A\text{ break the semantic gauge class}\}.
}
$$

Compute minimal grounding sets over finite model classes.

---

# Priority C — active POMDP discovery

The HMM benchmark uses a finite candidate grid.

Next jointly learn:

$$
\widehat P,
\widehat O,
\widehat R
$$

from action-observation-reward trajectories without hidden-state resets.

Maintain belief over latent models and latent states.

---

# Priority D — behavioral operator arity / domain growth

v0.8 searches all 16 binary Boolean truth tables.

Next allow the system to compare:

- unary;
- binary;
- ternary;
- finite multi-valued operators;
- sequential operators.

Charge search complexity explicitly.

---

# Priority E — proof-producing temporal checker

The v0.8 checker emits explicit graph paths, but not a machine-independent proof object.

Create a small proof schema for:

- reachability witness;
- safety counterexample;
- inductive invariant on finite graphs.

Keep the artifact independently replayable.

---

# Priority F — theorem-anchor registry

Diagnostic anchors are currently string IDs.

Create a registry:

```text
anchor_id
assumptions
formal statement
checker
scope
version/hash
```

so certificates cannot cite nonexistent or mismatched bounds.

---

# Priority G — drift detection before retirement

v0.8 uses a known shift point in the cost model.

v0.9 should infer drift online and compare:

- no retirement;
- fixed patience;
- Bayesian change-point;
- regret-triggered retirement.

---

# Priority H — equivalence classes as public artifacts

Export surviving model classes in a stable schema:

```json
{
  "equivalence_class_id": "...",
  "members": [],
  "admissible_interventions": [],
  "maximum_remaining_split_bits": 0.0,
  "grounding_needed": "unknown"
}
```

This should become a first-class HIPG artifact alongside success, gap, and impossibility certificates.

---

# Non-negotiable constraint

Do not choose a representative from a permanent semantic equivalence class and report it as truth merely for convenience.
