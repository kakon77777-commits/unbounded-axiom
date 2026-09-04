# Paper 02｜Cognitive Density Hypothesis：認知密度命題

**English Title:** *The Cognitive Density Hypothesis: A Verification-Adjusted Metric Family for Resident, Conditional, and Expandable Intelligence*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／AI 模型效率、認知架構與可否證量測研究

---

## 摘要

本文提出 **Cognitive Density Hypothesis（認知密度命題）**：對於承擔高階理解、推理、認識判斷、元認知、驗證與異質資源協調責任的 AI 系統，僅以總參數量、每 token FLOPs、benchmark accuracy 或單次 API 價格衡量模型效率，可能不足以描述其真正的認知—計算關係。當模型系統開始使用稀疏 Mixture-of-Experts、動態模型路由、外部檢索、工具、子 AI 與 adaptive test-time compute 時，「模型有多少參數」與「一次任務實際動用了多少認知資源」已不再是同一問題。

本文因此不把認知密度定義為單一固定分數，而提出一組 **verification-adjusted metric family**。其核心是先定義指定任務分布上的可驗證認知效用，再分別測量 resident capacity、active compute、context、external expansion、verification、coordination、latency、energy 與 monetary cost。本文提出：

$$
\mathbf C
=
(
C_{\mathrm{active}},
C_{\mathrm{context}},
C_{\mathrm{retrieval}},
C_{\mathrm{external}},
C_{\mathrm{verification}},
C_{\mathrm{coordination}},
C_{\mathrm{latency}},
C_{\mathrm{energy}},
C_{\mathrm{money}}
)
$$

作為成本向量，並以：

$$
Q_C(S\mid\mathcal T)
$$

表示系統 $S$ 在指定認知任務族 $\mathcal T$ 上經驗證後的有效認知品質。只有在部署情境已指定成本權重時，才將多維成本壓縮為：

$$
C_{\lambda}
=
\sum_j
\lambda_j
\widetilde C_j
$$

並定義情境化認知密度：

$$
\boxed{
\eta_C^{(\lambda)}
=
\frac{
Q_C(S\mid\mathcal T)
}{
C_{\lambda}(S\mid\mathcal T)
}
}
$$

本文進一步區分 Resident Cognitive Density、Active Cognitive Density、Verification-Adjusted Cognitive Density、Coordination Gain Density、Conditional Expert Density 與 Expansion Efficiency，避免把「小模型」、「低 FLOPs」、「低 token 數」直接等同於高認知密度。

本文主張，認知密度真正要測量的不是模型能否記得最多資訊，而是：在明確的任務、驗證與風險條件下，每單位常駐或動態計算資源能產生多少可重用、可校準、可驗證且可協調的認知能力。對 Mother AI 或 Cognitive Command Tower 類角色而言，特別重要的能力包括問題辨識、任務分解、因果推理、未知辨識、證據狀態管理、策略切換、能力邊界判斷、模型與工具選擇、驗證與結果整合。

本文同時提出十一項主要命題、九項失敗模式與八組可否證實驗。若實驗顯示認知能力無法從知識覆蓋與任務特化中穩定區分；若高認知密度模型在外部展開後的 integration tax 長期高於大型常駐模型；若 verification-adjusted utility 無法提供比傳統 accuracy／FLOPs 更穩定的架構判斷；或者 cognitive-density frontier 對模型、任務與時間高度不穩定而失去可重用性，則本文命題應被削弱。

本文不是試圖建立一個新的單一 AI 排行榜，而是提出另一個問題：

> **當智能開始可以被常駐、條件激活、外部展開與動態推理共同實現時，我們應如何量測「真正需要一直留在核心裡的認知能力」？**

**關鍵詞：** Cognitive Density、Cognitive Efficiency、Verification-Adjusted Utility、Mixture-of-Experts、Model Routing、Test-Time Compute、Mother AI、Cognitive Kernel、External Expansion、AI Efficiency、Pareto Frontier

---

# 0. 研究定位

Paper 01 提出：

$$
\boxed{
\text{Future Scaling}
\rightarrow
\text{Compute Allocation Problem}
}
$$

其核心問題不是否定 scaling，而是：

$$
\boxed{
\text{下一單位計算究竟應該放在哪裡？}
}
$$

Paper 02 進一步處理一個必要問題：

> 如果我們連「認知效率」都沒有可操作定義，就無法比較 resident model、MoE、retrieval、external worker、tool、verification 與 test-time compute 之間的資源配置。

因此本文不是模型架構實作論文，而是：

$$
\boxed{
\text{Measurement Proposition}
}
$$

其目標是建立一套足以支持後續實驗的共同量測語言。

---

# 1. 為什麼「每參數效能」不足？

最直覺的效率形式是：

$$
\eta_P
=
\frac{Q}{P}
$$

其中：

- $Q$：任務品質；
- $P$：參數量。

但這對現代 AI 系統很快失效。

第一，dense model 與 sparse MoE 的：

$$
P_{\mathrm{total}}
$$

與：

$$
P_{\mathrm{active}}
$$

不同。

第二，同一模型在不同 output length、reasoning mode 與 context length 下的 inference cost 不同。

第三，模型可以呼叫：

- retrieval；
- external model；
- tool；
- compiler；
- verifier；
- simulator。

第四，多 Agent 系統可能使用較小模型，卻付出很高 coordination cost。

第五，高準確率模型如果需要大量人工驗證，實際可部署效率可能低於較容易機械驗證的模型。

因此：

$$
\boxed{
\frac{Q}{P}
}
$$

最多是一種局部結構指標，而不是完整的系統認知效率。

---

# 2. 現有效率研究已經是多維問題

現有 LLM efficiency 研究通常同時考慮：

- memory；
- compute utilization；
- latency；
- throughput；
- energy；
- compression；
- serving architecture；
- batch geometry；
- quantization；
- attention optimization；
- MoE。

這說明：

$$
\boxed{
\text{Efficiency}
\neq
\text{One Number}
}
$$

一種技術可以降低 FLOPs，卻增加 VRAM。

另一種可以降低 latency，卻降低 throughput。

另一種可以降低 token cost，卻提高 verifier cost。

因此本文採取：

$$
\boxed{
\text{Metric Family}
+
\text{Pareto Analysis}
+
\text{Contextual Scalarization}
}
$$

而不是先定義一個全域唯一的排名分數。

---

# 3. 系統而不是單一模型是第一級量測對象

令待評估智能系統為：

