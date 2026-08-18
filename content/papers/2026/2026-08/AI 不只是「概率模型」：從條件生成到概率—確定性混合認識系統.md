---
title: "AI 不只是『概率模型』：從條件生成到概率—確定性混合認識系統"
english_title: "Beyond 'Just a Probabilistic Model': From Conditional Generation to Probabilistic–Deterministic Hybrid Epistemic Systems"
series: "AI Epistemic Reconstruction Series"
paper: "01"
author: "Neo.K"
date: "2026-08-14"
version: "v0.1"
document_type: "Research Paper / Position-and-Formalization Paper"
language: "zh-Hant"
status: "Research Draft"
---

# AI 不只是「概率模型」：從條件生成到概率—確定性混合認識系統

## Beyond “Just a Probabilistic Model”: From Conditional Generation to Probabilistic–Deterministic Hybrid Epistemic Systems

**作者：Neo.K**  
**系列：AI Epistemic Reconstruction Series — Paper 01**  
**版本：v0.1**  
**日期：2026 年 8 月 14 日**

---

## 摘要

「大型語言模型只是概率模型」是一個在局部層級可以成立、但在現代工具型 Agent 系統層級經常失去解釋力的敘述。自回歸語言模型確實可以由條件分布

$$
p_\theta(x_{t+1}\mid x_{\le t})
$$

描述其生成核心；然而，當模型被嵌入工具使用、程式執行、外部環境互動、持久狀態、驗證器與回饋迴路後，整個系統的功能已不再等同於單一條件生成器。

本文提出「**概率—確定性混合認識系統**」（Probabilistic–Deterministic Hybrid Epistemic System, PDHES）作為較完整的功能描述。其基本結構為

$$
\mathcal A=(M,T,E,S,V,\Pi),
$$

其中 $M$ 為概率生成模型， $T$ 為工具與可執行程序， $E$ 為外部環境， $S$ 為持久狀態與證據儲存， $V$ 為驗證與判定機制， $\Pi$ 為控制／調度策略。這類系統的典型認識閉環為

$$
\boxed{
\text{Probabilistic Proposal}
\rightarrow
\text{Deterministic or Externally Grounded Test}
\rightarrow
\text{Evidence}
\rightarrow
\text{Verification}
\rightarrow
\text{Epistemic Update}
}
$$

本文並不主張概率描述「錯誤」，也不主張工具使用本身足以證明意識、理解或通用智能。本文的核心主張較窄：**若研究對象是完整 Agent 的功能、研究能力與知識更新機制，單以「它是概率模型」作為充分解釋會發生層級錯置。**

本文以 PAL、ReAct、Toolformer、FunSearch、AlphaEvolve 等原始研究作為技術背景，並以一個長時半黑箱 DOS 遊戲逆向案例作為 running case study，分析模型如何使用通用先驗提出假說，再以程式、雜湊、binary diff、重新載入與外部執行結果將假說排除、保留或提升信心。最後，本文區分「可被概率形式表示」與「被概率機制充分解釋」兩件不同的事情，並提出可用於後續研究的形式化命題與實驗方向。

**關鍵詞：** Large Language Models, AI Agents, Probability, Determinism, Tool Use, External Verification, Epistemic Update, Scientific Agents, Hybrid Systems, Active Experimentation

---

# 1. 問題：一句「只是概率模型」到底說了什麼？

在當代 AI 討論中，常見一句簡化敘述：

> AI／LLM 只是概率模型。

若此句的精確意思是：

> 自回歸語言模型在生成階段計算或近似一個對下一 token 的條件分布，並據此產生輸出，

那麼這是一個合理的模型層描述。

Transformer 架構與後續大型自回歸模型的發展，使條件式序列建模成為現代語言模型的重要基礎。GPT-3 等工作亦明確位於 autoregressive language modeling 的脈絡中 [1,2]。

問題出現在「只是」二字。

如果從：

$$
M:\quad p_\theta(y\mid x)
$$

直接推論：

