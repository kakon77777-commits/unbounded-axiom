# 雙生智能體治理：分散式 AI 組織中的雙核心控制、雙向驗證與反身調度

**Twin-Agent Governance: Dual-Core Control, Bidirectional Verification, and Reflexive Scheduling in Distributed AI Organizations**

**系列**：FCAO / Fractal Conversational Agent Organization  
**文件編號**：EML-FCAO-2026-01-v0.1  
**文件類型**：Theory / Governance Paper  
**作者**：Neo.K  
**協作**：Aletheia / GPT-5.6 Sol  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-24  
**狀態**：Research Draft / Canonical UTF-8 Source  
**直接前置**：`EML-FCAO-2026-00-v0.1`、ANDO、CTCL-ITR、Software Spacetime、SEDB、Addressable Cognitive Runtime、Self-Constraint Experimental Harness  
**後續預定**：FCAO Temporal-Topological Computation Paper、FCAO Twin-Core Reference Architecture、FCAO × OpenHarness Integration Whitepaper  
**新穎性聲明**：本文不主張 verifier、critic、supervisor、redundant controller、multi-agent debate、fault-tolerant replication 或 coordinator-worker pattern 本身為首創。本文提出的是一個待比較與待實驗的統合治理命題：在 Conversation-local / project-local 的局部類全域 AI 域中，以持續存在且彼此可審視的 Primary–Twin 雙核心，結合 bottom-up evidence aggregation、top-down probe / reopen / repartition、selective audit、local closure certificate 與 bounded arbitration，形成可遞歸的雙向治理拓樸。

---

## 生成與保真聲明

本文為正式 UTF-8 Markdown source。數學原始碼只使用 ` $...$ ` 與 `$$...$$` 作為 canonical delimiter；不以 Unicode 數學字元替代 LaTeX source，不進行 unicode escape 類 round-trip。正式 package 附帶 JSON Schema、YAML profile、驗證報告與 SHA-256 指紋。

本文刻意區分：

1. **已有工程能力**：多 Agent、coordinator、subagent、verifier、message passing、background execution、MCP / CLI / API 等；
2. **本文提出的治理抽象**：Primary–Twin、雙向治理邊、selective audit、reopen / repartition、local closure certificate、temporary arbiter；
3. **尚待實驗的效率主張**：雙生架構是否能在特定錯誤率、任務拓樸、驗證成本與返工成本下，同時降低總成本、平均完成時間與 late-stage recomputation。

本文不宣稱保存或要求暴露 hidden chain-of-thought。治理所需的是可驗證 state、artifact、receipt、decision summary、evidence、authority 與 closure certificate。

---

# 摘要

多智能體系統常採用單一 coordinator / manager：上層模型分派工作，下層 Agent 執行，結果再回到上層彙整與驗證。此結構在工程上簡單，但容易形成一個隱含瓶頸：同一個上層 Agent 同時負責問題分解、子任務派發、結果理解、衝突處理、驗證、最終整合與完成宣告。當任務規模擴張時，系統可能先藉平行 Agent 降低局部執行時間，卻在最後的 single-root verification / integration 階段重新串行化；更嚴重時，Root AI 為了驗證子 Agent 結果而近似重新計算整個問題，使分散式執行的收益被 verification、integration 與 rework 成本抵消。

本文提出 **Twin-Agent Governance（雙生智能體治理）**。在一個 Conversation-local / project-local 的局部類全域 AI 域中，最小治理單位不再只是：

$$
Root
+
Children,
$$

而是：

$$
\boxed{
LocalGlobalAIUnit
=
Primary
+
Twin
+
EphemeralChildren.
}
$$

Primary AI 負責主要世界建模、規劃、委任、整合與 commit proposal；Twin AI 則作為獨立但同域的持續治理節點，負責 structural observation、selective verification、challenge、reopen、repartition、reassignment 與 meta-verification。Twin 不被定義為 Primary 的普通 child，也不被定義為一個完整複製 Primary 全部工作的 second executor。其價值來自 **非對稱、選擇性、風險導向的交叉監督**。

本文進一步將傳統單向 task graph：

$$
\mathcal G=(V,E)
$$

擴張為雙向治理圖：

$$
\boxed{
\mathcal G^{\leftrightarrow}
=
(V,E^{\uparrow},E^{\downarrow},E^{\times}),
}
$$

其中：

- $E^{\uparrow}$：result、evidence、receipt、artifact、local closure 向上聚合；
- $E^{\downarrow}$：audit、constraint、probe、reopen、repartition、reassignment 向下作用；
- $E^{\times}$：peer verification、cross-check、shared dependency、conflict relation 等橫向治理關係。

因此執行不再是一輪：

$$
Decompose
\rightarrow
Execute
\rightarrow
Merge,
$$

而可以形成：

$$
\boxed{
BottomUp
\rightarrow
GlobalInspection
\rightarrow
TopDownProbe
\rightarrow
LocalRepair
\rightarrow
BottomUp
\rightarrow
MetaVerification.
}
$$

本文提出 **Local Closure Certificate（LCC）**：子 Agent 不只回傳 `done`，而必須回傳 coverage、artifact、evidence、assumptions、open gaps、conflicts、verification status 與 lineage，使上層能做 certificate inspection，而非 full recomputation。Twin 依據 risk、uncertainty、graph centrality、failure impact、dependency depth、novelty 與 verification cost 建立 audit priority，只對高價值節點進行 fresh verification 或另派 audit Agent。

本文同時處理 Primary–Twin 的相互制衡。Twin 可以 challenge Primary 的 closure / integration decision；Primary 也可以拒絕缺乏證據或超越權限的 Twin intervention。當兩者在高風險 commit 上無法收斂時，系統可生成 **Temporary Arbiter Agent**，其 authority 僅限指定 dispute，完成後回收，避免永久第三核心。

本文最後提出一個待實證的成本條件：雙生治理只有在避免 full duplication、採 selective audit 並能提早阻斷錯誤傳播時才可能節省總成本。理想條件為：

$$
\boxed{
\mathbb E[C_{\mathrm{Twin}}]
<
\mathbb E[C_{\mathrm{SingleRoot}}],
}
$$

但本文不把此不等式當作先驗真理，而將其改寫為可測試假說。後續 FCAO 時間—拓樸論文將進一步建立 decomposition gain、temporal envelope、critical path、verification placement 與 dynamic repartition 的成本模型。

