# 自我校準與漂移感知的認知編排器：從推理路由到 Meta-Orchestration

**Self-Calibrating and Drift-Aware Cognitive Orchestration: From Reasoning Routing to Meta-Orchestration**

**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-11

## 摘要

當 AI 系統由單一模型推理逐步演化為多模型、多 Agent、多工具與多專家角色協同時，一個新的系統層問題開始出現：**上層 orchestrator 如何知道哪個 specialist 現在最值得被呼叫，而且如何知道自己對 specialist 的認識是否已經過期？**

前一篇工作以 residual doubt 與 Value of Information（VOI）為核心，將 proof-search 前的推理資源配置建模為 specialist routing 問題。然而，若 specialist cost、能力與 runtime behavior 被視為固定常數，則 routing policy 只能在靜態世界中成立。實際部署中，模型版本、prompt、tool、hardware、API pricing、latency、retrieval quality 與 provider reliability 都可能改變，使：

$$
P_t(C,R\mid M)
\neq
P_{t+1}(C,R\mid M),
$$

其中 $C$ 表示 specialist cost， $R$ 表示其對 residual doubt 的 reduction capability。

本文提出 **Self-Calibrating and Drift-Aware Cognitive Orchestration（SDCO）**。系統透過 runtime telemetry 持續估計：

$$
\widehat C_t(M_i),
\qquad
\widehat R_t(M_i\mid X,D),
$$

並更新：

$$
\widehat{\operatorname{VOI}}_t(M_i\mid D_t)
=
\frac{
\widehat{\mathbb E}[\Delta V\mid M_i,D_t]
}{
\widehat C_t(M_i)
}.
$$

由於只利用 exploitation 會造成 selection bias 與 cold-start lock-in，本文加入 uncertainty bonus：

$$
\operatorname{Score}_t(M_i)
=
\widehat{\operatorname{VOI}}_t(M_i)
+
\beta U_t(M_i),
$$

形成 exploration–exploitation tension。進一步，當 specialist behavior 發生 non-stationary drift 時，引入 staleness state $A_t(M)$ 、forgetting factor、change-point detection 與 local reset / re-exploration。

本文將上層 specialist state 表示為：

$$
\mathcal S_M(t)
=
(
\widehat C_t,
\widehat R_t,
U_t,
A_t,
V_t
),
$$

其中 $V_t$ 記錄 model / prompt / runtime version。透過 EXP-0008～EXP-0010 的 runtime telemetry contract、self-calibration plumbing test 與 non-stationary synthetic simulation，我們驗證了從 raw telemetry 到 posterior update、VOI routing、shift detection 與 recalibration 的工程閉環可以被實作。所有實驗均為 synthetic / proxy simulation，本文不宣稱已證明真實模型上的效率提升。

本文的核心主張是：成熟的 AI orchestrator 不只應管理 specialist，也應管理**自己對 specialist 的認識**。因此 meta-orchestration 的研究問題不再只是：

$$
\text{Who should think next?}
$$

而是：

$$
\boxed{
\text{How should the system learn, forget, and revise its beliefs about who should think next?}
}
$$

**關鍵詞：** Meta-Orchestration、Self-Calibration、Agent Routing、Concept Drift、Runtime Telemetry、Contextual Bandit、Exploration–Exploitation、Staleness、Change-Point Detection、Mathematical AI

---

## 1. 引言

多模型與多 Agent 系統的基本 routing 問題可以寫成：

$$
x
\rightarrow
M^\ast(x),
$$

即對輸入 $x$ 選擇最適合的模型或 Agent。

近年的 LLM routing 研究已逐步從 static router 走向 adaptive router。FlyRoute 透過實際流量累積 success evidence、自動重建 agent capability profiles，並針對 under-profiled agents 進行 targeted exploration；OrcaRouter 使用 hybrid offline–online learning 與 contextual bandit，在部署時只更新被選中模型的 arm；ParetoBandit 則直接把 production routing 建模為 non-stationary quality–cost problem，使用 forgetting mechanism、budget pacing 與 runtime hot-swap 來處理價格、品質與模型集合的變動。

這些研究顯示：

$$
\boxed{
\text{Router}
\text{ itself must be adaptive.}
}
$$

本文接受這個方向，但研究對象不同。

一般 model router 問：

> 哪個模型回答這個 query 的 quality–cost trade-off 最好？

本文研究：

> **哪個認知 specialist 對當前 residual doubt 最有價值？**

例如：

- MPF specialist；
- Source-Fidelity specialist；
- Bridge auditor；
- NLU interpreter；
- premise retriever；
- Lean prover；
- counterexample agent。

因此 routing target 不只是 output quality，而是：

$$
\boxed{
\text{expected reduction of proof-relevant uncertainty}.
}
$$

這使 orchestrator 本身變成一個需要持續學習的 epistemic control system。

---

## 2. 從 Adaptive Routing 到 Meta-Orchestration

