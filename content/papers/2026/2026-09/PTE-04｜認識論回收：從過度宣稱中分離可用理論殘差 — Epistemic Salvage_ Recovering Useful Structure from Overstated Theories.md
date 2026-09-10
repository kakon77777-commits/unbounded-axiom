# PTE-04｜認識論回收：從過度宣稱中分離可用理論殘差

## Epistemic Salvage: Recovering Useful Structure from Overstated Theories

**系列：** 《假設你是對的》／Provisional Truth Engineering Series（PTE）  
**系列文件：** PTE-04 / 07  
**版本：** v0.1  
**日期：** 2026-09-09  
**作者：** Neo.K  
**研究協作：** AI-assisted theoretical development  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 公開方法論論文／理論價值分解、降級與殘差保存  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

理論評價常被壓縮成二元判定：

$$
T
\in
\{
\text{True},
\text{False}
\}.
$$

但對跨域理論、宏大理論、工程性理論與尚未成熟的研究框架而言，這種二分法往往丟失最重要的資訊。一套理論可能在其最強本體論、全域性或不可約性主張上沒有得到支持，甚至部分主張已被反例削弱；然而，同一理論仍可能保留概念壓縮、形式規格、工程 heuristic、問題發現、架構組織、預測線索或研究搜尋價值。

本文提出 **Epistemic Salvage（認識論回收）**，作為 Provisional Truth Engineering（PTE）中處理「理論未完全成立，但也不應整體歸零」情況的核心方法。

本文首先定義理論價值向量：

$$
\boxed{
V(T)
=
(
V_C,
V_F,
V_E,
V_P,
V_U
)
}
$$

其中：

- $V_C$：Conceptual Value，概念與組織價值；
- $V_F$：Formal / Specification Value，形式化與規格價值；
- $V_E$：Engineering Value，工程與實作價值；
- $V_P$：Predictive Value，預測與經驗解釋價值；
- $V_U$：Unique / Irreducible Value，不可約新穎性價值。

本文再定義 **Irreducible Residue（不可約殘差）**：

$$
\boxed{
R_{\mathcal B,\mathcal E}(T)
=
T
-
K_{\mathcal B}(T)
-
O_{\mathcal E}(T)
}
$$

其中：

- $K_{\mathcal B}(T)$：可被當前 baseline family $\mathcal B$ 重建的部分；
- $O_{\mathcal E}(T)$：被當前證據 $\mathcal E$ 削除、降級或限制的過度宣稱；
- $R_{\mathcal B,\mathcal E}(T)$：尚未被重建、否定或充分解釋的剩餘理論結構。

本文特別主張：

$$
\boxed{
\Delta_T=0
\not\Rightarrow
V(T)=0
}
$$

以及：

$$
\boxed{
C_{\mathrm{overclaim}}=\text{False}
\not\Rightarrow
T=\varnothing.
}
$$

一個理論可能輸掉「我是新的基本原理」這一層，但仍然留下：

- 更好的座標系；
- 更簡潔的規格語言；
- 更早暴露的重要 invariant；
- 更好的研究問題分解；
- 更強的工程 modularity；
- 更具生產力的類比；
- 更有效的搜尋方向。

本文將理論狀態拆成：

$$
\boxed{
\text{Retain}
\cup
\text{Downgrade}
\cup
\text{Reject}
\cup
\text{Unresolved}
\cup
\text{Reconstructible}
}
$$

並提出 **Theory Residue Ledger（理論殘差帳本）**、**Claim-Level Downgrade Protocol（主張級降級協議）**、**Epistemic Salvage Ratio（ESR）** 與 **Residual Research Priority（RRP）**，使理論評價從整體標籤轉向細粒度狀態管理。

本文同時強調：認識論回收不是替失敗理論找藉口，也不是讓所有理論都能永久保留一點「也許」。真正的回收必須基於明確證據，並允許：

$$
R_{\mathcal B,\mathcal E}(T)
\rightarrow
\varnothing
$$

如果後續 baseline 與證據最終完全吸收或否定剩餘主張。

PTE 的目標不是保護理論，而是保護**資訊價值**。如果一套理論的宏大外殼失敗，但其中一個工程不變量、形式化技巧或問題分解方式仍然有效，科學方法不應因整體否定而把這些可用結構一起丟棄。

**關鍵詞：** Epistemic Salvage、Irreducible Residue、Theory Decomposition、Claim Downgrade、Reconstructibility、Overclaim、Engineering Value、Conceptual Value、Residual Research Priority、Provisional Truth Engineering

