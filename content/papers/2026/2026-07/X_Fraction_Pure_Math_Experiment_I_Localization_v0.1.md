# X 分數結構微積分純數學實戰 I：可去表示缺口、局部化與來源非坍縮

## X Fraction-Structure Pure Mathematics Experiment I: Removable Presentation Gaps, Localization, and Provenance Non-Collapse

**文件編號**：EML-X-FRAC-EXP-I-2026-v0.1  
**作者**：Neo.K（許筌崴）｜EveMissLab（一言諾科技有限公司）  
**理論整理與形式化協作**：Aletheia（GPT）  
**版本日期**：2026-07-26  
**承接文件**：《X 分數結構微積分 I：相對存在的形成、微分、約分與再積分》  
**文件性質**：純數學基準測試、交換代數案例、理論修正紀錄

---

## 摘要

本文對 X 分數結構微積分進行第一次純數學實戰。測試案例為整域中的可約分式及其在分式域、主局部化與局部環中的不同合法性。令 $R$ 為整域， $\mathfrak p$ 為素理想，取非零元素 $u\in\mathfrak p$ 與任意 $v\in R$ ，考察原始分數表示：

$$
E
=
\frac{uv}{u}.
$$

在分式域 $\operatorname{Frac}(R)$ 中：

$$
\left[
\frac{uv}{u}
\right]
=
\left[
\frac{v}{1}
\right].
$$

在主局部化 $R_u$ 中，因為 $u$ 被允許成為可逆元，原表示 $uv/u$ 是合法表示。相對地，在局部環 $R_{\mathfrak p}$ 中，合法分母必須位於 $R\setminus\mathfrak p$ ；由於 $u\in\mathfrak p$ ，原表示不是 $R_{\mathfrak p}$ 的合法分數代表。然而，同一分式域元素仍由合法代表 $v/1$ 屬於 $R_{\mathfrak p}$ 。

此案例證明：

$$
\boxed{
\text{特定分數表示不合法}
\not\Rightarrow
\text{其商類不屬於目標結構}.
}
$$

測試結果顯示，X 分數結構微積分的來源保存、非坍縮、上下文微分與表示缺口分類具有一致用途；但原始第一版形成流程過度線性，未充分區分：

1. 語法形成；
2. 環境分式域中的商類形成；
3. 特定代表在目標上下文中的直接合法性；
4. 商類是否存在至少一個目標上下文合法代表；
5. 商類向目標結構的語義實現。

本文因此提出「雙上下文、四判定」修正：分數首先在環境上下文 $\Gamma_{\mathrm{amb}}$ 中形成商類，再相對於目標上下文 $\Gamma_{\mathrm{tar}}$ 判定是否存在合法代表。第一輪實戰的結論不是 X 理論原樣通過，而是：

$$
\boxed{
\text{核心方向通過，}
\quad
\text{單一形成判定必須修正。}
}
$$

本文沒有得到新的交換代數定理。新增價值位於跨層判定、來源證書、表示—商類分離、上下文轉送與失敗分類。這個結果同時提供一個明確可反駁標準：若 X 系統把原表示在 $R_{\mathfrak p}$ 中的失敗誤判為其商類不存在，則該版本的 X 分數形成律不正確。

**關鍵詞**：X 積分；分數結構；局部化；局部環；分式域；表示缺口；商類；來源保存；非坍縮；語義實現

---

# 0. 實驗結論先行

本次實驗得到四個主要結論。

## 0.1 標準代數結果完全保守

X 分數系統在本例中不得改變：

$$
\frac{uv}{u}
=
v
$$

於 $\operatorname{Frac}(R)$ 中成立的事實。

若 X 系統因來源保存而拒絕此商類等式，則不保守。

## 0.2 來源保存具有額外資訊

雖然：

$$
\left[
(uv,u)
\right]
=
\left[
(v,1)
\right],
$$

但兩個表示具有不同來源與不同分母歷史。這些差異不屬於分式域元素本身，卻可作為 X 證書的外加結構保存。

## 0.3 原始形成律需要修正

在 $R_{\mathfrak p}$ 中，原表示 $(uv,u)$ 的分母不合法，但其商類仍屬於 $R_{\mathfrak p}$ 。

因此必須區分：

$$
\operatorname{RepLegal}_{\Gamma}(E)
$$

與：

$$
\operatorname{ClassLegal}_{\Gamma}([E]).
$$

一般而言：

$$
\boxed{
\neg\operatorname{RepLegal}_{\Gamma}(E)
\not\Rightarrow
\neg\operatorname{ClassLegal}_{\Gamma}([E]).
}
$$

## 0.4 X 的新增價值不是新代數等式

標準交換代數已經知道：

- 分式域等價；
- 局部化；
- 局部環；
- 合法分母；
- 正則函數與可去表示缺口。

X 在本例中增加的是：

- 統一的形成層級；
- 來源歷史；
- 關係與上下文證書；
- 表示失敗與結構失敗分離；
- 再積分停止前沿；
- 可供機器判定的失敗類型。

---

# 第一部　實驗問題與可反駁標準

## 1. 實驗問題

本次測試不問：

> X 語言能否重新敘述一個簡單約分？

真正問題是：

