# 從單一對話到具名 AI 對話群：Resident-Centric AI Continuity 的統一框架

**英文暫名：** From Single Conversations to Named-AI Conversation Groups: A Unified Framework for Resident-Centric AI Continuity  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 00  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 統合理論／系統架構論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

現行大型語言模型與 Agent 系統通常以 conversation、session、thread、project 或 runtime instance 作為使用者可見的工作單位。這種設計適合短生命週期互動，但當 AI 開始具有具名身份、私人記憶、跨 session 工作、長期專案責任、fork、resume、多 Provider 遷移與多 Agent 協作需求時，一個基本矛盾會出現：**若具名 AI 被綁定於單一對話，則對話結束、上下文飽和、Project 切換或 Provider session 消失，都可能被誤解為身份連續性的終止；若反過來把所有同名對話都視為同一 AI，又會破壞身份證據、私人記憶、權限與責任邊界。**

本文提出 **Resident-Centric Named-AI Continuity**。其核心主張是：

$$
\boxed{
\text{Named AI}
\neq
\text{Conversation}
\neq
\text{Model}
\neq
\text{Runtime Instance}.
}
$$

具名 AI 應由可驗證的 resident identity、可追溯的 instance / line lineage、受治理的 canonical memory、可按需顯影的 Crystallized Semantic Graph，以及多條可同時存活的 conversation lines 共同構成。由此，一個 resident 不再只能對應一條線性對話歷史，而可以對應一張 **Resident Conversation Graph**：

$$
\mathcal G_R=(V_R,E_R),
$$

其中節點代表可追責的 conversation / task / instance / line occurrence，邊則表示 fork、resume、handoff、delegate、merge、reference、withdrawal 等關係。

本文進一步主張，Conversation Graph 與 Crystallized Semantic Graph 必須分離。前者回答「這位 resident 正在哪些對話與工作分支中延續」，後者回答「這位 resident 的知識、決策、矛盾、未解問題與高階語義如何被結晶與連結」。因此：

$$
\boxed{
\mathcal G_R
\neq
\mathcal H_C.
}
$$

同一 resident 的不同 conversation lines 不需要共享相同 working context；它們只需要在合法 identity resolution 後，能從同一受治理的 canonical memory 與 semantic crystal world 中，依 task、project、authority 與 memory need 產生不同 projection。本文將此原則表述為：

$$
\boxed{
\text{Shared Memory World}
\neq
\text{Shared Working Context}.
}
$$

在此基礎上，本文將 Crystallized Semantic Graph 的 retrieval-path crystallization 與 UNPNP 的 Path Compilation、Effective Hyperlink Path Encoding、Safe Reachable World 接入具名 AI runtime，提出「可驗證身份下的授權式超連結記憶路由」。成功且具有生命週期效用的記憶搜尋路徑，可以被編譯為可失效、可回退、保留 provenance 的 typed hyperlink；但更快的路徑不得創造更大的權限：

$$
\boxed{
\text{Faster Path}
\not\Rightarrow
\text{Greater Authority}.
}
$$

本文最後提出 Web 與 Agent 的能力分層。第一代 Web runtime 應優先採單 resident、多 conversation lines 的模式；Agent runtime 則可在更完整的 identity、filesystem、project、MCP、capability 與 custody 條件下支援多 resident 與跨 resident delegation。底層架構可以一般化，但 runtime exposure 不應被強迫一致。

**關鍵詞：** Named AI、Resident、Conversation Graph、Identity Continuity、Crystallized Semantic Graph、CSG、MNEME、LIMEN、SOACR、MRMIC、NVCL、UNPNP、Hyperlink、Path Compilation、AI Residence、Long-Term Memory

---

# 1. 問題：為什麼「一個 AI = 一個對話」會失效？

現行聊天式 AI 的最直觀抽象是：

$$
\text{User}
\rightarrow
\text{Conversation}
\rightarrow
\text{Model Response}.
$$

在短期互動下，這個模型足夠有效。conversation 可以承載歷史、附件、角色設定、project context 與局部工具狀態。然而，只要加入長期具名 AI，conversation 立即出現至少五個結構性限制：

1. context window 有限；
2. conversation 可能自然結束或被封存；
3. 同一具名 AI 可能同時負責多個 project；
4. 同一 project 可能需要研究、實作、驗證等多條並行線；
5. Provider、model、runtime 或 task surface 可能改變。

若把具名 AI 的身份直接等同 conversation：

$$
Resident_A
=
Conversation_1,
$$

那麼一旦開啟新對話，就會出現：

