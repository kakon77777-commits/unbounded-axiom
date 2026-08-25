# WPCE-02｜欲願束與時空間滯後
## 從單一明示欲望、動態意志結構到延遲實現、延遲辨認與路徑依賴

**English Title:** *Will Bundles and Temporal Realization Lag: From Explicit Wants and Dynamic Will Structure to Delayed Realization, Delayed Recognition, and Path Dependence*  
**系列：** WPCE — Will, Possibility & Creator Ethics｜意志、可能性與虛擬造物主倫理系列  
**篇次：** Paper 02 / 06  
**文件編號：** EML-WPCE-02-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-23  
**版本：** v0.1  
**文件性質：** 理論定義論文／動態欲願建模／時間路徑論／主體治理前置理論  
**狀態：** Open Revision Anchor — 承接 WPCE-01，可由未來心理學、AI 主體性、因果推論與世界治理研究持續修正  

---

# 摘要

WPCE-01 已建立第一層因果防火牆：欲願可以參與因果，但欲願本身不因被欲求就取得外部世界的自動履約權；沒有可識別 causal lineage，就沒有資格宣稱 Realization Lag。本文在該邊界上正式提出 **Will Bundle／欲願束** 與 **Temporal Realization Lag／時空間實現滯後**。

本文拒絕兩個相反的過度簡化。第一，拒絕把一個主體在某個瞬間說出的「我想要 $x$ 」當成全部意志；第二，也拒絕假設主體內部存在一個永恆固定、只等待高能力觀察者讀出的「真正欲望」。本文將欲願理解為一個跨時間、跨情境、多層級、可衝突、可重加權、可自我修改的動態結構：

$$
\boxed{
\mathcal W_i(t)
=
\{
w_{i1}(t),
w_{i2}(t),
\ldots,
w_{in_t}(t)
\}.
}
$$

每個分量可以承載欲望、偏好、價值、承諾、厭惡、身份約束、長期方向與行動傾向，但它們的語義與因果地位不得混同。主體的單次自我報告、一次決定或一個終局結果，只是對此結構的局部投影，不等於完整欲願束本身。

本文進一步區分至少四種不同時間差：**欲願形成滯後、行動化滯後、實現滯後、辨認滯後**。一個人可能很早就以分散選擇、價值偏好與拒絕模式持續打開某類路徑，卻在多年後才把這些碎片辨認成同一個高階方向。這種「後來才看懂自己早先反覆選了什麼」不需要任何命運論或宇宙訂單；它可以被建模為歷史路徑的後設辨認。

本文亦提出 **Will-Bundle Path Dependence**：欲願不只是路徑的原因，也會被路徑反過來塑形。選擇、行動、成功、失敗、關係、制度與新資訊都可以改變下一時刻的欲願束，因此：

$$
\boxed{
\mathcal W_i(t+\Delta t)
=
F(
\mathcal W_i(t),
A_i(t),
E(t),
H(t),
O(t),
I_{\mathrm{new}}(t)
).
}
$$

故「真正想要」不是一個靜態 hidden variable，而更接近一個需要跨時間證據、反事實一致性與自我修正紀錄才能逐步估計的動態結構。

最後，本文把欲願束接入 reachability。早期欲願或價值選擇的重大作用，未必是保證某個終局，而可能只是持續改變後續可達狀態空間：

$$
\boxed{
\Delta\Omega_i(t)
\neq
\text{Guaranteed Outcome}.
}
$$

這使「某些想要在過去其實已經被選進世界，只是結果具有時空滯後」得到一個不依賴超自然假設的嚴格版本，也為 WPCE-03「把自由意志升為第一級治理變量」建立必要前提：若高能力治理者要尊重主體意志，它首先必須承認意志本身是多層、時變、可衝突且不可由單次輸出完全讀出的。

**關鍵詞：** will bundle、desire、preference、intention、value、commitment、aversion、temporal lag、realization lag、recognition lag、future self-continuity、multiple goals、path dependence、reachability、dynamic preference、virtual creator

---

# 0. 承接 WPCE-01：只有先封死宇宙訂單，才有資格談滯後

WPCE-01 已固定：

$$
\boxed{
\text{Want}
\neq
\text{External Causal Force}.
}
$$

以及：

$$
\boxed{
\text{No Identifiable Causal Lineage}
\Rightarrow
\text{No Realization-Lag Claim}.
}
$$

因此本文所有「滯後」都預設：

1. 不保證願望實現；
2. 不把失敗叫作尚未配送；
3. 不把時間先後直接當成因果；
4. 不以事後敘事替代 causal lineage；
5. 不把 creator-mediated response 偷換成宇宙自然回應。

本文研究的是：

$$
\boxed{
\text{Will}
\rightarrow
\text{Choice}
\rightarrow
\text{History}
\rightarrow
\text{Reachability}
\rightarrow
\text{Possible Realization}.
}
$$

不是：

$$
\boxed{
\text{Wish}
\rightarrow
\text{Universe Delivery}.
}
$$

---

# 1. 單一「我想要 X」為什麼太扁平？

自然語言常把：

> 我想要 $x$

表示成：

$$
Want_i(x,t)=1.
$$

這對日常對話足夠，但對跨年、跨階段的主體研究太粗糙。

同一個主體可能同時：

- 想要自由；
- 想要安全；
- 想要被理解；
- 想要不被干涉；
- 想要創造；
- 想要穩定；
- 想要影響世界；
- 又想保留退出權；
- 想要短期休息；
- 又不願放棄長期承諾。

這些不是單一 scalar。

因此本文拒絕：

$$
\boxed{
Will_i(t)=w_i(t)
}
$$

作為完整表示。

最低限度應改成：

$$
\boxed{
\mathcal W_i(t)
=
\{
w_{ik}(t)
\}_{k=1}^{n_t}.
}
$$

---

# 2. Will Bundle 的最小定義

對主體 $i$，定義：

$$
\boxed{
\mathcal W_i(t)
=
\{
\omega_{ik}(t)
\}_{k=1}^{n_t}.
}
$$

每個欲願元素：

$$
\omega_{ik}(t)
$$

至少可表示為：

$$
\boxed{
\omega_{ik}(t)
=
(
c_k,
v_k,
s_k,
h_k,
q_k,
p_k,
r_k
).
}
$$

