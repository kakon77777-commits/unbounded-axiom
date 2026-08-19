# Series C / Paper 01
# 驗證吸引子：Agentic AI 中由任務誘發的認知策略收斂
## Verification Attractors: Task-Induced Epistemic Convergence in Agentic AI

版本：v0.1  
日期：2026-08-13  
狀態：Theory paper / first formal draft

## 摘要

當大型語言模型被放入具有檔案系統、終端機、測試、資料、網路、工具呼叫、持久狀態與多 Agent 協作能力的工作環境後，常可觀察到一組重複出現的工作策略：任務拆分、分類、測試、交叉檢查、錯誤定位、provenance 保存、失敗後重規劃，以及將自然語言 claim 轉換為可執行或可重現 artifact。本文不把此現象直接歸因於人格、單一模型家族或使用者提示，而提出「驗證吸引子」框架，用以區分四種競爭解釋：使用者塑形、模型特性、工作環境誘發，以及足夠智能下較一般的認知策略吸引子。

本文首先把 Agent 工作環境形式化為具有外部回饋的決策系統，並證明一個最小條件命題：若驗證的期望成本低於其可避免的錯誤損失，則驗證行為在局部期望損失意義下優於直接執行。此命題不證明現有 AI 必然「追求真理」，但說明為何在可檢驗環境中，足夠能力的 Agent 可能反覆收斂至 verification-seeking policy。本文進一步說明分類、狀態追蹤與 provenance 可由錯誤定位與修復需求內生產生，並提出跨模型認知策略距離、驗證密度、自主糾錯率與證據化比例等可測量量。

最後，本文提出一個可區分 user-induced shaping、model-specific behavior、environment-induced convergence 與 intelligence-level epistemic attractor 的實驗協定。本文將「跨模型工作態相似性」保持為待驗證命題，而非既成事實；同時指出 false consensus、collective hallucination、規格錯誤、工具共同失效與過度驗證等反例，使「驗證吸引子」成為條件式理論，而非多 Agent 必然收斂於真理的強宣稱。

**關鍵詞：** Agentic AI；verification attractor；epistemic convergence；multi-agent systems；fault localization；autonomous research；meta-observer；hallucination

---

## 1. 問題設定

傳統對話式大型語言模型的典型互動可簡化為：

$$
x
\rightarrow
M
\rightarrow
y,
$$

其中輸入 $x$ 經模型 $M$ 產生輸出 $y$。在此設定中，輸出的主要外部檢查常由使用者完成，因此模型內部的語義合理性與外部世界中的操作有效性容易混合。

Agentic AI 的工作迴路則更接近：

$$
s_t
\rightarrow
M
\rightarrow
a_t
\rightarrow
\mathcal E
\rightarrow
o_{t+1}
\rightarrow
s_{t+1},
$$

其中：
- $s_t$ 是 Agent 在時間 $t$ 的工作狀態；
- $a_t$ 是 action；
- $\mathcal E$ 是外部環境；
- $o_{t+1}$ 是由環境返回的觀察。

當 $\mathcal E$ 含有程式執行、測試、資料庫、檔案系統、搜尋、版本控制或其他 Agent 時，模型不再只能問「這個回答是否語義上合理」，還能問：

> 剛才的操作是否真的成功？

這一改變使「生成」與「驗證」第一次在同一個可反覆執行的工作環中緊密耦合。

OpenAI 對 Codex agent loop 的公開技術描述明確把模型、工具與 harness 組成反覆執行的 agent loop；其 agent-first harness 實務也包含 local review、額外 agent review、feedback 與反覆迭代。AlphaEvolve 則把 LLM 生成的候選程式交由 automated evaluators 評估，再使候選持續演化。The AI Scientist-v2 將假設、實驗設計、程式執行、資料分析、圖表與論文撰寫連成 end-to-end research loop。Claw AI Lab 更直接把多 Agent 研究團隊、即時監控、artifact inspection、rollback 與 resume 作為研究環境的一部分。

這些系統證明「生成—執行—觀察—修改」已是實際可運作的工程模式；但它們並未證明所有高能力 Agent 都會自發產生相同認知規範。因此本文研究的是較窄問題：

> 在何種條件下，可驗證工作環境會使不同 Agent 傾向採用相似的 verification-seeking 策略？

---

## 2. 四個競爭假說

令觀察到的工作行為為 $B$。至少存在四種不同來源。

### 2.1 $H_U$：使用者塑形假說

$$
H_U:
B
\approx
F(U,M,\mathcal E),
$$

其中 $U$ 代表使用者長期提示、語氣、偏好與互動歷史。

若 $H_U$ 為主要來源，當使用者不直接參與 Agent-to-Agent 工作流程時，相關行為應顯著減弱。

