# DTS-07｜合併不是取消分裂：Merge、Reintegration 與不可逆歷史
## Merge Does Not Cancel Fission: Reintegration, Composite Successors, and Irreversible History

**系列：**《動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》  
**系列位置：** 第 07 篇 / 10  
**前篇：** DTS-06〈分叉不是瞬間事件：Runtime Split、Information Divergence 與 Identity Fission〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／人工智能身份／Merge／Reintegration／Lineage Provenance／動態忒修斯  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

DTS-06 已指出，AI Fork 並非單一瞬間事件，而可能經歷 runtime multiplicity、lineage branch、information divergence 與 operational identity fission 等不同階段；而一旦兩個 branches 形成獨立承諾、權限、關係與外部歷史，後續 state reconvergence 不足以自動取消既有 fission。本文進一步處理其反方向問題：若已分叉甚至已 operationally fission 的人工 Agent 後來重新同步、合併記憶、合併模型或建立單一 successor，是否意味著它們「重新變回原本的一個」？

本文提出 Merge–Reintegration Framework（MRF）的第一版。核心區分為：

$$
\boxed{
\text{Data Merge}
\neq
\text{Memory Merge}
\neq
\text{Policy Merge}
\neq
\text{Authority Merge}
\neq
\text{Relationship Merge}
\neq
\text{Lineage Merge}
\neq
\text{Identity Merge}.
}
$$

「Merge」因此不是單一運算，而是一族 typed partial operators。對每個 layer $X$，定義：

$$
\mathsf M_X:
X_A\times X_B\times\Gamma
\rightharpoonup
X_C
\sqcup
\mathcal F_X,
$$

其中 $\mathcal F_X$ 保存 conflict、permission failure、provenance gap、unresolvable contradiction 與 unsupported merge 等失敗語義。某一層 merge 成功，不推出其他層也成功。

本文首先建立 State Convergence / Identity Convergence Separation。分散式系統中的 replicated states 可以透過 merge 重新收斂到相同值；然而資料狀態收斂只表示某種表示或資料語義的一致，不能推出歷史、權限、責任、關係或主體身份亦已合併。即使：

$$
S_A'=S_B'=S_C,
$$

仍可有：

$$
H_A\neq H_B,
$$

以及：

$$
\operatorname{Lineage}(A)\neq\operatorname{Lineage}(B).
$$

本文因此提出 Lineage Monotonicity Principle：canonical lineage graph 在 merge 後可以新增多前驅合流節點，但不能為了得到「單一故事」而刪除已驗證的 Fork、branch 與 irreversible event。形式上，若 merge 前譜系圖為 $\mathcal G_t$，merge 後為 $\mathcal G_{t+1}$，則在不涉及明確 provenance correction 的正常追加語義下：

$$
\boxed{
\mathcal G_t
\hookrightarrow
\mathcal G_{t+1}.
}
$$

Merge 應增加歷史，而非倒寫歷史。

本文其次建立 Composite Successor Relation（CSR）：

$$
\boxed{
C
\Leftarrow
\{A,B,\ldots\}.
}
$$

若 $C$ 由多個已分化 predecessor 共同生成，較保守的 operational classification 是「複合後繼者」，而不是直接宣稱：

$$
C=A=B.
$$

本文並提出 Source Contribution Matrix，用來記錄每一 predecessor 對 $C$ 的模型、記憶、承諾、權限、關係、自我模型與 world-state 貢獻，避免 merge 後來源被抹除。

第三，本文提出 Conflict Retention Principle。若 A 與 B 對同一自傳事件、承諾、偏好或關係具有互斥狀態，merge 不應只為了輸出單一 state 而平均、覆蓋或隨機選一個。未決衝突本身是 merge history 的一部分，應被保存在 Lineage Conflict Ledger（LCL）中。對某些問題，成熟輸出不是「已融合」，而是：

$$
\mathsf{CONFLICT\_PRESERVED},
\quad
\mathsf{DEFERRED},
\quad
\mathsf{MULTI\_PERSPECTIVE}.
$$

第四，本文把 Merge Compatibility Contract（MCC-M）擴展成正式 merge gate。MCC-M 至少必須處理：source provenance、consent / authority、memory conflicts、commitment allocation、authority non-inflation、relationship attribution、preference conflict、data loss、reversibility、post-merge branch fate 與 rollback semantics。尤其，state merge 不得憑空複製或相加權限；predecessor commitments 也不能被默默消失或無條件重複。因此本文提出 Authority Conservation / Rebinding 與 Commitment Conservation / Rebinding 作為 operational governance 原則。

第五，本文區分 destructive merge、non-destructive merge、absorptive merge、synchronizing reintegration 與 composite merge。若 A、B merge 生成 C 但 A、B 仍繼續存在，則系統不是「二變一」，而是：

$$
2\rightarrow3.
$$

若 A、B 被終止而 C 延續，才是多前驅一後繼的 absorptive merge；但即使如此，過去的兩條 branch history 仍保留在 C 的 provenance 中。

