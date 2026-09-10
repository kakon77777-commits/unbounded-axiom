---
title: "GACEI-04｜對抗記憶基底：SEDB 特化版與軟體免疫記憶"
title_en: "GACEI-04 | Adversarial Memory Substrate: A Specialized SEDB Profile and Software Immune Memory"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-04"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 對抗記憶 / SEDB 特化 / 軟體工程知識基底"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "GACEI-02 MSSP 的對偶 v0.1"
  - "GACEI-03 局部攻擊抽象論 v0.1"
---

# GACEI-04｜對抗記憶基底
## SEDB 特化版與軟體免疫記憶

**英文題名：** Adversarial Memory Substrate: A Specialized SEDB Profile and Software Immune Memory

---

## 摘要

GACEI-03 已將一次性局部反例從 Concrete Witness、Typed Attack Instance、Parameterized Attack Template、Attack Family，逐步提升到 Transfer-Validated Reusable Operator。這解決了「什麼才算真正學會一個 attack」的語義問題，但尚未回答另一個工程問題：這些攻擊知識應如何被長期保存、版本化、去重、查詢、關聯、晉級、失效、重新驗證，並在未來專案中以低成本重新具體化？

本文提出「對抗記憶基底」（Adversarial Memory Substrate, AMS），並建議以 SEDB 的稀疏欄位、可擴展 schema、來源與狀態分離思想建立一個特化 profile。其目的不是建立「漏洞名單」或「攻擊腳本倉庫」，而是保存：

$$
\boxed{
\text{Failure Mechanism Knowledge}
}
$$

也就是經過型別化、抽象化、證據綁定、條件化與版本化後，可在授權測試環境中重新辨識、生成與驗證的軟體失敗機制。

本文將對抗記憶狀態記為：

$$
\boxed{
\mathfrak M_A(t)
=
\left(
N_t,
R_t,
V_t,
H_t,
P_t,
S_t,
Q_t,
C_t
\right),
}
$$

其中：

- $N_t$：attack knowledge nodes；
- $R_t$：typed relations；
- $V_t$：version / condition fibers；
- $H_t$：history and provenance；
- $P_t$：promotion / lifecycle state；
- $S_t$：structural signatures；
- $Q_t$：quality / confidence / discrimination evidence；
- $C_t$：cost and coverage metadata。

本文特別區分：

$$
\boxed{
\text{Attack Memory}
\neq
\text{Attack Planner}
\neq
\text{Attack Executor}.
}
$$

AMS 只回答：

> 我們以前學會了什麼、在什麼條件下成立、現在是否仍有效、與哪些結構或 attack 有關、值得如何被重新取回？

它不自行決定：

> 現在一定要執行哪些 attack？

全域 campaign selection 仍由 GACEI-05/06 的組合與壓縮層、風險目標、授權條件與算力預算共同決定。

本文提出第一版 adversarial memory record：

$$
m_a
=
\left\langle
id,
kind,
maturity,
family,
preconditions,
targets,
operator,
observations,
validator,
recovery,
coverage,
cost,
provenance,
history,
relations,
version,
status
\right\rangle.
$$

其中 attack identity 不等於 script identity。不同實作腳本可以實現同一 attack semantics，同一段 script 在不同 invariant、role、scope 或 validator 下也可以代表不同 attack。因此 AMS 使用 semantic identity、artifact identity 與 instance identity 三層分離。

本文進一步提出 attack memory lifecycle：

$$
\boxed{
\text{OBSERVED}
\rightarrow
\text{REPRODUCED}
\rightarrow
\text{TYPED}
\rightarrow
\text{ABSTRACTED}
\rightarrow
\text{TRANSFER\_TESTED}
\rightarrow
\text{PROMOTED}
\rightarrow
\text{ACTIVE}
}
$$

並允許：

$$
\text{ACTIVE}
\rightarrow
\{
\text{SUPERSEDED},
\text{DEPRECATED},
\text{RETIRED},
\text{QUARANTINED}
\}.
$$

「用過就學會」因此不表示資料永遠有效，而表示 attack knowledge 的發現成本被轉化為可重用資本，之後只需支付較低的匹配、具體化與必要重新驗證成本。

本文並提出「軟體免疫記憶」的有限類比：已知 attack family 類似免疫記憶中的已知反應模式，未來系統遇到結構相似風險時，可先做低成本 structural recognition；若遇到 corpus 外的 residual gap，再投入高階 AI 進行新 attack synthesis。本文不把軟體系統等同生物免疫，也不宣稱所有未知失敗都能被已知 attack family 推導。

最終，AMS 的目標是使：

$$
\boxed{
\text{Known Failure}
\rightarrow
\text{Cheap Recognition}
}
$$

以及：

$$
\boxed{
\text{Unknown Failure}
\rightarrow
\text{Expensive Reasoning}.
}
$$

從而避免前沿 AI 把大量算力浪費在已知 attack 的重複發現，並讓新的工程經驗可以持續累積成跨專案的全域對抗知識基底。

