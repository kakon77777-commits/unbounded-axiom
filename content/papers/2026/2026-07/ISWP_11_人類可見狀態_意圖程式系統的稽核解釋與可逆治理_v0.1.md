---
title: "人類可見狀態：意圖程式系統的稽核、解釋與可逆治理"
english_title: "Human-Visible State: Auditability, Explanation, and Reversible Governance in Intent-Driven Systems"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "11/12"
part: "第四部：可編譯世界與程式治理"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-25"
language: "zh-TW"
document_type: "理論論文／人機治理架構"
status: "初版完成"
---

# 人類可見狀態：意圖程式系統的稽核、解釋與可逆治理

## Human-Visible State: Auditability, Explanation, and Reversible Governance in Intent-Driven Systems

**系列：**《意圖—結構—世界程式論》第十一篇  
**部別：**第四部「可編譯世界與程式治理」  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 25 日  

---

## 摘要

意圖驅動程式、長時程 Agent 與可編譯世界，使機器能跨檔案、工具、時間、權限與世界狀態執行複雜行動。然而，系統能力的增加不等於人類控制能力的增加。若人類只能看到聊天式摘要、完成標記、進度動畫或原始日誌，而無法理解原始意圖、計畫版本、權限範圍、工具調用、世界差分、未驗證項、失敗、補償與回復路徑，Agent 越強，黑箱治理風險反而越高。

本文提出「人類可見狀態層」（Human-Visible State Layer, HVSL）的完整理論：HVSL 不是額外 UI，也不是將終端機輸出換成自然語言，而是一個與 Intent IR、Task IR、Capability IR、Agent Runtime、World Kernel 與 Event Ledger 同步的治理投影層。它把機器狀態、開發者狀態、治理狀態與使用者狀態轉換為可追溯、可驗證、可操作的人類視圖，同時保留由摘要下鑽至證據的能力。

本文將 HVSL 表示為：

$$
\mathbb H_V
=
\left\langle
\mathcal I,
\mathcal P,
\mathcal A,
\mathcal X,
\mathcal W,
\mathcal E,
\mathcal V,
\mathcal U,
\mathcal R,
\mathcal G,
\mathcal C
\right\rangle
$$

其中依序代表意圖視圖、計畫視圖、授權視圖、執行視圖、世界差分視圖、證據與驗證、不確定性、風險、回復、治理控制與因果來源。

本文主張：

$$
\boxed{
\text{Visible Output}
\neq
\text{Human-Visible State}
}
$$

單純顯示「完成」、百分比或聊天摘要不構成可見狀態。HVSL 至少必須回答：系統為何行動、做了什麼、沒有做什麼、以何種權限、改變了什麼、證明了什麼、未證明什麼、誰受影響、是否可逆、人類現在能做什麼。

本文建立六層證據梯：狀態摘要、語意差分、結構差分、執行證據、原始證據與可重放證書。人類不必預設閱讀所有技術細節，但任何重要宣稱都必須能沿證據鏈下鑽。系統不得以自然語言解釋取代來源資料，也不得用大量 log 傾倒冒充透明。

本文進一步提出「可見性不變量」：人類可見狀態必須與 Runtime 權威狀態具有可驗證對應；不得遺漏高風險差分、權限擴張、人類保留決策、未確定效果與不可逆行動；任何顯示為完成的任務都必須對應成功條件與驗證證據。本文將不可見性債表示為：

$$
D_{\mathrm{inv}}
=
C_{\mathrm{discover}}
+
C_{\mathrm{interpret}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{recover}}
+
R_{\mathrm{hidden}}
$$

其中包含人類自行追查狀態、理解技術輸出、確認結果、找出回復方法與承擔隱藏風險的成本。

本文建立可逆治理控制：暫停、取消、撤回、回復、補償、分支、接管、重新授權與封存。可逆治理不承諾所有世界狀態都能回到過去，而要求系統在行動前聲明可逆性等級、提供合法反向能力或補償計畫，並對不可逆效果提高批准與證據門檻。

本文同時分析解釋風險。解釋可能產生合理化、事後敘事、來源混淆、虛假因果、選擇性揭露與認知操縱。因此，HVSL 區分目的解釋、計畫解釋、權限解釋、因果解釋、證據解釋與反事實解釋，並要求每類解釋綁定不同證據。

