# T 怎麼變成 T？
## 身份生成、分類、承認與 Become-T 動力學

**英文題名：** *How Does T Become T? Identity Generation, Classification, Recognition, and the Dynamics of Become-T*  
**系列：**《T 的九問：符號身份、生成、命名與持續》Paper 04  
**版本：** v0.1 理論草稿  
**日期：** 2026-08-12  
**作者：** Neo.K、Aletheia（AI 協作）  
**機構：** EveMissLab／一言諾科技有限公司

---

## 摘要

Paper 01 將「T 是 T／T 不是 T」拆解為多重身份關係；Paper 02 將「T 是不是 T？」形式化為身份查詢與判定；Paper 03 則追問「T 為什麼是 T？」並區分構成性身份根據與證據性身份根據。

本文進一步處理一個不同問題：

> **一個原本尚未是 T 的存在，究竟如何取得 T 的身份？**

本文主張：

\[
\boxed{
\text{Being T}
\neq
\text{Becoming T}
}
\]

而：

\[
\boxed{
\text{Being Classified as T}
\neq
\text{Becoming T}
}
\]

也不必然成立。

一個存在 \(x\) 進入 \(T\)-身份域至少可能經由六條不同路徑：

1. **Discovery**：\(x\) 早已滿足 T 的構成條件，只是後來才被辨識；
2. **Transformation**：\(x\) 的內部狀態發生改變，因而首次滿足 T 條件；
3. **Relational Acquisition**：\(x\) 因進入新的關係網路而取得 T 身份；
4. **Institutional Conferment**：在合法規則與權威下，某個制度事件使 \(x\) 取得新的制度身份；
5. **Emergent Acquisition**：T 身份在系統演化中逐漸形成，而不存在單一瞬間的局部原因；
6. **Criterion Shift / Reclassification**：\(x\) 沒有改變，但 T 的判準、語境或分類體系發生改變。

因此，「T 怎麼變成 T？」不能只寫成：

\[
x\rightarrow T.
\]

更完整的形式為：

\[
\boxed{
\operatorname{BecomeT}_{\alpha}
(
x,
\Gamma,
c,
t,
E
)
}
\]

其中：

- \(\alpha\)：身份關係；
- \(\Gamma\)：身份生成機制；
- \(c\)：語境／制度；
- \(t\)：時間；
- \(E\)：事件與證據。

本文定義 Identity Acquisition Event（IAE）、Identity Transition Path（ITP）、Admission Gate、Recognition Gate 與 Stabilization Condition，並提出：

\[
\boxed{
\text{Identity Acquisition}
=
\text{Preconditions}
+
\text{Transition}
+
\text{Admission}
+
\text{Stabilization}
}
\]

但上述四者在不同身份類型中可以採不同形式。

本文最終提出一個重要區分：

\[
\boxed{
\Delta Object
\neq
\Delta Criterion
\neq
\Delta Relation
\neq
\Delta Institution
\neq
\Delta Recognition.
}
\]

只觀察到「昨天不是 T，今天是 T」，還不足以知道 **到底是誰變了**：對象、關係、制度、分類規則，還是我們自己的知識。

---

## 關鍵詞

身份生成、Become-T、Identity Acquisition、分類、制度身份、承認、社會本體論、身份轉換、分類回饋、身份穩定

---

# 0. 研究邊界

本文不主張：

1. 所有身份都是社會建構；
2. 所有身份都是被語言「說出來」才存在；
3. 分類者可以任意創造任何自然性質；
4. 只要叫一個東西 T，它就真的成為 T；
5. 所有身份取得都有明確單一時間點；
6. 所有身份取得都需要人類認可；
7. 內部狀態變化是所有身份生成的必要條件；
8. 制度身份與自然種類身份具有完全相同的生成機制；
9. 本文已解決所有社會身份、人格身份或法律身份問題。

本文研究的是：

> **當身份狀態從「尚未被判定為 T」變成「被合法判定為 T」時，系統應如何區分對象改變、關係改變、制度授予、分類改變與單純知識更新？**

---

# 1. Be-T 與 Become-T

定義：

\[
\operatorname{Be}_{\alpha}(x,T,c,t)
\]

表示在身份關係 \(\alpha\)、語境 \(c\)、時間 \(t\) 下，\(x\) 是 T。

