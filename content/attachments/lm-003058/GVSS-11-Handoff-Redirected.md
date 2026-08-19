# GVSS-11 Handoff — Compositional Visual Reachability Graphs and Cross-Provider Transformation Paths

## Starting state

GVSS-10 defines task-conditioned provider capability:

$$
\mathcal C_\nu(\theta)
=
E[
U
\mid
\theta,\nu
]
$$

and one-stage routing.

It also defines provider paths:

$$
p
=
(
\nu_1,a_1,\ldots,\nu_m
)
$$

but proves that final reward alone does not identify stage contribution.

## Objective

Formalize multi-stage cross-provider composition as a graph of visual transformation operators.

## Main questions

1. When can composition reach outside the simple provider union?
2. How should provider edge compatibility be represented?
3. What is the lowest-cost path to a target visual region?
4. How do semantic/style/identity defects accumulate over path composition?
5. When can a cycle be useful?
6. How does switching/translation cost affect reachability?
7. How should path dominance be defined?
8. What provenance is required for replay and attribution?

## Desired form

$$
\boxed{
\text{provider nodes}
+
\text{typed transformation edges}
+
\text{cost/defect}
\Longrightarrow
\text{compositional reachable graph}
+
\text{optimal path frontier}.
}
$$

## Prohibitions

- Do not equate multi-stage compositional reachability with simple union coverage.
- Do not assume stage contributions are identifiable from final reward alone.
- Preserve intermediate artifacts, provider versions, and transformation defects.
- Do not treat a cycle as beneficial unless it produces a declared gain exceeding its cost/debt.