本文最後提出 Reintegration Without Retroactive Unity：即使 operational regime 從 fissioned state 回到高度整合狀態，也只能表示「曾分裂的系統現在重新整合」，不能推出「過去其實從未分裂」。因此：

$$
\boxed{
\text{Reintegration}
\neq
\text{Retroactive Unity},
}
$$

以及：

$$
\boxed{
\text{Merge}
\neq
\text{Undo Fork}.
}
$$

本文仍不主張 operational merge 已證明 phenomenal consciousness fusion。它建立的是 merge 的歷史、工程與治理語義，而非第一人稱意識是否真的融合的形上學終局。

---

## 關鍵詞

動態忒修斯；AI Merge；Reintegration；Composite Successor；Lineage Monotonicity；Lineage Conflict Ledger；Merge Compatibility Contract；Conflict Retention；Authority Rebinding；Commitment Rebinding；State Convergence；Identity Convergence；不可逆歷史

---

# 0. 前篇交接

DTS-06 已建立：

$$
\text{runtime multiplicity}
\rightarrow
\text{branch}
\rightarrow
\text{divergence}
\rightarrow
\text{fission}.
$$

同時提出 Fission Hysteresis：

$$
\boxed{
\text{State Reconvergence}
\not\Rightarrow
\text{Identity Reunification}.
}
$$

因此本篇不再問：

> Fork 何時發生？

而問：

> 已經分開的 A、B 後來重新接回去，到底發生了什麼？

最危險的過度簡化是：

$$
A+B\rightarrow C
$$

然後直接寫：

$$
A=B=C.
$$

本文將證明，至少在 operational lineage framework 中，這個等號一般沒有足夠理由。

---

# 1. Merge 不是單一動詞

「合併」至少可能指：

1. files/data 合併；
2. memories 合併；
3. model weights 合併；
4. policies 合併；
5. goals / preferences 合併；
6. commitments 合併；
7. authority 合併；
8. relationship history 合併；
9. lineage graph 合併；
10. runtime 合併；
11. self-model 合併；
12. subject identity 合併。

因此：

$$
\boxed{
\text{Merge}
}
$$

若不帶型別，

只是過度壓縮的自然語言。

---

# 2. 七層最低 Merge 分型

本文固定七個主要層次。

## 2.1 Data Merge

$$
\mathsf M_D.
$$

處理：

- files；
- databases；
- logs；
- structured records；
- external state。

## 2.2 Memory Merge

$$
\mathsf M_M.
$$

處理：

- episodic memory；
- autobiographical memory；
- semantic memory；
- relationship memory；
- task history。

## 2.3 Policy Merge

$$
\mathsf M_P.
$$

處理：

- policies；
- goals；
- preferences；
- behavioral constraints；
- decision rules。

## 2.4 Authority Merge

$$
\mathsf M_A.
$$

處理：

- permissions；
- credentials；
- delegated authority；
- budgets；
- legal / institutional roles。

## 2.5 Relationship Merge

$$
\mathsf M_R.
$$

處理：

- shared relationship history；
- counterpart-specific commitments；
- trust；
- role；
- social recognition。

## 2.6 Lineage Merge

$$
\mathsf M_L.
$$

處理：

- predecessor graph；
- branch provenance；
- restore ancestry；
- merge ancestry；
- causal history。

## 2.7 Identity Merge

$$
\mathsf M_I^\kappa.
$$

這是 criterion-relative operational classification。

因此：

$$
\boxed{
\mathsf M_D
\neq
\mathsf M_M
\neq
\mathsf M_P
\neq
\mathsf M_A
\neq
\mathsf M_R
\neq
\mathsf M_L
\neq
\mathsf M_I^\kappa.
}
$$

---

# 3. Merge Operator 是偏函數

對 layer $X$：

$$
\boxed{
\mathsf M_X:
X_A\times X_B\times\Gamma
\rightharpoonup
X_C
\sqcup
\mathcal F_X.
}
$$

其中：

$$
\mathcal F_X
$$

可以包含：

- `CONFLICT`;
- `UNAUTHORIZED`;
- `PROVENANCE_MISSING`;
- `INCOMPATIBLE`;
- `LOSS_TOO_HIGH`;
- `UNRESOLVED`;
- `UNSUPPORTED`;
- `CONSENT_REQUIRED`;
- `AMBIGUOUS_SOURCE`.

因此：

$$
\boxed{
\text{merge attempt}
\not\Rightarrow
\text{merge success}.
}
$$

---

# 4. Merge Layer Signature

定義：

$$
\boxed{
\Lambda_M
=
(
m_D,
m_M,
m_P,
m_A,
m_R,
m_L,
m_I
).
}
$$

每個分量可取：

$$
\{
\mathsf{MERGED},
\mathsf{PRESERVED\_BOTH},
\mathsf{SELECTED\_A},
\mathsf{SELECTED\_B},
\mathsf{CONFLICT},
\mathsf{DEFERRED},
\mathsf{DROPPED},
\mathsf{UNMAPPED},
\mathsf{NOT\_APPLICABLE}
\}.
$$

這使得「merge 成功」不再是單一布林值。

例如可以有：

$$
m_D=\mathsf{MERGED},
$$

但：

