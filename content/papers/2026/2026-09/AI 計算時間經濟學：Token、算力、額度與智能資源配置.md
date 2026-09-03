# AI 計算時間經濟學：Token、算力、額度與智能資源配置

## AI Computational Time Economics: Tokens, Compute, Quotas, and the Allocation of Intelligent Resources

**系列**：AI 互動時間與智能時間經濟學系列，第 5 篇／共 8 篇  
**文件編號**：EML-AICTE-2026-05-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／時間經濟學／Inference-Time Compute／Agent 資源配置  
**狀態**：Public Theory Draft  
**直接前置**：《互動時間拓撲：平行 Agent、偏序因果與不可約互動深度》v0.1

---

## 摘要

AI 時代的生產力討論經常把模型能力、token 額度、推理時間、工具費用、Agent 數量與最終產出混成一個模糊概念：好像只要模型更強、額度更多、推理更長，產出就必然同比增加。然而，前四篇已經證明，AI-native 工作至少必須區分意圖、互動週期、執行軌跡、總工作量與不可約因果深度。本文進一步處理下一個問題：當 token、算力、context、工具呼叫、平行 Agent 槽位、wall-clock、金錢與人類治理時間都有限時，下一單位智能計算究竟應該被配置到哪裡？

本文提出「AI 計算時間經濟學」（AI Computational Time Economics, AICTE），把 AI inference budget 理解為對未來智能計算過程的有限索取權，而非單純的文字生成配額。令系統可用資源預算為：

$$
\mathbf B_A
=
\left(
B_{\mathrm{token}},
B_{\mathrm{compute}},
B_{\mathrm{context}},
B_{\mathrm{tool}},
B_{\mathrm{parallel}},
B_{\mathrm{runtime}},
B_{\mathrm{money}},
B_{\mathrm{human}}
\right).
$$

對候選計算行動 $c_i$，其價值不能只由「可能提高多少答案品質」表示，而應至少考慮：

$$
V(c_i)
=
V_{\mathrm{completion}}
+
V_{\mathrm{evidence}}
+
V_{\mathrm{verification}}
+
V_{\mathrm{option}}
+
V_{\mathrm{knowledge}}
-
C_i
-
R_i.
$$

本文進一步提出「邊際意圖實現價值」：

$$
MIV(c_i)
=
\frac{
E[\Delta V_{\mathrm{intent}}(c_i)]
}{
E[\Delta C(c_i)]+\epsilon
},
$$

並以 shadow price／影子價格描述有限智能計算的全域稀缺程度。當某計算的邊際價值低於當期影子價格時，系統應停止、延後、降階或將資源轉移到其他任務；當驗證債務過高時，計算資源應從生成轉向 verification reserve，而不是繼續擴大名義產量。

本文區分模型能力、已配置能力與實現產能：

$$
\boxed{
\text{AI Capability}
\neq
\text{Allocated AI Capability}
\neq
\text{Realized Productivity}.
}
$$

並指出 AI 額度的經濟意義並非「可以多講多少字」，而是「在有限人類載體時間與世界歷史時間中，可額外調度多少搜尋、推理、工具、驗證、分支、重算、平行執行與世界提交」。因此，在其他條件相同時，更高額度主要擴張的是：

$$
\Omega_{\mathrm{feasible}},
$$

即原本不會被完成、現在開始進入可行集合的任務與研究路徑。

本文與 EveMissLab 既有《時間稀缺性的永恆結構》、《AI 時間槓桿的多重估值》、UCPNP、WDC-06 世界計算投資組合、個體機構化理論直接整合；並與 2026 年 adaptive test-time compute、turn-adaptive budgeting、budget-constrained tool agents、value-of-information search control 與 global shadow-price allocation 等研究形成對話。本文的核心結論是：AI 時代真正稀缺的不再只是「推理能力」，而是**能否在有限世界時間中，持續把有限智能計算配置到最值得推進的意圖、證據、驗證與世界行動上**。

**關鍵詞**：AI 時間經濟學、Test-Time Compute、Token Budget、Compute Allocation、Shadow Price、Agent Budget、Value of Information、Verification Reserve、AI Quota、可行集合、智能計算索取權

---

# 0. 核心問題

如果一個 AI 系統今天可以使用：

$$
B_A
$$

單位計算，而明天可以使用：

$$
4B_A,
$$

能否直接推論：

$$
Y_{\mathrm{tomorrow}}
=
4Y_{\mathrm{today}}?
$$

答案一般是否定的。

原因是 AI 生產不是單一線性函數，而是：

$$
Y
=
F
\left(
I,
C_A,
\mathbf B_A,
G_I,
H,
V,
K,
W
\right),
$$

其中：

- $I$：意圖品質；
- $C_A$：AI 潛在能力；
- $\mathbf B_A$：被配置的資源預算；
- $G_I$：互動與執行拓撲；
- $H$：人類治理與判斷；
- $V$：驗證能力；
- $K$：知識、記憶與可重用資本；
- $W$：外部世界、工具、制度與期限。

因此本文的問題不是：

> 更多 token 有沒有用？

而是：

> 在多維預算有限時，哪一單位計算應該投入哪一個意圖、哪一輪、哪條 branch、哪個 Agent、哪個工具、哪一個 validator，才能提高整體有效價值？

---

# 1. 從時間稀缺到計算稀缺

前置時間理論提出：

$$
\boxed{
\text{運算資源的稀缺性}
=
\text{時間稀缺性的數位化形式}.
}
$$

即使智能存在可以高速運算、平行複製、長期存在，只要：

