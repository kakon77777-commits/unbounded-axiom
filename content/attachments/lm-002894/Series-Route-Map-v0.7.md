# 空間域證明包圍論 — Series Route Map v0.7

**Updated after Paper 07**  
**Date:** 2026-08-14

## P01 — Survivor Soundness

$$
\mathcal C\subseteq\Omega_t,
\qquad
\Omega_{t+1}=\Omega_t\cap H_t.
$$

## P02 — Representation Faithfulness

RouteCert、fiber saturation、singular-fiber semantics、Route Atlas。

## P03 — Global Coverage / Closure

Typed gaps 與：

$$
\mathsf{GCC}.
$$

## P04 — Trace Compilation

proof-history DAG、closure basis、support-aware rollback、incremental replay。

## P05 — Discovery–Verification Inversion

$$
D^{\rm resolve}\neq D^{\rm frontier}.
$$

建立 Weak / Strong / Productive DVI 與 frontier-hardening no-go。

## P06 — Residual Geometry / Exceptional Core

$$
\Omega_\infty=\bigcap_t\Omega_t,
$$

$$
\mu(\Omega_t)\to0
\not\Rightarrow
\Omega_\infty=\varnothing.
$$

建立 closure-separating diagnostics、relative theorem-language core、MeasureCert、exceptional-core hardening。

## P07 — Enclosure Routing

### Current marginal exclusion

$$
\boxed{
X_t(a)=\Omega_t\setminus H_a.
}
$$

只計 current survivor 上的新排除，避免重複 theorem 計功。

### Finite obligation model

$$
\boxed{
F_t(A)
=
\sum_{o\in\cup_{a\in A}R_t(a)}w_t(o).
}
$$

$F_t$ 是 monotone submodular。

只有在 routing objective 真正符合此 geometry 時，greedy approximation theory 才可合法使用。

### Synergy detector

$$
\boxed{
\Gamma_t(a,b\mid S)
=
\Delta(a\mid S\cup\{b\})-\Delta(a\mid S).
}
$$

若 $\Gamma>0$，存在 complementarity；proof value 不再是純 diminishing returns。

### Volume-greedy no-go

zero-measure exceptional core 可以是唯一 GCC blocker，因此：

$$
\boxed{
\text{largest volume cut}
\not\Rightarrow
\text{largest closure value}.
}
$$

### Route-value vector

$$
\boxed{
\mathbf V_t(a)
=
\left(
Y^{\rm excl},Y^{\rm gap},Y^{\rm core},Y^{\rm repr},Y^{\rm bridge},Y^{\rm cert};
-\mathbf C,-\mathbf R
\right).
}
$$

### Pareto routing

componentwise-dominated actions 可在所有 monotone preferences 下 prune。

### Bridge-aware lookahead

zero-immediate-yield refinement / bridge action 可以解鎖下一輪 closure theorem；myopic greedy 可以嚴格失敗。

### Closure fairness

persistent mandatory gaps 不得因 zero measure / low immediate score 永久 starvation。

### Routing protocol

$$
\boxed{
\mathsf{Profile}
\to\mathsf{GapExtract}
\to\mathsf{ActionGenerate}
\to\mathsf{SafetyGate}
\to\mathsf{ValueEstimate}
\to\mathsf{ParetoPrune}
\to\mathsf{GeometryClassify}
\to\mathsf{Select}
\to\mathsf{Execute}
\to\mathsf{Verify}
\to\mathsf{Update}
\to\mathsf{Compile}.
}
$$

## Current stack

$$
\boxed{
\begin{aligned}
&\text{P01 Survivor Soundness}\
&\to\text{P02 Representation Faithfulness}\
&\to\text{P03 Global Closure}\
&\to\text{P04 Trace Compilation}\
&\to\text{P05 Cost-Phase Separation}\
&\to\text{P06 Residual Geometry}\
&\to\text{P07 Cost-Aware Enclosure Routing}.
\end{aligned}
}
$$

## Paper 08 — Runtime, Benchmark, and Proof-Space Observatory

**Next.**

整合前七篇成可執行 schema：

$$
\boxed{
\mathbb S_t
=
\langle
\Omega_t,
RouteCert_t,
\mathbf G_t,
GCC_t,
\mathcal H_t,
Compiled_t,
DVI_t,
SurvProf_t,
RouteDecision_t
\rangle.
}
$$

最小 pipeline：

$$
\boxed{
\begin{aligned}
&\mathsf{Detect}\
&\to\mathsf{Profile}\
&\to\mathsf{GapExtract}\
&\to\mathsf{ActionGenerate}\
&\to\mathsf{Route}\
&\to\mathsf{Propose}\
&\to\mathsf{Verify}\
&\to\mathsf{CoverageAudit}\
&\to\mathsf{BoundaryAudit}\
&\to\mathsf{GlueAudit}\
&\to\mathsf{Compile}\
&\to\mathsf{Commit}.
\end{aligned}
}
$$

Paper 08 應產出：

- state schema；
- event ledger；
- theorem / gap / route APIs；
- replay checker；
- routing benchmark；
- DVI benchmark；
- exceptional-core benchmark；
- finite toy closure benchmark；
- Hard-Zeta case-study adapter specification。