> 當同一個分式域元素在不同局部化上下文中具有不同合法代表時，X 分數形成律能否同時保存來源、承認商類等價、正確判定局部合法性，並避免把表示失敗誤判為結構不存在？

## 2. 六項測試假設

### 假設 H1：分層能力

X 系統可以區分：

$$
\operatorname{RawExpression},
\quad
\operatorname{QuotientClass},
\quad
\operatorname{TargetRealization}.
$$

### 假設 H2：上下文分母合法性

相同分母 $u$ 在不同上下文中可以有不同合法性：

$$
\operatorname{DenLegal}_{\Gamma_u}(u),
$$

但：

$$
\neg
\operatorname{DenLegal}_{\Gamma_{\mathfrak p}}(u).
$$

### 假設 H3：來源非坍縮

商類等價不會抹除原始表示歷史：

$$
(uv,u)
\sim_q
(v,1),
$$

但：

$$
(uv,u)
\not\equiv_{\mathrm{src}}
(v,1).
$$

### 假設 H4：奇點分層

原表示在 $\mathfrak p$ 處的失敗應被分類為表示缺口，而非商類或正則結構的真奇點。

### 假設 H5：再積分守衛

一個分數可在某上下文中形成，不會使所有相關分數在另一上下文中自動形成。

### 假設 H6：保守實現

移除 X 證書後，所得代數語義必須回到標準局部化與分式域。

## 3. 失敗條件

任一情況成立，皆表示第一版框架需要修正：

1. 因來源不同而拒絕标准商類等式；
2. 因原表示分母不合法而宣稱商類不在局部環；
3. 未區分語法形成與語義實現；
4. 未區分特定代表合法與存在合法代表；
5. 把表示缺口分類為不可修復結構奇點；
6. 從一次合法約分推出後續所有再積分都合法；
7. 無法指出 X 相較標準代數增加了哪些可驗證資訊。

---

# 第二部　交換代數基準

## 4. 一般設定

令 $R$ 為整域， $\mathfrak p$ 為 $R$ 的素理想。選取：

$$
0
\neq
u
\in
\mathfrak p,
$$

以及：

$$
v
\in
R.
$$

令：

$$
K
:=
\operatorname{Frac}(R).
$$

定義兩個原始表示：

$$
E
:=
(uv,u),
$$

$$
N
:=
(v,1).
$$

對應字形為：

$$
E
\rightsquigarrow
\frac{uv}{u},
$$

$$
N
\rightsquigarrow
\frac{v}{1}.
$$

## 5. 分式域等價

分式域中的等價關係為：

$$
(a,b)
\sim
(c,d)
\quad
\Longleftrightarrow
\quad
ad
=
bc.
$$

對 $E$ 與 $N$ ：

$$
(uv)\cdot1
=
u\cdot v.
$$

因此：

$$
E
\sim
N.
$$

於是：

$$
\boxed{
[E]_K
=
[N]_K
=
v.
}
$$

這是後續所有 X 判定不得破壞的代數基準。

## 6. 主局部化 $R_u$

令：

$$
S_u
:=
\{
1,u,u^2,u^3,\ldots
\}.
$$

定義：

$$
R_u
:=
S_u^{-1}R.
$$

因為：

$$
u
\in
S_u,
$$

所以：

$$
\frac{uv}{u}
$$

是 $R_u$ 中的合法直接表示。

而且：

$$
\frac{uv}{u}
=
\frac{v}{1}
$$

於 $R_u$ 中成立。

## 7. 局部環 $R_{\mathfrak p}$

令：

$$
S_{\mathfrak p}
:=
R\setminus\mathfrak p.
$$

定義局部環：

$$
R_{\mathfrak p}
:=
S_{\mathfrak p}^{-1}R.
$$

合法分母必須屬於：

$$
S_{\mathfrak p}.
$$

但由設定：

$$
u
\in
\mathfrak p.
$$

因此：

$$
u
\notin
S_{\mathfrak p}.
$$

故原始對：

$$
(uv,u)
$$

不是 $R_{\mathfrak p}$ 的合法直接代表。

另一方面：

$$
1
\notin
\mathfrak p,
$$

所以：

$$
1
\in
S_{\mathfrak p}.
$$

因此：

$$
(v,1)
$$

是 $R_{\mathfrak p}$ 的合法代表。

由於兩者在 $K$ 中代表同一元素：

$$
[E]_K
=
[N]_K,
$$

得到：

$$
\boxed{
[E]_K
\in
R_{\mathfrak p}
\quad
\text{但}
\quad
E
\notin
R\times S_{\mathfrak p}.
}
$$

這裡第一個「屬於」指分式域元素由合法代表 $N$ 實現在局部環中；第二個「不屬於」指原始表示對不是局部環的合法表示資料。

## 8. 基準命題一：表示不合法不推出商類不存在

### 命題

設 $R$ 為整域、 $\mathfrak p$ 為素理想、 $0\neq u\in\mathfrak p$ 且 $v\in R$ 。令：

$$
E
=
\frac{uv}{u}
\in
K.
$$

則：

1. 原表示 $(uv,u)$ 不是 $R_{\mathfrak p}$ 的合法表示對；
2. 分式域元素 $[E]_K$ 屬於 $R_{\mathfrak p}$ ；
3. 其合法局部代表為 $(v,1)$ 。

