# 問句的 Normal Form
## T Query Compiler、重寫系統、型別規則與可問等價

**英文題名：** *Normal Forms of Questions: A T Query Compiler, Rewrite Systems, Typing Rules, and Query Equivalence*  
**系列：**《T 的最小完備可問：從問算子到高階語義空間》Paper 03  
**版本：** v0.1 候選理論草稿  
**日期：** 2026-08-13  
**作者：** Neo.K、Aletheia（AI 協作）  
**機構：** EveMissLab／一言諾科技有限公司

---

## 摘要

Paper 01 將 T-問題壓縮成六個候選基本問算子：

\[
\mathcal Q_0
=
\{
\mathbf B,\mathbf D,\mathbf G,\mathbf F,\mathbf C,\mathbf O
\}
\]

與語義提升算子 \(X_{\mathcal S}\)；Paper 02 進一步指出：

\[
X_iX_jT
\not\equiv_Q
X_jX_iT
\]

在一般情況下完全可能成立，因此 operator order 本身可能是 query semantics 的一部分。

一旦接受非交換性，新的工程／形式問題就不可避免：

> **兩句自然語言問題何時其實是在問同一件事？哪些 rewrite 可以安全地做？什麼叫做一個問句的 Normal Form？**

本文提出 T Query Compiler 的第一版架構：

\[
\boxed{
NaturalLanguage
\rightarrow
ParseForest
\rightarrow
TypedAST
\rightarrow
ScopedAST
\rightarrow
SemanticIR
\rightarrow
NF_R(q)
}
\]

其中 Normal Form 不是「把字串排整齊」，而是相對於 type system、scope、semantic model、task、rewrite system \(R\) 與 operator versions 所定義的 canonical query representation。

本文區分兩層 normalization：

### Surface Canonicalization

只處理 alias、operator canonical ID、parameter ordering、explicit version、whitespace / syntax 與 equivalent surface labels。

### Semantic Normalization

才可能處理 identity-lift elimination、certified idempotence、certified absorption、certified commutation、task-lossless projection 與 macro expansion / contraction。

第二層必須保存 query equivalence：

\[
\boxed{
q\rightarrow_R q'
\quad\Rightarrow\quad
q\equiv_Q q'.
}
\]

本文同時拒絕把「存在某條 reduction path 到 normal form」與「normal form 唯一」混為一談。若要讓：

\[
NF_R(q)
\]

成為可靠 canonical representation，至少需要研究：

1. **Termination**：不存在無限 rewrite chain；
2. **Confluence**：不同 rewrite path 可以重新匯合；
3. **Type Preservation**；
4. **Scope Preservation**；
5. **Semantic Preservation**；
6. **Version Stability / Explicit Versioning**。

因此本文只將 \(NF_R\) 視為相對於已驗證 rewrite subset 的安全 normalizer；尚未證明整個 T-query rewrite system globally terminating / confluent。

本文進一步定義 Query AST、Query IR、Rewrite Certificate、Critical Pair、Unsafe Rewrite、Task-Lossless Equivalence、Query Fingerprint 與 Query Provenance。並附一個最小 Python reference normalizer：它能安全刪除 identity lift、合併有證書的 idempotent duplicate、保留非交換的 Time/Name 次序，並只在明確 commutation certificate 存在時重排。

本文最終提出：

\[
\boxed{
\text{Canonical form is earned by proved rewrites, not imposed by formatting.}
}
\]

---

## 關鍵詞

Normal Form、Query Compiler、Typed AST、term rewriting、confluence、termination、query equivalence、safe rewrite、semantic normalization、\(X^nT\)、operator order

---

# 0. 研究邊界

本文不主張：

1. 已證明所有 T-query 都存在唯一 normal form；
2. 已建立 complete parser for natural language；
3. 所有 query equivalence 都可 decidably 判定；
4. term-rewriting theory 可直接無修改套用自然語言語義；
5. confluence 自動推出 semantic correctness；
6. 字串相等就是 query equivalence；
7. query equivalence 一定要求完全相同 wording；
8. 所有 operators 都可以 canonical sort；
9. 所有 macro contraction 都是 lossless；
10. 本文已證明 T Query Compiler 的 soundness / completeness。