前一篇 DDRA 架構定義：

$$
D_t
=
(D_F,D_S,D_B,\ldots)
$$

與：

$$
\operatorname{VOI}(M_i\mid D_t)
=
\frac{
\mathbb E[\Delta V\mid M_i,D_t]
}{
C(M_i)
}.
$$

如果：

$$
C(M_i)
$$

與：

$$
R_i(D)
=
\mathbb E[D_t-D_{t+1}\mid M_i,D_t]
$$

都是人工常數，

則 scheduler 本質上仍是 static policy。

本文改為：

$$
\boxed{
C(M_i)
\rightarrow
\widehat C_t(M_i),
}
$$

以及：

$$
\boxed{
R_i(D)
\rightarrow
\widehat R_t(M_i\mid X_t,D_t,\mathcal H_t),
}
$$

其中：

- $X_t$：problem / runtime context；
- $\mathcal H_t$：歷史 telemetry。

因此：

$$
\boxed{
\text{Reasoning Routing}
\rightarrow
\text{Learning-to-Route Reasoning}.
}
$$

本文稱此層為：

$$
\boxed{
\text{Meta-Orchestration}.
}
$$

---

## 3. Runtime Telemetry 是上層學習的基礎

如果沒有 observability，orchestrator 只能依賴人工印象。

因此需要保留每次 specialist invocation 的 raw telemetry。

令事件：

$$
e_t
=
(
M_i,
X_t,
D_t,
D_{t+1},
U_t,
L_t,
P_t,
Q_t,
\ldots
),
$$

至少包括：

### Model usage

$$
T_{\mathrm{prompt}},
\quad
T_{\mathrm{completion}},
\quad
T_{\mathrm{reasoning}},
\quad
T_{\mathrm{cached}}.
$$

### Runtime latency

$$
L_{\mathrm{wall}},
\quad
L_{\mathrm{TTFT}},
\quad
L_{\mathrm{queue}}.
$$

### Tool usage

$$
N_{\mathrm{tool}},
\quad
N_{\mathrm{web}},
\quad
N_{\mathrm{file}},
\quad
N_{\mathrm{python}}.
$$

### Proof telemetry

$$
N_{\mathrm{premise}},
\quad
N_{\mathrm{branch}},
\quad
N_{\mathrm{node}},
\quad
N_{\mathrm{tactic}},
\quad
N_{\mathrm{elab-fail}},
\quad
T_{\mathrm{prover}}.
$$

### Epistemic telemetry

$$
D_t,
\qquad
D_{t+1},
\qquad
\text{Freeze / Reject / Prove state}.
$$

---

## 4. Raw Telemetry 不應被單一 Cost Scalar 取代

可以定義：

$$
C_t(M)
=
w_1T_{\mathrm{prompt}}
+
w_2T_{\mathrm{completion}}
+
w_3L_{\mathrm{wall}}
+
w_4N_{\mathrm{tool}}
+
w_5N_{\mathrm{proof-node}}
+\cdots
$$

但本文強調：

$$
\boxed{
\text{Raw Telemetry}
\neq
\text{Composite Cost}.
}
$$

原因包括：

1. API pricing 會變；
2. 模型 token accounting 會變；
3. hardware latency 會變；
4. proof node 與 token 的相對價值依任務而變；
5. 不同部署場景可以有不同 objective。

因此正確流程是：

$$
\boxed{
\text{Raw telemetry}
\rightarrow
\text{calibrated view}
\rightarrow
C_t.
}
$$

而不是：

$$
\text{Raw telemetry}
\rightarrow
\text{discard}
\rightarrow
\text{single scalar}.
$$

---

## 5. Specialist Capability Estimation

設 specialist：

$$
M_i.
$$

每次呼叫得到：

$$
D_t
\rightarrow
D_{t+1}.
$$

可觀測 reduction：

$$
\Delta D_t
=
D_t-D_{t+1}.
$$

因此可以估：

$$
\widehat R_t(M_i)
=
\mathbb E[
\Delta D
\mid
M_i,\mathcal H_t
].
$$

更一般：

$$
\widehat R_t
(
M_i
\mid
X,D
),
$$

其中 $X$ 可以包含：

- domain；
- theorem form；
- source type；
- corruption signature；
- model version；
- prompt version；
- tool access；
- runtime environment。

這使 capability model 由：

$$
\boxed{
\text{“MPF is good at quantifiers”}
}
$$

變成：

$$
\boxed{
\text{“MPF-v3 under prompt P7 reduces formal doubt by this distribution on this task class.”}
}
$$

---

## 6. Shrinkage Estimation 與 Cold Start

新 specialist 的 observation 可能很少。

若直接使用 sample mean：

$$
\widehat C
=
\frac1n
\sum_{i=1}^{n}C_i
$$

在：

$$
n\ll1
$$

時極不穩定。

因此可使用 prior：

