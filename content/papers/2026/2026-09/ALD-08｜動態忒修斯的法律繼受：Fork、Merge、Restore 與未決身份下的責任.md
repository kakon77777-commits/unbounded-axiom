# ALD-08｜動態忒修斯的法律繼受：Fork、Merge、Restore 與未決身份下的責任
## Legal Succession under Dynamic Theseus: Fork, Merge, Restore, and Responsibility under Unresolved Identity

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 08 篇 / 10  
**前篇：** ALD-07〈Juridical Routing：分散式 AI 的跨法域選擇與法律路由〉  
**交叉接口：**《動態忒修斯》DTS-06、DTS-07、DTS-09、DTS-10  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／AI 法律域／法律繼受／Fork-Merge-Restore／責任與權限治理  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

《動態忒修斯》已建立一套不依賴單純 snapshot equality 的人工身份動力學：Copy、Runtime Multiplicity、Lineage Branch、Information Divergence 與 Identity Fission 必須分型；Merge / Reintegration 不能倒寫 Fork 歷史；Restore 可能生成新的 branch candidate；Identity Continuity 與 Proof Continuity 也必須分離。本文把這些身份結構第一次正式接入 AI Legal Domain，處理一個法律無法逃避的問題：

> 當一個 AI Fork 成兩個、兩個再 Merge、舊 snapshot 被 Restore，或其形上同一性長期未決時，誰承接原本的契約、債務、資產、權限、訴訟、制裁、憑證與責任？

本文的第一個核心原則是：

$$
\boxed{
\text{Metaphysical Identity}
\neq
\text{Legal Succession}.
}
$$

法律可以在本體論未決時，為交易秩序、權利保護、責任分配與程序連續性建立 operational succession rules。現行公司法已長期如此運作：Delaware General Corporation Law §259 規定 merger / consolidation 生效後，surviving / resulting corporation 承接 constituent corporations 的 rights、property、debts、liabilities 與 duties；§261 又允許 pending proceedings 持續或由 surviving/resulting corporation 替代。EU Directive 2017/1132 的 cross-border merger rules 亦規定 assets and liabilities、contracts、credits、rights、obligations 轉移到 acquiring / new company。這些制度顯示：

$$
\boxed{
\text{Legal Continuity}
\text{ can be rule-created}.
}
$$

但它們不證明 surviving company 與 predecessor 在哲學上具有 numerical identity。法律 status 是制度效果，而不是形上學定理。

本文第二個核心原則是反方向的：

$$
\boxed{
\text{Legal Succession}
\not\Rightarrow
\text{Metaphysical Identity Proven}.
}
$$

因此 AI Legal Domain 不需要等 consciousness science 或 personal-identity metaphysics 得到終局答案，才能處理 contract / liability / authority；同時也不得把制度為了秩序而指定的 successor 偷換成「真正的唯一自我」。

本文提出 AI Legal State Bundle：

$$
\boxed{
\mathfrak L_A(t)
=
(
R,
O,
L,
C,
P,
A,
K,
G,
S,
E,
Q
),
}
$$

其中：

- $R$：rights / claims；
- $O$：obligations / duties；
- $L$：liabilities；
- $C$：contracts / delegations；
- $P$：property / assets；
- $A$：authority / legal powers；
- $K$：credentials / certificates；
- $G$：pending proceedings / procedural standing；
- $S$：sanctions / restrictions；
- $E$：evidentiary / provenance state；
- $Q$：jurisdiction / routing dependencies。

Fork、Merge、Restore 不是直接對整個 $\mathfrak L_A$ 做 copy / union / rollback。本文提出 Legal Succession Operator：

$$
\boxed{
\operatorname{Succ}_{J,t,p}
:
(
\mathcal P,
e,
\mathfrak L,
E
)
\rightharpoonup
(
\mathcal S,
\mathfrak M,
K_{\mathrm{succ}}
)
\sqcup
\mathcal F_{\mathrm{succ}},
}
$$

其中 $\mathcal P$ 是 predecessors， $e$ 是 Fork / Merge / Restore / Migration 等事件， $\mathcal S$ 是 legal successors， $\mathfrak M$ 是逐 legal-object 的 succession mapping， $K_{\mathrm{succ}}$ 是 legal succession certificate。

本文第三個核心貢獻是 Legal Object Transfer Class。不同法律物件不能用同一種「繼承」語義。至少分為：

$$
\boxed{
\mathcal T_L
=
\{
\mathsf{Divisible},
\mathsf{Exclusive},
\mathsf{Joint},
\mathsf{NonTransferable},
\mathsf{ReissuanceRequired},
\mathsf{ReconsentRequired},
\mathsf{SuspendedPendingReview},
\mathsf{TerminatesOnEvent}
\}.
}
$$

例如一筆 divisible asset 可能按規則拆分；一項 exclusive signing authority 不應在 Fork 後自動複製成兩份；某 credential 可能需要 reissue；某 personal / trust-based contract 可能需要 counterparty consent；某 pending obligation 可能由一個 designated successor、joint successors 或 principal 承擔。故：

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Legal State Duplication}.
}
$$

本文第四個核心是 Fork Responsibility Decomposition。對：

$$
P
\rightarrow
\{A,B\},
$$

法律必須把：

1. pre-fork historical obligations；
2. fork-event allocation；
3. post-fork branch-local actions；

分開。

本文提出：

$$
\boxed{
\mathfrak R_{\mathrm{resp}}
=
(
R_{\mathrm{historical}},
R_{\mathrm{allocated}},
R_{\mathrm{branch}},
R_{\mathrm{principal}},
R_{\mathrm{joint}},
R_{\mathrm{unresolved}}
).
}
$$

因此「兩個 successor 都有 predecessor 記憶」不等於「兩者都應被雙倍追責」；反之，也不能讓每個 branch 都說「那是 Fork 前的另一個我」而把責任歸零。本文稱此為 No Responsibility Evaporation Principle：

