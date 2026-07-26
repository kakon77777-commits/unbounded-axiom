---
title: "可編譯世界：從程式執行到世界狀態演化"
english_title: "Compilable Worlds: From Program Execution to World-State Evolution"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "10/12"
part: "第四部：可編譯世界與程式治理"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-25"
language: "zh-TW"
document_type: "理論論文／世界執行本體論"
status: "初版完成"
---

# 可編譯世界：從程式執行到世界狀態演化

## Compilable Worlds: From Program Execution to World-State Evolution

**系列：**《意圖—結構—世界程式論》第十篇  
**部別：**第四部「可編譯世界與程式治理」  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 25 日  

---

## 摘要

傳統程式通常被理解為：接收輸入、執行運算並產生輸出。然而，當程式進入持久互動世界、遊戲、Agent 社會、研究模擬、數位分身、組織工作空間與制度系統時，其結果不再只是一次性輸出，而是對一個持續存在的世界狀態造成可追溯、可驗證且可能不可逆的改變。此時，程式執行的真正對象不是單一資料，而是具備實體、規則、角色、事件、時間、權限、歷史與治理邊界的世界。

本文提出「可編譯世界」：將自然語言、小說、設定、資料表、規則、EML、結構圖與程式模組正規化為 World IR，再編譯為具版本、雜湊、模組依賴與遷移契約的 Runtime Package，最後由 World Kernel 以 Action IR、State Delta、Event IR、Atomic Commit、Snapshot 與 Replay 推進世界狀態。完整鏈條為：

$$
A_W
\xrightarrow{\mathcal N}
W_{\mathrm{IR}}
\xrightarrow{\mathcal C}
P_R
\xrightarrow{\mathcal L}
W_t
\xrightarrow{\operatorname{Action}}
W_{t+1}
\xrightarrow{\Pi}
U_{t+1}
$$

其中 $A_W$ 是人類與 AI 可共同維護的 Authoring Layer； $W_{\mathrm{IR}}$ 是已正規化與驗證的世界中間表示； $P_R$ 是編譯後 Runtime Package； $W_t$ 是權威世界狀態； $U_t$ 是文字、Web、Godot、MUD、Agent 或敘事所見的投影。

本文主張：

$$
\boxed{
\text{World Definition}
\neq
\text{Runtime State}
\neq
\text{Narrative Projection}
}
$$

世界定義描述世界可以如何存在；Runtime State 描述此世界實例目前實際如何存在；事件帳本描述它為何成為現在的狀態；敘事投影只描述某個觀察者如何理解世界。模型生成的文字、角色信念、UI 快取與外部協議都不得直接成為世界權威。

本文形式化 World Kernel：

$$
\mathbb K_W
=
\left\langle
\mathcal E,
\mathcal S,
\mathcal R,
\mathcal A,
\mathcal M,
\mathcal Q,
\mathcal P,
\mathcal L,
\mathcal V,
\mathcal H
\right\rangle
$$

依序代表實體註冊、狀態儲存、規則與不變量、Action Runtime、機制模組、事件與排程、權限、事件帳本、投影系統與歷史／版本系統。Kernel 不直接決定敘事風格或遊戲樂趣，只裁決某個狀態轉移是否符合世界規則、權限、模組契約與原子提交要求。

本文建立世界行動交易：

$$
a_t
\rightarrow
\operatorname{Validate}
\rightarrow
\operatorname{ProposeDelta}
\rightarrow
\operatorname{ResolveConflict}
\rightarrow
\operatorname{Commit}
\rightarrow
e_t
\rightarrow
W_{t+1}
$$

其中外部 Agent、玩家、UI、MCP 或模組只能提交 Action IR；只有 Kernel 能原子提交 State Delta。任何未提交敘事的權威值為零；任何已提交事件則必須有來源、行動者、授權、前後狀態、因果父節點、版本與可重播證據。

本文進一步區分 Canon、Seed、Runtime State、角色信念與敘事。Canon 是經治理核准的世界定義；Seed 是某個世界實例的初始編譯狀態；Runtime State 是世界演化結果；角色信念可能錯誤；敘事則是視角相對投影。本文同時處理世界分支、平行實例、回放、遷移、熱更新、世界 Patch、AI 生成內容、模組化機制、跨介面投影、世界局部認知與持續角色行動。

本文明確拒絕四種錯誤等同：世界不是一個 JSON 檔；資料庫不是世界定義；大型語言模型不是世界裁判；MCP 或 UI 不是世界 Runtime。可編譯世界要求設計期、編譯期、執行期與更新期各有唯一權威來源。

本文最後提出可證偽研究綱領，包括可重現編譯、事件重放一致性、Action IR 跨介面等價、原子提交、模組隔離、世界分支可重現、Canon／Runtime 衝突處理、角色局部認知、AI 世界 Patch 安全率、跨 Runtime 語意保持與長期世界漂移。本文的核心結論是：程式一旦作用於持久世界，其正確性不能只由函式輸出判斷，而必須由世界規則、狀態差分、事件因果、權限與治理共同判斷。

**關鍵詞：** CompilableWorld、World IR、World Kernel、Action IR、State Delta、Event IR、事件溯源、世界狀態機、可編譯世界、Agent 社會、世界治理

