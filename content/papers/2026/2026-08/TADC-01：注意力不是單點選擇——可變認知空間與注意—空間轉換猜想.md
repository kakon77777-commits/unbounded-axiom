# TADC-01：注意力不是單點選擇——可變認知空間與注意—空間轉換猜想

**英文題名：** Attention Is Not Merely Point Selection: The Variable Cognitive Space and Attention–Space Transformation Conjectures  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-01  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論命題／形式化研究綱領／可證偽模型  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

注意力最直觀的描述，是在大量可處理資訊中選擇某些對象、位置、特徵或任務表示，並提高其認知優先權。這種描述非常有用，但它通常隱含一個最低階假設：

$$
\boxed{
\text{可供注意的認知空間已經存在。}
}
$$

亦即，存在一個候選集合：

$$
X=\{x_1,x_2,\ldots,x_n\},
$$

注意力所做的是：

$$
A_t:X\rightarrow \mathbf w_t,
$$

也就是改變既有元素的權重、激活或優先順序。

本文提出另一種可能：

$$
\boxed{
X_t
\text{ 本身也可能隨認知活動而改變。}
}
$$

因此，注意活動的作用未必只是在固定認知空間中重新分配資源；在部分高階認知條件下，它可能參與改變未來哪些認知對象、關係、鄰域與推理路徑成為可達。

本文提出兩個根猜想：

$$
\boxed{
\textbf{Variable Cognitive Space Conjecture — VCSC}
}
$$

即有效認知空間隨時間、目標、學習、記憶與控制而變動；以及更強的：

$$
\boxed{
\textbf{Attention–Space Transformation Conjecture — ASTC}
}
$$

即注意配置本身可能對這種認知空間變化具有可辨認的因果貢獻。

本文不直接假設這些結構已構成嚴格的數學 topology。為避免將「拓樸」僅作為漂亮隱喻，本文首先採用**動態關係結構、可達性核與鄰域系統**作為最小形式，並建立固定空間選擇模型作為虛無模型。

ASTC 進一步分成弱、中、強三個版本：注意改變表徵幾何；注意造成持續的可達性改變；以及注意參與產生不能由固定潛在表示加上單純 gain modulation 完整解釋的新結構。

因此，本文並不是宣告「注意力就是拓樸」，而是提出一個可以被傳統 attention、learning、working memory、semantic priming、task-set reconfiguration 與 cognitive-map 模型擊敗的命題。

---

# 0. 邊界聲明

本文不是臨床研究、醫療建議或神經疾病模型，不以 ADHD、hyperfocus 或任何個人案例作為理論成立的證據。

本文提出的是：

$$
\boxed{
\text{general cognitive architecture conjecture}
}
$$

而不是：

$$
\boxed{
\text{ADHD-specific theory}.
}
$$

ADHD、專家研究者、程式設計者、遊戲玩家、AI-assisted workers 與一般健康成人，未來都可以成為不同測試族群。

此外，本文不主張：

$$
\text{attention}
=
\text{topology}.
$$

本文的真正命題是較弱而可驗證的：

$$
\boxed{
\text{attention may participate in transforming
the effective structure of cognitive accessibility}.
}
$$

只有在後續能證明該結構具有可操作的 neighborhood、connectivity、nesting、continuity 與 invariants 時，才有資格將「topological」由方法論名稱提升為嚴格數學描述。

---

# 1. 問題：注意力是在空間中移動，還是在改變空間？

先考慮最低階模型。

存在固定認知集合：

$$
X=\{x_1,x_2,\ldots,x_n\}.
$$

注意力只改變：

$$
\mathbf w_t
=
(w_{1,t},w_{2,t},\ldots,w_{n,t}).
$$

例如：

$$
w_{3,t}\uparrow
$$

表示：

$$
x_3
$$

成為目前最重要的處理對象。

這種模型可以描述很多注意現象，本文不否定它。

但考慮高階推理。

一開始：

$$
X_t=\{a,b,c\}.
$$

主體注意到：

$$
a\mathrel{R_1}b.
$$

接著由：

$$
b
$$

推導出：

$$
b\mathrel{R_2}d.
$$

原來：

$$
d\notin X_t.
$$

