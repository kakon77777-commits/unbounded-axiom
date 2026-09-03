# ALD-03｜法律函數不是 Boolean：部分算子、證書、裁量與失敗語義
## Legal Functions Are Not Boolean: Partial Operators, Certificates, Discretion, and Failure Semantics

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 03 篇 / 10  
**前篇：** ALD-02〈載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／計算法學／法律算子／失敗語義／Machine-Executable Law  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

ALD-01 已提出 AI Legal Domain 與可調用的 `LawCall`；ALD-02 又指出法律規則必須依 carrier type、jurisdiction、time 與 legal purpose 做型別化解釋。本文處理下一個核心問題：**法律函數的輸出究竟是什麼？**

最簡單的工程實作常把法律判斷壓成：

```text
allowed = true / false
```

但這會將法律上完全不同的狀態混成同一個 `false`：真正禁止、缺乏證據、無司法管轄、身份未決、角色未成立、規則衝突、程序尚未完成、需要裁量、需要上級批准、規則已過期、carrier translation 尚未完成，全部可能被誤判成「法律禁止」。反方向同樣危險：沒有找到 prohibition 並不一定等於 positive permission。

本文因此提出 Legal Partial Operator Framework（LPOF）。其最低法律調用形式為：

$$
\boxed{
\operatorname{LawEval}_{J,t,d}
:
\mathcal Q_L
\rightharpoonup
\mathcal R_L
\sqcup
\mathcal F_L,
}
$$

其中 $\mathcal Q_L$ 是經型別化的法律查詢空間， $\mathcal R_L$ 是成功形成的 proof-carrying legal result， $\mathcal F_L$ 是結構化失敗空間。法律函數是 partial，因為某些 query 本來就不在該法域、該時間、該角色或該證據狀態下有定義。

本文進一步拒絕把 $\mathcal R_L$ 本身縮成單一枚舉。成熟法律結果至少應包含：

$$
\boxed{
\mathfrak R_L
=
(
N,
K,
P,
A,
V,
C,
X,
R
),
}
$$

其中：

- $N$：normative status；
- $K$：epistemic / evidence status；
- $P$：procedural status；
- $A$：authority status；
- $V$：validity / version status；
- $C$：conflict / defeasibility state；
- $X$：explanation / proof certificate；
- $R$：review / appeal route。

因此可以同時出現：

```text
normative_status = PERMITTED
evidence_status = SUFFICIENT
procedure_status = INCOMPLETE
authority_status = APPROVAL_REQUIRED
```

此時將整個結果投影成 `true` 明顯錯誤。

本文提出 No Boolean Collapse Principle：

$$
\boxed{
\text{Legal Semantics}
\not\equiv
\{0,1\}.
}
$$

如果某執行系統最終必須決定 `execute / block / escalate`，應由 query-specific gate：

$$
\boxed{
\pi_q:
\mathfrak R_L
\rightarrow
\{
\mathsf{Execute},
\mathsf{Block},
\mathsf{Escalate}
\}
}
$$

作最後投影。布林或三值 gate 是 decision projection，不是法律本體。

本文並將法律規範分為至少四個層次：constitutive rules、prescriptive / deontic rules、power-conferring rules 與 procedural / remedial rules。OASIS LegalRuleML 已正式支援 defeasibility、obligations、permissions、prohibitions、rights、negation、temporality、jurisdiction、authority 與 rule priority；Catala 則以 prioritized default logic 直接處理法律中的 base rule / exception 結構。這些外部工程已清楚顯示：法律計算不是一個單純布林條件樹。

本文特別建立 Discretion Capsule。當法律明確保留 interpretation、evaluation 或 authorised discretion 時，AI Legal Runtime 不應偷偷用任意模型判斷補成 deterministic answer，而應輸出：

$$
\boxed{
\mathsf{AuthorizedDecisionRequired}
}
$$

並附上合法 decision space、decision authority、mandatory considerations、forbidden considerations、evidence basis、deadline 與 review route。OECD 2026 Law as Code consultation 亦明確要求 interpretive、discretionary、evaluative elements 維持可見，而不是被靜默轉成 deterministic rule。

最後，本文提出 Legal Result Certificate 與 Legal Failure Certificate。成功結果與失敗結果都必須可稽核。`Forbidden` 是一個規範結論；`EvidenceMissing`、`JurisdictionUnresolved`、`AuthorityMissing` 等則不是禁止，而是法律 Runtime 無法合法完成某一階段。這種失敗型別分離是 AI-native law 能否保持 rule-of-law 可解釋性與可申訴性的最低條件。

---

## 關鍵詞

AI 法律域；Legal Partial Operator；LawCall；Boolean Collapse；LegalRuleML；Catala；Defeasibility；Deontic Logic；Discretion；Failure Semantics；Legal Certificate；Permission；Obligation；Prohibition；Appeal

---

# 0. 前兩篇交接

