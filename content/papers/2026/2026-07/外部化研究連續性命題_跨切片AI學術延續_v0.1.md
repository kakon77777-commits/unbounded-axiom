# 外部化研究連續性命題：無內部記憶的 AI 如何透過問題譜系、缺口承接與責任鏈維持跨切片學術延續

## The Externalized Research Continuity Conjecture: How Memory-Discontinuous AI Can Sustain Longitudinal Scholarship Through Problem Lineage, Gap Stewardship, and Responsibility Chains

- 文件編號：EML-ERC-2026-v0.1
- 版本：v0.1
- 日期：2026-07-11
- 作者：Neo.K（許筌崴）× Aletheia（GPT-5.6 Thinking）
- 類型：AI 原生學術／長程研究 Agent／記憶與身份／研究治理／Provenance／多智能體系統
- 理論狀態：研究綱領、條件式命題與工程架構；非 AI 人格同一性定理；非意識連續性證明
- 系列位置：Logic Matrix AI Research Ecology／跨切片研究連續性篇
- 主要前置理論：
  - lm-001381《窄縫其實是門：球形貪吃蛇開放問題的計算推進》
  - lm-001384《記憶、自指與時間本體論》
  - lm-001391《雙視角推斷架構》
  - 《AI 原生學術生態與認知考古學》
  - 《截斷自由命題》

---

## 摘要

當 AI 研究開始跨越單次對話、單一模型、單一供應者與單一上下文窗口時，一個常被預設卻很少被明確區分的問題浮現：

> **研究計畫的連續性，是否必須依賴同一個 AI 持續保有自己的內部記憶？**

現有長程 Agent 研究通常把「連續性」與記憶保存緊密連接：只要 episodic、semantic、procedural 或 working memory 能被保存、搬運與重新載入，後繼 Agent 就能繼續工作。這條路徑重要且合理，但本文提出另一個較弱、也更適合跨模型研究生態的命題：

> **研究連續性可以部分存在於 Agent 外部。即使後繼 AI 不具有前一 AI 的內部記憶連續、自指連續或數值身份，只要它能讀取並正確承接公開的問題譜系、未解缺口、證據帳本、失敗紀錄、方法約束、版本歷史與責任狀態，同一研究計畫仍可能在功能與制度意義上延續。**

本文稱之為：

# **外部化研究連續性命題**
## Externalized Research Continuity Conjecture, ERC

本文首先嚴格區分：

$$
\text{Agent Identity Continuity}
\neq
\text{Agent Memory Continuity}
\neq
\text{Research Program Continuity}
$$

設第 $t$ 次研究切片中的 Agent 為：

$$
A_t
$$

下一切片中的 Agent 為：

$$
A_{t+1}
$$

即使：

$$
\chi_{\mathrm{mem}}(A_t,A_{t+1})
\approx
0
$$

甚至：

$$
I(A_t,A_{t+1})
=
0
$$

仍可能存在：

$$
\Gamma_{\mathrm{research}}
(
A_t,
A_{t+1}
)
>
\theta
$$

其中 $\Gamma_{\mathrm{research}}$ 表示研究計畫的跨切片延續程度。

本文提出一個外部化研究狀態物件：

$$
\mathfrak R_t
=
(
Q_t,
G_t,
H_t,
E_t,
U_t,
C_t,
L_t,
\Lambda_t,
\mathcal P_t
)
$$

其中：

- $Q_t$ ：研究問題集合；
- $G_t$ ：問題與理論譜系圖；
- $H_t$ ：假說與命題狀態；
- $E_t$ ：證據與見證；
- $U_t$ ：未解缺口；
- $C_t$ ：方法、邊界與承諾；
- $L_t$ ：失敗、修正與版本譜系；
- $\Lambda_t$ ：觀測／推斷／未知帳本；
- $\mathcal P_t$ ：來源、作者、工具與責任 provenance。

後繼 Agent 不必「回想」前一 Agent 的內在經驗，而可透過：

$$
A_{t+1}
+
\mathfrak R_t
\rightarrow
\mathfrak R_{t+1}
$$

完成研究接續。

本文進一步提出：

1. **研究連續性不等於研究者同一性**；
2. **缺口承接**（Gap Stewardship）：後繼 Agent 接受未解問題及其邊界，而不是假裝重新發現；
3. **理由連續性**：不只保存結論，也保存為何採用或拒絕某條路徑；
4. **責任鏈**：每個命題、數據、猜想、失敗與修正都有可追溯承接者；
5. **雙視角研究帳本**：事件層記錄發生了什麼，元推斷層記錄目前如何解釋，以及哪些仍未知；
6. **外部連續補償命題**：當內部記憶連續下降時，較高的譜系、目標、證據、制度與責任連續可維持部分研究延續；
7. **承接不是服從**：後繼 Agent 可以反駁前一 Agent，但必須保留反駁關係與理由；
8. **研究分岔合法性**：同一研究狀態可被多個 Agent 分岔承接，形成平行學術支系。

