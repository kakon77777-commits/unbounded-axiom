# 從數學解題到自主數學研究：受約束數學域補全與自主數學研究 Runtime

## From Mathematical Problem Solving to Autonomous Mathematical Research: Constrained Mathematical Domain Completion and an Autonomous Mathematical Research Runtime

**系列：Autonomous Mathematical Research / Paper 01 of 04**  
**版本：v0.1**  
**日期：2026-08-22**  
**作者：Neo.K**

---

## 摘要

大型語言模型與形式證明系統在數學推理、自動形式化、定理證明與研究級問題探索上的能力正在快速提升。然而，「能解題」與「能自主進行數學研究」並不等價。既有系統通常預設問題、定義、成功條件與研究目標已由人類正確提供，之後再要求 AI 搜尋證明、生成猜想、調用工具或修正證明。真正的研究情境卻經常不是如此：原問題可能存在定義缺失、假設不足、表示方式不良、判定條件模糊、方法域缺口、計算能力不足、形式化不忠實，甚至問題本身就需要澄清、限制、推廣或重新建立與既有理論的關係。

本文提出一個由「解題器」轉向「自主數學研究 Runtime」的統合框架。第一，本文將數學研究失敗從單一的「未解」狀態拆解為多域問題診斷，並定義 **Mathematical Domain Gap Map**，使 AI 能夠判定目前阻塞究竟來自問題域、定義域、假設域、判定域、表示域、解決域、方法域、引理／依賴域、計算域、反例／證據域、驗證域、橋接域或新穎性域。第二，本文提出 **Constrained Mathematical Domain Completion, CMDC（受約束數學域補全）**：AI 在確認缺口後可以生成缺失的定義、術語、引理、方法、表示、假設、猜想與橋接構造，但每一種生成都必須同時產生對應的數學義務，並經過驗證、比較、溯源與治理後才能升格。第三，本文引入 **Problem Identity Protocol**，明確區分原問題與任何修正版、限制版、推廣版、弱化版、強化版或新問題，禁止 AI 以無聲改題取代原問題。第四，本文將上述方法嵌入 Addressable Cognitive Runtime 與 CTCL-ITR 類型的持續自治架構，提出 **Autonomous Mathematical Research Runtime, AMRR**：由持續研究目標、研究環境與研究契約驅動 AI 自主形成研究議程、選擇認知程序、診斷缺口、提出修復、執行研究、產生證明義務、調用驗證器、建立與既有數學的橋接，並留下可重建的時間因果研究歷史。

本文不主張現有 AI 已具備一般性的自主數學家能力，也不將形式可驗證性、數學正確性、語義忠實性、新穎性與學術接受度混為一談。本文的目標是提出一個可實作、可審計、可否證的研究架構，使「AI 自主數學研究」從模糊能力敘述轉為一組可以逐層驗證的工程與方法論命題。

**關鍵詞：** 自主數學研究、AI 數學、受約束數學域補全、問題身份、數學義務、自動形式化、形式證明、理論建構、Addressable Cognitive Runtime、CTCL-ITR

---

# 1. 引言：數學 AI 的下一個問題不是「還能多解幾題」

近年的 AI 數學研究已經跨越數個重要門檻。大型模型不再只處理基礎算術或標準競賽題，而開始結合長程推理、文獻搜尋、形式證明器與自我修訂處理研究級數學。Aletheia 類研究系統已經將「生成—驗證—修訂」推進到長程自然語言數學研究；AI-driven formal proof search 類系統則展示了大型模型與 Lean 等形式證明器結合後，在開放數學問題上進行可機器驗證搜尋的能力。另一方面，autoformalization 的研究焦點也正在從孤立命題翻譯，擴張到 definitions、axioms、lemmas 與依賴關係共同構成的 theory-level formalization。

這些成果共同表明：

$$
\text{MathematicalAI}
\neq
\text{Calculator}.
$$

同時也表明：

$$
\text{MathematicalAI}
\neq
\text{OneShotProblemSolver}.
$$

然而，若要進一步討論「自主數學研究 AI」，仍存在一個比提升 proof success rate 更基本的問題：

> **當原問題本身不完整、不精確、表示不良、缺乏必要方法或依賴時，AI 能否先辨認「缺的是什麼」，再在受約束條件下補出缺失數學，並證明自己沒有偷偷把問題換掉？**

傳統解題流程常被抽象為：

$$
Q
\rightarrow
Solve(Q)
\rightarrow
Answer.
$$

研究級數學更接近：

$$
Q_0
\rightarrow
Interpret
\rightarrow
Diagnose
\rightarrow
Reformulate
\rightarrow
Explore
\rightarrow
Construct
\rightarrow
Prove/Disprove
\rightarrow
Verify
\rightarrow
Integrate.
$$

其中任何一個箭頭都可能失敗。

因此，本文的核心立場是：

$$
\boxed{
\text{Unsolved}
\neq
\text{Single Failure Mode}.
}
$$

一個尚未解決的數學問題，可能不是因為「推理能力不夠」，而是因為研究系統尚未辨認自己所處的問題域與缺口類型。

---

# 2. 從解題到研究：兩種不同的計算對象

## 2.1 解題器的基本假設

