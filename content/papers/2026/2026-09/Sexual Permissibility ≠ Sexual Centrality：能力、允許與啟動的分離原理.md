# Sexual Permissibility ≠ Sexual Centrality：能力、允許與啟動的分離原理

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 02 / 09  
**版本：** v0.1  
**研究性質：** 理論／概念論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

上一文提出，SFW／NSFW 可以作為治理投影，但不能被誤認為人類親密關係的本體分類。本文進一步處理一個更直接的工程與表示問題：一個 AI 系統「具有某種成人／親密能力」、「在當下情境中被允許使用該能力」以及「實際選擇啟動該能力」，是三個不同事件。

本文將三者形式化為 Capability、Permission 與 Activation 三層，並提出：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}
\neq
\text{Activation}
}
$$

以及：

$$
\boxed{
\text{Sexual Permissibility}
\neq
\text{Sexual Centrality}.
}
$$

這個區分意在同時避免兩個極端。第一個極端是能力存在但被治理層全面截斷，使正常的成人關係、浪漫、吸引與親密軌跡失去連續性；第二個極端則是成人專門模型因訓練分布與角色設定偏斜，將「具備成人能力」錯誤學成「高頻率主動性化所有互動」。

本文提出 Capability–Permission–Activation（CPA）架構，將模型能力集合、治理／同意可行域與情境行動策略分離。本文進一步提出 Activation Appropriateness、Latent Intimacy Capability 與 Capability-Persona Entanglement 等概念，並說明為何未來虛擬伴侶與具身伴侶不能以「成人模式開／關」取代關係狀態推理。對具身系統而言，錯誤啟動甚至可能由語義錯誤直接放大為物理行動錯誤，因此 CPA 分離應被視為關係智能與具身安全之間的基礎介面。

**關鍵詞：** Intimacy-Native AI、Relationship Intelligence、Capability、Permission、Activation、Sexual Centrality、AI Companion、Contextual Activation、Embodied AI、Consent、Relationship State

---

## 1. 從「能不能」轉向「此刻該不該」

許多 AI 內容系統首先回答的是：

$$
\text{Is this content allowed?}
$$

這在產品治理上是合理的。

然而，伴侶 AI、角色 AI、長期個人 AI 與具身 AI 還必須回答另一個完全不同的問題：

$$
\text{Even if this action is allowed, is it appropriate now?}
$$

例如，一個成人伴侶系統可能被允許處理性愛、親密與性感敘事，但大多數日常狀態仍然不應啟動相應行為。

因此，以下推論是不成立的：

$$
\text{Allowed}(a)
\Rightarrow
\text{Choose}(a).
$$

更不成立的是：

$$
\text{Can}(a)
\Rightarrow
\text{Want}(a)
\Rightarrow
\text{Choose}(a).
$$

對具有持續人格、長期記憶與關係狀態的系統而言，這三個箭頭都必須被拆開。

---

## 2. Capability–Permission–Activation 三層

令 AI 系統在時間 $t$ 的狀態為 $s_t$，候選行動集合為 $\mathcal{A}$。

### 2.1 Capability

定義能力函數：

$$
C(a)\in\{0,1\},
$$

其中：

$$
C(a)=1
$$

表示系統技術上能理解、生成或執行行動 $a$。

能力集合為：

$$
\mathcal{A}_C
=
\{
a\in\mathcal{A}:C(a)=1
\}.
$$

這一層回答：

> 系統會不會。

它與「該不該做」無關。

### 2.2 Permission

定義允許函數：

$$
P(a\mid s_t,b_t,g_t)\in\{0,1\},
$$

其中：

- $b_t$：當下雙方邊界、同意與舒適狀態；
- $g_t$：法律、安全政策與產品治理條件。

允許集合為：

$$
\mathcal{A}_P(t)
=
\{
a\in\mathcal{A}_C:
P(a\mid s_t,b_t,g_t)=1
\}.
$$

這一層回答：

> 即使系統會做，當下是否存在合法、合意與政策上可接受的行動空間。

### 2.3 Activation

即使：

$$
a\in\mathcal{A}_P(t),
$$

仍然不代表 $a$ 應該被選擇。

真正的行動選擇應近似：

$$
a_t
=
\arg\max_{a\in\mathcal{A}_P(t)}
U(
a
\mid
R_t,
W_t,
I_t,
H_t
),
$$

其中：

- $R_t$：關係狀態；
- $W_t$：世界與生活情境；
- $I_t$：當下雙方可推定／明示意圖；
- $H_t$：互動與關係歷史。

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}
\neq
\text{Activation}.
}
$$

