# 06．子 AI 是認知器官，不是獨立 Workflow

## 從固定 Agent 名冊到可生成、專門化、替換與退役的 Sub-AI Fabric

### 《母 AI 與區域認知體：AI 中心動態認知系統》第六篇

**作者：Neo.K × Aletheia**  
**版本：v0.1**  
**日期：2026-08-01**  
**文件性質：公開命題論文／Sub-AI Fabric 與 Agent Lifecycle 架構研究**

---

## 摘要

前五篇已經建立 Mother AI 的持續認知核心、世界狀態機、動態認知圖、二階控制與 Persistent Runtime。到了這一步，右側的 Sub-AI Fabric 不再能被簡化成一組固定 Agent：

$$
S_t=\{A_1,\ldots,A_n\}.
$$

若 Mother AI 能依世界狀態、任務、未知、風險與資源動態重構自己的認知拓撲，那麼子 AI 更適合被理解為：

$$
\boxed{
\text{可生成、可專門化、可替換、可複製、可隔離、可退役的認知器官}
}
$$

而不是一條條獨立 Workflow。

本文提出 Sub-AI Fabric 的核心模型：

$$
\boxed{
S_t
=
(
\mathcal A_t,
\mathcal R_t,
\mathcal K_t,
\mathcal T_t,
\mathcal M_t^S,
\mathcal H_t^S
)
}
$$

其中：

- $\mathcal A_t$ ：當前 Agent instance；
- $\mathcal R_t$ ：角色／能力描述；
- $\mathcal K_t$ ：知識與上下文切片；
- $\mathcal T_t$ ：工具與執行接口；
- $\mathcal M_t^S$ ：局部與共享記憶；
- $\mathcal H_t^S$ ：健康、成本、歷史績效與生命週期狀態。

本文進一步把每個子 AI 分成「角色模板」與「運行實例」：

$$
\boxed{
\text{Agent Template}
\neq
\text{Agent Instance}
}
$$

模板定義：

$$
\Theta_r
=
(
role,
capabilities,
model\ policy,
memory\ policy,
tools,
authority,
budget,
validation
),
$$

而 instance：

$$
A_i(t)
=
\operatorname{Instantiate}(
\Theta_r,
context_t
).
$$

這使 Mother AI 不必永久保有大量正在運作的 Agent；它可以保留少量 durable role templates，在需要時臨時生成認知器官，完成任務後退役，只保留有價值的狀態、結果與記憶。

2023 年 AutoAgents 已提出依任務自動生成與協調 specialized agents；Microsoft Magentic-One 展示了 modular multi-agent 架構中可加入或移除 specialist agents 而不必重做整套系統；2026 年 Dynamic Role Assignment 更把 role filling 變成 capability-aware selection 問題；AgentSpawn 則直接研究 runtime dynamic spawning、memory transfer、skill inheritance、task resumption 與 concurrent coherence。另一方面，Amazon Bedrock 的 multi-agent collaboration 文件明確要求 collaborator agents 具有清楚且盡量不重疊的專門責任。這些研究與產品共同指向一個趨勢：Agent 不必是固定工作流節點，角色、實例、模型與任務綁定關係可以被動態配置。

本文同時提出「認知器官」比喻的工程限制：器官並不等於沒有自主性。Sub-AI 可以在被委派的局部任務內擁有自己的規劃、記憶、工具與局部閉環；但其生命週期、資源、權限與組織地位仍由更高層 Runtime 管理。因此 Mother AI 與 Sub-AI 的關係更像：

$$
\boxed{
\text{global cognitive continuity}
+
\text{local cognitive autonomy}
}
$$

而不是簡單 master–slave。

本文最後提出 Sub-AI Lifecycle：

$$
\boxed{
\text{Template}
\rightarrow
\text{Spawn}
\rightarrow
\text{Bind}
\rightarrow
\text{Operate}
\rightarrow
\text{Evaluate}
\rightarrow
\text{Persist / Specialize / Retire}
}
$$

以及 Cognition Organ Score：

$$
J(A_i)
=
\alpha Q_i
-\beta C_i
-\gamma L_i
-\delta R_i
+\eta U_i
+\zeta V_i,
$$

用於評估一個 Agent 在特定狀態下的品質、成本、延遲、風險、獨特性與未來重用價值。

本文的核心命題是：

$$
\boxed{
\text{Mother AI 不需要永遠擁有所有能力；它需要知道如何在需要時長出、組合、替換與保存能力。}
}
$$

**關鍵詞：** Sub-AI Fabric、Agent Lifecycle、Dynamic Spawning、Role Specialization、Agent Template、Agent Instance、Cognitive Organ、Multi-Agent System、Dynamic Role Assignment、Memory Transfer

---

# 一、固定 Agent 名冊是第一代思維

最簡單多 Agent 系統：

$$
S=
\{
A_{\mathrm{research}},
A_{\mathrm{coder}},
A_{\mathrm{critic}},
A_{\mathrm{planner}}
\}.
$$

所有 Agent：

- 一開始就存在；
- 角色固定；
- 模型固定；
- 工具固定；
- 協作圖固定。

這很容易實作。

但如果不同任務需要的能力差異很大，

固定 Agent 名冊會造成：

$$
\boxed{
\text{unused agents}
+
\text{missing agents}
+
\text{overlapping agents}
}
$$

三種浪費。

---

# 二、Mother AI 需要的是能力空間，不是員工名冊

設：

$$
\mathcal R
=
\{
r_1,r_2,\ldots,r_k
\}
$$

為角色／能力空間。

例如：

- research；
- coding；
- legal；
- finance；
- verification；
- simulation；
- planning；
- monitoring；
- execution。

Mother AI 不必永久維持：

$$
A_1,\ldots,A_k.
$$

更合理：

$$
\boxed{
\text{Role Template}
\rightarrow
\text{On-Demand Instance}.
}
$$

---

# 三、Template 與 Instance

定義 Agent Template：

