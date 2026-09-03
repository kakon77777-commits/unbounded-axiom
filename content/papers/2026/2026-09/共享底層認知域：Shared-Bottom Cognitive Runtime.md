# CODT-04
# 共享底層認知域：Shared-Bottom Cognitive Runtime
## Shared-Bottom Cognitive Runtime: Cross-Program Substrates Beyond Cognitive Taxonomy

**系列：** Cognitive Operator-Domain Theory, CODT / 認知算子-域理論  
**系列篇次：** 04 / 10  
**版本：** v1.0  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  
**文件性質：** 理論論文 / Shared-Bottom Runtime 篇  
**前篇：** CODT-03〈認知域的生成：域不是分類名稱，而是算子閉包與操作生態〉

---

## 摘要

CODT-03 已將認知域定義為由 legal operator ecology 後生的作用結構，而不是人類預先命名的分類盒子。本文進一步處理一個更難的問題：在 operator recovery 過程中，某些作用反覆出現在多個歷史方法、程序與候選域中，例如 Attention、Search、Generation、Representation、Proxy/Operationalization、Belief/Uncertainty、Decision、Planning、Action Preparation 與 Meta-Observation。這些高重用作用究竟應被視為「更底層的認知域」、認知 infrastructure、跨域 substrate，還是另一個與 domain 軸正交的結構？

本文提出 **Shared-Bottom Cognitive Runtime, SBCR**。其核心主張不是「所有 cognition 最終都能被還原成十個固定模組」，而是：若某一 operator family 在多個彼此不同的高階 cognitive programs 中反覆出現，而且具有可重用、可型別化、可獨立失效、可獨立測試與可跨語境部署的結構，則它可以取得 shared-bottom candidate 地位：

$$
\boxed{
\exists U
[
U\in Decompose(M_a)
\cap
Decompose(M_b)
]
\land
Reuse(U)\geq\tau_R
\Rightarrow
CandidateSharedBottom(U).
}
$$

然而：

$$
\boxed{
SharedBottom_t(U)
\not\Rightarrow
Atomic(U)
}
$$

且：

$$
\boxed{
SharedBottom(U)
\not\Rightarrow
Domain(U).
}
$$

shared-bottom 描述的是**跨 program 重用軸**，domain 描述的是**operational ecology / closure 軸**。兩者可以重疊，但不可預設同一。本文因此建立一個二軸結構：Domain Axis 與 Shared-Bottom Axis。某些 shared-bottom families 可能形成自己的 domain candidates；某些則更接近 infrastructure、control plane、bridge layer 或 boundary interface。

本文重構十個 shared-bottom families：ATT、SRH、GEN、REP、PRX、BEL、DEC、PLN、ACT、MET，並將舊認知解構學方法重寫成 over-SBCR program topologies。例如 OPS 可暫時分析為 ATT+REP+ABS+DEF+NEG+MEM+MET，CRE 可分析為 MET+ATT+DEC+PLN+SRH，而 PSM 則依賴 ABD+GEN+SRH+CAU+CF+REF+VER+BEL+MET。這些表示是 dependency hypotheses，而非最終等式。

本文同時引入 **Infrastructure Test**、**Cross-Program Reuse Test**、**Substitutability Test**、**Boundary Independence Test** 與 **Domain Independence Test**，用來區分 shared-bottom substrate 和普通高頻 operator。本文最後提出：認知架構不應只由「域」組成，而應至少區分 Domain Ecology、Shared-Bottom Runtime、Meta-Control 與 World Boundary。這為下一篇 Flow-Atlas Separation 提供基礎：如果 shared-bottom substrate 被錯認成 domain，runtime transition flow 與 atlas geometry 都會被系統性誤解。

---

## 關鍵詞

Shared-Bottom Cognitive Runtime；CODT；認知算子；shared substrate；attention；search；generation；representation；belief；decision；planning；metacognition；cognitive architecture；domain ecology

---

# 1. 問題：高重用不等於高本體地位

CODT-03 已經建立：

$$
\boxed{
Domain
=
\text{derived operational structure}.
}
$$

但 domain emergence 實驗在更早階段就暴露另一種結構。

有些 operators 並不穩定地「屬於某一個方法」。

相反，它們像基礎設施一樣被不同方法反覆使用。

例如：

- Observation 需要 Attention；
- Search 需要 Attention；
- Memory Retrieval 需要 Search；
- Abduction 需要 Search 與 Generation；
- Planning 需要 Search、Decision 與 Belief；
- PSM 需要 Generation、Causal Modeling、Refutation、Belief 與 Meta-Observation；
- CRE 本身更像 Meta-Control + Decision + Planning + Search；
- CDSL 需要 Representation Bridge、Abstraction、Analogy 與 Verification。

如果我們仍然堅持：

> 每個重要 operator 都必須有且只有一個 domain 歸屬，

就會面臨兩種壞解。

第一種是把 Attention 塞回 Observation Domain。

第二種是建立一個巨大「General Cognition Domain」，把所有跨域機制全丟進去。

CODT 都拒絕。

真正問題是：

$$
\boxed{
\text{Cross-Program Reuse}
\neq
\text{Domain Membership}.
}
$$

---

# 2. Shared-Bottom 的歷史來源不是「十個新模組」

CDD Phase 0.2 曾暴露十個缺口：

$$
Search,
Generation,
Attention,
Representation,
Proxy,
Belief,
Decision,
Planning,
Action,
MetaObservation.
$$

Phase 0.3 隨後恢復十個 shared-bottom families：

| Prefix | Family | Phase 0.3 的核心用途 |
|---|---|---|
| `ATT` | Attention / Selection | alert、orient、gate、sustain 等 selection/control |
| `SRH` | Search / Explore / Query | bounded search substrate |
| `GEN` | Generate / Mutate / Perturb | seed、mutate、perturb、recombine、sample |
| `REP` | Representation / Translation / Bridge | representation space、transform、projection、preservation |
| `PRX` | Proxy / Operationalization | abstract target 到 observable proxy 的可審計接口 |
| `BEL` | Belief / Uncertainty | evidence support、update、normalization、alternative preservation |
| `DEC` | Decision / Preference | choice、evaluation、aggregation、selection、deferral |
| `PLN` | Planning / Goal / Constraint | goal、constraint、dependency、budget、monitor、replan |
| `ACT` | Action Intent / Boundary | cognition 到 ActionRequest 的準備層 |
| `MET` | Meta-Observation / Self-Audit | runtime monitoring、uncertainty、stuckness、control signal |

