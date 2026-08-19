# LSI-PSD-08 — 生產性錯置：錯誤問題如何生成可存活的後代理論

## Productive Mis-specification: How a Flawed Parent Problem Can Generate Surviving Descendant Knowledge

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 08  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Productive Mis-specification Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文提出「生產性錯置」作為一個可檢驗的方法論概念，不主張錯誤問題、錯誤定義、錯誤模型或錯誤形式化本身具有真理地位，也不主張科學應故意採用錯誤前提。本文特別區分 deliberate idealization、model misspecification、formalization defect、scope mismatch、category/framing anomaly 與單純 hallucination。本文亦不主張 Navier--Stokes、P/NP 或任何既有未解問題已被證明存在範疇錯置；AI 長期未能證明一個命題，只能作為搜尋制度的觀察資料，不能直接判決原問題有誤。

---

## 摘要

一個研究問題若最後被證明具有錯誤假設、錯誤尺度、錯誤形式化、錯誤範疇或不適切的問題切割，其整個研究歷史是否因此歸零？科學史與現代模型科學都顯示，答案不必然是肯定的。錯誤的 parent framework 可以產生正確的 observation、可重用的 mathematics、有效的 experimental technique、可轉移的 correction term、可驗證的 local theorem 與後來在不同 framing 下仍能成立的 descendant knowledge。這種現象不能被粗糙地總結為「錯誤也有價值」，因為任意錯誤同樣可以產生大量自洽但無效的後代。真正需要的是一套可區分：

$$
\text{productive mis-specification}
$$

與：

$$
\text{error amplification}
$$

的方法論。

本文在 LSI-PSD-07 的 Truth–Generativity Separation 基礎上，正式定義 parent object：

$$
P
=
(Q,D,A,L,M,R),
$$

其中 $Q$ 為問題陳述， $D$ 為 domain， $A$ 為 assumptions， $L$ 為表示語言， $M$ 為方法／模型結構， $R$ 為搜尋制度。若後續 audit 發現存在修正算子：

$$
\mathcal C(P)=P',
$$

使原 parent 的某一部分被弱化、替換、重新定位或否定，則定義 parent revision distance：

