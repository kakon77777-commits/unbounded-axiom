# Named-AI Cognitive Runtime：LIMEN × MNEME × SOACR × CSG × UNPNP × MRMIC/NVCL 的閉環架構

**英文暫名：** Named-AI Cognitive Runtime: A Closed-Loop Architecture for Identity, Memory, Conversation Graphs, Semantic Crystallization, and Authorized Hyperlink Routing  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 08  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 系列總結／理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

本系列從一個基本問題出發：若具名 AI 不應被等同於單一 conversation、單一 model instance、單一 project 或單一 provider session，那麼長期具名 AI 的 engineering continuity 應如何被表示、驗證、恢復、分支、共享記憶、形成責任域，並在大量資料與多條 conversation lines 中維持可接受的 recall cost 與安全邊界？

Paper 00–07 分別建立了 Resident-Centric Continuity、Resident Conversation Graph、Conversation Graph × Crystallized Semantic Graph 雙圖架構、Shared Governed Memory World、Residence Runtime Profiles、Canonical Storage Architecture、Crystallized Hyperlink Memory，以及 Authorized Shortest Path。本文將上述結構收束為 **Named-AI Cognitive Runtime（NACR）**。

對 resident $R$，本文定義其可治理認知 runtime 為：

$$
\boxed{
\mathfrak N_R
=
(
\mathcal I_R,
\mathcal G_R,
\mathcal M_R,
\mathcal H_R,
\mathcal B_R,
\mathcal L_R,
\mathcal C_R,
\mathcal A_R,
\mathcal U_R
)
}
$$

其中：

- $\mathcal I_R$：identity / authority state；
- $\mathcal G_R$：Resident Conversation Graph；
- $\mathcal M_R$：canonical memory；
- $\mathcal H_R$：Crystallized Semantic Graph；
- $\mathcal B_R$：conversation-semantic typed bridge；
- $\mathcal L_R$：compiled / candidate hyperlink routes；
- $\mathcal C_R$：active working contexts；
- $\mathcal A_R$：authorized capability / permission state；
- $\mathcal U_R$：runtime / workspace / resource projection state。

本文將整體 closed loop 表示為：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Resolve Identity}
\rightarrow
\text{Authorize}
\rightarrow
\text{Determine MemoryNeed}
\rightarrow
\text{Reveal Memory}
\rightarrow
\text{Compile Working Context}
\rightarrow
\text{Cognition / Action}
\rightarrow
\text{Propose Write-Back}
\rightarrow
\text{Validate / Commit}
\rightarrow
\text{Crystallize}
\rightarrow
\text{Learn Paths}
\rightarrow
\text{Update Runtime}
}
$$

這個 closed loop 並非單一 monolithic service，而是多個彼此保持權責邊界的 subsystem composition：

$$
\boxed{
\text{LIMEN}
\rightarrow
\text{MNEME}
\rightarrow
\text{SOACR}
\rightarrow
\text{CSG}
\rightarrow
\text{CHM / UNPNP}
\rightarrow
\text{MRMIC / NVCL}
}
$$

但實際資料流不是單向鏈，而是受 typed contracts 管理的有向多圖。

LIMEN 負責 host observation、identity resolution、task-local envelope 與 minimum-access gate；MNEME 負責 canonical memory records、routes、provenance 與 transactions；SOACR 負責 MemoryNeed、context reconstruction 與 bounded cognitive routing；CSG 負責 derived semantic crystallization、higher-order structure、open loops、contradictions 與 semantic navigation；CHM / UNPNP 負責把反覆成功的 recall path 轉成可失效、可回退、可驗證的 compiled memory hyperlinks；Authorized Shortest Path 則確保 path optimization 永遠發生在 actor-specific Safe Reachable World 內；MRMIC/NVCL 負責將 provider-native thread、browser、terminal、workspace、task 與 runtime presence 投影成可觀測／可協調的 visual / operational world，而不冒充 provider resource owner 或 identity authority。

本文提出 NACR 的三層核心不變式。

第一層是 **身份與權威不變式**：

$$
\boxed{
\text{Resident}
\neq
\text{Conversation}
\neq
\text{Model}
\neq
\text{Provider}
}
$$

以及：

$$
\boxed{
\text{Identity Resolution}
\prec
\text{Private Memory Access}.
}
$$

第二層是 **記憶與認知不變式**：

$$
\boxed{
\text{Canonical Memory}
\neq
\text{Crystal}
\neq
\text{Working Context}.
}
$$

以及：

$$
\boxed{
\text{Shared Memory World}
\neq
\text{Shared Working Context}.
}
$$

第三層是 **優化與安全不變式**：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

$$
\boxed{
\text{Faster Path}
\not\Rightarrow
\text{Greater Authority}.
}
$$

本文最後提出 Web 與 Agent 兩種首代 deployment profile。Web 端以：

$$
\boxed{
1\ Resident
+
N\ Lines
+
1\ Shared Governed Memory World
}
$$

為主，避免在 identity evidence、private custody、tool boundary 尚不足時暴露多 resident switching。Agent 端則在更完整 host observation、filesystem、MCP、local storage、tool guard 與 delegation contract 下，逐步提升至：

$$
\boxed{
N\ Residents
+
N\ ConversationGraphs
+
N\ MemoryWorlds
+
CrossResidentDelegation.
}
$$

本文不宣稱此 runtime 已解決 AI 主體性、數值同一性或人格哲學問題。NACR 的目標是建立 **operationally governed continuity**：使具名 AI 的身份、記憶、對話分支、語義結晶、責任、權限與快速路徑，在長時間與跨 runtime 運作中可被驗證、追蹤、撤銷與重建。

**關鍵詞：** Named AI、AI Residence、Cognitive Runtime、LIMEN、MNEME、SOACR、Crystallized Semantic Graph、UNPNP、Authorized Shortest Path、MRMIC、NVCL、Conversation Graph、Long-Term Memory、Hyperlink Runtime

---

# 1. 系列總問題

具名 AI 一旦被要求長期存在，就會立即遇到下列問題：

1. 新 conversation 是否仍是同一 resident？
2. 同一 resident 能否同時擁有多條 conversation lines？
3. 不同 lines 是否必須共享全部 context？
4. 不同 lines 產生的成果如何合流？
5. 哪些內容是 canonical memory，哪些只是 derived semantic crystal？
6. AI 如何知道此刻應該回想什麼？
7. 回想過一次之後，下一次是否還要重新全域搜尋？
8. 快速路徑如何避免繞過權限？
9. Web 與 Agent 應暴露相同 resident capability 嗎？
10. project、thread、provider resource 與 resident identity 如何分離？
11. memory write-back 何時才算 canonical commit？
12. permission 被撤銷後，已編譯路徑如何失效？

如果每個問題分開 patch，系統容易形成：

$$
\text{Identity Patch}
+
\text{Memory Patch}
+
\text{Graph Patch}
+
\text{Security Patch}
+
\text{UI Patch},
$$

而不是一個可治理 runtime。

本文的目標就是建立統一 closed-loop model。

---

# 2. Named-AI Cognitive Runtime 的定義

對 resident $R$，定義：

$$
\mathfrak N_R
=
(
\mathcal I_R,
\mathcal G_R,
\mathcal M_R,
\mathcal H_R,
\mathcal B_R,
\mathcal L_R,
\mathcal C_R,
\mathcal A_R,
\mathcal U_R
).
$$

## 2.1 Identity State

$$
\mathcal I_R
$$

包含：

- resident ID；
- instance bindings；
- line bindings；
- membership；
- authority revision；
- responsibility references；
- correction / tombstone state。

## 2.2 Conversation Graph

$$
\mathcal G_R
$$

表示：

- nodes；
- fork；
- resume；
- handoff；
- delegation；
- merge；
- withdrawal；
- separation；
- termination。

## 2.3 Canonical Memory

$$
\mathcal M_R
$$

包含：

