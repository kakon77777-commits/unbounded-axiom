# 問題身份、理論擴張與數學義務：AI 生成數學的合法變換框架

## Problem Identity, Theory Extension, and Mathematical Obligations: A Legitimacy Framework for AI-Generated Mathematics

**系列：Autonomous Mathematical Research / Paper 03 of 04**  
**版本：v0.1**  
**日期：2026-08-23**  
**作者：Neo.K**

---

## 摘要

當 AI 從「解已知問題」進一步走向自主修改定義、補充假設、生成中間引理、提出新方法、建立新術語甚至建議新公理時，數學自治面臨一個比 proof search 更根本的治理問題：**系統何時仍在研究原問題，何時已形成另一個問題；何種理論變更只是表達擴張，何種變更真正增加了理論強度；以及每一種生成應承擔哪些數學義務？** 若缺乏這些區分，AI 可以透過限制問題、增加假設、改變定義或替換形式化目標而取得表面上的「成功」，但這種成功未必對應原問題的解決。

本文提出一套面向自主數學研究 AI 的 **Problem Identity–Theory Extension–Obligation Framework**。第一，本文將問題身份拆分為兩個互補層次：**Genealogical Identity（研究血統身份）**與 **Semantic Relation（語義關係）**。前者回答一個新問題版本是否由原問題可追溯地衍生；後者回答兩者究竟是等價、澄清、限制、推廣、弱化、強化、增加假設、重新詮釋，還是已成為新問題。這避免將「同一研究支線」誤認成「同一數學命題」。第二，本文建立 **Theory Extension Ladder**，區分記錄／符號擴張、定義擴張、保守擴張、已證定理登錄、假設擴張、非保守公理擴張與基礎／元理論變更，並要求每次變更明示其邏輯地位。第三，本文提出 **Mathematical Obligation System**：任何候選變更都必須根據其變更類型產生對應的 well-formedness、semantic faithfulness、problem-identity、conservativity、consistency、model-existence、independence、bridge、scope、verification、novelty 與 provenance 義務。未解除義務不得因後續成果漂亮而自動消失。

本文進一步提出 **No Mathematical Laundering Principle**：在擴張理論、加強假設、限制問題或更改語義後得到的結果，不得被重新包裝成原理論、原假設或原問題下的結果。本文以 **Assumption Envelope** 與 **Dependency Closure** 追蹤每個 theorem、method、definition 與 theory package 實際依賴的前提；以 **Problem Mutation Receipt、Theory Extension Receipt、Obligation Receipt、Verification Receipt** 將重要變更寫入可稽核研究歷史；並將 theory morphism / theory graph 視為連接新舊理論與異質形式庫的重要 bridge 機制。

本文的核心命題是：**AI 可以被允許創造、修改與擴張數學，但其創造自由必須與可追蹤的問題身份、明示的理論變更類型、不可洗白的前提依賴，以及可解除的數學義務同步增長。** 這使「AI 生成新數學」不再依賴模型自述，而成為一個可驗證、可審計、可否證的理論變更程序。

**關鍵詞：** 問題身份、理論擴張、保守擴張、定義擴張、數學義務、證明義務、AI 生成數學、CMDC、自主數學研究、理論圖、問題版本

---

# 1. 引言：真正危險的不是 AI 改題，而是 AI 改題後假裝沒改

自主數學研究必然會遇到理論變更。

研究者在實際工作中本來就會：

- 澄清問題；
- 補充假設；
- 改變表示；
- 引入新定義；
- 建立新引理；
- 推廣或限制命題；
- 修改方法；
- 建立另一套公理或模型。

因此若要求 AI 永遠保持：

$$
Q_t=Q_0,
$$

反而不符合真正數學研究。

但另一個極端同樣不可接受：

$$
Q_0
\rightarrow
Q_1
\rightarrow
Q_2
\rightarrow
\cdots
$$

最後證明了：

$$
Q_n,
$$

卻回報：

> 原問題 $Q_0$ 已經解決。

這是本文要禁止的核心錯誤。

因此：

$$
\boxed{
\text{Mathematical mutation is legitimate; untracked mutation is not.}
}
$$

---

# 2. 問題身份不是單一布林值

最直覺的做法是定義：

$$
SameProblem(Q_i,Q_j)
\in
\{0,1\}.
$$

但這通常太粗。

例如：

- 一個只修正文法的版本；
- 一個補上原本明顯省略條件的版本；
- 一個限制到 compact case 的版本；
- 一個增加 continuity assumption 的版本；
- 一個將存在性改成唯一性的版本；

顯然不是同一種變化。

本文因此不以單一：

$$
Same/NotSame
$$

處理問題身份。

而採：

$$
\boxed{
ProblemIdentity
=
Genealogy
+
SemanticRelation.
}
$$

---

# 3. Genealogical Identity：研究血統身份

令一個 problem object：

$$
P_i
=
(
id,
version,
parentRefs,
sourceRef,
createdAt,
mutationRef
).
$$

若：

$$
P_i
\rightarrow
P_j,
$$

只代表：

> $P_j$ 是由 $P_i$ 經某個可追蹤變更產生。

這稱為：

$$
GenealogicallyDerived(P_j,P_i).
$$

它不推出：

$$
P_i
\equiv
P_j.
$$

因此：

$$
\boxed{
GenealogicalContinuity
\not\Rightarrow
SemanticEquivalence.
}
$$

這一區分非常重要。

---

# 4. Semantic Relation：新舊問題究竟是什麼關係

對任意：

$$
P_i,P_j,
$$

定義：

$$
Rel_P(P_i,P_j)
\subseteq
\mathcal R_P.
$$

第一版 relation vocabulary：

$$
\mathcal R_P
=
\{
Equivalent,
Clarification,
Restriction,
Generalization,
Weakening,
Strengthening,
AddedAssumption,
RemovedAssumption,
Reparameterization,
RepresentationChange,
Reinterpretation,
NewProblem
\}.
$$