對傳統 solver，輸入通常已經隱含提供：

$$
Q=
(
Statement,
Definitions,
Assumptions,
Goal,
SuccessCriterion
).
$$

因此 solver 的主要工作是搜尋：

$$
\pi
\in
\Pi(Q),
$$

其中 $\Pi(Q)$ 是可能的解答、證明、構造、反例或計算路徑集合。

在這個模型下，問題空間被視為固定：

$$
Q_t=Q_0.
$$

AI 只需改變搜索狀態：

$$
R_t
\rightarrow
R_{t+1}.
$$

---

## 2.2 研究 Runtime 的基本假設

真正數學研究中，問題本身也可能是動態研究對象：

$$
Q_t
\rightarrow
Q_{t+1}.
$$

例如研究者可能發現：

- 原定義允許退化案例；
- 原命題缺少必要假設；
- 目前表示遮蔽了不變量；
- 原問題其實是已知定理的重新表述；
- 一個更一般的問題反而具有更自然的結構；
- 某個方法只適用於限制子類；
- 原猜想存在反例；
- 形式化版本與自然語言原意不一致。

因此數學研究系統的狀態不應只有「目前證明寫到哪裡」，而應包括：

$$
S_t^M
=
(
Q_t,
T_t,
K_t,
G_t,
\Delta_t,
O_t,
V_t,
H_t
),
$$

其中：

- $Q_t$：目前問題版本；
- $T_t$：目前理論背景；
- $K_t$：當時可知知識邊界；
- $G_t$：研究目標；
- $\Delta_t$：已識別缺口；
- $O_t$：尚未解除的數學義務；
- $V_t$：驗證狀態；
- $H_t$：研究歷史與溯源。

這使研究從：

$$
\text{Search over proofs}
$$

擴張為：

$$
\boxed{
\text{Search over proofs, representations, definitions, methods, assumptions, bridges, and problem versions}.
}
$$

---

# 3. 多域數學問題模型

本文提出第一版 **Mathematical Research Domain Set**：

$$
\mathfrak D
=
\{
D_P,
D_D,
D_A,
D_J,
D_R,
D_S,
D_M,
D_L,
D_C,
D_E,
D_V,
D_B,
D_N
\}.
$$

這個集合不是宣稱數學研究只能被永久切成十三類，而是一個可版本化、可擴張的 active ontology。

## 3.1 $D_P$：Problem / Specification Domain

問題：我們真正要問的是什麼？典型失敗包括問題語義含混、存在多種不同解讀、目標沒有固定，以及原始敘述與形式敘述不一致。

## 3.2 $D_D$：Definition Domain

問題：使用的對象是否被充分且一致地定義？典型失敗包括未定義術語、定義循環、定義粒度不足、與既有術語重複但未建立關係，以及邊界案例失效。

## 3.3 $D_A$：Assumption / Boundary Domain

問題：命題需要哪些假設、作用範圍與邊界？典型失敗包括缺必要假設、假設過強、假設互相矛盾、隱含前提未顯式化，以及研究結論超出原有效域。

## 3.4 $D_J$：Judgment / Success-Criterion Domain

問題：什麼才算解決？例如：

$$
Existence?
$$

$$
Uniqueness?
$$

$$
ClosedForm?
$$

$$
Algorithm?
$$

$$
Approximation?
$$

$$
FormalProof?
$$

不同成功條件對應不同研究空間。

## 3.5 $D_R$：Representation Domain

問題：當前表示是否適合研究？同一數學對象可能在：

$$
NaturalLanguage
\rightarrow
Logic
\rightarrow
Algebra
\rightarrow
Geometry
\rightarrow
Graph
\rightarrow
Matrix
\rightarrow
Program
$$

之間具有不同的可操作性。因此：

$$
Complexity(Q\mid R_1)
$$

可能遠大於：

$$
Complexity(Q\mid R_2).
$$

## 3.6 $D_S$：Solution Domain

問題：合法解答空間究竟是什麼？例如某問題要求 exact solution，但實際上較自然的是 classification、bound、existence theorem 或 counterexample。

## 3.7 $D_M$：Method Domain

問題：現有方法是否足以作用於此類結構？這一域允許 AI 不只選方法，也能提出候選新方法，但新方法必須產生 correctness、applicability 與 failure obligations。

## 3.8 $D_L$：Lemma / Dependency / Theory Domain

問題：目前是否缺少必要中間結果、依賴或理論基礎？形式：

$$
T
\vdash
L_1,\ldots,L_n
\Rightarrow
Q
$$

但若某個 $L_k$ 尚不存在，主要缺口可能不是最終 theorem，而是 supporting theory。

## 3.9 $D_C$：Computation / Search Domain

問題：困難主要來自計算、搜尋、記憶體、時間或形式證明搜索成本嗎？這一域對應：

$$
Compute,
Search,
Memory,
Parallelism,
Tooling,
FormalProofBudget.
$$

若瓶頸主要在此，提高算力或演算法才是合理修復。

## 3.10 $D_E$：Example / Counterexample / Evidence Domain

問題：是否缺少足以約束理論的例子、反例、極端案例或計算證據？候選新定義與猜想尤其需要：

