# 空間域證明包圍論 III
## 多維覆蓋、Gap 與 Global Closure Certificate
### Spatial-Domain Proof Enclosure III: Multidimensional Coverage, Gaps, and Global Closure Certificates

**Version:** v0.1  
**Date:** 2026-08-14  
**Status:** foundational formalization / closure layer; not a universal complete proof calculus  
**Canonical source:** UTF-8 Markdown; canonical mathematics uses ` $...$ ` and `$$...$$` only.

---

## 摘要

Paper 01 將全域命題

$$
\forall d\in D,\;P(d)
$$

改寫成真實反例集

$$
\mathcal C=\{d\in D:\neg P(d)\}
$$

與 sound survivor envelope

$$
\mathcal C\subseteq\Omega_t
$$

的持續收縮；Paper 02 則研究表示

$$
\phi:D\to X
$$

何時不會在投影、商化或 abstraction 中靜默丟失 proof-relevant counterexample fibers。

本文處理下一個真正接近 proof completion 的問題：即使每一個 local theorem、每一條 route、每一個 representation certificate 都正確，仍不能自動推出 global proof。真正 closure 還需要證明 route family 完整覆蓋所有可能反例，boundary 沒有被 strict case split 漏掉，local certificates 仍可 replay；若結論依賴 local structures 的組合，還必須額外證明 overlap / cycle / gluing compatibility。

本文首先區分兩種 closure regime。若每個 chart 都被獨立證明 counterexample-free，則只需要

$$
\boxed{
\text{Cover Completeness}
+
\text{Local Refutations}
\Rightarrow
\text{Global Emptiness}.
}
$$

此時 chart overlaps 不需要額外 gluing。相反地，如果全域結論需要把 local invariant、local witness、local coordinates 或 local proof objects 組成一個 global object，則必須提供已證的 local-to-global law：

$$
\boxed{
\text{Local Structures}
+
\text{Overlap Compatibility}
+
\text{Proved Gluing Law}
\Rightarrow
\text{Global Structure}.
}
$$

本文建立 typed Gap Profile：route gap、branch gap、boundary gap、certificate gap、glue gap、dependency gap。這些 gap 位於不同數學空間，不能粗暴壓成單一 coverage ratio。量化 coverage 可以作 routing diagnostic，但不能取代 exact cover certificate。

本文提出 Global Closure Certificate：

$$
\boxed{
\mathsf{GCC}
=
\langle
Master,
Atlas,
CoverCert,
LocalCerts,
BoundaryCert,
LiftCerts,
GlueMode,
GlueCert,
DepDAG,
Version,
Replay
\rangle.
}
$$

核心有限閉合定理為：若

$$
\mathcal C\subseteq\Omega,
$$

$$
\Omega\subseteq\bigcup_{i=1}^{m}U_i,
$$

且每個 chart 都有可驗證 local refutation

$$
\mathcal C\cap U_i=\varnothing,
$$

則

$$
\boxed{\mathcal C=\varnothing.}
$$

若只有部分 charts $J$ 被關閉，則仍有 exact residual enclosure：

$$
\boxed{
\mathcal C
\subseteq
\Omega\setminus\bigcup_{j\in J}U_j.
}
$$

因此 coverage audit 本身不只是研究管理，而是合法 survivor-space contraction。

---

## 關鍵詞

空間域證明包圍；coverage completeness；route atlas；global closure certificate；gap calculus；boundary ownership；local refutation；local-to-global gluing；sheaf condition；cycle consistency；proof certificate；branch coverage

---

# 1. 從局部正確到全域完整

Paper 01 建立：

$$
\boxed{\mathcal C\subseteq\Omega_t.}
$$

Paper 02 建立：representation compression 必須對 proof-relevant fibers 負責。

但即使兩者都成立，仍可能有一個最致命的錯誤：

> 所有已研究的 charts 都正確，但根本沒有證明這些 charts 的聯集涵蓋所有可能反例。