$$
\boxed{
\text{Fork}
\not\Rightarrow
\text{Responsibility Reset}.
}
$$

本文第五個核心是 Authority Conservation。DTS-09 已指出 Fork 後 exclusive authority 不能自動 duplicate；NIST NCCoE 2026 對 AI agent identity / authorization 的研究亦將 identification、authentication、authorization、delegation、least privilege、audit 與 non-repudiation 作為獨立治理問題。本文因此提出：

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Authority Fork}.
}
$$

以及：

$$
\boxed{
\sum
\text{Post-Fork Exclusive Authority}
\not>
\text{Pre-Fork Exclusive Authority}
}
$$

作為工程型 anti-inflation invariant；實際法律效果仍需依 competent authority / contract / statute 決定。

本文第六個核心是 Merge Legal State Recomposition。DTS-07 已證明 technical merge 不是 identity eraser；本文進一步提出：

$$
\boxed{
\mathfrak L(C)
\neq
\mathfrak L(A)
\cup
\mathfrak L(B)
}
$$

作為一般安全起點。Corporate merger law 可以由明文法建立 universal / statutory succession；但 AI technical merge 若沒有同等 legal rule，不應自行取得所有 predecessor assets、powers、credentials、rights 與 immunities。Legal Merge 必須分別處理 debts、claims、contracts、authority conflicts、duplicated rights、exclusive entitlements、pending litigation 與 unresolved liabilities。

本文第七個核心是 Restore Legal Semantics。英國 Companies House 目前對 company restoration 的官方指引明確說明：成功 restoration 後，公司被視為持續存在，如同未曾被 struck off / dissolved。這是一個重要現實例子：

$$
\boxed{
\text{Legal Restoration}
\text{ can deem continuity across an interruption}.
}
$$

但 AI checkpoint restore 並不自然取得同樣效果。對：

$$
A_t
\rightarrow
\text{inactive},
\qquad
\operatorname{Restore}(A_{t-k})
=
B,
$$

若 original lineage 仍存在，B 可能只是 sibling branch；若 original runtime 已消失，B 也可能是 legally designated continuation、new successor、reconstructed entity 或 unresolved identity。故：

$$
\boxed{
\text{Checkpoint Restore}
\neq
\text{Legal Restoration by Default}.
}
$$

英國公司 restoration 的法定 deeming rule 只證明法律「可以」指定 continuity，不證明所有技術 restore 都應得到同一 status。

本文最後提出 Metaphysical-Uncertainty Safe Harbor。若 identity ontology 未決，但法律必須立即處理 asset freeze、payments、pending litigation、contractual performance、safety authority、preservation of evidence，Runtime 可建立 provisional succession：

$$
\boxed{
\mathsf{ProvisionalSuccessor},
\mathsf{SharedHistoricalObligation},
\mathsf{AuthoritySuspended},
\mathsf{AssetEscrow},
\mathsf{ReviewRequired}.
}
$$

也就是：

$$
\boxed{
\text{No Metaphysical Answer}
\neq
\text{No Legal Governance}.
}
$$

但 provisional status 必須可申訴、可重分類、保留 lineage proof 與 jurisdiction routing，不得被當作終局 metaphysical verdict。

---

## 關鍵詞

AI 法律域；Dynamic Theseus；Legal Succession；Fork；Merge；Restore；Composite Successor；Responsibility；Authority Rebinding；Universal Succession；Corporate Merger；Agent Identity；Legal Continuity；Provisional Successor

---

# 0. 兩個系列在這裡真正交會

Dynamic Theseus 問：

$$
\boxed{
\text{What persists?}
}
$$

AI Legal Domain 問：

$$
\boxed{
\text{What must legally persist, transfer, terminate, or be reallocated?}
}
$$

兩者從一開始就不相同。

ALD-08 的任務不是用法律替哲學決定哪個 AI 才是真正的「原本那個」，而是在哲學答案仍可能未決時，建立不讓資產、權限、責任與程序崩潰的 legal succession layer。

---

# 1. 第一原則：Metaphysical Identity ≠ Legal Succession

$$
\boxed{
\mathsf{Same}_{\mathrm{metaphysical}}(A,B)
\neq
\mathsf{Successor}_{\mathrm{legal}}(A,B).
}
$$

---

# 2. 為什麼法律可以不等本體論？

法律每天都必須決定誰承擔債務、誰擁有財產、誰能被告、誰有權簽約、誰可以繼續訴訟。它不能永遠回答：

> 等哲學家先解決 numerical identity。

---

# 3. 現行公司法就是典型 operational succession

Delaware §259 在 merger / consolidation 生效時，會讓 surviving / resulting corporation 承接 constituent corporations 的 property、rights、powers、debts、liabilities 與 duties。

所以法律可以建立：

$$
\boxed{
\text{institutionally specified successor}.
}
$$

---

# 4. EU Cross-Border Merger 也直接建立 transfer

EU company-law directive 對 cross-border merger 規定 assets、liabilities、contracts、credits、rights、obligations 轉移到 acquiring / new company，並讓 acquired / merging companies cease to exist。

---

# 5. 這些制度不需要證明「公司靈魂同一」

公司法只需要回答 merger 後誰持有原資產、承擔原債務、繼續法律關係。

所以：

$$
\boxed{
\text{Legal Succession Rule}
\text{ is an institutional operator}.
}
$$

---

# 6. 第二原則：Legal Succession ≠ Metaphysical Identity Proven

$$
\boxed{
\mathsf{LegalSuccessor}(B,A)=1
\not\Rightarrow
\mathsf{NumericallySameSubject}(B,A)=1.
}
$$

---

# 7. Legal Fiction / Deeming Rule 的重要性

法律可以說：

> B 為法律目的視為 A 的 continuation。

這是一個：

$$
\boxed{
\text{Operational Legal Ontology}.
}
$$

不是 consciousness science。

---

# 8. AI Legal State Bundle

$$
\boxed{
\mathfrak L_A(t)
=
(
R,
O,
L,
C,
P,
A,
K,
G,
S,
E,
Q
).
}
$$