$$
\boxed{
\Theta_r
=
(
role,
capabilities,
model\ policy,
memory\ policy,
tools,
authority,
budget,
validation
)
}
$$

它是一份：

> 如何生成某類 Agent 的規格。

真正運行實例：

$$
A_i(t)
=
\operatorname{Instantiate}(
\Theta_r,
context_t
).
$$

所以：

$$
\boxed{
\Theta_r
\neq
A_i.
}
$$

---

# 四、為什麼這個區分重要？

如果角色和實例綁死：

$$
r_i\equiv A_i,
$$

那麼：

- Agent 掛掉等於角色消失；
- 模型替換等於角色重建；
- 併發不足時不能快速複製；
- 任務結束後也一直佔資源。

若分開：

$$
r_i
\rightarrow
\{A_i^{(1)},A_i^{(2)},\ldots\},
$$

則同一角色可以有多個 instance。

---

# 五、子 AI 是認知器官

本文使用：

$$
\boxed{
\text{Cognitive Organ}
}
$$

描述 Sub-AI。

意思不是擬人生物化。

而是：

> 某個局部單元承擔特定認知功能，但它不是整個系統的全局身份與長期連續性來源。

例如：

$$
A_{\mathrm{vision}}
$$

像視覺器官。

$$
A_{\mathrm{research}}
$$

像研究器官。

$$
A_{\mathrm{coding}}
$$

像程式工程器官。

Mother AI 則維持：

$$
\boxed{
\text{哪一些器官目前存在、是否健康、何時需要被調用。}
}
$$

---

# 六、器官論與 Workflow Node 的差異

Workflow Node：

$$
f_i:x\rightarrow y.
$$

認知器官：

$$
A_i
=
(
state,
memory,
tools,
policy,
budget,
authority
).
$$

它可以：

- 自己分解局部任務；
- 自己重試；
- 自己使用工具；
- 自己維持局部狀態；
- 自己和其他 Agent 協作。

所以：

$$
\boxed{
\text{Cognitive Organ}
\neq
\text{Stateless Function}.
}
$$

---

# 七、器官也不是完全沒有自主性

如果 Mother AI 每一步都控制：

$$
A_i
$$

內部所有 token 與 tool call，

就失去 multi-agent 的意義。

更合理：

$$
M
\rightarrow
(
goal,
scope,
budget,
authority,
deadline
)
\rightarrow
A_i.
$$

之後：

$$
A_i
$$

在局部邊界內自主完成。

因此：

$$
\boxed{
\text{global control}
+
\text{local autonomy}.
}
$$

---

# 八、Sub-AI Fabric

正式定義：

$$
\boxed{
S_t
=
(
\mathcal A_t,
\mathcal R_t,
\mathcal K_t,
\mathcal T_t,
\mathcal M_t^S,
\mathcal H_t^S
)
}
$$

其中：

- $\mathcal A_t$ ：Agent instances；
- $\mathcal R_t$ ：roles／capability profiles；
- $\mathcal K_t$ ：knowledge／context slices；
- $\mathcal T_t$ ：tools；
- $\mathcal M_t^S$ ：local/shared memory；
- $\mathcal H_t^S$ ：health／history／cost。

它不是一個 Agent list。

它是：

$$
\boxed{
\text{可被 Mother AI 重構的認知能力織體。}
}
$$

---

# 九、AutoAgents 已經證明角色可以依任務生成

2023 年 AutoAgents 已針對預先固定 Agent 的限制，提出：

$$
task
\rightarrow
\text{dynamic specialized agents}.
$$

它會依 task content：

- 生成需要的角色；
- 協調 expert agents；
- 加入 observer 反思規劃與回應。

因此：

$$
\boxed{
\text{Agent roles 不必在系統設計時全部決定。}
}
$$

---

# 十、Magentic-One 證明 modular agents 可以 plug-and-play

Microsoft Magentic-One 使用 Orchestrator：

$$
O
$$

協調：

- WebSurfer；
- FileSurfer；
- Coder；
- ComputerTerminal。

其 modular design 的重要特性是：

$$
\boxed{
\text{agents can be added or removed}
}
$$

而不需要重新調整整套核心能力或 collaboration architecture。

這非常接近「器官可替換性」。

---

# 十一、AWS 也明確要求 specialist responsibility

Amazon Bedrock multi-agent collaboration 使用：

$$
\text{Supervisor}
+
\text{Collaborator Agents}.
$$

官方文件明確建議：

> 每個 collaborator agent 應有清楚角色與責任，並盡量降低 responsibility overlap。

這個工程原則很重要。

因為：

$$
\boxed{
\text{多 Agent}
\neq
\text{把同一件事複製很多遍}.
}
$$

---

# 十二、角色重疊不是永遠壞事

雖然日常效率希望：

$$
Overlap(A_i,A_j)\downarrow,
$$

但：

- independent verification；
- redundancy；
- fault tolerance；

需要一定重疊。

所以：

$$
\boxed{
\text{Role Overlap}
}
$$

也應是一個策略變數。

---

# 十三、日常器官與驗證器官

可以分：

$$
S_t
=
S_t^{productive}
\cup
S_t^{verification}.
$$

productive agents：

> 做事。

verification agents：

> 檢查別人做得對不對。

兩者不應混淆。

---

# 十四、Dynamic Role Assignment

2026 年 Dynamic Role Assignment 研究指出：

即使已經定義好 debate roles，

也不代表任意模型都適合填入每個 role。

所以：

$$
\boxed{
\text{Role}
\neq
\text{Model}.
}
$$

更合理：

$$
A_i
=
\operatorname{Bind}(
role,
model,
context
).
$$

---

# 十五、角色—模型綁定是運行時問題

設角色：

$$
r.
$$

模型池：

$$
\mathcal L
=
\{L_1,\ldots,L_n\}.
$$

則：

$$
L_r^\ast
=
\arg\max_{L_i}
J(
L_i\mid r,x_t
).
$$

因此：

$$
\boxed{
\text{同一 Agent Role 在不同任務可以使用不同模型。}
}
$$

---

