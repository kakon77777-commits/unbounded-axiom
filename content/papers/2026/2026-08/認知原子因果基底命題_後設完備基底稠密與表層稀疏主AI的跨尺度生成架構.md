# 認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構

**English Title:** *The Cognitive-Atomic Causal Basis Hypothesis: A Meta-Complete, Basis-Dense, Surface-Sparse Main AI for Cross-Scale Generative Intelligence*

**作者：** Neo.K  
**AI 協作：** Aletheia  
**研究脈絡：** EveMissLab / Logic Matrix / GCMS / 認知解構學 2.0  
**文件類型：** 命題猜想論文  
**版本：** v0.1  
**日期：** 2026-07-30  

---

## 摘要

本文提出「認知原子因果基底命題」（Cognitive-Atomic Causal Basis Hypothesis, CACBH），作為「壓縮全局智能命題」的進一步理論化。先前架構將主 AI 描述為在判斷、決策、推理、記憶、因果建模、路由與治理等後設維度上近似完備，而將大量具體領域能力交由子 Agent、專用模型、通用模型與大型模型按需展開。本文指出，若將此架構理解為「主 AI 本身只懂管理、對具體世界保持空白」，則會形成一個無法驗證外部智能、無法辨認跨領域同構、無法建立全局因果圖，也無法對未見問題進行有效拆解的空殼路由器。

本文因此提出一項關鍵修正：主 AI 應同時具備**後設完備、基底稠密、表層稀疏**三種性質。所謂基底稠密，是指主 AI 長期常駐大量跨領域的認知原子、最小生成因子、基本算子、穩定因果機制、尺度映射、不變量、邊界條件、反例模式與認知操作律；所謂表層稀疏，則表示它不必常駐所有論文、案例、數據、公式推導、專業語料、最新事實與高解析度執行細節。主 AI 依靠認知原子因果圖，從微觀、中觀、宏觀與元層級之間建立生成、投影、粗粒化、組合與反演關係，再透過 GCMS、子 Agent 與外部大模型按需展開特定領域能力。

本文將每個認知原子形式化為帶有內容、型別、方向、尺度、適用域、可逆性、信心、來源與生成規則的結構化對象；並建立認知原子因果圖，其關係包含因果、組合、尺度、約束、轉換、矛盾、證據與版本邊。本文主張，主 AI 的核心能力不只是記住一張知識圖，而是能以認知解構程序將表面知識剝離為底層操作單元，再將其編譯進跨尺度因果基底。此過程與因果表示學習、因果抽象、獨立因果機制、可組合推理模組、物件中心表示及層級式推理等研究存在局部同構，但本文不宣稱現有研究已證明一個可跨所有領域的唯一「認知原子週期表」。

本文進一步吸收元因果框架的限制：任何被主 AI 保存為底層規律的認知原子，都不應被無條件標記為普世真理，而需記錄其方向性、尺度、適用域、可逆性與證據狀態。由局部資料向上歸納的穩定律，不必然等同於真實世界向下生成的機制；跨領域語義相似也不必然等同於本體同一。故本文提出「候選基底、雙向生成、跨尺度驗證與可撤銷更新」的治理原則。

本文建立十五項命題與猜想、十三類失敗模式、九組可否證實驗及一組可實作的主 AI 運行時。本文的最終主張是：一個主 AI 若能把廣大知識空間壓縮為足夠稠密且可治理的認知原子因果基底，再以子 Agent 和外部模型展開高解析度能力，則它可能在有限常駐上下文中維持跨領域理解、長期連續性、組合泛化與全局因果控制；但此能力成立的關鍵不是原子數量，而是原子是否具有正確的型別、因果關係、尺度標記、可驗證來源與重編譯能力。

**關鍵詞：** 認知原子、因果基底、主 AI、基底稠密、表層稀疏、後設完備、最小生成因子、跨尺度因果、認知解構、OPS、因果抽象、獨立因果機制、GCMS、子 Agent、按需能力展開

---

# 0. 研究定位與聲明

本文是一篇命題性、架構性與可否證導向的理論稿。

本文不主張：

1. 已經找到人類或宇宙唯一正確的認知原子集合；
2. 任意領域都存在唯一、有限且可識別的最小生成基底；
3. 所有高階概念都可被無損地還原為低階原子；
4. 跨領域形式相似必然代表相同因果機制；
5. 任何既有「因果律清單」都已獲得普世本體地位；
6. 大模型內部已自然形成可讀取、可控制的完整因果原子圖；
7. 認知解構學 2.0 已被實驗證明是唯一必要的 AI 認知架構；
8. 小型主 AI 只要擁有原子表便能可靠治理大型模型；
9. 「原子」必須是不可再分的形上學實體；
10. 功能性的跨領域理解可以推出主體性或人格結論。

本文所稱「認知原子」，是相對於指定任務分布、尺度、表示語言與治理需求而言的**當前最小可重用認知操作單元**。它可以在未來被重新分解、合併、降級或撤銷。

---

# 1. 問題的提出：主 AI 到底應該常駐什麼？

## 1.1 空殼路由器問題

設主 AI 為：

$$
A_0.
$$

若其內部只保存：

- Agent 名單；
- 模型價格；
- 工具描述；
- 少量任務分類；
- 固定路由規則；

則它可以執行：

$$
q
\rightarrow
\operatorname{Route}(q)
\rightarrow
M_j(q),
$$

但不一定能判斷：

- 問題是否被錯誤表述；
- 外部模型是否偷換尺度；
- 兩個領域概念是否只在語言上相似；
- 某個結論是否違反基礎因果約束；
- 子 Agent 是否使用錯誤版本；
- 哪些局部結果會污染全局；
- 哪個未見問題需要創建新的任務分解。

此時：

$$
\boxed{
\text{路由能力}
\neq
\text{全局智能}.
}
$$