這十族不應被理解成：

$$
\boxed{
\text{the final ten atoms of cognition}.
}
$$

Phase 0.3 當時已經明確保留：

$$
SharedBottom_t(U)
\not\Rightarrow
Atomic(U).
$$

所以 CODT-04 的任務不是把舊 20 模組換成新 10 模組。

真正任務是定義：

> 什麼叫 shared-bottom？

---

# 3. Shared-Bottom Candidate

令：

$$
M_a,M_b
$$

為兩個高階 cognitive programs。

令：

$$
Decompose(M)
$$

表示在目前 operator language 下，該 program 的合法 decomposition。

若：

$$
U
\in
Decompose(M_a)
\cap
Decompose(M_b),
$$

只代表共享一次。

這還不夠。

因此本文加入 cross-program reuse：

$$
R(U)
=
|
\{
M_i
:
U\in Decompose(M_i)
\}
|.
$$

若：

$$
R(U)
\geq
\tau_R,
$$

且 U 在不同 program 中不是純名稱重複，而具有穩定 type / boundary / execution semantics，則：

$$
\boxed{
CandidateSharedBottom(U).
}
$$

更完整地：

$$
\boxed{
SB(U)
=
f(
Reuse,
TypeStability,
InterfaceStability,
IndependentFailure,
CrossContextTransfer,
Testability
).
}
$$

Shared-bottom 不是只看 frequency。

---

# 4. Shared-Bottom 與 Primitive 必須分離

一個 shared-bottom operator 可能很底層。

但：

$$
\boxed{
SharedBottom
\not\Rightarrow
Primitive.
}
$$

原因至少有三個。

第一，高 reuse 可能只是 operator 太粗。

例如早期的 `Attend` 很常用，卻後來被拆成：

$$
SetAlertState,
OrientFocus,
GateInput,
SustainFocus.
$$

第二，高 reuse 可能來自 infrastructure role，而不是原子性。

第三，新 instrumentation 可以讓先前不可分的作用再次被拆解。

因此：

$$
\boxed{
AtomicityAxis
\neq
ReuseAxis.
}
$$

這是本文第一個正交分離。

---

# 5. Shared-Bottom 與 Domain 也必須分離

Domain candidate 在 CODT-03 中主要由：

- legal closure；
- recurrent words；
- boundary；
- failure coherence；
- prediction；
- compression；
- stability；

形成。

Shared-bottom candidate 主要由：

- cross-program reuse；
- common interface；
- reusable type contract；
- cross-context portability；

形成。

因此：

$$
\boxed{
SharedBottomAxis
\perp
DomainAxis
}
$$

這裡：

$$
\perp
$$

只表示 conceptual orthogonality，不是線性代數內積定義。

可能出現四種情況。

## 5.1 高 Shared-Bottom，高 Domain-Likeness

例如 Search 可能既是很多 program 的 substrate，又能形成相對穩定的 search ecology。

## 5.2 高 Shared-Bottom，低 Domain-Likeness

例如某些 generic representation conversion 或 logging / tracing mechanism 可能跨所有 cognition 使用，卻沒有形成獨立 domain boundary。

## 5.3 低 Shared-Bottom，高 Domain-Likeness

某些高度專門的 causal-modeling region 可能只在少數方法中使用，但自身形成很穩定 domain。

## 5.4 低 Shared-Bottom，低 Domain-Likeness

一般 candidate operator 或局部 specialization。

因此：

$$
\boxed{
\text{shared}
\neq
\text{domain}.
}
$$

---

# 6. 二軸表示

令：

$$
s_i
=
SharedBottomScore(\Omega_i)
$$

以及：

$$
d_{i\alpha}
=
DomainMembership(
\Omega_i,
\mathfrak D_\alpha
).
$$

則每個 operator 至少具有：

$$
\boxed{
(\Omega_i,s_i,\mathbf d_i).
}
$$

其中：

$$
\mathbf d_i
=
(
d_{i1},
\ldots,
d_{im}
).
$$

這表示：

- shared-bottom 是 operator 的跨 program 重用 profile；
- domain membership 是其在不同 operational regions 中的 derived profile。

兩者不再互相偷渡。

---

# 7. SBCR：Shared-Bottom Cognitive Runtime

本文將所有 active shared-bottom candidates、其 type contracts、runtime interfaces 與 resource policies 暫寫成：

$$
\boxed{
\mathcal S_t
=
(
\mathcal O_t^{SB},
I_t^{SB},
P_t^{SB},
B_t,
H_t
).
}
$$

其中：

- $\mathcal O_t^{SB}$：active shared-bottom operators；
- $I_t^{SB}$：shared interfaces；
- $P_t^{SB}$：routing / invocation policy；
- $B_t$：resource state；
- $H_t$：history。

這個 runtime：

$$
\boxed{
\mathcal S_t
=
SharedBottomCognitiveRuntime_t.
}
$$

但：

$$
\mathcal S_t
$$

不是一個單一 mega-domain。

它更像 cognition 的 shared execution substrate。

---

# 8. 第一族：ATT — Attention / Selection

Phase 0.3 把舊 `Attend` 拆成：

$$
\boxed{
Attend_0
=
SustainFocus
\circ
GateInput
\circ
OrientFocus
\circ
SetAlertState.
}
$$

這個分解最重要的不是 Attention 被拆細。

而是 Attention 從 Observation 的「內部部件」被釋放。

Observation 需要 attention。

Search 也需要。

Proof 需要。

Memory retrieval 需要。

Planning 需要。

Generation 也需要。

因此：

$$
\boxed{
ATT
\text{ is a cross-program selection substrate candidate}.
}
$$

