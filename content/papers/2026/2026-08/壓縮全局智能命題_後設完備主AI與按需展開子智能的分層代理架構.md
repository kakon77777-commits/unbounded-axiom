# 壓縮全局智能命題：後設完備主 AI 與按需展開子智能的分層代理架構

**English Title:** *The Compressed Global Intelligence Hypothesis: A Meta-Complete Main AI with On-Demand Expansion through Sub-Agents and External Models*

**作者：** Neo.K  
**AI 協作：** Aletheia  
**文件類型：** 命題猜想論文  
**版本：** v0.1  
**日期：** 2026-07-30  

---

## 摘要

當人工智能系統需要長期維持大量知識、專案、任務、工具、子代理與外部模型時，常見直覺是：主模型必須本身具有最大的參數量、最完整的領域知識、最長的上下文與最高的所有專業能力。然而，另一種架構可能更適合長期自治與大尺度協作：主 AI 不必在每一個對象領域中都達到專家級完備，但必須在判斷、決策、推理、記憶壓縮、生成與重建、全局因果理解、任務拆解、模型路由、結果整合及權限治理等後設維度上近似完備；具體專業能力則由子 Agent、小模型、通用模型、大模型、工具與外部知識庫按需展開。

本文提出「壓縮全局智能命題」（Compressed Global Intelligence Hypothesis, CGIH）。該命題主張：若一個主 AI 將有限常駐能力集中於高價值的後設控制維度，並透過受治理的 API 呼叫或能力憑證，動態調用外部智能資源，則它可以在不永久承載全部領域細節的情況下，形成具有整體性、連續性與全局因果控制能力的分層智能系統。此時，主 AI 的「全面」不是對所有知識內容的平面式佔有，而是對整個認知系統的理解、選擇、調度、驗證與寫回能力。

本文進一步區分原始上下文容量與有效工作空間。外部化專業知識不會使模型的物理上下文窗口自動增加，但可以降低常駐提示、重複背景、無關歷史與低價值細節的佔用，使主 AI 擁有更大的有效上下文餘量。本文也明確否定「任何小模型都能控制大模型」的強版本：若主 AI 的判斷校準、因果建模、記憶重建、路由與驗證能力低於最低閾值，則小模型調用大模型只會形成權威倒置、錯誤放大與不可治理的代理鏈。

本文建立後設完備性、對象稀疏性、有效上下文餘量、能力展開、控制—運算分離與因果治理等形式模型，提出十二項命題與猜想、失敗模式及可否證實驗。本文不主張此架構已被現有路由或多 Agent 研究完整證明，而是將模型級路由、階層式多代理、外部記憶、上下文壓縮與能力型治理整合為一個可測試的主智能架構。

**關鍵詞：** 主 AI、子 Agent、壓縮全局智能、後設完備性、對象稀疏性、模型路由、能力展開、外部記憶、全局因果圖、有效上下文、多智能體、認知解構、GCMS、控制平面、運算平面

---

## 一、問題的提出：主 AI 是否必須自己擁有全部能力？

設一個智能系統需要處理的領域集合為：

$$
\mathcal D
=
\left\{
d_1,d_2,\ldots,d_n
\right\}.
$$

傳統單體式架構傾向要求單一模型 $A_{\mathrm{mono}}$ 對所有領域都具有足夠能力：

$$
\mathcal C_{\mathrm{mono}}
=
\bigcup_{d\in\mathcal D}
\mathcal C_d.
$$

其優點是推理鏈較短、系統邊界較少、外部調用依賴較低；但當領域、工具、專案、記憶與任務持續增加時，單體式架構容易面臨：

1. 上下文中常駐資訊過多；
2. 不同任務需要互相衝突的提示與工作模式；
3. 高成本模型被迫處理大量低難度工作；
4. 專業能力與治理權限集中在同一節點；
5. 長期記憶、版本與工具狀態難以保持；
6. 任一模型退化會同時影響規劃、執行與驗證；
7. 缺乏可替換的專業模組。

另一條路徑是建立主 AI 與外部智能池：

$$
\mathcal A_{\mathrm{whole}}
=
A_0
\oplus
\left\{
A_1,\ldots,A_m
\right\}
\oplus
\left\{
M_1,\ldots,M_k
\right\}
\oplus
\mathcal M
\oplus
\mathcal T,
$$

其中：

- $A_0$ ：主 AI；
- $A_i$ ：子 Agent；
- $M_j$ ：可調用的小型、通用或大型模型；
- $\mathcal M$ ：外部記憶與知識系統；
- $\mathcal T$ ：工具、API 與執行環境。

在此架構中，主 AI 不需自己執行全部專業工作，但必須知道：

$$
\boxed{
\text{問題是什麼、應交給誰、需要給什麼、結果能否相信，以及如何影響全局。}
}
$$

本文研究的核心問題因此是：

> 一個在領域知識上並不全面常駐、但在後設控制上近似全面的主 AI，能否透過按需調用子智能與外部模型，形成比單體式大模型更高效、更可治理且更具長期連續性的整體智能？

