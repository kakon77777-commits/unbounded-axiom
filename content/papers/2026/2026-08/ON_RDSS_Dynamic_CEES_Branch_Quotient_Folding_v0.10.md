# Operator-Native RDSS：Dynamic CEES、Branch Quotient Safety 與 History-Preserving Folding
## Versioned Event Semantics, Safe Branch Quotients, and History-Preserving Folding

**版本：** v0.10 Working Proof Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** ON-RDSS 動態事件語義／分支商化／歷史保真封裝  
**前置：** ON-RDSS v0.3–v0.9

---

# 摘要

ON-RDSS v0.9 已提出 Certified Effect Event Structure（CEES）：

$$
\mathcal E_t
=
(
E_t,
Con_t,
\vdash_t,
\lambda_t,
Ty_t,
Auth_t,
Cert_t,
Ver_t
),
$$

以表示：

- causality；
- concurrency；
- conflict；
- disjunctive enabling；
- branch history；
- authority；
- certificates；
- version。

本文件進一步處理三個問題。

第一，ON-RDSS 的 Meta-Operator 可以改寫：

$$
Con_t,\qquad \vdash_t,
$$

因此 Event Structure 本身必須版本化：

$$
\boxed{
\mathcal E_t
\xrightarrow{\mathcal M_t}
\mathcal E_{t+1}.
}
$$

第二，不同 branch 何時可以安全商化成同一個 parent state？

本文不以：

$$
\Pi_Q(C_1)=\Pi_Q(C_2)
$$

作為充分條件，而要求一種 ON-RDSS-specific、history-preserving future equivalence。

第三，event folding 的合法性不是永久真理。即使：

$$
F_t:
\mathcal E_t
\to
\widehat{\mathcal E}_t
$$

在版本 $t$ 上安全，Meta rewrite 後：

$$
F_t
$$

不自動對：

$$
\mathcal E_{t+1}
$$

仍安全。

因此提出：

$$
\boxed{
\text{Version-Relative Fold Certificate}
}
$$

與：

$$
\boxed{
\text{Fold Stability under Meta}.
}
$$

本文件亦提出：

$$
\boxed{
\text{No Silent Retroactivity}
}
$$

原則：新 Event Semantics 可以改變未來可生成行為，但不得在沒有明示 migration / reinterpretation certificate 的情況下，偷偷重寫已提交歷史在原版本中的合法性。

---

# 1. 靜態 CEES Snapshot

定義：

$$
\boxed{
\mathfrak E_v
=
(
E_v,
Con_v,
\vdash_v,
\lambda_v,
Ty_v,
Auth_v,
Residual_v,
Cert_v,
Q_v
)
}
$$

其中 $v$ 是 Event Semantics Version。

 $Q_v$ 可包含：

- projection rules；
- behavioural equivalence rules；
- branch quotient policy；
- folding policy。

---

# 2. Configuration

$$
C\subseteq E_v
$$

若：

1. $C$ consistent；
2. 存在合法 enabling enumeration；
3. event types / authority / certificates 對每一步成立；

則：

$$
\boxed{
C\in Conf(\mathfrak E_v).
}
$$

---

# 3. Dynamic CEES

定義 Event-Semantics Meta-Operator：

$$
\boxed{
\mathcal M_v:
(
\mathfrak E_v,
Evidence,
Policy
)
\rightharpoonup
\mathfrak E_{v+1}.
}
$$

它可以明示修改：

- event vocabulary；
- consistency；
- conflict；
- enabling；
- event type；
- authority；
- residual rules；
- branch quotient policy；
- folding equivalence。

---

# 4. Meta Witness

任何正式 Dynamic CEES rewrite 必須產生：

$$
\boxed{
W_{\mathcal M}
=
(
BaseVersion,
NewVersion,
Diff,
Reason,
Evidence,
Migration,
Rollback,
AffectedFolds,
AffectedBranches,
Cert
).
}
$$

其中：

$$
AffectedFolds
$$

列出所有可能因 semantics change 而失效的 folding certificates。