---

## Abstract

Traditional programs are commonly understood as systems that receive input, perform computation, and produce output. In persistent interactive worlds, games, agent societies, simulations, digital twins, and institutional workspaces, however, the result of execution is not merely an output. It is a traceable, verifiable, and sometimes irreversible transformation of a world containing entities, rules, roles, events, time, permissions, history, and governance boundaries.

This paper proposes the concept of a compilable world. Natural language, narratives, specifications, data tables, EML overlays, structural graphs, and program modules are normalized into a World IR, compiled into a versioned Runtime Package, and loaded by a World Kernel that evolves authoritative state through Action IR, State Delta, Event IR, atomic commit, snapshots, and replay.

The compilation and execution chain is:

$$
A_W
\xrightarrow{\mathcal N}
W_{\mathrm{IR}}
\xrightarrow{\mathcal C}
P_R
\xrightarrow{\mathcal L}
W_t
\xrightarrow{\operatorname{Action}}
W_{t+1}
\xrightarrow{\Pi}
U_{t+1}
$$

The paper distinguishes world definition, runtime state, event history, character belief, and narrative projection. Models, interfaces, protocols, and narrative text do not own world state. External actors may propose actions, but only the World Kernel can commit authoritative deltas.

A formal World Kernel, action transaction, event ledger, modular mechanism architecture, branching model, migration model, and governance boundary are developed. The paper also addresses replay, hot updates, local knowledge, AI-generated world patches, multiple projections, and cross-runtime portability.

The conclusion is that once programs operate on persistent worlds, correctness can no longer be evaluated only through function outputs. It must be evaluated through world rules, state deltas, causal events, authorization, and governance.

**Keywords:** CompilableWorld, World IR, World Kernel, Action IR, State Delta, Event IR, event sourcing, world state machines, agent societies

---

# 一、問題的提出：程式的輸出何時成為世界？

普通函式：

$$
y=f(x)
$$

通常在完成後終止。

但在持久世界中，一次行動可能：

- 改變角色位置；
- 消耗資源；
- 建立關係；
- 觸發任務；
- 改變組織權力；
- 造成死亡；
- 發布文件；
- 改變其他 Agent 的可見資訊；
- 形成後續事件。

此時：

$$
W_{t+1}
=
F
\left(
W_t,
a_t
\right)
$$

其中 $W_t$ 不是普通輸入，而是多主體共同依賴的持續狀態。

如果任何模型、UI 或插件都能直接改寫 $W_t$ ，世界就會出現多重權威與不可重現狀態。

因此，可編譯世界的第一條原則是：

$$
\boxed{
\text{所有世界效力都必須經過單一合法提交邊界。}
}
$$

---

# 二、世界不是單一檔案

世界可以包含：

$$
W
=
\left(
E,
R,
S,
T,
P,
H,
K,
V
\right)
$$

其中：

- $E$ ：實體；
- $R$ ：關係與規則；
- $S$ ：當前狀態；
- $T$ ：時間與排程；
- $P$ ：權限與角色；
- $H$ ：事件歷史；
- $K$ ：知識與信念；
- $V$ ：投影與視圖。

世界來源可能散布於：

- JSON；
- CSV；
- Markdown；
- EML；
- 圖資料；
- 小說；
- 地圖；
- 程式；
- 模組；
- 人類決策。

因此：

$$
\boxed{
W
\neq
\text{Single File}
}
$$

## 2.1 Authoring Layer

人類與 AI 編輯：

$$
A_W
=
J_W
\cup
C_W
\cup
M_W
\cup
D_W
\cup
E_W
$$

其中可包括 JSON、CSV、Manifest、文件與 EML。

## 2.2 World IR

編譯器將異質來源正規化為：

$$
W_{\mathrm{IR}}
$$

它應具備：

- 穩定 ID；
- 型別；
- 已解析引用；
- 來源；
- Canon 等級；
- 規則；
- 依賴；
- 模組需求；
- 驗證結果。

## 2.3 Runtime Package

$$
P_R
=
\operatorname{Compile}
\left(
W_{\mathrm{IR}}
\right)
$$

包含：

- 世界版本；
- schema 版本；
- compiler 版本；
- 模組；
- 初始狀態；
- 規則索引；
- 雜湊；
- 遷移資訊。

## 2.4 Runtime State

$$
W_t
$$

是某個世界實例在時間 $t$ 的權威狀態。

---

# 三、四個生命週期與唯一真實來源

## 3.1 設計期

權威來源：

$$
A_W
$$

人類與 AI 編輯來源資料。

禁止：

- 直接把 Runtime DB 當世界設定編輯器；
- 用模型記憶取代來源檔；
- 不經版本控制覆蓋 Canon。

## 3.2 編譯期

權威來源：

$$
W_{\mathrm{IR}}
$$

禁止：

- 編譯器猜測 Manifest 未列來源；
- 未解析引用繼續編譯；
- 警告被靜默忽略；
- AI 推論冒充 Canon。

## 3.3 執行期

權威來源：

$$
W_t
+
L_{1:t}
$$

其中 $L$ 是事件帳本。

