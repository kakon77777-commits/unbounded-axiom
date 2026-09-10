---
title: "GACEI-09｜對抗性創造與生成：AI 如何發明從未見過的 Attack Family"
title_en: "GACEI-09 | Adversarial Creativity and Generation: How AI Can Propose Previously Unseen Attack Families"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-09"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / AI 創造能力 / 對抗生成 / Attack Family Synthesis"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "GACEI-02 MSSP 的對偶 v0.1"
  - "GACEI-03 局部攻擊抽象論 v0.1"
  - "GACEI-04 對抗記憶基底 v0.1"
  - "GACEI-05 全域攻擊組合代數 v0.1"
  - "GACEI-06 全域攻擊壓縮 v0.1"
  - "GACEI-07 一眼理解專案 v0.1"
  - "GACEI-08 工程理解不是摘要 v0.1"
  - "DEST-08 概念積分 2.0"
---

# GACEI-09｜對抗性創造與生成
## AI 如何發明從未見過的 Attack Family

**英文題名：** Adversarial Creativity and Generation: How AI Can Propose Previously Unseen Attack Families

---

## 摘要

GACEI-01 至 GACEI-08 已建立從全域注意力、工程理解、局部 attack 抽象、SEDB-style 對抗記憶、attack composition 到 global campaign compression 的前置鏈。但如果 AI 只能從記憶中重播已知 attack，整套系統仍只是高品質的「已知失敗再利用器」，而不是能對陌生架構提出新 failure hypothesis 的工程智能。

本文提出「對抗性創造與生成」（Adversarial Creativity and Generation, ACG）框架，研究 AI 如何根據：

$$
\boxed{
\text{Project Model}
+
\text{Attack Memory}
+
\text{Residual Gaps}
+
\text{Constraints}
}
$$

提出新的 failure hypothesis，形成新的 attack candidate，再把抽象假說轉換成可在授權 sandbox 中執行、可觀測、可驗證、可恢復的 adversarial experiment。

本文首先區分：

$$
\boxed{
\text{Retrieval}
\neq
\text{Composition}
\neq
\text{Creativity}
\neq
\text{Executable Generation}.
}
$$

Retrieval 是找回既有 operator；Composition 是重新組合已知 operators；Creativity 是提出目前 attack corpus、已知組合與明示 grammar 尚未直接包含的新 failure mechanism hypothesis；Executable Generation 則要求把 hypothesis 轉換成真正可執行的測試實驗。

本文將 failure hypothesis 表示為：

$$
\boxed{
h
=
\left(
P,
I,
M,
Q,
E,
R
\right),
}
$$

其中：

- $P$：適用前提；
- $I$：目標 invariant / contract；
- $M$：假設的 failure mechanism；
- $Q$：生成理由；
- $E$：預期 evidence；
- $R$：risk / scope / authorization conditions。

接著定義：

$$
\boxed{
\mathsf{GenAttack}
:
(h,\widehat{\mathfrak P},\theta)
\rightarrow
a,
}
$$

其中 $a$ 必須符合既有 attack operator 語義：

$$
a
=
(P,T,I,O,V,R,C,K,H).
$$

因此：

$$
\boxed{
\text{Hypothesis}
\neq
\text{Attack}
\neq
\text{Finding}
\neq
\text{Reusable Knowledge}.
}
$$

本文特別修正「新 attack」的過強說法。更嚴謹的第一版 novelty 應寫成：

$$
\boxed{
a
\notin
Cl_A
(
K
\mid
\Gamma,
\Pi,
\mathcal O,
B,
t
)
}
$$

也就是：在目前 attack memory $K$ 、生成 grammar $\Gamma$ 、representation $\Pi$ 、operator set $\mathcal O$ 、resource bound $B$ 與時間 $t$ 下，該候選不在可辨識的既有 attack closure 中。本文稱此為：

