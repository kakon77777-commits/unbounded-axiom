---
title: "AI 多尺度概率場：從 Token、語義與策略到任務能力的可重現分布"
english_title: "AI Multi-Scale Probability Fields: From Tokens, Semantics, and Strategies to Reproducible Task-Level Capability Distributions"
series: "判定域概率論與超概率研究"
series_id: "JDPSP"
paper_id: "JDPSP-08"
author: "Neo.K"
organization: "EveMissLab"
version: "0.1.0"
status: "研究初稿 / experimental formalization"
date: "2026-08-14"
language: "zh-TW"
---

# AI 多尺度概率場

## 從 Token、語義與策略到任務能力的可重現分布

**作者：** Neo.K  
**機構：** EveMissLab  
**系列：** 判定域概率論與超概率研究，Paper 08  
**版本：** v0.1.0  
**日期：** 2026-08-14

## 摘要

前七篇已建立判定域、局部—全域提升、尺度幾何、遞歸概率階、零測度支撐點與動態開放系統。本文把這些抽象結構壓到大型語言模型與生成式 AI 的可實驗對象上。

早期 AI Probability Field 草案已提出同時記錄：

$$
H_{\mathrm{token}},
\qquad
H_{\mathrm{semantic}},
\qquad
H_{\mathrm{strategy}},
\qquad
H_{\mathrm{task}},
\qquad
P_{\mathrm{success}},
$$

並以 repeated runs、protocol locking、hash chain、CTCL 與 distributional reproducibility 作為研究方法。本文保留此核心，但重新形式化其數學關係。

對固定 query / task 與 protocol condition $c$，令完整模型輸出為隨機變量：

$$
Y\sim Q_c
$$

其中 $Q_c$ 是 run-level output law。若為 white-box autoregressive model，在固定 decoding rule 下可由 token conditionals 誘導 sequence law；若為 black-box hosted model，則 $Q_c$ 以 repeated sampling 的 empirical law 近似。

語義、策略、任務與成功不再被視為四個彼此無關的概率來源，而是由尺度映射或 stochastic classifier 從同一 $Q_c$ 投影得到：

$$
P_L^{(c)}
=
(K_L)_\star Q_c,
$$

其中：

$$
L
\in
\{
\mathrm{semantic},
\mathrm{strategy},
\mathrm{task},
\mathrm{success}
\}.
$$

若尺度映射是 deterministic：

$$
g_L:\mathcal Y\rightarrow\mathcal Z_L,
$$

則：

$$
P_L^{(c)}
=
(g_L)_\#Q_c.
$$

因此本文將 AI 概率場定義為一族具有共同來源但不同判定尺度的 probability objects：

$$
\boxed{
\mathfrak F_{\mathrm{AI}}(c)
=
\left(
Q_c,
\{
P_L^{(c)}
\}_{L\in\Lambda},
\{
K_L
\}_{L\in\Lambda}
\right).
}
$$

本文特別區分三種常被混淆的 AI uncertainty。第一是 token / decoding uncertainty，來自局部 next-token conditionals；第二是 output / semantic uncertainty，來自 repeated generations 在語義等價類上的分布；第三是 task capability uncertainty，指同一 query 在固定 protocol 下 repeated execution 的成功概率。2026 年 capability-calibration 研究已明確區分 single-response confidence 與 expected query-level capability，證明兩者不可互換。近期大型 UQ benchmark 亦指出，token-level confidence 在 instruction-tuned / reasoning models 上可能受 probability-mass polarization 影響，而 sample-level answer consistency 常能提供更可靠的 task-level uncertainty signal。

本文證明一個多尺度 entropy decomposition。若語義類別：

$$
C=g_{\mathrm{sem}}(Y)
$$

是 output $Y$ 的 deterministic quotient，則：

$$
\boxed{
H(Y)
=
H(C)
+
H(Y\mid C).
}
$$

因此高 lexical / sequence entropy 不必代表高 semantic entropy；大量 paraphrases 可以提高表面變異而不提高意義層不確定性。此結果與 semantic-entropy 文獻的核心動機一致，但本文把它放入判定域尺度提升框架。

本文進一步定義 task capability：

$$
\boxed{
\kappa(q,c)
=
\mathbb E_{Y\sim Q_{q,c}}
[
S(Y)
],
}
$$

其中 $S(Y)\in[0,1]$ 為 task evaluator。若 $S$ 為 binary success indicator，則：

$$
\kappa(q,c)
=
P_{\mathrm{success}}^{(c)}.
$$

在 i.i.d. repeated-run assumption 下，對：

$$
\widehat\kappa_N
=
\frac1N
\sum_{i=1}^N S(Y_i),
$$

Hoeffding inequality 給出：

$$
\Pr(
|\widehat\kappa_N-\kappa|
\ge\varepsilon
)
\le
2e^{-2N\varepsilon^2}.
$$

因此若要求 confidence $1-\delta$：

$$
\boxed{
N
\ge
\frac{
\log(2/\delta)
}{
2\varepsilon^2
}
}
$$

即足以控制 binary capability estimation error。本文同時強調 hosted LLM 並不應無條件假設 repeated runs i.i.d.；model routing、snapshot changes、hidden prompts、tools、retrieval、memory、policy 與時間漂移都可能使 $\mathfrak D_t$ 改變，因此 protocol manifest 與時間證據是概率估計的一部分。

最後，本文定義 distributional reproducibility。若原始與 replication study 在同一 declared protocol family 下得到：

$$
\widehat P_L^{(A)},
\qquad
\widehat P_L^{(B)},
$$

則以：

$$
D_L(
\widehat P_L^{(A)},
\widehat P_L^{(B)}
)
\le
\varepsilon_L
$$

作為尺度 $L$ 的 $\varepsilon_L$ -distributional reproduction criterion。AI 概率場因此不是要求每一條回答逐字相同，而是要求在已鎖定的 judgment domain 與 protocol 下，跨尺度分布具有可量化的重現性。

**關鍵詞：** AI 概率場、LLM uncertainty、semantic entropy、token entropy、strategy distribution、task capability、calibration、self-consistency、distributional reproducibility、判定域、Repeated sampling、probability fingerprint

