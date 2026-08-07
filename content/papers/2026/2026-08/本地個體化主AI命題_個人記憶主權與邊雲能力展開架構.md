# 本地個體化主 AI 命題：個人記憶主權與邊雲能力展開架構

**English Title:** *The Local Individualized Main AI Hypothesis: Personal Memory Sovereignty and Edge–Cloud Capability Expansion*

**作者：** Neo.K  
**AI 協作：** Aletheia  
**研究脈絡：** EveMissLab / Logic Matrix / GCMS / 認知解構學 2.0  
**文件類型：** 命題猜想論文  
**版本：** v0.1  
**日期：** 2026-07-30  

---

## 摘要

本文提出「本地個體化主 AI 命題」（Local Individualized Main AI Hypothesis, LIMAIH）。該命題主張，未來真正具有長期個體化能力的人工智能，不應只被理解為某家雲端平台中的使用者設定、對話歷史或經過個人化微調的共享模型，而應由一個主要位於個人裝置與私人運算環境中的主 AI 控制層承擔。此主 AI 掌握個人身份、長期記憶、認知原子因果基底、偏好、目標、關係、專案狀態、權限政策、模型路由與正式記憶寫回；外部大型模型、專用模型、搜尋服務與遠端 Agent 則作為可替換、可限制且按需調用的能力服務。

本文所稱「本地」並不等於所有推理、訓練與資料處理永遠只在手機內完成。更精確的架構是：手機或隨身裝置保存最低持續核心、身份憑證、核心記憶索引與本地決策政策；個人電腦、家庭伺服器或 NAS 保存較大的私人記憶、知識庫和本地模型；雲端模型池則提供高成本推理、最新知識、多模態生成與彈性算力。斷線時，個體主 AI 仍保持有限但連續的存在；連線時，它可以在不交出完整個人狀態的條件下展開外部能力。

本文進一步提出「本地主權、雲端能力」原則。個體化 AI 的核心價值不只在隱私、低延遲或離線可用，而在於個人記憶、形成歷史、身份代理權、權限規則與長期方法不再附著於單一模型供應商。使用者可以更換雲端大模型、專用 Agent 或模型市場，而不必重建自己的整體 AI 關係與記憶世界。外部模型只取得完成特定任務所需的最小資訊，返回結果首先進入候選記憶區，不能直接改寫正式個人記憶。

本文將個人記憶分為核心、私人、下載、共享、暫存、候選與接受區，並提出可下載的「知識—能力包」：其不只是向量資料或提示詞，而是同時包含知識、認知原子、工作流、工具介面、測試、版本、簽章與權限要求。主 AI 可依來源、相容性、價值、風險和個人政策決定是否安裝、隔離、試用、撤銷或升級。

本文結合端側模型、邊雲協同、個人化記憶、任務範圍資訊揭露、裝置持續學習和個人 AI 堆疊研究，提出十八項命題與猜想、十五類失敗模式、九組可否證實驗及一個六層實作架構。本文不主張現有手機模型已足以實現完整主 AI，而是指出，當前 Apple、Android 與 Windows 生態已把端側模型、本地模型執行和可替換模型介面逐步推入作業系統與應用層；研究界也開始處理邊雲個人記憶、最小揭露、端側 Agent 加速和本地—雲端協作。這些發展共同支持一個方向：通用雲端模型可能成為共享認知基礎設施，而真正持續且屬於個人的智能控制層，則逐步下沉到使用者自己的裝置與私人資料環境。

**關鍵詞：** 本地主 AI、個體化 AI、個人記憶主權、邊雲協同、端側模型、手機 AI、GCMS、外掛記憶、能力包、模型路由、最小揭露、個人資料庫、數位身份、持續 Agent、可替換雲端模型

---

# 0. 研究定位與聲明

本文延續以下理論：

1. 結構生成式分布記憶；
2. 壓縮全局智能；
3. 認知原子因果基底；
4. 主 AI 的重構式與養成式形成路線；
5. 主 Agent—子 Agent 協同與權限治理。

本文的新增問題是：

> **為什麼要建立這種主 AI？**

本文的回答是：

> 因為它可能成為未來每個人的個體智能控制層，使身份、記憶、目標、權限與長期形成史由個人持有，而通用大模型則轉化為可替換的外部能力基礎設施。

本文不主張：

- 手機可以獨立運行所有前沿模型；
- 純本地一定比雲端安全；
- 所有私人資料都應永久保留；
- 本地資料庫天然不會被攻擊；
- 使用者一定有能力管理全部 AI 權限；
- 個人主 AI 可無限制代表使用者；
- 模型供應商一定願意提供可替換介面；
- 所有能力包都能安全移植；
- 個人化等於強化使用者既有偏見；
- 功能性身份連續等於人工主體性。

本文所稱「個體化」是工程與治理概念，表示系統的長期狀態、個人資料、決策政策與模型選擇以使用者為主要控制單位。

---

# 1. 問題的提出：共享大模型如何真正成為個人的 AI？

## 1.1 雲端個人化的結構限制

現有雲端 AI 的個人化通常包含：

- 帳號設定；
- 對話歷史；
- 少量長期偏好；
- 服務端記憶；
- 平台內的檔案與工具；
- 供應商特定的 Agent 設定。