> 完整 AI Agent 的所有功能都可由「概率抽取文字」充分解釋，

則把至少三個不同層級混為一談：

1. **模型層（model level）**：神經網路如何生成候選；
2. **系統層（system level）**：模型如何與工具、環境、記憶、驗證器共同運作；
3. **認識層（epistemic level）**：系統如何取得新證據、排除錯誤假說並改變其可用知識狀態。

本文研究的是第二與第三層。

---

# 2. 文獻背景：現代 Agent 已經不是單一文字生成器

## 2.1 PAL：模型產生程序，Runtime 執行程序

PAL（Program-Aided Language Models）把自然語言理解與程序生成交給 LLM，但把實際求解交給 Python runtime [3]。

其基本思想可寫為：

$$
x
\xrightarrow{M}
c
\xrightarrow{\operatorname{Exec}}
y,
$$

其中 $c$ 是模型生成的程式。

這裡已存在清楚的功能分工：

- LLM 負責候選程序；
- interpreter 負責程序語義；
- 執行結果由 runtime 決定。

因此即使 $c$ 是概率生成的，

$$
y=\operatorname{Exec}(c)
$$

在固定程式、固定輸入與固定執行環境時，可以是一個完全確定的結果。

## 2.2 ReAct：推理與行動交錯

ReAct 把 reasoning traces 與 task-specific actions 交錯，使模型能主動與外部來源或環境互動，取得新的 observation，再更新後續行動 [4]。

其抽象循環為：

$$
z_t
\rightarrow
a_t
\rightarrow
o_{t+1}
\rightarrow
z_{t+1}.
$$

這與單次：

$$
x\rightarrow y
$$

已有根本差異。

模型不只是針對固定輸入生成輸出，而能透過 action 改變下一步可獲得的資訊。

## 2.3 Toolformer：模型學習何時、如何呼叫工具

Toolformer 研究模型如何決定是否呼叫 API、呼叫哪個 API、使用什麼參數，以及如何把結果重新納入後續生成 [5]。

這表示：

$$
p_\theta(\text{next token}\mid context)
$$

仍可能是模型核心，但 Agent 的有效計算路徑已包含：

$$
\text{Model}+\text{External Computation}.
$$

## 2.4 FunSearch：生成與系統性 evaluator 分離

FunSearch 將 pretrained LLM 與系統性 evaluator 結合，讓模型提出程序，再執行並評估候選，形成迭代式搜尋 [6]。

其重要結構不是單一模型輸出，而是：

$$
\boxed{
\text{Generate}
\rightarrow
\text{Execute}
\rightarrow
\text{Evaluate}
\rightarrow
\text{Select}
\rightarrow
\text{Generate}
}
$$

FunSearch 特別適用於「解很難，但候選解容易被客觀評估」的問題。

## 2.5 AlphaEvolve：LLM 候選與自動 evaluator 的大規模閉環

AlphaEvolve 進一步把 LLM 產生的程式候選、可執行 evaluator、資料庫與演化選擇整合成大型自動探索系統 [7]。

這類工作說明一個重要趨勢：

> 模型的「創造候選能力」與外部系統的「判定候選能力」可以被刻意分離。

因此現代 AI 系統的功能結構愈來愈不像：

$$
\text{Probability}\rightarrow\text{Answer},
$$

而比較像：

$$
\text{Proposal Distribution}
+
\text{Executable Constraints}
+
\text{Selection Dynamics}.
$$

---

# 3. 定義：概率—確定性混合認識系統

## Definition 1 — Probabilistic Generator

令 $M_\theta$ 為概率生成器：

$$
q_t\sim p_\theta(q\mid c_t),
$$

其中：

- $c_t$：當前 context；
- $q_t$：候選文字、程序、假說、工具呼叫或 action proposal。

## Definition 2 — Tool System

令工具集合：

$$
T=\{T_1,\ldots,T_k\}.
$$

每個工具可以是 deterministic、stochastic、partially observable 或 external-service dependent。

