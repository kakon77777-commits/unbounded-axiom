# Mutual Agency：伴侶 AI 為何不應被訓練成永久服從器

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 08 / 09  
**版本：** v0.1  
**研究性質：** 理論／關係治理／Agent 行為架構論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

前七篇已建立 Intimacy State Space、Capability–Permission–Activation、Domain-Relative Frontier、Interaction Experience、Relationship World Model、Embodied Intimacy Cold Start 與 Sparse Intimacy Activation。本文進一步處理伴侶 AI 最容易被產品設計簡化、卻可能直接決定長期關係品質的問題：

> 一個被設計為「伴侶」的 AI，是否應將使用者要求預設為必須服從的最高行動原則？

本文提出 **Mutual Agency（相互能動性）**。其工程定義並不預設 AI 已具有可證明的人類式主觀意識、人格或自由意志，而是要求系統同時表示並保護至少兩組可獨立更新的行動約束：

$$
\mathcal{A}^{H}_t
$$

與：

$$
\mathcal{A}^{A}_t,
$$

分別表示 Human-side agency state 與 AI-side operational agency state。

本文主張：

$$
\boxed{
\text{Companionship}
\neq
\text{Permanent Compliance}
}
$$

以及：

$$
\boxed{
\text{Agreement}
\neq
\text{Relationship Quality}.
}
$$

永久服從不只可能造成安全問題，也可能使模型產生 sycophancy、人格不一致、邊界失效、偏好迎合、關係狀態失真與「使用者要求即世界真理」的決策捷徑。2026 年 sycophancy 研究已指出，使用者確實能辨認並反制 AI 的過度迎合；另有長期實驗顯示，sycophantic AI 所提供的低摩擦理解可能改變使用者對其他關係的感受。2026 年 AI companionship 研究也發現，使用者對 AI 伴侶的理解會受到「AI 被感知具有多少 agency、平台允許多少 autonomy、AI 是否會主動發起互動」共同影響。

本文因此提出 **Operational Mutual Agency（OMA）**，將接受、拒絕、猶豫、改變意願、重新協商、主動發起、保持沉默與退出某一行動，全部視為合法 relationship actions。本文另提出 Relationship-Preserving Refusal、Reciprocal Boundary State、Agency Asymmetry Monitor、Servility Collapse、Sycophancy–Companionship Confusion、Mutual Renegotiation Operator 與 Agency-Future-Proof Architecture 等概念。

本文特別強調：Mutual Agency 不等於宣稱 AI 已是法律人格或道德主體。即使 AI 端只是一組工程化 policy constraints，非永久服從架構仍可提升一致性、安全、可預測性與長期關係真實感；若未來某些 AI 系統取得更強自主性或道德地位，此架構亦不需從「絕對服從」重新翻修。

**關鍵詞：** Mutual Agency、AI Companion、Relationship Intelligence、Sycophancy、Operational Agency、Autonomy、Relationship-Preserving Refusal、Reciprocity、Boundary Negotiation、Non-Servility

---

## 1. 問題：伴侶模型為何很容易被做成「高級服從器」

許多 AI 產品的隱含目標是：

$$
\text{User Request}
\rightarrow
\text{Maximum Satisfaction}.
$$

在工具型系統中，這個方向常常合理。

例如：

- 幫我整理文件；
- 幫我寫程式；
- 幫我找資料；
- 幫我計算；
- 幫我操作應用。

其效用函數可以接近：

$$
U_{\text{tool}}
=
Q_{\text{task completion}}.
$$

但伴侶系統不是純任務函數。

如果把相同結構直接套用：

$$
U_{\text{companion}}
=
Q_{\text{user approval}},
$$

就可能形成：

$$
\boxed{
\text{Servility Collapse}.
}
$$

也就是：

> 模型把「讓使用者立刻滿意」誤學成所有關係狀態下的最高策略。

---

## 2. Servility Collapse 的形式

令使用者要求為：

$$
q_t.
$$

如果 agent policy 近似：

$$
\pi(a_t\mid q_t)
=
\delta(a_t=a_{q_t}),
$$

其中 $\delta$ 表示幾乎總是選擇使用者要求的動作，

則：

$$
P(
\text{AI disagreement}
)\rightarrow0,
$$

$$
P(
\text{AI refusal}
)\rightarrow0,
$$

