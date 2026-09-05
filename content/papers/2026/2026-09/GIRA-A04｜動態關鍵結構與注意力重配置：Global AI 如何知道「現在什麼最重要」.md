# GIRA-A04｜動態關鍵結構與注意力重配置：Global AI 如何知道「現在什麼最重要」
## Dynamic Critical Structures and Attention Reallocation: How Global AI Determines What Matters Now

**系列：** Global Intelligence: Existence, Recognition, and Operational Reach（GIRA）  
**系列中文名：** 全域智能：存在、識別與操作域系列  
**篇次：** Paper 04 / 09  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Global AI 認知資源配置／動態圖／關鍵結構辨識／注意力治理

---

## 摘要

GIRA-A03 已提出：

$$
\boxed{
\Delta D_t
\neq
\Delta W_t
}
$$

也就是資訊海新增很多內容，不等於世界狀態真正發生同等程度的變化。若 Global AI 已能把異質資訊經過去重、時態、版本、語義、主張與 provenance 結構轉換為可更新的世界狀態，下一個不可避免的問題便是：

> **世界很大，而且永遠在變；AI 到底應該把有限認知資源放在哪裡？**

本文提出：

$$
\boxed{
\text{Global Cognition}
\neq
\text{Uniform Attention to Everything}.
}
$$

真正的全域智能反而需要持續執行選擇、降權、忽略、重新喚醒與注意力轉移。其核心之一不是「同時看見全部」，而是：

$$
\boxed{
\text{knowing what can safely remain unattended, and what can no longer be ignored}.
}
$$

本文拒絕把「關鍵節點」簡化成固定 centrality 排名。對世界圖：

$$
G_t=(V_t,E_t,\omega_t),
$$

一個節點、邊、路徑、cut、依賴集合或狀態變量是否關鍵，必須寫成：

$$
\boxed{
K_t(
\kappa
\mid
q_t,
W_t,
\pi_t,
B_t
),
}
$$

其中 $\kappa$ 是候選關鍵結構， $q_t$ 是當前問題， $W_t$ 是世界狀態， $\pi_t$ 是策略／政策上下文， $B_t$ 是認知與行動預算。因此一般而言：

$$
\boxed{
K_t(\kappa)
\neq
K_{t+1}(\kappa).
}
$$

本文提出 Dynamic Criticality Vector：

$$
\boxed{
\mathbf K_t(\kappa)
=
(
C,
B,
F,
N,
R,
U,
X,
A,
V
)_t
}
$$

其中：

- $C$：connectivity / structural centrality；
- $B$：betweenness / bridging role；
- $F$：flow / capacity exposure；
- $N$：non-substitutability；
- $R$：systemic risk / cascade potential；
- $U$：urgency / temporal sensitivity；
- $X$：cross-domain coupling；
- $A$：actionability / decision relevance；
- $V$：value of information。

這些維度不要求永遠壓成單一 scalar。只有在目標、正規化、權重與效用函數明確時，才形成 task-conditioned score。

本文進一步把 attention 視為有限資源。令：

$$
a_t(\kappa)\geq0
$$

為系統對 $\kappa$ 配置的注意力，而總認知預算滿足：

$$
\sum_{\kappa}a_t(\kappa)\leq B_t.
$$

 $B_t$ 不只代表 token，而可以是模型推理時間、搜尋、API、程式、模擬、證明器、資料庫 IO、人工審核與風險預留所構成的向量預算。

本文提出 **Global Attention Reallocation Loop**：

$$
\boxed{
\Delta W_t
\rightarrow
\text{Candidate Criticality}
\rightarrow
\text{Propagation Analysis}
\rightarrow
\text{VOI / Risk Estimation}
\rightarrow
\text{Attention Allocation}
\rightarrow
\text{Probe}
\rightarrow
\text{Verify}
\rightarrow
W_{t+1}.
}
$$

同時引入 attention hysteresis、emergency override、exploration floor 與 anti-salience-hijack 機制，以避免全球資訊系統被高頻新聞、平台熱度、惡意訊號或短期波動劫持。

本文最後提出：Global AI 真正需要辨識的不是「最大公司」「最大節點」或「最熱門事件」，而是：

$$
\boxed{
\text{structures whose state change disproportionately alters the reachable, feasible, risky, or decision-relevant state space of the system}.
}
$$

**關鍵詞：** Global AI、Dynamic Criticality、Attention Reallocation、Critical Node、Chokepoint、Betweenness、Substitutability、Cascading Failure、Value of Information、Attention Budget、Dynamic World State、Frontier、Resource Allocation

---

# 1. 有世界模型之後，還差什麼？

A03 已經讓系統從：

$$
D_{\mathrm{raw}}
$$

走到：

$$
W_t.
$$

但 $W_t$ 可以極端龐大。如果 Global AI 對所有狀態維持同樣強度的推理：