**關鍵詞：** Adversarial Memory Substrate、SEDB、軟體免疫記憶、Attack Memory、Attack Identity、Provenance、Promotion、Supersession、Structural Retrieval、Typed Relations、全域對抗計算、AI 工程智能

---

# 0. 研究定位與安全範圍

本文中的「攻擊記憶」只保存用於：

- 授權軟體測試；
- synthetic fixture；
- isolated sandbox；
- 可恢復副本；
- 內部品質驗證；
- 防禦性工程研究；

的失敗機制知識。

本文不把：

$$
\boxed{
\text{Knowledge Reuse}
}
$$

理解成：

$$
\boxed{
\text{Unauthorized Exploit Reuse}.
}
$$

若某些 attack knowledge 涉及真實外部系統、未公開第三方缺陷、私人資料、憑證或可造成現實濫用的細節，AMS 應保存抽象 failure mechanism、必要治理 metadata 與最小 defensive evidence，而不是保存可直接對外濫用的操作資料。

---

# 1. 為什麼需要專門的對抗記憶？

## 1.1 一般測試檔不等於工程記憶

傳統 repository 可能已經保存：

- unit test；
- regression test；
- integration test；
- bug report；
- incident note；
- fixture；
- issue；
- commit history。

這些都很重要。

但它們通常回答：

> 某個具體版本以前發生過什麼？

不一定回答：

> 這個失敗背後的可重用機制是什麼？

因此：

$$
\boxed{
\text{Test Archive}
\neq
\text{Failure Mechanism Memory}.
}
$$

---

## 1.2 AI 最容易浪費在重新發現

若 AI 在專案 $S_1$ 已發現：

$$
a
$$

的 failure mechanism，

到了：

$$
S_2
$$

又從零推理一次，

則：

$$
C_{\mathrm{discover}}
$$

被重複支付。

若：

$$
a
$$

已被 promotion 到 reusable memory，

未來只需要：

$$
C_{\mathrm{retrieve}}
+
C_{\mathrm{match}}
+
C_{\mathrm{instantiate}}
+
C_{\mathrm{revalidate}}.
$$

理想條件：

$$
C_{\mathrm{retrieve}}
+
C_{\mathrm{match}}
+
C_{\mathrm{instantiate}}
+
C_{\mathrm{revalidate}}
\ll
C_{\mathrm{discover}}.
$$

---

# 2. SEDB 為什麼適合作為特化基底？

本文不重新定義完整 SEDB。

本文只使用幾個適合 attack memory 的抽象特性：

1. sparse fields；
2. 可擴展 schema；
3. 不強迫所有 record 擁有全部欄位；
4. identity、evidence、status、projection 可分離；
5. 關係可顯式化；
6. 歷史與當前狀態可同時保存；
7. derived view 不必等於 canonical source。

因此 attack memory 很適合表示成：

$$
\boxed{
\text{Sparse Typed Knowledge Records}.
}
$$

而不是一個巨大固定欄位表。

---

# 3. AMS 的總體狀態

本文定義：

$$
\boxed{
\mathfrak M_A(t)
=
\left(
N_t,
R_t,
V_t,
H_t,
P_t,
S_t,
Q_t,
C_t
\right).
}
$$

---

## 3.1 Node $N_t$

保存：

- witness；
- instance；
- template；
- family；
- macro；
- validator profile；
- recovery profile；
- structural signature。

---

## 3.2 Relation $R_t$

保存 typed relations。

---

## 3.3 Version $V_t$

保存：

- project version；
- architecture version；
- template version；
- validator version；
- condition fiber；
- platform；
- authorization profile。

---

## 3.4 History $H_t$

保存：

- discovery；
- reproduction；
- transfer；
- miss；
- false positive；
- false applicability；
- supersession；
- revalidation。

---

## 3.5 Promotion $P_t$

保存 maturity 與 lifecycle state。

---

## 3.6 Structural Signature $S_t$

保存：

> attack 適用的結構條件，而不是只保存文字描述。

---

## 3.7 Quality $Q_t$

保存：

- mechanism fidelity；
- discriminative evidence；
- applicability precision；
- transfer rate；
- uncertainty。

---

## 3.8 Cost / Coverage $C_t$

保存：

- compute；
- runtime；
- human review；
- sandbox；
- coverage signature；
- expected information gain。

---

# 4. 三層 Identity

## 4.1 Semantic Attack Identity

定義：

$$
ID_{\mathrm{sem}}(a).
$$

它表示：

> 這個 attack 在語義上測的是什麼 failure mechanism？

---

## 4.2 Artifact Identity

定義：

$$
ID_{\mathrm{artifact}}(x)
=
Hash(bytes(x)).
$$

它表示：

> 這個具體 script、fixture、validator 或 report 是哪一份 bytes？

---

## 4.3 Instance Identity

定義：

$$
ID_{\mathrm{inst}}
=
Hash
(
ID_{\mathrm{sem}},
target,
baseline,
conditions,
time
).
$$