---

# 0. 邊界聲明

本文不主張：

- 每個失敗理論都值得回收；
- 任何錯誤理論都一定含有真理；
- 工程 heuristic 可以抵銷錯誤的事實主張；
- 概念新穎性可以代替外部證據；
- 「有趣」等於「有學術價值」；
- 尚未被反駁就等於值得保留；
- 不可約殘差是永久不變的；
- 未知狀態應被無限期保留而不再測試；
- 作者主觀認為某部分重要，就足以提升其 epistemic status；
- 理論被重建後，其歷史或詮釋價值必然消失。

本文只研究：

> 當一套理論的部分強主張失敗、部分可被已知方法重建、部分仍有工程或概念價值時，如何進行可追蹤、可修訂、可證偽的細粒度價值分解，而不是把整套理論一次判成全對或全錯。

---

# 1. 二元判定為什麼太粗

設理論：

$$
T
=
\{C_1,C_2,\ldots,C_n\}.
$$

其中：

$$
C_i
$$

可能分屬：

- 定義；
- 形式命題；
- 經驗主張；
- 工程主張；
- 本體論主張；
- 方法論主張；
- 預測；
- 規範性主張。

如果其中：

$$
C_1
$$

失敗，

不能推出：

$$
\forall i,
\quad
C_i=\text{False}.
$$

---

## 1.1 整體標籤會丟失資訊

若只記錄：

```text
THEORY = FALSE
```

會遺失：

- 哪一個 claim 失敗；
- 哪一個 claim 被重建；
- 哪一個 claim 仍未測；
- 哪一個 claim 有工程效用；
- 哪一個 claim 只需降級；
- 哪一個 claim 應該完全刪除。

---

# 2. 理論不是單一真值物件，而是多層結構

定義：

$$
\boxed{
T
=
(
C,
F,
E,
P,
U
)
}
$$

其中：

- $C$：conceptual structure；
- $F$：formal structure；
- $E$：engineering structure；
- $P$：predictive / empirical structure；
- $U$：unique / irreducible claims。

這些層可以不同步成立。

---

# 3. 理論價值向量

本文正式定義：

$$
\boxed{
V(T)
=
(
V_C,
V_F,
V_E,
V_P,
V_U
)
}
$$

---

## 3.1 Conceptual Value

$$
V_C
$$

表示理論是否提供：

- 新分類；
- 新問題切分；
- 有效概念壓縮；
- 跨域連接；
- 更好的研究座標；
- 可重用的語義框架。

---

## 3.2 Formal / Specification Value

$$
V_F
$$

表示理論是否提供：

- 更清楚的變數；
- invariant；
- constraint；
- state transition；
- contract；
- verification target；
- 可重播形式化。

---

## 3.3 Engineering Value

$$
V_E
$$

表示理論是否改善：

- 系統設計；
- modularity；
- correctness；
- robustness；
- debugging；
- maintainability；
- runtime behavior；
- data organization。

---

## 3.4 Predictive Value

$$
V_P
$$

表示理論是否產生：

- 新預測；
- 經驗可區分結果；
- 可驗證外部效果；
- 比 baseline 更準確的預測。

---

## 3.5 Unique / Irreducible Value

$$
V_U
$$

表示理論是否留下：

> 不能被目前 strongest known matched reconstruction 吸收的穩定差異。

---

# 4. 各價值維度可以分離

完全可能：

$$
V_C>0,
$$

$$
V_F>0,
$$

$$
V_E>0,
$$

同時：

$$
V_P\approx0,
$$

$$
V_U=\text{NotEstablished}.
$$

---

## 4.1 這不是矛盾

它只表示：

> 理論很好用，但目前沒有證據顯示它提出了新的不可約原理。

---

# 5. 過度宣稱

定義：

$$
\boxed{
O(T)
}
$$

為理論中超出現有證據、形式或實驗支持範圍的主張集合。

---

## 5.1 Overclaim 不等於整體錯誤

若：

$$
O(T)\neq\varnothing,
$$

不能推出：

$$
T=O(T).
$$

---

## 5.2 常見過度宣稱

```text
局部結果 -> 全域真理
工程有效 -> 本體論成立
benchmark win -> fundamental principle
同一性 -> 唯一性
形式一致 -> 現實正確
作者解讀 -> 唯一解讀
```

---

# 6. 可重建部分

設 baseline family：

