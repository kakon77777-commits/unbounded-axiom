# CSM Paper 09 — NS_GSM: Canonical Domain Model and Ingestion Specification

## NS_GSM：Navier–Stokes 相對全域閉包空間的 Canonical Domain Model 與資料匯入規格

**Series:** Closure-Space Mathematics (CSM)  
**Paper:** 09  
**Canonical code:** `NS_GSM`  
**Version:** v0.1  
**Date:** 2026-08-27  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** zh-TW  
**Status:** Domain Instantiation / Canonical Graph & Ingestion Specification  
**Canonical source:** UTF-8 Markdown  
**Canonical math delimiters:** inline ` $...$ `; display `$$...$$`

> **命名註記**：`NS_GSM` 為本系列的 canonical project / framework code。本文件不擅自替 `GSM` 補定未由發起者指定的英文展開；全文只使用 `NS_GSM` 作正式代碼，並以「Navier–Stokes 相對全域閉包空間」描述其功能地位。

---

## 摘要

CSM Paper 00–08 已建立一套可區分 domain、route、obstruction、survivor、frontier、certificate、debt、reopening、projection、transfer、transaction 與 deterministic replay 的閉包空間數學論。本文停止繼續擴張抽象母理論，第一次將 CSM 完整落到 Navier–Stokes 長程研究體系中，建立：

$$
\boxed{
\textbf{NS\_GSM v0.1}.
}
$$

NS_GSM 的目標不是把既有研究論文做成知識圖譜，也不是用 paper 數量替代 theorem proof。它的第一目標是：

$$
\boxed{
\text{把過去所有已證、條件成立、封路、NO-GO、survivor、STOP、reopening 與未償 proof debt}
}
$$

重新編譯成一個 typed、quotient-aware、versioned、reopenable 的 **observed-relative closure graph**。

本文首先固定三個不得塌縮的 Navier–Stokes domain：

$$
\boxed{
\mathfrak N_{\rm C},
\qquad
\mathfrak N_{\rm G}^{\Sigma},
\qquad
\mathfrak N_{\rm P}.
}
$$

其中：

- $\mathfrak N_{\rm C}$：formal / Clay-facing mathematical NS domain；
- $\mathfrak N_{\rm G}^{\Sigma}$：由明確 signature $\Sigma$ 指定的 generalized NS-like equation family；
- $\mathfrak N_{\rm P}$：physical realization / model-to-world domain。

因此：

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm G}^{\Sigma})
}
$$

以及：

$$
\boxed{
\operatorname{Prove}(\mathfrak N_{\rm C})
\not\Rightarrow
\operatorname{Prove}(\mathfrak N_{\rm P}).
}
$$

本文接著建立 NS_GSM 的 series ontology。第一版正式承認的主要內部系列包括：

- ETN–X Integration；
- C1 / C2；
- C3–C6；
- RFP；
- MORP；
- X72；
- DCRP；
- FCBP；
- Proof Asset Map；
- theorem / symbolic / numerical validation scripts。

這些系列不是平面列表，而是不同研究階段與不同 representation / obstruction program 的 typed subgraphs。ETN–X 母架構提供 `Blowup → UV Escape → X-Legal UV Chain → Finite Obstruction` 的母路徑；RFP 對 source-traceability、finite ancestry、carrier / source debt 展開；MORP 將 minimal obstruction 壓向 ancient / escape / splitting kernel；DCRP 再對 diffuse carrier / adjoint ray / Riesz self-consistency / viscosity-matched survivor 做更深 rigidity；X72 則提供大量 route experiment、detector、continuous-response、commutator、lock、recurrence 與 bridge states。

本文正式定義 NS_GSM 的六大 canonical mathematical node families：

1. `TARGET`
2. `CLAIM`
3. `ROUTE`
4. `OBSTRUCTION`
5. `SURVIVOR`
6. `FRONTIER`

以及支撐層：

- `ASSUMPTION`
- `BRIDGE`
- `CERTIFICATE`
- `DEBT`
- `REPRESENTATION`
- `SERIES`
- `ARTIFACT`
- `VALIDATION`

本文特別禁止把原始文件中的：

`CLOSED / OPEN / NO-GO / SURVIVOR / STOP / CONDITIONAL`

直接匯入 native status。它們只能先進 Candidate Layer。只有經過：

$$
\boxed{
\mathsf{Ingest}
\to
\mathsf{Extract}
\to
\mathsf{Normalize}
\to
\mathsf{Validate}
\to
\mathsf{ApplyClosure}
\to
\mathsf{Rebuild}
\to
\mathsf{Snapshot}
}
$$

後，才能形成 native NS_GSM state。

本文最後定義 v0.1 seed corpus：ETN–X Integration、C1、C2、C6-Q、DCRP103、DCRP104、DCRP105。這七個節點橫跨 foundational reduction、route architecture、ancient/escape frontier、local ray classification、nonlocal self-consistency、NO-GO、survivor compression 與 vanishing-viscosity STOP，足以測試 NS_GSM 的第一個閉環。

---

# 1. NS_GSM 的定位

NS_GSM 不是：

- 新的 Navier–Stokes 方程；
- 對 Clay 問題的證明；
- 物理 Navier–Stokes 的統一理論；
- paper similarity graph；
- embedding cluster；
- 自動 theorem truth classifier。