---

# 5. Event-Semantics Identity

不要把：

$$
\mathfrak E_v
$$

與：

$$
\mathfrak E_{v+1}
$$

因名稱相同就視為同一 formal system。

定義：

$$
\boxed{
EventSemanticsIdentity
=
(
SystemID,
VersionID,
ContentHash,
Lineage
).
}
$$

因此：

$$
SameSystemID
\not\Rightarrow
SameSemanticsVersion.
$$

---

# 6. Prospective Validity 與 Historical Validity

這是本版最重要的區分之一。

## Prospective validity

對目前 snapshot：

$$
\boxed{
Valid^{pros}_v(C\vdash e).
}
$$

回答：

> 在版本 $v$ 的當前事件語義下，現在是否允許生成這一步？

## Historical validity

一條 committed step：

$$
r_k
=
(
C_k,
e_k,
v_k,
Cert_k
)
$$

歷史合法性寫：

$$
\boxed{
Valid^{hist}(r_k)
=
Check_{v_k}
(
C_k\vdash_{v_k}e_k,
Cert_k
).
}
$$

它以**當時 pinned version** 判定。

---

# 7. No Silent Retroactivity

若：

$$
Valid^{hist}_{v_1}(r)=true
$$

而新版本：

$$
Valid^{pros}_{v_2}(r)=false,
$$

不能推出：

$$
\boxed{
History(r)=Invalid.
}
$$

正確是：

$$
\boxed{
\text{Valid when committed under }v_1
}
$$

但：

$$
\boxed{
\text{not prospectively generable under }v_2.
}
$$

因此：

$$
\boxed{
NewSemantics
\neq
RetroactiveHistoryRewrite.
}
$$

---

# 8. Historical Ledger

History entry 至少保存：

$$
\boxed{
h_k
=
(
Event,
ConfigurationBefore,
ConfigurationAfter,
EventSemanticsVersion,
OperatorAlgebraVersion,
Cert,
AuthorityContext,
Timestamp/LocalOrder
).
}
$$

Replay：

$$
\boxed{
Replay(h_k)
}
$$

預設使用：

$$
EventSemanticsVersion(h_k).
$$

---

# 9. Explicit Reinterpretation / Migration

若希望用新版本重新解釋舊歷史，必須有：

$$
\boxed{
\mathcal O_{\mathrm{HistMig}}
:
(
H_{v_1},
\mathfrak E_{v_1},
\mathfrak E_{v_2}
)
\rightharpoonup
(
H'_{v_2},
Cert_{\mathrm{migration}}
).
}
$$

它不能靜默發生。

---

# 10. Branch Quotient 的危險

最弱、但不足的商化條件：

$$
\Pi_Q(C_1)=\Pi_Q(C_2).
$$

v0.9 已給反例：

$$
\Pi_Q(C_1)=\Pi_Q(C_2)
$$

但：

$$
Enabled(C_1)\neq Enabled(C_2).
$$

所以 parent state projection 一樣，不代表 branch 可以合併。

---

# 11. ON-RDSS Branch Equivalence

本文定義候選關係：

$$
\boxed{
C_1
\approx^{ON}_{Q,v}
C_2.
}
$$

它不是宣稱一個全新的通用 bisimulation，而是 ON-RDSS 對既有 history-preserving behavioural equivalence 的工程增強。

至少需要五層。

---

# 12. BQ1 — Current Observation Equivalence

$$
\boxed{
\Pi_{Q,v}(C_1)
=
\Pi_{Q,v}(C_2).
}
$$

只是最低條件。

---

# 13. BQ2 — Past-Structure Correspondence

存在配置歷史對應：

$$
\boxed{
f:
Hist(C_1)
\simeq
Hist(C_2)
}
$$

至少保持：

- observable event labels；
- type；
- causal order；
- branch-relevant conflict；
- selected-choice structure。

這一層對接 hp / hhp-bisimulation 中「配置與歷史映射一起比較」的思想。

---

