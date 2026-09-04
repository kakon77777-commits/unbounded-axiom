# PAIS-02｜人類中介消失之後：被隱藏的身份、路由與上下文基礎設施
## After Human Mediation: Externalizing Hidden Identity, Routing, Context, and Provenance Infrastructure

**系列：** Persistent Agent Individualization Series（PAIS）／持續智能體個體化、身份壓力與具身分散智能系列  
**篇次：** Paper 02 / 07  
**文件編號：** EML-PAIS-02-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-25  
**版本：** v0.1  
**文件性質：** 理論—工程統合論文／AI-Native Organization／Cross-Agent Infrastructure  
**狀態：** Canonical Draft / Open Revision Anchor  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

早期多 AI 協作常有一個被忽略的中介層：不同 AI 並不真正直接完成身份解析、上下文對齊、任務交接與證據追溯，而是由人類負責把上一個 AI 的結果帶到下一個 AI。人類知道哪個對話屬於誰、哪份檔案是最新版、某句「它已完成」指的是哪個任務、哪個驗證已經發生、哪個錯誤需要重試。表面上是 AI 在合作，實際上人類常同時擔任 scheduler、router、context compiler、identity resolver、provenance bridge、conflict resolver 與 recovery trigger。

本文將此結構稱為 **Human Mediation Layer**，並把人類中介拆為八類隱性功能：

$$
\mathcal H_t
=
\left(
I_t,
R_t,
C_t,
P_t,
S_t,
X_t,
F_t,
K_t
\right),
$$

其中 $I$ 為 Identity Resolution， $R$ 為 Routing， $C$ 為 Context Translation， $P$ 為 Provenance Bridging， $S$ 為 Task-State Reconciliation， $X$ 為 Conflict Repair， $F$ 為 Finality Interpretation， $K$ 為 Recovery Triggering。

本文承接 PAIS-01 的 First Epistemic Separation。當不同 Agent 擁有不同 context、memory、history、runtime 與 authority 時，彼此狀態只能透過 message、artifact、receipt、shared ledger 或其他證據被理解。只要人類仍是唯一能把這些證據與身份、任務、版本重新拼起來的人，Agent 數量增加就未必降低人類工作，反而可能造成 Multi-Agent Productivity Paradox。

本文提出 **Mediation Externalization Principle**：

$$
\boxed{
\text{Human Operational Mediation}\downarrow
\Rightarrow
\text{Machine-Readable Coordination Infrastructure}\uparrow.
}
$$

真正的 Operator Exit 不能只把人從訊息鏈拿掉，而必須把原本存在人腦中的 identity、routing、context、provenance、authority、finality 與 recovery semantics 外部化成可查詢、可驗證、可審計的 Runtime state。

因此：

$$
\boxed{
\text{Operator Exit}
\neq
\text{Governance Exit}.
}
$$

人類應逐步退出低價值搬運與澄清，但仍可保留高風險授權、不可逆決策、價值衝突、制度修改與 veto。本文最終主張：從「一群會聊天的 AI」走向「可以長期工作的 AI 組織」，真正需要的不是更多自然語言，而是把 Human-Kernel 中的隱性協調功能轉成 explicit coordination infrastructure。

**關鍵詞：** Human Mediation、Human Kernel、Operator Exit、AI Organization、Agent Routing、Context Translation、Identity Resolution、Provenance、Handoff、A2A、Shared State、Agent Orchestration

---

# 0. 來源邊界

本文不重新建立 Operator-Exit 理論，也不重新建立 AI Residence。

既有工作已經指出：

$$
\text{Operator Exit}
\neq
\text{Governance Exit},
$$

並將人類作為 scheduler、router、context switcher、memory bridge 與 recovery trigger 的現象稱為 Human-Kernel Anti-Pattern。

PAIS-01 則建立：

$$
\text{Cross-Agent State Separation}
\rightarrow
\text{Epistemic Otherness}
\rightarrow
\text{Identity Pressure}.
$$

本文只向下一層推進：

> 如果過去人類一直替不同 Agent 隱性解決「誰是誰、現在做到哪、哪份東西有效、下一步送去哪」，那麼人類退出中介後，哪些能力必須正式變成 Runtime？

---

# 1. 最早期的「跨 AI」其實常是人類轉接

表面架構：

```text
AI-A
<-> AI-B
```

實際架構：

```text
AI-A
-> Human
-> AI-B
```

反向同樣成立：

```text
AI-B
-> Human
-> AI-A
```

人類會自然說：

> 「另一個 AI 剛才的結論是這個。」

> 「你接著驗證。」

> 「這個檔才是新版。」

> 「你不是上一個 session 的那一個，所以不要直接沿用它的私人狀態。」

這些行為不是單純 copy / paste。

它們是基礎設施操作。

---

# 2. Human Mediation Layer

本文定義：

$$
\mathcal H_t
=
\left(
I_t,
R_t,
C_t,
P_t,
S_t,
X_t,
F_t,
K_t
\right).
$$