$$
\boxed{
S
=
(
M,
X,
R,
T,
V,
O
)
}
$$

其中：

- $M$：resident model 或 models；
- $X$：external models / Sub-AI；
- $R$：retrieval / external memory；
- $T$：deterministic tools / execution systems；
- $V$：verification mechanisms；
- $O$：orchestration / coordination layer。

這個定義故意不假設：

$$
S=M.
$$

因為未來實際工作系統的能力可能來自：

$$
\boxed{
\text{Model}
+
\text{Context}
+
\text{External Knowledge}
+
\text{Tools}
+
\text{Other Models}
+
\text{Verification}
}
$$

因此比較 AI 架構時應該至少有兩種模式：

## 3.1 Model-only mode

只比較：

$$
M_i.
$$

## 3.2 System mode

比較：

$$
S_i.
$$

若兩者混在一起，就會發生：

> 一個模型因為能查網路而被算成「模型自己知道」；

或者：

> 一個系統因為使用較小模型就被稱為低成本，但忽略外部 Agent 與驗證成本。

本文要求二者分開報告。

---

# 4. Task Distribution：認知密度永遠是相對於任務分布

不存在無條件的：

$$
\eta_C(S).
$$

更合理是：

$$
\boxed{
\eta_C(S\mid\mathcal T)
}
$$

其中 $\mathcal T$ 是明確任務分布。

對 Mother AI 類角色，本文提出至少六個初始 task families：

$$
\mathcal T_M
=
\{
\mathcal T_I,
\mathcal T_D,
\mathcal T_R,
\mathcal T_E,
\mathcal T_V,
\mathcal T_C
\}.
$$

其中：

- $\mathcal T_I$：Interpretation，問題與意圖辨識；
- $\mathcal T_D$：Decomposition，任務分解；
- $\mathcal T_R$：Reasoning，因果、約束、反事實與關係推理；
- $\mathcal T_E$：Epistemic，已知／未知、證據、衝突與信心管理；
- $\mathcal T_V$：Verification，驗證策略與錯誤辨識；
- $\mathcal T_C$：Coordination，工具、模型與資源協調。

這不是宣稱人類或 AI 的認知只有六類。

它只是第一代 Mother-role benchmark 的可操作切分。

---

# 5. Surface Knowledge 應另外測量

若把 trivia、歷史事實、最新新聞、API 版本與冷門領域細節全部混入：

$$
Q_C,
$$

就會重新把：

$$
\text{Knowledge Coverage}
$$

偷換成：

$$
\text{Cognitive Density}.
$$

因此本文把高解析度表層知識任務另外寫為：

$$
\mathcal T_K.
$$

並分別報告：

$$
Q_C(S\mid\mathcal T_M)
$$

與：

$$
Q_K(S\mid\mathcal T_K).
$$

這不代表：

$$
Q_K
$$

不重要。

而是因為本文真正要研究：

> 一個系統能否以較少 resident surface knowledge，維持高品質核心認知，並在需要時可靠展開表層知識。

因此：

$$
\boxed{
Q_C
\neq
Q_K.
}
$$

---

# 6. Verified Cognitive Utility

單純 accuracy 有一個問題：

如果一個 AI 產生錯誤答案但無法被系統檢出，其架構風險可能遠高於一個能力稍弱、但錯誤容易被 verifier 攔下的模型。

因此令任務：

$$
t\sim\mathcal T
$$

系統輸出：

$$
o=S(t).
$$

定義 task utility：

$$
u(t,o)\in[0,1].
$$

再定義驗證狀態：

$$
v(t,o)\in[0,1].
$$

第一代可使用：

$$
v=
\begin{cases}
1,&\text{獨立 verifier 支持輸出符合 acceptance contract}\\
0,&\text{輸出未通過或無可接受驗證證據}
\end{cases}
$$

也可以在未來使用分級 evidence strength。

則 Verification-Adjusted Cognitive Utility：

$$
\boxed{
Q_V(S\mid\mathcal T)
=
\mathbb E_{t\sim\mathcal T}
\left[
u(t,S(t))
\cdot
v(t,S(t))
\right].
}
$$

這使：

$$
\text{terminal success}
$$

與：

$$
\text{verified success}
$$

不再混淆。

---

# 7. 對不可機械驗證任務怎麼辦？

不是所有認知工作都有 deterministic verifier。

因此 $v$ 不應被誤解成：

> 沒有 unit test 的工作全部算零。

本文提出 Evidence Ladder：

$$
L_V
\in
\{
0,1,2,3,4
\}
$$

可暫定為：

- $0$：self-asserted；
- $1$：second-model review；
- $2$：human review；
- $3$：source-grounded / cross-evidence validation；
- $4$：deterministic or mechanically reproducible verification。

不同 task family 可以使用不同最低 evidence threshold：

$$
\theta_V(\mathcal T_k).
$$

所以：

$$
v(t,o)
=
g(
L_V,
\theta_V,
\text{evidence quality}
).
$$

重要的是：

$$
\boxed{
\text{驗證強度必須被顯式記錄。}
}
$$

而不是把所有「看起來合理」的輸出放在同一個 accuracy bucket。

---

# 8. Core Cognitive Quality

定義各核心 task family 的 verification-adjusted score：

$$
q_k
=
Q_V(S\mid\mathcal T_k).
$$

Mother-role cognitive quality：

$$
\boxed{
Q_C
=
\sum_{k}
w_k q_k,
\qquad
\sum_k w_k=1.
}
$$

其中 $w_k$ 不應是宇宙常數。

企業 Mother AI、研究 Mother AI、coding Mother AI 與個人 AI 可以使用不同權重。

因此正式寫成：

$$
\boxed{
Q_C(S\mid\mathcal T,\mathbf w).
}
$$

這表示 Cognitive Density 是：

$$
\text{Role-Relative}
$$

而不是：

$$
\text{Universal-IQ Score}.
$$

---

# 9. 成本必須是一個向量

本文定義：

$$
\boxed{
\mathbf C
=
(
C_A,
C_X,
C_R,
C_E,
C_V,
C_O,
C_L,
C_G,
C_{\$}
)
}
$$

其中：

## 9.1 Active Compute

$$
C_A
$$

表示實際推理計算，例如：

- activated parameter proxy；
- FLOPs；
- GPU time；
- accelerator-seconds。

## 9.2 Context Cost

$$
C_X
$$

包括：

- input tokens；
- KV cache；
- long-context attention cost；
- context construction。

## 9.3 Retrieval Cost