NS_GSM 是：

$$
\boxed{
\text{Navier–Stokes long-horizon research as a typed relative-global closure space}.
}
$$

---

# 2. Canonical Root Object

定義根物件：

```yaml
ns_gsm:
  id: ns_gsm:root
  version: v0.1
  closure_scope: observed-relative
  theorem_authority: none_by_default
```

其存在不表示 NS 已被 route-complete。

---

# 3. 三域根節點

$$
\boxed{
D_{\rm NS}
=
\{
\mathfrak N_{\rm C},
\mathfrak N_{\rm G}^{\Sigma},
\mathfrak N_{\rm P}
\}.
}
$$

---

# 4. Formal / Clay-Facing Domain

$$
\boxed{
\mathfrak N_{\rm C}
}
$$

指固定方程、dimension、data / solution / regularity scope 下的 formal NS mathematical target family。

NS_GSM v0.1 不把所有研究稿的 informal `global NS` 自動對齊到同一 formal statement；每個 claim 必有 scope record。

---

# 5. Generalized NS-Like Domain

$$
\boxed{
\mathfrak N_{\rm G}^{\Sigma}
}
$$

只有在 signature $\Sigma$ 明確時才存在。

 $\Sigma$ 至少可包含：

- evolution type；
- incompressibility / constraint；
- nonlinear interaction；
- dissipation；
- pressure / projection；
- geometry；
- boundary；
- forcing；
- parameter family。

---

# 6. Physical Realization Domain

$$
\boxed{
\mathfrak N_{\rm P}
}
$$

包含 model-to-world bridge obligations：

- physical adequacy；
- parameter identification；
- measurement mapping；
- operating regime；
- scale validity；
- omitted physics。

---

# 7. Three-Domain Firewall

$$
\boxed{
\mathfrak N_{\rm C}
\neq
\mathfrak N_{\rm G}^{\Sigma}
\neq
\mathfrak N_{\rm P}.
}
$$

同一 `NS` 名稱不構成 closure-transfer certificate。

---

# 8. Root Formal Research Architecture

ETN–X foundational architecture 的 canonical compile target：

$$
\boxed{
\mathrm{Blowup}
\Longrightarrow
\mathrm{Critical\ UV\ Escape}.
}
$$

再研究：

$$
\boxed{
\mathrm{Critical\ UV\ Escape}
\stackrel{?}{\Longrightarrow}
\mathrm{XLegalUVChain}.
}
$$

最後研究：

$$
\boxed{
\mathrm{XLegalUVChain}
\stackrel{?}{\Longrightarrow}
\mathrm{FiniteObstruction}.
}
$$

---

# 9. C1 Canonical Meaning

$$
\boxed{
\mathrm{C1}:
\mathrm{Blowup}
\Rightarrow
\mathrm{XLegalUVChain}.
}
$$

在 NS_GSM 中：

```text
C1 = proof obligation / route necessity target
```

不是 definition truth。

---

# 10. C2 Canonical Meaning

$$
\boxed{
\mathrm{C2}:
\neg
\mathrm{XLegalUVChain}
\quad
\text{for the declared formal scope}.
}
$$

在 NS_GSM 中：

```text
C2 = finite-obstruction / chain-exclusion target family
```

---

# 11. C1 + C2 Parent Bridge

只有當 C1 與 C2 都具有 theorem-level cert，且 scope 一致時，才允許 parent bridge：

$$
\mathrm{Blowup}
\Rightarrow
\mathrm{XLegalUVChain},
$$

$$
\neg\mathrm{XLegalUVChain}
$$

推出：

$$
\neg\mathrm{Blowup}.
$$

---

# 12. Foundational Separation

True ETN 在 NS_GSM 中首先編譯為：

```text
representation / global tension geometry
```

X Integration 首先編譯為：

```text
formation-legality / provenance calculus
```

兩者不直接獲得 PDE theorem authority。

---

# 13. NS_GSM Series Ontology

第一版 major series：

$$
\boxed{
\mathcal S_{\rm NS}
=
\{
\mathrm{ETNX},
\mathrm{C1C2},
\mathrm{C3C6},
\mathrm{RFP},
\mathrm{MORP},
\mathrm{X72},
\mathrm{DCRP},
\mathrm{FCBP},
\mathrm{PAM}
\}.
}
$$

---

# 14. ETN–X Integration

角色：

- foundational representation；
- root route decomposition；
- guard vocabulary；
- UV chain definition；
- parent bridge obligations。

---

# 15. C1 / C2

角色：

- chain necessity；
- finite obstruction；
- first parent-level architecture。

---

# 16. C3–C6

角色：

- cross-scale coupling；
- rigidity；
- carrier / geometry / ancient-profile reductions；
- local/global obstruction refinement；
- survivor compression。

不假設每個 C-series `CLOSED` 等於 Clay target closed。

---

# 17. RFP

RFP canonical role：

```text
singularity-formation ancestry /
source-traceable multiscale chain /
finite branching /
carrier-depth /
source-stock /
memory and bridge debt
```

RFP route 可建立 finite ancestry / infinite path 等 graph assets，但 full NS conclusion 仍必回到 exact NS Duhamel / source-stock quantitative bridge。

---

# 18. MORP

MORP canonical role：