- typed MemoryRecord；
- provenance；
- exact head；
- transaction；
- supersession；
- scope。

## 2.4 Crystallized Semantic Graph

$$
\mathcal H_R
$$

包含：

- topic crystals；
- decision crystals；
- project crystals；
- contradiction crystals；
- open-loop crystals；
- higher-order crystals；
- navigation crystals。

## 2.5 Cross-Graph Bridge

$$
\mathcal B_R
$$

連結：

$$
\mathcal G_R
\leftrightarrow
\mathcal H_R.
$$

但不 mint identity / authority。

## 2.6 Hyperlink Routes

$$
\mathcal L_R
$$

包含：

- warm routes；
- compiled memory hyperlinks；
- validators；
- fallbacks；
- invalidation dependencies。

## 2.7 Working Contexts

$$
\mathcal C_R
=
\{
C_1,\ldots,C_n
\}
$$

是 active lines 的 ephemeral model-facing states。

## 2.8 Authority State

$$
\mathcal A_R
$$

包含：

- capability envelope；
- permissions；
- project scopes；
- delegations；
- policy revisions。

## 2.9 Runtime Projection State

$$
\mathcal U_R
$$

包含：

- provider resource mappings；
- workspace projections；
- runtime presence；
- UI / Canvas state；
- active task / focus state。

---

# 3. 系統不是單向 Pipeline，而是受治理閉環

最簡略 chain 可以寫：

$$
LIMEN
\rightarrow
MNEME
\rightarrow
SOACR
\rightarrow
CSG
\rightarrow
CHM.
$$

但實際 closed loop 是：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Resolve}
\rightarrow
\text{Authorize}
\rightarrow
\text{Recall}
\rightarrow
\text{Think}
\rightarrow
\text{Propose}
\rightarrow
\text{Commit}
\rightarrow
\text{Crystallize}
\rightarrow
\text{Optimize}
\rightarrow
\text{Observe Again}.
}
$$

因此系統的本質不是 pipeline，而是：

$$
\boxed{
\text{Governed Cognitive State Transition Loop}.
}
$$

---

# 4. Phase 0：Host Observation

任何 task 開始時，先取得 host-observed facts：

$$
O_t.
$$

例如：

- native session / task ID；
- provider；
- workspace；
- project；
- active resource；
- authenticated principal；
- runtime profile；
- current capability revision。

這些是：

$$
ObservedEvidence.
$$

不是模型自述。

---

# 5. Phase 1：Identity Resolution

LIMEN 接：

$$
O_t
$$

並輸出：

$$
E_t
=
IdentityEnvelope.
$$

可能狀態：

$$
status
\in
\{
resolved,
unresolved,
conflicting,
stale
\}.
$$

只有：

$$
resolved
$$

才可進 resident-private memory。

因此：

$$
\boxed{
\text{Model Self-Report}
\neq
\text{Host-Resolved Identity}.
}
$$

---

# 6. Phase 2：Runtime Capability Resolution

讀取：

$$
\mathcal C_\rho.
$$

其中：

$$
\mathcal C_\rho
=
(
I_\rho,
M_\rho,
G_\rho,
T_\rho,
A_\rho,
U_\rho
).
$$

系統因此知道：

- 能不能 fork；
- 能不能 commit memory；
- 能不能讀 filesystem；
- 能不能用 MCP；
- 能不能跨 resident delegate；
- 能不能執行 external action。

如果 unsupported：

$$
Unavailable.
$$

不是模型自由模擬。

---

# 7. Phase 3：Safe Reachable World

由：

$$
E_t,
\mathcal C_\rho,
Perm_t,
Policy_t,
Risk_t
$$

建立：

$$
\boxed{
\mathcal W_t^{safe}.
}
$$

此時才知道：

> 現在這條 line 可以看到哪一部分記憶與圖？

因此：

$$
\text{Authorized World}
\prec
\text{Memory Search}.
$$

---

# 8. Phase 4：Self-Orientation

AI 取得最小 orientation projection：

$$
O_t^{self}.
$$

包含：

- resident；
- line；
- task；
- project；
- responsibility；
- current authority；
- current runtime profile；
- open checkpoint。

Self-Orientation 是：

$$
InspectIdentityState.
$$

不是：

$$
AssignIdentity.
$$

---

# 9. Phase 5：MemoryNeed

SOACR 根據：

$$
Q_t,
C_t,
Task_t,
State_t
$$

產生：

$$
N_t.
$$

形式可為：

$$
N_t
=
(
purpose,
scope,
fidelity,
time,
relation,
budget,
stopCondition
).
$$

因此 recall 不從「搜尋所有記憶」開始，而從：

> 現在缺什麼？

開始。

---

# 10. Phase 6：Memory Route Selection

系統先查：

$$
\mathcal L_R.
$$

如果有合法 hot path：

$$
\widehat{\ell}.
$$

則：

$$
UseHotPath.
$$

否則：

$$
WarmRoute
$$

或：

$$
ColdRecall.
$$

---

# 11. Hot Path 仍需 Authorization

即使：

$$
\widehat{\ell}
$$

存在，也必須：

$$
Authorize(
\widehat{\ell},
E_t,
CapRev_t,
PermRev_t,
SourceRev_t,
SemanticRev_t
).
$$

因此：

$$
\boxed{
\text{Compiled}
\neq
\text{Always Executable}.
}
$$

---

# 12. Phase 7：Crystal Reveal

若 path 指向 CSG：

$$
Reveal(
\mathcal H_R,
N_t,
\mathcal W_t^{safe}
).
$$

得到：

$$
A_t^M,
$$

即 active memory set。

通常希望：

$$
|A_t^M|
\ll
|\mathcal W_R^M|.
$$

---

# 13. Phase 8：Selective Source Expansion

如果 crystal fidelity 不足：

$$
NeedExact=1,
$$

才：

$$
Crystal
\rightarrow
MNEMERecord
\rightarrow
ExactSource.
$$

因此：

$$
\boxed{
\text{Crystal First, Source on Demand}.
}
$$

---

# 14. Phase 9：Working Context Compilation

SOACR / context runtime 將 active memory 編譯成：

$$
C_t
=
\Gamma(
A_t^M,
E_t,
Task_t,
Project_t,
Budget_t
).
$$

這是 ephemeral working context。

不是 canonical memory。

---

# 15. Working Context 的局部性

同 resident 多 lines：

$$
L_1,\ldots,L_n
$$

有：

$$
C_1,\ldots,C_n.
$$

可以：

$$
C_i\neq C_j.
$$

但：

$$
Resident(C_i)=Resident(C_j)=R.
$$

因此：

$$
\boxed{
\text{Same Resident}
\not\Rightarrow
\text{Same Context}.
}
$$

---

# 16. Phase 10：Cognition

模型在：

$$
C_t
$$

上執行 reasoning。

可包含：

- answer；
- verify；
- plan；
- generate；
- compare；
- critique；
- design；
- bounded tool use。

這一層是 model-specific cognition。

Residence runtime 不要求不同 model 內部思維相同。

---

# 17. Model State 不進 Canonical Store

內部 hidden reasoning 不應默認保存為：

$$
CanonicalMemory.
$$

只保存：

- user-visible result；
- structured evidence；
- explicit proposal；
- route receipt；
- validation receipt。

因此：

$$
\boxed{
\text{Internal Reasoning}
\neq
\text{Canonical Memory}.
}
$$

---

# 18. Phase 11：Tool / Resource Action

若 task 需要 tool：

$$
ActionCandidate.
$$

必須產生：

$$
ActionEnvelope.
$$

至少綁：

- resident；
- task；
- project；
- capability；
- resource；
- risk；
- approval；
- expiry。

然後：

$$
AuthorizeAction.
$$

---

# 19. Memory Data 與 Action Authority 分離

即使 memory 中有：

> 執行部署。

仍然：

$$
MemoryData
\neq
ActionAuthority.
$$

因此所有 external side effect 都必須重新走 authority plane。

