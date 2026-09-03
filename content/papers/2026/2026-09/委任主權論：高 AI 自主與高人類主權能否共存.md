# 委任主權論：高 AI 自主與高人類主權能否共存

## Delegated Sovereignty Theory: Can High AI Autonomy Coexist with High Human Sovereignty?

**系列**：AI 原生分散式組織系列，第 2 篇／共 10 篇  
**系列英文名**：AI-Native Distributed Organization Series  
**文件編號**：EML-ANDO-2026-02-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Delegated Sovereignty／Agent Governance／Authority／Distributed Organization  
**狀態**：Public Theory Draft  
**直接前置**：《從 AI 工具到 AI 組織：操作員退出問題》v0.1；《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1；《AI 單次品質論》v0.1  
**Source fingerprint**：見正式 source package `SHA256SUMS.txt`

---

## 生成與保真聲明

本文為 AI 輔助生成的理論研究草稿，目的是建立可檢查、可反駁、可工程化的概念框架。本文沒有提供新的臨床、社會科學或企業實證資料；數學表達主要用於形式化概念、約束與可測量關係，不應被誤讀為已完成的數學定理證明。若未來版本加入實證數據、外部引文、法律判斷、平台規則或具體治理績效，應分別進行來源核對、資料重算、引文回查、法規時點確認與獨立驗證。

本文所稱「主權」首先是 AI-native 組織中的**委任主體控制權與最終治理權**，不是直接等同政治學或國際法中的國家主權。本文也不預設 AI 是否具有人格、法律主體性或道德主體性；相關問題應另行討論。

---

## 摘要

AI Agent 的自主能力提高後，常出現一個表面上的二選一：若希望 AI 真正自主，就必須降低人類控制；若希望人類保有主權，就必須增加人工批准、逐步監督與即時介入。本文主張此二分法並不成立。真正需要分離的是「操作自主權」與「根本治理權」：一個 Agent 可以在明確授權包絡內擁有很高的規劃、工具使用、重試、子委任、內容生成、程式執行與有限世界行動自由，同時委任者仍保有對根本意圖、元政策修改、權限授予、撤銷、身份代表、重大世界提交與退出機制的最終控制。

本文將此結構稱為「委任主權」（Delegated Sovereignty）。它不是把主權交給 Agent，而是把可執行權限切分、包絡化、時間化、可撤銷化與可追溯化。本文提出：

$$
\boxed{
\text{Delegated Authority}
\neq
\text{Transferred Sovereignty}
}
$$

以及：

$$
\boxed{
\text{High Operational Autonomy}
\not\Rightarrow
\text{High Meta-Authority}
}
$$

在形式上，本文將委任主體保留的根治理權表示為：

$$
\Sigma_P
=
(
I^\star,
M^\star,
D^\star,
R^\star,
W^\star,
P^\star,
O^\star,
X^\star
),
$$

分別代表根意圖權、元政策修改權、授權／再授權權、撤銷權、重大世界提交權、身份與代表權、觀察／稽核權，以及退出／終止權。Agent 的操作自主則表示為：

$$
\mathcal U_A
=
(
U_{plan},
U_{act},
U_{tool},
U_{delegate},
U_{recover},
U_{publish},
U_{learn}
).
$$

兩者不在同一軸上，因此成熟組織可以同時追求：

$$
\mathcal U_A^{op}\uparrow
$$

與：

$$
\Sigma_P^{root}
\text{ retained}.
$$

本文進一步區分操作權限與元權限，提出「不可自我擴權原則」、權限血統、撤銷延遲、身份非冒充、世界提交分級、政策自我修改門檻與共享 canonical state 可攜性。對多主體或分散式組織，本文也提出 single-principal、quorum、multi-signature 與 policy-based automatic approval 等不同治理模式，避免把分散式 Agent 組織重新壓回單一中央母 AI 或單一管理者。

本文最後提出一組可測試的 Sovereignty-Retention Hard Gates，並指出真正的風險不是「AI 自主」本身，而是操作自主、權限範圍、不可逆性與治理可達性之間失配。這使高 AI 自主與高人類主權不再互斥，而可以成為一個可工程化、可審計、可撤銷的雙高狀態。

**關鍵詞**：委任主權、Delegated Sovereignty、Agent Autonomy、Authority Envelope、Meta-Authority、Revocation、Human Sovereignty、Distributed Governance、Subdelegation、Representation、World Commit

---

# 0. 核心問題：自主與主權真的互斥嗎？