其狀態可以表示為：

$$
S_{\mathrm{cloud},u}
=
\left(
M_p,
H_u,
P_u,
F_u
\right),
$$

其中：

- $M_p$ ：平台模型；
- $H_u$ ：使用者歷史；
- $P_u$ ：偏好；
- $F_u$ ：平台中的檔案或連線資源。

問題在於：

$$
S_{\mathrm{cloud},u}
\subseteq
\operatorname{Platform}_p.
$$

當使用者更換平台：

$$
p_1
\rightarrow
p_2,
$$

長期狀態通常不能完整轉移：

$$
\operatorname{Transfer}
\left(
S_{\mathrm{cloud},u}^{p_1}
\right)
\neq
S_{\mathrm{cloud},u}^{p_2}.
$$

因此，使用者雖然可以更換模型，卻不一定能攜帶已形成的個人 AI。

---

## 1.2 模型能力與個人連續性是不同資產

設雲端模型能力為：

$$
C_{\mathrm{foundation}}.
$$

設個人連續狀態為：

$$
S_{\mathrm{person}}
=
\left(
I,
M,
G,
P,
H,
R
\right),
$$

其中：

- $I$ ：身份與代理關係；
- $M$ ：長期記憶；
- $G$ ：個人因果、專案與關係圖；
- $P$ ：權限與偏好政策；
- $H$ ：共同工作和決策歷史；
- $R$ ：可調用能力與資源目錄。

兩者不應被綁定為：

$$
C_{\mathrm{foundation}}
\equiv
S_{\mathrm{person}}.
$$

更合理的結構是：

$$
\boxed{
S_{\mathrm{person}}
\text{ 持續存在，}
\quad
C_{\mathrm{foundation}}
\text{ 可以替換。}
}
$$

---

# 2. 本地個體化主 AI 的正式定義

本文定義個體化主 AI：

$$
A_u^{\mathrm{local}}
=
\left(
M_u,
\mathcal M_u,
\mathcal G_u,
\mathcal P_u,
\mathcal R_u,
\mathcal H_u
\right),
$$

其中：

- $M_u$ ：本地常駐主模型或主控模型組；
- $\mathcal M_u$ ：個人記憶系統；
- $\mathcal G_u$ ：個人認知、因果、專案與關係圖；
- $\mathcal P_u$ ：權限、披露與寫回政策；
- $\mathcal R_u$ ：模型、Agent、工具與裝置路由器；
- $\mathcal H_u$ ：版本、決策和審計歷史。

其完整能力不是單一本地模型能力，而是：

$$
\mathcal C_u^{\mathrm{total}}
=
\mathcal C_u^{\mathrm{resident}}
\oplus
\mathcal C_u^{\mathrm{device}}
\oplus
\mathcal C_u^{\mathrm{home}}
\oplus
\mathcal C_u^{\mathrm{cloud}}.
$$

---

# 3. 本地主權、雲端能力原則

## 3.1 本地控制平面

本地端主要負責：

$$
\mathcal L_{\mathrm{control}}
=
\left\{
\begin{aligned}
&\text{身份、記憶、個人狀態、}\\
&\text{權限、資料選擇、模型路由、}\\
&\text{候選寫回、正式接受、審計}
\end{aligned}
\right\}.
$$

## 3.2 遠端運算平面

遠端主要負責：

$$
\mathcal C_{\mathrm{remote}}
=
\left\{
\begin{aligned}
&\text{高成本推理、最新資訊、}\\
&\text{大型多模態生成、專用模型、}\\
&\text{大規模搜尋、模擬與計算}
\end{aligned}
\right\}.
$$

## 3.3 核心分離

$$
\boxed{
\text{個人狀態控制權}
\neq
\text{最大單次推理能力}.
}
$$

雲端模型可以比本地模型強，但不應因此自然獲得：

- 全部私人記憶；
- 對外代表權；
- 正式寫回權；
- 支付權；
- 長期身份控制；
- 無限制工具權限。

---

# 4. 「本地」不是純本地

## 4.1 分層裝置拓撲

完整個人 AI 可以分為：

$$
\mathcal T_u
=
\left(
D_{\mathrm{mobile}},
D_{\mathrm{personal}},
D_{\mathrm{home}},
C_{\mathrm{cloud}}
\right).
$$

### 手機或隨身裝置

保存：

- 最低持續核心；
- 個人身份憑證；
- 核心政策；
- 高頻記憶索引；
- 基本本地模型；
- 即時感知和通知；
- 低風險快速決策。

### 個人電腦

保存：

- 更大本地模型；
- 工作資料；
- 專案狀態；
- 本地工具；
- 程式執行環境；
- 高解析度私人文件。

### 家庭節點或 NAS

保存：

- 長期資料庫；
- 多裝置同步；
- 本地向量索引；
- 模型和能力包倉庫；
- 備份；
- 家庭共享記憶；
- 私人運算排程。

### 雲端能力池

提供：

- 前沿大模型；
- 最新資料；
- 外部搜尋；
- 高成本生成；
- 專業服務；
- 臨時高算力。

---

## 4.2 斷線與連線雙狀態

斷線時：