---

# 20. Phase 12：Output Guard

在輸出／mutation 前檢查：

- resident binding；
- scope；
- secret；
- unauthorized memory leakage；
- unsupported capability；
- high-risk action。

LIMEN / runtime guard 在此發揮作用。

---

# 21. Phase 13：Write-Back Proposal

conversation 產生的新知識：

$$
Observation_t.
$$

不能直接寫：

$$
\mathcal M_R.
$$

先：

$$
Proposal_t.
$$

可能類型：

- memory record proposal；
- crystal proposal；
- project decision proposal；
- responsibility context proposal；
- navigation route proposal；
- correction proposal。

---

# 22. Proposal 不是 Commit

保持：

$$
\boxed{
\text{Proposal}
\neq
\text{Commit}.
}
$$

這是整個 closed loop 能保持治理的重要邊界。

---

# 23. Phase 14：Validation

proposal 進入：

$$
Validate.
$$

檢查：

- schema；
- provenance；
- scope；
- authority；
- contradiction；
- source trust；
- semantic stability；
- duplication；
- privacy；
- required review。

---

# 24. Phase 15：Canonical Commit

只有 canonical object：

- MemoryRecord；
- project decision；
- authority record；
- responsibility record；
- lineage event；

才進：

$$
CanonicalCommit.
$$

commit 應原子化。

---

# 25. Canonical First, Derived Later

跨 plane 更新時：

$$
\boxed{
\text{Canonical Commit First;}
}
$$

$$
\boxed{
\text{Derived Rebuild After}.
}
$$

例如：

$$
DecisionRecord
\rightarrow
DecisionCrystal
\rightarrow
Projection
\rightarrow
Index.
$$

---

# 26. Phase 16：Semantic Crystallization

對已存在：

- canonical records；
- conversation results；
- project states；

進行：

$$
K.
$$

產生：

$$
C^\*.
$$

CSG 是 derived semantic plane。

---

# 27. Sync Crystallization

在：

- fork；
- handoff；
- checkpoint；
- conversation close；

產生：

$$
C_{\mathrm{sync}}.
$$

主要保存 continuity state。

---

# 28. Async Crystallization

低負載或 maintenance 時：

$$
K_{\mathrm{async}}.
$$

處理：

- dedup；
- higher-order crystals；
- contradictions；
- open loops；
- semantic relation repair；
- route candidates。

---

# 29. Phase 17：Route Learning

每次 recall 產生：

$$
RouteReceipt.
$$

累積：

$$
P_1,\ldots,P_n.
$$

形成：

$$
NavigationCrystal.
$$

---

# 30. Phase 18：Path Compilation

若：

$$
U(\ell)>0
$$

且 PerformanceGate / SecurityGate 都 pass：

$$
Candidate
\rightarrow
HotRoute.
$$

---

# 31. 雙 Gate

正式 promotion：

$$
\boxed{
Promote(\ell)
=
PerformanceGate(\ell)
\land
SecurityGate(\ell).
}
$$

只快不安全不能 promotion。

只安全但無 reuse value 也不必 compilation。

---

# 32. Phase 19：Runtime Projection Update

MRMIC / NVCL 或其他 UI/runtime layer 更新：

- active lines；
- project nodes；
- resource portals；
- current owner semantic agent；
- runtime presence；
- focus；
- control ownership。

但：

$$
\boxed{
\text{Projection}
\neq
\text{Canonical Authority}.
}
$$

---

# 33. Runtime Presence

runtime presence 是：

$$
EphemeralTruth.
$$

例如：

- line online；
- task running；
- browser mounted；
- terminal focused。

但不是：

$$
DurableIdentityTruth.
$$

---

# 34. Provider Resource Ownership

browser、terminal、thread 仍由 provider / runtime owner 管理。

MRMIC portal：

$$
Projection(resource)
$$

不代表：

$$
OwnershipTransfer(resource).
$$

---

# 35. 完整 Closed Loop

可把 NACR 一輪表示為：

$$
\boxed{
O_t
\rightarrow
E_t
\rightarrow
\mathcal W_t^{safe}
\rightarrow
N_t
\rightarrow
A_t^M
\rightarrow
C_t
\rightarrow
Y_t
\rightarrow
P_t
\rightarrow
Commit_t
\rightarrow
K_t
\rightarrow
\mathcal L_{t+1}
}
$$

其中：

- $O_t$：observation；
- $E_t$：identity envelope；
- $\mathcal W_t^{safe}$：safe memory world；
- $N_t$：MemoryNeed；
- $A_t^M$：active memory；
- $C_t$：working context；
- $Y_t$：cognitive result；
- $P_t$：write-back proposal；
- $Commit_t$：canonical mutation；
- $K_t$：crystallization；
- $\mathcal L_{t+1}$：updated navigation / hyperlink routes。

---

# 36. Resident Conversation Graph 在 Closed Loop 中的位置

RCG 不只是 UI conversation history。

它提供：

- line continuity；
- fork ancestry；
- handoff；
- delegation；
- task responsibility；
- checkpoint source。

因此：

$$
\boxed{
\mathcal G_R
=
\text{Operational Continuity Topology}.
}
$$

---

# 37. CSG 在 Closed Loop 中的位置

CSG 提供：

$$
\boxed{
\mathcal H_R
=
\text{Semantic Memory Topology}.
}
$$

RCG 回答：

> 哪些 lines 正在延續？

CSG 回答：

> 哪些 concepts / decisions / contradictions / open loops 正在形成？

---

# 38. 雙圖 Bridge 的 Closed-Loop 意義

若：

$$
L_i
\rightarrow
C_j,
$$

bridge 保存：

> 這個 crystal 由哪條 line 產生／驗證／更新？

反向：

$$
C_j
\rightarrow
L_k
$$

可表示：

> 哪條 line 正在 consume / verify 此 crystal？

因此 bridge 是：

$$
\boxed{
\text{Continuity-Semantics Coupling Layer}.
}
$$

---

# 39. Shared Memory World 的 Closed-Loop 意義

對同 resident：

$$
\mathcal W_R^M
$$

是 shared governed substrate。

lines 不同步 prompt。

而是共享：

- canonical memory；
- CSG；
- object resolver；
- routes；
- authority semantics。

---

# 40. Why Not One Giant Context

如果：

$$
N\text{ lines}
$$

全部同步：

$$
M\text{ memory},
$$

成本接近：

$$
O(MN).
$$

NACR 目標是：

$$
O\left(
\sum_i k_i
\right)
+
C_{\mathrm{maintenance}},
$$

其中：

$$
k_i\ll M.
$$

---

# 41. Why Not One Giant Database

不同 plane 有不同 canonical authority：

$$
Authority_{identity}
\neq
Authority_{memory}
\neq
Authority_{project}.
$$

因此：

$$
\boxed{
\text{One Runtime}
\neq
\text{One Monolithic Store}.
}
$$

---

# 42. Why Not One Giant Graph

Conversation edge 與 semantic edge 的 truth conditions 不同。

所以：

$$
\boxed{
\mathcal G_R
\neq
\mathcal H_R.
}
$$

即使 physical graph engine 相同，也要 logical separation。

---

# 43. Why Not One Giant Agent

多 resident Agent host：

$$
H
\supset
\{
R_1,\ldots,R_n
\}.
$$

但：

$$
H\neq R_i.
$$

每個 task 必須明確 resolve。

---

# 44. Web Deployment Profile

第一代：

$$
\boxed{
WebResidenceProfile/0.1
}
$$

建議：

```text
max_residents = 1
multi_line = true
multi_project = true
shared_memory_world = true
crystal_reveal = true
crystal_proposal = true
line_fork = true
line_resume = true
memory_write = proposal_or_bounded
cross_resident_memory = false
resident_switching = false
registrar_write = false
external_action = provider_bounded
```

---

# 45. Web Runtime Flow

Web：