而：

\[
\boxed{
\operatorname{Become}_{\alpha}
(
x,T,c,[t_0,t_1]
)
}
\]

表示：

\[
\neg \operatorname{Be}_{\alpha}(x,T,c,t_0)
\]

且：

\[
\operatorname{Be}_{\alpha}(x,T,c,t_1),
\qquad
t_1>t_0.
\]

因此：

\[
\boxed{
\operatorname{BecomeT}
}
\]

是一個 transition claim，而不是 static classification。

---

# 2. 最低階的 Become-T

最簡單情況是內部狀態改變。

令：

\[
x_{t+1}
=
F(x_t).
\]

而 T 的構成條件為：

\[
C_T(x).
\]

若：

\[
C_T(x_t)=0
\]

但：

\[
C_T(x_{t+1})=1,
\]

則：

\[
\boxed{
x_t
\xrightarrow{F}
x_{t+1}
\in T.
}
\]

這稱為：

# Transformational Become-T

例如某種程式完成必要初始化後首次進入 Ready state。

此時：

\[
\Delta x
\]

是身份取得的主要原因。

---

# 3. 但「今天被發現是 T」不等於今天才成為 T

考慮：

\[
C_T(x)=1
\]

其實從 \(t_0\) 就成立。

但觀察者在：

\[
t_1>t_0
\]

才取得證據。

因此：

\[
J_A(x,T,t_0)
=
\mathrm{Unknown},
\]

直到：

\[
J_A(x,T,t_1)
=
\mathrm{Same}.
\]

這裡改變的是：

\[
\Delta E_A
\]

而不是：

\[
\Delta x.
\]

所以：

\[
\boxed{
\text{Discovery of T}
\neq
\text{Becoming T}.
}
\]

本文稱此為：

# Recognition Without Acquisition

---

# 4. 分類不必創造被分類對象

如果研究者觀察到某動物並將其分類進 T 類：

\[
\operatorname{Classify}_A(x)=T,
\]

此分類本身通常不會立刻改變動物的物理結構。

所以：

\[
\boxed{
\operatorname{Classification}(x,T)
\not\Rightarrow
\operatorname{Constitution}(x,T).
}
\]

成熟身份系統必須問：

> 這個分類是在發現 T，還是在創造 T？

這兩者不能混用。

---

# 5. Identity Acquisition Event

本文定義：

\[
\boxed{
IAE_\alpha
=
(
x,
T,
t,
\Gamma,
c,
A,
P,
E
)
}
\]

為 Identity Acquisition Event。

其中：

- \(x\)：取得身份的對象；
- \(T\)：目標身份；
- \(t\)：身份取得時間或區間；
- \(\Gamma\)：取得機制；
- \(c\)：語境／制度；
- \(A\)：參與判定或授予的主體；
- \(P\)：provenance；
- \(E\)：證據。

---

# 6. Become-T 的六條基本路徑

本文暫定：

\[
\boxed{
\Gamma
\in
\{
D,
X,
R,
I,
M,
C
\}
}
\]

其中：

- \(D\)：Discovery；
- \(X\)：Transformation；
- \(R\)：Relational Acquisition；
- \(I\)：Institutional Conferment；
- \(M\)：Emergent / Maturation；
- \(C\)：Criterion Shift。

這六條路徑不必互斥。

一個身份取得事件可能同時包含多種機制。

---

# 7. Discovery：其實早就是 T

若：

\[
C_T(x,t_0)=1,
\]

但：

\[
J_A(x,T,t_0)=\mathrm{Unknown},
\]

之後：

\[
E_{t_1}
\]

增加，使：

\[
J_A(x,T,t_1)=\mathrm{Same},
\]

則：

\[
\boxed{
\Delta J_A
\neq
\Delta Identity.
}
\]

這稱為：

# Epistemic Acquisition Only

也就是身份在系統知識層首次取得，而不表示對象本體首次取得。

---

# 8. Transformation：對象真的改了

若：

\[
x_t
\notin T
\]

經：

\[
F_T
\]

變成：

\[
x_{t+1}\in T,
\]

則：

\[
\boxed{
\Delta Object
\rightarrow
\Delta Identity.
}
\]

例如：