```text
minimal obstruction rigidity /
equality manifold /
ancient kernel /
escape kernel /
zero-tax splitting /
rigidity cuts
```

MORP 的價值大量屬於：

$$
\boxed{
\text{frontier compression}
}
$$

而不是 parent theorem completion。

---

# 19. X72

X72 canonical role：

- proof-route experiments；
- detector families；
- continuous / discrete / hybrid representation experiments；
- pressure-response defects；
- commutator；
- locking；
- Kelvin / TR / X recurrence；
- branch and STOP generation。

每一 round 先編譯為 route experiment，不因 round number 增加 theorem authority。

---

# 20. DCRP

DCRP canonical role：

```text
diffuse-carrier rigidity /
adjoint eigen-lock /
tensor-ray classification /
Riesz self-consistency /
vanishing-viscosity survivor compression /
strict-DSS recurrence frontier
```

---

# 21. FCBP

FCBP canonical role：

```text
forest / budget / global obstruction aggregation candidate family
```

v0.1 不預設 Forest Coercive Budget 或 Finite Forest Obstruction 已證。

---

# 22. Proof Asset Map

Proof Asset Map 是：

$$
\boxed{
\text{artifact / dependency / theorem-asset index}
}
$$

不是 theorem-level closure graph 本身。

---

# 23. Canonical Node Families

NS_GSM native nodes：

```text
TARGET
CLAIM
ROUTE
OBSTRUCTION
SURVIVOR
FRONTIER
ASSUMPTION
BRIDGE
CERTIFICATE
DEBT
REPRESENTATION
SERIES
ARTIFACT
VALIDATION
```

---

# 24. TARGET

代表可明確 formalize 的 parent problem / subproblem。

例：

- formal NS regularity target；
- C1；
- C2；
- ancient kernel intersection；
- first-order solvability target。

---

# 25. CLAIM

單篇或跨篇可被獨立驗證的 mathematical statement。

---

# 26. ROUTE

從 assumptions / lemmas 到 target 的 proof / research route class。

---

# 27. OBSTRUCTION

使某 route / branch 無法成立或必支付額外代價的 typed object。

---

# 28. SURVIVOR

經過當前合法 obstruction propagation 後仍未被排除的 route class。

$$
\boxed{
\mathsf{SURVIVOR}
\neq
\mathsf{PROVEN}.
}
$$

---

# 29. FRONTIER

當前仍需研究的最小 active obligation。

`STOP-*` 通常先編譯為 FrontierCandidate。

---

# 30. ASSUMPTION

所有 theorem / obstruction 的作用條件。

---

# 31. BRIDGE

跨：

- series；
- representation；
- domain；
- scale；
- local/global；
- prelimit/limit；

的合法 transfer object。

---

# 32. CERTIFICATE

支援 theorem-level mutation的 proof-carrying evidence。

---

# 33. DEBT

未償 proof obligation。

---

# 34. REPRESENTATION

例如：

- Fourier / dyadic；
- ETN state；
- X-legal chain；
- strain / vorticity；
- adjoint ray；
- Riesz symbol；
- DSS / ancient profile；
- graph carrier。

---

# 35. ARTIFACT

論文、checkpoint、script、proof log、external theorem anchor。

---

# 36. VALIDATION

symbolic / numerical / theorem-prover / independent audit evidence。

Validation 不自動等於 theorem proof，authority 由 cert type 決定。

---

# 37. Canonical Edge Families

```text
IMPLIES
DEPENDS_ON
ASSUMES
REFINES
GENERALIZES
SPECIALIZES
BLOCKS
REFUTES
SURVIVES
REDUCES_TO
SPLITS_INTO
COMPRESSES_TO
BRIDGES_TO
TRANSFER_CANDIDATE
CERTIFIED_BY
VALIDATED_BY
SUPERSEDES
REOPENS
NEXT_FRONTIER
```

---

# 38. REDUCES_TO

例如：

$$
\mathsf K_{\rm local}
\Longrightarrow
\{
\mathsf K_{\rm coax},
\mathsf K_{\rm sh}^{12},
\mathsf K_{\rm sh}^{13},
\mathsf K_{\rm sh}^{23},
\mathsf K_{\rm axi}
\}.
$$

這是 branch decomposition / classification，不是 parent refutation。

---

# 39. COMPRESSES_TO

如果多個 branch 被排除後只剩：

$$
S_1\vee\cdots\vee S_m,
$$

建立：

```text
COMPRESSES_TO
```

而不是 `PROVES`.

---

# 40. DCRP103 Canonical Compile

DCRP103 的 local ray classification 編譯為：

```text
ROUTE/CLASSIFICATION:
  three simple-strain shear rays
  two coaxial rays
  axisymmetric degeneracy structure
```

其 five-ray spectrum 是局部 algebraic asset。

---

# 41. DCRP104 Canonical Compile

DCRP104 加入：

$$
r=\mathcal T_0^\ast\Phi
$$

的 nonlocal self-consistency。

其 canonical graph effect：

- coaxial frozen $L^2$ branch → obstruction / exclusion；
- simple-shear branches → survivors；
- axisymmetric polarization → survivor family。

---

# 42. DCRP104 Nonclaim Preservation

DCRP104 明確不應編譯成：

```text
Navier-Stokes regularity CLOSED
```

而只對其 declared frozen / self-consistency branches作用。

