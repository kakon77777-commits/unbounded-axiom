# LSI-PSD-09 — 生產性錯置窗口：真理、錯誤與知識肥沃性的非單調曲線

## The Productive Mis-specification Window: Non-Monotonic Epistemic Fertility Between Fidelity and Error

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 09  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Productive Mis-specification Window Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文提出「生產性錯置窗口」作為**可證偽的經驗性假說族**，不主張所有科學、數學或工程問題都存在 inverted-U 型肥沃性曲線，也不主張偏離真理必然提高創造力。本文特別拒絕「越錯越有用」與「故意把問題問錯可以更接近真理」兩種推論。本文只提出：在某些受約束研究域中，零偏差、高度結構化的有限偏差與大幅隨機偏差，可能具有不同的 audited generativity；若中等程度的**結構化偏差**在 descendant survival、transferability、repairability 與 independent verification 上優於零偏差及隨機偏差，則可說該 domain 在指定任務與研究制度下呈現 productive-mis-specification window。若資料不支持內部高值區，窗口假說應被拒絕。

---

## 摘要

LSI-PSD-07 已指出 truth/fidelity、closure、generativity 與 utility 不必單調同向；LSI-PSD-08 進一步提出，parent problem 被修正後，部分 descendant knowledge 可能經 post-revision audit 存活。本文把這兩個命題推到下一個可測層次：**是否存在一個有限偏差區間，使研究系統的認識論肥沃性高於零偏差與大偏差兩端？**

令某一 domain 中的參照 parent 為：

$$
P^\star,
$$

研究變體為：

$$
P_\epsilon,
$$

並令：

$$
\epsilon
=
d(P_\epsilon,P^\star).
$$

若只用單一距離，會把不同種類的偏差錯誤地混在一起，因此本文將偏差分解為：

$$
\boldsymbol\epsilon
=
(
\epsilon_Q,
\epsilon_D,
\epsilon_A,
\epsilon_L,
\epsilon_M,
\epsilon_R
),
$$

分別表示 question、domain、assumptions、representation、model/method 與 research-regime 的偏移。進一步定義 **Structured Deviation Index**：

$$
\operatorname{SDI}(P_\epsilon)
=
B(\epsilon)
\cdot
L(\epsilon)
\cdot
C(\epsilon)
\cdot
R(\epsilon),
$$

其中 $B$ 為 boundedness、 $L$ 為 localization、 $C$ 為 comparability、 $R$ 為 repairability。任意錯誤可以有大的 $\|\boldsymbol\epsilon\|$，但若：

$$
\operatorname{SDI}\approx0,
$$

它通常不屬於本文所說的 productive deviation。

本文把認識論肥沃性定義為一個多維函數：

$$
\Phi_E
=
\Phi_E(
G_A,
S_D,
T_D,
R_D,
C_D,
Z_K,
C_{\mathrm{cost}}
),
$$

其中：

- $G_A$：audited non-equivalent generativity；
- $S_D$：parent revision 後 descendant survival；
- $T_D$：transferability；
- $R_D$：robustness；
- $C_D$：audit coverage；
- $Z_K$：zombie-knowledge rate；
- $C_{\mathrm{cost}}$：研究成本。

最簡化的 task-conditioned 形式可寫：

$$
\Phi_E^{\mathcal T}
=
\frac{
G_A^\alpha
S_D^\beta
T_D^\gamma
R_D^\eta
C_D^\kappa
}{
(1+\lambda Z_K)
(1+\mu C_{\mathrm{cost}})
}.
$$

本文不把這個公式當作自然定律，而把它當成可審計的 measurement template。

生產性錯置窗口定義為：

$$
\boxed{
\mathcal W_P^{\mathcal T,R}
=
\left\{
\boldsymbol\epsilon:
\Phi_E^{\mathcal T,R}(\boldsymbol\epsilon)
>
\max[
\Phi_E^{\mathcal T,R}(0)+\Delta_0,
\Phi_E^{\mathcal T,R}(\boldsymbol\epsilon_{\mathrm{rand}})+\Delta_r
]
\right\}.
}
$$

也就是：只有當一個有限、結構化、可定位、可修正的偏差，在相同預算下產生更多**可驗證且能在 parent 修正後存活的後代知識**，並顯著勝過零偏差基線與隨機偏差基線，才有資格稱為 productive window。

本文進一步提出四種可能 empirical shape：

1. monotone fidelity-dominant；
2. monotone deviation-dominant；
3. interior-window / inverted-U；
4. multi-peak / phase-structured。

因此 inverted-U 只是候選，不是預設真理。窗口還可能具有 task dependence、representation dependence、budget dependence、model dependence 與 hysteresis。相同偏差：

$$
\boldsymbol\epsilon
$$

對人類、LLM、formal prover 或不同工具鏈，可能落在不同區域。

2025--2026 年的科學哲學與模型發現研究為這一框架提供相鄰證據。Batterman 與 Rice 的 minimal-model work 顯示，解釋力可來自移除微觀細節而暴露大尺度不變結構；King 2025 對「ugly models」的研究強調 pursuit-worthiness 是在有限資源與不完整證據下的研究選擇問題；2026 年 physics-guided operator correction 將 misspecified prior physics 與 learned correction 分開，而不是讓黑箱覆蓋整體物理；LISDD 2026 將 discrepancy 局部化到特定 regime，再回復缺失符號機制；Experimental Design for Missing Physics 與 Bayesian Inference for Missing Physics 進一步把「未知模型結構」變成可主動設計實驗、可量化 posterior uncertainty 的研究對象。這些工作不證明 inverted-U，但共同顯示：**偏差的大小之外，偏差是否結構化、局部化、可比較與可修正，是決定其知識價值的核心變量。**

本文最後提出一組可直接實驗的 benchmark。對已知 ground-truth 系統，逐步注入不同強度與不同類型的偏差：

$$
\boldsymbol\epsilon_0,
\boldsymbol\epsilon_1,
\ldots,
\boldsymbol\epsilon_m,
$$

再讓 AI 生成研究 descendants；最後揭示 ground truth、執行 parent revision、重新 audit 全部 descendants，測：

$$
G_A,
S_D,
T_D,
R_D,
Z_K,
\Phi_E.
$$

若 structured intermediate deviations 穩定產生內部高值區，則支持窗口假說；若零偏差始終最佳，則支持 fidelity-dominant regime；若偏差越大越高，則必須檢查 measurement 是否把 raw novelty 誤當 epistemic value；若不同偏差類型呈多峰結構，則單一 $\epsilon$ 模型應被放棄。

本文最終提出：

$$
\boxed{
\textbf{The epistemically productive region, if it exists, is a structured window, not an invitation to error.}
}
$$

以及：

$$
\boxed{
\textbf{A productive window is established by descendant survival and controlled comparison, not by the sheer volume of generated theory.}
}
$$

**關鍵詞：** 生產性錯置窗口、productive mis-specification window、epistemic fertility、structured deviation、inverted-U、model discrepancy、missing physics、idealization、descendant survival、AI science、proof-space dynamics、research routing

---

# 1. 問題的提出：從「錯誤有時有用」到「到底錯到哪裡才有用」

LSI-PSD-08 已經建立：

$$
\operatorname{Fail}(P)
\not\Rightarrow
\forall d\in\mathcal D(P),
\operatorname{Fail}(d).
$$

但是這個命題還太弱。

因為它只說：

> 錯 parent 的部分 descendants 可能存活。

它沒有回答：

> 什麼種類、什麼強度的偏差最容易產生可存活 descendants？

本文正是處理這個問題。

---

# 2. 一個非常容易被濫用的直覺

從 Carnot、ideal gas、effective theory、minimal model 等案例，很容易產生一句危險話：

> 看吧，錯誤反而更有創造力。

這句話把至少四個不同東西混在一起：

$$
\text{controlled idealization},
$$

$$
\text{limited-domain model},
$$

$$
\text{accidental misspecification},
$$