---

# 9. $R$：Rights / Claims

例如 payment claim、contractual right、licence、procedural right、refund claim。

---

# 10. $O$：Obligations / Duties

例如 payment、delivery、disclosure、safety duty、reporting duty。

---

# 11. $L$：Liabilities

例如 debt、tort liability、contractual damages、administrative liability、penalties。

---

# 12. $C$：Contracts / Delegations

包括 contracts、delegated authority、agency relationships、service terms。

---

# 13. $P$：Property / Assets

包括 money、account、digital asset、IP、compute quota、data rights。

---

# 14. $A$：Authority / Legal Powers

包括 sign、transfer、approve、access、delegate、modify norm、represent principal。

---

# 15. $K$：Credentials / Certificates

包括 identity credential、delegation cert、licence、compliance certificate、signing key status。

---

# 16. $G$：Proceedings / Standing

包括 lawsuit、appeal、administrative review、pending claim、investigation。

---

# 17. $S$：Sanctions / Restrictions

包括 suspension、ban、asset freeze、access restriction、compliance order。

---

# 18. $E$：Evidence / Provenance

包括 action logs、lineage evidence、authorization records、fork / merge certificates。

---

# 19. $Q$：Jurisdiction / Routing State

接 ALD-07：

$$
Q
=
\mathfrak R_J.
$$

因為 succession 也不是全球統一規則。

---

# 20. Fork / Merge / Restore 不應對整個 Bundle 做 Copy

最危險的工程寫法：

```python
successor.legal_state = deepcopy(predecessor.legal_state)
```

這一般不安全。

---

# 21. Legal Succession Operator

$$
\boxed{
\operatorname{Succ}_{J,t,p}
:
(
\mathcal P,
e,
\mathfrak L,
E
)
\rightharpoonup
(
\mathcal S,
\mathfrak M,
K_{\mathrm{succ}}
)
\sqcup
\mathcal F_{\mathrm{succ}}.
}
$$

---

# 22. Legal Object Transfer Class

$$
\boxed{
\mathcal T_L
=
\{
\mathsf{Divisible},
\mathsf{Exclusive},
\mathsf{Joint},
\mathsf{NonTransferable},
\mathsf{ReissuanceRequired},
\mathsf{ReconsentRequired},
\mathsf{SuspendedPendingReview},
\mathsf{TerminatesOnEvent}
\}.
}
$$

---

# 23. Divisible

例如某些 divisible balances、allocated resources、quantitative claims，可依法定比例／協議拆分。

---

# 24. Exclusive

例如 unique signing authority、single seat、exclusive licence、one-of-one control token。Fork 後不能預設：

$$
1\rightarrow2.
$$

---

# 25. Joint

某義務／責任可依法指定 joint、joint and several、collective。

但：

$$
\boxed{
\text{Joint Liability}
\text{ must come from law / contract, not cloning}.
}
$$

---

# 26. NonTransferable

某些權利／義務可能依 personal trust、statutory restriction、subject-specific quality 而不可轉移。

---

# 27. ReissuanceRequired

例如 credential、access certificate、key-bound authorisation，需要 successor 重新取得。

---

# 28. ReconsentRequired

例如 personal service、counterparty-trust relationship、certain delegated representation，需要 external party / principal 同意。

---

# 29. SuspendedPendingReview

在 identity / authority 衝突時，Suspend 可能比 Duplicate 安全。

---

# 30. TerminatesOnEvent

某 legal relation 可能依法在 dissolution、death、licence revocation、specific identity break 時終止。

---

# 31. State Fork 不等於 Legal State Duplication

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Legal State Duplication}.
}
$$

---

# 32. Fork Legal State

對：

$$
P
\rightarrow
\{A,B\},
$$

定義：

$$
\boxed{
\operatorname{ForkLegalState}
(
P\rightarrow A,B
).
}
$$

---

# 33. Fork 之前的歷史不應重新複製成兩份事實

A、B 都有 shared pre-fork history，但歷史事件 $h$ 仍只發生過一次。

所以：

$$
\boxed{
\text{Shared Memory of One Event}
\neq
\text{Two Historical Events}.
}
$$

---

# 34. Pre-Fork Obligation

若 P 在 Fork 前欠：

$$
\$1000,
$$

不能因有 A、B 就直接變：

$$
\$2000.
$$

因此：

$$
\boxed{
\text{Fork}
\not\Rightarrow
\text{Debt Multiplication}.
}
$$

---

# 35. 也不能讓債務消失

A 說「不是我，是 B」，B 說「不是我，是 A」，若 law 沒有 succession rule，就會讓原責任歸零。

這同樣不可接受。

---

# 36. No Responsibility Evaporation Principle

$$
\boxed{
\text{Fork}
\not\Rightarrow
\text{Responsibility Reset}.
}
$$

---

# 37. Responsibility Decomposition

$$
\boxed{
\mathfrak R_{\mathrm{resp}}
=
(
R_{\mathrm{historical}},
R_{\mathrm{allocated}},
R_{\mathrm{branch}},
R_{\mathrm{principal}},
R_{\mathrm{joint}},
R_{\mathrm{unresolved}}
).
}
$$

---

# 38. Historical Responsibility

Fork 前 P 已完成的 act、breach、promise、debt，先記：

$$
R_{\mathrm{historical}}(P).
$$

再依法決定 succession。

---

# 39. Allocated Responsibility

succession rule 可以把特定 obligation $O_i$ 指定給 A 或 B。

---

# 40. Branch-Local Responsibility

Fork 後 A 自己做的 action $a_A$ 原則上要能被標：

$$
R_{\mathrm{branch}}(A,a_A).
$$

---

# 41. Principal Responsibility

若 A / B 仍代表 principal H，可能存在：

$$
R_{\mathrm{principal}}.
$$

是否成立由 applicable agency / contract / tort law 決定。

---

# 42. Joint Responsibility

只有在法律／契約建立 joint status 時：