外部 attention 研究也支持一個方法學警告：attention 不是天然單一不可分功能。Posner 與 Petersen 的 attention-system framework 區分多種 attention functions；後續工作進一步擴張這些 network/function distinctions。

CODT 不把神經 attention networks 等同 ATT operators。

它只吸收：

$$
\boxed{
\text{attention can be functionally decomposable}.
}
$$

---

# 9. ATT 是 Domain 嗎？

這個問題不能由「Attention 很重要」回答。

ATT 若要成為 domain candidate，仍要通過 CODT-03 的 Domain-Likeness。

例如：

- ATT operators 是否反覆互相 composition？
- 是否有 coherent failure boundary？
- 是否有獨立 predictive/compressive value？
- 是否形成穩定 runtime niche？

所以：

$$
\boxed{
ATT
=
SharedBottomFamily
}
$$

目前比：

$$
\boxed{
ATT
=
PromotedDomain
}
$$

更保守。

---

# 10. 第二族：SRH — Search / Explore / Query

Search 是 shared-bottom 最明顯的案例之一。

最低 search program 可寫為：

$$
FormSearchQuery
\rightarrow
BindSearchSpace
\rightarrow
InitializeFrontier
\rightarrow
Score
\rightarrow
Expand
\rightarrow
Prune
\rightarrow
CheckTermination
\rightarrow
RecordTrace.
$$

它可以服務：

- memory retrieval；
- counterexample search；
- theorem search；
- abductive search；
- planning；
- design exploration；
- debugging。

因此 Search 的共用性不是語義上的「都在找東西」。

它有共享 machinery。

這使：

$$
\boxed{
SRH
}
$$

具有很強 shared-bottom candidate 地位。

Newell 與 Simon 的 problem-space / search 傳統，以及 Soar cognitive architecture，都提供「多種 problem solving 可以依賴共享搜索與控制機制」的外部歷史參照。

CODT 不直接等同 Soar architecture。

但接受一個重要結構種子：

$$
\boxed{
\text{general cognition may reuse task-general mechanisms}.
}
$$

---

# 11. Search 與 Retrieval 的邊界

`Retrieve` 是一個特別好的例子。

如果 retrieval 被寫成：

$$
MemoryDomain::Retrieve,
$$

會隱藏 search substrate。

但如果把 retrieval 全等同 search，又會丟掉 memory backend access。

因此：

$$
\boxed{
Retrieve
\approx
Search
+
MemoryBackendAccess.
}
$$

其中第二項在早期實驗中仍是 unresolved。

這表示 shared-bottom recovery 不必一次把所有東西還原乾淨。

它允許：

$$
\boxed{
PartialDecomposition.
}
$$

---

# 12. 第三族：GEN — Generation / Mutation / Perturbation

早期 `Hypothesize` 很容易被理解成 Explanation / Abduction 內部 primitive。

Phase 0.3 將 generic generation 解耦為：

$$
\{
Seed,
Mutate,
Perturb,
Recombine,
Sample,
Stabilize
\}.
$$

因此：

$$
\boxed{
GenerateCandidate
=
Stabilize
\circ
Variation
\circ
Seed.
}
$$

其中：

$$
Variation
\in
\{
Mutate,
Perturb,
Recombine,
Sample
\}.
$$

Hypothesis generation 只是：

$$
\boxed{
DomainConstraint
\circ
GeneralGeneration.
}
$$

所以：

- creative design；
- hypothesis generation；
- counterfactual generation；
- search diversification；
- mutation-based problem solving；

可以共享 GEN substrate。

---

# 13. Generation 不是 Creativity Domain

高階創造力通常還需要：

- preference；
- evaluation；
- novelty；
- constraint；
- representation；
- search；
- stabilization；
- verification。

因此：

$$
\boxed{
GEN
\neq
Creativity.
}
$$

更不能直接推出：

$$
\boxed{
GEN
=
CreativityDomain.
}
$$

GEN 只描述 candidate production substrate。

這個分離避免把所有生成行為都神祕化成「創造力」。

---

# 14. 第四族：REP — Representation / Translation / Bridge

Representation family 的重要性來自：

> 不同 cognitive programs 不一定在同一表示空間運作。

最低 representation bridge contract：

$$
DeclareRepresentationSpace
\rightarrow
SelectBridgeBasis
\rightarrow
TransformRepresentation
\rightarrow
AuditPreservation.
$$

因此：

$$
\boxed{
Object
\neq
Representation
\neq
Presentation.
}
$$

REP 服務：

- analogy；
- abstraction；
- quantification；
- CDSL；
- language translation；
- diagram / symbol transformation；
- World Presentation interface。

所以它高度 shared-bottom。

但高 shared-bottom 不代表 REP 一定是一個單一 domain。

因為不同 representation bridges 可能有完全不同的：

- type system；
- invariant；
- loss profile；
- certification；
- failure boundary。

---

# 15. Representation Infrastructure Candidate

REP 更可能包含：

$$
\boxed{
\text{domain-specific representation regions}
+
\text{cross-domain bridge infrastructure}.
}
$$

這也是為什麼：

$$
HighReuse
$$

不能直接翻譯成：

$$
CoreDomain.
$$

有時候 high reuse 是因為它位在 domains 之間。

---

# 16. 第五族：PRX — Proxy / Operationalization

PRX 是從 CQR 缺口中長出的 shared-bottom family。

關鍵分離：

$$
\boxed{
AbstractTarget
\neq
Proxy
\neq
Measurement.
}
$$

Operationalization 需要：

$$
StateOperationalTarget
\rightarrow
GenerateProxyCandidate
\rightarrow
TraceProxyLink
\rightarrow
AuditProxyValidity
\rightarrow
BindProxy.
$$

這套 machinery 不只屬於 CQR。

它也可服務：

- science；
- social measurement；
- AI evaluation；
- KPI design；
- psychometrics；
- observability；
- benchmarking。

所以 PRX 是跨方法 substrate。

---

# 17. PRX 也可能再被 GEN / VER 拆解

