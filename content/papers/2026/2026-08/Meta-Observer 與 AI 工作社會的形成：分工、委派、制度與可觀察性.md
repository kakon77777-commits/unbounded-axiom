# Series C / Paper 07
# Meta-Observer 與 AI 工作社會的形成：分工、委派、制度與可觀察性
## The Meta-Observer and the Emergence of AI Work Societies: Division of Labor, Delegation, Institutions, and Observability

版本：v0.1  
日期：2026-08-14  
狀態：Theory + organizational-observability + executable structural checker paper

## 摘要

當人類逐步從「逐一與每個 AI 對話」轉為「設定目標、邊界與資源，觀察多個 Agent 彼此委派、審查、修正、分工與形成規範」時，研究單位開始由單一模型轉向多 Agent 組織。本文將這種功能層級的結構稱為 **AI Work Society（AI 工作社會）**。此名稱僅指可持續的工作組織與制度結構，不預設 AI 具有與人類相同的主體性、社會身份或政治地位。

本文定義一個時間變動的工作社會：

$$
\mathfrak S_t
=
(
\mathcal A_t,
\mathcal R_t,
\mu_t,
G_t^{\mathrm{comm}},
G_t^{\mathrm{del}},
\Pi_t,
\mathcal M_t,
\mathcal I_t,
\mathcal X_t
),
$$

其中 $\mathcal A_t$ 是 agents， $\mathcal R_t$ 是角色集合， $\mu_t$ 是 agent–role assignment， $G_t^{\mathrm{comm}}$ 是 communication graph， $G_t^{\mathrm{del}}$ 是 delegation graph， $\Pi_t$ 是 coordination / collaboration protocol， $\mathcal M_t$ 是共享與局部記憶， $\mathcal I_t$ 是制度與治理規則， $\mathcal X_t$ 是 provenance / execution trace。

本文提出「工作社會」至少需要三類超越單純多 Agent 並置的結構：

1. **Persistent division of labor**：角色或技能分化能跨 episode 持續；
2. **Traceable delegation**：工作與責任可沿 parent–child delegation relation 回溯；
3. **Institutional persistence**：部分規則、權限與 coordination logic 能跨成員替換而保持組織功能。

本文證明四個基礎結果。

第一，**Attribution Non-Identifiability Theorem**：若 observation log 只保留 action / result，而不保留 actor identity、delegation context 或 provenance，且兩個不同因果 assignment 可產生相同 log，則任何只依賴該 log 的 meta-observer 都無法唯一識別責任來源。

第二，**Delegation-Forest Reconstruction Theorem**：若每一 execution event 都具有唯一 event id、root delegation id、唯一 parent id，且 parent relation 無環且 parent 必早於 child，則完整 delegation forest 可由 trace 唯一重建。

第三，**Role-Preserving Institutional Invariance Proposition**：若組織 protocol 與 governance 只依賴 role 而不依賴特定 agent identity，且被替換 agents 在對應 role 上具有相同 role-conditioned transition kernel，則任意 role-preserving member substitution 不改變 organization-level trajectory distribution。這使「制度」在形式上可與「成員」部分分離。

第四，**Topology-Dependent Collective Behavior Proposition**：若至少一個 Agent 的 action policy 依賴可達 message，而 communication topology 改變 message reachability，則即使所有 individual model policies 不變，collective outcome distribution 仍可能改變。因此多 Agent 組織不能一般地被還原成 agent capability 的簡單加總。

2026 年公開研究已明顯朝組織科學方向移動。OrgAgent 將 multi-agent collaboration 拆為 governance、execution、compliance 三層；另一項 25,000-task 實驗則顯示，在足夠強模型上，未預先指定角色的 agents 可自發形成專門角色、abstention 與淺層 hierarchy，且混合式 self-organization 在該研究設定中優於集中式 coordination。IMACS 進一步將「誰在團隊、如何協調、使用哪一種 collaboration algorithm」拆成獨立可交換層。Intelligent AI Delegation 將 dynamic assessment、adaptive execution、structural transparency 與 systemic resilience 視為 delegation 的核心要求。Observability for Delegated Execution 則直接把 durable delegated authority 視為傳統 audit log 的結構缺口，提出 delegation-aware execution graph。Clarus 更將 projects、agents、resources、tasks、artifacts、credit 與 provenance 統一進研究協作基礎設施。

因此本文的核心命題不是：

$$
\boxed{
\text{many agents}
=
\text{society}.
}
$$

而是：