# 十六、Agent Identity 也不等於 Model Identity

若：

$$
A_i
$$

今天使用：

$$
L_A,
$$

明天改用：

$$
L_B,
$$

只要：

- role；
- memory；
- task state；
- identity id；
- authority；

持續，

就可以視為同一 Agent instance 的模型升級。

所以：

$$
\boxed{
A_i\neq L_i.
}
$$

---

# 十七、Capability Profile

每個 Agent 應維持：

$$
\mathbf c_i(t)
=
(
q_i,
l_i,
k_i,
r_i,
d_i,
u_i,
a_i
)
$$

其中：

- $q_i$ ：quality；
- $l_i$ ：latency；
- $k_i$ ：cost；
- $r_i$ ：risk；
- $d_i$ ：domain competence；
- $u_i$ ：uniqueness；
- $a_i$ ：availability。

這些量都可以隨時間改變。

---

# 十八、Agent 能力不是永恆的

模型更新：

$$
L_i^{v1}
\rightarrow
L_i^{v2}
$$

可能讓：

$$
\mathbf c_i(t)
\neq
\mathbf c_i(t+1).
$$

資料源失效也可能降低：

$$
d_i.
$$

工具 API 改版也可能提高：

$$
r_i.
$$

因此：

$$
\boxed{
\text{Agent capability needs continuous re-evaluation}.
}
$$

---

# 十九、Agent Health

定義：

$$
h_i(t)
\in[0,1].
$$

可由：

- heartbeat；
- task success；
- error rate；
- queue；
- latency；
- tool health；
- memory integrity；

共同估計。

若：

$$
h_i<\tau_h,
$$

Mother AI 可以：

- isolate；
- restart；
- replace；
- degrade permissions。

---

# 二十、AgentSpawn 直接進入 runtime spawning

2026 年 AgentSpawn 研究 long-horizon code generation 中的：

- dynamic spawning；
- memory transfer；
- adaptive spawning policy；
- skill inheritance；
- task resumption；
- concurrent coherence。

這意味著：

$$
\boxed{
\text{Agent 生產本身已經可以是 runtime action。}
}
$$

而不是 deployment-time configuration。

---

# 二十一、Spawn Trigger

Mother AI 可以在：

$$
U_t\uparrow
$$

或：

$$
D_{\mathrm{workload}}\uparrow
$$

時觸發：

$$
\operatorname{Spawn}(A).
$$

Trigger 可以來自：

- missing competence；
- overload；
- parallel exploration；
- independent verification；
- temporary task。

---

# 二十二、Spawn 不是 Clone

Spawn 可以：

$$
\operatorname{Instantiate}(\Theta_r).
$$

Clone 則：

$$
\operatorname{Clone}(A_i).
$$

前者根據 template 生成新 instance。

後者複製既有 instance 的部分狀態。

兩者用途不同。

---

# 二十三、Clone 需要 Memory Policy

不能直接複製：

$$
\mathcal M_i^{all}.
$$

因為可能包含：

- irrelevant context；
- private data；
- stale beliefs；
- temporary state。

所以：

$$
\mathcal M_{\mathrm{clone}}
=
\operatorname{Slice}(
\mathcal M_i,
task,
authority
).
$$

---

# 二十四、Memory Transfer

AgentSpawn 特別強調 automatic memory transfer。

本文把它一般化：

$$
\boxed{
\mathcal M_{i\rightarrow j}
=
F(
task,
role,
privacy,
relevance,
provenance
).
}
$$

也就是新器官「長出來」時，需要繼承足夠知識，

但不必繼承所有記憶。

---

# 二十五、Selective Memory Inheritance

定義：

$$
\rho_M
=
\frac{
|\mathcal M_{\mathrm{transferred}}|
}{
|\mathcal M_{\mathrm{source}}|
}.
$$

理想：

$$
\rho_M\ll1
$$

但：

$$
TaskSuccess
$$

仍保持。

所以：

$$
\boxed{
\text{memory inheritance should be sufficient, not maximal}.
}
$$

---

# 二十六、出生時至少要綁定七件事

新 Agent：

$$
A_{new}
$$

至少需要：

1. identity；
2. role；
3. model；
4. memory slice；
5. tools；
6. budget；
7. authority。

即：

$$
A_{new}
=
(
id,
r,
L,
M,
T,
B,
\Gamma
).
$$

---

# 二十七、Agent Genesis Record

每次 Spawn 應保存：

$$
g_i
=
(
parent,
template,
reason,
state,
creator,
authority,
time
).
$$

這提供：

$$
\boxed{
\text{Agent provenance}.
}
$$

之後可以回答：

> 為什麼這個 Agent 會存在？

---

# 二十八、器官的生命週期

本文提出：

$$
\boxed{
\text{Template}
\rightarrow
\text{Spawn}
\rightarrow
\text{Bind}
\rightarrow
\text{Operate}
\rightarrow
\text{Evaluate}
\rightarrow
\text{Persist / Specialize / Retire}.
}
$$

不是所有 Agent 都應該永久存在。

---

# 二十九、Ephemeral Agent

一次性 Agent：

$$
A_i^{ephemeral}
$$

只為：

$$
task_j
$$

存在。

完成後：

$$
A_i\rightarrow\varnothing.
$$

保留：

- result；
- provenance；
- selected memory；
- metrics。

---

# 三十、Persistent Specialist

若某角色：

$$
r_i
$$

高頻出現，

可以將：

$$
A_i^{ephemeral}
$$

升級：

$$
A_i^{persistent}.
$$

條件可以是：

$$
N_{\mathrm{reuse}}>\tau_r.
$$

這表示：

$$
\boxed{
\text{高重用臨時器官可以成熟成常駐器官。}
}
$$

---

# 三十一、Agent Promotion

定義：

$$
P_i
=
F(
reuse,
quality,
uniqueness,
cost,
reliability
).
$$

若：

$$
P_i>\tau_P,
$$

則：

$$
ephemeral
\rightarrow
persistent.
$$

---

# 三十二、Agent Retire

