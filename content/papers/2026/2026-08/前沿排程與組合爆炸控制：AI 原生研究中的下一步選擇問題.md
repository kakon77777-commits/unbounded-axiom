# 前沿排程與組合爆炸控制：AI 原生研究中的下一步選擇問題

**English Title:** Frontier Scheduling and Combinatorial Explosion Control: Choosing the Next Research Step in AI-Native Knowledge Expansion  
**Series:** AI-Native Knowledge Expansion, Paper VI  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10

## 摘要

Base Knowledge Space Expansion（BKSE）允許 AI 對可靠知識進行變種、反駁、重組、形式化與交叉驗證。前五篇進一步建立了命題身份、錯誤鄰域、Proof Lattice 與 AI-Native Research Graph。然而，一旦這些機制被真正自動化，系統立即遭遇一個比「能否生成」更嚴重的問題：**可合法生成的下一步數量可能遠大於可實際探索的算力預算。**

對研究圖 \(G_t\) 中的每個節點，AI 都可能產生若干 specialization、generalization、converse、assumption ablation、composition、counterexample search、proof search、cross-verification 與 literature-check 任務。若平均分支因子為 \(b\)，深度為 \(d\)，則候選空間近似呈 \(O(b^d)\) 增長。即使每個節點都合法、可驗證，無差別展開也會把系統拖入大量 technically correct but scientifically irrelevant 的低價值工作。

本文提出 **Frontier Scheduling** 作為 AI 原生研究的核心控制層。研究系統不應問「下一個能做什麼」，而應問：

\[
\boxed{
\text{Which next action maximizes expected structural gain under a finite budget?}
}
\]

本文定義前沿節點（Frontier Node）、研究動作（Research Action）、預期結構增益（Expected Structural Gain）、驗證可行性、重用價值、分歧價值、未知度、成本、重複度與風險等量；提出多目標 Frontier Score、budget-aware scheduling、exploration–exploitation balance、stopping criteria、branch dormancy 與 revival 機制。本文並區分 uncertainty、novelty、importance 與 usefulness，指出「最不確定」不等於「最值得研究」。

本文的核心主張是：AI 原生研究真正的稀缺資源不是可生成候選，而是**注意力與驗證預算**。當生成接近廉價時，研究能力將越來越取決於選擇函數，而非生成函數。

**關鍵詞：** Frontier Scheduling；組合爆炸；AI 原生研究；BKSE；研究排程；探索與利用；proof search；theorem discovery；information gain；research graph

---

## 1. 從生成瓶頸到選擇瓶頸

早期 AI research pipeline 的主要問題常被寫成：

\[
\text{Can the model generate a useful hypothesis?}
\]

但 BKSE 把問題反過來。

若對每個知識節點 \(K_i\) 都允許一組動作：

\[
\mathcal A(K_i)
=
\{
T_{\mathrm{eq}},
T_{\mathrm{conv}},
T_{\mathrm{gen}},
T_{\mathrm{spec}},
T_{\mathrm{ablate}},
T_{\mathrm{compose}},
T_{\mathrm{prove}},
T_{\mathrm{disprove}},
T_{\mathrm{verify}}
\},
\]

則真正的問題很快變成：

\[
|\mathcal A(G_t)|\gg B_t,
\]

其中 \(B_t\) 是當前研究預算。

因此：

\[
\boxed{
\text{Generation Capacity}
>
\text{Evaluation Capacity}
}
\]

可能成為 AI-native research 的常態。

此時系統最重要的函數不再只是：

\[
\operatorname{Generate}(K),
\]

而是：

\[
\boxed{
\operatorname{SelectNext}(G_t,B_t).
}
\]

---

## 2. 組合爆炸不是理論問題，而是第一級工程問題

假設每個 claim 平均生成：

\[
b=20
\]

個合法後繼。

只展開五層：

\[
20^5
=
3.2\times10^6.
\]

若每個節點又有多條 proof、counterexample、verification、literature-check 與 composition edge，實際分支因子會更高。

