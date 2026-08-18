# 空間域證明包圍論 VII
## Enclosure Routing：邊際閉合價值、Gap 關鍵性與成本感知證明導航
### Spatial-Domain Proof Enclosure VII: Enclosure Routing, Marginal Closure Value, and Cost-Aware Proof Navigation

**Version:** v0.1  
**Date:** 2026-08-14  
**Status:** theorem-style research-routing framework; routing heuristics are not proof certificates  
**Canonical source:** UTF-8 Markdown; canonical mathematics uses ` $...$ ` and `$$...$$` only.

---

## 摘要

空間域證明包圍論前六篇依次建立 survivor soundness、route representation faithfulness、global coverage certificate、proof-trace compilation、Discovery–Verification Inversion 與 exceptional-core analysis。至此，研究系統已經可以回答「哪些區域仍可能包含反例」、「哪些表示與證書仍有效」、「哪些 gaps 阻止 global closure」以及「哪些歷史可以被編譯重用」。然而，一個新的決策問題隨之成為瓶頸：

> 在同時存在 bulk survivor、measure-zero exceptional core、boundary debt、representation singularity、stale certificate、bridge theorem 與昂貴 verification 的情況下，下一個研究動作應該選什麼？

本文提出 **Enclosure Routing**。核心原則不是最大化單一 survivor volume reduction，而是最大化**相對於當前 closure obligations 的非冗餘證明進展**。

對當前 survivor envelope $\Omega_t$ 與研究 action $a$，若 action 成功產生 sound theorem cut $H_a$，其真正新增排除區為

$$
\boxed{
X_t(a)
=
\Omega_t\setminus H_a.
}
$$

只計 $X_t(a)$ 而不計已被排除的歷史區域，可避免把重複 theorem 當成進展。若另有合法診斷函數 $q$，可定義

$$
\Delta_q(a\mid t)
=
q(\Omega_t)-q(\Omega_t\cap H_a),
$$

但 Paper 06 已證 measure / dimension 一般不是 closure-separating，因此 $\Delta_q$ 僅是 routing signal，不是 proof value 的完整定義。

本文把 closure obligations 建模為有限 witness / gap universe $\mathcal O_t$。每個 action 可影響一組 obligations $R_t(a)\subseteq\mathcal O_t$。對 action set $A$ 定義 weighted resolved-obligation functional

$$
F_t(A)
=
\sum_{o\in\cup_{a\in A}R_t(a)}w_t(o).
$$

本文證明 $F_t$ 為 monotone submodular。因此在「proof value 真正等價於有限 obligation coverage」且 action 成本相同的特殊 regime，經典 greedy maximum-coverage theory 才能合法提供近似保證。若 outcomes 帶不確定性且 objective 進一步滿足 adaptive monotonicity / adaptive submodularity，則 adaptive greedy theory 可作條件式 routing 輸入。

但一般 theorem research 不必然 submodular。兩個各自低收益的 lemmas 可能共同啟動一個 bridge theorem，使

$$
\Delta(a\mid S\cup\{b\})
>
\Delta(a\mid S),
$$

產生正 complementarity。本文以此建立 **Submodularity-by-Assumption No-Go**：未證 diminishing returns 時，不能因為「coverage 看起來像 submodular」就宣稱 greedy routing 有 approximation guarantee。

Paper 06 又指出 measure-zero exceptional core 可能承擔全部剩餘 closure difficulty。本文因此證明 **Volume-Greedy Failure Theorem**：只以 measure reduction 排序 action 的 policy 可以任意久地處理 positive-measure generic regions，而永遠延後唯一能碰到 zero-measure closure blocker 的 action。故

$$
\boxed{
\text{largest volume cut}
\not\Rightarrow
\text{largest closure value}.
}
$$

為處理這些異質目標，本文定義 route-value vector，而不是先假設唯一 scalar score：

$$
\boxed{
\mathbf V_t(a)
=
\left(
Y_t^{\rm excl},
Y_t^{\rm gap},
Y_t^{\rm core},
Y_t^{\rm repr},
Y_t^{\rm bridge},
Y_t^{\rm cert};
-\mathbf C_t(a),
-\mathbf R_t(a)
\right).
}
$$

其中 gains 分別表示非冗餘排除、gap closure、exceptional-core separability、representation refinement、bridge option value 與 certificate repair；完整成本向量包含 discovery、verification、coverage、gluing、maintenance、refinement 與 replay。本文證明 Pareto-dominated actions 在所有 componentwise-monotone routing preference 下可安全從候選集中刪除，但 Pareto frontier 上通常不存在不依賴偏好的唯一最佳 action。

本文再引入 **Bridge-Aware Lookahead**。若某個 action 的 immediate yield 為零，但可解鎖下一輪的大型 cut，純 myopic routing 可以嚴格失敗。因此 theorem-language expansion、representation refinement 與 bridge theorem 不應因「當輪排除 volume 為零」而自動降為低價值。

最後，本文提出 closure-fair routing：任何持續存在的 mandatory gap，若一直存在 admissible candidate route，不應因零 measure、低 immediate yield 或 score-scale mismatch 而永久 starvation。這不保證 gap 一定可解，但防止 routing policy 自己造成 global incompleteness。

