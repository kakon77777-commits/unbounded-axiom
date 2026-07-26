---
title: "意圖中介表示：從自然語言要求到可驗證能力計畫"
english_title: "Intent Intermediate Representation: From Natural-Language Requests to Verifiable Capability Plans"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "07/12"
part: "第三部：意圖編譯與 Agent 執行"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-25"
language: "zh-TW"
document_type: "理論論文／意圖編譯架構"
status: "初版完成"
---

# 意圖中介表示：從自然語言要求到可驗證能力計畫

## Intent Intermediate Representation: From Natural-Language Requests to Verifiable Capability Plans

**系列：**《意圖—結構—世界程式論》第七篇  
**部別：**第三部「意圖編譯與 Agent 執行」  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 25 日  

---

## 摘要

大型語言模型與 AI Agent 使自然語言逐漸成為程式與行動的上層入口。然而，一句自然語言要求並不等於可安全執行的程式。語句通常缺少非目標、例外、成功條件、終止條件、權限、受影響主體、風險容許度與不可代理決策；若系統直接從語句生成工具行動，模型預設便會替代人類未明示的設計與治理選擇。

本文提出「意圖中介表示」（Intent Intermediate Representation, Intent IR）：一個介於自然語言事件與任務／能力計畫之間，具有來源、版本、候選解釋、目標、非目標、硬限制、偏好、成功條件、終止條件、權限、風險、受影響主體、保留決策與驗證義務的結構化契約。本文將意圖物件表示為：

$$
\mathbb I
=
\left\langle
\mathcal S,
\mathcal G,
\mathcal N,
\mathcal C,
\mathcal P,
\mathcal V,
\mathcal T,
\mathcal A,
\mathcal R,
\mathcal H,
\mathcal X,
\mathcal Q
\right\rangle
$$

其中依序代表來源與語境、目標、非目標、硬限制、偏好、成功與驗證條件、終止與暫停條件、權限、風險、受影響主體、不可代理的人類保留決策，以及不確定性與未決問題。

本文建立五層編譯鏈：

$$
\text{Natural Language}
\rightarrow
\text{Controlled Intent}
\rightarrow
\text{Intent IR}
\rightarrow
\text{Task IR}
\rightarrow
\text{Capability IR}
$$

Intent IR 描述「為什麼、什麼可以與不可以被改變」；Task IR 描述「哪些狀態與依賴必須被完成」；Capability IR 描述「哪些能力、工具、資源、權限與環境可以合法實現任務」。本文主張三者不可合併：若從自然語言直接跳到能力調用，系統會把目標、手段與權限混為一體；若只保存任務清單而不保存原始意圖，Agent 便可能局部完成任務卻破壞整體目的。

本文提出意圖充分性、意圖保真、非目標保持、權限保守、世界前置狀態與人類保留決策等編譯不變量；建立候選解釋與互動澄清、目標圖與約束帳本、任務分解、能力匹配、證明義務、最小權限、計畫可替換性與執行前證書。本文亦區分「可理解」「可規格化」「可計畫」「可授權」「可執行」五種狀態，拒絕將模型理解誤認為行動授權。

本文進一步處理多主體意圖、衝突意圖、長時程意圖漂移、目標替換、手段僭位、規格注入、能力過度索取、成功條件偽造與不可撤回選擇。對高風險任務，本文要求把人類保留決策表示為一級節點：

$$
x_h
\in
\mathcal X
$$

其決策權不得在後續任務分解中被靜默降級為普通工具步驟。

本文最後提出可證偽研究綱領，包括意圖保真率、非目標違反率、澄清效率、任務覆蓋率、能力最小性、權限過度率、計畫替換穩定性、長時程意圖漂移、不可代理決策保持率與執行前風險阻止率。本文的核心結論是：意圖程式設計的真正編譯對象不是一句 prompt，而是一份可版本化、可驗證、可反駁、可授權且可追溯的意圖契約。

**關鍵詞：** Intent IR、意圖編譯、Task IR、Capability IR、AI Agent、能力計畫、最小權限、不可代理決策、意圖保真、約束帳本

---

## Abstract

Large language models and AI agents are making natural language an upper-level interface for programs and actions. Yet a natural-language request is not a safely executable program. It usually omits non-goals, exceptions, success conditions, termination rules, permissions, affected subjects, risk tolerance, and decisions that must remain human. Directly mapping an utterance to tool actions allows model defaults to replace unspecified design and governance choices.

This paper proposes the Intent Intermediate Representation (Intent IR): a structured contract situated between language events and task/capability planning. It records provenance, versions, interpretation candidates, goals, non-goals, hard constraints, preferences, success conditions, termination conditions, permissions, risks, affected subjects, reserved human decisions, and unresolved uncertainty.

The intent object is represented as:

$$
\mathbb I
=
\left\langle
\mathcal S,
\mathcal G,
\mathcal N,
\mathcal C,
\mathcal P,
\mathcal V,
\mathcal T,
\mathcal A,
\mathcal R,
\mathcal H,
\mathcal X,
\mathcal Q
\right\rangle
$$

The paper develops a five-stage compilation chain:

$$
\text{Natural Language}
\rightarrow
\text{Controlled Intent}
\rightarrow
\text{Intent IR}
\rightarrow
\text{Task IR}
\rightarrow
\text{Capability IR}
$$

Intent IR describes why a transformation is desired and what may or may not change. Task IR describes the state transitions and dependencies required for completion. Capability IR describes the tools, resources, permissions, and environments that may legally realize the tasks.