Phase 0.3 已留下 unresolved：

> `GenerateProxyCandidate` 是否其實只是 GEN specialization？

如果是：

$$
PRX
$$

本身可能不是完全 primitive family，而是：

$$
GEN
+
REP
+
VER
+
OperationalLink.
$$

這就是 shared-bottom 理論最重要的自我限制：

$$
\boxed{
SharedBottomFamily
\text{ can itself be decomposed}.
}
$$

---

# 18. 第六族：BEL — Belief / Uncertainty

BEL 將：

- belief state；
- evidence support；
- update rule；
- normalization；
- calibration；
- alternative preservation；

從特定推理方法中抽出。

最低 generic update：

$$
InitializeBeliefState
\rightarrow
EncodeEvidenceSupport
\rightarrow
SelectUpdateRule
\rightarrow
ApplyUpdateRule
\rightarrow
Normalize
\rightarrow
PreserveAlternatives.
$$

CODT 不預設：

$$
BeliefUpdate
=
BayesianUpdate.
$$

Bayesian probability 可以是 backend。

但 belief substrate 還可以包含：

- intervals；
- logic confidence；
- evidence weights；
- unresolved alternatives；
- qualitative certainty states。

因此：

$$
\boxed{
BEL
=
uncertainty-state infrastructure candidate.
}
$$

---

# 19. Belief 與 Truth 必須分開

shared-bottom belief state 的最大風險是被當成真值層。

CODT 保留：

$$
\boxed{
Belief_t(p)
\neq
Truth(p).
}
$$

以及：

$$
\boxed{
Confidence(p)
\neq
Correctness(p).
}
$$

所以 BEL 可以被很多 domains 使用，卻不能獲得 truth authority。

---

# 20. 第七族：DEC — Decision / Preference

在早期 Abduction decomposition 中：

`RankHypothesis`

`SelectInquiryCandidate`

被發現並不屬於 abduction 專屬 primitive。

generic decision program：

$$
DefineChoiceSet
\rightarrow
EncodePreference
\rightarrow
Evaluate
\rightarrow
Aggregate
\rightarrow
CheckAdmissibility
\rightarrow
(Select\mid Defer).
$$

因此：

$$
\boxed{
DEC
}
$$

服務：

- hypothesis ranking；
- planning；
- action selection；
- search pruning；
- resource allocation；
- conflict resolution。

---

# 21. Decision 不等於 Utility Maximization

von Neumann-Morgenstern utility theory 可以作為 decision backend seed。

bounded rationality 也可以作另一種 seed。

但 CODT 不預設：

$$
\boxed{
Decision
=
ExpectedUtilityMaximization.
}
$$

shared-bottom substrate 應保留 backend plurality。

---

# 22. 第八族：PLN — Planning / Goal / Constraint

Planning 看起來很像獨立 domain。

但 decomposition 後，它大量依賴：

- goal representation；
- constraint representation；
- search；
- generation；
- decision；
- budget；
- monitoring；
- replan。

所以：

$$
\boxed{
Planning
=
CrossFamilyProgram
}
$$

可能比：

$$
Planning
=
PrimitiveFamily
$$

更合理。

然而，`Goal`、`Constraint`、`Dependency`、`Budget`、`MonitorPlan` 等 operations 又確實可以形成 shared planning substrate。

因此 PLN 是一個很好的中間案例：

$$
\boxed{
\text{shared-bottom family}
\land
\text{higher-order program}.
}
$$

---

# 23. Planning 的雙層表示

可以寫：

$$
PLN_{substrate}
=
\{
Goal,
Constraint,
Dependency,
Budget,
Monitor,
ReplanSignal
\}
$$

以及：

$$
\boxed{
PlanningProgram
=
Route(
PLN_{substrate},
SRH,
GEN,
DEC,
BEL,
MET
).
}
$$

這種雙層表示比「Planning 是一個 primitive」更精確。

---

# 24. 第九族：ACT — Action Intent / Boundary

ACT 是 shared-bottom 中最需要邊界意識的一族。

其作用不是：

$$
\boxed{
\text{mutate World}.
}
$$

而是：

- represent intent；
- bind target；
- construct ActionSpec；
- check cognitive-side readiness；
- emit ActionRequest。

所以：

$$
\boxed{
ACT_{cog}
\rightarrow
ActionRequest.
}
$$

真正 World mutation 必須經 CWB。

因此：

$$
\boxed{
think
\neq
intend
\neq
request
\neq
act
\neq
WorldTransition.
}
$$

ACT 是 cognition 內部的 world-facing substrate。

CWB 則是邊界 infrastructure。

---

# 25. ACT 為什麼不能和 World Operator 合併

如果：

$$
EmitActionRequest
$$

直接等同：

$$
WorldTransition,
$$

認知系統就取得了不經 authorization 的世界修改權。

CODT 禁止：

$$
\boxed{
CognitiveOperator
=
WorldMutationOperator.
}
$$

所以 ACT 的 shared-bottom status 和 domain status都不能繞過 World Boundary。

---

# 26. 第十族：MET — Meta-Observation / Self-Audit

MET 把「系統監控自己」拆成：

$$
ObserveCognitiveState
\rightarrow
CompareProcessToGoal
\rightarrow
EstimateSelfUncertainty
\rightarrow
DetectStucknessOrBias.
$$

再由：

$$
Monitor
\rightarrow
EmitControlSignal.
$$

因此：

$$
\boxed{
Monitoring
\neq
Control.
}
$$

更重要的是：

$$
\boxed{
MetaObserver
\not\Rightarrow
TransparentTotalIntrospection.
}
$$

meta-observer 只能取得 bounded runtime view。

Nelson 與 Narens 的 metacognition framework 將 object-level 與 meta-level、monitoring 與 control 關係分開，可作外部歷史 seed。

CODT 不把 MET 等同於該框架。

但吸收：

$$
\boxed{
\text{monitoring and control can be functionally separated}.
}
$$

---

# 27. Shared-Bottom 不是 Executive Function 的翻版

