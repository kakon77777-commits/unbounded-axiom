# GVSS-06 — Diagnostic Visual Control and Minimal Intervention Policies

## Core belief control

$$
b_t
\to
a_t
\to
F_{t+1}
\to
Y_{t+1}
\to
b_{t+1}.
$$

## Core action classes

$$
\boxed{
\text{diagnose}
\vee
\text{correct}
\vee
\text{clarify}
\vee
\text{stop}.
}
$$

## Core one-step value

$$
\operatorname{VoD}(d\mid b)
=
R(b)
-
\mathbb E R(b^Y)
-
c(d).
$$

## Human clarification threshold

For two intents with wrong-action loss $L$:

$$
c_H
<
L\min(p,1-p).
$$

## Core no-go

$$
\boxed{
\text{least-cost currently justified correction}
\not\Rightarrow
\text{optimal sequential control}.
}
$$

## Package contents

- canonical paper;
- literature audit;
- roadmap;
- GVSS-07 handoff;
- theorem index;
- tests;
- validation;
- checksums.
