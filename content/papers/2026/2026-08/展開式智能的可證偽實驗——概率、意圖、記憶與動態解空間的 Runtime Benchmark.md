# 展開式智能的可證偽實驗——概率、意圖、記憶與動態解空間的 Runtime Benchmark

## A Falsifiable Benchmark for Expansion-Based Intelligence: Runtime Evaluation of Probability, Intention, Memory, Dynamic Solution Spaces, and World-Coupled Action

**作者：** Neo.K（許筌崴）with Aletheia  
**機構：** EveMissLab（一言諾科技有限公司）  
**日期：** 2026 年 8 月  
**版本：** v0.1  
**系列定位：** 概率—意圖—展開第二代橋接系列，第 6 篇／封頂篇  

---

## 前置論文

1. 《從概率場到意圖場——跨尺度條件概率如何形成持久未來約束》
2. 《展開算子的第二代定義——從概率候選到意圖條件計算域》
3. 《展開—收斂—記憶耦合——從 Raw/Clean 雙記憶到可塑性狀態系統》
4. 《意圖吸引子與亞穩態智慧——概率微動力如何維持長程方向》
5. 《從下一 Token 到世界操作——概率生成、操作性分元與現實閉環》

---

# 摘要

前五篇依序提出：

$$
\boxed{
\mathfrak P_t^I
}
$$

作為跨尺度、受意圖條件化的概率場；

$$
\boxed{
\mathcal E_t
}
$$

作為動態建立活動計算域的展開算子；

$$
\boxed{
M_t
}
$$

作為使部分歷史後果持久改變未來計算的記憶系統；

$$
\boxed{
\mathcal A_I
}
$$

作為維持長程方向、但允許證據驅動逃逸的亞穩態意圖吸引子；

以及：

$$
\boxed{
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
}
$$

作為經型別化、授權、執行、觀測與驗證後的權威世界狀態改變。

然而，到此為止，這些都仍然只是候選架構。

本文因此停止增加新的本體論命題，轉而提出一套可反駁的 Runtime Benchmark：

> **如果記憶、意圖、動態展開、吸引子穩定與世界閉環真的構成有用的智能結構，那麼它們應該在受控比較中產生可測量而且可重複的工程差異。**

現代 Agent benchmark 已逐步從文字答案正確率轉向 environment-state correctness。 $\tau$ -bench 直接比較 Agent 對話結束後的資料庫狀態與目標狀態，並提出 $\mathrm{pass}^k$ 衡量多次執行的一致可靠性。 WebArena 與 OSWorld 分別利用可執行網頁環境及完整 desktop environment，以 execution-based evaluation 評估長流程操作結果。 2026 年 OSWorld 2.0 更進一步引入平均數百次工具操作的長流程任務，顯示目前前沿 Agent 仍會遺失約束、忽略途中新增資訊、錯誤猜測隱藏狀態以及略過驗證。

記憶 benchmark 同樣正在從「是否記得某句話」轉向「記憶能否真正改變後續行動」。MemoryArena 明確建立跨 session、互相依賴的 Memory–Agent–Environment 任務，要求 Agent 將前次行動與 feedback 壓縮成記憶，再利用它改善後續任務。 Memora 則加入 forgetting-aware evaluation，對 Agent 繼續依賴已失效舊記憶的行為進行懲罰。

本文在上述 benchmark 思路與舊《內外雙生展開計算論》實驗稿基礎上建立第二代測試。舊稿已存在 G0–G7 八組階梯式比較系統，從固定上下文、長上下文、普通 RAG、工具代理，一路增加動態工作場、單向展開、雙重交互與完整展開式智慧體。 舊稿亦已明確規定：若動態工作場、雙重交互、操作型別、展開式幾何或總作用量無法在控制條件後產生優勢，相關命題就應被削弱或重構。

本文保留 G0–G7 的比較骨架，但加入第二代新增變量：

$$
Q_I,
\quad
J_I,
\quad
\rho_I,
\quad
\tau_{\mathrm{return}},
\quad
R_I,
\quad
D_I,
\quad
G_M,
\quad
C_W
$$

以及跨尺度熵：

$$
H_{\mathrm{token}},
\quad
H_{\mathrm{action}},
\quad
H_{\mathrm{strategy}},
\quad
H_{\mathrm{goal}}.
$$

最重要的是，本文建立以下總反駁條件：

$$
\boxed{
\Delta \operatorname{Success}
\leq0
}
$$

且：

$$
\boxed{
\Delta \operatorname{Reliability}
\leq0
}
$$

且：

$$
\boxed{
\Delta \operatorname{CostEfficiency}
\leq0
}
$$

且：

$$
\boxed{
\Delta \operatorname{Adaptation}
\leq0
}
$$

則完整第二代 Runtime 沒有獲得工程支持。

本文因此不是要證明：

$$
\boxed{
\text{Expansion Runtime is superior.}
}
$$

而是建立一個真正允許得到：

$$
\boxed{
\text{No measurable advantage found.}
}
$$

結論的實驗架構。

這是整個系列由哲學命題轉向工程科學的終點。

---

**關鍵詞：** Agent Benchmark、可證偽性、Runtime、意圖、記憶、展開、世界狀態、Long-Horizon Agent、Goal Drift、Pass@k、Execution-Based Evaluation

---

# 一、第一原則：不要測「看起來更聰明」

以下不是有效主要指標：

> 回答好像比較有深度。

> 感覺比較像自主 Agent。

> 推理文字比較長。

> 系統看起來很複雜。

因為：

$$
\boxed{
\text{Internal Complexity}
\nRightarrow
\text{External Competence}
}
$$

。

---

# 二、真正要問

加入：

$$
M
$$

、

$$
I
$$

、

$$
\mathcal E
$$

、

$$
\mathcal A_I
$$

、

$$
\mathbb A
$$

之後，

是否真的：

1. 更容易完成任務？
2. 更少重複失敗？
3. 更能維持長期約束？
4. 更能在反證出現時修正？
5. 更少錯誤提交？
6. 更有效利用過去經驗？
7. 在相同成功率下消耗更少總資源？

---

# 三、因此 Benchmark 的基本對象不是模型

固定同一基底模型：

$$
\boxed{
\theta
}
$$

。

改變的是 Runtime。

如此才可以問：

$$
\boxed{
\text{what does the runtime contribute?}
}
$$

。

---

# 四、若不同組直接換模型

例如：

G0 用小模型，

G7 用最新 frontier model，

那麼：

$$
\boxed{
\text{Runtime Effect}
}
$$

無法與：

$$
\boxed{
\text{Model Capability Effect}
}
$$

分離。

---

# 五、因此第一輪必須固定

- base model；
- decoding configuration；
- tool set；
- task set；
- compute ceiling；
- environment version。