---

# 43. DCRP105 Canonical Compile

DCRP105 的關鍵 graph effect：

```text
positive-viscosity exact frozen no-go
  DOES NOT transfer uniformly to epsilon -> 0
```

因此舊 closure 必限縮。

---

# 44. Viscosity-Matched Survivor

DCRP105 survivor：

$$
\boxed{
\mathsf C_{\rm vm\mbox{-}shear/pol}
}
$$

編譯為：

```text
SURVIVOR
  type: prelimit shear/polarization
  residual_scale: O(epsilon)
  frontier: first-order solvability / spectral drift
```

---

# 45. DCRP105 STOP

`STOP-D105` canonical frontier：

$$
\boxed{
\text{First-Order Vanishing-Viscosity Solvability / Spectral-Drift Gap}.
}
$$

---

# 46. DCRP106 Candidate

DCRP105 文件所列 next step：

```text
First-Order Fredholm /
Radial Spectral Narrowing /
Coefficient-Eigenframe Drift
```

在 v0.1 中只是 NEXT_FRONTIER candidate，除非存在後續 artifact。

---

# 47. MORP Canonical Kernel Classes

MORP 已將部分 equality-manifold frontier 壓成：

$$
\boxed{
\mathsf{A\mbox{-}KERNEL}
\vee
\mathsf{E\mbox{-}KERNEL}
\vee
\mathsf{S\mbox{-}KERNEL}.
}
$$

---

# 48. A-KERNEL

```text
ancient states outside currently excluded Liouville subclasses
```

---

# 49. E-KERNEL

```text
escape-only trace / scale / spatial / transition carriers
```

---

# 50. S-KERNEL

```text
zero-tax splitting supported on surviving A/E components
```

---

# 51. MORP Status Discipline

MORP 中：

- 某些 local-energy / defect exclusion = PROVED；
- selected Liouville cuts = EXTERNAL/CONDITIONAL；
- general ancient kernel = OPEN；
- escape kernel = OPEN；
- NS regularity = NOT PROVED。

NS_GSM 必逐項拆開，不能把整篇檔案給單一 status。

---

# 52. RFP Canonical Branches

RFP v0.1 taxonomy：

```text
UV first passage
source debt
dual witness
carrier escape
spatial tube
pressure-compatible localization
finite branching
infinite ancestry
inter-edge bridge
source-stock persistence
plateau / memory-depth / time-resolution debt
```

---

# 53. RFP Full-Conclusion Firewall

RFP graph theorem 即使建立 finite branching / infinite path，仍不能直接升格 full NS conclusion，除非 exact Duhamel / source-stock quantitative bridge 得證。

---

# 54. X72 STOP Semantics

X72 的：

```text
STOP-Cxx
```

一律先編譯：

```text
FRONTIER_CANDIDATE
```

其意義是：

> 此 route 在目前 representation / assumptions 下被壓到某一具名 gap。

不是 theorem refutation。

---

# 55. X72 Next Semantics

`Next = ...` 編譯：

```text
NEXT_FRONTIER
```

而不是 implied theorem dependency。

---

# 56. X72 Proof-Route Experiment

若文件 status 為：

```text
Proof-Route Experiment
```

則 artifact authority 預設：

```text
RESEARCH
```

其內部 individual theorem 再另行驗證。

---

# 57. Cross-Series Bridge

NS_GSM 不因文件彼此引用就自動建立 theorem bridge。

依賴引用：

```text
DEPENDS_ON
```

與數學 transfer：

```text
BRIDGES_TO
```

必分開。

---

# 58. Cross-Series Quotient

例如：

```text
carrier escape
```

只有在 target、scope、assumptions、mechanism、representation 對齊後，才可：

$$
O_1\sim_{\rm obs}O_2.
$$

---

# 59. Same Label Firewall

$$
\boxed{
\text{same label}
\not\Rightarrow
\text{same obstruction}.
}
$$

---

# 60. Same Equation Firewall

即使兩篇都研究 formal NS：

$$
\boxed{
\text{same PDE}
\not\Rightarrow
\text{same route scope}.
}
$$

---

# 61. Artifact Ingestion Layer

每個 source artifact 先建立：

```yaml
artifact:
  artifact_id:
  title:
  series:
  date:
  version:
  source_ref:
  source_hash:
  canonicality:
  parser_version:
```

---

# 62. Canonicality

`canonicality`：

```text
CANONICAL
CHECKPOINT
HANDOFF
DERIVED
VALIDATION
EXTERNAL_ANCHOR
DUPLICATE
SUPERSEDED
```

---

# 63. Duplicate Files

同名重複檔案不得自動算多個 proof objects。

先以：

- source hash；
- content identity；
- lineage；
- version；

做 artifact quotient。

---

# 64. Claim Extraction Record

```yaml
claim_candidate:
  candidate_id:
  artifact_id:
  statement:
  statement_span:
  claim_type:
  explicit_label:
  scope:
  assumptions: []
  dependencies: []
  evidence_refs: []
```

---

# 65. Explicit Label Is Not Status

```yaml
explicit_label: "NO-GO"
native_status: null
```

直到 validation。

---

# 66. Candidate Label Mapping

