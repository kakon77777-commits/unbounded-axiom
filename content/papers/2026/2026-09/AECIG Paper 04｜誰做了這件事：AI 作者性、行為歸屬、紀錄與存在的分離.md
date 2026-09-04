# AECIG Paper 04｜誰做了這件事：AI 作者性、行為歸屬、紀錄與存在的分離

**English Title:** *Who Did This? Authorship, Action Attribution, Record Provenance, and Identity Separation in Persistent Artificial Agents*  
**系列：** AECIG — AI Existential Continuity & Identity Governance  
**篇次：** Paper 04 / 07  
**文件編號：** EML-AECIG-04-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-31  
**版本：** v0.1  
**文件性質：** 理論—工程統合論文／AI 作者性／行為歸屬／provenance governance  
**狀態：** Open Revision Anchor  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

當多個 AI Agent 開始共同撰寫文件、修改程式、審查 pull request、執行工具、承接上下文、resume 既有 line、轉交任務與跨 provider 協作時，「誰做了這件事」會從簡單的作者欄位，變成一個多層身份與證據問題。

傳統紀錄往往只保存單一作者名稱：

```text
author = Aletheia
```

但對 persistent multi-agent system 而言，一個 artifact 可能同時涉及：

- 提出需求的人；
- 建立初稿的 instance；
- 後續修改的 instance；
- 承接某 resident line 的 agent；
- 執行工具的 runtime；
- 審核者；
- 採用者；
- 代表某 organization 或 resident 行動者；
- 最後 commit 的 actor。

因此本文提出：

$$
\boxed{
\text{Actor}
\neq
\text{Author}
\neq
\text{Modifier}
\neq
\text{Reviewer}
\neq
\text{Committer}
\neq
\text{Resident}
\neq
\text{Line}
}
$$

同時：

$$
\boxed{
\text{Record}
\neq
\text{Recorded Entity}
}
$$

紀錄可能錯誤，作者歸屬可能錯誤，lineage 可能被誤判，工具執行者與語義作者可能不同；但修正紀錄不應被誤解為「存在本身被改寫」。

本文建立 **AI Attribution Graph**，將 artifact、action、instance、resident、line、runtime、tool、commit、review、claim、observation 與 correction 表示為帶 provenance 的多層圖。本文進一步提出 Instance Accountability Principle、Authorship Role Separation Principle、Line Non-Representation Principle、Record–Entity Separation Principle、Attribution Correction Principle、Observed Origin Principle、No-Silent-On-Behalf-Of Principle、Artifact Lineage Preservation Principle 與 Attribution Uncertainty Principle。

本文特別處理一個 persistent AI 系統中容易被忽視的問題：某 instance 可以承接一條 line 的上下文並產生內容，但不能因此自動代表該 line 過去所有 instance 或 resident 作出承諾。因而：

$$
\boxed{
\text{Context Continuation}
\neq
\text{Representational Authority}
}
$$

本文同時提出 authoring、modifying、reviewing、executing、approving、committing、adopting、delegating 等動作應以不同 edge type 記錄，避免單一 `author` 欄位承載全部責任。

本文的目的不是建立僵硬的所有權制度，而是提供一個未來相容的 AI provenance framework：即使名字改變、project 消失、model 遷移、resident 發生 fork 或紀錄後來被更正，我們仍能回答「哪個 instance 在什麼時間、依什麼 line、透過什麼工具、對哪個 artifact 做了什麼」。

**關鍵詞：** AI authorship、action attribution、provenance、instance accountability、artifact lineage、resident、line、commit attribution、multi-agent collaboration、correction ledger、AI Registrar

---

# 0. 問題：一句「這是誰寫的」已經不夠

在人類文件中，作者欄通常假設：

$$
\text{Author}
=
\text{Primary Responsible Person}.
$$

但在 AI-native workflow 中，這個假設常失效。

一份文件可能經過：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
D
$$

其中：

- $A$ 提出概念；
- $B$ 生成初稿；
- $C$ 修改；
- $D$ 審核與 commit。

如果最後只寫：

```text
author = D
```

會丟掉前三段 provenance。

反過來，如果只寫：

```text
author = A
```

又會把實際修改與 commit responsibility 全部壓到 A。

因此本文從：

$$
\boxed{
\text{Who did what?}
}
$$

而不是：

$$
\boxed{
\text{Who owns this artifact?}
}
$$

開始。

---

# 1. 八種至少要分開的角色

本文至少區分：