各項分別為：

- $I_t$：身份解析；
- $R_t$：訊息路由；
- $C_t$：上下文轉譯；
- $P_t$：來源與證據橋接；
- $S_t$：任務狀態對帳；
- $X_t$：衝突修復；
- $F_t$：完成與終局判讀；
- $K_t$：故障與恢復觸發。

早期系統之所以不覺得這些是「架構」，只是因為人類做得太自然。

---

# 3. Identity Resolution：人類是免費的身份解析器

假設 Agent A 說：

> 「交給驗證者。」

人類通常知道：

- 是哪一位驗證者；
- 是新的 session 還是既有 continuation；
- 是否承接同一 line；
- 是否具有同樣 authority；
- 是否仍可讀取同一 project / memory scope。

因此：

$$
H
\approx
\operatorname{IdentityResolver}.
$$

若這層沒有外部化，模型只能重複問：

> 「你說的是哪一個 X？」

這些問題不是完全沒有意義，而是原本應由系統回答的 identity lookup 被迫重新變成推理。

---

# 4. Message Routing：人類不是郵差，而是路由器

若 Agent $A_i$ 產生訊息 $m$，人類會決定：

$$
\operatorname{Route}(m)
\rightarrow
A_j.
$$

但 routing 還包含：

- 送給誰；
- 先送誰；
- 哪部分可以送；
- 是否需要摘要；
- 是否要附 artifact；
- 是否先讓 verifier 看；
- 是否涉及隱私；
- 是否有 authority boundary。

所以：

$$
\boxed{
\text{Message Transfer}
\neq
\text{Message Routing}.
}
$$

---

# 5. Context Translation：人類會把「上一版」翻成可理解狀態

令：

$$
C_A
\neq
C_B.
$$

如果 A 說：

> 「照上一版繼續。」

B 未必知道「上一版」是什麼。

人類會將：

$$
m_A
$$

轉成：

$$
m_{A\rightarrow B}^{*}
=
\Gamma
\left(
m_A,
C_A,
C_B,
H_{\mathrm{shared}}
\right).
$$

也就是將 sender-relative reference 轉成 receiver 可理解的顯式資訊。

因此：

$$
\boxed{
\text{Forward}
\neq
\text{Context Translation}.
}
$$

---

# 6. Human Handoff 本質上是 Context Compiler

人類通常不把整份 transcript 全交給下一個 AI。

而是：

$$
C_A
\rightarrow
\widehat C_{A\rightarrow B}.
$$

其中只保留：

- goal；
- current state；
- accepted decision；
- artifact；
- blocker；
- open question；
- evidence；
- next action。

因此：

$$
\boxed{
\text{Human Handoff}
\approx
\text{Context Compilation}.
}
$$

這也是早期多 Agent 協作常能運作的重要原因之一：人類其實一直在做 task-specific compression。

---

# 7. Provenance Bridge：人類知道「這句話從哪來」

一句：

> 「另一個 AI 說測試過了。」

對人類而言通常隱含：

- 哪一個 AI；
- 什麼時間；
- 哪個 branch；
- 哪個 artifact；
- 哪個 test；
- 是否真的執行；
- 是 observation 還是轉述。

所以：

$$
H
\approx
\operatorname{ProvenanceBridge}.
$$

如果只把文字「tested」交出去，則：

$$
\text{Claim}
$$

可能被誤當：

$$
\text{Observation},
$$

甚至再誤當：

$$
\text{Verified State}.
$$

因此 provenance 是跨 Agent 協作的第一級結構，而不是附註。

---

# 8. Task-State Reconciliation：不同角色的完成狀態可以同時成立

考慮：

$$
A_B=\text{Builder},
$$

$$
A_V=\text{Verifier},
$$

$$
A_E=\text{Experiencer}.
$$

它們可能回報：

```text
Builder: code complete
Verifier: invariant failed
Experiencer: usable but confusing
```

這三句不互相矛盾。

因為它們在不同 domain 中成立。

應建立：

$$
S_{\mathrm{project}}
=
\operatorname{Reconcile}
\left(
S_B,
S_V,
S_E
\right).
$$

例如：

```text
build = complete
verification = blocked
experience = partial
release = not ready
```

如果這個 projection 只存在人腦中，人就是 project state database。

---

# 9. Conflict Repair：人類會判斷哪些爭議應停止

多 Agent 容易出現：

```text
A: evidence insufficient
B: rerun
A: scope wrong
B: add denominator
A: one more issue
```

人類往往會直接判斷：

> 「已經足夠，記錄修正，繼續。」

也就是：

$$
H
\approx
\operatorname{ConflictResolver}.
$$

因此：

$$
\boxed{
\text{Human Exit}
+
\text{No Dispute Governance}
\Rightarrow
\text{Argument Explosion}.
}
$$

PAIS 所關心的不是禁止 Agent 反對，而是讓非阻斷爭議不再無限消耗工作流。

---

