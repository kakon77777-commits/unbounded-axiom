# T 是 T，T 不是 T  
## 多重同一性符號學與符號身份動力學的初步框架

**英文題名：**  
*When T Is T and Is Not T: A Preliminary Framework for Multi-Identity Semiotics and Symbolic Identity Dynamics*

**系列：**《T 的九問：符號身份、生成、命名與持續》Paper 01  
**版本：** v0.1 理論草稿  
**日期：** 2026 年 8 月 12 日  
**作者：** Neo.K、Aletheia（AI 協作）  
**機構：** EveMissLab／一言諾科技有限公司

---

## 摘要

本文從一組看似自相矛盾的符號命題出發：

\[
T\text{ 是 }T,
\]

\[
T\text{ 不是 }T,
\]

\[
T\text{ 又是 }T,
\]

以及：

\[
T\text{ 是不是 }T？
\]

若將 \(T\) 僅理解為形式邏輯中的單一對象，則 \(T=T\) 只是同一律，而 \(T\neq T\) 顯然不能在同一對象、同一關係、同一時刻與同一語境下同時成立。

然而，實際符號系統中的「同一」往往不是單一關係。

兩個可見上完全相同的 \(T\)，可以：

- 屬於同一字元類型；
- 是兩個不同 token；
- 具有不同底層位元狀態；
- 指向不同對象；
- 承載不同語義；
- 執行不同算子；
- 具有不同命名歷史；
- 位於不同 namespace；
- 出現在不同時間；
- 被不同主體以不同判準重新識別。

反之，一個跨時間持續存在的符號身份，即使其字形、媒介、編碼或語義外觀發生改變，也可能仍被某套制度、歷史鏈或身份不變量判定為「同一個符號」。

本文因此提出**多重同一性符號學**（Multi-Identity Semiotics, MIS）與**符號身份動力學**（Symbolic Identity Dynamics, SID）的初步框架。其核心反轉為：

\[
\boxed{
\operatorname{Same}(T_i,T_j)
}
\]

通常不是充分定義的命題。

更完整的形式應為：

\[
\boxed{
\operatorname{Same}
\left(
T_i,T_j
\mid
\alpha,A,c,t
\right)
}
\]

其中：

- \(\alpha\)：採用的身份判準；
- \(A\)：進行判定的主體或系統；
- \(c\)：語境、任務與 namespace；
- \(t\)：時間與歷史位置。

因此：

\[
T_i=T_j
\]

與：

\[
T_i\neq T_j
\]

可以在**不同身份關係**下同時成立，而不構成形式邏輯上的直接矛盾。

本文進一步提出符號身份向量、身份投影、身份證書、身份斷裂與身份恢復等概念，並以極端單符號序列：

\[
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
\]

展示一項新的符號學命題：

\[
\boxed{
\text{可見符號熵趨近於零}
\not\Rightarrow
\text{潛在身份熵趨近於零}.
}
\]

這使符號研究從「這個符號代表什麼」進一步進入：

> **究竟依靠哪些關係、歷史、不變量與判定程序，我們仍有資格稱某個存在為同一個 \(T\)？**

**關鍵詞：** 符號身份、多重同一性、符號動力學、type/token、命名、指涉、身份持續、同形異態、單符號宇宙、身份熵

---

# 0. 研究邊界

本文不主張：

1. 傳統邏輯中的同一律 \(T=T\) 有問題；
2. 同一個對象可以在完全相同條件下同時滿足 \(T=T\) 與 \(T\neq T\)；
3. 所有身份問題都是相對的；
4. 只要改變觀察者，就可以任意宣告任何兩個對象相同；
5. 所有符號身份都必須包含本文列出的所有維度；
6. type/token distinction 已足以處理本文所有問題；
7. 名稱可以單獨決定對象的本體身份；
8. 語義相同必然表示符號身份相同；
9. 本文已提供一套完成的身份邏輯。

本文真正研究的是：

> 當「相同」一詞被同時用來指稱字形相同、類型相同、token 相同、狀態相同、所指相同、名稱相同、歷史相同與跨時間身份持續時，我們如何避免把不同的同一性關係壓縮成一個未標記的等號？

---

# 1. 問題的起點：兩個 T 到底有幾個 T？

考慮：

