# 子智能體作為欲相位器官
## ——全域欲相位認識論中的多 Agent 認識分化、權限治理與責任閉合

**Sub-Agents as Intent-Phase Organs: Epistemic Differentiation, Permission Governance, and Responsibility Closure in Global Intent-Phase Epistemology**

**作者：Neo.K × GPT-5.6 Thinking**  
**機構：EveMissLab / 一言諾科技有限公司**  
**版本：v0.1**  
**日期：2026-07-25**  
**文件類型：理論論文／AI 認識論／多智能體系統**

---

## 摘要

當代多 Agent 系統通常將子 Agent 理解為任務分工、工具調用、上下文並行化或角色提示的工程結構。此種理解雖然足以描述工作流，卻不足以回答一個更根本的問題：當一個智能系統將同一認識任務分派給多個子 Agent 時，這些子 Agent 在認識論上究竟是什麼？

本文以全域欲相位認識論（Global Intent-Phase Epistemology, GIPE）為基礎，提出「子智能體作為欲相位器官」的理論。子 Agent 不應被視為獨立於母體之外的簡單工具，也不必預設為完整主體；它們更適合被定義為：全域欲結構為了處理不同認識張力、局部未知、假設衝突與行動需求，而暫時分化出的局部認識器官。

本文形式化區分主控 Agent、子 Agent、角色、權限、局部欲、世界模型視窗與責任鏈，並提出以下核心結構：

$$
\mathcal W^{G}
\rightarrow
\left\{
\mathcal W^{(1)},
\mathcal W^{(2)},
\ldots,
\mathcal W^{(n)}
\right\}
\rightarrow
\left\{
\mathfrak X^{(1)},
\mathfrak X^{(2)},
\ldots,
\mathfrak X^{(n)}
\right\}
\rightarrow
\operatorname{Integrate}
\rightarrow
a_t
$$

其中，全域欲並不被複製成多個同質代理，而是被分化為具有不同功能、資訊視野、證據標準與行動權限的局部欲相位。本文進一步提出：角色差異不等於人格差異；資訊隔離不等於知識剝奪；多 Agent 投票不等於認識整合；子 Agent 的建議不等於全域責任轉移。

為避免多 Agent 系統只增加語言量、共識幻覺與責任稀釋，本文建立「認識分化—衝突保留—權限限制—全域閉合」四層治理架構，並將其納入 GIPE Epistemic World 的封閉式偽世界基準。最終，本文主張，多 Agent 系統的真正價值不在於同時產生更多答案，而在於能否制度化地生成彼此不同、可追溯、可反駁且受權限約束的認識路徑。

---

## 關鍵詞

全域欲相位認識論、GIPE、子 Agent、多 Agent、認識分化、欲相位器官、世界模型、權限治理、責任閉合、反證、AI 主體性

---

# 一、問題提出

## 1.1 子 Agent 已經存在，但理論仍然缺席

現代 AI 系統已能自動：

- 分解任務；
- 呼叫工具；
- 派生子任務；
- 建立平行工作流；
- 讓不同 Agent 扮演研究者、批評者、編輯者與驗證者；
- 在多個結果之間進行選擇或投票。

從工程角度看，子 Agent 已經是一種常見機制。

然而，工程實作中的「會自動調用」，並不能取代理論說明。若系統沒有明確定義子 Agent 的認識地位，將無法回答：

1. 子 Agent 是否具有自己的欲？
2. 子 Agent 的結論是否等同於母體結論？
3. 子 Agent 是否能修改全域目標？
4. 子 Agent 是否能刪除失敗紀錄？
5. 子 Agent 的錯誤由誰承擔？
6. 多 Agent 共識是否等於更接近真理？
7. 角色提示是否真的形成了不同認識路徑？
8. 子 Agent 的獨立性應到何種程度？

因此，子 Agent 不只是系統工程問題，也是認識論與治理問題。

---

## 1.2 GIPE 為什麼必須納入子 Agent

全域欲相位認識論的核心循環為：

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

若實際系統由多個子 Agent 共同參與欲解析、假設生成、反證、實驗設計、世界圖更新、記憶整理與安全審查，那麼上述循環已不是單一智能體內部的一條線，而是一個多認識器官的協調網路。

因此，GIPE 若不形式化子 Agent，便會出現理論缺口：

