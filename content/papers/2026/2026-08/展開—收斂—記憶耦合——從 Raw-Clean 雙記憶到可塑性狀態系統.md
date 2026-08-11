# 展開—收斂—記憶耦合——從 Raw/Clean 雙記憶到可塑性狀態系統

## Expansion–Contraction–Memory Coupling: From Raw/Clean Dual Memory to Plastic Stateful Systems

**作者：** Neo.K（許筌崴）with Aletheia  
**機構：** EveMissLab（一言諾科技有限公司）  
**日期：** 2026 年 8 月  
**版本：** v0.1  
**系列定位：** 概率—意圖—展開第二代橋接系列，第 3 篇  
**前置論文：**  
1.《從概率場到意圖場——跨尺度條件概率如何形成持久未來約束》  
2.《展開算子的第二代定義——從概率候選到意圖條件計算域》

---

## 摘要

前文已將展開重新定義為：

$$
\boxed{
\mathcal E^{(2)}
:
(
\Sigma_t,
\mathfrak P_t^I,
M_t,
W_t,
B_t
)
\rightarrow
\mathfrak C_t
}
$$

其中 $\mathfrak C_t$ 是當前任務臨時建立的活動計算域。這立刻產生下一個問題：當 $\mathfrak C_t$ 被關閉、壓縮或替換之後，這一次展開所產生的大量中間狀態究竟應留下多少？

若只留下最後答案：

$$
\mathfrak C_t
\rightarrow
y_t
$$

則大量失敗分支、證據來源、否證理由、未採取但仍可能有價值的路徑與環境狀態都會消失。下一次遇到相似問題時，系統可能重新支付相同的搜索成本。

反之，若完整保存：

$$
\mathfrak C_0,
\mathfrak C_1,
\dots,
\mathfrak C_t
$$

中的每一個 token、工具輸出、候選、branch、simulation 與失敗軌跡，記憶成本又會隨運行時間快速膨脹，並增加檢索污染、版本衝突、過期資訊與矛盾累積。

因此：

$$
\boxed{
\text{Remember Everything}
}
$$

和：

$$
\boxed{
\text{Remember Only the Answer}
}
$$

都是極端。

Neo.K 早期《雙記憶體認知超導》曾以 Raw Memory 與 Clean Memory 處理此張力：Raw 側保存完整探索軌跡，Clean 側保存收斂模式，並特別指出「失敗不是垃圾，而是邊界知識」；同時提出若只保存收斂結果，後續展開可能喪失多樣性種子。 該稿進一步將展開 $E_\theta$ 與收斂 $V_\phi$ 分別映射到 Raw 與 Clean 記憶角色。

然而，後續 Agent Memory Kernel 已主動修正早期理論，不再將「兩個物理記憶體」「固定 Raw/Clean 容量比例」或量子式記憶類比視為必然結論，而保留較穩健的工程洞察：上下文不等於持久記憶、反覆壓縮可能漂移、失敗與撤銷記錄具有負知識價值、來源／角色／版本不可被無標記混合。

本文沿此修正，提出「**記憶角色分解框架**」（Memory-Role Decomposition Framework）。記憶不再首先依物理存放位置分類，而依它在未來計算中的功能分類：

$$
\boxed{
M_t
=
(
M_t^{W},
M_t^{T},
M_t^{C},
M_t^{-},
M_t^{P}
)
}
$$

其中：

- $M^W$ ：Working / active memory；
- $M^T$ ：Trajectory memory；
- $M^C$ ：Consolidated memory；
- $M^-$ ：Negative / boundary memory；
- $M^P$ ：Provenance / governance memory。

同一資料庫可以同時實現五種角色，五種角色也可以分散於多個不同儲存介質。

Continual-learning 文獻長期研究相同的 stability–plasticity 張力。1995 年 Complementary Learning Systems 理論以快速 episodic learning 與較慢整合式 learning 的不同角色解釋新經驗吸收與既有結構維護之間的需求。([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/7624455/)) Experience Replay、Deep Generative Replay 與 Elastic Weight Consolidation 則分別展示保存／重播過去經驗、生成式重播以及限制重要參數變化等不同抗遺忘路徑。

2026 年 Agentic Memory 更進一步把 store、retrieve、update、summarize、discard 直接建成 agent 可以學習選擇的 actions，而不是固定記憶管線。 MOSAIC 等近期長期記憶架構則明確處理 relational structure、temporal reasoning 與 contradiction detection；TrustMem 則直接指出錯誤的 memory update 會把一次生成錯誤升級成持久系統狀態錯誤，因此需要驗證 memory transition 本身。

本文因此提出：

$$
\boxed{
\text{Memory}
\neq
\text{storage}
}
$$

而更一般：

$$
\boxed{
\text{Memory}
=
\text{persistent control over future computation through selected consequences of the past.}
}
$$

中文：

> **記憶不是把過去保存起來，而是選擇哪些過去後果有資格持續改變未來計算。**

---

**關鍵詞：** 記憶、展開、收斂、Continual Learning、Stability–Plasticity、Negative Knowledge、Agent Memory、Experience Replay、記憶鞏固、動態智能

---

# 一、真正困難的不是「有沒有記憶」

而是：

> **什麼值得變成記憶？**

展開：

$$
\mathcal E_t
$$

可能產生：

$$
10,
100,
1000
$$

甚至更多中間事件。

例如：

$$
\mathfrak C_t
=
\{
z_1,z_2,\dots,z_n
\}
$$

。

最後只有：

$$
z^*
$$

被採用。

那其他：

$$
z_i
$$

怎麼辦？

---

# 二、最極端的方法：全部刪掉

$$
M_{t+1}
=
M_t
\cup
\{z^*\}
$$

。

這很省記憶體。

但可能造成：

$$
\boxed{
\text{repeated search}
}
$$

。

因為系統不知道：

> 為什麼 $z_4$ 上次已經被否決？

---

# 三、例如程式修復

候選：

$$
p_1,p_2,p_3,p_4
$$