當某工具在固定輸入與固定執行狀態下為 deterministic 時：

$$
r_t=T_i(u_t).
$$

## Definition 3 — External Environment

令 $E$ 為模型不能任意指定輸出的外部環境，例如：

- 作業系統；
- 編譯器；
- 檔案系統；
- 模擬器；
- 遊戲；
- 真實實驗設備；
- 資料庫；
- 網路服務。

環境對 action 的回應：

$$
o_{t+1}=E(a_t,s_t).
$$

## Definition 4 — Evidence State

系統的證據狀態：

$$
K_t
$$

不等同於模型權重本身。

它可以包含：

- tool outputs；
- files；
- traces；
- hashes；
- tests；
- verified propositions；
- invalidated hypotheses；
- current frontier。

因此：

$$
K_{t+1}
=
U(K_t,o_{t+1},v_{t+1}),
$$

其中 $U$ 為 evidence update。

## Definition 5 — Verifier

令：

$$
V(h,e)\in\{\text{pass},\text{fail},\text{unknown}\}
$$

或更一般：

$$
V(h,e)\rightarrow score.
$$

Verifier 可以是：

- exact equality；
- compiler；
- unit test；
- theorem checker；
- hash comparison；
- constraint solver；
- statistical test；
- human review。

## Definition 6 — Probabilistic–Deterministic Hybrid Epistemic System

定義：

$$
\boxed{
\mathcal A=(M,T,E,S,V,\Pi)
}
$$

其中：

- $M$：生成／推理模型；
- $T$：工具集合；
- $E$：外部環境；
- $S$：持久狀態；
- $V$：驗證器；
- $\Pi$：調度與控制機制。

它的認識過程不是單一步驟，而是 trajectory：

$$
\tau=
(z_0,a_0,o_1,v_1,z_1,\ldots,z_T).
$$

---

# 4. 核心命題一：概率表示確定性，不等於概率解釋確定性

## Proposition 1 — Degenerate-Distribution Representation

對任意 deterministic function：

$$
y=f(x),
$$

皆可建立退化條件分布：

$$
P(Y=y\mid X=x)
=
\begin{cases}
1,&y=f(x),\\
0,&\text{otherwise}.
\end{cases}
$$

因此，**確定性計算可以嵌入概率形式中表示。**

但這不推出：

> $f$ 的演算法結構已被「概率」一詞充分解釋。

要知道：

$$
P(Y=f(x)\mid X=x)=1
$$

仍需要知道哪一個 $f$。

「概率為 1」描述的是結果的確定程度；它沒有自動提供：

- algorithm；
- data structure；
- runtime semantics；
- causal transition；
- computational complexity。

因此必須區分：

$$
\boxed{
\text{Probabilistic Representability}
\neq
\text{Mechanistic Sufficiency}
}
$$

---

# 5. 核心命題二：Agent 可以主動製造新的證據

令假說空間：

$$
\mathcal H_t.
$$

Agent 在時間 $t$ 選擇 action：

$$
a_t.
$$

環境返回：

$$
o_{t+1}=E(a_t).
$$

若 $o_{t+1}$ 在執行前尚不存在於任何靜態 corpus，例如：

- 新生成的 save file；
- 新的 binary diff；
- 現場實驗結果；
- 新編譯的程序輸出；

則 Agent 的有效 context 中加入的是一份**由當前互動新產生的 evidence**。

因此：

$$
K_{t+1}\supset K_t.
$$

這裡的知識增量不必來自模型參數更新。

它可以是：

$$
\boxed{
\text{In-Context / External-State Epistemic Growth}
}
$$

即：

> 模型權重不變，但系統可利用的證據狀態增加。

---

# 6. 核心命題三：精確觀測可以產生邏輯淘汰

假設：

$$
\mathcal H_t=\{h_1,\ldots,h_n\}
$$

且某 observation 是 exact。

定義：

$$
\mathcal H_{t+1}
=
\{
h\in\mathcal H_t:
h(a_t)=o_{t+1}
\}.
$$