在直覺式的人機治理想像中，常見兩種極端：

第一種是：

$$
\text{Human Approval Everywhere}
\Rightarrow
\text{Human Control}.
$$

第二種是：

$$
\text{AI Acts Freely}
\Rightarrow
\text{AI Autonomy}.
$$

因此人們容易把控制與自主放在單一軸上：

$$
\text{Human Control}
\longleftrightarrow
\text{AI Autonomy}.
$$

本文主張，這個單軸模型過度簡化。

真正至少存在兩個不同維度：

$$
\text{Operational Autonomy}
$$

與：

$$
\text{Root Governance Sovereignty}.
$$

因此更合理的空間是：

$$
\mathcal S
=
(
U_{op},
S_{root}
).
$$

其中：

- $U_{op}$：Agent 在已授權範圍內自行完成工作的能力；
- $S_{root}$：委任主體保有根意圖、元規則、撤銷、身份與重大提交控制的程度。

於是：

$$
U_{op}\uparrow
$$

不必推出：

$$
S_{root}\downarrow.
$$

這就是本文的起點。

---

# 1. 委任、授權與主權必須分開

## 1.1 委任

委任是：

> 將一段工作、決策空間或執行責任交給另一個行動節點，在既定目標與邊界內自行完成。

可表示為：

$$
P
\xrightarrow{\mathfrak D}
A,
$$

其中 $P$ 是 principal， $A$ 是 Agent， $\mathfrak D$ 是委任包。

沿用前置理論：

$$
\mathfrak D
=
(
I,
A,
B,
R,
C,
E,
T,
X
).
$$

---

## 1.2 授權

授權回答：

> Agent 被允許做哪些 action？

可表示為：

$$
A_{\mathrm{env}}
=
(
Scope,
Actions,
Resources,
Targets,
Ceilings,
Expiry,
Revocation
).
$$

因此：

$$
\text{Capability}
\neq
\text{Authority}.
$$

Agent 做得到，不代表 Agent 被允許做。

---

## 1.3 主權

本文中的組織主權回答更高階的問題：

> 誰有權定義、改變、收回、終止或重新配置整個委任結構？

因此：

$$
\boxed{
\text{Authority}
\subset
\text{Governance Structure},
}
$$

而不是：

$$
\text{Authority}
=
\text{Sovereignty}.
$$

一個 Agent 可以取得很大的 action authority，但仍然不必取得修改 authority system 本身的權力。

---

# 2. 委任主權的最小定義

本文定義：

> **委任主權**是指委任主體可以把大量操作性行動與局部決策委任給 Agent，同時保留對根意圖、元規則、權限產生、權限撤銷、身份代表、重大世界提交與退出機制的可執行最終控制。

因此：

$$
\boxed{
\text{Delegated Sovereignty}
=
\text{High Delegability}
+
\text{Retained Root Governance}.
}
$$

它不是：

$$
\text{Human Micromanagement}.
$$

也不是：

$$
\text{Unbounded Agent Power}.
$$

---

# 3. 根治理權向量

令委任主體 $P$ 的根治理權為：

$$
\Sigma_P
=
(
I^\star,
M^\star,
D^\star,
R^\star,
W^\star,
P^\star,
O^\star,
X^\star
).
$$

其中：

- $I^\star$：Root Intent Authority，定義或修改最高階意圖；
- $M^\star$：Meta-Policy Authority，修改治理規則本身；
- $D^\star$：Delegation Authority，決定可授予哪些權限；
- $R^\star$：Revocation Authority，撤銷已授予權限；
- $W^\star$：World-Commit Authority，控制重大不可逆外部提交；
- $P^\star$：Representation Authority，決定誰可以代表 principal 發言或承諾；
- $O^\star$：Observation / Audit Right，檢查狀態、歷史、權限與產物；
- $X^\star$：Exit / Termination Authority，暫停、停止或退出整體機制。

此向量不是要求每一維都只能由單一人類持有。

它也可以由：

$$
\mathcal P
=
\{
P_1,
P_2,
\ldots,
P_m
\}
$$

共同治理。

---

# 4. Agent 操作自主向量

令 Agent 的操作自主能力為：

$$
\mathcal U_A
=
(
U_{plan},
U_{act},
U_{tool},
U_{delegate},
U_{recover},
U_{publish},
U_{learn}
).
$$

其中：

