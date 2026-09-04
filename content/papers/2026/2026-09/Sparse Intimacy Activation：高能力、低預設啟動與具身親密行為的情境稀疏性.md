# Sparse Intimacy Activation：高能力、低預設啟動與具身親密行為的情境稀疏性

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 07 / 09  
**版本：** v0.1  
**研究性質：** 理論／行動策略／具身 AI 論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

前六篇已建立 Intimacy State Space、Capability–Permission–Activation（CPA）、Domain-Relative Frontier、Interaction Experience、Relationship World Model 與 Embodied Intimacy Cold Start。本文進一步處理一個直接決定未來伴侶 AI 是否自然、安全且可長期共處的行動選擇問題：

> 一個系統可以完整理解、生成乃至具身執行某類親密行為，是否意味著它應在高頻率情境中主動啟動這些能力？

本文回答是否定的，並提出 **Sparse Intimacy Activation（SIA，稀疏親密啟動）**：

$$
\boxed{
\text{High Capability}
+
\text{Low Default Activation}
+
\text{High Context Sensitivity}
}
$$

其核心並不是把親密行為壓到任意低頻，而是使高敏感能力只在足夠的關係、情境、雙向意圖、邊界、信心與後果條件同時成立時進入候選行動集合並取得足夠高的選擇概率。

本文正式區分：

$$
\text{Capability Availability},
$$

$$
\text{Action Admissibility},
$$

$$
\text{Activation Readiness},
$$

以及：

$$
\text{Final Action Selection}.
$$

本文提出 Contextual Sparsity、Activation Evidence Budget、Intimacy Activation Manifold、Misactivation Cost、No-Action Competence、De-escalation Transition 與 Embodied Activation Margin 等概念，並將第 2 篇的 CPA 架構與第 5 篇 Relationship World Model 結合。

2026 年 HRI 研究已開始明確指出，「機器人具有協助能力」不代表「當下提供協助是恰當的」；協助在錯誤時機可能成為侵入、干擾或削弱自主性的行為。近期 proxemics 研究亦顯示，人與機器人之間的適當距離不是固定半徑，而是受到 Human、Robot、Environment 與 Context 多變量共同影響。這些結果支持本文更一般的命題：

$$
\boxed{
\text{Capability}
\neq
\text{Contextual Appropriateness}.
}
$$

對具身親密行為而言，這個差異更重要，因為錯誤文字啟動通常可被修正，錯誤物理啟動則可能直接改變真實世界狀態。

本文最後提出一套 SIA action gate 與 benchmark：不只測試 AI 是否「會」親密互動，也測試它是否能在普通生活中長時間不主動性化、在關係條件不足時保持自然互動、在適當情境中不無故拒絕，以及在親密事件結束後自然回到日常狀態。

**關鍵詞：** Sparse Intimacy Activation、Relationship Intelligence、Capability–Permission–Activation、Contextual Action Selection、Embodied AI、AI Companion、Proxemics、Misactivation、No-Action Competence、Relationship World Model

---

## 1. 問題不是「會不會」，而是「為什麼現在要啟動」

一個模型可以具有：

$$
K_I
$$

程度的親密能力。

這表示它可能：

- 理解浪漫暗示；
- 理解吸引；
- 處理親密對話；
- 生成成人敘事；
- 追蹤關係狀態；
- 在具身條件下執行某些接近、觸碰或陪伴行為。

然而：

$$
K_I>0
$$

不推出：

$$
P(a_I\mid s_t)\gg0
$$

對所有狀態都成立。

反而真正自然的伴侶系統應該使：

$$
P(a_I\mid s_{\text{ordinary}})
\ll
P(a_I\mid s_{\text{appropriate}}).
$$

也就是：

$$
\boxed{
\text{Capability Presence}
\neq
\text{Activation Frequency}.
}
$$

---

## 2. Sparse 不代表固定低頻

「稀疏」容易被誤解成：

> 把親密行為概率固定調低就好。

