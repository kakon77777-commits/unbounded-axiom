# TADC-06：關係優先認知與跨域連續性——從學科距離到關係距離的認知拓樸猜想

**英文題名：** Relation-First Cognition and Cross-Domain Continuity: From Disciplinary Distance to Relational Cognitive Distance  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-06  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論命題／關係空間模型／可證偽研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

跨領域思考通常以外部知識分類為基礎描述。例如，從數學轉向認知科學、從生物學轉向人工智慧，常被視為一次「跨域切換」。然而，這種描述預設了學科分類距離可以代表認知轉換距離。

本文提出相反的候選框架：

$$
\boxed{
\text{disciplinary distance}
\neq
\text{cognitive relational distance}.
}
$$

一個表面上跨越多個學科的轉換，若兩個問題共享高度相似的因果結構、形式關係、程序結構、控制約束、類比映射或目標角色，則在認知系統的有效關係空間中可能仍是局部移動。反之，兩個被歸入同一學科的問題，若缺乏可重用的關係結構，對主體而言也可能需要高成本重建。

本文提出三個核心猜想：

1. **Relation-First Cognition Conjecture（RFCC）**：在部分高階推理中，關係結構比外部分類標籤更能預測有效認知鄰接與轉換成本；
2. **Cross-Domain Continuity Conjecture（CDCC）**：部分表面跨領域轉換，可在另一個 goal-conditioned relational topology 中形成連續或近連續的認知軌跡；
3. **Relational Re-representation Conjecture（RRC）**：跨域映射不只發現既有相似性，也可能透過 analogical alignment、abstraction 與 schema updating 改變後續有效關係表示。

本文定義外部分類距離：

$$
d_{\mathrm{ext}}(x,y),
$$

關係認知距離：

$$
d_{\mathrm{rel}}(x,y\mid G),
$$

以及跨域落差量：

$$
\boxed{
\Delta_{\mathrm{cross}}
=
d_{\mathrm{ext}}
-
d_{\mathrm{rel}}.
}
$$

當：

$$
\Delta_{\mathrm{cross}}\gg0,
$$

稱為 **Apparent Cross-Domain / Relationally Local Transition**：外部分類看似遙遠，但內部關係上近鄰。

本文進一步使用 multiplex relational graph 表示語義、因果、類比、程序、時間、目標與控制關係，並提出 structural-alignment score、bridge density、translation cost、relational path cost 與 continuity ratio 等可測量量。

現有 analogical reasoning 研究已證明人類可跨不同 sensory modalities 進行 analogical mapping；實驗也觀察到 relational re-representation；計算模型則展示 relational representations 可支援跨 video games 與心理任務的 cross-domain generalization。2025/2026 年的 schema-drift 研究進一步顯示，抽象 relational schemas 在反覆類比使用後可以發生可測改變。同時，semantic-control 與 task-space cognitive-map 研究顯示，相同刺激可因目標與控制需求形成不同的大尺度認知／腦狀態，且 task-relevant abstract structure 可被建構為 cognitive maps。

這些結果支持「關係結構具有跨表面分類的認知作用」，但尚未證明 RFCC / CDCC。本文因此建立 taxonomy-only、surface-similarity、fixed-semantic-space、ordinary analogy、random-association 與 expertise-only 等競爭模型，並提出跨學科距離矩陣、relation-matched switching、bridge induction、re-representation、schema drift、path-return 與 multi-scale continuity 等實驗。

本文的核心主張不是「所有領域其實都一樣」，而是：

$$
\boxed{
\text{external categorical discontinuity}
\not\Rightarrow
\text{internal cognitive discontinuity}.
}
$$

如果關係距離不能比學科標籤、語義相似度與一般熟悉度提供額外預測，則本篇強版本應被拒絕。

**關鍵詞：** relational cognition；cross-domain reasoning；analogy；structural alignment；cognitive distance；cognitive topology；re-representation；cognitive maps；semantic control；TADC

---

# 0. 邊界聲明

本文不是要主張：

> 「所有知識本質上都是一樣的。」

也不是：

> 「學科分類沒有意義。」

學科分類對：

- 知識累積；
- 教育；
- 方法論；
- 社群；
- 審查；
- 工具；
- 專業規範；

都具有重要功能。

本文研究的是另一個問題：

$$
\boxed{
\text{Are disciplinary boundaries
the same as cognitive transition boundaries?}
}
$$

本文提出的答案只是：

$$
\boxed{
\text{not necessarily}.
}
$$

此外，「關係優先」不是指：

$$
\text{relations always dominate objects}.
$$

而是：

> 在部分需要 transfer、analogy、abstraction、cross-domain inference 與 problem reformulation 的高階 cognition 中，relational structure 可能比表面 category labels 更能預測認知鄰接。

---

# 1. 從 TADC-02 的問題重新開始

TADC-02 已提出：

$$
d_{\mathrm{discipline}}(x,y)
\neq
d_{\mathrm{cognitive}}(x,y).
$$

但當時只是概念區分。

TADC-06 的目標是：

1. 定義這兩種距離；
2. 找到可觀察 proxy；
3. 建立競爭模型；
4. 決定是否真的需要「跨域連續性」這個構念。

---

# 2. 外部分類距離

令外部 taxonomy：

$$
\Pi^{\mathrm{ext}}
=
\{
D_1,D_2,\ldots,D_m
\}.
$$

每個 cognitive object：

$$
x
$$

可具有一個或多個外部分類標籤：

$$
L_{\mathrm{ext}}(x).
$$

最簡距離：

$$
d_{\mathrm{ext}}(x,y)
=
\begin{cases}
0,&L(x)=L(y),\\
1,&L(x)\neq L(y).
\end{cases}
$$

但真實 taxonomy 通常 hierarchical。

因此可用 tree distance：

$$
d_{\mathrm{ext}}^{\mathrm{tree}}
(
x,y
)
$$

或 ontology graph distance。

---

# 3. 外部分類距離的限制

兩個 concepts：

$$
x,y
$$

可能分別屬於：

$$
D_A,
D_B.
$$

即使：

$$
d_{\mathrm{ext}}(x,y)
\gg0,
$$

它們可能共享：

- feedback；
- invariance；
- conservation；
- recursion；
- optimization；
- hierarchy；
- phase transition；
- information bottleneck；
- control loop。

因此：

$$
\boxed{
\text{external label distance}
}
$$

不必等於：

$$
\boxed{
\text{structural reasoning distance}.
}
$$

---

# 4. Multiplex Relational Graph

定義 cognitive relational graph：

$$
\mathcal G_t
=
(
V_t,
E_t^{(S)},
E_t^{(C)},
E_t^{(A)},
E_t^{(P)},
E_t^{(T)},
E_t^{(G)},
E_t^{(K)}
).
$$

其中：

