# 修正型線性化：從仿射運算到 Correction Field
## ——log-sum-exp、log-diff-exp 與結構殘餘的統一形式

**English Title:** *Corrected Linearization from Affine Maps to Correction Fields: A Unified Formalism for Log-Sum-Exp, Log-Diff-Exp, and Structural Residuals*

**作者：** Neo.K  
**機構：** EveMissLab / 一言諾科技有限公司  
**系列：** Operation Translation Series A — Paper 03  
**版本：** v0.1  
**日期：** 2026-08-10

---

## 摘要

Series A Paper 01 建立了判定域下的運算轉譯框架，

$$
T(\mu(x,y))=\nu(Tx,Ty),
$$

Paper 02 則以自然對數證明正實數乘法可被全域、精確、可逆地轉成加法：

$$
\ln(xy)=\ln x+\ln y.
$$

然而，大多數真正的數學與工程運算並不如此理想。當原運算包含加法、偏移、仿射項、非交換效應或其他不能被目標運算完全吸收的結構時，精確加法化通常失敗。這時最直接的形式是：

$$
\boxed{
T(\mu(x,y))
=
\nu(Tx,Ty)+C_T(x,y),
}
$$

其中 $C_T$ 稱為結構修正、結構殘餘或 correction。

本文的目標不是宣稱「任何失敗都可以補一個 correction」，因為若允許 $C_T$ 任意複雜，則上式只是恆等式重寫：

$$
C_T=T\mu-\nu(T\times T),
$$

不具有任何簡化意義。本文真正關心的是：**在什麼條件下，correction 本身比原始運算低成本、低維、可控、可壓縮、可漸近展開、可局部查表或具有穩定的結構類？**

本文首先定義 correction field：

$$
C_T:\Omega_\mu\to Y,
$$

並提出 correction class：

$$
\mathscr C,
$$

用來限制允許的結構殘餘。只有當：

$$
C_T\in\mathscr C
$$

且總計算成本低於原運算或帶來結構性優勢時，才稱為有意義的修正型線性化。

本文以三個標準案例建立此理論。第一，對正實數仿射映射

$$
f(x)=ax+b,
$$

有：

$$
\ln(ax+b)
=
\ln x+\ln a
+
\ln\left(1+\frac{b}{ax}\right),
$$

因此 correction 為：

$$
C_{a,b}(x)
=
\ln\left(1+\frac{b}{ax}\right).
$$

第二，對正值加法：

$$
x+y,
$$

在 log-domain 中可寫成：

$$
\ln(x+y)
=
m+\ln\left(
e^{L_x-m}+e^{L_y-m}
\right),
$$

其中：

$$
m=\max(L_x,L_y).
$$

這是 log-sum-exp 類 correction。第三，對 $x>y>0$：

$$
\ln(x-y)
=
L_x+\ln\left(
1-e^{L_y-L_x}
\right),
$$

形成 log-diff-exp correction，並顯示 subtraction 的 singular boundary 出現在：

$$
L_y-L_x\to0^-.
$$

本文進一步提出 correction 的六個結構指標：幅度、維度、平滑性、衰減性、可組合性與計算成本，並建立一個第一版「非空洞化準則」：若 correction 需要重新計算與原始運算等價或更困難的完整資訊，則不應視為成功線性化；若 correction 可被有限參數、局部狀態、低階展開或結構 primitive 表達，則其具有真正方法論價值。

最後，本文把 correction 從「數值誤差」中分離。結構 correction 是為保存原運算在目標座標下無法被吸收的真實數學內容；數值誤差則是有限精度實作產生的近似偏差。二者必須在理論與 Runtime 中被分開追蹤。

本文因此把 Series A 從：

$$
\text{Exact Additivization}
$$

擴張為：

$$
\boxed{
\text{Exact}
\;\cup\;
\text{Corrected}
\;\cup\;
\text{Local/Approximate}.
}
$$

並為 Paper 04 的離散精確模型、Paper 05 的局部／流形擴張與 Paper 06 的非交換結構 correction 建立共同形式語言。

**關鍵詞：** Correction Field、修正型線性化、log-sum-exp、log-diff-exp、仿射轉譯、結構殘餘、運算簡化、判定域、數值穩定、Logarithmic Number System

---

# 1. 從 Exact 到 Corrected

Paper 01 的精確轉譯形式為：