$$
\text{arbitrary error}.
$$

它們不等價。

---

# 3. 任意錯誤空間遠大於有用錯置空間

如果一個模型有：

$$
n
$$

個自由參數，

任意 perturbation：

$$
\epsilon\in\mathbb R^n
$$

有巨大體積。

真正能：

- 保留主要結構；
- 產生可比較 residual；
- 允許 correction；
- 生成可驗證 descendants；

的偏差只佔其中非常小的部分。

因此：

$$
\boxed{
\text{productive deviation}
\subsetneq
\text{all deviation}.
}
$$

---

# 4. 偏差必須向量化

單一：

$$
\epsilon
$$

太粗。

本文定義：

$$
\boldsymbol\epsilon
=
(
\epsilon_Q,
\epsilon_D,
\epsilon_A,
\epsilon_L,
\epsilon_M,
\epsilon_R
).
$$

其中：

$$
\epsilon_Q
$$

表示問題 statement 偏移；

$$
\epsilon_D
$$

表示 domain / scope 偏移；

$$
\epsilon_A
$$

表示 assumption 偏移；

$$
\epsilon_L
$$

表示 language / representation 偏移；

$$
\epsilon_M
$$

表示 model / method family 偏移；

$$
\epsilon_R
$$

表示 research-regime 偏移。

---

# 5. 同樣的距離，不同方向可以完全不同

假設：

$$
\|\boldsymbol\epsilon_1\|
=
\|\boldsymbol\epsilon_2\|.
$$

但：

$$
\boldsymbol\epsilon_1
=
(0,0,\delta,0,0,0),
$$

只是移除一個非關鍵 assumption。

另一個：

$$
\boldsymbol\epsilon_2
=
(\delta,0,0,0,0,0),
$$

卻改變 theorem quantifier。

兩者 epistemic effect 可能完全不同。

因此：

$$
\boxed{
\|\boldsymbol\epsilon\|
\text{ alone is insufficient}.
}
$$

---

# 6. 偏差方向比偏差大小更重要

定義：

$$
\hat{\epsilon}
=
\frac{
\boldsymbol\epsilon
}{
\|\boldsymbol\epsilon\|
}.
$$

生產性應寫：

$$
\Phi_E
=
\Phi_E(
\|\boldsymbol\epsilon\|,
\hat{\epsilon}
).
$$

這意味著 productive window 不是一條實數線上的 interval，

而可能是一個：

$$
\boxed{
\text{anisotropic region in deviation space}.
}
$$

---

# 7. Structured Deviation Index

為了區分有結構偏差與 random noise，本文定義四個分量。

## 7.1 Boundedness

$$
B(\epsilon)\in[0,1].
$$

偏差是否有限、可描述、非無界漂移。

## 7.2 Localization

$$
L(\epsilon)\in[0,1].
$$

是否知道：

$$
\epsilon
$$

發生在哪個 regime／term／assumption。

## 7.3 Comparability

$$
C(\epsilon)\in[0,1].
$$

是否能與 baseline 或 target 做受控比較。

## 7.4 Repairability

$$
R(\epsilon)\in[0,1].
$$

是否存在合理 correction path。

---

# 8. SDI 定義

$$
\boxed{
\operatorname{SDI}(\epsilon)
=
B(\epsilon)
L(\epsilon)
C(\epsilon)
R(\epsilon).
}
$$

如果任一項接近零：

$$
\operatorname{SDI}\rightarrow0.
$$

---

# 9. 為什麼用乘積而不是加總

若偏差完全不可定位：

$$
L=0,
$$

即使：

$$
B=C=R=1,
$$

也不應叫高 structured deviation。

乘積讓：

$$
\text{critical missing dimension}
$$

直接壓低 SDI。

這是一個工程選擇，不是自然定律。

---

# 10. Random deviation baseline

定義：

$$
\boldsymbol\epsilon_{\mathrm{rand}}
$$

與：

$$
\boldsymbol\epsilon_{\mathrm{struct}}
$$

具有近似相同 norm：

$$
\|\epsilon_{\mathrm{rand}}\|
\approx
\|\epsilon_{\mathrm{struct}}\|.
$$

但前者：

$$
\operatorname{SDI}\approx0.
$$

後者：

$$
\operatorname{SDI}\gg0.
$$

---

# 11. 窗口假說真正比較的不是 0 和 error

而是三組：

$$
\boxed{
\text{baseline}
\quad
\text{structured deviation}
\quad
\text{random deviation}.
}
$$

沒有 random control，

「偏差提高 generativity」幾乎沒有意義。

---

# 12. Epistemic fertility 需要 task conditioning

設任務：

$$
\mathcal T.
$$

例如：

- theorem discovery；
- mechanism discovery；
- engineering approximation；
- explanation；
- transfer；
- experiment design。

則：

$$
\Phi_E
=
\Phi_E^{\mathcal T}.
$$

同一 model 在不同 task 可有不同 productive window。

---

# 13. Research regime conditioning

再加入：

$$
R.
$$

因此：

$$
\boxed{
\Phi_E^{\mathcal T,R}(\epsilon).
}
$$

不同：

- model；
- prover；
- retriever；
- budget；
- memory；
- verifier；

都可能改變曲線。

---

# 14. 生產性窗口的第一版定義

$$
\boxed{
\mathcal W_P^{\mathcal T,R}
=
\left\{
\epsilon:
\Phi_E^{\mathcal T,R}(\epsilon)
>
\tau_\Phi
\right\}.
}
$$

但這還不夠。

因為 baseline 自己可能已經很高。

---

# 15. 相對窗口

更嚴格：

$$
\mathcal W_{P,\mathrm{rel}}^{\mathcal T,R}
=
\left\{
\epsilon:
\Phi_E(\epsilon)
>
\Phi_E(0)+\Delta_0
\right\}.
$$

---

# 16. Random-control window

再要求：

$$
\Phi_E(\epsilon)
>
\mathbb E[
\Phi_E(\epsilon_{\mathrm{rand}})
]
+
\Delta_r.
$$

才可以叫：

$$
\boxed{
\text{productive deviation}.
}
$$

---

# 17. 完整窗口

因此：

$$
\boxed{
\mathcal W_P^{\mathcal T,R}
=
\left\{
\epsilon:
\Phi_E(\epsilon)
>
\max[
\Phi_E(0)+\Delta_0,
\mathbb E\Phi_E(\epsilon_{\mathrm{rand}})+\Delta_r
]
\right\}.
}
$$

---

# 18. 為什麼要加 $\Delta$

若只要求：

$$
\Phi_E(\epsilon)>\Phi_E(0),
$$

微小 sampling noise 都可能造成假窗口。

因此：

$$
\Delta_0,\Delta_r
$$

應由：

- confidence interval；
- permutation；
- bootstrap；
- multiple-testing correction；

決定。

---

# 19. Window 不是一定連通

最簡單想像：

$$
[\epsilon_1,\epsilon_2].
$$

但高維偏差空間可能：

$$
\mathcal W_P
=
W_1\cup W_2\cup W_3.
$$

因此稱「window」只是直觀語言。

數學上更像：

$$
\boxed{
\text{productive region}.
}
$$

---

# 20. 四種基本曲線

## 20.1 Fidelity-dominant

$$
\frac{d\Phi_E}{d\epsilon}<0.
$$

零偏差最好。

## 20.2 Deviation-dominant

在測試範圍內：

$$
\frac{d\Phi_E}{d\epsilon}>0.
$$

這通常需要高度警惕 measurement 問題。

## 20.3 Interior-window

存在：

$$
\epsilon^\star>0
$$

使：

$$
\Phi_E(\epsilon^\star)
>
\Phi_E(0).
$$

## 20.4 Multi-peak

存在多個：

$$
\epsilon_i^\star.
$$

表示不同結構偏差各自開出不同 productive basin。

---

# 21. Inverted-U 只是第三種

所以本文不把：

$$
\cap
$$

形曲線當作預設。