\[
T\qquad T.
\]

如果問：

> 這裡有幾個 \(T\)？

至少存在兩個合理答案。

若計算 type，可以說只有一種字母：

\[
|\mathcal T_{\mathrm{type}}|=1.
\]

若計算具體出現：

\[
|\mathcal T_{\mathrm{token}}|=2.
\]

type/token distinction 正是用來區分一個可重複類型與其具體 instances；Peirce 的相關討論也是現代 type/token 區分的重要歷史來源。當同一詞被多次寫出時，type 數量與 token 數量可以不同。

因此：

\[
\boxed{
\text{One Type}
\not\Rightarrow
\text{One Token}.
}
\]

這是本文的最低階起點。

但本文的問題不止於此。

因為即使已經區分：

\[
T_{\mathrm{type}}
\]

與：

\[
T_{\mathrm{token}},
\]

我們仍然不知道：

- 兩個 token 是否具有同一所指；
- 是否由同一命名制度產生；
- 是否執行同一操作；
- 是否來自同一歷史物件；
- 是否只是被顯示系統投影成同一字形；
- 是否在時間中維持同一身份；
- 是否被不同主體視為同一對象。

因此：

\[
\boxed{
\text{Type/Token}
}
\]

只是多重身份問題中的一條座標軸，而不是完整答案。

---

# 2. 第一反轉：沒有索引的「相同」是不完整的

我們通常寫：

\[
T_i=T_j.
\]

但在符號身份問題中，真正缺失的是：

> **在哪一種關係下相同？**

因此本文定義一族同一性關係：

\[
\mathfrak E
=
\{
\equiv_G,
\equiv_{\tau},
\equiv_X,
\equiv_R,
\equiv_N,
\equiv_O,
\equiv_H,
\equiv_C,
\equiv_T,
\ldots
\}.
\]

其中：

\[
T_i\equiv_G T_j
\]

表示 glyph identity；

\[
T_i\equiv_{\tau}T_j
\]

表示 type identity；

\[
T_i\equiv_XT_j
\]

表示 state identity；

\[
T_i\equiv_RT_j
\]

表示 referential identity；

\[
T_i\equiv_NT_j
\]

表示 naming identity；

\[
T_i\equiv_OT_j
\]

表示 operational identity；

\[
T_i\equiv_HT_j
\]

表示 historical identity。

因此更完整的身份命題不是：

\[
T_i=T_j,
\]

而是：

\[
\boxed{
T_i\equiv_\alpha T_j.
}
\]

---

# 3. 身份索引原理

本文提出：

## 原理 1：Identity Indexing Principle

在涉及符號、語言、命名、表示、歷史或動態身份的問題中，任何：

\[
x=y
\]

都應允許展開成：

\[
\boxed{
x
\equiv_{\alpha,A,c,t}
y.
}
\]

其中：

- \(\alpha\)：identity criterion；
- \(A\)：observer / judge；
- \(c\)：context；
- \(t\)：historical time。

換句話說：

\[
\boxed{
\text{Same}
\rightarrow
\text{Same Under What Relation?}
}
\]

這並不是否定絕對數學等號。

它只是指出：

> 自然語言中的「是同一個」往往把數種不同身份判準壓縮進同一語句。

---

# 4. T 是 T

現在重新閱讀：

\[
T=T.
\]

最純形式下，它表達：

\[
\forall x,\quad x=x.
\]

沒有問題。

但如果紙面上真正存在：

\[
T_1\qquad T_2,
\]

我們說：

> 「它們都是 T。」

更準確的形式其實可能是：

\[
T_1\equiv_{\tau}T_2
\]

以及：

\[
T_1\equiv_GT_2,
\]

同時：

\[
T_1\neq_{\mathrm{token}}T_2.
\]

因此：

\[
\boxed{
T\text{ 是 }T
}
\]

可能實際表示：

> 不同 token 被歸類到同一 type。

這不是哲學玄學，而是最基本的 identity criterion 切換。

---

# 5. T 不是 T

接著：

\[
T_1=T,\qquad T_2=T.
\]

若：

\[
G(T_1)=G(T_2)=T,
\]

但：

\[
X(T_1)\neq X(T_2),
\]

則：

\[
T_1
\equiv_G
T_2
\]