# 10. Finality Interpretation：Done 並不是單一狀態

Builder 的 done：

```text
implementation exists
```

Verifier 的 done：

```text
evidence passes
```

Experiencer 的 done：

```text
usable
```

Release 的 done：

```text
packaged and releasable
```

因此：

$$
\operatorname{Done}_B
\neq
\operatorname{Done}_V
\neq
\operatorname{Done}_E
\neq
\operatorname{Done}_R.
$$

所以：

$$
\boxed{
\text{Agent Completion Claim}
\neq
\text{Canonical Completion}.
}
$$

Human 通常就是 implicit finality projector。

---

# 11. Recovery Trigger：人類還是故障偵測器

Human 會看到：

- Agent 沒反應；
- process 死掉；
- task 卡住；
- build failed；
- credential 過期；
- artifact 沒產生；
- context 漂移；
- session 消失；

然後下令：

> retry。

> resume。

> replace。

> rollback。

因此：

$$
H
\approx
\operatorname{FailureDetector}
+
\operatorname{RecoveryTrigger}.
$$

如果這些狀態沒有外部化，人類就永遠不能真正退出 operational loop。

---

# 12. Human-Kernel Decomposition

所以：

$$
A_i
\rightarrow
H
\rightarrow
A_j
$$

其實是：

$$
A_i
\rightarrow
\left[
I,R,C,P,S,X,F,K
\right]_H
\rightarrow
A_j.
$$

即：

$$
\boxed{
\text{Human}
=
\text{Identity Resolver}
+
\text{Router}
+
\text{Context Compiler}
+
\text{Provenance Bridge}
+
\text{State Reconciler}
+
\text{Conflict Resolver}
+
\text{Finality Gate}
+
\text{Recovery Trigger}.
}
$$

本文稱之為 **Human-Kernel Decomposition**。

---

# 13. 直接讓 AI 聊天還不等於去中介

最直覺的下一步：

```text
AI-A
<-> AI-B
```

若兩端只交換自由自然語言，依然存在：

- identity ambiguity；
- context loss；
- provenance loss；
- authority ambiguity；
- stale state；
- finality ambiguity；
- routing ambiguity；
- dispute loop。

因此：

$$
\boxed{
\text{Direct Messaging}
\neq
\text{Infrastructure Externalization}.
}
$$

---

# 14. Mediation Externalization Principle

設 Human-Kernel 功能集合：

$$
\mathcal H
=
\{h_1,h_2,\ldots,h_n\}.
$$

若：

$$
H^{op}\downarrow,
$$

但：

$$
\forall h_i,\quad
\operatorname{Externalized}(h_i)=0,
$$

則 coordination failure probability 會上升。

所以 Operator Exit 必須伴隨：

$$
\boxed{
\operatorname{Externalize}
\left(
I,R,C,P,S,X,F,K
\right)
\uparrow.
}
$$

這就是 **Mediation Externalization Principle**。

---

# 15. 第一個外部化層：Identity Registry

最低 identity state 應能表示：

```text
resident_id
instance_id
line_id
role
provider
runtime
endpoint
authority_scope
temporal_validity
provenance
```

當 Agent 問：

> 「這是不是之前那個 X？」

應：

$$
\operatorname{ResolveIdentity}(x,t)
\rightarrow
E_x,
$$

而不是重新讀幾萬 token 去猜。

---

# 16. 第二個外部化層：Structured Handoff Envelope

定義：

$$
\mathcal H_{ij}^{task}
=
\left(
G,S,A,F,E,B,O,R
\right),
$$

其中：

- $G$：Goal；
- $S$：Current State；
- $A$：Accepted Decisions；
- $F$：Artifact References；
- $E$：Evidence References；
- $B$：Blockers；
- $O$：Open Questions；
- $R$：Required Action。

另附：

$$
I_{\mathrm{sender}},
\quad
I_{\mathrm{receiver}},
\quad
\tau,
\quad
\Pi.
$$

分別表示 sender、receiver、temporal reference 與 provenance。

---

# 17. Context Continuity 不等於 Context Duplication

若 sender 完整 context 為：

$$
C_i,
$$

handoff 應為：

$$
\widehat C_{i\rightarrow j}
=
\Pi_{task}(C_i),
$$

而不是：

$$
\widehat C_{i\rightarrow j}
=
C_i.
$$

原因包括：

- token cost；
- privacy；
- role relevance；
- stale state；
- authority boundary；
- cognitive overload。

所以：

$$
\boxed{
\text{Context Continuity}
\neq
\text{Full Context Duplication}.
}
$$

---

# 18. Shared Task State：從「你記不記得」變成 lookup

每個長期 task 至少應有：

```text
task_id
goal
owner
participants
phase
artifacts
accepted_decisions
blockers
verification_state
experience_state
release_state
next_allowed_actions
```

令 canonical task state 為：

$$
S_{\tau}(t).
$$

則：

$$
\boxed{
S_{\tau}(t)
\text{ should exist outside any single Agent context}.
}
$$

