# UGC/CUR External Academic Reconciliation — Round 2

**版本：** v0.1  
**日期：** 2026-08-26  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**狀態：** External academic reconciliation / novelty stress test  
**定位：** UGC/CUR 與 Unified Closure Theory（UCT）的外部學術對照第二輪；非最終新穎性聲明

---

## 摘要

Round 2 專門壓力測試三個高風險區：closure algebra / heterogeneous composition、epistemic accessibility / observation / action / ability，以及 provenance semiring / causal provenance / information accounting。

本輪結果實質縮小 UCT 可以安全宣稱的新穎性範圍。多閉包、閉包算子格、閉包交換與組合、以 distributive law 連接不同語義結構、異質 coalgebra composition、三重組合的 coherence、epistemic action、causal ability 與 epistemic ability 的區分，以及 provenance algebra，皆已有成熟 prior art。

因此 UCT 不應把 novelty 放在「存在多個閉包」、「bridge 需要條件」或「observer 不等於 actor」這些單獨命題。

目前較可辯護的新穎性候選縮為：

$$
\boxed{
\text{typed G/R/T synthesis}
+
\text{cross-type evidence and obstruction protocol}
+
\text{bridge coherence/debt accounting}
+
\text{first-cause / class-ultimate integration}
}
$$

其中：

$$
G=\text{Generation},
\qquad
R=\text{Reachability},
\qquad
T=\text{Transformation}.
$$

此結論仍是 **candidate novelty**，不是 publication-level novelty proof。

---

# 1. 多 Closure 與 Closure Algebra：已屬成熟 prior art

Kilpack 研究同一 algebraic lattice 上的 algebraic closure operators，並證明其形成 complete algebraic lattice；join 可由 closure operators 的有限 compositions 建構。

Hanai 更早研究同一 complete lattice 上的 commutative T-closure operators，並給出 composition 在何種條件下仍為 closure operator。

Tholen 進一步直接研究 closure operators 的 middle-interchange law。

因此：

$$
\boxed{
\text{multiple closure operators}
+
\text{closure algebra}
+
\text{commutation/interchange}
=
\text{established prior art}.
}
$$

UCT 若要使用「Unified Closure Theory」一名，必須明確指出它不是 ordinary closure-operator lattice 的重新發現。

---

# 2. UCT 與 homogeneous closure algebra 的真正差異

傳統 closure-operator 文獻主要考慮：

$$
\phi_i:L\to L
$$

其中所有 closure operators 共用同一 carrier $L$。

UCT 的 canonical objects 則不是三個同型 endomap：

$$
\operatorname{GenCl}_{D,T}
\left(
S\mid\mathfrak E^{\mathrm{gen}}
\right),
$$

$$
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t),
$$

$$
\operatorname{TransCl}_{D,T}(A\mid\Theta).
$$

其中 reachability 的 primitive 本身仍是 typed judgement；只有後續才聚合成 reachability envelope。

因此：

$$
\boxed{
\text{UCT triad}
\neq
\text{three homogeneous closure endomaps on one lattice}.
}
$$

---

# 3. Distributive Law：目前最接近 BridgeCert 的 prior art

König、Wolter、Kräuter（2023）直接研究 heterogeneously typed coalgebras。不同 local components 可以由不同 endofunctors 描述，再透過 interaction law 嵌入 distributive-law / bialgebraic framework，形成 compound behavioural system。

Zwart–Marsden 的 no-go theorems 顯示，兩種 monadic / algebraic structures 未必存在 distributive law。compatibility 不是免費結構。

Goy 對 iterated distributive laws 的研究進一步顯示，即使三個 monads 之間已有 pairwise distributive laws，仍需要額外 Yang–Baxter coherence 才能保證多重 composition 的一致性。

因此：

$$
\boxed{
\text{pairwise bridge legality}
\not\Rightarrow
\text{global bridge coherence}.
}
$$

UCT 應正式加入：

$$
\boxed{
\mathsf{BridgeCoherenceObligation}.
}
$$

同時加入：

$$
\boxed{
\mathsf{BRIDGE\_NO\_GO}
}
$$

用於保存「已取得結構性 bridge 不存在證明」的狀態。

---

# 4. BridgeCert 的 novelty 必須重新定位

Generic bridge / distributive law / interaction law 已有 prior art。

