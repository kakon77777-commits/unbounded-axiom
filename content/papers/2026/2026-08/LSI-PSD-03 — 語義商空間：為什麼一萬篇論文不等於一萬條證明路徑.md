# LSI-PSD-03 — 語義商空間：為什麼一萬篇論文不等於一萬條證明路徑

## Semantic Quotient Space: Why Ten Thousand Papers Do Not Equal Ten Thousand Proof Routes

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 03  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Semantic Quotient and Deduplication Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文建立長程 AI 數學研究中的語義商空間、表示商空間、路徑商空間與障礙商空間框架。本文的「等價」「商空間」「canonicalization」「去重」首先是研究工程與 proof-space measurement 的操作概念；除非明確給出形式系統中的互推證明或其他可重現證據，不應把語義相似、embedding 鄰近、圖結構近似或 LLM 判斷直接稱為數學等價。本文不主張任何未解問題的全部證明路徑已可被完整分類，也不主張有限 corpus 的 quotient 結果等於真實數學空間的 quotient。

---

## 摘要

當 AI 能在同一數學問題上持續生成數百、數千甚至上萬份研究稿時，最容易出現的統計錯覺不是「完全沒有新東西」，而是相反：**把大量表面不同的文本、符號與局部推導誤認為大量彼此獨立的證明路徑。** 同一命題可以經由變數重命名、等價假設、座標變換、定義展開、引理重排、形式庫差異、tactic surface 差異與自然語言重述而產生大量外觀不同的研究產物。若將每份 artifact 都視為一個獨立 proof-space sample，則 coverage、novelty、sampling order、confluence 與 saturation 指標都會被系統性高估。

然而，簡單「去重」同樣危險。兩個字面上高度相似的敘述，可能因量詞順序、domain、regularity class、邊界條件、背景公理、library semantics 或 hidden assumptions 不同而具有不同真值條件。更進一步，即使兩個 theorem statement 在數學上互相等價，它們對當前 AI prover 而言也未必是相同搜尋狀態。2026 年關於 formal theorem proving 對稱性的研究顯示，語義等價的 rewrites 仍可造成顯著不同的 proof success；2025 年 Rocq proof engineering 的 goal clone detection 則直接發現大型 proof codebase 中存在 exact duplication、generalization 與 $\alpha$ -equivalent goals with different proofs；ASSESS 與 GTED 等 formal statement evaluation 工作也指出，字串相似、結構相似與語義可證等價需要被分離處理。

本文因此提出一個**多層語義商空間框架**。令原始研究產物空間為：

$$
\Omega_R^{raw}(Q).
$$

本文不使用單一等價關係，而定義一族由弱至強、用途不同的關係：

$$
\sim_{lex},
\quad
\sim_{\alpha},
\quad
\sim_{def},
\quad
\sim_{prop},
\quad
\sim_{route},
\quad
\sim_{obs},
\quad
\sim_{evid}.
$$

其中分別表示字面／表面規範化、變數重命名、定義等價、命題等價、證明路徑骨架等價、障礙等價與證據等價。本文進一步區分：

$$
\Omega_R^{math}(Q)
=
\Omega_R^{raw}(Q)/\sim_{prop}
$$

與：

$$
\Omega_R^{search}(Q),
$$

後者保留具體 representation、proof state、library context 與 search policy，因為在演算法層它們可能直接影響可達性與成功率。這形成本文的核心原則：

$$
\boxed{
\text{Mathematical redundancy}
\not\Rightarrow
\text{search-dynamical redundancy}.
}
$$

本文提出「不可過早商化原則」：任何合併操作都必須保留足以重建原始 assumptions、quantifiers、domains、dependencies、evidence 與 provenance 的資訊。embedding、lexical similarity 與 LLM semantic judgment 只能作候選生成器，不得獨立充當等價證明。對不可確定 pair，本文使用三值 relation：

$$
E_{ij}
\in
\{
\text{equivalent},
\text{distinct},
\text{undetermined}
\},
$$

避免因強行二分造成 semantic collision 或 false split。

在計量層，本文定義 quotient-adjusted novelty：

$$
\nu_i^{quot}
=
1-
\max_{j<i}
\operatorname{Sim}_{quot}(g_i,g_j),
$$

有效樣本數：

$$
N_{\mathrm{eff}}
=
\sum_{c\in\mathcal C}
w(c),
$$

以及 multiplicity profile、route-family entropy、semantic redundancy ratio 與 quotient-corrected coverage。由此，原本的：

$$
N=10{,}000
$$

可能在商化後只對應：

$$
N_{\mathrm{eff}}\ll10{,}000.
$$

但如果同一數學命題的不同 representation 對 prover 具有不同成功率，則這些 representation 又不能在 search-space 層被直接刪除。本文因此主張 proof-space observatory 必須同時保存「數學身份」與「搜尋身份」，並以可追溯的 equivalence graph 而非單一 embedding cluster 作為去重基礎。

本文最後將此框架接回 LSI-PSD-01 與 LSI-PSD-02：前兩篇定義了搜尋制度與邏輯空間積分，本文回答其必要前置問題——**究竟什麼才算一個新的研究點？** 若沒有語義商空間，coverage 可能只是文字生成量；若 quotient 過度，真正影響搜尋的 representation 差異又會被抹除。本文因此把「正確商化」定位為長程 AI 數學研究從文本堆積轉向可審計 proof-space science 的第一道結構門檻。

**關鍵詞：** 語義商空間、proof-space quotient、representation sensitivity、goal clone、 $\alpha$ -equivalence、命題等價、proof skeleton、obstruction equivalence、semantic deduplication、canonicalization、novelty、有效樣本數、AI 數學研究

---

# 1. 問題的真正起點：一萬篇不等於一萬個數學狀態

## 1.1 Raw count 的誘惑

假設一個長程 AI 研究系統在固定問題 $Q$ 上生成：

$$
N=10{,}000
$$

份 artifact。

最直覺的統計是：

$$
|\mathcal G_N|=10{,}000.
$$

若每篇都使用不同標題、不同符號、不同局部 lemma 與不同語言敘述，看起來似乎表示研究系統已經走過一萬個不同位置。

但這個推論沒有保證。

考慮一個最簡單的例子：

$$
a+b=b+a
$$

與：

$$
x+y=y+x.
$$

如果背景型別與假設相同，它們可能只是變數重命名。

若系統又生成：

$$
u+v=v+u,
$$

$$
p+q=q+p,
$$

$$
r+s=s+r,
$$

那麼 raw artifact count 增加了五次，但數學內容可能只增加零次。

因此：

$$
\boxed{
N_{\mathrm{artifact}}
\neq
N_{\mathrm{semantic\ states}}.
}
$$

## 1.2 在 AI 時代，表面變異會非常便宜

傳統人類研究中，重寫一篇數學論文有成本。

AI 生成使以下操作接近廉價：

- 重新命名變數；
- 改變定義順序；
- 把同一 lemma 拆成三個 lemma；
- 把三個 lemma 合成一個 proposition；
- 改用 Fourier / physical-space / geometric language；
- 改變自然語言敘述；
- 改變 theorem prover library calls；
- 改變 tactic sequence；
- 改變中間 auxiliary quantity；
- 把同一 proof idea 換成不同敘事框架。

因此：

$$
\text{surface diversity}
$$

可以快速增長，而：

$$
\text{structural diversity}
$$

未必同步增長。

這使得「去重」不再只是資料清理，而是 proof-space measurement 的必要數學前置。

## 1.3 但去重也可能毀掉真正的新資訊

反過來，考慮：

$$
\forall x\in X,\ \exists y\in Y,\ P(x,y)
$$

與：

$$
\exists y\in Y,\ \forall x\in X,\ P(x,y).
$$

文字高度相似。

但量詞順序改變後，命題通常完全不同。

再例如：

$$
u\in L^3(\mathbb R^3)
$$

與：

$$
u\in L^\infty_tL^3_x.
$$

符號差異看似很小，對 PDE regularity 問題卻可能改變 theorem 的實質。

所以：

$$
\boxed{
\text{text similarity}
\not\Rightarrow
\text{semantic equivalence}.
}
$$

因此本文同時反對兩種粗糙化：

$$
\text{每篇都算新}
$$

與：

$$
\text{看起來像就合併}.
$$

---

# 2. 從 artifact 到研究對象：先分層，不先商化

## 2.1 原始研究產物

令：

$$
g_i
$$

表示第 $i$ 個 research artifact。

它可以是：

- 一篇 paper；
- 一個 proof attempt；
- 一個 lemma bundle；
- 一份 formal theorem file；
- 一個 counterexample candidate；
- 一個 computational experiment；
- 一個 no-go note；
- 一次 route audit。

原始 artifact 空間寫成：

$$
\Omega_R^{raw}(Q)
=
\{g_1,g_2,\ldots\}.
$$

這個空間保留所有歷史痕跡。

它不是最終用來計算 coverage 的空間，但它必須被保存。

## 2.2 每個 artifact 不只是一段文字

本文把 artifact 抽取為：

$$
g_i
=
(
S_i,
A_i,
C_i,
D_i,
R_i,
O_i,
E_i,
V_i,
P_i
),
$$

其中：

- $S_i$：statement / target；
- $A_i$：assumptions；
- $C_i$：claims / lemmas；
- $D_i$：dependency structure；
- $R_i$：proof route；
- $O_i$：obstruction；
- $E_i$：evidence；
- $V_i$：verification state；
- $P_i$：provenance。

只有在這些結構被抽取後，「這兩篇是不是同一條路」才有意義。

## 2.3 表面文字只是其中一個投影

令文本投影為：

$$
\pi_{text}(g_i).
$$

令 claim graph 投影為：

$$
\pi_{claim}(g_i).
$$

令 route graph 投影為：

$$
\pi_{route}(g_i).
$$

令 obstruction 投影為：

$$
\pi_{obs}(g_i).
$$

則：

$$
\pi_{text}(g_i)
\neq
g_i.
$$

因此不能把文本 embedding 直接當作完整研究身份。

---

# 3. 「相同」不是一個 relation，而是一族 relations

## 3.1 第一層：字面等價

定義：

$$
g_i\sim_{lex}g_j
$$

若經過允許的 whitespace、格式、標點與 deterministic normalization 後，核心文本相同。