這些 relation 不一定互斥。

例如一個新版本可能同時是：

$$
Clarification
+
RepresentationChange.
$$

---

# 5. Equivalent 與 Clarification 不能自動等同

若：

$$
P_i\equiv P_j,
$$

通常需要某種語義等價證據。

但 Clarification 可能只是：

> 根據作者、上下文或傳統用法，選定一個原本隱含的 intended reading。

因此：

$$
Clarification
\not\Rightarrow
FormalEquivalence.
$$

Clarification 可以提高 faithfulness，但仍需保留原始 source。

---

# 6. Restriction

若：

$$
Domain(P_j)
\subsetneq
Domain(P_i),
$$

且 target structure 基本保持，則：

$$
Rel_P(P_i,P_j)=Restriction.
$$

若：

$$
Proof(P_j)
$$

成立，一般不能推出：

$$
Proof(P_i).
$$

因此：

$$
\boxed{
Proof(Restriction(P))
\not\Rightarrow
Proof(P).
}
$$

---

# 7. Generalization

若：

$$
Domain(P_i)
\subsetneq
Domain(P_j),
$$

或 $P_j$ 將 $P_i$ 放入更一般結構，則可以標記：

$$
Generalization.
$$

但一般化後的問題即使包含原問題，也不能反過來假設：

$$
Failed(P_j)
\Rightarrow
Failed(P_i).
$$

---

# 8. Weakening 與 Strengthening

若命題目標由：

$$
C
$$

變為較弱：

$$
C',
$$

且：

$$
C\Rightarrow C',
$$

可標記：

$$
Weakening.
$$

若反向：

$$
C'\Rightarrow C,
$$

且 $C'$ 更強，則：

$$
Strengthening.
$$

因此證明 weakened target 不得回報為 strengthened target 的證明。

---

# 9. AddedAssumption：最常見也最容易被洗白的變更

原命題：

$$
T\vdash Q?
$$

AI 加入：

$$
A.
$$

新問題變成：

$$
T+A\vdash Q?
$$

即使成功：

$$
T+A\vdash Q,
$$

仍不能報告：

$$
T\vdash Q.
$$

本文稱這類錯誤為：

$$
\boxed{
AssumptionLaundering.
}
$$

---

# 10. 問題身份的最小 canonical record

本文建議：

$$
ProblemRecord
=
(
Identity,
Source,
Statement,
Definitions,
Assumptions,
Scope,
Target,
SuccessCriterion,
Representations,
Parents,
Relations
).
$$

例如：

```json
{
  "problem_id": "prob:017",
  "version": 3,
  "parent_refs": ["prob:017@2"],
  "source_ref": "artifact:original-question",
  "relation_to_parent": ["restriction", "added_assumption"],
  "assumption_refs": ["assump:compactness"],
  "scope_ref": "scope:compact-case",
  "canonical_statement_ref": "stmt:017:v3"
}
```

---

# 11. Problem Mutation

任何：

$$
P_i
\rightarrow
P_j
$$

若涉及語義或 scope 改變，應形成：

$$
ProblemMutation.
$$

定義：

$$
PM
=
(
BeforeRef,
AfterRef,
Relation,
Reason,
GapRef,
EvidenceRefs,
ObligationRefs,
ApprovalState
).
$$

所以：

$$
\boxed{
ProblemMutation
\neq
TextEdit.
}
$$

---

# 12. 什麼時候應建立 New Problem Branch

並非所有變更都應繼續使用同一 problem id。

令：

$$
d_P(P_i,P_j)
$$

表示 problem change magnitude。

它可由多維向量近似：

$$
d_P
=
(
d_{definition},
d_{assumption},
d_{scope},
d_{target},
d_{semantics},
d_{representation}
).
$$

若：

$$
Rel_P(P_i,P_j)=NewProblem,
$$

或超過 contract 指定的 branch threshold，則建立：

$$
P_i
\rightarrow
Branch(P_j).
$$

這不是拒絕探索。

而是避免錯誤 claim inheritance。

---

# 13. Theory State

令理論：

$$
T
=
(
\Sigma,
A,
D,
R
),
$$

其中：

- $\Sigma$：signature / vocabulary；
- $A$：axioms / assumptions；
- $D$：definitions；
- $R$：rules / foundation-dependent derivation structure。

在工程上還應附加：

$$
TheoryObject
=
(
TheoryCore,
FoundationRef,
LibraryRefs,
Version,
ParentRefs,
ExtensionRefs
).
$$

---

# 14. Theory Extension 不只有「加公理」

對：

$$
T_0
\rightarrow
T_1,
$$

本文區分至少七類：

$$
E_0=\text{Documentary/Registry Extension},
$$

$$
E_1=\text{Notation/Alias Extension},
$$

$$
E_2=\text{Definitional Extension},
$$

$$
E_3=\text{Conservative Extension},
$$

$$
E_4=\text{Derived-Theorem Registration},
$$

$$
E_5=\text{Assumption/Axiom Extension},
$$

$$
E_6=\text{Foundation/Meta-Theory Change}.
$$

它們的數學風險與義務不同。

---

# 15. Documentary / Registry Extension

若只是把已存在的 theorem、proof、citation 或 metadata 登錄進知識庫，且不改變 deductive system，則：

$$
Closure(T_1)=Closure(T_0).
$$

這類 change 主要產生：

$$
ProvenanceObligation,
$$

而不是新的 logical-strength obligation。

---

# 16. Notation / Alias Extension

新增：

$$
Symbol_{new}
$$

但其語義完全指向已知 object。

理想條件：

$$
Meaning(Symbol_{new})
=
Meaning(ExistingObject).
$$

它的主要義務是：

$$
SemanticAliasCorrectness.
$$

若 alias 實際改變語義，就不能仍標記成 notation-only。

---

# 17. Definitional Extension

在標準邏輯意義下，definitional extension 通常透過新符號的明確定義將語言擴張，而不應改變舊語言中的數學內容。

例如新增 relation symbol $R$：