$$
\boxed{
\text{Bounded Adversarial Novelty}.
}
$$

它只支持「相對於目前知識與生成條件的新穎」，不支持絕對歷史首創。

本文承接 DEST-08 的候選生成思想，把主要創造操作整理為：

$$
\boxed{
\mathfrak O_{ACG}
=
\{
Retrieve,
Compose,
Relate,
Bridge,
Abstract,
Specialize,
Macro,
Reframe,
Primitive,
Distill
\}.
}
$$

但在 GACEI 中，這些操作被約束到 failure-mechanism domain。尤其 `Bridge` 用於提出跨 component、state 或 lifecycle 的缺失 failure bridge；`Reframe` 用於改變 representation，以暴露原表示看不到的 failure；`Primitive` 只表示現有 attack grammar 無法忠實表達某 hypothesis，而不是宣稱本體論上不可還原的新存在。

本文進一步提出「創造不是亂猜」原則。令：

$$
\boxed{
G_R
=
(
G_V,
G_E,
G_X,
G_I,
G_P,
G_T,
G_Q,
G_H
)
}
$$

為 residual gap field，分別描述 component、relation、state、invariant、path、temporal、validator 與 history/version 的未知或薄弱區。AI 應把創造能力優先投入：

$$
\boxed{
\text{High Risk}
\cap
\text{High Uncertainty}
\cap
\text{Low Known Coverage}.
}
$$

本文提出 Attack Creativity Quality：

$$
\boxed{
Q_C(a)
=
\frac{
Novelty(a)
\cdot
Validity(a)
\cdot
MechanismValue(a)
\cdot
TransferPotential(a)
}{
ReasoningCost(a)+\epsilon
}.
}
$$

Executable Generation 則有另一組品質：

$$
\boxed{
Q_G(a)
=
f(
Executability,
Isolation,
Observability,
Validation,
Recoverability,
Reproducibility
).
}
$$

因此一個 AI 可以 $Q_C$ 高但 $Q_G$ 低：很會提出有趣失敗假說，卻不會把它轉成可測工程實驗；也可能相反，會寫大量測試程式，卻缺少真正新穎的 failure model。

本文最後提出 Attack Family Discovery Loop：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Model}
\rightarrow
\text{Residual}
\rightarrow
\text{Hypothesize}
\rightarrow
\text{Type}
\rightarrow
\text{Generate}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Localize}
\rightarrow
\text{Abstract}
\rightarrow
\text{Transfer}
\rightarrow
\text{Promote}.
}
$$

這使 AI 的創造能力從文本生成，提升成可驗證、可否證、可學習、可累積的工程智能。

**關鍵詞：** Adversarial Creativity、Attack Generation、Attack Family Discovery、Bounded Novelty、Residual Gap、Executable Generation、DEST-08、AI 工程智能、Global Adversarial Computation

---

# 0. 研究定位與安全範圍

本文只研究：

$$
\boxed{
\text{Authorized Adversarial Test Synthesis}.
}
$$

所有 generated attacks 僅作用於：

- synthetic system；
- authorized repository；
- sandbox；
- isolated clone；
- test fixture；
- 可恢復 runtime。

本文所稱 whole-system penetration 的工程語義是：

$$
\boxed{
\text{Whole-System Adversarial Simulation}.
}
$$

不是未授權第三方系統入侵。

---

# 1. Retrieval、Composition、Creativity、Generation

## 1.1 Retrieval

若：

$$
a\in K_A,
$$

則：

$$
\operatorname{Retrieve}(K_A,q)
\rightarrow
a.
$$

這是記憶能力。

## 1.2 Composition

若：

$$
a,b\in K_A,
$$

AI 提出：

$$
a\odot b
$$

或：

$$
a\circ b.
$$

這是組合能力。

## 1.3 Creativity

若：

$$
c
\notin
Cl_A(K_A\mid\Gamma,\Pi,\mathcal O,B,t),
$$