這只處理最便宜的 duplicate。

它可以抓：

- exact copy；
- Markdown formatting 差異；
- 標點與空格差異；
- metadata 順序差異。

但它幾乎不處理數學語義。

## 3.2 第二層： $\alpha$ -等價

定義：

$$
g_i\sim_{\alpha}g_j
$$

若差異主要來自 bound/free variable 的一致重命名，且不改變 binding structure。

例如：

$$
\forall x,\ P(x)
$$

與：

$$
\forall y,\ P(y)
$$

在適當條件下可屬於同一 $\alpha$ -class。

這一層在 proof engineering 中非常實際。Rocq 的 goal clone detection 已把 $\alpha$ -equivalent goals 視為可檢測的重複工作類型之一。

## 3.3 第三層：定義展開等價

定義：

$$
g_i\sim_{def}g_j
$$

若兩個 statement 或 proof state 僅因 definitional unfolding、notation expansion、syntactic sugar 或可逆 normalization 而不同。

例如某個 library abbreviation：

$$
A:=B\cap C
$$

展開後：

$$
x\in A
\Longleftrightarrow
x\in B\land x\in C.
$$

若形式系統判定兩者 definitionally equal，則它們可以在特定層級被合併。

## 3.4 第四層：命題等價

最強的數學核心之一是：

$$
g_i\sim_{prop}g_j
$$

當且僅當在指定背景理論 $\mathcal A$ 中：

$$
\mathcal A\vdash
Q_i\leftrightarrow Q_j.
$$

這比文字與結構相似強得多。

若背景理論不同，則 equivalence judgment 也可能不同。

因此完整記號應寫成：

$$
Q_i\sim_{prop}^{\mathcal A}Q_j.
$$

## 3.5 第五層：proof-route skeleton 等價

兩個 theorem statement 可以不同，但證明架構高度相同。

設 route graph：

$$
\Gamma_i=(V_i,E_i,\tau_i),
$$

其中 $\tau_i$ 是 node role：

$$
\tau_i(v)
\in
\{
A,L,B,C,O
\},
$$

分別表示 assumption、lemma、bridge、closure、obstruction。

若存在保留角色與核心 dependency 的映射：

$$
\phi:
\Gamma_i
\rightarrow
\Gamma_j,
$$

使兩圖在去除低階 notation 差異後同構或近似同構，則定義：

$$
g_i\sim_{route}g_j.
$$

這不是命題等價。

它表示：

> 這兩份研究在 proof architecture 上走的是同一類路。

## 3.6 第六層：obstruction 等價

定義：

$$
g_i\sim_{obs}g_j
$$

若兩條 route 最後失敗或停止於同一個 canonical obstruction family。

例如：

$$
R_1
\rightarrow
O^\star,
$$

$$
R_2
\rightarrow
O^\star.
$$

即使：

$$
R_1\not\sim_{route}R_2,
$$

仍可能：

$$
R_1\sim_{obs}R_2.
$$

這正是後續 LSI-PSD-06 的 confluence 核心。

## 3.7 第七層：evidence 等價

兩份 artifact 可能提出同一 claim，但 evidence 不同。

例如：

$$
C
\leftarrow
E_1
$$

與：

$$
C
\leftarrow
E_2.
$$

若 $E_1$ 是 formal proof、 $E_2$ 是 numerical experiment，不能因 claim 相同就把 evidence 層完全合併。

因此：

$$
g_i\sim_{claim}g_j
$$

不推出：

$$
g_i\sim_{evid}g_j.
$$

這一點對 scientific audit 特別重要。

---

# 4. 等價關係的層次不是單純線性階梯

最容易想像：

$$
\sim_{lex}
\subset
\sim_{\alpha}
\subset
\sim_{def}
\subset
\sim_{prop}.
$$

在某些形式化設定下可以近似這樣理解。

但 route equivalence 與 obstruction equivalence 並不一定落在線性鏈上。

可能：

$$
g_i\sim_{prop}g_j
$$

但：

$$
g_i\not\sim_{route}g_j.
$$

也可能：

$$
g_i\not\sim_{prop}g_j
$$

但：

$$
g_i\sim_{route}g_j.
$$

例如兩個不同定理都使用：

$$
\text{compactness}
\rightarrow
\text{limit object}
\rightarrow
\text{rigidity}
\rightarrow
\text{contradiction}.
$$

它們在命題上不同，但 route skeleton 同族。

因此本文把 equivalence structure 視為：

$$
\boxed{
\text{equivalence lattice / multi-relation graph}
}
$$

而不是單一 relation。

---

# 5. 語義商空間的第一個正式定義

## 5.1 數學命題商空間

固定背景理論 $\mathcal A$。

定義：

$$
\Omega_R^{math}(Q)
=
\Omega_R^{raw}(Q)/\sim_{prop}^{\mathcal A}.
$$

元素不是單篇 artifact，而是：

$$
[g]_{prop}.
$$

每個等價類可以包含：

- 多種 notation；
- 多種 formalization；
- 多種 natural-language rendering；
- 多個 proof scripts；
- 多個變數命名。

這是最接近「數學內容去重」的空間。

## 5.2 Route quotient

另外定義：

$$
\Omega_R^{route}(Q)
=
\Omega_R^{raw}(Q)/\sim_{route}.
$$

其元素：

$$
[g]_{route}
$$

代表一個 proof architecture family。

## 5.3 Obstruction quotient

再定義：

$$
\Omega_R^{obs}(Q)
=
\Omega_R^{raw}(Q)/\sim_{obs}.
$$

其元素：

$$
[g]_{obs}
$$

代表一個 obstruction family。

因此一份 corpus 可以有：

$$
N_{raw}=10{,}000,
$$

但：

$$
N_{prop}=1{,}200,
$$

$$
N_{route}=180,
$$

$$
N_{obs}=23.
$$

這三個數回答完全不同的研究問題。

---

# 6. 一個商空間不夠：數學身份與搜尋身份必須分離

## 6.1 表示在數學上可能冗餘

若：

$$
Q_i\sim_{prop}Q_j,
$$

數學家可能自然說：

> 這是同一個命題的兩種表示。

在純數學內容統計上，這樣 quotient 是合理的。

## 6.2 表示在 AI 搜尋上可能是因果變數

但是對 prover：

$$
P(
\operatorname{success}\mid
Q_i,R
)
$$

與：

$$
P(
\operatorname{success}\mid
Q_j,R
)
$$

可能不同。

2026 年「What are the Right Symmetries for Formal Theorem Proving?」直接研究了這種現象：語義等價的 statement rewrites 可造成 LLM prover 成功率大幅變動。

因此：

$$
\boxed{
Q_i\sim_{prop}Q_j
\centernot\Rightarrow
s_R(Q_i)=s_R(Q_j).
}
$$

## 6.3 搜尋身份

本文定義搜尋狀態：

$$
\sigma
=
(
[Q]_{prop},
\rho,
\Lambda,
\Pi,
\mathcal M,
B
),
$$

其中：

- $[Q]_{prop}$：數學命題身份；
- $\rho$：具體 representation；
- $\Lambda$：library / environment；
- $\Pi$：search policy；
- $\mathcal M$：可用方法族；
- $B$：資源界。

因此：

$$
\Omega_R^{search}(Q)
$$

不應對 $\rho$ 過早 quotient。

## 6.4 核心分離原則

本文提出：

$$
\boxed{
\textbf{Mathematical Identity}
\neq
\textbf{Search Identity}.
}
$$

以及：

$$
\boxed{
\text{Mathematical redundancy}
\not\Rightarrow
\text{search-dynamical redundancy}.
}
$$

這是整篇最重要的結論之一。

---

# 7. Representation Sensitivity Index

## 7.1 定義

對同一命題等價類：

$$
[Q]_{prop},
$$

令可審計表示集合為：

$$
\mathcal R(Q)
=
\{\rho_1,\ldots,\rho_m\}.
$$

定義成功率：

$$
p_k
=
P(
\operatorname{success}
\mid
Q,\rho_k,R
).
$$

定義：

$$
\operatorname{RSI}(Q;R)
=
\operatorname{Var}
(
p_1,\ldots,p_m
).
$$

稱為：

$$
\boxed{
\textbf{Representation Sensitivity Index}.
}
$$

## 7.2 另一個無尺度版本

可定義：

$$
\operatorname{RSI}_{range}
=
\max_k p_k-\min_k p_k.
$$

若：

$$
\operatorname{RSI}_{range}\approx0,
$$

表示 prover 接近 success invariance。

若：

$$
\operatorname{RSI}_{range}\gg0,
$$

表示 representation 是重要的 search variable。

## 7.3 為什麼 RSI 不是 theorem difficulty

一個命題可能平均成功率很低：

$$
\bar p\ll1,
$$

但：

$$
\operatorname{RSI}\approx0.
$$

這表示它在所有已測表示下都難。

另一命題可能：

$$
\bar p\approx0.5,
$$

但：

$$
\operatorname{RSI}\gg0.
$$

這表示其難度高度依賴表示。

因此：

$$
\boxed{
\text{difficulty}
\neq
\text{representation sensitivity}.
}
$$

---

# 8. Goal clone：形式 proof engineering 已經遇到同一個問題

2025 年 ECOOP 論文「Automatic Goal Clone Detection in Rocq」把 goal cloning 定義為 proof engineering 中的重複工作：相同或 $\alpha$ -equivalent goal 被多次證明。

該工作重要的不是某個單一數字，而是分類本身：

- exact goal duplication；
- generalization；
- $\alpha$ -equivalent goals with different proofs。

這三類直接顯示：

$$
\text{same goal}
$$

與：

$$
\text{same proof}
$$

不是同一件事。

形式上：

$$
Q_i\sim_{\alpha}Q_j
$$

仍可能：

$$
\pi_i\not\sim_{route}\pi_j.
$$

因此 proof corpus 去重至少要保存：

$$
([Q], [\pi]).
$$

而不是只保存其中一個。

---

# 9. Formal statement similarity：相似、等價與可證要拆開

## 9.1 字串相似不足

如果只用：

$$
\operatorname{Lev}(S_i,S_j)
$$

或 lexical overlap，則變數重命名會造成不必要距離。

## 9.2 純 proof-based equivalence 也不夠