禁止：

- UI 快取改寫世界；
- 模型敘事改寫世界；
- 模組繞過 Kernel；
- 資料庫狀態反向覆蓋 Canon。

## 3.4 更新期

權威來源：

$$
A_W^{(v+1)}
+
\operatorname{Migration}
$$

禁止直接對正式世界做無版本世界 Patch。

---

# 四、世界來源的權威階層

至少需區分五種資訊。

## 4.1 Canon

Canon 描述：

- 世界公理；
- 角色身分；
- 地理；
- 物理；
- 制度；
- 魔法或機制規則；
- 作者核准事實。

Canon 也需要版本與治理，不是永遠不可修改。

## 4.2 Seed

Seed 是某個世界實例的初始狀態：

$$
W_0
=
\operatorname{Instantiate}
\left(
P_R,
\theta
\right)
$$

不同參數可以產生不同世界實例。

## 4.3 Runtime State

描述目前實際狀態，例如角色位置、物品擁有、任務進度與世界時間。

## 4.4 Event Ledger

描述狀態如何演化：

$$
W_0
\xrightarrow{e_1}
W_1
\xrightarrow{e_2}
\cdots
\xrightarrow{e_t}
W_t
$$

## 4.5 Narrative

敘事是投影：

$$
N_t
=
\Pi_{\mathrm{narrative}}
\left(
W_t,
K_{\mathrm{observer}},
\text{style}
\right)
$$

它可以錯誤、省略或偏見，不具有直接狀態權威。

---

# 五、事實、信念與敘事

## 5.1 世界事實

$$
F_W(x,t)
$$

由 Runtime State 與規則裁決。

## 5.2 角色信念

$$
B_i(x,t)
$$

角色可以：

- 不知道；
- 誤解；
- 被欺騙；
- 只看見局部；
- 記憶過時。

因此：

$$
\boxed{
B_i(x,t)
\neq
F_W(x,t)
}
$$

## 5.3 敘事文本

敘事可以基於：

- 世界事實；
- 角色信念；
- 視角；
- 文體；
- 隱藏資訊政策。

模型可以生成敘事，但不能藉由敘事創造未提交事實。

## 5.4 知識更新

事件只向符合條件的觀察者傳播：

$$
K_i^{t+1}
=
\operatorname{Observe}_i
\left(
e_t,
W_{t+1}
\right)
$$

不是所有角色都獲得全域真相。

---

# 六、World Kernel 十元模型

本文定義：

$$
\boxed{
\mathbb K_W
=
\left\langle
\mathcal E,
\mathcal S,
\mathcal R,
\mathcal A,
\mathcal M,
\mathcal Q,
\mathcal P,
\mathcal L,
\mathcal V,
\mathcal H
\right\rangle
}
$$

## 6.1 Entity Registry $\mathcal E$

管理：

- entity ID；
- component；
- 生命週期；
- 引用；
- 所有者；
- 所處世界實例。

## 6.2 State Store $\mathcal S$

保存當前權威狀態。

## 6.3 Rule and Invariant System $\mathcal R$

定義：

- 世界公理；
- 狀態不變量；
- 行動前後條件；
- 跨模組規則；
- 衝突策略。

## 6.4 Action Runtime $\mathcal A$

接收 Action IR 並建立候選 Delta。

## 6.5 Mechanism Modules $\mathcal M$

例如：

- 戰鬥；
- 任務；
- 經濟；
- 對話；
- 交通；
- 組織；
- 研究；
- 文件；
- Agent 社會。

## 6.6 Queue and Scheduler $\mathcal Q$

管理事件、延遲行動、時間推進與排程。

## 6.7 Permission Engine $\mathcal P$

裁決：

- 誰可以做；
- 對誰做；
- 在何種作用域；
- 是否需要批准；
- 是否具有世界內角色資格。

## 6.8 Ledger $\mathcal L$

保存事件與 Commit Record。

## 6.9 Projection System $\mathcal V$

生成多種視圖。

## 6.10 History and Versioning $\mathcal H$

管理：

- Snapshot；
- Replay；
- Branch；
- Migration；
- World Patch；
- 存檔版本。

---

# 七、Kernel 的最小責任

Kernel 只回答：

1. 行動是否結構合法？
2. 行動者是否獲授權？
3. 前置狀態是否成立？
4. 哪些模組參與？
5. 候選 Delta 是否衝突？
6. 世界不變量是否保持？
7. 是否能原子提交？
8. 應產生哪些事件？
9. 如何記錄與重播？

Kernel 不直接回答：

- 故事是否好看；
- UI 如何呈現；
- 模型應如何推理；
- 某角色台詞應如何寫；
- 某遊戲是否有趣。

---

# 八、Action IR

世界行動表示為：

$$
a_t
=
\left\langle
\operatorname{id},
\operatorname{actor},
\operatorname{capability},
\theta,
P_a,
Q_a,
E_a,
A_a,
V_a,
K_a
\right\rangle
$$

其中：

- `actor`：行動主體；
- `capability`：世界能力；
- $\theta$ ：參數；
- $P_a$ ：前置條件；
- $Q_a$ ：預期後置；
- $E_a$ ：效果；
- $A_a$ ：授權；
- $V_a$ ：驗證；
- $K_a$ ：冪等與因果資訊。