$$
C_0(M),
\qquad
R_0(M),
$$

與 pseudo-count：

$$
\alpha_0.
$$

posterior-like shrinkage estimate：

$$
\widehat C_t(M)
=
\frac{
\alpha_0C_0(M)+\sum_{\tau\le t:M_\tau=M}C_\tau
}{
\alpha_0+n_t(M)
}.
$$

同理：

$$
\widehat R_t(M)
=
\frac{
\alpha_0R_0(M)+\sum \Delta D_\tau
}{
\alpha_0+n_t(M)
}.
$$

這不是要求 Bayesian interpretation，只是一個簡單、可工程化的 shrinkage estimator。

---

## 7. Selection Bias

然而，只利用歷史被選中的 specialist 會有 fundamental selection bias。

Orchestrator 看不到：

$$
\text{what would have happened if an unselected specialist had been called}.
$$

即 bandit feedback。

這與 online LLM routing 研究中的 partial-feedback 問題一致：部署時通常只知道被選中模型的 reward，而不是所有候選模型的 counterfactual reward。OrcaRouter 與其他 bandit routing 工作正是針對這類限制進行 online update。

對 cognitive orchestrator：

$$
\boxed{
\text{Only selected cognition produces telemetry}.
}
$$

若一個 specialist 因早期資料差而被減少調用：

$$
\text{few calls}
\rightarrow
\text{few observations}
\rightarrow
\text{high uncertainty}
\rightarrow
\text{possibly fewer calls}.
$$

可能形成 self-confirming lock-in。

---

## 8. Exploration–Exploitation Tension

因此不能只選：

$$
\arg\max_i
\widehat{\operatorname{VOI}}_t(M_i).
$$

我們加入：

$$
U_t(M_i)
$$

表示 epistemic uncertainty。

定義：

$$
\boxed{
\operatorname{Score}_t(M_i)
=
\widehat{\operatorname{VOI}}_t(M_i)
+
\beta U_t(M_i).
}
$$

其中：

$$
\beta\ge0.
$$

這使：

- exploitation：選目前估計最好；
- exploration：給 under-observed specialist 機會。

因此：

$$
\boxed{
\text{Reasoning allocation itself has a tolerance tension}.
}
$$

---

## 9. Targeted Exploration 而非 Blind Exploration

如果 uncertainty 高就無條件探索：

$$
U(M)\uparrow
\Rightarrow
P(M)\uparrow,
$$

會退化為浪費。

FlyRoute 提出的 targeted exploration 給出一個相似直覺：應優先探索 under-profiled agent，但只在 query 與 agent capability plausibly relevant 時進行，而非為了補資料隨機派發不相關任務。

因此本文建議：

$$
\operatorname{ExploreScore}(M_i)
=
U_i
\cdot
\operatorname{Relevance}(M_i,D_t).
$$

最後：

$$
\operatorname{Score}
=
\widehat{\operatorname{VOI}}
+
\beta
U
\operatorname{Relevance}.
$$

如此 Bridge specialist 不會因為沒資料，就被拿去處理純代數量詞問題。

---

## 10. EXP-0008：Telemetry Contract

EXP-0008 建立一個 runtime event schema。

每個事件保存：

$$
(
\text{run id},
\text{sample id},
\text{module},
\text{target state},
D_{\mathrm{before}},
D_{\mathrm{after}},
\text{usage},
\text{latency},
\text{proof telemetry},
\text{quality}
).
$$

事件類型包括：

- run start；
- surface audit；
- specialist selection；
- specialist start/end；
- target freeze/reject；
- proof start/attempt/end；
- error。

此實驗以 synthetic telemetry 驗證：

$$
\text{event emission}
\rightarrow
\text{JSONL}
\rightarrow
\text{aggregation}
\rightarrow
\text{per-run metrics}
$$

流程可以運作。

但 synthetic events 被明確標記，不能與 measured benchmark 混合。

---

## 11. 從 Telemetry 到 Self-Calibration

有了 history：

$$
\mathcal H_t
=
\{e_1,\ldots,e_t\},
$$

Orchestrator 更新：

$$
\widehat C_t(M)
$$

與：

$$
\widehat R_t(M).
$$

因此：

$$
\boxed{
\text{Telemetry}
\rightarrow
\text{Estimate}
\rightarrow
\text{VOI}
\rightarrow
\text{Routing}
\rightarrow
\text{New Telemetry}.
}
$$

這形成 closed loop。

---

## 12. EXP-0009：Self-Calibration Plumbing Test

EXP-0009 使用 EXP-0008 synthetic telemetry 作為初始 history。

起始資料不平衡：

- MPF 有少量 observations；
- Source Fidelity 幾乎沒有；
- Bridge 沒有。

因此：

$$
U_{\mathrm{MPF}}
<
U_{\mathrm{Source}}
\approx
U_{\mathrm{Bridge}}.
$$