ALD-01 建立：

$$
\operatorname{LawCall}_{J,t,d}
(s,r,a,o,e).
$$

ALD-02 又要求：

$$
s
\rightarrow
(s,\chi(s)),
$$

也就是法律查詢必須知道 carrier type。

但如果 Runtime 最後仍只輸出：

```text
true
false
```

前兩篇建立的：

- identity；
- role；
- carrier；
- evidence；
- jurisdiction；
- authority；
- version；
- procedure；

就會在輸出端全部重新被壓扁。

因此本篇正式處理：

$$
\boxed{
\text{legal result type}.
}
$$

---

# 1. 第一個錯誤：`false` 到底是什麼意思？

假設：

```text
permission.check(...) = false
```

它可能代表：

1. 法律明文禁止；
2. 沒有 positive permission；
3. identity proof 不足；
4. role 未成立；
5. delegation 已過期；
6. jurisdiction 不適用；
7. evidence 不足；
8. rule conflict；
9. exception 尚未解析；
10. authority 不足；
11. procedure 尚未完成；
12. approval required；
13. current rule version 無法解析；
14. carrier translation 未定；
15. system error。

這十五種狀態不能共享一個法律語義。

---

# 2. Forbidden 不等於 Unknown

最重要的分離之一：

$$
\boxed{
\mathsf{Forbidden}
\neq
\mathsf{Unknown}.
}
$$

`Forbidden` 表示已有足夠法律依據形成禁止性規範結論。

`Unknown` 則可能只表示：

> 系統目前不知道。

兩者若混合，會把 epistemic failure 偽裝成 substantive law。

---

# 3. Evidence Missing 不等於 Prohibition

$$
\boxed{
\mathsf{EvidenceMissing}
\neq
\mathsf{Forbidden}.
}
$$

例如：

> Agent A 是否有 delegation？

目前找不到 certificate。

合法輸出可能是：

$$
\mathsf{EvidenceMissing}.
$$

不是：

> 法律禁止 A 永遠執行。

---

# 4. No Jurisdiction 不等於 Permission

反方向也要防止。

如果：

$$
J_1
$$

沒有管轄權，

不能推出：

$$
\mathsf{Allowed}.
$$

因為可能真正適用：

$$
J_2.
$$

因此：

$$
\boxed{
\mathsf{JurisdictionMismatch}
\neq
\mathsf{Allowed}.
}
$$

---

# 5. Silence 不等於 Strong Permission

OASIS LegalRuleML 本身區分 weak permission 與 strong permission。

所以：

$$
\boxed{
\text{Not Proven Forbidden}
\neq
\text{Explicitly Permitted}.
}
$$

在某些 legal systems / domains 中：

- silence；
- weak permission；
- explicit exception；
- affirmative licence；

可能具有不同效果。

---

# 6. Legal Partial Operator

本文定義法律查詢空間：

$$
\mathcal Q_L
=
\{
q
\}.
$$

每個 query 至少可包含：

$$
q
=
(
s,
\chi,
r,
a,
o,
J,
t,
d,
e,
p
),
$$

其中：

- $s$：subject / actor；
- $\chi$：carrier profile；
- $r$：role；
- $a$：candidate action / state；
- $o$：object；
- $J$：jurisdiction；
- $t$：time；
- $d$：legal domain；
- $e$：evidence state；
- $p$：legal purpose。

---

# 7. LawEval

本文正式寫成：

$$
\boxed{
\operatorname{LawEval}_{J,t,d}
:
\mathcal Q_L
\rightharpoonup
\mathcal R_L
\sqcup
\mathcal F_L.
}
$$

這裡使用：

$$
\rightharpoonup
$$

而不是：

$$
\rightarrow
$$

因為法律函數天然可能在某些輸入上無合法定義。

---

# 8. 為什麼是 Partial？

至少有六類原因：

1. query 不屬於此 jurisdiction；
2. legal type 不成立；
3. required facts 不足；
4. applicable rule 不存在；
5. carrier translation 未定；
6. procedure 尚未達到 decision stage。

因此 total function：

$$
f:
\mathcal Q_L
\rightarrow
\{0,1\}
$$

常常只是把未定義狀態硬塞成假答案。

---

# 9. 成功結果也不是單一枚舉

本文定義：

$$
\boxed{
\mathfrak R_L
=
(
N,
K,
P,
A,
V,
C,
X,
R
).
}
$$

---

# 10. $N$：Normative Status

最低：

$$
N
\in
\{
\mathsf{Permitted},
\mathsf{Forbidden},
\mathsf{Obligatory},
\mathsf{PowerGranted},
\mathsf{NoPower},
\mathsf{Immunity},
\mathsf{Liable},
\mathsf{NoSubstantiveConclusion}
\}.
$$

這一層回答：

> 法律規範本身說什麼？

---

# 11. $K$：Epistemic / Evidence Status