$$
T(\mu(x,y))
=
\nu(Tx,Ty).
$$

最理想的情況是：

$$
\nu(u,v)=u+v.
$$

即：

$$
T(\mu(x,y))
=
T(x)+T(y).
$$

Paper 02 的正實數乘法正是如此：

$$
\ln(xy)=\ln x+\ln y.
$$

但若：

$$
\mu
$$

含有一個不能被目標加法結構吸收的部分，

則一般會得到：

$$
T(\mu(x,y))
-
T(x)-T(y)
\neq0.
$$

這個非零量不應立即被稱為「誤差」。

因為即使使用無限精度、完全符號化計算，

它仍然可能不為零。

因此本文定義：

$$
\boxed{
C_T(x,y)
=
T(\mu(x,y))
-
\nu(Tx,Ty).
}
$$

它描述的不是 implementation error，

而是：

> **原始運算經 $T$ 轉譯後，相對於指定目標運算 $\nu$ 所留下的結構差異。**

---

# 2. Correction Field 的定義

## 定義 2.1

設：

$$
\mu:\Omega_\mu\to X
$$

為部分運算，

$$
T:X\to Y
$$

為轉譯，

$$
\nu:\Omega_\nu\to Y
$$

為目標運算。

對所有同時合法的：

$$
(x,y)\in\Omega_\mu
$$

定義：

$$
\boxed{
C_{T,\nu}(x,y)
=
T(\mu(x,y))
-
\nu(Tx,Ty).
}
$$

若 $Y$ 為向量空間或可加減的 Abelian group，

則上式為良定義。

本文簡寫：

$$
C_T
$$

或：

$$
C.
$$

---

## 2.2 Correction Field

當：

$$
C_T
$$

隨：

$$
(x,y)
$$

在判定域中變化時，

本文稱其為：

$$
\boxed{
\text{Correction Field}.
}
$$

這裡的 field 是「定義在狀態域上的結構修正場」，

不必等同於代數中的 field / 域。

為避免歧義，

正式數學敘述中可使用：

**structural correction map**

而「Correction Field」保留為 Series A 的方法論名稱。

---

# 3. Correction 不能任意

如果不限制：

$$
C_T,
$$

則對任何：

$$
T,\mu,\nu
$$

都可以定義：

$$
C_T=T\mu-\nu(T\times T).
$$

因此：

$$
T\mu=\nu(T\times T)+C_T
$$

永遠成立。

這顯然會導致理論空洞化。

所以真正問題不是：

> 是否存在 correction？

而是：

$$
\boxed{
C_T
\text{ 是否落在一個事前限制、低複雜度且可利用的結構類中？}
}
$$

---

# 4. Correction Class

定義：

$$
\mathscr C
$$

為允許的 correction class。

例如：

$$
\mathscr C_{\mathrm{const}}
$$

表示常數修正，

$$
\mathscr C_{\mathrm{bounded}}
$$

表示有界修正，

$$
\mathscr C_{\mathrm{poly},n}
$$

表示至多 $n$ 階多項式修正，

$$
\mathscr C_{\mathrm{table},N}
$$

表示有限查表修正，

$$
\mathscr C_{\mathrm{asymp},n}
$$

表示具有 $n$ 階漸近展開，

或：

$$
\mathscr C_{\mathrm{sparse}}
$$

表示只在有限／稀疏條件下啟動。

---

# 5. 修正型可線性化

## 定義 5.1

若存在：

$$
T
$$

及：

$$
\nu\in\mathscr N
$$

使：

$$
T(\mu(x,y))
=
\nu(Tx,Ty)+C_T(x,y),
$$

並且：

$$
C_T\in\mathscr C,
$$

則稱：

$$
\mu
$$

相對於：

$$
(T,\nu,\mathscr C)
$$

為：

$$
\boxed{
\text{Corrected Linearizable}.
}
$$

---

# 6. 第一個標準模型：仿射運算

考慮：

$$
f(x)=ax+b
$$

並假設：

$$
x>0,
\qquad
a>0,
\qquad
ax+b>0.
$$

令：

$$
T(x)=\ln x.
$$

則：

$$
ax+b
=
ax
\left(
1+\frac{b}{ax}
\right).
$$

因此：

$$
\ln(ax+b)
=
\ln a+\ln x+
\ln\left(
1+\frac{b}{ax}
\right).
$$

