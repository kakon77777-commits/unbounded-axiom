# UGC/CUR Formal Core Specification v0.1
## 無界生成閉包、類終極可達性與轉換閉包之形式核心規格

**文件編號：** EML-UGC-CUR-FCSPEC-2026-v0.1  
**日期：** 2026-08-26  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**狀態：** INTERNAL CANONICAL FORMAL CORE / PAPER-00 ANCHOR  
**上游正典：** `UGC_CUR_Canonical_Reconciliation_v0.1_2026-08-26.md`  
**文件角色：** 後續 Paper 01--05 的共同形式核心；不是宇宙學、神學或絕對本體論的完成證明。  
**canonical source 規則：** 本文件以 UTF-8 Markdown 為正式 source；所有數學只使用 ` $...$ ` 與 `$$...$$` delimiter。

---

# 0. Release Decision

本文件固定 UGC/CUR 高階 closure layer 的第一版可推演形式核心。

核心研究對象不是一個裸 source、一個裸 agent 或一個裸 world，而是下列三族閉包及其責任記帳：

$$
\boxed{
\operatorname{GenCl}
=
\text{what can be generated}
}
$$

$$
\boxed{
\mathsf{Reach}
=
\text{what can be reached under a typed capability mode}
}
$$

$$
\boxed{
\operatorname{TransCl}
=
\text{what transformations can be realized}
}
$$

以及：

$$
\boxed{
\mathsf{Ledger}
=
\text{how state, history, provenance, resource responsibility and unresolved debt are accounted for}
}
$$

本文件採取以下最高層原則：

$$
\boxed{
\text{Unification}
\neq
\text{Primitive Collapse}.
}
$$

因此 UGC/CUR 不取代 OBRC、RDSS、SST、DEST、Realizability、Ledger-Causal Mathematics 或 MWT；本文件只定義它們在高階 closure 問題上的共同接口。

---

# 1. Claim Types and Formal Status

任何正式聲明必須帶至少一個 claim status：

$$
\boxed{
\mathfrak S_{\rm claim}
=
\{
\mathsf{DEF},
\mathsf{AX},
\mathsf{PROP},
\mathsf{CONJ},
\mathsf{MODEL},
\mathsf{OPEN}
\}.
}
$$

語義如下：

- $\mathsf{DEF}$：本文定義；
- $\mathsf{AX}$：形式協議／建模公理，不宣稱為宇宙形上真理；
- $\mathsf{PROP}$：由本文定義與明示假設可推出；
- $\mathsf{CONJ}$：結構猜想，尚待證明或反例；
- $\mathsf{MODEL}$：特定模型中的可構造聲明；
- $\mathsf{OPEN}$：目前未閉合的 proof obligation。

任何 $\mathsf{OPEN}$ 不得因敘事便利被提升為 $\mathsf{PROP}$。

---

# 2. Core Type Universe

## 2.1 Target Domain

令：

$$
\boxed{
\Omega_D
}
$$

表示本次聲明的 declared target domain。

它只表示「本模型宣告要討論的目標域」，不自動表示 metaphysically complete ontology。

因此：

$$
\boxed{
\Omega_D
\neq
\Omega_{\rm absolute}
}
$$

除非另有 completeness certificate。

## 2.2 Time / Evolution Horizon

令：

$$
\boxed{
T
\in
\mathfrak T
}
$$

表示演化 horizon。 $T$ 可以是離散步數、連續時間區間、事件偏序截面或模型內的無界 horizon。

若使用：

$$
T=\infty,
$$

它是明示模型條件，不得被隱藏為 source 的內在能力。

## 2.3 Judgement Context

定義 observer-indexed judgement context：

$$
\boxed{
\Theta
=
\left\langle
 o,
 s,
 \rho,
 t,
 \mathsf{Ops},
 \mathsf{Rep},
 \mathsf{Perm},
 \mathsf{Know},
 \mathsf{WorldAssump}
\right\rangle.
}
$$

其中依序表示 observer、scale、resolution、time、operator set、representation regime、permission regime、knowledge regime 與 world assumption。

任何 existence、non-being、reachability、connectivity、law-invariance、unboundedness 或 class-ultimate claim 都必須可追溯到 $\Theta$ 或明示其 observer-independent proof。

---

# 3. World / History / Law / Boundary Separation

## 3.1 Authoritative World State

令：

$$
\boxed{
\mathfrak W_t
}
$$

表示時間 $t$ 的 authoritative current world state。

## 3.2 History

令：

$$
\boxed{
\mathfrak H_{\le t}
}
$$

表示事件、路徑、版本與必要因果歷史。

本核心固定：

$$
\boxed{
\mathfrak W_t
\neq
\mathfrak H_{\le t}.
}
$$

相同 current state 可以具有不同 relevant histories。

## 3.3 Law Regime

令：

$$
\boxed{
\mathsf{Law}_t
}
$$

表示時間 $t$ 的 effective law / rule regime。

它可以是固定的、分層的、狀態依賴的或模型中允許演化的；本文件不預設唯一宇宙法則模型。

## 3.4 Boundary Family

令：

$$
\boxed{
\mathfrak B_t
}
$$

表示 typed, state-bearing boundary family。

邊界可以具有傳輸、過濾、轉碼、阻擋、權限、耦合與狀態更新，因此：

$$
\boxed{
\mathsf{Boundary}
\neq
\mathsf{Disconnection}.
}
$$

## 3.5 Relation Family

令：

$$
\boxed{
\mathfrak R_t
}
$$

表示可被判定、建立、移除或改寫的 typed relation family。

---

# 4. Canonical Generative Environment

定義生成環境：

$$
\boxed{
\mathfrak E_t^{\rm gen}
=
\left\langle
\mathsf{Car}_t,
\mathsf{Law}_t,
\mathfrak B_t,
\mathsf{Ops}_t,
\mathfrak H_{\le t},
\mathsf{Ext}_t,
\mathcal C_t^{\rm gen}
\right\rangle.
}
$$

其中：