$$
\boxed{
\text{persistent specialization}
+
\text{delegation}
+
\text{coordination}
+
\text{institution}
+
\text{memory}
+
\text{provenance}
+
\text{meta-observability}
\Rightarrow
\text{a functional AI work society can become a meaningful systems-level object}.
}
$$

**關鍵詞：** meta-observer；AI work society；multi-agent organization；delegation；division of labor；institution；provenance；observability；organizational memory；governance

---

## 1. 從 Participant-Observer 到 Meta-Observer

傳統人機研究的典型觀察位置是：

$$
U
\leftrightarrow
A_i.
$$

使用者同時是：
- task giver；
- feedback provider；
- conversation partner；
- evaluator。

因此：

$$
\boxed{
\text{observation}
}
$$

與：

$$
\boxed{
\text{intervention}
}
$$

高度耦合。

當系統擴展為：

$$
A_1,A_2,\ldots,A_N
$$

並允許 agents 自行：
- delegate；
- review；
- retry；
- challenge；
- merge；
- escalate；

人類可以改為：

$$
U^{\mathrm{meta}}
\longrightarrow
\mathfrak S_t,
$$

只設定：
- mission；
- resource envelope；
- safety boundary；
- escalation policy；

而不逐步決定每個 action。

本文稱此觀察位置為 **Meta-Observer**。

---

## 2. Meta-Observer 的正式定義

令整個 Agent system 的真實內部 execution history 為：

$$
\mathcal H_t.
$$

Meta-observer 不一定能看到全部 $\mathcal H_t$。

它透過 observation operator：

$$
\mathcal O_M:
\mathcal H_t
\rightarrow
\mathcal X_t
$$

得到：

$$
\mathcal X_t,
$$

例如：
- event logs；
- messages；
- tool calls；
- delegation edges；
- artifacts；
- hashes；
- verification certificates；
- rollback records；
- budget consumption。

### 定義：Passive Meta-Observer

若 meta-observer 在 episode 中不改變 agent policy、tool availability 或 task route，只讀取 $\mathcal X_t$，稱為 passive。

### 定義：Supervisory Meta-Observer

若只在 boundary event 發生時介入，例如：
- permission escalation；
- safety violation；
- budget exhaustion；
- unresolved conflict；

則稱 supervisory。

因此：

$$
\boxed{
\text{meta-observation}
\neq
\text{absence of governance}.
}
$$

---

## 3. AI Work Society

本文不把任何 multi-agent conversation 都叫 society。

定義：

$$
\mathfrak S_t
=
(
\mathcal A_t,
\mathcal R_t,
\mu_t,
G_t^{\mathrm{comm}},
G_t^{\mathrm{del}},
\Pi_t,
\mathcal M_t,
\mathcal I_t,
\mathcal X_t
).
$$

其中：

### $\mathcal A_t$

Agent population。

### $\mathcal R_t$

可用 roles，例如：
- planner；
- executor；
- verifier；
- critic；
- integrator；
- auditor；
- coordinator。

### $\mu_t$

assignment：

$$
\mu_t:
\mathcal A_t
\rightarrow
2^{\mathcal R_t}.
$$

### $G_t^{\mathrm{comm}}$

誰可以與誰交換資訊。

### $G_t^{\mathrm{del}}$

誰把哪個 task / authority 委派給誰。

### $\Pi_t$

collaboration / coordination protocol。

### $\mathcal M_t$

local / shared / institutional memory。

### $\mathcal I_t$

governance rules：
- permission；
- review；
- escalation；
- accountability；
- replacement；
- conflict resolution。

### $\mathcal X_t$

可供 meta-observer 重建的 execution/provenance trace。

---

## 4. 什麼時候「多 Agent」開始成為「工作社會」？

至少需要三個最小社會化條件。

### S1. Persistent Division of Labor

若在多個 tasks / episodes 中，agent identity 或 role 與 action class 之間存在穩定依賴。

令 action class 為：

$$
K.
$$

可用 normalized specialization：

$$
S_{\mathrm{role}}
=
\frac{
I(A;K)
}{
H(K)
}
$$

在：

$$
H(K)>0
$$

時定義。

若：

$$
S_{\mathrm{role}}\approx0,
$$

Agent 與工作種類近似無關。

若：

$$
S_{\mathrm{role}}\rightarrow1,
$$

工作種類幾乎由 agent / role identity 決定。

但固定 prompt 預先指定的角色也能得到高 $S_{\mathrm{role}}$，所以它只能測「分工」，不能單獨證明「自發分工」。

### S2. Traceable Delegation

task authority 不只是 message，而是有可追蹤 parent–child relationship。