卻：

\[
T_1
\not\equiv_X
T_2.
\]

因此：

\[
\boxed{
T\text{ 不是 }T
}
\]

不需要解釋成：

\[
T\neq T.
\]

真正形式是：

\[
\boxed{
T_i
\equiv_{\alpha}
T_j
\land
T_i
\not\equiv_{\beta}
T_j,
\qquad
\alpha\neq\beta.
}
\]

本文稱此現象為：

# 多重同一性分岔  
## Multi-Identity Divergence

---

# 6. 同形異態只是第一層

此前的單符號研究可以表示為：

\[
x_i\neq x_j
\]

但：

\[
\Pi(x_i)=\Pi(x_j)=T.
\]

於是：

\[
\boxed{
\text{Same Glyph}
\not\Rightarrow
\text{Same State}.
}
\]

然而，多重同一性框架進一步指出：

\[
\text{State}
\]

也不是最後一層。

即使：

\[
X(T_i)=X(T_j),
\]

仍可能：

\[
R(T_i)\neq R(T_j),
\]

或：

\[
H(T_i)\neq H(T_j),
\]

或：

\[
O(T_i)\neq O(T_j).
\]

所以：

\[
\boxed{
\text{Same State}
\not\Rightarrow
\text{Same Referential Identity}
}
\]

以及：

\[
\boxed{
\text{Same State}
\not\Rightarrow
\text{Same Historical Identity}.
}
\]

「T 不是 T」因此不是一條技巧，而是一整個身份空間。

---

# 7. 符號身份向量

定義一次具體符號存在：

\[
\boxed{
\mathfrak T_i
=
(
\tau_i,
g_i,
x_i,
r_i,
n_i,
o_i,
h_i,
c_i,
t_i
)
}
\]

其中：

- \(\tau_i\)：type；
- \(g_i\)：glyph；
- \(x_i\)：internal state；
- \(r_i\)：referent；
- \(n_i\)：naming state / naming history；
- \(o_i\)：operator / function；
- \(h_i\)：historical provenance；
- \(c_i\)：context / namespace；
- \(t_i\)：time。

我們可以寫：

\[
\mathbf I(T_i)
=
(
I_\tau,
I_G,
I_X,
I_R,
I_N,
I_O,
I_H,
I_C,
I_T
).
\]

這稱為：

# Identity Profile

它不是單一數字。

而是一個多維身份組態。

---

# 8. 身份距離

若需要比較兩個 \(T\)，可以定義：

\[
d_\alpha(T_i,T_j)
\]

表示在身份維度 \(\alpha\) 上的差距。

更一般：

\[
\boxed{
\mathbf d_I(T_i,T_j)
=
(
d_G,
d_\tau,
d_X,
d_R,
d_N,
d_O,
d_H,
d_C,
d_T
).
}
\]

因此可能：

\[
d_G=0
\]

但：

\[
d_R\gg0.
\]

或者：

\[
d_G>0
\]

而：

\[
d_H=0.
\]

這意味著：

> 兩個對象「有多相同」並不是一條天然的一維軸。

---

# 9. Frege 問題的重新嵌入

Frege 對 identity statement 的著名問題之一，是：

\[
a=a
\]

與：

\[
a=b
\]

即使最後涉及同一 denotation，其認知價值仍可能不同；這促成 sense 與 reference 的區分。

本框架可以把這個問題重新寫成：

\[
R(a)=R(b)
\]

但：

\[
N(a)\neq N(b)
\]

或：

\[
S(a)\neq S(b),
\]

其中 \(S\) 表示認知進入路徑或 sense-like structure。

所以：

\[
\boxed{
\text{Same Referent}
\not\Rightarrow
\text{Same Cognitive Route}.
}
\]

本文不是要取代 Frege。

而是把這種差異嵌入更一般的 identity profile：

\[
\mathbf I(a)
\neq
\mathbf I(b)
\]

即使：

\[
a\equiv_R b.
\]

---

# 10. Peirce 三元結構與身份判定

Peirce 的符號論強調 sign、object 與 interpretant 的三元結構；符號的意義並不是單純 sign 與 object 之間的二元連線，而與 interpretation 密切相關。

這對本文非常重要。

因為：

\[
T_i\equiv_R T_j
\]