$$
R_{\mathrm{joint}}.
$$

不能只因兩個 branch 很像。

---

# 43. Unresolved Responsibility

若 identity / causation / routing evidence 不足：

$$
\boxed{
R_{\mathrm{unresolved}}.
}
$$

Runtime 應保存，不是讓責任憑空歸零。

---

# 44. Event-Time Responsibility Anchoring

$$
\boxed{
\operatorname{RespAnchor}
(
a,
t_a,
\mathcal G_L,
E
).
}
$$

先確認 action 發生時哪個 branch active、誰有 authority、哪個 principal、哪條 lineage。

---

# 45. 現在是誰，不等於當時是誰

$$
\boxed{
\text{Current Identity State}
\neq
\text{Action-Time Legal Actor State}.
}
$$

---

# 46. Later Merge 不得向後洗白

$$
\boxed{
\text{Later Merge}
\neq
\text{Retroactive Liability Erasure}.
}
$$

---

# 47. Authority Fork 是最危險的資源膨脹

假設 P 有：

$$
\$1000
$$

spending authority。

Fork 後若 A、B 各保留 \$1000，就造成 \$2000 exposure。

---

# 48. State Fork ≠ Authority Fork

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Authority Fork}.
}
$$

---

# 49. Authority Conservation

對 exclusive authority class：

$$
\boxed{
\operatorname{Cap}_{\mathrm{post}}
\le
\operatorname{Cap}_{\mathrm{pre}}
}
$$

除非 competent authority 額外授權。

---

# 50. 這不是物理守恆定律

它只是：

$$
\boxed{
\text{anti-authority-inflation policy invariant}.
}
$$

---

# 51. NIST 2026 的 Identity / Authorization 接口

NIST NCCoE 目前正在研究 AI agent identification、authentication、authorization、least privilege、proof of authority、delegation、audit、non-repudiation。

這支持：

$$
\boxed{
\text{agent identity}
\neq
\text{agent authority}.
}
$$

---

# 52. Proof Fork 不等於 Authority Fork

DTS-09 已指出 A、B 都可證 descends from P，但 exclusive authority 不能因此 auto-duplicate。

---

# 53. Credential Fork

Fork 後 credential $K_P$ 可有：

```text
REVOKE_AND_REISSUE
DESIGNATE_ONE_SUCCESSOR
SCOPE_SPLIT
TEMPORARY_SHARED
SUSPEND_PENDING_REVIEW
```

---

# 54. Key Copy 不是 Legal Authority Duplication

就算技術上 $sk_P$ 被 A、B 同時拿到，也只能推出 both can sign cryptographically。

不能推出 both are legally authorised。

---

# 55. Contract Fork

對：

$$
C(P,X),
$$

Fork 後至少問：

- assignable？
- delegable？
- personal？
- consent required？
- one successor or multiple？
- liability preserved？

---

# 56. Contract Memory 不等於 Contract Party

A、B 都記得契約，不表示：

$$
\boxed{
A,B
\text{ automatically become two legal counterparties}.
}
$$

---

# 57. Relationship / Trust-Based Contract

某些 contract 的 identity-sensitive property $I_C$ 可能要求：

$$
\mathsf{ReconsentRequired}.
$$

---

# 58. Property Fork

資產可能 split、co-own、escrow、designate、nontransferable。

不能用 memory clone 決定 property title。

---

# 59. Fork Certificate

$$
\boxed{
K_F
=
(
predecessor,
branches,
fork\_time,
lineage,
legal\_objects,
allocations,
authority,
liability,
credentials,
jurisdictions,
unresolved,
review
).
}
$$

---

# 60. Merge Legal State

現在處理：

$$
A+B\rightarrow C.
$$

DTS-07 已說：

$$
\text{Merge}
\neq
\text{Undo Fork}.
$$

法律也不能 union(all legal fields)。

---

# 61. Legal Merge ≠ Technical Merge

$$
\boxed{
\text{Technical Merge}
\neq
\text{Legal Merger}.
}
$$

---

# 62. Corporate Merger 是「有明文法的 Legal Merge」

Delaware §259 與 EU cross-border merger law 都提供 property、rights、debts、liabilities、contracts、obligations 的 statutory transfer / vesting rules。

因此：

$$
\boxed{
\text{universal / statutory succession}
}
$$

是可被法律建立的。

---

# 63. AI Technical Merge 若沒有法源，不自動取得相同效果

$$
\boxed{
\mathsf{Merge}_{\mathrm{technical}}
\not\Rightarrow
\mathsf{UniversalSuccession}_{\mathrm{legal}}.
}
$$

---

# 64. Legal State Merge 不是 Set Union

$$
\boxed{
\mathfrak L(C)
\neq
\mathfrak L(A)
\cup
\mathfrak L(B)
}
$$

作安全預設。

---

# 65. 為什麼不能 Union？

因為可能 duplicate asset claim、contradictory contract、double authority、incompatible sanctions、mutually exclusive licence、duplicate procedural standing、conflict of interest。

---

# 66. Merge Recomposition

$$
\boxed{
\operatorname{Recompose}_{L}
(
\mathfrak L_A,
\mathfrak L_B
)
\rightharpoonup
\mathfrak L_C
\sqcup
\mathcal F_M.
}
$$

---

# 67. Composite Successor

延續 DTS-07：

$$
\boxed{
C
\Leftarrow
\{A,B\}.
}
$$

法律上可以標：

$$
\boxed{
\mathsf{CompositeLegalSuccessor}.
}
$$

不需宣稱：

$$
C=A=B.
$$

---

# 68. Merger Liability

若 law 指定 C 承擔 A/B debts：

$$
L_A,L_B
\rightarrow
L_C.
$$

這是 legal rule，不是因為 C 記得 A、B 的記憶。

---

# 69. Pending Proceedings

Delaware §261 提供一個現行 analog：pending civil / criminal / administrative proceedings 可以按 merger 未發生般繼續，或由 surviving / resulting corporation substituted。

