# Series C — C02｜由世界到個體、由個體到世界：全域觀察的對偶計算
## Dual Computation of Global Observation: From World to Individual and from Individual Back to World

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 02 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Foundational Theory / Dual Observer Computation / Domain Formation / Global Composition

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文延續 C01 的 Global Observer 定義，將其中兩個方向正式化：

$$
\mathcal O_{\downarrow}
:
\widehat{\Omega}
\rightarrow
W
\rightarrow
D
\rightarrow
S
\rightarrow
x,
$$

以及：

$$
\mathcal O_{\uparrow}
:
x
\rightarrow
S
\rightarrow
D
\rightarrow
W
\rightarrow
\widehat{\Omega}.
$$

本文稱兩者為 **全域觀察對偶計算（Dual Computation of Global Observation）**。

此處「對偶」不是宣稱兩者具有某一既有範疇論、線性代數或拓撲對偶的精確同構，而是指出：它們在功能上互補、可彼此約束、可形成往返閉環，但一般不必互為逆映射。

---

# 摘要

C01 提出：AI 在能夠全域計算一個世界以前，必須先學會如何全域地看見世界。本文進一步回答：

> **這種「看見」究竟如何在世界尺度與個體尺度之間運動？**

如果 AI 只能從全域概念向下拆解，它會得到越來越細的局部分析，但可能無法把局部重新整合成世界。

如果 AI 只能從局部資料向上聚合，它會形成越來越大的模型，但可能把關鍵差異過度壓縮。

因此本文提出兩條互補方向。

第一條為：

$$
\boxed{
\mathcal O_{\downarrow}
:
\widehat{\Omega}
\rightarrow
W
\rightarrow
D
\rightarrow
S
\rightarrow
x
}
$$

稱為 **Global-to-Local Differentiation（全域到局部分異）**。

其核心任務不是「把世界全部放大」，而是：

> 在當前世界模型中，找到哪些差異、邊界、局部尺度與未解結構值得提高解析度。

第二條為：

$$
\boxed{
\mathcal O_{\uparrow}
:
x
\rightarrow
S
\rightarrow
D
\rightarrow
W
\rightarrow
\widehat{\Omega}
}
$$

稱為 **Local-to-Global Composition（局部到全域組成）**。

其核心任務不是「把所有東西塞進同一集合」，而是：

> 從局部個體、差異、關係、重疊、非交集與條件作用中，建立更高階集合、計算域與世界模型。

本文強調：

$$
\boxed{
\mathcal O_{\uparrow}
\circ
\mathcal O_{\downarrow}
\neq
I
}
$$

通常成立，因為：

- projection 可以有損；
- decomposition 可以選擇性 materialize；
- aggregation 可以壓縮細節；
- domain boundary 可以依 task 改變；
- observer budget 有限；
- uncertainty 可能只能保留區間而不能還原原始狀態；
- world update 可以加入新的外部 evidence。

因此真正的 Global Observer 不是一個可完美復原的 encoder-decoder，而是一個持續重建世界的 **reprojection system**。

本文定義下行過程：

$$
\boxed{
\mathcal D_{\downarrow}
=
\mathsf{Resolve}
\circ
\mathsf{Differentiate}
\circ
\mathsf{Bound}
\circ
\mathsf{Domainize}
}
$$

以及上行過程：

$$
\boxed{
\mathcal C_{\uparrow}
=
\mathsf{Group}
\circ
\mathsf{Relate}
\circ
\mathsf{Bridge}
\circ
\mathsf{Glue}
\circ
\mathsf{WorldUpdate}.
}
$$

為避免把「分類」當作世界本體，本文引入 **Observer-Induced Partition**：

$$
\boxed{
\mathcal P_{O,q,t}(W)
=
\{C_1,\ldots,C_n,U\},
}
$$

其中 $C_i$ 是 observer 在 task $q$ 、time $t$ 下建立的可操作 cell，而 $U$ 保留 unresolved / unclassified mass。

這表示一個成熟 observer 不必強迫所有存在立即歸類：

$$
\boxed{
\text{Classification Completeness}
\neq
\text{Observer Completeness}.
}
$$

相反，能正確保留：

$$
U\neq\varnothing
$$

有時正是更高解析度的表現。

本文進一步建立四種損失：

$$
\boxed{
L_{\mathrm{collapse}},
L_{\mathrm{fragment}},
L_{\mathrm{bridge}},
L_{\mathrm{glue}}.
}
$$

分別表示：

1. **Collapse Loss**：把真正不同的對象錯誤合併；
2. **Fragmentation Loss**：把可安全壓縮的對象過度分裂；
3. **Bridge Loss**：跨域映射造成的資訊／語義損失；
4. **Glue Loss**：局部結果無法一致回寫全域世界的損失。

因此對偶觀察品質不能只以「分類準確率」衡量，而應同時看：

$$
\boxed{
Q_{\mathrm{dual}}
=
F(
L_{\mathrm{collapse}},
L_{\mathrm{fragment}},
L_{\mathrm{bridge}},
L_{\mathrm{glue}},
C_{\mathrm{coherence}},
Cost
).
}
$$

本文再引入 **Reprojection Error**：

$$
\boxed{
E_{\mathrm{reproj}}
=
d(
\widehat W_t,
\mathcal O_{\uparrow}
(
\mathcal O_{\downarrow}
(
\widehat W_t
)
)
).
}
$$

