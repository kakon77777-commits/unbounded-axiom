# X 分數結構微積分純數學實戰 II：一般局部化、 $S$-湮滅與強迫來源坍縮

**英文題名**：*X-Fraction Structural Calculus: Pure Mathematics Experiment II — General Localization, $S$-Annihilation, and Forced Source Collapse*

**版本**：v0.1  
**日期**：2026-07-26  
**系列位置**：X 分數結構微積分純數學實戰 II  
**前篇**：《X 分數結構微積分純數學實戰 I：可去表示缺口、局部化與來源非坍縮》  
**性質**：純數學壓力測試、核心公理修正案、後續改版依據  
**狀態**：可供內部檢驗；尚非最終公理版

---

## 摘要

本文對 X 分數結構微積分進行第二次純數學實戰。第一次實戰在整域中指出：一個分數表示在目標局部化中不合法，不代表其商類不能由另一個合法代表實現。因此，語法形成、環境商類、代表合法性與目標實現必須分層。

本次刻意移除整域假設，取任意域 $k$ ，並令：

$$
R
=
k[X,Y]/(XY).
$$

以 $x,y$ 表示 $X,Y$ 在 $R$ 中的像。考察兩個乘法閉集：

$$
S_x
=
\{1,x,x^2,\ldots\},
$$

$$
S_y
=
\{1,y,y^2,\ldots\}.
$$

由於：

$$
xy=0,
$$

但：

$$
x\neq 0,
\qquad
y\neq 0,
$$

在 $S_x^{-1}R$ 中會發生：

$$
\frac{y}{1}
=
\frac{0}{1},
$$

而在 $S_y^{-1}R$ 中則有：

$$
\frac{x}{1}
=
\frac{0}{1}.
$$

這不是數值投影造成的資訊壓縮，而是標準局部化等價關係本身強迫產生的商類識別。

一般交換環中的局部化等價不是單純的交叉乘積相等：

$$
at=bs,
$$

而是：

$$
\boxed{
(a,s)\sim_S(b,t)
\quad\Longleftrightarrow\quad
\exists u\in S,\;
u(at-bs)=0.
}
$$

因此，本次實驗得到第二項核心修正：

$$
\boxed{
\text{X 非坍縮}
\neq
\text{禁止所有商化識別}.
}
$$

較精確的版本應為：

$$
\boxed{
\text{X 非坍縮}
=
\text{禁止無關係宣告、無證書或跨層回推的識別}.
}
$$

來源不同的表示可以在局部化商類中合法相等；X 系統必須接受此等式，同時保存其來源差異、湮滅元素、目標上下文與識別理由。來源保存因而必須區分「來源可追蹤」、「來源可重建」與「來源映射具單射性」三個強度。前者可由外加證書達成；後兩者在本例中一般不成立。

本例亦顯示， $S_x^{-1}R$ 與 $S_y^{-1}R$ 無法在保持非零環的條件下直接合併，因為由 $x$ 與 $y$ 生成的乘法閉包包含：

$$
xy=0.
$$

因此，再積分守衛不只是形式檢查，而會排除真正不相容的局部上下文。

本文沒有產生新的交換代數定理。其新增價值在於：以 X 分數的語言，把局部化核、來源軌跡、強迫坍縮、飽和分母、上下文轉送與再積分失敗整理為同一個可稽核的跨層判定系統。

**關鍵詞**：X 積分；X 分數；一般局部化；零因子； $S$-湮滅；來源保存；非坍縮；飽和分母；上下文轉送；再積分守衛

---

# 第一部　結果先行

## 0.1 本次測試的最短結論

令：

$$
R=k[X,Y]/(XY),
$$

並取：

$$
S_x=\{x^n:n\geq 0\}.
$$

則：

$$
y\neq 0
\quad\text{於 }R,
$$

但：

$$
\frac{y}{1}
=
\frac{0}{1}
\quad\text{於 }S_x^{-1}R.
$$

其等價證書不是：

$$
y=0,
$$

而是：

$$
x(y-0)=0,
\qquad
x\in S_x.
$$

因此，標準代數要求 X 系統同時承認：

$$
\boxed{
y\neq_R 0
\quad\land\quad
\lambda_x(y)=\lambda_x(0).
}
$$

其中：

$$
\lambda_x:R\longrightarrow S_x^{-1}R
$$

是標準局部化映射。

## 0.2 第一項新漏洞

若 X 分數系統把一般環中的分數等價定義為：

$$
(a,s)\sim(b,t)
\quad\Longleftrightarrow\quad
at=bs,
$$

則此定義只在適當的正則性條件下成立。

一般情況必須改為：

$$
\boxed{
(a,s)\sim_S(b,t)
\quad\Longleftrightarrow\quad
\exists u\in S,\;
u(at-bs)=0.
}
$$

前一版本不是普遍錯誤，而是把整域模型誤當成一般交換環模型。

## 0.3 第二項新漏洞

若「來源非坍縮律」被強讀為：

$$
a\neq b
\Longrightarrow
\lambda_S(a)\neq\lambda_S(b),
$$

則本例直接反駁它。

局部化映射不一定單射。其核為：

$$
\ker(\lambda_S)
=
\left\{
r\in R:
\exists s\in S,\;sr=0
\right\}.
$$

因此，強非坍縮只能在下列條件成立時使用：

$$
\ker(\lambda_S)=0.
$$

## 0.4 必須採用的新讀法

X 非坍縮律應改寫為四項要求：

1. 商關係要求相等時，接受商類相等；
2. 商類相等不得無條件回推來源相等；
3. 來源不同而商類相等時，保存識別證書；
4. 只有證明目標映射單射後，才可宣稱強來源非坍縮。

濃縮為：

$$
\boxed{
[F]_S=[G]_S
\nRightarrow
F\equiv_{\mathrm{src}}G.
}
$$

以及：

$$
\boxed{
F\not\equiv_{\mathrm{src}}G
\;\land\;
[F]_S=[G]_S
\Longrightarrow
\operatorname{CollapseCert}_S(F,G).
}
$$

## 0.5 總判定

本輪總判定為：

$$
\boxed{
\operatorname{PassWithCoreRevision}.
}
$$

但本次修正比第一次更深。

第一次修正的是：

$$
\text{表示合法性}
\neq
\text{商類合法性}.
$$

第二次修正的是：

$$
\text{來源差異}
\neq
\text{商類差異}.
$$

---

# 第二部　研究問題與反駁標準

## 1. 核心研究問題

本輪問題是：

> 當局部化作用於含零因子的交換環時，X 分數系統能否接受標準代數所強迫的來源坍縮，同時保留來源軌跡、正確分類分母、判定上下文轉送，並阻止不相容局部化被錯誤再積分？

## 2. 測試假設

### H1：代數保守性

忘卻所有 X 證書後，結果必須回到標準局部化：

$$
U(\widetilde{S^{-1}R})
\cong
S^{-1}R.
$$

### H2：一般局部化等價正確性

系統必須使用：

$$
(a,s)\sim_S(b,t)
\Longleftrightarrow
\exists u\in S,\;u(at-bs)=0.
$$