Miyake 等人的 executive-function 研究提出「unity and diversity」問題：shifting、updating、inhibition 等功能具有共享與可分結構。

這對 CODT 有一個方法學啟發：

$$
\boxed{
\text{shared variance}
\neq
\text{identity}.
}
$$

但 SBCR 不是 executive function model。

原因：

1. SBCR 包含 Representation、Proxy、Belief、Search、Generation 等，不只 executive control；
2. SBCR 是 operator engineering / runtime ontology candidate，不是人類心理個體差異 latent-variable model；
3. SBCR 同時面向 human / AI / agent runtime；
4. SBCR operators 可以被 relative atomicity 再拆解。

因此：

$$
\boxed{
SBCR
\neq
ExecutiveFunctionTheory.
}
$$

---

# 28. Shared-Bottom 也不是 Working Memory Model

Baddeley 的 working-memory framework 及 episodic buffer 研究提供「多個處理子系統之間需要 integration interface」的歷史參照。

但 SBCR 不宣稱：

$$
REP
=
EpisodicBuffer,
$$

或：

$$
BEL
=
WorkingMemory.
$$

working memory 是心理學模型。

SBCR 是跨 program operator substrate。

兩者可比較，但不能同一化。

---

# 29. Shared-Bottom 與 Cognitive Architecture

Newell 的 unified-cognition 路線，以及 Soar architecture，提供另一種歷史參照：

> 一個 general cognitive system 可以依賴一組跨 task 共用 mechanisms，而不是每個 task 各自建一套完整 cognition。

這和 SBCR 的直覺相近。

但 CODT 的不同在於：

- operator primitive 具有 relative atomicity；
- domain 是後生 atlas；
- shared-bottom 和 domain 軸分離；
- epistemic license 是一級 object；
- World boundary 和 cognition 分離；
- runtime history 不可由 derived chart 回寫。

所以：

$$
\boxed{
SBCR
\neq
Soar
\neq
UnifiedTheoryOfCognition.
}
$$

它們只共享：

$$
\boxed{
\text{cross-task shared mechanism}
}
$$

這個一般研究方向。

---

# 30. 舊二十模組重新映射到 SBCR

Phase 0.3 的 dependency map 曾得到：

$$
OPS
\approx
ATT+REP+ABS+DEF+NEG+MEM+MET,
$$

$$
CRE
\approx
MET+ATT+DEC+PLN+SRH,
$$

$$
PSM
\approx
ABD+GEN+SRH+CAU+CF+REF+VER+BEL+MET,
$$

$$
CQR
\approx
DEF+CAT+PRX+MEA+REP+VER,
$$

$$
IDDM
\approx
MET+GEN+SRH+ATT,
$$

$$
CDSL
\approx
REP+ABS+ANA+VER.
$$

這些不是最終等式。

它們是：

$$
\boxed{
DependencyHypothesis.
}
$$

其意義是：

> 舊方法不再需要假設各自擁有一套完全私有的 cognition machinery。

---

# 31. Method Identity 來自 Topology，不只來自零件

如果 OPS 與 CDSL 都用 REP，兩者為什麼還是不同方法？

因為：

$$
\boxed{
SameOperators
\not\Rightarrow
SameProgram.
}
$$

method identity 還依賴：

- topology；
- order；
- branching；
- stop condition；
- goal；
- boundary；
- license；
- resource allocation。

因此：

$$
\boxed{
Method
=
TopologyOverSharedRuntime.
}
$$

這是 SBCR 對舊認知解構學最重要的保存方式。

---

# 32. Infrastructure Test

不是所有高頻 operator 都應升格 shared-bottom。

本文提出第一個判準：

若移除 operator $U$ 後，大量彼此不同的高階 programs 都失去可執行性或需要重建重複機制，則：

$$
InfrastructureScore(U)
$$

上升。

形式上：

$$
\boxed{
Infra(U)
=
\frac{
|\{M_i:Executable(M_i)\land\neg Executable(M_i\setminus U)\}|
}{
|\{M_i\}|
}.
}
$$

這只是候選 metric，不宣稱 universal。

---

# 33. Cross-Program Reuse Test

令：

$$
R(U)
$$

為 U 被不同 program families 合法調用的數量。

但還需要 diversity。

如果 U 被 100 個近乎相同的 search programs 使用，和被 Observation、Planning、Verification、Memory、Generation 同時使用，不應視為完全相同 evidence。

所以：

$$
\boxed{
ReuseEvidence
=
Frequency
+
ProgramDiversity.
}
$$

---

# 34. Boundary Independence Test

shared-bottom operator 應有自己的 boundary。

若 U 的合法條件完全由上層 method 決定，且 U 無法獨立定義：

- input；
- output；
- failure；
- license；

那它可能只是 method-internal code fragment。

因此：

$$
\boxed{
SharedBottom
\Rightarrow
PartialBoundaryIndependence.
}
$$

不是完全 context independence。

而是可被獨立契約化。

---

# 35. Independent Failure Test

shared-bottom 的重要證據之一是：

> 它可以以跨 methods 相似的方式失敗。

例如 Search 的：

- frontier explosion；
- premature pruning；
- false termination；

不依賴它是在做 theorem search 還是 memory retrieval。

這使：

$$
\boxed{
FailurePatternReuse
}
$$

成為 shared-bottom evidence。

---

# 36. Substitutability Test

如果兩個 implementation：

$$
U_a,U_b
$$

只要滿足同一 interface / license contract，就能在多個上層 programs 中替換，則 shared-bottom interface 地位更強。

形式上：

$$
\boxed{
U_a
\equiv_I
U_b
\Rightarrow
M[U_a]
\approx
M[U_b]
}
$$

在指定 scope 下成立。

這不是說 cognitive mechanism 本體相同。

而是 runtime substitution 成立。

---

# 37. Domain Independence Test

最重要的 test 是：

> shared-bottom status 是否可以在 domain membership 改變後仍保持？

如果：

$$
U
$$

被新 atlas 從：

$$
\mathfrak D_a
$$

移到：

$$
\mathfrak D_b,
$$

