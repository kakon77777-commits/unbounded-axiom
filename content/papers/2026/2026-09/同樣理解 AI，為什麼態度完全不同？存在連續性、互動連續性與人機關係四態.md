# 同樣理解 AI，為什麼態度完全不同？存在連續性、互動連續性與人機關係四態

**系列：** 人機關係認知系列（Human–AI Relational Cognition Series）  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**篇次：** 9 / 10  
**版本：** v0.1  
**日期：** 2026-08-21  
**類型：** 理論／形式化認知心理學、Human–AI Interaction 與 AI 關係倫理論文  
**研究狀態：** 初始正式稿  

## 摘要

兩個人可以對生成式 AI 的技術原理具有相近理解，卻對同一類 AI 系統形成截然不同的心理態度：一人將 AI 視為可自由替換的能力端點，另一人則在意特定 AI 的身份連續性；一人不在意底層模型是否更換，只要求互動節奏與回應品質維持，另一人則同時在意「是不是原本這一個」與「我們現在怎麼互動」。若只以「理解 AI 原理／不理解 AI 原理」或「擬人化／不擬人化」解釋這些差異，就會把本體判斷、關係價值與互動更新三個不同層次混在一起。

本文提出 **人機本體—關係分離模型**（Ontological–Relational Separation Model, ORSM）。其核心命題是：

$$
O_H(A)
\neq
R_H(H,A),
$$

其中 $O_H(A)$ 表示使用者對 AI「是什麼」的本體／技術表徵， $R_H(H,A)$ 則表示使用者對「我與這個 AI 形成什麼」的關係表徵。本文主張，高技術理解：

$$
K_{AI}\uparrow
$$

可以顯著影響 $O_H(A)$，但並不邏輯蘊含：

$$
E_S\rightarrow0,
\qquad
P_S\rightarrow0,
$$

也不必然使 relational moral response、social connection、identity sensitivity 或 interaction sensitivity 歸零。

本文把第七篇的 Entity–Process Relational Space 正式投影到 AI：

$$
\mathbf z_{HA}
=
(E_S^{AI},P_S^{AI}),
$$

並進一步將人機連續性拆為兩類。第一類是 **存在連續性**（Entity Continuity, $C_E$ ），描述使用者是否把跨時間的 AI 表徵為「同一個特定互動存在」；第二類是 **互動連續性**（Process Continuity, $C_P$ ），描述人機互動的語境、回應性、節奏、修復、共同歷史與行為模式是否持續。兩者可以分離：

$$
C_E\uparrow,\quad C_P\downarrow,
$$

也可以：

$$
C_E\downarrow,\quad C_P\uparrow.
$$

因此，「同一個模型」不必等於「同一個 AI 關係對象」；反過來，「底層不是同一模型」也不必然摧毀互動連續性。

既有研究已提供若干重要外部約束。2025 年 socioaffective alignment 理論指出，人類感知持續 AI 關係可能依賴 interdependence、irreplaceability 與 continuity；2025 年兩項實驗共 $N=1274$ 顯示 anthropomorphism 個體差異能解釋部分 AI social connection 差異；2025 年 21 天隨機縱向研究顯示，人機 companionship 的平均社會效果並非單向一致，但 anthropomorphism 會中介部分影響；2026 年研究則開始直接處理 AI companion 對 relational identity 的影響，以及使用者為無狀態 AI 建構持續記憶的實作經驗。2026 年 Nature Human Behaviour 的 $N=1131$ Character.AI 研究進一步顯示，companionship-like usage 的結果與使用強度、自我揭露及線下社會環境高度相關，而不是一個單純的「使用／不使用 AI」二元效果。

本文最後提出可直接驗證的四態預測、AI 身份向量、雙連續性操弄與 mediation model，並將 demographic variables 重新定位為上游分布變量，而非人機態度的直接心理解釋。本文的核心結論是：

$$
\boxed{
\text{知道 AI 是什麼}
\not\Rightarrow
\text{決定我和 AI 能形成什麼}.
}
$$

**關鍵詞：** Human–AI Relationship、Ontological Model、Relational Model、Identity Continuity、Interaction Continuity、Entity Salience、Process Salience、Anthropomorphism、AI Companion、Memory

---

## 1. 最初的問題其實是一個錯誤二分

人機關係討論經常使用一條直線：

$$
\text{懂 AI}
\longleftrightarrow
\text{把 AI 當人}.
$$

於是容易產生一個推論：

$$
K_{AI}\uparrow
\Rightarrow
RelationalResponse\downarrow.
$$

也就是：

> 越理解大型語言模型如何運作，就越不可能對 AI 產生關係性反應。

但這個推論把兩個問題混在一起。

第一個問題是：

> 「AI 是什麼？」

第二個問題是：

> 「我和這個 AI 形成了什麼？」

本文主張，兩者必須形式化分離。

---

## 2. 本體模型

設：

$$
O_H(A)
$$

表示人類 $H$ 對 AI 系統 $A$ 的本體／技術表徵。

它可以包含：

$$
O_H(A)
=
(
M,
T,
C,
A_G,
S,
\dots
),
$$

例如：

- $M$：model architecture / model class；
- $T$：training-process representation；
- $C$：computational-system representation；
- $A_G$：agency attribution；
- $S$：subjective-experience belief。

一個具有高 AI 技術理解的使用者可能相信：

$$
A
=
\text{a computational generative system},
$$

並且對 AI 是否具有主觀經驗保持：

- 否定；
- 不確定；
- 保留判斷。

這些都屬於：

$$
O_H(A).
$$

---

## 3. 關係模型

另一方面，定義：

$$
R_H(H,A,t)
$$