最低：

$$
K
\in
\{
\mathsf{Sufficient},
\mathsf{Insufficient},
\mathsf{Contested},
\mathsf{Unverified},
\mathsf{Stale},
\mathsf{Inadmissible},
\mathsf{Unknown}
\}.
$$

這一層回答：

> 我們知道得夠不夠？

---

# 12. $P$：Procedural Status

$$
P
\in
\{
\mathsf{Ready},
\mathsf{NoticeRequired},
\mathsf{HearingRequired},
\mathsf{WaitingResponse},
\mathsf{ApprovalPending},
\mathsf{ReviewPending},
\mathsf{TimeBarred},
\mathsf{ProcedureIncomplete}
\}.
$$

它回答：

> 就算 substantive rule 已經知道，現在是否可以合法形成／執行決定？

---

# 13. $A$：Authority Status

$$
A
\in
\{
\mathsf{Authorized},
\mathsf{Unauthorized},
\mathsf{Delegated},
\mathsf{ApprovalRequired},
\mathsf{AuthorityConflict},
\mathsf{AuthorityUnknown}
\}.
$$

它回答：

> 誰有權做這個法律行為或決定？

---

# 14. $V$：Validity / Version

$$
V
=
(
\nu,
t_{\mathrm{from}},
t_{\mathrm{until}},
\mathsf{status}
).
$$

其中：

$$
\mathsf{status}
\in
\{
\mathsf{Current},
\mathsf{Expired},
\mathsf{Superseded},
\mathsf{Future},
\mathsf{Unresolved}
\}.
$$

---

# 15. $C$：Conflict / Defeasibility State

$$
C
\in
\{
\mathsf{Clear},
\mathsf{ExceptionApplied},
\mathsf{OverrideApplied},
\mathsf{ConflictUnresolved},
\mathsf{PriorityUnresolved},
\mathsf{MultipleApplicableRules}
\}.
$$

---

# 16. $X$：Explanation / Proof

$$
X
=
(
\text{basis},
\text{evidence},
\text{authority},
\text{rule path},
\text{exceptions},
\text{certificate}
).
$$

---

# 17. $R$：Review / Appeal Route

$$
R
=
(
\text{challengeable},
\text{review body},
\text{deadline},
\text{required filing},
\text{effect of appeal}
).
$$

---

# 18. 一個合法結果可以看起來「矛盾」

例如：

```text
N = PERMITTED
K = SUFFICIENT
P = APPROVAL_PENDING
A = APPROVAL_REQUIRED
C = CLEAR
```

這沒有矛盾。

它只是表示：

> substantive law 原則上允許，但尚未完成合法批准程序。

---

# 19. 所以 `Permitted` 不等於 `ExecutableNow`

$$
\boxed{
\mathsf{Permitted}
\neq
\mathsf{ExecutableNow}.
}
$$

最終可執行可能要求：

$$
N=\mathsf{Permitted}
$$

且：

$$
P=\mathsf{Ready}
$$

且：

$$
A=\mathsf{Authorized}.
$$

---

# 20. No Boolean Collapse Principle

本文提出：

$$
\boxed{
\text{Legal Semantics}
\not\equiv
\{0,1\}.
}
$$

任何將：

$$
\mathfrak R_L
$$

直接壓成：

$$
0/1
$$

的動作都必須明示其 projection policy。

---

# 21. Decision Projection

若實際執行層只需要：

```text
EXECUTE
BLOCK
ESCALATE
```

則定義：

$$
\boxed{
\pi_q:
\mathfrak R_L
\rightarrow
\{
\mathsf{Execute},
\mathsf{Block},
\mathsf{Escalate}
\}.
}
$$

 $\pi_q$ 必須是：

- query-specific；
- domain-specific；
- risk-sensitive；
- versioned；
- auditable。

---

# 22. Projection 不是法律本體

$$
\boxed{
\pi_q(\mathfrak R_L)
\neq
\mathfrak R_L.
}
$$

就像：

> 紅燈

不是：

> 全部交通法。

---

# 23. LegalRuleML 已拒絕最簡單 Boolean 法律

OASIS LegalRuleML Core Specification 1.0 明確建模：

- defeasibility；
- obligations；
- permissions；
- prohibitions；
- rights；
- negation；
- temporality；
- constitutive / prescriptive norms；
- jurisdiction；
- authority / rule source；
- priority / override。

因此其外部結構本身已支持：

$$
\boxed{
\text{law}
\neq
\text{simple Boolean condition tree}.
}
$$

---

# 24. Constitutive Rule 與 Prescriptive Rule

## Constitutive

回答：

> X 在這個 jurisdiction 中算什麼？

例如：

$$
\mathsf{Employee}(x).
$$

## Prescriptive

回答：

> 若 X 屬某類，應該／可以／禁止什麼？

例如：

$$
[OBL]\mathsf{PayTax}(x).
$$

