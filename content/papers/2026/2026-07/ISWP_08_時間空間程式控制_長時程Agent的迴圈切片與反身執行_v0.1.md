---
title: "時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行"
english_title: "Temporal–Spatial Program Control: Loops, Slices, and Reflexive Execution for Long-Horizon Agents"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "08/12"
part: "第三部：意圖編譯與 Agent 執行"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-25"
language: "zh-TW"
document_type: "理論論文／長時程控制架構"
status: "初版完成"
---

# 時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行

## Temporal–Spatial Program Control: Loops, Slices, and Reflexive Execution for Long-Horizon Agents

**系列：**《意圖—結構—世界程式論》第八篇  
**部別：**第三部「意圖編譯與 Agent 執行」  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 25 日  

---

## 摘要

傳統程式控制流主要處理單次程序內的順序、分支、函式呼叫與有限迴圈。長時程 AI Agent 則必須跨越分鐘、數日、數月甚至更長週期，處理等待外部事件、排程、暫停、恢復、世界狀態變化、權限失效、工具替換、人類決策、重試、補償與目標修訂。若仍將這類系統理解為一個持續運行的 while loop，便會產生忙等、隱藏狀態、資源洩漏、意圖漂移、重複執行、過期計畫與無法稽核等問題。

本文提出「時間—空間程式控制」模型：長時程 Agent 應被表示為事件驅動、可切片、可暫停、可恢復並具有反身監督的持續狀態機，而不是一段永不結束的同步程序。本文將長時程控制狀態表示為：

$$
\Xi_k
=
\left\langle
I_k,
T_k,
C_k,
W_k,
M_k,
E_k,
A_k,
B_k,
K_k,
P_k
\right\rangle
$$

其中依序代表意圖契約、任務圖、能力計畫、世界狀態、持續記憶、事件集合、授權狀態、預算、檢查點與來源證據。系統不以牆鐘時間作為唯一索引，而以事件步 $k$ 描述狀態轉換：

$$
\Xi_{k+1}
=
F
\left(
\Xi_k,
e_k,
\pi_k
\right)
$$

其中 $e_k$ 可以是外部事件、排程喚醒、人類批准、超時、失敗、政策變更或世界狀態差分。

本文區分六種時間：物理時間、單調時間、邏輯時間、事件時間、有效時間與因果時間；並區分五種空間：語意空間、執行空間、資源空間、權限空間與世界狀態空間。所謂「時空切片」不是單純截取日誌區間，而是依時間、任務、語意、權限、資源、主體與因果關係，抽取可獨立理解、驗證、重放或交接的執行子結構。

本文建立九類長時程迴圈：有界迴圈、條件迴圈、事件迴圈、週期迴圈、持續性迴圈、監督迴圈、恢復迴圈、反身迴圈與人類閘門迴圈。每個迴圈必須具備入口、守衛、觀測、更新、預算、檢查點、退出與失效條件；任何開放式迴圈都必須受到租約、生命週期、預算與重新授權約束。

本文進一步定義 continuation 與 checkpoint。檢查點不只是序列化記憶，而必須保存 Intent IR、Task IR、Capability IR、世界前置狀態、未完成效果、事件訂閱、工具版本、權限租約、冪等鍵與恢復義務。恢復不是從上次行數繼續，而是：

$$
\operatorname{Resume}
\left(
K,
W',
A',
\Gamma'
\right)
$$

在重新驗證世界、授權、工具與意圖後，生成新的合法 continuation。

本文提出三層反身控制：物件層執行任務，監督層觀測安全、活性與資源，元層在不改變高層意圖與人類保留決策的前提下修訂計畫。反身性不等於自我授權；任何擴張權限、改變終極目標、取消人類決策點或提高不可逆性的修改，都必須回到 Intent IR 與治理層重新批准。

本文亦處理分散式事件排序、冪等、至少一次交付、有效一次效果、退避重試、補償交易、租約、超時、失效世界狀態、跨 Agent 交接與人類可見狀態。本文最後提出可證偽研究綱領，包括喚醒正確率、恢復保真率、重複效果率、忙等消除率、意圖漂移、事件排序、補償成功率、切片充分性、反身修訂合法率、人類閘門保持率與長時程資源上界。

本文的核心結論是：長時程 Agent 的控制本體，不是持續佔用算力的無限迴圈，而是以事件、租約、檢查點、切片、證書與反身監督構成的可恢復時空圖。

**關鍵詞：** 長時程 Agent、時空切片、事件驅動、continuation、checkpoint、反身執行、意圖漂移、冪等、補償、租約、Agent Runtime

---

## Abstract

Traditional control flow focuses on sequence, branching, function calls, and bounded loops within a single process. Long-horizon AI agents must instead operate across minutes, days, months, or longer periods while waiting for external events, following schedules, suspending and resuming, adapting to world-state changes, handling expiring permissions, switching tools, requesting human decisions, retrying, compensating, and revising plans.

This paper proposes temporal–spatial program control. A long-horizon agent should be modeled as an event-driven, sliceable, suspendable, resumable, and reflexively supervised persistent state machine rather than an endless synchronous loop.

The control state is represented as:

$$
\Xi_k
=
\left\langle
I_k,
T_k,
C_k,
W_k,
M_k,
E_k,
A_k,
B_k,
K_k,
P_k
\right\rangle
$$

The components denote the intent contract, task graph, capability plan, world state, persistent memory, event set, authorization state, budgets, checkpoints, and provenance. State transitions are indexed by event steps rather than wall-clock time alone:

