# CRE / Closure / CRL Toy Examples v0.1

## Example 1 — Fixed point but not global closure

Let:

$$
T(0)=0.
$$

Then 0 is a fixed point.

But if another legal operator:

$$
U(0)=1,
$$

exists, the singleton set $\{0\}$ is not closed under the full operator family.

Therefore:

$$
Cl^{fix}\not\Rightarrow Cl^{op}.
$$

## Example 2 — Local closure without coverage

Let global scope:

$$
\Omega=\{1,2,3\}.
$$

Suppose local domains:

$$
U_1=\{1\},
\quad
U_2=\{2\}
$$

are fully solved.

State 3 is uncovered.

Therefore local correctness does not imply global closure.

## Example 3 — Pairwise overlap without global coherence

Three local representations are pairwise translatable but their composed transport around a cycle is not identity.

Then:

$$
Cl^{glue}
$$

fails even if every pair looks locally compatible.

## Example 4 — False Merge

Branch A proves a result under assumption P.

Branch B proves the same textual conclusion under assumption not-P.

If the merge identity contract includes assumptions, the branches are not equivalent.

Merging them only because conclusion strings match is FalseMerge.

## Example 5 — CRL preserve divergence

If two branches have unresolved equivalence status, CRL stores both in the divergence set and may create a new validator query.

It does not average them into a compromise branch.

## Example 6 — Selection is not truth

Two valid open branches have scores:

$$
s(B_1)=0.9,\quad s(B_2)=0.2.
$$

The runtime explores $B_1$ first.

This says nothing about whether $B_1$ is ultimately true and $B_2$ false.

It only allocates finite research resources.

## Example 7 — Reopen

A theory is globally closed under query family:

$$
\mathcal J_1.
$$

Later provenance becomes a first-class criterion:

$$
\mathcal J_2=\mathcal J_1\cup\{j_P\}.
$$

Some historical merges no longer satisfy the identity/information contract.

The correct action is:

$$
Reopen,
$$

not pretending the old closure certificate remains universal.
