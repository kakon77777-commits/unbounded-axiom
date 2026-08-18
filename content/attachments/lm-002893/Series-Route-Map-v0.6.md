# 空間域證明包圍論 — Series Route Map v0.6

**Updated after Paper 06**  
**Date:** 2026-08-14

## P01 — Survivor Soundness

$$
\mathcal C\subseteq\Omega_t,
\qquad
\Omega_{t+1}=\Omega_t\cap H_t.
$$

## P02 — Representation Faithfulness

route representation 不得壓掉 proof-relevant fibers；建立 RouteCert / saturation / singular-fiber semantics。

## P03 — Global Coverage / Closure

建立 typed gaps 與 Global Closure Certificate：

$$
\mathsf{GCC}.
$$

核心：local correctness 不等於 global completeness。

## P04 — Trace Compilation / Incremental Replay

建立 proof-history DAG、closure basis、support index、support-aware rollback、incremental replay、amortization。

## P05 — Discovery–Verification Inversion

區分：

$$
D^{\rm resolve}
\neq
D^{\rm frontier}.
$$

建立 Weak / Strong / Productive DVI 與 frontier-hardening no-go。

## P06 — Survivor Measure、零測度與不可約例外集

### Limit core

$$
\boxed{
\Omega_\infty=\bigcap_t\Omega_t.
}
$$

soundness：

$$
\boxed{
\mathcal C\subseteq\Omega_\infty.
}
$$

### Measure no-go

$$
\boxed{
\mu(\Omega_t)\to0
\not\Rightarrow
\Omega_\infty=\varnothing.
}
$$

在 finite-measure decreasing chain 中只得到：

$$
\mu(\Omega_\infty)=0.
$$

### Compact survivor trap

若每個 $\Omega_t$ 非空 compact 且

$$
\operatorname{diam}(\Omega_t)\to0,
$$

則：

$$
\boxed{
\Omega_\infty
\text{ 是 singleton}.
}
$$

### Closure-separating diagnostic

$$
q(A)=0
\Longrightarrow
A=\varnothing
$$

必須對 admissible survivor family 成立，scalar zero 才能作 closure certificate。

### Positive gap rescue

若非空 survivors 全部滿足

$$
q(A)\ge\varepsilon_*>0,
$$

則

$$
q(A)<\varepsilon_*
\Longrightarrow
A=\varnothing.
$$

### Source-preserving route measure

$$
\boxed{
\nu_\phi(B)=\mu_D(\phi^{-1}(B)).
}
$$

route geometric measure 不能自動代表 concrete survivor mass。

### Relative theorem-language core

$$
\boxed{
\operatorname{Core}(\Omega_0,\mathscr H)
=
\Omega_0\cap\bigcap_{H\in\mathscr H}H.
}
$$

非空只表示 current theorem language 尚不足以分離 residue，不表示存在真反例。

### Exceptional-core hardening

新的 open hypothesis：

$$
\mu(\Omega_t)\downarrow0
$$

可能伴隨

$$
D_t^{\rm frontier}\uparrow
$$

若 survivor 集中到 singular / boundary / theorem-language-irreducible core。

## Current stack

$$
\boxed{
\begin{aligned}
&\text{P01 Survivor Soundness}\\
&\to\text{P02 Representation Faithfulness}\\
&\to\text{P03 Global Closure}\\
&\to\text{P04 Trace Compilation}\\
&\to\text{P05 Cost-Phase Separation}\\
&\to\text{P06 Residual Geometry / Exceptional Core}.
\end{aligned}
}
$$

## Paper 07 — Enclosure Routing：如何選下一刀

**Next.**

Paper 06 已證：大體積 reduction 不一定等於高 proof value；measure-zero singular core 可能承擔全部剩餘難度。

因此 Paper 07 將建立 multi-objective route selection：

$$
\boxed{
\text{expected exclusion yield}
+
\text{gap relevance}
+
\text{core separability gain}
}
$$

相對於：

$$
\boxed{
C^{\rm discover}
+C^{\rm verify}
+C^{\rm coverage}
+C^{\rm glue}
+C^{\rm maintain}
+C^{\rm refine}.
}
$$

並區分：

- bulk-cut action；
- boundary action；
- representation refinement；
- theorem-language expansion；
- bridge theorem；
- certificate / coverage repair。

這是全域量詞—研究路由、有效覆蓋率、解空間幾何、MCDM 與概念積分快速通道正式匯流的位置。

## Paper 08 — SDPE Runtime / Benchmark

最小 pipeline：

$$
\mathsf{Detect}
\to
\mathsf{Route}
\to
\mathsf{Propose}
\to
\mathsf{Verify}
\to
\mathsf{CoverageAudit}
\to
\mathsf{BoundaryAudit}
\to
\mathsf{GlueAudit}
\to
\mathsf{Compile}
\to
\mathsf{Commit}.
$$

新增 P06 telemetry：

$$
\mathsf{SurvProf}_t,
\quad
\eta_t^{\rm exc},
\quad
CoreLang_t,
\quad
SepGap_t,
\quad
MeasureCert_t.
$$
