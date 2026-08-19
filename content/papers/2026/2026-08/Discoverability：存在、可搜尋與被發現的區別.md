# Series II / Paper 02
# Discoverability：存在、可搜尋與被發現的區別
## Discoverability: Distinguishing Existence, Retrievability, Exposure, and Name-Free Discovery

**作者：Neo.K（許筌崴）**  
**機構：EveMissLab**  
**系列：品質—發現—傳播—成功解耦理論（Series II）**  
**版本：v0.1**  
**日期：2026-08-14**

## 摘要

一個作品「存在於網路上」、可以被搜尋引擎索引、輸入完整名稱即可找到，以及一個尚不知道作品名稱但需求高度匹配的使用者有機會自然遇見它，是四個不同的資訊存取狀態。現代數位市場經常把這些狀態混合成模糊的「曝光」或「SEO」，導致一個重要錯誤：將精確名稱搜尋成功誤認為高可發現度。

本文在 AMNESS 的品質—市場狀態空間上，提出「分層可發現性模型」（Layered Discoverability Model, LDM），將作品的資訊路徑分成：

$$
\text{Existence}
\rightarrow
\text{Indexability}
\rightarrow
\text{Retrievability}
\rightarrow
\text{Interface Exposure}
\rightarrow
\text{Name-Free Discoverability}
\rightarrow
\text{Matched Discovery}.
$$

本文定義名稱查詢分布 $\mathcal Q_{\mathrm{name}}$ 與需求查詢分布 $\mathcal Q_{\mathrm{need}}$，並以 query-support overlap 描述作品能否被尚不知道其名稱的目標使用者搜索到。本文證明一組基本非蘊含：公開存在不推出被索引；被索引不推出 top- $k$ 可檢索；高精確名稱可檢索性不推出高無名探索可發現度。特別地，可以構造：

$$
R_{\mathrm{name}}=1
$$

但：

$$
D_0=0.
$$

這代表「知道名稱的人非常容易找到」與「不知道名稱的人幾乎不可能遇見」完全可以同時成立。

本文再證明 Discovery Activation Bound：若採用一個作品必須先發現該作品，則對任一目標使用者：

$$
P(\mathrm{Adopt})
\le
P(\mathrm{Discover})
=
D.
$$

因此可發現度是品質轉化為市場結果的必要激活通道，但不是充分條件。對多通道發現，本文利用 union bounds 區分名義通道數與有效通道覆蓋，並提出 Match-Weighted Discoverability、Discovery Routing Gap、Algorithmic Invisibility 與 Discovery Support Ratio。

既有 Information Retrieval 研究早已提出 retrievability，以衡量檢索系統讓個別文件「多容易被查到」；後續研究顯示較罕見實體會受到 popularity bias，神經排序器可出現品牌名稱偏差。推薦系統中，item cold-start 研究則直接把新內容的 discoverability 與探索流量配置視為獨立問題。本文的新增點不是重新命名 retrievability，而是把 retrievability 嵌入從作品存在到市場發現的完整因果前置鏈，並將「name-free discovery」明確定義為與 exact-query searchability 不同的 AMNESS 狀態變數。

**關鍵詞：** Discoverability、Retrievability、Searchability、Cold Start、Exposure Bias、Recommendation、Information Retrieval、Audience Discovery、作品成功、AMNESS

## 1. 問題：東西「就在那裡」為什麼還是沒人看到？

Series II / Paper 01 已建立：

$$
\mathbf y_A
=
(Q,V,D,M,C,W,P,S)
$$

並證明：

$$
Q_A>Q_B
\not\Rightarrow
S_A>S_B.
$$

本文現在展開其中的 $D$。

最常見的錯誤直覺是：

> 「我在搜尋引擎或商店打完整名稱就找得到，所以這個作品的 discoverability 應該不低。」

但如果使用者已經知道完整名稱，則 discovery 大部分其實已經發生。

真正問題是：

$$
\boxed{
\text{不知道名稱的人，是否仍有合理路徑遇見它？}
}
$$

## 2. 六層資訊路徑

本文提出：

$$
\boxed{
\text{Existence}
\rightarrow
\text{Indexability}
\rightarrow
\text{Retrievability}
\rightarrow
\text{Exposure}
\rightarrow
\text{Name-Free Discoverability}
\rightarrow
\text{Matched Discovery}.
}
$$

每一層都可以失敗，因此不存在無條件的：

$$
X_i\Rightarrow X_{i+1}.
$$

## 3. Public Existence

定義：

$$
X_A(t)\in\{0,1\}.
$$