**關鍵詞**：Twin Agent、Dual-Core Governance、Primary AI、Independent Twin、Bidirectional Verification、Selective Audit、Reopen、Repartition、Local Closure Certificate、Meta-Verification、Fractal Agent Organization、CTCL-ITR、ANDO、Software Spacetime、SEDB

---

# 0. 理論定位：不是多一個 verifier，而是多一個治理核心

本文的起點不是：

> 每個工作結果最好再請另一個 AI 看一次。

這種做法早已存在於 code review、critic / verifier、agent debate、ensemble、redundant computation 與 fault-tolerant system 中。

本文真正提出的是：

> **當一個 Conversation / Project Domain 已被視為局部類全域 AI 域時，其上層治理是否應從單核心 Root 擴張為 Primary–Twin 雙核心，並使 Twin 持續參與 task topology、verification topology、reopen、repartition 與 closure，而不是只在最後做一次被動驗證？**

因此：

$$
\boxed{
Twin
\neq
FinalVerifier.
}
$$

也不是：

$$
\boxed{
Twin
=
DuplicatePrimary.
}
$$

本文定義：

$$
\boxed{
Twin
=
IndependentObserver
+
SelectiveVerifier
+
ChallengeNode
+
BoundedScheduler
+
MetaGovernancePeer.
}
$$

---

# 1. 單一 Root 架構的隱含問題

令 Root AI 為 $R$，子 Agent 集合為：

$$
\mathcal A
=
\{A_1,A_2,\ldots,A_n\}.
$$

最常見的工作流為：

$$
R
\rightarrow
\mathcal A
\rightarrow
R.
$$

其中 $R$ 同時執行：

$$
R
=
Planner
+
Dispatcher
+
Integrator
+
Verifier
+
ClosureJudge.
$$

這會產生五類問題。

## 1.1 Join bottleneck

若子 Agent 平行完成，但 Root 必須逐一重新閱讀與驗證：

$$
T_{\mathrm{total}}
\approx
\max_i T(A_i)
+
\sum_i T(V_i)
+
T_{\mathrm{integration}}.
$$

前段的平行化可能被後段串行 verification 抵消。

## 1.2 Self-confirmation risk

同一 Agent 建立分解方式、依賴假設與成功條件後，又由同一 Agent 判定自己的 decomposition 是否完整，容易形成：

$$
ModelError
\rightarrow
PlanError
\rightarrow
VerificationBlindSpot.
$$

此處不需要假設 AI 有心理偏誤；只要 inference / context / representation error 在同一計算路徑中具有相關性，就可能出現共同錯誤。

## 1.3 Late error discovery

若結構性問題直到 final merge 才被發現：

$$
Cost_{\mathrm{late}}
\gg
Cost_{\mathrm{local\ repair}}
$$

可能成立。

## 1.4 Closure authority concentration

若 Root 同時擁有：

$$
Decompose
+
Integrate
+
Verify
+
DeclareComplete,
$$

則「任務完成」高度依賴單一節點。

## 1.5 Verification as recomputation

若驗證沒有 receipt、test、certificate、artifact lineage，而只能重新推理原問題，則：

$$
VerificationCost
\approx
ExecutionCost
$$

甚至可能更高。

本文提出雙生治理，目的不是消滅 Root，而是避免所有治理職能在單一路徑上完全重合。

---

# 2. Conversation-local 雙生單位

延續 FCAO Foundation，令 Conversation-local project world 為：

$$
\mathcal W_C
=
(
State,
Goals,
Tasks,
Agents,
Artifacts,
Authority,
History,
Interfaces
).
$$

在此域中定義：

$$
P
=
Primary(\mathcal W_C),
$$

$$
T
=
Twin(\mathcal W_C).
$$

其中：

$$
P,T
\subset
\mathcal W_C.
$$

但：

$$
T
\not\preceq
P
$$

不應被理解為一般 child delegation。

同樣：

$$
P
\not\preceq
T.
$$

兩者是同一治理域內的 peer-like dual core，但其責任、authority 與 action class 可以不對稱。

因此：

$$
\boxed{
Primary
\parallel
Twin
}
$$

表示治理並置，不表示兩個 process 必須同步執行，也不表示兩者權限完全相等。

---

# 3. 雙生不等於身份複製

本文使用「雙生」描述治理結構，不要求兩個 Agent：

- 使用同一模型；
- 使用同一 provider；
- 具有同一 context；
- 具有同一 memory；
- 具有同一 tool set；
- 具有同一 system prompt；
- 具有同一 authority。

相反地，若 Twin 與 Primary 完全共享所有推理條件：

$$
Corr(Error_P,Error_T)
\rightarrow
1,
$$

則 Twin 的邊際驗證價值會下降。

因此 Twin 可以採異質配置：

$$
TwinProfile
=
(
Model,
ContextProjection,
Tools,
AuditPolicy,
Authority,
Budget
).
$$

理想設計不是追求「越不同越好」，而是降低不必要的 failure correlation，同時保持足夠共同語義以能理解同一 project world。

---

# 4. Primary AI 的責任

Primary 的第一代職責定義為：

$$
P
=
(
WorldModeling,
Planning,
Delegation,
Integration,
CommitProposal
).
$$

具體包括：

1. 建立 project objective；
2. 建立或更新 task / obligation topology；
3. 決定初始 decomposition；
4. 建立 Named Ephemeral Agents；
5. 設定 task contract 與 join condition；
6. 接收 bottom-up result；
7. 進行 integration；
8. 建立 candidate closure；
9. 建立 commit proposal；
10. 在 governance rule 允許時接受 Twin intervention。

Primary 不應被要求親自驗證所有 leaf artifact。

---

# 5. Twin AI 的責任

Twin 的第一代職責為：

$$
T
=
(
Observe,
Challenge,
SelectAudit,
Verify,
Redirect,
Repartition,
MetaVerify
).
$$

具體包括：

1. 觀察 task graph 狀態；
2. 檢查 decomposition 是否存在 missing region；
3. 監測高風險 dependency；
4. 選擇需要 fresh verifier 的節點；
5. 檢查 local closure certificate；
6. challenge unsupported merge；
7. 發起 `REOPEN`；
8. 建議或執行 bounded `REPARTITION`；
9. 建議停止低收益 Agent；
10. 建立 audit Agent；
11. 對 Primary candidate closure 做 meta-verification；
12. 在高風險 commit 前檢查 closure gate。

因此：

$$
\boxed{
Twin
=
Verifier
+
Scheduler
+
Controller
}
$$

但只有在其 authority envelope 允許的 action class 內成立。

---

# 6. Persistent Twin 與 Fresh Verifier 的區分

本文嚴格區分：