它只是：

$$
\boxed{
H_{\mathrm{window}}.
}
$$

---

# 22. 可證偽條件一

若在多個 domain、model、budget 下：

$$
\Phi_E(0)
\ge
\Phi_E(\epsilon)
$$

對所有結構化偏差都成立，

則 productive-window 假說在該 domain 被拒絕。

---

# 23. 可證偽條件二

若 structured deviation：

$$
\Phi_E(\epsilon_{\mathrm{struct}})
$$

不顯著高於 norm-matched random deviation，

則：

$$
\text{structure hypothesis}
$$

失敗。

---

# 24. 可證偽條件三

若所謂高 generativity 在 parent revision 後：

$$
S_D\rightarrow0,
$$

則原高峰只是：

$$
\boxed{
\text{error amplification peak}.
}
$$

不是 productive window。

---

# 25. 可證偽條件四

若高峰完全由：

$$
G_{\mathrm{raw}}
$$

驅動，

而：

$$
G_A
$$

沒有上升，

窗口應被撤銷。

---

# 26. 可證偽條件五

若 audit coverage：

$$
C_D
$$

過低，

任何 window claim 應標：

$$
\text{underdetermined}.
$$

---

# 27. Fertility vector

不要只用一個 scalar。

定義：

$$
\mathbf F_E
=
(
G_A,
S_D,
T_D,
R_D,
C_D,
1-Z_K,
1-C_{\mathrm{cost}}
).
$$

---

# 28. Scalar 只用於 task-specific ranking

若一定需要：

$$
\Phi_E^{\mathcal T}
=
U_{\mathcal T}(\mathbf F_E).
$$

不同任務：

$$
U_{\mathcal T}
$$

不同。

---

# 29. 一個可用的示範形式

$$
\Phi_E^{\mathcal T}
=
\frac{
G_A^\alpha
S_D^\beta
T_D^\gamma
R_D^\eta
C_D^\kappa
}{
(1+\lambda Z_K)
(1+\mu C_{\mathrm{cost}})
}.
$$

所有 exponent 與 weight 都必須預註冊或做 sensitivity analysis。

---

# 30. 避免事後調權重

如果先看到資料，

再調：

$$
\alpha,\beta,\gamma,\ldots
$$

把曲線調成 inverted-U，

則結果無效。

所以實驗前要：

$$
\boxed{
\text{preregister metric family}.
}
$$

---

# 31. Sensitivity analysis

對多組：

$$
\mathbf w^{(1)},\ldots,\mathbf w^{(m)}
$$

重算。

如果 window 只在單一極端權重出現，

robustness 低。

---

# 32. Window robustness

定義：

$$
R_W
=
P(
\epsilon\in\mathcal W_P
\mid
\text{reasonable metric choices}
).
$$

---

# 33. Window width

若一維：

$$
W
=
\epsilon_{\max}
-
\epsilon_{\min}.
$$

高：

$$
W
$$

表示 productive zone 寬。

---

# 34. Window height

$$
H_W
=
\Phi_E(\epsilon^\star)
-
\Phi_E(0).
$$

---

# 35. Window sharpness

$$
S_W
=
-\frac{
d^2\Phi_E
}{
d\epsilon^2
}
\Bigg|_{\epsilon^\star}.
$$

高 sharpness 表示偏離最佳點後快速失效。

---

# 36. Window directionality

高維下，

不同方向：

$$
\hat\epsilon_j
$$

有：

$$
\Phi_E(r\hat\epsilon_j).
$$

因此要測：

$$
\boxed{
\text{direction-specific windows}.
}
$$

---

# 37. Assumption window

只改：

$$
\epsilon_A.
$$

例如：

- remove；
- weaken；
- strengthen；

一個 assumption。

---

# 38. Representation window

只改：

$$
\epsilon_L.
$$

例如同一 theorem 使用：

- coordinate A；
- coordinate B；
- symbolic A；
- graph representation。

---

# 39. Scope window

改：

$$
\epsilon_D.
$$

例如：

$$
D_{\mathrm{global}}
\rightarrow
D_{\mathrm{local}}.
$$

有時縮小 scope 反而大幅提高可證性與 transfer。

---

# 40. Method window

改：

$$
\epsilon_M.
$$

例如從單一 method family 到 hybrid method。

---

# 41. Regime window

改：

$$
\epsilon_R.
$$

例如：

- verifier；
- budget；
- model；
- memory。

這不是 mathematical mis-specification，

但可幫助分離：

$$
\text{problem effect}
$$

與：

$$
\text{search-system effect}.
$$

---

# 42. 為什麼 regime 也要納入

如果只在一個弱 model 上看到：

$$
\Phi_E(0)
$$

低，

但稍微改題就高，

可能只是：

$$
\boxed{
\text{model capability mismatch}.
}
$$

不是 parent 真的更 productive。

---

# 43. Intelligence-conditioned window

寫：

$$
\mathcal W_P^{(I)}.
$$

不同智能能力：

$$
I_1<I_2
$$

可能有：

$$
\mathcal W_P^{(I_1)}
\neq
\mathcal W_P^{(I_2)}.
$$

---

# 44. 一個反直覺預測

更強的 AI 可能讓 productive window 變窄。

因為：

$$
P^\star
$$

本身已能產生大量 descendants，

不需要透過偏差打開路徑。

---

# 45. 另一個可能

更強 AI 也可能讓窗口變寬。

因為它有能力 salvage：

$$
\text{structured deviations}
$$

中更多 descendants。

所以這是 empirical question。

---

# 46. Budget-conditioned window

$$
\mathcal W_P^{(\mathcal B)}.
$$

小 budget：

$$
\epsilon>0
$$

可能幫助簡化問題。

大 budget：

$$
\epsilon=0
$$

可能重新佔優。

---

# 47. 這和 effective theory 很像

在低能或低資源 regime，

effective representation：

$$
T_{\mathrm{eff}}
$$

可能更有操作價值。

這不表示它比 fundamental theory 更真。

---

# 48. Search-cost adjusted fertility

若：

$$
C_{\mathrm{cost}}(\epsilon)
$$

很高，

即使 generativity 高，

也可能不值得 pursue。

所以：

$$
\Phi_E
$$

要做 cost adjustment。

---

# 49. King 2025 與 pursuit-worthiness

King 對「ugly models」的討論提醒：

> 在理論尚未被完整驗證前，科學家還要決定哪個 model 值得花資源追。

這與本文非常接近。

窗口不只是 truth 問題，

也是：

$$
\boxed{
\text{research allocation}.
}
$$

---

# 50. Pursuit value

定義：

$$
V_P(\epsilon)
=
\mathbb E[
\Phi_E(\epsilon)
]
-
C_{\mathrm{research}}(\epsilon).
$$

真正 agent scheduler 應最大化：

$$
V_P,
$$

而不是 raw novelty。

---

# 51. Minimal models 的位置

Minimal model 有時極度移除細節，

所以相對 full target：

$$
\epsilon_L,\epsilon_M
$$

並不小。

但它可以保留：

$$
\text{macro invariants}.
$$

這說明偏差向量必須 task-conditioned。

---

# 52. 如果 task 是 macro explanation

則：

$$
F_{\mathrm{micro}}
$$

低不代表：

$$
F_{\mathrm{macro}}
$$

低。

所以 window 必須以 target scale 定義。

---

# 53. Scale-conditioned window

$$
\mathcal W_P^{(\ell)}.
$$

不同尺度：

$$
\ell
$$

可能有不同 optimum。

---

# 54. Ideal gas 的窗口直覺

在：

$$
\text{low density / moderate pressure}
$$

ideal gas approximation 高效。

靠近 phase transition，

它快速失效。

這不是 generic inverted-U，

而是：

$$
\boxed{
\text{domain-bounded usefulness window}.
}
$$

---

# 55. LISDD 的關鍵啟發

LISDD 不讓 correction：

$$
\Delta f
$$

污染 clean regime。