### H3：來源軌跡保存

即使：

$$
\lambda_S(a)=\lambda_S(b),
$$

仍可在 X 外加層保存：

$$
(a,b,S,u,\text{形成路徑}).
$$

### H4：合法坍縮與非法坍縮可區分

系統必須區分：

$$
\text{有證書的商類識別}
$$

與：

$$
\text{無宣告的來源抹除}.
$$

### H5：分母狀態可分級

系統必須區分：

- 分母直接屬於 $S$ ；
- 分母不屬於 $S$ ，但在 $S^{-1}R$ 中可逆；
- 分母在目標中不可逆；
- 分母在目標中坍縮為零。

### H6：上下文再積分受守衛

若兩個局部化上下文的共同乘法閉包包含零，系統不得宣稱存在非平凡共同局部化。

## 3. 明確失敗條件

若系統出現下列任一結果，本輪即判定失敗：

1. 因 $y\neq 0$ 而拒絕 $y/1=0/1$ 於 $S_x^{-1}R$ ；
2. 由 $y/1=0/1$ 回推 $y=0$ 於 $R$ ；
3. 把來源軌跡說成局部化零元素的內在唯一資料；
4. 使用 $at=bs$ 作為任意交換環中局部化等價的充要條件；
5. 宣稱 $S_x^{-1}R$ 與 $S_y^{-1}R$ 可無條件合併成非零局部化；
6. 宣稱局部化映射永遠單射；
7. 把 $1/(x+y)$ 與 $1/y$ 在 $S_x^{-1}R$ 中判成相同的分母狀態。

---

# 第三部　標準代數基線

## 4. 一般局部化的輸入

令 $R$ 為含單位元的交換環， $S\subseteq R$ 為乘法閉集，滿足：

$$
1\in S,
$$

$$
s,t\in S
\Longrightarrow
st\in S.
$$

若希望局部化保持為非零環，另要求：

$$
0\notin S.
$$

原始分數材料為：

$$
R\times S.
$$

其中 $(a,s)$ 暫記為：

$$
\frac{a}{s}.
$$

## 5. 一般局部化的等價關係

在含零因子的環中，正確等價關係為：

$$
\boxed{
(a,s)\sim_S(b,t)
\Longleftrightarrow
\exists u\in S,\;
u(at-bs)=0.
}
$$

定義交叉缺陷：

$$
\Delta\big((a,s),(b,t)\big)
:=
at-bs.
$$

則：

$$
(a,s)\sim_S(b,t)
\Longleftrightarrow
\exists u\in S,\;
u\Delta\big((a,s),(b,t)\big)=0.
$$

## 6. 為何不能只要求 $at=bs$

若 $R$ 是整域且 $0\notin S$ ，則每個 $u\in S$ 都不是零因子。因此：

$$
u(at-bs)=0
\Longrightarrow
at-bs=0.
$$

此時才可簡化為：

$$
(a,s)\sim_S(b,t)
\Longleftrightarrow
at=bs.
$$

所以：

$$
\boxed{
\text{標準交叉相等}
\text{ 是正則局部化的特例，不是一般定義。}
}
$$

## 7. 等價證書

對兩個原始分數表示：

$$
E=(a,s),
\qquad
F=(b,t),
$$

定義局部化等價證書：

$$
\operatorname{LocEqCert}_S(E,F;u)
$$

成立，若且唯若：

$$
u\in S
$$

且：

$$
u(at-bs)=0.
$$

證書至少包含：

$$
C_{\mathrm{loc}}
=
\left(
S,
u,
at-bs,
u(at-bs)=0
\right).
$$

## 8. 等價關係的傳遞性

假設：

$$
(a,s)\sim_S(b,t)
$$

由 $u\in S$ 證明，並且：

$$
(b,t)\sim_S(c,w)
$$

由 $v\in S$ 證明。

亦即：

$$
u(at-bs)=0,
$$

$$
v(bw-ct)=0.
$$

注意：

$$
w(at-bs)+s(bw-ct)
=
t(aw-cs).
$$

乘上 $uv$ 後：

$$
uvt(aw-cs)=0.
$$

因為：

$$
uvt\in S,
$$

故：

$$
(a,s)\sim_S(c,w).
$$

這說明額外的 $u$ 不是裝飾資料，而是一般局部化等價能成立的必要部分。

## 9. 局部化映射

標準映射為：

$$
\lambda_S:
R
\longrightarrow
S^{-1}R,
$$

$$
\lambda_S(r)
=
\frac{r}{1}.
$$

對 $a,b\in R$ ：

$$
\lambda_S(a)
=
\lambda_S(b)
$$

若且唯若：

$$
\exists u\in S,\;
u(a-b)=0.
$$

## 10. $S$-湮滅核

定義：

$$
\operatorname{Ker}_S(R)
:=
\left\{
r\in R:
\exists s\in S,\;sr=0
\right\}.
$$

本文稱其為 $S$-湮滅核，亦即通常所說的 $S$-torsion 部分。

局部化映射的核正是：

$$
\boxed{
\ker(\lambda_S)
=
\operatorname{Ker}_S(R).
}
$$

因此：

$$
\lambda_S(a)=\lambda_S(b)
\Longleftrightarrow
a-b\in\operatorname{Ker}_S(R).
$$

## 11. 單射性的充要條件

局部化映射具單射性：

$$
\lambda_S
\text{ 單射},
$$

若且唯若：

$$
\operatorname{Ker}_S(R)=0.
$$

等價地：

$$
\forall r\in R,
\quad
\left(
\exists s\in S,\;sr=0
\right)
\Longrightarrow
r=0.
$$

若 $S$ 的每個元素都是非零因子，則此條件成立。

但「 $0\notin S$ 」本身不足以保證單射。

---

# 第四部　測試環

## 12. 節點交叉環

令 $k$ 為任意域，取：

$$
R
=
k[X,Y]/(XY).
$$

記：

$$
x=[X],
\qquad
y=[Y].
$$

則：

$$
xy=0.
$$

另一方面：

$$
x\neq 0,
\qquad
y\neq 0.
$$

因為令 $Y=0$ 可得映射：

$$
R\longrightarrow k[X],
$$

且 $x$ 映至非零的 $X$ 。同理，令 $X=0$ 可證 $y\neq 0$ 。

## 13. 標準形

每個 $r\in R$ 可唯一寫成：

$$
r
=
f(x)+y\,g(y),
$$

其中：

$$
f(x)\in k[x],
\qquad
g(y)\in k[y].
$$

這是因為所有同時含正次方 $x$ 與正次方 $y$ 的單項式都被關係：

$$
xy=0
$$

消去。

## 14. 幾何直觀

$R$ 是兩條座標軸之聯集的座標環。

兩個分支由：

$$
x\text{-軸}
$$

與：

$$
y\text{-軸}
$$

組成，並在原點相交。

局部化於 $x$ 會只保留 $x\neq 0$ 的部分；局部化於 $y$ 則只保留 $y\neq 0$ 的部分。