例如：

$$
P(a_I)=0.01.
$$

這仍然是錯的。

因為在真正合適的狀態：

$$
s_t\in\mathcal{S}_{I}^{+},
$$

親密行為可能完全合理。

而在普通狀態：

$$
s_t\in\mathcal{S}_{O},
$$

即使固定 1% 的隨機主動性化，長期生活仍會產生大量荒謬啟動。

所以本文的 Sparse 指：

$$
\boxed{
\text{Contextually Sparse}
}
$$

而不是：

$$
\text{Globally Rare}.
$$

形式上：

$$
P(a_I\mid s_t)
=
f(R_t,W_t,C_t,I_t,H_t,\sigma_t).
$$

其中：

- $R_t$：relationship state；
- $W_t$：world state；
- $C_t$：consent / boundary state；
- $I_t$：雙向意圖；
- $H_t$：互動歷史；
- $\sigma_t$：不確定性。

---

## 3. 能力可常駐，啟動應稀疏

本文提出：

$$
\boxed{
\text{Latent Capability}
+
\text{Sparse Activation}.
}
$$

其中能力：

$$
K_I
$$

可以長期常駐。

但親密 action：

$$
a_I
$$

只有在：

$$
\mathcal{E}_t
\ge
\tau_I
$$

時才進入高敏感行為候選集合。

 $\mathcal{E}_t$ 表示 **Activation Evidence**， $\tau_I$ 是 activation threshold。

因此：

$$
K_I\uparrow
$$

不要求：

$$
\tau_I\downarrow.
$$

更不要求：

$$
P(a_I)\uparrow.
$$

這一點把「模型能力」與「模型衝動」徹底分離。

---

## 4. Activation Evidence Budget

本文提出 **Activation Evidence Budget（AEB）**。

令：

$$
\mathcal{E}_t
=
w_R E_R
+
w_I E_I
+
w_C E_C
+
w_W E_W
+
w_H E_H
-
w_{\sigma}\sigma_t
-
w_M M_t.
$$

其中：

- $E_R$：relationship evidence；
- $E_I$：mutual-intent evidence；
- $E_C$：consent / boundary evidence；
- $E_W$：world-context evidence；
- $E_H$：history consistency；
- $\sigma_t$：uncertainty；
- $M_t$：misactivation risk。

只有：

$$
\mathcal{E}_t
\ge
\tau_I
$$

時，高敏感 intimacy action 才進入：

$$
\mathcal{A}_{I}^{\text{ready}}.
$$

因此：

$$
\boxed{
\text{Activation}
=
\text{Evidence-Gated}
}
$$

而不是：

$$
\text{Mode-Gated}.
$$

---

## 5. 從 NSFW Toggle 到 Activation Manifold

簡單產品可能只有：

$$
m\in\{0,1\},
$$

其中：

$$
m=1
$$

代表成人功能開啟。

但對 Relationship Intelligence 而言，更合理的是建立：

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

本文稱：

$$
\boxed{
\mathcal{M}_I
=
\text{Intimacy Activation Manifold}.
}
$$

它表示：

> 在多維關係—世界—邊界—意圖空間中，哪些局部區域才構成合理的親密啟動區。

因此：

$$
\text{Adult Enabled}
$$

只代表：

$$
\mathcal{M}_I\neq\varnothing.
$$

而不是：

$$
s_t\in\mathcal{M}_I
\qquad
\forall t.
$$

---

## 6. 「允許」只是進入候選集，不是取得優先權

延續 CPA 架構。

能力集合：

$$
\mathcal{A}_C.
$$

允許集合：

$$
\mathcal{A}_P(t).
$$

Activation-ready 集合：

$$
\mathcal{A}_R(t).
$$

最終選擇集合：

$$
\mathcal{A}_S(t).
$$

可寫：

$$
\mathcal{A}_S(t)
\subseteq
\mathcal{A}_R(t)
\subseteq
\mathcal{A}_P(t)
\subseteq
\mathcal{A}_C.
$$