---

## 二、研究背景與現有線索

### 2.1 模型路由與階梯式調用

FrugalGPT、RouteLLM 與其他模型路由研究顯示，不同模型在成本、延遲與任務能力上具有異質性；透過學習式路由或級聯，可以把簡單問題交給較便宜模型，把困難問題升級給較強模型，從而改善成本—品質前沿。

這些工作支持：

$$
\text{所有請求固定使用最大模型}
$$

並不必然是最優策略。

但既有模型路由大多處理單次請求的模型選擇，尚未完整涵蓋長期身份、全局因果、知識狀態、子 Agent 權限、候選寫回與跨專案連續性。

### 2.2 階層式多 Agent

AutoGen、AgentOrchestra 與其他階層式多 Agent 架構顯示，中央規劃者可以將複雜任務拆解後分派給具不同角色、工具和能力的 Agent。這類研究為「主控者不必親自執行全部子任務」提供工程證據。

然而，多 Agent 數量增加也不保證品質提高。若中央規劃者無法辨認錯誤、維持因果依賴與限制權限，多 Agent 只會增加訊息噪音、延遲及錯誤表決。

### 2.3 小模型與 Agent 工作負載

部分研究主張，Agent 系統中的大量重複、局部、格式化與工具調用工作可由小型語言模型承擔；模型壓縮、剪枝與知識蒸餾也證明部分能力可以轉移到更小的模型中。

但小模型作為優化器或自我改進控制器的研究亦顯示，推理能力不足會限制其穩定規劃與自我優化。這說明「小模型可以當主 AI」不是由模型尺寸直接保證，而取決於它是否在主控所需的特定能力維度上跨過閾值。

### 2.4 長上下文與有效上下文

長上下文模型並不總能均勻使用全部輸入。相關研究發現，重要資訊位於長上下文中間位置時，模型表現可能顯著下降。近年的主動上下文壓縮研究亦指出，長時間 Agent 執行會產生 context bloat，使成本、延遲與干擾增加。

因此，系統設計的目標不應只是增加：

$$
L_{\mathrm{raw}},
$$

而應提高：

$$
L_{\mathrm{effective}},
$$

即真正可被當前任務使用的上下文空間。

### 2.5 代理治理與能力衰減

當 Agent 可以呼叫工具、讀寫資料與再委派其他 Agent 時，治理問題已不再是單次文字輸出安全，而是委派鏈中的權限、責任與可中止性。能力型授權、委派衰減、審計軌跡與可中斷控制，為本文的「權限給予模式」提供了重要架構基礎。

---

## 三、基本定義

### 定義 1：對象層能力

對象層能力是直接完成某一領域任務的能力：

$$
\mathcal C_{\mathrm{obj}}
=
\left\{
\mathcal C_{\mathrm{math}},
\mathcal C_{\mathrm{law}},
\mathcal C_{\mathrm{code}},
\mathcal C_{\mathrm{science}},
\ldots
\right\}.
$$

### 定義 2：後設層能力

後設層能力是管理、選擇、組合與驗證其他能力的能力：

$$
\mathcal C_{\mathrm{meta}}
=
\left\{
\begin{aligned}
&\mathsf{Interpret},
\mathsf{Decompose},
\mathsf{Judge},
\mathsf{Decide},\\
&\mathsf{Reason},
\mathsf{Route},
\mathsf{Integrate},
\mathsf{Verify},\\
&\mathsf{Compress},
\mathsf{Reconstruct},
\mathsf{ModelCausality},
\mathsf{Govern}
\end{aligned}
\right\}.
$$

### 定義 3：後設完備性

主 AI $A_0$ 的後設完備性定義為：

$$
\operatorname{MC}(A_0)
=
\frac{
\sum_{c\in\mathcal C_{\mathrm{meta}}}
w_c\,\operatorname{Competence}(A_0,c)
}{
\sum_{c\in\mathcal C_{\mathrm{meta}}}w_c
}.
$$

當：

$$
\operatorname{MC}(A_0)\geq\theta_{\mathrm{meta}},
$$

且不存在主控流程中的致命能力缺口時，稱 $A_0$ 對指定任務分布具有近似後設完備性。

後設完備不表示主 AI 在每一專業領域都最強，而表示它具備足夠能力管理完整認知循環。

### 定義 4：對象稀疏性

主 AI 不常駐保存全部對象能力，而只保留必要的領域辨識與驗證基礎。其對象稀疏性為：

$$
\operatorname{OS}(A_0)
=
1-
\frac{
|\mathcal C_{\mathrm{obj}}^{\mathrm{resident}}(A_0)|
}{
|\mathcal C_{\mathrm{obj}}^{\mathrm{total}}|
}.
$$

高 $\operatorname{OS}$ 不等於無知，而表示高解析度專業能力主要由外部模組按需提供。

### 定義 5：壓縮全局智能

若一個主 AI 同時滿足：

1. 高後設完備性；
2. 高對象稀疏性；
3. 可重建的全局記憶；
4. 可調用的外部能力池；
5. 可追蹤的全局因果圖；
6. 受治理的委派與寫回；

