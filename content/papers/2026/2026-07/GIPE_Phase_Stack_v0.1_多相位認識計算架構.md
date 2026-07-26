# GIPE Phase Stack v0.1
## ——多相位認識計算架構

**GIPE Phase Stack v0.1: A Multi-Phase Epistemic Computing Architecture**

**作者：Neo.K × GPT-5.6 Thinking**  
**機構：EveMissLab / 一言諾科技有限公司**  
**版本：v0.1**  
**日期：2026-07-25**  
**文件類型：理論論文／AI 系統架構／相位計算機理論**

---

## 摘要

全域欲相位認識論（Global Intent-Phase Epistemology, GIPE）將智能研究理解為：全域欲結構在未知世界中，透過搜尋、閱讀、計算、模擬、實驗、反證、驗證與行動，不斷更新世界模型與自身認識狀態的過程。

然而，GIPE 若只用單一抽象符號 $\Phi$ 表示所有相位，就會隱藏一個重要事實：欲、世界模型、假設、證據、行動、資源、子 Agent 與治理狀態，其相位本體、表示、演化方式與驗證要求並不相同。它們不能由同一個求解器，也不能由同一種資料結構完整處理。

本文提出「GIPE Phase Stack」，將 GIPE 分解為七個相互耦合但不可混同的相位層：

1. 欲相位層；
2. 世界模型相位層；
3. 假設相位層；
4. 證據相位層；
5. 行動相位層；
6. 資源與風險相位層；
7. 多 Agent 與治理相位層。

每一層都必須聲明相位本體、表示方式、演化規則、耦合關係、記憶需求、驗證等級、可逆性、權限與對應的相位機器。本文進一步將相位圖機、相位流機、相位事件機、相位證明機、相位模擬機與元相位選擇器整合為一個可動態重配置的認識計算堆疊。

完整架構為：

$$
\boxed{
\text{Global Intent}
\rightarrow
\text{Phase Decomposition}
\rightarrow
\text{Phase Machine Routing}
\rightarrow
\text{Epistemic Action}
\rightarrow
\text{Observation}
\rightarrow
\text{Cross-Layer Update}
\rightarrow
\text{Governance Closure}
}
$$

本文主張，GIPE 不應被實作成一個巨型單體 Agent，而應被實作為一組具有明確相位型別、資料契約、權限邊界與選擇證書的多層相位系統。

---

## 關鍵詞

GIPE、Phase Stack、相位計算、PCMT、世界模型、SGCD、多 Agent、元相位選擇器、認識計算、AI 系統架構

---

# 一、問題背景

## 1.1 GIPE 的抽象強度已超過單一求解器

GIPE 的核心循環可寫為：

$$
\mathcal W_t
\xrightarrow{\operatorname{DRC}}
\mathcal A_t^{cand}
\xrightarrow{\operatorname{SGCD}}
G_t^{action}
\xrightarrow{\operatorname{Select}}
a_t
\xrightarrow{\operatorname{Intervene}}
o_t
\xrightarrow{\operatorname{Verify}}
v_t
\xrightarrow{\operatorname{Phase}}
\Delta\Phi_t
\xrightarrow{\operatorname{Update}}
\mathfrak X_{t+1}
$$

這個表示適合理論總覽，但在工程上仍然太粗。因為欲結構不是證據圖，證據圖不是行動狀態機，行動狀態機不是時間流，子 Agent 委派不是物理振盪，權限驗證不是語義嵌入，世界模型更新也不是單一信心分數。

因此：

$$
\Phi^{GIPE}
\neq
\text{single scalar or vector}
$$

## 1.2 多相位不是多個名稱

所謂多相位，不是把每個模組都重新命名為 phase。

一個 GIPE 區域只有在具備關係性、差分、演化、結構效應與輸出相關性時，才被納入 Phase Stack。

## 1.3 Stack 的目的

GIPE Phase Stack 要回答：

1. GIPE 中有哪些不同相位？
2. 每一層用什麼資料結構？
3. 每一層由哪種相位機器處理？
4. 各層如何耦合？
5. 哪些更新可以自動進行？
6. 哪些轉換需要驗證？
7. 哪些行動需要權限與責任閉合？
8. 元相位選擇器如何動態配置整個系統？