令：

$$
\boxed{
C_{a,b}(x)
=
\ln\left(
1+\frac{b}{ax}
\right).
}
$$

得到：

$$
\boxed{
T(f(x))
=
T(x)+\ln a+C_{a,b}(x).
}
$$

---

# 7. 仿射 correction 的合法域

Correction：

$$
C_{a,b}(x)
=
\ln\left(
1+\frac{b}{ax}
\right)
$$

要求：

$$
1+\frac{b}{ax}>0.
$$

這等價於：

$$
ax+b>0.
$$

因此 correction 的合法域不是額外隨意產生，

而正好反映原本：

$$
\ln(ax+b)
$$

的轉譯合法性。

所以：

$$
\boxed{
\Omega_C
=
\Omega_{T\circ f}
}
$$

在此案例成立。

這顯示 correction field 本身也必須有判定域。

---

# 8. 當 $b=0$

若：

$$
b=0,
$$

則：

$$
f(x)=ax.
$$

此時：

$$
C_{a,0}(x)
=
\ln1
=
0.
$$

因此：

$$
\ln(ax)
=
\ln a+\ln x.
$$

也就是：

$$
\boxed{
\text{Corrected}
\rightarrow
\text{Exact}
}
$$

在：

$$
b\to0
$$

時自然退化。

這是一個好 correction 應具有的性質：

> 當造成非線性的原結構消失時，correction 也應消失。

---

# 9. 仿射 correction 的漸近衰減

若：

$$
\left|
\frac{b}{ax}
\right|
\ll1,
$$

令：

$$
u=\frac{b}{ax}.
$$

有：

$$
\ln(1+u)
=
u-\frac{u^2}{2}+\frac{u^3}{3}-\cdots.
$$

因此：

$$
C_{a,b}(x)
=
\frac{b}{ax}
-
\frac{b^2}{2a^2x^2}
+
\frac{b^3}{3a^3x^3}
-\cdots.
$$

所以：

$$
\boxed{
C_{a,b}(x)
\sim
\frac{b}{ax}
}
$$

當：

$$
x\to\infty.
$$

這意味：

$$
C_{a,b}(x)\to0.
$$

因此：

$$
\ln(ax+b)
\to
\ln x+\ln a
$$

在大 $x$ 區域逐漸接近純 additive translation。

---

# 10. Correction 的導數

對：

$$
C(x)
=
\ln\left(
1+\frac{b}{ax}
\right),
$$

可以寫：

$$
C(x)=\ln(ax+b)-\ln(ax).
$$

所以：

$$
C'(x)
=
\frac{a}{ax+b}
-
\frac1x.
$$

整理得：

$$
\boxed{
C'(x)
=
-\frac{b}{x(ax+b)}.
}
$$

若：

$$
a>0,
\qquad
b>0,
$$

則：

$$
C'(x)<0.
$$

所以 correction 隨 $x$ 增大單調下降。

這不是單純「有 correction」，

而是 correction 的幾何具有清晰規律。

---

# 11. Correction 的曲率

再微分：

$$
C''(x)
=
\frac{b(2ax+b)}
{x^2(ax+b)^2}.
$$

在：

$$
a,b,x>0
$$

下：

$$
C''(x)>0.
$$

因此：

$$
C
$$

單調下降且凸。

這是第一個真正的 correction geometry 範例。

---

# 12. 一般二元加法

現在考慮：

$$
\mu(x,y)=x+y,
$$

且：

$$
x,y>0.
$$

令：

$$
L_x=\ln x,
\qquad
L_y=\ln y.
$$

如果仍想在 log-space 計算：

$$
x+y,
$$

則：

$$
x+y=e^{L_x}+e^{L_y}.
$$

直接取 log：

$$
\ln(x+y)
=
\ln\left(
e^{L_x}+e^{L_y}
\right).
$$

這不是：

$$
L_x+L_y.
$$

---

# 13. Log-Sum-Exp

令：

$$
m=\max(L_x,L_y).
$$

則：

$$
e^{L_x}+e^{L_y}
=
e^m
\left(
e^{L_x-m}
+
e^{L_y-m}
\right).
$$

所以：

$$
\boxed{
\ln(x+y)
=
m+
\ln\left(
e^{L_x-m}
+
e^{L_y-m}
\right).
}
$$