$$
\mathcal B.
$$

定義：

$$
\boxed{
K_{\mathcal B}(T)
}
$$

為理論中可由：

$$
\mathcal B
$$

在 matched information、matched resources、matched task 下獨立重建的部分。

---

## 6.1 可重建不等於無價值

如果：

$$
K_{\mathcal B}(T)
$$

很大，

可能代表：

> 理論重新組織了大量已知機制。

這可以是：

$$
V_C>0
$$

或：

$$
V_F>0.
$$

---

# 7. 不可約殘差

本文定義：

$$
\boxed{
R_{\mathcal B,\mathcal E}(T)
=
T
-
K_{\mathcal B}(T)
-
O_{\mathcal E}(T).
}
$$

---

## 7.1 其中 $\mathcal E$

表示當前證據集合。

所以：

$$
R
$$

不是只依 baseline，

也依證據。

---

## 7.2 殘差是動態的

若：

$$
\mathcal B_{t_1}
\supset
\mathcal B_{t_0},
$$

或：

$$
\mathcal E_{t_1}
\supset
\mathcal E_{t_0},
$$

則：

$$
R_{t_1}(T)
$$

可能縮小。

---

# 8. Residue 不是神秘剩餘

它不代表：

> baseline 解釋不了，所以一定是新的宇宙法則。

只代表：

$$
\boxed{
\text{Current explanatory remainder}.
}
$$

---

# 9. 五種 claim disposition

對每個：

$$
C_i
$$

本文定義：

```text
RETAIN
DOWNGRADE
REJECT
RECONSTRUCTIBLE
UNRESOLVED
```

---

## 9.1 RETAIN

有足夠支持，

且目前無需降級。

---

## 9.2 DOWNGRADE

核心結構可能保留，

但 claim scope 必須縮小。

例如：

$$
\forall x
$$

降為：

$$
\exists D:
\forall x\in D.
$$

---

## 9.3 REJECT

有直接反例或證據不支持，

且沒有合理縮域版本。

---

## 9.4 RECONSTRUCTIBLE

行為有效，

但可由 matched baseline 重建。

---

## 9.5 UNRESOLVED

目前：

- 無法形式化；
- 無足夠證據；
- baseline 不完整；
- external test 不可得。

---

# 10. Downgrade 不是救理論

降級必須滿足：

$$
\boxed{
\text{new claim}
\subset
\text{old claim}.
}
$$

不能失敗後改成完全不同命題。

---

## 10.1 例子

原主張：

> 所有語義轉換都保持某 invariant。

若反例存在，

可以降成：

> 在明確條件 $D$ 下保持 invariant。

前提是：

$$
D
$$

不是事後任意挑選。

---

# 11. Scope Downgrade

設原 claim：

$$
C:
\forall x\in D,
P(x).
$$

若只在：

$$
D'
\subset D
$$

成立，

可以改為：

$$
C':
\forall x\in D',
P(x).
$$

---

## 11.1 必須記錄

```text
original_scope
failed_region
retained_scope
evidence
```

---

# 12. Strength Downgrade

原：

$$
P(x)=1.
$$

可降為：

$$
P(x)\ge\tau.
$$

但必須有事前或獨立理由支持：

$$
\tau.
$$

---

# 13. Status Downgrade

原：

```text
ESTABLISHED
```

可以降為：

```text
SUPPORTED
PRELIMINARY
NOT_ESTABLISHED
UNRESOLVED
```

---

# 14. Ontological Downgrade

一個常見而重要的回收：

$$
\boxed{
\text{ontology claim}
\rightarrow
\text{engineering heuristic}
}
$$

---

## 14.1 例子結構

原：

> X 是世界的基本本體結構。

若證據只支持：

> X 作為資料模型很好用。

則可以保留：

$$
V_E>0,
$$

但：

$$
V_U
$$

與本體論狀態降級。

---

# 15. Engineering Downgrade

原：

> 這個方法一定優於所有現有方法。

若 strong baseline tie，

可降成：

> 這是一個可用且結構清晰的方法。

---

# 16. Prediction Downgrade

原：

$$
\text{strong universal prediction}
$$

若只有部分資料支持，

應改為：

$$
\text{conditional empirical regularity}.
$$

---

# 17. Theory Residue Ledger

每套理論應建立：

```text
theory_id
version
claim_id
original_claim
claim_type
scope
evidence
matched_baseline
reconstructible_part
failed_part
retained_part
downgraded_part
unresolved_part
value_dimensions
residue_status
next_test
```