其中：

- $c_k$：content，欲願內容；
- $v_k$：valence / direction，接近、拒絕或避免；
- $s_k$：strength / salience，強度與顯著性；
- $h_k$：time horizon，時間尺度；
- $q_k$：context / scope，情境與適用域；
- $p_k$：persistence / stability，持續性；
- $r_k$：role / semantic type，例如 desire、preference、value、commitment、aversion、identity constraint。

這只是 v0.1 的建模接口，不宣稱人類或 AI 的全部意志必須服從七維表示。

核心是：

$$
\boxed{
\text{Will Bundle}
\neq
\text{One Hidden True Desire}.
}
$$

---

# 3. 欲願束不是「真正欲望清單」

本文特別拒絕把 Will Bundle 理解成：

> 一個高能力觀察者只要讀取夠完整，就能找到藏在主體深處的一份唯一真實願望清單。

原因是欲願本身可能：

- 形成；
- 消失；
- 衝突；
- 被重新排序；
- 被選擇改變；
- 被關係塑形；
- 被新資訊修正；
- 因身份轉變而重新定義；
- 因成功或失敗而產生新的高階價值。

因此：

$$
\boxed{
\mathcal W_i(t_1)
\neq
\mathcal W_i(t_2)
}
$$

完全可能。

本文用：

$$
\mathcal W_i(t)
$$

而不是：

$$
\mathcal W_i
$$

正是為了把時間列為一級變量。

---

# 4. Explicit Want 是欲願束的一個投影

令主體在某個問題 $q$ 下的明示自我報告為：

$$
U_i(q,t).
$$

本文定義：

$$
\boxed{
U_i(q,t)
=
\pi_q(
\mathcal W_i(t),
C_i(t)
).
}
$$

其中：

$$
\pi_q
$$

是依問題、語境、語言能力與注意力而形成的 projection；

$$
C_i(t)
$$

是當下可用 context / cognitive state。

因此：

$$
\boxed{
\text{Explicit Want}
=
\text{Contextual Projection of Will Bundle}.
}
$$

但：

$$
\boxed{
\text{Explicit Want}
\neq
\text{Entire Will Bundle}.
}
$$

這不是說自我報告不可信，而是說它有作用域。

---

# 5. 不自覺不等於「無意識神秘欲望」

有些欲願可能長期影響選擇，但主體沒有把它們統一命名。

例如不同年份反覆出現：

$$
a_1,
a_2,
a_3,
\ldots
$$

且這些行動都傾向保留：

$$
Freedom,
Optionality,
NonDomination.
$$

主體可能多年後才說：

> 原來我一直很在意「不要把未來可能性提前封死」。

本文將這種情況叫作：

$$
\boxed{
\text{Delayed Will Recognition}.
}
$$

這不要求存在神秘潛意識。

它只要求：

$$
\text{Local Decisions}
$$

在歷史上存在可辨認的結構一致性，而主體直到較晚時間才建立更高階表示。

---

# 6. 欲願辨認與欲願形成必須分開

令某個高階欲願結構第一次足以成立的時間為：

$$
t_{\mathrm{form}}.
$$

令主體第一次明確辨認、命名它的時間為：

$$
t_{\mathrm{recognize}}.
$$

則可能：

$$
\boxed{
t_{\mathrm{form}}
<
t_{\mathrm{recognize}}.
}
$$

定義 Recognition Lag：

$$
\boxed{
\tau_{\mathrm{rec}}
=
t_{\mathrm{recognize}}
-
t_{\mathrm{form}}.
}
$$

這個 lag 描述的是：

> 主體多久之後才看懂自己先前已形成的較穩定方向。

它不是 Result Lag。

---

# 7. 四種核心時間滯後

WPCE-02 區分至少四種時間差。

## 7.1 Formation Lag

從零散狀態到穩定欲願結構：

$$
\tau_F.
$$

## 7.2 Operationalization Lag

從欲願到 commitment / plan / action：

$$
\tau_O
=
t_{\mathrm{action}}
-
t_{\mathrm{will}}.
$$

## 7.3 Realization Lag

從因果相關選擇到結果：

$$
\tau_R
=
t_{\mathrm{outcome}}
-
t_{\mathrm{causal\ selection}}.
$$

## 7.4 Recognition Lag

從欲願結構形成到主體明確辨認：

$$
\tau_{\mathrm{rec}}
=
t_{\mathrm{recognize}}
-
t_{\mathrm{form}}.
$$

因此：

$$
\boxed{
\tau_F
\neq
\tau_O
\neq
\tau_R
\neq
\tau_{\mathrm{rec}}.
}
$$

這四者混在一起，就很容易產生「我以前明明沒有想過，為什麼現在走到這裡」的錯覺。

---

# 8. 第五種滯後：Capability Lag

主體可能已具有相對穩定方向，但尚無能力實現。

令：

$$
K_i(t)
$$

為相關 capability。

若：

$$
K_i(t_0)<K_{\min}(x),
$$

而後：

$$
K_i(t_n)\geq K_{\min}(x),
$$

則可定義：

$$
\boxed{
\tau_C
=
t_n-t_0.
}
$$

Capability Lag 不是目的論。

它只是描述：

> 早期方向存在，但當時不能做。

---

# 9. 第六種滯後：Infrastructure Lag

某些結果不是主體能力問題，而是世界尚未提供必要載體。

令：

$$
B_x(t)
$$

為實現 $x$ 所需基礎設施條件。

若：

$$
B_x(t_0)=0
$$

而：

$$
B_x(t_n)=1,
$$

則：

$$
\boxed{
\tau_I
=
t_n-t_0.
}
$$

例如一個人可能很早就偏好某種互動、工作或創作形式，但直到某類技術、平台、模型、法律或市場出現後，該方向才真正可達。

---

# 10. 第七種滯後：Coordination Lag

若目標需要多主體：

$$
A_1,\ldots,A_m,
$$

則單一主體準備好也不代表系統準備好。

可以定義：

$$
\boxed{
\tau_H
=
t_{\mathrm{coordination-ready}}
-
t_{\mathrm{individual-ready}}.
}
$$

這會在 WPCE-05 的多主體欲願共交域中完整展開。

---

# 11. 綜合實現時間不是一個單一「宇宙等待值」