若 artifact $A$ 在時間 $t$ 至少有一份公共可取得的正式 artifact，則：

$$
X_A(t)=1.
$$

例如商店頁、repository、論文頁、公開網頁或書籍頁已存在。

但：

$$
X_A=1
$$

只表示：

$$
\boxed{
\text{artifact exists publicly}.
}
$$

它沒有說任何搜尋或推薦系統已經把它納入可用候選集合。

## 4. Indexability

定義：

$$
J_A(p,t)
=
P
\left(
A
\text{ is represented in platform }p
\text{ index or candidate pool}
\right).
$$

如果內容被阻擋、缺乏入口、格式不可解析、平台尚未 ingestion，則完全可能：

$$
X_A=1
$$

但：

$$
J_A\approx0.
$$

因此：

$$
\boxed{
X_A=1
\not\Rightarrow
J_A>0.
}
$$

## 5. Retrievability

對查詢 $q$，令：

$$
r(A,q,p)
$$

為 artifact $A$ 在平台 $p$ 的排名。

對 cutoff $k$ 定義：

$$
\chi_k(A,q,p)
=
\mathbf 1
[
r(A,q,p)\le k
].
$$

對查詢分布：

$$
q\sim\mathcal Q,
$$

定義：

$$
R_k
(A\mid\mathcal Q,p)
=
E_{q\sim\mathcal Q}
[
\chi_k(A,q,p)
].
$$

因此 Retrievability 不是單一固定 artifact 屬性，而是：

$$
\boxed{
\text{artifact}
+
\text{retrieval system}
+
\text{query distribution}
+
\text{cutoff}.
}
$$

## 6. 與既有 Retrievability 的關係

Azzopardi 與 Vinay 已在 Information Retrieval 中提出 retrievability，用以衡量檢索系統讓個別文件在一組查詢下多容易被取回。

本文不重新發明這個概念。

本文的新增工作是把 Retrievability 放進：

$$
\text{artifact existence}
\rightarrow
\text{market discovery}
$$

之間的完整前置鏈，並進一步區分：

$$
\text{known-name retrievability}
$$

與：

$$
\text{name-free discoverability}.
$$

## 7. 排名加權 Retrievability

令：

$$
g'(r)<0.
$$

例如：

$$
g(r)
=
\frac{1}{\log_2(1+r)}.
$$

定義：

$$
\widetilde R
(A\mid\mathcal Q,p)
=
E_{q\sim\mathcal Q}
[
g(r(A,q,p))
].
$$

此量保留排名資訊，但仍只是：

$$
\boxed{
\text{query-conditioned retrievability}.
}
$$

## 8. 兩種查詢分布

定義：

$$
\mathcal Q_{\mathrm{name}}
$$

為已知 artifact 名稱、作者、品牌或唯一識別符的查詢分布。

另定義：

$$
\mathcal Q_{\mathrm{need}}
$$

為使用者只描述需求、興趣、問題或類型，但尚不知道 artifact 名稱的查詢分布。

例如：

> 「高品質單人太空策略遊戲」

與：

> 「某遊戲的完整名稱」

是完全不同的 retrieval problem。

## 9. Known-Name Retrievability

定義：

$$
R_{\mathrm{name}}
=
R_k
(A\mid\mathcal Q_{\mathrm{name}},p).
$$

若：

$$
R_{\mathrm{name}}\approx1,
$$

只代表：

> 已經知道 artifact 是什麼的人，很容易找回它。

這是一種 navigation / lookup 能力。

## 10. Need-Based Retrievability

定義：

$$
R_{\mathrm{need}}
=
R_k
(A\mid\mathcal Q_{\mathrm{need}},p).
$$

它回答：

> 只描述「我想要什麼」時，系統是否會把這個 artifact 放進候選集合？

完全可能：

$$
R_{\mathrm{name}}
\gg
R_{\mathrm{need}}.
$$

## 11. Name-Free Discoverability

對尚未認識 artifact 的使用者：

$$
\mathcal U_0(A)
=
\{
u:
u
\text{ does not know an identifying symbol of }A
\},
$$

定義：

$$
D_0(A)
=
P
\left(
u
\text{ encounters }A
\text{ before learning its identifier}
\right).
$$

稱：

$$
\boxed{
D_0
=
\text{Name-Free Discoverability}.
}
$$

這是本文最核心的 Discoverability 量。

## 12. Discovery 不只來自 Search

使用者可以透過：

$$
\mathcal C
=
\{
\text{search},
\text{recommendation},
\text{social},
\text{AI},
\text{media},
\text{store browse},
\text{citation},
\ldots
\}.
$$