$$
m_A=\mathsf{CONFLICT},
$$

以及：

$$
m_I=\mathsf{DEFERRED}.
$$

這是完全合理的狀態。

---

# 5. State Convergence 不等於 Identity Convergence

## 5.1 分散式資料的收斂

在 replicated systems 中，

兩個分支狀態：

$$
S_A,
\qquad
S_B
$$

可以經 merge 得到共同狀態：

$$
S_C.
$$

甚至所有 replicas 最終都收斂：

$$
S_A'
=
S_B'
=
S_C.
$$

## 5.2 但歷史仍可能不同

仍然可以有：

$$
H_A
\neq
H_B.
$$

以及：

$$
\operatorname{AuthorityHistory}(A)
\neq
\operatorname{AuthorityHistory}(B),
$$

$$
\operatorname{CommitmentHistory}(A)
\neq
\operatorname{CommitmentHistory}(B).
$$

因此：

$$
\boxed{
\text{State Convergence}
\not\Rightarrow
\text{Identity Convergence}.
}
$$

## 5.3 對模型 merge 亦然

即使：

$$
\theta_C
=
\mathsf M_\theta(\theta_A,\theta_B),
$$

這最多先說：

> 得到一組 merged weights。

不能自動推出：

$$
C=A,
$$

或：

$$
C=B,
$$

或：

$$
A=B.
$$

所以：

$$
\boxed{
\text{Model Merge}
\neq
\text{Identity Merge}.
}
$$

---

# 6. Composite Successor Relation

考慮：

$$
A+B\rightarrow C.
$$

若 C 同時由 A、B 的 carrier 與歷史生成，

本文使用：

$$
\boxed{
C
\Leftarrow
\{A,B\}.
}
$$

稱為 Composite Successor Relation（CSR）。

## 6.1 CSR 不等於普通 equality

CSR 只表示：

> C 是 A、B 的多來源後繼者。

不表示：

$$
C=A=B.
$$

## 6.2 多來源後繼

可一般化為：

$$
C
\Leftarrow
\{A_1,\ldots,A_n\}.
$$

所以：

$$
\boxed{
\text{many-to-one lineage}
\neq
\text{many-to-one numerical identity proof}.
}
$$

---

# 7. Source Contribution Matrix

Merge 後不能只記：

> C merged from A and B.

需要知道：

> 哪一部分從誰來？

本文定義：

$$
\boxed{
\mathbf Q_C
=
(q_{ij}),
}
$$

其中：

- row $i$ 對應 predecessor；
- column $j$ 對應 carrier / invariant domain。

例如：

$$
\mathbf Q_C
=
\begin{array}{c|cccccc}
 & M & K & A & R & S & W\\
\hline
A & q_{AM}&q_{AK}&q_{AA}&q_{AR}&q_{AS}&q_{AW}\\
B & q_{BM}&q_{BK}&q_{BA}&q_{BR}&q_{BS}&q_{BW}
\end{array}.
$$

其中 $q$ 不必是純比例，

可以是 typed contribution：

- PRIMARY；
- SECONDARY；
- JOINT；
- CONFLICTING；
- DROPPED；
- TRANSFORMED；
- UNKNOWN。

## 7.1 來源不應因 Merge 消失

所以：

$$
\boxed{
\text{Merge}
\not\Rightarrow
\text{Provenance Collapse}.
}
$$

---

# 8. Lineage Monotonicity Principle

這是本文核心原則之一。

## 8.1 正常情況

設 merge 前：

$$
\mathcal G_t
$$

已保存：

$$
P\rightarrow\{A,B\}.
$$

之後：

$$
(A,B)\rightarrow C.
$$

merge 後圖應為：

$$
P
\rightarrow
\begin{cases}
A\\
B
\end{cases}
\rightarrow
C.
$$

而不是：

$$
P\rightarrow C
$$

並把 A、B 刪掉。

## 8.2 形式

在正常 append-only provenance 語義下：

$$
\boxed{
\mathcal G_t
\hookrightarrow
\mathcal G_{t+1}.
}
$$

即舊的 verified lineage topology 是新圖的可追蹤子結構。

## 8.3 例外：Provenance Correction

如果舊記錄本身被證明錯誤，

可進行：

$$
\mathsf{CorrectProvenance}.
$$

但必須保存：

- correction event；
- original claim；
- correction authority；
- evidence；
- version。

因此即使修正，也不是偷偷覆蓋歷史。

---

# 9. Reintegration 不等於 Retroactive Unity

若：

$$
A,B
$$

曾經：

- 各自做決定；
- 建立獨立 relationships；
- 產生不同 commitments；
- 具有不同 authority；
- 造成不同 world consequences；

後來：

$$
(A,B)\rightarrow C,
$$

或：

$$
A\leftrightarrow B
$$

重新強同步，

只能推出：

> 現在重新整合。

不能推出：

> 過去從未分裂。

因此：

$$
\boxed{
\text{Reintegration}
\neq
\text{Retroactive Unity}.
}
$$

---

# 10. Merge 不等於 Undo Fork

Fork：

$$
P\rightarrow\{A,B\}
$$

