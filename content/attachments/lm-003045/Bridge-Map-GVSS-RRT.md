# GVSS × RRT Bridge Map

## Frozen RRT side

RRT remains closed at RRT-20.

GVSS imports the frozen RRT meta-laws without reopening RRT numbering.

## Mapping

| RRT object | GVSS / runtime specialization |
|---|---|
| Representation regime | Prompt / Constraint / Style / Provider / Workflow state |
| Observer | Metric providers, VLM critic, human review |
| Reflexivity defect | Visual deficit / compiler mismatch / provider mismatch |
| Active sensing | Selecting evaluators / references / control providers |
| Action-observation reflexivity | Generate -> evaluate -> edit/rebind |
| Experiment allocation | Seed / verifier / backend / repair budget |
| Open-world model expansion | Adding new visual provider / model family |
| Representation-language expansion | Adding new style/control/constraint primitives |
| Provenance-preserving change | Runtime lineage child packets |
| Pareto frontier | Prompt/style/diversity/quality/cost tradeoff |

## Canonical GVSS state

$$
r_t
=
(
\mathsf G_t,
\Gamma_t,
C_t,
\Lambda_t,
\Pi_t,
O_t,
E_t,
B_t,
\mathsf{Prov}_t
).
$$

## Canonical loop

$$
I_t\sim K_{r_t}
$$

$$
Y_t=O_t(I_t,C_t)
$$

$$
a_t=\pi_{\mathrm{RVN}}(r_t,Y_t,B_t,H_t)
$$

$$
r_{t+1}=\Psi(r_t,a_t,Y_t).
$$

## Core diagnostic split

### RESAMPLE
Changes trajectory.

### RECOMPILE
Changes target/constraint representation.

### REBIND
Changes generator/provider reachable domain.

### REPAIR
Changes image locally/structurally.

### HUMAN_REVIEW
Changes observer set.

### SWITCH_BACKEND
Changes execution/generation regime.

## RRT final slogan specialized to GVSS

$$
\boxed{
\textbf{
Visual refinement transfers cost; it does not annihilate difficulty.
}
}
$$

A stronger style lock can reduce style defect while increasing homogenization.

A stricter verifier can improve accepted alignment while shrinking accepted reachability.

A stronger reference can preserve identity while reducing diversity.

A provider rebind can increase reachability while increasing switching and provenance debt.