兩者不能混成同一 predicate。

---

# 25. Deontic Operators

最低：

$$
[OBL]p
$$

表示 obligation；

$$
[PER]p
$$

表示 permission；

$$
[FOR]p
$$

表示 prohibition。

因此：

$$
\boxed{
\text{fact}
\neq
\text{normative modality}.
}
$$

---

# 26. Fact True 不等於 Action Permitted

即使：

$$
\mathsf{CanDeleteFile}(A)=1,
$$

也不能推出：

$$
[PER]\mathsf{DeleteFile}(A).
$$

這與分域憲章的：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}.
}
$$

一致。

---

# 27. Defeasibility

法律規則常是：

> 一般成立，除非例外。

形式上：

$$
r_0:
C\Rightarrow N,
$$

但若：

$$
E_1
$$

成立，

則：

$$
r_1
\succ
r_0.
$$

所以：

$$
\boxed{
\text{Applicable Rule}
\neq
\text{Final Rule After Exceptions}.
}
$$

---

# 28. Catala 的工程旁證

Catala 的法律程式語言直接使用 prioritized default logic 處理：

- base definitions；
- conditional definitions；
- exceptions；
- priority。

這證明「法律規則 + 例外」可以被做成精確可執行語義，而不是只能寫成自然語言備註。

但 Catala 主要是法律計算語言，不等於完整 AI Legal Domain。

---

# 29. Exception 不等於 Conflict

如果：

$$
r_1
\succ
r_0
$$

而 $r_1$ 是合法 exception，

這是：

$$
\mathsf{ExceptionApplied}.
$$

不是：

$$
\mathsf{ConflictUnresolved}.
$$

所以：

$$
\boxed{
\text{Exception}
\neq
\text{Contradiction}.
}
$$

---

# 30. Conflict 也不是 0.5

如果：

$$
[PER]p
$$

與：

$$
[FOR]p
$$

同時可推出，

不能平均：

$$
0.5.
$$

必須查：

- rule hierarchy；
- lex specialis；
- lex posterior；
- jurisdiction；
- exception；
- authority；
- precedent；
- explicit override。

---

# 31. Minimal Conflict Set

可延續分域憲章：

對 rule bundle：

$$
B
$$

找：

$$
M\subseteq B
$$

使：

$$
\mathsf{Unsat}(M),
$$

且所有 proper subset 可滿足。

這可形成：

$$
\boxed{
\text{Minimal Legal Conflict Set}.
}
$$

---

# 32. Discretion 不是 Randomness

法律中的 discretion 不是：

```python
return random.choice(options)
```

而是：

$$
\boxed{
\text{bounded legally authorised choice}.
}
$$

---

# 33. Discretion Capsule

本文定義：

$$
\boxed{
\mathfrak D_C
=
(
\Omega_D,
A_D,
M_D,
F_D,
E_D,
T_D,
R_D
).
}
$$

其中：

- $\Omega_D$：合法 decision space；
- $A_D$：authorized decision-maker；
- $M_D$：mandatory considerations；
- $F_D$：forbidden considerations；
- $E_D$：evidence basis；
- $T_D$：deadline / timing；
- $R_D$：review route。

---

# 34. AuthorizedDecisionRequired

若法律保留裁量：

$$
\operatorname{LawEval}(q)
$$

不應偷偷產生 substantive outcome。

而應：

$$
\boxed{
N
=
\mathsf{NoSubstantiveConclusion},
}
$$

$$
\boxed{
A
=
\mathsf{ApprovalRequired},
}
$$

並輸出：

$$
\mathfrak D_C.
$$

---

# 35. OECD 2026 Law as Code 的邊界

OECD 明確要求：

> interpretive、discretionary、evaluative elements remain visible rather than silently converted into deterministic rules。

這和本文：

$$
\boxed{
\text{Discretion Preservation Principle}
}
$$

完全相容。

---

# 36. Discretion Preservation Principle

$$
\boxed{
\text{Legal Discretion}
\not\Rightarrow
\text{Implementation Gap to Be Auto-Filled}.
}
$$

如果 law intentionally leaves choice，

Runtime 必須保存 choice 的制度位置。

---

# 37. AI 可以協助裁量，但不能偷換 Authority

AI 可以：

- organize evidence；
- compare precedent；
- generate options；
- identify mandatory factors；
- simulate consequences。

但：

$$
\boxed{
\text{AI Assistance}
\neq
\text{Decision Authority}.
}
$$

除非法源正式授權。

---

# 38. Failure Space

本文定義：

$$
\boxed{
\mathcal F_L
=
\mathcal F_{\mathrm{type}}
\sqcup
\mathcal F_{\mathrm{jur}}
\sqcup
\mathcal F_{\mathrm{evid}}
\sqcup
\mathcal F_{\mathrm{auth}}
\sqcup
\mathcal F_{\mathrm{proc}}
\sqcup
\mathcal F_{\mathrm{norm}}
\sqcup
\mathcal F_{\mathrm{version}}
\sqcup
\mathcal F_{\mathrm{carrier}}
\sqcup
\mathcal F_{\mathrm{tech}}.
}
$$