- $\mathsf{Car}_t$：carrier / substrate；
- $\mathsf{Law}_t$：effective law regime；
- $\mathfrak B_t$：boundary family；
- $\mathsf{Ops}_t$：available operator family；
- $\mathfrak H_{\le t}$：relevant history；
- $\mathsf{Ext}_t$：external input、oracle、randomness、resource feed 或其他外源；
- $\mathcal C_t^{\rm gen}$：generative admissibility constraints。

本文件固定：

$$
\boxed{
\mathsf{Source}
\neq
\mathsf{Carrier}
\neq
\mathsf{Law}
\neq
\mathsf{Boundary}
\neq
\mathsf{ExternalInput}.
}
$$

---

# 5. Generative Transition System

## 5.1 Generative Configuration

定義生成 configuration space：

$$
\boxed{
\mathfrak X^{\rm gen}
}
$$

其元素至少可以承載：

$$
\boxed{
\chi_t
=
\left\langle
\mathfrak W_t,
\mathsf{Law}_t,
\mathfrak E_t^{\rm gen}
\right\rangle.
}
$$

## 5.2 Source Initialization

source $S$ 不直接等同初始 world state。定義初始化映射：

$$
\boxed{
\mathsf{Init}_{D}
:
(S,\mathfrak E_0^{\rm gen})
\rightharpoonup
\mathfrak X^{\rm gen}.
}
$$

若初始化本身需要未列明外部來源，該依賴必須進入 Generative Responsibility record。

## 5.3 Generative Step

定義部分生成步：

$$
\boxed{
\mathsf{GenStep}_t
:
\mathfrak X^{\rm gen}
\rightharpoonup
\mathfrak X^{\rm gen}.
}
$$

允許非決定性或分支時，可改寫為 relation：

$$
\boxed{
\chi_t
\rightsquigarrow_{\rm gen}
\chi_{t+1}.
}
$$

任何生成 trace 必須保存必要 provenance。

## 5.4 Output Projection

定義模型內的生成結果投影：

$$
\boxed{
\mathsf{Out}_D
:
\mathfrak X^{\rm gen}
\rightharpoonup
\mathcal P(\Omega_D).
}
$$

這避免把整個 configuration 與被研究 outcome 混為同一物件。

---

# 6. Canonical Generative Closure

## 6.1 Trace Set

令：

$$
\mathsf{Trace}_{\le T}
(S\mid\mathfrak E^{\rm gen})
$$

表示由 $\mathsf{Init}$ 出發、遵守 $\mathsf{GenStep}$ 與 $\mathcal C^{\rm gen}$ 、長度或時間不超過 $T$ 的合法生成 traces。

## 6.2 Definition of Generative Closure

正式定義：

$$
\boxed{
\operatorname{GenCl}_{D,T}
\left(
S
\mid
\mathfrak E^{\rm gen}
\right)
=
\left\{
y\in\Omega_D
\;\middle|\;
\exists\tau
\in
\mathsf{Trace}_{\le T}
(S\mid\mathfrak E^{\rm gen}),
\exists\chi\in\tau:
y\in\mathsf{Out}_D(\chi)
\right\}.
}
$$

此定義取代舊版跨系列的裸生成閉包記法。

## 6.3 Fixed-Law Generative Closure

若：

$$
\boxed{
\mathsf{Law}_t
=
\mathsf{Law}_0
\qquad
\forall t\le T,
}
$$

稱為 fixed-law generative closure。

## 6.4 Law-Coevolving Generative Closure

若允許：

$$
\boxed{
\mathsf{Law}_{t+1}
\neq
\mathsf{Law}_t,
}
$$

則 law state 必須成為 $\chi_t$ 的顯式分量，且 law change 必須具有 transition witness。

## 6.5 Reflexive Generative Closure

若連 $\mathsf{GenStep}_t$ 的規格都可被系統內部合法改寫，定義 reflexive state：

$$
\boxed{
\chi_t^{\rm ref}
=
\left\langle
\mathfrak W_t,
\mathsf{Law}_t,
\mathfrak E_t^{\rm gen},
\mathsf{GenStep}_t
\right\rangle.
}
$$

此時任何 $\mathsf{GenStep}$ rewrite 必須由更高一層合法關係或自洽閉包規格承載。

因此：

$$
\boxed{
\text{Reflexive Generative Closure}
\neq
\text{Rulelessness}.
}
$$

是否存在非循環、非空洞的 reflexive grounding 保持 $\mathsf{OPEN}$。

---

# 7. Generative Sufficiency

對 declared generative target：

$$
\boxed{
\Omega_D^{\rm gen}
\subseteq
\Omega_D,
}
$$

定義：

$$
\boxed{
\mathsf{GenSufficient}_{D,T}
\left(
S\mid\mathfrak E^{\rm gen}
\right)
=1
}
$$

若且唯若：

$$
\boxed{
\Omega_D^{\rm gen}
\subseteq
\operatorname{GenCl}_{D,T}
\left(
S\mid\mathfrak E^{\rm gen}
\right).
}
$$

本文件固定：

$$
\boxed{
\mathsf{GenSufficient}
\not\Rightarrow
\mathsf{OntologicallyFirst}.
}
$$

生成充分性是 domain-relative coverage claim；ontological priority 需要額外 bridge。

---

# 8. Generative Responsibility Decomposition

## 8.1 Responsibility Record

對 outcome $y$ 定義：

$$
\boxed{
\mathsf{GR}(y)
=
\left\langle
S,
\mathsf{Car},
\mathsf{Law},
\mathfrak B,
\mathsf{Ops},
\mathfrak H,
\mathsf{Ext},
\mathsf{Rand},
\mathcal C^{\rm gen},
\mathsf{Wit}^{+},
\mathsf{Debt}
\right\rangle.
}
$$

其中 $\mathsf{Debt}$ 保存尚未閉合的來源、外部依賴與 grounding obligation。

## 8.2 Responsibility Hypergraph

允許以有向超圖表示生成依賴：

$$
\boxed{
\mathsf{RespGraph}(y)
=
(V_y,E_y^{\rm resp}).
}
$$