對兩項而言，

若假設：

$$
L_x\geq L_y,
$$

則：

$$
m=L_x
$$

且：

$$
\boxed{
\ln(x+y)
=
L_x+
\ln\left(
1+e^{L_y-L_x}
\right).
}
$$

---

# 14. 把 log-sum-exp 看成 correction

令：

$$
d=L_y-L_x\leq0.
$$

定義：

$$
\boxed{
C_+(d)
=
\ln(1+e^d).
}
$$

則：

$$
\boxed{
\ln(x+y)
=
\max(L_x,L_y)
+
C_+\left(
-|L_x-L_y|
\right).
}
$$

這裡 additive core 不再是：

$$
L_x+L_y,
$$

而是：

$$
\max(L_x,L_y).
$$

因此 Paper 03 的 corrected framework 不應被限制為：

$$
\nu(u,v)=u+v.
$$

更一般地：

$$
\boxed{
T\mu
=
\nu(Tx,Ty)+C_T.
}
$$

其中：

$$
\nu
$$

可以是指定的低成本 primitive。

---

# 15. 為什麼這仍然是「線性化／簡化」

在 log-domain 中，

原本需要處理：

$$
x+y
=
e^{L_x}+e^{L_y}.
$$

利用最大值抽取後，

correction 只依賴：

$$
d=|L_x-L_y|.
$$

也就是：

$$
\boxed{
C_+
=
C_+(d).
}
$$

原本二維輸入：

$$
(L_x,L_y)
$$

的非線性 correction，

被壓縮成一個一維差值函數。

因此它具有真正結構簡化：

$$
\boxed{
\dim C
<
\dim \Omega_{\mu}.
}
$$

這是 correction 非空洞化的一個強烈正面訊號。

---

# 16. $C_+$ 的界

因：

$$
d\geq0,
$$

寫：

$$
C_+(d)
=
\ln(1+e^{-d}).
$$

則：

$$
0<C_+(d)\leq\ln2.
$$

且：

$$
C_+(0)=\ln2.
$$

當：

$$
d\to\infty,
$$

有：

$$
C_+(d)\to0.
$$

所以：

$$
\boxed{
0<C_+(d)\leq\ln2.
}
$$

這表示 positive addition 的 correction 全域有界。

---

# 17. $C_+$ 的衰減

若：

$$
d\gg1,
$$

則：

$$
e^{-d}\ll1.
$$

因此：

$$
C_+(d)
=
e^{-d}
-\frac12e^{-2d}
+\frac13e^{-3d}
-\cdots.
$$

所以：

$$
\boxed{
C_+(d)
\sim
e^{-d}.
}
$$

因此兩個數在 log magnitude 上差距越大，

較小項對總和的 correction 呈 exponential decay。

這是非常強的壓縮性。

---

# 18. Softmax 權重自然出現

對：

$$
F(L_x,L_y)
=
\ln(e^{L_x}+e^{L_y}),
$$

有：

$$
\frac{\partial F}{\partial L_x}
=
\frac{e^{L_x}}
{e^{L_x}+e^{L_y}},
$$

$$
\frac{\partial F}{\partial L_y}
=
\frac{e^{L_y}}
{e^{L_x}+e^{L_y}}.
$$

兩者和為：

$$
1.
$$

因此 log-sum-exp 的梯度正是 normalized exponential weight。

這說明 correction 不只是計算技巧，

還具有自然的幾何／權重結構。

---

# 19. 多項 log-sum-exp

對：

$$
x_i>0,
\qquad
L_i=\ln x_i,
$$

有：

$$
\ln\left(
\sum_{i=1}^n x_i
\right)
=
\ln\left(
\sum_{i=1}^n e^{L_i}
\right).
$$

令：

$$
m=\max_iL_i.
$$

則：

$$
\boxed{
\operatorname{LSE}(L_1,\dots,L_n)
=
m+
\ln
\left(
\sum_{i=1}^n
e^{L_i-m}
\right).
}
$$

所有：

$$
L_i-m\leq0,
$$

因此 exponential 不再處理巨大正輸入。

這個 shifted form 是標準數值實作形式。

---

# 20. Log-Diff-Exp

現在考慮：

$$
x-y
$$

且：

$$
x>y>0.
$$

令：

$$
L_x=\ln x,
\qquad
L_y=\ln y.
$$