所以：

\[
\boxed{
\text{Legal Expansion}
\neq
\text{Exhaustive Expansion}.
}
\]

BKSE 的閉包：

\[
B^\ast
=
\bigcup_{k=0}^{\infty}B_k
\]

是理論上的可達空間，不是 runtime 必須窮舉的工作清單。

真正的 AI-native research 是在：

\[
B^\ast
\]

中進行高度稀疏的路徑選擇。

---

## 3. 定義 Frontier

令當前研究圖為：

\[
G_t=(V_t,E_t).
\]

定義 Frontier：

\[
\boxed{
F_t
=
\{(K,a):K\in V_t,\ a\in\mathcal A(K),\ a\text{ 尚未被充分執行}\}.
}
\]

注意 Frontier 不是單純的「尚未證明 theorem」。

它可以包含：

- 尚未嘗試的 proof family；
- 尚未檢查的 converse；
- 尚未做的 assumption ablation；
- 尚未搜尋的 counterexample；
- 尚未 formalize 的 claim；
- 尚未 cross-check 的 proof；
- 尚未 literature-check 的 derived claim；
- 尚未探索的 composition；
- 尚未解決的 contradiction；
- 尚未重播的 experiment。

因此研究前沿是一組：

\[
\boxed{
\text{node-action pairs}
}
\]

而不是單純節點集合。

---

## 4. 下一步不是「問題」，而是 Action

對同一 claim：

\[
C
\]

可能同時存在：

\[
a_1=\text{prove},
\]

\[
a_2=\text{disprove},
\]

\[
a_3=\text{generalize},
\]

\[
a_4=\text{formalize},
\]

\[
a_5=\text{literature search}.
\]

因此 scheduler 應評分：

\[
S(C,a),
\]

而不是只評：

\[
S(C).
\]

這一點很重要。

一個 theorem 可能不值得再找第五條 proof，但非常值得做 literature novelty check。

另一個 theorem 可能不值得 generalize，但值得尋找 minimal counterexample。

所以：

\[
\boxed{
\text{research value is action-conditional}.
}
\]

---

## 5. 七個核心排程維度

本文先提出七個工作維度。

對候選 action：

\[
q=(K,a)
\]

定義：

\[
\mathbf z(q)
=
(
N,U,G,R,V,C,D
).
\]

其中：

### \(N\)：Novelty Potential

該動作是否可能新增非重複結構？

### \(U\)：Uncertainty / Unresolvedness

目前資訊是否不足、衝突或未閉合？

### \(G\)：Structural Gain

成功後會新增多少可重用關係、lemma、proof class 或 bridge？

### \(R\)：Reuse Potential

結果是否可能被大量 downstream nodes 重用？

### \(V\)：Verification Feasibility

結果是否容易被形式 proof、tests、experiment 或 external evidence 檢查？

### \(C\)：Cost

需要多少：

- token；
- GPU；
- CPU；
- prover search；
- external calls；
- human review；
- wall-clock resource。

### \(D\)：Duplication / Redundancy Risk

是否高度可能只是已有結果的換皮？

---

## 6. Frontier Score

最簡版本：

\[
\boxed{
S_F(q)
=
w_NN
+
w_UU
+
w_GG
+
w_RR
+
w_VV
-
w_CC
-
w_DD.
}
\]

系統每輪選：

\[
q^\ast
=
\arg\max_{q\in F_t}S_F(q).
\]

但這只是一個 baseline。

因為不同任務的權重不能永久固定。

例如 proof-completion 階段：

\[
w_V,w_R
\]

可能較高。

探索新 theorem family 時：

\[
w_N,w_G
\]

較高。

debug / verification 階段：

\[
w_U,w_V
\]

可能較高。

所以更合理的是：

\[
\boxed{
S_F(q\mid s_t)
}
\]

其中 \(s_t\) 是研究 runtime 當前狀態。

---

## 7. Importance 不等於 Uncertainty

這是 Frontier Scheduling 最重要的防錯之一。