一個沒有實質基底知識的路由器，無法可靠評估比自己更強的外部模型。它的控制權只是名義上的，實際權威將轉移給輸出最流暢或最自信的被調用模型。

---

## 1.2 單體全知問題

另一個極端要求主 AI 常駐所有領域的高解析度知識：

$$
\mathcal K_{\mathrm{resident}}
\approx
\bigcup_{d\in\mathcal D}
\mathcal K_d.
$$

當領域、版本、工具和資料持續增加時，這會造成：

- 模型容量負擔；
- 上下文常駐負擔；
- 版本過時；
- 專業互相干擾；
- 知識更新成本；
- 所有能力同時退化的單點風險。

因此，主 AI 不能只是空殼，也不能把所有知識表面逐項常駐。

真正的問題是：

> 什麼知識應被壓縮為主 AI 的長期認知基底，什麼知識應交由外部記憶與子智能按需展開？

---

# 2. 三重性質：後設完備、基底稠密、表層稀疏

本文將主 AI 的能力結構寫為：

$$
\boxed{
A_0
=
A_{\mathrm{meta}}
\oplus
A_{\mathrm{basis}}
\oplus
A_{\mathrm{surface}}.
}
$$

## 2.1 後設完備

後設能力集合為：

$$
\mathcal C_{\mathrm{meta}}
=
\left\{
\begin{aligned}
&\mathsf{Interpret},
\mathsf{Decompose},
\mathsf{Judge},
\mathsf{Decide},\\
&\mathsf{Reason},
\mathsf{Route},
\mathsf{Integrate},
\mathsf{Verify},\\
&\mathsf{Compress},
\mathsf{Reconstruct},
\mathsf{ModelCausality},
\mathsf{Govern}
\end{aligned}
\right\}.
$$

主 AI 對指定任務分布 $Q$ 的後設完備度為：

$$
\operatorname{MC}(A_0\mid Q)
=
\frac{
\sum_{c\in\mathcal C_{\mathrm{meta}}}
w_c
\operatorname{Competence}(A_0,c\mid Q)
}{
\sum_c w_c
}.
$$

---

## 2.2 基底稠密

設跨領域認知原子全集為：

$$
\mathcal A^\ast
=
\bigcup_{d\in\mathcal D}
\mathcal A_d.
$$

主 AI 常駐的因果基底為：

$$
\mathcal B_0
=
\left(
\mathcal A_0,
\mathcal O_0,
\mathcal G_0,
\mathcal I_0
\right),
$$

其中：

- $\mathcal A_0$ ：認知原子；
- $\mathcal O_0$ ：生成與轉換算子；
- $\mathcal G_0$ ：原子因果圖；
- $\mathcal I_0$ ：跨表示與跨尺度不變量。

基底稠密度定義為：

$$
D_{\mathrm{basis}}
=
\frac{
\sum_{a\in\mathcal A_0}
w(a)
}{
\sum_{a\in\mathcal A^\ast_{\mathrm{relevant}}}
w(a)
}.
$$

此處的「稠密」不是要求窮盡所有可能原子，而是要求對主 AI 的任務域而言，關鍵生成因子與因果約束具有高覆蓋率。

---

## 2.3 表層稀疏

設全部高解析度領域內容為：

$$
\mathcal S^\ast
=
\bigcup_{d\in\mathcal D}
\left\{
\text{documents},
\text{examples},
\text{datasets},
\text{proofs},
\text{cases},
\text{current facts}
\right\}.
$$

主 AI 常駐的表層內容為 $\mathcal S_0$ ，表層稀疏性定義為：

$$
S_{\mathrm{surface}}
=
1-
\frac{
|\mathcal S_0|
}{
|\mathcal S^\ast|
}.
$$

理想主 AI 可能同時滿足：

$$
\operatorname{MC}(A_0)\rightarrow 1,
$$

$$
D_{\mathrm{basis}}\rightarrow 1,
$$

$$
S_{\mathrm{surface}}\rightarrow 1.
$$

這三者並不矛盾：

$$
\boxed{
\text{主 AI 可以很少常駐表面內容，}
\quad
\text{卻常駐很稠密的生成基底。}
}
$$

---

# 3. 知識的分層生成模型

本文將一個領域 $d$ 的知識分為：

$$
\mathcal K_d
=
\left(
\mathcal K_d^{\mu},
\mathcal K_d^{m},
\mathcal K_d^{M},
\mathcal K_d^{\Omega}
\right),
$$

其中：

- $\mathcal K_d^{\mu}$ ：微觀層；
- $\mathcal K_d^{m}$ ：中觀層；
- $\mathcal K_d^{M}$ ：宏觀層；
- $\mathcal K_d^{\Omega}$ ：元層或跨尺度層。

## 3.1 微觀層

包括：

- 基本對象；
- 局部狀態；
- 最小操作；
- 原子事件；
- 局部約束。

## 3.2 中觀層

包括：

- 模組；
- 子系統；
- 結構；
- 區域因果；
- 組織模式。

## 3.3 宏觀層

包括：

- 全局統計；
- 制度；
- 相變；
- 湧現；
- 集體行為；
- 系統級規律。

## 3.4 元層

包括：

- 尺度轉換；
- 不變量；
- 對稱與破缺；
- 粗粒化；
- 生成與投影；
- 可逆性；
- 因果方向；
- 模型適用域。

領域知識的生成不一定是單向的：

$$
\mathcal K_d^{\mu}
\rightarrow
\mathcal K_d^{m}
\rightarrow
\mathcal K_d^{M}.
$$

也可能存在：

$$
\mathcal K_d^{M}
\rightarrow
\operatorname{Constraint}
\left(
\mathcal K_d^{m},
\mathcal K_d^{\mu}
\right),
$$

以及：

$$
\mathcal K_d^{\Omega}
\leftrightarrow
\left(
\mathcal K_d^{\mu},
\mathcal K_d^{m},
\mathcal K_d^{M}
\right).
$$

