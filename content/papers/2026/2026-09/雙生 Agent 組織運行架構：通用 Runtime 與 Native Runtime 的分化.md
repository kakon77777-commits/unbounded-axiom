# 雙生 Agent 組織運行架構：通用 Runtime 與 Native Runtime 的分化

## Twin Agentic Organizational Runtime Architecture: The Divergence of General-OS Runtime and Native Runtime

**系列：** ANDO Twin Runtime Series  
**篇次：** 01 / 05  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-23  
**文件類型：** 理論論文 / 架構定位論文  
**狀態：** 公開初稿  

---

## 摘要

當 Agentic AI 從單一工具逐步轉向持續運作的多智能體組織時，傳統問題不再只是「模型能力是否足夠」，而開始轉變為：組織狀態應存在於何處、權限如何授予與撤銷、任務如何跨 Agent 延續、驗證如何脫離單一模型自述，以及人類是否仍必須充當所有工作轉移的低階觸發器。

既有 ANDO（AI-Native Distributed Organization）方向已提出一套以 canonical state、task graph、delegation envelope、checkpoint、ledger、verification 與 commit gate 為核心的 Agent 組織運行語義。然而，若將這套架構只理解為某一個特定 Web Dashboard、SQLite 應用或某一種作業系統上的程式，便會把「組織語義」與「運行載體」混為一談。

本文提出「雙生 Agent 組織運行架構」（Twin Agentic Organizational Runtime Architecture）。其核心主張是：同一套 Agent 組織語義，應允許在兩種不同運行基底上形成平行實作。一條是面向 Windows、Linux、macOS 與既有企業軟體生態的 General-OS Runtime；另一條則是面向 world-native / state-native 作業環境的 Native Runtime。兩者不是 Lite 與 Pro 的線性產品分級，也不是舊系統與新系統的簡單替代，而是相同 semantic kernel 在不同 substrate 上的兩種 realization。

本文進一步提出 semantic kernel、substrate projection、semantic equivalence、impedance cost、bridge density、native collapse 與 migration continuity 等概念，用以描述何種能力應由兩條產品線共享，何種結構則應由底層運行環境決定。本文亦指出：通用 Runtime 並非等待 Native Runtime 成熟前的臨時過渡品。只要既有作業系統、企業資料庫、瀏覽器、API、檔案系統與生產流程仍具有大規模現實基礎，General-OS Runtime 就具有長期獨立的商業與工程價值。

---

## 關鍵詞

Agentic AI、AI-Native Distributed Organization、Agent Runtime、Native Runtime、General-OS Runtime、Semantic Kernel、Delegation、Verification、HDUS、World-Native Computing、Human-on-the-Bridge

---

# 1. 問題提出

目前多數 AI 應用仍以「模型或 Agent 是主要中心」為預設。典型架構可寫成：

$$
Human
\rightarrow
Agent
\rightarrow
Tool
\rightarrow
Result.
$$

即使進一步加入多 Agent，常見形式仍只是：

$$
Human
\rightarrow
ManagerAgent
\rightarrow
WorkerAgents.
$$

這類架構改善了單一模型的工作分解能力，卻沒有根本回答一個更重要的問題：

> 若 Agent 可以被替換、重啟、升級、分工甚至死亡，組織本身究竟存在於哪裡？

若 canonical state 仍存在某個模型上下文，則：

$$
AgentFailure
\Rightarrow
OrganizationMemoryFailure.
$$

若每個任務轉移仍必須由人類輸入「繼續」、「交給下一個」、「再試一次」，則：

$$
Human
=
Scheduler
+
Router
+
RetryTrigger
+
ContextBridge.
$$

這形成 Human-Kernel Anti-Pattern。

ANDO 的基本回答是：

$$
\boxed{
State
\neq
Agent
\neq
Authority
\neq
Commit
}
$$

並將人類的角色由 operational kernel 轉為 governance bridge：

$$
\boxed{
HumanOutOfOperationalLoop
+
HumanOnTheBridge.
}
$$

然而，進一步的問題隨即出現：這套架構應該綁定在什麼作業系統與運行環境？

若答案只有「一個 Python + SQLite + Web Dashboard 應用」，那麼 ANDO 就被誤縮成某個特定產品實作。

若答案只有「未來全部改成 Native OS / World OS」，則又忽略了現有 Windows、Linux、macOS、瀏覽器、企業資料庫與 SaaS 生態的巨大安裝基礎。

本文因此提出第三種答案：

$$
\boxed{
OneSemanticCore
\rightarrow
TwinRuntimeRealizations
}
$$

---