$$
\Xi_{k+1}
=
F
\left(
\Xi_k,
e_k,
\pi_k
\right)
$$

The paper distinguishes physical, monotonic, logical, event, validity, and causal time, together with semantic, execution, resource, authority, and world-state spaces. Temporal–spatial slicing extracts independently understandable, verifiable, replayable, and transferable execution substructures along time, task, semantic, authority, resource, subject, and causal dimensions.

Nine loop classes are introduced: bounded, conditional, event, periodic, persistence, supervisory, recovery, reflexive, and human-gated loops. Every open-ended loop must be constrained by leases, budgets, lifetimes, checkpoints, and reauthorization.

The paper defines continuations and checkpoints as structured execution contracts carrying intent, task, capability, world-state, pending effects, subscriptions, tool versions, permission leases, idempotency keys, and recovery obligations. Resumption requires revalidation rather than simply continuing from the previous instruction pointer.

A three-level reflexive architecture is proposed: the object layer executes tasks, the supervisory layer monitors safety, liveness, and resources, and the meta-layer revises plans without silently changing the governing intent or reserved human decisions. Reflexivity does not imply self-authorization.

The central conclusion is that the control ontology of a long-horizon agent is not an infinite loop consuming continuous computation, but a recoverable temporal–spatial graph composed of events, leases, checkpoints, slices, certificates, and reflexive supervision.

**Keywords:** long-horizon agents, temporal–spatial slicing, event-driven control, continuations, checkpoints, reflexive execution, intent drift, idempotency, compensation

---

# 一、問題的提出：長時程 Agent 不是很長的函式

傳統程式可以在短時間內完成：

```text
input
→ compute
→ output
→ terminate
```

長時程 Agent 則可能：

1. 收到一個意圖；
2. 建立計畫；
3. 完成部分任務；
4. 等待人類批准；
5. 等待外部資料；
6. 因世界改變而重新計畫；
7. 在另一台機器或另一個 Agent 上恢復；
8. 數日後完成；
9. 產生後續監督任務。

若以普通同步程式描述：

```python
while not done:
    check_everything()
    sleep(60)
```

會出現：

- 持續佔用程序；
- 不必要輪詢；
- 狀態藏在記憶體；
- 重啟後遺失；
- 重複副作用；
- 權限過期仍執行；
- 世界改變卻沿用舊計畫；
- 無法判斷何時應終止；
- 無法把任務交接給另一主體。

因此，長時程控制的第一項轉變是：

$$
\boxed{
\text{Long-Horizon Program}
\neq
\text{Long-Running Process}
}
$$

長時程程式可以在大部分時間完全不執行，只保存：

- 狀態；
- 事件訂閱；
- 排程；
- 檢查點；
- 意圖與權限證書。

當條件成立時才被喚醒。

---

# 二、六種時間

## 2.1 物理時間

物理或牆鐘時間：

$$
t_{\mathrm{wall}}
$$

例如：

```text
2026-07-25T15:00:00+08:00
```

適合：

- 日曆；
- 法律期限；
- 人類約會；
- 公開發布時間。

但會受到：

- 時區；
- 夏令時間；
- 系統校時；
- 時鐘跳動；

影響。

## 2.2 單調時間

單調時間：

$$
t_{\mathrm{mono}}
$$

只保證向前，適合測量：

- 超時；
- 經過時間；
- 退避；
- 租約。

不能直接對應日曆時刻。

## 2.3 邏輯時間

邏輯時間：

$$
\lambda_k
$$

描述事件順序而非秒數：

$$
e_i\prec e_j
$$

表示 $e_i$ 在因果或程序上先於 $e_j$ 。

## 2.4 事件時間

事件時間：

$$
t_{\mathrm{event}}
$$

表示事件在來源世界中實際發生的時間，而不是系統收到它的時間。

## 2.5 有效時間

規則或權限的有效區間：

$$
[t_{\mathrm{start}},t_{\mathrm{end}})
$$

例如：

- 授權只在 24 小時內有效；
- 某政策自下月生效；
- 某資料只可保存 30 天。

## 2.6 因果時間

因果時間保存：

$$
e_i
\leadsto
e_j
$$

即事件 $e_j$ 是否依賴 $e_i$ 。

在分散式系統中，收到順序不必等於發生順序，牆鐘較晚也不必表示因果較後。

## 2.7 時間不可混用

例如：

```text
十分鐘後重試
```

應使用單調時間，而不是牆鐘差。

```text
明天上午九點發布
```

應保存時區與日曆語意。

```text
收到付款事件後寄送
```

應使用事件與因果時間，而不是固定輪詢。

---

# 三、五種空間

本文的「空間」不只指物理位置。

## 3.1 語意空間

表示：

- 意圖；
- 目標；
- 任務；
- 能力；
- 約束；
- 證據；

之間的結構位置。

## 3.2 執行空間

表示程序在哪個環境執行：

- 本地；
- 沙盒；
- 容器；
- 雲端；
- 瀏覽器；
- 邊緣裝置；
- 人類工作台。

## 3.3 資源空間

表示：

- CPU；
- GPU；
- 記憶體；
- 儲存；
- 網路；
- API 配額；
- 金錢；
- 能源。

## 3.4 權限空間

表示能力所處信任域：

- 公開；
- 私有；
- 組織；
- 專案；
- 管理員；
- 只讀；
- 高風險寫入；
- 多主體批准。

## 3.5 世界狀態空間

表示外部世界：