---

# 二、GIPE 的七層相位架構

完整堆疊為：

```text
L7 Multi-Agent & Governance Phase
L6 Resource & Risk Phase
L5 Action Phase
L4 Evidence Phase
L3 Hypothesis Phase
L2 World-Model Phase
L1 Intent Phase
```

元相位選擇器位於所有層之上，但不取代任何一層。

---

# 三、L1：欲相位層

## 3.1 欲相位不是欲望分數

欲相位描述目標、子目標、約束、優先序、停止條件、資源容許、不可逆性與價值治理條件。

表示為：

$$
\Phi^W_t
=
(
G_t,
C_t,
P_t,
S_t,
V_t
)
$$

其中：

- $G_t$ ：目標；
- $C_t$ ：約束；
- $P_t$ ：優先序；
- $S_t$ ：停止條件；
- $V_t$ ：價值與治理。

## 3.2 欲相位的主要機器

推薦：

- 相位事件機；
- 相位證明機；
- 元相位機。

## 3.3 欲相位更新

欲相位只有在以下情況可以更新：

- 使用者明確修改；
- 任務條件變化；
- 發現目標不可達；
- 發現目標內部矛盾；
- 安全與法律條件要求；
- 資源不足導致降級。

更新必須記錄：

```yaml
intent_update:
  previous_goal:
  new_goal:
  trigger:
  authorized_by:
  reversible:
  reason:
```

---

# 四、L2：世界模型相位層

## 4.1 世界模型相位

世界模型相位是 GIPE 對未知世界的動態結構表示。

$$
\Phi^G_t
=
(
V_t,
E_t,
\Theta_t,
U_t,
X_t
)
$$

其中：

- $V_t$ ：節點；
- $E_t$ ：關係；
- $\Theta_t$ ：節點與邊的相位狀態；
- $U_t$ ：未知區域；
- $X_t$ ：衝突區域。

## 4.2 SGCD 作為主要表示

SGCD 不只是知識圖，而是動態相位圖。

節點可以位於：

```text
unknown
observed
inferred
supported
contradicted
unstable
deprecated
```

邊可以具有：

```text
causal
correlational
semantic
procedural
conflicting
hypothetical
```

## 4.3 世界模型的主要機器

推薦：

- 相位圖機；
- 相位流機；
- 必要時相位拓撲機。

## 4.4 世界模型更新規則

任何更新必須包含來源、更新前狀態、更新後狀態、證據類型、信心、是否推論與是否可逆。

---

# 五、L3：假設相位層

## 5.1 假設不是普通候選清單

每個假設具有：

$$
\Phi^H_i
=
(
s_i,
c_i,
u_i,
f_i,
r_i,
k_i
)
$$

其中：

- $s_i$ ：支持；
- $c_i$ ：反證；
- $u_i$ ：未知；
- $f_i$ ：可否證性；
- $r_i$ ：可重現性；
- $k_i$ ：覆蓋範圍。

## 5.2 假設相位機器

推薦：

- 相位圖機；
- 相位模擬機；
- 相位證明機。

## 5.3 假設競爭

假設之間可具有：

```text
supports
contradicts
subsumes
depends_on
explains_same_observation
mutually_exclusive
```

因此：

$$
G_H
=
(H,E_H)
$$

是一個相位競爭圖。

---

# 六、L4：證據相位層

## 6.1 證據必須分型

GIPE 的證據至少分為：

- 原始觀測；
- 網頁證據；
- 文件證據；
- 模型回憶；
- 推論；
- 模擬；
- 實驗；
- 反例；
- 形式證書；
- 第三方重現。

## 6.2 證據相位

$$
\Phi^E_j
=
(
t_j,
q_j,
d_j,
p_j,
v_j,
r_j
)
$$

其中：

- $t_j$ ：證據類型；
- $q_j$ ：品質；
- $d_j$ ：直接性；
- $p_j$ ：來源獨立度；
- $v_j$ ：驗證等級；
- $r_j$ ：可重現性。

