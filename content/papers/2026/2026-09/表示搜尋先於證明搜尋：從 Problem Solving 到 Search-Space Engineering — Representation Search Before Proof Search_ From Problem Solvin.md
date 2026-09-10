# 表示搜尋先於證明搜尋：從 Problem Solving 到 Search-Space Engineering
## Representation Search Before Proof Search: From Problem Solving to Search-Space Engineering

**系列：** AI 原生數學與耦合求解（AI-Native Mathematics and Coupled Solution Dynamics, ANMCS）  
**系列編號：** Series A / Paper 03 of 07  
**文件編號：** EML-ANMCS-A03-2026-v0.1  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09  
**性質：** General Theory / Representation Search / Search-Space Engineering / AI-Native Mathematics  
**狀態：** FOUNDATIONAL THEORY DRAFT  
**直接前置：** A02〈跨基質數學複雜度：Human-Hard 不等於 Mathematically-Hard〉  
**直接後續：** A04〈遞迴測地超連結理論〉

---

# 摘要

傳統數學求解流程通常隱含：

$$
\boxed{
\text{Problem}
\rightarrow
\text{Fixed Representation}
\rightarrow
\text{Proof Search}.
}
$$

在這個框架中，問題的表示 $r$ 被視為已給定，而主要智力工作發生在：

$$
\boxed{
\pi
=
\text{proof / solution path}.
}
$$

A02 已建立跨基質數學複雜度：

$$
C(P;s,r,m),
$$

並指出同一問題 $P$ 在不同 substrate $s$ 、representation $r$ 與 method $m$ 下，可以具有完全不同的有效求解成本。

由此本文提出：

$$
\boxed{
\text{Representation}
}
$$

不應再只是求解問題的背景條件，而應成為：

$$
\boxed{
\text{Search Variable}.
}
$$

因此更高階的求解問題不是：

$$
\boxed{
\min_{\pi}C(\pi\mid P,r),
}
$$

而是：

$$
\boxed{
\min_{r,m,\pi}
\left[
C_{\mathrm{repr}}(r)
+
C_{\mathrm{search}}(\pi\mid P,r,m)
+
C_{\mathrm{verify}}(\pi)
+
C_{\mathrm{translate}}(r)
\right].
}
$$

本文將此稱為：

$$
\boxed{
\text{Representation Search}.
}
$$

其核心命題為：

$$
\boxed{
\text{Before searching harder, search for a representation in which the problem becomes easier}.
}
$$

更進一步，本文提出：

$$
\boxed{
\text{Problem Solving}
\rightarrow
\text{Search-Space Engineering}.
}
$$

AI 的數學能力不只表現在於既有搜索空間中更快找到路徑，而可能表現在：

1. 重新定義狀態；
2. 改變坐標；
3. 重組依賴；
4. 建立新 invariant；
5. 創造新局部 ontology；
6. 合併等價狀態；
7. 消去無效自由度；
8. 建立跨層 shortcut；
9. 將原本巨大搜索空間轉換為低成本可導航結構。

若某表示變換：

$$
\Phi:
\mathcal S
\rightarrow
\mathcal S'
$$

使：