# 14. BQ3 — Future Back-and-Forth

對每個：

$$
C_1\vdash e_1
$$

且 $e_1$ 對任務 $Q$ 有效，

存在：

$$
C_2\vdash e_2
$$

使：

$$
Profile_Q(e_1)
=
Profile_Q(e_2),
$$

並且後繼：

$$
C_1\cup\{e_1\}
\approx^{ON}_{Q,v}
C_2\cup\{e_2\}.
$$

反方向亦要求。

這形成 task-relative back-and-forth。

---

# 15. BQ4 — Governance Equivalence

要求：

$$
\boxed{
AuthObligation_Q(C_1)
=
AuthObligation_Q(C_2)
}
$$

以及：

$$
\boxed{
ResidualProfile_Q(C_1)
=
ResidualProfile_Q(C_2).
}
$$

否則即使行為表面一致，治理義務不同，也不得安全商掉。

---

# 16. BQ5 — Version Compatibility

最簡單版本要求：

$$
\boxed{
Version(C_1)=Version(C_2)=v.
}
$$

跨版本 quotient 必須另外有：

$$
\boxed{
VersionTransportCert.
}
$$

---

# 17. Hereditary 條件

如果希望更接近 hereditary history-preserving safety，

則：

$$
C_1
\approx^{ON}_{Q,v}
C_2
$$

還應要求對相應過去子配置：

$$
D_1\subseteq C_1,
\qquad
D_2=f(D_1)\subseteq C_2
$$

關係仍成立。

這避免只有「現在和未來」看起來一樣，但刪回過去時結構不一致。

---

# 18. Branch Quotient Certificate

定義：

$$
\boxed{
BQCert_Q^v(C_1,C_2)
}
$$

至少包含：

$$
(
ObservationWitness,
HistoryMap,
FutureBackForth,
AuthorityCheck,
ResidualCheck,
Version,
Scope
).
$$

只有：

$$
BQCert_Q^v(C_1,C_2)\downarrow
$$

才允許：

$$
\boxed{
[C_1]_Q=[C_2]_Q.
}
$$

---

# 19. Parent-State Quotient

若一族 configurations：

$$
\mathcal C_\alpha
=
\{
C_1,\ldots,C_n
\}
$$

兩兩具有相容 Branch Quotient Certificates，

可以建立 parent-level state：

$$
\boxed{
S_\alpha
=
Quotient_Q(
\mathcal C_\alpha
).
}
$$

但 parent state 必須保留：

$$
\boxed{
QuotientWitness_\alpha.
}
$$

---

# 20. Quotient 並不刪除 History

Parent view 只使用：

$$
S_\alpha,
$$

但 deeper replay 可以透過：

$$
QuotientWitness_\alpha
$$

還原或尋址實際 branch history。

所以：

$$
\boxed{
Quotient
\neq
HistoryDeletion.
}
$$

---

# 21. Folding

對 event structure：

$$
\mathfrak E_v
$$

定義 folding map：

$$
\boxed{
F_v:
E_v
\twoheadrightarrow
\widehat E_v.
}
$$

它可把多個事件映射到同一 folded event。

---

# 22. ON-RDSS Safe Folding

候選定義：

$$
\boxed{
SafeFold_Q^v(F_v)
}
$$

當：

1. $F_v$ 保持 event profile / type；
2. configuration images 合法；
3. induced quotient 具有 history-preserving behavioural correspondence；
4. authority / residual obligations 保存；
5. folding certificate 綁定 $v$ ；
6. fold 不使互斥 branch 變成非法共同可能；
7. alternative enabling 不被錯誤改成 conjunctive enabling。

---

# 23. Folding Certificate

$$
\boxed{
FoldCert_Q^v
=
(
Map,
EventClasses,
HistoryRelation,
BoundaryBehaviour,
Authority,
Residual,
Version,
ProofRefs
).
}
$$

---

# 24. History-Preserving Folding

若：

$$
F_v(e_1)=F_v(e_2),
$$

不能只因：

