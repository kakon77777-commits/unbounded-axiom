# 歸心後的等變拓樸判定域
## 黎曼猜想的除子固定點與繞數障礙重構

**英文題名：** *The Equivariant Topological Decision Domain after Re-centering: A Reconstruction of the Riemann Hypothesis via Divisor Fixed Points and Winding Obstructions*  
**作者：** Neo.K（許筌崴）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1（內部研究稿）  
**日期：** 2026-07-24  
**性質：** 數學方法論／等變拓樸／複分析／形式化基礎／RH 合法證明研究  
**狀態：** 非公開定稿；不構成黎曼猜想證明

---

## 重要聲明：本文不是黎曼猜想的證明

本文不宣稱證明黎曼猜想，也不宣稱本文建立的等變拓樸判定框架足以推出黎曼猜想。

本文研究的問題更為前置：

> **黎曼猜想若要獲得一個合法、可審查、可形式化且不偷渡結論的證明，其定義域、判定域、中介映射、不變量、障礙量與提升程序應滿足哪些條件？**

本文只保留早期研究中的「歸心」操作，並放棄將核化、零點鎖定、能量、熱流、相位、勢阱或物理碰撞直覺直接當作 RH 證明機制。這些方法可以是啟發、表示或輔助工具，但只有在其定義域、作用域、等價性與提升定理均被嚴格證明後，才能合法參與原命題的推導。

本文的主要成果是建立一個型別安全的重構：

1. 將臨界線表為一個標記對合的不動點集；
2. 將非平凡零點表為帶群作用的局部有限除子；
3. 將 RH 改寫為除子投影算子的固定點條件；
4. 將偏軸零點改寫為半帶邊界映射的非零繞數障礙；
5. 以 TOPO 纖維準則檢驗任何中介表示是否遺失 RH 的必要資訊；
6. 說明一個完整證明仍需額外建立的解析—算術提升定理。

這些重述只是在研究 RH **如何才可能被合法證明**，而不是已經完成證明。

---

# 摘要

黎曼猜想通常被表述為黎曼 ζ 函數所有非平凡零點均位於臨界線
$$
\operatorname{Re}s=\frac12.
$$
此命題看似是一個零點位置問題，但大量候選路線的主要缺陷，往往不是局部計算錯誤，而是定義域、判定域與中介方法之間缺乏合法的型別關係。對稱性被誤當成軸向固定，積分核被誤當成原函數本體，物理形變被誤當成數學等價，有限驗證被誤當成無限命題，而拓樸直覺則可能在遺忘座標與標記後失去「哪一條線是臨界線」的資訊。

本文提出一個歸心後的等變拓樸判定框架。首先定義
$$
F(z)=\xi\left(\frac12+z\right),
$$
使原臨界線轉化為虛軸。再於臨界帶
$$
X=\left\{z\in\mathbb C:\left|\operatorname{Re}z\right|<\frac12\right\}
$$
上引入反射對合
$$
j(z)=-\overline z,
$$
其不動點集正是
$$
A=\operatorname{Fix}(j)=i\mathbb R.
$$
功能方程與實結構生成群
$$
G\cong C_2\times C_2
$$
對零點集的等變作用。令 $D_F$ 為 $F$ 的零點除子，並令
$$
r(z)=i\,\operatorname{Im}z
$$
為 $X$ 到 $A$ 的連續收縮。其除子推前算子
$$
\mathcal R(D)=r_*D
$$
為冪等算子，且
$$
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
$$

為避免固定點重述只成為同義反覆，本文進一步建立半帶繞數障礙。對任意 $\varepsilon>0$ 與高度 $T>0$ ，在右半臨界帶矩形
$$
U_{\varepsilon,T}^{+}
=
\left\{
z:
\varepsilon<\operatorname{Re}z<\frac12, 
|\operatorname{Im}z|<T
\right\}
$$
的零點自由邊界上，定義相位映射
$$
\phi_{\varepsilon,T}(z)=\frac{F(z)}{|F(z)|}.
$$
其拓樸度數
$$
\omega_{\varepsilon,T}(F)
=
\deg\phi_{\varepsilon,T}
$$
由辯值原理等於該矩形內按重數計算的零點數。故 RH 等價於所有此類右半帶障礙均消失。

本文亦引入 TOPO 纖維完備性準則：若一個粗化映射的同一纖維中同時包含滿足軸上零點性質與不滿足該性質的函數，則該中介層不可能單獨判定 RH。此準則可嚴格說明，偶性、共軛對稱、函數階、一般核正性或裸拓樸類型均不足以完成判定。

本文最後提出一個六層合法證明架構：原始解析定義、歸心同構、等變拓樸抽取、離散障礙建立、解析—算術提升、ZFC 依賴審計。真正尚未完成的核心，不是重新命名「零點鎖定」，而是證明一條不循環的提升定理：
$$
\text{$\xi$ 的原始解析與算術結構}
\Longrightarrow
\omega_{\varepsilon,T}(F)=0
\quad
\text{對所有合法 }(\varepsilon,T).
$$