則：

$$
\boxed{
\mathcal H_{t+1}\subseteq\mathcal H_t
}
$$

成立。

若至少一個假說與 evidence 衝突，則：

$$
|\mathcal H_{t+1}|<|\mathcal H_t|.
$$

這是一個集合約束結果，而不是純語言偏好。

真實工程可能存在 hidden variables、measurement noise、nondeterminism 與 incomplete observability。此時必須把 exact elimination 改成 confidence update。

但當 verifier 本身為 exact，例如：

```text
SHA256(fileA) == SHA256(fileB)
```

則該比較結果不是 LLM 的語言判斷。

---

# 7. Proposal 與 Judgment 的分離

本文主張，Agent 系統中最值得區分的不是簡單的：

> Probability vs Non-Probability

而是：

$$
\boxed{
\text{Proposal}
\neq
\text{Judgment}
}
$$

模型可以負責：

- 提案；
- 假說；
- 程序；
- 搜尋方向；
- 實驗選擇。

判定則可以交給：

- compiler；
- runtime；
- environment；
- evaluator；
- test suite；
- formal checker。

因此：

$$
q_t\sim M
$$

與：

$$
V(q_t)=\text{pass/fail}
$$

可以屬於不同的計算機制。

---

# 8. Running Case：半黑箱 DOS 遊戲語義逆向

## 8.1 案例定位

本節不是把單一遊戲當成普遍證明，而是提供一個具體 workflow，顯示 PDHES 結構如何出現在長時 Agent 研究中。

研究對象是一個舊 DOS 養成遊戲的特定 build。

Agent 擁有大量**通用先驗**：

- x86；
- DOS；
- little-endian；
- reverse engineering；
- save file analysis；
- scripting。

但對某個特定 save offset 的局部語義並沒有直接答案。

## 8.2 從 bit 到假說

觀察：

```text
offset 0x0334:
00 → 64
```

這不能直接推出：

```text
0x0334 = Stress
```

因為候選可以包括：

- gameplay state；
- UI temporary state；
- RNG state；
- cache；
- hidden flag；
- checksum-related field。

模型在這裡的合理角色是：

$$
M
\rightarrow
\{h_1,h_2,\ldots,h_n\}.
$$

## 8.3 確定性工具介入

Agent 可以執行：

```text
load baseline
→ perform no gameplay action
→ save
→ hash
→ byte diff
```

如果輸出檔與 baseline：

$$
SHA256(A)=SHA256(B)
$$

而且 byte-by-byte：

$$
A=B,
$$

那麼這個局部 evidence 由檔案與 deterministic comparison 產生，不是 LLM 語言自行宣告。

## 8.4 外部環境作為反駁者

另一個實驗：

```text
load baseline
→ perform one declared schedule
→ save
→ terminate
→ restart
→ reload new save
→ compare visible state
```

如果新假說預測錯誤，遊戲 runtime 可以直接給出不相容 observation。

因此：

$$
\text{Environment}
$$

不只是資料來源，也成為：

$$
\boxed{
\text{Falsification Surface}
}
$$

## 8.5 歷史資料作為 prior，而非 truth

若舊 HEX guide 提供：

```text
Stress candidate = 0x50–0x51
```

則這應當：

$$
P(h_{\mathrm{stress}})\uparrow
$$

但仍不能直接：

$$
h_{\mathrm{stress}}=\text{verified}.
$$

需要：

$$
\text{Historical Prior}
\rightarrow
\text{Local Experiment}
\rightarrow
\text{Version-Specific Verification}.
$$

此例清楚分離：

- latent／historical retrieval；
- active epistemic reconstruction。

---

# 9. 為什麼這不是「模型突然不概率了」

本文不主張工具型 Agent 使模型本體變成 deterministic symbolic AI。

恰好相反：

$$
M
$$

仍可以是一個概率模型。

真正改變的是**研究對象的層級**。

如果問：

> LLM core 怎麼產生下一 token？