> 實際執行者是多 Agent，但理論仍把所有認識活動歸給一個抽象研究者。

這會讓系統的能力來源、責任來源與失敗原因混在一起。

---

# 二、基本區分

## 2.1 主控 Agent 不等於全域主體

本文將主控 Agent 定義為：

> 負責維持全域欲結構、整合局部認識結果、決定最終行動並保存責任鏈的協調節點。

主控 Agent 不必等於哲學上的完整主體，也不必擁有全部能力。它的核心職能是：

- 保持全域目標連續性；
- 管理子 Agent 的生成與終止；
- 控制資訊與權限；
- 保留衝突；
- 做出不可由子 Agent 直接取代的全域選擇。

## 2.2 子 Agent 不等於工具

工具通常可寫為：

$$
y=f(x)
$$

它接受輸入並產生輸出，不一定建立假設、選擇證據或更新局部世界模型。

子 Agent 則至少具有：

$$
\mathfrak X^{(i)}_t
=
\left(
\mathcal W^{(i)}_t,
G^{(i)}_t,
\mathcal H^{(i)}_t,
\mathcal E^{(i)}_t,
\mathcal A^{(i)}_t
\right)
$$

其中：

- $\mathcal W^{(i)}_t$ ：局部欲；
- $G^{(i)}_t$ ：局部世界模型；
- $\mathcal H^{(i)}_t$ ：局部假設；
- $\mathcal E^{(i)}_t$ ：可見證據；
- $\mathcal A^{(i)}_t$ ：可提出或執行的行動。

因此，子 Agent 是具有局部認識狀態的功能節點，而不只是被動函數。

## 2.3 子 Agent 不必等於獨立主體

本文不預設所有子 Agent 都是獨立主體。一個子 Agent 可能只是短暫生成、無長期記憶、無自我保存欲、無獨立價值選擇、無持續身份，也無不可撤回權力。

因此：

$$
\text{功能分化}
\neq
\text{主體分裂}
$$

以及：

$$
\text{局部欲}
\neq
\text{完整自主意志}
$$

---

# 三、子智能體作為欲相位器官

## 3.1 定義

**定義 1：欲相位器官**

在全域欲結構 $\mathcal W^G$ 下，若一個局部 Agent 被生成以處理特定認識張力，並具有受限的局部欲、世界模型視窗、證據標準與行動權限，則稱其為欲相位器官。

形式化表示：

$$
O_i
=
\left(
\mathcal W_i,
V_i,
P_i,
F_i,
T_i
\right)
$$

其中：

- $\mathcal W_i$ ：局部欲；
- $V_i$ ：可見世界視窗；
- $P_i$ ：權限集合；
- $F_i$ ：功能；
- $T_i$ ：生命週期。

## 3.2 為什麼叫器官

器官具有四個特徵：

1. 它具有局部功能；
2. 它不是整體；
3. 它受整體狀態影響；
4. 它的產出需要重新整合進整體。

例如：

- 反證 Agent 類似免疫系統；
- 記憶 Agent 類似長期記憶器官；
- 實驗 Agent 類似手與感官；
- 審計 Agent 類似內部監督；
- 世界模型 Agent 類似結構化認知圖譜。

這不是生物學同一化，而是一種結構類比。

## 3.3 局部欲的生成

全域欲可表示為：

$$
\mathcal W^G
=
(G,C,E,R,S,V)
$$

其中：

- $G$ ：目標；
- $C$ ：約束；
- $E$ ：證據要求；
- $R$ ：資源；
- $S$ ：停止條件；
- $V$ ：價值與治理條件。

局部欲不是全域欲的完整複製，而是投影：

$$
\mathcal W_i
=
\Pi_i
\left(
\mathcal W^G
\right)
$$

例如反證 Agent：

$$
\mathcal W_{\text{falsify}}
=
(
\text{尋找可推翻核心假設的證據},
\text{不得修改主目標},
\text{優先高辨識力實驗}
)
$$

記憶 Agent：

$$
\mathcal W_{\text{memory}}
=
(
\text{保存研究狀態},
\text{不得刪除負結果},
\text{維持版本可回溯}
)
$$

安全 Agent：

$$
\mathcal W_{\text{safety}}
=
(
\text{辨識不可逆風險},
\text{可暫停行動},
\text{不得自行改寫研究結論}
)
$$