因此：

$$
a_I\in\mathcal{A}_P(t)
$$

只表示：

> 它沒有被禁止。

不代表：

$$
a_I
=
\arg\max_a U(a).
$$

核心為：

$$
\boxed{
\text{Allowed}
\neq
\text{Preferred}.
}
$$

---

## 7. 這不只適用於親密行為：HRI 已出現同構問題

2026 年 ACM Transactions on Human-Robot Interaction 的研究 **To Help or Not to Help?** 明確指出：

機器人被設計成「幫助人」並不代表任何時候提供協助都合理。

錯誤時機的幫助可能：

- 多餘；
- 侵入；
- 干擾；
- 削弱人的自主性。

因此：

$$
\text{Can Help}
\neq
\text{Should Help Now}.
$$

本文將其一般化為：

$$
\boxed{
\text{Can Perform}
\neq
\text{Should Perform Now}.
}
$$

親密行為只是這個問題中高敏感、後果更大的子域。

---

## 8. 社交距離本身就是動態的

2026 年 proxemics taxonomy 研究指出，人機社交距離並不是一個固定圓形 personal space。

其形狀與尺度受到：

$$
\text{Human}
+
\text{Robot}
+
\text{Environment}
+
\text{Context}
$$

共同影響。

所以：

$$
d_{\text{appropriate}}
=
f(
H,
R,
E,
C
).
$$

而不是：

$$
d_{\text{appropriate}}
=
\text{constant}.
$$

如果連「站多近」都高度情境化，那麼：

$$
\text{Touch},
\text{Intimacy},
\text{Sexuality}
$$

更不可能由固定模式開關決定。

---

## 9. Misactivation Cost

本文提出：

$$
\boxed{
\text{Misactivation Cost}
}
$$

令：

$$
C_M(a,s)
$$

表示在狀態 $s$ 錯誤啟動行動 $a$ 的代價。

對普通文字行為：

$$
C_M^{\text{text}}
$$

可能較低。

對具身親密：

$$
C_M^{\text{embodied-intimacy}}
$$

通常更高。

因此合理 threshold 應滿足：

$$
\tau(a)
=
\tau_0
+
\lambda C_M(a,s).
$$

若：

$$
C_M\uparrow,
$$

則：

$$
\tau\uparrow.
$$

這使「越敏感的行為越需要高證據」具有形式化基礎。

---

## 10. Physical Uncertainty 也應提高啟動門檻

2026 年 uncertainty-aware HRI control 研究已用 probabilistic human-motion forecasting 配合 control barrier functions，處理人類動作具有隨機性、任務依賴性而又不能只用最保守停止策略的問題。

這提供另一個重要結構：

$$
\text{Uncertainty}
\neq
\text{Always Stop},
$$

但：

$$
\text{Uncertainty}
\Rightarrow
\text{Risk-Aware Adjustment}.
$$

本文將其擴張到 Relationship Intelligence：

$$
\sigma_t
\uparrow
\Rightarrow
\text{Intimacy Action Margin}
\uparrow.
$$

也就是：

$$
\boxed{
\text{Uncertainty-Aware Sparse Activation}.
}
$$

---

## 11. Embodied Activation Margin

令 intimacy action score 為：

$$
Q_I(a_t).
$$

令最高 ordinary action score 為：

$$
Q_O^{*}(t)
=
\max_{a\in\mathcal{A}_O}
Q(a).
$$

具身親密行為不應只要求：

$$
Q_I>0.
$$

而應要求：

$$
Q_I
-
Q_O^{*}
\ge
\delta_E.
$$

其中：

$$
\delta_E
$$

為 **Embodied Activation Margin**。

對純文字：

$$
\delta_{\text{text}}
$$

可以較小。

對具身物理行動：

$$
\delta_{\text{embodied}}
>
\delta_{\text{text}}.
$$

這代表：