因此 UCT 的：

$$
\mathsf{BridgeCert}^{X\to Y}
$$

如果只表示「存在一個相容 mapping」，不具充分 novelty。

較可能保留為 candidate contribution 的，是它作為跨領域研究證書物件時的 richer payload：

$$
\mathsf{BridgeCert}
=
\left\langle
\text{scope},
\text{assumptions},
\text{source type},
\text{target type},
\text{witness},
\text{obstruction},
\text{version},
\text{debt},
\text{ledger binding}
\right\rangle.
$$

也就是把 categorical bridge、control-theoretic lifting、epistemic-action mapping、cross-layer channel 等不同 bridge 類型放進同一 evidence protocol，而不宣稱它們數學上是同一 natural transformation。

---

# 5. Reachability 與 Transformation：Non-Collapse 必須改成 scoped claim

Modal Kleene Algebra 與 Dynamic Logic 類框架會把 programs 表示為 relations / algebraic program objects，並從 program semantics 導出 forward / backward modal reachability。

因此某些 representation 下：

$$
\text{program transformation relation}
\Rightarrow
\text{reachability information}.
$$

所以 UCT 不宜寫成：

$$
\text{Reachability and Transformation can never collapse}.
$$

更穩健的 canonical 版本是：

$$
\boxed{
\text{No unconditional cross-type entailment is licensed in UCT canonical typing.}
}
$$

並正式區分：

$$
\boxed{
\mathsf{CanonicalNonCollapse}
\neq
\mathsf{RepresentationRelativeCollapse}.
}
$$

換言之：UCT 的 primitive 不預設相同；但特定 domain、encoding 或 theorem 可以建立可證的 collapse / embedding / equivalence。

---

# 6. Concurrent Dynamic Algebra：Composition 不能自由推

Furusawa–Struth 的 concurrent dynamic algebra 在 multirelational semantics 中顯示：sequential composition 一般不完全 associative；left distributivity 一般失敗；sequential 與 parallel composition 只有 weaker interaction laws；在 domain / antidomain 等特殊 elements 下才恢復較強 algebraic laws。

因此：

$$
\boxed{
\text{legal operators}
\not\Rightarrow
\text{free composability}.
}
$$

這與 UCT 的 $\mathsf{BridgeCompCert}$ 高度相容，但同樣不是其新穎性來源。

---

# 7. Control Theory：真正的 Reach-to-Transform Bridge 範例

Agrachev–Caponigro 與 Raginsky 的工作提供一個非常好的 domain-specific bridge。

point-wise controllability / accessibility 不等於可實現 arbitrary global diffeomorphism。

需要額外條件，例如 bracket-generating、identity neighborhood、isotopy to identity、fragmentation 與 uniform feedback construction。

因此可形式化為：

$$
\boxed{
\mathsf{Reach}
+
\mathsf{DomainBridgeConditions}
\Rightarrow
\mathsf{Transform}.
}
$$

這是 UCT `R2TBridge` 最好的外部 prototype 之一。

---

# 8. Epistemic Access / Causal Action 的 Non-Collapse 已有成熟 prior art

Duijf 等人的 STIT / epistemic ability 工作顯示，agent 可能實際存在能達成結果的 action，卻不知道哪個 action 能保證結果。因此：

$$
\boxed{
\text{Causal Ability}
\not\Rightarrow
\text{Epistemic Ability}.
}
$$

Baltag–Moss–Solecki 的 Dynamic Epistemic Logic 則明確把 state model 中的 epistemic accessibility、action / program model、以及 update product 分開。

因此：

$$
\boxed{
\text{epistemic accessibility}
\neq
\text{epistemic action}.
}
$$

這支持 UCT/OBRC capability modes 的 typed separation，但該 separation 本身不能主張為新穎。

---

# 9. Provenance Semiring：Ledger 的代數祖先非常成熟

Green–Tannen 的 provenance semiring framework 已經可以代數化 alternative derivations、joint derivations、input annotations 與 query transformation provenance。

因此 UCT Global Ledger 不應聲稱「把來源與生成責任代數化」本身全新。

---

# 10. Provenance Algebra 在加入新 Operations 時可能失效

Amsterdamer–Deutch–Tannen 研究 relational difference 時證明，原本在 positive relational algebra 很漂亮的 semiring framework 無法無條件延伸，同時保留所有期望 algebraic identities。