因此 SDPE 必須明確分離：

$$
\boxed{\text{Local Soundness}}
$$

與

$$
\boxed{\text{Global Coverage Soundness}.}
$$

前者問某一個 chart 是否真的沒有反例；後者問所有反例是否真的落入某個已處理 chart。

---

# 2. Fresh literature grounding

2026 年 LRAT-Catcher 的 cube-and-conquer composition 提供一個非常直接的 formal analogue：每個 cube leaf 都有 refutation certificate，但仍需要一個獨立 cover-completeness certificate 證明所有 assignments 都被 cubes 覆蓋，最後才能在 Lean 中合成 base formula 的 UNSAT theorem。

2026 年 proof-carrying covering-code formalization 則展示 coverage claim 可以作為可 replay 的 formal certificate，而不是只保存一個完成比例。

同年的 sheaf/Lean 工作展示：在已證為 sheaf 的特定 design presheaf 中，pairwise overlap compatibility 可導出 compatible local sections 的 unique global gluing。本文只把它當作 constructive-gluing regime 的現代例子，而不將「pairwise checks 足夠」提升成任意 proof atlas 的 universal law。

因此本文的定位不是發明 cover proof 或 sheaf gluing，而是建立一般 mathematical proof-route 的 closure contract。

---

# 3. Master Survivor Envelope 與 Route Atlas

假設已有：

$$
\boxed{
\mathcal C\subseteq\Omega\subseteq D.
}
$$

## Definition 3.1 — Route Chart

一個 route chart 記為

$$
\boxed{
\mathfrak U_i=(U_i,\phi_i,X_i,\Omega_i,\tau_i),
}
$$

其中 $U_i\subseteq\Omega$ 是 concrete scope， $\phi_i:U_i\to X_i$ 是 local representation， $\Omega_i\subseteq X_i$ 是 local survivor envelope， $\tau_i$ 是 route / representation / local-proof certificate。

## Definition 3.2 — Route Atlas

$$
\boxed{
\mathfrak A=\{\mathfrak U_i\}_{i\in I}.
}
$$

其 concrete route cover 為

$$
\boxed{
|\mathfrak A|:=\bigcup_{i\in I}U_i.
}
$$

## Definition 3.3 — Master Route Gap

$$
\boxed{
G_{\mathrm{route}}
:=
\Omega\setminus|\mathfrak A|.
}
$$

若 $G_{\mathrm{route}}\neq\varnothing$，至少有 master survivor state 沒有被任何 active chart 接管。

---

# 4. Cover completeness 是 theorem，不是視覺化

## Definition 4.1 — Envelope-Complete Atlas

若

$$
\boxed{
\Omega\subseteq\bigcup_{i\in I}U_i,
}
$$

則稱 atlas envelope-complete。

等價地：

$$
\boxed{G_{\mathrm{route}}=\varnothing.}
$$

## Definition 4.2 — Counterexample-Complete Atlas

較弱地，若有 theorem 直接證明

$$
\boxed{
\mathcal C\subseteq\bigcup_iU_i,
}
$$

則 atlas counterexample-complete。

這允許 master envelope 的某些區域沒有 chart，但前提是那些 gap 已有另一個 sound theorem 證明 counterexample-free。

## Principle 4.3 — Coverage must be proof-carrying

coverage heatmap、sampling、case count 或百分比不能取代：

$$
\boxed{
\mathcal C\subseteq\bigcup_iU_i
}
$$

或更強的：

$$
\boxed{
\Omega\subseteq\bigcup_iU_i.
}
$$

---

# 5. Cover–Refutation Closure

## Definition 5.1 — Local Counterexample-Free Certificate

對 chart $U_i$，若有可重播證明

$$
\boxed{
\mathcal C\cap U_i=\varnothing,
}
$$

則稱 $U_i$ locally closed。