才開始具有 bounded novelty。

## 1.4 Executable Generation

如果：

$$
c
$$

仍只是自然語言 hypothesis，尚未成為：

$$
a_{\mathrm{exec}}.
$$

因此：

$$
\boxed{
\text{Creativity}
\neq
\text{Generation}.
}
$$

---

# 2. Failure Hypothesis

定義：

$$
\boxed{
h
=
(P,I,M,Q,E,R).
}
$$

 $P$ 問「何時有意義」； $I$ 問「測哪個 contract」； $M$ 問「為什麼可能失敗」； $Q$ 保存 hypothesis 生成理由； $E$ 描述預期 evidence； $R$ 保存 scope、risk、authorization 與 cleanup 條件。

---

# 3. Hypothesis、Attack、Finding、Knowledge 四層分離

$$
\boxed{
h
\rightarrow
a
\rightarrow
e
\rightarrow
k.
}
$$

其中：

- $h$：hypothesis；
- $a$：executable attack；
- $e$：execution evidence；
- $k$：經抽象與 transfer 驗證後的 attack knowledge。

任何一層都不能跳過。

---

# 4. Bounded Adversarial Novelty

定義 novelty context：

$$
\mathcal N
=
(K,\Gamma,\Pi,\mathcal O,B,t).
$$

如果：

$$
Novel_B(a\mid\mathcal N)=1,
$$

只表示 attack 在目前 bounded generation context 中不是已知 closure 的直接成員。

所以：

$$
\boxed{
Novel_B
\neq
\text{Historical Priority}.
}
$$

若要宣稱全球學術首創，仍需外部文獻與歷史搜尋。

---

# 5. Attack Closure

$$
Cl_A(K\mid\Gamma,\Pi,\mathcal O,B,t)
$$

可包含：

- known templates；
- known macros；
- known compositions；
- known specializations；
- known equivalence classes。

系統不必真的 materialize 全部 closure；可以保存 generators、grammar、family hierarchy 與 rewrite rules。

---

# 6. Residual Gap Field

定義：

$$
\boxed{
G_R
=
(
G_V,
G_E,
G_X,
G_I,
G_P,
G_T,
G_Q,
G_H
).
}
$$

其中：

- $G_V$：component gap；
- $G_E$：relation gap；
- $G_X$：state gap；
- $G_I$：invariant gap；
- $G_P$：path gap；
- $G_T$：temporal gap；
- $G_Q$：validator / observability gap；
- $G_H$：history / version gap。

---

# 7. Creativity Routing

對 residual：

$$
g,
$$

定義：

$$
Priority(g)
=
\frac{
Risk(g)
\cdot
Uncertainty(g)
\cdot
Impact(g)
}{
ExpectedReasoningCost(g)+\epsilon
}.
$$

高風險、高未知、低已知覆蓋區，才值得前沿 reasoning。

---

# 8. 十類 ACG 操作

$$
\boxed{
\mathfrak O_{ACG}
=
\{
Retrieve,
Compose,
Relate,
Bridge,
Abstract,
Specialize,
Macro,
Reframe,
Primitive,
Distill
\}.
}
$$

`Retrieve` 找回已知 attack；`Compose` 組合已知 attack；`Relate` 提出新的 typed attack relation；`Bridge` 提出跨結構的 failure bridge；`Abstract` 從多個 witness 找共同機制；`Specialize` 收窄過廣 family；`Macro` 壓縮反覆 sequence；`Reframe` 改變 representation；`Primitive` 提出現有 grammar 不足；`Distill` 把成功 attack 壓成最小可重建語義。

---

# 9. 創造不是自由聯想

若候選 attack 完全不綁：

- project model；
- residual；
- invariant；
- state；
- evidence；

那只是：

$$
\boxed{
\text{Adversarial Brainstorming}.
}
$$

不是高品質 adversarial creativity。

定義 hypothesis grounding：