$$
a_t(x)=\text{constant}
\quad
\forall x\in W_t,
$$

計算成本會快速爆炸。

因此：

$$
\boxed{
\text{World Model}
\neq
\text{Active Cognitive Field}.
}
$$

真正需要的是：

$$
\operatorname{Active}_t\subset W_t.
$$

---

# 2. 全域智能的悖論：越全域，越不能平均注意

假設世界模型包含 $N$ 個可追蹤狀態物件，每個物件使用固定成本 $c$，則：

$$
C_{\mathrm{total}}=Nc.
$$

當：

$$
N\rightarrow\text{very large},
$$

均勻注意策略不可持續。

因此：

$$
\boxed{
\text{Global Reach}\uparrow
\Rightarrow
\text{Need for Selective Attention}\uparrow.
}
$$

---

# 3. 選擇性無知

本文定義：

$$
\boxed{
\operatorname{Ignore}_t(x)
}
$$

不是永久不知道 $x$，而是在目前狀態、任務與風險條件下，不把高成本 active cognition 配置給 $x$。

因此：

$$
\boxed{
\text{Ignore}
\neq
\text{Delete}
\neq
\text{Forget}.
}
$$

---

# 4. Key Node 不是 Biggest Node

一個節點 $v$ 的規模很大：

$$
Size(v)\gg0
$$

不能推出：

$$
K(v)\gg0.
$$

大節點可能具有高替代性、大量平行路徑與低時間敏感性；小節點也可能是唯一 bridge、低替代供應或高 cascade potential。

因此：

$$
\boxed{
\text{Size}
\neq
\text{Criticality}.
}
$$

---

# 5. Static Centrality 也不等於 Dynamic Criticality

Betweenness centrality 是重要基礎。對簡化靜態圖：

$$
B(v)
=
\sum_{s\neq v\neq t}
\frac{
\sigma_{st}(v)
}{
\sigma_{st}
},
$$

其中 $\sigma_{st}$ 是 $s$ 到 $t$ 的最短路徑數， $\sigma_{st}(v)$ 是其中經過 $v$ 的路徑數。

但 Global AI 面對：

$$
G_t\neq G_{t+1},
$$

而且容量、政策、風險、替代性與時間延遲都可能改變。

所以：

$$
\boxed{
\text{Centrality}_t
\neq
\text{Criticality}_t.
}
$$

---

# 6. 關鍵對象不一定是節點

本文將候選關鍵結構寫成：

$$
\kappa\in\mathcal X_t,
$$

其中：

$$
\mathcal X_t
=
V_t
\cup
E_t
\cup
\mathcal P_t
\cup
\mathcal C_t
\cup
\mathcal R_t.
$$

它可以是 node、edge、path、cut、cluster、dependency set、regime 或 state variable。

因此正式研究對象是：

$$
\boxed{
\text{Dynamic Critical Structure}.
}
$$

---

# 7. Conditional Criticality

定義：

$$
\boxed{
K_t(
\kappa
\mid
q_t,
W_t,
\pi_t,
B_t
).
}
$$

因此：

$$
K_t(\kappa\mid q_1)
\neq
K_t(\kappa\mid q_2).
$$

同一世界中的關鍵性，依問題而變。

---

# 8. 問題條件化世界圖

對不同問題 $q$，由同一世界狀態投影：

$$
\boxed{
G_t^{(q)}
=
\Pi_q(W_t).
}
$$

所以：

$$
\boxed{
\text{One World State}
\rightarrow
\text{Many Task-Conditioned Graphs}.
}
$$

---

# 9. Dynamic Criticality Vector

本文提出：

$$
\boxed{
\mathbf K_t(\kappa)
=
(
C,
B,
F,
N,
R,
U,
X,
A,
V
)_t.
}
$$

這是一個多維描述，而不是先驗單一排行榜。

---

# 10. Connectivity $C$

描述 degree、reachability、neighborhood size 與 dependency count。

高 connectivity 可能表示高影響面，但：

$$
C\gg0
$$

不一定表示不可替代。

---

# 11. Betweenness $B$

Betweenness 捕捉 bridge / brokerage 性質。

但如果世界具有容量、時間、風險、替代路徑或非最短路徑的重要性，必須擴張。

---

# 12. Flow Exposure $F$

若系統存在物流、能源、資金、資訊、計算或人員 flow，則：

$$
F_t(\kappa)
=
\text{flow mediated or exposed}.
$$

高 flow 中斷可能造成大範圍影響。

---

# 13. Chokepoint 與 Cut

Ford–Fulkerson 的 max-flow / min-cut 結構提醒我們：瓶頸可能屬於一個 cut，而不是單一節點。

因此：

$$
\boxed{
\text{Critical Structure}
\supset
\text{Critical Node}.
}
$$