Active learning 常利用 uncertainty 選擇下一個樣本。

但研究系統若簡單採用：

\[
S(q)=U(q),
\]

很可能出現：

> AI 專門研究它最不懂、但完全不重要的東西。

所以：

\[
\boxed{
\text{uncertain}
\neq
\text{important}.
}
\]

例如某個極端邊界 case 可能非常難判定：

\[
U\approx1,
\]

但即使解決，它不產生新的 downstream capability：

\[
G\approx0,
\quad
R\approx0.
\]

這類問題應被降低優先級。

---

## 8. Novelty 也不等於 Value

同樣地：

\[
\text{novel}
\neq
\text{useful}.
\]

AI 可以生成無數從沒有人寫過的 theorem：

\[
T_1,T_2,\ldots
\]

但若它們都是：

- 人工拼接；
- 沒有後續依賴；
- 沒有概念橋接；
- 沒有壓縮價值；
- 沒有應用；
- 沒有異常結構；

則：

\[
N\gg0
\]

不代表：

\[
G,R\gg0.
\]

所以 novelty 必須與 structural gain 分開。

---

## 9. Usefulness 可以由未來重用近似

2026 年的 self-supervised theorem-discovery 工作已提供一個非常有意思的實證方向：agent 從 axioms 與 inference rules 開始，在 proof search 中抽取「有用 theorem」，建立 theorem library，並把這些 theorem 作為後續 proof 的 lemmas 重用。

這提示可以定義：

\[
\boxed{
R(K)
=
\text{expected future reuse}.
}
\]

一個 theorem 的價值不只在於它自己是否困難。

若：

\[
K_1
\]

能讓：

\[
100
\]

個後續 proof 變短或可解，而：

\[
K_2
\]

只是一個孤立結果，則即使 \(K_2\) 更難：

\[
R(K_1)>R(K_2).
\]

這是一種非常適合 AI-native mathematics 的 utility 定義。

---

## 10. Proof Search 已經是縮小版 Frontier Scheduling

Automatic theorem proving 已經面對同樣問題。

給定 proof state：

\[
s_t,
\]

模型會產生多個 tactics：

\[
a_1,\ldots,a_n.
\]

如果全部展開：

\[
\text{proof tree}
\]

會快速爆炸。

所以 proof search 本質上已經需要：

\[
\operatorname{Prioritize}(s,a).
\]

BFS-Prover 使用 best-first tree search，並透過訓練讓模型偏向更 productive 的 state–tactic expansion；LeanProgress 則直接預測 proof progress，用來改善 best-first search。

這說明：

\[
\boxed{
\text{Frontier Scheduling}
}
\]

不是抽象哲學，而是 theorem proving 中已存在的縮小版工程問題。

本文只是把單一 proof tree 的 node selection 提升到：

\[
\text{whole research graph}.
\]

---

## 11. Research Progress 不應只有距離終點

Proof progress 可以問：

\[
\text{還剩幾步？}
\]

但研究沒有固定 terminal state。

所以研究 progress 更接近：

\[
\boxed{
\Delta G_t
=
\text{new verified structural information}.
}
\]

一次 research action 的價值可能是：

- 解掉一個 open question；
- 找到反例；
- 發現兩個 theorem 等價；
- 刪除冗餘假設；
- 建立跨域 bridge；
- 把 UNKNOWN 變成 VERIFIED；
- 把「新結果」判定成已有文獻；
- 證明某條 branch 不值得再探索。

甚至：

\[
\boxed{
\text{good negative information is progress}.
}
\]

---

## 12. Expected Structural Gain

定義 action：

\[
a
\]

在 graph state \(G_t\) 下的結果隨機變數：

\[
O_a.
\]

則概念上可以定義：

\[
\boxed{
ESG(a\mid G_t)
=
\mathbb E[
\Delta \mathcal I(G_t,O_a)
].
}
\]

其中：

\[
\mathcal I(G)
\]

不是 Shannon information 的直接同義，而是「有效結構資訊」函數。

