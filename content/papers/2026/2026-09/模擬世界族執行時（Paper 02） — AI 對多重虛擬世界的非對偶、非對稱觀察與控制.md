# 模擬世界族執行時（Paper 02）
## AI 對多重虛擬世界的非對偶、非對稱觀察與控制
### Simulation World Family Runtime: Non-Dual, Asymmetric Observation and Control over Multiple Virtual Worlds

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列定位：** 載體投影與內視系列之工程延伸／PPOE Paper 02  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** world model × game engine × simulation runtime × AI agent × branching computation × counterfactual reasoning × digital twin × authority architecture  
**狀態：** 統合架構與形式框架；承接既有 WDC／BWC、HDUS、PNCW 與 PPOE

---

## 摘要

Unity、Unreal Engine、Godot 等遊戲引擎早已實作一個重要但常被低估的工程模式：維持可執行 world state，讓 physics、rules、agents 與 event loop 推動世界演化，再透過 camera、renderer、minimap、collision view、navigation view、debug overlay 等不同 observation/projection path，將同一世界投影給不同觀察者。因此遊戲引擎不只是「3D 圖形程式」，而可以被理解為早期的：

$$
\boxed{
\text{World-State Execution}
+
\text{Projection Runtime}.
}
$$

本文進一步提出：未來 AI 不必只在單一虛擬世界裡觀察與行動，也不必把 world model 理解為單一 predictive state。AI 可以同時建立、執行、觀察、比較、嵌套、分支、修剪與治理一整個模擬世界族：

$$
\boxed{
\mathfrak W
=
\{W_0,W_1,\ldots,W_n\}.
}
$$

每個 world 具有自己的 state、transition law、time domain、agents、evidence state、authority boundary 與 projection family：

$$
W_i
=
\left(
S_i,
\Phi_i,
T_i,
\mathcal A_i,
\mathcal E_i,
\mathcal G_i,
\mathcal P_i
\right).
$$

本文稱此架構為 **Simulation World Family Runtime（SWFR，模擬世界族執行時）**。

SWFR 的核心不是「多開幾個遊戲實例」，而是建立具型別、具方向、具 lineage、具 authority 與具 evidence semantics 的 world graph：

$$
\boxed{
G_{\mathfrak W}
=
(V_{\mathfrak W},E_{\mathfrak W}).
}
$$

world-to-world 邊具有明確型別：

$$
e_{ij}
\in
\{
\mathsf{Observe},
\mathsf{Project},
\mathsf{Fork},
\mathsf{Embed},
\mathsf{Query},
\mathsf{Couple},
\mathsf{Control},
\mathsf{Merge},
\mathsf{Prune},
\mathsf{Promote},
\mathsf{TransportEvidence}
\}.
$$

本文特別提出兩條統一原則：**非對偶（non-duality）**與**非對稱（asymmetry）**。

一般投影：

$$
\Pi:
W
\rightarrow
P
$$

通常是 many-to-one，因此可能：

$$
W_a\neq W_b
$$

但：

$$
\Pi(W_a)=\Pi(W_b).
$$

所以：

$$
\boxed{
\Pi^{-1}
\text{ need not exist}.
}
$$

Observation 也不等於 control 的逆：

$$
\boxed{
\mathsf{Observe}
\neq
\mathsf{Control}^{-1}.
}
$$

另一方面，world-to-world observation、authority、causal coupling 與 evidence transport 可以天然非對稱：

$$
O_{ij}\neq O_{ji},
$$

$$
A_{ij}\neq A_{ji},
$$

$$
K_{ij}\neq K_{ji},
$$

$$
E_{ij}\neq E_{ji}.
$$

因此 master runtime 可以完整觀察、fork 或 pause 一個 child world，而 child world 的 local agent 不必知道 master 存在，更不需要反向控制 parent runtime。

本文明確承接 Neo.K 既有 WDC／BWC 與 HDUS，保留：

$$
\boxed{
\text{Future Candidate}
\neq
\text{Runnable World}
\neq
\text{Real-World Future},
}
$$

$$
\boxed{
\text{Clone}
\neq
\text{Fork}
\neq
\text{Replay}
\neq
\text{Counterfactual Branch},
}
$$

$$
\boxed{
\text{World Generation}
\neq
\text{World Governance},
}
$$

$$
\boxed{
\text{Observation}
\neq
\text{Authority}
\neq
\text{Evaluation}
\neq
\text{Governance},
}
$$

以及：

$$
\boxed{
\text{World Count}
\neq
\text{Independent Evidence Count}
\neq
\text{Truth}.
}
$$

本文新增的是把上述 world-domain semantics 與「遊戲引擎作為投影計算機」「AI 並行觀察 simulation world family」「非對偶 projection」「非對稱 world graph」整合成一個 AI-native runtime。