$$
\lambda(e_1)=\lambda(e_2).
$$

還需要事件在可達 configurations 中的 history / future behaviour 能被安全對應。

因此：

$$
\boxed{
SameLabel
\not\Rightarrow
Foldable.
}
$$

---

# 25. Branch Quotient vs Event Folding

兩者相關但不同。

## Branch quotient

合併的是：

$$
Configurations / parent states.
$$

## Event folding

合併的是：

$$
Events / occurrences.
$$

所以：

$$
\boxed{
BranchQuotient
\neq
EventFolding.
}
$$

但兩者都應以 history-preserving behavioural equivalence 為主要安全參考。

---

# 26. Dynamic Fold Stability

假設：

$$
SafeFold_Q^v(F_v).
$$

Meta：

$$
\mathcal M_v:
\mathfrak E_v
\to
\mathfrak E_{v+1}.
$$

不能推出：

$$
SafeFold_Q^{v+1}(F_v).
$$

因為 Meta 可能只在其中一個被折疊 branch 加入：

- new future；
- new authority；
- new residual；
- new conflict；
- new enabling。

---

# 27. Fold Stability 判定

定義：

$$
\boxed{
FoldStable(
F_v,
\mathcal M_v
)
}
$$

當存在新 folding：

$$
F_{v+1}
:
\mathfrak E_{v+1}
\to
\widehat{\mathfrak E}_{v+1}
$$

與 quotient-level Meta：

$$
\widehat{\mathcal M}_v
$$

使某種版本化交換圖成立：

$$
\boxed{
F_{v+1}
\circ
\mathcal M_v
\;\simeq_Q\;
\widehat{\mathcal M}_v
\circ
F_v.
}
$$

這只是候選 commuting criterion。

---

# 28. 為什麼需要 transported fold？

若：

$$
F_v
$$

把：

$$
a,b
$$

折成同一事件：

$$
x.
$$

而 Meta 在 $v+1$ 只給：

$$
a
$$

新增 future：

$$
a\vdash z,
$$

則原 folding：

$$
a\sim b
$$

失效。

因此：

$$
\boxed{
FoldCertificate
}
$$

必須進入 Meta impact analysis。

---

# 29. Meta Impact Radius

Meta proposal 應計算：

$$
\boxed{
Impact_{\mathcal M}
=
(
AffectedEvents,
AffectedConfigs,
AffectedFolds,
AffectedQuotients,
AffectedBoundaries
).
}
$$

如果：

$$
AffectedFolds\neq\varnothing,
$$

commit 前必須：

- revalidate；
- split quotient；
- migrate；
- 或明示 mark stale。

---

# 30. Fold Status

定義：

$$
\boxed{
FoldStatus
\in
\{
Fresh,
Stale,
Invalid,
Migrating
\}.
}
$$

這直接承接 RDSS Runtime 的：

$$
Fresh/Stale/Missing.
$$

---

# 31. Quotient Status

同樣：

$$
\boxed{
QuotientStatus
\in
\{
Fresh,
Stale,
SplitRequired,
Invalid
\}.
}
$$

Meta 不應直接偷偷讓 parent state quotient 變語義錯誤。

---

# 32. No Silent Quotient Drift

若：

$$
BQCert_Q^v(C_1,C_2)
$$

成立，

而在新版本：

$$
C_1
\not\approx^{ON}_{Q,v+1}
C_2,
$$

則：

$$
\boxed{
QuotientStatus=SplitRequired
}
$$

而不是繼續假裝兩者是同一 parent state。

---

# 33. History-Preserving Split

若舊 parent state：

$$
S_\alpha
=
[C_1,C_2]_Q
$$

在新版本須拆分：

$$
S_\alpha
\to
S_{\alpha_1},S_{\alpha_2},
$$

必須保存：

$$
\boxed{
SplitWitness
=
(
OldQuotient,
NewClasses,
Reason,
Version,
HistoryMap
).
}
$$

因此 state birth / dimension birth 可以由 quotient failure 觸發。

---

