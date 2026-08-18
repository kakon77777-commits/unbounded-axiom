# 空間域證明包圍論 — Series Route Map v0.2

**Date:** 2026-08-14  
**Completed:** Paper 01, Paper 02

---

## Paper 01 — 全域量詞、反例域與可驗證收縮

建立：

$$
\mathcal C_X\subseteq\Omega_t,
$$

$$
\Omega_{t+1}=\Omega_t\cap H_t,
$$

finite / infinite closure、branch coverage、gluing obligation、trace compilation、zero-measure no-go。

---

## Paper 02 — 路徑域完備性與表示非坍縮

新增地基：

$$
\alpha_\phi(A)=\phi(A),
\qquad
\gamma_\phi(B)=\phi^{-1}(B),
$$

$$
\boxed{
\alpha_\phi\dashv\gamma_\phi,
}
$$

$$
\boxed{
\operatorname{Sat}_\phi(A)
=\phi^{-1}(\phi(A)).
}
$$

proof-relevant set 可精確下降到 route domain，當且僅當它 fiber-saturated。

定義：

$$
m_\Sigma(x)
=
|\{\sigma_\Sigma(d):d\in F_x\}|,
$$

$$
\operatorname{Sing}_\Sigma(\phi)
=
\{x:m_\Sigma(x)>1\}.
$$

合法策略：

$$
\boxed{
\text{Exact Quotient}
\quad\vee\quad
\text{Conservative Envelope + Fiber-Safe Exclusion}.
}
$$

新增 Route Representation Contract 與六項 route adequacy obligations：coverage、fiber、lift、operator、boundary、replay。

---

## Paper 03 — 多維覆蓋、Gap 與 Global Closure Certificate

**Next.**

核心問題：

$$
\boxed{
\text{很多局部 route 都正確}
\not\Rightarrow
\text{整個 counterexample atlas 已完整關閉}.}
$$

將建立：

$$
\boldsymbol\rho
=
(\rho_D,\rho_B,\rho_{\partial},\rho_{\partial\partial},\rho_C,\rho_R),
$$

以及：

- branch union completeness；
- Gap taxonomy；
- boundary ownership；
- overlap compatibility；
- cocycle / cycle debt；
- local-to-global gluing；
- finite / infinite global closure certificate；
- compact finite-subcover route；
- coverage ratio no-go。

---

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
C^{\rm discover}
+C^{\rm verify}
+C^{\rm coverage}
+C^{\rm glue}
+C^{\rm maintain}.
$$

---

## Paper 05 — Discovery–Verification Inversion

研究是否存在 proof-space phase transition：

$$
C^{\rm discover}\downarrow,
\qquad
C^{\rm verify}+C^{\rm coverage}+C^{\rm glue}\uparrow.
$$

---

## Paper 06 — Survivor Measure、零測度與不可約例外集

區分：

$$
\mu(\Omega_t)\to0
$$

與

$$
\Omega_t=\varnothing.
$$

研究 measure-zero survivor、fractal survivor、singular fiber、structural residue。

---

## Paper 07 — Enclosure Routing：如何選下一刀

研究 marginal exclusion yield：

$$
\Delta\mathfrak F(a\mid\Omega_t)
$$

相對於 discovery / verification / coverage cost。

---

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

要求 theorem ledger、representation contracts、dependency DAG、branch graph、replay checker、stale propagation、rollback。

---

## Case-study track

- Collatz Hard-Zeta survivor-space contraction；
- SAT / cube-and-conquer / LRAT cover certificate；
- finite graph classification；
- Lean proof search；
- representation-refinement toy benchmark。