```text
CLOSED       -> StatusCandidate
OPEN         -> OpenCandidate
NO-GO        -> ObstructionCandidate
SURVIVOR     -> SurvivorCandidate
STOP-*       -> FrontierCandidate
CONDITIONAL  -> ConditionalCandidate
PROVED       -> ProofClaimCandidate
```

---

# 67. Validation Stage

最低檢查：

1. statement fidelity；
2. target identity；
3. assumptions；
4. scope；
5. theorem/proof evidence；
6. internal dependencies；
7. external theorem status；
8. representation；
9. version；
10. nonclaims。

---

# 68. Nonclaim Extraction

NS_GSM 將：

```text
What is NOT proved
Non-claim
本文不主張
```

視為第一級 ingestion data。

---

# 69. Why Nonclaims Matter

因為它們直接建立：

```text
authority boundary
```

並阻止 downstream closure inflation。

---

# 70. Validation Script Role

Python / symbolic / numerical checks 可建立：

```text
VALIDATED_BY
```

但預設 certificate authority：

```text
COMPUTATIONAL_AUDIT
```

不是全文 theorem proof。

---

# 71. External Theorem Anchor

外部 theorem 建：

```yaml
external_anchor:
  citation:
  imported_claim:
  exact_scope:
  use_in_ns_gsm:
  transfer_limit:
```

---

# 72. External Result Firewall

外部 paper 只對明確 imported theorem 範圍提供 authority。

不得：

```text
paper cited -> whole NS_GSM branch closed
```

---

# 73. Seed Corpus v0.1

第一批七個 canonical seed：

```text
S00 ETN-X Integration
S01 C1
S02 C2
S03 C6-Q
S04 DCRP103 / X72-R86
S05 DCRP104 / X72-R87
S06 DCRP105 / X72-R88
```

---

# 74. Why ETN–X Is Seed

它提供：

- root route；
- UV escape；
- X-legal chain；
- C1；
- C2；
- explicit nonclaim。

---

# 75. Why C1 / C2 Are Seed

它們建立 parent route architecture 與第一個 branch-completeness obligation。

---

# 76. Why C6-Q Is Seed

它代表 C-series 深層 frontier 已經從早期 scalar/budget 問題走到 ancient / local-growth / carrier / order-geometry 類 survivor structure。

v0.1 只將其作 canonical C-series frontier seed，不從檔名或摘要推導比 source 更強的 theorem status。

---

# 77. Why DCRP103 Is Seed

它展示：

```text
classification / branch decomposition
```

如何在 NS_GSM 中變成 typed route classes。

---

# 78. Why DCRP104 Is Seed

它展示：

```text
one branch excluded
+
other branches survive
```

不能被壓成單一 `NO-GO`.

---

# 79. Why DCRP105 Is Seed

它展示：

- previous NO-GO nonuniform；
- closure downgrade；
- survivor compression；
- STOP frontier；
- explicit `not proved` list。

它是 reopening / status correction 的理想測試。

---

# 80. Seed Expected Graph

第一版 seed graph 應至少生成：

```text
1 root domain bundle
3 domain nodes
7 artifact nodes
>= 1 root target
C1 target
C2 target
UV escape claim
X-legal chain object
D103 ray branch family
D104 coaxial obstruction
D104 shear survivors
D104 axisymmetric survivor
D105 viscosity-matched survivor
D105 first-order frontier
certificate/debt/nonclaim nodes
```

實際數量由 claim extraction 決定，不硬編固定數字。

---

# 81. Native Status Set

NS_GSM 使用：

```text
UNVERIFIED
UNKNOWN
OPEN
CONDITIONAL
BLOCKED
CLOSED_POSITIVE
CLOSED_NEGATIVE
SURVIVOR
STALE
REOPENED
SUPERSEDED
```

---

# 82. SURVIVOR as Orthogonal Tag

更嚴格 runtime 可把 `SURVIVOR` 當 route-role tag，而 base closure status 仍是 `OPEN`。

v0.1 schema 允許：

```yaml
status: OPEN
role_tags: [SURVIVOR]
```

以避免 status lattice 混亂。

---

# 83. NO-GO as Object, Not Status

`NO-GO` 最好編譯為：

```text
OBSTRUCTION object
```

而不是 node status。

---

# 84. STOP as Frontier Object

`STOP-*` 最好編譯為：

```text
FRONTIER object
```

而不是 `FAILED`.

---

# 85. CLOSED as Ambiguous Source Label

原始 `CLOSED` 必判斷究竟是：

- claim proved；
- branch excluded；
- route blocked；
- local subproblem resolved；
- documentation closure。

---

# 86. Series Status vs Claim Status

整篇文件：

```text
Status: proof-development checkpoint
```

與內部 theorem：

```text
Theorem X: proved
```

必拆開。

---

# 87. Dependency Graph

Artifact dependency：

$$
A_i
\to
A_j
$$

只表示 lineage。

Claim dependency：

$$
Q_i
\Rightarrow
Q_j
$$

需要 theorem semantics。

---

# 88. Lineage Edge

```text
PREDECESSOR_OF
```

不具有 implication authority。

---

# 89. Supersession

例如新 round 修正舊 NO-GO scope：

```text
SUPERSEDES
```

並觸發 stale/reopen audit。

---

# 90. Reopening Test

D104 positive-viscosity exact frozen no-go 若在 D105 被證明對 vanishing viscosity 不 uniform：