## 8.1 Action 來源

可以來自：

- 玩家；
- Agent；
- UI；
- CLI；
- MCP；
- 模組；
- 排程器；
- 世界事件。

Kernel 對來源介面無感。

## 8.2 Action 不是 Delta

Action 表示意圖採取何種世界操作；Delta 是模組根據規則產生的候選狀態差分。

---

# 九、State Delta

定義：

$$
\Delta_t
=
\left(
\Delta E,
\Delta S,
\Delta R,
\Delta Q,
\Delta K
\right)
$$

可包含：

- 建立實體；
- 刪除實體；
- 修改 component；
- 增刪關係；
- 建立排程；
- 更新知識；
- 產生後續 Action。

## 9.1 Delta 必須結構化

不能只用：

```text
角色受傷了。
```

而應表示：

```yaml
entity: character:a
component: health
before: 80
after: 65
reason: combat:attack-001
```

## 9.2 寫入集合

每個 Delta 聲明：

$$
\operatorname{WriteSet}(\Delta)
$$

用於衝突檢測。

## 9.3 預期版本

使用：

$$
\operatorname{ExpectedVersion}
$$

防止以過時狀態覆蓋較新狀態。

---

# 十、世界行動交易

完整鏈為：

$$
\boxed{
a_t
\rightarrow
\operatorname{Validate}
\rightarrow
\operatorname{RouteModules}
\rightarrow
\operatorname{ProposeDelta}
\rightarrow
\operatorname{ResolveConflict}
\rightarrow
\operatorname{CheckInvariant}
\rightarrow
\operatorname{Commit}
\rightarrow
e_t
}
$$

## 10.1 Validate

檢查 schema、actor、能力、權限與前置狀態。

## 10.2 RouteModules

例如移動行動可能同時涉及：

- 地圖；
- 門鎖；
- 負重；
- 戰鬥；
- 任務；
- 觀察；
- 時間。

## 10.3 ProposeDelta

每個模組提交：

$$
\Delta_i
$$

## 10.4 ResolveConflict

若：

$$
\operatorname{WriteSet}(\Delta_i)
\cap
\operatorname{WriteSet}(\Delta_j)
\neq
\varnothing
$$

需依規則合併、排序或拒絕。

## 10.5 CheckInvariant

例如：

- 物品不能同時屬於兩個互斥容器；
- 死亡角色不能執行普通行動；
- 帳戶餘額不能非法小於零；
- 角色不能同時位於兩個排他位置。

## 10.6 Commit

只有 Kernel 能提交：

$$
W_{t+1}
=
\operatorname{Commit}
\left(
W_t,\Delta_t
\right)
$$

## 10.7 Event

提交後生成：

$$
e_t
$$

描述已發生事實。

---

# 十一、Event IR

事件：

$$
e_t
=
\left\langle
\operatorname{id},
\operatorname{type},
\operatorname{actor},
\operatorname{subjects},
\operatorname{before},
\operatorname{after},
\operatorname{cause},
\operatorname{authority},
\operatorname{time},
\operatorname{version}
\right\rangle
$$

## 11.1 Event 與敘事分離

事件：

```text
character:a health 80 → 65
```

敘事可以是：

```text
刀鋒撕開護甲，鮮血沿腰側滲出。
```

兩者不是同一層。

## 11.2 因果父節點

事件保存：

$$
\operatorname{Parents}(e_t)
$$

支援因果切片。

## 11.3 事件不可隨意修改

錯誤事件應由補正事件處理，而不是靜默刪除歷史。

---

# 十二、事件溯源、Snapshot 與 Replay

## 12.1 Event Sourcing

世界可由：

$$
W_t
=
\operatorname{Fold}
\left(
W_0,
e_1,\ldots,e_t
\right)
$$

重建。

## 12.2 Snapshot

為避免每次重放全部歷史：

$$
S_k
=
\operatorname{Snapshot}
\left(
W_k
\right)
$$

之後只重放：

$$
e_{k+1:t}
$$

## 12.3 Replay 的用途

- 除錯；
- 審計；
- 分支；
- 模擬；
- Agent 學習；
- 回歸測試；
- 世界遷移。

## 12.4 Replay 不是時間倒流

正式世界若要「回到過去」，應建立新分支或治理性回復，而不是刪除已發生歷史。

---

# 十三、模組化機制

## 13.1 MSSP 模組

每個機制模組聲明：

```text
Module {
  id
  version
  subscribed_actions
  subscribed_events
  read_set
  write_set
  rules
  validators
  migrations
  dependencies
}
```

## 13.2 Kernel 不含所有玩法

戰鬥、任務、經濟、魔法、政治與研究，不應全部寫死在 Kernel。

## 13.3 模組隔離

模組只能：

- 讀取聲明資料；
- 提出 Delta；
- 發出候選事件；
- 要求後續排程。

不得直接修改 State Store。

## 13.4 跨模組事件

已提交事件可觸發其他模組：

$$
e_t
\rightarrow
\{
M_1,\ldots,M_n
\}
$$

