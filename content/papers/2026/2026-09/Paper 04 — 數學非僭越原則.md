# Paper 04 — 數學非僭越原則
## 從可能世界模型到未來存在論的認識論邊界

**Series:** Recursive Simulation, Transcendence, and Mathematical Non-Usurpation / 遞歸模擬、超越者與數學非僭越  
**Author:** Neo.K  
**Institution:** EveMissLab／一言諾科技有限公司  
**Date:** 2026-09-04  
**Status:** Internal Research Draft v1.0  
**Role:** Final epistemic closure paper  
**Scope:** Mathematical non-usurpation, conjecture/model/theorem/evidence/future/ontology separation, epistemic inflation, model-world grounding, future state-space drift, posthuman unknowability, fallibilism, and the limits of mathematical authority over actuality

---

## 摘要

本系列前三篇依序處理：

1. Simulation Argument 的條件式本質與存在論誤讀；
2. posthuman civilization 作為超越者時的遞歸未閉包；
3. simulated world 不等於 unreal world，以及 simulation status 與 agency status 的分離。

最後仍剩下一個最根本的方法論問題：

> 數學與形式模型究竟有權說到哪裡？

若某個模型：

$$
M
$$

在前提集合：

$$
\mathcal A
$$

下推出：

$$
Q,
$$

即：

$$
M,\mathcal A\vdash Q,
$$

我們能正當得到的是：

$$
\boxed{
\text{在 }M,\mathcal A\text{ 中，}Q\text{ 成立。}
}
$$

但一般不能直接得到：

$$
\boxed{
\mathcal W\models Q,
}
$$

其中：

$$
\mathcal W
$$

代表實際世界。

更不能因：

$$
Q
$$

在模型內具有高機率、巨大倍率、漸近必然性或漂亮閉式解，就把它進一步升格為：

$$
\boxed{
\text{future actuality}
}
$$

或：

$$
\boxed{
\text{ontological truth}.
}
$$

因此，本篇提出 **Mathematical Non-Usurpation Principle, MNUP / 數學非僭越原則**：

> 數學可以約束已指定公理、模型與可能世界中的結構關係；但數學本身無權在缺少額外 grounding 的情況下，單方面宣告哪一套可能世界就是現實、哪一條未來路徑必然實現、或哪一種本體論已被證實。

形式上：

$$
\boxed{
M,\mathcal A\vdash Q
\not\Rightarrow
\mathcal W\models Q.
}
$$

同樣：

$$
\boxed{
P(F\mid M,D_t)\approx1
\not\Rightarrow
F=\text{unrevisable future fact}.
}
$$

以及：

$$
\boxed{
\text{Mathematical Possibility}
\neq
\text{Physical Possibility}
\neq
\text{Historical Realization}
\neq
\text{Ontological Actuality}.
}
$$

本篇並不反對數學，也不主張 radical skepticism。相反，MNUP 的目的恰恰是保護數學真正的力量：

$$
\boxed{
\text{如果前提成立，哪些結論必然成立？}
}
$$

同時拒絕一種常見的 epistemic inflation：

$$
\text{Conjecture}
\rightarrow
\text{Model}
\rightarrow
\text{Conditional Result}
\rightarrow
\text{Plausible Future}
\rightarrow
\text{Treated-as-Fact}
\rightarrow
\text{Ontological Absolutization}.
$$

最後，本篇主張所有未來學、simulation discourse、ASI/posthuman projection 與 mathematical cosmology 都應至少區分：

$$
\boxed{
H
\neq
M
\neq
T
\neq
E
\neq
F
\neq
O,
}
$$

其中：

- $H$：Hypothesis / Conjecture；
- $M$：Model；
- $T$：Theorem / Conditional Deduction；
- $E$：Empirical Evidence；
- $F$：Future Projection；
- $O$：Ontological Claim。

理論可以很強，卻仍然只是理論。

證據可以很強，卻仍可能被更廣模型重新定位。

數學可以極度精確，卻不因精確本身而獲得替世界選擇自身本體的權力。

---

# 1. 這不是反數學論

先排除最容易發生的誤讀。

MNUP 不主張：

$$
\boxed{
\text{mathematics is unreliable}.
}
$$

也不主張：

$$
\boxed{
\text{all mathematical models are arbitrary}.
}
$$

更不主張：

$$
\boxed{
\text{science cannot know anything}.
}
$$

本篇真正主張的是：

$$
\boxed{
\text{mathematical validity has a domain of authority}.
}
$$

只要越過這個 domain，

就需要額外 warrant。

---

# 2. 數學最強的地方：Conditional Necessity

設：

$$
\mathcal A
$$

是一組公理，

且：

$$
\mathcal A\vdash T.
$$

若 proof 正確，

那麼：

$$
T
$$

是：

$$
\boxed{
\text{formal consequence of }\mathcal A.
}
$$

這是數學最強的能力：

$$
\boxed{
\text{given the premises, the conclusion cannot escape}.
}
$$

---

# 3. 但公理成立於世界，不是 theorem 自己證明的

若我們想從：

$$
\mathcal A\vdash T
$$

進一步說：

$$
\mathcal W\models T,
$$

至少需要：

$$
\boxed{
\mathcal W\models\mathcal A.
}
$$

而：

$$
\mathcal W\models\mathcal A
$$

不是由：

$$
\mathcal A\vdash T
$$

自行提供的。

因此：

$$
\boxed{
\text{proof validity}
\neq
\text{world instantiation}.
}
$$

---

# 4. Model-World Grounding

定義：

$$
\boxed{
G(M,\mathcal W)
}
$$

表示 model：

$$
M
$$

與實際世界：

$$
\mathcal W
$$

之間的 grounding strength。

它可能來自：

- observation；
- experiment；
- repeated prediction；
- intervention；
- causal identification；
- measurement；
- cross-domain validation。

只有：

$$
G(M,\mathcal W)
$$

足夠高，

模型 output 才能獲得較強 world-level warrant。

---

# 5. Grounding 不是一次性二元

不是：

$$
G=0
$$

或：

$$
G=1.
$$

更合理：

$$
\boxed{
G(M,\mathcal W\mid D,t)\in[0,1].
}
$$

而且它依賴：

- domain；
- scale；
- evidence；
- historical time。

所以一個 model 可以：

$$
G\approx1
$$

在某個 domain，

但：

$$
G\ll1
$$

在另一個 domain。

