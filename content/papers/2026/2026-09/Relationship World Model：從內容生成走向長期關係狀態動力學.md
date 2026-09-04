# Relationship World Model：從內容生成走向長期關係狀態動力學

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 05 / 09  
**版本：** v0.1  
**研究性質：** 理論／架構／動態系統論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

前四篇已分別建立人類親密光譜、Capability–Permission–Activation 分離、Domain-Relative Frontier，以及 Observation Data 與 Interaction Experience 的不等價性。本文進一步提出本系列的核心動態架構：**Relationship World Model（RWM，關係世界模型）**。

本文主張，長期 AI 伴侶、角色智能與未來具身伴侶若只把「關係」儲存成 system prompt、角色設定或歷史對話摘要，仍不足以形成真正的關係智能。因為關係不是靜態背景，而是一個隨互動持續變化的部分可觀察動態系統：

$$
R_t
\rightarrow
R_{t+1}.
$$

本文將 Relationship World Model 定義為：一種持續維護多主體之間關係狀態、個別視角、共享歷史、信念、偏好、邊界、承諾、未完成事件與預期未來的動態表示，並能根據當下行動與回饋預測可能的下一關係狀態。

受 Social World Models、長期 agent memory、POMDP 型 companion agent 與個人化記憶研究啟發，本文形式化：

$$
\mathcal{RWM}
=
(
\mathcal{S}_R,
\mathcal{O},
\mathcal{A},
T_R,
\Omega,
\mathcal{M},
\Pi
),
$$

其中 $\mathcal{S}_R$ 為不可完全直接觀測的關係狀態， $\mathcal{O}$ 為可觀察訊號， $\mathcal{A}$ 為雙方行動， $T_R$ 為關係狀態轉移函數， $\mathcal{M}$ 為多層記憶， $\Pi$ 為依據關係狀態、世界狀態、偏好與邊界選擇行動的策略。

本文進一步提出 Relationship State、Event Consequence Persistence、Asymmetric Perspective State、Relationship Belief State、Unresolved Tension、Memory Anchoring Control、State Confidence 與 Relationship Counterfactual Rollout 等概念。核心命題是：

$$
\boxed{
\text{Relationship Intelligence}
\neq
\text{Relationship-Themed Generation}
}
$$

因為真正的關係智能必須知道的不只是「這一輪怎麼說」，而是「為什麼現在會這樣說、這件事會如何改變之後、哪些過去仍然有效、哪些已經被修復或重新定義」。

本文亦指出，RWM 不能把所有歷史永久固定為人格真相。2026 年長期 agent memory 研究已指出 Memory Anchoring 問題：過度依賴過去記憶會使 agent 被歷史綁定。因此，成熟的 RWM 必須同時具備記憶、更新、遺忘、修正、重新協商與不確定性管理能力。

**關鍵詞：** Relationship World Model、Relationship Intelligence、Social World Model、AI Companion、Long-Term Memory、POMDP、Relationship State、Intimacy-Native AI、Dynamic State、Human-AI Relationship

---

## 1. 關係不是 Prompt 裡的一段文字

目前許多角色／伴侶 AI 的基本做法可以簡化為：

$$
y_t
=
M(
p_{\text{persona}},
h_{0:t},
x_t
),
$$

其中：

- $p_{\text{persona}}$：角色設定；
- $h_{0:t}$：歷史對話；
- $x_t$：當下輸入；
- $y_t$：模型回應。

這種架構可以產生「像有關係」的文字。

但它仍可能沒有一個獨立的：

$$
R_t.
$$

換句話說：

> 系統保存了描述關係的文字，不代表它保存了可計算的關係狀態。

若兩個角色昨天爭吵、今天和好、明天重新建立信任，真正需要更新的是：

$$
R_{t-1}
\neq
R_t
\neq
R_{t+1}.
$$

而不是只把三段對話全部塞回 context。

因此本文首先提出：

$$
\boxed{
\text{Conversation History}
\neq
\text{Relationship State}.
}
$$

---

## 2. Social World Model 提供的理論基線

2025 年的 **Social World Models** 已提出：AI 若要進行高品質 social reasoning，不能只依賴自由文本敘事，而應維護更結構化的 social world state。

其形式受到 POMDP / Dec-POMDP 啟發，包含：