現在：

$$
d\in X_{t+1}.
$$

甚至原來不存在有效連結：

$$
(a,d)\notin\mathcal R_t,
$$

經過推理之後：

$$
(a,d)\in\mathcal R_{t+1}.
$$

此時變化不只是：

$$
w_a>w_b.
$$

而是：

$$
\boxed{
X_t\neq X_{t+1}
}
$$

甚至：

$$
\boxed{
\mathcal R_t\neq\mathcal R_{t+1}.
}
$$

所以真正的問題變成：

$$
\boxed{
\text{Attention selects states}
}
$$

與：

$$
\boxed{
\text{Attention participates in transforming
the state space}
}
$$

是不是兩種不同的認知作用？

---

# 2. 現有文獻其實已經靠得很近

這個命題並不是因為用了「拓樸」兩個字就自然成立，但現有認知神經科學確實已經提供數個很接近的拼圖。

首先，抽象知識並不只以孤立項目的形式存在。Garvert、Dolan 與 Behrens 的研究顯示，人類 hippocampal–entorhinal system 可以表示非空間、離散的 relational graph，而且 neural representation 會反映關係結構中的距離；後續研究也顯示分開學習的抽象結構可以被組合成支援新推論的 cognitive map。

2024 年研究又顯示，人類可以學習 multidimensional abstract spaces，hippocampus、entorhinal cortex 與 orbitofrontal cortex 在 exploration、learning 與 exploitation 階段呈現不同角色。這支持「抽象問題本身可以形成可導航的 relational space」這個方向。

更重要的是，2025 年 Peer 與 Epstein 直接研究 nested spaces，發現人類會把環境組織成 subspaces，跨 subspace integration 具有額外行為成本，而且相關腦區表徵反映這種階層結構。

2026 年 Leach、Chen 與 Hwang 則進一步把較抽象的 context reconfiguration 與較具體的 subordinate task-set reconfiguration 分開，發現不同階層具有不同的 behavioral switch cost 與 neural pattern reconfiguration。換言之，高階目標與低階規則並不是同一尺度上的同一種「切換」。

甚至注意本身也已被觀察到能改變表徵幾何。2023 年的 feature-based attention 研究顯示，選擇性注意特定顏色會使 color feature space 發生系統性的 expansion / compression，改變後續知覺相似性。

但這些結果都還沒有證明本文的強命題。

因為：

$$
\boxed{
\text{representational warping}
\neq
\text{new cognitive topology}.
}
$$

attention-induced warping 完全可能由既有 neural populations 上的 gain modulation 產生。

所以它最多直接支持我們後面定義的 **ASTC-W**。

---

# 3. 先建立敵人：固定空間選擇模型

如果 TADC 不能被簡單模型擊敗，就沒有研究價值。

因此定義：

## Fixed-Space Selection Model，FSSM

在一個分析 episode 中：

$$
X_t=X,
$$

$$
\mathcal R_t=\mathcal R,
$$

$$
\mathcal N_t=\mathcal N.
$$

只有：

$$
\mathbf w_t
$$

發生改變。

所以：

$$
\mathcal C_t
=
(X,\mathcal R,\mathcal N,\mathbf w_t,G_t).
$$

注意力：

$$
A_t:
\mathbf w_t
\mapsto
\mathbf w_{t+1}.
$$

即使：

- 某概念突然非常顯著；
- 某條 association 更容易被想到；
- 某種特徵被放大；
- 某個 decision boundary 改變；
- 某個 task set 暫時支配行為；

只要：

$$
X,\mathcal R,\mathcal N
$$

沒有真正改變，就不需要 TADC。

所以：

$$
\boxed{
\text{Activation}
\neq
\text{Structural Transformation}.
}
$$

這條要一直保留。

---

# 4. 可變認知空間猜想

現在定義：

$$
\boxed{
\mathcal C_t
=
(
X_t,
\mathcal R_t,
\kappa_t,
\mathcal N_t,
A_t,
G_t
)
}
$$

其中：

$$
X_t
$$

是目前有效的 cognitive objects；

$$
\mathcal R_t
$$

是關係集合；

$$
\kappa_t(x,y\mid G_t)
$$