---

# 6. Domain-Bounded Validity

這是科學史最常見的情況。

模型：

$$
M
$$

不是：

$$
\boxed{
\text{wrong everywhere}.
}
$$

而是：

$$
\boxed{
\text{valid within }D.
}
$$

例如：

$$
M_{\mathrm{Newton}}
$$

可以在：

$$
D_{\mathrm{low\ velocity,weak\ gravity}}
$$

極度有效。

但這不表示：

$$
M_{\mathrm{Newton}}
$$

就是：

$$
\boxed{
\text{complete ontology of motion}.
}
$$

---

# 7. 被更廣理論包覆不等於舊理論毫無價值

如果：

$$
M_1
$$

被：

$$
M_2
$$

擴張，

形成：

$$
D(M_1)\subset D(M_2),
$$

則：

$$
M_1
$$

可能仍然是：

$$
\boxed{
\text{excellent local approximation}.
}
$$

所以：

$$
\boxed{
\text{fallibility}
\neq
\text{worthlessness}.
}
$$

---

# 8. 命題猜想的正確地位

一個命題：

$$
H
$$

如果尚未有充分 argument / evidence，

就是：

$$
\boxed{
\text{Hypothesis / Conjecture}.
}
$$

它可以：

- 非常漂亮；
- 極具啟發；
- 高度 plausible；
- 有強 predictive value。

仍然不等於：

$$
\boxed{
\text{established fact}.
}
$$

---

# 9. 論證過也不代表永遠不可修正

這裡要區分兩種「論證」。

若：

$$
\mathcal A\vdash T
$$

是固定形式系統中的真 theorem，

那麼只要：

- $\mathcal A$ 不變；
- inference rules 不變；
- proof 無誤；

它不會被新實驗推翻。

但若：

$$
M
$$

是 empirical world-model，

即使今天高度成功，

仍可能：

$$
M_t
\rightarrow
M_{t+1}.
$$

所以：

$$
\boxed{
\text{Mathematical theorem revisability}
\neq
\text{Empirical model revisability}.
}
$$

---

# 10. 所謂「推翻」通常是在改適用域

人類科學史中，

大量所謂：

> 舊理論被推翻。

更精確是：

$$
\boxed{
\text{old theory lost universality claim}.
}
$$

例如：

$$
M_1
$$

原本被誤認為：

$$
D=\forall.
$$

後來發現：

$$
D=D_1.
$$

這不是：

$$
M_1=0.
$$

而是：

$$
\boxed{
\operatorname{Scope}(M_1)\text{ 被重新校準}.
}
$$

---

# 11. Scope Claim 本身也需要證據

一個 equation：

$$
E
$$

可以在：

$$
D_1
$$

被驗證。

但：

$$
E\text{ works in }D_1
$$

不能推出：

$$
\boxed{
E\text{ works in all possible domains}.
}
$$

因此：

$$
\boxed{
\text{success}
\not\Rightarrow
\text{universality}.
}
$$

---

# 12. 第一個僭越：Possible → Physical

若一個 structure：

$$
S
$$

數學上自洽，

表示：

$$
\boxed{
S\in\mathcal P_{\mathrm{math}}
}
$$

即它位於 mathematical possibility space。

但這不能直接推出：

$$
\boxed{
S\in\mathcal P_{\mathrm{physical}}.
}
$$

所以：

$$
\boxed{
\mathcal P_{\mathrm{physical}}
\subseteq?
\mathcal P_{\mathrm{math}}
}
$$

本身就是哲學／物理問題。

---

# 13. 第二個僭越：Physical → Actual

即使：

$$
S
$$

物理上可行，

也不能推出：

$$
\boxed{
S\text{ actually occurs}.
}
$$

可行：

$$
\neq
$$

實現。

例如：

$$
\text{a technically possible civilization architecture}
$$

不等於：

$$
\text{history will instantiate it}.
$$

---

# 14. 第三個僭越：Actual → Necessary

即使某件事：

$$
F
$$

實際發生，

也不能推出：

$$
\boxed{
F\text{ had to happen}.
}
$$

歷史 actualization：

$$
\boxed{
\text{actual}
\neq
\text{necessary}.
}
$$

---

# 15. 第四個僭越：Repeated → Ontological

即使：

$$
F
$$

在很多 domain 重複出現，

也不能立刻推出：

$$
\boxed{
F\text{ is a fundamental ontological invariant}.
}
$$

可能原因還包括：

- shared constraints；
- selection；
- common ancestry；
- limited design space；
- measurement bias。

---

# 16. 四段非僭越鏈

因此：

$$
\boxed{
\text{Mathematical}
\not\Rightarrow
\text{Physical}
\not\Rightarrow
\text{Actual}
\not\Rightarrow
\text{Necessary}
\not\Rightarrow
\text{Ultimate}.
}
$$

每一箭都需要新的 warrant。

---

# 17. Future Projection 是最容易僭越的地方

因為未來：

$$
F_{t+n}
$$

目前不存在完整觀測資料。

所以我們只能：

$$
P(
F_{t+n}
\mid
M_t,D_t
).
$$

這是一個：

$$
\boxed{
\text{conditional forecast}.
}
$$

不是：

$$
\boxed{
\text{future observation}.
}
$$

---

# 18. 預測未來當然可以

MNUP 不是說：

> 不准做 futurology。

相反，

未來研究非常重要。

可以建立：

$$
\mathcal F
=
\{F_1,F_2,\ldots,F_n\}
$$

並估：

$$
P(F_i\mid M,D_t).
$$

但應保持 label：

$$
\boxed{
\text{projection}.
}
$$

---

# 19. Future Fact 的條件比 Model Output 強

若要說：

$$
\boxed{
F_i=\text{future fact},
}
$$

那實際上必須等：

$$
t\rightarrow t_i
$$

並觀測：

$$
D_{t_i}.
$$

在此之前：

$$
F_i
$$

最多是：

$$
\boxed{
\text{forecast / scenario / conditional consequence}.
}
$$

---

# 20. 固定 Transition Function 的問題

很多預測暗中假設：

$$
x_{t+1}=F(x_t)
$$

並將：

$$
F
$$

視為固定。

對短期物理過程可能合理。

但對文明數百、數千、數萬年尺度：

$$
\boxed{
F_t
}
$$

本身可能演化。

所以：

$$
x_{t+1}=F_t(x_t).
$$

---