- \(E^{(S)}\)：semantic relations；
- \(E^{(C)}\)：causal relations；
- \(E^{(A)}\)：analogical relations；
- \(E^{(P)}\)：procedural relations；
- \(E^{(T)}\)：temporal relations；
- \(E^{(G)}\)：goal relations；
- \(E^{(K)}\)：control / constraint relations。

因此 cognition 不在單一 semantic embedding 中發生，

而可能在：

$$
\boxed{
\text{multiplex relational space}
}
$$

中發生。

---

# 5. 關係認知距離

每種 relation：

$$
r
$$

有權重：

$$
w_r(G_t).
$$

定義 aggregate accessibility：

$$
\kappa_t(x,y\mid G_t)
=
F
\left(
\kappa_S,
\kappa_C,
\kappa_A,
\kappa_P,
\kappa_T,
\kappa_G,
\kappa_K
\right).
$$

若 path：

$$
\gamma
=
x_0\rightarrow x_1\rightarrow\cdots\rightarrow x_n,
$$

可定義：

$$
K_{\mathrm{rel}}(\gamma\mid G)
=
-\sum_{i=0}^{n-1}
\log
\kappa(
x_i,x_{i+1}\mid G
).
$$

因此：

$$
\boxed{
d_{\mathrm{rel}}(x,y\mid G)
=
\min_{\gamma:x\leadsto y}
K_{\mathrm{rel}}(\gamma\mid G).
}
$$

---

# 6. 為什麼使用 goal-conditioned distance？

同兩個 concepts：

$$
x,y
$$

在不同問題下可能：

$$
d_{\mathrm{rel}}(x,y\mid G_1)
\ll
d_{\mathrm{rel}}(x,y\mid G_2).
$$

例如：

在：

$$
G_1
=
\text{compare feedback structures}
$$

時，

兩個不同學科系統可能非常近。

但在：

$$
G_2
=
\text{compare empirical measurement protocols}
$$

時，

它們可能非常遠。

因此：

$$
\boxed{
d_{\mathrm{rel}}
=
d_{\mathrm{rel}}(x,y\mid G).
}
$$

---

# 7. Relation-First Cognition Conjecture（RFCC）

RFCC 宣稱：

> 在至少部分高階推理與知識轉移任務中，goal-conditioned relational distance 比 external disciplinary distance 更能預測 transition cost、inference success 與 transfer。

形式：

$$
\boxed{
\operatorname{Pred}
(
d_{\mathrm{rel}}
)
>
\operatorname{Pred}
(
d_{\mathrm{ext}}
)
}
$$

在適當控制：

- familiarity；
- word similarity；
- education；
- exposure；
- motor / perceptual demands；

後成立。

---

# 8. 「關係優先」不是「語義優先」

semantic similarity：

$$
s_{\mathrm{sem}}(x,y)
$$

只是：

$$
\mathcal G
$$

的一層。

兩個表面語義很遠的情境：

$$
s_{\mathrm{sem}}\downarrow
$$

可能仍有：

$$
s_{\mathrm{struct}}\uparrow.
$$

這正是 analogy literature 長期研究的核心現象之一。

所以：

$$
\boxed{
\text{relation-first}
\neq
\text{semantic-similarity-first}.
}
$$

---

# 9. Analogical Mapping 的既有基礎

analogical reasoning 經常要求：

$$
\text{source}
\leftrightarrow
\text{target}
$$

表面 items 不同，

但：

$$
\text{relational structure}
$$

相似。

因此：

$$
\boxed{
\text{surface dissimilarity}
+
\text{structural similarity}
}
$$

不是新發現。

TADC-06 的新問題是：

> 這種 structural similarity 是否能被提升為對 cognitive transition distance 的一般描述？

---

# 10. 跨 modality analogy

Weinberger 等人（2022）研究 analogical mapping across sensory modalities，顯示 analogy ability 並不只局限於單一資訊 modality。

這支持：

$$
\boxed{
\text{relational mapping can cross
surface representational format}.
}
$$

但跨 modality 不等於跨 disciplinary domain。

因此只是鄰接證據。

---

# 11. Cross-Domain Generalization 的計算模型

Doumas、Puebla、Martin 與 Hummel（2022）提出 relation-learning / cross-domain generalization theory。

該模型能：

- 從簡單 visual stimuli 學 relational representations；
- 在 Breakout 與 Pong 等不同 domains 間 generalize；
- 在不同心理任務之間做 relational transfer。

這提供一個重要 possibility proof：

$$
\boxed{
\text{cross-domain transfer can be modeled
through structured relational representations}.
}
$$

但 computational sufficiency 不等於 human cognitive necessity。

---

# 12. Relational Re-representation

Lu、Wu 與 Holyoak 等人的 analogical re-representation work 顯示：

analogical mapping 過程中，

relation representation 本身可能發生改變，

以允許原本不完全相同的 relations 被重新對齊。

因此 analogy 不一定只是：

$$
\text{find existing isomorphism}.
$$

也可能：

$$
\boxed{
\text{transform representations so alignment becomes possible}.
}
$$

這與 TADC-01 的 ASTC 非常接近。

---

# 13. Relational Re-representation Conjecture（RRC）

本文提出更一般版本：

若：

$$
x,y
$$

原本：

$$
d_{\mathrm{rel}}^{(t)}(x,y)
\gg0,
$$

經：

$$
\text{alignment / abstraction / schema induction}
$$

後：

$$
d_{\mathrm{rel}}^{(t+1)}(x,y)
<
d_{\mathrm{rel}}^{(t)}(x,y),
$$

則：

$$
\boxed{
\text{cognitive distance itself has been transformed}.
}
$$

RRC 宣稱：

$$
\boxed{
\text{cross-domain reasoning can sometimes
change the relational metric it uses}.
}
$$

---

# 14. Schema Drift

Vagnino 與 Walker 的 2025/2026 Cognition work 研究：

$$
\text{abstract relational schemas}
$$

是否會在類比使用中改變。

結果指出 abstract schemas 在特定條件下確實會 drift。

這是一個很重要的鄰接結果：

$$
\boxed{
\text{relational abstraction itself can be plastic}.
}
$$

但 schema drift 不自動證明：

$$
\text{attention topology}.
$$

它只使：

$$
\mathcal R_t
\neq
\mathcal R_{t+1}
$$

變得更加實驗上可信。

---

# 15. Cross-Domain Continuity Conjecture（CDCC）

令一條 trajectory：

$$
\gamma
=
(x_0,x_1,\ldots,x_n).
$$

外部 taxonomy：

$$
L_{\mathrm{ext}}(x_i)
$$

可能頻繁改變。

如果：

$$
d_{\mathrm{rel}}
(
x_i,x_{i+1}
\mid G
)
\leq
\epsilon
$$

對大部分 \(i\) 成立，

則在 relational topology 中：

$$
\gamma
$$

仍是一條 low-cost path。

因此：

$$
\boxed{
\text{external domain discontinuity}
\not\Rightarrow
\text{relational cognitive discontinuity}.
}
$$

---

# 16. 跨域落差量

定義：

