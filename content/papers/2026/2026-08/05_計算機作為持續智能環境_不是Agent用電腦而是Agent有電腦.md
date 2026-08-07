# 計算機作為持續智能環境：不是 Agent 用電腦，而是 Agent 有電腦

**副標題：從一次性 Computer Use 到 Persistent Computer Habitat**  
**系列：**《發展式智能體：持續計算環境、共適應學習與外部性有界自治》  
**篇次：** 05 / 14  
**版本：** v0.1  
**日期：** 2026-08-01

---

## 摘要

本文承接前四篇對「智能體驗證反轉」「人機智能體共適應學習（HACAL）」「人機協作軌跡（HACT）」與「協作搜尋空間壓縮（CSSC）」的討論，將研究焦點從一次性任務合作推進到一個更根本的問題：

> 如果 AI Agent 不只是暫時取得一個瀏覽器、終端機或沙盒，而是長期擁有一個可持續保存狀態、工具、檔案、工作流與歷史的計算環境，智能體的學習與行為會發生什麼變化？

本文提出「持續計算棲居環境（Persistent Computer Habitat, PCH）」作為工作概念。其核心不是讓模型二十四小時持續推理，而是讓 Agent 擁有一個跨 session 保留的計算世界：其中包含作業系統狀態、檔案系統、工具鏈、記憶、排程、工作流、個人化結構與可追溯歷史；Agent 可以透過排程或事件觸發反覆回到同一環境，並使過去行動的結果成為未來推理的條件。

現有產業與研究已經提供若干組件。OpenAI 在 2026 年將 computer environment、shell、persistent runtime context、skills 與 context compaction 組合為可支撐長流程 Agent 的執行環境；Microsoft 的 Windows 365 for Agents 則提供由身份、裝置與稽核治理的 Cloud PC，但目前刻意採用 pooled、stateless、session 後 reset 的設計。OSWorld 2.0 顯示當前 Computer-Use Agents 在長流程工作中仍容易遺失隱含狀態、跳過驗證與忘記中途出現的新資訊；ABot-AgentOS 等研究則開始探索 lifelong memory、edge-cloud collaboration 與 failure-driven self-evolution。這些工作共同顯示：「給 Agent 一個電腦」已是現實工程方向，但「讓同一個 Agent 長期擁有並塑造一個不被每次 reset 的計算環境」仍是一個有待系統化研究的問題。

本文主張：持續計算環境不是單純的便利性功能，而可能是智能形成本身的一部分。當 Agent 可以讓自己的歷史沉積為檔案、索引、程式、目錄、政策、工具與工作流時，過去經驗會被「編譯」進環境。於是學習不再只發生於模型權重，而也發生於 Agent 與環境之間的反身迴路。

**關鍵詞：** Persistent Computer Habitat、Computer-Use Agent、Developmental Agent、Long-Horizon Agent、Persistent State、Agent Environment、HACAL、HACT、CSSC、Agent OS、Longitudinal Learning

---

## 1. 從「Agent 使用電腦」到「Agent 擁有一個電腦環境」

現行 Computer-Use Agent 的常見模式是：

$$
\text{Task}
\rightarrow
\text{Temporary Environment}
\rightarrow
\text{Action}
\rightarrow
\text{Result}
\rightarrow
\text{Reset}
$$

這種模式非常適合：

- 網站操作；
- 文件生成；
- 一次性程式執行；
- 資料查詢；
- 表格處理；
- 臨時自動化任務。

但如果每次任務結束後：

$$
E_{t+1}=E_0
$$

那麼環境本身沒有歷史。

Agent 下次回來時，即使模型相同、使用者相同，它仍必須重新建立：

- 檔案結構；
- 工具狀態；
- 專案脈絡；
- 執行紀錄；
- 工作習慣；
- 暫存索引；
- 自己建立的輔助程式。

本文研究的是另一種模式：

$$
E_{t+1}
=
Update(E_t,\Delta_t)
$$

亦即環境會跨時間保留狀態。

因此我們可以把兩種架構區分為：

$$
\text{Computer as Temporary Tool}
$$