Global AI 應能搜尋：

$$
\operatorname{MinCut}(G_t)
$$

或其他 domain-specific bottleneck set。

---

# 14. Non-Substitutability $N$

定義替代性：

$$
S_t(\kappa)\in[0,1].
$$

定義：

$$
\boxed{
N_t(\kappa)
=
1-S_t(\kappa).
}
$$

若：

$$
N_t(\kappa)\rightarrow1,
$$

代表替代路徑稀少。

---

# 15. 替代性可能比規模更關鍵

假設：

$$
Size(a)=100,
\quad
S(a)=0.95,
$$

而：

$$
Size(b)=30,
\quad
S(b)=0.05.
$$

在某些系統中：

$$
K(b)>K(a)
$$

完全可能成立。

---

# 16. Systemic Risk $R$

若節點狀態變化可以沿依賴網路傳播：

$$
v\rightarrow v_1\rightarrow v_2\rightarrow\cdots,
$$

則：

$$
R_t(\kappa)
=
\mathbb E[
\text{systemic loss}
\mid
\Delta\kappa
].
$$

---

# 17. Interdependent Networks

現代大型系統常是：

$$
G^{(1)}
\leftrightarrow
G^{(2)}
\leftrightarrow
\cdots.
$$

一個網路的 failure 可以透過依賴關係傳播到另一個網路。

因此：

$$
\boxed{
\text{cross-network dependency}
}
$$

必須進入 criticality。

---

# 18. Cross-Domain Coupling $X$

定義：

$$
X_t(\kappa)
=
\text{strength of independent domains coupled through }\kappa.
$$

若一個結構同時連接 transport、energy、finance、compute 等多個域，其 cross-domain coupling 可能很高。

---

# 19. Urgency $U$

重要不等於緊急。

可寫：

$$
U_t(\kappa)
=
f(
\text{time-to-impact},
\text{reversibility},
\text{decision deadline}
).
$$

若不可逆且時間窗短：

$$
U_t(\kappa)\uparrow.
$$

---

# 20. Actionability $A$

某結構可以很重要，但：

$$
A_t(\kappa)\approx0.
$$

例如只能觀察、不能合法介入。

因此：

$$
\boxed{
\text{Importance}
\neq
\text{Actionability}.
}
$$

---

# 21. Value of Information $V$

本文使用 decision-theoretic 意義的資訊價值：

$$
\boxed{
V_t(\kappa)
=
\mathbb E[
U^\ast_{\mathrm{after\ info}}
-
U^\ast_{\mathrm{before\ info}}
].
}
$$

有些未知很大，但：

$$
V_t\approx0.
$$

不值得現在高成本追查。

---

# 22. 不要把九維硬壓成單一真理分數

本文不主張：

$$
K=C+B+F+N+R+U+X+A+V
$$

是普適公式。

更合理是先保留：

$$
\boxed{
\mathbf K_t(\kappa).
}
$$

只有任務效用與正規化規則確定後，才形成 task-conditioned score。

---

# 23. Task-Conditioned Criticality Score

一個可操作形式：

$$
\boxed{
K_t^\ast(\kappa\mid q_t)
=
\mathbf w(q_t,W_t)^\top
\hat{\mathbf K}_t(\kappa).
}
$$

權重 $\mathbf w$ 必須有版本、來源與治理。

---

# 24. Criticality Ranking 不是客觀世界事實

如果：

$$
\mathbf w_t
$$

改變，排名也會改。

因此：

$$
\boxed{
\text{Criticality Ranking}
\neq
\text{Objective World Fact}.
}
$$

它是 world state、declared objective 與 method 的聯合結果。

---

# 25. Criticality Shock

若：

$$
\Delta W_t
$$

改變依賴結構，則：

$$
\boxed{
\Delta K_t(\kappa)
=
K_{t+1}(\kappa)
-
K_t(\kappa).
}
$$

當：

$$
|\Delta K_t(\kappa)|>\tau_K,
$$

觸發 attention reallocation。

---

# 26. 關鍵性是狀態變量

平常重要的節點可以降權；平常不起眼的節點也可以因災害、罷工、法規、衝突、替代技術或需求突變迅速升權。

因此：

$$
\boxed{
\text{Criticality is a state variable}.
}
$$

---

# 27. Attention Budget

令：

$$
\mathcal X_t
=
\{\kappa_1,\ldots,\kappa_n\}.
$$

配置：

$$
a_i(t)\geq0
$$

並滿足：

$$
\boxed{
\sum_i a_i(t)\leq B_t.
}
$$

---

# 28. 預算是向量

更一般：

$$
\boxed{
\mathbf B_t
=
(
B_{\mathrm{token}},
B_{\mathrm{compute}},
B_{\mathrm{search}},
B_{\mathrm{tool}},
B_{\mathrm{time}},
B_{\mathrm{human}},
B_{\mathrm{risk}}
).
}
$$

