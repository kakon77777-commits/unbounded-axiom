# HIPG Formal Toy Model v0.9
## Intervention-Language Learning, Grounding Number, Active POMDP Discovery, Proof Objects, and Public Equivalence Classes

**Framework**: HIPG — Heterogeneous Intelligence Protocol Generation  
**Version**: v0.9  
**Date**: 2026-08-14  
**Status**: Executable finite research scaffold

---

# 0. v0.9 frontier

v0.8 made the semantic model itself an equivalence-class object:

$$
[(\rho,h,\iota)]_{\equiv}.
$$

But its intervention semantics still lived in a very small permutation family over three known latent toggles.

v0.9 attacks the next layer:

$$
\boxed{
\text{known intervention labels}
\rightarrow
\text{learned finite intervention language}
}
$$

and asks a second question that becomes unavoidable once semantic gauge classes are explicit:

$$
\boxed{
G^*=\min\{|A|:A\text{ is sufficient to break a finite semantic gauge class}\}.
}
$$

The version also adds:

- active finite POMDP discovery of $P,O,R$ without hidden-state resets;
- operator-family growth across arity/domain/time structure;
- replayable proof objects for finite temporal claims;
- a hashed theorem-anchor registry;
- online drift detection before operator retirement;
- equivalence classes as stable public HIPG artifacts.

---

# 1. Finite intervention language

An intervention is no longer restricted to a permutation of three named toggles.

The bounded v0.9 language contains behavioral kernels of the form:

$$
\iota_a:X\to\mathcal P(X)
$$

with examples from four classes:

1. **multi-variable deterministic**
   $$
   \operatorname{TOGGLE}_{EJ};
   $$
2. **non-invertible**
   $$
   \operatorname{SET}_{O\leftarrow1};
   $$
3. **stochastic**
   $$
   \operatorname{STOCH\_TOGGLE}_{E,0.75};
   $$
4. **composite**
   $$
   \operatorname{TOGGLE}_J;\operatorname{SET}_{O\leftarrow0}.
   $$

After behavioral deduplication, the canonical finite library has:

$$
\boxed{32}
$$

unique transition kernels.

For every raw action $a$, the learner receives state-transition samples and maximizes finite-model likelihood.  It is evaluated on **kernel identity**, not syntactic operator name.

Canonical result: all four hidden intervention kernels are recovered exactly, including the stochastic kernel.

This supports only the bounded claim:

$$
\boxed{
\text{a finite heterogeneous intervention language can be learned up to behavioral equivalence}.
}
$$

It does **not** establish unrestricted intervention-language induction.

---

# 2. Minimal grounding number

For the finite semantic gauge class

$$
\Gamma=S_3
$$

of six permutations assigning three raw actions to $\{E,J,O\}$, define an anchor as a statement:

$$
(a_i\mapsto s_j).
$$

The v0.9 finite grounding number is:

$$
\boxed{G^*=2}.
$$

Every single correct anchor leaves two permutations alive, while any two distinct correct anchors determine the third by bijectivity.

Thus all three two-anchor subsets are minimal grounding sets.

Important boundary: this is a theorem about the six-element permutation gauge class, **not** a theorem about the full HIPG semantic model class.

---

# 3. Active POMDP discovery

v0.9 introduces a two-state, two-action finite POMDP candidate family.

Unknown model components are:

$$
(P,O,R).
$$

The learner is not given:

- hidden-state resets;
- the transition model $P$;
- the observation model $O$;
- the reward model $R$.

Instead it maintains:

$$
P(M\mid H_t)
$$

and a latent-state belief for each candidate model.

The active policy selects the next action by expected posterior model-entropy reduction.

For the canonical fixed budget of 18 experiments over 30 seeded runs:

$$
\boxed{
\operatorname{Acc}_{\mathrm{active}}=0.80
>
\operatorname{Acc}_{\mathrm{random}}=0.6333\ldots
}
$$

for identifying the correct **predictive equivalence signature**.

Both policies use the full budget in this benchmark. Therefore the supported statement is an identification-quality improvement under a fixed budget, **not** a sample-complexity theorem.

---

# 4. Operator arity and domain growth

The constructor now compares qualitatively different operator families instead of only binary Boolean truth tables.

## 4.1 Boolean majority

For the three-input majority target:

$$
\operatorname{MAJ}_3(x_1,x_2,x_3),
$$

best unary accuracy is:

$$
0.75,
$$

best binary-on-a-pair accuracy is:

$$
0.75,
$$

while the exact ternary truth table:

$$
\boxed{00010111}
$$

reaches:

$$
1.0.
$$

## 4.2 Multi-valued domain

On $\mathbb Z_3$ inputs, the correct family is identified as:

$$
\boxed{a+b\pmod 3}.
$$

## 4.3 Sequential operator