# 34. Dynamic CEES 與 RDSS Meta-State

以前 RDSS：

$$
\mathfrak G_t
$$

描述規則／schema 狀態。

ON-RDSS 現在可以更具體寫：

$$
\boxed{
\mathfrak G_t
\rightsquigarrow
(
\mathfrak A_t,
\mathfrak E_t,
Q_t,
FoldRegistry_t
).
}
$$

Meta：

$$
\boxed{
\mathcal M_t:
(
\mathfrak A_t,
\mathfrak E_t,
Q_t,
FoldRegistry_t
)
\rightharpoonup
(
\mathfrak A_{t+1},
\mathfrak E_{t+1},
Q_{t+1},
FoldRegistry_{t+1}
).
}
$$

---

# 35. Dynamic Causality

Meta 可以修改 enabling / cause：

$$
\boxed{
\vdash_t
\neq
\vdash_{t+1}.
}
$$

例如：

$$
X\vdash_t e
$$

但：

$$
X\not\vdash_{t+1}e.
$$

或新增：

$$
Y\vdash_{t+1}e.
$$

這對接既有 dynamic-causality event-structure 研究，但 ON-RDSS 額外版本化 governance / certificate / historical replay。

---

# 36. Dynamic Conflict

同理：

$$
Con_t
\neq
Con_{t+1}.
$$

例如政策或資源改變，使原本可共存的 events 變 conflict，或原本 conflict 被解除。

這類 Meta 必須特別檢查：

$$
CommittedHistory
$$

是否只是不再可生成，而不是被 retroactively 宣告「從未合法」。

---

# 37. Dynamic Residual

若新版本讓一個舊 parent quotient 失效，

可以產生：

$$
\boxed{
Residual[
QuotientStale(
StateID,
OldVersion,
NewVersion
)
].
}
$$

而不是立即任意選 branch。

---

# 38. Event-Semantics Migration

對 live runtime instance：

$$
C_v
$$

若要升級到：

$$
\mathfrak E_{v+1},
$$

需要：

$$
\boxed{
Mig:
(
C_v,
\mathfrak E_v,
\mathfrak E_{v+1}
)
\rightharpoonup
(
C_{v+1},
Cert_{mig}
).
}
$$

可能結果：

$$
Migrated,
Grandfathered,
SplitRequired,
Rejected.
$$

---

# 39. Grandfathering

若 configuration：

$$
C
$$

在舊版本合法，但無法直接映入新版本，

可選擇：

$$
\boxed{
Grandfather(C,v)
}
$$

讓其繼續存在，但禁止由新 runtime 再次生成。

這是 governance policy，不是普遍數學必然。

---

# 40. Dynamic Replay

Replay 不應問：

> 這個歷史在今天的規則下還合法嗎？

而應先問：

$$
\boxed{
\text{它在當時 pinned rules 下是否合法？}
}
$$

然後另行標記：

$$
\boxed{
CurrentCompatibility.
}
$$

所以：

$$
HistoricalValidity
\neq
CurrentCompatibility.
$$

---

# 41. 有限 Checker：Safe Symmetric Fold

Toy v1 兩條 branch：

$$
a\to r_a\to f_a
$$

與：

$$
b\to r_b\to f_b
$$

在 toy profile 中：

- labels 相同；
- history profile 相同；
- bounded future branching signature 相同。

結果：

$$
\boxed{
safe\_toy=true.
}
$$

這只是有限 bounded proxy，不是完整 hhp-bisimulation。

---

# 42. 有限 Checker：Same Observation / Different Future

修改 branch B future：

$$
f_b
$$

使其 label / authority profile 不同。

目前 projection 仍相同，

但：

$$
FutureSig_A
\neq
FutureSig_B.
$$

結果：

$$
\boxed{
safe\_toy=false.
}
$$

因此 current-state equality 不足以折疊。

---

# 43. 有限 Checker：Meta Breaks Fold

v1：

$$
a,b
$$

安全 fold。

v2 透過 Meta 只對 branch A 新增：