\[
\mathrm{UncompiledSource}
\rightarrow
\mathrm{ExecutableArtifact}.
\]

兩者可能歷史相關，但在 executable identity 下，後者首次取得新身份。

---

# 9. Relational Acquisition：對象未必改變，關係改變了

某些身份取決於：

\[
R(x,y).
\]

若：

\[
\neg R(x,y)
\]

時：

\[
x\notin T_R,
\]

但：

\[
R(x,y)
\]

建立後：

\[
x\in T_R,
\]

則：

\[
\boxed{
\Delta Relation
\rightarrow
\Delta Identity.
}
\]

這種身份不是純粹 intrinsic property。

例如：

- parent；
- owner；
- member；
- predecessor；
- successor；
- authorized agent。

此時：

\[
x_t=x_{t+1}
\]

在許多物理狀態上可以完全相同，但 relational identity 已經改變。

---

# 10. Institutional Conferment：制度可以使某些身份成立

社會本體論研究 money、law、corporations、institutions、language 等對象，並長期討論規則、共同接受與制度實踐如何構成某些 social status。

本文將制度身份寫成：

\[
\boxed{
X
\xRightarrow[c]{R_I}
T_I
}
\]

其中：

- \(X\)：底層對象；
- \(R_I\)：制度規則；
- \(c\)：制度語境；
- \(T_I\)：制度身份。

例如某一 physical token 是否是有效票券，不能只從紙張分子結構決定。

所以：

\[
\boxed{
\text{Institutional Identity}
}
\]

可能需要合法規則與承認網路才能成立。

---

# 11. Constitutive Rule 與身份取得

對某些制度身份，可以寫：

\[
\boxed{
X
\text{ counts as }
T
\text{ in context }
C.
}
\]

但本文不將這個形式擴張成所有身份的普遍定律。

自然種類、數學物件、程式狀態與制度身份可能有完全不同的 grounding。

所以：

\[
\boxed{
\text{Institutional Become-T}
\neq
\text{Universal Become-T}.
}
\]

---

# 12. Speech Act 與身份取得

語用學與 speech-act 傳統指出，某些合適語境中的言語行動不只是描述世界，也可以參與做成一項社會行動；Austin 的經典例子包括婚姻儀式、命名船隻、遺贈與下注。

本文將此抽象為：

\[
\boxed{
S_A
+
Authority(A)
+
Felicity(c)
+
Rule(c)
\rightarrow
\Delta Identity.
}
\]

注意：

\[
S_A
\]

本身不足。

若沒有：

- legitimate authority；
- correct procedure；
- required context；
- applicable rule；

則同一句話可能什麼身份都不改變。

---

# 13. Performative Identity Acquisition

定義：

\[
\boxed{
PIA
=
(
SpeechAct,
Authority,
Rule,
Context,
Acceptance
)
}
\]

若：

\[
\operatorname{Valid}(PIA)=1,
\]

才可能：

\[
x
\rightarrow
T_{\mathrm{institutional}}.
\]

因此：

\[
\boxed{
\text{Saying T}
\not\Rightarrow
\text{Making T}
}
\]

而：

\[
\boxed{
\text{Valid Institutional Act}
\Rightarrow
\text{Possible Institutional Become-T}.
}
\]

---

# 14. Emergent Become-T

並非所有身份取得都有一個清楚瞬間。

令：

\[
x(t)
\]

持續變化。

而身份指標：

\[
m_T(x(t))
\]

逐漸增加。

當：

\[
m_T
\]

沒有自然 discontinuity 時：

\[
\boxed{
\text{Become-T}
}
\]

可能是一個 interval，而不是一個 point。

因此定義：

\[
[t_a,t_b]
\]

為 Acquisition Interval。

此時：

\[
t^*
\]

若被制度硬性指定，只是 operational threshold，不必等於本體中的天然臨界點。

---

# 15. Threshold T 與 Gradient T

本文區分：

## Threshold Identity

存在：

\[
\theta_T
\]

使：

\[
m_T(x)\geq\theta_T
\Rightarrow
x\in T.
\]

## Gradient Identity

身份本身允許程度：

\[
\mu_T(x)\in[0,1].
\]

本文不預設哪一種更正確。

但系統必須記住：

> 將 gradient 強迫轉為 threshold 是判定規則，而不必是世界本身的離散裂縫。

