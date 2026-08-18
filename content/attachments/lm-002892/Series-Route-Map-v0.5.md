# 空間域證明包圍論 — Series Route Map v0.5

**Updated after Paper 05**  
**Date:** 2026-08-14

---

## Paper 01 — 全域量詞、反例域與可驗證收縮

建立：

$$
\boxed{
\mathcal C\subseteq\Omega_t,
\qquad
\Omega_{t+1}=\Omega_t\cap H_t.
}
$$

核心：theorem cut 不得誤刪真反例。

---

## Paper 02 — 路徑域完備性與表示非坍縮

建立 RouteCert、fiber saturation、singular fibers、Route Atlas。

核心：representation 不得壓掉 proof-relevant counterexample distinctions。

---

## Paper 03 — 多維覆蓋、Gap 與 Global Closure Certificate

建立：

$$
\boxed{
\mathbf G=(G_D,G_B,G_{\partial},G_C,G_G,G_R)
}
$$

與

$$
\boxed{
\mathsf{GCC}
=
\langle
Master,Atlas,CoverCert,LocalCerts,BoundaryCert,LiftCerts,
GlueMode,GlueCert,DepDAG,Version,Replay
\rangle.
}
$$

核心：local correctness 不等於 global completeness。

---

## Paper 04 — Proof Trace Compilation 與 Verification Amortization

建立 proof-history DAG：

$$
\mathcal H_t=(V_t,E_t),
$$

closure basis：

$$
\mathcal B_{\rm dep}(q)=\operatorname{Anc}(q)\cup\{q\},
$$

compiled support index：

$$
\kappa_t(x)=\#\{v\in A_t:x\in E_v\},
$$

以及 support-aware rollback / incremental replay。

核心：留下的 proof trace 可以成為 sound compiled pruning state，而不是靜態日誌。

---

## Paper 05 — Discovery–Verification Inversion

### Discovery split

$$
\boxed{
D_t^{\rm resolve}
\neq
D_t^{\rm frontier}.
}
$$

routine-resolution 是已知／可編譯區域的解析成本；frontier discovery 是取得下一個 nonredundant theorem cut 的成本。

### Fixed-distribution compilation theorem

若 query distribution 固定、compiled region 擴張且 hit cost 不高於 miss cost：

$$
\boxed{
D_{t+1}^{\rm resolve}\le D_t^{\rm resolve}.
}
$$

### Frontier drift decomposition

$$
\boxed{
\Delta D_t^{\rm resolve}
=
-G_t^{\rm compile}
+
P_t^{\rm drift}.
}
$$

加速條件：

$$
\boxed{
G_t^{\rm compile}>P_t^{\rm drift}.
}
$$

### Frontier cache no-go

嚴格 frontier-only sampling 下：

$$
\boxed{
\text{direct compiled-hit gain}=0.
}
$$

所以 known-region acceleration 不推出 frontier theorem discovery acceleration。

### Verification bundle

$$
W_t
=
C_t^{\rm verify}
+C_t^{\rm coverage}
+C_t^{\rm glue}
+C_t^{\rm maintain}
+C_t^{\rm replay}.
$$

verification share：

$$
\boxed{
\sigma_t=\frac{W_t}{D_t+W_t}.
}
$$

### DVI taxonomy

- Reuse Acceleration；
- Verification-Dominance Transition；
- Weak DVI；
- Strong DVI；
- Productive DVI；
- Frontier Hardening。

### Productive inversion

可以同時出現：

$$
\boxed{
C_t^{\rm total}\downarrow
\quad\text{且}\quad
\sigma_t\uparrow.
}
$$

因此「整體越來越快，但主要成本逐漸變成驗證」是數學上可一致的 regime。

### Status

Weak DVI 有 compilation theorem 與 domain-specific empirical precedents。

Strong DVI：

$$
\boxed{
D_t^{\rm frontier}\downarrow
}
$$

仍是 open falsifiable hypothesis。

---

## Current stack after Paper 05

$$
\boxed{
\begin{aligned}
&\text{P01 Survivor Soundness}\\
&\to\text{P02 Representation Faithfulness}\\
&\to\text{P03 Global Coverage / Closure}\\
&\to\text{P04 Trace Compilation / Incremental Replay}\\
&\to\text{P05 Cost-Phase Separation / DVI Falsifiability}.
\end{aligned}
}
$$

---

## Paper 06 — Survivor Measure、零測度與不可約例外集

**Next.**

Paper 05 已證：

$$
\boxed{
\text{survivor space 變小}
\not\Rightarrow
\text{frontier discovery 變容易}.
}
$$

Paper 06 將研究：

$$
\mu(\Omega_t)\to0
$$

與

$$
\Omega_t=\varnothing
$$

的本質差異，以及：

- measure-zero survivor；
- fractal survivor；
- singular fiber concentration；
- exceptional-set hardening；
- structural residue；
- 哪些 measure / dimension 指標能作 routing diagnostic，哪些不能作 proof closure。

這一篇會直接決定 Strong DVI 是否可能在 proof-space 後期失效。

---

## Paper 07 — Enclosure Routing

研究下一刀的 marginal exclusion yield、frontier hardness 與 verification burden。

---

## Paper 08 — SDPE Runtime / Benchmark

最低 runtime：

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

Paper 05 新增 runtime telemetry：

$$
D^{\rm resolve},
D^{\rm frontier},
W,
\sigma,
h,
G^{\rm compile},
P^{\rm drift}.
$$
