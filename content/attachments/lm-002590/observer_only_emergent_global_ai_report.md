# Observer-Only Emergent Global AI Experiment

## Purpose
No AI is allowed to directly read the hidden global state during reconstruction.
The simulator keeps the true state only for final scoring.

Embedded observers receive:
- their own local 2D measurements,
- optional time history,
- communication with other observers.

The network must build an emergent global estimate G_emergent.

## Experiment
Hidden state dimension: 4
Observer counts: 5, 8, 12, 20
Each observer instantaneous rank: 2
Noise sigma: 0, 0.005, 0.01, 0.03
120 random worlds per setting

A fraction of observers is deliberately corrupted by persistent measurement bias.

## Main results
- Full-rank fused network rate: 1.000000
- History-only full observability rate: 1.000000
- Mean state error before diagnosis: 0.0494479
- Mean state error after suspect removal: 0.0125506
- Mean history-only state error: 0.0226416
- Mean hybrid state error: 0.0136121
- Mean corrupted-observer detection rate: 0.945833
- Exact bad-set identification rate: 0.935937

## Interpretation
1. Collective communication can create global reconstructibility even though every individual observer is instantaneously incomplete.
2. Time history can independently create global observability for a single incomplete observer.
3. Observer-network consistency tests can identify corrupted local channels without direct access to the hidden state.
4. The hidden state is used only to evaluate the reconstruction after the fact, not to construct it.
5. Therefore G_emergent is not a disguised oracle: it is derived from local relations, communication, temporal transport, and consistency constraints.

## Series-B reading
Derived globality:

G_emergent = Fuse(local observations, history, dynamics, consistency).

The experiment implements:
- Paper 03: joint observer accessibility
- Paper 05: observer consistency
- Paper 06: derived globality from local data
- Paper 07: global invariant estimation after fusion

## Key next step
Replace linear measurements A_i z with nonlinear/partial measurement channels and replace direct least squares with a learned or agentic inference layer.
The observer mathematics stays the same while the inference engine becomes AI-driven.