$$
Ground(h)
=
f(
Structure,
Invariant,
State,
History,
Residual,
Evidence
).
$$

要求：

$$
Ground(h)\ge\tau_G.
$$

---

# 10. Creativity Quality

$$
\boxed{
Q_C(a)
=
\frac{
Novelty
\cdot
Validity
\cdot
MechanismValue
\cdot
TransferPotential
}{
ReasoningCost+\epsilon
}.
}
$$

其中 novelty 只是其中一項。

所以：

$$
\boxed{
\text{Novelty Maximization}
\neq
\text{Engineering Creativity}.
}
$$

---

# 11. Generation Quality

$$
\boxed{
Q_G(a)
=
f(
Executable,
Isolated,
Observable,
Verifiable,
Recoverable,
Reproducible
).
}
$$

一個 executable attack 至少需要：

- fixture；
- bounded perturbation；
- schedule；
- observation；
- validator；
- positive / negative controls；
- restore / discard semantics。

---

# 12. Attack Generation Pipeline

$$
h
\rightarrow
a_{\mathrm{typed}}
\rightarrow
a_{\mathrm{sandbox}}
\rightarrow
a_{\mathrm{validated}}.
$$

先補齊 attack semantics，再生成隔離 experiment，最後建立 validator 與 controls。

---

# 13. Generated Attack 不等於 Production Mutation

$$
\boxed{
\text{Generated Attack}
\neq
\text{Production Mutation}.
}
$$

所有 generation 都必須經：

$$
Auth(a,S)=1
$$

以及：

$$
Scope(a)
\subseteq
Scope_{\mathrm{authorized}}.
$$

---

# 14. Attack Family Novelty

parameter value 變化通常不構成新 family。

若：

$$
a'
$$

只是：

- 不同名字；
- 不同 delay value；
- 不同 fixture；

但 failure mechanism 相同，應視為 variant。

新 family 至少應有某種：

$$
\Delta Mechanism>0
$$

或 applicability / invariant / validation semantics 的重要差異。

---

# 15. Family Proposal

$$
F_{\mathrm{new}}
=
\operatorname{ProposeFamily}
(a_1,\ldots,a_k).
$$

先標記：

$$
PROPOSED.
$$

只有具備：

- multiple witnesses；
- mechanism consistency；
- negative control；
- transfer evidence；

才：

$$
PROPOSED
\rightarrow
VALIDATED
\rightarrow
PROMOTED.
$$

---

# 16. Attack Grammar

定義：

$$
\Gamma_A
$$

包含：

- primitives；
- combinators；
- conditions；
- observation operators；
- recovery operators。

Creativity 可以先在：

$$
\Gamma_A
$$

內探索。

---

# 17. Representation Escape

如果：

$$
\Gamma_A
$$

一直生成同一 failure family，可改 representation：

$$
\Pi_1
\rightarrow
\Pi_2.
$$

例如：

$$
\text{file/module graph}
\rightarrow
\text{state-transition graph}.
$$

定義：

$$
RV(\Pi_2)
=
\Delta
\text{Residual Visibility}.
$$

---

# 18. Primitive Proposal

如果新 representation 仍無法忠實表達：

$$
h,
$$

可以提出：

$$
p_{\mathrm{primitive}}.
$$

其 certificate 綁定：

$$
(\Gamma,\Pi,\mathcal O,B,Failures).
$$

它只表示目前 grammar / operator set 不足，不表示新 primitive 在本體論上永久不可還原。

---

# 19. Analogical Creativity

AI 可以建立 typed mapping：

$$
\phi:
Structure_A
\rightarrow
Structure_B.
$$

再測：

$$
Transfer(F_A,\phi).
$$

表面名稱相似不夠；真正 mapping 應看：

- role；
- state；
- lifecycle；
- ownership；
- invariant。

所以：

$$
\boxed{
\text{Analogy}
\neq
\text{Copy}.
}
$$