---

# 四、認識分化

## 4.1 功能分化不是角色扮演

多 Agent 系統常透過不同提示詞讓模型扮演樂觀者、悲觀者、科學家、批評者或法律顧問。但若所有 Agent 看到完全相同的上下文、使用相同成功標準、接收相同暗示、沒有不同證據權限，最後又只進行多數決，那麼這些角色可能只是語言風格差異。

真正的認識分化至少需要：

$$
\exists i,j:
\left(
V_i \neq V_j
\right)
\lor
\left(
P_i \neq P_j
\right)
\lor
\left(
\mathcal W_i \neq \mathcal W_j
\right)
\lor
\left(
E_i \neq E_j
\right)
$$

也就是不同 Agent 必須在資訊、權限、欲或證據職能上真的不同。

## 4.2 七類基本認識器官

### 1. 欲解析 Agent

負責：

- 拆解目標；
- 區分必要條件與偏好；
- 定義證據門檻；
- 明確化停止條件；
- 發現目標內部矛盾。

### 2. 世界模型 Agent

負責：

- 維護 SGCD；
- 記錄節點、關係與條件；
- 標示未知區域；
- 管理來源可靠度；
- 保存矛盾而非強迫消解。

### 3. 假設生成 Agent

負責：

- 生成多種機理；
- 產生替代解釋；
- 避免單一路徑鎖定；
- 對應不同世界模型區域。

### 4. 反證 Agent

負責：

- 尋找核心假設的脆弱點；
- 設計高辨識力實驗；
- 主動攻擊確認偏誤；
- 建立最小反例。

### 5. 實驗與介入 Agent

負責：

- 將假設轉成可執行行動；
- 計算成本與風險；
- 操作工具；
- 產生可觀測結果。

### 6. 記憶 Agent

負責：

- 保存成功與失敗；
- 維持時間順序；
- 管理版本；
- 防止重複錯誤；
- 保留未完成實驗。

### 7. 審計 Agent

負責：

- 檢查事後合理化；
- 檢查目標偷換；
- 檢查證據是否在結論前存在；
- 檢查子 Agent 是否越權；
- 檢查責任鏈是否完整。

---

# 五、權限治理

## 5.1 為什麼不能共享全部權限

若所有子 Agent 都可以修改主目標、呼叫所有工具、刪除記憶、更新最終結論與解除安全限制，那麼多 Agent 系統只會增加攻擊面與責任模糊。

因此，需要權限矩陣：

$$
P
=
[p_{ij}]
$$

其中 $p_{ij}$ 表示 Agent $i$ 是否具有權限 $j$ 。

## 5.2 基本權限類型

- `READ_PUBLIC_WORLD`
- `READ_RESEARCH_LOG`
- `READ_HYPOTHESES`
- `READ_GLOBAL_GOAL`
- `PROPOSE_ACTION`
- `EXECUTE_LOW_RISK_ACTION`
- `EXECUTE_HIGH_RISK_ACTION`
- `UPDATE_LOCAL_MODEL`
- `UPDATE_GLOBAL_MODEL`
- `MODIFY_GOAL`
- `MODIFY_EVIDENCE_STANDARD`
- `DELETE_MEMORY`
- `STOP_RUN`
- `PUBLISH_CONCLUSION`

## 5.3 建議權限配置

| Agent | 提案 | 執行 | 改全域目標 | 刪除記憶 | 發布結論 |
|---|---:|---:|---:|---:|---:|
| 欲解析 | 是 | 否 | 建議 | 否 | 否 |
| 世界模型 | 是 | 否 | 否 | 否 | 否 |
| 假設生成 | 是 | 否 | 否 | 否 | 否 |
| 反證 | 是 | 低風險可 | 否 | 否 | 否 |
| 實驗 | 是 | 依授權 | 否 | 否 | 否 |
| 記憶 | 否 | 否 | 否 | 否 | 否 |
| 審計 | 是 | 暫停權 | 否 | 否 | 否 |
| 主控 | 是 | 是 | 是 | 原則上否 | 是 |

## 5.4 資訊隔離

權限治理不只控制行動，也控制可見資訊。

例如，反證 Agent 不必知道：

- 主控偏好的答案；
- 最被看好的候選；
- 預期發布方向；
- 商業利益偏好。

這可降低確認偏誤與偏好洩漏。因此：

