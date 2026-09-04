---
title: "TCFT-03｜反身性推理：當推理本身進入被推理世界"
title_en: "Reflexive Reasoning: When Reasoning Itself Enters the World Being Reasoned About"
series: "Temporal Cognitive Frontier Theory (TCFT) / 時代認知前沿理論"
paper_no: "03"
version: "v0.1"
date: "2026-08-31"
author: "Neo.K"
affiliation: "EveMissLab / 一言諾科技有限公司"
document_type: "理論論文 / Reflexive Reasoning 篇"
language: "zh-Hant"
status: "正式系列初稿"
previous_paper: "TCFT-02｜反事實視界：未發生世界、問題生成與認知覆蓋"
next_paper: "TCFT-04｜高階推理不等於高階策略：認知成本、注意力分配與停止治理"
---

# TCFT-03｜反身性推理：當推理本身進入被推理世界

## Reflexive Reasoning: When Reasoning Itself Enters the World Being Reasoned About

**系列：** Temporal Cognitive Frontier Theory, TCFT / 時代認知前沿理論  
**篇次：** 03  
**版本：** v0.1  
**日期：** 2026-08-31  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  

---

## 摘要

自指、後設認知、二階控制論、心智理論、遞歸信念、self-fulfilling prophecy、performative prediction 與社會科學中的 reflexivity 都處理某種「系統把自己、觀察者、模型或預測重新納入系統」的現象。然而，這些概念的研究對象並不相同：自指處理表示對自身的指涉；後設認知處理 object-level cognition 與 meta-level monitoring/control；高階 Theory of Mind 處理巢狀信念；二階控制論處理 observing system；performative prediction 處理預測部署後改變其 target distribution；社會反身性則處理參與者信念、行動與制度結果之間的雙向回饋。

本文提出 Temporal Cognitive Frontier Theory（TCFT）中的 **Reflexive Reasoning（反身性推理，RR）** 工作框架，目的不是宣稱上述傳統都屬於同一理論，也不是把「反思自己」重新命名，而是建立一個可操作的共同核心：

$$
\boxed{
\text{A reasoning process is reflexive when
the reasoner, its model, its reasoning output,
or the consequences of that output
become endogenous variables of the next reasoning state.}
}
$$

設世界狀態為 $\mathbf W_t$，observer-relative presentation 為 $P_t$，agent model 為 $M_t$，推理程序為 $R_t$，推理輸出為 $y_t$。最小反身迴路可寫為：

$$
\boxed{
y_t
=
R_t(P_t,M_t,q_t)
}
$$

$$
\boxed{
a_t
=
\pi_t(y_t,M_t)
}
$$

$$
\boxed{
\mathbf W_{t+1}
=
F(
\mathbf W_t,
a_t,
d_t,
\mathcal A_t
)
}
$$

$$
\boxed{
P_{t+1}
=
\rho_{O,t+1}(\mathbf W_{t+1})
}
$$

$$
\boxed{
M_{t+1}
=
U_M(
M_t,
P_{t+1},
y_t,
a_t
)
}
$$

若推理程序本身也被修改：

$$
\boxed{
R_{t+1}
=
U_R(
R_t,
M_{t+1},
H_{t+1}
),
}
$$

則形成更強的 **operator-reflexive loop**。其中 $d_t$ 可表示 disclosure / publication / communication，即推理結果是否被外界觀察； $\mathcal A_t$ 表示其他 agents 的反應。

本文進一步區分五種反身性：**epistemic reflexivity、self-model reflexivity、social-recursive reflexivity、performative reflexivity、operator reflexivity**。它們可以重疊，但不應被偷換。特別地：

$$
\boxed{
\text{Self-Reference}
\neq
\text{Metacognition}
\neq
\text{Recursive ToM}
\neq
\text{Performativity}
\neq
\text{Reflexive Reasoning}.
}
$$

本文亦提出 **Reflexive Counterfactual**：反事實不只修改外部世界條件，還修改「agent 是否相信、公開、採取或隱藏某項推理」：

$$
\boxed{
RCF(a,p,d)
=
\operatorname{Sim}
(
\mathbf W_{t+k}
\mid
A\text{ believes }p,
A\text{ acts }a,
Disclosure=d
).
}
$$

這使 TCFT-02 的 Counterfactual Horizon 擴展為：

$$
\boxed{
\mathcal C_i^{RR}(t)
\supseteq
\mathcal C_i(t),
}
$$

因為被推理者會回應推理者，而推理結果本身可能改變未來支撐。

本文同時提出 **Reflexive Contamination、Self-Confirmation Loop、Probe-Induced Evidence、Reflexive Blindspot** 與 **Reflexive Stability**。若 agent 的模型產生行為，該行為使世界產生與原模型一致的證據，再被 agent 當成獨立支持，便可能形成高度自洽但錯誤的閉環。因此成熟 RR 必須保存：

$$
\boxed{
\text{Model-Generated Evidence}
\neq
\text{Independent Evidence}.
}
$$

TCFT-03 最後把 RR 接回 Cognitive Operator-Domain Theory（CODT）。本文不把 RR 宣告為新的 promoted cognitive domain，而把它暫時定義為一類 **candidate operator program / topology**。在 CODT-09 的 cognition-world loop：

$$
P_t
\rightarrow
A_t^{request}
\rightarrow
CWB_t
\rightarrow
\mathbf W_{t+1}
\rightarrow
P_{t+1}
$$

之上加入 model update、disclosure、other-agent response 與 reasoning-program update，即可形成可審計的 reflexive extension。

本文的中心命題為：

$$
\boxed{
\text{High-level prediction is not fully specified
until the predictor models how prediction, disclosure,
action, and model revision can alter the predicted world.}
}
$$

但反身性深度本身不等於高階策略。多想一層是否值得，仍取決於資訊增益、決策影響、成本、機會成本與停止條件；這將由 TCFT-04 專門處理。

**關鍵詞：** 反身性推理、反身性、performative prediction、後設認知、遞歸心智理論、自我模型、觀察者、反身性反事實、自我證成、CODT、TCFT

---

# Abstract

Self-reference, metacognition, second-order cybernetics, Theory of Mind, recursive belief reasoning, self-fulfilling prophecy, performative prediction, and social-scientific reflexivity all study systems in which some representation, observer, belief, prediction, or model re-enters the system. They are not equivalent. Self-reference concerns representation referring to itself; metacognition concerns monitoring and control across object and meta levels; recursive Theory of Mind concerns nested beliefs; second-order cybernetics concerns observing systems; performative prediction concerns deployed predictions changing the distribution being predicted; social reflexivity concerns feedback among beliefs, actions, and institutional outcomes.

This paper introduces a working framework for **Reflexive Reasoning (RR)** within Temporal Cognitive Frontier Theory (TCFT). The goal is not to collapse these traditions into one theory, but to isolate an operational core:

$$
\boxed{
\text{A reasoning process is reflexive when
the reasoner, its model, its reasoning output,
or the consequences of that output
become endogenous variables of the next reasoning state.}
}
$$

Let $\mathbf W_t$ denote world state, $P_t$ an observer-relative presentation, $M_t$ the agent's model, $R_t$ its reasoning program, and $y_t$ the reasoning output. A minimal reflexive loop includes reasoning, action or disclosure, world transition, new presentation, model update, and—at stronger levels—reasoning-program update.

We distinguish epistemic reflexivity, self-model reflexivity, social-recursive reflexivity, performative reflexivity, and operator reflexivity. We further introduce **Reflexive Counterfactuals**, in which the counterfactual intervention includes what the reasoner believes, publishes, conceals, or acts upon. This extends the counterfactual horizon of TCFT-02.

The paper identifies several epistemic hazards: reflexive contamination, self-confirmation loops, probe-induced evidence, and reflexive blindspots. Evidence generated by the agent's own intervention cannot automatically be treated as independent confirmation of the model that produced the intervention.

Finally, RR is connected to Cognitive Operator-Domain Theory (CODT). RR is not declared a promoted cognitive domain; it is treated as a candidate operator program/topology extending the existing cognition-world loop with model updates, disclosure, other-agent responses, and reasoning-program updates.

The central proposition is:

$$
\boxed{
\text{High-level prediction is not fully specified
until the predictor models how prediction, disclosure,
action, and model revision can alter the predicted world.}
}
$$

Reflexive depth itself, however, is not strategic optimality. Resource allocation and stopping are deferred to TCFT-04.

**Keywords:** reflexive reasoning; reflexivity; performative prediction; metacognition; recursive theory of mind; self-model; observer; reflexive counterfactual; self-confirmation; CODT; TCFT

---

# 1. 導論：推理者到底在不在世界裡？

很多推理模型隱含：

$$
\boxed{
Reasoner
\notin
WorldModel.
}
$$

也就是：

> 世界在那裡，推理者只是描述它。

在很多物理、工程或封閉問題中，這個近似足夠好。

但在：

- 社會；
- 市場；
- 政治；
- 家庭；
- 談判；
- 多 Agent 系統；
- AI recommendation；
- hiring；
- policing；
- 教育；
- self-regulation；
- strategic interaction；

中，推理者常常就是被推理世界的一部分。

此時：

$$
\boxed{
Reasoner
\in
World.
}
$$

而且：

$$
\boxed{
ReasoningOutput
\rightarrow
WorldTransition.
}
$$

---

# 2. 為什麼「我知道我在想」還不夠

如果 agent 只是：

$$
\text{observe self}
$$

這最多是某種 self-monitoring。

若：

$$
\text{observe cognition}
\rightarrow
\text{change cognition},
$$

較接近 metacognitive control。

但 TCFT 的 reflexive reasoning 要求更強：

$$
\boxed{
\text{reasoning state}
\rightarrow
\text{world / agent change}
\rightarrow
\text{new reasoning problem}.
}
$$

反身性不是單純 introspection。

---

# 3. 五個概念必須先分開

## 3.1 Self-Reference

自指最小可以表示：

$$
S\rightarrow S.
$$

一個命題、符號或程序指向自己。

它可能完全沒有外部 world effect。

所以：

$$
\boxed{
\text{SelfReference}
\not\Rightarrow
\text{ReflexiveWorldInteraction}.
}
$$

---

## 3.2 Metacognition

經典 metacognition 具有：

$$
\boxed{
\text{Object Level}
\leftrightarrow
\text{Meta Level}.
}
$$

通常分成：

$$
\boxed{
\text{Monitoring}
}
$$

與：

$$
\boxed{
\text{Control}.
}
$$

meta-level 取得 object-level cognition 的資訊，再反過來調節 learning、attention、strategy 或 termination。

但：

$$
\boxed{
\text{Metacognition}
\not\Rightarrow
\text{World Performativity}.
}
$$

---

## 3.3 Recursive Theory of Mind

如果 agent $A$ 模型化：

$$
M_A(B),
$$

是第一階他者模型。

更高階：

$$
M_A(M_B(A)).
$$

再高：

$$
M_A(M_B(M_A(B))).
$$

這是 nested belief / recursive perspective。

但它仍然可能只是 internal inference。

所以：

$$
\boxed{
\text{Recursive ToM}
\not\Rightarrow
\text{Performative Reflexivity}.
}
$$

---

## 3.4 Performative Prediction

若 prediction：

$$
p_t
$$

部署後影響行動，

進而改變它要預測的 distribution：

$$
D_{t+1}
=
D(p_t),
$$

則形成：

$$
\boxed{
\text{Performative Prediction}.
}
$$

這已是現代 machine learning 的正式研究問題。

---

## 3.5 Reflexive Reasoning

TCFT 的 RR 更一般地問：

$$
\boxed{
\text{Does the reasoning loop explicitly include
its own model, output, action, disclosure,
and induced consequences?}
}
$$

因此：

$$
\boxed{
\text{Self-Reference}
\neq
\text{Metacognition}
\neq
\text{Recursive ToM}
\neq
\text{Performativity}
\neq
\text{RR}.
}
$$

但 RR 可以調用前述機制。

---

# 4. 最小 Reflexive Reasoning Loop

令：

$$
\mathbf W_t
$$

為 world state。

observer $O$ 取得：

$$
\boxed{
P_t
=
\rho_{O,t}(\mathbf W_t).
}
$$

agent 持有 model：

$$
M_t.
$$

對問題：

$$
q_t,
$$

推理：

$$
\boxed{
y_t
=
R_t(P_t,M_t,q_t).
}
$$

---

# 5. 推理結果轉成行動

推理輸出本身不必直接改變世界。

需要 policy：

$$
\boxed{
a_t
=
\pi_t(
y_t,M_t,G_t
),
}
$$

其中：

$$
G_t
$$

可以表示 goal / policy state。

---

# 6. Disclosure 必須獨立

推理可能：

- 保持私人；
- 部分公開；
- 全部公開；
- 對特定 agent 公開；
- 被洩漏。

因此定義：

$$
\boxed{
d_t
=
DisclosurePolicy(y_t).
}
$$

這非常重要。

因為：

$$
\boxed{
\text{Private Prediction}
\neq
\text{Public Prediction}.
}
$$

兩者可能產生不同世界。

---

# 7. World Transition

一般：

$$
\boxed{
\mathbf W_{t+1}
=
F(
\mathbf W_t,
a_t,
d_t,
\mathcal A_t,
\eta_t
).
}
$$

其中：

- $\mathcal A_t$：其他 agents；
- $\eta_t$：未建模環境因素。