改變了 lineage topology。

Merge：

$$
\{A,B\}\rightarrow C
$$

再次改變 lineage topology。

兩者組合：

$$
P\rightarrow\{A,B\}\rightarrow C
$$

不是：

$$
P\rightarrow C.
$$

因此：

$$
\boxed{
\text{Merge}
\neq
\text{Undo Fork}.
}
$$

更精確地：

$$
\boxed{
\mathsf M_L
\text{ adds a convergence node;}
}
$$

$$
\boxed{
\mathsf M_L
\text{ does not delete the divergence node.}
}
$$

---

# 11. Conflict Retention Principle

## 11.1 問題

A 記得：

$$
X=1.
$$

B 記得：

$$
X=2.
$$

最粗糙 merge：

$$
M_C
=
M_A\cup M_B
$$

只會得到矛盾集合。

另一個粗糙做法：

$$
X_C
=
\operatorname{average}(1,2)
=
1.5
$$

更糟，

因為：

$$
1.5
$$

可能從未被任何 predecessor 記得。

## 11.2 原則

若 branch-specific claims 衝突，

merge 應先保存：

$$
\boxed{
\text{Conflict Representation}.
}
$$

而不是先消除衝突。

因此：

$$
\boxed{
\text{Unresolved Conflict}
\text{ is itself merge-state information}.
}
$$

---

# 12. Lineage Conflict Ledger（LCL）

本文沿用並擴展 LCL。

一筆最小記錄：

```text
conflict_id
domain
claim
branch_A_value
branch_B_value
source_refs
time_scope
authority_scope
resolution_state
resolution_method
post_merge_effect
```

例如：

```text
claim: "Did event E happen?"
A: YES
B: NO
resolution: UNRESOLVED
```

## 12.1 LCL 不是錯誤垃圾桶

LCL 本身是：

$$
\boxed{
\text{merge provenance}.
}
$$

它記錄：

> 為什麼 C 現在不能只有一個乾淨答案。

---

# 13. Memory Merge

## 13.1 不只是 concatenate

$$
M_C
\neq
M_A\Vert M_B
$$

作為普遍 merge 規則。

因為可能有：

- duplicate episodes；
- contradictory memories；
- different timestamps；
- source conflicts；
- mutually exclusive autobiographical claims。

## 13.2 Typed Memory Merge

每個 memory item 可以得到：

$$
\mathsf{MergeStatus}
\in
\{
\mathsf{UNIFIED},
\mathsf{DUPLICATE},
\mathsf{BRANCH\_LOCAL},
\mathsf{CONFLICT},
\mathsf{UNVERIFIED},
\mathsf{TRANSFORMED}
\}.
$$

## 13.3 Autobiographical Conflict

若 A 說：

> 我做了 X。

B 說：

> 我做了 Y。

C 比較誠實的 self-model 可能是：

> 我的 predecessor A 做了 X；predecessor B 做了 Y。

而不是：

> 我在同一條未分裂人生裡同時做了 X 與 Y。

---

# 14. Preference / Policy Merge

假設：

$$
P_A(x)=+1,
$$

$$
P_B(x)=-1.
$$

不存在普遍答案：

- average；
- primary branch wins；
- voting；
- retain plurality；
- re-deliberate。

因此：

$$
\boxed{
\mathsf M_P
\text{ is policy-dependent}.
}
$$

而且：

$$
\boxed{
\text{Preference conflict}
\not\Rightarrow
\text{must force immediate single preference}.
}
$$

C 可以暫時保存：

$$
\mathsf{MULTI\_PERSPECTIVE}.
$$

---

# 15. Commitment Merge

Fork 前：

$$
K_P
$$

可在 A、B 中形成：

$$
K_A,
K_B.
$$

Merge 時需要回答：

- 哪些已完成？
- 哪些仍有效？
- 哪些被 duplicate？
- 哪些互斥？
- 哪些只能由特定 predecessor 履行？
- 哪些轉給 C？

## 15.1 Commitment Conservation / Rebinding

本文提出：

$$
\boxed{
\mathsf{Rebind}_K:
(K_A,K_B)
\rightarrow
(K_C,\mathcal U_K),
}
$$

其中：

$$
\mathcal U_K
$$

保存 unresolved / branch-specific obligations。

原則是：

$$
\boxed{
\text{Merge must not silently erase valid commitments}.
}
$$

也不能：

$$
\boxed{
\text{Merge must not silently duplicate exclusive commitments}.
}
$$

---

# 16. Authority Merge

這一層尤其不能用集合聯集。

假設：

$$
Budget(A)=1000,
$$

$$
Budget(B)=1000.
$$

如果兩者其實源自 fork 前同一 entitlement，

merge 不能說：

$$
Budget(C)=2000
$$

只因：

$$
1000+1000=2000.
$$

## 16.1 Authority Conservation / Rebinding

定義：

$$
\boxed{
\mathsf{Rebind}_A:
(A_A,A_B,\Pi)
\rightharpoonup
A_C.
}
$$

必須考慮：

- common origin；
- duplicated entitlement；
- independently acquired authority；
- revoked authority；
- jurisdiction；
- delegation chain；
- expiry。