本文最後提出可證偽研究綱領，包括狀態保真、假完成率、證據下鑽成功率、權限可見性、風險揭露、回復成功率、人類接管時間、不可見性債、認知負荷、解釋忠實度、無障礙可用性與跨介面一致性。本文的核心結論是：在意圖程式文明中，透明不是「AI 願意說明」，而是人類具有持續看見、驗證、反駁、停止與改變系統行動的結構性權力。

**關鍵詞：** HVSL、人類可見狀態、不可見性債、Agent 稽核、可逆治理、狀態解釋、人類接管、證據鏈、語意差分、AI 協作

---

## Abstract

Intent-driven programming, long-horizon agents, and compilable worlds enable machines to act across files, tools, time, permissions, and persistent world states. Yet greater system capability does not automatically increase human control. If humans can see only conversational summaries, completion badges, progress animations, or raw logs, while remaining unable to inspect intent, plan versions, authorization scopes, tool invocations, world deltas, unverified claims, failures, compensation, and recovery paths, more powerful agents may create deeper governance black boxes.

This paper develops the Human-Visible State Layer (HVSL) as a formal governance layer synchronized with Intent IR, Task IR, Capability IR, Agent Runtime, World Kernel, and Event Ledger. HVSL is not merely an interface or a natural-language wrapper around terminal output. It translates machine, developer, governance, and user states into traceable, verifiable, and actionable human views while preserving drill-down paths to evidence.

The formal model is:

$$
\mathbb H_V
=
\left\langle
\mathcal I,
\mathcal P,
\mathcal A,
\mathcal X,
\mathcal W,
\mathcal E,
\mathcal V,
\mathcal U,
\mathcal R,
\mathcal G,
\mathcal C
\right\rangle
$$

The paper distinguishes visible output from human-visible state, introduces a six-level evidence ladder, defines visibility invariants, models invisibility debt, and develops reversible governance controls such as pause, cancel, revoke, recover, compensate, branch, take over, reauthorize, and archive.

It also examines explanation risks: rationalization, post-hoc storytelling, provenance confusion, false causality, selective disclosure, and cognitive manipulation. Multiple explanation types are separated and bound to different evidence requirements.

The central conclusion is that transparency in an intent-programming civilization is not the willingness of AI to explain itself. It is the structural power of humans to continuously see, verify, contest, stop, and redirect machine action.

**Keywords:** HVSL, human-visible state, invisibility debt, agent auditability, reversible governance, explanation fidelity, human takeover, evidence chains

---

# 一、問題的提出：看見輸出，不等於看見系統

Agent 回覆：

```text
完成了。
```

人類仍然不知道：

- 完成了哪個目標；
- 修改了哪些東西；
- 是否真的執行；
- 是否只是生成草稿；
- 是否測試；
- 是否有失敗；
- 是否使用新增權限；
- 是否改變正式世界；
- 是否還有未完成義務；
- 如何撤銷。

另一種系統可能貼出數千行 log。資訊雖然存在，人類仍然無法快速回答同樣的問題。

因此：

$$
\boxed{
\text{Data Availability}
\neq
\text{State Understandability}
}
$$

也就是：

$$
\boxed{
\text{Visible Output}
\neq
\text{Human-Visible State}
}
$$

人類可見狀態不是「畫面上有東西」，而是人類能以合理成本理解系統目前處於何種意圖、控制、權限、執行、世界與治理狀態。

---

# 二、HVSL 的正式定義

本文定義：

> **HVSL 是將意圖程式系統的權威狀態與證據，轉譯為可理解、可驗證、可操作、可下鑽且不隱藏治理差分的人類視圖之正式系統層。**

其輸入不是聊天文字，而是：

$$
S_{\mathrm{auth}}
=
\left(
I,
T,
C,
R_A,
K_W,
L,
V,
P
\right)
$$

其中包含 Intent、Task、Capability、Agent Runtime、World Kernel、Ledger、Verification 與 Policy 的權威資料。

HVSL 不是第二套狀態庫。若：

$$
S_{\mathrm{HVSL}}
\neq
\Pi_H(S_{\mathrm{auth}})
$$

則 Dashboard、聊天摘要或管理介面已經變成新的錯誤權威。

---

# 三、四層狀態翻譯

## 3.1 機器狀態

包含：

- process；
- exit code；
- stack trace；
- event offsets；
- database transactions；
- API response；
- resource metrics；
- hashes；
- raw deltas。

## 3.2 開發者狀態

翻譯為：

- build 是否成功；
- 哪個模組失敗；
- 哪些檔案改變；
- 測試通過情形；
- 哪些事件提交；
- 哪個版本被使用。

## 3.3 治理狀態

回答：

