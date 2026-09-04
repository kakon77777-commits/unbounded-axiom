# 模型不是智能系統：為什麼下一代 AI 競爭的基本單位正在改變

## Models Are Not Intelligent Systems: Why the Unit of Competition in AI Is Changing

**系列**：閉環全域智能：從模型競賽到文明級智能系統，第 1 篇／共 8 篇＋1 篇總結  
**系列英文名**：Closed-Loop Global Intelligence: From Model Competition to Civilization-Scale Intelligent Systems  
**文件編號**：EML-CLGI-2026-01-v0.1  
**作者**：Neo.K with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-09-02  
**性質**：理論框架／AI Systems Theory／Agentic Systems／Temporal Economics／Global Intelligence  
**狀態**：Public Theory Draft  
**直接前置**：《全域智能、資訊海與文明博弈》系列、《AI 時間槓桿的多重估值》、《Agentic Organization 的時間經濟學》

---

## 生成、邊界與可反駁性聲明

本文是一篇 AI 輔助生成的理論研究稿，討論的是 AI 能力的系統性表示、Agent 閉環、資訊外部化、持續狀態與文明級智能基礎設施之間的關係。

本文不主張任何特定公司、政府或研究機構已經建成文中所描述的完整系統，也不主張本文提出的發展路徑必然發生。本文所建立的是一個可供比較、反駁與後續實證的分析框架。

本文特別區分：

$$
\text{Model Capability}
\neq
\text{System Intelligence}.
$$

同時也區分：

$$
\text{Possible Architecture}
\neq
\text{Observed Deployment}.
$$

本文的核心目的不是將所有 AI 發展簡化成 Agent，也不是否定 foundation model、pretraining、post-training 或 scaling 的重要性，而是指出：當模型已足以進入長週期工作、外部資訊取得、工具使用、驗證、記憶與持續世界狀態之後，僅以「單一模型能力」作為下一代 AI 競爭的基本單位，可能已經不足。

---

# 摘要

過去十餘年的人工智慧競爭，主要以模型作為能力的基本單位。參數規模、訓練算力、資料量、benchmark、單輪推理、程式能力與多模態能力，構成了衡量前沿位置的主要指標。這套框架在模型能力快速增長的階段具有高度解釋力；然而，當 AI 開始具備工具使用、網路搜尋、程式執行、持續記憶、長週期 Agent loop、多 Agent 協作、外部驗證與真實世界操作能力時，「模型有多聰明」與「整個智能系統能完成多少事情」開始出現結構性分離。

本文提出：下一代 AI 的主要競爭單位可能逐漸從單一 foundation model，轉向由模型、外部知識、持續狀態、檢索、工具、Agent 控制迴路、驗證、資源配置與世界提交共同構成的閉環智能系統。本文以一個反事實世界作為思想實驗：若 AI 模型持續變強，但人類從未發明 Agent loop，AI 仍只能在單輪對話中回應，並必須由使用者手動觸發下一輪，即使模型能在單輪中完成高品質數學推導或軟體設計，整個生產流程仍會受到人類治理時間、外部資訊取得、真實執行結果與不可預知世界狀態的限制。

本文據此區分「隱式迭代」與「顯式閉環」。單輪超長推理可以在模型內部隱含地執行大量認知步驟，但只有顯式閉環能夠在中間節點取得新的真實資訊、執行動作、觀察結果、修正錯誤並持續累積外部狀態。Agent 的意義因此不只是將複雜問題拆步，而是把原本由人類擔任的控制器逐步機器化，使 AI 從一次性認知算子轉變為持續工作的智能過程。

本文進一步提出「閉環有效智能」與「世界沉積」概念。真正重要的能力不只在於一次輸出的品質，而在於系統能否將機器智能時間轉化為可驗證、可累積、可重用的世界狀態。若一個能力僅為中上但低錯誤、可恢復、能持續運行的 Agent，可以在數日、數月與數年內持續建立資料庫、軟體、知識圖譜、研究紀錄、驗證鏈與組織資產，則其經濟與文明效果可能顯著超過一個單輪能力更高、卻無法自主維持控制迴路的模型。