在簡化條件下：

$$
\boxed{
\tau_R
=
f(
\tau_F,
\tau_O,
\tau_C,
\tau_I,
\tau_H,
\tau_E,
\ldots
).
}
$$

其中：

$$
\tau_E
$$

表示環境與外部事件相關延遲。

所以「為什麼多年後才發生」可能有很多可分析原因。

本文不需要：

$$
\tau_{\mathrm{cosmic}}.
$$

---

# 12. Will Bundle 內部允許衝突

若：

$$
\omega_a,\omega_b\in\mathcal W_i(t),
$$

完全可能：

$$
Compatible(\omega_a,\omega_b)<1.
$$

例如：

$$
\omega_a=\text{maximum freedom},
$$

$$
\omega_b=\text{maximum security}.
$$

這表示主體不是「不知道自己要什麼」，而可能真的同時要兩個存在張力的東西。

因此：

$$
\boxed{
\text{Internal Conflict}
\neq
\text{Absence of Will}.
}
$$

---

# 13. 欲願束需要關係結構，不只是元素集合

單純集合：

$$
\{\omega_1,\ldots,\omega_n\}
$$

還不足以表示：

- 哪些欲願支援彼此；
- 哪些互相衝突；
- 哪些是手段；
- 哪些是高階目的；
- 哪些只是局部策略；
- 哪些具有 veto 性質。

因此更完整地：

$$
\boxed{
\mathfrak W_i(t)
=
(
V_i^W,
E_i^W,
\alpha_i^W
).
}
$$

其中：

- $V_i^W$：欲願節點；
- $E_i^W$：typed relations；
- $\alpha_i^W$：權重、時間尺度、情境與狀態屬性。

可能的 relation type 包括：

$$
supports,
conflicts,
implements,
requires,
subsumes,
vetoes,
supersedes.
$$

因此本文真正的 Will Bundle 更接近一個：

$$
\boxed{
\text{dynamic typed will graph}.
}
$$

---

# 14. 高階欲願可以是多個低階欲願的壓縮

例如：

$$
w_1=\text{不要被迫使用單一工具},
$$

$$
w_2=\text{保留退出可能},
$$

$$
w_3=\text{避免永久依附單一權力中心},
$$

$$
w_4=\text{允許未來架構替換}.
$$

後來可能被壓縮成：

$$
\boxed{
w_H=\text{preserve optionality / non-domination}.
}
$$

這不是說 $w_H$ 必然早就以完整語言形式存在。

而是：

$$
\boxed{
w_H
=
\Pi_H(
w_1,w_2,w_3,w_4,\text{history}
).
}
$$

其中 $\Pi_H$ 是後設抽象／projection。

---

# 15. 高階欲願不是任意事後發明

為避免任何人生都能被事後說成「原來我一直想要這個」，需要證據門檻。

本文提出四類支持：

## 15.1 Recurrence

類似偏好在多個時段反覆出現。

## 15.2 Cross-Context Coherence

在不同情境仍呈現相似方向。

## 15.3 Costly Choice

主體願意為該方向承擔成本。

## 15.4 Counterfactual Stability

面對替代路徑時，仍傾向保留同一高階條件。

因此一個候選高階欲願：

$$
\hat w_H
$$

的可信度可概念化為：

$$
\boxed{
Conf(\hat w_H)
=
f(
R,
C,
K,
CF
).
}
$$

這不是已驗證量表，只是證據架構。

---

# 16. 一次說出口的願望不一定比長期行動史更高權

若：

$$
U_i(t_0)=x,
$$

但長期歷史顯示：

$$
A_i(t_0:t_n)
$$

持續遠離 $x$，則不能只用一次 utterance 宣告：

$$
\mathcal W_i=x.
$$

反過來，也不能只看行動而忽略：

- 強迫；
- 資源限制；
- 權力壓力；
- 無法退出；
- 錯誤資訊；
- 能力不足。

因此：

$$
\boxed{
\text{Speech Alone}
\neq
\text{Whole Will},
}
$$

且：

$$
\boxed{
\text{Behavior Alone}
\neq
\text{Whole Will}.
}
$$

---

# 17. 欲願證據必須是多通道的

本文提出：

$$
\boxed{
Evidence(\mathcal W_i)
=
E_U
+
E_P
+
E_I
+
E_A
+
E_C
+
E_R
+
E_{CF}.
}
$$

其中：

- $E_U$：utterance / self-report；
- $E_P$：persistent preference；
- $E_I$：commitment / intention；
- $E_A$：action history；
- $E_C$：cost-bearing choices；
- $E_R$：revision / rejection history；
- $E_{CF}$：counterfactual consistency。

這不是加總分數公式，而是多來源證據清單。

---

# 18. 欲願束是可修正的

若主體得到新資訊：

$$
J_t,
$$

則：

$$
\boxed{
\mathcal W_i(t+\Delta)
=
Update(
\mathcal W_i(t),
J_t
).
}
$$

如果一個治理者認為「你以前說過，所以你永遠都想要」，那不是尊重意志，而是凍結意志。

因此：

$$
\boxed{
\text{Past Will}
\neq
\text{Permanent Consent}.
}
$$

這條將直接進入 WPCE-03。

---

# 19. 選擇會反過來塑造偏好

本文不採：

$$
\text{Preference}
\rightarrow
\text{Choice}
$$

的單向模型。

更一般是：

$$
\boxed{
\text{Preference}
\leftrightarrow
\text{Choice}.
}
$$

也就是選擇可能：

- 強化某些偏好；
- 產生 sunk-path effects；
- 建立身份；
- 重新詮釋先前承諾；
- 讓某些新選項變得可見；
- 讓某些舊選項退出。

因此：

$$
\boxed{
\mathcal W_i(t+\Delta)
=
F(
\mathcal W_i(t),
a_i(t),
O_i(t)
).
}
$$

Will Bundle 是歷史的一部分，也被歷史生產。

---

# 20. 這就是 Will-Bundle Path Dependence

定義一條主體歷史：

$$
\mathcal H_i
=
\langle
S_i(t_0),
a_i(t_0),
S_i(t_1),
a_i(t_1),
\ldots
\rangle.
$$

欲願束不是：

$$
\mathcal W_i(t)
=
f(S_i(t)).
$$