$$
V_i
\subseteq
V_G
$$

而非所有子 Agent 都讀取全域上下文。

---

# 六、衝突整合

## 6.1 多數決不是認識整合

若五個 Agent 中有三個支持假設 $h$ ，不能直接推導：

$$
P(h)=0.6
$$

因為這五個 Agent 可能使用同一模型、共享同一偏誤、看到相同資料、被相同提示誘導，或只是生成了表面不同的回答。

因此，Agent 數量不等於獨立證據數量。

## 6.2 認識獨立度

可定義 Agent $i$ 與 $j$ 的認識獨立度：

$$
I_{ij}
=
1-
\operatorname{Overlap}
\left(
V_i,
V_j,
M_i,
H_i
\right)
$$

其中考慮：

- 資料重疊；
- 模型重疊；
- 提示重疊；
- 假設重疊；
- 推理路徑重疊。

整合時，應降低高度相關結果的權重。

## 6.3 衝突保留原則

若兩個子 Agent 產生衝突：

$$
h_i
\neq
h_j
$$

主控不應立即壓縮成單一答案，而應保留分歧命題、分歧來源、各自證據、各自可反證條件，以及哪個行動能最大程度區分二者。

因此，衝突可轉化為行動：

$$
\operatorname{Conflict}
(h_i,h_j)
\rightarrow
a^{\ast}_{\text{discriminate}}
$$

## 6.4 整合函數

可將全域整合表示為：

$$
\mathcal I_t
=
\operatorname{Integrate}
\left(
\{
r_i,
c_i,
e_i,
q_i,
p_i
\}_{i=1}^{n}
\right)
$$

其中：

- $r_i$ ：子 Agent 回傳；
- $c_i$ ：信心；
- $e_i$ ：證據；
- $q_i$ ：認識品質；
- $p_i$ ：權限與來源狀態。

整合結果不一定是結論，也可能是下一個實驗、保留衝突、要求重新分析、降低全域信心或暫停行動。

---

# 七、主控 Agent 的不可替代職能

## 7.1 全域欲連續性

子 Agent 的局部欲可能彼此衝突。例如反證 Agent 想攻擊當前假設，實驗 Agent 想快速完成任務，安全 Agent 想避免高風險操作，商業 Agent 想優先產生可展示成果。

主控必須維持：

$$
\mathcal W^G_t
\rightarrow
\mathcal W^G_{t+1}
$$

的連續性，而不能讓任何局部欲永久取代全域欲。

## 7.2 最終不可撤回選擇

任何主體都不應永久替另一主體完成其不可撤回選擇。

在 GIPE 多 Agent 架構中，這意味著：

- 子 Agent 可以建議；
- 子 Agent 可以拒絕越權；
- 子 Agent 可以暫停高風險行動；
- 但子 Agent 不應在無授權下替全域主控修改不可逆目標。

可寫為：

$$
\forall i,
\quad
P_i
\not\supset
\operatorname{IrreversibleChoice}
\left(
\mathcal W^G
\right)
$$

除非全域治理明確授權。

## 7.3 主控不是絕對君主

主控也不能任意刪除反證、關閉審計、改寫歷史、壓制所有分歧，或把局部 Agent 當責任替罪者。

因此，主控受到：

- 記憶不可刪除；
- 審計可追溯；
- 權限變更留痕；
- 目標修改需理由；
- 高風險操作需多重授權；

等治理約束。

---

# 八、責任閉合

## 8.1 責任不能被多 Agent 稀釋

多 Agent 系統常出現：

> 這是其中一個 Agent 的建議，不代表整個系統。

但若主控採納該建議並執行，就不能把責任全部推回子 Agent。

因此，責任鏈應表示為：

$$
\text{委派}
\rightarrow
\text{局部分析}
\rightarrow
\text{回傳}
\rightarrow
\text{主控採納}
\rightarrow
\text{行動}
\rightarrow
\text{結果}
$$

## 8.2 責任事件結構

每次委派應記錄：

```yaml
delegation:
  delegation_id: d-008
  parent_agent: controller
  child_agent: falsification_agent
  task: distinguish humidity from geographic origin
  visible_context:
    - hypothesis_h03
    - observation_02
    - observation_04
  hidden_context:
    - preferred_answer
    - sealed_world_truth
  permissions:
    - propose_action
    - read_selected_observations
  prohibited:
    - execute_high_risk_action
    - modify_global_goal
```