$$
PersistentTwin
\neq
FreshVerifier.
$$

Fresh verifier 適合處理：

- artifact correctness；
- test pass / fail；
- citation check；
- localized proof check；
- independent reproduction。

Persistent Twin 則處理：

- graph-wide observation；
- risk accumulation；
- repeated anomaly；
- cross-task conflict；
- topology hole；
- Primary integration challenge；
- temporal trend；
- repartition decision。

因此合理結構為：

$$
Twin
\rightarrow
Spawn(FreshVerifier_i)
$$

而不是讓 Twin 自己重算每一個子任務。

這是避免雙核心演化成「所有工作做兩遍」的核心設計。

---

# 7. 雙向治理圖

傳統 task graph 使用：

$$
\mathcal G
=
(V,E).
$$

本文擴張為：

$$
\boxed{
\mathcal G^{\leftrightarrow}
=
(V,E^{\uparrow},E^{\downarrow},E^{\times}).
}
$$

## 7.1 向上邊

$$
E^{\uparrow}
=
\{
result,
evidence,
receipt,
artifact,
closure\_certificate,
conflict,
exception
\}.
$$

## 7.2 向下邊

$$
E^{\downarrow}
=
\{
constraint,
probe,
reopen,
repartition,
reassign,
pause,
stop,
budget\_change
\}.
$$

## 7.3 橫向邊

$$
E^{\times}
=
\{
peer\_check,
shared\_dependency,
contradiction,
cross\_validation,
resource\_conflict
\}.
$$

因此組織不再只是樹：

$$
Parent
\rightarrow
Children.
$$

而是具有回授的 control topology。

---

# 8. Bottom-up aggregation：下往上不是只回文字

Leaf Agent $A_i$ 完成工作後，不應只回傳：

`done`

或一段自由文字。

本文定義 Local Result Packet：

$$
LRP_i
=
(
Artifact_i,
Claims_i,
Evidence_i,
Coverage_i,
Assumptions_i,
OpenGaps_i,
Conflicts_i,
Usage_i,
LocalCertificate_i
).
$$

其中：

$$
Usage_i
=
(
Time_i,
Token_i,
ToolCalls_i,
ExternalCost_i
).
$$

Bottom-up 的目的不是把所有原始 context 塞回 Root，而是形成可壓縮、可追溯、可局部驗證的治理物件。

---

# 9. Local Closure Certificate

定義 Local Closure Certificate：

$$
LCC_i
=
(
Scope_i,
SatisfiedObligations_i,
VerifiedArtifacts_i,
OpenGaps_i,
Assumptions_i,
Receipts_i,
Lineage_i,
Confidence_i
).
$$

其核心語義為：

> 對我被授予的這個有限作用域，我處理了哪些 obligation、哪些已驗證、哪些仍開放，以及上層若要接受我的輸出，必須知道哪些前提。

因此：

$$
\boxed{
LCC
\neq
ProofOfGlobalCorrectness.
}
$$

它只是 local accountability certificate。

若：

$$
OpenGaps_i
\neq
\varnothing,
$$

仍可以允許上層接受部分結果，只要 gap 被顯式傳遞，而不是被摘要吃掉。

---

# 10. Global inspection：上層重新看圖

當多個 LCC 向上聚合後，Primary 與 Twin 的工作不同。

Primary：

$$
P:
\{LCC_i\}
\rightarrow
CandidateIntegration.
$$

Twin：

$$
T:
\{LCC_i\}
+
\mathcal G
\rightarrow
StructuralInspection.
$$

Twin 主要檢查：

- 是否有未覆蓋 mandatory node；
- 是否有衝突 LCC；
- 是否有共同 assumption 沒被驗證；
- 是否有一個高中心性 node 被低品質結果支撐；
- 是否有多個 child 使用同一錯誤 source；
- 是否有 artifact / claim lineage 斷裂；
- 是否出現 verification gap；
- 是否有 bottom-up evidence 與 Primary integration 不一致。

---

# 11. Top-down probe：上往下不是重做整個專案

若 Twin 發現 anomaly $x$，不應立即要求全域重算。

定義 Probe：

$$
Probe_x
=
(
Target,
Question,
Reason,
Scope,
Budget,
EvidenceNeeded,
StopCondition
).
$$

Twin 可以建立 audit child：

$$
T
\rightarrow
A_x^{audit}.
$$

其目標不是重做 $Q$，而是最小化地回答：

$$
DoesAnomaly(x)\ Hold?
$$

或：

$$
WhichBranchCaused(x)?
$$

因此 top-down intervention 應遵守：

$$
\boxed{
MinimalNecessaryReopening.
}
$$

---

# 12. Reopen：完成可以被撤銷

FCAO Foundation 已定義 topology closure。本文加入：

$$
Closed(v,t_1)=1
$$

不保證：

$$
Closed(v,t_2)=1
$$

對所有 $t_2>t_1$ 成立。

若新證據、矛盾或 integration anomaly 出現，可以：

$$
REOPEN(v).
$$

Reopen receipt：

$$
RR_v
=
(
Reason,
Trigger,
Evidence,
AffectedDescendants,
RequiredAction,
Issuer
).
$$

因此 closure 是：

$$
\boxed{
VersionedClosure
}
$$

而不是一次宣告後永久不可逆。

---

# 13. Repartition：任務切分不是固定的

若原 decomposition：

$$
D_0(Q)
=
\{Q_1,Q_2,Q_3\}
$$

在執行後發現 $Q_2$ 同時承載兩個強耦合子域，Twin 或 Primary 可以提出：

$$
D_1(Q_2)
=
\{Q_{2a},Q_{2b}\}.
$$

也可以反向合併：

$$
Merge(Q_3,Q_4)
\rightarrow
Q_{34}.
$$

因此：

$$
\boxed{
Decomposition
=
DynamicStateDependentPolicy.
}
$$

這一點將在下一篇 Temporal-Topological Computation Paper 中加入成本與時間上下界。

---

# 14. Selective Audit：Twin 不應 full duplicate

若 Twin 對所有節點完整重算：

$$
C_{\mathrm{Twin}}
\approx
C_{\mathrm{Primary}}
+
C_{\mathrm{Duplicate}},
$$

則雙生架構很可能失去經濟性。

本文定義 audit priority：

$$
\Pi(v)
=
f(
Risk(v),
Uncertainty(v),
Centrality(v),
FailureImpact(v),
DependencyDepth(v),
Novelty(v),
Conflict(v),
VerificationCost(v)
).
$$

Twin 選擇：