它表示：

> 這一次 attack execution 是哪個具體事件？

---

## 4.4 三者不能混淆

因此：

$$
\boxed{
ID_{\mathrm{sem}}
\neq
ID_{\mathrm{artifact}}
\neq
ID_{\mathrm{inst}}.
}
$$

---

# 5. 第一版 Canonical Record

本文提出：

```yaml
attack_record:
  semantic_id:
  kind:
  maturity:
  family:
  title:
  description:
  preconditions:
  target_invariants:
  target_structure_types:
  abstract_operator:
  observation_contract:
  validator_contract:
  recovery_contract:
  coverage_signature:
  cost_profile:
  condition_fibers:
  provenance:
  first_witness:
  reproduction_history:
  transfer_history:
  false_positive_history:
  false_applicability_history:
  relations:
  supersedes:
  superseded_by:
  status:
  last_revalidated:
```

這只是第一版 canonical logical shape，不要求所有後端直接使用 YAML。

---

# 6. Sparse Field 原則

不同 attack 不需要全部欄位。

例如：

$$
a_1
$$

可能沒有 recovery：

$$
R(a_1)=\text{DiscardSandbox}.
$$

另一個：

$$
a_2
$$

需要 explicit rollback receipt。

因此：

$$
\boxed{
\text{Missing Field}
\neq
\text{Null}
\neq
\text{Not Applicable}
\neq
\text{Unknown}.
}
$$

SEDB 類稀疏模型的價值就在於不強迫它們被壓成同一狀態。

---

# 7. Attack Maturity

承接 GACEI-03：

$$
W_0
\rightarrow
W_1
\rightarrow
W_2
\rightarrow
W_3
\rightarrow
W_4.
$$

AMS 應保存：

$$
maturity
$$

而不是只保存：

$$
\text{active}=\text{true}.
$$

---

## 7.1 Witness 與 promoted operator 的查詢權重不同

若：

$$
maturity=W_0,
$$

只代表：

> 曾觀察過。

若：

$$
maturity=W_4,
$$

才代表：

> 已有 transfer evidence，可優先進入 structural matching。

---

# 8. Lifecycle

本文定義：

$$
\boxed{
\mathcal L_A
=
\{
OBSERVED,
REPRODUCED,
TYPED,
ABSTRACTED,
TRANSFER\_TESTED,
PROMOTED,
ACTIVE,
SUPERSEDED,
DEPRECATED,
RETIRED,
QUARANTINED
\}.
}
$$

---

## 8.1 QUARANTINED

若 attack：

- provenance 不完整；
- validator 被證明錯；
- false applicability 過高；
- 現有版本語義不清；
- transfer evidence 被撤回；

可以：

$$
status=\text{QUARANTINED}.
$$

它不被刪除，但不再自動推薦。

---

# 9. Typed Relations

AMS 不應只依 embedding similarity。

本文提出：

$$
R_A
\subseteq
N_A\times\mathcal T_R\times N_A.
$$

---

## 9.1 第一版 relation types

```text
GENERALIZES
SPECIALIZES
OVERLAPS
REQUIRES
CONFLICTS
MASKS
SYNERGIZES_WITH
SUPERSEDES
SUPERSEDED_BY
VALIDATED_BY
FALSIFIED_BY
OBSERVED_IN
TRANSFERRED_TO
DERIVED_FROM
IMPLEMENTS
ANALOGOUS_TO
NOT_EQUIVALENT_TO
```

---

## 9.2 Similarity 只能產生 candidate

若：

$$
sim(a_i,a_j)\approx1,
$$

只能：

$$
\operatorname{RelationCandidate}(a_i,a_j).
$$

不能自動：

$$
a_i
\equiv
a_j.
$$

---

# 10. Structural Signature

## 10.1 為什麼文字關鍵字不夠？

attack title：

> stale state

可能在很多專案都出現。

但真正 applicability 取決於：

- state ownership；
- replication；
- cache；
- version binding；
- retry；
- lifecycle。

因此：

$$
\boxed{
\text{Keyword Match}
\neq
\text{Structural Match}.
}
$$

---

## 10.2 Signature

可定義：

$$
\sigma_a
=
\left(
R_o,
T_s,
E_s,
B_s,
X_s,
I_s,
\Theta_s
\right),
$$

其中：

- $R_o$：required roles；
- $T_s$：structure types；
- $E_s$：required relation shape；
- $B_s$：boundary pattern；
- $X_s$：state requirements；
- $I_s$：invariant classes；
- $\Theta_s$：condition requirements。

---

# 11. Structural Retrieval

對新專案：

$$
S,
$$

先抽出：

$$
\sigma_S.
$$

再：

$$
Match(a,S)
=
g(\sigma_a,\sigma_S).
$$

---

## 11.1 Match 不應只回布林值

更適合：

$$
Match(a,S)
=
\left(
p_{\mathrm{app}},
evidence,
missing,
conflicts
\right).
$$

其中：

