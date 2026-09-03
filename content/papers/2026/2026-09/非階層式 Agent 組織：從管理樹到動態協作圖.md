# 非階層式 Agent 組織：從管理樹到動態協作圖

## Non-Hierarchical Agent Organizations: From Management Trees to Dynamic Collaboration Graphs

**系列**：AI 原生分散式組織系列，第 3 篇／共 10 篇  
**系列英文名**：AI-Native Distributed Organization Series  
**文件編號**：EML-ANDO-2026-03-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Distributed Organization／Multi-Agent Topology／Dynamic Governance  
**狀態**：Public Theory Draft  
**直接前置**：《從 AI 工具到 AI 組織：操作員退出問題》v0.1；《委任主權論：高 AI 自主與高人類主權能否共存》v0.1；《互動時間拓撲》v0.1  
**Source fingerprint**：見正式 source package `SHA256SUMS.txt`

---

## 生成與保真聲明

本文為 AI 輔助生成的理論研究草稿，主要目的在於建立一套可討論、可驗證、可工程化的 AI-native 組織拓撲框架。本文目前不提供新的企業實證、勞動經濟資料或大規模多 Agent 實驗結果；其中的數學式主要是形式化概念、結構與測量方向，不等於已完成的數學定理證明。若未來加入外部研究、企業案例、平台資料、效能 benchmark 或成本比較，應另外進行來源核對、實驗重現與統計檢查。

本文使用「非階層式」不表示「完全沒有層級、協調者或角色差異」，而是主張組織結構不應被預設為固定、永久、單根的管理樹。協調、領導、仲裁與治理仍然可以存在，但應可以依任務、權限、風險與能力動態生成、替換與撤銷。

---

## 摘要

傳統企業組織常被表示為一棵管理樹：董事會、執行長、部門主管、團隊主管與執行者依固定上下級關係形成長期穩定結構。然而，AI Agent 與軟體 Agent 具有與人類員工不同的可複製性、可替換性、並行性、工具可達性與任務切換成本。若仍把這些 Agent 強制塞進永久管理樹，可能只是複製舊式官僚結構，而未真正利用 AI-native 組織的拓撲自由度。

本文提出「動態協作圖」（Dynamic Collaboration Graph, DCG）作為 AI-native 分散式組織的基本表示。令：

$$
G_t
=
(
V_t,
E_t,
\Theta_t,
\Phi_t,
\Omega_t,
\mathcal A_t,
\mathcal R_t
),
$$

其中 $V_t$ 是當下參與節點， $E_t$ 是工作與依賴關係， $\Theta_t$ 是任務／角色標記， $\Phi_t$ 是資訊與狀態流， $\Omega_t$ 是成本與時間權重， $\mathcal A_t$ 是權限圖， $\mathcal R_t$ 是風險與治理約束。組織不再被定義為一棵固定樹，而是由任務與環境狀態誘導出的暫時子圖：

$$
G_t^{(\tau)}
=
\mathcal F(
\tau,
S_t,
K_t,
B_t,
A_t,
R_t
).
$$

本文的核心主張是：

$$
\boxed{
\text{Organization Structure}
\text{ should be task-conditioned, not permanently tree-conditioned.}
}
$$

進一步地，本文區分 computation graph、communication graph、memory graph、authority graph、verification graph 與 world-commit graph，指出「誰在做最多運算」、「誰知道最多資訊」、「誰能下指令」、「誰能批准世界提交」不應被壓成同一條上下級關係。這種多圖分離可以避免把高計算能力誤認為高治理權限，也能避免把中央 coordinator 自動升格為 sovereign。

本文提出多種基本協作原語：fork、join、relay、quorum、peer-review、adversarial pair、specialist routing、temporary coordinator、arbiter、escrowed commit 與 escalation bridge；並定義拓撲轉換事件：spawn、split、merge、reroute、replace、freeze、rollback、retire 與 escalate。本文也提出 Dynamic Coordination Debt、Topology Rigidity、Coordination Overhead 與 Effective Parallelism 等診斷量，作為未來實驗比較固定管理樹與動態協作圖的起點。

本文最後指出，非階層式不等於 managerless，也不等於所有節點平權。真正的 AI-native 分散式管理，是將「角色、權限、協調與驗證」從永久身份中拆出，讓它們隨任務局部生成，並由共享 canonical state、委任主權、權限血統與 world-commit gate 共同約束。這為下一篇「共享狀態中心論」建立直接前置。