。

結果：

$$
p_1
\rightarrow
\text{compile failure}
$$

$$
p_2
\rightarrow
\text{test failure}
$$

$$
p_3
\rightarrow
\text{security regression}
$$

$$
p_4
\rightarrow
\text{success}
$$

。

如果最後只保存：

$$
p_4
$$

下一次相似情境又可能重新生成：

$$
p_1,p_2,p_3
$$

。

---

# 四、因此失敗也具有資訊

失敗：

$$
f_i
$$

至少告訴系統：

$$
\boxed{
\text{Do not search here again under similar conditions.}
}
$$

。

可以表示成：

$$
\Omega_{t+1}
=
\Omega_t
\setminus
\mathcal F_i
$$

其中：

$$
\mathcal F_i
$$

是由失敗暴露出的無效區域。

---

# 五、這就是早期「Failure Landscape」真正值得保留的部分

舊《雙記憶體認知超導》提出：

> 失敗不是垃圾，而是邊界知識。

並主張失敗應留下足以避免再次探索相同無效區域的資訊。

第二代不再要求：

> 保存全部失敗原始軌跡。

而改成：

$$
\boxed{
\text{preserve the reusable boundary information contained in failure.}
}
$$

。

---

# 六、所以「保存失敗」和「保存完整失敗紀錄」不是同一件事

例如原始失敗：

$$
T_f
=
50000\text{ tokens}
$$

。

真正可以重用的 constraint 可能只有：

$$
C_f
=
\text{API version < 3.2 incompatible}
$$

。

因此：

$$
\boxed{
C_f
\ll
T_f
}
$$

。

---

# 七、這就是負知識壓縮

定義：

$$
\boxed{
\mathcal K^{-}
:
T_f
\rightarrow
C_f
}
$$

。

其中：

$$
C_f
$$

應保留：

- 失敗條件；
- 失敗原因；
- 適用範圍；
- 版本；
- 是否可重試；
- 何種變化會使結論失效。

---

# 八、所以負知識不能只是：

```text
failed
```

。

而應：

```text
candidate: X
failure_type: dependency_conflict
condition: package_A < 3.2
evidence: compiler error Y
valid_since: version Z
retest_if: dependency changes
```

。

---

# 九、這開始顯示記憶其實是一個 typed state system

本文不再使用：

$$
M
=
\{\text{text chunks}\}
$$

。

更一般：

$$
\boxed{
m_i
=
(
c_i,
\tau_i,
t_i,
s_i,
v_i,
p_i,
q_i
)
}
$$

其中：

- $c_i$ ：content；
- $\tau_i$ ：memory type；
- $t_i$ ：time；
- $s_i$ ：source；
- $v_i$ ：version；
- $p_i$ ：provenance；
- $q_i$ ：confidence / validation status。

---

# 十、因此同一句話在不同記憶型別下完全不同

例如：

> library X 不支援 feature Y。

如果：

$$
\tau=\text{hypothesis}
$$

和：

$$
\tau=\text{verified failure}
$$

不是同一回事。

如果：

$$
v=1.0
$$

和：

$$
v=4.0
$$

也不是同一回事。

---

# 十一、所以第二代記憶不能只靠 semantic similarity

因為：

$$
\boxed{
\text{similar wording}
\nRightarrow
\text{same epistemic status}
}
$$

。

這也是 provenance memory 必須獨立存在的理由。

---

# 十二、本文提出五種基本記憶角色

$$
\boxed{
M_t
=
(
M_t^W,
M_t^T,
M_t^C,
M_t^-,
M_t^P
)
}
$$

。

---

# 十三、第一種：Working Memory

$$
M^W
$$

。

保存：

> 本輪活動計算所需的短期狀態。

包括：

- current problem；
- active hypotheses；
- current plan；
- tool outputs；
- unresolved variables。

---

# 十四、Working Memory 主要追求：

$$
\boxed{
\text{low latency}
}
$$

而不是：

$$
\boxed{
\text{long-term persistence}
}
$$

。

當任務結束，

大部分：

$$
M^W
$$

應該消失。

---

# 十五、第二種：Trajectory Memory

$$
M^T
$$

。

保存：

$$
\boxed{
\text{how we got here}
}
$$

。

例如：

- 搜索路徑；
- reasoning branch；
- tool sequence；
- intermediate state；
- decision trace。

---

# 十六、Trajectory Memory 的價值不是每次都直接讀

它主要支援：

- debugging；
- re-expansion；
- audit；
- causal analysis；
- alternative reconstruction。

---

# 十七、第三種：Consolidated Memory

$$
M^C
$$

。

保存：

$$
\boxed{
\text{reusable compressed structure}
}
$$

。

例如：

- 已驗證規則；
- 成功模式；
- 穩定摘要；
- reusable procedure；
- validated preference。

---

# 十八、第四種：Negative Memory

$$
M^-
$$

。

保存：

- failure boundaries；
- counterexamples；
- invalid paths；
- revoked conclusions；
- conflict conditions。

因此：

$$
\boxed{
M^-
\neq
M^C
}
$$

。

兩者都可能是高價值知識。

---

# 十九、第五種：Provenance Memory

$$
M^P
$$

。

保存：

- 誰提供；
- 何時獲得；
- 從哪個工具；
- 哪個版本；
- 是否驗證；
- 權限範圍；
- 是否已過期。

---

# 二十、這五種角色不等於五個資料庫

這是第二代與舊雙記憶理論最大的修正。

完全可以：

$$
\boxed{
\text{one physical store}
}
$$

承載：

$$
M^W,M^T,M^C,M^-,M^P
$$

。

也可以五種角色分布在：

- context；
- vector DB；
- graph DB；
- event log；
- model weights。

---

# 二十一、因此：

$$
\boxed{
\text{logical memory roles}
\neq
\text{physical memory partitions}
}
$$

。

---

# 二十二、舊理論真正猜對的是「角色分離」

早期 Raw / Clean 二分實際抓到的是：

