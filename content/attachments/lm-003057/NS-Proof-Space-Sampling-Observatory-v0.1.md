# NS Proof-Space Sampling Observatory v0.1

**Date:** 2026-08-17  
**Status:** corpus analysis / hypothesis-testing instrumentation; not a Navier--Stokes proof.  
**Canonical source:** UTF-8 Markdown.  
**Canonical math delimiters:** `$...$` and `$$...$$` only.

## 1. Executive result

This corpus already contains enough material to test the hypothesis that long-running AI mathematical research changes phase from first-order route discovery into higher-order resampling of previously discovered proof-space structures.

The recursive archive scan found:

- 1109 file instances across the outer ZIP and nested ZIPs;
- 593 Markdown instances;
- 565 exact-hash-unique Markdown artifacts;
- 203 NS paper-like artifacts after excluding README / CHANGELOG / SOURCE_POLICY / checkpoints / roadmaps / handoffs / audits;
- 27 paper-like artifacts in the `空間域證明包圍` branch.

Thus the user's informal statement "about 200 NS papers" is borne out by a conservative classifier: the core NS paper-like count is **203**.

The central observational hypothesis is:

$$
\text{route discovery}
\longrightarrow
\text{route revisit}
\longrightarrow
\text{relations among routes}
\longrightarrow
\text{family / all-order sampling}.
$$

The present v0.1 instrument calls these tiers $T_1,T_2,T_3,T_X$.

## 2. Why this is not merely textual repetition

The corpus contains explicit higher-order vocabulary inside substantive NS papers:

| Marker | NS papers containing marker | Total occurrences |
|---|---:|---:|
| second-order | 7 | 38 |
| third-order | 1 | 1 |
| higher-order | 18 | 35 |
| all-order | 9 | 62 |
| confluence | 9 | 49 |
| recurrence | 88 | 876 |
| no-go | 133 | 452 |

Examples detected by the registry include:

- P144 — NS-DCRP-33 — Circulation Replenishment, Backward Filamentation, and Navier–Stokes Kelvin Shadowing: explicit second-order viscous circulation residue / higher-order continuation language;
- P044 — Navier–Stokes C5-H: an explicit all-order escalation artifact;
- P169 — NS × X 積分 × 24/72 範式實戰: obstruction-confluence phase;
- P170 — NS × X 積分 × 24/72 範式實戰: coupled-confluence phase;
- P048 — Navier–Stokes C5-M: unified defect-graph compression.

These are qualitatively different from mere repeated wording, but the marker table is only an **evidence registry**. Some expressions such as `second-order` or `third-order` can denote ordinary derivative, Fourier, or correction order rather than proof-space order. Consequently, full-body marker counts are **not** directly converted into sampling tiers. Sampling-tier inference trusts order language only when it appears in the route/title surface, together with graph recurrence/confluence evidence.

## 3. Operational definitions

For each paper artifact $p_i$, define a reconstructed research state

$$
p_i=(S_i,R_i,C_i),
$$

where $S_i$ is the symbolic/title representation, $R_i$ is its route/dependency neighborhood, and $C_i$ is its controlled concept-family signature.

The primary v0.1 novelty diagnostic is fixed-window route-semantic novelty:

$$
\nu_i^{(W)}
=
1-\max_{i-W\le j<i}\operatorname{cos}(S_i,S_j),
\qquad W=20.
$$

A cumulative nearest-neighbor score is also retained, but it is explicitly treated as size-biased because the comparison pool grows with $i$. A controlled concept-family novelty ratio is retained only as a diagnostic and is **not** used as primary evidence for saturation, because any finite dictionary mechanically saturates.

The ordering $i$ is a **reconstructed proof-route order**, not an asserted exact wall-clock chronology. It is based on series progression plus internal numbering.

A revisit edge is created when title/route cosine similarity is at least 0.36. Explicit internal dependency references and consecutive-series links are separately preserved.

For a paper $p_i$, the v0.1 confluence degree is

$$
\kappa_i
=
\#\{\text{distinct prior NS series feeding recurrence/dependency edges into }p_i\}.
$$