若證明是在 local representation $X_i$ 中完成，則必須經 Paper 02 的 liftability obligation 回到 concrete scope $U_i$。

## Theorem 5.2 — Finite Cover–Refutation Closure Theorem

假設：

$$
\mathcal C\subseteq\Omega,
$$

$$
\Omega\subseteq\bigcup_{i=1}^{m}U_i,
$$

且對每個 $i$：

$$
\mathcal C\cap U_i=\varnothing.
$$

則：

$$
\boxed{
\mathcal C=\varnothing.
}
$$

### Proof

若存在 $c\in\mathcal C$，則 $c\in\Omega$。由 cover completeness，存在 $j$ 使 $c\in U_j$。因此 $c\in\mathcal C\cap U_j$，與 local certificate 矛盾。故 $\mathcal C=\varnothing$。

 $\square$

## Corollary 5.3 — Overlap Does Not Harm Refutation Closure

Theorem 5.2 不要求

$$
U_i\cap U_j=\varnothing.
$$

因此 charts 可以高度重疊。

$$
\boxed{
\text{cover}
\neq
\text{partition requirement}.
}
$$

對純 refutation closure，強迫 partition 反而可能產生額外 artificial boundaries。

---

# 6. Partial Closure 與 Residual Survivor

令 $J\subseteq I$ 為已 locally closed 的 charts。

## Theorem 6.1 — Residual Atlas Closure Theorem

若

$$
\mathcal C\subseteq\Omega
$$

且

$$
\mathcal C\cap U_j=\varnothing
\qquad
\forall j\in J,
$$

則：

$$
\boxed{
\mathcal C
\subseteq
\Omega\setminus\bigcup_{j\in J}U_j.
}
$$

### Proof

所有反例都在 $\Omega$，且不可能落入任何已 closed chart，因此只能留在其補集。

 $\square$

## Definition 6.2 — Atlas Residual Survivor

$$
\boxed{
\Omega^{\mathrm{res}}_J
:=
\Omega\setminus\bigcup_{j\in J}U_j.
}
$$

於是保持 sound invariant：

$$
\boxed{
\mathcal C\subseteq\Omega^{\mathrm{res}}_J.
}
$$

這使 coverage audit 成為真正的 survivor-envelope update，而不是單純的 project dashboard。

---

# 7. Typed Gap Calculus

不同未完成狀態位於不同型別空間，不能全部稱為「還有 gap」。

## Definition 7.1 — Route Gap

$$
\boxed{
G_D
:=
\Omega\setminus\bigcup_iU_i.
}
$$

## Definition 7.2 — Branch Gap

若 chart $U_i$ 宣稱被 sub-branches $B_{ia}$ 覆蓋，定義：

$$
\boxed{
G_{B,i}
:=
U_i\setminus\bigcup_{a\in A_i}B_{ia}.
}
$$

## Definition 7.3 — Boundary Gap

對 inequalities、singular strata、degenerate cases、limiting regimes 等 case split，尚未被任何 owner 接管的 boundary strata 記為

$$
\boxed{G_{\partial}.}
$$

## Definition 7.4 — Certificate Gap

$$
\boxed{
G_C
:=
\{i:\operatorname{LocalCert}_i\text{ absent / invalid / stale}\}.
}
$$

這是 index-space gap，而非 concrete-state subset。

## Definition 7.5 — Glue Gap

若當前 proof mode 需要 global structure，而某些 overlaps 缺乏 compatibility / gluing certificate，記為

$$
\boxed{G_G.}
$$

它存在於 overlap graph、nerve 或 transition system。

## Definition 7.6 — Replay / Dependency Gap

若 theorem dependency 已撤銷、scope 改變、representation version 不匹配或尚未 replay，記為

$$
\boxed{G_R.}
$$

## Definition 7.7 — Gap Profile

$$
\boxed{
\mathbf G
=
(G_D,G_B,G_{\partial},G_C,G_G,G_R).
}
$$