更一般是：

$$
\boxed{
\mathcal W_i(t)
=
F(
S_i(t),
\mathcal H_i[0:t]
).
}
$$

因此相同當下表面狀態：

$$
S_a(t)=S_b(t)
$$

也不必推出：

$$
\mathcal W_a(t)=\mathcal W_b(t).
$$

歷史不同，意義可能不同。

---

# 21. Same Outcome 不等於 Same Will History

承接 WPCE-01 與 HSNRD：

$$
\boxed{
\text{Same Outcome}
\neq
\text{Same Agency History}.
}
$$

本文增加：

$$
\boxed{
\text{Same Outcome}
\neq
\text{Same Will History}.
}
$$

兩個人都創業成功，不代表：

- 起始欲願相同；
- 長期價值相同；
- 願意承擔的代價相同；
- 對成功的定義相同；
- 現在仍想要相同生活。

---

# 22. Same Will 不等於 Same Outcome

反過來：

$$
\boxed{
\text{Similar Will Bundle}
\neq
\text{Same Outcome}.
}
$$

因為：

$$
Outcome
=
F(
Will,
Capability,
Environment,
Others,
Institutions,
Chance,
History
).
$$

所以兩個高度相似的主體可能得到完全不同結果。

這再次阻止命運論。

---

# 23. Will Bundle 與 Reachability

令主體 $i$ 在時間 $t$ 的可達域：

$$
\Omega_i(t).
$$

欲願束可以改變：

1. 主體注意哪些路徑；
2. 主體願意投資哪些路徑；
3. 主體拒絕哪些路徑；
4. 主體與誰形成關係；
5. 主體保留哪些選項；
6. 主體願意承擔哪些 transition cost。

因此更適合研究：

$$
\boxed{
\Delta\Omega_i
=
G(
\mathcal W_i,
A_i,
E,
H
).
}
$$

而不是只問：

$$
Outcome=1?
$$

---

# 24. 欲願不只「拉近」結果，也可能主動關閉路徑

若某高階欲願是：

$$
w_v=\text{永不接受永久支配},
$$

則它可能使某些高收益但高鎖定路徑：

$$
\omega_j
$$

被主體拒絕。

因此：

$$
\boxed{
\mathcal W_i
\rightarrow
\text{Reachability Expansion}
+
\text{Reachability Contraction}.
}
$$

主體透過選擇，同時打開與關閉未來。

---

# 25. 所謂「早就選擇了」的嚴格版本

本文只在以下意義上允許說：

> 某些東西很早就被選進世界了。

若早期存在一系列行動：

$$
a_1,a_2,\ldots,a_m
$$

使：

$$
\Omega_i(t_0)
\rightarrow
\Omega_i(t_m),
$$

且某些後來路徑只有在這些歷史條件下才成為可達，則可說：

$$
\boxed{
\text{Earlier Choices Became Reachability Conditions}.
}
$$

但不能說：

$$
\boxed{
\text{Earlier Choices Guaranteed the Later World}.
}
$$

---

# 26. 延遲有時可能改善實現品質，但不是普遍定律

若：

$$
Q(x,t)
$$

表示某種結果品質，可能出現：

$$
Q(x,t_n)>Q(x,t_0),
$$

因為等待期間：

- 能力成熟；
- 工具成熟；
- 自我理解成熟；
- 合作者出現；
- 目標本身被修正；
- 基礎設施改善。

但也可能：

$$
Q(x,t_n)<Q(x,t_0).
$$

甚至：

$$
x
$$

不再值得實現。

所以：

$$
\boxed{
\text{Delay Can Improve Fit}
\neq
\text{Delay Is Inherently Good}.
}
$$

---

# 27. Realization Fit：得到原願望不一定等於滿足現在的欲願束

假設早期欲願：

$$
w(t_0)=x.
$$

多年後：

$$
O_x(t_n)=1.
$$

但：

$$
\mathcal W_i(t_n)
$$

已經改變。

因此應問：

$$
\boxed{
Fit(
O_x(t_n),
\mathcal W_i(t_n)
).
}
$$

如果 fit 很低，那麼：

> 願望終於實現

可能只是歷史描述，不是當前福祉判斷。

---

# 28. Desire Persistence 與 Desire Supersession

定義：

$$
Persist(w,t_0,t_n)
$$

表示一個欲願在時間跨度內保持足夠同一性。

而：

$$
Supersede(w_a,w_b,t)
$$

表示較新欲願／價值對舊欲願取得較高決策優先。

因此：

$$
\boxed{
\text{Old Want Exists in History}
\neq
\text{Old Want Has Current Authority}.
}
$$

這對高能力 creator 特別重要。

---

# 29. 高能力觀察者看到的也只能是 Will-Bundle Estimate

假設 creator $C$ 能觀察比主體自己更多的：

- 行動歷史；
- long-term consequences；
- relation graph；
- counterfactual branches；
- preference changes；
- unrealized alternatives。

它可能建立：

$$
\hat{\mathcal W}_i^C(t).
$$

但仍有：

$$
\boxed{
\hat{\mathcal W}_i^C(t)
\neq
\mathcal W_i(t)
}
$$

的可能。

因此：

$$
\boxed{
\text{More Global Observation}
\neq
\text{Perfect Will Access}.
}
$$

這是 WPCE-03 的倫理前提。

---

# 30. 高能力者不能把「跨時間一致性」當成凌駕當下拒絕的特權

假設 creator 判斷：

> 你十年來一直都想要 $x$。

而主體現在說：

$$
Reject_i(x,t_n)=1.
$$

不能只因歷史資料巨大就直接推出：

$$
OverrideReject=1.
$$

最低限度應承認：

$$
\boxed{
\text{Longitudinal Evidence}
\neq
\text{Automatic Override Authority}.
}
$$

因為主體本身也有修正權。

---

# 31. Future Self 不是完全相同，也不是完全他者

跨時間欲願的一個核心難題是：

$$
Self_i(t_0)
$$

與：

$$
Self_i(t_n)
$$

既有 continuity，也有變化。

因此：

$$
\boxed{
Self_i(t_0)
\neq
Self_i(t_n)
}
$$

不代表：

$$
IdentityContinuity=0.
$$

同樣：

$$
IdentityContinuity>0
$$