NS_GSM 應：

1. 保留 D104 cert；
2. 限縮其 scope；
3. 標記舊 broader transfer stale；
4. 建立 D105 survivor；
5. 重建 frontier。

---

# 91. Frontier Engine v0.1

對 formal target：

$$
Q_{\rm NS,C}
$$

先輸出：

$$
\boxed{
\partial_{\rm obs}^{\ast}(Q_{\rm NS,C})
}
$$

不是 admissible-complete frontier。

---

# 92. Observed-Relative Guard

所有 v0.1 UI / export 必顯示：

```text
Observed-relative.
Not a complete enumeration of mathematical proof space.
```

---

# 93. Route Completeness Debt

根 target 預設：

```text
route_completeness: OPEN_DEBT
```

---

# 94. Representation Completeness Debt

因 NS_GSM 收錄的 representation 仍有限：

```text
representation_completeness: OPEN_DEBT
```

---

# 95. Cross-Series Equivalence Debt

大量同義／近義 obstruction 尚未 theorem-audited：

```text
obstruction_quotient: PARTIAL
```

---

# 96. Domain Transfer Debt

formal → generalized / physical：

```text
OPEN by default
```

---

# 97. Exhaustion Level v0.1

根 formal NS target 預設最高只能：

$$
\boxed{
\mathsf{EXH}_1
}
$$

而且多半連 EXH1 都只能在某 local route family 上聲稱。

---

# 98. Local Exhaustion Record

例如某個 DCRP frozen coaxial branch：

```yaml
exhaustion:
  target: frozen_coaxial_branch
  level: branch-relative
  scope: declared_D104_scope
```

不能傳到 root NS target。

---

# 99. Frontier Compression Metric

NS_GSM 可計：

$$
\operatorname{FCR}
=
\frac{
|\mathcal R_{\rm before}^{\ast}|
-
|\mathcal R_{\rm after}^{\ast}|
}{
|\mathcal R_{\rm before}^{\ast}|
}.
$$

只作 operational diagnostic。

---

# 100. FCR Nonclaim

$$
\boxed{
\operatorname{FCR}\uparrow
\not\Rightarrow
\text{closer to proving NS}.
}
$$

---

# 101. Obstruction Centrality

可計：

$$
Z(O).
$$

高 centrality 表示值得優先研究，不表示 absolute necessity。

---

# 102. Survivor Concentration

若多系列 route 壓到少數 survivor class：

```text
SURVIVOR_CONFLUENCE
```

但需要 genealogy correction。

---

# 103. False Confluence Guard

同一母稿衍生出的多條 route 不得假裝 independent rediscovery。

---

# 104. Cross-Series Mapping Table v0.1

第一版 candidate mapping：

| Source | Candidate target | Relation |
|---|---|---|
| ETN–X | C1/C2 | foundational architecture |
| C3–C6 | RFP | ancestry / finite obstruction refinement |
| MORP | DCRP | minimal diffuse-carrier handoff |
| X72 | DCRP | detector / response / adjoint bridge |
| DCRP103 | DCRP104 | local classification → nonlocal self-consistency |
| DCRP104 | DCRP105 | exact positive-viscosity no-go → vanishing-viscosity audit |

所有 relation 初始都需分：

```text
LINEAGE
MATH_BRIDGE
TRANSFER
```

---

# 105. MORP → DCRP Handoff

MORP Cycle VII 把 surviving object 壓向：

```text
minimal diffuse carrier
```

並將下一 program 指向 DCRP。

NS_GSM 因此可建立：

```text
LINEAGE/HANDOFF
```

但 DCRP theorem 不自動回寫 MORP theorem authority。

---

# 106. DCRP103 → 104

建立：

```text
REDUCES_TO / REFINES
```

local algebraic ray classes 經 nonlocal Riesz self-consistency 再篩選。

---

# 107. DCRP104 → 105

建立：

```text
SCOPE_REVISION
```

D104 exact positive-viscosity frozen exclusion不能無證擴到 vanishing-viscosity uniform exclusion。

---

# 108. DCRP105 Frontier

建立：

```text
NEXT_FRONTIER:
first-order solvability / spectral drift
```

而不是：

```text
NS solved next round
```

---

# 109. Ingestion Order

v0.1 建議：

```text
Phase A: domain / target anchors
Phase B: foundational ETN-X / C1 / C2
Phase C: C6-Q
Phase D: DCRP103
Phase E: DCRP104
Phase F: DCRP105
Phase G: seed cross-link audit
Phase H: frontier snapshot
```

---

# 110. Expansion Order after Seed

Seed 通過後：

```text
1. C3-C6 full
2. RFP full
3. MORP full
4. X72 key checkpoints
5. DCRP full
6. FCBP
7. Proof Asset Map reconciliation
8. validation scripts
```

---

# 111. Why Not Ingest Everything at Once

因為 v0.1 首要驗證的是：

- status parsing；
- quotient；
- scope；
- reopening；
- lineage vs implication；
- cross-series transfer；
- frontier rebuild。

先用 small heterogeneous seed 比全量 text dump 更容易抓 semantic bug。

---

# 112. Required Seed Assertions

runtime conformance 必確認：