節點可以是 source、carrier、law、operator、boundary、history state、external feed 或 intermediate outcome；超邊表示在指定模型中一組 antecedents 對某結果的生成責任。

## 8.3 Accounted Resource

對必要資源 $r$，若至少存在下列之一，稱 $r$ 已被 accounted：

1. 明示 provenance；
2. declared exogenous status；
3. 下一層 responsibility record；
4. 明示 $\mathsf{OPEN}$ debt。

因此 accounted 不等於 grounded；它只表示依賴沒有被隱藏。

## 8.4 Responsibility Closure

定義：

$$
\boxed{
\mathsf{RespClosed}_{D,T}(S)=1
}
$$

若對所有被納入 sufficiency proof 的 outcome 與必要生成資源，其 dependency chain 在 declared model boundary 內全部被 accounted，且不存在未標記依賴。

若存在 $\mathsf{OPEN}$ debt，則可標記 accounted-but-open，不得標記 fully grounded。

---

# 9. Generative Responsibility Axioms

## GR-A1 — No Unaccounted Generative Resource

$$
\boxed{
\text{任何對 outcome 必要的生成資源，都必須出現在責任記錄或明示 debt 中。}
}
$$

## GR-A2 — No Source-Alone Upgrade

若：

$$
\operatorname{GenCl}_{D,T}
(S\mid\mathfrak E^{\rm gen})
$$

依賴非平凡環境，則不得省略 $\mathfrak E^{\rm gen}$ 後宣稱同等能力屬於裸 source。

## GR-A3 — Recursive Attribution

若必要資源來自更高來源 $S_{-1}$，則必須：

$$
\boxed{
S_{-1}
\in
\mathsf{DeclaredBoundary}
}
$$

或建立下一層 $\mathsf{GR}$ ；否則 grounding status 保持 $\mathsf{OPEN}$。

## GR-A4 — Accounting Is Not Ultimate Grounding

$$
\boxed{
\mathsf{RespClosed}=1
\not\Rightarrow
\mathsf{OntologicalGroundingComplete}=1.
}
$$

責任閉包先保證「沒有未記帳資源」，不保證「形上學終極來源已解決」。

---

# 10. Typed Unboundedness Taxonomy

## 10.1 Status Space

定義：

$$
\boxed{
\mathfrak U
=
\{
\mathsf{bounded},
\mathsf{open},
\mathsf{unbounded},
\mathsf{unknown}
\}.
}
$$

## 10.2 Unboundedness Profile

定義：

$$
\boxed{
\mathbf U
=
\left(
 u_{\rm state},
 u_{\rm type},
 u_{\rm relation},
 u_{\rm law},
 u_{\rm operator},
 u_{\rm time},
 u_{\rm information},
 u_{\rm ontology},
 u_{\rm reach}
\right).
}
$$

每一分量取值於 $\mathfrak U$。

## 10.3 Open Is Not Unbounded

$$
\boxed{
\mathsf{open}
\not\Rightarrow
\mathsf{unbounded}.
}
$$

 $\mathsf{open}$ 只表示未預先封閉未來 extension vocabulary 或 extension rule； $\mathsf{unbounded}$ 需要相對某 quantity / preorder 的 no-finite-upper-bound witness schema。

## 10.4 Generic Unboundedness Certificate

對量測泛函：

$$
\phi:
\Omega_D
\rightarrow
\mathbb R_{\ge 0},
$$

定義 $\phi$ -unbounded：

$$
\boxed{
\forall M<\infty,
\exists y\in
\operatorname{GenCl}_{D,T}
(S\mid\mathfrak E^{\rm gen})
:
\phi(y)>M.
}
$$

若沒有明示 $\phi$ 或 preorder，禁止使用「已證明無界」作正式結論。

## 10.5 Open-Dimensional Bridge

允許：

$$
\boxed{
\left|
J_{\rm eff}(Q,t,\varepsilon)
\right|<\infty
}
$$

同時未來 dimension vocabulary 不預先封閉。

因此：

$$
\boxed{
\text{Potentially Open}
\neq
\text{Infinitely Active at Every Instant}.
}
$$

---

# 11. Typed Reachability Calculus

## 11.1 Capability Mode Family

定義 capability modes：

$$
\boxed{
\mathfrak M_{\rm cap}
=
\{
\mathsf{observe},
\mathsf{access},
\mathsf{act},
\mathsf{control},
\mathsf{transform},
\mathsf{ruleRewrite},
\mathsf{genRewrite},
\mathsf{verify}
\}.
}
$$

這些 mode 預設只是一個 typed family，不預設固定全序。

特別地，不自動宣稱：

$$
\mathsf{observe}
<
\mathsf{access}
<
\mathsf{act}
<
\mathsf{control}.
$$

模式間蘊含必須由 domain-specific bridge theorem 或 contract 明示。

## 11.2 Reachability Judgement

對 agent $A$ 、target $x$ 、mode $m$ 、relation type $R$ 、context $\Theta$ 與時間 $t$，定義：

$$
\boxed{
\mathsf{Reach}^{m}_{\Theta,R}
(A,x,t)
\in
\mathfrak J.
}
$$

其中 judgement status：

$$
\boxed{
\mathfrak J
=
\{
1,
0,
?,
\mathsf{B},
\mathsf{S}
\}.
}
$$

語義分別為 pass、fail、unknown、branch-dependent、scope-dependent。

## 11.3 Positive Reach Witness

若：

$$
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)=1,
$$

至少需要：

$$
\boxed{
\mathsf{Wit}^{+}_{\rm reach}
=
\left\langle
\pi,
\mathfrak B_{\pi},
R_{\pi},
\mathsf{Ops}_{\pi},
\mathsf{Cond}_{\pi},
\mathsf{Cert}_{\pi}
\right\rangle,
}
$$

其中 $\pi$ 是合法 typed path 或 intervention chain。

## 11.4 Negative Reach Certificate

若要將 judgement 設為 $0$ 而非 $?$，至少需要一個 scoped negative witness，例如：