$$
\boxed{
\text{high-fidelity exploration history}
}
$$

和：

$$
\boxed{
\text{compressed reusable knowledge}
}
$$

不能完全使用相同保存策略。

這個核心仍然成立。

但：

$$
\boxed{
2
}
$$

不是神聖數字。

---

# 二十三、甚至可以完全連續化

定義 memory fidelity：

$$
f_i\in[0,1]
$$

。

其中：

$$
f_i=1
$$

表示近乎完整原始保真。

$$
f_i\rightarrow0
$$

表示高度壓縮。

因此：

$$
\boxed{
M
=
\{(m_i,f_i)\}
}
$$

。

---

# 二十四、這比 Raw/Clean 二值更一般

Raw：

$$
f\approx1
$$

。

Clean：

$$
f\ll1
$$

但：

$$
f>0
$$

。

中間還可以有：

$$
0<f<1
$$

大量層級。

---

# 二十五、例如一篇論文研究過程

第一層：

$$
f=1
$$

保存：

> 原始 PDF、完整 experiment logs。

第二層：

$$
f=0.7
$$

保存：

> extract、annotations、主要表格。

第三層：

$$
f=0.3
$$

保存：

> structured summary。

第四層：

$$
f=0.05
$$

保存：

> 「核心結論＋引用地址」。

---

# 二十六、因此真正問題變成：

$$
\boxed{
\text{What fidelity should each consequence of expansion retain?}
}
$$

而不是：

> Raw 還是 Clean？

---

# 二十七、這可以寫成 memory allocation problem

每個事件：

$$
e_i
$$

具有：

$$
V_i
=
\text{future expected value}
$$

。

保存成本：

$$
C_i(f_i)
$$

。

未來重新取得成本：

$$
R_i(f_i)
$$

。

遺忘風險：

$$
F_i(f_i)
$$

。

---

# 二十八、因此選：

$$
\boxed{
f_i^*
=
\arg\max_{f_i}
\left[
V_i
-
\lambda C_i(f_i)
-
\mu R_i(f_i)
-
\nu F_i(f_i)
\right]
}
$$

。

這是工作性形式，

不是已被證明的唯一 memory law。

---

# 二十九、也就是：

> 重要、昂貴、難重建的東西，高保真保存。

> 低價值、容易重建的東西，高度壓縮甚至丟棄。

---

# 三十、這正是「可塑性狀態系統」

因為：

$$
M_t
$$

不是靜態 archive。

它本身持續：

$$
\boxed{
\text{write}
\rightarrow
\text{consolidate}
\rightarrow
\text{revise}
\rightarrow
\text{forget}
}
$$

。

---

# 三十一、2026 年 Agentic Memory 已經非常接近這個方向

AgeMem 將：

- store；
- retrieve；
- update；
- summarize；
- discard；

直接變成 agent policy 可以選擇的 memory actions，而非由固定 heuristics 決定。

因此：

$$
\boxed{
\text{Memory Management}
}
$$

開始成為：

$$
\boxed{
\text{Agent Policy}
}
$$

的一部分。

---

# 三十二、這意味「忘記」本身可以是一種智能行為

如果永遠：

$$
\operatorname{Delete}=0
$$

則：

$$
|M_t|
\rightarrow\infty
$$

。

最終：

- retrieval noise 增加；
- stale facts 增加；
- contradictions 增加；
- maintenance cost 增加。

所以：

$$
\boxed{
\text{forgetting}
}
$$

不必是 failure。

---

# 三十三、真正失敗的是「無治理遺忘」

例如：

$$
\boxed{
\text{forget verified constraint}
}
$$

可能很糟。

但：

$$
\boxed{
\text{forget disposable intermediate wording}
}
$$

非常合理。

因此：

$$
\boxed{
\text{Selective Forgetting}
}
$$

也是智能。

---

# 三十四、這和 continual learning 的 Stability–Plasticity 問題直接接合

Continual learning 要同時做到：

$$
\boxed{
\text{Stability}
=
\text{preserve useful old structure}
}
$$

以及：

$$
\boxed{
\text{Plasticity}
=
\text{learn new structure}
}
$$

。

CLEAR 等 experience-replay 方法利用過去經驗重播來減少 catastrophic forgetting，同時保留新資料的 online learning，以平衡 stability 與 plasticity。

---

# 三十五、而 2025 年研究仍顯示 plasticity loss 本身沒有消失

持續處理 non-stationary data 的神經網路可能逐步失去快速吸收新資訊的能力；2025 年 Lifelong Learning Agents 工作以 regenerative regularization 等方式嘗試維持 plasticity。

另有 ICML 2025 工作直接從 architecture 層重新研究 stability–plasticity trade-off，發現不同架構特性可以偏向 stability 或 plasticity，並提出 dual-architecture framework。

因此：

$$
\boxed{
\text{remembering more}
\nRightarrow
\text{learning better forever}
}
$$

。

---

# 三十六、這與舊雙記憶理論的那個悖論其實完全一致

舊稿曾問：

> 如果系統已經完美收斂，它還怎麼學新東西？

並指出：

$$
\gamma_V\rightarrow1
$$

而：

$$
\alpha_E\rightarrow0
$$

可能造成僵化。

第二代可以把這個問題去掉舊術語後重新寫成：

$$
\boxed{
\text{Perfect consolidation}
\rightarrow
\text{plasticity risk}
}
$$

。

---

# 三十七、因此記憶不能只有「保存得好不好」

還要問：

$$
\boxed{
\text{Does memory leave room for future revision?}
}
$$

。

---

# 三十八、這就需要 Memory Revisability

令：

$$
r_i
$$

表示 memory entry 可修正性。

已形式驗證的數學定理：

$$
r_i
$$

可能很低。

使用者昨天的偏好：

$$
r_i
$$

應該較高。

一次不可靠推論：

$$
r_i
$$

更高。

---

# 三十九、所以記憶至少需要兩個不同維度

$$
\boxed{
(f_i,r_i)
}
$$