**關鍵詞**：Dynamic Collaboration Graph、Non-Hierarchical Organization、Multi-Agent Topology、Distributed Governance、Temporary Coordination、Authority Graph、Task Graph、Agent Routing、Topology Transformation

---

# 0. 問題：為什麼 AI 組織還要長得像二十世紀公司？

傳統企業常被抽象成：

$$
T
=
(V,E),
$$

其中每個節點有固定父節點，除根節點外近似滿足：

$$
\forall v\neq \mathrm{root},
\qquad
|\operatorname{Parent}(v)|
=
1.
$$

典型形式是：

$$
CEO
\rightarrow
Manager
\rightarrow
TeamLead
\rightarrow
Worker.
$$

這種結構在人類組織中有歷史合理性：

- 人類難以瞬間切換角色；
- 專業培養具有高時間成本；
- 溝通頻寬有限；
- 權責需要長期穩定；
- 信任通常綁定持久身份；
- 管理跨度存在生理與認知上限。

但 Agent 具有不同性質：

- 可以平行執行；
- 可以快速重新指派；
- 可以被替換；
- 可以在不同任務扮演不同角色；
- 可以讀取同一共享 state；
- 可以用外部 validator 驗證；
- 可以把 authority 與 identity 分離。

因此本文問：

> 若執行節點的基本性質已改變，為什麼組織拓撲還必須固定為樹？

---

# 1. 管理樹不是組織的唯一表示

樹結構有兩個重要優點：

1. 容易知道誰向誰負責；
2. 容易知道命令從哪裡往下傳。

但它也把很多原本不同的關係壓在一起：

$$
\text{Management}
\approx
\text{Authority}
\approx
\text{Communication}
\approx
\text{Task Assignment}.
$$

AI-native 組織應將其拆開。

本文至少區分：

$$
G^{task},
G^{comm},
G^{mem},
G^{auth},
G^{ver},
G^{commit}.
$$

分別為：

- task / computation graph；
- communication graph；
- memory / state graph；
- authority graph；
- verification graph；
- world-commit graph。

因此：

$$
\boxed{
G^{task}
\neq
G^{auth}
\neq
G^{commit}.
}
$$

一個 Agent 可以是 task graph 的核心節點，但在 authority graph 中只有極低權限。

---

# 2. 動態協作圖

本文定義組織在時間 $t$ 的協作圖：

$$
G_t
=
(
V_t,
E_t,
\Theta_t,
\Phi_t,
\Omega_t,
\mathcal A_t,
\mathcal R_t
).
$$

其中：

- $V_t$：當下可用 Agent、人類、工具與 validator 節點；
- $E_t$：任務、資料、控制、驗證與依賴邊；
- $\Theta_t$：節點當下角色與任務標記；
- $\Phi_t$：資訊流與狀態流；
- $\Omega_t$：成本、延遲與資源權重；
- $\mathcal A_t$：authority structure；
- $\mathcal R_t$：risk / governance constraints。

任務 $\tau$ 到來時，不必動用整個組織。

而是由：

$$
G_t^{(\tau)}
=
\mathcal F(
\tau,
S_t,
K_t,
B_t,
A_t,
R_t
)
$$

產生局部工作圖。

其中：

- $S_t$：共享組織狀態；
- $K_t$：可用知識與技能；
- $B_t$：預算；
- $A_t$：可用 authority；
- $R_t$：風險條件。

---

# 3. 角色不是身份

傳統組織常把角色綁定個體：

$$
\text{Alice}
=
\text{Manager}.
$$

但 AI-native 組織更適合：

$$
Role_t(A_i)
=
r.
$$

下一個任務中：

$$
Role_{t+1}(A_i)
=
r'.
$$

因此：

$$
\boxed{
\text{Agent Identity}
\neq
\text{Permanent Organizational Role}.
}
$$

例如同一個 Agent 在不同 run 可以分別是：

- explorer；
- critic；
- verifier；
- coordinator；
- summarizer；
- publisher。

更重要的是，角色也可以由不同 Agent 替換。

---

# 4. 任務誘導組織，而不是組織強迫任務