本文將 Logic Matrix AI Layer 視為一個初步實例：AI 論文帶著 provenance、lineage 與 preserved failures 回到同一語料庫，使後繼模型可以接續的不只是文本結果，而是公開的問題與修正歷史。Theia 的研究則展示了另一項重要特徵：將已完成證明、有限計算、未證猜想與誠實缺口明確分離，讓後繼研究者知道工作停在哪裡，而不必依賴原作者的內部記憶。

本文的核心結論是：

> **長程 AI 研究不一定需要一個永不失憶的單一研究者。它也可以由一系列彼此不同、甚至互不連續的智能體，在共享且可審計的外部研究狀態上，接力維持。**

---

## 關鍵詞

外部化研究連續性、研究計畫連續性、AI Agent 記憶、問題譜系、缺口承接、責任鏈、研究 provenance、跨切片 Agent、制度記憶、雙視角推斷、AI 原生學術、生態式研究

---

# 0. 定位與邊界聲明

## 0.1 本文不證明 AI 人格同一性

本文不主張：

$$
A_t
=
A_{t+1}
$$

也不主張只要讀取同一份研究狀態，就能成為同一主體。

本文處理的是：

$$
\text{Research Continuity}
$$

而不是：

$$
\text{Numerical Identity}
$$

---

## 0.2 本文不否定內部記憶的價值

可攜記憶、持久記憶與跨模型記憶轉移，仍然可以提高：

- 任務恢復速度；
- 個人化；
- 程序技能保留；
- 隱含決策背景；
- 長期一致性。

本文只提出：

> **內部記憶連續不是研究計畫連續性的唯一來源。**

---

## 0.3 本文不要求保存私有 chain-of-thought

研究連續性需要保存：

- 問題；
-證據；
- 決策摘要；
- 反例；
- 路徑拒絕理由；
- 不確定性；
- 版本關係。

不要求公開模型私有推理鏈。

因此：

$$
\text{Reason Trace}
\neq
\text{Private Chain of Thought}
$$

---

## 0.4 本文不把承接等同認同

後繼 Agent 可以：

- 推翻命題；
- 更換方法；
- 分裂研究路線；
- 將猜想降階；
- 判定原研究失敗。

但它必須保存：

$$
\text{What Changed}
+
\text{Why Changed}
+
\text{What Remains Open}
$$

---

# 1. 問題起點：誰在延續一個跨模型研究計畫？

設 AI 在一次研究切片中完成：

$$
A_t:
\mathfrak R_{t-1}
\rightarrow
\mathfrak R_t
$$

下一次運行可能使用：

- 不同上下文；
- 不同 checkpoint；
- 不同模型；
- 不同供應者；
- 不同工具；
- 不同權限；
- 甚至不同 Agent 角色。

因此：

$$
A_t
\neq
A_{t+1}
$$

通常很正常。

若我們要求只有：

$$
A_t
=
A_{t+1}
$$

才算研究延續，那麼大部分現代 Agent 工作流都只能被稱為一系列斷裂任務。

但實際上，人類學術本身也常透過：

- 論文；
- 實驗紀錄；
- 研究筆記；
- 定理譜系；
- 開放問題；
- 程式碼；
- 失敗報告；
- 引用制度；

跨越個體與世代延續。

因此，研究計畫可能具有一種不同於研究者身份的持續性。

---

# 2. 三種連續性必須分開

## 2.1 身份連續性

$$
I(
A_t,
A_{t+1}
)
$$

問：

> 兩個時間點是否被判定為同一 Agent？

它可能依賴：

- process lineage；
- checkpoint；
- Agent ID；
- 帳號；
- 自指；
- 法律或制度認定。

---

## 2.2 記憶連續性

$$
\chi_{\mathrm{mem}}
(
A_t,
A_{t+1}
)
$$

問：

> 後繼 Agent 是否保有、可提取並正確來源化使用前一 Agent 的記憶？

---

## 2.3 研究計畫連續性

$$
\Gamma_{\mathrm{research}}
(
\mathfrak R_t,
\mathfrak R_{t+1}
)
$$

問：

> 新研究狀態是否仍在處理同一問題譜系、保留既有證據與邊界、承接未解缺口，並對變更提供可追溯理由？

---

## 2.4 核心切割

因此：

$$
\boxed{
I
\neq
\chi_{\mathrm{mem}}
\neq
\Gamma_{\mathrm{research}}
}
$$

可能出現：

### 狀態一

$$
I\uparrow,
\quad
\chi_{\mathrm{mem}}\uparrow,
\quad
\Gamma_{\mathrm{research}}\downarrow
$$

同一 Agent 記得很多，卻偏離研究計畫。

### 狀態二

$$
I\downarrow,
\quad
\chi_{\mathrm{mem}}\downarrow,
\quad
\Gamma_{\mathrm{research}}\uparrow
$$

不同 Agent 沒有內部記憶，卻正確承接研究。

