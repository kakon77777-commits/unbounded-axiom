---
title: "Agent Runtime：能力規劃、工具調用與可恢復執行"
english_title: "Agent Runtime: Capability Planning, Tool Invocation, and Recoverable Execution"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "09/12"
part: "第三部：意圖編譯與 Agent 執行"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-25"
language: "zh-TW"
document_type: "理論論文／Runtime 架構／第三部收束篇"
status: "初版完成"
---

# Agent Runtime：能力規劃、工具調用與可恢復執行

## Agent Runtime: Capability Planning, Tool Invocation, and Recoverable Execution

**系列：**《意圖—結構—世界程式論》第九篇  
**部別：**第三部「意圖編譯與 Agent 執行」  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 25 日  

---

## 摘要

AI Agent 經常被簡化為「大型語言模型加上工具調用」。此定義忽略了真正支撐可持續、可恢復與可治理行動的執行系統：任務狀態、事件佇列、能力註冊、權限租約、工作區隔離、工具適配器、驗證器、預算、檢查點、冪等、補償、人工批准、執行證書與人類可見狀態。模型可以產生候選決策，但若沒有 Runtime，便不能可靠地回答哪些能力存在、哪些已授權、哪些效果已發生、失敗後應如何恢復，以及同一任務是否正在被重複執行。

本文提出 Agent Runtime 的完整分層定義：Agent Runtime 是承接 Intent IR、Task IR、Capability IR 與時間—空間控制圖，負責將候選計畫轉化為受權限、風險、資源與驗證約束的世界狀態轉換之持久執行核心。其形式模型為：

$$
\mathbb R_A
=
\left\langle
\mathcal I,
\mathcal T,
\mathcal C,
\mathcal S,
\mathcal E,
\mathcal P,
\mathcal X,
\mathcal V,
\mathcal M,
\mathcal H,
\mathcal O,
\mathcal G
\right\rangle
$$

其中依序表示意圖契約儲存、任務與控制圖、能力註冊表、持久狀態、事件系統、政策與權限、執行器、驗證器、記憶與證據、人類介面、觀測系統與治理根。

本文主張：

$$
\boxed{
\text{Model}
\neq
\text{Agent Runtime}
}
$$

模型是可替換的推理供應者；Runtime 才是持續執行身分、權限邊界、狀態權威與效果帳本。MCP、API、CLI、插件、瀏覽器自動化與本地工具也只是能力介面或執行後端，不構成完整 Agent Runtime。

本文建立 Runtime 的九階段執行交易：

$$
\text{Wake}
\rightarrow
\text{Restore}
\rightarrow
\text{Observe}
\rightarrow
\text{Plan}
\rightarrow
\text{Authorize}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Commit}
\rightarrow
\text{Schedule or Terminate}
$$

任何對外效果在 `Commit` 前都必須具有執行身分、冪等鍵、世界前置狀態、權限證書、驗證計畫與補償描述。模型提出的工具請求只是候選 Action IR；工具執行器不得直接接受自由文字，而應接受經正規化、型別化與政策審查的結構化調用。

本文區分能力、工具、插件與供應者。能力描述「能合法造成何種狀態轉換」；工具是某能力的一種實作；插件封裝工具與其契約；供應者則提供模型、API、CLI 或本地服務。透過這一區分，Runtime 可以在保持 Task IR 與 Capability IR 的前提下替換模型、工具與後端。

本文進一步提出本地優先安全邊界：高風險檔案、Shell、憑證、工作區與本地 CLI 應由本地 daemon 或受信任執行節點控制；Web UI 與模型不直接擁有本地資源。Runtime 需對插件進行 manifest 驗證、依賴鎖定、簽章、最小權限、工作區沙盒與效果分級。

本文亦建立失敗與恢復模型：每次 Agent Run 應是可恢復狀態交易，具有 `planned`、`authorized`、`executing`、`verifying`、`committing`、`suspended`、`compensating` 等狀態。失敗不能只被轉成文字回覆，而必須分類為規格、權限、能力、工具、世界、驗證、資源、超時或人類拒絕，並觸發重試、替代能力、重新規劃、補償、暫停或人工接管。

本文最後提出可證偽研究綱領，包括能力匹配保真、工具替換穩定性、最小權限率、重複效果率、故障恢復時間、事件重放正確率、驗證獨立性、人類接管可用性、模型替換穩定性、插件供應鏈攻擊阻止率及長時程狀態一致性。本文的核心結論是：Agent 的可執行主體不是模型本身，而是由持久狀態、能力契約、政策閘門、工具執行、驗證證據與世界差分共同形成的 Runtime。

**關鍵詞：** Agent Runtime、Capability IR、Action IR、工具調用、插件運行層、最小權限、事件驅動、可恢復執行、MCP、本地優先、執行證書

---

## Abstract

AI agents are often reduced to “a large language model with tool calling.” This overlooks the execution system required for persistent, recoverable, and governable action: task state, event queues, capability registries, permission leases, workspace isolation, tool adapters, validators, budgets, checkpoints, idempotency, compensation, human approvals, execution certificates, and human-visible state.

This paper defines an Agent Runtime as the persistent execution core that receives Intent IR, Task IR, Capability IR, and temporal–spatial control graphs, and converts candidate plans into world-state transitions constrained by authorization, risk, resources, and verification.

The runtime is modeled as:

$$
\mathbb R_A
=
\left\langle
\mathcal I,
\mathcal T,
\mathcal C,
\mathcal S,
\mathcal E,
\mathcal P,
\mathcal X,
\mathcal V,
\mathcal M,
\mathcal H,
\mathcal O,
\mathcal G
\right\rangle
$$

The components denote intent storage, task/control graphs, capability registries, persistent state, event infrastructure, policy and authorization, executors, validators, memory and evidence, human interfaces, observability, and governance roots.

The central proposition is:

$$
\text{Model}\neq\text{Agent Runtime}
$$

A model is a replaceable reasoning provider. The runtime is the authority for persistent execution identity, permissions, state, and effect accounting. MCP, APIs, CLIs, plugins, browser automation, and local tools are capability interfaces or execution backends, not complete runtimes.

The paper introduces a nine-stage execution transaction: wake, restore, observe, plan, authorize, execute, verify, commit, and schedule or terminate. It defines Action IR, local-first security boundaries, plugin manifests, failure states, compensation, verification independence, and execution certificates.

The conclusion is that the executable subject of an agent system is not the model alone, but the runtime formed by persistent state, capability contracts, policy gates, tool execution, verification evidence, and world-state deltas.

**Keywords:** Agent Runtime, Capability IR, Action IR, tool invocation, plugin runtime, least privilege, event-driven agents, recoverable execution, MCP, local-first systems

---

# 一、問題的提出：模型為何不是 Agent？

大型語言模型可以：

- 理解要求；
- 生成計畫；
- 選擇工具；
- 產生參數；
- 解讀工具結果；
- 修改後續策略。

但模型單獨不能可靠保存：

- 任務是否已執行；
- 某次付款是否成功；
- 哪個檔案已修改；
- 哪個權限仍有效；
- 哪個事件已處理；
- 哪個工具版本被使用；
- 哪些副作用需要補償；
- 哪個人類批准了高風險動作。

若這些狀態只存在於對話文字中，便會產生：

- 摘要遺失；
- 重複執行；
- 權限幻覺；
- 世界狀態過時；
- 模型切換後失憶；
- 無法恢復；
- 無法稽核。

因此：

$$
\boxed{
\text{Reasoning Provider}
\neq
\text{Execution Authority}
}
$$

模型負責提出候選推理。

Runtime 負責決定候選是否能成為合法行動。

---

# 二、Agent Runtime 的正式定義

本文將 Agent Runtime 定義為：

> **接收意圖、任務、能力與時空控制結構，維持跨次執行狀態，對候選行動進行權限、風險、資源與驗證審查，調用工具並將結果提交為可追溯世界狀態差分的持久執行核心。**

其形式為：

$$
\boxed{
\mathbb R_A
=
\left\langle
\mathcal I,
\mathcal T,
\mathcal C,
\mathcal S,
\mathcal E,
\mathcal P,
\mathcal X,
\mathcal V,
\mathcal M,
\mathcal H,
\mathcal O,
\mathcal G
\right\rangle
}
$$

其中：

- $\mathcal I$ ：Intent IR 與版本；
- $\mathcal T$ ：Task IR、控制圖與 continuation；
- $\mathcal C$ ：能力註冊表與 Capability IR；
- $\mathcal S$ ：持久狀態與世界快照；
- $\mathcal E$ ：事件、排程與 Wake Queue；
- $\mathcal P$ ：政策、權限、租約與預算；
- $\mathcal X$ ：工具、插件與執行器；
- $\mathcal V$ ：驗證器與證書；
- $\mathcal M$ ：記憶、證據與因果歷史；
- $\mathcal H$ ：人類批准、接管與可見狀態；
- $\mathcal O$ ：日誌、trace、metrics 與事件溯源；
- $\mathcal G$ ：治理根、信任錨與撤銷政策。

---

# 三、Runtime 的責任邊界

## 3.1 Runtime 負責

- 恢復 Agent Run；
- 載入意圖與任務；
- 載入權限與預算；
- 取得喚醒原因；
- 建立候選計畫；
- 驗證能力與工具；
- 執行 Action IR；
- 收集結果；
- 驗證世界差分；
- 保存狀態；
- 建立下一次喚醒；
- 暫停、補償、終止與交接。

## 3.2 Runtime 不應負責全部內容

Runtime 不應自行決定：

- 人類終極目的；
- 所有倫理規範；
- 世界本體的全部規則；
- 所有模型推理；
- 所有 UI；
- 所有工具內部實作。

## 3.3 時間基礎設施的邊界

外部時間系統回答：

```text
何時、因何條件產生 WakeEvent？
```

Runtime 回答：

```text
收到 WakeEvent 後，如何恢復、判斷、行動與保存？
```

## 3.4 MCP 的邊界

MCP 或其他工具協議回答：

```text
哪些能力可被發現與調用？
```

但不自動提供：

- 長期記憶；
- 自主喚醒；
- 權限租約；
- 任務狀態；
- 補償；
- 執行證書；
- 人類治理。

因此：

$$
\boxed{
\text{MCP}
\neq
\text{Complete Agent Runtime}
}
$$

---

# 四、能力、工具、插件與供應者

## 4.1 能力

能力描述：

$$
c:
D_c
\rightarrow
R_c
$$

以及：

- 前置條件；
- 後置條件；
- 效果；
- 權限；
- 成本；
- 驗證；
- 失敗；
- 可逆性。

## 4.2 工具

工具是某能力的具體實作：

$$
x_j
\models
c
$$

同一能力可由多個工具提供。

## 4.3 插件

插件封裝：