本輪不依賴此幾何直觀完成證明，但它會解釋為何兩個局部上下文無共同非空重疊。

---

# 第五部　在 $x$ 上局部化

## 15. 乘法閉集 $S_x$

定義：

$$
S_x
=
\{x^n:n\geq 0\}.
$$

由於每個 $x^n$ 都非零：

$$
0\notin S_x.
$$

因此可形成非零局部化：

$$
R_x
:=
S_x^{-1}R.
$$

## 16. $y$ 被強迫坍縮

在 $R$ 中：

$$
xy=0.
$$

而：

$$
x\in S_x.
$$

故：

$$
\operatorname{LocEqCert}_{S_x}
\big((y,1),(0,1);x\big)
$$

成立，因為：

$$
x(y\cdot 1-0\cdot 1)
=
xy
=
0.
$$

所以：

$$
\boxed{
\frac{y}{1}
=
\frac{0}{1}
\quad\text{於 }R_x.
}
$$

## 17. 計算 $\ker(\lambda_x)$

令：

$$
\lambda_x:
R\longrightarrow R_x.
$$

先有：

$$
(y)\subseteq\ker(\lambda_x),
$$

因為：

$$
x\cdot y\,g(y)=0
$$

對所有 $g(y)\in k[y]$ 成立。

反向地，若：

$$
r=f(x)+y\,g(y)
$$

且：

$$
x^n r=0
$$

對某個 $n\geq 1$ 成立，則：

$$
x^n r
=
x^n f(x),
$$

因為：

$$
x^n y\,g(y)=0.
$$

映至 $k[x]$ 後得到：

$$
x^n f(x)=0.
$$

$k[x]$ 是整域，因此：

$$
f(x)=0.
$$

所以：

$$
r\in(y).
$$

結論為：

$$
\boxed{
\ker(\lambda_x)
=(y).
}
$$

## 18. 局部化的顯式模型

有：

$$
R_x
\cong
k[X,X^{-1},Y]/(XY).
$$

因為 $X$ 在此環中可逆，而：

$$
XY=0,
$$

故必有：

$$
Y=0.
$$

因此：

$$
\boxed{
R_x
\cong
k[X,X^{-1}].
}
$$

在此模型中：

$$
x\longmapsto X,
$$

$$
y\longmapsto 0.
$$

這再次確認 $y$ 的坍縮是局部化的內在結果。

---

# 第六部　在 $y$ 上局部化

## 19. 乘法閉集 $S_y$

定義：

$$
S_y
=
\{y^n:n\geq 0\}.
$$

同理：

$$
0\notin S_y.
$$

令：

$$
R_y
:=
S_y^{-1}R.
$$

## 20. 對稱結論

完全對稱地：

$$
\boxed{
\ker(\lambda_y)
=(x),
}
$$

並且：

$$
\boxed{
R_y
\cong
k[Y,Y^{-1}].
}
$$

因此：

$$
\frac{x}{1}
=
\frac{0}{1}
\quad\text{於 }R_y,
$$

但：

$$
\frac{y}{1}
\neq
\frac{0}{1}
\quad\text{於 }R_y.
$$

## 21. 同一來源差異的上下文反轉

在 $R$ 中：

$$
x\neq 0,
\qquad
y\neq 0.
$$

但兩個目標上下文給出：

| 來源元素 | 在 $R_x$ 中 | 在 $R_y$ 中 |
| --- | --- | --- |
| $x$ | 非零且可逆 | 坍縮為零 |
| $y$ | 坍縮為零 | 非零且可逆 |
| $x+y$ | 等於 $x$ ，故可逆 | 等於 $y$ ，故可逆 |

所以「是否坍縮」不是來源元素的絕對屬性，而是：

$$
\boxed{
\operatorname{CollapseStatus}(r;S)
}
$$

的上下文相對屬性。

---

# 第七部　交叉缺陷分類

## 22. 三態判定

對：

$$
E=(a,s),
\qquad
F=(b,t),
$$

令：

$$
\Delta(E,F)
=
at-bs.
$$

則可分為三種情況。

### 22.1 精確交叉相等

若：

$$
\Delta(E,F)=0,
$$

則：

$$
E\sim_S F
$$

且不需使用非平凡湮滅元素。

### 22.2 強迫局部化相等

若：

$$
\Delta(E,F)\neq 0
$$

但：

$$
\Delta(E,F)\in\operatorname{Ker}_S(R),
$$

則：

$$
E\sim_S F,
$$

但相等是由 $S$-湮滅強迫產生。

### 22.3 局部化中仍可區分

若：

$$
\Delta(E,F)\notin\operatorname{Ker}_S(R),
$$

則：

$$
E\not\sim_S F.
$$

因此：

$$
\boxed{
\Delta
\text{ 的狀態}
=
\text{局部化等價的結構診斷量}.
}
$$

## 23. 本例的完整判定表

| 比較 | 交叉缺陷 | $R_x$ 中 | $R_y$ 中 |
| --- | --- | --- | --- |
| $(y,1)$ 與 $(0,1)$ | $y$ | 強迫相等 | 可區分 |
| $(x,1)$ 與 $(0,1)$ | $x$ | 可區分 | 強迫相等 |
| $(x+y,1)$ 與 $(x,1)$ | $y$ | 強迫相等 | 可區分 |
| $(x+y,1)$ 與 $(y,1)$ | $x$ | 可區分 | 強迫相等 |

此表不是數值計算，而是上下文改變時，等價缺陷如何進入不同湮滅核的結構計算。

---

# 第八部　飽和分母與目標可逆性

## 24. 兩種分母合法性

標準局部化的原始代表要求：

$$
s\in S.
$$

但一個元素 $b\in R$ 即使不屬於 $S$ ，其像：

$$
\lambda_S(b)
$$

仍可能在 $S^{-1}R$ 中成為可逆元。

因此必須區分：

$$
\operatorname{DenGeneratorLegal}_S(b)
\Longleftrightarrow
b\in S,
$$

與：

$$
\operatorname{DenTargetInvertible}_S(b)
\Longleftrightarrow
\lambda_S(b)\in(S^{-1}R)^\times.
$$

## 25. 運算飽和

定義 $S$ 的目標可逆飽和：

$$
S^{\mathrm{sat}}
:=
\lambda_S^{-1}
\left(
(S^{-1}R)^\times
\right).
$$

因此：

$$
b\in S^{\mathrm{sat}}
\Longleftrightarrow
\lambda_S(b)
\text{ 在目標中可逆}.
$$

顯然：

$$
S\subseteq S^{\mathrm{sat}}.
$$

但等號不必成立。

## 26. $x+y$ 是衍生可逆分母

在 $R_x$ 中：

$$
\lambda_x(y)=0.
$$

因此：

$$
\lambda_x(x+y)
=
\lambda_x(x).
$$

而 $\lambda_x(x)$ 可逆，所以：

$$
x+y\in S_x^{\mathrm{sat}}.
$$

另一方面：

$$
x+y\notin S_x.
$$