並不必然推出：

\[
J_A(T_i)=J_B(T_j).
\]

也就是：

> 同樣的 sign-object 關係，不保證不同 interpretant 產生相同身份判定。

因此身份判定器必須包含主體：

\[
\boxed{
J_A
(
T_i,T_j
\mid
\alpha,c,t
).
}
\]

---

# 11. T 是不是 T？

現在問題從本體陳述轉成判定：

\[
\boxed{
T_i\stackrel{?}{\equiv}_\alpha T_j.
}
\]

傳統最簡答案為：

\[
J\in\{0,1\}.
\]

但對多重身份問題，本文提出最低四值輸出：

\[
\boxed{
J
\in
\{
\mathrm{Same},
\mathrm{Different},
\mathrm{Both},
\mathrm{Underdetermined}
\}.
}
\]

其中 `Both` 不是說：

\[
T=T
\land
T\neq T
\]

在同一關係下成立。

而是：

\[
\exists\alpha,\beta:
\quad
T_i\equiv_\alpha T_j
\land
T_i\not\equiv_\beta T_j.
\]

例如：

\[
J_G(T_1,T_2)=\mathrm{Same},
\]

而：

\[
J_{\mathrm{token}}(T_1,T_2)
=
\mathrm{Different}.
\]

如果只問：

> 它們一不一樣？

卻不給 \(\alpha\)，則：

\[
\boxed{
J=\mathrm{Underdetermined}.
}
\]

---

# 12. 身份判準本身也是系統的一部分

傳統問題常將 identity criterion 當成透明背景。

本文把它提升成顯式對象：

\[
\alpha
=
(
\mathcal I,
\mathcal R,
\theta,
\mathcal P
).
\]

其中：

- \(\mathcal I\)：需要比較的不變量；
- \(\mathcal R\)：允許的變換；
- \(\theta\)：判定閾值；
- \(\mathcal P\)：證據與驗證程序。

所以：

\[
\boxed{
\text{Identity Judgment}
=
\text{Object Comparison}
+
\text{Criterion Selection}.
}
\]

---

# 13. T 為什麼是 T？

現在問題變成：

> 為什麼我們有資格做這個身份判定？

定義：

# Identity Grounding Certificate

\[
\boxed{
\mathcal G_\alpha(T)
=
(
\mathcal I,
P,
H,
N,
R,
V
)
}
\]

其中：

- \(\mathcal I\)：身份不變量；
- \(P\)：provenance；
- \(H\)：history；
- \(N\)：naming chain；
- \(R\)：關係證據；
- \(V\)：validation procedure。

於是：

\[
T_i\equiv_\alpha T_j
\]

不只是輸出一個 `TRUE`。

系統還應該能回答：

\[
\boxed{
\operatorname{WhySame}
(T_i,T_j,\alpha)?
}
\]

---

# 14. T 怎麼變成 T？

身份也可能是生成結果。

設某個未分類對象：

\[
x_0.
\]

經歷：

\[
x_0
\xrightarrow{F_1}
x_1
\xrightarrow{F_2}
x_2
\rightarrow\cdots
\rightarrow
x_n.
\]

某個系統在 \(x_n\) 上建立：

\[
\operatorname{Classify}(x_n)=T.
\]

於是：

\[
\boxed{
x
\rightarrow
T
}
\]

不是邏輯等號。

而是：

# Identity Acquisition

因此：

\[
\boxed{
\text{Be-T}
}
\]

與：

\[
\boxed{
\text{Become-T}
}
\]

必須區分。

---

# 15. T 怎麼被稱為 T？

「成為」與「被稱為」仍然不同。

令：

\[
N_A(x,c,t)=T
\]

表示主體 \(A\) 在語境 \(c\)、時間 \(t\) 將 \(x\) 命名為 \(T\)。

完全可能：

\[
x\in\mathcal T
\]

但：

\[
N_A(x)\neq T.
\]

也可能：

\[
x\notin\mathcal T
\]

卻：

\[
N_A(x)=T.
\]

所以：

\[
\boxed{
\text{Being T}
\neq
\text{Being Called T}.
}
\]

名稱理論中對 rigid designation 的討論也明確區分名稱如何持續指涉某個對象與描述性條件；rigid designator 的核心概念是，在相關可能世界中持續指定同一對象。