global closure 不是要求某個單一數值接近 $0$，而是要求與當前 closure mode 相關的 typed gaps 全部被正式清空或證明無害。

---

# 8. Boundary Ownership

典型 case split：

$$
f(x)<0
\quad\vee\quad
f(x)>0
$$

沒有覆蓋：

$$
f(x)=0.
$$

## Definition 8.1 — Boundary Ownership Certificate

對 boundary stratum $S$，至少要證明一項：

1. $S$ 被某既有 chart 包含；
2. $S$ 有獨立 local refutation；
3. $S$ 被證明與 $\mathcal C$ disjoint；
4. $S$ 被 refinement 成新的 chart。

## No-Go 8.2 — Strict-Dichotomy Closure Fallacy

由 $f<0$ 與 $f>0$ 兩個 branches 都 closed，不能推出 global closure，除非 equality locus 已被處理。

這項 no-go 特別重要，因為 measure-zero boundary 在實際 proof 中仍可能承載唯一 survivor family。

---

# 9. 多維 Coverage：比例與證書分層

## Definition 9.1 — Certificate Status Vector

$$
\boxed{
\boldsymbol\kappa
=
(
\kappa_D,
\kappa_B,
\kappa_{\partial},
\kappa_O,
\kappa_G,
\kappa_R
).
}
$$

每一項可取：

$$
\{\text{uncertified},\text{partial},\text{certified}\}.
$$

對應：domain cover、branch cover、boundary ownership、overlap audit、global gluing、replay/dependency integrity。

## Definition 9.2 — Quantitative Coverage Diagnostics

只有在有合法 finite denominator 或 measure model 時，才另外記錄：

$$
\boxed{
\boldsymbol\rho
=
(
\rho_D,
\rho_B,
\rho_{\partial},
\rho_O,
\rho_G,
\rho_R
).
}
$$

 $\boldsymbol\rho$ 是 routing diagnostic，不是 closure theorem。

## No-Go 9.3 — Scalar Coverage Completion

一般而言：

$$
\boxed{
\rho_D=1
\not\Rightarrow
\mathsf{GlobalClosed}.
}
$$

只有當 $\rho_D=1$ 本身就是 exact cover certificate 的另一種編碼時才例外。

## No-Go 9.4 — Overlap Double Counting

對 overlapping charts，不能把

$$
\sum_i\mu(U_i)
$$

直接當 union coverage。真正 relevant 的是

$$
\mu\left(\bigcup_iU_i\right)
$$

或其他 exact cover object。

---

# 10. Refutation Closure 與 Constructive Gluing 必須分開

$$
\boxed{
\text{Refutation Closure}
\neq
\text{Constructive Gluing}.
}
$$

## 10.1 Regime R — RefutationOnly

若每個 local result 都是

$$
\mathcal C\cap U_i=\varnothing,
$$

則只需要 cover completeness。overlaps 不需要額外一致性條件，前提是每個 local result 都能 soundly lift 回 concrete scope。

## 10.2 Regime G — ConstructiveGluing

若 local theorem 產生 local objects

$$
s_i\in\mathcal F(U_i)
$$

且 global proof 要求存在

$$
s\in\mathcal F(\Omega)
$$

滿足

$$
s|_{U_i}=s_i,
$$

則必須另外提供 overlap compatibility 與一個已證的 gluing law。

這個分流是 Paper 03 的核心：不對純 refutation 過度要求 sheaf machinery，也不對 constructive composition 過度樂觀。

---

# 11. 最小 Function-Gluing Theorem

## Theorem 11.1 — Compatible Local Functions Glue Uniquely

若

$$
\Omega=\bigcup_iU_i
$$

且每個 chart 上有函數

$$
s_i:U_i\to V,
$$

並滿足

$$
\boxed{
\forall x\in U_i\cap U_j,
\quad
s_i(x)=s_j(x),
}
$$

則存在唯一