On bit pairs $(x_{t-1},x_t)$, the selected operator is:

$$
\boxed{\mathbf 1[x_{t-1}\ne x_t]}.
$$

The point is not that these three operators are difficult. The point is that v0.9 begins charging search across **arity, value domain, and temporal structure** as separate representational choices.

---

# 5. Proof-producing finite temporal checker

v0.8 returned graph paths.

v0.9 packages them as explicit proof objects under:

```text
HIPG-TEMP-PROOF-0.9
```

Three proof types are supported:

1. `SAFETY_COUNTEREXAMPLE`;
2. `REACHABILITY_WITNESS`;
3. `INDUCTIVE_INVARIANT`.

Canonical artifacts:

$$
[s_0,s_1,bad]
$$

is independently replayed as a safety counterexample;

$$
[s_0,s_1,goal]
$$

is independently replayed as a reachability witness;

and:

$$
\{s_0,s_1,goal\}
$$

is checked as a closed bad-free inductive invariant of the repaired graph.

This remains a finite explicit-state checker, not a general temporal theorem prover.

---

# 6. Theorem-anchor registry

Diagnostic certificates may cite theorem/lower-bound anchors only through a registry entry containing:

```text
anchor_id
assumptions
formal_statement
checker
scope
version
anchor_hash
```

The canonical registry includes:

- exact quotient bit lower bound;
- lost-distinction non-recovery;
- coarse Fano lower bound.

v0.9 correctly:

- accepts a valid content-hashed citation;
- rejects a stale/wrong hash;
- rejects a nonexistent anchor;
- rejects an assumption mismatch.

The registry therefore turns a theorem-anchor string into a content-bound object.

---

# 7. Online drift detection

v0.8 retirement used a known distribution-shift point in the toy cost stream.

v0.9 removes that privilege.

The runtime compares:

- no retirement;
- fixed patience;
- a Bayesian online change detector;
- a regret-trigger detector.

Canonical hidden shift:

$$
t^*=20.
$$

The Bayesian detector retires at index:

$$
\boxed{21}
$$

with posterior change probability:

$$
0.9009289\ldots
$$

and total toy cost:

$$
\boxed{238}
$$

versus:

$$
267
$$

for no retirement.

The shift index is used only for evaluation, not supplied to the detector.

---

# 8. Equivalence class as a public artifact

v0.9 exports a stable object:

```json
{
  "schema_version": "HIPG-EQUIV-0.9",
  "equivalence_class_id": "sha256:...",
  "members": [],
  "admissible_interventions": [],
  "maximum_remaining_split_bits": 0.0,
  "grounding_needed": {
    "minimum_anchor_count": 2
  },
  "selection_policy": "DO_NOT_CHOOSE_REPRESENTATIVE_AS_TRUTH",
  "artifact_hash": "..."
}
```

This makes:

$$
\boxed{[(\rho,h,\iota)]_{\equiv}}
$$

conceptually parallel to HIPG success, gap, and impossibility certificates: it can itself be stored, hashed, transferred, and audited.

The key invariant is explicit:

$$
\boxed{
\text{permanent equivalence class}
\not\Rightarrow
\text{pick a convenient representative as truth}.
}
$$

---

# 9. v0.9 certificate layer

Every canonical result is upgraded to:

```text
HIPG-CERT-0.9
```

and checked for:

1. JSON Schema validity;
2. SHA-256 self/lineage integrity;
3. semantic consistency;
4. v0.9-specific feature invariants.

Canonical regression:

$$
\boxed{58/58}
$$

certificates pass schema + hash + semantic validation.

---

# 10. What v0.9 establishes

The strongest justified finite claims are:

1. a bounded intervention grammar containing multi-variable, non-invertible, stochastic, and composite operators can be identified from finite transition samples up to behavioral equivalence;
2. the six-element $S_3$ intervention-semantic gauge class has grounding number $G^*=2$;
3. in one finite POMDP family, active action selection improves predictive-model identification accuracy over random action selection under a fixed experiment budget;
4. operator search can require growth in arity/domain/temporal structure when smaller families are insufficient;
5. finite temporal claims can carry independently replayable proof objects;
6. theorem-anchor references can be content-hashed and assumption-checked;
7. drift-triggered retirement can be inferred online rather than using the true shift time;
8. an unresolved equivalence class can be exported without selecting a representative as semantic truth.

---

# 11. What v0.9 does not establish

v0.9 does **not** prove:

- B-TSDPC;
- a universal intervention language;
- that $G^*=2$ outside the finite permutation gauge benchmark;
- general POMDP identifiability;
- active POMDP sample-complexity superiority;
- unrestricted operator invention;
- general temporal logic verification;
- general theorem-anchor soundness beyond registered checkers;
- optimal online drift detection.

The entire runtime remains a finite falsifiable scaffold.