- exhaustive finite search certificate；
- cut / barrier certificate；
- violated necessary condition；
- permission impossibility certificate；
- model-checking proof；
- declared scope completeness certificate。

因此：

$$
\boxed{
\text{No path found}
\not\Rightarrow
\mathsf{Reach}=0.
}
$$

---

# 12. Reach Profile

對 agent $A$ 與 target $x$ 定義：

$$
\boxed{
\mathbf R_A(x,t\mid\Theta)
=
\left(
 r_{\rm obs},
 r_{\rm access},
 r_{\rm act},
 r_{\rm ctrl},
 r_{\rm trans},
 r_{\rm rule},
 r_{\rm gen},
 r_{\rm ver}
\right),
}
$$

其中每一分量屬於 $\mathfrak J$，並且仍需 relation / boundary witness 才能形成完整 claim。

因此：

$$
\boxed{
\text{Seeing More}
\neq
\text{Being Higher}
}
$$

被形式化為 mode separation，而不是倫理或本體等級判斷。

---

# 13. Transformation Closure

## 13.1 Transformation Contract

令 transformation $\tau$ 為帶 contract 的部分映射：

$$
\boxed{
\tau:
X_{\rm pre}
\rightharpoonup
X_{\rm post}.
}
$$

每個 transformation 至少帶：

$$
\boxed{
\mathsf{Contract}(\tau)
=
\left\langle
\mathsf{Pre},
\mathsf{Post},
\mathsf{Inv},
\mathsf{Boundary},
\mathsf{Auth},
\mathsf{Verify}
\right\rangle.
}
$$

## 13.2 Realized Transformation Judgement

定義：

$$
\boxed{
\mathsf{RealizeTrans}_{\Theta}
(A,\tau,x,t)
\in
\mathfrak J.
}
$$

其中 pass 需要 action / state delta / outcome / verification witness。

## 13.3 Transformation Closure

定義：

$$
\boxed{
\operatorname{TransCl}_{D,T}
(A\mid\Theta)
=
\left\{
(x,\tau)
\;\middle|\;
 x\in\Omega_D,
 \exists t\le T:
 \mathsf{RealizeTrans}_{\Theta}(A,\tau,x,t)=1
\right\}.
}
$$

此物件回答「對哪些 target，可實現哪些 transformation」，不等同於 target reach set。

因此：

$$
\boxed{
\mathsf{Reach}^{\mathsf{transform}}=1
\not\Rightarrow
\text{all transformations are realizable}.
}
$$

---

# 14. Realizability Interface

UGC/CUR 不重造完整 Realizability theory。

定義 adapter：

$$
\boxed{
\mathsf{Realizable}_{\Theta}
(A,\tau,x,t)
}
$$

由既有 Realizability layer 判定 physical、engineering、normative、reversible、verifiable 等條件。

固定：

$$
\boxed{
\mathsf{Connectivity}
\neq
\mathsf{Reachability}
\neq
\mathsf{Realizability}.
}
$$

以及：

$$
\boxed{
\mathsf{Reach}=1
\not\Rightarrow
\mathsf{Realizable}=1.
}
$$

---

# 15. Meta-Causal Hierarchy

Meta-causality 一律相對某 baseline layer $L$ 定義。

## MC0 — Ordinary State Intervention

只改變 ordinary state：

$$
\boxed{
\mathfrak W_t
\rightarrow
\mathfrak W_{t+1}.
}
$$

## MC1 — Relation / Boundary / Causal-Topology Rewrite

至少改變：

$$
\boxed{
(\mathfrak R_t,\mathfrak B_t)
\rightarrow
(\mathfrak R_{t+1},\mathfrak B_{t+1}).
}
$$

## MC2 — Transition Rule / Operator Rewrite

至少改變：

$$
\boxed{
\mathsf{Ops}_t
\rightarrow
\mathsf{Ops}_{t+1}
}
$$

或 object-level transition contract。

## MC3 — Law-Regime Update

至少改變：

$$
\boxed{
\mathsf{Law}_t
\rightarrow
\mathsf{Law}_{t+1}.
}
$$

## MC4 — Generative-Rule / Meta-Law Rewrite Candidate

至少改變：

$$
\boxed{
\mathsf{GenStep}_t
\rightarrow
\mathsf{GenStep}_{t+1}
}
$$

或其 meta-law specification。

定義 certified meta-causal level：

$$
\boxed{
\mathsf{MCLevel}_{D,T,\Theta}(A\mid L)
=
\max
\left\{
k:\mathsf{Wit}^{+}_{\mathsf{MC}_k}(A)\text{ exists}\right\}.
}
$$

若最大值不存在或 scope 未閉合，回傳 $?$。

本文件固定：

$$
\boxed{
\mathsf{MC}_k
\not\Rightarrow
\text{absolute transcendence of all law}.
}
$$

---

# 16. Class-Ultimate Capability

## 16.1 Required Mode and Relation Sets

令：

$$
\boxed{
\mathcal M^{\star}
\subseteq
\mathfrak M_{\rm cap}
}
$$

與：

$$
\boxed{
\mathfrak R^{\star}
\subseteq
\mathfrak R.
}
$$

## 16.2 Typed Coverage

定義：

$$
\boxed{
\mathsf{Coverage}_{D,T}
(A)
=
\left\{
(x,m)
\in
\Omega_D\times\mathcal M^{\star}
\;\middle|\;
\exists t\le T,
\exists R\in\mathfrak R^{\star}:
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)=1
\right\}.
}
$$

## 16.3 Class-Ultimate Candidate

若：

$$
\boxed{
\mathsf{Coverage}_{D,T}(A)
=
\Omega_D\times\mathcal M^{\star},
}
$$

且每一個 pass 都有 witness，則：

$$
\boxed{
\mathsf{ClassUltimateCandidate}
\left(
A\mid
D,T,\mathcal M^{\star},\mathfrak R^{\star},\Theta
\right).
}
$$