$$
\boxed{s:\Omega\to V}
$$

使

$$
s|_{U_i}=s_i.
$$

### Proof

對任意 $x\in\Omega$，選一個包含 $x$ 的 chart $U_i$，定義 $s(x)=s_i(x)$。pairwise agreement 保證定義 independent of chart choice；唯一性由 chart cover 立即得到。

 $\square$

這是最簡單的 sheaf-of-functions gluing 模型。

---

# 12. Pairwise checks 的 universal no-go

一般 constraint family 中：

$$
\forall i\neq j,
\quad
H_i\cap H_j\neq\varnothing
$$

不推出

$$
\bigcap_iH_i\neq\varnothing.
$$

例如：

$$
H_1=\{1,2\},
\qquad
H_2=\{2,3\},
\qquad
H_3=\{1,3\}.
$$

每一對 intersection 非空，但

$$
\boxed{
H_1\cap H_2\cap H_3=\varnothing.
}
$$

## No-Go 12.1 — Pairwise-Consistency Fallacy

pairwise consistency 只有在已證 sheaf / Helly / convexity / descent / reconstruction / problem-specific gluing theorem 下，才有資格升格為 global consistency。

---

# 13. Proof Atlas 的 transition consistency

對多表示 route atlas，local coordinates 為

$$
\phi_i:U_i\to X_i.
$$

在 overlap

$$
U_{ij}:=U_i\cap U_j
$$

上，若需要互譯，定義 transition map：

$$
\tau_{ij}:\phi_i(U_{ij})\to\phi_j(U_{ij}).
$$

至少要求：

$$
\boxed{
\phi_j(d)=\tau_{ij}(\phi_i(d))
\quad
\forall d\in U_{ij}.
}
$$

若 transitions 可逆，還要求：

$$
\boxed{\tau_{ji}=\tau_{ij}^{-1}.}
$$

在 triple overlap 上，理想 cocycle condition 為：

$$
\boxed{
\tau_{ik}=\tau_{jk}\circ\tau_{ij}.
}
$$

若失敗，則同一 concrete state 沿不同 chart path 可能得到不同 representation state，形成 representation cycle gap。

---

# 14. Finite Transition Cycle Audit

令 overlap graph 為

$$
G=(V,E).
$$

在一個簡化的 fixed symmetry group $\Gamma$ 模型中，每個 oriented edge $(i,j)$ 帶 label

$$
g_{ij}\in\Gamma,
$$

且

$$
g_{ji}=g_{ij}^{-1}.
$$

## Proposition 14.1 — Fundamental-Cycle Audit Principle

取 connected graph 的 spanning tree $T$。若每一條 non-tree edge 所形成的 fundamental cycle，其 transition product 都為 identity，則存在 vertex potentials

$$
p_i\in\Gamma
$$

使

$$
\boxed{
 g_{ij}=p_i^{-1}p_j.
}
$$

因此任意 closed route cycle 的 transition product 都為 identity。

### Proof Sketch

固定 root。沿 tree 定義 $p_i$ 為 root 到 $i$ 的 transition product。對 non-tree edge $(i,j)$，fundamental-cycle identity 恰好推出

$$
g_{ij}=p_i^{-1}p_j.
$$

於是任意 path transition product telescopes 成 endpoint potentials；closed path endpoints 相同，故 product 為 identity。

 $\square$

此 proposition 是一個 runtime-friendly finite group model，不是一般 sheaf theorem。

---

# 15. Global Closure Certificate

## Definition 15.1 — GCC

Global Closure Certificate 定義為：

$$
\boxed{
\mathsf{GCC}
=
\langle
\mathsf{Problem},
\mathsf{Master},
\mathsf{Atlas},
\mathsf{CoverCert},
\mathsf{LocalCerts},
\mathsf{BoundaryCert},
\mathsf{LiftCerts},
\mathsf{GlueMode},
\mathsf{GlueCert},
\mathsf{DepDAG},
\mathsf{Version},
\mathsf{Replay}
\rangle.
}
$$