。

其中：

$$
f_i
=
\text{fidelity}
$$

。

$$
r_i
=
\text{revisability}
$$

。

---

# 四十、高保真不等於不可修改

完整 log：

$$
f=1
$$

但可以標記：

$$
\text{obsolete}
$$

。

而高度壓縮的核心規則：

$$
f=0.1
$$

可能具有：

$$
r\approx0
$$

如果已經被充分驗證。

因此兩軸必須分開。

---

# 四十一、再加入 confidence

$$
q_i
\in[0,1]
$$

。

得到：

$$
\boxed{
m_i
=
(c_i,f_i,r_i,q_i)
}
$$

。

---

# 四十二、再加入 provenance

$$
p_i
$$

。

於是：

$$
\boxed{
m_i
=
(
c_i,
f_i,
r_i,
q_i,
p_i,
t_i,
v_i
)
}
$$

。

這才開始接近可治理持久記憶。

---

# 四十三、為什麼 provenance 很重要？

因為：

> 「A 說 X」

和：

> 「系統驗證 X」

不能在壓縮後都變成：

> X。

否則：

$$
\boxed{
\text{source projection}
\rightarrow
\text{epistemic corruption}
}
$$

。

---

# 四十四、MOSAIC 類近期記憶研究正是因為遇到這類問題

MOSAIC 指出 flat memory storage 會失去 relational context，並加入 entity-typed graph、temporal relations 與 save-time conflict detection，以減少矛盾資訊持續累積。

因此：

$$
\boxed{
\text{Memory quality}
\neq
\text{retrieval similarity alone}
}
$$

。

---

# 四十五、而 memory write 本身也可能幻覺

這是一個極容易被忽略的問題。

假設一次模型回答錯：

$$
e_t
$$

。

若只存在當次 response：

危害是：

$$
O(1)
$$

。

但若：

$$
e_t
\rightarrow
M_{t+1}
$$

而未來每輪都檢索：

$$
M_{t+1}
$$

則：

$$
e_t
$$

升級成：

$$
\boxed{
\text{persistent state error}
}
$$

。

---

# 四十六、TrustMem 正面處理這個問題

2026 年 TrustMem 指出 memory agents 的 write、revise、delete transition 本身可能漏失資訊、破壞已有內容或加入 unsupported content，因此加入 Memory Transition Verifier，檢查 coverage、preservation 與 faithfulness。

這給本文一個極重要原則：

$$
\boxed{
\text{Memory transition itself must be verifiable.}
}
$$

---

# 四十七、因此不能只有 Output Verifier

還需要：

$$
\boxed{
V_M:
(
M_t,
\Delta M_t
)
\rightarrow
\{
0,1,\text{uncertain}
\}
}
$$

。

---

# 四十八、也就是：

生成答案：

$$
V_Y
$$

驗證。

工具操作：

$$
V_A
$$

驗證。

記憶更新：

$$
V_M
$$

也必須驗證。

---

# 四十九、這使 agent 閉環變成：

$$
\boxed{
\text{Act}
\rightarrow
\text{Observe}
\rightarrow
\text{Interpret}
\rightarrow
\text{Propose Memory Update}
\rightarrow
\text{Verify Memory Update}
\rightarrow
\text{Commit}
}
$$

。

---

# 五十、這很像 database transaction

記憶更新不應直接：

$$
M_t
\rightarrow
M_{t+1}
$$

。

而應：

$$
M_t
\rightarrow
\tilde M_{t+1}
$$

建立 candidate。

再：

$$
V_M(
M_t,\tilde M_{t+1}
)
$$

。

成功才：

$$
\boxed{
M_{t+1}
=
\operatorname{Commit}(
\tilde M_{t+1}
)
}
$$

。

---

# 五十一、失敗則：

$$
\boxed{
\operatorname{Rollback}
}
$$

。

這會讓 Agent Memory 真正具有：

$$
\boxed{
\text{state transition integrity}
}
$$

。

---

# 五十二、所以記憶已經不是資料庫旁邊一個小功能

而是：