表示在目前 goal 下：

$$
x\rightarrow y
$$

的有效可達強度；

$$
\mathcal N_t
$$

是 cognitive neighborhood system；

$$
A_t\subseteq X_t
$$

是當下 active set；

而：

$$
G_t
$$

是高階目標與 context。

關係可以具有不同類型：

$$
\mathcal R_t
=
\{
R_S,
R_C,
R_A,
R_P,
R_T,
R_G
\},
$$

分別表示：

- semantic；
- causal；
- analogical；
- procedural；
- temporal；
- goal-relative relationships。

VCSC 最低命題：

$$
\boxed{
\exists t_1,t_2:
\mathcal C_{t_1}\not\equiv\mathcal C_{t_2}.
}
$$

即有效認知空間不是永久固定。

這一條其實不強。

learning、memory、consolidation、task context 都可能讓它成立。

真正有風險的是下一條。

---

# 5. 注意—空間轉換猜想

令：

$$
a_t
$$

為 attention configuration，

$$
e_t
$$

為 external input，

$$
m_t
$$

為 memory state。

定義：

$$
\boxed{
\mathcal C_{t+1}
=
\Phi
(
\mathcal C_t,
a_t,
e_t,
m_t
).
}
$$

ASTC 宣稱：

$$
\boxed{
\frac{\partial\mathcal C_{t+1}}
{\partial a_t}
\neq0
}
$$

至少在部分認知條件成立。

這個偏導只表示**因果依賴概念**，目前並不宣稱 \(\mathcal C\) 一定具有普通微分結構。

換句話說：

如果：

$$
a_t^{(1)}
\neq
a_t^{(2)},
$$

而我們盡量固定：

$$
e_t,
m_t,
\text{exposure},
\text{reward},
\text{time},
$$

之後仍然得到：

$$
\mathcal C_{t+1}^{(1)}
\neq
\mathcal C_{t+1}^{(2)},
$$

那就開始有注意參與 space transformation 的證據。

---

# 6. 為什麼現在不能直接寫 \((X,\tau)\)？

這是一個重要的數學自我限制。

如果現在直接說：

$$
(X,\tau)
$$

是 topological space，

就得回答：

$$
\varnothing\in\tau?
$$

$$
X\in\tau?
$$

任意 union 是否仍然 open？

有限 intersection 是否仍 open？

更重要的是：

> cognitive open set 到底是什麼？

目前沒有充分理由。

所以第一篇只定義：

## Goal-conditioned cognitive neighborhood

$$
N_t(x;\theta,G_t)
=
\left\{
y:
\kappa_t(x,y\mid G_t)\geq\theta
\right\}.
$$

然後：

$$
\mathcal N_t
=
\{
N_t(x;\theta,G_t)
\}.
$$

也就是先得到：

$$
\boxed{
\text{dynamic neighborhood system}.
}
$$

未來如果它符合 topology、pretopology、Alexandrov topology 或其他結構，再正式升級。

所以現在：

$$
\boxed{
\text{Topological}
=
\text{research direction},
}
$$

而不是：

$$
\boxed{
\text{proved mathematical classification}.
}
$$

---

# 7. 注意力真正可能改變的是「可達性」

這可能是第一篇最重要的形式化。

假設目前 active set：

$$
A_t\subseteq X_t.
$$

定義：

$$
\operatorname{Reach}_t^{(k)}(A_t)
$$

為從：

$$
A_t
$$

經最多 \(k\) 個有效 relational transitions 可以到達的 cognitive objects。

粗略寫：

$$
\operatorname{Reach}_t^{(k)}(A_t)
=
\left\{
y:
A_t
\leadsto_k
y
\right\}.
$$

那注意的結果可能不只是：

$$
w(x)\uparrow,
$$

而是：

$$
\boxed{
\operatorname{Reach}_{t+1}^{(k)}
\neq
\operatorname{Reach}_{t}^{(k)}.
}
$$

例如本來從：

$$
A
$$

只能想到：

$$
B,C,D.
$$

經過 relational attention 後，同一起點自然可以到：

$$
B,C,D,E,F,G.
$$

這個變化就比：

> 「E 的 activation 比較高」

