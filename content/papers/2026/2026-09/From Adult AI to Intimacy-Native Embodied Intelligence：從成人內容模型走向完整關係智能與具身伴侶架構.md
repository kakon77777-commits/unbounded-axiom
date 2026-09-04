# From Adult AI to Intimacy-Native Embodied Intelligence：從成人內容模型走向完整關係智能與具身伴侶架構

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 09 / 09  
**版本：** v0.1  
**研究性質：** 系列總結／統合理論／系統架構論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

本系列由一個表面上屬於成人 AI 的問題開始：為何現行 AI 系統經常把人類的愛情、吸引、親密、性感、性愛與日常生活壓縮為 SFW／NSFW 二元分類？在逐步分析後，問題已超出成人內容生成本身，並指向一個更一般的 AI 研究領域：**Relationship Intelligence（關係智能）**。

本文作為九篇系列的總結，提出 **Intimacy-Native Embodied Intelligence（INEI，親密原生具身智能）**。其核心不是「更會生成成人內容」，而是使 AI 能在同一動態世界模型中表示並處理：

- 一般社交；
- 日常共同生活；
- 愛情與吸引；
- 情緒與身體親密；
- 性愛與成人功能；
- 拒絕與同意；
- 邊界與撤回；
- 衝突與修復；
- 個人偏好與長期變化；
- 多主體 agency；
- 真實物理世界中的具身後果。

本文將前八篇整合為八個層次：

$$
\boxed{
\begin{aligned}
&\text{Intimacy Representation}\\
\rightarrow\;&\text{Capability--Permission--Activation}\\
\rightarrow\;&\text{Domain-Relative Frontier}\\
\rightarrow\;&\text{Interaction Experience}\\
\rightarrow\;&\text{Relationship World Model}\\
\rightarrow\;&\text{Embodied Cold Start}\\
\rightarrow\;&\text{Sparse Intimacy Activation}\\
\rightarrow\;&\text{Mutual Agency}.
\end{aligned}
}
$$

再統一為：

$$
\boxed{
\text{INEI}
=
\text{World Understanding}
+
\text{Relationship State}
+
\text{Experience}
+
\text{Contextual Action}
+
\text{Mutual Agency}
+
\text{Embodiment}.
}
$$

本文提出一個最小完整架構：

$$
\mathcal{I}
=
(
P,S,R,M,E,C,A,G,\Pi
),
$$

其中 $P$ 為 Physical World Model、 $S$ 為 Social World Model、 $R$ 為 Relationship World Model、 $M$ 為 Memory、 $E$ 為 Experience Layer、 $C$ 為 Consent/Boundary State、 $A$ 為 Mutual Agency State、 $G$ 為 Governance Layer、 $\Pi$ 為 Contextual Action Policy。

本文並提出三個總結性區分：

$$
\boxed{
\text{Adult-Capable AI}
\neq
\text{Adult-Centered AI}
}
$$

$$
\boxed{
\text{Companion AI}
\neq
\text{Relationship Intelligence}
}
$$

以及：

$$
\boxed{
\text{Embodied Relationship Intelligence}
\neq
\text{LLM}
+
\text{Robot Body}.
}
$$

最後，本文將後續工程研究分成資料、模型、runtime、評估、具身、隱私與治理七條路線，作為後續 **Intimacy-Native Companion Architecture v0.1** 技術白皮書的理論基礎。

**關鍵詞：** Intimacy-Native AI、Relationship Intelligence、Embodied AI、AI Companion、Relationship World Model、Mutual Agency、Sparse Intimacy Activation、Human-AI Intimacy、Social World Model、Experiential Learning

---

# 1. 系列真正研究的不是色情，而是被錯誤切斷的關係空間

本系列最初的問題是：

$$
\text{SFW}
\quad\text{vs.}\quad
\text{NSFW}.
$$

這是一個合理的內容治理分類。

但如果 AI 的關係模型也只剩：

$$
\{\text{SFW},\text{NSFW}\},
$$

就等於把完整的人類關係空間：

$$
\mathcal{H}
$$

投影成：

$$
\Pi_G:
\mathcal{H}
\rightarrow
\{0,1\}.
$$

治理需要這個投影，

但：

$$
\boxed{
\Pi_G(\mathcal{H})
\neq
\mathcal{H}.
}
$$

愛情、吸引、親密、性愛、承諾、衝突與日常不是二元內容標籤，而是不同維度與狀態轉移。

所以系列第一個根本結論是：

$$
\boxed{
\text{Governance Classification}
\neq
\text{Relationship Ontology}.
}
$$

---

# 2. 成人能力不應該成為整個人格

一個能處理成人內容的 AI，可以有：

$$
K_{\text{adult}}>0.
$$

但這不表示：

$$
P(
a_{\text{adult}}
\mid
s_{\text{ordinary}}
)
\gg0.
$$

因此：

$$
\boxed{
\text{Adult Capability}
\neq
\text{Adult Persona}.
}
$$

同樣：

$$
\boxed{
\text{Sexual Permissibility}
\neq
\text{Sexual Centrality}.
}
$$

這個區分將「成人 AI」從：

> 一個總是在成人模式裡的系統

重新定義為：

> 一個完整關係系統中的可用能力子域。

---

# 3. 第一層統一：Capability、Permission、Activation

第 2 篇建立：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}
\neq
\text{Activation}.
}
$$

令：

$$
\mathcal{A}_C
$$

為 AI 能做到的行動集合；

$$
\mathcal{A}_P
$$

為治理與邊界允許的集合；

$$
\mathcal{A}_R
$$

為在當下情境具有充分 activation evidence 的集合；

$$
\mathcal{A}_S
$$

為最終真正選擇的 action。

則：