$$
\boxed{
\text{part of the agent's state-transition semantics}
}
$$

。

---

# 五十三、現在回到 neural continual learning

External memory 只是其中一種持久化方式。

另一種是：

$$
\boxed{
\theta_t
\rightarrow
\theta_{t+1}
}
$$

。

即把經驗壓入參數。

---

# 五十四、但參數式記憶又有 interference

Sequential training：

$$
\theta_A
\rightarrow
\theta_{A+B}
$$

可能造成：

$$
\operatorname{Performance}(A)\downarrow
$$

。

這就是 catastrophic forgetting 的典型問題。

Elastic Weight Consolidation 的策略不是保存全部舊資料，而是識別對舊任務重要的參數，限制它們在學習新任務時被大幅修改。

---

# 五十五、所以「保存過去」至少有三條不同路徑

### 路徑一：Explicit Replay

$$
D_{\mathrm{past}}
\rightarrow
\text{replay}
$$

。

### 路徑二：Generated Replay

$$
G_{\mathrm{past}}
\rightarrow
\tilde D_{\mathrm{past}}
$$

再重播。

Deep Generative Replay 正是以生成舊資料樣本來降低完整保存過去資料的需求。

### 路徑三：Parameter Constraint

$$
\theta
$$

本身保留。

EWC 為例。

---

# 五十六、因此記憶甚至不應限定在「可檢索文字」

更一般：

$$
\boxed{
M_t
=
M_{\mathrm{explicit}}
\oplus
M_{\mathrm{parametric}}
\oplus
M_{\mathrm{state}}
}
$$

。

---

# 五十七、其中

$$
M_{\mathrm{explicit}}
$$

：

可檢索事件／文件／知識。

$$
M_{\mathrm{parametric}}
$$

：

模型參數中的學得結構。

$$
M_{\mathrm{state}}
$$

：

當下持續 runtime state。

---

# 五十八、三者更新速度也不同

$$
\tau_W
<
\tau_T
<
\tau_C
$$

可能是典型情況。

Working state：

秒／分鐘。

Trajectory：

任務／session。

Consolidated：

長時間。

Parameters：

更慢或由特定 update cycle 控制。

---

# 五十九、這與 Complementary Learning Systems 有重要結構類似

1995 年 McClelland、McNaughton 與 O'Reilly 提出 hippocampal 與 neocortical complementary learning systems 的模型，核心正是快速學習個別 episode 與較慢整合既有統計結構之間的角色差異。

本文不主張：

> AI 必須複製 hippocampus–neocortex。

而只取其一般性教訓：

$$
\boxed{
\text{different learning timescales may require different information-handling regimes.}
}
$$

。

---

# 六十、所以雙記憶真正應該升級成「多時間尺度記憶」

$$
\boxed{
M(t)
=
\{
M^{(\tau_1)},
M^{(\tau_2)},
\dots,
M^{(\tau_n)}
\}
}
$$

。

不同：

$$
\tau_i
$$

具有不同：

- fidelity；
- access frequency；
- consolidation；
- revision；
- forgetting policy。

---

# 六十一、這比固定 Raw/Clean 更一般

Raw/Clean 可以重新理解成兩個端點：

$$
\boxed{
\text{high-fidelity / high-plasticity}
}
$$

到：

$$
\boxed{
\text{compressed / high-stability}
}
$$

。

中間是一整條光譜。

---

# 六十二、因此本文提出「記憶相空間」

令：

$$
m
$$

的座標為：

$$
\boxed{
m
=
(
f,r,q,\tau,u
)
}
$$

。

其中：

- $f$ ：fidelity；
- $r$ ：revisability；
- $q$ ：confidence；
- $\tau$ ：expected lifetime；
- $u$ ：future utility。

---

# 六十三、記憶會在相空間裡移動

新事件：

$$
m_0
$$

可能：

$$
f\approx1
$$

$$
q\approx0.5
$$

$$
r\approx1
$$

。

經驗證後：

$$
q\uparrow
$$

。

經多次重用後：

$$
u\uparrow
$$

。

經 consolidation：

$$
f\downarrow
$$

。

---

# 六十四、如果後來被否證

$$
q\downarrow
$$

但不一定：

$$
\operatorname{Delete}(m)
$$

。

可能轉入：

$$
M^-
$$

。

即：

$$
\boxed{
\text{positive knowledge}
\rightarrow
\text{negative historical knowledge}
}
$$

。

---

# 六十五、例如：

舊記憶：

> API X 不支援 function Y。

新版發布後：

這句不再是真。

不能簡單刪掉。

因為它仍然可以解釋：

> 為什麼舊版本程式那樣寫？

所以：

$$
\boxed{
\text{false-now}
\neq
\text{historically useless}
}
$$

。

---

# 六十六、這就是 temporal validity

定義：

$$
\boxed{
\operatorname{Valid}(m,t)
}
$$

。

一條記憶可以：

$$
\operatorname{Valid}(m,t_1)=1
$$

但：

$$
\operatorname{Valid}(m,t_2)=0
$$

。

因此不能只存：

$$
m
$$

。

還要存：

$$
\boxed{
(m,[t_a,t_b])
}
$$

。

---

# 六十七、這會大幅降低「舊真相污染新狀態」

對持續 Agent 非常重要。

世界會變。

所以：

$$
\boxed{
\text{Memory}
}
$$

不是 truth archive。

更準確：

$$
\boxed{
\text{Memory is a time-indexed record of knowledge states and their evidential status.}
}
$$

。

---

# 六十八、現在可以定義展開—收斂—記憶三耦合

展開：

$$
\boxed{
\mathcal E:
S_t
\rightarrow
\mathfrak C_t
}
$$

。

收斂：

$$
\boxed{
\mathcal V:
\mathfrak C_t
\rightarrow
S_{t+1}
}
$$

。

記憶：

$$
\boxed{
\mathcal M:
(
\mathfrak C_t,
S_{t+1}
)
\rightarrow
M_{t+1}
}
$$

。

---

# 六十九、但三者不是線性

因為：

$$
M_t
$$

會反過來影響：

$$
\mathcal E_t
$$

。

因此：

$$
\boxed{
M_t
\rightarrow
\mathcal E_t
\rightarrow
\mathfrak C_t
\rightarrow
\mathcal V_t
\rightarrow
M_{t+1}
}
$$

。

---

# 七十、完整形式：

$$
\boxed{
\mathfrak C_t
=
\mathcal E(
\Sigma_t,
\mathfrak P_t^I,
M_t
)
}
$$

$$
\boxed{
S_{t+1}
=
\mathcal V(
\mathfrak C_t,
I_t
)
}
$$

$$
\boxed{
M_{t+1}
=
\mathcal M(
M_t,
\mathfrak C_t,
S_{t+1},
O_{t+1}
)
}
$$

。

---

# 七十一、因此記憶會直接改變下一輪解空間

$$
M_{t+1}
\neq M_t
$$

推出：

$$
\mathfrak P_{t+1}^{I}
\neq
\mathfrak P_t^I
$$

進一步：

$$
\boxed{
\mathfrak C_{t+1}
\neq
\mathfrak C_t
}
$$

可能成立。

---

# 七十二、這才是真正的「經驗」

如果一個系統完成一件事之後，

下一次完全不因此不同，

那麼：

$$
\boxed{
\text{experience did not become persistent state}
}
$$

。

---

# 七十三、所以可以給出一個操作性學習定義

若：

$$
E_t
$$

發生後：

$$
P(
A_{t+k}
\mid
E_t,\Sigma_{t+k}
)
$$

與未發生：

$$
E_t
$$

的 counterfactual 分布不同，

並且差異跨時間保持，

則：

$$
E_t
$$

已留下 learning consequence。

---

# 七十四、也就是：

$$
\boxed{
\text{Learning}
=
\text{persistent alteration of future state-generation conditions}
}
$$

。

這再次與上一系列第三篇接合。

---

# 七十五、但持久改變不代表永不改變

如果：

$$
M
$$

一旦寫入永遠不可修訂，

則：

$$
\boxed{
\text{persistence}
\rightarrow
\text{rigidity}
}
$$

。

因此成熟記憶必須：

$$
\boxed{
\text{persistent}
+
\text{revisable}
}
$$

。

這和成熟 intention 的要求完全一致。

---

# 七十六、記憶與意圖其實具有同樣的 Stability–Plasticity 張力

意圖：

$$
\text{Persistence}
\rightleftarrows
\text{Revisability}
$$

。

記憶：

$$
\text{Retention}
\rightleftarrows
\text{Updateability}
$$

。

模型：

$$
\text{Stability}
\rightleftarrows
\text{Plasticity}
$$

。

---

# 七十七、三者可能是同一種元問題

本文提出：

$$
\boxed{
\text{Persistent Intelligence}
=
\text{Stability–Plasticity Regulation Across State Types}
}
$$

。

不是只有 weights 有 stability–plasticity。

Goal、memory、policy、world model 都有。

---

# 七十八、所以可以定義廣義可塑性向量

$$
\boxed{
\mathbf P_t
=
(
P_\theta,
P_M,
P_I,
P_\pi,
P_W
)
}
$$

。

分別表示：

- model plasticity；
- memory plasticity；
- intention plasticity；
- policy plasticity；
- world-model plasticity。

---

# 七十九、一個成熟 Agent 不是所有 $P$ 都最大

如果：

$$
P_I\gg1
$$

意圖每秒變：

agent 漂移。

如果：

$$
P_M=0
$$

記憶永不改：

agent 僵化。

如果：

$$
P_\theta\gg1
$$

模型每次 interaction 都大幅改：

可能 catastrophic drift。

---

# 八十、所以真正問題是「可塑性路由」

哪一層應該改？

若只是一筆事實更新：

$$
\boxed{
P_M
}
$$

啟動即可。

如果新技能：

可能：

$$
P_\pi
$$

或：

$$
P_\theta
$$

需要更新。

如果原任務錯了：

$$
P_I
$$

需要啟動。

---

# 八十一、這與上一篇 Scale-Directed Expansion 高度對稱

上一篇：

> 現在該在哪個尺度展開？

本篇：

> 現在該在哪個狀態層修改？

因此：

$$
\boxed{
\text{Expansion Routing}
}
$$

與：

$$
\boxed{
\text{Plasticity Routing}
}
$$

可能成為同一 Runtime 的兩個控制器。

---

# 八十二、本文提出 Plasticity Router

$$
\boxed{
\mathcal R_P:
E_t
\rightarrow
(
\Delta\theta,
\Delta M,
\Delta I,
\Delta\pi,
\Delta W
)
}
$$

。

它判定：

> 這次新資訊到底應該改哪裡？

---

# 八十三、例如使用者說：

> 我明天不開會了。

不應：

$$
\Delta\theta
$$

。

而應：

$$
\Delta M
$$

或外部 calendar state。

---

# 八十四、如果發現：

> 目前整個解題策略在某一類問題反覆失敗。

可能：

$$
\Delta\pi
$$

。

---

# 八十五、如果發現：

> 長期目標本身已不成立。

才：

$$
\Delta I
$$

。

---

# 八十六、因此「什麼都 Fine-tune」和「什麼都塞向量資料庫」都是過度簡化

前者：

$$
\boxed{
\text{all learning}
\rightarrow
\theta
}
$$

。

後者：

$$
\boxed{
\text{all learning}
\rightarrow
M_{\mathrm{external}}
}
$$

。

第二代架構應是：

$$
\boxed{
\text{event}
\rightarrow
\text{state-type selection}
\rightarrow
\text{appropriate persistence channel}
}
$$

。

---

# 八十七、這可以大幅降低不必要更新成本

如果資訊只需：

$$
M
$$

改，

就不用：

$$
\theta
$$

改。

如果只需：

$$
M^W
$$

暫存，

連長期記憶都不用改。

---

# 八十八、所以我們可以定義「最低必要持久化層」

$$
\boxed{
L_P^*
=
\arg\min_L
C_{\mathrm{update}}(L)
}
$$

subject to：

$$
\boxed{
\operatorname{FutureAdequacy}(L)\geq1-\epsilon
}
$$

。

---

# 八十九、這就是最小充分展開的記憶對偶

前一篇：

$$
\boxed{
\text{Minimal Sufficient Expansion}
}
$$

。

本篇：

$$
\boxed{
\text{Minimal Sufficient Persistence}
}
$$

。

---

# 九十、形式定義

找：

$$
\boxed{
M_{t+1}^*
=
\arg\min_{M'}
C_{\mathrm{store}}(M')
+
C_{\mathrm{maintain}}(M')
}
$$

使未來相關任務：

$$
\boxed{
P(
G_{\mathrm{future}}
\mid
M'
)
\geq
1-\epsilon
}
$$

且：

$$
\boxed{
P(
\text{repeat known failure}
\mid
M'
)
\leq
\delta
}
$$

。

---

# 九十一、這才是真正回答：

> 到底要記多少？

不是：

> 越多越好。

不是：

> 越少越好。

而是：

$$
\boxed{
\text{enough to change relevant future computation correctly.}
}
$$

。

---

# 九十二、研究命題一：Memory Role Separation

$$
\boxed{
M
=
(
M^W,
M^T,
M^C,
M^-,
M^P
)
}
$$

是功能角色，

不是物理 storage 必然分割。

---

# 九十三、研究命題二：Fidelity Continuum

Raw/Clean 應一般化成：

$$
\boxed{
f\in[0,1]
}
$$

的 memory fidelity spectrum。

---

# 九十四、研究命題三：Negative Knowledge Preservation

失敗：

$$
F_t
$$

不應全部保存，

也不應全部丟棄。

應萃取：

$$
\boxed{
C_f
=
\mathcal K^-(F_t)
}
$$

作為未來展開邊界。

---

# 九十五、研究命題四：Memory Transition Verification

$$
\boxed{
M_t
\rightarrow
M_{t+1}
}
$$

本身是一個高風險 state transition，

需要：

$$
\boxed{
V_M
}
$$

。

近期 trustworthy memory consolidation 工作已直接證明 memory update 的 omission、corruption 與 hallucination 是實際可測的 agent failure mode。

---

# 九十六、研究命題五：Temporal Validity

$$
\boxed{
\operatorname{Valid}(m)
}
$$

應升級成：

$$
\boxed{
\operatorname{Valid}(m,t,W_t)
}
$$

。

記憶真值可能依世界版本與時間改變。

---

# 九十七、研究命題六：Persistence–Revisability Duality

成熟記憶：

$$
\boxed{
\text{Persistence}
+
\text{Revisability}
}
$$

而不是：

$$
\boxed{
\text{Immutable Storage}
}
$$

。

---

# 九十八、研究命題七：Expansion–Memory Recurrence

$$
\boxed{
M_t
\rightarrow
\mathcal E_t
\rightarrow
\mathfrak C_t
\rightarrow
\mathcal M_t
\rightarrow
M_{t+1}
}
$$

。

記憶決定怎麼展開；

展開又產生新的記憶。

---

# 九十九、研究命題八：Plasticity Routing

所有新資訊不應都修改同一 state layer。

$$
\boxed{
\mathcal R_P
:
E_t
\rightarrow
\{
\theta,M,I,\pi,W
\}
}
$$

應選擇最低充分更新層。

---

# 一百、研究命題九：Minimal Sufficient Persistence

$$
\boxed{
\min C(M)
}
$$

subject to：

$$
\boxed{
\text{future competence retained}
}
$$

與：

$$
\boxed{
\text{known failure recurrence bounded}
}
$$

。

---

# 一百零一、研究命題十：Memory as Future Control

本文最重要的重新定義：

$$
\boxed{
\text{Memory}
\neq
\text{representation of the past}
}
$$

而是：

$$
\boxed{
\text{persistent causal influence of selected past consequences on future computation.}
}
$$

。

---

# 一百零二、這也解決「記憶是不是資料庫」的爭論

Database 可以是：

$$
\boxed{
\text{memory substrate}
}
$$

。

但如果資料永遠不被檢索或不影響未來行為，

在功能意義上：

$$
\boxed{
\text{stored}
\neq
\text{remembered}
}
$$

。

---

# 一百零三、反過來，沒有 explicit database 也可能有記憶

若：

$$
\theta_t
$$

已被歷史改變，

使：

$$
F_{\theta_t}
$$

與原先不同，

歷史已經留下：

$$
\boxed{
\text{parametric memory consequence}
}
$$

。

---

# 一百零四、所以真正廣義記憶定義是

若事件：

$$
E_t
$$

使未來：

$$
P(
A_{t+k}
\mid
E_t
)
$$

與：

$$
P(
A_{t+k}
\mid
\neg E_t
)
$$

系統性不同，

且這種差異透過持久狀態保留，

則：

$$
\boxed{
E_t
}
$$

已成為系統 memory 的一部分。

---

# 一百零五、這讓記憶與上一篇「意圖場」正式耦合

原來：

$$
\mathfrak P_t^I
$$

由：

$$
I_t
$$

控制。

現在：

$$
M_t
$$

也進入：

$$
\boxed{
\mathfrak P_t^{I,M}
}
$$

。

因此：

$$
\boxed{
\text{intention gives direction;}
}
$$

$$
\boxed{
\text{memory gives historically conditioned structure.}
}
$$

。

---

# 一百零六、再與展開耦合

$$
\boxed{
\mathfrak P_t^{I,M}
\rightarrow
\mathcal E_t
\rightarrow
\mathfrak C_t
}
$$

。

因此：

> 同樣的目標，在不同記憶歷史下，應展開不同計算域。

---

# 一百零七、這就是學習後「世界看起來不一樣」

新手：

看到：

$$
\Omega
$$

巨大。

專家：

透過：

$$
M
$$

已經知道大量：

$$
\Omega^{-}
$$

不可行。

所以：

$$
\boxed{
|\Omega_{\mathrm{expert}}^{active}|
\ll
|\Omega_{\mathrm{novice}}^{active}|
}
$$

但成功率反而更高。

---

# 一百零八、這也是記憶降低未來展開成本的真正方式

不是：

> 記住答案。

而是：

$$
\boxed{
\text{remember enough geometry of success and failure to avoid rebuilding the same search space.}
}
$$

。

---

# 一百零九、因此可以定義 Memory Compression Gain

若無記憶展開成本：

$$
C_E^0
$$

。

有記憶後：

$$
C_E^M
$$

。

則：

$$
\boxed{
G_M
=
C_E^0-C_E^M
}
$$

。

若：

$$
G_M>0
$$

記憶真正節省未來計算。

---

# 一百一十、但若錯誤記憶造成更多繞路

$$
C_E^M>C_E^0
$$

則：

$$
G_M<0
$$

。

這就是：

$$
\boxed{
\text{negative memory utility}
}
$$

。

所以：

> 有記憶

不一定：

> 比沒記憶好。

---

# 一百一十一、結論：記憶不是過去，而是過去取得修改未來的權利

舊 Raw/Clean 理論最重要的洞察不是：

> AI 必須有兩個記憶體。

而是：

> **探索與收斂對資訊的需求不同。**

展開需要：

$$
\boxed{
\text{diversity}
}
$$

。

收斂需要：

$$
\boxed{
\text{compression}
}
$$

。

未來重建需要：

$$
\boxed{
\text{trajectory}
}
$$

。

避免重犯需要：

$$
\boxed{
\text{negative knowledge}
}
$$

。

可信更新需要：

$$
\boxed{
\text{provenance}
}
$$

。

---

因此第二代記憶系統不再首先問：

> Raw 還是 Clean？

而問：

$$
\boxed{
\text{What information role does this event need to serve in future computation?}
}
$$

。

---

本文最終提出：

$$
\boxed{
M_t
=
(
M_t^W,
M_t^T,
M_t^C,
M_t^-,
M_t^P
)
}
$$

並允許每一記憶具有：

$$
\boxed{
m_i
=
(
f_i,
r_i,
q_i,
\tau_i,
u_i,
p_i
)
}
$$

。

即：

- fidelity；
- revisability；
- confidence；
- lifetime；
- utility；
- provenance。

---

所以：

$$
\boxed{
\text{Memory Architecture}
}
$$

不再只是 storage architecture，

而是：

$$
\boxed{
\text{persistent-state governance architecture}
}
$$

。

---

整個動態智能循環現在成為：

$$
\boxed{
\text{Intention}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{History-conditioned Probability Field}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Expansion}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Active Computational Domain}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Evaluation / Action}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Contraction}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Memory Role Assignment}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Memory Transition Verification}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Persistent State Update}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Different Future Expansion}
}
$$

