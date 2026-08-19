# GVSS-08 — Robust Visual Diagnostic Control under Model Uncertainty and Regime Drift

## Core state

$$
(
b_t,
\mathcal U_t,
\pi_t,
\nu_t,
B_t,
r_t
).
$$

## Core modes

$$
\boxed{
\text{nominal}
\vee
\text{robust}
\vee
\text{recalibrate}
\vee
\text{fallback}
\vee
\text{quarantine}
\vee
\text{stop}.
}
$$

## Nominal/robust margin

$$
\widehat Q(a^\star)+\Delta_{a^\star}
<
\widehat Q(b)-\Delta_b
$$

certifies action stability across the ambiguity set.

## Drift fallback threshold

$$
\pi
>
\frac{
c_F+s_1-s_0
}{
(d_0-d_1)+(s_1-s_0)
}.
$$

## Core quarantine boundary

$$
\boxed{
\text{future containment}
\not\Rightarrow
\text{past belief decontamination}.
}
$$

## Package contents

- canonical paper;
- literature audit;
- roadmap;
- GVSS-09 handoff;
- theorem index;
- tests;
- validation;
- checksums.