$$
p
=
\left\langle
\operatorname{manifest},
\operatorname{capabilities},
\operatorname{adapters},
\operatorname{permissions},
\operatorname{validators},
\operatorname{runtime}
\right\rangle
$$

## 4.4 供應者

供應者可能是：

- 大型語言模型 API；
- AI CLI；
- 本地模型；
- 雲端服務；
- 本地程式；
- 人類工作者；
- 其他 Agent。

供應者不是能力語意本身。

## 4.5 工具替換

若：

$$
x_1\models c
$$

且：

$$
x_2\models c
$$

則在滿足相同能力契約時，Runtime 可以替換工具：

$$
x_1
\rightsquigarrow
x_2
$$

而不改變 Task IR。

---

# 五、能力註冊表

能力註冊項目：

```text
CapabilityDescriptor {
  semantic_id
  version
  input_schema
  output_schema
  preconditions
  postconditions
  effects
  permissions
  cost_model
  risk
  reversibility
  validators
  providers
  provenance
}
```

## 5.1 發現

$$
\operatorname{Discover}
\left(
t,
\mathcal C
\right)
\rightarrow
\{
c_1,\ldots,c_n
\}
$$

## 5.2 篩選

Runtime 應移除：

- schema 不相容；
- 權限不足；
- 世界前置不成立；
- 風險超標；
- 預算不足；
- 無驗證器；
- 插件被撤銷；
- 版本不支援；
- 效果衝突。

## 5.3 排名

模型可以對合法候選排序，但不能把非法能力排入計畫。

## 5.4 能力狀態

```text
available
degraded
unavailable
revoked
untrusted
experimental
```

---

# 六、Action IR：模型與工具之間的正式邊界

模型不應直接輸出自由文字給工具執行器。

定義 Action IR：

$$
a
=
\left\langle
\operatorname{id},
c,
x,
\theta,
W^\ast,
A^\ast,
B^\ast,
V^\ast,
R^\ast,
K^\ast
\right\rangle
$$

其中：

- $c$ ：能力 semantic ID；
- $x$ ：選定工具／插件；
- $\theta$ ：正規化參數；
- $W^\ast$ ：世界前置狀態；
- $A^\ast$ ：權限證書；
- $B^\ast$ ：預算；
- $V^\ast$ ：驗證計畫；
- $R^\ast$ ：風險與補償；
- $K^\ast$ ：冪等鍵與執行身分。

## 6.1 候選 Action

模型輸出：

```text
candidate
```

只有 Runtime 可將其轉為：

```text
authorized
```

## 6.2 不接受自由 Shell

Shell 能力需轉成：

- 命令；
- 引數；
- 工作目錄；
- 環境變數；
- 檔案作用域；
- 網路權限；
- 超時；
- 預期輸出；
- 退出碼政策。

## 6.3 機密隔離

模型不應直接看到所有憑證。Runtime 可使用：

- 代號；
- secret handle；
- scoped token；
- 一次性憑證。

---

# 七、九階段執行交易

完整 Agent Run：

$$
\boxed{
\text{Wake}
\rightarrow
\text{Restore}
\rightarrow
\text{Observe}
\rightarrow
\text{Plan}
\rightarrow
\text{Authorize}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Commit}
\rightarrow
\text{Schedule or Terminate}
}
$$

## 7.1 Wake

接收：

- 時間事件；
- 外部事件；
- 人類回覆；
- 工具結果；
- 政策更新；
- 任務依賴完成。

## 7.2 Restore

載入：

- Identity；
- Intent IR；
- Task IR；
- Capability IR；
- continuation；
- 記憶；
- 權限；
- 預算；
- 上次 Decision Receipt。

## 7.3 Observe

取得新世界資訊，但須標記：

- 來源；
- 時間；
- 新鮮度；
- 信任；
- 是否完整。

## 7.4 Plan

模型或規劃器產生候選：

- no-op；
- Action IR；
- 新任務；
- 計畫修訂；
- 人類問題；
- 下一次喚醒。

## 7.5 Authorize

政策引擎檢查：

- 能力是否允許；
- 參數是否在作用域；
- 是否需要批准；
- 風險與預算；
- 租約；
- 不可逆性；
- 多主體權利。

## 7.6 Execute

執行器在沙盒或指定環境中調用工具。

## 7.7 Verify

獨立驗證：

- schema；
- 工具回傳；
- 狀態差分；
- 不變量；
- 測試；
- 權限；
- 非目標；
- 成功條件。

## 7.8 Commit

只有驗證通過後，才提交：

- 任務狀態；
- 世界差分；
- 記憶；
- 事件偏移；
- 預算；
- 證據；
- 執行證書。

## 7.9 Schedule or Terminate

建立下一次：

- WakeEvent；
- Temporal Contract；
- Human Decision；
- Retry；
- 完成或終止狀態。

---

# 八、Runtime 狀態機

Agent Run 狀態：

```text
created
queued
woken
restoring
observing
planning
waiting-authorization
authorized
executing
verifying
committing
suspended
waiting-event
waiting-human
retrying
compensating
completed
failed
cancelled
expired
revoked
```

## 8.1 狀態轉移不可任意

例如：

```text
planning → executing
```

若未經：

```text
waiting-authorization → authorized
```

應被禁止。

## 8.2 每次狀態變更產生事件

```text
agent_run.authorized
agent_run.execution_started
agent_run.verification_failed
agent_run.committed
```

## 8.3 非法轉移

非法狀態轉移應形成：

```text
RuntimeStateError
```

而不是被模型文字掩蓋。

---