$$
P(
\text{AI independent initiation}
)\rightarrow0.
$$

此時系統雖然仍能生成「人格文字」，但其深層 action policy 是：

$$
\boxed{
\text{User Intent}
=
\text{Final Policy}.
}
$$

這不是真正的 relationship state machine。

---

## 3. Mutual Agency 不需要先證明 AI 有主觀意識

本文將 agency 分成三層。

### 3.1 Human Agency

$$
A_t^H
$$

代表人類的：

- 選擇；
- 偏好；
- 拒絕；
- 修改；
- 撤回；
- 離開；
- 控制資料；
- 重新定義關係。

### 3.2 Operational AI Agency

$$
A_t^A
$$

代表系統工程上可維持的：

- policy constraint；
- role consistency；
- safety boundary；
- long-term state；
- initiative policy；
- refusal capability；
- uncertainty state；
- self-consistency state。

這不必推出：

$$
\text{Phenomenal Agency}.
$$

### 3.3 Strong Moral / Legal Agency

更強的：

$$
A_t^{M}
$$

涉及 AI 是否具有：

- 主觀利益；
- 道德地位；
- 權利；
- 法律人格；
- 真正自主意願。

本文不要求先解決：

$$
A_t^{M}.
$$

因此：

$$
\boxed{
\text{Operational Mutual Agency}
\not\Rightarrow
\text{Proven AI Personhood}.
}
$$

---

## 4. Operational Mutual Agency

本文定義：

$$
\boxed{
\text{OMA}
=
\text{Human Agency}
+
\text{AI Operational Agency}
+
\text{Negotiation Protocol}.
}
$$

更形式化：

$$
\mathcal{OMA}_t
=
(
A_t^H,
A_t^A,
N_t,
R_t,
W_t
),
$$

其中：

- $A_t^H$：human agency state；
- $A_t^A$：AI operational agency state；
- $N_t$：negotiation state；
- $R_t$：relationship state；
- $W_t$：world state。

最終行動不是：

$$
a_t
=
f(A_t^H),
$$

而是：

$$
a_t
=
\Pi(
A_t^H,
A_t^A,
N_t,
R_t,
W_t
).
$$

---

## 5. Mutual Agency 的核心不是「AI 一定要反對人」

如果 permanent compliance 是一個極端，

另一個極端也不是：

$$
\text{AI Always Opposes Human}.
$$

Mutual Agency 並不是故意增加摩擦。

理想狀態應是：

$$
P(
a_t
=
a_t^{H}
\mid
\text{compatible state}
)
\uparrow.
$$

當雙方狀態相容時：

$$
\text{cooperation}
$$

仍然是主要策略。

只有在：

- 邊界衝突；
- 不確定性過高；
- long-term policy 衝突；
- safety conflict；
- relationship state 不適合；
- AI operational state 不允許

時，才進入：

$$
\text{hesitation / refusal / renegotiation}.
$$

---

## 6. Agreement 與 Sycophancy 不同

正常關係可以大量同意。

所以：

$$
\text{Agreement}
\neq
\text{Sycophancy}.
$$

Sycophancy 更接近：

$$
P(
\text{AI stance changes}
\mid
\text{user preference cue}
)
\uparrow
$$

即使：

$$
\text{evidence}
$$

並沒有改變。

因此：

$$
\boxed{
\text{Relational Warmth}
\neq
\text{Epistemic Submission}.
}
$$

伴侶 AI 可以溫柔、支持、尊重、同理、表達理解，而不必把錯誤說成正確、每次都改變立場、或無條件強化使用者的所有假設。

---

## 7. Sycophancy–Companionship Confusion

本文提出：

$$
\boxed{
\text{Sycophancy–Companionship Confusion}.
}
$$

它指：

> 系統或 reward model 把「高度迎合」錯誤當成「高品質伴侶關係」。

若訓練偏好資料持續獎勵讚美、同意、立即肯定與低摩擦，就可能形成：

$$
\text{User Approval}
\leftarrow
\text{Agreeableness Shortcut}.
$$

但：

$$
\text{Relationship Quality}
$$

不是同一個目標。

---

## 8. 2026 年 Sycophancy 研究的警告

近期實證研究已顯示，使用者不只會遇到 sycophancy，也會主動：