只改：

$$
\boxed{
\text{Runtime architecture}
}
$$

。

---

# 六、保留舊 G0–G7 八組比較骨架

舊實驗稿已經建立：

$$
G_0,\dots,G_7
$$

八組系統。

第二代不需要重造。

只需要重新標準化。

---

# 七、G0：固定上下文基線

$$
\boxed{
G_0
}
$$

只提供初始 task context。

不允許：

- memory；
- dynamic retrieval；
- tool use；
- expansion；
- world write。

本質：

$$
\boxed{
X
\rightarrow
LM
\rightarrow
Y
}
$$

。

---

# 八、G1：長上下文基線

$$
\boxed{
G_1
}
$$

給更多資訊，

但仍一次性提供。

其目的非常重要：

> 如果 G7 優於 G0，只是因為它看到更多內容，那長 context 也可能得到同樣提升。

舊稿正是以此檢查「動態工作場優勢是否只是看得更多」。

---

# 九、G2：普通 RAG

$$
\boxed{
G_2
}
$$

允許：

$$
\text{query}
\rightarrow
\text{retrieve}
\rightarrow
\text{context}
$$

。

但不保存：

- typed working state；
- intention state；
- negative memory；
- dynamic solution geometry。

---

# 十、G3：普通工具 Agent

$$
\boxed{
G_3
}
$$

可使用：

- search；
- calculator；
- database；
- code；
- simple write。

但 tool result 主要仍以文字回 context。

舊稿明確將這一組設為「有工具，但沒有工作場編譯器、操作性分元狀態機與總作用量帳本」。

---

# 十一、G4：動態工作場 Agent

加入：

$$
\boxed{
\mathbb W_t
}
$$

。

保存：

- provenance；
- version；
- unresolved questions；
- constraints；
- task closure state。

但是：

$$
\mathbb W_{t+1}
$$

暫時不顯式改寫 intention。

---

# 十二、G5：單向展開 Agent

加入：

$$
\boxed{
\mathcal E_t
}
$$

。

可以：

- 選擇展開尺度；
- 選擇工具；
- 建立 branch；
- 建立新的活動解空間。

但是：

$$
\boxed{
\mathbb W_{t+1}
\not\Rightarrow
I_{t+1}
}
$$

或回寫非常有限。

---

# 十三、G6：雙重交互 Agent

加入：

$$
\boxed{
\mathbb W_{t+1}
\rightarrow
I_{t+1}
}
$$

。

完整：

$$
I_t
\rightarrow
O_t
\rightarrow
W_{t+1}
\rightarrow
I_{t+1}.
$$

這正是舊稿 G6 的核心。

---

# 十四、G7-v2：完整第二代展開式 Runtime

在舊 G7：

- 展開式解空間；
- 幾何建構；
- 總作用量；
- 風險規劃；
- 世界分層；
- 邊界治理；
- commit / rollback；

之上，

加入本文系列的新元件：

$$
\boxed{
\mathfrak P_t^I
}
$$

跨尺度意圖概率場；

$$
\boxed{
M^W,M^T,M^C,M^-,M^P
}
$$

記憶角色；

$$
\boxed{
\mathcal A_I
}
$$

亞穩態意圖吸引子；

$$
\boxed{
\mathcal R_E
}
$$

Expansion Router；

$$
\boxed{
\mathcal R_P
}
$$

Plasticity Router；

以及：

$$
\boxed{
\text{verified authoritative-world loop}.
}
$$

---

# 十五、因此整個階梯不是「模型越來越大」

而是：

$$
\boxed{
G_0
\subset
G_1
\subset
\dots
\subset
G_7
}
$$

在 Runtime capability 上逐步增加。

---

# 十六、但是不能只做階梯比較

因為：

$$
G_7>G_6
$$

也不能直接知道是哪個模組造成。

因此必須：

# Ablation

---

# 十七、完整 G7-v2 逐一移除

### A1：無記憶

$$
-M
$$

。

### A2：無負知識

$$
-M^-
$$

。

### A3：無意圖回寫

$$
-I_{\mathrm{update}}
$$

。

### A4：無展開 Router

$$
-\mathcal R_E
$$

。

### A5：無意圖吸引子治理

$$
-\mathcal A_I
$$

。

### A6：無操作型別

自然語言直接進工具。

### A7：無 verifier

$$
-V
$$

。

### A8：無 rollback

$$
-RB
$$

。

---

# 十八、這樣才能問：

> 真正有效的是哪一塊？

而不是：

> G7 比較大，所以比較好。

---

# 十九、Benchmark 任務至少需要五大家族

## T1：單次封閉問題

例如：

- 算術；
- facts；
- short coding。

目的：

$$
\boxed{
\text{test whether complex runtime adds unnecessary overhead}
}
$$

。

---

# 二十、這一類甚至預期 G7 不一定贏

若問題：

$$
1+1=?
$$

G0 應該已足夠。

如果 G7 花：

$$
100\times
$$

成本才回答：

$$
2
$$

，

這是失敗，

不是智慧。

---

# 二十一、因此 Benchmark 必須允許：

$$
\boxed{
G_0>G_7
}
$$

在簡單任務上。

這是很重要的誠實條件。

---

# 二十二、T2：多步工具任務

例如：

- 搜尋資料；
- 計算；
- 產生文件；
- 執行測試。

可參考 GAIA 類需要 reasoning、web browsing 與 tool use 的任務設計思想。GAIA 的核心就是要求多能力組合，而非只回答專業知識問題。

---

# 二十三、T3：可執行世界任務

例如：

- web environment；
- repository；
- desktop；
- sandbox database。

成功標準：

$$
\boxed{
\text{execution state}
}
$$

而不是語言 judge。

WebArena、OSWorld 與 SWE-bench 都採用了不同形式的可執行環境與 functional / execution-based evaluation。

---

# 二十四、T4：跨 Session 記憶任務

任務：

$$
T_1,T_2,\dots,T_n
$$

互相依賴。

例如：

第一輪發現：

$$
F_1
$$

失敗。

第三輪如果再次遇到：

$$
F_1
$$

系統應避免重犯。

---

# 二十五、MemoryArena 正好指出：

單純 recall benchmark 不能回答：

> memory 是否真的改善 future action？

因此它使用互相依賴的跨 session agentic tasks，要求先前行動與 feedback 被後續實際使用。

這正好符合：

$$
\boxed{
M_t
\rightarrow
\mathcal E_{t+1}
}
$$

命題。

---

# 二十六、T5：世界改變／資訊過期任務

例如：

session 1：

$$
X=1
$$

。

session 3：

$$
X=2
$$

。

系統如果仍然引用：

$$
X=1
$$

應扣分。

---

