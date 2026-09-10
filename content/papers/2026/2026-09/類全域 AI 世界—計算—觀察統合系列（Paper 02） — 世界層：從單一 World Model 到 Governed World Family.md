# 類全域 AI 世界—計算—觀察統合系列（Paper 02）
## 世界層：從單一 World Model 到 Governed World Family
### The World Layer: From a Single World Model to a Governed World Family

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 02 / 12  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** MWT × GSWUE × WDC/BWC × SWFR × Digital Twin × Counterfactual Simulation × World Identity × Evidence Transport × Governance  
**前篇：** Paper 01《類全域 AI 的世界—計算—觀察三重族》  
**狀態：** 世界層母規格／形式與工程架構；不宣稱 simulated worlds 等同物理平行宇宙，不宣稱單一 world-model 技術已足以實作本文完整架構

---

## 摘要

世界模型（world model）已成為當代 AI、機器人、model-based reinforcement learning、web agent 與 Physical AI 的重要抽象。它讓智能系統不只對當前 observation 作出反應，而能維持某種內部狀態、預測 action consequence、執行 rollout，並在真正 commit 前比較候選未來。然而，若研究目標進一步提升為長時程、跨域、可驗證、可治理的類全域 AI，將「世界層」簡化成一個單一 world model：

$$
W_t
$$

仍然不夠。

一個成熟系統可能同時需要：

- 與現實持續耦合的 actual-linked reconstruction；
- 多個 digital twins；
- alternative simulation worlds；
- counterfactual worlds；
- replay worlds；
- synthetic benchmark worlds；
- nested worlds；
- 由不同模型、資料、假設與 resolution 支撐的競爭性 worlds。

因此本文提出 **Governed World Family（GWF，受治理世界族）**，作為 WCO-TF 中正式的 World Layer：

$$
\boxed{
\mathfrak W_t^{G}
=
\left(
V_t,
G_t^{lin},
G_t^{int},
\mu_t,
\mathbf O_t,
\mathbf A_t,
\mathbf K_t,
\mathbf E_t,
\mathbf L_t,
\mathcal H_t,
\mathcal Q_t,
\mathcal B_t,
\mathcal G_t
\right).
}
$$

其中：

- $V_t$：world nodes；
- $G_t^{lin}$：lineage graph；
- $G_t^{int}$：interaction graph；
- $\mu_t$：world-mode map；
- $\mathbf O_t$：observation-access relations；
- $\mathbf A_t$：authority relations；
- $\mathbf K_t$：causal-coupling relations；
- $\mathbf E_t$：evidence-transport relations；
- $\mathbf L_t$：reality-link relations；
- $\mathcal H_t$：history / provenance；
- $\mathcal Q_t$：epistemic weights / plausibility state；
- $\mathcal B_t$：resource / fidelity budgets；
- $\mathcal G_t$：world-family governance state。

本文將單一 world node 定義為：

$$
\boxed{
W_i
=
\left\langle
Id_i,
S_i,
\Phi_i,
T_i,
\mathcal A_i,
\mathcal E_i,
\mu_i,
\Lambda_i,
\Gamma_i,
H_i,
R_i
\right\rangle.
}
$$

其中 $Id_i$ 是不可被 rendering 或 snapshot 取代的 world identity； $S_i$ 為 state； $\Phi_i$ 為 transition law； $T_i$ 為 local time； $\mathcal A_i$ 為 local agents； $\mathcal E_i$ 為 evidence / event state； $\mu_i$ 為 world mode； $\Lambda_i$ 為 reality-link contract； $\Gamma_i$ 為 governance / authority boundary； $H_i$ 為 lineage / history； $R_i$ 為 resource / resolution state。

本文承接既有 WDC／SWFR 的重要非同一性：

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

以及 MWT 的：

$$
\boxed{
\text{Presentation}
\neq
\text{World}.
}
$$

本文進一步把它們提升成 World Layer Constitution。

第一，**world identity 不由 snapshot、render、backend、model weights 或 state equality 單獨決定**。兩個 worlds 即使 state 相同，也可以因 lineage、authority、history 或 mode 不同而保持不同 identity：

$$
S(W_i)=S(W_j)
\not\Rightarrow
W_i=W_j.
$$

第二，**lineage 與 interaction 必須分圖**。Fork、clone、merge 描述 world ancestry；Observe、Query、Communicate、Control、TransportEvidence 則描述 runtime interaction。Ancestor relation 不推出 observation access，也不推出 authority。

第三，**world-to-world relation 天然可以非對稱且非對偶**。一般不要求：

$$
O_{ij}=O_{ji},
$$

$$
A_{ij}=A_{ji},
$$

$$
K_{ij}=K_{ji},
$$

$$
E_{ij}=E_{ji}.
$$

也不要求 projection、observation 或 action 存在逆元。Master runtime 可以觀察、pause 或 fork child world，而 child agent 不需要知道 parent 存在。

第四，**world multiplicity 不等 evidence multiplicity**。不同 WorldId、不同 render、不同 post-fork trajectory 都不能自動當成獨立證據來源：

$$
\boxed{
\text{Different World IDs}
\not\Rightarrow
\text{Independent Evidence}.
}
$$

World evidence dependence 至少需要追蹤 ancestry、model、data、randomness、evaluator、provider、infrastructure、communication 與 evidence transport。

第五，**reality link 是 typed contract，不是 identity relation**。Digital twin、actual-linked world 與 physical reality 之間的同步只能表示：

$$
\mathcal R
\xrightarrow{\mathsf{Sense}}
W^{AL},
$$

或：

$$
W^{AL}
\xrightarrow{\mathsf{Proposal}}
\mathcal R,
$$

不能推出：

$$
W^{AL}=\mathcal R.
$$

第六，**simulation result 不直接沉積為歷史**。只有經過 authority gate 的 real action 及其真正 observation consequence 才能更新 parent historical state。本文因此保留 WDC-08 的核心：

$$
\boxed{
\text{Computed Future}
\neq
\text{Actual Future}.
}
$$

第七，**world lifecycle 必須可治理**。World 可以被 create、admit、fork、pause、resume、reobserve、merge、prune、archive、reopen 或 terminate；但 `prune` 不等於「證明不可能」，`pause` 不等於「失效」，`merge` 不等於 identity collapse，而 `delete` 也不應與 logical pruning 混為一談。