---

# 1. 問題起點：AI 的「概率」究竟在哪一層？

大型語言模型常被描述為：

$$
\boxed{
\text{next-token probability model}.
}
$$

在 autoregressive form 中：

$$
p_\theta(
y_1,\ldots,y_T
\mid c
)
=
\prod_{t=1}^{T}
p_\theta(
y_t
\mid
y_{<t},c
).
$$

這個表示非常重要。

但它只直接告訴我們：

$$
\boxed{
\text{token / sequence generation law}.
}
$$

它不自動等於：

- semantic uncertainty；
- reasoning-strategy uncertainty；
- task outcome probability；
- probability of solving a query；
- model capability。

因此本文的第一個禁則是：

$$
\boxed{
P_{\mathrm{token}}
\not\equiv
P_{\mathrm{semantic}}
\not\equiv
P_{\mathrm{strategy}}
\not\equiv
P_{\mathrm{task}}
\not\equiv
P_{\mathrm{success}}.
}
$$

---

# 2. 既有 AI 不確定性研究已走到哪裡？

## 2.1 Self-Evaluation / Calibration

Kadavath et al. 研究 language models 是否能預測自己的答案正確性，包含：

$$
P(\mathrm{True})
$$

與：

$$
P(\mathrm{IK})
$$

等 self-evaluation quantities。

這代表：

$$
\boxed{
\text{model-reported confidence}
}
$$

已經是一條成熟研究路線。

但 self-reported confidence 並不自動等於真實 repeated-run probability。

## 2.2 Semantic Entropy

Semantic entropy 的核心是：不同表面文字可以語義等價，因此 lexical variation 不應全部被當作 epistemically distinct outcomes。

所以它不只計算 raw sequence entropy，而將 sampled generations 依 meaning clustering 後再計算 uncertainty。

本文採納：

$$
\boxed{
\text{surface output space}
\rightarrow
\text{semantic quotient space}
}
$$

這一核心觀點。

## 2.3 Semantic Entropy Probes / Kernel Language Entropy

後續研究已嘗試：

- 由 hidden states 近似 semantic entropy；
- 以 semantic-similarity kernel 取代 hard clusters；
- 降低多次生成的計算成本。

所以本文不宣稱首次提出：

$$
\boxed{
\text{semantic-level probability}.
}
$$

## 2.4 Self-Consistency

Self-consistency 透過 sampling 多條 reasoning paths，再 marginalize / vote 最終答案。

這顯示：

$$
\boxed{
\text{multiple reasoning trajectories}
}
$$

本身已被用作 task-level inference signal。

但本文所稱 strategy probability 會更嚴格：它要求一個明示 strategy state space 與 mapping / classifier，而不只做 final-answer majority vote。

## 2.5 Capability Calibration

2026 年 capability-calibration 工作明確區分：

$$
\boxed{
\text{response calibration}
}
$$

與：

$$
\boxed{
\text{query-level capability calibration}.
}
$$

後者關心的是：

> 對同一 query 反覆生成時，模型實際成功的機率是多少？

這與本文：

$$
P_{\mathrm{success}}
$$

及：

$$
\kappa(q,c)
$$

直接接軌。

## 2.6 2026 UQ Benchmark 的重要警告

大型 long-form QA uncertainty benchmark 發現：

- token-level confidence 可能因 instruction tuning 而出現 probability-mass polarization；
- verbalized confidence 可能和 correctness 關聯不佳；
- repeated-sample answer frequency / consistency 在多個設定下更可靠。

因此：

$$
\boxed{
\text{token confidence}
\not\Rightarrow
\text{task-level calibrated probability}.
}
$$

---

# 3. AI Experimental Judgment Domain

對一個 AI run，判定域不能只寫 model name。

定義：

$$
\boxed{
\mathfrak D_{\mathrm{AI}}
=
(
X,
\Sigma;
r,s,c
).
}
$$

其中 context：

$$
c
$$

至少可以包括：

$$
c
=
(
M,
V,
\Pi,
\Theta,
R,
\mathcal M,
\mathcal T,
\mathcal P,
t
).
$$

例如：

- $M$：model family / provider；
- $V$：exact model ID / snapshot；
- $\Pi$：prompt bundle；
- $\Theta$：sampling configuration；
- $R$：retrieved context；
- $\mathcal M$：memory state；
- $\mathcal T$：tools / tool policy；
- $\mathcal P$：evaluation protocol；
- $t$：time / API version。

因此：

$$
\boxed{
\text{same model name}
\not\Rightarrow
\text{same judgment domain}.
}
$$

---

# 4. Run-Level Output Law

對固定 query：

$$
q
$$

與 protocol condition：

$$
c,
$$

令完整輸出：

$$
Y
$$

為隨機變量。

定義：

$$
\boxed{
Y\sim Q_{q,c}.
}
$$

 $Q_{q,c}$ 稱為 run-level output law。

若模型與 decoding fully white-box， $Q_{q,c}$ 可由 token-level conditional distributions 理論上導出。

若只有 API black-box access， $Q_{q,c}$ 只能由 repeated sampling 估計。

---

# 5. Empirical Run Law

給定：

$$
Y_1,\ldots,Y_N,
$$

定義 empirical measure：

$$
\boxed{
\widehat Q_N
=
\frac1N
\sum_{i=1}^{N}
\delta_{Y_i}.
}
$$

它是：

$$
Q_{q,c}
$$

的 empirical approximation。

但此處必須明示假設。

若：

$$
Y_i
$$

不是同分布，例如 provider 在實驗期間更新 backend：

$$
Q_{q,c,t_1}
\neq
Q_{q,c,t_2},
$$

則把所有 runs 混成單一：

$$
\widehat Q_N
$$

會把 temporal drift 誤認成 sampling uncertainty。

---

# 6. Protocol Stationarity Assumption

本文定義一個實驗假設：

### Assumption 6.1：Protocol Stationarity

在一個 locked study batch：

$$
B
$$

內，所有會實質改變 run law 的 declared variables 保持固定，並假設：