本文研究的是：

> **在 operator order 可能有語義的前提下，如何建立一個不會因 normalization 自己改變問題的 query compiler。**

---

# 1. 為什麼需要 Normal Form？

自然語言可以用不同方式問同一件事：

> 改名之後，為什麼它還是原來那個 T？

> T 的名稱變化後，哪些 grounds 支持 identity continuity？

> 在 naming history 改變的時間條件下，什麼使 T 保持同一身份？

這些 surface 不同，但可能都編譯成近似：

\[
\boxed{
\mathbf G(
X_{\mathrm{Time}}
X_{\mathrm{Name}}
T;
\alpha=HistoricalIdentity
).
}
\]

若沒有 canonical representation，benchmark 會重複、retrieval 會碎裂、rule 無法重用，也無法可靠比較兩個問題。

---

# 2. 但 Normalization 本身可能毀掉問題

Paper 02 已給出：

\[
X_{\mathrm{Time}}
X_{\mathrm{Name}}T
\not\equiv_Q
X_{\mathrm{Name}}
X_{\mathrm{Time}}T.
\]

因此：

\[
\boxed{
\text{Canonicalization}
\neq
\text{Arbitrary Sorting}.
}
\]

---

# 3. Compiler Pipeline

\[
\boxed{
NL
\rightarrow
PF
\rightarrow
AST_T
\rightarrow
AST_S
\rightarrow
IR_Q
\rightarrow
NF_R.
}
\]

其中：

- \(NL\)：Natural language input；
- \(PF\)：Parse forest；
- \(AST_T\)：Typed AST；
- \(AST_S\)：Scoped AST；
- \(IR_Q\)：Semantic Query IR；
- \(NF_R\)：relative normal form。

---

# 4. Parse Forest 而不是過早單一路徑

自然語言可能有 attachment ambiguity，因此：

\[
\boxed{
Parser\rightarrow\{AST_1,\ldots,AST_k\}.
}
\]

若 downstream evidence / task 才能 disambiguate，保留：

\[
UnderdeterminedParse.
\]

---

# 5. 基本語法

Object-level term：

\[
\boxed{
t::=T\mid X_{\mathcal S}^{O}[v,\theta](t).
}
\]

Query：

\[
\boxed{
q::=\mathbf Q[\theta](t)\mid X_{\mathcal S}^{Q}[v,\theta](q).
}
\]

其中 \(X^O\) 作用於 object，\(X^Q\) 作用於 query。

---

# 6. Generator Typing

第一版：

\[
\mathbf B:Obj\rightarrow Query,
\quad
\mathbf D:Obj\times Obj\rightarrow Query,
\]

\[
\mathbf G,\mathbf F,\mathbf C:Obj\rightarrow Query,
\]

\[
\mathbf O:Obj\times Obj?\rightarrow Query.
\]

---

# 7. Query Lift 與 Object Lift

\[
X_{\mathrm{Observer}}^Q(\mathbf B(T))
\]

問的是：

> observer 如何理解「T 是不是 T」這個問題？

而：

\[
\mathbf B(X_{\mathrm{Observer}}^O(T))
\]

問的是：

> observer-view 下的 T 是否為 T？

因此：

\[
\boxed{
X^Q\neq X^O.
}
\]

---

# 8. Typed AST

例：

```text
Query(
  generator = G,
  target =
    LiftO(Time,
      LiftO(Name,
        Seed(T)
      )
    ),
  args = {identity_relation: HistoricalIdentity}
)
```

這是：

\[
\mathbf G(
X_{\mathrm{Time}}
X_{\mathrm{Name}}T
).
\]

---

# 9. Scope 是 AST 的一部分

```text
LiftO(Time, LiftO(Name,T))
```

與：