若 $\mathcal M^{\star}$ 只包含 $\mathsf{observe}$，得到 observation-ultimate candidate，而不是 total-capability ultimate。

## 16.4 Transformation-Complete Candidate

對 declared transformation class $\mathcal T^{\star}$，若：

$$
\boxed{
\Omega_D\times\mathcal T^{\star}
\subseteq
\operatorname{TransCl}_{D,T}(A\mid\Theta),
}
$$

可稱 transformation-complete candidate relative to $\mathcal T^{\star}$。

這仍不推出 ontological priority 或 absolute omnipotence。

---

# 17. Canonical Ledger Minimum Specification

定義：

$$
\boxed{
\mathsf{Ledger}_t
=
\left\langle
\mathfrak W_t,
\mathfrak H_{\le t},
\mathfrak P^{\rm causal}_{\le t},
\mathsf{LawLog}_{\le t},
\mathsf{BoundaryLog}_{\le t},
\mathsf{InfoAcct}_{\le t},
\mathsf{RespAcct}_{\le t},
\mathsf{Cert}_{\le t},
\mathsf{Debt}_{\le t}
\right\rangle.
}
$$

其中：

- $\mathfrak P^{\rm causal}_{\le t}$：causal provenance / partial order；
- $\mathsf{InfoAcct}_{\le t}$：retain / transform / compress / loss / unresolved / external accounting；
- $\mathsf{RespAcct}_{\le t}$：Generative Responsibility records；
- $\mathsf{Debt}_{\le t}$：未閉合 proof / source / grounding obligations。

## 17.1 Local Projection

observer 只得到：

$$
\boxed{
\mathsf{LocalLedger}_{o,\Theta}(t)
=
\Pi_{o,\Theta}
\left(
\mathsf{Ledger}_t
\right).
}
$$

因此：

$$
\boxed{
\mathsf{LocalLedger}
\neq
\mathsf{Ledger}.
}
$$

## 17.2 Accounting Discipline

核心只要求：

$$
\boxed{
\mathsf{Output}
\Rightarrow
\mathsf{Source/Transform/External/Loss/Unresolved\ Accounting}.
}
$$

本文件不把：

$$
\mathcal I(\mathsf{Ledger}_t)
=
\mathcal I(\mathsf{Ledger}_0)
$$

設為公理。

因此：

$$
\boxed{
\text{local information loss}
\not\Rightarrow
\text{global information destruction},
}
$$

同時：

$$
\boxed{
\text{local information loss}
\not\Rightarrow
\text{global information preservation}.
}
$$

兩個方向都不得偷渡。

---

# 18. First-Cause Sufficiency Test

本文件使用 `First-Cause Sufficiency Test`，縮寫：

$$
\boxed{
\mathsf{FCS}.
}
$$

它不是「證明上帝」或「證明絕對第一因」的測試，而是對 first-cause candidate 的結構充分性與責任閉包進行分層判定。

## 18.1 Input Record

對候選 $S_0$：

$$
\boxed{
\mathsf{FCSInput}
=
\left\langle
S_0,
\Omega_D^{\rm gen},
T,
\Theta,
\mathfrak E^{\rm gen},
\mathbf U,
\mathsf{GR},
\mathsf{CompCert}
\right\rangle.
}
$$

## 18.2 Test Vector

定義：

$$
\boxed{
\mathbf F_{\rm CS}
=
\left(
 f_{\rm typed},
 f_{\rm cover},
 f_{\rm resp},
 f_{\rm hidden},
 f_{\rm law},
 f_{\rm carrier},
 f_{\rm ext},
 f_{\rm unbound},
 f_{\rm comp},
 f_{\rm priority}
\right).
}
$$

各分量分別檢查：

1. target / source / environment 是否 well-typed；
2. generative sufficiency 是否成立；
3. responsibility 是否閉合或已明示 debt；
4. 是否存在 hidden higher source；
5. law grounding status；
6. carrier grounding status；
7. external input / randomness / oracle status；
8. 若 target claim 涉及 unboundedness，是否具有相容的 typed certificate；
9. scope completeness；
10. ontological priority bridge。

## 18.3 FCS Levels

定義最低分級：

$$
\boxed{
\begin{aligned}
\mathsf{FCS}_0 &: \text{ill-typed / scope undefined},\\
\mathsf{FCS}_1 &: \text{generatively insufficient},\\
\mathsf{FCS}_2 &: \text{conditionally generatively sufficient},\\
\mathsf{FCS}_3 &: \text{responsibility-closed first-cause candidate},\\
\mathsf{FCS}_4 &: \text{ontological-priority candidate with explicit bridge obligations}.
\end{aligned}
}
$$

 $\mathsf{FCS}_4$ 仍不是 automatic proof of absolute first cause。

若 completeness 或 ontological bridge 未證，status 保持 scope-relative 或 $\mathsf{OPEN}$。

---

# 19. First Cause and Absolute Nothingness Decoupling

本核心不以 creation-from-absolute-nothing 作為 generative sufficiency 的必要前提。

固定：

$$
\boxed{
\mathsf{FirstCauseSufficiency}
\perp
\mathsf{AbsoluteNothingnessThesis}.
}
$$

第一因候選的最低生成問題只要求：

$$
\boxed{
\Omega_D^{\rm gen}
\subseteq
\operatorname{GenCl}_{D,T}
(S_0\mid\mathfrak E^{\rm gen}).
}
$$

不要求先證明某個 ordinary state：

$$
\mathrm{AbsoluteNothingness}
$$

曾經存在。

本核心同時保留 typed negative-state discipline：zero、empty、undefined、absent、inaccessible、nondenoting、unknown 不得互換。

---

# 20. Local-to-Absolute Gate

UGC/CUR 直接採用：

$$
\boxed{
\mathcal G_{\rm LA}.
}
$$

對 local claim $P_{\Theta,D}$ 與 absolute candidate $P_{\rm abs}$，只允許：

$$
\boxed{
P_{\Theta,D}
\xRightarrow{\mathcal G_{\rm LA}}
P_{\rm abs}
}
$$

