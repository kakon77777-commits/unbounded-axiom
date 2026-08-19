# VWDC-06 — Transport-Aware World Decisions, Policy Transfer, and Reality-Gap Robust Control

## Deployment certificate

$$
\boxed{
\widehat Q_W(\widehat a)-\delta_{\widehat a}
>
\max_{b\neq\widehat a}
[
\widehat Q_W(b)+\delta_b
].
}
$$

## One-step reality regret

$$
\boxed{
\operatorname{Regret}_R
\le
\delta_{a_R^\star}
+
\delta_{\widehat a}
\le
2\delta_{\max}.
}
$$

## Fixed-policy Sim2Real value bound

$$
\boxed{
\|
V_R^\pi-V_W^\pi
\|_\infty
\le
\frac{\epsilon_r}{1-\gamma}
+
\frac{
\gamma R_{\max}\epsilon_P
}{
(1-\gamma)^2
}.
}
$$

## Policy-induced RTC shift

$$
\boxed{
D_\pi
\le
D_{\mathrm{val}}
+
M TV(
d_\pi,d_{\mathrm{val}}
).
}
$$

## Deployment modes

```text
CERTIFIED_DEPLOY
ROBUST_DEPLOY
SHADOW
PROBE
SAFE_FALLBACK
HUMAN_REQUIRED
STOPPED
```

## Package contents

- canonical paper;
- literature audit;
- roadmap;
- VWDC-07 handoff;
- theorem index;
- tests;
- validation;
- checksums.