---

# 18. 理論回收不是刪除歷史

即使 claim 被：

$$
REJECT,
$$

也應保留：

- 原始版本；
- 失敗原因；
- counterexample；
- revision history；
- downstream effects。

---

## 18.1 因為錯誤也有研究價值

失敗路線可能幫助未來避免：

$$
\text{repeat failure}.
$$

---

# 19. 理論版本化

設：

$$
T_0
\rightarrow
T_1
\rightarrow
T_2.
$$

每次 revision 應保留：

$$
\boxed{
\text{lineage}.
}
$$

---

## 19.1 禁止 silent rewrite

不能讓：

$$
T_0
$$

失敗後，

直接把：

$$
T_1
$$

當成：

> 其實一開始就是這個意思。

---

# 20. Epistemic Salvage Ratio

定義：

$$
\boxed{
ESR
=
\frac{
W_{\mathrm{retained}}
}{
W_{\mathrm{total}}
}
}
$$

其中：

$$
W
$$

是按 claim importance 加權的理論內容。

---

## 20.1 ESR 的意義

如果：

$$
ESR=0.8,
$$

不表示：

> 理論 80% 正確。

只表示：

> 在目前評估下，80% 加權結構仍具有某種可保留狀態。

---

# 21. Value-Weighted Salvage Ratio

更進一步：

$$
\boxed{
ESR_V
=
\frac{
\sum_i w_i V_i^{\mathrm{retained}}
}{
\sum_i w_i V_i^{\mathrm{original}}
}
}
$$

---

# 22. 不同價值不應平均成一個分數

例如：

$$
V_E
$$

很高，

不能補償：

$$
V_P=0.
$$

---

## 22.1 禁止

$$
Score
=
0.2V_C
+
0.2V_F
+
0.2V_E
+
0.2V_P
+
0.2V_U
$$

作為唯一真值判定。

---

# 23. Value Profile

建議輸出：

```text
Conceptual: High
Formal: Medium
Engineering: High
Predictive: Low
Unique: NotEstablished
```

而不是：

```text
Theory Score = 72/100
```

---

# 24. Residual Research Priority

不是所有 residue 都值得繼續。

定義：

$$
\boxed{
RRP
=
f(
\text{impact},
\text{uncertainty},
\text{testability},
\text{novelty},
\text{cost},
\text{cross-domain reach}
).
}
$$

---

## 24.1 高 RRP

如果：

- residue 很小；
- 但若成立影響很大；
- 可低成本測試；

則值得優先。

---

## 24.2 低 RRP

如果：

- 高度不可觀測；
- 幾乎沒有外部後果；
- 測試成本極高；
- 即使成立影響也小；

則可以暫停。

---

# 25. Epistemic Salvage 與 PTE-03 的關係

PTE-03 得到：

$$
\Delta_T.
$$

PTE-04 問：

> 如果 $\Delta_T=0$，或只剩局部差異，那理論其他價值怎麼處理？

---

# 26. Useful Tie 的回收方式

若：

$$
\Delta_T=0,
$$

但：

$$
V_C,V_F,V_E>0,
$$

則標：

$$
\boxed{
\text{USEFUL\_TIE}
}
$$

而不是：

$$
\text{FAILED THEORY}.
$$

---

# 27. Residual Win 的回收方式

若：

$$
\Delta_T>0,
$$

但還沒有 non-reducibility proof，

則：

$$
V_U
=
\text{Candidate}.
$$

不是：

$$
V_U
=
\text{Established}.
$$

---

# 28. Failed Universal Claim 的回收方式

若：

$$
\forall x\in D
$$

被一個反例擊穿，

保留：

- 成功子域；
- conditional rule；
- failure boundary。

---

# 29. Failure Boundary 可能比原理論更有價值

有時真正有價值的是：

$$
\boxed{
\partial D
}
$$

即：

> 理論從哪裡開始失效？

---

## 29.1 邊界也是知識

若：

$$
P(x)
$$

在：

$$
D_1
$$

成立，

在：

$$
D_2
$$

失敗，

則：

$$
D_1\leftrightarrow D_2
$$

的邊界可能成為新研究對象。

---

# 30. Counterexample as Structure Generator

反例不只是：

$$
\text{destroy}.
$$

也可能：

$$
\boxed{
\text{refine}.
}
$$

---

## 30.1 反例可以產生

