---
title: "X 奇點論初步：來源合流、投影退化、表示缺口與值域邊界"
subtitle: "Foundations of X-Singularity Theory: Source Confluence, Projection Degeneracy, Representational Gaps, and Codomain Boundaries"
version: "v0.1"
date: "2026-07-24"
author: "Neo.K / EveMissLab"
language: "zh-TW"
status: "Foundational Research Paper"
keywords:
  - X 積分
  - X 奇點論
  - 奇點分類
  - 節點
  - 尖點
  - 可去奇點
  - 極點
  - 正規化
  - 投影退化
  - 值域擴張
---

# X 奇點論初步：來源合流、投影退化、表示缺口與值域邊界

## 摘要

本文建立 X 積分框架下的第一版奇點分類理論。傳統數學中的「奇點」常依不同領域分別由 Jacobian 退化、函數未定義、極限發散、正則性失敗、分支產生或解類型轉換來判定。然而，這些現象並不發生在同一結構層。若只以「某點出問題」作為共同描述，便容易把來源合流、投影退化、表示缺口、值域邊界與真正結構斷裂混為一談。

本文提出：X 奇點分類的第一步，不是問某點是否奇異，而是問「奇異性發生在哪一層」。為此，本文引入來源空間、空間實現、投影纖維、秩譜、切向譜、延拓性、值域擴張與失敗層級等結構資料，並建立 X 奇點證書：

$$
\operatorname{XSingCert}(p)
=
\left\langle
B_p,
R_p,
T_p,
E_p,
V_p,
C_p
\right\rangle.
$$

本文以四個基礎案例進行測試：

1. 節點 $xy=0$ ：多個正常來源分支在空間像中合流；
2. 尖點 $y^2=x^3$ ：單一平滑來源的投影在奇點處退化；
3. 可去奇點 $\sin z/z$ ：原表示式失敗，但函數胚可在原值域內唯一補全；
4. 極點 $1/z$ ：無法在原值域內補全，但可透過值域擴張至黎曼球面而合法形成。

由此得到四種不同的 X 奇點類型：

$$
\boxed{
\text{來源合流}
\neq
\text{投影退化}
\neq
\text{表示缺口}
\neq
\text{值域邊界到達}.
}
$$

本文同時提出「表示—結構分離原則」、「奇點相對性原則」、「修復代價分類」與「層級化不可形成判定」。這些原則表明：某個公式不可形成，不等於其數學結構不可形成；某個點是否奇異，取決於來源類型、目標類型、允許映射、邊界與補全規則；奇點分類亦可由修復時必須改變哪一個結構層來判定。

本文不宣稱已完成一般奇點理論。其目前範圍限於低維代數曲線與單變數複函數中的四個基礎模型。分支點、本性奇點、分布奇點、動態 PDE 奇點、測度奇點與拓撲奇點，仍需後續擴展。

---

## 1. 問題：所有「出問題的點」都是同一種奇點嗎？

在不同數學領域中，奇點可由不同條件辨識：

- 隱式曲線上 Jacobian 或梯度退化；
- 參數化映射的秩下降；
- 函數在某點未定義；
- 極限不存在或發散；
- 解析延拓失敗；
- 值域需加入無窮遠點；
- 局部單值性失敗；
- 解的正則性在有限時間破裂；
- 測度集中在低維支撐；
- 投影或商化抹除必要差異。

因此，「奇點」不是天然單一類型。

例如，以下四個對象都在原點呈現某種異常：

$$
xy=0,
$$

$$
y^2=x^3,
$$

$$
\frac{\sin z}{z},
$$

$$
\frac1z.
$$

但它們的異常機制完全不同：

- 第一個有兩個來源分支；
- 第二個只有一個來源，但參數化微分退化；
- 第三個只有表示式缺值；
- 第四個不能在原值域補值，卻能在擴張值域中補成無窮遠點。

因此，X 奇點論的基本問題不是：