更強。

它變成：

$$
\boxed{
\text{future cognitive possibility space changed}.
}
$$

---

# 8. ASTC 必須拆成三個強度

## ASTC-W：Weak Geometry Version

只要求：

$$
\kappa_t
\neq
\kappa_{t+1}.
$$

即 relational weights 或 representational geometry 改變。

但是：

$$
X_t=X_{t+1},
$$

而且原來的 edges 全部還在。

這可能只是：

$$
\text{gain modulation}.
$$

---

## ASTC-M：Persistent Accessibility Version

要求注意 cue 消失後：

$$
a_{t+\Delta}
=
a_{\mathrm{baseline}},
$$

但：

$$
\mathcal N_{t+\Delta}
\neq
\mathcal N_t.
$$

或者：

$$
\operatorname{Reach}_{t+\Delta}^{(k)}
\neq
\operatorname{Reach}_t^{(k)}.
$$

也就是：

$$
\boxed{
\text{attention}
\rightarrow
\text{persistent accessibility change}.
}
$$

---

## ASTC-S：Strong Structural Construction Version

最強版要求真正出現：

$$
\mathcal R_t
\rightarrow
\mathcal R_{t+1},
$$

或：

$$
X_t
\rightarrow
X_{t+1}.
$$

例如原來：

$$
(x,y)
\notin
\mathcal R_t^{\mathrm{effective}},
$$

之後：

$$
(x,y)
\in
\mathcal R_{t+1}^{\mathrm{effective}}.
$$

甚至原來不存在 cognitive unit：

$$
z.
$$

經過 chunking / abstraction：

$$
z=f(x_1,x_2,\ldots,x_n),
$$

使：

$$
z\in X_{t+1}.
$$

但這裡最大問題是：

這完全可能只是：

$$
\text{learning},
$$

$$
\text{memory consolidation},
$$

$$
\text{chunking},
$$

或：

$$
\text{schema formation}.
$$

所以 ASTC-S 必須證明：

$$
\boxed{
\text{attention contributes independently
to this structural construction}.
}
$$

否則它不成立。

---

# 9. 移動和改造不是同一件事

我們至少要拆：

## Traversal

$$
x_t\rightarrow x_{t+1},
$$

但：

$$
\mathcal C_t=\mathcal C_{t+1}.
$$

## Reweighting

$$
\kappa_t\rightarrow\kappa_{t+1}.
$$

## Expansion

$$
X_t\subset X_{t+1}.
$$

## Contraction

$$
X_{t+1}\subset X_t.
$$

## Rewiring

$$
\mathcal R_t\neq\mathcal R_{t+1}.
$$

## Chunk Formation

$$
\{x_1,x_2,x_3\}
\rightarrow
z.
$$

使原本三個 low-level objects 可以在較高解析度下變成：

$$
\boxed{
\text{one object}.
}
$$

這會自然連到後續的 macro/micro relativity。

---

# 10. 「領域」也不必是基本物件

假設學科分類：

$$
D=
\{
D_{\mathrm{math}},
D_{\mathrm{AI}},
D_{\mathrm{psych}},
D_{\mathrm{biology}}
\}.
$$

這是 external classification。

但如果：

$$
x\in D_{\mathrm{math}},
$$

$$
y\in D_{\mathrm{psych}},
$$

然而在目前目標下：

$$
\kappa_t(x,y\mid G)\gg0,
$$

則兩者在 cognitive space 中可能非常近。

所以：

$$
\boxed{
d_{\mathrm{discipline}}(x,y)
\neq
d_{\mathrm{cognitive}}(x,y).
}
$$

甚至：

$$
d_{\mathrm{discipline}}\gg0
$$

但：

$$
d_{\mathrm{cognitive}}\approx1.
$$

外部觀察者看到的是跨領域跳躍，主體內部卻可能只是沿著關係鄰域遍歷。

這一部分留給 TADC-02 與 TADC-06 展開。

---

# 11. 最危險的競爭解釋：其實全部只是 learning

假設：

$$
a_t
\rightarrow
\text{encoding}
\rightarrow
\mathcal C_{t+1}.
$$

這時 attention 可能只是 gate。

甚至：