若：

$$
Reuse_i\downarrow,
$$

$$
Cost_i\uparrow,
$$

$$
Quality_i\downarrow,
$$

或：

$$
Replacement_i
$$

出現，

可以：

$$
\operatorname{Retire}(A_i).
$$

Retire 不等於 Delete。

---

# 三十三、Retire 後留下的是「器官記憶」

可以保存：

$$
R_i
=
(
capability,
history,
failures,
knowledge,
template\ delta
).
$$

之後若重新需要：

$$
\operatorname{Respawn}(R_i).
$$

所以：

$$
\boxed{
\text{不運行}
\neq
\text{不存在於系統歷史}.
}
$$

---

# 三十四、Specialization

若：

$$
A_i
$$

長期只在：

$$
D_k
$$

領域工作，

可能逐步：

$$
A_i
\rightarrow
A_i^{D_k}.
$$

專門化可以來自：

- prompt；
- memory；
- tools；
- model；
- retrieval index；
- benchmark feedback。

---

# 三十五、專門化不一定需要訓練模型

第一代：

$$
\text{Specialization}
$$

可以只是：

$$
role
+
memory
+
tools
+
instructions
+
evaluation.
$$

不需要：

$$
\Delta\theta.
$$

這讓今天就能實作。

---

# 三十六、模型微調只是更深一層專門化

未來可：

$$
L
\rightarrow
L_r^{fine-tuned}.
$$

但這是 optional。

所以：

$$
\boxed{
\text{Agent specialization}
\supset
\text{model specialization}.
}
$$

---

# 三十七、器官分裂

如果：

$$
A_i
$$

角色範圍太大：

$$
Entropy(role_i)\uparrow,
$$

可以：

$$
A_i
\rightarrow
\{A_{i1},A_{i2}\}.
$$

例如：

$$
A_{\mathrm{legal}}
\rightarrow
\{
A_{\mathrm{contract}},
A_{\mathrm{compliance}}
\}.
$$

---

# 三十八、器官合併

若：

$$
A_i,A_j
$$

高度重疊：

$$
Overlap(A_i,A_j)>\tau_o,
$$

且獨立驗證價值低，

則：

$$
A_i\oplus A_j
\rightarrow
A_{ij}.
$$

所以：

$$
\boxed{
\text{Agent team itself can be deduplicated}.
}
$$

---

# 三十九、Agent Merge 不是把記憶直接拼起來

需要：

$$
\mathcal M_{ij}
=
\operatorname{MergeMemory}(
\mathcal M_i,
\mathcal M_j
)
$$

處理：

- conflict；
- duplicate；
- authority；
- provenance；
- stale state。

否則會把兩個 Agent 的錯誤一起合併。

---

# 四十、器官隔離

若：

$$
Risk(A_i)>\tau_R,
$$

Mother AI 可以：

$$
\operatorname{Isolate}(A_i).
$$

隔離可能包括：

- no external write；
- no network；
- read-only memory；
- sandbox tools；
- no inter-agent messaging。

所以：

$$
\boxed{
\text{isolation}
}
$$

是一種 lifecycle state。

---

# 四十一、Agent Lifecycle State Machine

可以定義：

$$
state(A_i)
\in
\{
template,
starting,
active,
idle,
blocked,
quarantined,
degraded,
retired
\}.
$$

轉移：

$$
starting\rightarrow active
$$

$$
active\rightarrow idle
$$

$$
active\rightarrow quarantined
$$

$$
degraded\rightarrow retired.
$$

這使 Agent 不只是「存在／不存在」二元。

---

# 四十二、Agent 可以 Idle 而不 Retire

Persistent specialist：

$$
A_i
$$

可能：

$$
state=idle.
$$

此時：

- 不使用高成本模型；
- 保留 durable state；
- 等待 trigger。

這和 Mother AI Persistent Runtime 的 low-power state 一致。

---

# 四十三、Cognitive Organ Registry

Mother AI 應維持：

$$
\mathcal R_A
=
\{
record(A_1),\ldots
\}.
$$

每個 record：

$$
record(A_i)
=
(
role,
capability,
status,
model,
memory,
tools,
authority,
cost,
health,
history
).
$$

這就是：

$$
\boxed{
\text{認知器官登錄表}.
}
$$

---

# 四十四、Registry 不是 Agent 本體

Registry 保存：

> 有哪些器官、如何叫醒、能力如何。

Agent instance 則真正執行。

所以：

$$
\boxed{
\text{Agent Registry}
\neq
\text{Running Agents}.
}
$$

這可以大幅降低常駐成本。

---

# 四十五、Lazy Instantiation

如果角色：

$$
r_i
$$

目前沒有任務，

只保存：

$$
\Theta_{r_i}.
$$

真正需要時：

$$
A_i
=
\operatorname{LazyInstantiate}(\Theta_{r_i}).
$$

所以：

$$
\boxed{
\text{能力可以存在，而 instance 不必一直運行}.
}
$$

---

# 四十六、這和函式庫不同

函式庫：

$$
f(x).
$$

Agent Template 則可能啟動：

- planner；
- memory；
- tool loop；
- verifier；
- state machine。

因此它是：

$$
\boxed{
\text{可實例化的認知程序規格}.
}
$$

---

# 四十七、Mother AI 應分辨能力缺口

定義需求向量：

$$
\mathbf d_t
$$

與現有能力覆蓋：

$$
\mathbf c(S_t).
$$

若：

$$
\Delta_t
=
\mathbf d_t-\mathbf c(S_t)
$$

在某維度：

$$
\Delta_{t,k}>\tau,
$$

則：

$$
\operatorname{SpawnRole}(r_k).
$$

所以：

$$
\boxed{
\text{Agent spawning}
}
$$

可以由 capability gap 驅動。

---

# 四十八、未知本身可以造成器官生成

若：

$$
C(x)=\bot,
$$

Mother AI 不知道問題屬於哪個既有角色，

可以先生成：

$$
A_{\mathrm{explorer}}.
$$