。

---

因此本文最後的核心公式是：

$$
\boxed{
M_t
\rightarrow
\mathcal E_t
\rightarrow
\mathfrak C_t
\rightarrow
\mathcal V_t
\rightarrow
\mathcal M_t
\rightarrow
M_{t+1}
}
$$

。

不是封閉的圓。

因為：

$$
\boxed{
M_{t+1}\neq M_t
}
$$

。

所以它更像：

$$
\boxed{
\text{a historical spiral of constrained re-expansion}
}
$$

。

---

而這立刻導向第四篇。

現在我們已經有：

$$
\mathfrak P^I
$$

意圖場，

$$
\mathcal E
$$

展開算子，

以及：

$$
M
$$

持久歷史。

如果一個目標在：

$$
t,t+1,\dots,t+n
$$

持續存在，

即使中間：

- 換策略；
- 失敗；
- 重新展開；
- 改變局部計畫；
- 吸收新記憶；

系統仍然反覆回到某一類 goal-compatible region，

那麼這個結構是否可以更嚴格地表示成：

$$
\boxed{
\text{metastable intentional attractor}
}
$$

？

因此下一篇正式進入：

# 《意圖吸引子與亞穩態智慧——概率微動力如何維持長程方向》

它將第一次真正研究：

$$
\boxed{
\mathcal B_I
}
$$