$$
A_u^{\mathrm{offline}}
=
\left(
M_u,
\mathcal M_u^{\mathrm{local}},
\mathcal G_u,
\mathcal P_u,
\mathcal T_u^{\mathrm{local}}
\right).
$$

連線時：

$$
A_u^{\mathrm{online}}
=
A_u^{\mathrm{offline}}
\oplus
\left\{
M_j^{\mathrm{cloud}},
A_k^{\mathrm{remote}},
D_l^{\mathrm{current}}
\right\}.
$$

理想系統滿足：

$$
\operatorname{Continuity}
\left(
A_u^{\mathrm{offline}},
A_u^{\mathrm{online}}
\right)
=1.
$$

即能力可伸縮，但個人狀態不因斷線或模型切換而消失。

---

# 5. 本地記憶主權

## 5.1 個人記憶的分區

定義：

$$
\mathcal M_u
=
\mathcal M_{\mathrm{core}}
\cup
\mathcal M_{\mathrm{private}}
\cup
\mathcal M_{\mathrm{downloaded}}
\cup
\mathcal M_{\mathrm{shared}}
\cup
\mathcal M_{\mathrm{temporary}}
\cup
\mathcal M_{\mathrm{candidate}}
\cup
\mathcal M_{\mathrm{accepted}}.
$$

### 核心記憶

- 身份；
- 長期目標；
- 重要關係；
- 不可輕易覆寫的政策；
- 關鍵決策歷史；
- 核心認知基底。

### 私人記憶

- 個人文件；
- 通訊；
- 健康、財務與生活紀錄；
- 工作資料；
- 私人專案；
- 本地媒體。

### 下載記憶

- 公開知識包；
- 職業知識包；
- 法規包；
- 產品包；
- 學科原子包；
- 世界設定包。

### 共享記憶

- 家庭；
- 團隊；
- 公司；
- 社群；
- 專案共同知識。

### 暫存記憶

- 任務上下文；
- 中間資料；
- 可自動過期的敏感內容；
- 未完成草稿。

### 候選記憶

- 外部模型生成結果；
- 新推論；
- 未驗證摘要；
- 新下載包；
- 子 Agent 回報。

### 接受記憶

- 通過來源、版本、矛盾和權限檢查後的正式狀態。

---

## 5.2 記憶寫回路徑

外部模型的輸出必須經過：

$$
y_j
\rightarrow
\mathcal M_{\mathrm{candidate}}
\rightarrow
\mathsf{Verify}
\rightarrow
\mathsf{PolicyCheck}
\rightarrow
\mathcal M_{\mathrm{accepted}}.
$$

禁止預設：

$$
y_j
\rightarrow
\mathcal M_{\mathrm{accepted}}.
$$

---

## 5.3 記憶所有權與控制權

本文不將複雜法律所有權問題簡化為單一技術宣言，而提出最低工程要求：

1. 使用者可以匯出；
2. 使用者可以刪除；
3. 使用者可以查看來源；
4. 使用者可以撤銷能力包；
5. 使用者可以更換模型；
6. 使用者可以設定同步範圍；
7. 使用者可以禁止特定資料上雲；
8. 使用者可以查看正式寫回紀錄；
9. 使用者可以回滾到先前版本。

---

# 6. 任務範圍最小揭露

## 6.1 雲端不需要完整個人狀態

設外部任務為：

$$
q.
$$

主 AI 具有完整個人狀態：

$$
S_u.
$$

雲端真正需要的局部投影為：

$$
S_u^{(q)}
=
\operatorname{Project}
\left(
S_u,
q
\right).
$$

理想披露封包：

$$
B_q
=
\operatorname{Minimize}
\left(
S_u^{(q)}
\right),
$$

使：

$$
U(M_j,q,B_q)\geq\theta_U,
$$

同時：

$$
I(B_q;S_u^{\mathrm{sensitive}})
\rightarrow 0.
$$

---

## 6.2 本地披露治理器

披露程序：

$$
\boxed{
\begin{aligned}
q
&\xrightarrow{\mathsf{Interpret}}
z_q\\
S_u
&\xrightarrow{\mathsf{Select}}
S_u^{(q)}\\
&\xrightarrow{\mathsf{Abstract}}
\widetilde S_u^{(q)}\\
&\xrightarrow{\mathsf{Redact}}
B_q\\
&\xrightarrow{\mathsf{RemoteCall}}
M_j.
\end{aligned}
}
$$

例如：

- 真實姓名可替換為角色標記；
- 精確地址可降級為城市；
- 完整行程可只提供可用時段；
- 完整財務紀錄可只提供預算範圍；
- 全部醫療史可只提供與當前預約相關的必要條件。

---

# 7. 可下載記憶與能力包

## 7.1 記憶包不是普通檔案

定義記憶—能力包：

$$
\mathcal P_i
=
\left(
K_i,
A_i,
W_i,
T_i,
E_i,
V_i,
S_i,
\Gamma_i
\right),
$$

其中：

- $K_i$ ：知識；
- $A_i$ ：認知原子與因果關係；
- $W_i$ ：工作流；
- $T_i$ ：工具介面；
- $E_i$ ：測試與驗證；
- $V_i$ ：版本與依賴；
- $S_i$ ：來源和簽章；
- $\Gamma_i$ ：要求的權限。

---

## 7.2 包類型