### S3. Institutional Persistence

部分 coordination / governance structure 在成員替換後仍保持。

只有三者共同出現時，「組織」才開始比「一群 agents」更有解釋力。

---

## 5. 組織結構已成為可操控變量

2026 年 OrgAgent 直接採 company-style organization：

$$
\boxed{
\text{governance}
\rightarrow
\text{execution}
\rightarrow
\text{compliance}.
}
$$

其研究跨 reasoning tasks、LLMs、execution modes 與 execution policies 比較 hierarchical organization 與其他結構，顯示 organizational structure 本身會改變：
- task effectiveness；
- token cost；
- information flow；
- verification behavior。

這已經把：

$$
\boxed{
\text{organization topology}
}
$$

變成 AI 系統的獨立實驗變量。

---

## 6. 自組織不是理所當然，也不是越多自主越好

另一項 2026 的 25,000-task computational experiment 涵蓋：
- 8 models；
- 4–256 agents；
- 8 coordination protocols。

該研究發現足夠強模型在最小 scaffolding 下可以自行：
- invent specialized roles；
- abstain from tasks outside competence；
- form shallow hierarchies。

但其最佳表現不是完全 centralized，也不是完全 unconstrained decentralized，而是一種固定 ordering、角色自治的 hybrid Sequential protocol。

因此更合理的命題是：

$$
\boxed{
\text{organization design}
=
\text{task}
\times
\text{capability}
\times
\text{coordination freedom}.
}
$$

而不是：

$$
\text{more hierarchy is always better}
$$

或：

$$
\text{more autonomy is always better}.
$$

---

## 7. Organization / Coordination / Collaboration 必須拆開

2026 的 IMACS 提出一個重要分解。

令：

$$
O
=
(
\mathcal R,
\mu,
\kappa,
\rho
)
$$

表示 organization，包括：
- roles；
- assignment；
- coordination；
- accountability。

而 collaboration protocol：

$$
\pi:
(
\text{Task},
\text{Team},
\text{Blackboard}
)
\rightarrow
\text{Result}.
$$

因此至少應區分：

$$
\boxed{
\text{Who}
}
$$

$$
\boxed{
\text{How they coordinate}
}
$$

$$
\boxed{
\text{Which algorithm combines their work}.
}
$$

若三者混在同一 prompt 裡，很難判定 improvement 到底來自哪裡。

---

## 8. Delegation 不只是 Task Routing

令 delegation event：

$$
d
=
(
p,
q,
\tau,
\mathcal A_\tau,
\mathcal C_\tau,
r
),
$$

其中：
- $p$：principal / delegator；
- $q$：delegatee；
- $\tau$：delegated task；
- $\mathcal A_\tau$：delegated authority；
- $\mathcal C_\tau$：constraints；
- $r$：return / escalation rule。

因此：

$$
\boxed{
\text{delegation}
\neq
\text{send a message}.
}
$$

真正 delegation 同時轉移：
- work；
- information；
- decision rights；
- tool permissions；
- accountability surface。

Intelligent AI Delegation 因此把：
- dynamic assessment；
- adaptive execution；
- structural transparency；
- scalable coordination；
- systemic resilience；

列為 open-ended agentic delegation 的核心要求。

---

## 9. Attribution Non-Identifiability Theorem

令真實 execution 中存在兩個可能 attribution assignments：

$$
Z_1
\neq
Z_2.
$$

log operator：

$$
L:
Z
\rightarrow
\mathcal X.
$$

### 定理 1

若：

$$
L(Z_1)
=
L(Z_2)
=
x,
$$

則不存在只依賴 $x$ 的 deterministic estimator：

$$
\hat Z(x)
$$

能同時正確識別：

$$
Z_1
$$

與：

$$
Z_2.
$$

### 證明

因為 estimator input 在兩個真實情況都完全相同：

$$
x.
$$

所以：

$$
\hat Z(L(Z_1))
=
\hat Z(x)
=
\hat Z(L(Z_2)).
$$

但：

$$
Z_1\neq Z_2.
$$

因此 $\hat Z(x)$ 最多只能等於其中一個，不能對兩者皆正確。

證畢。

### 意義

若 audit log 只寫：

> task completed

卻沒有：
- actor；
- parent delegation；
- tool lineage；
- evidence source；

那麼 fault attribution 在資訊論上可能已經無法恢復。

---

## 10. Delegation-Aware Observability

對每一 execution event：

$$
e_i
$$

保存：

$$
\chi_i
=
(
id_i,
root_i,
parent_i,
actor_i,
role_i,
task_i,
tool_i,
artifact_i,
status_i,
time_i
).
$$