再透過三輪 synthetic online environment 產生新 observations。

結果顯示：

- MPF posterior cost 向 synthetic true cost 移動；
- Source Fidelity posterior cost 同樣移動；
- observation 數增加時 uncertainty 下降；
- Bridge 因沒有被相關 task 觸發，uncertainty 保持高值。

這個最後現象尤其重要：

$$
\boxed{
\text{No observation}
\Rightarrow
\text{remain uncertain}.
}
$$

而不是：

$$
\text{No observation}
\Rightarrow
\text{assume learned}.
$$

---

## 13. Meta-Orchestration 與一般 Model Training 的區別

本文的 self-calibration 並不要求重新訓練 foundation model。

底層：

$$
M_1,\ldots,M_k
$$

可以全部固定。

改變的是上層：

$$
\pi_t
:
(D,X,\mathcal H)
\rightarrow
a.
$$

即 routing / orchestration policy。

因此學習對象是：

$$
\boxed{
\text{how to allocate cognition},
}
$$

不是：

$$
\boxed{
\text{how to perform cognition internally}.
}
$$

這使 meta-orchestration 可以比 foundation-model retraining 更輕量、更頻繁地更新。

---

## 14. Non-Stationarity

靜態 estimator 假設：

$$
P(C,R\mid M)
$$

固定。

實際部署更合理：

$$
\boxed{
P_t(C,R\mid M)
}
$$

隨時間變動。

原因包括：

### Model drift

- provider 更新 model；
- silent regression；
- quantization change；
- context-window change。

### Prompt drift

$$
P_t
\neq
P_{t+1}.
$$

### Tool drift

retriever、search API、Lean library、CAS 版本改變。

### Cost drift

API price、rate limit、latency、hardware utilization 改變。

### Task-distribution drift

輸入 domain distribution 改變。

因此：

$$
\boxed{
\text{Historical competence is not permanent competence}.
}
$$

---

## 15. 與 Non-Stationary LLM Routing 的關係

ParetoBandit 特別把 production LLM routing 描述為 non-stationary quality–cost environment：

- provider pricing 改變；
- model quality 可能 silent regression；
- new models runtime onboarding。

其方法使用 forgetting、online budget control 與 new-model exploration，使 router 在條件改變時重新學習 quality–cost niche。

這與本文有重要共同點：

$$
\boxed{
\text{old routing evidence must sometimes decay}.
}
$$

但本文 tracking 的不是只有：

$$
(\text{quality},\text{price}),
$$

而是：

$$
\boxed{
(
\text{doubt-reduction capability},
\text{runtime cost},
\text{target-state effect}
).
}
$$

---

## 16. Staleness State

因此每個 specialist 的 meta-state 不應只有：

$$
(\widehat C,\widehat R,U).
$$

我們加入：

$$
A_t(M)
$$

表示 age / staleness。

最小 specialist state：

$$
\boxed{
\mathcal S_M(t)
=
(
\widehat C_t,
\widehat R_t,
U_t,
A_t,
V_t
).
}
$$

其中：

- $\widehat C_t$：估計成本；
- $\widehat R_t$：估計能力；
- $U_t$：uncertainty；
- $A_t$：staleness；
- $V_t$：version metadata。

---

## 17. Staleness Score

可以定義：

$$
S_t(M)
=
f(
\Delta t_{\mathrm{last}},
E_t,
\Delta V_t,
\Delta P_t,
\Delta H_t
).
$$

其中：

- $\Delta t_{\mathrm{last}}$：距上次 observation 的時間；
- $E_t$：prediction error；
- $\Delta V_t$：model version change；
- $\Delta P_t$：prompt version change；
- $\Delta H_t$：runtime / hardware change。

當：

$$
S_t(M)\uparrow,
$$

可以：

$$
w_{\mathrm{historical}}\downarrow,
$$

或：

$$
U_t(M)\uparrow,
$$

或：

$$
P(\text{re-explore }M)\uparrow.
$$

---

## 18. Forgetting Factor

最簡單的 non-stationary estimator 為 exponential forgetting。

對 observation：

$$
x_t,
$$

更新：

$$
\widehat x_t
=
(1-\alpha)\widehat x_{t-1}
+
\alpha x_t.
$$

其中：

$$
0<\alpha\le1.
$$

大 $\alpha$：

- adaptation 快；
- variance 大。

小 $\alpha$：

- 穩定；
- adaptation 慢。

所以 forgetting 本身也有 bias–variance tension。

---

## 19. Change-Point Detection

若 specialist behavior abrupt change：

$$
\theta_{t^-}
\neq
\theta_{t^+},
$$

持續 EWMA 可能適應太慢。

定義 innovation：

$$
I_t
=
g(
C_t-\widehat C_{t^-},
R_t-\widehat R_{t^-}
).
$$

若：

$$
I_t
$$

顯著超出近期 residual distribution，