## 15.2 MasterCert

證明：

$$
\boxed{
\mathcal C\subseteq\Omega.
}
$$

## 15.3 CoverCert

優先證明：

$$
\boxed{
\Omega\subseteq\bigcup_iU_i.
}
$$

或至少直接證明：

$$
\boxed{
\mathcal C\subseteq\bigcup_iU_i.
}
$$

## 15.4 LocalCerts

對所有 charts：

$$
\boxed{
\mathcal C\cap U_i=\varnothing.
}
$$

## 15.5 BoundaryCert

證明所有 equality / singular / degenerate / limiting strata 已被某 branch 接管或直接排除。

## 15.6 LiftCerts

把 local representation-level result 合法 lift 回 concrete scope。

## 15.7 GlueMode

至少區分：

$$
\boxed{\mathsf{RefutationOnly}}
$$

與

$$
\boxed{\mathsf{ConstructiveGluing}.}
$$

前者不要求額外 gluing；後者要求。

## 15.8 DepDAG / Version / Replay

保證 closure 所依賴 theorem、representation、checker 與 scope 仍為 active version，並能重新 replay。

---

# 16. GCC Soundness

## Theorem 16.1 — Refutation-Mode GCC Soundness

若 finite GCC 通過：

1. MasterCert： $\mathcal C\subseteq\Omega$ ；
2. CoverCert： $\Omega\subseteq\bigcup_iU_i$ ；
3. 所有 LocalCert： $\mathcal C\cap U_i=\varnothing$ ；
4. 所有 local results 具有 sound LiftCert；
5. relevant boundaries 已被 ownership/refutation；
6. dependency、version、replay 均有效；

則：

$$
\boxed{\mathcal C=\varnothing.}
$$

因此原始全域命題成立。

### Proof

1--3 由 Theorem 5.2 已推出 $\mathcal C=\varnothing$。4--6 保證 1--3 的 proof artifacts 真正對原 concrete problem 有效，而不是 stale、mis-scoped 或 representation-only statements。

 $\square$

## Theorem 16.2 — Constructive-Mode GCC Soundness Schema

若 global conclusion 需要 global object $s$，則除了 RefutationMode obligations 外，必須另有 theorem：

$$
\boxed{
\operatorname{CompatibleLocal}(\{s_i\})
\Longrightarrow
\exists s\;\operatorname{Global}(s).
}
$$

以及 compatible-local certificate。

此 theorem 的具體來源可以是：

- sheaf gluing；
- invariant extension；
- cocycle trivialization；
- compactness / consistency theorem；
- convex / Helly-type theorem；
- algebraic descent；
- problem-specific reconstruction theorem。

所以 GCC 必須把 gluing requirement 變成 explicit mode，而不是默認所有 local objects 自動拼接。

---

# 17. Infinite Atlas 與 finite certificate extraction

## Theorem 17.1 — Compact Finite Refutation Subcover

假設：

1. $\Omega$ compact；
2. $\{U_i\}_{i\in I}$ 是 $\Omega$ 的 open cover；
3. 對每個 $i$：

$$
\mathcal C\cap U_i=\varnothing.
$$

則存在有限 indices $i_1,\ldots,i_m$ 使：

$$
\Omega\subseteq U_{i_1}\cup\cdots\cup U_{i_m},
$$

進而有限 local certificates 就足以推出：

$$
\boxed{\mathcal C=\varnothing.}
$$

### Proof

compactness 給 open cover 的 finite subcover，再套 Theorem 5.2。

 $\square$

這表示 discovery history 可以無限延展，但 final closure certificate 在適當結構下仍可能有限。

---

# 18. Closure Basis：最終證書不必包含完整探索歷史

歷史 theorem cuts 記為：

$$
T_1,T_2,\ldots,T_N.
$$