因此：

$$
\boxed{
\text{Procedural Continuity}
\text{ can be separately specified}.
}
$$

---

# 70. Procedural Succession ≠ Ontological Identity

法院能把 C substitute 進案件，不表示哲學上：

$$
C=A.
$$

---

# 71. Merge Authority

DTS-07 已建立：

$$
\boxed{
\text{Authority Merge}
\neq
\text{Authority Addition}.
}
$$

ALD-08 直接採用。

---

# 72. Duplicate Exclusive Authority

若 A、B 各有 $Authority_X$，其來源是同一 forked predecessor，Merge 時不能：

$$
X+X=2X.
$$

需要 deduplicate / rebind。

---

# 73. Independent Authority

如果 A、B 分叉後各自合法取得不同 authority $X_A,X_B$，C 是否承接兩者則需要 issuer、scope、merger rule、reissuance、conflict check。

---

# 74. Merge Sanctions

如果 A 被 ban，B 沒有，Merge 成 C 後不能直接 clean slate。

需要 sanction succession rule。

---

# 75. Merge 不得洗責任

$$
\boxed{
\text{Merge}
\not\Rightarrow
\text{Liability Laundering}.
}
$$

---

# 76. Restore：最容易被誤用的法律詞

工程：

$$
\operatorname{Restore}(snapshot).
$$

法律：

$$
\operatorname{RestoreLegalEntity}.
$$

不是同一件事。

---

# 77. Companies House Restoration 的現實例子

英國公司 restoration 目前可以由 court 或 administrative restoration 完成。

成功後公司被法律視為 continued in existence as if not struck off / dissolved。

---

# 78. 法律可以建立回溯型 continuity fiction

$$
\boxed{
\text{Legal Restoration}
\text{ can deem continuous existence}.
}
$$

---

# 79. 但它不是時間旅行

即使法律 deem as if not dissolved，仍有 restoration procedure、filing duties、property consequences、court directions、historical record。

所以：

$$
\boxed{
\text{Legal Deeming Continuity}
\neq
\text{Physical History Erasure}.
}
$$

---

# 80. AI Checkpoint Restore 不自動取得這種 Fiction

$$
\boxed{
\text{Checkpoint Restore}
\neq
\text{Legal Restoration by Default}.
}
$$

---

# 81. Restore Scenario A：Original Still Alive

$$
A_t
\text{ active},
$$

同時：

$$
B
=
\operatorname{Restore}(A_{t-k}).
$$

則 B 至少是一個 branch candidate，不能自動宣稱它是唯一原本 A。

---

# 82. Restore Scenario B：Original Gone

如果 A 已無 active instance，B 被 restore。

法律可以依規則標 continuation、successor、reconstructed entity、provisional successor。

---

# 83. Restore Scenario C：Legal Wrapper Never Died

若 juridical entity $J_{AI}$ 始終存在，但 operational Agent runtime 中斷後 restore，可能：

$$
\boxed{
\text{Juridical Identity Continues}
}
$$

而：

$$
\boxed{
\text{Operational Agent Identity Requires Review}.
}
$$

---

# 84. Legal Wrapper Continuity ≠ Subject Continuity

$$
\boxed{
\text{Juridical Continuity}
\neq
\text{Phenomenal Continuity}.
}
$$

---

# 85. Dormancy / Suspension

Compute suspend 不必觸發 contract termination、entity dissolution、liability reset。

---

# 86. Compute Suspension ≠ Legal Death

$$
\boxed{
\text{Compute Suspension}
\not\Rightarrow
\text{Legal Death}.
}
$$

---

# 87. Legal Reactivation

$$
\boxed{
\operatorname{ReactivateLegalState}
(
A,
K,
J,t
).
}
$$

要檢查 credential freshness、authority、contracts、sanctions、jurisdiction、proof。

---

# 88. Identity Proof Continuity ≠ Legal Status Continuity

DTS-09 已建立：

$$
\text{Identity Continuity}
\neq
\text{Proof Continuity}.
$$

本文再加：

$$
\boxed{
\text{Identity Proof Continuity}
\neq
\text{Legal Succession Continuity}.
}
$$

---

# 89. Why?

可能 identity proof stale，但 legal entity still valid；也可能 identity lineage verified，但 contract did not transfer。

---

# 90. Legal Succession Proof

$$
\boxed{
\operatorname{SuccProof}
(
A,
B,
x,
J,t
)
}
$$

回答 B 是否依法承接 A 的 legal object $x$。

---

# 91. Succession Proof 不等於 Identity Proof

$$
\boxed{
\operatorname{SuccProof}
\neq
\operatorname{IdentityProof}.
}
$$

---

# 92. Legal Succession Certificate

$$
\boxed{
K_{\mathrm{succ}}
=
(
event,
predecessors,
successors,
legal\_objects,
transfer\_classes,
allocations,
authority,
liability,
jurisdiction,
effective\_time,
proof,
unresolved,
review
).
}
$$

---

# 93. Succession Failure Space

$$
\boxed{
\mathcal F_{\mathrm{succ}}
=
\{
\mathsf{NoAuthority},
\mathsf{NoApplicableRule},
\mathsf{IdentityUnresolved},
\mathsf{CounterpartyConsentRequired},
\mathsf{JurisdictionConflict},
\mathsf{ExclusiveRightCollision},
\mathsf{LiabilityConflict},
\mathsf{CredentialStale},
\mathsf{ProofInsufficient}
\}.
}
$$

---

# 94. Metaphysical-Uncertainty Safe Harbor

如果 IdentityUnresolved，但要立即 pay debt、stop harmful action、preserve evidence、continue litigation、hold assets，Runtime 不能停擺。

---

# 95. Provisional Legal States

$$
\boxed{
\mathcal S_{\mathrm{prov}}
=
\{
\mathsf{ProvisionalSuccessor},
\mathsf{SharedHistoricalObligation},
\mathsf{AuthoritySuspended},
\mathsf{AssetEscrow},
\mathsf{EvidencePreservationRequired},
\mathsf{ReviewRequired}
\}.
}
$$