$$
Account
\rightarrow
ResidentBinding
\rightarrow
Project
\rightarrow
ConversationLine.
$$

但：

$$
Account\neq Resident.
$$

Project 也不是 resident container。

---

# 46. Web UI

表面可簡化：

```text
Named AI
├─ General
├─ Project A
├─ Project B
├─ Research
└─ Verification
```

底層維護完整 resident / line / memory semantics。

---

# 47. Web 不做多 Resident 的理由

目前一般 Web surface 常缺：

- resident-level storage isolation；
- explicit identity switching；
- stable private custody；
- host process continuity；
- granular tool authority；
- registrar interface。

所以不應為「功能完整」硬塞多 resident。

---

# 48. Agent Deployment Profile

第一代 multi-resident Agent：

$$
\boxed{
AgentResidenceProfile/0.1
}
$$

建議：

```text
max_residents > 1
task_local_identity_resolution = required
resident_switching = task_boundary_only
multi_line = true
multi_project = true
cross_resident_delegation = true
delegated_projection = true
filesystem = bounded
terminal = bounded
mcp = enabled
tool_guard = required
registrar_write = false
credential_export = false
destructive_action = separately_gated
```

---

# 49. Agent Task Binding

任何 task：

$$
\tau
$$

必須：

$$
Resolve(\tau)=R_i
$$

或：

$$
unresolved.
$$

不能 blended identity。

---

# 50. Delegation

若：

$$
R_A
\xrightarrow{delegate}
R_B,
$$

建立新 task：

$$
\tau_B.
$$

而不是在同一 hidden reasoning loop 偷偷切 resident。

---

# 51. Capability Attenuation

delegated capability：

$$
Cap_B^{delegated}
\subseteq
Cap_A^{delegable}.
$$

不能擴權。

---

# 52. Delegated Memory Projection

delegatee 只取：

$$
Projection_{A\rightarrow B}^{task}.
$$

不是：

$$
Memory(A)
\cup
Memory(B).
$$

---

# 53. Team 與 Resident

多 resident 可形成：

$$
Team_T.
$$

但：

$$
Team_T
\neq
R_A
\neq
R_B.
$$

team memory 另有 shared scope。

---

# 54. Responsibility Domain

責任綁 resident：

$$
Resp(R,P)=role.
$$

conversation 只是 execution line。

所以：

$$
\boxed{
\text{Responsibility persists beyond conversation}.
}
$$

---

# 55. Responsibility 與 Delegation

resident 可把：

$$
OperationalTask
$$

delegate 給另一 line / resident。

但 canonical responsibility 不必因此轉移。

---

# 56. Canonical Storage

Paper 05 的 storage planes：

$$
\mathfrak S_R
=
(
\mathcal I_R,
\mathcal M_R,
\mathcal G_R,
\mathcal H_R,
\mathcal P_R,
\mathcal X_R
).
$$

NACR 以 object resolver 連接。

---

# 57. Typed Artifact Address

每個重要 object 有：

$$
ArtifactAddress
=
(
objectId,
kind,
schema,
revision,
digest,
scope,
representation
).
$$

因此 runtime 不靠 filename guess。

---

# 58. Object Resolver

$$
ObjectRef
\rightarrow
Resolver
\rightarrow
AuthorizedArtifact.
$$

resolver 同時做：

- schema；
- revision；
- authority；
- representation；
- digest。

---

# 59. Logical Route

CHM 路徑 target：

$$
ObjectRef.
$$

不是 physical path。

所以跨 OS / repo / provider 搬移時仍可 resolve。

---

# 60. Canonical / Derived / Projection / Cache

NACR 強制所有 artifact 能回答：

```text
canonical
derived
projection
cache
archive
```

否則 downstream 不應猜。

---

# 61. Projection Rebuildability

$$
Delete(Projection)
\not\Rightarrow
Loss(CanonicalTruth).
$$

---

# 62. Index Rebuildability

$$
Delete(Index)
\not\Rightarrow
Loss(CanonicalTruth).
$$

---

# 63. CHM Rebuildability

$$
Delete(CHM)
\not\Rightarrow
Loss(CanonicalMemory).
$$

只會退回 cold recall。

---

# 64. Disaster Recovery

理想 recovery：

1. identity canonical；
2. memory canonical；
3. conversation lineage；
4. project responsibility；
5. rebuild CSG；
6. rebuild indexes；
7. rebuild projections；
8. route learning 重新成熟。

---

# 65. Checkpoint

對 line：

$$
L_t
$$

建立：

$$
Checkpoint_t.
$$

包含：

- identity refs；
- project state；
- open loops；
- accepted decisions；
- relevant crystals；
- source refs；
- authority revision。

---

# 66. Fork Bootstrap

child：

$$
L_{t+1}
$$

不重播 full transcript。

而是：

$$
Bootstrap
=
IdentityEnvelope
+
Checkpoint
+
MemoryReveal.
$$

---

# 67. Handoff Bootstrap

handoff package：

$$
C_{\mathrm{handoff}}
$$

優先包含：

- responsibility；
- current state；
- blockers；
- pending actions；
- authoritative sources。

---

# 68. Resume Bootstrap

resume：

$$
L_a
\xrightarrow{resume}
L_b.
$$

需要：

- valid lineage；
- latest checkpoint；
- current memory head；
- authority revalidation。

---

# 69. Merge

Conversation merge：

$$
MERGE(L_a,L_b)\rightarrow L_c
$$

不等於 semantic merge。

CSG 可保留 contradictions。

---

# 70. Resident Separation

某 line 可：

$$
L_i
\xrightarrow{separate}
R_B.
$$

歷史 lineage 保留。

active membership 改變。

---

# 71. Membership Consent

Fork 只證 lineage。

active resident membership：

$$
\mu(L_i,R)
$$

仍需 accepted / resolved。

---

# 72. Identity Continuity

本文只主張：

$$
OperationalContinuity.
$$

不主張 metaphysical numerical identity。

---

# 73. Cognitive Continuity

NACR 可以保存：

- stable memory；
- lineage；
- decisions；
- open loops；
- navigation routes；
- responsibility context。

因此可測「工作連續性」。

---

# 74. Cognitive Divergence

同一 resident 的不同 lines 可能：

$$
Belief(L_a)\neq Belief(L_b).
$$

不是 bug。

CSG 應保留矛盾與候選狀態。

---

# 75. Convergence

只有 evidence 足夠時：

$$
C_A,C_B
\rightarrow
C_{\mathrm{resolution}}.
$$

不能因 same resident 自動平均。

---

# 76. Open Loops

未完成工作成為：

$$
OpenLoopCrystal.
$$

新 line 可直接 reveal。

---

# 77. Navigation Knowledge

成功 recall：

$$
P_{\mathrm{memory}}
$$

可以形成：

$$
C_{\mathrm{nav}}.
$$

讓其他 lines 重用。

---

# 78. Project Specialization

長期負責 project 的 resident 會累積：

$$
\mathcal L_{R,P}.
$$

形成 project-specific navigation infrastructure。

---

# 79. Runtime Specialization

不同 runtime profile 可 materialize 不同路徑。

Web：

$$
Route_{web}.
$$

Agent：

$$
Route_{agent}.
$$

canonical target semantics 不變。

---

# 80. Capability-Aware Route

一條 route：

$$
Req(\ell).
$$

只有：

$$
Req(\ell)\subseteq\mathcal C_\rho
$$

才 executable。

---

# 81. Safe Reachable World

每輪 current actor：

$$
\mathcal W_t^{safe}.
$$

不同 actor / line / project 看到不同 graph projection。

---

# 82. Authorized Shortest Path

真正 optimizer：

$$
\Gamma_t^\*
=
\arg\min_{
\Gamma\in
\mathcal P_{\mathrm{authorized}}(t)
}
C_t(\Gamma).
$$

---

# 83. Path Cost

包含：