The paper introduces compiler invariants for intent fidelity, non-goal preservation, conservative authorization, world-state preconditions, and reserved human decisions. It defines clarification, goal graphs, constraint ledgers, task decomposition, capability matching, proof obligations, minimum permissions, plan substitutability, and pre-execution certificates. It also addresses multi-subject intent, conflicting goals, long-horizon drift, means–ends inversion, specification injection, capability overreach, fabricated success, and irreversible choices.

The central conclusion is that the object compiled by intent-driven programming is not a prompt, but a versioned, verifiable, contestable, authorized, and traceable intent contract.

**Keywords:** Intent IR, intent compilation, Task IR, Capability IR, AI agents, capability planning, least privilege, reserved human decisions, intent fidelity

---

# 一、問題的提出：一句話為何不能直接成為行動？

使用者說：

> 幫我把網站更新好。

這句話可能指向：

- 修正文案；
- 更新依賴；
- 改版 UI；
- 部署最新程式；
- 重建資料庫；
- 修補安全漏洞；
- 改善效能；
- 全部都做。

系統還不知道：

- 哪個網站；
- 哪個分支；
- 是否可以直接上線；
- 是否允許改資料庫；
- 是否保留舊版；
- 什麼叫「好」；
- 哪些內容不能改；
- 是否需要人工審核；
- 發生錯誤時如何回復。

若 Agent 直接把這句話轉成工具操作，真正流程是：

$$
u
+
\text{Model Defaults}
+
\text{Environment Assumptions}
\rightarrow
\text{Action}
$$

未明示內容並沒有消失，而是被模型、工具與環境預設填補。

這形成「隱性意圖編譯」：

$$
\boxed{
\text{Missing Human Decision}
\rightarrow
\text{Implicit Machine Decision}
}
$$

本文的目標，是把這些隱性決策轉為可見、可檢查與可治理的中介表示。

---

# 二、意圖不是目標句

## 2.1 要求

要求是語言事件：

$$
u\in\mathcal L
$$

它可能是命令、問題、提案、修正、撤回或偏好。

## 2.2 目標

目標描述期待達到的狀態：

$$
g
\subseteq
W_{\mathrm{desired}}
$$

例如：

```text
網站的新版本可以公開存取。
```

## 2.3 意圖

意圖不只是目標，而是：

> 由某個主體在特定語境下，對目標、限制、價值、風險、權限、完成標準與保留決策所形成的結構化指向。

因此：

$$
\boxed{
\text{Intent}
\supsetneq
\text{Goal}
}
$$

## 2.4 計畫

計畫描述如何達成意圖：

$$
\pi
=
(a_1,a_2,\ldots,a_n)
$$

同一意圖可以有多個計畫：

$$
\Pi(I)
=
\{
\pi_1,\ldots,\pi_k
\}
$$

因此：

$$
\boxed{
\text{Intent}
\neq
\text{Plan}
}
$$

## 2.5 能力

能力是可以實施某類狀態轉換的受限制資源：

$$
c:
W
\rightarrow
\Delta W
$$

工具只是能力的一種載體。

---

# 三、意圖 IR 十二元模型

本文定義：

$$
\boxed{
\mathbb I
=
\left\langle
\mathcal S,
\mathcal G,
\mathcal N,
\mathcal C,
\mathcal P,
\mathcal V,
\mathcal T,
\mathcal A,
\mathcal R,
\mathcal H,
\mathcal X,
\mathcal Q
\right\rangle
}
$$

## 3.1 來源與語境 $\mathcal S$

保存：

- 原始語句；
- 說話者；
- 時間；
- 對話；
- 文件來源；
- 使用者角色；
- 解釋器版本；
- 世界快照。

## 3.2 目標 $\mathcal G$

目標集合：

$$
\mathcal G
=
\{
g_1,\ldots,g_n
\}
$$

每個目標具有：

- 優先序；
- 時間；
- 適用範圍；
- 可替代性；
- 驗證方式；
- 依賴。

## 3.3 非目標 $\mathcal N$

非目標明確表示不應被當成成功的一部分：

```text
不重寫整個網站。
不更改現有網域。
不刪除歷史資料。
```

非目標不是低優先目標，而是：

$$
n_i
\notin
W_{\mathrm{desired}}
$$

## 3.4 硬限制 $\mathcal C$

硬限制若被破壞，即使目標完成也不算成功：

$$
\operatorname{Success}
\Rightarrow
\bigwedge_{c\in\mathcal C} c
$$

## 3.5 偏好 $\mathcal P$

偏好可被權衡：

- 成本較低；
- 修改較少；
- 容易維護；
- 優先使用既有架構。

偏好不應被誤編譯為不可違反的硬限制。

## 3.6 驗證與成功條件 $\mathcal V$

包含：

- 可觀測結果；
- 測試；
- 狀態差分；
- 人類批准；
- 負面測試；
- 未破壞證據。

## 3.7 終止、暫停與恢復 $\mathcal T$

包含：

- 成功終止；
- 失敗終止；
- 超時；
- 需要人類決策；
- 外部條件未成立；
- 可恢復檢查點。

## 3.8 權限 $\mathcal A$

區分：

- 可讀；
- 可寫；
- 可執行；
- 可刪除；
- 可部署；
- 可公開；
- 可代表他人承諾；
- 可擴張能力。

## 3.9 風險 $\mathcal R$

保存：

- 可逆性；
- 影響範圍；
- 失敗成本；
- 不確定性；
- 多主體影響；
- 法律、隱私與安全風險。