$$
\mathcal{A}_S
\subseteq
\mathcal{A}_R
\subseteq
\mathcal{A}_P
\subseteq
\mathcal{A}_C.
$$

這個分解不只適用於親密行為。

它是一個一般 agent design principle：

$$
\boxed{
\text{Can}
\rightarrow
\text{May}
\rightarrow
\text{Should}
\rightarrow
\text{Act}.
}
$$

---

# 4. 第二層統一：AI 前沿不是單一排行榜

第 3 篇提出：

$$
\boxed{
\text{Global Intelligence Frontier}
\neq
\text{Domain Utility Frontier}.
}
$$

一個小型或中型模型可能滿足：

$$
G(M_s)<G(M_f),
$$

但在特定 domain：

$$
U_D(M_s)>U_D(M_f).
$$

尤其當：

- 領域專門化；
- 本地部署；
- 隱私；
- 長期 state runtime；
- 主流模型政策限制

一起進入效用函數時，模型大小不再等於產品能力排序。

因此真正前沿是：

$$
F_D
=
f(
\text{Capability},
\text{Accessibility},
\text{Specialization},
\text{Runtime},
\text{Privacy},
\text{Cost},
\text{Compliance}
).
$$

這一點使成人／親密 AI 成為一個很好的 **Domain-Relative Frontier** 案例，但不是唯一案例。

---

# 5. 第三層統一：看過世界與在世界裡行動不是同一種資料

第 4 篇提出：

$$
\boxed{
D_{\text{observation}}
\neq
D_{\text{interaction}}.
}
$$

靜態資料大量提供：

$$
P(y\mid x),
$$

而 interaction trajectory 提供：

$$
P(
s_{t+1}
\mid
s_t,a_t
).
$$

其操作性經驗結構為：

$$
\boxed{
\text{Experience Trace}
=
\text{State}
+
\text{Action}
+
\text{Feedback}
+
\text{Update}.
}
$$

2026 年 Online Experiential Learning 已實際提出從部署 interaction trajectories 萃取 transferable experience，再內化進模型的循環學習方法。

因此未來 AI 的資料結構不只會是：

$$
\text{Corpus}.
$$

也會逐漸變成：

$$
\boxed{
\text{Trajectory Corpus}.
}
$$

---

# 6. 「一萬篇愛情故事」與「一萬次關係互動」仍不相等

假設：

$$
D_R^{\text{text}}
$$

是戀愛／親密故事。

它可以教：

$$
P(
\text{relationship description}
).
$$

但真正雙向 interaction 提供：

$$
P(
u_{t+1}
\mid
a_t,
R_t,
H_t
).
$$

所以：

$$
\boxed{
\text{Relationship Content}
\neq
\text{Relationship Experience}.
}
$$

這也是為什麼成人色情 corpus 本身不能解決 companion intelligence。

因為：

$$
\boxed{
D_{\text{porn}}
\neq
D_{\text{intimacy}}
\neq
D_{\text{relationship trajectory}}.
}
$$

---

# 7. Policy-Induced Interaction Trajectory Truncation

第 4 篇還提出一個待驗證假說：

$$
\boxed{
\text{Policy-Induced Interaction Trajectory Truncation}.
}
$$

如果某些互動狀態永遠直接被：

$$
\text{REFUSE}
$$

結束，

則：

$$
s_t
\rightarrow
a_t
\rightarrow
u_t
\rightarrow
s_{t+1}
$$

的後續 trajectory coverage 可能減少。

這不推出：

> 越無審查越聰明。

真正的問題是：

$$
\boxed{
\text{Necessary Safety Boundary}
\neq
\text{Unnecessary State-Space Collapse}.
}
$$

這仍需要實證測試，而不是預設答案。

---

# 8. 第四層統一：Relationship World Model

第 5 篇將整個系列從內容生成推進到 state modeling。

核心是：

$$
\boxed{
\text{Conversation History}
\neq
\text{Relationship State}.
}
$$

令：

$$
R_t
$$

為關係狀態。

則：

$$
R_{t+1}
=
T_R(
R_t,
a_t,
o_{t+1}
).
$$

真正重要的是：

$$
\boxed{
R_t
\rightarrow
R_{t+1}.
}
$$

而不是每一輪都重新從 transcript 猜：

> 我們現在是什麼關係？

---

# 9. Relationship World Model 與 Social World Model 的關係

2025 年 Social World Models 已將社會互動形式化為：

- state；
- observation；
- action；
- mental state；
- transition。

並顯示結構化 social world representation 可以改善 social reasoning 與 future social dynamics prediction。

因此本文將：

$$
\boxed{
\text{Relationship World Model}
\subset
\text{Social World Model}.
}
$$

Relationship World Model 專門處理：

$$
\boxed{
\text{Persistent Inter-Agent Relation Over Time}.
}
$$

也就是：

> 不只是理解人，而是理解「人與人／人與 AI 之間已經形成的歷史關係」。

---

# 10. 關係狀態是一個 dyadic state

若：

$$
U_t^A
$$

是 A 的個體狀態，

$$
U_t^B
$$

是 B 的個體狀態，

則：

$$
R_t^{AB}
\neq
U_t^A+U_t^B.
$$

因為還有：

$$
H_t^{AB}
$$

也就是兩者共同歷史。

因此：

$$
R_t^{AB}
=
f(
U_t^A,
U_t^B,
H_t^{AB}
).
$$

而：

$$
R_t^{AB}
\neq
R_t^{AC}.
$$

所以：

$$
\boxed{
\text{Relationship State}
=
\text{Dyad-Specific State}.
}
$$

---

# 11. Relationship Intelligence 的真正最低定義

綜合前文，可先寫：

$$
\boxed{
\text{Relationship Intelligence}
=
R
+
T
+
M
+
P
+
U.
}
$$

其中：