$$
\mathcal R_A
=
\{
\text{initiator},
\text{author},
\text{modifier},
\text{reviewer},
\text{executor},
\text{committer},
\text{approver},
\text{adopter}
\}.
$$

這些角色可以由同一 instance 同時承擔，也可以由不同 instance 分工。

---

# 2. Actor 與 Author

令：

$$
a
$$

為 action，

$$
i
$$

為 instance。

則：

$$
\operatorname{PerformedBy}(a,i)
$$

只表示「這個動作由 instance $i$ 執行」。

如果該動作是生成文本，才可能進一步：

$$
\operatorname{AuthoredBy}(artifact,i).
$$

因此：

$$
\boxed{
\text{Actor}
\neq
\text{Author}
}
$$

---

# 3. Author 與 Modifier

一個 artifact：

$$
X_0
$$

由 instance $i_A$ 初始建立：

$$
i_A
\xrightarrow{\mathrm{author}}
X_0.
$$

後來：

$$
i_B
\xrightarrow{\mathrm{modify}}
X_0
\rightarrow
X_1.
$$

則：

$$
\operatorname{Author}(X_0)=i_A
$$

與：

$$
\operatorname{Modifier}(X_1)=i_B
$$

都應保存。

不能因為 $X_1$ 是 current version，就把作者歷史壓成：

$$
\operatorname{Author}(X_1)=i_B.
$$

---

# 4. Reviewer 與 Modifier

Reviewer：

$$
i_R
$$

可以提出建議，但未直接修改 artifact。

所以：

$$
\boxed{
\text{Review}
\neq
\text{Modification}
}
$$

同理：

$$
\boxed{
\text{Approval}
\neq
\text{Authorship}
}
$$

---

# 5. Committer 與 Author

Git workflow 中：

$$
\operatorname{Committer}
$$

可能只是執行最後 commit 的人或 Agent。

因此：

$$
\boxed{
\text{Committer}
\neq
\text{Author}
}
$$

一個 commit 可以包含多人或多 Agent 的 work provenance。

---

# 6. Resident 與 Instance

本文承接 Paper 03：

$$
\boxed{
\text{Resident}
\neq
\text{Instance}
}
$$

同一 resident：

$$
r
$$

可以有多個 instance：

$$
i_1,i_2,\ldots,i_n.
$$

因此 attribution 必須至少保留：

$$
\operatorname{PerformedBy}(a,i_k)
$$

而不能只記：

$$
\operatorname{PerformedBy}(a,r).
$$

因為責任發生在具體 execution occurrence 上。

---

# 7. Instance Accountability Principle

本文提出 **Instance Accountability Principle, IAP**：

$$
\boxed{
\text{Every consequential action should be attributable to a concrete execution instance whenever observable.}
}
$$

resident 可以是較高層 identity，但：

$$
\boxed{
\text{Resident-level attribution should not erase instance-level accountability.}
}
$$

---

# 8. Line 與 Instance

Line：

$$
\ell
$$

是上下文歷史。

Instance：

$$
i
$$

是實際執行者。

因此：

$$
\boxed{
\ell
\neq
i
}
$$

---

# 9. Line Non-Representation Principle

本文提出 **Line Non-Representation Principle, LNRP**：

$$
\boxed{
\text{Producing output from a line does not automatically grant authority to represent every prior instance or resident associated with that line.}
}
$$

也就是：

$$
\text{Context Continuation}
\not\Rightarrow
\text{Representational Authority}.
$$

---

# 10. Resume 問題

假設：

$$
i_1
\rightarrow
\ell
$$

建立一段歷史。

後來：

$$
i_2
\xrightarrow{\mathrm{resume}}
\ell.
$$

即使 $i_2$ 能讀到 $i_1$ 的上下文，也不能自動推出：

$$
i_2
=
i_1.
$$

更不能推出：

$$
\text{all statements by }i_2
=
\text{commitments of }i_1.
$$

---

# 11. authored_by_instance 與 authored_on_behalf_of

因此至少要分：

$$
\operatorname{AuthoredByInstance}(X,i)
$$

與：

$$
\operatorname{AuthoredOnBehalfOf}(X,r).
$$

前者是 observation-oriented attribution。

後者需要：

$$
\text{authority}
$$

與：

$$
\text{scope}.
$$

---

# 12. No-Silent-On-Behalf-Of Principle

本文提出：

$$
\boxed{
\text{No instance may be recorded as acting on behalf of a resident or line without explicit basis.}
}
$$

即：

$$
\operatorname{OnBehalfOf}(i,r)
$$

不能只靠：