- scope boundary；
- missing variable；
- hidden assumption；
- alternative mechanism；
- new subtype。

---

# 31. 理論錯誤與資料錯誤分離

如果實驗失敗，

至少要區分：

```text
theory error
formalization error
implementation error
data error
baseline error
metric error
infrastructure fault
```

---

# 32. 否則會錯誤回收

例如：

$$
\text{implementation bug}
$$

不應讓：

$$
C_i
$$

直接降級。

---

# 33. 回收需要因果歸因

只有當：

$$
\text{failure}
\rightarrow
C_i
$$

的因果鏈可信，

才能改 claim status。

---

# 34. Salvage Provenance

每一次狀態改變需保存：

```text
previous_status
new_status
triggering_evidence
baseline_version
evaluator
timestamp
reason
reversible
```

---

# 35. Unknown 不應被當垃圾桶

如果太多 claim 都標：

$$
UNRESOLVED,
$$

PTE 可能失去否證力。

---

## 35.1 Unknown 必須附理由

```text
insufficient evidence
unformalized
external test blocked
baseline incomplete
measurement unavailable
contradictory evidence
```

---

# 36. Unknown 也應有期限或 next action

例如：

```text
UNRESOLVED
next_test = external dataset
```

---

# 37. Epistemic Debt

若某 claim 長期停在：

$$
UNRESOLVED,
$$

可定義：

$$
\boxed{
D_E(C_i)
}
$$

為 epistemic debt。

---

## 37.1 Debt 增長

若理論繼續建立更多下游 claim，

但上游仍未驗證，

則：

$$
D_E\uparrow.
$$

---

# 38. Downstream Dependency Risk

設：

$$
C_2
\leftarrow
C_1.
$$

若：

$$
C_1
$$

被降級，

則：

$$
C_2
$$

必須重新評估。

---

## 38.1 Dependency propagation

可定義：

$$
\boxed{
\operatorname{Impact}(C_i)
=
\{C_j:C_j\text{ depends on }C_i\}.
}
$$

---

# 39. 理論圖而不是理論清單

將：

$$
T
$$

表示為：

$$
G_T=(V,E).
$$

---

## 39.1 Node status

每個 node 有：

```text
RETAIN
DOWNGRADE
REJECT
RECONSTRUCTIBLE
UNRESOLVED
```

---

## 39.2 Graph salvage

若高中心度 node 被拒絕，

整個理論可能大幅重構。

---

# 40. Centrality-Weighted Salvage

定義 claim centrality：

$$
c_i.
$$

則：

$$
\boxed{
ESR_C
=
\frac{
\sum_{i\in \mathrm{retained}}c_i
}{
\sum_i c_i
}.
}
$$

---

# 41. 核心 claim 失敗與邊緣 claim 失敗不同

若：

$$
c_i\gg c_j,
$$

則：

$$
Reject(C_i)
$$

影響可能遠大於：

$$
Reject(C_j).
$$

---

# 42. Theory Skeleton

回收後剩下的高中心度 retain nodes，

定義為：

$$
\boxed{
Skeleton(T).
}
$$

---

## 42.1 這可能成為新版理論

若：

$$
Skeleton(T)
$$

仍形成自洽、可用結構，

可以建立：

$$
T'.
$$

---

# 43. 但新版理論不能冒充原版

必須：

$$
T'\neq T
$$

且版本號、日期、scope 分開。

---

# 44. Theory Fork

若不同回收路徑：

$$
T'_1,
T'_2
$$

都合理，

可以形成：

$$
\boxed{
\text{theory fork}.
}
$$

---

# 45. Fork 不一定是壞事

它可能代表：

> 原理論其實包含多個可分離研究程序。

---

# 46. Authorial Decoupling

理論一旦公開，

不必由作者本人決定唯一回收方式。

---

## 46.1 因此

$$
\boxed{
\text{Authorial intent}
\neq
\text{exclusive evaluator}.
}
$$

但作者原始文本仍是重要 source boundary。

---

# 47. Person-Theory Separation

PTE-04 明確禁止：

$$
Reject(C_i)
\Rightarrow
Reject(A).
$$

其中：

$$
A
$$

是作者。

---

## 47.1 同樣

$$
Retain(C_i)
$$

也不代表：

$$
A
$$

在其他主張上正確。

---

# 48. Epistemic Salvage 與學術禮貌無關

它不是：

> 對作者客氣一點。

而是：

> 不要因粗糙分類而丟失可用資訊。

---