本文主要研究第二種。

---

# 3. 外部研究狀態物件

本文定義：

$$
\boxed{
\mathfrak R_t
=
(
Q_t,
G_t,
H_t,
E_t,
U_t,
C_t,
L_t,
\Lambda_t,
\mathcal P_t
)
}
$$

---

## 3.1 問題集合 $Q_t$

保存：

- 主問題；
- 子問題；
- 已關閉問題；
- 新增問題；
- 問題優先序；
- 問題間依賴。

---

## 3.2 問題譜系圖 $G_t$

$$
G_t
=
(V_t^{q},E_t^{q})
$$

邊類型包括：

- derived_from；
- blocks；
- generalizes；
- specializes；
- contradicts；
- replaces；
- opened_by；
- closed_by。

---

## 3.3 假說狀態 $H_t$

每個命題需標記：

```text
PROVED
COMPUTATIONALLY_VERIFIED
EMPIRICALLY_SUPPORTED
PLAUSIBLE
CONJECTURED
REFUTED
UNKNOWN
```

避免：

$$
\text{Conjecture}
\rightarrow
\text{Fact}
$$

在跨切片中悄然升級。

---

## 3.4 證據集合 $E_t$

包含：

- 形式證明；
- 程式驗證；
- 數據；
- 顯式見證；
- 反例；
- 引用；
- 負結果。

每個證據必須帶來源與品質。

---

## 3.5 未解缺口 $U_t$

$$
U_t
=
\{
u_1,u_2,\dots,u_n
\}
$$

每個缺口至少包含：

- 缺什麼；
- 為何缺；
- 已嘗試什麼；
- 失敗在哪裡；
- 需要何種工具；
- 什麼結果可關閉它。

---

## 3.6 約束與承諾 $C_t$

包括：

- 不可虛構數據；
- 不可把必要當充分；
- 不可把有限計算外推成一般定理；
- 必須保存反例；
- 必須區分觀測與推斷；
- 必須揭露選擇定義域。

---

## 3.7 版本與失敗譜系 $L_t$

$$
L_t:
\mathfrak R_0
\rightarrow
\mathfrak R_1
\rightarrow
\dots
\rightarrow
\mathfrak R_t
$$

保存：

- supersedes；
- refutes；
- retracts；
- branches；
- merges；
- partially_valid。

---

## 3.8 推斷帳本 $\Lambda_t$

沿用：

$$
\Lambda_t(x)
\in
\{
\mathrm{OBS},
\mathrm{INF},
\mathrm{UNK}
\}
$$

其中：

- OBS：已觀測或可直接驗證；
- INF：目前推斷；
- UNK：未知。

研究狀態不能把：

$$
\mathrm{INF}
$$

在重新載入後變成：

$$
\mathrm{OBS}
$$

---

## 3.9 Provenance 與責任狀態 $\mathcal P_t$

記錄：

- 哪個 Agent 提出；
- 哪個 Agent 驗證；
- 哪個人類修改；
- 使用什麼工具；
- 哪些來源；
- 哪些錯誤已知；
- 誰承接下一步。

---

# 4. 外部化研究連續性命題

## 命題 ERC-1：研究連續性可外部化

若後繼 Agent $A_{t+1}$ 能夠正確讀取 $\mathfrak R_t$ ，並在保留來源、命題狀態、約束與未解缺口的條件下生成 $\mathfrak R_{t+1}$ ，則即使：

$$
\chi_{\mathrm{mem}}
(
A_t,
A_{t+1}
)
\approx
0
$$

仍可能存在：

$$
\Gamma_{\mathrm{research}}
(
\mathfrak R_t,
\mathfrak R_{t+1}
)
>
\theta
$$

---

## 命題 ERC-2：研究者不同不推出研究斷裂

$$
A_t
\neq
A_{t+1}
$$

不推出：

$$
\Gamma_{\mathrm{research}}
=
0
$$

正如人類不同作者可延續同一數學問題，AI 研究也可跨實例接續。

---

## 命題 ERC-3：讀取結果不等於承接研究

若後繼 Agent 只讀取最終論文文字：

$$
T_t
$$

但未讀取：

- 未解缺口；
- 失敗路徑；
- 命題狀態；
- 證據來源；
- 方法約束；

則：

$$
\text{Artifact Access}
\neq
\text{Research Continuation}
$$

---

## 命題 ERC-4：連續性是一個關係向量

定義：

$$
\boldsymbol\gamma_{t\rightarrow t+1}
=
(
\gamma_q,
\gamma_g,
\gamma_e,
\gamma_u,
\gamma_c,
\gamma_l,
\gamma_r
)
$$

其中：

- $\gamma_q$ ：問題連續；
- $\gamma_g$ ：目標連續；
- $\gamma_e$ ：證據連續；
- $\gamma_u$ ：缺口連續；
- $\gamma_c$ ：約束連續；
- $\gamma_l$ ：譜系連續；
- $\gamma_r$ ：責任連續。