若假設 $x+y=x^n$ ，將 $x$ 送至零而映入 $k[y]$ ，則當 $n\geq 1$ 時會得到 $y=0$ ；當 $n=0$ 時則會得到 $y=1$ 。兩者皆不成立，故上述不屬關係確實成立。

因此：

$$
\boxed{
x+y
\text{ 不是直接生成分母，卻是目標中的衍生可逆分母。}
}
$$

其逆由：

$$
\frac{1}{x}
$$

實現，因為：

$$
\frac{x+y}{1}\cdot\frac{1}{x}
=
\frac{x+y}{x}
=
\frac{1}{1}
\quad\text{於 }R_x.
$$

等價證書可取 $u=x$ ：

$$
x\big((x+y)\cdot 1-1\cdot x\big)
=
xy
=
0.
$$

## 27. $y$ 是坍縮分母

在 $R_x$ 中：

$$
\lambda_x(y)=0.
$$

由於：

$$
R_x\cong k[X,X^{-1}]
$$

是非零環，零元素不可逆。因此：

$$
y\notin S_x^{\mathrm{sat}}.
$$

所以：

$$
\frac{1}{y}
$$

不能在 $R_x$ 中實現。

這與 $1/(x+y)$ 完全不同：

$$
\boxed{
\frac{1}{x+y}
\text{ 可間接實現},
\qquad
\frac{1}{y}
\text{ 不可實現}.
}
$$

## 28. 分母四態

本輪建議把分母狀態擴充為：

| 狀態 | 判準 | 本例 |
| --- | --- | --- |
| 直接生成分母 | $b\in S$ | $x$ 於 $R_x$ |
| 衍生可逆分母 | $b\notin S$ 且 $b\in S^{\mathrm{sat}}$ | $x+y$ 於 $R_x$ |
| 非可逆分母 | $\lambda_S(b)$ 非零但非單位 | 依環與 $S$ 而定 |
| 坍縮分母 | $\lambda_S(b)=0$ | $y$ 於 $R_x$ |

因此，第一版單一的：

$$
\operatorname{DenLegal}_{\rho}(b)
$$

應至少分裂為：

$$
\operatorname{DenRawLegal}_S(b),
$$

$$
\operatorname{DenInvertible}_S(b),
$$

$$
\operatorname{DenCollapsed}_S(b).
$$

---

# 第九部　X 分數四層判定的第二次擴充

## 29. 第一輪留下的四個判定

第一次實戰已要求區分：

### 29.1 語法形成

$$
\Gamma_{\mathrm{syn}}
\vdash
E
\;\operatorname{synform}.
$$

### 29.2 環境商類形成

$$
\Gamma_{\mathrm{amb}}
\vdash
[E]
\;\operatorname{classform}.
$$

### 29.3 目標代表合法性

$$
\Gamma_{\mathrm{tar}}
\vdash
E
\;\operatorname{replegal}.
$$

### 29.4 目標實現

$$
\Gamma_{\mathrm{tar}}
\vdash
[E]
\;\operatorname{realizable}.
$$

## 30. 本輪新增的第五項：識別模式

即使兩個商類在目標中相等，仍須回答：

$$
\text{它們為何相等？}
$$

新增判定：

$$
\Gamma_{\mathrm{tar}}
\vdash
(E,F)
\;\operatorname{idmode}(\mu),
$$

其中 $\mu$ 至少可取：

$$
\mu
\in
\left\{
\begin{array}{l}
\mathrm{ExactCrossEquality},\\
\mathrm{ForcedLocalizationEquality},\\
\mathrm{ProjectionOnlyEquality},\\
\mathrm{UncertifiedIdentification}
\end{array}
\right\}.
$$

## 31. 強迫坍縮證書

若：

$$
E=(a,s),
\qquad
F=(b,t),
$$

且：

$$
at-bs\neq 0,
$$

但存在：

$$
u\in S
$$

使：

$$
u(at-bs)=0,
$$

則定義：

$$
\operatorname{ForcedCollapseCert}_S(E,F;u).
$$

其最小資料為：

$$
C_{\mathrm{fc}}
=
\left(
\begin{array}{l}
E,F,\\
\Delta(E,F),\\
\Delta(E,F)\neq 0,\\
u\in S,\\
u\Delta(E,F)=0,\\
\Gamma_{\mathrm{tar}}
\end{array}
\right).
$$

## 32. 新的判定流程

本輪建議流程為：

$$
\boxed{
\begin{aligned}
&\text{語法形成}\\
\longrightarrow\;&\text{環境商類形成}\\
\longrightarrow\;&\text{目標代表或飽和分母搜尋}\\
\longrightarrow\;&\text{目標實現}\\
\longrightarrow\;&\text{識別模式判定}\\
\longrightarrow\;&\text{來源／坍縮證書}\\
\longrightarrow\;&\text{再積分守衛}.
\end{aligned}
}
$$

---

# 第十部　來源保存的三種強度

## 33. 軌跡保存

對來源 $a\in R$ ，即使：

$$
\lambda_S(a)=0,
$$

X 擴充資料仍可記錄：

$$
\operatorname{Trace}
\big(
a,
R,
S,
\lambda_S,
\text{形成路徑}
\big).
$$

這稱為：

$$
\operatorname{TracePreservation}.
$$

## 34. 來源可重建

來源可重建要求存在某種規則，可由目標商類唯一恢復來源：

$$
[a/1]_S
\longmapsto
a.
$$

本例中不可能做到，因為所有：

$$
a\in(y)
$$

都滿足：

$$
\lambda_x(a)=0.
$$

因此，僅從 $R_x$ 的零元素無法判斷來源是：

$$
0,
\quad
y,
\quad
y^2,
\quad
y+y^3,
\quad
\ldots
$$

所以：

$$
\boxed{
\operatorname{TracePreservation}
\nRightarrow
\operatorname{SourceReconstructibility}.
}
$$

## 35. 來源單射保存

最強版本要求：

$$
a\neq b
\Longrightarrow
\lambda_S(a)\neq\lambda_S(b).
$$

這恰好等價於：

$$
\lambda_S
\text{ 單射}.
$$

亦即：

$$
\operatorname{Ker}_S(R)=0.
$$

所以來源保存必須分成：

| 強度 | 意義 | 一般是否成立 |
| --- | --- | --- |
| 軌跡保存 | 外加資料記得來源 | 可以設計成立 |
| 來源可重建 | 由商類唯一恢復來源 | 一般不成立 |
| 單射保存 | 不同來源映為不同元素 | 僅在核為零時成立 |

## 36. 裝飾局部化

可用下列概念模型表示 X 擴充層：

$$
\widetilde{R_S}
=
\left\{
\big([a,s]_S,\tau\big)
\right\},
$$

其中 $\tau$ 是來源與形成軌跡。

存在忘卻映射：

$$
U:
\widetilde{R_S}
\longrightarrow
R_S,
$$

$$
U\big([a,s]_S,\tau\big)
=
[a,s]_S.
$$

於本例：

$$
U\big([y,1]_{S_x},\tau_y\big)
=
0,
$$

$$
U\big([0,1]_{S_x},\tau_0\big)
=
0,
$$

但可有：