如果只問：

$$
\mathcal A\vdash Q_i\leftrightarrow Q_j?
$$

則在 proof search 失敗時，系統只能得到：

$$
\text{unknown}.
$$

它不能提供 graded structural similarity。

## 9.3 ASSESS 的啟示

ASSESS 把：

- provability；
- likeness；
- semantic-preserving transformations；

分離，並以 operator tree 與 transformation-aware tree distance 建構 continuous similarity。

這正支持本文的立場：

$$
\boxed{
\text{semantic equivalence}
\neq
\text{structural likeness}.
}
$$

## 9.4 GTED 的啟示

GTED 先 standardize formal statements，再轉為 operator trees 進行距離估計。

對 proof-space observatory 而言，這類方法可作：

$$
\text{candidate pair ranking},
$$

但不是最終 merge authority。

---

# 10. 不可過早商化原則

本文正式提出：

$$
\boxed{
\textbf{Never quotient away information before preserving
the evidence required to reconstruct the distinction.}
}
$$

中文：

$$
\boxed{
\textbf{不可過早商化原則}.
}
$$

## 10.1 什麼資訊必須先保存

至少包括：

$$
\mathcal S_i
=
(
Q_i,
A_i,
\forall/\exists_i,
D_i,
B_i,
C_i,
E_i,
V_i,
P_i
).
$$

具體包含：

- 原始 statement；
- quantifier structure；
- domain；
- regularity / boundary conditions；
- background assumptions；
- dependencies；
- proof / counterexample evidence；
- verification state；
- provenance；
- source hash；
- version。

如果這些都沒保存，merge 是不可逆資訊損失。

## 10.2 商化是研究推論，不是壓縮格式

若把兩篇 artifact 合併為：

$$
[g],
$$

其實是在做一個 epistemic claim：

> 這兩份產物在某個指定 relation 下不應被計為兩個獨立狀態。

所以每次 quotient 都應記錄：

$$
\text{relation type}
+
\text{evidence}
+
\text{confidence}
+
\text{reversibility}.
$$

---

# 11. 三值等價：不要強迫所有 pair 立即二分

## 11.1 二值判斷過強

對兩個大型自然語言 proof attempts：

$$
g_i,g_j,
$$

常常無法立即知道：

$$
g_i\sim g_j
$$

或：

$$
g_i\not\sim g_j.
$$

如果系統強迫二分，就會產生：

- false merge；
- false split。

## 11.2 三值 relation

本文定義：

$$
E_{ij}^{(k)}
\in
\{
1,0,?
\},
$$

其中：

$$
1=\text{equivalent under relation }k,
$$

$$
0=\text{distinguishable under relation }k,
$$

$$
?=\text{undetermined}.
$$

## 11.3 Undetermined 不是失敗

在研究資料庫中：

$$
?
$$

是一個合法狀態。

它表示：

> 目前證據不足，尚不把兩者合併，也不宣告其不同。

這比錯誤確定性更有價值。

---

# 12. Semantic collision：過度商化的第一種災難

定義 semantic collision：

$$
g_i\not\sim_{prop}g_j
$$

但系統誤判：

$$
g_i\sim_{prop}g_j.
$$

這會造成：

$$
[g_i]=[g_j]
$$

被錯誤合併。

後果包括：

- 真正新 theorem 被吞掉；
- distinct obstruction 被合併；
- coverage 被低估；
- contradiction 被隱藏；
- provenance 被破壞。

因此：

$$
\boxed{
\text{false merge}
}
$$

通常比保守的暫時不合併更危險。

---

# 13. False split：商化不足的第二種災難

反過來：

$$
g_i\sim_{prop}g_j
$$

但系統持續視為：

$$
[g_i]\neq[g_j].
$$

這稱為 false split。

後果：

- novelty 被高估；
- coverage 被高估；
- saturation 被延遲看見；
- AI 不斷重做同一件事；
- route multiplicity 被誤認成 route diversity。

因此 quotient system 必須同時控制：

$$
\operatorname{FMR}
=
P(\text{false merge})
$$

與：

$$
\operatorname{FSR}
=
P(\text{false split}).
$$

---

# 14. 量詞、domain 與 assumptions 是語義身份的最低護欄

## 14.1 Quantifier signature

定義：

$$
\operatorname{QS}(Q)
=
(q_1,\ldots,q_m),
$$

其中：

$$
q_i\in\{\forall,\exists\}.
$$

若 quantifier dependency graph 不同，不應僅靠 embedding 合併。

## 14.2 Domain signature

定義：

$$
\operatorname{DS}(Q)
=
(
X_1,\ldots,X_n
),
$$

記錄變數與其 domain。

例如：

$$
x\in\mathbb R
$$

與：

$$
x\in\mathbb C
$$

不應被視為無害差異。

## 14.3 Assumption signature

令：

$$
\operatorname{AS}(Q)
=
\{A_1,\ldots,A_k\}.
$$

兩個 statement 的核心式子相同，但：

$$
\operatorname{AS}(Q_i)
\neq
\operatorname{AS}(Q_j)
$$

可能代表 theorem strength 完全不同。

## 14.4 Context signature

完整 context：

$$
\operatorname{CTX}(Q)
=
(
\operatorname{QS},
\operatorname{DS},
\operatorname{AS},
\Lambda,
\mathcal A
).
$$

若 context 未對齊，不應直接宣告 proposition equivalence。

---

# 15. Canonicalization 與 quotient 不同

## 15.1 Canonicalization

canonicalization 是選擇代表元：

$$
\kappa:
\Omega
\rightarrow
\Omega_{can}.
$$

理想上：

$$
x\sim y
\Rightarrow
\kappa(x)=\kappa(y).
$$

## 15.2 Quotient

quotient 則是建立等價類：

$$
q:
\Omega
\rightarrow
\Omega/\sim.
$$

canonicalization 可以幫助 quotient，但不是 quotient 本身。

## 15.3 Canonical form 可能不存在或成本過高

在大型自然語言研究 artifact 上，很難期待全域唯一 canonical form。

因此本文建議：

$$
\boxed{
\text{local canonicalization}
+
\text{equivalence graph}
}
$$

而不是追求一個虛假的 universal normal form。

---

# 16. 多階 canonical signature

每個 artifact 可建立：

$$
K(g)
=
(
K_0,
K_1,
K_2,
K_3,
K_4
).
$$

其中：

### $K_0$：surface signature

- normalized title；
- lexical hash；
- formula hash。

### $K_1$：statement signature

- quantifier tree；
- domain tree；
- assumption set；
- target operator tree。

### $K_2$：dependency signature

- theorem dependencies；
- lemma DAG；
- imported theory family。

### $K_3$：route signature

- proof tactic families；
- bridge lemmas；
- closure pattern；
- contradiction pattern。

### $K_4$：obstruction signature

- failure condition；
- uncontrolled quantity；
- missing implication；
- nonclosure mechanism。

這使 candidate dedup 可以逐層升級。

---

# 17. Proof-route graph 的商化

## 17.1 Route graph

令：

$$
\Gamma_i
=
(V_i,E_i,\tau_i,\lambda_i).
$$

其中：

- $V_i$：研究節點；
- $E_i$：依賴與推導邊；
- $\tau_i$：角色標籤；
- $\lambda_i$：語義標籤。

## 17.2 Skeleton operator

定義：

$$
\operatorname{Skel}(\Gamma_i)
$$

移除：

- 變數名稱；
- 無關 formatting；
- 某些低階 library tactic；
- 可證明為純 administrative 的節點。

保留：

- assumption family；
- principal lemma；
- bridge；
- closure；
- obstruction。

## 17.3 Route similarity

定義：

$$
S_{route}(i,j)
=
\Phi(
\operatorname{Skel}(\Gamma_i),
\operatorname{Skel}(\Gamma_j)
).
$$

 $\Phi$ 可以由：

- graph edit distance；
- role-aware graph matching；
- dependency motif matching；
- formal transformation；

構成。

## 17.4 Route equivalence 不應只靠 threshold

若：

$$
S_{route}(i,j)>\theta,
$$

最多表示：

$$
\text{candidate route-equivalence}.
$$

正式 merge 還應檢查：

- 核心 assumptions 是否對應；
- closure condition 是否同型；
- obstruction 是否真的同族；
- 是否有可逆 mapping。

---

# 18. Obstruction canonicalization

## 18.1 為什麼障礙比論文標題更穩定

一個研究 route 可能多次改名：

$$
\text{energy barrier}
\rightarrow
\text{closure gap}
\rightarrow
\text{critical residue}.
$$

如果實際都指：

$$
\text{某個相同 quantity 無法被現有 estimate 控制},
$$

那應建立 canonical obstruction ID。

## 18.2 Obstruction record

本文建議：

```text
obstruction_id
target_claim
failed_implication
required_bound
available_bound
missing_margin
domain
assumptions
first_seen
revisit_count
route_sources
verification_status
```

## 18.3 Obstruction equivalence

兩個 obstruction：

$$
O_i,O_j
$$

若存在保留 failure semantics 的 mapping：

$$
\psi:O_i\leftrightarrow O_j,
$$

才可合併。

僅僅都寫：

> closure problem

遠遠不夠。

---

# 19. 證據不能被 quotient 掉

## 19.1 同 claim，多 evidence

設：

$$
C^\star
$$

被三份 artifact 支持：

$$
E_1=\text{formal proof},
$$

$$
E_2=\text{symbolic computation},
$$

$$
E_3=\text{numerical experiment}.
$$

claim 層可以合併：

$$
[C_1]=[C_2]=[C_3],
$$

但 evidence 應保存為多重邊：

$$
E_1,E_2,E_3
\rightarrow
C^\star.
$$

## 19.2 Evidence multiplicity 有價值

如果三個真正獨立 evidence source 指向同一 claim：

$$
\operatorname{Ind}(E_1,E_2,E_3)>0,
$$

那不是重複浪費。

這與三篇文本都複製同一 proof 完全不同。

因此：

$$
\boxed{
\text{semantic deduplication}
\neq
\text{evidence deduplication}.
}
$$

---

# 20. 來源與 provenance 是商化後仍須保留的纖維

可以把 quotient 想成：

$$
q:
\Omega^{raw}
\rightarrow
\bar\Omega.
$$