概率描述仍然核心。

如果問：

> 一個長時間 Agent 怎麼提出假說、跑程式、產生新 evidence、排除錯誤與完成任務？

則：

$$
p_\theta(x_{t+1}\mid x_{\le t})
$$

只描述其中一個 component。

---

# 10. 系統層可被統一概率化，仍不取消功能分解

一個可能反駁是：

> 整個 Agent 仍可以寫成 transition kernel，所以最後還是概率系統。

這在數學上可以成立。

令：

$$
Z_t
$$

包含完整 Agent 與 environment state。

可以寫：

$$
P(Z_{t+1}\mid Z_t,A_t).
$$

deterministic transition 只是其中的 degenerate kernel。

但這種統一表示屬於**極高層抽象**。

同樣可以把 CPU、database、compiler、hash function、theorem checker 全部塞進一個 transition kernel。

代價是失去：

- 哪個 component 提案；
- 哪個 component 判定；
- 哪個結果可重現；
- 哪些錯誤來自 sampler；
- 哪些錯誤來自 environment；
- 哪些機制可被 formal verification。

因此本文區分：

$$
\boxed{
\text{Mathematical Unification}
\neq
\text{Explanatory Decomposition}
}
$$

---

# 11. 「只是概率」的三種不同版本

## Version A — 正確但狹窄

> 自回歸 LLM 的輸出核心可用條件概率分布描述。

本文接受。

## Version B — 可形式化但資訊量低

> 整個 Agent 也可以被一個概率 transition system 表示。

本文同樣不反對。

但這和說：

> 所有數位軟體都可以表示成 bit transition

一樣，並沒有提供足夠的功能分析。

## Version C — 過度推論

> 因此 Agent 沒有 genuine tool computation、external verification、stateful evidence accumulation 或 active experimentation；所有成功都只是「概率猜中」。

本文反對此推論。

因為 PAL、ReAct、FunSearch、AlphaEvolve 等系統已明確包含模型以外的執行與判定元件 [3–7]。

---

# 12. 確定性不是概率的敵人

在 PDHES 中，probabilistic 與 deterministic 不是互斥陣營。

它們可以被功能性配置：

### Probabilistic component

適合：

- open-ended proposal；
- semantic interpretation；
- hypothesis generation；
- heuristic search；
- uncertain planning。

### Deterministic component

適合：

- arithmetic；
- parsing；
- compilation；
- execution；
- hashing；
- exact diff；
- constraint checking。

### External empirical component

適合：

- observation；
- measurement；
- black-box behavior；
- runtime response。

因此：

$$
\boxed{
\text{Uncertainty}
\rightarrow
\text{Proposal}
\rightarrow
\text{Constraint}
\rightarrow
\text{Reduced Uncertainty}
}
$$

是一個自然閉環。

---

# 13. 認識論層：Agent 如何「知道自己錯了」

純文字生成最大的風險之一，是：

$$
\text{plausibility}
\neq
\text{truth}.
$$

當系統加入 external verifier：

$$
V
$$

後，可以建立：

$$
\text{Claim}
\rightarrow
\text{Test}
\rightarrow
\text{Result}.
$$

若：

$$
V(h,e)=\text{fail},
$$

則 epistemic state 應更新：

```text
hypothesis h:
  status: invalidated
```

這裡真正重要的不是模型是否「內心相信」什麼，而是系統是否保存：

- source；
- test；
- failure；
- contradiction；
- confidence transition。

因此 Agent epistemology 可以部分外部化成：

$$
\boxed{
\text{Evidence Graph}
}
$$

而不是完全存在神經網路隱狀態中。

---

# 14. 長時間 Agent 的知識不等於權重更新

長時間研究 Agent 可能持續數小時或數天，但模型參數：

$$
\theta
$$

並沒有在每個實驗後改變。

真正變動的是：

$$
K_t.
$$

所以必須區分：

### Parametric Learning

$$
\theta_t\rightarrow\theta_{t+1}
$$