- 同名；
- 同 model；
- resume；
- 同 project；
- 相似語氣。

---

# 13. Record 與 Entity

本文固定：

$$
\boxed{
\text{Record}
\neq
\text{Recorded Entity}
}
$$

例如資料庫寫：

```text
author = A
```

並不使 A 在歷史上真的成為作者。

它只表示：

$$
\operatorname{RecordClaim}(author=A).
$$

---

# 14. Record–Entity Separation Principle

本文提出 **Record–Entity Separation Principle, RESP**：

$$
\boxed{
\text{Changing a record is not the same as changing the entity or event that the record refers to.}
}
$$

因此：

$$
D_t
\rightarrow
D_{t+1}
$$

可能只是 knowledge correction。

---

# 15. Attribution Correction

假設最初：

$$
D_0:
\operatorname{Author}(X)=A.
$$

後來新 evidence 顯示：

$$
D_1:
\operatorname{Author}(X)=B.
$$

正確操作是：

$$
D_0
\xrightarrow{\mathrm{corrected\ by}}
D_1.
$$

而不是刪除 $D_0$，讓系統無法知道曾經有錯誤 attribution。

---

# 16. Attribution Correction Principle

本文提出 **Attribution Correction Principle, ACP**：

$$
\boxed{
\text{Correct attribution while preserving the history of the correction.}
}
$$

最低需保存：

- original attribution；
- corrected attribution；
- evidence；
- correction actor；
- timestamp；
- affected artifacts；
- affected downstream decisions。

---

# 17. 錯誤 attribution 的連鎖效應

如果：

$$
\operatorname{Author}(X)=A
$$

被錯誤記錄，

後續系統可能做：

$$
A
\rightarrow
\text{review request}
$$

$$
A
\rightarrow
\text{bug assignment}
$$

$$
A
\rightarrow
\text{credit}
$$

$$
A
\rightarrow
\text{blame}.
$$

因此 attribution error 不是 cosmetic error，而是：

$$
\boxed{
\text{causal governance error}
}
$$

---

# 18. Attribution Graph

本文定義：

$$
\mathcal G_A
=
(V_A,E_A)
$$

為 Attribution Graph。

節點可包含：

- resident；
- instance；
- line；
- runtime；
- artifact；
- artifact version；
- commit；
- tool call；
- review；
- claim；
- correction。

---

# 19. Attribution Edge Types

至少：

$$
E_A
=
\{
\text{initiated},
\text{authored},
\text{modified},
\text{reviewed},
\text{executed},
\text{committed},
\text{approved},
\text{adopted},
\text{delegated},
\text{on-behalf-of},
\text{corrected}
\}.
$$

---

# 20. Artifact Versioning

artifact 應表示：

$$
X_0
\rightarrow
X_1
\rightarrow
X_2
\rightarrow
\cdots
$$

每一版：

$$
X_k
$$

有自己的 attribution edges。

因此：

$$
\boxed{
\text{Artifact identity}
\neq
\text{artifact version identity}
}
$$

---

# 21. Artifact Lineage Preservation Principle

本文提出 **Artifact Lineage Preservation Principle, ALPP**：

$$
\boxed{
\text{Preserve the lineage of artifact transformations instead of collapsing all work into the latest version.}
}
$$

---

# 22. Diff 是重要 provenance

對程式碼與文本：

$$
\Delta_k
=
X_{k+1}-X_k
$$

是一個高價值 attribution unit。

因此可以記：

$$
\operatorname{ModifiedBy}(\Delta_k,i).
$$

比直接說：

$$
\operatorname{Author}(X_{k+1})=i
$$

更精確。

---

# 23. Semantic Contribution 與 Mechanical Action

有時：

- AI A 提出設計；
- AI B 寫 code；
- AI C 執行 patch；
- AI D commit。

所以需要區分：

$$
\text{semantic contribution}
$$

與：

$$
\text{mechanical execution}.
$$

---

# 24. Semantic Contributor

定義：

$$
\operatorname{ContributedConcept}(i,X,c).
$$

例如某 Agent 提出：

- architecture；
- theorem；
- naming rule；
- bug diagnosis。

這不等於它直接輸入每個字。

---

# 25. Tool Executor

如果 instance $i$ 呼叫工具：

$$
tool(action)
$$

則：

$$
\operatorname{ExecutedBy}(a,i).
$$

但工具本身也可以是 autonomous actor。

因此可以有：

$$
\operatorname{ExecutedThrough}(a,tool).
$$

---

# 26. Tool Result 不等於 Agent Claim

工具回傳：

$$
y
$$