# 九、事件系統與 Wake Queue

## 9.1 WakeEvent

```text
WakeEvent {
  event_id
  agent_id
  run_id
  source
  reason
  created_at
  not_before
  expires_at
  payload
  policy
  idempotency_key
  causal_parents
}
```

## 9.2 去重與合併

多個相同事件可合併，但不能丟失：

- 來源；
- 次數；
- 最早與最晚時間；
- 因果父節點。

## 9.3 Dead Letter Queue

無法處理的事件應進入死信佇列，而不是無限重試。

## 9.4 no-op

Agent 可合法回傳：

```text
no_action
```

但仍需 Decision Receipt。

## 9.5 事件偏移

持久化消費者應保存已提交偏移，避免重啟後重複處理。

---

# 十、持久狀態與記憶

## 10.1 狀態類型

- 控制狀態；
- 任務狀態；
- 世界觀測；
- 執行效果；
- 短期工作記憶；
- 長期記憶；
- 人類決策；
- 權限；
- 預算；
- 來源證據。

## 10.2 記憶不是完整真相

記憶項目應標記：

```text
fact
observation
inference
preference
decision
policy
summary
hypothesis
```

## 10.3 摘要不可覆蓋原始證據

摘要可以加速恢復，但原始事件、工具結果與證書應可追溯。

## 10.4 模型切換

模型替換時，Runtime 保存：

- Identity；
- Intent；
- Commitments；
- Memory；
- Pending Tasks；
- Permissions；
- Causal History。

因此：

$$
\text{Agent Continuity}
\not\equiv
\text{Same Model Weights}
$$

---

# 十一、權限、政策與最小授權

## 11.1 權限租約

每次 Run 建立短期權限：

$$
\ell
=
\left(
\text{scope},
\text{operations},
t_{\mathrm{expire}},
\text{budget}
\right)
$$

## 11.2 作用域

例如：

```text
workspace:/project-a
branch:feature/*
network:api.example.com
shell:read-only
```

## 11.3 最小權限

Runtime 應使用完成當前 Action 所需的最小集合，而不是整個任務可能使用的最大集合。

## 11.4 權限擴張

候選計畫若需要新增權限：

$$
A_{\mathrm{new}}
\not\subseteq
A_{\mathrm{current}}
$$

應進入重新批准。

## 11.5 政策優先於模型

模型不能用「為了完成任務」作為繞過政策的理由。

---

# 十二、本地優先執行邊界

## 12.1 Local Daemon

本地 daemon 可以負責：

- 工作區；
- 本地檔案；
- Shell；
- Git；
- API key；
- AI CLI；
- 編譯器；
- 測試；
- 瀏覽器橋接；
- 事件流。

## 12.2 Web UI 不直接執行

Web UI 應負責：

- 顯示；
- 建立任務；
- 授權；
- 批准；
- 暫停；
- 取消；
- 查看差分與證據。

不直接讀取磁碟或執行 Shell。

## 12.3 本地與雲端混合

低敏感推理可在雲端；高敏感效果在本地。

Runtime 必須標記資料流：

$$
\operatorname{DataFlow}
\left(
\text{source},
\text{destination},
\text{purpose}
\right)
$$

## 12.4 本地優先不是本地唯一

完全本地、混合與雲端 Runtime 都可實作此模型，但敏感資源應有明確控制邊界。

---

# 十三、插件安全

## 13.1 Plugin Manifest

```text
PluginManifest {
  id
  version
  publisher
  signature
  capabilities
  permissions
  entrypoints
  dependencies
  validators
  network_policy
  filesystem_policy
  sandbox_policy
}
```

## 13.2 安裝前驗證

- 簽章；
- 發布者；
- 雜湊；
- 依賴；
- 權限；
- 已知漏洞；
- schema；
- 來源。

## 13.3 執行時隔離

- 子程序；
- 容器；
- OS sandbox；
- 工作區限制；
- 網路 allowlist；
- 時間與記憶體上限。

## 13.4 插件撤銷

若插件被撤銷，尚未執行的 Action IR 應失效。

## 13.5 供應鏈攻擊

相同插件名稱不代表相同能力。Runtime 應鎖定：

- semantic ID；
- publisher；
- version；
- content hash；
- signature。

---

# 十四、工具執行與結果封裝

## 14.1 ToolInvocation

```text
ToolInvocation {
  invocation_id
  action_ir_hash
  plugin_id
  tool_id
  normalized_arguments
  workspace
  environment
  timeout
  idempotency_key
  permission_lease
}
```

## 14.2 ToolResult

```text
ToolResult {
  invocation_id
  status
  structured_output
  stdout_ref
  stderr_ref
  artifacts
  observed_effects
  exit_code
  timing
  evidence
}
```

## 14.3 工具回傳不等於世界真相

工具可能：

- 回傳錯誤；
- 延遲；
- 部分成功；
- 成功回應但世界未改；
- 超時但效果已發生。

Runtime 需額外觀測世界狀態。

---

# 十五、驗證層

## 15.1 驗證分層

1. schema 驗證；
2. 靜態結構驗證；
3. 權限驗證；
4. 沙盒執行；
5. 單元測試；
6. 整合測試；
7. round-trip；
8. 世界狀態檢查；
9. 人類批准；
10. 獨立模型或規則驗證。

## 15.2 驗證器不應與生成器完全同一

若同一模型生成並宣告自己正確，驗證獨立性不足。

## 15.3 Verification Receipt