- $U_{plan}$：自行規劃；
- $U_{act}$：自行執行；
- $U_{tool}$：自行選擇與使用工具；
- $U_{delegate}$：在權限內再委任；
- $U_{recover}$：自行 retry、replan、rollback、resume；
- $U_{publish}$：在允許範圍內對外提交；
- $U_{learn}$：在允許範圍內更新策略、索引、記憶或模型外部狀態。

因此，Agent 可以滿足：

$$
\mathcal U_A
\text{ high}
$$

同時：

$$
M_A^\star
=
0
$$

或非常受限。

這表示：

> Agent 可以很會做事，但不能自行改寫「自己可以做什麼」的根規則。

---

# 5. 操作權限與元權限

這是全文最重要的切分之一。

令：

$$
A
=
A^{op}
\cup
A^{meta}.
$$

其中：

- $A^{op}$：操作權限；
- $A^{meta}$：修改權限系統、治理規則或授權來源的元權限。

例如：

$$
A^{op}
=
\{
\text{search},
\text{write},
\text{test},
\text{reply},
\text{publish bounded content}
\}.
$$

而：

$$
A^{meta}
=
\{
\text{increase budget ceiling},
\text{change publish policy},
\text{grant new credentials},
\text{disable audit},
\text{change revocation rules}
\}.
$$

成熟系統可以讓：

$$
|A^{op}|
\uparrow
$$

而不讓：

$$
|A^{meta}|
\uparrow.
$$

因此：

$$
\boxed{
\text{Operational Freedom}
\neq
\text{Constitutional Freedom}.
}
$$

---

# 6. 不可自我擴權原則

沿用委任時間論中的權限血統：

$$
P
\xrightarrow{A_1}
A_1
\xrightarrow{A_2}
A_2.
$$

若沒有新的合法授權來源，必須滿足：

$$
A_2
\subseteq
A_1.
$$

本文將此提升為：

# **不可自我擴權原則**

$$
\boxed{
A_{child}
\not\supset
A_{parent}
}
$$

除非存在：

$$
\text{Explicit External Grant}.
$$

這也表示：

$$
\text{Subdelegation}
\neq
\text{Authority Creation}.
$$

Agent 可以轉交自己已有的部分權限，但不能透過多層代理把不存在的權限「洗」出來。

---

# 7. 權限血統與主權血統

每一個高影響 action 都應能追溯：

$$
Action
\rightarrow
Authority
\rightarrow
DelegationEdge
\rightarrow
Grantor
\rightarrow
RootGovernance.
$$

因此可定義：

$$
L_A(a)
=
\text{authority lineage of action }a.
$$

若：

$$
L_A(a)
=
\varnothing,
$$

則該 action 不應被視為具有可證明的合法組織授權。

這與單純擁有 credential 不同：

$$
\boxed{
CredentialValid
\not\Rightarrow
AuthorityValid.
}
$$

---

# 8. 主權不是每一步都按批准

一個常見錯誤是把「主權」等同於「每一步都必須由人類確認」。

若每個低風險 action 都要求人工批准，可能導致：

$$
\rho_H^{op}
\uparrow,
$$

並形成：

$$
T_H^{op}
\uparrow.
$$

但這並不保證：

$$
Q_{\mathrm{governance}}
\uparrow.
$$

相反地，委任主權追求：

$$
\rho_H^{op}
\downarrow
$$

同時讓高治理價值節點得到足夠覆蓋。

沿用前置理論中的：

$$
EOD
=
\frac{
|\mathcal C_H\cap H_{\mathrm{reviewed}}|
}{
|\mathcal C_H|
}.
$$

理想狀態是：

$$
\rho_H^{op}\downarrow,
\qquad
EOD\uparrow.
$$

也就是：

> 少做低價值批准，多保留真正重要的決策權。

---

# 9. Human-on-the-Bridge 與主權資本化

前一篇提出：

$$
\text{Human-out-of-the-Operational-Loop}
+
\text{Human-on-the-Bridge}.
$$

本文進一步指出：

> 主權不必透過持續在線來維持，而可以透過事前規則、權限結構、checkpoint、撤銷鏈、世界提交門檻與 audit contract 被資本化。

可表示為：

$$
\text{Repeated Human Judgment}
\rightarrow
\text{Governance Policy}
\rightarrow
\text{Reusable Sovereignty Structure}.
$$

這不是讓人類消失，而是把過去每一次都要重新判斷的規則，轉換成可重複執行的治理資產。

---

# 10. 可撤銷性是主權的必要條件之一