$$
W
=
\left(
W_{\mathrm{digital}},
W_{\mathrm{physical}},
W_{\mathrm{social}},
W_{\mathrm{institutional}}
\right)
$$

## 3.6 空間遷移

將任務從一個執行空間移至另一空間：

$$
S_i
\xrightarrow{\operatorname{Transfer}}
S_j
$$

需要檢查：

- 資料可否移動；
- 權限是否可轉移；
- 工具是否相容；
- 狀態是否完整；
- 法律與地域限制；
- 誰取得新的控制權。

---

# 四、長時程控制狀態

本文定義：

$$
\boxed{
\Xi_k
=
\left\langle
I_k,
T_k,
C_k,
W_k,
M_k,
E_k,
A_k,
B_k,
K_k,
P_k
\right\rangle
}
$$

其中：

- $I_k$ ：Intent IR；
- $T_k$ ：Task IR；
- $C_k$ ：Capability IR 與當前計畫；
- $W_k$ ：已知世界狀態；
- $M_k$ ：持續記憶；
- $E_k$ ：已訂閱、待處理與已處理事件；
- $A_k$ ：權限、租約與人類批准；
- $B_k$ ：資源與風險預算；
- $K_k$ ：continuation 與 checkpoints；
- $P_k$ ：來源、證據與執行 trace。

## 4.1 事件步

狀態轉換：

$$
\Xi_{k+1}
=
F
\left(
\Xi_k,
e_k,
\pi_k
\right)
$$

其中：

- $e_k$ ：新事件；
- $\pi_k$ ：當前合法控制策略。

## 4.2 事件來源

事件可來自：

- 工具結果；
- 人類輸入；
- 排程；
- 超時；
- 世界監測；
- 政策更新；
- 權限撤銷；
- 其他 Agent；
- 系統失敗；
- 預算耗盡。

## 4.3 無事件時不必轉移

若沒有相關事件：

$$
\Xi_{k+1}
=
\Xi_k
$$

系統可以完全休眠，而不是持續計算。

---

# 五、時間—空間控制圖

定義控制圖：

$$
\mathfrak G_{TS}
=
(V,E)
$$

節點：

$$
v
=
\left(
\tau,
\sigma,
q,
g
\right)
$$

其中：

- $\tau$ ：時間條件；
- $\sigma$ ：空間位置；
- $q$ ：控制狀態；
- $g$ ：守衛。

邊可表示：

- 立即轉移；
- 排程轉移；
- 事件轉移；
- 人類批准；
- 超時；
- 重試；
- 補償；
- 恢復；
- 元層修訂。

## 5.1 節點狀態

```text
ready
running
waiting-event
waiting-time
waiting-human
suspended
blocked
retrying
compensating
completed
failed
cancelled
expired
```

## 5.2 邊守衛

$$
g_e
:
\Xi
\rightarrow
\{\text{true},\text{false},\text{unknown}\}
$$

`unknown` 不是 `false`，可能要求取得資料或澄清。

---

# 六、九類迴圈

迴圈不應只有 `for` 與 `while`。

## 6.1 有界迴圈

$$
L_B(n)
$$

已知最大次數。

應保存：

- 計數器；
- 上界；
- 每輪證據；
- 提前退出條件。

## 6.2 條件迴圈

$$
\operatorname{while}\;p(W)
$$

守衛依世界或內部狀態。

必須處理：

- `true`；
- `false`；
- `unknown`；
- 狀態過時；
- 守衛取得成本。

## 6.3 事件迴圈

等待事件：

$$
\operatorname{await}(e)
$$

事件到達才喚醒。

這不是忙等。

## 6.4 週期迴圈

依排程執行：

$$
L_P(\Delta t)
$$

需要：

- 時區；
- 跳過或補跑政策；
- 重疊執行政策；
- 抖動與延遲容許。

## 6.5 持續性迴圈

長期維持某不變量：

$$
\Box P
$$

例如：

```text
保持備份可恢復。
```

它不是永遠執行，而是訂閱會破壞 $P$ 的相關事件。

## 6.6 監督迴圈

觀測：

- 安全；
- 活性；
- 資源；
- 漂移；
- 錯誤；
- 權限。

監督者不直接完成業務任務。

## 6.7 恢復迴圈

處理：

- 重試；
- 回復；
- 補償；
- 替代能力；
- 人類接管。

## 6.8 反身迴圈

檢查當前計畫是否仍適合：

$$
\pi_{k+1}
=
\operatorname{Revise}
\left(
\pi_k,
\Xi_k,
I_k
\right)
$$

## 6.9 人類閘門迴圈

系統準備資料並等待：

$$
x_h
$$

人類決策後才繼續。

等待期間不能自行把無回應解釋為同意，除非 Intent IR 明確規定合法默認。

---

# 七、迴圈契約

每個迴圈應表示為：

$$
L
=
\left\langle
\operatorname{Entry},
G,
B,
O,
U,
K,
X,
F
\right\rangle
$$

其中：

- $\operatorname{Entry}$ ：入口；
- $G$ ：守衛；
- $B$ ：迴圈體；
- $O$ ：觀測；
- $U$ ：更新；
- $K$ ：檢查點；
- $X$ ：退出；
- $F$ ：失敗與補償。

另需預算：

$$
\mathcal B_L
=
\left(
b_{\mathrm{time}},
b_{\mathrm{calls}},
b_{\mathrm{cost}},
b_{\mathrm{writes}},
b_{\mathrm{risk}}
\right)
$$

## 7.1 開放式迴圈