# 21. Transition-Law Drift

定義：

$$
\boxed{
\Delta F_t
=
F_{t+1}-F_t.
}
$$

若：

$$
\Delta F_t\neq0,
$$

則遠期 extrapolation error 不只來自 state uncertainty。

還來自：

$$
\boxed{
\text{law/model-of-transition uncertainty}.
}
$$

---

# 22. Posthuman Prediction 尤其受此影響

今日我們預測 posthuman civilization：

$$
C_P
$$

會做什麼，

往往使用：

- current human motives；
- current computation concepts；
- current research incentives；
- current identity concepts。

但：

$$
C_P
$$

可能已經改寫：

- substrate；
- cognition；
- value formation；
- reproduction；
- identity；
- temporal experience；
- resource accounting。

因此：

$$
\boxed{
F_{\mathrm{human}}
\neq
F_{\mathrm{posthuman}}
}
$$

高度可能。

---

# 23. State Space Drift

更深一層：

今天：

$$
x_t\in X_t.
$$

但未來：

$$
x_{t+n}\in X_{t+n}.
$$

且：

$$
\boxed{
X_t\neq X_{t+n}.
}
$$

也就是未來可能產生今天 model vocabulary 裡根本沒有的 state categories。

---

# 24. Conceptual Novelty Problem

假設今天的 action set：

$$
\Omega_t
=
\{
\text{simulate},
\text{compute},
\text{travel},
\text{reproduce}
\}.
$$

未來 civilization 可能擁有：

$$
\omega^*
\notin\Omega_t.
$$

那：

$$
P(\omega^*)
$$

今天甚至無法被合理 parameterize。

這就是：

$$
\boxed{
\text{Conceptual Novelty Problem}.
}
$$

---

# 25. 超越者不可理解，會增加不確定性

如果有人主張：

$$
C_P
$$

已經：

$$
\boxed{
\text{beyond current human conceptual modeling},
}
$$

那麼合理更新是：

$$
\boxed{
H(C_P)\uparrow
}
$$

其中：

$$
H
$$

表示 epistemic uncertainty / entropy。

不是：

$$
\boxed{
P(\text{我偏好的 future behavior})\uparrow.
}
$$

---

# 26. Unknowability Cannot Be Directional

這是 Paper 01 的 Epistemic Symmetry Requirement 的進一步一般化。

若：

$$
C_P
$$

不可預測，

那麼：

$$
\boxed{
\text{其不大量模擬祖先}
}
$$

與：

$$
\boxed{
\text{其大量模擬祖先}
}
$$

都同樣受到 uncertainty。

不能：

> 需要 defending hypothesis 時就說不可想像；
> 需要 multiplier 時又假設大量模擬。

---

# 27. 超越者是否還問第一因，也是同樣問題

有人可能說：

> 超越者已經超越，所以祂們根本不會問第一因。

若其心理真的不可知，

那這句話同樣是：

$$
\boxed{
\text{unwarranted behavioral prediction}.
}
$$

更重要：

RNCP 並不依賴祂們「有沒有問」。

它只問：

$$
\boxed{
\text{structural dependence 是否仍存在？}
}
$$

---

# 28. 不問問題不等於問題不存在

若：

$$
C_P
$$

完全不在乎：

$$
Q=\text{Why does our world exist?}
$$

仍然不能推出：

$$
\boxed{
Q\text{ has no truth-condition}.
}
$$

所以：

$$
\boxed{
\text{psychological irrelevance}
\neq
\text{ontological resolution}.
}
$$

---

# 29. Mathematical Non-Usurpation Principle

本篇正式定義：

$$
\boxed{
\text{MNUP}.
}
$$

若：

$$
M,\mathcal A\vdash Q,
$$

則：

$$
Q
$$

只能在：

$$
(M,\mathcal A)
$$

的授權域內被稱為必然。

若要升至：

$$
\mathcal W\models Q,
$$

必須加入：

$$
\boxed{
G(M,\mathcal W,\mathcal A).
}
$$

---

# 30. MNUP 的簡式

$$
\boxed{
\text{Formal Entailment}
+
\text{Grounding}
=
\text{World-Level Warrant}.
}
$$

缺少 Grounding：

$$
\boxed{
\text{Formal Entailment}
\neq
\text{World Fact}.
}
$$

---

# 31. MNUP 的未來版

如果：

$$
M_t,D_t
\Rightarrow
P(F)\approx1,
$$

仍只能得到：

$$
\boxed{
F\text{ is highly projected under current model/evidence}.
}
$$

不能得到：

$$
\boxed{
F\text{ is unrevisably fixed history}.
}
$$

---

# 32. MNUP 的存在論版

若：

$$
M
$$

允許：

$$
O_1,O_2,\ldots
$$

多種 coherent ontologies，

數學本身不能只因某個：

$$
O_k
$$

形式漂亮就決定：

$$
\boxed{
\mathcal W=O_k.
}
$$

這需要額外 metaphysical / empirical argument。

---

# 33. 「所有數學結構都存在」也不是數學 theorem

有人可能主張：

$$
\boxed{
\forall M\in\mathcal M_{\mathrm{consistent}},
\quad M\text{ exists physically/ontologically}.
}
$$

這是一個：

$$
\boxed{
\text{metaphysical thesis}.
}
$$

不是由：

$$
\text{mathematics itself}
$$

推出。

因此即使 mathematical multiverse 論非常有趣，

也要保持 category label。

---

# 34. 數學無法替自己授權成 Ontology

如果有人說：

> 數學結構存在，所以宇宙就是數學。

中間其實加入：

$$
\boxed{
\text{Identity Thesis}:
\mathcal W\equiv M.
}
$$

這個：

$$
\equiv
$$

本身不是一個普通 theorem。

它需要：

$$
\boxed{
\text{philosophy of mathematics + metaphysics}.
}
$$

---

# 35. Simulation Argument 正是 MNUP 的理想案例

Simulation Argument 可以得到：

$$
\boxed{
\text{if }A,B,C,\text{ then }P(S)\text{ can be very high}.
}
$$

很好。

但不能直接把：

$$
A,B,C
$$

當作：

$$
\boxed{
\text{future-established facts}.
}
$$

因此：

$$
\boxed{
\text{conditional strength}
}
$$

與：

$$
\boxed{
\text{premise warrant}
}
$$

要分開。

---

# 36. Magnitude Non-Authority

如果：

