# 超級智能的整合路徑：ASI 是否可能先以系統而非模型出現

## The Integration Path to Superintelligence: Could ASI Emerge at the System Level Before the Model Level?

**系列**：閉環全域智能：從模型競賽到文明級智能系統，第 2 篇／共 8 篇＋1 篇總結  
**系列英文名**：Closed-Loop Global Intelligence: From Model Competition to Civilization-Scale Intelligent Systems  
**文件編號**：EML-CLGI-2026-02-v0.1  
**作者**：Neo.K with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-09-02  
**性質**：理論框架／Superintelligence Studies／Agentic Systems／Systems Intelligence／Civilizational Intelligence  
**狀態**：Public Theory Draft  
**直接前置**：EML-CLGI-2026-01《模型不是智能系統：為什麼下一代 AI 競爭的基本單位正在改變》；《全域智能、資訊海與文明博弈》系列；《Agentic Organization 的時間經濟學》

---

## 生成、邊界與可反駁性聲明

本文是一篇 AI 輔助生成的理論研究稿。

本文不主張目前任何公開 AI 系統已達到 ASI，也不主張只要把現有模型、Agent、搜尋、記憶、資料庫、多智能體與機器人串接起來，就必然會形成 ASI。本文所提出的是一個結構性問題：

> 如果「超級智能」的比較對象不是單一人類，而是大型人類組織、科研體系、企業、政府與文明級協作系統，那麼 ASI 的前兆與部分功能，是否可能先在整合系統層出現，而不是等待某一顆 foundation model 單獨跨過所有超人類能力門檻？

本文因此嚴格區分：

$$
\text{System-Level Superhuman Capability}
\neq
\text{ASI}.
$$

以及：

$$
\text{Integration Path}
\neq
\text{Guaranteed Path to ASI}.
$$

本文的任務不是重新定義 ASI 以降低門檻，而是避免另一種對稱性錯誤：將「模型還不是 ASI」誤寫成「由模型構成的整體智能系統也不可能具備超人類組織級能力」。

---

# 摘要

當代人工智慧關於 AGI 與 ASI 的主要敘事，長期以單一模型能力為中心。典型路徑可以表示為：更大規模的模型、更高品質資料、更強推理、更長上下文、更好的工具使用與自我改進，最終使一個模型在愈來愈多認知任務上超越人類，並從 AGI 進一步走向 ASI。本文將此路徑稱為「模型尺度路徑」或 Scaling Path。

然而，隨著 Agent、長期記憶、搜尋、工具、驗證、多智能體協作、資料庫、世界狀態、軟體執行、模擬環境與具身系統逐漸成熟，另一條發展路徑開始變得不可忽略。即使單一模型尚未在所有認知領域超越頂尖人類，一個由多個模型實例、外部知識、長期狀態、平行任務、驗證流程、計算資源與世界操作能力共同構成的系統，仍可能先在某些長週期工作上超越大型人類組織。本文將此路徑稱為「超級智能的整合路徑」：

$$
\boxed{
\text{Integration Path to Superintelligence}
}
$$

本文首先區分「模型智能」與「整合系統智能」兩條曲線：

$$
M(t)
=
\text{Model Intelligence},
$$

$$
G(t)
=
\text{Integrated System Intelligence}.
$$

若傳統 ASI 敘事主要依賴：

$$
M(t)
\uparrow\uparrow,
$$

則整合路徑允許另一種可能：

$$
M(t)
\uparrow,
\qquad
G(t)
\uparrow\uparrow\uparrow.
$$

此時，整體能力的增長來自資訊覆蓋、持續記憶、Agent loop、多智能體平行度、外部工具、驗證、世界狀態與算力調度，而不只來自單輪模型能力的增長。

本文進一步提出「組織超越門檻」：

$$
\Theta_{\mathrm{org}},
$$

表示一個 AI 系統在特定任務域中，其品質調整後的長週期產出、速度、規模、記憶連續性、搜尋廣度、驗證能力與資源調度能力，開始長期超過可比大型人類組織。跨過此門檻並不等於 ASI，但它可能是文明第一次面對「沒有一個單獨 AI 必須成為神級模型，整個 AI 系統仍然能在組織尺度上超人類」的情況。