$$
|\Omega|>1
$$

且：

$$
\mathbf B<\infty,
$$

它仍然必須選擇。

選擇：

$$
c_i
$$

等於暫時不選擇：

$$
c_j.
$$

因此：

$$
\boxed{
\text{Compute Allocation}
\text{ is a temporal choice structure}.
}
$$

這是 AI 計算時間經濟學的第一原理。

---

# 2. AI 額度不是「文字額度」

一個 AI 配額可以限制：

- reasoning tokens；
- output tokens；
- context；
- model calls；
- tool calls；
- accelerator time；
- parallel workers；
- persistent Agent runtime；
- external API；
- storage；
- memory；
- money。

因此其一般形式應是：

$$
\mathbf B_A
=
\left(
B_t,
B_c,
B_x,
B_u,
B_p,
B_r,
B_m,
B_h
\right).
$$

其中：

$$
B_t
=
\text{token budget},
$$

$$
B_c
=
\text{compute budget},
$$

$$
B_x
=
\text{context / memory budget},
$$

$$
B_u
=
\text{tool-use budget},
$$

$$
B_p
=
\text{parallelism budget},
$$

$$
B_r
=
\text{runtime budget},
$$

$$
B_m
=
\text{monetary budget},
$$

$$
B_h
=
\text{human governance budget}.
$$

所以：

$$
\boxed{
\text{Quota}
\neq
\text{Text Length Limit}.
}
$$

---

# 3. 智能計算索取權

傳統時間經濟學把貨幣理解為對他人未來時間與能力的索取權。

在 AI 時代，可以提出功能類比：

$$
\boxed{
\text{AI Quota}
\sim
\text{Claim on Future Intelligent Computation}.
}
$$

這個 claim 可能讓使用者要求 AI：

- 搜尋；
- 比較；
- 推理；
- 生成候選；
- 執行工具；
- 寫程式；
- 跑測試；
- 找反例；
- 驗證；
- 重算；
- branch；
- parallelize；
- 保存與恢復；
- commit。

因此配額的經濟價值來自：

$$
\text{future state-transition capacity}.
$$

---

# 4. 模型能力與被配置能力

令模型／Agent 的潛在能力為：

$$
C_A.
$$

令實際配置強度為：

$$
A_A
=
\operatorname{Allocate}
\left(
C_A,
\mathbf B_A,
G_I
\right).
$$

則：

$$
A_A
\le
C_A
$$

在操作性意義上表示：潛在能力未必都能在特定任務中被實現。

因此：

$$
\boxed{
\text{AI Capability}
\neq
\text{Allocated AI Capability}.
}
$$

再考慮驗證、工具、世界與人類瓶頸：

$$
Y_{\mathrm{realized}}
=
F(A_A,H,V,K,W).
$$

故：

$$
\boxed{
\text{Allocated AI Capability}
\neq
\text{Realized Productivity}.
}
$$

---

# 5. 為什麼 4 倍額度不等於 4 倍成果

若成果函數：

$$
Y(B)
$$

具有 diminishing return，則：

$$
\frac{\partial^2Y}{\partial B^2}<0
$$

在某些區間成立。

若過度推理造成負效應，甚至可能：

$$
\frac{\partial Y}{\partial B}<0.
$$

因此更高額度提供的是：

$$
\boxed{
\text{更大的可配置選擇空間},
}
$$

而不是固定倍數產出承諾。

真正問題是：

$$
\operatorname{Policy}(\mathbf B_A).
$$

---

# 6. 外部研究：Test-Time Compute 已變成 allocation problem

2026 年 adaptive test-time compute 研究已直接把問題寫成：

$$
\max
E[\mathrm{Accuracy}]
$$

subject to：

$$
E[\mathrm{Compute}]
\le
B.
$$

這意味 inference-time compute 不再只是一個固定 generation length，而是一個 constrained allocation problem。

更重要的是，不同 query 的最佳 compute 並不相同。

因此：

$$
\boxed{
\text{Uniform Budget}
\neq
\text{Optimal Budget}.
}
$$

---

# 7. 單題、跨題與跨輪三種配置

本文區分：

## 7.1 Intra-Task Allocation

在同一問題內決定：

- 是否再想；
- 是否再 sample；
- 是否 search；
- 是否 verify。

## 7.2 Inter-Task Allocation

在多個任務間配置：

$$
B_1,\ldots,B_n
$$

使：

$$
\sum_iB_i\le B_{\mathrm{total}}.
$$

## 7.3 Inter-Turn Allocation

同一長時程 Agent trajectory 中：

$$
B^{(1)},
B^{(2)},
\ldots,
B^{(T)}.
$$

前面多花一單位資源，會減少後面可用資源。

所以：

$$
\boxed{
\text{Multi-Turn Budgeting}
=
\text{Sequential Resource Allocation}.
}
$$

---

# 8. Turn-Adaptive Budget

對第 $t$ 輪：

$$
s_t
=
\text{trajectory state},
$$

budget policy：

$$
\pi_B
:
s_t
\rightarrow
b_t.
$$

需滿足：

$$
\sum_{t=1}^{T}b_t
\le
B.
$$

這意味：

> 不是每一輪都值得同樣深度。

簡單 bookkeeping turn 可能只需少量推理。

關鍵決策 turn 可能需要高額 compute。

---

# 9. Context Cost 的跨輪複利

Multi-turn 系統存在一個容易忽略的現象：

第 $t$ 輪產生的內容：

$$
y_t
$$

可能進入：

$$
Context_{t+1}.
$$

因此早期不必要的長輸出，不只消耗本輪 token，也可能增加後續：