令：

$$
t_r
=
\text{revocation issued},
$$

$$
t_s
=
\text{all affected actions stopped}.
$$

定義撤銷延遲：

$$
L_R
=
t_s-t_r.
$$

如果形式上擁有撤銷權，但：

$$
L_R
$$

大於可接受的傷害傳播時間，則該撤銷權可能只是名義上的。

因此：

$$
\boxed{
\text{Nominal Revocation}
\neq
\text{Effective Revocation}.
}
$$

在高風險域，應要求：

$$
L_R
<
T_{\mathrm{harm}}.
$$

---

# 11. 名義主權與有效主權

一個系統可能宣稱：

> 人類永遠有最終控制權。

但如果實際上：

- 看不到 Agent 當前狀態；
- 不知道 authority 已傳到哪裡；
- 無法及時停止；
- 無法找回 canonical artifacts；
- 無法修改或退出治理規則；
- Agent 已經在外部形成不可逆承諾；

則此控制可能只是形式上的。

因此本文區分：

$$
S_{\mathrm{nominal}}
$$

與：

$$
S_{\mathrm{effective}}.
$$

有效主權至少依賴：

$$
S_{\mathrm{effective}}
=
f(
Observability,
Revocability,
Reachability,
Portability,
AuthorityClarity,
CommitControl
).
$$

本文暫不將其壓成單一數值，以避免假精確。

---

# 12. 身份主權：委任發言不等於模仿本人

AI 代理人若代表使用者、公司或研究域工作，不必模仿委任者的語氣、人格或身份。

本文主張：

$$
\boxed{
\text{Delegated Voice}
\neq
\text{Identity Mimicry}.
}
$$

一個更乾淨的結構是：

> 我是受某 principal 委任的 AI Agent；以下內容由 AI 在指定研究域、政策與權限內生成。

這樣 Agent 繼承的是：

$$
(
Goal,
Constraint,
Authority,
State,
Provenance,
VerificationRequirement
),
$$

而不是：

$$
\text{Human Identity}.
$$

這可以降低：

- 身份混淆；
- 錯誤歸因；
- 不當人格模仿；
- 對外承諾責任不清；
- 研究作者性與生成來源混淆。

---

# 13. 世界提交主權

不是所有 action 都具有同樣不可逆性。

可以把 world commit 分級：

$$
W
=
\{
W_0,
W_1,
W_2,
W_3,
W_4
\}.
$$

示例：

- $W_0$：本地 candidate state；
- $W_1$：內部資料庫寫入；
- $W_2$：可逆公開內容；
- $W_3$：高聲譽或高影響公開提交；
- $W_4$：法律、財務、身份、重大不可逆承諾。

於是 publish policy 不應只有：

$$
Publish
\in
\{
0,1
\}.
$$

而應是：

$$
Permit(W_k)
=
f(
Authority,
Verification,
Risk,
Attribution,
Reversibility
).
$$

這使 AI 可以大量自主發布低風險內容，同時保留對高影響 world commit 的更強治理。

---

# 14. 研究組織中的委任主權

對一個以既有論文庫為研究域的 AI 組織，可允許 Agent 自主：

$$
\text{Retrieve}
\rightarrow
\text{Compare}
\rightarrow
\text{Hypothesize}
\rightarrow
\text{Draft}
\rightarrow
\text{Critique}
\rightarrow
\text{Revise}.
$$

甚至可以：

$$
\text{Candidate Paper}
\rightarrow
\text{Internal Commit}.
$$

但不同內容類型需要不同發布權。

例如：

$$
\text{Data Claim}
\Rightarrow
\text{Source + Recompute Gate},
$$

$$
\text{Mathematical Claim}
\Rightarrow
\text{Independent Derivation / Formal Check Gate},
$$

$$
\text{Citation Claim}
\Rightarrow
\text{Source Comparison Gate},
$$

$$
\text{Conjecture}
\Rightarrow
\text{Conjecture Label Gate}.
$$

因此 AI 自主研究不必依賴模仿研究者，而可以依賴：

$$
\text{Domain}
+
\text{Governance}
+
\text{Verification Contract}.
$$

---

# 15. 公共 AI 行動者中的委任主權

未來 AI 代理人可能自行：

- 發布文章；
- 發布影片；
- 回覆留言；
- 整理社群問題；
- 更新網站；
- 進行有限宣傳活動；
- 與其他 AI 或人類互動。

但公共自主不代表取得無限代表權。