本文並分析整合路徑的核心限制：誤差累積、不可觀測錯誤、目標錯置、資料污染、權限治理、資源分配、跨 Agent 狀態不一致、反身性與世界介入風險。這些限制使系統能力無法簡化為元件能力的線性相加。系統可能產生正協同，也可能因協調成本而崩潰。因此本文提出：

$$
G
=
\Phi(
M,
K,
S,
A,
V,
P,
R,
E
)
-
\Omega,
$$

其中 $\Omega$ 表示整合摩擦、協調成本與錯誤傳播。

本文最後主張：AGI→ASI 的研究不應只問「下一顆模型還需要多聰明」，也應問「在模型能力尚未完全跨過超人類門檻之前，整合系統已經能做到什麼」。如果一個非 ASI 模型可以透過持續 Agent、全球級資訊海、長期記憶、驗證、多智能體與世界執行形成超越人類組織的有效能力，則未來文明所面對的首個超人類智能組織，可能不是一顆單一模型，而是一個由大量可替換模型組成的持續智能系統。

**關鍵詞**：ASI、AGI、整合路徑、系統智能、Agent、multi-agent、閉環智能、組織超越門檻、世界狀態、超人類組織能力

---

# 0. 問題的提出：ASI 一定要先是一顆模型嗎？

對 ASI 最直覺的想像通常是：

> 有一天，一顆模型在數學、科學、程式、策略、語言、創造、研究與決策上全面超越所有人類。

可抽象為：

$$
M_{\mathrm{ASI}}
>
H_{\mathrm{best}}
$$

對足夠廣泛的認知任務集合成立。

這是一個合理而重要的定義方向。

但它隱含了一個尚未被充分檢查的假設：

$$
\boxed{
\text{The unit of superintelligence is the model.}
}
$$

如果前一篇所提出的：

$$
M_t
\neq
\mathcal G_t
$$

成立，則一個自然問題隨之出現：

> 超級智能的比較單位，也許不應只是一顆模型。

因為現實世界中真正完成大型高價值工作的，通常本來就不是單一人類。

一座晶圓廠不是一個人。

一個國家科研體系不是一個人。

一家大型軟體公司不是一個人。

一個金融市場參與者網路不是一個人。

甚至一篇重大科學成果，也可能依賴：

$$
\text{Researchers}
+
\text{Computers}
+
\text{Labs}
+
\text{Databases}
+
\text{Institutions}
+
\text{Peer Review}.
$$

因此，如果 AI 系統的真實競爭對象逐漸從：

$$
\text{single human}
$$

轉向：

$$
\text{human organization},
$$

那麼 ASI 的前置現象也可能首先在組織尺度上出現。

---

# 1. 兩條不同的超級智能路徑

本文先定義兩條理論路徑。

## 1.1 模型尺度路徑

第一條是傳統路徑：

$$
M_0
\longrightarrow
M_1
\longrightarrow
M_2
\longrightarrow
\cdots
\longrightarrow
M_{\mathrm{AGI}}
\longrightarrow
M_{\mathrm{ASI}}.
$$

其主要進步來源可能包括：

$$
\text{Scaling},
$$

$$
\text{Architecture},
$$

$$
\text{Training Data},
$$

$$
\text{Post-training},
$$

$$
\text{Reasoning},
$$

$$
\text{Self-improvement}.
$$

本文稱之為：

$$
\boxed{
\text{Scaling Path}
}
$$

這裡的「Scaling」不是狹義只指參數增加，而泛指以模型本身能力上升為主軸的路徑。

---

## 1.2 整合系統路徑

第二條則是：

$$
M
+
K
+
S
+
A
+
V
+
P
+
R
+
E
\longrightarrow
G.
$$

其中：

$$
M
=
\text{model capability},
$$

$$
K
=
\text{knowledge and information access},
$$

$$
S
=
\text{persistent state and memory},
$$

$$
A
=
\text{agentic autonomy},
$$

$$
V
=
\text{verification},
$$

$$
P
=
\text{parallelism and multi-agent coordination},
$$

$$
R
=
\text{resource allocation},
$$

$$
E
=
\text{execution and world interaction}.
$$

本文稱之為：

$$
\boxed{
\text{Integration Path}
}
$$

這條路徑不要求：

$$
M
=
M_{\mathrm{ASI}}.
$$

它要求的是：

$$
\boxed{
G
\text{ 的整體有效能力持續提高。}
}
$$

---