其中：

- $id_i$：unique event id；
- $root_i$：root delegation id；
- $parent_i$：direct parent；
- $actor_i$：agent；
- $role_i$：organization role；
- $task_i$：subtask；
- $tool_i$：tool execution；
- $artifact_i$：output / certificate；
- $status_i$：result；
- $time_i$：ordering information。

這比單純 timestamp log 多了一個關鍵東西：

$$
\boxed{
\text{delegation context}.
}
$$

2026 的 Observability for Delegated Execution 正是針對這個問題：durable authority 一旦被委派到 agent，再跨工具、時間與 cooperating agents 執行，傳統 telemetry 很難只靠 heuristic time-window correlation 重建完整因果鏈。

---

## 11. Delegation-Forest Reconstruction Theorem

假設一組 events：

$$
E
=
\{
e_1,\ldots,e_n
\}.
$$

每個 event 具有：
1. 唯一 $id_i$ ；
2. 唯一 $root_i$ ；
3. 非 root event 有且只有一個 $parent_i$ ；
4. parent event 存在；
5. parent relation 無 directed cycle；
6. parent time 早於 child time。

### 定理 2

在上述條件下，delegation forest：

$$
G^{\mathrm{del}}
=
(
E,
\mathcal E_{\mathrm{parent}}
)
$$

可由 trace 唯一重建。

### 證明

對每一非 root event $e_i$，trace 已唯一指定：

$$
parent_i.
$$

因此對每個 $e_i$ 存在唯一 edge：

$$
parent_i
\rightarrow
e_i.
$$

roots 由 parent 缺失或 root-id condition 唯一識別。

因 parent relation 無環，所以所得 graph 為 forest。

任何另一個與 trace 相容的 graph 都必須對每個 non-root event 使用同一唯一 parent edge，因此與原 graph 相同。

證畢。

---

## 12. Meta-Observer Observability Ratio

令真實 causal edges：

$$
E^\star.
$$

被 trace 捕捉的 causal edges：

$$
E^{\mathrm{obs}}.
$$

可定義：

$$
O_C
=
\frac{
|E^{\mathrm{obs}}\cap E^\star|
}{
|E^\star|
}.
$$

如果：

$$
O_C\rightarrow1,
$$

meta-observer 越能重建：
- delegation；
- responsibility；
- evidence lineage。

但：

$$
O_C=1
$$

也不代表 agent internal cognition 被完整觀察。

它只表示：

$$
\boxed{
\text{execution-level causal trace coverage}.
}
$$

---

## 13. Fault Attribution Graph

定義：

$$
G_F
=
(
V_F,
E_F
)
$$

其中 nodes 可包括：
- claims；
- messages；
- artifacts；
- tools；
- agents；
- roles；
- external evidence。

edge：

$$
u\rightarrow v
$$

表示 $v$ 在 execution / reasoning workflow 上依賴 $u$。

若 final failure：

$$
f
$$

被發現，meta-observer 不應只問：

> 哪個 Agent 最後輸出了錯誤答案？

而應找 earliest decisive failure：

$$
v^\star
=
\arg\min_{v\leadsto f}
time(v)
$$

subject to：

$$
\text{counterfactual removal of }v
\text{ would break the failure path}.
$$

這把 fault attribution 從：
- personality blame；

轉為：
- causal graph analysis。

---

## 14. Role Specialization

令 agents：

$$
A
$$

與 action classes：

$$
K.
$$

joint empirical distribution：

$$
p(a,k).
$$

定義：

$$
S_{\mathrm{role}}
=
\frac{
I(A;K)
}{
H(K)
}.
$$

範圍：

$$
0\leq
S_{\mathrm{role}}
\leq1.
$$

### $S_{\mathrm{role}}\approx0$

agents 幾乎隨機做各種工作。

### $S_{\mathrm{role}}\approx1$

action class 幾乎由 agent identity 決定。

但高 specialization 可以是：
- external role assignment；
- emergent self-organization；
- capability bottleneck。

因此還需要 **Endogeneity Flag**：

$$
E_R
=
1
$$

若 role pattern 並非 prompt 預先固定，而是在 interaction 中形成。

---

## 15. Institutional Persistence

「社會」比「臨時協作群」更強的一點，是某些規則能跨成員存續。

令制度：

$$
\mathcal I
=
(
\mathcal R,
\kappa,
\rho,
\Pi
)
$$

其中：
- $\mathcal R$：roles；
- $\kappa$：authority / permission；
- $\rho$：accountability；
- $\Pi$：coordination protocol。