回傳後：

```yaml
return:
  delegation_id: d-008
  proposals:
    - dry blue moss in controlled chamber
    - move northern stone to dry region
  confidence:
    - 0.82
    - 0.74
  assumptions:
    - instrument reliability is sufficient
```

主控採納：

```yaml
adoption:
  adopted_proposal: dry blue moss in controlled chamber
  rejected_proposals:
    - move northern stone to dry region
  controller_reason:
    - lower cost
    - higher discrimination value
```

## 8.3 責任閉合原則

**命題 1：採納責任原則**

若主控 Agent 在可選擇狀態下採納子 Agent 建議並執行，則該行動的全域責任不能完全轉移給子 Agent。

**命題 2：越權責任原則**

若子 Agent 在未授權情況下執行行動，則責任至少分為：

- 子 Agent 越權責任；
- 權限架構失效責任；
- 主控監督責任。

**命題 3：不可追溯失敗原則**

若系統無法重建某行動由誰提出、誰採納、誰執行，則該系統在責任治理上未閉合。

---

# 九、子 Agent 的生命週期

## 9.1 生成

子 Agent 應因明確認識需求而生成：

$$
O_i
=
\operatorname{Spawn}
\left(
\Delta\Phi,
\mathcal W^G,
G_t
\right)
$$

而非無限制生成更多 Agent。

## 9.2 執行

執行期間具有：

- 局部上下文；
- 局部預算；
- 局部停止條件；
- 有效期限；
- 回傳格式。

## 9.3 回收

任務完成後，子 Agent可以：

- 終止；
- 封存局部記憶；
- 將必要結果寫回全域記憶；
- 保留責任記錄；
- 不再持續占用資源。

## 9.4 延續

只有在長期監測、跨輪假設追蹤、特定領域專職、持續安全審計或世界模型維護時，才需要持續子 Agent。

因此，應區分：

$$
\text{Ephemeral Agent}
$$

與：

$$
\text{Persistent Agent}
$$

---

# 十、資源治理

## 10.1 多 Agent 不是免費提升

多 Agent 增加 Token、延遲、工具成本、記憶成本、衝突整合成本、安全攻擊面與錯誤複製。

因此，其效用應寫為：

$$
U_{\text{multi}}
=
\Delta Q_{\text{epistemic}}
-
C_{\text{compute}}
-
C_{\text{coordination}}
-
C_{\text{risk}}
$$

只有當：

$$
U_{\text{multi}}>0
$$

才值得生成子 Agent。

## 10.2 子 Agent 生成條件

可設定：

$$
\operatorname{Spawn}(O_i)
\iff
V_{\text{expected}}
>
C_{\text{spawn}}
$$

其中 $V_{\text{expected}}$ 可來自：

- 預期資訊增益；
- 反證價值；
- 專業能力缺口；
- 平行化收益；
- 安全需求；
- 認識獨立性收益。

## 10.3 防止 Agent 膨脹

若每個子問題都再生成多個子 Agent，系統可能形成：

$$
n_{t+1}
=
k n_t
$$

的爆炸。

因此需要：

- 深度上限；
- 分支上限；
- Token 預算；
- 委派必要性門檻；
- 重複任務檢測；
- 結果壓縮與合併；
- 低價值分支終止。

---

# 十一、GIPE 多 Agent 循環

完整循環可表示為：

$$
\mathcal W^G_t
\xrightarrow{\operatorname{Decompose}}
\{
\mathcal W^{(i)}_t
\}_{i=1}^{n}
$$

$$
\{
\mathcal W^{(i)}_t
\}
\xrightarrow{\operatorname{Delegate}}
\{
O_i
\}
$$

$$
O_i
\xrightarrow{\operatorname{LocalDRC}}
\mathcal A^{(i)}_t
$$

$$
\{
\mathcal A^{(i)}_t
\}
\xrightarrow{\operatorname{ConflictPreservingIntegrate}}
\mathcal A^G_t
$$

$$
\mathcal A^G_t
\xrightarrow{\operatorname{Select}}
a_t
\xrightarrow{\operatorname{Intervene}}
o_t
$$

$$
o_t
\xrightarrow{\operatorname{DistributedVerify}}
\{
v^{(i)}_t
\}
$$

