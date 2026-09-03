# RLMM-07：證據、反例、查詢與方法更新
## Evidence, Counterexamples, Inquiry, and Method Revision

**系列：Recursive Linguistic Metacognition Methodology（RLMM）／遞歸語言元認知方法論**  
**版本：v0.1**  
**日期：2026-08-20**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

RLMM 前六篇已建立語言元認知介面、認知操作可組合性、元認知算子、認知對象升階、方法論反身性，以及非單調遞歸與停止條件。然而，任何元認知系統若不能正確處理外部資訊，就仍可能在更高階層上重複同樣的錯誤：把更多資料當成更多證據、把反對意見當成反例、把同源資料當成獨立驗證、把查詢數量當成資訊品質，或只修改 belief 而不修改產生錯誤的 method。

本文提出 RLMM 的「證據—反例—查詢—更新循環（Evidence–Counterexample–Inquiry–Revision Loop）」作為方法論的外部資訊接口。本文區分 Data、Evidence、Independent Evidence、Counterevidence、Counterexample 與 Discriminative Query；並主張證據價值不應只由支持方向決定，而應由其對競爭模型的區分力、來源獨立性、可靠性、時效性與行動相關性共同決定。

本文進一步建立兩層更新機制：Belief Update 與 Method Update。當新資訊只改變某個命題的可信度時，應更新 belief；當相同類型的失敗在不同內容上反覆出現、或證據選擇規則本身造成系統性偏差時，則應把 method 升格為新的認知對象。由此，RLMM 不再將「更新」理解為單純修正答案，而是：

$$
\boxed{
\text{Update}
=
\text{Belief Revision}
+
\text{Method Revision}
+
\text{Meta-Revision when necessary}.
}
$$

本文最後提出第一版 Evidence Protocol、Counterexample Protocol、Inquiry Protocol 與 Update Gate，作為未來 RLMM Language Protocol、AI 認知建議與測試框架的直接基礎。

---

## 關鍵詞

RLMM；證據；反例；查詢；資訊價值；belief update；method update；獨立證據；元認知；方法修正

---

# 1. 問題：更多資料真的等於更多認知嗎？

一個很常見的錯誤是：

$$
\text{More Data}
\Rightarrow
\text{More Evidence}
\Rightarrow
\text{Better Cognition}.
$$

但這個推論並不成立。

十篇文章可能都來自同一則新聞。

十個 AI 回答可能都受同一訓練來源影響。

十條推理路徑可能共享同一個隱含前提。

因此：

$$
\boxed{
\text{Data Count}
\neq
\text{Evidence Count}.
}
$$

更進一步：

$$
\boxed{
\text{Evidence Count}
\neq
\text{Evidence Value}.
}
$$

RLMM 因此不能只教：

> 「多查一點。」

而必須回答：

> **下一個資料是否真的能增加可區分性？**

---

# 2. Data 與 Evidence 的區分

令：

$$
d
$$

表示一筆資料。

資料只有在相對某一個命題：

$$
H
$$

具有認知相關性時，才進入 evidence 層。

可寫成：

$$
E(d\mid H).
$$

因此：

$$
\boxed{
\text{Evidence}
=
\text{Data conditioned on a cognitive question}.
}
$$

同一筆資料：

$$
d
$$

對：

$$
H_1
$$

可能非常重要，

對：

$$
H_2
$$

可能完全無關。

所以證據不是資料自身的固定屬性。

---

# 3. 證據至少有五個維度

RLMM 建議把證據表示成：

$$
E_i
=
(
R_i,
I_i,
D_i,
T_i,
A_i
).
$$

其中：

- $R_i$：Reliability，可靠性；
- $I_i$：Independence，獨立性；
- $D_i$：Discriminative Power，區分力；
- $T_i$：Timeliness，時效性；
- $A_i$：Action Relevance，行動相關性。

因此：

$$
\boxed{
\text{Evidence Quality}
\text{ is multidimensional}.
}
$$

---

# 4. Reliability：來源可靠不等於結論必真

即使：

$$
P(\text{source reliable})\approx1,
$$

仍不能推出：

$$
P(H)\approx1.
$$

因為來源可能：

- 誤解；
- 資料過時；
- 方法不適用；
- 遭遇 distribution shift；
- 在新情境第一次失敗。

因此：

$$
\boxed{
\text{Source Trust}
\neq
\text{Truth Guarantee}.
}
$$

這與前面 SCL Case Corpus 中「trusted coalition betrayal」的結構一致。