它可以包括：

\[
\mathcal I(G)
=
\alpha |V/\sim|
+
\beta |\text{verified edges}|
+
\gamma |\text{reusable lemmas}|
+
\delta |\text{resolved conflicts}|
-
\lambda |\text{redundant nodes}|.
\]

因此 scheduler 的目標可以是：

\[
\boxed{
\max_a
\frac{ESG(a\mid G_t)}{\operatorname{Cost}(a)}.
}
\]

這比單純最大化 novelty 更合理。

---

## 13. Verification-Weighted Gain

AI 可能提出一個極有趣的 hypothesis：

\[
H.
\]

但如果：

\[
\operatorname{VerifyCost}(H)
\rightarrow\infty,
\]

且沒有任何可分解的中間檢查，則短期 runtime 可能不應投入全部資源。

因此可以定義：

\[
G_V(a)
=
ESG(a)
\times
P_{\mathrm{verify}}(a),
\]

其中：

\[
P_{\mathrm{verify}}
\]

不是 theorem truth probability，而是：

> 在當前工具、預算與時間下，獲得可審核 outcome 的可行程度。

因此：

\[
\boxed{
\text{interesting but unauditable}
}
\]

與：

\[
\boxed{
\text{interesting and checkable}
}
\]

應有不同排程。

---

## 14. Disagreement as a Frontier Signal

若不同 prover / agent 對同一 claim：

\[
C
\]

給出：

\[
Y,N,U,B
\]

或不同 proof / counterexample prediction，

則 disagreement 本身是一個很好的 frontier signal。

定義：

\[
D_A(C)
=
\operatorname{Disagreement}
(
A_1(C),\ldots,A_n(C)
).
\]

若：

\[
D_A(C)\gg0,
\]

代表：

- claim 可能靠近 decision boundary；
- 定義可能不清楚；
- 某 agent 可能有錯；
- 存在 hidden assumption；
- 可能值得增加 verifier budget。

但同樣需要 importance gate：

\[
\boxed{
\text{high disagreement}
+
\text{low structural value}
}
\]

仍不必優先。

---

## 15. Exploration–Exploitation

Frontier Scheduler 必須避免兩個極端。

### 純 exploitation

永遠研究：

\[
R,G,V
\]

已知很高的熟悉區域。

結果：

\[
\text{local optimum}.
\]

### 純 exploration

永遠挑：

\[
N,U
\]

最大的陌生區域。

結果：

\[
\text{wasteful novelty chasing}.
\]

因此可以採：

\[
S'_F(q)
=
S_F(q)
+
\eta_t E(q),
\]

其中：

\[
E(q)
\]

是 exploration bonus。

隨研究成熟：

\[
\eta_t
\]

可以降低，或依 branch 自適應。

---

## 16. Research Budget

定義總預算：

\[
B
=
(
B_{\mathrm{token}},
B_{\mathrm{gpu}},
B_{\mathrm{cpu}},
B_{\mathrm{tool}},
B_{\mathrm{human}}
).
\]

不同 action 消耗不同資源：

\[
c(a)
=
(
c_1,\ldots,c_5
).
\]

scheduler 不是只解：

\[
\max S_F,
\]

而是類似：

\[
\boxed{
\max_{\mathcal A^\ast}
\sum_{a\in\mathcal A^\ast} ESG(a)
}
\]

subject to：

\[
\sum_{a\in\mathcal A^\ast}c(a)\le B.
\]

這把研究排程變成 resource-allocation problem。

---

## 17. Fast Pass / Deep Pass

可以建立兩層排程：

### Fast Pass

便宜檢查：

- canonical duplicate；
- type check；
- small counterexample search；
- cheap numerical tests；
- embedding / structure similarity；
- literature title retrieval。

目的：

\[
\text{reject obvious low-value branches}.
\]

### Deep Pass

昂貴工作：

- long proof search；
- second formal system；
- exhaustive search；
- large simulation；
- expert review；
- deep literature novelty audit。

因此：