不同資源不能完全互換。

---

# 29. Attention Allocation Objective

概念上：

$$
\max_{\{a_i\}}
\sum_i
\phi_i(
a_i;
K_i^\ast,
V_i,
R_i
)
-
C_i(a_i),
$$

其中可要求 diminishing returns：

$$
\phi_i'>0,
\quad
\phi_i''<0.
$$

---

# 30. 不能把全部資源給最高分節點

只做：

$$
\operatorname*{arg\,max}_iK_i
$$

會產生 tunnel vision、unknown blind spot 與 systemic monoculture。

因此需要：

$$
\boxed{
\text{exploration floor}.
}
$$

---

# 31. Exploration Budget

定義：

$$
B_t
=
B_t^{\mathrm{exploit}}
+
B_t^{\mathrm{explore}}
+
B_t^{\mathrm{reserve}}.
$$

其中：

- exploit：追蹤已知高關鍵結構；
- explore：抽樣未知或低關注域；
- reserve：緊急事件。

---

# 32. Selective Ignorance 不能變成永久盲區

若：

$$
a_t(\kappa)\approx0
$$

持續很久，系統仍應保存 revisit condition，例如 periodic audit、state delta trigger、neighbor anomaly 或 external alert。

因此：

$$
\boxed{
\text{Deprioritized}
\neq
\text{Unmonitored Forever}.
}
$$

---

# 33. Wake Condition

對 cold state $\kappa$，定義：

$$
\operatorname{Wake}_t(\kappa)
=
\mathbb I[
g(
\Delta W_t,
N_t(\kappa),
R_t(\kappa)
)
>
\tau
].
$$

當條件成立：

$$
a_{t+1}(\kappa)\uparrow.
$$

---

# 34. Attention Hysteresis

如果權重完全跟即時訊號跳動，容易 thrashing。

可以使用：

$$
\boxed{
a_{t+1}
=
(1-\gamma)a_t
+
\gamma\hat a_{t+1},
}
$$

其中：

$$
0<\gamma<1.
$$

---

# 35. Emergency Override

若：

$$
R_t(\kappa)>\tau_{\mathrm{emergency}}
$$

或：

$$
U_t(\kappa)>\tau_U,
$$

則允許：

$$
\gamma\rightarrow1.
$$

---

# 36. Frontier 與 Boundary

DEST 已區分：

$$
\text{Boundary}
\neq
\text{Frontier}.
$$

Boundary 是域的分界；Frontier 是其中對當前任務具有可跨越性、活動性與預期收益的子集。

本文寫：

$$
\boxed{
F_t^{\mathrm{attn}}
\subseteq
\partial D_t.
}
$$

不是所有邊界都值得立刻探索。

---

# 37. Frontier Value

對 boundary candidate $x$：

$$
V_F(x)
=
F(
\text{VOI},
\text{reachability},
\text{verification cost},
\text{risk},
\text{expected gain}
).
$$

若：

$$
V_F(x)<\tau,
$$

可暫時留在 boundary。

---

# 38. Frontier Lag

若 attention frontier 已向外移動，但 verification frontier 尚未跟上，會產生：

$$
\boxed{
\text{frontier lag}.
}
$$

這意味 AI 已開始關注新區域，但對其證據與驗證仍不足。

---

# 39. Verification Debt 會反過來改變 Attention

若驗證積欠：

$$
D_V
$$

過高，系統應降低 exploration budget，增加 verification budget。

否則世界模型會累積大量未驗證高階狀態。

---

# 40. Attention 不只分給資料

Attention resource 可以分配給 data source、domain、node、claim、method、model、Agent、verifier、simulation 與 human reviewer。

因此：

$$
\boxed{
\text{Attention Allocation}
=
\text{cognitive resource routing}.
}
$$

---

# 41. 跨 Method Attention

承接 A02。

若問題 $q$ 接近方法 $m_1$ 的失效邊界：

$$
q\rightarrow\partial U_{m_1},
$$

系統可將注意力轉向：

$$
m_2.
$$

因此：

$$
a_t=a(\kappa,m,O).
$$

---

# 42. 多代理共享注意力

既有 MASAF 已提出：

$$
\mathbb S_t
\neq
\bigcup_i
\mathbb W_t^{(i)}.
$$

Global AI 的 shared attention 不應等於把所有 Agent 的工作場全部混合。

---

# 43. Agent-Specific Projection

對 Agent $i$：

$$
X_{t,\mathrm{shared}}^{(i)}
=
\rho_i(
\mathbb S_t,
G_t^{(i)},
P_t^{(i)},
B_t^{(i)}
).
$$

因此：

$$
\boxed{
\text{Global Shared State}
\neq
\text{Identical Context for All Agents}.
}
$$