$$
N=10^{100},
$$

讓：

$$
P(Q\mid A)
$$

極接近：

$$
1,
$$

這只表示：

$$
\boxed{
\text{once }A\text{ is accepted, }Q\text{ is strongly implied}.
}
$$

不表示：

$$
\boxed{
P(A)\text{ rises merely because }N\text{ is large}.
}
$$

所以：

$$
\boxed{
\text{Magnitude amplifies consequence, not premise warrant}.
}
$$

---

# 37. Precision Non-Authority

同樣，

一個 model 給：

$$
P=0.999873451
$$

看起來很精準。

但如果 parameter：

$$
\theta
$$

本身只是 speculative，

那 decimal places 沒有額外 ontology power。

所以：

$$
\boxed{
\text{numerical precision}
\neq
\text{epistemic precision}.
}
$$

---

# 38. False Precision

假設：

$$
P(Q\mid\theta)=0.9999
$$

但：

$$
\theta
$$

的不確定性極大。

真正應該積分：

$$
P(Q)
=
\int
P(Q\mid\theta)
P(\theta)
d\theta.
$$

若：

$$
P(\theta)
$$

高度 diffuse，

則最終：

$$
P(Q)
$$

可能遠沒有 conditional value 那麼極端。

---

# 39. Conditional Probability 不能省略 Condition

這是最常見的流行化問題。

$$
P(Q\mid A,B,C)
$$

被簡化成：

$$
P(Q).
$$

也就是把：

$$
\boxed{
\mid A,B,C
}
$$

整段刪掉。

這種刪除不是簡化符號。

它改變了命題。

---

# 40. 條件被刪掉後，理論就被升級了

原本：

$$
\boxed{
P(Q\mid A,B,C)\approx1.
}
$$

變成：

$$
\boxed{
P(Q)\approx1.
}
$$

這需要：

$$
P(A,B,C)
$$

的額外資訊。

沒有它，

就是：

$$
\boxed{
\text{Epistemic Inflation}.
}
$$

---

# 41. Epistemic Inflation Chain

本篇統一寫成：

$$
\boxed{
H
\rightarrow
M
\rightarrow
T
\rightarrow
P
\rightarrow
F
\rightarrow
O.
}
$$

其中：

- $H$：hypothesis；
- $M$：model；
- $T$：formal consequence；
- $P$：plausibility；
- $F$：fact treatment；
- $O$：ontological absolutization。

越往右，

所需證據越高。

---

# 42. 每一級都需要 Upgrade Warrant

定義：

$$
U_{i\rightarrow i+1}
$$

為 epistemic upgrade warrant。

例如：

$$
H\rightarrow M
$$

需要 formalization。

$$
M\rightarrow T
$$

需要 proof。

$$
T\rightarrow E
$$

需要 empirical mapping。

$$
E\rightarrow F
$$

需要 predictive confirmation。

$$
F\rightarrow O
$$

需要 metaphysical argument。

不能：

$$
\boxed{
U_{i\rightarrow i+1}=\varnothing
}
$$

卻仍自動升級。

---

# 43. Theory Label Preservation

因此提出：

$$
\boxed{
\text{TLP: Theory Label Preservation}.
}
$$

一個命題在：

$$
L_i
$$

層級，

在沒有：

$$
U_{i\rightarrow i+1}
$$

前，

應保持：

$$
L_i.
$$

例如：

$$
\boxed{
\text{conjecture remains conjecture until upgraded}.
}
$$

---

# 44. 這不是語言潔癖

Label 錯誤會直接影響：

- policy；
- public understanding；
- risk；
- research funding；
- worldview；
- metaphysical belief。

如果：

$$
\text{possible}
$$

被報導成：

$$
\text{proven},
$$

決策就會偏移。

---

# 45. Science Communication 尤其需要 MNUP

例如：

> 科學家證明我們活在模擬裡。

如果原文其實只有：

$$
A,B,C
\Rightarrow
P(S)\text{ high},
$$

那這句報導就跨了：

$$
\boxed{
\text{Conditional}
\rightarrow
\text{Actual}
\rightarrow
\text{Ontological}.
}
$$

三層。

---

# 46. 「Theory」在科學與大眾語言中的差異

在科學中：

$$
\text{theory}
$$

可能有非常高 empirical support。

在一般口語：

$$
\text{theory}
$$

又可能只是猜想。

所以尤其需要明確標：

- conjecture；
- model；
- hypothesis；
- theory；
- theorem；
- observation；
- interpretation。

避免 category collapse。

---

# 47. Formal Model 也不是 Hypothesis 本身

假設：

$$
H
$$

是：

> posthuman civilizations run ancestor simulations.

我們可以建立多個模型：

$$
M_1(H),M_2(H),M_3(H).
$$

所以：

$$
\boxed{
H\neq M.
}
$$

模型只是：

$$
\boxed{
\text{one formalization of }H.
}
$$

---

# 48. 模型結果也可能是 Model-Specific

若：

$$
M_1\vdash Q
$$

但：

$$
M_2\not\vdash Q,
$$

那：

$$
Q
$$

可能依賴：

$$
\boxed{
\text{model choice}.
}
$$

因此 model robustness 也是必要 evidence。

---

# 49. Robustness Requirement

如果：

$$
Q
$$

在：

$$
M_1,M_2,\ldots,M_k
$$

不同合理模型中都出現，

則：

$$
\boxed{
Q\text{ is structurally robust}.
}
$$

但即使如此，

也只提升：

$$
\boxed{
\text{model-level confidence}.
}
$$

不是直接完成 ontology。

---

# 50. Empirical Evidence 也有 Domain Boundary

即使：

$$
E
$$

強力支持：

$$
M
$$

於：

$$
D_1,
$$

也不能自動推出：

$$
M
$$

於：

$$
D_2.
$$

所以：

$$
\boxed{
G(M,\mathcal W\mid D_1)
\not\Rightarrow
G(M,\mathcal W\mid D_2).
}
$$

---

# 51. Extrapolation Distance

定義：

$$
\boxed{
\delta_D
=
d(D_{\mathrm{observed}},D_{\mathrm{claimed}}).
}
$$

若：

$$
\delta_D
$$

很大，

則需要更強 bridge assumptions。

對 posthuman civilization：

$$
\delta_D
$$

可能極大。

---

# 52. Temporal Extrapolation Distance

再定義：