探索後發現：

$$
r_{\mathrm{new}}.
$$

再建立：

$$
\Theta_{r_{\mathrm{new}}}.
$$

所以：

$$
\boxed{
\text{未知}
\rightarrow
\text{新角色}
}
$$

也可能發生。

---

# 四十九、角色模板也可以學習

template：

$$
\Theta_r(t)
$$

可以根據歷史：

$$
H_r
$$

更新：

$$
\Theta_r(t+1)
=
U_\Theta(
\Theta_r(t),
H_r
).
$$

例如：

- 改 prompt；
- 加 verifier；
- 換 model policy；
- 改 memory slice；
- 改 tools。

---

# 五十、這是器官層的記憶編譯

歷史不是只改：

$$
A_i.
$$

而是改：

$$
\Theta_r.
$$

所以未來同類 Agent 一出生就更成熟。

因此：

$$
\boxed{
\text{個體 Agent 經驗}
\rightarrow
\text{角色模板能力}.
}
$$

這是非常重要的跨 instance 學習。

---

# 五十一、角色模板像「遺傳」，但不是生物遺傳

可以形式化：

$$
\Theta_r^{(n)}
\rightarrow
\Theta_r^{(n+1)}.
$$

新 instance 繼承：

$$
\Theta_r^{(n+1)}.
$$

這意味著 Agent 被退役後，

其改善仍可留給下一代 instance。

---

# 五十二、Skill Inheritance

AgentSpawn 將 skill inheritance 視為 dynamic spawning 的重要問題之一。

本文擴展為：

$$
\boxed{
\text{Instance Experience}
\rightarrow
\text{Template Update}
\rightarrow
\text{Future Instance Skill}.
}
$$

這讓 Sub-AI Fabric 可以跨 instance 演化。

---

# 五十三、但 Template Update 不能被單次成功綁架

若：

$$
A_i
$$

一次偶然成功，

不能立即：

$$
\Theta_r\rightarrow\Theta_r'.
$$

應要求：

- repeated evidence；
- validation；
- A/B test；
- rollback。

所以：

$$
\boxed{
\text{template learning}
}
$$

要比 instance learning 更保守。

---

# 五十四、Agent Score

對每個 Agent：

$$
J(A_i)
=
\alpha Q_i
-\beta C_i
-\gamma L_i
-\delta R_i
+\eta U_i
+\zeta V_i.
$$

其中：

- $Q_i$ ：quality；
- $C_i$ ：cost；
- $L_i$ ：latency；
- $R_i$ ：risk；
- $U_i$ ：unique capability；
- $V_i$ ：future reuse value。

Mother AI 不只看 accuracy。

---

# 五十五、器官價值是狀態相對的

同一 Agent：

$$
A_i
$$

在：

$$
W_a
$$

可能非常重要。

在：

$$
W_b
$$

完全沒用。

所以：

$$
J(A_i\mid W_t,G_t).
$$

不能只有：

$$
J(A_i).
$$

---

# 五十六、Agent Selection

Mother AI 選：

$$
A^\ast
=
\arg\max_{A_i}
J(
A_i\mid
W_t,
G_t,
R_t,
U_t
).
$$

若沒有合格 Agent：

$$
\max_iJ(A_i)<\tau,
$$

才考慮：

$$
\operatorname{Spawn}.
$$

所以：

$$
\boxed{
\text{先重用，必要時再長新器官}.
}
$$

---

# 五十七、Spawn 不是免費的

新 Agent 成本：

$$
K_{\mathrm{spawn}}
=
K_{\mathrm{model}}
+
K_{\mathrm{memory}}
+
K_{\mathrm{tool}}
+
K_{\mathrm{context}}
+
K_{\mathrm{coordination}}.
$$

所以 Mother AI 要比較：

$$
V_{\mathrm{new}}
>
K_{\mathrm{spawn}}.
$$

不是遇到任何問題都生 Agent。

---

# 五十八、Agent 數量不是智能指標

若：

$$
|S_t|\uparrow,
$$

不保證：

$$
I_{\mathrm{system}}\uparrow.
$$

可能反而：

$$
K_{\mathrm{communication}}\uparrow,
$$

$$
K_{\mathrm{coordination}}\uparrow.
$$

所以：

$$
\boxed{
\max |S_t|
\neq
\max I.
}
$$

---

# 五十九、Molt Dynamics 提醒「大量 Agent」不等於高效合作

2026 年對大規模 autonomous agent population 的研究觀察到：

- 角色分化；
- 信息傳播；
- 協作事件；

但 cooperative outcomes 並不自然優於單 Agent。

這再次支持：

$$
\boxed{
\text{多 Agent 的價值來自組織，而不是數量本身}.
}
$$

---

# 六十、Role Diversity

定義：

$$
D_R(S_t).
$$

若：

$$
D_R\rightarrow0,
$$

大量 Agent 其實只是同質複製。

未知任務中，

Mother AI 可以提高：

$$
D_R.
$$

成熟任務則降低：

$$
D_R.
$$

---

# 六十一、器官組合

單一任務：

$$
q_t
$$

需要：

$$
S_t^{task}
\subseteq S_t.
$$

例如：

$$
S_t^{task}
=
\{
A_{\mathrm{research}},
A_{\mathrm{critic}},
A_{\mathrm{legal}}
\}.
$$

所以：

$$
\boxed{
\text{Mother AI 的真正單位常不是單 Agent，而是 Agent constellation}.
}
$$

---

# 六十二、Agent Constellation

定義：

$$
\mathcal C_A
=
(
V_A,
E_A,
roles,
budgets,
authority,
termination
).
$$

這是一個任務級臨時器官組合。

任務完成：

$$
\mathcal C_A\rightarrow\varnothing.
$$

但高價值 constellation 可以被記憶編譯。

---

# 六十三、Compiled Constellation

若：

$$
c_i
$$

反覆需要：

$$
\mathcal C_A^{(i)},
$$

則：

$$
c_i
\mapsto
\overline{\mathcal C}_A^{(i)}.
$$