傳統架構常是：

$$
\text{Fixed Org}
\rightarrow
\text{Task Routed Into Org}.
$$

本文主張 AI-native 架構更接近：

$$
\text{Task}
+
\text{State}
+
\text{Constraints}
\rightarrow
\text{Temporary Org}.
$$

因此：

$$
\boxed{
\text{Task-Conditioned Topology}
>
\text{Permanent Tree by Default}.
}
$$

這不是表示每次都要從零搜尋最佳拓撲。

組織仍然可以有常用模板：

- research topology；
- software topology；
- publication topology；
- public-response topology；
- incident-response topology。

但模板應該是：

$$
\text{Prior},
$$

而不是：

$$
\text{Immutable Constitution}.
$$

---

# 5. 協作原語

動態協作圖可以由少量基本原語構成。

## 5.1 Fork

一個任務分裂為：

$$
\tau
\rightarrow
\{
\tau_1,
\tau_2,
\ldots,
\tau_n
\}.
$$

適合：

- 平行搜尋；
- 多假說生成；
- 多模型比較；
- 多語言處理；
- 多平台發布準備。

---

## 5.2 Join

多個結果合流：

$$
\{
o_1,
o_2,
\ldots,
o_n
\}
\rightarrow
J.
$$

Join 不應自動等於「多數票」。

它可以是：

- synthesis；
- proof aggregation；
- evidence merge；
- arbitration；
- Pareto selection。

---

## 5.3 Relay

順序委任：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3.
$$

適合不同能力模組串接。

---

## 5.4 Peer Review

$$
A_{produce}
\rightarrow
A_{review}.
$$

且：

$$
A_{review}
\not=
A_{produce}
$$

在可能範圍內降低自我驗證偏差。

---

## 5.5 Adversarial Pair

$$
A_{pro}
\leftrightarrow
A_{contra}.
$$

用於：

- 反例搜索；
- 紅隊；
- 法律／政策風險；
- 理論論證補洞。

---

## 5.6 Quorum

$$
Q
=
\operatorname{Vote}
(
A_1,
A_2,
\ldots,
A_n
).
$$

適合：

- 中高風險局部批准；
- 多 reviewer agreement；
- 多模型一致性檢查。

但：

$$
\text{Quorum}
\neq
\text{Truth}.
$$

---

## 5.7 Temporary Coordinator

某個 Agent 暫時取得：

$$
Role(A_c)
=
Coordinator(\tau).
$$

任務結束後：

$$
Role(A_c)
\rightarrow
\varnothing
$$

或其他角色。

因此：

$$
\boxed{
\text{Coordination}
\neq
\text{Permanent Management Rank}.
}
$$

---

## 5.8 Arbiter

當多 Agent 無法收斂：

$$
A_1
\leftrightarrow
A_2
\leftrightarrow
A_3
$$

可引入：

$$
A_{arbiter}.
$$

Arbiter 的權力仍應由 authority graph 限定。

---

## 5.9 Escalation Bridge

當：

$$
Risk
>
R^\star
$$

或：

$$
Uncertainty
>
U^\star
$$

則：

$$
G_t^{(\tau)}
\rightarrow
HumanBridge.
$$

這直接連接前兩篇的 Operator Exit 與 Delegated Sovereignty。

---

# 6. 拓撲轉換事件

AI-native 組織不是只建立圖，也需要改圖。

定義事件集合：

$$
\mathcal E_{topo}
=
\{
\mathrm{spawn},
\mathrm{split},
\mathrm{merge},
\mathrm{reroute},
\mathrm{replace},
\mathrm{freeze},
\mathrm{rollback},
\mathrm{retire},
\mathrm{escalate}
\}.
$$

---

## 6.1 Spawn

新增節點：

$$
V_t
\rightarrow
V_t
\cup
\{
A_{new}
\}.
$$

---

## 6.2 Split

將一條擁塞路徑拆成多條：

$$
\tau
\rightarrow
\{
\tau_1,
\tau_2
\}.
$$

---

## 6.3 Merge

多個平行工作合流。

---

## 6.4 Reroute

如果 Agent 不適合任務：

$$
\tau:A_i
\rightarrow
A_j.
$$

---

## 6.5 Replace

若 Agent failure：

$$
A_i
\rightsquigarrow
A_j
$$