$$
\text{exposure}
\rightarrow
\text{learning}
\rightarrow
\mathcal C_{t+1}
$$

已經足夠。

所以真正需要比較：

$$
M_0:
\text{exposure}
\rightarrow
\Delta\mathcal C,
$$

與：

$$
M_1:
\text{attention}
+
\text{matched exposure}
\rightarrow
\Delta\mathcal C.
$$

ASTC 至少需要：

$$
\boxed{
\Delta\mathcal C_{M_1}
>
\Delta\mathcal C_{M_0}
}
$$

在 exposure、time、reward 等條件被控制後出現。

否則：

$$
\text{learning theory}
$$

就夠了。

---

# 12. Working Memory 也可能把我們整篇殺掉

另一個可能：

$$
\text{attention}
\rightarrow
\text{WM activation}.
$$

只要相關 items 還留在 working memory：

$$
P(y\mid x)\uparrow.
$$

看起來就像 cognitive accessibility 改變。

所以我們需要：

$$
\boxed{
\text{post-cue persistence}.
}
$$

如果 attention cue 拿掉後：

$$
\Delta\mathcal C
\rightarrow0,
$$

那 ASTC-M 就不成立。

---

# 13. Semantic Priming 也不能被偷換成拓樸

如果注意：

$$
x
$$

之後：

$$
RT(y\mid x)\downarrow,
$$

完全可能只是 priming。

所以：

$$
\boxed{
\text{one faster association}
\neq
\text{topological transformation}.
}
$$

強證據至少要看：

- multi-step reachability；
- novel inference；
- generalization；
- neighborhood change；
- persistent restructuring；
- competing-model performance。

---

# 14. 第一個真正的實驗

## Matched-Exposure Relational Attention Experiment

所有 participant 都看到完全相同的：

$$
X
$$

以及完全相同 stimulus sequence。

差別只在：

### Group A

注意：

$$
\text{individual feature}.
$$

### Group B

注意：

$$
\text{pairwise relation}.
$$

### Group C

注意：

$$
\text{global relational structure}.
$$

所以：

$$
E_A=E_B=E_C.
$$

訓練後測：

$$
\text{pairwise similarity},
$$

$$
\text{multi-step inference},
$$

$$
\text{novel route discovery},
$$

$$
\text{generalization},
$$

$$
\text{free transition trajectory}.
$$

如果：

$$
\operatorname{Reach}_C^{(k)}
>
\operatorname{Reach}_A^{(k)}
$$

而且不能只用記憶強度解釋，

那 ASTC 開始有東西。

---

# 15. 第二個實驗：表徵幾何

建立：

$$
D_{\mathrm{pre}}
$$

與：

$$
D_{\mathrm{post}},
$$

分別表示 manipulation 前後的 representational distance matrix。

測：

$$
\Delta D
=
D_{\mathrm{post}}
-
D_{\mathrm{pre}}.
$$

如果只有局部 gain：

固定空間模型可能足以解釋。

但是如果出現：

- new cluster；
- new bridge；
- new effective dimension；
- new inference route；

動態空間模型的必要性就提高。

---

# 16. 第三個實驗：把 cue 拿掉

在：

$$
10\text{ min},
$$

$$
1\text{ day},
$$

$$
1\text{ week}
$$

後重新測：

$$
\mathcal C.
$$

如果：

$$
\Delta\mathcal C(10\text{ min})>0
$$

但：

$$
\Delta\mathcal C(1\text{ day})=0,
$$

可能只是短期 state effect。

如果持續：

$$
\Delta\mathcal C(1\text{ week})>0,
$$

則需要考慮：

$$
\text{attention-mediated learning/consolidation}.
$$

---

# 17. 第四個實驗：重新索引

假設：

$$
U_1\subset U_2\subset U_3.
$$

有時讓 participant 把：

$$
U_1
$$

當成整個 task。

另一條件則把：

$$
U_1
$$

視為：

$$
U_2
$$

裡的一個 subordinate unit。

如果只是固定 hierarchy：

固定 tree model 應該足以預測。

如果同一 object set 的：

$$
\mathcal N
$$

因觀察尺度而被系統性重新組織：