則：

$$
x-y
=
e^{L_x}
\left(
1-e^{L_y-L_x}
\right).
$$

因此：

$$
\boxed{
\ln(x-y)
=
L_x
+
\ln\left(
1-e^{L_y-L_x}
\right).
}
$$

令：

$$
d=L_x-L_y>0.
$$

得到：

$$
\boxed{
C_-(d)
=
\ln(1-e^{-d}).
}
$$

所以：

$$
\boxed{
\ln(x-y)
=
\max(L_x,L_y)
+
C_-(|L_x-L_y|)
}
$$

在已知符號次序的正值 subtraction 中成立。

---

# 21. $C_-$ 的 singular boundary

當：

$$
d\to0^+,
$$

有：

$$
e^{-d}\to1^-.
$$

因此：

$$
1-e^{-d}\to0^+.
$$

故：

$$
\boxed{
C_-(d)\to-\infty.
}
$$

這正對應：

$$
x-y\to0^+.
$$

所以 singularity 不是 numerical bug。

它是原始運算結果正在接近 log chart 的零邊界。

---

# 22. 大差距下的 subtraction correction

若：

$$
d\gg1,
$$

則：

$$
e^{-d}\ll1.
$$

利用：

$$
\ln(1-z)
=
-z-\frac{z^2}{2}-\frac{z^3}{3}-\cdots,
$$

得到：

$$
C_-(d)
=
-e^{-d}
-\frac12e^{-2d}
-\frac13e^{-3d}
-\cdots.
$$

所以：

$$
\boxed{
C_-(d)
\sim
-e^{-d}.
}
$$

和 addition correction 一樣，

當一項遠小於另一項時，

correction 指數級衰減。

---

# 23. Addition 與 subtraction correction 的對偶

定義：

$$
C_\pm(d)
=
\ln(1\pm e^{-d}).
$$

其中：

$$
C_+
$$

對所有：

$$
d\geq0
$$

有限，

而：

$$
C_-
$$

只對：

$$
d>0
$$

合法。

這給出一個簡潔的 correction family：

$$
\boxed{
C_\sigma(d)
=
\ln(1+\sigma e^{-d}),
\qquad
\sigma\in\{+1,-1\}.
}
$$

其中：

- $\sigma=+1$ 對應加法；
- $\sigma=-1$ 對應正值差。

---

# 24. Correction Field 的六個指標

為避免 correction 變成任意垃圾桶，

本文提出六個第一版結構指標。

## 24.1 幅度

定義：

$$
M_C
=
\sup_{\Omega_C}\|C\|.
$$

若有限，

則 correction globally bounded。

例如：

$$
C_+
$$

有：

$$
M_C=\ln2.
$$

---

## 24.2 有效維度

若：

$$
C(x,y)
$$

實際只依賴：

$$
\phi(x,y)\in\mathbb R^k
$$

且：

$$
k
<
\dim(x,y),
$$

則 correction 具有 dimension reduction。

log-sum-exp 的 two-term correction：

$$
C_+(|L_x-L_y|)
$$

就是典型例子。

---

## 24.3 平滑性

研究：

$$
C\in C^k,
$$

或 analytic / Lipschitz / piecewise smooth。

平滑 correction 容易：

- 插值；
- 近似；
- 微分；
- 誤差控制。

---

## 24.4 衰減性

若存在：

$$
\|C(z)\|
\to0
$$

在某種尺度極限，

則表示主運算在該 regime 漸近成為 exact linearization。

例如：

$$
C_{a,b}(x)\to0
$$

當：

$$
x\to\infty.
$$

---

## 24.5 可組合性

若連續多次 operation 的 correction 能以有限狀態遞推：

$$
C_{n+1}
=
\Phi(C_n,z_n),
$$

而不必重新展開完整歷史，

則 correction 具有 compositional closure。

這對 Runtime 特別重要。

---

## 24.6 計算成本

令：

$$
K(\mu)
$$

為原運算成本，

$$
K(T,\nu,C,T^{-1})
$$

為轉譯路徑成本。

若：

$$
K(T,\nu,C,T^{-1})
<
K(\mu)
$$

或即使成本相近但帶來：

- 更高 dynamic range；
- 更容易 parallelize；
- 更容易 cache；
- 更容易誤差控制；

則修正型線性化仍可能有工程價值。