$$
\boxed{
\Delta_{\mathrm{cross}}
(
x,y\mid G
)
=
\widehat d_{\mathrm{ext}}(x,y)
-
\widehat d_{\mathrm{rel}}(x,y\mid G)
}
$$

其中兩距離先標準化。

---

# 17. 四種情形

## Type I — Same-domain / Relationally Local

$$
d_{\mathrm{ext}}\downarrow,
\qquad
d_{\mathrm{rel}}\downarrow.
$$

最普通。

---

## Type II — Cross-domain / Relationally Local

$$
d_{\mathrm{ext}}\uparrow,
\qquad
d_{\mathrm{rel}}\downarrow.
$$

即：

$$
\Delta_{\mathrm{cross}}\gg0.
$$

這是 TADC-06 最關注情形。

---

## Type III — Same-domain / Relationally Distant

$$
d_{\mathrm{ext}}\downarrow,
\qquad
d_{\mathrm{rel}}\uparrow.
$$

外部分類相同，

但 cognition 可能需要大幅重建。

---

## Type IV — Cross-domain / Relationally Distant

$$
d_{\mathrm{ext}}\uparrow,
\qquad
d_{\mathrm{rel}}\uparrow.
$$

真正的高成本跨域。

---

# 18. 所以「跨領域能力」本身也要重新拆

一般說某人：

$$
\text{cross-domain ability}\uparrow.
$$

可能至少表示：

### A. Low Relational Distance

他已經建立很多跨 domain bridge。

### B. High Translation Ability

即使 distance 大，

也能做 chart translation。

### C. High Search Ability

能找出 hidden alignment。

### D. High Re-representation Ability

能改造表示以產生 alignment。

### E. High Re-indexing Ability

能換尺度重新描述問題。

因此：

$$
\boxed{
\text{cross-domain cognition}
\neq
\text{one scalar talent}.
}
$$

---

# 19. Structural Alignment Score

對兩個 local structures：

$$
U_A,
U_B,
$$

定義候選：

$$
S_{\mathrm{align}}
(
U_A,U_B
)
$$

考慮：

- role correspondence；
- relation type correspondence；
- causal ordering；
- graph motif；
- constraint structure；
- goal role。

例如：

$$
S_{\mathrm{align}}
=
\alpha S_R
+
\beta S_C
+
\gamma S_G
+
\delta S_M.
$$

---

# 20. 高 alignment 不要求 item similarity

可能：

$$
S_{\mathrm{item}}\approx0
$$

但：

$$
S_{\mathrm{align}}\approx1.
$$

這正是：

$$
\boxed{
\text{deep analogy}.
}
$$

所以 TADC 的 distance 應讓：

$$
S_{\mathrm{align}}
$$

降低：

$$
d_{\mathrm{rel}}.
$$

---

# 21. Bridge Object / Bridge Relation

TADC-02 已定義 bridge object。

本文加入：

$$
B_{\alpha\beta}
=
\{
b:
b
\text{ supports low-cost relational translation}
\}.
$$

bridge 不一定是一個 object。

它可能是一個 relation pattern：

$$
r^*.
$$

例如：

$$
r^*
=
\text{feedback loop}.
$$

則：

$$
r^*
$$

可以同時連接：

- biology；
- control engineering；
- economics；
- cognition。

---

# 22. Bridge Density

定義：

$$
\rho_B
(
U_A,U_B
)
=
\frac{
|B_{AB}|
}{
|U_A|+|U_B|
}
$$

或 weighted version：

$$
\rho_B^w
=
\sum_{b\in B}
w_b.
$$

候選預測：

$$
\rho_B\uparrow
\Rightarrow
K_{\mathrm{switch}}\downarrow.
$$

---

# 23. Translation Cost

沿用 TADC-02：

$$
K_{\alpha\beta}
=
K_{\mathrm{retrieval}}
+
K_{\mathrm{recode}}
+
K_{\mathrm{context}}
+
K_{\mathrm{loss}}.
$$

加入：

$$
K_{\mathrm{align}}.
$$

因此：

$$
\boxed{
K_{\alpha\beta}
=
K_R+K_C+K_L+K_A.
}
$$

若：

$$
S_{\mathrm{align}}\uparrow,
$$

通常預測：

$$
K_A\downarrow.
$$

---

# 24. Cognitive Discontinuity Index

定義：

$$
\operatorname{CDI}(x,y)
=
\alpha K_{\mathrm{context}}
+
\beta K_{\mathrm{align}}
+
\gamma K_{\mathrm{retrieval}}
+
\delta d_{\mathrm{rel}}.
$$

如果：

$$
CDI\downarrow
$$

即使：

$$
d_{\mathrm{ext}}\uparrow,
$$

實際 transition 可能仍然流暢。

---

# 25. 跨域連續不是「沒有切換」

重要限制：

如果：

$$
L_{\mathrm{ext}}(x)\neq L_{\mathrm{ext}}(y),
$$

外部分類確實改變。

CDCC 不是否認這件事。

而是說：

$$
\boxed{
\text{categorical switch}
\neq
\text{high cognitive discontinuity}.
}
$$

---

# 26. Relation-First 與 Category-First

定義兩種理想化 policy。

## Category-First

先：

$$
L(x)
$$

再找 domain-specific method：

$$
M_{L(x)}.
$$

流程：

$$
x
\rightarrow
D_i
\rightarrow
M_i.
$$

---

## Relation-First

先抽：

$$
\mathcal R(x)
$$

再找：

$$
\mathcal R(y)
\approx
\mathcal R(x).
$$

流程：

$$
x
\rightarrow
r^*
\rightarrow
\{y_1,y_2,\ldots\}.
$$

---

# 27. 兩者不應被道德化

Category-first 在很多領域很有效：

- 法律；
- medicine；
- engineering standards；
- taxonomy；
- regulated procedure。

Relation-first 對：

- analogy；
- theory transfer；
- creativity；
- model reuse；
- abstraction；

可能更有效。

所以：

$$
\boxed{
\text{relation-first}
\neq
\text{universally superior}.
}
$$

它是一種 task-dependent policy。

---

# 28. Relation-First Policy Selector

令：

$$
P_{\mathrm{RF}}
=
P(
\text{relation-first}
\mid
G,
X,
R,
C
).
$$

如果 goal：

$$
G
$$

要求：

- novel transfer；
- cross-domain inference；
- structural discovery；

則：

$$
P_{\mathrm{RF}}\uparrow
$$

可能更有效。

若要求：

- strict compliance；
- exact domain convention；
- fixed procedure；

則：

$$
P_{\mathrm{RF}}\downarrow
$$

可能更有效。

---

# 29. Semantic Control 的鄰接證據

Wang 等人（2024）使用相同或高度匹配 stimuli，

比較：

- global semantic association；
- semantic feature matching；
- non-semantic control tasks。

其結果顯示：

不同 retrieval demands 形成不同 macroscale brain-state configurations。

這支持：