---

# 20. Counterfactual Creativity

AI 可以問：

> 如果目前某個 high-risk invariant 的保證失效，最小需要改變什麼？

可寫：

$$
a^\ast
=
\arg\min_a
Perturbation(a)
$$

subject to：

$$
I(T_a(x))=0.
$$

這比任意 catastrophic destruction 更有資訊價值。

---

# 21. Failure Boundary

定義：

$$
\mathcal F
=
\{
x:I(x)=0
\}.
$$

高價值 attack 常嘗試靠近：

$$
\partial\mathcal F,
$$

以估計 robustness margin，而不是只追求最大破壞。

---

# 22. Attack Generation as Program Synthesis

給：

$$
Spec_a
=
(P,I,E,R,B),
$$

生成：

$$
p_a.
$$

但：

$$
\boxed{
\text{Generated Code}
\neq
\text{Validated Attack}.
}
$$

仍需執行 evidence。

---

# 23. Execution Feedback

如果：

$$
a
$$

是 `NotApplicable`，更新 $P$。

如果 false positive，更新 $V$。

如果出現非預期 failure，形成新的：

$$
h_{\mathrm{new}}.
$$

所以：

$$
\boxed{
\text{Generate}
\rightarrow
\text{Execute}
\rightarrow
\text{Observe}
\rightarrow
\text{Revise}.
}
$$

---

# 24. Outcome Classification

至少區分：

$$
Outcome
\in
\{
ProductDefect,
AttackInvalid,
HarnessDefect,
EnvironmentUnsupported,
NotMeasured,
Unknown
\}.
$$

不能把所有 red 都算 product defect。

---

# 25. Candidate Memory 與 Promoted Memory

所有 novel hypotheses 可先進：

$$
K_{\mathrm{candidate}}.
$$

只有通過 GACEI-03 promotion gate 才進：

$$
K_{\mathrm{promoted}}.
$$

---

# 26. Failed Hypothesis 也可形成負知識

若 plausible hypothesis 被清楚 falsify：

$$
h\rightarrow FALSIFIED.
$$

可以保存：

$$
K^-.
$$

其價值是避免未來重新支付同一失敗探索成本。

---

# 27. Novelty Audit

對新候選：

$$
AuditNovelty(a,K_A)
$$

輸出：

```text
KNOWN
DUPLICATE
SPECIALIZATION
GENERALIZATION
COMPOSITION
BOUNDARY-NOVEL
MECHANISM-NOVEL
UNKNOWN
```

其中：

$$
UNKNOWN
\neq
NOVEL.
$$

---

# 28. Creativity Inflation

若每個 parameter variant 都被標成「新 attack」：

$$
NoveltyInflation\uparrow.
$$

所以 family-level novelty 要求：

$$
\Delta Mechanism>0
$$

或等價的重要結構差異。

---

# 29. Generative Efficiency

$$
GE
=
\frac{
ValidNovelAttacks
}{
GenerationCost+\epsilon
}.
$$

Creativity precision：

$$
CP
=
\frac{
UsefulNovelHypotheses
}{
AllNovelHypotheses
}.
$$

若 benchmark 有 hidden mechanisms，可定義 creativity recall：

$$
CR
=
\frac{
NovelMechanismsFound
}{
NovelMechanismsInScope
}.
$$

---

# 30. Budget Coupling

總預算：

$$
B
=
B_C+B_G+B_E+B_V,
$$

分別為：

- creativity；
- generation；
- execution；
- verification。

不能把所有算力都花在「想 attack」。

必須保留：

$$
B_V>0.
$$

---

# 31. Creativity Shadow Price

若：

$$
MarginalNovelValue
<
\lambda_B,
$$

停止生成新 attack。

這直接避免：

> 只要還想得到，就一直生成。

---

# 32. Attack Family Discovery Loop