$$
\boxed{
\delta_t
=
t_{\mathrm{future}}-t_{\mathrm{evidence}}.
}
$$

時間距離越大，

不代表預測必然越差，

但：

$$
\boxed{
\text{unmodeled transition risk}
}
$$

通常提高。

---

# 53. Ontological Extrapolation Distance

從：

$$
\text{observed computation}
$$

跳到：

$$
\text{all minds are computational},
$$

再跳到：

$$
\text{all reality is computation},
$$

每一步都增加：

$$
\boxed{
\delta_O.
}
$$

而這種 distance 通常被流行敘事隱藏。

---

# 54. MNUP 三種 Distance

因此可定義：

$$
\boxed{
\Delta
=
(
\delta_D,
\delta_t,
\delta_O
).
}
$$

分別代表：

- domain extrapolation；
- temporal extrapolation；
- ontological extrapolation。

越遠：

$$
\|\Delta\|\uparrow,
$$

越需要：

$$
\boxed{
\text{explicit bridge assumptions}.
}
$$

---

# 55. Future Transcender 是高 $\Delta$ 物件

posthuman / transcendent civilization：

$$
C_T
$$

通常同時具有：

$$
\delta_t\gg0,
$$

$$
\delta_D\gg0,
$$

$$
\delta_O\gg0.
$$

因此：

$$
\boxed{
\text{對 }C_T\text{ 的強斷言應有較高 epistemic burden}.
}
$$

---

# 56. 不能把高能力當成已知心理

即使：

$$
K(C_T)\gg K(\text{human}),
$$

也不代表我們知道：

$$
V(C_T),
$$

其中：

$$
V
$$

是 value structure。

所以：

$$
\boxed{
\text{capability prediction}
\neq
\text{preference prediction}.
}
$$

---

# 57. 不能把計算能力當成模擬意願

若：

$$
\operatorname{CanSimulate}(C_T)=1,
$$

也不推出：

$$
\operatorname{WillSimulate}(C_T)=1.
$$

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Intent}
\neq
\text{Action}.
}
$$

---

# 58. 不能把 action 當成大規模 action

即使：

$$
\operatorname{WillSimulate}(C_T)=1,
$$

也不能推出：

$$
\overline N\gg1.
$$

它可能只跑：

$$
1
$$

個。

或：

$$
10.
$$

或根本不是 ancestor simulation。

所以：

$$
\boxed{
\text{Action Existence}
\neq
\text{Action Scale}.
}
$$

---

# 59. 不能把大規模 simulation 當 conscious observer multiplication

即使：

$$
\overline N\gg1,
$$

若：

$$
P(
\text{conscious observer}
\mid
\text{simulation}
)
$$

未知，

則：

$$
N_{\mathrm{conscious}}
$$

仍未知。

所以：

$$
\boxed{
\text{Simulation Count}
\neq
\text{Conscious Observer Count}.
}
$$

---

# 60. 不能把 observer count 當 self-location probability without principle

再往後：

$$
N_{\mathrm{conscious}}
$$

也不能直接變成：

$$
P(\text{I am simulated})
$$

除非接受：

$$
\boxed{
\text{self-locating inference principle}.
}
$$

因此完整鏈其實很長。

---

# 61. Simulation Probability Chain

可寫：

$$
\boxed{
\text{Capability}
\rightarrow
\text{Intent}
\rightarrow
\text{Action}
\rightarrow
\text{Scale}
\rightarrow
\text{Consciousness}
\rightarrow
\text{Reference Class}
\rightarrow
\text{Self-Location}.
}
$$

每一箭都有獨立 uncertainty。

---

# 62. 這就是為何公式精確不等於世界精確

最終：

$$
P(S)
=
f(
\theta_1,\ldots,\theta_n
).
$$

即使：

$$
f
$$

完全精確，

只要：

$$
\theta_i
$$

高度不確定，

world-level result 仍高度不確定。

所以：

$$
\boxed{
\text{exact function}
\neq
\text{exact world estimate}.
}
$$

---

# 63. Fallibilism

本篇採用：

$$
\boxed{
\text{fallibilism}.
}
$$

也就是：

> 對 empirical world-model 的高度信心，可以是合理的，但原則上仍允許被新 evidence 修正。

形式：

$$
P(M\mid D_t)
$$

可極高，

但：

$$
\boxed{
P(M\mid D_t)=1
}
$$

通常不是必要要求。

---

# 64. Fallibilism 不等於 Eternal Doubt

若 evidence：

$$
E
$$

非常強，

合理：

$$
P(H\mid E)\gg0.99.
$$

可以採取行動。

可以建立制度。

可以做工程。

MNUP 不要求：

$$
\boxed{
\text{永遠什麼都不相信}.
}
$$

---

# 65. 行動門檻與本體確定性不同

Decision threshold：

$$
\tau_D
$$

可以低於：

$$
1.
$$

例如：

$$
P(H)=0.9
$$

就足以採取某 action。

但：

$$
\boxed{
\text{decision sufficiency}
\neq
\text{ontological certainty}.
}
$$

---

# 66. 工程實用也不等於形上真理

模型：

$$
M
$$

可以：

$$
\boxed{
\text{extremely useful}.
}
$$

甚至讓文明建立：

- spacecraft；
- chips；
- AI；
- medicine。

仍不能只由 usefulness 推出：

$$
\boxed{
M\text{ exhausts ultimate reality}.
}
$$

---

# 67. Predictive Success 也不是唯一 Ontology

兩個模型：

$$
M_1,M_2
$$

可能在某 evidence domain：

$$
D
$$

中：

$$
P(E\mid M_1)
\approx
P(E\mid M_2).
$$

這形成：

$$
\boxed{
\text{empirical underdetermination}.
}
$$

因此：

$$
\boxed{
\text{prediction}
}
$$

與：

$$
\boxed{
\text{ontology selection}
}
$$

仍可分離。

---

# 68. Simulation/Base Empirical Equivalence

如 Paper 03：

若：

$$
P(E\mid H_B)=P(E\mid H_S)
$$

對所有可做 internal experiments 都相等，

則：

$$
H_B
\sim_{\mathrm{emp}}
H_S.
$$

在沒有新的 cross-layer evidence 前，

數學不能自行決定：

$$
\boxed{
H_B
}
$$

或：

$$
\boxed{
H_S
}
$$

哪個就是 actuality。

---

# 69. 理論可以限制，但不一定唯一選擇