$$
p_{\mathrm{app}}
$$

只是 applicability confidence，不是 attack success probability。

---

# 12. Retrieval 分層

本文提出四層 retrieval。

## 12.1 Exact Retrieval

依：

- semantic id；
- artifact digest；
- known project；
- exact version。

---

## 12.2 Structural Retrieval

依：

$$
\sigma_a.
$$

---

## 12.3 Relational Retrieval

依 relation graph：

$$
a
\rightarrow
GENERALIZES
\rightarrow
F.
$$

---

## 12.4 Residual Retrieval

若已知 coverage：

$$
\rho_A,
$$

只取：

> 對 residual gap 有幫助的 attack。

---

# 13. Known / Unknown 分流

AMS 的核心成本原則：

$$
\boxed{
\text{Known}
\rightarrow
\text{Retrieve Cheaply},
}
$$

$$
\boxed{
\text{Unknown}
\rightarrow
\text{Reason Expensively}.
}
$$

因此高階 AI 不應先自由 brainstorm 一百個 attack，再去資料庫看是否重複。

更合理：

$$
\text{Structure Parse}
\rightarrow
\text{Retrieve Known}
\rightarrow
\text{Coverage Map}
\rightarrow
\text{Residual Gap}
\rightarrow
\text{Novel Synthesis}.
$$

---

# 14. Promotion Gate

本文提出：

$$
G_P(a)
=
R(a)
\land
T(a)
\land
D(a)
\land
S(a)
\land
H(a).
$$

其中：

- $R$：reproduced；
- $T$：typed；
- $D$：discriminative；
- $S$：structurally abstracted；
- $H$：history / provenance complete。

若：

$$
G_P(a)=1,
$$

可 promotion 到：

$$
W_2/W_3.
$$

若再通過：

$$
X(a)=\text{Transfer Validated},
$$

才升：

$$
W_4.
$$

---

# 15. Promotion 不是 Trust Forever

即使：

$$
a\in W_4,
$$

若：

$$
version
\rightarrow
version',
$$

且核心 architecture 改變，

應：

$$
a
\rightarrow
\text{Revalidation Required}.
$$

所以：

$$
\boxed{
\text{Promoted}
\neq
\text{Permanently Valid}.
}
$$

---

# 16. Supersession

若新 template：

$$
a_2
$$

修正：

$$
a_1
$$

的 applicability 或 validator，

建立：

$$
a_2
\overset{\mathrm{SUPERSEDES}}{\longrightarrow}
a_1.
$$

舊 record 不刪。

因為歷史上：

$$
a_1
$$

曾經是當時的有效知識狀態。

---

# 17. Immutability 與 Current Projection

本文建議區分：

$$
\boxed{
\text{Event / History Layer}
}
$$

與：

$$
\boxed{
\text{Current Projection Layer}.
}
$$

歷史層保存：

- promotion event；
- revalidation；
- failure；
- supersession；
- quarantine。

current projection 只回答：

> 現在 active 的 attack knowledge 是什麼？

因此：

$$
\text{Projection}
$$

可以重建，

而：

$$
\text{History}
$$

不可由 projection 完整替代。

---

# 18. Evidence Binding

每一個重要狀態改變都應攜帶：

$$
EvidenceBinding.
$$

例如 promotion：

```yaml
promotion:
  attack_id:
  from:
  to:
  evidence:
  reviewer_or_process:
  baseline_refs:
  validator_refs:
  transfer_refs:
  timestamp:
```

---

# 19. Provenance

attack memory 至少要知道：

$$
\boxed{
\text{Where did this knowledge come from?}
}
$$

因此 provenance 應保存：

- source project；
- source baseline；
- witness；
- discovering agent / process；
- validator；
- review；
- date；
- environment；
- authorization class。

---

# 20. History 不能只存命中

本文延續 GACEI-03：

$$
H_a
=
\left(
N_{\mathrm{hit}},
N_{\mathrm{miss}},
N_{\mathrm{false+}},
N_{\mathrm{not-applicable}},
N_{\mathrm{unknown}}
\right).
$$

---

## 20.1 為什麼 miss 很重要？

若：

$$
N_{\mathrm{hit}}=5
$$

但：

$$
N_{\mathrm{miss}}=100,
$$

attack 的 applicability 或效用可能被高估。

---

# 21. Cost Profile

每個 attack record 應保存：

$$
K(a)
=
\left(
k_c,
k_t,
k_u,
k_h,
k_r
\right),
$$

其中：

- $k_c$：compute；
- $k_t$：runtime；
- $k_u$：tool；
- $k_h$：human governance；
- $k_r$：execution risk / sandbox cost。

---

# 22. Coverage Profile

$$
C(a)
=
\left(
C_N,
C_R,
C_\Theta,
C_P,
C_V,
C_T
\right).
$$

這讓 campaign planner 可以問：

> 哪些 attacks 最適合補目前 coverage residual？

---

# 23. 軟體免疫記憶

## 23.1 類比的有限用途