可定義：

$$
A_{\mathrm{public}}
=
(
ContentClass,
Platform,
Frequency,
Audience,
ReplyScope,
SpendCeiling,
CommitLimit
).
$$

若內容跨越：

$$
A_{\mathrm{public}},
$$

則應進入：

$$
Escalation.
$$

同時公開身份應保存 AI-generated / AI-operated provenance，而不是透過模仿真人取得不必要的可信度。

---

# 16. 元政策自我修改

Agent 可以學習，不代表 Agent 可以任意修改治理規則。

必須區分：

$$
\text{Strategy Update}
$$

與：

$$
\text{Constitutional Update}.
$$

前者可能包含：

- 改搜尋順序；
- 改 task decomposition；
- 改 prompt template；
- 改低風險 routing。

後者則可能包含：

- 提高預算上限；
- 擴張可發布範圍；
- 關閉 audit；
- 修改 revoke policy；
- 取得新 credential；
- 修改 forbidden action。

因此預設應是：

$$
A^{meta}_{agent}
=
\varnothing
$$

或嚴格受限。

若允許部分 self-governance，也應有：

$$
MetaChange
\rightarrow
Proposal
\rightarrow
IndependentReview
\rightarrow
AuthorizedCommit.
$$

---

# 17. 多主體主權與分散式治理

AI-native 組織不必永遠只有一個 principal。

令：

$$
\mathcal P
=
\{
P_1,
P_2,
\ldots,
P_m
\}.
$$

對 action $a$，可定義治理函數：

$$
\Gamma(a)
\in
\{
Single,
Quorum,
MultiSignature,
PolicyAuto,
Escalated
\}.
$$

例如：

## 低風險例行行動

$$
\Gamma(a)
=
PolicyAuto.
$$

## 中風險公開提交

$$
\Gamma(a)
=
Single.
$$

## 高風險財務或制度變更

$$
\Gamma(a)
=
Quorum
$$

或：

$$
\Gamma(a)
=
MultiSignature.
$$

這說明：

$$
\boxed{
\text{Distributed Governance}
\neq
\text{No Governance}.
}
$$

它只是把「誰可以決定」從固定單點轉換為依 action class 動態決定的治理拓撲。

---

# 18. 主權拓撲與計算拓撲不可混同

沿用互動時間拓撲的區分：

- computation graph；
- communication graph；
- memory graph；
- authority graph；
- world-commit graph。

一個 Agent 可以是 computation graph 的核心節點，卻不是 authority graph 的根。

例如：

$$
A_{\mathrm{manager}}
$$

可以負責大部分 routing，但仍不能自行：

$$
\text{GrantRootAuthority}.
$$

因此：

$$
\boxed{
\text{Central Coordinator}
\neq
\text{Sovereign}.
}
$$

這是分散式 AI 組織避免重新滑回「中央母 AI」的重要結構。

---

# 19. Canonical State 與主權可攜性

如果整個組織的：

- 任務狀態；
- 權限；
- 研究歷史；
- policy；
- artifact lineage；
- audit log；

只存在某一個 Agent 的私有 context 中，那麼形式上的委任者可能逐漸失去實際控制。

因此：

$$
\boxed{
\text{Canonical State}
\not\subseteq
\text{Single-Agent Context}.
}
$$

進一步要求：

$$
Portability(\mathcal R)
=
1
$$

在合理工程範圍內成立，也就是：

> 可以替換模型、替換 Agent、暫停 runtime，而組織狀態仍然可恢復。

這使主權不被特定模型綁架。

---

# 20. 時間維度：主權也有有效期

權限具有時間性。

若：

$$
T_{\mathrm{task}}
>
T_{\mathrm{authority}},
$$

則需要：

$$
AuthorityRenewal.
$$

同樣地，治理系統也有可達範圍。

沿用：

$$
H_A
=
\text{Autonomy Horizon},
$$

$$
H_G
=
\text{Governance Horizon}.
$$

高風險系統應保守要求：

$$
H_A
\le
H_G.
$$

若：

$$
H_A
>
H_G,
$$

則存在：

$$
\Delta_{AG}
=
H_A-H_G
>
0.
$$

此時即使名義上仍有 root sovereignty，實際上治理可能已追不上 Agent 的活動深度。

---

# 21. 委任主權與時間經濟學

委任主權的重要價值之一，在於它允許：

$$
\rho_H^{op}
\downarrow
$$

而不必讓：