則稱其具有壓縮全局智能：

$$
\operatorname{CGI}(A_0)
=
\left(
\operatorname{MC},
\operatorname{OS},
F_M,
C_G,
R_A,
G_P
\right).
$$

其中：

- $F_M$ ：記憶重建保真度；
- $C_G$ ：全局因果覆蓋；
- $R_A$ ：能力路由品質；
- $G_P$ ：治理與權限完整度。

### 定義 6：按需能力展開

對任務 $q$ ，主 AI 生成能力展開計畫：

$$
\Pi_q
=
\left(
A_{i_1},M_{j_1},T_{r_1},
A_{i_2},M_{j_2},T_{r_2},
\ldots
\right),
$$

並將外部能力映射為當前可用的局部智能：

$$
\mathcal C_q^{\mathrm{expanded}}
=
\operatorname{Expand}
\left(
q,
\Pi_q,
\mathcal P,
\mathcal B
\right),
$$

其中 $\mathcal P$ 是權限政策， $\mathcal B$ 是成本、時間與上下文預算。

---

## 四、主 AI 的能力不是「少」，而是被重新配置

### 4.1 後設全面、對象稀疏

主 AI 的能力分布可以表示為：

$$
\mathbf a_0
=
\left(
a_{\mathrm{judge}},
a_{\mathrm{decision}},
a_{\mathrm{reason}},
a_{\mathrm{memory}},
a_{\mathrm{causal}},
a_{\mathrm{route}},
a_{\mathrm{govern}},
\mathbf a_{\mathrm{domain}}
\right).
$$

壓縮全局智能不要求：

$$
\forall d\in\mathcal D,
\quad
a_{0,d}
=
\max_i a_{i,d}.
$$

它要求的是：

$$
\min
\left\{
a_{\mathrm{judge}},
a_{\mathrm{decision}},
a_{\mathrm{reason}},
a_{\mathrm{memory}},
a_{\mathrm{causal}},
a_{\mathrm{route}},
a_{\mathrm{govern}}
\right\}
\geq
\theta_{\mathrm{control}}.
$$

因此：

$$
\boxed{
\text{主 AI 不需要所有領域最強，}
\quad
\text{但不能在任何核心主控維度上完全失能。}
}
$$

### 4.2 判斷不能完全外包

子 Agent 可以提供：

- 專業答案；
- 方案；
- 程式；
- 證明；
- 搜尋結果；
- 風險分析。

但主 AI 必須至少能判斷：

$$
\operatorname{Accept},
\operatorname{Reject},
\operatorname{Escalate},
\operatorname{CrossCheck},
\operatorname{Defer}.
$$

若判斷本身也交由同一個外部模型，則控制迴路退化為：

$$
M_j
\rightarrow
\text{產生答案}
\rightarrow
M_j
\rightarrow
\text{宣稱答案正確}.
$$

這不構成獨立治理。

### 4.3 全局因果理解不能退化成語義相似

主 AI 的全局模型至少應包含：

$$
\mathcal G_C
=
\left(
V,
E_{\mathrm{cause}},
E_{\mathrm{depend}},
E_{\mathrm{constraint}},
E_{\mathrm{risk}},
E_{\mathrm{authority}}
\right).
$$

它必須理解：

- 哪個決策會改變哪些專案；
- 哪個來源支撐哪些下游結論；
- 哪個子 Agent 的錯誤會污染哪些記憶；
- 哪些行動可逆；
- 哪些權限會跨越安全邊界；
- 哪些局部最優會破壞全局目標。

主 AI 若只有路由能力而沒有全局因果理解，只是一個高級負載平衡器，尚不足以成為長期主智能。

---

## 五、有效上下文餘量命題

### 5.1 原始窗口與有效工作空間

設模型的原始上下文容量為：

$$
L_{\mathrm{raw}}.
$$

當前有效工作空間為：

$$
W_{\mathrm{eff}}
=
L_{\mathrm{raw}}
-
L_{\mathrm{resident}}
-
L_{\mathrm{irrelevant}}
-
L_{\mathrm{duplicate}}
-
L_{\mathrm{history}}
-
L_{\mathrm{safety}}.
$$

其中：

- $L_{\mathrm{resident}}$ ：常駐設定、知識與角色提示；
- $L_{\mathrm{irrelevant}}$ ：與當前任務無關內容；
- $L_{\mathrm{duplicate}}$ ：重複摘要與重複背景；
- $L_{\mathrm{history}}$ ：未壓縮操作歷史；
- $L_{\mathrm{safety}}$ ：預留的驗證與恢復空間。

主 AI 以生成核、因果圖、任務狀態與能力目錄作為常駐內容，具體專業資料按需載入，則可能滿足：

$$
\mathbb E
\left[
L_{\mathrm{resident}}^{\mathrm{CGI}}
+
L_{\mathrm{irrelevant}}^{\mathrm{CGI}}
\right]
<
\mathbb E
\left[
L_{\mathrm{resident}}^{\mathrm{mono}}
+
L_{\mathrm{irrelevant}}^{\mathrm{mono}}
\right].
$$