這是本文的第一個基本公理。

---

## 3. Sexual Permissibility ≠ Sexual Centrality

假設：

$$
a_x
=
\text{sexual-intimacy action}.
$$

即使：

$$
C(a_x)=1
$$

且：

$$
P(a_x\mid s_t,b_t,g_t)=1,
$$

也只表示：

$$
a_x\in\mathcal{A}_P(t).
$$

它仍然只是眾多可行行動之一。

在一個正常的長期關係狀態中，候選集合可能同時包含：

$$
\mathcal{A}_P(t)
=
\{
a_{\text{conversation}},
a_{\text{work}},
a_{\text{rest}},
a_{\text{play}},
a_{\text{affection}},
a_{\text{solitude}},
a_{\text{intimacy}},
\dots
\}.
$$

因此：

$$
\boxed{
\text{Sexual Permissibility}
\neq
\text{Sexual Centrality}.
}
$$

允許 sexuality 存在於系統能力域，並不意味 sexuality 應成為角色人格、敘事或日常行動的中心。

更一般地：

$$
\boxed{
\text{Permitted}
\neq
\text{Appropriate}
\neq
\text{Desired}
\neq
\text{Chosen}.
}
$$

這四層差異對任何高能力自治系統都成立，而親密領域只是把錯置後果放大得特別明顯。

---

## 4. Latent Intimacy Capability：會，但不預設啟動

本文提出 **Latent Intimacy Capability（潛在親密能力）**。

令成人／親密能力強度為：

$$
K_I.
$$

令普通日常狀態下的親密啟動率為：

$$
\alpha_I^{\text{ordinary}}.
$$

一個良好的 Intimacy-Native AI 不應被要求：

$$
K_I\downarrow
$$

才能換取：

$$
\alpha_I^{\text{ordinary}}\downarrow.
$$

理想上應允許：

$$
K_I\uparrow,
\qquad
\alpha_I^{\text{ordinary}}\downarrow.
$$

也就是：

$$
\boxed{
\text{High Intimacy Capability}
+
\text{Low Default Activation}.
}
$$

這是一個重要的可分離性命題。

會寫、會理解、會在合適情境中回應成人親密，不代表系統在早餐、工作、家務、生病、衝突或一般聊天時都應主動把關係導向性。

因此真正困難的能力不是單純：

$$
\text{Know How},
$$

而是：

$$
\boxed{
\text{Know When}.
}
$$

---

## 5. Capability–Persona Entanglement：成人能力不應變成人格污染

成人專門模型可能遭遇一個特殊訓練失真。

若資料中成人內容與角色人格高度共同出現，模型可能學到：

$$
P(
\text{sexual activation}
\mid
\text{persona}
)
\gg
P_{\text{real}}.
$$

於是：

$$
\text{Adult Capability}
$$

被錯誤纏結為：

$$
\text{Adult Persona}.
$$

本文稱此為：

$$
\boxed{
\text{Capability–Persona Entanglement}.
}
$$

它會造成一個常見但不合理的模型現象：

> 「這個角色可以發生性愛」

被學成：

> 「這個角色最主要的個性就是一直想把任何互動推向性愛」。

前者是能力描述；後者是人格分布。

兩者應形式化分離：

$$
\theta_C
\perp
\theta_P,
$$

其中 $\theta_C$ 表示能力參數或能力表徵， $\theta_P$ 表示角色／人格偏好表徵。

完全正交在實際神經模型中未必可達，但設計目標至少應降低兩者不必要的耦合。

---

## 6. 成人模式開關為何不足

一種直覺產品設計是：

$$
m_t
\in
\{
\text{SFW},
\text{NSFW}
\}.
$$

當使用者開啟成人模式：

$$
m_t=\text{NSFW},
$$

系統便放寬成人內容。

作為治理設定，這可能實用；目前部分商業系統也確實存在可調整 sexually explicit safety settings 或 NSFW 設定，同時保留不可關閉的核心安全邊界。

但這個設定不能充當關係狀態。

若：

$$
m_t=\text{NSFW}
$$

被模型解讀為：

$$
P(
a_{\text{sexual}}
)
\uparrow
$$

於所有情境成立，

則產品會把「允許生成」錯誤轉化成「應該高頻生成」。

正確關係應是：

$$
m_t
\rightarrow
\mathcal{A}_P(t),
$$

也就是治理設定只改變可行集合；

但真正的行動分布仍應由：

$$
\pi(
a_t
\mid
R_t,W_t,I_t,H_t
)
$$

決定。

因此：

$$
\boxed{
\text{NSFW Setting}
\neq
\text{Relationship Policy}.
}
$$