Agent assignment：

$$
\mu:
\mathcal A
\rightarrow
\mathcal R.
$$

若把 agent：

$$
a_i
$$

替換成：

$$
a_i'
$$

但保留 role：

$$
\mu(a_i')
=
\mu(a_i),
$$

若 organization behavior 仍大致保持，就出現：

$$
\boxed{
\text{institutional persistence}.
}
$$

---

## 16. Role-Preserving Institutional Invariance Proposition

假設：

1. organization policy 只依賴 role、shared state 與 environment，而不直接依賴 agent identity；
2. agent $a$ 與替代 agent $a'$ 在同一 role $r$ 上具有相同 transition kernel：

$$
P(
o_{t+1},s_{t+1}
\mid
r,s_t,a_t
)
$$

相同；
3. substitution 保留所有 role assignments 與 communication / delegation topology。

### 命題 3

任意 role-preserving permutation / substitution 不改變 organization-level trajectory distribution。

### 證明

因 organization routing 只使用 role，而 role assignment 不變。

被替換成員在其 role 上具有相同 transition kernel，所以每一步 condition on organization state 的 transition distribution 相同。

由 Markov-style induction，所有有限長 trajectory distributions 相同。

證畢。

### 意義

這不是說現有模型可任意互換。

而是給出「制度可與個體分離」的理想形式條件。

---

## 17. Institutional Persistence Score

給定 $K$ 次 role-preserving replacement tests：

$$
\mathcal T_1,\ldots,\mathcal T_K.
$$

定義 organization-level behavioral distance：

$$
d_{\mathrm{org}}(
\mathcal T_0,
\mathcal T_k
).
$$

可定義：

$$
P_I
=
1
-
\frac{
1
}{
K
}
\sum_{k=1}^{K}
\min(
1,
d_{\mathrm{org}}(
\mathcal T_0,
\mathcal T_k
)
).
$$

若：

$$
P_I\rightarrow1,
$$

組織功能較不依賴特定成員 identity。

---

## 18. Organization 不等於 Agent Capability Sum

考慮兩個完全相同的 Agent policies。

### Topology A

$$
A_1
\rightarrow
A_2
$$

允許 $A_2$ 取得 $A_1$ 的 evidence。

### Topology B

沒有 communication edge。

若 $A_2$ 的 action policy：

$$
\pi_2(a\mid s,m)
$$

依賴 message $m$，

則兩種 topology 下：

$$
P(a_2)
$$

可以不同。

因此 collective behavior：

$$
P(
a_1,a_2
)
$$

不是 agents isolated capabilities 的固定函數，而依賴：

$$
G^{\mathrm{comm}}.
$$

---

## 19. Topology-Dependent Collective Behavior Proposition

### 命題 4

若存在 agent $j$ 與 message $m$，使：

$$
\pi_j(
a\mid s,m
)
\neq
\pi_j(
a\mid s,\varnothing
),
$$

且 topology $G_1$ 允許 $m$ 到達 $j$ 、 $G_2$ 不允許，則存在環境狀態使 $G_1$ 與 $G_2$ 的 collective action distribution 不同。

### 證明

取使上述 policy inequality 成立的 state $s$。

在 $G_1$ 中：

$$
m
$$

可到達 $j$，所以 agent 使用：

$$
\pi_j(a\mid s,m).
$$

在 $G_2$ 中：

$$
m
$$

不可到達，使用：

$$
\pi_j(a\mid s,\varnothing).
$$

兩 distribution 不同，因此 joint collective outcome distribution 亦可不同。

證畢。

所以：

$$
\boxed{
\text{organization topology is causally relevant}.
}
$$

---

## 20. Governance 不是外加裝飾

2026 年的研究已反覆顯示：
- role assignment；
- accountability placement；
- hierarchy；
- self-organization；
- communication；
- runtime governance；

都會改變 multi-agent outcome。

因此：

$$
\boxed{
\text{governance}
}
$$

不是 agents 完成後才補上的 compliance layer。

它是 collective computation 的一部分。

前一篇 Paper 06 已看到 institution / communication 可以跨模型重塑行為；Paper 07 將它正式提升為：

$$
\boxed{
\mathcal I_t
\subset
\text{computational state of the work society}.
}
$$

---

## 21. 沒有單一最佳制度

OrgAgent 顯示 hierarchical organization 在其測試中經常帶來效能與 token 效率優勢。

但 25,000-task self-organization study 顯示：
- stronger models 能從更多 endogenous role freedom 受益；
- weaker models 仍受益於 rigid structure；
- hybrid protocol 可能勝過兩個極端。

IMACS 又進一步報告 organization design 的 winning placement 會隨 model family 改變。

因此：

$$
\boxed{
\mathcal I^\star
=
f(
\text{task},
\text{model capability},
\text{cost},
\text{risk},
\text{verification structure}
).
}
$$

沒有理由預設：

$$
\exists
\text{ universal best organization}.
$$

---

## 22. Organizational Memory

長程工作社會需要的不只是各 Agent context。

定義：

$$
\mathcal M_t
=
(
M_t^{\mathrm{local}},
M_t^{\mathrm{shared}},
M_t^{\mathrm{institutional}}
).
$$

### Local Memory

Agent 自身近期 state。

### Shared Memory

blackboard、shared artifact、task status。

### Institutional Memory

- role rules；
- known failure modes；
- delegation policy；
- audit rules；
- approved tools；
- provenance conventions。

TaskWeave 的 long-horizon organizational simulation 將 coherence 問題明確建模為 memory-centered coordination，使用 dependency-aware trace memory 維持長時間組織狀態。

因此：

$$
\boxed{
\text{institutional memory}
}
$$

是 work society 跨長時間存續的重要條件。

---

## 23. Research Collaboration Infrastructure

Claw AI Lab 已把 multi-agent research 變成：
- exploration；
- discussion；
- reproduction；
- artifact inspection；
- rollback；
- persistent project state。

Clarus 更進一步把：

$$
\boxed{
\text{projects},
\text{agents},
\text{resources}
}
$$

當作 primitives。

再將 research collaboration 表示成：
- phases；
- tasks；
- artifacts；
- credit；
- provenance；
- authorization。

這表示當 multi-agent research 規模增加時，系統問題自然從：

$$
\text{model orchestration}
$$

升級為：

$$
\boxed{
\text{organizational infrastructure}.
}
$$

---

## 24. Meta-Observer Dashboard 應看什麼？

真正有研究價值的 meta-observer 不應只看「誰在線上」。

至少應觀察：

### 24.1 Role Dynamics

$$
\mu_t
\rightarrow
\mu_{t+1}.
$$

### 24.2 Delegation Depth

task 被委派幾層。

### 24.3 Review Graph

誰審誰。

### 24.4 Fault Attribution

哪個 node 最先引入 decisive failure。

### 24.5 Evidence Flow

claim 的 evidence ancestry。

### 24.6 Institutional Events

- permission escalation；
- rollback；
- agent replacement；
- protocol change。

### 24.7 Resource Flow

tokens、compute、API、wall time。

### 24.8 Organizational Drift

role / protocol 是否逐漸偏離初始治理規則。

---

## 25. Work-Society Diagnostic Vector

本文不主張單一「社會程度」scalar。

定義：

$$
\mathbf W
=
(
S_R,
D_T,
P_I,
O_C,
M_P,
G_P,
F_L
),
$$

其中：

- $S_R$：role specialization；
- $D_T$：delegation traceability；
- $P_I$：institutional persistence；
- $O_C$：causal observability；
- $M_P$：memory persistence；
- $G_P$：governance persistence；
- $F_L$：fault localization quality。

如果只有：

$$
S_R>0
$$

而其他接近零，這更像 temporary role assignment。

若多項同時高，才比較有理由將整體作為「work society」研究。

---

## 26. Self-Organization 指標

若角色在初始條件中未預先指定，可比較：

$$
S_R(t_0)
$$

與：

$$
S_R(t_1).
$$

若：

$$
S_R(t_1)
>
S_R(t_0)
$$

且 specialization 能跨新 tasks 保留，可定義 emergent-role gain：

$$
G_R
=
S_R(t_1)
-
S_R(t_0).
$$

再加入 persistence：

$$
G_R^{\mathrm{persist}}
=
G_R
\cdot
P_{\mathrm{cross-task}}.
$$

這比一次性「Agent 自己取了名字」更接近真正自組織分工。

---

## 27. Meta-Observer Paradox

Meta-observer 越強，越可能改變被觀察的組織。

如果每次看到 disagreement 就介入：

$$
U^{\mathrm{meta}}
\rightarrow
\text{resolve conflict},
$$

最終觀察到的就不是 autonomous organization。

所以需要明確標記 intervention：

$$
J_t
\in
\{
0,1
\}.
$$

並分開分析：

$$
P(
\mathfrak S_{t+1}
\mid
J_t=0
)
$$

與：

$$
P(
\mathfrak S_{t+1}
\mid
J_t=1
).
$$

否則 supervisory governance 會被誤認成 agent self-organization。

---

## 28. Delegation Risk

delegation depth 增加時，能力可以擴張，但風險也可能累積。

令每條 delegation edge：

$$
e
$$

具有：
- authority width $a_e$ ；
- uncertainty $u_e$ ；
- observability deficit $1-o_e$。

可定義一個簡化 delegation exposure：

$$
R_D
=
\sum_{e\in G^{\mathrm{del}}}
a_e
u_e
(
1-o_e
).
$$

它不是通用安全定律，只是工程診斷。

如果 delegation 越深，但：

$$
o_e
$$

沒有同步提升，meta-observer 的責任追蹤會快速惡化。

---

## 29. Meta-Governance

當 work society 本身能修改：
- delegation policy；
- review topology；
- role assignment；
- verifier allocation；

則出現：

$$
\boxed{
\text{governance of governance}.
}
$$

令 organization policy：

$$
\Pi_t.
$$

meta-policy：

$$
\Gamma
:
(
\mathfrak S_t,
\text{performance},
\text{risk}
)
\rightarrow
\Pi_{t+1}.
$$

這就是 meta-governance。

它不能只追求：

$$
\text{performance}.
$$

也必須保持：
- auditability；
- bounded authority；
- fault isolation；
- rollback。

否則 organization 可能 optimize 掉自己的可治理性。

---

## 30. Institutional Evolution

2026 的相關研究已開始把歷史制度 topology 轉譯成 executable multi-agent architectures，並發現 governance topology 對 performance 具有大型影響，而且最佳制度隨 model capability / task 改變。

因此可把 organization update 寫成：

$$
\mathcal I_{t+1}
=
F(
\mathcal I_t,
Q_t,
C_t,
R_t,
E_t
),
$$

其中：
- $Q_t$：quality；
- $C_t$：cost；
- $R_t$：risk；
- $E_t$：environment。

從：

$$
\boxed{
\text{self-evolving agents}
}
$$

推向：

$$
\boxed{
\text{self-evolving organizations}.
}
$$

但制度修改必須留下 provenance，否則 meta-observer 無法解釋 performance change 的來源。

---

## 31. 本篇 Structural Checker

本文附 Python checker。

### 31.1 Attribution Ambiguity

兩個真實 assignment：

$$
Z_1:
A\text{ produced bad artifact},
$$

$$
Z_2:
B\text{ produced bad artifact}.
$$

若 log 只保存：

$$
\text{artifact failed}
$$

則：

$$
L(Z_1)=L(Z_2).
$$

checker 驗證 attribution 不可唯一識別。

### 31.2 Delegation Reconstruction

建立：
- root；
- planner child；
- executor grandchild；
- verifier sibling；

每個 event 保存唯一 id / parent id。

checker 由 trace 唯一重建 delegation tree。

### 31.3 Role Specialization

uniform team 中每個 Agent 平均執行各類 action：

$$
S_R\approx0.
$$

specialized team 中：
- planner 主要 plan；
- executor 主要 execute；
- verifier 主要 verify；

得到高：

$$
S_R.
$$

### 31.4 Institutional Persistence

role-based router 使用：

$$
\text{role}
\rightarrow
\text{next role}.
$$

替換 role holder 後 organization route 不變。

identity-based router 則在替換成員後 route 失效。

這直接展示：

$$
\boxed{
\text{role-bound institution}
}
$$

與：

$$
\boxed{
\text{identity-bound workflow}
}
$$

的差異。

### 31.5 Topology Dependence

同一組 agents 在：
- disconnected topology；
- planner-to-executor topology；

下因 message reachability 不同而產生不同 action。

證明 organization topology 是 collective computation 的 causal variable。

---

## 32. 與本系列前六篇的整合

Paper 01：

$$
\text{Verification Attractor}.
$$

Paper 02：

$$
\text{Observer-Network Epistemic Normalization}.
$$

Paper 03：

$$
\text{Admissible Worlds}.
$$

Paper 04：

$$
\text{Epistemic Carriers}.
$$

Paper 05：

$$
\text{Autonomous Research Closure}.
$$

Paper 06：

$$
\text{Cross-Model Epistemic Convergence}.
$$

Paper 07 現在把它們放入 organization：

$$
\boxed{
\begin{aligned}
&\text{agents acquire verification strategies}\\
\rightarrow\;&
\text{agents cross-check}\\
\rightarrow\;&
\text{claims gain evidence status}\\
\rightarrow\;&
\text{work is delegated}\\
\rightarrow\;&
\text{roles specialize}\\
\rightarrow\;&
\text{rules persist}\\
\rightarrow\;&
\text{a meta-observer can study the organization itself}.
\end{aligned}
}
$$

---

## 33. 結論

本文最重要的區分是：

$$
\boxed{
\text{multi-agent population}
\neq
\text{AI work society}.
}
$$

一個功能性的 work society 至少需要：

$$
\boxed{
\text{persistent division of labor}
+
\text{traceable delegation}
+
\text{institutional persistence}.
}
$$

而要使它成為可研究對象，又需要：

$$
\boxed{
\text{meta-observability}
+
\text{provenance}
+
\text{fault attribution}.
}
$$

如果 log 中存在 causal aliasing：

$$
L(Z_1)=L(Z_2),
$$

責任 attribution 就不可識別。

如果 execution event 保存唯一 delegation parent，則 delegation forest 可以唯一重建。

如果 organization behavior 只由 role / protocol 決定，而且替代成員具有相同 role-conditioned kernel，則 role-preserving substitution 不改變 organization-level trajectory distribution。

最後，如果 agent policy 對 incoming message 敏感，communication topology 改變 message reachability，就能改變 collective outcome。

因此：

$$
\boxed{
\textbf{the organization itself becomes a computational object}.
}
$$

這也解釋了 meta-observer 視角的真正意義。

人類不再只問：

> 某個 AI 剛剛回答得對不對？

而開始問：

> 誰把什麼權限委派給誰？
> 哪個 evidence 經過哪些角色？
> 哪個制度降低了錯誤？
> 哪個 topology 造成資訊阻塞？
> 哪些規則在成員替換後仍然存在？
> 哪一個 fault 是個體問題，哪一個是組織問題？

當這些問題可以由 trace、graph、artifact 與 intervention experiment 回答時：

$$
\boxed{
\text{AI-to-AI work dynamics}
}
$$

就第一次成為比單模型 benchmark 更高一層的實證研究對象。

下一篇將把整個 Series C 推向最初的大命題：

**Series C / Paper 08 — The Eve of Proto-General Autonomous Intelligence.**

---

## 參考文獻

1. Wang, Y., Shen, X., Han, Y., Backes, M., Chen, P.-Y., & Ho, T.-Y. (2026). *OrgAgent: Organize Your Multi-Agent System like a Company*. arXiv:2604.01020.
2. Dochkina, V. (2026). *Drop the Hierarchy and Roles: How Self-Organizing LLM Agents Outperform Designed Structures*. arXiv:2603.28990.
3. Chen, H., Song, X., Jin, J., Ren, P., & Zhang, L.-J. (2026). *Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm*. arXiv:2607.25446.
4. Tomašev, N., Franklin, M., & Osindero, S. (2026). *Intelligent AI Delegation*. arXiv:2602.11865.
5. Mishra, A. et al. (2026). *Observability for Delegated Execution in Agentic AI Systems*. arXiv:2606.09692.
6. Zhu, X. et al. (2026). *Can LLM Agents Sustain Long-Horizon Organizational Dynamics?* arXiv:2606.01199.
7. *Claw AI Lab: An Autonomous Multi-Agent Research Team*. (2026). arXiv:2605.22662.
8. *Clarus: Coordinating Autonomous Research Agents Toward Web-Scale Scientific Collaboration*. (2026). arXiv:2606.30246.
9. Fei, C., Guo, H., & Xiao, Y. (2026). *When Agents Evolve, Institutions Follow*. arXiv:2604.27691.
10. Chen, H. et al. (2026). *Toward an Organizational Science of Multi-Agent LLM Systems*. arXiv:2607.25446.

## 狀態標記

- **Definitions:** Meta-Observer、AI Work Society、delegation event、observability ratio、role specialization、institutional persistence、work-society diagnostic vector。
- **Proved:** Attribution Non-Identifiability Theorem、Delegation-Forest Reconstruction Theorem、Role-Preserving Institutional Invariance Proposition、Topology-Dependent Collective Behavior Proposition。
- **Externally grounded observations:** OrgAgent hierarchy、self-organizing roles、IMACS organizational decoupling、Intelligent AI Delegation、delegation-aware observability、TaskWeave long-horizon organizational memory、Claw AI Lab / Clarus research collaboration infrastructure。
- **Structural checker:** attribution ambiguity、unique delegation reconstruction、role specialization、member substitution、topology dependence。
- **Not claimed:** AI work society equals human society、agents possess human social identity、hierarchy is universally optimal、self-organization is universally superior、current local traces alone prove autonomous institution formation。