---

# 16. Criterion Shift：對象沒變，T 的定義變了

假設：

\[
x_t=x_{t+1},
\]

但：

\[
C_T^{(v1)}
\neq
C_T^{(v2)}.
\]

若：

\[
C_T^{(v1)}(x)=0
\]

而：

\[
C_T^{(v2)}(x)=1,
\]

則：

\[
x
\]

突然「變成 T」。

但真正變化是：

\[
\boxed{
\Delta Criterion.
}
\]

所以：

\[
\boxed{
\text{Reclassification}
\neq
\text{Object Transformation}.
}
\]

---

# 17. Context Shift：在 A 世界不是 T，在 B 世界是 T

若：

\[
C_{T,c_1}(x)=0
\]

但：

\[
C_{T,c_2}(x)=1,
\]

則：

\[
\boxed{
\Delta Context
\rightarrow
\Delta Identity Judgment.
}
\]

例如一個 token：

- 在測試系統中是 mock credential；
- 在 production 中不是合法 credential。

或者反之。

所以：

\[
\boxed{
\text{Identity Domain}
}
\]

必須攜帶 context。

---

# 18. Namespace Shift

同一 surface symbol：

\[
T
\]

在 namespace：

\[
N_1
\]

與：

\[
N_2
\]

可以指不同 type。

因此：

\[
\boxed{
T@N_1
\neq
T@N_2.
}
\]

如果一個對象被遷移進另一 namespace，其身份取得可能是：

\[
x@N_1
\rightarrow
x@N_2.
\]

這究竟是：

- same object with new namespace；
- new institutional identity；
- alias；
- fork；

取決於 migration rule。

---

# 19. Identity Admission Gate

為避免「任何人說它是 T 就算 T」，本文定義：

\[
\boxed{
Gate_T
(
x,
\Gamma,
c,
E
)
\in
\{
\mathrm{Accept},
\mathrm{Reject},
\mathrm{Provisional},
\mathrm{Underdetermined}
\}.
}
\]

只有：

\[
Gate_T=\mathrm{Accept}
\]

時，系統才正式記錄：

\[
IAE_T.
\]

---

# 20. Admission 不等於 Recognition

身份可能已經合法取得：

\[
Gate_T=\mathrm{Accept},
\]

但其他主體尚未知道。

所以：

\[
\boxed{
\text{Admission}
\neq
\text{Recognition}.
}
\]

定義：

\[
Recognize_A(x,T).
\]

可能：

\[
\operatorname{Be}(x,T)=1
\]

但：

\[
Recognize_A(x,T)=0.
\]

---

# 21. Recognition 也不等於 Admission

反過來：

\[
Recognize_A(x,T)=1
\]

也可能是錯誤判斷。

若：

\[
Gate_T=\mathrm{Reject},
\]

則只是：

# False Recognition

所以：

\[
\boxed{
\text{Being Treated as T}
\not\Rightarrow
\text{Being T}.
}
\]

---

# 22. Identity Acquisition Pipeline

本文提出最一般的管線：

\[
\boxed{
x
\rightarrow
Candidate_T
\rightarrow
Qualification
\rightarrow
Gate_T
\rightarrow
IAE_T
\rightarrow
Stabilization
\rightarrow
Recognized\ T.
}
\]

但這只是**可展開模板**，不是所有身份都必須走同樣流程。

---

# 23. Candidate-T

定義：

\[
\boxed{
Cand_T(x)
}
\]

表示 \(x\) 已進入 T 的候選域，但尚未取得正式身份。

Candidate 不等於：

\[
T.
\]

所以：

\[
\boxed{
Cand_T(x)
\not\Rightarrow
Be_T(x).
}
\]

這對：

- 新分類；
- AI 主體性候選；
- 安全事件；
- 法律資格；
- 新物種候選；

都很重要。

---

# 24. Provisional-T

若證據與規則支持暫時納入：

\[
Gate_T=\mathrm{Provisional},
\]

則可以：

\[
\boxed{
x\in T^{?}.
}
\]

其中：

\[
T^{?}
\]

不是完全 T，也不是非 T。

而是：

> 在指定治理條件下暫時以 T 處理。

這避免把：

\[
\mathrm{Underdetermined}
\]