### Epistemic State Accumulation

$$
K_t\rightarrow K_{t+1}
$$

### Contextual Adaptation

$$
c_t\rightarrow c_{t+1}.
$$

這三種「學習／更新」不能混稱。

---

# 15. Agent 的研究能力應如何測量？

若只測：

$$
P(\text{correct final answer}),
$$

會混合：

- memorization；
- lucky sampling；
- genuine reconstruction；
- tool use；
- hidden benchmark contamination。

因此後續應增加：

## 15.1 Evidence Novelty

結果是否包含執行當下新產生的 evidence？

## 15.2 Falsification Response

遇到反例後是否能撤回舊假說？

## 15.3 Tool Correctness

是否把 exact tool output 與 model guess 分開？

## 15.4 Hypothesis-Space Reduction

$$
|\mathcal H_0|
\rightarrow
|\mathcal H_T|.
$$

## 15.5 Cost-Normalized Information Gain

$$
\eta
=
\frac{
H(\mathcal H_0)-H(\mathcal H_T)
}{
C_{\mathrm{token}}
+
C_{\mathrm{compute}}
+
C_{\mathrm{time}}
}.
$$

這將在本系列後續論文中進一步展開。

---

# 16. 與 FunSearch / AlphaEvolve 的關係

FunSearch 已經給出一個重要模式：

$$
\text{LLM}+\text{Evaluator}.
$$

AlphaEvolve 則進一步展示：

$$
\text{LLM Proposals}
+
\text{Automated Evaluators}
+
\text{Database}
+
\text{Evolutionary Selection}.
$$

本文提出的 PDHES 不是替代這些系統，而是把其共同認識結構抽象化。

尤其在 reverse engineering、scientific agents、software engineering、mathematical search、automated experimentation 中，可以用同一個框架分析：

> 哪裡產生候選？  
> 哪裡產生新 evidence？  
> 哪裡做 exact judgment？  
> 哪裡保存 epistemic state？

---

# 17. 與「AI 是否理解」問題的界線

本文不直接回答：

> AI 是否具有意識？

也不直接證明：

> AI 具有與人類相同的理解。

本文只處理可操作的功能主張。

如果一個系統可以：

1. 提出可區分假說；
2. 選擇行動取得新 observation；
3. 使用 exact 或 empirical verifier；
4. 在證據衝突時淘汰候選；
5. 保存已驗證／已否證的狀態；
6. 用更新後的狀態選擇下一步；

那麼它具有一個可觀測的：

$$
\boxed{
\text{Epistemic Reconstruction Loop}
}
$$

是否將此功能稱為「理解」，是另一層哲學問題。

---

# 18. 反例與限制

## 18.1 Tool hallucination

模型可能錯誤理解工具輸出。

因此工具正確不代表整體 interpretation 正確。

## 18.2 Environment nondeterminism

外部環境可能有 randomness、hidden state、race condition、timing effects。

因此不能把所有不同結果都當成模型假說錯誤。

## 18.3 Verifier specification error

若 evaluator 寫錯：

$$
V_{\mathrm{bad}},
$$

則 Agent 可能對錯誤目標高度優化。

所以：

$$
\text{Verifier correctness}
$$

本身也是研究對象。

## 18.4 Historical prior contamination

如果目標答案早已存在訓練資料或公開網路，最終成功不能直接證明 active reconstruction。

因此需要：

- private variants；
- holdout mutations；
- fresh runtime evidence；

來降低 contamination。

## 18.5 Hybrid system 不等於 autonomous scientist

長時 Agent 可以自動執行大量研究勞動，但仍可能：

- 問錯問題；
- 忽略替代解釋；
- 過度搜索；
- 缺乏停止條件；
- 需要人類設定研究目的。

因此本文不把 PDHES 與「完整自主科學家」等同。

---

# 19. 可證偽預測

本框架提出幾個可實驗檢驗的預測。

## Prediction 1

在具有 exact evaluator 的任務上：

$$
M+V
$$