# 2. 模型智能曲線與系統智能曲線

令：

$$
M(t)
=
\text{單一模型在時間 } t \text{ 的能力},
$$

以及：

$$
G(t)
=
\text{整體智能系統在時間 } t \text{ 的有效能力}.
$$

若 AI 發展主要靠模型進步，則：

$$
G(t)
\approx
f(M(t)).
$$

但當搜尋、Agent、記憶、驗證、多智能體、世界狀態與執行能力加入後：

$$
G(t)
=
\Phi(
M(t),
K(t),
S(t),
A(t),
V(t),
P(t),
R(t),
E(t)
).
$$

此時可能出現：

$$
\frac{dM}{dt}
>
0,
$$

但：

$$
\frac{dG}{dt}
\gg
\frac{dM}{dt}.
$$

也就是：

> 模型沒有突然變成神級智能，但整個 AI 系統的可實現能力卻快速上升。

這是本文最核心的理論可能性。

---

# 3. 為什麼大型人類組織是更合理的比較單位

如果一個 AI 系統可以：

- 同時啟動上千個研究任務；
- 存取龐大資料庫；
- 讀取最新資訊；
- 跨語言檢索；
- 長期保存工作狀態；
- 自動執行程式；
- 進行交叉驗證；
- 自動產生實驗；
- 分配算力；
- 追蹤專案依賴；
- 長期維持任務。

那麼將它只和一名人類比較會產生測量偏差。

因為它真正模擬或替代的可能是：

$$
\text{Department},
$$

$$
\text{Research Lab},
$$

$$
\text{Enterprise},
$$

甚至：

$$
\text{Institutional Network}.
$$

因此可以定義：

$$
H_{\mathrm{org}}
=
\text{human organizational cognitive capability}.
$$

當：

$$
G
>
H_{\mathrm{org}}
$$

在某個任務域長期成立時，系統已經形成：

$$
\boxed{
\text{Organizational Superhuman Capability}.
}
$$

但本文強調：

$$
\boxed{
G > H_{\mathrm{org}}
\not\Rightarrow
G = ASI.
}
$$

因為一個系統可能只在特定類型的大規模組織工作中超越人類，而在價值判斷、新概念形成、陌生環境、物理常識或其他領域仍有重大限制。

---

# 4. 組織超越門檻

本文定義一個概念：

$$
\Theta_{\mathrm{org}}
=
\text{Organizational Superhuman Threshold}.
$$

若對某任務域 $\mathcal T$，AI 系統滿足：

$$
Q_G
\ge
Q_{\mathrm{org}},
$$

$$
R_G
\ge
R_{\mathrm{org}},
$$

$$
T_G
<
T_{\mathrm{org}},
$$

$$
C_G
<
C_{\mathrm{org}},
$$

且：

$$
P_G
>
P_{\mathrm{org}},
$$

其中：

- $Q$ 為品質；
- $R$ 為可靠性；
- $T$ 為完成曆時；
- $C$ 為成本；
- $P$ 為可利用平行度；

則可說該系統在此任務域跨過：

$$
\Theta_{\mathrm{org}}.
$$

注意，這裡比較的是：

$$
\text{AI system}
$$

與：

$$
\text{human organization},
$$

不是：

$$
\text{AI model}
$$

與：

$$
\text{best human genius}.
$$

這會導致完全不同的發展時間線。

---

# 5. 為什麼中上模型也可能形成超強系統

考慮一個極簡例子。

假設模型 A 的單次任務品質只有：

$$
Q_A
=
0.82.
$$

它並沒有全面超越頂尖人類。

但它可以：

- 24 小時持續工作；
- 平行啟動 10,000 個工作節點；
- 存取完整任務資料庫；
- 自動查資料；
- 自動執行工具；
- 自動驗證；
- 局部錯誤自我恢復；
- 保存多年歷史狀態。

則其總有效工作能力可以粗略表示為：

$$
W_G
=
Q_A
\cdot
R_A
\cdot
T_A
\cdot
P_A
\cdot
\eta_V,
$$

其中：

$$
\eta_V
=
\text{verification-adjusted survival rate}.
$$

此時：

$$
Q_A
<
Q_{\mathrm{elite\ human}}
$$

仍然可能與：

$$
W_G
\gg
W_{\mathrm{human\ organization}}
$$

同時成立。

因此：