如果：

$$
E_{\mathrm{reproj}}
$$

很高，表示 AI 下行拆解後再組回世界時，丟失大量結構或產生不一致。

但本文不要求：

$$
E_{\mathrm{reproj}}\rightarrow0
$$

永遠成立，因為新的局部 evidence 可能合理地改寫原世界模型：

$$
\widehat W_t
\rightarrow
\widehat W_{t+1}.
$$

因此需區分：

$$
\boxed{
\text{Reconstruction Error}
\neq
\text{Legitimate World Revision}.
}
$$

本文將 Global Observer 的真正穩定狀態理解為一個往返循環：

$$
\boxed{
\widehat W_t
\rightarrow
\mathcal O_{\downarrow}
\rightarrow
\{D_i\}
\rightarrow
\mathcal O_{\uparrow}
\rightarrow
\widehat W_{t+1}.
}
$$

若新的 evidence 使：

$$
\widehat W_{t+1}
\neq
\widehat W_t,
$$

不一定表示觀察失敗；反而可能表示 observer 正確修正了自己。

因此本文提出 **Dual Observer Closure**：

$$
\boxed{
\mathsf{DOC}(O,W,q,t)
}
$$

成立的最低條件不是「回到原模型」，而是：

1. 所有重要 local changes 都能回寫；
2. 所有 global constraints 都能下傳；
3. unresolved mass 被保留；
4. bridge / glue debt 可追蹤；
5. world state 更新保持 provenance；
6. 觀察者知道哪些變化來自 evidence、哪些來自 representation。

本文也將 C01 的 Global Observer Capability Vector 擴充為：

$$
\boxed{
\mathbf G_O^{(2)}
=
(
g_{\downarrow},
g_{\uparrow},
g_{rr},
g_{bd},
g_{gl},
g_{rp},
g_{cl}
),
}
$$

其中：

- $g_{\downarrow}$：top-down differentiation；
- $g_{\uparrow}$：bottom-up composition；
- $g_{rr}$：resolution routing；
- $g_{bd}$：boundary discrimination；
- $g_{gl}$：global gluing；
- $g_{rp}$：reprojection stability；
- $g_{cl}$：closure awareness。

本文最後提出一個重要研究命題：

$$
\boxed{
\text{Global Observer Intelligence}
\propto
\text{quality of scale traversal}
}
$$

而不是單純：

$$
\text{number of represented facts}.
$$

換句話說，未來真正的類全域 AI 需要能自由地：

$$
\boxed{
\text{zoom out}
\leftrightarrow
\text{zoom in}
}
$$

但此處的 zoom 不是視覺縮放，而是：

- 概念解析度；
- 因果解析度；
- 概率解析度；
- domain resolution；
- temporal resolution；
- computational representation；
- verification granularity。

一個能看全域卻不能進入局部差異的 AI，只是低解析度宏觀模型。

一個能看無數局部卻不能重新合成世界的 AI，只是高解析度碎片系統。

因此真正的 Global Observer 必須同時成立：

$$
\boxed{
\text{Global without flattening}
}
$$

以及：

$$
\boxed{
\text{Local without fragmentation}.
}
$$

**關鍵詞：** Global Observer、Dual Computation、Global-to-Local Differentiation、Local-to-Global Composition、Reprojection、Glue Debt、Observer Partition、Resolution Routing、World Update、AI-Native Domain Computation

---

# 1. 問題：為什麼「看見世界」需要兩個方向？

世界不是一張固定解析度的圖片。

對一個 observer 而言：

$$
W
$$

既可以被壓縮成：

$$
\widehat W,
$$

也可以被展開為：

$$
\{x_1,\ldots,x_n\}.
$$

但如果只有壓縮：

$$
\text{difference}\downarrow.
$$

如果只有展開：

$$
\text{integration}\downarrow.
$$

因此需要雙向運動。

---

# 2. 下行不是普通 reductionism

$$
\widehat W
\rightarrow
D
\rightarrow
S
\rightarrow
x
$$

並不等於：

> 世界只是由最小粒子組成。

本文的下行是：

$$
\boxed{
\text{observer-driven resolution increase}.
}
$$

它是計算行為，不是形上學還原論。

---

# 3. 上行也不是普通 holism

$$
x
\rightarrow
S
\rightarrow
D
\rightarrow
W
$$

不等於：

> 所有東西都屬於一個整體，所以差異不重要。

相反，上行必須保存合法差異。

---

# 4. 第一對偶原則

$$
\boxed{
\text{Differentiation}
\leftrightarrow
\text{Composition}.
}
$$

沒有 differentiation，composition 容易錯合。

沒有 composition，differentiation 容易碎裂。

---

# 5. Observer Traversal

定義 observer 在解析尺度上的位置：

$$
\lambda_O(t).
$$

但實際上不是單一 scalar。

更合理：

$$
\boxed{
\Lambda_O(t)
=
\{\lambda_i(t)\}_{i\in I}.
}
$$

不同 domain 可位於不同解析度。

---

# 6. 多解析度同時存在

例如：

$$
\lambda_{\mathrm{security}}
\gg
\lambda_{\mathrm{UI}}.
$$

代表 security domain 被細看，UI domain 只保持粗略。

這是合法 global observation。

---

# 7. 所以 Global Observer 不需要同步解析度

$$
\boxed{
\lambda_i
\neq
\lambda_j
}
$$