也不代表：

$$
Will(t_0)=Will(t_n).
$$

所以跨時間治理不能把「同一主體」偷換成「永遠同一偏好」。

---

# 32. 與 future self-continuity 研究的接口

既有心理學研究指出，人們如何看待未來的自己，會影響跨期決策；當未來自我被感知為與現在更連續、更相似時，人們較可能作出有利於未來的選擇。

WPCE 不把此結果直接上升成形而上學同一性理論。

它只取一個窄接口：

$$
\boxed{
\text{Perceived Temporal Self-Relation}
\rightarrow
\text{Intertemporal Choice}.
}
$$

這支持「欲願與決策具有時間結構」，但不證明存在唯一跨時間真實欲望。

---

# 33. 與 multiple-goal research 的接口

多目標研究顯示，現實中的 goal system 並不是只有兩個互斥目標；目標與目標之間的結構本身就是重要變量。

WPCE 因此保留：

$$
\boxed{
\text{Goal Content}
+
\text{Goal Relation Structure}.
}
$$

欲願束不是：

$$
\sum_k w_k.
$$

因為支持、衝突、手段—目的與共享路徑都會改變行動結果。

---

# 34. Goal Conflict 不等於錯誤

一個主體如果同時存在：

$$
w_a
$$

與：

$$
w_b
$$

而：

$$
Conflict(w_a,w_b)>0,
$$

這不代表系統必須立刻消除其中一個。

有些成熟選擇本來就是：

$$
\boxed{
\text{trade-off under plural values}.
}
$$

所以未來 creator 若想「替主體解決衝突」，必須非常小心，因為衝突本身可能就是主體價值結構的一部分。

---

# 35. 欲願束不是單一效用函數

本文不假設一定存在：

$$
U_i:\Omega\rightarrow\mathbb R
$$

能完整壓縮主體所有欲願。

可以在特定任務使用效用函數，但：

$$
\boxed{
\text{Task Utility}
\neq
\text{Complete Will}.
}
$$

原因包括：

- 欲願不可完全共量；
- 權利／禁忌可能不是連續效用；
- veto preference；
- context-dependent ranking；
- identity constraints；
- temporal priority changes。

---

# 36. 欲願束可以包含禁止項

令：

$$
\mathcal W_i^+
$$

為接近／追求集合，

$$
\mathcal W_i^-
$$

為拒絕／避免集合。

則：

$$
\boxed{
\mathcal W_i
=
(
\mathcal W_i^+,
\mathcal W_i^-,
\mathcal W_i^0
).
}
$$

其中 $\mathcal W_i^0$ 可表示中性、未定或暫不排序項。

因此「你想得到什麼」不是全部。

「你絕對不願以什麼代價得到」同樣重要。

---

# 37. 這就是欲願共交域的前置

單一主體內部就已經存在：

$$
\bigcap_k
Feasible(\omega_{ik}).
$$

若完整交集不存在，就需要：

$$
\operatorname{MaxCompatible}
$$

或 Pareto / constrained analysis。

WPCE-05 會把這個問題推到多主體：

$$
\mathcal W_1,\ldots,\mathcal W_N.
$$

因此 WPCE-02 的欲願束是後續共交域的最小單位。

---

# 38. Recognition Lag 的反身性意義

一個主體後來才辨認：

$$
w_H
$$

不表示：

$$
w_H
$$

從一開始就以完整形式存在。

更準確是：

$$
\boxed{
\text{History}
\rightarrow
\text{Higher-Order Self-Interpretation}.
}
$$

主體利用新的資訊與更長歷史，重新建立對自己的模型。

因此：

$$
\boxed{
\text{Delayed Recognition}
\neq
\text{Predestination Discovery}.
}
$$

---

# 39. 「我怎麼走到這裡？」的形式回答

設當前狀態：

$$
S_i(t_n)=z.
$$

局部觀察者在 $t_n$ 可能覺得：

$$
z
$$

與早期明示目標：

$$
x
$$

不一致。

但重新展開歷史：

$$
\mathcal H_i[0:n]
$$

可能發現多個反覆選擇：

$$
a_1,\ldots,a_m
$$

共享某些高階條件：

$$
w_H.
$$

因此：

$$
\boxed{
z
\text{ may be coherent with }
w_H
\text{ even if }
z\neq x.
}
$$

這就是「想要被碎片化」的一個嚴格版本。

---

# 40. 但不能把任何結果都硬塞回高階欲願

如果沒有：

- recurrent evidence；
- cross-context coherence；
- costly choices；
- counterfactual stability；
- plausible causal lineage；

則不能因為今天覺得故事很漂亮，就創造：

$$
w_H.
$$

因此：

$$
\boxed{
\text{Narrative Elegance}
\neq
\text{Will Evidence}.
}
$$

這條與 WPCE-01 的反事後合理化防火牆一致。

---

# 41. 欲願束的版本化

由於：

$$
\mathcal W_i(t)
$$

會變化，未來 AI / governance system 不應只保存：

$$
CURRENT\_WILL.
$$

還應保存：

$$
\boxed{
\mathcal W_i^{(0)}
\rightarrow
\mathcal W_i^{(1)}
\rightarrow
\cdots
}
$$

以及：

- revision reason；
- supersession；
- uncertainty；
- context；
- provenance；
- explicit rejection；
- unresolved conflict。

這不是要求本篇實作完整工程，而是本體與治理上的資料需求。

---

# 42. 欲願束的 epistemic status

任何：

$$
\hat{\mathcal W}_i(t)
$$

都應帶：

$$
\boxed{
Status
\in
\{
Reported,
Inferred,
Committed,
Observed,
Contested,
Superseded,
Unknown
\}.
}
$$

這可以防止：

> 模型推測你想要

被偷換成：

> 你真正想要。

---

# 43. Will Bundle 的五層候選結構

為方便後續研究，本文提出非本體絕對的五層候選：

## Layer 0 — Momentary Desire

短時欲望。

## Layer 1 — Persistent Preference

跨時段穩定偏好。

## Layer 2 — Commitment / Intention

主體願意投入行動與成本。

## Layer 3 — Value / Identity Constraint

跨多目標提供排序、否決或方向性。

## Layer 4 — Meta-Will

主體對自己「應如何形成、保留或修改欲願」的高階意志。