---

# 25. 非空洞化準則

本文提出第一版：

## Principle 25.1

一個 correction-based translation 只有在至少滿足以下一項時，才應被視為非空洞化：

1. correction 的輸入維度低於原運算；
2. correction 有界；
3. correction 可由有限參數族描述；
4. correction 在主要 regime 衰減；
5. correction 可由低階展開逼近；
6. correction 可有限查表；
7. correction 具有稀疏啟動條件；
8. correction 具有封閉組合律；
9. correction 計算成本顯著低於原始運算；
10. correction 揭露了原運算的結構分類或 obstruction。

如果以上皆不成立，

且：

$$
C_T
$$

本質上等價於重新執行：

$$
\mu,
$$

則：

$$
T\mu=\nu T+C
$$

只是一種符號搬家。

---

# 26. Correction Complexity Ratio

為提供更明確的工程判定，

定義：

$$
\boxed{
\rho_C
=
\frac{
K(C)+K(\nu)+K(T)+K(T^{-1})
}{
K(\mu)
}.
}
$$

若：

$$
\rho_C<1,
$$

則轉譯在指定 cost model 下具有直接成本優勢。

若：

$$
\rho_C\geq1,
$$

仍不能立刻判定無價值，

因為可能換取：

- 更低 overflow risk；
- 更高可並行性；
- 更簡潔的 global error bound；
- 更小記憶體；
- 更適合特定硬體。

因此：

$$
\rho_C
$$

只是第一個 cost indicator，

不是唯一判準。

---

# 27. Structural Residual 與 Numerical Error

這是本文最重要的區分之一。

## 結構殘餘

$$
C_T
=
T\mu-\nu T.
$$

即使無限精度，

也可能：

$$
C_T\neq0.
$$

它是數學結構。

## 數值誤差

實作中：

$$
\widehat C
=
C+\varepsilon_C.
$$

其中：

$$
\varepsilon_C
$$

是有限精度、近似或查表造成的偏差。

因此完整實作應寫：

$$
\boxed{
\widehat{T\mu}
=
\widehat\nu
+
C
+
\varepsilon.
}
$$

而不是把：

$$
C+\varepsilon
$$

混成一個「誤差」。

---

# 28. Correction 的拓樸判定域

對 correction：

$$
C_T:\Omega_C\to Y,
$$

應獨立記錄：

$$
\Omega_C.
$$

例如 subtraction：

$$
C_-(d)=\ln(1-e^{-d})
$$

只在：

$$
d>0
$$

合法。

當：

$$
d=0,
$$

原始結果：

$$
x-y=0
$$

離開非零 log chart。

因此：

$$
d=0
$$

不是「公式突然壞掉」，

而是 chart transition boundary。

---

# 29. Correction 與局部 chart

若：

$$
C_T
$$

在某區域變得巨大或 singular，

可以考慮切換 chart。

所以未來可以定義：

$$
\mathcal U
=
\{U_\alpha\},
$$

每個區域使用不同：

$$
(T_\alpha,\nu_\alpha,C_\alpha).
$$

例如：

- 大比例差距使用 log-diff-exp；
- 近 cancellation 使用 direct residual chart；
- 零點附近使用 zero-state chart。

因此：

$$
\boxed{
\text{Correction Field}
}
$$

自然連到 Paper 05 的 atlas。

---

# 30. 多運算系統

實際數學不只有單一：

$$
\mu.
$$

通常存在：

$$
\mathcal O
=
\{\mu_1,\mu_2,\dots,\mu_k\}.
$$

一個轉譯：

$$
T
$$

可能對：

$$
\mu_1
$$

是 exact：

$$
C_1=0,
$$

對：

$$
\mu_2
$$

需要有界 correction，

對：

$$
\mu_3
$$

卻需要 singular correction。

例如 log coordinate：

$$
\begin{aligned}
\times &: C=0,\\
\div &: C=0,\\
\text{power} &: C=0,\\
+ &: C=C_+,\\
- &: C=C_-.
\end{aligned}
$$

因此轉譯品質不是單一 scalar。

它應該是：

$$
\boxed{
\mathbf C_T
=
(C_1,\dots,C_k).
}
$$

---

# 31. Operation Profile

定義轉譯 $T$ 的運算 profile：