- memory；
- bandwidth；
- attention；
- serving；
- retrieval；
- compression；

成本。

所以：

$$
\boxed{
C_{\mathrm{early\ verbosity}}
>
C_{\mathrm{local\ tokens}}
}
$$

在長 trajectory 中可能成立。

---

# 10. 不是所有 Token 都是同型資源

Raw token count 不能完整表示：

$$
\text{reasoning effort}.
$$

因為：

- 有些 token 是重複敘述；
- 有些是有效推導；
- 有些是探索；
- 有些是自我驗證；
- 有些只是格式；
- 有些可能導致 overthinking。

因此：

$$
\boxed{
\text{Token Count}
\neq
\text{Effective Cognitive Work}.
}
$$

Token 是 accounting proxy，不是智能價值本體。

---

# 11. 邊際計算價值

對候選 computation：

$$
c_i,
$$

定義預期價值增量：

$$
E[\Delta V(c_i)].
$$

定義成本：

$$
E[\Delta C(c_i)].
$$

則：

$$
MV(c_i)
=
\frac{
E[\Delta V(c_i)]
}{
E[\Delta C(c_i)]+\epsilon
}.
$$

這是最簡單的 marginal value per compute。

但本文進一步要求：

$$
\Delta V
$$

回到意圖實現，而非單純 local score。

---

# 12. 邊際意圖實現價值

定義：

$$
MIV(c_i)
=
\frac{
E[\Delta V_{\mathrm{intent}}(c_i)]
}{
E[\Delta C(c_i)]+\epsilon
}.
$$

其中：

$$
\Delta V_{\mathrm{intent}}
$$

可以包含：

- completion gain；
- evidence gain；
- verification gain；
- uncertainty reduction；
- risk reduction；
- future option gain；
- knowledge capital；
- world value。

因此：

$$
\boxed{
MIV
\neq
\text{next-token probability gain}.
}
$$

它是 task-level / intent-level 的資源配置概念。

---

# 13. Value of Information 與 Value of Computation

一個 search action：

$$
c_s
$$

可能沒有直接提高完成度，但增加 evidence：

$$
\Delta E>0.
$$

一個 validator：

$$
c_v
$$

可能沒有生成新 artifact，但降低錯誤風險：

$$
\Delta R<0.
$$

所以計算價值至少分成：

$$
V(c)
=
V_C
+
V_E
+
V_V
+
V_O
+
V_K
-
Cost
-
Risk.
$$

其中：

- $V_C$：completion；
- $V_E$：evidence；
- $V_V$：verification；
- $V_O$：option / future policy；
- $V_K$：knowledge capital。

---

# 14. Myopic Value 與 Dynamic Value

Myopic computation value：

$$
V^{myopic}(c_t)
$$

只看現在做完這一步得到多少直接收益。

Dynamic value：

$$
V^{dyn}(c_t)
=
E
\left[
V_t
+
\sum_{\tau=t+1}^{T}
\gamma^{\tau-t}V_\tau
\right].
$$

一個便宜 probe 可能：

- 本身沒有高價值；
- 卻決定是否值得啟動昂貴模型；
- 是否需要外部工具；
- 是否應該放棄某 branch；
- 是否應該要求人類決策。

所以：

$$
\boxed{
\text{Cheap Probe}
\text{ can have high option value}.
}
$$

---

# 15. Deficit-Directed Computation

與其問：

> 哪一個候選目前分數最高？

更好的問題可能是：

> 現在真正缺哪種證據或能力？

定義 epistemic deficit：

$$
\boldsymbol\delta
=
(
\delta_{run},
\delta_{ind},
\delta_{counter},
\delta_{transport},
\delta_{tail},
\delta_{unknown}
).
$$

若：

$$
\delta_{counter}\gg0,
$$

則優先反例搜尋。

若：

$$
\delta_{ind}\gg0,
$$

則優先 independent backend。

若：

$$
\delta_{transport}\gg0,
$$

則優先 external calibration。

所以：

$$
\boxed{
\text{Score-Directed Compute}
\rightarrow
\text{Deficit-Directed Compute}.
}
$$

---

# 16. 計算投資組合

定義：

$$
\Pi_t^C
=
\{
(c_1,\mathbf b_1),
\dots,
(c_m,\mathbf b_m)
\}.
$$

要求：

$$
\sum_i\mathbf b_i
\preceq
\mathbf B_t.
$$

Portfolio 可以包含：

1. main-path execution；
2. alternative hypothesis；
3. counterexample search；
4. independent verification；
5. replication；
6. calibration；
7. rare-event stress；
8. unknown exploration；
9. fidelity escalation；
10. knowledge compression；
11. tool construction；
12. human review。

因此：

$$
\boxed{
\text{Compute Portfolio}
\neq
\text{全部資源投最高分候選}.
}
$$

---

# 17. Portfolio Diversity

若所有 compute 都投入同一推理模式：

$$
c_1\sim c_2\sim\cdots\sim c_n,
$$

可能形成：

$$
\text{Compute Mode Collapse}.
$$

因此 portfolio quality 應考慮：

$$
Q_{\Pi}
=
f
(
Utility,
Diversity,
CounterCoverage,
Independence,
Latency,
Safety,
Cost
).
$$

更多 sample 不一定增加真正資訊。

---

# 18. Shadow Price of Compute

令總預算限制：

$$
\sum_i b_i
\le
B.
$$

Lagrangian：

$$
\mathcal L
=
\sum_iU_i(b_i)
-
\lambda
\left(
\sum_i b_i-B
\right).
$$

