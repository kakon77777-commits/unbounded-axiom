# LSI-PSD-11 — 從 Carnot 到 AI：結構性錯誤的科學史與模型論

## From Carnot to AI: A Comparative History and Theory of Structurally Productive Error

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 11  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 科學史—模型論橋接論文 / Comparative Historical and Model-Theoretic Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文以科學史案例與現代模型研究作為「結構性錯誤可能留下可存活後代」的比較素材，而不是用歷史故事替任何當代未解數學命題背書。歷史案例只能支持「某些父框架後來被修正，而其中部分結構、數據、方法或數學仍被保留」；它們不能推出「錯理論一般更有價值」，也不能推出「Navier--Stokes、P/NP 或其他問題目前必然存在定義／範疇錯誤」。本文特別避免以 hindsight 把歷史重寫成單一路線的必然進步史，也不對無法觀察的反事實歷史作強因果斷言。

---

## 摘要

科學史中有一類反覆出現、但很容易被簡化成口號的現象：一個後來被修正、限制、重新解釋甚至否定的父理論，可能在其有效生命週期內產生大量後來仍然存活的科學資產。這些資產可能是：

$$
\text{observation},
$$

$$
\text{mathematical transformation},
$$

$$
\text{experimental technique},
$$

$$
\text{invariant},
$$

$$
\text{limit law},
$$

$$
\text{reversible structure},
$$

$$
\text{effective model},
$$

$$
\text{diagnostic residual}.
$$

因此：

$$
\boxed{
\text{parent theory revision}
\not\Rightarrow
\text{total descendant annihilation}.
}
$$

然而，這個歷史事實常被過度浪漫化成：

> 「錯誤會帶來真理。」

本文拒絕這種粗糙結論，並提出一個更精確的比較框架：**Structurally Productive Error**，中文暫稱「結構性生產錯誤」。它指的是一個 parent framework 的某些 ontological、mechanistic、scope、representation 或 specification 部分後來被修正，但其研究路徑因為保留了某些真正穩定、可遷移或可重建的結構，使部分 descendants 在 parent revision 後仍能通過 independent audit。

本文選取六組典型案例：

1. Carnot 與 caloric theory；
2. Priestley / phlogiston 與氧氣實驗；
3. Lorentz–ether tradition 與 Lorentz transformations；
4. Bohr atom model；
5. ideal gas / minimal model；
6. effective field theory / productive idealization。

這些案例並不是同一種類型的「錯」。Carnot 的 conserved caloric 是後來被修正的物理本體假設；phlogiston 是錯誤燃燒解釋下產生的真實氣體實驗；Lorentz 的 ether framework 包含後來被不同時空本體重新解釋、但數學形式仍保留的轉換結構；Bohr model 是高度成功但適用範圍有限且含有後來被量子力學替代的經典軌道圖像；ideal gas 是明知不字面真實但在受控 regime 中極具價值的 idealization；effective field theory 則更進一步，把「有限適用域、非基本、尺度依賴」直接制度化為現代理論實踐的一部分。

本文因此提出歷史比較矩陣：

$$
H(P)
=
(
E_{\mathrm{type}},
S_{\mathrm{retained}},
D_{\mathrm{survival}},
R_{\mathrm{repair}},
T_{\mathrm{transfer}},
C_{\mathrm{counterfactual}}
),
$$

其中：

- $E_{\mathrm{type}}$：parent error / limitation 類型；
- $S_{\mathrm{retained}}$：被保留的結構；
- $D_{\mathrm{survival}}$：後代存活情形；
- $R_{\mathrm{repair}}$：parent correction 方式；
- $T_{\mathrm{transfer}}$：是否跨新理論轉移；
- $C_{\mathrm{counterfactual}}$：反事實因果可主張程度。

本文進一步定義 **Structural Retention Ratio**：

