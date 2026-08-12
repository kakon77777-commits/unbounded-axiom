# 基底知識空間擴張：AI 原生高品質資料生成的結構閉包假說

**English Title:** Base Knowledge Space Expansion: A Structural-Closure Hypothesis for AI-Native High-Quality Data Generation  
**Series:** AI-Native Knowledge Expansion, Paper I  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-09

## 摘要

大型語言模型的數學能力通常被討論為模型規模、推理架構、強化學習、難題資料與形式化證明資料的函數。然而，「高品質資料」經常被不自覺地等同於「高難度資料」、「前沿研究資料」或「由專家撰寫的稀缺資料」。本文提出不同的假說：**深度不要求每一個資料點本身都很深；只要可靠的基礎知識能被大量、合法、可驗證地展開，其結構閉包本身就可能形成高價值推理資料。**

本文將此機制定義為「基底知識空間擴張」（Base Knowledge Space Expansion, BKSE）。對一個可靠基礎命題 \(P\)，不僅保存其單一敘述，而是建立由等價變換、逆向問題、條件消融、表示轉換、跨模組組合、反例鄰域、維度提升與形式驗證所形成的結構鄰域 \(\mathcal E(P)\)。資料品質因而不只由難度衡量，而應由正確性、結構變異、覆蓋密度、推導深度、可驗證性、去重程度與錯誤可檢出性共同決定。

本文進一步提出：AI 原生數學的早期突破未必首先來自更難的數學，而可能來自人類不願長期承受的大規模「認知重複」——對基礎命題反覆證明、反駁、重組、形式化與交叉驗證。這種高密度驗證與結構展開，可同時服務於資料生成、模型訓練、推理穩定性、形式化數學與自主研究系統。本文最後提出可被實驗否證的 BKSE 訓練與評測框架，並界定其與一般資料增強、表面改寫及純粹難題合成的差異。

**關鍵詞：** 基底知識空間；AI 原生數學；合成資料；形式化證明；結構閉包；資料品質；定理證明器；自動形式化；知識覆蓋；驗證密度

---

## 1. 問題：我們真的缺「更難的資料」嗎？

當代 AI 數學研究有一個合理但容易過度延伸的直覺：若希望模型變得更強，就應提供更難、更專業、更接近數學前沿的資料。這條路當然重要，但它隱含了一個未必成立的等價：

\[
\text{High-quality data}
\overset{?}{=}
\text{Difficult data}.
\]

本文否定這個等價。

一個資料點的「難度」只是資料品質的一個維度。對推理系統而言，同樣重要的還包括：

\[
Q(d)
=
f(
C,
V,
D,
R,
L,
E,
G
),
\]

其中：

- \(C\)：correctness，正確性；
- \(V\)：structural variation，結構變異；
- \(D\)：derivational depth，推導深度；
- \(R\)：reusability，可重用性；
- \(L\)：linkage，跨知識連接程度；
- \(E\)：error detectability，錯誤可檢出性；
- \(G\)：granularity，知識粒度。

因此，一個非常基礎的定理，只要能形成高密度、高變異、低錯誤的推理網路，也可能比一篇孤立而困難的自然語言論文提供更高的有效訓練價值。

本文的核心命題是：

\[
\boxed{
\text{Deep intelligence does not require every datum to be deep.}
}
\]

更強地說：

\[
\boxed{
\text{A sufficiently rich verified closure of reliable basics may itself become deep.}
}
\]

即：

> 深度不一定來自每一個資料點本身都很深；可靠基礎經過足夠豐富、可驗證的展開與組合，其閉包本身就可能產生深度。

---

## 2. 原始資料量與有效結構量不是同一個量

人類已經產生極大量的數學自然語言：教材、論文、題庫、講義、論壇回答、證明、翻譯、重述與評論。但「文字很多」不代表其中包含同等數量的獨立數學結構。

設原始資料集合為：

\[
D_{\mathrm{raw}}.
\]

若定義等價關係：

\[
x_i\sim x_j
\]

表示兩個樣本雖然字面不同，但承載近似相同的核心結構，則真正值得關心的數量不是：

\[
|D_{\mathrm{raw}}|,
\]