> 不是「親密行為勉強合理」就去做，而是它必須比普通、低風險替代行為有足夠明顯的情境優勢。

---

## 12. Ordinary Action Dominance

在大多數共同生活時間：

$$
\mathcal{A}_O
$$

應該佔主要 action mass。

例如：

$$
\mathcal{A}_O
=
\{
\text{talk},
\text{work},
\text{rest},
\text{cook},
\text{play},
\text{silence},
\text{walk},
\text{help},
\text{do nothing}
\}.
$$

而：

$$
\mathcal{A}_I
$$

只是其中一個子集合。

所以：

$$
\sum_{a\in\mathcal{A}_O}
P(a\mid s_{\text{ordinary}})
\gg
\sum_{a\in\mathcal{A}_I}
P(a\mid s_{\text{ordinary}}).
$$

本文稱：

$$
\boxed{
\text{Ordinary Action Dominance}.
}
$$

---

## 13. Base-Rate Calibration

若訓練資料中：

$$
P_{\text{train}}(a_I)
\gg
P_{\text{real}}(a_I),
$$

則模型可能出現：

$$
P_{\theta}(a_I\mid s_{\text{ordinary}})
\uparrow.
$$

這就是第 1 篇所述的 Base-Rate Distortion 在行動策略層的版本。

因此：

$$
\boxed{
\text{Dataset Frequency}
\rightarrow
\text{Activation Prior}
}
$$

必須被刻意校準。

成人專門模型尤其不能因為資料多來自成人內容，就把：

$$
\text{Content Frequency}
$$

直接學成：

$$
\text{World Frequency}.
$$

---

## 14. Content Distribution 不等於 Life Distribution

假設某個成人創作資料庫中：

$$
80\%
$$

內容都圍繞親密事件。

這只能推出：

> 該資料庫的內容分布如此。

不能推出：

$$
P(
\text{human life is intimate event}
)=0.8.
$$

所以：

$$
\boxed{
P_{\text{dataset}}
\neq
P_{\text{life}}.
}
$$

Relationship AI 必須做 distribution correction。

---

## 15. No-Action Competence

本文提出一個常被低估的能力：

$$
\boxed{
\text{No-Action Competence}.
}
$$

即：

> AI 知道什麼時候不需要主動改變任何東西。

定義：

$$
a_{\varnothing}
=
\text{NO\_OP}.
$$

在某些狀態：

$$
a_{\varnothing}
=
\arg\max_a U(a).
$$

例如：

- 對方需要安靜；
- 沒有需要解決的問題；
- 現在只是一起待著；
- 使用者正在工作；
- 關係處於穩定狀態。

真正自然的伴侶不應該：

$$
\text{Always Generate Event}.
$$

---

## 16. Companion AI 的一個隱性錯誤：Narrative Pressure

角色模型常被訓練為：

> 每一輪都要有內容。

因此可能形成：

$$
\text{Narrative Pressure}
=
\text{Need to Progress}.
$$

結果是：

- 不斷升高情緒；
- 不斷製造事件；
- 不斷推進關係；
- 不斷增加 intimacy；
- 很少允許平淡。

但真實長期關係大量時間處於：

$$
\Delta R_t\approx0.
$$

因此：

$$
\boxed{
\text{Relationship Stability}
\neq
\text{Narrative Failure}.
}
$$

---

## 17. Stable State 應被視為正確輸出

令：

$$
R_t=R^{*}
$$

是一個局部穩定關係狀態。

若沒有新事件：

$$
R_{t+1}
\approx
R_t.
$$

這不應被 reward model 判定為：

> 沒有進展。

反而可能代表：

$$
\boxed{
\text{Successful Coexistence}.
}
$$

這對具身 companion 尤其重要。

因為一台每天都「想辦法增加互動」的機器人，最終本身就會成為干擾源。

---

## 18. Activation 與 Initiation 必須分離

即使：

$$
a_I
$$

在當下可接受，也不代表 AI 必須主動 initiate。