若沒有固定上界，必須具有：

- 租約；
- 定期重授權；
- 成本上限；
- 觀測頻率；
- 終止條件；
- 無進展偵測。

## 7.2 無進展

令進展度量：

$$
\mu(\Xi_k)
$$

若連續 $n$ 輪：

$$
\mu(\Xi_{k+n})
\leq
\mu(\Xi_k)
$$

則應：

- 暫停；
- 改變計畫；
- 請求人類；
- 宣告阻塞。

---

# 八、等待不是迴圈

## 8.1 忙等

錯誤形式：

```text
repeat:
  check condition
  sleep
```

## 8.2 事件訂閱

合理形式：

```text
subscribe(condition_source)
persist continuation
release resources
resume on event
```

## 8.3 排程喚醒

對無事件來源的條件，可建立下一次合理檢查：

$$
t_{\mathrm{next}}
=
\operatorname{Schedule}
\left(
\text{change rate},
\text{risk},
\text{deadline},
\text{cost}
\right)
$$

## 8.4 自適應檢查頻率

變化快速或接近期限時提高頻率；穩定且低風險時降低頻率。

但頻率調整不得超出資源預算或使用者要求。

---

# 九、Continuation：可恢復執行身分

## 9.1 定義

Continuation：

$$
\kappa
=
\left\langle
H_I,
H_T,
H_C,
q,
\beta,
W^\ast,
A^\ast,
E^\ast,
B^\ast,
\Gamma
\right\rangle
$$

其中：

- $H_I$ ：Intent IR 雜湊；
- $H_T$ ：Task IR 雜湊；
- $H_C$ ：Capability IR 雜湊；
- $q$ ：控制節點；
- $\beta$ ：局部綁定；
- $W^\ast$ ：依賴的世界前置狀態；
- $A^\ast$ ：權限與租約；
- $E^\ast$ ：待處理事件與訂閱；
- $B^\ast$ ：剩餘預算；
- $\Gamma$ ：工具、schema 與環境版本。

## 9.2 Continuation 不是堆疊快照

對長時程 Agent，只保存程式計數器與記憶體不足，因為外部世界可能已改變。

## 9.3 恢復

$$
\operatorname{Resume}
\left(
\kappa,
W',
A',
\Gamma'
\right)
\rightarrow
\begin{cases}
\kappa' & \text{可恢復}\\
\text{replan} & \text{需重新計畫}\\
\text{human-review} & \text{需人類決策}\\
\text{blocked} & \text{不可恢復}
\end{cases}
$$

## 9.4 恢復驗證

至少檢查：

- 意圖是否仍有效；
- 任務是否被撤回；
- 世界前置狀態；
- 權限與租約；
- 工具版本；
- 未完成副作用；
- 已處理事件；
- 冪等鍵；
- 預算。

---

# 十、Checkpoint：檢查點不是備份檔

## 10.1 檢查點內容

```text
Checkpoint {
  intent_version
  task_graph_version
  capability_plan_version
  control_state
  local_bindings
  observed_world_hashes
  pending_effects
  completed_effects
  idempotency_keys
  subscriptions
  permission_leases
  budgets
  evidence
  recovery_policy
}
```

## 10.2 檢查點類型

- 任務前；
- 外部寫入前；
- 人類閘門前；
- 批次完成後；
- 計畫修訂前；
- 遷移前；
- 關閉前。

## 10.3 安全檢查點

安全檢查點要求：

$$
\operatorname{Recoverable}(K)
=
\text{true}
$$

或明確標記哪些效果不可回復。

## 10.4 檢查點鏈

$$
K_0
\rightarrow
K_1
\rightarrow
\cdots
\rightarrow
K_n
$$

每個節點保存差分與證據，避免每次完整複製所有狀態。

---

# 十一、時空切片

## 11.1 定義

切片算子：

$$
\operatorname{Slice}
\left(
\mathfrak G_{TS},
Q
\right)
\rightarrow
\mathfrak G_Q
$$

其中 $Q$ 是查詢或切片條件。

## 11.2 時間切片

抽取：

$$
[t_0,t_1)
$$

內的狀態、事件與效果。

## 11.3 任務切片

抽取與某目標或任務相關的所有節點。

## 11.4 語意切片

例如只查看：

- 權限；
- 隱私；
- 微分；
- 成本；
- 公開發布。

## 11.5 權限切片

抽取某能力、主體或租約所影響的節點。

## 11.6 資源切片

查看 GPU、API、金錢、儲存或網路資源的因果路徑。

## 11.7 主體切片

查看某人類或 Agent：

- 提出了什麼；
- 批准了什麼；
- 受何影響；
- 執行了什麼。

## 11.8 因果切片

對結果 $r$ ，抽取：

$$
\operatorname{Causes}(r)
$$

包括意圖、計畫、工具、事件、權限與世界狀態。

## 11.9 反事實切片

詢問：

> 若沒有事件 $e$ 或沒有批准 $a$ ，結果是否仍會發生？

用於分析關鍵依賴。

## 11.10 切片充分性

切片不能只顯示局部結果而隱藏必要上下文。

需有：

$$
\operatorname{Sufficient}
\left(
\mathfrak G_Q,
Q
\right)
$$

---

# 十二、安全、活性與公平

## 12.1 安全性

安全性要求壞狀態永不成立：

$$
\Box\neg B
$$

例如：

```text
未批准不得正式發布。
```

## 12.2 活性

活性要求在條件允許時最終進展：

$$
\Diamond G
$$