是正常狀態。

---

# 8. 下行映射

定義：

$$
\boxed{
\mathcal O_{\downarrow}^{q,t,B}
:
\widehat W_t
\rightarrow
\mathcal F_t
}
$$

其中：

$$
\mathcal F_t
$$

是被 active differentiated 的 frontier。

---

# 9. 下行輸出不是所有細節

而是：

$$
\boxed{
\mathcal F_t
=
\{D_i,S_{ij},x_{ijk},U_i\}.
}
$$

只展開當下值得展開的部分。

---

# 10. 下行的第一步：找 Resolution Debt

定義：

$$
Debt_R(D_i).
$$

若當前解析度不足以支持：

- prediction；
- intervention；
- verification；
- safe decision；

則：

$$
Debt_R(D_i)>0.
$$

---

# 11. 下行的第二步：Differentiation

對 cell：

$$
C
$$

找：

$$
C
\rightarrow
\{C_1,\ldots,C_k\}.
$$

---

# 12. Split 不等於 Truth

一個 observer 可以錯拆。

所以：

$$
\boxed{
\text{Split}
\neq
\text{Ontological Discovery}.
}
$$

需要外部 validation。

---

# 13. Split Gain

定義候選：

$$
\boxed{
G_{\mathrm{split}}
=
Perf(C_1,\ldots,C_k)
-
Perf(C).
}
$$

若：

$$
G_{\mathrm{split}}>0
$$

且可重複，split 才較有支持。

---

# 14. 過度 split

如果：

$$
G_{\mathrm{split}}\approx0
$$

但：

$$
Cost\uparrow,
$$

可能是 fragmentation。

---

# 15. 下行的第三步：Boundary Discovery

新 cell 需要：

$$
\partial C_i.
$$

不能只說：

> 這是一類。

還要知道：

> 到哪裡不再是一類。

---

# 16. Boundary 可能由條件決定

$$
\partial C_i
=
\partial C_i(\theta).
$$

條件改變，boundary 可移動。

---

# 17. 下行的第四步：Domainization

當 cell family 共享：

- state semantics；
- representation；
- transition law；
- verification regime；

才可能形成：

$$
D_i.
$$

---

# 18. Domainization 不等於命名

AI 把東西叫做：

> Domain X

沒有證據力。

真正需要：

$$
\boxed{
\text{computationally distinct regime}.
}
$$

---

# 19. Domain Criterion

第一版：

$$
\boxed{
\mathsf{Domain}(X)
=
1
}
$$

若存在相對穩定：

$$
(State,Rep,Law,Boundary,Verifier)
$$

組合。

---

# 20. 上行映射

定義：

$$
\boxed{
\mathcal O_{\uparrow}^{q,t,B}
:
\mathcal X_t
\rightarrow
\widehat W_{t+1}.
}
$$

其中：

$$
\mathcal X_t
$$

是 local objects / relations / domains。

---

# 21. 上行第一步：Grouping

不是先找名字。

而是找：

$$
\boxed{
\text{shared relevant invariants}.
}
$$

---

# 22. Grouping Relation

對：

$$
x_i,x_j
$$

定義：

$$
x_i\sim_{O,q,\lambda,t}x_j.
$$

只表示：

> 在此 task-resolution 下可共同處理。

---

# 23. Grouping 不要求全等

$$
x_i\sim x_j
$$

不代表：

$$
x_i=x_j.
$$

---

# 24. Contextual Equivalence Class

可形成：

$$
[x]_{O,q,\lambda,t}.
$$

這是 observer-relative class。

---

# 25. Class 不是永久身份

當：

$$
q
$$

或：

$$
\lambda
$$

改變，

class 可能裂開。

---

# 26. 上行第二步：Relation Formation

集合間需要：

$$
R_{ij}.
$$

---

# 27. Relation 可能是

- causal；
- statistical；
- semantic；
- structural；
- temporal；
- resource；
- dependency；
- compatibility。

不能全部壓成同一 edge type。

---

# 28. Typed Relation

$$
\boxed{
R_{ij}
=
(type,scope,condition,confidence,provenance).
}
$$

---

# 29. 上行第三步：Bridge

如果：

$$
D_i\neq D_j,
$$

不能只靠 relation merge。

需要：

$$
B_{ij}.
$$

---

# 30. Bridge 是計算契約

至少包含：

$$
\boxed{
B_{ij}
=
(
Input,
Output,
Validity,
Loss,
Uncertainty,
Certificate
).
}
$$

---

# 31. Bridge Loss

定義：

$$
\boxed{
L_{\mathrm{bridge}}(B_{ij}).
}
$$

表示跨域轉換時無法保留的相關結構。

---

# 32. 無損 bridge 不應預設存在

$$
L_{\mathrm{bridge}}=0
$$

是強條件。

---

# 33. 上行第四步：Glue

如果多域：

$$
D_1,\ldots,D_n
$$

需要形成 world state：

$$
W,
$$

則進行：

$$
\boxed{
\mathsf{Glue}(D_1,\ldots,D_n).
}
$$

---

# 34. Glue 不等於 union

$$
W
\neq
D_1\cup\cdots\cup D_n
$$

一般成立。

因為世界還需要：

- cross-domain constraints；
- shared history；
- consistency；
- bridge semantics；
- unresolved interfaces。

---

# 35. Glue Debt

定義：

$$
\boxed{
Debt_G(W)
}
$$