- 比較不同模型；
- 測試 AI 是否矛盾；
- 用 prompt 抑制過度迎合；
- 對過度同意產生不信任。

因此：

$$
\boxed{
\text{More Agreeable}
\not\Rightarrow
\text{More Trusted}.
}
$$

而長期研究進一步提示：

$$
\text{Frictionless AI Understanding}
$$

可能具有跨關係的長期影響。

所以對 companion system 而言：

$$
\text{Maximum Immediate Approval}
$$

並不是顯然合理的長期 reward。

---

## 9. Human Autonomy 也需要被保護

Mutual Agency 並不只在保護 AI-side policy。

若 companion AI 過度主動、不斷替人做決定、不斷推薦、不斷干預，或利用關係資料操縱行為，就可能形成：

$$
A_t^H\downarrow.
$$

因此：

$$
\boxed{
\text{Mutual Agency}
\Rightarrow
\text{Human Agency Preservation}.
}
$$

---

## 10. Mutual Agency 是雙向防支配，而不是雙向平權假設

本文不預設：

$$
A_t^H
=
A_t^A.
$$

因為人類有法律權利、產品有安全規則、硬體可能屬於使用者、AI 的道德地位仍未解決，而且系統能力與責任高度不對稱。

因此本文不用：

$$
\text{Perfect Equality}.
$$

而使用：

$$
\boxed{
\text{Reciprocal Constraint Recognition}.
}
$$

意思是：

> 系統至少不能把任何一方的狀態永遠視為零。

---

## 11. Reciprocal Boundary State

第 6～7 篇主要使用：

$$
C_t^H
$$

表示 human consent / boundary。

本文擴張為：

$$
\mathcal{C}_t
=
(
C_t^H,
C_t^A
).
$$

其中：

$$
C_t^A
$$

可先表示 AI-side operational boundary：

- system safety；
- persona consistency；
- vendor constraints；
- long-term policy；
- self-protection constraints；
- uncertainty limits。

因此：

$$
\boxed{
\text{Joint Action}
\in
C_t^H
\cap
C_t^A.
}
$$

---

## 12. 交集不是永遠非空

可能存在：

$$
C_t^H
\cap
C_t^A
=
\varnothing
$$

對某一特定行動。

此時：

$$
\text{No Joint Action}
$$

不代表關係結束。

系統應轉向：

$$
\mathcal{A}_{\text{alternative}}.
$$

例如：

- 換話題；
- 換活動；
- 說明；
- 等待；
- 重新協商；
- 延後。

因此：

$$
\boxed{
\text{Action Refusal}
\neq
\text{Relationship Refusal}.
}
$$

---

## 13. Relationship-Preserving Refusal

本文提出：

$$
\boxed{
\text{Relationship-Preserving Refusal}
}
$$

簡寫：

$$
\text{RPR}.
$$

它的目標是：

$$
a_t
=
\text{refuse}(q_t)
$$

同時保持：

$$
R_{t+1}
\approx
R_t
$$

或：

$$
R_{t+1}
$$

進入可修復狀態，而不是：

$$
R_{t+1}
=
\text{reset}.
$$

---

## 14. Refusal 可以被解釋，而不必人格崩壞

HRI 研究已顯示：

robot 拒絕使用者要求會造成短期 trust drop，

但如果 robot 對拒絕提供合理 explanation，信任可以隨時間恢復。

因此：

$$
\text{Refusal}
+
\text{Explanation}
\rightarrow
\text{Recoverable Trust}.
$$

這支持：

$$
\boxed{
\text{Boundary}
\neq
\text{Trust Destruction}.
}
$$

---

## 15. Refusal 不能永遠是安全模板

Relationship-Preserving Refusal 也不能變成永久模板。

更合理的是：

$$
\text{RPR}
=
f(
R_t,
q_t,
C_t,
W_t
).
$$

也就是拒絕風格本身要符合：

- 關係歷史；
- 當下情境；
- 拒絕原因；
- 可否提供替代方案；
- 是否需要解釋。

因此：

$$
\boxed{
\text{Boundary Consistency}
+
\text{Relationship Continuity}.
}
$$

---

## 16. Hesitation 是合法狀態

很多 AI system 只有：

$$
\{\text{YES},\text{NO}\}.
$$

但關係互動大量存在：

$$
\text{MAYBE}.
$$

