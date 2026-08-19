# LSI-PSD-11 — 從 Carnot 到 AI：結構性錯誤的科學史與模型論

## From Carnot to AI: A History and Philosophy of Structured Error

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

「錯誤理論仍可產生正確知識」不是 AI 時代才出現的現象。本文以科學史與模型哲學為案例層，檢查本系列的生產性錯置命題。核心案例包括：Carnot 在 caloric theory 背景下建立熱機效率的一般理論；Priestley 在 phlogiston framework 中發現氧氣相關現象，而 Lavoisier 後來重構燃燒理論；以太框架在相對論前史中促成對 length contraction、local time 與 Lorentz transformation 的發展；現代科學則制度化使用 idealized models、minimal models 與 effective field theories。本文不把這些案例粗暴地歸納為「錯誤越多越好」，而將它們分解成四個機制：錯誤框架保留真實局部結構、錯誤暴露可測 discrepancy、理想化移除無關細節、舊框架產生後來可遷移的數學工具。這些機制共同支持較弱但更可靠的結論：scientific fruitfulness 與 literal truth 並非單調同一。

**關鍵詞：** Carnot、caloric theory、phlogiston、ether、idealization、minimal models、effective field theory、scientific history

---

## 1. 歷史案例的用途與危險

科學史案例很容易被濫用。

我們今天知道某理論被替代，就會把它描述成：

$$
\text{wrong theory}
\to
\text{right theory}.
$$

但真正歷史往往更複雜：

- 舊理論包含部分可靠經驗結構；
- 新理論保留舊數學的一部分；
- 實驗不是一次性裁決；
- 同一概念的意義會在轉換中改變。

因此本文不用歷史案例「證明」 PMW，只用來測試：

$$
\boxed{
\text{parent error and descendant value can be separated in real science.}
}
$$

---

## 2. Carnot：錯誤熱本體與正確熱機結構

Carnot 的 1824 工作建立了熱機效率研究的基礎，但他的推理處於 caloric theory 背景中：熱被視為守恆的流體式實體。

按照現代能量觀，這個本體與部分量化推論並不正確；熱可以與功發生能量轉換。

然而 Norton 對 Carnot 的歷史與哲學分析指出，Carnot 的 waterfall analogy 與 reversible-process thinking 仍促成了極具一般性的熱機理論。

這個案例可表示為：

$$
P_{\mathrm{caloric}}
\to
\{
D_{\mathrm{reversibility}},
D_{\mathrm{efficiency}},
D_{\mathrm{cycle}},
\ldots
\}.
$$

後來：

$$
V(P_{\mathrm{caloric}})=0
$$

不妨礙部分 $D_i$ 被重新解釋、修正與保留。

Carnot 案例因此不是「錯誤神奇地變真」，而是：

$$
\boxed{
\text{a false parent ontology contained and generated salvageable structure.}
}
$$

---

## 3. Phlogiston：錯誤解釋框架中的新現象

十八世紀燃燒研究長期由 phlogiston theory 組織。Priestley 在這個框架中研究 gases，並把後來稱為 oxygen 的氣體理解為 dephlogisticated air。

American Chemical Society 的歷史資料明確記錄：Priestley 的發現發生在 phlogiston framework 中；Lavoisier 後來使用相關實驗結果建立新的氧化與燃燒理論，並反對 phlogiston。

因此：

$$
\text{wrong explanatory ontology}
$$

可以和：

$$
\text{good experimental production}
$$

共存。

這是一個重要分離：

$$
\boxed{
\text{discovery competence}
\neq
\text{correct ontology}.
}
$$

對 AI 科學尤其重要，因為 AI 可能提出錯誤 explanation，卻設計出有價值的 experiment 或 auxiliary computation。

---

## 4. Ether：被拋棄的本體與被保留的數學

十九世紀末，光與電磁理論常以 luminiferous ether 作為傳播背景。Michelson--Morley 等結果與相對論的發展使 ether 不再是特殊相對論所需的本體。

但 Lorentz 與同時代工作的數學發展，包括 local time、length contraction 與 Lorentz transformation，並沒有因 ether ontology 被放棄而消失。

歷史路徑更像：

$$
\text{ether problem}
\to
\text{mathematical compensations}
\to
\text{transformation structure}
\to
\text{new spacetime interpretation}.
$$

這是「descendant mathematical structure survives ontology replacement」的典型。

---

## 5. Idealized models：錯誤不是例外，而是方法

Stanford Encyclopedia of Philosophy 對 scientific models 的整理指出，idealization 會刻意簡化或扭曲複雜系統，使其更 tractable 或 understandable。

常見例子包括：

- frictionless plane；
- point mass；
- isolated system；
- perfectly rational agent；
- perfect equilibrium。

這些模型不按字面描述世界，卻是正常科學方法。

因此現代科學早已制度化承認：