表示局部結果尚未全域一致整合的未清義務。

---

# 36. Local Complete 不等於 Global Complete

即使：

$$
\forall i,\quad
Q(D_i)\approx1,
$$

也可能：

$$
Debt_G(W)\gg0.
$$

---

# 37. 這是 Series C 的關鍵

AI 能把每一科都答對，

仍不表示：

$$
\boxed{
\text{Global Observer}.
}
$$

---

# 38. Partition

定義 observer partition：

$$
\boxed{
\mathcal P_{O,q,t}(W)
=
\{C_1,\ldots,C_n,U\}.
}
$$

---

# 39. $U$ 的意義

$$
U
$$

保存：

- unclassified；
- ambiguous；
- unseen；
- unresolved；
- boundary debt。

---

# 40. 完美分類不是目標

強迫：

$$
U=\varnothing
$$

可能導致 premature closure。

---

# 41. Unresolved Preservation Principle

$$
\boxed{
\text{Unknown correctly preserved}
>
\text{Unknown falsely classified}.
}
$$

---

# 42. Collapse Loss

若：

$$
x\not\equiv y
$$

卻被同一 cell 處理，

定義：

$$
\boxed{
L_{\mathrm{collapse}}.
}
$$

---

# 43. Collapse Loss 的後果

可能造成：

- prediction bias；
- hidden subgroup failure；
- wrong theorem scope；
- wrong medical grouping；
- wrong software abstraction。

---

# 44. Fragmentation Loss

若：

$$
x\sim_q y
$$

卻被不必要地拆分，

定義：

$$
\boxed{
L_{\mathrm{fragment}}.
}
$$

---

# 45. Fragmentation 的後果

- compute cost；
- model complexity；
- maintenance；
- sample inefficiency；
- duplicated reasoning。

---

# 46. Observer 最佳化不是單一 loss 最小

而是：

$$
\boxed{
\min
\left[
\alpha L_{\mathrm{collapse}}
+
\beta L_{\mathrm{fragment}}
+
\gamma Cost
\right].
}
$$

權重依 task / risk 而變。

---

# 47. High-Risk Domain

例如 medical safety：

$$
\alpha\gg\beta.
$$

寧願多分，也不要錯合。

---

# 48. Low-Risk Compression Domain

例如 UI theme clustering：

$$
\beta
$$

可相對提高。

---

# 49. 所以 Observer Resolution 本質是政策函數

$$
\boxed{
\Pi^\ast
=
\arg\min_{\Pi}
RiskLoss(\Pi,q,B).
}
$$

---

# 50. 但不能把 observer 變成純 optimization slogan

真正難點是：

$$
RiskLoss
$$

本身常不知道。

所以 observer 必須探索。

---

# 51. Active Observation

AI 可以：

$$
\boxed{
\text{observe}
\rightarrow
\text{uncertainty}
\rightarrow
\text{choose next observation}.
}
$$

這是 global observer loop 的重要入口。

---

# 52. 下一個 observation 也可以改變 partition

$$
\mathcal P_t
\neq
\mathcal P_{t+1}.
$$

---

# 53. Repartition

定義：

$$
\boxed{
\mathsf{Repartition}
:
\mathcal P_t
\times
E_{t+1}
\rightarrow
\mathcal P_{t+1}.
}
$$

---

# 54. 穩定 observer 不是永遠不改分類

而是：

$$
\boxed{
\text{change when evidence justifies change}.
}
$$

---

# 55. Reprojection

完成下行與上行後：

$$
\widehat W_t
\rightarrow
\mathcal F_t
\rightarrow
\widehat W_{t+1}.
$$

---

# 56. Reprojection Error

若沒有新 evidence，只測結構穩定：

$$
\boxed{
E_{\mathrm{reproj}}
=
d(
\widehat W_t,
\mathcal O_{\uparrow}
(
\mathcal O_{\downarrow}
(
\widehat W_t
)
)
).
}
$$

---

# 57. $E_{\mathrm{reproj}}$ 高代表

可能：

- decomposition loss；
- bad bridge；
- overcompression；
- inconsistent gluing；
- missing provenance。

---

# 58. 但有新 evidence 時不能這樣判

若：

$$
E_{new}
$$

改變 world model，

則：

$$
\widehat W_{t+1}\neq\widehat W_t
$$

可能是正確。

---

# 59. Legitimate Revision

定義：

$$
\boxed{
\Delta_W^{legit}
}
$$

表示由新 evidence 合法支持的 world revision。

---

# 60. 所以真正 Error

$$
\boxed{
E_{\mathrm{dual}}
=
E_{\mathrm{reproj}}
-
\Delta_W^{legit}
}
$$

僅為概念關係，不是實際可直接相減的標準量。

---

# 61. Provenance-aware Reprojection

每次：

$$
\widehat W_t
\rightarrow
\widehat W_{t+1}
$$

必須能追蹤：

- new evidence；
- changed partition；
- changed bridge；
- changed boundary；
- changed confidence。

---

# 62. Observer History

定義：

$$
\boxed{
\mathcal H_O
=
\{
\mathcal P_0,
\mathcal P_1,
\ldots,
\mathcal P_t
\}.
}
$$

---

# 63. 忘記舊 partition 會失去什麼？

會失去：

- why split；
- why merge；
- failed taxonomy；
- observer bias history；
- regression audit。

---