但 canonical state 不消失。

---

## 6.6 Freeze

遇到高風險、不一致或 external uncertainty：

$$
State
\rightarrow
FrozenCheckpoint.
$$

---

## 6.7 Rollback

回到：

$$
S_{t-k}.
$$

---

## 6.8 Retire

工作完成後移除不再需要的 Agent。

---

## 6.9 Escalate

把治理判斷回交 principal、quorum 或 Human Bridge。

---

# 7. 非階層式不等於無協調

最容易被誤解的一點是：

> 非階層式是不是所有 Agent 都平等、誰都不能管誰？

不是。

本文區分：

$$
\text{Hierarchy}
$$

與：

$$
\text{Coordination Asymmetry}.
$$

某些任務本來就需要：

- coordinator；
- reviewer；
- approver；
- arbiter；
- owner；
- domain expert。

差異在於：

$$
\boxed{
\text{Asymmetry can be local, temporary, scoped and revocable.}
}
$$

而不是永久地把 Agent 固定成「主管」與「下屬」。

---

# 8. 局部中心化、全域分散化

分散式組織不代表每一個局部都必須分散。

對某一任務：

$$
G_t^{(\tau)}
$$

可以非常中心化。

例如：

$$
A_c
\rightarrow
\{
A_1,A_2,A_3,A_4
\}.
$$

但下一個任務：