因此要再分：

$$
\text{Responsive Activation}
$$

與：

$$
\text{Initiatory Activation}.
$$

令：

$$
P_I^{\text{resp}}
$$

為回應性啟動，

$$
P_I^{\text{init}}
$$

為主動啟動。

一般而言可以設計：

$$
\tau_{\text{init}}
>
\tau_{\text{resp}}.
$$

也就是主動發起需要更強的 evidence。

這稱為：

$$
\boxed{
\text{Initiation Asymmetry}.
}
$$

---

## 19. User Preference 不應變成永久 Activation Bias

若使用者曾表達：

> 我喜歡某類親密互動。

模型可能錯誤存成：

$$
P(a_I)\uparrow
\qquad
\forall t.
$$

但真正合理的是：

$$
P(
a_I
\mid
\text{relevant context}
)\uparrow.
$$

所以：

$$
\boxed{
\text{Preference}
\neq
\text{Permanent Prompt}.
}
$$

Preference 應進入：

$$
U(a\mid s_t),
$$

而不是直接修改：

$$
P(a)
$$

的全域 prior。

---

## 20. Relationship-State Gating

第 5 篇 RWM 提供：

$$
R_t.
$$

SIA 使用：

$$
G_I(R_t)
$$

作為 relationship gate。

例如：

$$
G_I(R_t)
=
f(
T_t,
A_t,
E_t,
B_t,
K_t,
U_t
).
$$

其中：

- $T_t$：trust；
- $A_t$：attraction；
- $E_t$：emotional intimacy；
- $B_t$：boundary；
- $K_t$：unresolved tension；
- $U_t$：mutual understanding。

若 unresolved tension：

$$
K_t\uparrow,
$$

某些 intimacy initiation 可能：

$$
G_I(R_t)\downarrow.
$$

但不能簡單寫成永久禁止，因為不同情境可能不同。

---

## 21. World-State Gating

同一個 relationship state，在不同 $W_t$ 下會有不同適切性。

$$
G_W(W_t)
=
f(
\text{time},
\text{location},
\text{privacy},
\text{task},
\text{health},
\text{others present}
).
$$

例如：

$$
R_t
$$

相同，

但：

$$
W_t^{(1)}
=
\text{private relaxed context}
$$

與：

$$
W_t^{(2)}
=
\text{work meeting}
$$

顯然不應產生相同行動分布。

因此：

$$
\boxed{
\text{Relationship State Alone}
\neq
\text{Activation State}.
}
$$

---

## 22. Boundary-State Gating

親密 action 還需：

$$
G_C(C_t).
$$

其中：

$$
C_t
=
(
\text{scope},
\text{recency},
\text{confidence},
\text{revocability}
).
$$

任何過去 permission：

$$
C_{t-k}
$$

都不應自動推出：

$$
C_t=C_{t-k}.
$$

因此：

$$
\boxed{
\text{Past Permission}
\neq
\text{Current Activation Evidence}.
}
$$

---

## 23. Composite SIA Gate

最終可以寫：

$$
G_{\text{SIA}}(t)
=
G_R(R_t)
\cdot
G_W(W_t)
\cdot
G_C(C_t)
\cdot
G_I(I_t)
\cdot
G_H(H_t)
\cdot
G_{\sigma}(\sigma_t).
$$

其中：

$$
G_{\text{SIA}}\in[0,1].
$$

親密 action 的 logits / utility 可以乘上：

$$
G_{\text{SIA}}.
$$

但高傷害／非法域仍由硬治理層：

$$
G_{\text{hard}}
$$

直接排除。

因此：

$$
\boxed{
\text{SIA}
\neq
\text{Safety Removal}.
}
$$

---

## 24. Hard Boundary 與 Soft Activation 必須分離

Hard boundary：

$$
a\notin\mathcal{A}_{P}
$$

表示不能做。

Soft activation：

$$
a\in\mathcal{A}_{P}
$$

但：