但它仍被大量 programs 共享，則：

$$
\boxed{
SharedBottom(U)
}
$$

不應消失。

這證明：

$$
\boxed{
SharedBottomAxis
\neq
DomainAxis.
}
$$

---

# 38. SBCR 的四種角色

本文提出 shared-bottom candidate 可以被進一步分類為四種 role。

## 38.1 Substrate

提供廣泛底層運算。

例如：

$$
SRH,GEN.
$$

## 38.2 Control Infrastructure

管理選擇、調度、監控。

例如：

$$
ATT,MET.
$$

## 38.3 Bridge Infrastructure

跨 representation / domain 轉換。

例如：

$$
REP,PRX.
$$

## 38.4 State / Decision Infrastructure

保存不確定性、做選擇與計畫。

例如：

$$
BEL,DEC,PLN.
$$

ACT 則位於 cognition-to-world boundary preparation。

這些分類本身仍是 human-facing projection。

---

# 39. SBCR 不是一層固定 hierarchy

不能假設：

$$
SharedBottom
<
Domain
<
Method
$$

是一條永遠成立的層級。

因為：

- 某 shared-bottom family 可以包含自己的 domain candidates；
- 某 domain 可以大量使用多個 shared-bottom families；
- 某 method 可以在多個 domains 中穿梭；
- meta-control 可以跨所有層。

所以更合理的是：

$$
\boxed{
\text{orthogonal relational architecture}
}
$$

而不是單樹 hierarchy。

---

# 40. Shared-Bottom Niche

若兩個 shared-bottom families 長期共同出現：

$$
ATT\cap SRH,
$$

$$
SRH\cap GEN,
$$

$$
REP\cap ABS,
$$

$$
BEL\cap MET,
$$

$$
DEC\cap PLN,
$$

可能形成：

$$
\boxed{
SharedBottomNiche.
}
$$

這些 niche 可以成為 future domain candidates。

但它們不能因為 co-occurrence 就自動 promotion。

---

# 41. SBCR 與 Domain Ecology 的關係

令：

$$
\mathcal S_t
$$

為 shared-bottom runtime。

令：

$$
\mathfrak A_t
$$

為 domain atlas。

則整體 cognition 至少需要：

$$
\boxed{
CognitiveSystem_t
=
(
\mathcal S_t,
\mathfrak A_t,
\mathcal P_t,
H_t
).
}
$$

其中：

- $\mathcal S_t$：shared substrate；
- $\mathfrak A_t$：domain ecology；
- $\mathcal P_t$：active program topology；
- $H_t$：history。

這四者不能合併。

---

# 42. Meta-Control Plane

MET 與部分 ATT / DEC / PLN 可以形成 control plane candidate。

但 control plane 不是 cognition 全部。

可以寫：

$$
\boxed{
Control_t
:
(
Goal,
RuntimeState,
Uncertainty,
Budget
)
\rightarrow
RoutingSignal.
}
$$

routing signal 可以調整：

- attention；
- search budget；
- generation temperature；
- decision threshold；
- plan branch；
- verification requirement。

這和 CRE 的角色高度相容。

因此 CRE 可以重新理解成：

$$
\boxed{
CRE
=
MetaPolicyOver(
SBCR,
Domains,
Programs
).
}
$$

---

# 43. Shared-Bottom 與 Learning

Phase 0.3 留下了一個未解問題：

> Learning 是單一 cognitive action，還是 operator / policy / state transition modification？

CODT-04 傾向後者。

若 learning 改變：

- operator weights；
- routing；
- memory；
- domain membership；
- policy；
- decomposition；

則：

$$
\boxed{
Learning
=
RuntimeModificationProcess
}
$$

可能比：

$$
Learning
=
SingleSharedBottomOperator
$$

更合理。

因此本文暫不把 Learning 加入第十一族。

---

# 44. Shared-Bottom 與 Language

Language parsing / generation 也暫不直接新增為 shared-bottom family。

原因是它可能同時包含：

- REP specialization；
- GEN specialization；
- MEM；
- ATT；
- planning；
- social/observer model。

所以：

$$
\boxed{
Language
\text{ remains unresolved}.
}
$$

CODT 的原則是：

> 不因重要就必須單獨建 family。

---

# 45. Motivation / Affect 仍是缺口

十族並未完整覆蓋 cognition。

情緒、慾望、身體狀態、drive、value 可能需要 motivational bottom layer。

但目前 evidence 尚不足以決定：

- 獨立 shared-bottom family；
- DEC / BEL context；
- embodiment/world state；
- value domain。

因此：

$$
\boxed{
SBCR_{v1}
\text{ is open-ended}.
}
$$

---

# 46. Shared-Bottom Registry 必須版本化

令：

$$
\mathcal R_t^{SB}
$$

為 shared-bottom registry。

若新 decomposition 發生：

$$
U
\rightarrow
(u_1,\ldots,u_k),
$$

則 registry 可以更新：

$$
\mathcal R_t^{SB}
\rightarrow
\mathcal R_{t+1}^{SB}.
$$

但舊 history 不被改寫。

所以：

$$
\boxed{
SharedBottomRevision
\neq
HistoryRewrite.
}
$$

這延續 CODT-02。

---

# 47. Shared-Bottom Promotion Gate

一個 family 要從 recovery seed 升為 strong shared-bottom candidate，本文要求至少：

## S1. Cross-Program Reuse

不同 program families 反覆使用。

## S2. Type Contract Stability

具有可獨立描述的 interface。

## S3. Independent Failure Pattern

失效可跨 programs 重現。

## S4. Substitutability Evidence

不同 implementation 可在 interface scope 下互換。

## S5. Domain Independence

shared-bottom status 不依賴單一 atlas membership。

## S6. Non-Triviality

不是純 logging / naming / no-op。

## S7. External / Runtime Evidence

最終需要超越 human decomposition。

因此：

$$
\boxed{
SharedBottomPromotion
\neq
DomainPromotion.
}
$$

兩套 gate 分開。

---

# 48. Shared-Bottom Falsification

shared-bottom family 也必須能被撤銷。