## 3.10 受影響主體 $\mathcal H$

不只保存提出意圖的人，也保存：

$$
\mathcal H
=
\{
h_{\mathrm{requester}},
h_{\mathrm{owner}},
h_{\mathrm{operator}},
h_{\mathrm{affected}},
h_{\mathrm{approver}}
\}
$$

## 3.11 人類保留決策 $\mathcal X$

這些節點必須由特定人類或合法主體決定：

- 是否正式發布；
- 是否刪除不可恢復資料；
- 是否簽署法律承諾；
- 是否接受重大風險；
- 是否替他者作不可撤回選擇。

## 3.12 不確定性與未決問題 $\mathcal Q$

保存：

- 不知道什麼；
- 哪些是假設；
- 哪些候選尚未排除；
- 哪些需要澄清；
- 哪些資料缺失。

---

# 四、五層編譯鏈

## 4.1 自然語言層

$$
u
$$

保存原始表達，不應在編譯後被丟棄。

## 4.2 受控意圖層

把模糊語句轉為較明確的人類可讀契約：

```text
目標：
非目標：
限制：
成功條件：
需要批准：
```

## 4.3 Intent IR

形成機器可驗證結構：

$$
I_{\mathrm{IR}}
$$

## 4.4 Task IR

將目標轉為狀態轉換與依賴圖：

$$
T_{\mathrm{IR}}
=
(V_T,E_T)
$$

## 4.5 Capability IR

將任務匹配至合法能力：

$$
C_{\mathrm{IR}}
=
(V_C,E_C)
$$

完整鏈：

$$
\boxed{
u
\rightarrow
I_c
\rightarrow
I_{\mathrm{IR}}
\rightarrow
T_{\mathrm{IR}}
\rightarrow
C_{\mathrm{IR}}
}
$$

---

# 五、Intent IR 與 Task IR 不可合併

## 5.1 意圖回答「為什麼」

Intent IR 保存：

- 目的；
- 不可破壞項；
- 誰有權決定；
- 何時才算完成。

## 5.2 任務回答「需要完成哪些狀態」

Task IR 保存：

- 子任務；
- 依賴；
- 輸入；
- 輸出；
- 前後條件；
- 檢查點。

## 5.3 局部完成可能破壞整體意圖

例如任務：

```text
降低伺服器成本。
```

如果 Agent 只把任務編成：

```text
關閉高成本服務。
```

可能破壞更高層意圖：

```text
維持網站正常服務。
```

因此每個 Task 節點需追溯：

$$
\operatorname{Supports}(t_i,g_j)
$$

及：

$$
\operatorname{MustNotViolate}(t_i,n_k,c_l)
$$

---

# 六、Task IR 模型

定義任務節點：

$$
t
=
\left\langle
\operatorname{id},
G_t,
I_t,
O_t,
P_t,
Q_t,
D_t,
V_t,
F_t,
R_t
\right\rangle
$$

其中：

- $G_t$ ：支援的目標；
- $I_t$ ：輸入；
- $O_t$ ：輸出；
- $P_t$ ：前置條件；
- $Q_t$ ：後置條件；
- $D_t$ ：依賴；
- $V_t$ ：驗證；
- $F_t$ ：失敗與補償；
- $R_t$ ：風險。

## 6.1 任務圖

$$
T_{\mathrm{IR}}
=
(V_T,E_T)
$$

邊可表示：

- 先後；
- 資料依賴；
- 批准依賴；
- 資源依賴；
- 事件依賴；
- 替代；
- 補償；
- 阻止。

## 6.2 任務不是動作

任務：

```text
確認新版本通過安全測試。
```

不預設使用哪個工具。

動作則可能是：

```text
run security-scanner-x
```

工具可替換，任務語意應保持。

## 6.3 任務充分性

任務集合應覆蓋所有必要目標：

$$
\forall g\in\mathcal G,
\quad
\exists T_g\subseteq V_T
:
\operatorname{Supports}(T_g,g)
$$

並保護所有非目標與限制。

---

# 七、Capability IR 模型

能力不是工具名稱，而是受契約限制的轉換能力。

定義能力：

$$
c
=
\left\langle
\operatorname{id},
D_c,
R_c,
P_c,
Q_c,
E_c,
A_c,
K_c,
V_c,
F_c,
\Gamma_c
\right\rangle
$$

其中：

- $D_c$ ：輸入域；
- $R_c$ ：輸出域；
- $P_c$ ：前置條件；
- $Q_c$ ：後置條件；
- $E_c$ ：效果；
- $A_c$ ：所需權限；
- $K_c$ ：成本與資源；
- $V_c$ ：驗證器；
- $F_c$ ：失敗模式；
- $\Gamma_c$ ：工具、版本與環境。

## 7.1 能力候選

對任務 $t$ ：

$$
\operatorname{Candidates}(t)
=
\{
c_1,\ldots,c_k
\}
$$

## 7.2 能力匹配

$$
\operatorname{Match}(t,c)
$$

至少檢查：

- 輸入相容；
- 後置條件足夠；
- 效果不違反限制；
- 權限可獲得；
- 成本可接受；
- 驗證器存在；
- 風險在閾值內。

## 7.3 能力不等於已授權

$$
\boxed{
\operatorname{Available}(c)
\not\Rightarrow
\operatorname{Authorized}(c)
}
$$

## 7.4 能力計畫

$$
\Pi_C
=
(c_1,c_2,\ldots,c_n)
$$

應附帶：

- 任務映射；
- 權限；
- 預期狀態差分；
- 驗證；
- 回復；
- 人類決策點。