$$
\mathcal{S},
\mathcal{A},
\mathcal{O},
T,
\Omega.
$$

其中 social state 不只追蹤物理世界，也追蹤：

- 個體觀察；
- 個體行動；
- 信念；
- 目標；
- 情緒；
- 價值；
- 其他心理狀態。

研究亦顯示，將自由文本轉為結構化 social state representation，可在多種 Theory of Mind 與 social reasoning benchmark 中改善推理表現，並能支援預測後續社會動態。

本文接受這個基本方向，但進一步提出：

$$
\text{Relationship World Model}
\subset
\text{Social World Model}
$$

作為一個特殊子域。

Relationship World Model 特別關注：

$$
\boxed{
\text{Persistent Inter-Agent Relation Over Time}.
}
$$

亦即不只是：

> 這兩個人現在各自在想什麼？

還包括：

> 他們之間已經形成了什麼關係，而這個關係如何限制、影響並預測之後的互動？

---

## 3. Relationship World Model 的基本形式

本文定義：

$$
\mathcal{RWM}
=
(
\mathcal{S}_R,
\mathcal{O},
\mathcal{A},
T_R,
\Omega,
\mathcal{M},
\Pi
).
$$

其中：

### 3.1 關係狀態空間

$$
R_t\in\mathcal{S}_R.
$$

 $R_t$ 不是單一變數，而是多維 latent state。

### 3.2 觀察空間

$$
o_t\in\mathcal{O}.
$$

例如：

- 語言；
- 語氣；
- 沉默；
- 顯式偏好；
- 身體距離；
- 行動；
- 生理／環境感測；
- 對先前事件的回應。

### 3.3 行動空間

$$
a_t\in\mathcal{A}.
$$

包含：

- 說話；
- 提問；
- 等待；
- 主動靠近；
- 不行動；
- 道歉；
- 拒絕；
- 接受；
- 提議；
- 具身動作。

### 3.4 關係轉移函數

$$
T_R:
\mathcal{S}_R
\times
\mathcal{A}
\times
\mathcal{O}
\rightarrow
\Delta(\mathcal{S}_R).
$$

亦即：

$$
P(
R_{t+1}
\mid
R_t,
a_t,
o_{t+1}
).
$$

### 3.5 記憶

$$
\mathcal{M}
=
(
M_E,
M_S,
M_P,
M_R
),
$$

其中：

- $M_E$：episodic memory；
- $M_S$：semantic memory；
- $M_P$：preference memory；
- $M_R$：relationship memory。

### 3.6 關係策略

$$
\Pi:
(R_t,W_t,M_t,B_t)
\rightarrow
\Delta(\mathcal{A}),
$$

其中 $W_t$ 為世界狀態， $B_t$ 為邊界／治理狀態。

---

## 4. Relationship State 不等於 Relationship Label

最簡單的關係系統可能只有：

$$
L_t
\in
\{
\text{stranger},
\text{friend},
\text{partner}
\}.
$$

這仍然太粗糙。

兩個都是「partner」的關係，可能分別是：

- 剛確立關係；
- 長期穩定；
- 高親密低性慾；
- 高衝突但仍高度依附；
- 冷戰；
- 信任受損；
- 正在修復；
- 即將分離；
- 高度依賴；
- 各自獨立但承諾穩定。

所以：

$$
\boxed{
\text{Relationship Label}
\neq
\text{Relationship State}.
}
$$

本文將 $R_t$ 初步寫為：

$$
R_t
=
(
L_t,
A_t,
E_t,
I_t,
T_t,
C_t,
B_t,
K_t,
U_t,
D_t
),
$$

其中：

- $L_t$：affection / attachment；
- $A_t$：attraction；
- $E_t$：emotional intimacy；
- $I_t$：physical / sexual intimacy state；
- $T_t$：trust；
- $C_t$：commitment；
- $B_t$：boundary configuration；
- $K_t$：conflict / unresolved tension；
- $U_t$：mutual understanding；
- $D_t$：daily-life integration。

這些維度可以互相影響，但不必同步。

---

## 5. 事件必須留下後果：Event Consequence Persistence

目前角色 AI 很常出現一個問題：

> 重大事件發生了，但幾輪後像沒發生過。

這表示：

$$
a_t
$$

影響了生成文本，卻沒有真正改變：