**關鍵詞：** 黎曼猜想、歸心、等變拓樸、除子、不動點、繞數、辯值原理、判定域、TOPO 纖維、ZFC、形式化證明

---

# 0. 基礎立場：ZFC、原始命題與證明依賴

## 0.1 研究立場

本文採取以下內部方法論立場：

> **黎曼猜想的原始命題應被視為通常 ZFC 數學框架中的命題；一個被稱為「無條件完成原始 RH」的證明，最終應能被還原、編譯或形式化為 ZFC 內的推導，或位於對相關語句保守且可消去的擴張系統中。**

這不是一個已被證明的元數學定理，也不是在宣稱 RH 必然可由 ZFC 證明。目前不能預設：

$$
\mathrm{ZFC}\vdash\mathrm{RH},
$$

也不能預設：

$$
\mathrm{ZFC}\nvdash\mathrm{RH}.
$$

本文只要求候選證明清楚列出其公理依賴。

若某個理論 $T$ 嚴格強於 ZFC，且只能得到

$$
T\vdash\mathrm{RH},
$$

但不能消去額外公理，也不能轉譯為

$$
\mathrm{ZFC}\vdash\mathrm{RH},
$$

則依本文的命名規則，該結果應稱為：

> **理論 $T$ 下的 RH 定理**

而不直接稱為未附條件的原始 RH 證明。

## 0.2 數學語言不等於額外公理

使用下列工具並不自動違反上述要求：

- 拓樸學；
- 代數幾何；
- 範疇論；
- 譜論；
- 機率；
- 計算機驗證；
- Lean、Coq 或其他證明助理；
- 暫時性的模型或物理啟發。

真正需要審計的是：

1. 對象是否仍在原命題的合法定義域中；
2. 中介轉換是否有雙向等價或合法提升；
3. 是否加入不可消去的額外公理；
4. 最終定理是否仍是原始 RH，而不是類比命題；
5. 形式化核心是否可追溯至明確公理與已證定理。

因此，本研究採用的最小證明依賴標記為：

$$
\mathfrak D(\Pi)
=
\left(
\mathsf{Base},
\mathsf{Defs},
\mathsf{Imports},
\mathsf{Extra},
\mathsf{Eliminable}
\right),
$$

其中 $\Pi$ 為候選證明。只有當額外依賴為空，或已證明可消去時，才通過本文的「原始命題完整性」審計。

---

# 1. 問題重置：只保留歸心

## 1.1 完成函數

定義黎曼完成函數

$$
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}
\Gamma\left(\frac s2\right)\zeta(s).
$$

它是整函數，並滿足

$$
\xi(s)=\xi(1-s)
$$

以及

$$
\xi(\overline s)=\overline{\xi(s)}.
$$

其零點恰好對應 ζ 函數的非平凡零點，並保留重數。

## 1.2 歸心坐標

令

$$
z=s-\frac12,
\qquad
F(z)=\xi\left(\frac12+z\right).
$$

此變換是複平面的平移同構，不改變：

- 零點重數；
- 解析性；
- 局部拓樸；
- 零點計數；
- 原命題真假。

功能方程變為

$$
F(-z)=F(z),
$$

實結構變為

$$
F(\overline z)=\overline{F(z)}.
$$

RH 變為：

$$
\boxed{
F(z)=0
\Longrightarrow
\operatorname{Re}z=0.
}
$$

因此，本文保留歸心，不把歸心當作證明，而把它當作一個合法的座標正規化。

## 1.3 為何其他舊機制暫不保留

下列操作不能在未證明等價前直接承擔 RH：

- 將 $F$ 替換為某個積分核；
- 將零點位置替換為能量極小；
- 將解析變形替換為物理時間演化；
- 將偏軸零點替換為粒子碰撞；
- 將對稱性直接提升為固定性；
- 將數值驗證提升為全域定理。

它們可能構成合法研究，但必須另外建立：

$$
\text{原域命題}
\iff
\text{中介域命題}.
$$

若只證明單向映射，則還必須證明足以返回原問題的提升定理。

---

# 2. 定義域、母域與判定域

## 2.1 四個不同層級

為避免型別混淆，本文區分四個域。

### （一）函數定義域

$$
F:\mathbb C\longrightarrow\mathbb C.
$$

### （二）零點候選母域

非平凡零點歸心後位於臨界帶

$$
X
=
\left\{
z\in\mathbb C:
-\frac12<\operatorname{Re}z<\frac12
\right\}.
$$

### （三）目標子空間

$$
A=i\mathbb R.
$$

RH 要求

$$
Z(F)\subseteq A,
$$

而不是只要求

$$
Z(F)\subseteq X.
$$

### （四）判定域

本文不把「零點被鎖定」當作判定域，而建立離散障礙空間

$$
\mathcal J
=
\prod_{\alpha\in\mathcal A}\mathbb N_0,
$$