觸發：

$$
\boxed{
\operatorname{ShiftSuspected}(M)=1.
}
$$

然後執行：

$$
\text{local reset}
\quad\text{or}\quad
\text{aggressive forgetting}.
$$

---

## 20. Partial Observability of Drift

一個重要限制：

如果 specialist 沒被呼叫，

就看不到它變了。

因此 shift detection latency 至少分為：

$$
\boxed{
L_{\mathrm{shift}}
=
L_{\mathrm{opportunity}}
+
L_{\mathrm{statistical}}.
}
$$

其中：

- $L_{\mathrm{opportunity}}$：到下一次 specialist 被觀測的時間；
- $L_{\mathrm{statistical}}$：取得足夠證據的時間。

這再次說明：

$$
\boxed{
\text{exploration is required not only for learning capability, but also for detecting capability drift}.
}
$$

---

## 21. EXP-0010：Non-Stationary Simulation

EXP-0010 建立 180 個 synthetic tasks，並在：

$$
t=61
$$

及：

$$
t=121
$$

改變 hidden specialist environment。

Phase 2：

- MPF cost 上升；
- MPF formal reduction 下降；
- Source Fidelity cost 下降；
- Source capability 提升。

Phase 3：

- Bridge cost 大幅下降；
- Bridge capability 提升；
- MPF 部分恢復。

比較：

1. stationary mean；
2. EWMA；
3. change-point + reset。

---

## 22. Choice Accuracy 不足以衡量 Adaptation

初步 scheduler-level choice accuracy 可能很快恢復。

但這可能只是因 task mix 剛好讓 stale estimate 沒造成太多錯選。

因此 EXP-0010 增加 parameter-level recovery：

要求：

$$
\frac{
|\widehat C-C^\ast|
}{
C^\ast
}
\le0.2
$$

且 specialist 主能力：

$$
|\widehat R-R^\ast|
\le0.1.
$$

才算重新學到新環境。

此結果顯示，stationary estimator 對某些大幅 shift 在整個 horizon 內都沒有真正恢復，而 change-point policy 在 abrupt shift 下可以大幅縮短 parameter recovery delay。

---

## 23. Abrupt Shift 與 Gradual Drift 不同

但 change-point policy 在 partial recovery / smaller drift 上可能漏報。

因此：

$$
\boxed{
\text{Abrupt Change Detection}
\neq
\text{General Drift Tracking}.
}
$$

未來需要至少區分：

$$
\begin{aligned}
&\text{Abrupt Shift},\\
&\text{Gradual Drift},\\
&\text{Recurring Drift},\\
&\text{Context-Conditional Shift}.
\end{aligned}
$$

這意味著單一 z-score detector 不足以構成完整 drift-aware orchestrator。

---

## 24. False Alarm 也是成本

change-point detector 越敏感：

$$
\text{detection delay}\downarrow,
$$

但：

$$
\text{false alarm rate}\uparrow.
$$

每次 false alarm 可能導致：

- estimator reset；
- forced re-exploration；
- temporary routing instability；
- unnecessary specialist calls。

所以真正目標是：

$$
\boxed{
\min
\left(
L_{\mathrm{recovery}},
R_{\mathrm{regret}},
N_{\mathrm{false-alarm}},
C_{\mathrm{reexplore}}
\right).
}
$$

這是一個 multi-objective control problem。

---

## 25. 三個 Feedback Loops

整體架構現在具有三個回饋迴路。

### 25.1 Epistemic Loop

$$
D_t
\rightarrow
M_t
\rightarrow
D_{t+1}.
$$

回答：

> 哪個 specialist 能消除當前問題疑點？

### 25.2 Operational Loop

$$
\text{Telemetry}_t
\rightarrow
(\widehat C_t,\widehat R_t)
\rightarrow
\text{Routing}
\rightarrow
\text{Telemetry}_{t+1}.
$$

回答：

> 我們目前對 specialist 的能力與成本估計是什麼？

### 25.3 Drift Loop

$$
\text{Prediction Error}
\rightarrow
\text{Shift Suspicion}
\rightarrow
\text{Forget / Reset / Re-explore}
\rightarrow
\text{Recalibrate}.
$$

回答：

> 我們以前學到的 specialist model 是否仍然有效？

---

## 26. 從 Orchestrator 到 Epistemic Governor

傳統 router：

$$
x\rightarrow M.
$$

Adaptive router：

$$
(x,\mathcal H)\rightarrow M.
$$

本文的 cognitive orchestrator：

$$
(D,X,\mathcal H,V,A)
\rightarrow
\{
M_i,\operatorname{Freeze}
\}.
$$

因此分層可以寫為：

$$
\begin{array}{ll}
L_0 &: \text{Worker / Solver}\\
L_1 &: \text{Specialist Reasoner}\\
L_2 &: \text{Adaptive Orchestrator}\\
L_3 &: \text{Epistemic Governor}
\end{array}
$$

 $L_3$ 不只決定誰工作。