對每個商空間元素：

$$
\bar g\in\bar\Omega,
$$

其 fiber：

$$
q^{-1}(\bar g)
$$

包含所有原始 artifact。

本文主張：

$$
\boxed{
q^{-1}(\bar g)
\text{ 必須可追溯。}
}
$$

這樣使用者仍能知道：

- 哪些 AI 生成過；
- 哪些版本先出現；
- 哪些 proof 不同；
- 哪些 evidence 獨立；
- 哪些 artifact 被 merge；
- merge 理由是什麼。

---

# 21. 商空間 novelty：真正的新東西是什麼

## 21.1 Raw novelty

定義：

$$
\nu_i^{raw}
=
1-
\max_{j<i}
S_{text}(g_i,g_j).
$$

這回答：

> 文字看起來有多新？

## 21.2 Proposition novelty

定義：

$$
\nu_i^{prop}
=
\mathbf 1
\left(
[g_i]_{prop}
\notin
\{[g_j]_{prop}:j<i\}
\right).
$$

## 21.3 Route novelty

定義：

$$
\nu_i^{route}
=
\mathbf 1
\left(
[g_i]_{route}
\notin
\{[g_j]_{route}:j<i\}
\right).
$$

## 21.4 Obstruction novelty

定義：

$$
\nu_i^{obs}
=
\mathbf 1
\left(
[g_i]_{obs}
\notin
\{[g_j]_{obs}:j<i\}
\right).
$$

## 21.5 Novelty vector

因此：

$$
\boxed{
\boldsymbol\nu_i
=
(
\nu_i^{raw},
\nu_i^{prop},
\nu_i^{route},
\nu_i^{obs},
\nu_i^{evid}
).
}
$$

這比單一 cosine novelty 更有研究價值。

---

# 22. 一個極重要的四象限

令：

$$
\nu^{raw}
$$

代表表面新穎度，

$$
\nu^{route}
$$

代表 route 新穎度。

可形成四象限。

## 象限 I：表面新，路徑也新

$$
\nu^{raw}\uparrow,
\qquad
\nu^{route}\uparrow.
$$

是真正高價值新探索候選。

## 象限 II：表面新，路徑舊

$$
\nu^{raw}\uparrow,
\qquad
\nu^{route}\downarrow.
$$

可能只是 rephrasing / reparameterization。

## 象限 III：表面舊，路徑新

$$
\nu^{raw}\downarrow,
\qquad
\nu^{route}\uparrow.
$$

這往往最容易被文字相似度漏掉。

小修改可能帶來新 closure。

## 象限 IV：表面舊，路徑也舊

$$
\nu^{raw}\downarrow,
\qquad
\nu^{route}\downarrow.
$$

高概率為真正重訪。

---

# 23. Multiplicity：同一類被重訪多少次

對 equivalence class：

$$
c\in\Omega/\sim,
$$

定義 multiplicity：

$$
m(c)
=
|\{g_i:q(g_i)=c\}|.
$$

如果：

$$
m(c)\gg1,
$$

代表該類被高頻重訪。

但高 multiplicity 有至少三種解釋：

1. 無意義重複；
2. search basin 有強吸引力；
3. 同一數學類有多種 search-effective representation。

所以：

$$
m(c)
$$

本身不是壞事。

需要和：

$$
\operatorname{RSI}(c)
$$

一起看。

---

# 24. 有效樣本數

## 24.1 最粗版本

若所有 exact-equivalent artifact 只算一次：

$$
N_{\mathrm{eff}}
=
|\Omega/\sim|.
$$

## 24.2 權重版本

對每個 class：

$$
c,
$$

給予權重：

$$
w(c)
=
f(
\text{semantic novelty},
\text{route novelty},
\text{evidence independence},
\text{verification}
).
$$

則：

$$
N_{\mathrm{eff}}
=
\sum_c w(c).
$$

## 24.3 Representation-sensitive correction

若同一 proposition class 的不同 representation 對 search success 有可測差異，則：

$$
w(c)
$$

不應固定為 $1$。

可以寫：

$$
w(c)
=
1+\lambda \Psi(\operatorname{RSI}(c)),
$$

其中：

$$
\Psi(0)=0.
$$

這表示：

> 數學上同一個命題，在 search dynamics 上仍可能提供額外實驗資訊。

---

# 25. Semantic Redundancy Ratio

定義：

$$
\operatorname{SRR}
=
1-
\frac{N_{\mathrm{eff}}}{N_{raw}}.
$$

若：

$$
\operatorname{SRR}\approx0,
$$

表示 raw corpus 多數產物都保有獨立有效結構。

若：

$$
\operatorname{SRR}\rightarrow1,
$$

表示大量 artifact 在所選 quotient 下是重複。

但必須標明 quotient type：

$$
\operatorname{SRR}_{prop},
\quad
\operatorname{SRR}_{route},
\quad
\operatorname{SRR}_{obs}.
$$

否則數字沒有意義。

---

# 26. Route-family entropy

令 route classes：

$$
\mathcal C_{route}
=
\{c_1,\ldots,c_k\}.
$$

令：

$$
p_i
=
\frac{m(c_i)}{\sum_jm(c_j)}.
$$

定義：

$$
H_{route}
=
-\sum_{i=1}^{k}
p_i\log p_i.
$$

若：

$$
H_{route}
$$

很低，表示大量研究集中於少數 route family。

若：

$$
H_{route}
$$

很高，表示探索分散。

## 26.1 Normalized entropy

$$
\widehat H_{route}
=
\frac{H_{route}}{\log k}.
$$

使：

$$
0\leq\widehat H_{route}\leq1.
$$

## 26.2 解讀限制

高 entropy 不一定好。

如果大量 route 都是低品質 hallucination：

$$
H_{route}\uparrow
$$

仍可能沒有數學價值。

所以 entropy 必須配合 verification weighting。

---

# 27. Verification-weighted quotient

對 class：

$$
c,
$$

定義 verifier confidence：

$$
v(c)\in[0,1].
$$

例如：

- formally verified theorem：接近 $1$ ；
- independently reproduced computation：高；
- heuristic argument：中；
- unsupported LLM claim：低。

定義：

$$
N_{\mathrm{eff}}^{ver}
=
\sum_c
v(c)w(c).
$$

這比單純 class count 更接近研究有效量。

但：

$$
v(c)
$$

不能假裝是一個普適真理機率。

它只是 evidence status 的 operational weight。

---

# 28. LSI-PSD-02 coverage 必須做 quotient correction

前篇定義：

$$
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
).
$$

若沒有 quotient，可能出現：

$$
C_N^{state}\uparrow
$$

只是因為：

$$
\text{同一狀態被重寫很多次}.
$$

因此本文修正：

$$
\widetilde C_N^{state}
=
C_N^{state}
\big/
\sim_{state}.
$$

更一般：

$$
\widetilde{\mathbf C}_N
=
\operatorname{QuotientCorrect}
(
\mathbf C_N,
\mathcal E_N
).
$$

其中：

$$
\mathcal E_N
$$

是已審計 equivalence graph。

---

# 29. Coverage 的分母問題與 quotient 的分母問題不同

即使已完成 perfect dedup：

$$
N_{eff}
$$

仍不能推出：

$$
\frac{N_{eff}}{|\Omega^{true}|}.
$$

因為：

$$
|\Omega^{true}|
$$

通常未知。

因此語義商化解決的是：

$$
\boxed{
\text{不要重複計數}
}
$$

而不是：

$$
\boxed{
\text{知道全域總空間大小}.
}
$$

這兩個問題必須分開。

---

# 30. 商空間與 higher-order sampling 的關係

LSI-PSD-04 將定義：

$$
\Omega^{(0)},
\Omega^{(1)},
\Omega^{(2)},\ldots
$$

若一階狀態沒有先 quotient，則二階 relation 會被重複污染。

例如：

$$
x_1\sim x_2\sim x_3
$$

卻被當成三個獨立 state。

那 transition：

$$
T(x_1),
T(x_2),
T(x_3)
$$

會被誤認為三條獨立二階樣本。

因此：

$$
\boxed{
\text{higher-order sampling requires lower-order quotient discipline}.
}
$$

---

# 31. Representation 不應在 higher-order analysis 前被刪掉

但另一面：

若：

$$
x_1\sim_{prop}x_2
$$

而：

$$
T(x_1)\neq T(x_2)
$$

對 prover 而言表示不同 representation 產生不同 transition。

這本身就是二階資訊。

所以 LSI-PSD-04 必須保留：

$$
([x]_{prop},\rho)
$$

而不是只保留：

$$
[x]_{prop}.
$$

這再度說明：

$$
\text{math quotient}
$$

與：

$$
\text{search quotient}
$$

不能混用。

---

# 32. Cross-formal-system translation：同一命題跨 proof assistant 仍有身份問題

ProofGym 等工作嘗試在 Lean、Coq/Rocq、Isabelle 等 formal systems 間提供共同介面。

這對本系列很重要，因為長期 proof-space science 不應把：

$$
\text{Lean theorem}
$$

與：

$$
\text{Rocq theorem}
$$

自動視為兩個不同數學命題。

但跨系統 equivalence 也不是字串比較可以解決。

應建立：

$$
Q^{Lean}
\leftrightarrow
Q^{Rocq}
\leftrightarrow
Q^{Isabelle}
$$

的 alignment evidence。

只有當 semantics、assumptions 與 imported foundations 對齊時，才可建立跨系統 proposition identity。

---

# 33. Formal proof state factorization 對 quotient 的啟示

LeanTree 把複雜 proof state factorize 成較簡單、可獨立處理的 branches。

這提醒我們：

$$
\text{state identity}
$$

也可能具有分解結構。

若：

$$
s
=
(s_1,\ldots,s_k),
$$

兩個 proof state：

$$
s,s'
$$

可能只差某個獨立 branch。

所以不能只用整段 state string 判斷 duplicate。

可定義：

$$
\operatorname{Fact}(s)
=
\{[s_1],\ldots,[s_k]\}.
$$

然後比較 factorized signatures。

---

# 34. 商空間不是刪資料，而是增加索引層

錯誤做法：

```text
artifact A
artifact B
artifact C
↓
merge
↓
只留下 A
```

本文建議：