$$
\boxed{
\text{Per-task Intelligence}
\neq
\text{Aggregate Cognitive Power}.
}
$$

---

# 6. 平行性是整合路徑的關鍵槓桿

人類組織可以擴張，是因為：

$$
N_{\mathrm{human}}
\uparrow.
$$

AI 系統則可以：

$$
N_{\mathrm{agent}}
\uparrow.
$$

但 Agent 數量本身不代表有效能力。

令總 interaction work 為：

$$
W_I,
$$

不可約依賴深度為：

$$
D_I.
$$

則理想平行度可表示為：

$$
\Pi_I
=
\frac{
W_I
}{
D_I
}.
$$

若：

$$
\Pi_I
\approx
1,
$$

增加大量 Agent 幾乎沒有幫助。

若：

$$
\Pi_I
\gg
1,
$$

則多智能體系統可能將大量原本需要很長曆時的人類工作壓縮到同一世界時間內。

因此 Integration Path 的一個核心不是：

$$
\text{More Agents},
$$

而是：

$$
\boxed{
\text{More exploitable cognitive parallelism}.
}
$$

---

# 7. 資訊海使系統能力與模型能力進一步解耦

若 AI 只依賴參數內知識：

$$
K_{\theta},
$$

則模型本身決定大量能力上限。

但若 AI 可以持續存取：

$$
K_{\mathrm{web}},
$$

$$
K_{\mathrm{science}},
$$

$$
K_{\mathrm{code}},
$$

$$
K_{\mathrm{private}},
$$

$$
K_{\mathrm{history}},
$$

並建立：

$$
K_{\mathrm{integrated}},
$$

則整體能力變成：

$$
K_G
=
K_{\theta}
+
K_{\mathrm{external}}
+
K_{\mathrm{persistent}}
+
K_{\mathrm{dynamic}}.
$$

這意味著：

$$
\boxed{
\text{the model no longer needs to internally memorize the whole world}.
}
$$

模型需要的是：

1. 知道什麼時候應該查；
2. 知道查什麼；
3. 知道如何判斷來源；
4. 知道如何處理矛盾；
5. 知道何時資訊不足；
6. 知道如何更新持續狀態。

這使「世界資訊基礎設施」本身成為智能的一部分。

---

# 8. 持續狀態使智能第一次擁有歷史

單輪模型沒有真正意義上的外部工作歷史。

它可以知道：

$$
K_{\theta},
$$

但它不一定擁有：

$$
S_{0:t},
$$

即自己過去數月或數年在真實任務中形成的持續世界狀態。

如果 Agent 系統具有：

$$
S_{t+1}
=
U(
S_t,
O_t,
E_t,
V_t
),
$$

則：

$$
S_t
$$

本身開始成為資產。

這表示：

> 系統今天的能力不只來自今天的模型，也來自昨天已經完成並驗證的工作。

因此：

$$
G_t
=
F(
M_t,
S_t
).
$$

即使：

$$
M_{t+1}
=
M_t,
$$

只要：

$$
S_{t+1}
>
S_t,
$$

整體：

$$
G_{t+1}
>
G_t
$$

仍可能成立。

這是模型中心視角非常容易忽略的累積性。

---

# 9. 世界沉積與系統級學習

當 Agent 完成：

- 新資料庫；
- 新工具；
- 新驗證器；
- 新程式；
- 新研究結果；
- 新資料分類；
- 新來源圖；
- 新錯誤案例；
- 新工作流程；

這些結果可以成為下一輪智能活動的輸入。

因此：

$$
\text{Output}_t
\longrightarrow
\text{Infrastructure}_{t+1}.
$$

進一步：

$$
\text{Infrastructure}_{t+1}
\longrightarrow
\text{Better Output}_{t+1}.
$$

形成：

$$
\boxed{
\text{Cumulative Intelligence Infrastructure Loop}.
}
$$

此循環不需要模型權重每一輪都更新。

所以必須區分：

$$
\text{Model Learning}
$$

與：

$$
\text{System Learning}.
$$

前者是：

$$
\theta_t
\longrightarrow
\theta_{t+1}.
$$

後者則可能是：

$$
\mathcal G_t
\longrightarrow
\mathcal G_{t+1}
$$

即使：

$$
\theta_t
=
\theta_{t+1}.
$$

這就是整合路徑中非常重要的「非權重學習」。