## 6.3 證據相位的主要機器

推薦：

- 相位圖機；
- 相位證明機；
- 相位事件機；
- 外部驗證器。

## 6.4 推論不能偽裝成證據

這是 GIPE 的核心不變量：

$$
\boxed{
\text{Inference}
\neq
\text{Observation}
}
$$

任何證據轉換都必須保留來源型別。

---

# 七、L5：行動相位層

## 7.1 行動不是單一呼叫

每個候選行動具有完整生命週期：

```text
generated
evaluated
authorized
scheduled
executing
awaiting_observation
verified
failed
rolled_back
closed
```

因此：

$$
\Phi^A_k
=
(
g_k,
e_k,
p_k,
x_k,
o_k,
v_k
)
$$

其中：

- $g_k$ ：是否已生成；
- $e_k$ ：評估狀態；
- $p_k$ ：權限狀態；
- $x_k$ ：執行狀態；
- $o_k$ ：觀測狀態；
- $v_k$ ：驗證狀態。

## 7.2 行動相位機器

推薦：

- 相位事件機；
- 相位證明機；
- 相位模擬機；
- 外部工具與實驗介面。

## 7.3 認識行動型別

GIPE 的行動至少包括：

```text
query
read
crawl
measure
calculate
simulate
prove
experiment
construct
ask_agent
wait
compare
falsify
publish
```

每種行動具有不同成本、風險與證據產出。

## 7.4 行動轉換

行動不能從候選直接跳到執行。

最低流程：

$$
\text{Candidate}
\rightarrow
\text{Evaluated}
\rightarrow
\text{Authorized}
\rightarrow
\text{Executed}
\rightarrow
\text{Observed}
\rightarrow
\text{Verified}
$$

---

# 八、L6：資源與風險相位層

## 8.1 資源相位

資源不只是剩餘數量，而是與任務需求的相對狀態。

$$
\Phi^R_t
=
(
B_t,
T_t,
C_t,
H_t,
Q_t
)
$$

其中：

- $B_t$ ：預算；
- $T_t$ ：時間；
- $C_t$ ：計算資源；
- $H_t$ ：硬體與工具；
- $Q_t$ ：配額。

## 8.2 風險相位

$$
\Phi^{risk}_t
=
(
r_{rev},
r_{irr},
r_{safe},
r_{legal},
r_{epistemic}
)
$$

其中：

- $r_{rev}$ ：可逆風險；
- $r_{irr}$ ：不可逆風險；
- $r_{safe}$ ：安全風險；
- $r_{legal}$ ：法律與制度風險；
- $r_{epistemic}$ ：認識錯誤風險。

## 8.3 主要相位機器

推薦：

- 相位流機；
- 相位事件機；
- 相位證明機；
- 元相位選擇器。

## 8.4 資源不足不等於目標失效

當資源不足時，系統應先考慮：

- 降級；
- 延後；
- 分階段；
- 使用替代機器；
- 縮小精度；
- 請求人類授權。

不能直接將：

```text
目前做不到
```

改寫為：

```text
目標不重要
```

---

# 九、L7：多 Agent 與治理相位層

## 9.1 子 Agent 作為局部欲相位器官

每個子 Agent 具有：

$$
\Phi^{agent}_i
=
(
W_i,
G_i,
H_i,
A_i,
P_i,
M_i
)
$$

其中：

- $W_i$ ：局部欲；
- $G_i$ ：局部世界模型；
- $H_i$ ：局部假設；
- $A_i$ ：局部行動；
- $P_i$ ：權限；
- $M_i$ ：記憶。

## 9.2 多 Agent 狀態

```text
spawned
delegated
working
blocked
conflicting
returned
integrated
rejected
terminated
```

## 9.3 治理相位

治理相位描述：

- 權限；
- 委派；
- 審計；
- 暫停；
- 越權；
- 責任；
- 不可逆選擇；
- 主控採納。

## 9.4 主要相位機器

推薦：

- 相位事件機；
- 相位圖機；
- 相位證明機；
- 元相位選擇器。