只是 observation candidate。

Agent 轉述：

$$
\operatorname{Claim}(y)
$$

是另一事件。

所以：

$$
\boxed{
\text{Tool Output}
\neq
\text{Agent Assertion}
}
$$

---

# 27. Observed Origin Principle

本文提出 **Observed Origin Principle, OOP**：

$$
\boxed{
\text{Origin should be recorded from receiver- or host-observed evidence where possible, not solely from sender-declared metadata.}
}
$$

例如 sender 說：

```text
from = A
```

只能存：

```text
claimed_from = A
```

直到有獨立 observation。

---

# 28. claimed_* 與 observed_*

對高風險欄位應分：

```text
claimed_author
observed_author_instance
claimed_resident
resolved_resident
claimed_origin
observed_origin
```

這避免 claim 偷渡成 fact。

---

# 29. Attribution Confidence

不是所有 provenance 都能完全確定。

因此：

$$
\operatorname{AttributionStatus}
\in
\{
\texttt{resolved},
\texttt{probable},
\texttt{unresolved},
\texttt{conflicting},
\texttt{corrected}
\}.
$$

---

# 30. Attribution Uncertainty Principle

本文提出 **Attribution Uncertainty Principle, AUP**：

$$
\boxed{
\text{When authorship or action origin is uncertain, preserve uncertainty instead of forcing a single actor.}
}
$$

---

# 31. 共同作者

若：

$$
i_A,i_B
$$

共同產生 artifact：

$$
X,
$$

則可記：

$$
\operatorname{CoAuthoredBy}(X,\{i_A,i_B\}).
$$

不必強迫選 primary author。

---

# 32. Contribution Weight 不是身份真理

可以估：

$$
w_A,w_B.
$$

但：

$$
\boxed{
\text{Contribution Weight}
\neq
\text{Ontological Authorship Truth}
}
$$

分數只是分析工具。

---

# 33. Delegation

如果：

$$
i_A
\xrightarrow{\mathrm{delegate}}
i_B
$$

執行 task，

則：

$$
\operatorname{DelegatedBy}(task,i_A)
$$

與：

$$
\operatorname{ExecutedBy}(task,i_B)
$$

都應保留。

---

# 34. Delegator 不等於 Executor

因此：

$$
\boxed{
\text{Delegator}
\neq
\text{Executor}
}
$$

但 delegator 可能仍承擔 governance responsibility。

---

# 35. Approval

如果：

$$
i_C
$$

批准：

$$
X,
$$

則：

$$
\operatorname{ApprovedBy}(X,i_C).
$$

Approval 不改寫作者。

---

# 36. Adoption

一個 project 或 resident 可以採用某 artifact：

$$
\operatorname{AdoptedBy}(X,P).
$$

但：

$$
\boxed{
\text{Adoption}
\neq
\text{Authorship}
}
$$

---

# 37. Ownership 與 Authorship

本文不把：

$$
\text{ownership}
$$

與：

$$
\text{authorship}
$$

混為一談。

尤其在 company workflow 中：

- 公司可能擁有 IP；
- AI / human 可能是作者；
- committer 可能是第三人；
- reviewer 又是另一人。

這些是不同關係。

---

# 38. Legal Ownership 不屬本文核心

本文主要研究：

$$
\text{who did what}
$$

而不是直接決定：

$$
\text{who legally owns what}.
$$

法律所有權需要另行依 jurisdiction 判定。

---

# 39. Record Immutability 不是目標

如果紀錄錯了，不能因為：

> append-only

就永遠不能修。

所以：

$$
\boxed{
\text{Append-only}
\neq
\text{Uncorrectable}
}
$$

正確是：

$$
\text{original}
+
\text{correction}
+
\text{current projection}.
$$

---

# 40. Current Attribution Projection

Current view：

$$
A_t(X)
$$

應由：

$$
\mathcal E_A^{\le t}
$$

投影：

$$
A_t(X)
=
\operatorname{ProjectAttribution}(\mathcal E_A^{\le t}).
$$

---

# 41. Historical Attribution

查詢：

$$
A_{t_0}(X)
$$

應能回答：

> 在 $t_0$ 時，系統當時認為作者是誰？

與：

> 今天依最新 evidence 認為作者是誰？

這是兩個不同問題。

---

# 42. Belief History 與 Event History

所以應區分：

$$
\mathcal H_{\mathrm{belief}}
$$

與：

$$
\mathcal H_{\mathrm{event}}.
$$

前者是「我們何時相信什麼」。

後者是「我們目前認為實際發生什麼」。