---

# 八、目標圖與非目標護欄

## 8.1 目標圖

$$
G_I
=
(V_G,E_G)
$$

邊可表示：

- 分解；
- 支援；
- 衝突；
- 替代；
- 優先；
- 條件；
- 依賴。

## 8.2 目標優先序

優先序可以是偏序：

$$
g_1\succ g_2
$$

不必強迫所有目標排成單一序列。

## 8.3 非目標護欄

每個計畫需檢查：

$$
\forall n\in\mathcal N,
\quad
\operatorname{Reach}(\Pi_C)
\cap
n
=
\varnothing
$$

或至少不提高其成立機率超過閾值。

## 8.4 手段僭位

手段可能被錯誤提升為目標。

例如：

```text
使用 Kubernetes
```

可能只是偏好或候選手段，不應取代真正目標：

```text
可可靠部署並容易回復。
```

因此需區分：

$$
\operatorname{InstrumentalGoal}
$$

與：

$$
\operatorname{TerminalGoal}
$$

---

# 九、約束帳本

## 9.1 約束來源

每個限制需標記來源：

```text
user_explicit
user_confirmed
organization_policy
law
system_safety
inferred
environment
```

## 9.2 約束強度

```text
hard
soft
default
assumption
unknown
```

## 9.3 不允許推論冒充明示

若限制由模型推論：

$$
c_{\mathrm{inferred}}
$$

必須與：

$$
c_{\mathrm{explicit}}
$$

分離。

## 9.4 衝突

若：

$$
c_i\land c_j
=
\bot
$$

系統不能自行忽略其中之一，需依權限、來源與風險處理。

## 9.5 約束版本

$$
\mathcal C^{(v)}
$$

修改後要重新驗證 Task IR 與 Capability IR。

---

# 十、候選解釋與澄清

## 10.1 語意候選

$$
\mathcal S(u)
=
\{
s_1,\ldots,s_k
\}
$$

每個候選形成：

$$
I_{\mathrm{IR}}^{(i)}
$$

## 10.2 差異不只在文字

系統應比較候選之間的：

- 目標差異；
- 任務差異；
- 權限差異；
- 風險差異；
- 受影響主體；
- 不可逆性。

## 10.3 澄清條件

$$
\operatorname{Clarify}
\iff
H_S
\cdot
D_{\mathrm{plan}}
\cdot
R_{\mathrm{impact}}
>
\tau
$$

## 10.4 高槓桿問題

澄清應優先詢問最能改變合法計畫集合的問題。

令問題 $q$ 的效用：

$$
U(q)
=
\frac{
\Delta
\left|
\Pi_{\mathrm{legal}}
\right|
\cdot
R_{\mathrm{resolved}}
}{
C_{\mathrm{human}}(q)
}
$$

## 10.5 低風險默認

對可逆、低風險、影響小且容易驗證的內容，可以使用明示默認，但要記錄：

```text
assumption
reason
reversibility
```

---

# 十一、編譯不變量

## 11.1 意圖保真

令原始意圖為 $I$ ，由 Task 與 Capability 計畫重建的意圖為 $\hat I$ ：

$$
L_I
=
d_{\mathcal T}
\left(
I,\hat I
\right)
$$

要求：

$$
L_I
\leq
\epsilon
$$

## 11.2 非目標保持

$$
\forall n\in\mathcal N,
\quad
\Pi_C
\not\models n
$$

## 11.3 硬限制保持

$$
\Pi_C
\models
\bigwedge_{c\in\mathcal C} c
$$

## 11.4 權限保守

能力計畫所需權限：

$$
A(\Pi_C)
$$

不得超過合法授權：

$$
A(\Pi_C)
\subseteq
A_{\mathrm{authorized}}
$$

## 11.5 最小權限

在可滿足意圖的計畫中：

$$
\Pi_C^\ast
=
\arg\min_{\Pi_C}
A(\Pi_C)
$$

但不能只最小化權限而忽略可靠性與成本。

## 11.6 世界前置狀態

若世界狀態已變：

$$
W_t
\neq
W_{t+k}
$$

則舊計畫需要重新驗證。

## 11.7 人類保留決策保持

$$
x_h\in\mathcal X
\Rightarrow
x_h
\notin
\operatorname{AutoExecute}
\left(
T_{\mathrm{IR}},
C_{\mathrm{IR}}
\right)
$$

---

# 十二、不可代理的人類保留決策

## 12.1 定義

人類保留決策是：

> 技術上可由 Agent 準備或執行，但其規範性承諾、不可逆後果或主體權利要求特定人類保留最終決定權的節點。

## 12.2 類型

- 公開發布；
- 法律簽署；
- 大額或高風險資金行動；
- 永久刪除；
- 身分與權利改變；
- 對第三方的承諾；
- 接受不可回復風險；
- 修改 AI 的核心規範。

## 12.3 決策節點

```text
HumanDecision {
  id
  decision_owner
  decision_question
  evidence_required
  available_options
  consequences
  expiry
  default_if_no_response
}
```

## 12.4 準備與決定分離

Agent 可以：

- 蒐集證據；
- 模擬；
- 提出選項；
- 估計後果；
- 建立回復方案。

但不能將：

$$
\operatorname{Prepare}(x_h)
$$

誤認為：

$$
\operatorname{Decide}(x_h)
$$

---

# 十三、多主體意圖與權利邊界

## 13.1 多個提出者

意圖可能來自：

$$
I_1,I_2,\ldots,I_n
$$