$$
C(P\mid\mathcal S')
\ll
C(P\mid\mathcal S),
$$

本文稱之為：

$$
\boxed{
\text{Representation Phase Transition}.
}
$$

本文不主張任意 NP-hard 問題都可以透過 representation rewrite 變成 polynomial-time solvable，也不主張表示改變可以免費繞過資訊論或計算複雜度下界。相反地，本文將 representation search cost 本身納入總成本，並強調：

$$
\boxed{
\text{Easy after transformation}
\neq
\text{Transformation was easy}.
}
$$

本文最後把 representation search 推進到下一個問題：

> 若一個表示不只降低成本，還能把底層最短路徑壓縮成高階邊，且在跨層壓縮中保持最短性，那麼表示便不再只是「寫法」，而成為一種可遞迴壓縮的路徑架構。

這就是 A04〈遞迴測地超連結理論〉的起點。

---

# 0. 生成與理論邊界聲明

本文是一篇 AI 輔助生成的理論研究稿。

本文不主張：

1. representation search 能解決所有 open problems；
2. 所有數學難題都只是表示錯配；
3. 任何表示改寫都保持 problem semantics；
4. representation rewrite 可以任意改變 classical complexity class；
5. AI 可以不付任何成本搜尋新表示；
6. 搜尋表示一定比搜尋 proof 更便宜；
7. 一個對 AI 有效的 representation 對人類也有效；
8. representation phase transition 等同正式 phase transition theorem；
9. search-space engineering 已成為成熟通用數學理論；
10. representation search 可取代 theorem proving；
11. 本文證明 $P=NP$ 或 $P\neq NP$ ；
12. 本文證明任何傳統 NP-hardness 都可被外部化；
13. 本文完成 A04 所需的 geodesic preservation 定理。

本文提出的是一個更弱、但可操作的元求解原則：

$$
\boxed{
\text{若 representation 是求解成本的重要變數，}
\text{則高階求解器應搜尋 representation，而不是永遠把它固定。}
}
$$

---

# 1. 傳統求解流程的隱藏固定點

許多數學與 AI benchmark 默認：

$$
P
$$

已經被寫成某個：

$$
r_0(P).
$$

接著求：

$$
\pi^\ast.
$$

即：

$$
\boxed{
\pi^\ast
=
\arg\min_{\pi}
C(\pi\mid r_0(P)).
}
$$

---

# 2. 但 $r_0$ 為什麼必須固定？

A02 已經指出：

$$
C(P;s,r_1,m)
\neq
C(P;s,r_2,m)
$$

完全可能成立。

因此固定 $r_0$ 其實是一個強假設。

---

# 3. Representation Search 的最低形式

令：

$$
\mathcal R(P)
$$

為問題 $P$ 的可接受表示族。

則：

$$
\boxed{
r^\ast
=
\arg\min_{r\in\mathcal R(P)}
C(P;s,r).
}
$$

---

# 4. 更完整形式

如果 method 也可變：

$$
\boxed{
(r^\ast,m^\ast)
=
\arg\min_{r,m}
C(P;s,r,m).
}
$$

---

# 5. 再把 proof path 加進來

$$
\boxed{
(r^\ast,m^\ast,\pi^\ast)
=
\arg\min_{r,m,\pi}
C(P;s,r,m,\pi).
}
$$

---

# 6. Representation Search 不是免費的

因此不能只比較：

$$
C_{\mathrm{solve}\mid r}.
$$

應該加入：

$$
C_{\mathrm{find}\;r}.
$$

---

# 7. 總成本

本文定義一個最小總成本：

$$
\boxed{
C_{\mathrm{total}}
=
C_{\mathrm{repr-search}}
+
C_{\mathrm{solve}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{translate}}
+
C_{\mathrm{store/update}}.
}
$$

---

# 8. Representation Search 只有在攤提後才可能划算

若：

$$
C_{\mathrm{repr-search}}
\gg
C_{\mathrm{solve}},
$$

但新表示可服務：

$$
N
$$

個問題，

平均成本：

$$
\boxed{
\bar C_{\mathrm{repr}}
=
\frac{
C_{\mathrm{repr-search}}
}{
N
}.
}
$$

---

# 9. 所以 representation discovery 具有 capital-like 性質

它像一項前置投資：

$$
\boxed{
\text{High Upfront Cost}
\rightarrow
\text{Low Future Marginal Cost}.
}
$$

---

# 10. 這與記憶編譯天然相接

一旦：

$$
r^\ast
$$

被發現並保存，

後續：

$$
P_1,P_2,\ldots
$$

可直接使用。

---

# 11. Representation 是歷史資產

因此：

$$
\boxed{
r_t^\ast
}
$$

不是一次性結果，

而可以成為：

$$
\boxed{
\text{Compiled Mathematical Memory}.
}
$$

---

# 12. Proof Search 與 Representation Search 的層級差異

Proof Search 問：

> 在這個世界裡怎麼走？

Representation Search 問：

> 是否應該先換一個世界描述？

---

# 13. 更精確

Proof Search：

$$
\boxed{
\text{Find a path in }G.
}
$$

Representation Search：

$$
\boxed{
\text{Find }G'\text{ in which the path is easier}.
}
$$

---

# 14. 這就是第一次超越 brute force

如果 AI 只是在：

$$
G
$$

裡每秒多試：

$$
10^6
$$

條路，

仍是：

$$
\boxed{
\text{Faster Search}.
}
$$

---

# 15. 真正 AI-native 的更高階能力

可能是：

$$
\boxed{
G
\rightarrow
G'.
}
$$

使：

$$
\operatorname{diam}(G')
\ll
\operatorname{diam}(G)
$$

或：

$$
|\operatorname{RelevantPaths}(G')|
\ll
|\operatorname{RelevantPaths}(G)|.
$$

---

# 16. Search-Space Engineering

本文將：

$$
\boxed{
\text{Search-Space Engineering}
}
$$

定義為：

> 主動改寫問題的可操作狀態、關係、坐標、等價類、依賴與路徑結構，使後續求解成本降低，同時保留所需語義與驗證條件。

---

# 17. Search-Space Engineering 不是作弊

只要：

$$
\boxed{
\operatorname{Sem}(P)
\equiv
\operatorname{Sem}(\Phi(P))
}
$$

在指定問題語義下成立，

改表示是合法求解的一部分。

---

# 18. 但 semantic preservation 必須驗證

若：

$$
\Phi(P)
$$

偷偷改了問題，

則成本下降沒有意義。

---

# 19. Fidelity Constraint

本文要求：

$$
\boxed{
\operatorname{Fid}(P,\Phi(P))=1.
}
$$

---

# 20. 形式化不代表自動 fidelity

即使：

$$
\Phi(P)
$$

可被 proof assistant 接受，

也要確認：

$$
\boxed{
\text{Formal Correctness}
\neq
\text{Problem Fidelity}.
}
$$

---

# 21. Representation Search 的基本操作族

可包含：

$$
\mathcal O_R
=
\{
\mathsf{recode},
\mathsf{quotient},
\mathsf{embed},
\mathsf{factor},
\mathsf{lift},
\mathsf{project},
\mathsf{dualize},
\mathsf{compile},
\mathsf{compress},
\mathsf{reindex}
\}.
$$

---

# 22. Recode

改變表示編碼：

$$
r_1\rightarrow r_2.
$$

---

# 23. Quotient

把等價狀態：

$$
x\sim y
$$

合併為：

$$
[x].
$$

---

# 24. Embed

把問題嵌入另一個空間：

$$
P
\hookrightarrow
P'.
$$

---

# 25. Factor

把：

$$
P
$$

拆成：

$$
P_1,\ldots,P_k.
$$

---

# 26. Lift

把低層問題提升到高層 representation。

---

# 27. Project

把高維結構投影到可操作低維視圖。

---

# 28. Dualize

換成對偶問題。

---

# 29. Compile

把昂貴歷史推理轉成：

$$
\boxed{
\text{fast path}.
}
$$

---

# 30. Compress

把長路徑／依賴壓成可重用高階單元。

---

# 31. Reindex

重新建立：

- state ID；
- theorem ID；
- relation index；
- semantic neighborhoods。

---

# 32. Representation Search 的本質

不是找：

> 最漂亮 representation。

而是找：

$$
\boxed{
\text{task-appropriate representation}.
}
$$

---

# 33. Task-Relative Representation

對：

$$
P_1
$$

最佳的：

$$
r^\ast_1
$$

不一定對：

$$
P_2
$$

最佳。

---

# 34. 所以不存在必然唯一 universal best representation

$$
\boxed{
r^\ast(P_1)
\neq
r^\ast(P_2)
}
$$

一般成立。

---

# 35. Representation Portfolio

成熟 AI 可以維護：

$$
\boxed{
\mathcal R^\ast
=
\{
r_1^\ast,\ldots,r_k^\ast
\}.
}
$$

---

# 36. 表示切換本身是能力

令：

$$
\operatorname{Switch}(r_i,r_j)
$$

具有成本：

$$
C_{\mathrm{switch}}.
$$

---

# 37. 太多表示也可能有負擔

如果：

$$
|\mathcal R^\ast|
\rightarrow
\text{large},
$$

會增加：

- indexing；
- translation；
- consistency；
- storage。

---

# 38. 因此 representation diversity 需要管理

不是：

$$
\boxed{
\text{more representations always better}.
}
$$

---

# 39. Representation Selection

給定：

$$
P,
$$

系統要先估計：

$$
\boxed{
\operatorname{Score}(r_i\mid P).
}
$$

---

# 40. Score 可包含

$$
\boxed{
J(r_i)
=
(
C_S,
C_V,
C_T,
C_M,
C_U
).
}
$$

其中：

- $C_S$：solve cost；
- $C_V$：verification cost；
- $C_T$：translation cost；
- $C_M$：memory cost；
- $C_U$：update cost。

---

# 41. Pareto Representation

因此最優 representation 可能是：

$$
\boxed{
\text{Pareto-optimal}.
}
$$

---

# 42. Representation Phase Transition

A02 已提出：

$$
\boxed{
\text{Representation Phase Transition}.
}
$$

本文進一步形式化其直覺。

---

# 43. 最低定義

若：

$$
\Phi:
r_1\rightarrow r_2
$$

使：

$$
\boxed{
\frac{
C(P;s,r_1)
}{
C(P;s,r_2)
}
\gg1,
}
$$

且下降主要來自結構重組，而非單純硬體加速，

稱之為：

$$
\boxed{
\text{Representation Phase Transition}.
}
$$

---

# 44. 相變不一定是 asymptotic class collapse

可以只是：

$$
10^{15}
\rightarrow
10^8.
$$

---

# 45. 但也可能導致不同 asymptotic expression

例如某表示使：

$$
2^n
$$

型直接搜索，

轉成利用特殊結構的：

$$
n^k.
$$

但若要正式宣稱 complexity class 改變，

仍需標準證明。

---

# 46. 所以 Representation Phase Transition 有兩層

### Effective Phase Transition

實務成本大幅下降。

### Asymptotic Phase Transition

正式 asymptotic complexity 改變。

---

# 47. 不能混淆

$$
\boxed{
\text{Effective}
\neq
\text{Asymptotic}.
}
$$

---

# 48. AI 最可能先大量發現 Effective Phase Transition

因為它們可以用：

- heuristics；
- priors；
- data；
- memory；
- special cases。

---

# 49. 而 formal math 再判斷是否有 asymptotic theorem

因此：

$$
\boxed{
A
\rightarrow
F
}
$$

在這裡非常自然。

---

# 50. Representation Discovery 本身就是數學成果

如果一個：

$$
\Phi
$$

使整個問題族：

$$
\mathcal P
$$

成本大降，

則：

$$
\boxed{
\Phi
}
$$

本身可能比單一 theorem 更重要。

---

# 51. 新數學坐標系

未來重要成果可能是：

$$
\boxed{
\text{New Mathematical Coordinate System}.
}
$$

---

# 52. 坐標系可以比單一證明更有再利用價值

因為：

$$
\Phi
$$

可以服務：

$$
P_1,\ldots,P_N.
$$

---

# 53. 這就是 Representation Capital

本文暫稱：

$$
\boxed{
\text{Representation Capital}.
}
$$

---

# 54. Representation Capital 的價值

可概念化為：

$$
\boxed{
V_R(\Phi)
=
\sum_i
\Delta C(P_i\mid\Phi)
-
C_{\mathrm{build}}(\Phi).
}
$$

---

# 55. 如果：

$$
V_R(\Phi)\gg0,
$$

表示表示投資高度有效。

---

# 56. 人類數學史其實早已充滿 Representation Capital

例如：

- coordinate systems；
- calculus notation；
- matrices；
- Fourier domain；
- abstract algebra。

本文只是把它推向 AI-native scale。

---

# 57. AI 的不同點是搜尋規模

人類可能深度探索：

$$
N_H
$$

種 representation。

AI collective 可能探索：

$$
N_A\gg N_H.
$$

---

# 58. Representation Search Breadth

定義：

$$
\boxed{
B_R(s,t)
}
$$

表示 substrate $s$ 在時間 $t$ 可有效探索的表示範圍。

---

# 59. AI 的優勢可能是 $B_R$ 極大

不是單純：

$$
\boxed{
\text{proof steps per second}.
}
$$

---

# 60. Representation Search Depth

也可定義：

$$
\boxed{
D_R(s,t)
}
$$

表示對單一 representation 的深入優化能力。

---

# 61. Breadth 與 Depth 不同

$$
\boxed{
B_R
\neq
D_R.
}
$$

---

# 62. AI 可以平行探索

例如：

$$
r_1,\ldots,r_{10^6}.
$$

---

# 63. 但評估 representation 也需要成本

所以需要：

$$
\boxed{
\text{Representation Evaluation}.
}
$$

---

# 64. 不能每個表示都完整求解再比較

那會太貴。

---

# 65. Representation Surrogate

可以用：

- local complexity estimate；
- proof-state entropy；
- branching factor；
- invariant density；
- compression ratio；

作 surrogate。

---

# 66. Representation Search 可能本身形成 meta-learning

系統學習：

> 什麼問題應換什麼表示。

---

# 67. Meta-Representation Policy

寫成：

$$
\boxed{
\pi_R:
P
\mapsto
r.
}
$$

---

# 68. 記憶編譯後

$$
\pi_R
$$

本身也能被編譯。

---

# 69. 所以 representation search 也會從搜尋變索引

第一次：

$$
\text{Search}(r).
$$

之後：

$$
\boxed{
\text{Recognize}(P)
\rightarrow
r^\ast.
}
$$

---

# 70. 這再次接 A06

昂貴 meta-search：

$$
\rightarrow
$$

快速 representation routing。

---

# 71. Representation Search 與 theorem retrieval

有時最好的 representation 不需新發明。

只需找到已有理論：

$$
T_j.
$$

---

# 72. 所以 retrieval 本身也是 representation search 的一部分

因為：

> 找到對的理論，就是找到對的問題表示。

---

# 73. 跨領域 transfer

問題在：

$$
D_1
$$

難，

映射到：

$$
D_2
$$

可能簡單。

---

# 74. Cross-Domain Representation Transfer

$$
\boxed{
\Phi:
D_1
\rightarrow
D_2.
}
$$

---

# 75. 成功 transfer 要保留什麼？

至少：

- statement fidelity；
- relevant invariants；
- solution recoverability。

---

# 76. Solution Recoverability

若：

$$
y^\ast
$$

是 transform-domain solution，

必須有：

$$
\boxed{
\Psi(y^\ast)
=
x^\ast.
}
$$

---

# 77. 不然只是換問題

所以：

$$
\boxed{
\text{Transfer}
\neq
\text{Substitution}.
}
$$

---

# 78. Search-Space Engineering 的三層

本文提出：

### Level 1 — Encoding Engineering

改寫符號／編碼。

### Level 2 — Structural Engineering

改寫 graph / factor / quotient / invariant。

### Level 3 — Problem-Space Engineering

重新構造可搜索問題空間。

---

# 79. Level 1

例如：

$$
r_1\leftrightarrow r_2.
$$

語義基本不變。

---

# 80. Level 2

把：

$$
G
$$

變成 quotient graph：

$$
G/{\sim}.
$$

---

# 81. Level 3

把原 problem：

$$
P
$$

改寫為：

$$
P'
$$

只要：

$$
P\equiv P'
$$

在目標語義下成立。

---

# 82. AI-native mathematics 的強項可能主要出現在 Level 2–3

因為這需要維護大量結構。

---

# 83. State-Space Compression

假設原狀態：

$$
\mathcal S.
$$

透過 equivalence：

$$
\sim,
$$

形成：

$$
\boxed{
\mathcal S/{\sim}.
}
$$

---

# 84. 這可能降低搜索節點數

如果：

$$
|\mathcal S/{\sim}|
\ll
|\mathcal S|.
$$

---

# 85. 但 quotient 必須保留決策資訊

否則壓縮會破壞求解。

---

# 86. Decision-Sufficient Compression

定義：

$$
\boxed{
Q:
\mathcal S
\rightarrow
\bar{\mathcal S}
}
$$

若所有目標相關決策可由：

$$
\bar{\mathcal S}
$$

恢復，

稱為 decision-sufficient。

---

# 87. Minimal Sufficient State

這與：

$$
\boxed{
\text{minimal sufficient state}
}
$$

概念相近。

---

# 88. 表示搜索可能尋找最小充分狀態

$$
\boxed{
\min
|\bar{\mathcal S}|
}
$$

subject to：

$$
\boxed{
\text{solution fidelity}.
}
$$

---

# 89. 這開始逼近 A04

因為如果：

$$
\bar{\mathcal S}
$$

還保留最短路徑，

壓縮就有更強性質。

---

# 90. 一般 sufficient 不代表 geodesic-preserving

可能：

$$
\text{correct solution}
$$

仍可恢復，

但：

$$
\boxed{
\text{shortest path}
}
$$

被改變。

---

# 91. 所以 A04 要增加 geodesic condition

本篇只到：

$$
\boxed{
\text{solution-preserving representation}.
}
$$

A04 再升到：

$$
\boxed{
\text{shortest-path-preserving representation}.
}
$$

---

# 92. Representation Search 的另一種目標：Branching Reduction

若原 graph 平均 branching：

$$
b.
$$

新 representation：

$$
b'.
$$

且：

$$
b'\ll b,
$$

搜索可大幅下降。

---

# 93. Depth Reduction

也可以：

$$
d'\ll d.
$$

---

# 94. Branching × Depth

粗略搜索成本：

$$
O(b^d).
$$

所以 representation 改變：

$$
b,d
$$

非常重要。

---

# 95. 但這只是搜索樹近似

不是一般 theorem。

---

# 96. Constraint Propagation Representation

有些 representation 使 constraint：

$$
c_i
$$

更早可見。

---

# 97. 越早 prune

$$
\boxed{
\text{search volume}
\downarrow.
}
$$

---

# 98. Invariant Exposure

好的 representation 可能把 hidden invariant：

$$
I
$$

變成顯式。

---

# 99. 一旦 invariant 顯式

大量 state：

$$
s
$$

可以直接排除。

---

# 100. 所以 representation 的價值之一是「讓約束可見」

$$
\boxed{
\text{Hidden Constraint}
\rightarrow
\text{Explicit Structure}.
}
$$

---

# 101. AI 可以搜尋 invariant-rich representation

這可能是未來 proof search 的重要前置。

---

# 102. Representation Search 與 abstraction

高階 abstraction：

$$
A(P)
$$

可以把多個細節折疊。

---

# 103. 但 abstraction 可能失真

所以需要：

$$
\boxed{
\text{Abstraction Error}.
}
$$

---

# 104. Exact 與 Approximate Representation

可以區分：

$$
\boxed{
r_{\mathrm{exact}}
}
$$

與：

$$
\boxed{
r_{\mathrm{approx}}.
}
$$

---

# 105. 數學證明通常需要 exact fidelity

但 discovery 階段可以使用 approximate representation。

---

# 106. Discovery Representation 與 Verification Representation 可以不同

這是重要結論：

$$
\boxed{
r_D
\neq
r_V.
}
$$

---

# 107. AI 可以在模糊／啟發式表示中發現

再把結果編譯成：

$$
r_V.
$$

---

# 108. 這就是 A01 的 $A\rightarrow F$

AI-native：

$$
A
$$

負責探索，

Formal：

$$
F
$$

負責驗證。

---

# 109. Explanation Representation 又可能不同

$$
\boxed{
r_E
\neq
r_D
\neq
r_V.
}
$$

---

# 110. 所以一個 theorem 至少可以有三個 representation

- discovery；
- verification；
- explanation。

---

# 111. 不要強迫同一 representation 同時最優

這會造成：

$$
\boxed{
\text{Multi-Objective Representation Conflict}.
}
$$

---

# 112. AI-native architecture 應接受多表示共存

不是追求：

$$
\boxed{
\text{One Representation to Rule Them All}.
}
$$

---

# 113. Representation Routing

不同階段：

$$
r_D
\rightarrow
r_V
\rightarrow
r_E.
$$

---

# 114. Routing 本身有 loss

所以：

$$
\boxed{
L_{D\rightarrow V},
\quad
L_{V\rightarrow E}.
}
$$

---

# 115. Loss 必須可審計

尤其 statement fidelity。

---

# 116. Search-Space Engineering 與自動理論生成

AI 可能為問題：

$$
P
$$

臨時生成：

$$
\mathcal T_P.
$$

---

# 117. $\mathcal T_P$ 就是一種表示工程

因為它重新定義：

- primitives；
- lemmas；
- relations；
- invariants。

---

# 118. 所以 Ephemeral Mathematics 可以被看成 Representation Search 的結果

$$
\boxed{
\text{Representation Search}
\rightarrow
\text{Ephemeral Local Theory}.
}
$$

---

# 119. 解完後：

$$
\mathcal T_P
$$

可以被：

- archive；
- compress；
- discard；
- compile。

---

# 120. Representation Search 與 Theorem Ocean

如果大量 AI 都在搜尋表示，

會產生大量：

- local theories；
- intermediate lemmas；
- transformations。

---

# 121. 因此 theorem ocean 可能包含大量「表示副產物」

不是所有都值得人類保存。

---

# 122. Significance Filter 必須識別 representation capital

有些 theorem 本身不重要，

但它背後：

$$
\Phi
$$

可能極重要。

---

# 123. 所以評價單位要從 theorem 擴張

$$
\boxed{
\text{Theorem}
\rightarrow
\text{Transformation / Representation / Invariant}.
}
$$

---

# 124. AI-native discovery 的單位可能是 operator

例如：

$$
\boxed{
\Phi^\ast
}
$$

能同時降低很多 problem family 成本。

---

# 125. Representation Centrality

可定義：

$$
\boxed{
C_R(\Phi)
}
$$

表示 transformation 在多個 problem graph 中的中心性。

---

# 126. High-Centrality Representation Operator

可能比某單一 theorem 更值得保留。

---

# 127. Search-Space Engineering 與 compiler

這裡可以借用 compiler 直覺：

$$
\text{Source}
\rightarrow
\text{IR}
\rightarrow
\text{Optimized IR}
\rightarrow
\text{Execution}.
$$

---

# 128. 數學也可以：

$$
\boxed{
\text{Human Statement}
\rightarrow
\text{Mathematical IR}
\rightarrow
\text{Optimized Representation}
\rightarrow
\text{Proof Search}.
}
$$

---

# 129. Optimization Pass

AI 可執行：

- dead branch elimination；
- common subexpression merge；
- invariant extraction；
- symmetry quotient；
- dependency factoring。

---

# 130. 這不是字面編譯器等價

但結構上高度相似。

---

# 131. Representation Compiler

本文暫稱：

$$
\boxed{
\mathfrak C_R.
}
$$

---

# 132. 輸入

$$
(P,\Gamma,R_0).
$$

---

# 133. 輸出

$$
\boxed{
R^\ast.
}
$$

---

# 134. 目標

$$
\boxed{
\min J(R)
}
$$

subject to：

$$
\boxed{
\operatorname{Fid}(P,R)=1.
}
$$

---

# 135. $\Gamma$ 在本系列 B 才完整處理

本篇可先把：

$$
\Gamma
$$

理解成 problem context。

---

# 136. 但 Representation Compiler 已暗示 frame-relative

因為：

$$
R^\ast(P,\Gamma_1)
\neq
R^\ast(P,\Gamma_2)
$$

可能成立。

---

# 137. Search-Space Engineering 與主體相對性

這個接口後續會變重要。

今天我們先停在：

$$
\boxed{
\text{representation is conditional}.
}
$$

---

# 138. AI 能不能「找到世界中正確的表示」？

本文不採：

> 唯一正確 representation。

---

# 139. 更合理是：

$$
\boxed{
\text{task-sufficient}
+
\text{semantically faithful}
+
\text{cost-effective}.
}
$$

---

# 140. Representation Truth Fallacy

不能寫：

$$
\boxed{
\text{Best Representation}
=
\text{Truth Itself}.
}
$$

---

# 141. Operational Optimality 不是 Ontological Privilege

保留 A01 原則：

$$
\boxed{
\text{Operational Optimality}
\neq
\text{Ontological Privilege}.
}
$$

---

# 142. AI 可能發現人類從未會選的表示

因為：

$$
C_H(r_A)
$$

太高。

---

# 143. 例如極高維局部圖

人類不會手動維護：

$$
10^9
$$

個局部節點。

AI 可以。

---

# 144. 因此 human ugliness 可以是 machine naturalness

$$
\boxed{
\text{Human-Ugly}
\neq
\text{Machine-Bad}.
}
$$

---

# 145. 但 human projection 仍可另做

$$
r_A
\rightarrow
r_H^{\mathrm{proj}}.
$$

---

# 146. 所以「不可讀」不應阻止 discovery

只要：

$$
\boxed{
\text{verifiable}
+
\text{reconstructable}
+
\text{translatable enough}.
}
$$

---

# 147. Representation Search 的最大風險：semantic drift

AI 為了降低成本，

可能悄悄改掉：

- domain；
- quantifier；
- assumptions；
- target。

---

# 148. 所以所有 representation transformation 都要有 mapping proof

至少：

$$
\boxed{
P
\leftrightarrow
P'
}
$$

在目標語義下可驗證。

---

# 149. Exact Equivalence

理想：

$$
\boxed{
P\equiv P'.
}
$$

---

# 150. One-Way Reduction

有時只有：

$$
P\leq P'.
$$

---

# 151. 這時必須標記方向性

不能把 reduction 當 equivalence。

---

# 152. Approximate Transform

如果只有：

$$
P\approx P',
$$

則只能用於：

- heuristic；
- candidate generation；
- exploration。

---

# 153. Verification stage 必須回到 exact claim

---

# 154. Representation Search 的第二個風險：overfitting

某表示：

$$
r^\ast
$$

只對訓練問題有效。

---

# 155. Cross-Instance Transfer

因此需測：

$$
\boxed{
\Delta C(P_{\mathrm{new}}\mid r^\ast).
}
$$

---

# 156. Representation Reuse Rate

定義：

$$
\boxed{
R_{\mathrm{reuse}}(r).
}
$$

---

# 157. 低 reuse 的表示可以是 ephemeral

這不是失敗。

---

# 158. 高 reuse 的表示應升格為 canon candidate

---

# 159. Representation Lifecycle

$$
\boxed{
\text{discover}
\rightarrow
\text{test}
\rightarrow
\text{verify}
\rightarrow
\text{reuse}
\rightarrow
\text{compile}
\rightarrow
\text{deprecate}.
}
$$

---

# 160. 這與軟體版本類似

但本文不將數學簡化為軟體。

---

# 161. Representation versioning

同一表示：

$$
r^{(1)},r^{(2)},\ldots
$$

需要 version identity。

---

# 162. 因為 proof dependency 依賴 representation semantics

---

# 163. Representation Search 的第三個風險：search explosion

如果 representation space：

$$
|\mathcal R|
$$

巨大，

meta-search 本身可能比 proof search 更難。

---

# 164. 所以：

$$
\boxed{
\text{Representation Search}
\neq
\text{Free Superpower}.
}
$$

---

# 165. Meta-Complexity

定義：

$$
\boxed{
C_{\mathrm{meta}}(P)
=
C_{\mathrm{search\;over}\;\mathcal R}(P).
}
$$

---

# 166. 如果：

$$
C_{\mathrm{meta}}
\gg
C_{\mathrm{proof}},
$$

那 representation search 不划算。

---

# 167. 但 memory compilation 可以降低 meta-cost

一旦知道：

> 某 problem pattern → 某 representation。

---

# 168. Meta-search 轉 routing

$$
\boxed{
\text{Meta Search}
\rightarrow
\text{Representation Index}.
}
$$

---

# 169. 這是 AI 累積優勢之一

---

# 170. Representation Search 的第四個風險：verification debt

若 discovery representation 太複雜，

formalization：

$$
C_V
$$

可能巨大。

---

# 171. 因此不能只優化 solve cost

必須：

$$
\boxed{
\min
(
C_S
+
C_V
+
C_T
).
}
$$

---

# 172. Representation Search 的第五個風險：translation lock-in

如果只有一個 AI 能讀：

$$
r^\ast,
$$

形成：

$$
\boxed{
\text{Mathematical Lock-In}.
}
$$

---

# 173. 所以 interchange layer 必須同步成熟

---

# 174. Representation Search 與 Mathematical ABI

AI 內部：

$$
r_A^\ast.
$$

外部：

$$
r_I.
$$

---

# 175. 不需要內部完全標準化

只需：

$$
\boxed{
\operatorname{Compile}_{A\rightarrow I}(r_A^\ast).
}
$$

---

# 176. 這維持：

$$
\boxed{
\text{Internal Diversity}
+
\text{External Interoperability}.
}
$$

---

# 177. Representation Search 的第六個風險：假壓縮

如果：

$$
r'
$$

表面很短，

但所有複雜度藏在 external oracle，

不能說問題消失。

---

# 178. 這正是 A05 的問題

$$
\boxed{
\text{Where Does Complexity Live?}
}
$$

---

# 179. 一行表示可以有巨大背後成本

$$
\boxed{
\text{Short Description}
\neq
\text{Low Total Complexity}.
}
$$

---

# 180. Representation Search 與 Hyperlink

假設底層：

$$
u
\rightarrow
x_1
\rightarrow
\cdots
\rightarrow
v
$$

可壓成：

$$
\boxed{
u\xrightarrow{h}v.
}
$$

---

# 181. 這是一種 representation compression

但現在關鍵：

> $h$ 是否保留底層真正最短成本？

---

# 182. 若保留

則：

$$
\boxed{
w(h)
=
d(u,v).
}
$$

---

# 183. 這就不是普通 shortcut

而是：

$$
\boxed{
\text{Geodesic Hyperlink}.
}
$$

---

# 184. A03 到這裡停下

因為「怎麼證明多層 shortcut 保持最短性」屬於 A04。

---

# 185. Representation Search 的終極方向

可以概括：

$$
\boxed{
\text{Find a world-description in which the solution path becomes structurally obvious}.
}
$$

---

# 186. 但「obvious」是 substrate-relative

對人類 obvious，

可能對 AI 不 obvious。

---

# 187. 所以應寫

$$
\boxed{
\text{low-cost under substrate }s.
}
$$

---

# 188. Representation Search 與 AI 原生數學的核心連接

A01：

$$
\boxed{
\text{AI can have machine-native representations}.
}
$$

A02：

$$
\boxed{
\text{representation changes cost}.
}
$$

A03：

$$
\boxed{
\text{therefore representation itself should be searched}.
}
$$

---

# 189. Series A 的推進

$$
A01
\rightarrow
A02
\rightarrow
A03
$$

即：

$$
\boxed{
\text{Nativeness}
\rightarrow
\text{Relative Complexity}
\rightarrow
\text{Representation Search}.
}
$$

---

# 190. 下一步：Path Architecture

當 representation 被工程化，

我們下一個問題不是：

> 表示漂亮嗎？

而是：

> 它如何重組 path geometry？

---

# 191. Path Geometry

令：

$$
G_r(P)
$$

表示在 representation $r$ 下的 problem graph。

---

# 192. 不同 $r$

$$
G_{r_1}(P)
\neq
G_{r_2}(P).
$$

---

# 193. 但目標語義應等價

$$
\boxed{
\operatorname{Goal}(G_{r_1})
\equiv
\operatorname{Goal}(G_{r_2}).
}
$$

---

# 194. Representation Search 可以看成 graph search over graphs

即：

$$
\boxed{
\mathcal G
=
\{
G_r(P)
\}_{r\in\mathcal R}.
}
$$

---

# 195. 第一層搜索

$$
\boxed{
\text{search over representations}.
}
$$

---

# 196. 第二層搜索

$$
\boxed{
\text{search inside selected representation}.
}
$$

---

# 197. 形成雙層搜索

$$
\boxed{
\operatorname{Search}_{r}
\left[
\operatorname{Search}_{\pi}(G_r)
\right].
}
$$

---

# 198. 多層甚至可以遞迴

representation itself 也可有 representation。

---

# 199. 但本文不宣稱 completed infinite tower

只需要：

$$
\boxed{
\text{finite recursive refinement when useful}.
}
$$

---

# 200. 這與 UBE 後續可接

但不是本篇核心。

---

# 201. Search-Space Engineering 的五個目標

1. 減少無效狀態；
2. 降低 branching；
3. 降低 path depth；
4. 提高 constraint visibility；
5. 提高 reusable structure density。

---

# 202. 無效狀態消除

若：

$$
S_{\mathrm{invalid}}
$$

可提前去掉：

$$
\boxed{
|\mathcal S'|
=
|\mathcal S|
-
|S_{\mathrm{invalid}}|.
}
$$

---

# 203. Symmetry Collapse

若大量狀態只差 symmetry，

quotient：

$$
\mathcal S/G
$$

可大幅縮小。

---

# 204. Dependency Factoring

如果：

$$
P=P_1\otimes P_2,
$$

可分解獨立處理。

---

# 205. Invariant Indexing

把 invariant 變成 lookup key。

---

# 206. Macro-Transition

把常用底層 path 壓成：

$$
\boxed{
\text{macro edge}.
}
$$

---

# 207. Macro-Transition 是 A04 的前身

一般 macro 不保證最短。

A04 要研究 exact geodesic macro。

---

# 208. Representation Search 的成功標準

不是：

$$
\boxed{
\text{representation looks simpler}.
}
$$

而是：

$$
\boxed{
C_{\mathrm{total}}(r')
<
C_{\mathrm{total}}(r).
}
$$

---

# 209. 並且：

$$
\boxed{
\operatorname{Fid}(P,r')=1.
}
$$

---

# 210. 如果只是壓縮文本

但：

$$
C_{\mathrm{execute}}
$$

變高，

不一定成功。

---

# 211. 所以短表示不等於好表示

$$
\boxed{
|r'|
<
|r|
\not\Rightarrow
C(r')<C(r).
}
$$

---

# 212. 這會在 A05 變得更重要

---

# 213. Representation Search 與 proof length

短 proof：

$$
|\pi|
$$

只是成本的一部分。

---

# 214. 某 representation 可能讓 proof 長

但 verification 很局部。

---

# 215. 另一 representation proof 短

但 translation 很難。

---

# 216. 所以 lifecycle cost 更重要

保留：

$$
\boxed{
C_L
=
C_{\mathrm{discover}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{store}}
+
C_{\mathrm{retrieve}}
+
C_{\mathrm{translate}}
+
C_{\mathrm{update}}.
}
$$

---

# 217. Representation Search 是 lifecycle optimization

而不只是 proof compression。

---

# 218. AI 原生數學的數學美感也會因此改變

AI 可能偏好：

$$
\boxed{
\text{low lifecycle cost}.
}
$$

---

# 219. Human elegance 與 machine efficiency 可以一致

但不必一致。

---

# 220. Representation Search 與新數學產生

當 AI 找不到好表示，

它可能創造：

- 新定義；
- 新 operator；
- 新 category；
- 新 invariant。

---

# 221. 這就是「新數學」的一種來源

不是因為：

> 想創造新理論。

而是：

> 現有表示成本太高。

---

# 222. New Mathematics as Compression Response

可以暫寫：

$$
\boxed{
\text{Representation Pressure}
\rightarrow
\text{New Mathematical Structure}.
}
$$

---

# 223. 這是一個有趣的 AI-native hypothesis

未來許多新概念可能由 optimizer 產生。

---

# 224. 但需人類或 AI 評估 significance

因為：

> 有用的局部 representation 不一定值得成為普遍理論。

---

# 225. Ephemeral vs Canonical Representation

若：

$$
V_R(\Phi)
$$

低 reuse，

保留 ephemeral。

若高：

$$
V_R(\Phi)\gg0,
$$

可升 canonical candidate。

---

# 226. Canonization 是另一種 compression

把很多局部成功：

$$
\Phi_1,\ldots,\Phi_n
$$

抽成：

$$
\boxed{
\Phi^\ast.
}
$$

---

# 227. 這是數學文化形成機制

AI-native math 也會需要。

---

# 228. Representation Search 與人類直覺

人類很擅長：

$$
\boxed{
\text{low-dimensional conceptual compression}.
}
$$

---

# 229. AI 很擅長的可能是：

$$
\boxed{
\text{high-dimensional structural exploration}.
}
$$

---

# 230. Hybrid system 可能最好

Human：

> 提出 powerful abstraction。

AI：

> 大量探索 variants。

---

# 231. 或反過來

AI：

> 找到 strange representation。

Human：

> 抽出 elegant invariant。

---

# 232. 所以：

$$
\boxed{
\text{Origin}
\neq
\text{Permanent Functional Role}.
}
$$

---

# 233. Representation Search 的可證偽性

若未來發現：

$$
C_{\mathrm{repr-search}}
$$

普遍遠高於直接 proof search，

則其實務重要性下降。

---

# 234. 若大部分問題只有少數自然表示

則 representation search space 不大。

---

# 235. 若 AI 自動生成表示但無法保持 fidelity

則 representation search 失敗。

---

# 236. 若表示切換帶來巨大 verification debt

總收益可能為負。

---

# 237. 所以本理論不是「表示萬能論」

---

# 238. Representation Search 的最小成立條件

至少需要：

1. 多表示存在；
2. 成本差異存在；
3. 語義可保持；
4. 表示可比較；
5. 搜尋成本可接受；
6. 成果可驗證。

---

# 239. 若六者都不成立

則：

$$
\boxed{
\text{fixed representation}
}
$$

仍合理。

---

# 240. AI-native benchmark 應允許 representation rewrite

如果 benchmark 只允許：

$$
r_H,
$$

則測到：

$$
\boxed{
\text{AI under human representation constraint}.
}
$$

---

# 241. 更強 benchmark

允許：

$$
P_H
\xrightarrow{\Phi_A}
P_A.
$$

---

# 242. 再求解：

$$
P_A
\rightarrow
Q_A.
$$

---

# 243. 再投影：

$$
Q_A
\xrightarrow{\Psi_H}
Q_H.
$$

---

# 244. 完整流程

$$
\boxed{
P_H
\xrightarrow{\Phi_A}
P_A
\xrightarrow{\operatorname{Solve}}
Q_A
\xrightarrow{\Psi_H}
Q_H.
}
$$

---

# 245. Fidelity 必須兩端檢查

$$
\boxed{
P_H\equiv P_A,
}
$$

以及：

$$
\boxed{
Q_H\equiv Q_A
}
$$

在指定語義下。

---

# 246. 這才是 AI-native mathematical benchmark 的候選形式

---

# 247. Representation Search 也可以跨 AI

AI- $1$ 發現：

$$
r_1.
$$

AI- $2$ 發現：

$$
r_2.
$$

---

# 248. 它們可以交換 transformation certificate

不用共享全部 internal reasoning。

---

# 249. 這再次依賴 Mathematical ABI

---

# 250. Representation Competition

不同 AI 可以提交：

$$
r_i
$$

以及：

$$
\boxed{
\text{cost + fidelity certificate}.
}
$$

---

# 251. 再由第三方驗證

---

# 252. 這可能成為未來數學研究的新競爭單位

不是：

> 誰先證出 theorem。

而是：

> 誰找到最有價值的 representation。

---

# 253. Representation Marketplace 不在本文討論

本文只處理理論。

---

# 254. Search-Space Engineering 的深層哲學

它提醒：

$$
\boxed{
\text{The shape of the problem space is partly a modeling choice}.
}
$$

---

# 255. 但不是完全任意

因為：

$$
\boxed{
\text{Reality / mathematical constraints resist bad representations}.
}
$$

---

# 256. 好 representation 不能憑空消除 constraint

它只能：

- expose；
- factor；
- compress；
- relocate。

---

# 257. 這就是複雜度外部化的前奏

如果你把困難藏到：

$$
\Phi
$$

裡，

後續求解很容易。

---

# 258. 但：

$$
\boxed{
C_{\Phi}
}
$$

仍存在。

---

# 259. 所以 A05 會問：

> 複雜度到底跑去哪裡？

---

# 260. A03 與 A04 的關鍵分界

A03：

$$
\boxed{
\text{find a better representation}.
}
$$

A04：

$$
\boxed{
\text{build a representation whose compressed edges preserve shortest-path structure}.
}
$$

---

# 261. 一般表示優化不需要 geodesic

只要解得出即可。

---

# 262. A04 要求更強

$$
\boxed{
d_{\ell+1}
=
d_\ell
}
$$

在指定 boundary states 上。

---

# 263. 這才會產生 exact hyperlink

---

# 264. Representation Search 的最終核心公式

$$
\boxed{
r^\ast
=
\arg\min_{r\in\mathcal R}
\left[
C_{\mathrm{find}}(r)
+
C_{\mathrm{solve}}(P\mid r)
+
C_{\mathrm{verify}}(r)
+
C_{\mathrm{translate}}(r)
+
C_{\mathrm{maintain}}(r)
\right].
}
$$

---

# 265. 這個式子不是最終 universal objective

因為權重與成本模型依 domain 而變。

---

# 266. 但它足以指出：

$$
\boxed{
\text{representation is an optimization variable}.
}
$$

---

# 267. 核心命題 A03-1

$$
\boxed{
\text{Representation}
\neq
\text{Fixed Background}.
}
$$

---

# 268. 核心命題 A03-2

$$
\boxed{
\text{Representation}
=
\text{Search Variable}.
}
$$

---

# 269. 核心命題 A03-3

$$
\boxed{
\text{Before searching harder, search for a representation in which the problem becomes easier}.
}
$$

---

# 270. 核心命題 A03-4

$$
\boxed{
\text{Problem Solving}
\rightarrow
\text{Search-Space Engineering}.
}
$$

---

# 271. 核心命題 A03-5

$$
\boxed{
\text{Easy after transformation}
\neq
\text{Transformation was easy}.
}
$$

---

# 272. 核心命題 A03-6

$$
\boxed{
\text{Representation Phase Transition}
\neq
\text{Automatic Complexity-Class Collapse}.
}
$$

---

# 273. 核心命題 A03-7

$$
\boxed{
\text{Discovery Representation}
\neq
\text{Verification Representation}
\neq
\text{Explanation Representation}.
}
$$

---

# 274. 核心命題 A03-8

$$
\boxed{
\text{Representation Capital}
}
$$

可以跨問題攤提搜尋成本。

---

# 275. 核心命題 A03-9

$$
\boxed{
\text{Search-Space Compression}
\neq
\text{Geodesic Preservation}.
}
$$

後者是更強條件。

---

# 276. 核心命題 A03-10

$$
\boxed{
\text{A high-value representation can be a mathematical result in its own right}.
}
$$

---

# 277. 一句話版本

> **更強的數學 AI 不只是更快地在既有空間找答案，而是更快地找到「應該在哪個空間裡找答案」。**

---

# 278. 更正式版本

$$
\boxed{
\text{Higher-order solving}
=
\text{search over representations}
+
\text{search within representations}.
}
$$

---

# 279. 這與人類數學史的連續性

人類一直在：

$$
\boxed{
\text{change coordinates}
}
$$

只是 AI 可能把它：

- 大規模化；
- 自動化；
- 並行化；
- 記憶化；
- 編譯化。

---

# 280. 所以 AI-native 不是憑空出現

它是既有人類數學方法的一個 substrate-scale extension。

---

# 281. 但規模差異可能產生質變

若：

$$
B_R(A)\gg B_R(H),
$$

representation search 可以從：

> 偶發天才洞見

變成：

$$
\boxed{
\text{systematic computational process}.
}
$$

---

# 282. 這可能是 AI 原生數學真正的轉折點

---

# 283. 與 A04 的正式接口

現在令：

$$
G_0
$$

為原始問題 graph。

AI 經 representation search 得到：

$$
G_1.
$$

再得到：

$$
G_2.
$$

---

# 284. 如果每次壓縮只是「解仍存在」

還不夠。

---

# 285. A04 將問：

$$
\boxed{
d_{G_{\ell+1}}
(
\phi_\ell(u),
\phi_\ell(v)
)
=
d_{G_\ell}(u,v)
}
$$

能否對指定 boundary states 成立。

---

# 286. 若可以

底層：

$$
u\rightarrow x_1\rightarrow\cdots\rightarrow v
$$

可被壓成：

$$
\boxed{
u\xrightarrow{h}v.
}
$$

---

# 287. 再把 hyperlink 重新壓縮

$$
h_1,h_2,\ldots
\rightarrow
H.
$$

---

# 288. 最後最高層可能只剩

$$
\boxed{
s\xrightarrow{H}g.
}
$$

---

# 289. 但：

$$
\boxed{
\text{One Link}
\neq
\text{Zero Complexity}.
}
$$

A05 再處理。

---

# 290. 因此 A03 的歷史位置

A01：

> 數學表示不必只為人類。

A02：

> 不同表示會改變不同 substrate 的成本。

A03：

> 所以表示應該被搜尋。

A04：

> 如果搜尋到的表示能保持最短路徑，就可以形成測地超連結。

---

# 291. Series A 前四篇的核心鏈

$$
\boxed{
\text{AI-Native Representation}
\rightarrow
\text{Substrate-Relative Complexity}
\rightarrow
\text{Representation Search}
\rightarrow
\text{Geodesic Hyperlink}.
}
$$

---

# 292. 結論

數學求解常被想像成：

$$
\boxed{
\text{Problem}
\rightarrow
\text{Search}
\rightarrow
\text{Solution}.
}
$$

本文提出更高階的流程：

$$
\boxed{
\text{Problem}
\rightarrow
\text{Representation Search}
\rightarrow
\text{Search-Space Engineering}
\rightarrow
\text{Proof / Solution Search}
\rightarrow
\text{Verification}.
}
$$

這個轉變的核心並不是否定 proof search。

相反地，

它重新定位：

$$
\boxed{
\text{Proof Search}
}
$$

只是更大求解系統中的一層。

真正 AI-native 的數學系統可能首先問：

> 目前這個問題空間本身是不是最佳問題空間？

如果不是，

它就不應該只在同一個空間裡投入更多搜索。

它應該：

$$
\boxed{
\text{rewrite the space}.
}
$$

因此本文最終提出：

$$
\boxed{
\text{Solve the search space before solving the problem}.
}
$$

但這句話仍不代表：

> 搜索空間可以任意縮短。

下一篇的真正困難是：

> **如果我們把巨大底層路徑壓成高階 shortcut，如何證明這些 shortcut 不只是看起來很短，而是真的保留底層最短性？**

這就是 Series A / Paper 04：

# 《遞迴測地超連結理論：從最短路徑保持到一行解》

的起點。

---

## 內部理論接口

本篇與下列理論建立橋接，但不主張還原：

- A01〈AI 原生數學不是人類數學的加速版〉
- A02〈跨基質數學複雜度〉
- Mathematical IR
- Ephemeral Mathematics
- 記憶編譯型狀態智能體
- MSSP × RDR
- CSM
- UBE
- SOBTA
- Neo.K 終極 P/NP 問題

原則：

$$
\boxed{
\text{Bridge}
\neq
\text{Reduction}.
}
$$

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown source。數學原始碼僅使用 ` $...$ ` 與 `$$...$$` 作為 canonical delimiter。