硬壓成：

\[
\mathrm{Different}.
\]

---

# 25. 身份生成的三個時間

本文區分：

\[
t_C
\]

構成條件首次成立；

\[
t_A
\]

正式 admission；

\[
t_R
\]

被特定 observer recognition。

一般：

\[
\boxed{
t_C
\neq
t_A
\neq
t_R
}
\]

完全可能。

例如：

\[
t_C<t_A<t_R.
\]

所以「它什麼時候成為 T？」也可能是一個多時間問題。

---

# 26. Constitutive Time

定義：

\[
t_C
=
\inf
\{
t:
C_T(x_t)=1
\}.
\]

這是：

# Constitutive Acquisition Time

---

# 27. Institutional Time

若身份需要制度 admission：

\[
t_A
=
\text{time of valid institutional act}.
\]

它可能晚於 constitutive eligibility。

例如候選者早已滿足資格，正式批准卻晚幾天。

---

# 28. Recognition Time

\[
t_R(A)
=
\inf
\{
t:
J_A(x,T)=\mathrm{Same}
\}.
\]

不同觀察者：

\[
A,B
\]

可以：

\[
t_R(A)\neq t_R(B).
\]

所以：

\[
\boxed{
\text{Recognition Time Is Observer-Relative}.
}
\]

---

# 29. Become-T 的因果圖

身份取得不應只記：

\[
x\rightarrow T.
\]

而應記：

\[
\boxed{
\mathcal B_T
=
(
V_B,E_B
)
}
\]

其中節點可以是：

- state；
- evidence；
- rule；
- authority；
- relation；
- speech act；
- classifier；
- institution；
- recognition event。

這稱為：

# Become-T Causal Graph

---

# 30. Identity Transition Path

定義：

\[
\boxed{
ITP_T
=
x_0
\xrightarrow{e_1}
x_1
\xrightarrow{e_2}
\cdots
\xrightarrow{e_n}
T.
}
\]

其中每個：

\[
e_i
\]

需要標記：

- causal；
- classificatory；
- institutional；
- epistemic；
- naming；
- relational。

因此：

\[
\boxed{
\text{Not Every Edge in Become-T Is Causal in the Same Sense}.
}
\]

---

# 31. 分類可能反過來改變被分類者

社會本體論中的分類研究指出，某些分類並非被動描述；分類被人理解與採用後，可能反過來影響被分類者的行為與性質，進一步改變分類本身。

本文將此寫成：

\[
C_t
\rightarrow
J_t(x)
\rightarrow
Behavior_{t+1}(x)
\rightarrow
x_{t+1}
\rightarrow
C_{t+1}.
\]

形成：

\[
\boxed{
\text{Classification Loop}.
}
\]

---

# 32. Identity Looping

定義：

\[
\boxed{
L_T:
T^{class}_t
\leftrightarrow
T^{object}_t.
}
\]

若一個分類：

\[
Class_T
\]

改變被分類者：

\[
x,
\]

而新的 \(x\) 又促使分類規則改變：

\[
Class_T',
\]

則：

\[
\boxed{
\text{Identity Category and Identity Bearer Co-Evolve}.
}
\]

這尤其適合研究人類社會類別與某些 AI 治理分類。

---

# 33. 分類回饋不表示分類完全任意

即使：

\[
Class
\rightarrow
Object
\]

存在 causal feedback，也不能推出：

\[
Class
\]

可以任意設定。

因為：

- 身體；
- 技術；
- 制度；
- 歷史；
- 反饋；
- 其他主體；

都可能形成 constraints。

所以：

\[
\boxed{
\text{Socially Interactive}
\not\Rightarrow
\text{Unconstrained}.
}
\]

---

# 34. Self-Identification

若：

\[
A
\]

宣稱：

\[
I\ am\ T,
\]

是否因此：

\[
A\in T？
\]

答案取決於 identity type。

對某些內在立場，self-identification 可能是重要甚至必要的證據。

對某些制度身份，則仍需：

\[
Gate_T.
\]

對某些自然或技術類型，自我聲稱幾乎沒有構成力。

因此：

\[
\boxed{
\text{Self-Ascription}
}
\]

的權重必須由 \(\alpha\) 決定。

---

# 35. External Assignment

反之，若制度宣告：