$$
\mathcal N^{(1)}
\neq
\mathcal N^{(2)},
$$

那就開始接近後續的：

$$
\boxed{
\text{Re-indexing}.
}
$$

---

# 18. 五個核心預測

## ASTC-H1 — Attention-Dependent Reachability

$$
a_1\neq a_2
$$

在 matched exposure 下造成：

$$
\operatorname{Reach}^{(k)}_1
\neq
\operatorname{Reach}^{(k)}_2.
$$

## ASTC-H2 — Persistence

attention cue 拿掉後：

$$
\Delta\mathcal N>0.
$$

否則中版不成立。

## ASTC-H3 — Novel Generalization

attention-induced change 必須影響：

$$
\boxed{
\text{untrained inference}.
}
$$

只改善熟悉 item 不夠。

## ASTC-H4 — Fixed-Space Model Failure

固定 latent representation 加 dynamic weights：

$$
M_F
$$

至少在部分任務必須輸給：

$$
M_D.
$$

即：

$$
\boxed{
\operatorname{PredictiveAccuracy}(M_D)
>
\operatorname{PredictiveAccuracy}(M_F).
}
$$

如果永遠沒有，ASTC-S 就是多餘的。

## ASTC-H5 — Goal-Dependent Neighborhood

同樣的 object set：

$$
X
$$

在：

$$
G_1
$$

與：

$$
G_2
$$

下形成：

$$
\mathcal N(X\mid G_1)
\neq
\mathcal N(X\mid G_2).
$$

---

# 19. 什麼會真正殺掉這套理論？

如果結果顯示：

$$
\boxed{
\text{fixed representation + gain modulation}
}
$$

就能完整解釋所有現象，

則：

$$
ASTC\text{-S}
$$

應直接放棄。

如果：

$$
\Delta\mathcal C=0
$$

只要 attention cue 消失，

則：

$$
ASTC\text{-M}
$$

應放棄。

如果 relational-space language 沒有比：

$$
\text{semantic similarity}
$$

與：

$$
\text{association strength}
$$

提供任何額外預測，

則：

$$
\text{space}
$$

只是重新命名。

如果我們始終找不到：

- neighborhood；
- connectivity；
- gluing；
- invariants；
- meaningful coarse-graining；

那「topological」也應該刪掉。

系列可以降級成：

$$
\boxed{
\text{Dynamic Relational Attention Theory}.
}
$$

這是可以接受的結果。

---

# 20. 為什麼仍然值得走「拓樸」方向？

因為它讓問題從：

> 哪個點的 activation 最大？

變成：

> 哪些東西彼此可達？

以及：

> 哪些區域形成 connected component？

> 哪條 bridge 被建立？

> 哪些 domain 被拆開？

> 哪些 domain 被黏合？

> 改變解析度之後，哪些結構仍然存在？

也就是從：

$$
\boxed{
\text{point value}
}
$$

走向：

$$
\boxed{
\text{relational organization}.
}
$$

如果未來這些量能穩定預測 cognition，那 topology 就不是修辭。

它會開始有真正的 explanatory content。

---

# 21. TADC 與 Cognitive Map 並不是競爭理論

cognitive-map literature 比較接近問：

$$
\boxed{
\text{How is relational structure represented?}
}
$$

而 TADC 問：

$$
\boxed{
\text{How can effective relational structure
change during cognition?}
}
$$

所以：

$$
\text{Cognitive Map}
$$

可以成為：

$$
\text{TADC}
$$

的一種 implementation substrate。

並不衝突。

---

# 22. 最小總模型

最後把全部壓成一行：

$$
\boxed{
\mathcal C_t
=
(X_t,\mathcal R_t,\kappa_t,\mathcal N_t,A_t,G_t)
}
$$

而：

$$
\boxed{
\mathcal C_{t+1}
=
\Phi(
\mathcal C_t,
a_t,
e_t,
m_t
).
}
$$

固定空間模型：

$$
\Phi_F:
(X,\mathcal R,\mathcal N,\mathbf w_t)
\rightarrow
(X,\mathcal R,\mathcal N,\mathbf w_{t+1}).
$$

動態空間模型：