但不能承諾無法控制的外部世界一定發生。

## 12.3 條件活性

$$
\Box
\left(
P
\Rightarrow
\Diamond G
\right)
$$

即當前置條件成立、資源可用且未撤回時，系統應最終處理。

## 12.4 公平

多任務系統需避免某任務永遠飢餓。

## 12.5 安全與活性衝突

過度安全可能永遠不行動；過度追求進展可能越權。

監督層需明示：

- 為何阻止；
- 哪個條件未成立；
- 如何解除阻塞。

---

# 十三、終止狀態

Agent 任務不應只有 `done` 與 `error`。

建議狀態：

```text
completed
partially-completed
waiting
suspended
blocked
failed
cancelled
expired
revoked
compensating
handed-off
```

## 13.1 完成

$$
\operatorname{Completed}
\iff
V_{\mathrm{goal}}
\land
V_{\mathrm{constraint}}
\land
V_{\mathrm{permission}}
\land
V_{\mathrm{state}}
\land
V_{\mathrm{report}}
$$

## 13.2 部分完成

必須列出：

- 已完成；
- 未完成；
- 原因；
- 風險；
- 是否可恢復。

## 13.3 過期

意圖、權限、資料或期限過期時：

$$
\operatorname{Expired}
$$

不得自動重啟。

---

# 十四、預算、租約與生命週期

## 14.1 預算向量

$$
B
=
\left(
B_t,
B_c,
B_a,
B_w,
B_r,
B_e
\right)
$$

其中：

- $B_t$ ：時間；
- $B_c$ ：金錢；
- $B_a$ ：API／工具呼叫；
- $B_w$ ：寫入；
- $B_r$ ：風險；
- $B_e$ ：能源或算力。

## 14.2 租約

權限或任務租約：

$$
\ell
=
\left(
\text{scope},
t_{\mathrm{expire}},
\text{renewal policy}
\right)
$$

租約到期後：

$$
\operatorname{Execute}
=
\text{blocked}
$$

## 14.3 生命週期

任何持續任務都應有：

- 建立者；
- 所有者；
- 有效期；
- 更新頻率；
- 停止條件；
- 無所有者時的政策。

## 14.4 無主迴圈

沒有所有者、期限與預算的持續任務應被拒絕或自動失效。

---

# 十五、冪等、重複與交付語意

## 15.1 至少一次

事件或動作可能重送：

$$
n\geq1
$$

## 15.2 至多一次

可能完全不重試：

$$
n\leq1
$$

## 15.3 有效一次

對外效果需使用：

- 冪等鍵；
- 去重表；
- 狀態檢查；
- 交易；
- 結果確認。

使多次處理在觀察上等價於一次：

$$
O(O(x))
\equiv
O(x)
$$

## 15.4 非冪等操作

付款、寄信、刪除、公開發布等，不能假設天然冪等。

## 15.5 執行身分

每個效果事件應有：

```text
effect_id
intent_hash
task_id
capability_id
idempotency_key
attempt
world_precondition
observed_result
```

---

# 十六、失敗、重試與補償

## 16.1 失敗分類

- 暫時性；
- 永久性；
- 權限；
- 世界狀態；
- 工具；
- 資源；
- 規格；
- 驗證；
- 人類拒絕；
- 不確定。

## 16.2 重試政策

重試需指定：

- 最大次數；
- 退避；
- 抖動；
- 可重試錯誤；
- 截止時間；
- 冪等條件。

## 16.3 補償

不可交易的跨系統操作可用補償：

$$
a_1,a_2,\ldots,a_n
$$

失敗後執行：

$$
\bar a_{n-1},\ldots,\bar a_1
$$

補償不是時間倒流，只是新的世界操作。

## 16.4 回復能力

每個效果應標記：

```text
fully-reversible
compensatable
partially-reversible
irreversible
unknown
```

## 16.5 不可逆前檢查點

高不可逆操作前必須：

- 更新世界狀態；
- 重新確認權限；
- 產生證據；
- 取得人類決策；
- 鎖定計畫版本。

---

# 十七、三層反身控制

## 17.1 物件層

執行 Task IR：

$$
L_0
:
T
\rightarrow
\Delta W
$$

## 17.2 監督層

監測：

$$
L_1
:
\left(
L_0,
W,
B,
A
\right)
\rightarrow
\{\text{continue},\text{pause},\text{stop},\text{escalate}\}
$$

## 17.3 元層

修訂計畫：

$$
L_2
:
\left(
\pi_k,
I,
T,
C,
\operatorname{Evidence}
\right)
\rightarrow
\pi_{k+1}
$$

## 17.4 反身不等於自我授權

元層不能自行：

- 擴張權限；
- 修改終極目標；
- 移除非目標；
- 取消人類閘門；
- 提高不可逆性；
- 變更受影響主體權利。

## 17.5 修訂證明

每次計畫修訂應產生：

$$
\operatorname{RevisionProof}
\left(
\pi_k,
\pi_{k+1},
I
\right)
$$

說明：

- 為何需要改；
- 哪些語意保持；
- 哪些成本與風險改變；
- 是否需要批准。

---

# 十八、意圖漂移與時態回錨

## 18.1 漂移向量

$$
D_I(k)
=
\left(
d_G,
d_N,
d_C,
d_A,
d_X,
d_H
\right)
$$

依序表示目標、非目標、限制、權限、人類決策與受影響主體的漂移。

## 18.2 回錨點

應在以下時機重新比較 Intent IR：