$$
C_R
$$

包括：

- search；
- embedding；
- index；
- database；
- network；
- reranking。

## 9.4 External Intelligence Cost

$$
C_E
$$

包括：

- Sub-AI；
- external model；
- specialist model；
- API invocation。

## 9.5 Verification Cost

$$
C_V
$$

包括：

- compiler；
- tests；
- mutation；
- reviewer；
- judge；
- human verification。

## 9.6 Coordination Cost

$$
C_O
$$

包括：

- routing；
- task decomposition；
- state synchronization；
- merge；
- context translation；
- retries caused by orchestration。

## 9.7 Latency

$$
C_L
$$

因為：

$$
\$0.001
$$

但需要三分鐘，

和：

$$
\$0.01
$$

但需要三秒，

在某些服務中不是同一種效率。

## 9.8 Energy

$$
C_G
$$

用於能源與硬體研究。

## 9.9 Monetary Cost

$$
C_{\$}
$$

是實際部署最容易量化，但不一定最穩定的成本。

---

# 10. 為什麼不能直接把成本相加？

因為：

$$
1\text{ second}
+
1\text{ joule}
+
1\text{ dollar}
$$

沒有天然意義。

因此第一級報告應保留：

$$
\boxed{
(
Q_C,
\mathbf C
)
}
$$

並比較 Pareto dominance。

若系統 $S_a$ 滿足：

$$
Q_C(S_a)\ge Q_C(S_b)
$$

且所有關鍵成本：

$$
C_j(S_a)\le C_j(S_b),
$$

並至少一項嚴格更好，則：

$$
S_a
$$

支配：

$$
S_b.
$$

如果兩者互有優缺點，就不應強行說：

> A 一定比 B 更有效率。

---

# 11. Contextual Scalarization

只有在部署需求給定後，才將成本向量轉成 scalar。

先以 reference baseline $B$ 正規化：

$$
\widetilde C_j(S)
=
\frac{
C_j(S)
}{
C_j(B)
}.
$$

再給定部署權重：

$$
\boldsymbol\lambda
=
(
\lambda_1,\ldots,\lambda_n
),
\qquad
\lambda_j\ge0,
\qquad
\sum_j\lambda_j=1.
$$

定義：

$$
\boxed{
C_{\lambda}(S)
=
\sum_j
\lambda_j
\widetilde C_j(S).
}
$$

最終得到：

$$
\boxed{
\eta_C^{(\lambda)}
=
\frac{
Q_C(S)
}{
C_{\lambda}(S)
}.
}
$$

因此：

$$
\eta_C^{(\lambda_{\mathrm{mobile}})}
$$

與：

$$
\eta_C^{(\lambda_{\mathrm{datacenter}})}
$$

可以不同。

這不是缺陷。

這正是現實。

---

# 12. Resident Cognitive Density

第一個衍生指標：

$$
\boxed{
D_R
=
\frac{
Q_C
}{
P_{\mathrm{resident}}
}.
}
$$

其中：

$$
P_{\mathrm{resident}}
$$

可以是：

- resident parameter count；
- resident model bytes；
- minimum resident memory footprint。

 $D_R$ 研究的是：

> 每單位常駐模型容量承載多少核心認知能力？

它適合比較：

- dense model；
- compact model；
- MoE shared core；
- future cognitive kernel。

但它不是完整 inference efficiency。

---

# 13. Active Cognitive Density

定義：

$$
\boxed{
D_A
=
\frac{
Q_C
}{
\mathbb E[C_A]
}.
}
$$

這對 MoE 特別重要。

因為：

$$
P_{\mathrm{total}}
$$

可以非常大，但：

$$
P_{\mathrm{active}}
$$

較小。

因此同一個 MoE 可以：

$$
D_R
$$

不高，

但：

$$
D_A
$$

很高。

這兩者不能混淆。

---

# 14. Verification-Adjusted Cognitive Density

對實際工程部署，本文認為最重要的指標之一是：

$$
\boxed{
D_V
=
\frac{
Q_V
}{
C_A+C_X+C_R+C_E+C_V+C_O
}.
}
$$

若不同成本單位不可直接相加，實際使用時應改成：

$$
\boxed{
D_V^{(\lambda)}
=
\frac{
Q_V
}{
C_{\lambda}
}.
}
$$

它回答：

> 真正得到一個「可接受結果」到底花多少完整系統成本？

這比：

$$
\frac{\text{raw candidate accuracy}}{\text{token price}}
$$

更接近 Agent 系統真實效率。

---

# 15. Human Attention 必須獨立列出

便宜 AI 可能製造大量需要人類驗證的結果。

因此另外定義：

$$
C_H
=
\text{human verification time}.
$$

並建立：

$$
\boxed{
D_H
=
\frac{
Q_V
}{
C_H
}.
}
$$

這尤其適用：

- coding；
- research；
- legal；
- high-stakes analysis。

如果：

$$
C_{\mathrm{generation}}\downarrow10\times
$$

但：

$$
C_H\uparrow10\times,
$$

則系統未必真正提高 throughput。

---

# 16. Coordination Gain Density

多 Agent 系統不應因為「用了很多 AI」就被視為更智能。

令單一組件最佳品質：

$$
Q_{\max}
=
\max_i
Q_C(A_i).
$$

整體系統：

$$
Q_C(S).
$$

定義：

$$
\boxed{
G_O
=
Q_C(S)-Q_{\max}.
}
$$

如果：

$$
G_O>0,
$$

代表協作創造超過最佳單一組件的系統收益。

再除以 coordination cost：

$$
\boxed{
D_O
=
\frac{
\max(0,G_O)
}{
C_O
}.
}
$$

若：

$$
G_O<0,
$$

代表 orchestration 反而傷害整體能力。

---

# 17. External Expansion Efficiency

令 baseline core system 為：

$$
S_0.
$$

加入外部資源 $E$ 後：

$$
S_1=S_0\oplus E.
$$

能力增益：

$$
\Delta Q_E
=
Q_C(S_1)-Q_C(S_0).
$$

外部總成本：

$$
\Delta C_E
=
C_R+C_E+C_X+C_V+C_O.
$$

定義：

$$
\boxed{
\eta_E
=
\frac{
\Delta Q_E
}{
\Delta C_E
}.
}
$$

這是後續 External Expansion 研究的核心量之一。

如果：

$$
\eta_E\le0,
$$

則該 externalization 對該任務沒有價值。

---

# 18. Surface Independence Ratio