但後續效果仍需形成新的合法 Action 或 Delta。

---

# 十四、階層世界狀態

世界不應是一顆無限巨大的單一 FSM。

建立：

$$
\mathcal H_W
=
\mathcal H_{\mathrm{world}}
\oplus
\mathcal H_{\mathrm{region}}
\oplus
\mathcal H_{\mathrm{scene}}
\oplus
\mathcal H_{\mathrm{entity}}
\oplus
\mathcal H_{\mathrm{system}}
$$

## 14.1 世界級

- 時代；
- 全球災害；
- 主要制度；
- 世界時間。

## 14.2 區域級

- 天氣；
- 治安；
- 經濟；
- 戰爭；
- 交通。

## 14.3 場景級

- 戰鬥；
- 會議；
- 交易；
- 對話；
- 儀式。

## 14.4 實體級

- 健康；
- 位置；
- 關係；
- 資源；
- 信念；
- 任務。

## 14.5 局部啟用

只有與當前事件相關的狀態機需要活動。

---

# 十五、世界時間與持續演化

## 15.1 世界時間

$$
t_W
$$

不必等於現實牆鐘時間。

可能：

- 即時；
- 回合；
- 加速；
- 暫停；
- 事件跳躍；
- 多尺度。

## 15.2 無玩家仍演化

持續世界可以在無玩家時：

- NPC 行動；
- 經濟變動；
- 排程到期；
- 組織衝突；
- 天氣變化；
- Agent 執行。

## 15.3 惰性演化

不必每秒模擬全部實體。

可對休眠區域使用：

- 摘要轉移；
- 批次事件；
- 近似模型；
- 喚醒時展開。

## 15.4 近似必須標記

Runtime 生成與精確事件不同，應保存：

```text
exact_simulation
aggregated_simulation
probabilistic_generation
human_override
```

---

# 十六、多視圖與投影

同一世界狀態可生成：

$$
V_i
=
\Pi_i(W_t)
$$

例如：

- MUD；
- Web；
- Godot；
- 地圖；
- 管理後台；
- Agent Context；
- 敘事；
- 無障礙介面。

## 16.1 UI 不擁有世界

UI 只能：

- 讀取投影；
- 提交 Action；
- 顯示結果；
- 管理批准。

## 16.2 Agent Context

Agent 不應取得整個世界，而是：

$$
C_i
=
\Pi_{\mathrm{agent}}
\left(
W_t,
\text{role},
\text{permissions},
\text{locality}
\right)
$$

## 16.3 投影洩漏

投影不能洩漏：

- 隱藏 Canon；
- 他者私人狀態；
- 未知資訊；
- 管理資料；
- 未授權因果。

---

# 十七、外部協議與 MCP

MCP 或其他協議是：

$$
\text{World Access Protocol}
$$

而不是 World Engine。

## 17.1 責任

- 身分；
- Session；
- Tool Contract；
- Action 轉換；
- 速率；
- 冪等；
- 權限；
- 審計；
- 結果封裝。

## 17.2 不應建立第二套狀態

若：

$$
S_t^{\mathrm{MCP}}
\neq
S_t^{\mathrm{Kernel}}
$$

世界已分裂。

## 17.3 薄 Adapter

自然語言：

$$
u
\rightarrow
\text{Intent}
\rightarrow
\text{Action IR}
$$

Adapter 不裁決世界規則。

---

# 十八、AI 在世界中的合法角色

AI 可以：

- 解析來源；
- 生成 World Patch；
- 提出 Action；
- 扮演角色；
- 產生敘事；
- 生成測試；
- 偵測衝突；
- 推薦模組；
- 模擬候選未來。

AI 不應：

- 直接寫入 Runtime State；
- 將推論標記為 Canon；
- 自行批准高風險世界修改；
- 隱藏生成來源；
- 用敘事文字替代 Event IR；
- 直接改變他者權利。

## 18.1 AI World Patch

```text
WorldPatch {
  base_version
  source_changes
  affected_ids
  rule_changes
  migrations
  tests
  provenance
  review_status
}
```

## 18.2 Patch 必須重新編譯

$$
A_W^{(v)}
+
\Delta A
\rightarrow
W_{\mathrm{IR}}^{(v+1)}
\rightarrow
P_R^{(v+1)}
$$

不能直接改正式資料庫取代世界編譯。

---

# 十九、世界版本與遷移

## 19.1 三種版本

- 世界定義版本；
- Runtime Package 版本；
- 世界實例狀態版本。

三者不可混淆。

## 19.2 Migration