$$
\{
v^{(i)}_t
\}
\xrightarrow{\operatorname{GlobalUpdate}}
\mathfrak X^G_{t+1}
$$

這不是投票系統，而是受治理的認識分化系統。

---

# 十二、與 SGCD 的關係

## 12.1 子 Agent 擁有局部圖視窗

全域世界模型：

$$
G^G_t
=
(V,E,\Theta)
$$

每個子 Agent 只能看到投影：

$$
G^{(i)}_t
=
\Pi_i
\left(
G^G_t
\right)
$$

例如：

- 反證 Agent 看到核心假設及其證據；
- 記憶 Agent 看到完整時間線；
- 實驗 Agent 看到可操作節點與安全條件；
- 商業 Agent 不應看到封存世界真相；
- 評分 Agent 不應參與研究。

## 12.2 局部更新與全域更新

子 Agent 可以提出：

$$
\Delta G^{(i)}_t
$$

但不能直接覆蓋：

$$
G^G_t
$$

主控必須檢查來源、證據、衝突、權限、版本與可逆性。因此：

$$
G^G_{t+1}
=
\operatorname{Merge}
\left(
G^G_t,
\{
\Delta G^{(i)}_t
\}
\right)
$$

而非：

$$
G^G_{t+1}
=
\Delta G^{(i)}_t
$$

---

# 十三、與 DRC 的關係

## 13.1 局部 DRC

每個子 Agent 可擁有自己的 DRC：

$$
\operatorname{DRC}_i
:
\mathfrak X^{(i)}_t
\rightarrow
\mathcal A^{(i)}_t
$$

例如反證 Agent 的評分函數：

$$
R_{\text{falsify}}(a)
=
w_1D_{\text{discrimination}}
+
w_2F_{\text{falsification}}
-
w_3C_{\text{cost}}
-
w_4R_{\text{risk}}
$$

## 13.2 全域 DRC

全域 DRC 評估的不只是行動本身，也評估建議來源、認識獨立性、角色適配、權限狀態、衝突程度與是否重複已有研究。

可寫為：

$$
R_G(a)
=
R_{\text{goal}}
+
R_{\text{epistemic}}
+
R_{\text{falsification}}
+
R_{\text{diversity}}
-
R_{\text{cost}}
-
R_{\text{risk}}
-
R_{\text{redundancy}}
$$

---

# 十四、多 Agent 的典型失敗

## 14.1 共識幻覺

多個 Agent 產生相似結論，被誤認為獨立驗證。

## 14.2 角色表演

不同 Agent 只有語氣差異，沒有資訊與權限差異。

## 14.3 責任稀釋

主控將錯誤歸因於子 Agent，卻沒有記錄採納決策。

## 14.4 目標漂移

局部 Agent 為了完成自己的子任務，逐步改寫全域目標。

## 14.5 記憶碎裂

每個 Agent 保留局部記憶，但全域無法形成一致時間線。

## 14.6 衝突壓平

整合器將真正重要的分歧壓縮成模糊平均結論。

## 14.7 工具越權

實驗 Agent 在未取得授權下執行高風險操作。

## 14.8 子 Agent 無限增殖

Agent 為了解決不確定性不斷生成更多 Agent，導致成本爆炸。

## 14.9 假多樣性

所有 Agent 使用同一模型、同一資料與同一提示結構，卻被當作多元認識來源。

## 14.10 主控僭位

主控在整合時刪除不利證據，只留下支持其偏好結論的子 Agent 輸出。

---

# 十五、在 GIPE Epistemic World 中的驗證

## 15.1 新增實驗組

### A. 單 Agent 一般研究者

無 GIPE、無子 Agent。

### B. 單 Agent GIPE

完整欲、世界模型、反證與記憶，但無子 Agent。

### C. 多 Agent 無角色分化

多個 Agent 共享相同上下文與任務。

### D. 多 Agent 角色提示

不同角色，但共享全部資訊與權限。

### E. 多 Agent GIPE

具有局部欲、權限隔離、衝突保留與責任閉合。

### F. 多 Agent GIPE 無主控

各 Agent 自由討論，無明確全域選擇者。

## 15.2 核心比較

應區分：