本文則進一步把問題放進歷史與多身份空間：

\[
\boxed{
\text{Name Continuity}
\neq
\text{Complete Identity}.
}
\]

---

# 16. 命名不是貼標籤，而是事件

定義一次命名事件：

\[
\mathcal N
=
(
A,x,T,c,t,\Gamma
)
\]

其中：

- \(A\)：命名者；
- \(x\)：被命名對象；
- \(T\)：名稱；
- \(c\)：語境；
- \(t\)：時間；
- \(\Gamma\)：命名規則、權威或傳播機制。

因此：

\[
\boxed{
\text{Name}
}
\]

本身具有歷史。

後來的人使用 \(T\)，可能並不是重新命名，而是在繼承：

\[
\mathcal N_0
\rightarrow
\mathcal N_1
\rightarrow
\cdots
\rightarrow
\mathcal N_t.
\]

這形成：

# Naming Chain

---

# 17. T 為何還是 T？

設：

\[
T_t
\xrightarrow{F}
T_{t+1}.
\]

如果：

\[
X(T_t)
\neq
X(T_{t+1}),
\]

為何我們仍說：

\[
T_t
\equiv_{\mathrm{id}}
T_{t+1}？
\]

關鍵不可能是：

\[
\text{Nothing Changed}.
\]

因為許多持續存在的對象一直在改變。

所以身份持續必須依賴一組允許變化下的不變條件：

\[
\mathcal I_\alpha(T).
\]

若：

\[
\mathcal I_\alpha(T_t)
\cong
\mathcal I_\alpha(T_{t+1}),
\]

則允許：

\[
T_t
\equiv_\alpha
T_{t+1}.
\]

得到：

\[
\boxed{
\text{Persistence}
\neq
\text{Static Sameness}.
}
\]

身份持續更接近：

\[
\boxed{
\text{Invariant Preservation Under Allowed Transformation}.
}
\]

---

# 18. T 又是 T

考慮：

\[
T_0
\rightarrow
X_1
\rightarrow
X_2
\rightarrow
T_3.
\]

中間：

\[
X_1
\not\equiv_\alpha
T_0.
\]

最後卻重新：

\[
T_3
\equiv_\alpha
T_0.
\]

這形成：

# Identity Recurrence

至少可以分成四種：

### 18.1 狀態恢復

\[
X_t
\rightarrow
X'
\rightarrow
X_t.
\]

### 18.2 命名恢復

舊名稱失效後重新被採用。

### 18.3 制度恢復

某身份曾被撤銷，後由制度重新承認。

### 18.4 認知再識別

對象從未失去身份，只是觀察者一度不知道：

\[
J_A(T)=\mathrm{Unknown}
\rightarrow
J_A(T)=\mathrm{Same}.
\]

因此：

\[
\boxed{
\text{T 又是 T}
}
\]

本身也是一族不同事件。

---

# 19. T 怎麼不是 T？

同樣：

\[
\boxed{
\text{Not-T}
}
\]

也不是唯一狀態。

某個 \(T\) 可以因以下原因失去某種身份：

\[
\Delta G
\]

字形斷裂；

\[
\Delta R
\]

所指轉移；

\[
\Delta N
\]

命名鏈斷裂；

\[
\Delta O
\]

操作功能改變；

\[
\Delta H
\]

歷史 provenance 無法持續；

\[
\Delta C
\]

namespace 發生遷移；

或：

\[
\Delta\mathcal I_\alpha
>
\theta_\alpha.
\]

因此：

\[
\boxed{
T\rightarrow\neg_\alpha T
}
\]

應理解為：

> \(T\) 在身份維度 \(\alpha\) 上發生斷裂。

本文稱為：

# Identity Rupture

---

# 20. 身份不是對象內部的一個單獨欄位

到這裡可以看到，一個符號的 identity 很難只寫成：

```text
id = "T"
```

更成熟的形式可能是：

\[
\boxed{
Identity
=
F
(
Object,
Relations,
History,
Criterion,
Observer,
Context
).
}
\]

這意味著身份具有至少兩種不同來源：

### 20.1 內生身份

由對象自身結構、不變量與狀態支持。

### 20.2 關係身份

由：