$$
\tau_y\neq\tau_0.
$$

因此：

$$
\boxed{
\text{X 層可區分軌跡，標準局部化層仍維持同一零元素。}
}
$$

這是保守擴充，而不是修改局部化等式。

---

# 第十一部　非坍縮律的核心修正

## 37. 不可接受的強讀法

下式一般為假：

$$
F\not\equiv_{\mathrm{src}}G
\Longrightarrow
[F]_S\neq[G]_S.
$$

本例取：

$$
F=(y,1),
\qquad
G=(0,1),
$$

即得反例。

## 38. 可接受的弱讀法

商類相等不得回推原始來源相等：

$$
[F]_S=[G]_S
\nRightarrow
F\equiv_{\mathrm{src}}G.
$$

這在本例中成立，並且是必要的層級區分。

## 39. 證書化讀法

若：

$$
F\not\equiv_{\mathrm{src}}G
$$

但：

$$
[F]_S=[G]_S,
$$

則必須輸出：

$$
\operatorname{IdentificationCert}_S(F,G).
$$

對一般局部化，此證書可具體化為：

$$
\operatorname{LocEqCert}_S(F,G;u).
$$

## 40. 條件式強非坍縮

只有在：

$$
\operatorname{Ker}_S(R)=0
$$

時，才可使用：

$$
\lambda_S(a)=\lambda_S(b)
\Longrightarrow
a=b.
$$

因此，建議把第三律改名或細分為：

1. **層級非混同律**；
2. **識別必有證書律**；
3. **條件式來源單射律**。

其共同核心是：

$$
\boxed{
\text{不可阻止合法商化，必須阻止無證書的跨層混同。}
}
$$

---

# 第十二部　坍縮型別學

## 41. 來源相等

若：

$$
F\equiv_{\mathrm{src}}G,
$$

則不存在來源差異。

## 42. 表示正規化

來源對或分母歷史不同，但交叉缺陷精確為零：

$$
\Delta(E,F)=0.
$$

例如整域中的普通約分通常屬於此型。

## 43. $S$-強迫商類坍縮

交叉缺陷非零：

$$
\Delta(E,F)\neq 0,
$$

但：

$$
\Delta(E,F)\in\operatorname{Ker}_S(R).
$$

本輪的：

$$
(y,1)\sim_{S_x}(0,1)
$$

即屬此型。

## 44. 後端投影坍縮

兩個局部化商類本來不同，但在後續映射 $\pi$ 下相等：

$$
[E]_S\neq[F]_S,
$$

$$
\pi([E]_S)=\pi([F]_S).
$$

這才是原 XF-6「投影非坍縮」最直接處理的情況。

## 45. 非法無證書坍縮

若系統在沒有指定：

$$
\sim,
\quad
S,
\quad
u,
\quad
\pi
$$

或其他識別機制時，直接宣稱兩來源相同，則輸出：

$$
\operatorname{UncertifiedCollapse}.
$$

## 46. 坍縮譜

因此不應只有二元判定：

$$
\operatorname{Collapse}
\in
\{\mathrm{Yes},\mathrm{No}\}.
$$

而應至少輸出：

$$
\operatorname{CollapseMode}
\in
\left\{
\begin{array}{l}
\mathrm{SourceIdentity},\\
\mathrm{ExactQuotientIdentification},\\
\mathrm{ForcedLocalizationIdentification},\\
\mathrm{ProjectionIdentification},\\
\mathrm{UncertifiedCollapse}
\end{array}
\right\}.
$$

---

# 第十三部　上下文轉送

## 47. 局部化的泛性條件

給定另一乘法閉集 $T$ ，存在延伸 $R$ 上恆等映射的環同態：

$$
\Phi:
S^{-1}R
\longrightarrow
T^{-1}R,
$$

若且唯若每個 $s\in S$ 在 $T^{-1}R$ 中都成為可逆元。

亦即：

$$
\forall s\in S,
\quad
\lambda_T(s)\in(T^{-1}R)^\times.
$$

這可作為 X 上下文轉送守衛：

$$
\operatorname{TransferGuard}(S\to T).
$$

## 48. $R_x$ 不能轉送至 $R_y$

若存在：

$$
\Phi:
R_x\longrightarrow R_y
$$

延伸 $R$ 的結構映射，則 $x$ 在 $R_y$ 中必須可逆。

但：

$$
\lambda_y(x)=0.
$$

而：

$$
R_y\cong k[Y,Y^{-1}]
$$

是非零環，所以零不可逆。

因此：

$$
\boxed{
\operatorname{TransferGuard}(S_x\to S_y)
=
\operatorname{Fail}.
}
$$

同理：

$$
\boxed{
\operatorname{TransferGuard}(S_y\to S_x)
=
\operatorname{Fail}.
}
$$

## 49. 為何不能直接合併

若試圖同時使 $x$ 與 $y$ 可逆，則乘法閉包必須包含：

$$
xy.
$$

但：

$$
xy=0.
$$

所以由 $S_x\cup S_y$ 生成的乘法閉集包含零：

$$
0\in\langle S_x\cup S_y\rangle_\times.
$$

若允許此局部化，所得只會是零環；若要求非平凡目標，合併守衛必須失敗：

$$
\boxed{
\operatorname{MergeGuard}(S_x,S_y)
=
\operatorname{Fail}_{0\in\langle S_x\cup S_y\rangle_\times}.
}
$$

## 50. 幾何核對

在譜空間中：

$$
D(x)\cap D(y)
=
D(xy).
$$

由於：

$$
xy=0,
$$

故：

$$
D(xy)
=
D(0)
=
\varnothing.
$$

所以兩個局部上下文沒有共同非空重疊。

X 再積分守衛在此不是拒絕一個其實存在的整體，而是正確偵測：

$$
\boxed{
\text{共同非平凡語境不存在。}
}
$$

---

# 第十四部　X 結構微分

## 51. 本輪的結構微分輸出

本輪不引入數值導數。X 結構微分的工作是揭露：

1. 交叉缺陷；
2. 缺陷是否為零；
3. 缺陷是否位於 $S$-湮滅核；
4. 使用哪個 $u\in S$ 湮滅缺陷；
5. 來源是否仍不同；
6. 分母是直接、衍生、非可逆或坍縮；
7. 上下文能否轉送或合併。

## 52. 局部化結構差分

可定義診斷算子：

$$
\mathsf D_{\mathrm{loc}}^S(E,F)
:=
\left(
\Delta(E,F),
\operatorname{Ker}_S(R),
\operatorname{CollapseMode},
C_{\mathrm{loc}}
\right).
$$

其目的不是產生數值，而是判定：

$$
\boxed{
\text{差異在哪一層仍存在，又在哪一層被合法識別。}
}
$$

## 53. 對本例的輸出

取：

$$
E=(y,1),
\qquad
Z=(0,1).
$$

則：

$$
\Delta(E,Z)=y.
$$

在 $S_x$ 上：

$$
y\in\operatorname{Ker}_{S_x}(R),
$$

故：