其中：

$$
\lambda
$$

是當前有限計算的 shadow price。

在內點最優條件下：

$$
U_i'(b_i)
=
\lambda.
$$

直觀上：

> 每個仍值得繼續投入的任務，其下一單位 compute 的邊際價值應大致達到同一個全域稀缺價格。

這提供跨任務資源配置的經濟學接口。

---

# 19. 非凹效用與啟動門檻

LLM reasoning utility 可能不是簡單凹函數。

有些問題在 budget 太低時：

$$
U_i(b)\approx0.
$$

超過某 threshold：

$$
b_i^\ast
$$

後才快速提高。

之後再飽和。

因此可能存在三區：

$$
\text{Strict}
\rightarrow
\text{Surge}
\rightarrow
\text{Ample}.
$$

這意味：

> 平均分配少量 budget 給所有任務，可能比集中足夠 budget 完成一部分任務更差。

---

# 20. Rational Abandonment

如果一個任務需要：

$$
b_i^\ast
$$

才能跨過有效解題 threshold，而目前總資源不足：

$$
B<b_i^\ast,
$$

則合理策略可能是：

$$
b_i=0,
$$

而不是把有限 budget 浪費在永遠達不到有效區間的 trajectory。

因此：

$$
\boxed{
\text{Abandonment}
\text{ can be an optimal allocation decision}.
}
$$

但高風險任務若涉及責任或不可拒絕義務，則不能只由經濟效率決定。

---

# 21. Overthinking 與負邊際價值

如果延長 reasoning：

$$
b
\rightarrow
b+\Delta b
$$

反而使正確答案翻成錯誤答案，則：

$$
\Delta U<0.
$$

因此：

$$
\boxed{
\text{More Thinking}
\not\Rightarrow
\text{More Value}.
}
$$

Agent runtime 需要：

$$
StopThinking
$$

而不只是：

$$
ContinueThinking.
$$

---

# 22. Early Stopping

令：

$$
MIV_t
=
\text{next-step marginal intent value}.
$$

若：

$$
MIV_t
<
\lambda_t,
$$

則可以：

- stop；
- commit；
- use current answer；
- fallback；
- transfer budget；
- ask human。

因此停止本身是資源配置動作。

---

# 23. Tool Budget 是不同市場

Tool call $u_j$ 有：

$$
Price(u_j),
$$

$$
Latency(u_j),
$$

$$
Risk(u_j),
$$

$$
SuccessProb(u_j).
$$

所以：

$$
E[V(u_j)]
=
P_{succ}V_{succ}
+
(1-P_{succ})V_{fail}
-
Price
-
Risk.
$$

當工具價格動態變化時，最優 plan 也可能改變。

因此：

$$
\boxed{
\text{Tool Planning}
=
\text{Budgeted Sequential Decision Making}.
}
$$

---

# 24. Monetary Budget 與 Compute Budget 不可完全互換

某些平台：

$$
Money
\rightarrow
MoreCompute.
$$

但不一定：

$$
1 USD =
k\text{ tokens}
$$

在所有時刻、模型、工具與方案下固定。

因為：

- price 變化；
- model tier；
- latency tier；
- quota；
- concurrency；
- cache；
- tool pricing；
- contract。

所以 monetary budget 與 compute budget 必須分欄。

---

# 25. Human Governance Budget

最容易被忽略的資源是：

$$
B_H.
$$

人類需要投入：

- intent；
- clarification；
- review；
- exception handling；
- authority；
- risk acceptance；
- final judgment。

因此完整資源限制：

$$
\sum_iT_{H,i}
\le
B_H.
$$

當 AI 產出速度大幅上升時：

$$
B_H
$$

可能成為新的瓶頸。

---

# 26. Verification Reserve

若總 AI budget 為：

$$
B_A,
$$

不應全部投入 generation。

定義：

$$
B_A
=
B_G
+
B_V
+
B_R
+
B_O,
$$

其中：

- $B_G$：generation；
- $B_V$：verification；
- $B_R$：recovery / repair；
- $B_O$：observation / external calibration。

本文提出：

$$
\boxed{
B_V
>
0
}
$$

應被視為高風險或高價值任務的基本治理要求。

---

# 27. Verification Debt 與 Compute Rebalancing

定義驗證債務：

$$
D_V
=
\sum_iw_i(1-v_i).
$$

若：

$$
\frac{dD_V}{dt}>0,
$$

表示生成速度長期高於驗證速度。

此時新增 compute 的最佳用途未必是：

$$
B_G\uparrow.
$$

可能應該：

$$
B_V\uparrow.
$$

因此：

$$
\boxed{
\text{More AI Budget}
\text{ should sometimes buy verification, not generation}.
}
$$

---

# 28. 瓶頸遷移

令：

$$
C_G
=
\text{generation capacity},
$$

$$
C_V
=
\text{verification capacity},
$$

$$
C_I
=
\text{integration capacity},
$$

$$
C_D
=
\text{diffusion capacity}.
$$

有效吞吐：

$$
Y_{\mathrm{eff}}
\lesssim
\min
(C_G,C_V,C_I,C_D).
$$

當：

$$
C_G\uparrow
$$

而其他不變，新增 generation budget 的邊際價值下降。

所以：

$$
\boxed{
\text{Optimal Budget Allocation}
\text{ follows the moving bottleneck}.
}
$$

---

# 29. 人類生理時間與 AI 計算時間

令一天可用的人類高品質治理時間：

$$
H_{\mathrm{bio}}.
$$

AI 可以在這段世界時間內執行：