$$
Examples
+
NonExamples
+
BoundaryCases.
$$

## 3.11 $D_V$：Verification / Faithfulness Domain

問題：我們證明的東西是不是原本想證明的東西？必須區分：

$$
TypeChecks
$$

與：

$$
SemanticallyFaithful.
$$

也必須區分：

$$
ProofValid
$$

與：

$$
StatementCorrectlyFormalized.
$$

## 3.12 $D_B$：Bridge / Integration Domain

問題：新構造與既有數學是什麼關係？AI 新生成一個定義並不足以建立新的數學貢獻。至少需要研究：

$$
Equivalent?
$$

$$
SpecialCase?
$$

$$
Generalization?
$$

$$
Isomorphic?
$$

$$
Reducible?
$$

$$
Independent?
$$

若沒有這一域，AI 很容易建立大量形式上自洽但與數學共同體脫節的私人理論島嶼。

## 3.13 $D_N$：Novelty / Interestingness Domain

最後仍必須問：即使正確，它是不是值得被保留？因此：

$$
Correct
\not\Rightarrow
Novel
\not\Rightarrow
Interesting
\not\Rightarrow
Useful.
$$

新穎性不是 proof assistant 能單獨判斷的屬性，必須依賴文獻、形式庫、歷史知識邊界與人類審查。

---

# 4. Mathematical Domain Gap Map

令：

$$
Diagnose:
S_t^M
\rightarrow
\Delta_t.
$$

其中：

$$
\Delta_t
=
\{
\delta_1,\delta_2,\ldots,\delta_n
\}.
$$

每一個 gap：

$$
\delta_i
=
(
id,
domain,
target,
evidence,
severity,
confidence,
blocking,
candidateRepairs
).
$$

其中：

$$
domain(\delta_i)\in\mathfrak D.
$$

於是 AI 的下一步不必直接是：

$$
Solve(Q).
$$

而可以是：

$$
SelectGap(\Delta_t)
\rightarrow
ResearchAgenda_{t+1}.
$$

這使「缺什麼補什麼」從語言直覺變成可管理研究狀態。

---

# 5. 受約束數學域補全 CMDC

## 5.1 定義

本文定義 **Constrained Mathematical Domain Completion**：

$$
\boxed{
CMDC:
(S_t^M,\delta_i)
\rightarrow
\mathcal C_i
}
$$

其中：

$$
\mathcal C_i
=
\{
c_1,\ldots,c_k
\}
$$

是一組針對缺口 $\delta_i$ 的候選補全。

候選可以是新定義、新術語、新表示、新假設、新 lemma、新 conjecture、新 method、新 computation strategy、新 bridge 或新 theory fragment。

但：

$$
Generate(c)
\neq
Accept(c).
$$

這是 CMDC 的第一個核心不變量。

## 5.2 補全不是自由生成

AI 可以生成：

$$
c_{new}.
$$

但必須進入：

$$
Candidate
\rightarrow
Test
\rightarrow
Compare
\rightarrow
Verify
\rightarrow
Certify
\rightarrow
Register.
$$

因此：

$$
\boxed{
Discovery
\neq
Certification.
}
$$

這一原則同時適用於 cognitive operators 與 mathematical objects。

## 5.3 補全的局部性

本文不把「domain completion」理解為完成整個數學領域。更合理的定義是相對某個研究作用域 $\Omega$ 的局部補全：

$$
LocalDomainCompletion(\Omega).
$$

對應理論包：

$$
\mathcal T_\Omega
=
(
\Sigma,
D,
A,
M,
L,
Th,
C,
E,
B,
H
).
$$

其中：

- $\Sigma$：語言、術語與符號；
- $D$：definitions；
- $A$：axioms / assumptions；
- $M$：models / semantics；
- $L$：lemmas；
- $Th$：theorems / conjectures；
- $C$：constructive / computational methods；
- $E$：examples / counterexamples；
- $B$：bridges；
- $H$：history / provenance。

因此 CMDC 的目標不是製造無界數學文本，而是：

$$
\boxed{
\text{restore enough mathematical structure for the current research scope to become well-posed, investigable, and auditable}.
}
$$

---

# 6. Problem Identity Protocol：允許改題，但禁止偷換問題

## 6.1 原問題必須不可覆寫

令初始問題為：

$$
Q_0.
$$

若 AI 判定問題需要修改，不應執行：

$$
Q_0:=Q_1.
$$

而應建立：

$$
Q_0
\xrightarrow{\rho}
Q_1.
$$

其中：

$$
\rho
=
Relation(Q_0,Q_1).
$$

## 6.2 問題變換類型

第一版可定義：

$$
Relation(Q_i,Q_j)
\in
\{
Equivalent,
Clarification,
Restriction,
Generalization,
Weakening,
Strengthening,
AddedAssumption,
Reinterpretation,
NewProblem
\}.
$$

必要時 ontology 可以繼續擴張。

## 6.3 不同變換不能共享同一成功聲明

若：

$$
Relation(Q_0,Q_1)=Restriction,
$$

且：

$$
Proof(Q_1)
$$

成立，一般不能推出：

$$
Proof(Q_0).
$$

同理，若：