傳統防毒或免疫系統的直覺：

$$
\text{Known Threat}
\rightarrow
\text{Faster Recognition}.
$$

AMS 也希望：

$$
\text{Known Failure Mechanism}
\rightarrow
\text{Faster Structural Recognition}.
$$

---

## 23.2 但不是 signature scanning

AMS 不只保存：

$$
\text{byte signature}.
$$

而是保存：

$$
\boxed{
\text{Typed Failure Mechanism}.
}
$$

所以更接近：

$$
\text{Pattern}
+
\text{Condition}
+
\text{Invariant}
+
\text{Validator}
+
\text{History}.
$$

---

## 23.3 未知仍然需要新推理

因此：

$$
\boxed{
\text{Immune Memory}
\neq
\text{Closed World}.
}
$$

已知 attack family 越多，不代表：

$$
\text{Unknown}=0.
$$

---

# 24. Attack Memory 與 Planner 必須分離

## 24.1 Memory

回答：

> 有哪些已知攻擊知識？

---

## 24.2 Planner

回答：

> 現在應該選哪些？

---

## 24.3 Executor

回答：

> 如何在 sandbox 中執行？

---

## 24.4 Validator

回答：

> 觀測到的結果支持什麼？

---

## 24.5 分離原則

$$
\boxed{
M
\neq
P
\neq
E
\neq
V.
}
$$

如果記憶層直接看到：

$$
a
$$

就自動執行，

則：

$$
\boxed{
\text{Knowledge}
\rightarrow
\text{Authority Escalation}.
}
$$

這是不允許的。

---

# 25. Authorization Boundary

attack record 可以被：

$$
\text{known}
$$

但不代表：

$$
\text{authorized}.
$$

執行前仍要求：

$$
Auth(a,S,t)=1.
$$

因此：

$$
\boxed{
\text{Known Attack}
\neq
\text{Executable Attack}.
}
$$

---

# 26. Query Model

對新系統：

$$
S,
$$

query 可以是：

```yaml
query:
  architecture_signature:
  target_invariants:
  residual_coverage:
  version:
  platform:
  authorization:
  max_cost:
  maturity_floor:
```

---

# 27. Retrieval Score

可以定義：

$$
Score(a\mid q)
=
w_sS
+
w_iI
+
w_rR
+
w_vV
+
w_cC
-
w_kK
-
w_fF.
$$

其中：

- $S$：structural fit；
- $I$：invariant relevance；
- $R$：relation relevance；
- $V$：version fit；
- $C$：coverage contribution；
- $K$：cost；
- $F$：false applicability penalty。

---

# 28. 不允許單一總分遮蔽理由

即使 planner 使用：

$$
Score,
$$

AMS 仍應回傳：

```yaml
match_explanation:
  structural_fit:
  invariant_fit:
  version_fit:
  missing_conditions:
  conflicts:
  coverage_gain:
  historical_quality:
  cost:
```

因此：

$$
\boxed{
\text{Ranking Score}
\neq
\text{Explanation}.
}
$$

---

# 29. De-duplication

## 29.1 Semantic duplicate

若兩個 attack：

$$
a_1,a_2
$$

有不同 artifact，

但：

$$
ID_{\mathrm{sem}}(a_1)
=
ID_{\mathrm{sem}}(a_2),
$$

可以建立：

$$
\text{IMPLEMENTS}
$$

關係，而不是保存兩個等級完全相同的 semantic node。

---

## 29.2 Overlap

若：

$$
a_1
$$

和：

$$
a_2
$$

只部分重疊，

則：

$$
OVERLAPS.
$$

不能強制 merge。

---

# 30. Canonicalization

attack semantic record 可 canonicalize：

$$
Canon(a)
=
Normalize
(
P,
I,
T_{\mathrm{sem}},
O,
V,
R,
C,
\Theta
).
$$

但：

$$
Canon(a_1)=Canon(a_2)
$$

才是 semantic duplicate candidate。

仍需處理：

- provenance；
- history；
- evidence；
- artifact variants。

---

# 31. Projection Views

AMS 可以建立不同 view。

## 31.1 Active Attack View

只看：

$$
ACTIVE.
$$

---

## 31.2 Family View

按：

$$
Attack Family.
$$

---

## 31.3 Architecture View

按：

$$
MSSP,
event-sourced,
browser-extension,
identity-runtime,
storage-runtime,
...
$$

分類。

---

## 31.4 Risk View

按：

- state；
- authority；
- boundary；
- temporal；
- recovery；
- validation。

---

# 32. Campaign Interface

AMS 對 planner 輸出：

$$
CandidateSet
=
\{
a_1,\ldots,a_k
\}.
$$

每一項至少帶：

- applicability；
- maturity；
- relation；
- coverage；
- cost；
- version；
- evidence quality；
- authorization need。

Planner 再決定：

$$
A_G^\ast.
$$

---

# 33. Residual Gap Interface

如果 AMS 找不到：

$$
a
$$

覆蓋某結構：