$$
p\text{ 是否奇異？}
$$

而是：

$$
\boxed{
\text{奇異性發生在來源、投影、表示、值域、邊界，還是其他結構層？}
}
$$

---

## 2. X 積分中的奇點背景

X 積分將結構形成置於測度與數值之前。其最小結構可寫為：

$$
X=
\langle
A_X,
T_X,
C_X,
R_X,
B_X,
P_X
\rangle,
$$

其中分別表示：

- 屬性；
- 類型；
- 範疇位置；
- 關係；
- 邊界；
- 權限或合法操作。

X 積分形成：

$$
\Gamma\vdash
\mathsf I_\rho(X;Y):Z
$$

要求：

- 輸入合法；
- 關係合法；
- 類型相容或存在橋接；
- 邊界轉換可定義；
- 非坍縮；
- 來源可保存。

奇點因此可初步理解為：

> 某個局部結構在形成、投影、延拓、再積分、邊界通過或類型保持時，出現合法性失敗或結構退化。

但這仍太粗。不同失敗層必須分開。

---

## 3. 來源—實現框架

設一個幾何或函數結構 C 具有較規則的來源空間：

$$
\nu:\widetilde C\to C.
$$

其中：

- $\widetilde C$ 是來源結構；
- $\nu$ 是空間實現、參數化或正規化映射；
- C 是觀察到的空間像。

對 $p\in C$ ，定義來源纖維：

$$
\operatorname{Src}(p)
=
\nu^{-1}(p).
$$

其大小：

$$
b(p)
=
|\nu^{-1}(p)|
$$

表示有多少不同來源被映至 p。

再定義秩譜：

$$
R_p
=
\left\{
\operatorname{rank}(d\nu_q)
:
q\in\nu^{-1}(p)
\right\}.
$$

來源數與秩譜給出最小二維分類：

| 來源數 | 秩譜 | 初步類型 |
|---|---|---|
| $b=1$ | 正常 | 正常點或表示層問題 |
| $b>1$ | 各分支正常 | 來源合流 |
| $b=1$ | 退化 | 投影退化 |
| $b>1$ | 部分或全部退化 | 混合高階奇點 |

---

## 4. X 奇點證書

本文提出第一版 X 奇點證書：

$$
\boxed{
\operatorname{XSingCert}(p)
=
\left\langle
B_p,
R_p,
T_p,
E_p,
V_p,
C_p
\right\rangle.
}
$$

其中：

### 4.1 來源分支譜 $B_p$

記錄：

- 來源數量；
- 各來源是否彼此獨立；
- 是否可經正規化分離；
- 是否有來源被商化識別。

### 4.2 投影秩譜 $R_p$

記錄：

$$
\operatorname{rank}(d\nu_q)
$$

在所有來源點上的狀態。

### 4.3 切向與重數譜 $T_p$

包括：

- 切線或切錐；
- 切向分支數；
- 局部重數；
- 是否出現重切線。

### 4.4 延拓譜 $E_p$

記錄：

- 是否可在原類型中補全；
- 補全是否唯一；
- 是否保持連續、光滑或解析；
- 是否必須正規化來源；
- 是否必須改變目標類型。

### 4.5 值域與邊界譜 $V_p$

記錄：

- 原值域是否足夠；
- 是否需緊化；
- 是否加入無窮遠點；
- 是否到達邊界；
- 是否存在邊界重數。

### 4.6 失敗層 $C_p$

可取：

$$
C_p
\in
\{
\mathrm{source},
\mathrm{relation},
\mathrm{projection},
\mathrm{representation},
\mathrm{codomain},
\mathrm{boundary},
\mathrm{measure},
\mathrm{dynamics}
\}.
$$

---

## 5. 案例一：節點 $xy=0$

考慮：

$$
C_N
=
\{(x,y)\in\mathbb R^2:xy=0\}.
$$

它由兩條分支組成：

$$
L_x=\{(t,0):t\in\mathbb R\},
$$