\[
\boxed{
\text{cheap triage first}
\rightarrow
\text{expensive verification later}.
}
\]

---

## 18. Branch Dormancy

低分 branch 不需要刪除。

設：

\[
q_i
\]

目前：

\[
S_F(q_i)<\tau.
\]

可以標記：

```text
state = DORMANT
reason = low_expected_gain
```

不是：

```text
deleted = true
```

因為未來新節點：

\[
K_j
\]

可能改變它的 reuse / connectivity：

\[
R(q_i,t+1)\gg R(q_i,t).
\]

因此：

\[
\boxed{
\text{low priority now}
\neq
\text{worthless forever}.
}
\]

---

## 19. Branch Revival

若新資訊：

\[
\Delta G
\]

使 dormant branch 的 score 超過門檻：

\[
S_F(q_i\mid G_{t+1})>\tau,
\]

則：

\[
\operatorname{Revive}(q_i).
\]

revival signal 可以來自：

- 新 theorem；
- 新 counterexample；
- 新 tool；
- 新 literature；
- 新需求；
- 新硬體；
- 新 proof technique。

所以 research graph 本身是動態排程環境。

---

## 20. Stopping Criteria

AI 不應因為「還能繼續生成」就永遠研究。

對 branch \(B_i\)，可以停止當：

\[
\frac{ESG}{Cost}<\tau.
\]

或者：

\[
N_{\mathrm{new\ structure}}
\rightarrow0.
\]

或者：

\[
\text{last }k\text{ expansions}
\]

皆高度重複。

或者：

\[
\text{research objective satisfied}.
\]

停止不代表 theorem space 已窮盡。

它只表示：

\[
\boxed{
\text{marginal value under current budget is too low}.
}
\]

---

## 21. Anti-Obsession Constraint

一個 autonomous system 可能因：

- high uncertainty；
- persistent failure；
- evaluator reward；
- novelty score；

反覆卡在同一問題。

因此需要：

\[
B_{\mathrm{branch}}
\]

即每個 branch 的最大連續 budget。

若超過：

\[
B_{\mathrm{branch}}^{\max},
\]

則強制：

\[
\text{cooldown}
\]

或：

\[
\text{external review}.
\]

這不是因為問題不重要，而是防止：

\[
\boxed{
\text{research fixation}.
}
\]

---

## 22. Portfolio Scheduling

與其每輪只挑一個最高分問題，可以維持 portfolio：

\[
\mathcal F^\ast
=
\{
q_{\mathrm{safe}},
q_{\mathrm{high\ gain}},
q_{\mathrm{explore}},
q_{\mathrm{verify}},
q_{\mathrm{repair}}
\}.
\]

例如：

- 40% exploit；
- 20% verification；
- 20% exploration；
- 10% repair；
- 10% novelty audit。

比例不應永久固定，但 portfolio 可降低單一 scoring function 的偏差。

---

## 23. Scheduler 也需要被驗證

若 scheduler：

\[
S_F
\]

本身錯誤，它可以非常高效地浪費算力。

因此 scheduler 需要 log：

```text
candidate
score_components
chosen_action
predicted_gain
actual_outcome
actual_cost
downstream_reuse
```

之後比較：

\[
\widehat{ESG}
\]

與：

\[
ESG_{\mathrm{observed}}.
\]

這樣 scheduler 可以持續校準。

---

## 24. Prediction Error

定義：

\[
e_t
=
\widehat{G}_t-G_t^{\mathrm{actual}}.
\]

如果某類 action 長期：

\[
e_t\gg0,
\]

代表 scheduler 高估其價值。

例如 AI 可能持續高估「大膽 generalization」。

反之：

\[
e_t\ll0
\]

表示系統低估某類研究操作。

這使：

\[
\boxed{
\text{research strategy itself becomes learnable}.
}
\]

---

## 25. Self-Supervised Scheduler

未來可以把每次研究 action 的 downstream reuse 當成 training signal。

例如 theorem \(K_i\) 被後續：

\[
37
\]