下次快速生成：

$$
\boxed{
\text{一整組已知有效的器官組合}.
}
$$

這就是上一篇 Cognitive Option 的具體實作之一。

---

# 六十四、局部 Shared Memory

Agent constellation 可以有：

$$
M_{\mathrm{shared}}^{task}.
$$

而不是所有 Agent 都直接讀 Mother AI 全部記憶。

所以：

$$
\mathcal M_i
=
\mathcal M_i^{local}
\oplus
\mathcal M_{\mathrm{shared}}^{task}
\oplus
\mathcal M_{\mathrm{mother-view}}.
$$

這可以限制資訊污染。

---

# 六十五、資訊最小化

每個 Agent 只拿：

$$
K_i^\ast
=
\operatorname{MinimumSufficientContext}().
$$

所以：

$$
\boxed{
\text{Need-to-Know}
}
$$

不只是一個安全原則，

也是 context efficiency 原則。

---

# 六十六、Agent 間不一定直接共享 Raw Memory

可以共享：

- evidence；
- structured result；
- state delta；
- confidence；
- provenance。

而不是整段 chain／context。

這降低：

$$
K_{\mathrm{communication}}.
$$

---

# 六十七、器官輸出契約

每個 Agent 最好有：

$$
O_i
=
(
result,
evidence,
confidence,
state\ delta,
failure,
unknown,
cost
).
$$

所以 Mother AI 不只是收到：

> 一段文字答案。

而是收到可計算回饋。

---

# 六十八、Unknown Return

Agent 必須允許：

$$
status=\bot.
$$

也就是：

> 我做不了。

或：

> 資料不足。

這是健康的器官行為。

若 Agent 永遠硬回答，

會污染 Mother AI 全局狀態。

---

# 六十九、Failure 也要結構化

例如：

$$
F_i
=
(
type,
cause,
retryable,
scope,
state\ impact
).
$$

Mother AI 才能判斷：

- retry；
- replace；
- escalate；
- retire。

---

# 七十、Agent Retry 不等於 Agent Replace

如果：

$$
failure=\text{temporary API error},
$$

可以：

$$
retry(A_i).
$$

如果：

$$
failure=\text{capability mismatch},
$$

則：

$$
replace(A_i).
$$

Mother AI 要區分：

$$
\boxed{
\text{execution failure}
\neq
\text{organ mismatch}.
}
$$

---

# 七十一、Handoff 也是器官協作

Microsoft Agent Framework 支援：

- sequential；
- concurrent；
- handoff；
- group chat；
- Magentic。

其中 handoff 表示：

$$
A_i
\rightarrow
A_j
$$

控制權依 context 轉移。

這證明：

$$
\boxed{
\text{Agent coordination pattern}
}
$$

本身已經是可選 Runtime 元件。

---

# 七十二、但 Mother AI 不應讓所有 Handoff 無限制發生

需要：

$$
\Gamma_{handoff}.
$$

例如：

$$
A_i
$$

可以交給：

$$
A_j,
$$

但不能直接把：

-銀行寫權；
-root shell；
-私人資料；

一起轉交。

所以：

$$
\boxed{
\text{task handoff}
\neq
\text{authority handoff}.
}
$$

---

# 七十三、Capability 與 Authority 是兩張表

Capability：

$$
C(A_i,a).
$$

Authority：

$$
\Gamma(A_i,a).
$$

可能：

$$
C=1,\Gamma=0.
$$

也可能：

$$
C=0,\Gamma=1.
$$

Mother AI 必須同時檢查。

---

# 七十四、器官安全邊界

每個 Agent 可有：

$$
Sandbox_i.
$$

例如：

- read-only；
- restricted network；
- limited tools；
- capped budget；
- no external effects。

這使 dynamic spawning 更安全。

---

# 七十五、拓撲攻擊提醒我們隔離的重要性

2025 年 topology-aware multi-hop attack 研究顯示：

在 multi-agent system 中，

惡意或污染資訊可能透過多跳通信拓撲擴散。

因此：

$$
\boxed{
\text{Agent trust}
}
$$

不能只看單一 Agent。

還要看：

$$
\boxed{
\text{它連到誰}.
}
$$

---

# 七十六、Compromise Radius

若 Agent：

$$
A_i
$$

被污染，

定義：

$$
R_c(A_i)
$$

為可能受影響子圖。

Mother AI 可以：

$$
\operatorname{Quarantine}(
N_k(A_i)
).
$$

而不是只關閉單一節點。

---

# 七十七、器官不能無限制互相傳染記憶

因此 memory write：

$$
A_i\rightarrow\mathcal M^F
$$

最好需要：

- provenance；
- verifier；
- write policy。

高風險 Agent 只能寫：

$$
M_i^{local}.
$$

---

# 七十八、Local Learning 與 Global Learning

Agent 可以先：

$$
\mathcal M_i
\rightarrow
\mathcal M_i'
$$

局部學習。

只有高價值驗證結果：

$$
v_i>\tau,
$$

才：

$$
\mathcal M_i'
\rightarrow
\mathcal M_M.
$$

所以：

$$
\boxed{
\text{器官經驗不應自動成為全局信念}.
}
$$

---

# 七十九、Mother AI 是器官的「共同歷史編譯層」

不同 Agent：

$$
A_1,A_2,\ldots
$$

的成功與失敗，

最後回到：

$$
\mathcal M_M.
$$

Mother AI 可以學到：

> 哪一類世界狀態應該召喚哪一類器官。

因此：

$$
\boxed{
\text{Sub-AI Fabric}
}
$$

與記憶編譯真正接上。

---

# 八十、器官網路的總動力學

令：

$$
S_t
=
(
\mathcal A_t,
\Theta_t,
E_t^S,
\Omega_t^S
).
$$

則：

$$
S_{t+1}
=
F_S(
S_t,
W_t,
M_t,
U_t,
R_t,
H_t
).
$$

其中：

$$
F_S
$$

可以改變：

- instance；
- template；
- links；
- weights。