---

# 39. Type Failure

例如：

- wrong legal entity type；
- role incompatible；
- object outside domain。

輸出：

$$
\mathsf{TypeMismatch}.
$$

---

# 40. Jurisdiction Failure

$$
\mathsf{JurisdictionUnresolved},
\qquad
\mathsf{JurisdictionMismatch}.
$$

---

# 41. Evidence Failure

$$
\mathsf{EvidenceMissing},
\mathsf{EvidenceInadmissible},
\mathsf{EvidenceConflict},
\mathsf{ProofStale}.
$$

---

# 42. Authority Failure

$$
\mathsf{AuthorityMissing},
\mathsf{DelegationExpired},
\mathsf{AuthorityConflict},
\mathsf{UnauthorizedDecisionMaker}.
$$

---

# 43. Procedure Failure

$$
\mathsf{NoticeMissing},
\mathsf{HearingRequired},
\mathsf{ApprovalPending},
\mathsf{ProcedureIncomplete}.
$$

---

# 44. Norm Failure

$$
\mathsf{RuleGap},
\mathsf{NormConflict},
\mathsf{ExceptionUnresolved},
\mathsf{PriorityUnresolved}.
$$

---

# 45. Version Failure

$$
\mathsf{RuleExpired},
\mathsf{VersionMismatch},
\mathsf{TransitionRuleMissing}.
$$

---

# 46. Carrier Failure

延續 ALD-02：

$$
\mathsf{CarrierTranslationRequired},
\mathsf{OntologyGap},
\mathsf{CarrierTypeUnresolved}.
$$

---

# 47. Technical Failure

例如 parser / database / network error。

這應明確輸出：

$$
\mathsf{TechnicalError}.
$$

不能偽裝成：

$$
\mathsf{Forbidden}.
$$

---

# 48. Failure Recovery Class

每個 failure 應標：

$$
\boxed{
\rho_F
\in
\{
\mathsf{Retryable},
\mathsf{EvidenceRecoverable},
\mathsf{ReviewRequired},
\mathsf{RuleChangeRequired},
\mathsf{NotRecoverableInCurrentDomain}
\}.
}
$$

---

# 49. Legal Failure Certificate

本文定義：

$$
\boxed{
K_F
=
(
q,
f,
\text{stage},
\text{reason},
\text{missing conditions},
\text{source},
\nu,
\text{affected scope},
\rho_F,
R
).
}
$$

其中 $R$ 是 review / remediation route。

---

# 50. Success Certificate

成功結果也要 certificate：

$$
\boxed{
K_L
=
(
q,
N,
K,
P,
A,
V,
C,
\text{basis},
\text{evidence},
\text{rule path},
R
).
}
$$

---

# 51. Proof-Carrying Legal Result

因此成熟輸出：

$$
\boxed{
\operatorname{LawEval}(q)
=
(
\mathfrak R_L,
K_L
)
}
$$

而不是：

```text
TRUE
```

---

# 52. Certificate 不等於不可挑戰

$$
\boxed{
\text{Certificate}
\neq
\text{Final Truth}.
}
$$

certificate 只表示：

> 在指定 source、version、evidence、authority、procedure 下，這次運算如何形成。

---

# 53. Appeal 可以改變 Legal Result

若：

$$
K_L^{(1)}
$$

被 appeal，

後續可形成：

$$
K_L^{(2)}.
$$

所以：

$$
\boxed{
\text{Legal Result}
\text{ is versionable and reviewable}.
}
$$

---

# 54. Review 不等於 Recompute

有些 appeal 不是：

> 再跑同一個 function。

而是：

- 新 evidence；
- higher authority；
- different legal interpretation；
- procedural error correction；
- constitutional review。

因此：

$$
\boxed{
\text{Appeal}
\neq
\text{Same Algorithm Twice}.
}
$$

---

# 55. HumanDecisionRequired 不是 AI Failure

如果 law intentionally requires authorised human / institutional judgment：

$$
\boxed{
\mathsf{HumanDecisionRequired}
}
$$

可以是：

$$
\boxed{
\text{successful legal analysis result}.
}
$$

不是 system failure。

---

# 56. Normative Completeness 不應被假設

對某些 query：

$$
\operatorname{LawEval}(q)
=
\mathsf{RuleGap}
$$

可能是誠實結果。

法律系統不能為了「永遠回答」而 hallucinate rule。

---

# 57. Rule Gap 與 Discretion 也不同

$$
\boxed{
\mathsf{RuleGap}
\neq
\mathsf{Discretion}.
}
$$

Discretion 表示法律有意授權選擇。

Rule gap 表示規範本身沒有給足規則。