$$
L_y=\{(0,s):s\in\mathbb R\}.
$$

其來源空間可取：

$$
\widetilde C_N
=
\mathbb R_x
\sqcup
\mathbb R_y.
$$

定義：

$$
\nu_N(t,x\text{-branch})=(t,0),
$$

$$
\nu_N(s,y\text{-branch})=(0,s).
$$

在原點：

$$
\nu_N^{-1}(0,0)
=
\{0_x,0_y\}.
$$

故：

$$
b_N(0)=2.
$$

每個來源分支的微分皆正常：

$$
d\nu_{N,0_x}(1)=(1,0),
$$

$$
d\nu_{N,0_y}(1)=(0,1).
$$

所以：

$$
R_{N,0}=\{1,1\}.
$$

其切錐為：

$$
xy=0,
$$

包含兩條不同切線：

$$
x=0,
\qquad
y=0.
$$

因此節點的 X 奇點證書可寫為：

$$
\boxed{
\operatorname{XSingCert}_N(0)
=
\left\langle
B=2,
R=\{1,1\},
T=\text{雙切線},
E=\text{正規化可分離來源},
V=\text{無需值域擴張},
C=\mathrm{source\ confluence}
\right\rangle.
}
$$

---

## 6. 節點的 X 解讀

節點的奇異性不來自來源本身。

每一條分支都是平滑的：

$$
\mathbb R_x,
\qquad
\mathbb R_y.
$$

問題出在空間實現中將兩個不同來源點識別為同一點：

$$
0_x\sim0_y.
$$

因此：

$$
C_N
=
\mathsf I_{\sim}
\left(
\mathbb R_x\sqcup\mathbb R_y
\right).
$$

但來源保存律要求：

$$
0_x
\not\equiv_{\mathrm{src}}
0_y.
$$

故節點是：

$$
\boxed{
\text{多來源合流型奇點。}
}
$$

其核心不是秩退化，而是：

$$
\boxed{
\text{多個正常來源在像空間中被積分至同一位置。}
}
$$

---

## 7. 節點的代數正規化

節點的座標環為：

$$
A_N
=
k[x,y]/(xy).
$$

其正規化可表現為：

$$
\widetilde A_N
\simeq
k[x]\times k[y].
$$

這個乘積分解對應兩個來源分支。

因此，X 來源微分與代數正規化得到一致結果：

$$
\mathsf D_{\mathrm{src}}(0)
=
\{L_x,L_y\}.
$$

---

## 8. 案例二：尖點 $y^2=x^3$

考慮：

$$
C_C
=
\{(x,y):y^2=x^3\}.
$$

它具有參數化：

$$
\nu_C(t)
=
(t^2,t^3).
$$

來源空間為：

$$
\widetilde C_C=\mathbb R.
$$

原點的來源纖維為：

$$
\nu_C^{-1}(0,0)=\{0\}.
$$

故：

$$
b_C(0)=1.
$$

但微分：

$$
d\nu_{C,t}
=
(2t,3t^2)
$$

在原點滿足：

$$
d\nu_{C,0}
=
(0,0).
$$

所以：

$$
R_{C,0}=\{0\}.
$$

切錐由最低次項：

$$
y^2
$$

決定，因此：

$$
y^2=0.
$$

它只有一條切線：

$$
y=0,
$$

但重數為 2。

尖點證書為：

$$
\boxed{
\operatorname{XSingCert}_C(0)
=
\left\langle
B=1,
R=\{0\},
T=\text{單切線、重數二},
E=\text{正規化可修復參數來源},
V=\text{無需值域擴張},
C=\mathrm{projection\ degeneracy}
\right\rangle.
}
$$

---

## 9. 尖點的 X 解讀

尖點只有一個來源分支。

沒有兩個不同來源在原點相撞。真正問題是：

$$
\boxed{
\text{來源向空間像的投影失去一階辨識能力。}
}
$$

即：