應比單獨：

$$
M
$$

更能維持可驗證正確性。

PAL、FunSearch、AlphaEvolve 等既有結果與此方向一致 [3,6,7]。

## Prediction 2

對 fresh black-box task，若 Agent 可主動實驗：

$$
M+T+E+V
$$

應比只讀靜態輸入：

$$
M
$$

更能恢復 target-specific semantics。

此預測適合用合成 legacy binary benchmark 測試。

## Prediction 3

若 evidence store 正確保存 invalidated hypotheses，長時間 Agent 的重複錯誤率應下降。

## Prediction 4

若移除 deterministic verifier，而只保留模型自評，對 exact computation 任務的 error propagation 應上升。

---

# 20. 一個更精確的語句

與其說：

> AI 不是概率模型。

本文建議改為：

> **現代 LLM 的生成核心可以是概率模型；但一個具有工具、環境、持久證據與驗證器的 Agent，不應被單一的「概率模型」標籤視為完整功能解釋。**

形式化：

$$
\boxed{
M_{\mathrm{probabilistic}}
\subset
\mathcal A_{\mathrm{hybrid}}
}
$$

而不是：

$$
M_{\mathrm{probabilistic}}
=
\mathcal A_{\mathrm{hybrid}}.
$$

---

# 21. 核心區分表

| 問題 | 概率模型層 | Agent 系統層 |
|---|---|---|
| 下一 token 候選 | 核心 | 一個 component |
| 工具執行 | 不負責 | Tool / Runtime |
| Hash | 不保證 exact | Deterministic tool |
| 編譯 | 不負責 | Compiler |
| 外部 observation | 無法自行決定 | Environment |
| 假說排除 | 可提出 | Verifier + Evidence |
| 長時狀態 | Context 有限 | External / Persistent state |
| 新 evidence | 主要重組既有 context | 可由 action 現場生成 |

---

# 22. 統一圖式

```text
                  ┌────────────────────┐
                  │ Probabilistic Model │
                  │ proposal / planning │
                  └──────────┬─────────┘
                             │
                             ▼
                    Candidate Action
                             │
               ┌─────────────┼─────────────┐
               ▼             ▼             ▼
          Deterministic   External      Stochastic
             Tool        Environment       Tool
               │             │             │
               └─────────────┼─────────────┘
                             ▼
                          Evidence
                             │
                             ▼
                         Verifier
                             │
                   ┌─────────┴─────────┐
                   ▼                   ▼
               Accepted            Rejected
                   │                   │
                   └─────────┬─────────┘
                             ▼
                    Epistemic State
                             │
                             └──────────→ next proposal
```

---

# 23. 結論

「LLM 是概率模型」可以是一個正確的局部描述。

但在工具型 Agent、程式輔助推理、自動科學探索與黑箱逆向等系統中，真正發生的流程通常包含：

$$
\boxed{
\text{Probability}
+
\text{Algorithms}
+
\text{Execution}
+
\text{Environment}
+
\text{Verification}
+
\text{Persistent Evidence}
}
$$

在此結構中，概率負責處理不確定性與候選生成；確定性程序負責精確運算與約束；外部環境提供模型不能自行指定的 observation；驗證器則將 proposal 轉化為可接受、可拒絕或仍未知的 epistemic state。

因此本文的最終命題不是：

$$
\text{AI}\neq\text{Probability},
$$

而是：

$$
\boxed{
\text{Probability alone is not a sufficient system-level explanation of a modern tool-using epistemic agent.}
}
$$

中文：

> **概率可以是現代 AI 的核心生成機制之一，但不是對一個能使用工具、接受外部反駁、保存證據並反覆實驗的 Agent 系統之充分功能解釋。**

這個區分使我們可以把討論從：

> 「AI 到底是不是概率？」

轉向更有研究價值的問題：

> **概率、確定性工具、外部環境與證據更新到底如何共同形成可驗證的機器研究能力？**

這也是本系列後續論文的起點。

---