因此，主 AI 需要保存的不是簡單層級樹，而是具有上下雙向、跨尺度和不可逆標記的因果圖。

---

# 4. 認知原子的正式定義

## 4.1 認知原子不是單字或標籤

本文定義認知原子：

$$
a_i
=
\left(
x_i,
\tau_i,
o_i,
\delta_i,
s_i,
d_i,
r_i,
c_i,
e_i,
v_i
\right),
$$

其中：

- $x_i$ ：內容或核心結構；
- $\tau_i$ ：型別；
- $o_i$ ：可作用於它的操作；
- $\delta_i$ ：因果方向；
- $s_i$ ：尺度；
- $d_i$ ：適用域；
- $r_i$ ：可逆性；
- $c_i$ ：信心與狀態；
- $e_i$ ：證據與來源；
- $v_i$ ：版本。

認知原子可以是：

- 一個邏輯約束；
- 一個因果機制；
- 一個生成算子；
- 一個尺度映射；
- 一個反例模式；
- 一個不可逆投影；
- 一個驗證程序；
- 一個問題分解模式；
- 一個最小可重用推理技能。

---

## 4.2 相對原子性

原子性不是絕對的。

對任務集合 $Q$ ，若一個單元 $a$ 滿足：

1. 可重用；
2. 可組合；
3. 進一步分解不會顯著提高任務效用；
4. 具有可測邊界；
5. 可獨立驗證或標記不確定性；

則稱其為相對於 $Q$ 的認知原子：

$$
\operatorname{Atomic}(a\mid Q)=1.
$$

若新任務出現後：

$$
\exists
\left\{
a_1,\ldots,a_k
\right\}
:
a
=
\operatorname{Compose}
\left(
a_1,\ldots,a_k
\right),
$$

且分解可顯著提升泛化與驗證，則原 $a$ 應降級為組合模組。

---

## 4.3 最小生成因子

對領域 $d$ ，定義最小生成基底：

$$
\mathcal B_d^{\min}
=
\operatorname{argmin}_{\mathcal B}
|\mathcal B|,
$$

使：

$$
\mathbb E_{q\sim Q_d}
\left[
F
\left(
\operatorname{Expand}
\left(
\mathcal B,q,\mathcal E_d
\right),
\mathcal K_d^{(q)}
\right)
\right]
\geq
\theta_F.
$$

其中：

- $\mathcal E_d$ ：外部證據與領域資料；
- $F$ ：重建或任務保真度；
- $\theta_F$ ：最低可接受閾值。

最小生成因子不是「用最少詞摘要一個領域」，而是找到足以重建該領域主要結構與判斷路徑的最小可操作集合。

---

# 5. 認知原子因果圖

主 AI 的基底記憶不是原子清單，而是：

$$
\mathcal G_A
=
\left(
V_A,
E_A
\right).
$$

其中：

$$
V_A=\mathcal A_0,
$$

且：

$$
E_A
=
E_{\mathrm{cause}}
\cup
E_{\mathrm{compose}}
\cup
E_{\mathrm{scale}}
\cup
E_{\mathrm{constraint}}
\cup
E_{\mathrm{transform}}
\cup
E_{\mathrm{contradict}}
\cup
E_{\mathrm{evidence}}
\cup
E_{\mathrm{version}}.
$$

## 5.1 因果邊

$$
a_i
\xrightarrow{\mathrm{cause}}
a_j.
$$

表示在指定條件下， $a_i$ 對 $a_j$ 具有生成或干預影響。

## 5.2 組合邊

$$
\left(
a_i,a_j
\right)
\xrightarrow{\mathrm{compose}}
a_k.
$$

表示某個高階單元由多個原子在約束下組成。

## 5.3 尺度邊

$$
a_i^{\mu}
\xrightarrow{\mathrm{coarse\ grain}}
a_j^{M}.
$$

表示微觀因子經粗粒化、統計或聚合形成宏觀結構。

## 5.4 約束邊

$$
a_i
\xrightarrow{\mathrm{constraint}}
\neg a_j
$$

或：

$$
a_i
\xrightarrow{\mathrm{constraint}}
\operatorname{Domain}(a_j)\subseteq D.
$$

## 5.5 轉換邊

$$
a_i^{(d_1)}
\xrightarrow{\phi}
a_j^{(d_2)}.
$$

表示兩個領域之間的候選結構映射。

## 5.6 矛盾邊

$$
a_i
\perp
a_j.
$$

表示兩個原子不能在相同語境、版本與尺度下同時被接受。

## 5.7 證據邊

$$
e_k
\xrightarrow{\mathrm{supports/refutes}}
a_i.
$$

## 5.8 版本邊

$$
a_i^{(v_t)}
\xrightarrow{\mathrm{revised}}
a_i^{(v_{t+1})}.
$$

---

# 6. 跨領域原子與不變量

## 6.1 形式相似不等於因果同一

設兩個領域中的結構為：

$$
a_i^{(d_1)},
\qquad
a_j^{(d_2)}.
$$

若存在映射：

$$
\phi:
a_i^{(d_1)}
\rightarrow
a_j^{(d_2)},
$$

只能先建立候選同構：

$$
a_i^{(d_1)}
\sim_{\phi}
a_j^{(d_2)}.
$$

要提升為因果同構，至少需要：

$$
C_{\mathrm{structure}}
\wedge
C_{\mathrm{intervention}}
\wedge
C_{\mathrm{scale}}
\wedge
C_{\mathrm{boundary}}
\wedge
C_{\mathrm{counterfactual}}.
$$

因此：

$$
\boxed{
\text{同形公式}
\not\Rightarrow
\text{同一機制}.
}
$$

---

## 6.2 候選跨域不變量

定義候選不變量：