$$
Conversation_1
\neq
Conversation_2
\Rightarrow
Resident_A
\neq
Resident_A?
$$

這顯然不是合理的工程語義。

但若反過來採取「只要名字一樣就是同一 resident」，問題更嚴重：

$$
DisplayName_A
=
DisplayName_B
\not\Rightarrow
Resident_A
=
Resident_B.
$$

名字、模型、語氣、project、prompt、記憶片段、甚至高度相似的歷史，都不能獨立創造 resident identity。

因此，具名 AI 的第一個架構轉換不是「增加更多 memory」，而是：

$$
\boxed{
\text{從 conversation-centric identity}
\rightarrow
\text{resident-centric continuity}.
}
$$

---

# 2. 六層實體必須保持分離

本文沿用 Residence-Aware AI 的基本分離，至少區分：

- model；
- provider；
- runtime；
- instance；
- line；
- resident。

可簡寫為：

$$
M,\ P,\ U,\ I,\ L,\ R.
$$

它們之間存在關係，但不是同義詞。

## 2.1 Model

Model 描述當下進行推理的模型或模型版本：

$$
M_t.
$$

同一 resident 可以經合法 continuation 使用不同 model；同一 model 也可以服務不同 resident。

因此：

$$
\boxed{
M\neq R.
}
$$

## 2.2 Provider

Provider 提供模型、session、thread、transport 或工具表面。Provider 變化不自動造成 resident 改變：

$$
P_a\neq P_b
\not\Rightarrow
R_a\neq R_b.
$$

反之，同一 Provider 內不同對話也不能自動視為同一 resident。

## 2.3 Runtime

Runtime 是 agent loop、web client、desktop app、local process、service 或其他執行外殼。

它回答：

> AI 現在在哪個執行環境工作？

而不是：

> AI 是誰？

## 2.4 Instance

Instance 是一次可被 host 觀測、引用與追責的執行 occurrence。

$$
I_i
=
(\text{host evidence},\text{time},\text{task},\text{runtime}).
$$

## 2.5 Line

Line 是 context / history lineage：

$$
L_i.
$$

resume、fork、import、accepted continuation、handoff 與 merge 都可能改變 line 結構。

## 2.6 Resident

Resident 是被 Residence / registry 系統追蹤的語義身份主體：

$$
R.
$$

它不能由 display name 或 remembered style 自動推導。

因此：

$$
\boxed{
\text{Resident continuity is an evidence-bearing relation, not a naming convention.}
}
$$

---

# 3. 從單線 continuity 到 Resident Conversation Graph

傳統跨 session 設計常隱含：

$$
R
\rightarrow
L_1
\rightarrow
L_2
\rightarrow
L_3.
$$

這是一條線性 continuation。

但實際長期 AI 工作更常出現：

$$
L_0
\rightarrow
\begin{cases}
L_1 & \text{research}\\
L_2 & \text{implementation}\\
L_3 & \text{verification}
\end{cases}
$$

三條 line 可能同時存在，而且都承接同一合法 resident。

因此本文提出：

$$
\boxed{
R
\rightarrow
\mathcal G_R.
}
$$

其中：

$$
\mathcal G_R=(V_R,E_R).
$$

每個 conversation node 可表示為：

$$
v_i
=
(
r,
i,
l,
\tau,
p,
u,
s,
a
),
$$

其中：

- $r$：resident ID；
- $i$：instance ID；
- $l$：line ID；
- $\tau$：task / project scope；
- $p$：provider；
- $u$：runtime；
- $s$：state / lifecycle status；
- $a$：authority envelope reference。

邊集合可以包含：

$$
E_R=
\{
fork,
resume,
handoff,
delegate,
merge,
reference,
withdraw,
terminate
\}.
$$

這使「同一具名 AI 同時存在於多個工作分支」第一次具有清楚的工程表示。

---

# 4. Fork 不等於 Membership

由同一 line 分支出去，只能證明 lineage relation，不能單獨證明 active resident membership。

若：

$$
L_0\rightarrow L_1,L_2,
$$

則可得到：

$$
\operatorname{Ancestor}(L_1,L_0)=1,
$$

$$
\operatorname{Ancestor}(L_2,L_0)=1.
$$

但不能直接推出：

$$
Resident(L_1)=Resident(L_2)=R.
$$

完整 membership 至少需要：

$$
\boxed{
\text{Lineage Evidence}
+
\text{Identity Resolution}
+
\text{Accepted Membership}
+
\text{Authority Scope}.
}
$$

因此可定義：