本文的主要結論是：Enclosure Routing 不是「哪一刀最大」的單目標最佳化，而是**先辨識當前 proof-value geometry，再選擇與該 geometry 相容的 routing policy**。這是全域量詞—研究路由、有效覆蓋率、動態 Gap 場、概念積分與解空間幾何快速通道在 SDPE 中的正式匯流點。

---

## 關鍵詞

空間域證明包圍；Enclosure Routing；marginal closure value；gap routing；submodular coverage；adaptive submodularity；proof search；bridge theorem；Pareto routing；exceptional core；proof value；research routing；verification cost

---

# 1. 前六篇留下的正式狀態

設原始命題反例集合為

$$
\mathcal C
=
\{d\in D:\neg P(d)\}.
$$

Paper 01 維持 sound survivor invariant：

$$
\boxed{
\mathcal C\subseteq\Omega_t.
}
$$

Paper 02 要求 route representation 不得丟失 proof-relevant fibers。

Paper 03 定義 typed global gaps：

$$
\boxed{
\mathbf G_t
=
(G_D,G_B,G_{\partial},G_C,G_G,G_R)
}
$$

以及 Global Closure Certificate：

$$
\boxed{
\mathsf{GCC}_t.
}
$$

Paper 04 建立 proof history DAG、compiled support index 與 incremental replay。

Paper 05 區分

$$
D_t^{\rm resolve}
\neq
D_t^{\rm frontier}
$$

並證明 survivor contraction 不直接推出 frontier theorem discovery acceleration。

Paper 06 定義 limit survivor：

$$
\Omega_\infty
=
\bigcap_t\Omega_t,
$$

以及 relative theorem-language core：

$$
\operatorname{Core}(\Omega_0,\mathscr H)
=
\Omega_0\cap\bigcap_{H\in\mathscr H}H.
$$

並證明：

$$
\boxed{
\mu(\Omega_t)\to0
\not\Rightarrow
\Omega_\infty=\varnothing.
}
$$

因此 Paper 07 的問題不是「怎麼快速切 volume」，而是：

$$
\boxed{
\text{下一個 action 如何最大化 closure-relevant progress？}
}
$$

---

# 2. Fresh literature grounding

## 2.1 Monotone submodular maximization

Nemhauser、Wolsey 與 Fisher 的經典工作研究 nondecreasing submodular set functions 在 cardinality constraint 下的 greedy approximation。這提供一個重要條件式原則：若某個 proof-routing objective **已證明**具有 monotone submodular structure，greedy routing 才有成熟的近似理論可依賴。

本文不把一般 proof value 預設成 submodular。

## 2.2 Adaptive submodularity

Golovin 與 Krause 將 submodularity 推廣到 partial-observation / adaptive decision setting，證明在 adaptive monotone / adaptive submodular 條件成立時，adaptive greedy policy 有近似保證。

這和 theorem research 很接近，因為研究 action 的 outcome 在執行前通常未知；但「theorem discovery 是否 adaptive submodular」必須逐 domain 證明，不能從形式類似直接假定。

## 2.3 Proof search routing 已是實際 ATP 問題

HyperTree Proof Search、DeepSeek-Prover-V1.5、BFS-Prover 與 LeanProgress 都直接研究 proof-state expansion 的選擇、search value / progress estimation 或 best-first / MCTS 型導航。LeanSearch v2 則顯示整體 premise retrieval quality 可以影響固定 prover loop 的 downstream proof success。

這些工作證明：

$$
\boxed{
\text{proof navigation / premise choice / expansion priority 本身就是有效性能變量。}
}
$$

但它們的 objective 主要是「完成當前 formal proof」。SDPE Paper 07 的 objective 是長期 global-proof research 中的 survivor / gap / representation / certificate routing。

---

# 3. Research Action

## Definition 3.1 — Enclosure Action

在 epoch $t$，研究 action 記為

$$
\boxed{a\in\mathcal A_t.}
$$

其類型可包括：

1. $\mathsf{BulkCut}$：嘗試排除大塊 survivor region；
2. $\mathsf{Boundary}$：處理 equality / singular / degenerate boundary；
3. $\mathsf{Refine}$：representation refinement；
4. $\mathsf{LanguageExpand}$：新增 theorem family / primitive / invariant；
5. $\mathsf{Bridge}$：建立兩個已有 proof regions / theorem families 間的新接口；
6. $\mathsf{CertRepair}$：修復 stale dependency、coverage、gluing 或 replay gap；
7. $\mathsf{Explore}$：針對未知 frontier 生成新 conjectural route。

action 本身不是 theorem。

## Definition 3.2 — Accepted Action Outcome

只有當 action 產生可接受 certificate 後，其結果才進入 proof layer。

例如 theorem-cut outcome 為

$$
\mathcal C\subseteq H_a,
$$

則更新

$$
\Omega_{t+1}
=
\Omega_t\cap H_a.
$$

研究期間的 predicted gain 與 final certified gain 必須分開保存。

---

# 4. Nonredundant Exclusion Yield

## Definition 4.1 — Newly Excluded Region

