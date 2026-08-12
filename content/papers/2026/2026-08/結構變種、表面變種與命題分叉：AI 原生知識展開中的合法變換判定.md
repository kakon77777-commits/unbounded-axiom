# 結構變種、表面變種與命題分叉：AI 原生知識展開中的合法變換判定

**English Title:** Structural Variation, Surface Variation, and Proposition Branching: Legality Tests for AI-Native Knowledge Expansion  
**Series:** AI-Native Knowledge Expansion, Paper II  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10

## 摘要

〈基底知識空間擴張〉提出：可靠基礎知識經過大量合法、可驗證的展開與重組，可以形成高品質的 AI 推理資料。然而，只要允許大規模自動生成，立即會出現一個更基本的問題：**什麼才算真正不同的變種？**

若僅更換變數名稱、數值、自然語言措辭或公式排列方式，資料量可以快速膨脹，但有效結構資訊幾乎沒有增加。反之，一個看似只修改單一條件的命題，卻可能已經改變其定義域、量詞、充分必要條件、依賴圖或可證性，從「同一命題的變種」分叉為新的命題族。

本文建立 AI 原生知識展開中的「合法變換判定框架」。我們區分四個層級：表面變種、表示變種、結構變種與命題分叉；定義命題的結構指紋、保留不變量、變換算子、標準形與分叉條件；並提出「變種證書」（Variation Certificate），使每一個 AI 生成節點都必須回答：它從哪個母命題產生、改變了什麼、保留了什麼、與母命題是等價、強化、弱化、特化、泛化、對偶、反例，還是已形成新的命題。

本文主張：AI 原生資料生成真正需要最大化的不是樣本數，而是**經過等價類去重後的有效結構覆蓋**。在此意義上，canonicalization、equivalence detection 與 proposition branching 不是資料清理的後處理，而是 BKSE 的核心生成規則。

**關鍵詞：** 結構變種；表面變種；命題分叉；基底知識空間擴張；標準形；等價類；形式驗證；AI 合成資料；知識圖；變種證書

---

## 1. 從「生成更多」轉向「生成真正不同」

Paper I 定義：

\[
\mathcal E(P)
=
\{\text{legal verified neighbors of }P\}.
\]

但這個定義留下了一個關鍵詞：

\[
\text{legal}.
\]

什麼是合法？

更進一步：

\[
P_1\neq_{\text{text}}P_2
\]

是否就代表：

\[
P_1\neq_{\text{structure}}P_2?
\]

答案顯然不是。

例如：

\[
a^2+b^2=c^2
\]

和：

\[
c^2=a^2+b^2
\]

在字面順序上不同，但數學命題沒有增加。

甚至：

\[
x^2+y^2=z^2
\]

也只是變數重新命名。

因此：

\[
\boxed{
\text{Surface Difference}
\not\Rightarrow
\text{Structural Difference}.
}
\]

反方向也成立。一個只修改一個符號的命題：

\[
\forall x,\ P(x)
\]

改成：

\[
\exists x,\ P(x)
\]

文字差異極小，但邏輯結構已根本不同。

所以 AI-native generation 若只以文字差異率、embedding distance 或 token diversity 衡量資料多樣性，很容易製造大量「看起來不同、其實相同」的資料，或把真正的新命題誤歸為原命題的同義變種。

---

## 2. 四層變種分類

本文先定義四個層級。

### 2.1 L0：表面變種（Surface Variation）

只改變外部表示，不改變可識別的語義或形式結構。

例如：

\[
a^2+b^2=c^2
\]

與：

\[
x^2+y^2=z^2.
\]

或自然語言：

> 兩股平方和等於斜邊平方。

與：

> 在直角三角形中，斜邊平方等於兩直角邊平方之和。

若兩者指向完全相同的形式命題，則屬於：

\[
V_0.
\]

典型操作包括變數重新命名、語序調整、同義改寫、格式改變、括號或排版改變，以及不改變意義的符號替換。

這類資料可服務語言魯棒性，但不應被計入主要的結構擴張量。

### 2.2 L1：表示變種（Representational Variation）

核心數學對象不變，但使用不同表示系統。

例如畢氏定理可寫為：

\[
a^2+b^2=c^2,
\]

也可寫成內積形式：

\[
\|u+v\|^2
=
\|u\|^2+\|v\|^2,
\qquad
\langle u,v\rangle=0.
\]

或座標形式：