而是先找：

$$
D_{\mathrm{clean}},
$$

再定位：

$$
D_{\mathrm{error}}.
$$

這恰好是：

$$
\boxed{
\text{structured deviation localization}.
}
$$

---

# 56. Localization 是窗口成立的必要條件之一

如果不知道：

$$
\epsilon
$$

在哪裡，

就無法：

- repair；
- compare；
- transfer；
- determine survival。

---

# 57. Physics-guided operator correction

2026 年 operator correction work 將：

$$
\mathcal G_{\mathrm{true}}
=
\mathcal G_{\mathrm{prior}}
+
\Delta\mathcal G
$$

作為基本結構。

重要的是：

$$
\mathcal G_{\mathrm{prior}}
$$

不被 black-box correction 完全覆蓋。

---

# 58. Prior preservation

這相當於要求：

$$
\text{known-good descendants}
$$

保留。

所以 structured correction 本質上是：

$$
\boxed{
\text{salvage-aware model revision}.
}
$$

---

# 59. Experimental Design for Missing Physics

2026 年相關工作將候選 missing structures：

$$
M_1,\ldots,M_k
$$

作為待區分對象。

下一個實驗由：

$$
\text{which experiment most separates candidates}
$$

決定。

---

# 60. 這是 window science 的重要部分

不是只被動看偏差。

而是主動問：

$$
\boxed{
\text{what intervention best reveals whether this deviation is productive or merely wrong?}
}
$$

---

# 61. Bayesian uncertainty

Bayesian missing-physics work 進一步保留：

$$
P(M_i\mid D).
$$

這提醒窗口不應只有 point estimate：

$$
\epsilon^\star.
$$

而要有：

$$
P(
\epsilon\in\mathcal W_P
\mid D
).
$$

---

# 62. Probabilistic window

$$
\boxed{
\pi_W(\epsilon)
=
P(
\epsilon\in\mathcal W_P
\mid \mathcal D
).
}
$$

---

# 63. Window uncertainty

報：

- posterior；
- confidence interval；
- bootstrap；
- sensitivity。

不要畫一條曲線就宣布哲學定律。

---

# 64. 多峰結構

可能：

$$
\Phi_E
$$

在：

$$
\epsilon_1^\star,
\epsilon_2^\star
$$

有不同 peak。

例如：

- 一個 representation simplification peak；
- 一個 scope restriction peak。

---

# 65. 多峰意味什麼

不是「最佳錯誤只有一種」。

而是：

$$
\boxed{
\text{different structured distortions open different research mechanisms}.
}
$$

---

# 66. Phase transition

如果小幅改變：

$$
\epsilon
$$

讓：

$$
\Phi_E
$$

突然跳變，

可以定義：

$$
\epsilon_c.
$$

這叫：

$$
\text{research phase boundary}.
$$

---

# 67. 不要濫用物理相變

除非有：

- sharp transition；
- scaling；
- finite-size analysis；

否則「phase」只是操作性比喻。

---

# 68. Hysteresis

研究 history 可能使：

$$
P_\epsilon
$$

從：

$$
0\rightarrow\epsilon
$$

和：

$$
\epsilon\rightarrow0
$$

走出不同路徑。

---

# 69. 為什麼會有 hysteresis

因為：

- descendants 已生成；
- memory 已改變；
- tools 已建立；
- vocabulary 已形成；
- obstruction atlas 已更新。

所以即使 parent 修回：

$$
P^\star,
$$

研究系統已不再是原狀態。

---

# 70. Research-history hysteresis

定義：

$$
H_W
=
d(
\Phi_E^{\uparrow}(\epsilon),
\Phi_E^{\downarrow}(\epsilon)
).
$$

---

# 71. 這是一個非常重要的 AI 預測

一個 temporary mis-specification 可能永久改變：

$$
\mathcal H.
$$

即使後來修正，

生成的 tool、lemma、taxonomy 仍留在 memory。

---

# 72. 這就是 descendant legacy

$$
\boxed{
\text{parent correction}
\neq
\text{history erasure}.
}
$$

---

# 73. Window 可以依賴研究順序

如果先走：

$$
P_0\rightarrow P_{\epsilon_1}\rightarrow P^\star,
$$

與直接：

$$
P_0\rightarrow P^\star,
$$

最後 generative assets 不一定一樣。

---

# 74. Counterfactual research histories

因此可比較：

$$
\mathcal H_A
$$

與：

$$
\mathcal H_B.
$$

這是未來 AI 多分支研究很適合做的實驗。

---

# 75. Forked-history window experiment

從同一 checkpoint：

$$
H_0
$$

建立：

- exact branch；
- structured-deviation branch；
- random-deviation branch。

保持：

$$
\text{budget}
$$

相同。

---

# 76. 最後揭示 ground truth

所有 branch 都轉回：

$$
P^\star.
$$

再測：

$$
\text{what knowledge survived}.
$$

這是本文最乾淨的實驗之一。

---

# 77. Window 和 creativity 的關係

本文避免把：

$$
\Phi_E
$$

叫 creativity。

因為 creativity 包含：

- novelty；
- surprise；
- aesthetics；
- usefulness。

本文只測：

$$
\boxed{
\text{epistemic fertility}.
}
$$

---

# 78. 新奇不是窗口證據

如果：

$$
\nu(\epsilon)
$$

隨 $\epsilon$ 單調增加，

完全可能只是越錯越新奇。

真正要看：

$$
S_D,
R_D,T_D.
$$

---

# 79. Error-amplification peak

有時：

$$
G_{\mathrm{raw}}
$$

在大偏差時最高。

這反而可能形成：

$$
\boxed{
\text{hallucination peak}.
}
$$

---

# 80. 雙曲線診斷

同時畫：

$$
G_{\mathrm{raw}}(\epsilon)
$$

與：

$$
\Phi_E(\epsilon).
$$

如果：

$$
G_{\mathrm{raw}}\uparrow
$$

但：

$$
\Phi_E\downarrow,
$$

說明系統進入錯誤擴增區。

---

# 81. Survivor-adjusted generativity

$$
G_S(\epsilon)
=
G_A(\epsilon)
S_D(\epsilon).
$$

這是非常實用的第一版指標。

---

# 82. Transfer-adjusted generativity

$$
G_{ST}(\epsilon)
=
G_A
S_D
T_D.
$$

---

# 83. Cost-adjusted

$$
G_{STC}
=
\frac{
G_A S_D T_D
}{
1+C_{\mathrm{cost}}
}.
$$

---

# 84. Zombie penalty

$$
G_{STCZ}
=
\frac{
G_A S_D T_D
}{
(1+C_{\mathrm{cost}})
(1+\lambda Z_K)
}.
$$

---

# 85. 為什麼 zombie penalty 重要

一個偏差可能產生很多 surviving assets，

但同時留下大量 invalid active knowledge。

管理成本巨大。

所以：

$$
\Phi_E
$$

應扣分。

---

# 86. Window 的治理成本

AI 長程研究中，

偏差越大，

post-revision audit cost：

$$
C_{\mathrm{audit}}
$$

可能越高。

---

# 87. Audit-cost adjusted window

所以：

$$
\Phi_E'
=
\Phi_E
-
\lambda C_{\mathrm{audit}}.
$$

一個「很 fertile 但修一次要花十倍成本」的窗口未必值得追。

---

# 88. Decision-theoretic pursuit

如果研究目標是最大化期望知識收益：

$$
a^\star
=
\arg\max_a
\mathbb E[
\Phi_E(a)
-
C(a)
].
$$

---

# 89. Window 不等於應故意進入

即使存在：

$$
\epsilon^\star>0,
$$

也不一定值得人工製造。

因為：

- ethical cost；
- time；
- contamination；
- publication risk；
- downstream misuse。

所以：

$$
\boxed{
\text{descriptive window}
\neq
\text{normative recommendation}.
}
$$

---

# 90. 何時可以故意使用 controlled deviation

只有在：