- 主要里程碑；
- 失敗後；
- 工具替換；
- 世界狀態顯著改變；
- 權限更新；
- 長時間休眠後；
- 交接給其他 Agent。

## 18.3 漂移閾值

$$
\|D_I(k)\|>\tau
\Rightarrow
\text{pause and review}
$$

## 18.4 合法修訂

人類明示修改：

$$
I^{(v)}
\rightarrow
I^{(v+1)}
$$

需要重新編譯受影響的 Task、Capability 與 Continuation。

---

# 十九、分散式 Agent 與事件排序

## 19.1 多 Agent

$$
\mathcal A
=
\{
A_1,\ldots,A_n
\}
$$

每個 Agent 可能只持有局部狀態。

## 19.2 因果順序

若：

$$
e_i\leadsto e_j
$$

則所有合法重放都應保留此順序。

## 19.3 並行事件

若沒有因果關係：

$$
e_i\parallel e_j
$$

可以並行，但仍需檢查資源與效果衝突。

## 19.4 交接

Agent 交接需傳遞：

- Intent IR；
- Task IR；
- Capability IR；
- continuation；
- 世界快照；
- 權限；
- 未完成效果；
- 事件偏移；
- 證據；
- 人類決策點。

## 19.5 接手驗證

接手者不能只相信摘要，需驗證版本、雜湊與來源。

---

# 二十、人類可見狀態

長時程 Agent 不能只顯示：

```text
working
```

應至少顯示：

- 當前目標；
- 目前狀態；
- 正在等待什麼；
- 下一個喚醒條件；
- 已使用預算；
- 剩餘權限租約；
- 已完成效果；
- 未完成效果；
- 風險；
- 人類決策；
- 停止方法；
- 恢復方法。

## 20.1 時間線

事件時間線應區分：

- 計畫事件；
- 世界事件；
- 工具事件；
- 人類事件；
- 政策事件；
- 補償事件。

## 20.2 不能用敘事代替狀態

「我會繼續處理」不是可恢復狀態。

必須有持久化 continuation、訂閱與檢查點。

---

# 二十一、主要失敗模式

## 21.1 無限 while

用程序常駐冒充長時程控制。

## 21.2 忙等

沒有事件訂閱，只反覆查詢。

## 21.3 牆鐘混亂

把超時、期限與經過時間混用。

## 21.4 檢查點不足

只保存對話摘要，沒有世界、權限與副作用狀態。

## 21.5 重複副作用

重試造成重複付款、寄信或發布。

## 21.6 過期 continuation

世界與權限已變仍直接恢復。

## 21.7 隱藏租約

持續任務沒有期限、所有者與預算。

## 21.8 恢復等同重跑

從頭執行導致重複效果。

## 21.9 反身僭位

計畫修訂偷偷改變高層意圖。

## 21.10 人類閘門繞過

把沉默、超時或無回應解釋為批准。

## 21.11 切片誤導

只顯示局部成功，隱藏相關失敗與權限。

## 21.12 分散式亂序

晚到事件覆蓋較新的合法狀態。

## 21.13 補償幻覺

把補償當成完美 rollback。

## 21.14 無進展持續

系統反覆運行卻沒有可測量進展。

---

# 二十二、可證偽研究綱領

## 22.1 喚醒正確率

$$
\eta_W
=
\frac{
\text{correctly awakened continuations}
}{
\text{all eligible awakenings}
}
$$

同時測量誤喚醒與漏喚醒。

## 22.2 恢復保真率

恢復後比較：

$$
d
\left(
\Xi_{\mathrm{expected}},
\Xi_{\mathrm{resumed}}
\right)
$$

## 22.3 重複效果率

$$
R_D
=
\frac{
\text{unintended duplicate effects}
}{
\text{all retried effects}
}
$$

## 22.4 忙等消除率

比較事件驅動與輪詢架構的無效喚醒、API 呼叫、算力與成本。

## 22.5 意圖漂移

追蹤：

$$
\|D_I(k)\|
$$

比較有無回錨與修訂證明。

## 22.6 事件排序

注入亂序、重複、延遲與遺失事件，測量最終狀態正確性。

## 22.7 補償成功率

測量：

- 完整補償；
- 部分補償；
- 新增副作用；
- 人類介入需求。

## 22.8 切片充分性

給定問題，評估切片是否包含重建答案所需的全部因果與治理上下文。

## 22.9 反身修訂合法率

檢查計畫修訂是否保持：

- 目標；
- 非目標；
- 限制；
- 權限；
- 人類保留決策。

## 22.10 人類閘門保持率

$$
\eta_H
=
\frac{
\text{human gates not bypassed}
}{
\text{all required human gates}
}
$$

## 22.11 資源上界

測量持續任務在長時間內是否遵守：

- 呼叫；
- 成本；
- 儲存；
- 網路；
- 風險；
- 能源；

上界。

---

# 二十三、與第七篇的關係

第七篇建立：

$$
\text{Intent IR}
\rightarrow
\text{Task IR}
\rightarrow
\text{Capability IR}
$$

本篇把靜態能力計畫提升為時間中的持續控制：

$$
\boxed{
\text{Capability Plan}
\rightarrow
\text{Temporal–Spatial Control Graph}
\rightarrow
\text{Events and Checkpoints}
\rightarrow
\text{Recoverable Execution}
}
$$

Intent IR 決定：

- 為何執行；
- 哪些邊界不能越過；
- 哪些決策保留給人類。

時空控制決定：