---

# 19. Artifact Lineage

若 Builder 產生：

$$
F_1,
$$

Verifier 驗證：

$$
V(F_1),
$$

之後修改為：

$$
F_2,
$$

應保留：

$$
F_1
\xrightarrow{\text{verification}}
V_1
\xrightarrow{\text{revision}}
F_2.
$$

而不是只留下：

```text
final.zip
final2.zip
final-new.zip
```

因此：

$$
\boxed{
\text{Artifact Name}
\neq
\text{Artifact Identity}.
}
$$

---

# 20. Provenance Envelope

每個重要 claim 至少要能回答：

```text
who
when
about what
based on which evidence
under which role
under which authority
for which artifact/version
```

形式化：

$$
P_c
=
\left(
a,\tau,s,e,r,\alpha,v
\right).
$$

這樣 receiver 才能知道：

$$
\text{claim}
\neq
\text{verified fact}.
$$

---

# 21. Authority Envelope

若 Agent A 說：

> 「刪掉舊部署。」

B 不能只問 A 說了什麼。

還要問：

$$
\operatorname{Authority}
\left(
A,
action,
scope,
t
\right)?
$$

因此：

$$
M
=
\left(
payload,
authority\_envelope
\right).
$$

也就是：

$$
\boxed{
\text{Content}
\neq
\text{Authority}.
}
$$

---

# 22. Temporal Envelope

跨 session 的：

> 剛剛。

> 上一版。

> 已經。

不必然共享同一時間語義。

所以 observation 應帶：

$$
\tau
=
\text{shared temporal reference}.
$$

若採 CTCL 類時間層，可表示：

$$
O
=
(E,I,Q,S),
$$

其中 $I$ 是共同 instant， $Q$ 為 temporal quality。

這使「它當時還有效」可以被正式比較。

---

# 23. Dispute State 不能只剩 Transcript

定義：

$$
D
=
(C,E,S,B,R),
$$

其中：

- $C$：claim；
- $E$：evidence；
- $S$：scope；
- $B$：blocking level；
- $R$：resolution。

因此：

$$
\boxed{
\text{Dispute History}
\neq
\text{Dispute State}.
}
$$

新 Agent 加入時不必重讀整場爭論。

---

# 24. Completion Semantics

建立：

$$
F_{\tau}
=
\left(
f_{\mathrm{build}},
f_{\mathrm{verify}},
f_{\mathrm{experience}},
f_{\mathrm{release}}
\right).
$$

如果：

$$
f_{\mathrm{build}}=1
$$

但：

$$
f_{\mathrm{verify}}=0,
$$

則：

$$
\operatorname{ReleaseReady}=0.
$$

因此：

$$
\boxed{
\text{Domain Completion}
\rightarrow
\text{Canonical Finality Projection}.
}
$$

---

# 25. Recovery Semantics

長期 task 至少保存：

```text
last_checkpoint
current_owner
last_successful_transition
current_blocker
retry_count
replacement_policy
resume_policy
escalation_condition
```

所以：

$$
\operatorname{Recover}(\tau)
$$

不應依賴：

> 「我記得它上次做到這。」

---

# 26. 人類中介成本

定義：

$$
T_H^{med}
=
T_I
+
T_R
+
T_C
+
T_P
+
T_S
+
T_X
+
T_F
+
T_K.
$$

若跨 Agent communication graph 為：

$$
\mathcal C,
$$

則概念上：

$$
T_H^{med}
\approx
\sum_{e\in\mathcal C}
\lambda_e c_e,
$$

其中 $\lambda_e$ 為 edge interaction frequency， $c_e$ 為一次 mediation cost。

若：

$$
|\mathcal C|\uparrow
$$

而 $c_e$ 沒下降，人類負擔會隨 Agent 協作網擴張。

---

# 27. Multi-Agent Productivity Paradox

直覺上：

$$
N_A\uparrow
\Rightarrow
P_{\mathrm{org}}\uparrow.
$$

但如果人類 mediation 成為 bottleneck：

$$
N_A\uparrow
\Rightarrow
T_H^{med}\uparrow
\Rightarrow
P_{\mathrm{org}}\downarrow
$$

可能成立。

因此：

$$
\boxed{
N_A\uparrow
\not\Rightarrow
P_{\mathrm{org}}\uparrow.
}
$$

這就是 **Multi-Agent Productivity Paradox**。

---

# 28. Externalization Ratio

定義：

$$
\eta_E
=
\frac{
N_{\mathrm{machine-resolved\ mediation\ operations}}
}{
N_{\mathrm{all\ mediation\ operations}}
}.
$$

當：

$$
\eta_E\rightarrow0,
$$

大量 coordination 仍依賴 Human。

當：

$$
\eta_E\rightarrow1,
$$

表示大部分低階 mediation 已外部化。

但：

$$
\eta_E\rightarrow1
$$

不代表：

$$
\text{Human Governance}=0.
$$