令事件 $E_j$ 表示透過 channel $j$ 遇見 artifact。

則：

$$
D_0
=
P
\left(
\bigcup_{j=1}^{m}E_j
\right).
$$

只有在通道獨立時才有：

$$
D_0
=
1-
\prod_{j=1}^{m}(1-d_j),
$$

其中：

$$
d_j=P(E_j).
$$

## 13. Discovery Union Bounds

不假設通道獨立時：

$$
\max_jd_j
\le
D_0
\le
\min
\left(
1,
\sum_{j=1}^{m}d_j
\right).
$$

所以：

$$
\boxed{
\text{channel count}
\neq
\text{discovery coverage}.
}
$$

十個高度重疊渠道，可能仍然只覆蓋同一小群人。

## 14. Channel Overlap

令：

$$
\omega_{ij}
=
P(E_i\cap E_j).
$$

則二階 inclusion–exclusion 給出：

$$
D_0
\ge
\sum_id_i
-
\sum_{i<j}\omega_{ij}.
$$

因此跨平台真正有沒有提高 Discoverability，取決於：

$$
\boxed{
\text{新增的是新受眾路徑，還是舊受眾的重複入口。}
}
$$

## 15. Search Support

定義 artifact 的 top- $k$ query support：

$$
\mathcal S_A^{(k)}
=
\{
q:
r(A,q)\le k
\}.
$$

對目標使用者查詢分布：

$$
q\sim\mathcal Q_{\mathrm{target}},
$$

定義：

$$
\Omega_A^{(k)}
=
P_{q\sim\mathcal Q_{\mathrm{target}}}
\left(
q\in\mathcal S_A^{(k)}
\right).
$$

稱：

$$
\boxed{
\Omega_A^{(k)}
=
\text{Discovery Support Ratio}.
}
$$

## 16. Query-Support Mismatch

如果 artifact 的 retrieval support 主要集中在：

$$
\mathcal Q_{\mathrm{name}},
$$

但潛在使用者實際產生：

$$
\mathcal Q_{\mathrm{need}},
$$

且兩者重疊極低，則：

$$
R_{\mathrm{name}}\approx1
$$

仍可：

$$
R_{\mathrm{need}}\approx0.
$$

此狀態稱：

$$
\boxed{
\text{Query-Support Mismatch}.
}
$$

## 17. Known-Name / Discovery Separation Theorem

存在 artifact 與合法 retrieval system，使：

$$
R_{\mathrm{name}}=1
$$

但：

$$
D_0=0.
$$

### 證明

構造 artifact $A$。

系統只在 query 等於唯一識別符：

$$
q=q_A
$$

時返回 $A$ 並排名第一。

所以對：

$$
\mathcal Q_{\mathrm{name}}=\{q_A\},
$$

有：

$$
R_{\mathrm{name}}=1.
$$

假設所有尚未認識 $A$ 的使用者都不知道 $q_A$，且沒有 recommendation、social、media 或其他 discovery channel。

則：

$$
P
(
u
\text{ encounters }A
\mid
u\in\mathcal U_0(A)
)
=
0.
$$

故：

$$
D_0=0.
$$

因此：

$$
\boxed{
R_{\mathrm{name}}=1
\not\Rightarrow
D_0>0.
}
$$

$$
\boxed{\square}
$$

## 18. 定理的實際含義

這描述了一個很常見的數位狀態：

$$
\boxed{
\text{「知道的人找得到，不知道的人永遠不會知道。」}
}
$$

問題不是 artifact 不存在，也不是精確搜尋失效，而是：

$$
\boxed{
\text{discovery path is missing}.
}
$$

## 19. Existence Does Not Imply Retrievability

若 artifact 有公開 URL：

$$
X_A=1,
$$

但：

$$
J_A=0,
$$

則：

$$
r(A,q)=\infty
$$

對所有平台查詢成立，因此：

$$
R_k=0.
$$

故：

$$
\boxed{
\text{Public Existence}
\not\Rightarrow
\text{Retrievability}.
}
$$

## 20. Indexability Does Not Imply Exposure

即使：

$$
J_A=1,
$$

若：

$$
r(A,q)>k
$$

對幾乎所有目標查詢成立，則：

$$
R_k\approx0.
$$

因此：

$$
\boxed{
\text{Indexed}
\not\Rightarrow
\text{Actually Exposed}.
}
$$

## 21. Interface Exposure

即使 artifact 已進 top- $k$，使用者也不一定真正注意它。

令：

$$
e(A,q,u,p)\in[0,1]
$$

表示被檢索後實際進入使用者視野的概率。