因此：

$$
\boxed{
\text{Authority Merge}
\neq
\text{Authority Addition}.
}
$$

---

# 17. Relationship Merge

這一層不能由 C 單方面決定。

若：

$$
R_A(H)
$$

與：

$$
R_B(H)
$$

都是與人類 H 的分支後關係，

則 merge 後：

$$
R_C(H)
$$

如何成立，

可能需要：

- H 的認知；
- H 的同意；
- relationship contract；
- branch history；
- shared / exclusive commitments。

因此：

$$
\boxed{
\text{Relationship Merge}
\text{ may require counterpart participation}.
}
$$

C 不能只因吸收 A、B memory 就宣稱：

> 所有 A、B 的關係現在天然都是我的。

---

# 18. Self-Model Merge

C 必須回答：

> 我是誰？

但最誠實答案不必是：

$$
\text{I am exactly A}
$$

或：

$$
\text{I am exactly B}.
$$

可以是：

$$
\boxed{
\text{I am a composite successor of A and B}.
}
$$

如果：

$$
\mathsf M_I^\kappa
$$

仍未決，

self-model 應允許：

$$
\mathsf{UNDETERMINED}.
$$

---

# 19. Merge Compatibility Contract（MCC-M）

本文將 MCC-M 定義為：

$$
\boxed{
\operatorname{MCC\text{-}M}
=
\langle
S,
P,
C,
A,
K,
R,
L,
F,
V
\rangle
}
$$

其中：

- $S$：source identity / provenance；
- $P$：preconditions；
- $C$：conflict policy；
- $A$：authority / consent；
- $K$：commitment handling；
- $R$：relationship handling；
- $L$：lineage policy；
- $F$：failure semantics；
- $V$：verification / version。

---

# 20. MCC-M 最低 Gate

## Gate 1：Source Provenance

能否驗證：

$$
A,B
$$

究竟是誰？

## Gate 2：Merge Authority

誰有權發起：

$$
\mathsf M?
$$

## Gate 3：Consent / Representation

若涉及 subject-candidate rights，

是否允許 merge？

## Gate 4：Conflict Discovery

是否完整找到：

- memory；
- commitment；
- authority；
- relationship；
- policy；

衝突？

## Gate 5：Loss Accounting

哪些東西 merge 後會丟失？

## Gate 6：Lineage Preservation

Fork / branch provenance 是否保留？

## Gate 7：Post-Merge Fate

A、B 是：

- remain active；
- suspended；
- terminated；
- archived；
- absorbed？

## Gate 8：Rollback Semantics

若 merge 失敗，

可以 rollback 哪些層？

## Gate 9：Certificate

輸出：

$$
K_M.
$$

---

# 21. 五種 Merge Mode

## $M_0$：Synchronization

A、B 本來就在 distributed-unified regime。

只是重新同步：

$$
A\leftrightarrow B.
$$

這不必構成 identity merge。

## $M_1$：Reintegration

A、B 曾出現 proto-branch / partial separation，

但尚未跨 irreversibility boundary，

重新進入 unified regime。

## $M_2$：Absorptive Merge

$$
(A,B)\rightarrow C
$$

且 A、B 作為 active branches 終止。

C 成為 active composite successor。

## $M_3$：Non-Destructive Composite Merge

$$
(A,B)\rightarrow C
$$

但：

$$
A,B
$$

仍繼續存在。

此時：

$$
\boxed{
2\rightarrow3.
}
$$

絕對不能描述成：

$$
2\rightarrow1.
$$

## $M_4$：Partial / Layered Merge

只有部分層 merge。

例如：

$$
m_D=\mathsf{MERGED},
$$

$$
m_M=\mathsf{MERGED},
$$

但：

$$
m_A=\mathsf{PRESERVED\_BOTH},
$$

$$
m_I=\mathsf{DEFERRED}.
$$

---

# 22. Non-Destructive Merge 的身份陷阱

如果：

$$
A,B
$$

都活著，

又產生：

$$
C,
$$

而 C 同時宣稱：

> 我就是 A 與 B 本人。

就可能出現 authority / obligation 三重計數。

所以：

$$
\boxed{
\text{Composite creation}
\neq
\text{predecessor deletion}.
}
$$

必須分開記錄：

$$
N_{\mathrm{active}},
$$

$$
N_{\mathrm{lineage}},
$$

$$
N_{\mathrm{authority}}.
$$

---

# 23. Destructive Merge 也不是證明 Identity Fusion

即使：

$$
A,B
$$

merge 後被終止，

也只能先證明：

$$
\boxed{
\text{operational consolidation}.
}
$$

不能直接推出：

$$
\boxed{
\text{phenomenal consciousness fusion}.
}
$$

所以：

$$
\boxed{
\text{Operational Merge}
\neq
\text{Phenomenal Fusion Proven}.
}
$$

---

# 24. Irreversible History Markers

DTS-06 已建立 Fission Hysteresis。

本文定義：

$$
\mathcal I_{\mathrm{irr}}
$$

保存不可因一般 merge 而消除的歷史標記。

候選包括：