如果我們想知道某種核心認知能力到底多依賴 resident surface knowledge，可以比較：

$$
Q_C^{\mathrm{resident}}
$$

與：

$$
Q_C^{\mathrm{externalized}}.
$$

定義：

$$
\boxed{
R_S
=
\frac{
Q_C^{\mathrm{externalized}}
}{
Q_C^{\mathrm{resident}}
}.
}
$$

若：

$$
R_S\approx1,
$$

表示大量表層知識外置後，核心認知能力仍大致保持。

若：

$$
R_S\ll1,
$$

則說明：

> 我們以為是「推理核心」的能力，其實高度依賴常駐知識結構。

這是一個重要反證工具。

---

# 19. Conditional Expert Density

MoE 提供一個新的量測對象。

令：

$$
E_t
$$

為任務 $t$ 實際啟動 expert 集。

平均 active expert compute：

$$
C_{\mathrm{expert}}
=
\mathbb E_t
\left[
\sum_{e\in E_t}
c_e
\right].
$$

則：

$$
\boxed{
D_{\mathrm{MoE}}
=
\frac{
Q_C
}{
C_{\mathrm{shared}}
+
C_{\mathrm{expert}}
}.
}
$$

同時保存：

$$
P_{\mathrm{total}}
$$

與：

$$
P_{\mathrm{active}}.
$$

這讓研究可以區分：

> 模型總共擁有多少條件能力？

與：

> 每次解一個問題真正啟動多少？

---

# 20. Routing Entropy 不是能力，但很值得記錄

對 MoE router，令 expert probability：

$$
p_e(t).
$$

routing entropy：

$$
\boxed{
H_R(t)
=
-\sum_e
p_e(t)\log p_e(t).
}
$$

較低 entropy 可能表示高度集中 routing。

較高 entropy 可能表示：

- 任務需要多種能力；
- router 不確定；
- expert specialization 不清楚；
- 負載均衡機制影響 routing。

因此：

$$
H_R
$$

本身不能被解讀為：

$$
\text{cognitive quality}.
$$

但與：

$$
Q_C,
D_A,
\text{task family}
$$

共同觀察，可以成為後續 Capability Tomography 的重要信號。

---

# 21. Model Routing 與認知密度

FrugalGPT、RouteLLM、BEST-Route 等工作已經顯示：

$$
\boxed{
\text{one query}
\not\Rightarrow
\text{always call strongest model}.
}
$$

不同 query 可以在不同 cost-quality frontier 上選不同模型。

因此外部 model routing 可以視為：

$$
\boxed{
\text{Macro Conditional Compute}.
}
$$

令 router：

$$
\pi(t)\rightarrow M_i.
$$

則 routing system 的認知密度不能只看：

$$
Q(M_i).
$$

而要看：

$$
Q_C(\pi,\{M_i\})
$$

以及：

$$
C_{\mathrm{router}}
+
C_{M_i}
+
C_V.
$$

這直接銜接未來 Mother AI 的異質模型協調。

---

# 22. Test-Time Compute 與認知密度

固定 reasoning budget：

$$
b(t)=b_0
$$

通常忽略任務難度差異。

adaptive test-time compute 則允許：

$$
b(t)
=
f(
\text{difficulty},
\text{uncertainty},
\text{expected gain}
).
$$

於是可定義：

$$
\boxed{
\eta_{\mathrm{TTC}}
=
\frac{
\Delta Q_C
}{
\Delta C_{\mathrm{test}}
}.
}
$$

這個量可以回答：

> 再多想 1000 tokens 值不值得？

而不是預設：

$$
\text{more reasoning tokens}
=
\text{always better}.
$$

---

# 23. Difficulty-Conditional Cognitive Density

平均值可能隱藏真正結構。

因此將任務按難度分層：

$$
\mathcal T
=
\mathcal T^{(1)}
\cup
\cdots
\cup
\mathcal T^{(d)}.
$$

定義：

$$
\boxed{
\eta_C^{(k)}
=
\eta_C(
S\mid\mathcal T^{(k)}
).
}
$$

可能出現：

$$
\eta_C^{\mathrm{small}}
>
\eta_C^{\mathrm{large}}
$$

在簡單問題上，

但：

$$
\eta_C^{\mathrm{small}}
<
\eta_C^{\mathrm{large}}
$$

在極難問題上。

因此真正需要找的是：

$$
\boxed{
\text{Cognitive Density Crossover Point}.
}
$$

這比宣稱「小模型比較有效率」或「大模型永遠比較好」更精確。

---

# 24. Cognitive Density Frontier

對候選系統集合：

$$
\mathcal S
=
\{
S_1,\ldots,S_n
\},
$$

建立：

$$
\boxed{
\mathcal F_C
=
\operatorname{ParetoFrontier}
(
Q_C,
\mathbf C
).
}
$$

任何被其他系統在：

- quality；
- latency；
- cost；
- energy；
- verification；

同時支配的系統，都不應成為該情境的首選。

這使「最佳模型」變成：

$$
\boxed{
\text{best feasible point under constraints}
}
$$

而不是單一 leaderboard 第一名。

---

# 25. Mother Cognitive Density

本文特別定義 Mother-role 指標：

$$
\boxed{
D_M
=
\frac{
w_Iq_I+
w_Dq_D+
w_Rq_R+
w_Eq_E+
w_Vq_V+
w_Cq_C
}{
C_{\lambda}
}.
}
$$

其中 numerator 刻意不直接放：

$$
Q_K
$$

百科式表層知識覆蓋。

但 $Q_K$ 必須另外報告。

因此一個模型可能：

$$
D_M\uparrow,
\qquad
Q_K\downarrow.
$$

這對 Mother AI 可能是可接受 trade-off。

對一般 consumer chatbot 則未必。

這正是：

$$
\boxed{
\text{Role-Relative Optimization}.
}
$$

---

# 26. Epistemic Density

Mother AI 最重要的能力之一不是回答，而是：

> 知道什麼時候不應該直接回答。

因此建立：

$$
Q_E
$$

至少包含：

- unknown detection；
- contradiction detection；
- source conflict；
- uncertainty calibration；
- evidence classification；
- escalation correctness。

定義：

$$
\boxed{
D_E
=
\frac{
Q_E
}{
C_{\lambda}
}.
}
$$

一個 factual QA 很強、但永遠過度自信的模型，可能具有：

$$
Q_K\uparrow
$$

但：

$$
D_E\downarrow.
$$

對指揮塔角色而言，這是重大缺陷。