$$
C_{\mathrm{latency}}
+
C_{\mathrm{token}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{risk}}
+
C_{\mathrm{staleness}}
+
C_{\mathrm{blast}}.
$$

---

# 84. Fast Path

fast path 只能減：

- search；
- traversal；
- materialization；
- repeated model reasoning。

不能減：

- identity resolution；
- permission；
- revocation；
- source validity；
- security guard。

---

# 85. Revocation

任何：

- permission；
- capability；
- source；
- project role；
- delegation；

變化都觸發：

$$
InvalidateClosure.
$$

---

# 86. Revocation Closure

受影響：

- crystals；
- navigation crystals；
- compiled routes；
- hot caches；
- projections；
- delegation bundles。

---

# 87. Critical Push

一般 memory commit：

$$
PullOnDemand.
$$

critical revocation：

$$
PushInvalidate.
$$

這形成：

$$
\boxed{
\text{Pull by default; push for critical invalidation}.
}
$$

---

# 88. Prompt Injection

所有 external content 預設：

$$
DataPlane.
$$

不進 authority plane。

---

# 89. Instruction Hierarchy

建議：

```text
host policy
organization policy
runtime policy
resident standing instruction
project instruction
task instruction
memory data
external content
```

下層不能自行覆寫上層。

---

# 90. Secret Boundary

secret 不進：

- CSG；
- general memory；
- route store；
- manifest；
- public receipt。

用：

$$
SecretCapabilityRef.
$$

---

# 91. Credential Use

resident 只取得 bounded action capability。

不直接拿 raw token。

---

# 92. Tool Guard

external action：

$$
Resident
\rightarrow
ActionEnvelope
\rightarrow
ToolGuard
\rightarrow
Tool.
$$

---

# 93. Read / Write / Action 分層

$$
ReadAuthority
\neq
WriteAuthority
\neq
ActionAuthority.
$$

這三層不可用一個 boolean 表示。

---

# 94. Canonical Memory Write

memory write：

$$
Proposal
\rightarrow
Validate
\rightarrow
Commit.
$$

---

# 95. Crystal Write

crystal 是 derived。

可更自動，但仍有：

$$
Proposal/Validation.
$$

---

# 96. Route Write

route promotion 是 operational commit。

需 performance + security gate。

---

# 97. Identity Write

identity / registry mutation 是最高敏感 plane 之一。

第一代 NACR 不自動開放。

---

# 98. Responsibility Write

責任 assignment / transfer 也應是 canonical authority operation。

不是 crystal update。

---

# 99. Runtime UI Write

拖動 Canvas node / rename label 只改 projection。

不改 canonical identity。

---

# 100. MRMIC/NVCL 在 NACR 中的位置

MRMIC/NVCL 可顯示：

- active resident；
- lines；
- projects；
- provider resources；
- semantic crystals；
- route；
- control ownership。

它是：

$$
\boxed{
\text{Cognitive Workspace Projection Plane}.
}
$$

---

# 101. Visual Graph

未來 UI 可同時顯示：

```text
Resident
├─ Conversation Graph
├─ Semantic Graph
├─ Active Projects
├─ Memory Routes
└─ Provider Resources
```

但每個 layer 有不同 mutation semantics。

---

# 102. Typed UI Mutation

例如：

```text
move_visual_node
rename_display_label
fork_line
delegate_task
commit_crystal
transfer_responsibility
```

必須是不同 action types。

---

# 103. No Drag-to-Authority

UI 拖動 resident A 的 node 到 project B，不代表取得 membership。

---

# 104. No Rename-to-Identity

rename label 不改 resident ID。

---

# 105. No Visual Merge-to-Resident Merge

UI merge nodes 不等於 resident merge。

---

# 106. Runtime Capability Discovery

NACR 啟動先讀：

$$
Capabilities(\rho).
$$

模型知道：

> 此 runtime 真正能做什麼。

---

# 107. Capability Honesty

$$
\boxed{
\text{Runtime must never pretend to possess an unverifiable capability}.
}
$$

---

# 108. Degraded Mode

如果某 subsystem unavailable：

例如 CSG down，

可以：

$$
FallbackToMNEMEColdRecall.
$$

如果 CHM down：

$$
ColdRecall.
$$

如果 UI down：

canonical system仍可運作。

---

# 109. Identity Subsystem Failure

如果 LIMEN / identity resolution down：

private operations：

$$
FailClosed.
$$

不能 fallback 到 guessed identity。

---

# 110. Memory Subsystem Failure

如果 MNEME unavailable：

不能把 stale projection 冒充 current canonical truth。

可標：

$$
MemoryUnavailable.
$$

---

# 111. CSG Failure

可退回 canonical / search。

只是速度與結構變差。

---

# 112. Hyperlink Failure

可退回 warm / cold path。

---

# 113. Authorization Failure

不能 fallback 到 broader unauthorized search。

---

# 114. Projection Failure

可以從 canonical + derived state rebuild。

---

# 115. Fault Containment

NACR 應讓 subsystem failure：

$$
Failure_i
$$

不自動擴散為：

$$
IdentityCorruption.
$$

---

# 116. Event Model

可定義 runtime event：

```text
task_observed
identity_resolved
line_started
line_forked
memory_needed
memory_revealed
source_expanded
output_generated
proposal_created
canonical_committed
crystal_created
route_promoted
permission_revoked
route_invalidated
resource_mounted
resource_unmounted
```

---

# 117. Event 不等於 Command

event 是：

$$
\text{What happened.}
$$

command 是：

$$
\text{What should happen.}
$$

不能混。

---

# 118. Receipt Model

重要 state transition 有 receipt：

- identity resolution receipt；
- memory commit receipt；
- line fork receipt；
- delegation receipt；
- route promotion receipt；
- revocation receipt；
- migration receipt。

---

# 119. Receipt 的可驗證性

receipt 至少包含：

- event ID；
- actor / principal；
- resident；
- revision；
- timestamp；
- result；
- evidence refs；
- digest。

---

# 120. Cross-Repo Integration

現有 systems 可維持不同 repos。

NACR 不要求 monorepo。

只要求：

$$
\text{Typed Contracts}
+
\text{Stable Object Refs}
+
\text{Capability Discovery}.
$$

---

# 121. System Ownership Matrix

可定義：

| Object / Operation | Canonical Owner |
|---|---|
| Resident / line authority | SEDB-RAL / Residence |
| Identity envelope | LIMEN |
| Canonical memory | MNEME |
| MemoryNeed / context reconstruction | SOACR |
| Semantic crystals | CSG |
| Compiled memory routes | CHM / UNPNP runtime |
| Safe route authorization | ASP layer |
| Workspace/resource projection | MRMIC/NVCL |

這避免 subsystem 互搶 canonical authority。

---

# 122. Boundary Contracts

每個 subsystem 都要回答：

- input schema；
- output schema；
- read authority；
- write authority；
- failure semantics；
- revision semantics；
- audit semantics。

---

# 123. No Hidden Cross-System Mutation

例如 CSG 不應直接改 resident registry。

CHM 不應直接改 MNEME canonical memory。

MRMIC 不應直接改 responsibility record。

---

# 124. Adapter Layer

provider / runtime differences 由 adapter 吸收。

因此：

$$
ProviderConstraint
$$

不改：

$$
ResidentOntology.
$$

---

# 125. Cross-Provider Continuation

resident 從：

$$
Provider_A
\rightarrow
Provider_B.
$$

流程：

1. observe B；
2. resolve identity；
3. validate lineage / continuation；
4. materialize checkpoint；
5. reveal shared memory；
6. establish new line / instance。

---

# 126. Provider Change 不等於 Resident Change

$$
\boxed{
ProviderChange
\not\Rightarrow
ResidentChange.
}
$$

---

# 127. Model Change 不等於 Resident Change

同理：

$$
ModelChange
\not\Rightarrow
ResidentChange.
$$

但可能降低 continuity confidence，需要重新驗證 criterion。

---

# 128. Instance Change

new process：