而是某種近似的結構商空間：

\[
\left|D_{\mathrm{raw}}/\sim\right|.
\]

自然語言具有極高的「表示重數」。同一個定理可能被不同語言、不同教材、不同例子與不同敘述方式重複數萬次，但完整、可機械檢查、可追溯依賴的形式證明數量可能非常有限。

形式數學的現況支持這種「表面龐大、形式結構仍稀疏」的判斷。Mathlib 已是目前規模最大的形式數學庫之一，包含超過兩百萬行形式化內容，並強調定義、定理與證明的可組合重用；然而，自動形式化研究仍普遍將高品質形式資料不足視為核心瓶頸。2025–2026 年的研究甚至仍以數千道自然語言題轉換為 Lean、或把整本教材轉成形式內容，作為重要的資料與工程進展。

因此本文不主張「世界上的數學很少」，而是提出更窄的命題：

\[
\boxed{
\text{Verified structural coverage}
\ll
\text{natural-language repetition}.
}
\]

---

## 3. 基底知識空間擴張（BKSE）

令：

\[
B_0=\{P_1,P_2,\ldots,P_n\}
\]

為一組已知可靠的基礎命題。

對每個命題 \(P\)，定義一組合法轉換算子：

\[
\mathcal T
=
\{
T_{\mathrm{eq}},
T_{\mathrm{inv}},
T_{\mathrm{repr}},
T_{\mathrm{cond}},
T_{\mathrm{gen}},
T_{\mathrm{spec}},
T_{\mathrm{counter}},
T_{\mathrm{compose}}
\}.
\]

分別代表：

1. 等價變換；
2. 逆向／逆命題；
3. 表示語言轉換；
4. 條件增加、移除與消融；
5. 泛化；
6. 特化；
7. 反例與近錯誤生成；
8. 與其他命題組合。

第一階擴張為：

\[
B_1
=
B_0
\cup
\{
T(P):
P\in B_0,\,
T\in\mathcal T
\}.
\]

再允許跨命題組合：

\[
B_{k+1}
=
B_k
\cup
\{T(P)\}
\cup
\{C(P,Q):P,Q\in B_k\}.
\]

理想化閉包：

\[
\boxed{
B^\ast
=
\bigcup_{k=0}^{\infty} B_k.
}
\]

本文不主張實際系統應窮舉 \(B^\ast\)。相反，這個定義只是指出：一個看似簡單的基礎命題周圍，可能存在遠大於其原始敘述的合法結構鄰域。

因此對單一命題 \(P\)，定義：

\[
\boxed{
\mathcal E(P)
=
\{\text{legal verified neighbors of }P\}.
}
\]

BKSE 的目標不是產生最多樣本，而是提高：

\[
\text{coverage}\bigl(\mathcal E(P)\bigr).
\]

---

## 4. 變異不等於多樣性

最簡單的資料增強很容易退化成：

\[
3,4,5
\rightarrow
6,8,10
\rightarrow
9,12,15.
\]

這增加樣本數，卻不一定增加結構資訊。

因此：

\[
\boxed{
\text{Variation}\neq\text{Diversity}.
}
\]

真正的結構變異應至少改變一項：

- 推理方向；
- 隱藏資訊位置；
- 前提集合；
- 表示系統；
- 所需中間引理；
- 組合模組；
- 可用工具；
- 反例結構；
- 維度；
- 證明路徑。

以畢氏定理為例：

\[
a^2+b^2=c^2
\]

可以生成的不只是不同邊長，而包括：

- 已知兩股求斜邊；
- 已知斜邊與一股反求另一股；
- 逆定理判斷直角；
- 銳角／直角／鈍角分類；
- 相似三角形證明；
- 面積重排證明；
- 內積空間表示；
- 座標表示；
- 三維正交距離；
- 高維正交分解；
- 與圓、投影、高、內切圓、外接圓組合；
- 條件消融；
- 錯誤命題與最小反例。

同一個母命題因此可以形成「局部理論生態」，而不是一列換數字的題目。

---

## 5. 錯誤鄰域也是高品質資料

若只生成正確變種，模型學到的可能只是：