$$
\boxed{
\text{same inputs can induce different effective
relational retrieval states depending on goal}.
}
$$

但這不是 RFCC 的直接證明。

---

# 30. Task-Space Cognitive Maps

Tan 等人（2025）顯示 medial / lateral OFC 等區域對 task-space cognitive map 有互補表徵，

支持：

$$
\boxed{
\text{task-relevant abstract state structure
can be explicitly represented}.
}
$$

這使：

$$
d_{\mathrm{rel}}(x,y\mid G)
$$

不再只是語言遊戲。

但仍需行為與 neural data 共同驗證。

---

# 31. 關係空間可以不是唯一的

同一：

$$
X
$$

可有：

$$
\mathcal G^{(causal)},
$$

$$
\mathcal G^{(semantic)},
$$

$$
\mathcal G^{(procedural)}.
$$

因此：

$$
\boxed{
\text{one object set}
\neq
\text{one cognitive topology}.
}
$$

goal：

$$
G
$$

決定哪一層 weighting 上升。

---

# 32. Relation Layer Switching

如果從：

$$
E^{(S)}
$$

切到：

$$
E^{(C)},
$$

即由 semantic similarity 看問題，

改成 causal structure 看問題，

這是一種：

$$
\boxed{
\text{relation-layer switch}.
}
$$

它可能：

$$
X_t=X_{t+1}
$$

但：

$$
d_{\mathrm{rel}}^{(t)}
\neq
d_{\mathrm{rel}}^{(t+1)}.
$$

這又是一種 TADC-01 式 space transformation。

---

# 33. 跨域推理的三階段

候選模型：

### Stage 1 — Retrieval

找：

$$
U_B
$$

作為 candidate source。

### Stage 2 — Alignment

計算：

$$
S_{\mathrm{align}}(U_A,U_B).
$$

### Stage 3 — Re-representation

必要時：

$$
\mathcal R_A,\mathcal R_B
\rightarrow
\widetilde{\mathcal R}_A,
\widetilde{\mathcal R}_B
$$

使共通結構可被抽取。

---

# 34. 第四階段：Transfer

建立：

$$
M:
U_A
\rightsquigarrow
U_B.
$$

如果：

$$
M
$$

支援 novel inference，

才算真正 cross-domain transfer。

單純說：

> 「這兩個很像。」

不夠。

---

# 35. 第五階段：Schema Update

從 source / target 對齊後形成：

$$
S^*.
$$

而：

$$
S^*
$$

會影響未來：

$$
d_{\mathrm{rel}}.
$$

因此：

$$
\boxed{
\text{cross-domain transfer
can alter future cross-domain distance}.
}
$$

這是 RRC / schema-drift 方向最重要的推論。

---

# 36. Distance Plasticity

定義：

$$
\Delta d_{\mathrm{rel}}
=
d_{\mathrm{rel}}^{\mathrm{post}}
-
d_{\mathrm{rel}}^{\mathrm{pre}}.
$$

若 alignment learning 後：

$$
\Delta d_{\mathrm{rel}}<0,
$$

則 cognitive distance 被壓縮。

若錯誤 analogy 被修正：

$$
\Delta d_{\mathrm{rel}}>0,
$$

則 cognitive distance 被拉開。

所以：

$$
\boxed{
d_{\mathrm{rel}}
\text{ itself may be plastic}.
}
$$

---

# 37. Relation Compression

多個 domains：

$$
D_1,\ldots,D_n
$$

若共享：

$$
r^*,
$$

則可以 coarse-grain 成：

$$
\boxed{
[r^*]
}
$$

這是一個 relation-centered super-domain。

例如：

$$
\{D_1,D_2,D_3\}
\rightarrow
U_{r^*}.
$$

這是一種 TADC-04 Re-indexing。

---

# 38. 所謂「沒有領域」的嚴格版本

本文不使用：

> 沒有任何領域。

而使用：

$$
\boxed{
\text{No fixed single partition is assumed
to be cognitively privileged across all goals}.
}
$$

中文：

> **不假定存在一套對所有目標都具有認知優先性的固定領域分割。**

這比「領域不存在」精確得多。

---

# 39. 多個合法 atlas

同一：

$$
X
$$

可能有：

$$
\mathfrak A^{(disciplinary)},
$$

$$
\mathfrak A^{(causal)},
$$

$$
\mathfrak A^{(formal)},
$$

$$
\mathfrak A^{(procedural)}.
$$

不同 atlas 可能都有效，

但適用 goal 不同。

因此：

$$
\boxed{
\text{multiple valid atlases}
\neq
\text{no structure}.
}
$$

---

# 40. Relation-First Cognition 的風險：錯誤 analogy

若看到：

$$
r_A\approx r_B
$$

就過度 transfer，

可能造成：

$$
\boxed{
\text{false structural equivalence}.
}
$$

例如：

- surface relation 類似但 causal mechanism 不同；
- mathematical form 相同但 domain assumptions 不同；
- control architecture 類似但 scale / noise regime 不同。

所以 RFCC 需要：

$$
\boxed{
\text{alignment}
+
\text{constraint checking}.
}
$$

---

# 41. Constraint-Preserving Mapping

一個合法 mapping：

$$
M:U_A\rightarrow U_B
$$

不能只保 relation names。

還要測：

$$
C_A
\rightarrow
C_B.
$$

定義：

$$
Q_M
=
S_{\mathrm{align}}
-
\lambda
L_{\mathrm{constraint}}.
$$

其中：

$$
L_{\mathrm{constraint}}
$$

是 constraint violation。

只有：

$$
Q_M>\theta
$$

才接受 transfer。

---

# 42. Cross-Domain Hallucination

在 human / AI reasoning 中，

若：

$$
S_{\mathrm{surface}}\uparrow
$$

但：

$$
S_{\mathrm{constraint}}\downarrow,
$$

仍強行 Gluing，

會產生：

$$
\boxed{
\text{cross-domain hallucination}.
}
$$

這裡 hallucination 只是廣義錯誤結構對齊，

不是精神醫學術語。

---

# 43. Detachment 在跨域研究中的必要性

TADC-03 的：

$$
D
=
\text{Detachment}
$$

在這裡尤其重要。

一個 analogy：

$$
A\leftrightarrow B
$$

部分成立，

不能因此所有 relations 都被 Gluing。

需要：

$$
D[
R_{\mathrm{invalid}}
].
$$

因此成熟 relation-first cognition 不是：

$$
G\rightarrow G\rightarrow G
$$

而是：

$$
\boxed{
G
\rightarrow
\text{test}
\rightarrow
D
\rightarrow
G_{\mathrm{valid}}.
}
$$

---

# 44. Cross-Domain Continuity Ratio

對 trajectory：

$$
\gamma=(x_1,\ldots,x_n),
$$

定義：

$$
CCR(\gamma)
=
\frac{
\sum_i
\mathbf 1[
d_{\mathrm{rel}}(x_i,x_{i+1}\mid G)<\theta
]
}{
n-1
}.
$$