```text
artifact A ─┐
artifact B ─┼──> equivalence_class EC-17
artifact C ─┘

EC-17:
  relation: proposition_equivalence
  evidence: ...
  confidence: ...
  representative: A
  members: [A,B,C]
```

也就是：

$$
\boxed{
\text{quotient layer}
\neq
\text{destructive deletion}.
}
$$

---

# 35. Equivalence graph

定義圖：

$$
\mathcal E
=
(V,E),
$$

其中：

$$
V=\{g_i\},
$$

邊：

$$
e_{ij}
=
(
k,
status,
evidence,
confidence
).
$$

其中 $k$ 可為：

$$
lex,\alpha,def,prop,route,obs,evid.
$$

因此同一 pair 可以有：

$$
g_i\sim_{prop}g_j
$$

但：

$$
g_i\not\sim_{route}g_j.
$$

graph model 能自然表達這種多重關係。

---

# 36. Equivalence class 不一定應立刻做 transitive closure

對真正形式等價：

$$
\sim_{prop}
$$

若已嚴格證明為 equivalence relation，可以做 transitive closure。

但對 heuristic relation：

$$
\approx_{route},
$$

若只靠 threshold similarity，則：

$$
A\approx B,
\quad
B\approx C
$$

不一定：

$$
A\approx C.
$$

因此 heuristic route clustering 不應冒充真正 quotient。

本文建議區分：

$$
\sim
$$

與：

$$
\approx.
$$

前者是 audited equivalence。

後者是 similarity / candidate relation。

---

# 37. Pseudometric 比硬 equivalence 更適合早期 corpus

定義：

$$
d_k(g_i,g_j)\geq0.
$$

若：

$$
d_k=0
$$

可能表示在某層無法區分。

但不同點仍可有零距離，所以可先使用 pseudometric。

例如：

$$
d_{route}
=
1-S_{route}.
$$

再由：

$$
d_{route}<\epsilon
$$

產生 candidate cluster。

這比一開始硬宣告：

$$
g_i\sim_{route}g_j
$$

更保守。

---

# 38. Semantic dedup pipeline

本文建議 proof-space observatory 使用以下流程：

```text
Raw Artifact Ingestion
        |
        v
Immutable Source + Hash
        |
        v
Surface Normalization
        |
        v
Statement / Assumption Extraction
        |
        v
Quantifier + Domain Signature
        |
        v
Candidate Retrieval
        |
        v
Structural Similarity
        |
        v
Formal Mutual Implication if Available
        |
        v
Route Graph Comparison
        |
        v
Obstruction Comparison
        |
        v
Equivalence Graph Update
        |
        v
Quotient Metrics
```

關鍵不是某一個模型。

而是：

$$
\boxed{
\text{cheap candidate generation}
\rightarrow
\text{expensive audited merge}.
}
$$

---

# 39. Candidate generation 可以大量使用 embedding

對 $N$ 篇 artifact 做全 pair：

$$
O(N^2)
$$

會快速昂貴。

因此先用：

$$
\operatorname{ANN}
$$

或 sparse lexical index 找：

$$
K\ll N
$$

個候選鄰居。

複雜度近似下降為：

$$
O(NK).
$$

embedding 在這裡很有價值。

但它的角色是：

$$
\boxed{
\text{retrieval}
}
$$

不是：

$$
\boxed{
\text{proof of equivalence}.
}
$$

---

# 40. 多觀察者 semantic audit

對重要 merge：

$$
g_i\leftrightarrow g_j,
$$

可以要求多個獨立 classifier：

$$
A_1,A_2,\ldots,A_m.
$$

每個輸出：

$$
E_{ij}^{(a)}.
$$

但：

$$
\text{majority vote}
$$

仍不是 formal proof。

因此多觀察者只提升：

$$
\text{audit confidence},
$$

不自動提升為：

$$
\mathcal A\vdash Q_i\leftrightarrow Q_j.
$$

---

# 41. Formal verifier 在商化中扮演什麼角色

若可以構造：

$$
Q_i\rightarrow Q_j
$$

與：

$$
Q_j\rightarrow Q_i
$$

並由 proof assistant 驗證，則命題等價證據最強。

但 formal verifier 仍依賴：

- theorem statement 是否 faithful；
- imported axioms；
- definitions；
- library versions；
- formalization correctness。

因此：

$$
\boxed{
\text{verified equivalence of formal statements}
}
$$

不自動等於：

$$
\boxed{
\text{perfect equivalence of original informal intentions}.
}
$$

provenance 必須把 informal-to-formal mapping 保留下來。

---

# 42. Semantic identity 與 historical identity 必須分開

兩篇論文可能數學上完全等價：

$$
g_i\sim_{prop}g_j,
$$

但在歷史上：

$$
t_i<t_j
$$

而 $g_j$ 是獨立重發現。

如果 destructive dedup，把 $g_j$ 刪掉，就會失去：

- independent rediscovery；
- convergence evidence；
- research dynamics；
- route attraction。

所以：

$$
\boxed{
\text{semantic quotient}
\neq
\text{historical quotient}.
}
$$

---

# 43. 重複有時本身就是訊號

若某個 class：

$$
c
$$

在沒有直接 copy 的情況下，被多條獨立路線重訪：

$$
m_{\mathrm{ind}}(c)\gg1,
$$

這可能表示：

- 這個 lemma 是 attractor；
- 這個 obstruction 是 basin boundary；
- 這個 representation 很自然；
- 這個局部 theorem 是高連接 hub。

因此 dedup 後不能只留下：

$$
c.
$$

還要留下：

$$
m(c),
\quad
m_{\mathrm{ind}}(c),
\quad
t_{first},
\quad
t_{revisit}.
$$

---

# 44. Independent rediscovery score

定義：

$$
\operatorname{IRS}(c)
=
\sum_{i\in q^{-1}(c)}
\chi_i,
$$

其中 $\chi_i$ 衡量該 artifact 相對既有 class 的資訊隔離程度，例如：

- 不同模型；
- 不同 prompt lineage；
- 不同方法族；
- 不同時間窗口；
- 未讀取前一結果。

若：

$$
\operatorname{IRS}(c)\gg1,
$$

表示同一結果被獨立重發現多次。

這與 copy multiplicity 完全不同。

---

# 45. Quotient-adjusted recurrence

定義某 class 的 revisit sequence：

$$
t_1<t_2<\cdots<t_m.
$$

定義 inter-revisit interval：

$$
\Delta t_k
=
t_{k+1}-t_k.
$$

若：

$$
\Delta t_k
$$

逐步縮短，可能表示研究路徑越來越被吸引回該 basin。

這是 LSI-PSD-04 與 06 可以研究的高階訊號。

---

# 46. 商空間與「符號先到盡」命題

本系列原始動機之一是：

> 大規模 AI 研究可能在最終證明出現前，先耗盡某個可見的符號／路徑語料。

若不 quotient，這個命題幾乎無法測試。

因為模型永遠可以：

$$
x\mapsto y
$$

換字，

$$
L_1\mapsto L_2
$$

換 lemma 名，

甚至重排章節。

raw novelty 永遠可以被人工製造。

只有在：

$$
\Omega/\sim
$$

上，才有可能問：

$$
\Delta N_{\mathrm{eff}}\rightarrow0?
$$

也就是：

$$
\boxed{
\text{表面還在生成，
但有效 equivalence class 不再增加嗎？}
}
$$

這才是「符號飽和」的可測版本。

---

# 47. 但「符號飽和」必須指定 quotient

不能說：

> 符號空間飽和了。

而應說：

$$
\text{在 relation }\sim_k
\text{ 與 regime }R
\text{ 下，}
$$

觀察到：

$$
\Delta
|\Omega_{N}/\sim_k|
\rightarrow0.
$$

例如：

$$
\Delta N_{route}\rightarrow0
$$

不代表：

$$
\Delta N_{prop}\rightarrow0.
$$

也不代表：

$$
\Delta N_{repr}\rightarrow0.
$$

所以 saturation 是 relation-dependent。

---

# 48. Quotient profile

本文提出：

$$
\boxed{
\mathbf Q_N
=
(
N_{raw},
N_{\alpha},
N_{def},
N_{prop},
N_{route},
N_{obs},
N_{evid}
).
}
$$

這稱為 quotient profile。

若：

$$
N_{raw}\gg N_{route},
$$

表示大量文字變體匯聚到少量 route family。

若：

$$
N_{route}\gg N_{obs},
$$

表示不同方法大量匯聚到少量 obstruction。

這正是 confluence 的前兆。

---

# 49. Quotient compression ratio

對 relation $k$ 定義：

$$
\operatorname{QCR}_k
=
\frac{N_{raw}}{N_k}.
$$

例如：

$$
\operatorname{QCR}_{route}=25
$$

表示平均每個 route class 對應 25 份 raw artifact。

若隨時間：

$$
\operatorname{QCR}_{route}(N)\uparrow,
$$

而：

$$
N_{route}
$$

增長變慢，這比文本重複更像 route saturation。

---

# 50. NS-203 案例應如何升級

前一輪 NS Proof-Space Sampling Observatory 主要仍以 paper-level artifact 和 heuristic concept family 為主。

本文提出第二輪需要：

$$
\boxed{
\text{Paper}
\rightarrow
\text{Claim}
\rightarrow
\text{Lemma}
\rightarrow
\text{Route}
\rightarrow
\text{Obstruction}.
}
$$

## 50.1 不應直接把 203 當有效樣本數

即使：

$$
N_{paper}=203,
$$

真正：

$$
N_{route},
\quad
N_{obs},
\quad
N_{prop}
$$

仍未知。

## 50.2 應先抽 canonical claim

每篇建立：

```text
paper_id
claim_ids
assumption_signature
route_signature
obstruction_ids
formal_status
dependency_ids
```

## 50.3 再建立 equivalence graph

特別檢測：

- 同一 claim 是否跨系列重現；
- 同一 route 是否換 notation 回訪；
- 不同 route 是否落同 obstruction；
- 同 proposition 是否因 representation 不同而 proof behavior 不同。

## 50.4 這樣才能真正測 X 階採樣

若一階 state 都沒 quotient，X 階採樣只是語言統計。

---

# 51. 對 Navier--Stokes 的認識論限制