\[
A\in T,
\]

也不能推廣成：

\[
\text{all dimensions of A are T}.
\]

制度可能只創造：

\[
T_{\mathrm{institutional}}.
\]

所以：

\[
\boxed{
\text{Institutional Assignment}
\not\Rightarrow
\text{Total Ontological Conversion}.
}
\]

---

# 36. Identity Acquisition 與權力

誰有權操作：

\[
Gate_T
\]

不是純技術問題。

它可能涉及：

- government；
- court；
- platform；
- scientific community；
- standards body；
- local community；
- individual；
- autonomous agent。

因此身份生成系統需要：

\[
\boxed{
Authority_T
}
\]

以及：

\[
\boxed{
Appeal_T.
}
\]

也就是：

> 誰能讓一個對象正式成為 T？  
> 誰能拒絕？  
> 誰能重新審查？

---

# 37. Become-T 與治理可逆性

身份取得可能：

## Reversible

\[
T
\rightarrow
\neg T
\rightarrow
T.
\]

## Irreversible

某些事件一旦發生，就無法真正回到 pre-T 歷史。

因此定義：

\[
\boxed{
Rev_T\in\{0,1,\mathrm{partial}\}.
}
\]

這將與 Paper 07 的 Identity Rupture／Recovery 直接連接。

---

# 38. 成為 T 也可能產生新的權利與義務

若制度身份：

\[
x\rightarrow T_I
\]

成立，則可能同時：

\[
Rights(x)
\rightarrow
Rights'(x),
\]

以及：

\[
Duties(x)
\rightarrow
Duties'(x).
\]

所以：

\[
\boxed{
\text{Identity Acquisition}
}
\]

有時不是純分類資料更新，而是 normative state transition。

---

# 39. Identity Transition 需要 provenance

Paper 03 已提出 Identity Grounding Certificate。

Paper 04 增加：

\[
\boxed{
IAC_T
=
Identity\ Acquisition\ Certificate.
}
\]

記錄：

- pre-state；
- target identity；
- acquisition mechanism；
- time；
- authority；
- rules；
- evidence；
- provenance；
- stabilization state。

---

# 40. IGC 與 IAC 的區分

Paper 03：

\[
IGC
\]

回答：

> 為什麼你現在有資格判它是 T？

Paper 04：

\[
IAC
\]

回答：

> 它是透過什麼事件取得 T 身份？

所以：

\[
\boxed{
IGC
\neq
IAC.
}
\]

但：

\[
IAC
\]

可以成為：

\[
IGC
\]

中的重要 evidence。

---

# 41. Acquire-T Operator

本文定義核心算子：

\[
\boxed{
\mathfrak B_T:
(
x,
\Gamma,
c,
t,
E,
R
)
\longrightarrow
(
x',
IAE,
IAC,
S
)
}
\]

其中：