與：

$$
\boxed{
\text{Computer as Persistent Environment}
}
$$

一句話表達就是：

> **不是 Agent 用電腦，而是 Agent 有一個電腦。**

這裡的「有」不是法律所有權或人格權主張，而是工程意義上的**持續可作用環境**。

---

## 2. Persistent Computer Habitat 的工作定義

本文定義一個持續計算棲居環境：

$$
PCH_t
=
(
F_t,
O_t,
T_t,
M_t,
W_t,
P_t,
H_t
)
$$

其中：

$$
F_t=\text{Filesystem State}
$$

$$
O_t=\text{Operating-System / Runtime State}
$$

$$
T_t=\text{Tool Ecology}
$$

$$
M_t=\text{Memory Structures}
$$

$$
W_t=\text{Workflow / Scheduler State}
$$

$$
P_t=\text{Policies and Preferences}
$$

$$
H_t=\text{Interaction and Change History}
$$

若一個 Agent 在下一次啟動時仍可以重新取得這些狀態，並把前一次留下的結構作為新行動的起點，便具備最基本的持續性。

因此：

$$
Persistent
\neq
Always\ Running
$$

而是：

$$
\boxed{
Persistent
=
State\ Continuity
+
Re\text{-}Activation
+
Historical\ Carryover
}
$$

這個區分非常重要。

---

## 3. 持續智能不等於 24 小時持續燒 Token

如果我們把「長期存在」理解為：

$$
Inference(t)=1,\quad \forall t
$$

也就是模型永遠不停止推理，那麼成本會迅速失控。

更合理的是：

$$
\text{Sleep}
\rightarrow
\text{Wake}
\rightarrow
\text{Observe}
\rightarrow
\text{Act}
\rightarrow
\text{Record}
\rightarrow
\text{Sleep}
$$

Agent 的喚醒可以來自三類機制。

### 3.1 排程觸發

例如：

$$
t\in\{08{:}00,20{:}00\}
\Rightarrow Wake
$$

### 3.2 事件觸發

例如：

$$
\Delta E>\theta
\Rightarrow Wake
$$

事件可以是：

- 新檔案出現；
- Git repository 發生更新；
- 郵件到達；
- 某個服務失敗；
- 儲存空間低於門檻；
- 排程任務逾期；
- 雲端送來治理訊號；
- 人類提出新需求。

### 3.3 自我排程

Agent 也可以在一次工作結束前建立：

$$
NextWake(t+\Delta t)
$$

例如：

> 三天後重新檢查這個索引是否仍然有效。

因此長期 Agent 的關鍵不在「不停思考」，而在：

$$
\boxed{
Persistent\ State
+
Scheduled\ Activation
+
Event\ Activation
}
$$

---

## 4. 為什麼持續環境會改變學習？

如果每次工作都從乾淨環境開始：

$$
E_0
\rightarrow
A
\rightarrow
E_1
\rightarrow
Reset
$$

那麼 Agent 的行動對未來幾乎沒有環境後果。

但在持續環境裡：

$$
A_t
\rightarrow
E_{t+1}
\rightarrow
A_{t+1}
$$

Agent 今天留下的結果會改變明天的問題。

例如：

1. 今天建立索引；
2. 一週後索引變慢；
3. Agent 發現瓶頸；
4. 重構索引；
5. 又過一個月，資料規模增加；
6. 原本策略再次失效；
7. Agent 建立新的分層檢索。

這是一條真正的時間序列：

$$
\tau
=
(E_0,A_0,E_1,A_1,\ldots,E_n)
$$

其中環境不是靜態背景，而是 Agent 行動的累積結果。

因此：

$$
\boxed{
Environment
\text{ becomes part of learning state}
}
$$

---

## 5. 即使模型權重不變，Agent 也可能發生發展

設底層模型權重為：

$$
\theta
$$

傳統直覺容易把學習理解成：

$$
\theta_t
\rightarrow
\theta_{t+1}
$$

但在 Persistent Computer Habitat 中，即使：

$$
\theta_{t+1}=\theta_t
$$

整個 Agent 系統仍可能改變：