其中每一個座標記錄一個合法半帶區域內的偏軸零點數。判定映射記為

$$
\Omega:\mathcal E\longrightarrow\mathcal J.
$$

最終：

$$
\mathrm{RH}
\iff
\Omega(F)=\mathbf 0.
$$

## 2.2 函數類而非單一函數

定義一個最低限度的函數類

$$
\mathcal E
=
\left\{
f\in\operatorname{Hol}(\mathbb C):
f(-z)=f(z),
f(\overline z)=\overline{f(z)},
\operatorname{ord}(f)\le 1
\right\}.
$$

具體的 $F$ 滿足

$$
F\in\mathcal E.
$$

引入 $\mathcal E$ 的目的不是把 RH 泛化，而是檢查某個方法究竟使用了 $F$ 的哪些特有結構。

若一個論證只使用所有 $f\in\mathcal E$ 共有的資料，而 $\mathcal E$ 中存在偏軸零點函數，則該論證不可能只靠這些資料推出 RH。

---

# 3. 帶對合的等變拓樸

## 3.1 裸拓樸的不足

若只把 $X$ 看成未標記的拓樸空間，虛軸並不具有不可移動的特殊身份。平面上的不同嵌入直線可被同胚互相搬移。

因此，僅說「使用拓樸」不足以保留臨界線。

真正需要保存的是：

$$
(X,j),
$$

即一個帶有標記對合的拓樸空間。

## 3.2 臨界對合

定義

$$
j:X\longrightarrow X,
\qquad
j(z)=-\overline z.
$$

則

$$
j^2=\operatorname{id}_X.
$$

而且

$$
j(z)=z
\iff
z=-\overline z
\iff
\operatorname{Re}z=0.
$$

故

$$
\boxed{
A=\operatorname{Fix}(j)=i\mathbb R.
}
$$

這使臨界線不再只是外加的一條線，而成為標記對合的固定點集。

## 3.3 Klein 四群作用

再定義

$$
a(z)=-z,
\qquad
b(z)=\overline z.
$$

則

$$
a^2=b^2=\operatorname{id},
\qquad
ab=ba=j.
$$

因此生成群

$$
G=\langle a,b\rangle
\cong C_2\times C_2.
$$

由 $F(-z)=F(z)$ 與實結構，零點除子在 $G$ 作用下不變。

對一般偏軸、非實點 $\rho$ ，其軌道為

$$
G\rho
=
\{
\rho,-\rho,\overline\rho,-\overline\rho
\},
$$

通常具有四個元素。

若 $\rho\in i\mathbb R$ ，則

$$
j(\rho)=\rho,
$$

軌道縮為

$$
G\rho=\{\rho,-\rho\}.
$$

所以 RH 可表為：

$$
\boxed{
\text{每一個零點均具有包含 }j\text{ 的非平凡穩定子。}
}
$$

但必須強調：

> 功能方程只保證零點除子為 $G$ -不變；RH 要求其支撐落在 $\operatorname{Fix}(j)$ 。群不變性不等於逐點固定性。

---

# 4. 零點除子與固定點算子

## 4.1 局部有限有效除子

令

$$
\operatorname{Div}_{\mathrm{lf}}^+(X)
$$

表示 $X$ 上的局部有限有效除子。其元素形式為

$$
D
=
\sum_{\rho\in X}m_\rho[\rho],
\qquad
m_\rho\in\mathbb N_0,
$$

且任意緊子集只與有限多個支撐點相交。

令 $D_F$ 為 $F$ 在 $X$ 中的零點除子：

$$
D_F
=
\operatorname{div}_0(F)
=
\sum_{F(\rho)=0}m_\rho[\rho].
$$

由整函數零點的離散性， $D_F$ 局部有限。

## 4.2 軸向收縮

定義

$$
r:X\longrightarrow A,
\qquad
r(z)
=
\frac{z+j(z)}2
=
i\,\operatorname{Im}z.
$$

它滿足

$$
r|_A=\operatorname{id}_A
$$

以及

$$
r\circ r=r.
$$

因此 $r$ 是 $X$ 到 $A$ 的連續收縮。

## 4.3 除子推前算子

將 $A$ 視為 $X$ 的子空間，定義

$$
\mathcal R:
\operatorname{Div}_{\mathrm{lf}}^+(X)
\longrightarrow
\operatorname{Div}_{\mathrm{lf}}^+(X),
\qquad
\mathcal R(D)=r_*D.
$$

若

$$
D=\sum_\rho m_\rho[\rho],
$$

則

$$
\mathcal R(D)
=
\sum_\rho m_\rho[r(\rho)],
$$

相同像點的重數相加。

由 $r^2=r$ ，得到

$$
\mathcal R^2=\mathcal R.
$$

故 $\mathcal R$ 是冪等算子。

## 4.4 固定點等價

### 命題 4.1

對任意 $D\in\operatorname{Div}_{\mathrm{lf}}^+(X)$ ，