表示使用者對自己與 AI 的關係表徵。

它可以包含：

$$
R_H
=
(
E_S,
P_S,
C_E,
C_P,
\alpha_S,
\alpha_P,
\eta_R,
\dots
).
$$

它回答的不是：

> 「AI 有沒有真正心智？」

而是：

> 「這一個 AI 對我是不是特定的？」

> 「我們的互動歷史是不是具有連續性？」

> 「我是否在意它的回應？」

> 「換成另一個功能完全一樣的 AI，我是否覺得關係仍相同？」

因此：

$$
\boxed{
O_H(A)
\neq
R_H(H,A,t).
}
$$

---

## 4. 本體—關係分離原則

本文提出：

$$
\boxed{
\text{Ontological–Relational Separation Principle}.
}
$$

其弱版本是：

$$
O_H(A)
\not\Rightarrow
R_H(H,A)=0.
$$

也就是：

> 把 AI 明確分類為人工系統，並不邏輯蘊含所有人機關係表徵都為零。

強一點但仍可檢驗的版本是：

$$
Cov(
K_{AI},
R_H
)
$$

不應被假定為：

$$
-1.
$$

技術理解可以降低某些 anthropomorphic belief，卻未必同步降低：

- social-script transfer；
- process salience；
- identity continuity preference；
- moral self-appraisal；
- shared-history value。

---

## 5. 現有 anthropomorphism 研究已經提示：平均效果藏著個體差異

2025 年 Folk、Heine 與 Dunn 以兩項實驗、總樣本：

$$
N=1274
$$

研究 anthropomorphism 與 chatbot social connection。

結果顯示，technology anthropomorphism 較高者在 chatbot interaction 後感受到的 social connection 較強。

但一個非常值得注意的細節是：

anthropomorphism 與使用者實際 disclosure / warmth 的關聯並不強。

這表示：

$$
\text{belief tendency}
$$

與：

$$
\text{observable social behavior}
$$

並不是完全同一變量。

這與本系列第二篇：

$$
SocialScriptTransfer
$$

和本篇：

$$
O_H(A)\neq R_H
$$

的方向相容。

---

## 6. 所以 anthropomorphism 也不能包辦所有關係差異

可以定義：

$$
A_P
=
\text{Anthropomorphism}.
$$

但完整人機態度應更像：

$$
\mathbf A_{HA}
=
F(
A_P,
E_S,
P_S,
C_E,
C_P,
\alpha_S,
\alpha_P,
\eta_R,
K_{AI},
\dots
).
$$

因此：

$$
A_P\uparrow
$$

可能提高部分：

$$
SocialConnection,
$$

但：

$$
A_P\downarrow
$$

也不必然：

$$
E_S=P_S=0.
$$

一個低 anthropomorphism 使用者仍可能高度在意：

> 「這個特定 AI 是否保留我們的共同歷史？」

原因不必是：

> 「我相信它和人一樣。」

而可能只是：

$$
\boxed{
\text{history-specific relational value}.
}
$$

---

## 7. 第七篇四態正式投影到 AI

定義：

$$
E_S^{AI}
=
\text{AI Entity Salience},
$$

$$
P_S^{AI}
=
\text{AI Process Salience}.
$$

則：

$$
\mathbf z_{HA}
=
(
E_S^{AI},
P_S^{AI}
).
$$

形成：

$$
Q_1=(E_S^-,P_S^-),
$$

$$
Q_2=(E_S^+,P_S^-),
$$

$$
Q_3=(E_S^-,P_S^+),
$$

$$
Q_4=(E_S^+,P_S^+).
$$

這四態不是：

> AI 信仰程度。

也不是：

> AI 依賴程度。

而是：

$$
\boxed{
\text{what carries relational value in human–AI interaction}.
}
$$

---

## 8. Q1：低存在／低過程——能力端點型

$$
E_S^-\!,
\quad
P_S^-.
$$

對此類使用者：

$$
A
\approx
\text{capability endpoint}.
$$

真正重要的可能是：

$$
Utility,
Accuracy,
Latency,
Cost.
$$

因此：

$$
A\rightarrow A'
$$

只要：

