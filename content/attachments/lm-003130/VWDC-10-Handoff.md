# VWDC-10 Handoff — Byzantine-Resilient World Federation, Trust Domains, and Fault Containment

## Starting state

VWDC-09 defines:

$$
\mathfrak F
=
(
\mathcal R,
X^R,
\mathcal I_G,
Ledger,
CommitAuthority,
TrustState,
Prov
).
$$

It introduces runtime trust states:

```text
ACTIVE
LIMITED
PROBATION
QUARANTINED
REVOKED
```

and proves a limited quorum safety lemma:

with $n=3f+1$, at most $f$ Byzantine validators, honest non-equivocation, two conflicting $2f+1$ commit certificates cannot both exist.

It also separates:

$$
\text{commit quorum}
\neq
\text{evidence independence}.
$$

## Objective

Formalize Byzantine/fault containment across proposal, evidence, certificate, learning, and commit layers.

## Main questions

1. What powers can a Byzantine runtime have under each capability layer?
2. How should malicious evidence differ from malicious commit authority?
3. How should trust be updated without one scalar reputation collapse?
4. When is partial quarantine enough?
5. How should conflicting certificates be handled?
6. What fault threshold is needed for availability under different authority models?
7. What must a runtime prove before reentry?
8. How should shared dependencies limit fault containment?

## Desired form

$$
\boxed{
\text{fault/adversary model}
+
\text{capability graph}
+
\text{quorum/trust assumptions}
+
\text{dependency graph}
\Longrightarrow
\text{containment}
+
\text{quarantine}
+
\text{safe reentry}.
}
$$

## Prohibitions

- Do not equate Byzantine-resistant learning aggregation with Byzantine-safe physical commit.
- Do not equate validator count with independent evidence count.
- Do not grant reentry from model accuracy alone if authority/certificate integrity was compromised.
- Do not assume quarantine blast radius is local without checking dependency closure.