$$
\operatorname{rank}(d\nu_{C,0})=0.
$$

因此尖點是：

$$
\boxed{
\text{單來源投影退化型奇點。}
}
$$

其代數座標環為：

$$
A_C
=
k[x,y]/(y^2-x^3)
\simeq
k[t^2,t^3].
$$

其正規化為：

$$
\widetilde A_C=k[t].
$$

這表示來源本身是一條正常線，但空間實現退化。

---

## 10. 節點與尖點的區分

兩者都滿足：

$$
\nabla F(0)=0.
$$

但其 X 證書不同。

### 節點

$$
B=2,
\qquad
R=\{1,1\}.
$$

### 尖點

$$
B=1,
\qquad
R=\{0\}.
$$

因此：

$$
\boxed{
\text{多來源正常合流}
\neq
\text{單來源投影退化}.
}
$$

這說明單一 Jacobian 奇異判定不足以揭露奇點機制。

---

## 11. 案例三：可去奇點 $\sin z/z$

考慮：

$$
f(z)=\frac{\sin z}{z},
\qquad
z\neq0.
$$

其原表示式在：

$$
z=0
$$

不可形成。

但 Taylor 展開給出：

$$
\sin z
=
z-\frac{z^3}{3!}+\frac{z^5}{5!}-\cdots,
$$

所以：

$$
\frac{\sin z}{z}
=
1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots.
$$

右側在原點合法。

定義：

$$
\widetilde f(z)
=
1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots.
$$

則：

$$
\widetilde f(0)=1,
$$

且：

$$
\widetilde f(z)=\frac{\sin z}{z}
$$

在穿孔鄰域成立。

---

## 12. 表示式與結構分離

必須區分：

### 語法表示

$$
E(z)=\frac{\sin z}{z}.
$$

在原點：

$$
\Gamma\nvdash E(0)\;\operatorname{form}.
$$

### 穿孔鄰域函數

$$
f:U\setminus\{0\}\to\mathbb C.
$$

它在自己的定義域內完全合法。

### 解析函數胚

$$
\widetilde f\in\operatorname{Hol}(U).
$$

它在原點也完全正常。

因此：

$$
\boxed{
\text{失敗的是表示式，不是函數胚。}
}
$$

---

## 13. 可去奇點的補全守衛

若要合法補入：

$$
(0,L),
$$

至少需要：

$$
\mathsf G_{\mathrm{rem}}
=
G_{\mathrm{limit}}
\land
G_{\mathrm{unique}}
\land
G_{\mathrm{local}}
\land
G_{\mathrm{analytic}}.
$$

即：

1. 極限存在；
2. 極限唯一；
3. 補全後限制於穿孔鄰域仍等於原函數；
4. 補全後保持解析類型。

對 $\sin z/z$ ：

$$
\lim_{z\to0}\frac{\sin z}{z}=1.
$$

所以：

$$
\Gamma\vdash
\mathsf I_{\mathrm{completion}}
\left(
f;(0,1)
\right)
:
\operatorname{Hol}(U,\mathbb C).
$$

---

## 14. 可去奇點的 X 證書

其來源分支只有一個，圖像對基底投影正常，且存在唯一原值域解析補全。

因此：

$$
\boxed{
\operatorname{XSingCert}_R(0)
=
\left\langle
B=1,
R=\{1\},
T=\text{正常},
E=\text{原值域唯一解析延拓},
V=\mathbb C\text{ 不需擴張},
C=\mathrm{representation\ gap}
\right\rangle.
}
$$

故其 X 類型是：

$$
\boxed{
\text{表示缺口型奇點。}
}
$$

更準確地說：

$$
\boxed{
\text{它是表示式奇點，但不是完成後函數胚的真奇點。}
}
$$

---

## 15. 表示—結構分離原則

由此提出：

## 表示—結構分離原則

若某表示式 E 在 p 不可形成，但存在唯一同類型結構 $\widetilde X$ ，滿足：