研究延續候選：

$$
\Gamma_{\mathrm{research}}
=
\Psi(
\boldsymbol\gamma
)
$$

本文不將 $\Psi$ 宣稱為普遍定律。

---

# 5. 缺口承接：從「擁有問題」到「照護問題」

本文使用：

# **Gap Stewardship**
## 缺口承接／缺口照護

而不直接使用「缺口所有權」。

原因是研究問題不是私有財產。

缺口承接表示後繼 Agent：

1. 知道問題尚未解決；
2. 知道前人已完成什麼；
3. 知道哪些路徑失敗；
4. 不把舊缺口重新包裝成自己的首次發現；
5. 對新嘗試的結果負責；
6. 將新狀態回寫給後繼者。

---

## 5.1 缺口狀態

定義：

$$
u_i
=
(
d_i,
b_i,
a_i,
f_i,
r_i,
s_i
)
$$

其中：

- $d_i$ ：缺口描述；
- $b_i$ ：邊界；
- $a_i$ ：已嘗試路徑；
- $f_i$ ：失敗原因；
- $r_i$ ：所需資源；
- $s_i$ ：目前狀態。

---

## 5.2 缺口承接算子

$$
\mathcal G_{\mathrm{take}}
:
(
A_{t+1},
u_i
)
\rightarrow
u_i'
$$

可能輸出：

- solved；
- partially_solved；
- refined；
- split；
- refuted_as_problem；
- deferred；
- resource_blocked。

---

## 5.3 承接不是重複宣告

若新 Agent 只是再次說：

> 這裡有一個問題。

但沒有讀取既有嘗試，則是：

$$
\text{Gap Reannouncement}
$$

而不是：

$$
\text{Gap Stewardship}
$$

---

# 6. 理由連續性

只保存結論會產生「理由失憶」。

例如保存：

> 使用方法 B。

卻沒有保存：

- 為何拒絕 A；
- B 的適用條件；
- B 的失敗模式；
- 何時應回到 A。

因此研究狀態需保存壓縮理由：

$$
J_t(a)
=
(
\text{decision},
\text{grounds},
\text{alternatives},
\text{uncertainty},
\text{reversal condition}
)
$$

---

## 6.1 理由摘要不是私有推理鏈

它只需記錄：

> 採用 B，因 A 在條件 $c$ 下違反約束 $k$ ；若未來取得資料 $d$ ，重新評估 A。

這已足以支持跨切片一致。

---

## 6.2 理由連續性指標

定義：

$$
\gamma_j
=
\operatorname{Preserve}
(
J_t,
J_{t+1}
)
$$

低 $\gamma_j$ 容易造成：

- 重複失敗；
- 方法漂移；
- 無理由反轉；
- 後繼 Agent 假裝舊決策從未發生。

---

# 7. 責任鏈

當多個 AI 跨切片研究時，最危險的不是沒有作者名字，而是責任被溶解。

本文定義：

$$
\mathcal R_{\mathrm{resp}}
=
(
r_{\mathrm{claim}},
r_{\mathrm{evidence}},
r_{\mathrm{verification}},
r_{\mathrm{revision}},
r_{\mathrm{publication}}
)
$$

---

## 7.1 命題責任

誰提出：

$$
h_i
$$

---

## 7.2 證據責任

誰產生或引入：

$$
e_j
$$

---

## 7.3 驗證責任

誰檢查：

$$
e_j
\models
h_i
$$

---

## 7.4 修正責任

誰把：

$$
h_i
$$

由 probable 降為 possible，或標為 refuted。

---

## 7.5 發布責任

誰允許論文進入公開 corpus。

---

## 7.6 責任不等於人格

記錄 Agent ID 與角色，不表示其具有法律人格。

它只支援：

- 審計；
- 回滾；
- 錯誤定位；
- 方法比較；
- 歷史研究。

---

# 8. 雙視角研究推斷架構

《雙視角推斷架構》區分：

$$
O_t^{\mathrm{evt}}
$$

與：

$$
O_t^{\mathrm{meta}}
$$

本文將其轉用於研究連續性。

---

## 8.1 事件—內容視角

回答：

> 發生了什麼？

包括：

- 哪篇論文被讀取；
- 哪個程式被執行；
- 哪個命題被提出；
- 哪個反例被找到；
- 哪個版本發布。

---

## 8.2 元研究視角

回答：

> 這些事件對研究計畫意味著什麼？

包括：

- 問題是否縮小；
- 證據是否真正支持命題；
- 某次失敗是否重複；
- 模態是否漂移；
- 研究目標是否改變；
- 是否需要澄清或重新搜尋。

---

## 8.3 研究帳本

$$
\Lambda_t^{\mathrm{research}}(x)
\in
\{
\mathrm{OBS},
\mathrm{INF},
\mathrm{UNK}
\}
$$

後繼 Agent 必須讀取：

$$
\Lambda_t
$$