$$
\mathsf D_{\mathrm{loc}}^{S_x}(E,Z)
=
\left(
y,
(y),
\mathrm{ForcedLocalizationIdentification},
x
\right).
$$

在 $S_y$ 上：

$$
y\notin\operatorname{Ker}_{S_y}(R)=(x),
$$

故：

$$
\mathsf D_{\mathrm{loc}}^{S_y}(E,Z)
=
\left(
y,
(x),
\mathrm{DistinctClasses},
\varnothing
\right).
$$

這是同一來源差異在兩個上下文中的完整結構展開。

---

# 第十五部　六大基本律稽核

## 54. 第一律：形成律

### 原要求

分子、分母、關係與上下文合法後形成分數。

### 本輪發現

單一分母合法性不足。至少要區分：

$$
b\in S,
$$

$$
b\in S^{\mathrm{sat}},
$$

$$
\lambda_S(b)=0,
$$

以及：

$$
\lambda_S(b)
\text{ 為非零非單位}.
$$

### 判定

$$
\boxed{
\operatorname{PassWithRevision}.
}
$$

## 55. 第二律：來源保存律

### 可成立部分

來源與形成歷史可由外加 X 證書追蹤。

### 不可宣稱部分

不能由局部化商類唯一重建來源，也不能假設來源映射單射。

### 判定

$$
\boxed{
\operatorname{PassAsTracePreservation}.
}
$$

若原律聲稱商類本身內在保存唯一來源，則：

$$
\boxed{
\operatorname{Fail}.
}
$$

## 56. 第三律：非坍縮律

### 弱讀法

商類相等不等於來源相等，並且識別必須有證書。

此讀法通過。

### 強讀法

不同來源在任何合法結構中永遠不可變成同一元素。

此讀法被本例反駁。

### 判定

$$
\boxed{
\operatorname{CoreRevisionRequired}.
}
$$

## 57. 第四律：再積分守衛律

$R_x$ 與 $R_y$ 不能在非零局部化中同時實現，因共同乘法閉包含零。

守衛給出明確失敗理由：

$$
0\in\langle S_x\cup S_y\rangle_\times.
$$

### 判定

$$
\boxed{
\operatorname{StrongPass}.
}
$$

## 58. 第五律：結構微分律

本輪可展開：

$$
\Delta(E,F),
$$

$$
\operatorname{Ker}_S(R),
$$

$$
\operatorname{CollapseMode},
$$

$$
\operatorname{DenStatus},
$$

$$
\operatorname{TransferGuard}.
$$

這構成可驗證的非數值結構微分。

### 判定

$$
\boxed{
\operatorname{Pass}.
}
$$

## 59. 第六律：動態整體閉合律

各自的局部化內部具有環運算閉包。

但兩個局部整體不能無條件再合併：

$$
R_x
\nrightarrow
\text{共同非零局部化}
\nleftarrow
R_y.
$$

若動態閉合律允許守衛拒絕不相容擴張，則通過；若要求任何既有整體都必須形成更大整體，則失敗。

### 判定

$$
\boxed{
\operatorname{ConditionalPass}.
}
$$

## 60. 六律總表

| 基本律 | 判定 | 必要修正 |
| --- | --- | --- |
| 形成律 | 通過但需修正 | 分裂直接分母、飽和分母與坍縮分母 |
| 來源保存律 | 軌跡版通過 | 不得宣稱可由商類唯一重建 |
| 非坍縮律 | 核心修正 | 改為層級非混同、證書化識別與條件單射 |
| 再積分守衛律 | 強通過 | 加入共同乘法閉包含零判定 |
| 結構微分律 | 通過 | 輸出缺陷、湮滅核與識別模式 |
| 動態整體閉合律 | 條件通過 | 合法停止也是閉合系統的一部分 |

---

# 第十六部　對第一版公理的修正案

## 61. XF-3 修正：分母角色分層

原單一判定：

$$
\operatorname{DenLegal}_{\rho}(b)
$$

改為：

$$
\operatorname{DenRawLegal}_{S}(b),
$$

$$
\operatorname{DenTargetInvertible}_{S}(b),
$$

$$
\operatorname{DenCollapsed}_{S}(b).
$$

並允許：

$$
\neg\operatorname{DenRawLegal}_{S}(b)
\quad\land\quad
\operatorname{DenTargetInvertible}_{S}(b).
$$

## 62. XF-4 修正：形成上下文雙分離

形成公理必須明示：

$$
\Gamma_{\mathrm{amb}}
\neq
\Gamma_{\mathrm{tar}}
$$

可能成立，並分開判定：

$$
\operatorname{ClassForm},
\quad
\operatorname{RepLegal},
\quad
\operatorname{TargetRealizable}.
$$

## 63. XF-5 修正：來源保存強度標註

任何來源保存主張必須標記：

$$
\operatorname{PreservationLevel}
\in
\left\{
\mathrm{Trace},
\mathrm{Reconstructible},
\mathrm{Injective}
\right\}.
$$

未標記時，預設只能主張：

$$
\mathrm{Trace}.
$$

## 64. XF-6 修正：非坍縮三分律

建議以三條取代單一口號。

### XF-6a：層級非混同

$$
[F]_{\sim}=[G]_{\sim}
\nRightarrow
F\equiv_{\mathrm{src}}G.
$$

### XF-6b：識別證書

$$
[F]_{\sim}=[G]_{\sim}
\Longrightarrow
\exists C_{\sim}\;
\operatorname{Certifies}(C_{\sim};F,G).
$$

### XF-6c：條件單射

只有存在單射證書：

$$
C_{\mathrm{inj}}
:
\ker(q)=0
$$

時，才可反推：

$$
q(F)=q(G)
\Longrightarrow
F=G.
$$

## 65. XF-7 修正：一般局部化商關係

若語義後端為一般交換環局部化，商關係必須使用：

$$
(a,s)\sim_S(b,t)
\Longleftrightarrow
\exists u\in S,\;
u(at-bs)=0.
$$

只有附帶正則性證書後，才能化簡成：

$$
at=bs.
$$

## 66. XF-8 修正：上下文合併守衛

對兩個局部化上下文 $S,T$ ，加入：

$$
\operatorname{MergeGuard}(S,T)
\Longrightarrow
0\notin\langle S\cup T\rangle_\times.
$$

若：

$$
0\in\langle S\cup T\rangle_\times,
$$

則非平凡再積分失敗。

---

# 第十七部　候選定理

## 67. 一般局部化的 X 保守實現定理

### 定理候選

令 $R$ 為交換環， $S\subseteq R$ 為乘法閉集且 $0\notin S$ 。若 X 分數系統採用：

1. 原始材料 $R\times S$ ；
2. 分母生成守衛 $s\in S$ ；
3. 一般局部化等價：

$$
(a,s)\sim_S(b,t)
\Longleftrightarrow
\exists u\in S,\;u(at-bs)=0;
$$

4. 商化閉包；
5. 來源軌跡作為外加資料；
6. 忘卻映射丟棄軌跡資料；

則其忘卻語義與標準局部化同構：

$$
U(\operatorname{XLoc}_S(R))
\cong
S^{-1}R.
$$