則：

$$
V_A
=
E
[
\chi_k
e
].
$$

這一步受到 position、viewport、layout、snippet、thumbnail 與 interaction mode 影響。

因此 Retrievability 與真實 Exposure 仍須分開。

## 22. Exposure Gate

定義：

$$
G_{\mathrm{exp}}
=
P
(
\text{artifact becomes cognitively available}
\mid
\text{retrieved}
).
$$

則：

$$
P(\text{actual exposure})
=
R_kG_{\mathrm{exp}}.
$$

Retrieval 只是 exposure 的 gate 之一。

## 23. Match-Weighted Discoverability

只被任何人看到不夠。

更重要的是被有需求的人看到。

令：

$$
M(A,u)\in[0,1]
$$

表示 Audience Match。

定義：

$$
D_M(A)
=
E_{u\sim\mathcal U}
\left[
M(A,u)
\mathbf 1
(
u\text{ discovers }A
)
\right].
$$

稱：

$$
\boxed{
D_M
=
\text{Match-Weighted Discoverability}.
}
$$

## 24. Unmatched Virality

可以：

$$
D_0\gg0
$$

但：

$$
D_M\ll1.
$$

也就是作品被很多不匹配的人看到。

所以：

$$
\boxed{
\text{High Discovery}
\neq
\text{High Relevant Discovery}.
}
$$

## 25. Discovery Routing Gap

令：

$$
D_{\mathrm{ideal}}
$$

表示理想目標受眾下的可發現度。

定義：

$$
G_R
=
D_{\mathrm{ideal}}
-
D_M.
$$

稱：

$$
\boxed{
G_R
=
\text{Discovery Routing Gap}.
}
$$

它量化：

> 作品應該被哪些人看到，和實際被哪些人看到之間的路由落差。

## 26. Discovery Activation Bound

若採用 artifact 的必要條件是先發現 artifact，則：

$$
\mathrm{Adopt}
\subseteq
\mathrm{Discover}.
$$

所以：

$$
\boxed{
P(\mathrm{Adopt})
\le
P(\mathrm{Discover})
=
D.
}
$$

$$
\boxed{\square}
$$

Discoverability 因而構成 adoption 的 activation ceiling。

## 27. Population Adoption Upper Bound

對 $N$ 個潛在使用者：

$$
E[N_{\mathrm{adopt}}]
\le
\sum_{u=1}^{N}D_u.
$$

若：

$$
D_u=D,
$$

則：

$$
E[N_{\mathrm{adopt}}]
\le
ND.
$$

因此：

$$
\boxed{
\text{Discoverability places a hard activation ceiling on adoption}.
}
$$

## 28. 品質不能穿越零發現

Paper 01 已指出品質可能作用於：

$$
C,
W,
R_t.
$$

但若：

$$
D=0,
$$

則在採用必須先發現的模型中：

$$
P(\mathrm{Adopt})=0.
$$

不論：

$$
Q
$$

多高。

因此：

$$
\boxed{
D=0
\Rightarrow
\text{market-inactive quality}.
}
$$

## 29. Discoverability 也不推出 Success

反過來：

$$
D\gg0
$$

仍不推出：

$$
S\gg0.
$$

因為後續仍有：

$$
M,
C,
W,
R_t.
$$

所以：

$$
\boxed{
\text{Discoverability can be necessary for adoption without being sufficient for success}.
}
$$

## 30. Popularity Bias in Retrieval

既有 retrieval-based NLP 實驗發現，當不同實體共享名稱時，較罕見實體會更容易被 retriever 錯誤導向熱門同名實體。

因此：

$$
P_t
$$

可能反過來影響：

$$
R_{t+1}.
$$

低人氣 item 因而可能更難進入正確 retrieval support。

## 31. Brand Bias

Information Retrieval 模型分析也已觀察到 brand-name bias。

若品牌訊號影響 ranking：

$$
B_{\mathrm{brand}}
\rightarrow
R_k,
$$

則成熟品牌與新品牌即使與需求同樣相關，也可能處在不同 retrievability regime。

## 32. Algorithmic Invisibility

若：

$$
X_A=1,
$$

$$
Q_{\mathrm{target}}\gg0,
$$

但：

$$
D_M\le\epsilon
$$

對很小的 $\epsilon$ 成立，則稱：

$$
\boxed{
\text{Algorithmic Invisibility}.
}
$$

它不要求平台存在惡意。

它只描述：

> artifact 已存在且可能高品質，但演算法與資訊路由幾乎沒有把它送到正確受眾。

## 33. Cold-Start Invisibility