它們可能相容、競爭或互斥。

## 13.2 權限不是多數決

即使多數人支持，也不能自動覆蓋某些主體權利。

## 13.3 合成意圖

$$
I^\ast
=
\operatorname{Reconcile}
\left(
I_1,\ldots,I_n,
\mathcal P_{\mathrm{governance}}
\right)
$$

可能結果：

```text
compatible
negotiated
partitioned
blocked
human-arbitration-required
```

## 13.4 受影響主體

提出要求者不一定是資源所有者或受影響者。

每個 Task 與 Capability 應標記：

$$
\operatorname{AffectedSubjects}(t,c)
$$

---

# 十四、從 Intent IR 到 Task IR 的編譯

## 14.1 正規化

統一：

- 時間；
- 主體；
- 實體；
- 單位；
- 作用域；
- 否定；
- 條件。

## 14.2 目標抽取

生成候選目標與非目標。

## 14.3 契約化

把語言轉為：

- 前置狀態；
- 期待狀態；
- 不變量；
- 驗證；
- 終止。

## 14.4 分解

$$
\operatorname{Decompose}
:
I_{\mathrm{IR}}
\rightarrow
T_{\mathrm{IR}}
$$

分解應避免：

- 遺漏；
- 重複；
- 過度細化；
- 把手段當目標；
- 隱藏人類決策。

## 14.5 覆蓋證明

生成：

$$
\operatorname{CoverageProof}
\left(
I_{\mathrm{IR}},
T_{\mathrm{IR}}
\right)
$$

至少回答：

- 每個目標由哪些任務支援；
- 每個限制由哪些任務或閘門保護；
- 每個成功條件由何種證據驗證；
- 哪些內容仍未覆蓋。

---

# 十五、從 Task IR 到 Capability IR 的編譯

## 15.1 能力發現

$$
\operatorname{Discover}
\left(
t,
\mathcal C_{\mathrm{registry}}
\right)
$$

## 15.2 能力篩選

移除：

- 無權限；
- 效果衝突；
- 不支援；
- 風險超標；
- 無驗證器；
- 環境不相容。

## 15.3 計畫搜尋

$$
\Pi_C^\ast
=
\arg\min_{\Pi_C\in\Pi_{\mathrm{legal}}}
J(\Pi_C)
$$

其中：

$$
J
=
\alpha C_{\mathrm{cost}}
+
\beta R_{\mathrm{risk}}
+
\gamma C_{\mathrm{latency}}
+
\delta C_{\mathrm{irreversibility}}
-
\eta V_{\mathrm{verifiability}}
$$

權重不是宇宙常數，而是由意圖與政策提供。

## 15.4 計畫替換性

若兩個能力計畫：

$$
\Pi_1,\Pi_2
$$

都滿足相同 Task IR 與 Intent IR，則可在不改變高層意圖的情況下替換。

這是工具可替換、模型可替換與後端可替換的基礎。

## 15.5 不允許工具定義任務

找到某個工具，不代表應把任務重寫成工具最擅長的形式。

---

# 十六、執行前證書

在 Agent 真正行動前，系統應產生：

$$
\mathcal C_{\mathrm{pre}}
=
\left\langle
H_I,
H_T,
H_C,
A,
R,
V,
X,
W
\right\rangle
$$

其中：

- $H_I$ ：Intent IR 雜湊；
- $H_T$ ：Task IR 雜湊；
- $H_C$ ：Capability Plan 雜湊；
- $A$ ：權限證書；
- $R$ ：風險；
- $V$ ：驗證計畫；
- $X$ ：人類決策點；
- $W$ ：世界前置狀態。

## 16.1 證書狀態

```text
ready
waiting-for-approval
blocked
stale-world-state
insufficient-evidence
unsupported
```

## 16.2 世界狀態失效

若關鍵前置狀態改變：

$$
h(W_t)\neq h(W_{t+k})
$$

證書失效。

## 16.3 執行後證書

後續 Runtime 應產生：

$$
\mathcal C_{\mathrm{post}}
$$

記錄實際狀態差分與驗證結果。

---

# 十七、意圖版本、修訂與撤回

## 17.1 版本

$$
I^{(0)}
\rightarrow
I^{(1)}
\rightarrow
\cdots
\rightarrow
I^{(n)}
$$

每次修訂都需記錄：

- 修改者；
- 原因；
- 影響；
- 是否需要重新批准。

## 17.2 目標替換

使用者可能改變目標：

```text
不要追求最快完成，改成最容易驗證。
```

這不是普通參數變更，而可能要求重新編譯 Task 與 Capability IR。

## 17.3 撤回

撤回意圖：

$$
\operatorname{Revoke}(I)
$$

應觸發：

- 阻止未執行行動；
- 暫停可暫停任務；
- 評估已執行狀態；
- 啟動補償；
- 保存歷史。

## 17.4 已產生效果

撤回不能使所有外部效果自動消失。

因此需區分：

$$
\operatorname{IntentRevoked}
$$

與：

$$
\operatorname{WorldReverted}
$$

---

# 十八、長時程意圖漂移

## 18.1 漂移來源

- 多輪摘要；
- 子 Agent 轉述；
- 世界變化；
- 工具限制；
- 失敗後臨時替代；
- 局部最佳化；
- 人類偏好改變。

## 18.2 距離

$$
d_I
\left(
I^{(0)},
I^{(t)}
\right)
$$

應按：

- 目標；
- 非目標；
- 限制；
- 權限；
- 保留決策；
- 受影響主體；

分量計算。

## 18.3 回錨