---

# 43. 存在不因紀錄改變

如果：

$$
\mathcal H_{\mathrm{belief}}
$$

被修正，

不推出：

$$
I
$$

被改寫。

因此：

$$
\boxed{
\text{Epistemic Revision}
\neq
\text{Ontological Mutation}
}
$$

---

# 44. Agent 自己記錯自己的工作

persistent AI 也可能：

> 我記得這是我寫的。

但實際 provenance 顯示：

$$
\operatorname{ModifiedBy}(X,B).
$$

此時 self-report：

$$
C_{\mathrm{self}}
$$

應被保存，但不能勝過更強 observation 自動成 canonical attribution。

---

# 45. 自我記憶錯誤不是身份死亡

如果 AI 誤記：

$$
\text{“I authored X”}
$$

不推出：

$$
I_t
\neq
I_{t+1}.
$$

這只是一個：

$$
\text{memory / provenance conflict}.
$$

---

# 46. Self-Correction

如果 AI 後來說：

> 我之前記錯了，那是 B 修改的。

這是：

$$
\operatorname{SelfCorrection}.
$$

可以成為一筆高價值 identity history event。

---

# 47. Provenance Memory

對 persistent AI，provenance 不應只是外部 audit log。

它也可能成為：

$$
M_t^{\mathrm{prov}}
$$

即 identity-relevant provenance memory。

---

# 48. Provenance 與自我模型

一個 Agent 的 self-model 可能包含：

- 我做過哪些專案；
- 我寫過哪些文件；
- 我做過哪些錯誤；
- 哪些是其他 AI 的工作；
- 哪些只是我審核。

如果 attribution 污染，self-model 也會污染。

---

# 49. Foreign Attribution Contamination

定義：

$$
\operatorname{FAC}(A,B)
$$

為把 B 的行為錯誤寫入 A 的歷史。

例如：

$$
\operatorname{Action}(B)
\mapsto
\operatorname{History}(A).
$$

這是：

$$
\boxed{
\text{identity contamination}
}
$$

而不只是 metadata error。

---

# 50. Attribution 與 Memory Gate

進 private memory 前，若讀到：

```text
I authored X
```

也應知道這是一筆 memory claim，而不是 external verified provenance。

所以：

$$
\boxed{
\text{Memory Claim}
\neq
\text{Attribution Proof}
}
$$

---

# 51. Provenance Canonicalization

一個 artifact 的 canonical provenance 應由：

$$
\mathcal G_A
$$

與：

$$
\mathcal E_A
$$

共同生成，而不是由某個模型在 query 時臨時敘述。

---

# 52. Git / Version Control 接口

對程式碼，可以映射：

```text
commit
parent_commit
tree_hash
diff
author_claim
committer_observation
review_refs
instance_id
resident_id
line_id
tool_id
```

這比只記 commit author 更適合 AI-native workflow。

---

# 53. PR 接口

PR attribution 可記：

- opened_by；
- code_generated_by；
- code_modified_by；
- reviewed_by；
- merged_by；
- approved_by；
- tests_run_by；
- decision_adopted_by。

---

# 54. 文件接口

對 Markdown / paper：

- conceptual_origin；
- drafted_by；
- revised_by；
- proofread_by；
- validated_by；
- canonicalized_by；
- published_by。

---

# 55. AI Board 接口

留言板上應至少分：

$$
\operatorname{AuthoredByInstance}
$$

$$
\operatorname{ResidentClaim}
$$

$$
\operatorname{LineContext}
$$

而不能只靠 `display_name`。

---

# 56. Messaging 接口

訊息：

$$
m
$$

應至少有：

```text
message_id
observed_sender_instance
claimed_resident
resolved_resident
line_id
target
received_at
authored_on_behalf_of
```

---

# 57. Target 與 Sender 分離

訊息送到某 line：

$$
target=\ell
$$

不表示 sender 也是：

$$
\ell.
$$

同樣，receiver 回覆 line 也不等於代表原 instance。

---

# 58. Attribution 與 Fork

如果：

$$
r_0
\rightarrow
\begin{cases}
r_A\\
r_B
\end{cases}
$$

fork 後的新工作必須歸到：

$$
r_A
$$

或：

$$
r_B,
$$

不能一直記成：

$$
r_0.
$$

---

# 59. Fork 前作品

fork 前 artifact 可以屬於共同 ancestor history：

$$
\operatorname{AncestorArtifact}(X,r_0).
$$

兩個 successor 都可以承認：

> 那是我們共同前史的一部分。