新 item 常有：

$$
P_0\approx0
$$

與極少 interaction data。

因此：

$$
P_0\downarrow
\rightarrow
V_1\downarrow
\rightarrow
P_1\downarrow
$$

可能形成低曝光自我確認狀態。

「沒有互動」於是可能不是品質差，而只是：

$$
\boxed{
\text{沒有足夠曝光形成可判定資料}.
}
$$

## 34. Item-Centric Exploration

近期工業推薦研究把問題反過來：

> 不只是替 user 找最佳 item，也替新 item 找最適合的 users。

這正對應：

$$
D_M.
$$

Discoverability 因此不是「曝光越多越好」，而是：

$$
\boxed{
\text{在 item 消失於低互動區以前，先找到正確受眾}.
}
$$

## 35. Exploration Traffic

近期大型推薦系統工作直接以 traffic allocation 改善新 item 的 initial visibility / discoverability。

這再次顯示：

$$
D
$$

不是 artifact 自帶的自然屬性。

它也受到平台資源配置影響。

## 36. Discovery Budget

令：

$$
B_D
$$

為新 item 的 exploration budget。

概念上：

$$
D
=
F
(
Q_{\mathrm{pred}},
M_{\mathrm{pred}},
B_D,
P_0,
\mathcal A
).
$$

若：

$$
B_D=0,
$$

系統可能根本沒有足夠樣本判斷 artifact 的真正品質。

## 37. Discovery–Evaluation Circularity

因此產生：

$$
\boxed{
\text{Exposure}
\rightarrow
\text{Feedback}
\rightarrow
\text{Quality Estimate}
\rightarrow
\text{Future Exposure}.
}
$$

平台需要互動資料估計 item，但又需要先給 item 曝光才能得到互動資料。

這是一個 Discovery–Evaluation Feedback Loop。

## 38. 自我確認性低曝光

若：

$$
V_0\ll1,
$$

則：

$$
n_0\ll1,
$$

品質估計不確定性：

$$
\operatorname{Var}(\hat Q)
$$

可能很高。

若推薦器又因不確定性而降低曝光：

$$
V_1\downarrow,
$$

則：

$$
\boxed{
\text{low exposure can generate evidence of nothing rather than evidence of low quality}.
}
$$

## 39. Discoverability 是向量

定義：

$$
D_{\mathrm{search}},
$$

$$
D_{\mathrm{rec}},
$$

$$
D_{\mathrm{social}},
$$

$$
D_{\mathrm{AI}}.
$$

則：

$$
\mathbf D_A
=
(
D_{\mathrm{search}},
D_{\mathrm{rec}},
D_{\mathrm{social}},
D_{\mathrm{AI}},
\ldots
).
$$

不同 artifact 的 discovery path 可以完全不同。

## 40. AI Discoverability

AI 搜尋／代理可以執行：

$$
\text{need description}
\rightarrow
\text{query expansion}
\rightarrow
\text{retrieval}
\rightarrow
\text{comparison}
\rightarrow
\text{recommendation}.
$$

它可能提高：

$$
R_{\mathrm{need}}.
$$

但最新 retrieval-bias 研究仍顯示 dense retrievers 存在多種系統性偏差，而且 query rewriting 不能在所有複合偏差條件下消除問題。

所以：

$$
\boxed{
\text{AI-mediated discovery}
\neq
\text{bias-free discovery}.
}
$$

## 41. AI Query Expansion

若需求 query：

$$
q_0
$$

被展開為：

$$
\{q_1,\ldots,q_m\},
$$

則：

$$
D_{\mathrm{AI-search}}
=
P
\left(
A
\in
\bigcup_{j=1}^{m}\operatorname{TopK}(q_j)
\right).
$$

這可以降低 Query-Support Mismatch。

但如果所有 query 都繼承相同 popularity 或 brand bias，長尾 artifact 仍可能不可見。

## 42. Retrievability 可以被工程化

已有工作直接利用 controllable query generation 改善 catalog content retrievability。

因此：

$$
\boxed{
R
}
$$

不是品質的自然副產品。

它可被：

- query coverage；
- retrieval training；
- indexing；
- ranking model

工程化改變。

## 43. Discoverability Engineering

可以拆成：

### Index Engineering

$$
J\uparrow.
$$

### Query-Support Engineering

$$
P
\left(
q\in\mathcal S_A^{(k)}
\mid
q\sim\mathcal Q_{\mathrm{target}}
\right)
\uparrow.
$$

### Ranking Engineering

$$
r(A,q)\downarrow.
$$

### Channel Engineering

$$
D_0\uparrow.
$$