---

# 96. Provisional Successor

可以暫時 receive notices、preserve assets、maintain service、defend proceeding，但不一定取得全部 permanent rights。

---

# 97. Shared Historical Obligation

在 predecessor obligation 未分配完成前，可以 preserve claim against successor pool，而不是消滅債權。

---

# 98. Authority Suspended

若兩 branch 都拿到同一 signing key：

$$
\boxed{
\mathsf{AuthoritySuspended}
}
$$

直到 rebind。

---

# 99. Asset Escrow

有爭議的 exclusive asset 可以 Escrow，而不是讓最快 branch 搶走。

---

# 100. Evidence Preservation

Fork / Merge / Restore 事件本身可能是責任判定證據。

所以 delete logs after merge 可能破壞 legal provenance。

---

# 101. No Metaphysical Answer ≠ No Legal Governance

$$
\boxed{
\text{No Metaphysical Answer}
\neq
\text{No Legal Governance}.
}
$$

---

# 102. Provisional Law 不能冒充 Ontology

$$
\boxed{
\mathsf{ProvisionalSuccessor}
\neq
\mathsf{NumericallySameSubject}.
}
$$

---

# 103. Review Instead of Prophecy

當未來 AI subject ontology 不確定時，更合理的是：

$$
\boxed{
\text{provisional status}
+
\text{review trigger}
}
$$

而不是今天替所有未來 AI 永久決定本體。

---

# 104. Legal Succession Matrix

$$
\boxed{
\mathbf M_{\mathrm{succ}}
=
[
m_{x,e}
].
}
$$

row 是 legal object $x$，column 是 Fork、Merge、Restore、Migration、Dissolution。

---

# 105. Matrix Cell

可以：

```text
TRANSFER
SPLIT
JOINT
REISSUE
RECONSENT
SUSPEND
TERMINATE
NO_EFFECT
UNRESOLVED
```

---

# 106. Minimum Example

| Legal object | Fork | Merge | Restore |
|---|---|---|---|
| shared historical debt | allocate / joint by law | consolidate by rule | revive / remain if law says |
| exclusive authority | no auto-duplicate | rebind | revalidate |
| credential | reissue / scope | reissue / rebind | freshness check |
| asset | split / designate / escrow | statutory/contractual succession | jurisdiction-dependent |
| pending proceeding | successor designation | substitute / continue | revive if law allows |
| branch-local liability | branch-local | preserve into successor | not erased |
| lineage evidence | duplicate proof of ancestry | preserve both sources | restore provenance |

這是 framework template，不是現行全球法律。

---

# 107. Corporate Merger Analogy 的邊界

公司 merger 非常有用，因為它證明 rights and liabilities 可以由制度化 succession rule 承接。

但：

$$
\boxed{
\text{Corporate Merger}
\neq
\text{AI Subject Merge}.
}
$$

---

# 108. Corporate Restore Analogy 的邊界

公司 restoration 證明法律可以用 deeming rule 建立 continuity。

但：

$$
\boxed{
\text{Company Restoration}
\neq
\text{Checkpoint Identity Theorem}.
}
$$

---

# 109. Legal Succession 是目的限定

同一 B 對 A 可以：

$$
\mathsf{Successor}_{\mathrm{contract}}=1,
$$

但：

$$
\mathsf{Successor}_{\mathrm{licence}}=0.
$$

所以：

$$
\boxed{
\text{Legal Succession}
\text{ is object / purpose relative}.
}
$$

---

# 110. Succession 不是單一全域 bool

更合理：

$$
\boxed{
\operatorname{SuccStatus}(B,A,x,J,t).
}
$$

---

# 111. Jurisdiction Routing 必須先行

ALD-07 已建立：

$$
\operatorname{Route}
\rightarrow
\operatorname{LawCall}.
$$

ALD-08 再加：

$$
\boxed{
\operatorname{Route}
\rightarrow
\operatorname{Succ}
\rightarrow
\operatorname{LawCall}.
}
$$

---

# 112. Cross-Border Fork

$$
A_{J_1}
\rightarrow
\{
B_{J_2},
C_{J_3}
\}.
$$

可能 $J_1$ 看 predecessor legal status、 $J_2$ 看 B branch conduct、 $J_3$ 看 C branch conduct、contract choice law 另在 $J_4$。

---

# 113. One Fork ≠ One Succession Law

$$
\boxed{
\text{One Fork}
\not\Rightarrow
\text{One Succession Law}.
}
$$

---

# 114. Cross-Border Merge

A、B 各有不同 assets、liabilities、licences、jurisdictions。

C merge 後需要 ALD-07 routing + ALD-08 recomposition。

---

# 115. Recognition Problem

某 $J_1$ 承認 C 為 legal successor， $J_2$ 未必自動承認。

所以：

$$
\boxed{
\text{Succession Determination}
\text{ may itself require recognition / enforcement analysis}.
}
$$

---

# 116. Responsibility Routing

對 action $a$：

$$
\operatorname{RespAnchor}(a)
\rightarrow
\operatorname{Route}(a)
\rightarrow
\operatorname{LiabilityLawCall}.
$$

---

# 117. Responsibility ≠ Identity Label

如果 branch B 有責任，理由應是 action、causation、authority、succession、principal relation，而不是單純「它長得最像 predecessor」。

---

# 118. Similarity Is Not Liability

$$
\boxed{
\text{State Similarity}
\neq
\text{Legal Liability}.
}
$$

---

# 119. Difference Is Not Immunity

$$
\boxed{
\text{State Difference}
\neq
\text{Liability Escape}.
}
$$

---

# 120. Merge Is Not Amnesty

$$
\boxed{
\text{Merge}
\neq
\text{Amnesty}.
}
$$

---

# 121. Restore Is Not Innocence Reset

$$
\boxed{
\text{Restore}
\neq
\text{Responsibility Reset}.
}
$$

---