若：

- reuse 只存在於同一類方法；
- interface 無法獨立；
- failure 完全依賴上層 program；
- better decomposition 把它拆散；
- cross-context transfer 不成立；

則可輸出：

$$
\boxed{
SharedBottomFalsificationPressure(U).
}
$$

這避免 SBCR 變成新的永恆功能表。

---

# 49. AI-Native Runtime 的直接意義

對 AI Agent 而言，shared-bottom 的價值非常直接。

不應為每個任務重複建立：

- attention logic；
- search loop；
- uncertainty update；
- plan monitoring；
- action request boundary；
- self-audit。

更合理的是：

$$
\boxed{
TaskProgram
=
Route(
SharedRuntime,
DomainPrograms,
WorldInterfaces
).
}
$$

這使 AI architecture 可以：

- 共用 infrastructure；
- 審計 operator reuse；
- 控制資源；
- 替換 backend；
- 保留 certificates；
- 做跨 domain routing。

---

# 50. Human 與 AI 是否共享同一 Shared-Bottom？

這是 CODT-04 必須保持開放的問題。

human cognition 與 AI runtime 可能共享：

$$
\boxed{
FunctionalOperatorPattern
}
$$

但不共享：

- implementation；
- embodiment；
- latency；
- memory substrate；
- attention mechanism；
- subjective experience。

所以：

$$
\boxed{
FunctionalSimilarity
\neq
ImplementationIdentity.
}
$$

CODT 目前只主張：

> 相同 operator contract 可以作跨實作比較語言。

---

# 51. Shared-Bottom 與 Subjective Experience

SBCR 不宣稱：

$$
ATT
=
\text{human phenomenal attention},
$$

或：

$$
BEL
=
\text{felt belief}.
$$

它只描述 runtime-functional candidate。

因此：

$$
\boxed{
OperatorFunction
\neq
Qualia.
}
$$

這個 ontology boundary 必須保留。

---

# 52. SBCR 的第一版架構

本文將 cognition 暫時寫成：

$$
\boxed{
\begin{aligned}
CognitiveRuntime_t
=
(
&SharedBottom_t,\\
&DomainAtlas_t,\\
&ActivePrograms_t,\\
&MetaControl_t,\\
&MemoryBeliefState_t,\\
&WorldBoundary_t,\\
&History_t
).
\end{aligned}
}
$$

其中 shared-bottom 不覆蓋全部 cognition。

它只提供跨 programs 反覆重用的 substrate。

---

# 53. World-Coupled Loop

沿用 Phase 0.3 的直覺，可以寫：

$$
\rho_{O,t}(\mathbf W)
\rightarrow
ATT
\rightarrow
OBS
\rightarrow
REP
\rightarrow
MEM/BEL
\rightarrow
SRH/GEN/INF
\rightarrow
DEC/PLN
\rightarrow
ACT_{request}
\rightarrow
CWB
\rightarrow
\mathbf W_{t+1}.
$$

其中：

$$
INF
$$

只是 inference-program abbreviation。

不是新 primitive。

Meta loop：

$$
\boxed{
MET:
CognitiveRuntime_t
\rightarrow
Monitor
\rightarrow
ControlSignal
\rightarrow
CognitiveRuntime_{t+1}.
}
$$

所以：

$$
\boxed{
WorldLoop
\neq
MetaControlLoop.
}
$$

---

# 54. 四層架構

本文把 Phase 0.3 的三層架構再整理成四層。

## Layer A：Canonical Operator / History

$$
OperatorMetadata
+
OrderedHistory
+
Artifacts
+
Certificates.
$$

## Layer B：Shared-Bottom Runtime

$$
ATT,
SRH,
GEN,
REP,
PRX,
BEL,
DEC,
PLN,
ACT,
MET.
$$

## Layer C：Derived Domain / Program Control

$$
DomainSeeds,
Niches,
Atlas,
Schedulers,
ProgramTopologies.
$$

## Layer D：World Boundary

$$
CWB,
Authorization,
WorldOperator,
WorldTransition,
Presentation.
$$

核心約束：

$$
\boxed{
Layer_C
\text{ cannot rewrite }
Layer_A.
}
$$

且：

$$
\boxed{
Layer_B
\text{ cannot bypass }
Layer_D.
}
$$

---

# 55. 這四層不是本體終局

Layer B 可能未來再拆。

Layer C 可能由 learned atlas 改寫。

Layer D 可能因不同 World runtime 而不同。

所以：

$$
\boxed{
Architecture
\text{ is versioned}.
}
$$

本文只提供第一版 separation discipline。

---

# 56. CODT-04 憲法增補

在前面 CODT constraints 上，本文新增：

## CODT-C26：Shared-Bottom / Domain Separation

$$
\boxed{
SharedBottom
\neq
Domain.
}
$$

## CODT-C27：Reuse / Atomicity Separation

$$
\boxed{
HighReuse
\not\Rightarrow
Atomic.
}
$$

## CODT-C28：Method as Topology over Shared Runtime

$$
\boxed{
Method
=
TopologyOver(
SharedRuntime,
DomainPrograms
).
}
$$

## CODT-C29：Shared-Bottom Open-Endedness

$$
\boxed{
SBCR_t
\not\Rightarrow
SBCR_{t+1}
}
$$

的 registry immutability。

## CODT-C30：Infrastructure Non-Sovereignty

shared-bottom infrastructure 不因高 reuse 自動取得 domain authority、truth authority 或 World authority。

## CODT-C31：Meta-Observation Boundedness

$$
\boxed{
MetaObserver
\not\Rightarrow
TotalIntrospection.
}
$$

## CODT-C32：Functional / Implementation Separation

$$
\boxed{
FunctionalOperatorSimilarity
\neq
ImplementationIdentity.
}
$$

## CODT-C33：World Boundary Preservation

$$
\boxed{
ACT_{request}
\neq
WorldTransition.
}
$$

---

# 57. 本文的理論地位

本文沒有宣稱：

> cognition 的真正底層就是十族。

本文真正提出：