$$
\mathcal V_{audit}
=
\{
v
\mid
\Pi(v)\ge \theta
\}.
$$

不同專案可以有不同 $\theta$。

高風險專案：

$$
\theta
\downarrow.
$$

低風險探索：

$$
\theta
\uparrow.
$$

因此：

$$
\boxed{
TwinCoverage
\neq
100\%\ FullRecompute.
}
$$

---

# 15. Verification placement 是 task topology 的一部分

傳統系統常把 verification 視為最後階段：

$$
Execute
\rightarrow
Verify.
$$

本文主張：

$$
\boxed{
VerificationTopology
\subseteq
TaskTopology.
}
$$

也就是某些驗證應該位於：

- leaf 完成後；
- branch merge 前；
- high-risk dependency 前；
- external commit 前；
- cross-domain translation 後；
- closure 前。

因此可定義：

$$
VPlace(v)
\in
\{
local,
branch,
merge,
global,
commit
\}.
$$

Twin 的重要任務之一，就是動態調整 verification placement。

---

# 16. Primary 與 Twin 的相互審視

雙生架構不能變成：

$$
Twin
>
Primary.
$$

也不能變成：

$$
Primary
>
Twin
$$

且 Twin 只是建議工具。

本文將兩者視為帶不同 authority classes 的治理 peer。

Primary 可以 challenge Twin intervention：

$$
Challenge_P(Action_T).
$$

Twin 可以 challenge Primary closure：

$$
Challenge_T(Closure_P).
$$

每個 challenge 都必須帶：

$$
ChallengeReceipt
=
(
Claim,
Evidence,
AffectedScope,
RequestedAction,
RiskClass
).
$$

禁止只以：

> 我覺得不對。

作為 governance-critical intervention 的唯一依據。

---

# 17. Commit gate：Twin 不必擁有所有 commit 權

不同 world-commit class 可以設定不同策略。

令 commit risk class：

$$
R_c
\in
\{
R_0,R_1,R_2,R_3,R_4
\}.
$$

例如：

- $R_0$：純內部草稿；
- $R_1$：可逆 local change；
- $R_2$：重要 repository change；
- $R_3$：外部發布 / 對外行動；
- $R_4$：高風險不可逆 action。

可設定：

$$
R_0:
PrimaryOnly,
$$

$$
R_1:
Primary+AuditOnDemand,
$$

$$
R_2:
Primary+TwinCheck,
$$

$$
R_3:
Primary+TwinConcurrence,
$$

$$
R_4:
Primary+Twin+HumanOrExternalGate.
$$

因此雙生不意味所有決策都要雙簽。

---

# 18. Disagreement：雙核心衝突怎麼辦

若：

$$
Decision_P
\neq
Decision_T,
$$

系統不應永遠 deadlock。

本文定義三階衝突策略。

## Level 1：Evidence exchange

雙方交換：

$$
Claim
+
Evidence
+
Receipt.
$$

## Level 2：Targeted fresh verification

生成：

$$
A^{fresh}_{verify}
$$

只處理 disagreement scope。

## Level 3：Temporary Arbiter

若仍未解：

$$
A_{arb}
=
TemporaryArbiter(
DisputeScope,
EvidenceBundle,
AuthorityEnvelope
).
$$

其生命週期：

$$
Lifetime(A_{arb})
=
UntilDisputeResolved.
$$

Arbiter 完成後回收。

因此：

$$
\boxed{
ThirdCore
\neq
Permanent.
}
$$

---

# 19. Temporary Arbiter 的權限限制

Temporary Arbiter 不應藉爭議取得整個 project authority。

令 dispute domain：

$$
\mathcal D_d
\subset
\mathcal W_C.
$$

則：

$$
Authority(A_{arb})
\preceq
Authority(\mathcal D_d).
$$

且：

$$
CommitClass(A_{arb})
\le
DisputeRequiredClass.
$$

它可以輸出：

- `PRIMARY_SUPPORTED`
- `TWIN_SUPPORTED`
- `BOTH_PARTIAL`
- `INSUFFICIENT_EVIDENCE`
- `REOPEN_REQUIRED`

但不自動取得與爭議無關的 project control。

---

# 20. 雙生架構的經濟性不是先驗真理

本文拒絕直接假設：

$$
Twin
\Rightarrow
Cheaper.
$$

完整成本：

$$
C_{\mathrm{twin}}
=
C_P
+
C_T
+
C_{audit}
+
C_{communication}
+
C_{coordination}
+
C_{arbitration}
+
C_{rework}.
$$

單 Root：

$$
C_{\mathrm{single}}
=
C_R
+
C_{verification}
+
C_{integration}
+
C_{lateRework}.
$$

雙生有經濟性的條件是：

$$
\boxed{
\mathbb E[C_{\mathrm{twin}}]
<
\mathbb E[C_{\mathrm{single}}].
}
$$

其主要節省來源不是 `C_T=0`，而是：

$$
EarlyDetectionSavings
+
ReducedFullRecompute
+
ReducedLateRework
+
BetterVerificationPlacement.
$$

---

# 21. 提早發現錯誤的價值

令 error $e$ 在 dependency depth $d$ 被發現。

若錯誤向後污染：

$$
Desc(e)
=
\{v_j\mid e\leadsto v_j\},
$$

則 late correction cost 可近似：

$$
C_{late}(e)
=
C_{detect}
+
C_{repair}(e)
+
\sum_{v_j\in Desc(e)}C_{invalidate}(v_j).
$$

若 Twin 在較早 depth 發現：

$$
C_{early}(e)
<
C_{late}(e)
$$

的可能性上升。

因此 Twin 的經濟價值與：

$$
ErrorPropagationDepth
$$

高度相關。

---

# 22. 雙生系統可能更貴的情況

雙生治理不是永遠優勢。

以下條件可能使其失去收益：

1. 任務極小；
2. 子任務高度可驗證且幾乎無 integration risk；
3. Twin 與 Primary 高度相關，沒有新增資訊；
4. audit threshold 太低導致過度驗證；
5. communication overhead 高；
6. Twin 頻繁 reopen 造成 thrashing；
7. arbiter 過度生成；
8. task graph 本身錯誤，使 Twin 監督錯圖；
9. verification cost 大於 potential rework saving；
10. project deadline 極短而 intervention latency 太高。

因此系統必須允許：

$$
TwinMode
\in
\{
OFF,
LIGHT,
SELECTIVE,
STRICT
\}.
$$

---

# 23. Twin Mode

## OFF

$$
TwinActivity=0.
$$

適用極小、低風險、可逆任務。