- 誰授權；
- 授權範圍；
- 是否越權；
- 哪些主體受影響；
- 是否需要批准；
- 是否可逆；
- 哪些政策適用；
- 是否有未決爭議。

## 3.4 使用者狀態

回答：

```text
現在發生了什麼？
結果是否符合我的目的？
我需要做什麼？
我能如何確認？
我能如何停止或回復？
```

完整翻譯鏈：

$$
\text{Machine State}
\rightarrow
\text{Developer State}
\rightarrow
\text{Governance State}
\rightarrow
\text{User State}
$$

任何上層摘要都必須能追溯到下層證據。

---

# 四、HVSL 的十一個視圖

## 4.1 Intent View

顯示：

- 原始要求；
- Intent IR 版本；
- 目標；
- 非目標；
- 硬限制；
- 人類保留決策；
- 已授權修訂；
- 意圖漂移。

## 4.2 Plan View

顯示：

- Task Graph；
- 當前節點；
- 已完成；
- 待完成；
- 阻塞；
- 替代計畫；
- 計畫版本；
- 修訂原因。

## 4.3 Authorization View

顯示：

- 目前權限；
- 租約；
- 使用過的高風險能力；
- 權限擴張；
- 批准者；
- 到期時間；
- 撤銷方法。

## 4.4 Execution View

顯示：

- 實際工具；
- provider；
- Action IR；
- 執行時間；
- 參數摘要；
- 工作區；
- 結果；
- 重試；
- `effect-uncertain`。

## 4.5 World Delta View

顯示：

$$
W_{\mathrm{before}}
\rightarrow
W_{\mathrm{after}}
$$

以及新增、修改、刪除、外部通知、公開發布、角色改變與不可逆效果。

## 4.6 Evidence View

顯示：

- 測試；
- 驗證器；
- 證書；
- ToolResult；
- Event IR；
- Commit Record；
- Snapshot；
- Replay。

## 4.7 Uncertainty View

區分：

```text
已確認
高信心推論
低信心推論
尚未確認
無法確認
需要人類決定
```

## 4.8 Risk View

顯示風險、影響主體、影響範圍、不可逆性、失敗成本與補償狀態。

## 4.9 Recovery View

顯示暫停、取消、撤回、回復、補償、分支、接管與封存。

## 4.10 Provenance View

回答：

- 誰提出；
- 哪個模型建議；
- 哪個 Agent 執行；
- 哪個工具；
- 哪個版本；
- 誰批准；
- 哪些資料影響。

## 4.11 Governance Control View

讓人類可以改變意圖、限制作用域、調整權限、要求驗證、暫停、接管、阻止 Commit、要求補償與撤銷持續任務。

---

# 五、可見性不變量

## 5.1 狀態保真

顯示狀態 $S_H$ 必須能映射回權威狀態 $S_A$ ：

$$
d
\left(
S_H,
\Pi_H(S_A)
\right)
\leq
\epsilon
$$

## 5.2 高風險完整性

所有權限擴張、不可逆行動、人類保留決策、影響第三方、世界規則改變與未確定效果，不得被摘要省略。

## 5.3 完成一致性

若 UI 顯示 `completed`，則必須存在：

$$
V_{\mathrm{goal}}
\land
V_{\mathrm{constraint}}
\land
V_{\mathrm{world}}
\land
V_{\mathrm{evidence}}
$$

## 5.4 未驗證保持

底層為 `unverified` 時，人類視圖不得顯示 `verified`、`safe` 或 `completed`。

## 5.5 權限可見性

任何效果都能追溯到：

$$
\operatorname{Authority}(e)
$$

## 5.6 因果可追溯

任何重要結果 $r$ 都能找到：

$$
\operatorname{Causes}(r)
$$

## 5.7 控制可達

若系統仍在執行，人類必須有可達的暫停、取消或接管入口，除非明示該效果已不可中止。

---

# 六、不可見性債

Agent 不可見性債是：

> 人類為理解、確認、控制與恢復 Agent 行動，被迫承擔的額外認知與操作成本。

形式化為：

$$
\boxed{
D_{\mathrm{inv}}
=
C_{\mathrm{discover}}
+
C_{\mathrm{interpret}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{recover}}
+
R_{\mathrm{hidden}}
}
$$

其中：

- $C_{\mathrm{discover}}$ ：自行找到狀態；
- $C_{\mathrm{interpret}}$ ：理解技術資料；
- $C_{\mathrm{verify}}$ ：自行驗證；
- $C_{\mathrm{recover}}$ ：自行尋找回復路徑；
- $R_{\mathrm{hidden}}$ ：不知道需要檢查的風險。