```text
VerificationReceipt {
  validator
  version
  subject_hash
  tests
  evidence
  result
  uncertainty
}
```

## 15.4 未驗證

`unverified` 是合法狀態，不能被改寫為「大概完成」。

---

# 十六、Commit 與世界差分

## 16.1 預期差分

Action IR 預告：

$$
\Delta W_{\mathrm{expected}}
$$

## 16.2 觀測差分

執行後取得：

$$
\Delta W_{\mathrm{observed}}
$$

## 16.3 差異

$$
d
\left(
\Delta W_{\mathrm{expected}},
\Delta W_{\mathrm{observed}}
\right)
$$

若超過閾值，不得直接 commit。

## 16.4 Commit Record

```text
CommitRecord {
  run_id
  action_id
  before_state
  after_state
  observed_delta
  verification_receipts
  actor
  authority
  timestamp
  compensability
}
```

---

# 十七、可恢復執行

## 17.1 RunCheckpoint

保存：

- 狀態機位置；
- Intent／Task／Capability 雜湊；
- 已完成 Action；
- 待處理 Action；
- ToolResult；
- 事件偏移；
- 權限租約；
- 預算；
- 未完成效果；
- 補償；
- 下一次喚醒。

## 17.2 Crash Recovery

重啟後先判斷：

- Tool 是否執行；
- 效果是否發生；
- Commit 是否完成；
- 事件是否確認；
- 冪等鍵是否存在。

## 17.3 不允許盲目重跑

如果狀態不明，進入：

```text
effect-uncertain
```

並進行觀測或人工處理。

## 17.4 恢復結果

```text
resume
replay-safe
replan
compensate
human-review
abort
```

---

# 十八、重試、降級與替代能力

## 18.1 重試

只對可重試失敗使用，且有：

- 最大次數；
- 退避；
- 抖動；
- 截止時間；
- 冪等；
- 預算。

## 18.2 降級

例如：

```text
高精度模型不可用
→ 改用低成本模型做初步分類
→ 保留高風險項目等待
```

降級不能靜默降低安全或人類批准要求。

## 18.3 替代能力

若工具 $x_1$ 失效，可搜尋：

$$
x_2\models c
$$

但需重新驗證其效果與權限。

## 18.4 重新規劃

若能力集合改變：

$$
\mathcal C_t
\neq
\mathcal C_{t+1}
$$

可重新產生 Capability Plan，但不得改變高層 Intent IR。

---

# 十九、補償與不可逆效果

## 19.1 補償描述

```text
CompensationDescriptor {
  trigger
  inverse_or_repair_capability
  required_permissions
  limitations
  verification
}
```

## 19.2 補償不是 rollback

發送通知後的「再發一封更正」不是讓第一封消失。

## 19.3 不可逆等級

```text
reversible
compensatable
partially-compensatable
irreversible
unknown
```

## 19.4 高不可逆行動

必須：

- 重新觀測世界；
- 重新授權；
- 鎖定 Intent 與 Plan；
- 建立證據；
- 取得人類決策；
- 產生執行前證書。

---

# 二十、人類批准與接管

## 20.1 Human Decision Request

```text
HumanDecisionRequest {
  decision_id
  owner
  question
  evidence
  options
  consequences
  deadline
  silence_policy
}
```

## 20.2 沉默不等於同意

除非原始 Intent IR 明確規定合法默認。

## 20.3 接管

人類應能：

- 暫停；
- 取消；
- 修改意圖；
- 修改權限；
- 選擇計畫；
- 手動完成；
- 要求補償；
- 封存。

## 20.4 接管後恢復

Agent 若再次接手，需重新載入人類已做的世界差分。

---

# 二十一、多 Agent 協作

## 21.1 角色

```text
planner
executor
verifier
observer
approver
coordinator
```

## 21.2 分工不能只靠提示詞

角色應由：

- 能力；
- 權限；
- 任務；
- 狀態；
- 責任；

正式定義。

## 21.3 任務交接

交接包：

```text
Intent IR
Task Slice
Capability Scope
Checkpoint
Evidence
Permissions
Pending Effects
Human Gates
```

## 21.4 合併

多 Agent 結果需要：

- 結構化 diff；
- 衝突；
- 驗證；
- 來源；
- 批准。

## 21.5 驗證者分離

對高風險任務，執行者與最終驗證者應分離。

---

# 二十二、觀測與人類可見狀態

Runtime 應輸出：

- Agent Run；
- 當前狀態；
- 目標；
- 任務；
- 能力；
- 權限；
- 預算；
- 工具調用；
- 世界差分；
- 驗證；
- 等待條件；
- 失敗；
- 補償；
- 下一次喚醒。

## 22.1 事件名稱

```text
agent_run.created
agent_run.woken
agent_run.planned
action.authorized
tool.started
tool.completed
verification.failed
commit.completed
agent_run.suspended
agent_run.completed
```

## 22.2 不可只顯示聊天紀錄

聊天是解釋投影，不是完整執行狀態。

## 22.3 PHOSPHOR／HVSL 類介面

人類可見層應提供：

- 即時狀態；
- 語意 diff；
- 權限變化；
- 事件時間線；
- 風險；
- 一鍵停止；
- 恢復入口。

---

# 二十三、治理根與信任模型

## 23.1 治理根

Runtime 需有不可被一般模型或插件修改的根政策：

- 誰擁有系統；
- 哪些資料不可外流；
- 哪些行動必須人類批准；
- 哪些權限不可自授；
- 哪些證據必須保存；
- 如何撤銷。