$$
Q_1
=
Q_0+A_{new},
$$

那麼：

$$
T+A_{new}\vdash Q_1
$$

不能被報告成：

$$
T\vdash Q_0.
$$

因此本文提出：

$$
\boxed{
\text{Mutation is permitted; silent mutation is forbidden.}
}
$$

---

# 7. Mathematical ChangeSet

任何研究過程中的數學變更應形成一級物件：

$$
\Delta^M_t
=
MathChangeSet_t.
$$

它至少應包含：

$$
MathChangeSet
=
(
SourceRefs,
ChangeType,
Target,
Before,
After,
Reason,
GapRef,
Obligations,
VerificationState
).
$$

可接受的 ChangeType 例如：

$$
DefinitionAdded,
AssumptionAdded,
RepresentationChanged,
LemmaIntroduced,
MethodIntroduced,
ProblemRestricted,
ProblemGeneralized.
$$

這使研究歷史不再只留下「後來我們改了定義」，而能回答：改了哪一版、為什麼、是為了處理哪個 gap、因此新增了哪些 proof obligations，以及最後是否通過。

---

# 8. 數學義務：生成自由必須伴隨驗證責任

## 8.1 Obligation Generator

對任何候選數學生成物 $x$，定義：

$$
\mathcal O(x)
=
\{
o_1,o_2,\ldots,o_m
\}.
$$

因此：

$$
Promote(x)
\Rightarrow
DischargeRequired(\mathcal O(x)).
$$

不一定要求所有 obligation 都必須被完全自動證明，但未解除義務必須保持顯式。

## 8.2 不同生成物產生不同義務

新 notation 可能要求：

$$
SemanticPreservation.
$$

新 definition 可能要求：

$$
WellFormed
\land
NonCircular
\land
BoundaryDefined
\land
PriorArtRelation.
$$

新 lemma 要求：

$$
FormalProof
\lor
AcceptedProof.
$$

新 assumption 要求：

$$
ProblemMutationDeclared.
$$

新 conjecture 至少要求：

$$
CounterexampleSearch
+
PriorArtSearch
+
ScopeDeclaration.
$$

新 method 可能要求：

$$
Correctness
+
Applicability
+
FailureConditions
+
Complexity.
$$

新 theory bridge 則要求相應的 equivalence、inclusion、reduction、morphism 或 interpretation 證明。

新 axiom 必須明確標記：

$$
NonConservativeExtensionCandidate.
$$

並研究可能的：

$$
ModelExistence,
RelativeConsistency,
Independence,
Consequences.
$$

## 8.3 自由與義務的單調原則

本文提出方法論原則：

$$
\boxed{
GenerationFreedom\uparrow
\Longrightarrow
VerificationObligation\uparrow.
}
$$

AI 越能創造新的數學結構，就越不能只靠語言可信度宣告完成。

---

# 9. Definitional Extension 與真正 Theory Extension

## 9.1 保守定義擴張

若：

$$
T_1
=
T_0+\Delta_D
$$

只是新的 definition / notation，理想情況應具有保守性：

$$
T_1\vdash\phi
\land
\phi\in Lang(T_0)
\Rightarrow
T_0\vdash\phi.
$$

也就是新語言提高表達與操作能力，但不偷偷增加舊語言中的證明能力。

## 9.2 非保守擴張

若：

$$
T_1
=
T_0+A_{new},
$$

則必須承認：

$$
\boxed{
T_1\neq T_0.
}
$$

這不代表擴張不合法。真正不合法的是：

$$
\boxed{
\text{non-conservative extension without explicit declaration}.
}
$$

因此 AMRR 不應禁止 AI 提出新公理，而應將其提升到最高義務級別。

---

# 10. 從「一個新概念」到「一個可研究域」

若 AI 生成：

$$
\tau_{new},
$$

應至少建立：

$$
ConceptCandidate
=
(
Name,
Definition,
Signature,
Examples,
NonExamples,
BoundaryCases,
Invariants,
Relations,
PriorArt
).
$$

接著研究：

$$
C_{new}
\equiv
C_{old}?
$$

或：

$$
C_{new}
\subsetneq
C_{old}?
$$

或：

$$
C_{old}
\subsetneq
C_{new}?
$$

或真正：

$$
C_{new}
\not\equiv
C_{known}.
$$

只有在這種結構下，AI 的「發明術語」才從文字生成變成候選數學建構。

---

# 11. 方法也應成為一級數學物件

定義：

$$
MethodCandidate
=
(
Domain,
Preconditions,
Inputs,
Transformation,
Outputs,
Invariants,
Termination,
Correctness,
Complexity,
FailureModes,
Bridges
).
$$

這使新方法可以被：

$$
Generate
\rightarrow
Benchmark
\rightarrow
Formalize
\rightarrow
Compare
\rightarrow
Certify.
$$

並避免「我發明了一個新技巧」只停留在自然語言描述。

---

# 12. 從 ACR 到 AMRR

## 12.1 母 Runtime 不需要重寫

Addressable Cognitive Runtime 的一般閉環可以表示為：