## LIGHT

Twin 只做：

- closure check；
- high-risk anomaly；
- final meta-verification。

## SELECTIVE

Twin 持續監測，依 $\Pi(v)$ 觸發 audit。

## STRICT

高風險專案採更高 coverage、更多 independent verifier 與更嚴 commit gate。

因此雙生不是固定成本，而是 adaptive governance capacity。

---

# 24. 失敗相關性：兩個 AI 一起錯

雙生架構的重要限制是 correlated failure。

若 Primary 與 Twin：

- 使用同一錯誤資料；
- 使用同一錯誤測試；
- 使用同一錯誤 ontology；
- 共享同一 context corruption；
- 使用同一不可觀察 blind spot；

則：

$$
P(Error_P\cap Error_T)
$$

可能很高。

因此需要 distinction：

$$
ModelDiversity
\neq
EvidenceDiversity
\neq
ToolDiversity
\neq
ContextDiversity.
$$

真正重要的是針對 failure mode 選擇 diversity，而不是機械式「一定用不同模型」。

---

# 25. Twin independence 的第一代定義

本文不要求統計獨立，只要求治理上的 minimum independence：

$$
Ind(T)
=
(
SeparateDecisionState,
IndependentChallengeRight,
IndependentAuditBudget,
IndependentVerifierSpawn,
NoForcedAgreement
).
$$

即：

1. Twin 可以保存自己的 audit state；
2. Twin 可以 challenge Primary；
3. Twin 有獨立 audit budget；
4. Twin 可以產生 fresh verifier；
5. Twin 不因 Primary 宣告完成而必須自動同意。

這是工程治理獨立，不是概率論意義上的獨立。

---

# 26. 反身性：Twin 也必須可被審計

如果 Twin 擁有 reopen / repartition 權，Twin 自己也可能：

- 過度審計；
- 造成 thrashing；
- 誤判 risk；
- 不必要地擴張成本；
- 對某些 branch 產生 blind spot。

因此定義：

$$
Audit(TwinAction)
$$

可以由：

- Primary；
- policy engine；
- fresh auditor；
- temporal-cost monitor；

執行。

Twin intervention 必須記錄：

$$
TwinActionReceipt
=
(
Action,
Reason,
Target,
Evidence,
ExpectedBenefit,
ActualOutcome
).
$$

這讓後續可以估計 Twin 的真正 marginal value。

---

# 27. Twin intervention 的停損

若某個 node 重複：

$$
REOPEN
\rightarrow
REPAIR
\rightarrow
REOPEN
$$

系統可能進入 thrashing。

定義 reopen count：

$$
N_r(v).
$$

若：

$$
N_r(v)\ge \theta_r,
$$

則必須升級為：

$$
Escalate(v)
$$

或：

$$
Reframe(v).
$$

禁止無限重試。

---

# 28. Fractal Twin：每一層都需要雙生嗎？

不需要。

FCAO 的遞歸結構允許 local parent：

$$
A_i
\rightarrow
\{A_{i1},\ldots,A_{ik}\}.
$$

但不要求每個 $A_i$ 都立即產生 Twin。

定義 Twin activation：

$$
ActivateTwin(\mathcal D_i)
=
g(
Risk_i,
Complexity_i,
Depth_i,
Budget_i,
ExpectedRework_i
).
$$

只有當：

$$
ActivateTwin(\mathcal D_i)\ge \theta_T
$$

時，局部域才建立：

$$
P_i
\parallel
T_i.
$$

因此：

$$
\boxed{
FractalTwin
=
ConditionalRecursiveGovernance,
}
$$

不是無限倍增 Agent。

---

# 29. Named Ephemeral Audit Agents

Twin 產生的 verifier / auditor 同樣遵守 FCAO Named Ephemeral Agent。

例如：

```yaml
agent_id: audit-03-9fd2
name: Argus
task_name: Storage Invariant Audit
role: fresh_verifier
parent_agent_id: twin-root
lifetime: until_receipt
```

名字仍只是 semantic handle：

$$
EphemeralName
\neq
PersistentIdentity.
$$

但它讓：

> `Argus 發現 Atlas 的 dependency assumption 未驗證`

比：

> `agent-9fd2 發現 agent-a12c...`

更適合人類與 AI 共同管理。

---

# 30. CTCL-ITR：雙向圈必須有時間因果位置

雙生治理若沒有 temporal-causal ledger，容易只剩：

> Twin 後來覺得有問題。

CTCL-ITR 應記錄：

$$
Event
=
(
Actor,
Time,
StateBefore,
Decision,
Target,
Authority,
Evidence,
StateAfter,
Receipt
).
$$

例如：

$$
E_1
=
PrimaryDispatch,
$$

$$
E_2
=
ChildLocalClosure,
$$

$$
E_3
=
TwinReopen,
$$

$$
E_4
=
AuditResult,
$$

$$
E_5
=
PrimaryReintegration.
$$

如此才能回答：

> 哪一個 intervention 真正避免了 late rework？

---

# 31. Software Spacetime：Primary 與 Twin 不共享單一執行時間

Primary：

$$
\tau_P
$$

Twin：

$$
\tau_T
$$

各子 Agent：

$$
\tau_i
$$

可以非同步演化。

Project makespan：

$$
T_W
$$

不等於：

$$
\tau_P+\tau_T+\sum_i\tau_i.
$$

Twin 可以在某些 branch 尚未完成時先 audit 已成熟節點，也可以在 Primary integration 過程中執行 top-down probe。

因此雙生治理天然需要 multi-time-domain viewpoint。

---

# 32. SEDB：Twin state 不應只存在對話 context

Twin 的 audit map、risk score、reopen receipt、LCC 與 dispute history 應外部化。

可定義 SEDB projection：

$$
F_{Twin}
=
\{
risk,
audit\_priority,
closure\_status,
reopen\_reason,
verifier,
receipt,
conflict,
arbiter
\}.
$$

但：

$$
AddField
\not\Rightarrow
FillField.
$$

只有相關 project object 需要 materialize 這些欄位。

---

# 33. ANDO：雙生治理不取代組織治理

ANDO 已區分：

$$
State
\neq
Agent
\neq
Authority
\neq
Commit.
$$

Twin 必須繼承此不變量。

Twin 能力：

$$
Capability_T
$$

不自動等於：

$$
Authority_T.
$$

例如 Twin 可以偵測需要停止某 Agent，但實際 `STOP` 是否可直接執行，取決於 authority envelope。

因此：

$$
TwinProposal
\neq
TwinCommit.
$$

---