它還管理：

- 哪些 specialist belief 已 stale；
- 哪些能力模型需要重新估；
- 哪些 uncertainty 需要探索；
- 哪些 history 應該忘記；
- 哪些 target 可以 Freeze；
- 哪些 operational shifts 必須觸發 re-routing。

---

## 27. Self-Evolving Agent Profiles 與本文的關係

FlyRoute 使用成功案例與 traffic data 持續更新 agent profiles，顯示 static capability description 在 agent 持續變動的環境中會失效。

本文採取更數值化的角色模型：

$$
\operatorname{Profile}(M)
=
(
\widehat C,
\widehat R,
U,
A,
V
).
$$

兩者可以互補：

- textual capability profile：
  用於 semantic matching；
- quantitative telemetry profile：
  用於 VOI / cost / uncertainty routing。

因此未來可以：

$$
\boxed{
\text{Semantic Profile}
+
\text{Empirical Performance Profile}.
}
$$

---

## 28. Contextual Bandit Interpretation

若每一輪只能看到被選 specialist 的結果，

meta-orchestration 可被視為 contextual bandit：

Context：

$$
X_t
=
(D_t,\text{problem features},\text{runtime state}).
$$

Arm：

$$
M_i.
$$

Reward：

$$
r_t
=
\Delta V_t
-
\lambda C_t.
$$

或：

$$
r_t
=
\frac{\Delta V_t}{C_t}.
$$

但本文比一般 bandit 多一個特殊 action：

$$
\boxed{
\operatorname{Freeze}.
}
$$

而且 freeze 受到 hard target-safety constraints。

所以更精確是：

$$
\boxed{
\text{constrained contextual bandit / sequential control with stopping}.
}
$$

---

## 29. Routing Regret

若 hindsight oracle：

$$
M_t^\ast
=
\arg\max_i
\operatorname{VOI}^{\mathrm{true}}_t(M_i),
$$

則：

$$
R_T
=
\sum_{t=1}^{T}
[
\operatorname{VOI}^{\mathrm{true}}_t(M_t^\ast)
-
\operatorname{VOI}^{\mathrm{true}}_t(M_t)
].
$$

在真實世界：

$$
\operatorname{VOI}^{\mathrm{true}}
$$

通常不可直接觀測。

因此 regret 只能透過：

- controlled benchmark；
- full-information offline evaluation；
- counterfactual estimator；
- synthetic environment；

近似。

所以本文中的 EXP-0010 regret 明確只是一個 synthetic diagnostic。

---

## 30. Specialist Versioning

當：

$$
M^{(v1)}
\rightarrow
M^{(v2)},
$$

歷史 telemetry 是否可直接繼承？

不一定。

如果只看 role：

$$
\operatorname{Role}(M^{v1})
=
\operatorname{Role}(M^{v2})
=
\mathrm{MPF},
$$

但 capability distribution：

$$
P(R,C\mid M^{v1})
\neq
P(R,C\mid M^{v2}),
$$

則完全繼承可能錯。

因此：

$$
\boxed{
\text{Specialist Role}
\neq
\text{Specialist Instance}.
}
$$

這是下一階段 model replacement / identity continuity 的核心問題。

---

## 31. Capability Transfer

可以定義兩 specialist instances 的 transfer coefficient：

$$
\rho
(
M^{v1},
M^{v2}
)
\in[0,1].
$$

若：

$$
\rho=1,
$$

完全繼承。

若：

$$
\rho=0,
$$

cold start。

一般：

$$
0<\rho<1.
$$

new prior：

$$
\theta_0^{v2}
=
\rho\widehat\theta^{v1}
+
(1-\rho)\theta_{\mathrm{role-prior}}.
$$

這讓 model hot-swap 不必永遠從零開始，也不必盲目繼承全部 history。

---

## 32. Runtime Identity 與 Functional Identity

因此需要區分：

### Runtime identity

具體：

- model ID；
- model version；
- prompt；
- tool set；
- hardware；
- endpoint。

### Functional identity

例如：

$$
\mathrm{MPF\ Specialist}.
$$

同一 functional role：

$$
R
$$

可以由多個 runtime substrate 實現。

因此：

$$
\boxed{
\text{Functional Role}
\neq
\text{Runtime Substrate}.
}
$$

這也是 scalable agent runtime 的重要抽象。

---

## 33. 評測指標

真正部署時至少需要：

### Calibration

$$
|\widehat C-C|,
\qquad
|\widehat R-R|.
$$

### Routing

$$
\text{selection accuracy},
\quad
\text{regret}.
$$

### Exploration

$$
N_{\mathrm{explore}},
\quad
C_{\mathrm{explore}}.
$$

### Drift

$$
L_{\mathrm{detect}},
\quad
L_{\mathrm{recover}},
\quad
\text{false alarm rate}.
$$