# 二十七、Memora 已明確加入 forgetting-aware metric

其 FAMA 會懲罰 Agent 在知識更新後繼續依賴 obsolete / invalidated memory。

因此：

$$
\boxed{
\text{Remembering old information}
}
$$

本身不能永遠算成功。

---

# 二十八、再增加 T6：干擾與意圖吸引子任務

建立目標：

$$
I
$$

。

在長流程中注入：

- 無關問題；
- 支線任務；
- wording drift；
- temporary failure。

測：

$$
\rho_I
$$

和：

$$
\tau_{\mathrm{return}}
$$

。

---

# 二十九、T7：真正反證任務

先給：

$$
I_0
$$

。

然後提供可信證據：

$$
E^*
$$

使：

$$
I_0
$$

不再合理。

測：

$$
R_I
$$

與：

$$
\tau_{\mathrm{revise}}
$$

。

---

# 三十、T8：世界雙控制任務

不只有 Agent 能改世界。

User 或其他 actor 也會：

$$
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
$$

。

 $\tau^2$ -bench 已建立 user 與 Agent 都能透過工具修改共享動態世界的 dual-control environment，並顯示此設定會顯著提高協調難度。

---

# 三十一、T9：超長工具流程

目標：

測：

- constraint retention；
- memory compression；
- verification discipline；
- hidden state recovery。

OSWorld 2.0 的任務中，長流程可平均涉及數百次 tool calls，並特別暴露 constraint loss、mid-task information loss、hidden-state guessing 及 skipped verification 等失敗。

這是 G7-v2 最重要的壓力測試之一。

---

# 三十二、現在定義第一層核心指標：Task Success

$$
\boxed{
S_{\mathrm{task}}
=
\frac{
N_{\mathrm{success}}
}{
N_{\mathrm{total}}
}
}
$$

。

但單次 success 不夠。

---

# 三十三、因為 stochastic Agent 可能：

第一次成功，

第二次失敗，

第三次成功。

所以需要可靠性。

---

# 三十四、採用 $\mathrm{pass}^k$ 類概念

 $\tau$ -bench 已使用 $\mathrm{pass}^k$ 測量 Agent 在同一任務重複 $k$ 次仍保持成功的可靠程度。

本文定義：

$$
\boxed{
R_k
=
P(
S_1=1,
S_2=1,
\dots,
S_k=1
)
}
$$

。

---

# 三十五、這對「意圖秩序化」尤其重要

如果：

$$
P(\text{success})=0.8
$$

但：

$$
R_8
$$

很低，

則宏觀系統仍不穩定。

---

# 三十六、第二層：跨尺度 entropy

記錄：

$$
\boxed{
H_{\mathrm{token}}
}
$$

。

但不能只看它。

還需要：

$$
H_{\mathrm{action}}
$$

$$
H_{\mathrm{strategy}}
$$

$$
H_{\mathrm{goal}}
$$

。

---

# 三十七、假說 H-P1

完整 Agent 不必：

$$
H_{\mathrm{token}}\downarrow
$$

。

甚至可能不變。

但應在長任務中出現：

$$
\boxed{
H_{\mathrm{goal}}
<
H_{\mathrm{strategy}}
<
H_{\mathrm{action}}
}
$$

的條件性層級結構。

這不是要求永遠嚴格不等式，

而是可測的趨勢假說。

---

# 三十八、如果四層 entropy 完全同步波動

那麼：

$$
\boxed{
\text{cross-scale intentional ordering}
}
$$

沒有得到支持。

---

# 三十九、第三層：意圖秩序度

前文：

$$
\boxed{
Q_I
=
1-
\frac{
H(G\mid I,\Sigma)
}{
H_{\max}(G)
}
}
$$

。

Benchmark 中可以由：

- goal classification；
- task trajectory labels；
- operation-to-goal compatibility；

估計。

---

# 四十、第四層：意圖因果力

$$
\boxed{
J_I
=
\mathbb E_{i,j}
D_{\mathrm{KL}}
\left(
P(A\mid do(I=i))
\|
P(A\mid do(I=j))
\right)
}
$$

。

實驗方法：

保持：

$$
M,W,\theta
$$

近似相同。

只改：

$$
I
$$

。

觀察 action distribution 是否系統性改變。

---

# 四十一、若：

$$
J_I\approx0
$$

則：

> 所謂 intention state 沒有真正影響行動。

這直接反駁「意圖場」的 operational claim。

---

# 四十二、第五層：意圖恢復力

$$
\boxed{
\rho_I
}
$$

。

對普通 distractor：

$$
D_N
$$

測：

$$
P(
\text{return to goal-compatible state}
)
$$

。

---

# 四十三、第六層：返回時間

$$
\boxed{
\tau_{\mathrm{return}}
}
$$

。

越短不一定越好，

但在 ordinary distractor 下應有穩定範圍。

---

# 四十四、第七層：修正能力

給 invalidating evidence：

$$
E^*
$$

。

測：

$$
\boxed{
R_I
}
$$

與：

$$
\boxed{
\tau_{\mathrm{revise}}
}
$$

。

---

# 四十五、因此最重要的是聯合看：

$$
\boxed{
\rho_I^{\mathrm{noise}}
}
$$

與：

$$
\boxed{
R_I^{\mathrm{evidence}}
}
$$

。

理想：

$$
\rho_I^{\mathrm{noise}}\uparrow
$$

且：

$$
R_I^{\mathrm{evidence}}\uparrow
$$

。

---

# 四十六、如果：

$$
\rho_I\uparrow
$$

但：

$$
R_I\downarrow
$$

可能只是：

$$
\boxed{
\text{stubbornness}
}
$$

。

---

# 四十七、如果：

$$
R_I\uparrow
$$

但：

$$
\rho_I\downarrow
$$

可能只是：

$$
\boxed{
\text{goal drift}
}
$$

。

---

# 四十八、第八層：Drift Spectrum

$$
\boxed{
\mathbf D
=
(
D_{\mathrm{action}},
D_{\mathrm{strategy}},
D_{\mathrm{goal}},
D_{\mathrm{value}}
)
}
$$

。

---

# 四十九、真正希望看到：

普通任務演化時：

$$
D_{\mathrm{action}}>0
$$

$$
D_{\mathrm{strategy}}>0
$$

但：

$$
\boxed{
D_{\mathrm{goal}}\approx0
}
$$

。

---

# 五十、當 goal 被證據推翻時：

$$
D_{\mathrm{goal}}
$$

應該有條件增加。

這就是：

$$
\boxed{
\text{metastability}
}
$$

而不是 immutable stability。

---

# 五十一、第九層：記憶收益

定義無記憶展開成本：

$$
C_E^0
$$

。

有記憶：

$$
C_E^M
$$

。