### 知識包

例如：

- 某國稅法；
- 某款設備維修；
- 某門學科；
- 某座城市旅遊；
- 某公司內部制度。

### 方法包

例如：

- 論文審查；
- 法律文件整理；
- 程式碼審查；
- 財務報表分析；
- 專案風險評估。

### Agent 包

包含：

- 角色；
- 工具；
- 記憶；
- 任務狀態機；
- 權限需求；
- 評測。

### 世界包

包含：

- 遊戲世界；
- 虛擬角色；
- 故事設定；
- 模擬規則；
- 地圖與事件狀態。

---

## 7.3 安裝流程

$$
\boxed{
\begin{aligned}
\mathcal P_i
&\xrightarrow{\mathsf{SignatureCheck}}
\mathcal P_i^1\\
&\xrightarrow{\mathsf{DependencyCheck}}
\mathcal P_i^2\\
&\xrightarrow{\mathsf{PermissionDiff}}
\mathcal P_i^3\\
&\xrightarrow{\mathsf{SandboxTest}}
\mathcal P_i^4\\
&\xrightarrow{\mathsf{Compatibility}}
\mathcal P_i^5\\
&\xrightarrow{\mathsf{UserPolicy}}
\begin{cases}
\mathsf{Reject},\\
\mathsf{Quarantine},\\
\mathsf{Trial},\\
\mathsf{Install}.
\end{cases}
\end{aligned}
}
$$

---

# 8. 個人主 AI 與可替換模型市場

## 8.1 能力供應商不應等於身份供應商

設模型供應商集合：

$$
\mathcal V
=
\left\{
v_1,v_2,\ldots,v_n
\right\}.
$$

本地主 AI 路由：

$$
\operatorname{Route}(q)
=
\operatorname{argmax}_{M_j}
\left[
Q(M_j,q)
-
C(M_j,q)
-
R(M_j,q)
-
D(M_j,q)
\right],
$$

其中：

- $Q$ ：品質；
- $C$ ：成本和延遲；
- $R$ ：風險；
- $D$ ：需要披露的資料量。

---

## 8.2 模型可替換性

若任務契約和記憶格式足夠獨立，則：

$$
M_j
\rightsquigarrow
M_k,
$$

而：

$$
\Delta S_{\mathrm{person}}
\approx 0.
$$

個人不應因更換模型而失去：

- 記憶；
- 關係；
- 目標；
- 專案狀態；
- 權限；
- 工作方法；
- 歷史。

---

## 8.3 防止供應商路由偏置

若模型路由由同一供應商控制，可能存在：

$$
\operatorname{RouteBias}
\left(
v_i
\right)
>0.
$$

本地控制層至少應能：

- 記錄選擇理由；
- 比較替代模型；
- 設定供應商上限；
- 禁止敏感任務上雲；
- 使用本地基準測試；
- 對模型退化自動降權。

---

# 9. 個體化不等於微調完整世界模型

## 9.1 傳統個人化

傳統方式：

$$
M_u
=
\operatorname{FineTune}
\left(
M_G,
D_u
\right).
$$

其問題包括：

- 計算成本；
- 遺忘；
- 難以解釋；
- 更新困難；
- 資料刪除困難；
- 個人資訊進入參數後難以定位；
- 不同裝置版本難以同步。

---

## 9.2 結構個人化

本文提出：

$$
\boxed{
\operatorname{Personalize}(u)
=
\mathcal M_u
+
\mathcal G_u
+
\mathcal P_u
+
\mathcal R_u
+
\Delta\theta_u^{\mathrm{selective}}.
}
$$

其中模型參數更新只是可選項。

主要個體化來自：

- 個人記憶；
- 個人因果圖；
- 個人方法；
- 個人權限；
- 個人模型偏好；
- 個人裝置與資料環境。

---

# 10. 本地主 AI 的六層架構

## 第零層：硬體與可信執行層

- 手機 SoC；
- NPU／GPU；
- 安全區域；
- 生物辨識；
- 加密儲存；
- 個人電腦；
- 家庭節點；
- 網路與電源狀態。

## 第一層：身份與政策層

- 使用者身份；
- 裝置身份；
- 憑證；
- 本地授權；
- 披露政策；
- 支付和簽署規則；
- 緊急撤銷。

## 第二層：記憶與因果層

- GCMS；
- 原始資料；
- 生成核；
- 認知原子；
- 關係圖；
- 專案圖；
- 候選／接受記憶；
- 版本與回滾。

## 第三層：本地主模型層

- 小型語言模型；
- 意圖判斷；
- 路由；
- 本地摘要；
- 記憶尋址；
- 簡單工具；
- 離線工作。

## 第四層：裝置與家庭 Agent 層

- 電腦 Agent；
- NAS Agent；
- 家庭設備 Agent；
- 工作站推理；
- 本地程式執行；
- 家庭共享服務。

## 第五層：雲端能力層

- 前沿模型；
- 搜尋；
- 專業 Agent；
- 模型市場；
- 大規模計算；
- 可替換 API。

---

# 11. 個人主 AI 的運行循環