即使未來得到：

$$
N_{raw}\gg N_{route},
$$

$$
N_{route}\gg N_{obs},
$$

且：

$$
\Delta N_{obs}\rightarrow0,
$$

仍只能說：

> 在目前研究制度、抽取法與 quotient 定義下，觀察到高度 recurrent obstruction structure。

不能推出：

$$
\text{Navier--Stokes 問題錯了}.
$$

不能推出：

$$
\text{不可證}.
$$

不能推出：

$$
\text{獨立}.
$$

不能推出：

$$
\text{全部 proof space 已耗盡}.
$$

這個 epistemic firewall 必須保留到 LSI-PSD-10。

---

# 52. 對 P/NP 的同樣限制

P/NP 更容易出現 representation trap，因為：

- machine model；
- reduction language；
- uniformity；
- circuit model；
- proof complexity；
- relativization；
- natural proofs；
- algebrization；

本來就存在多層 formulation。

因此若做類似 corpus：

$$
\Omega_{P/NP}^{raw},
$$

更必須把：

$$
\sim_{prop},
\quad
\sim_{route},
\quad
\sim_{barrier}
$$

分開。

不能把「又撞到 relativization-style barrier」簡化成：

> 所有方法都一樣。

---

# 53. 商空間對研究記憶的價值

沒有 quotient 的長期記憶：

$$
\mathcal K_N
$$

會越來越大。

但新增內容中可能大量是：

$$
\text{semantic duplicates}.
$$

結果：

- retrieval 變差；
- context 被重複佔據；
- agent 誤判 novelty；
- 相同路線被多次重開。

語義商化後：

$$
\mathcal K_N
\rightarrow
(
\bar{\mathcal K}_N,
\mathcal F_N
),
$$

其中：

- $\bar{\mathcal K}_N$：canonical class layer；
- $\mathcal F_N$：完整 source fibers。

這是一種：

$$
\boxed{
\text{lossless-at-source, compressed-at-navigation}
}
$$

架構。

---

# 54. 商空間對 AI prompt context 的價值

長上下文裡如果塞入：

$$
30
$$

篇本質同 route 的 paper，

AI 可能因頻率誤認：

> 這條 route 很有支持。

但那可能只是同一 source lineage 的重寫。

因此 context builder 應按：

$$
\text{class diversity}
$$

而不是：

$$
\text{artifact count}
$$

取樣。

可以定義：

$$
P(g_i\mid c)
=
\frac{1}{m(c)}
$$

作 class-balanced sampling。

---

# 55. 商空間對多 AI 研究的價值

如果十個 agent 同時工作，最常見浪費之一是：

$$
A_1,\ldots,A_{10}
$$

都進入同一 route basin。

若 observatory 有即時 quotient：

$$
[g_{A_1}]_{route}
=
[g_{A_2}]_{route}
=
\cdots,
$$

scheduler 可以把後續 agent 導向未覆蓋 class。

但不能完全禁止重訪。

因為 independent rediscovery 有驗證價值。

所以應設：

$$
\text{exploration quota}
+
\text{replication quota}.
$$

---

# 56. Exploration 與 replication 必須同時存在

如果只追求：

$$
\nu^{route}\uparrow,
$$

系統可能不再驗證舊結果。

如果只追求：

$$
m(c)\uparrow,
$$

系統會陷入重複。

因此資源配置：

$$
B
=
B_{explore}
+
B_{replicate}
+
B_{audit}.
$$

其中：

$$
B_{explore}
$$

追求新 class，

$$
B_{replicate}
$$

做獨立重現，

$$
B_{audit}
$$

驗證 merge / split。

---

# 57. Quotient-aware scheduler

可以定義 action score：

$$
S(a)
=
\alpha N(a)
+
\beta V(a)
+
\gamma D(a)
-
\delta R(a),
$$

其中：

- $N(a)$：預期 quotient novelty；
- $V(a)$：驗證價值；
- $D(a)$：diversity gain；
- $R(a)$：重複風險。

如果某 route class：

$$
m(c)\gg1
$$

且 independent evidence 已足夠，

則：

$$
R(a)\uparrow.
$$

scheduler 應偏向其他 basin。

---

# 58. 商空間錯誤本身也必須被版本化

今天系統可能判：

$$
g_i\sim_{route}g_j.
$$

未來發現一個 hidden assumption：

$$
A^\star
$$

後，必須拆分：

$$
[g]_{route}
\rightarrow
[g_i]_{route}
\cup
[g_j]_{route}.
$$

因此 equivalence class 不是不可修改真理。

它應有：

```text
class_version
merge_history
split_history
evidence_history
review_status
```

這使 quotient 本身也成為可審計研究對象。

---

# 59. Quotient provenance

每次 merge 記錄：

$$
M_t
=
(
c_i,
c_j,
k,
E,
A,
t
),
$$

其中：

- $c_i,c_j$：原 classes；
- $k$：relation type；
- $E$：證據；
- $A$：執行者／agent；
- $t$：時間。

每次 split：

$$
S_t
=
(
c,
\{c_1,\ldots,c_m\},
reason,
t
).
$$

這和版本控制一樣重要。

---

# 60. 不同 relation 需要不同 verifier

| Relation | 最低合理 verifier |
|---|---|
| $\sim_{lex}$ | deterministic normalization |
| $\sim_{\alpha}$ | binder-aware structural checker |
| $\sim_{def}$ | formal elaborator / definitional equality |
| $\sim_{prop}$ | mutual implication proof or strong formal evidence |
| $\sim_{route}$ | audited route graph mapping |
| $\sim_{obs}$ | canonical failure-condition audit |
| $\sim_{evid}$ | provenance + evidence dependency audit |

這個表顯示：

$$
\boxed{
\text{沒有一個 universal similarity score 能取代全部 relation}.
}
$$

---

# 61. LLM 在 quotient pipeline 中最適合的角色

LLM 很適合：

- semantic candidate retrieval；
- assumption extraction；
- route labeling；
- obstruction paraphrase clustering；
- graph alignment proposal；
- merge explanation；
- split hypothesis。

但 LLM 不應單獨作：

$$
\text{formal equivalence oracle}.
$$

比較合理：

$$
\boxed{
\text{LLM proposes}
\rightarrow
\text{formal / structural checker audits}
\rightarrow
\text{human or multi-agent review for high-risk cases}.
}
$$

---

# 62. 商空間與 theorem discovery

如果系統發現：

$$
g_1,\ldots,g_n
$$

表面完全不同，但：

$$
[g_1]_{route}
=
\cdots
=
[g_n]_{route},
$$

且它們跨不同 mathematical domains，

這可能反而揭露一個更一般 theorem schema。

也就是：

$$
\text{deduplication}
\rightarrow
\text{abstraction}.
$$

因此 quotient 不只是刪除重複。

它也可能生成：

$$
\boxed{
\text{higher-level theorem family}.
}
$$

---

# 63. 從等價類反推出 invariant

若一組 artifact：

$$
\{g_i\}_{i=1}^n
$$

被判定為 route-equivalent，

可以尋找：

$$
I(g_i)=I^\star
$$

的共同 invariant。

這個 $I^\star$ 可能是：

- proof motif；
- conserved quantity；
- compactness pattern；
- duality；
- monotonicity；
- obstruction form。

因此：

$$
\boxed{
\text{quotient class}
\rightarrow
\text{invariant mining}.
}
$$

這是從資料庫工程進入新數學的一條可能路。

---

# 64. 「越是真理越可能像廢話」與 quotient 的關係

如果大量不同表達：

$$
g_1,\ldots,g_n
$$

在高階 quotient 後都收斂到：

$$
[g]^\star,
$$

那表面複雜度：

$$
K_{surface}
$$

可以很大，

但核心描述長度：

$$
K_{core}
$$

可能很小。

形式上：

$$
K_{core}
\ll
K_{surface}.
$$

這正好提供本系列後續「真理—生成性反轉」的一個資訊論入口：

> 大量理論展開可能在 quotient 後收斂成極短核心，而極短核心又可以生成大量展開。

但本文暫不把這解讀為「真理必然簡單」。

這裡只建立可測結構。

---

# 65. Quotient 不等於 reductionism

把兩篇研究歸入同 route class，不代表：

> 它們所有意義都一樣。

商化只在指定 relation 下成立。

所以應寫：

$$
g_i\sim_{route}g_j,
$$

而不是：

$$
g_i=g_j.
$$

同樣：

$$
g_i\sim_{prop}g_j
$$

不表示其：

- 歷史意義；
- 教學價值；
- proof elegance；
- search difficulty；
- computational cost；

都相同。

---

# 66. 多商空間表示

最終一份 artifact 應同時有多個 identity：

$$
\operatorname{ID}(g_i)
=
(
[g_i]_{prop},
[g_i]_{route},
[g_i]_{obs},
[g_i]_{evid},
\rho_i
).
$$

這可以看成一個 product-like index：

$$
\mathcal I
=
\mathcal Q_{prop}
\times
\mathcal Q_{route}
\times
\mathcal Q_{obs}
\times
\mathcal Q_{evid}
\times
\mathcal R.
$$

不是所有組合都可達。

但這比單一 document ID 更接近研究身份。

---

# 67. Quotient lattice 的版本

可將不同 coarse-graining 寫成：

$$
\Omega^{raw}
\rightarrow
\Omega^{\alpha}
\rightarrow
\Omega^{def}
\rightarrow
\Omega^{prop}.
$$

另外：

$$
\Omega^{raw}
\rightarrow
\Omega^{route}
\rightarrow
\Omega^{obs}.
$$

這兩條不是同一條鏈。

可以畫成：

```text
              Ω_raw
             /     \
            v       v
      Ω_statement  Ω_route
         |            |
         v            v
       Ω_prop        Ω_obs
             \      /
              \    /
             meta-classes
```

這個 lattice structure 比單一 embedding cluster 更適合研究空間。

---

# 68. Quotient uncertainty 應進入 coverage error bar

如果 equivalence graph 中有大量：

$$
?
$$

邊，

則：

$$
N_{eff}
$$

不是一個確定值。

可以定義上下界：

$$
N_{\mathrm{eff}}^{-}
\leq
N_{\mathrm{eff}}
\leq
N_{\mathrm{eff}}^{+}.
$$