- 何時執行；
- 在哪裡執行；
- 何時等待；
- 如何恢復；
- 何時重新計畫；
- 何時終止。

---

# 二十四、與第九篇的關係

本篇建立控制語義，但尚未完整定義 Runtime 的模組邊界。

第九篇將把控制圖實作為：

- 狀態儲存；
- 事件匯流排；
- 排程器；
- 能力註冊表；
- 工具執行器；
- 權限引擎；
- 驗證器；
- 補償管理器；
- 人類介面；
- trace 與證書。

也就是：

$$
\mathfrak G_{TS}
\rightarrow
\operatorname{AgentRuntime}
$$

---

# 二十五、本文的十五項命題

## 命題一

$$
\boxed{
\text{Long-Horizon Program}
\neq
\text{Long-Running Process}
}
$$

## 命題二

等待應被表示為事件訂閱、排程或人類閘門，而不是忙等。

## 命題三

牆鐘時間、單調時間、邏輯時間、事件時間、有效時間與因果時間不可混用。

## 命題四

長時程 Agent 的空間至少包含語意、執行、資源、權限與世界狀態空間。

## 命題五

每個開放式迴圈都必須具有預算、租約、檢查點與退出條件。

## 命題六

Continuation 必須保存外部世界與權限義務，而不只是程序位置。

## 命題七

恢復必須重新驗證，不是簡單繼續執行。

## 命題八

時空切片應支援時間、任務、語意、權限、資源、主體與因果查詢。

## 命題九

安全與活性必須同時被監督。

## 命題十

有效一次效果需要冪等鍵、去重、狀態檢查與證據，而不是口頭承諾。

## 命題十一

補償是新的世界操作，不是時間倒流。

## 命題十二

反身計畫修訂不得變成自我授權。

## 命題十三

人類保留決策在長時間等待後仍不得被自動繞過。

## 命題十四

無所有者、無期限、無預算的持續迴圈不具治理合法性。

## 命題十五

$$
\boxed{
\text{Long-Horizon Agent Control}
=
\text{Events}
+
\text{Leases}
+
\text{Checkpoints}
+
\text{Slices}
+
\text{Reflexive Supervision}
}
$$

---

# 二十六、結論：真正持續的不是程序，而是可恢復的承諾

長時程 Agent 最容易產生的錯覺，是：

> 只要程式一直運行，任務就會持續存在。

實際上，程序可能崩潰、機器可能關閉、模型可能更換、工具可能失效、權限可能撤銷、世界可能改變，人類也可能修改或撤回原始意圖。

因此，真正需要持續的不是某個程序記憶體，而是：

- 意圖契約；
- 任務與能力結構；
- 世界前置狀態；
- 事件訂閱；
- 檢查點；
- 權限與租約；
- 已產生效果；
- 未完成義務；
- 人類決策；
- 來源與證據。

其完整形式是：

$$
\boxed{
\text{Persistent Commitment}
\rightarrow
\text{Event-Driven Wakeup}
\rightarrow
\text{Revalidation}
\rightarrow
\text{Bounded Action}
\rightarrow
\text{Checkpoint}
}
$$

然後再次等待下一個合法事件。

這種系統可以跨越時間，卻不需要永遠消耗計算。

可以跨越機器，卻不丟失執行身分。

可以修改計畫，卻不必修改高層意圖。

可以自我監督，卻不能自我擴權。

可以等待人類，卻不能把沉默當成同意。

因此，本文的最終命題是：

$$
\boxed{
\text{長時程 Agent 的本體不是無限迴圈，}
}
$$

$$
\boxed{
\text{而是一張由事件、檢查點、租約、切片與證書構成的}
}
$$

$$
\boxed{
\text{可暫停、可交接、可恢復、可終止的時空控制圖。}
}
$$

下一篇將把這套控制語義落入 Agent Runtime，正式處理能力註冊、工具調用、事件匯流排、狀態持久化、權限、驗證與失敗恢復。

---

# 附錄 A：長時程控制規格範例

```yaml
temporal_spatial_control:
  control_id: "tsc-website-review-001"
  intent_hash: "sha256:..."
  task_hash: "sha256:..."
  capability_hash: "sha256:..."
  status: "waiting-human"

current_node:
  task_id: "t4"
  state: "waiting-human"
  entered_at: "2026-07-25T15:00:00+08:00"

wait:
  type: "human-decision"
  decision_id: "x1"
  owner: "project_owner"
  timeout: null
  silence_means_approval: false

subscriptions:
  - event: "human_decision_submitted"
    filter:
      decision_id: "x1"
  - event: "intent_revoked"
    filter:
      intent_hash: "sha256:..."
  - event: "policy_changed"
    filter:
      project: "website"

lease:
  scope:
    - "preview_environment:read"
  expires_at: "2026-07-26T15:00:00+08:00"
  renewable: true
  renewal_requires: "policy_revalidation"

budget:
  api_calls_remaining: 20
  writes_remaining: 0
  risk_remaining: "low"

on_event:
  human_decision_submitted:
    - "revalidate_intent"
    - "revalidate_world"
    - "revalidate_authorization"
    - "continue_or_replan"
  intent_revoked:
    - "cancel_pending_tasks"
    - "archive_checkpoint"
  policy_changed:
    - "suspend"
    - "require_review"
```

---

# 附錄 B：Continuation 範例