如果：

$$
CCR\rightarrow1,
$$

即使 external labels 頻繁改變，

trajectory 仍具有高 relational continuity。

---

# 45. External Switching Ratio

定義：

$$
ESR(\gamma)
=
\frac{
\sum_i
\mathbf 1[
L_{\mathrm{ext}}(x_i)
\neq
L_{\mathrm{ext}}(x_{i+1})
]
}{
n-1
}.
$$

關鍵 signature：

$$
\boxed{
ESR\uparrow
\quad\land\quad
CCR\uparrow.
}
$$

也就是：

> 表面高跨域，內部高連續。

---

# 46. Relation-First Signature

因此候選 relation-first trajectory：

$$
\Theta_{RF}
=
(
ESR,
CCR,
S_{\mathrm{align}},
K_{\mathrm{translation}},
P_{\mathrm{return}},
Q_M
).
$$

如果：

$$
ESR\uparrow,
CCR\uparrow,
K_{\mathrm{translation}}\downarrow,
Q_M\uparrow,
$$

比「random switching」更符合 RFCC。

---

# 47. 與 TADC-05 的連接

TADC-05：

$$
H_{\mathrm{macro}}\downarrow
\land
H_{\mathrm{micro}}\uparrow.
$$

TADC-06 現在補：

即使 micro topics 跨 external disciplines：

$$
H_{\mathrm{ext-domain}}\uparrow,
$$

只要：

$$
CCR\uparrow
$$

仍可屬於同一 higher-order cognitive complex。

因此：

$$
\boxed{
\text{domain hyperfocus}
}
$$

不必等於：

$$
\boxed{
\text{discipline hyperfocus}.
}
$$

---

# 48. Null Model 1：Taxonomy-Only

假設：

$$
K_{\mathrm{switch}}
=
f(
d_{\mathrm{ext}}
).
$$

如果外部學科距離已穩定預測：

- RT；
- error；
- transfer；
- re-entry；

則 RFCC 沒必要。

---

# 49. Null Model 2：Surface Similarity

假設：

$$
K_{\mathrm{switch}}
=
f(
1-s_{\mathrm{surface}}
).
$$

如果普通 lexical / perceptual / semantic similarity 已完整解釋，

不用 structural relation。

---

# 50. Null Model 3：Fixed Semantic Embedding

假設存在：

$$
Z_{\mathrm{sem}}
$$

固定。

只需 embedding cosine distance：

$$
d_Z(x,y)
$$

即可。

如果：

$$
d_{\mathrm{rel}}
$$

無法提供增量，

multiplex relational topology 沒必要。

---

# 51. Null Model 4：Ordinary Analogy

也可能 TADC-06 只是：

$$
\boxed{
\text{analogy theory renamed}.
}
$$

這是一個真正風險。

若 RFCC 只在 explicit analogy tasks 成立，

而無法預測：

- spontaneous topic transition；
- switching cost；
- domain return；
- research problem navigation；

那它應被限制為 analogy subtheory。

---

# 52. Null Model 5：Expertise Only

專家跨域流暢，

可能只是：

$$
\text{more knowledge}.
$$

如果控制：

$$
\text{expertise},
\text{familiarity},
\text{retrieval fluency}
$$

後，

relation distance 不再有預測力，

RFCC 被削弱。

---

# 53. Null Model 6：Random Association

高 branching：

$$
\nu_{\mathrm{switch}}\uparrow
$$

可能只是 diffuse association。

如果 transitions：

$$
d_{\mathrm{rel}}
$$

並不比隨機 baseline 短，

則：

$$
CCR
$$

不成立。

---

# 54. 實驗一：Crossed Distance Matrix

建立四類 pairs：

1. same-domain / relationally near；
2. same-domain / relationally far；
3. cross-domain / relationally near；
4. cross-domain / relationally far。

控制：

- familiarity；
- word frequency；
- surface similarity；
- task difficulty。

測：

$$
RT,
Accuracy,
Transfer,
Memory.
$$

---

# 55. 關鍵比較

RFCC 預測：

$$
K(
\text{cross-domain, relationally near}
)
<
K(
\text{same-domain, relationally far}
).
$$

如果反覆成立，

就是非常強的證據：

$$
\boxed{
d_{\mathrm{rel}}
>
d_{\mathrm{ext}}
\text{ in predictive importance}.
}
$$

---

# 56. 實驗二：Bridge Induction

先測：

$$
d_{\mathrm{rel}}^{pre}
(
U_A,U_B
).
$$

再教一個 shared relational schema：

$$
r^*.
$$

之後測：

$$
d_{\mathrm{rel}}^{post}.
$$

RRC 預測：

$$
d_{\mathrm{rel}}^{post}
<
d_{\mathrm{rel}}^{pre}.
$$

---

# 57. 實驗三：False Bridge

建立 surface-similar 但 structurally invalid pair。

若 relation-first cognition 成熟，

經 constraint feedback 後應：

$$
d_{\mathrm{rel}}\uparrow
$$

或：

$$
Q_M\downarrow.
$$

這直接測：

$$
\boxed{
\text{Detachment of false analogy}.
}
$$

---

# 58. 實驗四：Re-representation

提供兩個 relations：

$$
r_A,r_B
$$

初始不容易對齊。

經 analogy task 後測：

- predicate interpretation；
- relation categorization；
- transfer；
- change detection。

若 representations 本身改變：

$$
\mathcal R_t
\rightarrow
\mathcal R_{t+1},
$$

支持 RRC。

---

# 59. 實驗五：Spontaneous Cross-Domain Navigation

不提示 analogy。

給 open-ended problem solving task。

記錄：

$$
x_1\rightarrow x_2\rightarrow\cdots
$$

並事後建立：

- external labels；
- semantic distance；
- structural distance；
- causal distance；
- goal relevance。

測：

$$
K_{\mathrm{switch}}
$$

到底最受哪個 distance 預測。

---

# 60. 實驗六：Return Path

如果：

$$
x_i
$$

跨到：

$$
y_j
$$

再返回：

$$
x_{i+k},
$$

測：

$$
P_{\mathrm{return}}
$$

是否被 structural bridge 預測。

RFCC 預測：

$$
S_{\mathrm{align}}\uparrow
\Rightarrow
P_{\mathrm{return}}\uparrow.
$$

---

# 61. 實驗七：Multi-Atlas Task

同一 object set：

$$
X
$$

先按：

$$
\mathfrak A^{(disciplinary)}
$$

操作，

再按：

$$
\mathfrak A^{(causal)}
$$

或：

$$
\mathfrak A^{(formal)}
$$

操作。

測：

- performance；
- switch cost；
- novel inference；
- neural representational geometry。

如果某 goal 下：

$$
\mathfrak A^{(causal)}
$$

明顯勝過：

$$
\mathfrak A^{(disciplinary)},
$$

支持 multiple-valid-atlas model。

---