其中：

- 下界：把所有可能等價候選盡量合併；
- 上界：把未確定 pair 保守分開。

coverage 也應輸出：

$$
[\widetilde C^{-},\widetilde C^{+}].
$$

這比給出虛假的單點百分比更誠實。

---

# 69. 商空間審計的最小 benchmark

可建立 synthetic benchmark：

### 類型 A：純 $\alpha$ -rename

應被合併。

### 類型 B：定義展開

應在 definitional layer 合併。

### 類型 C：量詞交換

不應合併。

### 類型 D：假設減弱／加強

應標成 implication relation，不是 equivalence。

### 類型 E：同 theorem 不同 proof

proposition 合併，route 分開。

### 類型 F：不同 theorem 同 route skeleton

proposition 分開，route 合併。

### 類型 G：不同 route 同 obstruction

route 分開，obstruction 合併。

若系統連這七類都不能穩定區分，則不應用於 proof-space saturation claim。

---

# 70. 等價以外還需要 implication graph

很多研究產物不是：

$$
Q_i\leftrightarrow Q_j,
$$

而是：

$$
Q_i\Rightarrow Q_j.
$$

例如一個 stronger theorem：

$$
Q_s
$$

推出 weaker theorem：

$$
Q_w.
$$

若把兩者強行 quotient，會丟掉 theorem strength。

因此除了 equivalence graph：

$$
\mathcal E,
$$

還要有 implication DAG：

$$
\mathcal D_{imp}.
$$

這使研究空間不只有 class，還有 partial order。

---

# 71. Theorem strength lattice

若：

$$
Q_1\Rightarrow Q_2,
$$

$$
Q_2\not\Rightarrow Q_1,
$$

則：

$$
Q_1
$$

較強。

可定義：

$$
Q_1\succeq Q_2.
$$

這形成 theorem-strength preorder。

它對 dedup 非常重要，因為很多看似「重複」其實是：

- generalization；
- specialization；
- corollary；
- strengthening；
- weakening。

Rocq goal clone work 把 generalization 單獨分類，正好提醒這一點。

---

# 72. 「同一條路」也可能存在強弱關係

Route A：

$$
A
\rightarrow
L
\rightarrow
C.
$$

Route B：

$$
A
\rightarrow
L'
\rightarrow
L
\rightarrow
C.
$$

若 $L'$ 只是更一般的 bridge，

兩 route 不必完全 equivalence。

可以有：

$$
R_A\preceq R_B.
$$

因此 route space 也可以具有 refinement order。

這將在後續 proof-route dynamics 中很有用。

---

# 73. Quotient-aware novelty decay

原始 novelty decay：

$$
\nu_N^{raw}\rightarrow0
$$

可能只是文本變得相似。

真正有意思的是：

$$
\nu_N^{prop}\rightarrow0,
$$

$$
\nu_N^{route}\rightarrow0,
$$

$$
\nu_N^{obs}\rightarrow0.
$$

如果三者發生在不同時間：

$$
T_{prop}
<
T_{route}
<
T_{obs},
$$

就表示不同層次的 saturation phase transition。

這直接預告 LSI-PSD-04 與 05。

---

# 74. Quotient phase diagram

可以建立：

$$
\mathbf Z_N
=
(
\Delta N_{prop},
\Delta N_{route},
\Delta N_{obs},
\operatorname{RSI},
H_{route}
).
$$

不同區域代表：

### Phase A：新命題、新路線

$$
\Delta N_{prop}>0,
\quad
\Delta N_{route}>0.
$$

### Phase B：命題重訪、路線創新

$$
\Delta N_{prop}\approx0,
\quad
\Delta N_{route}>0.
$$

### Phase C：路線重訪、障礙創新

$$
\Delta N_{route}\approx0,
\quad
\Delta N_{obs}>0.
$$

### Phase D：高度 confluence

$$
\Delta N_{route}\approx0,
\quad
\Delta N_{obs}\approx0,
\quad
m(c)\uparrow.
$$

這比「文章越來越像」精確得多。

---

# 75. 商空間與 local basin

假設 route quotient 得到：

$$
\mathcal C_{route}.
$$

再以 transition / dependency 連接 classes：

$$
\mathcal G_{route}.
$$

高密度子圖：

$$
B_k
\subset
\mathcal G_{route}
$$

可以作為 proof basin 候選。

這樣 LSI-PSD-05 的 local saturation 就有一個乾淨的底層：

$$
\text{basin}
=
\text{quotient-aware route subgraph}.
$$

沒有 quotient，basin 密度可能只是 duplicate density。

---

# 76. 商空間與 obstruction confluence

若：

$$
R_1,R_2,\ldots,R_m
$$

在 route quotient 下彼此不同：

$$
[R_i]_{route}\neq[R_j]_{route},
$$

但：

$$
[O(R_i)]_{obs}
=
[O^\star]_{obs},
$$

則才真正構成：

$$
\boxed{
\text{obstruction confluence}.
}
$$

如果 route 本身其實都是同一條，只是換 notation，那不能叫 confluence。

所以 LSI-PSD-06 完全依賴本文。

---

# 77. 商空間與 productive mis-specification

後續 LSI-PSD-08 / 09 會研究：

$$
\text{parent framing}
\rightarrow
\text{descendant theories}.
$$

若 descendant corpus 不 quotient，就會高估 generativity。

真正的 generativity 應計：

$$
G_{eff}
=
|\{[T_i]_{prop}\}|
$$

或更強：

$$
G_{route},
\quad
G_{transfer}.
$$

因此「錯誤問題很會生理論」也必須先去除表面重複。

---

# 78. 研究系統的 canonical record

本文建議最小 schema：

```yaml
artifact_id: ...
source_hash: ...
parent_artifacts: [...]
statement:
  raw: ...
  formal: ...
quantifiers: [...]
domains: [...]
assumptions: [...]
claims: [...]
dependencies: [...]
route:
  nodes: [...]
  edges: [...]
obstructions: [...]
evidence: [...]
verification:
  status: ...
  tool: ...
representation:
  language: ...
  library: ...
  notation_profile: ...
equivalence:
  proposition_class: ...
  route_class: ...
  obstruction_class: ...
  unresolved_links: [...]
provenance:
  created_at: ...
  agent: ...
  lineage: ...
```

這不是論文本身。

它是 observatory 的導航層。

---

# 79. Canonical record 不可取代原始 source

永遠保持：

$$
F(g)\neq g.
$$

feature record：

$$
F(g)
$$

用來：

- 搜尋；
- graph；
- quotient；
- metrics。

原始 source：

$$
g
$$

用來：

- audit；
- reconstruction；
- citation；
- re-extraction。

這與 canonical source policy 完全一致。

---

# 80. 商空間的工程複雜度

全 pair comparison：

$$
\binom{N}{2}
=
O(N^2).
$$

當：

$$
N=10^5,
$$

不可直接對每 pair 做 formal equivalence proof。

因此採分層：

$$
O(N\log N)
$$

級 retrieval，

加上：

$$
O(NK)
$$

候選 pair，

再對少數高風險 pair 做昂貴 audit。

工程上：

$$
\boxed{
\text{cheap broad filter}
+
\text{expensive narrow verifier}.
}
$$

---

# 81. 風險分層

## 81.1 低風險 merge

- exact hash；
- deterministic whitespace；
- certified $\alpha$ -equivalence。

可以自動。

## 81.2 中風險 merge

- definitional equality；
- structural canonicalization；
- obvious corollary mapping。

需要 formal tool。

## 81.3 高風險 merge

- natural-language semantic equivalence；
- route equivalence；
- obstruction equivalence；
- cross-domain theorem schema。

需要 audit，不能自動 destructive merge。

---

# 82. Falsification protocol

本文框架可以被實證挑戰。

若未來發現：

1. quotient correction 幾乎不改變任何 long-horizon novelty statistics；
2. representation sensitivity 在成熟 prover 上消失；
3. route equivalence 無法可靠抽取；
4. obstruction classes 不具跨 artifact 穩定性；
5. quotient-aware scheduler 不比 raw retrieval 降低重複；

那麼本文對 proof-space science 的實用價值應被下修。

這些都是可測的。

---

# 83. 實驗假說一：Raw novelty 會系統性高估 route novelty

提出：

$$
H_1:
\mathbb E[\nu^{raw}]
>
\mathbb E[\nu^{route}]
$$

在長程生成 corpus 後期成立。

這不是數學定理。

它是 corpus-level hypothesis。

---

# 84. 實驗假說二：表示敏感性在 LLM prover 中非零

提出：

$$
H_2:
\operatorname{RSI}(Q;R)>0
$$

對相當比例 theorem class 成立。

現有 representation-symmetry 研究已提供直接外部支持，但具體值依 prover 與 benchmark 而變。

---

# 85. 實驗假說三：Obstruction class 數量會比 route class 更早顯示收斂

在高難度長程問題中，可能：

$$
N_{obs}
\ll
N_{route}.
$$

如果很多不同 route 都撞少數障礙，就會：

$$
\operatorname{QCR}_{obs}
\gg
\operatorname{QCR}_{route}.
$$

這是 confluence-rich regime 的一個可測 signature。

---

# 86. 實驗假說四：Quotient-aware memory 會降低無效重複

比較：

$$
R_{raw}
$$

與：

$$
R_{quot}.
$$

若：

$$
\operatorname{DuplicateRate}(R_{quot})
<
\operatorname{DuplicateRate}(R_{raw})
$$

且：

$$
\operatorname{VerifiedNovelty}(R_{quot})
\geq
\operatorname{VerifiedNovelty}(R_{raw}),
$$

則 quotient-aware research memory 有工程價值。

---

# 87. 實驗假說五：保留 representation fibers 會提高 search robustness

若對同一 proposition class 保存多個 representation：

$$
\rho_1,\ldots,\rho_m,
$$

並在 test time 做 representation ensemble，

可能提高：

$$
P(\operatorname{success}).
$$

這與 symmetry aggregation 的既有研究方向一致。

因此正確 quotient 不是把表示刪掉。

而是：

$$
\boxed{
\text{把表示掛到同一數學身份下面}.
}
$$

---

# 88. 十個核心命題

## 命題一：Raw Count Non-Identity