$$
\mathcal R(D)=D
\iff
\operatorname{supp}D\subseteq A.
$$

### 證明

若 $\operatorname{supp}D\subseteq A$ ，則 $r$ 在每個支撐點上為恆等，故 $\mathcal R(D)=D$ 。

反之， $\mathcal R(D)$ 的支撐包含於 $A$ 。若 $\mathcal R(D)=D$ ，則 $D$ 的支撐亦包含於 $A$ 。證畢。

### 推論 4.2

$$
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
$$

這是 RH 的除子固定點形式。

## 4.5 此算子的真實地位

$\mathcal R$ 的定義沒有使用「RH 為真」，因為：

- $X$ 由已知臨界帶決定；
- $j$ 由已知功能方程與實結構決定；
- $A=\operatorname{Fix}(j)$ 可獨立定義；
- $r$ 是明確公式。

但 $\mathcal R$ 仍然只是**診斷算子**，不是證明算子。

它告訴我們：

$$
\text{RH 等價於 }D_F\text{ 是某個冪等算子的固定點},
$$

卻沒有說明為什麼 $D_F$ 必須是固定點。

這對應 M6 方法中必須區分的兩件事：

1. 建立不循環的固定點刻畫；
2. 建立能從原始結構推出固定性的實質定理。

本文目前只完成第一件事。

---

# 5. 偏軸除子障礙

## 5.1 自由除子群中的差

將有效除子嵌入局部有限整係數除子群

$$
\operatorname{Div}_{\mathrm{lf}}(X).
$$

定義

$$
\Theta(D)
=
D-\mathcal R(D).
$$

則

$$
\Theta(D)=0
\iff
\mathcal R(D)=D.
$$

故

$$
\boxed{
\mathrm{RH}
\iff
\Theta(D_F)=0.
}
$$

$\Theta(D_F)$ 可稱為「偏軸除子障礙」。

## 5.2 為何還需要繞數

$\Theta$ 仍直接使用完整零點除子，因此計算上接近原問題。它適合表示邏輯結構，但尚未提供從邊界資料判定內部偏軸零點的方法。

為此，需要將除子障礙投影到整數值拓樸不變量。

---

# 6. 右半帶與繞數障礙

## 6.1 為何只需研究右半帶

若存在偏軸零點 $\rho$ ，則由 $j$ 對稱，

$$
j(\rho)=-\overline\rho
$$

也是零點，且兩者實部相反。

因此任意偏軸零點軌道中至少有一個零點滿足

$$
\operatorname{Re}\rho>0.
$$

故排除右半帶零點便足以排除全部偏軸零點。

## 6.2 截斷區域

對

$$
0<\varepsilon<\frac12,
\qquad
T>0,
$$

定義右半帶開矩形

$$
U_{\varepsilon,T}^+
=
\left\{
z\in X:
\varepsilon<\operatorname{Re}z<\frac12,
|\operatorname{Im}z|<T
\right\}.
$$

令

$$
N_{\varepsilon,T}^+(F)
$$

表示其中零點總數，按重數計算。

即使邊界上有零點，這個開集零點數仍有明確意義。

## 6.3 正則參數與相位映射

稱 $(\varepsilon,T)$ 為 $F$-正則，若

$$
F(z)\ne0
\qquad
\text{對所有 }z\in\partial U_{\varepsilon,T}^+.
$$

對正則參數，定義

$$
\phi_{\varepsilon,T}:
\partial U_{\varepsilon,T}^+
\longrightarrow
S^1,
\qquad
\phi_{\varepsilon,T}(z)
=
\frac{F(z)}{|F(z)|}.
$$

其拓樸度數為

$$
\omega_{\varepsilon,T}(F)
=
\deg\phi_{\varepsilon,T}.
$$

由辯值原理，