# 62. 實驗八：Schema Drift

對同一 relational schema：

$$
S
$$

反覆應用到不同 domains：

$$
D_1,D_2,\ldots,D_n.
$$

追蹤：

$$
S_0\rightarrow S_1\rightarrow\cdots.
$$

測其：

- boundary；
- prototype；
- inference pattern；
- transfer errors。

如果 schema 會因應用 history 改變，

支持：

$$
\boxed{
\text{relation-space plasticity}.
}
$$

---

# 63. 八個核心可證偽命題

## TADC6-H1 — Relational Distance Predicts Switching

控制 external taxonomy 後：

$$
d_{\mathrm{rel}}
$$

仍預測：

$$
K_{\mathrm{switch}}.
$$

---

## TADC6-H2 — Cross-Domain Near Can Beat Same-Domain Far

存在：

$$
K_{CN}
<
K_{SF},
$$

其中：

- \(CN\)：cross-domain relationally near；
- \(SF\)：same-domain relationally far。

---

## TADC6-H3 — Bridge Learning Compresses Distance

$$
d_{\mathrm{rel}}^{post}
<
d_{\mathrm{rel}}^{pre}.
$$

---

## TADC6-H4 — False Analogy Can Be Detached

constraint feedback 後：

$$
Q_M\downarrow
$$

且 erroneous transfer 減少。

---

## TADC6-H5 — Relational Re-representation

analogical alignment 後：

$$
\mathcal R_t
\neq
\mathcal R_{t+1}
$$

具有獨立 behavioral signature。

---

## TADC6-H6 — High ESR Can Coexist with High CCR

存在 trajectories：

$$
ESR\uparrow
\land
CCR\uparrow.
$$

---

## TADC6-H7 — Multiple Atlases Have Goal-Specific Value

不同：

$$
\mathfrak A_i
$$

對不同：

$$
G_j
$$

具有不同 predictive utility。

---

## TADC6-H8 — Relation Model Adds Prediction

multiplex relational model：

$$
M_R
$$

必須在 out-of-sample prediction 上優於：

- taxonomy；
- surface similarity；
- semantic embedding；
- familiarity；

模型。

---

# 64. 什麼會殺掉 RFCC / CDCC？

## F1 — Taxonomy Wins

若：

$$
d_{\mathrm{ext}}
$$

穩定優於：

$$
d_{\mathrm{rel}},
$$

RFCC 強版失敗。

---

## F2 — Semantic Embedding Is Enough

若：

$$
d_Z
$$

完全吸收 structural relation effect，

multiplex model 過度複雜。

---

## F3 — Relation Effect Disappears after Familiarity Control

若：

$$
\text{expertise / familiarity}
$$

解釋全部效果，

relation-first 不需要。

---

## F4 — No High-ESR / High-CCR Trajectories

若 external domain switching 高時，

relational continuity 必然低，

CDCC 被否定。

---

## F5 — Re-representation Is Not Needed

若 alignment 只是在固定 representation 中匹配，

RRC 強版失敗。

---

## F6 — Schema Drift Has No Functional Consequence

若 schema representation 改變，

但不影響 future inference / transfer，

distance-plasticity 說法被削弱。

---

## F7 — Relation-First Only Works in Explicit Analogy Tasks

則本篇應縮減為 analogy theory extension，

不能宣稱一般 cognitive-domain continuity。

---

# 65. Relation-First 的最小模型

令：

$$
\mathcal G_t
=
(V,E^{(1)},\ldots,E^{(m)}).
$$

goal-conditioned weighting：

$$
\mathbf w_t(G)
=
(
w_1,\ldots,w_m
).
$$

有效 graph：

$$
\mathcal G_t^G
=
\sum_r
w_r(G)
E^{(r)}.
$$

認知距離：

$$
d_{\mathrm{rel}}^G
=
d(
\mathcal G_t^G
).
$$

因此：

$$
\boxed{
\text{goal changes}
\Rightarrow
\text{effective topology changes}.
}
$$

---

# 66. Cross-Domain Continuity 的最小判準

對 trajectory：

$$
\gamma.
$$

若：

$$
ESR(\gamma)\geq\theta_E
$$

且：

$$
CCR(\gamma)\geq\theta_C,
$$

則稱：

$$
\boxed{
\text{surface-cross-domain but relationally continuous trajectory}.
}
$$

這只是描述性分類。

要升級成認知機制，

仍需：

$$
CCR
$$

預測 behavior / neural dynamics。

---

# 67. 與 TADC-03 六算子的統一

Relation-first cognition 可以直接映射到：

### Expansion

發現新 source domain：

$$
E.
$$

### Traversal

沿 relational path：

$$
T.
$$

### Gluing

建立 analogy bridge：

$$
G.
$$

### Detachment

移除 invalid transfer：

$$
D.
$$

### Re-indexing

把兩個具體 domains 壓成：

$$
r^*
$$

的 abstract schema：

$$
R^-.
$$

再把 schema 套回新 domain：

$$
R^+.
$$

---

# 68. 一條典型跨域推理路徑

$$
x_A
\overset{E}{\longrightarrow}
U_B
\overset{G}{\longrightarrow}
B_{AB}
\overset{R^-}{\longrightarrow}
S^*
\overset{R^+}{\longrightarrow}
U_C
\overset{D}{\longrightarrow}
S_{\mathrm{valid}}.
$$

這比：

$$
A\rightarrow B\rightarrow C
$$

的「換領域」描述多出了真正結構內容。

---

# 69. 與 TADC-04 的統一

若：

$$
U_A,U_B,U_C
$$

在 fine scale 是不同 domains，

但：

$$
R^-
$$

後都變成：

$$
z_{r^*},
$$

則 coarse scale：

$$
d_{\mathrm{rel}}
(
U_A,U_B
)
\rightarrow0.
$$

因此：

$$
\boxed{
\text{cross-domain distance can collapse
under relational coarse-graining}.
}
$$

這是 TADC-04 scale relativity 在跨域認知上的直接結果。

---

# 70. 與 TADC-05 的統一

若 long-focus trajectory：

$$
\gamma
$$

跨：

$$
D_1,D_2,\ldots,D_n
$$

但：

$$
CCR(\gamma)\uparrow
$$

且：

$$
G_C\uparrow,
$$

則這些 external switches 不一定破壞：

$$
\boxed{
\text{Topological Hyperfocus}.
}
$$

也就是：

$$
\boxed{
\text{disciplinary diversity}
\neq
\text{attentional fragmentation}.
}
$$

---

# 71. Cross-Domain Entropy

外部分類 entropy：

$$
H_{\mathrm{ext}}
=
-\sum_Dp(D)\log p(D).
$$

relation-family entropy：

$$
H_R
=
-\sum_rp(r)\log p(r).
$$

一條 trajectory 可以：

$$
H_{\mathrm{ext}}\uparrow
$$

但：

$$
H_R\downarrow,
$$

如果它一直在追同一種 structure。