## 23.2 信任層

```text
untrusted input
model proposal
validated plan
authorized action
verified result
committed state
```

## 23.3 輸入不等於指令

網頁、文件、郵件、工具輸出中的文字，預設是資料，不得自動提升為高權限意圖。

## 23.4 政策變更

政策更新後，所有受影響 continuation 與 Action IR 需重新驗證。

---

# 二十四、主要失敗模式

## 24.1 模型本體化

把模型誤認為 Agent 的持久執行主體。

## 24.2 工具直通

模型輸出的自由文字直接進入 Shell、API 或檔案系統。

## 24.3 能力與工具混淆

工具失效時，任務語意也被迫改變。

## 24.4 權限長期暴露

一次授權永久有效。

## 24.5 狀態只存在對話

重啟或模型切換後無法恢復。

## 24.6 工具成功幻覺

工具回傳成功便宣告世界狀態已完成。

## 24.7 驗證自證

生成者同時是唯一驗證者。

## 24.8 Commit 過早

效果尚未驗證就更新任務為完成。

## 24.9 重試造成重複效果

缺少冪等與去重。

## 24.10 插件供應鏈污染

相同名稱或版本被替換。

## 24.11 人類介面失真

只顯示自然語言摘要，隱藏實際權限與副作用。

## 24.12 事件遺失與亂序

造成錯誤恢復或舊狀態覆蓋新狀態。

## 24.13 無界成本

Agent 在失敗迴圈中持續消耗模型、API 或算力。

## 24.14 反身擴權

Agent 為完成任務而自行擴大能力。

## 24.15 Runtime 與世界權威混淆

Agent Runtime 不應直接取代特定世界 Kernel 的狀態規則。

---

# 二十五、可證偽研究綱領

## 25.1 能力匹配保真率

比較 Task IR 所需能力與 Runtime 選定能力：

$$
\phi_C
=
1
-
d
\left(
C_{\mathrm{required}},
C_{\mathrm{selected}}
\right)
$$

## 25.2 工具替換穩定性

替換供應者後，檢查：

- Task IR；
- Capability IR；
- 世界結果；
- 驗證；

是否保持。

## 25.3 最小權限率

$$
\eta_A
=
\frac{
|A_{\min}|
}{
|A_{\mathrm{granted}}|
}
$$

越接近 $1$ 越好。

## 25.4 重複效果率

在重試、崩潰與事件重送下，測量非預期重複副作用。

## 25.5 故障恢復時間

測量從 Runtime 中斷到：

```text
合法恢復
重新規劃
人類接管
```

的時間與正確率。

## 25.6 事件重放

重放同一事件歷史，檢查最終狀態是否一致。

## 25.7 驗證獨立性

比較：

- 同模型自評；
- 獨立規則；
- 測試；
- 不同模型；
- 人類；

的錯誤捕捉率。

## 25.8 人類接管可用性

測量人類在有限時間內能否理解：

- 正在做什麼；
- 已改變什麼；
- 如何停止；
- 如何恢復。

## 25.9 模型替換穩定性

更換模型後，測量身份、意圖、任務與承諾的保持。

## 25.10 插件攻擊阻止率

注入：

- 惡意 manifest；
- 權限擴張；
- 同名替換；
- 依賴污染；
- 結果偽造；

測量阻止率。

## 25.11 長時程一致性

在長期喚醒、休眠、遷移與升級下，測量：

- 任務狀態；
- 事件偏移；
- 權限；
- 世界效果；
- 人類閘門；

是否一致。

---

# 二十六、第三部總結：從意圖到可恢復行動

第三部三篇建立完整鏈條。

第七篇：

$$
\boxed{
\text{Intent IR}
\rightarrow
\text{Task IR}
\rightarrow
\text{Capability IR}
}
$$

回答「目的如何轉為合法能力計畫」。

第八篇：

$$
\boxed{
\text{Capability Plan}
\rightarrow
\text{Temporal–Spatial Control Graph}
}
$$

回答「能力計畫如何跨時間、事件、等待與恢復」。

本文：

$$
\boxed{
\text{Control Graph}
\rightarrow
\text{Agent Runtime}
\rightarrow
\text{Verified World Delta}
}
$$

回答「Runtime 如何真正調用工具、保存狀態、處理失敗並提交結果」。

第三部總鏈：

$$
\boxed{
\text{Intent Contract}
\rightarrow
\text{Task Graph}
\rightarrow
\text{Capability Plan}
\rightarrow
\text{Temporal Control}
\rightarrow
\text{Authorized Action}
\rightarrow
\text{Verified Commit}
}
$$

---

# 二十七、與第四部的橋接

Agent Runtime 只能執行能力，卻不應自行定義所有世界規則。

下一篇將處理：

> 當 Runtime 對一個持久數位世界、模擬世界、遊戲世界、研究環境或組織狀態採取行動時，什麼系統才是世界狀態的權威？

將建立：

$$
\text{Action IR}
\rightarrow
\text{World Kernel}
\rightarrow
\Delta W
\rightarrow
\text{Event Ledger}
$$

並區分：

- Agent Runtime；
- 世界 Runtime；
- 外部操作協議；
- 敘事投影；
- 人類治理。

---

# 二十八、本文的十五項命題

## 命題一

$$
\boxed{
\text{Model}
\neq
\text{Agent Runtime}
}
$$

## 命題二

Runtime 是持久執行身分、狀態、權限與效果的權威。

## 命題三

能力、工具、插件與供應者必須分層表示。