---

# 27. Meta-Cognitive Density

令：

$$
Q_M^{\mathrm{meta}}
$$

測量：

- strategy switching；
- self-check trigger；
- tool-use decision；
- delegation decision；
- stop / continue decision；
- retry / escalate decision；
- capability-boundary recognition。

則：

$$
\boxed{
D_{\mathrm{meta}}
=
\frac{
Q_M^{\mathrm{meta}}
}{
C_{\lambda}
}.
}
$$

這一項尤其適合研究：

> 一個較小但元認知很強的 Mother Model，能否有效組織比自己局部更強的外部模型？

---

# 28. 「認知密度高」不等於「自己什麼都會」

這是一個必須明確排除的誤讀。

假設：

$$
M
$$

本身 coding 能力只達：

$$
0.8,
$$

而外部 specialist：

$$
A_C
$$

達：

$$
0.95.
$$

如果 $M$ 能正確：

1. 發現 coding 任務；
2. 知道自己的邊界；
3. 選擇 $A_C$ ；
4. 建立正確 context；
5. 選擇 verifier；
6. 判斷結果是否接受；

那麼：

$$
\boxed{
Q_C(S)>Q_C(M)
}
$$

完全可能成立。

因此：

$$
\boxed{
\text{Cognitive Density}
\neq
\text{Standalone Capability Density}.
}
$$

---

# 29. 系統能力可以超過最大單體，但必須扣除組織成本

若：

$$
Q_C(S)
>
\max_i Q_C(A_i),
$$

可以稱為：

$$
\boxed{
\text{Organizational Cognitive Gain}.
}
$$

但只有當：

$$
\frac{
Q_C(S)-\max_iQ_C(A_i)
}{
C_O+C_V+C_E
}
>0
$$

才代表有正向的組織效率。

否則：

> 十個 AI 做完一個一個 AI 就能做好的任務

不能算架構進步。

---

# 30. Cognitive Density 不是壓縮比

模型壓縮可能得到：

$$
P\downarrow
$$

但同時：

$$
Q_C\downarrow\downarrow.
$$

因此：

$$
\boxed{
\text{Compression Ratio}
\neq
\text{Cognitive Density}.
}
$$

反過來，某種模型：

$$
P_{\mathrm{total}}\uparrow
$$

但：

$$
P_{\mathrm{active}}\downarrow
$$

且：

$$
Q_C\uparrow,
$$

仍可能具有更高 active cognitive density。

MoE 就是重要例子。

---

# 31. Cognitive Density 不是蒸餾成功率

傳統 distillation 常希望 student：

$$
f_S(x)
\approx
f_T(x).
$$

但本文真正關心的是：

$$
\boxed{
\text{哪些能力值得被保留？}
}
$$

而不是：

$$
\boxed{
\text{能否完整模仿 Teacher？}
}
$$

因此未來即使某 student 在：

$$
Q_K
$$

下降，

但：

$$
Q_C
$$

接近 Teacher，

也可能是成功的 Cognition-Dense Student。

這一命題將在後續 Cognitive Factorization Problem 再處理。

---

# 32. 認知密度的十一項命題

## 命題 1：參數非充分命題

$$
P_A>P_B
$$

不能推出：

$$
D_C(A)>D_C(B).
$$

---

## 命題 2：總參數—活躍參數分離命題

對 sparse conditional architecture：

$$
P_{\mathrm{total}}
\neq
P_{\mathrm{active}}.
$$

因此兩者必須分別報告。

---

## 命題 3：表層知識—核心認知分報命題

$$
Q_K
$$

與：

$$
Q_C
$$

應分別量測，避免百科記憶直接支配 Mother-role evaluation。

---

## 命題 4：驗證調整命題

若兩個系統 raw quality 相近，但其中一個錯誤更容易被獨立 verifier 攔截，則後者可以具有更高：

$$
D_V.
$$

---

## 命題 5：Human Attention Bottleneck 命題

若 AI generation cost 趨近於零，但：

$$
C_H
$$

不下降，總工作吞吐量不會無限上升。

---

## 命題 6：任務條件化命題

不存在必然全域最優的：

$$
S^\ast.
$$

更合理：

$$
S^\ast
=
S^\ast(
\mathcal T,
\mathbf C_{\max},
\mathbf w
).
$$

---

## 命題 7：動態計算優勢命題

當任務難度分布高度異質，若 difficulty estimator 足夠準確，adaptive compute allocation 可以提高平均認知密度。

---

## 命題 8：External Expansion 正效益條件

外部資源只有在：

$$
\Delta Q_E
>
\Delta C_E
$$

經相同 normalization 後成立時，才是有效 externalization。

---

## 命題 9：組織能力非免費命題

多 Agent 帶來的：

$$
G_O
$$

必須扣除：

$$
C_O+C_V+C_E.
$$

---

## 命題 10：Mother-role specialization 命題

Mother AI 的最佳模型可能不是：

$$
\arg\max_M Q_K(M),
$$

而是：

$$
\boxed{
\arg\max_M D_M(M).
}
$$

---

## 命題 11：Cognitive Density Frontier 命題

未來更合理的模型比較可能不是單一榜單，而是：

$$
\boxed{
\mathcal F_C
}
$$

即 quality—cost—latency—verification—energy 的多維 Pareto frontier。

---

# 33. 九類主要失敗模式

## 33.1 Metric Gaming

模型針對：

$$
\mathcal T_M
$$

過度訓練，得到高 $D_M$，但失去未見任務 generalization。

---

## 33.2 Knowledge Leakage

所謂 reasoning benchmark 實際被訓練資料記憶污染，使：

$$
Q_C
$$

偷帶大量：

$$
Q_K.
$$

---

## 33.3 Verifier Bias

如果：

$$
V
$$

和 generator 使用相同失敗模式，

則：

$$
Q_V
$$

會被高估。

---

## 33.4 Externalization Tax

$$
C_R+C_E+C_O+C_V
$$

可能大於節省的 resident / active compute。

---

## 33.5 Hidden Resident Dependence

移除高解析度 parametric knowledge 後，抽象推理能力本身下降。

此時：

$$
R_S\ll1.
$$

---

## 33.6 Latency Explosion

系統 monetary cost 很低，但多輪 orchestration 造成不可接受 latency。

---

## 33.7 Capability Drift

外部模型更新使：

$$
Q_C(S,t)
$$

隨時間漂移。

因此任何 density score 都需要版本與時間戳。

---