$$
\boxed{
\Pi_T
=
\left[
(\mu_i,\nu_i,\mathscr C_i)
\right]_{i=1}^k.
}
$$

例如 logarithmic coordinate：

$$
\Pi_{\log}
=
\{
\times\mapsto+,
\div\mapsto-,
\text{power}\mapsto\text{scale},
+\mapsto\operatorname{LSE},
-\mapsto\operatorname{LDE}
\}.
$$

這比只問：

> 「這個 representation 好不好？」

精確很多。

---

# 32. Correction Spectrum

可以根據：

$$
C
$$

的結構，定義一個初步光譜：

### Level 0

$$
C=0.
$$

Exact。

### Level 1

常數／有限離散 correction。

### Level 2

單變量 bounded correction。

### Level 3

低維 smooth correction。

### Level 4

局部／分段 correction。

### Level 5

高階 recursive correction。

### Level 6

correction 和原運算幾乎等複雜。

此時線性化價值趨近於零。

這是一個未來可形式化的研究方向。

---

# 33. Correction 與信息保存

若：

$$
T
$$

本身丟失信息，

correction 可能被迫重新攜帶那些遺失資訊。

因此 correction complexity 也可以視為：

> **轉譯造成的信息損失，為了保持運算忠實性所必須支付的回補成本。**

若 $T$ 是雙射，

那 correction 主要反映的是：

$$
\mu
$$

與：

$$
\nu
$$

結構不匹配。

若 $T$ 不是單射，

correction 還可能混入 information loss。

因此兩者應分開。

---

# 34. Correction 與 obstruction

如果某個：

$$
C
$$

無法在任何低階類：

$$
\mathscr C_n
$$

中表達，

那它可能是一個 obstruction signal。

也就是：

$$
\boxed{
\text{correction complexity}
\text{ 可以測量目標線性化與原結構之間的失配程度。}
}
$$

Paper 06 的 BCH commutator hierarchy 正是這種情況的高階範例。

---

# 35. 與 LNS 的關係

Logarithmic Number System 已長期利用：

$$
\log(xy)=\log x+\log y
$$

簡化乘除，

並承認 addition / subtraction 會變成非線性函數。

現代 LNS 實作通常需要：

- lookup table；
- interpolation；
- co-transformation；
- error correction；

處理加減。

本篇不主張發明這些既有工程技巧。

本文真正新增的框架是：

> 把這些非線性加減函數提升為「correction class」案例，並放入一個可以跨越 LNS、仿射轉換、局部幾何與非交換系統的統一分類中。

---

# 36. Correction 的三種角色

目前至少可以區分：

## Type A：Operation-Induced Correction

例如：

$$
ax+b,
$$

中的：

$$
\ln\left(1+\frac{b}{ax}\right).
$$

## Type B：Representation-Induced Correction

某個 representation 為方便計算而引入的 normalization / chart correction。

## Type C：Structure-Induced Correction

由原始代數與目標代數不匹配所產生。

非交換 BCH correction 將屬於此類。

---

# 37. 第一版 Correction Field 公理要求

一個可作為 Series A 正式對象的 correction field，

至少應記錄：

$$
\boxed{
\mathcal C
=
(
\Omega_C,
C,
\mathscr C,
K_C,
R_C
)
}
$$

其中：

- $\Omega_C$：合法域；
- $C$：修正映射；
- $\mathscr C$：結構類；
- $K_C$：成本模型；
- $R_C$：還原／誤差規格。

這讓 correction 成為正式數學／工程介面，

而不是隨手補項。

---

# 38. Corrected Translation Object

因此一個完整修正型轉譯可以寫成：

$$
\boxed{
\mathfrak T_C
=
(
X,Y,
\Omega_\mu,
T,
\nu,
C,
T^{-1}
).
}
$$

其執行流程：

$$
x,y
$$

先進：

$$
T,
$$

再算：

$$
\nu(Tx,Ty),
$$

加入：

$$
C(x,y),
$$

最後：

$$
T^{-1}.
$$

即：

$$
\boxed{
\mu(x,y)
=
T^{-1}
\left(
\nu(Tx,Ty)+C(x,y)
\right).
}
$$

---

# 39. Correction Runtime 雛形

對 Engineering Whitepaper，

這直接對應：

$$
\text{Domain Validator}
$$

$$
\downarrow
$$

$$
\text{Transform Selector}
$$