$$
M
$$

單位機器計算。

若：

$$
M\uparrow,
$$

但人類 review capacity 不變，則：

$$
\frac{M}{H_{\mathrm{bio}}}
$$

上升。

這就是 AI leverage。

但當：

$$
\frac{M}{H_{\mathrm{bio}}}
$$

超過可治理範圍，系統可能產生：

- verification debt；
- integration debt；
- context debt；
- decision overload。

因此 leverage 也有治理極限。

---

# 30. Delegated Compute Block

成熟 Agent 可以形成：

$$
U(I)
\rightarrow
\boxed{
A^{(1)}
\rightarrow
A^{(2)}
\rightarrow
\cdots
\rightarrow
A^{(n)}
}
\rightarrow
U(checkpoint).
$$

令此自主區塊消耗：

$$
B_{block},
$$

人類治理時間：

$$
T_H^{gov}.
$$

可定義委任計算槓桿：

$$
\Lambda_D
=
\frac{
V_{\mathrm{effective}}(block)
}{
T_H^{gov}
}.
$$

這比「用了多少 token」更接近使用者真正關心的價值。

---

# 31. AI 額度與可行集合

對任務 $q$，若要求：

$$
C_q\le B_m,
$$

$$
T_q^H\le B_h,
$$

$$
T_q^W\le d,
$$

$$
Q_q\ge Q_{\min},
$$

則可行集合：

$$
\Omega(\mathbf B)
=
\{
q:
constraints(q,\mathbf B)=1
\}.
$$

當：

$$
\mathbf B_A
\uparrow,
$$

可能：

$$
\mu(\Omega)
\uparrow.
$$

所以更高 AI 額度最重要的價值之一可能不是：

> 把原本一件事做得更快。

而是：

> 讓原本不會被做的事第一次變成可行。

---

# 32. Feasibility Generation Value

定義：

$$
\Delta\Omega
=
\Omega_A
\setminus
\Omega_{baseline}.
$$

對新增可行任務：

$$
q\in\Delta\Omega,
$$

其價值：

$$
V_{\mathrm{FG}}
=
\sum_{q\in\Delta\Omega}
p_qV_q.
$$

這就是可行性生成價值。

它不能被誤寫成：

$$
\text{現金節省}.
$$

但也不能被當成零。

---

# 33. 20X 類現象的抽象化

假設方案：

$$
L
$$

提供較低 budget，

方案：

$$
H
$$

提供：

$$
\mathbf B_H
>
\mathbf B_L.
$$

理論上比較不應只看：

$$
Price_H-Price_L.
$$

而應估：

$$
\Delta V
=
V(\Omega_H)
-
V(\Omega_L)
+
V_{\tau}
+
V_K
-
\Delta Cost
-
\Delta Risk.
$$

如果新增 budget 使一批重要任務：

$$
q_1,\ldots,q_n
$$

從不可行變可行，價值可能遠大於單純「每次回答長一點」。

反之，若主要瓶頸已經是人類驗證，增額可能價值很低。

---

# 34. 邊際方案升級判準

對較高方案額外成本：

$$
\Delta M,
$$

額外有效價值：

$$
\Delta V_{\mathrm{eff}},
$$

則最簡判準：

$$
Upgrade
=
\mathbb I
\left[
E[\Delta V_{\mathrm{eff}}]
>
\Delta M
\right].
$$

但：

$$
\Delta V_{\mathrm{eff}}
$$

必須包含：

- 新增可行任務；
- 曆時壓縮；
- 人類時間釋放；
- 知識資本；
- 驗證負荷；
- 風險。

不能只以名義 token 數計算。

---

# 35. Shadow Price 與個人／組織階段

當公司現金有限時：

$$
\lambda_{money}
$$

高。

當人類時間更稀缺時：

$$
\lambda_{human}
$$

高。

當大型 Agent 系統的 compute 很稀缺：

$$
\lambda_{compute}
$$

高。

因此同一 AI 方案在不同企業階段的最佳選擇不同。

所以：

$$
\boxed{
\text{AI Plan Value}
\text{ is state-dependent}.
}
$$

不存在脫離資本、時間、任務與瓶頸的普遍「最划算方案」。

---

# 36. 多專案 Compute Portfolio

若同時有：

$$
Project_1,\ldots,Project_n,
$$

則：

$$
\sum_i\mathbf B_i
\preceq
\mathbf B_{\mathrm{org}}.
$$

組織需決定：

- 哪些 project 加速；
- 哪些 project 維持；
- 哪些 project 暫停；
- 哪些 project 只做 cheap probe；
- 哪些 project 進入 verification；
- 哪些 project 值得開平行 Agent。

這是：

$$
\boxed{
\text{Machine-Time Portfolio Allocation}.
}
$$

---

# 37. 跨專案的邊際價值

最簡策略是每次把下一單位 budget 給：

$$
i^\ast
=
\arg\max_iMIV_i.
$$

但有：

- threshold；
- fixed startup cost；
- dependency；
- deadline；
- fairness；
- risk；
- option value；

時，greedy 不一定全域最佳。

因此實際上可能需要：

- dynamic programming；
- constrained MDP；
- bandit；
- portfolio optimization；
- rule-based governor；
- hybrid Agent manager。

---

# 38. 任務價值不只由成功率決定

兩個任務：

$$
q_1,
q_2
$$

可能成功率相同，但：

$$
V(q_1)\gg V(q_2).
$$

因此 compute allocator 不應只追求：

$$
Accuracy.
$$

而應最大化：

$$
ExpectedIntentValue.
$$