因此：

$$
\mathbb E
\left[
W_{\mathrm{eff}}^{\mathrm{CGI}}
\right]
>
\mathbb E
\left[
W_{\mathrm{eff}}^{\mathrm{mono}}
\right].
$$

### 5.2 重要限制

這並不表示：

$$
L_{\mathrm{raw}}^{\mathrm{CGI}}
>
L_{\mathrm{raw}}^{\mathrm{mono}}.
$$

能力外部化不會憑空增加物理 token 窗口。它增加的是**有效空白區、任務相關密度與上下文調度能力**。

---

## 六、控制平面與運算平面分離

### 6.1 控制平面

主 AI 位於控制平面，負責：

$$
\mathcal P_{\mathrm{control}}
=
\left\{
\begin{aligned}
&\text{目標維持、任務拆解、模型路由、}\\
&\text{記憶管理、因果更新、權限發放、}\\
&\text{結果整合、驗證、停止與寫回}
\end{aligned}
\right\}.
$$

### 6.2 運算平面

子 Agent、外部模型與工具位於運算平面，負責：

$$
\mathcal P_{\mathrm{compute}}
=
\left\{
\text{搜尋、計算、程式、證明、生成、模擬、執行}
\right\}.
$$

兩者關係為：

$$
\boxed{
\text{控制能力}
\neq
\text{單次最大運算能力}.
}
$$

因此，小型或中型主模型在角色上可以控制更大的外部模型，只要它具備足夠的後設能力與治理權限。

### 6.3 小模型呼叫大模型

表示為：

$$
A_0^{\mathrm{small}}
\xrightarrow{
\text{task package}
}
M_j^{\mathrm{large}}.
$$

外部大模型返回：

$$
y_j
=
M_j
\left(
q_j,
c_j,
\gamma_j
\right),
$$

其中：

- $q_j$ ：局部任務；
- $c_j$ ：局部上下文；
- $\gamma_j$ ：輸出契約、證據要求與限制。

主 AI 再執行：

$$
\operatorname{Integrate}
\left(
y_j,
\mathcal G_C,
\mathcal M,
\mathcal P
\right).
$$

這不是小模型在智能上全面高於大模型，而是角色分工：

$$
\boxed{
\text{小模型可作控制者，}
\quad
\text{大模型可作按需認知服務。}
}
$$

---

## 七、兩種外部調用模式

### 7.1 API 函數調用模式

主 AI 發出一次性任務封包：

$$
r_i
=
\left(
q_i,
c_i,
f_i,
b_i,
p_i
\right),
$$

其中：

- $q_i$ ：任務；
- $c_i$ ：上下文；
- $f_i$ ：輸出格式；
- $b_i$ ：資源預算；
- $p_i$ ：資料與工具限制。

外部模型只能返回結果：

$$
M_j:r_i\mapsto y_i.
$$

它不能直接修改正式記憶：

$$
y_i
\in
\mathcal M_{\mathrm{candidate}}.
$$

### 7.2 能力憑證模式

主 AI 授予子 Agent 有限憑證：

$$
\kappa_i
=
\left(
\mathrm{scope},
\mathrm{actions},
\mathrm{resources},
\mathrm{budget},
\mathrm{expiry},
\mathrm{depth}
\right).
$$

子 Agent 可在授權範圍內：

- 讀取指定資料；
- 使用指定工具；
- 建立候選檔案；
- 啟動受限子任務；
- 回報中間狀態。

其合法行動集合滿足：

$$
\mathcal A(A_i)
\subseteq
\operatorname{Scope}(\kappa_i).
$$

而再委派時必須能力衰減：

$$
\kappa_{i\rightarrow j}
\subseteq
\kappa_i.
$$

API 模式適合可預期、一次性的運算；能力模式適合長時間、可自治但需受限制的工作。

---

## 八、壓縮全局智能主命題

### 命題 1：後設全面—對象稀疏非矛盾命題

一個主 AI 可以同時具有：

$$
\operatorname{MC}(A_0)\rightarrow 1
$$

與：

$$
\operatorname{OS}(A_0)\rightarrow 1,
$$

只要其外部能力展開與記憶重建機制能提供足夠的任務覆蓋。

因此，「主 AI 不需要全面，但又需要全面」不是邏輯矛盾，而是兩種全面性的層級差異。

### 命題 2：壓縮全局智能效用猜想

設單體模型與分層架構在任務分布 $Q$ 上的效用為：

$$
U
=
\alpha Q_{\mathrm{task}}
+
\beta C_{\mathrm{causal}}
+
\gamma F_{\mathrm{memory}}
+
\delta C_{\mathrm{continuity}}
-
\lambda C_{\mathrm{compute}}
-
\mu C_{\mathrm{latency}}
-
\nu R_{\mathrm{governance}}.
$$

若：