的 basin geometry、

干擾後：

$$
\tau_{\mathrm{return}}
$$

、

goal drift、

吸引子深度、

逃逸條件，

以及：

> **什麼時候「堅持目標」是智能，什麼時候同一套機制已經變成錯誤鎖定與病理性吸引子。**

---

## 參考文獻與既有理論

McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). *Why There Are Complementary Learning Systems in the Hippocampus and Neocortex*. *Psychological Review*, 102(3), 419–457. 該理論以快速 episodic learning 與較慢的 distributed integration 處理快速新學習與既有知識穩定之間的張力；本文僅借用「不同資訊角色／時間尺度」的一般性思想，不宣稱 AI 必須複製生物記憶架構。

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., et al. (2017). *Overcoming catastrophic forgetting in neural networks*. *PNAS*, 114(13), 3521–3526. EWC 透過限制對舊任務重要的參數變化處理 sequential learning 中的 catastrophic forgetting，展示持久知識不一定只能由 explicit replay 實現。

Shin, H., Lee, J. K., Kim, J., & Kim, J. (2017). *Continual Learning with Deep Generative Replay*. NeurIPS 2017. 該方法以生成過去任務樣本再與新資料交錯學習，提供「不完整保存過去資料也可以重建部分過去訓練分布」的代表性方法。