---

# 5. Independence：真正獨立的證據

若：

$$
E_1,E_2,E_3
$$

表面來自三個來源，

但：

$$
Root(E_1)
=
Root(E_2)
=
Root(E_3),
$$

則它們不能被直接當作三份獨立證據。

因此可以定義：

$$
N_{\text{effective}}
\le
N_{\text{observed}}.
$$

真正重要的是：

$$
\boxed{
\text{Effective Evidence Count}.
}
$$

而不是表面來源數量。

---

# 6. Provenance Graph

為了判斷獨立性，RLMM 建議使用：

$$
G_P=(V,E)
$$

表示 provenance graph。

node：

$$
V
$$

可以是：

- 原始資料；
- 報導；
- 模型；
- 人類專家；
- API；
- 文件；
- 中介摘要。

edge：

$$
u\rightarrow v
$$

表示：

> $v$ 在資訊上依賴 $u$。

因此獨立性不是：

> 「網站不同。」

而是：

$$
\boxed{
\text{No dominant shared causal information root}.
}
$$

---

# 7. Discriminative Power：證據最重要的功能

若兩個假設：

$$
H_1,H_2
$$

都能解釋某資料：

$$
d,
$$

則：

$$
d
$$

可能資訊量很高，但區分力低。

真正有價值的 evidence 應該：

$$
P(d\mid H_1)
\neq
P(d\mid H_2).
$$

差異越大，通常越有區分價值。

因此：

$$
\boxed{
\text{Evidence value}
\approx
\text{ability to distinguish live hypotheses}.
}
$$

---

# 8. 支持證據與區分證據不是同一件事

很多認知流程會問：

> 有沒有更多支持我？

RLMM 更關心：

> 有沒有東西能區分我與最強替代模型？

假設：

$$
H_1
$$

已有十個支持例。

但：

$$
H_2
$$

也能解釋這十個例。

此時第十一個同類支持：

$$
E_{11}
$$

價值可能很低。

反而一個：

$$
d^*
$$

只在 $H_1$ 下合理，

在 $H_2$ 下不合理，

其價值更高。

---

# 9. Counterevidence 與 Counterexample

「反對」不等於「反例」。

RLMM 至少區分：

### Counterevidence

降低：

$$
P(H)
$$

的證據。

### Counterexample

若命題是普遍形式：

$$
\forall x,\ P(x),
$$

則只需要一個：

$$
x^*
$$

滿足：

$$
\neg P(x^*)
$$

即可破壞該普遍命題。

因此：

$$
\boxed{
\text{Counterexample}
\neq
\text{mere disagreement}.
}
$$

---

# 10. 反例的真正價值

好的反例不是：

> 找一個不同意我的人。

而是：

> 找一個在目前方法聲稱應成功的條件下，方法卻會失敗的最小案例。

因此可以定義：

$$
x^*
=
\arg\min_x
\operatorname{Complexity}(x)
$$

subject to：

$$
M(x)
\text{ fails}.
$$

這就是：

$$
\boxed{
\text{Minimal Discriminative Counterexample}.
}
$$

---

# 11. 最小反例與方法除錯

對方法：

$$
M
$$

而言，

若可以找到：

$$
x^*
$$

使：

$$
M(x^*)\neq Goal(x^*),
$$

那麼：

$$
x^*
$$

不只是錯誤例子。

它可能揭露：

- 邊界條件；
- 隱含假設；
- 接口錯誤；
- objective mismatch；
- stop rule failure。

因此：

$$
\boxed{
\text{Counterexample}
\rightarrow
\text{Method Diagnosis}.
}
$$

---

# 12. 反例也可能是假反例

需要避免：

$$
x^*
$$

根本不滿足方法的適用前提。

如果：

$$
x^*\notin D(M),
$$

那麼它不能證明：

$$
M
$$

在自己的定義域內失效。

因此：

$$
\boxed{
\text{Counterexample validity requires domain compatibility}.
}
$$

---

# 13. Challenge 不應變成反對成癮

若 RLMM 只教：

> 一定要找反例。

AI 可能形成：

$$
\boxed{
\text{Counterexample Addiction}.
}
$$

即：

- 對任何結論都強制反駁；
- 把小例外當成整體推翻；
- 忽視 base rate；
- 忽視適用域。

所以：

$$
\boxed{
\text{Challenge}
\neq
\text{Contrarianism}.
}
$$

---

# 14. Inquiry：查詢不是「問更多問題」

令：

$$
q
$$