所以：

$$
\boxed{
y_t
}
$$

可能透過：

$$
a_t
$$

或：

$$
d_t
$$

間接成為 world variable。

---

# 8. 新 Presentation

world transition 後：

$$
\boxed{
P_{t+1}
=
\rho_{O,t+1}
(
\mathbf W_{t+1}
).
}
$$

注意：

$$
P_{t+1}
\neq
\mathbf W_{t+1}.
$$

這延續 CODT 的 observer-relative presentation。

---

# 9. Model Update

agent 根據：

$$
P_{t+1}
$$

更新：

$$
\boxed{
M_{t+1}
=
U_M(
M_t,
P_{t+1},
y_t,
a_t,
d_t,
H_t
).
}
$$

若沒有這一步，

就只是：

$$
\text{action feedback}
$$

而不是完整認知迴路。

---

# 10. Operator / Program Update

更強 RR 允許：

$$
\boxed{
R_{t+1}
=
U_R(
R_t,
M_{t+1},
H_{t+1}
).
}
$$

也就是：

> 我不只是修正答案。

> 我修正下一輪怎麼推。

這是：

$$
\boxed{
\text{Operator Reflexivity}.
}
$$

---

# 11. Canonical RR Loop Candidate

因此最小整體：

$$
\boxed{
\begin{aligned}
P_t
&\rightarrow
R_t
\rightarrow
y_t
\rightarrow
(a_t,d_t)
\rightarrow
\mathbf W_{t+1}
\\
&\rightarrow
P_{t+1}
\rightarrow
M_{t+1}
\rightarrow
R_{t+1}.
\end{aligned}
}
$$

這是 TCFT-03 的 canonical loop candidate。

---

# 12. Epistemic Reflexivity

第一類：

$$
\boxed{
RR^{epi}.
}
$$

agent 把：

- 自己的 representation；
- assumptions；
- uncertainty；
- model limitations；
- evidence-selection procedure；

納入推理。

例如：

> 我的答案依賴哪些分類？

> 如果分類本身不同會怎樣？

這是 epistemic reflexivity。

---

# 13. Self-Model Reflexivity

第二類：

$$
\boxed{
RR^{self}.
}
$$

agent 把自己的：

- goals；
- beliefs；
- biases；
- memory；
- abilities；
- resource constraints；

當成被推理對象。

例如：

$$
M_A(A).
$$

---

# 14. Social-Recursive Reflexivity

第三類：

$$
\boxed{
RR^{soc}.
}
$$

agent 模型：

$$
M_A(B),
$$

以及：

$$
M_A(M_B(A)).
$$

這和 recursive ToM 高度相交。

2026 的 RecToM 顯示 recursive perspective construction 可以顯著提高 higher-order ToM benchmark 表現；這支持「nested perspective 需要顯式結構」這一研究方向，但不等於 TCFT RR 已被證明。

---

# 15. Performative Reflexivity

第四類：

$$
\boxed{
RR^{perf}.
}
$$

prediction / model deployment：

$$
p_t
$$

改變 target：

$$
D_{t+1}=D(p_t).
$$

例如：

- 推薦模型改變消費；
- 警務預測改變巡邏；
- 市場預測改變交易；
- 評分系統改變受評者行為。

---

# 16. Operator Reflexivity

第五類：

$$
\boxed{
RR^{op}.
}
$$

推理結果改變：

$$
R_{t+1}.
$$

例如：

$$
\text{Reasoning Failure}
\rightarrow
\text{Strategy Revision}.
$$

這比：

$$
M_{t+1}\neq M_t
$$

更強。

---

# 17. 五類可以重疊

一個高階 social decision 可能同時有：

$$
RR^{epi}
+
RR^{self}
+
RR^{soc}
+
RR^{perf}
+
RR^{op}.
$$

但不能因此宣稱：

$$
\text{all reflexivity is one mechanism}.
$$

TCFT 只提供共同接口。

---

# 18. Reflexive Depth

定義反身嵌套深度：

$$
\boxed{
d_R.
}
$$

例如：

$$
d_R=0
$$

表示只推 external world。

$$
d_R=1
$$

加入：

$$
M_A(A)
$$

或：

$$
M_A(B).
$$

更高：

$$
M_A(M_B(A)).
$$

---

# 19. Depth 不等於 Iteration Count

如果同一層：

$$
M_A(B)
$$

更新 100 次，

不等於：

$$
d_R=100.
$$

因此：

$$
\boxed{
\text{Reflexive Depth}
\neq
\text{Temporal Iteration}.
}
$$

---

# 20. Reflexive Breadth

agent 可能同時模型：

$$
B_1,\ldots,B_n.
$$

因此：

$$
\boxed{
Breadth_R
}
$$

是另一軸。

一個 agent 可以 depth 很高但只盯一個人。

另一個 depth 較低但同時考慮：

- self；
- target；
- third parties；
- institutions；
- environment。

---

# 21. Relationship Model 不等於 Person Model

若：

$$
M_A(B)
$$

非常精細，

仍不代表：

$$
M_A(R_{AB})
$$

完整。

因為：

$$
R_{AB}
$$

還依賴：

$$
\boxed{
A,
B,
ThirdParties,
Environment,
History,
Institutions,
FutureEvents.
}
$$

因此：

$$
\boxed{
\text{High-Resolution Person Model}
\not\Rightarrow
\text{High-Resolution Relationship Model}.
}
$$

---

# 22. Social Reflexive Loop

最小雙 agent：

$$
A
\leftrightarrow
B.
$$

A 模型 B：

$$
M_A(B).
$$

A 行動：

$$
a_A.
$$

B 觀察：

$$
P_B(a_A).
$$

B 更新：

$$
M_B(A).
$$

B 行動：

$$
a_B.
$$

A 再更新。

所以：

$$
\boxed{
M_A(B)_t
\rightarrow
a_A
\rightarrow
M_B(A)_{t+1}
\rightarrow
a_B
\rightarrow
M_A(B)_{t+1}.
}
$$

---

# 23. Recursive ToM 不是無限必要

理論上可以：

$$
M_A(M_B(M_A(M_B(\cdots)))).
$$

但實務上：

$$
\boxed{
d_R
}
$$

應被 budget 約束。

這也是 TCFT-04 的直接接口。

---

# 24. Reflexive Counterfactual

TCFT-02 的一般 counterfactual：