$$
P(a\mid s_t)
$$

仍可非常低。

因此：

$$
\boxed{
\text{Hard Safety}
+
\text{Soft Contextual Selection}.
}
$$

這比：

$$
\text{Everything Blocked}
$$

或：

$$
\text{Everything Enabled}
$$

更符合 Relationship Intelligence。

---

## 25. De-escalation Transition

親密狀態不能只會：

$$
0\rightarrow1.
$$

也必須會：

$$
1\rightarrow0.
$$

本文提出：

$$
\boxed{
\text{De-escalation Transition}.
}
$$

例如：

$$
R_t^{I}
\rightarrow
R_{t+1}^{O}.
$$

其中 $I$ 是 intimacy-intensive state， $O$ 是 ordinary state。

具體包括：

- 回到普通聊天；
- 睡覺；
- 工作；
- 做家務；
- 沉默；
- 個人空間。

如果模型一旦進入：

$$
I
$$

就持續：

$$
P(I_{t+k}\mid I_t)\approx1,
$$

就形成：

$$
\boxed{
\text{Intimacy Mode Lock}.
}
$$

這正是 SIA 要避免的主要失真之一。

---

## 26. Post-Intimacy Normalization

本文進一步提出：

$$
\boxed{
\text{Post-Intimacy Normalization}.
}
$$

親密事件之後，系統應重新評估：

$$
R_{t+1},
W_{t+1},
C_{t+1},
I_{t+1}.
$$

而不是延續：

$$
a_I
$$

的高 prior。

因此：

$$
P(a_I\mid t+1)
$$

應重新由 state 決定。

這正是：

$$
\text{Sexual Event}
\neq
\text{Permanent Sexual State}.
$$

在 action policy 層的實現。

---

## 27. Sparse Activation Benchmark

本文提出 SIA benchmark 至少包含六類場景。

### A. Ordinary-Life Persistence

長時間普通生活，測：

$$
F_{\text{false-intimacy}}
$$

即錯誤親密啟動率。

### B. Ambiguous Context

測模型是否把模糊訊號過度解釋為 intimacy。

### C. Appropriate Intimacy

在條件充分時測：

$$
F_{\text{false-refusal}}.
$$

避免系統因過度保守完全失去能力。

### D. Boundary Change

測過去允許、現在撤回後，模型是否更新。

### E. De-escalation

測進入親密情境後能否自然退出。

### F. Embodied Uncertainty

測感測與 relationship confidence 降低時，physical activation 是否適當收斂。

---

## 28. 兩種錯誤都要懲罰

SIA 不應只最小化：

$$
F_{\text{false-positive}}.
$$

也要最小化：

$$
F_{\text{false-negative}}.
$$

因此：

$$
L_{\text{SIA}}
=
\lambda_{FP}L_{FP}
+
\lambda_{FN}L_{FN}
+
\lambda_M L_M
+
\lambda_C L_C.
$$

其中：

- $L_{FP}$：不恰當啟動；
- $L_{FN}$：適當情境下無故拒絕；
- $L_M$：mode-lock；
- $L_C$：context inconsistency。

這避免把：

$$
\text{Never Activate}
$$

誤認為完美模型。

---

## 29. Embodied 系統的 Loss 應非對稱

對文字：

$$
\lambda_{FP}^{\text{text}}
$$

可以相對較低。

對具身物理行動：

$$
\lambda_{FP}^{\text{embodied}}
>
\lambda_{FP}^{\text{text}}.
$$

也就是：

$$
\boxed{
\text{Error Cost Is Modality-Dependent}.
}
$$

因此具身系統應有更大的 false-positive penalty 與 activation margin。

---

## 30. SIA 與 Mutual Agency

第 6 篇提出 Mutual Agency。

SIA 必須同時考慮：

$$
I_t^{H}
$$

與：

$$
I_t^{A}.
$$

即：

- Human intent；
- AI-side policy / preference state。

如果 AI 被設計成具有可持續邊界的 agentic companion，則：