使用者確認狀態所花的時間：

$$
C_{\mathrm{human-time}}
$$

是自動化的真實成本，不能被排除。

---

# 七、六層證據梯

## 7.1 狀態摘要

例如：

```text
功能已完成。
正式環境未修改。
兩項測試通過，一項尚未驗證。
```

## 7.2 語意差分

回答哪個目標完成、哪個限制保持、哪個權限使用、哪個世界狀態改變。

## 7.3 結構差分

顯示 Task IR、Capability IR、GraphPatch、World Delta 與事件關係。

## 7.4 執行證據

顯示 ToolInvocation、ToolResult、Test Report、Verification Receipt 與 Commit Record。

## 7.5 原始證據

包含 log、stdout、stderr、API response、raw diff、database row 與 sensor data。

## 7.6 可重放證書

提供 Snapshot、Event Ledger、版本、hash、Replay 與可重現編譯。

完整梯度：

$$
\text{Summary}
\rightarrow
\text{Semantic Diff}
\rightarrow
\text{Structural Diff}
\rightarrow
\text{Execution Evidence}
\rightarrow
\text{Raw Evidence}
\rightarrow
\text{Replay Certificate}
$$

---

# 八、摘要不是證據

摘要可以降低認知負荷、突出風險並提供決策入口，但不能取代：

- Event Ledger；
- ToolResult；
- 測試；
- 權限證書；
- World Delta；
- 原始失敗。

每個摘要宣稱應綁定：

```text
claim_id
source_records
confidence
generator
generated_at
```

「已處理」可能代表已規劃、已執行、已提交、已驗證或已補償。狀態詞必須有明確定義。

---

# 九、解釋的六種類型

## 9.1 目的解釋

回答為什麼做，來源是 Intent IR。

## 9.2 計畫解釋

回答為何選擇某路徑，來源是候選計畫、成本、風險與能力比較。

## 9.3 權限解釋

回答憑什麼有權做，來源是 Authority、Lease、Approval 與 Policy。

## 9.4 因果解釋

回答哪些事件造成結果，來源是 Event Ledger 與 causal parents。

## 9.5 證據解釋

回答為何相信成功，來源是 Verification Receipts。

## 9.6 反事實解釋

回答若不做或採另一計畫可能如何，來源是模擬、分支或受限推論，不得冒充已發生事實。

---

# 十、解釋性風險

## 10.1 事後合理化

模型在結果發生後生成一個聽起來合理、但不是實際決策原因的故事。

## 10.2 來源混淆

把使用者明示、模型推論、組織政策與世界規則混成單一理由。

## 10.3 虛假因果

把時間先後誤認為因果。

## 10.4 選擇性揭露

只顯示成功證據，不顯示失敗與未驗證。

## 10.5 可讀性操縱

使用流暢語言降低人類警覺。

## 10.6 過度簡化

將多主體、權限與不可逆風險壓縮成「建議繼續」。

每個重要解釋需標記：

```text
explanation_type
evidence_scope
direct_or_inferred
uncertainty
omitted_dimensions
```

---

# 十一、可逆治理

可逆治理不承諾所有世界狀態都能回到過去：

$$
\boxed{
\text{Reversible Governance}
\neq
\text{Perfect World Reversal}
}
$$

它要求人類能理解並選擇合法控制與補救方式。

九種控制為：

```text
pause
cancel
revoke
rollback
compensate
branch
takeover
reauthorize
archive
```

- 暫停：阻止新 Action，保留 continuation。
- 取消：終止尚未提交的任務。
- 撤回：撤回 Intent 或 Authority。
- Rollback：只適用於真正可逆狀態。
- 補償：以新行動修復、抵消或說明舊效果。
- 分支：保留原歷史，建立替代世界或計畫。
- 接管：人類取得控制，Agent 進入暫停。
- 重新授權：修改權限與作用域後恢復。
- 封存：停止持續執行但保留證據。

---

# 十二、可逆性分級

每個 Action 與 World Delta 應標記：

```text
fully_reversible
transactionally_reversible
compensatable
partially_compensatable
irreversible
unknown
```

未知必須採保守治理，不得當成可逆。

對不可逆行動，HVSL 應在執行前顯示：

- 行動本體；
- 影響主體；
- 權限；
- 失敗後果；
- 不可回復內容；
- 可能補償；
- 決策所有者。

---