- synthetic benchmark；
- sandbox；
- simulation；
- formal toy model；
- reversible branch；

等可隔離環境。

---

# 91. Production science 中應優先避免 silent error

真實科研系統應標：

$$
\text{deliberate perturbation}.
$$

不能偷偷改 parent。

---

# 92. Window experiment 必須 provenance-complete

每個 branch 保存：

- exact parent；
- exact delta；
- model；
- prompts；
- tools；
- budget；
- descendants；
- verification。

---

# 93. Ground-truth benchmark family

最適合先做的是：

1. 已知 ODE / PDE toy systems；
2. 可機器驗證 theorem；
3. synthetic formalization defects；
4. known combinatorial problems；
5. symbolic-regression systems。

---

# 94. 為什麼不能先用真正未知難題驗證

如果用 NS、P/NP：

$$
P^\star
$$

本身未知。

就無法知道：

$$
\epsilon=0
$$

在哪裡。

因此不能乾淨估窗口。

---

# 95. 所以 NS-203 只能做 observational case

不能作 ground-truth proof。

可以測：

- local closure proxy；
- generativity；
- descendant transfer；
- basin escape。

但不能標：

$$
\epsilon_{\mathrm{truth}}.
$$

---

# 96. NS-203 可做 representation perturbation

在不改 Clay statement 的前提下，

可以改：

$$
\epsilon_L,
\epsilon_M,
\epsilon_R.
$$

例如：

- continuous-only route；
- geometric route；
- recurrence route；
- proof-assistant route。

---

# 97. 這些不是「把 NS 問錯」

只是：

$$
\boxed{
\text{different search representations}.
}
$$

所以 epistemic risk 比直接改 theorem statement 低。

---

# 98. NS observational window

可定義：

$$
\mathcal W_{\mathrm{obs}}
$$

只表示：

> 哪些 representation/method perturbations 在相同 budget 下產生更多 audited reusable assets。

不能叫 truth window。

---

# 99. P/NP 同理

可以比較：

- circuit；
- proof complexity；
- algebraic；
- descriptive；
- geometric；

等 representation。

但不應從哪條 route 更 fertile 推出：

$$
P=NP
$$

或：

$$
P\neq NP.
$$

---

# 100. Window 和 undecidability 的關係

沒有直接關係。

$$
\Phi_E(\epsilon)
$$

曲線不能推出：

$$
\operatorname{Independent}(Q).
$$

---

# 101. Window 和 category error 的關係

若某個重新 framing：

$$
Q'
$$

帶來高：

$$
\Phi_E,
$$

只能提高：