若 accepted theorem cut $H_a$ 在當前 survivor 上生效，定義

$$
\boxed{
X_t(a)
:=
\Omega_t\setminus H_a.
}
$$

這是 action 在 epoch $t$ 真正新增的 exclusion region。

如果某 theorem 排除的區域早已不在 $\Omega_t$，則該部分不應再計 proof progress。

## Definition 4.2 — Diagnostic Marginal Yield

給定可用 diagnostic $q_t$，定義

$$
\boxed{
\Delta_q(a\mid t)
=
q_t(\Omega_t)
-
q_t(\Omega_t\cap H_a).
}
$$

Paper 06 的 closure-separation no-go 仍有效：

$$
\Delta_q
$$

可以是 routing signal，但若 $q$ 不是 closure-separating，不能單獨成為 proof completion criterion。

## Proposition 4.3 — Redundancy-Free Yield

若兩個 action $a,b$ 在當前 survivor 上滿足

$$
X_t(a)=X_t(b),
$$

則任何只依賴當前新排除 region 的 immediate-exclusion metric 必須給二者相同 yield，不得因歷史 theorem statement 不同而重複計功。

---

# 5. Closure Obligations

## Definition 5.1 — Finite Obligation Universe

在可有限化的 routing epoch，令

$$
\boxed{
\mathcal O_t
}
$$

為當前必須處理的 closure obligations，例如：

- uncovered branch witness；
- equality boundary stratum；
- unresolved representation-singular fiber class；
- stale certificate dependency；
- unowned overlap / glue obligation；
- explicit exceptional-core stratum；
- finite route-gap witnesses。

對每個 action $a$，定義它若成功可處理的 obligation subset：

$$
\boxed{
R_t(a)\subseteq\mathcal O_t.
}
$$

## Definition 5.2 — Weighted Obligation Coverage

給定非負 criticality weights

$$
w_t(o)\ge0,
$$

對 action set $A$ 定義

$$
\boxed{
F_t(A)
=
\sum_{o\in\cup_{a\in A}R_t(a)}w_t(o).
}
$$

## Theorem 5.3 — Obligation Coverage Is Monotone Submodular

 $F_t$ 滿足：

$$
A\subseteq B
\Longrightarrow
F_t(A)\le F_t(B),
$$

且對

$$
A\subseteq B,
\qquad
a\notin B,
$$

有 diminishing returns：

$$
\boxed{
F_t(A\cup\{a\})-F_t(A)
\ge
F_t(B\cup\{a\})-F_t(B).
}
$$

### Proof

action $a$ 的 marginal gain 只來自

$$
R_t(a)
\setminus
\bigcup_{b\in A}R_t(b).
$$

而 $A\subseteq B$ 時，後者的已覆蓋 union 更大，因此 $a$ 的未覆蓋 obligations 只能減少。非負 weights 保持不等式。

 $\square$

## Corollary 5.4 — Conditional Greedy Guarantee

若：

1. routing objective 真正就是 $F_t$ ；
2. action cost 相同；
3. 預算為最多 $k$ 個 actions；
4. $R_t(a)$ 已知且 outcomes deterministic；

則 classical monotone-submodular maximum-coverage greedy result 可用，greedy 在 $k$ 步後得到至少

$$
\boxed{
1-\left(1-\frac1k\right)^k
\ge
1-\frac1e
}
$$

倍的 optimal $k$ -action value。

這是**條件式 transfer theorem**，不是一般 theorem discovery 的 universal guarantee。

---

# 6. Adaptive Routing Under Uncertain Outcomes

真實 theorem research 中，action outcome 通常未知。

令 partial observation state 為

$$
\psi_t.
$$

對 action $a$ 定義 conditional expected marginal gain

$$
\Delta(a\mid\psi_t).
$$

如果 domain-specific routing utility 已被證明：

$$
\boxed{
\text{adaptive monotone}
+
\text{adaptive submodular},
}
$$

則 Golovin--Krause adaptive greedy framework 可作 routing theorem input。

## No-Go 6.1 — Adaptive Submodularity by Analogy

僅因研究流程是 sequential / uncertain，不推出 adaptive submodularity。

SDPE runtime 必須把

$$
\mathsf{AdaptiveSubmodularCert}
$$

視為可選的 domain-specific structure certificate，而不是預設值。

---

# 7. Theorem Synergy and Submodularity Failure

## Definition 7.1 — Complementarity Defect

對 routing utility $U$ 定義

$$
\boxed{
\Gamma_t(a,b\mid S)
=
\Delta_U(a\mid S\cup\{b\})
-
\Delta_U(a\mid S).
}
$$

若

$$
\Gamma_t(a,b\mid S)>0,
$$

則 $b$ 提高了 $a$ 的 marginal value，存在 synergy。

submodularity 要求所有此類 complementarity defect 非正。

## Proposition 7.2 — Bridge Synergy Counterexample

存在 actions $a,b$ 使

$$
U(\varnothing)=0,
$$

$$
U(\{a\})=U(\{b\})=0,
$$

但

$$
U(\{a,b\})=1.
$$

此時：