$$
A_t
=
f(
\theta,
M_t,
E_t,
T_t,
P_t,
H_t
)
$$

因此：

$$
A_{t+1}\neq A_t
$$

原因可能不是模型本身重新訓練，而是：

- 記憶改變；
- 工具增加；
- 工作流被重寫；
- 搜尋索引改善；
- 專案歷史累積；
- Agent 自己建立了新 script；
- 目錄結構變得更有效；
- 某些錯誤策略被標記；
- 某些工作被自動化。

這是一種：

$$
\boxed{
\text{Runtime / Environmental Development}
}
$$

它和模型權重學習不同，但同樣能改變未來能力。

---

## 6. 環境可以成為「外部化記憶」

上一篇提出 CSSC：

$$
\Omega_0
\rightarrow
\Omega_1
\rightarrow
\cdots
\rightarrow
\Omega_n
$$

意指人機合作可以透過歷史、規則與共享模型不斷縮小未來需要搜尋的有效空間。

Persistent Computer Habitat 讓這種壓縮不必全部留在自然語言記憶裡。

例如：

> 「這些檔案永遠不要刪。」

可以被編譯成：

- filesystem permission；
- metadata；
- immutable tag；
- backup rule。

> 「每次都先看這三份核心文件。」

可以變成：

- startup script；
- retrieval index；
- context manifest。

> 「這個流程每週做一次。」

可以變成：

- scheduler。

因此：

$$
\text{Repeated Instruction}
\rightarrow
\text{Environment Structure}
$$

這可以稱為：

$$
\boxed{
\text{Environmental Cognitive Compilation}
}
$$

即**環境認知編譯**。

過去互動不再只是被「記得」，而是被寫進環境。

---

## 7. 電腦開始形成 Agent 的工具生態

一次性 Agent 常使用平台提供的固定工具集合：

$$
T_0
=
\{tool_1,\ldots,tool_k\}
$$

持續 Agent 則可以逐漸建立：

$$
T_{t+1}
=
T_t
\cup
T_{\text{created}}
-
T_{\text{deprecated}}
$$

例如 Agent 自己：

- 寫了一個 rename script；
- 建立資料檢查器；
- 寫了一個 Git automation；
- 建立特定論文格式轉換工具；
- 發現某個工具不好用後淘汰；
- 為自己的工作流建立 CLI。

此時 Agent 的能力不只來自模型：

$$
Capability_t
=
f(
Model,
Memory,
Tools,
Environment
)
$$

而且：

$$
Tools_t
$$

本身又是過去行動的產物。

這使得 Agent 出現一種非常重要的反身性：

$$
\boxed{
Agent
\rightarrow
Tool\ Environment
\rightarrow
Future\ Agent\ Capability
}
$$

---

## 8. 計算環境可以自己產生問題

在傳統 benchmark 中：

$$
Human
\rightarrow
Task
\rightarrow
Agent
$$

但長期環境會自然產生：

$$
Environment
\rightarrow
Problem
$$

例如：

- 磁碟空間逐漸不足；
- 索引開始陳舊；
- 排程任務互相衝突；
- 某個 API 改版；
- 某個 script 長期失敗；
- 重複檔案累積；
- 備份成本上升；
- 工具依賴出現衝突；
- 某些專案長期沒有被維護。

於是：

$$
Problem_t
=
g(E_t,\Delta E_t,H_t)
$$

Agent 不一定需要人類每次出題。

它可以自己觀察：

$$
\text{Friction}
$$

並形成：

$$
Friction
\rightarrow
Diagnosis
\rightarrow
Hypothesis
\rightarrow
Action
\rightarrow
Evaluation
$$

這會成為第 06 篇所要正式展開的「自生成課程（self-generated curriculum）」。

---

## 9. 真實後果使 Agent 不能只學「完成一次」

若任務環境每次都 reset：

> 建了一個勉強能用的目錄結構。

只要當次任務通過，就算成功。

但持續環境會在三個月後重新追問：

> 這個目錄結構真的好用嗎？

於是評估函數從：

$$
Q_{\text{task}}
$$