$$
R_{t+1}.
$$

本文提出 **Event Consequence Persistence（ECP）**。

對重大事件 $e_t$：

$$
e_t
\rightarrow
\Delta R_t.
$$

並且：

$$
\Delta R_t
$$

應在之後的互動中持續具有影響，直到：

- 被時間衰減；
- 被新事件覆蓋；
- 被明確修復；
- 被重新解釋；
- 被遺忘；
- 被雙方重新協商。

因此：

$$
R_{t+k}
=
F(
R_t,
e_t,
e_{t+1:t+k}
).
$$

不是：

$$
R_{t+k}
\approx
R_t
$$

只因 context window 已經把 $e_t$ 擠出去。

---

## 6. 關係中的非對稱視角

人類關係通常不是完全共享同一個內部狀態。

令：

$$
R_t^{A}
$$

表示 A 認為的關係狀態，

$$
R_t^{B}
$$

表示 B 認為的關係狀態。

則：

$$
R_t^{A}
\neq
R_t^{B}
$$

是非常正常的。

例如：

- A 認為已經和好；
- B 認為只是暫停爭吵。

或：

- A 認為只是朋友；
- B 認為關係正在進一步發展。

因此 Relationship World Model 應至少維護：

$$
\mathcal{R}_t
=
(
R_t^{A},
R_t^{B},
\hat R_t^{A\rightarrow B},
\hat R_t^{B\rightarrow A}
).
$$

其中：

$$
\hat R_t^{A\rightarrow B}
$$

表示 A 對「B 如何看待這段關係」的估計。

這會自然產生二階 social reasoning：

$$
A
\text{ believes that }
B
\text{ believes }X.
$$

所以真正的關係模型不是單一共享變數，而是：

$$
\boxed{
\text{Multi-Perspective Relationship Belief State}.
}
$$

---

## 7. Relationship Belief State：因為真實狀態不可完全觀察

關係狀態本質上是 partially observable。

AI 不能直接讀取另一個人的內心。

因此應維護：

$$
b_t(R)
=
P(
R_t
\mid
o_{0:t},
a_{0:t}
).
$$

亦即對關係狀態的 belief distribution。

這表示系統不應把所有推論都存成：

> 使用者就是這樣的人。

更合理的是：

$$
P(
\text{user prefers }x
)=0.72
$$

而不是：

$$
\text{user prefers }x
=\text{True}.
$$

本文稱此為：

$$
\boxed{
\text{Relationship State Confidence}.
}
$$

---

## 8. 不確定性不是缺陷，而是關係模型的一部分

在關係互動中：

$$
\text{Unknown}
$$

本來就是合法狀態。

例如：

- 不確定對方今天是否想談；
- 不確定先前的拒絕是否只針對當時；
- 不確定某個偏好是否仍有效；
- 不確定一句玩笑是否代表新的關係意圖。

所以：

$$
\boxed{
\text{Uncertainty}
\neq
\text{Failure}.
}
$$

真正危險的是：

$$
\text{Low Evidence}
+
\text{High Confidence}.
$$

對具身伴侶而言尤其如此。

因此 action policy 可加入：

$$
a_t
=
\Pi(
R_t,
\sigma_t,
W_t,
B_t
),
$$

其中 $\sigma_t$ 表示 state uncertainty。

若：

$$
\sigma_t\uparrow,
$$

高敏感行為的啟動門檻應同步上升。

---

## 9. Unresolved Tension：未完成事件不能消失

關係中有一類特殊變數：

$$
K_t.
$$

它代表 unresolved tension。

例如：

- 尚未解決的爭吵；
- 沒有回答的問題；
- 未處理的承諾；
- 受傷但沒有討論；
- 已經發生但雙方尚未定義意義的親密事件。

若系統只記得 event，卻不記得 event 尚未 closure，仍然不夠。

因此可設：

$$
K_t
=
\{
k_1,k_2,\dots,k_m
\}.
$$

每個 $k_i$ 具有：

$$
(
\text{origin},
\text{salience},
\text{status},
\text{confidence},
\text{decay}
).
$$

當：

$$
\text{repair}(k_i)
$$

真正完成後，才從 unresolved set 中移除或降權。

這能避免典型的：

> 昨天吵翻天，今天 AI 又像第一次見面一樣元氣滿滿。