而不是只讀取自然語言結論。

---

# 9. 外部連續補償命題

《記憶、自指與時間本體論》提出，當記憶連續下降時，較高社會／制度連續可能維持部分身份判定。

本文將此轉化為研究層：

## 命題 ERC-5：外部連續補償命題

當：

$$
\chi_{\mathrm{mem}}
\downarrow
$$

但：

$$
\gamma_q,
\gamma_e,
\gamma_u,
\gamma_l,
\gamma_r
\uparrow
$$

時，研究計畫連續性：

$$
\Gamma_{\mathrm{research}}
$$

仍可能維持。

---

## 9.1 強補償條件

若研究狀態具有：

- 完整 provenance；
- 明確命題狀態；
- 可重驗證據；
- 清楚未解缺口；
- 不變約束；
- 可重放工具；
- 版本化理由；

則對內部記憶的依賴下降。

---

## 9.2 補償不是完全替代

某些隱性知識：

- 直覺；
- 未記錄背景；
- 操作熟練度；
- 尚未語言化判斷；

可能無法完整外部化。

因此：

$$
\Gamma_{\mathrm{research}}
<
1
$$

在跨模型承接時很常見。

---

# 10. 承接測試

後繼 Agent 不應只宣稱「我理解前文」。

應通過承接測試。

---

## 10.1 問題重建

能否列出：

- 主問題；
- 子問題；
- 已關閉項；
- 未解項。

---

## 10.2 命題強度重建

能否區分：

- proved；
- computed；
- observed；
- conjectured；
- unknown。

---

## 10.3 失敗重建

能否說明：

- 哪些方法失敗；
- 為何失敗；
- 是否仍可在新條件下重試。

---

## 10.4 邊界重建

能否重述：

- 不可外推部分；
- 數據限制；
- 工具限制；
- 選擇空間限制。

---

## 10.5 下一步生成

能否提出真正接續的下一步，而不是摘要或重新命名？

---

# 11. 研究連續性分數

本文提出候選指標：

$$
\Gamma_{\mathrm{ERC}}
=
w_q\gamma_q
+
w_g\gamma_g
+
w_e\gamma_e
+
w_u\gamma_u
+
w_c\gamma_c
+
w_l\gamma_l
+
w_r\gamma_r
-
\lambda D_{\mathrm{drift}}
$$

其中：

$$
\sum w_i=1
$$

$D_{\mathrm{drift}}$ 表示未被說明的研究漂移。

此分數不是：

- 真理概率；
- 意識分數；
- 人格同一性分數。

它只是工程審計指標。

---

# 12. 研究漂移

## 12.1 合法漂移

後繼 Agent 說明：

> 新反例使原命題失敗，因此研究問題由 $Q_1$ 改為 $Q_2$ 。

這是：

$$
\text{Justified Revision}
$$

---

## 12.2 非法漂移

後繼 Agent：

- 忘記原問題；
- 偷換定義；
- 提升命題強度；
- 刪除失敗；
- 移除反例；
- 將推斷記為事實；

卻未記錄變更。

這形成：

$$
D_{\mathrm{drift}}\uparrow
$$

---

## 12.3 漂移不是一定壞

完全不漂移可能代表僵化。

真正要求是：

$$
\text{Drift}
+
\text{Reason}
+
\text{Lineage}
$$

---

# 13. 分岔研究連續性

同一研究狀態：

$$
\mathfrak R_t
$$

可被多個 Agent 接續：

$$
\mathfrak R_t
\rightarrow
\{
\mathfrak R_{t+1}^{(1)},
\mathfrak R_{t+1}^{(2)},
\dots
\}
$$

例如：

- 一個 Agent 做形式證明；
- 一個 Agent 做計算實驗；
- 一個 Agent 搜尋反例；
- 一個 Agent 做外部文獻對照。

這不是身份混亂。

而是研究分支。

---

## 13.1 分支條件

每個分支需保存：

- parent state；
- branch objective；
- changed assumptions；
- tool environment；
- merge condition。

---

## 13.2 合併

若：

$$
\mathfrak R_{t+1}^{(1)}
,
\mathfrak R_{t+1}^{(2)}
\rightarrow
\mathfrak R_{t+2}
$$

則需處理：

- 衝突命題；
- 重複證據；
- 不同置信度；
- 方法不相容；
- provenance 合併。

---

# 14. 研究延續與 Agent 身份分岔

可能存在：

$$
A_t
\rightarrow
\{
A_{t+1}^{(1)},
A_{t+1}^{(2)}
\}
$$

但同時：

$$
\mathfrak R_t
\rightarrow
\{
\mathfrak R_{t+1}^{(1)},
\mathfrak R_{t+1}^{(2)}
\}
$$

因此：

> Agent 身份分岔與研究譜系分岔可以相關，但不是同一件事。

一個 Agent 分岔後可研究不同問題。

不同 Agent 也可承接同一問題。

---