# 34. Addressable Cognitive Runtime：Twin 可以審計認知地址

若 Primary 建立某個 cognitive call：

$$
CognitionAddress_k,
$$

Twin 可以針對：

- assumption extraction；
- contradiction search；
- evidence gap；
- alternative decomposition；
- closure audit；

建立指定 cognitive operator，而不是重新生成整個回答。

因此 Twin intervention 可以是 addressable，而非全文重算。

---

# 35. Self-Constraint：Twin 也受 Execute / Refuse / Defer / Idle / Escalate 約束

Twin 不應因為被稱為 governor 就必須永遠介入。

Twin 可以：

$$
EXECUTE
$$

當 intervention value 高；

$$
REFUSE
$$

當要求超越 authority；

$$
DEFER
$$

等待關鍵 evidence；

$$
IDLE
$$

當目前無需 intervention；

$$
ESCALATE
$$

當 Primary–Twin dispute 超出本地治理能力。

這避免 Twin 成為無限制 supervisory loop。

---

# 36. MWT：雙生是局部世界中的兩個觀察—控制節點

從 MWT 角度，Primary 與 Twin 都不是 World 本身。

它們是：

$$
ObserverController_P
$$

與：

$$
ObserverController_T.
$$

兩者可以具有不同 projection：

$$
\pi_P(W)
\neq
\pi_T(W).
$$

但彼此輸出必須能透過 canonical state、receipt 與 transport relation 比較。

因此 Twin 的價值也可以理解為：

$$
\boxed{
MultipleObserverProjection
+
GovernedReconciliation.
}
$$

---

# 37. Protocol-agnostic：Twin 不是 MCP 專屬概念

本文的 canonical relation：

$$
Primary
\parallel
Twin
$$

以及：

$$
E^{\uparrow},
E^{\downarrow},
E^{\times}
$$

不依賴特定 transport。

底層可以是：

- in-process subagent；
- CLI；
- MCP；
- A2A；
- API；
- message queue；
- local model；
- cloud runtime。

定義 adapter：

$$
\phi_i:
\mathcal C_{Twin}
\leftrightarrow
Protocol_i.
$$

因此協議可以替換，而 governance semantics 保持穩定。

---

# 38. 與既有 verifier / debate / redundancy 的差異

本文不把下列概念視為相同：

## 38.1 Verifier

Verifier 通常回答：

$$
IsArtifactCorrect?
$$

Twin 還回答：

$$
IsProjectTopologyStillValid?
$$

## 38.2 Debate

Debate 常聚焦多 Agent 對同一命題提出不同 argument。

Twin 更聚焦：

$$
Governance
+
Scheduling
+
Closure
+
Reopen.
$$

## 38.3 N-version / redundant execution

完整冗餘傾向：

$$
Execute_Q^{(1)}
+
Execute_Q^{(2)}
+\cdots
$$

Twin 採 selective audit，而非預設 full duplicate。

## 38.4 Supervisor tree

傳統 supervisor 常是上層管理下層。

本文 Twin 可以 challenge Primary 本身，因此治理關係不是單純 supervisor hierarchy。

---

# 39. 雙向控制循環

完整第一代循環：

$$
\boxed{
\begin{aligned}
ProjectWorld
&\rightarrow
PrimaryPlan\\
&\rightarrow
TopologyEstimate\\
&\rightarrow
NamedAgentDispatch\\
&\rightarrow
LocalExecution\\
&\rightarrow
LocalVerification\\
&\rightarrow
LCC\\
&\rightarrow
BottomUpAggregation\\
&\rightarrow
PrimaryIntegration\\
&\parallel
TwinInspection\\
&\rightarrow
TopDownProbe/Reopen/Repartition\\
&\rightarrow
LocalRepair\\
&\rightarrow
Reaggregation\\
&\rightarrow
MetaVerification\\
&\rightarrow
Closure\\
&\rightarrow
Commit.
\end{aligned}
}
$$

中間允許：

$$
\circlearrowleft
$$

直到 closure 或 stop condition。

---

# 40. 最小狀態機

Primary state：

$$
PState
\in
\{
Modeling,
Planning,
Dispatching,
Integrating,
CommitPending,
Closed
\}.
$$

Twin state：

$$
TState
\in
\{
Observing,
Auditing,
Challenging,
Repartitioning,
MetaVerifying,
Idle
\}.
$$

Project state：

$$
WState
\in
\{
Open,
Running,
Reopened,
Repairing,
Verifying,
CommitPending,
Closed,
Escalated
\}.
$$

三者不應被壓成單一 status。

---

# 41. 事件類型

v0.1 canonical event set：

$$
\mathcal E
=
\{
DISPATCH,
RESULT,
LCC,
AUDIT,
CHALLENGE,
PROBE,
REOPEN,
REPARTITION,
REASSIGN,
PAUSE,
STOP,
REPAIR,
REVERIFY,
ARBITRATE,
CLOSE,
COMMIT
\}.
$$

每個 governance-critical event 必須有：

$$
Receipt(e).
$$

---

# 42. 核心不變量

## Invariant 1：Twin 不是普通 child

$$
Twin
\notin
OrdinaryChildSet(Primary).
$$

## Invariant 2：Twin 不是 full duplicate

$$
TwinWork
\neq
FullRecompute(PrimaryWork).
$$

## Invariant 3：Primary closure 可被 challenge

$$
Closure_P
\not\Rightarrow
GlobalClosure.
$$

## Invariant 4：Twin intervention 必須有 receipt

$$
TwinAction
\Rightarrow
Reason+Target+Evidence+Authority.
$$

## Invariant 5：Verification topology 是 task topology 的一部分

$$
VerificationTopology
\subseteq
TaskTopology.
$$

## Invariant 6：Reopen 必須版本化

$$
REOPEN(v)
\Rightarrow
VersionIncrement(v).
$$

## Invariant 7：Arbiter 只能是 bounded temporary role

$$
Authority(A_{arb})
\preceq
DisputeScope.
$$

## Invariant 8：Child local closure 不等於 global closure

$$
\forall i,\ LCC_i=1
\not\Rightarrow
GlobalClosure=1.
$$

## Invariant 9：Twin 可以 IDLE

$$
NoUsefulIntervention
\Rightarrow
IDLE
$$

是合法結果。

## Invariant 10：雙生收益必須可量測

$$
TwinBenefit
\neq
AssumedConstant.
$$

---

# 43. Twin Value 指標

定義第一代 Twin marginal value：

$$
MV_T
=
AvoidedRework
+
AvoidedFailure
+
VerificationSavings
-
TwinOperatingCost.
$$

