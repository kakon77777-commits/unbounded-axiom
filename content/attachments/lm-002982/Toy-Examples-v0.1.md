# TIBRF Toy Examples v0.1

## Example 1 — Macro-identical, micro-distinct

Let:

$$
x=(0,1),
\qquad
y=(1,0).
$$

Query:

$$
j(x_1,x_2)=x_1+x_2.
$$

Then:

$$
j(x)=j(y)=1,
$$

so:

$$
x\equiv_{\{j\}}y.
$$

But:

$$
x\neq y.
$$

The query family is not point-separating.

## Example 2 — Add one separating query

Add:

$$
k(x_1,x_2)=x_1.
$$

Now:

$$
k(x)=0,
\qquad
k(y)=1.
$$

Therefore:

$$
x\not\equiv_{\{j,k\}}y.
$$

Identity resolution becomes finer when the query family grows.

## Example 3 — Approximate identity is non-transitive

Let:

$$
x=0,\quad y=0.75,\quad z=1.5,\quad \epsilon=1.
$$

Then:

$$
x\approx_\epsilon y,
\qquad
y\approx_\epsilon z,
$$

but:

$$
x\not\approx_\epsilon z.
$$

Do not form a quotient without additional closure/partition rules.

## Example 4 — Boundary mismatch

A cloud service runs on hardware in one data center.

- physical/hardware boundary: one facility;
- causal boundary: remote clients and dependent services;
- permission boundary: tenant-specific access domain;
- computational boundary: a distributed cluster.

These boundaries need not coincide.

## Example 5 — Subject/object role reversal

Agent A observes Agent B.

For relation r1:

$$
Role(A;r_1)=Subj,\quad Role(B;r_1)=Obj.
$$

Later B evaluates A.

For relation r2:

$$
Role(B;r_2)=Subj,\quad Role(A;r_2)=Obj.
$$

Role is relational, not permanent.

## Example 6 — High coupling, distinct entities

Two oscillators synchronize perfectly on a selected observable.

They still have different tokens, histories and physical carriers.

Therefore:

$$
Sync\not\Rightarrow Identity.
$$