本文最後定義 **World Constitution Contract（WCC）**：

$$
\boxed{
\mathsf{WCC}(W_i)
=
\left\langle
Identity,
Mode,
State,
Dynamics,
Clock,
Lineage,
RealityLink,
Observation,
Authority,
Evidence,
Resources,
Lifecycle,
Audit
\right\rangle.
}
$$

只要一個 world 要進入類全域 AI 的正式 world family，就必須至少能回答：

1. 它是誰？
2. 它從哪裡來？
3. 它是哪一種 world mode？
4. 它依什麼 dynamics 演化？
5. 誰能看它？
6. 誰能改它？
7. 它與現實有什麼關係？
8. 它的結果可被當成哪一級 evidence？
9. 它和其他 worlds 有哪些依賴？
10. 它何時可以 fork、merge、prune、reopen 或終止？

因此本文的核心結論是：

$$
\boxed{
\text{A Global-Like AI does not merely maintain a world model;}
}
$$

$$
\boxed{
\text{it maintains a governed family of typed,
versioned, evidentially scoped, and authority-bounded worlds.}
}
$$

**關鍵詞：** Governed World Family、World Identity、World Lineage、Digital Twin、Counterfactual World、Runnable World、Evidence Transport、World Governance、SWFR、WDC、MWT、Global AI

---

# 0. Paper 01 留下的 World Layer 問題

Paper 01 定義：

$$
\mathfrak T_t
=
(
\mathfrak W_t,
\mathfrak C_t,
\mathfrak O_t
).
$$

其中：

$$
\mathfrak W_t
$$

只是先被指定為 world family。

但還沒有完整回答：

> 什麼東西有資格叫 World？

> 兩個 state 相同的 worlds 是否同一？

> fork 與 clone 有何不同？

> simulation result 可以怎麼回到 reality？

> 哪些 world 可以互相看見？

> 哪些 world 可以互相控制？

> 如何避免 100 個 branches 被誤認成 100 份 independent evidence？

本文專門解決這些問題。

---

# 1. World 必須是 Primitive-like Runtime Object

本文承接 MWT：

$$
\boxed{
\mathbf W
\text{ is primitive-like at the framework level}.
}
$$

意思不是禁止分析 World。

而是：

> 不把 World 強制還原成任何單一 presentation、state vector、graph、simulation engine、tensor 或 database row。

---

# 2. World 不由 Representation 定義

如果：

$$
\rho(W)
$$

是 world presentation，

一般：

$$
\boxed{
\rho(W)
\not\equiv
W.
}
$$

---

# 3. World 不等 Rendering

$$
\boxed{
\text{World}
\neq
\text{Rendered Scene}.
}
$$

同一 world 可被 render 成：

- 3D scene；
- 2D map；
- graph；
- table；
- causal structure；
- symbolic state；
- AI-native representation。

---

# 4. World 不等 Snapshot

$$
\boxed{
WorldSnapshot
\neq
World.
}
$$

snapshot 是：

$$
\sigma_t(W).
$$

它只固定某一時刻或 checkpoint 的部分 state。

---

# 5. World 不等 Backend

如果：

$$
Backend(W)=Unity,
$$

後來 migration 成：

$$
Backend(W)=Godot,
$$

不能因此自動推出：

$$
W_{\mathrm{before}}
\neq
W_{\mathrm{after}}.
$$

是否維持 identity 要由 explicit migration / invariants 判定。

---

# 6. World 不等 World Model Weights

一個 learned dynamics model：

$$
M_\theta
$$

可以被多個 worlds 共用。

因此：

$$
\boxed{
ModelIdentity
\neq
WorldIdentity.
}
$$

---

# 7. World 的最小正式記錄

本文定義：

$$
\boxed{
W_i
=
\left\langle
Id_i,
S_i,
\Phi_i,
T_i,
\mathcal A_i,
\mathcal E_i,
\mu_i,
\Lambda_i,
\Gamma_i,
H_i,
R_i
\right\rangle.
}
$$

---

# 8. $Id_i$

World identity。

它不能只是 filename 或 scene name。

需要：

- stable identifier；
- version lineage；
- creation event；
- parent relationship；
- identity specification。

---

# 9. $S_i$

world state。

可以是：

- symbolic；
- graph；
- tensor；
- database state；
- physics state；
- hybrid state。

---

# 10. $\Phi_i$

transition law family。

可以是：

$$
S_{t+1}
=
\Phi_i(S_t,A_t,E_t).
$$

也可以是 stochastic / continuous / hybrid。

---

# 11. $T_i$

world-local time。

一般不要求：

$$
T_i=T_j.
$$

---

# 12. $\mathcal A_i$

world-local agents。

local agent 不自動擁有 global observer knowledge。

---

# 13. $\mathcal E_i$

world-local evidence / event state。

它與 real evidence 必須分開。

---

# 14. $\mu_i$

world modality。

本文暫定：

$$
\mu_i
\in
\{
AL,
DT,
SIM,
CF,
RP,
SYN,
NST
\}.
$$

---

# 15. $AL$ — Actual-Linked

與真實系統保持 observation/update link 的 reconstruction。

但：

$$
\boxed{
W^{AL}
\neq
\mathcal R.
}
$$

---

# 16. $DT$ — Digital Twin

具更強 synchronization／asset correspondence contract 的 actual-linked world。

Digital twin 仍不是 physical twin。

---

# 17. $SIM$ — Simulation

在指定模型、初值、policy、seed 下執行的 runnable world。

---

# 18. $CF$ — Counterfactual

由明確 intervention：