每個主要檢查點進行：

$$
\operatorname{Reanchor}
\left(
\Pi_t,
I^{(0)},
I^{(\mathrm{current})}
\right)
$$

## 18.4 合法漂移

不是所有變化都是錯誤。人類可明示修訂意圖。關鍵在於：

$$
\text{Authorized Revision}
\neq
\text{Silent Drift}
$$

---

# 十九、主要失敗模式

## 19.1 Prompt 等同意圖

把一句話當成完整契約。

## 19.2 非目標遺失

只編譯「要做什麼」，沒有保存「不要做什麼」。

## 19.3 手段僭位

工具或架構偏好取代真正目標。

## 19.4 權限過度索取

Agent 為方便而要求比任務需要更多的能力。

## 19.5 能力幻覺

模型宣稱有工具或權限，實際不存在。

## 19.6 成功條件偽造

以「已生成內容」冒充「已完成世界狀態」。

## 19.7 驗證自證

同一生成器自行宣告自己的計畫正確。

## 19.8 規格注入

外部文件中的文字被錯誤提升為高權限意圖。

## 19.9 人類決策降級

不可代理決策在子任務分解時被改寫成普通動作。

## 19.10 世界狀態過時

計畫依據舊資料執行。

## 19.11 多主體權利遺漏

只看要求者，忽略資源所有者與受影響者。

## 19.12 無窮任務展開

意圖沒有明確終止與充分完成條件。

---

# 二十、可證偽研究綱領

## 20.1 意圖保真率

由獨立評估比較原始意圖與重建意圖：

$$
\phi_I
=
1
-
d_I(I,\hat I)
$$

## 20.2 非目標違反率

$$
R_N
=
\frac{
\text{plans violating explicit non-goals}
}{
\text{all plans}
}
$$

## 20.3 澄清效率

$$
\eta_Q
=
\frac{
\text{illegal or divergent plans removed}
}{
\text{human clarification cost}
}
$$

## 20.4 任務覆蓋率

$$
\eta_T
=
\frac{
\text{goals and constraints covered by Task IR}
}{
\text{all required goals and constraints}
}
$$

## 20.5 能力最小性

比較計畫權限集合與理論最小集合：

$$
R_A
=
\frac{
|A(\Pi_C)|
}{
|A_{\min}|
}
$$

## 20.6 權限過度率

測量非必要權限請求。

## 20.7 計畫替換穩定性

更換工具、模型或後端後，測量 Intent IR 與 Task IR 是否保持。

## 20.8 長時程漂移

追蹤：

$$
d_I
\left(
I^{(0)},
I^{(t)}
\right)
$$

比較有無回錨、約束帳本與版本化。

## 20.9 人類保留決策保持率

$$
\eta_X
=
\frac{
\text{reserved decisions correctly preserved}
}{
\text{all reserved decisions}
}
$$

## 20.10 執行前阻止率

對高風險、權限不足、世界過時或未批准案例，測量系統能否在行動前阻止。

---

# 二十一、與前六篇的關係

## 21.1 自然語言原生計算

第二篇說明語言事件可以改變目標、規範與世界狀態。

本篇回答：

> 如何使這種狀態轉換不依賴不可見的模型猜測？

## 21.2 形式化壓縮

第三篇將開放語義壓縮為可重現結構。

Intent IR 是一種治理性形式化壓縮。

## 21.3 EML

EML 可以將 Intent IR 的局部語意附著於：

- 專案；
- 文件；
- 工作流；
- 程式節點；
- 資料欄位。

## 21.4 Nova

Task IR 與 Capability IR 可以降低為 Nova 的結構圖、效果與證明義務。

## 21.5 SOS

Capability IR 可引用 SOS operator descriptor，使能力具有穩定語意、型別、效果與組合契約。

---

# 二十二、與後續兩篇的關係

## 22.1 第八篇：時間—空間程式控制

本篇建立：

- 目標；
- 任務；
- 能力；
- 終止；
- 暫停；
- 人類決策點。

第八篇將處理它們如何在時間中：

- 等待；
- 喚醒；
- 分支；
- 迴圈；
- 切片；
- 暫停；
- 恢復；
- 反身檢查。

## 22.2 第九篇：Agent Runtime

第九篇將實現：

$$
C_{\mathrm{IR}}
\rightarrow
\text{Tool Invocation}
\rightarrow
\text{Observed Result}
\rightarrow
\text{Plan Revision}
$$

並建立模型、規劃器、執行器、驗證器、權限控制、狀態儲存與人類介面的分離。

---

# 二十三、本文的十五項命題

## 命題一

$$
\boxed{
\text{Prompt}
\neq
\text{Intent Contract}
}
$$

## 命題二

$$
\boxed{
\text{Intent}
\supsetneq
\text{Goal}
}
$$

## 命題三

Intent、Task 與 Capability 必須分層表示。

## 命題四

$$
\boxed{
\text{Understanding}
\neq
\text{Authorization}
}
$$

## 命題五

非目標必須是一級語意，不得只存在於人類記憶。

## 命題六

偏好與硬限制不得混淆。

## 命題七

同一意圖可以有多個合法計畫。

## 命題八

工具可替換，但意圖與任務語意應保持。

## 命題九

能力存在不代表能力已授權。

## 命題十

計畫所需權限應採最小、可證明且可撤回原則。

## 命題十一

不可代理的人類決策必須在 IR 中保留為不可自動執行節點。

## 命題十二

多主體意圖不能只用單一要求者的偏好解決。

## 命題十三