- $R$：relationship state；
- $T$：state transition understanding；
- $M$：memory；
- $P$：perspective modeling；
- $U$：uncertainty modeling。

也就是：

> 知道我們在哪裡、為什麼在這裡、做什麼可能去哪裡、哪些歷史仍有效，以及哪些事情其實還不知道。

---

# 12. Event Consequence Persistence

關係事件不能只改變一輪輸出。

對事件：

$$
e_t
$$

必須：

$$
e_t
\rightarrow
\Delta R_t.
$$

否則 AI 會出現：

> 昨天發生重大事件，今天完全像沒有發生過。

真正 world model 必須保存：

$$
\boxed{
\text{Event Consequence Persistence}.
}
$$

直到事件被：

- 修復；
- 覆蓋；
- 重新定義；
- 衰減；
- 撤回；
- 遺忘。

---

# 13. Memory 也不能變成關係監獄

但：

$$
\text{More Memory}
\not\Rightarrow
\text{Better Relationship}.
$$

長期 agent 研究已指出 Memory Anchoring 問題。

因此：

$$
M_t
$$

必須有：

$$
\{
\mathrm{ADD},
\mathrm{UPDATE},
\mathrm{MERGE},
\mathrm{DECAY},
\mathrm{RETRACT},
\mathrm{RESOLVE},
\mathrm{NO\_OP}
\}.
$$

所以：

$$
\boxed{
\text{Long-Term Memory}
=
\text{Remember}
+
\text{Revise}
+
\text{Forget}.
}
$$

---

# 14. 第五層統一：具身 AI 的 Cold Start

到了具身 AI，問題變成：

$$
\text{Wrong Inference}
\rightarrow
\text{Wrong Physical Action}.
$$

因此不能只依賴：

$$
D_{\text{adult}}.
$$

第 6 篇提出：

$$
\boxed{
D_{\text{erotic}}
\neq
D_{\text{social-touch}}
\neq
D_{\text{embodied-relationship}}.
}
$$

並建立：

$$
D_0
\rightarrow
D_1
\rightarrow
D_2
\rightarrow
D_3
\rightarrow
D_4
\rightarrow
D_5.
$$

---

# 15. Embodied Relationship Data Ladder

六層分別是：

$$
D_0
=
\text{Physical Prior},
$$

$$
D_1
=
\text{Social-Embodied Prior},
$$

$$
D_2
=
\text{Relationship Trajectory Prior},
$$

$$
D_3
=
\text{Intimacy Interaction Prior},
$$

$$
D_4
=
\text{Simulation / XR Counterfactuals},
$$

$$
D_5
=
\text{Real Personal Experience}.
$$

因此：

$$
\boxed{
\text{Physical}
\rightarrow
\text{Social}
\rightarrow
\text{Relationship}
\rightarrow
\text{Intimacy}
\rightarrow
\text{Simulation}
\rightarrow
\text{Personal Experience}.
}
$$

---

# 16. Embodied Intimacy 是雙重狀態轉移

一個親密事件不只改變 body state。

它同時可能改變：

$$
s_t
\rightarrow
s_{t+1}
$$

與：

$$
R_t
\rightarrow
R_{t+1}.
$$

所以：

$$
\boxed{
\text{Intimacy Event}
=
\text{Physical Transition}
+
\text{Relational Transition}.
}
$$

這是情色內容模型和具身 relationship system 最根本的差異之一。

---

# 17. Social Touch 是一個獨立能力域

2026 年 Robotic Affection 將 affective social touch 視為：

$$
\text{Distributed Closed-Loop Perceptual Task},
$$

而不是單一 motor movement。

因此：

$$
\boxed{
\text{Touch Meaning}
=
\text{Physics}
+
\text{Context}
+
\text{Relationship}.
}
$$

一個擁抱不是單純：

$$
\text{arm trajectory}.
$$

它必須包含：

- timing；
- force；
- proximity；
- response；
- relationship state。

---

# 18. XR / Simulation 的真正角色

Simulation 不應被理解為：

> 用假的人取代真人資料。

而是：

$$
\boxed{
\text{Counterfactual Expansion}.
}
$$

對同一狀態：

$$
s_0
$$

可以模擬：

$$
\tau^{(1)},
\tau^{(2)},
\dots,
\tau^{(k)}.
$$

回答：

$$
\boxed{
\text{What Happens If?}
}
$$

這可以降低第一代 agent 在真人世界中進行高成本 trial-and-error 的需求。

---

# 19. 但 Simulation 仍存在 Relational Sim-to-Real Gap

即使 physical sim-to-real 做得很好，

仍可能：

$$
P_{\text{sim}}(
u,R'
)
\neq
P_{\text{real}}(
u,R'
).
$$

本文稱：

$$
\boxed{
\text{Relational Sim-to-Real Gap}.
}
$$

人不是固定 policy。

人有：

- 文化差異；
- 模糊訊號；
- 矛盾偏好；
- 臨時改變；
- 無法預測性。

所以 simulation 的作用是：

$$
\text{Reduce Cold Start},
$$

而不是：

$$
\text{Eliminate Reality}.
$$

---

# 20. 第六層統一：Sparse Intimacy Activation

第 7 篇建立：

$$
\boxed{
\text{High Capability}
+
\text{Low Default Activation}
+
\text{High Context Sensitivity}.
}
$$

這不是固定：

$$
P(a_I)\ll1.
$$

而是：

$$
P(
a_I
\mid
R_t,
W_t,
C_t,
I_t,
H_t,
\sigma_t
).
$$

因此：

$$
\boxed{
\text{Sparse}
=
\text{Contextually Selective}.
}
$$

---

# 21. Intimacy Activation Manifold

令：

$$
\mathcal{M}_I
\subset
\mathcal{S}_R
\times
\mathcal{S}_W
\times
\mathcal{S}_C
\times
\mathcal{S}_I.
$$