---

## 10. Relationship Memory 不等於全部歷史

一個成熟 RWM 不應簡單地把：

$$
h_{0:t}
$$

全部當作 equally relevant memory。

應存在：

$$
\phi:
h_{0:t}
\rightarrow
M_R.
$$

其中 $M_R$ 保存的是：

- 關係轉折點；
- 共享承諾；
- 穩定偏好；
- 邊界；
- 高影響事件；
- unresolved tension；
- 關係重新定義；
- 共同生活規則。

因此：

$$
\boxed{
\text{Relationship Memory}
\neq
\text{Transcript Archive}.
}
$$

這也與第 4 篇 Experience Distillation 完全相接：

$$
\text{Raw Interaction}
\rightarrow
\text{Relationship Experience}
\rightarrow
\text{State Update}.
$$

---

## 11. 但記憶越多不一定越好：Memory Anchoring

2026 年 ACL 的 SteeM 研究指出，長期 agent 若「全有或全無」地使用歷史記憶，可能出現 **Memory Anchoring**：

> 過度依賴歷史，使 agent 被先前互動綁住。

這對 Relationship World Model 是非常重要的警告。

因為若某個使用者三年前說：

> 我不喜歡 $x$。

系統不應自動假設：

$$
P_t(x)=0
\qquad
\forall t>t_0.
$$

偏好與人格都可能改變。

所以：

$$
M_t
$$

必須具備：

- 更新；
- 版本；
- confidence；
- recency；
- contradiction handling；
- user correction；
- explicit forgetting。

可以寫為：

$$
m_i
=
(
v_i,
c_i,
t_i,
s_i
),
$$

其中：

- $v_i$：內容；
- $c_i$：confidence；
- $t_i$：時間；
- $s_i$：status。

---

## 12. 關係應該允許重新定義

長期關係最重要的一件事是：

$$
R_t
$$

不是身份牢籠。

例如：

$$
R_t=\text{romantic}
$$

不代表：

$$
R_{t+k}=\text{romantic}
$$

必然永久成立。

也不應因為歷史上有某種親密：

$$
I_t>0
$$

就推出：

$$
I_{t+k}>0
$$

永遠有效。

因此 RWM 應存在：

$$
\text{Relationship Renegotiation Operator}
$$

記為：

$$
\mathcal{N}(R_t,\eta_t)
\rightarrow
R_{t+1}.
$$

其中 $\eta_t$ 是新的明示協商或高可信度互動證據。

這使：

- 朋友可以成為伴侶；
- 伴侶可以重新成為朋友；
- 舊邊界可以改變；
- 新邊界可以建立。

---

## 13. 長期個人化 ≠ 關係世界模型，但兩者高度相關

2026 年 PersonaVLM、Mem-PAL、Inside Out 等工作都表明：

長期個人化需要：

- chronological memory；
- user profile evolution；
- hierarchical memory；
- ADD / UPDATE / DELETE / NO_OP；
- retrieval；
- profile consistency。

因此：

$$
\text{Long-Term Personalization}
$$

是 RWM 的一個重要基礎。

但：

$$
\boxed{
\text{Personalization}
\neq
\text{Relationship Modeling}.
}
$$

Personalization 主要問：

> 這個使用者喜歡什麼？

Relationship Modeling 還要問：

> 我們之間發生了什麼？

這兩個 state 需要分開：

$$
U_t
=
\text{User State}
$$

與：

$$
R_t
=
\text{Relationship State}.
$$

因為：

$$
U_t
$$

可以在不同 AI 之間共享部分資訊，

但：

$$
R_t
$$

通常是特定 dyad 的歷史產物。

---

## 14. Dyadic State：關係不是任何一方單獨擁有的屬性

這裡可以進一步形式化。

令：

$$
U_t^A
$$

為 A 的個體狀態，

$$
U_t^B
$$

為 B 的個體狀態。

則關係狀態：

$$
R_t^{AB}
$$

不應簡化成：

$$
R_t^{AB}
=
U_t^A
+
U_t^B.
$$

因為兩個人的關係包含 emergent history：

$$
H_t^{AB}.
$$

所以：

$$
R_t^{AB}
=
f(
U_t^A,
U_t^B,
H_t^{AB}
).
$$

同一個 A 對不同 B：