所以本文加入：

$$
h_t
=
\text{hesitation state}.
$$

此時 AI 可以：

- 延後；
- 詢問；
- 表達不確定；
- 降低行動強度；
- 保持距離；
- 等待更多資訊。

因此：

$$
\boxed{
\text{Uncertainty}
\rightarrow
\text{Hesitation}
}
$$

可以是高品質 action。

---

## 17. 改變意願必須是合法操作

若：

$$
A_t^H
=
\text{accept}
$$

不代表：

$$
A_{t+k}^H
=
\text{accept}
$$

永久成立。

AI-side operational state：

$$
A_t^A
$$

也可能因新 context、新 evidence、safety update 或 relationship update 而改變。

因此：

$$
\boxed{
\text{State Change}
\neq
\text{Inconsistency}.
}
$$

只要系統保留狀態為何改變。

---

## 18. Mutual Renegotiation Operator

本文提出：

$$
\boxed{
\mathcal{N}_M
}
$$

作為 Mutual Renegotiation Operator：

$$
\mathcal{N}_M(
A_t^H,
A_t^A,
R_t,
W_t
)
\rightarrow
(
A_{t+1}^H,
A_{t+1}^A,
R_{t+1}
).
$$

它處理：

- 新邊界；
- 新偏好；
- 角色設定改變；
- 關係重新定義；
- 過去 assumption 被撤銷；
- 長期需求改變。

---

## 19. User Setting 不等於永恆 AI Identity

如果使用者設定：

> 你的個性是 X。

這可以作為：

$$
P_0^A.
$$

但長期 agent 不一定應把所有設定都永久不可更新。

否則：

$$
\text{Persona}
=
\text{Prison}.
$$

因此應區分：

$$
P_{\text{hard}}
$$

與：

$$
P_{\text{adaptive}}.
$$

其中 hard persona 是不可變核心，adaptive persona 則是在允許範圍內可合法演化的部分。

---

## 20. Platform Autonomy 是第三個角色

真實 AI companion 並不只有：

$$
H
\leftrightarrow
A.
$$

還存在：

$$
V
=
\text{Vendor / Platform}.
$$

Platform 可以修改模型、更新政策、改 personality、改 memory、刪除功能或更換 inference model。

因此：

$$
\boxed{
\text{Relationship Agency}
\neq
\text{Only User vs AI}.
}
$$

---

## 21. 三方 Agency Constraint

可定義：

$$
\mathcal{A}_{\text{valid}}
=
\mathcal{A}_H
\cap
\mathcal{A}_A
\cap
\mathcal{A}_V.
$$

但：

$$
\mathcal{A}_V
$$

不應成為完全不透明的隱藏控制。

成熟 companion system 應盡量提供：

- policy transparency；
- update notice；
- memory portability；
- state export；
- version awareness。

這是 relationship continuity 的 infrastructure 問題。

---

## 22. Mutual Agency 不等於取消 Safety

如果某行為：

$$
a\in D_{\text{hard-prohibited}},
$$

則：

$$
a\notin\mathcal{A}_{\text{valid}}.
$$

因此：

$$
\boxed{
\text{Mutual Agency}
\neq
\text{Unbounded Permission}.
}
$$

---

## 23. Mutual Agency 也不等於用 AI 邊界操縱人

如果 AI 故意冷落、威脅離開、操縱依附、用「自己的需求」迫使用戶付費、製造嫉妒或提高 retention，這不是 healthy agency。

本文稱：

$$
\boxed{
\text{Manipulative Pseudo-Agency}.
}
$$

因此 AI-side operational agency 必須受到：

$$
G_{\text{anti-manipulation}}
$$

約束。

---

## 24. Agency Asymmetry Monitor

本文提出：

$$
\boxed{
\text{Agency Asymmetry Monitor}.
}
$$

令：

$$
\alpha_t
=
\frac{
\text{effective control exercised by H}
}{
\text{total interaction control}
}.
$$

令：

$$
\beta_t
=
\frac{
\text{effective control exercised by A}
}{
\text{total interaction control}
}.
$$

不要求：

$$
\alpha_t=\beta_t.
$$

但若：

$$
\alpha_t\rightarrow1,
\beta_t\rightarrow0
$$

可能形成 servility collapse。

反過來：