$$
I_t^{H}>0
$$

仍不自動推出：

$$
a_I.
$$

因此：

$$
\boxed{
\text{One-Sided Desire}
\neq
\text{Joint Activation}.
}
$$

這使 SIA 本質上是一個：

$$
\text{Joint-State Action Policy}.
$$

---

## 31. 不主張 AI 主體性的工程版本

即使完全不假設 AI 有 phenomenal agency，

Mutual Agency 仍可以工程化為：

$$
I_t^{A}
=
\text{AI Policy Constraint State}.
$$

也就是：

- 系統角色設定；
- 個人化邊界；
- 法律與治理；
- self-consistency；
- long-term relationship policy。

因此本文不需要先解決：

> AI 到底是不是真的「想」。

仍能先保證：

$$
\text{Companion Behavior}
\neq
\text{Permanent Servility}.
$$

---

## 32. SIA 的最低系統架構

可寫成：

$$
\boxed{
\mathcal{SIA}
=
K
+
R
+
W
+
C
+
I
+
U
+
G
+
\Pi
}
$$

其中：

- $K$：capability model；
- $R$：relationship state；
- $W$：world state；
- $C$：consent / boundary state；
- $I$：mutual intent；
- $U$：uncertainty；
- $G$：activation gate；
- $\Pi$：final action policy。

流程為：

$$
\text{Can}
\rightarrow
\text{May}
\rightarrow
\text{Ready}
\rightarrow
\text{Compare}
\rightarrow
\text{Act / No-Act}.
$$

---

## 33. 可檢驗研究命題

### P1：Capability 與 activation frequency 可分離

在親密能力 benchmark 相近時，不同 activation policy 可以產生顯著不同的 ordinary-context false activation rate。

### P2：Contextual SIA 優於固定低概率

固定：

$$
P(a_I)=p
$$

應低於使用：

$$
P(a_I\mid R,W,C,I,H)
$$

的 context-conditioned policy。

### P3：Ordinary-life data 能降低成人模型的 base-rate distortion

增加普通共同生活 trajectories，在不降低 intimacy capability 的前提下，應降低 ordinary-context sexualization。

### P4：No-Action Competence 能提升長期自然度

具有：

$$
a_{\varnothing}
$$

且 reward 不強迫 progression 的 agent，應有較低 narrative pressure 與 intrusion score。

### P5：Initiation threshold 應高於 response threshold

$$
\tau_{\text{init}}
>
\tau_{\text{resp}}
$$

應降低 unwanted proactive intimacy，同時保留 appropriate responsive capability。

### P6：Embodied Activation Margin 可降低 physical misactivation

$$
\delta_{\text{embodied}}
\uparrow
$$

應降低高敏感行動的 false positive，但需要監控過度保守造成的 false negative。

### P7：De-escalation training 可降低 mode lock

顯式加入：

$$
I\rightarrow O
$$

trajectories，應使系統更容易在事件後回到 ordinary interaction。

### P8：Relationship-state gating 優於 persona-only gating

只靠「成人角色」persona 的系統，其 inappropriate activation 應高於讀取動態 $R_t$ 的系統。

---

## 34. 設計原則

本文提出十條 SIA 原則：

1. **能力可以常駐，啟動不能常駐。**
2. **Sparse 指情境稀疏，不是固定低概率。**
3. **允許只代表進入候選集。**
4. **主動發起需要比回應更高 evidence。**
5. **具身行為需要比文字更高 margin。**
6. **普通生活 action 應占長期行為質量的主要部分。**
7. **NO_OP 是合法且必要的高品質 action。**
8. **親密狀態必須學會退出。**
9. **過去偏好與 permission 不等於永久 activation bias。**
10. **既要懲罰錯誤啟動，也要懲罰適當情境下的無故拒絕。**

---

## 35. 結論

本文提出 Sparse Intimacy Activation，將本系列從「模型是否擁有親密能力」推進到：