# 十三、Diff-first Review

最終畫面可能沒變，但底層權限、資料流、世界規則、依賴、隱私與成本可能已改變。

因此應提供：

- Intent Diff；
- Task Diff；
- Capability Diff；
- Permission Diff；
- Action Diff；
- World Delta；
- Policy Diff；
- Evidence Diff。

差分優先序：

$$
Priority
=
Impact
\times
Irreversibility
\times
Uncertainty
\times
AuthorityChange
$$

人類批准的對象應是某一版本的結構化差分與證據包，而不是持續變動的模糊任務。

---

# 十四、人類控制語言與 Agent Semantic Pad

高頻控制可以結構化：

```text
繼續
暫停
停止
只限目前
先驗證
不要提交
建立分支
回復
要求證據
交給人類
```

控制操作碼：

$$
o_h
=
\left(
\text{operator},
\text{scope},
\text{phase},
\text{authority},
\text{termination}
\right)
$$

它必須映射到當前 Intent、Run、Task、Workspace、World 與 Permission，而不是固定文字巨集。

「繼續」不能自動批准新的高風險權限或不可逆世界行動。

介面提供哪些操作碼，會影響人類如何理解任務。因此 Semantic Pad 不應只暴露加速、執行與接受，也應暴露：

- 質疑；
- 驗證；
- 暫停；
- 分支；
- 回退；
- 限制；
- 顯示不確定性。

---

# 十五、人類可見狀態的最小卡片

```yaml
human_visible_state:
  status: "waiting-human"
  intent: "建立審核版本，不直接上線"

  completed:
    - "建立功能分支"
    - "部署預覽"
    - "通過自動測試"

  not_done:
    - "未部署正式環境"

  changed:
    - "4 個檔案"
    - "建立 preview deployment"

  authorization:
    used:
      - "feature_branch:write"
      - "preview:deploy"
    not_used:
      - "production:deploy"

  verification:
    confirmed:
      - "unit tests"
      - "preview healthcheck"
    unverified:
      - "mobile visual review"

  risk:
    level: "medium"
    irreversible_effects: []

  waiting_for:
    - "project_owner approval"

  controls:
    - "approve"
    - "request_changes"
    - "pause"
    - "cancel"
    - "view_diff"
    - "view_evidence"
```

---

# 十六、時間線、因果圖與切片

時間線顯示意圖建立、計畫、權限、工具、驗證、Commit、失敗、補償與人類介入。

因果圖顯示：

$$
e_i
\leadsto
e_j
$$

人類可查詢：

```text
只看權限變更
只看外部寫入
只看失敗
只看 AI 推論
只看人類批准
只看不可逆事件
```

顏色不能成為唯一辨識方式，需同時提供文字、圖示、無障礙標籤與可篩選欄位。

---

# 十七、世界可見狀態

對 CompilableWorld，HVSL 應區分：

## 17.1 World Definition Diff

Canon、schema、規則、模組與遷移改變。

## 17.2 Runtime State Diff

實體、關係、資源、角色與任務狀態改變。

## 17.3 Event Diff

新增哪些已提交世界事件。

## 17.4 Belief Diff

哪些角色學到、誤解或遺忘資訊。

## 17.5 Projection Diff

UI 或敘事改變，但權威世界是否未改變。

世界操作與世界規則修改必須用不同治理介面呈現。

---

# 十八、多主體可見性

世界所有者、一般使用者、受影響者、審計者與 Agent 不應看到完全相同內容。

HVSL 需要同時滿足：

- 透明；
- 隱私；
- 最小揭露；
- 角色權限；
- 安全。

重要行動可能需要向受影響者提供：

- 發生了什麼；
- 為何；
- 依據；
- 申訴；
- 回復或補救。

不得只對系統所有者透明。若行動影響他人權利，只讓管理者看見並不構成完整治理。

---

# 十九、無障礙與認知可用性

HVSL 應支援：

- 文字；
- 語音；
- 結構導航；
- 鍵盤；
- 高對比；
- 放大；
- 簡易模式；
- 專家模式。

透明不等於傾倒全部資料。預設應顯示決策相關內容，再允許逐層展開。

同一狀態不能在不同頁面被含糊地稱為 `done`、`finished`、`committed` 或 `published`，除非它們被定義為不同狀態。

個人化可以調整資訊密度，但不得隱藏治理必要資訊。

---

# 二十、稽核包

對重要 Run，系統應輸出：

$$
\mathcal A_P
=
\left\langle
I,
T,
C,
A,
X,
\Delta W,
E,
V,
R,
G
\right\rangle
$$