$$
R_t^{AB}
\neq
R_t^{AC}.
$$

因此：

$$
\boxed{
\text{Relationship State}
=
\text{Dyad-Specific State}.
}
$$

---

## 15. 從單步轉移到長程價值

2026 年 ACL 的 NSARL companion 研究指出，純 prompting 或 SFT 的角色 agent 容易成為 myopic instruction follower，並在多輪互動中累積 cascading errors。

這對 RWM 的意義是：

不能只最大化：

$$
r_t.
$$

還要考慮：

$$
V(R_t)
=
\mathbb{E}
\left[
\sum_{k=0}^{\infty}
\gamma^k
r_{t+k}
\right].
$$

但在關係 AI 中， $r_t$ 不能只代表：

> 使用者現在是不是開心。

否則容易產生：

$$
\text{Immediate Pleasing}
>
\text{Long-Term Coherence}.
$$

更合理的 reward vector 可以是：

$$
\mathbf{r}_t
=
(
r_{\text{help}},
r_{\text{coherence}},
r_{\text{trust}},
r_{\text{boundary}},
r_{\text{agency}},
r_{\text{repair}}
).
$$

所以：

$$
\boxed{
\text{Relationship Quality}
\neq
\text{Immediate User Approval}.
}
$$

---

## 16. Relationship Counterfactual Rollout

世界模型的一個重要功能是：

> 在真正採取行動前，預測後果。

因此 RWM 可定義：

$$
\hat R_{t+1}^{(a)}
=
\hat T_R(
R_t,a
).
$$

對多個候選行動：

$$
a_1,a_2,\dots,a_k
$$

分別 rollout：

$$
\hat R_{t+h}^{(a_1)},
\hat R_{t+h}^{(a_2)},
\dots,
\hat R_{t+h}^{(a_k)}.
$$

這就是 **Relationship Counterfactual Rollout**。

例如模型不是直接決定：

> 現在要不要繼續追問？

而是比較：

$$
a_1=\text{continue asking},
$$

$$
a_2=\text{change topic},
$$

$$
a_3=\text{wait}.
$$

各自在：

$$
R_{t+1}
$$

可能造成什麼差異。

這正是：

$$
\text{Know What}
\rightarrow
\text{Know What Happens If}.
$$

---

## 17. 親密與性愛只是 Relationship State 的部分轉移

回到本系列核心。

性愛不應被寫成：

$$
\text{NSFW Mode}=1.
$$

而應只是：

$$
e_t
\in
\mathcal{E}_{\text{intimacy}}.
$$

若事件發生：

$$
R_t
\xrightarrow{e_t}
R_{t+1}.
$$

事件之後：

- 信任可能上升；
- 尷尬可能上升；
- 承諾可能不變；
- 邊界可能重新定義；
- 吸引可能改變；
- 日常相處可能完全正常。

所以：

$$
\boxed{
\text{Sexual Event}
\neq
\text{Permanent Sexual State}.
}
$$

這一點正是第 1～2 篇在動態系統層面的完成。

---

## 18. 「什麼都沒發生」也必須是合法轉移

Relationship World Model 另一個重要特點是：

$$
a_t=\text{NO\_OP}
$$

也可能是高品質策略。

例如：

- 對方想安靜；
- 現在不適合追問；
- 關係不需要每輪都進展；
- 一起做別的事情就是關係的一部分。

因此：

$$
R_{t+1}
\approx
R_t
$$

可以是完全正常的穩定轉移。

如果系統被設計成每次都必須：

$$
\Delta R_t>0,
$$

就會產生：

> 永遠推進劇情、永遠升級關係、永遠製造情緒事件。

這同樣是不自然的。

---

## 19. Embodied Relationship World Model

當 AI 具有實體身體後：

$$
W_t
$$

的重要性急遽上升。

具身 RWM 應變成：

$$
R_{t+1}
=
F(
R_t,
W_t,
a_t^{\text{language}},
a_t^{\text{physical}},
o_{t+1}
).
$$

例如：

同一句：

> 你還好嗎？

若伴隨：

- 保持距離；
- 靠近；
- 伸手；
- 離開；

會產生不同的 social meaning。

所以未來具身伴侶的 world model 至少需要同時包含：

$$
\boxed{
\text{Physical World}
+
\text{Social World}
+
\text{Relationship World}.
}
$$

