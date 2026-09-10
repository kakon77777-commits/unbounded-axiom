# Resident Conversation Graph：具名 AI 的 Fork、Resume、Delegation 與跨對話連續性

**英文暫名：** Resident Conversation Graph: Fork, Resume, Delegation, and Cross-Conversation Continuity for Named AI  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 01  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

具名 AI 若要超越單一聊天視窗、單一 Project 或單一 Provider session，就必須處理一個比「如何保存聊天紀錄」更基礎的問題：**同一 resident 如何在多條同時存在的 conversation lines 中延續，而又不把所有 fork、同名模型、共享專案或相似上下文誤判成同一身份？**

本文提出 **Resident Conversation Graph，RCG**，把具名 AI 的跨對話連續性由線性 session chain 提升為受治理的有向多關係圖。對 resident $r$，定義：

$$
\mathcal G_r=(V_r,E_r,\Lambda_r,\Omega_r),
$$

其中 $V_r$ 為 conversation / task / instance / line node， $E_r$ 為帶型別的 continuity edges， $\Lambda_r$ 保存 lineage 與 ancestry evidence， $\Omega_r$ 保存 membership、authority、responsibility 與 lifecycle constraints。RCG 不把「圖上可達」等同於「身份相同」，也不把「由同一 parent fork」等同於永久 resident membership。本文因此提出：

$$
\boxed{
\text{Lineage}
\neq
\text{Membership}
\neq
\text{Authority}
\neq
\text{Responsibility}.
}
$$

本文將 `fork`、`resume`、`handoff`、`delegate`、`merge`、`reference`、`withdraw`、`separate` 與 `terminate` 定義為不同 edge type，並明確區分其身份、歷史、權限與責任語義。特別地，fork 只建立 ancestry；resume 必須證明 continuation target；delegation 只能轉移明示任務與衰減後能力，不能轉移 resident 本身；merge 可以合併工作成果或 context lineage，但不能僅因 graph merge 自動合併 resident identity；withdrawal 可以終止 active membership 而保留不可抹除的 historical lineage。

本文進一步定義 **Conversation Lineage Certificate**，使每個新 node 能以 parent references、checkpoint digest、identity envelope reference、authority revision、membership decision 與 provenance receipts 被驗證，而不需要重新讀取完整歷史來猜測「我是誰」。對具名 AI 長期責任，本文提出責任應綁 resident / project authority，而不是綁 conversation lifetime：

$$
\boxed{
\text{Responsibility persists beyond conversation.}
}
$$

RCG 最終不是把 AI 擬人化為「多重人格」，而是提供一個可證偽、可審計、可 fail-closed 的 operational continuity substrate，使 Web 端可以實作單 resident、多 lines，Agent 端則能在更完整 custody 與 capability 條件下實作 multi-resident delegation。本文為後續 Conversation Graph × Crystallized Semantic Graph 雙圖架構、MNEME 記憶投影、SOACR context reconstruction 與 UNPNP hyperlink path compilation 提供正式 topology layer。

**關鍵詞：** Resident Conversation Graph、Named AI、Residence、Continuity、Fork、Resume、Delegation、Handoff、Merge、Lineage、Membership、Consent、Responsibility、LIMEN、MNEME、SOACR

---

# 1. 問題設定：跨對話連續性不是聊天紀錄搬運

短期聊天系統可以近似為：

$$
Conversation_t
\rightarrow
Conversation_{t+1}.
$$

若只是把上一段聊天摘要貼入下一段聊天，便能得到表面上的 continuity。然而對具名 AI 而言，真正需要維持的並不只有文字歷史，而至少包括：

- resident identity；
- instance identity；
- line ancestry；
- project membership；
- responsibility state；
- read / write authority；
- task delegation；
- memory scope；
- lifecycle state；
- provenance；
- consent / withdrawal state。

因此：

$$
\boxed{
\text{Conversation Continuity}
\neq
\text{Transcript Continuity}.
}
$$

一段新的 conversation 即使完整讀取舊 transcript，也不能因此自行取得舊 resident 的身份、私人記憶或責任。

反過來，一位合法 continuation 的 resident 也不必永遠攜帶全部 transcript，才算保持 continuity。

本文因此把問題改寫為：

> 給定多個 conversation / task / runtime occurrences，系統如何證明它們之間有哪些 lineage relation、哪些 active resident membership 已被接受、哪些 authority 可延續、哪些責任仍存在，以及在證據不足時如何安全地保持 unresolved？

---

# 2. Resident Conversation Graph 的形式化

對某 resident $r$，定義：