The estimated sampling tier is intentionally heuristic:

$$
T_1:\ \text{state / route sampling},
$$

$$
T_2:\ \text{revisit / transition sampling},
$$

$$
T_3:\ \text{relations / confluence among prior routes},
$$

$$
T_X:\ \text{explicit higher/all-order or family-level saturation evidence}.
$$

It is **not** claimed that $T_X$ is a formally proven mathematical order.

## 4. Novelty robustness check: no global exhaustion claim yet

The cumulative nearest-neighbor novelty falls from an early-quarter mean of

$$
\bar\nu_{\mathrm{cum,Q1}}=0.7095
$$

to a final-quarter mean of

$$
\bar\nu_{\mathrm{cum,Q4}}=0.5429.
$$

However, that statistic is biased downward by the growing number of prior comparison points. The fixed-window test is therefore the stronger diagnostic. With $W=20$, the Q2 and Q4 means are

$$
\bar\nu_{\mathrm{W20,Q2}}=0.5425,
\qquad
\bar\nu_{\mathrm{W20,Q4}}=0.5781.
$$

Their difference is

$$
\Delta\bar\nu_{\mathrm{W20}}=0.0356.
$$

Against 500 random reorderings, the null mean difference is -0.0009 with standard deviation 0.0363, giving $z=1.01$. The observed change is therefore **not unusually negative**. In this v0.1 corpus analysis, a global whole-corpus novelty collapse is **not established**.

This is an important correction: the strongest evidence is presently **localized higher-order resampling and confluence inside specific routes**, not proof-space exhaustion of the corpus as a whole.

The within-series diagnostic likewise changes from Q2 mean 0.5546 to Q4 mean 0.6182; it also does not support a simple monotone global saturation story.

See `novelty_diagnostics.png` and `novelty_robustness.json`.

## 5. Estimated sampling-tier distribution

| Tier | Papers |
|---|---:|
| $T_1$ | 84 |
| $T_2$ | 107 |
| $T_3$ | 10 |
| $T_X$ | 2 |

The key signal is not a monotone global rise. Instead, `sampling_tier_timeline.png` exposes localized clusters where a branch shifts from ordinary route work into revisit, confluence, or explicit higher/all-order analysis. This matches the qualitative claim more closely than a simple corpus-wide saturation curve.

## 6. Cross-series concept confluence

The following controlled concept families are the strongest cross-series convergence zones in v0.1:

| Concept family | Paper mentions | Distinct NS series | Max estimated tier |
|---|---:|---:|---:|
| carrier-supplier | 57 | 9 | 4 |
| rigidity-closure | 48 | 9 | 4 |
| obstruction-gap-defect | 47 | 9 | 3 |
| flux-transfer-work | 24 | 6 | 3 |
| criticality | 23 | 6 | 4 |
| spectral-frequency | 21 | 6 | 3 |
| dissipation-viscous | 17 | 6 | 2 |
| cancellation-sign | 13 | 6 | 3 |
| packing-congestion | 12 | 6 | 2 |
| recurrence-return | 19 | 5 | 3 |
| geometry-alignment | 18 | 5 | 2 |
| phase-coherence | 15 | 5 | 2 |

This table is deliberately family-level. A broad term such as `criticality` does not by itself prove mathematical equivalence. It is a routing signal that tells the next audit where to test whether superficially different branches are genuinely quotient-equivalent or merely lexically related.

## 7. Cross-series proof-route traffic

The strongest cross-series recurrence/dependency directions detected by v0.1 are:

| Earlier / source series | Later / target series | Edge count |
|---|---|---:|
| NS_MORP | NS-DCRP | 21 |
| NS-FCBP | NS-DCRP | 11 |
| NS_O | NS_X72 | 7 |
| NS_O | NS-DCRP | 5 |
| NS-CSP | NS_DRC | 5 |
| NS_DRC | NS_ANP | 4 |
| NS-FCBP | NS_Proof_Asset_Map | 4 |
| NS_X72 | NS_Proof_Asset_Map | 4 |
| NS-DCRP | NS_Proof_Asset_Map | 3 |
| NS_TSKR | NS_Proof_Asset_Map | 3 |
| NS-DCRP | NS-IDRP | 2 |
| NS_DRC | NS_CFOP | 2 |