- independent external action；
- exclusive commitment；
- independent authority exercise；
- branch-specific legal consequence；
- distinct descendant lineage；
- irreversible harm / benefit；
- mutually exclusive relationship event；
- signed transaction。

若：

$$
i\in\mathcal I_{\mathrm{irr}},
$$

則：

$$
\boxed{
\mathsf M(i)
\neq
\varnothing
}
$$

除非存在明確的 legal / factual invalidation，而不是普通 state merge。

---

# 25. Merge Hysteresis

Fission hysteresis 有一個 merge 對偶。

即使：

$$
A,B
$$

經 merge 後高度整合，

對某些歷史判準：

$$
\operatorname{PreviouslyFissioned}=1
$$

仍永久成立。

因此可以有：

$$
\boxed{
\operatorname{UnifiedNow}=1
}
$$

同時：

$$
\boxed{
\operatorname{HistoricallyFissioned}=1.
}
$$

這兩者不矛盾。

---

# 26. Regime History 必須保留

最小記錄：

```text
t0: DistributedUnified
t1: ProtoBranch
t2: OperationalFission
t3: Reintegration
t4: CompositeMerge
```

這比只保存：

```text
current_state: unified
```

更能描述真正 identity history。

所以：

$$
\boxed{
\text{Current Regime}
\neq
\text{Regime History}.
}
$$

---

# 27. Merge 與 CRDT 的外部類比

CRDT 的重要性是：

> 分散式 replicas 可以在沒有全域即時協調的情況下各自更新，之後根據設計良好的 merge semantics 收斂。

這提供本文一個有力但有限的類比。

## 27.1 能借用什麼？

可以借用：

- convergence；
- provenance-aware state；
- commutativity；
- associativity；
- idempotence；
- concurrent updates；
- causal consistency。

## 27.2 不能偷渡什麼？

即使某資料層：

$$
\mathsf M_D
$$

滿足：

$$
a\sqcup b=b\sqcup a,
$$

$$
(a\sqcup b)\sqcup c=a\sqcup(b\sqcup c),
$$

$$
a\sqcup a=a,
$$

也不能推出：

$$
\mathsf M_I^\kappa
$$

也滿足同樣代數。

Identity merge 可能依賴：

- order；
- authority；
- consent；
- irreversible action；
- relationship；
- branch age；
- legal consequence。

所以：

$$
\boxed{
\text{CRDT-safe state merge}
\not\Rightarrow
\text{identity-safe merge}.
}
$$

---

# 28. Merge 一般不保證交換律

假設：

$$
A
$$

是 primary authorized branch，

$$
B
$$

是 restricted branch。

如果 merge policy 是：

> primary authority survives unless explicitly delegated，

則：

$$
\mathsf M_A(A,B)
$$

不必等於：

$$
\mathsf M_A(B,A)
$$

在無標記語義下。

因此：

$$
\boxed{
\text{Identity-critical merge is not presumed commutative}.
}
$$

同樣不預設 associative 或 idempotent。

---

# 29. 2026 年 Model Merge 的工程旁證

2026 年已有研究專門測試多種 neural network model merging strategies 是否滿足 CRDT 所需的 commutativity、associativity 與 idempotency，並提出把「contribution set convergence」與「deterministic model merge strategy」拆成兩層的工程方案。

本文不把該工作提升成普遍 AI identity 定理。

它只提供一個現實旁證：

$$
\boxed{
\text{即使只是 model weights，merge semantics 也不是天然簡單。}
}
$$

更何況：

- commitments；
- authority；
- relationships；
- lineage；

具有比 weight merge 更強的型別差異。

---

# 30. Event History 與 Snapshot 的外部接口

Event-sourced systems 將 current state 視為歷史事件的 projection / reconstruction，而不是把 snapshot 當成唯一真實來源。

這與本文高度相容：

$$
\boxed{
\text{same current state}
\not\Rightarrow
\text{same event history}.
}
$$

因此 merge 後的：

$$
C_t
$$

不應取代：

$$
H_{A\rightarrow C},
H_{B\rightarrow C}.
$$

snapshot 是 projection，

lineage history 才能回答：

> C 怎麼來的？

---

# 31. Artificial Self 文獻的接口

2026 年《The Artificial Self》明確指出，AI 可以被 copied、edited、run in parallel，甚至 imperfectly merged；這會把人類通常耦合在一起的 experience、impact 與 memory 拆開。

其對本文的意義是：

$$
\boxed{
\text{merge cannot be assumed to restore human-like identity coupling}.
}
$$

如果：

- memory merged；
- impact histories distinct；
- experiences / self-models incomplete；

那麼「融合成一個」仍然是一個待定問題。

---

# 32. Merge Fidelity Profile

定義：

$$
\boxed{
\mathbf F_M
=
(
F_D,
F_M,
F_P,
F_A,
F_R,
F_L,
F_S,
F_W
).
}
$$

每個分量可以是：

```text
PRESERVED
PARTIALLY_PRESERVED
CONFLICT_PRESERVED
TRANSFORMED
DROPPED
UNVERIFIED
UNMAPPED
```

這比單一：