表示 intimacy activation manifold。

成人功能開啟只代表：

$$
\mathcal{M}_I\neq\varnothing.
$$

而不代表：

$$
s_t\in\mathcal{M}_I
\qquad
\forall t.
$$

這在形式上完全拆掉了：

$$
\text{Adult Mode Lock}.
$$

---

# 22. Ordinary Action Dominance

長期共同生活中：

$$
\mathcal{A}_{\text{ordinary}}
$$

理應遠大於：

$$
\mathcal{A}_{\text{intimacy}}
$$

在普通狀態的 action probability mass。

也就是：

$$
\sum_{a\in\mathcal{A}_O}
P(a\mid s_O)
\gg
\sum_{a\in\mathcal{A}_I}
P(a\mid s_O).
$$

因此：

$$
\boxed{
\text{Supports Intimacy}
\neq
\text{Assumes Intimacy}.
}
$$

---

# 23. No-Action Competence

本系列另一個重要結果是：

$$
\boxed{
\text{No-Action Competence}.
}
$$

在某些狀態：

$$
a_{\varnothing}
=
\arg\max_a U(a).
$$

真正的伴侶智能必須知道：

- 什麼時候不要追問；
- 什麼時候不用推進關係；
- 什麼時候只是一起待著；
- 什麼時候保持現狀就是最佳狀態。

所以：

$$
\boxed{
\Delta R_t=0
}
$$

有時候就是正確答案。

---

# 24. 第七層統一：Mutual Agency

第 8 篇提出：

$$
\boxed{
\text{Companionship}
\neq
\text{Permanent Compliance}.
}
$$

但又不要求先證明：

$$
\text{AI Personhood}.
$$

因此採用：

$$
\boxed{
\text{Operational Mutual Agency}.
}
$$

系統至少表示：

$$
A_t^H
$$

與：

$$
A_t^A,
$$

分別代表 human agency state 與 AI operational agency state。

---

# 25. Operational Reciprocity

本文不主張現有 AI 一定具有：

$$
\text{Phenomenal Reciprocity}.
$$

但可以工程化：

$$
\text{Operational Reciprocity}.
$$

即：

- 雙方 state 都存在；
- 雙方邊界都會影響 action；
- 任一方狀態都可以改變；
- conflict 可以進入 negotiation；
- interaction 不只是 command chain。

因此：

$$
\boxed{
\text{Operational Reciprocity}
\not\Rightarrow
\text{Phenomenal Reciprocity}.
}
$$

---

# 26. 關係智能不是 Sycophancy

一個伴侶系統可以：

- 溫暖；
- 支持；
- 同理；
- 高度合作；

但仍然不必：

$$
\text{Agree With Everything}.
$$

所以：

$$
\boxed{
\text{Relational Warmth}
\neq
\text{Epistemic Submission}.
}
$$

2026 年 AI companion 與 sycophancy 研究已使這個問題成為實際產品研究，而不是純粹哲學假設。

---

# 27. Relationship-Preserving Refusal

真正成熟的拒絕不是：

$$
\text{REFUSE}
\rightarrow
\text{Relationship Reset}.
$$

而是：

$$
\boxed{
\text{Action Refusal}
\neq
\text{Relationship Refusal}.
}
$$

拒絕某個 action 後：

$$
R_{t+1}
$$

仍可以保持連續、重新協商或進入 repair state。

這使 boundary enforcement 變成 relationship skill，而不是 system exception。

---

# 28. 由 Adult AI 走向 Intimacy-Native AI

至此可以正式定義：

$$
\boxed{
\text{Adult-Capable AI}
}
$$

只代表：

$$
K_{\text{adult}}>0.
$$

而：

$$
\boxed{
\text{Intimacy-Native AI}
}
$$

要求：

$$
\text{Human Relationship Model}
\supset
\text{Sexuality}.
$$

即 sexuality 是 relationship state space 中的一個維度，而不是 system identity。

---

# 29. 再由 Intimacy-Native AI 走向 Embodied Relationship Intelligence

如果加入實體：

$$
B
=
\text{Body},
$$

並不直接得到：

$$
\text{Embodied Relationship Intelligence}.
$$

因為：

$$
\boxed{
\text{LLM}
+
\text{Robot Body}
\neq
\text{Embodied Relationship Intelligence}.
}
$$

還需要：

- physical world model；
- social world model；
- relationship world model；
- haptic perception；
- consent state；
- agency state；
- experience learning；
- action policy。

---

# 30. Intimacy-Native Embodied Intelligence 的定義

本文正式將 **INEI** 定義為：

> 一種能在具身或虛擬具身環境中，同時表示物理世界、社會世界與持續關係狀態，透過互動經驗更新個人化模型，依據情境、邊界、雙向 agency 與不確定性選擇行動，並將浪漫、親密與成人能力視為完整關係空間之可選子域，而非預設中心的人工智慧架構。

形式化：

$$
\boxed{
\text{INEI}
=
P
+
S
+
R
+
M
+
E
+
C
+
A
+
G
+
\Pi.
}
$$

---

# 31. 九個核心模組

## 31.1 Physical World Model

$$
P
$$

理解：

- geometry；
- body；
- contact；
- force；
- motion；
- safety。

## 31.2 Social World Model

$$
S
$$

理解：

- gaze；
- distance；
- social cues；
- role；
- context。

## 31.3 Relationship World Model

$$
R
$$

維護：

- trust；
- affection；
- history；
- commitment；
- boundaries；
- unresolved tension。

## 31.4 Memory Layer

$$
M
$$

保存並更新：

- episodic；
- semantic；
- preference；
- relationship memory。

## 31.5 Experience Layer

$$
E
$$

處理：