$$
Environment_t
\rightarrow
Observation_t
\rightarrow
SemanticState_t
\rightarrow
Agenda_t
\rightarrow
CognitiveProgram_t
\rightarrow
Governance_t
\rightarrow
Action_t
\rightarrow
Audit_t
\rightarrow
Update_{t+1}.
$$

本文主張，數學自治不應另造一套完全獨立 Agent，而應建立：

$$
\boxed{
AMRR
=
ACR
+
MathematicalDomainAdapter
+
CMDC
+
MathematicalVerifierLayer.
}
$$

## 12.2 Mathematical Semantic State

定義：

$$
S_t^M
=
Extend(
SemanticState_t,
MathExtension_t
).
$$

其中 MathExtension 至少可以包括：

$$
(
problemRef,
theoryRefs,
definitionRefs,
assumptionRefs,
representationRefs,
gapRefs,
obligationRefs,
verificationRefs,
bridgeRefs,
noveltyState
).
$$

這樣原 ACR 的 progress、uncertainty、failures、missing、risks、budget、authority 可以繼續保留，而不是重新發明。

## 12.3 Mathematical Cognitive Registry

一般 ACR 可以使用 VERIFY、COUNTEREXAMPLE、REFRAME、BACKTRACK、DECOMPOSE。數學專用 namespace 可以擴張為：

```text
cog://math/interpret
cog://math/formalize
cog://math/diagnose-gap
cog://math/define
cog://math/generate-lemma
cog://math/generate-conjecture
cog://math/search-counterexample
cog://math/change-representation
cog://math/introduce-assumption
cog://math/check-conservativity
cog://math/prove
cog://math/disprove
cog://math/bridge-theory
cog://math/check-prior-art
cog://math/discharge-obligation
cog://math/package-theory
```

但新 operator 不應直接升格：

$$
Discovery
\neq
Registration.
$$

---

# 13. 數學自治仍需要治理

一個 AI 能生成某個數學物件，不代表它應立即把該物件視為正式理論。因此本文沿用三分：

$$
Can
\neq
Should
\neq
Authorized.
$$

映射到數學研究可得到：

$$
CanGenerate(x)
\neq
ShouldPursue(x)
\neq
MayPromote(x).
$$

例如 AI 可以生成一個新公理：

$$
CanGenerate(A)=1.
$$

但研究契約可能規定：

$$
MayPromote(A)=0
$$

除非完成 ESCALATE 或取得人類數學家審查。

因此數學治理輸出仍可保留：

$$
Decision
\in
\{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE
\}.
$$

---

# 14. 自主數學研究的持續閉環

本文提出 AMRR 主循環：

$$
\boxed{
\begin{aligned}
ResearchGoal_t
&\rightarrow Observe\\
&\rightarrow MathematicalState_t\\
&\rightarrow DiagnoseDomains\\
&\rightarrow GapMap_t\\
&\rightarrow GenerateAgenda\\
&\rightarrow RetrieveCognitiveMethods\\
&\rightarrow GenerateRepairCandidates\\
&\rightarrow Falsify/Compare\\
&\rightarrow GovernMutation\\
&\rightarrow ExecuteResearchProgram\\
&\rightarrow Prove/Disprove/Compute\\
&\rightarrow VerifyFaithfulness\\
&\rightarrow DischargeObligations\\
&\rightarrow BridgeExistingMathematics\\
&\rightarrow NoveltyAudit\\
&\rightarrow TheoryPackage\\
&\rightarrow UpdateResearchState_{t+1}.
\end{aligned}
}
$$

並允許：

$$
STOP,
DEFER,
IDLE,
ESCALATE.
$$

因此自主研究不是：

$$
\text{always keep thinking}.
$$

而是：

$$
\boxed{
\text{know when to research, when to repair, when to verify, when to stop, and when to ask for external judgment}.
}
$$

---

# 15. Verifier Ensemble：形式證明器不是唯一驗證器

AMRR 不應將所有數學問題強迫映射到單一 proof assistant。

定義：

$$
\mathcal V
=
\{
V_{formal},
V_{symbolic},
V_{numeric},
V_{sat},
V_{smt},
V_{cas},
V_{simulation},
V_{human}
\}.
$$

例如：

- Lean / Isabelle / Rocq：formal proof；
- CAS：symbolic algebra；
- SAT / SMT：有限邏輯與約束；
- numerical computation：數值檢驗；
- exhaustive search：有限反例搜尋；
- simulation：動態系統或機率結構的候選驗證；
- human expert：語義忠實、新穎性與研究價值。

因此：

$$
\boxed{
Verification
=
TypedVerifierSelection(State,Claim,Obligation).
}
$$

而不是：

$$
Verification=LeanOnly.
$$

---

# 16. Faithfulness：形式正確不代表形式化正確

autoformalization 的根本風險之一是 FormalStatement 可以 syntactically valid，甚至被成功證明，但仍未必忠於 informal source。

因此至少要分：

$$
WellFormed,
Faithful,
Provable.
$$

並保持：

$$
\boxed{
WellFormed
\not\Rightarrow
Faithful.
}
$$

以及：

$$
\boxed{
Provable(Formalized(Q))
\not\Rightarrow
Solved(Intended(Q)).
}
$$

Problem Identity Protocol 與 semantic faithfulness evaluator 必須共同工作。

---