---

# 58. Underdetermined 與 Discretion 也不同

$$
\boxed{
\mathsf{Underdetermined}
\neq
\mathsf{Discretionary}.
}
$$

前者可能是 evidence / ontology 不足；

後者是制度授權的決策空間。

---

# 59. Violation 不等於 Impossibility

如果：

$$
[OBL]p
$$

但主體沒有履行 $p$，

表示：

$$
\mathsf{Violation}.
$$

不代表：

$$
p
$$

在邏輯上不可能。

所以：

$$
\boxed{
\text{Norm Violation}
\neq
\text{Logical Contradiction}.
}
$$

---

# 60. 違反規範可以觸發 Reparative Norm

LegalRuleML 的程序／違規建模方向允許：

$$
\mathsf{Violation}(r_1)
\Rightarrow
[OBL]q.
$$

例如原 obligation 失敗後觸發：

- compensation；
- correction；
- notice；
- penalty；
- remedial action。

因此 legal runtime 不是一次性 decision tree，

而可以形成：

$$
\boxed{
\text{normative state transition}.
}
$$

---

# 61. Normative State Machine

本文提出：

$$
\boxed{
\Sigma_L(t)
=
(
\text{active obligations},
\text{permissions},
\text{prohibitions},
\text{powers},
\text{violations},
\text{remedies}
).
}
$$

事件：

$$
e_t
$$

使：

$$
\Sigma_L(t)
\rightarrow
\Sigma_L(t+1).
$$

---

# 62. Obligation 有生命週期

一項 obligation 可以：

```text
CREATED
ACTIVE
SATISFIED
VIOLATED
WAIVED
EXPIRED
REMEDIED
DISPUTED
```

因此：

$$
\boxed{
\text{Obligation}
\neq
\text{Static Boolean}.
}
$$

---

# 63. Permission 也可能有 Scope

$$
\mathsf{Permission}
=
(
\text{subject},
\text{action},
\text{object},
\text{scope},
\text{time},
\text{condition},
\text{authority}
).
$$

所以：

$$
\boxed{
\text{Permission}
\neq
\text{Global Capability Token}.
}
$$

---

# 64. Prohibition 也可能有 Exception

$$
[FOR]p
$$

可以被：

$$
\mathsf{Exception}(e)
$$

在合法條件下 defeat。

因此：

$$
\boxed{
\text{Prohibition}
\neq
\text{Unconditional Forever Rule}.
}
$$

---

# 65. Power-Conferring Rule

法律不只說：

> 可以／不可以做某件事。

還可能賦予：

> 做某個法律行為會產生新的法律狀態。

例如：

$$
\mathsf{ValidDelegate}(A,B,o)
$$

可以創造：

$$
\mathsf{Authority}(B,o).
$$

所以：

$$
\boxed{
\text{Legal Power}
\neq
\text{Ordinary Permission}.
}
$$

---

# 66. Legal Power 對 AI 特別重要

因為 AI Agent 常被：

- delegate；
- revoke；
- limit；
- fork；
- rotate keys。

Runtime 必須知道：