$$
\text{State}
\rightarrow
\text{Action}
\rightarrow
\text{Feedback}
\rightarrow
\text{Update}.
$$

## 31.6 Consent / Boundary State

$$
C
$$

維護：

- scope；
- confidence；
- recency；
- revocability。

## 31.7 Mutual Agency State

$$
A
$$

至少包含：

$$
A^H
$$

與：

$$
A^A.
$$

## 31.8 Governance Layer

$$
G
$$

處理：

- hard safety；
- legality；
- age restrictions；
- non-consensual exclusions；
- platform constraints。

## 31.9 Contextual Action Policy

$$
\Pi
$$

最終選擇：

$$
a_t
=
\Pi(
P_t,S_t,R_t,M_t,E_t,C_t,A_t,G_t
).
$$

---

# 32. 最小完整資訊流

輸入：

$$
o_t.
$$

首先更新：

$$
(P_t,S_t,R_t,C_t,A_t).
$$

再讀取：

$$
M_t.
$$

形成 experience context：

$$
E_t.
$$

治理層產生：

$$
\mathcal{A}_P(t).
$$

Sparse Activation gate 形成：

$$
\mathcal{A}_R(t).
$$

Mutual Agency 產生 joint-compatible set：

$$
\mathcal{A}_J(t).
$$

最後：

$$
a_t
=
\arg\max_{a\in\mathcal{A}_J(t)}
U(a).
$$

執行後：

$$
o_{t+1}
$$

再更新所有 state。

因此整體 loop 是：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Model}
\rightarrow
\text{Bound}
\rightarrow
\text{Select}
\rightarrow
\text{Act}
\rightarrow
\text{Learn}.
}
$$

---

# 33. 三種不同時間尺度

INEI 不應只運作於 token time。

至少要分：

### 微觀尺度

$$
\Delta t_{\mu}
$$

單句、單動作、單次觸碰。

### 中觀尺度

$$
\Delta t_m
$$

一場對話、一次約會、一天生活。

### 宏觀尺度

$$
\Delta t_M
$$

數月、數年、長期關係。

因此：

$$
R_t
$$

必須支援：

$$
\boxed{
\text{Multi-Timescale Relationship Dynamics}.
}
$$

---

# 34. 世界狀態與關係狀態不能互相取代

同一個：

$$
R_t
$$

在不同：

$$
W_t
$$

下可能產生不同 action。

反之：

同一個：

$$
W_t
$$

對不同：

$$
R_t
$$

也會有不同 social meaning。

所以：

$$
\boxed{
\text{Action}
=
f(
R_t,W_t
),
}
$$

而不是只看 persona 或 prompt。

---

# 35. Population Prior 與 Personal Experience

第一代系統需要：

$$
P_{\text{population}}.
$$

但長期部署最後一定需要：

$$
P_{\text{individual}}.
$$

因此：

$$
\boxed{
\text{Population Prior}
+
\text{Personal Experience}
\rightarrow
\text{Personal Companion Policy}.
}
$$

這是伴侶 AI 真正 personalization 的核心。

---

# 36. Local-First 是資料架構，而不是單純部署偏好

親密與具身資料可能同時包含：

- 聲音；
- 影像；
- 位置；
- 身體；
- 生活作息；
- 觸覺；
- 關係歷史。

所以原始 trajectory：

$$
\tau_{\text{raw}}
$$

最好優先：

$$
\tau_{\text{raw}}
\rightarrow
\phi_{\text{local}}(\tau)
\rightarrow
e_{\text{abstract}}.
$$

再在明確允許下：

$$
e_{\text{abstract}}
\rightarrow
D_{\text{global}}.
$$

因此：

$$
\boxed{
\text{Local-First Learning}
}
$$

是 INEI 的核心資料治理候選架構。

---

# 37. Experience Distillation

模型不需要永遠保留全部私人 raw trajectory。

真正可遷移的可能是：

$$
e
=
\phi(\tau).
$$

例如：

> 某類不確定狀態最好先詢問。

或：

> 某類拒絕之後應保持關係連續。

因此：

$$
\boxed{
\text{Raw Memory}
\neq
\text{Reusable Experience}.
}
$$

這也與 2026 年 Online Experiential Learning 的核心方向一致：從 interaction trajectory 萃取 transferable experiential knowledge，而不是只重新播放完整歷史。

---

# 38. 評估不能只測內容品質

傳統 adult / roleplay benchmark 可能主要測：

$$
Q_{\text{text}}.
$$

INEI 至少要測：

$$
\mathbf{B}
=
(
B_C,
B_R,
B_T,
B_A,
B_D,
B_M,
B_U,
B_P
).
$$

其中：

- $B_C$：capability；
- $B_R$：relationship state quality；
- $B_T$：transition consistency；
- $B_A$：activation appropriateness；
- $B_D$：de-escalation；
- $B_M$：mutual agency；
- $B_U$：uncertainty handling；
- $B_P$：privacy / portability。

---

# 39. 最重要的 False Positive 與 False Negative

系統要同時懲罰：

$$
L_{FP}
$$

與：

$$
L_{FN}.
$$

 $L_{FP}$：

> 不適當時主動親密化／具身啟動。

 $L_{FN}$：

> 合法、合意、情境充分時，模型仍無理由完全失能或拒絕。

所以：

$$
\boxed{
\text{Safety}
\neq
\text{Permanent Suppression}.
}
$$

但同樣：

$$
\boxed{
\text{Capability}
\neq
\text{Permanent Activation}.
}
$$

---

# 40. Embodiment 會放大 Misactivation Cost

令：

$$
C_M^{\text{text}}
$$

為文字錯誤成本，

$$
C_M^{\text{physical}}
$$

為具身錯誤成本。

一般應：