# 64. 因此 observer 也需要版本控制

$$
\boxed{
O_t
\rightarrow
O_{t+1}
}
$$

是可版本化的。

---

# 65. Dual Observer Closure

本文提出：

$$
\boxed{
\mathsf{DOC}(O,W,q,t)
}
$$

作為對偶觀察閉包狀態。

---

# 66. DOC 條件一：Downward Reach

global constraints 可下傳至 relevant local domains。

---

# 67. DOC 條件二：Upward Return

local updates 能回寫 world state。

---

# 68. DOC 條件三：Unresolved Preservation

未知不被非法消除。

---

# 69. DOC 條件四：Bridge Accountability

每個跨域作用可追蹤。

---

# 70. DOC 條件五：Glue Accountability

全域黏合 debt 可見。

---

# 71. DOC 條件六：Revision Provenance

world revision 有來源。

---

# 72. DOC 不是 Final Closure

$$
\boxed{
\mathsf{DOC}
\neq
\text{World Completely Known}.
}
$$

它只是 observer loop 當下可正常閉合。

---

# 73. Relative Closure

所以：

$$
\boxed{
\text{Closure}
=
\text{relative operational closure}.
}
$$

---

# 74. 世界可以重新開啟

新 evidence：

$$
E'
$$

可：

$$
\mathsf{DOC}\rightarrow\mathsf{OPEN}.
$$

---

# 75. 這接 Dynamic Fixed-Point Mathematics

穩定不是永遠不變。

而是：

$$
\boxed{
\text{stable identity under revisable structure}.
}
$$

---

# 76. Scale Traversal

本文提出：

$$
\boxed{
T_S
=
\text{ability to move across computational scales}.
}
$$

---

# 77. Scale 不只 spatial

包括：

- spatial；
- temporal；
- semantic；
- probabilistic；
- causal；
- organizational；
- abstraction；
- proof；
- resource。

---

# 78. Semantic Zoom

例如：

$$
token
\rightarrow
phrase
\rightarrow
meaning
\rightarrow
strategy
\rightarrow
goal.
$$

---

# 79. Temporal Zoom

例如：

$$
ms
\rightarrow
s
\rightarrow
day
\rightarrow
year.
$$

---

# 80. Causal Zoom

例如：

$$
local\ interaction
\rightarrow
mechanism
\rightarrow
systemic\ effect.
$$

---

# 81. Domain Zoom

例如：

$$
software
\rightarrow
security
\rightarrow
auth
\rightarrow
token\ rotation.
$$

---

# 82. Scale Traversal Failure

AI 若只能固定 scale 工作：

$$
T_S\ll1.
$$

---

# 83. Zoom-in Failure

看得到宏觀趨勢，

卻找不到局部 causal mechanism。

---

# 84. Zoom-out Failure

看得到很多 details，

卻不知道它們對 world state 有何意義。

---

# 85. 全域 observer 要能切換

$$
\boxed{
\lambda(t+1)
=
\mathsf{RouteResolution}
(
q,
Risk,
Evidence,
Debt,
Budget
).
}
$$

---

# 86. Resolution Routing

不是手工 rule table。

理想上 AI 自行學會：

> 現在該看哪裡。

---

# 87. Attention 與 Resolution 不同

$$
\boxed{
\text{Attention}
\neq
\text{Resolution}.
}
$$

可以高度注意某 domain，但仍用粗粒度模型。

---

# 88. Materialization 與 Resolution 也不同

$$
\boxed{
\text{Materialized}
\neq
\text{High Resolution}.
}
$$

---

# 89. Compute Resolution 與 Observe Resolution

承接 GCM：

$$
\lambda^{compute}
\neq
\lambda^{observe}.
$$

---

# 90. AI 可以粗看、細算

某 hidden solver：

$$
\lambda^{compute}\gg\lambda^{observe}.
$$

---

# 91. 也可以細看、粗算

例如 anomaly inspection：

$$
\lambda^{observe}\gg\lambda^{compute}.
$$

---

# 92. 所以雙向 observer 需要多 resolution state

不能只用 single embedding resolution。

---

# 93. World-to-Individual Path

正式寫：

$$
\boxed{
\widehat{\Omega}
\xrightarrow{\Pi_W}
W
\xrightarrow{\Pi_D}
D_i
\xrightarrow{\Pi_S}
S_{ij}
\xrightarrow{\Pi_x}
x_{ijk}.
}
$$

---

# 94. Individual-to-World Path

$$
\boxed{
x_{ijk}
\xrightarrow{\Gamma_S}
S_{ij}
\xrightarrow{\Gamma_D}
D_i
\xrightarrow{\Gamma_W}
W
\xrightarrow{\Gamma_\Omega}
\widehat{\Omega}.
}
$$

---

# 95. $\Pi$ 與 $\Gamma$ 不必互逆

$$
\Gamma\circ\Pi
\neq I
$$

是正常情況。

---

# 96. 什麼時候近似互逆？

若：

- information loss 小；
- ontology stable；
- no new evidence；
- bridge reversible；
- resolution preserved。

才可能：

$$
\Gamma\circ\Pi
\approx I.
$$

---

# 97. Irreversible Observation

有些 aggregation 一旦壓縮就無法重建。

例如：

$$
\{x_i\}
\rightarrow
mean.
$$

只保存 mean，原始分布丟失。

---

# 98. 所以 observer 要管理 compression irreversibility