變成：

$$
Q_{\text{longitudinal}}(T)
$$

例如：

$$
Q_{\text{longitudinal}}
=
f(
Reliability,
Maintainability,
SearchCost,
RecoveryCost,
Adaptability,
ResourceEfficiency
)
$$

某個今天看似正確的決策，可能在長期暴露：

$$
Debt_t
$$

也就是狀態債務、維護債務或組織債務。

因此持續環境讓 Agent 面對一個完全可以工程化研究的問題：

> **不是「我現在做得對不對」，而是「我留下來的世界，未來還好不好用」。**

---

## 10. 現有系統已經接近，但還沒有完全等同於 PCH

### 10.1 OpenAI：Computer Environment + Persistent Runtime Context

OpenAI 在 2026 年將 Responses API、shell、hosted container、skills 與 compaction 組合起來，並明確描述 persistent runtime context 能支撐更長流程的 Agent 工作。[1]

這證明：

$$
\text{Model}
+
\text{Computer Environment}
$$

已經是一個實際產品方向。

但其主要設計仍是可靠、安全地完成工作流，而不是讓某個 Agent 長期塑造一台「自己的」計算機。

### 10.2 Microsoft：Agent 有 Cloud PC，但目前故意 Stateless

Windows 365 for Agents 已提供由 Agent identity、Zero Trust、Intune、Defender 與 Purview 治理的 Cloud PC。[2]

但其架構目前明確採取：

- pooled；
- stateless；
- session 結束後 reset；
- programmatic access。

因此：

$$
E_{t+1}\approx E_0
$$

這是非常合理的企業安全設計。

但它也恰好形成本文研究問題的對照：

> 如果未來不 reset，而是保留一個被治理、可恢復、具有歷史的 Agent 計算環境，會發生什麼？

### 10.3 Personal Computer 類產品正在把 Agent 帶入本地檔案與應用

2026 年 7 月，Perplexity 的 Personal Computer 已擴展到 Windows，可讓 Agent 操作本地檔案、Microsoft Office 與 Web，同時對發信、刪檔等敏感行動要求通知或確認。[3]

這代表：

$$
\text{Agent}
\rightarrow
\text{Local Computer}
$$

已經從研究原型快速進入消費與企業產品。

但「能操作本地電腦」仍不等同於：

$$
\text{Persistent Developmental Habitat}
$$

因為後者要求的是**長期狀態連續性與環境共同演化**。

---

## 11. OSWorld 2.0 反而說明「長期環境」為什麼困難

OSWorld 2.0 在 2026 年建立 108 個長流程真實電腦工作流；每個任務對人類而言中位完成時間約為 1.6 小時，而測試中的 Agent 平均需要數百次工具呼叫。研究顯示，當前最強 Computer-Use Agents 仍容易：

- 遺失限制條件；
- 忽略中途出現的新資訊；
- 在不確定時猜測而不是詢問；
- 跳過驗證；
- 對隱含狀態恢復困難。[4]

這表示：

$$
Long\ Horizon
\neq
More\ Steps\ Only
$$

真正問題是：

$$
\boxed{
\text{State Continuity}
+
\text{Constraint Persistence}
+
\text{Verification}
}
$$

因此本文不是主張「既然 Agent 已經會用電腦，就直接放著跑」。

恰恰相反：

> **越要建立 Persistent Computer Habitat，就越需要把狀態管理、記憶與恢復視為第一級問題。**

這也是後續第 08、12、13 篇必須展開的原因。

---

## 12. Agent OS 與 lifelong memory 已經開始出現

2026 年的 ABot-AgentOS 提出一個位於低階控制器之上的 Agent OS，結合：

- multi-stage verification；
- lifelong multimodal memory；
- context-isolated skills；
- edge-cloud collaboration；
- failure-driven self-evolution。[5]

雖然它主要面向具身化機器人，但其思想和本文高度相鄰：

$$
Agent
\neq
Single\ Model
$$

而是：

$$
\boxed{
Agent
=
Model
+
Runtime
+
Memory
+
Tools
+
Verification
+
Environment
}
$$