```text
LiftO(Name, LiftO(Time,T))
```

不是同一 tree。

因此：

\[
\boxed{
Scope\subset QuerySemantics.
}
\]

---

# 10. Query IR

本文定義最小：

\[
\boxed{
IR_Q
=
(
Generator,
OrderedLifts,
Types,
Scopes,
Parameters,
Versions,
Task,
Model,
EvidenceRequirements
).
}
\]

OrderedLifts 不能降成 set。

---

# 11. Surface Canonicalization

第一層：

\[
\boxed{
SC(q)
}
\]

只做：

- terminology alias；
- canonical operator ID；
- explicit version；
- parameter key ordering；
- Unicode / syntax normalization。

它不能交換 operators。

---

# 12. Semantic Normalization

第二層：

\[
\boxed{
SN_R(q)
}
\]

只有在存在：

\[
r\in R
\]

且 side conditions 成立時才應用。

---

# 13. Rewrite Rule

一般形式：

\[
\boxed{
r:l\rightarrow r'
\quad[\Phi].
}
\]

\(\Phi\) 包含 domain、task、operator version、semantic preconditions 等。

---

# 14. Rewrite Certificate

定義：

\[
\boxed{
RC
=
(
RuleID,
LHS,
RHS,
Conditions,
Domain,
Task,
OperatorVersions,
Evidence,
Status
).
}
\]

Production semantic rewrite 必須：

\[
Status=Validated.
\]

---

# 15. Definitional Rewrite：Identity Elimination

\[
\boxed{
X_{\varnothing}(t)\rightarrow t.
}
\]

這是由 \(X_{\varnothing}\) 的定義直接授權。

---

# 16. Certified Idempotence

若已證：

\[
X_iX_it\equiv_QX_it
\]

在 domain \(D\)，才可：

\[
\boxed{
X_i(X_i(t))\rightarrow X_i(t).
}
\]

Duplicate lift 不得預設可刪。

---

# 17. Certified Commutation

只有存在：

\[
CC_{ij}
\]

證明：

\[
X_iX_jt\equiv_QX_jX_it
\]

在條件 \(\Phi\) 下，才可重排。

---

# 18. Canonical Ordering 只能在 Commutation Class 內做

若 \(\mathcal C\subseteq\Sigma_X\) 已在 domain \(D\) 證明兩兩 commute，才可在 \(\mathcal C\) 內排序。

因此：

\[
\boxed{
\text{canonical order is local, not universal}.
}
\]

---

# 19. Certified Absorption

若：

\[
X_jX_it\equiv_QX_jt
\]

在 \(\Phi\) 下，可：

\[
\boxed{
X_j(X_i(t))\rightarrow X_j(t).
}
\]

但 containment intuition 本身不足以證明 absorption。

---

# 20. Semantic Preservation

production rewrite 必須：

\[
\boxed{
q\rightarrow_Rq'
\Rightarrow
q\equiv_Qq'.
}
\]

這是核心安全條件。

---

# 21. Type Preservation

要求：