$$
\Delta_U(a\mid\varnothing)=0,
$$

但

$$
\Delta_U(a\mid\{b\})=1.
$$

所以

$$
\boxed{
\Gamma(a,b\mid\varnothing)=1>0,
}
$$

utility 不是 submodular。

這對 proof research 非常自然：一個 representation lemma 與一個 arithmetic lemma 可能單獨都無法切 survivor，組合後才產生 bridge theorem。

## No-Go 7.3 — Greedy Guarantee Without Geometry Certificate

未證 submodularity / adaptive submodularity 時，不得引用 greedy approximation guarantee 作為研究路由的數學保證。

---

# 8. Volume-Greedy Failure

Paper 06 已證 zero-measure survivor 可以非空並承擔全部 closure obstruction。

## Theorem 8.1 — Volume-Greedy Can Postpone the Only Closure-Critical Action Arbitrarily Long

對任意 $m\ge1$，存在 survivor

$$
\Omega=G_1\cup\cdots\cup G_m\cup S
$$

與 measure $\mu$，其中：

$$
\mu(G_i)>0,
\qquad
\mu(S)=0,
\qquad
S\neq\varnothing,
$$

以及 actions

$$
a_1,\ldots,a_m,a_*，
$$

使：

- $a_i$ 只排除 $G_i$ ；
- $a_*$ 只排除 $S$ ；
- 任何 remaining $G_i$ 的 volume gain 都嚴格大於 $a_*$ 的 volume gain $0$。

因此任何每輪只最大化正 immediate volume reduction 的 routing policy 都會先選完

$$
a_1,\ldots,a_m
$$

才可能處理 $a_*$。

因 $m$ 任意，zero-measure closure blocker 可被 volume-greedy 任意久 postponement。

 $\square$

## Corollary 8.2

$$
\boxed{
\text{largest immediate measure reduction}
\not\Rightarrow
\text{largest closure value}.
}
$$

---

# 9. Gap Criticality

## Definition 9.1 — Action Support of an Obligation

對 obligation $o$，定義目前已知可影響它的 actions：

$$
\boxed{
\mathcal A_t(o)
=
\{a\in\mathcal A_t:o\in R_t(a)\}.
}
$$

若

$$
|\mathcal A_t(o)|=1,
$$

唯一 action 稱為 **currently essential route** for $o$。

## Definition 9.2 — Closure Criticality

可定義一個 routing diagnostic：

$$
\boxed{
\operatorname{Crit}_t(o)
=
\frac{w_t(o)}{|\mathcal A_t(o)|}
}
$$

作為「高權重且可替代 route 很少」的簡化 criticality signal。

這不是 theorem probability，也不是證明 obligation 可解。

## No-Go 9.3 — Zero Measure Implies Zero Routing Priority

mandatory boundary / core obligation 即使 measure zero，只要未 ownership / refute，就仍是 GCC blocker，不能因 measure zero 而設 priority 為零。

---

# 10. Route-Value Vector

單一 score 容易把不可交換的 proof objectives 隱藏掉。本文先定義 vector：

$$
\boxed{
\mathbf V_t(a)
=
\left(
Y_t^{\rm excl},
Y_t^{\rm gap},
Y_t^{\rm core},
Y_t^{\rm repr},
Y_t^{\rm bridge},
Y_t^{\rm cert};
-\mathbf C_t(a),
-\mathbf R_t(a)
\right).
}
$$

其中：

### $Y^{\rm excl}$ — Nonredundant Exclusion Yield

當 action 成功後對當前 survivor 的新增排除。

### $Y^{\rm gap}$ — Gap Resolution Yield

對 typed mandatory gaps / obligations 的 resolution value。

### $Y^{\rm core}$ — Core Separability Gain

對

$$
\operatorname{Core}(\Omega_t,\mathscr H_t)
$$

的可分離性增益。例如新增 theorem language 後，相對 core 是否縮小或被 stratify。

### $Y^{\rm repr}$ — Representation Gain

減少

$$
\operatorname{Sing}_\Sigma(\phi)
$$

或提升 RouteCert adequacy。

### $Y^{\rm bridge}$ — Bridge / Option Value

action 是否解鎖原本不可用的 theorem family、representation map、proof channel 或下一步高價值 action。

### $Y^{\rm cert}$ — Certificate Repair Value

修復

$$
G_C,G_G,G_R
$$

或降低 Dirty / reopen burden。

---

# 11. Full Cost Vector

沿用 GCS 與 Paper 04--05 的完整帳本，對 action $a$ 定義：

$$
\boxed{
\mathbf C_t(a)
=
\left(
C^{\rm discover},
C^{\rm verify},
C^{\rm coverage},
C^{\rm glue},
C^{\rm maintain},
C^{\rm refine},
C^{\rm replay}
\right).
}
$$

另保存 risk / uncertainty vector：

$$
\boxed{
\mathbf R_t(a)
=
\left(
R^{\rm fail},
R^{\rm stale},
R^{\rm repr},
R^{\rm dependency},
R^{\rm estimate}
\right).
}
$$

這些是 routing estimates，不可替代 final checker。

---

# 12. Pareto Routing