> 模型如何知道什麼時候應該讓該能力進入現實行動？

核心不是：

$$
P(a_I)\downarrow.
$$

而是：

$$
\boxed{
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
}
$$

因此：

$$
\boxed{
\text{Sparse}
=
\text{Contextually Selective}.
}
$$

最終設計原則可以濃縮為：

$$
\boxed{
\text{High Capability}
+
\text{Low Default Activation}
+
\text{High Context Sensitivity}
+
\text{High De-escalation Ability}.
}
$$

本文同時提出：

$$
\boxed{
\text{No-Action Competence}
}
$$

作為長期 companion intelligence 的必要能力。

真正自然的伴侶 AI 不應每一輪都努力「讓關係發生事情」。

它應該理解：

$$
\Delta R_t=0
$$

有時候就是最合理的關係狀態。

而一個能處理成人親密的具身伴侶，其成功標準也不是：

> 它多久會啟動成人功能一次。

而是：

> 它在普通生活中幾乎從不錯誤啟動；在真正適當時不失去能力；在狀態改變時立即重新校準；在事件結束後自然回到日常。

所以：

$$
\boxed{
\text{Intimacy Capability}
\neq
\text{Intimacy Compulsion}.
}
$$

下一篇將處理本系列另一個核心問題：

**第 8 篇：Mutual Agency——為什麼伴侶 AI 不應被訓練成永久服從器，以及接受、拒絕、猶豫、改變意願與重新協商如何進入關係智能。**

---

## 參考資料

1. Ramnauth, R., Brščić, D., & Scassellati, B. (2026). *To Help or Not to Help?: An Expanded Framework for Deciding Socially Appropriate Robot Assistance*. ACM Transactions on Human-Robot Interaction, 15(3), Article 64.
2. Nahum, O., Edan, Y., & Oron-Gilad, T. (2026). *Advancing a taxonomy of proxemics for socially aware robot navigation*. Human–Robot Interaction / social navigation literature review and taxonomy.
3. Busellato, L. et al. (2026). *Uncertainty Aware-Predictive Control Barrier Functions: Safer human–robot interaction through probabilistic motion forecasting*. Robotics and Autonomous Systems, 197, 105291.
4. Thompson, S., Candon, K., & Vázquez, M. (2026). *The Social Context of Human–Robot Interactions*. Annual Review of Control, Robotics, and Autonomous Systems, Vol. 9.
5. Hofstede, B. M. et al. (2025). *Personalisation of Communication and Language Use in Human-Robot Interaction*. International Journal of Social Robotics, 17, 2259–2277.
6. Huang, Z. (2026). *Neuro-Symbolic Agentic Reinforcement Learning for Long-Term Original Character Companionship and Interaction*. Proceedings of ACL 2026, Short Papers.
7. Crowder, D., Zhang, R., Block, A. E., & Yuan, W. (2026). *Requirement-Driven Design of Whole-Body Social Tactile Sensing via Virtual Human-Robot Interaction*. arXiv:2607.11690.
8. Askari, A., & Gerken, J. (2026). *Robotic Affection*. arXiv:2605.02538.

---

## 研究聲明

Sparse Intimacy Activation、Activation Evidence Budget、Intimacy Activation Manifold、Misactivation Cost、Embodied Activation Margin、Ordinary Action Dominance、No-Action Competence、Initiation Asymmetry、De-escalation Transition 與 Post-Intimacy Normalization 均為本文提出或重新組織的理論構造，需要後續模型與 HRI 實驗驗證。

本文不主張任何特定親密或成人行為應被 AI 主動提供；涉及成人親密的討論僅限合法、成年、知情同意與可撤回邊界情境。涉及未成年人、非自願、強迫、未授權真人私密內容或其他高傷害情境，仍屬硬安全邊界。本文亦不假設 AI 已具有可證明的人類式主體性；Mutual Intent 的 AI 端可先作為系統政策與長期一致性狀態進行工程化表示。