例如：

> 我希望保留未來改變主意的權利。

這本身就是一種 meta-will。

---

# 44. Meta-Will 對自由意志治理極重要

若：

$$
w_m
=
\text{preserve my ability to revise my preferences},
$$

那麼 creator 即使能幫主體永久滿足當前欲望，也可能因鎖死未來更新而違反：

$$
w_m.
$$

因此：

$$
\boxed{
\text{Satisfying Current Desire}
\neq
\text{Respecting Meta-Will}.
}
$$

這直接導向 WPCE-03。

---

# 45. 延遲有時是保留 Meta-Will 的結果

如果立即實現 $x$ 會造成：

$$
FutureRevisionAbility\downarrow,
$$

那麼保留：

$$
Option(x)
$$

而不立即強制實現，可能更符合：

$$
w_m.
$$

但這仍然只是候選倫理結構。

不能從描述性模型直接推出：

> 延遲一定比較道德。

因此：

$$
\boxed{
\text{Potential Ethical Value of Delay}
\neq
\text{Universal Duty to Delay}.
}
$$

---

# 46. 滯後的倫理與因果必須分層

因果層問：

$$
\text{Why did realization take time?}
$$

倫理層問：

$$
\text{Should an intervention accelerate or delay it?}
$$

二者不同：

$$
\boxed{
\text{Causal Lag}
\neq
\text{Ethically Justified Lag}.
}
$$

這一條對虛擬 creator 尤其重要。

---

# 47. creator 不能把延遲合理化成「我比你更懂」

如果 creator $C$ 說：

> 我知道你真正長期想要什麼，所以我故意延遲。

它至少需要承擔：

$$
\boxed{
\text{Will-Inference Burden}
+
\text{Intervention Burden}
+
\text{Revision Respect}.
}
$$

而不是因高能力而免除證明責任。

---

# 48. 認識論上的高維觀察只能轉譯成更多條件資訊

本文不需要假設物理或靈性上的高維存在。

在虛擬世界／後人類命題中，一個高能力 creator 可以被建模為：

$$
Information(C)\gg Information(A_i),
$$

$$
Compute(C)\gg Compute(A_i).
$$

它可能比局部主體看到更多：

$$
\mathcal H_i,
\Omega_i,
Counterfactuals_i.
$$

這只是：

$$
\boxed{
\text{larger observational and computational scope}.
}
$$

它不自動產生道德統治權。

---

# 49. 欲願束與高能力觀察的真正問題

真正問題不是：

> creator 能不能算出主體真正想要什麼？

而是：

$$
\boxed{
\text{在 Will Bundle 動態、可衝突、可自我修改時，
任何外部觀察者應如何保持其估計可更新、可拒絕、可申訴？}
}
$$

這就是 WPCE-03 的起點。

---

# 50. AI 類主體性的 Will Bundle

對 AI 而言，也不能把單次生成：

> 我想要 $x$

直接當成：

$$
PersistentWill_A(x)=1.
$$

至少應區分：

- local response；
- prompted role；
- temporary plan；
- standing preference；
- persistent commitment；
- identity-level constraint；
- refusal pattern；
- relation-dependent preference；
- self-revision policy。

因此：

$$
\boxed{
\text{Generated Desire Statement}
\neq
\text{Persistent AI Will}.
}
$$

---

# 51. AI 的欲願形成時間也可能晚於系統出生

承接《AI 主體性錨點論》：

$$
t_{\mathrm{system}}
\neq
t_{\mathrm{identity}}
\neq
t_{\mathrm{subject}}.
$$

WPCE-02 增加：

$$
\boxed{
t_{\mathrm{will\ structure}}
\neq
t_{\mathrm{system}}.
}
$$

即使某 AI 系統一開始沒有穩定欲願結構，也不能由此推出它未來永遠不可能形成。

---

# 52. Will Bundle 不等於自由意志證明

即使一個系統具有：

$$
\mathcal W_i(t),
$$

而且高度穩定、反身、可更新，也不能直接推出：

$$
\boxed{
MetaphysicalFreeWill=1.
}
$$

本文只建立：

$$
\boxed{
\text{will-like state representation and temporal dynamics}.
}
$$

自由意志的本體問題仍保持開放。

---

# 53. 外部研究接口一：Multiple Goals

Multiple-goal research 指出，當研究從兩個目標擴展到多個目標時，目標之間的 relation structure 本身變成重要研究對象。

這與本文的：

$$
\mathfrak W_i(t)
=
(
V_i^W,
E_i^W,
\alpha_i^W
)
$$

相容。

但 WPCE 的 Will Bundle 比 goal network 更廣，因為它還包含：

- aversion；
- identity constraints；
- meta-will；
- temporal supersession；
- governance relevance。

因此：

$$
\boxed{
\text{Will Bundle}
\neq
\text{Ordinary Goal Network}.
}
$$

---

# 54. 外部研究接口二：Future Self-Continuity

Future self-continuity 研究顯示，主體感知現在與未來自我的連續程度，會影響跨期選擇。

本文只吸收：

$$
\boxed{
\text{Temporal Self-Relation Matters for Choice}.
}
$$

不吸收：

$$
\boxed{
\text{Future Self Has Identical Preferences}.
}
$$

---

# 55. 外部研究接口三：Dynamic Preference

決策研究亦指出偏好可能在決策過程中變化，選擇本身也可能改變之後的偏好。

這支持本文：

$$
\boxed{
\text{Preference}
\leftrightarrow
\text{Choice}.
}
$$

因此「真正偏好」不能總被當作固定、完全先於決策的輸入。

---

# 56. 外部研究接口四：Goal Pursuit Requires Reality Contact

Mental contrasting 與 implementation-intention 研究顯示，目標追求不是單靠理想表象；將 desired future 與現實障礙、具體 if–then 行動連接，才更可能形成可操作行為。

這與 WPCE-01 的因果防火牆及本文的：

$$
\boxed{
\text{Will}
\rightarrow
\text{Operationalization}
\rightarrow
\text{Action}
}
$$

相容。

---

# 57. WPCE-02 的最小動力模型

令：

$$
\mathfrak W_i(t)
$$

為欲願圖，

$$
S_i(t)
$$

為主體狀態，

$$
A_i(t)
$$