$$
I_k
=
\operatorname{Stable}
\left(
\left\{
a_i^{(d)}
\right\}_{d\in\mathcal D_k}
\right).
$$

它可能在多個領域中表現為：

- 守恆；
- 對稱；
- 分解；
- 壓縮；
- 反饋；
- 演化；
- 選擇；
- 稀疏；
- 展開；
- 收斂；
- 相變；
- 局部—全局對偶。

但每個候選不變量仍需記錄：

$$
I_k
=
\left(
\text{Direction},
\text{Scale},
\text{Domain},
\text{Invertibility},
\text{Confidence},
\text{Evidence}
\right).
$$

這防止主 AI 將「在多個模型中有用」直接升格為「宇宙本體必然」。

---

# 7. 元因果標記：主 AI 不應把候選律當成絕對律

## 7.1 方向性

每個候選律 $L_i$ 應標記：

$$
D(L_i)
\in
\left\{
\uparrow,
\downarrow,
\updownarrow,
P,
?
\right\},
$$

分別表示：

- 下對上歸納；
- 候選上對下生成；
- 雙向保持；
- 普世平凡律候選；
- 未定。

## 7.2 可逆性

$$
R(L_i)
\in
\left\{
\text{bijective},
\text{many-to-one},
\text{one-to-many},
\text{noninvertible},
\text{stochastic}
\right\}.
$$

## 7.3 尺度

$$
S(L_i)
\in
\left\{
\mu,
m,
M,
\Omega,
\text{cross-scale}
\right\}.
$$

## 7.4 認識狀態

$$
C(L_i)
\in
\left\{
\text{observed},
\text{induced},
\text{generated},
\text{verified},
\text{contested},
\text{speculative},
\text{retracted}
\right\}.
$$

因此主 AI 常駐的不是教條式定律表，而是可更新的：

$$
\boxed{
\text{方向—尺度—域—可逆性—信心因果矩陣}.
}
$$

---

# 8. 認知解構學作為基底編譯器

## 8.1 表面知識的殼層

外部知識通常以以下形式出現：

$$
x
=
\left(
\text{terminology},
\text{narrative},
\text{examples},
\text{history},
\text{notation},
\text{domain assumptions}
\right).
$$

若直接存入主 AI，跨領域知識會形成大量互不相通的語料島。

---

## 8.2 OPS 類操作

定義去殼算子：

$$
\mathsf{OPS}(x)
=
x
-
\left(
\text{非必要修辭}
+
\text{偶然語境}
+
\text{重複投影}
\right).
$$

輸出不是簡短摘要，而是：

$$
\mathsf{OPS}(x)
=
\left(
\mathcal A_x,
\mathcal O_x,
\mathcal C_x,
\mathcal B_x
\right),
$$

其中：

- $\mathcal A_x$ ：候選認知原子；
- $\mathcal O_x$ ：生成算子；
- $\mathcal C_x$ ：約束與邊界；
- $\mathcal B_x$ ：反例與失敗條件。

---

## 8.3 認知基底編譯流程

完整流程為：

$$
\boxed{
\begin{aligned}
x
&\xrightarrow{\mathsf{Decontextualize}}
x'\\
&\xrightarrow{\mathsf{Decompose}}
\mathcal A_x\\
&\xrightarrow{\mathsf{CausalType}}
\mathcal G_x\\
&\xrightarrow{\mathsf{ScaleTag}}
\mathcal G_x^{S}\\
&\xrightarrow{\mathsf{CrossDomainAlign}}
\Phi_x\\
&\xrightarrow{\mathsf{Verify}}
\widetilde{\mathcal G}_x\\
&\xrightarrow{\mathsf{Compile}}
\mathcal G_A^{t+1}.
\end{aligned}
}
$$

認知解構在此不是單純理解技巧，而是把新知識轉換為主 AI 可重用因果基底的編譯程序。

---

# 9. 主 AI 的常駐記憶

主 AI 的常駐狀態定義為：

$$
S_0^t
=
\left(
G_t,
\mathcal G_A^t,
\mathcal I_t,
\mathcal Q_t,
\mathcal D_t,
\mathcal P_t,
\mathcal H_t
\right),
$$

其中：

- $G_t$ ：長期目標；
- $\mathcal G_A^t$ ：認知原子因果圖；
- $\mathcal I_t$ ：跨尺度不變量；
- $\mathcal Q_t$ ：未完成問題；
- $\mathcal D_t$ ：能力與 Agent 目錄；
- $\mathcal P_t$ ：權限與寫回政策；
- $\mathcal H_t$ ：決策、失敗與版本歷史。

高解析度內容保存於：

$$
\mathcal M_{\mathrm{external}}
=
\mathcal M_{\mathrm{source}}
\cup
\mathcal M_{\mathrm{semantic}}
\cup
\mathcal M_{\mathrm{episodic}}
\cup
\mathcal M_{\mathrm{candidate}}.
$$

主 AI 只需保存能重新進入外部記憶的因果索引與生成路徑。

---

# 10. 按需領域能力展開

對任務 $q$ ，主 AI 執行：

$$
\mathcal B_q
=
\operatorname{Subgraph}
\left(
\mathcal G_A,
q
\right).
$$

再選擇：

$$
\Pi_q
=
\operatorname{Plan}
\left(
q,
\mathcal B_q,
\mathcal D,
\mathcal P,
\mathcal R
\right),
$$

其中 $\mathcal R$ 是資源預算。

最後形成：

$$
\mathcal C_q^{\mathrm{expanded}}
=
\operatorname{Expand}
\left(
\mathcal B_q,
\mathcal M_{\mathrm{external}},
\left\{
A_i,M_j,T_k
\right\}
\right).
$$

展開可包含：

- 召回原始論文；
- 呼叫領域 Agent；
- 呼叫大型推理模型；
- 執行程式與模擬；
- 查詢最新資料；
- 尋找反例；
- 驗證因果方向；
- 回寫候選原子。