$$
\Phi_D:
(X_t,\mathcal R_t,\mathcal N_t)
\rightarrow
(X_{t+1},\mathcal R_{t+1},\mathcal N_{t+1}).
$$

所以整篇真正只問：

$$
\boxed{
\operatorname{PredictiveGain}
(\Phi_D,\Phi_F)
>0?
}
$$

如果答案是：

$$
0,
$$

我們不需要這套理論。

如果穩定：

$$
>0,
$$

那才開始有資格往真正 topology 前進。

---

# 23. 結論

本文提出：

$$
\boxed{
\textbf{VCSC}
}
$$

即：

> 有效認知空間不是必然固定的。

以及：

$$
\boxed{
\textbf{ASTC}
}
$$

即：

> 注意活動可能不只在認知空間中移動與分配權重，也可能參與改變之後哪些認知對象、關係與路徑成為可達。

但本文刻意不宣稱：

$$
\text{Attention}=\text{Topology}.
$$

目前最嚴格的寫法仍然是：

$$
\boxed{
\text{Attention may transform
effective cognitive accessibility structure.}
}
$$

等到後面真的能定義：

$$
\text{neighborhood},
$$

$$
\text{connectivity},
$$

$$
\text{nesting},
$$

$$
\text{gluing},
$$

$$
\text{invariants},
$$

再決定「拓樸注意力」究竟是數學理論，還是一個最後應被降級的研究比喻。

這也是 TADC-01 最重要的自我限制：

$$
\boxed{
\text{Do not call a change topological
until topology adds testable structure.}
}
$$

但若 ASTC 成立，注意力問題就會從：

$$
\boxed{
\text{What is being selected?}
}
$$

向上多出一個問題：

$$
\boxed{
\text{What becomes reachable because of that selection?}
}
$$

而這兩個問題，不再是同一個問題。

---

# 參考文獻

1. Garvert MM, Dolan RJ, Behrens TEJ. *A map of abstract relational knowledge in the human hippocampal-entorhinal cortex.* eLife. 2017;6:e17086.  
2. Park SA, Miller DS, Nili H, Ranganath C, Boorman ED. *Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps.* Neuron. 2020;107:1226–1238.e8.  
3. Qiu Y, et al. *Forming cognitive maps for abstract spaces: the roles of the human hippocampus and orbitofrontal cortex.* Communications Biology. 2024;7:517.  
4. Wang X, et al. *Macroscale brain states support the control of semantic cognition.* Communications Biology. 2024;7:926.  
5. Peer M, Epstein RA. *Cognitive maps for hierarchical spaces in the human brain.* Cerebral Cortex. 2025;35(9):bhaf261.  
6. Leach SC, Chen X, Hwang K. *Hierarchical Reconfiguration of Neurocognitive Task Set Representations Mediates Cognitive Flexibility.* Journal of Neuroscience. 2026.  
7. Baram AB, et al. *An abstract relational map emerges in the human medial prefrontal cortex with consolidation.* Current Biology. 2026;36:3315–3325.e4.  
8. *Feature-based attention warps the perception of visual features.* Scientific Reports. 2023.  
9. Behrens TEJ, Muller TH, Whittington JCR, Mark S, Baram AB, Stachenfeld KL, Kurth-Nelson Z. *What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior.* Neuron. 2018;100(2):490–509.  
10. Theves S, Fernández G, Doeller CF. *The hippocampal-entorhinal system represents nested hierarchical relations between words during concept learning.* Hippocampus. 2021.  

---

## 系列後續

**TADC-02：**《動態認知域：領域作為局部座標圖》  
**TADC-03：**《拓樸注意力六算子：展開、收斂、遍歷、黏合、切離與重索引》  
**TADC-04：**《嵌套注意域與觀察尺度》  
**TADC-05：**《從單點超專注到拓樸超專注》  
**TADC-06：**《關係優先認知與跨域連續性》  
**TADC-07：**《外部認知支架與人—AI 認知拓樸》  
**TADC-08：**《拓樸注意力的測量、反證與工程化》

---

**狀態：** TADC-01 v0.1  
**原始人體／臨床數據：** 無  
**理論狀態：** 猜想／研究綱領；未經實驗驗證