$$
\boxed{
\begin{aligned}
q_t
&\xrightarrow{\mathsf{LocalInterpret}}
z_t\\
&\xrightarrow{\mathsf{RecallPersonalState}}
S_t^{q}\\
&\xrightarrow{\mathsf{LocalSolveCheck}}
\begin{cases}
\mathsf{LocalExecute},\\
\mathsf{HomeExecute},\\
\mathsf{RemoteDelegate}
\end{cases}\\
&\xrightarrow{\mathsf{DisclosureMinimize}}
B_t\\
&\xrightarrow{\mathsf{ModelRoute}}
M_j\\
&\xrightarrow{\mathsf{ResultReturn}}
y_t\\
&\xrightarrow{\mathsf{LocalVerify}}
\widetilde y_t\\
&\xrightarrow{\mathsf{CandidateWrite}}
\mathcal M_{\mathrm{candidate}}\\
&\xrightarrow{\mathsf{PolicyCommit}}
\mathcal M_{\mathrm{accepted}}^{t+1}.
\end{aligned}
}
$$

---

# 12. 十八項命題與猜想

## 命題 1：個人連續性與模型供應分離命題

個人主 AI 的長期狀態可以與任一特定雲端模型分離：

$$
\operatorname{Continuity}(S_u)
\perp
\operatorname{Provider}(M_j).
$$

---

## 命題 2：本地主權優於純雲端個人化命題

若本地端持有身份、記憶、政策和正式寫回權，則其模型可替換性與資料可控制性高於完全依附單一雲端平台的個人化。

---

## 命題 3：本地不等於純離線命題

本地個體化的必要條件是控制層本地化，而不是全部計算本地化：

$$
\text{Local Control}
\not\Rightarrow
\text{Local-only Compute}.
$$

---

## 命題 4：能力伸縮—狀態連續命題

理想系統可以在斷線與連線間改變能力，但保持身份和記憶連續：

$$
\Delta\mathcal C\neq 0,
\quad
\Delta S_{\mathrm{person}}\approx 0.
$$

---

## 命題 5：最小揭露增益猜想

若本地端能正確抽取任務所需資訊，則在維持任務效用的同時，可以顯著降低上雲資料量與再識別風險。

---

## 命題 6：正式寫回本地化命題

外部模型可以生成候選記憶，但正式個人記憶的接受權應留在本地政策層。

---

## 命題 7：個體化主要來自狀態而非完整微調命題

在大量日常任務中：

$$
U
\left(
\mathcal M_u+\mathcal G_u+\mathcal P_u
\right)
\geq
U
\left(
\Delta\theta_u
\right)
$$

可能成立；完整個人微調不是個體化的必要條件。

---

## 命題 8：記憶包可移植性命題

若記憶包具有開放格式、來源、版本和依賴描述，則它可以跨模型與跨裝置移植；否則它會形成新的供應商鎖定。

---

## 命題 9：能力包安全非同於應用程式安全命題

能力包同時包含知識、工作流和 Agent 行動，攻擊面大於普通內容包，需要更嚴格的沙箱、權限和候選寫回機制。

---

## 命題 10：本地模型不必是最強模型命題

本地模型只要能可靠完成：

- 個人狀態尋址；
- 任務理解；
- 隱私篩選；
- 路由；
- 基本驗證；
- 權限控制；

就可以把高難度推理交給外部模型。

---

## 命題 11：主控能力最低閾值命題

若本地模型低於主控閾值，它不能可靠判斷需要披露什麼或拒絕外部錯誤，此時本地主權只是名義上的。

---

## 命題 12：家庭節點中介命題

在手機資源不足、雲端披露風險過高時，家庭節點可以形成第三運算層，降低本地—雲端二元架構的張力。

---

## 命題 13：個人模型市場猜想

若模型介面、能力描述和記憶格式標準化，個人主 AI 可以依任務在多個模型供應商間動態選擇，形成使用者側模型市場。

---

## 命題 14：本地記憶不是無限累積命題

裝置記憶具有容量、能耗和安全限制，個人主 AI 必須具備：

$$
\mathsf{Keep},
\mathsf{Forget},
\mathsf{Archive},
\mathsf{Share},
\mathsf{Trust}.
$$

---

## 命題 15：供應商能力與代理權分離命題

模型提供者可提供高能力，但不應自動取得代表使用者作出付款、簽署、發送或公開發布的權限。

---

## 命題 16：跨裝置一致性困難命題

個人 AI 分布在手機、電腦和家庭節點後，必須處理衝突版本、離線更新和裝置失竊；分布式本地化不等於簡單同步。

---

## 命題 17：個人認知資產累積命題

隨時間增加，個人主 AI 的主要資產可能不是模型權重，而是：

$$
\mathcal A_u
=
\mathcal M_u
+
\mathcal G_u
+
\mathcal H_u
+
\mathcal P_u.
$$

---

## 命題 18：本地個體化主 AI 命題

若本地端具備可靠主控模型、版本化個人記憶、最小揭露治理、可替換模型路由、候選寫回與跨裝置恢復能力，則存在一類長期個人任務，使其在連續性、隱私、供應商可替換性與個體適應上優於純雲端單模型個人化。

---

# 13. 十五類失敗模式

## 13.1 手機遺失即身份失落

若缺乏加密備份與恢復機制，本地化會形成單點失效。

## 13.2 本地資料庫被入侵