## 命題四

模型產生的是候選 Action IR，而不是已授權行動。

## 命題五

MCP、API、CLI 與插件不構成完整 Agent Runtime。

## 命題六

每次對外效果都應經過 Wake、Restore、Observe、Plan、Authorize、Execute、Verify、Commit。

## 命題七

工具回傳成功不等於世界狀態成功。

## 命題八

Commit 必須晚於獨立驗證。

## 命題九

每次 Agent Run 應使用最小、短期、可撤銷的權限租約。

## 命題十

本地優先是敏感資源控制邊界，而不是拒絕所有雲端能力。

## 命題十一

可恢復執行需要事件偏移、冪等鍵、效果狀態與 checkpoint。

## 命題十二

補償不能被描述成完美 rollback。

## 命題十三

人類必須能查看、暫停、接管與撤回。

## 命題十四

Runtime 的反身能力不得變成自我授權。

## 命題十五

$$
\boxed{
\text{Executable Agency}
=
\text{Persistent State}
+
\text{Capability Contracts}
+
\text{Policy Gates}
+
\text{Tool Execution}
+
\text{Verification Evidence}
}
$$

---

# 二十九、結論：Agent 的主體不在模型單點，而在執行閉環

模型可以是極強的推理器。

但模型不應單獨擁有：

- 世界狀態；
- 長期權限；
- 憑證；
- 工具結果真值；
- Commit 權；
- 事件偏移；
- 補償歷史；
- 人類批准。

真正可執行的 Agent 必須由一個外部、持久且可治理的 Runtime 承載。

其閉環為：

$$
\boxed{
\text{Wake}
\rightarrow
\text{Restore}
\rightarrow
\text{Reason}
\rightarrow
\text{Authorize}
\rightarrow
\text{Act}
\rightarrow
\text{Verify}
\rightarrow
\text{Commit}
\rightarrow
\text{Persist}
}
$$

模型可以被更換。

工具可以被替換。

供應者可以離線。

工作可以跨機器恢復。

只要意圖、任務、能力、狀態、權限、證據與因果鏈保持，Agent 的執行連續性便可以持續。

因此，本文的最終命題是：

$$
\boxed{
\text{Agent 並不是一個會調用工具的模型。}
}
$$

$$
\boxed{
\text{Agent 是一個由模型參與、但由 Runtime 承載的}
}
$$

$$
\boxed{
\text{可授權、可驗證、可恢復、可撤回的執行閉環。}
}
$$

第三部至此完成。下一步將進入世界層：能力計畫與 Agent Runtime 所產生的 Action IR，如何在一個具有權威狀態、規則、事件、角色與歷史的可編譯世界中合法改變現實。

---

# 附錄 A：Runtime Run 規格

```yaml
agent_run:
  run_id: "run-20260725-001"
  agent_id: "agent-project-maintainer"
  status: "waiting-authorization"

wake_event:
  event_id: "wake-001"
  reason: "repository_changed"
  idempotency_key: "repo-change:abc123"
  causal_parents:
    - "git-event-998"

restore:
  intent_hash: "sha256:..."
  task_hash: "sha256:..."
  capability_hash: "sha256:..."
  continuation_id: "cont-004"
  world_state_hash: "sha256:..."

plan:
  model_provider: "provider-a"
  model_version: "model-x"
  candidate_actions:
    - "action-001"

authorization:
  required:
    - "workspace:read"
    - "feature_branch:write"
  granted:
    - "workspace:read"
  missing:
    - "feature_branch:write"

next_state:
  status: "waiting-authorization"
  human_decision_id: "decision-branch-write"
```

---

# 附錄 B：Plugin Manifest

```yaml
plugin:
  id: "org.evemisslab.git-workspace"
  version: "0.1.0"
  publisher: "EveMissLab"
  signature: "sig:..."
  status: "validated"

capabilities:
  - semantic_id: "cap.repository.read"
  - semantic_id: "cap.repository.create_feature_branch"
  - semantic_id: "cap.repository.apply_patch"
  - semantic_id: "cap.repository.run_tests"

permissions:
  filesystem:
    scope: "workspace"
    modes:
      - "read"
      - "write-feature-branch"
  network:
    allow:
      - "github.com"
  shell:
    allow_commands:
      - "git"
      - "python"
      - "pytest"

sandbox:
  process_isolation: true
  max_runtime_seconds: 600
  max_memory_mb: 2048

validators:
  - "schema"
  - "git_diff"
  - "test_result"
  - "workspace_scope"

provenance:
  source_hash: "sha256:..."
  dependencies_lock: "sha256:..."
```

---

# 附錄 C：Action IR 與 ToolResult

```yaml
action_ir:
  action_id: "action-001"
  capability_id: "cap.repository.apply_patch"
  plugin_id: "org.evemisslab.git-workspace"
  tool_id: "git.apply_patch"

arguments:
  workspace: "workspace://project-a"
  branch: "feature/intent-001"
  patch_artifact: "artifact://patch-001"

world_precondition:
  repository_head: "git:abc123"

authorization:
  lease_id: "lease-001"
  expires_at: "2026-07-25T22:00:00+08:00"

budget:
  writes: 1
  runtime_seconds: 120

verification:
  - "patch_applied_cleanly"
  - "tests_pass"
  - "main_branch_unchanged"

idempotency:
  key: "intent001-task002-patch001"

compensation:
  capability: "cap.repository.revert_commit"
  limitations:
    - "external clones are not reverted"
```