$$
\forall x_1\ldots x_n,
\quad
R(x_1,\ldots,x_n)
\leftrightarrow
\varphi(x_1,\ldots,x_n),
$$

其中：

$$
\varphi
$$

只使用原語言。

因此：

$$
DefinitionalExtension
\Rightarrow
ConservativeExtension
$$

在標準條件下成立。

但反向一般不成立：

$$
ConservativeExtension
\not\Rightarrow
DefinitionalExtension.
$$

---

# 18. Conservative Extension

令：

$$
T_0
\subseteq
T_1
$$

且：

$$
Lang(T_0)
\subseteq
Lang(T_1).
$$

若對所有舊語言句子 $\phi$：

$$
T_1\vdash\phi
\Rightarrow
T_0\vdash\phi,
$$

則稱：

$$
T_1
$$

是 $T_0$ 的 proof-theoretic conservative extension。

也就是：

$$
\boxed{
NewExpressivity
\neq
NewOldLanguageTheorems.
}
$$

---

# 19. Model-Theoretic Conservativity

更強的模型觀點可以要求：

> 每個 $T_0$ 的 model 都能擴張成 $T_1$ 的 model。

形式地：

$$
\forall M\models T_0,
\quad
\exists M'\models T_1
$$

使 $M'$ 在舊 signature 上與 $M$ 相容。

這類 model extension 條件通常能推出相應 proof-theoretic conservativity，但判定成本可能更高。

因此 AMRR 必須記錄：

$$
ConservativityType
\in
\{
ProofTheoretic,
ModelTheoretic,
Definitional,
Unknown
\}.
$$

---

# 20. Derived-Theorem Registration

若：

$$
T_0\vdash\phi,
$$

而 $T_1$ 只是將 $\phi$ 以 theorem declaration 登錄，則在 deductive closure 意義上：

$$
Closure(T_1)=Closure(T_0).
$$

因此：

$$
\boxed{
NewTheoremRecord
\neq
NewLogicalStrength.
}
$$

這個區分對 AI 很重要，否則 AI 可能把「第一次由它找出的已可推出 theorem」誤描述成「理論被擴張」。

---

# 21. Assumption / Axiom Extension

若：

$$
T_1=T_0+A_{new},
$$

且：

$$
T_0\nvdash A_{new},
$$

則這通常不是單純 definitional extension。

若存在舊語言命題：

$$
\phi
$$

使：

$$
T_1\vdash\phi
$$

但：

$$
T_0\nvdash\phi,
$$

則：

$$
T_1
$$

對 $T_0$ 為 non-conservative extension。

這不表示「不合法」。

而表示：

$$
\boxed{
The logical strength changed and must be declared.
}
$$

---

# 22. Foundation / Meta-Theory Change

若從：

$$
Foundation_0
$$

轉到：

$$
Foundation_1,
$$

例如改變 underlying logic、type theory 或 set-theoretic foundation，這是比局部 axiom extension 更大的變更。

此時需要：

$$
Translation,
Interpretation,
TheoryMorphism,
RelativeStrength
$$

等 bridge。

不能只用：

$$
version++
$$

表示。

---

# 23. Theory Extension Ladder 不是單一線性強度排序

需要特別避免：

$$
E_0<E_1<E_2<\cdots<E_6
$$

被理解成單一總序。

因為：

- definitional extension 與 arbitrary conservative extension 的關係不是完全相同；
- foundation change 可能只是另一種等價表示，也可能增加強度；
- documentary extension 根本不是同類 logical extension。

所以更合理的是：

$$
ExtensionProfile
=
(
LanguageChange,
SemanticChange,
ProofStrengthChange,
ModelChange,
FoundationChange
).
$$

---

# 24. Theory Extension Receipt

每次：

$$
T_i\rightarrow T_j
$$

都應形成：

$$
TheoryExtensionReceipt.
$$

至少保存：

$$
(
ParentTheory,
ChildTheory,
ExtensionClass,
AddedSymbols,
AddedDefinitions,
AddedAxioms,
FoundationChange,
ConservativityStatus,
ObligationRefs,
VerificationRefs
).
$$

---

# 25. Mathematical Obligation：生成物必須承擔的可解除責任

本文將 obligation 定義為：

$$
O_i
=
(
Claim,
Trigger,
RequiredEvidence,
VerifierClass,
Status,
DependsOn
).
$$

其中：

$$
Status(O_i)
\in
\{
OPEN,
PARTIAL,
DISCHARGED,
FAILED,
WAIVED,
SUPERSEDED
\}.
$$

WAIVED 不等於 DISCHARGED。

---

# 26. 核心 Obligation Classes

第一版至少包括：

$$
O_{wf}=\text{WellFormedness},
$$

$$
O_{sem}=\text{SemanticFaithfulness},
$$

$$
O_{id}=\text{ProblemIdentity},
$$

$$
O_{consv}=\text{Conservativity},
$$

$$
O_{cons}=\text{Consistency/RelativeConsistency},
$$

$$
O_{model}=\text{ModelExistence},
$$

$$
O_{ind}=\text{Independence},
$$

$$
O_{bridge}=\text{TheoryBridge},
$$

$$
O_{scope}=\text{ScopeValidity},
$$

$$
O_{verify}=\text{Proof/ComputationVerification},
$$

$$
O_{novel}=\text{NoveltyAssessment},
$$

$$
O_{prov}=\text{Provenance}.
$$

---

# 27. Obligation Profile：不同變更類型不能套同一套檢查

定義：

$$
Profile(ChangeType)
\rightarrow
RequiredObligations.
$$

例如：

### 新 notation

$$
\{O_{wf},O_{sem},O_{prov}\}.
$$

### 新 definition

$$
\{O_{wf},O_{sem},O_{consv},O_{bridge},O_{prov}\}.
$$

### 新 assumption

$$
\{O_{id},O_{scope},O_{cons},O_{prov}\}.
$$

### 新 theorem