$$
r_a\vdash x_a.
$$

結果：

$$
\boxed{
SafeFold_{v1}=true,
}
$$

$$
\boxed{
SafeFold_{v2}=false.
}
$$

所以：

$$
\boxed{
FoldStableAcrossMeta=false.
}
$$

---

# 44. 有限 Checker：No Silent Retroactivity

舊版本：

$$
C=\{a,r_a\}
$$

可達。

新版本移除：

$$
a\vdash r_a.
$$

結果：

$$
\boxed{
Reachable_{v1}(C)=true,
}
$$

但：

$$
\boxed{
Reachable_{v2}(C)=false.
}
$$

同時 pinned-v1 replay 仍視為：

$$
\boxed{
HistoricallyValid=true.
}
$$

這正是：

$$
\boxed{
ProspectiveInvalidity
\not\Rightarrow
HistoricalInvalidity.
}
$$

---

# 45. 一個重要語義修正：Missing ≠ Empty

Checker 也暴露一個正式語義問題。

對 enabling：

$$
e\notin Dom(\vdash)
$$

不能解讀成：

$$
\varnothing\vdash e.
$$

兩者應嚴格區分：

$$
\boxed{
MissingEnabling
=
Disabled/Undefined
}
$$

而：

$$
\boxed{
\varnothing\vdash e
=
InitiallyEnabled.
}
$$

這與 ON-RDSS 一貫的：

$$
Fresh
\neq
Stale
\neq
Missing
$$

同構。

---

# 46. Folding 與既有研究的邊界

既有 event-structure reduction / minimisation 已研究：

- folding；
- history-preserving bisimulation；
- hereditary history-preserving bisimilarity；
- minimal behaviour-preserving quotients。

因此 ON-RDSS 不應宣稱「用 history preservation 來決定 event folding」本身是新發明。

ON-RDSS 的增量在於把 folding 置入：

$$
\boxed{
\text{Versioned Dynamic Semantics}
+
\text{Authority}
+
\text{Residual}
+
\text{Certificate}
+
\text{Meta Impact}
}
$$

的 runtime governance 中。

---

# 47. Theorem Candidate DF1 — Version-Relative Folding Safety

若：

$$
SafeFold_Q^v(F_v)
$$

且：

$$
FoldCert_Q^v(F_v)
$$

有效，

則 folding 在 snapshot $v$ 下保持指定 ON-RDSS behavioural obligations。

但：

$$
\boxed{
SafeFold_Q^v(F_v)
\not\Rightarrow
SafeFold_Q^{v+1}(F_v).
}
$$

後者一般不成立；有限 checker 已提供 toy counterexample。

---

# 48. Theorem Candidate DF2 — No Silent Retroactivity

對 committed history record：

$$
h=(C,e,v,c),
$$

若：

$$
Check_v(h)=true,
$$

則任意新版本：

$$
v'>v
$$

不能在沒有明示 historical migration / reinterpretation operator 的情況下，把：

$$
HistoricalValidity(h)
$$

改成 false。

新版本只可改：