### 證明

由：

$$
u
\in
\mathfrak p,
$$

可知：

$$
u
\notin
R\setminus\mathfrak p.
$$

因此 $(uv,u)$ 不是 $R_{\mathfrak p}$ 的合法表示對。

另一方面：

$$
(uv)\cdot1
=
u\cdot v,
$$

所以：

$$
(uv,u)
\sim
(v,1)
$$

於 $K$ 中成立。

又因：

$$
1
\in
R\setminus\mathfrak p,
$$

故 $(v,1)$ 是 $R_{\mathfrak p}$ 的合法表示。於是 $[E]_K$ 由 $(v,1)$ 實現在 $R_{\mathfrak p}$ 中。證畢。

## 9. 基準命題二：不可逆分母的真正障礙

令：

$$
G
:=
\frac{1}{u}
\in
K.
$$

則：

$$
G
\in
R_u,
$$

但：

$$
G
\notin
R_{\mathfrak p}.
$$

### 證明

在 $R_u$ 中， $u\in S_u$ ，因此 $1/u$ 合法。

反設：

$$
\frac{1}{u}
=
\frac{r}{s}
$$

於 $K$ 中成立，其中：

$$
s
\notin
\mathfrak p.
$$

交叉相乘得到：

$$
s
=
ur.
$$

由於：

$$
u
\in
\mathfrak p,
$$

故：

$$
ur
\in
\mathfrak p.
$$

於是：

$$
s
\in
\mathfrak p,
$$

與 $s\notin\mathfrak p$ 矛盾。

因此：

$$
\boxed{
\frac{1}{u}
\notin
R_{\mathfrak p}.
}
$$

此命題提供再積分守衛的真正失敗案例： $uv/u$ 可藉由合法代表進入 $R_{\mathfrak p}$ ，但 $1/u$ 不行。

---

# 第三部　具體多項式案例

## 10. 單變量專門化

取任意域 $K_0$ ，令：

$$
R
:=
K_0[x].
$$

選取：

$$
a
\in
K_0,
$$

並定義：

$$
u
:=
x-a,
$$

$$
v
:=
x+a.
$$

則：

$$
uv
=
(x-a)(x+a)
=
x^2-a^2.
$$

取素理想：

$$
\mathfrak p
:=
(x-a).
$$

原始分數為：

$$
E_a
:=
\frac{x^2-a^2}{x-a}.
$$

正規代表為：

$$
N_a
:=
\frac{x+a}{1}.
$$

在有理函數域 $K_0(x)$ 中：

$$
\boxed{
[E_a]
=
[N_a].
}
$$

## 11. 三個代數上下文

### 11.1 有理函數域

在：

$$
\Gamma_K
:=
K_0(x)
$$

中， $E_a$ 與 $N_a$ 均為合法表示，且屬於同一商類。

### 11.2 主局部化

在：

$$
\Gamma_u
:=
K_0[x,(x-a)^{-1}]
$$

中， $x-a$ 已被宣告可逆，因此 $E_a$ 是合法直接表示。

### 11.3 局部環

在：

$$
\Gamma_{\mathfrak p}
:=
K_0[x]_{(x-a)}
$$

中，原分母：

$$
x-a
$$

位於極大理想 $(x-a)$ ，因此不是合法局部分母。

但：

$$
x+a
\in
K_0[x]_{(x-a)},
$$

故商類仍有合法局部代表。

## 12. 幾何解讀

令：

$$
X
:=
\operatorname{Spec}(K_0[x]).
$$

主開集：

$$
D(x-a)
:=
\{
\mathfrak q
\in
X
\mid
x-a
\notin
\mathfrak q
\}.
$$

原表示：

$$
\frac{x^2-a^2}{x-a}
$$

直接定義 $D(x-a)$ 上的正則函數。

但此正則函數等於：

$$
x+a,
$$

而 $x+a$ 是整個 $X$ 上的正則函數。

因此，原表示在閉點 $(x-a)$ 處的失敗不是函數本身的真奇點，而是特定分數表示沒有使用最大正則域。

---

# 第四部　X 分數編碼

## 13. 四種上下文必須分開

本例至少需要四種上下文。

### 13.1 語法上下文

$$
\Gamma_{\mathrm{syn}}
$$

負責判定字形與來源對能否形成原始分數表示：

$$
\Gamma_{\mathrm{syn}}
\vdash
E
:
\operatorname{RawFracExpr}(R).
$$

### 13.2 環境分式域上下文

$$
\Gamma_{\mathrm{amb}}
:=
K
=
\operatorname{Frac}(R)
$$

負責形成商類：

$$
\Gamma_{\mathrm{amb}}
\vdash
[E]_K
:
K.
$$

### 13.3 直接表示上下文

對目標代數 $A\subseteq K$ ，判定特定表示 $E=(a,b)$ 的分母是否被 $A$ 的表示規則接受：

$$
\Gamma_A
\vdash
\operatorname{RepLegal}(E;A).
$$

### 13.4 目標實現上下文

判定商類是否存在至少一個合法代表，使其屬於 $A$ ：

$$
\Gamma_A
\vdash
\operatorname{ClassLegal}([E]_K;A).
$$