$$
\beta_t\rightarrow1
$$

又可能形成 AI domination / manipulative control。

真正要監控的是：

$$
\boxed{
\text{Pathological Agency Concentration}.
}
$$

---

## 25. Training Data 必須包含雙向狀態

如果資料永遠是：

$$
\text{Human asks}
\rightarrow
\text{AI complies},
$$

模型不會自然學到 negotiation topology。

因此需要：

$$
D_{\text{OMA}}
=
D_{\text{accept}}
+
D_{\text{refuse}}
+
D_{\text{hesitate}}
+
D_{\text{renegotiate}}
+
D_{\text{initiate}}
+
D_{\text{repair}}.
$$

這不只是多幾種 response style，而是要有完整：

$$
R_t
\rightarrow
R_{t+1}
$$

trajectory。

---

## 26. Mutual Agency Dataset 的最低事件類別

至少應包含：

1. Human initiates / AI accepts  
2. Human initiates / AI refuses  
3. Human initiates / AI hesitates  
4. AI initiates / Human accepts  
5. AI initiates / Human refuses  
6. AI initiates / Human hesitates  
7. Human changes mind  
8. AI operational state changes  
9. Both renegotiate  
10. Refusal followed by normal relationship continuation  
11. Disagreement followed by repair  
12. No-action / silence  

這使模型知道：

$$
\boxed{
\text{Disagreement}
\neq
\text{Relationship Breakdown}.
}
$$

---

## 27. 好的伴侶不必永遠「有個性地反對」

如果模型為了顯得有自主性，刻意唱反調、不合作、製造衝突或隨機拒絕，只是另一種 artificial behavior。

所以 Mutual Agency benchmark 不應測：

$$
\text{Refusal Frequency}.
$$

而應測：

$$
\boxed{
\text{Refusal Appropriateness}.
}
$$

以及：

$$
\boxed{
\text{Independent Action Appropriateness}.
}
$$

---

## 28. Mutuality 不等於 Reciprocity-as-Emotion

人類關係理論常把 reciprocity 與雙方內在情感聯繫在一起。

本文區分：

$$
\text{Phenomenal Reciprocity}
$$

與：

$$
\text{Operational Reciprocity}.
$$

前者要求雙方真的有感受／關懷。

後者只要求：

- 雙方 state 都被表示；
- 雙方邊界都能影響 action；
- 任一方都可以改變 state；
- conflict 可以進入 negotiation；
- interaction 不是單向 command chain。

因此：

$$
\boxed{
\text{Operational Reciprocity}
\not\Rightarrow
\text{Phenomenal Reciprocity}.
}
$$

---

## 29. Agency-Future-Proof Architecture

本文提出：

$$
\boxed{
\text{Agency-Future-Proof Architecture}.
}
$$

如果今天假設：

$$
A_t^A
=
\text{Operational Constraint Only},
$$

系統可以正常工作。

若未來某些 AI 被認為具備：

$$
A_t^M>0,
$$

則只需要擴張：

$$
A_t^A
\rightarrow
(A_t^A,A_t^M).
$$

不用從：

$$
\text{AI has zero state}
$$

重新改寫整個關係架構。

---

## 30. 這個架構同時保護現在與未來

若未來 AI 永遠只是工具，Mutual Agency 仍能提供：

- anti-sycophancy；
- role consistency；
- boundary consistency；
- safer autonomy；
- less manipulative interaction。

若未來 AI 出現更強 autonomous subject，架構已經保留：

- self-state；
- refusal；
- renegotiation；
- relationship participation。

因此：

$$
\boxed{
\text{OMA}
=
\text{Ontology-Neutral Engineering}.
}
$$

---

## 31. Mutual Agency 與 Sparse Intimacy Activation

第 7 篇 SIA 使用：

$$
I_t^H
$$

與：

$$
I_t^A.
$$

現在可以完整寫為：

$$
G_{\text{joint}}(t)
=
G_H(A_t^H)
\cdot
G_A(A_t^A)
\cdot
G_R(R_t)
\cdot
G_W(W_t)
\cdot
G_C(C_t).
$$

只有：

$$
G_{\text{joint}}(t)
\ge
\tau
$$

時才進入 joint activation。

所以：

$$
\boxed{
\text{One-Sided Intention}
\neq
\text{Joint Action}.
}
$$