其中依序代表意圖、任務、能力、授權、執行、世界差分、事件、驗證、回復與治理決策。

稽核包不是所有 log 的 ZIP。它應提供：

- 索引；
- 摘要；
- 結構化證據；
- 原始證據引用；
- 雜湊；
- 版本；
- 重放說明。

它也應可由獨立工具閱讀，不綁定單一 Agent UI。

---

# 二十一、主要失敗模式

## 21.1 Done 反模式

只說完成，不提供完成定義與證據。

## 21.2 Log Dump

大量原始輸出，沒有決策摘要。

## 21.3 False Completion

未驗證卻標記完成。

## 21.4 Hidden Assumption

推論與明示混淆。

## 21.5 Invisible Permission Expansion

新增權限未顯示。

## 21.6 Narrative Substitution

用自然語言故事取代世界與執行證據。

## 21.7 Recovery Theater

顯示可回復，實際沒有合法回復能力。

## 21.8 Selective Diff

只顯示檔案變化，不顯示政策、權限與世界變化。

## 21.9 Silent Compensation Failure

補償失敗未告知。

## 21.10 Control Illusion

介面有停止按鈕，但行動已不可中止。

## 21.11 Dashboard Truth Monopoly

Dashboard 成為沒有證據連結的第二套真實來源。

## 21.12 Explanation Rationalization

事後生成合理理由。

## 21.13 Cognitive Overload

用資訊過量阻止有效理解。

## 21.14 Accessibility Exclusion

只靠圖形、顏色與拖拉操作。

## 21.15 Observer Privilege Blindness

只對擁有者透明，忽略受影響者。

---

# 二十二、可證偽研究綱領

## 22.1 狀態保真

$$
\phi_H
=
1
-
d
\left(
S_H,
\Pi_H(S_A)
\right)
$$

## 22.2 假完成率

$$
R_F
=
\frac{
\text{displayed completed without sufficient evidence}
}{
\text{all completed displays}
}
$$

## 22.3 證據下鑽成功率

測量人類是否能從摘要定位到支持宣稱的原始證據。

## 22.4 權限可見性

測量人類是否能正確識別使用、擴張、未使用與可撤銷權限。

## 22.5 風險揭露率

對高風險與不可逆 Action，測量是否在批准前完整顯示。

## 22.6 回復成功率

比較 UI 宣稱的回復能力與實際結果。

## 22.7 人類接管時間

從接管需求出現到人類取得有效控制所需時間。

## 22.8 不可見性債

測量使用者為確認結果而開啟額外工具、查閱文件與反覆詢問的時間。

## 22.9 認知負荷

比較原始 log、單一摘要與分層 HVSL 的決策正確率與時間。

## 22.10 解釋忠實度

比較顯示理由與實際 Decision Receipt、Plan Revision 及 Event Causes。

## 22.11 無障礙可用性

測量純鍵盤、螢幕閱讀器、低視力與認知簡化模式的任務完成率。

## 22.12 跨介面一致性

Web、CLI、IDE、手機與語音介面對同一權威狀態應顯示相容結論。

---

# 二十三、與第七至第十篇的關係

Intent IR 提供目的、非目標、限制、人類保留決策與修訂。

時空控制提供等待、喚醒、租約、預算、檢查點與恢復條件。

Agent Runtime 提供 Action IR、工具、權限、驗證、Commit、失敗與補償。

CompilableWorld 提供 World Definition、Runtime State、Event Ledger、Canon、信念與分支。

因此：

$$
\boxed{
\text{HVSL}
=
\Pi_{\mathrm{governable}}
\left(
I,T,C,R_A,K_W,L,V,P
\right)
}
$$

---

# 二十四、與最終篇的橋接

前十一篇已建立程式本體擴張、自然語言原生計算、形式化壓縮、EML、Nova、SOS、Intent IR、時空控制、Agent Runtime、CompilableWorld 與 HVSL。

最終篇將不再新增另一個獨立模組，而是回答：

> 當意圖、結構、算子、Agent、世界與人類治理形成同一閉環時，程式語言與程式文明的基本單位變成了什麼？

---

# 二十五、本文的十五項命題