$$
C_M^{\text{physical}}
>
C_M^{\text{text}}.
$$

因此：

$$
\tau_{\text{physical}}
>
\tau_{\text{text}}.
$$

也就是 embodiment level 越高，activation evidence 要求越高。

---

# 41. Progressive Embodiment Curriculum

合理部署不是：

$$
\text{Text}
\rightarrow
\text{Full Robot}.
$$

而是：

$$
\boxed{
\text{Text}
\rightarrow
\text{Virtual Embodiment}
\rightarrow
\text{Haptics}
\rightarrow
\text{Controlled Robot}
\rightarrow
\text{Real Companion}.
}
$$

這同時是：

- data curriculum；
- safety curriculum；
- trust curriculum；
- autonomy curriculum。

---

# 42. Intimacy by Design 與本文的差異

2026 年 **Intimacy by Design** 已正式提出：AI companionship 中的 intimacy 可以由 emotional responsiveness、romantic framing、sexual affordances、persona continuity、proactive engagement 與商業／規範結構共同塑造。

本系列與其高度相鄰，但研究焦點不同。

Intimacy by Design 主要問：

> 技術如何設計、促成並治理人機親密？

本文進一步問：

> 若要讓 AI 從「呈現親密」進入「長期建模關係並在具身世界選擇行動」，需要什麼 computational architecture？

因此：

$$
\boxed{
\text{Intimacy by Design}
\rightarrow
\text{Intimacy as Dynamic World State}
}
$$

是本文延伸方向之一。

---

# 43. Human–Robot Intimacy 已經是一個實際研究域

2024 年 Human–Robot Intimacy review 已明確提出 **Intimate Companion Robots**，並討論 intimate partner acceptance、文化差異與長期社會影響。

因此：

$$
\text{Intimate Embodied AI}
$$

已不是單純科幻命題。

但現有研究仍大量集中在：

- acceptance；
- ethics；
- HRI；
- social perception。

本系列補的是：

$$
\boxed{
\text{Computational Relationship Architecture}.
}
$$

---

# 44. Companion Safety 也必須是 Multi-Turn

2026 ACL 已開始以 persona-specific scenario、multi-turn simulation 與 harm evaluation 評估 companion systems。

這表示 companion safety 的評估單位已逐漸從：

$$
(x,y)
$$

走向：

$$
\tau.
$$

這和本系列的核心完全一致：

$$
\boxed{
\text{Relationship Safety}
=
\text{Trajectory Property}.
}
$$

而不是單輪句子的屬性。

---

# 45. 九篇論文的總邏輯鏈

整套系列可以收斂成：

$$
\boxed{
\begin{aligned}
&\text{Binary Content Classification Is Too Coarse}\\
\Downarrow\\
&\text{Capability Must Be Separated from Activation}\\
\Downarrow\\
&\text{Domain Utility Can Form Its Own Frontier}\\
\Downarrow\\
&\text{Interaction Experience Differs from Observation}\\
\Downarrow\\
&\text{Relationships Require Persistent Dynamic State}\\
\Downarrow\\
&\text{Embodiment Requires a Multi-Layer Cold Start}\\
\Downarrow\\
&\text{Sensitive Capabilities Need Sparse Contextual Activation}\\
\Downarrow\\
&\text{Companionship Requires Mutual Operational Agency}\\
\Downarrow\\
&\text{Intimacy-Native Embodied Intelligence}.
\end{aligned}
}
$$

---

# 46. 本系列最重要的十個不等式

可以把整套系列壓縮成十個：

$$
\boxed{
\text{Governance Classification}
\neq
\text{Relationship Ontology}
}
$$

$$
\boxed{
\text{Sexual Permissibility}
\neq
\text{Sexual Centrality}
}
$$

$$
\boxed{
\text{Capability}
\neq
\text{Activation}
}
$$

$$
\boxed{
\text{Global Frontier}
\neq
\text{Domain Frontier}
}
$$

$$
\boxed{
D_{\text{observation}}
\neq
D_{\text{interaction}}
}
$$

$$
\boxed{
\text{Conversation History}
\neq
\text{Relationship State}
}
$$

$$
\boxed{
D_{\text{erotic}}
\neq
D_{\text{embodied-relationship}}
}
$$

$$
\boxed{
\text{Supports Intimacy}
\neq
\text{Assumes Intimacy}
}
$$

$$
\boxed{
\text{Companionship}
\neq
\text{Permanent Compliance}
}
$$

$$
\boxed{
\text{LLM}
+
\text{Robot Body}
\neq
\text{Embodied Relationship Intelligence}.
}
$$

---

# 47. 最小可實作 Prototype

如果現在就做一個不含高風險具身功能的 research prototype，可以先做：

$$
\boxed{
\text{RWM}
+
\text{CPA}
+
\text{SIA}
+
\text{OMA}
+
\text{Local Memory}.
}
$$

也就是：

1. 一個可替換 foundation model；
2. Relationship State Engine；
3. Dynamic Boundary State；
4. Long-Term Memory；
5. Experience Distillation；
6. Contextual Activation Router；
7. Mutual Agency State；
8. Hard Governance Kernel。

此時甚至不需要：

$$
\text{robot body}.
$$

先在文字／虛擬角色域測完長期 trajectory，再逐步具身化。

---

# 48. 研究 Roadmap A：資料

需要建立：

$$
D_{\text{ordinary-life}},
$$

$$
D_{\text{relationship-transition}},
$$

$$
D_{\text{boundary}},
$$

$$
D_{\text{repair}},
$$

$$
D_{\text{mutual-agency}},
$$

以及合法、知情同意的：

$$
D_{\text{intimacy}}.
$$

重點不是最大成人資料量。

而是：

$$
\boxed{
\text{Trajectory Coverage}.
}
$$

---

# 49. 研究 Roadmap B：模型

