# VWDC-01 Bridge Map — GVSS ↔ WDC

## Shared meta-layer

RRT remains frozen.

RRT supplies:
- observer fibers;
- representation dependence;
- defect transport;
- provenance-preserving change.

## GVSS layer

$$
I\in\Omega_\Sigma.
$$

Provides:
- visual state space;
- visual constraints;
- provider reachability;
- evaluators;
- routing;
- visual provenance.

## WDC layer

$$
W
=
(
ID,
Parent,
X,
\mathcal D,
\mathcal A,
\mathcal G,
\mathcal H,
\Theta,
\mathcal O,
\mathcal E,
\mathbf B,
\kappa
).
$$

Provides:
- persistent state;
- dynamics;
- actions/interventions;
- local history;
- identity;
- checkpoints/forks;
- world evidence.

## Bridge operator

$$
O_{\mathrm{vis}}:
\mathcal X_W
\to
\Omega_\Sigma.
$$

## Reverse candidate operator

$$
L_{\mathrm{vis}\to W}:
D_L
\subseteq
\Omega_\Sigma
\to
\mathcal W_\kappa.
$$

Generally:

$$
L\circ O_{\mathrm{vis}}
\neq
\operatorname{Id}.
$$

## Bridge-compatible reachability

$$
\mathcal R_{\mathrm{bridge}}
=
\mathcal R_{\mathrm{GVSS}}
\cap
O_{\mathrm{vis}}(
\mathcal W_\kappa
).
$$

## Promotion ladder

```text
VISUAL_ONLY
  -> RENDER_CONSISTENT
  -> CONTRACT_VALID
  -> DYNAMICS_TESTED
  -> RUNNABLE
  -> WORLD_EVIDENCE_VALID
  -> REALITY_TRANSPORT_REVIEWED
```

## Next bridge

VWDC-02:
typed visual/world reachability graph with:
- generate;
- edit;
- lift;
- fork;
- intervene;
- observe;
- evaluate;
- checkpoint;
- restore.