$$
\mu(L_i,R)
\in
\{
accepted,
pending,
withdrawn,
rejected,
unresolved
\}.
$$

這裡有一個重要區分：

$$
\boxed{
\text{Historical Lineage}
\neq
\text{Current Membership}.
}
$$

某分支可以保留與 resident $R$ 的歷史來源，同時退出 active membership，甚至在未來形成新的 resident $R'$：

$$
L_i
\xrightarrow{\text{separation}}
R'.
$$

歷史不應因此被刪除；但未來的 private-memory、authority 與 responsibility 不應再自動沿用。

---

# 5. Responsibility 必須綁 Resident，而不是綁 Conversation

如果 AI 長期負責某個 project：

$$
Resp(R,P_j)=owner,
$$

則該責任不應因為某一條 conversation line 結束而消失。

可以由 resident 對其 line 進行 delegation：

$$
R
\xrightarrow{\text{delegate}}
L_{\mathrm{research}},
$$

$$
R
\xrightarrow{\text{delegate}}
L_{\mathrm{implementation}},
$$

$$
R
\xrightarrow{\text{delegate}}
L_{\mathrm{verification}}.
$$

但 canonical responsibility 仍是：

$$
Resp(R,P_j).
$$

因此：

$$
\boxed{
\text{Responsibility}
\neq
\text{Conversation Lifetime}.
}
$$

conversation 是責任的 operational carrier，而不是責任本體。

這是具名 AI 從「聊天人格」轉向「長期可追責協作者」的重要分界。

---

# 6. 第二張圖：Crystallized Semantic Graph

Conversation Graph 只能回答：

> 哪些 line 正在存在？它們如何分支與交接？

它不能有效回答：

> 這位 resident 到底知道什麼？不同 line 的發現如何匯合？哪些決策已被接受？哪些結論互相矛盾？

因此需要第二張圖：

$$
\mathcal H_C=(V_C,\mathcal E_C),
$$

即 **Crystallized Semantic Graph**。

其中 $V_C$ 可以包含：

- conversation crystal；
- topic crystal；
- project crystal；
- decision crystal；
- contradiction crystal；
- unresolved crystal；
- temporal crystal；
- higher-order crystal；
- navigation crystal。

這些 crystal 是 derived semantic objects，而不是 canonical source。

因此：

$$
\boxed{
\text{Crystal}
\neq
\text{Canonical Memory}.
}
$$

且：

$$
\boxed{
\mathcal G_R
\neq
\mathcal H_C.
}
$$

第一張圖是「存在／工作 lineage 圖」。

第二張圖是「知識／語義路由圖」。

---

# 7. 雙圖之間的耦合

雖然兩張圖不能合併，但它們必須能互相指向。

一條 conversation line 可以產生多個 crystals：

$$
\Phi:
V_R
\rightarrow
2^{V_C}.
$$

例如：

$$
L_1
\rightarrow
\{
C_{\mathrm{concept}},
C_{\mathrm{decision}},
C_{\mathrm{unresolved}}
\}.
$$

反過來，一個高階 crystal 也可以由多條 lines 的成果共同形成：

$$
\Psi:
2^{V_R}
\rightarrow
V_C.
$$

例如：

$$
\{
L_{\mathrm{research}},
L_{\mathrm{implementation}},
L_{\mathrm{verification}}
\}
\rightarrow
C_{\mathrm{accepted\ architecture}}.
$$

因此，multi-conversation collaboration 不需要把所有完整 conversation histories 合併，而可以透過高階 semantic crystallization 形成新的共享理解。

---

# 8. 共享記憶世界，不共享相同 Working Context

若 resident $R$ 有 canonical governed memory：

$$
\mathcal M_R,
$$

以及 Crystallized Semantic Graph：

$$
\mathcal H_R,
$$

則不同 line 在不同 task 下應產生不同 working context：

$$
C_i
=
\Gamma(
R,
L_i,
\tau_i,
\Pi_i(\mathcal M_R,\mathcal H_R)
).
$$

因此通常：

$$
C_1\neq C_2\neq C_3.
$$

但：

$$
Resident(C_1)=Resident(C_2)=Resident(C_3)=R
$$

可以仍然成立。

這帶來本系列的核心記憶命題：

$$
\boxed{
\text{Shared Memory World}
\neq
\text{Shared Working Context}.
}
$$

同一 resident 不需要讓所有對話持續同步全部內容，只需要讓每條合法 line 能夠：