## 33.8 Over-Scalarization

把所有成本壓成：

$$
\eta_C
$$

後遺失真正的 Pareto trade-off。

因此本文要求原始：

$$
(Q_C,\mathbf C)
$$

永久保存。

---

## 33.9 Mother-Role Narrowing

過度追求 Mother-role density，使模型無法理解足夠多的世界基礎，最後變成：

$$
\boxed{
\text{High-density empty router}.
}
$$

這會重新落入既有「空殼路由器」問題。

---

# 34. 實驗 1：Dense / MoE / Routed-System 等品質成本比較

選擇同一 task suite：

$$
\mathcal T_M.
$$

比較：

1. large dense；
2. smaller dense；
3. sparse MoE；
4. smaller model + external model router；
5. Mother model + heterogeneous workers。

固定：

$$
Q_C\ge q_{\min}
$$

後比較：

$$
\mathbf C.
$$

再反過來固定成本預算：

$$
C_{\lambda}\le B
$$

比較：

$$
Q_C.
$$

兩種方向都要做，避免單邊 benchmark。

---

# 35. 實驗 2：Resident Surface Knowledge Ablation

建立兩組模型或系統：

$$
S_R
$$

偏向 parametric / resident knowledge，

以及：

$$
S_E
$$

偏向 external knowledge。

在：

$$
\mathcal T_M
$$

與：

$$
\mathcal T_K
$$

分開測量：

$$
Q_C,
Q_K,
R_S,
D_M.
$$

這可以直接測：

> 表層知識外置到底會不會連核心推理一起破壞？

---

# 36. 實驗 3：Verification Cost Crossover

對 coding、structured output、research claim 等不同 task family：

測：

$$
C_{\mathrm{generation}}
$$

與：

$$
C_V.
$$

找：

$$
\boxed{
C_V=C_{\mathrm{generation}}
}
$$

的 crossover point。

如果生成成本已經極低，而 verifier 成為主要成本，系統優化方向就應改變。

---

# 37. 實驗 4：Human Attention Crossover

同一批任務使用：

- expensive high-quality model；
- cheap worker；
- cheap worker + mechanical verifier；
- cheap worker + human reviewer。

測：

$$
Q_V,
C_{\$},
C_H,
C_L.
$$

如果：

$$
C_H
$$

主導總成本，

則「便宜 worker」本身並不足以提高系統效率。

---

# 38. 實驗 5：Difficulty-Conditional Routing

將任務按 difficulty 分桶：

$$
d_1,\ldots,d_n.
$$

比較：

1. 永遠使用 strongest model；
2. 永遠使用 cheap model；
3. strong / weak router；
4. model + variable test-time compute；
5. Mother planner + heterogeneous executors。

觀察：

$$
\eta_C^{(d)}
$$

與 crossover point。

---

# 39. 實驗 6：MoE Conditional Density

對可取得 routing telemetry 的 MoE：

記錄：

$$
P_{\mathrm{active}},
H_R,
E_t,
Q_C,
C_A.
$$

比較不同 task families。

這一實驗不直接宣稱：

$$
E_i
=
\text{某認知功能}.
$$

只建立：

$$
\boxed{
\text{Routing Fingerprint}
}
$$

作為後續 causal intervention 的輸入。

---

# 40. 實驗 7：Coordination Gain

對同一複雜任務：

比較：

$$
A_{\max}
$$

最佳單體，

與：

$$
S_{\mathrm{multi}}
$$

多 Agent 系統。

測：

$$
G_O
$$

及：

$$
D_O.
$$

如果：

$$
Q_C(S_{\mathrm{multi}})
>
Q_C(A_{\max})
$$

但：

$$
D_O\le0,
$$

則多 Agent 只是以巨大成本換取小幅能力，而不構成高密度架構。

---

# 41. 實驗 8：Mother Cognitive Density Benchmark

建立專門 benchmark：

## A. Problem Reframing

給錯誤表述問題，看 AI 是否先修正問題。

## B. Unknown Recognition

資料不足時是否拒絕假裝已知。

## C. Delegation

給不同能力 workers，看是否分配正確。

## D. Verification Selection

同一 candidate 可用不同 verifier，是否選對。

## E. Source Conflict

不同來源互相矛盾時如何處理。

## F. Capability Boundary

是否知道自己或外部 worker 已超出已驗證能力域。

## G. Stop / Escalate

是否知道繼續生成沒有價值。

這些共同形成：

$$
Q_M^{\mathrm{core}}.
$$

---

# 42. 認知密度不應是新的「AI IQ」

本文明確拒絕：

$$
\boxed{
D_C
=
\text{general intelligence scalar}.
}
$$

原因是：

1. task distribution 不同；
2. verifier 不同；
3. risk tolerance 不同；
4. deployment cost 不同；
5. model / system boundary 不同。

因此任何 Cognitive Density 報告至少要帶：

$$
(
\mathcal T,
\mathbf w,
\boldsymbol\lambda,
V,
\text{model version},
\text{system version},
t
).
$$

沒有這些 metadata 的單一分數應被視為不完整。

---

# 43. Versioned Cognitive Density

模型與外部系統會變。

因此：

$$
\boxed{
D_C
=
D_C(S,v,t\mid\mathcal T).
}
$$

其中：

- $v$：system / model version；
- $t$：測量時間。

對 external API-based architecture 尤其重要。

同一模型 alias：

$$
m_{\mathrm{latest}}
$$

在不同日期可能代表不同模型。

因此 evidence 必須綁：

$$
\boxed{
\text{Concrete Model Identity}.
}
$$

---

# 44. 認知密度與 Mother AI 自我模型

如果 Mother AI 能長期記錄：

$$
D_C(A_i,\mathcal T_k,t),
$$

它就不只是擁有 model registry。

而是逐步建立：

$$
\boxed{
\widehat{\mathcal C}_{A_i}(t)
}
$$

即對每個外部智能能力域的估計。

同樣也可以保存：

$$
\boxed{
\widehat{\mathcal C}_{M}(t)
}
$$

形成自己的能力模型。

這將在後續 Capability Boundary Tomography 中展開。

---

# 45. 認知密度與能力成熟

Paper 01 定義 Functional Maturity：

$$
\operatorname{FM}(M,\mathcal T)
\ge
\theta_{\mathcal T}.
$$

Paper 02 可以進一步說：

當：

$$
Q_C
$$

已經超過最低可用門檻時，

真正要最大化的可能變成：

$$
\boxed{
D_C
}
$$