# 49. 理論的歷史價值也是獨立維度

某理論即使：

$$
V_P=0,
$$

仍可能具有：

$$
V_H>0
$$

即歷史價值。

---

## 49.1 但本文不把 $V_H$ 納入核心五維

因為 PTE 主要評估：

> 現在還能做什麼。

---

# 50. 教學價值

有些理論可作為：

- 思考工具；
- 反例教材；
- 系統設計案例。

可記：

$$
V_D.
$$

但同樣不等於真值。

---

# 51. Search Heuristic Value

若理論讓研究者更快找到：

$$
x^{*},
$$

即重要問題或反例，

則可有：

$$
V_S>0.
$$

---

# 52. Extended Value Vector

若需要更完整：

$$
\boxed{
V^{+}(T)
=
(
V_C,
V_F,
V_E,
V_P,
V_U,
V_H,
V_D,
V_S
)
}
$$

---

# 53. 但公開主結論仍建議保留五維

避免模型過度複雜。

---

# 54. Epistemic Salvage 的三個錯誤極端

## 54.1 Total Rejection

$$
\text{one strong claim fails}
\Rightarrow
T=0.
$$

---

## 54.2 Endless Rescue

$$
\text{every failure}
\Rightarrow
\text{new reinterpretation}.
$$

---

## 54.3 Value Inflation

$$
\text{small heuristic value}
\Rightarrow
\text{theory remains revolutionary}.
$$

---

# 55. PTE-04 的中間路徑

$$
\boxed{
\text{preserve what survives}
+
\text{downgrade what weakens}
+
\text{reject what fails}
+
\text{label what remains unknown}.
}
$$

---

# 56. Claim-Level Salvage Protocol

```text
1. Freeze original claim
2. Record original scope
3. Record evidence
4. Record matched reconstruction
5. Identify failed region
6. Identify retained region
7. Determine value dimensions
8. Assign disposition
9. Propagate dependency impact
10. Produce residue
11. Define next test
12. Version the theory
```

---

# 57. Salvage 必須可逆

如果後來新證據出現，

可以：

$$
DOWNGRADE
\rightarrow
RETAIN
$$

或：

$$
UNRESOLVED
\rightarrow
REJECT.
$$

---

# 58. State Transition

建議：

```text
UNRESOLVED -> RETAIN
UNRESOLVED -> DOWNGRADE
UNRESOLVED -> REJECT
RETAIN -> DOWNGRADE
DOWNGRADE -> REJECT
DOWNGRADE -> RETAIN
RECONSTRUCTIBLE -> RESIDUAL_WIN
```

---

# 59. 不允許 silent upgrade

任何：

$$
NOT\_ESTABLISHED
\rightarrow
ESTABLISHED
$$

必須有新 evidence receipt。

---

# 60. Residual Research Program

若：

$$
R(T)\neq\varnothing,
$$

可以把 residue 變成新研究計畫。

---

## 60.1 每個 residue node

建立：

```text
residue_id
claim
why_unreconstructed
why_unfalsified
observable consequence
cost
next experiment
```

---

# 61. 研究資源應從整體理論轉向 residue

傳統做法：

> 繼續替整套理論找證據。

PTE 建議：

$$
\boxed{
\text{focus on }R(T).
}
$$

---

# 62. 因為已被重建的部分不需要重複證明不可約

如果：

$$
K_{\mathcal B}(T)
$$

已經很大，

繼續在那裡投入：

$$
C_{\mathrm{research}}
$$

邊際資訊增益可能很低。

---

# 63. Residual Information Gain

定義：

$$
\boxed{
IG_R
=
\frac{
\Delta \text{epistemic state of }R(T)
}{
C_{\mathrm{test}}
}.
}
$$

---

# 64. 高 $IG_R$ 的實驗應優先

這可接到：

$$
RRP.
$$

---

# 65. 理論回收與開源研究

若理論與其實驗公開，

其他研究者可以獨立：

- fork；
- downgrade；
- reconstruct；
- challenge；
- retain。

---

# 66. 這使理論變成公共可演化物件

而不是：

> 只能由作者宣布自己是否被反駁。

---

# 67. Theory Residue as Public Object

可表示：

$$
\boxed{
T
\rightarrow
R(T)
\rightarrow
\mathfrak P(R(T))
}
$$

其中：

$$
\mathfrak P
$$

表示公共投影與再研究。

---

# 68. AI 的角色

AI 可以協助：