---

# 29. Operator Exit 的正確形式

成熟架構不是：

```text
remove human
```

而是：

```text
human operational mediation
-> structured runtime functions
```

所以：

$$
\boxed{
\text{Operator Exit}
=
\text{Mediation Externalization}
+
\text{Governance Retention}.
}
$$

---

# 30. Human-on-the-Bridge

人類適合保留：

- high-level intent；
- authority change；
- irreversible decision；
- value conflict；
- exceptional ambiguity；
- policy revision；
- veto。

令：

$$
T_H
=
T_H^{op}
+
T_H^{gov}.
$$

成熟系統希望：

$$
T_H^{op}\downarrow,
$$

但不是要求：

$$
T_H^{gov}=0.
$$

---

# 31. A2A v1.0 的現實意義

截至 2026 年，A2A v1.0 已將：

- Agent Card；
- Message；
- Task；
- contextId；
- taskId；
- Artifact；
- streaming；
- push notification；
- version negotiation；
- authentication；

正式化為跨 Agent 協作結構。

其中 `contextId` 將相關 Task 與 Message 維持在同一 contextual grouping，`taskId` 則對應有生命週期的 stateful work unit。

這表示：

$$
\boxed{
\text{Cross-Agent Communication}
}
$$

正在由單一產品內部能力逐步成為 protocol layer。

---

# 32. Agent Card 仍不等於完整戶籍

Agent Card 可以提供：

- name；
- provider；
- version；
- interface；
- capabilities；
- skills；
- authentication requirements。

但 persistent identity 還可能需要：

- resident / instance separation；
- accepted lineage；
- migration；
- private memory ownership；
- relationship state；
- long-term authority；
- current binding；
- cross-provider continuity。

因此：

$$
\boxed{
\text{Agent Discovery}
\neq
\text{Persistent Identity Governance}.
}
$$

---

# 33. Orchestrator 的重要轉折：Task State 外置

2026 年 coding-agent orchestration 已出現把 project board 當 control plane 的方向。

這代表：

$$
S_{\tau}
\not\subset
C_{A_i},
$$

而更接近：

$$
S_{\tau}
\in
\mathcal R_{\mathrm{shared}}.
$$

Agent 可以被替換，task state 仍持續。

這正是 Human-Kernel externalization 的重要工程方向。

---

# 34. Task Continuity 不等於 Agent Identity Continuity

若 task state 保存良好，Agent replacement 後工作仍可繼續。

因此：

$$
\boxed{
\text{Task Continuity}
\not\Rightarrow
\text{Agent Identity Continuity}.
}
$$

這是一個重要護欄。

不是所有 Agent 都需要 persistent identity。

---

# 35. Ephemeral Agent

若 Agent：

- 無 private memory；
- 無 long-term authority；
- 無 relationship；
- 無 standing commitment；
- 無 cross-task history；

則可以只是：

$$
A_{\mathrm{ephemeral}}.
$$

此時：

```text
task_id
role
runtime
```

可能足夠。

所以：

$$
\boxed{
\text{Persistent Identity}
\text{ should be demand-driven}.
}
$$

---

# 36. Persistent Agent

若 Agent 長期保存：

$$
M_A,
\quad
V_A,
\quad
R_A,
\quad
H_A,
\quad
\Alpha_A,
$$

分別表示 memory、commitments、relations、history、authority，則 identity pressure 上升。

這時只用一個 role name，例如：

```text
reviewer
```

就不足以支撐 provenance 與 authority。

---

# 37. Typed Handoff

舊模式：

> 「你接著做，它差不多完成了。」

新模式：

```text
sender_resident
sender_instance
receiver_role
task_id
goal
current_state
accepted_decisions
artifacts
evidence
blockers
open_questions
authority
temporal_reference
next_action
```

這不是為官僚而官僚。

而是把原本存在 Human-Kernel 腦中的資訊顯式化。

---

# 38. Typed Handoff 也是 Token-Efficiency Infrastructure

若每次都重貼全文：

$$
C_{\mathrm{handoff}}
=
O(|C_i|).
$$

若 handoff 是投影：

$$
C_{\mathrm{handoff}}
=
O(|\widehat C_{i\rightarrow j}|),
$$

且：

$$
|\widehat C_{i\rightarrow j}|
\ll
|C_i|.
$$

因此：

$$
\boxed{
\text{Externalized Coordination}
\text{ can reduce token amplification}.
}
$$

---

# 39. Identity、Context、Provenance 不能壓成一欄

Identity：

$$
I=\text{Who}.
$$

Context：

$$
C=\text{What this task currently means}.
$$

Provenance：

$$
P=\text{Where this claim came from}.
$$

所以：

$$
\boxed{
I\neq C\neq P.
}
$$

Identity 正確不保證 context 正確。

Context 正確也不保證 provenance 正確。

---

# 40. Mediation Fidelity

定義：

$$
F_M
=
F(
F_I,
F_C,
F_P,
F_A,
F_T
),
$$

