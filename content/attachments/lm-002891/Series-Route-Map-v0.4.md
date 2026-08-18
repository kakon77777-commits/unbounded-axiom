# 空間域證明包圍論 — Series Route Map v0.4

**Updated after Paper 04**  
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

核心：representation 不得先壓掉 proof-relevant counterexample distinctions。

---

## Paper 03 — 多維覆蓋、Gap 與 Global Closure Certificate

建立：

$$
\boxed{
\mathbf G=(G_D,G_B,G_{\partial},G_C,G_G,G_R)
}
$$

及：

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

### 新增 proof-history state

$$
\boxed{
\mathcal H_t=(V_t,E_t).
}
$$

### Closure basis

$$
\boxed{
\mathcal B_{\rm dep}(q)
=
\operatorname{Anc}(q)\cup\{q\}.
}
$$

在 dependency completeness / compositional checker 下，target replay 不需整個 discovery history。

### Compiled support index

$$
\boxed{
\kappa_t(x)
=
\#\{v\in A_t:x\in E_v\}.
}
$$

若 $\kappa_t(x)>0$，存在 active sound certificate 排除 $x$。

### Support-aware rollback

$$
\boxed{
R(Z^+)
=
\{x:\kappa_{\rm old}(x)>0,\;\kappa_{\rm new}(x)=0\}.
}
$$

只 reopen 所有 support 都失效的 region。

### Incremental replay

$$
\boxed{
Dirty(M)=M\cup\operatorname{Desc}(M).
}
$$

在 dependency metadata 完整及 checker deterministic / compositional 下，只 replay dirty closure 與 full replay 等價。

### Cost model

$$
\boxed{
C_{\rm comp}(N)
=
B+N[h c_H+(1-h)c_F+m].
}
$$

若

$$
\Delta=h(c_F-c_H)-m>0,
$$

break-even：

$$
\boxed{
N>B/\Delta.
}
$$

### 新 closure stack

$$
\boxed{
\begin{aligned}
&\text{P01 Survivor Soundness}\\
&\to\text{P02 Representation Faithfulness}\\
&\to\text{P03 Global Coverage / Closure}\\
&\to\text{P04 Trace Compilation / Incremental Replay}.
\end{aligned}
}
$$

---

## Paper 05 — Discovery–Verification Inversion

**Next.**

Paper 04 已提供觀測 primitives：

$$
\boxed{
C_t^{\rm discover},
C_t^{\rm verify},
C_t^{\rm coverage},
C_t^{\rm glue},
C_t^{\rm maintain},
C_t^{\rm replay}.
}
$$

另有：

$$
\boxed{
h_t,\chi_t,|Dirty_t|,|R_t|.}
$$

Paper 05 將研究是否存在可重現 phase regime：

$$
\boxed{
C_t^{\rm discover}\downarrow,
\qquad
\frac{C_t^{\rm verify}+C_t^{\rm coverage}+C_t^{\rm glue}+C_t^{\rm maintain}}
{C_t^{\rm total}}\uparrow.
}
$$

並嚴格區分：

- true discovery acceleration；
- reconstruction avoidance；
- hidden build-cost transfer；
- frontier-hardening；
- verification-dominated phase。

---

## Paper 06 — Survivor Measure、零測度與不可約例外集

研究：

$$
\mu(\Omega_t)\to0
$$

與

$$
\Omega_t=\varnothing
$$

的不可混淆性。

---

## Paper 07 — Enclosure Routing

研究下一刀的 marginal exclusion yield / verification burden。

---

## Paper 08 — SDPE Runtime / Benchmark

Runtime 擴充成：

$$
\boxed{
\begin{aligned}
&\mathsf{Detect}\to\mathsf{Route}\to\mathsf{KnownnessGate}\to\\
&\mathsf{CompiledPrune}\vee\mathsf{Explore}\to\mathsf{Verify}\to\\
&\mathsf{CoverageAudit}\to\mathsf{BoundaryAudit}\to\mathsf{GlueAudit}\to\\
&\mathsf{Commit}\to\mathsf{TraceCompile}\to\mathsf{IndexUpdate}.
\end{aligned}
}
$$

Change path：

$$
\boxed{
\mathsf{Invalidate}
\to
\mathsf{DirtyClosure}
\to
\mathsf{SupportRollback}
\to
\mathsf{IncrementalReplay}.
}
$$