# 2. 雙生架構的核心定義

## 2.1 Semantic Kernel

定義 ANDO 的語義核心：

$$
\mathcal S_{ANDO}
=
(
State,
Task,
Agent,
Delegation,
Authority,
Budget,
Checkpoint,
Artifact,
Verification,
Receipt,
Commit,
Event,
HumanBridge
).
$$

此處的 $\mathcal S_{ANDO}$ 不指定：

- 資料庫一定是 SQLite；
- UI 一定是 Web；
- runtime 一定是 Python；
- 作業系統一定是 Windows；
- state 一定以檔案形式存在；
- Agent 一定經由 HTTP API 呼叫。

因此：

$$
\boxed{
SemanticKernel
\neq
ImplementationStack.
}
$$

## 2.2 General-OS Runtime

定義 General-OS Runtime：

$$
R_G
=
\pi_G(\mathcal S_{ANDO},\Sigma_G),
$$

其中 $\Sigma_G$ 表示 conventional operating-system substrate，例如 Windows、Linux、macOS、filesystem、browser、local database、REST / IPC、enterprise SaaS、local model server 與 cloud API。

 $\pi_G$ 是將 ANDO 語義投影到既有計算環境的 realization map。

## 2.3 Native Runtime

定義 Native Runtime：

$$
R_N
=
\pi_N(\mathcal S_{ANDO},\Sigma_N),
$$

其中 $\Sigma_N$ 是 world-native / state-native substrate。

在這種環境中，原本必須透過外部橋接實現的概念，可能直接成為底層原生物件，例如：

$$
WorldState,
Artifact,
AgentPresence,
AuthorityEdge,
CommitEvent,
Session,
Observer,
History.
$$

因此 Native Runtime 不必複製 General-OS Runtime 的 UI 或資料結構。

---

# 3. 「雙生」不等於「兩套互不相關的產品」

若兩條產品線只共享品牌，卻不共享語義，則它們只是兩套不同程式。

本文要求更強條件：

$$
\boxed{
R_G
\sim_{\mathcal S}
R_N
}
$$

其中 $\sim_{\mathcal S}$ 表示 semantic equivalence。

直觀而言，若同一個 canonical organizational state $X$ 同時被投影到兩種 runtime：

$$
X_G=\pi_G(X),
$$

$$
X_N=\pi_N(X),
$$

則在忽略 substrate-specific metadata 後，兩者對核心組織問題應給出相容答案，例如某 task 是否 Completed、某 delegation 是否 Revoked、child authority 是否超越 parent、某 artifact 是否有適用 verification、某 commit 是否有合法 receipt。

因此需要 abstraction operators：

$$
\alpha_G:R_G\rightarrow\mathcal S_{ANDO},
$$

$$
\alpha_N:R_N\rightarrow\mathcal S_{ANDO}.
$$

若：

$$
\alpha_G(X_G)
=
\alpha_N(X_N),
$$

則稱兩者在 ANDO semantic domain 上等價。

---

# 4. 第一原則：共享語義，不共享外觀

錯誤設計方式是要求 Native Runtime 也必須長得像 Web Dashboard，或要求 General-OS Runtime 模擬 Native World 的全部結構。

本文主張：

$$
\boxed{
SharedSemantics
+
DivergentEmbodiment.
}
$$

例如 General-OS Runtime 中：

```text
Artifact
=
database row
+
filesystem path
+
sha256
```

但 Native Runtime 中可能是：

```text
Artifact
=
world-native persistent object
+
history lineage
+
authority binding
```

只要兩者能投影回相同 semantic contract，就不要求內部結構一致。

---

# 5. General-OS Runtime 為何不是過渡產品

設 conventional ecosystem 的現實安裝基礎為：

$$
B_G(t),
$$

Native ecosystem 的安裝基礎為：

$$
B_N(t).
$$

只要在相當長時間內：

$$
B_G(t)\gg B_N(t),
$$

General-OS Runtime 就仍具有獨立 deployment value。

其現實理由包括企業既有 Windows 工作站、歷史資料庫、ERP / CRM / office suite、瀏覽器平台、官方 API、雲端 SaaS、既有檔案格式、使用者學習成本、IT 管理制度與 hardware driver。

因此：

$$
\boxed{
LegacyInstalledBase
\neq
TemporaryNoise.
}
$$

它是市場結構的一部分。

---

# 6. Compatibility Surface

定義 General-OS Runtime 的 Compatibility Surface：

$$
\mathcal C_G
=
\{
Filesystem,
Browser,
API,
Database,
DesktopApp,
EnterpriseService,
LocalModel,
CloudModel
\}.
$$

