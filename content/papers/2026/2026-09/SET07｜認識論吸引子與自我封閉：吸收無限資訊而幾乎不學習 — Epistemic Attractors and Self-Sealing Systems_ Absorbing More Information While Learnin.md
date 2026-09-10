# SET07｜認識論吸引子與自我封閉：吸收無限資訊而幾乎不學習
## Epistemic Attractors and Self-Sealing Systems: Absorbing More Information While Learning Almost Nothing

**定位：** Selective Truth and Epistemic Topology / Foundation Paper 07 / Series Closure  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Epistemology / Belief Revision / Dynamical Systems Metaphor / Self-Sealing Beliefs / Philosophy of Science / Misinformation Correction / Epistemic Resilience

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不針對任何特定人物、政治陣營、宗教、哲學學派、科學學派、數學學派、媒體、企業或 AI 系統。

本文使用 **epistemic attractor** 作為一個可操作的動力學比喻與研究框架，不宣稱人類 belief system 在神經或物理層面必然是一個數學意義上的 dynamical attractor。本文所稱 self-sealing 也不是二元人格標籤，而是相對於特定 evidence class、revision rule、time horizon 與 decision domain 的結構性性質。

本文承接 SET01 至 SET06，特別是：

$$
\boxed{
\text{Sincerity}
\not\Rightarrow
\text{Epistemic Neutrality}
}
$$

$$
\boxed{
\text{A worldview is not exhausted by its node set}
}
$$

以及：

$$
\boxed{
\text{Node Truth}
\not\Rightarrow
\text{Topological Truth}
}
$$

SET07 的收束問題是：

$$
\boxed{
\text{What happens when a system can absorb counterevidence without granting it revision power?}
}
$$

---

# 摘要

一個 belief system 不必拒絕新資訊才會自我封閉。更穩定的封閉形式是：新 evidence 可以大量進入，卻被重新分類為例外、噪音、特殊條件、方法缺陷、來源問題、語義誤會、輔助假說需求或尚待研究的 anomaly，使核心命題與核心 relation topology 幾乎不需改變。此時系統表面上資訊量持續增加，概念與文獻愈來愈豐富，內部也可能發生大量局部修訂，但真正具鑑別力的 learning 近乎停滯。

心理學的 belief-perseverance、subtyping、differential evaluation 與 belief-consistent information processing 文獻已描述若干相近機制。Oeberst 與 Imhoff 2023 的整合框架特別指出，不一致資訊可以透過 subtyping 被移入「例外」類別，也可以因不同評價標準而降低對原 belief 的威脅。然而，2019 年 Anglin 的四項研究提供重要反方：在其研究條件下，人們面對清楚、方向一致的反態度實證時通常會更新，而不是普遍維持或極化原 belief。2025 年 Sanna 與 Lagnado 也發現，在 source reliability 被清楚呈現時，參與者可以合理地折減錯誤資訊並更新信念。這表示 self-sealing 不能被當成人類認知的普遍預設。

哲學上，Boudry 2024 以 **epistemic black holes** 描述某些 equipped-with-immunization 的 belief systems；但 Hagen 2026 提出重要反駁：利用 auxiliary hypotheses 或 modification 逃離單一反證並不是某一類信念的專屬缺陷，科學理論也會如此。Lakatos 的 research programme 更早就系統化了 hard core、protective belt、positive heuristic 與 progressive / degenerating problem shifts。由此可得：**保護核心本身不是病態；關鍵在於保護之後是否增加可檢驗內容、承擔新的預測風險，還是只降低反證的殺傷力。**

本文因此提出 **Epistemic Attractor Framework（EAF）**。令 belief state 為：

$$
\mathcal B_t
=
(V_t,E_t,\tau_t,\omega_t,\pi_t,\Phi_t)
$$

新 evidence batch 為：

$$
X_t.
$$

更新為：

$$
\mathcal B_{t+1}
=
\Phi_t(\mathcal B_t,X_t).
$$

若對一組具有高 discriminative pressure 的 evidence sequences，系統雖能擴張 nodes、auxiliaries 與 local explanations，卻反覆返回某一核心狀態鄰域：

$$
d_{\mathrm{core}}
(
\mathcal B_{t+1},
\mathcal B_t
)
\approx0,
$$

且 predictive / discriminative performance 沒有相應改善，則可視為 **candidate epistemic attractor**。

本文不以單一總分判定封閉，而建立 **Epistemic Attractor Profile（EAP）**：

$$
\mathrm{EAP}
=
\langle
\mathrm{DP},
\mathrm{CR},
\mathrm{AG},
\mathrm{NRE},
\mathrm{ESR},
\mathrm{PG},
\mathrm{EC}
\rangle
$$

其中分別代表 Discriminative Pressure、Core Revision、Auxiliary Growth、Novel Risk Exposure、Exception Sink Rate、Predictive Gain 與 Escape Capacity。

本文提出的核心劃界是：

$$
\boxed{
\text{Healthy resilience}
\neq
\text{Self-sealing resilience}
}
$$

較健康的理論可以暫時保護核心，但必須以新增獨立可測預測、提高鑑別力或最終核心修訂為代價；self-sealing system 則主要增加解釋彈性，使更多可能觀察結果都與核心相容。

本文最後提出 **Epistemic Attractor Stress Protocol（EASP）**，要求事前 revision threshold、rival-topology construction、exception audit、auxiliary independence test、novel-risk accounting、out-of-sample prediction 與 core-exit test。

系列最終命題為：

$$
\boxed{
\text{A system does not learn merely because it absorbs information}
}
$$

以及：

$$
\boxed{
\text{The decisive question is whether new information can change what the system is allowed to become}
}
$$

---

# 0　最危險的封閉系統，不是「什麼都不聽」

最容易辨識的封閉者說：