These edges are visible in `series_confluence_network.png` and the interactive document graph.

## 8. Relation to SDPE / space-domain proof enclosure

The corpus supports a concrete bridge to SDPE.

Let $\Omega_0$ denote the initial candidate proof space and let each audited no-go / rigidity / incompatibility result induce a cut $H_t$. Then

$$
\Omega_{t+1}=\Omega_t\cap H_t.
$$

Large-scale generation is useful not merely because it produces candidate proofs. It also produces **negative proof information** and recurrent quotient structure. If independent routes repeatedly land in the same obstruction family, the research process begins to estimate not only points of $\Omega_t$ but the topology/geometry of the surviving region itself.

The hypothesis to test in later versions is therefore stronger than simple saturation:

$$
\boxed{
\text{AI long-run proof search can induce an empirical filtration of proof space.}
}
$$

A corresponding multi-order integration picture is

$$
I_k(N)=\int_{\Omega^{(k)}}c_{N,k}(\xi)\,d\mu_k(\xi),
$$

where $\Omega^{(0)}$ is a state/representation space, $\Omega^{(1)}$ a route/transition space, and higher $\Omega^{(k)}$ encode relations among lower-order proof structures.

The observable saturation signal is not $I_k=1$, which would be unjustified, but

$$
\Delta I_k(N)\to 0
$$

under a fixed representation, method family, verifier, and resource budget.

## 9. What this dataset can and cannot establish

### It can currently support

1. exact corpus-size accounting;
2. explicit higher-order vocabulary detection;
3. route recurrence and cross-series confluence candidates;
4. novelty-decay measurement under a declared quotient heuristic;
5. a reproducible graph for targeted manual/formal audit.

### It cannot yet establish

1. exhaustion of the mathematical proof space;
2. semantic equivalence of every clustered obstruction;
3. independence/unprovability of Navier--Stokes regularity;
4. correctness of every generated mathematical claim;
5. that an estimated $T_X$ artifact is literally an $X$-th order object in a formal higher-category or proof-theoretic sense.

## 10. Next hardening step

The next version should replace coarse title-family quotienting with a theorem-level graph:

$$
\text{claim}
\to
\text{assumptions}
\to
\text{lemmas}
\to
\text{obstruction}
\to
\text{status}.
$$

Each obstruction should receive a canonical ID. Two routes should be merged only if their normalized hypotheses and terminal obstruction are formally or manually audited as equivalent.

That would allow a much stronger quantity:

$$
\rho_k(N)
=
\frac{\#\text{new audited equivalence classes at order }k}
{\#\text{new generated artifacts at order }k},
$$

and an empirical saturation criterion such as

$$
\rho_k(N)<\varepsilon
$$

for a sustained window, together with a representation-change trigger when several $k$ simultaneously saturate.

---

## Files

- `ns_papers_metrics.csv`: 203 NS paper-like nodes and all metrics.
- `ns_proof_route_edges.csv`: sequence, explicit-dependency, and revisit-similarity edges.
- `concept_families.csv`: first appearance, revisits, and cross-series confluence.
- `higher_order_evidence.csv`: exact artifact/snippet registry for order/confluence/recurrence/no-go markers.
- `series_summary.csv`: series-level sampling and novelty statistics.
- `series_confluence_edges.csv`: cross-series edge aggregation.
- `ns_proof_route_graph.graphml`: graph for Gephi / Cytoscape / NetworkX.
- `ns_proof_route_graph_interactive.html`: zoomable document graph.
- `novelty_diagnostics.png`, `sampling_tier_timeline.png`, `concept_confluence.png`, `series_confluence_network.png`: visual diagnostics.
- `novelty_robustness.json`: fixed-window permutation baseline.
- `run_analysis.py`: reproducible analysis script.