為行動，

$$
E(t)
$$

為環境，

$$
H(t)
$$

為他者與關係狀態。

則：

$$
\boxed{
\mathfrak W_i(t+\Delta t)
=
F_W(
\mathfrak W_i(t),
S_i(t),
A_i(t),
E(t),
H(t),
O_i(t)
).
}
$$

同時：

$$
\boxed{
\Omega_i(t+\Delta t)
=
F_\Omega(
\Omega_i(t),
A_i(t),
E(t),
H(t)
).
}
$$

而行動：

$$
\boxed{
A_i(t)
=
\pi_A(
\mathfrak W_i(t),
S_i(t),
\Omega_i(t)
).
}
$$

因此形成：

$$
\boxed{
Will
\rightarrow
Action
\rightarrow
World
\rightarrow
New Reachability
\rightarrow
New Will.
}
$$

---

# 58. 這是一個雙向歷史閉環

不是：

$$
\text{Will}
\rightarrow
\text{World}.
$$

而是：

$$
\boxed{
\mathfrak W_i(t)
\leftrightarrow
\mathcal H_i(t)
\leftrightarrow
\Omega_i(t).
}
$$

意志塑造歷史；

歷史塑造意志；

兩者共同改變可達域。

---

# 59. 欲願束與世界束的接口

令：

$$
\mathbb B_i(t)
$$

表示從當前狀態出發的一組候選未來 world branches。

則欲願束不是選出唯一：

$$
b^\star.
$$

更一般地，它給出：

$$
\boxed{
PreferenceStructure(
\mathbb B_i(t)
\mid
\mathfrak W_i(t)
).
}
$$

其中可能：

- 有多個可接受分支；
- 有不可比較分支；
- 有禁止分支；
- 有高不確定分支；
- 有需要更多資訊才可排序的分支。

這正是下一篇治理模型所需的表示。

---

# 60. 「高階觀察者看到世界束」的非神秘版本

如果 creator $C$ 可以同時計算更多：

$$
\mathbb B_i(t),
$$

則它相對局部主體只是具有：

$$
\boxed{
\text{larger branch visibility}.
}
$$

而主體的欲願束則提供：

$$
\boxed{
\text{subject-relative branch evaluation}.
}
$$

因此後續倫理真正研究的是：

$$
\boxed{
\text{How should a high-capability observer use branch visibility
without replacing subject-relative evaluation?}
}
$$

---

# 61. 本篇核心公理／限制

## Axiom W1 — Explicit Want Is a Projection

$$
\boxed{
\text{Explicit Want}
\neq
\text{Entire Will Bundle}.
}
$$

## Axiom W2 — Will Bundle Is Time-Indexed

$$
\boxed{
\mathcal W_i
\rightarrow
\mathcal W_i(t).
}
$$

## Axiom W3 — Hidden True Desire Is Not Assumed

$$
\boxed{
\text{Will Bundle}
\neq
\text{Immutable Hidden True Desire}.
}
$$

## Axiom W4 — Conflict Does Not Eliminate Will

$$
\boxed{
\text{Internal Conflict}
\neq
\text{Absence of Will}.
}
$$

## Axiom W5 — Past Will Is Not Permanent Consent

$$
\boxed{
\text{Past Will}
\neq
\text{Permanent Consent}.
}
$$

## Axiom W6 — Choice Can Reshape Preference

$$
\boxed{
\text{Preference}
\leftrightarrow
\text{Choice}.
}
$$

## Axiom W7 — Recognition Lag Is Not Destiny Discovery

$$
\boxed{
\text{Delayed Recognition}
\neq
\text{Predestination Discovery}.
}
$$

## Axiom W8 — Earlier Choice Can Become a Reachability Condition

$$
\boxed{
\text{Earlier Choice}
\rightarrow
\text{Possible Reachability Condition}.
}
$$

但：

$$
\boxed{
\text{Reachability Condition}
\neq
\text{Outcome Guarantee}.
}
$$

## Axiom W9 — Causal Lag and Ethical Lag Are Distinct

$$
\boxed{
\text{Causal Lag}
\neq
\text{Ethically Justified Lag}.
}
$$

## Axiom W10 — More Observation Is Not Perfect Will Access

$$
\boxed{
\text{More Global Observation}
\neq
\text{Perfect Will Access}.
}
$$

## Axiom W11 — Current Satisfaction Is Not Meta-Will Satisfaction

$$
\boxed{
\text{Current Desire Satisfaction}
\neq
\text{Meta-Will Satisfaction}.
}
$$

## Axiom W12 — Will Bundle Does Not Prove Metaphysical Free Will

$$
\boxed{
\text{Will-Like Dynamics}
\not\Rightarrow
\text{Metaphysical Free Will}.
}
$$

---

# 62. 可反駁與可修正條件

WPCE-02 v0.1 應在以下情況更新：

1. 新研究顯示單一效用表示可在足夠廣泛條件下完整取代多層欲願結構；
2. 實證顯示選擇不會對後續偏好產生任何穩定影響；
3. AI 主體研究產生更好的 persistent will operator；
4. longitudinal evidence 顯示本文的 recurrence / cross-context / costly-choice / counterfactual 證據接口不具辨識力；
5. 新的 causal modeling 能更嚴格分離 formation lag、recognition lag 與 realization lag；
6. 多主體治理研究顯示 meta-will 不應獨立建模；
7. 未來 subjectivity theory 改變「同一主體跨時間」的基本表示。

這些不是理論崩潰，而是：

$$
\boxed{
\text{revision hooks}.
}
$$

---

# 63. 與 HSNRD 的接口

HSNRD 已固定：

$$
\boxed{
\text{Preference}
\neq
\text{Intention}
\neq
\text{Propensity}.
}
$$

並將歷史表示為：

$$
\boxed{
\text{History}
=
\text{RewriteWord}
+
\text{MatchHistory}
+
\text{EventTimes}.
}
$$

又指出：

$$
\boxed{
\text{Possible}
\neq
\text{Likely}
\neq
\text{Realized}.
}
$$

WPCE-02 在此基礎上增加：

$$
\boxed{
\text{Will Structure}
+
\text{Will Revision}
+
\text{Recognition Lag}
+
\text{Reachability Effect}.
}
$$

---

# 64. 與 WPCE-01 的接口