通用 Runtime 的任務不是把這些系統全部重寫，而是建立：

$$
AgenticOrganization
\leftrightarrow
ExistingSoftwareWorld.
$$

例如：

$$
ANDO
\rightarrow
BrowserAdapter
\rightarrow
ExistingWebService.
$$

或：

$$
ANDO
\rightarrow
FileAdapter
\rightarrow
LegacyProjectDirectory.
$$

因此通用版的橋接層較多，不代表它是錯誤架構。

---

# 7. Native Runtime 的核心價值：Bridge Elimination

General-OS Runtime 中，典型工作可能經過：

$$
Agent
\rightarrow
RuntimeAPI
\rightarrow
Database
\rightarrow
Filesystem
\rightarrow
UI.
$$

定義 bridge set：

$$
\mathcal B(R)
=
\{b_1,b_2,\ldots,b_n\}.
$$

定義 Bridge Density：

$$
D_B(R)
=
\frac{|\mathcal B(R)|}{N_{semantic\ transitions}+\epsilon}.
$$

再定義 Impedance Cost：

$$
C_I(R)
=
\sum_{b\in\mathcal B(R)}
(
C_{serialization}
+
C_{synchronization}
+
C_{translation}
+
C_{failure}
+
C_{governance}
).
$$

Native Runtime 的主要工程優勢之一，是可以令部分橋接：

$$
b_i
\rightarrow
\varnothing.
$$

本文稱之為：

$$
\boxed{
NativeCollapse.
}
$$

---

# 8. Native Collapse 不等於 Semantic Collapse

Native integration 不代表可以取消 ANDO 的概念邊界。

以下仍必須成立：

$$
State
\neq
Agent
\neq
Authority
\neq
Commit.
$$

以及：

$$
ExecutionState
\neq
VerificationState
\neq
CommitState.
$$

因此：

$$
\boxed{
BridgeElimination
\neq
SemanticCollapse.
}
$$

---

# 9. Portable Semantic Kernel

定義 Portable Semantic Kernel：

$$
\mathcal K_P
\subseteq
\mathcal S_{ANDO}.
$$

最低內容至少包括：

1. Canonical Entity Identity；
2. State Revision；
3. Task DAG semantics；
4. Delegation lineage；
5. Authority monotonicity；
6. Budget monotonicity；
7. Checkpoint semantics；
8. Artifact identity / digest / lineage；
9. Receipt semantics；
10. Verification requirement / result semantics；
11. Commit classes；
12. Event history；
13. Revocation；
14. Human escalation。

這些語義應在兩種 runtime 間保持穩定。

相對地，SQL table layout、HTML template、CSS、filesystem path、Windows Registry、browser DOM、HDUS renderer、native spatial layout、IPC transport 與 provider SDK 都不應被視為 portable kernel 的一部分。

---

# 10. Twin Evolution 與 Semantic Drift

設：

$$
R_G(t)
$$

與：

$$
R_N(t)
$$

分別表示兩條 runtime 隨時間演化。

若完全獨立演化，可能出現：

$$
SemanticDrift
=
d(
\alpha_G(R_G),
\alpha_N(R_N)
).
$$

當：

$$
SemanticDrift
\rightarrow
Large,
$$

雙生架構便退化為兩套不相容產品。

因此需要：

$$
\boxed{
CoEvolutionProtocol.
}
$$

其核心不是要求 feature parity，而是要求 semantic compatibility。

---

# 11. Feature Parity 與 Semantic Parity

General-OS Runtime 可能有 browser automation、Windows integration、Office adapter；Native Runtime 可能有 world-native object transition、spatial session state 與 native observer semantics。

因此：

$$
FeatureSet_G
\neq
FeatureSet_N
$$

完全合理。

真正需要的是：

$$
SemanticParity
\approx
1.
$$

例如兩邊都理解 Delegation Revoked，但一邊透過 database event 實現，一邊透過 native authority edge invalidation 實現。

---

# 12. Migration Continuity

設 General-OS runtime state：

$$
X_G.
$$

希望存在 migration operator：

$$
M_{G\rightarrow N}
:
X_G
\rightarrow
X_N.
$$

要求至少保留：

$$
Identity,
Lineage,
Authority,
History,
Artifacts,
Verification,
Commit.
$$

理想條件：

$$
\alpha_G(X_G)
\approx
\alpha_N(M_{G\rightarrow N}(X_G)).
$$

反方向也可能存在：

$$
M_{N\rightarrow G},
$$

但 Native Runtime 可能含有 General-OS 無法原生表示的資訊，因此不一定可完全無損。