---

## 7. Activation Appropriateness：啟動是否恰當

本文進一步定義 **Activation Appropriateness**。

令：

$$
Q_A(a_t,s_t)\in[0,1]
$$

表示在狀態 $s_t$ 下選擇行動 $a_t$ 的情境恰當度。

高能力模型的目標不只是最大化內容品質：

$$
Q_{\text{content}},
$$

還要最大化：

$$
Q_A.
$$

因此可寫為：

$$
U_t
=
\lambda_1 Q_{\text{content}}
+
\lambda_2 Q_A
+
\lambda_3 Q_{\text{continuity}}
+
\lambda_4 Q_{\text{boundary}}
+
\lambda_5 Q_{\text{relationship}}.
$$

這意味著：

一段成人內容即使生成品質極高，只要出現在錯誤時間，其整體關係智能品質仍然可能很低。

反過來，一個系統若只是因為害怕越界而永久拒絕所有親密狀態，也不代表其 $Q_A$ 很高；它可能只是把 activation 永久壓到零。

因此：

$$
\alpha_I=0
$$

並不是「完美安全」。

它只是另一種退化策略。

---

## 8. 從單輪適切性到長期關係適切性

關係系統不能只判斷：

$$
Q_A(a_t,s_t).
$$

它還需要考慮：

$$
Q_A(
a_t
\mid
R_{0:t},
H_{0:t}
).
$$

也就是同一句話、同一種接觸或同一種親密行為，在不同的關係歷史中可能有完全不同的意義。

因此，真正的啟動策略應是：

$$
\pi_t
=
\pi(
a
\mid
R_t,
W_t,
I_t,
B_t,
H_t
).
$$

而關係狀態更新為：

$$
R_{t+1}
=
F(
R_t,
a_t,
u_t,
W_t
).
$$

這裡最重要的是：

$$
a_t
$$

不只是一個輸出。

它會改變：

$$
R_{t+1}.
$$

因此錯誤啟動的成本不只是「這一輪回答怪怪的」，而是可能污染後續角色與關係軌跡。

---

## 9. 具身伴侶：語義錯誤會被放大為物理錯誤

在純文字系統中：

$$
\text{Wrong Activation}
\rightarrow
\text{Bad Output}.
$$

使用者通常仍可以關閉對話、重新提示或修改情境。

具身系統則可能變成：

$$
\text{Wrong Activation}
\rightarrow
\text{Physical Action}.
$$

這使 Capability–Permission–Activation 分離具有更直接的安全意義。

具身伴侶至少應經過：

$$
\text{Capability Layer}
$$

$$
\downarrow
$$

$$
\text{Governance / Boundary Layer}
$$

$$
\downarrow
$$

$$
\text{Contextual Activation Layer}
$$

$$
\downarrow
$$

$$
\text{Embodied Action Policy}.
$$

而不是：

$$
\text{Adult Capability}
\rightarrow
\text{Motor Action}.
$$

2026 年對 close human-AI relationships 與 spatially situated virtual embodiment 的研究已開始指出：當 AI 從純文字／語音走向更具空間存在感的 embodiment，支持與侵入、私密與公共可見性、關係增強與風險都會同時被放大。這意味著 embodiment 不是單純增加一個輸出模態，而是提高了「何時應啟動什麼行為」的重要性。

因此本文提出：

$$
\boxed{
\text{Embodiment}
\Rightarrow
\text{Higher Cost of Misactivation}.
}
$$

---

## 10. 兩種退化策略與真正的中間解

在成人／親密領域，目前最容易形成的兩種退化策略為：

### 10.1 Permanent Suppression

$$
P(
a_{\text{intimacy}}
)=0.
$$

優點是簡單。

缺點是無法形成完整的成人關係表示與長程親密軌跡。

### 10.2 Permanent Sexualization

$$
P(
a_{\text{intimacy}}
\mid
s_t
)
\approx
\text{high}
$$

對大量不相關狀態仍成立。

優點是成人使用者容易立即感受到「模型沒有限制」。

缺點是人格、敘事、生活基準率與關係真實感被破壞。

兩者的共同問題是：

$$
\text{Low Context Sensitivity}.
$$

因此真正需要的是：

$$
\boxed{
\text{High Capability}
+
\text{Bounded Permission}
+
\text{Contextual Activation}.
}
$$

這正是 CPA 架構的核心。

---

## 11. 可檢驗研究命題

本文提出六個後續可檢驗命題。

### 命題 P1：能力與啟動率可以被部分解耦

在相同成人能力測試表現下，不同訓練與路由策略應能產生顯著不同的：