$$
\widetilde X|_{U\setminus\{p\}}=X,
$$

且 $\widetilde X$ 在 p 正則，則 p 只是表示缺口，而不是完成結構的真奇點。

形式上：

$$
\boxed{
\Gamma\nvdash E(p)\;\operatorname{form}
}
$$

不推出：

$$
\boxed{
\Gamma\nvdash X(p)\;\operatorname{form}.
}
$$

---

## 16. 案例四：極點 $1/z$

考慮：

$$
f(z)=\frac1z,
\qquad
z\neq0.
$$

若要在原值域 $\mathbb C$ 中補入有限值 L，必須有：

$$
\lim_{z\to0}\frac1z=L.
$$

但：

$$
\left|\frac1z\right|\to\infty.
$$

不存在有限複數值補全。

其圖像為：

$$
\Gamma_f^\times
=
\{(z,w):zw=1\}.
$$

若在：

$$
U\times\mathbb C
$$

中補入 $(0,w_0)$ ，則須滿足：

$$
0\cdot w_0=1,
$$

不可能。

因此：

$$
\boxed{
\pi_z^{-1}(0)=\varnothing
}
$$

在普通複數值域中成立。

---

## 17. 值域擴張後的補全

將值域擴張為黎曼球面：

$$
\widehat{\mathbb C}
=
\mathbb C\cup\{\infty\}
\simeq
\mathbb P^1(\mathbb C).
$$

定義：

$$
\widetilde f(z)
=
\begin{cases}
\dfrac1z,&z\neq0,\\[4pt]
\infty,&z=0.
\end{cases}
$$

則：

$$
\widetilde f:
U\to\mathbb P^1
$$

成為合法映射。

在無窮遠局部座標：

$$
\eta=\frac1w
$$

下：

$$
w=\frac1z
$$

轉化為：

$$
\eta=z.
$$

因此在新的值域座標中，映射於原點正常：

$$
\frac{d\eta}{dz}=1.
$$

---

## 18. 極點的 X 類型

極點不是：

- 多來源合流；
- 單來源投影秩退化；
- 原值域內可補全的表示缺口。

它的真正問題是：

$$
\boxed{
\text{原值域缺少映射所到達的邊界點。}
}
$$

因此：

$$
\boxed{
\text{極點是有限值域不可補全、擴張值域可補全型奇點。}
}
$$

也可稱為：

$$
\boxed{
\text{值域邊界到達型奇點。}
}
$$

---

## 19. 極點的 X 證書

對一階極點：

$$
f(z)=\frac1z,
$$

可寫：

$$
\boxed{
\operatorname{XSingCert}_P(0)
=
\left\langle
B=1,
R_{\mathbb P^1}=\{1\},
T=\text{正常基底方向},
E_{\mathbb C}=0,\ E_{\mathbb P^1}=1,
V=\infty,
C=\mathrm{codomain\ boundary}
\right\rangle.
}
$$

其中：

- 原值域補全失敗；
- 擴張值域補全成功；
- 在黎曼球面座標中局部映射正常。

---

## 20. 高階極點與邊界重數

對：

$$
f(z)=\frac1{z^m},
$$

在無窮遠座標：

$$
\eta=\frac1w
$$

中：

$$
\eta=z^m.
$$

當：

$$
m=1,
$$

局部映射不分歧。

當：

$$
m>1,
$$

有：

$$
d\eta_0=0.
$$

因此高階極點在值域擴張後仍具有局部重數。

可提出：

$$
\boxed{
\operatorname{PoleOrder}
=
\operatorname{BoundaryMultiplicity}.
}
$$

此處極點階數被重新解讀為到達值域邊界時的覆蓋重數。

---

## 21. 四型分類總表