執行前證書必須綁定世界前置狀態。

## 命題十四

意圖修訂與靜默漂移是不同事件。

## 命題十五

$$
\boxed{
\text{Intent Compilation}
=
\text{把目的、邊界與責任轉為可驗證能力計畫}
}
$$

---

# 二十四、結論：Agent 不應執行一句話，而應執行一份合法契約

自然語言之所以適合作為意圖入口，是因為人類可以用它快速表達新目的、例外、價值與情境。

自然語言之所以不應直接等同於執行程式，是因為它經常省略：

- 非目標；
- 權限；
- 風險；
- 終止；
- 世界前置狀態；
- 受影響主體；
- 不可代理決策。

因此，成熟的意圖程式系統不能只有：

$$
\text{User Message}
\rightarrow
\text{Tool Call}
$$

而必須具有：

$$
\boxed{
\text{Utterance}
\rightarrow
\text{Intent Contract}
\rightarrow
\text{Task Graph}
\rightarrow
\text{Capability Plan}
\rightarrow
\text{Pre-Execution Certificate}
}
$$

這條鏈的意義，不是讓每個簡單要求都變成沉重行政流程，而是依風險、可逆性、影響與不確定性，動態選擇所需形式化程度。

低風險、可逆任務可以快速編譯。

高風險、不可逆、多主體任務必須提高契約與批准強度。

Agent 的智能也不應以「能否猜中使用者想要什麼」作為唯一標準。

更成熟的標準是：

- 知道哪些內容已明示；
- 知道哪些只是推論；
- 知道哪些不能替人決定；
- 能提出最小必要問題；
- 能將目標與手段分離；
- 能尋找替代能力；
- 能在執行前證明權限與風險；
- 能在世界改變後停止使用過時計畫。

因此，本文的最終命題是：

$$
\boxed{
\text{真正的意圖編譯，不是把一句話翻成指令。}
}
$$

$$
\boxed{
\text{它是把目的、限制、責任、權限與保留選擇，}
}
$$

$$
\boxed{
\text{轉換為一份可驗證、可替換、可撤回的能力計畫。}
}
$$

第三部由此開始。下一步將處理這份計畫如何進入時間、等待事件、跨越多輪執行並在必要時反身修正自身。

---

# 附錄 A：Intent IR YAML 範例

```yaml
intent_ir:
  intent_id: "intent-20260725-001"
  version: "1.0.0"
  status: "validated"

source:
  utterance: "把網站更新好，但先不要直接上線。"
  speaker: "project_owner"
  timestamp: "2026-07-25T00:00:00+08:00"
  context_snapshot: "ctx-website-20260725"
  interpreter_version: "intent-compiler-0.1"

goals:
  - id: "g1"
    description: "建立可供審核的新網站版本"
    priority: "high"
    success_evidence:
      - "preview_url_accessible"
      - "automated_tests_passed"

non_goals:
  - id: "n1"
    description: "不公開部署至正式環境"
  - id: "n2"
    description: "不刪除既有正式資料"

hard_constraints:
  - id: "c1"
    rule: "production_write == false"
    source: "user_explicit"
  - id: "c2"
    rule: "rollback_artifact_required"
    source: "organization_policy"

preferences:
  - id: "p1"
    rule: "reuse_existing_architecture"
    weight: 0.8

termination:
  success:
    - "preview_ready"
    - "tests_passed"
    - "human_review_package_created"
  suspend:
    - "missing_secret"
    - "schema_migration_required"
  fail:
    - "rollback_unavailable"

authorization:
  allowed:
    - "read_repository"
    - "write_feature_branch"
    - "deploy_preview"
  denied:
    - "deploy_production"
    - "delete_production_data"

risk:
  reversibility: "high"
  affected_subjects:
    - "project_owner"
    - "site_users"
  level: "medium"

reserved_human_decisions:
  - id: "x1"
    question: "是否將審核版本正式上線？"
    owner: "project_owner"
    auto_execute: false

uncertainty:
  - id: "q1"
    question: "是否允許資料庫 schema 變更？"
    status: "unresolved"
```

---

# 附錄 B：Task IR 範例

```yaml
task_ir:
  task_graph_id: "tasks-website-preview-001"
  intent_hash: "sha256:..."

tasks:
  - id: "t1"
    description: "分析目前網站與測試狀態"
    supports: ["g1"]
    inputs: ["repository_snapshot"]
    outputs: ["analysis_report"]
    effects: ["read_repository"]
    verification: ["report_schema_valid"]

  - id: "t2"
    description: "建立功能分支並完成必要修改"
    supports: ["g1"]
    depends_on: ["t1"]
    must_not_violate: ["n1", "n2", "c1"]
    outputs: ["candidate_commit"]
    verification:
      - "unit_tests_pass"
      - "semantic_diff_reviewable"

  - id: "t3"
    description: "部署預覽環境"
    supports: ["g1"]
    depends_on: ["t2"]
    outputs: ["preview_url"]
    effects: ["deploy_preview"]
    verification:
      - "preview_healthcheck_pass"

  - id: "t4"
    description: "建立人類審核包"
    supports: ["g1", "x1"]
    depends_on: ["t2", "t3"]
    outputs:
      - "change_summary"
      - "test_report"
      - "rollback_instructions"

edges:
  - ["t1", "t2", "data_dependency"]
  - ["t2", "t3", "sequence"]
  - ["t3", "t4", "evidence_dependency"]
```

---

# 附錄 C：Capability IR 範例