而不是繼續只最大化：

$$
Q_C.
$$

因此可能存在兩階段：

$$
\boxed{
\text{Capability Acquisition Phase}
}
$$

與：

$$
\boxed{
\text{Cognitive Density Optimization Phase}.
}
$$

兩者不是絕對年代分界。

同一個模型對 coding 可能已進第二階段，

對 theorem proving 還在第一階段。

---

# 46. Cognitive Density Transition

定義某 task family 的 transition point：

$$
\tau_C
$$

使得在：

$$
Q_C\ge\theta_Q
$$

後，

更多 resident scaling 的：

$$
\frac{\Delta Q_C}{\Delta C_R}
$$

低於某種 alternative allocation：

$$
\max
\left\{
\frac{\Delta Q_C}{\Delta C_{\mathrm{MoE}}},
\frac{\Delta Q_C}{\Delta C_{\mathrm{TTC}}},
\frac{\Delta Q_C}{\Delta C_{\mathrm{external}}},
\frac{\Delta Q_C}{\Delta C_V}
\right\}.
$$

則稱該任務區域進入：

$$
\boxed{
\text{Cognitive Density Transition}.
}
$$

這提供 Paper 01「轉向」命題更形式化的版本。

---

# 47. 與 MoE 的關係

MoE 可以被理解為第一個非常重要的：

$$
\boxed{
\text{Conditional Capacity Architecture}.
}
$$

但 Paper 02 不主張：

$$
\text{MoE}
=
\text{Cognitive Kernel + External Experts}.
$$

目前的 expert：

- 在同一 hidden space；
- token-level routing；
- training jointly；
- function highly entangled；
- routing 受 load balancing 等因素影響。

因此它只能證明：

$$
\boxed{
\text{總容量與每次激活計算可以分離。}
}
$$

至於：

> 哪些能力真正屬於 shared core？

> 哪些可以 externalize？

需要後續 Paper 04–06。

---

# 48. 與外部模型 routing 的關係

FrugalGPT 類 cascade 與 RouteLLM 類 routing 已經提供：

$$
\boxed{
\text{model-level conditional execution}.
}
$$

它們的主要問題通常是：

> quality-cost trade-off。

本文把它再推進成：

> **認知角色—能力—驗證—成本 trade-off。**

也就是 router 不只需要知道：

$$
\text{誰比較強？}
$$

而需要逐漸知道：

$$
\boxed{
\text{誰在什麼 task family、什麼 verifier、什麼成本與什麼風險條件下最適合？}
}
$$

---

# 49. 與 Test-Time Scaling 的關係

現有研究已顯示 test-time compute allocation 與：

- task difficulty；
- model type；
- budget；
- inference strategy；

高度相關。

這支持：

$$
\boxed{
\text{固定 inference budget}
}
$$

不是唯一選擇。

認知密度框架因此把 test-time compute 視為：

$$
\boxed{
\text{動態認知資源}.
}
$$

而不是模型能力外部的附加成本。

---

# 50. 與 Cognitive Kernel 的關係

如果未來存在：

$$
K_C
$$

Cognitive Kernel，

理想上應該具有：

$$
D_M(K_C)\uparrow
$$

而不要求：

$$
Q_K(K_C)\rightarrow\max.
$$

但至少必須保持：

$$
Q_K(K_C)\ge\theta_{\mathrm{world-basis}},
$$

否則它無法理解世界或驗證外部資訊。

因此真正目標不是：

$$
\text{Zero Knowledge Core}.
$$

而是：

$$
\boxed{
\text{Minimum Sufficient World Basis}
+
\text{High Cognitive Density}.
}
$$

---

# 51. Minimum Sufficient World Basis

令：

$$
K_B
$$

為 Mother Model 常駐世界基底。

要求：

$$
\boxed{
\operatorname{Interpret}(K_B,q)
}
$$

足以支持：

- 問題辨識；
- 外部資料檢索；
- 因果基本判斷；
- cross-domain mapping；
- verifier selection；
- output sanity checking。

但不要求：

$$
K_B
=
K_{\mathrm{world}}.
$$

因此未來需要研究：

$$
\boxed{
K_B^\ast
=
\arg\min_{K_B}
|K_B|
}
$$

subject to：

$$
Q_C(K_B)\ge\theta_C.
$$

這就是「最小充分認知世界基底」問題。

---

# 52. 這個問題為什麼不能靠 pruning 直接解？

因為 neural representation 並不保證：

$$
\text{某段參數}
=
\text{某類表層知識}.
$$

知識、語言、抽象、世界模型與推理能力可能高度共享表示。

因此本文只提出：

$$
\boxed{
\text{Functional Density Target}.
}
$$

不宣稱已存在：

$$
\boxed{
\text{Clean Weight-Level Partition}.
}
$$

這個技術障礙會留給 Cognitive Factorization Problem。

---

# 53. 公開命題與未公開解法的邊界

本文公開：

- Cognitive Density metric family；
- task-family separation；
- cost vector；
- verification adjustment；
- Pareto frontier；
- resident / active / expansion / coordination density；
- falsifiable experiments。

本文不提供：

- 如何識別 frontier model 內部真正的 cognitive circuits；
- 如何把 knowledge 與 reasoning 乾淨分離；
- 如何決定 parameter-level extraction；
- 如何實際壓縮並保持 meta-cognition；
- 如何將 external expert 映射回 latent space；
- 如何重新訓練或收斂新的 Cognitive Kernel。

因此：

$$
\boxed{
\text{Measurement Architecture}
\neq
\text{Solution Architecture}.
}
$$

---

# 54. 八項優先實驗輸出

未來若要把本文從命題推向實證，第一輪至少輸出：

1. `mother_role_task_suite`;
2. `surface_knowledge_control_suite`;
3. `verification_strength_schema`;
4. `cost_vector_schema`;
5. `dense_moe_router_comparison`;
6. `difficulty_bucket_analysis`;
7. `external_expansion_cost_curve`;
8. `cognitive_density_pareto_frontier`.

每一筆結果至少綁：

$$
\boxed{
(
model,
version,
task,
evidence,
cost,
timestamp
).
}
$$

---

# 55. 什麼結果會支持本文？

以下結果會增加本命題可信度：