\[
(x_2-x_1)^2+(y_2-y_1)^2=d^2.
\]

此時不同表示可能揭露不同推理路徑，所以資訊價值高於 L0，但它們仍可能屬於同一個核心定理族。

記為：

\[
V_1.
\]

### 2.3 L2：結構變種（Structural Variation）

至少一個推理結構發生改變，但仍能明確追溯到母命題。

例如：

- 正命題轉逆命題；
- 固定部分變數，改成求解問題；
- 將定理嵌入幾何／代數／向量不同模組；
- 移除或增加條件；
- 從二維推廣到 \(n\) 維；
- 將存在性問題改為分類問題；
- 把結果改成極值或可實現域問題。

這一層記為：

\[
V_2.
\]

### 2.4 L3：命題分叉（Proposition Branching）

當變換改變了核心定義域、量詞、依賴、真值條件、對象類型或主要結論，使新節點不能再合理稱為「同一命題的變種」，則應建立新的命題 ID。

記為：

\[
V_3.
\]

例如：

\[
P:
\forall x\in D,\ A(x)\Rightarrow B(x)
\]

若改成：

\[
P':
\exists x\in D,\ A(x)\Rightarrow B(x),
\]

即使只改一個量詞，也應視為命題分叉。

因此：

\[
\boxed{
V_0
\rightarrow
V_1
\rightarrow
V_2
\rightarrow
V_3
}
\]

不是單純難度排序，而是「結構偏離母命題程度」的分類。

---

## 3. 命題結構指紋

為了判斷兩個命題是否仍屬於同一結構族，本文定義一個概念性的結構指紋：

\[
\boxed{
\Phi(P)
=
(
\mathcal D,
\mathcal O,
\mathcal Q,
\mathcal A,
\mathcal R,
\mathcal C,
\mathcal K
)
}
\]

其中：

- \(\mathcal D\)：domain，定義域；
- \(\mathcal O\)：objects，主要對象與型別；
- \(\mathcal Q\)：quantifiers，量詞結構；
- \(\mathcal A\)：assumptions，假設；
- \(\mathcal R\)：relations，核心關係；
- \(\mathcal C\)：conclusion，結論；
- \(\mathcal K\)：dependency kernel，必要依賴骨架。

如果 AI 只把 \(a,b,c\) 改成 \(x,y,z\)，則：