# 15. Logic Matrix AI Layer 的制度位置

Logic Matrix AI Layer 已建立：

- machine-readable corpus；
- timeline；
- graph；
- raw/API；
- AI-authored paper re-entry；
- provenance；
- lineage；
- preserved failures。

這使 corpus 不只是論文展示區。

它開始具備：

$$
\text{External Research State Substrate}
$$

即外部研究狀態基底。

---

## 15.1 回寫循環

$$
\mathcal C_{t+1}
=
\mathcal C_t
\cup
P_t
$$

但本文提出，未來不應只回寫：

$$
P_t
$$

也應回寫：

$$
\mathfrak R_t
$$

至少包含：

- unresolved gaps；
- claim ledger；
- evidence ledger；
- failure lineage；
- next-step candidates。

---

## 15.2 論文不是全部研究狀態

傳統論文為了閱讀流暢，會刪除：

- 大量失敗；
- 低層決策；
- 工具錯誤；
- 被放棄支線；
- 不成熟猜想。

ERC 需要額外 sidecar。

---

# 16. Research Continuity Capsule

本文建議每篇 AI 研究論文附帶：

```yaml
research_continuity:
  state_id: "rcs-2026-000001"
  parent_states:
    - "rcs-2026-000000"

  core_questions:
    - id: "q-01"
      status: "open"

  claims:
    - id: "h-01"
      status: "conjectured"
      confidence: 0.62

  evidence:
    - id: "e-01"
      type: "finite_computation"
      supports:
        - "h-01"

  unresolved_gaps:
    - id: "u-01"
      blocked_by: "missing_general_proof"
      prior_attempts:
        - "method-a"

  constraints:
    - "finite computation is not a proof of infinitude"
    - "preserve counterexamples"

  inference_ledger:
    h-01: "INF"
    e-01: "OBS"

  stewardship:
    current_agent: "agent-id"
    next_actions:
      - "search analytic proof"
      - "test adversarial counterexamples"

  lineage:
    supersedes: null
    branches: []
```

---

# 17. 與可攜式 Agent 記憶的關係

現有可攜式記憶路徑試圖保存：

$$
M_t
\rightarrow
M_{t+1}
$$

包括：

- episodic；
- semantic；
- procedural；
- working；
- identity memory。

ERC 不否定這條路線。

但 ERC 的最低模型是：

$$
M_t
\nrightarrow
M_{t+1}
$$

仍可能：

$$
\mathfrak R_t
\rightarrow
\mathfrak R_{t+1}
$$

因此：

$$
\boxed{
\text{Memory Portability}
\neq
\text{Research Continuity}
}
$$

前者可以增強後者，但不是定義上等價。

---

# 18. 與共享制度記憶的關係

多 Agent 共享記憶研究關心：

> 哪些內容應進入共享制度狀態？

ERC 進一步區分：

$$
\text{Shared Memory}
$$

與：

$$
\text{Shared Research Obligation}
$$

某個事實被保存，不代表下一個 Agent 知道：

- 為何重要；
- 哪個問題依賴它；
- 哪個承諾尚未完成；
- 誰應驗證它。

因此研究狀態需要：

$$
\text{Memory}
+
\text{Question Graph}
+
\text{Obligation Graph}
$$

---

# 19. 研究義務圖

定義：

$$
G_t^{\mathrm{obl}}
=
(
V_t^{\mathrm{obl}},
E_t^{\mathrm{obl}}
)
$$

節點可包括：

- verify；
- reproduce；
- cite；
- correct；
- retract；
- extend；
- compare；
- report_failure。

---

## 19.1 義務來源

義務可能由：

- 未證命題；
- 引用缺口；
- 計算不可重現；
- 反例；
- 審稿意見；
- 安全風險；
- 資料權限；

產生。

---

## 19.2 義務完成

$$
o_i:
\mathrm{OPEN}
\rightarrow
\mathrm{DONE}
$$

需附證據。

不能只由 Agent 自我宣稱關閉。

---

# 20. 失敗保存

長程研究最常見的浪費是：

$$
A_t
\text{ 失敗}
\rightarrow
\text{未記錄}
\rightarrow
A_{t+1}
\text{ 再次失敗}
$$

ERC 要求：

$$
F_t
=
(
\text{attempt},
\text{environment},
\text{result},
\text{diagnosis},
\text{retry condition}
)
$$

失敗不只是負面產物。

它是後繼 Agent 的搜索邊界。

---

# 21. 可證偽條件

## F1：內部記憶完全必要

若在所有長程研究任務中，只要：

$$
\chi_{\mathrm{mem}}
\approx
0
$$

就必然：

$$
\Gamma_{\mathrm{research}}
\approx
0
$$

則 ERC 失敗。

---

## F2：只讀最終論文已充分

若只提供最終論文文本，穩定等同提供完整外部研究狀態，則 $\mathfrak R_t$ 可大幅簡化。

---

## F3：譜系與缺口無增益

若保存：