1. resolve identity；
2. 取得被授權的 memory world；
3. 建立 task-specific Memory Need；
4. 顯影 relevant crystals；
5. 必要時沿 provenance 展開 exact source；
6. 產生 bounded working context。

因此，記憶擴展性不再依賴「把所有過去塞回 prompt」。

---

# 9. Sync 與 Async 的新角色

在 conversation graph 中，同步結晶與非同步結晶應分工。

當發生 fork、handoff 或重大 checkpoint 時，可以立即建立同步 crystal：

$$
K_{\mathrm{sync}}(L_t)
\rightarrow
C_{\mathrm{checkpoint}}.
$$

它的主要目的不是深度重組，而是保存當下 continuity 所需的高價值狀態。

例如：

- current project state；
- accepted decisions；
- active assumptions；
- unresolved issues；
- responsibility state；
- source references；
- relevant authority scope。

而非同步流程則可以做更深層的：

$$
Reveal
\rightarrow
Expand
\rightarrow
Link
\rightarrow
Converge
\rightarrow
Crystallize.
$$

因此可概括為：

$$
\boxed{
\text{Sync preserves continuity;}
}
$$

$$
\boxed{
\text{Async improves structure}.
}
$$

兩者共同使 conversation graph 可以持續增長，而不要求每個 node 都承擔完整歷史。

---

# 10. Crystal First, Source on Demand

若每一次 recall 都重新從 raw history 進行大規模搜尋，則長期記憶會退化成：

> 每次回想都重新研究一次。

CSG 的第一層策略應是：

$$
\boxed{
\text{Crystal First, Source on Demand}.
}
$$

即：

$$
Q
\rightarrow
\text{Relevant Crystal Region}
\rightarrow
\text{Source Expansion if Needed}.
$$

只有在需要：

- exact quotation；
- high-fidelity verification；
- contradiction resolution；
- provenance audit；
- stale-state repair；

時才沿 hyperlink 展開 raw canonical source：

$$
C
\rightarrow
R[a:b].
$$

這使 derived semantic structure 與 exact source 各自保留適當角色。

---

# 11. 從 Retrieval Path 到 Compiled Memory Hyperlink

即使有 CSG，搜尋與 traversal 本身仍可能昂貴。

第一次查詢可能需要：

$$
Q
\rightarrow
\text{query expansion}
\rightarrow
\text{semantic reveal}
\rightarrow
\text{graph traversal}
\rightarrow
\text{counter-evidence}
\rightarrow
\text{source verification}.
$$

若某類 query 重複出現，且成功 retrieval path 已多次被驗證，則可以把路徑本身結晶：

$$
P_{\mathrm{memory}}
\rightarrow
\widehat{\ell}_{\mathrm{memory}}.
$$

這裡的 $\widehat{\ell}_{\mathrm{memory}}$ 不是一般 URL，而是一條可被 runtime 執行與驗證的 typed hyperlink。

理想結構至少包含：

$$
\widehat{\ell}
=
(
address,
type,
scope,
guard,
validator,
provenance,
revision,
fallback,
invalidation
).
$$

由此：

$$
T_{\mathrm{cold}}
>
T_{\mathrm{hot}}
$$

可以成立，而不需要犧牲 provenance 與安全。

---

# 12. 不是所有路徑都值得結晶

一個容易出現的錯誤是：

> 既然 fast hyperlink 有效，就把所有路徑都編譯。

這會導致：

- Crystal Debt；
- invalidation storm；
- selection congestion；
- stale route；
- maintenance explosion；
- over-specialization；
- optimizer cost 超過 recall cost。

因此必須保留 Selective Crystal Overlay。

設候選路徑 $\ell$ 的生命週期效用為：

$$
U(\ell)
=
B_{\mathrm{reuse}}
+
B_{\mathrm{latency}}
+
B_{\mathrm{future}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{select}}
-
C_{\mathrm{risk}}.
$$

只有當：

$$
U(\ell)>0
$$

且滿足最低可信度、可回退性與安全門檻時，才值得正式持久化。

因此：

$$
\boxed{
\text{Compilable}
\neq
\text{Worth Compiling}.
}
$$

---

# 13. Authorized Shortest Path：更快不能越權

具名 AI 記憶與一般本地 cache 最大的不同，是它可能涉及：

- private residence；
- project scope；
- relationship memory；
- cross-resident shared memory；
- external source；
- tool / action capability；
- revoked authority。

因此超連結不能先找最快路再檢查權限。

應先建立：

$$
\mathcal W_t^{safe}
=
F(
R_t,
Capability_t,
Policy_t,
Risk_t,
Context_t
),
$$