$$
\downarrow
$$

$$
\text{Linear Core}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Correction Engine}
}
$$

$$
\downarrow
$$

$$
\text{Inverse Transform}
$$

$$
\downarrow
$$

$$
\text{Error / Decision Validator}.
$$

Paper 03 因此正式定義了 Runtime 中 Correction Engine 的數學職責。

---

# 40. 本篇核心命題

本文可以濃縮成八條。

### 命題一

Correction 不是自動等於 error。

### 命題二

任何運算都能形式上定義 correction，

所以 correction 的存在本身沒有 novelty。

### 命題三

必須事先限制：

$$
C\in\mathscr C.
$$

### 命題四

仿射運算在 log-space 中產生：

$$
C_{a,b}(x)
=
\ln\left(1+\frac{b}{ax}\right).
$$

### 命題五

正值加法產生 bounded one-dimensional correction：

$$
C_+(d)
=
\ln(1+e^{-d}).
$$

### 命題六

正值減法產生：

$$
C_-(d)
=
\ln(1-e^{-d}),
$$

且在 cancellation boundary：

$$
d\to0^+
$$

出現必然 singularity。

### 命題七

Correction 是否有價值，應由其維度、平滑性、衰減性、可組合性與成本共同判定。

### 命題八

Correction complexity 可以被視為 source operation 與 target operation 結構失配的一種量。

---

# 41. 限制

本文仍刻意不做幾件事。

第一，尚未為：

$$
K(C)
$$

建立唯一、跨硬體的複雜度定義。

第二，尚未證明 correction spectrum 的分類完備。

第三，尚未建立 correction field 的 sheaf / bundle / module 正式結構。

第四，尚未處理 matrix BCH correction 的完整收斂域。

第五，尚未處理 valuation exact coordinate。

這些分別留給後續 Paper 04–06。

---

# 42. 結論

Paper 02 給出了一個極度理想的模型：

$$
\ln(xy)=\ln x+\ln y.
$$

但一般數學不可能永遠如此乾淨。

本文因此把 Series A 的核心方程由：

$$
\boxed{
T\mu=\nu T
}
$$

擴張成：

$$
\boxed{
T\mu=\nu T+C.
}
$$

這一步的關鍵不是「允許補項」，

而是要求：

$$
C
$$

本身必須：

- 有合法判定域；
- 落在受限 correction class；
- 具有結構規律；
- 可被分析；
- 可被估計；
- 可被壓縮或低成本計算；
- 不得只是把原運算完整藏回去。

仿射映射：

$$
ax+b
$$

提供第一個 state-dependent correction；

log-sum-exp 提供 bounded、低維、指數衰減 correction；

log-diff-exp 則展示 singular boundary 如何對應原始結果跨入 zero chart。

因此 correction 應被理解為：

$$
\boxed{
\text{為保存原運算結構而在簡化座標中必須攜帶的殘餘資訊。}
}
$$

而不是：

$$
\boxed{
\text{計算沒算準留下的誤差。}
}
$$

這個區分將成為 Series A 後續發展的核心。

---

# 參考文獻

1. Pierre Blanchard, Desmond J. Higham, Nicholas J. Higham, *Accurate Computation of the Log-Sum-Exp and Softmax Functions*, 2019/2020.
2. SciPy Documentation, `scipy.special.logsumexp`.
3. Thanh Son Nguyen, Alexey Solovyev, Ganesh Gopalakrishnan, *Rigorous Error Analysis for Logarithmic Number Systems*, 2024.
4. Syed Asad Alam, James Garland, David Gregg, *Low precision logarithmic number systems: Beyond base-2*, 2021.
5. NIST DLMF, Chapter 4, *Logarithm, Exponential, Powers*.

---

## Series A 銜接

**下一篇：Paper 04**

**《離散精確模型：估值座標、指數格與有限域精確還原》**

下一篇將切換到完全不同但非常重要的模型：

$$
\mathbb Q_{>0}^{\times}
\cong
\bigoplus_{p\in\mathbb P}\mathbb Z,
$$

研究：

- prime-exponent coordinate；
- valuation；
- exponent lattice；
- exact discrete representation；
- finite-domain nearest-state recovery；

並回答一個核心問題：

> 是否可以在完全不依賴連續近似 logarithm 的情況下，仍然把乘除法轉成純加減？