這是 MNUP 的較弱形式：

$$
\boxed{
\text{mathematics can eliminate incoherent possibilities}.
}
$$

它可以告訴我們：

$$
S_1
$$

矛盾，

$$
S_2
$$

不滿足 conservation，

$$
S_3
$$

不能 normalization。

很好。

但剩下：

$$
S_4,S_5,S_6
$$

時，

數學不必然獨自決定 actuality。

---

# 70. Possibility Filter，不是 Reality Sovereign

因此：

$$
\boxed{
\text{Mathematics}
=
\text{powerful possibility/constraint filter}.
}
$$

不是：

$$
\boxed{
\text{unilateral sovereign over actuality}.
}
$$

這就是「非僭越」的真正意思。

---

# 71. 非僭越不是限制數學，而是限制錯誤推論者

數學本身不會：

> 僭越。

僭越的是：

$$
\boxed{
\text{the interpreter}.
}
$$

也就是使用者將：

$$
M\models Q
$$

誤讀成：

$$
\mathcal W\models Q.
$$

所以 MNUP 最終是：

$$
\boxed{
\text{a discipline on inference and interpretation}.
}
$$

---

# 72. 數學不需要替自己的強大道歉

恰恰相反。

因為數學能：

$$
\boxed{
\text{make assumptions explicit}.
}
$$

所以它也是防止 epistemic inflation 的最好工具之一。

真正應做的是：

$$
\boxed{
\text{把前提全部寫出來}.
}
$$

---

# 73. Assumption Ledger

任何未來 ontology model 應附：

$$
\boxed{
\mathcal L_A
=
\{A_1,A_2,\ldots,A_n\}.
}
$$

每個 assumption 標：

- observed；
- inferred；
- theoretical；
- speculative；
- metaphysical。

這樣：

$$
Q
$$

的 epistemic status 才能追溯。

---

# 74. Warrant Ledger

同樣：

$$
\boxed{
\mathcal L_W
=
\{W_{i\rightarrow j}\}.
}
$$

記每次 epistemic upgrade 的依據。

例如：

$$
H\rightarrow M:
\text{formalization},
$$

$$
M\rightarrow E:
\text{empirical fit},
$$

$$
E\rightarrow F:
\text{forecast validation},
$$

$$
F\rightarrow O:
\text{metaphysical interpretation}.
$$

---

# 75. 不允許 Silent Upgrade

若：

$$
W_{i\rightarrow i+1}
$$

沒有，

則：

$$
\boxed{
L_i
}
$$

不能 silent 升成：

$$
L_{i+1}.
$$

這就是：

$$
\boxed{
\text{No Silent Epistemic Upgrade Rule}.
}
$$

---

# 76. 本系列對 Simulation Argument 的最終位置

Paper 01：

$$
\boxed{
\text{Conditional Argument}
\neq
\text{Verified Ontology}.
}
$$

Paper 02：

$$
\boxed{
\text{Simulator}
\neq
\text{Ultimate Ground}.
}
$$

Paper 03：

$$
\boxed{
\text{Simulated}
\neq
\text{Unreal}.
}
$$

Paper 04：

$$
\boxed{
\text{Mathematical Model}
\neq
\text{Self-Authorizing Reality Claim}.
}
$$

四篇形成完整 closure。

---

# 77. 四篇其實對稱地拆了四種錯誤

## Error 1 — Probability Inflation

$$
P(Q\mid A)
\rightarrow
P(Q).
$$

## Error 2 — Creator Inflation

$$
\operatorname{Creator}(W_i)
\rightarrow
\operatorname{Ultimate}.
$$

## Error 3 — Reality Deflation

$$
\operatorname{Simulated}(W_i)
\rightarrow
\operatorname{Unreal}(W_i).
$$

## Error 4 — Mathematical Usurpation

$$
M\models Q
\rightarrow
\mathcal W\models Q.
$$

---

# 78. 這四種錯誤其實有共同結構

它們都是：

$$
\boxed{
\text{relation/domain-specific predicate}
\rightarrow
\text{unqualified global predicate}.
}
$$

例如：

$$
\operatorname{CreatorOf}(A,W)
$$

被偷換成：

$$
\operatorname{Ultimate}(A).
$$

$$
\operatorname{Simulated}(W\mid H)
$$

被偷換成：

$$
\operatorname{Unreal}(W).
$$

$$
M\models Q
$$

被偷換成：

$$
\mathcal W\models Q.
$$

---

# 79. 因此本系列真正研究的是「取消條件詞」的危險

很多哲學誤讀來自刪除：

$$
\boxed{
\mid
}
$$

例如：

$$
\operatorname{GodLike}(A\mid W)
$$

變成：

$$
\operatorname{God}(A).
$$

$$
P(S\mid A,B,C)
$$

變成：

$$
P(S).
$$

$$
\operatorname{Real}(W\mid O)
$$

變成單一真假二分。

所以：

$$
\boxed{
\text{context erasure}
}
$$

是 epistemic inflation 的常見機制。

---

# 80. Context Preservation Principle

本篇最後再提出：

$$
\boxed{
\text{CPP: Context Preservation Principle}.
}
$$

若一個 predicate：

$$
P(x\mid C)
$$

只在 context：

$$
C
$$

中成立，

不得未經論證刪除：

$$
C.
$$

所以：

$$
\boxed{
P(x\mid C)
\not\Rightarrow
P(x).
}
$$

---

# 81. MNUP 與 CPP 的關係

MNUP：

$$
\boxed{
\text{model context cannot be silently erased}.
}
$$

CPP：

$$
\boxed{
\text{relation context cannot be silently erased}.
}
$$

兩者共同防止：

$$
\boxed{
\text{local truth}
\rightarrow
\text{global absolutization}.
}
$$

---

# 82. Future Ontology 應被標記為 Scenario Space

對未來：

$$
\mathcal F
$$

最好寫成：

$$
\boxed{
\mathcal F
=
\{
(F_i,P_i,\mathcal A_i)
\}.
}
$$

其中每個：

$$
F_i
$$

都附：

- probability；
- assumptions；
- evidence；
- model dependence。

而不是選一條：

$$
F^*
$$

直接宣告：

$$
\boxed{
\text{this is the future}.
}
$$

---

# 83. 未來不是由模型單方面生成的

模型：

$$
M_t
$$

只是：

$$
\boxed{
\text{our current compression of possibilities}.
}
$$