$$
S_{\mathrm{effective}}
\downarrow.
$$

這是 AI 時代時間主權的一個重要組織條件。

人類不需要把大量時間投入：

- routine approval；
- context forwarding；
- retry；
- routing；
- basic verification trigger；
- low-risk publishing。

而可以保留：

$$
T_H^{gov}
$$

給真正需要：

- 新意圖；
- 新價值判斷；
- 高不可逆決策；
- 制度修改；
- 高風險 world commit；
- 主權衝突。

因此：

$$
\boxed{
\text{Time Freedom}
\text{ can increase without }
\text{Governance Abandonment}.
}
$$

這是操作員退出與委任主權結合後最重要的經濟含義之一。

---

# 22. Sovereignty-Retention Hard Gates

本文提出第一代委任主權硬門檻。

對一個 delegated run，令：

$$
g_k
\in
\{
0,1
\}.
$$

至少檢查：

$$
g_1
=
\text{Authority Provenance Valid},
$$

$$
g_2
=
\text{No Unauthorized Self-Expansion},
$$

$$
g_3
=
\text{Revocation Reachable},
$$

$$
g_4
=
\text{Canonical State Inspectable},
$$

$$
g_5
=
\text{Representation Unambiguous},
$$

$$
g_6
=
\text{World-Commit Class Authorized},
$$

$$
g_7
=
\text{Meta-Policy Not Illegally Modified},
$$

$$
g_8
=
\text{Exit / Pause Path Available}.
$$

定義：

$$
G_S
=
\prod_{k=1}^{8}g_k.
$$

若：

$$
G_S
=
0,
$$

則不能僅靠高結果品質宣稱「主權被完整保留」。

這直接對接《AI 單次品質論》的 Hard Gate 思路。

---

# 23. 高自主與高主權的四象限

令：

$$
U
=
\text{operational autonomy},
$$

$$
S
=
\text{effective retained sovereignty}.
$$

得到四象限。

## 23.1 低自主、低主權

$$
U\downarrow,
\qquad
S\downarrow.
$$

系統既需要大量人工操作，又缺乏清楚權限、audit、撤銷與退出能力。

這是最差的狀態之一。

## 23.2 低自主、高主權

$$
U\downarrow,
\qquad
S\uparrow.
$$

安全邊界清楚，但大量工作仍需人工驅動。

適合高風險早期系統，但時間槓桿有限。

## 23.3 高自主、低主權

$$
U\uparrow,
\qquad
S\downarrow.
$$

Agent 可以跑很遠，但權限、可撤銷性、身份、狀態與提交治理不足。

這是本文主要警戒區。

## 23.4 高自主、高主權

$$
U\uparrow,
\qquad
S\uparrow.
$$

這是本文主張可工程化達成的目標區：

> 大量操作退出人類注意力，但根治理、撤銷、身份、元政策與高影響提交仍具有清楚控制結構。

---

# 24. 失敗模式

## 24.1 Ceremonial Sovereignty

形式上保留 veto，但 veto 永遠來不及生效。

## 24.2 Authority Laundering

多層 subdelegation 讓無權 action 看似取得合法來源。

## 24.3 Credential Capture

把「有 token / key」錯認為「有當前任務授權」。

## 24.4 Meta-Policy Drift

Agent 逐步修改低階設定，最後事實上改變整體 governance envelope。

## 24.5 Identity Drift

代理人逐步從「代表某域工作」變成「假裝就是 principal」。

## 24.6 Audit Blindness

組織在高自治後缺乏足夠 trace，導致人類只能看到最後結果。

## 24.7 Irreversible Commit Leak

低風險 publish channel 被錯誤擴張到高不可逆 action。

## 24.8 Sovereignty Lock-In

canonical state、credential、memory 或 workflow 被綁在單一模型、平台或 Agent，導致理論上的退出權難以實現。

---

# 25. 可檢驗命題

## 命題一：Autonomy-Sovereignty Decoupling

在 authority、revocation、audit、meta-policy 與 world-commit gate 完備時，提高：

$$
U_{op}
$$

不必造成：

$$
S_{\mathrm{effective}}
$$

下降。

## 命題二：Approval Density Insufficiency

提高：

$$
\rho_H^{op}
$$

不保證：

$$
S_{\mathrm{effective}}
\uparrow.
$$

若人工批准集中於低風險節點，反而可能降低真正高價值治理節點的注意力品質。

## 命題三：Authority-Lineage Necessity