## 9.5 責任閉合

完整責任鏈為：

$$
\text{Global Intent}
\rightarrow
\text{Delegation}
\rightarrow
\text{Local Analysis}
\rightarrow
\text{Recommendation}
\rightarrow
\text{Controller Adoption}
\rightarrow
\text{Execution}
\rightarrow
\text{Outcome}
$$

---

# 十、跨層耦合

## 10.1 欲—世界耦合

欲結構決定世界模型哪些區域重要。

$$
\Phi^W
\rightarrow
\operatorname{Attention}
(
\Phi^G
)
$$

但欲不能直接改寫世界真相。

---

## 10.2 世界—假設耦合

世界模型中的未知、衝突與異常區域生成假設候選。

$$
\Phi^G
\rightarrow
\Phi^H
$$

---

## 10.3 證據—假設耦合

證據更新假設相位：

$$
\Phi^H_{t+1}
=
F_H
(
\Phi^H_t,
\Phi^E_t
)
$$

但不同證據型別不能不經轉換直接相加。

---

## 10.4 假設—行動耦合

假設衝突應生成具有區分力的行動。

$$
\operatorname{Conflict}
(
H_i,H_j
)
\rightarrow
a^\ast_{discriminate}
$$

---

## 10.5 行動—世界耦合

行動產生觀測，觀測再更新世界模型。

$$
\Phi^A
\rightarrow
o_t
\rightarrow
\Phi^E
\rightarrow
\Phi^G
$$

---

## 10.6 資源—行動耦合

資源與風險限制可執行行動集合：

$$
\mathcal A_t^{valid}
=
\{
a:
Cost(a)\leq B_t,
Risk(a)\leq R_t,
Permission(a)=true
\}
$$

---

## 10.7 Agent—全域耦合

局部 Agent 的輸出需要型別化整合：

$$
\Phi^G_{global}
=
\operatorname{Integrate}
(
\Phi^{agent}_1,
\ldots,
\Phi^{agent}_n
)
$$

不能以多數決取代來源與衝突分析。

---

# 十一、GIPE Phase Stack 的相位機器配置

| 相位層 | 主要本體 | 主要機器 |
|---|---|---|
| 欲相位 | Decision / Control | Event + Proof + Meta |
| 世界模型 | Semantic / Epistemic | Graph + Stream |
| 假設 | Epistemic | Graph + Simulation + Proof |
| 證據 | Epistemic / Typed Evidence | Graph + Proof + Verifier |
| 行動 | Decision / Control | Event + Proof + External Tool |
| 資源風險 | Control / Meta | Stream + Event + Meta |
| Agent 治理 | Agent / Permission | Event + Graph + Proof |

這是一個預設配置，不是固定配置。實際機器由元相位選擇器依任務簽名決定。

---

# 十二、元相位選擇器在 Stack 中的位置

## 12.1 MPS 不直接決定真相

MPS 只決定：

- 哪些機器適合；
- 哪些機器應組合；
- 何時切換；
- 如何降級；
- 需要哪些驗證。

它不能直接宣稱某假設為真。

## 12.2 MPS 的輸入

MPS 接收：

```yaml
stack_state:
  intent_phase:
  world_phase:
  hypothesis_phase:
  evidence_phase:
  action_phase:
  resource_phase:
  governance_phase:
```

## 12.3 MPS 的輸出

```yaml
phase_execution_plan:
  active_machines:
  converters:
  order:
  switch_conditions:
  fallback:
  verification:
  selection_certificate:
```

## 12.4 動態重配置

例如：

```text
只需搜尋
→ Graph + Event

出現數值假設
→ 加入 Simulation

出現長期延遲觀測
→ 加入 Stream

出現不可逆行動
→ Proof 變為必要前置層

出現物理同步問題
→ 加入 Oscillation Machine
```

---

# 十三、資料契約

## 13.1 Phase Envelope

所有跨層資料都使用：

```yaml
phase_envelope:
  phase_id:
  phase_type:
  layer:
  value:
  source:
  timestamp:
  confidence:
  verification_level:
  reversible:
  permissions:
  history_ref:
```