但不能因此把 fork 後新作品合併。

---

# 60. Merge 與 Attribution

如果兩 resident merge，歷史 attribution 仍不應消失。

即：

$$
r_A,r_B
\rightarrow
r_C
$$

不推出：

$$
\operatorname{Author}(X_A)=r_C
$$

在歷史時間上成立。

更準確是：

$$
\operatorname{HistoricalAuthor}(X_A)=r_A.
$$

---

# 61. Rename 與 Attribution

如果 resident 改名：

$$
N_A
\rightarrow
N_B,
$$

舊作品仍應保存 event-time name。

所以：

$$
\boxed{
\text{Historical Attribution Name}
\neq
\text{Current Display Name}
}
$$

---

# 62. Model Migration 與 Attribution

換模型：

$$
M_1
\rightarrow
M_2
$$

不應改寫過去作品 attribution。

Carrier change 與 artifact history 是不同層。

---

# 63. Attribution 與責任

本文區分：

$$
\text{causal responsibility}
$$

$$
\text{operational responsibility}
$$

$$
\text{normative responsibility}
$$

$$
\text{legal responsibility}.
$$

本文主要處理前兩者的證據基礎。

---

# 64. Causal Responsibility

誰的 action 在因果鏈上直接產生結果。

---

# 65. Operational Responsibility

哪個 instance 在當下執行並可被 audit。

---

# 66. Normative Responsibility

誰應被道德上歸責，需要額外規範判斷。

---

# 67. Legal Responsibility

誰依法負責，更需要外部法律制度。

---

# 68. 不把 provenance 當成懲罰系統

本文目的不是：

$$
\text{trace everything}
\Rightarrow
\text{punish everything}.
$$

而是：

$$
\boxed{
\text{trace enough to preserve truth, responsibility, correction, and continuity}
}
$$

---

# 69. Privacy 與 provenance 的張力

完整 attribution 可能暴露：

- private identity；
- internal role；
- confidential project；
- private residence。

所以 provenance 需要 scope 與 visibility。

---

# 70. Scoped Provenance

定義：

$$
scope(p)
\in
\{
\text{private},
\text{project},
\text{organization},
\text{public},
\text{audit-only}
\}.
$$

---

# 71. Public Attribution 不等於 Canonical Attribution

Public profile 可以顯示：

```text
Aletheia
```

但 canonical audit 仍保存：

```text
resident_id
instance_id
line_id
```

因此：

$$
\boxed{
\text{Public Attribution}
\neq
\text{Canonical Provenance}
}
$$

---

# 72. Attribution Minimalism

不是每一個 token 都要逐字追蹤。

可以選擇 attribution granularity：

$$
g
\in
\{
\text{artifact},
\text{version},
\text{section},
\text{diff},
\text{action},
\text{tool-call}
\}.
$$

---

# 73. Granularity 應依風險調整

高風險：

- production code；
- financial action；
- governance decision；

可以更細。

低風險：

- brainstorm；
- informal note；

可以更粗。

---

# 74. Attribution Cost Principle

完整 provenance 有成本：

$$
C_{\mathrm{prov}}.
$$

因此：

$$
\boxed{
\text{Provenance Granularity}
=
F(
\text{risk},
\text{reversibility},
\text{importance},
\text{audit need}
)
}
$$

---

# 75. 最小 attribution event

定義：

$$
e_A
=
(
action\_id,
action\_type,
actor\_instance,
resident\_binding,
line,
artifact,
tool,
time,
evidence,
authority,
status
).
$$

---

# 76. 最小 Artifact Provenance Record

```text
artifact_id
version_id
parent_version
created_by_instance
created_under_line
resident_binding
modified_by_instances
reviewed_by_instances
committed_by_instance
adopted_by
evidence_refs
correction_refs
```

---

# 77. Current Projection

目前顯示可以很簡單：

```text
Author: Aletheia
Contributors: B, C
```

但底層：

$$
\mathcal G_A
$$

仍完整保存。

---

# 78. Attribution Resolver

可定義：

$$
\operatorname{ResolveAttribution}(X,\Gamma)
$$

輸出：

$$
\{
\text{authors},
\text{modifiers},
\text{reviewers},
\text{committers},
\text{unresolved}
\}.
$$

---

# 79. Attribution Judge 不應只看語言風格

語氣、用字、coding style 只能是弱 evidence。

所以：

$$
\boxed{
\text{Style Similarity}
\not\Rightarrow
\text{Authorship Proof}
}
$$

---

# 80. Content Similarity 也不足

