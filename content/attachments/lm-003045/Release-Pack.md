# GVSS-10 — Task-Conditioned Visual Routing, Capability Attribution, and Portfolio Learning

## Core capability

$$
\mathcal C_\nu(\theta)
=
E[
U
\mid
\theta,\nu
].
$$

## Core data warning

$$
\boxed{
\text{historical routed average}
\not\Rightarrow
\text{provider capability ranking}.
}
$$

## Core support no-go

$$
\boxed{
\text{no routing overlap}
\Longrightarrow
\text{unobserved provider value not point identified}.
}
$$

## Core IPS estimator

$$
\widehat V_{\mathrm{IPS}}
=
\frac1n
\sum_i
\frac{
\pi(A_i\mid\theta_i)
}{
\mu(A_i\mid\theta_i)
}
R_i.
$$

## Core attribution no-go

$$
\boxed{
\text{final multi-stage reward}
\not\Rightarrow
\text{provider-stage causal contribution}.
}
$$

## Package contents

- canonical paper;
- literature audit;
- roadmap;
- GVSS-11 handoff;
- theorem index;
- tests;
- validation;
- checksums.