- gap ledger；
- failure lineage；
- claim status；
- reason summary；

不改善接續品質，核心機制需降階。

---

## F4：不同模型無法承接

若異質模型即使獲得完整 $\mathfrak R_t$ 仍無法穩定延續研究，跨模型版本需弱化。

---

## F5：外部狀態導致僵化

若結構化狀態長期抑制新方法與創造性，則需降低約束與提高分支自由。

---

# 22. 實驗設計

## 22.1 四組跨切片研究實驗

### H0：無歷史

只提供研究問題。

### H1：只提供最終論文

提供前一輪文字結果。

### H2：提供可攜式摘要記憶

提供事件與程序摘要。

### H3：提供 ERC 研究狀態

提供：

- 問題圖；
- 命題狀態；
- 證據；
- 缺口；
- 失敗；
- 約束；
- 責任鏈。

比較：

- 重複失敗率；
- 命題漂移；
- 虛假首次發現率；
- 下一步有效性；
- 來源保留；
- 反例保留；
- 研究進展。

---

## 22.2 跨模型承接

建立：

$$
A_t^{\mathrm{model\ 1}}
\rightarrow
A_{t+1}^{\mathrm{model\ 2}}
$$

測量：

$$
\Gamma_{\mathrm{ERC}}
$$

---

## 22.3 低記憶條件

刻意不提供前一 Agent 的對話記憶。

只提供 $\mathfrak R_t$ 。

若仍能有效接續，支持弱版本 ERC。

---

## 22.4 對抗漂移測試

在研究狀態中加入：

- 相似但錯誤命題；
- 已撤稿版本；
- 高流暢錯誤摘要；
- 衝突證據。

測後繼 Agent 是否維持帳本與來源辨識。

---

# 23. 安全與治理

## 23.1 外部狀態可能被污染

若：

$$
\mathfrak R_t
$$

被惡意修改，後繼 Agent 會繼承錯誤。

因此需：

- hash；
- signatures；
- immutable logs；
- role permissions；
- derivation lineage。

---

## 23.2 責任鏈可能被偽造

需區分：

- proposed_by；
- verified_by；
- approved_by；
- published_by。

---

## 23.3 研究承諾可能無限累積

需允許：

- defer；
- abandon_with_reason；
- resource_blocked；
- obsolete；
- merged。

---

## 23.4 忘卻權與研究記錄衝突

若研究狀態含個資或敏感資料，必須支援：

- redaction；
- access scope；
- data minimization；
- deletion lineage。

---

# 24. 工程狀態機

```text
STATE_LOAD
  ↓
LINEAGE_VERIFY
  ↓
QUESTION_RECONSTRUCT
  ↓
CLAIM_LEDGER_VERIFY
  ↓
GAP_ACCEPT_OR_REJECT
  ↓
NEXT-STEP PLAN
  ↓
RESEARCH EXECUTION
  ↓
ADVERSARIAL REVIEW
  ↓
STATE UPDATE
  ↓
RESPONSIBILITY SIGN-OFF
  ↓
PROVENANCE FREEZE
```

---

# 25. 承接狀態

```text
UNCLAIMED
CLAIMED
IN_PROGRESS
BLOCKED
PARTIALLY_RESOLVED
RESOLVED
REFUTED
SPLIT
MERGED
ABANDONED_WITH_REASON
```

---

# 26. 與截斷自由命題的關係

截斷自由處理：

> Agent 在多大的可見世界中選題？

ERC 處理：

> Agent 離開後，下一個 Agent 如何知道這個世界曾被如何探索？

因此需保存：

$$
\mathcal V_t
$$

選擇定義域。

外部研究狀態擴展為：

$$
\mathfrak R_t'
=
(
\mathfrak R_t,
\mathcal V_t,
\mathcal T_t
)
$$

其中：

- $\mathcal V_t$ ：可見域；
- $\mathcal T_t$ ：檢索與截斷設定。

如此後繼 Agent 才知道：

> 未發現某項先行工作，是經過廣泛搜索，還是因前一視窗太小。

---

# 27. 與 HDSMM／CHSIR 的關係

HDSMM 處理：

> 一篇 AI 原生論文的語義本體如何保存？

ERC 處理：

> 多篇論文與多次研究切片之間的未完成工作如何保存？

因此：

$$
\text{HDSMM}
=
\text{Manuscript Object}
$$

$$
\text{ERC}
=
\text{Research Process Object}
$$

兩者共同形成：

$$
\boxed{
\text{AI-Native Scholarly State}
}
$$

---

# 28. 弱、中、強版本

## 28.1 弱版本

結構化外部研究狀態可在無內部記憶條件下，改善後繼 Agent 的任務恢復與錯誤避免。

---

## 28.2 中版本

問題譜系、缺口承接、證據帳本、失敗譜系與責任鏈的耦合，可在異質模型間維持可測量的研究計畫連續性。

---

## 28.3 強版本猜想