若至少具備：

$$
\boxed{
\mathsf{CompCert}(\Theta,D,P)=1
}
$$

以及足以覆蓋缺失作用域的 bridge witness。

典型禁止：

$$
\boxed{
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)=0
\not\Rightarrow
\mathsf{AbsoluteUnreachability}(A,x),
}
$$

$$
\boxed{
\mathsf{GenSufficient}_{D,T}=1
\not\Rightarrow
\mathsf{AbsoluteFirstCause},
}
$$

$$
\boxed{
\mathsf{MC}_4
\not\Rightarrow
\text{transcendence of all possible meta-law}.
}
$$

---

# 21. Formal Core Axioms / Protocol Invariants

以下皆為 UGC/CUR formal protocol axioms，不宣稱為宇宙先驗真理。

## FC-A1 — Type Before Claim

任何 claim 在判真前先確定 domain、context、relation、mode 與 horizon。

## FC-A2 — Witness Before Positive Upgrade

$$
\boxed{
J=1
\Rightarrow
\exists\mathsf{Wit}^{+}.
}
$$

## FC-A3 — Negative Claim Requires Scoped Obstruction

$$
\boxed{
J=0
\Rightarrow
\exists\mathsf{Wit}^{-}_{\rm scoped}.
}
$$

## FC-A4 — State / History / Law / Ledger Separation

$$
\boxed{
\mathfrak W_t
\neq
\mathfrak H_{\le t}
\neq
\mathsf{Law}_t
\neq
\mathsf{Ledger}_t.
}
$$

## FC-A5 — No Unaccounted Generative Resource

任何必要生成資源必須出現在 responsibility accounting 或 debt 中。

## FC-A6 — Boundary Is Active Structure

邊界不自動等於斷裂，也不自動等於可通過。

## FC-A7 — Open Is Not Unbounded

$$
\boxed{
\mathsf{open}
\neq
\mathsf{unbounded}.
}
$$

## FC-A8 — Connectivity / Reachability / Realizability Separation

$$
\boxed{
\mathsf{Connectivity}
\neq
\mathsf{Reachability}
\neq
\mathsf{Realizability}.
}
$$

## FC-A9 — Observation / Transformation Separation

$$
\boxed{
\mathsf{observe}
\neq
\mathsf{transform}.
}
$$

## FC-A10 — Capability Modes Are Not Globally Totally Ordered

任何 mode implication 都需要 domain-specific bridge。

## FC-A11 — Meta-Causality Is Layer-Relative

$$
\boxed{
\mathsf{MC}_k
\not\Rightarrow
\text{absolute law transcendence}.
}
$$

## FC-A12 — Ledger Accounting Is Not Information Conservation

provenance accounting 不等於某個全域 scalar information invariant。

## FC-A13 — No Local-to-Absolute Promotion Without Gate

任何 absolute upgrade 必須通過 $\mathcal G_{\rm LA}$。

## FC-A14 — First Cause and Class-Ultimate Are Distinct

$$
\boxed{
\mathsf{FirstCauseCandidate}
\neq
\mathsf{ClassUltimateCandidate}.
}
$$

## FC-A15 — Accounting Is Not Ontological Completion

responsibility closure、ledger completeness 或 model completeness 都不自動等於 metaphysical completion。

---

# 22. Derived Propositions

## Proposition P1 — Horizon Monotonicity Under Fixed Transition Semantics

若 $T_1\le T_2$，且 $\mathsf{Init}$ 、 $\mathsf{GenStep}$ 、admissibility 與 environment semantics 在兩個 horizon 間不變，且合法 trace 具有 prefix-extension closure，則：

$$
\boxed{
\operatorname{GenCl}_{D,T_1}
(S\mid\mathfrak E^{\rm gen})
\subseteq
\operatorname{GenCl}_{D,T_2}
(S\mid\mathfrak E^{\rm gen}).
}
$$

此命題不適用於 horizon 改變同時改變規則、權限或 admissibility 的情況。

## Proposition P2 — Fixed-Law Closure Is a Special Case

若：

$$
\mathsf{Law}_t=\mathsf{Law}_0
\qquad
\forall t\le T,
$$

則 law-coevolving generative model 退化為 fixed-law model。

## Proposition P3 — Source-Alone Inference Is Invalid Under Essential Environment Dependence

若存在 outcome $y$，且 $y$ 的所有 positive generation witnesses 都使用非平凡環境資源 $r\in\mathfrak E^{\rm gen}$，則只由 $S$ 不足以證明同一生成 claim。

因此：

$$
\boxed{
\mathsf{EssentialEnvDep}(y)
\Rightarrow
\neg\mathsf{SourceAloneProof}(S\Rightarrow y).
}
$$

## Proposition P4 — Observation-Ultimate Does Not Imply Transformation-Complete

若：

$$
\mathcal M^{\star}=\{\mathsf{observe}\},
$$

則 class-ultimate coverage 只證明 observation-relative coverage，不提供：

$$
\Omega_D\times\mathcal T^{\star}
\subseteq
\operatorname{TransCl}_{D,T}(A\mid\Theta).
$$

## Proposition P5 — Local Ledger Projection Is Generally Non-Invertible

若 observer projection $\Pi_{o,\Theta}$ 非單射，則存在不同 global ledger states 對應相同 local view；因此：

$$
\boxed{
\Pi_{o,\Theta}^{-1}
}
$$

一般不保證唯一存在。

## Proposition P6 — Responsibility Closure Does Not Eliminate Grounding Regress by Definition

即使 $\mathsf{RespClosed}=1$，只要最外層資源被標記為 declared exogenous 或 $\mathsf{OPEN}$，仍不能推出 ontological regress 已終止。

---

# 23. Proof Obligation Matrix