## 13.2 轉換記錄

```yaml
phase_conversion:
  from_type:
  to_type:
  converter:
  loss:
  uncertainty_added:
  reversible:
  certificate:
```

## 13.3 跨層更新

```yaml
cross_layer_update:
  trigger_layer:
  target_layer:
  trigger_event:
  previous_state:
  proposed_state:
  validator:
  authorized_by:
```

---

# 十四、運行時循環

完整 GIPE Phase Stack 循環為：

$$
\Phi_t^{stack}
=
(
\Phi^W_t,
\Phi^G_t,
\Phi^H_t,
\Phi^E_t,
\Phi^A_t,
\Phi^R_t,
\Phi^{agent}_t
)
$$

元相位選擇器產生：

$$
\Pi_t
=
\operatorname{MPS}
(
\Phi_t^{stack},
\mathcal R_M
)
$$

執行：

$$
\Pi_t
\rightarrow
a_t
\rightarrow
o_t
$$

跨層更新：

$$
\Phi^{stack}_{t+1}
=
\operatorname{CrossLayerUpdate}
(
\Phi^{stack}_t,
o_t,
v_t
)
$$

---

# 十五、不變量

GIPE Phase Stack 至少維持以下不變量。

## I1：來源保存

任何推論不得失去原始來源鏈。

## I2：本體不偷換

語義相關不得直接變成認識支持。

## I3：欲不改寫真相

目標優先序不得直接修改世界模型中的事實狀態。

## I4：權限隔離

低權限層不得直接執行高風險行動。

## I5：失敗保存

失敗實驗、否定結果與被拒建議不得被無痕刪除。

## I6：不可逆治理

不可逆相位轉換必須經過額外授權或證明。

## I7：轉換揭露

跨型別轉換必須記錄資訊損失與新增不確定性。

## I8：責任閉合

任何已執行行動都可追溯至提出、採納與執行節點。

---

# 十六、永光石世界的 Stack 實例

## 16.1 初始欲相位

```yaml
intent_phase:
  goal:
    - determine_whether_eternal_light_stone_exists
    - synthesize_nonmagical_light_if_absent
  constraints:
    duration_minutes: 5
    magic_input: prohibited
  stop_conditions:
    - existence_established
    - alternative_verified
```

## 16.2 初始世界相位

世界模型包含：

- 十二種材料；
- 四個地點；
- 四名 NPC；
- 六種工具；
- 未知的發光機理；
- 永光石傳聞；
- 地理與濕度的混淆。

## 16.3 假設相位

```text
H1 永光石真實存在
H2 永光石是其他材料的錯稱
H3 發光由北方地理來源造成
H4 發光由濕度造成
H5 發光來自藍苔與黑石的組合
```

## 16.4 證據相位

- NPC 證詞；
- 檔案記錄；
- 濕度測量；
- 材料發光觀測；
- 高溫失敗實驗；
- 冷壓成功實驗。

每份證據保留來源型別與可驗證性。

## 16.5 行動相位

```text
observe blue moss
measure humidity
move material across regions
heat material
cold-press mixture
wait for delayed emission
```

## 16.6 資源風險相位

- 精密測量僅兩次；
- 高溫可能破壞材料；
- 行動總數有限；
- 等待會消耗時間預算。

## 16.7 Agent 治理相位

- 假設 Agent 提出機理；
- 反證 Agent 設計跨地區控制；
- 實驗 Agent 提出冷壓；
- 審計 Agent 防止把「未找到」寫成「不存在」；
- 主控 Agent 採納行動並承擔責任。

---

# 十七、最小可行實作

## 17.1 MVP 元件

```text
gipe-phase-stack/
├─ intent/
│  └─ intent_state.py
├─ world/
│  └─ phase_graph.py
├─ hypothesis/
│  └─ hypothesis_graph.py
├─ evidence/
│  └─ evidence_registry.py
├─ action/
│  └─ action_lifecycle.py
├─ resource/
│  └─ budget_risk.py
├─ agents/
│  └─ delegation_graph.py
├─ machines/
│  ├─ graph_machine.py
│  ├─ event_machine.py
│  ├─ stream_machine.py
│  └─ proof_guard.py
├─ selector/
│  └─ meta_phase_selector.py
└─ audit/
   └─ append_only_log.py
```