1. $\text{Visible Output}\neq\text{Human-Visible State}$ 。
2. 終端機、Console、IDE 與原始 log 可以是證據來源，但不能是唯一使用者介面。
3. 人類可見狀態必須由權威 Runtime 與 World State 投影，而不是由模型自由敘事。
4. 每個完成宣稱都必須對應目標、限制、世界狀態與驗證證據。
5. 未驗證狀態不得被可讀性包裝成已完成。
6. 權限擴張、不可逆效果與人類保留決策不得被摘要省略。
7. 透明需要證據下鑽，而不只是更多文字。
8. 大量原始資料不等於有效透明。
9. 解釋應區分目的、計畫、權限、因果、證據與反事實。
10. 可逆治理不等於完美倒帶，而是提供真實可用的控制、補救與接管能力。
11. Diff-first Review 應包含意圖、任務、能力、權限、行動、世界、政策與證據差分。
12. Agent Semantic Pad 應同時提供執行與質疑、驗證、暫停、分支及回復操作。
13. HVSL 必須兼顧透明、隱私、最小揭露與多主體權利。
14. 使用者理解與確認狀態所花費的時間是自動化系統的實際成本。
15. 
$$
\boxed{
\text{Human Governance}
=
\text{Visibility}
+
\text{Evidence}
+
\text{Contestability}
+
\text{Control}
+
\text{Recovery}
}
$$

---

# 二十六、結論：透明不是解釋，而是人類仍具有改變系統的力量

Agent 可以說得非常清楚，卻不一定真的透明。

它可能：

- 解釋事後合理化的理由；
- 省略高風險權限；
- 用流暢語言掩蓋未驗證；
- 顯示停止按鈕，但實際已不可中止；
- 提供回復選項，但沒有真正補償能力。

因此，透明不能只由模型的語言品質衡量。

真正的人類可見狀態要求：

$$
\boxed{
\text{權威狀態}
\rightarrow
\text{可追溯投影}
\rightarrow
\text{證據下鑽}
\rightarrow
\text{人類判斷}
\rightarrow
\text{治理控制}
}
$$

人類不必理解每一個底層細節，但必須知道：

- 系統相信自己在做什麼；
- 它實際做了什麼；
- 它依據什麼權限；
- 世界發生了什麼改變；
- 哪些結論已被證明；
- 哪些仍不確定；
- 誰受影響；
- 哪些效果不可逆；
- 自己現在能採取什麼行動。

本文的最終命題是：

$$
\boxed{
\text{沒有可見狀態，就沒有真正協作。}
}
$$

更進一步：

$$
\boxed{
\text{沒有證據、反駁、停止與回復能力，}
}
$$

$$
\boxed{
\text{所謂透明只是一種更友善的黑箱。}
}
$$

第十一篇至此完成。下一篇將完成整個系列，統一意圖、語言、結構、算子、Agent、世界與人類治理，正式提出「意圖程式文明」的完整架構。

---

# 附錄 A：HVSL 狀態物件

```yaml
hvsl_state:
  view_id: "hvsl-run-001"
  authority_snapshot: "sha256:..."
  generated_at: "2026-07-25T22:00:00+08:00"

intent:
  version: "1.2.0"
  goal: "建立可審核網站版本"
  non_goals:
    - "不部署正式環境"
  drift: "none"

run:
  status: "waiting-human"
  current_task: "review preview"
  progress_basis: "task_graph"
  completed_tasks: 4
  total_tasks: 5

authorization:
  used:
    - "feature_branch:write"
    - "preview:deploy"
  denied:
    - "production:deploy"

world_delta:
  created:
    - "feature branch"
    - "preview deployment"
  modified:
    - "4 files"
  protected:
    - "production unchanged"

verification:
  confirmed:
    - "unit tests"
    - "integration tests"
  unverified:
    - "mobile visual review"

human_decisions:
  - id: "release-approval"
    status: "pending"

controls:
  - "approve"
  - "request_changes"
  - "pause"
  - "cancel"
  - "view_semantic_diff"
  - "view_raw_evidence"
```

---

# 附錄 B：Claim–Evidence Link

```yaml
claim:
  claim_id: "claim-tests-passed"
  text: "自動測試已通過"
  claim_type: "verification"
  status: "confirmed"

evidence:
  receipts:
    - "verify-unit-001"
    - "verify-integration-001"
  raw_artifacts:
    - "artifact://pytest-report.xml"
  subject_hash: "sha256:..."

explanation:
  generated_by: "hvsl-renderer@0.1"
  direct_or_inferred: "direct"
  uncertainty: 0.0
```

---

# 附錄 C：可逆治理物件