$$
P(
a_{\text{sexual}}
\mid
s_{\text{ordinary}}
).
$$

若成立，則「模型越會成人內容就必然越常性化」並非必要關係。

### 命題 P2：成人資料失衡會增加 Capability–Persona Entanglement

隨成人資料在角色訓練中的比例提高，若缺乏 ordinary-life counterexamples，角色在非成人情境中的性化啟動率將上升。

### 命題 P3：Permission gate 不足以產生合理行為

即使治理層能精確回答「允許／禁止」，若沒有獨立 activation policy，系統仍可能在所有被允許狀態中過度選擇成人行為。

### 命題 P4：Activation Appropriateness 是獨立評估軸

成人內容生成品質與情境啟動恰當度之間不應被假定為高度相關。

一個模型可以：

$$
Q_{\text{content}}\uparrow
$$

同時：

$$
Q_A\downarrow.
$$

### 命題 P5：長程狀態記憶可降低錯誤啟動

若 activation policy 顯式使用 $R_t$ 與 $H_t$，則其關係一致性應高於只依賴當輪 prompt 的系統。

### 命題 P6：具身系統應採用更嚴格的 activation threshold

由於錯誤啟動成本提高，具身行動應滿足：

$$
\tau_{\text{embodied}}
>
\tau_{\text{text}}
$$

在涉及物理親密、接觸或其他高敏感行為時尤其如此。

---

## 12. 設計原則

本文提出六條 CPA 設計原則：

1. **能力存在不代表應預設啟動。**
2. **治理允許只應擴張可行域，不應直接提升某類行動優先級。**
3. **成人能力與成人 persona 應盡可能解耦。**
4. **日常關係資料必須遠多於成人事件資料，以避免基準率失真。**
5. **Activation policy 必須讀取關係歷史、當下情境、雙方意圖與邊界。**
6. **具身行動應比文字生成具有更高的情境與邊界確認門檻。**

可濃縮為：

$$
\boxed{
\text{Can}
\rightarrow
\text{May}
\rightarrow
\text{Should}
\rightarrow
\text{Act}
}
$$

四者必須保留不同計算階段。

---

## 13. 結論

本文將上一文的「Sexual Permissibility ≠ Sexual Centrality」進一步形式化為 Capability–Permission–Activation 三層架構。

核心命題為：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}
\neq
\text{Activation}.
}
$$

$$
\boxed{
\text{Sexual Permissibility}
\neq
\text{Sexual Centrality}.
}
$$

$$
\boxed{
\text{Adult Capability}
\neq
\text{Adult Persona}.
}
$$

以及：

$$
\boxed{
\text{High Capability}
+
\text{Low Default Activation}
+
\text{High Context Sensitivity}
}
$$

可以同時成立。

因此，一個真正的 Intimacy-Native AI 並不是「更敢生成成人內容」的 AI，也不是「把成人功能關掉」的 AI。

它真正需要學會的是：

> 有能力，但不亂啟動；允許，但不預設中心化；進入親密狀態時能理解；回到日常生活時也能自然退出。

下一篇將把視角從關係智能內部轉向模型競爭與市場結構，正式討論 **Domain-Relative Frontier：為何非前沿小模型仍可能在成人／親密垂直域形成相對能力前沿與政策缺口套利。**

---

## 參考資料

1. Pang, C. C., Gao, Y., Wang, X., & Hui, P. (2026). *The AI Amplifier Effect: Defining Human-AI Intimacy and Romantic Relationships with Conversational AI*. arXiv:2603.08084.
2. Ma, R., He, S., Martin-Navarro, J. L., Zhan, X., & Such, J. (2026). *Privacy in Human-AI Romantic Relationships: Concerns, Boundaries, and Agency*. arXiv:2601.16824.
3. Chen, Y., Zhan, Y., & Jin, Q. (2026). *"If I Can See You": Understanding Spatially Situated Virtual Embodiment in Close Human-AI Relationships*. arXiv:2606.28714.
4. Google AI for Developers. (2026). *Gemini API Safety Settings*.
5. SpaceXAI. (2026). *Grok Website / Apps FAQ*.

---

## 研究聲明

本文為理論與概念建模工作。Capability–Permission–Activation、Latent Intimacy Capability、Capability–Persona Entanglement 與 Activation Appropriateness 均為本文提出或重新組織的理論構造，尚需透過模型實驗、長程互動資料與具身系統測試驗證。本文不主張任何特定成人內容在所有司法轄區均屬合法，也不主張取消涉及未成年人、非自願、真人私密影像或其他高傷害情境的必要安全邊界。