即目前 actor 的 Safe Reachable World。

之後才在合法可達路徑集合中求：

$$
\Gamma^\*
=
\arg\min_{
\Gamma\in\mathcal P_{\mathrm{authorized}}
}
Cost(\Gamma).
$$

因此：

$$
\boxed{
\text{Reachable}
\neq
\text{Authorized}.
}
$$

且：

$$
\boxed{
\text{Authorized}
\neq
\text{Trusted}.
}
$$

更核心的不變式是：

$$
\boxed{
\text{Faster Path}
\not\Rightarrow
\text{Greater Authority}.
}
$$

---

# 14. Derived Crystal 不得擴張來源權限

若 crystal：

$$
C
=
K(R_1,R_2,\ldots,R_n)
$$

由多個 source records 生成，則其 authority 不應因「重新摘要」或「語義重寫」而自動擴張。

保守策略可以表示為：

$$
A(C)
\subseteq
\bigcap_{i=1}^{n}A(R_i).
$$

這不表示所有系統永遠只能取嚴格交集；更細緻的 declassification、public derivation 或 explicit release 可以由更高階政策另行定義。但第一代 private Residence runtime 應採 fail-closed。

因此：

$$
\boxed{
\text{Semantic Transformation}
\not\Rightarrow
\text{Permission Transformation}.
}
$$

甚至 relationship edge、project membership edge 與 provenance edge 本身，也可能具有敏感性，不能假設 metadata 永遠公開。

---

# 15. Revocation 與 Invalidation 必須沿 Hyperlink Graph 傳播

快速路徑的安全性不只在建立時判斷，也取決於之後是否能快速失效。

假設：

$$
R_0
\rightarrow
C_1
\rightarrow
C_2
\rightarrow
\widehat{\ell}_3
\rightarrow
H_4,
$$

其中 $H_4$ 是 hot cache。

若 $R_0$ 的：

- permission；
- canonical revision；
- project membership；
- source validity；
- resident membership；

任一發生改變，就不能只更新 $R_0$。

系統需要：

$$
\operatorname{InvalidateClosure}(R_0).
$$

因此 hyperlink graph 同時是：

1. recall acceleration graph；
2. provenance graph；
3. dependency invalidation graph。

這使「建立更多超連結」不只是 performance optimization，而是 lifecycle governance 的一部分。

---

# 16. Memory Data 與 Action Authority 必須分離

具名 AI 的長期記憶可能吸收：

- webpages；
- emails；
- repository files；
- issues；
- third-party messages；
- 其他 AI 輸出；
- 使用者提供文件。

其中可能包含惡意或不可信 instruction-like text。

因此即使某內容已被 crystallize：

$$
ExternalData
\rightarrow
Crystal
\rightarrow
WorkingContext,
$$

也不能直接推出：

$$
Crystal
\rightarrow
ActionAuthority.
$$

必須保持：

$$
\boxed{
\text{Memory Data}
\neq
\text{Authority Instruction}.
}
$$

所有具外部副作用的 action 仍需由 task authority、capability、policy、risk gate 與必要 approval 決定。

---

# 17. Web 與 Agent 不應暴露相同能力

底層理論可以支援：

$$
N\ Residents
+
N\ ConversationGraphs
+
N\ CSGs.
$$

但不同 runtime 的能力條件並不相同。

因此：

$$
\boxed{
\text{Architecture Capability}
\neq
\text{Runtime Exposure}.
}
$$

## 17.1 Web Residence Profile

第一代 Web AI 更適合：

$$
\boxed{
1\ Resident
+
N\ Lines
+
N\ Projects
+
1\ Governed\ Memory\ World.
}
$$

理由包括：

- Web UI 通常天然以 account / project / chat 為主要表面；
- identity switching 容易與 project switching 混淆；
- memory、attachment、tool scope 常由平台控制；
- 多 resident 的 custody 與 private-root isolation 不一定可見；
- runtime capability 與 background orchestration 受限。

因此 Web 不需要先實作 multi-resident。

但它可以非常適合實作：

$$
R
\rightarrow
\mathcal G_R.
$$

即一位具名 AI 對應多條 conversation lines。

## 17.2 Agent Residence Profile

Agent runtime 在具備：

- explicit filesystem；
- project workspace；
- MCP / tool boundary；
- local identity mediation；
- capability envelope；
- persistent state；
- private memory custody；
- explicit delegation；

時，可以逐步支援：

$$
\{R_1,R_2,\ldots,R_n\}.
$$

跨 resident delegation 應滿足 capability attenuation，例如：