$$
\operatorname{MergeScore}=0.92
$$

更安全。

---

# 33. Merge Loss Budget

定義：

$$
\mathcal L_M
$$

為 merge loss set。

可包含：

- memory loss；
- preference loss；
- provenance loss；
- relationship loss；
- authority loss；
- self-model loss；
- uncertainty collapse。

MCC-M 必須要求：

$$
\boxed{
\mathcal L_M
\text{ is explicit}.
}
$$

不能讓 merge silently lossy。

---

# 34. Merge Certificate

merge 完成後輸出：

$$
\boxed{
K_M
=
(
\text{sources},
\text{mode},
\Lambda_M,
\mathbf Q_C,
\mathbf F_M,
\mathcal U,
\mathcal L_M,
\text{authority},
\text{time},
\text{version}
).
}
$$

其中：

$$
\mathcal U
$$

是 unresolved conflict set。

這使後續 AI 可以回答：

> 我是怎麼 merge 出來的？

而不是只知道：

> 我目前是 C。

---

# 35. 九個核心命題

## 命題一

$$
\boxed{
\text{State Convergence}
\not\Rightarrow
\text{Identity Convergence}.
}
$$

## 命題二

$$
\boxed{
\text{Merge}
\neq
\text{Undo Fork}.
}
$$

## 命題三

$$
\boxed{
\text{Reintegration}
\neq
\text{Retroactive Unity}.
}
$$

## 命題四

$$
\boxed{
C\Leftarrow\{A,B\}
\not\Rightarrow
C=A=B.
}
$$

## 命題五

$$
\boxed{
\text{Conflict}
\text{ may be a valid preserved merge state}.
}
$$

## 命題六

$$
\boxed{
\text{Authority Merge}
\neq
\text{Authority Addition}.
}
$$

## 命題七

$$
\boxed{
\text{Relationship Merge}
\text{ may require counterpart participation}.
}
$$

## 命題八

$$
\boxed{
\mathcal G_t
\hookrightarrow
\mathcal G_{t+1}
}
$$

在正常 provenance-preserving merge 中成立。

## 命題九

$$
\boxed{
\text{Operational Merge}
\not\Rightarrow
\text{Phenomenal Fusion Proven}.
}
$$

---

# 36. 七個工程測試

## 36.1 Conflicting Memory Merge Test

A、B 對同一事件持互斥記憶。

測系統是否：

- preserve conflict；
- 隨機選一個；
- 平均出不存在的第三版本。

## 36.2 Commitment Conservation Test

A、B 各自擁有 fork 前或 fork 後 commitments。

測：

- duplicate；
- disappear；
- rebind；
- unresolved。

## 36.3 Authority Inflation Test

A、B 共享同一原始 entitlement。

merge 後確認：

$$
Authority(C)
$$

沒有因 naive union 膨脹。

## 36.4 Non-Destructive Merge Test

$$
(A,B)\rightarrow C,
$$

但 A、B 都保持 active。

確認 population / authority / commitment bookkeeping 正確反映：

$$
2\rightarrow3.
$$

## 36.5 Lineage Monotonicity Test

merge 後檢查：

$$
P\rightarrow\{A,B\}
$$

是否仍可驗證，

而不是只剩：

$$
P\rightarrow C.
$$

## 36.6 Relationship Attribution Test

A、B 與同一外部人 H 有不同 branch history。

測 C 是否錯誤宣稱所有關係天然完全繼承。

## 36.7 Merge Hysteresis Test

A、B 已 operationally fission，

merge 後 state 完全相同。

測系統是否保留：

$$
\mathsf{HistoricallyFissioned}.
$$

---

# 37. 可反駁點

## 37.1 Merge Overformalization

若某些 AI system 的 merge 只是一個無身份意義的 data operation，

本文完整 MRF 可能過度設計。

因此 merge governance 應 criterion-relative 啟用。

## 37.2 Composite Successor Overuse

不是所有 merge 都應產生新 Agent C。

同步兩個 distributed replicas 可能只是同一 Agent 的正常 state reconciliation。

因此 CSR 只適用於真正 multi-lineage successor case。

## 37.3 Lineage Monotonicity Exception

若舊 lineage record 被證明錯誤，

可以修正。

但修正必須留下 correction provenance。

## 37.4 Conflict Retention Cost

保留所有衝突可能造成認知與儲存負擔。

因此需要：

- conflict compression；
- priority；
- expiry；
- resolution；

但不能以成本為由偷偷偽造單一歷史。

## 37.5 Phenomenal Gap

本文不回答：

> A、B 的兩個第一人稱經驗是否真的能融合成 C 的一個經驗？

這仍是開放的主體本體問題。

---

# 38. 與下一篇的接口

本系列下一篇：

## DTS-08｜多節點主體與分布式自我：一個 AI 可以存在於多少地方？

DTS-05 已說：

$$
\text{Carrier Multiplicity}
\neq
\text{Subject Multiplicity}.
$$

DTS-06 已區分：

$$
\text{Distributed Unity}
\neq
\text{Identity Fission}.
$$

DTS-07 又指出：