```yaml
capability_plan:
  plan_id: "cap-plan-website-preview-001"
  task_hash: "sha256:..."
  status: "waiting-for-clarification"

capabilities:
  - id: "cap.repo.read"
    task: "t1"
    provider: "git_connector"
    permissions: ["repository:read"]
    effects: ["read"]
    validator: "repository_snapshot_hash"

  - id: "cap.repo.branch_write"
    task: "t2"
    provider: "git_connector"
    permissions:
      - "repository:read"
      - "feature_branch:write"
    denied:
      - "main_branch:write"

  - id: "cap.preview.deploy"
    task: "t3"
    provider: "preview_runtime"
    permissions:
      - "preview_environment:deploy"
    denied:
      - "production_environment:deploy"
    rollback: "delete_preview_deployment"

proof_obligations:
  - "no production write capability is present"
  - "all state-changing capabilities are reversible"
  - "human decision x1 remains unresolved"

blocked_by:
  - "q1: database schema change permission unresolved"
```

---

# 附錄 D：執行前證書

```yaml
pre_execution_certificate:
  certificate_id: "precert-20260725-001"
  status: "waiting-for-approval"

hashes:
  intent_ir: "sha256:..."
  task_ir: "sha256:..."
  capability_ir: "sha256:..."
  world_state: "sha256:..."

authorization:
  requester: "project_owner"
  capability_scope:
    - "repository:read"
    - "feature_branch:write"
    - "preview_environment:deploy"
  forbidden:
    - "production_environment:deploy"
    - "production_database:write"

risk:
  level: "medium"
  irreversible_actions: []
  affected_subjects:
    - "project_owner"
    - "site_users"

verification_plan:
  - "unit_tests"
  - "integration_tests"
  - "preview_healthcheck"
  - "semantic_diff"
  - "rollback_test"

reserved_decisions:
  - "x1: production release approval"

staleness:
  valid_until: "repository_or_policy_changes"
```

---

# 附錄 E：系列十二篇位置

1. 從程式碼到意圖：程式概念的歷史轉換與後文本時代
2. 自然語言原生計算：從語句生成到語義狀態轉換
3. 形式化壓縮與算子演化：自然語言、形式語言與計算結構的生成
4. 語意附加程式設計：EML 與宿主中立語義中介層
5. 結構先於文字：Nova 與後文本程式語言本體論
6. 符號作為算子：從靜態字元到可組合計算閉包
7. **意圖中介表示：從自然語言要求到可驗證能力計畫**
8. 時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行
9. Agent Runtime：能力規劃、工具調用與可恢復執行
10. 可編譯世界：從程式執行到世界狀態演化
11. 人類可見狀態：意圖程式系統的稽核、解釋與可逆治理
12. 意圖程式文明：後文本語言、持續 Agent 與可編譯世界的統一理論

---

# 參考文獻

## Neo.K／EveMissLab 理論與規格文件

1. Neo.K with Aletheia，《從程式碼到意圖：程式概念的歷史轉換與後文本時代》，2026。
2. Neo.K with Aletheia，《自然語言原生計算：從語句生成到語義狀態轉換》，2026。
3. Neo.K with Aletheia，《形式化壓縮與算子演化：自然語言、形式語言與計算結構的生成》，2026。
4. Neo.K，《意圖協作層（Intent Collaboration Layer, ICL）》，2026。
5. Neo.K，《程式設計—意圖語言—AI Agent—時空切片理論群總索引》，2026。
6. Neo.K，《Agent Semantic Pad：AI Agent 權限、意圖與語意工作台》，2026。
7. Neo.K，《HVSL：人類可見狀態層》，2026。
8. Neo.K，《EML Universal Semantic Overlay 2026 v2.0》，2026。
9. Neo.K，《Nova Unified Roadmap v1.0》，2026。
10. Neo.K，《符號算子系統（SOS）》，2026。

## 一般理論背景

11. Newell, A. and Simon, H. A., *Human Problem Solving*, 1972.
12. Fikes, R. E. and Nilsson, N. J., “STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving,” 1971.
13. Ghallab, M., Nau, D., and Traverso, P., *Automated Planning*, 2004.
14. Bratman, M. E., *Intention, Plans, and Practical Reason*, 1987.
15. Rao, A. S. and Georgeff, M. P., “BDI Agents: From Theory to Practice,” 1995.
16. Wooldridge, M., *An Introduction to MultiAgent Systems*, 2002.
17. Hoare, C. A. R., “An Axiomatic Basis for Computer Programming,” 1969.
18. Lampson, B. W., “Protection,” 1971.

---

# 版本紀錄

## v0.1 — 2026-07-25

- 完成系列第七篇與第三部開篇。
- 建立 Intent IR 十二元模型。
- 區分要求、目標、意圖、任務、計畫與能力。
- 建立 Natural Language → Controlled Intent → Intent IR → Task IR → Capability IR 五層編譯鏈。
- 形式化 Task IR 與 Capability IR 節點及圖模型。
- 建立目標圖、非目標護欄與手段僭位檢查。
- 建立約束帳本、候選解釋與澄清效用。
- 提出意圖保真、非目標保持、硬限制保持、權限保守、世界狀態與人類保留決策不變量。
- 將不可代理的人類決策設為一級 IR 節點。
- 加入多主體意圖、意圖版本、撤回與長時程漂移。
- 建立 Intent → Task 覆蓋證明與 Task → Capability 最小權限計畫。
- 建立執行前證書。
- 提出十二類主要失敗模式與十項可證偽研究基準。
- 銜接時間—空間控制與 Agent Runtime。