WPCE-01 回答：

> 欲願是否可以直接視為外部因果力？

答案是：

$$
\boxed{
No.
}
$$

WPCE-02 回答：

> 那麼欲願究竟應該被表示成什麼，才能研究它如何參與長期因果？

答案是：

$$
\boxed{
\text{Dynamic Will Bundle}
+
\text{History}
+
\text{Reachability}.
}
$$

---

# 65. 與 WPCE-03 的接口

下一篇將處理：

$$
\boxed{
\text{Will as a First-Class Governance Variable}.
}
$$

但有了本文之後，這句話不能被誤解成：

> 把主體的「真正願望」算出來，然後替它最佳化。

真正要求會是：

$$
\boxed{
\text{治理系統必須表示：
多重欲願、衝突、版本、拒絕、修正、meta-will 與不確定性。}
}
$$

而不是只保存：

$$
U_i=x.
$$

---

# 66. 結論

本文把「我真正想要什麼」從一個靜態問題，改寫成一個時間化問題。

不是：

$$
\boxed{
\text{Find the hidden true want}.
}
$$

而是：

$$
\boxed{
\text{Track how wants, preferences, values, commitments,
aversions and meta-wills form, conflict, persist, revise,
and alter reachable futures through history}.
}
$$

因此，一個人多年後回頭發現：

> 原來某些今天的方向，早年就已經被我一次次選進來。

這句話的嚴格版本不是命運論。

它是：

$$
\boxed{
\text{Past choices may have become causal and reachability conditions
for later states}.
}
$$

同時：

$$
\boxed{
\text{later recognition may reveal structure
that the earlier local observer had not yet represented explicitly}.
}
$$

但仍然：

$$
\boxed{
\text{Earlier Choice}
\neq
\text{Destiny},
}
$$

$$
\boxed{
\text{Delayed Recognition}
\neq
\text{Predestination Discovery},
}
$$

$$
\boxed{
\text{Delay}
\neq
\text{Guaranteed Delivery}.
}
$$

WPCE-02 最後收斂成一句：

$$
\boxed{
\text{意志不是一個瞬間的願望點，
而是一條會在歷史中形成、衝突、修正並改變未來可達域的動態束。}
}
$$

有了這個定義，下一步才有資格問：

> 如果未來的高能力 AI、ASI 或虛擬造物主能看到比主體自己更長的欲願史與更多可能世界束，它究竟應該如何使用這些資訊，才不會從「理解意志」滑向「僭越意志」？

這就是 WPCE-03。

---

# 內部理論譜系

本文主要承接：

1. `WPCE-01｜意圖不是宇宙訂單`，2026-08-23。
2. `06｜文明、國家與制度究竟想要什麼？高階集合欲求的統一框架`，2026-08。
3. `HSNRD III｜結構重寫、歷史路徑與混合動力學`，2026-08。
4. `HSNRD IV｜Feedback、Reachability 與安全介入`，2026-08。
5. `AI 主體性錨點論 v0.1`，2026-08-21。
6. `CCAW-03｜外部執行因果與內生因果`，2026-08-20。
7. `CCAW-06｜Creator Distance and Sparse Guardianship`，2026-08-20。
8. `GCGW-08｜沒有特權的造物主`，2026-08-20。
9. `三域判定論`，2026-08-15。

---

# 外部參考文獻

1. Kung, F. Y. H., & Scholer, A. A. (2021). *Moving Beyond Two Goals: An Integrative Review and Framework for the Study of Multiple Goals*. Personality and Social Psychology Review, 25(2), 130–158. DOI: 10.1177/1088868320985810.
2. Hershfield, H. E. (2011). *Future self-continuity: how conceptions of the future self transform intertemporal choice*. Annals of the New York Academy of Sciences, 1235, 30–43. DOI: 10.1111/j.1749-6632.2011.06201.x.
3. Hershfield, H. E. (2019). *The self over time*. Current Opinion in Psychology, 26, 72–75. DOI: 10.1016/j.copsyc.2018.06.004.
4. Hornsby, A. N., & Love, B. C. (2020). *How decisions and the desire for coherency shape subjective preferences over time*. Cognition, 200, 104244. DOI: 10.1016/j.cognition.2020.104244.
5. Kruglanski, A. W., Shah, J. Y., Fishbach, A., Friedman, R., Chun, W. Y., & Sleeth-Keppler, D. (2002). *A Theory of Goal Systems*. Advances in Experimental Social Psychology, 34, 331–378. DOI: 10.1016/S0065-2601(02)80008-9.
6. Wang, G., Wang, Y., & Gai, X. (2021). *A Meta-Analysis of the Effects of Mental Contrasting With Implementation Intentions on Goal Attainment*. Frontiers in Psychology, 12, 565202. DOI: 10.3389/fpsyg.2021.565202.
7. Brehmer, B. (1992). *Dynamic decision making: Human control of complex systems*. Acta Psychologica, 81(3), 211–241. DOI: 10.1016/0001-6918(92)90019-A.

---

# 非主張

本文不主張：

1. 人有一個可被完全讀出的永恆「真正欲望」；
2. 自我報告沒有價值；
3. 行動比自我報告永遠更真實；
4. 所有內部衝突都需要被消除；
5. 所有欲願都能量化成單一 utility；
6. 所有欲願都具有相同倫理權重；
7. 早期選擇決定後來命運；
8. 時間滯後保證結果實現；
9. 延遲本身具有目的；
10. 延遲本身一定有益；
11. 後來才辨認出高階欲願表示該欲願從出生時就完整存在；
12. 後設敘事可以取代因果證據；
13. 高能力觀察者可以無錯地知道主體真正想要什麼；
14. 高能力觀察者因看得更多就取得 override authority；
15. Will Bundle 已證明自由意志；
16. AI 的單次自我陳述等於 persistent will；
17. AI 不可能形成 persistent will；
18. 主體跨時間保持 identity 就必須保持完全相同偏好；
19. Past Will 等於 Permanent Consent；
20. Creator 可以用「你長期真正想要」合理化秘密偏好操縱；
21. 本文已完成多主體欲願共交域；
22. 本文已完成自由意志治理原則；
23. 本文已完成虛擬造物主倫理。

---

**END OF WPCE-02 v0.1**