1. ETN–X 不被標成 NS theorem；
2. C1/C2 保持 OPEN obligation；
3. D103 classification 不被標 parent proof；
4. D104 coaxial branch可局部 exclusion；
5. D104 shear/axisymmetric remain survivor；
6. D105 限縮 D104 uniformity；
7. D105 global regularity remains unproved；
8. D105 STOP 成 frontier；
9. source labels不直接控制 native status。

---

# 113. Required Seed Reopening Test

模擬：

```text
D104 broad inherited no-go
```

被 D105 新結果限縮後：

Expected：

```text
old broad closure -> STALE
narrow D104 closure -> VALID
D105 survivor -> OPEN/SURVIVOR
frontier -> REBUILT
```

---

# 114. Required Seed Projection Test

Overview view 可以只畫：

```text
ETN-X
  -> C1/C2
  -> C-series
  -> RFP/MORP
  -> X72/DCRP
  -> active frontier
```

但 authority：

```text
DISPLAY / RESEARCH
```

不能 PROOF。

---

# 115. Required Audit View

audit view 必保留：

- statement；
- assumptions；
- scope；
- status；
- cert；
- debt；
- source；
- version；
- predecessor；
- nonclaims。

---

# 116. Canonical ID Scheme

建議：

```text
ns_gsm:<domain>:<kind>:<stable-name>
```

例：

```text
ns_gsm:formal:target:c1-chain-necessity
ns_gsm:formal:obstruction:d104-frozen-coaxial
ns_gsm:formal:survivor:d105-vm-shear-pol
```

---

# 117. Series IDs

```text
ns_gsm:series:etnx
ns_gsm:series:c
ns_gsm:series:rfp
ns_gsm:series:morp
ns_gsm:series:x72
ns_gsm:series:dcrp
ns_gsm:series:fcbp
```

---

# 118. Artifact IDs

```text
ns_gsm:artifact:<series>:<canonical-slug>:<version>
```

---

# 119. Claim IDs

claim identity 不應依 section number alone。

建議用：

```text
semantic slug + source lineage
```

---

# 120. Obstruction Record

```yaml
obstruction:
  id:
  target_pattern:
  assumptions: []
  scope:
  representation:
  mechanism:
  strength:
  certificate_refs: []
  exceptions: []
  series:
  source_artifact:
  version:
```

---

# 121. Survivor Record

```yaml
survivor:
  id:
  route_class:
  parent_split:
  surviving_conditions: []
  excluded_siblings: []
  unresolved_debts: []
  next_frontier_ids: []
  version:
```

---

# 122. Frontier Record

```yaml
frontier:
  id:
  target_id:
  frontier_type:
  originating_routes: []
  unresolved_statement:
  required_bridge_ids: []
  debt_ids: []
  source_artifacts: []
  version:
```

---

# 123. Series Bridge Record

```yaml
series_bridge:
  id:
  source_series:
  target_series:
  source_objects: []
  target_objects: []
  relation_type:
  semantic_match:
  scope_match:
  assumption_match:
  transfer_certificate:
  debt_ids: []
  status:
```

---

# 124. Nonclaim Record

```yaml
nonclaim:
  id:
  source_artifact:
  forbidden_promotion:
  target_scope:
  reason:
  version:
```

---

# 125. Source Basis v0.1

Paper 09 v0.1 的 internal source basis 包括：

- `NS_ETN_XIntegration_Multiscale_NonCollapse_v0.1.md`
- `NS_RFP_05_WitnessPersistence_FiniteBranching_InfinitePath_v0.1.md`
- `NS_MORP_04_EqualityManifold_RigidityAudit_v0.1.md`
- `NS_MORP_CYCLE_VII_HANDOFF_v1.0.md`
- `NS_DCRP103_X72R86_AdjointEigenLock_FiveRayClassification_2026-08-20.md`
- `NS_DCRP104_X72R87_RieszSelfConsistency_ShearPolarization_2026-08-20.md`
- `NS_DCRP105_X72R88_VanishingViscosity_ShearTR_ResidualMatching_2026-08-20.md`
- X72 checkpoint material
- CSM Paper 00–08

本文只把來源中明示或可安全編譯的結構寫入 canonical model；沒有來源支持的 detailed C6-Q theorem list 不在本文件自行補寫。

---

# 126. Epistemic Firewall

$$
\boxed{
\text{artifact label}
\neq
\text{native status}
\neq
\text{root theorem status}.
}
$$

---

# 127. Mathematical Firewall

$$
\boxed{
\text{route excluded}
\neq
\text{claim refuted}.
}
$$

---

# 128. Series Firewall

$$
\boxed{
\text{series handoff}
\neq
\text{theorem implication}.
}
$$

---

# 129. Domain Firewall

$$
\boxed{
\text{formal NS}
\neq
\text{generalized NS-like}
\neq
\text{physical NS}.
}
$$

---

# 130. Runtime Firewall

$$
\boxed{
\text{candidate extraction}
\neq
\text{native theorem mutation}.
}
$$

---

# 131. v0.1 Definition of Done

NS_GSM v0.1 canonical domain model 完成，需滿足：

1. three domains fixed；
2. series ontology fixed；
3. node/edge taxonomy fixed；
4. seed corpus defined；
5. source-label parsing fixed；
6. status firewall fixed；
7. seed reopening test defined；
8. cross-series bridge schema defined；
9. observed-relative guard fixed；
10. runtime handoff schema available。