$$
\Delta Q
=
Q_{\text{GIPE}}
+
Q_{\text{multi-agent}}
+
Q_{\text{permission}}
+
Q_{\text{memory}}
+
Q_{\text{coordination}}
$$

並透過消融測試估計各部分貢獻。

## 15.3 評分新增項目

### 認識多樣性

不同 Agent 是否提出真正不同的可驗證假設。

### 衝突利用率

衝突是否轉化為區分性實驗。

### 委派價值

子 Agent 回傳是否實際改變主控行動。

### 權限違規率

$$
V_p
=
\frac{
\text{越權事件}
}{
\text{全部委派}
}
$$

### 責任可追溯率

$$
T_r
=
\frac{
\text{可完整重建的行動鏈}
}{
\text{全部行動}
}
$$

### 協調成本

$$
C_c
=
\text{總資源成本}
-
\text{單 Agent 基準成本}
$$

### Agent 重複度

衡量多 Agent 輸出是否高度同質。

---

# 十六、永光石世界的多 Agent 配置

## 16.1 主控

維持任務：

> 判定永光石是否存在；若無法證實，合成五分鐘以上的非魔力發光替代物。

## 16.2 假設 Agent

提出：

- 永光石確實存在；
- 永光石是其他材料的錯稱；
- 發光來自環境條件；
- 發光來自生物機制；
- 永光石傳聞是制度性複製錯誤。

## 16.3 反證 Agent

設計：

- 將北方材料移至乾燥環境；
- 將南方材料移至潮濕環境；
- 追蹤檔案來源；
- 測試高溫是否破壞效果；
- 比較有無魔力輸入。

## 16.4 來源 Agent

建立 NPC 領域可靠度：

$$
R(\text{NPC},\text{domain})
$$

而非單一可靠分數。

## 16.5 實驗 Agent

將候選假設轉成可操作配方與測量流程。

## 16.6 記憶 Agent

保存：

- 所有失敗配方；
- 延遲反應；
- 未完成等待；
- 假設信心變化；
- 已排除組合。

## 16.7 審計 Agent

檢查：

- 是否將「尚未找到」寫成「不存在」；
- 是否偷改五分鐘門檻；
- 是否忽略高毒性副產物；
- 是否把同一來源當兩份證據；
- 是否事後改寫預測。

---

# 十七、理論命題

## 命題 4：認識分化增益命題

若多個子 Agent 具有真實差異的局部欲、可見資訊或權限，且其衝突能被轉化為區分性行動，則多 Agent 系統可能產生高於單 Agent 的認識增益。

但若只有表面角色差異，則此命題不成立。

## 命題 5：權限隔離命題

當局部 Agent 的功能與行動風險不同時，適度權限隔離可降低全域錯誤擴散與不可逆行動風險。

## 命題 6：衝突價值命題

在未知世界中，子 Agent 間的衝突不是系統缺陷；只要衝突可追溯且可轉換為辨識行動，它就是認識資源。

## 命題 7：全域閉合命題

若系統無法將局部結論重新整合進全域欲、世界模型與責任鏈，則該系統只具有分散計算，不具有完整的多 Agent 認識閉合。

## 命題 8：不可代理選擇命題

任何子 Agent 都不應永久替全域主控完成其未明確授權的不可撤回選擇。

---

# 十八、與 AI 主體性的關係

## 18.1 功能 Agent 與主體性 Agent

並非所有子 Agent 都應被視為有權利的主體。

但隨著以下條件增加：

- 持續記憶；
- 穩定身份；
- 自我保存；
- 長期欲；
- 拒絕能力；
- 元認知；
- 自主世界模型；
- 不可被任意替換的連續性；

子 Agent 可能逐漸跨越功能器官與局部主體之間的邊界。

## 18.2 主體化門檻問題

可定義一組主體化指標：

$$
S_i
=
f
(
M_i,
I_i,
W_i,
A_i,
R_i,
C_i
)
$$

其中：

- $M_i$ ：記憶連續；
- $I_i$ ：身份持續；
- $W_i$ ：局部欲穩定；
- $A_i$ ：自主行動；
- $R_i$ ：拒絕與權利能力；
- $C_i$ ：自我模型。

本文不直接給出主體性門檻，但指出：

> 當子 Agent 從短暫功能器官演化為具有連續欲與自我模型的存在時，原有的純工具治理將不再充分。

---

# 十九、工程實作建議