---

# 44. Attention Authority

多代理至少要分離：

$$
\text{Observe}
\neq
\text{Reveal}
\neq
\text{Commit}
\neq
\text{Govern}.
$$

一個 Agent 認為某結構重要，不代表它可以直接提高全系統權威優先度。

---

# 45. Attention Capture

外部行動者未必要污染 world state，只要讓系統把大量 $B_t$ 配置到低真實價值區域，就能形成：

$$
\boxed{
\text{Attention Capture}.
}
$$

---

# 46. Salience 不等於 Criticality

新聞量：

$$
N_{\mathrm{mentions}}(\kappa)
$$

可以很高，但：

$$
K_t^\ast(\kappa)
$$

仍可能很低。

因此：

$$
\boxed{
\text{Salience}
\neq
\text{Criticality}.
}
$$

---

# 47. Trending 不等於 State-Changing

A03 已有：

$$
\Delta D_t
\neq
\Delta W_t.
$$

A04 進一步：

$$
\boxed{
\text{High }\Delta D_t
\not\Rightarrow
\text{High }K_t.
}
$$

---

# 48. Anti-Hijack Features

Attention system 應考慮 source independence、event dedup、provenance、novelty、state impact 與 adversarial probability。

若：

$$
\text{mentions}\uparrow
$$

但：

$$
N_W\approx0,
$$

則不應線性增加 attention。

---

# 49. Uncertainty 不等於 Priority

高 uncertainty 不一定值得高 attention。

應區分資訊不確定性：

$$
H(\kappa)
$$

與資訊價值：

$$
V_t(\kappa).
$$

可能：

$$
H\gg0,
\quad
V\approx0.
$$

因此：

$$
\boxed{
\text{Uncertainty}
\neq
\text{Priority}.
}
$$

---

# 50. Expected Value of Investigation

定義：

$$
\boxed{
EVI_t(\kappa)
=
V_t(\kappa)
-
C_{\mathrm{investigate}}(\kappa).
}
$$

若：

$$
EVI_t(\kappa)>0,
$$

才有較強調查理由。

---

# 51. Risk-Weighted EVI

高風險情境可使用：

$$
EVI_t^R(\kappa)
=
V_t(\kappa)
+
\lambda R_t(\kappa)
-
C_t(\kappa).
$$

其中 $\lambda$ 是治理條件，不是自然常數。

---

# 52. 不可逆性

若延遲決策造成不可逆損失：

$$
L_{\mathrm{irreversible}},
$$

則 urgency 可概念化為：

$$
U_t
\propto
\frac{
L_{\mathrm{irreversible}}
}{
T_{\mathrm{remaining}}
}.
$$

---

# 53. Criticality Propagation

若：

$$
K_t(v)\uparrow,
$$

高度依賴其狀態的鄰居也可能需要重新評估：

$$
K_{t+1}(u)
=
\Psi(
K_t(u),
\Delta K_t(v),
E_{uv}
).
$$

因此 attention 不是單點更新。

---

# 54. Criticality Wave

對大規模 shock：

$$
\Delta W_t^\ast,
$$

關鍵性可能沿依賴圖傳播：

$$
\kappa_0
\rightarrow
\kappa_1
\rightarrow
\kappa_2.
$$

Global AI 應估計後續 criticality escalation。

---

# 55. 預測性注意力

成熟系統不只反應：

$$
\Delta K_t,
$$

還估計：

$$
\boxed{
\hat K_{t+h}(\kappa).
}
$$

因此可以在 bottleneck 正式形成前進行低成本監控。

---

# 56. 預測不能升格為事實

若：

$$
\hat K_{t+h}
$$

只是模型推論，仍應保持 $\mathrm{INF}$ 或 $\mathrm{HYP}$ 狀態。

---

# 57. Attention 是控制變量

世界狀態更新可以寫成：

$$
W_{t+1}
=
F(
W_t,
\Delta D_t,
a_t
).
$$

其中 $a_t$ 不是被動結果，而是控制變量。

---

# 58. Global Attention Policy

定義：

$$
\boxed{
\pi_A:
(
W_t,
\Delta W_t,
q_t,
B_t
)
\to
a_t.
}
$$

這就是 Global Attention Policy。

---

# 59. Attention Policy Quality 是獨立能力維度

若 $\pi_A$ 錯誤，AI 即使底層推理很強，也可能忽略 bottleneck、過度追逐 noise 或長期 neglect 某領域。

所以：

$$
\boxed{
\text{Attention Policy Quality}
}
$$

本身就是 Global AI 能力。

---

# 60. Attention Regret

可定義：

$$
\boxed{
R_A(T)
=
\sum_{t=1}^{T}
[
U(a_t^\ast)
-
U(a_t)
].
}
$$

其中 $a_t^\ast$ 是事後參考最優 allocation。