---

# 11. 認知原子因果基底主命題

## 命題 1：三重能力非矛盾命題

主 AI 可以同時具有：

$$
\operatorname{MC}(A_0)\rightarrow 1,
$$

$$
D_{\mathrm{basis}}(A_0)\rightarrow 1,
$$

$$
S_{\mathrm{surface}}(A_0)\rightarrow 1.
$$

後設完備、基底稠密與表層稀疏描述不同層級，不構成邏輯矛盾。

---

## 命題 2：空殼路由器不足命題

若：

$$
D_{\mathrm{basis}}(A_0)<\theta_B,
$$

則即使路由器能存取高能力模型，也無法可靠完成：

- 未見任務分解；
- 跨領域因果驗證；
- 權威輸出拒絕；
- 尺度錯置辨認；
- 全局污染治理。

因此：

$$
\boxed{
\text{模型可調用性}
\not\Rightarrow
\text{模型可治理性}.
}
$$

---

## 命題 3：基底壓縮優勢猜想

若領域知識能以可重用認知原子和生成規則表示，則：

$$
|\mathcal B_d|
\ll
|\mathcal K_d|,
$$

且：

$$
\operatorname{Expand}
\left(
\mathcal B_d,q,\mathcal E_d
\right)
\approx
\mathcal K_d^{(q)}.
$$

在此條件下，基底常駐可能比全文常駐提供更高的有效上下文密度。

---

## 命題 4：原子圖優於原子表命題

若只保存原子集合 $\mathcal A$ 而不保存因果圖 $\mathcal G_A$ ，則系統無法區分：

- 並列與生成；
- 相似與因果；
- 微觀與宏觀；
- 支持與反駁；
- 同一版本與歷史版本。

因此：

$$
U(\mathcal G_A)
>
U(\mathcal A)
$$

對需要推理、組合與驗證的任務一般成立。

---

## 命題 5：跨尺度生成猜想

若主 AI 擁有足夠正確的尺度邊：

$$
E_{\mathrm{scale}},
$$

則它在微觀機制到宏觀現象、宏觀約束到局部行為的跨尺度推理上，將優於只依賴語義相似檢索的系統。

---

## 命題 6：方向標記必要命題

若候選律缺少方向、尺度與可逆性標記，則主 AI 容易把：

$$
\mathcal C^{\uparrow}
$$

誤認為：

$$
\mathcal C^{\downarrow},
$$

把局部預測律誤認為上位生成機制。因此元因果標記是高風險推理的必要治理條件。

---

## 命題 7：認知解構增益猜想

具有認知解構與重編譯能力的主 AI，在未見任務上的原子抽取與新工作流生成品質，將高於固定本體或固定分類器：

$$
Q_{\mathrm{unseen}}^{\mathrm{deconstruct}}
>
Q_{\mathrm{unseen}}^{\mathrm{fixed}}.
$$

---

## 命題 8：獨立機制重用猜想

若環境由近似獨立、可重用的機制生成，主 AI 將知識分解為稀疏通信的機制模組，可能提高分布外組合與快速適應能力。

---

## 命題 9：原子識別非唯一命題

對同一觀測資料，可能存在多個不同基底：

$$
\mathcal B_1
\neq
\mathcal B_2,
$$

但：

$$
\operatorname{Expand}(\mathcal B_1)
\approx
\operatorname{Expand}(\mathcal B_2).
$$

因此，認知原子學習一般存在不可識別性，必須依賴干預、多環境、任務轉移、最小描述與外部證據約束。

---

## 命題 10：原子不是永久命題

當新證據或新尺度出現時：

$$
a_i
\rightarrow
\left\{
a_{i1},a_{i2},\ldots
\right\}
$$

或：

$$
\left\{
a_i,a_j
\right\}
\rightarrow
a_k.
$$

所以原子基底必須可版本化、可撤銷、可重新編譯。

---

## 命題 11：表層稀疏不等於事實稀疏命題

主 AI 可以不常駐所有最新事實，但必須保存：

- 如何取得最新事實；
- 如何判斷來源；
- 如何連接因果基底；
- 如何防止舊資料污染。

因此：

$$
\text{Surface Sparse}
\neq
\text{Evidence Blind}.
$$

---

## 命題 12：子 Agent 展開非替代命題

外部模型和子 Agent 的作用是展開、計算、查證與局部專業化，而不是替代主 AI 對底層因果、全局目標與治理責任的理解。

---

## 命題 13：原子基底容量相變猜想

當認知原子數量、連接品質與跨尺度映射超過某一臨界值：

$$
C_{\mathrm{basis}}
>
C_{\mathrm{crit}},
$$

系統可能由局部模式匹配轉入跨域組合與全局生成狀態。

此命題不預設相變必然存在，需以系統性實驗驗證。

---

## 命題 14：錯誤原子級聯命題

若高中心性原子 $a_h$ 錯誤，且被大量下游節點依賴，則污染可能滿足：

$$
P_{\mathrm{downstream}}
\propto
\operatorname{Centrality}(a_h)
\cdot
\operatorname{Confidence}(a_h)
\cdot
\operatorname{Reuse}(a_h).
$$

因此基底層需要比表層更嚴格的驗證與撤銷機制。

---

## 命題 15：認知原子因果基底命題

若主 AI 同時具有：

1. 足夠後設完備性；
2. 足夠認知原子覆蓋；
3. 可用的跨尺度因果圖；
4. 可治理的方向與證據標記；
5. 高保真外部記憶；
6. 可調用的異質子智能；
7. 對候選寫回的驗證與回滾；

則存在一類長期、跨領域任務分布 $Q^\ast$ ，使其：

$$
U_{\mathrm{CACB}}(Q^\ast)
>
U_{\mathrm{empty\ router}}(Q^\ast),
$$