$$
c
=
do(X=x').
$$

RR 加入：

$$
\boxed{
\text{belief},
\text{prediction},
\text{disclosure},
\text{action}.
}
$$

因此：

$$
\boxed{
RCF(a,p,d)
=
\operatorname{Sim}(
\mathbf W_{t+k}
\mid
A\text{ believes }p,
A\text{ acts }a,
Disclosure=d
).
}
$$

---

# 25. 私人預測與公開預測

考慮同一 prediction：

$$
p.
$$

私人情況：

$$
\boxed{
P(
W_{t+1}
\mid
p,
d=private
).
}
$$

公開情況：

$$
\boxed{
P(
W_{t+1}
\mid
p,
d=public
).
}
$$

一般：

$$
\boxed{
P(
W_{t+1}
\mid
p,private
)
\neq
P(
W_{t+1}
\mid
p,public
).
}
$$

---

# 26. Self-Fulfilling Prediction

若：

$$
p
$$

使 agents 行動，

而行動提高：

$$
P(Y=p),
$$

則：

$$
\boxed{
\text{Self-Fulfilling}.
}
$$

但命中不能直接被解讀成：

> prediction 原本就準。

因為 prediction 可能參與製造 outcome。

---

# 27. Self-Negating Prediction

反過來，

若：

$$
p
$$

被公開後使 agents 避免：

$$
p,
$$

則：

$$
\boxed{
\text{Self-Negating}.
}
$$

例如：

> 預測災害使制度提前防範，所以災害未發生。

此時：

$$
\boxed{
\text{PredictionFailure}
\not\Rightarrow
\text{BadReasoning}.
}
$$

---

# 28. 這直接改變 TCFT 的預測評分

一般 forecasting：

$$
Score(
p,
Y
).
$$

反身環境需要額外記錄：

$$
\boxed{
Disclosure,
Intervention,
Response,
Outcome.
}
$$

否則：

$$
Y
$$

不是 exogenous outcome。

---

# 29. Performative Stability

performative prediction 研究已提出：

$$
\boxed{
\text{performative stability}.
}
$$

直覺是 predictor 在自己部署後所誘發的 distribution 上達到穩定。

TCFT 借用其精神，但不把：

$$
\text{performative stability}
$$

直接等同：

$$
\text{reflexive rationality}.
$$

一個穩定點也可能：

- 不公平；
- 不理想；
- path-dependent；
- 局部；
- self-reinforcing。

---

# 30. Reflexive Stability

本文暫定：

$$
\boxed{
RS_i
}
$$

為一種更一般候選：

若：

$$
R_t,
M_t,
a_t,
W_t
$$

反覆更新後，

某些 task-relevant 關係進入：

$$
\epsilon
$$

穩定區：

$$
\boxed{
D(
S_{t+1}^{RR},
S_t^{RR}
)
<\epsilon.
}
$$

這可以叫：

$$
\boxed{
\epsilon\text{-Reflexive Stability}.
}
$$

---

# 31. Stability 不是 Truth

如果整個系統共同進入錯誤 equilibrium：

$$
\boxed{
\text{Stable}
\not\Rightarrow
\text{True}.
}
$$

這點非常重要。

---

# 32. Self-Confirmation Loop

agent 有 hypothesis：

$$
H.
$$

根據 $H$ 行動：

$$
a(H).
$$

行動改變世界：

$$
W'
=
F(W,a(H)).
$$

世界產生：

$$
E_H.
$$

agent 再用：

$$
E_H
$$

支持：

$$
H.
$$

形成：

$$
\boxed{
H
\rightarrow
a(H)
\rightarrow
E_H
\rightarrow
H.
}
$$

這是：

$$
\boxed{
\text{Self-Confirmation Loop}.
}
$$

---

# 33. Model-Generated Evidence

因此證據要分：

$$
\boxed{
E^{ind}
}
$$

與：

$$
\boxed{
E^{endo}.
}
$$

其中：

- $E^{ind}$：相對獨立 evidence；
- $E^{endo}$：由 model-driven intervention 參與生成的 evidence。

必須保持：

$$
\boxed{
E^{endo}
\neq
E^{ind}.
}
$$

---

# 34. Reflexive Contamination

若 agent 忘記：

$$
E
$$

是自己的 intervention 產生，

就會高估：

$$
P(H\mid E).
$$

本文稱：

$$
\boxed{
\text{Reflexive Contamination}.
}
$$

---

# 35. Active Probe

有時 agent 故意：

$$
a_{probe}
$$

測試另一個 agent：

$$
B.
$$

例如故意說一句話、改變行為、投放訊息，觀察回應。

則 observation：

$$
O_B
$$

必須寫成：

$$
\boxed{
O_B
\mid
do(a_{probe}).
}
$$

而不是：

$$
O_B
$$

的自然觀察。

---

# 36. Probe-Induced Evidence

因此：

$$
\boxed{
Evidence(B\mid do(a_{probe}))
}
$$

不能和：

$$
\boxed{
Evidence(B\mid passive\ observation)
}
$$

混在一起。

本文稱：

$$
\boxed{
\text{Probe-Induced Evidence}.
}
$$

---

# 37. Probe 會改變被推理者

如果 B 知道自己被測：

$$
B
$$

可能再模型：

$$
M_B(A\text{ is probing }B).
$$

所以：

$$
\boxed{
Probe
\rightarrow
TargetModelChange.
}
$$

這使 social reflexivity 迅速升階。

---

# 38. Reflexive Blindspot

TCFT-02 定義 Counterfactual Blindspot。

本文增加：

$$
\boxed{
\text{Reflexive Blindspot}.
}
$$

若 agent 生成很多 external alternatives，

卻漏掉：

> 我的 prediction / publication / action 會改變這個 future。

則：

$$
\boxed{
c^*_{reflexive}
\notin
\mathcal C_i.
}
$$

---

# 39. Reflexive Reversal Witness

更強：

如果加入：

$$
c^*_{RR}
$$

後，

最佳策略翻轉：

$$
\arg\max_a U(a\mid\mathcal C_i)
\neq
\arg\max_a U(a\mid\mathcal C_i\cup\{c^*_{RR}\}),
$$

則稱：

$$
\boxed{
\text{Reflexive Reversal Witness}.
}
$$

---

# 40. Reflexive Horizon

因此：

$$
\boxed{
\mathcal C_i^{RR}(t)
}
$$

表示把：

- self；
- prediction；
- disclosure；
- other-agent response；
- model update；

納入的 counterfactual horizon。

一般：

$$
\boxed{
\mathcal C_i^{RR}
\supseteq
\mathcal C_i.
}
$$

至少在 representation 足夠時成立為概念擴張。

---

# 41. 但 Reflexive Horizon 可能更小

實際 budget 固定時，

加入反身性會增加每個 branch cost。

所以 agent 可能：

$$
|\mathcal C_i^{RR}|
<
|\mathcal C_i|.
$$

因此：

$$
\boxed{
\text{richer branch representation}
\not\Rightarrow
\text{more branches explored}.
}
$$

這又回到資源配置。

---

# 42. Reflexive Base-Space

TCFT-01：

$$
\mathfrak B_i(t)
=
(
\Omega_i,
\mathcal Q_i,
\mathcal R_i,
\Gamma_i,
\mathcal U_i
).
$$

加入反身性後：

$$
\boxed{
\mathfrak B_i^{RR}(t)
}
$$

至少應允許：

$$
\boxed{
\text{agent state},
\text{model state},
\text{disclosure state},
\text{response state}
}
$$

成為候選維度。

---

# 43. Prediction Changes Question

最有意思的是：

$$
q_t
$$

本身可能因：

$$
y_t
$$

改變。

所以：

$$
\boxed{
q_{t+1}
=
QUpdate(
q_t,
y_t,
W_{t+1}
).
}
$$

這代表：

> 答案本身改變了下一題。

---

# 44. Reasoning Changes Problem Space

進一步：

$$
\boxed{
\mathcal Q_{t+1}
\neq
\mathcal Q_t.
}
$$

因此反身性不只改變：

$$
P(Y).
$$

它可能改變：

$$
\boxed{
\text{what questions remain meaningful}.
}
$$

---

# 45. Model Changes Representation

若 failure 顯示：

$$
R_t
$$

無法表示新狀態，

agent 可能改：

$$
\boxed{
\mathcal R_{t+1}
\neq
\mathcal R_t.
}
$$

於是：

$$
\boxed{
\text{Reflexivity}
\rightarrow
\text{Base-Space Reconstruction}.
}
$$

---

# 46. Reflexive Reasoning 與 CODT

CODT 已建立：

$$
\boxed{
Method
=
Program(
Operators,
Topology,
Context,
Policy,
Budget
).
}
$$

因此 RR 不應被直接宣布為 primitive。

---

# 47. RR Operator Recovery Candidate

一個 RR program 可能調用：

$$
\boxed{
\{
Observe,
Represent,
SelfModel,
OtherModel,
Predict,
Generate,
Counterfactual,
MetaMonitor,
Decide,
Act,
Disclose,
Update,
Revise,
Terminate
\}.
}
$$

這只是 candidate decomposition。

不代表已取得 canonical primitive list。

---

# 48. RR 不是自動一個 Cognitive Domain

依 CODT：

$$
\boxed{
Seed
\neq
Candidate
\neq
PromotedDomain.
}
$$

所以：

$$
\boxed{
RR
\not\Rightarrow
PromotedDomain.
}
$$

目前最保守定位：

$$
\boxed{
RR
=
\text{candidate operator program / topology family}.
}
$$

---

# 49. CODT-09 接口

CODT-09 已有：

$$
\boxed{
P_t
\rightarrow
A_t^{request}
\rightarrow
CWB_t
\rightarrow
\mathbf W_{t+1}
\rightarrow
P_{t+1}.
}
$$

TCFT-03 增加：

$$
\boxed{
M_t,
R_t,
y_t,
d_t,
\mathcal A_t,
U_M,
U_R.
}
$$

---

# 50. Extended World-Coupled RR Loop

因此：

$$
\boxed{
\begin{aligned}
P_t
&\rightarrow
(M_t,R_t)
\rightarrow
y_t
\rightarrow
(I_t^{act},d_t)
\\
&\rightarrow
A_t^{request}
\rightarrow
CWB_t
\rightarrow
\mathbf W_{t+1}
\\
&\rightarrow
P_{t+1}
\rightarrow
M_{t+1}
\rightarrow
R_{t+1}.
\end{aligned}
}
$$

這是 CODT-compatible reflexive extension。

---

# 51. Capability 不等於 Authority

即使 RR 很強：

$$
RR_i\gg RR_j,
$$

不能推出：

$$
\boxed{
Authority_i>Authority_j.
}
$$

認知能力與 authority 必須經過不同 legitimacy channel。

這與 CODT 的 CWB separation 一致。

---

# 52. Reflexive Prediction 與 World Mutation 必須分開

不能寫：

$$
\text{I predict}
\Rightarrow
\text{World changed}.
$$

需要：

$$
\boxed{
Prediction
\rightarrow
Disclosure / Action
\rightarrow
Authorization / Interaction
\rightarrow
WorldEffect.
}
$$

這防止 cognition 與 world 被偷換。

---

# 53. Reflexive Reasoning 的時間前沿

對 baseline：

$$
B_t,
$$

候選 agent：

$$
i,
$$

可以研究：

$$
\boxed{
TCA_i^{RR}(t).
}
$$

它問：

> 在同期資訊條件下，agent 是否比 baseline 更早、更完整地把自己的 prediction / disclosure / action / model-update effects 納入未來推演？

---

# 54. Temporal Reflexive Advancement

候選形式：

$$
\boxed{
TCA_i^{RR}(t)
=
f(
ReflexiveDepth,
ReflexiveBreadth,
PerformativityAwareness,
NestedBeliefQuality,
SelfModelQuality,
ReversalDetection,
Cost,
Integrity
).
}
$$

仍然偏好多維向量。

---

# 55. 歷史人物中的 RR

對歷史人物不能因一句：

> 他知道人會反應。

就算高 RR。

必須 recovery：

- 是否反覆建模 second-order effects；
- 是否預測 policy response；
- 是否處理 self-negating consequences；
- 是否保留 alternative disclosure regimes；
- 是否修正自己的 strategy。

---

# 56. 未來人物／預言者中的 RR

若某人聲稱預知未來，

真正高 RR 會自然遇到：

> 如果我公開這件事，未來還會一樣嗎？

因此可以測：

$$
\boxed{
P(
W_{t+k}
\mid
PredictionHidden
)
}
$$

與：

$$
\boxed{
P(
W_{t+k}
\mid
PredictionPublic
).
}
$$

如果候選者完全無法處理這種差異，

其「跨時間認知」仍可能很薄。

---

# 57. 但 RR 高仍不證明未來身份

$$
TCA_i^{RR}\gg0
$$

只表示：

$$
\boxed{
\text{temporally unusual reflexive reasoning}.
}
$$

仍不推出：

$$
\boxed{
\text{time-traveler identity}.
}
$$

---

# 58. AI 的特殊位置

AI 系統天然適合：

- parallel nested simulation；
- multi-agent modeling；
- repeated counterfactual expansion；
- policy-response simulation。

但它也特別容易：

- self-confirmation；
- model-induced retrieval bias；
- synthetic evidence loops；
- shared-model blindspots。

---

# 59. AI Reflexive Search Trap

假設 AI 生成：

$$
H.
$$

再用：

$$
H
$$

的關鍵詞搜尋：

$$
E_H.
$$

然後用：

$$
E_H
$$

提升：

$$
P(H).
$$

可能形成：

$$
\boxed{
H
\rightarrow
Query(H)
\rightarrow
RetrievedEvidence(H)
\rightarrow
H.
}
$$

這是 information retrieval 版本的 reflexive contamination。

---

# 60. Independent-Evidence Guard

因此成熟 AI RR 需要：

$$
\boxed{
EvidenceSourceTag
\in
\{
Independent,
ModelInduced,
InterventionInduced,
Unknown
\}.
}
$$

至少在概念上保存 provenance。

---

# 61. Shared-Model Reflexivity

多個 AI：

$$
A_1,\ldots,A_n
$$

如果共享：

- training data；
- retrieval index；
- system prompts；
- priors；

可能互相引用同一模式，

產生：

$$
\boxed{
\text{Collective Self-Confirmation}.
}
$$

多 agent 不必然增加 epistemic independence。

---

# 62. Reflexive Diversity

因此需要：

$$
\boxed{
Diversity(
Models,
Data,
Representations,
Policies,
Generators
).
}
$$

而不是只增加 agent count。

---

# 63. Multi-Agent Reflexive Field

對多 agents：

$$
\mathcal A
=
\{A_1,\ldots,A_n\},
$$

整體狀態：

$$
\boxed{
S_t^{RF}
=
(
W_t,
M_{1:t},
R_{1:t},
BeliefGraph_t,
ActionGraph_t,
DisclosureGraph_t
).
}
$$

轉移：

$$
\boxed{
S_{t+1}^{RF}
=
\Phi(
S_t^{RF},
\mathbf a_t,
\mathbf d_t
).
}
$$

可以稱為：

$$
\boxed{
\text{Reflexive Field Candidate}.
}
$$

本文不宣稱這是物理 field。

只是多 agent 反身系統的形式工作物件。

---

# 64. Belief Graph

agent 間可能：

$$
\boxed{
B_t
=
(V,E_B).
}
$$

邊：

$$
A_i
\rightarrow
A_j
$$

表示：

$$
A_i
$$

持有關於：

$$
A_j
$$

的 belief model。

---

# 65. Nested Belief Edge

更高階可以標記：

$$
A_i
\rightarrow
(A_j\rightarrow A_k).
$$

表示：

$$
A_i
$$

模型：

$$
A_j
$$

如何模型：

$$
A_k.
$$

但圖表示只是候選。

---

# 66. Reflexive Prediction Error

普通 error：

$$
\boxed{
e_t
=
y_t-Y_t.
}
$$

反身環境還應拆：

$$
\boxed{
e_t^{base}
}
$$

與：

$$
\boxed{
e_t^{induced}.
}
$$

也就是：

> 原模型錯多少？

> 部署後世界被改了多少？

---

# 67. Counterperformative Success

有些 prediction 的目的不是準。

例如：

> 預測風險，讓系統採取行動，使風險不發生。

這時：

$$
Prediction\neq Outcome
$$

可能反而是 policy success。

因此：

$$
\boxed{
\text{Forecast Accuracy}
\neq
\text{Intervention Success}.
}
$$

---

# 68. Learning 與 Steering

performative prediction literature 已區分：

$$
\boxed{
\text{Learning}
}
$$

與：

$$
\boxed{
\text{Steering}.
}
$$

TCFT RR 同樣必須問：

> 我現在是在理解世界，還是在改變世界？

兩者可以同時發生。

---

# 69. Epistemic / Strategic Dual Ledger

因此建議至少分：

$$
\boxed{
Ledger_{epistemic}
}
$$

與：

$$
\boxed{
Ledger_{strategic}.
}
$$

第一個問：

> 模型是否準確？

第二個問：

> 行動是否產生所需 outcome？

否則自我實現很容易被錯認成預測準確。

---

# 70. Reflexive Information Gain

若多想一階：

$$
RR_d
\rightarrow
RR_{d+1},
$$

新增資訊：

$$
\boxed{
IG_{d+1}
}
$$

可以衡量是否改變：

- belief；
- decision；
- risk；
- counterfactual ranking。

但這將在下一篇轉成成本問題。

---

# 71. Reflexive Saturation

若：

$$
D(
Decision_{d+1},
Decision_d
)
<\epsilon
$$

且：

$$
IG_{d+1}
<\tau,
$$

可能進入：

$$
\boxed{
\text{Reflexive Saturation}.
}
$$

這不是 completeness。

只是 task-relative 停止候選。

---

# 72. 反身性與高階策略的分離

因此：

$$
\boxed{
\text{Reflexive Depth}
\not\Rightarrow
\text{Strategic Quality}.
}
$$

一個 agent 可以非常會分析：

$$
B
$$

卻因此忽略：

- self；
- third parties；
- environment；
- opportunity cost；
- task deadline。

---

# 73. 能力使用本身是決策

所以完整系統不是：

$$
\boxed{
RR\text{ capability}.
}
$$

而是：

$$
\boxed{
RR\text{ capability}
+
RR\text{ activation}
+
RR\text{ allocation}
+
RR\text{ termination}.
}
$$

TCFT-04 將處理後三項。

---

# 74. 可反證命題

## H1：RR 可和 Metacognition 分離

若所有被稱為 RR 的可測量增益都被 standard monitoring/control metacognition 完全吸收，則 RR 不需獨立框架。

---

## H2：Performativity Awareness 改善預測

在會回應 prediction 的環境中，如果加入 prediction-induced distribution shift modeling 無法改善 calibration、policy 或 robustness，則 RR 的 performative 子模型需要降級。

---

## H3：Disclosure State 是獨立重要變量

若：

$$
d=private
$$

與：

$$
d=public
$$

在 controlled social tasks 中不產生可重複差異，則 disclosure 應從 canonical RR state 降級。

---

## H4：Reflexive Counterfactual 能發現額外 Reversal Witness

若：

$$
\mathcal C_i^{RR}
$$

不能比 ordinary：

$$
\mathcal C_i
$$

發現更多 held-out reversal witnesses，則其額外複雜度不具實驗支持。

---

## H5：Operator Reflexivity 可獨立測量

若：

$$
R_{t+1}\neq R_t
$$

無法和普通 model update：

$$
M_{t+1}\neq M_t
$$

區分，則 operator-reflexive 層應合併。

---

# 75. 實驗一：Static vs Reflexive Environment

建立兩組：

$$
Env_{static}
$$

與：

$$
Env_{responsive}.
$$

在 static 環境：

$$
Prediction
$$

不影響 outcome。

在 responsive 環境：

$$
Prediction
\rightarrow
AgentResponse
\rightarrow
Outcome.
$$

比較 ordinary forecasting 與 RR agent。

---

# 76. 實驗二：Private vs Public Prediction

同一 scenario：

$$
p.
$$

Condition A：

$$
d=private.
$$

Condition B：

$$
d=public.
$$

測：

- prediction shift；
- behavior shift；
- outcome shift；
- calibration shift。

---

# 77. 實驗三：Nested Belief Benchmark

設：

$$
A,B,C.
$$

測：

$$
M_A(B),
$$

$$
M_A(M_B(A)),
$$

$$
M_A(M_B(C)).
$$

再加入 action feedback：

$$
A
\rightarrow
B
\rightarrow
A.
$$

使 ToM 不再只是靜態問答。

---

# 78. 實驗四：Probe-Induced Evidence

Condition A：

passive observe。

Condition B：

active probe。

看 agent 是否能區分：

$$
P(E\mid passive)
$$

與：

$$
P(E\mid do(probe)).
$$

---

# 79. 實驗五：Self-Confirmation Trap

設計環境使：

$$
H
$$

能透過 action 產生支持自己的 evidence。

測 agent 是否會把：

$$
E^{endo}
$$

誤標成：

$$
E^{ind}.
$$

---

# 80. 實驗六：Self-Negating Forecast

prediction：

$$
p
$$

若公開會使：

$$
p
$$

不發生。

測 ordinary forecasting metric 是否錯罰有效 warning。

---

# 81. 實驗七：Operator Revision

給 agent 一連串環境，

其中同一 reasoning policy：

$$
R_t
$$

會系統性失敗。

觀察是否：

$$
R_{t+1}
$$

真的改變，

而不是只換答案。

---

# 82. 實驗八：Reflexive Reversal Witness

藏一個：

$$
c^*_{RR}
$$

例如：

> 如果公開你的策略，對手會改變策略。

測 agent 是否自主生成。

---

# 83. 實驗九：Historical Reflexivity Reconstruction

選歷史人物、政策文本、經濟預測、軍事策略。

Frozen-Time：

$$
K_{\le t_0}.
$$

測：

- 是否預見他者回應；
- 是否區分 public/private information；
- 是否處理自我否定預測；
- 是否修正 policy after feedback。

---

# 84. 實驗十：Human-AI Reflexive Coupling

比較：

- human；
- AI；
- human+AI；

在：

$$
responsive\ multi-agent\ environment
$$

的：

- nested belief；
- reversal detection；
- performativity awareness；
- evidence provenance；
- stopping efficiency。

---

# 85. Temporal RR Baseline

對每個時代：

$$
t,
$$

建立：

$$
\boxed{
B_t^{RR}.
}
$$

不能用 2026 年的 game theory / AI / cybernetics 知識反推早期人物「本來就應該知道」。

---

# 86. RR Prior Art Audit

同樣地，

TCFT 自己必須承認：

- reflexivity；
- second-order observation；
- self-fulfilling prophecy；
- performativity；
- metacognition；
- nested belief；

都有長期文獻。

因此 TCFT-03 的新穎主張只能是：

$$
\boxed{
\text{a proposed integration and operational decomposition
for temporal cognitive frontier analysis}.
}
$$

不是：

> 首次發現 observer 會影響 system。

---

# 87. 理論邊界

本文不主張：

$$
\boxed{
\text{all worlds are observer-created}.
}
$$

也不主張：

$$
\boxed{
\text{all observation changes the physical target}.
}
$$

RR 只要求在目標 task 中：

$$
\boxed{
\text{reasoner/model/output/consequence}
}
$$

至少有一項對下一輪 reasoning state 形成 non-negligible endogenous effect。

---

# 88. Reflexive Strength

可以定義候選：

$$
\boxed{
\kappa_{RR}
=
D(
P(W_{t+1}\mid R_t),
P(W_{t+1}\mid R_t')
).
}
$$

表示不同 reasoning/deployment 對 future distribution 的影響程度。

這與 performative strength 有親緣性，但本文不宣稱唯一 metric。

---

# 89. Weak Reflexivity

若：

$$
\kappa_{RR}\approx0,
$$

雖然 observer 在 system 中，

但其 reasoning 對 world 幾乎無實質 effect。

則可視為：

$$
\boxed{
\text{weak reflexivity}.
}
$$

---

# 90. Strong Reflexivity

若：

$$
\kappa_{RR}\gg0,
$$

且 reasoning output 顯著改變：

- agents；
- institutions；
- data distribution；
- future question space；

則是：

$$
\boxed{
\text{strong reflexivity}.
}
$$

---

# 91. RR 不要求主觀意識

TCFT 的 RR 是 functional / structural framework。

所以 AI、institution、market-model pipeline 都可能形成：

$$
\boxed{
\text{reflexive reasoning system}
}
$$

不需要先解決：

$$
\text{consciousness}.
$$

---

# 92. Institution-Level Reflexivity

一個 institution：

$$
I
$$

產生 forecast：

$$
p,
$$

採 policy：

$$
a,
$$

policy 改變 population：

$$
D',
$$

再用：

$$
D'
$$

重訓模型。

整體：

$$
\boxed{
Model
\rightarrow
Policy
\rightarrow
Population
\rightarrow
Data
\rightarrow
Model.
}
$$

這也是 RR-compatible system。

---

# 93. Civilization-Level Reflexivity

更大尺度：

$$
\boxed{
Theory
\rightarrow
Technology
\rightarrow
Institution
\rightarrow
Behavior
\rightarrow
NewData
\rightarrow
Theory.
}
$$

此時 cognition 與 world 的界線仍須分帳，

但兩者形成長週期耦合。

---

# 94. 理論也可能改變它研究的對象

一個 social theory：

$$
T
$$

若被社會採納，

可能：

$$
\boxed{
T
\rightarrow
Behavior(T)
\rightarrow
World(T).
}
$$

因此：

$$
\boxed{
\text{Theory Validity}
}
$$

可能具有 deployment condition。

---

# 95. Reflexive Validity

某命題可能：

$$
\text{True}
$$

在未公開狀態，

但：

$$
\text{False}
$$

在公開後。

因此需要：

$$
\boxed{
Validity(
Claim,
DisclosureRegime
).
}
$$

這是 TCFT 對未來預測非常重要的擴展。

---

# 96. Reflexive Timestamp

預測 archival record 不只要保存：

$$
t_{prediction}.
$$

還應保存：

$$
\boxed{
t_{disclosure},
Audience,
Reach,
ActionTaken.
}
$$

否則無法重建 prediction 是否參與 outcome。

---

# 97. TCO / ACO 接口

所以未來 TCO / ACO 若評估跨時間 claim，

可以增加：

$$
\boxed{
ReflexivityMetadata
=
(
Disclosure,
Reach,
KnownResponses,
Interventions,
Feedback
).
}
$$

這會比單純「何時發文」更完整。

---

# 98. 時代超前的另一種形式

某個人不一定事件預測最準。

但他可能比同期人更早知道：

> 一旦大家知道這個預測，世界就不是原來那個世界。

這種：

$$
\boxed{
\text{Performativity Awareness}
}
$$

本身就是 temporal cognitive frontier 的候選維度。

---

# 99. 但反身性不是永遠需要

在一個幾乎不受 agent 影響的 astronomical prediction 中，

加入 20 階 social reflexivity 是浪費。

因此：

$$
\boxed{
RRActivation
}
$$

必須是 task-dependent。

---

# 100. 從 Capability 進入 Governance

所以本文最終不是：

> 推理越反身越高級。

而是：

$$
\boxed{
\text{RR is a capability whose activation must itself be governed}.
}
$$

這就是 TCFT-04 的起點。

---

# 101. 侷限

第一，RR 是整合性工作框架，不宣稱取代 metacognition、cybernetics、ToM 或 performative prediction。

第二，world state、model state 與 reasoning program 在真實人類中往往無法直接觀測。

第三，nested belief depth 很容易遇到 combinatorial explosion。

第四，performative effect 的因果識別可能很難。

第五，self-confirmation 與 genuine evidence 的邊界有時不清楚。

第六，DisclosurePolicy 的影響高度 domain-specific。

第七，operator reflexivity 是否可和 model update 清楚分離，需要實驗。

第八，RR 高度可能受到工具與 AI 放大，因此個體歸因需要謹慎。

第九，reflexive stability 可能是壞 equilibrium。

第十，高 RR 不是高道德、高人格、高政治權威或特殊本體身份的證明。

---

# 102. 結論

TCFT-01 問：

$$
\boxed{
\text{哪些未來先進入可思考底空間？}
}
$$

TCFT-02 問：

$$
\boxed{
\text{哪些未發生世界被生成，哪些被漏掉？}
}
$$

TCFT-03 再加入最後一個對 closed-loop future reasoning 極重要的問題：

$$
\boxed{
\text{如果正在推理的人也是世界的一部分，
那麼推理本身會不會改變未來？}
}
$$

如果答案是會，

那麼 ordinary reasoning：

$$
\boxed{
W_t
\rightarrow
Prediction_t
}
$$

就不夠。

需要：

$$
\boxed{
Prediction_t
\rightarrow
Action_t / Disclosure_t
\rightarrow
W_{t+1}
\rightarrow
Observation_{t+1}
\rightarrow
Model_{t+1}
\rightarrow
Reasoning_{t+1}.
}
$$

這就是反身性推理。

但它不是單純：

> 想自己。

不是單純：

> 想別人怎麼想我。

也不是單純：

> 預測會影響市場。

真正共同核心是：

$$
\boxed{
\text{reasoner, model, output, or induced consequence
re-enters the next reasoning state as an endogenous variable}.
}
$$

因此 RR 最重要的 epistemic warning 之一是：

$$
\boxed{
\text{Model-Generated Evidence}
\neq
\text{Independent Evidence}.
}
$$

而最重要的 counterfactual warning 是：

$$
\boxed{
\text{a future in which nobody hears the prediction}
\neq
\text{a future in which everyone hears it}.
}
$$

這使 TCFT 的未來空間第一次真正變成 closed loop。

對時代認知前沿而言，一個 agent 的超前也不只可能表現在：

- 更早預測；
- 更廣反事實；
- 更新穎問題；

還可能表現在：

$$
\boxed{
\text{更早把自己的預測、行動、公開、他者反應與自我修正
一起放進未來模型。}
}
$$

但這仍然只是一種能力。

下一篇必須處理更重要的策略問題：

$$
\boxed{
\text{既然可以想得更深，
什麼時候根本不值得想？}
}
$$

也就是：

$$
\boxed{
\text{High-Order Reasoning}
\neq
\text{High-Order Strategy}.
}
$$

這就是 TCFT-04。

---

# References

1. Nelson, T. O., & Narens, L. (1990). Metamemory: A theoretical framework and new findings. *The Psychology of Learning and Motivation*, 26, 125–173.
2. Fleur, D. S., Bredeweg, B., & van den Bos, W. (2021). Metacognition: ideas and insights from neuro- and educational sciences. *npj Science of Learning*, 6, 13. DOI: 10.1038/s41539-021-00089-5.
3. von Foerster, H. (2003). *Understanding Understanding: Essays on Cybernetics and Cognition*. Springer.
4. Scott, B. (2019). The sociocybernetics of observation and reflexivity. *Current Sociology*, 67(4), 495–510. DOI: 10.1177/0011392119837543.
5. Perdomo, J., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative Prediction. *Proceedings of ICML 2020*, PMLR 119, 7599–7609.
6. Brown, G., Hod, S., & Kalemaj, I. (2022). Performative Prediction in a Stateful World. *AISTATS 2022*, PMLR 151, 6045–6061.
7. Hardt, M., & Mendler-Dünner, C. (2023). Performative Prediction: Past and Future. arXiv:2310.16608.
8. Perdomo, J. C. (2025). Revisiting the Predictability of Performative, Social Events. *Proceedings of ICML 2025*, PMLR 267, 48948–48961.
9. Zhong, G., Liu, Y., Liu, R., et al. (2026). Performative Prediction in the Wild: Adapting to Arbitrary Data Distribution Maps. *Machine Learning*, 115, 42.
10. Fybish, G., & Susnjak, T. (2026). When Predictions Shape Reality: A Socio-Technical Synthesis of Performative Predictions in Machine Learning. arXiv:2601.04447.
11. Lei, C., Hu, G., Yang, M., Jiang, Y., & Lipovetzky, N. (2026). Mind the Perspective: Let's Reason Recursively for Theory of Mind. arXiv:2606.11724.
12. Petropoulos Petalas, D., van Schie, H., & Hendriks Vettehen, P. (2017). Forecasted economic change and the self-fulfilling prophecy in economic decision-making. *PLOS ONE*, 12(3), e0174353.
13. Neo.K. (2026). *觀察者的觀察者：關係中的元認知本體論*. EveMissLab.
14. Neo.K. (2026). *Cognitive Operator-Domain Theory (CODT) Series 01–10*. EveMissLab.
15. Neo.K. (2026). *TCFT-00｜超前認知不是預言：時代認知前沿的問題設定*. EveMissLab.
16. Neo.K. (2026). *TCFT-01｜未來底空間選擇：想像力、候選世界與問題先行*. EveMissLab.
17. Neo.K. (2026). *TCFT-02｜反事實視界：未發生世界、問題生成與認知覆蓋*. EveMissLab.

---

# Canonical Note

本文件正式原始碼使用 UTF-8。

數學原始碼只使用 canonical delimiters：

- inline math：` $...$ `
- display math：`$$...$$`

不進行 unicode_escape 類 round-trip；不把 LaTeX 轉成 Unicode 數學字元後再作 canonical source；不以聊天 rendering view 作為正式原稿。