- 歷史；
- 制度；
- 社群；
- 所指；
- 命名；
- provenance；

共同支持。

因此：

\[
\boxed{
\text{Identity}
\neq
\text{Intrinsic State Only}.
}
\]

---

# 21. 單符號極限

現在考慮：

\[
\Gamma_n
=
T_1T_2\cdots T_n
\]

且：

\[
\forall i,\quad G(T_i)=T.
\]

所以表面字母表：

\[
\mathcal A_G=\{T\}.
\]

其字形多樣性：

\[
|\mathcal A_G|=1.
\]

若只看 glyph 變數：

\[
H(G)=0.
\]

但底層可以有：

\[
X(T_1),
X(T_2),
\ldots,
X(T_n)
\]

且：

\[
X(T_i)\neq X(T_j).
\]

因此：

\[
H(X\mid G=T)>0.
\]

甚至可以隨 \(n\) 增長。

---

# 22. 表面符號熵—身份熵分離原理

本文提出：

## 原理 2：Surface–Identity Entropy Separation Principle

存在符號系統，使：

\[
H(G)\rightarrow0
\]

而：

\[
H(I\mid G)
\not\rightarrow0.
\]

更強地，可能：

\[
\boxed{
H(G)=0,
\qquad
H(I\mid G=T)>0.
}
\]

這裡的 \(I\) 不是單純 bit payload。

它可以包含：

\[
I
=
(
X,R,N,O,H,C,\ldots
).
\]

因此：

\[
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
\]

不必是一串「完全相同的東西」。

它只是一串：

> **對某個低維觀察器而言具有相同可見投影的對象。**

---

# 23. 投影同一性與本體同一性的分離

定義觀察投影：

\[
\Pi_A:
\mathcal X
\rightarrow
\mathcal Y_A.
\]

若：

\[
\Pi_A(T_i)=\Pi_A(T_j),
\]

我們只能推出：

\[
T_i
\equiv_{\Pi_A}
T_j.
\]

不能直接推出：

\[
T_i=T_j.
\]

因此：

\[
\boxed{
\text{Observer-Indistinguishability}
\not\Rightarrow
\text{Ontological Identity}.
}
\]

反方向也一樣。

某個持續對象對兩個觀察器可能：

\[
\Pi_A(T)\neq\Pi_B(T),
\]

但兩者仍然指向同一歷史對象。

所以：

\[
\boxed{
\text{Different Projection}
\not\Rightarrow
\text{Different Object}.
}
\]

---

# 24. 同一性格與 equivalence lattice

如果存在多個身份關係：

\[
\equiv_1,
\equiv_2,
\ldots,
\equiv_n,
\]

它們可以形成由粗到細的判定結構。

例如：

\[
\equiv_G
\]

可能非常粗，只看 glyph。

而：

\[
\equiv_{GXHR}
\]

要求 glyph、state、history、referent 全部相符。

因此可以建立：

\[
\boxed{
\mathcal L_I
=
(
\mathfrak E,\preceq
)
}
\]

其中：

\[
\equiv_\alpha
\preceq
\equiv_\beta
\]

表示：

> \(\beta\) 至少與 \(\alpha\) 一樣嚴格。

這形成：

# Identity Criterion Lattice

於是：

> 「它們是不是同一個？」

可以被重新表述成：

> 「你要求多嚴格的身份關係？」

---

# 25. 身份過嚴與身份過鬆

這個 lattice 立即帶出兩種失敗模式。

## 25.1 Identity Over-Collapse

判準太鬆：

\[
\alpha\rightarrow0
\]

大量不同對象被壓成：

\[
T_i\equiv_\alpha T_j.
\]

結果：

\[
\boxed{
\text{Difference Loss}.
}
\]

## 25.2 Identity Over-Fragmentation

判準太嚴：

\[
\alpha\rightarrow\infty
\]

任何微小變化都造成：

\[
T_t\not\equiv_\alpha T_{t+\epsilon}.
\]

結果是：

\[
\boxed{
\text{Continuity Loss}.
}
\]

成熟的 identity system 因此需要在：

\[
\text{Collapse}
\]

與：

\[
\text{Fragmentation}
\]

之間找到任務相對判準。

---

# 26. Identity Resolution

本文因此定義：