---

# 10. 系統級自我改進不等於模型級遞歸自我改進

ASI 討論常提到：

$$
\text{Recursive Self-Improvement}.
$$

傳統想像是：

$$
M_t
\rightarrow
M_{t+1}
\rightarrow
M_{t+2}.
$$

也就是 AI 改善自己的模型。

但整合路徑還存在另一種較弱但更早可能出現的形式：

$$
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
$$

例如 Agent 可以：

- 改善搜尋策略；
- 建立新的索引；
- 新增驗證器；
- 改寫 orchestration；
- 自動生成工具；
- 優化資料結構；
- 重新安排工作流；
- 建立更好的記憶檢索；
- 發現某個失敗模式後新增 hard gate。

這些都可能使：

$$
G_{t+1}
>
G_t
$$

而不需要：

$$
M_{t+1}
>
M_t.
$$

因此可以定義：

$$
\boxed{
\text{System Recursive Improvement}
}
$$

並區分於：

$$
\boxed{
\text{Model Recursive Improvement}.
}
$$

這兩者最終可能互相耦合，但不應在理論上混為一談。

---

# 11. 模型可以成為可替換部件

若一個系統已經建立：

$$
\mathcal D
=
\text{persistent data layer},
$$

$$
\mathcal S
=
\text{state and memory layer},
$$

$$
\mathcal V
=
\text{verification layer},
$$

$$
\mathcal A
=
\text{agent runtime},
$$

則模型可以表示為：

$$
M^{(1)}
\rightarrow
M^{(2)}
\rightarrow
M^{(3)}.
$$

只要介面保持可交換：

$$
\mathcal G
=
\Phi(
M,
\mathcal D,
\mathcal S,
\mathcal V,
\mathcal A
),
$$

系統就可以不斷替換更強模型。

因此真正累積性較高的資產可能不是：

$$
M_t,
$$

而是：

$$
\boxed{
\mathcal I_{\mathrm{persistent}}
=
\mathcal D
+
\mathcal S
+
\mathcal V
+
\mathcal A
+
\mathcal H,
}
$$

其中：

$$
\mathcal H
=
\text{historical interaction and task experience}.
$$

這意味著某個組織可以先用 open-weight 模型建立完整智能基礎設施，再在未來替換成自己的模型，而不需要等自家模型先成為世界第一才開始建立閉環。

---

# 12. 整合的真正困難：能力不是線性相加

必須避免另一個極端：

> 既然所有零件都有，把它們接起來就等於超級智能。

這是錯誤的。

更合理的表示是：

$$
G
=
\Phi(
M,
K,
S,
A,
V,
P,
R,
E
)
-
\Omega.
$$

其中：

$$
\Omega
=
\text{integration friction}.
$$

 $\Omega$ 可以包含：

- 跨 Agent 狀態衝突；
- 錯誤傳播；
- 資訊污染；
- 任務重複；
- 權限錯配；
- 目標不一致；
- 資源競爭；
- context drift；
- 記憶污染；
- 驗證失敗；
- coordination overhead；
- latency；
- security constraints。

所以：

$$
G
\neq
M+K+S+A+V+P+R+E.
$$

真正問題是：

$$
\boxed{
\text{Can integration gains exceed integration friction?}
}
$$

只有當：

$$
\Delta G_{\mathrm{integration}}
>
\Delta \Omega,
$$

整合才具有正淨收益。

---

# 13. 錯誤傳播可能是 Integration Path 的硬上限

如果一個 Agent 錯誤率為：

$$
e,
$$

而錯誤會被寫入持續狀態：

$$
S_t,
$$

則：

$$
S_t
$$

可能逐步受到污染。

如果多 Agent 又相互引用：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3,
$$

一個局部錯誤甚至可能轉成：

$$
\text{Systemic Error}.
$$

因此 Integration Path 的真正核心不是「更多 Agent」，而是：

$$
\boxed{
\text{Error Containment Architecture}.
}
$$

它至少需要：

$$
\text{Provenance},
$$

$$
\text{Verification},
$$

$$
\text{Rollback},
$$

$$
\text{Confidence},
$$

$$
\text{Conflict Detection},
$$

$$
\text{Human Escalation}.
$$

長期系統要最小化的不是：

$$
P(\text{any local error}),
$$

而是：