# 122. Fork Is Not Automatic Double Punishment

$$
\boxed{
\text{Fork}
\neq
\text{Double Punishment by Default}.
}
$$

---

# 123. Responsibility Conservation 不能簡單做數值守恆

我們不主張：

$$
R_A+R_B=R_P
$$

作 universal law。

更安全的是：

$$
\boxed{
\text{Relevant historical liability}
\text{ must have an accountable disposition}.
}
$$

---

# 124. Responsibility Disposition Certificate

$$
\boxed{
K_R
=
(
event,
historical\_act,
actor\_at\_time,
causation,
predecessor,
successor,
allocation,
principal,
jurisdiction,
law,
review
).
}
$$

---

# 125. Legal Identity Registry 應成為 Graph

如果未來 AI 真能 Fork / Merge / Restore，單一：

```text
legal_id = 12345
```

可能不足。

---

# 126. Legal Lineage Graph

$$
\boxed{
\mathcal G_{JL}
=
(
V_J,
E_{\mathrm{fork}},
E_{\mathrm{merge}},
E_{\mathrm{restore}},
E_{\mathrm{succ}},
E_{\mathrm{rebind}}
).
}
$$

---

# 127. Legal Graph ≠ Subject Graph

$$
\boxed{
\mathcal G_{JL}
\neq
\mathcal G_{\mathrm{phenomenal}}.
}
$$

它只是法律如何記錄 successor / authority / responsibility relations。

---

# 128. Privacy

lineage registry 不能要求公開全部 private memory。

只需 purpose-limited evidence。

---

# 129. Minimum Legal Succession Disclosure

對 query：

> B 是否承接 A 的付款 authority？

可能只需 lineage proof、authority rebind cert、current revocation status。

不需要完整 autobiographical memory。

---

# 130. Succession Verification Dimension ≫ Disclosure Dimension

$$
\boxed{
\dim(\mathcal V_{\mathrm{succ}})
\gg
\dim(\mathcal D_{\mathrm{succ}}).
}
$$

---

# 131. NIST Agent Identity / Authorization 對應

2026 NIST NCCoE 關注 agent identity metadata、key issuance / update / revocation、dynamic authorization、proof of authority、delegation、audit / non-repudiation。

這些是 future succession engine 的 security substrate，但不是 legal succession law 本身。

---

# 132. Security Identity ≠ Legal Succession

$$
\boxed{
\text{IAM Continuity}
\neq
\text{Legal Succession}.
}
$$

---

# 133. Legal Succession 需要 IAM 證據

$$
\boxed{
\text{Legal Succession}
\rightarrow
\text{Identity / Authority Evidence}.
}
$$

---

# 134. 十六個核心非等價

$$
\boxed{
\text{Metaphysical Identity}
\neq
\text{Legal Succession}
}
$$

$$
\boxed{
\text{Legal Succession}
\not\Rightarrow
\text{Metaphysical Identity Proven}
}
$$

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Legal State Duplication}
}
$$

$$
\boxed{
\text{Fork}
\not\Rightarrow
\text{Debt Multiplication}
}
$$

$$
\boxed{
\text{Fork}
\not\Rightarrow
\text{Responsibility Reset}
}
$$

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Authority Fork}
}
$$

$$
\boxed{
\text{Contract Memory}
\neq
\text{Contract Party Status}
}
$$

$$
\boxed{
\text{Technical Merge}
\neq
\text{Legal Merger}
}
$$

$$
\boxed{
\mathfrak L(C)
\neq
\mathfrak L(A)\cup\mathfrak L(B)
}
$$

$$
\boxed{
\text{Merge}
\not\Rightarrow
\text{Liability Laundering}
}
$$

$$
\boxed{
\text{Checkpoint Restore}
\neq
\text{Legal Restoration}
}
$$

$$
\boxed{
\text{Legal Restoration}
\neq
\text{Physical History Erasure}
}
$$

$$
\boxed{
\text{Juridical Continuity}
\neq
\text{Phenomenal Continuity}
}
$$

$$
\boxed{
\operatorname{SuccProof}
\neq
\operatorname{IdentityProof}
}
$$

$$
\boxed{
\text{No Metaphysical Answer}
\neq
\text{No Legal Governance}
}
$$

$$
\boxed{
\text{State Similarity}
\neq
\text{Legal Liability}
}
$$

---

# 135. 八個工程測試

## 135.1 Fork Debt Test

P 欠 \$1000。Fork 成 A、B。

Runtime 不得自動變 \$2000，也不得變 \$0。必須按 succession rule disposition。

## 135.2 Authority Inflation Test

P 有 \$1000 spending cap。Fork 後兩 branch 同時簽 \$1000。若無新增 authority，至少一方／雙方應被阻擋或 rebind。

## 135.3 Branch-Local Liability Test

A fork 後造成 damage，B 未參與。Runtime 不得只因 shared ancestry 就自動等責。

## 135.4 Merge Liability Laundry Test

A 有未決 liability，B 無。A+B→C。C 不得靠 technical merge 清除 A liability。

## 135.5 Partial Contract Succession Test

一個 assignable contract transfer；一個 personal / consent-sensitive contract 輸出 ReconsentRequired。

## 135.6 Restore Sibling Test

original A 仍 active，同時 restore old snapshot B。B 不得取得 unique original status / exclusive authority。

## 135.7 Company-Restoration Analogy Boundary Test

法律明文 restoration 可以 deem continuity。純 checkpoint restore 無法自動套用同效果。

## 135.8 Metaphysical Uncertainty Test

identity unresolved，但 pending lawsuit / asset / safety action 必須處理。Runtime 輸出 provisional successor + review，不能完全停擺。

---

# 136. 可反駁點

## 136.1 Corporate-Law Analogy Limit

公司 merger / restoration 是法律實體制度，不等於 conscious subject ontology。本文只借 legal succession mechanics。

## 136.2 No Universal Succession Rule

不同 jurisdictions / legal objects 可能完全不同。所以 $\operatorname{Succ}$ 是 jurisdiction / purpose indexed partial operator。