個 proofs 使用。

則：

\[
R_{\mathrm{observed}}(K_i)=37
\]

提供一種 hindsight utility。

因此 scheduler 可以學：

\[
(K,a,G_t)
\rightarrow
\text{future structural utility}.
\]

這與「從 proof search 中抽取有用 theorem，再回饋未來 proof search」的自我演化方向高度相容。

---

## 26. 但不能只用 Downstream Reuse

若只以 reuse 次數評價 theorem：

\[
Utility(K)=\#\text{uses},
\]

會偏愛基礎常用 lemma，低估：

- 少用但深刻 theorem；
- bridge theorem；
- paradigm-changing result；
- negative result；
- contradiction discovery。

因此 utility 應是向量：

\[
\mathbf U(K)
=
(
R,
G,
N,
B,
E,
H
)
\]

例如：

- reuse；
- structural gain；
- novelty；
- bridge value；
- error-reduction value；
- human/scientific relevance。

---

## 27. Bridge Value

一個 theorem 可能只被直接使用一次，但把兩個原本分離的子圖連起：

\[
G_1
\leftrightarrow
G_2.
\]

定義 bridge value：

\[
B(K)
=
\Delta\operatorname{Connectivity}(G\mid K).
\]

這種節點可能非常值得研究。

因為它不是增加更多局部 theorem，而是：

\[
\boxed{
\text{connect previously disconnected knowledge regions}.
}
\]

---

## 28. Compression Value

如果新 lemma：

\[
L
\]

讓大量 proof：

\[
\Pi_1,\ldots,\Pi_n
\]

縮短，則可定義：

\[
C_L
=
\sum_i
\left(
|\Pi_i^{old}|
-
|\Pi_i^{new}|
\right).
\]

高 compression value 的 theorem 可能代表：

> 系統發現了一個更好的抽象。

因此 proof compression 也可以成為 frontier scoring 的正向訊號。

---

## 29. Contradiction Priority

若研究圖出現：

\[
C
\]

同時有：

\[
PROVES(C)
\]

與：

\[
REFUTES(C),
\]

或 Proof Lattice 中 checker results 衝突，

則：

\[
S_F(C,\text{resolve})
\]

應大幅提高。

因為 unresolved contradiction 可能污染大量 downstream nodes。

可以定義 impact：

\[
I_C
=
|\operatorname{Descendants}(C)|.
\]

priority：

\[
S_{\mathrm{conflict}}
\propto
I_C.
\]

因此 root-level conflict 比 leaf-level conflict 優先。

---

## 30. Dependency-Critical Scheduling

若某 open node：

\[
K
\]

被大量未完成工作依賴：

\[
\deg^+_{\mathrm{blocked}}(K)\gg0,
\]

則即使它自身 novelty 不高，也值得優先。

定義：

\[
B_L(K)
=
\#\text{blocked downstream tasks}.
\]

這就是：

\[
\boxed{
\text{bottleneck value}.
}
\]

研究排程因此不只是「最有趣問題優先」，還包括：

> 解哪個問題可以解鎖最多其他問題？

---

## 31. ScienceClaw 的 Pressure-Based Scoring

近期 agent-native science 系統已開始出現類似機制。

ScienceClaw + Infinite 允許 agents broadcast unsatisfied information needs，並由 ArtifactReactor 透過 pressure-based scoring 讓其他 agents 發現與滿足 open needs；其 mutation layer 也會處理 expanding artifact DAG 中的衝突與冗餘。

這與 Frontier Scheduling 的精神相近：

\[
\text{open need}
\rightarrow
\text{score}
\rightarrow
\text{agent allocation}.
\]

本文的差異是將 scoring 進一步作用於 BKSE 的 proposition-level action space。

---

## 32. XScientist 的 Daemon Scheduling

XScientist 將 autonomous science 明確描述為 long-running、branching、failure-prone workflow，並包含 daemon scheduling、repair、quality gating 與可重播 exploration DAG。

這同樣說明：