$$
g,
$$

應回：

$$
\boxed{
\text{NO\_KNOWN\_ATTACK}
}
$$

而不是：

$$
\boxed{
\text{SAFE}.
}
$$

這是非常重要的 epistemic discipline。

---

# 34. Unknown 不等於 Safe

因此：

$$
\boxed{
\text{No Known Attack}
\neq
\text{No Failure Mechanism}.
}
$$

這也是為什麼 GACEI-09 的創造／生成能力仍不可省略。

---

# 35. Learning Commit

新 attack：

$$
a_{\mathrm{new}}
$$

不能在第一次命中後直接：

$$
ACTIVE.
$$

流程：

$$
OBSERVED
\rightarrow
REPRODUCED
\rightarrow
TYPED
\rightarrow
ABSTRACTED
\rightarrow
TRANSFER\_TESTED
\rightarrow
PROMOTED.
$$

---

# 36. Memory Write Gate

AMS write 可以要求：

$$
WriteAllowed
=
Auth
\land
SchemaValid
\land
EvidenceBound
\land
VersionBound
\land
NoIdentityCollision.
$$

---

# 37. SEDB 特化版的邏輯 schema

第一版可分成：

```text
attack/
attack_family/
attack_template/
witness/
validator/
recovery_profile/
structural_signature/
coverage_profile/
cost_profile/
relation/
event/
projection/
```

這是 logical namespace，不要求實作一定使用同名 directory。

---

# 38. Event Types

可以包含：

```text
ATTACK_OBSERVED
ATTACK_REPRODUCED
ATTACK_TYPED
ATTACK_ABSTRACTED
ATTACK_TRANSFERRED
ATTACK_PROMOTED
ATTACK_REVALIDATED
ATTACK_FALSE_POSITIVE
ATTACK_NOT_APPLICABLE
ATTACK_SUPERSEDED
ATTACK_DEPRECATED
ATTACK_QUARANTINED
ATTACK_RETIRED
```

---

# 39. Current Projection

current attack state：

$$
State_t(a)
=
Fold
(
Events_{\le t}(a)
).
$$

這讓 history 保持 append-oriented，而 current view 可重建。

---

# 40. Revalidation Policy

不是每次 query 都重驗所有 attack。

可依：

$$
Revalidate(a)
=
f
(
VersionDelta,
ArchitectureDelta,
ValidatorDelta,
Age,
Risk,
UsageFrequency
).
$$

---

## 40.1 高風險 attack

高 risk family 可以較頻繁 revalidate。

---

## 40.2 Stable family

若：

- architecture stable；
- validator stable；
- transfer history strong；

可降低 revalidation 頻率。

---

# 41. Version Delta

定義：

$$
\Delta_V(a,S)
=
d
(
VersionContext(a),
VersionContext(S)
).
$$

若：

$$
\Delta_V>\tau,
$$

attack 不應自動具體化。

---

# 42. Memory Decay

本文不主張知識一定要物理刪除。

可以有：

$$
Priority_t(a)
=
Priority_0(a)e^{-\lambda t}
$$

作為 retrieval priority decay。

但若：

$$
Risk(a)
$$

極高，

可以降低：

$$
\lambda.
$$

這只是可選策略，不是唯一模型。

---

# 43. Memory Consolidation

如果多個 attack：

$$
a_1,\ldots,a_n
$$

反覆形成相同 macro，

可建立：

$$
m
=
\operatorname{Consolidate}
(a_1,\ldots,a_n).
$$

但原 witness/history 仍保留。

---

# 44. 反向展開能力

任何 distill 後 attack record 都應盡量支持：

$$
\boxed{
\text{Can Reconstruct Test Intent}.
}
$$

也就是：

> 新 AI 不看舊對話，只看 canonical attack record，能不能理解要測什麼、為什麼、何時適用、如何知道結果？

---

# 45. Memory Quality Benchmark

可測：

$$
Q_M
=
f
(
R,
T,
P,
F,
C,
X
).
$$

其中：

- $R$：retrieval precision；
- $T$：transfer success；
- $P$：applicability precision；
- $F$：false positive control；
- $C$：compression；
- $X$：reconstructability。

---

# 46. Compression 不應犧牲 Reconstruction

若：

$$
Compression\uparrow
$$

但：

$$
Reconstructability\downarrow,
$$

就不是好的 memory distillation。

因此：

$$
\boxed{
\text{Shortest Record}
\neq
\text{Best Memory}.
}
$$

---

# 47. AI 能力與 AMS

AMS 可以支援，但不能取代：

$$
\mathcal C_{\mathrm{GAC}}
=
(A,U,R,C,G,K,V,L,M).
$$

其中：

$$
M
$$

是 memory / learning，

但：

$$
C,G,K
$$

仍需要創造、生成、計算能力。

---

# 48. 多 Agent 共用記憶

若多個 AI：

$$
A_1,A_2,\ldots,A_n
$$

共用 AMS，

則：