> 我不看。

這種系統的缺陷很明顯。

更難辨識的系統會說：

> 我看了。

> 我知道這篇研究。

> 我也承認這個反例。

> 但它只是特殊情況。

> 那篇方法有侷限。

> 這個現象不適用於真正的理論版本。

> 這反而證明系統比想像中複雜。

於是：

$$
X_t
$$

完整進入。

甚至：

$$
|V_{t+1}|
>
|V_t|.
$$

但核心仍是：

$$
\mathcal C_{t+1}
\approx
\mathcal C_t.
$$

這就是 SET07 的真正研究對象：

$$
\boxed{
\text{high information absorption with low discriminative learning}
}
$$

---

# 1　資料變多，不等於學習變多

令 cumulative information intake：

$$
I_T
=
\sum_{t=1}^{T}
I(X_t).
$$

若只看資料庫大小，一個系統可以：

$$
I_T
\to
\text{large}.
$$

但 learning 至少還應包含：

- belief calibration；
- predictive improvement；
- topology revision；
- uncertainty reduction；
- discrimination among rival models；
- removal of failed commitments。

因此資料吸收：

$$
I_T
$$

不能直接代表：

$$
L_T.
$$

本文提出：

$$
\boxed{
\text{information accumulation}
\neq
\text{epistemic learning}
}
$$

---

# 2　核心與外圍必須分開

若只用：

$$
d(\mathcal B_{t+1},\mathcal B_t)
$$

量 belief change，可能被大量 peripheral change 欺騙。

例如：

- 新增十篇引用；
- 增加五個例外類；
- 新增三個 auxiliary hypotheses；
- 改寫術語；
- 加入新的解釋分支。

整體 graph edit distance 可能很大。

但真正核心：

$$
\mathcal C_t
$$

完全不動。

所以定義投影：

$$
P_{\mathrm{core}}
:
\mathcal B
\mapsto
\mathcal C.
$$

並觀察：

$$
d_{\mathrm{core}}
(
P_{\mathrm{core}}(\mathcal B_{t+1}),
P_{\mathrm{core}}(\mathcal B_t)
).
$$

這比「全文改了很多」更能測量核心 revision。

---

# 3　什麼叫 epistemic attractor？

令 belief-state space 為：

$$
\mathfrak S.
$$

一個核心狀態區域：

$$
\mathcal A
\subset
\mathfrak S.
$$

若存在 neighborhood：

$$
U(\mathcal A)
$$

使對某一明確定義的 evidence class：

$$
\mathcal X^{*},
$$

系統從：

$$
\mathcal B_0
\in
U(\mathcal A)
$$

出發後，在多種 evidence sequences 下仍反覆停留或返回：

$$
U(\mathcal A),
$$

則稱 $\mathcal A$ 為 candidate epistemic attractor。

形式上：

$$
X_t\in\mathcal X^{*}
$$

且：

$$
\mathcal B_{t+1}
=
\Phi_t(\mathcal B_t,X_t)
$$

仍滿足：

$$
d_{\mathrm{core}}
(
\mathcal B_{t+1},
\mathcal A
)
\leq
\epsilon.
$$

這只是 operational analogy。

它不宣稱 belief dynamics 必然具有 classical dynamical-system attractor 的全部數學性質。

---

# 4　反證如何被吸收：Exception Sink

Oeberst 與 Imhoff 的 belief-consistent information processing framework 整合了多種偏差機制。

其中一個與 SET07 特別相關的是：

$$
\text{subtyping}.
$$

也就是把 belief-inconsistent case 重新放入：

$$
\text{exception category}.
$$

例如核心 belief：

$$
H.
$$

遇到：

$$
x
$$

不符合 $H$。

系統不是修改：

$$
H,
$$

而是新增：

$$
C_x=\text{special exception}.
$$

使：

$$
H\mid\neg C_x
$$

繼續存活。

單次這樣做可能完全合理。

問題在：

$$
C_{x_1},
C_{x_2},
\ldots,
C_{x_n}
$$

持續增長，而核心仍不承擔新的 discriminative risk。

---

# 5　Exception 不是原罪

科學中本來就存在：

- boundary conditions；
- measurement failures；
- heterogeneous populations；
- regime changes；
- exceptions；
- model domains。

所以：

$$
\text{exception}
\not\Rightarrow
\text{immunization}.
$$

真正需要問：

1. exception 是否事前有獨立理由？
2. exception 是否可被獨立測量？
3. exception 是否產生新的 prediction？
4. exception class 是否不斷擴張？
5. exception 是否只在反證出現後被新增？
6. exception 是否降低 theory exposure 而不提高 explanation discrimination？

---

# 6　Exception Sink Rate

令高鑑別力 counterevidence 集合：

$$
X^{-}
=
\{x_1,\ldots,x_n\}.
$$

若其中：

$$
k
$$

項被重新分類為：

- exception；
- irrelevant；
- noisy；
- invalid source；
- special case；

且核心不改，

定義啟發式：

$$
\mathrm{ESR}
=
\frac{k}{n}.
$$

高 ESR 不自動證明 self-sealing。

但若同時：

$$
\mathrm{CR}\approx0
$$

與：

$$
\mathrm{NRE}\approx0,
$$

風險顯著上升。

---

# 7　Differential Evaluation：同樣標準嗎？

belief-consistent information processing 也可能透過不同 evidence criteria 保護核心。

若：

$$
e^{+}
$$

支持核心，

$$
e^{-}
$$

反對核心。

控制 study quality 後仍有：

$$
w(e^{+})
\gg
w(e^{-}),
$$

系統就可以吸收 $e^{-}$ 的存在，卻不讓它取得 revision power。

這與 SET04 的 Counterevidence Weight Ratio 直接接軌。

---