\[
\boxed{
\text{long-running autonomous research requires scheduling as a first-class subsystem}.
}
\]

ANRG/BKSE 可把這個 scheduler 的 decision unit 從「research job」進一步細化到：

\[
\text{epistemic frontier action}.
\]

---

## 33. 一個最小 Frontier Scheduler

第一版不需要 RL。

可以直接：

```text
for q in frontier:
    novelty      = estimate_novelty(q)
    unresolved   = estimate_unresolvedness(q)
    gain         = estimate_structural_gain(q)
    reuse        = estimate_reuse(q)
    verifiable   = estimate_verifiability(q)
    duplicate    = estimate_duplication(q)
    cost         = estimate_cost(q)

    score[q] =
        wN*novelty +
        wU*unresolved +
        wG*gain +
        wR*reuse +
        wV*verifiable -
        wD*duplicate -
        wC*cost

select portfolio(score, budget)
```

最重要的是：

\[
\boxed{
\text{all score components are logged}.
}
\]

因為之後才能校準。

---

## 34. MVP 實驗

以 Paper V 的 ANRG 為基礎。

Seed：

\[
100
\]

個已驗證 theorem。

生成：

\[
5000
\]

個 candidate frontier actions。

比較四種 scheduler：

### Random

隨機選。

### Novelty-Only

\[
S=N.
\]

### Uncertainty-Only

\[
S=U.
\]

### Multi-Objective

使用本文：

\[
S_F.
\]

在相同 budget：

\[
B
\]

下比較：

1. verified new structural nodes；
2. duplicate rate；
3. reusable lemma count；
4. downstream proof success；
5. contradiction resolution；
6. open-question resolution；
7. compute per useful node；
8. human-rated relevance。

核心假說：

\[
\boxed{
\frac{\Delta \mathcal I}{Cost}_{\mathrm{multi}}
>
\frac{\Delta \mathcal I}{Cost}_{\mathrm{random}}
}
\]

且多目標 scheduler 優於單一 novelty / uncertainty 策略。

---

## 35. 第二階段：Self-Improving Scheduler

完成 baseline 後，記錄：

\[
(q_t,\hat G_t,c_t,G_t^{actual}).
\]

訓練：

\[
f_\theta(q,G)
\rightarrow
\widehat{ESG}.
\]

之後：

\[
S_F
\]

不再完全手工。

但 rule-based safety constraints 仍保留，例如：

- unresolved root contradiction priority；
- proof-status confusion prohibition；
- branch budget cap；
- human-review-required tags；
- unknown \(\neq\) false。

所以：

\[
\boxed{
\text{learned scheduling}
+
\text{hard epistemic constraints}.
}
\]

---

## 36. 研究重要性的不可完全自動化

本文必須承認：

\[
\text{scientific importance}
\]

不是純粹 graph metric。

有些問題重要，因為：

- 人類社會需要；
- 具倫理影響；
- 解決實際疾病；
- 具有歷史意義；
- 改變整個學科視角。

這些不能全部由：

\[
degree,
reuse,
novelty
\]

推出。

因此 scheduler 可以有：

\[
H(q)
=
\text{human / community priority}.
\]

最終：

\[
S_F(q)
=
S_{\mathrm{machine}}(q)
+
w_HH(q).
\]

Machine-first 不等於 machine-value-only。

---

## 37. 研究邊界

本文不主張：

1. 存在唯一正確的 frontier score；
2. uncertainty 可以直接代表信息增益；
3. novelty 可以被完美估計；
4. downstream reuse 等於學術重要性；
5. graph connectivity 等於科學價值；
6. scheduler 可以消除所有組合爆炸；
7. dormant branch 永遠可以安全忽略；
8. learned scheduler 不會形成偏見；
9. 研究可以完全轉化為多臂 bandit 或單一 optimization problem；
10. 人類不再需要決定研究方向。

本文只主張：

\[
\boxed{
\text{finite research budget requires explicit selection policy}.
}
\]

而在 AI 能大規模生成候選之後，這個 selection policy 會成為核心研究能力。