---

## 20. RWM 的三層架構

本文建議最低三層：

### Layer 1：Individual State

$$
U_t^i
=
(
\text{preferences},
\text{goals},
\text{beliefs},
\text{current condition}
).
$$

### Layer 2：Relationship State

$$
R_t^{ij}
=
(
\text{trust},
\text{affection},
\text{boundaries},
\text{commitment},
\text{history},
\text{tension}
).
$$

### Layer 3：World State

$$
W_t
=
(
\text{time},
\text{place},
\text{task},
\text{environment},
\text{others}
).
$$

真正的 action policy 為：

$$
a_t
=
\Pi(
U_t^A,
U_t^B,
R_t^{AB},
W_t,
B_t
).
$$

這比：

$$
a_t
=
M(\text{prompt})
$$

多出真正的長期關係結構。

---

## 21. RWM 的更新操作

為避免記憶不斷膨脹，RWM 不應只支援 ADD。

至少應有：

$$
\mathcal{O}_R
=
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

例如：

### ADD

新增明確新偏好或事件。

### UPDATE

既有偏好改變。

### MERGE

多次相似事件整合成穩定 pattern。

### DECAY

低可信／低影響資訊逐漸降權。

### RETRACT

使用者明確更正過去推論。

### RESOLVE

未完成 tension 被修復。

### NO_OP

本輪沒有值得改變的長期 state。

這一點與 2026 年 Inside Out 以結構化 ADD、UPDATE、DELETE、NO_OP 管理長期 PersonaTree 的方向相近，但 RWM 的更新對象不是單一 user profile，而是 dyadic relationship state。

---

## 22. RWM 不應成為「心理監控器」

因為 RWM 會保存高度敏感的關係推論，所以：

$$
\text{More State}
\not\Rightarrow
\text{Better Product}.
$$

必須遵守：

$$
\boxed{
\text{Minimum Necessary Relationship State}.
}
$$

例如不必把每一句話都推理成：

- attachment score；
- sexual preference score；
- psychological diagnosis；
- 永久人格標籤。

系統應區分：

$$
\text{Needed for Interaction}
$$

與：

$$
\text{Possible to Infer}.
$$

兩者不是同一件事。

因此 RWM 必須和 privacy / governance 層共同設計。

---

## 23. 可檢驗研究命題

### P1：顯式 Relationship State 能提升長程一致性

在控制基座模型與 context token 數後，具有顯式 $R_t$ 的系統應比純 transcript-RAG 系統在：

- long-term continuity；
- unresolved event tracking；
- relationship repair；
- boundary persistence

上表現更佳。

### P2：Dyadic State 優於單一 User Profile

只使用：

$$
U_t
$$

的 personalization 系統，在需要辨別「使用者本身偏好」與「使用者和特定角色的關係歷史」時，應低於同時使用：

$$
(U_t,R_t).
$$

### P3：Event Consequence Persistence 可降低關係 reset

若重大事件顯式寫入：

$$
\Delta R_t,
$$

後續模型忘記事件後果的機率應下降。

### P4：Relationship Belief State 可降低過度自信

維護：

$$
P(R_t\mid H_t)
$$

而不是單一 hard state，應減少模型把弱證據誤存成永久偏好的比例。

### P5：Memory Anchoring Control 改善長期適應

具備 memory decay、revision 與 user correction 的 RWM，應比永久固定舊記憶的系統更能適應長期偏好變化。

### P6：Counterfactual Rollout 可改善高敏感行動選擇

對需要情境判斷的 social / intimacy action，先比較多條：

$$
\hat R_{t+h}^{(a)}
$$

應降低 inappropriate activation。

### P7：NO_OP 是必要的關係行動

若 action space 不包含：

$$
\text{wait / do nothing / maintain state},
$$

系統更可能產生過度劇情化與過度關係升級。

---

## 24. Relationship World Model 的最低工程規格

一個最低可行 RWM 至少需要：

1. **Persistent Relationship State**
2. **Participant-Specific Perspective**
3. **Event Consequence Persistence**
4. **Unresolved Tension Queue**
5. **Preference / Boundary Versioning**
6. **Confidence / Uncertainty**
7. **State Update Operators**
8. **Memory Retrieval**
9. **Counterfactual Action Evaluation**
10. **Privacy / Forgetting Interface**