本文最後主張，未來 AI 競爭不應只觀察：

$$
M_t,
$$

即某一時間點的模型能力，而應同時觀察：

$$
\mathcal G_t,
$$

即由模型與外部世界耦合形成的整體智能系統。當：

$$
\frac{\partial \mathcal G}{\partial K},
\quad
\frac{\partial \mathcal G}{\partial A},
\quad
\frac{\partial \mathcal G}{\partial V},
\quad
\frac{\partial \mathcal G}{\partial C}
$$

在某些任務域開始高於單純提高模型能力的邊際收益時，AI 發展的主要戰場就可能由「誰有最強模型」轉向「誰擁有最完整、最可靠、最能持續累積的智能閉環」。

**關鍵詞**：foundation model、Agent、閉環智能、持續狀態、世界沉積、資訊海、外部記憶、長週期任務、系統智能、時間經濟學

---

# 0. 問題的提出：如果世界從未發明 Agent

考慮一個反事實世界。

在這個世界中，語言模型仍然沿著現實世界相似的方向持續變強。模型擁有更大的上下文、更好的推理、更高的數學能力、更強的程式設計能力、更完整的多模態理解，也可能擁有某種跨對話記憶。

但是有一件事從未出現：

> 沒有人提出讓 AI 自己進入「規劃、行動、觀察、修正、再行動」的持續控制迴路。

AI 永遠維持：

$$
\text{Prompt}
\longrightarrow
\text{Response}.
$$

下一輪必須由人類重新觸發：

$$
\text{Human Trigger}
\longrightarrow
\text{Next Prompt}
\longrightarrow
\text{Next Response}.
$$

即使模型已經強到可以在一次回答中完成一個優秀的軟體模組、提出一篇高水準研究草稿，甚至完成某些複雜數學推導，它仍然有一個結構性限制：

$$
\boxed{
\text{The model cannot autonomously maintain the task-control loop.}
}
$$

這個思想實驗的目的不是貶低單輪模型，而是暴露一個長期被「模型能力」指標遮蔽的問題：

> 一個極強的認知算子，與一個能長期維持工作狀態的智能系統，不是同一種東西。

---

# 1. 單輪智能與系統智能的分離

令模型在時間 $t$ 的單輪能力為：

$$
M_t.
$$

如果只以 benchmark、單次程式生成、一次數學解答或單輪分析品質衡量 AI，則可以近似寫成：

$$
I_{\mathrm{observed}}
\approx
f(M_t).
$$

然而，一個真實世界任務通常還需要：

$$
K_t
=
\text{external knowledge},
$$

$$
S_t
=
\text{persistent state},
$$

$$
A_t
=
\text{action capability},
$$

$$
V_t
=
\text{verification capability},
$$

$$
R_t
=
\text{resource allocation},
$$

$$
C_t
=
\text{continuity}.
$$

因此，對長週期真實任務更合理的表示是：

$$
\mathcal G_t
=
F(
M_t,
K_t,
S_t,
A_t,
V_t,
R_t,
C_t
).
$$

本文稱：

$$
\mathcal G_t
$$

為「閉環有效智能」的系統狀態。

這意味著：

$$
M_a > M_b
$$

並不必然推出：

$$
\mathcal G_a > \mathcal G_b.
$$

一個單輪能力較弱、但擁有可靠搜尋、工具、記憶、驗證與持續 Agent loop 的系統，在長週期工作中完全可能超過一個單輪能力更強但無法自主迭代的模型。

---

# 2. 一輪完成不是沒有迭代，而是把迭代藏進推理

假設一個極強模型可以在單輪中完成複雜數學證明。

其表面形式是：

$$
P
\longrightarrow
QED.
$$

但真正的內部認知過程不可能完全沒有中間結構。更合理的抽象是：