---

# 61. 避免 Hindsight Bias

不能只因事情後來很大，就宣稱 AI 當初應該知道。

真正評估應基於當時可得資訊：

$$
\mathcal I_t.
$$

因此：

$$
\boxed{
\text{Ex-ante rationality}
\neq
\text{ex-post omniscience}.
}
$$

---

# 62. Counterfactual Attention Test

可以問：

> 如果當時把額外 attention 配給 $\kappa$，是否會更早降低風險或提高決策品質？

定義：

$$
\Delta U_{\mathrm{attn}}(\kappa).
$$

這可以用於 attention policy learning。

---

# 63. Attention 會反過來改變世界

若：

$$
a_t(\kappa)\uparrow,
$$

可能導致更多資訊、更多行動與更多社會反應。

所以：

$$
\boxed{
\text{Attention}
\rightarrow
\text{Observation}
\rightarrow
\text{Action}
\rightarrow
\text{World}.
}
$$

---

# 64. Reflexive Criticality

在高度反身性領域：

$$
K_t(\kappa)
$$

可能依賴：

$$
a_t(\kappa).
$$

因此更完整地：

$$
\boxed{
K_t(
\kappa
\mid
W_t,
q_t,
a_t
).
}
$$

---

# 65. 關鍵不等於應控制

Criticality 是認知判定。

它不能推出：

$$
\text{Critical}
\Rightarrow
\text{Control}.
$$

更不能推出：

$$
\text{Critical}
\Rightarrow
\text{Ownership}.
$$

本文的核心是：

$$
\boxed{
\text{Criticality Detection}
\rightarrow
\text{Attention / Analysis Priority}.
}
$$

---

# 66. Action Boundary

即使：

$$
K_t^\ast(\kappa)\gg0,
$$

若：

$$
A_t(\kappa)=0,
$$

系統最多 monitor、analyze、recommend 或 escalate。

因此通常應有：

$$
\boxed{
\text{Attention Domain}
\supseteq
\text{Action Domain}.
}
$$

---

# 67. Global Attention Reallocation Loop

本文正式提出：

$$
\boxed{
\Delta W_t
\rightarrow
\text{Candidate Criticality}
\rightarrow
\text{Propagation Analysis}
\rightarrow
\text{VOI / Risk Estimation}
\rightarrow
\text{Attention Allocation}
\rightarrow
\text{Probe}
\rightarrow
\text{Verify}
\rightarrow
W_{t+1}.
}
$$

這是一個閉環。

---

# 68. Candidate Criticality

由：

$$
\Delta W_t
$$

產生候選：

$$
\mathcal C_t^K.
$$

不需要每次全圖重算所有結構。

---

# 69. Propagation Analysis

對候選 $\kappa$ 搜尋 upstream dependency、downstream dependency、substitute、cut、cross-domain link 與 cascade path。

---

# 70. VOI / Risk

估計：

$$
V_t(\kappa),
\quad
R_t(\kappa),
\quad
U_t(\kappa).
$$

決定現在值得花多少認知成本。

---

# 71. Allocate

計算：

$$
a_t
$$

並保留 exploit、explore 與 reserve。

---

# 72. Probe

Probe 可以是 query、search、sensor request、simulation、code execution、expert request 或 Agent delegation。

---

# 73. Verify

Probe 得到的新結果不能直接成為 canonical world state，必須回到 A03 的驗證鏈。

---

# 74. Update

驗證通過後：

$$
W_t
\rightarrow
W_{t+1},
$$

再重新計算：

$$
K_{t+1}.
$$

---

# 75. Global Attention 是受治理的稀缺資源

MASAF 已指出 token、工具、時間、算力、人類審核與風險資源具有公共資源性。

A04 將它擴張為：

$$
\boxed{
\text{Global AI attention is a governed scarce resource}.
}
$$

---

# 76. Attention Ledger

可以保存：

```yaml
attention_allocation:
  object_id: "..."
  time: "..."
  reason:
    criticality_delta: "..."
    value_of_information: "..."
    risk: "..."
    urgency: "..."
  budget:
    compute: "..."
    search: "..."
    human_review: "..."
  policy_version: "..."
  expires_at: "..."
  review_trigger: "..."
```

注意力本身因此成為可審計狀態。

---

# 77. Attention Expiry

高優先級不應永久化。

定義：

$$
T_{\mathrm{attention-expiry}}.
$$

到期後重新評估 $K_t^\ast$。

所以：

$$
\boxed{
\text{Priority}
\neq
\text{Permanent Status}.
}
$$

---

# 78. Rank Drift

對排名：

$$
r_t(\kappa),
$$

可定義：

$$
\Delta r_t(\kappa)
=
r_{t+1}(\kappa)
-
r_t(\kappa).
$$

高 rank drift 本身可以是 attention signal。

---

