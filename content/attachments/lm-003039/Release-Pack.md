# GVSS-04 — Reflexive Visual Navigation Release Pack

## Canonical paper

`Paper_04_Reflexive_Visual_Navigation_v0.1.md`

## Position

This is **Global Visual Space & Generative Navigation — Paper 04**.

It is a domain specialization of the frozen RRT framework.

It is **not RRT-21**.

## Core bridge

$$
\boxed{
\text{GVSS state-space geometry}
+
\text{RRT representation reflexivity}
=
\text{Reflexive Visual Navigation}.
}
$$

## Core action separation

$$
\boxed{
\text{RESAMPLE}
\neq
\text{RECOMPILE}
\neq
\text{REBIND}.
}
$$

## Core recursion

$$
\boxed{
e_{t+1}
\preceq
A_te_t+\varepsilon_t.
}
$$

## Package contents

- canonical paper;
- literature audit;
- GVSS × RRT bridge map;
- roadmap;
- GVSS-05 handoff;
- theorem index;
- regression tests;
- validation report;
- checksums.