$$
P_0
\longrightarrow
H_1
\longrightarrow
L_1
\longrightarrow
H_2
\longrightarrow
L_2
\longrightarrow
\cdots
\longrightarrow
QED.
$$

其中：

- $H_i$ 表示某個假設、方向或候選推理；
- $L_i$ 表示局部推導或檢查結果。

因此，所謂「單輪完成」並不代表問題沒有被切分，而只是表示：

$$
\boxed{
\text{Iteration is internalized into one inference trajectory.}
}
$$

這種方法對封閉問題可能非常有效。

但一旦任務需要取得尚未存在的資訊，問題就改變了。

例如軟體工程中的：

$$
\text{Edit}
\longrightarrow
\text{Compile}
\longrightarrow
\text{Runtime Result}.
$$

在程式尚未執行以前，真正的 runtime result 並不是模型權重中的既定事實。

同理，科學研究中的：

$$
\text{Hypothesis}
\longrightarrow
\text{Experiment}
\longrightarrow
\text{Observation}
$$

也具有不可消除的世界交互性。

因此：

$$
\boxed{
\text{Internal reasoning cannot fully replace external causal interaction.}
}
$$

---

# 3. Agent 的核心不是拆步，而是重新取得世界

Agent 經常被描述成：

> 把大任務拆成小任務，再逐步完成。

這是對的，但不完整。

更根本的意義在於：

$$
\text{State}_t
\longrightarrow
\text{Action}_t
\longrightarrow
\text{Observation}_{t+1}
\longrightarrow
\text{State}_{t+1}.
$$

其中：

$$
\text{Observation}_{t+1}
$$

可能包含：

- 新搜尋到的網頁；
- 最新論文；
- terminal output；
- compiler error；
- API response；
- 資料庫查詢結果；
- 真實測試數據；
- 外部 Agent 的回覆；
- 人類新決策；
- 物理世界感測資訊。

因此 Agent loop 提供的不是單純更多 token，而是：

$$
\boxed{
\text{Repeated access to newly produced world information.}
}
$$

這使 AI 從：

$$
\text{Static Knowledge Processor}
$$

轉變為：

$$
\text{World-Coupled Cognitive Process}.
$$

---

# 4. 沒有 Agent 時，人類其實就是 Agent Runtime

在傳統 chatbot 工作流中，人類通常負責：

1. 決定下一步；
2. 把前一輪輸出重新貼回；
3. 執行程式；
4. 收集錯誤；
5. 搜尋資料；
6. 告知模型搜尋結果；
7. 保存狀態；
8. 選擇是否重試；
9. 判斷是否回溯；
10. 觸發下一輪。

所以真正的系統不是：

$$
\text{Chatbot}.
$$

而是：

$$
\boxed{
\text{Human Controller}
+
\text{Chatbot}.
}
$$

其工作迴路可以表示為：

$$
\text{AI}
\longrightarrow
\text{Human}
\longrightarrow
\text{World}
\longrightarrow
\text{Human}
\longrightarrow
\text{AI}.
$$

Agent 化之後，部分低風險控制工作可以改為：

$$
\text{AI}
\longrightarrow
\text{World}
\longrightarrow
\text{AI}.
$$

人類則從每一步都介入，改為只在必要節點治理：

$$
\text{Human Governance}
\longrightarrow
\text{High-Risk Gates}.
$$

因此，Agent 的經濟價值之一，是降低：

$$
\rho_H
=
\frac{
N_{\mathrm{human\ interventions}}
}{
N_{\mathrm{effective\ task\ transitions}}
}.
$$

當：

$$
\rho_H
\downarrow,
$$

同一個人類就能治理更多平行智能工作。

---

# 5. 模型知識不是世界資料庫

Foundation model 的參數可以視為某種高度壓縮的知識結構：

$$
K_{\theta}.
$$

但真實任務需要的知識至少可以拆成：