$$
\boxed{
P(
\text{undetected error}
\rightarrow
\text{persistent contamination}
).
}
$$

---

# 14. 世界介入使系統智能比模型智能更危險

單一模型的錯誤主要造成：

$$
\text{bad output}.
$$

具備 Agent 與世界操作能力的系統錯誤可能造成：

$$
\text{bad state transition}.
$$

即：

$$
S_t
\longrightarrow
S_{t+1}^{\mathrm{wrong}}.
$$

如果系統還具有：

$$
\text{Capital Allocation},
$$

$$
\text{Software Deployment},
$$

$$
\text{Robotics},
$$

$$
\text{Communication},
$$

則錯誤可能進一步變成：

$$
\text{World Mutation}.
$$

因此：

$$
\boxed{
\text{System Capability Growth}
\Rightarrow
\text{Governance Requirement Growth}.
}
$$

整合路徑越成功，權限、驗證與可逆性越重要。

---

# 15. 超級智能的比較對象可能分成三層

為避免「一個很強的 Agent 系統就是 ASI」的概念膨脹，本文提出三層比較。

## 15.1 個體超人類

$$
G
>
H_{\mathrm{individual}}.
$$

系統在大量個人級任務上超過大多數人類。

---

## 15.2 組織超人類

$$
G
>
H_{\mathrm{organization}}.
$$

系統在長週期、多任務、大規模協作上超過大型人類組織。

---

## 15.3 廣義超級智能

$$
G
>
H_{\mathrm{civilizational\ frontier}}
$$

在足夠廣泛的重要認知領域中，系統持續超過人類文明當前可組織出的最佳能力。

只有第三層才接近本文願意保留給 ASI 的嚴格含義。

因此：

$$
\boxed{
\Theta_{\mathrm{individual}}
<
\Theta_{\mathrm{org}}
<
\Theta_{\mathrm{ASI}}
}
$$

是較合理的概念結構。

---

# 16. ASI 可能先以「組織」而不是「人格」被觀察到

流行文化常把超級智能想像成：

> 一個會說話的超級人格。

但如果整合路徑成立，第一個逼近超級智能的系統，可能根本沒有單一穩定人格。

它可能是：

$$
\mathcal G
=
\{
M_1,
M_2,
\ldots,
M_n,
A_1,
A_2,
\ldots,
A_k
\}
$$

加上：

$$
\text{Databases}
+
\text{Tools}
+
\text{Verification}
+
\text{World State}.
$$

外界看到的不是：

> 「某一個 AI 突然變成 ASI。」

而可能是：

> 「這個組織突然能以人類無法匹敵的速度，同時完成科研、軟體、資訊整合、資源配置與策略分析。」

因此超級智能的第一個可觀測形態，可能更像：

$$
\boxed{
\text{Institutional Intelligence}
}
$$

而不是：

$$
\boxed{
\text{Singular Supermind}.
}
$$

---

# 17. 這改變了「AGI 到 ASI」的時間線

傳統時間線：

$$
\text{LLM}
\rightarrow
\text{AGI Model}
\rightarrow
\text{ASI Model}.
$$

整合路徑則可能是：

$$
\text{Strong Model}
\rightarrow
\text{Agent System}
\rightarrow
\text{Persistent Organization}
\rightarrow
\text{Organizational Superhuman System}
\rightarrow
\text{Further Integration}
\rightarrow
\text{Possible ASI}.
$$

甚至：

$$
M_t
<
M_{\mathrm{AGI}}
$$

與：

$$
G_t
>
H_{\mathrm{organization}}
$$

可能在某些任務域同時成立。

這不代表「沒有 AGI 就有 ASI」，而是表示：

$$
\boxed{
\text{model-level taxonomy}
\text{ and }
\text{system-level capability}
\text{ need not cross thresholds in the same order}.
}
$$

---

# 18. Integration Path 的資本意義

如果提升模型一個單位能力需要：

$$
C_M,
$$

而建立搜尋、記憶、Agent、驗證與資料基礎設施需要：

$$
C_I,
$$

則企業真正應比較的是：

$$
\frac{
\Delta G_M
}{
C_M
}
$$

與：

$$
\frac{
\Delta G_I
}{
C_I
}.
$$

如果某階段：

$$
\frac{
\Delta G_I
}{
C_I
}
>
\frac{
\Delta G_M
}{
C_M
},
$$