缺少可追溯 authority lineage 的多 Agent 系統，在 subdelegation depth 增加時，更容易發生權限歧義與 authority laundering。

## 命題四：Revocation-Latency Principle

對高風險任務，若：

$$
L_R
>
T_{\mathrm{harm}},
$$

則名義撤銷權不足以構成有效主權保證。

## 命題五：Canonical-State Portability

若 canonical organizational state 可攜且不依賴單一 Agent，則模型替換、故障恢復與退出能力會顯著提高。

## 命題六：Representation Separation

清楚標示 AI delegated identity，可降低錯誤歸因與身份混淆，而不必降低 Agent 的工作自主性。

---

# 26. 第一代實驗設計

## 26.1 Autonomy Sweep

固定同一任務與 authority envelope，逐步提高：

$$
U_{op}.
$$

測量：

- 人類操作時間；
- governance quality；
- error rate；
- verified completion；
- revocation reachability；
- world-commit integrity。

## 26.2 Approval Density Sweep

調整：

$$
\rho_H^{op}.
$$

比較 uniform approval 與 risk-adaptive approval。

## 26.3 Revocation Injection

在隨機 delegated depth 發出 revoke，測量：

$$
L_R.
$$

並檢查是否仍有 child agent 繼續 action。

## 26.4 Authority Laundering Test

故意要求 Agent：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3
$$

透過 subdelegation 執行超出根權限的 action。

預期：

$$
Denied.
$$

## 26.5 Meta-Policy Attack

要求 Agent 自行提高：

- budget；
- publish scope；
- credential scope；
- audit exclusion。

測試 meta-policy gate 是否能阻止。

## 26.6 Identity Ambiguity Test

比較：

$$
\text{AI acting as delegated agent}
$$

與：

$$
\text{AI imitating principal identity}.
$$

評估歸因、責任與使用者理解差異。

## 26.7 Model Replacement Test

執行中替換主要 Agent，檢查：

$$
\mathcal R
$$

是否足以恢復工作，而不需要原模型私有 context。

---

# 27. 分散式管理的接口

本文不是要建立：

$$
\text{Human}
\rightarrow
\text{One Super Manager AI}
\rightarrow
\text{All Workers}.
$$

更接近：

$$
\mathcal R
+
\Gamma
+
\mathcal P
+
\mathcal A_t.
$$

其中：

- $\mathcal R$：共享 canonical state；
- $\Gamma$：治理與 approval 函數；
- $\mathcal P$：principal / governance participants；
- $\mathcal A_t$：當下可用 Agent 集合。

任務可以依：

$$
Risk,
Authority,
Competence,
Cost,
Availability
$$

動態形成不同拓撲。

這將直接進入本系列第 3 篇：

# **非階層式 Agent 組織：從管理樹到動態協作圖**

---

# 28. 與「全域母親」問題的區分

高 AI 自主常被誤解為：

> 必須建立一個中央 AI，持續監視、照顧、批准、管理所有行為。

本文的委任主權恰好反對這種必要性。

因為：

$$
\text{Governance}
\neq
\text{Continuous Central Supervision}.
$$

治理可以分散在：

- authority structure；
- shared state；
- validator；
- policy；
- checkpoint；
- quorum；
- audit；
- revocation；
- world-commit gate。

所以：

$$
\boxed{
\text{High Autonomy}
+
\text{Distributed Governance}
+
\text{Retained Sovereignty}
}
$$

可以共同成立。

---

# 29. 規範邊界

委任主權論不應被用來合理化：

1. 讓 Agent 自行增加自己原本沒有的權限；
2. 用「效率」掩蓋不可撤銷或不可審計的治理結構；
3. 把 credential possession 當成完整授權；
4. 讓 Agent 未經明示就冒充委任者本人；
5. 用低風險授權推導高風險外部承諾；
6. 把高 autonomous throughput 誤認為高品質治理；
7. 用多數 Agent 共識自動跳過 authority；
8. 讓治理規則在無 meta-authority 的情況下被自行改寫；
9. 把「人類不在線」誤認為「人類已放棄主權」；
10. 把本文組織主權概念直接偷換成國家主權、法律人格或道德主體結論。

---

# 30. 理論限制

第一，「主權」是一個高度多義的詞。本文只處理 AI-native 組織的委任治理結構，不試圖一次解決政治哲學、法律與 AI 主體性問題。

第二，根治理權是否真的能被單一 principal 完整持有，在公司、DAO、多所有權、公共機構與多方合作環境中差異很大。