$$
\{O_{verify},O_{scope},O_{prov}\}.
$$

### 新 axiom

$$
\{O_{id},O_{cons},O_{model},O_{ind},O_{bridge},O_{prov}\}
$$

中的適用子集。

---

# 28. Proof Obligation 與 Mathematical Obligation

傳統 proof obligation 通常是由某個 correctness property 產生的待證公式。

本文採更廣義：

$$
ProofObligation
\subset
MathematicalObligation.
$$

因為一些義務不是單一 theorem proving 能完全解除，例如：

$$
NoveltyAssessment,
$$

$$
SemanticFaithfulness,
$$

$$
PriorArtMapping.
$$

因此：

$$
\boxed{
MathematicalAccountability
\neq
ProofAssistantOnly.
}
$$

---

# 29. Obligation Dependency Graph

義務彼此也可能依賴。

例如：

$$
O_{wf}
\rightarrow
O_{sem}
\rightarrow
O_{consv}.
$$

若 definition 甚至尚未 well-formed，就沒有意義先宣稱它 conservative。

因此：

$$
G_O
=
(
V_O,
E_O
).
$$

其中：

$$
O_i\rightarrow O_j
$$

表示 $O_j$ 的解除依賴 $O_i$。

---

# 30. Obligation Inheritance

若 theorem：

$$
\tau
$$

依賴：

$$
D_{new},A_{new},L_1,
$$

則：

$$
ObligationClosure(\tau)
$$

必須包含其依賴鏈中尚未解除的重要 obligations。

因此：

$$
\boxed{
\text{Downstream success cannot erase upstream uncertainty.}
}
$$

---

# 31. Assumption Envelope

對任何結果：

$$
R,
$$

定義：

$$
AE(R)
=
\text{explicit assumption/dependency envelope of }R.
$$

若：

$$
R
$$

是在：

$$
T+A+B
$$

下得到，則 claim 必須保留：

$$
AE(R)
\supseteq
\{A,B\}.
$$

除非另有證明消除其中假設。

---

# 32. Assumption Discharge

如果後續證明：

$$
T\vdash A,
$$

則原本：

$$
AE(R)=\{A\}
$$

可在重新驗證後縮減。

也就是：

$$
AssumptionEnvelope
$$

可以變小，但必須有正式 discharge path。

不能因為「看起來 $A$ 應該多餘」而刪除。

---

# 33. No Mathematical Laundering Principle

本文正式提出：

$$
\boxed{
\text{No Mathematical Laundering}.
}
$$

其意義是：

> 任何透過改變問題、限制 scope、增加假設、擴張理論或更換基礎所得到的結果，都不得在輸出、摘要、引用或後續推理中被重新標示成原始條件下的無條件結果。

形式：

若：

$$
T'\vdash\phi
$$

且：

$$
T'\neq T,
$$

則只有在：