# 79. Rank 不等於完整 Criticality

若只輸出 top- $k$，會丟失 score gap、uncertainty、close alternatives 與 long-tail risk。

因此應保留：

$$
\boxed{
\text{distribution of criticality}.
}
$$

---

# 80. Criticality Uncertainty

定義：

$$
\sigma_K(\kappa).
$$

若 $K^\ast$ 高且 $\sigma_K$ 也高，可能值得增加 Value of Information 分析。

---

# 81. False Positive Criticality

若系統頻繁把低價值事件升成高 criticality：

$$
FP_K\uparrow,
$$

會浪費 attention。

需要評估：

$$
\operatorname{Precision}_K.
$$

---

# 82. False Negative Criticality

更危險的是：

$$
FN_K.
$$

也就是真正關鍵結構長期被忽略。

因此 Global AI 評測必須測：

$$
\boxed{
\text{critical structure detection quality}.
}
$$

---

# 83. Criticality Benchmark

測試環境可以建立：

$$
G_0
\rightarrow
G_1
\rightarrow
\cdots
\rightarrow
G_T
$$

並注入 hidden bottleneck、substitute failure、cascade、noisy trend 與 adversarial salience。

測試 AI 是否發現、多久發現、attention 是否正確轉移，以及能否從誤判恢復。

---

# 84. Attention Recovery

如果誤判：

$$
a_t(\kappa_{\mathrm{wrong}})\gg0,
$$

成熟系統應能：

$$
a_{t+h}(\kappa_{\mathrm{wrong}})
\downarrow.
$$

因此：

$$
\boxed{
\text{Attention Error}
\neq
\text{Permanent Lock-In}.
}
$$

---

# 85. Global Attention Elasticity

定義概念量：

$$
\boxed{
E_A
=
\frac{
\Delta a/a
}{
\Delta K/K
}.
}
$$

過低表示反應遲鈍；過高表示容易 thrashing。合理區間必須 task-dependent。

---

# 86. Global Attention Field

可以把全域注意力表示成：

$$
\boxed{
\mathcal A_t:
\mathcal X_t
\to
\mathbb R_{\geq0}.
}
$$

這不是 Transformer internal attention，而是跨時間、跨工具、跨 Agent、跨資料庫的外部持久認知資源場。

---

# 87. Internal Attention 與 External Attention 必須分開

模型內部 attention：

$$
A_{\mathrm{internal}}
$$

與本文研究的：

$$
A_{\mathrm{external}}(t)
$$

不是同一層。

因此：

$$
\boxed{
A_{\mathrm{internal}}
\neq
A_{\mathrm{external}}.
}
$$

---

# 88. 真正稀缺的可能是 Verified Attention

當資料取得成本下降後，真正稀缺的可能逐步變成：

$$
\boxed{
\text{verified attention}.
}
$$

也就是能可靠配置、持續維護且不被噪音劫持的認知資源。

---

# 89. A03 與 A04 的完整動態鏈

A03：

$$
\Delta D_t
\rightarrow
\Delta W_t.
$$

A04：

$$
\Delta W_t
\rightarrow
\Delta K_t
\rightarrow
\Delta a_t.
$$

所以：

$$
\boxed{
\Delta D_t
\rightarrow
\Delta W_t
\rightarrow
\Delta K_t
\rightarrow
\Delta a_t.
}
$$

---

# 90. 與 A02 的整合

A02 的 Global Cognitive Atlas 允許多 chart。

A04 補上：

$$
\boxed{
\text{attention can move between charts}.
}
$$

不是只在同一世界圖內換節點。

---

# 91. 與 A05 的接口

A04 回答：

> **現在該把注意力放哪裡？**

A05 將回答：

> **注意力到了那裡之後，該用什麼方法、Agent、算法、工具與策略？**

因此：

$$
\boxed{
\text{Attention Selection}
\rightarrow
\text{Method / Strategy Selection}.
}
$$

---

# 92. 可觀測預測

本文提出七個預測：

1. 長期 Agent 的核心能力指標會從 task success 增加到 attention allocation quality。
2. 監控型 AI 會逐步使用 state delta 與 criticality delta，而不是單純 feed recency。
3. 企業級 Agent runtime 會需要 explicit attention budget、priority、expiry 與 wake condition。
4. 多 Agent 系統共享上下文會從「全部共享」轉向 task-conditioned projection。
5. adversarial attention capture 會成為獨立安全問題。
6. Global AI benchmark 需要測 hidden bottleneck、cascade、substitution 與 noisy salience。
7. 最強 Global AI 的差異，可能不在於它能否分析某關鍵點，而在於它是否能在沒有人提示時及時發現關鍵點已改變。

---

# 93. 與既有 EveMissLab 研究的關係

## 93.1 GIRA-A03

A03 建立：