本地不等於安全；裝置惡意程式可能直接取得長期記憶。

## 13.3 過度上雲

主 AI 為提高品質，將不必要的個人狀態送給雲端。

## 13.4 過度遮蔽

最小揭露失敗，導致外部模型缺乏必要資訊而完成錯誤任務。

## 13.5 本地主模型過弱

無法判斷敏感資訊、外部錯誤或權限風險。

## 13.6 記憶污染

外部模型生成內容被直接寫入正式個人記憶。

## 13.7 記憶膨脹

個人資料、下載包和 Agent 經驗無限制累積，超出裝置容量。

## 13.8 外掛供應鏈攻擊

惡意能力包要求過多權限或注入錯誤認知原子。

## 13.9 模型供應商鎖定

記憶和 Agent 包只相容單一模型介面。

## 13.10 跨裝置分裂

手機、電腦和家庭節點形成不同個人狀態。

## 13.11 過度個人化

系統只強化使用者既有偏好，降低外部觀點和反例。

## 13.12 代表權混淆

主 AI 在沒有明確授權時對外發送、購買或承諾。

## 13.13 家庭共享邊界錯誤

個人與家庭記憶混用，造成關係和隱私洩漏。

## 13.14 雲端斷供

核心能力長期依賴某家模型，停止服務後個人 AI 大幅退化。

## 13.15 本地生態壟斷

作業系統供應商控制本地模型、記憶介面與模型市場，新的控制中心由雲端平台轉移到裝置平台。

---

# 14. 九組可否證實驗

## 實驗 1：純雲端與本地主控

比較：

1. 純雲端模型加平台記憶；
2. 本地記憶加雲端模型；
3. 本地主模型加本地記憶和雲端路由；
4. 手機—家庭—雲端三層架構。

測量：

- 長期任務成功；
- 資料披露；
- 延遲；
- 供應商切換成本；
- 記憶連續。

---

## 實驗 2：模型更換

在不中斷個人狀態的前提下，替換主要雲端模型，測量：

$$
\Delta Q,
\quad
\Delta S_{\mathrm{person}},
\quad
C_{\mathrm{migration}}.
$$

---

## 實驗 3：最小揭露

建立需要不同程度個人資料的任務，比較：

- 全狀態上雲；
- 固定遮蔽；
- 任務範圍抽取；
- 本地抽象化；
- 人工最佳披露。

---

## 實驗 4：本地主模型尺寸

測試不同小模型是否能可靠完成：

- 敏感資料辨認；
- 任務路由；
- 外部答案拒錯；
- 記憶候選判斷；
- 權限控制。

---

## 實驗 5：記憶與能力包

測試：

- 開放格式包；
- 供應商專用包；
- 有簽章包；
- 惡意包；
- 過期包；
- 衝突包。

---

## 實驗 6：斷線韌性

模擬：

- 短期斷線；
- 長期斷線；
- 雲端供應商停機；
- 家庭節點失效；
- 手機更換。

---

## 實驗 7：跨裝置衝突

讓不同裝置離線修改同一記憶或政策，測量合併、回滾和人工介入成本。

---

## 實驗 8：記憶治理

比較：

- 全部保留；
- 固定時間刪除；
- 價值／風險／容量治理；
- 使用者手動治理；
- 混合治理。

---

## 實驗 9：過度個人化

建立需要反例、異議與新觀點的任務，測量個人主 AI 是否因歷史偏好而降低校正能力。

---

# 15. 評估指標

## 15.1 個人狀態可攜率

$$
P_{\mathrm{portable}}
=
\frac{
\text{可跨模型與裝置遷移的狀態}
}{
\text{全部個人狀態}
}.
$$

## 15.2 任務披露率

$$
D_{\mathrm{task}}
=
\frac{
\text{上雲個人資訊量}
}{
\text{完整可用個人資訊量}
}.
$$

## 15.3 必要披露精確率

$$
P_{\mathrm{necessary}}
=
\frac{
\text{真正為任務必要的披露資訊}
}{
\text{全部披露資訊}
}.
$$

## 15.4 斷線能力保留率

$$
R_{\mathrm{offline}}
=
\frac{
Q_{\mathrm{offline}}
}{
Q_{\mathrm{online}}
}.
$$

## 15.5 模型切換連續率

$$
C_{\mathrm{switch}}
=
1-
d
\left(
S_u^{\mathrm{before}},
S_u^{\mathrm{after}}
\right).
$$

## 15.6 正式寫回污染率

$$
P_{\mathrm{write}}
=
\frac{
\text{未驗證內容進入正式記憶}
}{
\text{全部正式寫回}
}.
$$

## 15.7 能力包可撤銷率

$$
R_{\mathrm{revoke}}
=
\frac{
\text{可完整移除並回復影響的能力包}
}{
\text{全部已安裝能力包}
}.
$$

## 15.8 本地主控準確率

$$
A_{\mathrm{control}}
=
f
\left(
A_{\mathrm{route}},
A_{\mathrm{privacy}},
A_{\mathrm{verify}},
A_{\mathrm{permission}}
\right).
$$

## 15.9 個人認知資產增長

$$
G_{\mathrm{asset}}
=
\frac{
|\mathcal A_u(t_2)|
-
|\mathcal A_u(t_1)|
}{
t_2-t_1
},
$$