| ID | Obligation | Minimal Requirement | Current Status |
| --- | --- | --- | --- |
| PO-01 | Target domain well-typed | $\Omega_D$ + scope declaration | $\mathsf{DEF}$ |
| PO-02 | Judgement context explicit | $\Theta$ | $\mathsf{DEF}$ |
| PO-03 | Positive generation claim | trace + provenance | $\mathsf{DEF}$ |
| PO-04 | Negative generation claim | scoped obstruction / completeness | $\mathsf{OPEN}$ generally |
| PO-05 | Generative sufficiency | coverage proof over $\Omega_D^{\rm gen}$ | $\mathsf{MODEL}$ / $\mathsf{OPEN}$ |
| PO-06 | Responsibility accounting | $\mathsf{GR}$ for essential resources | $\mathsf{DEF}$ |
| PO-07 | Ultimate grounding | no hidden higher source + bridge | $\mathsf{OPEN}$ |
| PO-08 | Unboundedness | quantity / preorder + certificate schema | $\mathsf{OPEN}$ by dimension |
| PO-09 | Positive reachability | typed path witness | $\mathsf{DEF}$ |
| PO-10 | Negative reachability | scoped negative witness | $\mathsf{OPEN}$ generally |
| PO-11 | Capability-mode implication | domain-specific bridge theorem | $\mathsf{OPEN}$ |
| PO-12 | Transformation realization | contract + state delta + verify witness | $\mathsf{DEF}$ |
| PO-13 | Meta-causal level | witness of rewritten layer | $\mathsf{DEF}$ |
| PO-14 | MC4 grounding | meta-law / reflexive closure grounding | $\mathsf{OPEN}$ |
| PO-15 | Class-ultimate coverage | complete target-mode coverage + witnesses | $\mathsf{OPEN}$ generally |
| PO-16 | Global ledger existence | coherent global or gluable ledger construction | $\mathsf{OPEN}$ outside declared models |
| PO-17 | Global information invariant | explicit invariant + proof | $\mathsf{OPEN}$ |
| PO-18 | Local-to-absolute promotion | $\mathsf{CompCert}$ + bridge witness | $\mathsf{OPEN}$ generally |
| PO-19 | Absolute first cause | FCS + ontological priority bridge | $\mathsf{OPEN}$ |
| PO-20 | Absolute nothingness | separate ontology / semantics | outside core requirement |

---

# 24. FCS Evaluation Matrix

對 first-cause candidate $S_0$，正式報告不得只輸出 true / false，而應至少輸出：

| Field | Meaning |
| --- | --- |
| `typed_scope` | source、domain、horizon、environment 是否明確 |
| `generative_coverage` | $\Omega_D^{\rm gen}$ 是否被覆蓋 |
| `responsibility_status` | essential resources 是否 accounted |
| `hidden_source_status` | 是否發現未宣告 higher source |
| `carrier_grounding` | carrier 的來源與角色 |
| `law_grounding` | law / rule regime 的來源與狀態 |
| `external_dependency` | oracle / randomness / external feed |
| `unboundedness_profile` | 各 typed dimension 狀態 |
| `completeness_status` | 是否有 $\mathsf{CompCert}$ |
| `ontological_priority` | 是否存在獨立 bridge |
| `fcs_level` | $\mathsf{FCS}_0$ -- $\mathsf{FCS}_4$ |
| `open_debts` | 未閉合 proof obligations |

---

# 25. Canonical Runtime Records

## 25.1 Generative Closure Claim

```yaml
GenerativeClosureClaim:
  source: null
  target_domain: null
  horizon: null
  judgement_context: null
  generative_environment: null
  closure_kind: fixed_law | law_coevolving | reflexive
  coverage_status: unknown
  positive_witnesses: []
  negative_witnesses: []
  responsibility_records: []
  unboundedness_profile: {}
  open_debts: []
  claim_status: OPEN
```

## 25.2 Reachability Claim

```yaml
ReachabilityClaim:
  agent: null
  target: null
  mode: null
  relation_type: null
  boundary_state: null
  judgement_context: null
  horizon: null
  status: "?"
  positive_witness: null
  negative_witness: null
  completeness_certificate: null
```

## 25.3 Transformation Claim

```yaml
TransformationClaim:
  agent: null
  target: null
  transformation: null
  contract: null
  judgement_context: null
  horizon: null
  realizability_profile: null
  status: "?"
  witness: null
  verification: null
```

## 25.4 First-Cause Sufficiency Claim

```yaml
FirstCauseSufficiencyClaim:
  source: null
  target_domain: null
  horizon: null
  generative_environment: null
  generative_sufficiency: unknown
  responsibility_closure: unknown
  hidden_source_status: unknown
  carrier_grounding: OPEN
  law_grounding: OPEN
  external_dependency_status: unknown
  unboundedness_profile: {}
  completeness_certificate: null
  ontological_priority_bridge: null
  fcs_level: FCS0
  open_debts: []
```

---

# 26. Canonical Compact Kernel

本文件完成後，UGC/CUR formal core 固定為：

$$
\boxed{
\mathsf{Kernel}^{\rm UGC/CUR}
=
\left\langle
\Omega_D,
T,
\Theta,
\mathfrak W_t,
\mathfrak H_{\le t},
\mathsf{Law}_t,
\mathfrak B_t,
\mathfrak R_t,
\mathfrak E_t^{\rm gen},
\operatorname{GenCl},
\mathsf{GR},
\mathbf U,
\mathsf{Reach},
\operatorname{TransCl},
\mathsf{MCLevel},
\mathsf{Ledger},
\mathsf{FCS},
\mathsf{Wit},
\mathsf{CompCert},
\mathcal G_{\rm LA}
\right\rangle.
}
$$

其四個主要問題為：

$$
\boxed{
\begin{aligned}
Q_G &: \text{What can this declared source-plus-environment generate?}\\
Q_R &: \text{What can this agent reach, under which capability mode and relation?}\\
Q_T &: \text{Which transformations can this agent actually realize?}\\
Q_A &: \text{Where are the necessary resources, state changes and unresolved debts accounted for?}
\end{aligned}
}
$$

第一因問題是 $Q_G+Q_A$ 再加 ontological-priority bridge；類終極問題是 $Q_R+Q_T$ 再加 meta-causal level 與 coverage condition。

---