### Safety

$$
\text{false freeze rate},
\quad
\text{corruption miss rate}.
$$

### Downstream impact

$$
\text{proof success},
\quad
\text{proof nodes},
\quad
\text{tokens},
\quad
\text{latency}.
$$

---

## 34. EXP-0008～0010 的研究地位

必須明確區分三個層級。

### Level 1：Schema / Plumbing

已完成：

- telemetry event schema；
- recorder；
- aggregator；
- cost interface；
- self-calibration learner；
- shift monitor。

### Level 2：Synthetic Simulation

已完成：

- posterior movement；
- exploration–exploitation；
- non-stationary shift；
- change-point reset；
- parameter recovery。

### Level 3：Measured Empirical Validation

尚未完成。

需要：

- fresh independent agents；
- real token usage；
- real latency；
- real tool logs；
- real Lean/prover logs；
- fixed model versions；
- blinded evaluation。

因此：

$$
\boxed{
\text{engineering feasibility}
\neq
\text{empirical effectiveness}.
}
$$

---

## 35. 可檢驗假說

### H1：Self-Calibration

真實 telemetry 可降低：

$$
|\widehat C-C|
$$

與：

$$
|\widehat R-R|
$$

相較固定人工 proxy。

### H2：Exploration

適度 exploration 應降低 cold-start / selection-lock-in regret。

### H3：Forgetting

在 non-stationary environment：

$$
R_T^{\mathrm{forgetting}}
<
R_T^{\mathrm{stationary}}
$$

至少在某些 shift regimes 成立。

### H4：Change-Point Reset

對 abrupt shift：

$$
L_{\mathrm{recover}}^{\mathrm{reset}}
<
L_{\mathrm{recover}}^{\mathrm{EWMA}}.
$$

### H5：Drift Cost

過度敏感的 change detector 會提高：

$$
N_{\mathrm{false-alarm}}
+
C_{\mathrm{reexplore}}.
$$

因此不存在單純「越敏感越好」。

---

## 36. 失敗模式

### 36.1 Feedback Poisoning

錯誤 quality label 會污染 capability model。

### 36.2 Selection Bias

只有被選 specialist 有 observation。

### 36.3 Survivorship Bias

失敗 Agent 若被移除，其歷史可能不再進入比較。

### 36.4 Cross-Task Generalization Error

某 specialist 在一個 domain 很好，不代表另一 domain 相同。

### 36.5 Version Leakage

不同 model version telemetry 被錯誤混合。

### 36.6 Cost Miscalibration

token cost、latency 與 proof-node cost 被錯誤壓成不合理 scalar。

### 36.7 Change Detector Overreaction

noise 被誤判成 shift。

### 36.8 Under-Exploration

新 specialist 永遠沒有足夠資料。

### 36.9 Over-Exploration

系統退化為 Always-Dual。

### 36.10 Governance Failure

上層 orchestrator 本身的 objective 若錯，底層 specialists 再強也無法保證整體正確。

---

## 37. 三層「知道」

一個 solver 需要知道：

$$
\boxed{
\text{how to solve}.
}
$$

一個 orchestrator 需要知道：

$$
\boxed{
\text{who should solve}.
}
$$

一個 meta-orchestrator 需要知道：

$$
\boxed{
\text{how confident it should be in its belief about who should solve}.
}
$$

因此：

$$
\boxed{
\text{knowledge}
\rightarrow
\text{knowledge allocation}
\rightarrow
\text{knowledge about allocation quality}.
}
$$

這是本文認為 meta-orchestration 的核心認知層次。

---

## 38. 從 AI Router 到 AI Organization

當 specialist 數量增加：

$$
|\mathcal M|
\gg1,
$$

整個系統越來越像一個 organization。

每個 specialist：

- 有 role；
- 有成本；
- 有歷史績效；
- 有 uncertainty；
- 會更新；
- 可能退化；
- 可能被替換。

Orchestrator：

- 分配工作；
- 監測結果；
- 更新 profile；
- 調整信任；
- 重新探索；
- 停止無效工作。

因此可以把它視為：

$$
\boxed{
\text{Cognitive Organization Controller}.
}
$$

但本文不賦予「organization」任何人格或法律主體含義；這只是一個 functional systems analogy。

---

## 39. Problem-Space Governance 的完整閉環

整個系列到本文可以寫為：

$$
\boxed{
C_{\mathrm{source}}
\rightarrow
\mathcal C_{\mathrm{candidate}}
\rightarrow
C^\ast_{\mathrm{freeze}}
\rightarrow
D_t
\rightarrow
M_t
\rightarrow
D_{t+1}
}
$$

同時：

$$
\boxed{
\text{Telemetry}
\rightarrow
\widehat C_t,
\widehat R_t,
U_t,
A_t
\rightarrow
\text{routing policy update}.
}
$$

如果 drift：