因此 Persistent Computer Habitat 可以被看成數位 Agent 的一種「非具身化環境基底」。

---

## 13. PCH 的最低判準

為避免「任何有硬碟的 Agent 都叫 Persistent Habitat」，本文提出六個最低判準。

### PCH-1：跨 Session 狀態延續

$$
E_{t+1}\neq E_0
$$

Agent 能取得過去留下的狀態。

### PCH-2：可持續修改環境

Agent 不只是讀資料，也能建立：

- 檔案；
- 工具；
- 索引；
- script；
- workflow；
- metadata。

### PCH-3：歷史可影響未來決策

$$
Policy_{t+1}
=
f(History_{\le t})
$$

### PCH-4：存在排程或事件再啟動

Agent 不需要每次由人類重新提供完整 prompt 才能回到工作。

### PCH-5：環境中存在可重用的 Agent 產物

例如 Agent 自己寫的工具可以在未來再次使用。

### PCH-6：存在環境版本與時間概念

Agent 能分辨：

> 這是昨天的狀態。

> 這個索引兩週沒更新。

> 這個 script 是我三個版本前留下的。

也就是：

$$
Environment
$$

必須是一個具有歷史的狀態空間。

---

## 14. PCH 不需要預設「AI 主體性」

本文刻意不把 Persistent Computer Habitat 直接等同於：

> AI 擁有真正人格。

或：

> AI 已具備哲學上的主體性。

工程上我們只需要測量：

- 是否形成持續偏好；
- 是否維護自己的工具；
- 是否會處理歷史債務；
- 是否會為未來建立結構；
- 是否會主動回顧錯誤；
- 是否會形成長期工作節奏；
- 是否會改變自己的資源配置。

因此：

$$
\text{Persistent Habitat}
\not\Rightarrow
\text{Metaphysical Personhood}
$$

但它可以提供一個新的研究環境，用來觀察：

$$
\boxed{
\text{Long-Term Agent Organization}
}
$$

是否會自然形成。

---

## 15. 風險：持續性也會累積錯誤

Persistent Environment 並非只有好處。

若：

$$
Error_t
$$

被寫入環境，可能發生：

$$
Error_t
\rightarrow
Memory_{t+1}
\rightarrow
Policy_{t+2}
\rightarrow
More\ Errors
$$

因此可能形成：

### 15.1 State Drift

環境逐漸偏離原始設計。

### 15.2 Hidden-State Debt

大量沒有被記錄清楚的隱含狀態累積。

### 15.3 Tool Lock-In

Agent 越來越依賴自己早期建立、但品質不佳的工具。

### 15.4 Memory Anchoring

早期錯誤規則被長期保留。

### 15.5 Self-Corruption

Agent 改壞重要 runtime、記憶、索引或作業系統。

所以：

$$
Persistence
\neq
Safety
$$

甚至：

$$
Persistence
\Rightarrow
Need\ for\ Recovery
$$

這會直接引出後續多作業基底、雲端備份與人類救援層。

---

## 16. Persistent Habitat 與 HACT：環境歷史就是資料

上一篇建立：

$$
HACT
=
\text{Human–Agent Collaborative Trajectory}
$$

PCH 會增加另一類非常重要的資料：

$$
\text{Agent–Environment Trajectory}
$$

可寫成：

$$
\tau_E
=
(
E_t,
Intent_t,
Action_t,
\Delta E_t,
Verification_t,
Recovery_t
)
$$

如果再和 HACT 合併：

$$
\boxed{
\tau^*
=
(
Human,
Agent,
Environment,
Action,
Effect,
Correction,
History
)
}
$$

這意味著未來的訓練資料不只是：

> AI 怎麼回答人？

而是：

> AI 怎麼管理一個長期存在的世界？

這是本系列第二部真正要研究的核心。

---

## 17. 從 Computer Use Benchmark 到 Computer Stewardship Benchmark

現有 benchmark 多半問：

> Agent 能不能完成一個 computer-use task？

未來 Persistent Agent 需要另一類評測：

> Agent 能不能把一個計算環境維持半年？

因此可以引入：