$$
K_{\mathrm{task}}
=
K_{\theta}
+
K_{\mathrm{external}}
+
K_{\mathrm{dynamic}}
+
K_{\mathrm{private}}.
$$

其中：

$$
K_{\mathrm{external}}
$$

代表論文、文件、公開資料庫、程式碼庫與其他外部知識。

$$
K_{\mathrm{dynamic}}
$$

代表現在正在變化的世界狀態。

$$
K_{\mathrm{private}}
$$

代表組織內部資料、使用者資料、專案狀態與私有歷史。

因此：

$$
\boxed{
\text{Model Weights}
\neq
\text{World State}.
}
$$

即使模型訓練時吃下極大量世界資訊，它仍面臨：

1. 世界在更新；
2. 資料存在時效性；
3. 精確資料庫查詢與參數記憶不是同一種操作；
4. 某些資訊只有在執行後才產生；
5. 私有狀態不可能全部預先存在於公開訓練語料。

所以模型能力越強，並不推出外部世界越不重要。

在許多任務中反而可能是：

$$
\boxed{
\text{Stronger Model}
\Rightarrow
\text{Higher Marginal Value of External Information}.
}
$$

因為更強的模型能更有效率地判斷什麼值得搜尋、如何驗證、如何整合矛盾資訊，以及何時需要更多證據。

---

# 6. 真正重要的不是輸出，而是累積

一次性 chatbot 可以產生：

$$
O_1,
O_2,
O_3,
\ldots,
O_n.
$$

但如果這些輸出沒有進入可持續外部狀態，它們只是：

$$
\text{disconnected outputs}.
$$

持續 Agent 則可以建立：

$$
S_0
\longrightarrow
S_1
\longrightarrow
S_2
\longrightarrow
\cdots
\longrightarrow
S_n.
$$

其中：

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

 $E_t$ 是外部新資訊， $V_t$ 是驗證結果。

這時 AI 的產出不再只是文字，而可能沉積成：

- 可搜尋資料庫；
- 知識圖譜；
- 已測試程式；
- 已驗證研究紀錄；
- 版本歷史；
- 問題與錯誤資料集；
- 來源證據鏈；
- 組織流程；
- 長期使用者狀態；
- 世界模型的更新記錄。

因此本文沿用既有時間經濟學中的「世界沉積」概念，將 Agent 的累積能力表示為：

$$
\rho_{\mathrm{commit}}
=
\frac{
V_{\mathrm{verified\ world\ commit}}
}{
\Delta t_W
}.
$$

真正值得關心的不是 Agent 在內部跑了多少 token，而是：

$$
\boxed{
\text{How much verified state entered the world?}
}
$$

---

# 7. 中上品質也可能形成巨大經濟能力

下一個重要命題是：

> AI 不需要在所有領域超越頂尖人類，才可能形成大規模經濟替代。

令任務 $j$ 的最低可接受品質為：

$$
Q_j^{\min}.
$$

某 Agent 對任務 $j$ 的平均品質為：

$$
Q_{A,j}.
$$

如果：

$$
Q_{A,j}
\ge
Q_j^{\min},
$$

並且同時滿足：

$$
P(
\text{undetected unrecoverable error}
)
\le
\epsilon_j,
$$

以及：

$$
C_{A,j}
<
C_{H,j},
$$

則該 Agent 即使不是該領域最強智能，也可能已跨過任務的經濟可用門檻。

因此：

$$
\boxed{
\text{Top-Human Quality}
\text{ is not required for every task.}
}
$$

大量組織工作真正要求的是：

- 品質達標；
- 穩定；
- 可驗收；
- 低錯誤；
- 可回溯；
- 可持續；
- 成本合理。

如果一個 Agent 每次只能產生中上品質，但可以長時間穩定累積，其總有效產出可以粗略寫成：

$$
W_A
=
Q_A
\cdot
R_A
\cdot
T_A
\cdot
P_A,
$$

其中：