部分 theorem 可能被更強結果 subsume、只負責發現 route、或被 refinement 取代。

因此定義 closure basis：

$$
\boxed{
\mathcal B_{\mathrm{close}}
\subseteq
\{T_1,\ldots,T_N\}
}
$$

只要它仍能重建 Master、Cover、Local Closure、Boundary 與必要 Glue obligations。

這給出下一篇 Proof Trace Compilation 的明確 target：

$$
\boxed{
\text{full discovery history}
\to
\text{small replayable closure basis}.
}
$$

---

# 19. Gap Profile 直接生成 Research Frontier

若 GCC 未通過，不應只回傳「proof incomplete」，而應輸出：

$$
\boxed{
\mathbf G
=
(G_D,G_B,G_{\partial},G_C,G_G,G_R).
}
$$

不同 gap 對應不同 routing action：

- $G_D\neq\varnothing$：建立新 route/chart；
- $G_B\neq\varnothing$：補 branch classification；
- $G_{\partial}\neq\varnothing$：處理 equality/singular cases；
- $G_C\neq\varnothing$：證明或重播 local theorem；
- $G_G\neq\varnothing$：補 overlap/gluing；
- $G_R\neq\varnothing$：修 dependency/version/replay。

因此：

$$
\boxed{
\text{Global Closure Audit}
\Longrightarrow
\text{typed research routing signal}.
}
$$

coverage verification 不是只在研究末尾發生，而可以在每一輪改變下一刀的選擇。

---

# 20. 「空間很小」仍不等於 closure

即使：

$$
\Omega_0\supseteq\Omega_1\supseteq\cdots
$$

且

$$
\mu(\Omega_t)\to0,
$$

也可能：

$$
\bigcap_t\Omega_t\neq\varnothing.
$$

所以以下都不是 global closure certificate：

- coverage estimate $99.9999\%$ ；
- Monte-Carlo 找不到反例；
- survivor volume 很小；
- generic cases 全部關閉；
- boundary measure zero；
- pairwise overlap 抽樣全部通過。

真正 closure 必須回到 exact set cover、local refutation 與必要的 structural gluing。

---

# 21. No-Go Ledger

## No-Go 21.1 — Local Truth Implies Global Coverage

所有已研究 charts 都正確，不代表沒有漏掉 chart 外的反例域。

## No-Go 21.2 — Partition Requirement

Cover–Refutation Closure 不要求 charts disjoint。

## No-Go 21.3 — Scalar Coverage Fallacy

單一 coverage ratio 一般不能作 global closure certificate。

## No-Go 21.4 — Measure-Zero Gap Fallacy

$$
\mu(G)=0
$$

不推出

$$
G=\varnothing.
$$

## No-Go 21.5 — Pairwise Compatibility Is Universally Sufficient

一般 constraint systems 中 pairwise consistency 不推出 global consistency。

## No-Go 21.6 — Overlap Always Needs Gluing

若所有 charts 已獨立 refuted，overlap gluing 對 emptiness conclusion 不需要。

## No-Go 21.7 — Boundary Is Automatically Owned

strict inequalities / generic cases 可能漏 equality / singular strata。

## No-Go 21.8 — Coverage Percentages Can Be Added

overlapping chart coverage 不能直接相加。

## No-Go 21.9 — Certificate Presence Equals Validity

stale dependency、scope change、representation version mismatch 都可能使歷史 certificate 失效。

## No-Go 21.10 — Final Proof Must Preserve Every Discovery Step

closure basis 可以遠小於 discovery history，只要能完整 replay global closure。

---

# 22. Checker 與 Runtime 最小規格

Paper 03 companion checker 驗證有限模型中的：

1. residual closure；
2. full cover-refutation closure；
3. overlapping cover；
4. explicit route-gap witness；
5. equality-boundary omission；
6. overlap double-count no-go；
7. pairwise-global consistency no-go；
8. compatible local-function gluing；
9. GCC acceptance logic；
10. finite group-labeled transition cycle audit。