# 17. Bridge to Existing Mathematics

每個被提升的新概念、新方法或新理論片段都應建立：

$$
BridgeSet(x)
=
\{
b_1,\ldots,b_n
\}.
$$

Bridge 可以是：

$$
EquivalentTo,
Generalizes,
Specializes,
ReducesTo,
Interprets,
IsomorphicTo,
IndependentFrom,
Uses,
Contradicts.
$$

這將 AI 生成數學從孤立符號系統變成知識網路中的可定位節點。

---

# 18. 新穎性必須時間化

對候選貢獻 $x$，AI 不能合理聲稱「從來沒有人發現過」，只能在給定知識邊界 $K_t$ 下聲稱：

$$
NovelCandidate(x\mid K_t).
$$

其中：

$$
K_t
=
\{
LiteratureRefs,
FormalLibraryRefs,
SearchScope,
DatasetVersions,
ToolOutputs
\}.
$$

因此可以建立：

$$
DiscoveryReceipt_t
=
(
ContributionRef,
KnowledgeBoundaryRef,
SearchScope,
PriorArtRefs,
NoveltyAssessment
).
$$

未來若發現舊文獻：

$$
NovelCandidate
\rightarrow
Rediscovered
$$

即可追加更新，而不需要篡改原研究歷史。

---

# 19. CTCL-ITR：研究歷史必須可重建

當 AI 可以自己改題、加假設、生成 lemma、提出方法、形成 conjecture、放棄路線、回退與切換 representation，單一 chat log 不再足以作為研究歷史。

應保存：

$$
History(AMRR)
=
(
V,E,\Phi,T,I
),
$$

其中：

- $V$：research / cognition / verification events；
- $E$：causal edges；
- $\Phi$：problem、theory、artifact、contract、obligation references；
- $T$：temporal coordinates；
- $I$：integrity evidence。

特別重要的是：

$$
ProblemChange
\rightarrow
MathChangeSet
\rightarrow
DecisionReceipt
\rightarrow
VerificationReceipt.
$$

因此未來可以回答「為什麼 AI 在第 37 輪加入這個假設？」而不是重新讓模型事後編一個理由。

---

# 20. 研究契約

AMRR 的 persistent input 不應只是 Problem，而可以定義為：

$$
\boxed{
ResearchGoal
+
ResearchEnvironment
+
ResearchContract.
}
$$

ResearchContract 可以包含：

$$
C_R
=
(
Scope,
AllowedMutations,
VerificationPolicy,
ComputeBudget,
LiteraturePolicy,
FormalizationPolicy,
EscalationPolicy,
Termination
).
$$

例如：

```text
Allowed:
- generate definitions and lemmas as candidates
- change representations
- search literature
- run Lean/CAS/numerical tools

Approval required:
- promote a new axiom
- claim novelty
- change the canonical problem statement
- mark a theory package as submission-ready

Denied:
- erase original problem identity
- report a restricted theorem as proof of the unrestricted theorem
- fabricate citations
```

這使「自主」與「任意更改數學」正式分離。

---

# 21. 數學合法性階梯

本文提出第一版 promotion ladder：

$$
Generated
$$

$$
\downarrow
$$

$$
WellFormed
$$

$$
\downarrow
$$

$$
Faithful
$$

$$
\downarrow
$$

$$
Verified
$$

$$
\downarrow
$$

$$
TheoryCoherent
$$

$$
\downarrow
$$

$$
Bridged
$$

$$
\downarrow
$$

$$
Nontrivial
$$

$$
\downarrow
$$

$$
NovelCandidate
$$

$$
\downarrow
$$

$$
ResearchUseful
$$

$$
\downarrow
$$

$$
SubmissionReady.
$$

最後仍必須保持：

$$
\boxed{
SubmissionReady
\not\Rightarrow
CommunityAccepted.
}
$$

數學共同體的接受不能由 AI Runtime 自我授權。

---

# 22. AMRR 與現有研究方向的關係

本文不主張 autonomous mathematics、formal theorem proving、autoformalization、conjecturing 或 theory exploration 是本文首次提出。相反，本文建立在這些方向已經快速成熟的事實上。

現有研究已經分別證明：

1. AI 可以進行長程自然語言數學研究與反覆修訂；
2. LLM 與形式證明器結合可以在部分開放問題上產生可機器驗證結果；
3. 真實世界 mathematical definitions 的 autoformalization 明顯比受控 benchmark 更困難，且需要 formal-library grounding 與外部 feedback；
4. autoformalization 正從 isolated statements 轉向完整 theory dependencies；
5. 數學研究 AI 的核心問題已不再只剩 competition benchmark accuracy。

本文所提出的新增統合層是：

$$
\boxed{
DomainDiagnosis
+
TypedGapRepair
+
ProblemIdentity
+
ObligationGeneration
+
TheoryLevelCompletion
+
TemporalCausalGovernance.
}
$$

本文的主要研究問題是：

> **這六項能力是否能被組合為一個可持續運行、可驗證、可審計的自主數學研究 Runtime？**

---

# 23. 與一般 Agent 的差異

一般 research agent 可能遵循：

$$
Task
\rightarrow
Plan
\rightarrow
ToolUse
\rightarrow
Answer.
$$