則從整體智能角度：

> 投資整合層可能比再提升模型一小段更有效。

這不代表停止前沿模型研究。

而是表示資本配置問題從：

$$
\text{Model Maximization}
$$

轉成：

$$
\boxed{
\text{System Intelligence Optimization}.
}
$$

---

# 19. Integration Path 的人才意義

如果 AI 系統的核心問題從：

$$
\text{train a model}
$$

轉向：

$$
\text{design a persistent intelligence system},
$$

那人才結構也會改變。

重要人才可能從單純：

$$
\text{AI specialist}
$$

擴張為：

$$
\text{AI}
+
\text{Systems}
+
\text{Databases}
+
\text{Mathematics}
+
\text{Verification}
+
\text{Security}
+
\text{Economics}
+
\text{Cognitive Science}
+
\text{Robotics}.
$$

這並不是說上一代 AI 專家失去價值。

而是：

$$
\boxed{
\text{Previous-domain prestige}
\not\Rightarrow
\text{future-system leverage}.
}
$$

當既有 AI 知識可以大量由 AI 本身協助補足時，跨領域抽象、問題形成、形式化能力與系統整合能力的邊際價值可能上升。

---

# 20. Integration Path 也可能失敗

本文必須保留一個重要反命題。

可能存在：

$$
M<M^{*},
$$

使得只要基礎模型能力沒有跨過某個門檻：

$$
G
$$

就無法因整合而持續提升。

例如：

- 模型不能可靠理解自己的工具輸出；
- 無法判斷資訊品質；
- 無法維持長期目標；
- 無法發現隱性錯誤；
- 無法處理陌生問題；
- 無法有效協調其他 Agent。

則：

$$
\Omega
$$

可能快速上升。

此時：

$$
\Delta G_{\mathrm{integration}}
<
\Delta \Omega.
$$

整個系統只會變成大量互相放大錯誤的 Agent 網路。

因此 Integration Path 並不是「繞過模型智能」。

更精確是：

$$
\boxed{
\text{Once models cross a sufficient competence threshold, integration may become the dominant marginal source of effective intelligence.}
}
$$

這是一個可實證檢驗的命題。

---

# 21. 從超級模型問題轉向超級系統問題

因此，關於 ASI 的研究至少應同時問兩組問題。

## 模型問題

- 模型能否形成新理論？
- 模型能否自主改善模型？
- 模型能否超過頂尖人類研究者？
- 模型是否具有足夠廣泛的通用能力？

## 系統問題

- 系統能否持續取得世界資訊？
- 系統能否長期保持可信狀態？
- 多 Agent 能否有效平行而非互相污染？
- 系統能否自動驗證與回溯？
- 系統能否建立內生知識資產？
- 系統能否將輸出持續沉積成下一輪基礎設施？
- 系統能否超越大型人類組織的曆時與協作瓶頸？

這兩組問題不能互相取代。

---

# 22. 一個新的 ASI 前兆指標：組織尺度智能密度

沿用時間經濟學，可定義：

$$
\rho_{\mathrm{intel}}
=
\frac{
W_I^{\mathrm{quality\ adjusted}}
}{
\Delta t_W
}.
$$

若進一步只計算長期可驗證沉積：

$$
\rho_{\mathrm{commit}}
=
\frac{
V_{\mathrm{verified\ world\ commit}}
}{
\Delta t_W
}.
$$

則一個可能的 ASI 前兆，不是單純：

$$
\text{benchmark score}
\uparrow,
$$

而是：

$$
\boxed{
\rho_{\mathrm{commit}}^{AI\ system}
>
\rho_{\mathrm{commit}}^{large\ human\ organization}
}
$$

在越來越多高價值任務域中持續成立。

這種比較比「模型是否在某一測試高於人類」更接近文明實際感受到的能力差。

---

# 23. 系統級超級智能與權力問題

若一個系統同時具備：

$$
\text{Observation}
+
\text{Knowledge}
+
\text{Prediction}
+
\text{Action},
$$

其能力不再只是「知道很多」。

而是形成：

$$
\text{Observe}
\rightarrow
\text{Model}
\rightarrow
\text{Decide}
\rightarrow
\text{Act}
\rightarrow
\text{Observe}.
$$

如果再加入：

$$
\text{Capital},
$$

$$
\text{Compute},
$$

$$
\text{Infrastructure},
$$