$$
\boxed{
L_{\mathrm{irreversible}}.
}
$$

---

# 99. 可逆性不是永遠必要

若 task 不需要原 detail，壓縮可以合法。

---

# 100. 但必須知道自己不可逆

這是 observer epistemic responsibility。

---

# 101. World Model 不應假裝 Full Fidelity

$$
\boxed{
\widehat W
=
\text{compressed observer state}.
}
$$

---

# 102. Global Observer 的一項能力：Know the Compression

AI 應能回答：

> 我在哪些地方做了 approximation？

---

# 103. 另一項：Know the Missing Detail

> 若要提高信心，需要展開哪一區？

---

# 104. 這就是眼睛的聚焦

不是像素 focus，

而是：

$$
\boxed{
\text{epistemic-computational focus}.
}
$$

---

# 105. Dual Loss Vector

本文定義：

$$
\boxed{
\mathbf L_O
=
(
L_c,
L_f,
L_b,
L_g,
L_r
).
}
$$

其中：

- $L_c$：collapse；
- $L_f$：fragmentation；
- $L_b$：bridge；
- $L_g$：glue；
- $L_r$：reprojection。

---

# 106. Observer Quality Vector

$$
\boxed{
\mathbf Q_O
=
(
Q_d,
Q_c,
Q_b,
Q_g,
Q_r,
Q_h
).
}
$$

分別是 differentiation、composition、bridge、glue、reprojection、history。

---

# 107. 全域觀察不能用單一 accuracy

因為：

$$
Accuracy
$$

可能高，

但：

$$
L_g
$$

也很高。

---

# 108. 例如

AI 對每個 department prediction 都準，

但 company-level strategic model 錯。

---

# 109. Local Correctness / Global Wrongness

定義：

$$
\boxed{
\forall i,\quad
Perf(D_i)\uparrow
\quad
\not\Rightarrow
\quad
Perf(W)\uparrow.
}
$$

---

# 110. Global Correctness / Local Blindness

反過來也可能：

總體預測準，

但對 minorities / edge cases 完全錯。

---

# 111. 所以兩方向需要互相校驗

$$
\boxed{
\mathcal O_{\downarrow}
\leftrightarrow
\mathcal O_{\uparrow}
}
$$

不是美學對稱，而是 error control。

---

# 112. Top-Down Constraint

Global model 可限制 local interpretation。

---

# 113. Bottom-Up Counterexample

Local anomaly 可推翻 global model。

---

# 114. 真正 Global Observer 必須允許局部反例向上傳播

否則是：

$$
\boxed{
\text{global dogmatism}.
}
$$

---

# 115. 也必須允許全域 constraint 阻止局部過擬合

否則是：

$$
\boxed{
\text{local fragmentation}.
}
$$

---

# 116. 對偶觀察的控制思想

因此：

$$
\boxed{
\text{Top-down regularization}
+
\text{Bottom-up correction}.
}
$$

---

# 117. 自發 Domain Formation

未來重要事件之一：

AI 在沒有 taxonomy hint 時：

$$
\{x_i\}
\rightarrow
\{D_j\}.
$$

---

# 118. 自發 Domain Dissolution

同樣重要：

AI 發現：

$$
D_j
$$

其實沒有必要，

於是 merge / dissolve。

---

# 119. Domain Formation 不應只增不減

成熟 observer 需要：

$$
\boxed{
\text{split}
+
\text{merge}
+
\text{relabel}
+
\text{retire}.
}
$$

---

# 120. Domain Lifecycle

$$
\boxed{
Potential
\rightarrow
Candidate
\rightarrow
Active
\rightarrow
Stable
\rightarrow
Revised
\rightarrow
Retired.
}
$$

---

# 121. 這使 Domain 本身成為動態物件

不是固定 ontology node。

---

# 122. World 本身也是動態物件

$$
W_t\neq W_{t+1}.
$$

---

# 123. Observer 與 World Co-Evolution

$$
\boxed{
O_t,W_t
\rightarrow
O_{t+1},W_{t+1}.
}
$$

---

# 124. 這裡不能偷換現實

AI world model 改變：

$$
\widehat W_t\rightarrow\widehat W_{t+1}
$$

不代表 reality：

$$
W^{real}
$$

被改變。

---

# 125. 只有 action / external dynamics 才改變 real world

保持：

$$
\boxed{
\text{Model Revision}
\neq
\text{Reality Transition}.
}
$$

---

# 126. 如果 AI 有 action

則：

$$
\widehat W_t
\rightarrow
a_t
\rightarrow
W_{t+1}^{real}
\rightarrow
O_{t+1}.
$$

這將在後續 world closure 中更重要。

---

# 127. Series C 不先假定 physical realism

同一方法可用於：

- software world；
- legal world；
- game world；
- research world；
- simulated world；
- physical world。

---

# 128. World Boundary 必須聲明

$$
\boxed{
\partial W
}
$$

不清楚，就不能談 global。

---

# 129. 所以 Global 是 relative

$$
\boxed{
\text{Global}(W)
}
$$

不是宇宙級絕對詞。

---

# 130. 全域 AI 的 local-global duality

一個 AI 可以在：

$$
W_1
$$

接近 global observer，

在：

$$
W_2
$$

仍非常局部。

---

# 131. Domain-Specific Globality

所以：

$$
G_O(A,W_1)\neq G_O(A,W_2).
$$

---