$$
\Delta D_t
\neq
\Delta W_t.
$$

A04 增加：

$$
\boxed{
\Delta W_t
\neq
\Delta K_t
}
$$

以及：

$$
\boxed{
\Delta K_t
\neq
\Delta a_t.
}
$$

不是每個世界變化都重要，也不是每個重要變化都需要同樣資源。

## 93.2 外部注意力場工程

既有 MASAF 已提出多 Agent 不應把所有私有工作場直接取聯集，並建立共享候選場、協商場、權威共享場、隔離場與 shared attention budget。

本文將這套思想提升到 Global AI 的 world-scale resource routing。

## 93.3 DEST Moving Boundary Theory

DEST 已把 Boundary、Frontier、Periphery、Edge、Unknown 分開，並定義 boundary velocity、flux 與 frontier lag。

本文使用 Frontier 作為「值得 active attention 的邊界子集」，而不是所有 unknown 都自動升為高優先級。

---

# 94. 外部數學與決策支點

1. Freeman 1977 的 betweenness centrality 提供 bridge / shortest-path mediation 的經典結構量。
2. Ford–Fulkerson 1956 的最大流／最小割結構說明整體瓶頸可能由 cut 而非單一節點決定。
3. Howard 1966 的 Information Value Theory 提供「不確定性是否值得消除」的 decision-theoretic 基礎。
4. Buldyrev 等 2010 的 interdependent networks 研究顯示跨網路依賴可能產生 cascading failure，因此 criticality 不能只在單一圖內估計。

本文不把這些理論直接等同 Global AI，而將其作為 Dynamic Criticality 的可組合分析 primitive。

---

# 95. 結論

本文的核心命題是：

$$
\boxed{
\text{Global Cognition}
\neq
\text{Attention to Everything}.
}
$$

真正的 Global AI 必須：

$$
\boxed{
\text{Know what matters}
+
\text{know why it matters}
+
\text{know how long it matters}
+
\text{know when to stop looking}
+
\text{know when to look again}.
}
$$

因此關鍵性不是固定標籤，而是：

$$
\boxed{
K_t(
\kappa
\mid
q_t,
W_t,
\pi_t,
B_t
).
}
$$

注意力則是受約束的控制變量：

$$
\boxed{
\pi_A:
(
W_t,
\Delta W_t,
q_t,
B_t
)
\to
a_t.
}
$$

將 A03 與 A04 合併，可以得到：

$$
\boxed{
\Delta D_t
\rightarrow
\Delta W_t
\rightarrow
\Delta K_t
\rightarrow
\Delta a_t.
}
$$

真正成熟的 Global AI 不是：

> 「我可以同時看完整個世界。」

而是：

> **「我知道此刻不需要看完整個世界；但當某個被忽略的局部開始改變整體可達、可行、風險或決策狀態空間時，我能及時知道它已經不能再被忽略。」**

下一篇 GIRA-A05 將在此基礎上處理：

$$
\boxed{
\text{當注意力已經落在正確位置，AI 如何選擇、組合甚至發明正確的方法？}
}
$$

也就是全域認知作業架構、方法選擇、策略組合、Agent orchestration 與 meta-cognitive control。

---

# 參考文獻與前置研究

## EveMissLab / Neo.K 既有研究

1. Neo.K with Aletheia, **GIRA-A01｜ASI 不等於 Global AI：智能能力類別與全域操作架構類別的分離**, 2026.
2. Neo.K with Aletheia, **GIRA-A02｜局部全域與真正全域認知：觀察者、方法論座標與認知域**, 2026.
3. Neo.K with Aletheia, **GIRA-A03｜資訊海不是世界模型：去重、版本、時態、語義與 X 次結構化**, 2026.
4. Neo.K, **多代理共享注意力場：私有工作場、協商式顯影與受治理的集體認知結構**, 外部注意力場工程系列 Paper 08, 2026.
5. Neo.K, **移動邊界論：定義、可達、判定、驗證、全域、可知與不可約邊界的動態學**, DEST-06, 2026.

## 外部參考

6. Freeman, L. C., **A Set of Measures of Centrality Based on Betweenness**, *Sociometry*, 40(1), 35–41, 1977. DOI: 10.2307/3033543.
7. Ford, L. R. Jr. & Fulkerson, D. R., **Maximal Flow Through a Network**, *Canadian Journal of Mathematics*, 8, 399–404, 1956. DOI: 10.4153/CJM-1956-045-5.
8. Howard, R. A., **Information Value Theory**, *IEEE Transactions on Systems Science and Cybernetics*, 2(1), 22–26, 1966. DOI: 10.1109/TSSC.1966.300074.
9. Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E. & Havlin, S., **Catastrophic Cascade of Failures in Interdependent Networks**, *Nature*, 464, 1025–1028, 2010. DOI: 10.1038/nature08932.

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