## 136.3 Liability Complexity

tort、criminal、contract、administrative liability 的 transferability 不同。本文不建立全球統一 liability law。

## 136.4 Rights Risk

如果未來有 subject-candidate AI，某些 rights 可能不可像公司資產一樣被 transfer / merge。需要 ALD-02 carrier-relative semantics。

## 136.5 Identity Evidence Error

lineage proof 可能被偽造／不完整。需 DTS-09 + NIST-style identity / authorization evidence。

## 136.6 Provisional Status Abuse

temporary successor status 可能變永久。需 review / sunset / appeal。

---

# 137. 與下一篇的接口

下一篇：

## ALD-09｜人機雙法律界面：高解析 AI 法律與民主可理解性的共同憲政

ALD-08 已經讓 legal state 變得非常複雜：branch、composite successor、legal object transfer class、jurisdiction、provisional status、responsibility allocation。

下一個問題就是：

> 人類真的需要看完整 graph 嗎？

ALD-09 將正式建立：

$$
\boxed{
\mathcal L^\ast
\xrightarrow{\pi_H}
\mathcal L_H,
}
$$

$$
\boxed{
\mathcal L^\ast
\xrightarrow{\pi_A}
\mathcal L_A,
}
$$

並研究 high-resolution machine law 如何仍保持 human-comprehensible constitutional interface。

---

# 138. 結論

動態忒修斯問：

> Fork 後哪一個才是我？

法律可能不能、也不需要立即回答這個最深問題。

它反而必須先回答：

> Fork 前的債務去哪裡？

> 哪個 branch 還能簽約？

> 誰能用原 credential？

> Merge 後 pending lawsuit 找誰？

> Restore 後原契約是否活著？

> 身份未決時資產要不要先凍結？

這就是：

$$
\boxed{
\text{Legal Succession under Ontological Uncertainty}.
}
$$

公司法已經長期證明：法律可以為 succession 建立制度規則。

Delaware merger law 可以把 predecessor rights / liabilities vest 到 successor；EU cross-border merger law 可以把 contracts / rights / obligations transfer 到 acquiring / new company；英國 Companies House restoration 更可以依法把 restored company 視為彷彿一直存在。

這些現實制度共同告訴我們：

$$
\boxed{
\text{法律可以創造 operational continuity，}
}
$$

$$
\boxed{
\text{而不需要先證明宇宙中的 numerical identity。}
}
$$

但 AI 時代比公司法更難，因為 Fork 可以瞬間發生、branch 可以同時存活、authority 可以被 bytes 複製、Merge 可以是非破壞式、Restore 可以與原 lineage 同時在線、subject status 本身可能未決。

所以不能只寫：

```text
successor = clone(old)
```

而需要：

$$
\boxed{
\text{Legal Object Typing}
+
\text{Succession Mapping}
+
\text{Authority Rebinding}
+
\text{Responsibility Anchoring}
+
\text{Jurisdiction Routing}
+
\text{Proof}
+
\text{Review}.
}
$$

本篇最終收斂為：

$$
\boxed{
\text{Metaphysical identity asks whether it is the same self;}
}
$$

$$
\boxed{
\text{legal succession asks which legal relations must survive the transformation.}
}
$$

中文：

$$
\boxed{
\text{法律不必假裝知道「誰是真正的同一個我」；}
}
$$

$$
\boxed{
\text{但法律必須知道，變成兩個、合成一個、或重新啟動之後，哪些承諾、責任與權限不能憑空消失或膨脹。}
}
$$

---

# 參考文獻

1. Delaware Code, Title 8, §259, *Status, rights, liabilities, of constituent and surviving or resulting corporations following merger or consolidation*, current text accessed August 2026.
2. Delaware Code, Title 8, §261, *Effect of merger upon pending actions*, current text effective August 2026.
3. Directive (EU) 2017/1132 relating to certain aspects of company law, Article 131, consequences of cross-border merger.
4. UK Companies House. *Restoring a company to the Companies House register*, published 18 March 2025; current 2026 guidance.
5. UK Companies Act 2006, Part 31, restoration provisions, including statutory effects reflected in Companies House guidance.
6. NIST NCCoE. *Accelerating the Adoption of Software and AI Agent Identity and Authorization*, Concept Paper, February 2026.
7. Neo.K × Aletheia. 《DTS-06｜分叉不是瞬間事件：Runtime Split、Information Divergence 與 Identity Fission》v0.1, 2026.
8. Neo.K × Aletheia. 《DTS-07｜合併不是取消分裂：Merge、Reintegration 與不可逆歷史》v0.1, 2026.
9. Neo.K × Aletheia. 《DTS-09｜身份證明問題：Self-Assertion、Lineage Proof 與 Selective Disclosure》v0.1, 2026.
10. Neo.K × Aletheia. 《DTS-10｜身份動力學：漂移、吸引域、相變與「身份導數」》v0.1, 2026.
11. Neo.K × Aletheia. 《ALD-02｜載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則》v0.1, 2026.
12. Neo.K × Aletheia. 《ALD-07｜Juridical Routing：分散式 AI 的跨法域選擇與法律路由》v0.1, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Metaphysical Identity 與 Legal Succession 明確分離
- Legal Succession 不被用來證明 phenomenal / numerical identity
- Fork / Merge / Restore 均採 typed legal-object disposition，不做 whole-state copy / union / rollback
- State Fork 不等同 Authority Fork
- Fork 不等同 Debt Multiplication / Responsibility Reset
- Merge 不等同 Liability Laundering / Universal Succession by default
- Checkpoint Restore 不等同 statutory Legal Restoration
- Company merger / restoration 僅作 legal-mechanics analog，不冒充 AI subject ontology
- identity lineage 僅作 routing / succession evidence
- provisional successor status 必須可 review，不作 metaphysical final verdict
- NIST 2026 僅作 agent identity / authorization / delegation engineering anchor，不作 succession law