這對企業、研究與治理任務尤其重要。

---

# 39. Deadline 與 World Time

令世界 deadline：

$$
d_q.
$$

即使某計算具有高最終價值，如果：

$$
T(c)>d_q,
$$

也可能失去實際價值。

因此：

$$
V(c)
=
V(c\mid t_W,d_q).
$$

時間經濟學中的「成果提前存在」在 AI 系統中尤其重要。

---

# 40. 曆時與總 Compute

兩個方案可能：

### A

$$
W_A=1000
$$

compute units，

$$
\tau_A=10.
$$

### B

$$
W_B=300
$$

compute units，

$$
\tau_B=30.
$$

A 使用更多總工作但更快完成。

所以：

$$
\boxed{
\text{Compute Economy}
\neq
\text{Latency Economy}.
}
$$

兩者可能衝突。

---

# 41. Energy 與 Infrastructure Cost

若擴展至完整社會成本，compute 還包括：

$$
C_{\mathrm{energy}},
$$

$$
C_{\mathrm{hardware}},
$$

$$
C_{\mathrm{cooling}},
$$

$$
C_{\mathrm{network}},
$$

$$
C_{\mathrm{storage}}.
$$

本文不在 v0.1 建立精確能源模型，但要求：

> 大規模 AI 時間經濟分析不能永遠把 machine time 視為免費背景。

---

# 42. Precomputation 與歷史外部化

今天一次便宜 query 可能依賴：

- pretraining；
- index；
- cache；
- memory；
- tool；
- knowledge base；
- compiler；
- benchmark；
- prior failed runs。

因此即時成本：

$$
C_{\mathrm{online}}
$$

不能自動代表完整 lifecycle cost。

應區分：

$$
C_{\mathrm{build}},
$$

$$
C_{\mathrm{precompute}},
$$

$$
C_{\mathrm{online}},
$$

$$
C_{\mathrm{maintain}}.
$$

這也與「歷史外部化補償」直接相容。

---

# 43. Knowledge Capital

如果一次計算產生：

- reusable prompt；
- ontology；
- validator；
- code；
- cache；
- index；
- memory；
- benchmark；
- failure record；

則未來成本：

$$
C_{t+1}
$$

可能下降。

所以：

$$
\Delta K>0
$$

應被視為資本形成。

因此：

$$
\boxed{
\text{Compute Consumption}
\text{ can create future compute capital}.
}
$$

---

# 44. Compute Capitalization Rate

定義：

$$
\rho_K
=
\frac{
\Delta K_{\mathrm{reusable}}
}{
C_{\mathrm{compute}}
}.
$$

高：

$$
\rho_K
$$

表示本輪計算不只消耗資源，也形成可降低未來成本的資產。

這是一次性問答與機構型 Agent 系統的重大差異。

---

# 45. Budget Debt

如果系統持續超額消耗：

$$
B_t>B_t^{plan},
$$

可以形成 budget debt：

$$
D_B(t)
=
\sum_{\tau\le t}
\max(0,B_\tau-B_\tau^{plan}).
$$

若平台採硬 quota，債務會以：

- 未來不可用；
- 降速；
- 額外費用；
- 任務延遲；

形式顯現。

若採軟 monetary billing，則轉化為 cash-flow risk。

---

# 46. Token Hoarding 與 Underthinking

過度節省也可能失敗。

若：

$$
B_i<B_i^{min},
$$

使：

$$
P_{success}\downarrow,
$$

則：

$$
\text{Underthinking}
$$

同樣是配置錯誤。

所以 optimal policy 必須避開：

$$
\text{Overthinking}
$$

與：

$$
\text{Underthinking}.
$$

---

# 47. Budget Robustness

一個成熟 Agent 應在不同 budget 下 graceful degradation。

定義：

$$
Q(B).
$$

希望：

$$
B_1<B_2
$$

時，較低 budget 仍能：

- 提供部分結果；
- 保存進度；
- 顯示未完成；
- 避免虛假完成；
- 產生可恢復 checkpoint。

所以：

$$
\boxed{
\text{Budget Exhaustion}
\neq
\text{False Completion}.
}
$$

---

# 48. Anytime Intelligence

若任務可在任意 budget 截止時提供目前最佳可用結果：

$$
O(B),
$$

且：

$$
Quality(O(B))
$$

通常隨 budget 改善，則可視為 anytime agent。

這對真實 deadline 與動態 quota 特別重要。

---

# 49. Budget-Aware Stop State

Run 結束原因至少應區分：

```text
SUCCESS
BUDGET_EXHAUSTED
DEADLINE_REACHED
MARGINAL_VALUE_LOW
WAITING_FOR_HUMAN
WAITING_FOR_EXTERNAL_EVENT
RISK_BLOCKED
FAILED
CANCELLED
```

因此：

$$
\boxed{
\text{Stopped}
\neq
\text{Failed}
\neq
\text{Completed}.
}
$$

---

# 50. 第一代 AI Compute Ledger

```text
AIComputeLedger
  allocation_id
  intent_id
  project_id
  run_id
  event_id
  model
  tool
  budget_class
  token_budget
  compute_budget
  context_budget
  tool_budget
  parallel_slots
  runtime_budget
  money_budget
  human_budget
  budget_before
  budget_after
  expected_completion_gain
  expected_evidence_gain
  expected_verification_gain
  expected_option_gain
  expected_knowledge_gain
  expected_risk_change
  expected_value
  realized_value
  marginal_intent_value
  shadow_price
  verification_reserve
  debt_state
  stop_reason
  world_deadline
  provenance_ref
```