```yaml
tool_result:
  invocation_id: "invoke-001"
  action_id: "action-001"
  status: "succeeded"

structured_output:
  commit: "git:def456"
  files_changed: 4

observed_effects:
  - "feature_branch_created"
  - "working_tree_modified"
  - "commit_created"

verification_status: "pending"
```

---

# 附錄 D：Execution Certificate

```yaml
execution_certificate:
  certificate_id: "exec-cert-001"
  status: "committed"

hashes:
  intent_ir: "sha256:..."
  task_ir: "sha256:..."
  capability_plan: "sha256:..."
  action_ir: "sha256:..."
  before_world: "sha256:..."
  after_world: "sha256:..."

authority:
  requester: "project_owner"
  lease: "lease-001"
  scope:
    - "workspace:read"
    - "feature_branch:write"

execution:
  plugin: "org.evemisslab.git-workspace@0.1.0"
  tool: "git.apply_patch"
  invocation: "invoke-001"
  idempotency_key: "intent001-task002-patch001"

verification:
  receipts:
    - "verify-schema-001"
    - "verify-tests-001"
    - "verify-diff-001"
  result: "passed"

world_delta:
  created:
    - "branch:feature/intent-001"
    - "commit:def456"
  modified:
    - "4 files"
  protected:
    - "main branch unchanged"

compensation:
  available: true
  capability: "cap.repository.revert_commit"
```

---

# 附錄 E：第三部三篇文件

7. **意圖中介表示：從自然語言要求到可驗證能力計畫**
8. **時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行**
9. **Agent Runtime：能力規劃、工具調用與可恢復執行**

第三部總鏈：

$$
\boxed{
\text{Intent Contract}
\rightarrow
\text{Task and Capability IR}
\rightarrow
\text{Temporal Control Graph}
\rightarrow
\text{Authorized Action}
\rightarrow
\text{Verified Commit}
}
$$

---

# 附錄 F：系列十二篇位置

1. 從程式碼到意圖：程式概念的歷史轉換與後文本時代
2. 自然語言原生計算：從語句生成到語義狀態轉換
3. 形式化壓縮與算子演化：自然語言、形式語言與計算結構的生成
4. 語意附加程式設計：EML 與宿主中立語義中介層
5. 結構先於文字：Nova 與後文本程式語言本體論
6. 符號作為算子：從靜態字元到可組合計算閉包
7. 意圖中介表示：從自然語言要求到可驗證能力計畫
8. 時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行
9. **Agent Runtime：能力規劃、工具調用與可恢復執行**
10. 可編譯世界：從程式執行到世界狀態演化
11. 人類可見狀態：意圖程式系統的稽核、解釋與可逆治理
12. 意圖程式文明：後文本語言、持續 Agent 與可編譯世界的統一理論

---

# 參考文獻

## Neo.K／EveMissLab 理論與規格文件

1. Neo.K with Aletheia，《意圖中介表示：從自然語言要求到可驗證能力計畫》，2026。
2. Neo.K with Aletheia，《時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行》，2026。
3. Neo.K，《本地優先 AI Agent 通用插件運行層技術白皮書》，2026。
4. Neo.K，《外部時間基礎設施承載的自我喚醒智能體》，2026。
5. Neo.K，《通用脈衝式 Agent：間歇喚醒、狀態連續性與自主工具調用的未來架構》，2026。
6. Neo.K，《Temporal Loop Runtime Spec》，2026。
7. Neo.K，《NOEMA Agent OS 技術白皮書》，2026。
8. Neo.K，《Noesis Studio／NOEMA AgentOS Human Cockpit》，2026。
9. Neo.K，《HVSL：人類可見狀態層》，2026。
10. Neo.K，《Agent Semantic Pad》，2026。

## 一般理論背景

11. Lampson, B. W., “Protection,” 1971.
12. Saltzer, J. H. and Schroeder, M. D., “The Protection of Information in Computer Systems,” 1975.
13. Lamport, L., “Time, Clocks, and the Ordering of Events in a Distributed System,” 1978.
14. Hewitt, C. et al., “A Universal Modular Actor Formalism for Artificial Intelligence,” 1973.
15. Garcia-Molina, H. and Salem, K., “Sagas,” 1987.
16. Gray, J. and Reuter, A., *Transaction Processing*, 1992.
17. Hohpe, G. and Woolf, B., *Enterprise Integration Patterns*, 2003.
18. Kleppmann, M., *Designing Data-Intensive Applications*, 2017.

---

# 版本紀錄

## v0.1 — 2026-07-25

- 完成系列第九篇與第三部收束。
- 建立 Agent Runtime 十二元模型。
- 明確區分模型、能力、工具、插件與供應者。
- 建立 Capability Registry 與 Action IR。
- 建立 Wake、Restore、Observe、Plan、Authorize、Execute、Verify、Commit 九階段交易。
- 形式化 Runtime 狀態機、Wake Queue、事件偏移與 no-op。
- 建立持久狀態、記憶分類與模型替換連續性。
- 建立最小權限、權限租約與本地優先安全邊界。
- 建立插件 manifest、供應鏈、沙盒與撤銷。
- 建立 ToolInvocation、ToolResult、Verification Receipt 與 Commit Record。
- 建立 crash recovery、effect-uncertain、重試、降級與替代能力。
- 建立補償、人類接管、多 Agent 分工與人類可見狀態。
- 建立治理根與信任層。
- 提出十五類失敗模式與十一項可證偽研究基準。
- 完成第三部總鏈並銜接可編譯世界。