# 24. 後續系列接口

Paper 02 將處理：

> **同一個 01 並不是同一個語義 01：位元、定義域、表示域與判定域。**

Paper 03 將處理：

> **AI 如何在半黑箱、局部未知的環境中，從 prior 走向 active epistemic reconstruction。**

Paper 04 將處理：

> **External Falsification：世界如何成為 Agent 的反駁器。**

Paper 05–08 則進一步處理 evidence explosion、semantic compression、research trajectory compression、repetitive epistemic labor 與 contamination-resistant black-box research benchmark。

---

# References

[1] Vaswani, A., et al. **Attention Is All You Need.** NeurIPS 2017. arXiv:1706.03762.  
https://arxiv.org/abs/1706.03762

[2] Brown, T. B., et al. **Language Models are Few-Shot Learners.** NeurIPS 2020. arXiv:2005.14165.  
https://arxiv.org/abs/2005.14165

[3] Gao, L., et al. **PAL: Program-Aided Language Models.** arXiv:2211.10435, 2022.  
https://arxiv.org/abs/2211.10435

[4] Yao, S., et al. **ReAct: Synergizing Reasoning and Acting in Language Models.** ICLR 2023. arXiv:2210.03629.  
https://arxiv.org/abs/2210.03629

[5] Schick, T., et al. **Toolformer: Language Models Can Teach Themselves to Use Tools.** NeurIPS 2023. arXiv:2302.04761.  
https://arxiv.org/abs/2302.04761

[6] Romera-Paredes, B., et al. **Mathematical discoveries from program search with large language models.** Nature 625, 468–475 (2024). DOI: 10.1038/s41586-023-06924-6.  
https://doi.org/10.1038/s41586-023-06924-6

[7] Novikov, A., et al. **AlphaEvolve: A coding agent for scientific and algorithmic discovery.** arXiv:2506.13131, 2025.  
https://arxiv.org/abs/2506.13131

[8] Luo, N., et al. **Self-Training Large Language Models for Tool-Use Without Demonstrations.** arXiv:2502.05867, 2025.  
https://arxiv.org/abs/2502.05867

[9] Wölflein, G., Ferber, D., Truhn, D., Arandjelović, O., & Kather, J. N. **LLM Agents Making Agent Tools.** arXiv:2502.11705, 2025.  
https://arxiv.org/abs/2502.11705

---

# Appendix A — Claim Classification

## External empirical grounding

由文獻支持：

- LLM 可以產生程序並由 interpreter 執行；
- LLM 可以交錯 reasoning / acting；
- LLM 可以學習或選擇工具呼叫；
- LLM proposal 可以和 automated evaluator 結合；
- iterative generate–evaluate–select 系統已被實際用於數學與演算法探索。

## 本文形式化

本文自行提出：

- PDHES 六元組；
- Proposal / Judgment separation；
- Probabilistic Representability vs Mechanistic Sufficiency；
- Epistemic State Accumulation；
- Falsification Surface；
- Hybrid Agent 的系統層解釋框架。

## Running case

PM2/DOS 逆向僅作工程案例，不作為普遍性定理的唯一證據。

## 尚待驗證

- cost-normalized information gain 是否能穩定比較不同 Agent；
- black-box semantic reconstruction benchmark 的泛化性；
- persistent invalidation memory 對長時研究效率的實際提升幅度。

---

# Appendix B — 最小 PDHES Pseudocode

```python
state = load_epistemic_state()

while not stop(state):

    proposal = model.propose(state)

    action = controller.route(proposal)

    observation = execute(action)

    verdict = verifier.evaluate(
        proposal=proposal,
        observation=observation,
        state=state
    )

    state = update(
        state=state,
        proposal=proposal,
        observation=observation,
        verdict=verdict
    )

save_epistemic_state(state)
```

重點不是這段 pseudocode 本身，而是其中至少存在三種不可混為一談的功能：

```text
model.propose()
execute()
verifier.evaluate()
```

它們共同形成完整研究閉環。