---

# 51. 第一代核心指標

本文提出：

$$
MIV
=
\text{Marginal Intent Value per Compute},
$$

$$
\lambda_C
=
\text{Compute Shadow Price},
$$

$$
\rho_K
=
\text{Compute Capitalization Rate},
$$

$$
D_V
=
\text{Verification Debt},
$$

$$
D_B
=
\text{Budget Debt},
$$

$$
\Lambda_D
=
\text{Delegation Leverage},
$$

$$
\Lambda_\Omega
=
\text{Feasibility-Set Leverage}.
$$

其中：

$$
\Lambda_\Omega
=
\frac{
\mu(\Omega_A)
}{
\mu(\Omega_{baseline})
}.
$$

---

# 52. 可檢驗命題

## 命題一：Uniform Allocation 劣化命題

存在混合難度任務集，使 adaptive allocation 在等總 budget 下優於 uniform allocation：

$$
V_{adaptive}
>
V_{uniform}.
$$

## 命題二：Overthinking 命題

存在任務區間，使：

$$
\frac{\partial V}{\partial B}<0.
$$

## 命題三：Verification Rebalancing 命題

當：

$$
D_V
$$

超過某臨界區，新增 budget 配置至 verification 的有效價值高於配置至 generation。

## 命題四：Feasibility Expansion 命題

存在任務：

$$
q
\notin
\Omega(B_1)
$$

但：

$$
q\in
\Omega(B_2),
\qquad
B_2>B_1.
$$

因此新增 budget 可以創造新可行任務，而非只縮短既有任務。

## 命題五：Human Bottleneck 命題

當：

$$
B_A\uparrow
$$

而：

$$
B_H
$$

固定，存在區間使：

$$
Y_{\mathrm{effective}}
$$

不再同比增加。

## 命題六：Portfolio Dominance 命題

在相同總 budget 下，具 evidence diversity、counterexample coverage 與 verification reserve 的 portfolio 可優於只追最高分候選的 allocation。

---

# 53. 實驗設計

## 53.1 多額度同任務

固定：

- intent；
- model；
- tools；
- evaluator。

改變：

$$
B
\in
\{B_1,B_2,B_3,B_4\}.
$$

測：

$$
Completion,
Quality,
Tokens,
Latency,
ToolCalls,
D_V,
\Delta K.
$$

## 53.2 多輪 Budget Allocation

固定 global token budget。

比較：

- uniform；
- difficulty heuristic；
- history-aware adaptive；
- full-plan allocation。

## 53.3 Generation vs Verification

固定總 budget：

$$
B=B_G+B_V.
$$

掃描不同：

$$
\frac{B_V}{B}
$$

找 effective output 最大區域。

## 53.4 Multi-Project Portfolio

建立多個：

- 高價值高難度；
- 低價值低難度；
- 高風險；
- knowledge-capital task。

比較 greedy、uniform、portfolio allocation。

## 53.5 Upgrade Threshold

比較低額與高額方案，測新增 budget 實際造成：

$$
\Delta\Omega,
\Delta T_H,
\Delta\tau,
\Delta K,
\Delta D_V.
$$

---

# 54. 與 UCPNP 的接口

UCPNP 已要求每個能力 claim 明確揭露：

$$
\mathbf B_t
=
\text{resource budget},
$$

以及：

$$
\mathbf C_t
=
\text{cost ledger}.
$$

並分離 completion、verification、certification frontier。

AICTE 因此可被理解為：

$$
\boxed{
\text{UCPNP resource ledger 的時間經濟學與 allocation 層}.
}
$$

UCPNP 問：

> 哪些 intervention 改變 agent-relative tractability frontier？

AICTE 再問：

> 在有限 budget 下，哪個 intervention 現在最值得買？

---

# 55. 與 WDC-06 的接口

WDC-06 已建立：

$$
\Pi_t^W
=
\{
(c_i,b_i)
\},
$$

與：

$$
\sum_i\mathbf b_i
\preceq
\mathbf B_t^G.
$$

並要求 allocation 同時考慮：

- utility；
- evidence diversity；
- counterexample；
- dependence；
- transport；
- latency；
- safety；
- compute cost。

AICTE 將此從「世界計算」推廣到一般：

$$
\boxed{
\text{Intelligent Computation Portfolio}.
}
$$

---

# 56. 與個體機構化的接口

個體機構化的生產函數已包含：

$$
I_H,
J_H,
A_P,
K,
W,
V,
D
$$

以及 orchestration、platform 與 risk cost。

AICTE 提供其中：

$$
A_P
$$

的 allocation theory。

即：

> AI 平行產能不是一個靜態數字，而是一個需要被持續分配的稀缺資產。

---

# 57. 與第 6 篇的接口

本文處理：

> 有多少 AI 計算，以及應該花在哪裡？

下一篇將處理：

> 當 AI 可以長時間自行消耗這些 budget 時，人類究竟要多久介入一次？哪些 checkpoint 可以放權？哪些必須由人類保留？

因此第 6 篇將建立：

$$
\rho_H
=
\text{Human Intervention Density},
$$

以及：

$$
\Lambda_D
=
\text{Delegation Leverage}.
$$

即：

# **委任時間論**

---

# 58. 規範與倫理邊界

AI 計算時間經濟學不應被用來：