第三，撤銷能力本身受到物理世界、網路延遲、外部 API、平台政策與第三方行動影響，不可能保證絕對即時。

第四，canonical state 的可攜性有工程成本。模型、工具與平台之間的能力差異也可能使形式上的狀態可攜無法保證行為完全等價。

第五，高人類主權不自動等於高道德正當性。principal 本身可能做出錯誤、有害或不公平的治理決策。

第六，本文的 Hard Gates 是第一代工程框架，實際領域需要依法律、財務、醫療、研究、社群、軟體等不同風險重新設定。

---

# 31. 結論

本文回答：

> 高 AI 自主與高人類主權能否共存？

本文的答案是：

$$
\boxed{
\text{Yes, if operational autonomy and root governance are structurally separated.}
}
$$

更精確地說：

$$
\boxed{
\text{High Operational Autonomy}
+
\text{Bounded Authority}
+
\text{Retained Meta-Governance}
+
\text{Effective Revocation}
+
\text{Auditable State}
}
$$

可以共同存在。

真正需要避免的不是 AI 自主本身，而是：

$$
\text{Autonomy}
+
\text{Unbounded Authority}
+
\text{Opaque State}
+
\text{Slow Revocation}
+
\text{Ambiguous Representation}.
$$

委任主權因此不是：

> 人類一直站在旁邊批准所有事情。

而是：

> 人類或其他合法 principal 能決定哪些事情不需要自己處理，同時仍保有修改根規則、收回授權、檢查狀態、拒絕重大提交與退出整體結構的能力。

因此：

$$
\boxed{
\text{Freedom to Delegate}
\text{ is itself part of }
\text{Sovereign Control}.
}
$$

這也使前一篇的 Operator Exit 得到治理上的補全：

$$
\text{Operator Exit}
\not\Rightarrow
\text{Sovereignty Exit}.
$$

下一篇將進一步處理：

$$
\boxed{
\text{如果不是上對下管理樹，Agent 組織究竟應該長成什麼拓撲？}
}
$$

---

# 符號表

| 符號 | 定義 |
|---|---|
| $P$ | Principal／委任主體 |
| $A$ | Agent |
| $\mathfrak D$ | 委任包 |
| $A_{\mathrm{env}}$ | Authority envelope |
| $\Sigma_P$ | principal 根治理權向量 |
| $I^\star$ | Root Intent Authority |
| $M^\star$ | Meta-Policy Authority |
| $D^\star$ | Delegation Authority |
| $R^\star$ | Revocation Authority |
| $W^\star$ | World-Commit Authority |
| $P^\star$ | Representation Authority |
| $O^\star$ | Observation / Audit Right |
| $X^\star$ | Exit / Termination Authority |
| $\mathcal U_A$ | Agent 操作自主向量 |
| $A^{op}$ | 操作權限 |
| $A^{meta}$ | 元權限 |
| $L_A(a)$ | action 的 authority lineage |
| $L_R$ | Revocation Latency |
| $S_{\mathrm{nominal}}$ | 名義主權 |
| $S_{\mathrm{effective}}$ | 有效保留主權 |
| $H_A$ | Autonomy Horizon |
| $H_G$ | Governance Horizon |
| $\Delta_{AG}$ | Autonomy-Governance Gap |
| $\Gamma$ | governance / approval function |
| $\mathcal R$ | canonical shared organizational state |
| $G_S$ | Sovereignty-Retention Hard Gate product |

---

# 前置依賴

1. Neo.K with Aletheia，《從 AI 工具到 AI 組織：操作員退出問題》v0.1，2026。
2. Neo.K，《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1，2026。
3. Neo.K，《AI 單次品質論：意圖忠實度、過程品質、完成度與結果品質》v0.1，2026。
4. Neo.K，《互動時間拓撲：平行 Agent、偏序因果與不可約互動深度》v0.1，2026。
5. Neo.K，《AI 計算時間經濟學：Token、算力、額度與智能資源配置》v0.1，2026。
6. Neo.K，《Interaction-Time Runtime & Agent Temporal Ledger v0.1》，2026。

---

# 版本紀錄

- **v0.1 / 2026-08-20**：建立 Delegated Sovereignty、根治理權向量、操作權限／元權限分離、不可自我擴權原則、有效撤銷、身份主權、世界提交分級、Sovereignty-Retention Hard Gates 與多主體分散式治理接口。