$$
\boxed{
\text{Shared Memory}
\neq
\text{Shared Judgment}.
}
$$

不同 Agent 可以讀同一 attack record，

仍可能對：

- applicability；
- priority；
- release relevance；

有不同判斷。

---

# 49. 共享記憶的好處

可以降低：

$$
\text{Cross-Agent Rediscovery}.
$$

例如一個 Agent 已發現並 promotion：

$$
a,
$$

其他 Agent 不必：

> 我也重新想一次。

---

# 50. 共享記憶的風險

若錯誤 attack 被 promotion：

$$
a_{\mathrm{bad}},
$$

會造成：

$$
\text{Error Propagation}.
$$

因此：

$$
\boxed{
\text{Shared Memory Requires Stronger Provenance}.
}
$$

---

# 51. Quarantine 與回滾

如果：

$$
a
$$

被新 evidence 證明：

- validator wrong；
- applicability wrong；
- family merge wrong；

可以：

$$
a\rightarrow QUARANTINED.
$$

current projection 立即停止推薦。

歷史仍保留。

---

# 52. Attack Knowledge Debt

可以定義：

$$
D_A
=
D_{\mathrm{untyped}}
+
D_{\mathrm{unvalidated}}
+
D_{\mathrm{untransferred}}
+
D_{\mathrm{stale}}
+
D_{\mathrm{conflicted}}.
$$

這表示 attack corpus 不是越大越好。

---

# 53. Corpus Growth 與 Knowledge Growth 不同

若：

$$
|N_t|\uparrow
$$

但：

$$
D_A\uparrow
$$

可能只是資料膨脹。

因此：

$$
\boxed{
\text{More Attack Records}
\neq
\text{More Usable Attack Knowledge}.
}
$$

---

# 54. Attack Memory Coverage

定義：

$$
\boldsymbol\rho_M
=
\left(
\rho_{\mathrm{family}},
\rho_{\mathrm{structure}},
\rho_{\mathrm{condition}},
\rho_{\mathrm{version}},
\rho_{\mathrm{validator}},
\rho_{\mathrm{transfer}}
\right).
$$

---

# 55. Memory Coverage 也不是 Global Safety

即使：

$$
\boldsymbol\rho_M
$$

很高，

仍不能：

$$
\text{System Safe}.
$$

因為：

$$
\text{Unknown Attack Space}
$$

可能仍存在。

---

# 56. 軟體免疫記憶的學習循環

本文提出：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Reproduce}
\rightarrow
\text{Abstract}
\rightarrow
\text{Validate}
\rightarrow
\text{Promote}
\rightarrow
\text{Retrieve}
\rightarrow
\text{Instantiate}
\rightarrow
\text{Revalidate}
\rightarrow
\text{Update}.
}
$$

---

# 57. AMS 與 Global Campaign 的閉環

$$
\mathfrak M_A(t)
\rightarrow
\operatorname{Retrieve}
\rightarrow
A_{\mathrm{known}}
\rightarrow
\operatorname{Campaign}
\rightarrow
E_G
\rightarrow
A_{\mathrm{novel}}
\rightarrow
\operatorname{Abstract}
\rightarrow
\mathfrak M_A(t+1).
$$

這形成：

$$
\boxed{
\text{Adversarial Learning Loop}.
}
$$

---

# 58. 第一版執行流程

```text
INPUT
  project model S_hat
  adversarial memory M_A
  authorization Auth
  coverage residual G
  budget B

1. BUILD_QUERY
   Extract structure, invariants, versions, conditions, and residual gaps.

2. EXACT_RETRIEVE
   Recover exact historical matches if present.

3. STRUCTURAL_RETRIEVE
   Match reusable templates and families by typed structure.

4. FILTER
   Remove NotApplicable, stale, quarantined, unauthorized, or over-budget items.

5. EXPLAIN_MATCH
   Preserve why each attack was retrieved.

6. RETURN_KNOWN_SET
   Produce known attack candidates with maturity, coverage, cost, and evidence.

7. MAP_RESIDUAL
   Identify gaps not covered by known memory.

8. NOVEL_REASONING
   Send only residual gaps to high-capability synthesis.

9. EXECUTE_CAMPAIGN
   Run authorized bounded global campaign.

10. COLLECT_HISTORY
    Record hits, misses, false positives, NotApplicable, Unknown.

11. ABSTRACT_NOVEL
    Process new witnesses through GACEI-03 abstraction.

12. PROMOTION_GATE
    Promote only evidence-sufficient knowledge.

13. UPDATE_RELATIONS
    Add GENERALIZES, SPECIALIZES, OVERLAPS, SUPERSEDES, etc.

14. REBUILD_PROJECTION
    Refresh active views.

15. STOP
    Do not reinterpret "no known attack" as "safe".
```

---

# 59. 研究假說

## H1：AMS 可降低已知 attack 的重複推理成本

隨著：

$$
|K_A|\uparrow,
$$

對 matched attacks：

$$
C_{\mathrm{reasoning}}^{\mathrm{known}}
\downarrow
$$