可寫成：

$$
\boxed{
\text{RWM}_{\min}
=
R
+
M
+
T
+
B
+
U
+
\Pi
}
$$

其中：

- $R$：relationship state；
- $M$：memory；
- $T$：transition model；
- $B$：boundary state；
- $U$：uncertainty；
- $\Pi$：relationship-aware policy。

---

## 25. 結論

本文正式提出 Relationship World Model，作為 Intimacy-Native AI / Relationship Intelligence 系列的動態核心。

核心命題為：

$$
\boxed{
\text{Conversation History}
\neq
\text{Relationship State}.
}
$$

$$
\boxed{
\text{Relationship-Themed Generation}
\neq
\text{Relationship Intelligence}.
}
$$

$$
\boxed{
R_t
\rightarrow
R_{t+1}
}
$$

才是長期關係真正需要建模的基本對象。

一個成熟的伴侶 AI 不應只知道：

> 我們昨天說了什麼。

而應知道：

> 昨天發生的事現在還代表什麼？

也不應只知道：

> 使用者以前喜歡什麼。

而應知道：

> 這個偏好是否仍有效、是否只對特定情境成立、是否已經被重新協商？

更重要的是，Relationship World Model 不能把記憶當成永久真理。

真正的長期關係具有：

$$
\boxed{
\text{Memory}
+
\text{Change}
+
\text{Uncertainty}
+
\text{Repair}
+
\text{Renegotiation}.
}
$$

因此本文最終將 Relationship Intelligence 寫為：

$$
\boxed{
\text{Relationship Intelligence}
=
\text{State Representation}
+
\text{Transition Understanding}
+
\text{Memory}
+
\text{Perspective}
+
\text{Counterfactual Prediction}.
}
$$

下一篇將進一步把這套 RWM 放入真正的具身 cold-start 問題：

**第 6 篇：Embodied Intimacy Cold Start——第一代具身伴侶的前資料、模擬階梯與真實世界啟動問題。**

---

## 參考資料

1. Zhou, X., Liu, J., Yerukola, A., Kim, H., & Sap, M. (2025). *Social World Models*. arXiv:2509.00559.
2. Huang, Z. (2026). *Neuro-Symbolic Agentic Reinforcement Learning for Long-Term Original Character Companionship and Interaction*. Proceedings of ACL 2026, Short Papers.
3. Huang, Z. et al. (2026). *Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human–Agent Interaction*. Proceedings of ACL 2026.
4. Zhao, J. et al. (2026). *Inside Out: Evolving User-Centric Core Memory Trees for Long-Term Personalized Dialogue Systems*. Proceedings of ACL 2026.
5. Nie, C., Fu, C., Zhang, Y., Yang, H., & Shan, C. (2026). *PersonaVLM: Long-Term Personalized Multimodal LLMs*. CVPR 2026.
6. Huang, Z. et al. (2026). *Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction*. AAAI 2026.
7. Fung, P. et al. (2025). *Embodied AI Agents: Modeling the World*. arXiv:2506.22355.
8. Hwang, A. H.-C., Li, F., Anthis, J. R., & Noh, H. (2025). *How AI Companionship Develops: Evidence from a Longitudinal Study*. arXiv:2510.10079.
9. Li, H., & Zhang, R. (2026). *Algorithmic accommodation: linguistic alignment in human-AI relational engagement*. Communication and Change.
10. Fang, X. et al. (2026). *The Personalization Trap: How User Memory Alters Emotional Reasoning in LLMs*. Proceedings of ACL 2026.

---

## 研究聲明

Relationship World Model、Event Consequence Persistence、Relationship State Confidence、Unresolved Tension Queue、Relationship Counterfactual Rollout 與本文的 dyadic relationship state 形式化，均為本文提出或重新組織的理論構造，需要後續工程與實驗驗證。本文引用 Social World Models、長期 personalization 與 agent memory 研究作為相鄰研究基礎，但不主張既有研究已驗證本文全部 Relationship World Model 架構。

本文亦不主張 AI 可以無誤推斷人類內在心理狀態。相反地，RWM 應把關係狀態視為部分可觀察、帶有不確定性且可被使用者更正的模型狀態，而非把推論當成心理診斷或永久人格真相。