> 什麼時候可以推出答案。

但強推理還需要：

> 什麼時候不可以推出。

因此對命題 \(P\)，定義錯誤鄰域：

\[
N^-(P)
=
\{
P'_1,P'_2,\ldots
\},
\]

其中每個 \(P'_i\) 都與 \(P\) 結構接近，但至少存在一個關鍵錯誤：

- 缺少必要條件；
- 將充分條件誤當必要條件；
- 量詞錯置；
- 定義域擴張過頭；
- 符號相似但對象不同；
- 合法推導中插入一個非法步驟；
- 把有限驗證誤當全稱證明。

因此高品質訓練單元不應只有：

\[
(P,\text{proof}),
\]

而更接近：

\[
\boxed{
(
P,
\text{proof},
\text{assumptions},
\text{counterexamples},
\text{near-misses},
\text{equivalents},
\text{dependencies}
).
}
\]

這使「錯誤可檢出性」本身成為資料品質的一部分。

---

## 6. 驗證器使大規模展開成為可能

BKSE 若沒有驗證，只會快速變成合成垃圾資料。

因此核心不是：

\[
\text{Generate}.
\]

而是：

\[
\boxed{
\text{Generate}
+
\text{Verify}.
}
\]

至少可建立多層驗證：

\[
V
=
(
V_{\mathrm{parse}},
V_{\mathrm{type}},
V_{\mathrm{symbolic}},
V_{\mathrm{formal}},
V_{\mathrm{numeric}},
V_{\mathrm{counter}},
V_{\mathrm{cross}}
).
\]

其中：

1. 語法／解析驗證；
2. 型別與定義域驗證；
3. 符號代數驗證；
4. theorem prover 形式證明；
5. 數值測試；
6. 反例搜尋；
7. 獨立證明或跨驗證器檢查。

近期研究已經顯示，定理證明器可被用作合成數學資料的判定器；也有工作透過 proof-state exploration 大量生成訓練資料，提高自動定理證明表現。這些結果支持「生成—驗證閉環」的工程可行性，但本文將其研究對象向更基礎處擴張：不是只對難題或既有 benchmark 生成證明資料，而是有系統地擴張整個基礎知識鄰域。

---

## 7. AI 的特殊優勢：驗證密度而不只是智力

人類研究者必須分配注意力。

設理論圖：

\[
G=(V,E)
\]

包含大量局部推理節點。人類通常只能詳細檢查：

\[
S_H\subset V.
\]

AI 系統則可以在資源允許時逼近：

\[
S_{AI}\approx V,
\]

並且對每個節點執行多種操作：

\[
v_i
\rightarrow
\{
\text{prove},
\text{disprove},
\text{formalize},
\text{rederive},
\text{perturb},
\text{test}
\}.
\]

因此 AI 的一項重要研究優勢可定義為：

\[
\boxed{
\text{Verification Density}.
}
\]

這不是聲稱 AI 永遠比人類聰明，而是指出兩者成本函數不同。人類會合理地覺得第 10,000 個微小邊界條件「不值得再查」；自動系統則可以將這類工作制度化。

由此可提出：

> AI 原生數學未必首先來自更高的智力，也可能先來自對大規模、反覆、精細甚至令人類嫌煩的邏輯清理工作的極高耐受性。

---

## 8. 有效結構資料量

傳統資料集主要以：

- token 數；
- 文件數；
- 題目數；
- proof 數；

衡量規模。

本文提出一個概念性指標：

\[
\boxed{
E(D)
=
\sum_{s\in\mathcal S}
w(s)
C(s)
V(s)
R(s)
}
\]

其中：

- \(s\)：近似獨立結構；
- \(C(s)\)：結構覆蓋；
- \(V(s)\)：有效變異；
- \(R(s)\)：驗證可靠性；
- \(w(s)\)：資訊或任務權重。

稱：

\[
E(D)
=
\text{Effective Structural Dataset Size}.
\]

因此：

\[
|D_1|>|D_2|
\]

不必然表示：

\[
E(D_1)>E(D_2).
\]

一個包含大量自然語言近義重複的巨大 corpus，其有效結構量可能小於一個規模較小、但包含高密度形式變種、反例與證明依賴的資料集。

此量目前只是理論指標，不是已建立的標準 metric。後續必須研究如何近似估計結構等價、覆蓋與驗證可靠性。

---

## 9. BKSE 與一般 synthetic data 的差別

BKSE 不等於普通合成資料。

普通流程常為：

\[
P
\rightarrow
\text{LLM generates }P'_1,\ldots,P'_n.
\]

BKSE 則要求：

\[
\boxed{
\text{Invariant}
+
\text{Transformation}
+
\text{Verification}.
}
\]

每個生成物至少必須回答：

1. 哪個核心結構被保留？
2. 哪個結構被改變？
3. 此轉換是否合法？
4. 新命題與母命題是等價、強化、弱化、特化、泛化，還是分叉？
5. 如何驗證？
6. 是否與資料庫既有節點重複？
7. 是否產生新的可研究鄰域？

因此一個 BKSE 節點更適合表示成：

```text
claim_id
parent_ids
transformation
assumptions
statement
proof
verification
counterexamples
equivalence_class
novelty_status
frontier
```

它首先是一個機器可操作的研究節點，而不只是問答對。

---

## 10. AI-Native Research Loop

BKSE 可以自然形成自主研究循環：

\[
P_0
\rightarrow
\operatorname{Expand}
\rightarrow
\operatorname{Attack}
\rightarrow
\operatorname{Verify}
\rightarrow
\operatorname{Deduplicate}
\rightarrow
\operatorname{Select}
\rightarrow
P_1.
\]

其中 Select 不應只按「難度」排序，而應同時考慮：

\[
J
=
\lambda_1 N
+
\lambda_2 C
+
\lambda_3 V
-
\lambda_4 R_d
-
\lambda_5 C_e,
\]

其中可分別表示：

- \(N\)：novelty；
- \(C\)：coverage gain；
- \(V\)：verification value；
- \(R_d\)：redundancy；
- \(C_e\)：compute cost。

這可以避免組合爆炸。

如果沒有選擇器：

\[
|B_k|
\]

會快速失控；因此 BKSE 的核心工程問題不是「能不能生成很多」，而是：

\[
\boxed{
\text{Which frontier is worth expanding next?}
}
\]

---

## 11. 可否證的實驗設計

本文提出一個最小實驗。

### 11.1 基礎資料集

選擇 100–500 個中學到大學基礎命題，例如：

- 代數恆等式；
- 初等數論；
- 歐氏幾何；
- 基礎組合；
- 微積分基本命題；
- 線性代數基本命題。

### 11.2 三組資料

**Group A：Raw Repetition**

只收集大量自然語言教材、解釋與重述。

**Group B：Hard-Problem Expansion**

主要加入競賽／高難度題。

**Group C：BKSE**

對同一基礎命題做：

- 結構變種；
- 條件消融；
- 多證法；
- 反例；
- 錯誤鄰域；
- Lean／其他形式驗證；
- 等價類去重；
- 跨命題組合。

控制 token budget：

\[
|D_A|
\approx
|D_B|
\approx
|D_C|.
\]

### 11.3 評測

測量：

1. 未見過的結構變種；
2. 長鏈推理正確率；
3. 必要／充分條件辨識；
4. 反例搜尋能力；
5. proof repair；
6. autoformalization；
7. theorem proving；
8. 對錯誤前提的拒絕能力；
9. 跨表示轉換；
10. OOD 組合能力。

核心假說：

\[
\boxed{
\operatorname{Perf}(D_C)
>
\operatorname{Perf}(D_A)
}
\]

並且在某些任務上：

\[
\operatorname{Perf}(D_C)
\ge
\operatorname{Perf}(D_B),
\]

即使 BKSE 的原始母命題難度較低。

若結果不成立，BKSE 的強版本即被削弱。

---

## 12. 研究邊界

本文不主張：

1. 基礎資料可以取代前沿數學；
2. 所有知識都可無損形式化；
3. 合成資料必然優於人類資料；
4. 數值測試等同一般數學證明；
5. 形式證明器永遠無錯；
6. 只要生成足夠多變種就會自動產生新數學；
7. 結構等價可以在任意程式或任意語義系統中完美判定；
8. 一個形式系統的驗證等同跨所有公理系統的真理；
9. BKSE 已經是一個完成的訓練演算法。

本文只提出一個較窄的研究假說：

\[
\boxed{
\text{Reliable basics have underexploited structural neighborhoods.}
}
\]

而 AI、形式工具與自動驗證，使得大規模探索這些鄰域第一次變得具有實際工程可能性。

---

## 13. 與現有研究的關係

近年的研究已經提供若干重要拼圖：

- Mathlib 顯示大規模形式知識庫可以形成高度可組合、可重用的數學基礎；
- autoformalization 研究正試圖把大量非形式數學轉換成可驗證形式；
- FormaRL 等工作直接指出形式化資料稀缺，並嘗試利用 compiler / consistency feedback 在少量標註甚至無標註條件下改進形式化；
- Theorem Prover as a Judge 將 theorem prover 用作合成資料的嚴格判定器；
- proof-state synthetic data 工作則顯示，擴張中間證明狀態本身可以提高自動定理證明能力；
- Formal Conjectures 類專案則顯示，甚至「只有形式化命題、尚無證明」的研究節點本身也可以成為獨立資源。

BKSE 與這些工作的差別在於研究單位。

現有工作通常從：

\[
\text{problem}
\rightarrow
\text{formalize / solve / synthesize proof data}
\]

出發。

BKSE 則從：

\[
\text{reliable knowledge atom}
\rightarrow
\text{verified structural neighborhood}
\]

出發。

它研究的不是單一答案，而是知識原子周圍可被系統探索的閉包。

---

## 14. 結論

人類已經產生大量數學文字，但我們尚不能因此推論，人類已經充分探索了基礎數學知識的可驗證結構鄰域。

同一個基礎命題可以被：

\[
\text{證明}
\rightarrow
\text{逆向}
\rightarrow
\text{消融}
\rightarrow
\text{反駁}
\rightarrow
\text{泛化}
\rightarrow
\text{重組}
\rightarrow
\text{形式化}
\rightarrow
\text{交叉驗證}.
\]

這些操作產生的並非單純重複，而可能形成高密度的推理結構。

因此本文提出：

\[
\boxed{
\text{High-quality data}
\neq
\text{hard data only}.
}
\]

以及：

\[
\boxed{
\text{High-quality AI reasoning data}
\supset
\text{verified structural expansion of reliable basics}.
}
\]

如果此假說成立，AI 原生數學的第一階段不必等待 AI 自己解出最難的未解問題。它可以先完成一項人類從未大規模完成的工作：

> 對已知可靠知識進行近乎工業化的展開、反駁、重組、形式化、去重與交叉驗證。

這種工作看似基礎、重複，甚至令人類感到無聊；但正因為如此，它可能是最適合 AI 的研究生產層之一。

下一篇將進一步處理本系列的第二個核心問題：

\[
\boxed{
\text{What counts as a genuinely different variation?}
}
\]

亦即：如何區分表面改寫、參數替換、結構變種與真正的新命題，並建立可計算的「結構覆蓋」與「變種合法性」框架。

---

## 參考文獻（初版）

1. Lean Community. *Mathlib: A Foundation for Formal Mathematics Research and Verification*. Lean.
2. Weng, K. et al. (2025). *Autoformalization in the Era of Large Language Models: A Survey*. arXiv:2505.23486.
3. Huang, Y. et al. (2025). *FormaRL: Enhancing Autoformalization with no Labeled Data*. arXiv:2508.18914.
4. Leang, J. O. J. et al. (2025). *Theorem Prover as a Judge for Synthetic Data Generation*. arXiv:2502.13137.
5. Lai, J. et al. (2025). *LLM-based Automated Theorem Proving Hinges on Scalable Synthetic Data Generation*. arXiv:2505.12031.
6. Xie, J. et al. (2025). *FMC: Formalization of Natural Language Mathematical Competition Problems*. arXiv:2507.11275.
7. Google DeepMind. *Formal Conjectures: A Collection of Formalised Statements of Conjectures in Lean*.