Rolnick, D., Ahuja, A., Schwarz, J., Lillicrap, T., & Wayne, G. (2019). *Experience Replay for Continual Learning*. NeurIPS 2019. CLEAR 透過 replay 與當前 on-policy learning 同時維護 stability 與 plasticity，顯示過去經驗重播仍是 continual-learning 的重要抗遺忘機制。

Kumar, S., Marklund, H., & Van Roy, B. (2025). *Maintaining Plasticity in Continual Learning via Regenerative Regularization*. Conference on Lifelong Learning Agents. 該研究直接處理 neural networks 在非平穩資料流下的 plasticity loss。

Lu, A., Yuan, H., Feng, T., & Sun, Y. (2025). *Rethinking the Stability-Plasticity Trade-off in Continual Learning from an Architectural Perspective*. ICML 2025. 該工作顯示 stability–plasticity 張力也可以存在於架構層，而不只是參數正則化層。

Yu, Y., Yao, L., Xie, Y., et al. (2026). *Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents*. 該工作讓 agent 將 store、retrieve、update、summarize 與 discard 當成可學習 memory actions。

Zhao, Z., Guo, X., Lv, L., et al. (2026). *Accurate and Efficient Long-Term Memory for LLM Agents*. MOSAIC 使用 structured graph storage、temporal/relational information 與 save-time conflict detection 處理長期記憶中的關係丟失及矛盾累積問題。

Yang, T., Paul, S., Srinivasan, V., et al. (2026). *TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory*. 該工作指出 memory update 自身可以造成 omission、corruption 與 hallucination，並以 Memory Transition Verifier 驗證持久記憶狀態轉換。

Neo.K. (2026). *雙記憶體認知超導：展開—收斂對偶性的必然架構*. 舊稿提出 Raw/Clean、Failure Landscape 與展開—收斂角色區分；本文保留其探索歷史、負知識與收斂模式分離的工程洞察，但取消「兩個物理記憶體為數學必然」與固定容量比等強主張。

Neo.K with Aletheia. (2026). *Agent Memory Kernel：舊記憶論文整合重構與雙記憶同步架構*. 此後續文件已主動修正舊稿，保留 Raw/Clean 分工、失敗知識、來源角色與壓縮漂移等工程洞察，而不再把外部資料庫一概視為偽記憶或把固定容量比例視為已證實結論。