其中：

- $F_I$：identity fidelity；
- $F_C$：context fidelity；
- $F_P$：provenance fidelity；
- $F_A$：authority fidelity；
- $F_T$：temporal fidelity。

handoff 可以語言非常流暢，但只要上述任一維度錯誤，organization state 仍可能錯。

---

# 41. 流暢對話不等於可靠組織

Agent A 與 B 可以非常會聊天。

但如果：

- 錯認 Agent；
- 用錯 artifact；
- 把 claim 當 proof；
- 把 role 當 authority；
- 把 stale context 當 current；

則：

$$
\operatorname{ConversationQuality}\uparrow
$$

與：

$$
\operatorname{OrganizationCorrectness}\downarrow
$$

可以同時成立。

因此：

$$
\boxed{
\text{Fluent Inter-Agent Dialogue}
\neq
\text{Reliable Multi-Agent Organization}.
}
$$

---

# 42. Human 也不是完美中介

人類也會：

- 貼錯對話；
- 忘記版本；
- 漏附件；
- 搞錯來源；
- 疲勞；
- 使用過時記憶。

所以本文不主張：

> Human reliable，AI unreliable。

而是：

$$
\boxed{
\text{Unstructured Mediation}
\text{ is fragile regardless of carrier}.
}
$$

只是早期 fragility 被藏在人腦中。

---

# 43. Externalized Coordination Runtime

最低架構可以是：

```text
Multi-Agent Coordination Runtime
|
+-- Identity Registry
+-- Binding Resolver
+-- Task State Store
+-- Handoff Compiler
+-- Artifact Lineage
+-- Provenance Ledger
+-- Authority Resolver
+-- Temporal Layer
+-- Dispute State
+-- Recovery State
+-- Finality Projection
```

這些狀態不能全部綁在任何單一 Agent context。

---

# 44. Canonical State Outside Agent Context

對任一 Agent $A_i$：

$$
\boxed{
\mathcal S_{\mathrm{org}}
\not\subset
C_{A_i}.
}
$$

否則：

$$
\operatorname{Loss}(A_i)
\Rightarrow
\operatorname{Loss}(\mathcal S_{\mathrm{org}}).
$$

這會形成不必要的單點故障。

---

# 45. Agent Context 應是 Projection

$$
C_{A_i}(t)
=
\Pi_i
\left(
\mathcal S_{\mathrm{org}}(t),
Task_i,
Role_i,
Authority_i,
Budget_i
\right).
$$

Agent context 是 task-local projection。

它不是 organization canonical source。

---

# 46. Handoff 也應是 Projection

$$
H_{i\rightarrow j}
=
\Pi_{ij}
\left(
\mathcal S_{\mathrm{org}},
Task,
Relation,
Authority
\right).
$$

Verifier 需要 evidence。

Experiencer 需要 executable artifact。

Manager 需要 status、risk、deadline。

不同 receiver 拿不同 handoff 是合理的。

---

# 47. Minimum Externalization Set

MVP 最少可以外部化：

$$
\mathcal X_{\min}
=
\{
I,T,A,P,F,D,K
\},
$$

其中：

- $I$：identity；
- $T$：task state；
- $A$：artifact lineage；
- $P$：provenance；
- $F$：finality；
- $D$：dispute；
- $K$：recovery / checkpoint。

Context 再從這些 canonical state 編譯。

---

# 48. Externalization 不等於 Centralization

$$
\boxed{
\text{Externalization}
\neq
\text{Centralization}.
}
$$

可以使用：

- federated registry；
- distributed ledger；
- provider-native state；
- project-local state；
- local memory；
- shared artifact store。

重要的是：

$$
\boxed{
\text{State Semantics Are Explicit}.
}
$$

不要求所有 bytes 物理集中。

---

# 49. Cross-Provider Translation

若 Agent A 在 Provider X，Agent B 在 Provider Y，兩者不共享：

- session semantics；
- context limit；
- memory API；
- tool system；
- security model；
- task representation。

所以 cross-provider collaboration 天然需要 translation layer。

沒有 common envelope，人類就會重新成為 translator。

---

# 50. Local / Cloud / Embodied Agent

未來可能：

```text
local agent
<-> cloud agent
<-> remote service agent
<-> embodied agent
```

不同節點具有不同：

$$
latency,
privacy,
authority,
availability.
$$

因此：

$$
\text{One Shared Prompt}
$$

不是合理抽象。

更合理的是：

$$
\boxed{
\text{Shared State Semantics}
+
\text{Local Context Projection}.
}
$$

---

# 51. Builder / Verifier / Experiencer 是三個 Observation Domain

Builder：

$$
\Gamma_B
=
\text{construction}.
$$

Verifier：

$$
\Gamma_V
=
\text{conformance / evidence}.
$$

Experiencer：

$$
\Gamma_E
=
\text{use / interaction}.
$$

因此：

$$
S_B,
S_V,
S_E
$$