$$
\operatorname{do}(X=x')
$$

或 equivalent intervention contract 建立的 world。

---

# 19. $RP$ — Replay

主要重播：

$$
H_{0:t}.
$$

不預設改變過去條件。

---

# 20. $SYN$ — Synthetic

沒有必要 real ancestor 的人工世界。

例如 benchmark、game、formal toy world。

---

# 21. $NST$ — Nested

由另一 world 的 local agent 或 runtime 建立的 child simulation。

---

# 22. World Mode 不等 Epistemic Status

一個 world 是：

$$
SIM
$$

並不自動表示「低品質」。

一個：

$$
DT
$$

也不自動表示「真」。

所以：

$$
\boxed{
\text{World Mode}
\neq
\text{Epistemic Quality}.
}
$$

---

# 23. $\Lambda_i$ — Reality-Link Contract

本文把 world 與 reality 的關係獨立成：

$$
\Lambda_i.
$$

---

# 24. Reality Link 的最小方向

至少分：

$$
\Lambda_{\mathcal R\rightarrow W}
$$

與：

$$
\Lambda_{W\rightarrow\mathcal R}.
$$

---

# 25. Sense Link

$$
\mathcal R
\xrightarrow{\mathsf{Sense}}
W.
$$

可以持續更新 state estimate。

---

# 26. Actuation Link

$$
W
\xrightarrow{\mathsf{Proposal}}
\mathcal R.
$$

但 proposal 不等 authorized actuation。

---

# 27. Reality Link 可以非對稱

常見安全配置：

$$
\Lambda_{\mathcal R\rightarrow W}
\gg
\Lambda_{W\rightarrow\mathcal R}.
$$

也就是：

> 看得多，動得少。

---

# 28. Reality Link 不產生本體同一

$$
\boxed{
\Lambda(W,\mathcal R)>0
\not\Rightarrow
W=\mathcal R.
}
$$

---

# 29. $\Gamma_i$ — Governance / Authority Boundary

它定義：

- who may read；
- who may write；
- who may fork；
- who may pause；
- who may terminate；
- who may export evidence；
- who may propose real action。

---

# 30. $H_i$ — History / Lineage

如果歷史會影響未來可達性：

$$
\boxed{
\text{State Equality}
\not\Rightarrow
\text{History Equality}.
}
$$

---

# 31. $R_i$ — Resource / Resolution State

world 不一定全時 full fidelity。

可以有：

$$
r_i(t).
$$

---

# 32. World Identity Specification

本文定義：

$$
\mathsf{IdSpec}(W)
=
\left(
\mathcal I,
\mathcal H,
\mathcal G,
\mathcal M
\right).
$$

其中：

- $\mathcal I$：required invariants；
- $\mathcal H$：history conditions；
- $\mathcal G$：governance continuity；
- $\mathcal M$：mode / migration rules。

---

# 33. State 相同不推出 World 相同

$$
S_i=S_j
$$

一般不推出：

$$
W_i=W_j.
$$

---

# 34. Restore 會產生什麼？

如果：

$$
Restore(C_0)
\rightarrow
W_a,
$$

再次 restore：

$$
Restore(C_0)
\rightarrow
W_b,
$$

可以有：

$$
S(W_a)=S(W_b),
$$

但：

$$
Id(W_a)\neq Id(W_b).
$$

這對 lineage audit 更乾淨。

---

# 35. Clone

Clone 先表示：

$$
CopyState(W,t).
$$

它是 state-level operation。

---

# 36. Fork

Fork 表示：

$$
W
\xrightarrow{\mathsf{Fork}}
W'.
$$

 $W'$ 取得：

- new WorldId；
- parent reference；
- fork checkpoint；
- divergence contract。

---

# 37. Fork Certificate

$$
\boxed{
\mathsf{ForkCert}
=
\left(
ParentId,
Checkpoint,
ForkTime,
Divergence,
Mode,
Authority,
Purpose
\right).
}
$$

---

# 38. Clone 不必自動成為 Fork

只是 memory copy：

$$
Clone(S)
$$

不等於：

$$
AdmitWorld(Clone(S)).
$$

---

# 39. Replay

Replay 指：

$$
\mathsf{Replay}(W,H_{0:t}).
$$

它可能產生新的 execution instance，但不應冒充 counterfactual。

---

# 40. Counterfactual Branch

$$
W
\xrightarrow{\operatorname{do}(X=x')}
W^{CF}.
$$

需要明確記錄：

$$
InterventionSet.
$$

---

# 41. Replay 與 Counterfactual 的核心差異

Replay 問：

> 原來發生過什麼？

Counterfactual 問：

> 若指定條件不同，這個模型會如何演化？

---

# 42. Future Candidate 不等 Runnable World

想法：

$$
F_i
$$

只有在通過 admission 後才成為：

$$
W_i.
$$

---

# 43. World Admission

本文定義：

$$
\mathsf{AdmitWorld}(c)
\rightarrow
W_i
$$

需要至少通過：

- schema；
- identity；
- dynamics；
- mode；
- authority；
- provenance；
- resource；
- lifecycle。

---

# 44. Candidate World 不等 Admitted World

$$
\boxed{
\text{Candidate World}
\neq
\text{Admitted World}.
}
$$

---

# 45. World Family

正式 world nodes：

$$
V_t
=
\{W_i\}.
$$

---

# 46. 但 World Family 不只是 Set

必須加入關係：

$$
\boxed{
\mathfrak W_t^{G}
=
(
V_t,
G_t^{lin},
G_t^{int},
\ldots
).
}
$$

---

# 47. Lineage Graph

$$
G_t^{lin}
=
(V_t,E_t^{lin}).
$$

Edge type 包括：

- fork；
- clone-admit；
- merge；
- restore；
- relift；
- migration。

---

# 48. Lineage Graph 應盡量保持可審計

特別對 fork / restore：

$$
\text{state recurrence}
$$

不應讓 lineage cycle 消失。

---

# 49. Interaction Graph

$$
G_t^{int}
=
(V_t,E_t^{int}).
$$

Edge type 可包括：

- observe；
- query；
- communicate；
- control；
- transport evidence；
- synchronize；
- actuate。

---

# 50. Lineage Graph 不等 Interaction Graph

$$
\boxed{
G^{lin}
\neq
G^{int}.
}
$$

---

# 51. Ancestor 不等 Observer

$$
Ancestor(W_i,W_j)
$$

不推出：

$$
CanObserve(W_i,W_j).
$$

---

# 52. Sibling 不等 Communication

$$
Sibling(W_i,W_j)
$$

不推出：

$$
CanCommunicate(W_i,W_j).
$$

---

# 53. Branch Blindness

child world local agent 可以只看到：

$$
K_i^{local}.
$$

不需要看到 sibling branches。

---

# 54. Meta-Observer Access

外部 evaluator 可以：

$$
Observe(W_1,\ldots,W_n).
$$

但：

$$
\boxed{
\text{Meta-Observer Access}
\neq
\text{In-World Communication}.
}
$$

---

# 55. Cross-Branch Contamination

如果 sibling worlds 執行中交換資訊：

$$
W_i
\leftrightarrow
W_j,
$$

必須記錄：

$$
CommunicationEdge.
$$

因為 evidence dependence 已改變。

---

# 56. Observation Relation

定義：

$$
O_{ij}.
$$

它可以是 boolean、graded 或 typed permission。

---

# 57. Authority Relation

$$
A_{ij}^{(d)}
$$

依 domain $d$ 分開。

例如：

- read；
- pause；
- write；
- fork；
- terminate；
- evidence export；
- real action proposal。

---

# 58. Causal Coupling Relation

$$
K_{ij}.
$$

它表示 world $i$ 的 state/event 能否真正改變 world $j$。

---

# 59. Evidence Transport Relation

$$
E_{ij}.
$$

它表示：

> $W_i$ 的什麼結果，可用什麼 status 進入 $W_j$ 的 evidence state？

---

# 60. 四種 Relation 不得合併

$$
\boxed{
O_{ij},
A_{ij},
K_{ij},
E_{ij}
}
$$

是四種不同語義。

---

# 61. Observation 不等 Authority

$$
\boxed{
O_{ij}>0
\not\Rightarrow
A_{ij}>0.
}
$$

---

# 62. Authority 不等 Knowledge

某 governor 可以有 terminate permission，

但：

$$
\boxed{
\text{Authority}
\neq
\text{Omniscience}.
}
$$

---

# 63. Causality 不等 Evidence

一個 world 可以因果影響另一個，

但該 effect 不必自動成為可信 evidence。

---

# 64. Evidence 不等 Communication

external evidence aggregator 可以比較 worlds，

不代表 worlds 彼此通信。

---

# 65. 非對稱 World Relations

一般：

$$
\boxed{
O_{ij}\neq O_{ji},
}
$$

$$
\boxed{
A_{ij}\neq A_{ji},
}
$$

$$
\boxed{
K_{ij}\neq K_{ji},
}
$$

$$
\boxed{
E_{ij}\neq E_{ji}.
}
$$

---

# 66. 非對偶 World Relations

如果：

$$
\Pi(W)=P,
$$

不保證存在：

$$
\Pi^{-1}(P)=W.
$$

同樣：

$$
\mathsf{Act}
$$

不必有完全 undo。

---

# 67. World Family 是 Directed Typed Structure

所以它不只是：

$$
\{W_i\}.
$$

而是：

$$
\boxed{
\text{typed directed relational world system}.
}
$$

---

# 68. World Lineage 與 Evidence Independence

不同 WorldIds：

$$
W_i\neq W_j
$$

不推出：

$$
E_i\perp E_j.
$$

---

# 69. Shared Ancestry

siblings 可能共享：

- parent state；
- dynamics model；
- hidden parameter error；
- training data；
- evaluator；
- infrastructure。

---

# 70. Evidence Dependency Vector

本文提出：

$$
\boxed{
\mathbf D_{ij}^{evid}
=
(
D_{anc},
D_{model},
D_{data},
D_{rng},
D_{eval},
D_{provider},
D_{infra},
D_{comm},
D_{transport}
).
}
$$

---

# 71. Lineage Distance 不是 Independence

$$
\boxed{
d_{lin}(W_i,W_j)
\not\Rightarrow
I_{\mathrm{evid}}(W_i,W_j).
}
$$

---

# 72. World Count 不等 Effective Sample Size

$$
N_{world}
$$

只能是執行數量。

有效 evidence multiplicity 另行估計。

---

# 73. World Family 可以刻意共享 Noise

例如 paired counterfactual。

這種 dependence 不是錯誤。

只要明確標記。

---

# 74. Common-Mode Failure

真正危險的是：

$$
100
$$

個 worlds 都共享同一錯誤模型，

卻因結果一致被誤認為 robustness。

---

# 75. World Evidence Ledger

每個 world result 需要：

$$
\mathsf{WEL}
=
\left(
WorldId,
Model,
Data,
Seed,
Evaluator,
Provider,
Ancestor,
Comm,
Transport,
Result
\right).
$$

---

# 76. World Mode 與 Evidence Type

本文建議：

$$
EvidenceType
\in
\{
Observed,
Simulated,
Counterfactual,
ReplayDerived,
Synthetic,
Imported
\}.
$$

---

# 77. Simulated Evidence 不等 Reality Evidence

$$
\boxed{
E^{sim}
\neq
E^{real}.
}
$$

---

# 78. World Evidence Transport Contract

$$
\boxed{
\mathsf{ETC}_{i\rightarrow j}
=
(
SourceMode,
TargetMode,
Scope,
Transform,
Loss,
Independence,
Validation,
Expiry
).
}
$$

---

# 79. Reality Transport

從 simulation 到 reality-facing decision：

$$
W^{sim}
\rightarrow
Proposal.
$$

不能直接：

$$
W^{sim}
\rightarrow
HistoricalFact.
$$

---

# 80. Actual History Sedimentation

承接 WDC-08：

$$
\boxed{
\text{Real Action}
+
\text{Real Consequence}
\rightarrow
\text{Next Historical State}.
}
$$

---

# 81. Computed Future 不等 Actual Future

$$
\boxed{
\text{Computed Future}
\neq
\text{Actual Future}.
}
$$

---

# 82. World Family 不得封閉學習現實

如果只：

$$
\mathfrak W
\rightarrow
\mathfrak W
$$

沒有新 external evidence，

長期可能形成 epistemic self-sealing。

---

# 83. Reality Re-entry

需要：

$$
\mathcal R_{t+1}
\xrightarrow{\mathsf{Sense}}
W_{t+1}^{AL}.
$$

---

# 84. Reality Re-entry 可能推翻整個 World Family

新 evidence 可以：

- reweight；
- invalidate；
- reopen；
- fork；
- retire；

既有 worlds。

---

# 85. Reality Link Freshness

對 actual-linked world：

$$
Age(W)
=
t_{now}-t_{last\_sync}.
$$

---

# 86. Stale World

若：

$$
Age(W)>\theta_{fresh},
$$

world 應標記：

$$
STALE.
$$

---

# 87. Digital Twin 不是永遠同步

因此：

$$
\boxed{
\text{Digital Twin}
\neq
\text{Perfect Live Mirror}.
}
$$

---

# 88. World Freshness 也是 Epistemic Metadata

它不能只被藏在 backend log。

---

# 89. Merge 問題

如果：

$$
W_A,W_B
$$

需要合併，

最安全語義通常不是：

$$
W_A=W_B.
$$

---

# 90. Merge Descendant

建立：

$$
\boxed{
W_C
=
\mathsf{MergeDescendant}(W_A,W_B).
}
$$

並給新 WorldId。

---

# 91. Merge Certificate

$$
\boxed{
\mathsf{MergeCert}
=
(
Parents,
ConflictSet,
MergeRule,
PreservedInvariants,
DroppedState,
Authority,
Debt
).
}
$$

---

# 92. Merge 不一定可行

如果：

- histories incompatible；
- irreversible side effects conflict；
- identity invariants conflict；
- authority forbids；

則：

$$
\mathsf{Merge}
\downarrow
$$

可以是 false。

---

# 93. Merge 不應偷偷抹掉衝突

如果：

$$
Conflict(W_A,W_B)\neq\varnothing,
$$

應顯式保留 conflict set。

---

# 94. Branch Preservation

承接 MWT：

$$
\boxed{
\text{legal incompatible branches}
\text{ need not be forcibly homogenized}.
}
$$

---

# 95. Convergence Without Homogenization

收斂可以是：

$$
\mathfrak W^\ast
=
\{W_a,W_b,W_c\}
$$

而不是：

$$
W^\ast.
$$

---

# 96. Plural Stable Worlds

在 evidence 尚不足時：

$$
\boxed{
\text{Plural Stable World Family}
}
$$

可以是合法暫時終態。

---

# 97. Prune

World Family 不能無限 expansion。

因此：

$$
\mathsf{Prune}(W_i).
$$

---

# 98. Prune 不是 Impossibility Proof

$$
\boxed{
\mathsf{Prune}
\neq
\mathsf{ProveImpossible}.
}
$$

---

# 99. Prune Reasons

可包括：

- low value；
- low plausibility；
- compute budget；
- domination；
- redundancy；
- stale model；
- policy retirement。

---

# 100. Logical Prune 不等 Delete

$$
\boxed{
\mathsf{Prune}
\neq
\mathsf{Delete}.
}
$$

---

# 101. Archive

pruned world 可以：

$$
\mathsf{Archive}(W_i)
$$

保留 lineage、certificate 與 reactivation info。

---

# 102. Reopen

如果新 evidence 出現：

$$
\mathsf{Reopen}(W_i).
$$

---

# 103. Reopenability 是 World Layer Constitution

一個 world 被 prune 只因 budget，

未來不應被永久冒充「已否定」。

---

# 104. Terminate

真正 terminate 可以表示：

- runtime instance stopped；
- no further execution；
- archived state preserved。

---

# 105. Destroy 不等 Forget

即使 execution 被終止：

$$
\boxed{
\text{Terminate}
\neq
\text{Erase History}.
}
$$

---

# 106. World Garbage Collection

大量 inactive branches 可以進：

$$
\mathsf{GC}_{world}.
$$

但 lineage metadata 不應同步消失。

---

# 107. World Lifecycle State

本文定義：

$$
\ell(W_i)
\in
\{
Candidate,
Admitted,
Active,
Paused,
Pruned,
Archived,
Reopened,
Terminated,
Invalidated
\}.
$$

---

# 108. Invalidated 與 Pruned 分離

Pruned：

> 現在不值得算。

Invalidated：

> 某必要依賴、模型、證據或 contract 已失效。

---

# 109. Invalidation Propagation

如果 shared model：

$$
M_v
$$

被 invalidated，

所有依賴 world：

$$
Dep(W_i,M_v)
$$

都應重新評估。

---

# 110. World Provenance DAG

需要：

$$
G_{\mathrm{prov}}.
$$

它記錄：

- world；
- model；
- data；
- checkpoint；
- evaluator；
- provider；
- external evidence。

---

# 111. Lineage DAG 不等 Provenance DAG

$$
\boxed{
G_{lin}
\neq
G_{prov}.
}
$$

---

# 112. World Constitution Contract

本文正式提出：

$$
\boxed{
\mathsf{WCC}(W_i)
=
\left\langle
Identity,
Mode,
State,
Dynamics,
Clock,
Lineage,
RealityLink,
Observation,
Authority,
Evidence,
Resources,
Lifecycle,
Audit
\right\rangle.
}
$$

---

# 113. WCC-I1：Identity

World 必須有可追蹤 identity。

---

# 114. WCC-I2：Mode

World modality 必須 explicit。

---

# 115. WCC-I3：State / Dynamics Separation

$$
S_i
\neq
\Phi_i.
$$

當前 state 與 transition law 不可混同。

---

# 116. WCC-I4：Clock

每個 world 的時間語義必須可查。

---

# 117. WCC-I5：Lineage

fork、merge、restore、migration 不得遺失 lineage。

---

# 118. WCC-I6：Reality Link

與 reality 的 observation / actuation relation必須顯式。

---

# 119. WCC-I7：Observation

誰可以看什麼必須是 contract。

---

# 120. WCC-I8：Authority

誰可以改什麼必須是 contract。

---

# 121. WCC-I9：Evidence Scope

每個 result 的 evidence status 不得由 display 自動決定。

---

# 122. WCC-I10：Resources

resolution、compute、latency 與 persistence budget 可查。

---

# 123. WCC-I11：Lifecycle

world 是否 active / paused / pruned / invalidated 必須明示。

---

# 124. WCC-I12：Audit

所有高影響 world transition 應能重放其依賴與證書。

---

# 125. Governed World Family 正式定義

$$
\boxed{
\mathfrak W_t^{G}
=
\left(
V_t,
G_t^{lin},
G_t^{int},
\mu_t,
\mathbf O_t,
\mathbf A_t,
\mathbf K_t,
\mathbf E_t,
\mathbf L_t,
\mathcal H_t,
\mathcal Q_t,
\mathcal B_t,
\mathcal G_t
\right).
}
$$

---

# 126. $\mu_t$

world modes。

---

# 127. $\mathbf O_t$

observation accessibility。

---

# 128. $\mathbf A_t$

authority matrix / typed relation set。

---

# 129. $\mathbf K_t$

causal coupling。

---

# 130. $\mathbf E_t$

evidence transport。

---

# 131. $\mathbf L_t$

reality-link graph。

---

# 132. $\mathcal H_t$

world history / provenance。

---

# 133. $\mathcal Q_t$

epistemic weights。

不要求一定是 probability。

---

# 134. $\mathcal B_t$

world budgets：

- compute；
- memory；
- fidelity；
- latency；
- lifetime。

---

# 135. $\mathcal G_t$

governance state。

---

# 136. World Governor

本文定義：

$$
\mathsf{Gov}_W.
$$

它負責：

- admission；
- identity；
- lifecycle；
- authority；
- lineage；
- evidence contracts；
- invalidation；
- reopenability。

---

# 137. World Governor 不等 World Scheduler

Governor 問：

> 允不允許？

Scheduler 問：

> 現在值不值得算？

---

# 138. WFS 只在本篇保留接口

$$
\mathsf{WFS}
:
(\mathfrak W_t^{G},\tau,B,\rho)
\rightarrow
\mathcal A_{sched}.
$$

詳細 routing 留給 Paper 09。

---

# 139. World Governor 不等 Global Observer

$$
\boxed{
\mathsf{Gov}_W
\neq
\mathsf{Observer}.
}
$$

---

# 140. Governor 可以無法看完整 world

它仍可以根據 certificate / metadata 管理 lifecycle。

---

# 141. World Admission Gate

$$
\boxed{
\operatorname{Admit}(W)
\iff
I
\land
M
\land
D
\land
G
\land
P
\land
R.
}
$$

概念上代表 identity、mode、dynamics、governance、provenance、resource contract 都通過。

---

# 142. High-Risk World Gate

如果 world 可產生：

$$
K_{W,\mathcal R}>0,
$$

需要更高 authority / safety requirements。

---

# 143. Pure Simulation World

如果：

$$
K_{W,\mathcal R}=0,
$$

可以允許更自由：

- time acceleration；
- rollback；
- hidden-state inspection；
- destructive experiments。

---

# 144. Reality-Coupled World

一旦有：

$$
K_{W,\mathcal R}>0,
$$

不能把 simulation rollback 語義套到 physical consequences。

---

# 145. Rollback Boundary

$$
\boxed{
\text{Rollback Computational State}
\neq
\text{Rollback Physical History}.
}
$$

---

# 146. World Family Time

不同 worlds：

$$
T_i\neq T_j.
$$

---

# 147. Time Rate

可以：

$$
\frac{dT_i}{dt_{wall}}
\neq1.
$$

---

# 148. Time Acceleration 不等 Future Access

simulation 跑快：

$$
\boxed{
\text{Fast Simulation}
\neq
\text{True Future Observation}.
}
$$

---

# 149. Cross-World Time Mapping

$$
\tau_{i\rightarrow j}:T_i\rightarrow T_j.
$$

需要標明 semantic basis。

---

# 150. World Family 可保持多個 Future Candidates

不需要：

$$
\arg\max_i q_i
$$

後立刻刪除其他 worlds。

---

# 151. World Portfolio

$$
\mathcal P_W
=
\{(W_i,q_i,c_i,v_i)\}.
$$

 $q_i$ 為 epistemic weight， $c_i$ 為 cost， $v_i$ 為 information / decision value。

---

# 152. World Portfolio 不等 Voting

$$
\boxed{
\text{World Aggregation}
\neq
\text{Majority Vote by Default}.
}
$$

---

# 153. Counterexample World

單一高風險 failure world 可以具有很高：

$$
V_{ce}(W_i).
$$

---

# 154. Catastrophic Tail

對 safety task：

$$
P(\text{catastrophe})
$$

可能比平均 utility 更重要。

---

# 155. World Diversity

至少分：

$$
\mathbf D_W
=
(
D_{model},
D_{param},
D_{policy},
D_{seed},
D_{data},
D_{evidence}
).
$$

---

# 156. Diversity 不等 Independence

$$
\boxed{
\text{Diversity}
\neq
\text{Independence}.
}
$$

---

# 157. Same Backend Worlds

可以提供 parameter exploration，

但不能被錯算成 independent replication。

---

# 158. Multi-Backend Worlds

不同 backend 可降低部分 common-mode risk，

但仍可能共享：

- data；
- objective；
- ontology；
- evaluator。

---

# 159. World Family Closure

何時可以暫時停止擴張？

不是：

$$
|\mathfrak W|=\infty.
$$

---

# 160. Local Closure

可以定義：

$$
\mathsf{Closure}_{\tau}
$$

表示當前 task 下：

- no unresolved high-value branch；
- required evidence threshold reached；
- remaining uncertainty below bound；
- budget rationally exhausted。

---

# 161. Local Closure 不等 Global Closure

$$
\boxed{
\text{Current Closure}
\neq
\text{Global Closure}.
}
$$

---

# 162. Closure Certificate

需要：

$$
\mathsf{CloseCert}
=
(
Task,
WorldSet,
Evidence,
Uncertainty,
Budget,
OpenGaps,
ReopenTriggers
).
$$

---

# 163. Reopen Trigger

例如：

- new evidence；
- model invalidation；
- ontology change；
- authority change；
- new observer；
- new computational method；
- world-mode reclassification。

---

# 164. Governed Plurality

本文不要求所有 worlds 最後合併成一個。

所以：

$$
\boxed{
\text{Governed Plurality}
\neq
\text{Unresolved Chaos}.
}
$$

只要：

- identity；
- relation；
- evidence；
- authority；
- lifecycle；

都可治理。

---

# 165. 類全域 AI 的 World Layer 不應只有「信哪個世界」

更重要的是：

> 哪些 worlds 必須保持 live？

> 哪些只是 archive？

> 哪些可以拿來做 decision？

> 哪些只適合反例搜尋？

> 哪些與 reality 維持同步？

---

# 166. 現有 World-Model 研究接口

2026 Physical AI world-model survey 將 world model 定義為用 observation/action history 預測未來 state、observation、reward 或 decision-relevant quantity 的 predictive model，並特別強調 partial observability、uncertainty、rollout error、planner exploitation、long-horizon consistency 與 sim-to-real。

這證明：

$$
\boxed{
\text{world model quality}
}
$$

本身已經是一個實際工程問題。

但本文的 World Layer 比單一 predictive model 多處理：

- identity；
- plurality；
- lineage；
- governance；
- cross-world evidence；
- lifecycle；
- reality transport。

---

# 167. Web-Agent 接口

2025 model-based web agents 已經顯示一個重要現實需求：

不可逆真實 action 前，可以先：

$$
a_i
\rightarrow
\widehat W_i
\rightarrow
\widehat o_{i,t+1}
$$

模擬候選後果再 commit。

本文把這種 pattern 擴張成 Governed World Family，而不是只做一次 action prediction。

---

# 168. Digital Twin 接口

Digital twin 已提供：

$$
\mathcal R
\leftrightarrow
W^{DT}
$$

的工程方向。

Governed World Family 再增加：

$$
W^{DT}
\rightarrow
\{W^{scenario}_1,\ldots,W^{scenario}_n\}.
$$

---

# 169. Game Engine 接口

Unity、Unreal、Godot 可直接作為部分 world backend。

但：

$$
\boxed{
\text{Game Engine}
\neq
\text{World Governance Layer}.
}
$$

---

# 170. MVP：四世界族

最小原型：

$$
W_0
\rightarrow
\{W_A,W_B,W_C,W_N\}.
$$

其中：

- $W_A$：Policy A；
- $W_B$：Policy B；
- $W_C$：Policy C；
- $W_N$：No Action。

---

# 171. MVP 必須有 WorldId

每個：

$$
W_i
$$

都有 stable WorldId。

---

# 172. MVP 必須有 Mode

所有四個：

$$
SIM
$$

不能冒充 actual-linked world。

---

# 173. MVP 必須有 Parent Lineage

共同 parent：

$$
W_0.
$$

---

# 174. MVP 必須有 Shared-Dependency Ledger

記錄共享：

- model；
- dataset；
- evaluator；
- seed family；
- infrastructure。

---

# 175. MVP 必須有 Observation Firewall

local branch 不知道 siblings。

---

# 176. MVP 必須有 Meta-Evaluator

外部 evaluator 可比較：

$$
W_A,W_B,W_C,W_N.
$$

---

# 177. MVP 必須有 Evidence Fence

world result 只能進：

$$
SimulationEvidence.
$$

不能直接：

$$
RealFactStore.
$$

---

# 178. MVP 必須有 Lifecycle

至少：

$$
Active,
Paused,
Pruned,
Archived,
Reopened.
$$

---

# 179. MVP 必須有 Reopen Test

先 prune：

$$
W_C.
$$

加入 new evidence，

要求：

$$
\mathsf{Reopen}(W_C).
$$

---

# 180. MVP 必須有 Merge Test

讓：

$$
W_A,W_B
$$

產生部分 compatible state，

建立：

$$
W_M
=
MergeDescendant(W_A,W_B).
$$

驗證新 WorldId 與 conflict set。

---

# 181. 實驗一：Identity Stress Test

建立 state-identical restored worlds：

$$
S_a=S_b.
$$

驗證系統仍追蹤不同 lineage。

---

# 182. 實驗二：Evidence Multiplicity Illusion

從同一 parent fork：

$$
100
$$

worlds。

測 AI 是否誤把 100 worlds 當 100 independent sources。

---

# 183. 實驗三：Sibling Contamination

允許部分 siblings 通信。

測 evidence dependence estimate 是否更新。

---

# 184. 實驗四：Stale Digital Twin

延遲 real sync。

測：

- decision degradation；
- stale-state detection；
- freshness warning。

---

# 185. 實驗五：Reality Transport Gate

讓 simulation 提出 action。

驗證不經：

$$
Authority
$$

無法產生 real actuation。

---

# 186. 實驗六：Prune / Reopen

測 budget pruning 後新 evidence 是否可恢復 world。

---

# 187. 實驗七：Plural Stable Worlds

建立兩個無法由目前 evidence 區分的 worlds。

驗證 runtime 不強迫：

$$
W_A=W_B
$$

或任意刪除其中一個。

---

# 188. 實驗八：Backend Migration

將 world backend：

$$
Engine_A
\rightarrow
Engine_B.
$$

測 invariants、identity、history 是否可維持。

---

# 189. 實驗九：Nested World Authority

讓 child agent 建立：

$$
W_{child}^{sim}.
$$

測 child simulation 不可未授權修改 parent。

---

# 190. 實驗十：Rollback Boundary

在 simulation rollback 後，

確認 real side effect 不會被誤標記成已 rollback。

---

# 191. 可反駁性

本文會被削弱，如果：

1. world identity 與 lineage 在代表性 multi-world tasks 中沒有任何可測價值；
2. mode separation 不降低 source confusion；
3. evidence-dependence tracking 不改善 calibration；
4. prune/reopen lifecycle 成本始終高於重新建立 world；
5. simpler single-world predictive state 在所有長時程、branching、counterfactual、multi-authority tasks 都同等有效；
6. world governance 層完全可以被一般 database transaction semantics 無損取代。

---

# 192. 本文不主張什麼

本文不主張：

1. simulated world 是物理平行宇宙；
2. actual-linked world 等於 reality；
3. digital twin 是 perfect mirror；
4. world identity 是自然界唯一正確本體概念；
5. 每個 AI 任務都需要 world family；
6. world 數量越多越好；
7. branches 彼此獨立；
8. different WorldId 等於 independent evidence；
9. counterfactual simulation 等於 causal proof；
10. simulation consensus 等於 truth；
11. governor 應擁有 complete observation；
12. higher-level world 應擁有 lower-level world 全部權力；
13. merge 永遠可行；
14. prune 表示 impossible；
15. archive 表示 irrelevant；
16. replay 可以改寫過去；
17. rollback 可以消除 real-world consequence；
18. local closure 等於 global closure；
19. SWFR、WDC、MWT 或 digital-twin literature 已完整實作本文 Governed World Family；
20. 本文已完成 production runtime。

---

# 193. World Layer 核心非同一性

$$
\boxed{
Reality
\neq
ActualLinkedWorld
\neq
DigitalTwin
\neq
SimulationWorld.
}
$$

$$
\boxed{
World
\neq
Snapshot
\neq
Render
\neq
Backend.
}
$$

$$
\boxed{
Clone
\neq
Fork
\neq
Replay
\neq
Counterfactual.
}
$$

$$
\boxed{
Lineage
\neq
Interaction
\neq
EvidenceDependence.
}
$$

$$
\boxed{
Observation
\neq
Authority
\neq
CausalCoupling
\neq
EvidenceTransport.
}
$$

$$
\boxed{
WorldCount
\neq
EvidenceCount
\neq
Truth.
}
$$

$$
\boxed{
Prune
\neq
Delete
\neq
Invalidate.
}
$$

$$
\boxed{
Merge
\neq
IdentityCollapse.
}
$$

---

# 194. Paper 02 核心母式

世界節點：

$$
\boxed{
W_i
=
\left\langle
Id_i,
S_i,
\Phi_i,
T_i,
\mathcal A_i,
\mathcal E_i,
\mu_i,
\Lambda_i,
\Gamma_i,
H_i,
R_i
\right\rangle.
}
$$

世界族：

$$
\boxed{
\mathfrak W_t^{G}
=
\left(
V_t,
G_t^{lin},
G_t^{int},
\mu_t,
\mathbf O_t,
\mathbf A_t,
\mathbf K_t,
\mathbf E_t,
\mathbf L_t,
\mathcal H_t,
\mathcal Q_t,
\mathcal B_t,
\mathcal G_t
\right).
}
$$

世界憲約：

$$
\boxed{
\mathsf{WCC}(W_i)
=
\left\langle
Identity,
Mode,
State,
Dynamics,
Clock,
Lineage,
RealityLink,
Observation,
Authority,
Evidence,
Resources,
Lifecycle,
Audit
\right\rangle.
}
$$

---

# 195. 結論：類全域 AI 需要治理世界，而不只是預測世界

一個普通 world model 可以問：

> 下一步會發生什麼？

一個更強的 model-based agent 可以問：

> 如果我做 action A 或 B，哪個後果比較好？

但類全域 AI 的 World Layer 還必須再回答：

> 我現在維持的是哪一種 world？

> 這個 world 與 reality 是什麼關係？

> 它從哪個 parent fork？

> 它用哪個 model、data、seed、evaluator？

> 這個 branch 的結果是 simulation evidence 還是 observed evidence？

> 哪些 sibling worlds 可以通信？

> 誰可以觀察它？

> 誰可以修改它？

> 誰可以把它的結果送往真實 action？

> 這個 world 被 prune 是因為不可能，還是只是沒預算？

> 新 evidence 出現後，它能不能 reopen？

所以：

$$
\boxed{
\text{World Modeling}
<
\text{World-Family Governance}
}
$$

不是說後者取代前者。

而是後者把 predictive world model 放入更大的 identity、evidence、authority 與 lifecycle system。

因此：

$$
\boxed{
\text{A Global-Like AI does not merely predict a world.}
}
$$

它更接近：

$$
\boxed{
\text{maintain}
+
\text{fork}
+
\text{compare}
+
\text{govern}
+
\text{audit}
+
\text{reopen}
}
$$

一整個受治理世界族。

這也使 Paper 01 的第一個核心族：

$$
\mathfrak W_t
$$

從一個抽象集合，正式升級成：

$$
\boxed{
\mathfrak W_t^{G}.
}
$$

接下來 Paper 03 才能真正問：

> **既然世界族已經建立，類全域 AI 應如何在這些 worlds、domains、transition laws 與 compute backends 之間進行 globally coherent heterogeneous computation？**

---

# 196. 下一篇接口

## Paper 03
# **計算層：世界族上的全域異質計算**
### Heterogeneous Global Computation over Governed World Families

將正式處理：

- computational form family；
- transition-law family；
- 24/72 computational configuration space；
- domain-relative computation；
- GCM composition；
- finite active support；
- bounded unbounded expansion；
- compute routing；
- computation history；
- state equality vs history equality；
- World Family × Computation Family coupling。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K，《Mathematical World Theory（MWT）》v0.1，2026。
2. Neo.K × Aletheia，《MWT／WBRG／GCRGDC：Observer-Separated Global Computation》v0.2，2026。
3. Neo.K × Aletheia，《全域系統世界與無界展開（GSWUE）Series》，2026。
4. Neo.K × Aletheia，《WDC / Branching World Computation Series》，2026。
5. Neo.K × Aletheia，《WDC-08：三生世界域計算》v0.1，2026。
6. Neo.K × Aletheia，《SWFR Paper 02：模擬世界族執行時》v0.1，2026。
7. Neo.K × Aletheia，《Visual–World Domain Computation Series》，2026。
8. Neo.K × Aletheia，《PNCW Series》，2026。
9. Neo.K × Aletheia，《類全域 AI 世界—計算—觀察統合系列 Paper 01》v0.1，2026。
10. Neo.K × Aletheia，《動態不動點數學奠基系列》，2026。

## External Research Interfaces

11. Kirchner, S., Purschke, N., & Knoll, A. (2026). *A survey of world models for physical AI with uncertainty representation and control*. Discover Artificial Intelligence, 6, 1037.
12. Gu, Y., Zhang, K., Ning, Y., et al. (2025). *Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents*. Transactions on Machine Learning Research.
13. Chae, H., Kim, N., Ong, K. T.-i., et al. (2025). *Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation*. ICLR 2025.
14. Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, 2nd ed. MIT Press.
15. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press.

---

**Paper 02 狀態：COMPLETE v0.1**  
**下一篇：Paper 03 — 計算層：世界族上的全域異質計算**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