最後，本文提出 **World Family Scheduler（WFS）**。給定世界族、現實證據、任務、算力與風險：

$$
\mathsf{WFS}
:
(\mathfrak W_t,E_t,\tau,b,\rho)
\rightarrow
\mathcal A_{\mathfrak W},
$$

其中：

$$
\mathcal A_{\mathfrak W}
=
\{
\mathsf{Continue},
\mathsf{Fork},
\mathsf{Merge},
\mathsf{Prune},
\mathsf{Pause},
\mathsf{Reobserve},
\mathsf{IncreaseResolution},
\mathsf{PromoteCandidate}
\}.
$$

AI 的「想像」於是可以從 token 中的假設，真正 materialize 成多個 runnable worlds，再對它們施加不同 observation operators。

本文最終命題：

$$
\boxed{
\text{Future AI perception}
\neq
\text{observation of one rendered world}.
}
$$

更一般地：

$$
\boxed{
\text{Future AI perception}
=
\text{structured observation over a family of actual-linked,
simulated, counterfactual, replayed, synthetic, and nested worlds}.
}
$$

**關鍵詞：** Simulation World Family Runtime、SWFR、world family、branching simulation、counterfactual world、nested simulation、asymmetric observation、authority matrix、world graph、game engine、world model

---

# 1. 遊戲引擎其實已經是一台投影計算機

一個 game engine 維持：

$$
W_t
\xrightarrow{\Phi}
W_{t+1}.
$$

同一 $W_t$ 可以有：

$$
\mathcal O_{\mathrm{camera}}(W_t),
$$

$$
\mathcal O_{\mathrm{map}}(W_t),
$$

$$
\mathcal O_{\mathrm{collision}}(W_t),
$$

$$
\mathcal O_{\mathrm{nav}}(W_t).
$$

所以：

$$
\boxed{
\text{3D render}
\text{ is only one observation operator}.
}
$$

---

# 2. Renderer 不等於 World

$$
\boxed{
\text{Renderer}
\neq
\text{World State}
\neq
\text{World Dynamics}.
}
$$

未來引擎的核心不應是「如何畫 3D」，而是：

$$
\boxed{
\text{Simulation Kernel}
+
\text{Projection Operator Family}.
}
$$

---

# 3. 同一世界可以有很多合法 View

$$
\mathcal P(W)
=
\{
P_{\mathrm{3D}},
P_{\mathrm{graph}},
P_{\mathrm{causal}},
P_{\mathrm{economic}},
P_{\mathrm{risk}},
P_{\mathrm{semantic}},
P_{\mathrm{AI}}
\}.
$$

對 AI 而言，graph 或 structured state 可能比 3D viewport 更合理。

---

# 4. 從一個 World 到 World Family

本文定義：

$$
\boxed{
\mathfrak W
=
\{W_0,\ldots,W_n\}.
}
$$

每個 $W_i$ 都是一個具有獨立 runtime semantics 的 world node。

---

# 5. World 的最小型別

$$
W_i
=
\left(
S_i,
\Phi_i,
T_i,
\mathcal A_i,
\mathcal E_i,
\mathcal G_i,
\mathcal P_i
\right).
$$

其中分別是 state、transition、local time、agents、evidence/events、governance/authority、projection family。

---

# 6. World Mode

定義：

$$
\mu(W_i)
\in
\{
\mathsf{ActualLinked},
\mathsf{DigitalTwin},
\mathsf{Simulation},
\mathsf{Counterfactual},
\mathsf{Replay},
\mathsf{Synthetic},
\mathsf{Nested}
\}.
$$

不同 mode 不得混淆。

---

# 7. Actual-Linked World 仍然不是 Reality

$$
\boxed{
W_{\mathrm{actual-linked}}
\neq
\mathcal R.
}
$$

它只是與現實持續 evidence-coupled 的 reconstruction/runtime。

---

# 8. Simulation 與 Counterfactual

Simulation world 可以改 initial state、policy 或參數。

Counterfactual world 更明確包含：