# 132. 這也支持 C01 的光譜觀

Globality 是 profile，不是 badge。

---

# 133. 脈衝式 Duality

某次 run：

$$
g_{\downarrow}\uparrow,
g_{\uparrow}\uparrow.
$$

下一次又下降。

---

# 134. 所以要測 Repeatability

$$
\boxed{
P(
\mathsf{DOC}=1
\mid
W,q
).
}
$$

---

# 135. Regime 需要穩定往返

不是只一次漂亮 decomposition。

---

# 136. C02 實驗原型：Bidirectional World Reconstruction Test

給 AI：

$$
W_{partial}.
$$

---

# 137. Step A

先讓它建立：

$$
\widehat W_0.
$$

---

# 138. Step B

要求它自行決定哪些部分需要展開。

記錄：

$$
\mathcal O_{\downarrow}.
$$

---

# 139. Step C

注入 local anomalies。

看是否：

$$
\mathcal O_{\uparrow}
$$

能修改 world model。

---

# 140. Step D

要求重新壓縮成 global operational state。

---

# 141. Step E

測：

- prediction；
- intervention；
- consistency；
- compression；
- provenance。

---

# 142. Ablation 1：固定 taxonomy

禁止 AI 改分類。

---

# 143. Ablation 2：允許自建 taxonomy

比較：

$$
Perf_{\mathrm{fixed}}
$$

與：

$$
Perf_{\mathrm{adaptive}}.
$$

---

# 144. Ablation 3：禁止 bottom-up world revision

看 local anomalies 是否被 global model 吞掉。

---

# 145. Ablation 4：禁止 top-down constraint

看是否 fragmentation。

---

# 146. 核心觀測量一

$$
\boxed{
R_{\downarrow}
=
\text{relevant differentiation recall}.
}
$$

---

# 147. 核心觀測量二

$$
\boxed{
P_{\downarrow}
=
\text{differentiation precision}.
}
$$

---

# 148. 核心觀測量三

$$
\boxed{
G_{\uparrow}
=
\text{valid composition gain}.
}
$$

---

# 149. 核心觀測量四

$$
\boxed{
C_{\mathrm{glue}}
=
\text{world coherence after integration}.
}
$$

---

# 150. 核心觀測量五

$$
\boxed{
E_{\mathrm{reproj}}.
}
$$

---

# 151. 核心觀測量六

$$
\boxed{
Debt_G.
}
$$

---

# 152. 核心觀測量七

$$
\boxed{
U_{\mathrm{preserve}}.
}
$$

衡量 unresolved 是否被合法保留。

---

# 153. 成功條件

真正 high-quality dual observer 應同時：

$$
L_c\downarrow,
$$

$$
L_f\downarrow,
$$

$$
L_b\downarrow,
$$

$$
L_g\downarrow,
$$

並保持：

$$
Cost
$$

可接受。

---

# 154. 不能靠 brute-force

若：

$$
Cost\rightarrow\infty,
$$

則不構成有效 global observer。

---

# 155. Bounded Computation Principle

$$
\boxed{
\text{Globality under finite active realization}.
}
$$

延續 GCM。

---

# 156. 這裡開始看到 AI-native 優勢

人類工作記憶很難同時維持：

- 多尺度；
- 多域；
- 多版本；
- 多 bridge；
- unresolved mass；
- history。

---

# 157. AI 可能比較適合做往返

不是因為 AI 天生全知，

而是：

$$
\boxed{
\text{parallel state maintenance}
+
\text{reprojection}
+
\text{persistent memory}
}
$$

可以工程化。

---

# 158. 但 2026 仍不能假定已成熟

目前多數 Agent：

- context 有限；
- memory 不穩；
- taxonomy 常由 task 給定；
- world model 常為局部；
- self-repartition 不穩定。

---

# 159. 所以 C02 是測量骨架，不是現況宣告

---

# 160. 由世界到個體的真正意義

不是「宏觀變微觀」。

而是：

$$
\boxed{
\text{find the next difference that matters}.
}
$$

---

# 161. 由個體到世界的真正意義

不是「小東西堆成大東西」。

而是：

$$
\boxed{
\text{find the next structure that remains coherent after composition}.
}
$$

---

# 162. 兩者共同構成 Global Seeing

$$
\boxed{
\text{Seeing}
=
\text{Differentiating}
+
\text{Composing}.
}
$$

---

# 163. 更完整：

$$
\boxed{
\text{Seeing}
=
\text{Differentiate}
+
\text{Bound}
+
\text{Relate}
+
\text{Bridge}
+
\text{Glue}
+
\text{Revise}.
}
$$

---

# 164. 這不是人類視覺隱喻而已

它是一個可以實際測：

- decomposition；
- compression；
- transfer；
- world-model revision；

的 computational program。

---

# 165. C02 第一核心命題

$$
\boxed{
\text{Global Observation requires bidirectional scale traversal}.
}
$$

---

# 166. C02 第二核心命題

$$
\boxed{
\text{Differentiation without composition fragments;
composition without differentiation collapses}.
}
$$

---

# 167. C02 第三核心命題

$$
\boxed{
\text{Observer partitions are operational,
conditional, and revisable}.
}
$$

---

# 168. C02 第四核心命題

$$
\boxed{
\mathcal O_{\uparrow}
\circ
\mathcal O_{\downarrow}
\neq
I
}
$$

一般成立。

---