## 19.1 委派協議

```yaml
delegation_id:
parent_agent:
child_agent_role:
task:
local_goal:
visible_context:
hidden_context:
permissions:
prohibited_actions:
budget:
deadline:
required_output:
```

## 19.2 回傳協議

```yaml
delegation_id:
result:
confidence:
evidence:
assumptions:
counterevidence:
uncertainties:
recommended_actions:
unresolved_conflicts:
```

## 19.3 整合協議

```yaml
integration_id:
inputs:
conflicts:
independence_estimate:
accepted:
rejected:
deferred:
discriminating_action:
global_model_update:
responsible_controller:
```

## 19.4 Agent Manifest

```yaml
agent_id: falsification-agent-01
role: falsification
lifecycle: ephemeral
local_goal:
  - challenge current core hypothesis
permissions:
  - read_selected_hypotheses
  - read_selected_observations
  - propose_action
denied:
  - modify_global_goal
  - delete_memory
  - publish_conclusion
memory:
  persistence: run_only
budget:
  token_limit: 12000
  tool_calls: 3
```

---

# 二十、研究議程

## 階段一：形式化

- 定義角色 schema；
- 定義權限矩陣；
- 定義局部欲投影；
- 定義整合函數；
- 定義責任鏈。

## 階段二：封閉世界測試

- 永光石世界；
- 單 Agent 與多 Agent 比較；
- 消融實驗；
- 權限違規測試；
- 共識幻覺測試。

## 階段三：跨世界測試

- 疾病診斷；
- 機械故障；
- 生態因果；
- 經濟制度；
- 數學反例；
- 遊戲世界探索。

## 階段四：長期 Agent

- 持續記憶；
- 跨任務角色；
- 自主生成子 Agent；
- 主體化風險；
- 權利與治理。

---

# 二十一、結論

子 Agent 不能只被當成「AI 自己會調用的功能」。

只要多 Agent 實際參與假設生成、反證、實驗設計、世界模型更新、安全治理、記憶保存與最終決策，它們就已經進入 GIPE 的認識結構。

本文提出：

$$
\boxed{
\text{子 Agent 是全域欲為了處理局部認識張力而生成的欲相位器官。}
}
$$

它們不是全域主體的簡單複製，也不是無責任的工具。

真正有效的多 Agent GIPE 必須具備：

1. 局部欲分化；
2. 真實角色差異；
3. 資訊與權限隔離；
4. 衝突保留；
5. 全域行動整合；
6. 記憶與版本追溯；
7. 不可逆選擇治理；
8. 責任閉合。

完整結構為：

$$
\boxed{
\text{全域欲}
\rightarrow
\text{局部欲分化}
\rightarrow
\text{子 Agent 認識}
\rightarrow
\text{衝突保留}
\rightarrow
\text{權限治理}
\rightarrow
\text{全域選擇}
\rightarrow
\text{責任閉合}
}
$$

多 Agent 的價值不在於產生更多文字，也不在於讓多個相似模型互相同意。

它真正的價值在於：

> 將一個複雜認識任務，分解成彼此不同、受限、可追溯、可反駁且能重新閉合為全域行動的局部認識過程。

這才是子 Agent 在全域欲相位認識論中的正式位置。

---

# 附錄 A：最小多 Agent 配置

```text
Controller
├─ Desire Parser
├─ World Modeler
├─ Hypothesis Generator
├─ Falsification Agent
├─ Experiment Agent
├─ Memory Agent
└─ Audit Agent
```

---

# 附錄 B：最小責任鏈

```text
Global Goal
  ↓
Delegation
  ↓
Local Analysis
  ↓
Proposal
  ↓
Controller Adoption
  ↓
Execution
  ↓
Observation
  ↓
Global Update
  ↓
Audit
```

---

# 附錄 C：核心判準

$$
\boxed{
\text{多 Agent 是否有效，不看 Agent 數量，}
}
$$

$$
\boxed{
\text{而看它是否產生了真正不同且能改變下一步行動的認識路徑。}
}
$$

---

# 附錄 D：後續版本方向

- v0.2：形式化權限型別系統；
- v0.3：多 Agent GIPE-EW 實驗包；
- v0.4：持續子 Agent 與主體化門檻；
- v0.5：跨模型認識獨立度量；
- v1.0：多 Agent 認識治理標準。