例如跨很多 domains，

但都在追：

$$
r^*
=
\text{feedback}.
$$

---

# 72. 反過來也可能

外部 domain：

$$
D
$$

固定，

但 relation families：

$$
r_1,r_2,\ldots
$$

一直亂跳。

所以：

$$
H_{\mathrm{ext}}\downarrow
$$

但：

$$
H_R\uparrow.
$$

這再次說明：

$$
\boxed{
\text{discipline entropy}
\neq
\text{cognitive relation entropy}.
}
$$

---

# 73. Relation-Locked Attention

本文提出一個不等於 hyperfocus 的中性描述：

$$
\boxed{
\text{Relation-Locked Attention（RLA）}.
}
$$

若：

$$
P(r^*\mid\gamma)\rightarrow1,
$$

即使：

$$
P(D_i)
$$

分散，

可說 attention 長期鎖定某個 relation family。

這個構念比：

$$
\text{domain lock}
$$

更抽象。

---

# 74. RLA 與 THF 的差別

THF：

$$
\boxed{
\text{persistent evolving cognitive complex}.
}
$$

RLA：

$$
\boxed{
\text{persistent relation family}.
}
$$

RLA 可以是 THF 的一個 invariant：

$$
I_R(\mathcal K_t)=r^*.
$$

如果：

$$
r^*
$$

在多次 domain changes 中保持，

它可能就是 TADC-04 所求的 cross-scale invariant 候選之一。

---

# 75. 關係不變量

假設：

$$
M_i:
U_i\rightarrow U_{i+1}.
$$

如果：

$$
I_R(U_i)
=
I_R(U_{i+1}),
$$

則：

$$
I_R
$$

是 relational invariant。

例如：

$$
\boxed{
\text{feedback structure}
}
$$

可能在 biological / computational / social systems 中保持。

但真正合法 transfer 還要保：

$$
\text{constraints}.
$$

---

# 76. Relation Invariant ≠ Mechanism Identity

兩個 systems 共享：

$$
I_R
$$

不表示：

$$
\text{mechanism}_A
=
\text{mechanism}_B.
$$

因此：

$$
\boxed{
\text{structural invariance}
\neq
\text{ontological identity}.
}
$$

這是避免跨域理論過度膨脹的重要限制。

---

# 77. 可驗證的「領域沒有領域」版本

最強但仍合法的命題不是：

$$
\text{there are no domains}.
$$

而是：

$$
\boxed{
\text{No single external domain partition
is assumed to dominate cognitive adjacency
for every high-level goal.}
}
$$

若實驗最後顯示：

$$
\Pi^{\mathrm{ext}}
$$

在所有 task 上都最有預測力，

這句就被否定。

---

# 78. 研究方法上的重要後果

若 RFCC 可能成立，

研究 cross-domain cognition 時不能只記：

$$
\text{how many labels changed}.
$$

還要記：

- relational distance；
- mapping quality；
- bridge structure；
- constraint preservation；
- re-representation；
- return path；
- goal continuity。

否則會把：

$$
\boxed{
\text{relational traversal}
}
$$

誤判成：

$$
\boxed{
\text{cognitive fragmentation}.
}
$$

---

# 79. TADC-06 最小預測模型

定義 switch cost：

$$
K_{i\rightarrow j}
=
\beta_0
+
\beta_1d_{\mathrm{ext}}
+
\beta_2d_{\mathrm{sem}}
+
\beta_3d_{\mathrm{rel}}
+
\beta_4F
+
\beta_5E
+
\epsilon.
$$

其中：

- \(F\)：familiarity；
- \(E\)：expertise。

RFCC 最小要求：

$$
\boxed{
\beta_3>0
}
$$

且加入：

$$
d_{\mathrm{rel}}
$$

後，

out-of-sample prediction 提升。

---

# 80. 強版本預測

更強：

$$
|\beta_3|
>
|\beta_1|
$$

在 cross-domain transfer task 中成立。

但本文不把這個不等式當必要條件。

只要：

$$
\Delta\operatorname{Prediction}_{d_{\mathrm{rel}}}>0
$$

就有增量價值。

---

# 81. 最小資料集

一個未來 dataset 至少應有：

$$
\{
x_i,
L_i,
G_i,
R_{ij},
d_{\mathrm{sem}},
d_{\mathrm{rel}},
t_i,
K_i,
Y_i
\}.
$$

其中：

- cognitive state；
- external label；
- goal；
- relation type；
- distances；
- timestamp；
- switch cost；
- outcome。

這樣才能真正驗證：

$$
d_{\mathrm{ext}}
$$

與：

$$
d_{\mathrm{rel}}
$$

誰更重要。

---

# 82. 不能只靠自我報告

一個 participant 說：

> 我覺得這兩個領域其實一樣。

不是證據。

必須有：

- RT；
- error；
- transfer；
- novel inference；
- eye tracking；
- transition sequence；
- neural representation；
- predictive model；

等 independent observables。

因此：

$$
\boxed{
\text{subjective continuity}
\neq
\text{measured continuity}.
}
$$

---

# 83. 也不能只靠 embedding

LLM embedding：

$$
z(x)
$$

可以估 semantic distance，

但：

$$
\boxed{
\text{embedding similarity}
\neq
\text{human relational distance}.
}
$$

尤其：

- causal；
- procedural；
- analogical；
- goal；

關係可能和一般 semantic embedding 不一致。

embedding 可以是 proxy，

不能直接當 ground truth。

---

# 84. 人–AI 情境暫時不在本篇證明

AI 可以：

- 找 analogy；
- 補 bridge；
- 保存 context；
- 降低 retrieval cost；
- 建 relational graphs。

這可能大幅改變：

$$
d_{\mathrm{rel}}^{\mathrm{effective}}.
$$

但那是 TADC-07 的主題。

TADC-06 先建立：

$$
\boxed{
\text{relation-first cognition}
}
$$

本身。

---

# 85. 核心理論總結

本文提出：

$$
\boxed{
\mathcal G_t^G
=
\sum_r
w_r(G)E^{(r)}
}
$$

以及：

$$
\boxed{
d_{\mathrm{rel}}(x,y\mid G)
=
\min_{\gamma:x\leadsto y}
K_{\mathrm{rel}}(\gamma\mid G).
}
$$

與外部分類：

$$
d_{\mathrm{ext}}(x,y)
$$

比較。

---

# 86. 三個根猜想

## RFCC

$$
\boxed{
d_{\mathrm{rel}}
\text{ adds predictive value beyond }
d_{\mathrm{ext}}.
}
$$

---

## CDCC

$$
\boxed{
ESR\uparrow
\land
CCR\uparrow
}
$$

的 trajectory 可以存在。

---

## RRC

$$
\boxed{
d_{\mathrm{rel}}^{post}
\neq
d_{\mathrm{rel}}^{pre}
}
$$

因 alignment / re-representation / schema change 而發生。

---

# 87. 結論

本文將「跨領域」從一個單一類別事件：