$$
\boxed{
N_{raw}
\neq
N_{semantic}.
}
$$

## 命題二：Similarity Non-Equivalence

$$
\boxed{
\operatorname{Sim}(g_i,g_j)\uparrow
\not\Rightarrow
g_i\sim_{prop}g_j.
}
$$

## 命題三：Mathematical/Search Identity Separation

$$
\boxed{
g_i\sim_{prop}g_j
\not\Rightarrow
\sigma_i=\sigma_j.
}
$$

## 命題四：Representation Sensitivity

$$
\boxed{
\operatorname{RSI}>0
}
$$

可使數學冗餘表示保有搜尋價值。

## 命題五：Evidence Preservation

$$
\boxed{
[g_i]_{claim}=[g_j]_{claim}
\not\Rightarrow
[E_i]=[E_j].
}
$$

## 命題六：Non-Premature Quotient

$$
\boxed{
\text{先保存可重建差異，再商化}.
}
$$

## 命題七：Quotient-Dependent Saturation

$$
\boxed{
\text{Saturation}
=
\text{relation-dependent}.
}
$$

## 命題八：Higher-Order Dependence

$$
\boxed{
\text{高階採樣量測依賴低階 quotient discipline}.
}
$$

## 命題九：Confluence Requires Distinct Routes

$$
\boxed{
\text{同 obstruction 的多次出現}
\neq
\text{confluence}
}
$$

除非來源 route 在適當 quotient 下確實不同。

## 命題十：Quotient Is an Index Layer

$$
\boxed{
\text{quotient}
\neq
\text{destructive deletion}.
}
$$

---

# 89. 符號表

| 符號 | 意義 |
|---|---|
| $\Omega_R^{raw}(Q)$ | 原始研究產物空間 |
| $\sim_{lex}$ | 字面／表面規範化等價 |
| $\sim_{\alpha}$ | 變數重命名等價 |
| $\sim_{def}$ | 定義展開等價 |
| $\sim_{prop}$ | 背景理論下命題等價 |
| $\sim_{route}$ | proof-route skeleton 等價 |
| $\sim_{obs}$ | obstruction family 等價 |
| $\sim_{evid}$ | evidence 等價 |
| $\Omega_R^{math}$ | 數學命題商空間 |
| $\Omega_R^{search}$ | 保留 representation 的搜尋狀態空間 |
| $\Gamma_i$ | route graph |
| $\operatorname{RSI}$ | Representation Sensitivity Index |
| $m(c)$ | equivalence class multiplicity |
| $N_{\mathrm{eff}}$ | 有效樣本數 |
| $\operatorname{SRR}$ | Semantic Redundancy Ratio |
| $\operatorname{QCR}$ | Quotient Compression Ratio |
| $H_{route}$ | route-family entropy |
| $\boldsymbol\nu_i$ | 多層 novelty vector |
| $\mathcal E$ | equivalence graph |
| $\mathcal D_{imp}$ | implication graph |
| $\operatorname{IRS}$ | independent rediscovery score |

---

# 90. 與前兩篇的依賴

**依賴：**

- LSI-PSD-01：定義研究制度、proof-space 與 epistemic firewall；
- LSI-PSD-02：定義 logic-space integration、coverage vector、local basin 與 marginal research yield。

本文對 LSI-PSD-02 做一個必要修正：

$$
\boxed{
\text{所有 coverage 與 novelty 指標，都必須說明其 quotient policy}.
}
$$

否則：

$$
\text{coverage}
$$

可能只是：

$$
\text{text proliferation}.
$$

---

# 91. 對後續系列的依賴

LSI-PSD-04 將使用本文的：

$$
\Omega/\sim
$$

建立：

$$
\Omega^{(0)},
\Omega^{(1)},
\Omega^{(2)},\ldots
$$

高階 proof-space sampling。

LSI-PSD-05 將把 quotient-aware route graph 分解為 local basins。

LSI-PSD-06 將在：

$$
\sim_{route}
$$

與：

$$
\sim_{obs}
$$

上正式定義 obstruction confluence。

LSI-PSD-07 至 09 會用：

$$
N_{\mathrm{eff}}
$$

與 descendant quotient，避免把表面理論數量誤認成 generativity。

LSI-PSD-12 將把本文 schema 實作成 Proof-Space Observatory 的 equivalence registry。

---

# 92. 結論：研究空間的第一個問題不是「有多少」，而是「哪些其實是同一個」

AI 可以很便宜地生成：

$$
10^2,
\quad
10^3,
\quad
10^4
$$

份數學研究稿。

但 raw count 只告訴我們：

$$
\text{有多少檔案}.
$$

它沒有告訴我們：

$$
\text{有多少命題},
$$

$$
\text{有多少 proof routes},
$$

$$
\text{有多少 obstruction},
$$

$$
\text{有多少獨立 evidence}.
$$

因此長程 AI 數學研究的第一個統計修正，不是再加一個更漂亮的 embedding。

而是建立：

$$
\boxed{
\textbf{Semantic Quotient Space}.
}
$$

本文的核心不是主張所有重複都該刪除。

恰恰相反。

它主張同一 artifact 必須同時被看成：

$$
\text{mathematical object}
$$

與：

$$
\text{search event}.
$$

在數學層：

$$
Q_i\sim_{prop}Q_j
$$

可以被視為同一命題類。

在搜尋層：

$$
(Q_i,\rho_i)
$$

與：

$$
(Q_j,\rho_j)
$$

仍可能是不同實驗條件。

因此最終架構不是：

$$
\text{deduplicate everything}.
$$

而是：

$$
\boxed{
\text{quotient what is mathematically redundant,
preserve what is dynamically informative,
and keep every source reconstructable}.
}
$$

這使 proof-space science 能夠第一次回答：

> 一萬篇論文裡，到底有多少是真的新數學狀態？多少只是同一狀態的不同表示？多少是同一命題的不同 proof route？多少不同 route 最後又撞上同一 obstruction？哪些重複是浪費，哪些重複反而是獨立驗證或搜尋對稱性資訊？

沒有這層，後續的「二階、三階、X 階採樣」「局部飽和」「障礙匯流」「真理—生成性反轉」都可能只是文字統計的幻覺。

有了這層，研究 corpus 才開始從：

$$
\text{document pile}
$$

轉成：

$$
\boxed{
\text{auditable quotient-aware proof-space memory}.
}
$$

---

# 參考文獻

1. Olejniczak, K., Dimitrov, R., Huang, X., Cuenca Grau, B., Kim, J., Ceylan, İ. İ. **What are the Right Symmetries for Formal Theorem Proving?** arXiv:2605.22257 (2026). https://arxiv.org/abs/2605.22257
2. Ghanbari, A. **Automatic Goal Clone Detection in Rocq.** *39th European Conference on Object-Oriented Programming (ECOOP 2025)*, LIPIcs 333, 12:1--12:19. DOI: 10.4230/LIPIcs.ECOOP.2025.12. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2025.12
3. Liu, X., Zhu, T., Dong, Z., Liu, Y., Guo, Q., Liu, Z., Chen, Y., Luo, T. **ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity.** arXiv:2509.22246 (2025; accepted ICLR 2026). https://arxiv.org/abs/2509.22246
4. Liu, Y., Zhu, T., Liu, X., Chen, Y., Liu, Z., Guo, Q., Zhang, J., Bao, K., Luo, T. **Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization.** arXiv:2507.07399 (2025). https://arxiv.org/abs/2507.07399
5. Kripner, M., Šustr, M., Straka, M. **LeanTree: Accelerating White-Box Proof Search with Factorized States in Lean 4.** arXiv:2507.14722 (2025). https://arxiv.org/abs/2507.14722
6. Li, X. et al. **ProofGym: Unifying LLM-Based Theorem Proving Across Formal Systems.** MATH-AI Workshop at NeurIPS 2025. https://neurips.cc/virtual/2025/131121
7. Hubert, T. et al. **Olympiad-level formal mathematical reasoning with reinforcement learning.** *Nature* (2025). https://www.nature.com/articles/s41586-025-09833-y
8. Qian, Y., Clune, J., Barrett, C., Avigad, J. **Lean-auto: An Interface between Lean 4 and Automated Theorem Provers.** CAV 2025; arXiv:2505.14929. https://arxiv.org/abs/2505.14929
9. Dong, K., Ma, T. **STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving.** *Proceedings of ICML 2025*, PMLR 267. https://proceedings.mlr.press/v267/dong25h.html
10. **ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings.** arXiv:2510.15681 (2025). https://arxiv.org/abs/2510.15681
11. **Minif2f in Rocq: Automatic Translation Between Proof Assistants — A Case Study.** MATH-AI 2025, OpenReview. https://openreview.net/forum?id=wkELXtGZa6
12. Stanford Encyclopedia of Philosophy. **Automated Reasoning.** Summer 2025 Edition. https://plato.stanford.edu/archives/sum2025/entries/reasoning-automated/

---

# 版本與非主張

## 本文主張

- 大規模 AI 數學 corpus 的 raw artifact count 不能直接視為 proof-space sample count。
- 字串相似、結構相似、命題等價、route 等價與 obstruction 等價必須分離。
- 數學身份與搜尋身份不同；數學上等價的表示仍可能對 prover 具有不同搜尋難度。
- embedding 與 LLM semantic judgment 適合作 candidate generation，不應單獨作 equivalence proof。
- quotient 必須保留 source fiber、evidence 與 provenance。
- saturation、novelty、coverage 都必須標示使用哪一層 quotient。
- high-order proof-space sampling 需要 lower-order quotient discipline。

## 本文不主張

1. 已存在一個對所有數學語料通用且完備的語義等價判定器；
2. embedding 相似度可替代形式互推證明；
3. route graph similarity 自動構成數學 equivalence relation；
4. 所有表示差異都應被刪除；
5. 所有重複都是浪費；
6. 同一 proposition 的不同 proof 沒有研究價值；
7. NS-203 的 203 篇已被本文正式壓縮成確定數量的 route classes；
8. quotient class 數量可以直接除以某個未知 proof-space denominator；
9. representation sensitivity 證明了任何公開未解問題被「錯誤表述」；
10. 本文已建立全域可計算的 mathematical canonical form。

---

**END OF LSI-PSD-03 v2.0 Expanded Edition**