| 案例 | 來源分支 | 投影秩 | 原類型補全 | 擴張類型補全 | 主要失敗層 | X 類型 |
|---|---:|---|---|---|---|---|
| 節點 $xy=0$ | 2 | $\{1,1\}$ | 不能消除合流 | 正規化可分離 | 來源識別 | 來源合流型 |
| 尖點 $y^2=x^3$ | 1 | $\{0\}$ | 不能直接修復 | 正規化可修復來源 | 投影 | 投影退化型 |
| $\sin z/z$ | 1 | $\{1\}$ | 可以 | 不需要 | 表示 | 表示缺口型 |
| $1/z$ | 1 | 球面中 $\{1\}$ | 不可以 | 可以補 $\infty$ | 值域邊界 | 值域邊界型 |

因此：

$$
\boxed{
\text{來源合流}
\neq
\text{投影退化}
\neq
\text{表示缺口}
\neq
\text{值域邊界到達}.
}
$$

---

## 22. 修復代價分類

奇點也可依「修復時必須改變什麼」分類。

### 22.1 零代價修復

只需換用等價表示：

$$
\frac{\sin z}{z}
\rightsquigarrow
1-\frac{z^2}{3!}+\cdots.
$$

### 22.2 來源修復

需正規化來源空間：

$$
C_N
\rightsquigarrow
\mathbb R_x\sqcup\mathbb R_y,
$$

或：

$$
C_C
\rightsquigarrow
\mathbb R_t.
$$

### 22.3 投影修復

需改用更適合的參數化或來源實現。

### 22.4 值域修復

需擴張：

$$
\mathbb C
\hookrightarrow
\mathbb P^1.
$$

### 22.5 不可有限修復

可能需要多值化、覆蓋空間、分布、弱解或其他新範疇。

因此可定義修復代價：

$$
\operatorname{RepairCost}(p)
=
\min
\left\{
\text{需改變的結構層}
\right\}.
$$

---

## 23. 層級化不可形成判定

X 積分原先強調：

$$
\Gamma\nvdash X\;\operatorname{form}.
$$

奇點案例顯示，必須標明是哪一層不可形成。

例如：

$$
\Gamma\nvdash E(0)\;\operatorname{form}
$$

可能只表示原公式非法。

而：

$$
\Gamma\nvdash
\mathsf I_{\mathrm{completion}}(f;0)
:\operatorname{Hol}(U,\mathbb C)
$$

表示原類型補全失敗。

但仍可能有：

$$
\Gamma'\vdash
\mathsf I_{\mathrm{completion}}(f;0)
:\operatorname{Hol}(U,\mathbb P^1).
$$

因此，不可形成應細分為：

$$
\boxed{
\operatorname{Unformable}
\left(
\text{layer},
\Gamma,
\text{type}
\right).
}
$$

---

## 24. 奇點相對性原則

同一對象是否奇異，取決於上下文：

$$
\Gamma
=
\left\langle
\text{來源類型},
\text{目標類型},
\text{允許映射},
\text{邊界},
\text{補全規則}
\right\rangle.
$$

例如：

$$
f(z)=\frac1z.
$$

在：

$$
\Gamma_1
=
\operatorname{Hol}(-,\mathbb C)
$$

中，原點不可補全。

在：

$$
\Gamma_2
=
\operatorname{Hol}(-,\mathbb P^1)
$$

中，原點可映至 $\infty$ 。

所以：

$$
\boxed{
\operatorname{Singular}_{\Gamma_1}(f,0)
\neq
\operatorname{Singular}_{\Gamma_2}(f,0).
}
$$

這提出：

## 奇點相對性原則

$$
\boxed{
\text{奇點不是脫離類型與範疇而絕對存在的標記。}
}
$$

---

## 25. X 奇點與六大基本律

### 25.1 積分形成律

奇點顯示某種局部形成規則失敗，或需改變上下文才能形成。

### 25.2 來源保存律

節點證明：像空間中的同一點不可抹除不同來源分支。

### 25.3 非坍縮律

節點的兩個來源、尖點的局部重數、高階極點的邊界重數，均不可因像重合而消失。

### 25.4 再積分守衛律