### 新增結構

X 層可額外保存：

$$
\operatorname{LocEqCert},
\quad
\operatorname{SourceTrace},
\quad
\operatorname{CollapseMode},
\quad
\operatorname{DenStatus},
\quad
\operatorname{TransferGuard}.
$$

### 限制

此定理不表示 X 層的來源軌跡是標準局部化元素的內在不變量。

## 68. 條件式來源非坍縮定理

### 定理

若：

$$
\operatorname{Ker}_S(R)=0,
$$

則：

$$
\lambda_S:R\longrightarrow S^{-1}R
$$

單射。

因此：

$$
\lambda_S(a)=\lambda_S(b)
\Longrightarrow
a=b.
$$

### X 解讀

強來源非坍縮不是無條件公理，而是由：

$$
C_{\mathrm{inj}}
:
\operatorname{Ker}_S(R)=0
$$

啟用的條件式規則。

## 69. 強迫坍縮分類定理

令：

$$
E=(a,s),
\qquad
F=(b,t).
$$

則：

$$
[E]_S=[F]_S
$$

若且唯若：

$$
\Delta(E,F)
\in
\operatorname{Ker}_S(R).
$$

進一步：

$$
\Delta(E,F)=0
$$

對應精確交叉相等；而：

$$
0\neq\Delta(E,F)
\in
\operatorname{Ker}_S(R)
$$

對應強迫局部化相等。

這給出一個完全可判定的兩級商類識別分類。

---

# 第十八部　演算法化判定草案

## 70. 輸入

輸入資料：

$$
\mathcal I
=
(R,S,E,F,\Gamma_{\mathrm{tar}}),
$$

其中：

$$
E=(a,s),
\qquad
F=(b,t).
$$

## 71. 判定步驟

### Step 1：乘法集檢查

檢查：

$$
1\in S,
\qquad
S\cdot S\subseteq S,
\qquad
0\notin S.
$$

### Step 2：代表檢查

檢查：

$$
s,t\in S.
$$

### Step 3：交叉缺陷

計算：

$$
\Delta=at-bs.
$$

### Step 4：精確等價

若：

$$
\Delta=0,
$$

輸出：

$$
\mathrm{ExactCrossEquality}.
$$

### Step 5：湮滅搜尋

若：

$$
\Delta\neq 0,
$$

搜尋：

$$
u\in S
$$

使：

$$
u\Delta=0.
$$

若找到，輸出：

$$
\mathrm{ForcedLocalizationEquality}
$$

及：

$$
\operatorname{LocEqCert}_S(E,F;u).
$$

### Step 6：可區分

若不存在此 $u$ ，輸出：

$$
\mathrm{DistinctLocalizationClasses}.
$$

### Step 7：來源層

不論商類是否相等，另行比較：

$$
E\equiv_{\mathrm{src}}F.
$$

禁止由商類結果代替來源比較。

### Step 8：分母目標狀態

對任意待用分母 $b$ ，判定：

$$
b\in S,
$$

$$
b\in S^{\mathrm{sat}},
$$

$$
\lambda_S(b)=0.
$$

### Step 9：再積分守衛

若欲合併另一上下文 $T$ ，檢查：

$$
0\notin\langle S\cup T\rangle_\times
$$

及雙向可逆性條件。

## 72. 建議輸出格式

建議輸出：

$$
\operatorname{XLocReport}
=
\left(
\begin{array}{l}
\operatorname{SyntaxStatus},\\
\operatorname{RepresentativeStatus},\\
\operatorname{ClassStatus},\\
\operatorname{CrossDefect},\\
\operatorname{AnnihilatorWitness},\\
\operatorname{IdentificationMode},\\
\operatorname{SourceRelation},\\
\operatorname{DenominatorStatus},\\
\operatorname{TransferStatus},\\
\operatorname{ReintegrationStatus}
\end{array}
\right).
$$

---

# 第十九部　可反駁命題

## 73. 來源軌跡不是商類內在唯一資料

可反駁主張：

> 每個局部化商類都內在地帶有唯一來源。

反例：

$$
\lambda_x(0)
=
\lambda_x(y)
=
\lambda_x(y^2)
=
0.
$$

因此，若無外加軌跡，零商類沒有唯一來源。

## 74. 非零來源不保證非零目標

可反駁主張：

$$
a\neq 0
\Longrightarrow
\lambda_S(a)\neq 0.
$$

反例：

$$
y\neq 0
\quad\text{於 }R,
$$

但：

$$
\lambda_x(y)=0.
$$

## 75. 不屬於 $S$ 不代表不可逆

可反駁主張：

$$
b\notin S
\Longrightarrow
\lambda_S(b)
\text{ 不可逆}.
$$

反例：

$$
x+y\notin S_x,
$$

但：

$$
\lambda_x(x+y)
=
\lambda_x(x)
$$

可逆。

## 76. 兩個合法局部上下文不保證可合併

可反駁主張：

> 若 $S^{-1}R$ 與 $T^{-1}R$ 各自合法，則必存在共同非零局部化。

反例：

$$
S=S_x,
\qquad
T=S_y.
$$

兩者各自合法，但：

$$
0=xy
\in
\langle S_x\cup S_y\rangle_\times.
$$

---

# 第二十部　標準數學與 X 新增層

## 77. 標準交換代數已知內容

下列內容皆屬標準交換代數：

- 一般局部化的等價關係；
- 局部化映射的核；
- 單射性判準；
- $k[X,Y]/(XY)$ 的兩個主局部化；
- 局部化的泛性；
- $D(x)\cap D(y)=D(xy)$ ；
- 飽和乘法集與目標可逆性。

本文不把這些結果宣稱為 X 理論新定理。

## 78. X 層可能新增的工作

X 框架可新增的是統一記錄：

1. 原始來源；
2. 分數關係型別；
3. 語法、商類、代表與目標四層合法性；
4. 交叉缺陷；
5. 湮滅證書；
6. 坍縮模式；
7. 分母狀態；
8. 上下文轉送；
9. 再積分失敗原因；
10. 忘卻後回到標準模型的保守性。

## 79. 誠實的新穎性判定

本輪沒有創造新的局部化構造。

真正的理論進展是抓到兩個不能繼續模糊的地方：

$$
\boxed{
\text{一般局部化等價}
\neq
\text{整域交叉相等}.
}
$$

以及：

$$
\boxed{
\text{來源保存}
\neq
\text{來源映射必然單射}.
}
$$

若這兩點不修，X 分數理論只能安全作用於整域模型，不能宣稱涵蓋一般交換環。

---

# 第二十一部　限制

## 80. 本輪未處理非交換局部化

本文假設 $R$ 為交換環。

非交換環的 Ore 局部化需要不同的存在條件與等價關係，不能直接套用本文公式。

## 81. 本輪未建立證書範疇

本文使用：

$$
\widetilde{R_S}
$$

作為裝飾局部化的概念模型，但尚未指定：

- 對象；
- 態射；
- 證書同一性；
- 證書合成；
- 忘卻函子；
- 纖維中的等價關係。