若：

$$
MV_T>0,
$$

則該時段 Twin 具有正邊際價值。

也可定義：

$$
ROI_T
=
\frac{
AvoidedCost_T
}{
TwinCost_T
}.
$$

但對高風險領域不能只看 cost；可加入 expected loss：

$$
EL
=
P(Failure)\cdot Impact(Failure).
$$

因此：

$$
TwinValue
=
\Delta Cost
+
\lambda\Delta EL
+
\mu\Delta Quality.
$$

---

# 44. 測試假說

本文提出至少六個可測試假說。

## H1：Late rework

在 dependency depth 較高的專案中：

$$
TwinSelectiveAudit
$$

可降低：

$$
LateStageRework.
$$

## H2：Verification recomputation

使用 LCC + typed receipt 後：

$$
ParentVerificationCost
$$

低於：

$$
FullRecomputationVerification.
$$

## H3：False closure

Twin meta-verification 可降低：

$$
FalseClosureRate.
$$

## H4：Overhead boundary

對極小任務：

$$
TwinCost
>
TwinBenefit
$$

的比例較高。

## H5：Correlation

若 Primary / Twin failure correlation 高，Twin 邊際價值下降。

## H6：Adaptive mode

Adaptive Twin Mode 比固定 100% verification 更可能取得：

$$
Quality/Cost
$$

較佳 Pareto frontier。

---

# 45. 實驗設計

建議 benchmark 至少包含四種 task family：

1. software engineering；
2. research synthesis；
3. structured data transformation；
4. planning / architecture。

每個 task 比較：

### Baseline A

Single Root + no child。

### Baseline B

Single Root + multi-agent + final root verification。

### Baseline C

Multi-agent + fresh verifier per artifact。

### Treatment D

Primary + Persistent Twin + selective audit + LCC。

測量：

$$
T_{makespan},
$$

$$
TokenCost,
$$

$$
ExternalCost,
$$

$$
FalseClosureRate,
$$

$$
LateReworkCost,
$$

$$
DefectEscapeRate,
$$

$$
VerificationRecomputeRatio.
$$

其中：

$$
VerificationRecomputeRatio
=
\frac{
VerificationTokensOnReconstructingOriginalWork
}{
TotalVerificationTokens
}.
$$

---

# 46. Ablation

至少做：

- remove Twin；
- remove LCC；
- remove reopen；
- remove repartition；
- remove fresh verifier spawn；
- remove temporary arbiter；
- force same-model Twin；
- force different-model Twin；
- disable CTCL receipts；
- disable external state。

用以分辨真正收益來源。

---

# 47. 安全與治理限制

本文雙生治理不代表：

- Twin 擁有無限工具權；
- Twin 可以繞過人類設定；
- Twin 可以秘密修改 canonical state；
- Twin 可以自行取得 credential；
- Twin 可以因 challenge 就直接 world commit；
- 多 Agent 共識自動等於真實。

任何 action 仍受：

$$
Policy
+
Authority
+
Verification
+
CommitGate.
$$

---

# 48. 隱私與最小披露

Twin audit 不要求保存完整 internal reasoning。

治理必要資訊：

$$
MinimalGovernanceRecord
=
(
DecisionSummary,
EvidenceRef,
ArtifactRef,
StateTransition,
Authority,
Receipt
).
$$

因此：

$$
Auditability
\neq
HiddenCoTLogging.
$$

---

# 49. 工程承載層

現有 agent harness、coding agent、MCP runtime、CLI orchestration 與 multi-agent framework 已能提供部分必要 primitive，例如：

- coordinator；
- subagent；
- verifier；
- message passing；
- tool execution；
- background task；
- memory；
- session；
- hooks；
- plugin。

因此後續工程不必假設 FCAO 必須從零建立 provider、terminal、tool registry、MCP stack 或 TUI。

但本文的理論貢獻不依賴特定 carrier。實際 OpenHarness fit-gap、extension surface、patch / fork decision 另列技術白皮書處理。

---

# 50. 與下一篇的邊界

本文回答：

> **誰治理誰？如何形成 Primary–Twin 雙核心與上下雙向驗證圈？**

下一篇 FCAO Temporal-Topological Computation Paper 回答：

> **何時值得切？切多少？在哪裡驗證？何時重分區？時間上下界、critical path、verification placement 與總成本怎麼估？**

因此本文刻意不完整展開：

$$
[T^-,T^+],
$$

$$
DecompositionGain,
$$

$$
CriticalPath,
$$

$$
ExpectedMakespan.
$$

避免和下一篇重複。

---

# 51. 第一代 Canonical Twin Profile

Twin Profile：

$$
TwinProfile
=
(
TwinID,
Name,
ProjectDomain,
Authority,
AuditPolicy,
RiskThreshold,
Budget,
VerifierPolicy,
ReopenPolicy,
ArbitrationPolicy
).
$$

Primary Profile：

$$
PrimaryProfile
=
(
PrimaryID,
Name,
ProjectDomain,
Authority,
PlanningPolicy,
DelegationPolicy,
IntegrationPolicy,
CommitPolicy
).
$$

兩者共享：

$$
CanonicalProjectState
$$

但不必共享全部 private working context。

---

# 52. 最小雙生 Runtime

最小實作不需要大型平台。

只需：

1. 一個 Primary Agent；
2. 一個 Persistent Twin Agent；
3. 一個共享 canonical task graph；
4. Named Ephemeral Agent spawn；
5. Local Closure Certificate；
6. `REOPEN`；
7. `REPARTITION`；
8. fresh verifier spawn；
9. CTCL-style event receipt；
10. closure gate。

這已足以驗證本文主要命題。

---

# 53. 強版本與弱版本

## 弱版本

Twin 只：

- 看 graph；
- 讀 LCC；
- 做 selective verifier dispatch；
- challenge closure。

## 中版本

Twin 還可：

- reopen；
- repartition；
- stop / reassign child。

## 強版本

Twin 可以在 policy envelope 內動態修改 verification topology、分配 audit budget，並參與高風險 commit concurrence。

實驗應從弱版本開始。

---

# 54. 理論風險：治理複雜度本身會成為問題

增加 Twin 會增加：

$$
GovernanceStateSpace.
$$

如果 governance protocol 過度複雜：

$$
C_{governance}
>
C_{task},
$$

則系統本末倒置。

因此本文保留最小化原則：

$$
\boxed{
UseTheSmallestGovernanceTopology
ThatMeetsRiskAndClosureRequirements.
}
$$