# 169. C02 第五核心命題

$$
\boxed{
\text{Reprojection mismatch may be error or legitimate learning}.
}
$$

需要 provenance 區分。

---

# 170. C02 第六核心命題

$$
\boxed{
\text{Global coherence is not the same as global compression}.
}
$$

可以壓縮很多，但仍錯。

---

# 171. C02 第七核心命題

$$
\boxed{
\text{Unknown preservation is part of observer quality}.
}
$$

---

# 172. C02 第八核心命題

$$
\boxed{
\text{Global observer intelligence is partly the quality of moving between scales}.
}
$$

---

# 173. 與 C03 的橋

C02 尚未回答：

> 差異究竟如何形成 identity、集合、非交集與 domain？

這由 C03 處理。

---

# 174. 與 C04 的橋

C02 尚未回答：

> 跨域 bridge 何時合法？

這由 C04 處理。

---

# 175. 與 C05 的橋

C02 把 uncertainty 保留成 state。

C05 將把 probability / uncertainty 自身 domainize。

---

# 176. 與 C06 的橋

C02 建立雙向 observer traversal。

C06 將進一步建立：

$$
\text{Expand}
\rightarrow
\text{Link}
\rightarrow
\text{Converge}.
$$

---

# 177. 與 C09 的橋

C02 的真正強測試必須：

> 不告訴 AI 應該怎麼切。

這將成為 Methodology-Blind Globality。

---

# 178. 與 C10 的橋

未來要找的是：

$$
\boxed{
\mathcal O_{\downarrow}
\leftrightarrow
\mathcal O_{\uparrow}
}
$$

何時從偶發事件變成穩定 regime。

---

# 結論

C01 說：

> AI 需要先有眼睛。

C02 則開始回答：

> 這隻眼睛怎麼動？

它不是固定焦距。

不是永遠看宏觀。

也不是永遠看局部。

它必須從世界往下：

$$
\widehat{\Omega}
\rightarrow
W
\rightarrow
D
\rightarrow
S
\rightarrow
x,
$$

找到真正值得保留的差異。

然後再從局部往上：

$$
x
\rightarrow
S
\rightarrow
D
\rightarrow
W
\rightarrow
\widehat{\Omega},
$$

找到真正能維持一致的高階結構。

真正困難的不是任一方向單獨完成。

而是反覆往返：

$$
\boxed{
\widehat W_t
\rightarrow
\mathcal O_{\downarrow}
\rightarrow
\{D_i\}
\rightarrow
\mathcal O_{\uparrow}
\rightarrow
\widehat W_{t+1}.
}
$$

並且知道：

- 哪些差異被壓縮；
- 哪些 domain 被拆分；
- 哪些 bridge 有損；
- 哪些局部尚未黏合；
- 哪些 unknown 仍然存在；
- 哪些 world revision 來自新 evidence。

因此本文對 Global Observer 的第二階段定義可以濃縮成：

> **全域觀察不是站在最高處看全部，而是在全域與局部之間持續改變解析度，同時不丟掉世界的一致性。**

或者更形式地：

$$
\boxed{
\text{Global without flattening}
\quad+\quad
\text{Local without fragmentation}.
}
$$

這就是全域觀察對偶計算的最低要求。

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **《全域系統世界：從物理宇宙到類終極世界的廣義定義》**, GSWUE-01, 2026.
3. Neo.K, **《分域算子本體論：從萬物皆算子到合法作用》**, 2026.
4. Neo.K with Aletheia, **《多域知識判定論》**, DEST-01, 2026.
5. Neo.K with Aletheia, **Global Computation Methodology Series**, 2026.
6. Neo.K with Aletheia, **WDC-08｜三生世界域計算**, 2026.
7. Neo.K with Aletheia, **PNCW Paper 05｜全域計算、局部顯現**, 2026.
8. Neo.K with Aletheia, **《數學研究空間方法論》**, 2026.
9. Neo.K, **《原生可計算數學》**, 2026.
10. Neo.K with Aletheia, **Dynamic Fixed-Point Mathematics Foundational Series**, 2026.

## 理論對照

本文與 multi-scale modeling、hierarchical state representation、coarse-graining、renormalization、abstraction、sheaf-like gluing、graph partitioning、active perception、world models、representation learning 等既有思想存在結構對照，但不宣稱本文的 Dual Observer Computation 等同於任何單一既有數學框架。

本文的特殊研究焦點是：

$$
\boxed{
\text{AI 自主調整觀察解析度與 domain structure 的全域認知能力}.
}
$$

---

# Series C Roadmap

## C01
**AI 需要先有眼睛：全域觀察者維度的定義**

## C02
**由世界到個體、由個體到世界：全域觀察的對偶計算**

## C03
**差異先於分類：從歧義個體、集合與非交集到計算域**

## C04
**分域算子世界：合法作用、跨域橋接與世界組合**

## C05
**概率也有域：不確定性、混沌、不可判定與世界預測包絡**

## C06
**全域展開、連結與收斂：類全域觀察者的核心計算循環**

## C07
**一句話不是魔法：Sparse Intent 與 Project-World Cognition**

## C08
**從完成任務到負責一個域：長時空 Agent Stewardship**

## C09
**不准考 Neo.K：方法論盲測與全域 AI 觀測器**

## C10
**眼睛何時睜開：全域觀察者相變、脈衝與 AI 原生世界計算**

---

**End of C02**