真正未來：

$$
\mathcal W_{t+n}
$$

由：

- physical processes；
- agents；
- choices；
- accidents；
- new technologies；
- new constraints；
- unknown factors

共同產生。

所以：

$$
\boxed{
M_t
\neq
\mathcal W_{t+n}.
}
$$

---

# 84. Choice 也是 Future Uncertainty 的一部分

若 agents：

$$
A_i
$$

具有：

$$
\boxed{
\text{nontrivial decision spaces},
}
$$

那未來並非只是一條目前已知 trajectory。

至少在模型層：

$$
\mathcal T
=
\{
\tau_1,\tau_2,\ldots
\}.
$$

所以 prediction：

$$
\boxed{
\text{must respect branching}.
}
$$

---

# 85. 即使 Deterministic，也未必 Predictable

就算底層：

$$
W(t+1)=F(W(t))
$$

是 deterministic，

只要：

- initial-state uncertainty；
- chaos；
- computational irreducibility；
- observer limitation

存在，

則：

$$
\boxed{
\text{determinism}
\neq
\text{practical predictability}.
}
$$

所以未來僭越也不能靠：

> 宇宙可能決定論。

自動解決。

---

# 86. 第一因與終極因更不能被 Future Math 偷渡

如果 posthuman model：

$$
M_P
$$

產生一個：

$$
C^*
$$

具有巨大創造力，

也不能：

$$
\boxed{
C^*
\rightarrow
\text{Ultimate Ground}.
}
$$

這正是 Paper 02。

所以數學能力：

$$
\boxed{
\text{cannot manufacture metaphysical ultimacy by extrapolation}.
}
$$

---

# 87. 能描述一個 Ultimate Being 也不代表它存在

反方向亦然。

如果：

$$
G
$$

可被形式化成：

$$
G=(N,O,P,\ldots),
$$

這只表示：

$$
\boxed{
\text{a formal concept has been specified}.
}
$$

不能由：

$$
\operatorname{Consistent}(G)
$$

直接推出：

$$
\operatorname{Exists}(G).
$$

因此 MNUP 對有神論、無神論與 simulation metaphysics 都對稱。

---

# 88. MNUP 不偏袒任何 Ontology

它不預設：

$$
\text{materialism}.
$$

不預設：

$$
\text{simulationism}.
$$

不預設：

$$
\text{theism}.
$$

不預設：

$$
\text{mathematical universe}.
$$

它只要求：

$$
\boxed{
\text{每一層 claim 使用與其證據相稱的 label}.
}
$$

---

# 89. Evidence-Proportional Ontology

本篇提出：

$$
\boxed{
\text{EPO: Evidence-Proportional Ontology}.
}
$$

本體論 claim strength：

$$
O_s
$$

不應大於：

$$
\boxed{
\text{evidence + argument warrant}.
}
$$

粗略：

$$
O_s
\le
f(E,A,G).
$$

不是：

$$
O_s
=
f(\text{mathematical elegance}).
$$

---

# 90. Elegance 是 Theory Virtue，不是 World Proof

數學模型：

$$
M
$$

可能：

- simple；
- symmetric；
- beautiful；
- compressive。

這些是：

$$
\boxed{
\text{theoretical virtues}.
}
$$

但：

$$
\boxed{
\text{beauty}
\neq
\text{empirical identification}.
}
$$

---

# 91. Compression 也不自動等於 Ontology

如果：

$$
L(M_1)<L(M_2),
$$

表示：

$$
M_1
$$

description length 更短。

這可能增加模型偏好。

但：

$$
\boxed{
\arg\min L(M)
}
$$

不能單獨推出：

$$
\boxed{
M=\mathcal W.
}
$$

---

# 92. Occam 也是 Selection Principle，不是 Reality Oracle

Occam's razor 可以：

$$
\boxed{
\text{prefer simpler adequate models}.
}
$$

它不是：

$$
\boxed{
\text{proof that reality must instantiate the simplest model}.
}
$$

---

# 93. Bayesian 更新也不能替 Prior 來源消失

若：

$$
P(H\mid E)
\propto
P(E\mid H)P(H),
$$

則 posterior 依賴：

$$
P(H).
$$

在極端 speculative ontology 中，

prior：

$$
P(H)
$$

本身可能高度 uncertain。

所以：

$$
\boxed{
\text{Bayesian formalism}
\neq
\text{objective ontology oracle}.
}
$$

---

# 94. Probability Model 必須標記其 Reference Class

尤其 anthropic questions：

$$
P(H\mid E,\mathcal R).
$$

如果：

$$
\mathcal R
$$

改變，

result 可能改。

所以：

$$
\boxed{
\mathcal R
}
$$

不能隱藏。

這也是 MNUP 的 context-preservation 要求。

---

# 95. 理論真正成熟的標誌不是「敢下絕對結論」

反而是：

$$
\boxed{
\text{知道自己哪裡還不能下結論}.
}
$$

一個成熟 model 應能列出：

- assumptions；
- domain；
- uncertainty；
- falsifiers；
- alternatives；
- update conditions。

---

# 96. Falsifiability / Revisability

對 empirical hypothesis：

$$
H,
$$

至少應問：

$$
\boxed{
\text{What evidence would make us reduce credence in }H?
}
$$

若答案是：

> 任何 evidence 都能被重新解釋成支持 H。

那：

$$
H
$$

的 empirical status 需要重新評估。

---

# 97. Simulation Hypothesis 尤其要避免 Elasticity

若：

- 有異常 → simulator 留下痕跡；
- 沒異常 → simulator 太高明；
- 可觀測 → simulation；
- 不可觀測 → simulation 仍可能；

那 hypothesis 很容易變成：

$$
\boxed{
\text{empirically elastic}.
}
$$

這不表示它必假。

但表示：

$$
\boxed{
\text{empirical confirmation becomes difficult}.
}
$$

---

# 98. 可能性不能自己累積成證據

如果：

$$
H
$$

能解釋任何 outcome：

$$
E_i,
$$

那：

$$
P(E_i\mid H)
$$

可能都不低。

但如果 competitor：

$$
H'
$$

同樣可以，

Bayes factor：