\[
\boxed{
Type(q)=Type(q')
}
\]

或存在明確 coercion。

---

# 22. Scope Preservation

lossless rewrite 應有：

\[
\boxed{
Scope(q)\cong Scope(q').
}
\]

---

# 23. Task-Lossless Rewrite

某些 rewrite 不 globally equivalent，但對 task \(\mathcal T\)：

\[
\boxed{
q\equiv_Q^{\mathcal T}q'.
}
\]

這種 rule 必須 task-scoped。

---

# 24. Query Equivalence 的層級

至少分：

1. AST identity；
2. definitional equivalence；
3. answer-space / resolution equivalence；
4. task equivalence；
5. pragmatic equivalence。

Compiler core 應優先使用更強、可審計的等價層。

---

# 25. Normal Form

若：

\[
q\not\rightarrow_R,
\]

稱 \(q\) 為 \(R\)-normal。

但：

\[
\boxed{
Normal\not\Rightarrow Canonical.
}
\]

---

# 26. Termination

若不存在無限：

\[
q_0\rightarrow_Rq_1\rightarrow_Rq_2\rightarrow_R\cdots
\]

則 \(R\) terminating。

---

# 27. Confluence

若：

\[
q\rightarrow_R^*q_1
\]

與：

\[
q\rightarrow_R^*q_2
\]

總能匯合到共同：

\[
q_3,
\]

則 \(R\) confluent。

---

# 28. 為什麼 Confluence 對 Query Compiler 關鍵？

如果 rewrite order 不同導致不同 irreducible forms，canonical representation 就依賴 optimizer 執行路徑。

因此：

\[
\boxed{
\text{rewrite-path dependence}
}
\]

本身就是 compiler 的錯誤來源。

---

# 29. Construction Curvature 與 Rewrite Curvature 要分開

Paper 02 的 semantic curvature 是：

> query construction path 改變問題。

Paper 03 的 normalization path dependence 是：

> 同一問題被不同 rewrite path 化簡後得到不同 representation。

兩者不是同一層。

---

# 30. Critical Pair

若兩條 rules 可對同一 term 的重疊位置作用：

\[
q\rightarrow q_1,
\qquad
q\rightarrow q_2,
\]

則形成 candidate critical pair。

需要檢查：

\[
q_1\downarrow q_2.
\]

---

# 31. 問算子 Critical Pair

假設：

\[
X_iX_i\rightarrow X_i
\]

以及：

\[
X_iX_j\rightarrow X_jX_i.
\]

在：

\[
X_iX_iX_jT
\]

上可能有不同 rewrite 先後。

如果 side conditions 不一致，會產生不同 normal forms。

---

# 32. Operator Versioning

\[
X_i^{v1}
\]

與：

\[
X_i^{v2}
\]

可能 semantics 不同。

所以：

\[
\boxed{
OperatorVersion
}
\]

必須留在 IR 與 NF。

---

# 33. Version Collapse Bug

如果：

\[
X_i^{v1}\not\equiv_QX_i^{v2}
\]

卻都 normalize 成裸：

\[
X_i,
\]

就是：

\[
\boxed{
VersionCollapseBug.
}
\]

---

# 34. Parameter Canonicalization

parameter map 的 key order 可 canonicalize。

這與 operator order 完全不同。

因此：

\[
\boxed{
ParameterOrdering\neq OperatorOrdering.
}
\]

---

# 35. Alias Canonicalization

若 vocabulary registry 明確宣告：

\[
Temporal\equiv_{def}Time,
\]

則可：

\[
X_{\mathrm{Temporal}}\rightarrow X_{\mathrm{Time}}.
\]

Alias registry 本身也需 versioning。

---

# 36. Query Provenance

定義：

\[
\boxed{
QP(q)
}
\]

保存：

- original text；
- parser version；
- selected parse；
- rewrite sequence；
- certificates；
- final NF。

---

# 37. Rewrite Trace

\[
q_0
\xrightarrow{r_1}
q_1
\rightarrow\cdots\rightarrow
q_n=NF(q).
\]

每一步可重播。

---

# 38. Query Normalization Certificate

\[
\boxed{
QNC
=
(
Input,
TypedAST,
RewriteTrace,
Certificates,
NF,
CompilerVersion,
Status
).
}
\]

---

# 39. Query Fingerprint

\[
\boxed{
FP_Q
=
Hash(
Serialize(NF(q)),
ModelVersion,
Task,
RewriteSetVersion
).
}
\]

fingerprint 是工程 identity，不是 query-equivalence proof。

---

# 40. Same Fingerprint / Different Fingerprint 的限制

Same fingerprint 支持 serialized NF 相同。

Different fingerprint 不推出不同問題，因 normalizer 可能 incomplete。

因此：

\[
\boxed{
FingerprintIdentity
\neq
QuerySemanticIdentity.
}
\]

---

# 41. Unsafe Rewrite：Operator Sorting

沒有 certificate 時禁止：

\[
Time(Name(T))
\rightarrow
Name(Time(T)).
\]

---

# 42. Unsafe Rewrite：Scope Flattening

禁止：

\[
X_i(X_j(T))
\rightarrow
\{X_i,X_j\}(T).
\]

---

# 43. Unsafe Rewrite：Version Erasure

禁止無條件：

\[
X_i^{v1}\rightarrow X_i.
\]

---

# 44. Unsafe Rewrite：Unknown-to-False

\[
Unknown\rightarrow False
\]

會把 epistemic uncertainty 誤寫成 semantic negation。

---

# 45. Unsafe Rewrite：Macro Overcontraction

若：

\[
X_AX_B
\]

只在特定 context 等價 \(X_C\)，不能全域：

\[
X_AX_B\rightarrow X_C.
\]

---

# 46. Unsafe Rewrite：Task Leakage

task-lossless rule 不能跨 task 無條件重用。

---

# 47. Natural-Language Equivalent Candidate

句 A：

> T 改名後為什麼還是原來那個？

句 B：

> 名稱變更後，什麼 grounds 支持 T 的 historical identity？

在同一 parse / task 下可候選編譯為：

\[
\mathbf G(
X_{\mathrm{Time}}
X_{\mathrm{Name}}T;
\alpha=Historical
).
\]

---

# 48. Natural-Language Near-Miss

句 A：

> 現在叫 T 的東西未來是誰？

句 B：

> 未來叫 T 的東西是誰？

Paper 02 的 witness 顯示它們可能不同，因此 compiler 必須保留兩個不同 AST。

---

# 49. Conservative Normalizer

初版 production 建議只開：

1. identity elimination；
2. definitional alias；
3. explicit version resolution；
4. proven idempotence；
5. proven commutation；
6. proven absorption。

未知情況保持原 AST。

---

# 50. Incomplete 比 Unsound 安全

若：

\[
q_1\equiv_Qq_2
\]

但 compiler 沒合併，只是 redundancy。

若：

\[
q_1\not\equiv_Qq_2
\]

卻被合併，問題直接被改掉。

因此 identity-sensitive query compiler 初期應：

\[
\boxed{
\text{prioritize avoiding false merges}.
}
\]

---

# 51. Query False Merge

\[
q_1\not\equiv_Qq_2
\]

但：

\[
NF(q_1)=NF(q_2).
\]

---

# 52. Query False Split

\[
q_1\equiv_Qq_2
\]

但：

\[
NF(q_1)\neq NF(q_2).
\]

---

# 53. Query Equivalence Benchmark

建立：

\[
\boxed{
\mathcal B_Q
=
\{
(q_i,q_j,label,evidence)
\}.
}
\]

label：

\[
\{
Equivalent,
TaskEquivalent,
Different,
Underdetermined
\}.
\]

---

# 54. Rewrite Validation Benchmark

每條 rule 至少需要：

- positive；
- boundary；
- negative witness；
- version mismatch；
- task mismatch。

---

# 55. Mutation Suite

故意建立：

- unconditional Time/Name sort；
- unconditional duplicate deletion；
- version erasure；
- unknown→false；

確認 validator 能抓到。

---

# 56. Normalization Levels

### N0 — Parse Preservation  
只保存 AST。

### N1 — Surface Canonicalization  
alias / syntax / version。

### N2 — Definitional Normalization  
identity / macro definitions。

### N3 — Certified Algebraic Rewrite  
commutation / idempotence / absorption。

### N4 — Task-Lossless Compression  
只對指定 task。

---

# 57. Query Normal Form Status

\[
Status_{NF}
\in
\{
Parsed,
Typed,
SurfaceCanonical,
DefinitionallyNormal,
CertifiedNormal,
TaskNormal,
Underdetermined
\}.
\]

---

# 58. Unique NF 的條件

若 rewrite subset \(R_s\) 已：

- terminating；
- confluent；
- type-preserving；
- semantics-preserving；

則可在該 subset 稱：

\[
\boxed{
\text{unique canonical normal form}.
}
\]

---

# 59. 目前只主張 Safe Local Normal Forms

對完整：

\[
R_T
\]

我們尚未證：

\[
Termination(R_T)
\]

或：

\[
Confluence(R_T).
\]

因此：

\[
\boxed{
\text{global canonicality remains open}.
}
\]

---

# 60. Term Rewriting 的外部接口

term rewriting 長期研究 normal forms、confluence、Church–Rosser、completion 與 critical pairs。Knuth–Bendix 類 completion 的目標之一就是在適用情況下把 equational specification 轉成更可用的 confluent rewriting presentation。

本文借用的是：

\[
\boxed{
\text{rewrite discipline}.
}
\]

不是把自然語言問句直接宣稱為普通 TRS。

---

# 61. Inquisitive Logic 的外部接口

inquisitive / dependence logics 已經存在正式 normal-form 與 completeness results。這證明「含 question-like operators 的正式語言可以建立嚴格 normal-form theorem」不是概念上不可能。

本文不同的是 operator-composed T identity queries。

---

# 62. Inferential Erotetic Logic 的外部接口

IEL 正式研究 question evocation、question generation、erotetic implication。

本文新增：

\[
\boxed{
NaturalLanguage
\rightarrow
TypedOperatorAST
\rightarrow
CertifiedRewriteNF.
}
\]

---

# 63. Dynamic Epistemic Logic 的外部接口

DEL 類框架把 epistemic actions 當成 model-transforming operators。

這提醒 compiler：

> action-like semantic lifts 一旦被 reorder，後一算子可能已經面對不同 model state。

因此 Paper 02 的非交換性限制必須成為 Paper 03 normalizer 的硬規則。

---

# 64. Reference Normalizer v0.1

本 ZIP 附帶 toy normalizer。

它直接接受 typed AST，不做 full NLP。

實作：

1. \(X_\varnothing(t)\to t\)；
2. 未證 idempotence 不刪 duplicate；
3. 有 certificate 才做 idempotence；
4. 未證 commutation 不重排；
5. 有 certificate 才 canonicalize commuting pair；
6. operator version 永遠保留。

---

# 65. 驗證目標

reference normalizer 應通過：

- Identity elimination；
- Uncertified idempotence blocked；
- Certified idempotence；
- Uncertified Time/Name reorder blocked；
- Noncommuting orders stay distinct；
- Certified commutation canonicalizes；
- Operator versions preserved。

---

# 66. Query IR Schema

本文附：

\[
\boxed{
QueryIR
}
\]

與：

\[
\boxed{
RewriteCertificate
}
\]

machine-readable schema，供後續 Paper 04 benchmark 使用。

---

# 67. Research Corpus 應用

如果大量論文的 research questions 都被編成：

\[
NF(q),
\]

可做：

- query deduplication；
- theory genealogy；
- benchmark coverage；
- cross-paper question retrieval；
- unresolved-question tracking。

---

# 68. Question-Native Research Index

因此理論庫未來可以不只按 title / keyword / claim 索引，

還按：

\[
\boxed{
NF(q)
}
\]

索引。

這稱為：

**Question-Native Research Index**。

---

# 69. Query Dependency Graph

若：

\[
q_2
\]

需要先解：

\[
q_1,
\]

可建：

\[
q_1\rightarrow q_2.
\]

這與 IEL 的 question-generation / implication 外部研究接口自然銜接。

---

# 70. Paper 04 的前置條件

要測六生成元的 completeness / minimality，必須先知道 benchmark 中哪些 query 真的是不同問題。

否則：

- surface duplicate 會灌高 query count；
- aggressive merge 會灌高 coverage。

所以：

\[
\boxed{
\text{Minimality testing requires query equivalence infrastructure}.
}
\]

---

# 71. Conjecture 1 — Safe Normalization Subsystem

存在非平凡：

\[
R_s
\]

同時具有：

\[
\boxed{
Termination+
Confluence+
TypePreservation+
SemanticPreservation.
}
\]

---

# 72. Conjecture 2 — Useful Canonicalization

存在非平凡自然語言 T-query 子集，可以穩定編譯到：

\[
NF_{R_s}(q)
\]

並把 false-merge 控制在嚴格低水平。

---

# 73. Conjecture 3 — Ordered Core

任何 sound normalizer 若處理完整 T-query domain，都必須保留一個不能自由排序的 ordered operator core。

---

# 74. Conjecture 4 — Layered Query Equivalence

「同一個問題」不是單一 equivalence 尺度；至少需分 definitional、semantic、task、pragmatic levels。

---

# 75. 核心命題一

\[
\boxed{
NormalForm\neq PrettyFormatting.
}
\]

---

# 76. 核心命題二

production semantic rewrite 必須滿足：

\[
\boxed{
q\rightarrow_Rq'
\Rightarrow
q\equiv_Qq'.
}
\]

---

# 77. 核心命題三

\[
\boxed{
Normal\not\Rightarrow UniqueNormal.
}
\]

---

# 78. 核心命題四

非交換 operators 不能參與未證明 canonical sorting。

---

# 79. 核心命題五

\[
\boxed{
\text{conservative but incomplete}
}
\]

優於：

\[
\boxed{
\text{aggressive but unsound}.
}
\]

---

# 80. 核心命題六

在 identity-sensitive query compilation 中，False Merge 通常比 False Split 更危險。

---

# 81. T Query Compiler 核心算子

\[
\boxed{
\mathfrak C_Q:
(
NL,
Task,
Context,
Model
)
\longrightarrow
(
ParseForest,
TypedAST,
IR,
NF,
QNC
).
}
\]

---

# 82. Normalization 核心算子

\[
\boxed{
\mathfrak N_R:
IR
\longrightarrow
(
NF_R,
RewriteTrace,
Certificates
).
}
\]

---

# 83. Query Equivalence Resolver

\[
\boxed{
\mathfrak E_Q:
(
q_1,q_2,Model,Task
)
\longrightarrow
\{
Equivalent,
TaskEquivalent,
Different,
Underdetermined
\}.
}
\]

---

# 84. 最終編譯鏈

\[
\boxed{
NaturalQuestion
\rightarrow
TypedOrderedAST
\rightarrow
SemanticIR
\rightarrow
CertifiedRewrites
\rightarrow
QueryNormalForm.
}
\]

---

# 85. 結論

Paper 01 告訴我們：

\[
T
\]

可以透過少數問算子與 \(X\)-lifts 生成大量問題。

Paper 02 告訴我們：

\[
X_iX_jT
\]

與：

\[
X_jX_iT
\]

可能不是同一個問題。

Paper 03 因此得到最重要的 compiler 原則：

\[
\boxed{
\text{不要為了得到 Normal Form，
先把真正的問題改掉。}
}
\]

安全 normalization 的順序必須是：

\[
\boxed{
Parse
\rightarrow
Type
\rightarrow
Scope
\rightarrow
Version
\rightarrow
Equivalence
\rightarrow
Certificate
\rightarrow
Rewrite.
}
\]

而不是：

\[
\boxed{
\text{先排序、先合併、先壓縮，再問是不是等價。}
}
\]

真正的 Query Normal Form 不是 formatter 的偏好。

它是：

\[
\boxed{
\text{a canonical representative justified by a semantics-preserving rewrite history}.
}
\]

下一篇 Paper 04〈T 的最小完備性猜想：Coverage、Independence 與反例搜尋〉就可以正式開始測試：

\[
\boxed{
\mathcal Q_{\min}^{?}
=
\{
\mathbf B,\mathbf D,\mathbf G,\mathbf F,\mathbf C,\mathbf O
\}
}
\]

到底是不是相對最小完備基底。

因為現在我們終於有能力先問：

> **兩個 benchmark query 到底是真的不同，還是只是不同寫法？**
