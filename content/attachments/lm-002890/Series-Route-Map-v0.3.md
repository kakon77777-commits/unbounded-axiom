# 空間域證明包圍論 — Series Route Map v0.3

**Updated after Paper 03**  
**Date:** 2026-08-14

## Paper 01 — 全域量詞、反例域與可驗證收縮

建立：

$$
\mathcal C\subseteq\Omega_t,
\qquad
\Omega_{t+1}=\Omega_t\cap H_t.
$$

核心：theorem cut 不得誤刪真反例。

## Paper 02 — 路徑域完備性與表示非坍縮

建立 representation saturation、fiber adequacy、RouteCert、Route Atlas。

核心：表示壓縮不得丟失 proof-relevant counterexample fibers。

## Paper 03 — 多維覆蓋、Gap 與 Global Closure Certificate

### Cover–Refutation Closure

$$
\mathcal C\subseteq\Omega,
\quad
\Omega\subseteq\bigcup_iU_i,
\quad
\mathcal C\cap U_i=\varnothing\ \forall i
$$

推出：

$$
\boxed{\mathcal C=\varnothing.}
$$

### Residual closure

$$
\boxed{
\mathcal C
\subseteq
\Omega\setminus\bigcup_{j\in J}U_j.
}
$$

### Typed gaps

$$
\boxed{
\mathbf G=(G_D,G_B,G_{\partial},G_C,G_G,G_R).
}
$$

### Closure modes

$$
\mathsf{RefutationOnly}
$$

需要 cover + local refutations。

$$
\mathsf{ConstructiveGluing}
$$

另外需要 overlap compatibility + proved gluing law。

### Global Closure Certificate

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

## Current closure stack

$$
\boxed{
\text{P01 Survivor Soundness}
\to
\text{P02 Representation Faithfulness}
\to
\text{P03 Global Coverage / Closure}.
}
$$

## Paper 04 — Proof Trace Compilation 與 Verification Amortization

下一步：

$$
\boxed{
\text{verified proof history}
\to
\text{closure basis}
\to
\text{compiled pruning state}
\to
\text{incremental replay}.
}
$$

核心問題：

- 怎麼抽取最小／近最小 closure basis？
- stale dependency 如何只 reopen 受影響區域？
- closed charts 如何編譯成低成本 pruning query？
- GCC 如何 incremental 更新而非全重算？
- verification cost 如何 amortize？

## Paper 05 — Discovery–Verification Inversion

研究：

$$
C^{\rm discover}\downarrow,
\qquad
C^{\rm verify}+C^{\rm coverage}+C^{\rm glue}\uparrow.
$$

## Paper 06 — Survivor Measure、零測度與不可約例外集

區分：

$$
\mu(\Omega_t)\to0
$$

與

$$
\Omega_t=\varnothing.
$$

## Paper 07 — Enclosure Routing

研究 marginal exclusion yield 與 verification cost。

## Paper 08 — SDPE Runtime / Benchmark

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
\mathsf{Commit}.
$$