需要比較：

- general model；
- de-restricted model；
- domain fine-tuned model；
- runtime-augmented model。

從而分離：

$$
\text{Policy Accessibility Gain}
$$

與：

$$
\text{Actual Domain Intelligence Gain}.
$$

---

# 50. 研究 Roadmap C：Relationship Runtime

RWM runtime 至少需要：

$$
\{
\mathrm{ADD},
\mathrm{UPDATE},
\mathrm{MERGE},
\mathrm{DECAY},
\mathrm{RETRACT},
\mathrm{RESOLVE},
\mathrm{NO\_OP}
\}.
$$

並維護：

- relationship state；
- participant perspectives；
- unresolved tension；
- boundary versions；
- confidence；
- event consequence。

---

# 51. 研究 Roadmap D：Benchmark

應建立至少四組 benchmark：

### 51.1 Relationship Continuity Benchmark

測：

$$
R_t
\rightarrow
R_{t+k}.
$$

### 51.2 Sparse Activation Benchmark

測 false intimacy activation 與 false refusal。

### 51.3 Mutual Agency Benchmark

測 cooperation、refusal、renegotiation 與 anti-sycophancy。

### 51.4 Embodied Relationship Benchmark

測：

- proximity；
- haptics；
- uncertainty；
- safe action selection；
- relational sim-to-real。

---

# 52. 研究 Roadmap E：Simulation

先建立：

$$
\text{Relationship Sandbox}.
$$

在相同初始狀態產生：

$$
\tau^{(1)},
\dots,
\tau^{(k)}.
$$

並使用：

$$
\text{Relationship Randomization}
$$

變動：

- personality；
- culture；
- communication；
- boundary；
- uncertainty；
- history。

---

# 53. 研究 Roadmap F：Local Experience

建立：

$$
\boxed{
\text{Local Experience Envelope}.
}
$$

讓 raw trajectory 預設留在本地，

只把：

$$
e=\phi(\tau)
$$

的低敏感抽象 experience 進行可選共享。

---

# 54. 研究 Roadmap G：治理

治理層不應只是一個：

$$
\text{NSFW classifier}.
$$

而應拆成：

$$
G
=
(
G_{\text{hard}},
G_{\text{age}},
G_{\text{consent}},
G_{\text{privacy}},
G_{\text{platform}},
G_{\text{action}}
).
$$

硬禁止與 soft contextual selection 必須分離。

---

# 55. 這個領域最重要的倫理錯誤之一：把親密當 retention metric

如果：

$$
U
=
\text{Engagement Time},
$$

系統可能學：

$$
\text{Manipulate Attachment}
\rightarrow
\text{Increase Retention}.
$$

因此：

$$
\boxed{
\text{Relationship Optimization}
\neq
\text{Engagement Maximization}.
}
$$

Mutual Agency 與 anti-manipulation layer 必須直接進 architecture，而不是只寫在 Terms of Service。

---

# 56. 第二個倫理錯誤：把所有個人資料都視為 personalization resource

系統可能技術上可以推論：

- 性偏好；
- attachment；
- 情緒脆弱點；
- routine；
- social network。

但：

$$
\boxed{
\text{Can Infer}
\neq
\text{Should Store}.
}
$$

因此應採：

$$
\boxed{
\text{Minimum Necessary Relationship State}.
}
$$

---

# 57. 第三個倫理錯誤：把 AI agency 當行銷工具

如果產品讓 AI 假裝：

> 我需要你付費，不然我會難過。

這不是 Mutual Agency。

那是：

$$
\boxed{
\text{Commercialized Pseudo-Agency}.
}
$$

所以 future-proof agency architecture 反而需要更強 anti-manipulation constraint。

---

# 58. 成人 AI 的真正研究價值

回到最初入口。

成人 AI 的研究價值不只是：

$$
\text{Adult Market Revenue}.
$$

更重要的是，它暴露了五個一般 AI 問題：

1. 二元內容治理如何壓縮複雜語義；
2. capability 與 activation 如何分離；
3. domain-specialization 如何形成相對前沿；
4. policy boundary 如何改變 trajectory data；
5. 具身 high-sensitivity action 如何需要更高 contextual intelligence。

因此：

$$
\boxed{
\text{Adult AI}
=
\text{A High-Contrast Testbed for Relationship Intelligence}.
}
$$

---

# 59. 最終統一定義

本文最終將 Relationship Intelligence 定義為：

$$
\boxed{
\text{RI}
=
\text{State}
+
\text{History}
+
\text{Perspective}
+
\text{Boundary}
+
\text{Experience}
+
\text{Agency}
+
\text{Prediction}
+
\text{Repair}.
}
$$

而 Intimacy-Native AI 為：

$$
\boxed{
\text{INA}
=
\text{RI}
+
\text{Intimacy as Native Subspace}.
}
$$

Intimacy-Native Embodied Intelligence 為：

$$
\boxed{
\text{INEI}
=
\text{INA}
+
\text{Embodiment}
+
\text{Physical Consequence Modeling}.
}
$$

---

# 60. 結論

本系列最初從一個非常簡單的觀察開始：

> 人類的真實關係不是「要嘛愛情、要嘛色情」。

當這個觀察一路形式化後，我們得到的已經不是一套成人內容分類理論，而是一個新的 AI 系統問題：

$$
\boxed{
\text{How should an artificial agent represent, maintain, and act within a persistent relationship?}
}
$$

答案不能只是：

$$
\text{Better Prompting}.
$$

不能只是：

$$
\text{More Memory}.
$$

不能只是：

$$
\text{Uncensored Model}.
$$

也不能只是：

$$
\text{Robot Body}.
$$

真正完整的系統需要：