## Definition 12.1 — Dominance

若 actions $a,b$ 滿足：

- $a$ 的所有 gain components 不低於 $b$ ；
- $a$ 的所有 cost / risk components 不高於 $b$ ；
- 至少一項嚴格較優；

則記：

$$
\boxed{a\succ b.}
$$

## Theorem 12.2 — Pareto-Dominated Action Pruning

對任何對 gains componentwise nondecreasing、對 costs / risks componentwise nonincreasing 的 routing preference functional $J$，若

$$
a\succ b,
$$

則

$$
\boxed{J(a)\ge J(b).}
$$

因此在這一類 preferences 下， $b$ 不需要作為唯一候選最優 action 保留。

 $\square$

## Corollary 12.3

Pareto pruning 可以先於任何 scalarization 執行。

## No-Go 12.4 — Universal Scalar Routing Score

若兩個 actions 的 gain vectors 分別為

$$
(1,0)
$$

與

$$
(0,1),
$$

則不同合法 preferences 可以分別偏好二者。因此不存在不依賴 proof objective / policy weights 的 universal scalar ranking 能同時代表所有 monotone preferences。

---

# 13. Cost-Aware Scalarization Is a Policy, Not a Theorem

若 runtime 已明示 weights $\mathbf w,\boldsymbol\lambda$，可使用：

$$
\boxed{
S_t(a)
=
\frac{\mathbf w\cdot\mathbf Y_t(a)}
{\boldsymbol\lambda\cdot\mathbf C_t(a)}.
}
$$

也可加入 risk penalty。

但 weights 必須保存於 RouteDecision certificate；改 weights 就是改 policy，不應假裝 theorem 本身改變。

MCDM 的量詞—證明 profile 可作 cost / risk prior，但不能直接提供 proof validity。

---

# 14. Bridge-Aware Lookahead

## Definition 14.1 — Action Unlock Set

令

$$
\operatorname{Unlock}_t(a)
$$

為 action $a$ 成功後才變 admissible / meaningful 的下一層 actions。

## Definition 14.2 — Two-Step Route Value

對 immediate utility $u_t$，定義簡化二步值：

$$
\boxed{
V_t^{(2)}(a)
=
\nu_t u_t(a)
+
\max_{b\in\operatorname{Unlock}_t(a)}u_{t+1}(b)
-
\operatorname{Cost}_t^{(2)}(a).
}
$$

其中 $\nu_t$ 可為 discount / confidence factor。

## Proposition 14.3 — Myopic Bridge Failure

存在 actions $a_{\rm bulk},a_{\rm bridge},b_{\rm close}$ 使：

$$
\nu_t u(a_{\rm bulk})>u(a_{\rm bridge})=0,
$$

故 one-step greedy 選 $a_{\rm bulk}$ ；但

$$
\operatorname{Unlock}(a_{\rm bridge})
=\{b_{\rm close}\},
$$

且 $b_{\rm close}$ 可完成 GCC，而 $a_{\rm bulk}$ 不解鎖任何 closure route。

因此在 two-step objective 下：

$$
\boxed{
V^{(2)}(a_{\rm bridge})
>
V^{(2)}(a_{\rm bulk})
}
$$

可以成立。

所以 representation refinement、theorem-language expansion 與 bridge theorem 不能因當輪 immediate exclusion 為零而自動判定低價值。

---

# 15. Closure-Fair Routing

## Definition 15.1 — Persistent Mandatory Obligation

若 obligation $o$：

1. 持續阻止 GCC；
2. 尚未被 refute / owned / repaired；
3. 長期存在至少一個 admissible candidate action；

則稱 $o$ persistent mandatory。

## Definition 15.2 — $B$ -Fair Router

若每個 persistent mandatory obligation 在至多 $B$ 個 routing epochs 內至少被一個影響它的 admissible action 實際選中一次，則 policy 稱為 $B$ -fair。

## Proposition 15.3 — No Routing-Induced Starvation

在 $B$ -fair policy 下，不存在 persistent mandatory gap 僅因其它 actions 長期具有較高 immediate score 而永遠不被嘗試。

注意：

$$
\boxed{
\text{no starvation}
\not\Rightarrow
\text{gap is solvable}.
}
$$

fairness 是 research completeness policy，不是數學 closure theorem。

---

# 16. Discrete Closure Potential

在有限 obligation model 中，定義 unresolved weighted potential：

$$
\boxed{
\Phi_t
=
\sum_{o\in\mathcal O_t^{\rm unresolved}}w(o).
}
$$

## Theorem 16.1 — Finite Successful-Progress Termination

若在一個 stable epoch family 中：

1. $\mathcal O$ 有限；
2. $w(o)\ge\varepsilon>0$ ；
3. 不產生新 mandatory obligations；
4. 每個 accepted action 至少永久解決一個 unresolved obligation；
5. obligation 不 reopen；
6. $\Phi=0$ 已由 GCC semantics 證明等價於 closure；

則最多經

$$
\boxed{
\frac{\Phi_0}{\varepsilon}
}
$$

個 successful accepted actions 即必須 closure。

### Boundary