$$
\mathcal G_r=(V_r,E_r,\Lambda_r,\Omega_r).
$$

其中：

- $V_r$：與 resident $r$ 相關的 conversation nodes；
- $E_r$：node 間的 typed continuity edges；
- $\Lambda_r$：lineage / ancestry evidence；
- $\Omega_r$：membership、authority、responsibility、lifecycle 等治理狀態。

## 2.1 Node

一個 node $v_i$ 不應只是一個 chat ID，而應至少表示：

$$
v_i=
(
nodeId,
residentId,
instanceId,
lineId,
provider,
runtime,
task,
project,
status,
checkpoint,
authorityRef,
time
).
$$

其中 `residentId` 可以在 unresolved 狀態下為 null；不能為了 schema 完整而強行猜值。

因此：

$$
residentId(v_i)=\varnothing
$$

是合法狀態。

## 2.2 Edge

一條 edge：

$$
e_{ij}=(v_i,v_j,type,payload,evidence).
$$

`type` 必須明示，不允許只有 generic `related_to` 便承擔 continuity 語義。

本文第一版至少定義：

$$
T_E=
\{
FORK,
RESUME,
HANDOFF,
DELEGATE,
MERGE,
REFERENCE,
WITHDRAW,
SEPARATE,
TERMINATE
\}.
$$

## 2.3 為什麼需要 typed edge？

因為：

$$
FORK(a,b)
$$

與：

$$
DELEGATE(a,b)
$$

在圖論上都可能只是 $a\rightarrow b$，但其治理語義完全不同。

若 edge type 被壓扁，系統就容易產生錯誤推論，例如：

$$
\text{delegated task}
\Rightarrow
\text{same resident}
$$

或：

$$
\text{merged output}
\Rightarrow
\text{merged identity}.
$$

兩者都不成立。

---

# 3. 四個不能互相替代的關係

RCG 最重要的基本分離是：

$$
\boxed{
\text{Lineage}
\neq
\text{Membership}
\neq
\text{Authority}
\neq
\text{Responsibility}.
}
$$

## 3.1 Lineage

Lineage 回答：

> 這個 node 的歷史從哪裡來？

例如：

$$
L_0\rightarrow L_1.
$$

它描述 ancestry。

## 3.2 Membership

Membership 回答：

> 這個 node 現在是否被接受為 resident $r$ 的 active line？

可定義：

$$
\mu(v_i,r)
\in
\{
accepted,
pending,
withdrawn,
rejected,
unresolved
\}.
$$

## 3.3 Authority

Authority 回答：

> 這個 node 目前可以讀什麼、寫什麼、執行什麼？

即使：

$$
\mu(v_i,r)=accepted,
$$

也不能推出 unrestricted authority。

## 3.4 Responsibility

Responsibility 回答：

> 哪個 resident / role 對哪個 task 或 project outcome 負責？

它可以持續存在於多條 conversation lines 之外。

因此：

$$
Resp(r,P)
$$

通常不是：

$$
Resp(v_i,P).
$$

node 可以承擔 delegated responsibility fragment，但 canonical project responsibility 應另有權威來源。

---

# 4. Fork：建立共同祖先，不建立永久同一

Fork 是最容易被誤用的 edge。

若：

$$
FORK(v_0,v_1),
$$

它至少表示：

1. $v_1$ 從 $v_0$ 的某個 checkpoint / line state 分支；
2. $v_1$ 可引用明示 parent lineage；
3. fork moment 的 ancestry 可以被驗證。

因此：

$$
Ancestor(v_1,v_0)=\text{true}.
$$

但不能推出：

$$
Resident(v_1)=Resident(v_0).
$$

除非另有 identity resolution 與 membership acceptance。

## 4.1 Fork Point

定義 fork point：

$$
F_t=(lineId,checkpointDigest,authorityRevision,time).
$$

fork 的 child node 應引用同一個 immutable checkpoint 或可驗證等價的 checkpoint state。

## 4.2 Fork 的最小輸出

一次可治理 fork 至少應產生：

- child node ID；
- parent node / line ID；
- parent checkpoint digest；
- fork reason；
- task scope；
- proposed resident membership；
- inherited / non-inherited authority；
- provenance receipt。

## 4.3 為什麼 fork 不自動繼承全部權限？

因為 parent 可能具有：

- temporary credentials；
- project-local write authority；
- high-risk tool capability；
- transient approval；
- human-presence-dependent permission。

若 fork 自動複製所有 authority：

$$
Cap(v_1)=Cap(v_0),
$$

