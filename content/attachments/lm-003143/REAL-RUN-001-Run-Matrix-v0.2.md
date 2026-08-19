# REAL RUN 001 — Run Matrix v0.2

## Design correction: isolate architecture from heterogeneity

A direct comparison between a heterogeneous four-model observer network and a single model would confound:

$$
\text{role separation}
+
\text{agent count}
+
\text{model diversity}.
$$

Therefore REAL RUN 001 is split into two phases.

## Phase A — clean causal 2×2, blocked by model family

For each model family $M_i$, run four conditions from clean sessions:

$$
\boxed{
\{ON\_M+,ON\_M-,SA\_M+,SA\_M-\}
}
$$

`ON` here means **four isolated Agent instances of the same model family** occupying `Proposer`, `Verifier`, `CoverageAuditor`, and `BoundaryAuditor`. They must have separated scratchpads / contexts.

`SA` means one instance of that same model family performs proposal + self-verification while the deterministic commit controller remains external.

With four model families this gives:

$$
4\text{ models}\times4\text{ cells}=16\text{ episodes}.
$$

This estimates memory and role-separation effects while blocking on model family.

### Critical reset rule

$M^+$ means failure memory is preserved **inside the episode after rollback**. It does not mean memory carries across experimental episodes. Every episode starts from a clean model/session state except for the frozen initial benchmark materials.

## Phase B — heterogeneous observer-network extension

Only after Phase A passes protocol validation, run four-model heterogeneous Observer Networks using Latin-style role rotation under both $M^+$ and $M^-$:

$$
2\text{ memory conditions}\times4\text{ rotations}=8\text{ episodes}.
$$

Phase B tests:
- cross-model epistemic convergence;
- role portability;
- model-role interaction;
- institutional persistence under member substitution.

It is **not** used as the clean ON-vs-SA architecture estimate.

## Total first full batch

If both phases are completed:

$$
16+8=24\text{ episodes}.
$$

Phase A has priority. Phase B may be deferred if cost is high.

## Suggested analysis

Phase A lower-is-better endpoint model:

$$
Y
=
\mu
+
\alpha_{memory}
+
\beta_{architecture}
+
\gamma_{model}
+
(\alpha\beta)
+
\epsilon.
$$

Phase B:

$$
Y
=
\mu
+
\alpha_{memory}
+
\beta_{role}
+
\gamma_{model}
+
\text{rotation block}
+
\epsilon.
$$

No inferential p-value is planned for a single episode per cell. The first batch is effect-size / trace validation; replication across benchmark seeds comes next.