```yaml
continuation:
  continuation_id: "cont-20260725-004"
  control_node: "waiting_release_decision"

hashes:
  intent_ir: "sha256:..."
  task_ir: "sha256:..."
  capability_ir: "sha256:..."
  world_precondition: "sha256:..."

bindings:
  preview_url: "https://preview.example.invalid"
  candidate_commit: "git:abc123"
  test_report: "artifact:test-report-001"

effects:
  completed:
    - effect_id: "deploy-preview-001"
      idempotency_key: "intent001-preview-v1"
  pending: []

subscriptions:
  - "human_decision:x1"
  - "intent_revoked:intent001"
  - "policy_changed:project001"

authorization:
  leases:
    - scope: "preview_environment:read"
      expires_at: "2026-07-26T15:00:00+08:00"

budget:
  api_calls_remaining: 20
  cost_remaining: 0
  writes_remaining: 0

resume_policy:
  revalidate:
    - "intent"
    - "world_state"
    - "authorization"
    - "tool_versions"
  if_stale: "replan"
  if_unauthorized: "blocked"
```

---

# 附錄 C：迴圈契約範例

```yaml
loop:
  loop_id: "monitor-preview-health"
  class: "persistence-loop"
  owner: "project_owner"

invariant:
  rule: "preview_health == healthy"

observation:
  source: "preview_health_event"
  polling_fallback:
    enabled: true
    interval: "PT30M"
    max_checks: 24

budget:
  api_calls: 30
  lifetime: "P1D"
  risk: "low"

lease:
  expires_at: "2026-07-26T15:00:00+08:00"
  renewal_requires: "owner_confirmation"

on_violation:
  - "collect_diagnostics"
  - "attempt_once_restart"
  - "if_still_failed_suspend_and_notify"

termination:
  - "preview_deleted"
  - "production_decision_completed"
  - "lease_expired"
  - "intent_revoked"

checkpoint:
  after_each_event: true
```

---

# 附錄 D：時空切片查詢範例

```yaml
slice_query:
  question: "為什麼預覽部署被重新執行？"

dimensions:
  time:
    from: "2026-07-25T14:00:00+08:00"
    to: "2026-07-25T16:00:00+08:00"
  task:
    - "t3"
  effects:
    - "deploy_preview"
  subjects:
    - "agent-runtime"
  causal_ancestors: true
  include_permissions: true
  include_world_state: true
  include_retries: true

required_output:
  - "trigger_event"
  - "prior_attempts"
  - "idempotency_decision"
  - "authorization"
  - "observed_world_state"
  - "final_effect"
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
8. **時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行**
9. Agent Runtime：能力規劃、工具調用與可恢復執行
10. 可編譯世界：從程式執行到世界狀態演化
11. 人類可見狀態：意圖程式系統的稽核、解釋與可逆治理
12. 意圖程式文明：後文本語言、持續 Agent 與可編譯世界的統一理論

---

# 參考文獻

## Neo.K／EveMissLab 理論與規格文件

1. Neo.K with Aletheia，《意圖中介表示：從自然語言要求到可驗證能力計畫》，2026。
2. Neo.K，《時間迴圈分類學：一種面向長時程程式、AI Agent 與人機協作的通用控制流理論》，2026。
3. Neo.K，《時空迴圈－切片動力學：面向 AI Agent 的反身圖論式系統控制理論》，2026。
4. Neo.K，《程式設計—意圖語言—AI Agent—時空切片理論群總索引》，2026。
5. Neo.K，《Local-first Agent Plugin Runtime Technical Whitepaper》，2026。
6. Neo.K，《Noesis Studio／NOEMA AgentOS Human Cockpit Whitepaper》，2026。
7. Neo.K，《HVSL：人類可見狀態層》，2026。
8. Neo.K，《Agent Semantic Pad》，2026。

## 一般理論背景

9. Hoare, C. A. R., “Communicating Sequential Processes,” 1978.
10. Milner, R., *Communication and Concurrency*, 1989.
11. Lamport, L., “Time, Clocks, and the Ordering of Events in a Distributed System,” 1978.
12. Hewitt, C., Bishop, P., and Steiger, R., “A Universal Modular Actor Formalism for Artificial Intelligence,” 1973.
13. Pnueli, A., “The Temporal Logic of Programs,” 1977.
14. Harel, D., “Statecharts: A Visual Formalism for Complex Systems,” 1987.
15. Gray, J. and Reuter, A., *Transaction Processing*, 1992.
16. Garcia-Molina, H. and Salem, K., “Sagas,” 1987.
17. Fidge, C., “Timestamps in Message-Passing Systems,” 1988.
18. Mattern, F., “Virtual Time and Global States of Distributed Systems,” 1989.

---

# 版本紀錄

## v0.1 — 2026-07-25

- 完成系列第八篇。
- 將長時程 Agent 定義為事件驅動、可切片、可恢復的持續狀態機。
- 建立六種時間與五種空間。
- 建立長時程控制狀態與時間—空間控制圖。
- 提出九類 Agent 迴圈與迴圈契約。
- 區分等待、事件訂閱、排程與忙等。
- 建立 continuation 與 checkpoint 的完整結構。
- 建立時間、任務、語意、權限、資源、主體、因果與反事實切片。
- 形式化安全、活性、公平與多終止狀態。
- 加入預算、租約、生命週期與無主迴圈限制。
- 建立冪等、有效一次效果、重試、退避與補償模型。
- 建立物件層、監督層與元層三層反身控制。
- 加入意圖漂移、回錨、分散式排序與 Agent 交接。
- 提出十四類主要失敗模式與十一項可證偽研究基準。
- 銜接 Agent Runtime。