此 theorem 的強假設正好說明真實研究為何困難：representation refinement 可能出生新 gaps，dependency staleness 可能 reopen obligations，且 finite obligation universe 本身需要 completeness certificate。

---

# 17. Routing Regimes

本文建議 runtime 先辨識 routing geometry，再選 policy。

## Regime A — Certified Coverage Geometry

若 closure obligations finite，action effects deterministic，且 objective 是 weighted union coverage：

$$
\boxed{
\text{use submodular / set-cover style routing}.
}
$$

## Regime B — Adaptive Submodular Geometry

若 outcomes uncertain，但 adaptive submodularity 已證：

$$
\boxed{
\text{use adaptive greedy family}.
}
$$

## Regime C — Synergistic / Bridge Geometry

若 observed complementarity

$$
\Gamma>0
$$

顯著：

$$
\boxed{
\text{use lookahead / bridge-aware routing}.
}
$$

## Regime D — Exceptional-Core Geometry

若 bulk measure 已低但 mandatory core / boundary persists：

$$
\boxed{
\text{prioritize separability / boundary / representation routes over volume}.
}
$$

## Regime E — Certificate Debt Geometry

若 $G_C,G_G,G_R$ 阻止 GCC：

$$
\boxed{
\text{proof repair may dominate new theorem discovery}.
}
$$

---

# 18. Enclosure Routing Protocol v0.1

本文提出：

$$
\boxed{
\begin{aligned}
&\mathsf{Profile}\\
&\to\mathsf{GapExtract}\\
&\to\mathsf{ActionGenerate}\\
&\to\mathsf{SafetyGate}\\
&\to\mathsf{ValueEstimate}\\
&\to\mathsf{ParetoPrune}\\
&\to\mathsf{GeometryClassify}\\
&\to\mathsf{Select}\\
&\to\mathsf{Execute}\\
&\to\mathsf{Verify}\\
&\to\mathsf{Update}\\
&\to\mathsf{Compile}.
\end{aligned}
}
$$

## 18.1 Profile

讀入：

$$
\Omega_t,
\mathbf G_t,
\mathsf{SurvProf}_t,
\mathsf{GCC}_t,
\mathcal H_t,
\mathbf C_t.
$$

## 18.2 GapExtract

辨識：

- bulk survivor；
- zero-measure core；
- boundary debt；
- singular fibers；
- stale certificates；
- theorem-language irreducible residue。

## 18.3 ActionGenerate

從 DEST Gap-directed generation / concept integration 產生 action types。

## 18.4 SafetyGate

過濾明顯 scope mismatch、representation-invalid、dependency-invalid actions。

## 18.5 ValueEstimate

估計 gains、costs、risks；必須標示 predicted / uncertified。

## 18.6 ParetoPrune

去除 dominated actions。

## 18.7 GeometryClassify

判定 coverage / adaptive-submodular / synergy / exceptional-core / certificate-debt regime。

## 18.8 Select

使用與 regime 相容的 policy。

## 18.9 Verify

只有 verifier 接受後，predicted gain 才轉為 certified state update。

---

# 19. Route Decision Certificate

每一輪 routing 決策保存：

$$
\boxed{
\mathsf{RouteDecision}_t
=
\langle
StateFP,
CandidateSet,
ActionTypes,
PredictedValues,
Costs,
Risks,
GapTouches,
CoreTouches,
Unlocks,
Policy,
Weights,
Chosen,
Reason,
Outcome,
Verifier,
ActualGain,
Version,
Replay
\rangle.
}
$$

這讓 routing policy 本身可以被 longitudinal audit。

如果未來發現某類 score 長期誤估 bridge actions，可以重新估計 policy，而不必改寫已接受的 theorem validity。

---

# 20. Routing Regret

在 finite benchmark 中，若 oracle policy 在 horizon $T$ 的 closure utility 為

$$
U_T^*,
$$

router 得到

$$
U_T^{\pi},
$$

定義 routing regret：

$$
\boxed{
\operatorname{Regret}_T(\pi)
=
U_T^*-U_T^{\pi}.
}
$$

如果 utility 是 closure time，可改用 time regret。

真實數學研究通常沒有 oracle；regret 主要用於 synthetic / finite benchmark，而不是主張人類歷史研究存在可知 global optimum。

---

# 21. Benchmark Families

Paper 08 runtime 前，本文建議至少測六種 routing family。

## 21.1 Redundant bulk coverage

大量 actions 重疊排除同一 generic region，測 marginal de-duplication。

## 21.2 Zero-measure exceptional core

bulk actions 有高 measure yield，但只有 zero-measure core action 可 closure，測 volume-greedy failure。

## 21.3 Finite weighted obligation coverage

測 greedy submodular routing 與 exact optimum 差距。

## 21.4 Synergistic bridge

單一 actions immediate gain 低，組合後產生高 closure value，測 myopic failure。

## 21.5 Representation singularity

bulk cuts 無法區分 mixed fibers，只有 refinement action 解鎖 sound exclusion。

## 21.6 Certificate debt / stale replay

新增 theorem 不再是瓶頸，GCC 只差 certificate repair，測 repair-aware routing。

---

# 22. Ablations

至少比較：