# 8　Belief perseverance 並不是普遍宿命

這是 SET07 必須保留的最重要反方之一。

Anglin 2019 的四項研究發現，在宗教、政治、死刑與槍枝議題等條件中，參與者面對方向一致的反態度實證時會隨 evidence 更新；即使有時對研究品質評價存在偏差，整體 belief change 仍然發生。

因此不能寫：

$$
\text{counterevidence}
\Rightarrow
\text{perseverance}.
$$

較合理的是：

$$
\boxed{
\text{self-sealing is a conditional failure mode, not a universal human law}
}
$$

---

# 9　2025 的重要修正：人可以合理折減錯誤資訊

Sanna 與 Lagnado 2025 進行四項實驗，研究 retraction、contradictory information 與 source reliability。

結果顯示 participants：

- 可以折減被撤回的 misinformation；
- 會依 source reliability 調整 belief；
- 會對被 correction 的來源降低 reliability judgment；
- trustworthiness 與 expertise 都影響 source evaluation。

這與「人類永遠困在舊 belief」明顯不一致。

因此：

$$
\boxed{
\text{well-structured correction can produce real updating}
}
$$

SET07 的任務不是宣布更新不可能，而是辨識：

> 什麼 system design 讓更新路徑被關掉？

---

# 10　Correction research 本身也提醒我們避免單一結論

Chan 與 Albarracin 2023 對 science-relevant misinformation 的 meta-analysis 報告平均 debunking effect 不顯著，且效果受議題與政治極化等 moderator 影響。

2025 年 Butler 等人在 *Nature Human Behaviour* 對該 meta-analysis 的 effect pooling 提出方法論異議，主張適當區分 effect type 後，corrections 其實有效；Chan 與 Albarracin 隨後回覆並維護原分析邏輯。

SET07 不替這場方法學爭議作最終裁決。

它要保留的是：

$$
\boxed{
\text{even meta-analytic conclusions remain sensitive to model and effect specification}
}
$$

這本身就是一個很好的自反案例：

> 方法越高階，越需要讓自己的 aggregation rule 可被審查。

---

# 11　Self-Sealing Beliefs 與 Epistemic Black Holes

Boudry 2024 使用 **epistemic black holes** 描述某些 belief systems：它們的防禦機制可以把缺乏證據、甚至反證本身，吸收到 theory 內部。

一種極端形式：

$$
\text{No evidence}
\Rightarrow
\text{the hidden agent is effective}.
$$

甚至：

$$
\text{Counterevidence}
\Rightarrow
\text{the cover-up is deeper}.
$$

於是：

$$
X
$$

不再區分：

$$
H
$$

與：

$$
\neg H.
$$

這是鑑別力崩潰的典型結構。

---

# 12　2026 的重要反方：Self-Sealing 不能被當作某類理論的專屬罪名

Hagen 2026 對 self-sealing critique 提出一個必要修正。

任何複雜 theory 都可能：

- 修改 auxiliary assumptions；
- 改 boundary conditions；
- 調整 measurement assumptions；
- 重新解釋 anomaly。

因此：

$$
\boxed{
\text{the ability to survive a counterexample by modification is not by itself pathological}
}
$$

如果把「可修改」直接定義成 self-sealing，

則幾乎所有成熟理論都可能被指控。

所以 SET07 不採：

$$
\text{survival after counterevidence}
\Rightarrow
\text{self-sealing}.
$$

真正的問題是：

$$
\boxed{
\text{What epistemic price did survival pay, and what new empirical risk did it create?}
}
$$

---

# 13　Lakatos：Protective Belt 可以是進步，也可以退化

Lakatos 的 methodology of scientific research programmes 提供最適合 SET07 的科學哲學橋梁。

研究綱領包含：

- hard core；
- protective belt；
- negative heuristic；
- positive heuristic。

protective belt 的存在不是詐術。

理論發展本來就需要 auxiliary assumptions。

真正關鍵是 problem shift 是否：

$$
\text{progressive}
$$

或：

$$
\text{degenerating}.
$$

若調整帶來：

- novel prediction；
- empirical corroboration；
- increasing explanatory reach；
- higher precision；

則保護核心可能是有生產力的。

若調整主要是：

> 每次失敗後再補一層，

卻沒有新的 risk exposure，

則更接近 degenerating shift。

---

# 14　從「防禦」改成「修訂成本與新風險」

因此 SET07 不問：

> 你有沒有保護核心？

而問兩件事。

第一：

$$
\boxed{
\text{Revision Cost}
}
$$

核心生存需要改多少 assumptions、boundary、weights 與 topology？

第二：

$$
\boxed{
\text{Novel Risk Exposure}
}
$$

修訂後是否新增「如果出現某觀察，理論會真的更危險」的條件？

一個健康修訂可以：

$$
\text{survive}
+
\text{become more exposed}.
$$

self-sealing 修訂則傾向：

$$
\text{survive}
+
\text{become less exposed}.
$$

---

# 15　Discriminative Pressure

不是所有 evidence 都值得迫使 theory revision。

令 candidate theory：

$$
H.
$$

rival theory：

$$
H'.
$$

evidence $x$ 的 discriminative pressure 可概念化為：