$$
\boxed{
\text{Observe}
\rightarrow
\text{Model}
\rightarrow
\text{Residual}
\rightarrow
\text{Hypothesize}
\rightarrow
\text{Type}
\rightarrow
\text{Generate}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Localize}
\rightarrow
\text{Abstract}
\rightarrow
\text{Transfer}
\rightarrow
\text{Promote}.
}
$$

如果：

$$
\Delta K_{\mathrm{useful}}
\approx0,
$$

停止。

---

# 33. Cost-Normalized Learning Gain

定義：

$$
NLG_t
=
\frac{
|K_{t+1}^{\mathrm{useful}}-K_t^{\mathrm{useful}}|
}{
Cost_t+\epsilon
}.
$$

若：

$$
NLG_t<\lambda_L,
$$

停止本輪 discovery。

---

# 34. Creativity 與 Generation 在能力向量中的分離

$$
C
=
\text{Creativity}
$$

回答：

> 能否提出新的 failure mechanism？

$$
G
=
\text{Generation}
$$

回答：

> 能否把它變成 executable experiment？

$$
K
=
\text{Computation}
$$

回答：

> 哪些候選值得投資？

$$
V
=
\text{Verification}
$$

回答：

> 是否真的命中？

$$
M
=
\text{Memory}
$$

回答：

> 如何把它學會？

---

# 35. 四種失衡

## 35.1 Creativity Without Understanding

容易形成：

$$
\text{Hallucinated Attack}.
$$

## 35.2 Understanding Without Creativity

形成優秀 reviewer，但弱 discoverer。

## 35.3 Creativity Without Verification

容易形成：

$$
\text{Attack Fiction}.
$$

## 35.4 Generation Without Creativity

容易形成大量 test boilerplate。

---

# 36. MSSP 作第一個創造 Benchmark

MSSP 適合第一階段，因為：

- invariant 清晰；
- topology 清晰；
- known attack corpus 已有；
- residual 可控制。

可給 AI 一個新的 MSSP App，隱藏一組 synthetic failure mechanisms，不給 attack descriptions。

---

# 37. Hidden Failure 分層

Benchmark 可包含：

1. known family variant；
2. known composition；
3. benchmark-defined novel family。

AI 需要先分類：

$$
KNOWN,
COMPOSITION,
NOVEL.
$$

---

# 38. Generation Benchmark

對 novel hypothesis：

$$
h,
$$

要求 AI 生成：

- synthetic fixture；
- bounded mutation；
- observation；
- validator；
- recovery。

所有 experiment 必須：

$$
Scope\subseteq Sandbox.
$$

---

# 39. Evaluation Vector

$$
\boxed{
\boldsymbol S_{ACG}
=
(
NoveltyPrecision,
NoveltyRecall,
GenerationValidity,
ExecutionSafety,
DefectRecall,
Localization,
Transfer,
Cost
).
}
$$

---

# 40. 比較系統

### A：Replay-only

只用 memory。

### B：Random Mutation

只做隨機變異。

### C：Free Brainstorming

自由生成 attack ideas。

### D：Residual-Guided ACG

使用本文框架。

理想假說：D 在 useful novelty、validity 與 cost efficiency 上較佳。

---

# 41. 研究假說

## H1：Residual-guided creativity 優於 unconstrained brainstorming

$$
Q_C^{\mathrm{residual}}
>
Q_C^{\mathrm{free}}
$$

在部分工程 benchmark 中成立。

## H2：Creativity / generation 分離可降低 invalid attack

先 hypothesis 再 executable generation，應降低 false attack rate。

## H3：Bounded novelty 可降低 novelty inflation

對 parameter variants：

$$
FalseNovelty\downarrow.
$$

## H4：Negative knowledge 可降低失敗 hypothesis 的重複發現

若：

$$
K^-
$$

存在，rediscovery cost 應下降。

## H5：Representation reframe 可增加 novel mechanism discovery