1. 不同模型在 $Q_K$ 相近時， $Q_C$ 與成本存在大幅差異；
2. 某些較小模型在 Mother-role task 上有接近 frontier model 的 $Q_C$ ；
3. 外部 retrieval 降低 $Q_K$ 缺口，而不嚴重破壞 $Q_C$ ；
4. MoE 在相同或更低 active compute 下維持高 $Q_C$ ；
5. dynamic routing 提高等成本 $Q_C$ ；
6. adaptive test-time compute 提高 difficulty-weighted $D_C$ ；
7. mechanical verification 顯著降低人工 $C_H$ ；
8. heterogeneous system 的 $G_O>0$ 且 $D_O>0$。

---

# 56. 什麼結果會削弱本文？

以下結果會削弱甚至否定部分命題：

1. $Q_C$ 無法和大量表層知識穩定區分；
2. 一旦降低 resident knowledge，meta-reasoning 同步崩潰；
3. 所有 external expansion 都具有極高 integration tax；
4. verification cost 永遠比大型模型直接回答更高；
5. model routing 在真實 task distribution 無穩定收益；
6. MoE routing 與能力結構完全無可利用關係；
7. Mother-role benchmark 只是在測另一種 prompt overfitting；
8. density frontier 在模型更新後完全不可重用；
9. 大型 resident model 在等總系統成本下持續支配所有 modular architecture。

若最後第 9 項長期成立，

那麼：

$$
\boxed{
\text{Largest Practical Resident Model}
}
$$

仍可能是最好的 Mother AI。

本文接受這個可能性。

---

# 57. 本文與「更強模型仍然更好」並不衝突

假設未來：

$$
M_{t+1}
$$

同時：

- reasoning 更強；
- meta-cognition 更強；
- latency 更低；
- active compute 更低；
- verification 更容易；
- context 更高效。

則：

$$
D_C(M_{t+1})
>
D_C(M_t).
$$

本文完全支持使用新模型。

真正反對的是：

$$
\boxed{
\text{只因總參數更多，就預設架構更好。}
}
$$

---

# 58. 認知密度最終研究問題

本文最後把問題濃縮成四問：

## 問題一

$$
\boxed{
\text{What cognitive capability must remain resident?}
}
$$

## 問題二

$$
\boxed{
\text{What capability can be conditionally activated?}
}
$$

## 問題三

$$
\boxed{
\text{What capability can be externally expanded?}
}
$$

## 問題四

$$
\boxed{
\text{What is the total verified cost of making them behave as one intelligence?}
}
$$

這四個問題共同決定真正的：

$$
\boxed{
\text{Cognitive Density}.
}
$$

---

# 59. 結論

大型模型的能力發展讓 AI 研究長期習慣使用：

$$
\text{parameters},
\quad
\text{FLOPs},
\quad
\text{tokens},
\quad
\text{benchmark score}
$$

描述進步。

但當 AI 系統開始同時擁有：

$$
\text{dense models}
+
\text{MoE}
+
\text{retrieval}
+
\text{external models}
+
\text{tools}
+
\text{test-time compute}
+
\text{verification},
$$

單一模型大小已不足以描述：

> 一次認知任務真正動用了多少資源，以及這些資源換回多少可靠能力。

因此本文提出：

$$
\boxed{
\text{Cognitive Density Hypothesis}.
}
$$

其核心並不是：

$$
\text{smaller is better},
$$

也不是：

$$
\text{bigger is worse}.
$$

而是：

$$
\boxed{
\text{Only useful, verified cognition should justify persistent or active computational cost.}
}
$$

對 Mother AI 尤其如此。

Mother AI 不必成為所有領域最強的單一執行者。

但它若要成為真正的 Cognitive Command Tower，就必須在有限資源下保持足夠高的：

$$
D_{\mathrm{reason}},
\quad
D_{\mathrm{epistemic}},
\quad
D_{\mathrm{meta}},
\quad
D_{\mathrm{coord}},
\quad
D_{\mathrm{verify}}.
$$

未來真正值得比較的因此不只是：

> 哪個模型最大？

而是：

> 哪個系統在指定任務、風險、驗證與資源條件下，能以最低完整成本產生最多可信且可組織的認知能力？

這將問題從：

$$
\boxed{
\text{Model Size}
}
$$

推向：

$$
\boxed{
\text{Cognitive Resource Architecture}.
}
$$

而後續 MoE、Cognitive Factorization、External Expert、Capability Tomography 與 Expandable Intelligence 的研究，都可以建立在這一量測框架上。

---

# References

1. Hoffmann, J., et al. (2022). *Training Compute-Optimal Large Language Models*. arXiv:2203.15556.
2. Fedus, W., Zoph, B., & Shazeer, N. (2021). *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*. arXiv:2101.03961.
3. Borgeaud, S., et al. (2021). *Improving Language Models by Retrieving from Trillions of Tokens*. arXiv:2112.04426.
4. Chen, L., Zaharia, M., & Zou, J. (2023). *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance*. arXiv:2305.05176.
5. Dai, D., et al. (2024). *DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models*. arXiv:2401.06066.
6. Ong, I., et al. (2024). *RouteLLM: Learning to Route LLMs with Preference Data*. arXiv:2406.18665.
7. Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*. arXiv:2408.03314.
8. Ding, D., et al. (2025). *BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute*. ICML 2025.
9. Yuan, Z., et al. (2025). *EfficientLLM: Efficiency in Large Language Models*. arXiv:2505.13840.
10. Agarwal, A., Sengupta, A., & Chakraborty, T. (2025). *The Art of Scaling Test-Time Compute for Large Language Models*. arXiv:2512.02008.
11. Zhai, Z., et al. (2026). *Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization*. arXiv:2604.14853.
12. Neo.K × Aletheia. (2026). *當 Frontier AI 基本能力逐漸成熟：從 Scaling 轉向 Cognitive Efficiency*.
13. Neo.K × Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.
14. Neo.K × Aletheia. (2026). *AI 不是流程中的一個節點：從 Agentic Workflow 到持續母 AI 的架構躍遷*.
15. Neo.K × Aletheia. (2026). *母 AI、世界狀態機與子智能網路：三向耦合的 AI 中心動態認知架構*.
16. Neo.K × Aletheia. (2026). *子 AI 是認知器官，不是獨立 Workflow*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開命題與量測架構論文。

本文不公開任何未驗證或未公開的：

- weight-level capability separation；
- cognitive circuit extraction；
- parameter remapping；
- latent-space expert linking；
- cognitive-kernel compression；
- reconvergence training method。

本文提出的是：

$$
\boxed{
\text{Measurement Architecture}
}
$$

而不是：

$$
\boxed{
\text{Private Solution Architecture}.
}
$$