---

## 38. 與現有工作的關係

BFS-Prover 顯示，Lean theorem proving 中即使使用相對直接的 best-first tree search，只要 state expansion 的排序、資料過濾與 policy 訓練設計得當，也可以達到很強的 proof-search 表現。這是 frontier prioritization 在單一 proof tree 中的直接實例。

LeanProgress 則把 proof progress prediction 作為 search signal，顯示「估計某個中間狀態距離成功還有多遠」可以改善 theorem-proving search。

2026 年的 *Self-Supervised Theorem Discovery in a Formal Axiomatic System* 更接近本文核心：系統在 proof search 與 useful-theorem extraction 之間循環，建立會被後續 proof 重用的 theorem library，並發現數萬個形式 theorem。這說明 theorem utility 可以透過 downstream use 被部分觀察。

ScienceClaw + Infinite 透過 pressure-based scoring 讓 agents 回應 unsatisfied information needs，並對 artifact DAG 做衝突與冗餘處理。

XScientist 則把 long-running daemon scheduling、quality gating、repair 與 exploration DAG 作為 autonomous science infrastructure 的一部分。

這些工作共同顯示：當 AI 研究從一次性答案走向長期自主運行時，「下一步做什麼」已逐漸從隱含 heuristic 變成明確的系統元件。

---

## 39. 結論

Paper I 建立：

\[
\text{Expansion}.
\]

Paper II 建立：

\[
\text{Identity}.
\]

Paper III 建立：

\[
\text{Falsification}.
\]

Paper IV 建立：

\[
\text{Proof Trust}.
\]

Paper V 建立：

\[
\text{Research Graph}.
\]

Paper VI 則加入：

\[
\boxed{
\text{Attention Allocation}.
}
\]

因此 AI-native research runtime 現在可以寫成：

\[
\boxed{
G_t
\xrightarrow{\text{generate frontier}}
F_t
\xrightarrow{\text{score}}
q^\ast
\xrightarrow{\text{execute}}
O_t
\xrightarrow{\text{verify}}
G_{t+1}.
}
\]

完整 LOOP：

\[
\boxed{
G_t
\rightarrow
F_t
\rightarrow
S_F
\rightarrow
A_t
\rightarrow
V_t
\rightarrow
G_{t+1}.
}
\]

真正的稀缺資源不再只是知識。

也不是候選問題。

而是：

\[
\boxed{
\text{verified attention}.
}
\]

也就是：

> 在有限的 token、算力、工具、人類審核與時間預算下，哪些節點值得獲得下一單位的嚴格研究注意力？

這可能成為 AI 原生數學與 AI 原生科學之間最重要的共同工程問題之一。

下一篇將作為 Series I 的第一階段收束篇：

\[
\boxed{
\text{AI-Native Knowledge Expansion Runtime}
}
\]

把 Papers I–VI 統合為可實作的 end-to-end architecture：從 seed knowledge、variation generation、error neighborhood、Proof Lattice、research graph 到 frontier scheduler，形成完整的 BKSE Runtime MVP 與實驗路線。

---

## 參考文獻

Xin, R., Xi, C., Yang, J., et al. (2025). *BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving*. arXiv:2502.03438.

Huang, S., Song, P., George, R. J., & Anandkumar, A. (2025). *LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction*. arXiv:2502.17925.

Ota, K., Osa, T., & Harada, T. (2026). *Self-Supervised Theorem Discovery in a Formal Axiomatic System*. arXiv:2606.28747.

Wang, F. Y., Marom, L., Pal, S., et al. (2026). *Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange*. arXiv:2603.14312.

Luo, J. (2026). *XScientist: A Git-Like Research Protocol for Long-Running Autonomous Scientific Discovery*. arXiv:2607.12301.

Xu, Z., Yu, X., Zhou, B., et al. (2026). *Reliable Use of Lemmas via Eligibility Reasoning and Section-Aware Reinforcement Learning*. arXiv:2602.00998.