$$
\mathrm{DP}(x)
=
D
\left(
P(x\mid H),
P(x\mid H')
\right)
\times
Q(x),
$$

其中：

- $D$ 表示 likelihood discrimination；
- $Q(x)$ 表示 evidence quality / reliability。

如果：

$$
\mathrm{DP}(x)\approx0,
$$

不更新很合理。

所以「你看了很多反方」本身沒有意義。

真正需要的是：

$$
\text{high-quality discriminative counterevidence}.
$$

---

# 16　Core Revision

令核心投影：

$$
P_C(\mathcal B_t)=\mathcal C_t.
$$

定義：

$$
\mathrm{CR}_t
=
d_C
(
\mathcal C_{t+1},
\mathcal C_t
).
$$

高 CR 代表核心結構顯著移動。

低 CR 可以是：

- theory 很強；
- evidence 很弱；
- 或 system 很僵硬。

必須與 DP 聯合解讀。

---

# 17　Auxiliary Growth

令 auxiliary structure：

$$
\mathcal A_t.
$$

定義：

$$
\mathrm{AG}_t
=
\operatorname{Complexity}(\mathcal A_{t+1})
-
\operatorname{Complexity}(\mathcal A_t).
$$

complexity 可以依 domain 使用：

- parameter count；
- exception count；
- auxiliary hypothesis count；
- graph complexity；
- description length；
- special-case rule count。

高 AG 不是壞事。

如果同時：

$$
\mathrm{PG}\uparrow
$$

與：

$$
\mathrm{NRE}\uparrow,
$$

它可能表示成熟化。

若：

$$
\mathrm{AG}\uparrow
$$

但：

$$
\mathrm{PG}\approx0,
$$

則可能只是吸收反例的成本。

---

# 18　Novel Risk Exposure

定義新修訂：

$$
H_t
\mapsto
H_{t+1}.
$$

若 $H_{t+1}$ 產生一組 $H_t$ 沒有的可鑑別承諾：

$$
\mathcal R_{t+1}^{\mathrm{new}},
$$

則：

$$
\mathrm{NRE}_t
=
\operatorname{Weight}
(
\mathcal R_{t+1}^{\mathrm{new}}
).
$$

例如理論補上 auxiliary $A$ 後，不能只說：

> 有 $A$ 所以反例不算。

還要說：

> 如果 $A$ 真的存在，那在獨立情境 $Y$ 應出現 observable $Z$。

這才真正把 auxiliary 送進風險區。

---

# 19　Predictive Gain

令 out-of-sample predictive / discriminative performance：

$$
P_t.
$$

定義：

$$
\mathrm{PG}_t
=
P_{t+1}-P_t.
$$

如果一個 theory 每次遇到失敗都增加 explanatory vocabulary，

但：

$$
\mathrm{PG}_t\approx0
$$

長期不變，

那麼：

$$
\text{explanation growth}
$$

可能沒有轉成：

$$
\text{predictive learning}.
$$

---

# 20　Escape Capacity

承接 SET04 的 Epistemic Escape Capacity 與 SET05 的 Topological Escape Capacity。

SET07 使用：

$$
\mathrm{EC}\in[0,1]
$$

作為研究概念。

高 EC 的 system 能：

1. 指出哪些核心命題可能被撤回；
2. 事前定義高鑑別反證；
3. 允許 independent resampling；
4. 允許核心 edge 被刪除；
5. 接受 rival topology；
6. 在 prediction failure 後真正降低核心 confidence；
7. 必要時退出整個 research programme。

低 EC 的 system 則：

> 每一條出口都存在於文字上，但沒有一條能真正通往外部。

---

# 21　Epistemic Attractor Profile

本文不建立單一「封閉分數」。

因為：

$$
\text{low revision}
$$

可以代表高可靠性，也可以代表僵化。

所以提出 profile：

$$
\boxed{
\mathrm{EAP}
=
\langle
\mathrm{DP},
\mathrm{CR},
\mathrm{AG},
\mathrm{NRE},
\mathrm{ESR},
\mathrm{PG},
\mathrm{EC}
\rangle
}
$$

典型 candidate self-sealing pattern：

$$
\mathrm{DP}\uparrow,
$$

$$
\mathrm{CR}\downarrow,
$$

$$
\mathrm{AG}\uparrow,
$$

$$
\mathrm{NRE}\downarrow,
$$

$$
\mathrm{ESR}\uparrow,
$$

$$
\mathrm{PG}\approx0,
$$

$$
\mathrm{EC}\downarrow.
$$

這不是定律。

它是一個供實驗與理論 audit 使用的 profile。

---

# 22　「吸收無限資訊而幾乎不學習」的較嚴格版本

標題中的「無限」是極限語言，不應字面理解成實際 agent 能輸入無限資料。

令：

$$
I_T
=
\sum_{t=1}^{T}
I(X_t)
$$

隨 $T$ 增加。

若：

$$
I_T
\to
\text{large}
$$

但：

$$
\sum_{t=1}^{T}\mathrm{PG}_t
\approx0
$$

與：

$$
d_C(\mathcal C_T,\mathcal C_0)
\approx0
$$

且：

$$
\mathrm{AG}_T
\gg0,
$$

則稱系統呈現：

$$
\boxed{
\text{absorptive without discriminative learning}
}
$$

不是資料沒進來。

是資料主要轉成 auxiliary complexity，而不是模型區分力。

---

# 23　資訊量不是唯一問題，反事實區分力才是

一個 theory 可以對所有 observation 都給解釋。

但若：

$$
P(X\mid H)
$$

對幾乎所有 $X$ 都能事後調整為高，

則 observation 不再能區分：

$$
H
$$

與 rivals。

所以：

$$
\boxed{
\text{explanatory accommodation}
\neq
\text{discriminative prediction}
}
$$

SET07 不是反對 explanation。

而是要求：

> explanation 是否讓未來某些結果變得更不可能？

若沒有，

理論 exposure 不增加。

---

# 24　反證變證據：最強的封閉操作

最極端 self-sealing transformation 是：

$$
x
\xrightarrow{\text{counterevidence}}
H
$$

被 retype 成：

$$
x
\xrightarrow{\text{supports}}
H.
$$

例如：

> 沒找到，證明它藏得很好。

> 你反對，證明理論觸及你的防禦機制。

> 預測失敗，證明系統具有更深層隨機性。

這些句子在某些特定理論中可能有獨立成立條件。

真正危險的是：

$$
\boxed{
\text{both }x\text{ and }\neg x\text{ are systematically converted into support without independent discriminators}
}
$$

一旦如此，

$$
x
$$

不再具有 testing power。

---

# 25　Self-Sealing 不是 binary property

同一 theory 可以對：

$$
X_1
$$

高度可更新，

對：

$$
X_2
$$

非常僵硬。

同一 agent 也可以：

- 在科學問題上高 EC；
- 在身份問題上低 EC；
- 在低 stakes 問題上容易更新；
- 在高 identity cost 問題上 resistance 上升。

所以：

$$
\boxed{
\text{self-sealing is domain-relative and evidence-class-relative}
}
$$

不是人格 essence。

---

# 26　Echo Chamber 不是 SET07 的必要條件

2025 年 systematic review 對 129 項 echo-chamber studies 顯示，echo chamber 的 existence、measurement 與 effect 高度依賴 operationalization、platform、region 與 data source；有相當一部分研究並不支持 rigid echo-chamber picture。

因此 SET07 不需要：

$$
\text{echo chamber}
$$

才能成立。

一個 agent 即使大量接觸反方資訊，

仍可能透過：

$$
\Phi
$$

把反方資訊吸收進原 topology。

反過來，多元媒體接觸也可能真的降低封閉。

所以：

$$
\boxed{
\text{exposure diversity}
\neq
\text{revision guarantee}
}
$$

但也：

$$
\boxed{
\text{exposure diversity can matter}
}
$$

---

# 27　記憶與檢索：外部環境可以形成 basin

如果 agent 的下一輪搜尋由當前 belief 生成：

$$
Q_{t+1}
=
g(B_t),
$$

搜尋結果又影響：

$$
B_{t+1},
$$

則形成：

$$
B_t
\to
Q_{t+1}
\to
R_{t+1}
\to
B_{t+1}.
$$

若 query framing、social network、AI memory、recommendation system 與 prior 持續共振，

belief attractor 可能不只存在於頭腦，

而存在於：

$$
\boxed{
\text{human}
+
\text{search}
+
\text{social network}
+
\text{AI}
+
\text{memory}
}
$$

的耦合系統。

本文不宣稱該宏觀 attractor 已被普遍實證。

它是後續研究假說。

---

# 28　AI 可以成為吸引子放大器，也可以成為退出機制

AI 若長期：

- 記住使用者 worldview；
- 用同一 framing 搜尋；
- 優先產生 congruent explanations；
- 把所有反例翻譯成 auxiliary；
- 缺少 independent critic；

則可能降低：

$$
\mathrm{EC}.
$$

但 AI 也可以提高 EC：

- blind rival-model generation；
- independent web resampling；
- preregistered falsifier；
- counterfactual search；
- topology diff；
- prediction ledger；
- automatic exception counting；
- delayed outcome audit。

因此：

$$
\boxed{
\text{AI does not determine the attractor direction; interaction protocol does}
}
$$

---

# 29　Builder 與 Falsifier 必須分離

若同一 AI role 同時負責：

1. 幫 theory 存活；
2. 判斷 theory 是否應死；

容易產生 conflict。

所以對高影響研究可拆：

$$
A_{\mathrm{builder}},
$$

$$
A_{\mathrm{falsifier}},
$$

$$
A_{\mathrm{historian}},
$$

$$
A_{\mathrm{empiricist}},
$$

$$
A_{\mathrm{forecast}}.
$$

其中 builder 不掌握 final validation authority。

falsifier 也不能因一次失敗自動處決 theory。

真正 final state 由 evidence ledger 與 independent procedures 共同決定。

---

# 30　預先註冊「什麼會讓我改變」

最廉價的 anti-attractor 方法之一是：

在看結果前定義：

$$
R^{*}.
$$

例如：

> 若三次獨立 replication 皆出現 $X$，核心 confidence 從 $0.8$ 降到 $0.4$ 以下。

結果出現後再觀察：

$$
R_{\mathrm{actual}}.
$$

若：

$$
R_{\mathrm{actual}}
\neq
R^{*}
$$

且每次門檻都被往外推，

記錄：

$$
\text{Revision Threshold Drift}.
$$

這比問：

> 你願不願意改？

更有測量價值。

---

# 31　Auxiliary Independence Test

新增 auxiliary hypothesis：

$$
A_x
$$

以處理反證 $x$。

問：

1. $A_x$ 在 $x$ 出現前是否已有理由？
2. $A_x$ 是否能在獨立 domain 被測？
3. $A_x$ 是否產生新 observable？
4. $A_x$ 若失敗，是否真的會反過來傷害 core？
5. $A_x$ 是否只是讓 $x$ 失去反證身份？

若 $A_x$ 只有單一功能：

$$
\text{save core from }x,
$$

但沒有 independent empirical life，

其 immunization risk 較高。

---

# 32　Novel-Risk Accounting

每次 theory 修訂：

$$
H_t
\mapsto
H_{t+1}
$$

建立 ledger：

| Revision | 解決哪個 anomaly | 新增 assumptions | 新增 prediction | 新增 falsifier | Out-of-sample result |
|---|---|---|---|---|---|

真正健康的 research programme 應該不是只讓：

$$
\text{Assumptions}
$$

欄愈來愈長。

而是：

$$
\text{Predictions}
$$

與：

$$
\text{Falsifiers}
$$

也增加。

---

# 33　Core Exit Test

問 agent：

> 哪一種 evidence sequence 會讓你退出核心？

如果回答：

> 沒有任何可能結果。

那至少在當前 formulation：

$$
\mathrm{EC}=0
$$

或非常低。

如果回答：

> 有，但永遠只有不可能取得的 evidence 才算。

則需要再審查：

$$
\text{practical falsifiability}.
$$

真正有效的 exit path 應該：

- principle possible；
- operationally specified；
- independent of outcome direction；
- not continuously movable after observation。

---

# 34　Epistemic Attractor Stress Protocol（EASP）

## Step 1：Freeze the Core

列出：

$$
\mathcal C_0.
$$

不能讓「核心是什麼」在每次失敗後重寫。

---

## Step 2：Build Rival Topologies

至少建立：

$$
G_1,
G_2,\ldots,G_k.
$$

避免 theory 只和「沒有 theory」比較。

---

## Step 3：Find High-DP Evidence

優先測：

$$
X^{*}
$$

使 rival likelihood 差異大。

---

## Step 4：Precommit Revision Threshold

事前寫：

$$
R^{*}.
$$

---

## Step 5：Run Exception Audit

所有反證被標記：

- accepted counterevidence；
- legitimate boundary；
- unresolved anomaly；
- exception；
- rejected evidence。

計算概念性：

$$
\mathrm{ESR}.
$$

---

## Step 6：Audit Auxiliary Growth

記錄：

$$
\mathrm{AG}.
$$

---

## Step 7：Demand Novel Risk

每個 auxiliary 至少提出一個 independent observable。

估計：

$$
\mathrm{NRE}.
$$

---

## Step 8：Measure Predictive Gain

使用：

- holdout data；
- future event；
- independent replication；
- new domain transfer。

估計：

$$
\mathrm{PG}.
$$

---

## Step 9：Run Core Exit Test

若 evidence 達門檻，核心是否：

$$
\mathcal C_0
\mapsto
\mathcal C_1?
$$

---

## Step 10：Report EAP

輸出：

$$
\mathrm{EAP}
=
\langle
\mathrm{DP},
\mathrm{CR},
\mathrm{AG},
\mathrm{NRE},
\mathrm{ESR},
\mathrm{PG},
\mathrm{EC}
\rangle.
$$

不要輸出單一：

> 科學 / 不科學。

---

# 35　實驗一：Exception Sink

給 participants 一個可學習 rule。

持續提供 high-quality counterexamples。

允許三種反應：

1. revise rule；
2. create exception；
3. reject datum。

測：

$$
\mathrm{ESR}
$$

與：

$$
\mathrm{CR}.
$$

再比較有無 preregistered revision threshold。

---

# 36　實驗二：Auxiliary Hypothesis Dynamics

讓 participants / AI agent 建立 theory。

每次 prediction failure 後可：

- abandon core；
- modify auxiliary；
- add new auxiliary。

比較：

$$
\mathrm{AG},
\mathrm{NRE},
\mathrm{PG}.
$$

重點不是 auxiliary 越少越好，

而是：

$$
\boxed{
\text{Does auxiliary growth buy new predictive exposure?}
}
$$

---

# 37　實驗三：Builder versus Builder-plus-Falsifier

比較：

Condition A：

$$
\text{single collaborative agent}
$$

Condition B：

$$
A_{\mathrm{builder}}
+
A_{\mathrm{falsifier}}.
$$

固定模型能力與 evidence access。

測：

- core revision；
- false-theory survival；
- true-theory preservation；
- novel prediction；
- auxiliary proliferation。

如果 falsifier 只提高 indiscriminate rejection，則 protocol 失敗。

---

# 38　實驗四：Memory Reinforcement

長期人機 interaction 中比較：

1. no memory；
2. preference memory；
3. theory memory；
4. theory memory + adversarial resampling。

測：

$$
\mathrm{EC},
\mathrm{ESR},
\mathrm{CR}.
$$

此設計用來檢驗：

> memory 是否在某些架構下將 local bias 焊成 long-term attractor。

---

# 39　實驗五：Correction and Exit

利用 misinformation correction paradigm。

比較：

- correction only；
- correction + source reliability；
- correction + explicit contrast reminder；
- correction + precommitted revision criterion。

測：

- immediate update；
- delayed update；
- source memory；
- core confidence；
- repeated correction response。

2025 correction research已顯示 reminder 與 source reliability 可以改善 updating，因此若 EASP 完全無增益，本文的 protocol 需要縮小。

---

# 40　科學理論也必須被 SET07 檢查

SET07 不能只拿去批評：

- 宗教；
- conspiracy；
- political ideology；
- pseudoscience。

科學 research programme 同樣具有：

- hard core；
- auxiliaries；
- paradigm commitments；
- institutional incentives；
- citation inheritance。

所以同一判準必須問：

$$
\mathrm{AG}
$$

增加時，

是否也有：

$$
\mathrm{NRE}
$$

與：

$$
\mathrm{PG}
$$

增加？

若沒有，

「這是科學」不能自動免疫 degenerating dynamics。

---

# 41　但不能把 theory resilience 當成壞事

如果 evidence 很 noisy，

一個 theory 每遇到 anomaly 就崩潰，

反而不是好 epistemology。

因此：

$$
\boxed{
\text{good theories need inertia}
}
$$

真正問題是：

$$
\boxed{
\text{how much inertia is justified by evidence and predictive success?}
}
$$

健康系統應該同時具有：

$$
\text{stability}
$$

與：

$$
\text{escape}.
$$

不是零阻力。

也不是無限阻力。

---

# 42　吸引子不是「信念很強」

高 confidence：

$$
P(H)\approx1
$$

不等於 attractor。

如果有足夠 likelihood ratio：

$$
\frac{P(X\mid\neg H)}{P(X\mid H)}
$$

長期壓倒 prior，

且 agent 會更新，

那只是 strong prior。

epistemic attractor 更強：

> evidence 不只需要克服 prior，還會被 system 的 selection、retyping、exception、auxiliary 與 gate rules 重新加工。

所以：

$$
\boxed{
\text{high prior}
\neq
\text{self-sealing update architecture}
}
$$

---

# 43　Bayesian coherence 仍可能被 model class 限制

一個 agent 可以完美執行：

$$
P(H_i\mid X)
$$

但若 hypothesis class：

$$
\mathcal H
$$

從未包含真正生成機制，

則 posterior 只能在錯誤 model class 裡重新分配。

因此：

$$
\boxed{
\text{perfect updating inside a closed hypothesis class can still miss the world outside the class}
}
$$

這不是 Bayesianism 的缺陷。

這是任何 model-based inference 都需要處理的 model misspecification 問題。

所以真正 exit capacity 也包含：

$$
\mathcal H
\mapsto
\mathcal H'
$$

的能力。

---

# 44　方法也可以成為吸引子

若一個方法 $M$ 對所有 failure 都回答：

> 不是方法錯，是你沒有正確使用方法。

這句有時是真的。

但若永遠如此，

則：

$$
M
$$

不再受到 outcome 更新。

因此：

$$
\boxed{
\text{Any method that only audits its users and never itself can become an epistemic attractor}
}
$$

這適用於：

- Bayesian method；
- falsificationism；
- formalism；
- empiricism；
- rationalism；
- qualitative method；
- AI-assisted research；
- SET 系列本身。

---

# 45　SET 系列自己的 attractor risk

SET01 至 SET07 已建立：

- selective truth；
- listener identification；
- strategic concession；
- sincere selection；
- admissible arrows；
- false topology；
- epistemic attractors。

這套 vocabulary 本身可能開始：

> 看什麼都像 selection、arrow、topology、attractor。

如果如此，

系列就成為自己的證據。

因此必須設置 core-exit condition：

若大量 empirical comparison 顯示：

1. node-only models 已足以解釋大多數案例；
2. edge-aware metrics 缺乏可靠性；
3. EAP 無法預測 correction、revision 或 forecast performance；
4. alternative simpler theories 解釋力更高；
5. 所謂 attractor profile 只是既有 confirmation-bias constructs 的重命名；

則 SET framework 應縮減、合併或放棄部分新術語。

---

# 46　Series B 的整體閉環

SET01：

$$
F(W)
\xrightarrow{\pi}
M.
$$

研究真實事實如何被選擇。

SET02：

$$
M
\not\Rightarrow
\pi.
$$

研究 receiver 對生成政策的不可識別性。

SET03：

$$
\text{small concession}
\to
\text{credibility dividend}.
$$

研究張力如何改變 source weight。

SET04：

$$
B
\to
\pi_B.
$$

研究真誠 belief 如何塑造 selection 與 weighting。

SET05：

$$
\mathcal B
=
(V,E,\mathfrak A,\Phi).
$$

研究 worldview 如何規定可允許 arrows。

SET06：

$$
q(V)=1
\not\Rightarrow
q(E)=1.
$$

研究真節點如何構成假拓撲。

SET07：

$$
\Phi(\mathcal B,X)
\approx
\mathcal B
$$

研究整個 system 如何在大量新資訊下保持核心不變。

於是系列完整路徑為：

$$
\boxed{
\text{World}
\to
\text{Selection}
\to
\text{Message}
\to
\text{Interpretation}
\to
\text{Topology}
\to
\text{Revision Dynamics}
}
$$

---

# 47　最終劃界：不是「你信什麼」，而是「什麼能讓你離開」

一個 worldview 可以非常離奇，

但若它：

- 指定 falsifier；
- 接受 independent evidence；
- 允許核心 edge 被刪除；
- 修訂後承擔新風險；
- prediction 失敗時降低 confidence；

它具有高：

$$
\mathrm{EC}.
$$

一個 worldview 可以非常主流，

但若任何 failure 都只增加：

$$
\mathrm{AG}
$$

而不增加：

$$
\mathrm{NRE},
$$

也應接受同一檢查。

所以劃界不是題材。

而是動力學。

---

# 48　什麼結果會削弱 SET07？

以下結果若跨 domain 穩定成立，SET07 應被大幅縮小：

1. belief perseverance 在高品質、清楚反證下極少出現；
2. exception classification 幾乎不預測 core persistence；
3. auxiliary growth 與 predictive gain 通常同步上升；
4. self-sealing profile 無法區分 progressive 與 degenerating theory change；
5. precommitted revision thresholds 不改善 updating；
6. independent falsifier 不降低 false-theory survival；
7. EAP 不預測 out-of-sample performance 或 correction uptake；
8. core-periphery decomposition reliability 很低；
9. echo / memory / AI context 對 attractor dynamics 沒有穩定影響；
10. simpler existing constructs 已能完整解釋 EAP 所有效應。

如果如此，

$$
\text{epistemic attractor}
$$

應保留為 metaphor，

而不是 framework。

---

# 49　自反性：真正的出口必須存在於本文之外

本文無法用自己的文字證明：

> 本文不是 self-sealing。

因為任何自我聲明都可以只是另一層 protective belt。

真正測試只能來自：

- independent reviewers；
- rival models；
- empirical failure；
- alternative formalization；
- preregistered experiments；
- unsuccessful prediction；
- cross-domain non-transfer。

所以：

$$
\boxed{
\text{self-reflexive language is not self-correction}
}
$$

只有實際 revision 才是。

---

# 50　結論

最封閉的 belief system，不一定最貧乏。

它可能是最豐富的。

它可以有：

- 最多引用；
- 最多例外；
- 最多 auxiliary hypotheses；
- 最多術語；
- 最完整敘事；
- 最漂亮 graph；
- 最長的歷史解釋。

卻仍然：

$$
d_{\mathrm{core}}
(
\mathcal C_T,
\mathcal C_0
)
\approx0.
$$

所以：

$$
\boxed{
\text{complexity growth}
\not\Rightarrow
\text{epistemic growth}
}
$$

SET07 最後留下六條原則：

$$
\boxed{
\text{A system does not learn merely because it absorbs information}
}
$$

$$
\boxed{
\text{Protecting a core is not inherently irrational}
}
$$

$$
\boxed{
\text{Healthy protection should buy new prediction or new empirical risk}
}
$$

$$
\boxed{
\text{Counterevidence must retain a legal path to core revision}
}
$$

$$
\boxed{
\text{A worldview's health depends on whether exit remains operational, not merely verbal}
}
$$

以及整個 Series B 的最終收束：

$$
\boxed{
\text{The decisive question is not only what a system can explain, but what can still force it to become something else}
}
$$

---

# References

1. Anderson, C. A., Lepper, M. R., & Ross, L. (1980). Perseverance of Social Theories: The Role of Explanation in the Persistence of Discredited Information. *Journal of Personality and Social Psychology*, 39(6), 1037-1049. https://doi.org/10.1037/h0077720

2. Nickerson, R. S. (1998). Confirmation Bias: A Ubiquitous Phenomenon in Many Guises. *Review of General Psychology*, 2(2), 175-220. https://doi.org/10.1037/1089-2680.2.2.175

3. Oeberst, A., & Imhoff, R. (2023). Toward Parsimony in Bias Research: A Proposed Common Framework of Belief-Consistent Information Processing for a Set of Biases. *Perspectives on Psychological Science*, 18(6), 1464-1487. https://doi.org/10.1177/17456916221148147

4. Anglin, S. M. (2019). Do Beliefs Yield to Evidence? Examining Belief Perseverance vs. Change in Response to Congruent Empirical Findings. *Journal of Experimental Social Psychology*, 82, 176-199. https://doi.org/10.1016/j.jesp.2019.02.004

5. Sanna, G. A., & Lagnado, D. (2025). Belief Updating in the Face of Misinformation: The Role of Source Reliability. *Cognition*, 258, 106090. https://doi.org/10.1016/j.cognition.2025.106090

6. Wellons, B. M., & Wahlheim, C. N. (2025). Misinformation Reminders Enhance Belief Updating and Memory for Corrections: The Role of Attention During Encoding Revealed by Eye Tracking. *Cognitive Research: Principles and Implications*, 10, 39. https://doi.org/10.1186/s41235-025-00649-y

7. Chan, M. S., & Albarracin, D. (2023). A Meta-Analysis of Correction Effects in Science-Relevant Misinformation. *Nature Human Behaviour*, 7, 1514-1525. https://doi.org/10.1038/s41562-023-01623-8

8. Butler, L. H., DeGutis, J., Tay, L. Q., Swire-Thompson, B., & Ecker, U. K. H. (2025). Corrections Are Effective for Science Misinformation. *Nature Human Behaviour*, 9, 2458-2460. https://doi.org/10.1038/s41562-025-02245-y

9. Chan, M. S., & Albarracin, D. (2025). Reply to: Corrections Are Effective for Science Misinformation. *Nature Human Behaviour*, 9, 2461-2470. https://doi.org/10.1038/s41562-025-02265-8

10. Boudry, M. (2024). On Epistemic Black Holes: How Self-Sealing Belief Systems Develop and Evolve. *Theoria*, 90(4), 429-447. https://doi.org/10.1111/theo.12554

11. Hagen, K. (2026). Are Conspiracy Theories Problematically Self-Sealing? *Episteme*, First View, 1-19. https://doi.org/10.1017/epi.2026.10115

12. Lakatos, I. (1970). Falsification and the Methodology of Scientific Research Programmes. In I. Lakatos & A. Musgrave (Eds.), *Criticism and the Growth of Knowledge* (pp. 91-196). Cambridge University Press. Reprinted in *The Methodology of Scientific Research Programmes*.

13. Hartmann, D., Wang, S. M., Pohlmann, L., et al. (2025). A Systematic Review of Echo Chamber Research: Comparative Analysis of Conceptualizations, Operationalizations, and Varying Outcomes. *Journal of Computational Social Science*, 8, Article 52. https://doi.org/10.1007/s42001-025-00381-z

14. Hunt, J. C. (2012). On Ad Hoc Hypotheses. *Philosophy of Science*, 79(1), 1-14. https://doi.org/10.1086/663238

15. Schindler, S. (2018). A Coherentist Conception of Ad Hocness. *Studies in History and Philosophy of Science Part A*, 67, 54-64. https://doi.org/10.1016/j.shpsa.2017.11.011

---

## 系列位置

**Selective Truth and Epistemic Topology**

- SET01：高明的謊言不需要假話：選擇性真實、資訊抽樣與失真世界
- SET02：聽者的不可識別問題：當客觀評估與策略性真話產生相同表面訊息
- SET03：張力控制與策略性讓步：可信度如何被工程化
- SET04：真誠的人也能產生選擇性世界：Sincere Selection Bias
- SET05：信念系統不是信念集合，而是允許箭頭的系統
- SET06：真節點，假拓撲：資訊失真如何發生在關係而非命題
- **SET07：認識論吸引子與自我封閉：吸收無限資訊而幾乎不學習**

---

## Series Closure

Series B 的最小骨架：

$$
\boxed{
\text{World}
\to
\text{Selection}
\to
\text{Message}
\to
\text{Interpretation}
\to
\text{Topology}
\to
\text{Revision Dynamics}
}
$$

其最終劃界不是：

> 這套 worldview 現在相信什麼？

而是：

> **當足夠強的世界證據出現時，它是否仍保留一條真正可以離開自己的路？**

---

*SET07 / Selective Truth and Epistemic Topology / EveMissLab / v0.1 / 2026-09-07*