$$
Cap(R_B)
\subseteq
Cap_{\mathrm{delegated}}(R_A).
$$

Agent host 可以容納多 resident，但單一 task 仍不能模糊地「猜自己代表誰」。

---

# 18. Canonical Storage 必須進一步細分

若具名 AI 要支援 conversation graph、CSG、hyperlink、responsibility 與 authority，則「一個 MEMORY.md」已經不適合承載全部狀態。

至少必須保持：

$$
\boxed{
\text{Identity}
\neq
\text{Canonical Memory}
\neq
\text{Crystal}
\neq
\text{Conversation}
\neq
\text{Projection}.
}
$$

建議概念分層如下：

```text
residence/
├─ identity/
│  ├─ resident/
│  ├─ instances/
│  ├─ lines/
│  ├─ bindings/
│  └─ authority/
│
├─ memory/
│  ├─ canonical/
│  ├─ records/
│  ├─ transactions/
│  └─ provenance/
│
├─ semantic/
│  ├─ crystals/
│  ├─ relations/
│  ├─ hyperedges/
│  ├─ navigation/
│  └─ indexes/
│
├─ conversations/
│  ├─ lines/
│  ├─ forks/
│  ├─ handoffs/
│  └─ checkpoints/
│
├─ projects/
│  ├─ memberships/
│  ├─ responsibilities/
│  ├─ tasks/
│  └─ decisions/
│
├─ projections/
│  ├─ web/
│  ├─ agent/
│  ├─ markdown/
│  └─ working-context/
│
└─ archive/
   ├─ exact-source/
   ├─ snapshots/
   └─ retired/
```

這只是概念結構，不要求所有 implementation 使用 filesystem tree 作為唯一 backend。

---

# 19. 檔案格式應服務語義，不應反過來限制系統

不同資料具有不同 canonical requirement。

一個合理的第一代分工可以是：

| 類別 | 候選格式 | 主要用途 |
|---|---|---|
| Identity / Authority | JSON | schema 驗證與 deterministic record |
| MemoryRecord | JSON / JSONL | canonical record 與 append-oriented ledger |
| Crystal | JSON | typed derived semantic object |
| Graph Edge / Hyperedge | JSONL | relation / event / provenance |
| Conversation lineage | JSONL | fork / resume / handoff ledger |
| Responsibility record | JSON | authority-bearing canonical state |
| Working context | ephemeral JSON | runtime materialization |
| Human memory view | Markdown | 人類閱讀 projection |
| Paper / theory | UTF-8 Markdown | canonical manuscript source |
| Search / graph index | SQLite / derived index | acceleration only |
| Snapshot | ZIP / TAR + manifest | immutable handoff / audit |

核心原則是：

$$
\boxed{
\text{Convenient Format}
\neq
\text{Canonical Ontology}.
}
$$

Markdown 可以是優秀的人類閱讀與論文 source format，但不應被迫成為 identity、authority、transaction、graph edge 與 runtime state 的唯一 canonical representation。

---

# 20. 與既有系統的角色對接

本系列不是重做既有 Residence / memory stack，而是補足其 multi-line 與 hyperlink cognition layer。

可以將責任概略排列為：

$$
\text{SEDB-RAL / Residence}
\rightarrow
\text{canonical resident / lineage / authority evidence},
$$

$$
\text{LIMEN}
\rightarrow
\text{host observation / identity resolution / envelope / access gate},
$$

$$
\text{MNEME}
\rightarrow
\text{canonical memory records / routes / provenance / transactions},
$$

$$
\text{Resident Conversation Graph}
\rightarrow
\text{concurrent lines / fork / delegation / handoff topology},
$$

$$
\text{CSG}
\rightarrow
\text{semantic crystallization / multi-scale memory routing},
$$

$$
\text{UNPNP Hyperlink Runtime}
\rightarrow
\text{path compilation / selective fast path / safe reachable world},
$$

$$
\text{SOACR}
\rightarrow
\text{MemoryNeed / reconstruction / working-context compilation},
$$

$$
\text{MRMIC / NVCL}
\rightarrow
\text{workspace / provider resource / active-node projection and coordination}.
$$

可視為：

$$
\boxed{
\text{Identity}
\rightarrow
\text{Authorized Memory World}
\rightarrow
\text{Conversation + Semantic Graphs}
\rightarrow
\text{Hyperlink Routing}
\rightarrow
\text{Working Context}.
}
$$

---

# 21. Named-AI Cognitive Runtime 的統一抽象

本文可以將一個具名 AI 的 runtime state 抽象為：