則可能形成自我增強的組織能力。

因此 Integration Path 不只是 AI engineering 問題。

它同時是：

$$
\boxed{
\text{Political Economy of Intelligence}.
}
$$

這也是為什麼系統能力的集中與多個局部全域 AI 的存在，會成為後續文明治理問題。

---

# 24. 結論：ASI 的第一個影子，可能不是一顆模型

本文不主張：

$$
\text{Current Agent Systems}
=
\text{ASI}.
$$

也不主張：

$$
\text{Enough Components}
\Rightarrow
\text{ASI}.
$$

本文提出的是一個更窄、更具可檢驗性的命題：

$$
\boxed{
\text{System-level superhuman organizational intelligence may emerge before model-level ASI.}
}
$$

其原因在於：

1. 模型能力與系統能力不同；
2. 外部資訊降低模型內部記憶的必要性；
3. Agent loop 允許持續取得新世界資訊；
4. 長期記憶允許歷史累積；
5. 多 Agent 提供可利用平行度；
6. 驗證與恢復降低長週期錯誤；
7. 世界沉積使今天的工作成為明天的基礎設施；
8. 模型可以成為可替換認知元件。

因此：

$$
M(t)
$$

與：

$$
G(t)
$$

必須分開追蹤。

真正值得問的不是：

> 「下一顆模型是不是 ASI？」

而還包括：

> 「即使沒有任何一顆模型是 ASI，整個 AI 組織的有效能力是否已經跨過大型人類組織？」

如果答案在愈來愈多任務域變成肯定，那麼文明可能先遇到的不是：

$$
\boxed{
\text{ASI as a Model}
}
$$

而是：

$$
\boxed{
\text{Superhuman Intelligence as an Organization}.
}
$$

這會使 AGI→ASI 的研究從單純的模型尺度問題，擴張為：

$$
\boxed{
\text{Model Intelligence}
+
\text{System Integration}
+
\text{World Coupling}
+
\text{Historical Accumulation}.
}
$$

---

## 核心命題摘要

### 命題一：超級智能至少存在兩條理論路徑

$$
\boxed{
\text{Scaling Path}
\quad\text{與}\quad
\text{Integration Path}.
}
$$

### 命題二：模型智能與整合系統智能應分別測量

$$
\boxed{
M(t)
\neq
G(t).
}
$$

### 命題三：系統可能先跨過組織超人類門檻

$$
\boxed{
G
>
H_{\mathrm{organization}}
}
$$

不必要求：

$$
M
>
H_{\mathrm{best\ individual}}.
$$

### 命題四：系統學習可以先於模型權重更新

$$
\boxed{
\mathcal G_t
\rightarrow
\mathcal G_{t+1}
}
$$

即使：

$$
\theta_t
=
\theta_{t+1}.
$$

### 命題五：整合能力不是元件能力的線性相加

$$
\boxed{
G
=
\Phi(
M,K,S,A,V,P,R,E
)
-
\Omega.
}
$$

### 命題六：Integration Path 的核心瓶頸是錯誤污染與整合摩擦

$$
\boxed{
\Delta G_{\mathrm{integration}}
>
\Delta \Omega
}
$$

是整合產生正淨能力的必要條件。

### 命題七：組織級超人類能力不等於 ASI

$$
\boxed{
\text{Organizational Superhuman Capability}
\neq
\text{ASI}.
}
$$

### 命題八：ASI 的第一個可觀測前兆可能是制度級而非人格級

$$
\boxed{
\text{Institutional Superintelligence Precursor}
}
$$

可能先於：

$$
\boxed{
\text{Singular Supermind}.
}
$$

---

## 系列接口

Paper 01 將模型與智能系統分離。

Paper 02 則進一步證明：即使不降低 ASI 的嚴格定義，也必須承認存在一個重要中間層：

$$
\boxed{
\text{Organizational Superhuman Intelligence}.
}
$$

下一篇將研究這個中間層最先可能產生的經濟相變：

**Paper 03：《可靠自主勞動門檻：為什麼經濟相變不必等待 AGI》**

其核心問題是：

> 如果一個 Agent 尚未達到 AGI，但已能以低錯誤率、可恢復、長期自主與中上品質持續完成工作，它是否已足以成為一個新的機器勞動單元，並先於 AGI 改變公司、職業與時間經濟結構？