補全、正規化或值域擴張都必須重新檢查類型、唯一性與邊界。

### 25.5 結構微分律

奇點分類依賴：

$$
\mathsf D_{\mathrm{src}},
\quad
\mathsf D_{\mathrm{rank}},
\quad
\mathsf D_{\mathrm{tangent}},
\quad
\mathsf D_{\mathrm{extension}},
\quad
\mathsf D_{\mathrm{boundary}}.
$$

### 25.6 動態整體閉合律

若局部修復後仍可形成一致整體，奇點可能被吸收；若無法跨迴路、尺度或時間閉合，則形成更高階奇點。

---

## 26. 一般化的 X 奇點判別流程

### 第一步：分離表示與結構

問：

- 是公式失效？
- 還是結構本身失效？

### 第二步：建立來源空間

尋找：

$$
\nu:\widetilde X\to X.
$$

### 第三步：計算來源纖維

$$
\nu^{-1}(p).
$$

### 第四步：計算秩譜

$$
\left\{
\operatorname{rank}(d\nu_q)
\right\}.
$$

### 第五步：檢查切向與重數

包括：

- 切錐；
- 分支數；
- 重切線；
- 局部覆蓋重數。

### 第六步：測試原類型延拓

判斷是否存在唯一：

$$
\widetilde X
$$

在原範疇內補全。

### 第七步：測試擴張類型延拓

若原類型失敗，檢查：

- 值域緊化；
- 來源正規化；
- 覆蓋空間；
- 分布範疇；
- 弱解範疇；
- 多值結構。

### 第八步：輸出 X 奇點證書

$$
\operatorname{XSingCert}(p).
$$

---

## 27. 第一版 X 奇點分類樹

$$
\operatorname{Singularity}(p)
$$

先分為：

### A. 表示層

原公式失敗，但底層結構可同類型補全：

$$
\Rightarrow
\text{表示缺口型}.
$$

### B. 來源層

多個正常來源被像空間識別：

$$
\Rightarrow
\text{來源合流型}.
$$

### C. 投影層

單一或多個來源的實現映射秩退化：

$$
\Rightarrow
\text{投影退化型}.
$$

### D. 值域層

原目標類型不足，擴張後可補全：

$$
\Rightarrow
\text{值域邊界型}.
$$

### E. 高階未分類

即使擴張值域或正規化仍無唯一局部閉合：

$$
\Rightarrow
\text{分支、本性、動態或其他高階奇點}.
$$

---

## 28. 本理論目前沒有完成的工作

### 28.1 未分類本性奇點

例如：

$$
e^{1/z}
$$

在原點無法靠加入單一有限值或無窮遠點補全。

### 28.2 未分類分支點

例如：

$$
\sqrt z
$$

的問題不是局部值不存在，而是全域繞圈後分支交換。

### 28.3 未分類分布奇點

例如 Dirac delta 的零測度支撐與非零作用。

### 28.4 未分類動態奇點

例如 Burgers 激波中的光滑解破裂與弱解類型轉換。

### 28.5 未分類測度奇點

例如測度發散但底層結構仍可形成的情況。

### 28.6 尚未證明分類完備性

本文四型只是一組基礎類型，不是一般奇點的完備分類。

---

## 29. 理論風險

### 29.1 過度重述風險

若 X 奇點論只替既有分類換名，則缺乏新增價值。

其真正價值必須來自：

- 跨領域統一；
- 層級判定；
- 修復代價；
- 可機器判定的證書；
- 對新案例產生可檢驗差異。

### 29.2 上下文任意化風險

若可任意改變來源與值域，任何奇點似乎都能被「修復」。

因此類型擴張必須受守衛限制：

- 最小擴張；
- 來源保存；
- 唯一性；
- 非坍縮；
- 與原結構相容。

### 29.3 正規化並非消除全部奇異性

正規化可改善來源，但不一定保留嵌入、切向或外部幾何。

### 29.4 局部正常不代表全域正常