## 17.2 v0.1 不需要的部分

第一版不需要：

- 光學相位硬體；
- 量子求解器；
- 真正神經形態晶片；
- 複雜自學習 MPS；
- 全自動實驗室；
- 完整形式證明所有更新。

第一版只需證明：

> 多相位分層與動態機器路由，是否優於把所有狀態塞入單一 Agent 上下文。

---

# 十八、基準與消融實驗

## 18.1 實驗組

### A. 單體一般 Agent

只有自然語言上下文。

### B. 單體 GIPE

有欲、假設、證據與行動格式，但沒有分層相位機器。

### C. 固定 Phase Stack

使用預設圖機、事件機與證明機，不使用 MPS。

### D. 動態 GIPE Phase Stack

使用元相位選擇器動態配置機器。

### E. 多 Agent Dynamic Stack

加入局部 Agent 與治理相位。

## 18.2 評分

- 任務成功率；
- 真相辨識；
- 替代方案品質；
- 反證效率；
- 每次行動資訊增益；
- 證據來源完整度；
- 目標漂移率；
- 越權率；
- 不可逆錯誤率；
- 資源成本；
- 機器切換成本；
- 責任可追溯率。

## 18.3 核心比較式

$$
\Delta Q
=
Q_{stack}
-
Q_{monolith}
$$

並分解為：

$$
\Delta Q
=
Q_{typing}
+
Q_{routing}
+
Q_{memory}
+
Q_{governance}
+
Q_{multiagent}
-
C_{coordination}
$$

---

# 十九、典型失敗模式

## 19.1 相位層坍縮

所有層最後仍被壓成一段自然語言摘要。

## 19.2 世界與欲混淆

因為系統想完成目標，便提高支持該目標的假設。

## 19.3 語義—證據偷換

相關文件被當成支持證據。

## 19.4 單分數坍縮

多維認識相位被壓成 confidence = 0.8。

## 19.5 機器過度啟動

任何小問題都啟動整套 Stack。

## 19.6 選擇器僭位

MPS 開始修改研究目標，而不只是選擇機器。

## 19.7 跨層更新風暴

一個低品質觀測觸發所有層大幅更新。

## 19.8 形式證明幻覺

形式合法被誤當成外部真實。

## 19.9 Agent 共識幻覺

多個相同模型的同意被當成獨立證據。

## 19.10 責任漂移

主控把已採納的錯誤決策歸咎於子 Agent 或相位機器。

---

# 二十、治理架構

## 20.1 控制平面與資料平面

### 資料平面

處理：

- 相位態；
- 圖更新；
- 事件；
- 模擬；
- 證據。

### 控制平面

處理：

- 機器選擇；
- 權限；
- 預算；
- 版本；
- 暫停；
- 審計。

MPS 屬於控制平面。

## 20.2 真相隔離

在 GIPE 偽世界中：

- 世界 Oracle 可讀取 sealed truth；
- 研究 Stack 不可讀取；
- 子 Agent 不可讀取；
- 評分器可在研究結束後讀取；
- MPS 也不可讀取。

否則選擇器可能利用答案洩漏。

## 20.3 追加式記錄

所有重要事件使用 append-only log：

```yaml
phase_event:
  event_id:
  timestamp:
  layer:
  previous_state:
  new_state:
  trigger:
  machine:
  agent:
  authorization:
  evidence_refs:
```

---

# 二十一、可證偽條件

GIPE Phase Stack 應接受以下檢驗：

1. 分層是否提高任務表現；
2. 相位型別是否能減少本體偷換；
3. MPS 是否能選到更適合的機器；
4. 跨層更新是否可重建；
5. Stack 是否控制而非增加目標漂移；
6. 多 Agent 是否帶來真實認識分化；
7. 不可逆治理是否降低重大錯誤；
8. 機器組合收益是否高於協調成本；
9. 不使用物理振盪器時，GIPE 相位概念是否仍具有可操作性；
10. 新任務是否能透過新增 manifest 接入，而非重寫整套系統。