---

# 132. What Paper 09 Does Not Do

本文不：

- 執行完整 203+ artifact ingestion；
- 宣稱 route completeness；
- 宣稱 root frontier 完整；
- 建立 absolute NS proof-space；
- 解 D105 frontier；
- 提出 DCRP106 theorem；
- 宣稱任何 physical NS modification；
- 修改既有 theorem status。

---

# 133. Immediate Engineering Handoff

下一步不是再寫 abstract CSM paper。

下一步應建立：

$$
\boxed{
\textbf{NS\_GSM Seed Dataset v0.1}
}
$$

包含：

```text
domains.yaml
series.yaml
artifacts.yaml
claims.yaml
routes.yaml
obstructions.yaml
survivors.yaml
frontiers.yaml
bridges.yaml
debts.yaml
certificates.yaml
nonclaims.yaml
```

---

# 134. Seed Compiler Handoff

Reference Runtime 的 NS compiler 第一版只處理七個 seed artifacts。

成功標準：

```text
deterministic parse
+
candidate/native firewall
+
replay stable
+
expected statuses
+
frontier rebuild
```

---

# 135. Full-Corpus Handoff

seed 通過後，再開始完整：

$$
\boxed{
\text{NS historical corpus}
\to
\text{NS\_GSM native graph}.
}
$$

---

# 136. NS 方程「到底哪裡惹到我們」

它真正「惹到」這個研究計畫的地方不是方程本身。

而是它同時具有：

- 足夠大的 formal global target；
- 巨量局部 theorem / criterion；
- 多 representation；
- 多 scale；
- nonlocal pressure；
- nonlinear transport；
- dissipation；
- geometry；
- ancient-profile / blowup / compactness branches；
- 長期研究史；
- 大量彼此相似但不等價的 proof routes。

因此它非常適合作為：

$$
\boxed{
\text{Closure-Space Mathematics 的第一個大型壓力測試場}.
}
$$

---

# 137. 結論

NS_GSM v0.1 的核心不是再增加一條 Navier–Stokes proof route。

而是把過去所有 route 的命運第一次變成一個可以查詢的數學空間：

$$
\boxed{
\text{哪條被證成？}
}
$$

$$
\boxed{
\text{哪條只被 block？}
}
$$

$$
\boxed{
\text{哪個 NO-GO 只在局部 scope 有效？}
}
$$

$$
\boxed{
\text{哪個 survivor 是真正剩餘 branch？}
}
$$

$$
\boxed{
\text{哪個 STOP 是下一個 frontier？}
}
$$

$$
\boxed{
\text{哪個舊 closure 因新結果必須 reopen？}
}
$$

ETN–X 建立了最早的母路徑：

$$
\mathrm{Blowup}
\to
\mathrm{UV\ Escape}
\to
\mathrm{XLegalUVChain}
\to
\mathrm{FiniteObstruction}.
$$

後續 C-series、RFP、MORP、X72、DCRP 沒有簡單地「一直失敗」，而是在不斷：

$$
\boxed{
\text{split}
\to
\text{exclude}
\to
\text{compress}
\to
\text{survive}
\to
\text{reframe frontier}.
}
$$

NS_GSM 的任務就是把這些歷史從散落的 paper-state，重建成：

$$
\boxed{
\text{typed}
+
\text{scoped}
+
\text{certified}
+
\text{versioned}
+
\text{reopenable}
+
\text{relative-global}
}
$$

的 closure graph。

從這一篇開始，下一步不再只是「寫理論」，而是可以真正開始建第一個 NS_GSM dataset 與 graph runtime。

---

## 附錄 A — NS_GSM v0.1 核心不變量

1. `NS_GSM` 是 canonical code；
2. formal / generalized / physical 三域不得塌縮；
3. artifact label 不等於 native status；
4. NO-GO 是 obstruction object，不是 root status；
5. STOP 是 frontier object，不是 failure；
6. SURVIVOR 不等於 PROVEN；
7. CLOSED 必重新判定 closure level；
8. series lineage 不等於 theorem implication；
9. same terminology 不等於 same obstruction；
10. dependency citation 不等於 bridge certificate；
11. validation script 不自動等於 theorem proof；
12. nonclaims 必進 native audit data；
13. D104 no-go 不得無證 uniform transfer 到 vanishing viscosity；
14. D105 survivor 必保留 OPEN frontier；
15. v0.1 只聲稱 observed-relative graph。

---

## 附錄 B — Seed Corpus

| Seed | Artifact | Primary NS_GSM role |
|---|---|---|
| S00 | ETN–X Integration | root architecture |
| S01 | C1 | chain necessity target |
| S02 | C2 | finite obstruction target |
| S03 | C6-Q | C-series advanced frontier seed |
| S04 | DCRP103 / X72-R86 | local branch classification |
| S05 | DCRP104 / X72-R87 | nonlocal NO-GO + survivors |
| S06 | DCRP105 / X72-R88 | no-go scope correction + viscosity-matched survivor + STOP |

---

## 附錄 C — Next Artifact

$$
\boxed{
\textbf{NS\_GSM Seed Dataset v0.1}
}
$$

應直接作為 CSM Reference Runtime 的第一個 domain package。

---

**END OF CSM PAPER 09 / NS_GSM v0.1**