- \(x\)：原狀態；
- \(\Gamma\)：生成機制；
- \(c\)：語境；
- \(t\)：時間；
- \(E\)：證據；
- \(R\)：規則；
- \(x'\)：後狀態；
- \(IAE\)：身份取得事件；
- \(IAC\)：身份取得證書；
- \(S\)：結果狀態。

---

# 42. Acquire-T 結果狀態

\[
S
\in
\{
\mathrm{Acquired},
\mathrm{RecognizedOnly},
\mathrm{Provisional},
\mathrm{Rejected},
\mathrm{Underdetermined}
\}.
\]

### Acquired

真的完成身份取得。

### RecognizedOnly

只是發現原本就有的身份。

### Provisional

暫時納入。

### Rejected

未通過 Admission Gate。

### Underdetermined

無足夠條件判定。

---

# 43. 核心命題一：分類—生成分離

\[
\boxed{
Classify_A(x,T)
\not\Rightarrow
Become_T(x).
}
\]

分類可以只是 epistemic act。

---

# 44. 核心命題二：身份取得不必要求 intrinsic state change

存在 relational／institutional identity，使：

\[
x_t=x_{t+1}
\]

在主要 intrinsic state 上成立，但：

\[
\boxed{
Identity_t
\neq
Identity_{t+1}.
}
\]

---

# 45. 核心命題三：Recognition 不決定 Acquisition

\[
\boxed{
Recognize_A(x,T)
\not\Leftrightarrow
Acquire_T(x).
}
\]

可以有未被發現的身份，也可以有錯誤承認。

---

# 46. 核心命題四：Become-T 可能由 criterion change 造成

若：

\[
C_T^{v1}(x)=0,
\qquad
C_T^{v2}(x)=1,
\]

則：

\[
\Delta J
\]

可能完全源自：

\[
\boxed{
\Delta Criterion
}
\]

而非：

\[
\Delta Object.
\]

---

# 47. 核心命題五：身份生成機制必須型別化

不能只保存：

\[
x\rightarrow T.
\]

至少應保存：

\[
\boxed{
x
\xrightarrow{\Gamma}
T
}
\]

因為：

\[
\Gamma=
Discovery
\]

與：

\[
\Gamma=
InstitutionalConferment
\]

具有完全不同的本體與治理意義。

---

# 48. TTTTT 的生成史

考慮：

\[
T_1T_2T_3T_4T_5.
\]

表面：

\[
G(T_i)=T.
\]

但：

\[
\Gamma(T_i)
\]

可以全部不同。

例如：

\[
\Gamma(T_1)=Discovery,
\]

\[
\Gamma(T_2)=Transformation,
\]

\[
\Gamma(T_3)=Institutional,
\]

\[
\Gamma(T_4)=Relational,
\]

\[
\Gamma(T_5)=CriterionShift.
\]

於是：

\[
\boxed{
\text{Same Surface}
\not\Rightarrow
\text{Same Identity Genesis}.
}
\]

---

# 49. Genesis Entropy

因此可以定義：

\[
H(\Gamma\mid G=T).
\]

即使：

\[
H(G)=0,
\]

仍可能：

\[
\boxed{
H(\Gamma\mid G=T)>0.
}
\]

這進一步擴張了 Paper 01 的：

\[
\text{Surface Entropy}
\neq
\text{Identity Entropy}.
\]

現在變成：

\[
\boxed{
\text{Surface Entropy}
\neq
\text{Genesis Entropy}.
}
\]

---

# 50. 與既有研究的邊界

社會本體論研究制度、規則、社會種類以及分類與對象之間可能存在的互動；其中 Searle 式 constitutive-rule 路線強調某些 institutional facts 與 collective acceptance／rules 的關聯，但這並非社會本體論的唯一模型。分類研究也討論某些 human kinds 中 classification 對被分類者產生 causal feedback 的可能。

Speech-act 研究則提供另一個重要外部定位：在合適制度與語境下，一些 utterances 並非單純描述既有世界，也是在執行社會行動。

本文的新增工作不是把這些理論重新命名。

而是把它們與：

- intrinsic transformation；
- discovery；
- relation acquisition；
- emergent maturation；
- criterion shift；

一起放進一個統一的 Become-T identity transition framework。

---

# 51. 結論

「T 怎麼變成 T？」不能只寫：

\[
x\rightarrow T.
\]

因為至少還要問：

> 是 \(x\) 改變了嗎？

還是：

> 關係改變了？

或者：

> 制度承認了它？

或者：

> 我們只是今天才發現？

或者：

> T 的定義改了？

甚至：

> 分類本身反過來改變了它？

所以本文最終提出：

\[
\boxed{
\Delta Identity
=
F(
\Delta Object,
\Delta Relation,
\Delta Institution,
\Delta Criterion,
\Delta Evidence,
\Delta Recognition
).
}
\]

但：

\[
F
\]

不是所有身份共享的單一固定公式。

成熟身份理論必須首先辨認：

\[
\boxed{
\Gamma
=
\text{Which Become-T Mechanism?}
}
\]

因此：

\[
\boxed{
\text{Being T}
\neq
\text{Becoming T}
\neq
\text{Being Recognized as T}.
}
\]

下一篇 Paper 05〈T 怎麼被稱為 T？〉將把這個系列推進到 naming：

\[
\boxed{
A
\xrightarrow{\operatorname{Name}}
x
\mapsto
T.
}
\]

核心問題會變成：

> 誰有資格命名？  
> 名稱如何取得指涉？  
> 名稱是否能跨時間、語言與 namespace 持續指向同一對象？  
> 被稱作 T 與真正是 T，究竟何時重合、何時分離？