$$
D_i\rightarrow D_j
$$

重寫為兩個彼此可分離的問題：

第一：

$$
\boxed{
\text{external taxonomy changed?}
}
$$

第二：

$$
\boxed{
\text{effective relational state changed discontinuously?}
}
$$

兩者不必相同。

因此：

$$
\boxed{
\text{external categorical discontinuity}
\not\Rightarrow
\text{internal cognitive discontinuity}.
}
$$

本文提出：

$$
\boxed{
\Delta_{\mathrm{cross}}
=
d_{\mathrm{ext}}
-
d_{\mathrm{rel}}
}
$$

來描述外部分類與內部關係距離的落差。

當：

$$
\Delta_{\mathrm{cross}}\gg0,
$$

外界可能看到：

> 大幅跨領域。

但 cognition 可能只是：

$$
\boxed{
\text{traversing a short relational path}.
}
$$

現有 analogical reasoning、cross-domain generalization、re-representation、schema drift、semantic control 與 task-space cognitive-map literature 都說明：

- surface category 並非唯一有效結構；
- relational mapping 可以跨 representation format；
- relational representations 可以支援 transfer；
- relation representations 本身可能改變；
- task goal 可以重配置有效認知／腦狀態。

但這些仍不足以證明：

$$
\boxed{
\text{relation-first topology
is the general architecture of human cognition}.
}
$$

所以本篇接受明確反證：

如果：

- external taxonomy；
- semantic embedding；
- familiarity；
- ordinary analogy；

已能完整預測 switching、transfer 與 return，

則 RFCC 不需要。

如果：

$$
ESR\uparrow
$$

必然伴隨：

$$
CCR\downarrow,
$$

則 CDCC 失敗。

如果 relational representations 在 cross-domain use 後沒有功能性塑形，

RRC 強版本失敗。

因此 TADC-06 的最終命題不是：

> 「領域不存在。」

而是：

$$
\boxed{
\text{No single fixed domain partition
should be assumed to define cognitive adjacency
before relational structure is measured.}
}
$$

中文：

> **在測量關係結構之前，不應先假定任何單一固定領域分割必然等於認知鄰接結構。**

若這個命題成立，

「跨領域能力」就不再只是：

$$
\boxed{
\text{ability to jump far}.
}
$$

它可能同時包括：

$$
\boxed{
\text{ability to discover that two apparently distant regions
were structurally adjacent all along}.
}
$$

而這正是 TADC-07 的入口：

> 如果 AI、外部記憶與多智能體系統可以主動保存 context、發現 bridge、建立 relation graph，那它們是否不只是「幫人算得更快」，而是在直接改變有效認知距離與可達拓樸？

---

# 參考文獻

1. Wang X, Krieger-Redwood K, Cui Y, Smallwood J, Du Y, Jefferies E, et al. **Macroscale brain states support the control of semantic cognition.** *Communications Biology*. 2024;7:926. doi:10.1038/s42003-024-06630-7.  
2. Tan L, Qiu Y, Qiu L, et al. **The medial and lateral orbitofrontal cortex jointly represent the cognitive map of task space.** *Communications Biology*. 2025;8:163. doi:10.1038/s42003-025-07588-w. PMID: 39900714.  
3. Qiu Y, Li H, Liao J, et al. **Forming cognitive maps for abstract spaces: the roles of the human hippocampus and orbitofrontal cortex.** *Communications Biology*. 2024;7:517. doi:10.1038/s42003-024-06214-5. PMID: 38693344.  
4. Weinberger AB, Gallagher NM, Warren T, Green AE. **Analogical mapping across sensory modalities and evidence for a general analogy factor.** *Cognition*. 2022;223:105029. doi:10.1016/j.cognition.2022.105029. PMID: 35091260.  
5. Kroczek B, Ciechanowska I, Chuderski A. **Uncovering the course of analogical mapping using eye tracking.** *Cognition*. 2022;225:105140. doi:10.1016/j.cognition.2022.105140. PMID: 35483161.  
6. Doumas LAA, Puebla G, Martin AE, Hummel JE. **A theory of relation learning and cross-domain generalization.** *Psychological Review*. 2022;129(5):999–1041. doi:10.1037/rev0000346. PMID: 35113620.  
7. **Evidence of analogical re-representation from a change detection task.** *Cognition*. 2019. doi:10.1016/j.cognition.2019.04.031. PMID: 31075695.  
8. Vagnino R, Walker C. **Schema drift: Relational concepts and conceptual change.** *Cognition*. 2026;271:106418. doi:10.1016/j.cognition.2025.106418. PMID: 41494364.  
9. Garvert MM, Dolan RJ, Behrens TEJ. **A map of abstract relational knowledge in the human hippocampal-entorhinal cortex.** *eLife*. 2017;6:e17086. doi:10.7554/eLife.17086.  
10. Park SA, Miller DS, Nili H, Ranganath C, Boorman ED. **Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps.** *Neuron*. 2020;107(6):1226–1238.e8. doi:10.1016/j.neuron.2020.06.030.  
11. Behrens TEJ, Muller TH, Whittington JCR, et al. **What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior.** *Neuron*. 2018;100(2):490–509. doi:10.1016/j.neuron.2018.10.002.  
12. Holyoak KJ, Thagard P. **The analogical mind.** *American Psychologist*. 1997;52(1):35–44. PMID: 9017931.  
13. **Semantic Structural Alignment of Neural Representational Spaces Enables Translation between English and Chinese Words.** *Journal of Cognitive Neuroscience*. 2016. doi:10.1162/jocn_a_01000. PMID: 27315264.  
14. Qiu Y, et al. **Dynamic changes in orbitofrontal-hippocampal connectivity linked to cognitive map formation in humans.** *NeuroImage*. 2025;318:121415. PMID: 40780573.  

---

## 與系列的關係

**已完成：**

- TADC-01：《注意力不是單點選擇——可變認知空間與注意—空間轉換猜想》
- TADC-02：《動態認知域——領域作為局部座標圖》
- TADC-03：《拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引》
- TADC-04：《嵌套注意域與觀察尺度——宏觀／微觀的相對性與多尺度重索引》
- TADC-05：《從單點超專注到拓樸超專注——域級持續性、內部高熵遍歷與可控退出》
- TADC-06：《關係優先認知與跨域連續性——從學科距離到關係距離的認知拓樸猜想》

**下一篇：**

- TADC-07：《外部認知支架與人—AI 認知拓樸》

後續：

- TADC-08：《拓樸注意力的測量、反證與工程化》

---

**狀態：** TADC-06 v0.1  
**原始人體／臨床數據：** 無  
**理論狀態：** 猜想／研究綱領；未經一般性實驗驗證  
**跨域狀態：** RFCC / CDCC / RRC 均為待驗證命題  
**拓樸狀態：** relational topology 為 goal-conditioned multiplex accessibility 的候選形式，不宣稱已建立嚴格數學拓樸