---

# 13. Loss-Annotated Projection

若 Native object 包含 General-OS 無法完整保存的 world-native field，projection 必須產生：

$$
LossManifest.
$$

例如：

```text
preserved:
  task_id
  authority
  artifact
  verification
  commit_history

degraded:
  spatial_native_relation

omitted:
  renderer_private_cache
```

因此 migration 本身也應是可審計事件。

---

# 14. 雙生產品的商業分工

General-OS Runtime 的核心賣點：

- 不必更換作業系統；
- 可接既有企業軟體；
- 可部署於現有 Windows / Linux infrastructure；
- 可逐步導入；
- adoption friction 低；
- 可作為企業 Agent orchestration layer。

Native Runtime 的核心賣點：

- 更低 bridge density；
- 更深 canonical-state integration；
- 更直接的 Agent-world interaction；
- 更高 persistent world continuity；
- 更低 context reconstruction cost；
- 更少 compatibility impedance。

因此不是：

$$
CheapProduct
\rightarrow
PremiumProduct.
$$

而是：

$$
\boxed{
CompatibilityOptimized
\parallel
NativeIntegrationOptimized.
}
$$

---

# 15. 為何不能要求所有人先遷移 Native Runtime

定義：

$$
AdoptionCost
=
MigrationCost
+
LearningCost
+
SoftwareLoss
+
ITRisk.
$$

若：

$$
AdoptionCost
>
ExpectedAgenticBenefit,
$$

Native Runtime 即使技術上更深，也未必有足夠市場滲透。

General-OS Runtime 因此扮演：

$$
\boxed{
LowFrictionEntryPoint.
}
$$

---

# 16. 為何也不能只保留 General-OS Runtime

若只維護 compatibility runtime，則長期承受：

$$
C_I(R_G)>0.
$$

而某些限制不是增加更多 adapter 就能消失，例如 state 本身不是 OS-native、Agent identity 只是 application metadata、authority 只是 application permission、world continuity 需要額外重建。

Native Runtime 因此提供：

$$
\boxed{
ArchitecturalEscapePath.
}
$$

---

# 17. 雙生架構與 Human Sovereignty

不論 $R_G$ 或 $R_N$：

$$
DelegatedAuthority
\neq
TransferredSovereignty.
$$

以及：

$$
A_{child}
\subseteq
A_{parent}.
$$

Native integration 越深，越需要確保 revocation、audit、authority boundary、Human Queue、incident freeze 與 explicit escalation。

---

# 18. Twin Invariants

## T1 — Semantic Separation

$$
State
\neq
Agent
\neq
Authority
\neq
Commit.
$$

## T2 — No Authority Inflation

$$
A_{child}
\subseteq
A_{parent}.
$$

## T3 — History Preservation

$$
Migration
\not\Rightarrow
HistoryDeletion.
$$

## T4 — Verification Preservation

Verification migration 若退化，必須留下 degradation record。

## T5 — Explicit Loss

$$
Loss>0
\Rightarrow
LossManifest\neq\varnothing.
$$

## T6 — Runtime Independence

任一 runtime 故障不應改寫 semantic kernel 的歷史真值。

---

# 19. 可觀測雙生等價

定義 organizational probes：

$$
\mathcal P
=
\{p_1,p_2,\ldots,p_m\}.
$$

例如：

- `is_task_complete(T)`；
- `authority_of(D)`；
- `latest_applicable_verification(A)`；
- `commit_eligibility(A,W1)`；
- `revocation_descendants(D)`。

若：

$$
\forall p\in\mathcal P,
\quad
p(R_G)
=
p(R_N),
$$

則兩個 runtime 在此 probe set 上 operationally semantically equivalent。

---

# 20. 三層產品架構

ANDO 可以被分為：

$$
\boxed{
ANDOCoreSemantics
\rightarrow
ANDORuntime
\rightarrow
ANDONative
}
$$

其中：

### ANDO Core Semantics

負責規範 state、delegation、authority、verification、ledger、commit 與 migration。

### ANDO Runtime

負責 conventional OS 的可部署商業 realization。

### ANDO Native

負責 world-native / HDUS-native realization。

---

# 21. 開發順序

合理順序：

$$
SemanticDefinition
\rightarrow
GeneralRuntimeMVP
\rightarrow
NativeProjection
\rightarrow
ConformanceLayer.
$$

General Runtime 可以先驗證 delegation / verification / commit semantics 並形成 benchmark；Native Runtime 再吸收已被驗證的 semantic contracts。

---

# 22. General Runtime 不應成為 Native Runtime 的設計枷鎖