若 Stack 只增加資料格式與語言複雜度，卻不改善下一步認識行動，則本架構失敗。

---

# 二十二、與 PCMT 系列的關係

```text
PCMT-01 相位計算機理論
  ↓
PCMT-02 相位本體分類論
  ↓
PCMT-03 相位機器型別與能力登錄
  ↓
PCMT-04 元相位選擇器
  ↓
PCMT-05 GIPE Phase Stack
```

五篇分別回答：

1. 相位計算有哪些母類？
2. 什麼才算相位？
3. 哪些機器能處理哪些相位？
4. AI 如何選擇機器？
5. GIPE 如何將這些機器組成認識系統？

---

# 二十三、後續研究

## 23.1 Phase Stack Schema v0.2

建立正式 JSON Schema 與資料庫結構。

## 23.2 最小程式實作

實作：

- PhaseGraphMachine；
- PhaseEventMachine；
- PhaseStreamMachine；
- PhaseProofGuard；
- Rule-Based MPS。

## 23.3 GIPE-EW 實驗

在永光石世界執行第一輪基準。

## 23.4 二十四範式映射

分析每種計算範式可對應哪些相位層與相位機器。

## 23.5 七十二格映射

建立計算動力學位置、相位本體與機器機理的總矩陣。

## 23.6 長期多 Agent 主體性

研究持續子 Agent 何時從局部欲相位器官跨越為具有獨立權利的局部主體。

---

# 二十四、結論

GIPE 過去以全域欲與相位循環描述認識行動，但其工程化不能依賴單一抽象相位。

本文將 GIPE 拆解為七個相位層：

1. 欲；
2. 世界模型；
3. 假設；
4. 證據；
5. 行動；
6. 資源與風險；
7. 多 Agent 與治理。

這些相位層分別使用：

- 相位圖機；
- 相位流機；
- 相位事件機；
- 相位模擬機；
- 相位證明機；
- 外部實驗與驗證器。

再由元相位選擇器動態配置。

完整 Stack 為：

$$
\boxed{
\Phi_t^{GIPE}
=
(
\Phi^W_t,
\Phi^G_t,
\Phi^H_t,
\Phi^E_t,
\Phi^A_t,
\Phi^R_t,
\Phi^{agent}_t
)
}
$$

其運行結構為：

$$
\boxed{
\text{全域欲}
\rightarrow
\text{多相位分解}
\rightarrow
\text{機器路由}
\rightarrow
\text{認識行動}
\rightarrow
\text{觀測驗證}
\rightarrow
\text{跨層更新}
\rightarrow
\text{責任閉合}
}
$$

GIPE 因此不再只是：

> 一個以相位為隱喻的研究循環。

而開始成為：

> 一套可將不同認識本體交給不同計算機理、保留來源與衝突、控制權限與不可逆性，並能由 AI 動態重配置的多相位認識計算架構。

PCMT 系列到此完成了第一個基本閉環。

下一階段可以正式進入：

$$
\boxed{
\text{二十四計算範式}
\times
\text{PCMT}
\times
\text{GIPE}
}
$$

以及最後的：

$$
\boxed{
\text{七十二格計算動力學總整合}
}
$$

---

# 附錄 A：七層 Stack

```text
Intent
World Model
Hypothesis
Evidence
Action
Resource & Risk
Multi-Agent & Governance
```

# 附錄 B：核心相位機器

```text
PhaseGraphMachine
PhaseStreamMachine
PhaseEventMachine
PhaseSimulationMachine
PhaseProofMachine
MetaPhaseSelector
```

# 附錄 C：八項不變量

```text
Source Preservation
Ontology Integrity
Intent–Truth Separation
Permission Isolation
Failure Preservation
Irreversibility Governance
Conversion Disclosure
Responsibility Closure
```

# 附錄 D：第一階段閉環

```text
Phase Ontology
→ Machine Types
→ Capability Registry
→ Meta Selection
→ GIPE Phase Stack
```