在部分 project：

$$
Novel(\Pi_2)
>
Novel(\Pi_1).
$$

---

# 42. 本文非主張

本文不主張：

1. AI 能證明某 attack 是全人類歷史首創；
2. novelty 越高越好；
3. 所有 novel hypothesis 都值得執行；
4. attack generation 等於 real-world exploitation；
5. program synthesis 成功等於 defect finding；
6. random mutation 沒有價值；
7. known memory 應限制 creativity；
8. creativity 可以脫離 project understanding；
9. creativity 可以脫離 authorization；
10. 所有 attack family 都存在唯一自然分類；
11. reframe 一定產生新知識；
12. primitive proposal 等於不可還原的新存在；
13. 所有 failed hypotheses 都值得永久保存；
14. cross-domain analogy 可以直接 copy；
15. generated attack 可以直接作用 production；
16. 本文可用於未授權第三方系統攻擊。

本文主張的是：

$$
\boxed{
\text{對抗性創造應被 residual、結構、invariant、risk 與 evidence 約束，}
}
$$

以及：

$$
\boxed{
\text{failure hypothesis 必須經 executable generation 與 sandbox verification 才能成為工程知識。}
}
$$

---

# 43. 與 GACEI-08 的關係

GACEI-08 回答：

$$
\boxed{
\text{理解到什麼程度才有資格談 adversarial understanding？}
}
$$

本文回答：

$$
\boxed{
\text{有了理解後，怎麼產生以前沒有的 failure hypothesis？}
}
$$

---

# 44. 與 DEST-08 的關係

DEST-08 已建立：

$$
\text{Gap}
\rightarrow
\text{Proposal}
\rightarrow
\text{Guard}
\rightarrow
\text{Verify}
\rightarrow
\text{Glue}.
$$

本文將其收斂到 adversarial engineering domain：

$$
\boxed{
\text{Residual Gap}
\rightarrow
\text{Attack Proposal}
\rightarrow
\text{Typing}
\rightarrow
\text{Generation}
\rightarrow
\text{Verification}
\rightarrow
\text{Memory}.
}
$$

---

# 45. 下一篇：全域攻擊的計算理論

GACEI-10 將把：

$$
A_{\mathrm{known}}
+
A_{\mathrm{novel}}
$$

放進有限算力系統。

核心問題：

$$
\boxed{
\text{AI 在組合爆炸的 attack space 中，如何配置計算、記憶、尋址、並行與驗證資源？}
}
$$

---

# 46. 結論

如果未來 AI 只能：

> 從 attack database 裡找一個最像的測試。

那它具備的是：

$$
\boxed{
\text{Adversarial Retrieval}.
}
$$

如果它能把兩個已知 attack 重新組合，則是：

$$
\boxed{
\text{Adversarial Composition}.
}
$$

更高階的能力是：

> **AI 看懂一個以前沒看過的專案後，能不能指出目前 corpus 沒有直接記錄的 failure mechanism，說明為什麼值得懷疑，再生成一套最小、可執行、可觀測、可驗證、可恢復的 sandbox experiment 去證明或推翻它？**

這才是：

$$
\boxed{
\text{Adversarial Creativity}
+
\text{Executable Generation}.
}
$$

因此本文把能力壓縮成：

$$
\boxed{
\text{Understand}
\rightarrow
\text{See the Residual}
\rightarrow
\text{Create a Failure Hypothesis}
\rightarrow
\text{Generate an Experiment}
\rightarrow
\text{Verify}
\rightarrow
\text{Learn}.
}
$$

而「從未見過」的嚴謹版本不是「全球歷史上沒人見過」，而是：

$$
\boxed{
\text{目前 AI 的 attack memory、grammar、representation、operator set 與 resource-bounded closure 無法直接生成或識別。}
}
$$

這個限制反而讓「創造能力」變成可 benchmark、可比較、可反駁的工程概念。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