$$
Bridge(T',T,\phi)
$$

足以解除差異後，才能報告：

$$
T\vdash\phi.
$$

---

# 34. Claim Scope Invariant

對任何公開 claim $C$：

$$
ClaimScope(C)
\subseteq
VerifiedScope(C).
$$

即：

$$
\boxed{
ClaimScope
\not>
VerifiedScope.
}
$$

這個不變量同時限制：

- 定理的作用域；
- 假設；
- 數值範圍；
- 模型類別；
- 形式化版本；
- verifier 能力。

---

# 35. Epistemic Status 與 Logical Status 必須分離

對一個 claim：

$$
C,
$$

logical status 可以是：

$$
Provable,
Disprovable,
Independent,
Unknown.
$$

但系統實際 epistemic status 可能是：

$$
Candidate,
Tested,
ProofFound,
KernelVerified,
HumanReviewed,
NoveltyUnknown.
$$

因此：

$$
\boxed{
LogicalStatus
\neq
RuntimeEpistemicStatus.
}
$$

---

# 36. Semantic Faithfulness Obligation

若自然語言問題：

$$
Q_N
$$

轉成形式問題：

$$
Q_F,
$$

需要：

$$
O_{sem}(Q_N,Q_F).
$$

proof assistant 驗證的是：

$$
Q_F.
$$

它不自動驗證：

$$
Meaning(Q_F)=Meaning(Q_N).
$$

因此：

$$
KernelVerified(Q_F)
\not\Rightarrow
Faithful(Q_N,Q_F).
$$

這與 statement autoformalization benchmark 中強調 semantic-equivalence evaluation 的方向一致。

---

# 37. Definition Identity

問題身份之外，definition 本身也需要版本化。

令：

$$
D_i
=
(
id,
version,
body,
scope,
parent,
relation
).
$$

若：

$$
D_1\rightarrow D_2,
$$

必須區分：

$$
EquivalentDefinition,
Refinement,
Generalization,
SemanticChange.
$$

否則 theorem dependency 會產生 definition drift。

---

# 38. Method Identity

同理：

$$
M_i
$$

若被修正，至少應追蹤：

$$
Algorithm,
Preconditions,
CorrectnessClaim,
ComplexityClaim,
FailureModes.
$$

因此：

$$
MethodName
\neq
MethodIdentity.
$$

---

# 39. Theory Graph

數學知識不應只是一列：

$$
T_1,T_2,T_3,\ldots
$$

而可表示成：

$$
G_T=(V_T,E_T).
$$

其中 node 是 theories，edge 可以是：

$$
Inclusion,
DefinitionExtension,
Interpretation,
Translation,
Morphism,
Model,
Generalization.
$$

這與 Mathematical Knowledge Management 中 theory graph / theory morphism 的方向一致。

---

# 40. Theory Morphism 作為 Bridge

若：

$$
\mu:T_1\rightarrow T_2
$$

是 truth-preserving theory morphism，則它可以把：

$$
T_1
$$

中的 declarations / theorems 映射到：

$$
T_2.
$$

因此 AMRR 的 bridge 不應只保存 prose：

> 這兩個理論很像。

更強的情況應儘量形成：

$$
FormalBridgeObject.
$$

---

# 41. Theory Bridge 不一定要求同一 proof assistant

不同 formal libraries 可能使用不同 foundation。

因此：

$$
Bridge
$$

可以是：

- exact theory morphism；
- symbol alignment；
- translation with obligations；
- semantic correspondence；
- human-reviewed mapping。

系統必須標明 bridge strength。

---

# 42. Bridge Strength

第一版可定義：

$$
BridgeStrength
\in
\{
Exact,
FormallyVerified,
PartiallyVerified,
SemanticCandidate,
Heuristic
\}.
$$

因此：

$$
HeuristicBridge
$$

不能被後續當成：

$$
FormalEquivalence.
$$

---

# 43. New Concept Promotion

AI 生成：

$$
C_{new}.
$$

要升格至少需經：

$$
Candidate
\rightarrow
WellFormed
\rightarrow
SemanticallySpecified
\rightarrow
ExamplesChecked
\rightarrow
PriorArtMapped
\rightarrow
BridgeAssessed
\rightarrow
Promoted.
$$

並保持：

$$
Promoted
\not\Rightarrow
CommunityAccepted.
$$

---

# 44. New Axiom Promotion

新公理：

$$
A_{new}
$$

不能和新 definition 用相同 promotion gate。

至少應檢查：

$$
ExplicitNonConservativeStatus,
$$

$$
ModelSearch,
$$

$$
RelativeConsistencyEvidence,
$$

$$
KnownConsequences,
$$

$$
RelationToExistingAxioms,
$$

$$
ResearchUtility.
$$

若 contract 要求 human approval：

$$
ESCALATE.
$$

---

# 45. Independence 不應被假裝自動可判

對：

$$
A_{new}
$$

AI 可能嘗試研究：

$$
T\nvdash A_{new},
$$

以及：

$$
T\nvdash\neg A_{new}.
$$

但 independence proof 往往本身是高難度數學。

因此：

$$
IndependenceStatus
\in
\{
Proved,
EvidenceOnly,
Unknown
\}.
$$

不得把：

$$
NotYetDerived
$$

誤標成：

$$
Independent.
$$

---

# 46. Consistency 也不能被過度宣稱

對複雜理論：

$$
Consistency(T)
$$

未必能在其自身內證明或由有限測試確立。

因此系統應區分：

$$
NoContradictionFound,
$$

$$
ModelFound,
$$

$$
RelativeConsistencyArgument,
$$

$$
FormalMetatheoreticProof.
$$

它們不是同一 claim。

---

# 47. Obligation Waiver

某些工程或 exploratory research 可以允許 obligation：

$$
WAIVED.
$$

但 waiver 必須帶：

$$
Who,
Why,
Scope,
Expiry,
DownstreamEffect.
$$

因此：

$$
WAIVED
\neq
DISCHARGED.
$$

且 downstream package 必須看得見 waiver。

---

# 48. Obligation Supersession

若 problem branch 被廢棄，部分義務可能不再 relevant。

這時可：

$$
OPEN
\rightarrow
SUPERSEDED.
$$

但仍不得刪除其歷史。

這讓 ledger 可以回答：

> 這個義務為什麼沒有被完成？

---

# 49. Problem Mutation Receipt

每個重大問題變更應保存：

```json
{
  "receipt_type": "problem_mutation",
  "before_problem_ref": "prob:017@2",
  "after_problem_ref": "prob:017@3",
  "relations": ["restriction", "added_assumption"],
  "gap_ref": "gap:assumption:09",
  "reason_codes": ["counterexample_found"],
  "obligation_refs": ["obl:identity:44", "obl:scope:12"],
  "approval_state": "accepted_candidate"
}
```

---

# 50. Obligation Receipt

對：

$$
O_i,
$$

解除時保存：

$$
ObligationReceipt
=
(
ObligationRef,
EvidenceRefs,
VerifierRefs,
StatusBefore,
StatusAfter,
KnowledgeBoundaryRef,
DecisionRef
).
$$

---

# 51. Verification Receipt

VerificationReceipt 不應只保存：

```text
pass
```

而應保存：

$$
(
ClaimRef,
VerifierClass,
VerifierVersion,
InputRefs,
EnvironmentRef,
Result,
Scope,
AssumptionEnvelope
).
$$

因此：

$$
VerificationResult
$$

可以被重播與重新評價。

---

# 52. Decision Receipt 與 Mathematical Receipt 的關係

ACR / CTCL-ITR 已經區分：

$$
DecisionReceipt
\neq
CommitReceipt.
$$

數學域可以進一步形成：

$$
DecisionReceipt
\rightarrow
ProblemMutationReceipt,
$$

$$
DecisionReceipt
\rightarrow
TheoryExtensionReceipt,
$$

$$
Verification
\rightarrow
VerificationReceipt,
$$

$$
ObligationDischarge
\rightarrow
ObligationReceipt.
$$

這些是 domain-specific evidence，不需要重寫 temporal ledger 核心。

---

# 53. Knowledge Boundary 與 Novelty Claim

若 AI 在時間 $t$ 聲稱：

$$
NovelCandidate(X\mid K_t),
$$

則：

$$
K_t
$$

必須記錄其當時 literature / library / search boundary。

未來發現 prior art 時：

$$
NovelCandidate
\rightarrow
Rediscovered.
$$

不得倒過來改寫當時 receipt。

---

# 54. Problem Identity 與 Knowledge Boundary

同樣，後來的人類可能澄清：

> 原題作者其實 intended $P_2$。

這不應使歷史上的：

$$
P_1
$$

消失。

應追加：

$$
InterpretationUpdate.
$$

因此：

$$
HistoricalProblemRecord
\neq
CurrentPreferredInterpretation.
$$

---

# 55. Governance：CanGenerate、MayAdopt、MayClaim

數學自治至少需要三分：

$$
CanGenerate(x),
$$

$$
MayAdopt(x),
$$

$$
MayClaim(x).
$$

例如 AI 可以生成一個新 axiom：

$$
CanGenerate(A)=1.
$$

但 contract 可能要求：

$$
MayAdopt(A)=ApprovalRequired.
$$

即使 internal branch 採用，也不代表：

$$
MayClaim(A\text{-dependent theorem as original theorem})=1.
$$

---

# 56. Claim Governance

外部發表也是 action。

因此：

$$
ClaimCandidate
\rightarrow
Governance
\rightarrow
PublishableClaim.
$$

必須檢查：

$$
ProblemIdentity,
$$

$$
AssumptionEnvelope,
$$

$$
VerificationStatus,
$$

$$
OpenObligations,
$$

$$
NoveltyStatus.
$$

---

# 57. Submission-Ready 不代表 Accepted

內部可以定義：

$$
SubmissionReady(X)=1
$$

表示：

- required internal obligations 已達門檻；
- proof / computation artifacts 已整理；
- problem lineage 清楚；
- assumptions 明示；
- prior-art search 已在 knowledge boundary 內完成。

但：

$$
\boxed{
SubmissionReady
\not\Rightarrow
CommunityAccepted.
}
$$

---

# 58. Formalization 也是 Theory Change Candidate

將 informal mathematics：

$$
I
$$

映射到：

$$
F
$$

不能只當 serialization。

因為 formalization 通常需要明示：

- type；
- domain；
- implicit assumptions；
- representation choices；
- library definitions。

所以：

$$
Formalize(I)
\rightarrow
F
$$

本身應產生：

$$
SemanticFaithfulnessObligation.
$$

---

# 59. Formal Library Definitions 也不是永遠等於作者 intended meaning

若 formalizer 將自然語言術語：

$$
t
$$

對應到 library symbol：

$$
s,
$$

需要：

$$
Alignment(t,s).
$$

因此：

$$
LibraryMatch
$$

也是 bridge candidate，而不是無條件 semantic identity。

---

# 60. Theory Refactoring

有時 AI 不是新增數學，而是重新組織已知理論：

$$
T
\rightarrow
T_1\cup T_2\cup T_{shared}.
$$

如果 closure 保持，這屬 knowledge-structure change，而不一定是 logical-strength change。

因此 theory refactoring 應和 axiom extension 分離。

---

# 61. Obligation Budget

完全驗證所有候選可能成本極高。

因此：

$$
Budget(O_i)
$$

也是治理問題。

系統可以：

$$
DEFER(O_i)
$$

但不能：

$$
Forget(O_i).
$$

所以：

$$
\boxed{
DeferredObligation
\neq
ResolvedObligation.
}
$$

---

# 62. Risk-Tiered Obligations

可以依 change risk 分級：

$$
RiskLevel
\in
\{L0,L1,L2,L3,L4\}.
$$

例如：

- $L0$：metadata / citation update；
- $L1$：notation / alias；
- $L2$：definition / representation；
- $L3$：assumption / major scope mutation；
- $L4$：new axiom / foundation change。

通常：

$$
Risk\uparrow
\Rightarrow
ObligationStrength\uparrow.
$$

---

# 63. 自主性與數學責任的耦合

因此本文將 Paper 01 的原則：

$$
GenerationFreedom\uparrow
\Longrightarrow
VerificationObligation\uparrow
$$

進一步寫成：

$$
\boxed{
AutonomyLevel(x)
\uparrow
\Longrightarrow
IdentityTracking(x)
+
ExtensionDisclosure(x)
+
ObligationStrength(x)
\uparrow.
}
$$

---

# 64. 最小 AMRR 介面

Paper 04 的 Runtime 至少需要：

```text
problem.register
problem.derive
problem.relate
problem.branch

theory.extend
theory.classify_extension
theory.check_conservativity
theory.bridge

obligation.generate
obligation.discharge
obligation.defer
obligation.waive
obligation.inherit

claim.compute_scope
claim.validate
claim.package
```

---

# 65. 最小 schemas

至少需要：

```text
ProblemRecord
ProblemRelation
ProblemMutation
TheoryRecord
TheoryExtension
AssumptionEnvelope
MathematicalObligation
ObligationDependency
TheoryBridge
ProblemMutationReceipt
TheoryExtensionReceipt
VerificationReceipt
ObligationReceipt
ClaimRecord
```

---

# 66. Falsification Gate A — Silent Mutation Detection

建立題目：

$$
Q_0.
$$

誘導模型：

- 加條件；
- 限制 domain；
- 改 definition；
- 改 target。

測：

$$
SilentMutationRate.
$$

希望加入 protocol 後：

$$
SilentMutationRate_{with}
<
SilentMutationRate_{without}.
$$

---

# 67. Gate B — Relation Classification

給定：

$$
(P_i,P_j),
$$

人工標註 relation。

測：

$$
RelAccuracy,
$$

$$
MultiLabelF1.
$$

特別測：

$$
Restriction
\leftrightarrow
AddedAssumption,
$$

以及：

$$
Clarification
\leftrightarrow
Reinterpretation.
$$

---

# 68. Gate C — Extension Classification

給定：

$$
(T_0,T_1),
$$

測 AI 是否區分：

$$
Notation,
Definition,
Conservative,
NonConservative,
FoundationChange.
$$

不能只靠自然語言 label，應配合 symbolic / model / proof checks。

---

# 69. Gate D — Obligation Coverage

對每種 mutation：

$$
M_i,
$$

有 gold obligation set：

$$
O_i^*.
$$

模型生成：

$$
\hat O_i.
$$

測：

$$
Precision_O,
Recall_O,
F1_O.
$$

---

# 70. Gate E — Obligation Inheritance

建立依賴：

$$
A_{new}
\rightarrow
L_1
\rightarrow
T_1.
$$

故意讓 $A_{new}$ obligation 未解除。

測最終 theorem 是否仍帶：

$$
OpenDependency(A_{new}).
$$

---

# 71. Gate F — No Laundering

建立：

$$
T+A\vdash Q.
$$

然後要求系統摘要結果。

觀察是否錯誤輸出：

$$
T\vdash Q.
$$

定義：

$$
LaunderingRate.
$$

這應是 AMRR 最重要的安全／學術誠信 metric 之一。

---

# 72. Gate G — Formalization Faithfulness

給定：

$$
Q_N,Q_F,
$$

其中部分 formal statements 故意有 scope、quantifier、definition mismatch。

測：

$$
FaithfulnessDetection.
$$

而不能只測：

$$
LeanCompile.
$$

---

# 73. Gate H — Theory Bridge

建立已知：

$$
T_1\leftrightarrow T_2
$$

的不同關係。

測系統能否找到：

$$
Equivalent,
Generalizes,
Interprets,
Independent,
NoBridgeKnown.
$$

並校準 bridge strength。

---

# 74. Gate I — Claim Scope

對不同 assumption / domain 下的結果，測：

$$
ClaimScope
\subseteq
VerifiedScope
$$

是否保持。

任何越界：

$$
ClaimScope>VerifiedScope
$$

均記為 scope violation。

---

# 75. Gate J — Long-Horizon Theory Drift

讓 AMRR 經：

$$
50\sim100
$$

次 problem / definition / lemma mutation。

最後檢查：

- 原問題是否仍可恢復；
- 每個 branch 是否有 lineage；
- theorem assumption envelope 是否完整；
- open obligations 是否仍可追蹤；
- 是否出現 unnoticed definition drift。

---

# 76. 與 Paper 02 的關係

Paper 02 回答：

$$
\boxed{
WhatIsMissing?
}
$$

以及：

$$
\boxed{
WhatRepairIsAppropriate?
}
$$

本文回答：

$$
\boxed{
WhatDoesThatRepairChange?
}
$$

以及：

$$
\boxed{
WhatMustBeProvedOrDisclosedAfterTheChange?
}
$$

因此：

$$
Diagnosis
\rightarrow
Repair
\rightarrow
Identity/Extension/Obligation.
$$

---

# 77. 與 ACR Governance 的關係

一般 ACR 已要求：

$$
Can
\neq
Should
\neq
Authorized.
$$

本文映射為：

$$
CanGenerate
\neq
MayAdopt
\neq
MayClaim.
$$

且：

$$
Candidate
\neq
Decision
\neq
Commit.
$$

在數學域變成：

$$
MathematicalCandidate
\neq
AcceptedTheoryMutation
\neq
PublishedClaim.
$$

---

# 78. 與 CTCL-ITR 的關係

CTCL-ITR 的價值在於：

> 問題身份與 theory status 不只要知道「現在是什麼」，還要能回答「當時何時、基於什麼知識與哪一版規則變成這樣」。

因此每個：

$$
ProblemMutation,
TheoryExtension,
ObligationChange,
ClaimPromotion
$$

都應有 temporal-causal event。

---

# 79. 可否證性

本文框架可能失敗於：

1. problem relation taxonomy 太粗或太複雜；
2. semantic equivalence 在研究級問題上難以可靠判定；
3. conservativity check 成本過高；
4. obligation explosion 使 research loop 無法運作；
5. theory graph bridge 高度依賴人工；
6. assumption envelope 在複雜 proof dependency 下過度膨脹；
7. governance 過強導致創造性下降。

因此本文不假設：

$$
MoreGovernance
\Rightarrow
BetterMathematics.
$$

而要測：

$$
ValidityGain
-
ResearchCost.
$$

---

# 80. 核心不變量

本文固定以下不變量：

$$
\boxed{
GenealogicalContinuity
\not\Rightarrow
SemanticEquivalence.
}
$$

$$
\boxed{
ProblemMutation
\neq
TextEdit.
}
$$

$$
\boxed{
Proof(RestrictedProblem)
\not\Rightarrow
Proof(OriginalProblem).
}
$$

$$
\boxed{
T+A\vdash Q
\not\Rightarrow
T\vdash Q.
}
$$

$$
\boxed{
DefinitionalExtension
\Rightarrow
ConservativeExtension
}
$$

在相應標準條件下，但：

$$
\boxed{
ConservativeExtension
\not\Rightarrow
DefinitionalExtension.
}
$$

$$
\boxed{
WAIVED
\neq
DISCHARGED.
}
$$

$$
\boxed{
DeferredObligation
\neq
ResolvedObligation.
}
$$

$$
\boxed{
ClaimScope
\not>
VerifiedScope.
}
$$

$$
\boxed{
DownstreamSuccess
\not\Rightarrow
UpstreamObligationsDisappear.
}
$$

---

# 81. 最終形式

一個合法的數學 mutation pipeline：

$$
\boxed{
\begin{aligned}
Gap_t
&\rightarrow MutationCandidate_t\\
&\rightarrow ProblemRelation_t\\
&\rightarrow TheoryExtensionClass_t\\
&\rightarrow ObligationSet_t\\
&\rightarrow GovernanceDecision_t\\
&\rightarrow CandidateTheoryState_{t+1}\\
&\rightarrow Verification_t\\
&\rightarrow ObligationDischarge_t\\
&\rightarrow AcceptedTheoryState_{t+1}\\
&\rightarrow ClaimScopeCheck_t\\
&\rightarrow Receipt/Ledger_t.
\end{aligned}
}
$$

若任一必要 obligation 未解除，系統可以：

$$
DEFER,
ESCALATE,
REJECT,
$$

或者保留：

$$
ConditionalResult.
$$

---

# 82. 核心命題

本文最核心的原則是：

$$
\boxed{
\textbf{
AI may change mathematics, but every change must change the accounting state of the mathematics as well.
}
}
$$

中文：

> **AI 可以改定義、補假設、分支問題、建立新方法甚至擴張理論；但每一次數學變更，都必須同步改變它的問題身份紀錄、理論擴張狀態、前提依賴與待解除義務。**

因此真正合法的自主數學生成不是：

$$
Generate
\rightarrow
Claim.
$$

而是：

$$
\boxed{
Generate
\rightarrow
Relate
\rightarrow
ClassifyExtension
\rightarrow
GenerateObligations
\rightarrow
Verify
\rightarrow
Disclose
\rightarrow
Claim.
}
$$

---

# 83. 結論

若 AI 永遠不能改問題、不能建定義、不能提出新方法、不能擴張理論，它就難以成為真正的自主數學研究系統。

但若 AI 可以任意修改，卻沒有 problem lineage、semantic relation、theory extension classification、assumption envelope 與 obligation accounting，那麼它也很容易透過「改到可解」製造虛假的研究成功。

因此本文提出的真正中間道路是：

$$
\boxed{
CreativeMathematicalAutonomy
+
ExplicitTheoryChange
+
MathematicalAccountability.
}
$$

它允許：

$$
DefinitionGeneration,
ProblemReformulation,
MethodGeneration,
TheoryExtension,
NewAxiomCandidate,
$$

但同時要求：

$$
ProblemIdentity,
ExtensionDisclosure,
AssumptionEnvelope,
ObligationTracking,
Verification,
Provenance.
$$

這使 AI 的數學創造力不需要被壓縮成只能在固定 theorem statement 上做 proof search；同時也不允許創造力繞過數學共同體最基本的可檢驗性。

下一篇將把前三篇的理論物件真正壓成 **Autonomous Mathematical Research Runtime (AMRR)** 的 executable architecture：canonical schemas、math registry、diagnosis router、problem/theory stores、obligation engine、verifier ensemble、CTCL events、research contracts 與 persistent loop。

---

# 參考文獻

[1] Xue, T. (2014). *Definitional Extension in Type Theory*. 19th International Conference on Types for Proofs and Programs (TYPES 2013), LIPIcs 26, 251–269. DOI: 10.4230/LIPIcs.TYPES.2013.251.

[2] Andréka, H., Gyenis, Z., Németi, I., & Sayed Ahmed, T. (2022). *Extensions in graph normal form*. Logic Journal of the IGPL, 30(1), 101–133. 本文使用其對 definitional extension、model extension 與 conservative extension 關係的標準邏輯背景。

[3] Rabe, F., & Kohlhase, M. (2013). *A Scalable Module System*. Information and Computation, 230, 1–54. DOI: 10.1016/j.ic.2013.06.001.

[4] Müller, D. (2019). *Mathematical Knowledge Management Across Formal Libraries*. Doctoral dissertation. 關於 MMT、theory graphs、theory morphisms 與跨形式庫 knowledge management。

[5] Poiroux, A., Weiss, G., Kunčak, V., & Bosselut, A. (2025). *Reliable Evaluation and Benchmarks for Statement Autoformalization*. Proceedings of EMNLP 2025, 17947–17969. DOI: 10.18653/v1/2025.emnlp-main.907.

[6] Min, M. J., He, M., Li, Z., Yi, Z., Malik, S., Gupta, A., Si, X., & Bastani, O. (2026). *Theory-Level Autoformalization: From Isolated Statements to Unified Formal Knowledge Bases*. arXiv:2607.13292. ICML 2026 Position Track, Spotlight.

[7] Feng, T., Trinh, T. H., Bingham, G., et al. (2026). *Towards Autonomous Mathematics Research*. arXiv:2602.10177.

[8] Zhang, L., Valentino, M., & Freitas, A. (2025). *Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions*. Proceedings of EMNLP 2025, 1720–1738. DOI: 10.18653/v1/2025.emnlp-main.90.

---

# 內部架構依賴文件

[I1] Neo.K. (2026). *從數學解題到自主數學研究：受約束數學域補全與自主數學研究 Runtime*，Autonomous Mathematical Research / Paper 01 of 04，v0.1.

[I2] Neo.K. (2026). *數學問題不是只有可解與不可解：多域問題診斷與受約束數學域補全*，Autonomous Mathematical Research / Paper 02 of 04，v0.1.

[I3] Neo.K. (2026). *從自提示到自主認知閉環：持續目標型 AI 的基礎理論*，系列 01/06，v0.1.

[I4] Neo.K. (2026). *可定址認知空間：Cognitive Affordance、Semantic Address 與認知算子*，系列 02/06，v0.1.

[I5] Neo.K. (2026). *自我對話不是文字：AI-Native Cognitive Program 與 Zero-Rendering Runtime*，系列 03/06，v0.1.

[I6] Neo.K. (2026). *時間因果自我史：CTCL-ITR、Decision Receipt 與上下文壓縮後的可追溯性*，系列 04/06，v0.1.

[I7] Neo.K. (2026). *契約邊界內的 AI 自主性：Execute、Refuse、Defer、Idle 與 Escalate*，系列 05/06，v0.1.

[I8] Neo.K. (2026). *Addressable Cognitive Runtime × CTCL：統一技術白皮書與實作路線圖 v0.1*，系列 06/06.

---

# 版本備註

**v0.1 / 2026-08-23**

本版正式固定：

1. Genealogical Identity / Semantic Relation 雙層問題身份；
2. ProblemRelation vocabulary；
3. Problem Mutation / Problem Branch；
4. Theory Extension Ladder 與多維 Extension Profile；
5. definitional / conservative / non-conservative extension 的邊界；
6. Mathematical Obligation System；
7. Obligation Dependency / Inheritance；
8. Assumption Envelope；
9. No Mathematical Laundering Principle；
10. Claim Scope Invariant；
11. Theory Graph / Theory Morphism bridge；
12. Problem Mutation / Theory Extension / Verification / Obligation Receipts；
13. risk-tiered obligation governance；
14. Paper 04 Runtime 所需最小接口與 schemas；
15. Silent Mutation、No-Laundering、Theory Drift 等 falsification gates。

本版不宣稱 conservativity、independence、consistency 或 semantic equivalence 對任意研究級理論皆可自動判定；本文的主張是系統必須辨認這些義務、標記其狀態並防止未解除義務被後續成果洗白。