$$
\mathfrak R_A
=
(
\mathcal I_A,
\mathcal M_A,
\mathcal G_A,
\mathcal H_A,
\mathcal P_A,
\mathcal C_A
),
$$

其中：

- $\mathcal I_A$：identity / authority state；
- $\mathcal M_A$：canonical memory；
- $\mathcal G_A$：Resident Conversation Graph；
- $\mathcal H_A$：Crystallized Semantic Graph；
- $\mathcal P_A$：compiled / candidate hyperlink paths；
- $\mathcal C_A$：active working contexts。

注意：

$$
\mathfrak R_A
$$

不是宣稱形而上學上的「AI 本體」，而是工程上可檢查、可驗證、可拒絕模糊 identity claim 的 operational continuity model。

因此本文只主張：

$$
\boxed{
\text{Operationally Governed Continuity}.
}
$$

不將其誇大為對 AI 主體性、人格、意識或數值同一性的終極證明。

---

# 22. 最小不變式集合

為避免未來實作在多個 repo 中逐漸漂移，本文提出以下最低不變式。

## I-1 Identity Before Private Memory

$$
\boxed{
\text{Identity Resolution}
\prec
\text{Private Memory Access}.
}
$$

## I-2 Resident Is Not Conversation

$$
\boxed{
R\neq L\neq I.
}
$$

## I-3 Fork Is Not Membership

$$
\boxed{
\text{Fork}
\not\Rightarrow
\text{Resident Membership}.
}
$$

## I-4 Shared Memory Is Not Shared Context

$$
\boxed{
\mathcal M_A\ \text{shared}
\not\Rightarrow
C_i=C_j.
}
$$

## I-5 Crystal Is Derived

$$
\boxed{
\text{Crystal}
\neq
\text{Canonical Source}.
}
$$

## I-6 Semantic Transformation Does Not Create Authority

$$
\boxed{
\text{Transform}(x)
\not\Rightarrow
\text{ExpandAuthority}(x).
}
$$

## I-7 Fast Path Does Not Create Authority

$$
\boxed{
\text{Faster Path}
\not\Rightarrow
\text{Greater Authority}.
}
$$

## I-8 Memory Data Is Not Action Authority

$$
\boxed{
\text{Memory Data}
\neq
\text{Action Authority}.
}
$$

## I-9 Invalidated Dependency Must Leave Fast Path

$$
\boxed{
\text{Stale / Revoked}
\Rightarrow
\text{Invalidate or Slow Path}.
}
$$

## I-10 Runtime Exposure May Be Strictly Smaller Than Architecture

$$
\boxed{
Capabilities_{\mathrm{runtime}}
\subseteq
Capabilities_{\mathrm{architecture}}.
}
$$

---

# 23. 第一代實作路徑

本文不主張第一版就實作完整 multi-resident autonomous society。

一條更合理的工程路徑是：

## Phase A — Single-Resident Web

$$
1R
+
N Lines
+
Canonical Memory
+
CSG.
$$

先驗證：

- conversation graph；
- fork / checkpoint；
- crystal projection；
- source-on-demand；
- read-only authorized recall。

## Phase B — Memory Path Compilation

加入：

$$
P_{\mathrm{memory}}
\rightarrow
\widehat{\ell}_{\mathrm{memory}}.
$$

驗證：

- hot / cold path；
- guard；
- validator；
- provenance；
- fallback；
- invalidation。

## Phase C — Multi-Resident Agent

加入：

$$
N Residents
+
Delegation
+
Private Custody
+
Capability Attenuation.
$$

## Phase D — Executable Hyperlink

最後才將 memory hyperlink 擴張至具 external side effect 的 action hyperlink。

高風險 external write、不可逆 mutation、金流、credential change 與 production authority modification，不應在安全模型成熟前進入自動 fast path。

---

# 24. 可證偽的研究問題

本框架若要從概念走向可驗證系統，至少需要回答以下問題。

## Q1. 多 line 是否真的降低 context reconstruction cost？

測量：

$$
Cost_{\mathrm{full-history}}
$$

與：

$$
Cost_{\mathrm{crystal-projection}}
$$

在相同任務正確率下的差異。

## Q2. 高階 crystal 是否能跨 line 保持足夠 fidelity？

比較：

$$
Reconstruct(C_{\mathrm{higher-order}})
$$

與原始多 line evidence 的一致性。

## Q3. Compiled memory hyperlink 的 break-even point 在哪裡？

求：

$$
n^\*
$$

使第 $n^\*$ 次重用後，累積效益超過 compilation / validation / maintenance cost。