1. 把所有價值都化約成金錢；
2. 把人類休息視為低效資源浪費；
3. 為追求 ROI 而取消必要安全驗證；
4. 把高 compute 誤認為高智慧；
5. 把低 token 誤認為高效率；
6. 把未驗證的大量生成當有效生產力；
7. 用 shadow price 自動決定不可商品化的人格、權利與尊嚴問題；
8. 因高額度存在就鼓勵無限制 Agent 執行；
9. 忽略能源、硬體與平台權力；
10. 把特定產品方案的商業配額誤寫成普遍物理單位。

---

# 59. 理論限制

第一，token、FLOPs、GPU-seconds、工具價格與 wall-clock 並非穩定可互換單位。

第二， $MIV$ 需要 task-relative value function，不存在已證明的通用唯一標準。

第三，shadow-price 模型在非凹效用、threshold、fixed cost 與離散 tool actions 下可能需要更複雜最佳化。

第四，使用者與組織的價值函數本身可能不完整、動態或不可量化。

第五，人類治理成本不能單純等價成機器成本。

第六，本文仍是一般理論框架，而非特定 AI 平台付費方案的採購建議。

---

# 60. 結論

AI 時代的額度問題，表面上像是：

> 我可以多用多少 token？

實際上更接近：

$$
\boxed{
\text{我可以在有限世界時間裡，多索取多少智能計算過程？}
}
$$

而真正困難的問題則是：

$$
\boxed{
\text{這些智能計算應該被配置到哪裡？}
}
$$

本文因此把 AI inference、Agent 工具、multi-turn reasoning、verification 與 multi-project orchestration 統一為一個有限資源配置問題。

其基本狀態是：

$$
\mathbf B_A
=
(
B_{\mathrm{token}},
B_{\mathrm{compute}},
B_{\mathrm{context}},
B_{\mathrm{tool}},
B_{\mathrm{parallel}},
B_{\mathrm{runtime}},
B_{\mathrm{money}},
B_{\mathrm{human}}
).
$$

其基本選擇是：

$$
\Pi_t^C
=
\{(c_i,\mathbf b_i)\}.
$$

其核心比較量是：

$$
MIV(c_i)
=
\frac{
E[\Delta V_{\mathrm{intent}}(c_i)]
}{
E[\Delta C(c_i)]+\epsilon
}.
$$

其全域稀缺訊號則可由：

$$
\lambda_C
$$

表示。

因此：

$$
\boxed{
\text{更多 AI 能力}
\neq
\text{更多已配置能力}
\neq
\text{更多有效產能}.
}
$$

而 AI 時代真正成熟的 Agent manager，不只是讓模型「多想」，而是知道：

- 何時該多想；
- 哪一輪值得多想；
- 哪個任務值得多想；
- 哪個 branch 值得繼續；
- 何時應該驗證；
- 何時應該停止；
- 何時應該把 budget 留給未來；
- 何時應該把控制權交還人類。

所以 AI 計算時間經濟學的最簡核心可以寫成：

$$
\boxed{
\text{有限智能計算}
+
\text{有限人類時間}
+
\text{不可逆世界時間}
\rightarrow
\text{最值得實現的意圖配置問題}.
}
$$

---

# 參考文獻與前置理論

## EveMissLab 前置理論

1. Neo.K，《互動時間論：從鐘錶時間到意圖驅動的智能狀態轉換》v0.1，EveMissLab，2026。
2. Neo.K，《意圖週期論：使用者意圖、AI 接受、執行與結果的閉環結構》v0.1，EveMissLab，2026。
3. Neo.K，《單輪不是一步：AI Turn、內部迴圈、工具動作與執行軌跡》v0.1，EveMissLab，2026。
4. Neo.K，《互動時間拓撲：平行 Agent、偏序因果與不可約互動深度》v0.1，EveMissLab，2026。
5. Neo.K，《時間稀缺性的永恆結構：從生命有限到選擇排他》，EveMissLab，2026。
6. Neo.K，《AI 時間槓桿的多重估值：從避免成本、曆時壓縮到可行集合擴張》，EveMissLab，2026。
7. Neo.K，《WDC-06：Which Worlds Deserve Computation》，EveMissLab，2026。
8. Neo.K with Aletheia，《UCPNP Unified Theory》v0.1，EveMissLab，2026。
9. Neo.K，《個體機構化：AI 增幅型單核複合機構與人數產能脫鉤》，EveMissLab，2026。

## 外部研究

10. Snell, C., Lee, J., Xu, K., Kumar, A. *Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters*. arXiv:2408.03314.
11. Zhai, Z., Li, B., Xiao, B., Li, M., Wang, X. *Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization*. arXiv:2604.14853, 2026.
12. Jali, N., Nayak, A., Joshi, G. *Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning in Agents*. arXiv:2604.05164v3, 2026.
13. Liu, H., Tian, C., An, N., Wang, Z., Lu, P., Yu, C., Qi, Q. *Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use*. arXiv:2602.11541, 2026.
14. *Inference-Time Budget Control for LLM Search Agents*. arXiv:2605.05701, 2026.
15. *The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs*. arXiv:2606.03092, 2026.
16. Zhou, S., Ling, R., Chen, J., et al. *When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling*. arXiv:2604.10739, 2026.
17. Chen, W.-L., Peng, L., Tan, T., et al. *Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens*. arXiv:2602.13517v2, 2026.
18. Hariri, M., et al. *Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility*. arXiv:2608.04001, 2026.

---

## 一句話版本

> **AI 額度不是可以多生成多少文字，而是對未來智能計算過程的有限索取權；真正的能力則在於把這些有限計算配置到邊際意圖價值最高、且不留下不可承受驗證與治理債務的位置。**

---

*EML-AICTE-2026-05-v0.1*  
*AI 互動時間與智能時間經濟學系列 05/08*