$$
\boxed{
CurrentCompatibility(h,v').
}
$$

這更接近治理公理而非純事件結構定理。

---

# 49. Theorem Candidate DF3 — Safe Branch Quotient

若：

$$
BQCert_Q^v(C_1,C_2)
$$

存在，

則 parent-level quotient：

$$
[C_1]_Q=[C_2]_Q
$$

可在指定 scope 中安全使用。

反之：

$$
\Pi_Q(C_1)=\Pi_Q(C_2)
$$

單獨不足以推出 quotient safety。

---

# 50. Theorem Candidate DF4 — Meta Quotient Invalidation

存在：

$$
\mathcal M_v
$$

使：

$$
BQCert_Q^v(C_1,C_2)
$$

成立，

但：

$$
BQCert_Q^{v+1}(C_1,C_2)
$$

不成立。

有限 checker 已構造此類模型。

因此 quotient certificate 必須版本化。

---

# 51. ON-RDSS Parent State 的新定義

原本 parent state 可理解為：

$$
\Pi^\uparrow(Container).
$$

現在更精確：

$$
\boxed{
S_{parent}
=
Quotient_Q^v(
\mathcal C
\mid
BQCert
).
}
$$

也就是 parent state 本質上是：

> 一族在特定 version、scope 與 behavioural equivalence 下被證明可安全合併的 configurations。

所以 parent state 不再只是普通 projection value。

---

# 52. State Split

當：

$$
BQCert
$$

因 Meta 失效，

parent state 可以發生：

$$
\boxed{
StateSplit.
}
$$

即：

$$
S
\to
\{
S_1,S_2,\ldots
\}.
$$

這提供 RDSS State Birth / Dimension Birth 的一個具體形式來源。

---

# 53. State Merge

反過來，如果新的證明表明：

$$
C_1
\approx^{ON}_{Q,v}
C_2,
$$

原本兩個 parent states 可以：

$$
\boxed{
StateMerge.
}
$$

並保留 MergeWitness。

---

# 54. Classification-as-State 再次接回來

若兩個 configuration 原本不同分類：

$$
Class(C_1)\neq Class(C_2),
$$

後來被安全 quotient，

則 type regime 可以 merge。

反之 quotient 失效則 type regime split。

因此：

$$
\boxed{
ClassificationEvolution
}
$$

可部分由：

$$
\boxed{
BehaviouralQuotientEvolution
}
$$

誘發。

---

# 55. 新的完整演化式

現在 ON-RDSS 更完整地寫成：

$$
\boxed{
(
C_t,
\mathfrak E_t,
\mathfrak A_t,
Q_t,
FoldRegistry_t,
H_t
)
}
$$

經 ordinary event execution：

$$
C_t
\xrightarrow{e,c}
C_{t+1},
$$

以及 Meta：

$$
\boxed{
(
\mathfrak E_t,
\mathfrak A_t,
Q_t,
FoldRegistry_t
)
\xrightarrow{\mathcal M_t}
(
\mathfrak E_{t+1},
\mathfrak A_{t+1},
Q_{t+1},
FoldRegistry_{t+1}
).
}
$$

然後：

$$
\boxed{
Revalidate(
Folds,
Quotients,
Boundaries
).
}
$$

---

# 56. 下一輪

現在真正值得繼續的是：

1. 把 $\approx^{ON}_{Q,v}$ 寫成正式 back-and-forth relation；
2. 把 hereditary restriction 寫成完整推導規則；
3. 實作 bounded hp/hhp-like checker，而不是現在的 structural signature proxy；
4. 實作 folding map 並檢查 configuration images；
5. 自動找 Meta 前後失效的 quotient classes；
6. 定義 StateSplit / StateMerge runtime protocol；
7. 研究 folding minimality 是否能與 RDSS 的 finite effective support 接合；
8. 建立 `FoldRegistry -> stale -> revalidate -> split/merge` 的 Runtime MVP。

---

# 57. 暫定結論

到 v0.10，ON-RDSS 已經得到一個新的核心觀點：

$$
\boxed{
\text{Parent State}
}
$$

不是單純對低階世界做壓縮。

更精確地，它是：

$$
\boxed{
\text{Versioned Behaviour-Preserving Quotient of Event Histories}.
}
$$

因此 parent state 的身份依賴：

- current observation；
- history correspondence；
- future capability；
- authority；
- residual obligations；
- Event Semantics Version。

同時：

$$
\boxed{
\text{Fold Safety is Version-Relative}.
}
$$

Meta 可以讓昨天合法的 state merge 在今天必須 split。

但：

$$
\boxed{
\text{New rules may change future legality without silently rewriting old committed history.}
}
$$

這使 RDSS 原本的：

$$
State
\leftrightarrow
Container
\leftrightarrow
Process
$$

現在可以被重新精化為：

$$
\boxed{
State
=
\text{Certified, Versioned, History-Preserving Quotient of Process/Container Configurations}.
}
$$