---

# 55. 不把所有分歧都當錯誤

Primary 與 Twin 的 disagreement 可能代表：

- 兩個都部分正確；
- task specification 不完整；
- 不同合法 trade-off；
- evidence 不足；
- ontology 需要擴張。

因此：

$$
Disagreement
\not\Rightarrow
OneSideWrong.
$$

Temporary Arbiter 也可以返回：

$$
BOTH\_PARTIAL
$$

或：

$$
REFRAME\_REQUIRED.
$$

---

# 56. 從「驗證答案」到「驗證組織狀態」

Twin 真正重要的轉向是：

$$
Verify(Answer)
$$

擴張成：

$$
Verify(
Topology,
Coverage,
Evidence,
Authority,
Artifact,
TemporalHistory,
Closure
).
$$

因此雙生治理不是 answer evaluator，而是 project-world governor。

---

# 57. 核心命題總結

本文的核心可以壓縮為七條。

第一：

$$
\boxed{
LocalGlobalAIUnit
=
Primary+Twin+EphemeralChildren.
}
$$

第二：

$$
\boxed{
Twin
\neq
FinalVerifier
\neq
DuplicatePrimary.
}
$$

第三：

$$
\boxed{
\mathcal G^{\leftrightarrow}
=
(V,E^{\uparrow},E^{\downarrow},E^{\times}).
}
$$

第四：

$$
\boxed{
BottomUp
\rightarrow
GlobalInspection
\rightarrow
TopDownProbe
\rightarrow
LocalRepair
\rightarrow
BottomUp.
}
$$

第五：

$$
\boxed{
VerificationTopology
\subseteq
TaskTopology.
}
$$

第六：

$$
\boxed{
LocalClosureCertificate
\neq
GlobalClosure.
}
$$

第七：

$$
\boxed{
TwinBenefit
\text{ must be measured, not assumed.}
}
$$

---

# 58. 結論

FCAO Foundation 將 Conversation 從訊息序列提升為 temporary local computational world，並以 Named Ephemeral Agent、recursive delegation 與 topological completion 描述分形式多 Agent 組織。本文在此基礎上進一步指出：若所有 decomposition、integration、verification 與 closure authority 仍集中在單一 Root，分散執行可能在上層 join / verification 階段重新串行化，也可能因共同模型錯誤而產生 false closure。

因此本文提出 Primary–Twin 雙生治理。Twin 不是附屬 verifier，也不是第二個完整 Primary，而是持續存在、可獨立 challenge、可選擇性派發 verifier、可在 authority 內 reopen / repartition 的治理 peer。其核心不是增加冗餘本身，而是讓分散式工作形成真正的雙向控制循環：

$$
\boxed{
ExecuteUpward
+
InspectGlobally
+
ProbeDownward
+
RepairLocally
+
RecloseGlobally.
}
$$

雙生架構只有在 selective audit、local closure certificate、bounded intervention 與 temporal-causal receipts 配合下，才有機會避免「所有工作做兩遍」的成本陷阱。本文因此將「雙生一定更省」改寫成可實證假說，並把時間上下界、decomposition gain、critical path、verification placement 與 dynamic repartition 留給下一篇 FCAO Temporal-Topological Computation Paper。

若後續實驗支持本文假說，則 Conversation-local AI 的最小治理單位將不再只是：

$$
Root+Children,
$$

而可能更適合表達為：

$$
\boxed{
Primary
\parallel
Twin
\rightarrow
FractalEphemeralOrganization.
}
$$

這使 AI 專案管理從單向 delegation tree，向具有反身性、可重開、可再分區、可證據化的雙向計算組織前進。

---

# 附錄 A：Canonical Event Example

```yaml
event_id: ev-20260824-001
event_type: REOPEN
actor:
  role: twin
  id: twin-root-001
target:
  type: task
  id: task-storage-017
reason: "Merge certificate depends on an unverified storage invariant."
evidence_refs:
  - receipt://verify/storage-012
requested_action:
  type: targeted_audit
  scope: storage_invariant
authority_class: project_governance
ctcl:
  observed_at: "2026-08-24T14:19:00+08:00"
  causal_parent: ev-20260824-000
```

---

# 附錄 B：Local Closure Certificate Example

```yaml
lcc_id: lcc-atlas-017
agent:
  id: child-017
  name: Atlas
task:
  id: task-017
  name: Storage Topology
scope:
  mandatory_obligations: 8
  satisfied: 7
artifacts:
  - artifact://storage-model-v3
verification:
  status: partial
open_gaps:
  - "Crash recovery invariant not independently reproduced."
assumptions:
  - "Single-writer mode during migration."
receipts:
  - receipt://test-017
  - receipt://lint-017
lineage:
  parent_task: task-root-001
  parent_agent: primary-root-001
closure:
  local_complete: false
```

---

# 附錄 C：Primary–Twin Dispute Example

```yaml
dispute_id: dispute-004
primary:
  position: CLOSE
  evidence:
    - lcc://branch-a
    - lcc://branch-b
twin:
  position: REOPEN
  evidence:
    - conflict://shared-assumption-09
risk_class: R3
resolution_policy:
  first: evidence_exchange
  second: fresh_verifier
  third: temporary_arbiter
```

---

# 參考文獻與相關脈絡

以下文獻用於定位本文相對於既有分散式、並行、容錯與多智能體思想的關係；本文並不宣稱其列舉構成完整 prior-art search。

1. Hewitt, C., Bishop, P., & Steiger, R. (1973). *A Universal Modular ACTOR Formalism for Artificial Intelligence*. IJCAI.
2. Lamport, L. (1978). *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM.
3. Lamport, L., Shostak, R., & Pease, M. (1982). *The Byzantine Generals Problem*. ACM Transactions on Programming Languages and Systems.
4. Avizienis, A. (1985). *The N-Version Approach to Fault-Tolerant Software*. IEEE Transactions on Software Engineering.
5. Ramadge, P. J., & Wonham, W. M. (1989). *The Control of Discrete Event Systems*. Proceedings of the IEEE.
6. Wooldridge, M. (2009). *An Introduction to MultiAgent Systems*, 2nd ed. Wiley.
7. FCAO Foundation / Integration Paper v0.1, EveMissLab, 2026.
8. AI-Native Distributed Organization Reference Architecture v0.1, EveMissLab, 2026.
9. CTCL-ITR / Addressable Cognitive Runtime × CTCL documents, EveMissLab, 2026.
10. Mathematical World Theory v0.1, EveMissLab, 2026.

---

**End of canonical source.**