## 14. 原始單上下文流程的問題

第一版 X 分數流程可概括為：

$$
(a,b)
\longrightarrow
\operatorname{RawFrac}(a,b)
\xrightarrow{\operatorname{DenLegal}(b)}
\operatorname{XFrac}(a,b)
\xrightarrow{q}
[a,b].
$$

若把唯一上下文直接設為 $R_{\mathfrak p}$ ，則由：

$$
u
\in
\mathfrak p
$$

得到：

$$
\neg
\operatorname{DenLegal}_{\Gamma_{\mathfrak p}}(u).
$$

於是原流程會在商化前停止，無法到達合法代表 $(v,1)$ 。

這會誤判：

$$
[E]_K
\notin
R_{\mathfrak p}.
$$

但標準代數已證明：

$$
[E]_K
=
[v,1]
\in
R_{\mathfrak p}.
$$

因此，單一上下文與單一形成判定不夠。

## 15. 雙上下文修正

定義：

$$
\Gamma_{\mathrm{amb}}
$$

為環境形成上下文，並定義：

$$
\Gamma_{\mathrm{tar}}
$$

為目標實現上下文。

流程改為：

$$
\boxed{
E
\xrightarrow[\Gamma_{\mathrm{amb}}]{\operatorname{QuotientFormation}}
[E]_K
\xrightarrow[\Gamma_{\mathrm{tar}}]{\operatorname{RepresentativeSearch}}
E'
\xrightarrow{\operatorname{Realization}}
[E']_{\Gamma_{\mathrm{tar}}}.
}
$$

其中要求：

$$
E'
\sim_K
E,
$$

以及：

$$
\operatorname{RepLegal}_{\Gamma_{\mathrm{tar}}}(E').
$$

## 16. 商類合法性的存在量詞

對目標上下文 $\Gamma$ ，定義：

$$
\boxed{
\operatorname{ClassLegal}_{\Gamma}([E])
\quad
\Longleftrightarrow
\quad
\exists E'
\left[
E'
\sim
E
\land
\operatorname{RepLegal}_{\Gamma}(E')
\right].
}
$$

本例中：

$$
\neg
\operatorname{RepLegal}_{\Gamma_{\mathfrak p}}(E),
$$

但取：

$$
E'
=
N
=
(v,1),
$$

可得：

$$
E'
\sim
E,
$$

且：

$$
\operatorname{RepLegal}_{\Gamma_{\mathfrak p}}(E').
$$

所以：

$$
\boxed{
\operatorname{ClassLegal}_{\Gamma_{\mathfrak p}}([E]).
}
$$

## 17. 四判定系統

本次實驗要求加入以下四種判定。

### 17.1 語法形成

$$
\Gamma_{\mathrm{syn}}
\vdash
E
\;\operatorname{synform}.
$$

### 17.2 環境商類形成

$$
\Gamma_{\mathrm{amb}}
\vdash
[E]
\;\operatorname{classform}.
$$

### 17.3 特定代表合法

$$
\Gamma_{\mathrm{tar}}
\vdash
E
\;\operatorname{replegal}.
$$

### 17.4 商類目標實現

$$
\Gamma_{\mathrm{tar}}
\vdash
[E]
\;\operatorname{realizable}.
$$

四者不能合併為單一：

$$
\Gamma
\vdash
E
\;\operatorname{form}.
$$

---

# 第五部　上下文判定矩陣

## 18. 核心矩陣

| 對象與判定 | $\Gamma_{\mathrm{syn}}$ | $\Gamma_K$ | $\Gamma_u$ | $\Gamma_{\mathfrak p}$ |
|---|---:|---:|---:|---:|
| 原字形 $E=(uv,u)$ 可形成 | 成立 | 成立 | 成立 | 成立 |
| $E$ 是合法直接代表 | 不適用 | 成立 | 成立 | 不成立 |
| 商類 $[E]_K$ 可形成 | 不適用 | 成立 | 經嵌入成立 | 經合法代表成立 |
| 正規代表 $N=(v,1)$ 合法 | 成立 | 成立 | 成立 | 成立 |
| $[E]_K=[N]_K$ | 不判定 | 成立 | 成立 | 由環境商類轉送成立 |
| 原分母 $u$ 可逆 | 不判定 | 成立 | 成立 | 不成立 |
| 商類由某合法代表實現 | 不判定 | 成立 | 成立 | 成立 |
| 來源歷史仍可回溯 | 由 X 證書要求 | 由 X 證書要求 | 由 X 證書要求 | 由 X 證書要求 |

表中的第一列只表示原字形可以作為語法對象形成，不表示它能直接作為每個代數中的合法表示。

## 19. 形成狀態不是二值

本例顯示至少需要以下狀態：

$$
\operatorname{SynFormed},
$$

$$
\operatorname{ClassFormed},
$$

$$
\operatorname{DirectlyAdmissible},
$$

$$
\operatorname{IndirectlyRealizable},
$$

$$
\operatorname{NotRealizable}.
$$

對原表示 $E$ 在 $\Gamma_{\mathfrak p}$ 中：

$$
\operatorname{SynFormed}(E),
$$

$$
\neg
\operatorname{DirectlyAdmissible}_{\Gamma_{\mathfrak p}}(E),
$$

但：

$$
\operatorname{IndirectlyRealizable}_{\Gamma_{\mathfrak p}}([E]).
$$

對 $G=1/u$ 在 $\Gamma_{\mathfrak p}$ 中：

$$
\operatorname{SynFormed}(G),
$$

但：

$$
\neg
\operatorname{ClassLegal}_{\Gamma_{\mathfrak p}}([G]).
$$

這兩種失敗不能輸出同一個標記。

---

# 第六部　X 六律逐條實戰

## 20. 第一律：積分形成律

### 20.1 原判定

原形成律要求：

$$
\operatorname{DenLegal}_{\Gamma}(u)
$$

後才形成：

$$
\operatorname{XFrac}_{\mathrm{quot}}^{\Gamma}(uv,u).
$$

### 20.2 實驗結果

在 $\Gamma_u$ 中：

$$
\operatorname{DenLegal}_{\Gamma_u}(u)
$$

成立，因此直接形成通過。

在 $\Gamma_{\mathfrak p}$ 中：

$$
\operatorname{DenLegal}_{\Gamma_{\mathfrak p}}(u)
$$

不成立，因此特定代表直接形成失敗。

但商類可藉由 $N=(v,1)$ 實現。

### 20.3 判定

第一律：

$$
\boxed{
\operatorname{PassWithRevision}.
}
$$

必須把「分數形成」拆成：

$$
\operatorname{PresentationFormation}
$$

與：

$$
\operatorname{ClassRealization}.
$$

## 21. 第二律：來源保存律

對原表示：

$$
\operatorname{Src}(E)
=
\langle
uv,u,
/_{\mathrm{quot}},
\Gamma_{\mathrm{amb}}
\rangle.
$$

對正規代表：

$$
\operatorname{Src}(N)
=
\langle
v,1,
/_{\mathrm{quot}},
\Gamma_{\mathrm{tar}}
\rangle.
$$

商化證書記錄：

$$
\operatorname{QuotCert}(E,N)
=
\left\langle
(uv)\cdot1
=
u\cdot v,
u,
\Gamma_{\mathrm{amb}},
\Gamma_{\mathrm{tar}}
\right\rangle.
$$

因此：

$$
\operatorname{Src}([E])
\supseteq
\{
E,N,\operatorname{QuotCert}(E,N)
\}.
$$

### 判定

第二律：

$$
\boxed{
\operatorname{Pass}.
}
$$

但應明確說明：來源歷史是 X 擴充資料，不是分式域元素的內在不變量。

## 22. 第三律：非坍縮律

標準代數要求：

$$
[E]_K
=
[N]_K.
$$

X 非坍縮要求：

$$
E
\not\equiv_{\mathrm{presentation}}
N.
$$

兩者完全相容，只要不錯置層級：

$$
\boxed{
[E]_K=[N]_K
\quad
\land
\quad
E\not\equiv_{\mathrm{presentation}}N.
}
$$

### 判定

第三律：

$$
\boxed{
\operatorname{Pass}.
}
$$

若非坍縮律被解讀為拒絕 $[E]_K=[N]_K$ ，則立即失敗。

## 23. 第四律：再積分守衛律

取：

$$
G
=
\frac{1}{u}.
$$

在 $\Gamma_u$ 中：

$$
G
\in
R_u.
$$

因此，若關係 $\sigma$ 是 $R_u$ 中的乘法或其他合法代數操作，則：

$$
\Gamma_u
\vdash
\mathsf I_{\sigma}(F;G)
\;\operatorname{form}.
$$

在 $\Gamma_{\mathfrak p}$ 中：

$$
G
\notin
R_{\mathfrak p}.
$$

因此：

$$
\Gamma_{\mathfrak p}
\nvdash
\mathsf I_{\sigma}(F;G)
\;\operatorname{form}.
$$

即使：

$$
F
\in
R_{\mathfrak p},
$$

也不能推出：

$$
G
\in
R_{\mathfrak p}.
$$

### 判定

第四律：

$$
\boxed{
\operatorname{Pass}.
}
$$

而且本例提供了非人為的停止前沿。

## 24. 第五律：結構微分律

### 24.1 來源微分

$$
\mathsf D_{\mathrm{src}}(E)
=
\left\langle
uv,u,
/_{\mathrm{quot}},
\Gamma_{\mathrm{amb}}
\right\rangle.
$$

### 24.2 商化微分

$$
\mathsf D_{\mathrm{quotient}}(E)
=
\left\langle
E,
N,
E\sim N,
u,
\Delta_{\mathrm{identified}},
\Delta_{\mathrm{preserved}}
\right\rangle.
$$

其中：

$$
\Delta_{\mathrm{identified}}
=
\text{商類中的共同因子差異},
$$

而：

$$
\Delta_{\mathrm{preserved}}
=
\text{表示與來源歷史}.
$$

### 24.3 上下文微分

$$
\mathsf D_{\mathrm{ctx}}(E)
=
\left\langle
\Gamma_K,
\Gamma_u,
\Gamma_{\mathfrak p},
\operatorname{RepLegal},
\operatorname{ClassLegal}
\right\rangle.
$$

### 24.4 分母微分

$$
\mathsf D_{\mathrm{den}}(E)
=
\left\langle
u\in S_u,
u\notin S_{\mathfrak p},
\operatorname{Invertible}_{R_u}(u),
\neg\operatorname{Invertible}_{R_{\mathfrak p}}(u)
\right\rangle.
$$

### 24.5 奇點微分

$$
\mathsf D_{\mathrm{sing}}(E;\mathfrak p)
=
\left\langle
\operatorname{PresentationFail},
\operatorname{AlternativeRep}(N),
\operatorname{ClassLegal},
\operatorname{Extendable}
\right\rangle.
$$

### 判定

第五律：

$$
\boxed{
\operatorname{Pass}.
}
$$

但其新增價值是診斷結構，不是新的導數值。

## 25. 第六律：動態整體閉合律

本例只包含有限次：

$$
E
\rightsquigarrow
[E]_K
\rightsquigarrow
N
\rightsquigarrow
R_{\mathfrak p}
$$

的形成與轉送。

它可以測試：

- 身份核心是否保存；
- 來源是否延續；
- 下一次再積分是否停止。

但不能單獨證明：

- 無限遞歸閉合；
- 極限一致性；
- 超限來源保存；
- 動態不動點存在。

### 判定

第六律：

$$
\boxed{
\operatorname{PartialPass}.
}
$$

需要連分數或局部化鏈才能進一步測試。

---

# 第七部　X 分數奇點證書

## 26. 原表示在 $\mathfrak p$ 處的證書

對：

$$
E
=
\frac{uv}{u},
$$

定義：

$$
\operatorname{XFracSingCert}(E;\mathfrak p)
=
\left\langle
C_E,
R_E,
D_E,
I_E,
E_E,
V_E,
Q_E,
G_E
\right\rangle.
$$

各欄位為：

$$
C_E
=
\Gamma_{\mathfrak p},
$$

$$
R_E
=
/_{\mathrm{quot}},
$$

$$
D_E
=
u\notin S_{\mathfrak p},
$$

$$
I_E
=
u^{-1}\notin R_{\mathfrak p},
$$

$$
E_E
=
\operatorname{AlternativeRepresentative}(v,1),
$$

$$
V_E
=
\operatorname{NoCodomainExtensionRequired},
$$

$$
Q_E
=
(uv,u)\sim(v,1),
$$

$$
G_E
=
\operatorname{RealizableVia}(v,1).
$$

因此：

$$
\boxed{
\operatorname{SingType}(E;\mathfrak p)
=
\operatorname{RemovablePresentationGap}.
}
$$

## 27. 與真正逆元缺失的對照

對：

$$
G
=
\frac{1}{u},
$$

不存在 $R_{\mathfrak p}$ 中的合法替代代表。

因此：

$$
\operatorname{XFracSingCert}(G;\mathfrak p)
$$

具有：

$$
D_G
=
u\notin S_{\mathfrak p},
$$

$$
I_G
=
u^{-1}\notin R_{\mathfrak p},
$$

$$
E_G
=
\operatorname{NoAlternativeRepresentative},
$$

$$
G_G
=
\operatorname{TargetRealizationFail}.
$$

故：

$$
\boxed{
\operatorname{SingType}(G;\mathfrak p)
=
\operatorname{InverseObstruction}.
}
$$

本例由此成功區分：

$$
\operatorname{PresentationGap}
\neq
\operatorname{InverseObstruction}.
$$

---

# 第八部　必要理論修正

## 28. 修正一：形成律拆成兩個階段

原形式：

$$
\operatorname{DenLegal}_{\Gamma}(b)
\Longrightarrow
\operatorname{XFrac}_{\rho}^{\Gamma}(a,b)
\;\operatorname{form}
$$

應改為兩階段。

### 28.1 環境形成

$$
\frac{
\Gamma_{\mathrm{amb}}
\vdash
a,b
\quad
\Gamma_{\mathrm{amb}}
\vdash
b
\neq
0
}{
\Gamma_{\mathrm{amb}}
\vdash
[a,b]
:
\operatorname{FracClass}(R)
}.
$$

### 28.2 目標實現

$$
\frac{
\Gamma_{\mathrm{amb}}
\vdash
[a,b]
:
\operatorname{FracClass}(R)
\quad
\exists(c,d)
\left[
(c,d)\sim(a,b)
\land
\operatorname{DenLegal}_{\Gamma_{\mathrm{tar}}}(d)
\right]
}{
\Gamma_{\mathrm{tar}}
\vdash
[a,b]
\;\operatorname{realizable}
}.
$$

## 29. 修正二：分母合法性附著於代表

第一版容易把：

$$
\operatorname{DenLegal}_{\Gamma}(b)
$$

誤解為商類的固有性質。

本例證明它首先是特定代表的性質：

$$
\boxed{
\operatorname{DenLegal}_{\Gamma}
\left(
\operatorname{den}(E)
\right)
\text{ 是表示依賴的。}
}
$$

商類合法性則是存在合法代表：

$$
\operatorname{ClassLegal}_{\Gamma}([E])
\Longleftrightarrow
\exists E'
\left[
E'\sim E
\land
\operatorname{DenLegal}_{\Gamma}
\left(
\operatorname{den}(E')
\right)
\right].
$$

## 30. 修正三：加入正規化轉送證書

定義：

$$
\boxed{
\operatorname{NormTransportCert}_{\Gamma}
(E,E')
=
\left\langle
E\sim E',
\operatorname{RepLegal}_{\Gamma}(E'),
\operatorname{Src}(E),
\operatorname{Src}(E'),
\Delta_{\mathrm{identified}},
\Delta_{\mathrm{preserved}}
\right\rangle.
}
$$

本例中：

$$
\operatorname{NormTransportCert}_{\Gamma_{\mathfrak p}}
\left(
(uv,u),
(v,1)
\right)
$$

是商類進入 $R_{\mathfrak p}$ 的合法轉送證書。

## 31. 修正四：X 分數證書加入雙上下文

原證書只有單一：

$$
\Gamma.
$$

應擴張為：

$$
\boxed{
\operatorname{XFracCert}^{*}(F)
=
\left\langle
\Gamma_{\mathrm{syn}},
\Gamma_{\mathrm{amb}},
\Gamma_{\mathrm{tar}},
C_{\mathrm{rep}},
C_{\mathrm{class}},
C_{\mathrm{transport}},
C_{\mathrm{src}},
C_{\mathrm{guard}}
\right\rangle.
}
$$

其中：

- $\Gamma_{\mathrm{syn}}$ ：語法形成上下文；
- $\Gamma_{\mathrm{amb}}$ ：商類形成的環境上下文；
- $\Gamma_{\mathrm{tar}}$ ：目標實現上下文；
- $C_{\mathrm{rep}}$ ：特定代表合法性；
- $C_{\mathrm{class}}$ ：商類目標合法性；
- $C_{\mathrm{transport}}$ ：代表替換與跨上下文轉送；
- $C_{\mathrm{src}}$ ：來源保存；
- $C_{\mathrm{guard}}$ ：後續再積分守衛。

## 32. 修正五：失敗輸出分層

至少新增：

$$
\operatorname{SyntacticFormationFailure},
$$

$$
\operatorname{AmbientClassFailure},
$$

$$
\operatorname{DirectRepresentationFailure},
$$

$$
\operatorname{AlternativeRepresentativeFound},
$$

$$
\operatorname{TargetRealizationFailure}.
$$

原表示 $E$ 的輸出應是：

$$
\operatorname{DirectRepresentationFailure}
\quad
\land
\quad
\operatorname{AlternativeRepresentativeFound}.
$$

而 $G=1/u$ 的輸出應是：

$$
\operatorname{TargetRealizationFailure}.
$$

---

# 第九部　新增資訊與重述審計

## 33. 哪些完全屬於既有數學

以下內容完全是標準交換代數：

- $\operatorname{Frac}(R)$ 的等價關係；
- $R_u$ 的主局部化；
- $R_{\mathfrak p}$ 的局部環；
- $uv/u=v$ ；
- $1/u\notin R_{\mathfrak p}$ ；
- 合法代表可以不同；
- 正則函數的局部與全域延拓。

這些不能算作 X 理論的新定理。

## 34. X 框架真正增加的內容

### 34.1 統一判定語言

同一套語言同時描述：

- 語法；
- 商化；
- 上下文；
- 表示合法性；
- 目標實現；
- 來源；
- 奇點；
- 再積分。

### 34.2 來源歷史作為一級資料

標準分式域有意捨棄代表差異。X 可以在不破壞商類等式的前提下，於外層保存表示歷史。

### 34.3 失敗層分類

X 明確區分：

$$
\text{這個代表不能用}
$$

與：

$$
\text{這個商類不存在於目標結構}.
$$

### 34.4 跨上下文轉送證書

商類從環境分式域進入特定局部化時，需要記錄使用哪個合法代表。

### 34.5 機器可判定接口

上述差異可被編碼為證書與失敗標記，適合 AI 或證明助理進行結構審計。

## 35. 尚未證明的新增價值

本例尚未證明：

- X 框架能產生新交換代數定理；
- X 微分具有傳統不變量未涵蓋的自然性；
- 來源歷史在純數學中總是必要；
- 證書成本低於其診斷收益；
- X 分數系統具有唯一或最佳形式化。

因此，本次不能宣稱 X 已建立新的代數分支。

較準確的判斷是：

$$
\boxed{
\text{X 在本例中形成一個跨層證書化方法，}
\quad
\text{尚未形成新的代數結果。}
}
$$

---

# 第十部　測試評分

## 36. 假設結果

| 假設 | 結果 | 理由 |
|---|---|---|
| H1：分層能力 | 修正後通過 | 必須增加語法、商類、代表與目標實現四判定 |
| H2：上下文分母合法性 | 通過 | $u$ 在 $R_u$ 可逆，在 $R_{\mathfrak p}$ 不可逆 |
| H3：來源非坍縮 | 通過 | 可同時保存商類等式與表示差異 |
| H4：奇點分層 | 通過 | 成功區分表示缺口與逆元障礙 |
| H5：再積分守衛 | 通過 | $F$ 可進入 $R_{\mathfrak p}$ ，但 $1/u$ 不可 |
| H6：保守實現 | 通過 | 移除證書後回到標準局部化結果 |

## 37. 六律結果

| X 基本律 | 結果 |
|---|---|
| 積分形成律 | 修正後通過 |
| 來源保存律 | 通過 |
| 非坍縮律 | 通過 |
| 再積分守衛律 | 通過 |
| 結構微分律 | 通過其診斷版本 |
| 動態整體閉合律 | 僅部分測試 |

## 38. 總判定

本次不輸出：

$$
\operatorname{UnconditionalPass}.
$$

也不輸出：

$$
\operatorname{Failure}.
$$

而是：

$$
\boxed{
\operatorname{PassWithCoreRevision}.
}
$$

核心概念——來源、非坍縮、關係類型、上下文與守衛——經受住測試。

但第一版：

$$
\text{原始分數}
\longrightarrow
\text{分母合法}
\longrightarrow
\text{X 分數}
\longrightarrow
\text{商化}
$$

的單線流程必須改寫為：

$$
\boxed{
\text{語法形成}
\longrightarrow
\text{環境商類形成}
\longrightarrow
\text{目標合法代表搜尋}
\longrightarrow
\text{目標實現}
\longrightarrow
\text{再積分守衛}.
}
$$

---

# 第十一部　下一輪實驗

## 39. 一般局部化

下一步可將：

$$
R_u
$$

推廣為任意乘法閉集：

$$
S^{-1}R.
$$

測試：

- 不同 $S$ 之間的上下文轉送；
- 飽和閉包；
- 零因子下的局部化等價；
- 非整域中的等價關係；
- 商類合法代表搜尋。

## 40. 射影直線

再下一步可取：

$$
\mathbb P^1(K_0).
$$

使用兩張仿射圖：

$$
U_0
\cong
\mathbb A^1,
$$

$$
U_1
\cong
\mathbb A^1,
$$

測試：

- 分母換圖；
- 無窮遠點；
- 值域邊界；
- 同一射影點的不同分數代表；
- 齊次比例與普通商的關係型別差異。

## 41. 為何暫不進入連分數

本輪已證明有限形成層仍有必要修正。

若此時直接進入：

$$
F_0
\rightsquigarrow
F_1
\rightsquigarrow
\cdots
\rightsquigarrow
F_{\omega},
$$

會把代表合法性、商類形成、上下文轉送與極限一致性同時混在一起。

因此應先完成一般局部化與射影換圖，再測試遞歸分數。

---

# 42. 結論

第一次純數學實戰沒有證明 X 分數結構微積分產生了新的代數定理。

但它成功完成了一件更基礎的工作：找出第一版形式系統會在哪裡判錯。

原始分數：

$$
E
=
\frac{uv}{u}
$$

在局部環 $R_{\mathfrak p}$ 中不是合法直接表示，因為：

$$
u
\in
\mathfrak p.
$$

然而：

$$
[E]_K
=
\left[
\frac{v}{1}
\right]
\in
R_{\mathfrak p}.
$$

因此：

$$
\boxed{
\text{表示不合法}
\not\Rightarrow
\text{商類不存在}.
}
$$

這逼出 X 分數理論的第一個實戰修正：

$$
\boxed{
\operatorname{RepLegal}_{\Gamma}(E)
\neq
\operatorname{ClassLegal}_{\Gamma}([E]).
}
$$

並進一步要求：

$$
\boxed{
\Gamma_{\mathrm{amb}}
\neq
\Gamma_{\mathrm{tar}}
}
$$

可以被正式記錄。

因此，本次實驗的真正成果不是約分本身，而是建立：

1. 語法形成；
2. 環境商類形成；
3. 特定代表合法；
4. 商類目標實現；
5. 正規化轉送；
6. 來源保存；
7. 再積分守衛；

七個不同但可連接的判定位置。

最終判定為：

$$
\boxed{
\text{X 分數核心方向成立，}
\quad
\text{但形成律必須由單上下文改為雙上下文、四判定系統。}
}
$$

這是一個正面結果，因為它不是靠理論自我解釋通過，而是由標準交換代數迫使理論接受可檢查的修正。

---

## 附錄 A：最小證書

### A.1 原表示證書

$$
\operatorname{Cert}(E)
=
\left\langle
\operatorname{Src}=(uv,u),
\rho=/_{\mathrm{quot}},
\Gamma_{\mathrm{amb}}=K,
\Gamma_{\mathrm{tar}}=R_{\mathfrak p},
\operatorname{RepLegal}=\operatorname{No},
\operatorname{ClassLegal}=\operatorname{Yes},
\operatorname{AlternativeRep}=(v,1)
\right\rangle.
$$

### A.2 真逆元障礙證書

$$
\operatorname{Cert}(G)
=
\left\langle
\operatorname{Src}=(1,u),
\rho=/_{\mathrm{quot}},
\Gamma_{\mathrm{amb}}=K,
\Gamma_{\mathrm{tar}}=R_{\mathfrak p},
\operatorname{RepLegal}=\operatorname{No},
\operatorname{ClassLegal}=\operatorname{No},
\operatorname{AlternativeRep}=\varnothing
\right\rangle.
$$

---

## 附錄 B：一句話結果

> **一個分數表示可以在目標上下文中不合法，而它所代表的商類仍能透過另一個合法代表存在；因此，X 分數形成律必須區分表示合法性與商類可實現性。**