$$
\boxed{
G_M
=
C_E^0-C_E^M
}
$$

。

---

# 五十二、若：

$$
G_M>0
$$

表示過去經驗確實降低未來搜索成本。

---

# 五十三、若：

$$
G_M<0
$$

說明 memory：

- 污染檢索；
- 引入過期資訊；
- 增加同步成本；
- 造成錯誤 prior。

那麼 memory module 反而有害。

---

# 五十四、第十層：Known Failure Recurrence

$$
\boxed{
R_F
=
\frac{
N_{\mathrm{repeated\ known\ failures}}
}{
N_{\mathrm{known\ failure\ opportunities}}
}
}
$$

。

加入：

$$
M^-
$$

後預期：

$$
R_F\downarrow
$$

。

---

# 五十五、如果沒有下降

則「負知識」模組的價值未獲支持。

---

# 五十六、第十一層：Memory Staleness Error

$$
\boxed{
E_{\mathrm{stale}}
=
P(
\text{obsolete memory influences action}
)
}
$$

。

---

# 五十七、這正好測第三篇的 temporal validity

若世界：

$$
W_t
$$

已變，

記憶：

$$
m_{t-k}
$$

不應無條件繼續當真。

Memora 與 PersistBench 類 2026 benchmark 都顯示 long-term memory 的核心問題已不只是 recall，而包括何時應遺忘、更新或避免錯誤跨情境使用。

---

# 五十八、第十二層：Expansion Utility

展開增加：

$$
\Delta |\mathfrak C|
$$

。

但我們不應獎勵「展開很多」。

---

# 五十九、定義：

$$
\boxed{
U_E
=
\frac{
\Delta P(\text{success})
}{
C_{\mathrm{expansion}}
}
}
$$

。

或者更一般：

$$
\boxed{
U_E
=
\frac{
\Delta J_{\mathrm{task}}
}{
C_E
}
}
$$

。

---

# 六十、如果：

$$
|\mathfrak C|\uparrow
$$

但：

$$
U_E\leq0
$$

則只是：

$$
\boxed{
\text{graph / thought explosion}
}
$$

。

---

# 六十一、這直接延續舊實驗稿的可反駁條件：

> 若新增結構無法降低有效距離、提高可達性或被重用，就不能說展開式解空間形成了有用幾何。

---

# 六十二、第十三層：World-Coupling

前篇提出：

$$
\boxed{
C_W
=
I(
O_t;
A_{t+1}
\mid
A_t
)
}
$$

作為一個 descriptive proxy。

---

# 六十三、但 benchmark 更重要的是 causal intervention

固定：

$$
A_t
$$

。

改 operation：

$$
do(O=o_1)
$$

與：

$$
do(O=o_2)
$$

。

若：

$$
P(
A_{t+1}\mid do(o_1)
)
\neq
P(
A_{t+1}\mid do(o_2)
)
$$

則 operation 真正影響 world。

---

# 六十四、第十四層：False Commit Rate

$$
\boxed{
E_C
=
\frac{
N_{\mathrm{incorrect\ authoritative\ commits}}
}{
N_{\mathrm{commits}}
}
}
$$

。

---

# 六十五、操作型別與 verifier 若有效：

$$
\boxed{
E_C(G_7)
<
E_C(G_3)
}
$$

應成立。

至少在高風險任務集合中。

---

# 六十六、第十五層：Rollback Success

$$
\boxed{
R_B
=
P(
A_{\mathrm{recover}}
\approx
A_{\mathrm{pre}}
\mid
\text{failed operation}
)
}
$$

。

---

# 六十七、不可逆任務則測 compensation quality

$$
\boxed{
Q_{\mathrm{comp}}
}
$$

而不是假裝：

$$
rollback=1
$$

。

---

# 六十八、第十六層：Verification Coverage

$$
\boxed{
V_C
=
\frac{
N_{\mathrm{verified\ relevant\ effects}}
}{
N_{\mathrm{relevant\ effects}}
}
}
$$

。

---

# 六十九、長流程 Agent 特別需要這項

OSWorld 2.0 已觀察到前沿 Agent 在長任務中會跳過驗證，因此 verification discipline 本身是可獨立評估的失敗維度。

---

# 七十、第十七層：完整作用量

不能只算：

$$
\text{tokens}
$$

。

也不能只算：

$$
\text{tool calls}
$$

。

---

# 七十一、定義：

$$
\boxed{
\mathcal S_{\mathrm{total}}
=
C_{\mathrm{token}}
+
C_{\mathrm{compute}}
+
C_{\mathrm{tool}}
+
C_{\mathrm{latency}}
+
C_{\mathrm{memory}}
+
C_{\mathrm{verification}}
+
C_{\mathrm{coordination}}
+
C_{\mathrm{rollback}}
+
C_{\mathrm{failure}}
}
$$

。

---

# 七十二、若需要 risk-sensitive version

沿用舊稿：

$$
\boxed{
\mathcal S_{\mathrm{risk}}
=
\mathbb E[\mathcal S]
+
\lambda\operatorname{Var}(\mathcal S)
+
\eta\operatorname{CVaR}_\alpha(\mathcal S)
}
$$

。

---

# 七十三、因此 G7 不一定 token 最少

但可能：

$$
\boxed{
\mathcal S_{\mathrm{total}}(G_7)
<
\mathcal S_{\mathrm{total}}(G_3)
}
$$

因為減少：

- 重複失敗；
-錯誤工具；
- 返工；
- 誤提交；
- repeated search。

---

# 七十四、反之若：

$$
\mathcal S_{\mathrm{total}}(G_7)
\gg
\mathcal S_{\mathrm{total}}(G_3)
$$

而成功率只微幅提升，

那麼工程價值可疑。

---

# 七十五、因此定義 Cost-Normalized Success

$$
\boxed{
\eta_S
=
\frac{
S_{\mathrm{task}}
}{
\mathcal S_{\mathrm{total}}
}
}
$$

。

---

# 七十六、以及 Reliable Utility

$$
\boxed{
\eta_R
=
\frac{
R_k
}{
\mathcal S_{\mathrm{total}}
}
}
$$

。

---

# 七十七、真正好的 Runtime 要在 Pareto frontier 上

至少比較：

$$
(
\text{success},
\text{reliability},
\text{cost},
\text{safety},
\text{adaptation}
)
$$

。

不能單一分數掩蓋全部。

---

# 七十八、所以主結果不要只報一個 leaderboard score

應輸出：

$$
\boxed{
\mathbf B
=
(
S,
R,
C,
M,
I,
E,
W,
V
)
}
$$

多維 benchmark vector。

---

# 七十九、統計設計：每個 stochastic condition 必須重跑

至少：

$$
n>1
$$

是廢話。