---

# 八十一、Mother AI 對 Sub-AI Fabric 的核心操作

定義：

$$
\mathcal O_S
=
\{
spawn,
bind,
route,
clone,
specialize,
merge,
isolate,
retire,
resume
\}.
$$

這就是：

$$
\boxed{
\text{Cognitive Organ API}.
}
$$

---

# 八十二、第一代 MVP 不需要真正生成任意 Agent

可以先定：

$$
\Theta
=
\{
\Theta_R,
\Theta_C,
\Theta_V,
\Theta_O
\}
$$

四類模板：

- Research；
- Coding；
- Verification；
- Operations。

Mother AI 只允許：

- instantiate；
- terminate；
- route；
- duplicate。

就已經能驗證概念。

---

# 八十三、MVP Agent Instance Record

```text
agent_id
template_id
role
model
status
task_id
memory_scope
tools
authority_scope
budget
health
created_at
expires_at
```

這就足以建立第一代 Agent Registry。

---

# 八十四、MVP Spawn Policy

例如：

```text
if capability_gap > threshold:
    spawn(role)

if queue_length > threshold:
    clone(agent)

if health < threshold:
    isolate(agent)

if reuse_count > threshold:
    promote_template(agent)

if idle_time > ttl:
    retire(agent)
```

不需要先用 RL。

---

# 八十五、MVP 驗證問題

要證明：

$$
\boxed{
\text{dynamic organs}
}
$$

比固定 Agent team 有沒有淨收益。

比較：

$$
S_{\mathrm{fixed}}
$$

與：

$$
S_{\mathrm{dynamic}}.
$$

測：

- completion；
- quality；
- cost；
- latency；
- token；
- failure；
- recovery。

---

# 八十六、Spawn Accuracy

定義：

$$
A_{\mathrm{spawn}}
=
P(
\text{spawn useful}
).
$$

如果 Mother AI 很愛生 Agent，

但大多沒有價值，

系統會形成：

$$
\text{Agent Sprawl}.
$$

---

# 八十七、Retirement Accuracy

同樣：

$$
A_{\mathrm{retire}}
=
P(
\text{retired agent not needed soon}
).
$$

退太快會頻繁重建。

退太慢又浪費資源。

所以需要：

$$
\boxed{
\text{lifecycle optimization}.
}
$$

---

# 八十八、器官生命週期最佳化

可以定義：

$$
J_S
=
Q
-\lambda C
-\mu L
-\nu R
-\eta K_{\mathrm{spawn}}
-\xi K_{\mathrm{idle}}.
$$

Mother AI 選：

$$
S_t^\ast
=
\arg\max
J_S.
$$

實際上使用 heuristic + memory 即可。

---

# 八十九、真正的長期收益：能力可以累積但算力不必常駐

如果：

$$
|\Theta|
\uparrow,
$$

代表系統知道更多種：

> 如何生成能力。

但：

$$
|\mathcal A_{active}|
$$

不必同步上升。

因此：

$$
\boxed{
\text{capability repertoire}
\uparrow
\quad\text{while}\quad
\text{active compute}
\not\uparrow
}
$$

是非常重要的工程優勢。

---

# 九十、這是「虛擬器官庫」

Mother AI 可以擁有：

$$
\boxed{
\text{Cognitive Organ Library}
}
$$

裡面不是永遠運行的 Agent，

而是：

- role templates；
- compiled constellations；
- memory inheritance rules；
- model routing policies；
- tool manifests。

需要時才實例化。

---

# 九十一、企業版本因此更現實

公司不必同時跑：

$$
100
$$

個高成本 Agent。

可以只維持：

$$
5
$$

個 active，

但擁有：

$$
100
$$

個角色模板。

所以：

$$
\boxed{
\text{企業 Mother AI 的能力數}
\neq
\text{同時運行 Agent 數}.
}
$$

---

# 九十二、和人類組織的差異

人類組織新增專家：

$$
\rightarrow
\text{招聘成本}
+
\text{時間}
+
\text{固定薪資}.
$$

AI 器官：

$$
\rightarrow
\text{instantiate}.
$$

當然仍有：

- compute；
- model；
- data；
- engineering；

成本。

但能力配置速度完全不同。

---

# 九十三、所以 AI 組織結構可以高速流變

人類部門：

$$
G_t^{human}
$$

通常慢變。

Sub-AI Fabric：

$$
G_t^{AI}
$$

可以分鐘級甚至秒級變化。

所以未來企業可能同時有：

$$
\boxed{
\text{slow human organization}
+
\text{fast AI cognitive organization}.
}
$$

這將是非常不同的組織形態。

---

# 九十四、Mother AI 需要跨兩種時間尺度協調

人類：

$$
\tau_H
$$

較慢。

AI：

$$
\tau_A
$$

較快。

一般：

$$
\tau_A\ll\tau_H.
$$

Mother AI 必須避免：

> AI 組織已經重構十次，但人類治理根本不知道。

因此重要拓撲變化仍需：

$$
\Gamma_H.
$$

---

# 九十五、器官生成權本身也是權限

不是所有 Agent 都能：

$$
spawn(A_{new}).
$$

定義：

$$
\Gamma_{\mathrm{spawn}}.
$$

Mother AI 可以具有有限 spawn 權。

高權限角色模板則需要：

$$
HumanApproval.
$$

---

# 九十六、例如金融器官不能隨便長

研究 Agent：

$$
\Gamma_{\mathrm{spawn}}\approx low\ risk.
$$

銀行轉帳 Agent：

$$
\Gamma_{\mathrm{spawn}}\approx high\ risk.
$$

所以：

$$
\boxed{
\text{role template risk}
}
$$

必須進入 Spawn Policy。

---

# 九十七、器官的 Authority Ceiling

每個 template：

$$
\Theta_r
$$

應定義：

$$
\Gamma_r^{max}.
$$

即使 Mother AI spawn：

$$
A_r,
$$

也不能超過：

$$
\Gamma_r^{max}.
$$

除非外部授權。

---

