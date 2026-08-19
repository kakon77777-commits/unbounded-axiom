# SSDC Toy Examples v0.1

## Example 1 — Shared protocol, no active coupling

A and B both serialize a state to the same JSON schema.

- Share: high
- Transport: valid
- Fidelity: high
- Active coupling: zero because B stores but never consumes A's state
- Synchronization: absent

This demonstrates:

$$
Share
+
Transport
\not\Rightarrow
Couple.
$$

## Example 2 — Strong one-way sensor coupling

Sensor A exposes a small measurement state to controller B.

- $\rho_{A\to B}^{share}\approx1$
- $\rho_{B\to A}^{share}\ll1$
- $\kappa_{A\to B}>0$
- $\kappa_{B\to A}=0$

This demonstrates directional SSDC.

## Example 3 — Common forcing without pairwise coupling

A and B are both driven by an external clock/source U.

Their chosen observables synchronize, but neither update law reads the other.

Therefore:

$$
Sync(A,B)
\not\Rightarrow
\kappa_{A\to B}>0.
$$

## Example 4 — Pairwise overlap without global overlap

$$
Z_1=\{a,b\},
\quad
Z_2=\{b,c\},
\quad
Z_3=\{a,c\}.
$$

All pairwise intersections are nonempty, but:

$$
Z_1\cap Z_2\cap Z_3=\varnothing.
$$

Pairwise SSDC therefore cannot certify global shared state.

## Example 5 — Legacy Co

A formalization runtime binds:

- intent version;
- axiom/specification version;
- execution environment;
- data version;

to one snapshot identifier.

This is modeled as:

$$
Co_{\mathrm{legacy}}
\mapsto
SSDC^{\mathrm{version-sync}}.
$$

It is not a full SSDC implementation until shared-state coverage, transport fidelity, and active coupling are separately represented.