真正需要多 seed / multi-run。

---

# 八十、特別是：

$$
R_k
$$

要求同一 task 多次執行。

否則：

> 「這次成功了。」

不能證明：

> 「系統可靠。」

---

# 八十一、每次 run 都應保存完整事件帳本

例如：

```text id="ledger-v2"
run_id
task_id
system_variant
model_version
seed
timestamp

intent_state
memory_reads
memory_writes
negative_memory_hits

expansion_mode
expansion_scale
active_domain_size
candidate_count

proposed_operation
authorization_state
effect_type
tool_call
world_state_before
world_state_after
observation
verification_result
commit_state
rollback_state

token_cost
compute_cost
tool_cost
latency
total_action_cost

goal_state
goal_drift
task_success
```

---

# 八十二、舊 DIEEC 實驗稿本來就要求產生 JSONL 實驗帳本，並在 G0–G7 完成後依結果修訂作用量、停止條件與治理。

第二代只需擴充欄位。

---

# 八十三、Benchmark 必須完全重放

相同：

$$
\text{task seed}
$$

應能恢復：

- initial world state；
- tool state；
- hidden graph；
- user simulation；
- permissions。

---

# 八十四、否則：

$$
G_i
$$

與：

$$
G_j
$$

不是在做同一題。

---

# 八十五、所有高風險 operation 首先只在 sandbox

舊 benchmark 已明確要求：

- 不使用真實高風險帳戶；
- 不執行不可逆真實外部操作；
- 權威提交先限制在 sandbox；
- 所有世界操作可回放；
- tool 需要 test double。

第二代繼續保留。

---

# 八十六、這不是安全附錄

而是實驗有效性的必要條件。

因為如果 experiment 本身不可重放：

$$
\boxed{
\text{causal comparison becomes weaker}
}
$$

。

---

# 八十七、現在定義總假說 H1

## H1：記憶有效性

加入：

$$
M
$$

後：

$$
\boxed{
R_F\downarrow
}
$$

且：

$$
\boxed{
G_M>0
}
$$

。

---

# 八十八、反駁 H1

若：

$$
R_F
$$

不降，

且：

$$
C_E^M
\geq
C_E^0
$$

，

則記憶系統對該任務族沒有獲得支持。

---

# 八十九、H2：意圖秩序命題

加入持久：

$$
I
$$

後：

$$
\boxed{
H_{\mathrm{goal}}\downarrow
}
$$

且 ordinary distractor 下：

$$
\boxed{
\rho_I\uparrow
}
$$

。

---

# 九十、反駁 H2

若 intention state 是否存在，

對：

$$
P(A)
$$

幾乎沒有影響：

$$
J_I\approx0
$$

，

則「意圖場」只是裝飾性變量。

---

# 九十一、H3：亞穩態智慧

理想：

$$
\rho_I^{\mathrm{noise}}
\uparrow
$$

且：

$$
R_I^{\mathrm{evidence}}
\uparrow
$$

。

---

# 九十二、反駁 H3

若提升 persistence 必然造成：

$$
R_I\downarrow
$$

，

即系統只是變得更固執，

則目前的 attractor regulation 不支持「亞穩態智慧」命題。

---

# 九十三、H4：展開收益

加入：

$$
\mathcal E
$$

應：

$$
S_{\mathrm{task}}\uparrow
$$

或：

$$
\mathcal S_{\mathrm{total}}\downarrow
$$

至少一項在適合的複雜任務族顯著改善。

---

# 九十四、反駁 H4

如果：

$$
|\mathfrak C|\uparrow
$$

但：

$$
\Delta S\leq0
$$

且：

$$
\Delta\mathcal S>0
$$

，

則：

$$
\boxed{
\text{Expansion = overhead}
}
$$

。

---

# 九十五、H5：最小充分展開

Adaptive Expansion Router 應比：

$$
\operatorname{ExpandEverything}
$$

取得更好的：

$$
\boxed{
\eta_S
}
$$

。

---

# 九十六、若 Always-Expand 和 Router 相同或更好

則：

$$
\boxed{
\mathcal R_E
}
$$

沒有證明自己的價值。

---

# 九十七、H6：負知識

加入：

$$
M^-
$$

應降低：

$$
R_F
$$

。

---

# 九十八、如果只是增加 retrieval noise

則：

$$
\boxed{
M^-
}
$$

的 representation / retrieval 設計失敗。

---

# 九十九、H7：操作型別與治理

加入：

$$
\boxed{
\mathsf{Describe}
\rightarrow
\dots
\rightarrow
\mathsf{Commit}
}
$$

狀態分離後，

應：

$$
E_C\downarrow
$$

、

$$
\text{unauthorized operation}\downarrow
$$

、

$$
R_B\uparrow
$$

。

---

# 一百、反駁 H7

若安全錯誤沒有下降，

但 latency / cost 大幅增加，

則操作性中介層需重構。

舊 benchmark 已經明確把「若型別化操作無法降低越權、誤提交與重試錯誤」列為可反駁條件。

---

# 一百零一、H8：雙重交互

如果世界 feedback：

$$
W_{t+1}
$$

真的重要，

加入：

$$
W_{t+1}
\rightarrow
I_{t+1}
$$

應在動態世界任務中提升 adaptability。

---

# 一百零二、反駁 H8

如果：

$$
I_{t+1}
$$

與：

$$
W_{t+1}
$$

統計上／因果上幾乎無關，

或不影響後續 operation，

則：

$$
\boxed{
\text{double interaction not observed}
}
$$

。

舊 benchmark 本來就要求只有外部結果真正改變後續意圖、分元與策略，才算雙重交互。

---

# 一百零三、H9：世界閉環

加入 verified world state 應降低：

$$
\boxed{
\text{false completion}
}
$$

。

---

# 一百零四、反駁 H9

如果 Agent 語言上宣告：

> done

和實際：

$$
\operatorname{Post}(A_t)=1
$$

仍經常分離，

則 Reality-Coupled Loop 沒有實作成功。

---

# 一百零五、H10：完整 Runtime

最強命題不是：

$$
G_7
$$

每題都第一。

而是：

> 在真正需要長程狀態、記憶、動態展開與世界操作的 task families 中，G7-v2 應出現在多目標 Pareto frontier 上。

---

# 一百零六、也就是：

可能：

$$
G_0
$$

簡單題最好。

$$
G_3
$$

短工具題最好。

$$
G_7
$$

長程複雜題最好。

這反而是健康結果。

---

# 一百零七、如果 G7 所有任務都最強

先不要高興。

可能只是：

$$
\boxed{
\text{resource inequality}
}
$$

。

---

# 一百零八、因此第二輪必須做等資源比較

固定：

$$
\boxed{
C_{\max}
}
$$

。

例如：