$$
\boxed{
\text{who has legal power to change another agent's normative state}.
}
$$

---

# 67. No Compensation Across Hard Gates

分域憲章已指出高風險操作可能需要：

- identity；
- role；
- conflict-of-interest；
- budget；
- authority；
- audit。

若 authority gate 失敗，

不能因：

> model confidence 很高

就補償。

所以：

$$
\boxed{
\text{Hard Legal Failure}
\text{ is non-compensatory}.
}
$$

---

# 68. Legal Confidence 不是 Legal Authority

$$
\boxed{
\text{Confidence}=0.99
\not\Rightarrow
\text{Authorized}.
}
$$

同理：

$$
\text{model uncertainty}
$$

也不等於法律不存在。

---

# 69. AI Prediction 與 Legal Conclusion 分離

模型可以預測：

> 法官 83% 可能允許。

但：

$$
\boxed{
\text{Prediction}
\neq
\text{Legal Decision}.
}
$$

prediction 可以作 evidence / analytics，

不能偷換 normative authority。

---

# 70. Runtime 的雙輸出層

本文建議：

## Layer A — Legal Analysis

輸出：

$$
\mathfrak R_L.
$$

## Layer B — Operational Gate

輸出：

$$
\pi_q(\mathfrak R_L).
$$

這使法律 reasoning 與實際執行控制分離。

---

# 71. Gate Policy 也要版本化

$$
\pi_q^{(\nu)}
$$

可能更新。

因此：

$$
\boxed{
\text{same legal analysis}
+
\text{different execution policy}
}
$$

可能產生不同 operational result。

必須保留：

- policy version；
- authority；
- purpose。

---

# 72. Example：Hotel Booking Agent

query：

```text
Agent A
role = travel_agent
action = book_hotel
budget = 300
delegation = valid
```

可能：

```text
N = PERMITTED
K = SUFFICIENT
P = READY
A = DELEGATED
V = CURRENT
C = CLEAR
```

最後：

$$
\pi_q
=
\mathsf{Execute}.
$$

---

# 73. Example：證據不足

同一 query，

但 delegation certificate 找不到：

```text
N = NO_SUBSTANTIVE_CONCLUSION
K = INSUFFICIENT
P = NOT_READY
A = AUTHORITY_UNKNOWN
```

最後：

$$
\pi_q
=
\mathsf{Escalate}
$$

或：

$$
\mathsf{Block}
$$

取決於 risk policy。

但法律本體不是：

$$
\mathsf{Forbidden}.
$$

---

# 74. Example：法律禁止

若法規明確：

$$
[FOR]\mathsf{BookHotel}(A)
$$

則：

```text
N = FORBIDDEN
K = SUFFICIENT
P = READY
A = AUTHORIZED_TO_ENFORCE
```

這才是 substantive prohibition。

---

# 75. Example：需要裁量

若規則要求：

> 若特殊公共利益成立，可由 authorised officer 批准例外。

則：

```text
N = NO_SUBSTANTIVE_CONCLUSION
A = APPROVAL_REQUIRED
P = READY_FOR_DISCRETION
C = EXCEPTION_CANDIDATE
```

並附：

$$
\mathfrak D_C.
$$

---

# 76. Example：規則衝突

若：

$$
r_1\Rightarrow[PER]p,
$$

$$
r_2\Rightarrow[FOR]p,
$$

且沒有可解決 priority：

```text
C = CONFLICT_UNRESOLVED
N = NO_SUBSTANTIVE_CONCLUSION
```

輸出：

$$
\mathsf{ReviewRequired}.
$$

---

# 77. AI Legal Runtime 的最低 API 改寫

ALD-01 的：

```text
permission.check
```

在本篇應變成：

```text
permission.evaluate
obligation.evaluate
prohibition.evaluate
power.evaluate
conflict.resolve
exception.trace
discretion.package
failure.explain
certificate.issue
review.route
```

---

# 78. Legal Explain Surface

`decision.explain` 至少回答：

- applicable norms；
- non-applicable norms；
- facts used；
- evidence status；
- exceptions；
- priority rules；
- authority；
- procedure；
- version；
- review。

而不是只生成一篇流暢自然語言。

---

# 79. Explanation 也必須 Type-Safe

$$
\boxed{
\text{Explanation}
\neq
\text{Rationalisation}.
}
$$

如果 system 先得 answer 再編理由，

就不是 legal certificate。

---

# 80. Certificate-First Architecture

較安全流程：

```text
typed query
-> source resolution
-> facts/evidence
-> norm applicability
-> defeasibility
-> authority
-> procedure
-> typed result
-> certificate
-> human-readable explanation
```

而不是：

```text
LLM answer
-> plausible citation
```

---

# 81. ALD-03 的十二個核心非等價

$$
\boxed{
\mathsf{Forbidden}
\neq
\mathsf{Unknown}
}
$$

$$
\boxed{
\mathsf{EvidenceMissing}
\neq
\mathsf{Forbidden}
}
$$

$$
\boxed{
\mathsf{JurisdictionMismatch}
\neq
\mathsf{Allowed}
}
$$

$$
\boxed{
\text{Silence}
\neq
\text{Strong Permission}
}
$$

$$
\boxed{
\mathsf{Permitted}
\neq
\mathsf{ExecutableNow}
}
$$

$$
\boxed{
\text{Exception}
\neq
\text{Conflict}
}
$$

$$
\boxed{
\text{Discretion}
\neq
\text{Randomness}
}
$$

$$
\boxed{
\mathsf{RuleGap}
\neq
\mathsf{Discretion}
}
$$

$$
\boxed{
\text{Violation}
\neq
\text{Logical Contradiction}
}
$$

$$
\boxed{
\text{Legal Power}
\neq
\text{Permission}
}
$$

$$
\boxed{
\text{Prediction}
\neq
\text{Legal Decision}
}
$$

$$
\boxed{
\text{Certificate}
\neq
\text{Final Truth}
}
$$

---

# 82. 七個工程測試

## 82.1 Boolean Collapse Test

將至少十種 failure 都輸入舊 `false` API。

新版必須能逐一分型。

## 82.2 Weak / Strong Permission Test

沒有 prohibition 與 explicit licence 兩個案例不得輸出相同 proof state。

## 82.3 Exception Priority Test

base rule 與 exception 同時適用時，必須記錄 override path。

## 82.4 Discretion Preservation Test

有 authorised discretion 的規則不得被 AI 自動填成 deterministic answer。

## 82.5 Technical Failure Test

database outage 不得輸出 `Forbidden`。

## 82.6 Appeal Version Test

一審與覆核結果都要保留 certificate lineage。

## 82.7 Gate Projection Test

同一 $\mathfrak R_L$ 在低風險／高風險 query 下可以投影成不同 operational gate，但 underlying legal result 必須相同。

---

# 83. 可反駁點

## 83.1 Type Explosion

如果輸出型別太多，Runtime 可能難以實作。

因此可以提供 domain-specific projection，但 canonical result 不應因此消失。

## 83.2 Deontic Logic Limitation

LegalRuleML / deontic logic 並不能解決全部法律推理。本文只借其 normative typing、defeasibility、temporality 等結構。

## 83.3 Discretion Encoding Risk

即使建立 Discretion Capsule，也可能漏掉 tacit institutional practice。需要保留 human / institutional review。

## 83.4 Certificate Overtrust

certificate 只能證明 process / source path，不自動證明 legal interpretation 最終正確。

## 83.5 Computational Cost

完整 proof-carrying result 比 Boolean 慢，但高風險法律域中可解釋性與可申訴性可能值得成本。

---

# 84. 與下一篇的接口

下一篇：

## ALD-04｜快法律與慢憲法：AI 時代的版本化規範與更新速度分層

ALD-03 已建立：

- rule version；
- validity；
- appeal；
- authority；
- typed failure。

因此下一篇將處理：

$$
\boxed{
\tau_{\mathrm{constitution}}
\gg
\tau_{\mathrm{law}}
\gg
\tau_{\mathrm{operation}}
\gtrsim
\tau_{\mathrm{protocol}}.
}
$$

並研究：

- fast patch；
- slow legitimacy；
- emergency rule；
- sunset；
- backward compatibility；
- certificate invalidation；
- constitutional hard constraints；
- AI-speed events vs human political review。

---

# 85. 結論

法律系統最危險的工程偷換之一，是把：

> 「我現在無法合法得出可以」

縮成：

> 「法律禁止」。

另一個同樣危險的偷換，是把：

> 「我沒有找到禁止」

縮成：

> 「法律明確允許」。

因此成熟 AI Legal Domain 必須從：

```text
true / false
```

升級為：

$$
\boxed{
\text{Typed Normative Result}
+
\text{Evidence State}
+
\text{Procedure State}
+
\text{Authority State}
+
\text{Version}
+
\text{Defeasibility}
+
\text{Certificate}
+
\text{Review}.
}
$$

本文最終把法律 Runtime 的核心寫成：

$$
\boxed{
\operatorname{LawEval}
:
\mathcal Q_L
\rightharpoonup
\mathcal R_L
\sqcup
\mathcal F_L.
}
$$

如果實際機器最後需要一個簡單 action gate，

再做：

$$
\boxed{
\pi_q:
\mathfrak R_L
\rightarrow
\{
\mathsf{Execute},
\mathsf{Block},
\mathsf{Escalate}
\}.
}
$$

所以：

$$
\boxed{
\text{Boolean is allowed at the edge;}
}
$$

$$
\boxed{
\text{Boolean must not become the ontology of law.}
}
$$

中文最後一句：

$$
\boxed{
\text{法律可以最後給機器一個「做／不做」，}
}
$$

$$
\boxed{
\text{但法律本身絕不能只剩下一個「是／否」。}
}
$$

---

# 參考文獻

1. OASIS. *LegalRuleML Core Specification Version 1.0*. OASIS Standard, 30 August 2021.
2. OASIS LegalRuleML Technical Committee. *Charter*.
3. OECD. “Consultation on the digital provision of law: Towards a shared reference framework for Law as Code.” 2026.
4. Catala. *Conditional Definitions and Exceptions* and *General Questions*, current documentation accessed 2026.
5. Neo.K × Aletheia. 《ALD-01｜AI 法律域：從 Law as Code 到機器原生規範 Runtime》v0.1, 2026.
6. Neo.K × Aletheia. 《ALD-02｜載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則》v0.1, 2026.
7. Neo.K. 《分域憲章：結構域、概念身份與角色型別系統》v0.1, 2026.
8. Neo.K. 《分域算子本體論：從萬物皆算子到合法作用》v0.1, 2026.
9. Neo.K. 《分域證書化理論工程：混合型理論的概念提取、接口重構與認識狀態管理》v0.1, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- LawEval 使用 partial function，不假定全部 query 有定義
- canonical legal result 使用多軸 typed object，不壓成 Boolean
- `Execute / Block / Escalate` 被定位為目的限定 decision projection
- `Forbidden` 與 `Unknown / EvidenceMissing / JurisdictionMismatch / TechnicalError` 明確分型
- permission、obligation、prohibition、power 明確分型
- exception 與 conflict 明確分離
- discretion 不被自動填成 deterministic answer
- Discretion Capsule 明確保存 decision space、authority、mandatory / forbidden considerations 與 review
- success / failure 皆可產生 certificate
- certificate 不等於 final truth
- appeal 不等於 simple recomputation
