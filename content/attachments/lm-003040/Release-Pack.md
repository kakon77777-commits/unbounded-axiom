# GVSS-05 — Visual Failure Stratification and Reachability Diagnosis

## Core failure state

$$
F_t
\in
\{
F_{\mathrm{sample}},
F_{\mathrm{constraint}},
F_{\mathrm{compile}},
F_{\mathrm{search}},
F_{\mathrm{reach}},
F_{\mathrm{eval}},
F_{\mathrm{intent}}
\}.
$$

## Core reroll theorem

If every independent reroll succeeds with probability at least $p_0$, then $n$ consecutive failures have probability at most:

$$
(1-p_0)^n.
$$

## Core no-go

$$
\boxed{
\text{finite bad seeds}
\not\Rightarrow
\text{zero generator reachability}.
}
$$

## Core control principle

$$
\boxed{
\textbf{
A failed image is an observation.
A failure layer is a hypothesis.
}
}
$$

## Package contents

- canonical paper;
- literature audit;
- roadmap v0.5;
- GVSS-06 handoff;
- theorem index;
- tests;
- validation;
- checksums.