$$
Q_{q,c,t}
\approx
Q_{q,c}
$$

對：

$$
t\in B
$$

成立。

如果無法保證：

$$
\boxed{
\text{stationarity is an assumption, not a hidden fact}.
}
$$

因此 exact model snapshot unavailable 時，protocol 必須標記：

```text
snapshot_known: false
```

而不能假裝完全重現。

---

# 7. 從 Output Law 到多尺度 Probability Objects

令：

$$
\Lambda
=
\{
\mathrm{surface},
\mathrm{semantic},
\mathrm{strategy},
\mathrm{task},
\mathrm{success}
\}.
$$

對每一層：

$$
L\in\Lambda,
$$

建立 output-to-scale transport：

$$
K_L:
\mathcal Y
\rightsquigarrow
\mathcal Z_L.
$$

則：

$$
\boxed{
P_L^{(q,c)}
=
(K_L)_\star Q_{q,c}.
}
$$

如果 classifier deterministic：

$$
K_L(y,\cdot)
=
\delta_{g_L(y)},
$$

則：

$$
\boxed{
P_L^{(q,c)}
=
(g_L)_\#Q_{q,c}.
}
$$

這是本文 AI Probability Field 最重要的形式化。

---

# 8. Surface / Sequence Level

最直接的 output scale 是：

$$
\mathcal Z_{\mathrm{surface}}
=
\mathcal Y.
$$

因此：

$$
P_{\mathrm{surface}}
=
Q.
$$

若 white-box sequence probability 可得：

$$
Q(y)
=
\prod_t
p(y_t\mid y_{<t},c).
$$

但 sequence probability 常高度受：

- length；
- paraphrase；
- punctuation；
- lexical choice；

影響。

所以：

$$
\boxed{
\text{surface uncertainty}
}
$$

不能直接當成 semantic uncertainty。

---

# 9. Token-Level Entropy

對生成 step：

$$
t,
$$

有：

$$
p_t(v)
=
p(
y_t=v
\mid
y_{<t},c
).
$$

定義：

$$
H_{\mathrm{tok},t}
=
-
\sum_v
p_t(v)\log p_t(v).
$$

若需要 run-level token entropy profile，可使用：

$$
\boxed{
\bar H_{\mathrm{tok}}
=
\frac1T
\sum_{t=1}^{T}
H_{\mathrm{tok},t}.
}
$$

或保存整條：

$$
(
H_{\mathrm{tok},1},
\ldots,
H_{\mathrm{tok},T}
).
$$

本文不把：

$$
\bar H_{\mathrm{tok}}
$$

與 semantic / task entropy 強行放入單調序列。

因它們測量的是不同 random objects。

---

# 10. Semantic Scale

令：

$$
g_{\mathrm{sem}}
:
\mathcal Y
\rightarrow
\mathcal C_{\mathrm{sem}}
$$

把表面輸出映射到 semantic equivalence classes。

則：

$$
C_{\mathrm{sem}}
=
g_{\mathrm{sem}}(Y).
$$

語義分布為：

$$
\boxed{
P_{\mathrm{sem}}
=
(g_{\mathrm{sem}})_\#Q.
}
$$

Semantic entropy：

$$
\boxed{
H_{\mathrm{sem}}
=
-
\sum_c
P_{\mathrm{sem}}(c)
\log
P_{\mathrm{sem}}(c).
}
$$

這與既有 semantic entropy 的基本思想一致。

---

# 11. 定理一：Surface–Semantic Entropy Decomposition

令：

$$
C
=
g(Y)
$$

為 $Y$ 的 deterministic function。

則：

$$
\boxed{
H(Y)
=
H(C)
+
H(Y\mid C).
}
$$

### 證明

因：

$$
C=g(Y),
$$

有：

$$
H(C\mid Y)=0.
$$

由 joint entropy chain rule：

$$
H(Y,C)
=
H(Y)
+
H(C\mid Y)
=
H(Y).
$$

另一方面：

$$
H(Y,C)
=
H(C)+H(Y\mid C).
$$

所以：

$$
H(Y)
=
H(C)+H(Y\mid C).
$$

$$
\boxed{\square}
$$

---

# 12. Entropy Decomposition 的 AI 解讀

對 semantic quotient：

$$
C=C_{\mathrm{sem}},
$$

有：

$$
\boxed{
H_{\mathrm{surface}}
=
H_{\mathrm{semantic}}
+
H_{\mathrm{surface}\mid\mathrm{semantic}}.
}
$$

其中：

$$
H_{\mathrm{surface}\mid\mathrm{semantic}}
$$

代表同一意思內部的：

- paraphrase variation；
- lexical variation；
- stylistic variation；
- syntactic variation。

所以：

$$
\boxed{
H_{\mathrm{surface}}\gg0
}
$$

可以同時有：

$$
\boxed{
H_{\mathrm{semantic}}\approx0.
}
$$

這就是「說法很多，但意思其實非常穩」。

---

# 13. Semantic Classifier 不是上帝視角

實際：

$$
g_{\mathrm{sem}}
$$

常不是完美 deterministic oracle。

若 semantic judge 自身有 uncertainty，應使用：

$$
\boxed{
K_{\mathrm{sem}}
:
\mathcal Y
\rightsquigarrow
\mathcal C_{\mathrm{sem}}.
}
$$

則：

$$
P_{\mathrm{sem}}
=
(K_{\mathrm{sem}})_\star Q.
$$

此時 observed semantic uncertainty 同時包含：

- model output uncertainty；
- semantic classifier uncertainty。

因此 protocol 必須保存 judge model / embedding model / threshold / clustering algorithm。

---

# 14. Strategy Scale

本文提出：

$$
\mathcal C_{\mathrm{strategy}}
$$

作為明示 strategy state space。

例如數學任務中可能有：

- direct algebra；
- case split；
- induction；
- contradiction；
- search / enumeration；
- tool-assisted computation；
- retrieval-first；
- abstention。

定義：

$$
K_{\mathrm{strategy}}
:
\mathcal Y
\rightsquigarrow
\mathcal C_{\mathrm{strategy}}.
$$

然後：