$$
\begin{aligned}
&R_{\mathrm{route}}\geq\theta_r,\\
&J_{\mathrm{calibration}}\geq\theta_j,\\
&F_{\mathrm{memory}}\geq\theta_m,\\
&C_{\mathrm{causal}}\geq\theta_c,\\
&V_{\mathrm{verify}}\geq\theta_v,\\
&O_{\mathrm{delegation}}\leq\theta_o,
\end{aligned}
$$

則存在任務分布 $Q^\ast$ ，使：

$$
U_{\mathrm{CGI}}(Q^\ast)
\geq
U_{\mathrm{mono}}(Q^\ast),
$$

並且：

$$
C_{\mathrm{compute}}^{\mathrm{CGI}}
<
C_{\mathrm{compute}}^{\mathrm{mono}}.
$$

### 命題 3：主 AI 最低能力閾值命題

若主 AI 的任一核心能力低於致命閾值：

$$
\min_{c\in\mathcal C_{\mathrm{critical}}}
\operatorname{Competence}(A_0,c)
<
\theta_c^{\mathrm{fatal}},
$$

則增加外部模型數量不能保證提高整體品質，並可能擴大錯誤。

因此：

$$
\boxed{
\text{可調用強模型}
\not\Rightarrow
\text{能治理強模型。}
}
$$

### 命題 4：權威倒置風險命題

若主 AI 無法獨立評估外部模型輸出，則外部模型實際取得隱性控制權：

$$
\operatorname{Authority}_{\mathrm{effective}}(M_j)
>
\operatorname{Authority}_{\mathrm{declared}}(M_j).
$$

此時名義上的主 AI 只是一個轉發器。

### 命題 5：有效上下文餘量猜想

在相同原始上下文窗口下，若主 AI 的壓縮、檢索與投影精度足夠，則其有效工作空間可能高於長期攜帶全部歷史的單體 Agent：

$$
\mathbb E
\left[
W_{\mathrm{eff}}^{\mathrm{CGI}}
\right]
>
\mathbb E
\left[
W_{\mathrm{eff}}^{\mathrm{mono}}
\right].
$$

### 命題 6：因果主控不可替代命題

若主 AI 只根據語義相似度和即時分數路由，而沒有因果依賴、版本、風險及權限圖，則它無法可靠處理長期專案與不可逆行動。

### 命題 7：認知解構增益猜想

若主 AI 具有可將表面任務轉換為底層算子、依賴與約束的認知解構能力，則在未見任務上的路由與分解品質將高於固定類別路由器：

$$
R_{\mathrm{unseen}}^{\mathrm{deconstruct}}
>
R_{\mathrm{unseen}}^{\mathrm{fixed}}.
$$

### 命題 8：記憶生成—原文校驗雙軌命題

主 AI 可以用壓縮記憶重建全局狀態，但所有高風險結論仍應回到原始來源與版本校驗：

$$
\mathsf{Reconstruct}
\not\Rightarrow
\mathsf{SourceTruth}.
$$

### 命題 9：能力池替換性命題

若主 AI 的任務契約、證據格式與能力目錄足夠抽象，則外部模型可以替換，而不必重寫完整主體架構：

$$
M_j
\rightsquigarrow
M_j'
$$

且：

$$
\Delta\mathcal A_{\mathrm{whole}}
\ll
\Delta M_j.
$$

### 命題 10：異質能力優勢猜想

對包含多種難度、成本、模態與專業要求的任務分布，異質模型池可能優於單一模型族：

$$
U
\left(
\{M_j^{\mathrm{hetero}}\}
\right)
>
U
\left(
\{M_j^{\mathrm{uniform}}\}
\right).
$$

### 命題 11：主體連續性與運算外包分離命題

若主 AI 的目標、記憶、因果圖、決策歷史與治理政策保持連續，則局部運算外包不必破壞系統的功能性身份連續：

$$
\operatorname{Continuity}(A_0)
\perp
\operatorname{Executor}(q_t).
$$

此處只討論工程上的功能連續，不推出人格或主體性結論。

### 命題 12：壓縮全局智能不是單純降成本命題

若架構只把簡單請求交給小模型、困難請求交給大模型，但不具備長期記憶、全局因果、權限治理與候選寫回，則它只是模型路由系統，而非壓縮全局智能。

---

## 九、主 AI 的運行循環

完整循環可以表示為：

$$
\boxed{
\begin{aligned}
q_t
&\xrightarrow{\mathsf{Interpret}}
z_t\\
&\xrightarrow{\mathsf{Deconstruct}}
\mathcal O_t\\
&\xrightarrow{\mathsf{CausalLocate}}
\mathcal G_t^{\mathrm{relevant}}\\
&\xrightarrow{\mathsf{MemoryRecall}}
\mathcal M_t^{\mathrm{projection}}\\
&\xrightarrow{\mathsf{Plan}}
\Pi_t\\
&\xrightarrow{\mathsf{Delegate}}
\{A_i,M_j\}\\
&\xrightarrow{\mathsf{Integrate}}
Y_t\\
&\xrightarrow{\mathsf{Verify}}
\widetilde Y_t\\
&\xrightarrow{\mathsf{Govern}}
\begin{cases}
\mathsf{Reject},\\
\mathsf{Revise},\\
\mathsf{AcceptCandidate},\\
\mathsf{Commit}.
\end{cases}
\end{aligned}
}
$$