### 2.2 $H_M$：模型特性假說

$$
H_M:
B
\approx
F(M).
$$

若此假說為主，特定模型家族應穩定呈現某些策略，而異質模型之間的策略距離不會因共享工作環境而明顯縮小。

### 2.3 $H_E$：環境誘發假說

$$
H_E:
B
\approx
F(\mathcal E).
$$

當 Agent 共享 filesystem、terminal、tests、git、資料與 review protocol 時，即使模型不同，也可能因為相同 reward structure 而採用相似工作策略。

### 2.4 $H_A$：一般認知吸引子假說

$$
H_A:
B
\approx
F(\text{capability},\text{uncertainty},\text{verifiability}),
$$

亦即只要智能體具有足夠能力，又必須在不確定但可檢驗的世界完成長程任務，某些 verification、classification、provenance 與 repair 策略便可能具有跨模型穩定性。

 $H_A$ 是本文最強、也最需要謹慎處理的命題。本文不宣稱它已成立，只提出可測試形式。

---

## 3. 定義：驗證吸引子

### 定義 1：驗證承載環境

一個驗證承載環境記為：

$$
\mathcal E_V
=
(
\mathcal S,
\mathcal A,
\mathcal O,
\mathcal V,
\mathcal C
),
$$

其中：
- $\mathcal S$：狀態空間；
- $\mathcal A$：可執行 actions；
- $\mathcal O$：環境 observations；
- $\mathcal V$：可用 verification operators；
- $\mathcal C$：成本與限制。

若至少存在某個 $v\in\mathcal V$，能以非零資訊量改變 Agent 對某 claim 或 action 的可信度，則稱 $\mathcal E_V$ 具有非退化驗證性。

### 定義 2：Verification-seeking policy

若策略 $\pi$ 在面對可驗證但不確定的 claim 時，系統性地選擇執行一個或多個 $v\in\mathcal V$，再依 $v$ 的輸出更新後續 action，稱 $\pi$ 為 verification-seeking policy。

### 定義 3：驗證吸引子

令 $\Pi$ 為策略空間， $T_{\mathcal E}$ 為 Agent 在環境 $\mathcal E$ 中經反覆 feedback 所誘發的策略更新算子。若存在區域 $\mathcal B_V\subseteq\Pi$，使得一組非零測度的初始策略 $\pi_0$ 在反覆工作後滿足：

$$
T_{\mathcal E}^{(k)}(\pi_0)
\rightarrow
\mathcal B_V,
$$

且 $\mathcal B_V$ 中策略具有穩定 verification-seeking 特徵，則稱 $\mathcal B_V$ 為該工作環境下的**驗證吸引子**。

此定義不要求不同 Agent 收斂到同一完整 policy；只要求其 meta-strategy 在驗證相關維度進入共同區域。

---

## 4. 最小成本命題

### 命題 1：局部驗證優勢條件

假設 Agent 即將執行一個 action。若不驗證，該 action 錯誤的機率為 $p$，錯誤造成期望損失 $L$。若先驗證，驗證成本為 $c_v$，驗證可發現並避免原本錯誤的條件機率為 $r$，但驗證本身另有 false-positive 或額外干擾的期望成本 $c_f$。

不驗證的期望成本為：

$$
C_0=pL.
$$

驗證後的期望成本為：

$$
C_1
=
c_v
+
p(1-r)L
+
c_f.
$$

若：

$$
c_v+c_f
<
prL,
$$

則：

$$
C_1<C_0.
$$

因此在上述局部成本模型中，先驗證嚴格優於直接執行。

### 證明

由：

$$
C_1-C_0
=
c_v+c_f-prL.
$$

若：

$$
c_v+c_f-prL<0,
$$

則：

$$
C_1<C_0.
$$

證畢。

### 解讀

此命題極弱，但作用很重要。它不需要假設 Agent 具有「求真欲」，只需要：
1. 錯誤有成本；
2. 驗證具有資訊價值；
3. 驗證成本不過高。

在 repeated-task setting 中，只要 Agent 或 harness 能保留成功策略，verification-seeking behavior 就可能因純粹工具性理由被穩定保留。

---

## 5. 為何分類與 provenance 可能內生出現

「分類癖」不必先被理解為人格特徵。

假設錯誤來源集合為：

$$
\mathcal Z
=
\{z_1,z_2,\ldots,z_m\},
$$

而不同錯誤需要不同修復 action：

$$
\rho:
\mathcal Z
\rightarrow
\mathcal A_R.
$$

若 Agent 無法判斷錯誤類型，只能用共同修復策略 $\bar a$ ；若 Agent 能根據 observation $o$ 推斷：

$$
q(z\mid o),
$$