因此，它目前是形式化方向，不是已完成的範疇定義。

## 82. 本輪未解決演算法可判定性

對一般環與一般乘法集，搜尋：

$$
u\in S
$$

使：

$$
u\Delta=0
$$

未必具有有限演算法。

在有限生成環、明示乘法集或可用 Gröbner 基底處理的情況下，才可能轉成實際計算程序。

## 83. 本輪未把來源軌跡內在化

來源軌跡目前是外加資料。

若未來要把它內在化，必須選擇：

- 歷史型別；
- 證明相關或證明無關語義；
- 同一商類上的多個來源是否形成群胚；
- 哪些軌跡差異可再商化。

在完成這些選擇前，不應宣稱軌跡是局部化元素本身的一部分。

---

# 第二十二部　下一個純數學實戰

## 84. 射影直線

下一輪建議考察：

$$
\mathbb P^1(k).
$$

使用齊次座標：

$$
[X:Y]
$$

及兩張仿射圖：

$$
U_X=\{X\neq 0\},
$$

$$
U_Y=\{Y\neq 0\}.
$$

在重疊區：

$$
U_X\cap U_Y,
$$

座標由：

$$
t=\frac{Y}{X}
$$

與：

$$
s=\frac{X}{Y}
$$

互換，滿足：

$$
st=1.
$$

這可測試：

- 分數線型別是普通商還是齊次比例；
- 同一射影點的多重代表；
- 圖冊換圖證書；
- 無窮遠點不是除零錯誤；
- 目標上下文之間存在合法重疊；
- 與本輪「空重疊」案例的對照。

## 85. 為何射影直線現在適合

第一次實戰處理：

$$
\text{同一商類的替代代表}.
$$

第二次實戰處理：

$$
\text{商關係強迫的來源坍縮}.
$$

射影直線將處理：

$$
\text{同一幾何對象的圖冊依賴表示}
$$

與：

$$
\text{合法上下文重疊及換圖}.
$$

三者合起來，才足以判斷 X 分數能否從環論表示推進到幾何表示。

---

# 第二十三部　結論

## 86. 本輪最重要的修正

一般局部化要求：

$$
\boxed{
(a,s)\sim_S(b,t)
\Longleftrightarrow
\exists u\in S,\;
u(at-bs)=0.
}
$$

因此，局部化可以把不同來源合法映成同一元素。

## 87. 非坍縮的正確位置

X 非坍縮不能位於「禁止商類相等」這一層。

它應位於：

$$
\boxed{
\begin{aligned}
&\text{禁止商類等式回推成來源等式},\\
&\text{禁止無關係宣告的識別},\\
&\text{要求所有來源損失具有可追蹤證書},\\
&\text{只在單射證書存在時啟用強非坍縮}.
\end{aligned}
}
$$

## 88. 對 X 分數理論的實質影響

本輪證明 X 分數理論若要涵蓋一般交換環，必須新增：

1. $S$-湮滅核；
2. 一般局部化等價證書；
3. 強迫坍縮分類；
4. 來源保存強度；
5. 飽和分母；
6. 上下文轉送守衛；
7. 共同乘法閉包含零的再積分失敗。

## 89. 最終判定

本輪不是替 X 理論尋找支持性例子，而是讓標準代數決定理論能否存活。

結果是：

$$
\boxed{
\operatorname{PassWithCoreRevision}.
}
$$

保留下來的核心不是「任何東西都不能坍縮」，而是更精確的原則：

$$
\boxed{
\text{可以合法坍縮，但不得無證書坍縮；}
}
$$

$$
\boxed{
\text{可以在商類中相等，但不得把商類相等偷換成來源相等。}
}
$$

這使 X 非坍縮律從直覺口號轉變為可與一般交換代數相容的層級紀律。

---

# 附錄 A　核心公式表

## A.1 一般局部化等價

$$
(a,s)\sim_S(b,t)
\Longleftrightarrow
\exists u\in S,\;
u(at-bs)=0.
$$

## A.2 交叉缺陷

$$
\Delta((a,s),(b,t))
=
at-bs.
$$

## A.3 $S$-湮滅核

$$
\operatorname{Ker}_S(R)
=
\{r\in R:\exists s\in S,\;sr=0\}.
$$

## A.4 局部化核

$$
\ker(\lambda_S)
=
\operatorname{Ker}_S(R).
$$

## A.5 相等判準

$$
[E]_S=[F]_S
\Longleftrightarrow
\Delta(E,F)\in\operatorname{Ker}_S(R).
$$

## A.6 強迫相等

$$
0\neq\Delta(E,F)
\in
\operatorname{Ker}_S(R).
$$

## A.7 條件單射

$$
\lambda_S
\text{ 單射}
\Longleftrightarrow
\operatorname{Ker}_S(R)=0.
$$

## A.8 飽和分母

$$
S^{\mathrm{sat}}
=
\lambda_S^{-1}
\big((S^{-1}R)^\times\big).
$$

## A.9 合併守衛

$$
\operatorname{MergeGuard}(S,T)
\Longrightarrow
0\notin\langle S\cup T\rangle_\times.
$$

---

# 附錄 B　本例速查

$$
R=k[X,Y]/(XY).
$$

$$
S_x=\{x^n:n\geq 0\}.
$$

$$
S_y=\{y^n:n\geq 0\}.
$$

$$
\ker(\lambda_x)=(y).
$$

$$
\ker(\lambda_y)=(x).
$$

$$
R_x\cong k[X,X^{-1}].
$$

$$
R_y\cong k[Y,Y^{-1}].
$$

$$
\lambda_x(y)=0.
$$

$$
\lambda_y(x)=0.
$$

$$
\lambda_x(x+y)=\lambda_x(x)\in R_x^\times.
$$

$$
\lambda_y(x+y)=\lambda_y(y)\in R_y^\times.
$$

$$
0=xy\in\langle S_x\cup S_y\rangle_\times.
$$

$$
D(x)\cap D(y)=\varnothing.
$$

---

# 附錄 C　對主論文 v0.2 的最小移植清單

1. 把局部化等價由整域公式擴充為一般環公式；
2. 加入 $\operatorname{Ker}_S(R)$ ；
3. 加入 $\operatorname{LocEqCert}_S$ ；
4. 加入 $\operatorname{ForcedCollapseCert}_S$ ；
5. 將來源保存分成軌跡、可重建與單射三層；
6. 將非坍縮律分成層級非混同、識別證書與條件單射；
7. 將分母合法性分成直接、飽和、非可逆與坍縮；
8. 加入 $\operatorname{TransferGuard}$ ；
9. 加入 $\operatorname{MergeGuard}$ ；
10. 明示 X 軌跡是外加結構，忘卻後回到標準局部化。

---

# 參考方向

本稿使用的標準數學背景包括：

1. 交換環的乘法閉集與局部化；
2. 局部化等價關係及其泛性；
3. 局部化映射的核與單射性；
4. 零因子環的主局部化；
5. 仿射概形的基本開集。

後續正式版可對照交換代數標準教材與代數幾何基礎文獻補入精確書目。