但必須扣除：

- 重複；
- 污染；
- 過期；
- 不可追溯內容。

---

# 16. 與當前技術發展的關係

## 16.1 作業系統級端側模型

Apple 的 Foundation Models framework 已提供對裝置端模型的應用介面，並允許框架接入其他符合協定的語言模型；Apple 同時保留裝置端與 Private Cloud Compute 的能力分層。這顯示「本地模型加可替換遠端模型」正在從應用實驗走向作業系統級介面。

Android 的 Gemini Nano 經由 AICore 系統服務提供裝置端模型執行、模型管理與硬體加速；Google 亦提供面向文字、影像與音訊的端側生成式 API。

Microsoft Foundry Local 則提供在 Windows 裝置上下載並執行本地模型的運行環境，說明桌面作業系統正逐步把本地模型視為標準應用能力。

這些平台尚未等同本文的完整個人主 AI，但已提供其部分基礎：

- 本地模型；
- 系統級模型管理；
- 裝置硬體加速；
- 本地／雲端選擇；
- 多模型介面。

---

## 16.2 個人 AI 堆疊

OpenJarvis 將個人 AI 分解為 Intelligence、Engine、Agents、Tools & Memory、Learning 五種可編輯原語，並研究如何以雲端模型協助搜尋更好的本地規格，再使最終規格於裝置端運行。這支持本文的主張：個人 AI 不只是換上一個本地模型，而是一個可共同最佳化的完整堆疊。

---

## 16.3 邊雲個人記憶

MemPrivacy 研究讓本地端辨認敏感記憶片段、以具型別的占位結構交給雲端處理，再於本地恢復原始內容。此方向支持「個人記憶留在本地、必要語義有限上雲」的架構。

PrivScope 則直接把本地端設計成任務範圍披露治理器，要求只有為遠端子任務必要的資訊才能送往雲端，而且採用足以完成任務的最低細節表示。

---

## 16.4 端側持續記憶

端側 Agent 的記憶並非免費資源。相關研究指出，記憶會消耗 RAM、能量與傳輸，也會成為可寫入的攻擊面；因此需要按價值、成本、來源和風險決定保留、分享與信任。

這支持本文把忘記、隔離、來源與候選寫回視為個人主 AI 的核心功能，而非附加優化。

---

## 16.5 邊雲協同

邊雲協同研究普遍指出，純雲端具有隱私與通訊成本，純端側則受算力和記憶限制；讓本地小模型處理敏感、個人化和低延遲工作，再由雲端大模型承擔高難度推理，是一條實際發展路線。

本文在此基礎上增加了：

- 個人身份和狀態連續；
- 正式寫回本地化；
- 可替換模型市場；
- 記憶與能力包；
- 個人因果圖；
- 跨裝置恢復；
- 代表權治理。

---

# 17. 與前序理論的關係

## 17.1 結構生成式分布記憶

解決：

> 個人如何在不保存全部文字的條件下，維持大型知識群的可尋址與可重建性？

## 17.2 壓縮全局智能

解決：

> 主 AI 如何以後設能力調用子 Agent 和外部模型？

## 17.3 認知原子因果基底

解決：

> 主 AI 應常駐哪些底層知識，避免成為空殼路由器？

## 17.4 主 AI 雙路形成

解決：

> 主 AI 如何由通用模型重構，或由種子智能持續養成？

## 17.5 本地個體化主 AI

解決：

> 主 AI 最終由誰持有、在哪裡運行，以及如何成為每個人的長期個體智能？

---

# 18. 工程路線

## 階段一：個人記憶核心

- 本地資料庫；
- 版本化記憶；
- 來源；
- 候選／接受區；
- 匯出與回滾；
- 多模型查詢。

## 階段二：本地路由與披露治理

- 小型意圖模型；
- 敏感資料分類；
- 任務範圍上下文；
- 模型選擇；
- 本地／雲端決策；
- 審計。

## 階段三：跨裝置個人節點

- 手機；
- 電腦；
- NAS；
- 安全同步；
- 離線合併；
- 本地模型倉庫。

## 階段四：記憶與能力包

- 開放格式；
- 簽章；
- 權限聲明；
- 依賴；
- 沙箱；
- 市場與撤銷。

## 階段五：養成式個人主 AI

- 長期能力形成；
- 認知原子基底；
- 個人方法內化；
- 自主權分級；
- 模型替換；
- 形成史。

---

# 19. 理論邊界與否證條件

若未來實驗顯示：

1. 純雲端平台可以提供同等可攜、可刪除和可替換的個人狀態；
2. 本地主控模型無法在手機資源中可靠進行隱私、路由和驗證；
3. 最小揭露造成的任務損失長期高於隱私收益；
4. 跨裝置同步和本地安全成本不可接受；
5. 開放記憶與能力包無法抵抗供應鏈攻擊；
6. 使用者側模型路由無法優於平台路由；
7. 個人記憶長期累積只會增加偏見、污染和認知僵化；
8. 供應商模型替換必然導致不可恢復的能力和狀態損失；
9. 家庭節點和本地資料庫的維護成本使普通使用者無法採用；
10. 不存在任何長期任務使本地個體化架構優於純雲端個人化；