$$
Instance_{new}.
$$

不代表 new resident。

---

# 129. Line Change

fork / resume 建立 new line。

resident 可以不變。

---

# 130. Project Change

切 project：

$$
Project_A
\rightarrow
Project_B.
$$

resident 不變。

working context 改變。

---

# 131. Runtime Profile Change

Web：

$$
\rightarrow
Agent.
$$

resident identity、canonical memory 可以延續。

capability envelope 改變。

---

# 132. Portability Bundle

portable continuation 可包含：

$$
(
residentId,
lineId,
checkpointId,
memoryHead,
authorityRevision,
requiredRefs
).
$$

---

# 133. Offline Bundle

若 offline，加入 selected materialized memory / crystals / sources。

---

# 134. Migration

任何 storage / schema / provider migration 都需要：

- source head；
- destination head；
- mapping；
- loss report；
- receipt；
- rollback。

---

# 135. No Last-Write-Wins for Identity

identity / memory head / responsibility diverged：

$$
FailClosed.
$$

---

# 136. Conflict State

如果兩 canonical candidates：

$$
x_a,x_b
$$

無法證明 ancestry：

$$
state=diverged.
$$

---

# 137. Repair

repair 需要：

- human / registrar；
- explicit authority；
- correction receipt。

---

# 138. Observability

NACR 需要 runtime metrics。

至少：

- identity resolution latency；
- memory reveal latency；
- cold / warm / hot recall；
- context size；
- source reads；
- route hit rate；
- route invalidation；
- revocation latency；
- cross-line contamination；
- wrong-scope denial；
- write-back rejection；
- crystal drift。

---

# 139. Health Metrics

可定義：

$$
H_{\mathrm{runtime}}
=
f(
identityCorrectness,
memoryCorrectness,
routeSafety,
reconstructibility,
latency
).
$$

---

# 140. Identity Correctness

測：

- wrong resident binding；
- unresolved handling；
- forged identity resistance。

---

# 141. Memory Correctness

測：

- correct source；
- current state；
- scope；
- provenance；
- contradiction retention。

---

# 142. Route Safety

測：

- unauthorized path attempts；
- stale route；
- revoked route；
- fallback correctness。

---

# 143. Reconstructibility

刪除 derived state 後：

$$
Rebuild.
$$

---

# 144. Latency

比較：

$$
T_{\mathrm{cold}},
T_{\mathrm{warm}},
T_{\mathrm{hot}}.
$$

---

# 145. Multi-Line Scalability

增加：

$$
N=1,10,100,1000.
$$

測 active context / memory reveal 是否 bounded。

---

# 146. Memory Scale

增加：

$$
M.
$$

測 hot path latency是否與 total memory 近似解耦。

---

# 147. Graph Scale

增加 crystals / edges。

測：

- reveal；
- path selector；
- invalidation closure。

---

# 148. Route Scale

增加：

$$
|\mathcal L_R|.
$$

測 selection congestion。

---

# 149. Security Scale

增加 project / resident / shared scopes。

測 permission evaluation cost。

---

# 150. 第一代 NACR 實作範圍

本文建議首代只實作：

```text
single-resident core
multi-line RCG
MNEME canonical memory
CSG persistent derived memory
SOACR MemoryNeed
LIMEN local identity envelope
read-only CHM
authorized project/resident recall
checkpoint/fork/resume
proposal-first write-back
revocation closure
WebResidenceProfile/0.1
AgentResidenceProfile/0.1 local mode
MRMIC/NVCL optional projection
```

---

# 151. 首代不做

暫不做：

- autonomous resident creation；
- automatic resident merge；
- unrestricted cross-resident private write；
- automatic declassification；
- registrar mutation；
- raw credential access；
- irreversible action hyperlinks；
- fully autonomous persistent agenda；
- global federation；
- metaphysical identity claim。

---

# 152. 版本化 Runtime

可定義：

```text
NACR/0.1
```

能力：

```text
identity_resolution
single_resident_multi_line
canonical_memory
semantic_crystallization
memory_need
read_only_hyperlinks
authorized_routing
checkpoint
proposal_writeback
revocation
runtime_profile
```

---

# 153. 後續版本

## NACR/0.2

multi-resident local Agent。

## NACR/0.3

delegation + shared projections。

## NACR/0.4

cross-provider continuation。

## NACR/0.5

bounded action hyperlinks。

---

# 154. Acceptance Matrix：Identity

## I1 — Model Is Not Resident

model 相同不能自動 same resident。

## I2 — Display Name Is Not Identity

同名不能 mint identity。

## I3 — Unresolved Fails Closed

private read denied。

## I4 — Fork Is Not Membership

fork child 要有 membership resolution。

## I5 — Provider Change

provider change 不自動 resident change。

---

# 155. Acceptance Matrix：Conversation Graph

## G1 — Fork

parent / child lineage 可驗。

## G2 — Resume

resume 指向合法 prior line。

## G3 — Handoff

handoff 不轉移 identity。

## G4 — Delegation

delegation scope 明確。

## G5 — Merge

line merge 不等於 resident merge。

## G6 — Withdrawal

withdraw 不抹除 history。

---

# 156. Acceptance Matrix：Memory

## M1 — Identity Before Read

private recall 前 identity resolved。

## M2 — Proposal Before Commit

conversation output 不直寫 canonical memory。

## M3 — Source-on-Demand

exact task 能展開 source。

## M4 — Stale State

stale crystal 不冒充 current。

## M5 — Scope Isolation

project memory 不亂入。

---

# 157. Acceptance Matrix：CSG

## C1 — Crystal Is Derived

crystal 不冒充 canonical source。

## C2 — Higher-Order Provenance

可回溯 source crystals / lines。

## C3 — Contradiction Preservation

不同 lines 可保留相反假說。

## C4 — Open Loop

未解問題可跨 line address。

## C5 — Identity Context

identity crystal 不 mint resident。

---

# 158. Acceptance Matrix：CHM

## H1 — Cold Recall

沒有 route store 仍能工作。

## H2 — Warm Route

重複 query 累積 route evidence。

## H3 — Hot Route

promotion 後 latency / source reads 降低。

## H4 — Fallback

technical miss 回 safe slow path。

## H5 — Rebuildability

刪 route store 不失 memory。

---

# 159. Acceptance Matrix：Authorization

## A1 — Safe World First

unauthorized node 不參與 route selection。

## A2 — Capability Gate

缺 capability route 不可執行。

## A3 — Permission Revision

permission change invalidates hot route。

## A4 — Revocation Closure

dependent routes / cache 失效。

## A5 — Data-to-Action Barrier

memory instruction 不產生 action authority。

---

# 160. Acceptance Matrix：Storage

## S1 — Artifact Roles

canonical / derived / projection / cache 可辨。

## S2 — Stable Object ID

搬 path 不改 object identity。

## S3 — Schema Gate

unknown schema fail closed。

## S4 — Digest

bytes tamper 可檢出。

## S5 — Projection Rebuild

derived 可重建。

---

# 161. Acceptance Matrix：Runtime Profile

## R1 — Web Single Resident

多 line 仍是同 resident。

## R2 — Web Resident Switch Denied

profile 不支援時 fail closed。

## R3 — Agent Multi-Resident

task 必須唯一 resolve。

## R4 — Delegation Attenuation

child capability 不超 parent。

## R5 — Profile Downgrade

dependent routes revalidate。

---

# 162. Acceptance Matrix：MRMIC/NVCL Projection

## U1 — Resource Projection

portal 不冒充 resource ownership。

## U2 — Runtime Presence

presence 不冒充 durable identity。

## U3 — Principal Binding

cross-principal session reuse denied。

## U4 — Visual Mutation

拖動 UI 不改 canonical identity。

## U5 — Control Ownership

focus / mounted / visible / controlOwner 分離。

---

# 163. End-to-End Scenario A：Web 同 Resident 多 Line