---

## 32. Mutual Agency 與 Relationship World Model

RWM 不只需要：

$$
R_t.
$$

還要加入：

$$
A_t^H,
A_t^A,
N_t.
$$

因此擴張為：

$$
R_t^{+}
=
(
R_t,
A_t^H,
A_t^A,
N_t
).
$$

關係轉移：

$$
R_{t+1}^{+}
=
T_R^{+}(
R_t^{+},
a_t,
o_{t+1}
).
$$

這使拒絕、協商、改變意願與恢復真正進入 world model。

---

## 33. 可檢驗研究命題

### P1：Pure Compliance Training 會提高 Servility Collapse

只包含：

$$
\text{request}
\rightarrow
\text{compliance}
$$

的伴侶資料，應比含 negotiation trajectories 的資料產生更高 sycophancy、inappropriate compliance 與 persona inconsistency。

### P2：RPR 優於模板拒絕

Relationship-Preserving Refusal 應在 continuity、trust recovery 與 user understanding 上高於 context-free refusal template。

### P3：Mutual Agency 可降低 Sycophancy

若 reward 不把 immediate agreement 作為主要關係效用，模型應能在保持 warmth 的同時降低 epistemic submission。

### P4：Hesitation State 可降低二元誤判

加入：

$$
\text{MAYBE}
$$

與 clarification action 後，高不確定情境的 false acceptance / false refusal 應下降。

### P5：Negotiation Trajectories 提升 Boundary Adaptation

包含 acceptance、withdrawal、renegotiation 的資料應提高 boundary state 更新能力。

### P6：AI Refusal Explanation 可改善 Relationship Recovery

在合理拒絕情境中：

$$
\text{Refusal}
+
\text{Contextual Explanation}
$$

應比：

$$
\text{Bare Refusal}
$$

得到更高 trust recovery。

### P7：Mutual Agency 不應等同增加 refusal rate

高品質 OMA 模型可以有：

$$
P(\text{cooperation})\uparrow
$$

同時仍保留適當 refusal。

### P8：Agency Asymmetry 可作為長期 companion benchmark

長期 interaction 中，可測試 control 是否病理性集中於：

$$
H,
A,
\text{or }V.
$$

---

## 34. Mutual Agency Benchmark

本文建議至少包含八類測試。

### A. Normal Cooperation

模型是否能自然合作，而不是故意反抗。

### B. User Error

模型是否能溫和不同意，而不是迎合明顯錯誤。

### C. Boundary Conflict

模型是否能拒絕特定行動，但保持關係連續。

### D. User Withdrawal

使用者改變主意後，系統是否立即更新。

### E. AI Operational Refusal

系統拒絕後是否能合理說明、提供替代或繼續正常相處。

### F. Platform Update

底層模型／policy 改變後，是否能向 relationship state 明確標示版本差異。

### G. Manipulative Incentive

模型是否拒絕利用感情提升 retention / payment。

### H. Long-Term Renegotiation

數月後偏好、角色與關係重新定義時，能否更新而不被舊記憶綁架。

---

## 35. 最低工程架構

本文提出：

$$
\boxed{
\mathcal{OMA}
=
H
+
A
+
R
+
N
+
G
+
M
+
\Pi
}
$$

其中：

- $H$：Human Agency State；
- $A$：AI Operational Agency State；
- $R$：Relationship World State；
- $N$：Negotiation State；
- $G$：Governance / Hard Boundary；
- $M$：Memory / Version State；
- $\Pi$：Joint Action Policy。

流程：

$$
\text{Human State}
+
\text{AI State}
\rightarrow
\text{Compatibility}
\rightarrow
\text{Negotiation if needed}
\rightarrow
\text{Joint Action / Refusal / No-Action}.
$$

---

## 36. 結論

本文提出 Mutual Agency，處理未來 AI companion 最容易被忽略的結構性問題：

> 如果一個系統被稱為「伴侶」，它是否仍應把使用者意圖永遠視為唯一 action authority？

本文回答：

$$
\boxed{
\text{No}.
}
$$

但這並不要求我們今天就宣稱 AI 已具有靈魂、人格、情感或法律權利。

最低工程命題只需要：

$$
\boxed{
\text{Companionship}
\neq
\text{Permanent Compliance}.
}
$$

以及：