- $Q_A$ 為品質；
- $R_A$ 為可靠性；
- $T_A$ 為有效工作時間；
- $P_A$ 為可利用平行度。

這個量與「單次回答是否勝過頂尖專家」是不同問題。

---

# 8. 長週期 Agent 的真正瓶頸是未檢出錯誤

若一個流程具有 $n$ 個彼此依賴的步驟，每一步成功率為：

$$
p,
$$

而任一步失敗都導致整體失敗，則理想化成功率為：

$$
P_{\mathrm{success}}
=
p^n.
$$

例如：

$$
p
=
0.99,
$$

$$
n
=
100,
$$

則：

$$
P_{\mathrm{success}}
=
0.99^{100}
\approx
0.366.
$$

所以單步正確率很高，仍然不代表長週期可靠。

但真正的 Agent 系統不應被設計成「任何錯誤都永久污染後續」。

若系統具有：

$$
\text{Detection}
+
\text{Checkpoint}
+
\text{Retry}
+
\text{Rollback}
+
\text{Cross-Verification},
$$

則更重要的量是：

$$
P(
\text{undetected and unrecoverable error}
).
$$

因此，下一代 Agent 工程的重要目標不是要求：

$$
P(
\text{any error}
)
=
0,
$$

而是壓低：

$$
\boxed{
P(
\text{error survives verification and contaminates persistent state}
).
}
$$

這個差異非常關鍵。

因為只要錯誤能被局部吸收，長週期系統就可能逐漸從「會偶爾犯錯的聊天模型」轉變成「可以長期維持有效工作狀態的自主智能單元」。

---

# 9. Token、上下文與記憶不是附屬問題

如果 Agent 持續運行，會立刻遇到三個硬限制：

$$
C_{\mathrm{token}},
$$

$$
C_{\mathrm{context}},
$$

$$
C_{\mathrm{memory}}.
$$

如果所有歷史都直接塞回上下文：

$$
L_t
\longrightarrow
\infty,
$$

則推理成本與注意力負擔都會快速上升。

因此持續智能系統不能只依賴「更長 context window」。

它必須將不同歷史分層：

$$
\text{Hot State},
$$

$$
\text{Warm Memory},
$$

$$
\text{Cold Archive},
$$

並由檢索、摘要、索引、圖關係與證據鏈決定何時重新載入。

所以：

$$
\boxed{
\text{Long Context}
\neq
\text{Long-Term Intelligence}.
}
$$

真正的長期智能依賴的是：

$$
\text{State Architecture}
+
\text{Retrieval Policy}
+
\text{Compression}
+
\text{Provenance}
+
\text{Reconstruction}.
$$

這也是為什麼下一代 AI 競爭開始不可避免地進入資料庫、記憶系統、搜尋與外部狀態管理。

---

# 10. 從模型中心競賽到系統中心競賽

過去可以將 AI 前沿粗略表示為：

$$
F_t
\approx
M_t.
$$

也就是：誰的模型最好，誰就最接近前沿。

但當 Agent、工具、搜尋、記憶、驗證與持續狀態成熟後，更合理的表示可能變成：

$$
F_t
\approx
\mathcal G_t.
$$

其中：

$$
\mathcal G_t
=
F(
M_t,
K_t,
S_t,
A_t,
V_t,
R_t,
C_t
).
$$

這不代表模型不再重要。

模型仍然是整個系統最重要的認知核心之一。

但它可能從：

$$
\text{the whole product}
$$

轉變為：

$$
\text{a replaceable cognitive component inside a larger system}.
$$

如果一個組織已經建立：

- 全球或大型專業資訊索引；
- 持續更新資料庫；
- 可信來源圖；
- Agent 歷史；
- 高品質驗證器；
- 任務執行基礎設施；
- 長期記憶；
- 世界狀態；
- 自動研究資料；

那麼它可以替換模型：

$$
M_1
\longrightarrow
M_2
\longrightarrow
M_3,
$$

而：