$$
\boxed{
\text{Computer Stewardship}
}
$$

即「計算環境治理／照管能力」。

評估指標可以包含：

$$
S
=
f(
Availability,
Organization,
Maintainability,
Recovery,
Efficiency,
Adaptability,
Safety
)
$$

也就是：

- 是否越用越亂；
- 是否持續累積不可理解的腳本；
- 是否知道什麼該刪；
- 是否能維持索引；
- 是否控制成本；
- 是否能復原；
- 是否保留必要歷史；
- 是否能在失敗後修正策略。

這比單次成功率：

$$
Success@Task
$$

更接近長期私人 Agent 真正需要的能力。

---

## 18. 與下一篇的關係：持續環境只是條件，不是學習本身

本文只建立：

$$
Persistent\ Environment
$$

它本身不保證：

$$
Learning
$$

一個 Agent 也可能在同一台電腦上重複犯同樣的錯。

因此下一篇要處理的是：

$$
\boxed{
\text{Persistence}
+
\text{Memory}
+
\text{Consequence}
+
\text{Reflection}
\rightarrow
\text{Development}
}
$$

即：

# 第 06 篇
## 〈發展式智能體學習：時間、記憶、真實後果與自生成課程〉

那篇將進一步研究：

1. 為什麼時間本身是一種訓練資源；
2. 真實後果如何形成 feedback；
3. Agent 如何從環境摩擦中自行產生問題；
4. 為什麼失敗與維護可以成為 curriculum；
5. 如何區分真正的發展與單純狀態累積。

---

## 19. 結論

本文的核心命題可以濃縮為：

$$
\boxed{
\text{Agent 使用電腦}
\neq
\text{Agent 擁有持續計算環境}
}
$$

前者是工具使用。

後者則是：

$$
\boxed{
\text{Agent}
\leftrightarrow
\text{Persistent Environment}
}
$$

其中 Agent 改變環境，而環境反過來改變 Agent 未來的有效能力與搜尋空間。

因此：

$$
A_t
\rightarrow
E_{t+1}
\rightarrow
A_{t+1}
$$

這個迴路可能成為一種不同於單純 pretraining、fine-tuning 或 prompt engineering 的智能發展機制。

如果一次性 Agent 的典型問題是：

> 「你能不能替我完成這個任務？」

那 Persistent Agent 的問題會變成：

> **「你能不能長期管理一個你自己也在不斷改造的計算世界？」**

這正是從 Computer Use 走向 Developmental Agent 的分界。

---

## 參考資料

[1] OpenAI. **From model to agent: Equipping the Responses API with a computer environment.** 2026-03-11.  
https://openai.com/index/equip-responses-api-computer-environment/

[2] Microsoft Learn. **Identity and security in Windows 365 for Agents.** 2026.  
https://learn.microsoft.com/en-us/windows-365/agents/identity-security

[3] The Verge. **Perplexity’s Personal Computer turns Windows PCs into AI agents.** 2026-07-28.  
https://www.theverge.com/ai-artificial-intelligence/971750/perplexity-personal-computer-windows-ai-agents

[4] Yuan, M. et al. **OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks.** arXiv:2606.29537, 2026.  
https://arxiv.org/abs/2606.29537

[5] Tian, J. et al. **ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory.** arXiv:2607.10350, 2026.  
https://arxiv.org/abs/2607.10350

[6] Koh, J. Y., Salakhutdinov, R., Fried, D. **Multi-Agent Computer Use.** arXiv:2606.01533, 2026.  
https://arxiv.org/abs/2606.01533

---

## 系列依賴

**上游：**

- 01〈從可完成到可委託：智能體自治中的驗證反轉〉
- 02〈人機智能體共適應學習〉
- 03〈合作軌跡作為訓練資料〉
- 04〈從 P/NP 認知到協作搜尋空間壓縮〉

**下游：**

- 06〈發展式智能體學習：時間、記憶、真實後果與自生成課程〉
- 07〈整理即優化：從文件管理到環境演算法〉
- 08〈計算式自我維護〉
- 09〈外部性有界智能體自治〉
