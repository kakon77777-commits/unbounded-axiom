# TICDR Toy Examples v0.1

## Example 1 — Label-preserving compression

Source:

$$
x=(\text{image pixels},\text{class label}).
$$

Transformation returns only the class label.

For:

$$
\mathcal J=\{\text{class}\},
$$

the representation is $\mathcal J$-complete.

For:

$$
\mathcal J'=\{\text{class},\text{RGB pixels}\},
$$

it is not complete.

Therefore:

$$
\text{task completeness}\neq\text{source invertibility}.
$$

## Example 2 — Same content, different provenance

Two theorem statements have identical text but different source states:

- source A: formally verified theorem;
- source B: unverified generated claim.

A transformation that stores only the statement text merges them.

State-content query can be preserved while provenance query is lost.

## Example 3 — Current state, different history

Two systems reach the same current state $s_t$ through different histories.

A snapshot-only transformation can preserve current-state queries and destroy history queries.

## Example 4 — Side-information recovery

A compressed file cannot be decoded without a key.

From compressed bytes alone, target content is unavailable.

From:

$$
(\text{compressed bytes},\text{key})
$$

it is recoverable.

The key is side information and must be declared in the restoration contract.

## Example 5 — Fiber collision

Let:

$$
T(0)=T(1)=a.
$$

For:

$$
j(x)=x,
$$

$j$ is not constant on the fiber $\{0,1\}$, so it cannot factor through $T$.

For:

$$
k(x)=0,
$$

$k$ is constant on every fiber and is preserved.

## Example 6 — Post-processing cannot recover a lost distinction

Let:

$$
T(0)=T(1)=a
$$

and any:

$$
U(a)=z.
$$

No decoder from $z$ can distinguish whether source was 0 or 1.

Pure post-processing cannot restore distinctions already merged by $T$.