# 27. Canonical Non-Equivalences

後續文件至少保留：

$$
\boxed{
\begin{aligned}
\mathsf{Observation} &\neq \mathsf{Existence},\\
\mathsf{Representation} &\neq \mathsf{Ontology},\\
\mathsf{Boundary} &\neq \mathsf{Disconnection},\\
\mathsf{Difference} &\neq \mathsf{Disconnection},\\
\mathsf{Connectivity} &\neq \mathsf{Reachability},\\
\mathsf{Reachability} &\neq \mathsf{Realizability},\\
\mathfrak W_t &\neq \mathfrak H_{\le t},\\
\mathsf{WorldState} &\neq \mathsf{ObserverView},\\
\mathsf{LawChange} &\neq \mathsf{ObserverModelChange},\\
\mathsf{Open} &\neq \mathsf{Unbounded},\\
\mathsf{GenSufficient} &\neq \mathsf{OntologicallyFirst},\\
\mathsf{ClassUltimate} &\neq \mathsf{FirstCause},\\
\mathsf{RespClosed} &\neq \mathsf{UltimateGrounding},\\
\mathsf{MC}_4 &\neq \mathsf{AbsoluteLawTranscendence}.
\end{aligned}
}
$$

---

# 28. Preserved Open Problems

以下問題不得由 Formal Core v0.1 假裝解決：

1. 是否存在 metaphysically complete $\Omega_D$ ；
2. foundational law 是否固定、演化、湧現或具有其他形式；
3. reflexive generative closure 是否存在非循環、非空洞 grounding；
4. 是否存在 universal carrier；
5. 是否存在跨 relevant domains 的 completeness certificate；
6. 是否存在可辯護的 global information invariant；
7. class-ultimate coverage 是否能在 open world 中完成證明；
8. meta-causal rewrite 是否存在 finite ceiling；
9. 不可計算或不可觀測生成資源如何進行完整 responsibility closure；
10. absolute first cause 是否是可判定、可驗證、甚至在某 explanation operator 的定義域內；
11. open-dimensionality 在何種條件下升格為 mathematical unboundedness；
12. local ledgers 是否能唯一黏合成 global ledger；
13. capability modes 之間是否存在 domain-independent partial order；
14. transformation closure 在 law-coevolving world 中應採何種 equivalence relation；
15. $\mathsf{FCS}_4$ 以上是否存在合理、非循環的更高分級。

---

# 29. Migration from Canonical Reconciliation

本文件不推翻 Reconciliation v0.1，而是增加可推演定義。

| Reconciliation object | Formal Core object | Decision |
| --- | --- | --- |
| $\operatorname{GenCl}_{D,T}(S\mid\mathfrak E^{\rm gen})$ | trace-based $\operatorname{GenCl}$ | formalized |
| Generative Responsibility | $\mathsf{GR}(y)$ + $\mathsf{RespGraph}(y)$ | formalized |
| typed reachability | $\mathsf{Reach}^{m}_{\Theta,R}$ + witness semantics | formalized |
| reach profile | $\mathbf R_A$ | preserved |
| meta-causal levels | $\mathsf{MCLevel}_{D,T,\Theta}(A\mid L)$ | formalized |
| class-ultimate candidate | typed coverage + optional transformation completeness | strengthened |
| Global Ledger | ledger + responsibility accounting + debt | strengthened |
| FirstCauseCandidate | $\mathsf{FCS}$ evaluation | operationalized |
| open / unbounded | $\mathbf U$ + generic unboundedness certificate | strengthened |
| local-to-absolute gate | $\mathcal G_{\rm LA}$ + $\mathsf{CompCert}$ | preserved |

---

# 30. Paper Release Sequence

完成 Formal Core 後，後續正式系列採：

$$
\boxed{
00
\rightarrow
01
\rightarrow
02
\rightarrow
03
\rightarrow
04
\rightarrow
05.
}
$$

其中：

- **Paper 00 — Formal Core Specification**：本文件；
- **Paper 01 — Unbounded Ontological Extension**：無界／開放展開、有限邊界與 OBRC 負狀態限制；
- **Paper 02 — Generative Closure and First-Cause Sufficiency**：生成閉包、生成責任、first-cause candidate 與 FCS；
- **Paper 03 — Global Ledger and Generative Accounting**：state / history / provenance / information / responsibility accounting；
- **Paper 04 — Typed Class-Ultimate Reachability**：typed reach、cross-layer channel、coverage；
- **Paper 05 — Transformation Closure and Meta-Causal Agency**：transformation closure、rule rewrite、law rewrite 與 relative meta-causality。

任何 Paper 01--05 若要偏離本文件 primitive，必須先新增 ADR / canonical amendment，而不是在正文內靜默改義。

---

# 31. Final Formal-Core Statement

UGC/CUR v0.1 formal core 最終固定：

$$
\boxed{
\begin{aligned}
&\text{一個來源的能力不能只由裸 source 表示，而必須相對生成環境、作用域與責任鏈；}\\
&\text{一個作用者的能力不能只由裸 reach set 表示，而必須區分 capability mode 與 transformation class；}\\
&\text{一個 meta-causal claim 只能相對被改寫的層級成立，不能偷渡成絕對超越所有 law；}\\
&\text{一個 first-cause claim 必須先通過生成充分性與責任閉包，再另行處理 ontological priority；}\\
&\text{任何 local claim 若要升格 absolute claim，必須通過 local-to-absolute gate。}
\end{aligned}
}
$$

因此，本系列的形式問題不再是：

> 「某來源是不是無限？」或「某存在是不是全能？」

而是：

$$
\boxed{
\begin{aligned}
&\text{在明示 world、law、carrier、boundary、history、observer、resource 與 evidence 條件下，}\\
&\text{什麼可以被生成，什麼可以被抵達，什麼可以被改寫，}\\
&\text{這些能力需要哪些資源，以及哪些 claim 仍然沒有資格被提升為 absolute。}
\end{aligned}
}
$$

**END OF CANONICAL FORMAL CORE v0.1**