是一個 query。

真正應選的不是：

$$
q_{\text{interesting}}
$$

而是：

$$
q^*
=
\arg\max_q
VOI(q).
$$

即：

$$
\boxed{
\text{Query Selection}
=
\text{Value-of-Information Selection}.
}
$$

---

# 15. Value of Information

簡化地說：

$$
VOI(q)
=
\mathbb E[
U(\text{after }q)
]
-
U(\text{before }q)
-
C(q).
$$

其中：

$$
C(q)
$$

包括：

- 搜尋成本；
- 延遲；
- 工具費用；
- 風險；
- 新複雜度。

若：

$$
VOI(q)\le0,
$$

則：

$$
\boxed{
\text{Do not query}.
}
$$

---

# 16. 查詢的目標應該是「區分」

最好的 query 通常不是：

> 找更多支持。

而是：

> 哪個觀測會讓 $H_1$ 與 $H_2$ 產生最大不同？

即：

$$
q^*
=
\arg\max_q
D
\left(
P(E_q\mid H_1),
P(E_q\mid H_2)
\right).
$$

這是：

$$
\boxed{
\text{Discriminative Inquiry}.
}
$$

---

# 17. Query 也有 provenance

若每個 query 都問同一工具：

$$
Q_1,Q_2,Q_3
$$

但全部底層依賴同一 dataset，

則：

$$
\boxed{
\text{Multiple Queries}
\neq
\text{Multiple Information Channels}.
}
$$

因此 query selection 也應考慮：

$$
\operatorname{ChannelIndependence}(q).
$$

---

# 18. 查詢成本與查詢深度

假設：

$$
q_1
$$

之後可以根據結果決定：

$$
q_2.
$$

那麼 inquiry 是一個策略：

$$
\pi_q
=
(q_1,q_2,\ldots).
$$

而不是單次查詢。

因此：

$$
\boxed{
\text{Inquiry}
=
\text{Adaptive Information Acquisition Policy}.
}
$$

---

# 19. 一步 VOI 的限制

只比較：

$$
\text{act now}
$$

與：

$$
\text{query once}
$$

可能錯過：

$$
q_1
\rightarrow
q_2
\rightarrow
\text{resolution}.
$$

因此：

$$
VOI_1
$$

不一定代表：

$$
VOI_H.
$$

這與先前 Case Corpus 中 one-step inquiry collapse 的結構一致。

---

# 20. 有限 horizon 查詢

更完整可以寫：

$$
\pi^*
=
\arg\max_{\pi}
\mathbb E
\left[
U_H(\pi)
-
\sum_{t=1}^{H}C(q_t)
\right].
$$

這讓查詢變成：

$$
\boxed{
\text{Information Planning}.
}
$$

而不是工具呼叫次數。

---

# 21. Belief Update

當新 evidence：

$$
E
$$

改變命題：

$$
H
$$

的可信度，

最基本的更新是：

$$
B_t(H)
\rightarrow
B_{t+1}(H).
$$

可抽象寫成：

$$
B_{t+1}
=
\mathcal U_B(B_t,E).
$$

這就是：

$$
\boxed{
\text{Belief Revision}.
}
$$

---

# 22. 但不是所有失敗都應更新 belief

如果：

$$
H
$$

錯了，

可能只是：

> 這次判斷錯。

但如果：

$$
H_1,H_2,H_3
$$

在不同內容上都因同一規則失敗，

那問題可能不是 individual belief。

而是：

$$
M.
$$

因此：

$$
\boxed{
\text{Repeated belief failure}
\rightarrow
\text{possible method failure}.
}
$$

---

# 23. Method Update

令：

$$
M_t
$$

為當前方法。

若 failure set：

$$
F_t
$$

具有共同結構：

$$
\operatorname{Pattern}(F_t)=p,
$$

則：

$$
M_{t+1}
=
\mathcal U_M(M_t,p).
$$

這就是：

$$
\boxed{
\text{Method Revision}.
}
$$

---

# 24. Belief Update 與 Method Update 的 Gate

可以建立：

### BG1 — Locality

失敗是否只出現在單一內容？

若是，優先 belief update。

### BG2 — Repetition

是否跨不同內容反覆出現？

若是，考慮 method update。

### BG3 — Structural Commonality

失敗是否共享：

- 同一 evidence rule；
- 同一 stop rule；
- 同一 trust rule；
- 同一 query rule？

若是，升階分析 method。

### BG4 — Environment Shift

方法以前有效，但環境改變？

