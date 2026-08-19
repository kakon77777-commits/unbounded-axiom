# VWDC-02 Handoff — Compositional Visual–World Reachability Graphs

## Starting state

VWDC-01 defines:

$$
O_{\mathrm{vis}}:
\mathcal X_W
\to
\Omega_\Sigma
$$

and partial lift:

$$
L:
D_L
\subseteq
\Omega_\Sigma
\to
\mathcal W_\kappa.
$$

It establishes:

$$
L\circ O_{\mathrm{vis}}
\neq
\operatorname{Id}
$$

in general.

It defines:

$$
\mathcal R_{\mathrm{bridge}}
=
\mathcal R_{\mathrm{GVSS}}
\cap
\mathcal L_\kappa.
$$

## Objective

Build a typed graph containing both visual artifacts and runnable worlds.

## Candidate node types

- VisualArtifact
- VisualProvider
- RunnableWorld
- WorldCheckpoint
- Evaluator
- Intervention
- LiftModel

## Candidate edge types

- GENERATE
- EDIT
- REPAIR
- RENDER
- LIFT
- FORK
- INTERVENE
- CHECKPOINT
- RESTORE
- EVALUATE

## Main questions

1. When can composition reach beyond one-stage provider union?
2. When does a LIFT edge create a runnable world rather than a scene artifact?
3. How do edge defects compose?
4. What is the least-cost contract-valid path?
5. When is one mixed visual/world path dominated?
6. Can cycles improve state or only accumulate cost/debt?
7. How should world and visual identities be preserved?
8. How should evidence packets move along mixed paths?

## Required no-go

Do not identify:
- image edit with world intervention;
- visual equality with checkpoint equality;
- render consistency with dynamics validity;
- final image quality with world evidence.