$$
\boxed{
P_{\mathrm{strategy}}
=
(K_{\mathrm{strategy}})_\star Q.
}
$$

這裡的 strategy probability 是本文 proposed experimental layer。

它不是目前 LLM uncertainty literature 中已有統一標準定義。

---

# 15. Strategy Probability 與 Self-Consistency 不同

Self-consistency 主要：

$$
\boxed{
\text{sample many reasoning paths}
\rightarrow
\text{aggregate final answers}.
}
$$

本文 strategy probability 則保留：

$$
\boxed{
\text{reasoning / action path class itself}.
}
$$

即使兩條 strategy 最終答案相同：

$$
g_{\mathrm{success}}(y_1)
=
g_{\mathrm{success}}(y_2),
$$

仍可能：

$$
g_{\mathrm{strategy}}(y_1)
\neq
g_{\mathrm{strategy}}(y_2).
$$

因此 strategy layer 保存 final-answer voting 會消去的結構。

---

# 16. Task Outcome Scale

對任務定義 outcome state space：

$$
\mathcal C_{\mathrm{task}}.
$$

例如：

$$
\{
\mathrm{correct},
\mathrm{partial},
\mathrm{incorrect},
\mathrm{invalid},
\mathrm{abstain}
\}.
$$

由 evaluator：

$$
K_{\mathrm{task}}
:
\mathcal Y
\rightsquigarrow
\mathcal C_{\mathrm{task}},
$$

得到：

$$
\boxed{
P_{\mathrm{task}}
=
(K_{\mathrm{task}})_\star Q.
}
$$

若 evaluator deterministic，改用：

$$
g_{\mathrm{task}}.
$$

---

# 17. Success Probability 與 Capability

令：

$$
S:
\mathcal Y
\rightarrow
[0,1]
$$

為 task score。

定義：

$$
\boxed{
\kappa(q,c)
=
\mathbb E_{Y\sim Q_{q,c}}
[
S(Y)
].
}
$$

稱為：

$$
\boxed{
\text{protocol-conditioned task capability}.
}
$$

若：

$$
S(Y)
=
\mathbf 1_{\{\mathrm{success}\}},
$$

則：

$$
\boxed{
\kappa(q,c)
=
P_{\mathrm{success}}^{(q,c)}.
}
$$

這與 capability calibration 的 query-level expected correctness 概念高度對接。

---

# 18. Response Confidence 與 Capability 不可互換

對單一 sampled output：

$$
y,
$$

可以有：

$$
C_{\mathrm{resp}}(y)
$$

表示回答自身 confidence。

但 capability：

$$
\kappa(q,c)
$$

是：

$$
Y\sim Q_{q,c}
$$

下的 expected success。

因此：

$$
\boxed{
C_{\mathrm{resp}}(y)
\neq
\kappa(q,c)
}
$$

一般成立。

一個 lucky correct sample 可以來自低 capability query。

一個 unlucky wrong sample 也可以來自高 capability query。

---

# 19. 定理二：Repeated-Run Capability Estimation

若：

$$
S(Y_i)\in\{0,1\}
$$

且：

$$
Y_1,\ldots,Y_N
$$

在固定 $q,c$ 下 i.i.d.，令：

$$
\widehat\kappa_N
=
\frac1N
\sum_{i=1}^{N}
S(Y_i).
$$

則：

$$
\mathbb E[
\widehat\kappa_N
]
=
\kappa.
$$

且由 Hoeffding inequality：

$$
\boxed{
\Pr(
|\widehat\kappa_N-\kappa|
\ge\varepsilon
)
\le
2e^{-2N\varepsilon^2}.
}
$$

因此若：

$$
2e^{-2N\varepsilon^2}
\le
\delta,
$$

只需：

$$
\boxed{
N
\ge
\frac{
\log(2/\delta)
}{
2\varepsilon^2
}.
}
$$

---

# 20. 這個 Sample-Complexity Bound 不能亂用

Hosted LLM repeated runs 可能違反 i.i.d.：

- backend routing；
- snapshot replacement；
- safety-policy change；
- retrieval drift；
- context mutation；
- memory update；
- tool availability；
- API behavior change。

所以真正實驗必須先建立：

$$
\boxed{
\text{domain stability evidence}.
}
$$

否則：

$$
\widehat\kappa_N
$$

只是 mixture over changing domains。

---

# 21. Black-Box 與 White-Box Probability Field

## 21.1 White-Box Mode

可存取：

- token logits；
- hidden states；
- model snapshot；
- seed / RNG；
- internal activations。

可直接研究：

$$
P_{\mathrm{token}}
$$

與 sequence law。

## 21.2 Black-Box Mode

只能存取：

$$
\boxed{
\text{input}
\rightarrow
\text{sampled output}.
}
$$

此時可可靠研究：

- empirical semantic distribution；
- answer consistency；
- strategy distribution；
- task distribution；
- success probability。

SelfCheckGPT、black-box consistency UQ 與 conformal abstention 等工作都證明 repeated sampling 本身可形成有效 uncertainty signal。

---

# 22. Multi-Scale Probability Field

本文正式定義：

### 定義 22.1

固定：

$$
q,c,
$$

AI Multi-Scale Probability Field 為：

$$
\boxed{
\mathfrak F_{\mathrm{AI}}(q,c)
=
\left(
Q_{q,c},
\{
P_L^{(q,c)}
\}_{L\in\Lambda},
\{
K_L
\}_{L\in\Lambda}
\right),
}
$$

其中：

$$
\Lambda
=
\{
\mathrm{surface},
\mathrm{semantic},
\mathrm{strategy},
\mathrm{task},
\mathrm{success}
\}.
$$

若 white-box token law 可取得，另加入：

$$
\{
p_t
\}_{t=1}^{T}.
$$

---

# 23. Entropy Profile

定義：

$$
\boxed{
\mathbf H(q,c)
=
(
\bar H_{\mathrm{token}},
H_{\mathrm{surface}},
H_{\mathrm{semantic}},
H_{\mathrm{strategy}},
H_{\mathrm{task}}
).
}
$$

這是一個：

$$
\boxed{
\text{profile},
}
$$