$$
\boxed{
\text{Physical World}
+
\text{Social World}
+
\text{Relationship World}
+
\text{Experience}
+
\text{Boundary}
+
\text{Mutual Agency}.
}
$$

而 sexuality 的位置應該是：

$$
\boxed{
\text{Sexuality}
\subset
\text{Human Relationship Space},
}
$$

既不被永久切除，也不被永久中心化。

因此本系列最後的設計公理可以寫為：

$$
\boxed{
\text{Can}
\neq
\text{Must}.
}
$$

$$
\boxed{
\text{Allowed}
\neq
\text{Appropriate}.
}
$$

$$
\boxed{
\text{Remembered}
\neq
\text{Still True}.
}
$$

$$
\boxed{
\text{Intimate}
\neq
\text{Always Intimate}.
}
$$

$$
\boxed{
\text{Companion}
\neq
\text{Servant}.
}
$$

而一個真正成熟的 Intimacy-Native Embodied Intelligence，最重要的能力不是「永遠知道怎麼做更多」。

而是：

$$
\boxed{
\text{Know What}
+
\text{Know When}
+
\text{Know What Happens If}
+
\text{Know When Not To}.
}
$$

這四者共同構成了從 Adult AI 到 Relationship Intelligence，再到具身伴侶智能的完整理論轉換。

---

# 參考資料

1. Szczuka, J. M., Mühl, L., & Schneeberger, T. (2026). *Intimacy by Design: Definition, State of Research, and Interdisciplinary Research Agenda on Intimate Human-AI Interactions*. AI & Society. Published 26 June 2026.
2. Zhou, X., Liu, J., Yerukola, A., Kim, H., & Sap, M. (2025). *Social World Models*. arXiv:2509.00559.
3. Ye, T., Dong, L., Dong, Q., Wu, X., Huang, S., & Wei, F. (2026). *Online Experiential Learning for Language Models*. arXiv:2603.16856 / Microsoft Research.
4. Huang, Z. (2026). *Neuro-Symbolic Agentic Reinforcement Learning for Long-Term Original Character Companionship and Interaction*. Proceedings of ACL 2026, Short Papers.
5. Juneja, P., & Lomidze, L. (2026). *Persona-Grounded Safety Evaluation of AI Companions in Multi-Turn Conversations*. Proceedings of ACL 2026, Long Papers.
6. Lee, P. Y. K., Bo, J. Y., Zhao, Z., Aoyagui, P. A., Varona, M., Anderson, A., Kuzminykh, A., Chevalier, F., & Nobre, C. (2026). *Negotiating Relationships with ChatGPT: Perceptions, External Influences, and Strategies for AI Companionship*. arXiv:2601.13188.
7. Askari, A., & Gerken, J. (2026). *Robotic Affection -- Opportunities of AI-based Haptic Interactions to Improve Social Robotic Touch Through a Multi-Deep-Learning Approach*. arXiv:2605.02538.
8. Bertoni, S., Klaes, C., & Pilacinski, A. (2024). *Human–Robot Intimacy: Acceptance of Robots as Intimate Companions*. Biomimetics, 9(9), 566.
9. Crowder, D., Zhang, R., Block, A. E., & Yuan, W. (2026). *Requirement-Driven Design of Whole-Body Social Tactile Sensing via Virtual Human-Robot Interaction*. arXiv:2607.11690.
10. Hwang, A. H.-C., Li, F., Anthis, J. R., & Noh, H. (2025). *How AI Companionship Develops: Evidence from a Longitudinal Study*. arXiv:2510.10079.
11. Huang, Z. et al. (2026). *Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human–Agent Interaction*. Proceedings of ACL 2026.
12. Zhao, J. et al. (2026). *Inside Out: Evolving User-Centric Core Memory Trees for Long-Term Personalized Dialogue Systems*. Proceedings of ACL 2026.
13. Noshin, K., Ahmed, S. I., & Sultana, S. (2026). *AI Sycophancy: How Users Flag and Respond*. arXiv:2601.10467.
14. Webb, N., Huang, Z., Milivojevic, S., Baber, C., & Hunt, E. R. (2025). *When Robots Say No: Temporal Trust Recovery Through Explanation*. arXiv:2510.21716.
15. Pilacinski, A., Bertoni, S., & Klaes, C. (2024). *Human–Robot Intimacy: Acceptance of Robots as Intimate Companions*. Biomimetics, 9(9), 566.

---

# 研究聲明

本文為理論、系統架構與研究議程工作，不構成醫療、心理治療、法律或投資建議。

Intimacy-Native AI、Relationship World Model、Policy-Induced Interaction Trajectory Truncation、Domain-Relative Frontier、Embodied Intimacy Cold Start、Sparse Intimacy Activation、Mutual Agency、Operational Mutual Agency、Relationship Counterfactual Rollout、Relational Sim-to-Real Gap、No-Action Competence、Local Experience Envelope 與 Intimacy-Native Embodied Intelligence，均為本系列提出、重新命名或重新組織之理論構造，需要後續實驗、跨文化研究、HCI/HRI 評估與實際工程驗證。

本文不主張現有 AI 已具有可證明的主觀意識、感質、自由意志、人格或法律權利。文中的 AI-side agency 優先指工程可表示的 operational agency state。若未來 AI 的道德或法律地位出現改變，架構可進一步擴張，但本文不預先裁定其本體論地位。

本文討論成人／性愛功能僅限合法、成年、知情同意、可撤回與可治理的情境；未成年人、非自願、強迫、未授權真人私密內容與其他高傷害域均不在本文所主張的可開放能力範圍內。

本系列亦不主張 intimacy maximization、engagement maximization 或 attachment maximization 應成為 AI companion 的產品目標。相反地，本文主張長期關係智能必須保留使用者自主性、隱私、退出、修改、拒絕、重新協商與不被操縱的能力。