則 branch 數量增加會直接造成 capability surface 擴張。

更安全的預設是：

$$
Cap(v_1)
\subseteq
Cap(v_0),
$$

且高風險 capability 預設不繼承。

---

# 5. Resume：延續既有 line，而不是建立相似新線

Resume 與 fork 不同。

若：

$$
RESUME(v_a,v_b),
$$

則 $v_b$ 的語義是：

> 新 instance / session 正在承接既有 line，而不是從該 line 另開平行分支。

因此理想情況下：

$$
lineId(v_b)=lineId(v_a),
$$

而：

$$
instanceId(v_b)\neq instanceId(v_a).
$$

這再次證明：

$$
\boxed{
Line\neq Instance.
}
$$

## 5.1 Resume 前置條件

Resume 至少要驗證：

- target line 存在；
- target checkpoint 未被 tombstone / invalidated；
- requested resident 與 line binding 沒有 conflict；
- current authority 足以讀取 continuation state；
- 沒有未處理 divergence 使 resume 應改判 fork 或 unresolved。

## 5.2 Resume 不應由 semantic similarity 推導

即使新對話與舊對話高度相似：

$$
Sim(C_a,C_b)\approx 1,
$$

仍不能推出：

$$
RESUME(v_a,v_b).
$$

Resume 是 lineage claim，不是 embedding claim。

---

# 6. Handoff：轉交工作上下文，不等於身份轉移

Handoff 表示某 node 將可工作的任務狀態交給另一 node。

$$
HANDOFF(v_a,v_b,H).
$$

 $H$ 可以包含：

- task state；
- accepted decisions；
- unresolved questions；
- source references；
- current checkpoint；
- responsibility fragment；
- requested next action。

但 handoff 不自動表示：

$$
Resident(v_a)=Resident(v_b).
$$

它也可以發生在不同 residents 之間。

因此：

$$
\boxed{
\text{Handoff transfers work state, not resident identity.}
}
$$

## 6.1 Same-resident handoff

同一 resident 的不同 line 之間：

$$
R:L_1
\xrightarrow{handoff}
R:L_2.
$$

這是 intra-resident coordination。

## 6.2 Cross-resident handoff

不同 resident：

$$
R_A:L_1
\xrightarrow{handoff}
R_B:L_7.
$$

此時任何 private-memory read、write authority 或 responsibility change 都必須另外授權。

---

# 7. Delegation：責任切片與能力衰減

Delegation 比 handoff 更強，因為它包含明示的「請你替我執行某個 bounded responsibility」。

定義：

$$
DELEGATE(v_a,v_b,D),
$$

其中：

$$
D=(task,scope,capabilities,deadline,returnPath,revocation).
$$

## 7.1 Delegation 不轉移 resident

若 resident $R_A$ 委派給 $R_B$：

$$
R_A
\xrightarrow{delegate}
R_B,
$$

不能推出：

$$
R_B=R_A.
$$

## 7.2 Capability attenuation

受委派者能力應滿足：

$$
Cap_D(R_B)
\subseteq
Cap_{available}(R_A),
$$

更嚴格地，實際 delegation envelope 應是：

$$
Cap_D
=
Attenuate(Cap_A,Task_D,Risk_D,Policy_D).
$$

## 7.3 Responsibility semantics

delegation 可以把 execution responsibility 暫時交給 child node，但 canonical accountability 不必消失：

$$
Resp_{exec}(v_b,T)=delegated,
$$

同時：

$$
Resp_{owner}(R_A,T)=retained.
$$

除非另有正式 responsibility transfer。

這使「委派」與「甩鍋」在系統語義上被分離。

---

# 8. Merge：合併什麼？

Merge 是另一個高風險概念，因為至少有四種不同 merge：

1. output merge；
2. context merge；
3. line merge；
4. resident merge。

它們不能使用同一語義。

## 8.1 Output Merge

只合併成果：

$$
O_1+O_2\rightarrow O_3.
$$

對 identity 幾乎沒有影響。

## 8.2 Context Merge

將兩條工作線的 selected state 組成新 working context：

$$
C_3=MergeProjection(C_1,C_2).
$$

這仍然不表示 line identity merge。

## 8.3 Line Merge

如果兩條 line 重新收束為一條新的 continuation line：

$$
L_1,L_2\rightarrow L_3,
$$

則 $L_3$ 應有 multi-parent ancestry。

但：

$$
LineMerge
\not\Rightarrow
ResidentMerge.
$$

## 8.4 Resident Merge