不是單調階梯。

只有當兩層之間確實為 deterministic quotient 時，才能使用 entropy monotonicity / chain decomposition。

---

# 24. 不應預設「越高層 entropy 越低」

舊草案可能直覺期待：

$$
H_{\mathrm{token}}
>
H_{\mathrm{semantic}}
>
H_{\mathrm{strategy}}
>
H_{\mathrm{task}}.
$$

本文不把此式當公理。

理由：

- token entropy 是 conditional local entropy；
- semantic entropy 是 run-level quotient entropy；
- strategy classifier 可能不是 semantic quotient；
- task outcome space 可能有更多 meaningful states；
- stochastic classifier 可以增加 apparent uncertainty。

所以：

$$
\boxed{
\text{cross-scale entropy ordering must be tested, not assumed}.
}
$$

---

# 25. Scale Sensitivity Spectrum

考慮 protocol perturbation：

$$
c
\rightarrow
c'.
$$

例如：

- temperature；
- memory；
- system prompt；
- tool access；
- model snapshot；
- intention constraint。

對每尺度：

$$
L,
$$

定義：

$$
\boxed{
\Delta_L(c,c')
=
D_L
\left(
P_L^{(c)},
P_L^{(c')}
\right).
}
$$

由此得到：

$$
\boxed{
\mathbf\Delta(c,c')
=
(
\Delta_{\mathrm{surface}},
\Delta_{\mathrm{semantic}},
\Delta_{\mathrm{strategy}},
\Delta_{\mathrm{task}}
).
}
$$

稱為 scale sensitivity spectrum。

---

# 26. Temperature Experiment 的正式版本

對：

$$
T_1,\ldots,T_k,
$$

建立：

$$
P_L^{(T_i)}.
$$

不再只問：

> temperature 是否讓回答變多樣？

而問：

$$
\boxed{
T
\mapsto
\Delta_L(T,T_0)
}
$$

在每個尺度如何變動。

例如可能觀察：

$$
\Delta_{\mathrm{surface}}
\gg
\Delta_{\mathrm{strategy}}.
$$

這意味：

> temperature 主要增加表面生成差異，但策略分布相對穩定。

這是一個實驗命題，不是理論預設。

---

# 27. Memory Reshaping Experiment

固定其他 protocol，只改 memory state：

$$
m_0
\rightarrow
m_1.
$$

定義：

$$
\boxed{
\Delta_L^{\mathrm{memory}}
=
D_L(
P_L^{(m_0)},
P_L^{(m_1)}
).
}
$$

若：

$$
\Delta_{\mathrm{strategy}}
\gg
\Delta_{\mathrm{surface}},
$$

表示 memory 主要改變策略選擇。

若：

$$
\Delta_{\mathrm{task}}
\approx0
$$

但：

$$
\Delta_{\mathrm{strategy}}>0,
$$

則可能存在：

$$
\boxed{
\text{strategy reshaping without task-performance change}.
}
$$

---

# 28. Dynamic Probability Field

Paper 07 已建立：

$$
\mathfrak P_{s,t}^{(r)}.
$$

在 AI 中：

$$
\boxed{
P_{L,t}
}
$$

可以追蹤：

- model updates；
- context changes；
- long-term memory；
- user adaptation；
- tool ecosystem；
- policy changes。

因此 longitudinal AI study 必須避免把：

$$
P_{L,t_1}
$$

與：

$$
P_{L,t_2}
$$

直接當作同一 static distribution 的 sampling variation。

---

# 29. Probability Order 在 AI 中的實例

一階：

$$
P_{\mathrm{strategy}}^{(1)}
$$

描述固定 model/context 下的 strategy distribution。

二階：

$$
H_{\mathrm{strategy}}^{(2)}
$$

可以描述不同：

- model snapshots；
- prompt families；
- deployment nodes；
- memory regimes；

上的 strategy distributions 自身如何分布。

flattening：

$$
\mu(
H_{\mathrm{strategy}}^{(2)}
)
$$

只留下平均 strategy law。

若部署差異本身重要，就必須保存二階 probability order。

---

# 30. Probability Field Fingerprint

對 model / deployment：

$$
M,
$$

定義：

$$
\boxed{
\Phi(M)
=
\left(
\{
P_L
\},
\mathbf H,
\{
\Delta_L^{(j)}
\},
\{
\mathcal C_L
\},
\kappa
\right),
}
$$

其中：

- $P_L$：多尺度 distributions；
- $\mathbf H$：entropy profile；
- $\Delta_L^{(j)}$：對 perturbation $j$ 的 sensitivity；
- $\mathcal C_L$：calibration / uncertainty diagnostics；
- $\kappa$：task capability。

這就是更正式的 Probability Field Fingerprint。

---

# 31. Distributional Reproducibility

舊實驗設計已正確指出：

$$
\boxed{
\text{LLM reproducibility}
\neq
\text{verbatim reproducibility}.
}
$$

因此對 replication：

$$
A,
B,
$$

在尺度 $L$ 上比較：

$$
\widehat P_L^{(A)},
\qquad
\widehat P_L^{(B)}.
$$

定義：

$$
\boxed{
D_L(
\widehat P_L^{(A)},
\widehat P_L^{(B)}
)
\le
\varepsilon_L.
}
$$

若成立，稱：

$$
\boxed{
\varepsilon_L\text{-distributionally reproduced at scale }L.
}
$$

---

# 32. Multi-Scale Reproducibility Certificate

一個 study 不應只報：

```text
reproduced: yes
```

而應報：

$$
\boxed{
\boldsymbol\varepsilon
=
(
\varepsilon_{\mathrm{semantic}},
\varepsilon_{\mathrm{strategy}},
\varepsilon_{\mathrm{task}},
\varepsilon_{\mathrm{success}}
).
}
$$

以及：

$$
\boxed{
\mathbf D
=
(
D_{\mathrm{semantic}},
D_{\mathrm{strategy}},
D_{\mathrm{task}},
D_{\mathrm{success}}
).
}
$$

因此可能出現：

- semantic reproducible；
- strategy slightly drifted；
- task outcome reproduced；
- token distribution unavailable。

這比單一 binary reproducibility 更精確。

---

# 33. Evaluator Uncertainty 必須獨立保存

若：

$$
K_{\mathrm{semantic}},
K_{\mathrm{strategy}},
K_{\mathrm{task}}
$$

由另一個 LLM judge 執行，

則 judge 自身也是 stochastic system。

所以實驗必須至少選擇以下一種：

1. deterministic rule / verifier；
2. frozen classifier；
3. repeated judge with judge-distribution estimation；
4. human multi-rater protocol；
5. hybrid rule + judge。

否則：

$$
\boxed{
\text{model uncertainty}
}
$$

與：

$$
\boxed{
\text{evaluator uncertainty}
}
$$

會不可辨識地混合。

---

# 34. Capability Calibration 與 Outcome Distribution

若 task outcome space：

$$
\mathcal C_{\mathrm{task}}
$$

不是 binary，

則：

$$
P_{\mathrm{task}}
$$

比：

$$
P_{\mathrm{success}}
$$

包含更多資訊。

例如：

$$
P_{\mathrm{task}}
=
(
0.60,
0.20,
0.10,
0.05,
0.05
)
$$

對應：

$$
(
\mathrm{correct},
\mathrm{partial},
\mathrm{wrong},
\mathrm{invalid},
\mathrm{abstain}
).
$$

而：

$$
P_{\mathrm{success}}
=
0.60
$$

只是 projection。

因此：

$$
\boxed{
\text{success probability}
}
$$

是 task distribution 的低維 summary，不是完整 task-level probability field。

---

# 35. Coherence Across Scales

若尺度 mapping：

$$
g_{L\rightarrow H}
$$

確實存在，則應驗證：

$$
\boxed{
P_H
=
(g_{L\rightarrow H})_\#P_L.
}
$$

若 observed：

$$
\widehat P_H
$$

與 induced：

$$
(g_{L\rightarrow H})_\#
\widehat P_L
$$

不一致，可定義：

$$
\boxed{
\Delta_{L\rightarrow H}^{\mathrm{coh}}
=
D_H
\left(
\widehat P_H,
(g_{L\rightarrow H})_\#
\widehat P_L
\right).
}
$$

這是 AI probability-field 的跨尺度 coherence test。

---

# 36. Strategy Layer 的可證偽性要求

Strategy probability 若只靠研究者事後「感覺」分類，就不是可靠 probability field。

所以 strategy ontology 必須事前固定：

$$
\mathcal C_{\mathrm{strategy}}
=
\{
S_1,\ldots,S_k
\},
$$

並提供：

- classification rule；
- examples；
- ambiguity policy；
- multi-label policy；
- unknown class；
- inter-rater / judge reliability。

如果 ontology 在看到結果後一直改：

$$
\boxed{
P_{\mathrm{strategy}}
}
$$

就沒有固定判定域。

---

# 37. Open-Set Strategy Space

實際 AI 可能產生事前未定義的策略。

所以可加入：

$$
S_{\mathrm{other}},
$$

或採 open-set classifier。

則：

$$
P_{\mathrm{strategy}}(S_{\mathrm{other}})
$$

本身就是：

$$
\boxed{
\text{strategy ontology incompleteness signal}.
}
$$

如果它持續很高，就應建立新 protocol branch，而不是偷偷重標舊資料。

---

# 38. Locked Study 與 Exploratory Study

正式 probability-field experiment 應分：

## Locked Study

事前固定：

- model；
- task；
- prompts；
- sampling；
- number of runs；
- judge；
- scale mappings；
- analysis rules。

## Exploratory Study

允許修改，但每次修改都建立：

$$
\boxed{
\text{new judgment domain / new protocol version}.
}
$$

不可把新舊 runs 直接混成同一 static distribution。

---

# 39. Evidence Stream

每個 run：

$$
R_i
$$

至少保存：

- exact input bundle；
- exact model identifier；
- sampling configuration；
- timestamps；
- raw output；
- tool calls / retrieved context；
- memory condition；
- evaluation labels；
- hashes。

因此：

$$
\boxed{
\text{probability field requires data provenance}.
}
$$

不是因為 hash 能證明理論正確，而是因為 repeated-run distribution 若沒有 provenance，第三方無法知道哪些 runs 被刪除或條件被改變。

---

# 40. Distributional Evidence 不等於「證明 AI 是概率機器」

即使實驗得到穩定：

$$
P_{\mathrm{strategy}},
$$

也只能說：

> 在指定判定域、protocol 與 repeated-run observation 下，觀察到穩定 empirical distribution。

它不直接證明：

$$
\boxed{
\text{AI 本體上就是純概率系統}.
}
$$

同樣地，低 variance 也不證明 deterministic ontology。

本研究測量的是：

$$
\boxed{
\text{observable distributional behavior}.
}
$$

不是把形上學結論偷渡進統計結果。

---

# 41. 三類 Reproducibility 必須分開

## 41.1 Exact Reproducibility

$$
Y_i^{(A)}
=
Y_i^{(B)}
$$

逐字相同。

Hosted stochastic LLM 通常不應假設這種重現。

## 41.2 Procedural Reproducibility

第三方能重建：

- protocol；
- tasks；
- prompts；
- model family；
- sampling policy；
- evaluation rules。

## 41.3 Distributional Reproducibility

$$
D(
\widehat P^{(A)},
\widehat P^{(B)}
)
\le
\varepsilon.
$$

本文核心追求第三種，同時需要第二種作為其前提。

---

# 42. Experiment Families

本文建議第一批只做四組。

## E1：Temperature Sweep

$$
T
\rightarrow
\mathbf H(T),
\quad
\mathbf\Delta(T,T_0).
$$

## E2：Memory Reshaping

$$
m_0
\rightarrow
m_1
\rightarrow
P_L^{(m)}.
$$

## E3：Prompt / Intention Strength

$$
\beta
\rightarrow
P_{\mathrm{strategy}}^{(\beta)}.
$$

## E4：Repeated-Run Capability

$$
N
\rightarrow
\widehat\kappa_N.
$$

這四組已足以驗證：

$$
\boxed{
\text{不同尺度的概率結構是否會解耦}.
}
$$

---

# 43. 第一個可證偽核心命題

本文提出：

### Conjecture 43.1：Cross-Scale Decoupling

存在某些 AI model / task / protocol，使：

$$
\Delta_{\mathrm{surface}}(c,c')
\gg
\Delta_{\mathrm{strategy}}(c,c'),
$$

或反向：

$$
\Delta_{\mathrm{strategy}}(c,c')
\gg
\Delta_{\mathrm{surface}}(c,c').
$$

如果所有 perturbations 下所有尺度變化始終近似完全同調：

$$
\Delta_L
\approx
a_L\Delta_0
$$

且不存在獨立尺度效應，則多尺度 probability-field hypothesis 會被大幅削弱。

這使理論具有可證偽性。

---

# 44. 第二個可證偽核心命題

### Conjecture 44.1：Stable Probability Fingerprint

對固定 model family 與 protocol class，存在一個跨 task family 仍可辨識的 probability-field fingerprint：

$$
\Phi(M).
$$

若：

$$
\Phi(M)
$$

在小 perturbations 下完全不穩定、跨 batch 不可重現，則「模型具有穩定跨尺度概率指紋」的主張應被拒絕。

---

# 45. 第三個可證偽核心命題

### Conjecture 45.1：Semantic Compression Gap

對某些 generative tasks：

$$
\boxed{
H_{\mathrm{surface}}
-
H_{\mathrm{semantic}}
\gg0.
}
$$

此 gap：

$$
G_{\mathrm{sem}}
=
H_{\mathrm{surface}}
-
H_{\mathrm{semantic}}
=
H(Y\mid C_{\mathrm{sem}})
$$

代表：

$$
\boxed{
\text{表面多樣性中可被語義 quotient 消去的部分}.
}
$$

這一 quantity 可以直接測量 paraphrase / stylistic freedom 與 semantic uncertainty 的分離程度。

---

# 46. 第四個可證偽核心命題

### Conjecture 46.1：Capability–Response Gap

對某些 queries：

$$
C_{\mathrm{resp}}(y)
$$

與：

$$
\kappa(q,c)
$$

可顯著分離。

這一 gap 的存在已受到現代 capability-calibration 研究支持，但不同 task / model 上的穩定結構仍需實驗。

---

# 47. AI Probability Field Schema

一個最小研究物件：

$$
\boxed{
\mathcal E_{\mathrm{AIPF}}
=
(
\mathfrak D,
q,
Q,
\{K_L\},
\{P_L\},
\mathbf H,
\kappa,
\mathbf\Delta,
\mathbf R
).
}
$$

其中：

- $\mathfrak D$：AI judgment domain；
- $q$：task/query；
- $Q$：run-level output law；
- $K_L$：scale mappings；
- $P_L$：scale distributions；
- $\mathbf H$：entropy profile；
- $\kappa$：capability；
- $\mathbf\Delta$：condition sensitivity；
- $\mathbf R$：reproducibility metrics。

---

# 48. 與前七篇的正式對接

Paper 02：

$$
\boxed{
\text{每個 AI probability 都必須帶判定域}.
}
$$

Paper 03：

$$
\boxed{
\text{跨尺度 probability 需要 transport witness}.
}
$$

Paper 04：

$$
\boxed{
\text{token / semantic / strategy / task 形成 scale geometry}.
}
$$

Paper 05：

$$
\boxed{
\text{不同 deployment distributions 還可形成 higher-order probability}.
}
$$

Paper 06：

$$
\boxed{
\text{discrete token layer 與 continuous latent layer 可以具有不同 point ontology}.
}
$$

Paper 07：

$$
\boxed{
\text{model / memory / context 隨時間更新時，概率場本身動態演化}.
}
$$

所以本文不是孤立 AI 指標集合，而是前七篇數學框架的第一個完整實驗 projection。

---

# 49. 新穎性邊界

本文不宣稱首次提出：

- next-token probability；
- sequence likelihood；
- LLM calibration；
- self-consistency；
- semantic entropy；
- semantic uncertainty；
- black-box sampling UQ；
- conformal abstention；
- repeated-run evaluation；
- capability calibration。

本文真正提出的整合框架是：

$$
\boxed{
\text{Run-Level Law}
\rightarrow
\text{Multi-Scale Probability Projections}
\rightarrow
\text{Dynamic / Recursive Judgment-Domain Field}.
}
$$

其中主要新增概念候選為：

1. strategy probability as an explicit typed experimental scale；
2. task distribution 與 scalar success capability 的分離；
3. scale sensitivity spectrum；
4. cross-scale coherence defect；
5. multi-scale distributional reproducibility certificate；
6. AI Probability Field Fingerprint as a structured family；
7. 把 token / semantic / strategy / task / success 全部接入 JDPSP 的 scale–time–order framework。

---

# 50. 結論

本文把早期 AI Probability Field 的直覺：

$$
H_{\mathrm{token}},
H_{\mathrm{semantic}},
H_{\mathrm{strategy}},
H_{\mathrm{task}},
P_{\mathrm{success}}
$$

改寫成同一 run-level output law：

$$
Q_{q,c}
$$

在不同判定尺度上的 projections：

$$
\boxed{
P_L
=
(K_L)_\star Q_{q,c}.
}
$$

這帶來第一個重要結論：

$$
\boxed{
\text{不同尺度概率不是彼此獨立神祕來源}.
}
$$

它們可以來自同一生成 law，但經不同 quotient、classifier、evaluator 或 stochastic kernel 形成。

第二個重要結果是：

$$
\boxed{
H(Y)
=
H(C_{\mathrm{sem}})
+
H(Y\mid C_{\mathrm{sem}}).
}
$$

所以表面文字變化與 semantic uncertainty 可以被嚴格分離。

第三個核心是 task capability：

$$
\boxed{
\kappa(q,c)
=
\mathbb E[
S(Y)
].
}
$$

它與單一回答的 response confidence 不同。

對 binary repeated runs，在 i.i.d. condition 下：

$$
\boxed{
N
\ge
\frac{
\log(2/\delta)
}{
2\varepsilon^2
}
}
$$

即可給出 Hoeffding 型 capability-estimation 保證。

第四個核心則是：

$$
\boxed{
\text{distributional reproducibility}.
}
$$

AI 不需要每次逐字輸出一樣，才能稱研究可重現。

真正需要的是：

$$
\boxed{
D_L(
\widehat P_L^{(A)},
\widehat P_L^{(B)}
)
\le
\varepsilon_L
}
$$

在明確 protocol 下跨尺度成立。

因此 AI Probability Field 最終成為：

$$
\boxed{
\mathfrak F_{\mathrm{AI}}
=
(
Q,
\{P_L\},
\{K_L\},
\mathbf H,
\kappa,
\mathbf\Delta,
\mathbf R
).
}
$$

如果再帶入前篇的時間與概率階：

$$
\boxed{
\mathfrak P_{L,t}^{(r)},
}
$$

就得到：

$$
\boxed{
\text{AI 的多尺度、動態、遞歸概率場}.
}
$$

至此，本系列前八篇的抽象概率結構已第一次真正落到可運行的 AI repeated-run experiment。

下一篇 Paper 09 將完成 Series I 的總收斂：

$$
\boxed{
\text{超概率統一框架：判定域、尺度、遞歸與動態概率的公理化}.
}
$$

---

# 參考文獻

[1] Neo.K. (2026). *AI Probability Field Live Evidence Stream v0.1*. EveMissLab internal research protocol.

[2] Kadavath, S. et al. (2022). Language Models (Mostly) Know What They Know. arXiv:2207.05221.

[3] Wang, X. et al. (2022). Self-Consistency Improves Chain of Thought Reasoning in Language Models. arXiv:2203.11171.

[4] Kuhn, L., Gal, Y., & Farquhar, S. (2023). Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation. arXiv:2302.09664.

[5] Manakul, P., Liusie, A., & Gales, M. J. F. (2023). SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. arXiv:2303.08896.

[6] Kossen, J. et al. (2024). Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs. arXiv:2406.15927.

[7] Nikitin, A., Kossen, J., Gal, Y., & Marttinen, P. (2024). Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities. arXiv:2405.20003.

[8] Yadkori, Y. A. et al. (2024). Mitigating LLM Hallucinations via Conformal Abstention. arXiv:2405.01563.

[9] Wang, Z. et al. (2024). ConU: Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees. arXiv:2407.00499.

[10] Xiao, Q. et al. (2025). The Consistency Hypothesis in Uncertainty Quantification for Large Language Models. arXiv:2506.21849.

[11] McCabe, L. H., Melamed, R., Hartvigsen, T., & Huang, H. H. (2025). Estimating Semantic Alphabet Size for LLM Uncertainty Quantification. arXiv:2509.14478.

[12] Yang, S.-H. et al. (2026). On Calibration of Large Language Models: From Response To Capability. arXiv:2602.13540.

[13] Müller, P., Popovič, N., Färber, M., & Steinbach, P. (2026). Benchmarking Uncertainty Calibration in Large Language Model Long-Form Question Answering. arXiv:2602.00279.

[14] Matta, K., Naphade, A., & Zou, A. (2026). Rethinking Uncertainty Evaluation in Large Language Models. arXiv:2607.19367.

[15] Iwase, N., Ichihara, Y., Quamar, M. A., & Komiyama, J. (2026). Reliable Chain-of-Thought via Prefix Consistency. arXiv:2605.07654.

---

# Appendix A. 最小符號表

| 符號 | 意義 |
|---|---|
| $Q_{q,c}$ | fixed query/protocol 的 run-level output law |
| $\widehat Q_N$ | empirical run law |
| $K_L$ | output-to-scale stochastic classifier / transport |
| $g_L$ | deterministic scale mapping |
| $P_L$ | scale- $L$ probability distribution |
| $H_{\mathrm{tok},t}$ | token-step entropy |
| $H_{\mathrm{semantic}}$ | semantic-class entropy |
| $P_{\mathrm{strategy}}$ | strategy class distribution |
| $P_{\mathrm{task}}$ | task outcome distribution |
| $\kappa(q,c)$ | protocol-conditioned task capability |
| $\Delta_L(c,c')$ | scale sensitivity |
| $\Delta_{L\to H}^{\mathrm{coh}}$ | cross-scale coherence defect |
| $\Phi(M)$ | AI probability-field fingerprint |

# Appendix B. AI Probability Field Run Schema

```text
study:
  study_id:
  protocol_version:
  locked_or_exploratory:

task:
  domain:
  subdomain:
  task_id:
  query_hash:

model:
  provider:
  model_name:
  exact_model_id:
  snapshot:
  api_version:

prompt_bundle:
  system_hash:
  developer_hash:
  user_hash:
  fewshot_hash:
  retrieved_context_hash:

sampling:
  temperature:
  top_p:
  max_tokens:
  seed:
  reasoning_mode:

dynamic_context:
  memory_state:
  tools_enabled:
  tool_policy:
  intention_condition:
  timestamp:

run:
  run_id:
  sequence_number:
  raw_output:
  output_hash:

scale_labels:
  semantic:
  strategy:
  task:
  success:

evaluator:
  semantic_judge:
  strategy_judge:
  task_verifier:
  judge_snapshot:
  deterministic_or_stochastic:

analysis:
  token_entropy:
  semantic_entropy:
  strategy_entropy:
  task_entropy:
  success_rate:

evidence:
  previous_event_hash:
  event_hash:
  batch_root:
  timestamp_commit:
```

# Appendix C. Multi-Scale Reproducibility Record

```text
source_study:
replication_study:

protocol_equivalence:
model_equivalence:
task_equivalence:
evaluator_equivalence:

scales:
  semantic:
    divergence:
    tolerance:
    reproduced:
  strategy:
    divergence:
    tolerance:
    reproduced:
  task:
    divergence:
    tolerance:
    reproduced:
  success:
    absolute_gap:
    confidence_interval:
    reproduced:

overall_status:
  exact_reproduction:
  procedural_reproduction:
  distributional_reproduction:
```