- claim decomposition；
- dependency graph；
- baseline search；
- counterexample search；
- value tagging；
- residue clustering；
- version diff。

---

# 69. 但 AI 不能自己決定全部價值權重

例如：

$$
V_C
$$

或：

$$
V_H
$$

帶有部分學術社群與研究目標依賴。

---

# 70. AI Judge 的限制

AI 可以輔助：

$$
\text{classification}.
$$

但 hard status：

$$
REJECT
$$

最好依：

- deterministic oracle；
- explicit counterexample；
- external evidence。

---

# 71. Residue Hallucination Risk

AI 可能為了「保留價值」，

發明：

> 其實這個理論還有某某意義。

---

## 71.1 防止方式

任何 retained value 都需：

```text
source-supported
experiment-supported
inference-labeled
```

---

# 72. Salvage Claim 必須可追溯

若說：

> 這部分有工程價值。

要有：

$$
E_{\mathrm{eng}}.
$$

---

# 73. Pure Interpretive Value

若只有：

> 這個比喻很有啟發性。

可以標：

$$
V_C
$$

而不是：

$$
V_E.
$$

---

# 74. Practical Example Template

一套抽象理論：

$$
T.
$$

經 PTE-03 得：

$$
\Delta_T=0.
$$

但它提出：

- 一個更清楚的 identity / representation 分離；
- 一個更簡潔的 invariant language；
- 一個 useful failure taxonomy。

則：

$$
V_C>0,
$$

$$
V_F>0,
$$

$$
V_E>0,
$$

但：

$$
V_U=\text{NotEstablished}.
$$

這是典型：

$$
\boxed{
\text{Useful Tie + Epistemic Salvage}.
}
$$

---

# 75. 另一種例子

若：

$$
\Delta_T>0,
$$

但只在：

$$
D_1
$$

成立，

則：

$$
V_U(D_1)
=
\text{Candidate},
$$

不能寫：

$$
V_U(\Omega)
=
\text{Established}.
$$

---

# 76. 研究敘事也應降級

論文文字應從：

> 新基本原理

改成：

> 在指定域觀察到 residual advantage。

---

# 77. 語言降級是科學操作的一部分

不是公關問題。

---

# 78. Claim Strength Ledger

對每個 claim 記：

```text
universal
broad
conditional
local
heuristic
descriptive
```

---

# 79. 降級方向

$$
\boxed{
\text{universal}
\rightarrow
\text{conditional}
\rightarrow
\text{local}
\rightarrow
\text{heuristic}.
}
$$

---

# 80. 不能反向偷偷升級

需要新證據。

---

# 81. Epistemic Salvage 與 replication

第三方重現後，

可更新：

$$
V_P,
V_E,V_U.
$$

---

# 82. 多個 independent replication

若：

$$
n\uparrow,
$$

confidence 可提高，

但仍不代表不可約。

---

# 83. Reconstruction Replication

除了重現 theory system，

也應重現：

$$
B^{*}.
$$

否則 baseline fairness 可能不可驗。

---

# 84. Theory Residue Benchmark

未來可以建立 benchmark：

> 給一套部分失敗理論，AI 能否正確拆出 retained / rejected / unresolved residue？

---

# 85. 評測維度

- claim fidelity；
- no over-salvage；
- no total-rejection bias；
- dependency propagation；
- evidence grounding；
- value separation；
- correct uncertainty。

---

# 86. Salvage Precision

定義：

$$
\boxed{
SP
=
\frac{
\text{correctly retained claims}
}{
\text{all retained claims}
}
}
$$

---

# 87. Salvage Recall

$$
\boxed{
SR
=
\frac{
\text{correctly retained claims}
}{
\text{all retainable claims}
}
}
$$

---

# 88. 過度回收

若：

$$
SP\downarrow,
$$

代表：

> 太容易替理論找價值。

---

# 89. 過度丟棄

若：

$$
SR\downarrow,
$$

代表：

> 太容易整體打成零。

---

# 90. 理想目標

$$
\boxed{
SP\uparrow,
\qquad
SR\uparrow.
}
$$

---

# 91. PTE-04 的核心研究命題

## ES-H1：Non-Binary Value Hypothesis

大量複雜理論的價值不能被：

$$
\{\text{true},\text{false}\}
$$

充分表示。

---

## ES-H2：Useful Residue Hypothesis

存在理論：

$$
T
$$

使其最強 claim 被否定，

但：

$$
R(T)\neq\varnothing
$$