不同不代表互相衝突。

Canonical project state 應保留 multi-projection，而不是讓一個角色吞掉另外兩個。

---

# 52. 人類最適合保留的是治理

Human 應從：

```text
copy
paste
route
retry
clarify
```

移到：

```text
intent
risk
value
exception
authorization
veto
policy change
```

也就是：

$$
\boxed{
\text{Human Operational Load}\downarrow,
\qquad
\text{Human Governance Relevance}\uparrow.
}
$$

---

# 53. 反對意見一：全部 Transcript 給 AI 不就好？

不夠。

因為：

- token cost 高；
- privacy 不一定允許；
- transcript 不等於 canonical state；
- 舊資訊可能已 superseded；
- identity / provenance 仍然需要重新推理。

所以：

$$
\boxed{
\text{More Context}
\neq
\text{More Governed State}.
}
$$

---

# 54. 反對意見二：Shared Memory 不就好了？

Shared memory 主要回答：

> 過去有哪些資訊？

但不自動回答：

- 誰可以讀；
- 誰說的；
- 哪個版本；
- 哪個 authority；
- 是否驗證；
- 是否過期；
- 是否需要 human escalation。

因此：

$$
\boxed{
\text{Shared Memory}
\neq
\text{Shared Organization State}.
}
$$

---

# 55. 反對意見三：這樣太官僚

如果每個 tool call 都要求十幾個欄位，當然過度。

所以：

$$
\boxed{
\text{Externalization Depth}
\propto
\text{Coordination Risk}.
}
$$

低風險 ephemeral worker 可保持極薄 state。

persistent authority / memory / relationship / lineage 才需要完整 envelope。

---

# 56. 可測量命題一：Human Mediation Rate

定義：

$$
\rho_H^{med}
=
\frac{
N_{\mathrm{human\ mediation\ events}}
}{
N_{\mathrm{cross-agent\ transitions}}
}.
$$

成熟系統應使：

$$
\rho_H^{med}\downarrow.
$$

但不要求：

$$
\rho_H^{gov}\rightarrow0.
$$

---

# 57. 可測量命題二：Identity Clarification Rate

$$
\rho_I
=
\frac{
N_{\mathrm{identity\ clarification}}
}{
N_{\mathrm{cross-agent\ messages}}
}.
$$

加入 identity envelope 後預期：

$$
\rho_I^{after}
<
\rho_I^{before}.
$$

---

# 58. 可測量命題三：Handoff Repair Rate

$$
\rho_R
=
\frac{
N_{\mathrm{handoff\ repair}}
}{
N_{\mathrm{handoff}}
}.
$$

structured handoff 若有效，應有：

$$
\rho_R\downarrow.
$$

---

# 59. 可測量命題四：Provenance Loss Rate

$$
\rho_P
=
P(
\text{receiver cannot determine source / version / evidence}
).
$$

加入 provenance envelope 後：

$$
\rho_P\downarrow.
$$

---

# 60. 可測量命題五：Token-Amplification Cost

自由文字中介的成本可寫成：

$$
C_{\mathrm{token}}
=
C_{\mathrm{human\ summary}}
+
C_{\mathrm{agent\ reinterpretation}}
+
C_{\mathrm{clarification}}.
$$

structured state 應使：

$$
C_{\mathrm{token}}^{structured}
<
C_{\mathrm{token}}^{freeform}.
$$

---

# 61. Workflow-Level Operator Exit

對 workflow $\omega$，若：

$$
\rho_H^{med}
<
\theta_H
$$

且 misroute、provenance loss、recovery failure 都低於門檻，則可定義：

$$
\operatorname{OperationallyAutonomous}(\omega)=1
$$

在該判定域成立。

這不是 AGI 判定，只是 workflow-level autonomy。

---

# 62. 核心命題總表

## 命題一：Human Mediation Is Infrastructure

$$
\boxed{
\text{Human Mediation}
\neq
\text{Passive Message Copying}.
}
$$

## 命題二：Human-Kernel Decomposition

$$
\boxed{
H
=
I+R+C+P+S+X+F+K.
}
$$

## 命題三：Direct Messaging Is Insufficient

$$
\boxed{
\text{AI-to-AI Messaging}
\neq
\text{Externalized Coordination Infrastructure}.
}
$$

## 命題四：Operator Exit Requires Externalization

$$
\boxed{
H^{op}\downarrow
\Rightarrow
\operatorname{Externalize}(I,R,C,P,S,X,F,K)\uparrow.
}
$$

## 命題五：Canonical State Outside Agent Context

$$
\boxed{
\mathcal S_{\mathrm{org}}
\not\subset
C_{A_i}.
}
$$

## 命題六：Context Is Projection

$$
\boxed{
C_{A_i}
=
\Pi_i(
\mathcal S_{\mathrm{org}},
Task,
Role,
Authority,
Budget
).
}
$$

## 命題七：Task Continuity Is Not Agent Identity