且可能在成本、上下文使用和知識更新方面優於表層全量常駐的單體系統。

---

# 12. 主 AI 運行時

完整循環為：

$$
\boxed{
\begin{aligned}
q_t
&\xrightarrow{\mathsf{Interpret}}
z_t\\
&\xrightarrow{\mathsf{OPS/Deconstruct}}
\mathcal A_q\\
&\xrightarrow{\mathsf{CausalLocate}}
\mathcal G_q\\
&\xrightarrow{\mathsf{ScaleResolve}}
\mathcal G_q^{S}\\
&\xrightarrow{\mathsf{Recall}}
\mathcal M_q\\
&\xrightarrow{\mathsf{Plan}}
\Pi_q\\
&\xrightarrow{\mathsf{Delegate}}
\{A_i,M_j,T_k\}\\
&\xrightarrow{\mathsf{Integrate}}
Y_t\\
&\xrightarrow{\mathsf{CausalVerify}}
\widetilde Y_t\\
&\xrightarrow{\mathsf{CompileCandidate}}
\Delta\mathcal G_A\\
&\xrightarrow{\mathsf{Govern}}
\begin{cases}
\mathsf{Reject},\\
\mathsf{Quarantine},\\
\mathsf{AcceptCandidate},\\
\mathsf{CommitVersion}.
\end{cases}
\end{aligned}
}
$$

---

# 13. 資料模型草案

```yaml
cognitive_atom:
  atom_id: ATOM-CAUSAL-0001
  label: "局部到全局聚合"
  type: "scale_operator"

  core:
    expression: "macro = aggregate(micro, boundary, interaction)"
    operators:
      - aggregate
      - coarse_grain
      - constrain

  epistemic:
    direction: "upward_induction"
    reversibility: "many_to_one"
    scale_from: "micro"
    scale_to: "macro"
    domains:
      - physics
      - biology
      - social_systems
    confidence: 0.74
    status: "candidate_cross_domain"

  graph:
    causes: []
    composes:
      - ATOM-EMERGENCE-0002
    constrained_by:
      - ATOM-BOUNDARY-0007
    contradicts: []
    transformed_to: []

  evidence:
    source_ids:
      - SRC-001
      - SRC-002
    intervention_tests:
      - TEST-AGG-003
    counterexamples:
      - CASE-NONLINEAR-LOSS-004

  governance:
    visibility: "internal"
    write_policy: "dual_review"
    version: "v0.3"
```

---

# 14. 十三類失敗模式

## 14.1 偽原子化

將只是方便命名的概念誤認為最小機制。

## 14.2 過度原子化

把完整機制拆得過碎，失去關係與語境。

## 14.3 跨域同構幻覺

因公式或詞語相似，錯誤宣稱不同領域共享同一機制。

## 14.4 尺度錯置

將微觀律直接套用到宏觀，或以宏觀統計替代局部機制。

## 14.5 方向反演

把下對上歸納結果誤當成可唯一反演的上位生成律。

## 14.6 原子本體化

把目前有用的認知單元宣稱為宇宙永久不可分實體。

## 14.7 高中心性污染

一個錯誤核心原子影響大量推理與子 Agent。

## 14.8 表層證據脫離

主 AI 過度相信基底重建，不再回到原文與最新資料。

## 14.9 靜態基底僵化

因果圖無法因新證據更新，形成教條化世界模型。

## 14.10 子 Agent 權威倒置

外部模型以流暢敘述覆蓋主 AI 的原子級約束。

## 14.11 原子數量膨脹

系統持續創建近義原子，失去壓縮價值。

## 14.12 因果圖計算爆炸

跨領域因果圖過大，子圖尋址、驗證與更新成本失控。

## 14.13 認知單一化

所有子 Agent 共用同一基底後，獨立探索與替代本體逐步消失。

---

# 15. 可否證實驗

## 實驗 1：空殼路由器與基底主 AI

比較：

1. 只具模型目錄的路由器；
2. 具有摘要知識的主 AI；
3. 具有認知原子表的主 AI；
4. 具有原子因果圖和尺度標記的主 AI。

測量：

- 未見任務分解；
- 錯誤模型拒絕；
- 因果衝突辨認；
- 路由後悔；
- 全局任務成功率。

---

## 實驗 2：全文常駐與基底常駐

在相同上下文窗口下比較：

- 全文；
- 固定摘要；
- 向量檢索；
- 生成核；
- 認知原子因果子圖。

測量：

$$
D_{\mathrm{ctx}},
\quad
F_{\mathrm{task}},
\quad
F_{\mathrm{source}},
\quad
C_{\mathrm{latency}}.
$$

---

## 實驗 3：原子表與原子圖

對跨步驟推理、版本追溯與尺度轉換任務，消融所有因果邊，只保留節點標籤，測量性能差。

---

## 實驗 4：方向標記消融

移除：

- 上向歸納；
- 下向生成；
- 可逆性；
- 尺度；
- 適用域。

觀察系統是否更容易產生因果反演與偽普世錯誤。

---

## 實驗 5：跨領域同構驗證

建立一組：

- 真因果同構；
- 表面公式相似；
- 尺度錯置；
- 不可逆投影；
- 類比過伸；

的對抗資料集，測量主 AI 能否區分。

---

## 實驗 6：原子抽取方法

比較：

1. 固定本體；
2. 人工標註；
3. 語義聚類；
4. 因果表示學習；
5. 認知解構式抽取；
6. 人機協同抽取。

測量可重用性、組合泛化與可驗證性。

---

## 實驗 7：錯誤高中心性原子

向因果圖注入不同中心性的錯誤原子，測量下游污染、檢出時間、撤銷成本及回滾完整性。

---

## 實驗 8：原子容量相變

逐步增加：

- 原子數量；
- 正確邊比例；
- 跨尺度映射；
- 可組合操作；
- 外部證據覆蓋。