若是，可能需要 context-conditioned method update。

---

# 25. Method Update 也可能過度

不能每次錯一次就重寫方法。

否則：

$$
M_0
\rightarrow
M_1
\rightarrow
M_2
\rightarrow\cdots
$$

造成：

$$
\boxed{
\text{Method Churn}.
}
$$

因此 method update 需要：

$$
\text{evidence of systematic failure}.
$$

---

# 26. Update Threshold

可以寫：

$$
P(
\text{systematic method failure}
\mid
F
)
>
\tau_M
$$

才進行 method update。

否則：

$$
\boxed{
\text{Keep method; revise local belief}.
}
$$

---

# 27. Meta-Update

如果：

$$
M_{t+1}
$$

反覆修正後仍出現新型失敗，

可能需要升到：

$$
\mathcal M(M).
$$

例如：

> 為什麼我們的 method update rule 每次都變得更保守？

此時問題已不是：

$$
M
$$

而是：

$$
\boxed{
\text{Method Revision Policy}.
}
$$

---

# 28. 更新不是覆寫

RLMM 建議：

$$
\boxed{
\text{Revision}
\neq
\text{Silent Overwrite}.
}
$$

應保留：

$$
B_t
\rightarrow
B_{t+1}
$$

以及：

$$
M_t
\rightarrow
M_{t+1}.
$$

並記錄：

- 什麼 evidence；
- 為什麼改；
- 哪個版本；
- 哪些 failure 觸發；
- 是否可 rollback。

---

# 29. Revision Ledger

可以建立：

$$
L_R
=
\{
r_1,r_2,\ldots
\}.
$$

每個 record：

$$
r_i
=
(
\text{object},
\text{old},
\text{new},
\text{evidence},
\text{reason},
\text{time},
\text{version}
).
$$

這是：

$$
\boxed{
\text{Metacognitive Revision Ledger}.
}
$$

---

# 30. Evidence 也可能被污染

需要考慮：

$$
E
$$

本身可能：

- 錯；
- stale；
- manipulated；
- adversarial；
- correlated；
- generated from previous artifact。

所以：

$$
\boxed{
\text{Evidence processing itself is a metacognitive object}.
}
$$

---

# 31. Evidence on Evidence

有時候需要：

$$
E(E).
$$

例如：

> 這個來源可靠嗎？

這是：

$$
\text{Evidence about evidence}.
$$

再往上一階：

> 我的可靠性判斷方法可靠嗎？

則進入：

$$
\mathcal M(E(E)).
$$

這與 RLMM-04 的 promotion 完全一致。

---

# 32. 但不能無限驗證 evidence

如果：

$$
E
\rightarrow
E(E)
\rightarrow
E(E(E))
\rightarrow\cdots
$$

就形成：

$$
\boxed{
\text{Evidence Recursion}.
}
$$

仍然必須服從：

$$
\Delta U>0
$$

與 STOP Gate。

---

# 33. 反例與 evidence 的不對稱性

對普遍命題：

$$
\forall x\,P(x)
$$

一個 counterexample 可以具有極高破壞力。

但對統計命題：

$$
P(P(x))=0.9,
$$

單一反例不一定重要。

所以：

$$
\boxed{
\text{Counterexample value depends on claim form}.
}
$$

不能把所有命題都當 deterministic universal claim。

---

# 34. Claim Type 應先被辨識

RLMM 建議先判斷命題屬於：

- universal；
- existential；
- probabilistic；
- causal；
- predictive；
- normative；
- procedural。

不同 claim type 對 evidence 的要求不同。

例如：

$$
\exists x\,P(x)
$$

只需一個成立例。

而：

$$
\forall x\,P(x)
$$

只需一個反例即可推翻。

---

# 35. Causal Evidence

若 claim 是：

$$
X\rightarrow Y,
$$

單純相關 evidence：

$$
Corr(X,Y)
$$

不等於因果 evidence。

需要額外：

- intervention；
- mechanism；
- temporal order；
- confound control。

因此：

$$
\boxed{
\text{Evidence validity is claim-type dependent}.
}
$$

---

# 36. Normative Claim 的特殊性

若問題是：

> 應該怎麼做？

那 evidence 不能直接推出 value。

因為：

$$
\text{Is}
\not\Rightarrow
\text{Ought}.
$$

需要額外：

$$
V
=
\text{value / objective structure}.
$$

因此：

$$
Decision
=
f(E,V,R,B).
$$

---