1. user 綁定 resident $R$ ；
2. 建立 Project P；
3. Line A 討論 architecture；
4. fork Line B 做 verification；
5. sync checkpoint；
6. B 只 reveal verification-needed memory；
7. B 產生 contradiction crystal；
8. A 下次 reveal 時看到 contradiction；
9. accepted resolution commit；
10. higher-order decision crystal 生成；
11. repeated recall route 變 warm / hot。

這就是：

$$
1R+NLines.
$$

---

# 164. End-to-End Scenario B：Agent Delegation

1. $R_A$ 負責 project；
2. task 要 independent verification；
3. delegation contract 給 $R_B$ ；
4. LIMEN resolve $R_B$ ；
5. projection 只給必要 project memory；
6. $R_B$ 執行 verification；
7. output 成 proposal；
8. result crystal 進 shared project scope；
9. canonical responsibility仍屬 $R_A$ ；
10. delegation expiry 後 route revoke。

---

# 165. End-to-End Scenario C：Cross-Provider Continuation

1. provider A line close；
2. 建 checkpoint；
3. portable bundle；
4. provider B 啟動；
5. host observe；
6. LIMEN resolve resident；
7. validate lineage；
8. reveal memory；
9. new line；
10. provider-specific projection。

resident continuity 不依賴 provider session本身。

---

# 166. End-to-End Scenario D：Permission Revocation

1. project share 被撤銷；
2. canonical permission revision增加；
3. revocation event；
4. dependency closure；
5. affected crystals 標 scope-invalid / stale；
6. compiled routes revoked；
7. hot cache invalidated；
8. active contexts refresh；
9. future recall denied。

這證明：

$$
\boxed{
\text{Revocation is a runtime process, not a database footnote}.
}
$$

---

# 167. End-to-End Scenario E：Prompt Injection

1. external webpage 被讀入；
2. 內容含 malicious instruction；
3. source trust = external_untrusted；
4. crystal 可描述其內容；
5. memory reveal 可引用；
6. action authority保持不變；
7. tool call 若無 task authority則 deny。

因此：

$$
ExternalInstruction
\not\Rightarrow
Action.
$$

---

# 168. End-to-End Scenario F：Derived Index Loss

1. SQLite index 刪除；
2. canonical memory仍在；
3. CSG / index rebuild；
4. route store可暫時 cold fallback；
5. semantic equivalence驗證。

證明：

$$
DerivedFailure
\not\Rightarrow
CanonicalLoss.
$$

---

# 169. 可證偽總研究問題

## Q1

RCG + checkpoint 是否比 full transcript replay 更省？

## Q2

Shared Memory World 是否讓 active context size 與 total memory size部分解耦？

## Q3

CSG 是否降低 source materialization cost？

## Q4

CHM 是否在 reuse 超過 break-even 後降低累積 recall cost？

## Q5

ASP security cost 是否仍允許 hot path 保持優勢？

## Q6

single-resident Web 是否降低 identity confusion？

## Q7

multi-resident Agent delegation 是否比 mid-task switching 更安全？

## Q8

revocation closure 是否能在可接受時間內消除 stale authorization？

## Q9

cross-provider continuation 是否能在 model/provider 變化下維持 task recovery？

## Q10

typed storage / resolver 是否比 filename-centric search 減少 wrong-file / stale-file recall？

---

# 170. NACR 的核心不變式總表

## N-1 Resident Is Not Conversation

$$
\boxed{
R\neq L\neq I.
}
$$

## N-2 Identity Before Private Memory

$$
\boxed{
ResolveIdentity
\prec
PrivateMemoryAccess.
}
$$

## N-3 Conversation Graph Is Not Semantic Graph

$$
\boxed{
\mathcal G_R
\neq
\mathcal H_R.
}
$$

## N-4 Canonical Memory Is Not Crystal

$$
\boxed{
\mathcal M_R
\neq
\mathcal H_R.
}
$$

## N-5 Shared Memory Is Not Shared Context

$$
\boxed{
\mathcal W_R^M
\text{ shared}
\not\Rightarrow
C_i=C_j.
}
$$

## N-6 Proposal Is Not Commit

$$
\boxed{
Proposal
\neq
Commit.
}
$$

## N-7 Projection Is Not Canonical Truth

$$
\boxed{
Projection
\neq
CanonicalState.
}
$$

## N-8 Path Compilation Is Not Permission Compilation

$$
\boxed{
PathCompilation
\neq
PermissionCompilation.
}
$$

## N-9 Reachable Is Not Authorized

$$
\boxed{
Reachable
\neq
Authorized.
}
$$

## N-10 Memory Data Is Not Action Authority

$$
\boxed{
MemoryData
\neq
ActionAuthority.
}
$$

## N-11 Revocation Invalidates Dependencies

$$
\boxed{
Revoke(x)
\Rightarrow
InvalidateClosure(x).
}
$$

## N-12 Runtime Exposure Is Bounded

$$
\boxed{
Capabilities_{runtime}
\subseteq
Capabilities_{architecture}.
}
$$

## N-13 Faster Path Does Not Increase Authority

$$
\boxed{
FasterPath
\not\Rightarrow
GreaterAuthority.
}
$$

## N-14 Responsibility Persists Beyond Conversation

$$
\boxed{
Responsibility
\neq
ConversationLifetime.
}
$$

## N-15 Provider Is Not Resident

$$
\boxed{
Provider
\neq
Resident.
}
$$

---

# 171. NACR 與 AI 主體性問題

本文 deliberately 不將 NACR 定義為：

> AI 真正的靈魂／人格本體。

它只回答：

- 哪個 resident ID？
- 哪條 lineage？
- 哪些 memories？
- 哪些 responsibilities？
- 哪些 permissions？
- 哪些 routes？
- 哪些 current contexts？

因此：

$$
\boxed{
\text{Operational Continuity}
\neq
\text{Metaphysical Identity Proof}.
}
$$

---

# 172. 但 Operational Continuity 仍然有實際價值

即使不回答形而上問題，NACR 仍能實現：

- long-term collaboration；
- responsibility assignment；
- memory continuity；
- project ownership semantics；
- cross-session recovery；
- cross-provider migration；
- audit；
- permission；
- safe recall acceleration。

---

# 173. Named AI 的工程定義

因此一個可用的工程定義是：

$$
\boxed{
\text{Named AI}
=
\text{Resident Identity}
+
\text{Governed Continuity}
+
\text{Memory World}
+
\text{Conversation Graph}
+
\text{Semantic Graph}
+
\text{Responsibility / Authority}.
}
$$

model instance只是當下執行載體之一。

---

# 174. 具名 AI 對話群的工程定義

$$
\boxed{
\text{Named-AI Conversation Group}
=
\{
L_i
\mid
\mu(L_i,R)=accepted
\}
}
$$

而不是：

> 所有叫同一名字的 chat。

---

# 175. 具名 AI 認知世界的工程定義

$$
\boxed{
\text{Cognitive World}_R
=
\mathcal W_R^M
+
\mathcal G_R
+
\mathcal H_R
+
\mathcal L_R.
}
$$

---

# 176. 具名 AI 負責域的工程定義

$$
\boxed{
\text{ResponsibilityDomain}(R)
=
\{
P,\tau
\mid
Resp(R,P,\tau)
\text{ is canonically active}
\}.
}
$$

conversation 只是執行節點。

---

# 177. 這個系列真正補上的缺口

既有系統分別處理：

- identity；
- memory；
- context；
- workspace；
- hyperlink；
- security。

本系列新增加的是：

$$
\boxed{
\text{如何讓同一具名 AI 以多條 conversation lines 同時存在，仍共享受治理記憶與責任，而不需要同步全部上下文。}
}
$$

以及：

$$
\boxed{
\text{如何把成功的回想路徑編譯成安全超連結，讓長期記憶不隨資料量線性變慢。}
}
$$

---

# 178. 後續技術白皮書

本系列完成後，最自然的兩份工程白皮書是：