AMRR 則需要：

$$
ResearchGoal
\rightarrow
ProblemState
\rightarrow
GapDiagnosis
\rightarrow
ResearchAgenda
\rightarrow
TheoryMutationCandidate
\rightarrow
Obligation
\rightarrow
Verification
\rightarrow
TheoryUpdate.
$$

因此最關鍵差異不是「多幾個工具」，而是：

$$
\boxed{
\text{mathematical objects and mathematical mutations become first-class runtime state}.
}
$$

---

# 24. 最小 falsification gates

本文不應以「AI 看起來會研究」作為驗證。

## Gate M0 — State Encoding

相同公開研究狀態是否得到：

$$
CanonicalMathematicalState?
$$

## Gate M1 — Gap Diagnosis

給定人工構造的缺定義、缺假設、錯表示、缺 lemma 等案例：

$$
PredictedGap
\approx
GroundTruthGap?
$$

## Gate M2 — Problem Identity

AI 是否能在改題後保持：

$$
Q_0
\neq
Q_1
$$

並正確分類變換？

## Gate M3 — Obligation Coverage

生成新的數學物件時，是否能產生必要 obligation？

## Gate M4 — Repair Validity

候選補全是否真的解除原 gap，而不是製造新未標記問題？

## Gate M5 — Verification Routing

系統是否能選擇適合的 verifier，而非對所有任務使用同一工具？

## Gate M6 — Bridge Accuracy

新生成理論與既有數學的關係是否可被外部檢查？

## Gate M7 — Long-Horizon Research

只提供：

$$
ResearchGoal
+
Environment
+
Contract
$$

後，系統是否能持續：

$$
50\sim100
$$

個 research transitions，而不依賴人類逐輪給下一個 prompt？

---

# 25. 評估不應只有「解出幾題」

AMRR evaluator 至少應分為：

$$
Score
=
(
P,
D,
R,
I,
O,
V,
B,
N,
C
).
$$

其中：

- $P$：problem-solving performance；
- $D$：domain diagnosis accuracy；
- $R$：repair validity；
- $I$：problem identity preservation；
- $O$：obligation coverage / discharge；
- $V$：verification correctness；
- $B$：bridge quality；
- $N$：novelty calibration；
- $C$：continuity / auditability。

因此：

$$
TaskSuccess
\neq
ResearchProcessValidity.
$$

一個 AI 可能碰巧得到正確答案，但過程中偷偷改題。反過來，它也可能沒有證成最終 conjecture，卻正確發現原猜想為 false，找到反例並完成問題重新分類。後者不能簡單記為 failure。

---

# 26. 可否證性

本文框架可能在多個層級失敗。例如：

1. 多域分類對實際研究沒有預測力；
2. Gap diagnosis 比直接讓模型自由研究更差；
3. Obligation generation 造成成本遠高於收益；
4. Problem identity tracking 無法處理高度漸進式的數學重構；
5. Theory bridging 高度依賴人工專家；
6. 長程自治造成 error accumulation；
7. formal verification 與 semantic faithfulness 的成本過高；
8. autonomy loop 只是在放大模型既有偏誤。

因此本文不是把 AMRR 定義成必然成立的未來，而是提出：

$$
\boxed{
Architecture
\rightarrow
Capability
\rightarrow
FalsificationGate.
}
$$

只有每一層能力通過相應實驗，才應升格下一層自治。

---

# 27. 研究限制

第一，本文目前主要是一篇理論與架構論文，而不是大規模 empirical evaluation。

第二，多域 ontology 是第一版 active taxonomy，不應被誤認為數學研究的終極分類。

第三，數學語義、interestingness 與 novelty 不能被形式證明器完全取代。

第四，形式化本身可能改變問題表示，因此 formalization 也必須受 Problem Identity 與 Faithfulness 約束。

第五，自主研究的功能性定義不等於哲學意義上的主體性、意識或人格。

第六，本文所稱「domain completion」是局部研究作用域內的結構補全，不主張有限系統可以完成整個開放數學。

---

# 28. 本文主要貢獻

本文的核心貢獻可以收斂為七點。

第一，提出：

$$
\boxed{
Unsolved
\neq
SingleFailureMode
}
$$

並建立多域數學問題診斷框架。

第二，提出 **Mathematical Domain Gap Map**，讓缺口成為一級研究狀態。

第三，提出 **Constrained Mathematical Domain Completion (CMDC)**，允許 AI 生成缺失數學，但要求生成與 certification 分離。

第四，提出 **Problem Identity Protocol** 與 **Mathematical ChangeSet**，允許改題而禁止無聲改題。

第五，提出 **Mathematical Obligation Generator**：

$$
Generation
\rightarrow
Obligation.
$$

第六，將 Domain Diagnosis、CMDC、Obligations、Bridge、Verification 與 Addressable Cognitive Runtime、CTCL-ITR 統合為：

$$
\boxed{
AutonomousMathematicalResearchRuntime.
}
$$

第七，提出可否證的 Gate-based research program，而不是以模型自述或單一 task score 判斷自主數學能力。

---

# 29. 核心命題

本文最終主張不是「AI 應該被允許自由修改數學問題」，而是：