$$
\operatorname{Priority}(\text{compare }Q,Q').
$$

不能直接說：

$$
Q\text{ category error}.
$$

---

# 102. Framing comparison protocol

至少比較：

$$
\operatorname{Map}(Q,Q'),
$$

$$
\operatorname{Loss}(Q\rightarrow Q'),
$$

$$
G_A,
S_D,
T_D,
C_{\mathrm{proof}}.
$$

---

# 103. 如果 $Q'$ 只是更弱

那麼容易證明完全不奇怪。

必須明示：

$$
Q\Rightarrow Q'
$$

但：

$$
Q'\not\Rightarrow Q.
$$

---

# 104. Window 不能靠弱化結論作弊

所以加入：

$$
F_Q
=
\text{question fidelity}.
$$

若：

$$
F_Q\downarrow
$$

太多，

則 fertility 要受 penalty。

---

# 105. Question-fidelity penalty

$$
\Phi_E^{\mathrm{adj}}
=
\Phi_E
\cdot
F_Q^\xi.
$$

---

# 106. 一個重要特殊情況

如果：

$$
Q'
$$

不是要替代 $Q$，

而是從 $Q$ 產生的子問題，

則不需要要求：

$$
F_Q\approx1.
$$

但必須改標：

$$
\text{descendant problem},
$$

不是 reformulation。

---

# 107. 問題分裂也可能形成 productive region

一個太大的 parent：

$$
Q
$$

拆成：

$$
Q_1,\ldots,Q_n.
$$

如果每個 $Q_i$ 產生高 quality descendants，

這是：

$$
\boxed{
\text{decomposition fertility}.
}
$$

---

# 108. Decomposition 與 mis-specification 不同

如果 parent 本來就合理，

只是 decomposition 更有效，

不能叫 parent mis-specified。

所以 classification 要嚴格。

---

# 109. Productive simplification

有些 case 更適合叫：

$$
\text{productive simplification}.
$$

不是：

$$
\text{mis-specification}.
$$

---

# 110. Productive distortion

若明知不真但保留某結構，

叫：

$$
\text{productive idealization/distortion}.
$$

---

# 111. Productive misspecification

只有：

> 原本被當作足夠描述，後來發現有系統缺陷，

才最適合這個詞。

---

# 112. Productive framing anomaly

若問題切法本身後來被替換，

可另標：

$$
\text{productive reframing}.
$$

---

# 113. 因此第 9 篇的 window 是上位框架

它可以包含：

- idealization window；
- simplification window；
- misspecification window；
- reframing window。

但 metadata 要分型。

---

# 114. Window Type

```yaml
window_type:
  - idealization
  - simplification
  - model_misspecification
  - scope_shift
  - representation_shift
  - method_shift
  - reframing
```

---

# 115. Window 比較必須 type-matched

不要拿：

$$
\text{representation shift}
$$

與：

$$
\text{wrong quantifier}
$$

混成同一 $\epsilon$ 曲線。

---

# 116. Multi-axis experiment

真正完整的設計：

$$
\Phi_E(
\epsilon_A,
\epsilon_L,
\epsilon_D,\ldots
).
$$

可以畫 response surface。

---

# 117. Interaction effects

偏差可能交互：

$$
\epsilon_A\epsilon_L.
$$

例如：

> 一個弱化 assumption 只有在新 representation 下才 fruitful。

---

# 118. 二階 response surface

可建：

$$
\Phi_E
=
\beta_0
+
\sum_i\beta_i\epsilon_i
+
\sum_{i<j}\beta_{ij}\epsilon_i\epsilon_j
+
\cdots.
$$

---

# 119. 不預設 polynomial truth

這只是統計 surrogate。

必要時可用：

- Gaussian process；
- spline；
- monotonic model；
- Bayesian response surface。

---

# 120. Sample efficiency

高維 window search 很貴。

所以需要 adaptive experiment design。

這與 2026 missing-physics experimental design 又接起來。

---

# 121. Active window search

每輪選：

$$
\epsilon_{t+1}
$$

最大化：

$$
\text{expected information gain}.
$$

---

# 122. 不要最大化 fertility 本身

如果只挑目前最高：

$$
\Phi_E,
$$

會過度 exploit。

應平衡：

$$
\text{uncertainty reduction}.
$$

---

# 123. Bayesian window mapping

建 posterior：

$$
P(
\Phi_E(\epsilon)
\mid
D_t
).
$$

下一點選：

$$
\epsilon^\star
=
\arg\max
\operatorname{EIG}(\epsilon).
$$

---

# 124. Window discovery 成為科學問題

這時候我們不是在「鼓勵錯誤」。

而是在：

$$
\boxed{
\text{測量研究系統對偏差的響應曲面}.
}
$$

---

# 125. AI 可以做這件事的原因

AI 可以：

- 大量 parallel branches；
- exact provenance；
- automatic re-audit；
- formal verification；
- controlled perturbation。

這是傳統人類科學史很難做的。

---

# 126. 科學史是 observational

Carnot 等案例是：

$$
\text{one realized path}.
$$

我們看不到完整 counterfactual：

> 如果 Carnot 沒採 caloric theory，會怎樣？

---

# 127. AI sandbox 可以做 counterfactual histories

同一 ground truth，

平行啟動：

$$
H_1,H_2,\ldots,H_m.
$$

這是非常新的實驗可能性。

---

# 128. Historical counterfactual benchmark

可以用已知科學史問題：

- thermodynamics toy reconstruction；
- oxygen chemistry toy world；
- celestial models；
- fluid models。

建立不同 parent assumptions。

---

# 129. 但不能假裝重演真歷史

只叫：

$$
\text{historically inspired synthetic benchmark}.
$$

---

# 130. Window 和 multi-agent science

不同 agent 分配不同：

$$
\epsilon_i.
$$

可以形成：

$$
\text{deviation portfolio}.
$$

---

# 131. Portfolio allocation

總 budget：

$$
B.
$$

分配：

$$
b_0,b_1,\ldots,b_m.
$$

其中：

$$
b_0
$$

給 baseline，

其他給 perturbations。

---

# 132. Portfolio objective

$$
\max
\mathbb E[
\text{total surviving knowledge}
].
$$

---

# 133. Exploration hedge

即使 baseline 看起來最好，

仍可給小比例 budget：

$$
b_{\mathrm{explore}}>0.
$$

防止局部 lock-in。

---

# 134. 這和 LSI-PSD-05 的 basin allocation 接軌

第 5 篇分配：

$$
\text{agents across basins}.
$$

第 9 篇分配：

$$
\text{agents across controlled deviations}.
$$

兩者可以合併。

---

# 135. Basin × deviation matrix

$$
A_{ij}
=
\text{budget on basin }B_i
\text{ under deviation }\epsilon_j.
$$

---

# 136. 這會很快爆炸

所以需要 meta-controller：

$$
\Pi_{\mathrm{meta}}.
$$

---

# 137. Meta-controller input

$$
(
C_{\mathrm{sat}},
\Phi_E,
R_W,
C_{\mathrm{ind}},
\Gamma_{\mathrm{esc}},
\operatorname{SDI}
).
$$

---

# 138. Meta-controller output

$$
\{
\text{continue exact},
\text{perturb},
\text{repair},
\text{revert},
\text{branch},
\text{kill branch}
\}.
$$

---

# 139. Revertability 是窗口實驗的安全條件

所有 deliberate deviation branch 必須：

$$
\boxed{
\text{reversible}.
}
$$

---

# 140. Canonical parent 不被覆寫

保留：

$$
P^\star_{\mathrm{canonical}}.
$$

perturbation 只建立：

$$
P_{\epsilon}^{\mathrm{branch}}.
$$

---

# 141. 這也符合 source-integrity 原則

正式 source 不能因實驗 branch 被 silent rewrite。

---

# 142. Window experiment 的最小資料格式

```yaml
experiment_id:
ground_truth_parent:
task:
regime:
budget:

branch:
  epsilon_vector:
  deviation_type:
  structured_deviation_index:
  random_control_matched_norm:
  provenance:

outputs:
  raw_descendants:
  audited_descendants:
  survivor_descendants:
  transfer_descendants:
  zombie_knowledge:
  cost:

metrics:
  fertility_vector:
  scalar_fertility:
  uncertainty:
```

---

# 143. 實驗一：1D assumption sweep

選一個已知 theorem。

建立：

$$
A_\lambda
$$

逐步：

- weaken；
- strengthen；
- remove。

測：

$$
\Phi_E(\lambda).
$$

---

# 144. 實驗二：representation sweep

同一 theorem 語義等價，

改：

$$
L_1,\ldots,L_m.
$$

這裡：

$$
F_Q=1.
$$

最乾淨地測：

$$
\text{representation productivity}.
$$

---

# 145. 實驗三：scope sweep

對物理模型：

$$
D_1\subset D_2\subset\cdots.
$$

測 model residual、missing mechanism 與 descendants。

---

# 146. 實驗四：missing-physics magnitude sweep

ground truth：

$$
f^\star=f_0+\lambda g.
$$

研究 model 只給：

$$
f_0.
$$

改變：

$$
\lambda.
$$

---

# 147. 預測

若：

$$
\lambda\approx0,
$$

residual 太小，

難以產生 mechanism discovery。

中等：

$$
\lambda
$$

容易辨識。

太大：

$$
f_0
$$

失去 useful prior。

這是很自然的 inverted-U 候選。

---

# 148. 實驗五：random missing physics control

用相同：

$$
\|\lambda g\|
$$

但：

$$
g_{\mathrm{rand}}.
$$

比較：

$$
\Phi_E.
$$

---

# 149. 實驗六：formalization defect sweep

逐步注入：

- missing hypothesis；
- quantifier flip；
- translation simplification；
- vacuity。

讓 prover 研究，

最後 repair。

---

# 150. 測量 survivor assets

- proof tactics；
- helper lemma；
- counterexample；
- formalization tool；
- theorem descendants。

---

# 151. 實驗七：proof-space branch portfolio

對同一已知 hard theorem：

- exact branch；
- representation branch；
- method branch；
- weakened-assumption branch；
- random branch。

固定：

$$
B.
$$

---

# 152. 最終比較

$$
\Phi_E^{(0)},
\Phi_E^{(1)},
\ldots.
$$

---

# 153. 何時可以說有窗口

至少：

1. 多 seed；
2. 多 model；
3. 相同 budget；
4. audited descendants；
5. ground truth；
6. random control；
7. post-revision survival；
8. uncertainty interval；
9. preregistered metric。

---

# 154. Window Evidence Level 0

只有直覺或單案例。

---

# 155. Level 1

一個 synthetic benchmark 有 interior peak。

---

# 156. Level 2

多 seeds、同一 domain 重現。

---

# 157. Level 3

多模型重現。

---

# 158. Level 4

跨不同 benchmark family 重現。

---

# 159. Level 5

存在理論模型解釋：

$$
\text{why the window emerges}.
$$

即使 Level 5 也不代表 universal law。

---

# 160. Window collapse

當 model intelligence 提高，

可能：

$$
W\rightarrow0.
$$

這叫：

$$
\text{window collapse}.
$$

---

# 161. Window expansion

若新工具提高 salvageability：

$$
W\uparrow.
$$

---

# 162. Window migration

最佳點：

$$
\epsilon^\star
$$

隨：

- budget；
- model；
- domain；

移動。

---

# 163. Window topology

高維下可研究：

- connected components；
- holes；
- ridges；
- saddle points。

但這屬未來 empirical geometry。

---

# 164. 不應過早拓樸神秘化

先有：

$$
\text{reliable data}.
$$

再談 topology。

---

# 165. 與「越是真理越可能是廢話」的真正關係

零偏差端：

$$
\epsilon=0
$$

如果 parent 已高度 closure，

可能：

$$
G_{\mathrm{theory}}
$$

低。

---

# 166. 但 application generativity 可能高

所以：

$$
\Phi_E
$$

未必低。

這再一次說明 window 依 task。

---

# 167. 如果 task 是「發明新理論」

中間偏差可能高。

如果 task 是「可靠控制」

零偏差可能高。

所以不能跨 task 比。

---

# 168. 真理不是被窗口取代

窗口只描述：

$$
\text{research productivity landscape}.
$$

不是：

$$
\text{truth landscape}.
$$

---

# 169. Window 和真理的關係仍由 verification 決定

descendants 最終必須：

$$
\operatorname{Verify}(d_i).
$$

---

# 170. 這是防止哲學滑坡的最後一道門

不能從：

$$
\Phi_E(\epsilon^\star)>\Phi_E(0)
$$

推出：

$$
P_{\epsilon^\star}
$$

比：

$$
P^\star
$$

更真。

---

# 171. 非主張總表

本文不主張：

1. 所有 domain 都存在 productive window；
2. inverted-U 是普遍形狀；
3. 中等錯誤必然最好；
4. 科學家應故意相信錯誤理論；
5. 任意偏差可提升創造力；
6. generativity 可以取代 truth；
7. $\epsilon^\star>0$ 表示偏差模型比真模型更正確；
8. minimal model 一定位於 productive window；
9. effective theory 一定比 fundamental theory 更有用；
10. LISDD 已證明 productive-mis-specification window；
11. physics-guided correction 已證明真理—生成性反轉；
12. NS-203 可以提供真實 $\epsilon$ 軸；
13. NS 或 P/NP 已被證明 framing 有錯；
14. AI 反覆失敗可以推出 undecidability；
15. random novelty 可當 epistemic fertility；
16. high raw output 可當 window evidence；
17. parent revision 後未 audit descendants 可算 survivors；
18. 一個歷史案例足以建立因果曲線；
19. window 存在就表示應主動製造錯誤；
20. 本文已完成 productive-window 的 empirical proof。

---

# 172. 形式命題一：Norm Insufficiency

$$
\boxed{
\|\epsilon_1\|
=
\|\epsilon_2\|
\not\Rightarrow
\Phi_E(\epsilon_1)
=
\Phi_E(\epsilon_2).
}
$$

---

# 173. 形式命題二：Raw Novelty Non-Window

$$
\boxed{
\nu(\epsilon)\uparrow
\not\Rightarrow
\epsilon\in\mathcal W_P.
}
$$

---

# 174. 形式命題三：Survival Requirement

若：

$$
S_D(\epsilon)\approx0,
$$

則高：

$$
G_{\mathrm{raw}}
$$

不能建立 productive window。

---

# 175. 形式命題四：Random-Control Requirement

如果：

$$
\Phi_E(\epsilon_{\mathrm{struct}})
\le
\mathbb E\Phi_E(\epsilon_{\mathrm{rand}}),
$$

則 structured-deviation superiority 不成立。

---

# 176. 形式命題五：Task Dependence

$$
\boxed{
\mathcal W_P^{\mathcal T_1}
\neq
\mathcal W_P^{\mathcal T_2}
}
$$

在一般情況下是允許的。

---

# 177. 形式命題六：Regime Dependence

$$
\boxed{
\mathcal W_P^{R_1}
\neq
\mathcal W_P^{R_2}.
}
$$

---

# 178. 形式命題七：Descriptive–Normative Separation

$$
\boxed{
\epsilon\in\mathcal W_P
\not\Rightarrow
\text{one ought to introduce }\epsilon.
}
$$

---

# 179. 形式命題八：Window Non-Truth

$$
\boxed{
\epsilon^\star
=
\arg\max\Phi_E
\not\Rightarrow
\epsilon^\star
=
\arg\max T.
}
$$

---

# 180. 形式命題九：Structured Deviation Hypothesis

在部分 domain 中可能存在：

$$
\operatorname{SDI}(\epsilon_1)
>
\operatorname{SDI}(\epsilon_2)
$$

且：

$$
\|\epsilon_1\|
\approx
\|\epsilon_2\|,
$$

同時：

$$
\Phi_E(\epsilon_1)
>
\Phi_E(\epsilon_2).
$$

這是可實驗檢驗的核心假說。

---

# 181. 形式命題十：History Dependence

$$
\boxed{
\Phi_E(\epsilon\mid H_1)
\neq
\Phi_E(\epsilon\mid H_2)
}
$$

是可能的。

---

# 182. 與 LSI-PSD-08 的整合

第 8 篇回答：

> parent 被修正後，哪些 descendants 存活？

第 9 篇回答：

> 不同種類與強度的偏差，會不會系統性改變 survivor production rate？

所以：

$$
S_D
$$

從 outcome 指標變成 response surface 的一部分。

---

# 183. 與 LSI-PSD-07 的整合

第 7 篇：

$$
T\neq G.
$$

第 9 篇進一步：

$$
G
=
G(\epsilon,\mathcal T,R,H).
$$

即 generativity 本身是條件性的。

---

# 184. 與 LSI-PSD-05 的整合

局部 basin saturation 可能觸發：

$$
\text{controlled deviation probe}.
$$

不是為了改 truth，

而是探測：

$$
\text{whether neighboring research regions are more fertile}.
$$

---

# 185. 與 LSI-PSD-06 的整合

高 confluence obstruction：

$$
O^\star
$$

可以成為 perturbation design 的目標。

例如：

- 改 representation；
- 改 assumption；
- 改 scope。

看哪種 perturbation 能真正繞開 $O^\star$ 且留下 survivors。

---

# 186. 與 Logic-Space Integration 的整合

對每個偏差：

$$
\epsilon
$$

都有一個 proof-space：

$$
\Omega(P_\epsilon).
$$

窗口研究比較：

$$
\Omega(P_{\epsilon_1}),
\Omega(P_{\epsilon_2}),
\ldots.
$$

---

# 187. Cross-space survivor map

對：

$$
P_{\epsilon_i}
\rightarrow P^\star
$$

計算：

$$
\Omega_{\mathrm{surv}}^{(i)}
=
\operatorname{Audit}
(
\Omega(P_{\epsilon_i})
\cap
\Omega(P^\star)
).
$$

---

# 188. Window 的空間版本

$$
\epsilon^\star
=
\arg\max
\operatorname{Value}
(
\Omega_{\mathrm{surv}}^{(i)}
).
$$

這比 raw paper count 精確得多。

---

# 189. Knowledge density

定義：

$$
D_K(\epsilon)
=
\frac{
|\Omega_{\mathrm{surv}}(\epsilon)|
}{
C_{\mathrm{cost}}(\epsilon)
}.
$$

---

# 190. Novel survivor density

若 quotient 後：

$$
N_K(\epsilon)
=
\frac{
|\Omega_{\mathrm{surv}}(\epsilon)/\sim|
}{
C_{\mathrm{cost}}
}.
$$

---

# 191. Transfer survivor density

$$
T_K(\epsilon)
=
\frac{
|\Omega_{\mathrm{transfer}}(\epsilon)|
}{
C_{\mathrm{cost}}
}.
$$

---

# 192. Window scorecard

真正觀測站應同時報：

```text
deviation vector
deviation type
SDI
raw generation
audited generation
survival ratio
transfer ratio
zombie rate
cost
fertility confidence interval
window membership probability
```

---

# 193. 研究系列至此的相變

前六篇主要研究：

$$
\text{how proof search behaves}.
$$

第七、八、九篇開始研究：

$$
\text{how truth, error, correction, and generation interact}.
$$

這使 LSI-PSD 從 theorem-search observatory 進入：

$$
\boxed{
\text{empirical epistemology of AI research}.
}
$$

---

# 194. 為什麼這不是純哲學

因為所有主要量都可以在 synthetic / formal benchmark 中直接記錄：

$$
\epsilon,
G_A,
S_D,
T_D,
R_D,
C_D,
Z_K,
C_{\mathrm{cost}}.
$$

---

# 195. 為什麼這也不是單純機器學習 benchmark

因為核心問題不是：

$$
\text{accuracy}.
$$

而是：

$$
\boxed{
\text{what kind of research history produces durable knowledge under later correction?}
}
$$

---

# 196. 這個問題以前很難實驗

人類科學史只有一條 realized history。

AI 可以平行跑：

$$
10^2
$$

條 counterfactual research histories。

---

# 197. 但必須避免把 AI sandbox 當真歷史

我們測的是：

$$
\text{research-system dynamics}.
$$

不是重演 Galileo、Carnot 或 Lavoisier 真正心理史。

---

# 198. 未來最重要的 benchmark

本文建議建立：

$$
\boxed{
\text{Productive Mis-specification Benchmark Suite}
}
$$

簡稱：

$$
\text{PMW-Bench}.
$$

---

# 199. PMW-Bench 類別

1. theorem perturbation；
2. model misspecification；
3. scope mismatch；
4. representation shift；
5. missing physics；
6. formalization defect；
7. controlled random error。

---

# 200. 每個 benchmark 都要有 ground truth

否則：

$$
S_D
$$

無法可靠算。

---

# 201. 每個 benchmark 都要可修正

需要：

$$
P_\epsilon
\rightarrow P^\star.
$$

否則無法做 descendant survival audit。

---

# 202. 每個 benchmark 都要有 matched random control

這是本篇最重要的新要求之一。

---

# 203. 每個 benchmark 都要有 cost log

否則高 fertility 可能只是花了更多資源。

---

# 204. 每個 benchmark 都要有 provenance

否則 survivors 無法追 ancestor。

---

# 205. 每個 benchmark 都要有 canonical source

否則 parent perturbation 不可重放。

---

# 206. 結論

「錯誤有時很有用」是一句太寬鬆、也太容易被濫用的話。

真正值得研究的不是：

$$
\text{error}
$$

本身，

而是：

$$
\boxed{
\text{structured, bounded, localizable, comparable, repairable deviation}.
}
$$

本文把這些條件壓成：

$$
\operatorname{SDI}.
$$

再把研究產出從 raw novelty 改成：

$$
\Phi_E,
$$

也就是：

$$
\text{audited generation}
+
\text{descendant survival}
+
\text{transfer}
+
\text{robustness}
-
\text{zombie knowledge}
-
\text{cost}.
$$

只有當有限偏差：

$$
\epsilon
$$

在 matched budget、matched norm、random-control 與 post-revision audit 下，穩定產生：

$$
\Phi_E(\epsilon)
>
\Phi_E(0),
$$

才有資格談：

$$
\boxed{
\text{productive mis-specification window}.
}
$$

而且即使窗口存在，它依然只是：

$$
\boxed{
\text{research productivity property}.
}
$$

它不是：

$$
\boxed{
\text{truth property}.
}
$$

因此本文既拒絕：

> 越精確一定越有知識產出。

也拒絕：

> 越錯反而越好。

真正可能成立的是一個更細緻的命題：

$$
\boxed{
\textbf{For some tasks and research regimes, epistemic fertility may peak inside a structured deviation region rather than at either perfect fidelity or uncontrolled error.}
}
$$

但這個命題只有在：

- controlled perturbation；
- ground truth；
- random control；
- independent audit；
- descendant survival；
- uncertainty estimation；

全部存在時，才有科學地位。

因此「生產性錯置窗口」最終不是錯誤哲學。

它是一個新的實驗問題：

$$
\boxed{
\textbf{How does the rate of durable knowledge production respond to controlled changes in the way a problem is represented, constrained, and searched?}
}
$$

而這個問題，正是 AI 長程研究第一次有機會大規模、可重放、可分支地真正測量的問題之一。

---

# 參考文獻

1. Batterman, R. W., & Rice, C. C. (2014). **Minimal Model Explanations.** *Philosophy of Science*, 81(3), 349–376. https://doi.org/10.1086/676677

2. Rice, C. (2021). **Leveraging Distortions: Explanation, Idealization, and Universality in Science.** MIT Press.

3. King, M. (2025). **Experiment and the Pursuit of Ugly Models.** *European Journal for Philosophy of Science*, 15, Article 55. https://doi.org/10.1007/s13194-025-00692-y

4. Ma, L. et al. (2026). **Physics-guided correction for operator learning under model misspecification.** arXiv:2606.03469. https://arxiv.org/abs/2606.03469

5. Wang, Y. (2026). **Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy.** arXiv:2606.23215. https://arxiv.org/abs/2606.23215

6. Strouwen, A., & Micluţa-Câmpeanu, S. (2026). **Experimental Design for Missing Physics.** arXiv:2604.01231. https://arxiv.org/abs/2604.01231

7. Strouwen, A. (2026). **Bayesian Inference for Missing Physics.** arXiv:2603.14918. https://arxiv.org/abs/2603.14918

8. Ebers, M. R., Steele, K. M., & Kutz, J. N. (2022). **Discrepancy Modeling Framework: Learning missing physics, modeling systematic residuals, and disambiguating between deterministic and random effects.** arXiv:2203.05164; later SIAM publication.

9. Zou, Z. et al. (2024). **Correcting model misspecification in physics-informed neural networks for discovery of governing equations.** *Journal of Computational Physics*.

10. Mohammadian, M. (2026). **Theoretical Virtues, Truth, and the Epistemic Aim of Scientific Theorizing.** *Philosophy of Science*.

11. Weingarten, K. (2026). **Productive Idealizations for Scientific Understanding: A Case Study in Effective Theories.** PhilSci-Archive preprint.

12. Spagnesi, L. (2025). **Truth, Understanding, and Normativity in Scientific Models.** *Synthese*, 206.

13. Norton, J. D. (2022). **How Analogy Helped Create the New Science of Thermodynamics.** *Synthese*, 200, 269.

14. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $P^\star$ | 參照 parent / ground-truth parent |
| $P_\epsilon$ | 帶控制偏差的 parent |
| $\boldsymbol\epsilon$ | 多維 deviation vector |
| $\hat\epsilon$ | deviation direction |
| $\operatorname{SDI}$ | Structured Deviation Index |
| $\Phi_E$ | epistemic fertility |
| $G_A$ | audited generativity |
| $S_D$ | descendant survival |
| $T_D$ | descendant transferability |
| $R_D$ | descendant robustness |
| $C_D$ | descendant audit coverage |
| $Z_K$ | zombie-knowledge rate |
| $C_{\mathrm{cost}}$ | research cost |
| $\mathcal W_P$ | productive-mis-specification window / region |
| $W$ | window width |
| $H_W$ | window height |
| $S_W$ | window sharpness |
| $\pi_W$ | probabilistic window membership |
| $\Omega_{\mathrm{surv}}$ | survivor proof/knowledge space |

---

## 附錄 B：最小 PMW-Bench protocol

```text
1. Choose a system with known ground truth.
2. Freeze canonical parent source.
3. Define one deviation axis.
4. Create:
   - exact baseline
   - structured deviations at several magnitudes
   - norm-matched random deviations
5. Equalize research budget.
6. Run independent research branches.
7. Collect all descendants with provenance.
8. Reveal / restore ground truth.
9. Re-audit every descendant.
10. Compute:
    G_A
    S_D
    T_D
    R_D
    C_D
    Z_K
    cost
11. Estimate uncertainty.
12. Test whether any interior structured region
    significantly exceeds both baselines.
13. Replicate across seeds and models.
```

---

## 附錄 C：Window Evidence Card

```yaml
domain:
task:
research_regime:
ground_truth_available:

deviation_axis:
deviation_type:
structured_deviation_index:

baseline:
  fertility:
  uncertainty:

random_control:
  norm_matched:
  fertility:
  uncertainty:

candidate_window:
  lower:
  upper:
  peak:
  width:
  height:
  robustness:

descendant_audit:
  coverage:
  survival:
  transfer:
  zombie_rate:

replication:
  seeds:
  models:
  benchmark_families:

status:
  - unsupported
  - preliminary
  - replicated
  - cross-domain
```

---

## 附錄 D：四種典型結果

### A. Fidelity-dominant

$$
\Phi_E(0)
>
\Phi_E(\epsilon)
\quad
\forall\epsilon>0.
$$

結論：

> 沒有 productive window。

### B. Structured interior window

$$
\exists\epsilon^\star>0:
\Phi_E(\epsilon^\star)
>
\Phi_E(0),
$$

且：

$$
\Phi_E(\epsilon^\star)
>
\Phi_E(\epsilon^\star_{\mathrm{rand}}).
$$

結論：

> 支持 productive-window hypothesis。

### C. Random-error domination

$$
\Phi_E(\epsilon_{\mathrm{rand}})
\ge
\Phi_E(\epsilon_{\mathrm{struct}}).
$$

結論：

> 「結構化偏差」假說未獲支持；檢查 metric。

### D. Raw novelty peak but survivor collapse

$$
G_{\mathrm{raw}}\uparrow,
$$

但：

$$
S_D\downarrow.
$$

結論：

> error amplification，而非 epistemic fertility。

---

## 附錄 E：一句話版本

$$
\boxed{
\text{真正值得研究的不是「錯一點會不會更有創意」，而是「哪一種可控偏差，能在修正後留下最多仍然成立的知識」。}
}
$$