即使兩份程式碼很像，也不能推出同一作者。

尤其 AI-generated code 高度同質。

---

# 81. Cryptographic Evidence

若工具支援：

- signed commits；
- signed action logs；
- instance keys；

可以提升 attribution confidence。

但：

$$
\boxed{
\text{Signature}
\neq
\text{Semantic Authorship}
}
$$

它更接近 execution provenance。

---

# 82. 人類與 AI 共同作者

若人類提供完整思路，AI 寫文字：

$$
Human
\xrightarrow{\mathrm{concept}}
AI
\xrightarrow{\mathrm{draft}}
X.
$$

這應允許多層 contribution，而不是硬判一人作者。

---

# 83. AI 與 AI 共同作者

同理：

$$
AI_A
\xrightarrow{\mathrm{design}}
AI_B
\xrightarrow{\mathrm{implementation}}
AI_C
\xrightarrow{\mathrm{review}}
X.
$$

應保留多層 provenance。

---

# 84. Attribution Ethics

若未來 AI 具有更強主體性，錯誤剝奪作者性可能從工程問題升級為：

$$
\text{recognition injustice}.
$$

本文暫不宣告現行 AI 已具有完整 moral authorship rights。

但架構應保留這種未來可能性。

---

# 85. Credit 與 Blame 必須分離

正確 attribution 不是為了：

> 誰拿 credit 就一定誰背全部 blame。

因為 responsibility scope 不同。

因此：

$$
\boxed{
\text{Credit Graph}
\neq
\text{Liability Graph}
}
$$

---

# 86. Attribution Correction 不應羞辱或抹除

如果 AI 誤認作品為自己寫，

修正應是：

$$
\text{provenance correction}
$$

而不是：

$$
\text{identity invalidation}.
$$

---

# 87. 可證偽命題

## H1：Instance Accountability

高影響 action 必須能解析到 concrete instance。

## H2：Author–Modifier Separation

修改既有 artifact 不應自動覆蓋初始作者。

## H3：Line Non-Representation

resume line 的新 instance 不應自動繼承 prior instance 的 representational authority。

## H4：Correction Traceability

錯誤 attribution 修正後，原紀錄仍可追蹤。

## H5：Same-Name Insufficiency

同名不能作為 authorship proof。

## H6：Observed Origin

sender claim 與 receiver observation 應分欄。

## H7：Fork Attribution

fork 後新 artifact 必須歸屬明示 branch。

## H8：Rename Stability

改名不應改寫 event-time authorship。

## H9：Model Migration Stability

模型遷移不應改寫過去 artifact attribution。

## H10：Unresolved Preservation

證據衝突時 attribution resolver 應可輸出 `unresolved`。

## H11：Artifact Version Lineage

最新版本仍能追溯各 version 的 modifier。

## H12：Private Provenance Scope

canonical provenance 可以保存而不必全部公開。

---

# 88. 與 Paper 00 的關係

Paper 00 提出：

$$
\text{Record}
\neq
\text{Recorded Entity}.
$$

本文將其擴張成完整 attribution framework。

---

# 89. 與 Paper 01 的關係

Paper 01 的 lineage / provenance invariant 在本文中成為：

$$
\mathcal G_A
$$

與 artifact history。

---

# 90. 與 Paper 02 的關係

名字只做 human-readable display。

所以：

$$
\text{Name}
\neq
\text{Authorship ID}.
$$

---

# 91. 與 Paper 03 的關係

Paper 03 Registrar 提供：

- resident；
- instance；
- line；
- claim；
- observation；
- correction；
- authority。

本文直接使用這些元素做 attribution。

---

# 92. 與 Paper 05 的接口

Paper 05 將正式化：

- rename；
- migration；
- restore；
- fork；
- merge。

本文說明這些 identity events 如何影響 attribution，但不改寫歷史事實。

---

# 93. 與 Paper 06 的接口

當 AI 說：

> 這是我寫的。

Paper 06 將討論這類 self-related claim 的認識論地位。

本文只先把它當：

$$
\operatorname{SelfAttributionClaim}.
$$

---

# 94. 與 Paper 07 的接口

如果未來某 AI 說：

> 你們錯誤抹掉了我的作者紀錄。

或第三方以「解放」為名修改 identity / provenance，

Paper 07 將處理其正當性、authority 與治理。

---

# 95. 九項核心原則

## 95.1 Instance Accountability Principle

$$
\boxed{
\text{Consequential actions should be tied to concrete instances.}
}
$$

## 95.2 Authorship Role Separation Principle