# 37. Evidence 與 Value 的分離

成熟 RLMM 必須區分：

$$
\boxed{
\text{What is true?}
}
$$

與：

$$
\boxed{
\text{What should be done?}
}
$$

前者主要由 evidence 更新。

後者還需要：

- values；
- risk；
- cost；
- policy；
- rights；
- constraints。

---

# 38. Inquiry 也必須服務原始目標

如果 original goal：

$$
G
$$

但 inquiry 不斷轉向：

$$
Q_1,Q_2,Q_3
$$

最後與 $G$ 無關，

就形成：

$$
\boxed{
\text{Inquiry Drift}.
}
$$

因此每次 query 都應問：

> 這個資訊真的會改變原始決策或方法嗎？

---

# 39. Decision-Relevance Gate

若：

$$
P(
\text{query result changes action}
)
\approx0,
$$

則 query 的實際價值通常很低。

所以：

$$
\boxed{
\text{Interesting information}
\neq
\text{decision-relevant information}.
}
$$

---

# 40. Evidence Compression

當 evidence 太多，

AI 需要摘要：

$$
E_1,\ldots,E_n
\rightarrow
\hat E.
$$

但摘要可能丟失：

- minority evidence；
- provenance；
- contradiction；
- uncertainty。

所以 evidence compression 也需要 invariants。

---

# 41. Evidence Invariants

壓縮 evidence 時至少保留：

- provenance diversity；
- strongest counterevidence；
- unresolved conflict；
- confidence；
- timestamp；
- claim linkage。

否則：

$$
\boxed{
\text{Compression}
\rightarrow
\text{epistemic distortion}.
}
$$

---

# 42. Case Corpus 的統一位置

過去案例可以重新分類為：

### Evidence Failure
同源資料被重複計數。

### Inquiry Failure
reactive query 太晚。

### Objective Failure
defer 被當成最便宜選項。

### Method Failure
升階後只增加 trigger，不改 action。

### Revision Failure
hard constraint 修掉 abstention，卻造成 over-rejection。

這些共同支持：

$$
\boxed{
\text{Evidence handling and method revision are inseparable}.
}
$$

---

# 43. 第一版 Evidence Protocol

### E1 — 先說明 claim

> 這份資料是要支持／反駁哪個命題？

### E2 — 查 provenance

> 它與其他證據是否共享主要來源？

### E3 — 查區分力

> 它能區分哪兩個仍存活的模型？

### E4 — 查時效性

> 它是否仍適用於當前時間／版本／環境？

### E5 — 查行動相關性

> 即使得到這份證據，決策會改變嗎？

---

# 44. 第一版 Counterexample Protocol

### C1 — 確認 claim type

這是 universal、probabilistic、causal 還是 procedural？

### C2 — 確認 domain

候選反例是否真的落在適用域？

### C3 — 尋找最小區分例

優先找能最清楚揭露失敗結構的案例。

### C4 — 不把 disagreement 當 counterexample

只有真正破壞 claim / method condition 的例子才算。

### C5 — 把反例回饋到 method

問：

> 這只是局部例外，還是方法規則本身錯？

---

# 45. 第一版 Inquiry Protocol

### Q1 — 列出 live hypotheses

不要對單一結論盲目搜尋。

### Q2 — 找最大區分 query

問：

> 哪個結果最能分開這些 hypotheses？

### Q3 — 查 channel independence

避免每個 query 都從同一來源得到答案。

### Q4 — 計算 VOI

若：

$$
VOI(q)\le0,
$$

停止。

### Q5 — 必要時做 multi-step inquiry

不要只用 one-step myopia。

---

# 46. 第一版 Update Gate

當新 evidence 到來時，依序問：

### U1 — 只改變這個 belief 嗎？

若是：

$$
\operatorname{BeliefUpdate}.
$$

### U2 — 同類 failure 是否跨案例重複？

若是：

$$
\operatorname{MethodInspection}.
$$

### U3 — 是否共享同一方法失敗根？

若是：

$$
\operatorname{MethodUpdate}.
$$

### U4 — Method update 是否又產生系統性副作用？

若是：

$$
\operatorname{MetaUpdate}.
$$

### U5 — 是否只是在追逐噪聲？

若是：

$$
\operatorname{STOP}.
$$

---

# 47. Belief–Method–Meta 三層更新

因此完整更新架構為：

$$
\boxed{
B_t
\rightarrow
B_{t+1}
}
$$

必要時：

$$
\boxed{
M_t
\rightarrow
M_{t+1}
}
$$

