# 空間域證明包圍論 — Series Route Map v0.1

## Paper 01 — 全域量詞、反例域與可驗證收縮

建立：

$$
\mathcal C_X\subseteq\Omega_t,
$$

$$
\Omega_{t+1}=\Omega_t\cap H_t,
$$

以及 finite / infinite closure、branch coverage、gluing、trace compilation、zero-measure no-go。

## Paper 02 — 路徑域完備性與表示非坍縮

核心問題：

$$
\phi:D\to X
$$

何時能保證沒有漏掉或壓扁 proof-relevant counterexample fibers？

預計連接：DEST 多域判定、表示逃逸、X 積分 non-collapse、abstract interpretation Galois connection。

## Paper 03 — 多維覆蓋、Gap 與 Global Closure Certificate

把 proof completion 從單一 coverage ratio 改為：

$$
(\rho_D,\rho_B,\rho_{\partial},\rho_{\partial\partial},\rho_C,\rho_R).
$$

研究 branch completeness、boundary ownership、cycle / gluing audit。

## Paper 04 — Proof Trace Compilation 與驗證攤銷

研究：

$$
\text{verified proof history}
\to
\text{compiled pruning state}
\to
\text{lower marginal discovery cost}.
$$

建立完整成本帳本：

$$
C_{m discover}+C_{m verify}+C_{m coverage}+C_{m glue}+C_{m maintain}.
$$

## Paper 05 — Discovery–Verification Inversion

形式化／實驗研究是否存在 proof-space phase transition：

$$
C^{\rm discover}\downarrow,
\qquad
C^{\rm verify}+C^{\rm coverage}\uparrow.
$$

## Paper 06 — Survivor Measure、零測度與不可約例外集

使用 X 積分／前測度觀點嚴格區分：

$$
\mu(\Omega_t)\to0
$$

與

$$
\Omega_t=\varnothing.
$$

研究 measure-zero survivor、fractal survivor、singular boundary、structural residue。

## Paper 07 — Enclosure Routing：如何選下一刀

研究 marginal exclusion yield：

$$
\Delta\mathfrak F(a\mid\Omega_t)
$$

和 verification cost 的比值，連接 MCDM、有效覆蓋率、概念積分與 solution-space geometry。

## Paper 08 — SDPE Runtime / Benchmark

最小 runtime：

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
\mathsf{GlueAudit}
\to
\mathsf{Commit}.
$$

要求 theorem ledger、dependency DAG、branch graph、replay checker、stale propagation、rollback。

## Case-study track

- Collatz Hard-Zeta survivor-space contraction；
- SAT / cube-and-conquer / LRAT cover certificate；
- 小型圖論猜想；
- finite combinatorial classification problem；
- Lean formal proof search benchmark。