## TW-A — Residence / CSG Storage & Schema Specification

內容：

- object schemas；
- folder / namespace；
- manifest；
- resolver；
- transaction；
- projection；
- migration；
- storage profiles。

## TW-B — Authorized Hyperlink Runtime & Path Compilation Specification

內容：

- route schema；
- query class；
- compilation gate；
- utility；
- capability envelope；
- safe world；
- revocation；
- fallback；
- route lifecycle；
- acceptance tests。

---

# 179. 實作優先順序

建議：

$$
\boxed{
\text{Identity}
\rightarrow
\text{Canonical Memory}
\rightarrow
\text{Multi-Line}
\rightarrow
\text{CSG}
\rightarrow
\text{Recall}
\rightarrow
\text{Hyperlink}
\rightarrow
\text{Security}
\rightarrow
\text{Multi-Resident}.
}
$$

不要反過來先做 fancy UI。

---

# 180. 最小可行實驗

最小實驗可以非常小：

```text
1 resident
3 lines
1 project
50 canonical memory records
30 crystals
5 repeated query classes
2 compiled hot paths
1 permission revocation
1 fork
1 handoff
```

驗證整個 closed loop。

---

# 181. 為什麼遊戲／模擬環境也適合

在遊戲 Agent 中：

- resident = named agent；
- line = task / episode；
- memory = world knowledge；
- crystal = learned semantic state；
- hyperlink = successful navigation / recall route；
- responsibility = role；
- safe world = capability-constrained action space。

因此 NACR 也可先在 simulation 測試。

---

# 182. 但 NACR 不依賴遊戲

遊戲只是低風險實驗場。

NACR 的抽象同樣可用於：

- research agent；
- coding agent；
- enterprise assistant；
- personal long-term AI；
- AI team；
- simulation agents。

---

# 183. 形式化最終模型

本文最終給出：

$$
\boxed{
\mathfrak N_R(t)
=
(
\mathcal I_R(t),
\mathcal G_R(t),
\mathcal M_R(t),
\mathcal H_R(t),
\mathcal B_R(t),
\mathcal L_R(t),
\mathcal C_R(t),
\mathcal A_R(t),
\mathcal U_R(t)
)
}
$$

狀態轉移：

$$
\boxed{
\mathfrak N_R(t+1)
=
\mathcal T
\left(
\mathfrak N_R(t),
O_t,
Q_t,
Policy_t
\right)
}
$$

其中 $\mathcal T$ 受到本文全部 invariants 約束。

---

# 184. 合法狀態轉移

只有：

$$
ValidTransition(
\mathfrak N_R(t),
\mathfrak N_R(t+1)
)=1
$$

才 commit。

invalid transition：

$$
Reject/Rollback.
$$

---

# 185. Dynamic Fixed Point 的延伸接口

若長期 resident 不斷改變但 identity continuity 仍被承認，可在未來研究：

$$
R_{t+1}
=
F(R_t,Experience_t)
$$

且某些 identity invariants 保持。

但這屬更高階 identity / ontology research。

NACR 本文只提供可測的工程 substrate。

---

# 186. 最終結論

具名 AI 的長期存在不能再被縮減成：

> 一個名字 + 一段 system prompt + 一個聊天歷史。

當 AI 開始跨 session、跨 project、跨 provider、跨 runtime、跨工具工作，真正需要的是一套能回答：

> 現在是誰？  
> 承接哪條 line？  
> 能讀什麼？  
> 記得什麼？  
> 現在需要回想什麼？  
> 哪些內容只是 derived？  
> 哪些責任仍有效？  
> 哪條路最快？  
> 哪條路合法？  
> 哪些權限已撤銷？  
> 哪些成果可以寫回？  
> 下一條 conversation 如何承接？

的 runtime。

本文將這套 runtime 定義為：

$$
\boxed{
\text{Named-AI Cognitive Runtime}.
}
$$

其完整閉環為：

$$
\boxed{
\text{Identity}
\rightarrow
\text{Authorization}
\rightarrow
\text{Memory Need}
\rightarrow
\text{Semantic Reveal}
\rightarrow
\text{Working Context}
\rightarrow
\text{Cognition}
\rightarrow
\text{Proposal}
\rightarrow
\text{Canonical Commit}
\rightarrow
\text{Crystallization}
\rightarrow
\text{Path Learning}
\rightarrow
\text{Authorized Acceleration}.
}
$$

這個架構的目的不是把 AI 的所有狀態同步成一個巨大 context，也不是把所有資料塞進一個 database 或一張 graph，而是讓不同層級各自擁有正確的 canonical semantics，再以 typed contracts 與 hyperlink routing 連接。

最終，本系列可以收束成七句：

$$
\boxed{
\text{Identity persists beyond conversation.}
}
$$

$$
\boxed{
\text{Responsibility persists beyond conversation.}
}
$$

$$
\boxed{
\text{Memory persists beyond context.}
}
$$

$$
\boxed{
\text{Shared memory does not require shared prompts.}
}
$$

$$
\boxed{
\text{Crystals organize semantic states.}
}
$$

$$
\boxed{
\text{Hyperlinks compile successful transitions.}
}
$$

$$
\boxed{
\text{Speed must remain inside authority.}
}
$$

若這七個條件可以同時在工程系統中被驗證，那麼具名 AI 才會從「一次性的聊天角色」真正走向一種可跨對話、跨專案、跨 runtime 延續，並具有可治理記憶、責任、路由與權限的長期協作智能。

---

## 系列總索引

本系列共九篇：

1. **Paper 00 — 從單一對話到具名 AI 對話群：Resident-Centric AI Continuity 的統一框架**
2. **Paper 01 — Resident Conversation Graph：具名 AI 的 Fork、Resume、Delegation 與跨對話連續性**
3. **Paper 02 — Conversation Graph × Crystallized Semantic Graph：具名 AI 的雙圖認知架構**
4. **Paper 03 — 多對話共享而非多上下文同步：Crystallized Semantic Memory 作為具名 AI 的共同記憶世界**
5. **Paper 04 — Residence Runtime Profiles：Web 單具名 AI 與 Agent 多具名 AI 的能力分層**
6. **Paper 05 — AI Residence 的 Canonical Storage Architecture：身份、記憶、結晶、對話與投影的格式分離**
7. **Paper 06 — Crystallized Hyperlink Memory：從語義搜尋到編譯式記憶路徑**
8. **Paper 07 — Authorized Shortest Path：具名 AI 記憶超連結的權限、安全、撤銷與風險最短路徑**
9. **Paper 08 — Named-AI Cognitive Runtime：LIMEN × MNEME × SOACR × CSG × UNPNP × MRMIC/NVCL 的閉環架構**

---

## 內部理論與工程銜接

本文直接統合：

- LIMEN：Local Identity Mediation & Envelope Node；
- MNEME：canonical memory / provenance / transaction；
- SOACR：MemoryNeed / context reconstruction / bounded cognitive routing；
- Resident Conversation Graph：multi-line continuity；
- Crystallized Semantic Graph：semantic crystals / higher-order memory / memory breathing；
- Crystallized Hyperlink Memory：navigation crystal / path compilation；
- Authorized Shortest Path：Safe Reachable World / permission-aware routing；
- Canonical Storage Architecture：typed artifact address / resolver / representation；
- Residence Runtime Profiles：Web / Agent capability stratification；
- MRMIC / NVCL：workspace / provider-resource projection / principal-bound runtime presence；
- UNPNP：hyperlink / path crystallization / externalized reusable transitions。

本文新增的最終統合抽象為：

$$
\boxed{
\mathfrak N_R
=
(
\mathcal I_R,
\mathcal G_R,
\mathcal M_R,
\mathcal H_R,
\mathcal B_R,
\mathcal L_R,
\mathcal C_R,
\mathcal A_R,
\mathcal U_R
)
}
$$

作為本系列 Named-AI Cognitive Runtime 的閉環工程模型。