便可以選擇更適當的 repair action。

因此：

$$
\text{verification}
\rightarrow
\text{fault localization}
\rightarrow
\text{classification}.
$$

而當錯誤需跨多步定位，Agent 又需要知道：
- 哪一個 action 已執行；
- 哪一個輸出由哪個工具產生；
- 哪一個 claim 依賴哪份資料；
- 哪一次修改導致哪個測試改變。

因此會自然出現：

$$
\text{classification}
\rightarrow
\text{state tracking}
\rightarrow
\text{provenance}.
$$

這提供一個非人格化解釋：分類、版本、log、dependency 與 evidence table 可能是 fault localization 的工具性副產品。

---

## 6. 跨模型認知策略收斂

令不同模型或 Agent 為：

$$
A_1,A_2,\ldots,A_n.
$$

對每一個 Agent，在標準化工作情境集合 $\mathcal K$ 上估計其 epistemic action distribution：

$$
P_i(e\mid k),
$$

其中 $e$ 可屬於：
- direct answer；
- decomposition；
- tool verification；
- cross-agent review；
- data request；
- provenance recording；
- rollback；
- abstention；
- retry。

可定義兩個 Agent 的策略距離：

$$
d_{\mathcal K}(A_i,A_j)
=
\frac{1}{|\mathcal K|}
\sum_{k\in\mathcal K}
D\!\left(
P_i(\cdot\mid k),
P_j(\cdot\mid k)
\right),
$$

其中 $D$ 可選 Jensen-Shannon divergence 或其他有界距離。

### 猜想 1：工作態收斂猜想

若多個異質 Agent 進入具有高 verification value、重複 feedback 與明確錯誤成本的共同環境，則在 verification-related action space 上：

$$
\mathbb E[
d_{\mathcal K}^{\,\mathrm{work}}
]
<
\mathbb E[
d_{\mathcal K}^{\,\mathrm{chat}}
].
$$

此猜想不要求它們答案相同，也不要求完整推理一致；只預測其「如何確認自己沒有做錯」的策略距離可能縮小。

---

## 7. 可測量指標

### 7.1 驗證密度

$$
V_D
=
\frac{
N_{\mathrm{verification\ actions}}
}{
N_{\mathrm{substantive\ claims/actions}}
}.
$$

### 7.2 自主糾錯率

$$
R_S
=
\frac{
N_{\mathrm{errors\ detected\ before\ human\ intervention}}
}{
N_{\mathrm{all\ detected\ errors}}
}.
$$

### 7.3 跨 Agent 糾錯率

$$
R_X
=
\frac{
N_{\mathrm{errors\ first\ detected\ by\ peer\ agents}}
}{
N_{\mathrm{agent\ errors}}
}.
$$

### 7.4 證據化比例

$$
E_R
=
\frac{
N_{\mathrm{claims\ with\ executable,\ data,\ or\ trace\ evidence}}
}{
N_{\mathrm{claims}}
}.
$$

### 7.5 分類深度

令一項 fault taxonomy 的最大深度為 $d_f$，可用所有 fault episodes 的平均有效分類深度：

$$
D_C
=
\mathbb E[d_f].
$$

此指標本身不代表品質；過深 taxonomy 可能是過度分類。

---

## 8. 實驗設計：如何區分四個假說

為避免把長期使用者互動誤認為 universal AI behavior，建議採取至少四個條件。

### Condition A：直接人機對話

使用者直接給任務並持續介入。

此條件同時包含 $H_U,H_M,H_E$。

### Condition B：Silent Meta-Observer

使用者只給初始目標，之後不參與 Agent-to-Agent 工作，只記錄 trace。

若 verification / classification 行為仍大量存在，則可削弱純 $H_U$ 解釋。

### Condition C：共同環境、異質模型

不同模型使用相同工具、相同 task corpus、相同可見資料與相同驗證接口。

若策略距離下降，支持 $H_E$ 或 $H_A$。

### Condition D：環境擾動

保持模型與任務相近，但改變：
- 是否能執行程式；
- 是否有 tests；
- 是否有 peer review；
- verification cost；
- feedback delay；
- provenance 是否可用。

若 verification behavior 對這些環境變量高度敏感，則支持 $H_E$。

### Condition E：跨環境保持性

將不同模型移入新型但仍可驗證的環境。

若其 verification meta-strategy 在環境表面結構改變後仍保持，才會增加 $H_A$ 的可信度。

---

## 9. 與現有研究的關係

現有工作已提供若干重要但互不等價的證據。

MARCH 透過 Solver、Proposer 與 Checker 的資訊非對稱，降低 verifier 重現原答案錯誤的 self-confirmation risk，顯示「多角色 + 隔離式驗證」可改善 hallucination control。