$$
\omega_{\varepsilon,T}(F)
=
\frac{1}{2\pi i}
\oint_{\partial U_{\varepsilon,T}^+}
\frac{F'(z)}{F(z)}\,dz
=
N_{\varepsilon,T}^+(F).
$$

因 $F$ 為整函數，沒有極點項。

所以

$$
\omega_{\varepsilon,T}(F)\in\mathbb N_0.
$$

## 6.4 障礙族

令

$$
\mathcal A_F
=
\left\{
(\varepsilon,T):
0<\varepsilon<\frac12,
T>0,
(\varepsilon,T)\text{ 為 }F\text{-正則}
\right\}.
$$

定義

$$
\Omega(F)
=
\left(
\omega_{\varepsilon,T}(F)
\right)_{(\varepsilon,T)\in\mathcal A_F}.
$$

其值域為

$$
\mathcal J_F
=
\prod_{(\varepsilon,T)\in\mathcal A_F}
\mathbb N_0.
$$

### 定理 6.1：繞數障礙等價

$$
\boxed{
\mathrm{RH}
\iff
\omega_{\varepsilon,T}(F)=0
\quad
\text{對所有 }(\varepsilon,T)\in\mathcal A_F.
}
$$

### 證明

若 RH 成立，所有零點位於 $\operatorname{Re}z=0$ ，而 $U_{\varepsilon,T}^+$ 位於 $\operatorname{Re}z>\varepsilon>0$ ，故其中沒有零點，所以所有繞數為零。

反之，若 RH 不成立，存在零點 $\rho$ 滿足 $\operatorname{Re}\rho\ne0$ 。由對稱性可選取實部為正的零點。取

$$
0<\varepsilon<\operatorname{Re}\rho
$$

及

$$
T>|\operatorname{Im}\rho|.
$$

再對 $\varepsilon,T$ 作任意小擾動以避開離散零點集合，使邊界零點自由，則

$$
N_{\varepsilon,T}^+(F)\ge1,
$$

故

$$
\omega_{\varepsilon,T}(F)\ge1.
$$

矛盾。證畢。

## 6.5 可數判定族

為形式化與計算，可限制

$$
\varepsilon\in\mathbb Q\cap\left(0,\frac12\right),
\qquad
T\in\mathbb Q_{>0}.
$$

若存在偏軸零點，總可選取有理 $\varepsilon,T$ 包含它，並再選取正則有理邊界。因此一個可數障礙族已足以判定。

---

# 7. 拓樸在此處究竟完成了什麼

拓樸沒有證明

$$
\omega_{\varepsilon,T}(F)=0.
$$

拓樸完成的是以下轉換：

$$
\text{偏軸零點存在}
\longmapsto
\text{某個整數值度數非零}.
$$

其價值有三點。

## 7.1 離散化

偏軸零點的連續位置，被轉成

$$
\omega_{\varepsilon,T}\in\mathbb N_0.
$$

## 7.2 同倫穩定性

只要邊界映射在變形過程中不穿過零點，度數保持不變。

## 7.3 局部—全域橋接

邊界上的相位繞行，精確計數內部零點。

但拓樸不能自行解釋：

- 為什麼每個右半帶矩形的度數為零；
- 為什麼 ζ 函數的算術結構強迫零度數；
- 為什麼某個中介變形不會穿越零點；
- 為什麼有限高度結果可以提升至所有高度。

因此：

> **拓樸負責把障礙變得離散、穩定且可追蹤；解析與算術仍必須負責證明障礙消失。**

---

# 8. TOPO 纖維完備性檢查

## 8.1 粗化映射

設

$$
Q:\mathcal E\longrightarrow\mathcal T
$$

是一個中介粗化映射，只保留某些資料，例如：

- 偶性；
- 共軛實結構；
- 函數階；
- 一般增長類；
- 某種核表示；
- 某種未標記拓樸類型。

令命題

$$
P(f)
=
\begin{cases}
1,&Z(f)\subseteq i\mathbb R,\\
0,&\text{否則}.
\end{cases}
$$

若希望 $P$ 能下降為 $\mathcal T$ 上的判定，至少必須存在

$$
\overline P:\mathcal T\to\{0,1\}
$$

使

$$
P=\overline P\circ Q.
$$

## 8.2 纖維常值準則

必要條件是：

$$
Q(f)=Q(g)
\Longrightarrow
P(f)=P(g).
$$

也就是 $P$ 必須在 $Q$ 的每一條纖維上保持常值。

若存在

$$
f,g\in\mathcal E
$$

使

$$
Q(f)=Q(g)
$$

但

$$
P(f)\ne P(g),
$$

則 $Q$ 遺失了判定 RH 所需的資訊。

## 8.3 對稱、階與裸拓樸不足的明確反例

取

$$
f_0(z)=\cosh z.
$$

它是偶整函數，具有實係數，階為一，全部零點位於虛軸：

$$
z=i\pi\left(k+\frac12\right).
$$

取一個不位於實軸或虛軸的複數 $a$ ，定義

$$
q_a(z)
=
(z-a)(z+a)(z-\overline a)(z+\overline a).
$$

則 $q_a$ 為偶多項式且具有實係數。再令

$$
f_1(z)=f_0(z)q_a(z).
$$

則 $f_1$ 仍然：

- 是偶整函數；
- 滿足共軛實結構；
- 階為一；
- 與 $f_0$ 具有相同的一般對稱類型。

但 $f_1$ 額外具有偏軸四元組零點

$$
\{a,-a,\overline a,-\overline a\}.
$$

因此，只保留偶性、實結構與函數階的粗化映射，其同一纖維中可同時存在 $P=1$ 與 $P=0$ 的函數。

結論是：

$$
\boxed{
\text{功能方程型對稱資料不足以判定 RH。}
}
$$

同理，若一個核化、相位化或物理化表示使上述兩類函數落入同一纖維，該表示也不足以判定。

---

# 9. 空間狀態與型別安全

## 9.1 RH 的最小空間狀態

依空間狀態方法，可將本研究的最小狀態寫為

$$
\Sigma_{\mathrm{RH}}
=
\left(
B,
X,
F,
\Theta,
\mathcal A,
\mathcal P
\right),
$$

其中：

- $B=\mathbb C$ ：背景複平面；
- $X$ ：歸心後臨界帶；
- $F$ ：完成函數；
- $\Theta=(G,j,A)$ ：群作用、標記對合與固定點集；
- $\mathcal A$ ：合法算子，如除子形成、推前、邊界限制、度數；
- $\mathcal P$ ：觀測與粗化，如零點除子、截斷計數、繞數族。

任何方法加入新對象 $Y$ 時，都必須提供型別宣告：

$$
Y\in\mathsf{Type}(Y),
$$

以及合法映射：

$$
\alpha:X\to Y,
\qquad
\beta:Y\to\mathcal J.
$$

若最終要返回 RH，還需證明：

$$
\beta(\alpha(F))=0
\Longrightarrow
\Omega(F)=0.
$$

缺少此提升箭頭時，中介模型只能是啟發或類比。

## 9.2 合法複合條件

對跨域鏈

$$
\mathcal D_{\mathrm{RH}}
\xrightarrow{Q}
\mathcal T
\xrightarrow{B}
\mathcal K
\xrightarrow{L}
\mathcal J,
$$

必須逐一檢查：

1. $Q$ 的定義域是否包含 $F$ ；
2. $Q$ 遺忘哪些資訊；
3. $B$ 是否為良定義映射；
4. $L$ 是否能回到 RH 的判定域；
5. 複合 $L\circ B\circ Q$ 是否與 $\Omega$ 相容；
6. 相容是相等、單向蘊含，還是僅為經驗相關。

只有在存在交換關係

$$
L\circ B\circ Q
=
\Omega
$$

或至少存在足夠強的蘊含

$$
L(B(Q(F)))=0
\Longrightarrow
\Omega(F)=0
$$

時，中介方法才具有完成 RH 的邏輯資格。

---

# 10. M6 方法的移植與限制

M6 研究提供三個可移植原則。

## 10.1 先確定母域

M6 先建立 $M6^*$ ，再承認質數只是其中真子集。

在 RH 中相應地：

$$
Z(F)\subset X
$$

是已知母域限制，而

$$
Z(F)\subset A
$$

是待證子域限制。

不能把「位於臨界帶」誤當成「位於臨界線」。

## 10.2 算子不能循環定義

$\mathcal R$ 不以「哪些點是 RH 零點」為輸入，而只使用獨立定義的 $j$ 、 $A$ 與 $r$ 。

因此固定點刻畫在定義上不循環。

## 10.3 一肢定位與多肢佐證

M6 的形式化經驗要求區分：

- 哪一個算子真正完成唯一定位；
- 哪些統計或遍歷性質只提供佐證。

在 RH 中：

- $\mathcal R(D_F)=D_F$ 與 $\Omega(F)=0$ 是等價定位條件；
- 零點統計、有限驗證、平均分布與數值計算只能作佐證，除非另有全域提升定理。

本文不得將多個「看起來都支持 RH」的必要性質拼接成充分性。

---

# 11. 合法證明的六層架構

本文提出下列最低證明架構。

## 層一：原始解析層

在 ZFC 可形式化的複分析與數論中定義：

$$
\zeta,\quad \xi,\quad F.
$$

證明：

- 整性；
- 功能方程；
- 共軛相容性；
- 臨界帶位置；
- 零點離散性。

## 層二：歸心同構層

證明平移

$$
s\mapsto z=s-\frac12
$$

完整保存原命題。

## 層三：等變拓樸層

建立：

$$
(X,G,j,A),
$$

並證明

$$
A=\operatorname{Fix}(j).
$$

## 層四：判定障礙層

建立：

$$
D_F,\quad \mathcal R,\quad \Theta,\quad \Omega.
$$

證明等價鏈：

$$
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F
\iff
\Theta(D_F)=0
\iff
\Omega(F)=0.
$$

## 層五：實質提升層

這是目前完全未完成的核心。

需要找到不循環的資料集合 $\mathfrak S(F)$ ，並證明：

$$
\mathfrak S(F)
\Longrightarrow
\Omega(F)=0.
$$

$\mathfrak S(F)$ 必須來自 $\xi$ 的獨立解析或算術結構，不能把「沒有偏軸零點」以改名形式放入假設。

## 層六：基礎與形式化審計層

最後必須列出：

- 使用的 ZFC 公理；
- 引用定理；
- 額外假設；
- 計算證書；
- 經典邏輯依賴；
- 選擇公理依賴；
- 是否存在未消去的更強公理；
- 證明助理核心信任基礎。

---

# 12. 尚缺的核心定理

本文將真正待研究的缺口命名為：

## 等變障礙消失提升問題

尋找一組不循環、可形式化的 $\xi$ 結構條件 $\mathfrak S_\xi$ ，使

$$
\boxed{
\mathfrak S_\xi
\Longrightarrow
\omega_{\varepsilon,T}(F)=0
\quad
\text{對所有正則 }(\varepsilon,T).
}
$$

這個命題不能被下列同義句替代：

- 零點被鎖定在臨界線；
- 偏軸零點不能存在；
- 所有右半帶繞數為零；
- 除子為收縮算子固定點；
- 拓樸障礙消失。

這些都是 RH 的等價表達或直接重命名。

真正的新內容必須是：

$$
\text{已知或獨立可證的解析／算術結構}
\Longrightarrow
\text{障礙消失}.
$$

---

# 13. 不合法或不充分的捷徑

## 13.1 對稱即固定

錯誤形式：

$$
D_F\text{ 為 }G\text{-不變}
\Longrightarrow
\operatorname{supp}D_F\subseteq\operatorname{Fix}(j).
$$

群不變除子完全可以由四點軌道構成。

## 13.2 裸拓樸辨認臨界線

沒有標記對合 $j$ 時，拓樸不能區分虛軸與其他嵌入直線。

## 13.3 固定點重述即證明

$$
\mathcal R(D_F)=D_F
$$

雖然形式乾淨，仍只是 RH 的等價命題。

## 13.4 核表示自動保留零點判定

除非證明核映射對相關命題為纖維常值，否則核化可能遺失必要資訊。

## 13.5 物理動力學替代解析定理

能量、熱流、碰撞、相變或穩態語言若不能被編譯成合法數學映射與定理，只能視為類比。

## 13.6 有限高度驗證替代全域證明

證明

$$
\omega_{\varepsilon,T}(F)=0
$$

對所有 $T\le T_0$ ，不能推出所有 $T$ 。

必須另有尾部定理或無限提升。

## 13.7 更強公理未聲明

若候選證明使用額外公理 $A$ ，則必須標記為

$$
\mathrm{ZFC}+A\vdash\mathrm{RH},
$$

直到 $A$ 被消去或證明為保守擴張。

---

# 14. 形式化研究計畫

## 14.1 第一階段：等價框架

在 Lean 4／Mathlib 中建立：

1. 完成函數與歸心函數的接口；
2. 臨界帶 $X$ ；
3. 對合 $a,b,j$ ；
4. $G=C_2\times C_2$ 作用；
5. $A=\operatorname{Fix}(j)$ ；
6. 零點除子；
7. 收縮 $r$ ；
8. 冪等除子算子 $\mathcal R$ ；
9. RH 與固定點條件等價。

## 14.2 第二階段：繞數障礙

形式化：

1. 右半帶矩形；
2. 正則邊界；
3. $F/|F|$ 的圓值映射；
4. 拓樸度數；
5. 辯值原理；
6. 度數與零點數相等；
7. RH 與全障礙消失等價。

## 14.3 第三階段：TOPO 纖維測試器

對每個候選中介方法 $Q$ ，要求輸出：

$$
\operatorname{FiberTest}(Q,P).
$$

測試項目：

- 是否找到同纖維異判定反例；
- 遺失哪些不變量；
- 是否存在提升映射；
- 提升是否單值；
- 提升是否保重數；
- 提升是否保全域量詞；
- 是否加入額外公理。

## 14.4 第四階段：提升定理搜尋

只有前三階段完成後，才研究可能的 $\mathfrak S_\xi$ 。

研究目標不是再發明一個 RH 等價式，而是尋找：

$$
\mathfrak S_\xi
\not\equiv
\mathrm{RH}
$$

且

$$
\mathfrak S_\xi
\Longrightarrow
\Omega(F)=0.
$$

---

# 15. 可否證性與失敗條件

本框架的等價部分可被直接檢查。若以下任一點失敗，本文相應部分必須修正：

1. $j(z)=-\overline z$ 的固定點集不是虛軸；
2. $D_F$ 在 $X$ 中不是局部有限；
3. $\mathcal R$ 不是良定義的局部有限除子算子；
4. $\mathcal R^2\ne\mathcal R$ ；
5. $\mathcal R(D)=D$ 與支撐位於 $A$ 不等價；
6. 正則右半帶的繞數不等於內部零點數；
7. 可數有理參數族不足以捕捉任意偏軸零點；
8. ZFC 依賴聲明混淆了方法語言與公理依賴。

更重要的是，即使上述全部成立，也不能推出 RH。若無法建立層五的提升定理，本文應永久保持為：

> **RH 合法證明架構與判定域重構**

而不是 RH 證明。

---

# 16. 結論

本文只保留歸心。

歸心後，RH 的數學身份可以被乾淨地重寫為：

$$
F(z)=\xi\left(\frac12+z\right),
$$

$$
X=\left\{\left|\operatorname{Re}z\right|<\frac12\right\},
$$

$$
j(z)=-\overline z,
$$

$$
A=\operatorname{Fix}(j)=i\mathbb R,
$$

$$
D_F=\operatorname{div}_0(F).
$$

除子固定點形式為：

$$
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
$$

繞數障礙形式為：

$$
\boxed{
\mathrm{RH}
\iff
\omega_{\varepsilon,T}(F)=0
\quad
\text{對所有合法右半帶。}
}
$$

這兩個形式都沒有證明 RH。

它們完成的是：

1. 分離原始定義域與判定域；
2. 將臨界線變成標記對合的不動點集；
3. 將零點對稱與逐點固定嚴格區分；
4. 將偏軸零點轉化為整數值拓樸障礙；
5. 為任何中介方法建立纖維資訊損失檢查；
6. 為形式化與 ZFC 依賴審計提供清楚接口。

因此，本文對 RH 的核心判斷是：

> **RH 的困難不應再被含糊描述為「如何鎖定零點」，而應被精確描述為：如何從 $\xi$ 的獨立解析與算術結構，在不循環、不跨錯型別、不遺失全域量詞且不引入未聲明額外公理的條件下，證明整個等變繞數障礙族消失。**

真正的證明若存在，必須跨過的是這條提升箭頭：

$$
\boxed{
\text{原始解析／算術結構}
\Longrightarrow
\Omega(F)=\mathbf0.
}
$$

在這條箭頭被合法建立以前，一切固定點、拓樸、核、相位、動力學或計算結果，都只能是判定框架、局部證書、研究中介或類比，而不是原始黎曼猜想的完成證明。

---

# 附錄 A：最小符號表

| 符號 | 含義 |
|---|---|
| $\xi(s)$ | 黎曼完成函數 |
| $F(z)$ | 歸心後完成函數 $\xi(1/2+z)$ |
| $X$ | 歸心後臨界帶 |
| $a(z)$ | 中心反演 $-z$ |
| $b(z)$ | 複共軛 $\overline z$ |
| $j(z)$ | 臨界反射 $-\overline z$ |
| $G$ | $C_2\times C_2$ 對稱群 |
| $A$ | $\operatorname{Fix}(j)=i\mathbb R$ |
| $D_F$ | $F$ 的零點除子 |
| $r$ | 軸向收縮 $i\operatorname{Im}z$ |
| $\mathcal R$ | 除子推前冪等算子 |
| $\Theta$ | 偏軸除子障礙 $D-\mathcal R(D)$ |
| $U_{\varepsilon,T}^+$ | 右半帶截斷矩形 |
| $\omega_{\varepsilon,T}$ | 邊界相位映射的拓樸度數 |
| $\Omega(F)$ | 全部右半帶繞數障礙族 |
| $Q$ | TOPO 粗化／受控遺忘映射 |
| $\mathfrak S_\xi$ | 尚待發現的獨立提升條件 |

---

# 附錄 B：最小等價鏈

$$
\mathrm{RH}
$$

$$
\iff
Z(F)\subseteq i\mathbb R
$$

$$
\iff
\operatorname{supp}D_F\subseteq\operatorname{Fix}(j)
$$

$$
\iff
\mathcal R(D_F)=D_F
$$

$$
\iff
\Theta(D_F)=0
$$

$$
\iff
N_{\varepsilon,T}^+(F)=0
\quad
\text{對所有 }\varepsilon,T
$$

$$
\iff
\omega_{\varepsilon,T}(F)=0
\quad
\text{對所有正則 }\varepsilon,T.
$$

此鏈全部屬於重述與判定域重構，不包含 RH 的實質證明。

---

# 附錄 C：內部理論來源與角色

## C.1 M6\* 上的三重不動點刻畫

移植內容：

- 先建立候選母域；
- 目標子集與母域分離；
- 算子定義不得預設待判定性質；
- 固定點定位與統計佐證必須分工；
- 形式化會改變主張的精確形狀。

未移植內容：

- M6 的具體整除拓樸；
- 質數最小因子算子；
- 統計與遍歷算子本身。

## C.2 TOPO 學

移植內容：

- 拓樸作為受控遺忘；
- 粗化—中介—提升鏈；
- 纖維常值判定準則；
- 不變量存活失敗；
- 提升間隙；
- 交換圖不閉合殘餘。

## C.3 空間狀態論

移植內容：

- 底空間、型別、算子、觀測必須共同標記；
- 共同表示不等於共同運算；
- 粗粒化通常不可逆；
- 非法跨型別複合必須阻斷；
- 中介方法必須留下可追蹤接口。

---

# 附錄 D：版本邊界

v0.1 已完成：

- 非證明聲明；
- ZFC 方法論立場；
- 歸心後等變母空間；
- 除子固定點重述；
- 繞數障礙重述；
- TOPO 纖維不足準則；
- 六層合法證明架構；
- 形式化研究計畫。

v0.1 尚未完成：

- Lean 4 實作；
- 除子推前的完整形式化細節；
- 辯值原理接口；
- 外部數學文獻系統回顧；
- 非循環解析—算術提升定理；
- 任何形式的 RH 證明。