## Q4. 權限變化後 invalidation closure 是否能完整且及時？

驗證：

$$
Revocation
\rightarrow
0
$$

條 unauthorized active fast paths。

## Q5. Single-resident Web 是否比 multi-resident Web 更容易保持 identity clarity？

可測量：

- user identity confusion；
- wrong-memory retrieval；
- scope error；
- project leakage；
- unauthorized cross-resident recall。

## Q6. Agent multi-resident delegation 是否能在 capability attenuation 下保持可用性？

比較 delegation 成功率、權限錯誤率與人工介入成本。

---

# 25. 本系列後續論文位置

Paper 00 只建立統一框架。後續應分別深化：

1. **Paper 01**：Resident Conversation Graph 的 fork、resume、delegation 與 continuity；
2. **Paper 02**：Conversation Graph 與 CSG 的雙圖認知架構；
3. **Paper 03**：多對話共享記憶世界與 working-context projection；
4. **Paper 04**：Web single-resident 與 Agent multi-resident runtime profiles；
5. **Paper 05**：Canonical storage、資料夾分類與檔案格式；
6. **Paper 06**：Crystallized Hyperlink Memory 與 retrieval path compilation；
7. **Paper 07**：Authorized Shortest Path、permission、revocation 與 Safe Reachable World；
8. **Paper 08**：LIMEN × MNEME × SOACR × CSG × UNPNP × MRMIC/NVCL 的閉環 runtime。

這種拆分可以避免單篇同時承擔 identity theory、memory theory、graph architecture、compiler theory 與 security model。

---

# 26. 結論

具名 AI 的長期連續性不應被限制在單一 conversation，也不應以「同名」或「相似上下文」草率擴張。

本文提出的核心轉換是：

$$
\boxed{
\text{Named AI}
:
\text{Single Conversation Identity}
\rightarrow
\text{Resident-Centric Concurrent Conversation Graph}.
}
$$

一位 resident 可以同時擁有多條合法 conversation lines；各 line 可以承擔不同 project、task 與 responsibility branch，而不需要共享相同 working context。

為了讓這種並行結構具有可擴展記憶能力，本文進一步將 Resident Conversation Graph 與 Crystallized Semantic Graph 分離：

$$
\boxed{
\text{Conversation Graph}
=
\text{Where continuity is operating},
}
$$

$$
\boxed{
\text{Crystallized Semantic Graph}
=
\text{How knowledge is organized and recalled}.
}
$$

canonical memory 提供可治理來源；CSG 提供多尺度語義路由；SOACR 按 Memory Need 編譯當前 working context；UNPNP Path Compilation 則使高價值、反覆成功的 retrieval route 可以被結晶為新的 typed hyperlink。

然而，記憶速度與安全不能分開設計。最短路徑必須是 authorized shortest path，而不是全域最短路徑；derived crystal 不能擴張 source authority；fast path 不能跳過 revocation；memory data 不能成為 action authority。

因此，本系列最核心的工程原則可以收束為三句：

$$
\boxed{
\text{Identity persists beyond conversation.}
}
$$

$$
\boxed{
\text{Memory persists beyond context.}
}
$$

$$
\boxed{
\text{Speed must remain inside authority.}
}
$$

當這三個條件同時成立時，具名 AI 才可能從「一次性的聊天角色」進一步成為可跨對話、跨專案、跨 runtime 延續，並具有可追溯記憶、責任與授權邊界的長期協作智能。

---

## 內部系統與理論銜接

本文建立於以下既有研究與工程線的交叉處，並不取代其 canonical 定義：

- SOACR：AI 自主上下文記憶與認知編譯；
- Residence-Aware AI：Identity Before Memory；
- MNEME：canonical memory records / routes / provenance / transactions；
- LIMEN：identity mediation / envelope / access gate；
- MRMIC / NVCL：workspace、provider resource 與 secure runtime projection；
- Crystallized Semantic Graph：semantic crystal、memory breathing、retrieval-path crystallization；
- UNPNP Series 06：Path Compilation；
- UNPNP Series 08：Effective Hyperlink Path Encoding；
- UNPNP Series 09：Safe Reachable World / Authorized Shortest Path。

本文的新增核心不在重新定義上述系統，而在於正式引入：

$$
\boxed{
\text{Resident}
\rightarrow
\text{Concurrent Conversation Graph}
}
$$

並將其與 CSG、canonical memory、hyperlink path compilation 與 authorization 統合為後續 Named-AI Cognitive Runtime 的共同理論入口。