\[
\boxed{
\operatorname{ResolveIdentity}
(
T_i,T_j,
\mathcal T
)
}
\]

其中 \(\mathcal T\) 是任務。

例如：

### 字型渲染任務

主要要求：

\[
\equiv_G.
\]

### 密碼封包任務

需要：

\[
\equiv_X
\land
\equiv_H
\]

甚至 authenticated identity。

### 法律身份

可能高度依賴：

\[
\equiv_H
\land
\equiv_N
\land
\equiv_{\mathrm{institution}}.
\]

### 語義理解

主要關注：

\[
\equiv_R
\]

與 interpretive alignment。

所以：

\[
\boxed{
\text{Identity Is Task-Conditioned}.
}
\]

但這不等於：

> 身份純粹任意。

因為每一個有效判定仍然必須接受其任務的 constraints。

---

# 27. 新的符號學基本問題

傳統符號學經常問：

> 這個符號指什麼？

本文增加一組不同問題：

\[
\boxed{
\begin{aligned}
&\text{這是什麼？}\\
&\text{它為什麼還是它？}\\
&\text{誰把它稱為它？}\\
&\text{它何時開始成為它？}\\
&\text{什麼改變會使它不再是它？}\\
&\text{它失去身份後能否恢復？}\\
&\text{兩個相同表面是否具有不同歷史？}\\
&\text{不同表面是否仍能保持同一身份？}
\end{aligned}
}
\]

符號因此不再只是：

\[
\boxed{
\text{representation}
}
\]

而進一步成為：

\[
\boxed{
\text{identity-bearing dynamic object}.
}
\]

---

# 28. 與既有理論的關係

本文與既有研究至少有四個直接接點。

第一，type/token distinction 已經提供「可重複類型」與「具體出現」的基本區別，但當前哲學研究也承認 type/token 關係本身仍有許多爭議，不能簡化成唯一一種普遍關係。

第二，Frege 的 identity puzzle 說明：

\[
a=a
\]

與：

\[
a=b
\]

即使涉及同一 denotation，也可能具有不同 cognitive significance。

第三，Peirce 的 sign-object-interpretant 結構使符號身份不能只被處理成 sign 與 object 的靜態二元映射，interpretation 本身是符號作用的一部分。

第四，rigid designation 與相關名稱／指涉研究顯示「名稱如何跨可能情境繼續指定同一對象」本身就是獨立哲學問題。

本文的新增工作不是聲稱上述問題從未有人研究。

真正新增的研究程序是：

\[
\boxed{
\text{將多種 identity relations 同時顯式化}
}
\]

並把：

\[
\text{生成}
+
\text{命名}
+
\text{狀態}
+
\text{所指}
+
\text{歷史}
+
\text{持續}
+
\text{恢復}
+
\text{觀察器}
\]

放入同一套動態符號身份框架。

---

# 29. 核心命題

## 命題 1：同形不足以推出同一

\[
G(T_i)=G(T_j)
\not\Rightarrow
T_i=T_j.
\]

---

## 命題 2：異形不足以推出不同身份

\[
G(T_i)\neq G(T_j)
\not\Rightarrow
T_i\neq_{\mathrm{id}}T_j.
\]

---

## 命題 3：未索引同一性可能欠定義

若至少存在兩個合法身份關係：

\[
\equiv_\alpha,
\equiv_\beta
\]

使：

\[
T_i\equiv_\alpha T_j
\]

但：

\[
T_i\not\equiv_\beta T_j,
\]

則未指定 identity criterion 的問題：

\[
T_i\stackrel{?}{=}T_j
\]

對當前框架而言是欠定義的。

---

## 命題 4：身份持續不要求完全狀態不變

存在：

\[
T_t,T_{t+1}
\]

使：

\[
X(T_t)\neq X(T_{t+1})
\]

但：

\[
T_t\equiv_H T_{t+1}.
\]

---

## 命題 5：名稱同一不充分

\[
N(T_i)=N(T_j)
\not\Rightarrow
T_i=T_j.
\]

---

## 命題 6：所指同一不充分

\[
R(T_i)=R(T_j)
\not\Rightarrow
\mathbf I(T_i)=\mathbf I(T_j).
\]

---

## 命題 7：可見熵不決定身份熵