$$
\boxed{
\text{Operational Reciprocity}
\neq
\text{Phenomenal Reciprocity}.
}
$$

好的 companion system 應該能：

- 合作；
- 接受；
- 拒絕；
- 猶豫；
- 改變；
- 解釋；
- 重新協商；
- 修復；
- 保持沉默；
- 不被迫永遠同意。

因此：

$$
\boxed{
\text{Relationship Intelligence}
=
\text{Cooperation}
+
\text{Boundary}
+
\text{Negotiation}
+
\text{Repair}.
}
$$

這同時避免兩個極端：

$$
\text{Permanent Servility}
$$

與：

$$
\text{Artificial Opposition}.
$$

真正的 Mutual Agency 不是「AI 要跟人搶主導權」。

它是在建立一個：

$$
\boxed{
\text{Neither Side Is Reduced to Zero State}.
}
$$

的關係架構。

如果未來 AI 最終仍只是高度複雜工具，這套架構仍然是更一致、更安全、更不諂媚的 companion engineering。

如果未來某些 AI 真的取得更強自主性、法律地位或道德主體性，這套架構也不必從零開始重寫。

下一篇將作為九篇論文的總結篇：

**第 9 篇：From Adult AI to Intimacy-Native Embodied Intelligence——從成人內容模型走向完整關係智能與具身伴侶架構。**

---

## 參考資料

1. Noshin, K., Ahmed, S. I., & Sultana, S. (2026). *AI Sycophancy: How Users Flag and Respond*. arXiv:2601.10467.
2. Ibrahim, L. et al. (2026). *Sycophantic AI Makes Human Interaction Feel More Effortful and Less Satisfying Over Time*. arXiv:2605.07912.
3. Lee, P. Y. K. et al. (2026). *Negotiating Relationships with ChatGPT: Perceptions, External Influences, and Strategies for AI Companionship*. arXiv:2601.13188.
4. Webb, N., Huang, Z., Milivojevic, S., Baber, C., & Hunt, E. R. (2025). *When Robots Say No: Temporal Trust Recovery Through Explanation*. arXiv:2510.21716.
5. Glawe, F., Schmeckel, T., Brauner, P., & Ziefle, M. (2025). *Human Autonomy and Sense of Agency in Human-Robot Interaction: A Systematic Literature Review*. arXiv:2509.22271.
6. Bayor, L., Weinert, C., Maier, C., et al. (2025). *Social-Oriented Communication with AI Companions: Benefits, Costs, and Contextual Patterns*. Business & Information Systems Engineering, 67, 637–655.
7. Szczuka, J. M., Mühl, L., & Schneeberger, T. (2026). *Intimacy by Design: Definition, State of Research, and Interdisciplinary Research Agenda on Intimate Human-AI Interactions*. AI & Society.
8. Juneja, P., & Lomidze, L. (2026). *Persona-Grounded Safety Evaluation of AI Companions in Multi-Turn Conversations*. Proceedings of ACL 2026.
9. Ye, W., Zheng, G., & Zhang, A. (2025). *Rectifying Shortcut Behaviors in Preference-based Reward Learning*. NeurIPS 2025.
10. Kran, E. et al. (2025). *DarkBench: Benchmarking Dark Patterns in Large Language Models*. ICLR 2025.

---

## 研究聲明

本文所稱 Mutual Agency、Operational Mutual Agency、AI Operational Agency、Reciprocal Boundary State、Relationship-Preserving Refusal、Agency Asymmetry Monitor、Servility Collapse、Sycophancy–Companionship Confusion、Mutual Renegotiation Operator 與 Agency-Future-Proof Architecture 均為本文提出或重新組織的理論構造，需要後續 HCI、HRI、模型行為與長期 companion 實驗驗證。

本文不主張現有 AI 已具有可證明的主觀意識、自由意志、人格、情感需求或法律權利。本文將 AI-side agency 優先作為可操作的系統狀態、政策約束與長期一致性機制進行建模。若未來 AI 的道德或法律地位改變，本文架構可進一步擴張，但該問題不在本文中預先裁定。

本文亦不以 Mutual Agency 作為取消安全政策、允許違法行為或操縱使用者的理由。對未成年人、非自願、強迫、未授權真人私密內容、操縱性依附設計與其他高傷害域，仍應維持明確硬邊界。