1. random routing；
2. volume greedy；
3. immediate obligation greedy；
4. cost-ratio greedy；
5. Pareto + greedy；
6. bridge-aware lookahead；
7. gap-fair routing；
8. full enclosure router。

報告：

$$
\boxed{
\begin{aligned}
&\text{time-to-GCC},\\
&\text{accepted theorem count},\\
&\text{failed proposal cost},\\
&\text{verification cost},\\
&\text{coverage debt},\\
&\text{gap starvation},\\
&\text{exceptional-core lifetime},\\
&\text{routing regret},\\
&\text{Pareto-front size},\\
&\text{bridge discovery rate}.
\end{aligned}
}
$$

---

# 23. Internal-Series Integration

## 23.1 MCDM

MCDM 的 quantifier / proof-asymmetry / difficulty profile 可提供：

- action cost prior；
- proof-direction prior；
- verification difficulty prior；
- global-coupling risk prior。

但 MCDM score 不直接等於 closure value。

## 23.2 Effective Coverage

《從路徑數量到有效覆蓋率》的核心：

$$
\Delta C(p\mid\mathcal P_t)
$$

在 SDPE 中被收斂成 current-survivor / current-obligation 上的 **nonredundant marginal gain**。

## 23.3 Known / Unknown Compilation

「已知則編譯、未知則展開」在 Paper 07 中成為 routing gate：

- compiled / certified regions 不重複搜尋；
- persistent unknown / singular / boundary residue 進入 action generation。

## 23.4 Solution-Space Geometry

概念積分與幾何快速通道提供 bridge / representation / shortcut action 類別。

Paper 05 已證 cache hit 不直接降低 frontier theorem difficulty；Paper 07 現在提供可測的 structural bridge-value channel。

## 23.5 DEST Gap Field / Concept Integral 2.0

Gap Field 提供 typed gap support、persistence、coupling、detectability；Concept Integral 2.0 提供 Gap-directed candidate generation。

SDPE 新增的限制是：candidate generation 後必須進入 proof-safe SafetyGate、verification 與 GCC update。

---

# 24. No-Go Ledger

## No-Go 24.1 — Largest Volume Cut Is Best Research Action

zero-measure core counterexample 否定。

## No-Go 24.2 — More Paths Mean More Progress

高度重疊 actions 必須按 current marginal gain 去重。

## No-Go 24.3 — Greedy Is Universally Near-Optimal

只有已證 submodular / adaptive-submodular structure 才有相應 guarantee。

## No-Go 24.4 — Immediate Gain Captures Bridge Value

representation / language / bridge actions 可以零 immediate yield 但高 future closure value。

## No-Go 24.5 — Single Scalar Score Is Canonical

多目標 tradeoff 在一般情況沒有 preference-free total order。

## No-Go 24.6 — Measure-Zero Gap Gets Zero Priority

mandatory gap 的 closure relevance 不由 measure 決定。

## No-Go 24.7 — Fair Routing Proves Solvability

fairness 只阻止 starvation，不保證存在成功 theorem。

## No-Go 24.8 — High Predicted Value Is a Proof Artifact

prediction 只有通過 verification 才能更新 survivor / GCC。

## No-Go 24.9 — Route Repair Is Non-Research Work

若 GCC blocker 是 certificate / coverage / representation debt，repair action 可以比新 theorem 更高 closure value。

## No-Go 24.10 — Routing Policy and Mathematical Truth Are the Same Layer

policy 可以錯、可以改、可以學習；已驗證 theorem validity 不應依賴 routing policy 的歷史正確性。

---

# 25. Theorem / External Input / Hypothesis Ledger

## 25.1 Internal theorems / propositions

1. Redundancy-Free Yield；
2. Obligation Coverage Monotone Submodularity；
3. Volume-Greedy Failure；
4. Pareto-Dominated Action Pruning；
5. Bridge-Synergy Counterexample；
6. Myopic Bridge Failure；
7. No Routing-Induced Starvation under $B$ -fairness；
8. Finite Successful-Progress Termination under stable complete obligation model。

## 25.2 Conditional external transfers

1. monotone-submodular greedy approximation under cardinality constraint；
2. adaptive greedy guarantees under adaptive monotonicity / adaptive submodularity。

這些只在 SDPE routing utility 已被證明符合其 assumptions 時使用。

## 25.3 Open hypotheses

1. late-stage SDPE proof routing often becomes synergy-dominated rather than submodular；
2. exceptional-core targeting improves time-to-GCC over volume greedy；
3. bridge-aware routing can provide a structural mechanism for Strong DVI；
4. learned action-value estimates can generalize across theorem families when RouteCert / Gap types align；
5. routing policies trained on compiled proof histories can reduce frontier branching without increasing unsound proposal rate。

## 25.4 External grounding

- Nemhauser--Wolsey--Fisher / Nemhauser--Wolsey submodular maximization；
- Golovin--Krause adaptive submodularity；
- HyperTree Proof Search；
- DeepSeek-Prover-V1.5；
- BFS-Prover；
- LeanProgress；
- LeanSearch v2。

---

# 26. Checker Scope

companion checker 驗證 finite models 中：