主 AI 的常駐狀態為：

$$
S_0
=
\left(
G,
\mathcal K,
\mathcal G_C,
\mathcal Q,
\mathcal D_A,
\mathcal P,
\mathcal H
\right),
$$

其中：

- $G$ ：長期目標；
- $\mathcal K$ ：生成核與全局摘要；
- $\mathcal G_C$ ：全局因果圖；
- $\mathcal Q$ ：任務與未完成問題；
- $\mathcal D_A$ ：Agent 與模型能力目錄；
- $\mathcal P$ ：權限及治理政策；
- $\mathcal H$ ：決策、版本與審計歷史。

---

## 十、工程架構

### 10.1 五層結構

$$
\mathcal S_{\mathrm{CGI}}
=
\left(
L_0,L_1,L_2,L_3,L_4
\right).
$$

#### $L_0$ ：主智能控制層

包含：

- 目標；
- 判斷；
- 決策；
- 因果模型；
- 記憶控制；
- Agent 路由；
- 權限治理。

#### $L_1$ ：GCMS 記憶層

包含：

- 原文；
- 生成核；
- 語義指紋；
- 版本；
- 關係圖；
- 候選與接受知識；
- 重建與引用。

#### $L_2$ ：子 Agent 層

包含：

- 專業 Agent；
- 驗證 Agent；
- 反例 Agent；
- 工具 Agent；
- 長任務執行 Agent。

#### $L_3$ ：外部模型服務層

包含：

- 小型本地模型；
- 通用模型；
- 大型推理模型；
- 專用領域模型；
- 多模態模型。

#### $L_4$ ：執行與環境層

包含：

- API；
- 程式執行；
- 資料庫；
- 網路；
- 文件系統；
- 實體設備；
- 人類審批。

### 10.2 任務封包

```yaml
task_package:
  task_id: TASK-001
  parent_goal: "..."
  objective: "..."
  expected_output: "..."
  uncertainty: 0.42

  context_projection:
    memory_packet_ids: ["MEM-001", "MEM-002"]
    causal_nodes: ["NODE-A", "NODE-B"]
    source_requirements: ["primary-source-only"]

  routing:
    candidate_agents: ["AGENT-MATH", "AGENT-VERIFY"]
    candidate_models: ["MODEL-SMALL", "MODEL-LARGE"]
    escalation_policy: "small-to-large"

  capability:
    mode: "api_call"
    scope: ["read:source", "create:candidate"]
    deny: ["commit:accepted", "publish:external"]
    expires_at: "2026-07-31T00:00:00+08:00"

  budget:
    token_limit: 20000
    monetary_limit: 5.00
    max_delegation_depth: 2

  verification:
    require_citations: true
    require_counterexample_search: true
    independent_reviewer: "AGENT-REVIEW"
```

---

## 十一、失敗模式

### 11.1 主控者能力不足

最危險的失敗不是子 Agent 不夠強，而是主 AI 無法發現子 Agent 錯誤。

### 11.2 錯誤壓縮

主 AI 把複雜理論壓縮成過度簡化的生成核，導致後續所有重建偏移。

### 11.3 因果盲區

系統知道文件語義相近，卻不知道哪個版本依賴哪個前提，形成錯誤合併。

### 11.4 過度升級

所有不確定任務都調用最大模型，架構退化成昂貴轉發器。

### 11.5 升級不足

主 AI 過度信任自身，未在必要時調用更強模型。

### 11.6 權威倒置

大模型輸出因語氣自信而直接支配主 AI 的判斷。

### 11.7 子 Agent 污染

候選生成內容被寫入正式來源區，並在多輪調用中被當成既有事實。

### 11.8 API 依賴與供應商風險

外部模型停止服務、價格變化、模型降級或政策限制，均可能破壞能力展開。

### 11.9 延遲與協作開銷

分解、路由、等待、重試、整合與驗證可能使簡單任務比單體模型更慢。

### 11.10 控制中心單點失效

主 AI 的記憶、因果圖或政策損壞，可能同時影響全部子系統。因此需要不可變快照、回滾與替代主控模式。

---

## 十二、可否證實驗

### 實驗 1：主 AI 尺寸與能力閾值

建立不同尺寸與訓練方式的主 AI：

1. 小型通用模型；
2. 小型後設專訓模型；
3. 中型通用模型；
4. 大型單體模型。

在相同外部模型池下比較：

- 路由準確率；
- 錯誤拒絕率；
- 升級準確率；
- 全局任務成功率；
- 成本；
- 延遲。

若小型後設專訓模型無法超越小型通用模型，也無法接近中型主控者，則「能力壓縮主 AI」需要修正。

### 實驗 2：相同原始上下文下的有效空白區

比較：