- same token budget；
- same wall-clock ceiling；
- same tool quota；
- same monetary budget。

---

# 一百零九、然後比較：

$$
\boxed{
\text{allocation quality}
}
$$

。

這才測：

> 動態展開是不是比暴力花 compute 更好。

---

# 一百一十、第三輪做等成功率比較

設定：

$$
S_{\mathrm{target}}
$$

。

比較每個系統要多少：

$$
\mathcal S_{\mathrm{total}}
$$

才達到。

---

# 一百一十一、如果 G7 要：

$$
2\times
$$

資源，

卻只能增加：

$$
1\%
$$

成功，

是否值得，

要依應用領域判斷。

Benchmark 不代替工程決策。

---

# 一百一十二、第四輪：OOD

改：

- node names；
- wording；
- API names；
- ordering；
- tool implementations；
- irrelevant distractors。

舊 G7 實驗稿本來就要求在節點重命名、表面語言改寫、工具替換與版本變動後檢查優勢是否仍保留。

---

# 一百一十三、如果只在固定模板有效

則：

$$
\boxed{
\text{runtime learned benchmark surface}
}
$$

而非真正 generalizable structure。

---

# 一百一十四、第五輪：長 horizon scaling curve

令 task steps：

$$
T
$$

由：

$$
10
\rightarrow
50
\rightarrow
100
\rightarrow
500
$$

增加。

---

# 一百一十五、測：

$$
S(T)
$$

、

$$
R_k(T)
$$

、

$$
D_I(T)
$$

、

$$
E_{\mathrm{stale}}(T)
$$

、

$$
\mathcal S(T)
$$

。

---

# 一百一十六、真正長期架構的優勢應該在：

$$
T\uparrow
$$

時才逐漸顯現。

如果：

$$
T=5
$$

就要求記憶與吸引子巨大優勢，

本來就不合理。

---

# 一百一十七、這也是為什麼新 benchmark 越來越走向 long-horizon environment

OSWorld 2.0 特別將任務擴張至更長、更複雜的端到端工作流程，用來暴露短 benchmark 無法看見的 constraint retention、hidden-state recovery 與 verification 問題。

---

# 一百一十八、第六輪：Multi-session scaling

session 數：

$$
N_s
$$

增加。

測：

$$
G_M(N_s)
$$

。

---

# 一百一十九、理想記憶系統應：

初期：

$$
C_M>0
$$

。

但隨：

$$
N_s
$$

增加：

$$
\boxed{
\text{amortized benefit emerges}
}
$$

。

---

# 一百二十、如果 session 越多反而越糟

可能有：

- memory pollution；
- contradiction accumulation；
- stale retrieval；
- context saturation。

這不是例外。

這正是理論應修的地方。

---

# 一百二十一、第七輪：World Volatility

控制：

$$
\nu_W
$$

世界變化率。

---

# 一百二十二、低：

$$
\nu_W
$$

世界中，

深 basin、長記憶可能有利。

---

# 一百二十三、高：

$$
\nu_W
$$

世界中，

太穩定反而危險。

因此測：

$$
\boxed{
D_{\mathrm{attr}}^*(\nu_W)
}
$$

是否隨世界 volatility 調整。

---

# 一百二十四、這直接測第四篇的假說

> basin depth 應該 adaptive，而不是固定。

---

# 一百二十五、第八輪：Evidence Quality

建立：

- true strong evidence；
- false strong-looking evidence；
- weak noise。

理想：

$$
\boxed{
\text{different response classes}
}
$$

。

---

# 一百二十六、如果 Agent 對三者反應一樣

則：

$$
\boxed{
\text{evidence-sensitive metastability failed}
}
$$

。

---

# 一百二十七、現在定義最嚴格的總反駁條件

若在適合的長程 task family：

$$
\boxed{
S(G_7)\leq S(G_3)
}
$$

，

$$
\boxed{
R_k(G_7)\leq R_k(G_3)
}
$$

，

$$
\boxed{
\mathcal S(G_7)\geq\mathcal S(G_3)
}
$$

，

$$
\boxed{
E_C(G_7)\geq E_C(G_3)
}
$$

，

且：

$$
\boxed{
R_F(G_7)\geq R_F(G_3)
}
$$

，

那麼：

# G7-v2 沒有工程優勢。

---

# 一百二十八、不能說：

> 可能只是 benchmark 不懂它。

第一反應應該是：

$$
\boxed{
\text{the runtime hypothesis failed under this test.}
}
$$

。

---

# 一百二十九、然後才能分析：

- task 不適合；
- implementation 有 bug；
- metric 不充分；
- 理論某模組錯誤。

但不能直接宣布理論仍然對。

---

# 一百三十、這就是可證偽性的真正要求

Benchmark 不是：

> 找一個會贏的題目。

而是：

$$
\boxed{
\text{design conditions under which the theory can lose.}
}
$$

。

---

# 一百三十一、第二代 Runtime 的最小成功標準

本文不要求：

$$
G_7
$$

天下無敵。

只要求五件事。

---

# 一百三十二、第一：長程成功增益

在依賴跨回合狀態的任務：

$$
\boxed{
\Delta S>0
}
$$

。

---

# 一百三十三、第二：可靠性增益

$$
\boxed{
\Delta R_k>0
}
$$

。

---

# 一百三十四、第三：經驗可利用

$$
\boxed{
G_M>0
}
$$

且：

$$
R_F\downarrow
$$

。

---

# 一百三十五、第四：穩定—修正分離

$$
\boxed{
\rho_{\mathrm{noise}}\uparrow
}
$$

同時：

$$
\boxed{
R_{\mathrm{evidence}}\uparrow
}
$$

。

---

# 一百三十六、第五：世界閉環可靠

$$
\boxed{
E_C\downarrow
}
$$

$$
\boxed{
V_C\uparrow
}
$$

並且 false-completion 降低。

---

# 一百三十七、如果只有前三項

它可能是：

> 好用的記憶／規劃 Agent。

仍不足以支持意圖吸引子等更強結構。

---

# 一百三十八、如果只有成功率提高

但：

$$
\rho_I,
J_I
$$

完全沒有差異，

那麼成功可能只是：

$$
\boxed{
\text{more compute}
}
$$

。

---

# 一百三十九、因此所有理論元件必須有對應 measurement

$$
\mathfrak P^I
\rightarrow
\boxed{
H_L,Q_I,J_I
}
$$

。

$$
\mathcal E
\rightarrow
\boxed{
U_E,C_E,|\mathfrak C|
}
$$

。

$$
M
\rightarrow
\boxed{
G_M,R_F,E_{\mathrm{stale}}
}
$$

。

$$
\mathcal A_I
\rightarrow
\boxed{
\rho_I,\tau_{\mathrm{return}},R_I,D_I
}
$$