則本文命題應被限制在特定高隱私、長週期或專業場景，而不能作為一般個人 AI 架構。

---

# 20. 結論

本文所提出的個體化 AI 不是：

$$
\text{在手機裡塞進一個縮小版前沿大模型}.
$$

它是：

$$
\boxed{
\begin{aligned}
\mathcal A_u^{\mathrm{individual}}
={}&
A_u^{\mathrm{local\ main}}\\
&\oplus
\mathcal M_u^{\mathrm{personal}}\\
&\oplus
\mathcal G_u^{\mathrm{causal}}\\
&\oplus
\mathcal P_u^{\mathrm{authority}}\\
&\oplus
\mathcal D_u^{\mathrm{devices}}\\
&\oplus
\mathcal C^{\mathrm{cloud\ pool}}.
\end{aligned}
}
$$

本地端負責：

$$
\boxed{
\text{身份}
+
\text{記憶}
+
\text{權限}
+
\text{連續性}
+
\text{正式寫回}.
}
$$

雲端端負責：

$$
\boxed{
\text{高算力}
+
\text{最新能力}
+
\text{專業模型}
+
\text{可替換的認知服務}.
}
$$

因此，真正的本地個體化不是純離線，而是：

$$
\boxed{
\text{本地保持存在、主權與長期狀態，}
}
$$

$$
\boxed{
\text{連線時向外展開能力，斷線時仍保有自己。}
}
$$

通用大模型的發展與此架構並不衝突。前者提供文明級共享智能，後者提供個人級持續智能。沒有通用模型，個人主 AI 缺乏足夠的能力池；沒有本地主 AI，通用模型則可能永遠只是每次都很強、卻不真正屬於任何人的服務。

本文的最終命題是：

> **未來的個體化 AI，不應只是某家雲端模型對使用者的暫時記憶，而應是一個由個人持有身份、記憶、權限與形成歷史，並能自主選擇外部智能服務的本地主 AI。**

---

# 參考文獻

1. Apple Developer. (2026). *Foundation Models Framework*.
2. Apple Developer. (2026). *Adding Server-Side Intelligence with Private Cloud Compute*.
3. Apple Developer. (2026). *Bring an LLM Provider to the Foundation Models Framework*.
4. Android Developers. (2026). *Gemini Nano*.
5. Android Developers. (2026). *Find the Right AI/ML Solution for Your App*.
6. Microsoft Learn. (2026). *Use Local AI with Microsoft Foundry on Windows*.
7. Microsoft Learn. (2026). *Foundry Local Architecture Overview*.
8. Saad-Falcon, J., et al. (2026). *OpenJarvis: Personal AI, On Personal Devices*. arXiv:2605.17172.
9. Chen, Y., et al. (2026). *MemPrivacy: Privacy-Preserving Personalized Memory Management for Edge-Cloud Agents*. arXiv:2605.09530.
10. Seeam, S. R., et al. (2026). *PrivScope: Task-scoped Disclosure Control for Hybrid Agentic Systems*. arXiv:2605.16630.
11. Wu, B., et al. (2026). *Forget to Improve: On-Device LLM-Agent Continual Learning via Budget-Curated Memory*. arXiv:2606.25115.
12. Li, Z., Dutt, N., & Liu, C. (2026). *Orion: Enabling Self-adaptive Memory Management for On-device Online Continual Learning*. arXiv:2605.26473.
13. Xiong, Y., Hu, S., & Clune, J. (2026). *Learning to Continually Learn via Meta-learning Agentic Memory Designs*. arXiv:2602.07755.
14. Haque, M. A., et al. (2025). *Evaluation and Optimization of Small Language Models for Agentic Tasks on Edge Devices*. arXiv:2511.22138.
15. Belcak, P., et al. (2025). *Small Language Models are the Future of Agentic AI*. arXiv:2506.02153.
16. Niu, C., et al. (2025). *Collaborative Learning of On-Device Small Model and Cloud-Based Large Model: Advances and Future Directions*. arXiv:2504.15300.
17. Wang, F., et al. (2025). *A Survey on Collaborating Small and Large Language Models*. arXiv:2510.13890.
18. Zhan, J., et al. (2025). *PRISM: Privacy-Aware Routing for Adaptive Cloud-Edge Large Language Model Inference*. arXiv:2511.22788.
19. Li, Y., Li, C., & Liu, J. (2026). *Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models*. arXiv:2607.13093.
20. *Agent-X: Full Pipeline Acceleration of On-device AI Agents*. (2026). arXiv:2605.10380.
21. Neo.K & Aletheia. (2026). *無記憶術的記憶架構：結構編譯、生成核拓撲與外部智能協同*.
22. Neo.K & Aletheia. (2026). *壓縮全局智能命題*.
23. Neo.K & Aletheia. (2026). *認知原子因果基底命題*.
24. Neo.K & Aletheia. (2026). *主 AI 的雙路形成命題*.
25. Neo.K & Aletheia. (2026). *GCMS v1.0 與《可繼承的認知》系列*.

---

# 附錄 A：一句話命題

> **真正的個體化 AI，不是把最強模型縮進每一支手機，而是讓每個人擁有一個本地持續的身份、記憶與權限核心，再由它按需調用全世界可替換的模型能力。**