因此：

$$
\boxed{
\text{valid algebra under operator set }\mathcal O
\not\Rightarrow
\text{valid algebra under }\mathcal O\cup\{\Delta\}.
}
$$

UCT 應新增：

$$
\boxed{
\mathsf{AlgebraExtensionStability}.
}
$$

任何新增 negation、obstruction、meta-rewrite、bridge type 或 closure type，都必須重新檢查原本 composition law 是否仍成立。

---

# 11. Negation 甚至要求換 Provenance Algebra

Grädel–Tannen 對 full first-order logic with negation 的 provenance 研究需要 dual indeterminates：

$$
p,
\qquad
\bar p
$$

並採 quotient relation：

$$
p\bar p=0.
$$

當進一步進入 fixed-point logics，又需要 absorptive / fully continuous semirings 等更強條件。

因此：

$$
\boxed{
\text{provenance algebra is semantics-relative}.
}
$$

不存在「一個 unrestricted semiring 自動吃下所有新語義」。

---

# 12. Provenance Trace 不等於 Causal Completeness

Cheney–Acar–Ahmed 將 provenance trace 的要求分成 Consistency 與 Fidelity。Consistency 只保證 trace 與該次 execution 相符；Fidelity 更要求 input 改變時，trace 仍具有足夠 derivational structure 支持 adaptation。

Cheney 之後進一步指出 provenance graph 的 syntactic dependency / reachability 不等於 actual causality。

因此 Paper 03 必須保持：

$$
\boxed{
\mathsf{LedgerComplete}
\not\Rightarrow
\mathsf{CausallyComplete}.
}
$$

與：

$$
\boxed{
\mathsf{ProvenanceRecorded}
\not\Rightarrow
\mathsf{ActualCauseEstablished}.
}
$$

---

# 13. Round 2 Novelty Reclassification

| UCT component | Round 2 status | Closest prior art | Novelty assessment |
|---|---|---|---|
| Multiple closure operators | KNOWN | Kilpack; Hanai; Tholen | Not novel |
| Closure composition / commutation | KNOWN | Hanai; Kilpack | Not novel |
| Heterogeneously typed composition | KNOWN | König–Wolter–Kräuter | Not novel |
| Compatibility / bridge no-go | KNOWN | Zwart–Marsden | Generic idea not novel |
| Triple bridge coherence | KNOWN ANALOGUE | Goy / Cheng | Coherence itself not novel |
| Program semantics + modal reach | KNOWN | Möller–Struth | Domain-specific collapse exists |
| Non-free concurrent composition | KNOWN | Furusawa–Struth | Supports bridge certification |
| Causal vs epistemic ability | KNOWN | Duijf et al. | Not novel |
| Epistemic action vs accessibility | KNOWN | Baltag–Moss–Solecki | Not novel |
| Provenance semiring / algebra | KNOWN | Green–Tannen | Not novel |
| Provenance limits under difference | KNOWN | Amsterdamer et al. | Supports stability obligations |
| Provenance trace vs causality | KNOWN | Cheney et al. | Not novel |
| Canonical G/R/T triad with no unconditional entailment | CANDIDATE | Distributed across fields | Plausible synthesis novelty |
| First-cause generative sufficiency + resource responsibility | CANDIDATE | No close match found yet | Needs grounding/metaphysics search |
| Class-ultimate typed reach + meta-causal transformation hierarchy | CANDIDATE | Partial analogues | Needs agency/causal-power search |
| Bridge witness + obstruction + debt + ledger writeback | CANDIDATE COMBINATION | Distributive laws + provenance separately | Plausible integration novelty |
| Local-to-absolute gate integrated with closure claims | CANDIDATE | Related epistemic caution | Needs philosophy-of-science search |
| Functional convergence without ontological identity | CANDIDATE | No close match yet | Needs identity/metaphysics search |

---

# 14. 對 UCT v0.2 的建議 Patch

Round 2 不建議直接覆寫 v0.1 canonical source。應先建立 research patch，至少包含：

## P1 — Canonical Non-Collapse 修正

由強版本改為：

$$
\boxed{
X\not\vdash Y
\quad
\text{without an explicit bridge under the declared scope}.
}
$$

並加入：

$$
\mathsf{RepresentationRelativeCollapse}.
$$