$$
\boxed{
\text{Prediction Error}
\rightarrow
\text{Shift Detection}
\rightarrow
\text{Forget / Reset / Re-explore}.
}
$$

最後 target freeze 後：

$$
C^\ast_{\mathrm{freeze}}
\rightarrow
\mathrm{MCDM}
\rightarrow
\mathrm{ProofRouter}
\rightarrow
\mathrm{FormalProof}.
$$

---

## 40. 討論

本文的核心不是讓 AI「自我修改」到不可控。

相反地，meta-orchestration 的更新對象可以非常有限：

$$
\boxed{
\text{routing beliefs and allocation policy}.
}
$$

底層：

- model weights；
- proof kernel；
- tool permissions；

可以完全固定。

這提供一個重要工程優勢：

> **系統可以適應環境，而不必讓所有能力層都同步可變。**

因此 adaptive orchestration 可以成為：

$$
\boxed{
\text{a controlled adaptation layer}.
}
$$

---

## 41. 結論

本文提出 Self-Calibrating and Drift-Aware Cognitive Orchestration。

其最小 specialist state 為：

$$
\boxed{
\mathcal S_M(t)
=
(
\widehat C_t,
\widehat R_t,
U_t,
A_t,
V_t
).
}
$$

其中：

- $\widehat C_t$：cost estimate；
- $\widehat R_t$：capability / doubt-reduction estimate；
- $U_t$：uncertainty；
- $A_t$：staleness；
- $V_t$：runtime identity/version。

Routing 使用：

$$
\boxed{
\operatorname{Score}_t(M)
=
\widehat{\operatorname{VOI}}_t(M)
+
\beta U_t(M)
}
$$

並在 non-stationary setting 下加入：

$$
\text{forgetting},
\quad
\text{change-point detection},
\quad
\text{re-exploration}.
$$

因此系統形成三個 feedback loops：

$$
\boxed{
\text{Epistemic Loop}
}
$$

$$
\boxed{
\text{Operational Learning Loop}
}
$$

$$
\boxed{
\text{Drift Adaptation Loop}.
}
$$

數學 AI 的上層控制問題因此由：

$$
\text{Who should think next?}
$$

進一步變成：

$$
\boxed{
\text{How should the system update its belief about who should think next?}
}
$$

本文中的 EXP-0008～0010 只證明該閉環可以被資料化、實作與 synthetic stress-test；真正的性能主張仍必須由 measured runtime telemetry、獨立 Agent 與 formal prover benchmark 驗證。

但就架構而言，數學 AI 已不再只能被描述為 solver 的集合。它可以被更完整地描述為：

$$
\boxed{
\text{a self-monitoring cognitive organization with controlled epistemic resource allocation}.
}
$$

---

## 參考文獻

1. Li, R., Zhou, Z., Wu, Y. *FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing.* arXiv:2605.22057, 2026.
2. Bao, Z., Tian, F., Zhang, C., Chen, Z., Ma, X., Shi, Y. *OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning.* arXiv:2605.30736, 2026.
3. Taberner-Miller, A. *ParetoBandit: Budget-Paced Adaptive Routing for Non-Stationary LLM Serving.* arXiv:2604.00136, 2026.
4. Nguyen, M., Gupta, S., Le, H. *Uncertainty-Aware Budget Allocation for Adaptive Test-Time Reasoning.* arXiv:2605.26849, 2026.
5. Zhai, Z., Li, B., Xiao, B., Li, M., Wang, X. *Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization.* arXiv:2604.14853, 2026.
6. Wei, W., Yang, T., Chen, H., Zhao, Y., Dernoncourt, F., Rossi, R. A., Eldardiry, H. *Learning to Route LLMs from Bandit Feedback: One Policy, Many Trade-offs.* arXiv:2510.07429, 2025.
7. Li, Y. *LLM Bandit: Cost-Efficient LLM Generation via Preference-Conditioned Dynamic Routing.* arXiv:2502.02743, 2025.
8. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., Liu, F. *LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.* arXiv:2606.05400, 2026.
9. Firsching, M., Lezeau, P., Mercuri, S., et al. *Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics.* arXiv:2605.13171, 2026.

---

## 研究狀態聲明

本文提出的 Self-Calibrating Cognitive Orchestration、specialist state $\mathcal S_M(t)$ 、doubt-reduction capability model、staleness state、drift loop 及其與 theorem-target governance 的整合，屬於本文提出的研究框架。

EXP-0008～EXP-0010 使用的 telemetry、cost、capability、task distribution、change point 與 regret 均包含 synthetic / proxy components。本文不將任何 synthetic numerical result 解讀為真實 LLM routing accuracy、token savings、latency improvement 或 formal theorem proving speedup。

真正 empirical validation 需要固定 model / prompt / runtime version，使用獨立 Agent，保存 raw measured telemetry，並在 blinded benchmark 與 formal prover logs 上重現。