且具有正工程或概念價值。

---

## ES-H3：Baseline-Expansion Shrinkage Hypothesis

隨：

$$
\mathcal B
$$

擴張，

若理論並無不可約 primitive，

則：

$$
|R_{\mathcal B,\mathcal E}(T)|
\downarrow.
$$

---

## ES-H4：Counterexample Refinement Hypothesis

有效反例不只降低 claim confidence，

還能提高：

$$
\text{boundary knowledge}.
$$

---

## ES-H5：Versioned Salvage Hypothesis

保留 theory lineage 與 claim-state history，

比 silent rewrite 更能提高後續研究可重建性。

---

# 92. 最小 PTE-04 執行協議

```text
Step 1  Import PTE-03 result
Step 2  Decompose theory graph
Step 3  Assign claim statuses
Step 4  Separate reconstructible content
Step 5  Identify overclaim
Step 6  Identify unresolved content
Step 7  Compute value profile
Step 8  Identify residue
Step 9  Propagate dependency impact
Step 10 Produce revised theory skeleton
Step 11 Define residual research priorities
Step 12 Version and archive
```

---

# 93. 最小輸出

```text
TheoryResidueLedger
ValueProfile
ClaimDispositionMap
DependencyImpactMap
OverclaimSet
ReconstructibleSet
UnresolvedSet
IrreducibleResidue
ResidualResearchPlan
VersionReceipt
```

---

# 94. 最終方法論結論

理論評價若只有：

$$
\boxed{
\text{accept}
\quad\text{or}\quad
\text{reject},
}
$$

很容易同時犯兩種錯誤：

第一種，把失敗理論裡仍有效的工程或概念結構一起丟掉。

第二種，把局部有效結構繼續拿來支撐已經失敗的宏大主張。

PTE-04 的目的，就是同時避免兩者。

---

# 95. 最終核心公式

第一個：

$$
\boxed{
V(T)
=
(
V_C,V_F,V_E,V_P,V_U
).
}
$$

第二個：

$$
\boxed{
R_{\mathcal B,\mathcal E}(T)
=
T
-
K_{\mathcal B}(T)
-
O_{\mathcal E}(T).
}
$$

第三個：

$$
\boxed{
\text{Overclaim failure}
\not\Rightarrow
\text{total value failure}.
}
$$

第四個：

$$
\boxed{
\text{Engineering usefulness}
\not\Rightarrow
\text{irreducible novelty}.
}
$$

---

# 96. 結論：科學不是保護理論，而是保護資訊

一套理論如果：

- 一部分錯；
- 一部分被重建；
- 一部分有用；
- 一部分未知；

那麼最差的兩個選擇是：

> 全部相信。

和：

> 全部丟掉。

更好的做法是：

$$
\boxed{
\text{拆分}
\rightarrow
\text{驗證}
\rightarrow
\text{降級}
\rightarrow
\text{回收}
\rightarrow
\text{聚焦殘差}.
}
$$

PTE 因此把：

$$
T
$$

從一個需要被護衛或摧毀的整體，

轉成一個可以被：

- 分解；
- 重建；
- 修訂；
- 回收；
- 版本化；

的研究物件。

真正值得保護的不是理論的宏大標籤。

而是：

$$
\boxed{
\text{其中仍然具有資訊增益的結構}.
}
$$

如果最終：

$$
R_{\mathcal B,\mathcal E}(T)
=
\varnothing,
$$

那麼也應接受：

> 當前沒有剩餘不可約主張。

如果：

$$
R_{\mathcal B,\mathcal E}(T)
\neq
\varnothing,
$$

下一步不是再次宣稱勝利，

而是：

> **把最昂貴、最精確的下一輪研究，只集中在這個 residue 上。**

這就是認識論回收的核心。

---

# 97. 下一篇

**PTE-05｜AI 原生理論壓測：從文字論證到可重播證偽系統**  
*AI-Native Theory Stress Testing: From Argument to Reproducible Falsification*

下一篇將把 PTE-01 至 PTE-04 的方法正式工程化為 AI-native runtime，建立：

```text
TheoryManifest
ClaimLedger
OperationalizationManifest
BaselineManifest
ExperimentManifest
EvidenceReceipt
ResidueReport
```

並回答：

> **如果未來 AI 可以自動讀理論、形式化、實作、建立強 baseline、生成反例與保存 residue，一個真正不容易自我欺騙的 Theory Testing Runtime 應該長什麼樣？**