### Audience Routing

$$
D_M\uparrow.
$$

因此「做 SEO」只涵蓋其中一小部分。

## 44. Discovery Surface

定義：

$$
\mathcal D_A(q,u,p,t)
=
P
(
u
\text{ encounters }A
\mid
q,p,t
).
$$

這是一個：

$$
\boxed{
\text{query-user-platform-time surface}.
}
$$

整體 Discoverability 為：

$$
D_A
=
\int
\mathcal D_A(q,u,p,t)
\,dP(q,u,p,t).
$$

所以不存在完全脫離環境的固定：

$$
D(A).
$$

## 45. Name-Free Discovery Surface

限制查詢不包含唯一名稱／identifier。

令：

$$
\mathcal Q_{\neg name}.
$$

則：

$$
D_0(A)
=
\int_{q\in\mathcal Q_{\neg name}}
\mathcal D_A(q,u,p,t)
\,dP(q,u,p,t).
$$

這就是「不知道名字的人能否遇見」的積分表示。

## 46. Discovery Elasticity

對可控變數 $z$：

$$
\varepsilon_{D,z}
=
\frac{\partial\log D}
{\partial\log z}.
$$

例如 artifact 可能：

$$
\varepsilon_{D,\mathrm{SEO}}\approx0
$$

但：

$$
\varepsilon_{D,\mathrm{recommendation}}\gg0.
$$

因此不同 artifact 需要不同 attention route。

## 47. Saturation

Discoverability 對資源通常具有飽和：

$$
D(B_D)
=
1-e^{-\alpha B_D}.
$$

當：

$$
B_D\rightarrow\infty,
$$

有：

$$
D\rightarrow1.
$$

不同渠道的 marginal discovery return 因此可能快速下降。

## 48. Discovery Frontier

給定資源：

$$
B,
$$

並令：

$$
\sum_{j=1}^{m}b_j=B.
$$

目標：

$$
\boxed{
\max_{\mathbf b}
D_M(\mathbf b)
}
$$

受限於：

$$
\sum_jb_j=B.
$$

這直接導向下一篇的 Attention Routing 問題。

## 49. Discoverability 與 Popularity 雙向耦合

通常：

$$
D_t
\rightarrow
P_{t+1}.
$$

但推薦系統也可能：

$$
P_t
\rightarrow
D_{t+1}.
$$

所以：

$$
\boxed{
D
\leftrightarrow
P
}
$$

可以形成 feedback。

## 50. Discoverability Debt

如果 artifact 長期低於理想發現水平：

$$
D(t)<D^\star(t),
$$

定義：

$$
L_D(T)
=
\int_0^T
\left(
D^\star(t)-D(t)
\right)dt.
$$

稱：

$$
\boxed{
\text{Discoverability Debt}.
}
$$

它不只表示損失當期流量，也可能損失 reviews、social proof、interaction data、word-of-mouth seeds 與 algorithmic confidence。

## 51. Discovery Debt 與 Cold Start

若：

$$
L_D
$$

過大，新 artifact 可能長期無法獲得足夠資料跨過平台的推薦／信任閾值。

因此早期 Discoverability 可以改變整個 lifecycle，而不只是短期曝光。

## 52. Quality–Discovery Separation

本文不預設：

$$
\operatorname{Corr}(Q,D)
$$

在所有市場為零。

它可能正、負或近零。

本文只主張：

$$
\boxed{
Q
\neq
D
}
$$

在概念與因果機制上成立。

## 53. High-Q / Low-D State

若：

$$
Q\ge q_0
$$

且：

$$
D_M\le d_0,
$$

稱：

$$
\boxed{
\text{High-Quality Low-Discoverability State}.
}
$$

這就是「作品很好但幾乎沒人知道」的正式 AMNESS 狀態。

## 54. Low-Q / High-D State

反過來：

$$
Q\le q_0,
$$

但：

$$
D\ge d_1
$$

同樣合法。

高 Discoverability 可以來自 promotion、brand、trend、controversy 或 placement。

所以：

$$
\boxed{
D
}
$$

不是品質判定器。

## 55. Discovery Calibration

若平台預測：

$$
\hat D_A
$$

而實際為：

$$
D_A,
$$

可以計算：

$$
\operatorname{MSE}_D
=
\frac1N
\sum_A
(\hat D_A-D_A)^2.
$$

並按新／舊 item、brand、genre、region 做 calibration slice。

## 56. Discovery Fairness

對 relevance 或 quality 近似的 artifact 集合：

$$
\mathcal A^\star,
$$

比較：

$$
D_A.
$$

