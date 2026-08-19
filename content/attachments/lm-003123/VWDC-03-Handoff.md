# VWDC-03 Handoff — Visual World Branching, Lineage, and Evidence Transport

## Starting state

VWDC-02 defines typed graph:

$$
G_{\mathrm{VW}}
=
(
V,E,\tau,\sigma
)
$$

with node types:

$$
\mathsf T,\mathsf V,\mathsf U,\mathsf W,\mathsf C,\mathsf E.
$$

It defines mixed paths and evidence policies:

$$
\mathsf{DERIVED},
\mathsf{WORLD\_OBSERVATION},
\mathsf{INTERVENTIONAL},
\mathsf{EXTERNAL\_MEASUREMENT}.
$$

It proves RESTORE can revisit state while provenance lineage remains a DAG if restoration creates a new world identity.

## Objective

Formalize branch ancestry, evidence dependence, invalidation/replay, and world/visual lineage.

## Main questions

1. When are sibling-world outputs statistically/causally dependent?
2. What common-parent information must be preserved?
3. When may evidence from sibling branches be combined?
4. How should evaluator/provider invalidation propagate through branch evidence?
5. What checkpoint is needed for clean replay?
6. When can two branches be merged?
7. How do visual artifact lineage and world lineage interlock?
8. What transport contract permits world evidence to support a real-world claim?

## Desired form

$$
\boxed{
\text{branch graph}
+
\text{common ancestry}
+
\text{evidence dependencies}
+
\text{checkpoints}
\Longrightarrow
\text{valid aggregation}
+
\text{replay}
+
\text{transport boundary}.
}
$$

## Prohibitions

- Do not treat sibling branches as independent merely because their rendered images differ.
- Do not merge worlds from visual similarity alone.
- Do not count deterministic descendants as independent evidence.
- Do not transport world evidence to reality without an explicit contract.