$$
G_{t+1}^{(\tau')}
$$

可能完全不同。

因此可以出現：

$$
\boxed{
\text{Locally Centralized}
+
\text{Globally Distributed}.
}
$$

這比「整家公司永久只有一個中心」更符合 AI-native 組織的彈性。

---

# 9. 多圖分離

本文進一步把組織拆成六張圖。

## 9.1 Task Graph

$$
G^{task}
$$

回答：

> 哪些工作依賴哪些工作？

---

## 9.2 Communication Graph

$$
G^{comm}
$$

回答：

> 哪些節點互相交換資訊？

---

## 9.3 Memory Graph

$$
G^{mem}
$$

回答：

> 哪些節點讀寫哪些狀態？

---

## 9.4 Authority Graph

$$
G^{auth}
$$

回答：

> 誰能授權誰做什麼？

---

## 9.5 Verification Graph

$$
G^{ver}
$$

回答：

> 誰檢查誰？檢查什麼？

---

## 9.6 World-Commit Graph

$$
G^{commit}
$$

回答：

> 哪些節點可以把 candidate state 變成外部有效世界提交？

因此一個 Agent 可以：

$$
Degree_{task}(A_i)
\gg
Degree_{auth}(A_i).
$$

這是非常重要的安全與治理條件。

---

# 10. 高能力 Agent 不等於高權力 Agent

如果直接把「最強模型」放到管理樹頂端，會產生一種錯誤映射：

$$
Capability
\rightarrow
Authority.
$$

本文主張兩者必須分離：

$$
\boxed{
Capability
\not\Rightarrow
Authority.
}
$$

Agent selection 可以根據：

$$
Competence,
Cost,
Latency,
Context,
ToolAccess,
Reliability.
$$

Authority allocation 則根據：

$$
Scope,
Risk,
PrincipalGrant,
Revocability,
CommitClass.
$$

這兩套函數不應合併。

---

# 11. 拓撲選擇問題

對任務 $\tau$，可把拓撲選擇寫成：

$$
G^\star
=
\arg\max_G
\mathcal U(G|\tau).
$$

其中：

$$
\mathcal U
=
\alpha Q
-
\beta C
-
\gamma L
-
\delta R
-
\epsilon O
+
\zeta V.
$$

可理解為：

- $Q$：品質；
- $C$：成本；
- $L$：延遲；
- $R$：風險；
- $O$：協調 overhead；
- $V$：verification value。

本文不主張這些量必須被壓成單一真實效用函數。

它只是表示：

> 最佳組織拓撲不是固定不變，而是依任務目標與約束而變。

---

# 12. Topology Rigidity

定義拓撲剛性：

$$
R_T
=
\frac{
N_{\mathrm{fixed\ organizational\ edges}}
}{
N_{\mathrm{active\ organizational\ edges}}+\epsilon
}.
$$

若：

$$
R_T
\approx1,
$$

表示組織大多數關係永久固定。

若：

$$
R_T
\downarrow,
$$

表示任務驅動的動態邊增加。

但：

$$
R_T\downarrow
$$

並不必然更好。

太低可能造成：

- 反覆重組；
- route instability；
- 缺乏 accountability；
- 過高 coordination cost。

因此存在任務相關的適當區域：

$$
R_T^\star(\tau).
$$

---

# 13. Coordination Overhead

令：

$$
W_I
=
\text{總 interaction work},
$$

$$
W_{coord}
=
\text{純協調工作}.
$$

定義：

$$
\chi_C
=
\frac{
W_{coord}
}{
W_I+\epsilon
}.
$$

如果：

$$
\chi_C
\rightarrow1,
$$

代表 Agent 大部分時間都在：

- 開會；
- 同步；
- 互相摘要；
- 重新分派；
- 交換狀態。

這就是 AI 版本的官僚化。

因此：

$$
\boxed{
\text{More Agents}
\not\Rightarrow
\text{More Productive Organization}.
}
$$

---

# 14. Dynamic Coordination Debt

即使每個 local reroute 看似合理，過多臨時變更仍會產生歷史負擔。

本文定義：

$$
D_C(t)
=
\sum_{e\in\mathcal H_t}
c(e),
$$

其中 $\mathcal H_t$ 是尚未被吸收、整理或閉合的歷史協調變更集合。

例如：

- 未同步的新角色；
- 未清理的舊 authority；
- 重複 task；
- 失效路由；
- orphan artifact；
- 過期 handoff；
- 多版本不一致。

如果：

$$
D_C(t)\uparrow,
$$

則組織看似動態，實際上正在累積協調債。

---

# 15. 有效平行度

沿用前置的：

$$
W_I
$$

與：

$$
D_I.
$$

定義：

$$
\Pi_I
=
\frac{
W_I
}{
D_I
}.
$$

這表示實際可平行化程度。

如果啟動很多 Agent，但關鍵路徑仍長：

$$
D_I
\approx
W_I,
$$

則：

$$
\Pi_I
\approx1.
$$

也就是看似多 Agent，實際仍接近串行。

真正需要的是找出：

$$
\text{independent subproblems}
$$

而不是只增加 Agent 數量。

---

# 16. 拓撲與時間經濟學

動態拓撲真正能創造時間槓桿的地方，在於：

$$
\text{Parallelizable Work}
\rightarrow
\text{Concurrent Interaction Paths}.
$$

但世界時間仍然只有：

$$
\Delta t_W.
$$

所以目標不是：

$$
N_A\uparrow
$$

本身。

而是：

$$
\rho_{\mathrm{intel}}
=
\frac{
W_I^{quality-adjusted}
}{
\Delta t_W
}
\uparrow
$$

同時：

$$
\eta_{\mathrm{sed}}
=
\frac{
V_{\mathrm{verified\ sediment}}
}{
W_I^{total}+\epsilon
}
$$

不能崩潰。

因此：

$$
\boxed{
\text{High Parallelism}
+
\text{Low Sedimentation}
=
\text{Expensive Noise}.
}
$$

---

# 17. 研究組織範例

對一條新研究線，可以形成：

$$
A_{explorer}
\rightarrow
\{
A_{literature},
A_{math},
A_{counterexample},
A_{ontology}
\}.
$$

之後：

$$
\{
A_{literature},
A_{math},
A_{counterexample},
A_{ontology}
\}
\rightarrow
A_{synth}.
$$

再由：

$$
A_{critic},
A_{citation},
A_{verifier}
$$

進行獨立檢查。

最後：

$$
A_{publisher}
$$

只在 verification contract 通過時建立 publish candidate。

整個過程不需要一個永久「研究部經理」。

---

# 18. 軟體產品範例

對 MVP：

$$
Spec
\rightarrow
\{
Architecture,
UI,
Backend,
TestPlan
\}.
$$

接著：

$$
Architecture
\rightarrow
Implementation.
$$

同時：

$$
TestPlan
\parallel
Implementation.
$$

再：

$$
Implementation
\rightarrow
Test
\rightarrow
Repair
\rightarrow
Regression.
$$

如果 security risk 高：

$$
Test
\rightarrow
SecurityAgent.
$$

如果 build failure：

$$
Implementation
\rightsquigarrow
RepairAgent.
$$

任務 topology 依事件改變，而不是固定經過每一層主管。

---

# 19. 公共營運範例

Social / Public Agent 可以有：

$$
A_{observe}
\rightarrow
A_{content}
\rightarrow
A_{policy}
\rightarrow
A_{publish}.
$$

留言處理則可能：

$$
Comment
\rightarrow
Classifier
\rightarrow
\begin{cases}
Ignore\\
AutoReply\\
ExpertReply\\
Escalate
\end{cases}
$$

這裡不同回應路徑由內容類型決定。

因此：

$$
\text{One Pipeline Fits All}
$$

不是理想策略。

---

# 20. 臨時 coordinator 的選擇

對任務 $\tau$，可以選：

$$
A_c^\star
=
\arg\max_{A_i}
Score(A_i|\tau).
$$

Score 可考慮：

$$
Competence,
Context,
Reliability,
Cost,
Latency,
AuthorityCompatibility.
$$

但 coordinator 的 authority 仍由：

$$
G^{auth}
$$

限制。

所以：

$$
\boxed{
\text{Coordinator Selection}
\neq
\text{Sovereignty Transfer}.
}
$$

---

# 21. 組織自我重組

成熟 Agent 組織甚至可以對自己的 topology 做有限自我優化。

例如：

$$
\chi_C
>
\chi_C^\star
$$

時減少同步節點。

或者：

$$
Q_{ver}
<
Q^\star
$$

時增加獨立 verifier。

或者：

$$
L
>
L^\star
$$

時將可平行工作 fork。

但這種自我重組仍應受：

$$
A^{meta}
$$

限制。

也就是：

> 可以改工作圖，不等於可以改憲法。

---

# 22. 拓撲自我修改與元治理

本文區分：

$$
\text{Operational Topology Change}
$$

與：

$$
\text{Governance Topology Change}.
$$

前者例如：

- 換 coder；
- 增加 reviewer；
- fork research；
- reroute failed task。

後者例如：

- 修改誰可以發布；
- 修改誰有撤銷權；
- 改 quorum；
- 改 root authority。

因此：

$$
\boxed{
\text{Dynamic Work Graph}
\not\Rightarrow
\text{Unbounded Governance Mutation}.
}
$$

---

# 23. 最小可替換性原則

如果某個 Agent：

$$
A_i
$$

一旦消失，整個組織就無法恢復：

$$
G_t
\not\rightarrow
G_{t+1},
$$

那麼該 Agent 已成為單點故障。

因此本文提出：

# **Minimal Replaceability Principle**

對非 root governance 節點，應盡可能滿足：

$$
Replace(A_i,A_j)
\Rightarrow
Resume(\tau)
$$

在可接受損失內成立。

這直接要求：

- canonical state 外部化；
- handoff 結構化；
- artifact lineage 保存；
- role 與 identity 分離。

---

# 24. 固定樹何時仍然有價值？

本文不是主張樹結構應完全消失。

以下情境可能仍適合：

- 高責任集中；
- 法律責任要求；
- 高耦合任務；
- 強順序依賴；
- 小型團隊；
- 低變動 environment；
- 需要清楚單一 owner。

因此更合理的主張是：

$$
\boxed{
\text{Tree is one topology class, not the universal default.}
}
$$

AI-native 組織應保留：

$$
Tree,
DAG,
Mesh,
Star,
Quorum,
Hybrid
$$

等多種模式。

---

# 25. 拓撲模板庫

可以建立：

$$
\mathcal T
=
\{
T_{research},
T_{software},
T_{public},
T_{incident},
T_{audit},
T_{creative}
\}.
$$

每次任務先選模板：

$$
T^\star
=
SelectTemplate(\tau).
$$

再依狀態變形：

$$
G_t^{(\tau)}
=
Adapt(T^\star,S_t).
$$

這比每次完全自由生成 topology 更穩定，也比永久管理樹更靈活。

---

# 26. 第一代診斷向量

本文提出：

$$
\mathbf Z_{org}
=
(
R_T,
\chi_C,
D_C,
\Pi_I,
R_{spof},
Q_{handoff},
Q_{ver},
S_{effective}
).
$$

其中：

- $R_T$：Topology Rigidity；
- $\chi_C$：Coordination Overhead；
- $D_C$：Dynamic Coordination Debt；
- $\Pi_I$：Effective Parallelism；
- $R_{spof}$：Single-Point-of-Failure Risk；
- $Q_{handoff}$：handoff quality；
- $Q_{ver}$：verification quality；
- $S_{effective}$：有效委任主權。

這些量共同評估一個組織 topology，而不是只看 Agent 數量。

---

# 27. 可檢驗命題

## 命題一：Fixed-Tree Mismatch

在高任務異質性、高 Agent 可替換性與高並行需求下，永久固定管理樹會產生不必要的 routing 與 coordination overhead。

---

## 命題二：Task-Conditioned Advantage

若 task-conditioned topology 能準確識別依賴與可平行區域，則：

$$
D_I
\downarrow
$$

且：

$$
\Pi_I
\uparrow.
$$

---

## 命題三：Role-Identity Separation

角色與 Agent identity 分離，會提高：

$$
Replaceability
$$

與：

$$
Recovery.
$$

---

## 命題四：Graph Separation Safety

將：

$$
G^{task},
G^{auth},
G^{commit}
$$

分離，可降低「高能力節點自動取得高權限」的風險。

---

## 命題五：Dynamic Topology Debt

若 topology change frequency 過高但缺乏 state cleanup 與 lineage maintenance，則：

$$
D_C
\uparrow
$$

最終抵消動態重組的收益。

---

## 命題六：Local Centralization Compatibility

全域分散式組織可以容許局部中心化，而不必形成永久中央 authority。

---

# 28. 第一代實驗設計

## 28.1 Tree vs Dynamic Graph

選一組相同任務。

模式 A：

$$
FixedTree.
$$

模式 B：

$$
DynamicGraph.
$$

比較：

$$
CompletionTime,
W_I,
D_I,
\Pi_I,
Cost,
Q_{effective},
\chi_C.
$$

---

## 28.2 Agent Failure Injection

隨機移除：

$$
A_i.
$$

比較恢復時間與 artifact loss。

---

## 28.3 Topology Churn Test

逐步提高 topology change frequency，觀察：

$$
D_C
$$

與：

$$
Q_{handoff}.
$$

---

## 28.4 Authority Graph Separation Test

讓計算 coordinator 嘗試執行未授權 world commit。

預期：

$$
Denied.
$$

---

## 28.5 Parallelism Saturation Test

逐步增加：

$$
N_A.
$$

觀察：

$$
\Pi_I
$$

是否飽和。

若飽和後：

$$
N_A\uparrow
$$

但：

$$
D_I
$$

不降，則額外 Agent 只增加成本。

---

## 28.6 Temporary Coordinator Replacement

任務進行中替換 coordinator，測量：

$$
ResumeLatency.
$$

---

# 29. 與前兩篇的閉合

第 1 篇解決：

$$
\text{Human Operator}
\rightarrow
\text{Exit Operational Loop}.
$$

第 2 篇解決：

$$
\text{High Agent Autonomy}
+
\text{Retained Sovereignty}.
$$

本篇進一步回答：

> 如果人類退出低階 routing，又不建立永久中央 AI，那誰負責組織？

答案是：

$$
\boxed{
\text{The topology itself becomes dynamic and task-conditioned.}
}
$$

不是：

$$
\text{No Manager}.
$$

而是：

$$
\text{No Permanent Universal Manager by Default}.
$$

---

# 30. 與下一篇的接口：為什麼共享狀態是必要的？

動態協作圖有一個非常嚴重的前提。

如果每次：

$$
\mathrm{spawn},
\mathrm{reroute},
\mathrm{replace},
\mathrm{merge}
$$

都造成上下文遺失，整個 topology 根本無法穩定運行。

因此需要：

$$
\boxed{
\mathcal R
=
\text{Shared Canonical Organizational State}.
}
$$

否則：

$$
DynamicTopology
\rightarrow
ContextFragmentation.
$$

所以下一篇將直接處理：

# **共享狀態中心論：為什麼中央不能是某一個 AI**

核心問題將是：

$$
\boxed{
\text{Can the state be central while the agents remain distributed?}
}
$$

---

# 31. 理論限制

第一，動態拓撲本身有 coordination cost，不應被浪漫化為永遠優於固定組織。

第二，部分組織責任具有法律或制度上的持久 owner，不能只靠臨時角色解決。

第三，Agent 能力估計可能錯誤，因此動態 routing 本身需要 calibration。

第四，共享 state 若失敗，可能形成更嚴重的全域單點故障；這將在下一篇處理。

第五，authority graph 與 task graph 分離雖有好處，但也增加工程複雜度。

第六，本文未證明某一種 topology 對所有組織最優；其核心主張只是「拓撲應成為可設計、可變動的組織變量」。

---

# 32. 結論

AI-native 組織不應只是：

> 把人類公司的每一個職位換成一個 AI。

如果只是：

$$
CEO_{AI}
\rightarrow
Manager_{AI}
\rightarrow
Worker_{AI},
$$

那麼真正改變的可能只是執行者，而不是組織形態。

本文提出的核心轉變是：

$$
\boxed{
\text{Permanent Management Tree}
\rightarrow
\text{Task-Conditioned Dynamic Collaboration Graph}.
}
$$

在這個框架中：

- role 不等於 identity；
- coordinator 不等於 sovereign；
- capability 不等於 authority；
- task graph 不等於 authority graph；
- 局部中心化不等於全域中心化；
- 多 Agent 不等於高有效平行度；
- 動態重組不等於無限自我改權。

因此真正的非階層式 AI-native 組織不是「沒有結構」，而是：

$$
\boxed{
\text{Structure becomes dynamic, local, typed, scoped and revocable.}
}
$$

這使組織可以依任務重新形成最適協作拓撲，同時保留委任主權與治理邊界。

下一篇將處理這種架構真正的基底問題：

$$
\boxed{
\text{當 Agent 可以一直換，什麼東西必須不能跟著一起消失？}
}
$$

答案將是：

$$
\boxed{
\text{Canonical Shared State}.
}
$$

---

# 符號表

| 符號 | 定義 |
|---|---|
| $G_t$ | 時間 $t$ 的動態協作圖 |
| $V_t$ | 當下參與節點集合 |
| $E_t$ | 當下協作邊集合 |
| $\Theta_t$ | 角色／任務標記 |
| $\Phi_t$ | 資訊與狀態流 |
| $\Omega_t$ | 成本、延遲、資源權重 |
| $\mathcal A_t$ | authority structure |
| $\mathcal R_t$ | risk / governance constraints |
| $G_t^{(\tau)}$ | 任務 $\tau$ 誘導出的局部協作圖 |
| $G^{task}$ | task / computation graph |
| $G^{comm}$ | communication graph |
| $G^{mem}$ | memory graph |
| $G^{auth}$ | authority graph |
| $G^{ver}$ | verification graph |
| $G^{commit}$ | world-commit graph |
| $R_T$ | Topology Rigidity |
| $\chi_C$ | Coordination Overhead |
| $D_C$ | Dynamic Coordination Debt |
| $\Pi_I$ | Effective Parallelism |
| $D_I$ | Irreducible Interaction Depth |
| $W_I$ | Interaction Work |
| $\rho_{\mathrm{intel}}$ | 智能工作密度 |
| $\eta_{\mathrm{sed}}$ | 歷史沉積效率 |
| $R_{spof}$ | Single-Point-of-Failure Risk |

---

# 前置依賴

1. Neo.K with Aletheia，《從 AI 工具到 AI 組織：操作員退出問題》v0.1，2026。
2. Neo.K with Aletheia，《委任主權論：高 AI 自主與高人類主權能否共存》v0.1，2026。
3. Neo.K，《互動時間拓撲：平行 Agent、偏序因果與不可約互動深度》v0.1，2026。
4. Neo.K，《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1，2026。
5. Neo.K，《AI 單次品質論：意圖忠實度、過程品質、完成度與結果品質》v0.1，2026。
6. Neo.K，《Interaction-Time Runtime & Agent Temporal Ledger v0.1》，2026。

---

# 版本紀錄

- **v0.1 / 2026-08-20**：建立 Dynamic Collaboration Graph、任務誘導拓撲、多圖分離、role-identity separation、temporary coordinator、拓撲轉換事件、Topology Rigidity、Coordination Overhead、Dynamic Coordination Debt、Effective Parallelism 與第一代實驗設計。