應在部分專案族成立。

---

## H2：Structural retrieval 優於 keyword retrieval

對跨命名、跨語言、跨模組 layout：

$$
Precision_{\mathrm{struct}}
>
Precision_{\mathrm{text}}
$$

應在 attack applicability 上成立。

---

## H3：History-complete memory 可降低錯誤高估

若保存：

$$
\text{hit}+\text{miss}+\text{false}+\text{NA}+\text{unknown},
$$

其 utility calibration 應優於只保存 successful hits 的資料庫。

---

## H4：Promotion / quarantine 可提高 corpus quality

有 lifecycle gate 的 AMS 應比：

> 所有 attack 一律 active

具有較低 false applicability。

---

## H5：Shared AMS 可降低多 Agent rediscovery

多 Agent 使用同一 promotion memory 時：

$$
C_{\mathrm{duplicate-discovery}}
\downarrow
$$

應成立。

---

# 60. Benchmark

可建立三種 memory backend。

## A：Raw Test Archive

只保存 scripts。

## B：Textual Attack Notes

保存自然語言摘要。

## C：SEDB-style AMS

保存：

- typed semantics；
- structural signature；
- lifecycle；
- relations；
- history；
- version；
- coverage；
- cost。

給 AI 一組表面不同但結構相似的新系統。

測：

$$
\text{Retrieval Precision},
$$

$$
\text{Applicability Precision},
$$

$$
\text{Transfer Recall},
$$

$$
\text{Reasoning Cost},
$$

$$
\text{Time-to-Campaign},
$$

$$
\text{False Positive},
$$

$$
\text{Novel Gap Detection}.
$$

---

# 61. 本文非主張

本文不主張：

1. SEDB 是唯一可用 attack memory backend；
2. 所有 attack knowledge 都適合公開；
3. 所有 attack records 都應永久 active；
4. embedding similarity 可以代替 structural identity；
5. semantic identity 可以完全自動判定；
6. historical hit rate 等於 attack value；
7. attack memory coverage 等於軟體安全性；
8. promoted attack 永遠不需 revalidate；
9. shared memory 等於 shared judgment；
10. attack memory 可以直接授權 attack execution；
11. No Known Attack 等於 Safe；
12. 所有未知 attack 都能由已知 family 推導；
13. 所有 attack family 都能無損去重；
14. 所有版本都應保留同一 attack priority；
15. 所有防禦性測試知識都應保存可外部濫用的操作細節；
16. AMS 可以取代高階 AI 的創造與生成能力。

本文主張的是：

$$
\boxed{
\text{對抗知識必須被型別化、版本化、證據化、關聯化與生命週期化，}
}
$$

以及：

$$
\boxed{
\text{記憶應降低已知問題的認知成本，而不是自動擴大 attack authority。}
}
$$

---

# 62. 與前文的關係

GACEI-03 回答：

$$
\boxed{
\text{What should be learned?}
}
$$

本文回答：

$$
\boxed{
\text{How should that learning persist?}
}
$$

下一篇 GACEI-05 將回答：

$$
\boxed{
\text{How should remembered local attacks interact and compose?}
}
$$

---

# 63. 下一篇：全域攻擊組合代數

GACEI-05 將把：

$$
A_{\mathrm{known}}
+
A_{\mathrm{novel}}
$$

轉成：

$$
H_A
$$

attack interaction hypergraph。

核心將正式處理：

- independence；
- ordering；
- conflict；
- masking；
- synergy；
- dependency；
- conditional applicability；
- multi-attack state transition；
- partial order；
- composition safety；
- global campaign synthesis。

---

# 64. 結論

如果局部 attack 每次使用完都被丟掉，那麼：

$$
\text{Experience}
\rightarrow
\text{Disposable Cost}.
$$

如果它只被保存在 log 裡，但沒有型別、版本、前提、validator、history 與 relation，那麼：

$$
\text{Experience}
\rightarrow
\text{Archive}.
$$

只有當失敗被轉化為：

$$
\boxed{
\text{Versioned}
+
\text{Typed}
+
\text{Evidence-Bearing}
+
\text{Structurally Retrievable}
+
\text{Transfer-Aware}
}
$$

的知識後，才真正形成：

$$
\boxed{
\text{Adversarial Memory Capital}.
}
$$

本文因此提出：

$$
\boxed{
\text{SEDB-style AMS}
}
$$

作為全域對抗計算的持久知識層。

它不是永動 attack engine。

它的真正目的恰恰相反：

$$
\boxed{
\text{Remember enough so that AI does not have to think the same expensive thought twice.}
}
$$

中文可以表述為：

> **把已經付過算力成本的失敗，保存成未來不必重新付費的工程知識。**

因此：

$$
\text{Known Failure}
\rightarrow
\text{Cheap Recognition},
$$

而：

$$
\text{Residual Unknown}
\rightarrow
\text{Frontier Reasoning}.
$$

這就是軟體免疫記憶的第一版工程含義。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