1. weighted obligation coverage monotonicity；
2. weighted obligation coverage submodularity；
3. cardinality- $k$ greedy maximum-coverage lower bound on random small instances；
4. redundancy-free current-survivor gain；
5. zero-weight exceptional-core volume-greedy failure；
6. bridge synergy / submodularity failure；
7. Pareto dominated action pruning under random monotone scalarizations；
8. bridge-aware two-step routing beats myopic example；
9. finite closure-potential termination；
10. bounded-starvation fair scheduling toy model。

checker 不證：

- 一般 theorem discovery objective 是 submodular；
- 預測 route value 已校準；
- Strong DVI；
- 任意數學猜想存在 finite complete obligation universe；
- SDPE routing policy 能保證找到未知 theorem。

---

# 27. 前七篇形成的 proof-space architecture

$$
\boxed{
\begin{aligned}
&\text{P01 Survivor Soundness}\\
&\downarrow\\
&\text{P02 Representation Faithfulness}\\
&\downarrow\\
&\text{P03 Global Coverage / Closure}\\
&\downarrow\\
&\text{P04 Trace Compilation / Incremental Replay}\\
&\downarrow\\
&\text{P05 Discovery--Verification Cost Dynamics}\\
&\downarrow\\
&\text{P06 Residual Geometry / Exceptional Core}\\
&\downarrow\\
&\text{P07 Cost-Aware Enclosure Routing}.
\end{aligned}
}
$$

Paper 07 的核心改變是：SDPE 不再被動等待下一個 theorem，而第一次明確建模

$$
\boxed{
\text{研究下一刀本身也是一個可分析、可驗證、可 benchmark 的決策問題。}
}
$$

---

# 28. 下一篇：SDPE Runtime / Benchmark

前七篇已經提供 runtime 需要的主要語義：

- survivor envelope；
- RouteCert；
- typed gaps；
- GCC；
- proof-history DAG；
- compiled pruning；
- DVI telemetry；
- survivor profile；
- route-value / route-decision certificate。

因此下一篇可以正式整合成：

$$
\boxed{
\textbf{SDPE Paper 08 — Runtime, Benchmark, and Proof-Space Observatory}.}
$$

最小 pipeline 升級為：

$$
\boxed{
\begin{aligned}
&\mathsf{Detect}\\
&\to\mathsf{Profile}\\
&\to\mathsf{GapExtract}\\
&\to\mathsf{ActionGenerate}\\
&\to\mathsf{Route}\\
&\to\mathsf{Propose}\\
&\to\mathsf{Verify}\\
&\to\mathsf{CoverageAudit}\\
&\to\mathsf{BoundaryAudit}\\
&\to\mathsf{GlueAudit}\\
&\to\mathsf{Compile}\\
&\to\mathsf{Commit}.
\end{aligned}
}
$$

---

# 29. Final Status

本文最重要的結論可以壓成四句。

第一：

$$
\boxed{
\text{proof progress 應計 nonredundant closure gain，而不是 theorem count。}
}
$$

第二：

$$
\boxed{
\text{volume reduction 是 routing signal，不是 universal proof value。}
}
$$

第三：

$$
\boxed{
\text{greedy guarantee 必須由 proof-value geometry 的 submodularity certificate 支撐。}
}
$$

第四：

$$
\boxed{
\text{bridge、boundary、representation 與 certificate repair 可以具有零 immediate volume gain，卻是 global closure 的最高價值 action。}
}
$$

因此 Enclosure Routing 的總原則是：

$$
\boxed{
\textbf{先辨識 proof-value geometry，再選擇 routing algorithm。}
}
$$

---

# References

1. G. L. Nemhauser, L. A. Wolsey, M. L. Fisher, **An Analysis of Approximations for Maximizing Submodular Set Functions—I**, *Mathematical Programming* 14 (1978), 265–294, DOI `10.1007/BF01588971`.
2. G. L. Nemhauser, L. A. Wolsey, **Best Algorithms for Approximating the Maximum of a Submodular Set Function**, *Mathematics of Operations Research* 3(3) (1978), 177–188, DOI `10.1287/moor.3.3.177`.
3. Daniel Golovin, Andreas Krause, **Adaptive Submodularity: Theory and Applications in Active Learning and Stochastic Optimization**, arXiv:`1003.3967`.
4. Guillaume Lample et al., **HyperTree Proof Search for Neural Theorem Proving**, arXiv:`2205.11491`.
5. Huajian Xin et al., **DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search**, arXiv:`2408.08152`.
6. Ran Xin et al., **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving**, arXiv:`2502.03438`.
7. Suozhi Huang, Peiyang Song, Robert Joseph George, Anima Anandkumar, **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction**, arXiv:`2502.17925`.
8. Guoxiong Gao et al., **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving**, arXiv:`2605.13137`.
9. Prior SDPE artifacts: Papers 01--06.
10. Prior internal artifacts: **MCDM v0.2**; **從路徑數量到有效覆蓋率**; **已知則編譯，未知則展開**; **概念積分與解空間填充**; **快速究竟有多快**; **DEST Gap 場論**; **概念積分 2.0**.