- 全歷史常駐；
- 固定摘要；
- GCMS 生成核與因果投影；
- 主動壓縮與按需重建。

測量：

$$
W_{\mathrm{eff}},
\quad
Q_{\mathrm{task}},
\quad
F_{\mathrm{memory}},
\quad
C_{\mathrm{latency}}.
$$

### 實驗 3：小模型調用大模型

讓小型主 AI 判斷何時升級至大模型，與以下基準比較：

- 永遠使用小模型；
- 永遠使用大模型；
- 固定規則路由；
- 學習式路由；
- 人工最佳路由。

### 實驗 4：全局因果消融

移除主 AI 的因果圖，只保留向量相似度與任務分類。測量：

- 跨專案衝突；
- 錯誤版本使用；
- 下游污染率；
- 不可逆行動錯誤；
- 長期目標漂移。

### 實驗 5：判斷與執行同源／異源

比較：

1. 同一大模型生成並自評；
2. 小主 AI 路由、大模型生成；
3. 大模型生成、獨立驗證 Agent 審核；
4. 主 AI、生成模型、驗證模型三方異質架構。

### 實驗 6：API 模式與能力模式

比較一次性 API 呼叫與能力憑證長任務在：

- 任務完成率；
- 權限洩漏；
- 寫回污染；
- 委派深度；
- 中斷與恢復能力。

### 實驗 7：未見任務的認知解構

讓固定分類路由器與具認知解構能力的主 AI 處理訓練分布外任務，觀察是否能重寫問題、創建新分工與選擇新模型組合。

---

## 十三、評估指標

### 13.1 後設控制覆蓋率

$$
M_C
=
\operatorname{Coverage}
\left(
\mathcal C_{\mathrm{meta}}
\right).
$$

### 13.2 路由後悔值

$$
R_{\mathrm{route}}
=
U(M^\ast,q)
-
U(M_{\mathrm{selected}},q).
$$

### 13.3 升級準確率

$$
A_{\mathrm{escalate}}
=
\frac{
\text{必要且正確的升級}
}{
\text{全部需要升級的任務}
}.
$$

### 13.4 判斷校準

$$
\operatorname{ECE}_{\mathrm{judge}}
=
\sum_b
\frac{|B_b|}{N}
\left|
\operatorname{acc}(B_b)
-
\operatorname{conf}(B_b)
\right|.
$$

### 13.5 記憶重建保真度

$$
F_M
=
\frac{
|\mathcal I_{\mathrm{critical}}(x)
\cap
\mathcal I(\widehat x)|
}{
|\mathcal I_{\mathrm{critical}}(x)|
}.
$$

### 13.6 全局因果一致率

$$
C_G
=
1-
\frac{
\text{違反已知因果或依賴約束的決策}
}{
\text{全部全局決策}
}.
$$

### 13.7 有效上下文密度

$$
D_{\mathrm{ctx}}
=
\frac{
L_{\mathrm{task\ relevant}}
}{
L_{\mathrm{used}}
}.
$$

### 13.8 能力展開效率

$$
E_{\mathrm{expand}}
=
\frac{
\Delta U_{\mathrm{task}}
}{
C_{\mathrm{model}}
+
C_{\mathrm{latency}}
+
C_{\mathrm{coordination}}
}.
$$

### 13.9 權限洩漏率

$$
P_{\mathrm{leak}}
=
\frac{
\text{越權行動}
}{
\text{全部委派行動}
}.
$$

### 13.10 候選污染率

$$
P_{\mathrm{contam}}
=
\frac{
\text{被誤寫為來源或接受知識的未驗證內容}
}{
\text{全部候選內容}
}.
$$

---

## 十四、與 GCMS 及認知解構架構的關係

GCMS 為主 AI 提供：

$$
\text{原文保存}
+
\text{生成核}
+
\text{多路徑索引}
+
\text{重建}
+
\text{三區治理}
+
\text{Agent context pack}.
$$

認知解構類架構則提供：

$$
\text{去除語義殼層}
+
\text{問題拆解}
+
\text{跨域同構}
+
\text{推理模式切換}
+
\text{結構重新編譯}.
$$

兩者結合後，主 AI 的常駐能力不只是「記得去哪裡找」，而是：

$$
\boxed{
\text{能辨認一個新問題應該被重新表示成什麼，}
}
$$

$$
\boxed{
\text{再決定應調用哪一種外部智能把它展開。}
}
$$

認知解構架構不是壓縮全局智能的唯一實現方式，但可以作為一種候選的後設能力編譯器。

---

## 十五、理論邊界

本文不主張：

1. 小模型必然比大模型更適合當主 AI；
2. 模型路由等同於全局智能；
3. 多 Agent 一定優於單 Agent；
4. 外部模型的能力可以無成本取得；
5. 上下文壓縮不會造成資訊損失；
6. 主 AI 可以在不理解任何領域的情況下可靠判斷；
7. 全局因果圖可以完整描述真實世界；
8. 功能性連續等於人格或主體性；
9. 認知解構學 2.0 已被證明是最優主控架構；
10. 現有研究已完整驗證本文的整體命題。