$$
\mathcal G
$$

的歷史資產繼續累積。

這就是模型 checkpoint 與智能工廠之間的差異。

---

# 11. 新的護城河：不是最聰明的一顆模型，而是最完整的智能生產閉環

令某個組織的智能生產閉環為：

$$
\mathfrak F_I
=
(
\mathcal D,
\mathcal M,
\mathcal A,
\mathcal V,
\mathcal S,
\mathcal C
),
$$

其中：

$$
\mathcal D
=
\text{data and world-state infrastructure},
$$

$$
\mathcal M
=
\text{models},
$$

$$
\mathcal A
=
\text{agents and action systems},
$$

$$
\mathcal V
=
\text{verification},
$$

$$
\mathcal S
=
\text{persistent state and memory},
$$

$$
\mathcal C
=
\text{compute and orchestration}.
$$

其真正競爭力可能不是某一時間點的：

$$
M_t,
$$

而是：

$$
\boxed{
\frac{
d\mathfrak F_I
}{
dt
}.
}
$$

也就是：

> 這個組織能多快地吸收新資訊、產生新經驗、驗證結果、沉積世界狀態，再把這些結果重新餵回下一代模型與系統。

因此可能形成：

$$
M_0
\longrightarrow
\mathcal G_0
\longrightarrow
D_1^{*}
\longrightarrow
M_1
\longrightarrow
\mathcal G_1
\longrightarrow
D_2^{*}
\longrightarrow
M_2
\longrightarrow
\cdots
$$

其中：

$$
D_t^{*}
$$

不是單純網路原始資料，而是系統在真實工作中產生的：

- 搜尋軌跡；
- 工具使用紀錄；
- 成功與失敗案例；
- 驗證結果；
- 修正路徑；
- 高品質任務分解；
- 世界狀態變化；
- 人機治理決策。

這類資料可能成為下一代模型極高價值的內生資料資產。

---

# 12. 系統智能的雙曲線：模型能力與整合能力

未來 AI 發展至少應分成兩條曲線：

$$
M(t)
=
\text{Model Intelligence},
$$

以及：

$$
G(t)
=
\text{Integrated System Intelligence}.
$$

傳統敘事主要關心：

$$
M(t)
\uparrow.
$$

但即使：

$$
M(t)
$$

的進步速度暫時放緩，只要：

$$
G(t)
$$

因為 Agent、搜尋、資料庫、記憶、驗證、多智能體與世界操作而快速上升，整體有效智能仍然可能高速增長。

因此，未來一個非常重要的研究問題是：

$$
\boxed{
\frac{\partial G}{\partial M}
\quad
\text{何時不再是最大的邊際項？}
}
$$

如果某個階段：

$$
\frac{\partial G}{\partial K},
\quad
\frac{\partial G}{\partial A},
\quad
\frac{\partial G}{\partial V},
\quad
\frac{\partial G}{\partial C}
$$

高於：

$$
\frac{\partial G}{\partial M},
$$

那麼繼續把絕大多數資本與人才投入「再做一顆更強模型」，就可能不再是提高整體智能的最優配置。

---

# 13. 與時間經濟學的連接：智能的價值在於單位世界時間的沉積

時間經濟學的核心不是「AI 幫人節省幾個小時」，而是：

> 在同一不可逆世界時間中，能有多少品質調整後的智能活動真正轉化成可持續世界狀態。

因此可以使用：

$$
\rho_{\mathrm{intel}}
=
\frac{
W_I^{\mathrm{quality\ adjusted}}
}{
\Delta t_W
},
$$

以及：

$$
\rho_{\mathrm{commit}}
=
\frac{
V_{\mathrm{verified\ world\ commit}}
}{
\Delta t_W
}.
$$

如果 Agent 只是大量生成文字：

$$
\rho_{\mathrm{intel}}
\uparrow,
$$

但：

$$
\rho_{\mathrm{commit}}
\approx
0,
$$