$$
\delta_P
=
d(P,P').
$$

研究歷史中由 $P$ 生成的後代集合為：

$$
\mathcal D(P)
=
\{d_1,\ldots,d_n\}.
$$

對每個 descendant $d_i$，在 parent 修正後重新進行 independent audit。若：

$$
d_i
$$

不依賴已被撤銷的錯誤部分，或可以經有限 translation／repair 在新 parent $P'$ 中保持有效，則稱其為 survivor descendant。

本文定義 descendant survival ratio：

$$
S_D(P\rightarrow P')
=
\frac{
\sum_i w_i\,\mathbf 1[d_i\text{ survives}]
}{
\sum_i w_i
},
$$

以及更嚴格的 epistemic fertility：

$$
\Phi_E(P)
=
G_A(P)
\cdot
S_D(P)
\cdot
R_D(P)
\cdot
T_D(P),
$$

其中 $G_A$ 為 audited generativity、 $R_D$ 為後代穩健性、 $T_D$ 為 transferability。生產性錯置不是「parent 錯但輸出很多」，而是：

$$
\boxed{
\text{parent revision}
+
\text{non-zero descendant survival}
+
\text{independent audit}
+
\text{truth-sensitive correction}.
}
$$

本文進一步建立六類 mis-specification：

1. deliberate idealization；
2. model-form misspecification；
3. scope／regime mismatch；
4. specification／formalization mismatch；
5. category／framing mismatch candidate；
6. arbitrary error／hallucination。

其中前五類都可能在特定條件下具有生產性，第六類通常只造成 error propagation。

現代研究提供了直接相鄰的工程實例。2026 年 LISDD 將物理模型的局部失效定位到特定 operating regime，再以稀疏符號形式發現缺失機制，顯示 model discrepancy 可以被轉換為新機制發現；同年的 physics-guided operator correction 與 missing-physics symbolic regression 工作，也把已知物理與 residual correction 明確分離，而不是把整個 parent model 丟棄。另一方面，2026 年 Lean benchmark audit 在多個 machine-checked theorem benchmark 中辨識出 counterexample、vacuity、unsound axiom、missing hypothesis、translation error 與 specification hazard，證明「形式 proof 成功」與「原 intended problem 被忠實表示」是不同層次。這些案例共同支持：**parent representation 或 model 可能有缺陷，而其中某些 local derivations、proof objects、diagnostics 或 correction mechanisms 仍可被保存。**

本文亦重新檢視 Carnot、phlogiston、ideal gas 與 effective-theory 類案例。這些案例不能簡化成「錯理論導致真理」，更合理的描述是：

$$
\text{flawed parent constraint}
\rightarrow
\text{structured research trajectory}
\rightarrow
\text{descendant separation}
\rightarrow
\text{selective survival}.
$$

本文最後將此框架接回 AI 長程數學研究。對 NS-203 這類 corpus，若未來某個 proof family 被證明基於不適切 assumption 或 representation，正確做法不是刪除整個 corpus，而是逐項重驗：

$$
\text{lemma},
\text{obstruction},
\text{counterexample},
\text{tool},
\text{transfer},
\text{negative result}.
$$

只有經過 post-revision descendant audit，才能知道哪些研究資產真正存活。

本文最終提出：

$$
\boxed{
\textbf{A parent problem can fail without annihilating all of its descendants.}
}
$$

但同時堅持：

$$
\boxed{
\textbf{Descendant productivity never retroactively makes the flawed parent true.}
}
$$

**關鍵詞：** 生產性錯置、productive mis-specification、descendant survival、parent revision、error inheritance、idealization、model discrepancy、formalization mismatch、category error、scientific models、AI mathematics、proof-space dynamics

---

# 1. 問題的提出：研究母體錯了，後面的東西都要丟掉嗎？

## 1.1 二元評價的誘惑

最簡單的研究評價是：

$$
P=
\begin{cases}
\text{correct},\\
\text{incorrect}.
\end{cases}
$$

若 parent：

$$
P
$$

最後被判：

$$
\operatorname{Incorrect}(P),
$$

直覺上容易推出：

$$
\forall d\in\mathcal D(P),
\quad
\operatorname{Invalid}(d).
$$

但這個推論一般不成立。

## 1.2 Parent 和 descendant 不是同一命題

一個 parent theory：

$$
P
$$

通常包含：

$$
P
=
(A_1,A_2,\ldots,A_m,M,Q).
$$

一個 descendant theorem：

$$
d_i
$$

只依賴其中部分：

$$
A(d_i)
\subseteq
\{A_1,\ldots,A_m\}.
$$

如果 parent 失敗來自：

$$
A_m,
$$

但：

$$
A_m\notin A(d_i),
$$

那麼 $d_i$ 不必一起失敗。

## 1.3 研究歷史需要 dependency-aware revision

所以 parent revision 後，不能做：

$$
\mathcal D(P)\rightarrow\varnothing.
$$

更合理是：

$$
\boxed{
\mathcal D(P)
\rightarrow
\operatorname{Audit}_{P\rightarrow P'}
(
\mathcal D(P)
).
}
$$

---

# 2. Parent object 的正式表示

本文定義研究母體：

$$
P
=
(
Q,D,A,L,M,R,H
),
$$

其中：

- $Q$：question / proposition；
- $D$：domain；
- $A$：assumptions；
- $L$：language / representation；
- $M$：model / method family；
- $R$：research regime；
- $H$：research history。

這個表示刻意比單一 theorem statement 更寬。

因為「錯置」可能發生在不同層。

---

# 3. 六種錯置不能混為一談

## 3.1 Deliberate Idealization

研究者明知：

$$
A_{\mathrm{ideal}}
$$

不字面成立，

但在指定 regime 中使用。

例如：

$$
\text{friction}=0.
$$

這不是疏忽。

是有目的的簡化。

## 3.2 Model-Form Misspecification

研究者原本相信：

$$
M
$$

足以描述系統，

後來 residual 顯示：

$$
M
$$

缺少某個 mechanism。

## 3.3 Scope / Regime Mismatch

模型在：

$$
D_1
$$

有效，

卻被錯用到：

$$
D_2.
$$

模型本身未必錯，

錯在適用範圍。

## 3.4 Specification / Formalization Mismatch

informal target：

$$
Q_I
$$

被形式化成：

$$
Q_F
$$

但：

$$
Q_I\not\equiv Q_F.
$$

這是 formal AI mathematics 特別重要的錯置。

## 3.5 Category / Framing Mismatch Candidate

問題本身可能把不同類型的對象、量詞、尺度或 truth criterion 混到同一判定域。

本文只稱：

$$
\boxed{
\text{candidate}
}
$$

除非有額外形式證據。

## 3.6 Arbitrary Error / Hallucination

沒有可校準結構、

沒有穩定對應、

沒有可驗證後代。

這不應被美化成 productive mis-specification。

---

# 4. 修正算子

若 audit 發現 parent 需要修正，

定義：

$$
\mathcal C:
P\mapsto P'.
$$

修正可以是：

- remove assumption；
- add missing assumption；
- change domain；
- weaken conclusion；
- strengthen premise；
- change representation；
- split problem；
- merge equivalent problems；
- replace mechanism；
- correct formalization。

---

# 5. Parent revision distance

## 5.1 定義

$$
\delta_P
=
d(P,P').
$$

這不是單純文本 edit distance。

## 5.2 分量

可寫：

$$
\delta_P
=
(
\delta_Q,
\delta_D,
\delta_A,
\delta_L,
\delta_M
).
$$

## 5.3 小修和大修

若：

$$
\delta_P\ll1,
$$

可能只是：

- typo；
- missing premise；
- normalization。

若：

$$
\delta_P\gg1,
$$

可能是：

- ontology replacement；
- domain replacement；
- theorem statement collapse。

---

# 6. Descendant object

由 parent $P$ 產生：

$$
d_i
=
(
C_i,
A_i,
\Pi_i,
V_i,
T_i
),
$$

其中：

- $C_i$：claim；
- $A_i$：dependencies；
- $\Pi_i$：derivation / proof；
- $V_i$：verification status；
- $T_i$：transfer status。

---

# 7. Descendant dependency

建立：

$$
A_i
\subseteq
A_P.
$$

如果 parent 被修掉部分：

$$
A_P^{-},
$$

那麼：

$$
A_i\cap A_P^{-}
$$

決定 descendant 的直接風險。

## 7.1 Error exposure

定義：

$$
E_i
=
\frac{
|A_i\cap A_P^{-}|
}{
|A_i|
}.
$$

越高：

$$
E_i,
$$

越可能需要重證。

---

# 8. Descendant survival

## 8.1 強存活

在新 parent $P'$ 下：

$$
P'\vdash d_i.
$$

## 8.2 可修復存活

存在有限 repair：

$$
\mathcal R_i(d_i)=d_i'
$$

且：

$$
P'\vdash d_i'.
$$

## 8.3 失敗

若：

$$
P'\vdash\neg d_i
$$

或形式 counterexample 存在，

則：

$$
d_i
$$

不存活。

## 8.4 未知

若無法判定，

狀態必須保留：

$$
\text{unknown}.
$$

---

# 9. Survival state 不應只用二值

定義：

$$
\sigma_i
\in
\{
\text{strong},
\text{repairable},
\text{transferred},
\text{refuted},
\text{unknown}
\}.
$$

這比：

$$
0/1
$$

更適合研究史。

---

# 10. Descendant survival ratio

給每個 descendant 權重：

$$
w_i.
$$

定義：

$$
S_D(P\rightarrow P')
=
\frac{
\sum_i w_i\,s_i
}{
\sum_i w_i
},
$$

其中：

$$
s_i=
\begin{cases}
1,&\text{strong survival},\\
\alpha,&\text{repairable},\\
\beta,&\text{transferred},\\
0,&\text{refuted},\\
\text{excluded},&\text{unknown}.
\end{cases}
$$

---

# 11. 為什麼 unknown 不應硬算零

如果：

$$
\text{unknown}=0,
$$

會把尚未驗證誤當成失敗。

所以應分別報：

$$
S_D^{\mathrm{verified}}
$$

與 coverage：

$$
C_D
=
\frac{
N_{\mathrm{audited}}
}{
N_{\mathrm{descendants}}
}.
$$

---

# 12. Productive mis-specification 的最小定義

本文定義：

一個 parent $P$ 在修正為 $P'$ 後，若：

1. parent revision 有實質內容；
2. descendant corpus 已建立；
3. 有非零比例 descendants 經 independent audit 存活；
4. survivor 不只依賴被撤銷錯誤；
5. survivor 具有 theorem、prediction、mechanism、tool、negative result 或 transfer value；

則可稱：

$$
\boxed{
P
\text{ exhibited productive mis-specification}.
}
$$

---

# 13. 這是一個歷史性質，不是先驗資格

在 parent 還沒被修正以前，

不能宣布：

> 我的錯誤一定會很有生產力。

Productive mis-specification 多半是：

$$
\boxed{
\text{retrospective or post-revision classification}.
}
$$

---

# 14. 為什麼這一點重要

否則任何人都可以說：

> 我現在胡說，但未來可能很有啟發。

這會讓概念失去區分力。

所以必須：

$$
\text{audit after revision}.
$$

---

# 15. Error amplification

相反地，定義：

$$
\boxed{
\text{Error Amplification}
}
$$

若 parent 錯誤：

$$
e_P
$$

被 descendants 大量繼承，

使：

$$
P\rightarrow
d_1,d_2,\ldots,d_n
$$

全部共享錯誤核心。

當 parent 被修正後：

$$
S_D\approx0.
$$

---

# 16. Error amplification ratio

定義：

$$
A_E
=
1-S_D
$$

在已充分 audit 的 corpus 中。

若：

$$
A_E\rightarrow1,
$$

代表 parent error 具有高污染性。

---

# 17. Error inheritance graph

建立：

$$
G_E
=
(V_D,E_{\mathrm{inherit}}).
$$

若：

$$
d_i
$$

把錯誤 assumption：

$$
a^{-}
$$

傳給：

$$
d_j,
$$

則：

$$
d_i\rightarrow d_j.
$$

這使錯誤傳播可追蹤。

---

# 18. Error centrality

某個錯誤 assumption：

$$
a^{-}
$$

如果出現在大量 descendants，

可定義：

$$
Z_E(a^{-})
=
\sum_i
\mathbf 1[a^{-}\in A_i]w_i.
$$

高：

$$
Z_E
$$

表示修正成本高。

---

# 19. 錯置的「肥沃」不是錯誤量，而是 survivor 量

錯誤很多：

$$
\epsilon\uparrow
$$

不代表：

$$
\Phi_E\uparrow.
$$

真正重要：

$$
\boxed{
\text{surviving audited descendants}.
}
$$

---

# 20. Epistemic fertility

定義 audited generativity：

$$
G_A(P)
=
\#\text{audited non-equivalent descendants}.
$$

descendant robustness：

$$
R_D(P).
$$

transferability：

$$
T_D(P).
$$

則：

$$
\boxed{
\Phi_E(P)
=
G_A(P)
\cdot
S_D(P)
\cdot
R_D(P)
\cdot
T_D(P).
}
$$

---

# 21. Raw fertility 與 epistemic fertility

一個 hallucination engine：

$$
G_{\mathrm{raw}}\gg1
$$

但：

$$
S_D\approx0,
$$

所以：

$$
\Phi_E\approx0.
$$

這是最重要的防濫用公式之一。

---

# 22. Idealization 和 mis-specification 的差別

## 22.1 Idealization

研究者知道：

$$
M\neq W,
$$

但使用：

$$
M
$$

作為受控 approximation。

## 22.2 Misspecification

研究者或系統在某階段把：

$$
M
$$

當作足夠模型，

後來發現不夠。

## 22.3 兩者都可能 productive

但 epistemic status 不同。

所以 observatory 必須記：

```text
ERROR_STATUS:
  deliberate
  accidental
  discovered_later
  unknown
```

---

# 23. Idealization 的科學角色

Stanford Encyclopedia 對 scientific models 的整理指出，Galilean idealization 常故意引入字面上不真的假設，例如 point masses、frictionless planes 等，以隔離主要結構。

這種：

$$
\text{known falsehood}
$$

與：

$$
\text{mistaken theory}
$$

不是一回事。

---

# 24. Productive idealization

如果理想化：

$$
I
$$

使：

$$
\text{invariant}
$$

更清晰、

可解性上升、

prediction 仍在 domain 內有效，

則：

$$
I
$$

具有 epistemic utility。

這不是本文最強的 productive mis-specification 案例，

但提供近鄰概念。

---

# 25. Model discrepancy：錯在哪裡比「整體錯」更重要

2026 年 LISDD 的核心問題：

$$
\boxed{
\text{where does the physical model fail?}
}
$$

而不是：

$$
\text{throw the whole model away}.
$$

它先找 clean regime，

再定位 discrepant regime，

最後找 missing symbolic term。

---

# 26. Local correction

令原模型：

$$
f_0(x).
$$

在 region：

$$
D_c
$$

成立。

在：

$$
D_e
$$

失效。

修正：

$$
f(x)
=
f_0(x)
+
\mathbf 1_{x\in D_e}\Delta f(x).
$$

這是一個典型：

$$
\boxed{
\text{parent preservation + local repair}.
}
$$

---

# 27. 為什麼這是 descendant survival 的工程類比

原模型中的 clean structure：

$$
f_0|_{D_c}
$$

被保留。

只修：

$$
D_e.
$$

因此 parent 不是：

$$
\text{all-or-nothing}.
$$

---

# 28. Physics-guided correction under misspecification

2026 年 operator-learning correction 類研究同樣把：

$$
\text{trusted physics}
$$

與：

$$
\text{correction}
$$

拆開。

模型缺陷：

$$
\neq
$$

全部 prior physics 無效。

這正是本文的結構。

---

# 29. Missing physics symbolic regression

若：

$$
\dot x
=
f_{\mathrm{known}}(x)
+
f_{\mathrm{missing}}(x),
$$

研究不是丟掉：

$$
f_{\mathrm{known}},
$$

而是發現：

$$
f_{\mathrm{missing}}.
$$

這是一種：

$$
\text{repairable parent}.
$$

---

# 30. Experimental design 甚至可以為「找缺失」服務

2026 年 missing-physics experimental design 直接根據候選 model structures 設計新實驗，

目的不是只估參數，

而是：

$$
\boxed{
\text{discriminate among missing mechanisms}.
}
$$

這表示錯置本身可以改變下一步實驗路由。

---

# 31. Formal theorem proving 的 specification problem

在 Lean 中，

kernel 證明：

$$
\Pi\vdash Q_F.
$$

只能推出：

$$
Q_F
$$

被形式證明。

它不能推出：

$$
Q_F\equiv Q_I.
$$

其中：

$$
Q_I
$$

是人類原始 intended theorem。

---

# 32. 2026 Lean benchmark audit

近期 corpus-scale audit 發現：

- counterexamples；
- vacuous theorems；
- unsound axioms；
- missing hypotheses；
- incomplete translations；
- incorrect translations；
- Lean-specific specification hazards。

這證明：

$$
\boxed{
\text{formal proof validity}
\neq
\text{specification fidelity}.
}
$$

---

# 33. 形式化 parent 失敗不一定抹掉 proof engineering descendants

假設：

$$
Q_F
$$

後來發現：

$$
Q_F\not\equiv Q_I.
$$

但在證：

$$
Q_F
$$

過程中可能產生：

- tactic；
- lemma；
- library patch；
- proof repair dataset；
- dependency tool；
- counterexample checker。

它們仍可能有效。

---

# 34. 但 theorem descendant 必須重新判

如果 lemma：

$$
L
$$

只對錯 formalization 有意義，

那：

$$
L
$$

未必具有目標數學價值。

所以：

$$
\text{tool survival}
$$

與：

$$
\text{theorem survival}
$$

必須分開。

---

# 35. Descendant taxonomy

本文將 descendants 分成：

1. theorem descendant；
2. observational descendant；
3. mechanism descendant；
4. method descendant；
5. tool descendant；
6. dataset descendant；
7. negative-result descendant；
8. transfer descendant。

---

# 36. 不同 descendant 有不同 survival criterion

## 36.1 Theorem

需要重新 proof。

## 36.2 Observation

需要獨立 measurement / historical record。

## 36.3 Method

需要在新 target 上重測。

## 36.4 Tool

需要 functionality test。

## 36.5 Negative result

需要確認 no-go assumptions 是否仍成立。

---

# 37. Descendant survival vector

$$
\boxed{
\mathbf S_D
=
(
S_T,
S_O,
S_M,
S_{\mathrm{tool}},
S_{\mathrm{data}},
S_{\mathrm{neg}},
S_{\mathrm{transfer}}
).
}
$$

不要把所有 survivor 混成一個比例。

---

# 38. Parent truth 不由 descendant survival 反推

即使：

$$
S_D\gg0,
$$

仍不能推出：

$$
P\text{ true}.
$$

這是：

$$
\boxed{
\text{Descendant Non-Retrovalidation Principle}.
}
$$

---

# 39. Descendant Non-Retrovalidation Principle

$$
\boxed{
S_D(P)\uparrow
\not\Rightarrow
T(P)=1.
}
$$

一個錯 parent 可以產生真 descendants。

真 descendants 不會回頭把 parent 變真。

---

# 40. Parent Failure Non-Annihilation Principle

反向：

$$
\boxed{
T(P)=0
\not\Rightarrow
\forall d_i,\ T(d_i)=0.
}
$$

這是本文核心。

---

# 41. Parent Revision Audit Principle

若：

$$
P\rightarrow P',
$$

則：

$$
\boxed{
\mathcal D(P)
\text{ must be re-audited, not automatically retained or discarded.}
}
$$

---

# 42. 科學史：Carnot

## 42.1 Parent

caloric conservation：

$$
A_c.
$$

## 42.2 後來修正

熱不被理解成守恆 caloric fluid。

## 42.3 Survivor

Carnot 的 reversible cycle structure、

temperature-dependent efficiency insight 等，

成為後續 thermodynamics 的核心歷史資產。

## 42.4 正確讀法

不是：

$$
A_c\text{ was true}.
$$

而是：

$$
\boxed{
A_c
\text{ constrained a fruitful route whose key descendants survived}.
}
$$

---

# 43. Carnot 的「幸運錯誤」不是隨機幸運

如果 parent 假設完全任意，

不太可能穩定導向可保留結構。

更合理理解：

$$
A_c
$$

抓住了一部分：

$$
\text{reversibility / state dependence}
$$

的結構，

但本體解釋錯。

---

# 44. 科學史：phlogiston

## 44.1 Parent interpretation

燃燒透過 phlogiston 解釋。

## 44.2 Observation descendants

Priestley 等人的氣體實驗產生可重複 observations。

## 44.3 Parent 被替換

Lavoisier 的 oxygen framework 重新解釋。

## 44.4 Survival

$$
\text{observation}
$$

存活，

$$
\text{interpretation}
$$

不存活。

---

# 45. Observation–Interpretation Separation

因此：

$$
\boxed{
\text{Observation}(d)
\neq
\text{Interpretation}(d).
}
$$

parent 修正時應分離重驗。

---

# 46. Ideal gas

理想氣體不是歷史上的「錯理論後來被推翻」同一類型。

它更像：

$$
\text{controlled idealization}.
$$

但它顯示：

$$
\text{strict literal falsehood}
$$

可以與：

$$
\text{high domain utility}
$$

共存。

---

# 47. Ideal gas descendants

偏差：

$$
\Delta(P,V,T)
$$

促使：

- virial expansion；
- van der Waals corrections；
- phase-transition analysis。

所以 idealization 既是模型，

也是：

$$
\boxed{
\text{deviation reference}.
}
$$

---

# 48. Effective theories

EFT 類框架更進一步：

$$
T_{\mathrm{eff}}
$$

公開承認：

$$
\text{domain limited}.
$$

它不假裝是 ultimate truth。

這使它降低：

$$
\text{mis-specification risk}.
$$

因為 scope 被明示。

---

# 49. Scope declaration 是防錯的重要技術

定義：

$$
\operatorname{Scope}(M)
=
D_M.
$$

若：

$$
x\notin D_M,
$$

則：

$$
M(x)
$$

不應自動被視為模型 failure。

這是：

$$
\boxed{
\text{scope-aware epistemology}.
}
$$

---

# 50. Scope mismatch 的 productive 形式

如果把模型錯用到：

$$
D'\not\subseteq D_M,
$$

發現：

$$
\Delta\neq0,
$$

這個失敗可以幫助找：

$$
\partial D_M.
$$

也就是：

$$
\text{boundary discovery}.
$$

---

# 51. Boundary descendants

這類後代不是新 theorem 本身，

而是：

$$
\boxed{
\text{where the old theory stops working}.
}
$$

這非常有科學價值。

---

# 52. Category mismatch candidate

最難的是：

> 問題切割本身可能不適切。

例如：

- 把不同尺度當同一對象；
- 把 operational criterion 當 ontology；
- 把 representation artifact 當 invariant；
- 把局部量詞偷渡成全域量詞。

---

# 53. Category mismatch 的判定門檻必須最高

不能因為：

$$
\text{proof hard}
$$

就說：

$$
\text{category mistake}.
$$

至少需要：

1. explicit alternative formulation；
2. mapping theorem；
3. explanation of recurrent obstruction；
4. practical or formal gain；
5. independent audit。

---

# 54. 只是「我換個定義比較好證」還不夠

若：

$$
Q'
$$

比：

$$
Q
$$

好證，

可能只是：

$$
Q'
$$

比較弱。

所以需要：

$$
\operatorname{Map}(Q,Q').
$$

---

# 55. Reformulation map

理想情況有：

$$
f:Q\rightarrow Q',
$$

以及：

$$
g:Q'\rightarrow Q
$$

的清楚關係。

如果：

$$
Q\Leftrightarrow Q',
$$

則是等價重表述。

如果只有：

$$
Q\Rightarrow Q',
$$

必須明示 loss。

---

# 56. Framing superiority 不是語言喜好

定義：

$$
\operatorname{Sup}(Q',Q)
$$

至少依賴：

- semantic clarity；
- proof utility；
- empirical fit；
- transfer；
- obstruction resolution；
- mapping fidelity。

---

# 57. Productive mis-specification 的三種主要路徑

## A. Residual path

$$
P
\rightarrow
\Delta
\rightarrow
\text{missing mechanism}.
$$

## B. Boundary path

$$
P
\rightarrow
\text{failure regime}
\rightarrow
\partial D.
$$

## C. Reinterpretation path

$$
P
\rightarrow
d_i
\rightarrow
P'
\rightarrow
\text{same }d_i\text{ under new interpretation}.
$$

---

# 58. 第四條：Tool path

$$
P
\rightarrow
\text{hard research}
\rightarrow
\text{new tool}.
$$

即使 parent 失敗，

tool 仍可能長期存活。

---

# 59. 第五條：Negative path

錯 parent 的研究可能證明：

$$
\text{method }M\text{ cannot achieve target under assumptions }A.
$$

如果這個 no-go theorem 本身正確，

它仍存活。

---

# 60. 第六條：Representation path

為了解一個錯置問題建立：

$$
L'
$$

新表示。

後來發現：

$$
L'
$$

對其他問題也有價值。

這是 transfer survivor。

---

# 61. Survivor independence

定義 descendant 對錯 parent component：

$$
e_P
$$

的 dependence：

$$
I_i
=
\operatorname{Dep}(d_i,e_P).
$$

若：

$$
I_i=0,
$$

strong independence。

---

# 62. Repair cost

如果：

$$
I_i>0
$$

但可修：

$$
d_i\rightarrow d_i',
$$

定義：

$$
C_R(d_i)
=
\operatorname{Cost}(d_i\rightarrow d_i').
$$

低 repair cost 表示 robust descendant。

---

# 63. Survivor robustness score

$$
R_i
=
f(
1-I_i,
1-C_R,
\text{independent verification},
\text{cross-domain transfer}
).
$$

---

# 64. Descendant value matrix

| descendant | truth status | dependence on parent error | repair cost | transfer | survivor |
|---|---:|---:|---:|---:|---|
| $d_1$ | proven | low | 0 | high | yes |
| $d_2$ | unknown | medium | unknown | low | unknown |
| $d_3$ | refuted | high | high | none | no |

這比一句：

> 這個理論很 fruitful。

精確得多。

---

# 65. Post-revision knowledge accounting

parent 修正後：

$$
K_{\mathrm{before}}
$$

不應直接歸零。

建立：

$$
K_{\mathrm{after}}
=
K_{\mathrm{survive}}
\cup
K_{\mathrm{repaired}}
\cup
K_{\mathrm{unknown}}.
$$

---

# 66. Knowledge write-off ratio

$$
W_O
=
\frac{
K_{\mathrm{refuted}}
}{
K_{\mathrm{audited}}
}.
$$

與：

$$
S_D
$$

一起報。

---

# 67. AI 大規模生成時，write-off 可能非常重要

若 AI 生成：

$$
10^4
$$

個 descendants，

parent 後來修正，

如果：

$$
W_O=0.95,
$$

那麼 raw generativity 幾乎沒有價值。

---

# 68. 因此研究系統應保存 provenance

每個 descendant 必須知道：

$$
\text{which parent assumptions generated it}.
$$

否則 parent revision 後無法重算風險。

---

# 69. Provenance schema

```yaml
descendant_id:
parent_id:
parent_version:
assumptions_used:
representation:
method:
proof_dependencies:
verification:
derived_at:
transfer_targets:
revision_status:
```

---

# 70. Versioned parent

研究 parent 必須版本化：

$$
P^{(0)},
P^{(1)},
\ldots.
$$

descendant 也記：

$$
d_i@P^{(t)}.
$$

---

# 71. Revision cascade

若：

$$
P^{(t)}\rightarrow P^{(t+1)},
$$

系統自動找：

$$
\{d_i:A_i\cap\Delta A\neq\varnothing\}.
$$

這些進入 re-audit queue。

---

# 72. Research database 的新需求

普通文獻庫只存：

- title；
- abstract；
- citation。

Proof-space database 還要存：

- assumption lineage；
- obstruction lineage；
- revision lineage；
- survivor status。

---

# 73. AI agent 的 revision-aware memory

Agent 不只需要知道：

> 我以前證過 $L$。

而要知道：

> $L$ 是在 parent version $v3$ 、assumption set $A_{v3}$ 下證的； $v4$ 已移除 $a_7$，需要確認 $L$ 是否依賴 $a_7$。

---

# 74. 這會防止「殭屍知識」

殭屍知識：

$$
d_i
$$

已因 parent revision 失效，

但後續 agent 仍引用。

這在長程 AI research 特別危險。

---

# 75. Zombie knowledge rate

定義：

$$
Z_K
=
\frac{
N_{\mathrm{invalid\ but\ active}}
}{
N_{\mathrm{active}}
}.
$$

成熟系統應讓：

$$
Z_K\rightarrow0.
$$

---

# 76. 生產性錯置與 proof-space saturation

一個 basin：

$$
B
$$

可能長期研究後被發現：

$$
\text{framing flawed}.
$$

這時：

$$
B
$$

不是垃圾桶。

而是一個 descendant reservoir。

---

# 77. Basin salvage

定義：

$$
\operatorname{Salvage}(B)
=
\{
d\in B:d\text{ survives revision}
\}.
$$

salvage ratio：

$$
S_B.
$$

---

# 78. Obstruction salvage

一些 obstruction：

$$
O
$$

可能只因錯 formalization 存在。

另一些 obstruction 其實是更一般方法族的真限制。

所以 obstruction 也要 post-revision audit。

---

# 79. No-go salvage

若 parent 被修正，

一個 no-go theorem：

$$
N
$$

若量詞與 assumptions 仍保持，

可能繼續有效。

這類 negative survivor 很重要。

---

# 80. NS-203：如何使用本框架

目前不能說：

$$
\text{NS parent is mis-specified}.
$$

但可以預先建立：

$$
\text{revision-ready corpus}.
$$

---

# 81. Revision-ready NS corpus

每個 NS artifact 抽：

$$
(
A,C,L,O,R,T
).
$$

如果未來某 assumption family 被否定，

可以立刻找出受影響 descendants。

---

# 82. 假設性案例

假設未來發現：

$$
A^\star
$$

是某支 NS route 的不適切 global assumption。

則：

$$
\mathcal D(A^\star)
$$

進入 audit。

---

# 83. 可能存活的東西

即使 parent route 失效，

仍可能存活：

- local estimate；
- finite-scale lemma；
- computational diagnostic；
- visualization；
- obstruction taxonomy；
- other-PDE transfer。

---

# 84. 不能提前宣稱存活

每個都要：

$$
\operatorname{Reverify}.
$$

否則只是希望。

---

# 85. P/NP 同理

即使有人懷疑現有 problem framing 有高難度表示／範疇問題，

在沒有更強 reformulation theorem 前，

只能標：

$$
\text{meta-hypothesis}.
$$

不能寫：

$$
\text{P/NP is malformed}.
$$

---

# 86. 「無法判定」也不能由 corpus exhaustion 推出

即使：

$$
10^6
$$

輪 AI 都失敗，

仍不能推出：

$$
\operatorname{Independent}(Q,\mathcal A).
$$

independence 需要 metamathematical proof。

---

# 87. Productive mis-specification 的最危險濫用

> 因為歷史上錯理論有時 fruitful，所以我的錯理論也值得保留。

不成立。

歷史案例是 retrospective。

---

# 88. Retrospective evidence requirement

至少需要：

$$
N_{\mathrm{survivors}}>0
$$

且：

$$
C_D
$$

足夠高。

否則不能稱 productive。

---

# 89. 任意 wrong framing 的對照組

未來實驗應故意加入：

$$
P_{\mathrm{random}}
$$

作為 negative control。

看其：

$$
\Phi_E
$$

是否顯著低於 structured mis-specification。

---

# 90. 實驗一：Synthetic Parent Revision Benchmark

## 90.1 建立 ground truth parent

$$
P^\star.
$$

## 90.2 注入錯置

- missing assumption；
- wrong scope；
- wrong term；
- wrong quantifier；
- representation distortion。

## 90.3 讓 AI 研究

產生：

$$
\mathcal D(P_\epsilon).
$$

## 90.4 揭示 ground truth

修正：

$$
P_\epsilon\rightarrow P^\star.
$$

## 90.5 測

$$
S_D,
W_O,
\Phi_E.
$$

---

# 91. 實驗二：Formalization Mismatch Salvage Test

選取 Lean benchmark 中已知 specification defect。

讓 prover 在 defect version 上產生：

- proof；
- helper lemma；
- tool trace。

修正 statement 後，

測哪些資產仍能使用。

---

# 92. 實驗三：Missing-Physics Descendant Test

使用已知 dynamical system。

故意移除 mechanism：

$$
f_m.
$$

讓系統發現：

- residual；
- candidate corrections；
- symbolic mechanisms。

最後與 ground truth 比較。

---

# 93. 實驗四：Historical Retrospective Graph

對 Carnot、phlogiston 等案例建立：

$$
P
\rightarrow
d_i
\rightarrow
P'
$$

圖。

需要避免 presentism，

只標可文獻支持的 dependency。

---

# 94. 實驗五：NS Revision Simulation

不是宣稱 NS 錯。

而是人工選一個 route-level assumption：

$$
a
$$

做 ablation。

比較：

$$
\mathcal D_{\mathrm{keep}}
$$

與：

$$
\mathcal D_{\mathrm{drop}}.
$$

測 corpus salvageability。

---

# 95. 實驗六：Zombie Knowledge Stress Test

修改 parent version，

看 agent 是否仍引用 invalid descendants。

指標：

$$
Z_K.
$$

這對 persistent AI research system 很關鍵。

---

# 96. Productive Mis-specification Observatory

應至少有四張圖：

1. parent revision graph；
2. descendant dependency graph；
3. error inheritance graph；
4. survivor map。

---

# 97. Parent revision graph

$$
P^{(0)}
\rightarrow
P^{(1)}
\rightarrow
\cdots.
$$

每條 edge 記：

$$
\Delta A,\Delta D,\Delta Q,\Delta L,\Delta M.
$$

---

# 98. Descendant dependency graph

$$
P^{(t)}
\rightarrow
d_i.
$$

讓 lineage 可追蹤。

---

# 99. Error inheritance graph

標出：

$$
a^{-}
$$

如何往後傳。

---

# 100. Survivor map

parent revision 後：

- green：strong survivor；
- yellow：repairable；
- blue：transferred；
- red：refuted；
- gray：unknown。

UI 顏色只是 status，不是 truth metaphysics。

---

# 101. Productive Mis-specification Score

可建立操作性向量，而非單數：

$$
\mathbf P_M
=
(
G_A,
S_D,
R_D,
T_D,
C_D,
1-Z_K
).
$$

---

# 102. 為什麼不建議單 scalar

因為：

- 高 generativity 可能低 survival；
- 高 survival 可能樣本很少；
- 高 transfer 可能 theorem value 低。

向量更誠實。

---

# 103. 如果一定要排序

指定任務權重：

$$
J_{\mathcal T}
=
\mathbf w_{\mathcal T}\cdot\mathbf P_M.
$$

不同任務有不同排序。

---

# 104. Mis-specification discovery time

定義：

$$
t_m.
$$

parent 從建立到被修正：

$$
\Delta t_m.
$$

---

# 105. 越晚發現，corpus 污染越大

若 generation rate：

$$
g(t),
$$

則潛在 affected descendants：

$$
N_{\mathrm{risk}}
=
\int_0^{t_m}
g(t)\,dt.
$$

AI 高生成時代這個量可能非常大。

---

# 106. 因此 AI 需要更早的 parent audit

生成速度：

$$
g\uparrow
$$

時，

parent audit frequency 也應：

$$
f_{\mathrm{audit}}\uparrow.
$$

否則錯誤會快速擴散。

---

# 107. Auditing cadence

可設：

$$
f_{\mathrm{audit}}
=
h(
g,
Z_E,
C_{\mathrm{sat}},
R_O
).
$$

高生成、高 error centrality、反覆 obstruction 時提高 audit。

---

# 108. 生產性錯置不是反對嚴謹

恰恰相反。

如果不嚴謹，

根本不知道：

$$
\text{which descendants survived}.
$$

所以這套理論要求比「全部丟掉」更細的 provenance。

---

# 109. 生產性錯置不是反對真理

本文仍承認：

$$
T(P)
$$

與：

$$
T(d_i)
$$

是核心判準。

只是反對：

$$
T(P)=0
\Rightarrow
T(d_i)=0
$$

這個錯誤傳播推論。

---

# 110. 與 Lakatos 類研究綱領思想的距離

Lakatos 強調 research programme 可以在 anomaly 下持續發展，

而不是遇到一次反例立刻被拋棄。

本文與其有精神上的近鄰：

> research history 不應由單次 parent failure 全部抹除。

但本文更工程化地要求：

$$
\text{descendant-level post-revision audit}.
$$

---

# 111. 與 scientific realism / anti-realism 的距離

本文不解決：

$$
\text{science aims at truth?}
$$

這個宏觀爭論。

本文只要求：

$$
\boxed{
\text{truth status and generative value be separately recorded}.
}
$$

---

# 112. 生產性錯置和「醜模型」

2025 年對 high-energy physics 的討論指出，在特定實驗環境中，研究可能合理轉向更狹窄、ad hoc、complex 的「ugly models」。

這提醒：

$$
\text{simplicity}
$$

也不是永遠優先的單調判準。

模型選擇受：

$$
\text{available evidence landscape}
$$

制約。

---

# 113. 這與 mis-specification 的關係

一個 narrow model 可能：

$$
\text{less universal}
$$

但：

$$
\text{better targeted}.
$$

所以：

$$
\text{scope reduction}
$$

有時是 correction，不是退步。

---

# 114. Problem splitting

如果 parent：

$$
Q
$$

過度寬，

可拆：

$$
Q
\rightarrow
(Q_1,\ldots,Q_n).
$$

某些 descendants 可能其實屬於：

$$
Q_i.
$$

修正後應重新歸檔。

---

# 115. Problem merge

反過來，兩個看似不同 parent：

$$
Q_1,Q_2
$$

可能其實同一更高階結構的投影。

reformulation 可以 merge。

---

# 116. Category repair

若發現：

$$
Q
$$

混了兩種 truth criterion，

修正可能不是：

$$
Q\rightarrow Q'
$$

單一命題，

而是：

$$
Q\rightarrow
(Q_{\mathrm{math}},
Q_{\mathrm{empirical}}).
$$

---

# 117. 這種 split 會使很多舊爭論消失

因為原來：

$$
\text{disagreement}
$$

其實是：

$$
\text{different propositions}.
$$

但這要靠明確 semantic audit，

不能只靠哲學宣言。

---

# 118. Parent error 也可能是量詞錯誤

例如：

$$
\exists x
$$

被誤寫：

$$
\forall x.
$$

這種錯誤可以產生大量「很難的」證明失敗。

修正後問題突然簡單。

---

# 119. 量詞錯誤的 descendant salvage

一些局部 lemma：

$$
L(x)
$$

仍可能真。

只是不能支撐：

$$
\forall x.
$$

因此 local theorem 可存活，

global claim 不存活。

---

# 120. 這正是局部／全域分離的重要例子

$$
\boxed{
\text{global parent failure}
\not\Rightarrow
\text{local descendant failure}.
}
$$

---

# 121. AI theorem research 的高風險：語義微錯，生成爆炸

如果 formal target 微妙偏離，

AI 可以非常有效率地生成：

$$
10^3
$$

個局部 proof。

所以 AI 時代：

$$
\text{small specification error}
\times
\text{high generation rate}
$$

會產生巨大污染。

---

# 122. 因此 canonical source 和 provenance 是必要條件

若 source 本身被 silent normalization，

甚至無法知道 parent 何時改變。

所以：

$$
\boxed{
\text{source integrity}
}
$$

也是 productive-mis-specification audit 的基礎。

---

# 123. Research artifact 必須可重建

至少保存：

- exact source；
- version；
- checksum；
- dependency；
- validation；
- revision log。

否則 post-revision audit 不可靠。

---

# 124. 真正的「錯誤價值」是在可逆性

一個錯 parent 若讓所有 descendants 都無法追溯，

價值低。

若每個 descendant 都可追 provenance，

即使 parent 被修正，

仍可 salvage。

所以：

$$
\boxed{
\text{recoverability}
}
$$

是 AI 科學的重要設計原則。

---

# 125. 生產性錯置與語義負熵

如果系統保留：

$$
\text{source}
+
\text{version}
+
\text{dependency}
+
\text{audit},
$$

parent revision 後可以重建哪些知識受影響。

這就是一種：

$$
\text{semantic recoverability}.
$$

---

# 126. 從「證明成功」改成「知識資產組合」

一個研究 run 的結果不應只有：

```text
SOLVED / UNSOLVED
```

而應輸出：

```text
theorem_assets:
obstruction_assets:
tool_assets:
negative_results:
transfer_assets:
revision_risk:
```

---

# 127. 未解 parent 的價值可以被分解

$$
V(P)
=
V_{\mathrm{proof}}
+
V_{\mathrm{desc}}
+
V_{\mathrm{tool}}
+
V_{\mathrm{negative}}
+
V_{\mathrm{transfer}}.
$$

若：

$$
V_{\mathrm{proof}}=0,
$$

不代表：

$$
V(P)=0.
$$

---

# 128. 但未解不能冒充已解

報告必須明示：

$$
\text{parent unresolved}.
$$

這是學術倫理底線。

---

# 129. 形式命題一：Parent Failure Non-Annihilation

$$
\boxed{
\operatorname{Fail}(P)
\not\Rightarrow
\forall d\in\mathcal D(P),
\operatorname{Fail}(d).
}
$$

---

# 130. 形式命題二：Descendant Non-Retrovalidation

$$
\boxed{
\exists d\in\mathcal D(P)
\text{ survives}
\not\Rightarrow
P\text{ valid}.
}
$$

---

# 131. 形式命題三：Audit Requirement

$$
\boxed{
P\rightarrow P'
\Rightarrow
\operatorname{Reaudit}(\mathcal D(P)).
}
$$

---

# 132. 形式命題四：Raw Generativity Non-Productivity

$$
\boxed{
G_{\mathrm{raw}}\uparrow
\not\Rightarrow
\Phi_E\uparrow.
}
$$

---

# 133. 形式命題五：Error Exposure Monotonic Risk

其他條件相同下，

若 descendant 對被撤銷 assumption 的 dependency 增加：

$$
E_i\uparrow,
$$

則 post-revision invalidation risk 不應降低。

這是一個可檢驗的風險命題。

---

# 134. 形式命題六：Scope Repair Preservation

若 model 在 clean domain：

$$
D_c
$$

已被驗證，

只在：

$$
D_e
$$

失效，

則 local correction 不應無理由抹除：

$$
M|_{D_c}.
$$

---

# 135. 形式命題七：Specification Separation

$$
\boxed{
\operatorname{Proof}(Q_F)
\not\Rightarrow
Q_F\equiv Q_I.
}
$$

---

# 136. 形式命題八：Mis-specification Non-Diagnosis

$$
\boxed{
\text{repeated proof failure}
\not\Rightarrow
\operatorname{MisSpecified}(P).
}
$$

---

# 137. 非主張總表

本文不主張：

1. 錯誤問題一般比正確問題有價值；
2. 錯誤越大，生成性越高；
3. AI 應故意錯誤形式化；
4. idealization 等於錯誤研究；
5. model misspecification 等於 category mistake；
6. formalization defect 代表 informal theorem 錯；
7. parent 被修正後 descendants 自動有效；
8. descendant 存活會使 parent 重新變真；
9. 科學史上的 fruitful false theories 證明所有錯理論都值得保留；
10. Carnot 的 caloric ontology 因 fruitful 而正確；
11. phlogiston theory 因促成氧氣研究而正確；
12. NS-203 已證明 Navier--Stokes 問題 framing 有錯；
13. P/NP 已證明存在 category mismatch；
14. AI 證不出來可作為 mis-specification proof；
15. proof-space saturation 可推出 undecidability；
16. descendants 很多就等於 epistemic fertility 高；
17. tool descendant 和 theorem descendant 可用同一真值標準；
18. community consensus 決定 parent truth；
19. 新定義較容易證明就一定優於舊定義；
20. 本文已找到 universal productive-mis-specification law。

---

# 138. 與 LSI-PSD-07 的整合

第 7 篇建立：

$$
T
\neq
G.
$$

本文再建立：

$$
\boxed{
T(P)
\neq
T(d_i).
}
$$

以及：

$$
\boxed{
\text{parent correction}
\neq
\text{corpus annihilation}.
}
$$

---

# 139. 與 LSI-PSD-06 的整合

如果多條 route 匯流到 obstruction：

$$
O,
$$

可能觸發：

$$
\text{parent audit}.
$$

但只有 parent audit 真正發現：

$$
P\rightarrow P'
$$

後，

才進入本文的 descendant survival analysis。

---

# 140. 與 LSI-PSD-05 的整合

一個 saturated basin：

$$
B
$$

若後來被發現依賴錯 parent component，

則：

$$
B
$$

成為 salvage target。

不能整 basin 刪除。

---

# 141. 與 Logic-Space Integration 的整合

錯 parent 也會產生一個研究空間：

$$
\Omega(P).
$$

修正後：

$$
\Omega(P').
$$

重要問題是：

$$
\boxed{
\Omega(P)\cap\Omega(P')
}
$$

有多大。

這個交集就是 descendant survival 的空間版本。

---

# 142. Survivor space

定義：

$$
\Omega_{\mathrm{surv}}
=
\operatorname{Audit}
(
\Omega(P)\cap\Omega(P')
).
$$

---

# 143. Error-only space

$$
\Omega_{\mathrm{err}}
=
\Omega(P)\setminus\Omega_{\mathrm{surv}}.
$$

---

# 144. New-corrected space

$$
\Omega_{\mathrm{new}}
=
\Omega(P')\setminus\Omega(P).
$$

---

# 145. 修正後的三區圖

$$
\boxed{
\Omega(P)\cup\Omega(P')
=
\Omega_{\mathrm{err}}
\cup
\Omega_{\mathrm{surv}}
\cup
\Omega_{\mathrm{new}}.
}
$$

這是下一篇「生產性錯置窗口」的重要幾何基礎。

---

# 146. 研究不應只問 parent 是否錯

更好的問題是：

$$
\boxed{
\text{what survives the correction?}
}
$$

這會把科學史從：

> theory succession

改成：

> knowledge lineage.

---

# 147. AI 科學中的 lineage science

未來 AI 自主研究若持續多年，

最重要的資產可能不是單篇 paper。

而是：

$$
\boxed{
\text{versioned lineage of claims, assumptions, failures, repairs, and survivors}.
}
$$

---

# 148. 結論

生產性錯置不是「替錯誤辯護」的理論。

它首先是一套**錯誤發生之後如何不把真正知識一起丟掉**的方法論。

研究母體：

$$
P
$$

可能因：

- wrong assumption；
- wrong scope；
- missing physics；
- formalization mismatch；
- representation mismatch；
- framing defect；

被修正成：

$$
P'.
$$

這時最粗糙的處理有兩種。

第一種：

> 以前全部錯，全部丟掉。

第二種：

> 以前很 fruitful，所以其實沒錯。

兩者都不合理。

本文提出第三條路：

$$
\boxed{
P\rightarrow P'
\rightarrow
\operatorname{Reaudit}(\mathcal D(P))
\rightarrow
\{
\text{survive},
\text{repair},
\text{transfer},
\text{refute},
\text{unknown}
\}.
}
$$

真正有價值的不是「錯誤」，

而是：

$$
\boxed{
\text{在修正後仍能存活的知識譜系。}
}
$$

這也解釋了科學史上一個反覆出現的現象：

$$
\text{false or limited parent}
$$

可以與：

$$
\text{true or useful descendant}
$$

共存。

但這個共存絕不能被倒轉成：

$$
\text{useful descendant}
\Rightarrow
\text{true parent}.
$$

對 AI 大規模數學研究而言，這個區分會越來越重要。當生成速度上升到：

$$
10^2,
10^3,
10^4
$$

個研究 artifact，

任何小型 parent error 都可能形成大規模 error cascade。

同時，任何過度粗暴的 parent reset 也可能摧毀大量真正可保留的 lemma、tool、obstruction、negative result 與 transfer asset。

因此成熟 AI research infrastructure 必須從：

$$
\text{paper generation}
$$

進入：

$$
\boxed{
\text{revision-aware knowledge lineage management}.
}
$$

本文最後留下兩條互相制衡的原則：

$$
\boxed{
\textbf{A flawed parent can generate knowledge that survives its correction.}
}
$$

以及：

$$
\boxed{
\textbf{No amount of surviving descendant knowledge can retroactively validate the flawed parent.}
}
$$

這兩條同時成立，才是「生產性錯置」真正嚴格的版本。

---

# 參考文獻

1. Frigg, R., & Hartmann, S. **Models in Science.** *Stanford Encyclopedia of Philosophy*. Updated reference entry on scientific modeling, idealization, representation, and model ontology. https://plato.stanford.edu/entries/models-science/

2. Weisberg, M. (2007). **Three Kinds of Idealization.** *The Journal of Philosophy*, 104(12), 639–659.

3. Batterman, R. W., & Rice, C. C. (2014). **Minimal Model Explanations.** *Philosophy of Science*, 81(3), 349–376. https://doi.org/10.1086/676677

4. Norton, J. D. (2022). **How Analogy Helped Create the New Science of Thermodynamics.** *Synthese*, 200, 269.

5. King, M. (2025). **Experiment and the Pursuit of Ugly Models.** *European Journal for Philosophy of Science*, 15, Article 55. https://doi.org/10.1007/s13194-025-00692-y

6. Lepoutre, M. (2025). **Educational Falsehoods.** *Ergo: An Open Access Journal of Philosophy*.

7. Ma, L. et al. (2026). **Physics-guided correction for operator learning under model misspecification.** arXiv:2606.03469.

8. Wang, Y. (2026). **Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy.** arXiv:2606.23215. https://arxiv.org/abs/2606.23215

9. Strouwen, A., & Micluţa-Câmpeanu, S. (2026). **Experimental Design for Missing Physics.** arXiv:2604.01231. https://arxiv.org/abs/2604.01231

10. Strouwen, A. et al. (2026). **Bayesian Symbolic Regression for Missing Physics.** arXiv:2603.14918.

11. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493. https://arxiv.org/abs/2606.29493

12. Wang, E., Chess, S., Lee, D., Ge, S., Mallavarapu, A., & Ilin, V. (2026). **Learning to Repair Lean Proofs from Compiler Feedback.** arXiv:2602.02990.

13. American Chemical Society. **Joseph Priestley, Discoverer of Oxygen — National Historic Chemical Landmark.** Historical resource on oxygen discovery, phlogiston interpretation, and Lavoisier's reinterpretation.

14. Weingarten, K. (2026). **Productive Idealizations for Scientific Understanding: A Case Study in Effective Theories.** PhilSci-Archive preprint.

15. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $P$ | parent problem / theory / model |
| $P'$ | revised parent |
| $\mathcal C$ | parent correction operator |
| $\delta_P$ | parent revision distance |
| $\mathcal D(P)$ | descendants generated under parent $P$ |
| $d_i$ | individual descendant |
| $A_P^{-}$ | removed / invalidated parent assumptions |
| $E_i$ | descendant exposure to parent error |
| $S_D$ | descendant survival ratio |
| $C_D$ | descendant audit coverage |
| $W_O$ | write-off ratio |
| $Z_K$ | zombie-knowledge rate |
| $\Phi_E$ | epistemic fertility |
| $G_A$ | audited generativity |
| $R_D$ | descendant robustness |
| $T_D$ | transferability |
| $\Omega_{\mathrm{surv}}$ | survivor space |
| $\Omega_{\mathrm{err}}$ | error-only space |
| $\Omega_{\mathrm{new}}$ | corrected-new space |

---

## 附錄 B：Parent Revision Record

```yaml
parent_id:
version_from:
version_to:

revision:
  question:
  domain:
  assumptions_added:
  assumptions_removed:
  representation:
  model:
  scope:

reason:
  counterexample:
  specification_audit:
  missing_physics:
  scope_failure:
  category_reformulation:
  other:

affected_descendants:
  total:
  queued_for_reaudit:

status:
  revision_verified:
  independent_review:
```

---

## 附錄 C：Descendant Re-audit Record

```yaml
descendant_id:
parent_version_original:
parent_version_current:

dependency_exposure:
  removed_assumptions:
  changed_definitions:
  changed_domain:
  changed_representation:

verification:
  old_status:
  new_status:

survival:
  class:
    - strong
    - repairable
    - transferred
    - refuted
    - unknown
  repair_cost:
  transfer_target:

provenance:
  source:
  theorem_dependencies:
  tool_dependencies:
  checksum:
```

---

## 附錄 D：最小判定流程

```text
PARENT REVISION DETECTED
        |
        v
Identify changed assumptions / domain / statement
        |
        v
Find all dependent descendants
        |
        v
Re-audit each descendant
        |
        +--> strong survivor
        +--> repairable survivor
        +--> transfer survivor
        +--> refuted
        +--> unknown
        |
        v
Recompute survival / write-off / zombie rates
        |
        v
Update research memory
```

---

## 附錄 E：一句話版本

$$
\boxed{
\text{問題問錯了，不代表研究過程裡得到的每一件事都錯；但那些留下來的東西必須重新證明自己不依賴原來的錯。}
}
$$

這就是生產性錯置的最小形式。