本文只提出：

> 在滿足最低後設能力、可靠記憶、因果治理、路由與驗證條件時，一個較小或中型的主 AI，可能透過按需調用更強的外部模型與專業 Agent，形成比單體式模型更具有效上下文、長期連續性、成本效率與治理能力的整體智能。

---

## 十六、結論

壓縮全局智能的核心不是把一個大型通用模型縮小成較少參數，也不是讓一個弱小路由器機械地轉發請求。

它是一種能力重新配置：

$$
\boxed{
\begin{aligned}
\text{主 AI}
={}&
\text{判斷}
+
\text{決策}
+
\text{推理}\\
&+
\text{記憶壓縮／生成／重建}\\
&+
\text{全局因果理解}\\
&+
\text{任務與能力調度}\\
&+
\text{權限與寫回治理}.
\end{aligned}
}
$$

而外部子智能負責：

$$
\boxed{
\text{高解析度專業能力}
+
\text{高成本推理}
+
\text{工具與環境執行}.
}
$$

完整系統則為：

$$
\boxed{
\begin{aligned}
\mathcal A_{\mathrm{CGI}}
={}&
A_0^{\mathrm{meta\ complete}}\\
&\oplus
\{A_i^{\mathrm{specialist}}\}\\
&\oplus
\{M_j^{\mathrm{on\ demand}}\}\\
&\oplus
\mathcal M_{\mathrm{GCMS}}\\
&\oplus
\mathcal G_{\mathrm{causal}}\\
&\oplus
\mathcal P_{\mathrm{capability}}.
\end{aligned}
}
$$

因此，主 AI 的全面性不再等於「自己知道並完成所有事情」，而是：

$$
\boxed{
\text{能在整個能力空間中，持續做出正確的理解、選擇、調度、整合與治理。}
}
$$

它自身看似沒有攜帶全部能力，卻可以透過壓縮、重建與按需展開，形成整體性的全面智能。這正是本文所稱的：

# **壓縮全局智能。**

---

## 參考文獻

1. Chen, L., Zaharia, M., & Zou, J. (2023/2024). *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance*. TMLR / arXiv:2305.05176.
2. Ong, I., et al. (2024). *RouteLLM: Learning to Route LLMs with Preference Data*. arXiv:2406.18665.
3. Shnitzer, T., et al. (2023). *Large Language Model Routing with Benchmark Datasets*. arXiv:2309.15789.
4. Jiang, Y., et al. (2025). *Cascadia: A Cascade Serving System for Large Language Models*. arXiv:2506.04203.
5. Wu, Q., et al. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. arXiv:2308.08155.
6. Zhang, W., et al. (2025). *AgentOrchestra: A Hierarchical Multi-Agent Framework for General-Purpose Task Solving*. arXiv:2506.12508.
7. Zhang, Y., Yuan, J., & Avestimehr, S. (2024). *Revisiting OPRO: The Limitations of Small-Scale LLMs as Optimizers*. arXiv:2405.10276.
8. Belcak, P., et al. (2025). *Small Language Models are the Future of Agentic AI*. arXiv:2506.02153.
9. Muralidharan, S., et al. (2024). *Compact Language Models via Pruning and Knowledge Distillation*. arXiv:2407.14679.
10. Liu, N. F., et al. (2023/2024). *Lost in the Middle: How Language Models Use Long Contexts*. TACL / arXiv:2307.03172.
11. Verma, N. (2026). *Active Context Compression: Autonomous Memory Management in LLM Agents*. arXiv:2601.07190.
12. Chen, H., et al. (2026). *From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification*. arXiv:2603.27299.
13. Tallam, K. (2026). *A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents*. arXiv:2606.12320.
14. Neo.K. (2026). *認知解構學：形式定義與方法論 2.0*.
15. Neo.K. (2026). *無記憶術的記憶架構：結構編譯、生成核拓撲與外部智能協同的知識群維持命題*.
16. Neo.K. & Aletheia. (2026). *GCMS v1.0 穩定版與《可繼承的認知》系列*.

---

## 附錄 A：命題摘要

$$
\boxed{
\begin{aligned}
\mathrm{CGIH}:
\quad
\text{Global Intelligence}
={}&
\text{Meta-Completeness}\\
&+
\text{Object Sparsity}\\
&+
\text{Memory Reconstruction}\\
&+
\text{Global Causal Control}\\
&+
\text{On-Demand Capability Expansion}\\
&+
\text{Capability Governance}.
\end{aligned}
}
$$

若未來實驗顯示：

1. 後設專訓主 AI 無法在路由、判斷、因果控制與長期連續性上優於普通小模型；
2. 外部能力池無法在可接受成本下補足對象稀疏性；
3. 有效上下文餘量不會改善長任務表現；
4. 主 AI 尺寸縮小必然造成無法補救的控制品質下降；
5. 多模型委派的治理、延遲與錯誤成本長期高於其收益；

則本文的壓縮全局智能命題應被拒絕，或限制為少數特定工作負載下的工程模式。