局部補全可能在全域迴路、拓撲或動態下失敗。

---

## 30. 後續研究方向

### 30.1 本性奇點

比較：

$$
\frac1z
$$

與：

$$
e^{1/z}.
$$

建立：

$$
\text{單一邊界值可補全}
\neq
\text{輸出簇集不可單點補全}.
$$

### 30.2 分支點

研究：

$$
w^2=z.
$$

建立：

$$
\text{局部合法}
\neq
\text{全域動態閉合}.
$$

### 30.3 Dirac delta

研究：

$$
\operatorname{supp}\delta_0=\{0\}
$$

但：

$$
\langle\delta_0,\varphi\rangle=\varphi(0).
$$

建立零測度支撐與非零作用分類。

### 30.4 Burgers 激波

研究：

$$
u_t+uu_x=0
$$

中的：

$$
\text{光滑解}
\to
\text{梯度爆破}
\to
\text{弱解}.
$$

### 30.5 X 奇點證書系統

將：

$$
\operatorname{XSingCert}
$$

形式化為可計算資料結構與推導規則。

---

## 31. 結論

本文建立了 X 奇點論的第一個基礎版本。

四個表面上都在原點「出問題」的案例，被區分為四種不同結構機制：

$$
xy=0
\quad\Rightarrow\quad
\text{來源合流},
$$

$$
y^2=x^3
\quad\Rightarrow\quad
\text{投影退化},
$$

$$
\frac{\sin z}{z}
\quad\Rightarrow\quad
\text{表示缺口},
$$

$$
\frac1z
\quad\Rightarrow\quad
\text{值域邊界到達}.
$$

因此：

$$
\boxed{
\text{奇點不是單一異常，而是不同結構層的形成、投影、延拓或邊界問題。}
}
$$

本文最重要的結果不是重新命名四個已知案例，而是提出一個共同判斷框架：

$$
\boxed{
\text{先找失敗層，再判定奇點類型。}
}
$$

以及：

$$
\boxed{
\text{修復奇點時必須改變哪一層，本身就是奇點類型的一部分。}
}
$$

第一版 X 奇點證書為：

$$
\boxed{
\operatorname{XSingCert}(p)
=
\left\langle
B_p,
R_p,
T_p,
E_p,
V_p,
C_p
\right\rangle.
}
$$

它保存：

- 來源分支；
- 投影秩；
- 切向與重數；
- 延拓能力；
- 值域與邊界；
- 失敗層級。

這使 X 積分不再只判斷某個結構能否形成，也開始回答：

> 當形成失敗時，究竟是哪個層級失敗，以及最小合法修復需要改變什麼。

---

## 附錄 A：四種核心證書

### 節點

$$
\operatorname{XSingCert}_N(0)
=
\left\langle
2,
\{1,1\},
\text{雙切線},
\text{來源正規化},
\text{無值域擴張},
\mathrm{source}
\right\rangle.
$$

### 尖點

$$
\operatorname{XSingCert}_C(0)
=
\left\langle
1,
\{0\},
\text{單切線重數二},
\text{來源正規化},
\text{無值域擴張},
\mathrm{projection}
\right\rangle.
$$

### 可去奇點

$$
\operatorname{XSingCert}_R(0)
=
\left\langle
1,
\{1\},
\text{正常},
\text{原值域唯一解析延拓},
\mathbb C,
\mathrm{representation}
\right\rangle.
$$

### 極點

$$
\operatorname{XSingCert}_P(0)
=
\left\langle
1,
\{1\}_{\mathbb P^1},
\text{邊界重數一},
\text{原值域失敗、擴張值域成功},
\infty,
\mathrm{codomain}
\right\rangle.
$$

---

## 附錄 B：一句話定義

> X 奇點是某個結構在來源、投影、表示、值域、邊界、測度或動態層中的局部合法性失敗、退化或非唯一閉合；其類型由失敗層與最小修復代價共同決定。