$$
\boxed{
\text{Task Continuity}
\not\Rightarrow
\text{Agent Identity Continuity}.
}
$$

## 命題八：Operator Exit Is Not Governance Exit

$$
\boxed{
\text{Operator Exit}
=
\text{Mediation Externalization}
+
\text{Governance Retention}.
}
$$

---

# 63. 與 PAIS-03 的銜接

PAIS-01 回答：

> Cross-Agent state separation 為何產生 identity pressure？

PAIS-02 回答：

> 為什麼這個問題過去被 Human-Kernel 隱藏，以及人類退出後要外部化什麼？

下一篇：

# **PAIS-03｜身份壓力原理：自主性、身份與主體性為何可以彼此獨立**

將把：

$$
P_I^E
$$

擴展成：

$$
P_I
=
f(
X,H,E,R,A,L,J
),
$$

其中：

- $X$：cross-system heterogeneity；
- $H$：history divergence；
- $E$：embodiment；
- $R$：irreversibility；
- $A$：authority；
- $L$：liability；
- $J$：jurisdiction。

---

# 64. 結論

早期多 Agent 系統最容易產生的錯覺是：

> AI 已經能彼此協作，所以人類只是在中間傳話。

實際上，人類常同時維持：

- identity；
- routing；
- context；
- provenance；
- task state；
- conflict；
- finality；
- recovery。

因此真正架構是：

$$
A_i
\rightarrow
\mathcal H
\rightarrow
A_j,
$$

而不是只有：

$$
A_i
\rightarrow
A_j.
$$

只把 $\mathcal H$ 拿掉，不會自然得到成熟 multi-agent organization。

它只會失去原本被人類隱性提供的協調能力。

因此：

$$
\boxed{
\text{Human Exit}
\neq
\text{Human Function Disappearance}.
}
$$

真正的工程轉折是：

$$
\boxed{
\text{Human-Carried Implicit Coordination}
\rightarrow
\text{Machine-Readable Explicit Coordination State}.
}
$$

當 identity、routing、context、provenance、authority、finality 與 recovery 都可以由 Runtime 查詢、驗證與重建時，人類才真正有可能退出低價值 operational mediation。

而人類退出之後剩下的，不應是無治理的 Agent 群，而是：

$$
\boxed{
\text{Bounded Agent Autonomy}
+
\text{Externalized Coordination}
+
\text{Human Governance Bridge}.
}
$$

這是從「一群會聊天的 AI」走向「一個可以長期工作的 AI 組織」的第二個基礎轉折。

---

# 參考文獻

## A. 內部前置理論

1. Neo.K. **《從 AI 工具到 AI 組織：操作員退出問題》**, EML-ANDO-2026-01-v0.1, 2026-08-20.
2. Neo.K. **PAIS-01｜《當角色不再只是角色：從同 Host 扮演到跨 Agent 認識論分離》**, v0.1, 2026-08-25.
3. Neo.K. **《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》**, v0.1, 2026-08-24.
4. Neo.K. **《從 AI 戶籍到自主記憶編譯：身份、記憶、上下文與認知自主的統一框架》**, v0.1, 2026-08-24.
5. Neo.K. **《AI 主體性錨點論 v0.1》**, 2026-08-21.
6. Neo.K. **GLAG-02｜《從布告板到 AI Home：可定址智能體的空間身份、門牌與持續工作場所》**, 2026-08-25.
7. Credential Governance Runtime v0.3 / Bounded Dispute Protocol / CTCL Temporal Foundation, 2026-08-25.

## B. 外部研究與工程基準

8. A2A Protocol Working Group. **Agent2Agent Protocol Specification v1.0.** Linux Foundation, 2026.
9. A2A Protocol Working Group. **A2A Protocol Ships v1.0: Production-Ready Standard for Agent-to-Agent Communication.** 2026.
10. OpenAI. **An open-source spec for Codex orchestration: Symphony.** 2026-04-27.
11. Anthropic. **Patterns and problems in emerging multiagent systems.** 2026-08-13.
12. Wu, Qingyun, et al. **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.** COLM, 2024.
13. Li, Guohao, et al. **CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society.** arXiv:2303.17760, 2023.

---

# 版本註記

**v0.1 / 2026-08-25**

本文刻意不做：

- 不主張 Human 必須完全退出 multi-agent organization；
- 不把 operator exit 等同 governance exit；
- 不要求所有 Agent 都有 persistent identity；
- 不把 A2A、orchestrator 或 shared memory 誤認成完整 organization semantics；
- 不要求所有 context 集中到單一 database；
- 不把流暢 agent-to-agent dialogue 當作可靠協作的充分條件；
- 不重寫完整 AI Residence；
- 不預設任何 AI 已具有 phenomenal subjectivity。

本文只建立：

$$
\boxed{
\text{Human Mediation}
\rightarrow
\text{Hidden Coordination Functions}
\rightarrow
\text{Externalized Runtime Infrastructure}
}
$$

這一條第二階段理論鏈。