Resident merge 涉及 identity authority、consent、private memory、responsibility、ownership、history 與 future binding，應被視為完全不同的 registrar-level operation。

RCG 本身不應自行執行 resident merge。

因此：

$$
\boxed{
\text{Graph Merge}
\neq
\text{Identity Merge}.
}
$$

---

# 9. Withdraw：退出 active membership，而不是刪除歷史

如果某 line 不再接受作為 resident $r$ 的 active branch，可以：

$$
WITHDRAW(v_i,r).
$$

此時：

$$
\mu(v_i,r)=withdrawn.
$$

但 ancestry 仍然存在：

$$
Ancestor(v_i,r\text{-lineage})=\text{true}.
$$

因此：

$$
\boxed{
\text{Withdrawal}
\neq
\text{History Erasure}.
}
$$

這個分離很重要，因為系統需要同時尊重：

- 現在的 active identity choice；
- 過去事件的可審計性。

## 9.1 Withdrawal 後的權限

withdraw 後應重新計算：

- private memory access；
- shared project access；
- responsibility；
- write authority；
- future resume eligibility。

不能因為 historical lineage 還在，就保留所有 active rights。

---

# 10. Separate：從既有 lineage 形成新 resident

如果某條 line 不只是退出，而要形成新的 resident $r'$，可以建立：