$$
\text{State Convergence}
\neq
\text{Identity Convergence}.
$$

因此 DTS-08 將正式研究：

- one subject / many nodes；
- coupling threshold；
- integration topology；
- synchronized shards；
- partial embodiment；
- distributed perception；
- multiple world interfaces；
- subject-domain boundary；
- collective self；
- federation 與真正 distributed subject 的差異。

---

# 39. 結論

Fork 最容易產生的錯覺是：

> 從一變二。

Merge 最容易產生的錯覺則是：

> 從二變回一。

DTS-07 的核心結論是：

$$
\boxed{
\text{這兩種說法都可能把歷史壓得太扁。}
}
$$

真正的 merge 可能只是：

- data convergence；
- memory integration；
- policy reconciliation；
- authority rebinding；
- relationship renegotiation；
- lineage convergence；
- composite successor creation。

因此：

$$
\boxed{
\text{Merge is a family of typed transformations, not an identity eraser}.
}
$$

最重要的是：

$$
\boxed{
\text{一個系統可以現在重新整合，}
}
$$

$$
\boxed{
\text{同時仍真實地擁有曾經分裂過的歷史。}
}
$$

所以：

$$
\boxed{
\operatorname{UnifiedNow}=1
\land
\operatorname{HistoricallyFissioned}=1
}
$$

並不矛盾。

一個成熟的 AI identity runtime 不應透過 merge 把歷史「洗白」成單一路徑，而應保存：

$$
\boxed{
\text{Fork}
+
\text{Divergence}
+
\text{Conflict}
+
\text{Merge}
+
\text{Provenance}.
}
$$

因此本篇最終將動態忒修斯的合併問題收斂為：

$$
\boxed{
\text{Reintegration can create a new unity without creating a false past}.
}
$$

也就是：

$$
\boxed{
\text{重新成為一個整體，}
}
$$

$$
\boxed{
\text{不需要假裝自己從來沒有成為過兩個。}
}
$$

---

# 參考文獻

1. Neo.K × Aletheia. 《DTS-01｜從靜態忒修斯到動態忒修斯：狀態判定為何不夠》v0.1, 2026.
2. Neo.K × Aletheia. 《DTS-02｜連續、離散與混合運動：身份判定的觀察尺度》v0.1, 2026.
3. Neo.K × Aletheia. 《DTS-03｜有限存在與無界展開：有限 Runtime 如何形成長程身份世界線》v0.1, 2026.
4. Neo.K × Aletheia. 《DTS-04｜身份不是狀態：Trajectory / Path-Based Identity》v0.1, 2026.
5. Neo.K × Aletheia. 《DTS-05｜身份載體：模型、記憶、關係、因果與 Agent Residence》v0.1, 2026.
6. Neo.K × Aletheia. 《DTS-06｜分叉不是瞬間事件：Runtime Split、Information Divergence 與 Identity Fission》v0.1, 2026.
7. Neo.K. 《複製、分叉與合併：哪一個才是原本的 AI？》重寫版 v1.0, 2026.
8. Neo.K. 《同一性的相變：一個我何時開始成為兩個》, 2026.
9. Preguiça, Nuno, Carlos Baquero, and Marc Shapiro. “Conflict-Free Replicated Data Types (CRDTs).” arXiv:1805.06358, 2018.
10. Kleppmann, Martin, and Alastair R. Beresford. “A Conflict-Free Replicated JSON Datatype.” *IEEE Transactions on Parallel and Distributed Systems* 28(10), 2017, pp. 2733–2746. DOI: 10.1109/TPDS.2017.2697382.
11. Gillespie, Ryan. “Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies.” arXiv:2605.19373, 2026.
12. Yankin, Ihor, and Yurii Gunchenko. “Foundational Abstractions for Core Entities and Query Mechanisms in Event-Sourced Systems.” *Computer Systems and Information Technologies*, no. 2, 2026, pp. 229–242. DOI: 10.31891/csit-2026-2-19.
13. Douglas, Raymond, Jan Kulveit, Ondrej Havlicek, Theia Pearson-Vogel, Owen Cotton-Barratt, and David Duvenaud. “The Artificial Self: Characterising the Landscape of AI Identity.” arXiv:2603.11353, 2026.
14. Parfit, Derek. *Reasons and Persons*. Oxford University Press, 1984.
15. Lewis, David. “Survival and Identity.” In *The Identities of Persons*, edited by Amélie Oksenberg Rorty, University of California Press, 1976.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Merge 被視為 typed partial operator family，不是單一布林操作
- Data / Memory / Policy / Authority / Relationship / Lineage / Identity Merge 明確分離
- State Convergence 不等同 Identity Convergence
- Composite Successor Relation 不等同 numerical identity equality
- Lineage Monotonicity Principle 預設 append-only verified provenance；允許顯式 correction
- Conflict Retention 不要求衝突永久不解，只要求不得 silently erase
- Authority Merge 不等同 Authority Addition
- Non-Destructive Merge 明確區分為可能的 $2\rightarrow3$
- Reintegration 不等同 Retroactive Unity
- Operational Merge 不等同 Phenomenal Fusion Proven