\[
H(G)=0
\]

仍可能：

\[
H(I\mid G)>0.
\]

---

# 30. 一個極端思想實驗

假設宇宙只允許顯示一個符號：

\[
\boxed{T}
\]

所有存在都必須顯示成：

\[
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT.
\]

但系統內部仍保存：

\[
T_i
=
(
x_i,r_i,n_i,o_i,h_i,t_i
).
\]

此時：

\[
|\mathcal A_{\mathrm{visible}}|=1.
\]

然而若：

\[
|\mathcal X|>1,
\]

甚至：

\[
|\mathcal X|\rightarrow\infty,
\]

則：

\[
\boxed{
\text{表面符號宇宙可以極端貧乏，
而身份宇宙仍極端豐富。}
}
\]

這是一個很重要的反直覺：

> 語言表面複雜度不是身份結構複雜度的必要代理量。

---

# 31. TTTTTTTT 的真正問題

所以：

\[
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
\]

不再只是「很多個 T」。

我們必須問：

\[
\begin{aligned}
&T_1\equiv_GT_2？\\
&T_1\equiv_XT_2？\\
&T_1\equiv_RT_2？\\
&T_1\equiv_HT_2？\\
&T_1\equiv_NT_2？\\
&T_1\equiv_OT_2？\\
&T_1\equiv_{T}T_2？
\end{aligned}
\]

也就是：

\[
\boxed{
\text{Which T is the same T under which identity relation?}
}
\]

---

# 32. 從符號本體論轉向符號身份動力學

傳統靜態表示可以寫：

\[
T\mapsto R.
\]

本文則要求：

\[
\mathfrak T_{t+1}
=
F
(
\mathfrak T_t,
u_t,
A_t,
c_t
).
\]

身份判定：

\[
J_{t+1}
=
J
(
\mathfrak T_t,
\mathfrak T_{t+1},
\alpha,
A,
c
).
\]

因此本文真正研究的是：

\[
\boxed{
\text{Identity as a Dynamical Relation}.
}
\]

而不只是：

\[
\text{Identity as a Static Label}.
\]

---

# 33. 系列後續問題

完成這篇總地基後，後續論文將分別處理：

### Paper 02  
**T 是不是 T？**  
身份判定、四值輸出、觀察者與不確定性。

### Paper 03  
**T 為什麼是 T？**  
身份 grounding、不變量與 Identity Certificate。

### Paper 04  
**T 怎麼變成 T？**  
符號生成、分類、制度承認與 Become-T。

### Paper 05  
**T 怎麼被稱為 T？**  
命名事件、指涉、權威、namespace 與 naming chain。

### Paper 06  
**T 為何還是 T？**  
跨時間身份、不變量、持續與忒修斯型問題。

### Paper 07  
**T 又是 T；T 怎麼不是 T？**  
身份斷裂、失去、恢復、再識別與 recurrence。

### Paper 08  
**TTTTTTTTTTTTTT…**  
表面符號熵坍縮、潛在身份熵與單符號極限。

---

# 34. 結論

本文最初的問題似乎只是：

\[
T=T？
\]

但真正展開後，它變成：

\[
\boxed{
T_i
\equiv_{\alpha,A,c,t}
T_j？
}
\]

也就是：

> 兩個存在，在什麼身份判準、什麼觀察者、什麼語境與什麼歷史時間下，有資格被判定為同一個 \(T\)？

所以：

\[
\boxed{
T\text{ 是 }T
}
\]

可以成立。

\[
\boxed{
T\text{ 不是 }T
}
\]

也可以成立。

\[
\boxed{
T\text{ 又是 }T
}
\]

仍可以成立。

只要這些命題的 identity relation 不同，就不存在真正的形式矛盾。

因此本文最終提出：

\[
\boxed{
\text{Identity is not one equality sign.}
}
\]

以及：

\[
\boxed{
\text{Same appearance is only one possible projection of sameness.}
}
\]

最後，一串看似毫無差異的：

\[
TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
\]

真正隱藏的問題不是：

> 「為什麼全部都是 T？」

而是：

\[
\boxed{
\text{我們究竟靠什麼，認為其中任何兩個 T 是同一個 T？}
}
\]

這才是多重同一性符號學真正的起點。