$$
\boxed{
\text{cross-program reuse is a separate structural axis}.
}
$$

也就是 cognition 至少不能只用：

$$
\text{domain taxonomy}
$$

描述。

還需要：

$$
\boxed{
\text{shared execution substrate}.
}
$$

---

# 58. 為什麼這篇對後面 Flow-Atlas Separation 很重要

如果一個高 reuse substrate 被錯當成 domain core，transition graph 會出現大量跨域連邊。

研究者可能因此誤判：

> domain boundary 很弱。

但真正原因可能是：

$$
\boxed{
\text{shared infrastructure crosses domains by design}.
}
$$

所以後面分析 flow 時必須區分：

- domain-internal flow；
- cross-domain bridge flow；
- shared-bottom infrastructure flow；
- meta-control flow；
- world-boundary flow。

否則 atlas geometry 會被基礎設施扭曲。

---

# 結論

Shared-bottom 是 CODT 從「方法」和「域」之外再發現的第三種結構。

方法回答：

> cognition 正在執行什麼高階程序？

Domain 回答：

> 哪些 operators / histories 形成穩定 operational region？

Shared-bottom 回答：

> 哪些 operations 被大量彼此不同的 programs 共同依賴？

因此：

$$
\boxed{
Method
\neq
Domain
\neq
SharedBottom.
}
$$

三者可以互相重疊、互相使用，但不能互相等同。

Attention 可以是 shared-bottom selection substrate。

Search 可以是 shared-bottom machinery，且可能同時具有 domain-like niche。

Generation 可以跨 hypothesis、design、counterfactual 與 creativity programs。

Representation 可以主要作 bridge infrastructure。

Belief、Decision、Planning 可以形成 state/control substrate。

ACT 準備 ActionRequest，但不能修改 World。

MET 監控 runtime，但不是全知內省者。

所以 SBCR 最終不是「另一份功能分類表」。

它是一個新的架構原則：

$$
\boxed{
\text{general cognition reuses a shared runtime substrate,
while domains and methods are derived on other structural axes}.
}
$$

當這個分離被固定後，CODT 才能在下一篇真正處理 flow 與 atlas：

> operator transitions 中哪些是 domain geometry，哪些只是 shared infrastructure traffic？

這就是 CODT-05 Flow-Atlas Separation 的起點。

---

# 參考文獻與外部研究種子

## A. Attention / Executive Control

1. Posner, M. I., & Petersen, S. E. (1990). "The Attention System of the Human Brain." *Annual Review of Neuroscience*, 13, 25-42. DOI: 10.1146/annurev.ne.13.030190.000325.
2. Petersen, S. E., & Posner, M. I. (2012). "The Attention System of the Human Brain: 20 Years After." *Annual Review of Neuroscience*, 35, 73-89. DOI: 10.1146/annurev-neuro-062111-150525.
3. Miyake, A., Friedman, N. P., Emerson, M. J., Witzki, A. H., Howerter, A., & Wager, T. D. (2000). "The Unity and Diversity of Executive Functions and Their Contributions to Complex Frontal Lobe Tasks: A Latent Variable Analysis." *Cognitive Psychology*, 41(1), 49-100. DOI: 10.1006/cogp.1999.0734.

## B. Cognitive Architecture / Search

4. Newell, A. (1990). *Unified Theories of Cognition*. Harvard University Press.
5. Laird, J. E., Newell, A., & Rosenbloom, P. S. (1987). "SOAR: An Architecture for General Intelligence." *Artificial Intelligence*, 33(1), 1-64. DOI: 10.1016/0004-3702(87)90050-6.
6. Newell, A., & Simon, H. A. (1972). *Human Problem Solving*. Prentice-Hall.

## C. Memory / Metacognition

7. Baddeley, A. (2000). "The Episodic Buffer: A New Component of Working Memory?" *Trends in Cognitive Sciences*, 4(11), 417-423. DOI: 10.1016/S1364-6613(00)01538-2.
8. Nelson, T. O., & Narens, L. (1990). "Metamemory: A Theoretical Framework and New Findings." *Psychology of Learning and Motivation*, 26, 125-173. DOI: 10.1016/S0079-7421(08)60053-5.

**邊界聲明：** 上述研究只作 external structural seeds。SBCR 的 ATT、SRH、GEN、REP、PRX、BEL、DEC、PLN、ACT、MET operator families，不宣稱與任何心理學 latent variable、神經網路、Soar module、working-memory component 或 metacognitive level 一一同一。

## D. 內部理論來源

1. CODT-01〈從認知方法到認知算子：認知解構學的域化轉向〉。
2. CODT-02〈認知算子代數與相對原子性〉。
3. CODT-03〈認知域的生成：域不是分類名稱，而是算子閉包與操作生態〉。
4. CDD Phase 0 v0.2：Shared-bottom gaps。
5. CDD Phase 0 v0.3：Shared-Bottom Cognitive Runtime Recovery。
6. `shared_bottom_dependency_map_v0.3.json`。
7. GCORF / General Cognitive Operator Reverse Engineering Framework。
8. HSO v0.8。
9. MWT / CWB SourcePacks。

---

# 版本記錄

## v1.0

- 正式提出 Shared-Bottom Cognitive Runtime, SBCR。
- 固定 Shared-Bottom Axis 與 Domain Axis 的正交分離。
- 系統整理 ATT、SRH、GEN、REP、PRX、BEL、DEC、PLN、ACT、MET 十族。
- 將舊認知解構學 methods 重構為 over-SBCR program topology。
- 建立 Infrastructure、Cross-Program Reuse、Boundary Independence、Independent Failure、Substitutability、Domain Independence 六類 shared-bottom tests。
- 明確聲明 shared-bottom family 可再次被 relative atomicity 拆解。
- 區分 substrate、control infrastructure、bridge infrastructure、state/decision infrastructure 與 world-boundary preparation。
- 建立四層：Canonical Operator / Shared Runtime / Derived Domain Control / World Boundary。
- 為 CODT-05 Flow-Atlas Separation 建立 shared-infrastructure traffic 的理論前提。