那它仍然沒有形成高價值長期生產能力。

反之，如果一個中上能力 Agent 可以穩定將工作轉成：

$$
\text{verified code},
$$

$$
\text{structured database},
$$

$$
\text{validated research},
$$

$$
\text{maintained infrastructure},
$$

那它的：

$$
\rho_{\mathrm{commit}}
$$

可能非常高。

因此真正的 Agent 經濟學問題不是：

> 一次回答比人類聰明多少？

而是：

$$
\boxed{
\text{每單位世界時間能沉積多少可驗證智能資產？}
}
$$

---

# 14. 結論：模型仍然重要，但模型已經不再足以描述智能競爭

本文不是「模型已經不重要」的論文。

相反地，模型能力仍然決定：

- 搜尋品質；
- 任務分解能力；
- 錯誤檢測能力；
- 工具使用能力；
- 抽象推理能力；
- 世界狀態理解能力。

但當模型跨過某個可用門檻後，整個 AI 發展問題開始從：

$$
\boxed{
\text{How intelligent is the model?}
}
$$

轉變成：

$$
\boxed{
\text{How much effective intelligence can the whole system realize?}
}
$$

這使未來競爭的基本單位逐漸由：

$$
M_t
$$

轉向：

$$
\mathcal G_t.
$$

因此，下一代真正重要的能力可能包括：

1. 模型能力；
2. 世界資訊取得；
3. 可追溯資料庫；
4. 持續記憶；
5. Agent loop；
6. 工具與世界操作；
7. 驗證與恢復；
8. 多智能體協作；
9. 資源配置；
10. 長期世界沉積。

當這些元件形成閉環時，AI 就不再只是「回答問題的模型」。

它開始變成：

$$
\boxed{
\text{a persistent intelligence-production system}.
}
$$

而這也導向本系列下一個問題：

> 如果一個尚未達到模型級 ASI 的系統，已經可以透過整合、並行、記憶、資訊海、Agent 與持續世界狀態，形成超過大型人類組織的有效認知能力，那麼「超級智能」究竟應該以模型定義，還是以系統定義？

這將是下一篇：

**《超級智能的整合路徑：ASI 是否可能先以系統而非模型出現》**

的核心問題。

---

## 核心命題摘要

本文提出以下可反駁命題：

### 命題一：模型能力與系統智能不可等同

$$
\boxed{
M_t
\neq
\mathcal G_t.
}
$$

### 命題二：單輪推理不能完全替代世界閉環

$$
\boxed{
\text{Internal Reasoning}
\neq
\text{External Causal Interaction}.
}
$$

### 命題三：Agent 的關鍵不是拆步，而是持續重新取得世界

$$
\boxed{
\text{Agent}
=
\text{Cognition}
+
\text{Action}
+
\text{Observation}
+
\text{State Update}.
}
$$

### 命題四：中上品質的持續 Agent 可能先跨過經濟替代門檻

$$
\boxed{
Q_A
\ge
Q_{\min}
}
$$

不要求：

$$
Q_A
=
Q_{\mathrm{elite}}.
$$

### 命題五：世界沉積比內部 token 活動更重要

$$
\boxed{
\rho_{\mathrm{commit}}
>
\text{raw token throughput}
}
$$

作為長期生產力指標更具解釋力。

### 命題六：未來 AI 競爭的基本單位可能從模型轉向閉環智能系統

$$
\boxed{
\text{Frontier Unit}
:
M_t
\longrightarrow
\mathcal G_t.
}
$$

---

## 系列接口

Paper 01 完成的工作是把：

$$
\text{Model}
$$

與：

$$
\text{Intelligent System}
$$

正式分離。

Paper 02 將進一步研究：

$$
\boxed{
ASI_{\mathrm{system}}
\not\equiv
ASI_{\mathrm{model}}
}
$$

並分析是否存在一條不同於單純 scaling 的：

$$
\boxed{
\text{Integration Path to Superintelligence}.
}
$$