$$
\operatorname{do}(x=x').
$$

因此兩者可以重疊，但不必同義。

---

# 9. Replay 不是 Counterfactual

Replay 主要重新執行或查看既有歷史：

$$
H_{0:t}.
$$

所以承接舊 WDC：

$$
\boxed{
\text{Replay}
\neq
\text{Counterfactual Branch}.
}
$$

---

# 10. Nested World

若 $W_i$ 中的 agent 建立：

$$
W_j,
$$

則：

$$
W_j\triangleleft W_i.
$$

但：

$$
\boxed{
\text{runtime nesting}
\neq
\text{ontological containment}.
}
$$

---

# 11. World Identity 與 Snapshot 分離

承接 HDUS：

$$
\boxed{
WorldSnapshot
\neq
World.
}
$$

同樣：

$$
\boxed{
WorldId
\neq
RenderedSceneId.
}
$$

---

# 12. World Family Graph

$$
G_{\mathfrak W}
=
(V_{\mathfrak W},E_{\mathfrak W}).
$$

節點是 world，邊必須有型別。

---

# 13. Typed World Edge

$$
e_{ij}
=
(W_i,W_j,\tau_e,\gamma_e).
$$

 $\tau_e$ 是 operation type， $\gamma_e$ 是 contract。

---

# 14. World Edge Family

$$
\tau_e
\in
\{
\mathsf{Observe},
\mathsf{Project},
\mathsf{Fork},
\mathsf{Embed},
\mathsf{Query},
\mathsf{Couple},
\mathsf{Control},
\mathsf{Merge},
\mathsf{Prune},
\mathsf{Promote},
\mathsf{TransportEvidence}
\}.
$$

---

# 15. 非對偶一：Projection 通常不可逆

可能：

$$
W_a\neq W_b,
$$

但：

$$
\Pi(W_a)=\Pi(W_b).
$$

因此：

$$
\boxed{
\Pi^{-1}
\text{ need not exist}.
}
$$

從 projection 回推 world 是新的 inverse problem，不是把箭頭反過來。

---

# 16. 非對偶二：Observation 不是 World Recovery

$$
\boxed{
\text{Observation}
\neq
\text{Complete World Reconstruction}.
}
$$

AI 看見一個 world slice 不等於擁有完整 world state。

---

# 17. 非對偶三：Observe 不是 Control 的逆

$$
\boxed{
\mathsf{Observe}
\neq
\mathsf{Control}^{-1}.
}
$$

某些 control 甚至是不可逆 action。

---

# 18. 非對稱 Observation Matrix

$$
O_{ij}
\in
[0,1].
$$

一般：

$$
\boxed{
O_{ij}
\neq
O_{ji}.
}
$$

master world 可以看 child，而 child 可以完全不知道 master。

---

# 19. Branch Blindness

local agent 不一定能觀察：

- sibling worlds；
- parent runtime；
- evaluator；
- governor。

這可以是實驗隔離需求，不是 bug。

---

# 20. Authority Matrix

$$
A_{ij}
\in
[0,1].
$$

一般：

$$
\boxed{
A_{ij}
\neq
A_{ji}.
}
$$

master 可能能 pause、fork、terminate child，但 child 沒有反向能力。

---

# 21. Observation 與 Authority 分離

承接 WDC：

$$
\boxed{
\text{Observation}
\neq
\text{Authority}
\neq
\text{Evaluation}
\neq
\text{Governance}.
}
$$

所以：

$$
O_{ij}=1
$$

不推出：

$$
A_{ij}>0.
$$

---

# 22. Causal Coupling Matrix

$$
K_{ij}
$$

表示 $W_i$ 是否能因果影響 $W_j$。

一般：

$$
K_{ij}\neq K_{ji}.
$$

這對 real world／simulation world 特別重要。

---

# 23. 現實與 Simulation 的典型非對稱

現實可以持續更新 digital twin：

$$
K_{\mathcal R,W}>0.
$$

但 simulation 不應自動改變現實：

$$
K_{W,\mathcal R}=0
$$

直到通過 actuation gate。

---

# 24. Evidence Transport Matrix

$$
E_{ij}
$$

表示 $W_i$ 的 result 是否能成為 $W_j$ 的 admissible evidence。

---

# 25. Simulation Result 不等 Real Evidence

$$
\boxed{
\text{World Execution Result}
\neq
\text{Real-World Evidence}.
}
$$

必須建立 world-to-reality evidence transport contract。

---

# 26. World Count 不等 Evidence Count

$$
\boxed{
\text{World Count}
\neq
\text{Independent Evidence Count}
\neq
\text{Truth}.
}
$$

100 個 shared-backend worlds 可以共享同一 model-form error。

---

# 27. Cross-World Agreement 不等 Replication

$$
\boxed{
\text{Cross-World Agreement}
\neq
\text{Independent Replication}
\neq
\text{Real-World Validation}.
}
$$

---

# 28. AI 可以真的「看多個 Worlds」

令：

$$
\mathfrak W_t
=
\{W_t^{(1)},\ldots,W_t^{(m)}\}.
$$

AI 不必把每個 world render 成影片。

---

# 29. Per-World Observation Operator

$$
P_i
=
\mathcal O_{\tau_i}
(W_i).
$$

例如：

$$
\mathcal O_{\mathrm{risk}},
\quad
\mathcal O_{\mathrm{causal}},
\quad
\mathcal O_{\mathrm{economic}},
\quad
\mathcal O_{\mathrm{goal}}.
$$

---

# 30. AI-native World View

$$
P_i^{AI}
=
\left(
Graph_i,
State_i,
Value_i,
Uncertainty_i
\right).
$$

這可以完全沒有 3D 圖像。

---

# 31. Future AI Perception

$$
\boxed{
\mathcal P_{AI}(t)
=
\{
\mathcal O_{i,k}(W_i)
\}_{i,k}.
}
$$

AI perception 可以是 world × operator 的 observation family。

---

# 32. 不要求 Collapse 成單一 World

AI 可以維持：

$$
\mathcal Q_t
=
\{(W_i,q_i)\}.
$$

 $q_i$ 可以是 probability、rank、plausibility 或其他 task-specific weight。

本文不要求 Bayesian-only。

---

# 33. World Family Scheduler

$$
\boxed{
\mathsf{WFS}
:
(\mathfrak W_t,E_t,\tau,b,\rho)
\rightarrow
\mathcal A_{\mathfrak W}.
}
$$

---

# 34. Scheduler Action

$$
\mathcal A_{\mathfrak W}
=
\{
\mathsf{Continue},
\mathsf{Fork},
\mathsf{Merge},
\mathsf{Prune},
\mathsf{Pause},
\mathsf{Reobserve},
\mathsf{IncreaseResolution},
\mathsf{PromoteCandidate}
\}.
$$

---

# 35. Fork

當 uncertainty 或政策候選需要分開：

$$
W_i
\rightarrow
W_i^{(a)},W_i^{(b)}.
$$

如果 branch 可以獨立 authoritative evolution，應取得 distinct world identity。

---

# 36. Merge

$$
W_A+W_B
\rightarrow
W_C.
$$

但：

$$
\boxed{
WorldMerge
\neq
W_A=W_B=W_C.
}
$$

 $W_C$ 是 merge descendant。

---

# 37. Prune

如果某 world：

$$
Q(W_i)<\theta_Q
$$

或成本：

$$
C(W_i)>\theta_C,
$$

scheduler 可以 prune。

但：

$$
\boxed{
\mathsf{Prune}
\neq
\text{impossibility proof}.
}
$$

---

# 38. Prune 不等 Delete

$$
\boxed{
\mathsf{Prune}
\neq
\mathsf{Delete}.
}
$$

budget prune 最好可 reopen。

---

# 39. Reobserve

對同一 world 改 operator：

$$
\mathcal O_a
\rightarrow
\mathcal O_b.
$$

這正好承接投影系列的 adversarial reprojection。

---

# 40. Increase Resolution

不是每個 world 都要最高 fidelity。

可以：

$$
r_i\neq r_j.
$$

因此形成 multi-fidelity world family：

$$
\mathfrak W
=
\{(W_i,r_i)\}.
$$

---

# 41. Promote Candidate

simulation world 的結論可轉成 action proposal。

但：

$$
\boxed{
\text{PromoteCandidate}
\neq
\text{CommitToReality}.
}
$$

---

# 42. World Family Utility

概念上：

$$
J(W_i)
=
U_{\tau}(W_i)
+
V_{\mathrm{info}}(W_i)
+
V_{\mathrm{counterexample}}(W_i)
-
C_{\mathrm{compute}}(W_i)
-
D_{\mathrm{model}}(W_i).
$$

---

# 43. 世界族不是越大越好

$$
|\mathfrak W|\uparrow
$$

會增加 coverage，也會增加：

- compute；
- memory；
- coordination；
- common-mode error；
- false consensus。

---

# 44. World Family Budget

$$
B_{\mathfrak W}
=
(B_{\mathrm{compute}},B_{\mathrm{memory}},B_{\mathrm{latency}}).
$$

scheduler 分配：

$$
\sum_i b_i
\leq
B_{\mathfrak W}.
$$

---

# 45. AI 的想像可以 Materialize 成 Runnable World

$$
\boxed{
\text{candidate thought}
\rightarrow
\text{runnable world}.
}
$$

這比純 token hypothesis 多出：

- pause；
- inspect；
- query；
- replay；
- instrument；
- fork。

---

# 46. Debug Observer 與 Local Agent 必須分開

外部 observer 可以看 hidden state。

但：

$$
\boxed{
\text{World-External Observer Access}
\neq
\text{World-Local Agent Access}.
}
$$

---

# 47. 三種 Knowledge Domain

$$
K_i^{local}
\neq
K_i^{global}
\neq
K^{cross}.
$$

分別是 local-agent knowledge、world-global knowledge、cross-world knowledge。

---

# 48. Master、Local Agent、Observer、Evaluator、Governor 分離

$$
A^{master}
\neq
A_i^{local}
\neq
O_i
\neq
E_i
\neq
G.
$$

這是世界族治理的基本非坍縮。

---

# 49. Higher-Level 不自動擁有所有 Authority

execution nesting：

$$
W_j\triangleleft W_i
$$

不推出 higher level 在所有 domain 都天然全權。

authority 應為：

$$
A_{ij}^{(d)}.
$$

---

# 50. World Family Governor

$$
\mathsf{Gov}_{\mathfrak W}
$$

管理：

- WorldId；
- lineage；
- lifecycle；
- quota；
- authority；
- evidence transport；
- merge/prune/promotion gate。

---

# 51. Governor 不等 Omniscient Observer

$$
\boxed{
\text{Governance Authority}
\neq
\text{Complete Epistemic Access}.
}
$$

---

# 52. Nested Simulation Depth 必須有界

若：

$$
W_0
\triangleright
W_1
\triangleright
\cdots
\triangleright
W_d,
$$

需有：

$$
d\leq d_{\max}.
$$

由 compute、latency、safety 與 governance 決定。

---

# 53. World Graph 不一定是 Tree

fork lineage 比較像 tree。

但 merge、observe、evidence transport、control 會形成一般 directed graph。

所以應分開：

$$
G_{\mathrm{lineage}}
$$

與：

$$
G_{\mathrm{interaction}}.
$$

---

# 54. Ancestor 不等 CanObserve

$$
Ancestor(W_i,W_j)
$$

不表示：

$$
CanObserve(W_i,W_j).
$$

lineage edge 與 interaction edge 不可混用。

---

# 55. World Time 可以不同

$$
T_i\neq T_j.
$$

因此 cross-world causality 不等 shared clock：

$$
\boxed{
CrossWorldCausality
\neq
SharedWallClock.
}
$$

---

# 56. Time Mapping

需要：

$$
T_{i\rightarrow j}.
$$

但時間換算不改 World identity。

---

# 57. World Family Provenance

$$
Prov(W_i)
=
\left(
WorldId,
Ancestor,
Mode,
Model,
Seed,
Policy,
Evidence,
Engine,
Time,
Authority
\right).
$$

---

# 58. Fork Certificate

$$
\mathsf{ForkCert}
=
\left(
Ancestor,
ForkPoint,
ChangedVariables,
Authority,
Purpose,
Mode
\right).
$$

---

# 59. Merge Certificate

$$
\mathsf{MergeCert}
=
\left(
Parents,
ConflictSet,
MergeRule,
PreservedInvariants,
Authority,
Debt
\right).
$$

---

# 60. Prune Certificate

$$
\mathsf{PruneCert}
=
\left(
WorldId,
Reason,
Evidence,
Budget,
ReopenPolicy
\right).
$$

---

# 61. Cross-World Communication 必須 Explicit

定義 channel：

$$
C_{ij}^{world}.
$$

可限制 bandwidth、event types、authority、latency、provenance。

因此：

$$
\boxed{
\text{world adjacency}
\not\Rightarrow
\text{ambient authority}.
}
$$

---

# 62. Simulation Sandbox

高風險 action 可以先在：

$$
W_{\mathrm{sandbox}}
$$

中執行。

但：

$$
\boxed{
\text{Sandbox Success}
\neq
\text{Real Success}.
}
$$

存在：

$$
D_{\mathrm{sim2real}}.
$$

---

# 63. Reality Re-Entry

真正 action 後，新的 real evidence：

$$
E_{real,t+1}
$$

必須回流：

$$
\mathfrak W_{t+1}
=
\mathcal U(\mathfrak W_t,E_{real,t+1}).
$$

---

# 64. Expected Outcome 不等 Observed Outcome

承接 PNCW：

$$
\boxed{
ExpectedOutcome
\neq
ObservedOutcome.
}
$$

所以任何 promoted action 後都要重新 observe。

---

# 65. SWFR 與 Tree Search 不同

Tree search 主要是 state-action tree。

SWFR node 是具有 identity、time、authority、evidence、lineage、projection contract 的 runnable world。

所以：

$$
\boxed{
\mathsf{SWFR}
\neq
\mathsf{TreeSearch}.
}
$$

---

# 66. SWFR 與 Model-Based RL

model-based RL 提供 learned dynamics 與 planning。

SWFR 新增治理焦點：

- world identity；
- lifecycle；
- cross-world observation；
- evidence；
- authority；
- projection semantics。

---

# 67. SWFR 與 Digital Twin

digital twin 常是：

$$
\mathcal R
\leftrightarrow
W_{\mathrm{DT}}.
$$

SWFR 再生成：

$$
W_{\mathrm{DT}}
\rightarrow
\{W_{\mathrm{scenario}}^{(i)}\}.
$$

形成 scenario family。

---

# 68. SWFR 與 Generative Video World Model

video world model 可是 backend。

但：

$$
\boxed{
\text{Generated Video}
\neq
\text{Complete Runnable World Semantics}.
}
$$

SWFR 不把 world 強制降成 pixels。

---

# 69. Symbolic World 也可以 Runnable

例如：

- PDDL；
- executable simulator；
- causal state machine；
- graph transition system。

所以 world backend 可以非視覺。

---

# 70. Hybrid World Backend

$$
\Phi_i
=
\Phi_{\mathrm{physics}}
+
\Phi_{\mathrm{LLM}}
+
\Phi_{\mathrm{agent}}
+
\Phi_{\mathrm{data}}.
$$

不同 backend 衝突時需要 arbitration，而不是自動平均。

---

# 71. Engine Independence

Unity、Unreal、Godot 都可成為：

$$
Backend(W_i).
$$

SWFR 不綁任一 engine。

---

# 72. Headless World 是一等公民

$$
Renderer=Null
$$

世界仍然 runnable。

這對 AI 同時運行大量 branches 很重要。

---

# 73. Game Engine 的下一代拆法

$$
\boxed{
\text{Simulation Kernel}
+
\text{World Identity}
+
\text{Branching Runtime}
+
\text{Observation Operator Registry}
+
\text{Authority Graph}
+
\text{Evidence Graph}
+
\text{World Family Scheduler}.
}
$$

---

# 74. Observation Operator Plugin

可以定義：

$$
\mathsf{ObsPlugin}
=
\left\langle
InputWorldSchema,
OutputSchema,
Scope,
Cost,
Debt,
Permission
\right\rangle.
$$

---

# 75. SWFR 最小 Runtime

$$
\boxed{
\mathsf{SWFR}
=
\left(
\mathfrak W,
G_{\mathrm{lineage}},
G_{\mathrm{interaction}},
\mathbf O,
\mathbf A,
\mathbf K,
\mathbf E,
\mathsf{WFS},
\mathsf{Gov}_{\mathfrak W},
\mathsf{Proj}
\right).
}
$$

---

# 76. SWFR 最小 Loop

$$
\boxed{
E_t
\rightarrow
\mathfrak W_t
\rightarrow
\mathsf{Observe}
\rightarrow
\mathsf{Evaluate}
\rightarrow
\mathsf{Schedule}
\rightarrow
\mathfrak W_{t+1}.
}
$$

如果涉及現實 action，再增加：

$$
\mathsf{Proposal}
\rightarrow
\mathsf{Authority}
\rightarrow
\mathsf{Actuation}
\rightarrow
E_{real,t+1}.
$$

---

# 77. SWFR 與 PPOE 接合

Paper 01 回答：

$$
W
\rightarrow
P
\rightarrow
\Phi
\rightarrow
Observer.
$$

Paper 02 回答：

$$
\mathfrak W
\rightarrow
\{P_i\}
\rightarrow
Observer/AI.
$$

所以：

$$
\boxed{
\mathfrak W
\xrightarrow{\text{observation selection}}
P^\ast
\xrightarrow{\text{carrier}}
\widehat P.
}
$$

---

# 78. AI 不需要物理 Materialize 所有 Worlds

對 AI-native simulation：

$$
P_i^{AI}
$$

可以只存在於計算載體。

只有人類 inspection 時才：

$$
W_i
\xrightarrow{\Pi_H}
P_i^H.
$$

---

# 79. World Mode 必須始終可見

每個結果必須知道它是：

$$
Observed,
Predicted,
Simulated,
Counterfactual,
Replay,
Synthetic.
$$

否則會發生 world-modality confusion。

---

# 80. AI 也需要 World Source Monitoring

counterfactual event 不能混進 real evidence store。

這就是 B04 source monitoring 的 world-runtime 版本。

---

# 81. World Audit Packet

$$
\mathsf{WAudit}
=
\left\langle
WorldId,
Mode,
Ancestor,
Model,
Evidence,
Observation,
Authority,
Time,
Debt,
Validation
\right\rangle.
$$

---

# 82. 高風險第一原則

$$
\boxed{
\text{more simulated worlds}
\neq
\text{more truth}.
}
$$

---

# 83. 第二原則

$$
\boxed{
\text{better-looking world}
\neq
\text{better-calibrated world}.
}
$$

---

# 84. 第三原則

$$
\boxed{
\text{world-local success}
\neq
\text{real-world action authority}.
}
$$

---

# 85. 第四原則

$$
\boxed{
\text{cross-world access}
\neq
\text{cross-world control}.
}
$$

---

# 86. 第五原則

$$
\boxed{
\text{nested level}
\neq
\text{epistemic superiority}.
}
$$

---

# 87. Counterexample World

世界族不能只做 majority vote。

一個揭露 catastrophic failure 的 world 可能比大量「成功」world 更有決策價值。

可定義：

$$
V_{\mathrm{ce}}(W_i).
$$

---

# 88. Diversity 不是 Independence

世界族可有：

$$
\mathbf D_{\mathfrak W}
=
(
D_{\mathrm{param}},
D_{\mathrm{model}},
D_{\mathrm{policy}},
D_{\mathrm{seed}},
D_{\mathrm{evidence}}
).
$$

不同 seed 不等於不同 model。

---

# 89. Common-Mode Error

如果所有 worlds 使用同 backend：

$$
M_b,
$$

就可能共享：

$$
D_{\mathrm{model}}.
$$

所以真正 audit 應看：

$$
N_{\mathrm{independent\ assumptions}}
$$

而不是只看 $N_{\mathrm{world}}$。

---

# 90. 現有研究接口

2025 的 SimuRA 已讓 agent 利用 world model 模擬候選 action 後果再規劃；model-based web-agent 研究也明確提出在不可逆 web action 前先用 world model deliberation。

2025 的 FLIP、AdaWorld 等工作把 learned world models 用於 long-horizon interactive planning。

2025 Agent2World 類研究則生成 symbolic／executable world models，再透過 simulation-based testing 驗證。

2026 Gamma-World 已開始處理多個 independently controllable agents 與 shared interactive world 的 real-time rollout。

2025–2026 digital-twin + agent-based simulation 工作則已實作 real-time state ingestion、scenario instantiation、alternative configuration comparison 與 decision support。

這些工作提供了 SWFR 的現實技術接口，但本文新增的是 world-family identity、typed relation、asymmetry、non-duality、authority、evidence transport 與 scheduler 的統一。

---

# 91. MVP

第一版甚至不必自己寫 game engine。

可以使用 Godot、Unity 或 Unreal 任一現成 backend，加上：

1. `world_registry`
2. `world_heads`
3. `snapshot_store`
4. `lineage_edges`
5. `interaction_edges`
6. `observer_plugins`
7. `authority_matrix`
8. `evidence_matrix`
9. `world_family_scheduler`
10. `world_audit`

---

# 92. MVP 世界族

建立：

$$
W_0
\rightarrow
W_1,W_2,W_3,W_4.
$$

四個 branches 分別：

$$
Policy_A,
Policy_B,
Policy_C,
NoAction.
$$

全部 headless run。

---

# 93. AI 不看影片

AI 可以直接讀：

$$
\mathcal O_{\mathrm{risk}}(W_i),
$$

$$
\mathcal O_{\mathrm{cost}}(W_i),
$$

$$
\mathcal O_{\mathrm{causal}}(W_i).
$$

人需要時才 render 3D。

---

# 94. Nested MVP

讓 $W_1$ 中 local agent 建立：

$$
W_{1,1}.
$$

測試：

- parent observation；
- child blindness；
- authority firewall；
- cross-world provenance。

---

# 95. Evidence MVP

simulation result：

$$
e_i^{sim}
$$

只能進：

$$
SimEvidenceStore,
$$

不能自動進：

$$
RealEvidenceStore.
$$

---

# 96. Scheduler MVP

先用 heuristic：

$$
Score_i
=
\alpha Q_i
+
\beta V_i
+
\gamma V_{\mathrm{ce},i}
-
\delta C_i.
$$

後續再考慮 learned scheduler。

---

# 97. Scheduler 也不能 Ambient Authority

WFS 可以建議 prune、pause、fork。

高風險 destructive operation 仍應經 governor／authority gate。

---

# 98. 可實驗研究

本文提出至少八類實驗：

1. single-world vs world-family planning；
2. asymmetric observation；
3. authority separation；
4. shared-backend evidence illusion；
5. catastrophic counterexample world；
6. adaptive pruning；
7. multi-fidelity world family；
8. nested simulation depth。

---

# 99. 本文不主張什麼

本文不主張 simulated worlds 是平行宇宙，也不賦予它們自動本體地位。

本文不主張 world 數越多越接近真理，不主張 simulation consensus 等於 reality validation，也不主張 higher-level agent 自動擁有 lower-level 全權。

本文不把 SWFR 等同 tree search、model-based RL、digital twin、game engine、video world model 或 LLM world model。

它是一個統合 runtime 抽象。

---

# 100. 核心命題總結

$$
\boxed{
\text{Game Engine}
\supset
\text{World Execution}
+
\text{Projection Operators}.
}
$$

$$
\boxed{
\mathfrak W
=
\{W_0,W_1,\ldots,W_n\}.
}
$$

$$
\boxed{
G_{\mathfrak W}
=
(V_{\mathfrak W},E_{\mathfrak W}).
}
$$

$$
\boxed{
\Pi^{-1}
\text{ need not exist}.
}
$$

$$
\boxed{
\mathsf{Observe}
\neq
\mathsf{Control}^{-1}.
}
$$

$$
\boxed{
O_{ij}\neq O_{ji},
\qquad
A_{ij}\neq A_{ji}.
}
$$

$$
\boxed{
K_{ij}\neq K_{ji},
\qquad
E_{ij}\neq E_{ji}.
}
$$

$$
\boxed{
\text{World Count}
\neq
\text{Independent Evidence Count}
\neq
\text{Truth}.
}
$$

$$
\boxed{
\mathcal P_{AI}(t)
=
\{
\mathcal O_{i,k}(W_i)
\}_{i,k}.
}
$$

---

# 101. 結論

人類通常是在一個世界裡想像很多可能。

傳統 AI 也常把「如果怎樣」寫成一段 token sequence。

未來 AI 可以再往前一步：

$$
\boxed{
\text{hypothesis}
\rightarrow
\text{runnable world}.
}
$$

它可以真正建立：

$$
W_1,W_2,\ldots,W_n,
$$

讓每個 world 擁有自己的 state、clock、agents、causal evolution、projection operators、authority boundary、evidence semantics 與 lineage。

AI 的 perception 也不必是一個 viewport。

它可以同時問：

$$
\mathcal O_{\mathrm{risk}},
\quad
\mathcal O_{\mathrm{causal}},
\quad
\mathcal O_{\mathrm{goal}},
\quad
\mathcal O_{\mathrm{counterexample}}
$$

作用在整個：

$$
\mathfrak W_t.
$$

因此真正 AI-native 的「多重世界觀察」不是科幻式觀看平行宇宙。

它是一個很明確的計算機架構：

$$
\boxed{
\text{one AI}
\rightarrow
\text{many runnable worlds}
\rightarrow
\text{many typed observation operators}.
}
$$

而且 world relations 天然不必對偶、不必對稱。

AI 能觀察 child world，不代表 child 能觀察 AI。

AI 能 pause simulation，不代表 simulation agent 能 pause parent。

兩個不同 worlds 甚至可以在同一 projection 下完全相同，因此 projection 不能唯一恢復 world。

這就是：

$$
\boxed{
\text{non-dual}
+
\text{asymmetric}
+
\text{typed world-family computation}.
}
$$

遊戲引擎提供了工程起點。

下一代則應從：

> 「一個虛擬世界給玩家玩」

升級成：

> **「一個 AI 可以生成、運行、觀察、嵌套、比較、修剪與治理一整個模擬世界族。」**

---

# 102. 兩篇工程延伸總接口

Paper 01：

$$
\boxed{
M
\rightarrow
P^\ast
\rightarrow
u
\rightarrow
\Phi
\rightarrow
\widehat P.
}
$$

Paper 02：

$$
\boxed{
\mathfrak W
=
\{W_0,\ldots,W_n\},
\qquad
\mathcal P_{AI}
=
\{\mathcal O_{i,k}(W_i)\}.
}
$$

兩篇合起來：

$$
\boxed{
\text{World Family}
\rightarrow
\text{Observation Operator}
\rightarrow
\text{Projection Compiler}
\rightarrow
\text{Carrier}
\rightarrow
\text{Observer}.
}
$$

---

# 參考文獻與內部依賴

1. Neo.K (2026). 《PPOE Paper 01：物理投影—觀察工程》.
2. Neo.K (2026). *WDC-01 / Branching World Computation foundations*.
3. Neo.K (2026). *WDC-02: Clone, Fork, Replay, and Counterfactual Branch semantics*.
4. Neo.K (2026). *WDC-03: World Generation and Governance separation*.
5. Neo.K (2026). *WDC-04: Nested Agents and Observer Separation*.
6. Neo.K (2026). *WDC-05: Cross-World Evidence*.
7. Neo.K (2026). *HDUS Multi-World Recursive World Runtime*.
8. Neo.K (2026). *PNCW Paper 08: Projection-Native Perception–Action Loop*.
9. Neo.K (2026). *HDUS Architecture Constitution v0.1*.
10. Deng, M., Hou, J., Shen, Y., et al. (2025). *SimuRA: Towards General Goal-Oriented Agent via Simulative Reasoning Architecture with LLM-Based World Model*. arXiv:2507.23773.
11. Gu, Y., Zhang, K., Ning, Y., et al. (2025). *Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents*. Transactions on Machine Learning Research.
12. Gao, C., Zhang, H., Xu, Z., et al. (2025). *FLIP: Flow-Centric Generative Planning as General-Purpose Manipulation World Model*. ICLR 2025.
13. Gao, S., Zhou, S., Du, Y., Zhang, J., & Gan, C. (2025). *AdaWorld: Learning Adaptable World Models with Latent Actions*. ICML 2025.
14. Hu, M., Xia, B., Wu, Y., et al. (2025). *Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback*. arXiv:2512.22336.
15. Liu, F., He, K., Shen, T., et al. (2026). *Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players*. arXiv:2605.28816.
16. Yeung, T., Martinez Ribon, J. G. T., Schlenger, J., et al. (2025). *Integrating digital twin and agent-based simulation to support adaptive production system design in building projects*. Automation in Construction, 180, 106550.

---

**Paper 02 狀態：COMPLETE v0.1**  
**兩篇工程延伸狀態：COMPLETE**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