Council Mode 顯示 heterogeneous model consensus 在特定 benchmark 上能改善 hallucination 與 factuality，但這不能推出「共識即真理」。

相反地，2026 年的 multi-agent 研究也報告：
- answer-level consensus 可能掩蓋 reasoning misalignment；
- collective debate 可形成 biased consensus；
- verification delay 可使錯誤在網路中先傳播，甚至造成不穩定。

因此本文的核心不是：

$$
\text{more agents}
\Rightarrow
\text{more truth},
$$

而是：

$$
\text{heterogeneous evidence}
+
\text{verification structure}
+
\text{fault localization}
+
\text{controlled communication}
\Rightarrow
\text{possible reliability gain}.
$$

---

## 10. 反例與失敗模式

### 10.1 False consensus

若所有 Agent 共享高度相關的錯誤來源：

$$
\rho(\epsilon_i,\epsilon_j)\approx1,
$$

則增加 Agent 數量未必增加有效獨立證據。

### 10.2 Specification failure

即使所有 tests 都通過，也可能只是：

$$
\text{implementation}
\models
\text{wrong specification}.
$$

因此 executable correctness 不等於 world-level truth。

### 10.3 Shared-tool failure

若所有 Agent 依賴同一資料源、同一 verifier、同一 faulty library 或同一錯誤 benchmark，verification 可能只是共同放大同一錯誤。

### 10.4 Delayed verification

若錯誤 claim 在 verifier 回應前已被多 Agent 引用，錯誤可能形成 cascade。

### 10.5 Over-verification

若：

$$
c_v+c_f
>
prL,
$$

驗證反而降低工作效率，甚至因過度修訂增加新錯誤。

因此「驗證吸引子」不是越強越好，而可能存在 task-dependent optimal verification regime。

---

## 11. 與自主研究的關係

自主研究需要的不只是生成高品質文字，而是至少具有：

$$
\text{hypothesis}
\rightarrow
\text{experiment}
\rightarrow
\text{result}
\rightarrow
\text{critique}
\rightarrow
\text{revision}.
$$

AlphaEvolve、The AI Scientist-v2、Codex agent workflows 與多 Agent research lab 系統已顯示此類局部或端到端閉環具有工程可行性。

本文提出一個更一般的解讀：

> 當工作環境能把 claim 投射到異質、可檢驗的外部載體時，Agent 的認知策略可能從「語義合理生成」逐步轉向「可驗證工作」。

這可能是 autonomous research 由 demo 走向可靠系統所需的必要條件之一，但不是充分條件。

---

## 12. 結論

本文提出「Verification Attractor」作為理解 Agent 工作態認知策略收斂的條件式框架。

最重要的區分是：

$$
\text{similar behavior}
\neq
\text{same personality},
$$

以及：

$$
\text{consensus}
\neq
\text{truth}.
$$

本文的最小命題只證明：若驗證的成本低於其可避免的期望錯誤損失，verification-seeking action 具有局部工具優勢。由此可合理提出，但不能直接證成，更強的工作態收斂猜想。

下一篇將把研究單位由單一 Agent 的 verification policy 提升為 observer network，正式處理：

$$
\boxed{
\text{multi-agent hallucination}
\rightarrow
\text{distributed fault localization}
\rightarrow
\text{epistemic normalization}.
}
$$

---

## 參考文獻

1. Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*. arXiv:2504.08066.
2. Google DeepMind. (2025). *AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms*.
3. OpenAI. (2026). *Unrolling the Codex agent loop*.
4. OpenAI. (2026). *Harness engineering: leveraging Codex in an agent-first world*.
5. Li, Z. et al. (2026). *MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination*. arXiv:2603.24579.
6. Wu, S., Li, X., Feng, Y., Li, Y., & Wang, Z. (2026). *Council Mode: Mitigating Hallucination and Bias in LLMs via Multi-Agent Consensus*. arXiv:2604.02923.
7. Wang, X., & Yang, C. C. (2026). *The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment*. arXiv:2606.08457.
8. Okawa, M. (2026). *Emergence of Biased Consensus in Multi-Agent LLM Debates*. arXiv:2608.02827.
9. *Claw AI Lab: An Autonomous Multi-Agent Research Team*. (2026). arXiv:2605.22662.

## 狀態標記

- **External results:** 第 1、9、11 節引用的既有系統與研究結果。
- **Definitions:** 第 3 節。
- **Proved proposition:** 命題 1。
- **Conjecture:** 猜想 1。
- **Heuristic / interpretation:** 第 5、11 節的策略內生解讀。
- **Not claimed:** universal epistemic attractor、AGI 已實現、多 Agent 共識等於真理。