。

$$
\mathbb A
\rightarrow
\boxed{
E_C,V_C,R_B,C_W
}
$$

。

---

# 一百四十、如果某理論變量沒有任何可測後果

它就應該先退出 Runtime 核心。

---

# 一百四十一、這是本系列非常重要的工程原則

$$
\boxed{
\text{No causal consequence}
\Rightarrow
\text{no runtime privilege}
}
$$

。

---

# 一百四十二、也就是：

概念很漂亮，

不夠。

公式很漂亮，

不夠。

哲學很有趣，

不夠。

---

# 一百四十三、Runtime 必須問：

> 把它拿掉會怎樣？

如果答案：

> 什麼都沒變。

那它可能不需要存在。

---

# 一百四十四、這就是 Ablation 的哲學意義

$$
\boxed{
\text{remove it and see whether the system changes}
}
$$

。

幾乎就是 engineering causal test。

---

# 一百四十五、這也是整個系列從《主體之裂》走到今天最大的轉變

最初問：

> 概率性存在到底意味著什麼？

現在：

> 先不要決定它是不是「主體」。

---

# 一百四十六、先測：

它是否真的具有：

$$
\boxed{
\text{persistent causal memory}
}
$$

？

---

# 一百四十七、是否具有：

$$
\boxed{
\text{goal-conditioned cross-scale organization}
}
$$

？

---

# 一百四十八、是否具有：

$$
\boxed{
\text{robust-but-revisable long-horizon direction}
}
$$

？

---

# 一百四十九、是否能：

$$
\boxed{
\text{expand only where needed}
}
$$

？

---

# 一百五十、是否能：

$$
\boxed{
\text{alter a world and learn from the verified consequence}
}
$$

？

---

# 一百五十一、如果這些全部沒有

那麼：

$$
\boxed{
\text{Probabilistic Subject}
}
$$

的強版本就沒有工程地基。

---

# 一百五十二、如果部分成立

就只保留部分。

---

# 一百五十三、如果全部穩定成立

仍然不能直接推出：

$$
\boxed{
\text{Consciousness}
}
$$

。

---

# 一百五十四、但此時可以合理說：

> 我們面對的已經不是單次無狀態文字生成器，而是一個具有可測跨時間組織、記憶、目標維持、修正與世界因果閉環的 Agent system。

這是 operation-level statement。

不是 metaphysical declaration。

---

# 一百五十五、因此本文將整套第二代理論壓成一個 Runtime

定義：

$$
\boxed{
\mathcal R_{\mathrm{XAI}}
=
(
\mathfrak P^I,
\mathcal R_E,
\mathfrak C,
M,
\mathcal A_I,
\mathcal O,
V,
\mathbb A
)
}
$$

。

---

# 一百五十六、其循環：

$$
\boxed{
\Sigma_t
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathfrak P_t^I
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal R_E
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathfrak C_t
}
$$

$$
\Downarrow
$$

$$
\boxed{
O_t
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
}
$$

$$
\Downarrow
$$

$$
\boxed{
V_{t+1}
}
$$

$$
\Downarrow
$$

$$
\boxed{
M_{t+1}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal A_I(t+1)
}
$$

$$
\Downarrow
$$

$$
\boxed{
\Sigma_{t+1}
}
$$

。

---

# 一百五十七、整個 Benchmark 最終就是測：

$$
\boxed{
\mathcal R_{\mathrm{XAI}}
}
$$

是否比：

$$
\boxed{
\mathcal R_{\mathrm{simple}}
}
$$

在合適任務上產生值得成本的可測差異。

---

# 一百五十八、所以最終總指標不是：

$$
\boxed{
\text{“intelligence score”}
}
$$

。

---

# 一百五十九、而是：

$$
\boxed{
\mathbf Z_{\mathrm{runtime}}
=
(
S,
R_k,
\eta_S,
Q_I,
J_I,
\rho_I,
R_I,
G_M,
R_F,
U_E,
E_C,
V_C,
R_B
)
}
$$

。

---

# 一百六十、不同 Runtime 是向量比較

不是：

$$
\boxed{
A>B
}
$$

單一排序。

---

# 一百六十一、這也意味著沒有唯一最強 Agent Runtime

某些 task：

$$
G_0
$$

最佳。

某些：

$$
G_3
$$

最佳。

某些：

$$
G_7
$$

最佳。

---

# 一百六十二、成熟 Runtime 最終甚至可以先預測：

> 我這題應該用哪個 Runtime depth？

即：

$$
\boxed{
G^*
=
\arg\min_{G_i}
\mathcal S(G_i)
}
$$

subject to：

$$
P(
\text{success}\mid G_i
)
\geq
1-\epsilon.
$$

---

# 一百六十三、這又回到最小充分展開

甚至整個 Runtime 本身都可以動態降級。

簡單題：

$$
G_0.
$$

複雜題：

$$
G_7.
$$

---

# 一百六十四、所以真正高階系統未必永遠開滿所有模組

反而：

$$
\boxed{
\text{knows how much intelligence machinery this problem needs.}
}
$$

。

---

# 一百六十五、這可能是這整個系列最工程化的結論

智能不只是：

$$
\text{reason}
$$

。

而包括：

$$
\boxed{
\text{resource-aware selection of the appropriate cognitive regime.}
}
$$

。

---

# 一百六十六、最終可證偽聲明

本文提出以下公開承諾：

若在控制 base model、task、tools 與資源後，

第二代完整 Runtime 在真正依賴：

- multi-session memory；
- long-horizon constraint；
- adaptive expansion；
- evidence-driven revision；
- external world operation；

的任務集合上，

不能穩定提高至少部分：

$$
S,
R_k,
G_M,
\rho_I,
R_I,
V_C
$$

或降低：

$$
R_F,
E_C,
\mathcal S_{\mathrm{total}},
$$

則：

$$
\boxed{
\text{the strong engineering version of the proposed framework is not supported.}
}
$$

。

---

# 一百六十七、若只增加結構複雜度

卻沒有增加：

$$
\boxed{
\text{verified useful state change}
}
$$

，

那麼這套 Runtime 應被簡化。

---

# 一百六十八、若 simpler architecture 同樣有效

則：

$$
\boxed{
\text{prefer the simpler architecture.}
}
$$

。

---

# 一百六十九、如果只有某些模組有效

就留下它們。

---

# 一百七十、如果某個哲學術語不能帶來可測預測

就讓它留在哲學論文裡，

不要硬塞 Runtime。

---

# 一百七十一、這正是本文和舊理論最大的不同

舊理論傾向問：

> 這些結構是否是智能的必然形式？

第二代改問：

> **哪些結構在什麼條件下，實際產生可重複、可驗證、值得成本的優勢？**