$$
\frac{P(E_i\mid H)}{P(E_i\mid H')}
$$

就未必有力。

所以：

$$
\boxed{
\text{explainability}
\neq
\text{discriminative evidence}.
}
$$

---

# 99. 世界可被數學描述，不等於世界只剩數學

即使：

$$
\mathcal W
$$

高度 mathematical regular，

仍可區分：

$$
\boxed{
\text{mathematical describability}
}
$$

與：

$$
\boxed{
\text{ontological identity with mathematics}.
}
$$

後者需要額外 thesis。

---

# 100. Final Mathematical Non-Usurpation Principle

本篇最終給出完整版：

$$
\boxed{
\begin{aligned}
&\text{If }M,\mathcal A\vdash Q,\\
&\text{then }Q\text{ is warranted as a conditional result within }(M,\mathcal A).\\
&\text{To promote }Q\text{ into an empirical, historical, future, or ontological claim,}\\
&\text{an explicit grounding and upgrade warrant appropriate to that level is required.}
\end{aligned}
}
$$

簡寫：

$$
\boxed{
M,\mathcal A\vdash Q
+
G
+
U
\Rightarrow
\text{higher-level warrant}.
}
$$

沒有：

$$
G,U,
$$

則：

$$
\boxed{
\text{no silent promotion}.
}
$$

---

# 101. 系列四篇最終統合

## Paper 01 — Epistemic Boundary

$$
\boxed{
P(S\mid A,B,C)
\neq
P(S).
}
$$

## Paper 02 — Recursive Ontological Non-Closure

$$
\boxed{
\operatorname{Creator}(W_i)
\neq
\operatorname{Ultimate}.
}
$$

## Paper 03 — Reality Restructuring

$$
\boxed{
\operatorname{Simulated}(W_i)
\neq
\operatorname{Unreal}(W_i).
}
$$

## Paper 04 — Mathematical Non-Usurpation

$$
\boxed{
M\models Q
\neq
\mathcal W\models Q.
}
$$

---

# 102. Series Unified Error Pattern

四篇共同處理：

$$
\boxed{
\text{Contextual Claim}
\rightarrow
\text{Context Erasure}
\rightarrow
\text{Global Absolutization}.
}
$$

因此本系列最深的統一敵人不是：

$$
\text{Simulation Hypothesis}.
$$

而是：

$$
\boxed{
\text{unlicensed removal of conditions}.
}
$$

---

# 103. Series Unified Principle

可以壓縮成：

$$
\boxed{
\text{Never delete the condition bar without a warrant}.
}
$$

也就是：

$$
P(Q\mid C)
\not\Rightarrow
P(Q),
$$

$$
\operatorname{Creator}(A\mid W)
\not\Rightarrow
\operatorname{Ultimate}(A),
$$

$$
\operatorname{Simulated}(W\mid H)
\not\Rightarrow
\operatorname{Unreal}(W),
$$

$$
M\models Q
\not\Rightarrow
\mathcal W\models Q.
$$

---

# 104. 這也是對 Future Theory 的要求

未來理論應寫：

$$
\boxed{
\text{If current assumptions remain valid...}
}
$$

而不是：

$$
\boxed{
\text{the future must be...}
}
$$

尤其當：

$$
\delta_t,\delta_D,\delta_O
$$

都很大時。

---

# 105. 最終認識論位置

我們可以：

- 大膽提出假說；
- 大膽建立模型；
- 大膽做數學；
- 大膽做未來推演；
- 大膽做本體論。

但每一步都必須：

$$
\boxed{
\text{標明自己在哪一層}.
}
$$

這才是：

$$
\boxed{
\text{epistemic discipline}.
}
$$

---

# 106. Final Internal Seal

本篇封存八個核心命題。

第一：

$$
\boxed{
\text{Mathematical validity is conditional on a specified formal context}.
}
$$

第二：

$$
\boxed{
\text{Model validity does not self-authorize model-world identity}.
}
$$

第三：

$$
\boxed{
\text{Future projection is not future observation}.
}
$$

第四：

$$
\boxed{
\text{Unknown posthuman behavior must increase uncertainty rather than selectively support preferred projections}.
}
$$

第五：

$$
\boxed{
\text{Magnitude and numerical precision do not create premise warrant}.
}
$$

第六：

$$
\boxed{
\text{Empirical success does not by itself prove final ontology}.
}
$$

第七：

$$
\boxed{
\text{No epistemic level may be silently promoted without an explicit upgrade warrant}.
}
$$

第八：

$$
\boxed{
\text{Mathematics can constrain possible worlds without usurping the authority to declare which world is actual}.
}
$$

因此：

$$
\boxed{
\text{Mathematics is strongest when it does not pretend to be more than mathematics}.
}
$$

而：

$$
\boxed{
\text{a theory is not weakened by correctly calling it a theory}.
}
$$

---

# 107. Series Closure

整個系列現在完成：

$$
\boxed{
\text{Conditional Probability}
\rightarrow
\text{Recursive Transcendence}
\rightarrow
\text{Layered Reality}
\rightarrow
\text{Mathematical Non-Usurpation}.
}
$$

最終不需要證明：

$$
\boxed{
\text{we are simulated}.
}
$$

也不需要證明：

$$
\boxed{
\text{we are not simulated}.
}
$$

真正完成的是一個更基礎的框架：

> 無論 simulation hypothesis 最終是真是假，我們都應把條件式推論、遞歸層級、真實性、主體自主權與數學模型的認識論邊界分開。

最後：

$$
\boxed{
\text{Conjecture remains conjecture until warrant changes its status}.
}
$$

即使 status 已被提升：

$$
\boxed{
\text{empirical knowledge remains open to domain refinement and future revision}.
}
$$

而：

$$
\boxed{
\text{formal truth remains formal truth without needing to impersonate ontology}.
}
$$

---

## Final Series Status

**Paper 01** — Simulation Argument 的邊界：條件機率、命題猜想與存在論誤讀  
**Paper 02** — 超越者之上的超越者：Simulation Argument 的遞歸未閉包問題  
**Paper 03** — 模擬不等於虛假：真實性、主體性、自主權與跨層主權  
**Paper 04** — 數學非僭越原則：從可能世界模型到未來存在論的認識論邊界  

$$
\boxed{
\text{Series theoretical closure = COMPLETE}.
}
$$

後續若再往下推，

就應回到既有更大的理論鏈：

- Architect / Ultimate Ground；
- 系統超越者；
- 跨層干涉；
- 可達世界狀態；
- 第一因與終極因；
- 自由意志與選擇本體論。

不需要在本系列中重複展開。