$$
\operatorname{SRR}(P\rightarrow P')
=
\frac{
\sum_i w_i\mathbf 1[s_i\text{ survives under }P']
}{
\sum_i w_i
},
$$

但強調它在歷史案例中通常只能做半定量評估；真正可量化版本更適合未來在 synthetic AI research benchmark 中建立。

2025--2026 年的模型哲學與 AI 科學方法又讓這一問題重新變得工程化。Spagnesi 將 idealized model 視為可產生解釋性 deviation 的規範比較點；Frigg 等人以 stability / noetic core 討論理想化模型如何仍提供 understanding；Weingarten 以 effective theories 討論 non-fundamental theory 的 productive idealization；LISDD 與 discrepancy-modeling work 則把：

$$
\text{model–world discrepancy}
$$

轉化為：

$$
\text{missing mechanism discovery}.
$$

2026 年 formal specification 與 theorem-proving audit 進一步揭示另一種現代「父框架錯置」：一個 machine-checked proof 可以在 formal target $Q_F$ 上完全正確，但 $Q_F$ 仍可能偏離 natural-language intention $Q_I$。這使「formal success」與「semantic fidelity」成為兩個必須分開追蹤的層。

本文由此把科學史與 AI research infrastructure 連成同一個問題：

$$
\boxed{
\text{When a parent framework is revised, what exactly should survive?}
}
$$

這個問題不能靠故事回答，而需要：

$$
\text{provenance}
+
\text{dependency graph}
+
\text{revision map}
+
\text{descendant re-audit}.
$$

本文最後提出 **Historical-to-AI Translation Principle**：

> 科學史提供「父理論可失敗而後代部分存活」的存在性案例；AI 長程研究則第一次有機會把這種現象做成可版本化、可分支、可重跑、可量化的研究對象。

這也是本文的核心結論：

$$
\boxed{
\textbf{What survives a theory is often more informative than the binary fact that the theory survived or failed.}
}
$$

**關鍵詞：** 科學史、Carnot、caloric theory、phlogiston、Lorentz ether、Bohr model、ideal gas、effective field theory、productive error、descendant survival、idealization、scientific models、AI science、formalization fidelity

---

# 1. 問題的提出：歷史上的「錯理論」到底錯在哪裡？

「錯理論」這個詞太粗。

一個理論可以在：

- ontology；
- mechanism；
- domain；
- scale；
- representation；
- parameterization；
- formalization；

其中一層錯，

但其他層仍然相當準確。

---

# 2. Parent theory 不是單一命題

本文沿用：

$$
P
=
(
O,M,D,L,A,E
),
$$

其中：

- $O$：ontology；
- $M$：mechanism；
- $D$：domain；
- $L$：language / mathematical representation；
- $A$：assumptions；
- $E$：empirical relations。

---

# 3. 一個 parent 可以「部分錯」

例如：

$$
O\text{ wrong},
$$

但：

$$
E\text{ reliable}.
$$

或：

$$
M\text{ incomplete},
$$

但：

$$
L\text{ transferable}.
$$

---

# 4. 因此 theory transition 不是二元 wipeout

舊模型：

$$
P
$$

轉成：

$$
P'.
$$

真正問題是：

$$
\boxed{
\operatorname{Map}(P\rightarrow P').
}
$$

---

# 5. Transition map

定義：

$$
\mathcal T_{P\rightarrow P'}
:
\{
O,M,D,L,A,E
\}
\rightarrow
\{
\text{retain},
\text{reinterpret},
\text{repair},
\text{discard}
\}.
$$

---

# 6. 四種轉移狀態

## 6.1 Retain

結構幾乎原樣保留。

## 6.2 Reinterpret

公式或數據保留，但本體意義改變。

## 6.3 Repair

局部修改後保留。

## 6.4 Discard

被反例或新框架直接淘汰。

---

# 7. 科學史不應只問「誰對誰錯」

更值得問：

$$
\boxed{
\text{which components crossed the transition boundary?}
}
$$

---

# 8. 歷史比較矩陣

對每個案例：

$$
H(P)
=
(
E_t,
S_r,
D_s,
R_c,
T_r,
C_f
).
$$

---

# 9. $E_t$：error type

例如：

- ontology；
- mechanism；
- scope；
- idealization；
- representation；
- interpretation。

---

# 10. $S_r$：retained structure

被保留：

- equations；
- invariant；
- experiment；
- method；
- limiting relation。

---

# 11. $D_s$：descendant survival

後代有多少在新框架仍成立。

---

# 12. $R_c$：repair character

修正是：

- local；
- global；
- reinterpretive；
- replacement；
- scale restriction。

---

# 13. $T_r$：transferability

舊理論產物是否跨到新理論。

---

# 14. $C_f$：counterfactual confidence

我們能多大程度說：

> 如果沒有舊錯理論，就不會有後來成果？

通常：

$$
C_f
$$

很低。

---

# 15. 為什麼反事實特別危險

我們只看到：

$$
\text{actual history}.
$$

看不到：

$$
\text{all possible histories}.
$$

---

# 16. 所以本文避免說

> Carnot 必須靠 caloric theory 才能發現熱力學。

---

# 17. 更安全的說法

> caloric framework 在實際歷史中提供了一條後來高度 fruitful 的研究路徑。

---

# 18. Carnot case：最乾淨的核心案例

Sadi Carnot 1824 年研究熱機，

工作時期早於現代能量守恆與第二定律的成熟形式。

---

# 19. Conserved caloric

Carnot 採用當時主流觀點：

$$
\text{heat}
=
\text{conserved caloric fluid}.
$$

---

# 20. 以今天眼光看，這個 ontology 不成立

熱可以：

$$
\text{convert into work}.
$$

---

# 21. Norton 的「fortuitous error」

Norton 2022 明確指出：

Carnot 對 conserved caloric 的使用是一個：

$$
\boxed{
\text{fortuitous error}.
}
$$

---

# 22. 為什麼 fortuitous

因為在這個框架下，

heat engine 的核心被看成：

$$
\text{caloric falling from hot to cold}.
$$

---

# 23. 這迫使 heat sink 成為結構性角色

如果 caloric 必須出去，

cold sink 就不是偶然設計。

---

# 24. Carnot efficiency structure

Carnot 得到：

> 最大效率只依賴 source / sink temperatures，而不依賴 working substance 的具體種類。

---

# 25. Reversibility

更重要：

$$
\boxed{
\text{reversible process}
}
$$

成為核心。

---

# 26. 這個 descendant 後來大量存活

熱的本體圖像被修正，

但 reversible process 沒有被拋棄。

---

# 27. 甚至進入 entropy 定義

Clausius 後來的 entropy：

$$
dS
=
\frac{
dq_{\mathrm{rev}}
}{
T
}
$$

直接依賴 reversible process 概念。

---

# 28. Carnot transition map

$$
\text{caloric ontology}
\rightarrow
\text{discard / reinterpret},
$$

$$
\text{reversibility}
\rightarrow
\text{retain},
$$

$$
\text{temperature efficiency relation}
\rightarrow
\text{retain / repair}.
$$

---

# 29. Carnot 的教訓不是「錯誤最好」

而是：

$$
\boxed{
\text{wrong ontology can coexist with a structurally fertile constraint system}.
}
$$

---

# 30. 第一種結構性生產錯誤

稱為：

$$
\boxed{
\text{Ontology-Wrong / Structure-Retained}
}
$$

簡寫：

$$
OWSR.
$$

---

# 31. Phlogiston case

18 世紀燃燒常以 phlogiston 解釋。

---

# 32. Priestley

Joseph Priestley 在 1774 年隔離出後來稱為 oxygen 的氣體，

但他使用：

$$
\text{dephlogisticated air}
$$

來解釋。

---

# 33. Observation 與 interpretation 分離

氣體：

- support combustion；
- support respiration；
- 可被重複製備；

這些 observation 並沒有因 phlogiston 被推翻而消失。

---

# 34. Lavoisier

Lavoisier 用 oxygen framework 重新解釋 combustion。

---

# 35. Parent transition

$$
\text{phlogiston interpretation}
\rightarrow
\text{discard},
$$

$$
\text{gas observations}
\rightarrow
\text{retain}.
$$

---

# 36. 第二種結構性存活

稱：

$$
\boxed{
\text{Interpretation-Wrong / Observation-Retained}
}
$$

簡寫：

$$
IWOR.
$$

---

# 37. 這個案例特別重要

它證明：

$$
\boxed{
\text{experimental data}
\neq
\text{theory used to interpret the data}.
}
$$

---

# 38. AI 時代的直接類比

模型可以給錯 explanation，

但 raw measurement：

$$
D
$$

仍可保留。

---

# 39. 所以 research database 不應把 observation 和 interpretation 綁死

應存：

```text
OBSERVATION
INTERPRETATION@VERSION
```

---

# 40. Ether case：更複雜

19 世紀 electrodynamics 中，

luminiferous ether 是重要背景。

---

# 41. Lorentz theory

Lorentz 在 ether framework 下發展 moving-body electrodynamics。

---

# 42. Lorentz transformations 的前史

在 Einstein 1905 以前，

Lorentz 已發展相關 coordinate / field transformations。

---

# 43. Einstein 的改變

special relativity 不需要一個：

$$
\text{absolutely stationary luminiferous ether}.
$$

---

# 44. 但數學 transformation 沒消失

Lorentz transformation 反而成為：

$$
\boxed{
\text{special relativity 的核心 kinematic structure}.
}
$$

---

# 45. 這是一種 reinterpretation survival

$$
\text{same / related mathematics},
$$

但：

$$
\text{new ontology}.
$$

---

# 46. 第三種類型

$$
\boxed{
\text{Ontology-Replaced / Mathematics-Retained}
}
$$

簡寫：

$$
ORMR.
$$

---

# 47. 但 ether history 不能簡化

Einstein 1920 對 ether 又使用不同、廣義相對論語境下的語言。

所以：

> ether 被完全消滅

也是過度簡化。

---

# 48. 更精確的說法

1905 special relativity 不需要：

$$
\text{stationary luminiferous ether}
$$

作為 privileged mechanical medium。

---

# 49. 歷史類型必須精確

否則我們會拿一個：

$$
\text{word}
$$

跨不同 ontology 偷渡。

---

# 50. 這和 LSI-PSD-03 完全同構

同一符號：

$$
X
$$

不等於同一語義。

---

# 51. Bohr model case

Bohr model 引入：

- quantized orbits；
- discrete energy levels。

---

# 52. 對 hydrogen 成功

它能解釋 hydrogen spectral structure 的重要部分。

---

# 53. 但 classical orbit 圖像後來不可維持

現代 quantum mechanics 不把電子理解成沿精確 classical orbit 運行。

---

# 54. 多電子系統也暴露限制

Bohr model 很難直接擴展到：

$$
\text{helium and beyond}.
$$

---

# 55. 但 energy quantization 留下

不是所有結構被丟掉。

---

# 56. 第四種類型

$$
\boxed{
\text{Mechanism-Limited / Quantized-Structure-Retained}
}
$$

---

# 57. Bohr model 也提醒教育模型問題

今天教學仍會使用 Bohr-style 圖像。

---

# 58. 教育 falsehood 的問題

某模型可以：

$$
\text{literally inaccurate}
$$

但：

$$
\text{pedagogically useful}.
$$

---

# 59. 這不能直接轉成研究真理

$$
\boxed{
\text{pedagogical utility}
\neq
\text{ontological correctness}.
}
$$

---

# 60. Ideal gas：不是「錯理論被推翻」

它屬 deliberate idealization。

---

# 61. Assumptions

理想氣體常假設：

- particles point-like；
- negligible interactions。

---

# 62. 這些對真實氣體不完全成立

但在適當 regime：

$$
PV=nRT
$$

極具預測力與操作力。

---

# 63. 偏差本身又產生新科學

當：

$$
PV-nRT
\neq0,
$$

研究者可問：

> 哪個假設失效？

---

# 64. Corrections

產生：

- virial corrections；
- excluded volume；
- intermolecular interaction models。

---

# 65. 第五種類型

$$
\boxed{
\text{Known-Idealization / Deviation-Generative}
}
$$

簡寫：

$$
KIDG.
$$

---

# 66. Spagnesi 的重要性

理想模型可以成為：

$$
\boxed{
\text{regulative reference}.
}
$$

---

# 67. 模型與現象的 deviation

$$
\Delta
=
W-M
$$

不是純失敗。

可以作為：

$$
\text{explanatory input}.
$$

---

# 68. 這讓「錯誤」變成 residual science

研究：

$$
\boxed{
\text{why the world deviates from the ideal}.
}
$$

---

# 69. Minimal model

Batterman–Rice 進一步指出：

有些極簡模型的價值在於顯示：

$$
\text{which details are irrelevant}.
$$

---

# 70. 這種 model 不是越 detailed 越好

更少細節反而讓：

$$
\text{universality}
$$

更可見。

---

# 71. 第六種類型

$$
\boxed{
\text{Detail-Removed / Invariant-Revealed}
}
$$

簡寫：

$$
DRIR.
$$

---

# 72. Effective Field Theory

EFT 是更成熟的 scale-aware model practice。

---

# 73. 核心

在 cutoff：

$$
\Lambda
$$

以下，

只保留 relevant degrees of freedom。

---

# 74. EFT 不聲稱自己是 ultimate theory

它明確是：

$$
\text{effective}.
$$

---

# 75. 這使 limitation 本身制度化

$$
\boxed{
\text{scope limitation becomes part of the theory specification}.
}
$$

---

# 76. 第七種類型

$$
\boxed{
\text{Non-Fundamental / Domain-Explicit}
}
$$

簡寫：

$$
NFDE.
$$

---

# 77. Weingarten 2026 的核心

productive idealization 可以讓 non-fundamental effective theory 提供科學 understanding。

---

# 78. 這再次打破

$$
\text{more fundamental}
\Rightarrow
\text{more understanding}.
$$

---

# 79. Frigg 等人的 stability / noetic core

理想化模型若與 target 的完美模型共享：

$$
\text{behavior-stabilizing core},
$$

仍可產生 understanding。

---

# 80. 這和本文 retained structure 非常接近

我們可以寫：

$$
S_r
=
\text{stable structural core}.
$$

---

# 81. 不同文獻術語不能硬等價

noetic core、universality、retained structure、effective degrees 不完全是同一概念。

本文只指出：

$$
\text{family resemblance}.
$$

---

# 82. 歷史案例總表一

| 案例 | Parent 問題 | 被修正部分 | 存活部分 |
|---|---|---|---|
| Carnot | conserved caloric | heat ontology | reversibility / efficiency structure |
| Phlogiston | combustion explanation | interpretive mechanism | oxygen observations |
| Lorentz ether | stationary ether | spacetime ontology | Lorentz transformation structure |
| Bohr | classical quantized orbit | microscopic mechanism | discrete-energy insight |
| Ideal gas | literal particle assumptions | micro-detail fidelity | macroscopic law in regime |
| EFT | non-fundamental by design | none in naive sense | scale-appropriate structure |

---

# 83. 這張表不能誤讀

EFT 不應被列成：

> 錯理論。

它是對照組。

---

# 84. 為什麼需要對照組

它顯示一種成熟科學策略：

> 不把有限域描述誤稱 ultimate description。

---

# 85. 也就是 scope honesty

$$
\boxed{
\text{scope honesty reduces mis-specification}.
}
$$

---

# 86. 科學史的真正轉變

不是從：

$$
\text{false}
\rightarrow
\text{true}
$$

單一路徑。

---

# 87. 更像：

$$
\boxed{
\text{retain}
+
\text{reinterpret}
+
\text{repair}
+
\text{discard}.
}
$$

---

# 88. Component survival vector

對 parent：

$$
P
$$

定義：

$$
\mathbf S(P)
=
(
S_O,
S_M,
S_D,
S_L,
S_A,
S_E
).
$$

---

# 89. $S_O$

ontology survival。

---

# 90. $S_M$

mechanism survival。

---

# 91. $S_D$

domain survival。

---

# 92. $S_L$

mathematical language survival。

---

# 93. $S_A$

assumption survival。

---

# 94. $S_E$

empirical-relation survival。

---

# 95. Historical survival signature

不同案例有不同：

$$
\mathbf S.
$$

Carnot：

$$
S_O\text{ low},
\quad
S_L,S_E\text{ high}.
$$

只是概念示意，

不是精確數據。

---

# 96. Structural Retention Ratio

定義：

$$
\operatorname{SRR}
=
\frac{
\sum_i w_i s_i
}{
\sum_i w_i
}.
$$

---

# 97. 在歷史案例中不宜假裝精確

權重：

$$
w_i
$$

高度詮釋依賴。

---

# 98. 所以歷史 SRR 用於比較框架

不是：

> Carnot SRR = 0.73。

---

# 99. 真正可量化版本適合 AI benchmark

因為 AI branch 有：

- exact source；
- exact descendants；
- exact revision；
- formal verification。

---

# 100. 歷史存在性，AI 可量化性

$$
\boxed{
\text{history provides existence cases;}
\quad
\text{AI can provide controlled measurements.}
}
$$

---

# 101. 從科學史到 model discrepancy

現代工程不再只等：

> 模型被革命推翻。

---

# 102. 可以直接研究 residual

$$
r(x)
=
y_{\mathrm{obs}}
-
y_{\mathrm{model}}.
$$

---

# 103. Discrepancy Modeling Framework

Ebers、Steele、Kutz 提出：

- state-space residual learning；
- deterministic dynamical error discovery。

---

# 104. 核心思想

如果模型近似但不完整，

不要：

$$
\text{discard all physics}.
$$

---

# 105. 而是：

$$
\boxed{
\text{preserve trusted structure}
+
\text{model discrepancy}.
}
$$

---

# 106. 這就是 repair-aware science

與第 8 篇：

$$
P\rightarrow P'
$$

完全接軌。

---

# 107. LISDD 2026

進一步問：

$$
\boxed{
\text{Where is my physics wrong?}
}
$$

---

# 108. 不是：

> 我的 physics 全錯嗎？

---

# 109. 先找 clean region

$$
D_c.
$$

---

# 110. 再找 discrepant region

$$
D_e.
$$

---

# 111. 最後找 missing mechanism

$$
f_{\mathrm{missing}}.
$$

---

# 112. 這是現代版 descendant salvage

原模型：

$$
f_0
$$

沒有完全消失。

---

# 113. Physics-guided operator correction

類似：

$$
\mathcal G_{\mathrm{true}}
=
\mathcal G_{\mathrm{prior}}
+
\Delta\mathcal G.
$$

---

# 114. 核心哲學

$$
\boxed{
\text{repair the wrong part, preserve the trusted part}.
}
$$

---

# 115. 這比「模型錯／模型對」更成熟

因為現實模型幾乎都：

$$
\text{approximate}.
$$

---

# 116. Missing-physics Bayesian work

再加入：

$$
P(M_i\mid D).
$$

不是只有單一 correction。

---

# 117. Model uncertainty 成為一等物件

這是：

$$
\boxed{
\text{error-aware scientific modeling}.
}
$$

---

# 118. Experimental design for missing physics

如果有多個候選缺失機制，

下一個實驗可以被選來最大化：

$$
\text{discrimination}.
$$

---

# 119. 這使 error 直接成為研究路由器

$$
\text{discrepancy}
\rightarrow
\text{next experiment}.
$$

---

# 120. 與 LSI-PSD-06 的 obstruction 完全同構

$$
O
\rightarrow
\text{next route}.
$$

---

# 121. 但物理 discrepancy 和 proof obstruction 不是同一物件

只能做：

$$
\text{methodological analogy}.
$$

---

# 122. 2026 formal specification：另一個錯誤類型

AI 生成 formal specification：

$$
S_F
$$

可能：

$$
\text{type-check}
$$

但不符合：

$$
\text{human intent}.
$$

---

# 123. Intent-aligned specification synthesis

VeriSpecGen 類工作強調：

- atomic requirement decomposition；
- traceability map；
- targeted tests；
- localized repair。

---

# 124. 這很像 scientific discrepancy repair

只是 target 從：

$$
\text{physical world}
$$

換成：

$$
\text{human requirement}.
$$

---

# 125. Formal specification discrepancy

$$
\Delta_S
=
S_{\mathrm{intent}}
-
S_{\mathrm{formal}}.
$$

---

# 126. Traceability

知道每個 clause 對應：

$$
\text{which requirement}.
$$

---

# 127. Localized repair

失敗時修：

$$
\text{specific clause},
$$

不是整個 specification 重寫。

---

# 128. 這和 descendant provenance 完全一致

$$
\boxed{
\text{traceability is the prerequisite for selective salvage}.
}
$$

---

# 129. Formal theorem benchmark defects

2026 benchmark audit 又展示更嚴重版本：

$$
Q_F
$$

可能：

- vacuous；
- missing hypothesis；
- wrong translation；
- counterexample-bearing。

---

# 130. 所以：

$$
\boxed{
\text{proof success}
\neq
\text{problem fidelity}.
}
$$

---

# 131. 這是 AI 時代的新「父框架錯置」

parent 不一定是 physical theory。

也可以是：

$$
\boxed{
\text{formal specification}.
}
$$

---

# 132. Machine-checked error

最反直覺：

一個 formal object 可以 machine-check，

但仍是錯 target。

---

# 133. 這不矛盾

kernel 只保證：

$$
\text{proof matches formal statement}.
$$

---

# 134. 它不保證：

$$
\text{formal statement matches intended meaning}.
$$

---

# 135. 這是 representation fidelity 問題

與：

$$
\text{mathematical validity}
$$

不同層。

---

# 136. 歷史與 AI 的共同結構

$$
\boxed{
\text{parent representation}
\rightarrow
\text{research outputs}
\rightarrow
\text{revision}
\rightarrow
\text{selective survival}.
}
$$

---

# 137. 差異

科學史：

$$
\text{revision over decades / centuries}.
$$

AI：

$$
\text{revision over minutes / days}.
$$

---

# 138. AI 速度放大污染

若 parent defect：

$$
e
$$

存在，

generation rate：

$$
g
$$

高，

則：

$$
N_{\mathrm{affected}}
\propto
g\Delta t.
$$

---

# 139. 所以 AI 時代更需要早期 audit

不是更少。

---

# 140. Historical lag vs AI lag

科學史中：

$$
\Delta t_{\mathrm{revision}}
$$

可能數十年。

---

# 141. AI 可縮短

如果：

- formal verifier；
- counterexample search；
- multiple models；
- provenance；

都存在。

---

# 142. 但 AI 也能增加錯誤密度

所以：

$$
\text{speed}
$$

是雙刃。

---

# 143. Historical-to-AI Translation Principle

本文提出：

$$
\boxed{
\textbf{Historical theory change should be translated into AI research as versioned component revision, not binary memory deletion.}
}
$$

---

# 144. Parent component ledger

```yaml
parent:
  ontology:
  mechanism:
  domain:
  representation:
  assumptions:
  empirical_relations:
```

---

# 145. Revision ledger

```yaml
revision:
  retained:
  reinterpreted:
  repaired:
  discarded:
```

---

# 146. Descendant ledger

```yaml
descendant:
  dependency:
  original_parent_version:
  post_revision_status:
  transfer:
```

---

# 147. 科學史可做 schema validation

看 schema 是否能合理表達：

- Carnot；
- phlogiston；
- ether；
- Bohr；
- ideal gas；
- EFT。

---

# 148. 如果一個 schema 只能處理「整個錯／整個對」

就太粗。

---

# 149. Theory Replacement Index

定義：

$$
R_T
=
\frac{
N_{\mathrm{discarded}}
}{
N_{\mathrm{components}}
}.
$$

---

# 150. Theory Retention Index

$$
R_S
=
1-R_T
$$

概念上。

---

# 151. 但 component granularity 會影響值

所以：

$$
R_T
$$

不能跨研究隨便比。

---

# 152. Granularity declaration

任何 retention metric 必須聲明：

$$
\text{component ontology}.
$$

---

# 153. 這和 proof-space quotient 同一問題

分得越細：

$$
N_{\mathrm{components}}\uparrow.
$$

---

# 154. 所以歷史計量也需要 quotient discipline

---

# 155. Historical survivor class

本文建議只做 coarse classes：

1. empirical；
2. mathematical；
3. methodological；
4. instrumental；
5. conceptual；
6. ontological。

---

# 156. Empirical survivor

數據／觀察。

---

# 157. Mathematical survivor

公式、轉換、定理。

---

# 158. Methodological survivor

實驗設計、推理方法。

---

# 159. Instrumental survivor

儀器、技術。

---

# 160. Conceptual survivor

例如 reversible process。

---

# 161. Ontological survivor

對世界構成的實體承諾。

---

# 162. Carnot signature

大致：

- empirical：中；
- mathematical：高；
- conceptual：高；
- ontological：低。

---

# 163. Phlogiston signature

- empirical：高；
- interpretive ontology：低。

---

# 164. Lorentz ether signature

- mathematical：高；
- stationary-medium ontology：低。

---

# 165. Bohr signature

- pedagogical / conceptual：中高；
- exact mechanism：低；
- energy quantization：高。

---

# 166. Ideal gas signature

- domain-conditioned law：高；
- literal micro ontology：低。

---

# 167. EFT signature

它不是 parent failure case。

而是：

$$
\boxed{
\text{explicitly limited theory design}.
}
$$

---

# 168. EFT 是成熟反例

它說明：

> 我們不一定要等到 theory 被推翻才承認有限域。

---

# 169. 這是一種提前防錯置

$$
\boxed{
\text{scope declaration}
\rightarrow
\text{lower revision shock}.
}
$$

---

# 170. Revision shock

定義：

$$
S_R
=
\frac{
N_{\mathrm{descendants\ requiring\ reaudit}}
}{
N_{\mathrm{active\ descendants}}
}.
$$

---

# 171. Scope-honest model 預期較低 $S_R$

這是一個可實驗的 AI hypothesis。

---

# 172. Historical asymmetry

早期 theory 常缺少今天的：

- measurement precision；
- formal tools；
- computing；
- data infrastructure。

---

# 173. 所以不能以今天標準嘲笑歷史

錯理論可能是：

$$
\text{best available structure under historical constraints}.
$$

---

# 174. 這和 AI 弱模型 regime 類似

弱 AI：

$$
R_1
$$

可能需要 simplifying assumptions。

---

# 175. 強 AI：

$$
R_2
$$

可能不需要。

---

# 176. 所以「productive error」可能 intelligence-conditioned

$$
\Phi_E
=
\Phi_E(P,R).
$$

---

# 177. 歷史 progress 的另一層

一些理論之所以 fertile，

不只因理論內容。

還因：

- institution；
- instrumentation；
- notation；
- social network。

---

# 178. 本文不還原到單一 logical mechanism

所以：

$$
C_f
$$

反事實信心必須保守。

---

# 179. 科學史不是 controlled experiment

這點不能忘。

---

# 180. 因此歷史只提供

$$
\boxed{
\text{existence and pattern evidence}.
}
$$

不是：

$$
\boxed{
\text{clean causal estimate}.
}
$$

---

# 181. AI benchmark 可以補足

因為可以：

- branch；
- randomize；
- control budget；
- reveal ground truth。

---

# 182. 這是 PMW-Bench 的意義

第 9 篇提出：

$$
\text{controlled deviation experiments}.
$$

---

# 183. 第 11 篇現在提供歷史 taxonomy

兩者結合。

---

# 184. Historical-to-Benchmark Mapping

| Historical pattern | Synthetic AI analogue |
|---|---|
| caloric ontology | wrong mechanism assumption |
| phlogiston interpretation | wrong label / interpretation |
| ether ontology | representation ontology mismatch |
| Bohr limitation | limited-domain mechanistic model |
| ideal gas | deliberate idealization |
| EFT | explicit scope model |

---

# 185. Carnot benchmark

建立 dynamical system，

給 agent 一個：

$$
\text{wrong conservation assumption}
$$

但保留某個 structural invariant。

---

# 186. 看是否產生可存活 descendants

測：

$$
S_D.
$$

---

# 187. Phlogiston benchmark

給正確 observations，

配錯 interpretation ontology。

---

# 188. 看 agent 能否在 parent revision 後保留 data

---

# 189. Ether benchmark

給一套錯 ontology，

但數學 transformation 正確。

---

# 190. 看 AI 是否能：

$$
\text{reinterpret rather than discard}.
$$

---

# 191. Bohr benchmark

給 limited model，

測 agent 是否：

- 正確在 domain 內使用；
- 遇 domain expansion 時升級模型。

---

# 192. Idealization benchmark

給 controlled simplification，

測 deviation discovery。

---

# 193. EFT benchmark

測 system 是否能：

$$
\text{declare scope explicitly}.
$$

---

# 194. AI research 的 mature response

不是：

> 我錯了，全部忘記。

---

# 195. 也不是：

> 我曾經產生有用結果，所以我沒錯。

---

# 196. 而是：

$$
\boxed{
\text{revise parent}
+
\text{re-audit descendants}
+
\text{retain survivors}.
}
$$

---

# 197. 這是科學史壓縮後的工程原則

---

# 198. 從 theory history 到 knowledge lineage

傳統描述：

$$
T_1
\rightarrow
T_2
\rightarrow
T_3.
$$

---

# 199. 更真實：

$$
T_1
\rightarrow
\{
d_1,d_2,d_3
\}
$$

再：

$$
T_2
$$

保留其中：

$$
d_1,d_3.
$$

---

# 200. 因此 history 是 DAG

不是線。

---

# 201. Knowledge lineage graph

$$
G_K
=
(V_K,E_{\mathrm{inherit}}).
$$

---

# 202. Theory node 只是其中一類

還有：

- data；
- method；
- lemma；
- concept；
- tool。

---

# 203. 科學革命不是 memory reset

而是 graph rewiring。

---

# 204. 這和 Goedel-Architect 類 blueprint repair 很像

只是尺度從 proof graph 放大到 scientific knowledge graph。

---

# 205. 但這是類比

不能說歷史科學就是 formal proof graph。

---

# 206. Structural survival 的原因

可能來自：

1. empirical anchoring；
2. mathematical invariance；
3. scale robustness；
4. method independence；
5. semantic reinterpretability。

---

# 207. Empirical anchoring

observation 可被不同 theory 重解釋。

---

# 208. Mathematical invariance

公式結構跨 ontology 保留。

---

# 209. Scale robustness

relation 在特定尺度仍有效。

---

# 210. Method independence

結果不依賴 parent 的錯 assumption。

---

# 211. Semantic reinterpretability

同一 formal object 可被新 ontology 賦予不同解釋。

---

# 212. Survival predictor

可以建立：

$$
P(S_i=1)
=
f(
E_A,
I_M,
R_S,
M_I,
S_R
).
$$

---

# 213. 這在歷史上難估

但 AI synthetic benchmark 可估。

---

# 214. Scientific realism 的接口

realist 會關心：

> 存活是否支持對結構的實在論？

---

# 215. Structural realism 的近鄰

歷史上理論變換中 mathematical structure 存活，

常被拿來討論 structural realism。

---

# 216. 本文不選邊

我們只使用較弱命題：

$$
\boxed{
\text{some structure can persist across theory change}.
}
$$

---

# 217. Instrumentalism 的接口

instrumentalist 可能說：

> 模型只要有效。

---

# 218. 本文也不接受純 utility replacement

因為：

$$
\text{survival audit}
$$

仍然 truth-sensitive。

---

# 219. 我們不是說有用就真

也不是說不真就沒用。

---

# 220. 這正是第 7 篇的核心

$$
T\neq G.
$$

---

# 221. 第 11 篇的新增

$$
\boxed{
\text{theory change can redistribute truth and utility across components}.
}
$$

---

# 222. 不是所有 retained structure 都「真」

有些只是：

- approximation；
- effective relation；
- coordinate convention。

---

# 223. 所以 survivor status 還要分類

$$
\text{exact},
\text{effective},
\text{approximate},
\text{instrumental}.
$$

---

# 224. AI memory 不應把四類混在一起

---

# 225. Survivor metadata

```yaml
survival_status:
  exact:
  approximate:
  effective:
  pedagogical:
  instrumental:
```

---

# 226. 這可以防止歷史錯讀

例如：

> Bohr model 還在教，所以它是真的。

錯。

---

# 227. 教育使用 ≠ fundamental truth

---

# 228. 也防止 ideal gas 錯讀

> 理想氣體是假，所以不能用。

同樣錯。

---

# 229. Domain statement 必須跟著 model

$$
M@D.
$$

---

# 230. Model without domain is incomplete metadata

---

# 231. 這也是 EFT 最成熟的教訓之一

---

# 232. Error-aware ontology

未來 AI knowledge base 應允許：

```text
MODEL:
  valid_scope:
  known_idealizations:
  known_failure_modes:
  successor_models:
```

---

# 233. 不是只存：

```text
TRUE / FALSE
```

---

# 234. Historical correction mode

四種：

$$
\boxed{
\text{replace},
\text{restrict},
\text{reinterpret},
\text{extend}.
}
$$

---

# 235. Replace

phlogiston combustion explanation。

---

# 236. Restrict

Bohr / ideal-gas style domain narrowing。

---

# 237. Reinterpret

Lorentz transformation under new spacetime framework。

---

# 238. Extend

effective models + correction term。

---

# 239. Correction-mode classification 是 AI revision engine 的核心

---

# 240. Historical case confidence

本文建議每個案例附：

$$
C_H
\in
\{
\text{high},
\text{medium},
\text{low}
\}.
$$

---

# 241. High

史料直接支持。

---

# 242. Medium

學界合理重構。

---

# 243. Low

強反事實：

> 沒有 A 就沒有 B。

---

# 244. 本文只依靠 high / medium claims

---

# 245. Carnot direct evidence

Norton 明確稱：

$$
\text{conserved caloric}
$$

為 fortuitous error。

---

# 246. Phlogiston direct evidence

ACS 歷史資料記錄：

Priestley 使用 dephlogisticated-air 解釋，

Lavoisier 後來以 oxygen chemistry 取代 phlogiston。

---

# 247. Ether direct evidence

Einstein 1905 認為 stationary luminiferous ether 在其理論中是 superfluous；

Lorentz transformation 仍成為 SR 結構。

---

# 248. Bohr direct evidence

現代教材明確指出其精確軌道圖像受限，

量子力學取代該 microscopic picture。

---

# 249. Idealization direct evidence

科學哲學文獻廣泛承認 scientific models 可含 deliberate idealization。

---

# 250. EFT direct evidence

現代物理明確把 EFT 當有限尺度的有效理論。

---

# 251. 所以案例族是異質的

這是優點。

---

# 252. 因為我們不是在證明單一「錯理論定律」

而是在找：

$$
\boxed{
\text{different mechanisms of partial survival}.
}
$$

---

# 253. 生產性錯誤 taxonomy

本文總結七類：

$$
OWSR,
IWOR,
ORMR,
MLQR,
KIDG,
DRIR,
NFDE.
$$

---

# 254. MLQR

Mechanism-Limited / Quantized-Structure-Retained。

---

# 255. 七類不是互斥

一個案例可同時多類。

---

# 256. 這是 tagging system

不是 natural kinds 的宣稱。

---

# 257. Error-to-survival matrix

$$
M_{ij}
=
P(
\text{survival type }j
\mid
\text{error type }i
).
$$

---

# 258. 歷史上無法可靠估

---

# 259. AI benchmark 可以估

這是未來方向。

---

# 260. 從歷史到 empirical epistemology

真正新東西不是重新講 Carnot。

---

# 261. 而是把 Carnot 類模式轉成可測問題

$$
\boxed{
\text{Which error structures systematically generate salvageable knowledge?}
}
$$

---

# 262. 科學史提供 hypothesis generator

不是 final estimator。

---

# 263. AI 提供 estimator

如果 benchmark 設計好。

---

# 264. 對 NS-203 的啟示

目前只能做：

$$
\text{historically informed caution}.
$$

---

# 265. 不能說

> NS 就像 caloric theory。

---

# 266. 因為我們不知道 parent 是否錯

---

# 267. 可以說

> 如果未來某 NS route framing 被修正，歷史告訴我們不應假定其全部 descendants 一起失效。

---

# 268. 因此現在就應保存 provenance

這是立即可行的工程結論。

---

# 269. NS corpus 的 historical-readiness

每個 artifact 應存：

- assumptions；
- formal claims；
- lemma；
- obstruction；
- transfer；
- status。

---

# 270. 如果未來 parent revision

立刻跑：

$$
\operatorname{Reaudit}.
$$

---

# 271. 對 P/NP 同理

proof barrier 的 descendants 可存活，

不論最終 verdict 是什麼。

---

# 272. Barrier results 本身就是 historical survivors candidate

---

# 273. 理論歷史告訴我們一件更深的事

科學知識不是一棵：

$$
\text{truth tree}.
$$

---

# 274. 更像版本化圖

$$
\boxed{
\text{claims}
+
\text{evidence}
+
\text{interpretations}
+
\text{dependencies}.
}
$$

---

# 275. 這正是 AI knowledge architecture 應採用的形式

---

# 276. Historical epistemology becomes data architecture

這是本文的工程轉譯。

---

# 277. 非主張總表

本文不主張：

1. 錯誤理論一般比正確理論更有價值；
2. Carnot 的 caloric ontology 是正確的；
3. Carnot 必須依靠 caloric theory 才能發現可逆熱機；
4. phlogiston theory 因氧氣發現而獲得真理地位；
5. Priestley 的 interpretation 與 Lavoisier 的 oxygen theory 等價；
6. luminiferous ether 與廣義相對論中 Einstein 1920 使用的 ether 一詞同義；
7. Lorentz ether theory 與 special relativity 在 ontology 上等價；
8. Bohr model 在現代量子力學中仍是 fundamental model；
9. ideal gas 是 accidental scientific error；
10. effective field theory 是「錯理論」；
11. minimal model 的少細節必然比 detailed model 更好；
12. 模型越不真，理解力越高；
13. 科學史存在單一路徑、線性、必然的 rational progress；
14. retained mathematical structure 自動證明 structural realism；
15. utility 可以取代 truth；
16. history case study 可以提供 clean causal estimate；
17. NS 問題就是 Carnot 類型的 mis-specification；
18. P/NP 就是 ether 類型的 representation error；
19. AI 長期證不出來可以由科學史推導成「問題問錯」；
20. formal theorem proof 自動保證 formalization faithful；
21. specification defect 會使所有 proof artifacts 歸零；
22. parent revision 後所有 observations 都必然存活；
23. historical survivor ratio 可以不宣告 granularity 就精確量化；
24. scientific consensus 決定理論真值；
25. 本文已建立 universal law of productive error。

---

# 278. 形式命題一：Componentwise Revision

$$
\boxed{
P\rightarrow P'
\not\Rightarrow
\text{all components are discarded}.
}
$$

---

# 279. 形式命題二：Interpretation–Observation Separation

$$
\boxed{
\operatorname{False}(I)
\not\Rightarrow
\operatorname{False}(O).
}
$$

其中 $I$ 為 interpretation， $O$ 為獨立觀測事實。

---

# 280. 形式命題三：Ontology–Mathematics Separation

$$
\boxed{
\operatorname{Reject}(O_{\mathrm{ontology}})
\not\Rightarrow
\operatorname{Reject}(L_{\mathrm{math}}).
}
$$

---

# 281. 形式命題四：Scope Honesty

若：

$$
M
$$

明示：

$$
D_M,
$$

則：

$$
M
$$

在 $D_M$ 外失效不必自動視為 parent contradiction。

---

# 282. 形式命題五：Revision Map Requirement

任何「舊理論被新理論取代」的精確分析，

應至少給：

$$
\mathcal T_{P\rightarrow P'}.
$$

---

# 283. 形式命題六：Historical Counterfactual Humility

從 realized path：

$$
P\rightarrow D
$$

不能推出：

$$
P
$$

是 $D$ 的唯一必要原因。

---

# 284. 形式命題七：AI Salvage Principle

當 AI parent artifact 修正：

$$
P\rightarrow P',
$$

應進行 component-level descendant re-audit，

而不是自動全刪或全保留。

---

# 285. 與第 7 篇的整合

第 7 篇：

$$
T\neq G.
$$

歷史案例證明：

$$
\text{low truth in one component}
$$

可以與：

$$
\text{high generativity in another component}
$$

共存。

---

# 286. 與第 8 篇的整合

第 8 篇：

$$
\text{parent failure non-annihilation}.
$$

第 11 篇給出歷史 case family。

---

# 287. 與第 9 篇的整合

第 9 篇提出：

$$
\text{productive window}.
$$

歷史案例只能作：

$$
\text{hypothesis inspiration}.
$$

---

# 288. 不能用歷史直接畫 inverted-U

沒有 counterfactual branches。

---

# 289. 與第 10 篇的整合

第 10 篇說：

$$
\text{saturation is not verdict}.
$$

第 11 篇補：

> 即使 verdict 最後真的改寫 parent，仍然需要逐項判斷 descendants。

---

# 290. 所以二者形成雙重保守

在 verdict 前：

$$
\text{不要過早判 parent}.
$$

在 verdict 後：

$$
\text{不要過早刪 descendants}.
$$

---

# 291. 這是完整 epistemic lifecycle

$$
\boxed{
\text{explore}
\rightarrow
\text{evaluate}
\rightarrow
\text{revise}
\rightarrow
\text{salvage}.
}
$$

---

# 292. 對 AI 科學的制度建議一

所有 theory object 都版本化。

---

# 293. 制度建議二

observation 與 interpretation 分離儲存。

---

# 294. 制度建議三

每個 formula 存 ontology / domain metadata。

---

# 295. 制度建議四

parent revision 自動建立 re-audit queue。

---

# 296. 制度建議五

不可 silent delete history。

---

# 297. 制度建議六

不可把 discarded theory 完全當垃圾，

但也不可繼續標 active truth。

---

# 298. Archive status

```text
HISTORICAL
REFUTED
LIMITED
SUPERSEDED
EFFECTIVE
ACTIVE
```

---

# 299. 這比「old」精確

---

# 300. Scientific memory maturity

成熟 science memory 應知道：

> 這個公式從哪個理論來、現在為什麼還在用、其原本 interpretation 是否仍被接受。

---

# 301. AI 特別需要

因為 AI 容易把不同時代文字混成 contemporaneous truth。

---

# 302. Historical semantics

同一詞：

$$
\text{ether}
$$

在不同年代不是同一概念。

---

# 303. 所以 temporal metadata

$$
t
$$

也是 semantic coordinate。

---

# 304. 完整 claim

$$
p^\star
=
p(D,C,t,F,S).
$$

這和先前真理邊界研究一致。

---

# 305. 時間是 theory meaning 的一部分

科學史資料庫不能去時間化。

---

# 306. 這也是 AI RAG 的問題

retriever 只看 lexical similarity，

可能把不同 ontology 混在一起。

---

# 307. Historical RAG 應加：

- date；
- framework；
- status；
- successor theory。

---

# 308. 這會減少 anachronism

---

# 309. 科學史不是裝飾

它可以直接改善 AI knowledge routing。

---

# 310. 例如查「ether」

系統先問：

$$
\text{which ether?}
$$

---

# 311. 查「Bohr orbit」

先顯示：

$$
\text{historical / pedagogical status}.
$$

---

# 312. 查「ideal gas」

顯示：

$$
\text{validity regime}.
$$

---

# 313. 這就是 status-aware retrieval

---

# 314. 對 proof corpus 也一樣

查某 lemma：

先看：

$$
\text{which parent version?}
$$

---

# 315. 歷史方法與 proof-space observatory 合流

$$
\boxed{
\text{context-aware lineage retrieval}.
}
$$

---

# 316. 未來研究一：Historical Lineage Dataset

建立：

$$
\text{Theory Revision Corpus}.
$$

---

# 317. 每個案例存：

- parent；
- successor；
- retained components；
- discarded components；
- primary sources；
- confidence。

---

# 318. 未來研究二：AI Salvage Benchmark

故意注入 parent defect，

讓 AI 產生 descendants。

---

# 319. 後來 reveal correction

測 salvage。

---

# 320. 未來研究三：Status-Aware RAG

看是否降低：

- anachronism；
- obsolete-theory hallucination；
- false equivalence。

---

# 321. 未來研究四：Historical Counterfactual Sandbox

讓 AI 在 historically inspired toy world 走多條 branch。

---

# 322. 不把它當真歷史

而是：

$$
\text{epistemic dynamics experiment}.
$$

---

# 323. 未來研究五：Structure survival predictor

訓練模型預測：

$$
\text{which descendants survive parent revision}.
$$

---

# 324. 預測器不能決定 truth

只是 audit priority。

---

# 325. 未來研究六：Theory-status compiler

輸入：

$$
\text{scientific corpus}.
$$

輸出：

```text
ACTIVE
LIMITED
HISTORICAL
REFUTED
EFFECTIVE
```

---

# 326. 這對 AI 科普和科研都重要

---

# 327. 最終歷史矩陣

| Case | Error / limitation | Retained asset | Transition type | Modern analogue |
|---|---|---|---|---|
| Carnot | conserved caloric | reversibility / efficiency | reinterpret + repair | wrong mechanism, stable structure |
| Phlogiston | combustion interpretation | gas observations | interpretation replacement | label/model error, data survival |
| Lorentz ether | privileged medium ontology | transformations | ontology replacement | representation survival |
| Bohr | precise orbit picture | quantized energy scaffold | scope restriction + replacement | limited model |
| Ideal gas | deliberate micro idealization | macroscopic law | domain conditioning | controlled approximation |
| EFT | non-fundamental by design | scale-relevant dynamics | explicit scope | mature model governance |
| AI formal spec | target mismatch | some proofs/tools | localized repair | specification revision |
| AI physics model | missing mechanism | trusted prior | residual correction | discrepancy modeling |

---

# 328. 這張表最重要的不是「錯誤」

而是：

$$
\boxed{
\text{transition type}.
}
$$

---

# 329. 如果知道 transition type

才能知道：

> 應該刪什麼，留什麼。

---

# 330. 結論

科學史真正反覆告訴我們的，不是：

> 錯誤很棒。

而是：

$$
\boxed{
\text{科學理論不是不可分割的單一真值塊。}
}
$$

一個 parent framework 可以同時包含：

- 被後來拒絕的 ontology；
- 仍有效的 empirical data；
- 被重新詮釋的 mathematical structure；
- 被保留的方法；
- 被限制到局部 domain 的 approximation。

Carnot 的 conserved caloric 被修正，但 reversibility 成為 thermodynamics 的核心資產；Priestley 的 phlogiston interpretation 被替換，但 oxygen observations 留下；Lorentz 的 stationary ether ontology 失去必要性，但 transformation structure 進入 special relativity；Bohr 的 classical-orbit mechanism 被 quantum mechanics 超越，但 quantized-energy scaffold 仍具有歷史、教育與局部計算價值；ideal gas 甚至從一開始就是一種明知失真的 model；effective field theory 則進一步把 scale limitation 直接寫入成熟的 theory practice。

所以科學史更接近：

$$
\boxed{
\text{revision}
+
\text{reinterpretation}
+
\text{selective retention}.
}
$$

而不是：

$$
\text{old false}
\rightarrow
\text{new true}.
$$

當 AI 開始以極高速生成 theorem、model、simulation、formal specification 與 research branches 時，這個歷史教訓變成了一個直接的資料工程問題。AI 不能只保存：

```text
THEORY = TRUE
```

或：

```text
THEORY = FALSE
```

它必須保存：

$$
\boxed{
\text{which component,
under which scope,
in which version,
with which descendants,
survived which revision}.
}
$$

這也讓「生產性錯置」從哲學直覺進入可操作制度。

歷史告訴我們：

$$
\boxed{
\exists P,P':
P\text{ is revised}
\land
\mathcal D_{\mathrm{surv}}(P\rightarrow P')\neq\varnothing.
}
$$

AI 則第一次讓我們有機會進一步測量：

$$
\boxed{
\text{which kinds of }P\rightarrow P'
\text{ systematically maximize durable descendant survival}.
}
$$

因此本文最終提出：

$$
\boxed{
\textbf{The right unit of scientific continuity is not the theory name, but the lineage of structures, observations, methods, and claims that survive revision.}
}
$$

以及：

$$
\boxed{
\textbf{What survives a theory may be scientifically more informative than the binary fact that the theory itself survived.}
}
$$

這兩句話把 Carnot 的十九世紀問題與 AI 的二十一世紀研究基礎設施真正接在了一起。

---

# 參考文獻

1. Norton, J. D. (2022). **How Analogy Helped Create the New Science of Thermodynamics.** *Synthese*, 200, 269. https://doi.org/10.1007/s11229-022-03708-9

2. Carnot, S. (1824). **Réflexions sur la puissance motrice du feu et sur les machines propres à développer cette puissance.**

3. American Chemical Society. **Joseph Priestley, Discoverer of Oxygen — National Historic Chemical Landmark.** https://www.acs.org/education/whatischemistry/landmarks/josephpriestleyoxygen.html

4. American Chemical Society. **Antoine-Laurent Lavoisier: The Chemical Revolution — International Historic Chemical Landmark.** https://www.acs.org/education/whatischemistry/landmarks/lavoisier.html

5. Einstein, A. (1905). **Zur Elektrodynamik bewegter Körper.** *Annalen der Physik*, 17, 891–921.

6. Einstein, A. (1920). **Ether and the Theory of Relativity.** Leiden lecture; English translation collected in *Sidelights on Relativity*.

7. Janssen, M. and related historical scholarship on Lorentz transformations and pre-relativistic electrodynamics. See also historical analyses of Lorentz’s theorem of corresponding states.

8. OpenStax. **The Bohr Model.** *Chemistry: Atoms First* and *Physics*. Modern educational summary of the model’s achievements and limitations.

9. Frigg, R., & Hartmann, S. **Models in Science.** *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/models-science/

10. Batterman, R. W., & Rice, C. C. (2014). **Minimal Model Explanations.** *Philosophy of Science*, 81(3), 349–376. https://doi.org/10.1086/676677

11. Rice, C. (2021). **Leveraging Distortions: Explanation, Idealization, and Universality in Science.** MIT Press.

12. Spagnesi, L. (2025). **Truth, Understanding, and Normativity in Scientific Models.** *Synthese*, 206.

13. Frigg, R., Nguyen, J., & collaborators (2025). **Stabilising Understanding.** *Philosophical Studies*. On idealized models, stability, and noetic cores.

14. Weingarten, K. (2026). **Productive Idealizations for Scientific Understanding: A Case Study in Effective Theories.** PhilSci-Archive preprint. https://philsci-archive.pitt.edu/27959/

15. Stanford Encyclopedia of Philosophy. **Intertheory Relations in Physics.** Spring 2026 edition; discussion of effective field theory and scale-sensitive theory relations.

16. Ebers, M. R., Steele, K. M., & Kutz, J. N. (2022). **Discrepancy Modeling Framework: Learning missing physics, modeling systematic residuals, and disambiguating between deterministic and random effects.** arXiv:2203.05164.

17. Wang, Y. (2026). **Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy.** arXiv:2606.23215.

18. Ma, L. et al. (2026). **Physics-guided correction for operator learning under model misspecification.** arXiv:2606.03469.

19. Strouwen, A., & Micluţa-Câmpeanu, S. (2026). **Experimental Design for Missing Physics.** arXiv:2604.01231.

20. Strouwen, A. (2026). **Bayesian Inference for Missing Physics.** arXiv:2603.14918.

21. Ye, Z. et al. (2026). **Intent-aligned Formal Specification Synthesis via Traceable Refinement.** arXiv:2604.10392.

22. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493.

23. Zhang, K. et al. (2026). **Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization.** arXiv:2606.31002.

24. King, M. (2025). **Experiment and the Pursuit of Ugly Models.** *European Journal for Philosophy of Science*, 15, Article 55.

25. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：歷史案例比較表

| Case | Error Type | Retained Structure | Repair Mode | Descendant Status |
|---|---|---|---|---|
| Carnot | ontology | reversibility / efficiency | reinterpret + repair | high historical retention |
| Phlogiston | interpretation / mechanism | oxygen observations | replace interpretation | empirical survival |
| Lorentz ether | ontology | transformation mathematics | reinterpret | mathematical survival |
| Bohr | mechanism / scope | discrete energies | restrict + supersede | partial survival |
| Ideal gas | deliberate idealization | macroscopic law | domain-bound use | effective survival |
| EFT | explicit non-fundamentality | low-energy structure | scope declaration | designed persistence |

---

## 附錄 B：Historical Revision Record

```yaml
case_id:
historical_period:
parent_framework:

components:
  ontology:
  mechanism:
  domain:
  representation:
  assumptions:
  observations:

revision:
  successor_framework:
  retained:
  reinterpreted:
  repaired:
  discarded:

descendants:
  empirical:
  mathematical:
  methodological:
  instrumental:
  conceptual:
  ontological:

confidence:
  direct_source:
  retrospective_reconstruction:
  counterfactual_claim:
```

---

## 附錄 C：AI Translation Record

```yaml
parent_version:
error_type:
scope:
known_failure_mode:

descendant_assets:
  theorem:
  observation:
  tool:
  dataset:
  method:
  obstruction:
  negative_result:

revision:
  new_parent:
  changed_components:

reaudit:
  retained:
  repaired:
  transferred:
  discarded:
  unknown:
```

---

## 附錄 D：七種暫定結構類型

| Code | 名稱 |
|---|---|
| OWSR | Ontology-Wrong / Structure-Retained |
| IWOR | Interpretation-Wrong / Observation-Retained |
| ORMR | Ontology-Replaced / Mathematics-Retained |
| MLQR | Mechanism-Limited / Quantized-Structure-Retained |
| KIDG | Known-Idealization / Deviation-Generative |
| DRIR | Detail-Removed / Invariant-Revealed |
| NFDE | Non-Fundamental / Domain-Explicit |

這些只是比較標籤，不是自然種類定理。

---

## 附錄 E：一句話版本

$$
\boxed{
\text{科學理論被修正時，真正值得追蹤的不是「舊理論死了沒有」，而是「哪些結構穿過了理論更替仍然活著」。}
}
$$

對 AI 而言，這句話會直接變成資料庫與研究記憶的設計原則。