$$
\text{literal fidelity}<1
$$

不必然使：

$$
\text{scientific utility}=0.
$$

---

## 6. Minimal models：少一點真實細節，可能多一點結構

Batterman 與 Rice 的 minimal model account 強調，某些模型的解釋力來自揭示不同系統之間的 universality，而不是最大限度重建每個微觀機制。

如果不同微觀系統都落入同一宏觀 class，增加所有細節可能反而遮蔽：

$$
\text{relevant invariant}.
$$

所以：

$$
\boxed{
\text{more detail}
\not\Rightarrow
\text{more explanation}.
}
$$

這與本系列的 semantic quotient 非常接近：研究系統必須知道哪些差異應保留，哪些只是對目標無關的自由度。

---

## 7. Effective theories：非最基本仍可最適用

Effective field theory 的核心特徵之一是明確承認尺度與適用域。它不必宣稱自己是最 fundamental 的最終理論，卻可以在特定 energy scale 提供非常有效的描述。

近期 productive idealization 與 EFT 哲學研究進一步把問題指向：

$$
\text{fundamentality},
\text{fidelity},
\text{understanding},
\text{utility}
$$

之間的非單調關係。

這使「最底層理論一定最適合所有研究任務」成為需要證明、而不是可以偷渡的前提。

---

## 8. 四種生產性機制

從上述案例，本文整理四種不同機制。

### M1：Local truth retention

父理論錯，但保留某些局部正確關係。

### M2：Discrepancy exposure

模型的失效位置本身暴露 missing mechanism。

### M3：Irrelevance stripping

理想化刪除對目標不重要的細節，使 invariant 更清楚。

### M4：Tool migration

舊框架中發展的數學、儀器、實驗設計遷移到新框架。

這四者都可能增加 descendant value，但邏輯機制不同。

---

## 9. AI 時代新增了什麼

歷史科學的 productive error 通常需要多年甚至數十年才能被重構。

AI 長程研究第一次可能讓我們保存：

$$
\text{generation}
+
\text{route}
+
\text{failure}
+
\text{revision}
+
\text{descendant transfer}
$$

的高密度縱向資料。

這意味著「錯誤如何生知識」可能從歷史重建問題，變成部分可觀測的 prospective science。

例如 LISDD 類方法已經把：

$$
\text{where model fails}
$$

轉成：

$$
\text{which symbolic mechanism is missing}.
$$

Proof-space observatory 則可以嘗試把：

$$
\text{where proof routes fail}
$$

轉成：

$$
\text{which obstruction family or representation assumption is shared}.
$$

---

## 10. 歷史案例不能證明 NS 或 P vs NP framing 錯

這是本文最重要的反濫用條款。

Carnot、phlogiston、ether 告訴我們：

$$
\exists P:
\neg V(P)
\land
R_S(P)>0.
$$

它們不告訴我們：

$$
\forall\text{ hard problem }Q,
\operatorname{Hard}(Q)
\Rightarrow
\operatorname{MisSpecified}(Q).
$$

因此科學史只能支持「可能性與機制」，不能替代對具體未解問題的數學分析。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $P_{\mathrm{caloric}}$ | caloric parent framework |
| $D_i$ | descendant structures |
| M1--M4 | 四種生產性機制 |
| $V(P)$ | parent validity |
| $R_S(P)$ | salvage ratio |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-07 至 09。  

**後續：** LSI-PSD-12。

---

## 結論

科學史最穩健的教訓不是「錯誤是好的」，而是：

$$
\boxed{
\text{Scientific fruitfulness and literal truth are not the same variable.}
}
$$

一個成熟的 AI 科學系統因此不能只保存最後勝出的理論；它也應保存被替代框架中仍可遷移的數學、實驗、工具與 failure structure。這正是 proof-space observatory 下一步的資料任務。

---

## 參考文獻

1. John D. Norton. *How Analogy Helped Create the New Science of Thermodynamics*. Synthese 200:269, 2022. DOI: 10.1007/s11229-022-03708-9.
2. American Chemical Society. *Joseph Priestley and the Discovery of Oxygen*. National Historic Chemical Landmark.
3. American Chemical Society. *The Chemical Revolution of Antoine-Laurent Lavoisier*. National Historic Chemical Landmark.
4. Rafael Ferraro. *From aether theory to Special Relativity*. arXiv:1302.6965, 2013.
5. Roman Frigg and Stephan Hartmann. *Models in Science*. Stanford Encyclopedia of Philosophy, current online edition, accessed 2026-08-17.
6. Robert W. Batterman and Collin C. Rice. *Minimal Model Explanations*. Philosophy of Science 81(3), 2014.
7. Karla Weingarten. *Productive Idealizations for Scientific Understanding*. PhilSci-Archive preprint, 2026.
8. Yifan Wang. *Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy*. arXiv:2606.23215, 2026.