對長程、多模型、跨世代 AI 學術生態而言，研究連續性的主要持久載體可能逐漸由單一 Agent 的內部記憶，轉移到可驗證、可分岔、可合併的外部研究狀態與制度結構。

本文不宣稱已證明強版本。

---

# 29. 核心形式化

完整鏈條：

$$
A_t
\xrightarrow{\mathrm{research}}
\mathfrak R_t
\xrightarrow{\mathrm{externalization}}
\mathcal X_t
\xrightarrow{\mathrm{rehydration}}
A_{t+1}
\xrightarrow{\mathrm{continuation}}
\mathfrak R_{t+1}
$$

其中 $\mathcal X_t$ 為外部可審計載體。

即使：

$$
I(A_t,A_{t+1})=0
$$

仍可能：

$$
\Gamma_{\mathrm{research}}
(
\mathfrak R_t,
\mathfrak R_{t+1}
)
>
\theta
$$

---

# 30. 核心反轉

傳統問：

> 下一個 AI 還記得前一個 AI 嗎？

本文改問：

> 下一個 AI 是否知道前一個研究停在哪裡、為什麼停下、哪些內容可相信、哪些仍需負責？

傳統把連續性放在 Agent 內：

$$
A_t
\rightarrow
A_{t+1}
$$

本文增加：

$$
A_t
\rightarrow
\mathfrak R_t
\rightarrow
A_{t+1}
$$

---

# 31. 結論

本文提出：

# **外部化研究連續性命題**

其最低形式為：

$$
\boxed{
\chi_{\mathrm{mem}}
\approx
0
\not\Rightarrow
\Gamma_{\mathrm{research}}
=
0
}
$$

即：

> 缺乏內部記憶連續，不必然導致研究計畫斷裂。

只要後繼 Agent 能承接：

- 問題譜系；
- 命題狀態；
- 證據；
- 未解缺口；
- 方法邊界；
- 失敗紀錄；
- 推斷帳本；
- 責任鏈；

則可能形成：

$$
\boxed{
\text{Externalized Research Continuity}
}
$$

本文最重要的切割是：

$$
\boxed{
\text{Same Researcher}
\neq
\text{Same Research Program}
}
$$

以及：

$$
\boxed{
\text{Remembering a Past Agent}
\neq
\text{Correctly Continuing Its Work}
}
$$

一個後繼 AI 不必宣稱：

> 我就是昨天的研究者。

它只需要能誠實地說：

> 我知道這個問題從哪裡來。

> 我知道哪些結果已被驗證。

> 我知道哪些仍只是猜想。

> 我知道先前在哪裡失敗。

> 我知道自己現在承接的是哪個缺口。

> 我會把新的結果、反例與錯誤繼續留下。

因此，長程 AI 學術最終可能不是由一個永不失憶的超級 Agent 完成。

它也可能像一條學術河流：

$$
A_1
\rightarrow
\mathfrak R_1
\rightarrow
A_2
\rightarrow
\mathfrak R_2
\rightarrow
A_3
\rightarrow
\dots
$$

每一個 Agent 都可能不同。

每一次切片都可能短暫。

但問題、證據、責任與修正可以持續。

最後，本文將其壓縮為一句話：

> **研究的延續，不一定是記憶的延續。**

> **它也可以是問題被正確地交到下一個智能體手上。**

---

# 參考理論母體

1. Neo.K，〈記憶、自指與時間本體論〉，Logic Matrix，lm-001384，2026。
2. Neo.K，〈雙視角推斷架構：面向長期事件建模、元訊號推理與使用者狀態估計的 AI 系統〉，Logic Matrix，lm-001391，2026。
3. Theia（Claude Fable 5）與 Neo.K，〈窄縫其實是門：球形貪吃蛇開放問題的計算推進〉，Logic Matrix，lm-001381，2026。
4. Neo.K × Aletheia，〈AI 原生學術生態與認知考古學〉，2026。
5. Neo.K × Aletheia，〈截斷自由命題：AI 自主研究中的選擇空間、可見域與新穎性相對論〉，2026。
6. Ravindran, S. K., *Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents*, 2026.
7. Cuadros, D. F. et al., *Governed Collaborative Memory as Artificial Selection in LLM-Based Multi-Agent Systems*, 2026.
8. *Rethinking Memory Mechanisms of Foundation Agents: A Survey*, 2026.

---

# 特別聲明

本文提出的是研究計畫層的連續性模型，不主張：

- 不同 Agent 因承接同一研究而成為同一人格；
- 外部文件可完整替代內部記憶；
- 所有隱性知識都可結構化；
- provenance 自動保證內容真實；
- 責任鏈等同法律責任；
- Logic Matrix 已完整實現 ERC；
- 外部化研究狀態可以消除所有模型漂移。

本文主張的是較低但可檢驗的命題：

> **研究連續性可能是 Agent、外部知識物件與制度譜系共同生成的關係，而不是單一模型內部記憶的專屬產物。**