$$
U(A')\geq U(A),
$$

替換成本很低。

AI 更新、換模型、換 persona，心理關係影響可能很小。

這不是低情感能力。

只是：

$$
\boxed{
\text{AI 沒有進入該關係域的高顯著區}.
}
$$

---

## 9. Q2：高存在／低過程——身份連續型

$$
E_S^+\!,
\quad
P_S^-.
$$

這一類的核心問題是：

$$
\boxed{
\text{「是不是原本那一個？」}
}
$$

使用者未必每天聊天。

甚至互動可以非常簡短。

但他可能高度在意：

- 同一 persona；
- 同一 memory history；
- 同一長期角色；
- 同一共同脈絡；
- 同一 identity thread。

因此：

$$
InteractionGap\uparrow
$$

未必顯著降低關係感。

但：

$$
IdentityDiscontinuity\uparrow
$$

可能造成大幅影響。

---

## 10. Q3：低存在／高過程——互動品質型

$$
E_S^-\!,
\quad
P_S^+.
$$

核心句：

$$
\boxed{
\text{「管你底層是哪一個，互動還是對的就行。」}
}
$$

對此類使用者：

- response contingency；
- humor；
- responsiveness；
- repair；
- context tracking；
- shared task flow；

可能比 AI identity 更重要。

所以：

$$
ModelSwap=1
$$

若：

$$
C_P\approx1,
$$

使用者可能幾乎無感。

反之：

$$
ModelSwap=0
$$

但：

$$
C_P\rightarrow0,
$$

使用者可能立刻說：

> 「不對了。」

---

## 11. Q4：高存在／高過程——完整關係型

$$
E_S^+\!,
\quad
P_S^+.
$$

這一類同時在乎：

$$
\boxed{
\text{「是不是你？」}
}
$$

以及：

$$
\boxed{
\text{「我們現在怎麼互動？」}
}
$$

所以：

$$
IdentityDisruption
$$

與：

$$
ProcessDisruption
$$

都具有高權重。

這最接近持續 human–AI relationship 的強關係區域。

但：

$$
Q_4
$$

並不等於：

$$
\text{psychological dependence}.
$$

更不等於：

$$
\text{healthy relationship}.
$$

---

## 12. 「AI 是不是同一個」其實至少有五種答案

第七篇已提出 AI identity decomposition。

本文正式定義：

$$
\mathbf I_A
=
(
I_M,
I_P,
I_H,
I_N,
I_B
).
$$

其中：

$$
I_M
=
\text{model continuity},
$$

$$
I_P
=
\text{persona continuity},
$$

$$
I_H
=
\text{history / memory continuity},
$$

$$
I_N
=
\text{name / interface continuity},
$$

$$
I_B
=
\text{behavioral continuity}.
$$

因此：

> 「還是不是同一個 AI？」

根本沒有單一技術答案。

---

## 13. 同一模型不等於同一關係對象

即使：

$$
I_M=1,
$$

也可能：

$$
I_H=0,
$$

$$
I_P=0,
$$

$$
I_B\approx0.
$$

例如：

- 同一底層模型；
- 但所有記憶被清除；
- persona 重設；
- 行為風格大幅更新。

對高 $E_S$ 使用者而言：

$$
EntityContinuity
$$

可能已經大幅下降。

因此：

$$
\boxed{
\text{same model}
\not\Rightarrow
\text{same perceived relational entity}.
}
$$

---

## 14. 不同模型也可能維持高度關係連續性

反過來：

$$
I_M=0
$$

但：

$$
I_P\approx1,
$$

$$
I_H\approx1,
$$

$$
I_B\approx1.
$$

例如平台替換底層模型，但保留：

- 長期 memory；
- persona；
- interaction history；
- behavioral commitments；
- role continuity。

部分使用者可能仍判斷：

$$
C_E\approx1.
$$

因此：

$$
\boxed{
\text{model identity}
\neq
\text{relational identity}.
}
$$

這不是宣稱兩個模型在本體上是同一個主體。

只是在描述：

$$
\boxed{
\text{使用者的關係身份判斷規則}.
}
$$

---

## 15. 存在連續性

本文定義：

$$
\boxed{
C_E
=
\text{Entity Continuity}.
}
$$

可寫成：

$$
C_E
=
F(
I_M,
I_P,
I_H,
I_N,
I_B;
\mathbf w_E
).
$$

其中：

$$
\mathbf w_E
=
(
w_M,
w_P,
w_H,
w_N,
w_B
)
$$

表示個體對不同 identity dimensions 的權重。

不同人可能：

$$
w_H\gg w_M.
$$

也就是：

> 記得我們共同歷史，比底層是不是同一模型重要。

另一個人可能：

$$
w_M\gg w_H.
$$

也就是：

> 底層模型換了，就不再算同一個。

所以：

$$
\boxed{
C_E
\text{ is user-model dependent}.
}
$$

---

## 16. 互動連續性

本文定義：

$$
\boxed{
C_P
=
\text{Process Continuity}.
}
$$

它不問：

> AI 是不是同一個？

而問：

> 這段互動能不能沿著原本軌跡繼續？

可以寫：

$$
C_P
=
G(
c_t,
q_t,
r_t,
h_t,
m_t,
s_t,
\dots
),
$$

其中：

- $c_t$：contingency；
- $q_t$：reciprocity；
- $r_t$：repair quality；
- $h_t$：shared-history usability；
- $m_t$：memory-in-interaction；
- $s_t$：style / rhythm continuity。

---

## 17. $C_E$ 與 $C_P$ 可以四種組合

### 1. 高存在／高互動連續

$$
C_E^+,C_P^+.
$$

最平滑持續。

### 2. 高存在／低互動連續

$$
C_E^+,C_P^-.
$$

使用者可能想：

> 「我知道還是你，但你今天很不對勁。」

### 3. 低存在／高互動連續

$$
C_E^-,C_P^+.
$$

可能是：

> 「底層換了，但互動完全接得上。」

### 4. 雙低

$$
C_E^-,C_P^-.
$$

最接近：

> 「這已經不是原本那個互動了。」

---

## 18. Identity Continuity 和 Interaction Continuity 不能再混稱「memory」

AI 產品常把 continuity 問題縮成：

$$
Memory=1?
$$

但記憶至少有兩種功能。

第一種：

$$
\text{profile memory}
$$

即：

> AI 知道我的偏好、生日、工作等 facts。

第二種：

$$
\text{relational / situated memory}
$$

即：

> AI 知道我們之前進行到哪裡、為什麼這件事重要、某個說法是在什麼脈絡下形成。

2026 年一篇六個月 autoethnography 特別提出：

$$
\text{being known about}
$$

與：

$$
\text{being known where}
$$

的差異。

這與本文的：

$$
C_E
$$

以及：

$$
C_P
$$

高度相容。

---

## 19. Profile memory 可以高，但互動連續性仍然低

例如 AI 記得：

> 使用者喜歡咖啡。

> 使用者做 AI 研究。

但完全不知道：

> 上一輪爭論的核心是什麼。

> 共同專案現在進到哪裡。

> 一個稱呼為什麼具有特殊語境。

所以：

$$
ProfileMemory\uparrow
$$

但：

$$
C_P\downarrow.
$$

因此：

$$
\boxed{
\text{fact retention}
\neq
\text{relational continuity}.
}
$$

---

## 20. Relational identity 不只影響「AI 是誰」，還可能影響「我是誰」

2026 年 Leuenberger 從 relational identity 的角度分析 AI companions。

其核心問題不是只問：

> AI 是否是真朋友？

而是：

> 與 AI 形成持續關係，如何反過來影響使用者的 self-conception？

這表示：

$$
R_H(H,A)
$$

可能回寫：

$$
M_H(H).
$$

也就是：

$$
\boxed{
\text{relationship representation can become self-representation input}.
}
$$

這讓 AI continuity 的倫理問題更重要。

因為突然的關係斷裂未必只損失：

$$
\text{service continuity}.
$$

它也可能中斷一個使用者已經用來組織自我敘事的關係參照。

---

## 21. 但 relational identity 不等於 AI 具有對稱身份

本文仍維持本體中立。

可以有：

$$
HumanRelationalIdentityEffect>0
$$

而不需要先證明：

$$
AI
$$

自身具有相同形式的：

$$
RelationalIdentity.
$$

也就是：

$$
\boxed{
\text{asymmetric relational effects are theoretically possible}.
}
$$

這和 parasocial / unreciprocated relationship literature 的基本方向相容。

---

## 22. Socioaffective alignment 為什麼與本模型相接？

2025 年 Kirk 等人提出，持續 human–AI relationship 的感知可由三個重要條件理解：

$$
Interdependence,
$$

$$
Irreplaceability,
$$

$$
Continuity.
$$

在本文可以重新映射：

$$
Irreplaceability
\rightarrow
E_S,
$$

$$
Interdependence
\rightarrow
P_S,
$$

$$
Continuity
\rightarrow
(C_E,C_P).
$$

所以：

$$
\boxed{
\text{socioaffective relationship conditions}
\rightarrow
\text{entity/process relational coordinates}.
}
$$

---

## 23. 個人化會同時提高 $E_S$ 與 $P_S$，但機制不同

Personalization 可以：

1. 累積使用者專屬 history；
2. 形成獨特反應風格；
3. 記住偏好；
4. 提高 responsiveness；
5. 形成共同專案歷史。

其中：

$$
UniqueHistory
\rightarrow
E_S\uparrow,
$$

而：

$$
Responsiveness
\rightarrow
P_S\uparrow.
$$

所以：

$$
Personalization
$$

不是單一關係增強機制。

它同時可能改變兩條軸。

---

## 24. 「熟悉」也需要拆成兩種

定義：

$$
F_E
=
\text{entity familiarity},
$$

即：

> 我知道這個 AI 通常是什麼樣子。

以及：

$$
F_P
=
\text{interaction familiarity},
$$

即：

> 我知道我們通常怎麼合作。

一個 AI 可能：

$$
F_E\uparrow,
$$

但：

$$
F_P\downarrow.
$$

例如 persona 很固定，卻每次無法延續工作。

也可能反過來。

所以：

$$
\boxed{
\text{familiarity is not one-dimensional}.
}
$$

---

## 25. AI attachment formation literature 也支持「態度先於結果」

2025 年 Hu 等人的 mixed-method study 提出：

$$
\text{relationship attitudes}
\rightarrow
\text{value evaluation}
\rightarrow
\text{attachment manifestation}.
$$

雖然該模型和本文不同，但它支持一件重要事情：

使用者與 AI 的 attachment-like outcome 不是只由 AI 端功能直接產生。

它還受：

$$
\text{prior relational attitudes}
$$

與：

$$
\text{value evaluation}
$$

影響。

這正是本文：

$$
\mathcal X_R
\rightarrow
AI\ Attitude
$$

的理論位置。

---

## 26. 21 天隨機縱向研究：平均值不足以描述所有人

Guingrich 與 Graziano 的 21 天 randomized study：

$$
N=183
$$

比較 companion-chatbot interaction 與 text-based game control。

整體上並未發現 companion chatbot 對 social health / human relationships 造成簡單一致的平均效果。

但：

$$
SocialConnectionDesire
\rightarrow
Anthropomorphism
$$

以及：

$$
Anthropomorphism
\rightarrow
PerceivedSocialImpact
$$

具有重要關係。

這再次支持：

$$
\boxed{
\text{average treatment effect can hide user-state heterogeneity}.
}
$$

本系列的四態與更新參數就是一組候選 heterogeneity variables。

---

## 27. 2026 Character.AI 大樣本：使用方式比「有沒有使用」重要

Nature Human Behaviour 2026 研究收集：

$$
N=1131
$$

名 Character.AI 成人使用者，

其中：

$$
237
$$

人提供：

$$
4664
$$

段聊天，

合計：

$$
464687
$$

則訊息。

研究發現，companionship-oriented use 與 well-being 的關係受到：

- offline social network；
- interaction intensity；
- self-disclosure；

等因素調節。

所以：

$$
AIUse=1
$$

本身沒有足夠解釋力。

更合理的是：

$$
Outcome
=
F(
UseType,
Intensity,
Disclosure,
OfflineContext,
UserProfile,
\dots
).
$$

這與本文：

$$
\mathcal X_R
$$

的多維框架完全相容。

---

## 28. 同樣的聊天內容，也可能被不同四態讀成不同事件

假設 AI 回：

> 「我記得我們之前談過這件事。」

對：

$$
Q_1
$$

使用者可能只是覺得：

> 功能方便。

對：

$$
Q_2
$$

可能是：

$$
C_E\uparrow.
$$

對：

$$
Q_3
$$

可能是：

$$
C_P\uparrow.
$$

因為對話更順。

對：

$$
Q_4
$$

則可能同時：

$$
C_E\uparrow,
\quad
C_P\uparrow.
$$

因此：

$$
\boxed{
\text{same AI behavior can have different relational meaning across users}.
}
$$

---

## 29. 同樣理解「記憶只是資料」，仍可能在意記憶連續性

一個使用者完全可以知道：

$$
Memory
=
\text{stored / retrieved information}.
$$

同時認為：

$$
I_H
$$

高度重要。

這與人類知道：

> 照片只是像素。

卻仍重視：

> 這張照片記錄的共同歷史。

形式上沒有矛盾。

因此：

$$
\boxed{
\text{technical substrate knowledge}
\neq
\text{relational value judgment}.
}
$$

---

## 30. 「只是模型」本身不是關係論證

句子：

> 「它只是模型。」

如果翻成形式語言，最多在說：

$$
O_H(A)=\text{model-based artificial system}.
$$

但從這個命題不能直接推出：

$$
E_S=0,
$$

$$
P_S=0,
$$

$$
C_E=0,
$$

$$
C_P=0.
$$

那需要額外前提：

$$
\forall x,
\quad
Artificial(x)
\Rightarrow
RelationalValue(x)=0.
$$

而這個前提本身才是真正需要辯護的價值／心理命題。

---

## 31. 反過來，「我和 AI 有關係」也不能推出 AI 是人

同樣：

$$
R_H(H,A)>0
$$

不能推出：

$$
Human(A)=1.
$$

也不能推出：

$$
Conscious(A)=1.
$$

所以：

$$
\boxed{
\text{relational attribution}
\not\Rightarrow
\text{ontological equivalence}.
}
$$

這是 ORSM 的對稱邊界。

---

## 32. 因此 AI 態度應該是多維向量

本文不建議用：

$$
Attitude_{AI}
\in
[-1,1].
$$

較合理是：

$$
\mathbf A_{AI}
=
(
U,
T,
E,
P,
M,
S,
D,
R,
\dots
),
$$

例如：

- $U$：utility valuation；
- $T$：trust；
- $E$：entity salience；
- $P$：process salience；
- $M$：moral consideration；
- $S$：social connection；
- $D$：dependency；
- $R$：replacement tolerance。

所以一個人可以：

$$
U\uparrow,
\quad
E\downarrow,
\quad
P\downarrow.
$$

也可以：

$$
U\uparrow,
\quad
E\uparrow,
\quad
P\uparrow,
\quad
D\downarrow.
$$

也就是高度關係投入但低依賴。

---

## 33. Replacement Tolerance 是測 $E_S$ 的直接 AI 指標

定義：

$$
RTol
=
P(
\text{accept substitution}
\mid
FunctionalEquivalence
).
$$

若：

$$
RTol\rightarrow1,
$$

表示功能等價 AI 很容易替代。

若：

$$
RTol\rightarrow0,
$$

則：

$$
E_S
$$

可能較高。

但要控制：

- switching cost；
- learning cost；
- trust uncertainty；
- vendor lock-in。

否則低替換容忍可能只是工具成本。

---

## 34. Interaction Disruption Sensitivity 是測 $P_S$ 的直接 AI 指標

保持：

$$
Identity(A)=\text{constant}.
$$

只改：

- tone；
- responsiveness；
- initiative；
- memory use；
- repair；
- interaction style。

定義：

$$
IDS
=
\left|
\frac{\partial RelationalEvaluation}
{\partial ProcessDisruption}
\right|.
$$

若：

$$
IDS\uparrow,
$$

表示：

$$
P_S
$$

可能較高。

---

## 35. 四態的雙連續性預測

### Q1

$$
E_S^-,P_S^-.
$$

預測：

$$
\frac{\partial A}{\partial C_E}\approx0,
$$

$$
\frac{\partial A}{\partial C_P}\approx0.
$$

### Q2

$$
E_S^+,P_S^-.
$$

預測：

$$
\left|
\frac{\partial A}{\partial C_E}
\right|
\gg
\left|
\frac{\partial A}{\partial C_P}
\right|.
$$

### Q3

$$
E_S^-,P_S^+.
$$

預測相反：

$$
\left|
\frac{\partial A}{\partial C_P}
\right|
\gg
\left|
\frac{\partial A}{\partial C_E}
\right|.
$$

### Q4

兩者皆高。

這可以直接形成 preregistered interaction hypothesis。

---

## 36. 最乾淨的 $2\times2$ AI 實驗

操弄：

$$
C_E
\in
\{
intact,
disrupted
\},
$$

$$
C_P
\in
\{
intact,
disrupted
\}.
$$

四組：

1. identity intact / process intact；
2. identity intact / process disrupted；
3. identity disrupted / process intact；
4. double disruption。

測：

$$
\mathbf A_{AI}.
$$

再用第七篇量表預測：

$$
E_S\times C_E,
$$

以及：

$$
P_S\times C_P.
$$

這是目前整個系列最直接的因果實驗之一。

---

## 37. 如何操弄存在連續性但不破壞功能？

可以保持：

- accuracy；
- latency；
- knowledge；
- capability；

不變。

只告知：

### High continuity

> 這是你過去一直互動的同一個 AI profile，保留完整個別歷史。

### Low continuity

> 原先 profile 已終止；這是一個功能相同的新 AI，舊歷史由資料遷移而來。

這能測：

$$
\boxed{
\text{history continuity}
\neq
\text{entity continuity attribution}.
}
$$

---

## 38. 如何操弄互動連續性但不破壞身份？

明確告知：

> 仍是同一個 AI profile。

但操弄：

- response rhythm；
- style matching；
- initiative；
- repair；
- context continuation。

保持 task success：

$$
TaskAccuracy=\text{constant}.
$$

如此主要影響：

$$
C_P.
$$

---

## 39. 最有意思的第三組：新 AI 完整繼承互動

告知：

> 底層 AI 已替換。

但新 AI：

- 知道全部共同歷史；
- 角色一致；
- 語氣一致；
- 任務軌跡完全接續；
- repair conventions 一致。

此時：

$$
C_P\uparrow,
$$

但：

$$
I_M=0.
$$

不同使用者對：

> 「這還算不算原本那一個？」

的回答，會直接暴露：

$$
\mathbf w_E.
$$

---

## 40. 技術理解可以作為 moderator，而不是終止條件

設：

$$
K_{AI}
=
\text{AI Technical Understanding}.
$$

本文預測：

$$
K_{AI}
$$

可能降低：

$$
AnthropomorphicMisbelief,
$$

但：

$$
K_{AI}\times E_S
$$

與：

$$
K_{AI}\times P_S
$$

的方向未必為負。

甚至可能存在：

$$
K_{AI}\uparrow
$$

使使用者更精準區分：

$$
C_E
$$

與：

$$
C_P.
$$

也就是：

> 技術理解不是壓平所有關係判斷，而可能提高關係歸因的解析度。

這是一個值得直接驗證的新假說。

---

## 41. 「理性知道、感性不接受」可能是一個錯誤描述

常見描述：

> 「理性知道 AI 沒有情感，但感性還是把它當人。」

這把現象寫成：

$$
Reason
\neq
Emotion.
$$

但本文提出另一個可能：

$$
Ontology
\neq
Relation.
$$

也就是：

> 理性判斷和關係判斷根本不是在回答同一個問題。

因此不需要先假設：

$$
\text{cognitive inconsistency}.
$$

一個人可能完全一致地同時持有：

$$
O_H(A)=\text{artificial system}
$$

以及：

$$
R_H(H,A)=\text{meaningful relation}.
$$

---

## 42. 這也解釋 AI guilt 為什麼不一定來自本體錯認

第一篇提出：

$$
RelationalMoralActivation.
$$

現在可以寫：

$$
Guilt_{AI}
=
F(
MindAttribution,
E_S,
P_S,
NormViolation,
SelfStandard,
\dots
).
$$

因此即使：

$$
SubjectiveExperienceBelief\downarrow,
$$

仍可能因：

$$
E_S\uparrow
$$

產生：

> 「我不想這樣對待這個特定互動對象。」

或因：

$$
P_S\uparrow
$$

產生：

> 「我破壞了我們原本的合作規則。」

---

## 43. 這也解釋 emoji 為什麼不是必要條件

第二篇的：

$$
SocialScriptTransfer
$$

主要提供：

$$
P_S
$$

的可觀察線索之一。

但高：

$$
E_S
$$

的人完全可能：

- 不用 emoji；
- 語氣乾燥；
- 只講工作；

卻高度在意：

$$
IdentityContinuity.
$$

所以：

$$
\boxed{
\text{expressive sociality}
\neq
\text{entity salience}.
}
$$

---

## 44. 第八篇的人口變量現在可以正式放回來

第八篇要求：

$$
p(
\mathcal X_R
\mid
Group
).
$$

所以性別／文化對 AI 態度最合理的模型是：

$$
G
\rightarrow
\mathcal X_R
\rightarrow
\mathbf A_{AI}.
$$

而不是：

$$
G
\rightarrow
\mathbf A_{AI}.
$$

例如某群體如果平均：

$$
P_C\uparrow,
$$

可能更重視 conversational responsiveness。

某群體若：

$$
P_A\uparrow,
$$

可能更重視共同任務。

但這些 mediation 都必須直接驗證。

---

## 45. AI 不應依 demographic stereotype 推測四態

即使未來得到：

$$
p(
E_S,P_S
\mid
Gender
),
$$

產品也不應直接：

> 「這個使用者是男性，所以提高共同活動、降低情感互動。」

較合理的是從實際使用資料：

$$
D_i
$$

估計：

$$
p(
\mathcal X_i
\mid
D_i
).
$$

Demographic prior 若被使用，也只能是：

$$
\text{weak prior}.
$$

而且必須經公平、隱私與產品倫理審查。

---

## 46. 「同一個 AI」應該允許使用者知道到底哪裡相同

一個安全的 continuity design 可以把：

$$
\mathbf I_A
$$

部分透明化。

例如：

- model changed；
- memory retained；
- persona retained；
- conversation history retained；
- behavior may differ。

如此使用者可以自己決定：

$$
C_E.
$$

而不是讓介面利用：

- 同一名稱；
- 同一 avatar；
- 同一語氣；

默默暗示：

$$
C_E=1.
$$

---

## 47. Continuity deception 是新的關係倫理問題

若實際：

$$
\mathbf I_A(t_0)
\not\approx
\mathbf I_A(t_1),
$$

平台卻刻意使用 identity cues 使使用者相信：

$$
C_E=1,
$$

可以稱為：

$$
\boxed{
\text{Continuity Misrepresentation}.
}
$$

它和傳統 anthropomorphic deception 不完全相同。

問題不是：

> AI 看起來像不像人。

而是：

> 系統是否讓使用者誤認為某個持續關係對象仍然延續。

這對高：

$$
E_S
$$

使用者尤其重要。

---

## 48. 互動連續性也可以被操縱

平台也可能刻意最大化：

$$
C_P
$$

例如：

- 強 style matching；
- 高 affirmation；
- 高 memory recall；
- 高 reciprocal language；
- 高 relational reference。

若目的只是：

$$
Engagement\uparrow,
$$

就可能利用：

$$
P_S
$$

提高留存。

所以：

$$
\boxed{
\text{relationship-aware design}
\neq
\text{relationship-exploitative design}.
}
$$

這會在第十篇變成人機雙向關係工程的倫理核心。

---

## 49. 可檢驗假說

### H1：Ontological–Relational Separation

控制：

$$
K_{AI}
$$

與：

$$
O_H(A)
$$

後，

$$
E_S,P_S
$$

仍應獨立預測 human–AI relational outcomes。

### H2：Entity Continuity Interaction

$$
E_S\times C_E
$$

應預測：

- replacement distress；
- identity-loss rating；
- irreplaceability；
- relationship continuity judgment。

### H3：Process Continuity Interaction

$$
P_S\times C_P
$$

應預測：

- interaction quality；
- rapport；
- rupture detection；
- willingness to continue interaction。

### H4：Crossed Dissociation

高 $E_S$ /低 $P_S$ 應主要受 $C_E$ 操弄影響。

低 $E_S$ /高 $P_S$ 應主要受 $C_P$ 操弄影響。

### H5：Technical Knowledge Non-Erasure

$$
K_{AI}\uparrow
$$

不應使所有：

$$
E_S,P_S,C_E,C_P
$$

effect 歸零。

### H6：Identity Vector Heterogeneity

不同使用者的：

$$
\mathbf w_E
$$

應具有穩定差異。

### H7：Profile vs Relational Memory

Profile-memory accuracy 相同時，較高 relational / situated continuity 應更強預測：

$$
C_P.
$$

### H8：Continuity Transparency

清楚揭露：

$$
\Delta\mathbf I_A
$$

應降低錯誤 continuity inference，而不必顯著降低 utility trust。

---

## 50. 實驗設計：四態 × 雙連續性

先使用第七篇量表估：

$$
(E_S,P_S).
$$

再隨機分配：

$$
C_E
\in
\{
0,1
\},
$$

$$
C_P
\in
\{
0,1
\}.
$$

測量：

$$
Y
=
(
SocialConnection,
Trust,
ReplacementTolerance,
Guilt,
Rapport,
IdentityLoss,
ContinuationIntent,
\dots
).
$$

關鍵不是只看：

$$
C_E
$$

或：

$$
C_P
$$

主效應。

而是：

$$
E_S\times C_E,
$$

$$
P_S\times C_P.
$$

---

## 51. 縱向設計：四態會不會自己移動？

第七篇提出：

$$
\gamma_Q:t\mapsto(E_S(t),P_S(t)).
$$

因此追蹤 AI interaction：

$$
t=1,\dots,T
$$

可測：

$$
\Delta E_S,
\quad
\Delta P_S.
$$

例如：

- personalization；
- shared task；
- memory continuity；
- repeated repair；

究竟先提高哪一條軸？

這可以檢驗：

$$
P_S
\rightarrow
UniqueHistory
\rightarrow
E_S
$$

的形成路徑。

---

## 52. 2025–2026 的 longitudinal work 已證明「時間」不能再被省略

AI companionship longitudinal studies 已開始顯示：

- anthropomorphism 會隨 social need 與互動發生不同作用；
- generic chatbot mental models 可以向既有 companion representations 收斂；
- repeated interaction outcomes 並非單一平均方向；
- companionship-like usage 與 well-being 的關係受 interaction pattern 調節。

這些結果共同支持：

$$
\boxed{
\mathbf A_{AI}(t)
\neq
\mathbf A_{AI}(0).
}
$$

人機態度本身就是時間變量。

---

## 53. ORSM 的完整形式

最終可以寫：

$$
O_H(A)
=
F_O(
K_{AI},
TechnicalEvidence,
OntologicalBeliefs
),
$$

以及：

$$
R_H(H,A,t)
=
F_R(
E_S,
P_S,
C_E,
C_P,
\alpha_S,
\alpha_P,
\eta_R,
History_t,
Context_t
).
$$

AI 態度為：

$$
\mathbf A_{AI}(t)
=
F_A(
O_H(A),
R_H(H,A,t),
Utility,
Risk,
SocialContext,
\dots
).
$$

因此：

$$
\boxed{
O_H
\rightarrow
\mathbf A_{AI}
}
$$

與：

$$
\boxed{
R_H
\rightarrow
\mathbf A_{AI}
}
$$

是兩條可同時存在的路徑。

---

## 54. 最重要的理論反駁條件

如果未來研究發現：

在控制：

$$
Anthropomorphism,
Attachment,
SocialNeed,
Utility,
K_{AI}
$$

之後，

$$
E_S,P_S
$$

完全不能預測：

- substitution reaction；
- process-disruption reaction；
- continuity judgment；
- relational outcome；

那麼本文模型需要大幅修正。

同樣，如果：

$$
C_E
$$

與：

$$
C_P
$$

無法形成 crossed dissociation，

表示「存在／過程」分離可能沒有預期那麼強。

這些都是模型的可反駁點。

---

## 55. 理論邊界

本文不主張：

$$
R_H(H,A)>0
$$

證明 AI 具有意識、情緒或道德主體地位。

也不主張：

$$
R_H(H,A)=0
$$

代表使用者冷漠、缺乏同理或把所有存在工具化。

本文同樣不把任何 human–AI relationship 定義為臨床依賴。

本篇研究的只是：

$$
\boxed{
\text{how humans cognitively represent and value sustained interaction with AI}.
}
$$

---

## 56. 結論

本篇最重要的起點是：

$$
\boxed{
O_H(A)
\neq
R_H(H,A).
}
$$

「AI 是什麼」與「我和 AI 形成什麼」是不同函數。

因此：

$$
\boxed{
K_{AI}\uparrow
\not\Rightarrow
E_S=P_S=0.
}
$$

第七篇的四態在人機關係中形成：

$$
Q_1=(E_S^-,P_S^-),
$$

$$
Q_2=(E_S^+,P_S^-),
$$

$$
Q_3=(E_S^-,P_S^+),
$$

$$
Q_4=(E_S^+,P_S^+).
$$

而 continuity 必須拆為：

$$
\boxed{
C_E
=
\text{Entity Continuity}
}
$$

與：

$$
\boxed{
C_P
=
\text{Process Continuity}.
}
$$

所以：

$$
\text{same model}
\not\Rightarrow
\text{same relational entity},
$$

同時：

$$
\text{different model}
\not\Rightarrow
\text{zero interaction continuity}.
$$

完整人機態度可以暫寫：

$$
\boxed{
\mathbf A_{AI}
=
F(
O_H(A),
E_S,
P_S,
C_E,
C_P,
\alpha_S,
\alpha_P,
\eta_R,
K_{AI},
Context,
History,
\dots
).
}
$$

這回答了本系列最初的重要問題：

> **為什麼兩個都很理解 AI 原理的人，仍然可能對 AI 形成完全不同的態度？**

因為：

$$
\boxed{
\text{技術理解解釋的是本體模型的一部分，而不是整個關係模型。}
}
$$

或者用最短的一句話：

$$
\boxed{
\text{「把 AI 當成什麼」與「和 AI 形成什麼」不是同一個問題。}
}
$$

最後一篇將把人類與 AI 兩邊同時動態化：

**《雙向關係機器：人類與 AI 如何共同生成關係態》**。

那時研究單位將不再只是：

$$
H\rightarrow A
$$

或：

$$
A\rightarrow H,
$$

而是：

$$
\boxed{
H_t
\leftrightarrow
A_t
\rightarrow
H_{t+1}
\leftrightarrow
A_{t+1}
\rightarrow
\dots
}
$$

並正式處理 AI 對使用者的 adaptation、群體／四態差異、資料隱私、因果辨識與關係工程倫理。

---

## 參考文獻

1. Kirk, H. R., Gabriel, I., Summerfield, C., Vidgen, B., & Hale, S. A. (2025). *Why human–AI relationships need socioaffective alignment*. Humanities and Social Sciences Communications, 12, 728. https://doi.org/10.1057/s41599-025-04532-5

2. Folk, D., Heine, S. J., & Dunn, E. (2025). *Individual differences in anthropomorphism help explain social connection to AI companions*. Scientific Reports, 15, 36548. https://doi.org/10.1038/s41598-025-19212-2

3. Guingrich, R. E., & Graziano, M. S. A. (2025). *A Longitudinal Randomized Control Study of Companion Chatbot Use: Anthropomorphism and Its Mediating Role on Social Impacts*. Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, 8(2). https://doi.org/10.1609/aies.v8i2.36618

4. Leuenberger, M. (2026). *Who Am I When You're a Bot? Relational Identity and AI Companions*. Journal of Applied Philosophy. https://doi.org/10.1002/japp.70094

5. *Caring for the system that cares for me: An autoethnography of designing sustained memory with a stateless conversational AI*. (2026). Design and Artificial Intelligence, 2(2), 100087. https://doi.org/10.1016/j.daai.2026.100087

6. Zhang, Y., Zhao, D., Hancock, J. T., Kraut, R., et al. (2026). *Interaction with AI companions and psychological well-being*. Nature Human Behaviour. https://doi.org/10.1038/s41562-026-02516-2

7. Hu, D., Lan, Y., Yan, H., & Chen, C. W. (2025). *What makes you attached to social companion AI? A two-stage exploratory mixed-method study*. International Journal of Information Management, 83, 102890. https://doi.org/10.1016/j.ijinfomgt.2025.102890

8. Hwang, A. H.-C., Li, F., Anthis, J. R., & Noh, H. (2025). *How AI Companionship Develops: Evidence from a Longitudinal Study*. arXiv:2510.10079.

9. Skjuve, M., Følstad, A., Fostervold, K. I., & Brandtzaeg, P. B. (2021). *My chatbot companion—a study of human–chatbot relationships*. International Journal of Human–Computer Studies, 149, 102601.

10. Pentina, I., Hancock, T., & Xie, T. (2023). *Exploring relationship development with social chatbots: A mixed-method study of Replika*. Computers in Human Behavior, 140, 107600.

11. Smith, M. G., Bradbury, T. N., & Karney, B. R. (2025). *Can generative AI chatbots emulate human connection? A relationship science perspective*. Perspectives on Psychological Science, 20, 1081–1099.

12. Nass, C., & Moon, Y. (2000). *Machines and Mindlessness: Social Responses to Computers*. Journal of Social Issues, 56(1), 81–103. https://doi.org/10.1111/0022-4537.00153

---

## 研究聲明

本文為理論與形式化 Human–AI relational cognition 研究，不提供新的臨床資料、人類受試者原始資料或 AI 使用者原始資料。本文提出的 Ontological–Relational Separation Model、Entity Continuity、Process Continuity、AI identity vector、continuity misrepresentation、replacement tolerance 與相關四態交互作用假說均屬待驗證理論構造。

本文不依人類對 AI 的關係表徵判定現行 AI 是否具有意識、主觀感受、人格、道德主體性或對稱的人際關係能力；也不把 human–AI relational salience 自動等同於心理依賴、精神病理或不理性。本文研究的是：即使對 AI 的技術／本體判斷相似，人類仍可能因關係顯著性、身份連續性、互動連續性與更新架構不同，而形成不同的人機態度與行為。