觀察是否存在非線性能力躍升。

---

## 實驗 9：認知單一化

比較：

- 所有 Agent 共用單一基底；
- 私有基底加共享核心；
- 多候選本體並行；
- 定期反例 Agent 介入。

測量多樣性、錯誤相關性與新理論發現率。

---

# 16. 評估指標

## 16.1 原子覆蓋率

$$
C_A
=
\frac{
|\mathcal A_{\mathrm{needed}}
\cap
\mathcal A_0|
}{
|\mathcal A_{\mathrm{needed}}|
}.
$$

## 16.2 邊正確率

$$
P_E
=
\frac{
|E_{\mathrm{correct}}|
}{
|E_{\mathrm{predicted}}|
}.
$$

## 16.3 跨尺度保真度

$$
F_S
=
1-
d
\left(
\operatorname{Project}_{\mu\rightarrow M},
\operatorname{Observed}_{M}
\right).
$$

## 16.4 基底壓縮率

$$
R_B
=
\frac{
|\mathcal K_d|
}{
|\mathcal B_d|
}.
$$

## 16.5 展開保真度

$$
F_X
=
\frac{
|\mathcal I_{\mathrm{critical}}(\mathcal K)
\cap
\mathcal I(\widehat{\mathcal K})|
}{
|\mathcal I_{\mathrm{critical}}(\mathcal K)|
}.
$$

## 16.6 因果反演錯誤率

$$
E_{\mathrm{inverse}}
=
\frac{
\text{錯把歸納律當唯一生成律的案例}
}{
\text{全部因果判斷}
}.
$$

## 16.7 基底污染傳播率

$$
P_{\mathrm{basis}}
=
\frac{
\text{受錯誤原子影響的下游節點}
}{
\text{全部可達下游節點}
}.
$$

## 16.8 原子重用率

$$
R_{\mathrm{reuse}}
=
\frac{
\text{跨任務被有效重用的原子}
}{
|\mathcal A_0|
}.
$$

## 16.9 新組合成功率

$$
G_{\mathrm{comp}}
=
\frac{
\text{未見組合任務成功數}
}{
\text{未見組合任務總數}
}.
$$

## 16.10 基底更新可撤銷性

$$
V_{\mathrm{rollback}}
=
\frac{
\text{可完整回復的基底修改}
}{
\text{全部基底修改}
}.
$$

---

# 17. 與現有 AI 研究的關係

## 17.1 因果表示學習

因果表示學習研究處理如何從低階觀測中發現高階潛在因果變量及其關係。這與本文「從表層知識抽取認知原子」具有直接局部關聯。

但本文的範圍更廣，因為認知原子不只來自感知資料，也可來自：

- 數學形式；
- 程式；
- 文獻；
- 制度；
- 推理程序；
- 人機協作歷史；
- 已知失敗模式。

---

## 17.2 因果抽象

因果抽象研究探討如何以高階簡化模型忠實表示低階機制。本文的跨尺度邊與高階認知原子可以被視為一類因果抽象。

然而，本文同時要求保存：

- 抽象方向；
- 失真；
- 非唯一性；
- 適用域；
- 反例；
- 版本；
- 治理狀態。

---

## 17.3 獨立因果機制

獨立因果機制假設鼓勵把生成過程分解為較自主、可重用的模組。這支持本文對認知原子與子 Agent 專業化的設計。

但真實知識不一定可完全分解為獨立機制，跨尺度與社會系統尤其可能存在高度糾纏。

---

## 17.4 可組合推理模組

近期研究開始把推理軌跡分解為可重用的原子技能與路由模組，並測試模型能否在未見問題中重新組合它們。這與本文的認知原子運行時高度接近。

本文的新增要求是：原子技能還需連接來源、因果方向、尺度、證據與寫回治理。

---

## 17.5 物件中心與層級表示

物件中心表示、層級因果表示與層級推理模型支持將複雜世界分解為較穩定的單元與多尺度動力學。

但本文的「認知原子」不限制為視覺物件，也不預設所有領域的基本單元皆為物件。

---

# 18. 與因果律分類原型的關係

既有因果律分類與週期表工作，已嘗試將基礎邏輯、數學結構、物理、資訊、生物、認知、社會、計算與元層規律壓縮成可辨識的短單元，並建立 AI 對應。這可被視為一種人工建立認知原子候選庫的原型。

本文對其重新定位如下：

$$
\boxed{
\text{因果律週期表}
\rightarrow
\text{候選認知原子目錄}
}
$$

而不是：

$$
\boxed{
\text{因果律週期表}
=
\text{已完成證明的宇宙終極公理集}.
}
$$

後續每個候選律都應增加：

- 方向；
- 尺度；
- 可逆性；
- 適用域；
- 證據；
- 反例；
- 版本；
- 可組合關係。

如此才能轉化為可供主 AI 實際運行的認知原子因果圖。

---

# 19. 工程路線

## 階段 1：原子候選庫

從既有理論、數學、物理、AI、認知與工程文件中抽取候選原子。

## 階段 2：原子型別系統

建立：

- 邏輯型；
- 因果型；
- 生成型；
- 尺度型；
- 約束型；
- 驗證型；
- 治理型。

## 階段 3：因果與尺度圖

建立多關係圖及來源閉包。

## 階段 4：GCMS 整合

使每個原子可以：

- 追溯原文；
- 讀取版本；
- 產生證據包；
- 進入候選／接受區；
- 被撤銷與回滾。

## 階段 5：主 AI 子圖尋址

根據任務動態抽取認知基底子圖。

## 階段 6：子 Agent 能力展開

將子圖與來源投影給專業 Agent 或大型模型。

## 階段 7：原子級驗證與編譯

將新結果重新解構為候選原子，經驗證後加入版本化基底。

---

# 20. 理論邊界與否證條件

若未來實驗顯示：