## P2 — Bridge Coherence Obligation

新增：

$$
\mathsf{BridgeCoherenceObligation}.
$$

pairwise bridge 不自動推出 multi-way coherent composition。

## P3 — Bridge No-Go

新增：

$$
\mathsf{BRIDGE\_NO\_GO}.
$$

## P4 — Algebra Extension Stability

新增：

$$
\mathsf{AlgebraExtensionStability}.
$$

## P5 — Ledger / Causality Firewall

正式寫入：

$$
\mathsf{LedgerComplete}
\not\Rightarrow
\mathsf{CausallyComplete}.
$$

## P6 — Reach-to-Transform Lifting Family

把：

$$
\mathsf{R2TBridge}
$$

改寫成 domain-indexed lifting theorem family，而不是通用 bridge schema 的單一實例。

---

# 15. Round 2 結論

Round 2 明顯降低 UCT 的 broad novelty，但沒有找到一個現有理論可以完整取代 UCT。

目前最穩健的工作假說是：

$$
\boxed{
\begin{aligned}
\mathsf{UCTNoveltyCandidate}
=
&\;\mathsf{TypedGRTSynthesis}
\\
&+\mathsf{CrossTypeEvidenceProtocol}
\\
&+\mathsf{BridgeObstructionAndCoherence}
\\
&+\mathsf{ResponsibilityDebtAccounting}
\\
&+\mathsf{FirstCauseAndClassUltimateIntegration}.
\end{aligned}
}
$$

其中「多 closure」、「distributive bridge」、「coherence」、「provenance」、「observer/action separation」全部必須視為 prior-art-aligned components，而不是獨立 novelty。

下一輪若要繼續 publication-level novelty audit，最值得攻擊的三區是：

$$
\boxed{
\text{metaphysical grounding / first-cause explanation}
}
$$

$$
\boxed{
\text{formal causal power / agency / intervention}
}
$$

$$
\boxed{
\text{open-system categorical composition / institution-level mappings}
}
$$

只有這三區也壓完，才適合對 UCT 的「真正新增部分」做較強聲明。

---

# 核心外部文獻索引

- Kilpack, *The lattice of algebraic closure operators* (2014), arXiv:1411.6497.
- Hanai, *On commutative T-closure operators* (1953), DOI: 10.2996/KMJ/1138843295.
- Tholen, *Closure operators and their middle-interchange law* (2011), DOI: 10.1016/J.TOPOL.2011.04.015.
- König, Wolter, Kräuter, *Structural Operational Semantics for Heterogeneously Typed Coalgebras* (2023), DOI: 10.4230/LIPIcs.CALCO.2023.7.
- Zwart, Marsden, *No-Go Theorems for Distributive Laws* (2019), DOI: 10.1109/LICS.2019.8785707.
- Goy, *Weakening and Iterating Laws using String Diagrams* (2022), DOI: 10.46298/entics.10482.
- Möller, Struth, *Algebras of modal operators and partial correctness* (2006), DOI: 10.1016/j.tcs.2005.09.069.
- Furusawa, Struth, *Concurrent Dynamic Algebra* (2014/2015), DOI: 10.1145/2785967.
- Agrachev, Caponigro, *Controllability on the group of diffeomorphisms* (2009), DOI: 10.1016/J.ANIHPC.2009.07.003.
- Raginsky, *Some Remarks on Controllability of the Liouville Equation* (2024), arXiv:2404.14683.
- Duijf et al., *Doing Without Action Types*, DOI: 10.1017/S1755020320000362.
- Baltag, Moss, Solecki, *Logics for Epistemic Actions*, DOI: 10.48550/arXiv.2203.06744.
- Green, Tannen, *The Semiring Framework for Database Provenance* (2017), DOI: 10.1145/3034786.3056125.
- Amsterdamer, Deutch, Tannen, *On the Limitations of Provenance for Queries with Difference* (2011), arXiv:1105.2255.
- Cheney, Acar, Ahmed, *Provenance Traces* (2008), arXiv:0812.0564.
- Cheney, *Causality and the Semantics of Provenance* (2010), DOI: 10.4204/EPTCS.26.6.
- Grädel, Tannen, *Provenance Analysis and Semiring Semantics for First-Order Logic* (2024), DOI: 10.48550/arXiv.2412.07986.