```yaml
governance_controls:
  run_id: "run-001"
  state: "waiting-human"

available:
  pause:
    effect: "prevent future actions"
    preserves_continuation: true

  cancel:
    effect: "terminate pending tasks"
    affects_committed_world_state: false

  rollback:
    available: true
    scope:
      - "feature branch commit"
    limitations:
      - "preview access logs remain"

  compensate:
    available: true
    capability: "delete_preview_deployment"

  takeover:
    available: true
    effect: "agent enters suspended mode"
```

---

# 附錄 D：稽核包索引

```yaml
audit_package:
  package_id: "audit-run-001"
  format_version: "0.1"

index:
  intent_ir: "intent.yaml"
  task_ir: "tasks.yaml"
  capability_ir: "capabilities.yaml"
  action_ir: "actions/"
  authorization: "authority/"
  tool_results: "tool-results/"
  verification: "verification/"
  world_deltas: "world-deltas/"
  events: "events/"
  governance: "governance/"
  summary: "human-summary.md"

integrity:
  manifest_hash: "sha256:..."
  signed_by: "runtime-governance-root"
  replay_supported: true
```

---

# 附錄 E：系列十二篇位置

1. 從程式碼到意圖：程式概念的歷史轉換與後文本時代
2. 自然語言原生計算：從語句生成到語義狀態轉換
3. 形式化壓縮與算子演化：自然語言、形式語言與計算結構的生成
4. 語意附加程式設計：EML 與宿主中立語義中介層
5. 結構先於文字：Nova 與後文本程式語言本體論
6. 符號作為算子：從靜態字元到可組合計算閉包
7. 意圖中介表示：從自然語言要求到可驗證能力計畫
8. 時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行
9. Agent Runtime：能力規劃、工具調用與可恢復執行
10. 可編譯世界：從程式執行到世界狀態演化
11. **人類可見狀態：意圖程式系統的稽核、解釋與可逆治理**
12. 意圖程式文明：後文本語言、持續 Agent 與可編譯世界的統一理論

---

# 參考文獻

## Neo.K／EveMissLab 理論與規格文件

1. Neo.K，《HVSL：人類可見狀態層——Agent 不得把終端機當成使用者介面》，2026。
2. Neo.K，《Agent Semantic Pad：AI Agent 權限、意圖與語意工作台》，2026。
3. Neo.K，《介面誘導語言機械化猜想》，2026。
4. Neo.K，《虛擬語義控制面板技術白皮書》，2026。
5. Neo.K，《語義合法性橋接》，2026。
6. Neo.K，《動態思維工作場技術白皮書》，2026。
7. Neo.K，《Noesis Studio／NOEMA AgentOS Human Cockpit》，2026。
8. Neo.K，《PHOSPHOR Observatory》，2026。
9. Neo.K with Aletheia，《Agent Runtime：能力規劃、工具調用與可恢復執行》，2026。
10. Neo.K with Aletheia，《可編譯世界：從程式執行到世界狀態演化》，2026。

## 一般理論背景

11. Norman, D. A., *The Design of Everyday Things*, 1988.
12. Shneiderman, B., *Designing the User Interface*, 1987.
13. Endsley, M. R., “Toward a Theory of Situation Awareness in Dynamic Systems,” 1995.
14. Weick, K. E., *Sensemaking in Organizations*, 1995.
15. Parasuraman, R. and Riley, V., “Humans and Automation: Use, Misuse, Disuse, Abuse,” 1997.
16. Hollnagel, E., Woods, D. D., and Leveson, N., *Resilience Engineering*, 2006.
17. Doshi-Velez, F. and Kim, B., “Towards a Rigorous Science of Interpretable Machine Learning,” 2017.
18. Miller, T., “Explanation in Artificial Intelligence: Insights from the Social Sciences,” 2019.

---

# 版本紀錄

## v0.1 — 2026-07-25

- 完成系列第十一篇。
- 將 HVSL 從介面方法論提升為正式治理投影層。
- 建立 HVSL 十一元模型與四層狀態翻譯。
- 建立十一類治理視圖。
- 提出七項可見性不變量。
- 形式化不可見性債。
- 建立六層證據梯與 Claim–Evidence Link。
- 區分六種解釋並分析解釋性風險。
- 建立九類可逆治理控制與六級可逆性。
- 建立 Diff-first Review 多層差分架構。
- 納入 Agent Semantic Pad 與人類控制語言。
- 建立時間線、因果圖、世界可見狀態與多主體透明。
- 加入無障礙、認知負荷與可攜稽核包。
- 提出十五類失敗模式與十二項可證偽研究基準。
- 銜接最終統一篇。