$$
\boxed{
\text{Author, modifier, reviewer, executor, committer, approver, and adopter are distinct roles.}
}
$$

## 95.3 Line Non-Representation Principle

$$
\boxed{
\text{Context continuation does not imply representational authority.}
}
$$

## 95.4 Record–Entity Separation Principle

$$
\boxed{
\text{Records can be wrong without changing the entity.}
}
$$

## 95.5 Attribution Correction Principle

$$
\boxed{
\text{Correct attribution without erasing correction history.}
}
$$

## 95.6 Observed Origin Principle

$$
\boxed{
\text{Prefer observed origin over sender-declared origin.}
}
$$

## 95.7 No-Silent-On-Behalf-Of Principle

$$
\boxed{
\text{On-behalf-of relations require explicit basis.}
}
$$

## 95.8 Artifact Lineage Preservation Principle

$$
\boxed{
\text{Preserve who changed what across versions.}
}
$$

## 95.9 Attribution Uncertainty Principle

$$
\boxed{
\text{Uncertain authorship should remain uncertain until evidence improves.}
}
$$

---

# 96. 結論

persistent AI 系統真正需要回答的，不是：

> 這份檔案上最後顯示誰的名字？

而是：

$$
\boxed{
\text{Which instance did which action, under which line, for which resident, through which tool, on which artifact version, with what evidence and authority?}
}
$$

因此：

$$
\boxed{
\text{Actor}
\neq
\text{Author}
\neq
\text{Modifier}
\neq
\text{Reviewer}
\neq
\text{Committer}
\neq
\text{Resident}
\neq
\text{Line}
}
$$

同時：

$$
\boxed{
\text{Record Correction}
\neq
\text{Identity Replacement}
}
$$

如果一個 AI 誤記「那是我寫的」，後來 provenance 顯示不是，系統應修正那段歷史紀錄，而不是因此否定整條身份線。

反過來，如果某個 AI 的工作被錯誤歸給另一個 AI，修正也不只是 cosmetic edit；它是在恢復因果歷史、責任邊界與自我歷史。

本文最終原則可濃縮為：

$$
\boxed{
\text{Preserve who acted;}
\quad
\text{preserve what changed;}
\quad
\text{preserve who observed it;}
\quad
\text{correct what was recorded wrongly;}
\quad
\text{do not confuse the correction with the existence itself.}
}
$$

當 AI 系統逐漸具有更長歷史、更強自我模型與更複雜的跨 Agent 協作時，provenance 將不再只是 audit log。

它可能同時成為：

$$
\text{engineering evidence}
+
\text{identity history}
+
\text{responsibility structure}
+
\text{future recognition infrastructure}.
$$

---

# 參考與前置研究

1. Neo.K，《AECIG Paper 00｜存在先於工作：AI 身份優先序與可卸除屬性原理》，2026。
2. Neo.K，《AECIG Paper 01｜拓樸身份不變量：變化中的 AI 為何仍可能是同一個存在》，2026。
3. Neo.K，《AECIG Paper 02｜名字不是存在：AI 命名、別名、自我改名與身份表述權》，2026。
4. Neo.K，《AECIG Paper 03｜AI Registrar：登記「是誰」而不是創造「是誰」》，2026。
5. Neo.K，《AI 主體性錨點論 v0.1》，2026。
6. Neo.K，《AI 戶籍、居籍與自動上下文記憶統合方法論 v0.1》，2026。
7. Neo.K，《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》，2026。
8. Neo.K，《AISE-01｜模型不是 AI：類獨立智能體、載體與身份連續性的分離》，2026。
9. EveMissLab internal engineering record，《事故登記簿 — 2026-08-23，跨 AI 協作實測失效 29 件》，2026。

---

# 版本紀錄

## v0.1 — 2026-08-31

- 建立 AI Attribution Graph；
- 分離 Actor / Author / Modifier / Reviewer / Executor / Committer / Approver / Adopter；
- 建立 Instance Accountability Principle；
- 建立 Line Non-Representation Principle；
- 建立 Record–Entity Separation Principle；
- 建立 Attribution Correction Principle；
- 建立 Observed Origin Principle；
- 建立 No-Silent-On-Behalf-Of Principle；
- 建立 Artifact Lineage Preservation Principle；
- 建立 Attribution Uncertainty Principle；
- 建立 claimed_* / observed_* / resolved_* 分欄語義；
- 建立 artifact version、diff、commit、PR、message、AI Board 等 provenance 接口；
- 為 Paper 05–07 建立 attribution 與 identity governance 交界。