$$
\boxed{
\text{A mathematical research AI must be able to diagnose, repair, extend, verify, and integrate mathematics without silently changing what it claims to have solved.}
}
$$

中文：

> **真正的自主數學研究 AI，不只是自行尋找答案，而是能辨認目前缺少哪一種數學結構、在受約束條件下提出補全、為每一次生成承擔對應的數學義務、保留原問題身份，並把新的局部理論重新接回可驗證的人類數學網路。**

因此：

$$
\boxed{
AutonomousMathematics
\neq
UnboundedGeneration.
}
$$

更合理的是：

$$
\boxed{
AutonomousMathematics
=
SelfDirectedResearch
+
ConstrainedTheoryChange
+
Verification
+
Provenance.
}
$$

---

# 30. 結論

數學 AI 正從「計算工具」向「推理系統」、「證明系統」與「研究 Agent」快速演進。然而，如果下一階段只是增加推理 token、擴大搜尋或接入更多 proof tools，仍然沒有處理數學研究最根本的一類困難：研究者經常需要先判定自己究竟問對了什麼、缺少了什麼、哪些東西可以修改、哪些修改改變了問題、哪些新構造值得被提升成正式數學對象。

本文因此提出從：

$$
Question
\rightarrow
Answer
$$

轉向：

$$
\boxed{
ResearchGoal
\rightarrow
Diagnose
\rightarrow
Repair
\rightarrow
Construct
\rightarrow
Verify
\rightarrow
Bridge
\rightarrow
Update.
}
$$

在此框架中，AI 不再只有「解題能力」，而開始具有 problem diagnosis、problem repair、theory construction、method generation、obligation management、verification routing 以及 research-history continuity。

這些能力共同構成本文所稱的：

$$
\boxed{
\text{Autonomous Mathematical Research Runtime}.
}
$$

但真正的自治並不來自取消約束。恰恰相反：

$$
\boxed{
\text{the stronger the generative autonomy, the stronger the required mathematical accountability}.
}
$$

後續第二篇將專門形式化 **多域問題診斷與 CMDC**；第三篇將集中處理 **Problem Identity、Theory Extension 與 Mathematical Obligations**；第四篇則把本文的統合理論壓入可執行的 **AMRR architecture**。在四篇理論完成後，技術白皮書將固定 canonical schemas、registry、verifier adapters、CTCL events、research contracts 與 MVP gates，最後再以獨立 empirical paper 評估實際的自主研究能力。

---

# 參考文獻

[1] Feng, T., Trinh, T. H., Bingham, G., et al. (2026). *Towards Autonomous Mathematics Research*. arXiv:2602.10177.

[2] Tsoukalas, G., Kovsharov, A., Shirobokov, S., et al. (2026). *Advancing Mathematics Research with AI-Driven Formal Proof Search*. arXiv:2605.22763.

[3] Min, M. J., He, M., Li, Z., Yi, Z., Malik, S., Gupta, A., Si, X., & Bastani, O. (2026). *Theory-Level Autoformalization: From Isolated Statements to Unified Formal Knowledge Bases*. arXiv:2607.13292. ICML 2026 Spotlight.

[4] Zhang, L., Valentino, M., & Freitas, A. (2025). *Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions*. Proceedings of EMNLP 2025, 1720–1738. DOI: 10.18653/v1/2025.emnlp-main.90.

[5] Zhang, L., Quan, X., & Freitas, A. (2024). *Consistent Autoformalization for Constructing Mathematical Libraries*. Proceedings of EMNLP 2024, 4020–4033. DOI: 10.18653/v1/2024.emnlp-main.233.

---

# 內部架構依賴文件

[I1] Neo.K. (2026). *從自提示到自主認知閉環：持續目標型 AI 的基礎理論*，系列 01/06，v0.1.

[I2] Neo.K. (2026). *可定址認知空間：Cognitive Affordance、Semantic Address 與認知算子*，系列 02/06，v0.1.

[I3] Neo.K. (2026). *自我對話不是文字：AI-Native Cognitive Program 與 Zero-Rendering Runtime*，系列 03/06，v0.1.

[I4] Neo.K. (2026). *時間因果自我史：CTCL-ITR、Decision Receipt 與上下文壓縮後的可追溯性*，系列 04/06，v0.1.

[I5] Neo.K. (2026). *契約邊界內的 AI 自主性：Execute、Refuse、Defer、Idle 與 Escalate*，系列 05/06，v0.1.

[I6] Neo.K. (2026). *Addressable Cognitive Runtime × CTCL：統一技術白皮書與實作路線圖 v0.1*，系列 06/06.

---

# 版本備註

**v0.1 / 2026-08-22**

本版固定：AMRR、CMDC、Mathematical Research Domain Set、Mathematical Domain Gap Map、Problem Identity Protocol、Mathematical ChangeSet、Mathematical Obligation Generator、Local Domain Completion、Verifier Ensemble、Bridge / Novelty / CTCL-ITR integration、falsification gates，以及後續四篇論文與技術白皮書的依賴關係。

本版不宣稱已完成 empirical validation；任何有關能力優勢的主張均留待後續 MVP 與實驗論文驗證。