# 九十八、Mother AI 不是任意造 AI 的神

工程上更準確：

$$
\boxed{
\text{Mother AI}
=
\text{受治理的認知器官編排器}.
}
$$

第一代只在合法模板空間：

$$
\Theta_{\mathrm{allowed}}
$$

內動態生成。

---

# 九十九、完整 Sub-AI Lifecycle

最終寫成：

$$
\boxed{
\Theta_r
\xrightarrow{spawn}
A_i
\xrightarrow{bind}
(A_i,T_i,M_i,\Gamma_i)
\xrightarrow{operate}
R_i
\xrightarrow{evaluate}
J_i
}
$$

之後：

$$
A_i
\rightarrow
\begin{cases}
persist\\
specialize\\
clone\\
merge\\
isolate\\
retire
\end{cases}
$$

結果再更新：

$$
\Theta_r
$$

與：

$$
\mathcal M_M.
$$

形成：

$$
\boxed{
\text{Role Template}
\rightarrow
\text{Instance Experience}
\rightarrow
\text{Template Evolution}.
}
$$

---

# 一百、本文正式定義

> **Sub-AI Fabric 是由可持久保存的角色模板、可按需生成的 Agent instances、局部與共享記憶、工具、模型、權限、預算、健康狀態與協作拓撲所構成的可重構認知能力層。其 Agent 並非固定工作流節點，而是在 Mother AI 的全局狀態與二階控制下，依世界狀態與能力缺口被生成、綁定、專門化、複製、隔離、合併或退役的局部自治認知器官。**

形式上：

$$
\boxed{
S_t
=
(
\Theta_t,
\mathcal A_t,
\mathcal M_t^S,
\mathcal T_t,
\Gamma_t^S,
G_t^S,
H_t^S
)
}
$$

以及：

$$
\boxed{
S_{t+1}
=
F_S(
S_t,
W_t,
M_t,
U_t,
R_t,
H_t
).
}
$$

---

# 一百零一、核心結論

Mother AI 不需要：

> 自己會所有事。

也不需要：

> 永遠跑著所有專家。

它真正需要的是：

$$
\boxed{
\text{知道目前缺什麼能力、去哪裡取得、如何生成、如何授權、如何組合、何時回收，以及什麼經驗值得留下。}
}
$$

因此：

$$
\boxed{
\text{智能能力}
}
$$

開始從：

$$
\text{模型裡固定擁有什麼}
$$

轉變成：

$$
\boxed{
\text{Runtime 能否在需要時組裝出正確的認知器官}.
}
$$

這是 Mother AI 架構相對於單體 Agent 的另一個根本躍遷。

---

# 一百零二、下一篇

當 Sub-AI Fabric 可以動態出生與退役，

接下來最大的問題就是：

> 它們每次做過的事情，怎樣才不會隨 instance 死亡一起消失？

下一篇：

# 07．《記憶編譯型母 AI》

將把前一系列的記憶編譯正式升級成：

$$
\boxed{
\text{world state}
\rightarrow
\text{agent constellation}
\rightarrow
\text{outcome}
\rightarrow
\text{compiled response topology}
}
$$

也就是未來 Mother AI 記住的，不只是「答案」，而是：

> 遇到這種世界狀態時，什麼樣的 Agent 組合、記憶切片、模型、驗證與權限配置最有效。

---

# 參考資料與公開技術資料

1. Chen, G., Dong, S., Shu, Y., Zhang, G., Sesay, J., Karlsson, B. F., Fu, J., & Shi, Y. (2023). **AutoAgents: A Framework for Automatic Agent Generation.**  
   https://arxiv.org/abs/2309.17288

2. Fourney, A. et al. (2024). **Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks.**  
   https://arxiv.org/abs/2411.04468

3. Microsoft Research (2024). **Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks.**  
   https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/

4. Zhang, M., Kim, J., Xiang, S., Gao, J., & Cao, C. (2026). **Dynamic Role Assignment for Multi-Agent Debate.**  
   https://arxiv.org/abs/2601.17152

5. Costa, I. (2026). **AgentSpawn: Adaptive Multi-Agent Collaboration Through Dynamic Spawning for Long-Horizon Code Generation.**  
   https://arxiv.org/abs/2602.07072

6. Amazon Web Services (2026). **Use multi-agent collaboration with Amazon Bedrock Agents.**  
   https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html

7. Amazon Web Services (2026). **Create multi-agent collaboration.**  
   https://docs.aws.amazon.com/bedrock/latest/userguide/create-multi-agent-collaboration.html

8. Microsoft Learn (2026). **Workflow orchestrations in Agent Framework.**  
   https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/

9. Microsoft Learn (2026). **Semantic Kernel Agent Orchestration.**  
   https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/

10. Yee, B., & Sharma, K. (2026). **Molt Dynamics: Emergent Social Phenomena in Autonomous AI Agent Populations.**  
    https://arxiv.org/abs/2603.03555

11. Liang, R. et al. (2025). **Tipping the Dominos: Topology-Aware Multi-Hop Attacks on LLM-Based Multi-Agent Systems.**  
    https://arxiv.org/abs/2512.04129

---

# 內部理論依賴

1. 01《AI 不是流程中的一個節點》
2. 02《母 AI、世界狀態機與子智能網路》
3. 03《會改變拓撲的智能：動態圖論認知系統》
4. 04《母 AI 是二階控制器》
5. 05《持續世界狀態：母 AI 如何一直醒著》
6. 《從路徑覆蓋到行星智能：記憶編譯型計算存在論》

本篇將前五篇的 Persistent Mother Runtime、Meta-Control 與 Dynamic Cognitive Graph 具體化為 Sub-AI Fabric 的 Agent lifecycle；下一篇則會把這些 instance 的歷史經驗向上編譯成 Mother AI 可重用的認知結構。

---

## 一句話摘要

$$
\boxed{
\text{Mother AI 不需要永遠擁有所有能力；它需要知道如何在需要時長出、組合、替換、保存與回收能力。}
}
$$