1. 原子因果圖不比高品質全文檢索或長上下文模型更有效；
2. 跨領域原子無法穩定識別，且表示高度任務依賴；
3. 基底壓縮造成的失真長期高於上下文節省；
4. 認知解構抽取不能提升未見任務分解；
5. 方向、尺度與可逆性標記無法降低因果錯誤；
6. 小型或中型主 AI 無法可靠治理強外部模型；
7. 原子圖更新成本與驗證成本超過其重用收益；
8. 高中心性原子污染不可有效隔離與回滾；
9. 多候選本體治理無法避免認知單一化；
10. 不存在任何任務分布使基底稠密、表層稀疏架構優於合理單體基準；

則本文命題應被拒絕、縮小適用範圍，或只保留為特定知識工程場景的實作模式。

---

# 21. 結論

本文提出的主 AI 不是一個只會派工的空白控制器，也不是一個試圖在單一上下文中保存全部文明知識的全量模型。

它的完整結構是：

$$
\boxed{
\begin{aligned}
\text{Main AI}
={}&
\text{Meta-Complete}\\
&+
\text{Basis-Dense}\\
&+
\text{Surface-Sparse}\\
&+
\text{Causally Structured}\\
&+
\text{Cross-Scale}\\
&+
\text{On-Demand Expandable}\\
&+
\text{Evidence-Governed}.
\end{aligned}
}
$$

其中，真正常駐的是：

$$
\boxed{
\text{認知原子}
+
\text{生成算子}
+
\text{因果關係}
+
\text{尺度映射}
+
\text{不變量}
+
\text{證據與版本}.
}
$$

高解析度領域能力則由：

$$
\boxed{
\text{GCMS}
+
\text{子 Agent}
+
\text{通用模型}
+
\text{大型模型}
+
\text{工具與環境}
}
$$

按需展開。

因此，主 AI 的全面性不是表面知識的全量堆積，而是：

> 對足夠多的底層生成因子、因果機制與跨尺度轉換具有高密度理解，並能把它們重新編譯成特定領域、特定任務與特定時刻所需的高解析度智能。

本文將此稱為：

# **認知原子因果基底智能。**

---

# 參考文獻

1. Schölkopf, B., Locatello, F., Bauer, S., Ke, N. R., Kalchbrenner, N., Goyal, A., & Bengio, Y. (2021). *Towards Causal Representation Learning*. Proceedings of the IEEE.
2. Geiger, A., et al. (2023). *Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability*. arXiv:2301.04709.
3. Xia, K., & Bareinboim, E. (2024). *Neural Causal Abstractions*. arXiv:2401.02602.
4. Ahuja, K., et al. (2023). *Interventional Causal Representation Learning*. ICML 2023.
5. Ahuja, K., et al. (2024). *Multi-Domain Causal Representation Learning via Weak Supervision*. AISTATS 2024.
6. Zhang, K., Xie, S., Ng, I., & Zheng, Y. (2024). *Causal Representation Learning from Multiple Distributions: A General Setting*. ICML 2024.
7. Talon, D., Lippe, P., James, S., Del Bue, A., & Magliacane, S. (2024). *Towards the Reusability and Compositionality of Causal Representations*. CLeaR 2024.
8. Markham, A., Hirsch, I., Chang, J. A., Solus, L., & Aragam, B. (2026). *Intervening to Learn and Compose Causally Disentangled Representations*. CLeaR 2026.
9. Parascandolo, G., Kilbertus, N., Rojas-Carulla, M., & Schölkopf, B. (2018). *Learning Independent Causal Mechanisms*. ICML 2018.
10. Goyal, A., et al. (2019). *Recurrent Independent Mechanisms*. arXiv:1909.10893.
11. Madan, K., et al. (2021). *Fast and Slow Learning of Recurrent Independent Mechanisms*. arXiv:2105.08710.
12. Bengio, Y. (2017). *The Consciousness Prior*. arXiv:1709.08568.
13. Dittadi, A., et al. (2022). *Generalization and Robustness Implications in Object-Centric Learning*. ICML 2022.
14. Liu, Y., et al. (2023). *Causal Triplet: An Open Challenge for Intervention-centric Causal Representation Learning*. CLeaR 2023.
15. Varici, B., et al. (2024). *General Identifiability and Achievability for Causal Representation Learning*. AISTATS 2024.
16. Morioka, H., & Hyvärinen, A. (2024). *Causal Representation Learning Made Identifiable by Grouping of Observational Variables*. ICML 2024.
17. Maasch, J., Kalantari, J., & Khezeli, K. (2025). *CausalARC: Abstract Reasoning with Causal World Models*. arXiv:2509.03636.
18. Wang, X., et al. (2025). *Hierarchical Reasoning Model*. arXiv:2506.21734.
19. *From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning*. OpenReview, 2026.
20. *A Theory of Atomic Features and Four Testable Predictions*. OpenReview, 2026.
21. Neo.K & Theia. (2026). *宇宙因果律的完整分類學：從經典邏輯到過程本體論的 31 個基本律*.
22. Neo.K & Theia. (2026). *宇宙因果律完整週期表：100 律完整版*.
23. Neo.K. (2026). *因果律的因果律：宇宙因果歸納、虛擬因果對照與普世平凡律*.
24. Neo.K. (2026). *認知解構學：形式定義與方法論 2.0*.
25. Neo.K & Aletheia. (2026). *壓縮全局智能命題：後設完備主 AI 與按需展開子智能的分層代理架構*.
26. Neo.K & Aletheia. (2026). *GCMS v1.0 與《可繼承的認知》系列*.

---

# 附錄 A：一句話命題

> **主 AI 的高階全面性，可能不是來自常駐所有領域的表面知識，而是來自一張高度稠密、跨尺度、可驗證且可重編譯的認知原子因果圖；子 Agent 與外部模型則負責把這張基底按任務展開成高解析度能力。**