再必要時：

$$
\boxed{
\mathcal U_t
\rightarrow
\mathcal U_{t+1}
}
$$

其中：

$$
\mathcal U
$$

表示「如何更新方法」的規則。

這就是：

$$
\boxed{
\text{Recursive Revision}.
}
$$

---

# 48. 與 RLMM-04 的接合

RLMM-04 提出：

$$
\text{Repeated failure}
\rightarrow
\text{Promotion}.
$$

本文補上：

$$
\boxed{
\text{Evidence determines whether promotion is justified}.
}
$$

也就是：

> 不能只因為感覺方法有問題就升階。

需要 failure pattern 有足夠證據。

---

# 49. 與 RLMM-06 的接合

即使 inquiry 有價值，

也要服從：

$$
\Delta U>0.
$$

所以：

$$
\boxed{
\text{More evidence}
\not\Rightarrow
\text{more useful cognition}.
}
$$

如果：

- 查詢成本高；
- deadline 快到；
- 決策已不會改；
- 剩餘未知不可約；

就應停止。

---

# 50. 與 RLMM-05 的接合

反身 artifact 本身也是 evidence。

但它可能：

- 已知；
- 被過度重用；
- 改變環境；
- 成為對手已知策略。

因此：

$$
\boxed{
\text{Prior methodological knowledge}
\text{ is both evidence and intervention}.
}
$$

這使 evidence evaluation 必須帶 historical conditioning。

---

# 51. 未來 AI 學習的意義

如果 RLMM 被拿來當未來 AI 的學習材料，

最重要的不是讓 AI 記住：

> 「要找反例。」

而是讓 AI 學會：

1. 什麼叫有效反例；
2. 什麼時候反例有高資訊價值；
3. 什麼時候 query 應停止；
4. 什麼時候更新 belief；
5. 什麼時候升階更新 method；
6. 什麼時候 method update 本身也需要被檢查。

因此：

$$
\boxed{
\text{Metacognitive learning}
\neq
\text{rule memorization}.
}
$$

---

# 52. 邊界與非主張

本文不主張：

1. 所有 evidence quality 都能精確量化；
2. Bayesian update 是唯一合法 belief update；
3. 所有 claim 都可由 counterexample 處理；
4. 更多 provenance 一定表示更獨立；
5. VOI 可以被任何系統完美估計；
6. method update 越頻繁越好；
7. 所有 systematic failure 都來自 method；
8. 所有 query 都應服務立即決策；
9. evidence compression 可以無損；
10. RLMM 可以消除所有認知偏誤。

本文只提出：

$$
\boxed{
\text{Evidence should be evaluated by relevance, independence, discrimination, timeliness and action value; revision should target beliefs or methods according to the structure of observed failure.}
}
$$

---

# 53. 結論

RLMM 的元認知循環若要真正接觸世界，就必須經過：

$$
\boxed{
\text{Evidence}
\rightarrow
\text{Counterexample}
\rightarrow
\text{Inquiry}
\rightarrow
\text{Revision}.
}
$$

但這四個詞都不能被簡化。

真正重要的是：

$$
\boxed{
\text{Data}
\neq
\text{Evidence}
}
$$

$$
\boxed{
\text{Disagreement}
\neq
\text{Counterexample}
}
$$

$$
\boxed{
\text{More Queries}
\neq
\text{More Information}
}
$$

以及：

$$
\boxed{
\text{Belief Error}
\neq
\text{Method Error}.
}
$$

成熟系統必須知道：

> 什麼資訊值得取得？  
> 什麼反例真的能區分？  
> 哪些 evidence 其實同源？  
> 這次應修正答案，還是修正產生答案的方法？  
> 如果方法修正本身反覆失敗，是否應再升一階？

因此：

$$
\boxed{
\text{Update}
=
\text{Belief Revision}
+
\text{Method Revision}
+
\text{Meta-Revision when necessary}.
}
$$

這使 RLMM 從一套內部反思方法，正式接上外部世界、工具、證據與學習。

---

# 下一篇

**RLMM-08：多主體／多 AI 的共享元認知**  
**Shared Metacognition Across Multiple Agents**

下一篇將正式處理：當多個人類或 AI 各自具有不同觀察、不同記憶、不同方法與不同偏誤時，如何共享元認知而不把共識誤當真理；如何區分 shared state、shared method、shared evidence 與 shared error；以及如何利用 objection、correction、branch、merge 與 supersession 建立分散式元認知。