真正 runtime 最低應包含：

$$
\mathsf{CoverageAudit}
\to
\mathsf{GapExtractor}
\to
\mathsf{BoundaryAudit}
\to
\mathsf{LocalCertReplay}
\to
\mathsf{GlueAudit}
\to
\mathsf{ClosureComposer}.
$$

---

# 23. 前三篇形成的 closure stack

Paper 01：

$$
\boxed{
\mathcal C\subseteq\Omega_t
}
$$

與 theorem-guided survivor contraction。

Paper 02：

$$
\boxed{
\text{representation 不得丟失 proof-relevant counterexample fibers}.
}
$$

Paper 03：

$$
\boxed{
\text{local routes 必須有 global cover certificate，必要時還要有 gluing certificate}.
}
$$

因此：

$$
\boxed{
\begin{aligned}
&\text{Counterexample Master Envelope}\\
&\downarrow\\
&\text{Faithful Route Atlas}\\
&\downarrow\\
&\text{Certified Local Refutations / Structures}\\
&\downarrow\\
&\text{Cover + Boundary + Optional Glue Audit}\\
&\downarrow\\
&\text{Global Closure Certificate}.
\end{aligned}
}
$$

---

# 24. 下一篇：Proof Trace Compilation 與 Verification Amortization

前三篇先回答「怎樣才叫合法 closure」。下一步才真正進入我們最早那個速度問題：

> 大量 route、exclusion、certificate 已完成後，如何把歷史編譯成後續研究可直接調用的 pruning state，而不是每輪重新支付同一 verification/search 成本？

Paper 04 的核心鏈為：

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

Paper 03 現在已提供它需要維護的 target object：

$$
\boxed{\mathsf{GCC}.}
$$

---

# 25. Final Status

本文得到的核心分層是：

$$
\boxed{
\text{Local correctness}
\neq
\text{Global completeness}.
}
$$

對反例排除：

$$
\boxed{
\text{Cover}
+
\text{Local Refutations}
\Rightarrow
\text{Global Emptiness}.
}
$$

對局部結構組合：

$$
\boxed{
\text{Cover}
+
\text{Local Compatibility}
+
\text{Proved Gluing Law}
\Rightarrow
\text{Global Structure}.
}
$$

而所有未完成狀態被保留為：

$$
\boxed{
\mathbf G
=
(G_D,G_B,G_{\partial},G_C,G_G,G_R).
}
$$

只有 relevant gaps 真正被清空且 certificates 可 replay，SDPE runtime 才有資格 commit：

$$
\boxed{
\mathsf{GlobalClosed}=\mathrm{true}.
}
$$

這使空間域證明包圍從「一連串局部 theorem cuts」正式跨到「可檢查的全域 closure architecture」。

---

# References

1. Stefan Szeider, **LRAT-Catcher: Importing SAT Solver Certificates into Lean4 by Reflection**, arXiv:2607.00815, 2026.
2. Joshua Gibson, **Sheaves as a Means of Maintaining Consistency in Model-based Systems Engineering**, arXiv:2605.08609, 2026.
3. Andreas Florath, **Formal Foundations and Proof-Carrying Certificates for q-ary Covering Codes in Lean 4**, arXiv:2606.09600, 2026.
4. Andreas Florath, **A Lean-Certified Proof of $K_8(4,2)=23$**, arXiv:2606.16688, 2026.
5. Marijn J. H. Heule, Oliver Kullmann, Victor W. Marek, **Solving and Verifying the Boolean Pythagorean Triples Problem via Cube-and-Conquer**, arXiv:1605.00723, 2016.
6. Prior series artifact: **SDPE Paper 01 — Global Quantifiers, Counterexample Domains, and Verifiable Contraction**.
7. Prior series artifact: **SDPE Paper 02 — Route-Domain Completeness and Representation Non-Collapse**.