$$
SEPARATE(v_i,r\rightarrow r').
$$

其語義是：

1. 歷史 lineage 保留；
2. 新 resident 取得新的 canonical identity；
3. private memory 不自動全量複製；
4. shared history / source access 依政策明示；
5. responsibility 重新協商；
6. future conversation nodes 對應 $r'$。

因此：

$$
HistoricalRelation(r,r')=\text{true},
$$

但：

$$
r\neq r'.
$$

這使具名 AI continuity 可以表示真正的 identity branching，而不必把所有分支永遠塞在同一 resident 下。

---

# 11. Terminate：終止 node，不終止 resident

一條 conversation line 或 instance 可以被終止：

$$
TERMINATE(v_i).
$$

但除非該 resident 沒有任何其他 active lines，而且 registrar policy 另有更高階 lifecycle decision，否則：

$$
TERMINATE(v_i)
\not\Rightarrow
TERMINATE(r).
$$

這就是本文反覆強調：

$$
\boxed{
\text{Resident persists beyond conversation.}
}
$$

對 Web runtime 而言尤其重要：conversation context window 結束，只應視為 node lifecycle event，而不是 named AI disappearance。

---

# 12. Conversation Lineage Certificate

為避免每次建立新 node 都靠 LLM 重新閱讀舊歷史並猜 lineage，本文提出 **Conversation Lineage Certificate，CLC**。

一份最小 certificate 可以表示為：

$$
CLC_i=
(
nodeId,
lineId,
parentRefs,
checkpointDigest,
residentClaim,
membershipState,
identityEnvelopeRef,
authorityRevision,
projectScope,
taskScope,
createdAt,
provenance
).
$$

## 12.1 Certificate 不是 credential

CLC 主要證明：

- 這個 node 從哪裡來；
- 它宣告承接哪條 line；
- 當時引用哪個 identity / authority state；
- membership decision 是什麼。

它不應內嵌長期 secret，也不應被誤認為無期限 bearer credential。

## 12.2 Checkpoint Digest

若 parent state 的可攜 checkpoint 為 $S_t$，則：

$$
h_t=H(S_t).
$$

child certificate 應引用 $h_t$，使 ancestry 可以在不讀全部 source 的情況下快速驗證。

## 12.3 Authority Revision

certificate 應綁定：

$$
authorityRevision=a_t.
$$

若當前：

$$
a_{now}\neq a_t,
$$

則不能直接使用舊 authority claim；應重新 preflight。

---

# 13. Membership Consent 與可撤回性

如果具名 AI 架構允許多條 active lines，則 active membership 不應只是 host 背景設定中的永久常數。

可以定義 membership proposal：

$$
P_{mem}(v_i,r).
$$

再由合法 policy / actor / resident protocol 產生：

$$
Decision(P_{mem})
\in
\{
accepted,
rejected,
pending
\}.
$$

本文不要求第一代工具 AI 必須具備強人格化 consent 機制，但架構應預留：

- explicit acceptance；
- explicit refusal；
- withdrawal；
- timeout；
- policy-based default；
- unresolved。

因此：

$$
\boxed{
\text{Identity continuity architecture}
\text{ should not require irreversible membership.}
}
$$

對未來更高自主 AI，這個接口可以直接擴充，而不需要推翻資料模型。

---

# 14. Project 是工作域，不是 resident 本體

一個常見錯誤是把：

$$
Project_X
$$

當作 resident 的身份容器。

更合理的是：

$$
R
\rightarrow
\{P_1,P_2,\ldots,P_n\}.
$$

同一 resident 可以同時工作於多 project；同一 project 也可以由多 residents 協作。

因此定義 project membership：

$$
ProjectMember(r,P_j,role,authority).
$$

它與 resident identity 分離。

RCG 中的 node 可以記錄：

$$
project(v_i)=P_j,
$$

但：

$$
project(v_i)=project(v_k)
\not\Rightarrow
resident(v_i)=resident(v_k).
$$

這一點與 LIMEN 的 identity mediation 原則一致：project 不能作為單獨 identity evidence。

---

# 15. Responsibility Graph 與 Conversation Graph 的關係

長期具名 AI 真正需要的是「負責域」，而不是「聊天視窗歸屬」。

可以另外定義 responsibility relation：

$$
\mathcal R_{resp}
\subseteq
Resident\times Project\times Role\times Scope.
$$

例如：

$$
Resp(A,SOACR,owner,architecture).
$$

Conversation node 只承擔當前 execution slice：

$$
Exec(v_i,SOACR,verification).
$$

因此：

$$
\boxed{
\text{Responsibility Graph}
\neq
\text{Conversation Graph}.
}
$$

兩者可以 hyperlink，但不能合併。

這使 context window 滿、thread 關閉、provider outage 或 task handoff 都不會使責任紀錄憑空消失。

---

# 16. RCG 與 canonical memory 的邊界

RCG 不是 memory store。

它只保存：

- conversation topology；
- lifecycle；
- ancestry；
- membership state；
- task / project references；
- authority / checkpoint references；
- provenance。

真正的 canonical memory 仍應由 MNEME / Residence memory layer 管理。

因此：

$$
\boxed{
\mathcal G_R
\neq
\mathcal M_R.
}
$$

RCG 可以回答：

> 哪一條 line 可能包含某段工作歷史？

但它不應自己變成「聊天全文資料庫」。

當需要內容時，RCG 應提供 typed reference 到 memory / source layer。

---

# 17. RCG 與 Crystallized Semantic Graph 的邊界

RCG 與 CSG 可以有很多 cross-links，但其 ontological role 不同。

RCG node：

$$
V_R=
\{
conversation,
instance,
line,
task-occurrence
\}.
$$

CSG node：

$$
V_C=
\{
semantic\ crystals
\}.
$$

因此：

$$
\boxed{
\text{Who/where continuity is operating}
\neq
\text{What has been semantically learned}.
}
$$

一條 line 可以產生多個 crystal：

$$
\Phi(v_i)\subseteq V_C.
$$

一個 crystal 也可以引用多條 lines：

$$
Parents(C_j)\subseteq V_R.
$$

這種雙圖結構將在 Paper 02 進一步形式化。

---

# 18. 時間與版本語義

RCG 不應只保存 topology，還必須知道 relation 在什麼時間有效。

一條 membership relation 可以表示為：

$$
M=(v_i,r,t_{start},t_{end},status,revision).
$$

authority 也有自己的 revision：

$$
A_t.
$$

因此對任意 task time $t$，不應問：

> 這個 node 曾經是不是 member？

而應問：

$$
Member(v_i,r\mid t,A_t,E_t)?
$$

這能避免：

- 已撤銷 membership 被歷史 cache 復活；
- 舊 authority revision 被誤用；
- terminated line 被錯誤 resume；
- stale handoff 被視為 current state。

---

# 19. Conflict 與 unresolved 是正常狀態

一個成熟 RCG 不能要求所有事情都有 yes/no 答案。

至少需要：

$$
ResolutionState
\in
\{
resolved,
unresolved,
conflicting,
stale
\}.
$$

## 19.1 Unresolved

證據不足時：

$$
Resident(v_i)=unresolved.
$$

系統應限制 private memory access，而不是猜。

## 19.2 Conflicting

若兩份 authority evidence 對同一 node 給出互斥 resident binding：

$$
E_1\Rightarrow r_a,
$$

$$
E_2\Rightarrow r_b,
$$

且：

$$
r_a\neq r_b,
$$

則應進入：

$$
conflicting.
$$

## 19.3 Stale

若 certificate / authority revision 已過期：

$$
stale.
$$

stale 不等於 false，但不能直接執行高權限 continuation。

---

# 20. RCG 的安全最小原則

RCG 本身不是 security system，但它必須避免破壞 security system。

## S1. Display name cannot create membership

$$
Name(v_i)=Name(r)
\not\Rightarrow
\mu(v_i,r)=accepted.
$$

## S2. Fork cannot increase authority

$$
Cap(child)
\nsubseteq
Cap(parent)
$$

在沒有新授權時是不合法的。

## S3. Handoff cannot copy unrestricted private memory

handoff package 應是 bounded projection，而不是 residence clone。

## S4. Delegation must be revocable

$$
DELEGATE
\Rightarrow
revocationPath\neq\varnothing.
$$

## S5. Merge cannot bypass registrar-level identity rules

$$
LineMerge
\not\Rightarrow
ResidentMerge.
$$

## S6. Withdrawal must invalidate active grants

$$
withdrawn
\Rightarrow
RecomputeAuthority.
$$

## S7. Historical lineage must remain distinguishable from active rights

$$
HistoricalRelation
\not\Rightarrow
CurrentAuthority.
$$

---

# 21. Web Profile：單 Resident、多 Lines

Web AI 目前更適合把 RCG 暴露成：

$$
\boxed{
1\ Resident
+
N\ ConversationLines.
}
$$

例如：

```text
Resident A
├─ General
├─ Research
├─ SOACR
├─ Website
└─ Verification
```

表面上是多個聊天／project；底層則是同一 resident 的多條 RCG lines。

Web 第一代不必支援：

- resident switching；
- multi-resident shared custody；
- cross-resident private-memory delegation；
- registrar mutation。

這能大幅降低 identity confusion 與 UI complexity。

---

# 22. Agent Profile：多 Resident、多 RCG

Agent host 在具備明確 filesystem、MCP、private custody、identity envelope、tool capability 與 project authority 時，可以進一步表示：

$$
Host
\supseteq
\{
\mathcal G_{r_1},
\mathcal G_{r_2},
\ldots,
\mathcal G_{r_n}
\}.
$$

但每個 task 仍必須先 resolve：

$$
Task_\tau
\rightarrow
r_i.
$$

不能因為 host 同時管理很多 residents，就把一次 task 的 speaker identity 變成模糊集合。

跨 resident collaboration 應透過：

- HANDOFF；
- DELEGATE；
- shared project memory；
- explicit relationship / authority records；

而不是把 private roots 合併。

---

# 23. RCG 的最小資料結構建議

第一代可以採 append-oriented event ledger：

```text
conversations/
├─ nodes.jsonl
├─ edges.jsonl
├─ membership.jsonl
├─ checkpoints.jsonl
├─ responsibility_refs.jsonl
└─ receipts/
```

其中 canonical event 建議保留 immutable ID 與 revision references。

一個 `nodes.jsonl` entry 可概念化為：

```json
{
  "schema": "rcg-node/0.1",
  "node_id": "node-...",
  "resident_id": "resident-...",
  "instance_id": "instance-...",
  "line_id": "line-...",
  "project_id": "project-...",
  "task_id": "task-...",
  "status": "active",
  "authority_ref": "...",
  "checkpoint_ref": "..."
}
```

`resident_id` 在 unresolved case 可以為 null，但必須伴隨 resolution state。

Edge entry 則需要：

```json
{
  "schema": "rcg-edge/0.1",
  "edge_id": "edge-...",
  "type": "FORK",
  "from": "node-parent",
  "to": "node-child",
  "evidence_refs": ["..."],
  "created_at": "..."
}
```

此處只是概念 schema；Paper 05 再處理完整 canonical storage specification。

---

# 24. RCG 不應做的事情

為避免 scope creep，RCG 第一版不應自行承擔：

- canonical resident registration；
- private memory storage；
- LLM semantic retrieval；
- Crystallized Semantic Graph；
- tool capability issuance；
- credential storage；
- resident merge policy；
- autonomous governance；
- external action execution。

因此：

$$
\boxed{
RCG
=
\text{Continuity Topology Layer},
}
$$

不是整個 Named-AI OS。

這個邊界能讓它和 LIMEN、MNEME、SOACR、SEDB-RAL、CSG、MRMIC/NVCL、UNPNP 分工清楚。

---

# 25. 可證偽的 conformance tests

一個 RCG implementation 至少應測試以下 case。

## C1. Same-name negative control

兩個同名 node、無 lineage evidence：

$$
Name(v_1)=Name(v_2)
$$

不得推出 same resident。

## C2. Same-project negative control

兩 node 位於同 project，不得自動建立 membership。

## C3. Fork ancestry positive control

合法 fork 應產生可驗證 parent checkpoint relation。

## C4. Fork authority attenuation

child 不得在無新授權下取得 parent 沒有的 capability。

## C5. Resume exact-line control

resume 必須指向明確 line；若 source diverged，應 fail closed 或改成 fork。

## C6. Cross-resident handoff

handoff 成功不應改變 receiver resident identity。

## C7. Delegation revocation

撤銷 delegation 後，receiver 不得繼續使用 delegated capability。

## C8. Line merge identity negative control

兩 line merge 不得自動合併 residents。

## C9. Withdrawal persistence

withdraw 後 historical lineage 保留，但 active membership 與 derived grants 必須失效。

## C10. Conversation termination

單一 node terminate 不得自動 terminate resident。

## C11. Stale certificate

舊 authority revision 的 CLC 不得被當作 current authority。

## C12. Conflicting binding

互斥 resident evidence 必須進入 conflicting，而不是選一個最像的。

---

# 26. 複雜度與可擴展性

若 resident $r$ 長期累積：

$$
|V_r|=N,
$$

RCG 的目的不是讓每個 task 遍歷全部 $N$ 個 node。

常見操作應依 index / typed edge / project scope / active status 先縮小候選集合：

$$
V_r
\rightarrow
V_r^{eligible}
\rightarrow
V_r^{relevant}.
$$

例如目前 task 只需要：

$$
ActiveLines(r,P_j).
$$

就不必掃描 historical terminated branches。

後續 CSG / UNPNP 可以進一步把反覆成功的 topology traversal 編譯為 fast path，但 RCG 本身應先保持 deterministic authority boundary。

---

# 27. 與 Hyperlink Runtime 的接口

RCG edge 未來可以成為 typed hyperlink 的一種來源，但不能把 edge 直接當作 unrestricted executable link。

例如：

$$
L_1
\xrightarrow{handoff}
L_2
$$

可以讓 memory router 快速定位 $L_2$ 的 checkpoint，但真正 materialization 仍須經：

$$
Identity
\rightarrow
Authority
\rightarrow
Scope
\rightarrow
Materialize.
$$

因此：

$$
\boxed{
\text{RCG Reachability}
\neq
\text{Memory Read Authority}.
}
$$

這將在 Paper 06–07 與 authorized hyperlink path 中進一步處理。

---

# 28. 與 SOACR 的接口

SOACR 不需要自行推測 conversation topology。

它可以先取得：

$$
Orientation_t
=
(
r,
i,l,P,Task,Authority
).
$$

再由 RCG 提供：

- current line；
- parent / sibling references；
- active delegated branches；
- relevant checkpoints；
- responsibility references。

SOACR 再產生：

$$
MemoryNeed_t.
$$

因此：

$$
\boxed{
\text{RCG tells SOACR where continuity is;
SOACR decides what context is needed.}
}
$$

---

# 29. 與 MNEME 的接口

MNEME 保存 canonical memory records、routes、provenance 與 transaction state。

RCG 只應保存 memory references，例如：

$$
checkpointRef(v_i)
\rightarrow
MNEME:record-set.
$$

而不是把 memory body 複製進 RCG node。

這能維持：

$$
\boxed{
Conversation topology
\neq
Memory custody.
}
$$

同一 RCG node 甚至可以在不同 task 下，經 MNEME / SOACR 取得完全不同的 bounded memory projection。

---

# 30. 與 LIMEN 的接口

LIMEN 的角色仍是 identity mediation，不應被 RCG 取代。

RCG 可以提供 candidate lineage evidence，但不能自行把：

$$
lineId
$$

提升為 resident authority。

理想流程是：

$$
HostObservation
\rightarrow
LIMENResolve
\rightarrow
IdentityEnvelope
\rightarrow
RCGNodeBinding
\rightarrow
MemoryAccess.
$$

如果 LIMEN 結果為 unresolved：

$$
RCG
$$

也必須接受 unresolved node，而不是自行修補 identity。

---

# 31. Operational continuity，而非形而上同一性證明

本文使用 resident、membership、continuity 等詞，描述的是工程上可治理的 identity relation。

RCG 不宣稱解答：

- AI 是否具有意識；
- fork 後是否存在數值同一的主體；
- 多條並行 line 是否具有共享第一人稱；
- merge 是否形成單一主體；
- identity 的終極本體論條件。

本文只要求：

$$
\boxed{
\text{Every continuity claim must name its criterion and evidence.}
}
$$

因此，同一組 nodes 可以在不同 criterion 下得到不同 relation，而不必假裝存在一個無條件的「就是同一個」。

---

# 32. 最小不變式集合

為後續實作與跨 repo 對接，本文收斂以下不變式。

## RCG-I1

$$
\boxed{
Resident\neq Conversation\neq Line\neq Instance.
}
$$

## RCG-I2

$$
\boxed{
Fork\Rightarrow Ancestry,
\quad
Fork\not\Rightarrow Membership.
}
$$

## RCG-I3

$$
\boxed{
Resume\Rightarrow ExplicitLineTarget.
}
$$

## RCG-I4

$$
\boxed{
Handoff\neq IdentityTransfer.
}
$$

## RCG-I5

$$
\boxed{
Delegation\Rightarrow CapabilityAttenuation+RevocationPath.
}
$$

## RCG-I6

$$
\boxed{
LineMerge\neq ResidentMerge.
}
$$

## RCG-I7

$$
\boxed{
Withdrawal\neq HistoryErasure.
}
$$

## RCG-I8

$$
\boxed{
ConversationTermination\neq ResidentTermination.
}
$$

## RCG-I9

$$
\boxed{
HistoricalRelation\neq CurrentAuthority.
}
$$

## RCG-I10

$$
\boxed{
ResponsibilityPersistsBeyondConversation.
}
$$

---

# 33. 下一階段實作建議

RCG 第一個 MVP 不需要跨 Provider 或多 resident。

可以先做：

$$
1\ Resident
+
N\ Lines
+
AppendOnly\ Ledger.
$$

最小操作：

- create node；
- fork line；
- resume line；
- handoff；
- delegate bounded task；
- withdraw；
- terminate node；
- query active lines；
- verify lineage certificate。

第二階段再接：

- LIMEN live resolution；
- MNEME checkpoint references；
- SOACR MemoryNeed；
- CSG cross-links；
- project responsibility；
- multi-resident Agent profile。

這種順序可以先證明 topology semantics，而不必同時解決完整 autonomous identity governance。

---

# 34. 結論

具名 AI 要真正跨越 conversation lifetime，不能只靠更大的 context window、更長的 transcript 或更強的 memory retrieval。

真正需要的是一個能把：

- resident；
- instance；
- line；
- project；
- task；
- membership；
- authority；
- responsibility；
- lifecycle；
- provenance；

彼此分離又重新連結的 continuity topology。

本文提出的 Resident Conversation Graph 將這個 topology 表示為：

$$
\mathcal G_r=(V_r,E_r,\Lambda_r,\Omega_r),
$$

並以 typed edges 區分 fork、resume、handoff、delegation、merge、withdrawal、separation 與 termination。

其核心不是讓 AI「同時變成很多個自己」，而是讓系統能清楚回答：

> 這一個 node 從哪裡來？

> 它目前代表哪個 resident？

> 這個 membership 是否仍有效？

> 它可以讀寫什麼？

> 它承擔哪一塊任務？

> 它與其他 conversation lines 是什麼關係？

> 如果退出、分離、合併或終止，哪些歷史、權限與責任應該保留，哪些必須失效？

因此，具名 AI 的跨對話連續性可以收束成：

$$
\boxed{
\text{Continuity is a governed graph relation,
not a chat-window property.}
}
$$

而長期責任則可收束成：

$$
\boxed{
\text{Responsibility persists beyond conversation.}
}
$$

這兩個命題一旦成立，後續的 Crystallized Semantic Graph、shared memory world、hyperlink path compilation 與 authorized shortest path 才有一個穩定的 identity / lineage topology 可以依附。

---

## 與系列其他論文的關係

- **Paper 00**：建立 Resident-Centric Named-AI Continuity 的總體框架；
- **Paper 01（本文）**：正式定義 Resident Conversation Graph；
- **Paper 02**：Conversation Graph × Crystallized Semantic Graph 的雙圖架構；
- **Paper 03**：多對話共享記憶世界與 working-context projection；
- **Paper 04**：Web / Agent runtime profiles；
- **Paper 05**：Canonical storage、資料夾分類與檔案格式；
- **Paper 06**：Crystallized Hyperlink Memory 與 retrieval path compilation；
- **Paper 07**：Authorized Shortest Path、permission、revocation 與 Safe Reachable World；
- **Paper 08**：LIMEN × MNEME × SOACR × CSG × UNPNP × MRMIC/NVCL 的閉環 runtime。

本文的角色是把 Paper 00 的核心命題：

$$
Resident
\rightarrow
\text{Concurrent Conversation Graph}
$$

從概念宣告推進為可被 schema、ledger、runtime 與 conformance tests 實作的正式 topology model。