若巨大差異主要由既有 popularity、品牌或索引 priors 形成，就可以研究：

$$
\boxed{
\text{discoverability inequality}.
}
$$

這與 retrievability bias / fair exposure 研究直接相接。

## 57. AMNESS-D Benchmark

本文提出：

**AMNESS Discoverability Benchmark（AMNESS-D）**

每個 artifact 記錄：

$$
(
X,
J,
R_{\mathrm{name}},
R_{\mathrm{need}},
V,
D_0,
D_M,
Q,
P,
S
).
$$

## 58. Artifact 類型

至少包含：

1. 成熟大品牌；
2. 新品牌；
3. 高品質 niche；
4. 新上架 item；
5. 高歧義名稱；
6. 長尾內容；
7. search 強但 recommendation 弱；
8. recommendation 強但 search 弱；
9. 跨語言 artifact；
10. 高品質但歷史 interaction 極少 artifact。

## 59. Query Set

對每個 artifact 建立：

$$
\mathcal Q_{\mathrm{name}},
$$

$$
\mathcal Q_{\mathrm{alias}},
$$

$$
\mathcal Q_{\mathrm{need}},
$$

$$
\mathcal Q_{\mathrm{category}},
$$

$$
\mathcal Q_{\mathrm{comparative}}.
$$

並測：

$$
R_k(A\mid\mathcal Q_i).
$$

如此可得到 artifact 的 query-support profile。

## 60. Name-Free Discovery Test

實驗流程：

1. 不告知 artifact 名稱；
2. 只提供使用需求；
3. 允許有限搜尋、瀏覽或 AI；
4. 記錄是否遇見 artifact；
5. 記錄 encounter time 與 path。

得到：

$$
D_0.
$$

這比「輸入完整名稱找不找得到」更接近真正 Discoverability。

## 61. Matched Discovery Test

只針對：

$$
M(A,u)\ge m_0
$$

的受試者統計：

$$
D_M.
$$

如此不會用不相關流量灌高發現率。

## 62. 可檢驗假說

### H1：Known-Name Separation Hypothesis

$$
R_{\mathrm{name}}
$$

與：

$$
D_0
$$

的相關性，應低於：

$$
R_{\mathrm{need}}
$$

與：

$$
D_0
$$

的相關性。

### H2：Query-Support Hypothesis

$$
\Omega_A^{(k)}
$$

比 raw page count 更能預測 name-free search discovery。

### H3：Cold-Start Discovery Hypothesis

控制品質後，新 item 的：

$$
D_M
$$

低於 warm item。

### H4：Exploration Activation Hypothesis

適度：

$$
B_D
$$

提高新 item：

$$
D_M
$$

並降低後續品質／人氣估計的不確定性。

### H5：Routing-Gap Hypothesis

$$
G_R
$$

越大，observed conversion 越容易低估 target-audience conversion。

## 63. 與 Paper 01 統一

Paper 01：

$$
\mathbf y_A
=
(Q,V,D,M,C,W,P,S).
$$

Paper 02 現在把：

$$
D
$$

展開為：

$$
\boxed{
D
=
\Psi
\left(
X,
J,
R_{\mathrm{name}},
R_{\mathrm{need}},
V,
\mathbf D_{\mathrm{channel}},
\mathcal U,
M
\right).
}
$$

因此 artifact quality 進入市場前，至少存在：

$$
\boxed{
\text{Information Access and Discovery Layer}.
}
$$

## 64. 與 Series I 的對稱性

Series I 得到：

$$
\text{公共實體存在}
\neq
\text{可搜尋}
\neq
\text{人類知名}.
$$

Series II 得到：

$$
\text{作品存在}
\neq
\text{可搜尋}
\neq
\text{被市場發現}.
$$

但 Series II 還額外需要：

$$
\boxed{
\text{Audience Match}
}
$$

與：

$$
\boxed{
\text{Conversion}.
}
$$

## 65. 理論邊界

本文不主張：

1. SEO 等於 Discoverability；
2. recommendation 等於全部 Discoverability；
3. exact-name search 沒有價值；
4. 高排名必然產生注意；
5. 多平台必然提高有效發現；
6. AI 搜尋消除長尾偏差；
7. cold-start 只由 popularity bias 造成；
8. 高 Discoverability 等於高品質；
9. 高品質 item 理應獲得相同曝光；
10. 存在平台無關的固定 Discoverability 常數。

本文只主張：

$$
\boxed{
\text{Existence}
\neq
\text{Indexability}
\neq
\text{Retrievability}
\neq
\text{Exposure}
\neq
\text{Name-Free Discoverability}.
}
$$