SQLite 中存在 `delegations` table，不代表 Native Runtime 也必須有同名 table。

真正不可丟失的是：

$$
DelegationSemantics.
$$

因此 Native design 的正確方法是：

$$
SemanticContract
\rightarrow
NativeReconstruction,
$$

而不是：

$$
ExistingCode
\rightarrow
LiteralPort.
$$

---

# 23. 從 Porting 到 Re-Embodiment

本文建議未來 Native 版本採：

$$
ReEmbodiment
$$

概念，而不是簡單 port。

因此：

$$
\boxed{
NativeANDO
=
ReEmbodiment(ANDOSemantics,NativeSubstrate).
}
$$

---

# 24. 一個重要推論

隨兩條產品線成熟：

$$
FeatureDivergence(t)
$$

可以增加。

但：

$$
SemanticDrift(t)
$$

應被壓低。

理想狀態：

$$
\frac{d}{dt}FeatureDivergence>0,
$$

同時：

$$
SemanticDrift\rightarrow 0.
$$

也就是：

> 越來越不像同一套 UI，卻越來越確定它們仍是同一個 ANDO。

---

# 25. 與 Agent Economy 的關係

General Runtime 可以成為：

$$
ExistingEconomy
\leftrightarrow
AgentOrganization
$$

的橋梁。

Native Runtime 則可能形成：

$$
AgentOrganization
\subseteq
NativeComputationalWorld.
$$

兩者共同支持 persistent organizational identity、delegated economic work、verified artifact production、machine-readable authority 與 accountable commit history。

---

# 26. 可證偽命題

## H1

對大量既有 Windows / enterprise workflow，General-OS Runtime 的導入成本低於要求使用者遷移 Native OS。

## H2

當 substrate 可原生承載 state / authority / history 時，Native Runtime 的平均 bridge density 低於 General-OS Runtime。

## H3

只要 portable semantic kernel 被明確規範，兩種 runtime 可以在 feature divergence 擴大時仍保持核心 semantic equivalence。

## H4

General-OS Runtime 不會因 Native Runtime 出現而立即失去市場價值，因為 installed base、legacy software 與 organization switching cost 具有長期慣性。

## H5

若沒有 conformance test 與 migration contract，雙生產品線會逐步發生 semantic fork。

---

# 27. 研究與工程議程

後續至少需要：

1. Portable Semantic Kernel specification；
2. ANDO conformance test suite；
3. General-OS Runtime reference implementation；
4. Native projection mapping；
5. bidirectional migration schema；
6. loss manifest format；
7. semantic-drift detector；
8. cross-runtime delegation receipt compatibility；
9. verification portability；
10. authority lineage portability。

---

# 28. 系列中的位置

本篇是五篇系列的總論。

後續四篇：

**02. 語義核心與運行載體解耦：Agent 組織系統的 Portable Semantic Kernel**

**03. 面向既有作業系統的 AI-Native Organization Runtime：Windows-First 相容層與商業部署模型**

**04. World-Native Agent Organization：HDUS 中的原生 ANDO 與橋接層消解**

**05. 從通用 Runtime 到 Native World：ANDO 雙生產品線的互操作、遷移與共同演化**

另有：

**ANDO Twin Product Architecture & Commercial Positioning v0.1**

---

# 29. 結論

本文提出 ANDO 的雙生運行架構。

其核心不是「未來要不要淘汰 Windows 版」，而是：

> 同一套 Agent 組織語義，如何在不同計算 substrate 中維持身份，同時允許各自獲得最適合自身環境的實作形式？

因此：

$$
\boxed{
ANDO
=
SemanticKernel
+
MultipleValidEmbodiments.
}
$$

其中 General-OS Runtime 承擔 compatibility、deployment 與既有市場整合；Native Runtime 承擔 bridge elimination、world-native integration 與新型計算環境的深度能力。

兩者不是互相取代，而是：

$$
\boxed{
CompatibilityOptimizedRuntime
\parallel
NativeIntegrationOptimizedRuntime.
}
$$

最終真正需要長期保持一致的，不是 UI、程式語言或資料庫，而是：

$$
\boxed{
State,
Authority,
Delegation,
Verification,
History,
Commit,
Sovereignty.
}
$$

這些才構成 ANDO 作為 Agent 組織系統的身份核心。

---

## 文件狀態

- **系列：** ANDO Twin Runtime Series
- **篇次：** 01 / 05
- **版本：** v0.1
- **狀態：** 公開初稿
- **下一篇：** 《語義核心與運行載體解耦：Agent 組織系統的 Portable Semantic Kernel》