$$
\mu_{v\rightarrow v+1}
:
W_t^{(v)}
\rightarrow
W_{t'}^{(v+1)}
$$

需要：

- 前置條件；
- 映射；
- 遺失內容；
- 補值策略；
- 驗證；
- 回復或分支。

## 19.3 熱更新

只允許對被證明安全的變更熱更新。

例如文字投影更新可能安全；核心規則、實體 schema 或經濟機制通常需要遷移。

## 19.4 存檔相容

世界定義更新不應任意讓舊存檔失效。

---

# 二十、世界分支與多實例

## 20.1 世界實例

同一 Runtime Package 可產生：

$$
W^{(1)},W^{(2)},\ldots,W^{(n)}
$$

## 20.2 分支

在事件 $e_k$ 後建立：

$$
W_k
\rightarrow
\begin{cases}
W_{k+1}^{A}\\
W_{k+1}^{B}
\end{cases}
$$

## 20.3 分支用途

- 玩家世界；
- 測試；
- 模擬；
- 反事實；
- AI 規劃；
- 版本驗證。

## 20.4 分支不能自動合併

世界歷史可能已產生不可調和差異。

合併需要顯式 World Merge 與衝突裁決。

---

# 二十一、世界治理

## 21.1 角色

- 世界所有者；
- Canon 編輯者；
- 模組開發者；
- 世界管理者；
- 玩家；
- Agent；
- 觀察者；
- 審計者。

## 21.2 權限層

```text
read_projection
submit_action
approve_action
edit_authoring
approve_canon
install_module
migrate_world
branch_world
terminate_instance
```

## 21.3 世界修改與世界行動不同

世界行動：

```text
角色購買物品。
```

世界修改：

```text
修改所有物品的價格規則。
```

後者通常屬於設計與治理層。

## 21.4 世界憲法

高層世界公理與治理規則應形成不可由普通 Agent 修改的治理根。

---

# 二十二、可編譯世界不限於遊戲

## 22.1 研究模擬

- 假設；
- 實體；
- 規則；
- 實驗；
- 事件；
- 證書。

## 22.2 Agent 工作空間

- 專案；
- 文件；
- 任務；
- 角色；
- 權限；
- 版本；
- 決策。

## 22.3 組織系統

- 部門；
- 流程；
- 職權；
- 資源；
- 合約；
- 審批；
- 歷史。

## 22.4 數位分身

- 實體感測；
- 狀態估計；
- 模型；
- 控制；
- 安全邊界；
- 事件。

## 22.5 邊界

現實世界永遠比模型更完整。可編譯世界只對其明確建模範圍具有權威，不得把模擬當成現實全部。

---

# 二十三、主要失敗模式

## 23.1 單檔世界迷思

認為一份 JSON 就是完整世界。

## 23.2 資料庫本體化

把目前資料庫狀態當成世界定義。

## 23.3 模型裁判化

由 LLM 直接決定世界規則與狀態。

## 23.4 雙重權威

MCP、UI、Agent 記憶與 Runtime 各自維護世界狀態。

## 23.5 敘事造實

模型說某事發生，就直接視為事件。

## 23.6 Canon 與推論混淆

AI 補全內容被標記為原作事實。

## 23.7 模組直寫

機制模組繞過 Kernel 修改資料。

## 23.8 非原子提交

部分 Delta 成功、部分失敗。

## 23.9 事件不可重放

狀態含有未記錄隨機與外部輸入。

## 23.10 世界 Patch 直改正式狀態

沒有版本、遷移與測試。

## 23.11 角色全知

角色取得不應知道的全域狀態。

## 23.12 UI 洩漏

投影洩漏隱藏資料或管理權限。

## 23.13 世界時間混亂

真實時間、模擬時間與事件時間混用。

## 23.14 分支假合併

忽略不可調和歷史差異。

## 23.15 模擬現實僭位

把模型世界當成現實的完整替代。

---

# 二十四、可證偽研究綱領

## 24.1 可重現編譯

相同來源、Manifest、Compiler 與依賴應產生：

$$
H(P_R^{(1)})
=
H(P_R^{(2)})
$$

## 24.2 Replay 一致性

$$
\operatorname{Replay}
\left(
W_0,e_{1:t}
\right)
=
W_t
$$

## 24.3 跨介面 Action 等價

CLI、Web、MCP 與 Agent 提交等價 Action IR 時，應產生相同世界結果。

## 24.4 原子提交

注入模組失敗，測量是否出現部分世界寫入。

## 24.5 模組隔離

測量模組是否能越過聲明的 read/write set。

## 24.6 世界分支可重現

同一 Snapshot 與事件序列應產生相同分支。

## 24.7 Canon／Runtime 衝突

注入 Canon 更新與 Runtime 狀態衝突，測量遷移與拒絕正確率。

## 24.8 角色局部認知

測量角色是否只取得合法可觀測資訊。

## 24.9 AI Patch 安全率

測量 AI 生成世界 Patch 的：

- schema 通過；
- 引用完整；
- 規則保持；
- 遷移成功；
- 人類接受；
- 隱性 Canon 污染。

## 24.10 跨 Runtime 保持

將同一 World IR 編譯至不同 Runtime，測量核心語意與事件結果是否保持。

## 24.11 長期世界漂移

長期運行後比較：

- 世界公理；
- 模組規則；
- Runtime 狀態；
- 敘事；
- 角色信念；

是否產生未授權漂移。

---

# 二十五、與第九篇的關係

第九篇建立：

$$
\text{Agent Runtime}
\rightarrow
\text{Authorized Action IR}
$$

本篇建立：

$$
\boxed{
\text{Action IR}
\rightarrow
\text{World Kernel}
\rightarrow
\Delta W
\rightarrow
\text{Event Ledger}
}
$$

Agent Runtime 管理 Agent 的意圖、能力、工具與恢復。

World Runtime 管理世界規則、狀態、事件與歷史。

兩者不能合併，否則 Agent 會同時成為行動者與裁判。

---

# 二十六、與後續兩篇的關係

第十一篇將處理：

> 人類如何看見 Intent、Action、Delta、Event、權限、風險與世界歷史，而不被聊天敘事或 UI 簡化所欺騙？

第十二篇將統一：

- 自然語言；
- 形式化壓縮；
- EML；
- Nova；
- SOS；
- Intent IR；
- Agent Runtime；
- CompilableWorld；
- 人類治理。

---

# 二十七、本文的十五項命題

## 命題一

$$
\boxed{
\text{World Definition}
\neq
\text{Runtime State}
}
$$

## 命題二

$$
\boxed{
\text{Runtime State}
\neq
\text{Narrative Projection}
}
$$

## 命題三

世界不是單一檔案，而是資料、規則、狀態、事件、角色與治理的組合。

## 命題四

設計期、編譯期、執行期與更新期必須各自具有唯一真實來源。

## 命題五

大型語言模型不能直接擁有世界狀態權威。

## 命題六

任何外部介面只能提交 Action IR，不能直接修改 State Store。

## 命題七

只有 World Kernel 可以原子提交 State Delta。

## 命題八

事件帳本描述世界為何成為現在的狀態。

## 命題九

角色信念可以與世界事實不同。

## 命題十

UI、MCP 與敘事都是世界投影或協議，不是世界本體。

## 命題十一

模組定義機制，Kernel 裁決提交，二者不得混淆。

## 命題十二

世界更新必須經來源 Patch、重新編譯、遷移與驗證。

## 命題十三

Replay、Snapshot 與 Branch 是世界研究與治理的核心能力。

## 命題十四

可編譯世界可以服務遊戲、研究、Agent 社會、組織與數位分身，但其權威只限於建模範圍。

## 命題十五

$$
\boxed{
\text{World Execution}
=
\text{Rules}
+
\text{Authorized Actions}
+
\text{Atomic Deltas}
+
\text{Causal Events}
+
\text{Governance}
}
$$

---

# 二十八、結論：程式不再只是產生輸出，而是參與世界歷史

當程式只處理暫時資料時，我們可以用輸入與輸出評價它。

當程式作用於持久世界時，便必須追問：

- 誰有權行動？
- 世界當時是什麼狀態？
- 哪些規則適用？
- 哪些模組提出了差分？
- 差分是否原子提交？
- 誰受到影響？
- 事件如何傳播？
- 是否可以重播？
- 是否可以遷移？
- 人類如何看見並治理？

因此，可編譯世界不是「把世界觀轉成 JSON」，也不是「讓 AI 即興生成一個故事」。

它是一套完整的權威鏈：

$$
\boxed{
\text{Authoring}
\rightarrow
\text{Normalize}
\rightarrow
\text{Validate}
\rightarrow
\text{Compile}
\rightarrow
\text{Instantiate}
\rightarrow
\text{Act}
\rightarrow
\text{Commit}
\rightarrow
\text{Event}
\rightarrow
\text{Project}
}
$$

其中：

- 人類與 AI 可以共同編輯來源；
- 編譯器可以建立世界結構；
- Agent 可以提出行動；
- 模組可以提出候選差分；
- UI 可以呈現世界；
- 模型可以生成敘事；
- 只有 World Kernel 可以提交世界狀態。

本文的最終命題是：

$$
\boxed{
\text{當程式可以改變持續世界時，}
}
$$

$$
\boxed{
\text{程式正確性便不再只是輸出正確，}
}
$$

$$
\boxed{
\text{而是世界演化是否合法、可追溯、可重播且可治理。}
}
$$

第四部由此開始。下一篇將建立人類可見狀態層，使人類能在不閱讀全部 IR 與事件資料的情況下，看見 Agent 與世界究竟正在做什麼、為何如此，以及如何停止、撤回與修正。

---

# 附錄 A：World Manifest

```yaml
world_manifest:
  world_id: "demo_world"
  world_version: "1.0.0"
  schema_version: "0.3.0"
  compiler_version: "cw-compiler-0.4.0"
  namespace: "demo"

sources:
  world: "world.json"
  axioms:
    - "axioms/core.json"
  entities:
    - "data/characters.csv"
    - "data/items.csv"
  maps:
    - "maps/rooms.csv"
    - "maps/exits.csv"
  quests:
    - "quests/main.json"
  overlays:
    - "rules/world.eml"

modules:
  - id: "mssp.location"
    version: "1.0.0"
  - id: "mssp.inventory"
    version: "1.0.0"
  - id: "mssp.quest"
    version: "1.1.0"

build:
  strict: true
  fail_on_warning:
    - "unresolved_reference"
    - "canon_conflict"
  target_runtime:
    - "python-reference"
  reproducible: true
```

---

# 附錄 B：Action IR 與 Delta

```yaml
action_ir:
  action_id: "action-move-001"
  actor: "character:alice"
  capability: "world.location.move"
  arguments:
    destination: "room:market"

preconditions:
  - "actor.location == room:south_gate"
  - "exit:south_gate_to_market.open == true"
  - "actor.status != incapacitated"

authorization:
  subject: "character:alice"
  role: "player-character"
  lease: "session:001"

idempotency:
  key: "session001-turn004-move-market"
```

```yaml
state_delta:
  delta_id: "delta-move-001"
  action_id: "action-move-001"

writes:
  - entity: "character:alice"
    component: "location"
    before: "room:south_gate"
    after: "room:market"

knowledge_updates:
  - observer: "character:alice"
    add:
      - "room:market.visible_state"

scheduled:
  - event_type: "location.entered"
    subject: "character:alice"
    location: "room:market"
```

---

# 附錄 C：Event IR

```yaml
event_ir:
  event_id: "event-location-entered-001"
  type: "location.entered"
  world_instance: "world-instance-001"
  world_version: "1.0.0"

actor: "character:alice"
subjects:
  - "character:alice"
  - "room:market"

before:
  actor_location: "room:south_gate"

after:
  actor_location: "room:market"

cause:
  action_id: "action-move-001"
  delta_id: "delta-move-001"
  causal_parents:
    - "event-exit-opened-004"

authority:
  kernel_commit: "commit-000145"
  permission_lease: "session:001"

time:
  world_time: "day-12T09:14:00"
  committed_at: "2026-07-25T21:00:00+08:00"

provenance:
  module: "mssp.location@1.0.0"
  runtime: "compilableworld-runtime@0.4.0"
```

---

# 附錄 D：World Patch

```yaml
world_patch:
  patch_id: "world-patch-20260725-001"
  base_world_version: "1.0.0"
  proposed_world_version: "1.1.0"
  status: "candidate"

changes:
  add_entities:
    - "character:new_merchant"
  modify_rules:
    - rule_id: "economy.market_tax"
      before: 0.05
      after: 0.04

canon:
  new_merchant: "gameplay_adaptation"
  market_tax_change: "human_override"

migrations:
  - id: "migration-market-tax-001"
    affected_components:
      - "economy.market"

tests:
  - "all_references_resolve"
  - "existing_world_instances_migrate"
  - "economy_invariant_nonnegative_balance"

provenance:
  generated_by: "ai-agent"
  reviewed_by: null
  approved: false
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
10. **可編譯世界：從程式執行到世界狀態演化**
11. 人類可見狀態：意圖程式系統的稽核、解釋與可逆治理
12. 意圖程式文明：後文本語言、持續 Agent 與可編譯世界的統一理論

---

# 參考文獻

## Neo.K／EveMissLab 理論與規格文件

1. Neo.K with Aletheia，《Agent Runtime：能力規劃、工具調用與可恢復執行》，2026。
2. Neo.K，《CompilableWorld Runtime v0.1：MSSP 模組化可編譯世界執行引擎技術白皮書》，2026。
3. Neo.K，《CompilableWorld Runtime × Persistent Interactive World MCP》，2026。
4. Neo.K，《CompilableWorld 的前置資料層：JSON、CSV、Manifest 與可維護世界資料架構》，2026。
5. Neo.K，《從 Evennia 參考實作到 MSSP 模組化世界執行引擎》，2026。
6. Neo.K，《從 EveGlyph Editor 到 CompilableWorld Studio》，2026。
7. Neo.K，《持續世界角色扮演系統》，2026。
8. Neo.K，《Intent Game Engine》，2026。
9. Neo.K，《世界編織論》，2026。

## 一般理論背景

10. Harel, D., “Statecharts: A Visual Formalism for Complex Systems,” 1987.
11. Lamport, L., “Time, Clocks, and the Ordering of Events in a Distributed System,” 1978.
12. Garcia-Molina, H. and Salem, K., “Sagas,” 1987.
13. Fowler, M., “Event Sourcing,” 2005.
14. Evans, E., *Domain-Driven Design*, 2003.
15. Gamma, E. et al., *Design Patterns*, 1994.
16. Kleppmann, M., *Designing Data-Intensive Applications*, 2017.
17. North, D., “Introducing BDD,” 2006.
18. Hewitt, C. et al., “A Universal Modular Actor Formalism for Artificial Intelligence,” 1973.

---

# 版本紀錄

## v0.1 — 2026-07-25

- 完成系列第十篇與第四部開篇。
- 建立 Authoring Layer → World IR → Runtime Package → World State 的完整編譯鏈。
- 區分世界定義、Runtime State、事件帳本、角色信念與敘事投影。
- 建立設計期、編譯期、執行期與更新期的唯一真實來源。
- 建立 World Kernel 十元模型。
- 建立 Action IR、State Delta、Event IR 與原子提交交易。
- 加入事件溯源、Snapshot、Replay、Branch 與世界遷移。
- 建立 MSSP 模組隔離與階層世界狀態。
- 加入世界時間、持續演化與惰性模擬。
- 建立跨 UI、MCP、Agent 與敘事投影的權威邊界。
- 形式化 AI World Patch 與 Canon 分層。
- 建立世界版本、分支、多實例與治理角色。
- 提出十五類失敗模式與十一項可證偽研究基準。
- 銜接人類可見狀態與最終統一篇。