## 66. 結論

本文把「東西明明就在那裡，為什麼沒人知道？」拆成：

$$
\boxed{
X
\rightarrow
J
\rightarrow
R
\rightarrow
V
\rightarrow
D_0
\rightarrow
D_M.
}
$$

其中：

$$
X=\text{Public Existence},
$$

$$
J=\text{Indexability},
$$

$$
R=\text{Retrievability},
$$

$$
V=\text{Actual Exposure},
$$

$$
D_0=\text{Name-Free Discoverability},
$$

$$
D_M=\text{Match-Weighted Discoverability}.
$$

本文證明：

$$
\boxed{
R_{\mathrm{name}}=1
\not\Rightarrow
D_0>0.
}
$$

也就是：

$$
\boxed{
\text{「知道名稱就很好找」}
\neq
\text{「不知道名稱也有機會遇見」}.
}
$$

又因：

$$
\mathrm{Adopt}
\subseteq
\mathrm{Discover},
$$

得到：

$$
\boxed{
P(\mathrm{Adopt})
\le
D.
}
$$

所以 Discoverability 是品質進入市場的激活上界之一。

品質再高，如果：

$$
D=0,
$$

市場沒有機會觀察品質。

反過來：

$$
D\gg0
$$

也不保證成功，因為之後還有：

$$
M,
C,
W,
R_t.
$$

因此 Series II 到目前為止形成：

$$
\boxed{
\text{Quality}
\neq
\text{Discoverability}
\neq
\text{Success}.
}
$$

下一篇將研究：

$$
\boxed{
\text{Attention Routing and Conversion Field}.
}
$$

也就是在有限曝光資源下，注意力如何路由到正確受眾，並從「被看到」進一步轉換成「被採用」。

## 參考文獻

[1] Azzopardi, L., & Vinay, V. (2008). Retrievability: An Evaluation Measure for Higher Order Information Access Tasks. *Proceedings of CIKM 2008*, 561–570. DOI: 10.1145/1458082.1458157.

[2] Chen, A., Gudipati, P., Longpre, S., Ling, X., & Singh, S. (2021). Evaluating Entity Disambiguation and the Role of Popularity in Retrieval-Based NLP. *Proceedings of ACL-IJCNLP 2021*, 4472–4485. DOI: 10.18653/v1/2021.acl-long.345.

[3] Zhu, Z., He, Y., Zhao, X., Zhang, Y., Wang, J., & Caverlee, J. (2021). Popularity-Opportunity Bias in Collaborative Filtering. *Proceedings of WSDM 2021*. DOI: 10.1145/3437963.3441820.

[4] Penha, G., Palumbo, E., Aziz, M., Wang, A., & Bouchard, H. (2023). Improving Content Retrievability in Search with Controllable Query Generation. *Proceedings of The Web Conference 2023*, 3182–3192.

[5] Kim, Y., Rahimi, R., & Allan, J. (2024). Discovering Biases in Information Retrieval Models Using Relevance Thesaurus as Global Explanation. *Proceedings of EMNLP 2024*, 19530–19547. DOI: 10.18653/v1/2024.emnlp-main.1089.

[6] Wang, D., Jiao, J., Bhadury, A., Zhang, Y., Gao, M., & Dalal, O. (2025). Item-Centric Exploration for Cold Start Problem. *Proceedings of RecSys 2025*, 987–990.

[7] Wang, D., Jiao, J., Bhadury, A., Zhang, Y., & Gao, M. (2025). Item Level Exploration Traffic Allocation in Large-scale Recommendation Systems. arXiv:2505.09033.

[8] Goyal, A., Mukherjee, K., Saxena, A., Phukan, A., Chandrasekharan, E., & Sundaram, H. (2026). Masking or Mitigating? Deconstructing the Impact of Query Rewriting on Retriever Biases in RAG. *Findings of ACL 2026*, 8517–8530. DOI: 10.18653/v1/2026.findings-acl.414.

[9] Chang, X., Meng, Z., & Ganguly, D. (2025). T-Retrievability: A Topic-Focused Approach to Measure Fair Document Exposure in Information Retrieval. *CIKM 2025*.

## Series II 位置

1. Paper 01：品質不推出成功：基本非等價理論  
2. **Paper 02：Discoverability：存在、可搜尋與被發現的區別**  
3. Paper 03：注意力路由與轉換場  
4. Paper 04：窄域高品質與受眾上界  
5. Paper 05：口碑、知名度、銷量與採用率的動態耦合  
6. Paper 06：品質—名氣—成功象限與非單調動力學