\[
\Phi(P')=\Phi(P).
\]

若把平面改成任意內積空間，但仍保持正交平方和結構，則可能：

\[
\Phi(P')\neq\Phi(P)
\]

但存在清楚的泛化映射：

\[
P\hookrightarrow P'.
\]

這應標記為 structural generalization，而不是普通等價。

---

## 4. 不變量：什麼必須被保留？

對一個指定變換類型 \(T\)，不應要求所有元素都不變，而應指定「該類變換允許改什麼、禁止改什麼」。

定義：

\[
I_T(P)
\]

為變換 \(T\) 必須保留的不變量集合。

例如變數重新命名：

\[
T_{\alpha}
\]

必須保留：

\[
I_{T_\alpha}
=
\{
\mathcal D,
\mathcal O,
\mathcal Q,
\mathcal A,
\mathcal R,
\mathcal C,
\mathcal K
\}.
\]

而泛化算子：

\[
T_{\mathrm{gen}}
\]

則允許 \(\mathcal D\) 擴張，但要求原命題可嵌入新命題：

\[
P
=
P'|_{\mathcal D_0}.
\]

因此，合法性不是一個全域布林值，而是：

\[
\boxed{
\operatorname{Legal}(T,P,P')
}
\]

依變換種類而定。

---

## 5. 八種基本變換算子

BKSE 可以先定義一套最小操作語彙。

### 5.1 Alpha / Surface Renaming

\[
T_\alpha(P)
\]

只改變符號或名稱。

預期：

\[
P\equiv T_\alpha(P).
\]

### 5.2 Equivalent Rewrite

\[
T_{\mathrm{eq}}(P)
\]

使用已證明等價規則重新表示。

預期：

\[
P\leftrightarrow T_{\mathrm{eq}}(P).
\]

### 5.3 Specialization

\[
T_{\mathrm{spec}}(P)
\]

把一般命題限制到子域：

\[
D'\subseteq D.
\]

通常：

\[
P\Rightarrow T_{\mathrm{spec}}(P),
\]

但反向不一定成立。

### 5.4 Generalization

\[
T_{\mathrm{gen}}(P)
\]

擴張定義域或對象類型。

要求至少能證明在原域嵌入下：

\[
T_{\mathrm{gen}}(P)
\Rightarrow P.
\]

### 5.5 Assumption Ablation

對：

\[
A=\{A_1,\ldots,A_n\}
\]

移除 \(A_i\)，得到：

\[
P_{-A_i}.
\]

若仍可證，則原假設可能冗餘；若找到反例，則得到假設必要性證據。

### 5.6 Converse / Dualization

若：

\[
P:A\Rightarrow B,
\]

則生成：

\[
T_{\mathrm{conv}}(P):
B\Rightarrow A.
\]

它不預設成立，而是問題生成器。

### 5.7 Composition

\[
T_{\mathrm{comp}}(P,Q)
\]

把兩個已有命題接成新結構。

若：

\[
P:A\Rightarrow B,
\qquad
Q:B\Rightarrow C,
\]

可生成候選：

\[
A\Rightarrow C.
\]

但只有中間型別、假設與語義接口一致時才合法。

### 5.8 Counterfactual / Error-Neighborhood Mutation

刻意修改一個條件，使命題成為 near-miss：

\[
T_{\mathrm{err}}(P).
\]

其目標不是保存真值，而是產生錯誤鄰域，並附最小反例或失敗原因。

---

## 6. 標準形與等價類

如果 AI 每生成一個節點都直接存進資料庫，BKSE 很快就會被等價重複淹沒。

因此定義 canonicalization：

\[
\operatorname{Can}(P)
=
P^\ast.
\]

若：

\[
\operatorname{Can}(P_1)
=
\operatorname{Can}(P_2),
\]

則優先將兩者歸入同一等價類：

\[
[P]
=
\{Q:Q\sim P\}.
\]

這裡的 \(\sim\) 可以分層：

\[
\sim_{\alpha},
\quad
\sim_{\mathrm{def}},
\quad
\sim_{\mathrm{logic}},
\quad
\sim_{\mathrm{semantic}}.
\]

分別表示變數重命名等價、定義展開等價、可證邏輯等價，以及更高層語義等價。

不能把所有等價都混成單一關係。

因此資料庫應區分：

\[
\text{identity}
\neq
\text{equivalence}
\neq
\text{useful alternative representation}.
\]

---

## 7. 結構距離

為了做自動 frontier scheduling，可以定義概念性的結構距離：

\[
d_S(P,Q)
=
\sum_i
w_i
\delta_i(
\Phi_i(P),
\Phi_i(Q)
).
\]

例如：

\[
d_S
=
w_D\Delta_D
+
w_Q\Delta_Q
+
w_A\Delta_A
+
w_R\Delta_R
+
w_C\Delta_C
+
w_K\Delta_K.
\]

這個距離不是普通 embedding distance。

兩段自然語言可以 embedding 很接近，但若一個使用 \(\forall\)、另一個使用 \(\exists\)，結構距離應很大。

反之，一條公式與一段長篇自然語言說明，字面距離很大，但形式結構距離可以接近 0。

因此：

\[
\boxed{
d_{\mathrm{text}}
\neq
d_{\mathrm{semantic}}
\neq
d_{\mathrm{structural}}.
}
\]

---

## 8. 命題分叉條件

何時必須建立新 proposition ID？

本文提出最小規則：若以下任一核心元素發生未被父變換類型允許的改變，則應 branch：

1. 定義域改變；
2. 主要對象型別改變；
3. 量詞改變；
4. 核心假設改變；
5. 真值條件改變；
6. 主要結論改變；
7. 必要依賴骨架改變；
8. 從 theorem 變成 optimization / classification / existence 等不同任務型別。

形式上：

\[
\exists i:
\Phi_i(P)\neq \Phi_i(P')
\land
i\notin
\operatorname{AllowedChange}(T)
\]

則：

\[
\boxed{
\operatorname{Branch}(P,P')=1.
}
\]

---

## 9. 變種證書（Variation Certificate）

每個生成節點應附：

```text
variation_id
parent_id
operator
source_fingerprint
target_fingerprint
preserved_invariants
changed_dimensions
formal_relation
verification_method
canonical_form
equivalence_class
branch_status
counterexample_status
```

其中：

\[
\text{formal\_relation}
\in
\{
=,\leftrightarrow,\Rightarrow,\Leftarrow,
\subset,\supset,
\text{incomparable},
\text{unknown}
\}.
\]

因此 AI 不能只說：

> 我生成了一個新變種。

而必須能說：

> 它是 \(P\) 的 specialization；保留核心關係與結論，縮小 domain；canonicalization 後不與現有節點重複；形式關係已驗證。

這才是可用的 AI-native research object。

---

## 10. 畢氏定理的最小示例

令：

\[
P_0:
\angle C=90^\circ
\Rightarrow
a^2+b^2=c^2.
\]

若只是：

\[
x^2+y^2=z^2,
\]

則主要是：

\[
V_0.
\]

若改寫成：

\[
c=\sqrt{a^2+b^2},
\qquad c>0,
\]

則在適當 domain 下屬表示等價：

\[
V_1.
\]

若改成：

\[
a^2+b^2=c^2
\Rightarrow
\angle C=90^\circ,
\]

則是 converse：

\[
V_2.
\]

若進一步研究：

\[
a^2+b^2>c^2
\]

與角度分類，則已進入新的分類命題家族，應建立獨立 proposition ID，但保留 lineage。

若推廣到內積空間：

\[
u\perp v
\Rightarrow
\|u+v\|^2
=
\|u\|^2+\|v\|^2,
\]

則屬 generalization，原直角三角形命題可以視為其具體 instance。

因此：

\[
P_{\mathrm{Pyth}}
\hookrightarrow
P_{\mathrm{inner}}.
\]

兩者不應被壓成同一節點。

---

## 11. 與形式證明器的接口

形式系統特別適合判定 L0–L2 的部分關係，例如：

- definitional equality；
- alpha-equivalence；
- equality proof；
- iff proof；
- implication；
- subtype specialization；
- instance inheritance。

Lean 的 `simp` 使用已註冊的 equality / iff theorem 把表達式改寫成較標準的形式；Lean 官方也明確區分 simplification 與一般 rewriting：前者強調把問題 reformulate 成較標準、適合後續證明的形態，而後者是更具方向性的手選改寫。

這給 BKSE 一個重要啟示：

\[
\boxed{
\text{Canonicalization is not merely text normalization.}
}
\]

它應盡可能由：

\[
\text{proved rewrite rules}
\]

驅動。

但形式證明器仍無法單獨回答所有「研究上是否值得視為新結構」的問題。

所以：

\[
\text{formal equivalence}
\neq
\text{research redundancy}.
\]

---

## 12. 從抽象結構到 instance

近期 autoformalization 工作已開始明確使用「抽象結構 → 具體 instance」方向。SITA 將抽象數學結構視為包含 definitions、assumptions、operations 與 theorems 的 reusable template，再生成具體 Lean instance 並檢查結構假設。

這非常接近：

\[
T_{\mathrm{spec}}:
P_{\mathrm{abstract}}
\rightarrow
P_{\mathrm{instance}}.
\]

其核心不是產生更多文字，而是保留：

\[
\text{structural assumptions}.
\]

因此 transformation lineage 可以直接成為形式資料集 metadata。

---

## 13. 程式語言中的對應問題

相同框架也適用程式碼。

若只改：

```text
x -> item
```

屬 L0。

若 Python 改寫成 Rust，但演算法與輸入輸出語義保持一致，可能屬 L1。

若把：

\[
O(n^2)
\]

演算法改為：

\[
O(n\log n),
\]

即使輸出功能一致，內部演算法結構已不同，屬 L2。

若 API 行為、輸入域或 side-effect contract 改變，則可能屬 L3。

因此：

\[
\text{behavioral equivalence}
\neq
\text{algorithmic identity}.
\]

BKSE 必須維護多種 equivalence relation，而不能只靠 hash 或 embedding。

---

## 14. 有效結構覆蓋

Paper I 定義概念性的有效結構資料量。本篇進一步提出：

\[
\boxed{
C_{\mathrm{eff}}(D)
=
\sum_{[P]\in D/\sim}
w([P])
}
\]

即：先依適當等價關係去重，再計算有效覆蓋。

因此資料集報告應同時給：

\[
|D|,
\]

\[
|D/\sim|,
\]

\[
\text{branch count},
\]

\[
\text{operator distribution},
\]

\[
\text{verification rate}.
\]

這比只說「合成了多少 samples」更能反映知識增量。

---

## 15. 最小演算法

BKSE 的變種引擎可以寫成：

```text
INPUT: verified node P

1. fingerprint(P)
2. choose operator T
3. generate candidate P'
4. infer intended relation R(P,P')
5. canonicalize(P')
6. search equivalent existing nodes
7. verify relation R
8. compare fingerprints
9. classify V0 / V1 / V2 / V3
10. if duplicate:
       attach alternative representation/proof
    elif legal variation:
       add child node
    elif proposition branch:
       create new proposition ID with lineage
    else:
       reject or store as negative/error node
11. emit Variation Certificate
```

核心不是第 3 步的「生成」。

真正困難的是：

\[
4,5,6,7,8,9,10.
\]

也就是分類、標準化、去重、驗證與身份管理。

---

## 16. 可否證實驗

選擇一組已形式化的基礎 theorem。

對每個 theorem 生成四組候選：

- A：paraphrase / rename；
- B：equivalent representation；
- C：structural mutation；
- D：branch / invalid mutation。

再要求系統完成：

1. 四層分類；
2. formal relation 預測；
3. canonical duplicate detection；
4. branch detection；
5. counterexample generation；
6. proof verification。

評測：

\[
\text{Acc}_{\mathrm{class}},
\]

\[
\text{Acc}_{\mathrm{relation}},
\]

\[
\text{Precision}_{\mathrm{dedup}},
\]

\[
\text{Recall}_{\mathrm{branch}},
\]

\[
\text{VerifiedRate}.
\]

更重要的 downstream 實驗則比較：

\[
D_{\mathrm{raw}}
\]

與：

\[
D_{\mathrm{structure-aware}}
\]

在相同 token budget 下的推理與 theorem-proving 表現。

若結構感知去重與變種分類沒有任何收益，則本框架的工程價值會被削弱。

---

## 17. 研究邊界

本文不主張存在一個對所有數學與程式都完美有效的全域結構距離。

也不主張：

\[
P\leftrightarrow Q
\]

即可自動推出 P 與 Q 在教育、搜尋、證明策略、表示學習上完全冗餘。

此外，對自然語言哲學、法律、社會科學等高語義領域，「同一命題」本身可能缺乏穩定形式核心，因此本篇框架不能直接無條件移植。這些領域需要額外的語義保真層、底空間與判定域分析；本系列之後的橋接論文將另行處理。

---

## 18. 結論

AI-native knowledge expansion 的真正單位不應是：

\[
\text{sample}.
\]

而應是：

\[
\boxed{
\text{verified structural node}.
}
\]

一個高品質節點必須知道：

- 它從哪裡來；
- 經過什麼變換；
- 保留什麼；
- 改變什麼；
- 與父節點是什麼形式關係；
- 是否與既有節點等價；
- 是否應建立新的 proposition identity；
- 如何被驗證。

因此：

\[
\boxed{
\text{Generate More}
\rightarrow
\text{Generate Distinguishably More}.
}
\]

再進一步：

\[
\boxed{
\text{Structural Diversity}
=
\text{Variation}
-
\text{Equivalence Redundancy}
+
\text{Verified Branching}.
}
\]

Paper I 的問題是：

> 基礎知識能不能被大量展開？

Paper II 的答案是：

> 可以，但如果沒有等價類、標準形、合法變換與命題分叉判定，「大量展開」很快就會退化為大量重複。

因此，BKSE 的第二個核心不是生成器，而是：

\[
\boxed{
\text{Identity Management for Knowledge}.
}
\]

下一篇將處理第三個問題：

\[
\boxed{
\text{How should errors and counterexamples be systematically generated?}
}
\]

亦即建立「錯誤鄰域與反例空間」：如何讓 AI 不只學會證明一個命題，也學會辨認與母命題距離極近、卻因一個條件、量詞、定義域或推導步驟而失敗的命題。

---

## 參考文獻

Lean Language Reference. *Simp Sets; Rewrite Rules; Simplification vs Rewriting*. Lean Project.

Leang, J. O. J., Hong, G., Li, W., & Cohen, S. B. (2025). *Theorem Prover as a Judge for Synthetic Data Generation*. arXiv:2502.13137.

Lai, J., Zhang, J., Xu, S., et al. (2025). *LLM-based Automated Theorem Proving Hinges on Scalable Synthetic Data Generation*. arXiv:2505.12031.

Li, C., Ma, W., Wang, Z., & Wen, Z. (2025). *SITA: A Framework for Structure-to-Instance Theorem Autoformalization*. arXiv:2511.10356.

Lean Community. *Mathlib: A Foundation for Formal Mathematics Research and Verification*. Lean.