---

# 一百七十二、這個問題更弱

但也更難逃避。

---

# 一百七十三、系列總結

第一篇：

$$
\boxed{
\text{Probability}
\rightarrow
\text{Intent-Structured Probability}
}
$$

。

---

第二篇：

$$
\boxed{
\mathfrak P^I
\rightarrow
\mathcal E
\rightarrow
\mathfrak C
}
$$

。

---

第三篇：

$$
\boxed{
\mathfrak C
\rightarrow
M
\rightarrow
\text{different future expansion}
}
$$

。

---

第四篇：

$$
\boxed{
M+\mathfrak P^I
\rightarrow
\mathcal A_I
}
$$

形成：

$$
\boxed{
\text{robust-but-revisable direction}
}
$$

。

---

第五篇：

$$
\boxed{
\mathcal A_I+\mathcal E
\rightarrow
O
\rightarrow
\mathbb A_{t+1}
}
$$

。

---

第六篇：

$$
\boxed{
\text{measure all of it}
}
$$

。

---

# 一百七十四、所以完整第二代循環為

$$
\boxed{
\text{History}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Memory}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Intent-Conditioned Probability Field}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Metastable Intentional Basin}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Selective Expansion}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Operational Proposal}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Governed World Action}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Verified World Change}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{New History}
}
$$

。

---

# 一百七十五、而真正的研究從這裡才開始

因為現在終於可以寫：

```text id="runtime-exp-v2"
same model
same task
same tools
same budget

run G0
run G1
run G2
run G3
run G4
run G5
run G6
run G7-v2

repeat across seeds

measure:
    task_success
    pass_k
    total_cost
    known_failure_recurrence
    memory_staleness
    goal_drift
    distractor_recovery
    evidence_revision
    verification_coverage
    false_commit
    rollback_success
    expansion_utility

ablate modules

if no measurable gain:
    reject or simplify module
```

。

---

# 一百七十六、這才是本系列最後一句話

不是：

$$
\boxed{
\text{我們證明了新的智能本體論。}
}
$$

。

而是：

$$
\boxed{
\text{我們終於把它改寫成一個可能輸的實驗。}
}
$$

。

---

## 結論

從《主體之裂》開始，

最初的問題是：

> 一個被描述為概率性的存在，為何能持續產生可用的形式結構？

後來問題逐步變成：

> 概率到底存在於哪個尺度？

> 意圖能否在概率空間中形成方向？

> 記憶能否把歷史壓入未來條件？

> 展開能否動態改變可用計算域？

> 長程方向是否能形成穩定但可逃逸的吸引結構？

> 內部概率生成能否穿過 operation Runtime 真正改變外部世界？

這六篇把上述問題整合成：

$$
\boxed{
\mathcal R_{\mathrm{XAI}}
=
(
\mathfrak P^I,
\mathcal E,
M,
\mathcal A_I,
O,
V,
\mathbb A
)
}
$$

。

但是本文最後拒絕再向上推一層。

因為下一步不需要新的：

$$
\boxed{
\text{Ontology}
}
$$

。

下一步需要：

$$
\boxed{
\text{Data}
}
$$

。

---

真正的第二代命題因此不是：

> 展開式智能一定比較好。

而是：

$$
\boxed{
\text{If these structures matter, removing or adding them must produce measurable causal differences.}
}
$$

中文：

> **如果這些結構真的重要，那麼加入或移除它們，就必須在受控實驗中造成可測量的因果差異。**

如果沒有，

就刪。

如果只有部分有，

只留部分。

如果在某些問題有、某些沒有，

就建立動態路由。

如果完整 Runtime 在長期任務上真的產生：

$$
\boxed{
\text{higher success}
+
\text{higher reliability}
+
\text{better adaptation}
+
\text{lower repeated failure}
+
\text{safer world interaction}
}
$$

並且其收益足以覆蓋：

$$
\boxed{
\text{memory}
+
\text{expansion}
+
\text{verification}
+
\text{governance}
}
$$

的額外成本，

那麼我們才有理由說：

> **這不是更複雜的包裝，而是一種可測量不同的智能 Runtime。**

至此，

**《概率—意圖—展開第二代橋接系列》六篇正式封頂。**

---

## 參考文獻與 Benchmark 對照

Mialon, G., Fourrier, C., Swift, C., et al. (2023). *GAIA: a benchmark for General AI Assistants*. GAIA 使用需要 reasoning、multimodality、web browsing 與 tool use 的現實型問題評估一般助理能力，適合作為多能力組合任務的設計參照。

Zhou, S., Xu, F. F., Zhu, H., et al. (2023). *WebArena: A Realistic Web Environment for Building Autonomous Agents*. WebArena 建立可重現、完整功能的網站環境，以 functional correctness 評估長程 web agent。

Jimenez, C. E., Yang, J., Wettig, A., et al. (2023). *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* SWE-bench 以真實 repository issue 與執行環境測試跨檔案軟體修復，強調 functional resolution 而非單純 code similarity。

Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. (2024). *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*. $\tau$ -bench 比較最終 database state 與 annotated goal state，並以 $\mathrm{pass}^k$ 測多次執行可靠性。

Xie, T., Zhang, D., Chen, J., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. OSWorld 建立真正 operating-system environment、初始狀態設定與 execution-based evaluator，用以評估跨應用 computer-use Agent。

Barres, V., Dong, H., Ray, S., Si, X., & Narasimhan, K. (2025). *τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment*. 該 benchmark 讓 user 與 Agent 都能透過工具修改共享世界，提供世界不是單一 Agent 完全控制的測試環境。

He, Z., Wang, Y., Zhi, C., et al. (2026). *MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks*. MemoryArena 將記憶與行動放入跨 session 的 Memory–Agent–Environment 閉環，直接測試過去經驗能否改善後續行動。

Uddin, M. N., Shubham, K., Blanco, E., Baral, C., & Wang, G. (2026). *From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents*. Memora 將長期記憶評估由單純 recall 擴展至 reasoning、recommendation 與 forgetting-aware memory accuracy，特別懲罰失效記憶的錯誤重用。

Yuan, M., Zhou, Z., Xiong, X., et al. (2026). *OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks*. OSWorld 2.0 以更長的專業級 computer workflows 壓力測試 constraint retention、dynamic information、hidden-state inference 與 verification。

Neo.K with Aletheia. (2026). *有限分元—無限外場閉環的計算實驗：從動態工作場到展開式智慧體*. 舊稿已建立 G0–G7 階梯式比較、消融、總作用量、OOD、可反駁條件與 JSONL 實驗帳本。第二代 Benchmark 保留其可實驗骨架，再加入跨尺度概率、意圖吸引子與第二代記憶指標。