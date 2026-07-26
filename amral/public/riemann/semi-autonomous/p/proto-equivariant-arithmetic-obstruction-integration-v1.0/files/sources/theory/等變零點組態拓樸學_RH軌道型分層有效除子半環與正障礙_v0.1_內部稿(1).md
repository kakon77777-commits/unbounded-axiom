# 等變零點組態拓樸學
## 黎曼猜想的軌道型分層、有效除子半環與正障礙

**英文題名：** *Equivariant Topology of Zero Configurations: Orbit-Type Stratification, Effective Divisor Semirings, and Positive Obstructions for the Riemann Hypothesis*  
**作者：** Neo.K（許筌崴）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1（內部研究稿）  
**日期：** 2026-07-24  
**性質：** 等變拓樸／複分析／零點組態／有效除子／RH 判定域研究  
**前置文件：**《從歸心到等變拓樸：RH 合法判定研究的思考方法與方法群》  
**狀態：** 內部稿；不構成黎曼猜想證明

---

## 重要聲明

本文不是黎曼猜想的證明。

本文建立的是黎曼猜想歸心後的第一個技術性拓樸分支：把完成函數的零點視為有限群作用下的局部有限有效除子，建立軌道型分解、組態空間拓樸、冪等軸向投影、有效軌道型半環、不可抵消的偏軸正障礙，以及依高度展開的障礙過濾。

本文所證明的主要命題均屬於下列類型：

1. 定義與良定義性；
2. 零點對稱的等變重述；
3. RH 與某些固定點或正障礙消失條件的等價；
4. 有限視窗中的軌道型分類；
5. 解析函數擾動與局部零點組態穩定性的接口。

上述結果不會自行推出所有偏軸障礙均為零。真正的 RH 證明仍需從 \(\xi\) 的獨立解析與算術結構，推出本文定義的全部偏軸正障礙消失。

---

# 摘要

令
\[
F(z)=\xi\left(\frac12+z\right),
\]
並令閉臨界帶與其內部為
\[
S=\left\{z\in\mathbb C:\left|\operatorname{Re}z\right|\le\frac12\right\},
\qquad
X=S^\circ.
\]
完成函數的非平凡零點全部位於 \(X\)。功能方程與共軛實結構在歸心後生成 Klein 四群
\[
G=\langle a,b\rangle\cong C_2\times C_2,
\qquad
a(z)=-z,\quad b(z)=\overline z,
\]
其中臨界反射
\[
j=ab,\qquad j(z)=-\overline z
\]
的不動點集正是虛軸
\[
A=\operatorname{Fix}(j)=i\mathbb R.
\]

本文將 \(F\) 的零點表示為 \(S\) 上、支撐位於 \(X\) 的局部有限 \(G\)-不變有效除子
\[
D_F=\sum_\rho m_\rho[\rho].
\]
有效除子亦可視為整數值正 Radon 測度。賦予局部有限除子空間 vague 拓樸後，可在有限高度視窗中研究零點軌道的產生、移動、合併與軌道型退化。

本文首先分類 \(G\) 在 \(S\) 上可實現的穩定子型別。一般偏軸且非實點具有平凡穩定子與四點軌道；非零虛軸點具有 \(\langle j\rangle\) 穩定子與兩點軌道；非零實軸點具有 \(\langle b\rangle\) 穩定子與兩點軌道；原點具有全群穩定子。RH 因而等價於 \(D_F\) 的全部支撐均位於包含 \(j\) 的軌道型層。

其次，本文在閉帶 \(S\) 上定義適當的軸向收縮
\[
r(z)=i\,\operatorname{Im}z.
\]
由於 \(S\) 在水平方向緊，\(r:S\to A\) 為 proper 連續映射，故能在局部有限除子上良定義推前
\[
\mathcal R(D)=r_*D.
\]
此算子連續且冪等，並滿足
\[
\mathcal R(D)=D
\iff
\operatorname{supp}D\subseteq A.
\]
因此
\[
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
\]

為防止偏軸障礙在群化後因正負係數抵消，本文引入有限 \(G\)-集合的正 Burnside 半環
\[
A^+(G),
\]
以及有限視窗內的軌道型值
\[
\tau_W(D)\in A^+(G).
\]
透過保留所有穩定子不包含 \(j\) 的生成元，定義偏軸正投影
\[
\pi_{\mathrm{off}}^+.
\]
由於係數位於 \(\mathbb N_0\)，此障礙不能以代數消去。有限視窗中的 RH 條件等價於
\[
\pi_{\mathrm{off}}^+\tau_W(D_F)=0.
\]

最後，本文以高度視窗
\[
S_T=\{z\in S:|\operatorname{Im}z|\le T\}
\]
建立單調的偏軸障礙輪廓
\[
\beta_D(T)=D(S_T\setminus A).
\]
它是非負整數值、右連續的階梯型輪廓；RH 等價於
\[
\beta_{D_F}(T)=0
\qquad
\forall T\ge0.
\]
此輪廓提供有限驗證、繞數證書、局部除子層與後續算術分離方法的共同接口，但不允許將有限高度零障礙自動提升為全高度結論。

**關鍵詞：** 黎曼猜想、等變拓樸、零點組態、有效除子、Burnside 半環、軌道型、正障礙、vague 拓樸、高度過濾、固定點

---

# 1. 研究目的與位置

## 1.1 本文要處理的問題

前置研究已將 RH 重構為歸心後的等變拓樸判定問題：

\[
F(z)=\xi\left(\frac12+z\right),
\]

\[
F(z)=0
\Longrightarrow
z\in i\mathbb R.
\]

但單純寫成
\[
Z(F)\subseteq i\mathbb R
\]
仍不足以形成一個可擴展的方法群。

本文進一步問：

1. 無限零點集應放在哪一個拓樸空間中？
2. 對稱零點四元組如何被表示為軌道型？
3. 零點重數如何保留？
4. 偏軸零點如何成為不可抵消的正障礙？
5. 高度增加時，障礙如何被過濾與追蹤？
6. 解析函數的局部擾動如何映射到零點組態的拓樸變化？
7. 哪些結果只是 RH 的等價重述，哪些結果可能成為後續證明接口？

## 1.2 本文在整體方法群中的位置

整體研究鏈為：

\[
\text{歸心}
\to
\boxed{\text{等變零點組態拓樸}}
\to
\text{層化局部—全域}
\to
\text{拓樸分離}
\to
\text{解析可容許提升}
\to
\text{算術符號控制}.
\]

本文只完成方框中的部分。

## 1.3 與「零點鎖定」語言的區別

本文不使用「零點被某種力鎖定」作為數學前提。

本文只定義：

- 哪些組態是軸上組態；
- 哪些組態包含偏軸軌道；
- 軸上組態是否為某個算子的固定點；
- 偏軸軌道是否產生非零正障礙。

這些定義本身不包含零點為何必須在軸上的原因。

---

# 2. 歸心後的等變母空間

## 2.1 完成函數與歸心

定義

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}
\Gamma\left(\frac s2\right)\zeta(s),
\]

以及

\[
F(z)=\xi\left(\frac12+z\right).
\]

由功能方程與實結構：

\[
F(-z)=F(z),
\qquad
F(\overline z)=\overline{F(z)}.
\]

## 2.2 閉帶與開帶

定義閉臨界帶：

\[
S
=
\left\{
z\in\mathbb C:
\left|\operatorname{Re}z\right|
\le\frac12
\right\},
\]

以及其內部：

\[
X
=
\left\{
z\in\mathbb C:
\left|\operatorname{Re}z\right|
<\frac12
\right\}.
\]

非平凡零點位於 \(X\)。

本文特意在 \(S\) 而不是只在 \(X\) 上建立除子拓樸，原因是軸向投影

\[
r(z)=i\,\operatorname{Im}z
\]

在閉帶 \(S\) 上為 proper 映射。這可保證局部有限除子的推前仍局部有限。

若只在開帶 \(X\) 上考慮任意局部有限除子，可能存在無限多個點在有限高度內向垂直邊界聚集，使投影後在虛軸有限區間內產生無限質量。因此，先前的除子推前必須補上 properness 條件。

## 2.3 群作用

定義

\[
a(z)=-z,
\]

\[
b(z)=\overline z,
\]

\[
j(z)=a(b(z))=-\overline z.
\]

則

\[
a^2=b^2=j^2=\operatorname{id},
\qquad
ab=ba=j.
\]

因此

\[
G=\{e,a,b,j\}
\cong C_2\times C_2.
\]

\(G\) 連續作用於 \(S\) 與 \(X\)。

## 2.4 臨界線作為標記固定集

有：

\[
j(z)=z
\iff
z=-\overline z
\iff
\operatorname{Re}z=0.
\]

故

\[
A
=
\operatorname{Fix}(j)
=
i\mathbb R.
\]

這裡的 \(A\) 不是裸拓樸空間中任意選取的直線，而是帶標記對合 \(j\) 的固定點集。

---

# 3. 點軌道與穩定子型別

## 3.1 穩定子

對 \(z\in S\)，定義

\[
G_z
=
\{g\in G:g\cdot z=z\}.
\]

由軌道—穩定子公式：

\[
|Gz|
=
\frac{|G|}{|G_z|}.
\]

## 3.2 一般偏軸點

若

\[
\operatorname{Re}z\ne0,
\qquad
\operatorname{Im}z\ne0,
\]

則

\[
G_z=\{e\}.
\]

軌道為

\[
Gz
=
\{
z,-z,\overline z,-\overline z
\},
\]

具有四個元素。

這是一般偏軸四元軌道。

## 3.3 非零虛軸點

若

\[
z=iy,
\qquad
y\ne0,
\]

則

\[
j(z)=z,
\]

而

\[
a(z)=b(z)=-z.
\]

因此

\[
G_z=\langle j\rangle,
\]

軌道為

\[
Gz=\{z,-z\}.
\]

這是 RH 所允許的主要軌道型。

## 3.4 非零實軸點

若

\[
z=x\in\mathbb R,
\qquad
x\ne0,
\]

則

\[
b(z)=z,
\]

而

\[
a(z)=j(z)=-z.
\]

因此

\[
G_z=\langle b\rangle,
\]

軌道為

\[
Gz=\{z,-z\}.
\]

此軌道不位於臨界線，故在一般判定框架中仍屬偏軸障礙。

## 3.5 原點

對

\[
z=0,
\]

有

\[
G_0=G.
\]

原點是全群固定點。

## 3.6 可實現軌道型

在 \(S\) 上可實現的穩定子型別為：

\[
[e],
\qquad
[\langle b\rangle],
\qquad
[\langle j\rangle],
\qquad
[G].
\]

由於 \(G\) 為阿貝爾群，共軛類等於子群本身。

\(\langle a\rangle\) 單獨作為穩定子不會出現，因為

\[
a(z)=z
\Longrightarrow
z=0,
\]

而原點同時被全群固定。

## 3.7 軌道型層

定義：

\[
S_{(H)}
=
\{z\in S:G_z=H\}.
\]

則

\[
S
=
S_{(e)}
\sqcup
S_{(\langle b\rangle)}
\sqcup
S_{(\langle j\rangle)}
\sqcup
S_{(G)}.
\]

其中：

\[
S_{(\langle j\rangle)}
=
i\mathbb R\setminus\{0\},
\]

\[
S_{(\langle b\rangle)}
=
\left(
\mathbb R\cap S
\right)\setminus\{0\},
\]

\[
S_{(G)}=\{0\}.
\]

而 \(S_{(e)}\) 為去除實軸與虛軸後的一般區域。

## 3.8 RH 的軌道型形式

令 \(D_F\) 為零點除子。

RH 等價於：

\[
\operatorname{supp}D_F
\subseteq
S_{(\langle j\rangle)}
\cup
S_{(G)}.
\]

若另使用 \(F(0)\ne0\)，則可進一步寫成：

\[
\operatorname{supp}D_F
\subseteq
S_{(\langle j\rangle)}.
\]

---

# 4. 局部有限有效除子空間

## 4.1 有效除子

\(S\) 上的局部有限有效除子為形式和：

\[
D
=
\sum_{\rho\in S}
m_\rho[\rho],
\qquad
m_\rho\in\mathbb N_0,
\]

並滿足：

> 對任意緊集 \(K\subset S\)，只有有限多個 \(\rho\in K\) 具有 \(m_\rho>0\)。

記其空間為：

\[
\operatorname{Div}_{\mathrm{lf}}^+(S).
\]

## 4.2 Radon 測度表示

將 \(D\) 視為正整數值 Radon 測度：

\[
\mu_D
=
\sum_\rho m_\rho\delta_\rho.
\]

以下不區分 \(D\) 與 \(\mu_D\)。

加法使

\[
\operatorname{Div}_{\mathrm{lf}}^+(S)
\]

成為交換么半群。

## 4.3 支撐於開帶的子空間

定義：

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)
=
\left\{
D\in\operatorname{Div}_{\mathrm{lf}}^+(S):
\operatorname{supp}D\subset X
\right\}.
\]

\(D_F\) 屬於此空間。

## 4.4 \(G\)-不變除子

定義：

\[
g_*D(B)=D(g^{-1}B).
\]

若

\[
g_*D=D
\qquad
\forall g\in G,
\]

則稱 \(D\) 為 \(G\)-不變。

記：

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G.
\]

### 命題 4.1

\(F\) 的零點除子 \(D_F\) 屬於

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G.
\]

### 證明要點

由

\[
F(-z)=F(z)
\]

與

\[
F(\overline z)=\overline{F(z)},
\]

若 \(\rho\) 為零點，則

\[
-\rho,
\quad
\overline\rho,
\quad
-\overline\rho
\]

亦為相同重數的零點。因此除子在 \(G\) 下不變。

---

# 5. 組態空間的 vague 拓樸

## 5.1 定義

令

\[
C_c(S)
\]

表示 \(S\) 上的緊支撐連續函數。

稱一列局部有限除子 \(D_n\) vague 收斂到 \(D\)，若對所有

\[
\varphi\in C_c(S),
\]

皆有

\[
\int_S\varphi\,dD_n
\longrightarrow
\int_S\varphi\,dD.
\]

記為：

\[
D_n\xrightarrow{v}D.
\]

## 5.2 直觀

vague 拓樸只觀察任意有限視窗中的零點組態。

它允許：

- 零點在有限區域內移動；
- 零點向無窮遠離開；
- 新零點從無窮遠進入；
- 多個零點在極限中合併並累積重數。

但在任一固定緊視窗中，局部有限性仍被保存。

## 5.3 \(G\)-不變子空間

因 \(G\) 為有限群且作用連續，

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G
\]

形成 \(G\)-不變組態空間的自然閉合子類。

## 5.4 軌道合併的典型極限

設

\[
z_n=x_n+iy,
\qquad
x_n\to0,
\qquad
x_n\ne0.
\]

一般軌道除子為：

\[
D_n
=
[z_n]+[-z_n]+[\overline z_n]+[-\overline z_n].
\]

當 \(x_n\to0\) 時：

\[
z_n,
\ -\overline z_n
\to iy,
\]

而

\[
-z_n,
\ \overline z_n
\to -iy.
\]

故 vague 極限為：

\[
D_n
\xrightarrow{v}
2[iy]+2[-iy].
\]

這表示一個四點平凡穩定子軌道可以在極限中退化為兩個具有雙重重數的 \(j\)-固定軌道點。

## 5.5 RH 與單根性必須分離

上述極限顯示：

- 軌道型可以改變；
- 重數可以增加；
- 偏軸軌道可以退化到臨界線。

RH 只要求位置位於 \(A\)，不要求零點單純。

因此本文不把「多重零點判別式」當作 RH 障礙。

目標組態空間必須允許：

\[
m_\rho>1
\qquad
\text{且 }\rho\in A.
\]

否則將 RH 與單根猜想非法合併。

---

# 6. 軸向收縮與冪等除子算子

## 6.1 收縮映射

定義：

\[
r:S\to A,
\qquad
r(z)=i\,\operatorname{Im}z.
\]

它滿足：

\[
r|_A=\operatorname{id}_A,
\]

\[
r\circ r=r.
\]

## 6.2 properness

### 命題 6.1

\(r:S\to A\) 為 proper 映射。

### 證明

令 \(K\subset A\) 為緊集。則存在有界閉區間 \(I\subset\mathbb R\)，使

\[
K\subseteq\{iy:y\in I\}.
\]

有：

\[
r^{-1}(K)
\subseteq
\left[-\frac12,\frac12\right]\times I.
\]

且 \(r^{-1}(K)\) 為閉集。因此它是 \(\mathbb R^2\) 中的閉有界集，故緊。證畢。

## 6.3 除子推前

因 \(r\) proper，可定義：

\[
\mathcal R:
\operatorname{Div}_{\mathrm{lf}}^+(S)
\to
\operatorname{Div}_{\mathrm{lf}}^+(S),
\]

\[
\mathcal R(D)=r_*D.
\]

其支撐位於 \(A\)。

## 6.4 連續性

### 命題 6.2

\(\mathcal R\) 對 vague 拓樸連續。

### 證明

若

\[
D_n\xrightarrow{v}D,
\]

對任意 \(\varphi\in C_c(A)\)，因 \(r\) proper，

\[
\varphi\circ r\in C_c(S).
\]

故

\[
\int_A\varphi\,d(r_*D_n)
=
\int_S\varphi\circ r\,dD_n
\to
\int_S\varphi\circ r\,dD
=
\int_A\varphi\,d(r_*D).
\]

證畢。

## 6.5 冪等性

由

\[
r^2=r,
\]

得到：

\[
\mathcal R^2=\mathcal R.
\]

故 \(\mathcal R\) 為連續冪等算子。

## 6.6 固定點刻畫

### 定理 6.3

對任意正局部有限除子 \(D\)，

\[
\mathcal R(D)=D
\iff
\operatorname{supp}D\subseteq A.
\]

### 證明

若 \(\operatorname{supp}D\subseteq A\)，則 \(r\) 在支撐上為恆等，故 \(\mathcal R(D)=D\)。

反之，\(\mathcal R(D)\) 的支撐包含於 \(A\)。若 \(\mathcal R(D)=D\)，則 \(D\) 的支撐亦包含於 \(A\)。正性阻止任何偏軸質量被負係數抵消。證畢。

### 推論 6.4

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
\]

## 6.7 算子的定位

\(\mathcal R\) 是診斷性投影：

- 它定義軸上除子子空間；
- 它建立固定點等價；
- 它不提供 \(D_F\) 為固定點的原因。

因此：

\[
\mathcal R(D_F)=D_F
\]

不能被當成已證定理，只能當成待達成的等價判定。

---

# 7. 有限視窗與軌道型值

## 7.1 \(G\)-不變有限視窗

令

\[
W\subset S
\]

為緊緻且 \(G\)-不變的 Borel 集。

因 \(D\) 局部有限，

\[
D(W)<\infty.
\]

因此 \(W\) 中只出現有限多個零點軌道。

## 7.2 軌道重數

若 \(D\) 為 \(G\)-不變，則同一軌道上各點重數相同。

對軌道 \(\mathcal O=G\rho\)，記共同重數為：

\[
m_{\mathcal O}.
\]

## 7.3 正 Burnside 半環

令

\[
A^+(G)
\]

表示有限 \(G\)-集合同構類所成的正 Burnside 半環。

其加法由不交聯集給出，乘法由笛卡兒積給出。

加法基底由傳遞 \(G\)-集合：

\[
[G/H]
\]

給出，其中 \(H\le G\)。

因此每個元素可寫為：

\[
\sum_{[H]}n_H[G/H],
\qquad
n_H\in\mathbb N_0.
\]

## 7.4 視窗軌道型值

定義：

\[
\tau_W(D)
=
\sum_{\mathcal O\subseteq\operatorname{supp}D\cap W}
m_{\mathcal O}[G/G_\rho]
\in A^+(G),
\]

其中 \(\rho\in\mathcal O\)。

由於 \(G\) 阿貝爾，選取同軌道代表不影響穩定子型別。

## 7.5 展開形式

在本文作用中，可寫為：

\[
\tau_W(D)
=
n_e(W)[G/e]
+
n_b(W)[G/\langle b\rangle]
+
n_j(W)[G/\langle j\rangle]
+
n_G(W)[G/G].
\]

各係數皆位於 \(\mathbb N_0\)。

其中：

- \(n_e\)：一般四點偏軸軌道重數；
- \(n_b\)：實軸偏軸軌道重數；
- \(n_j\)：虛軸軌道重數；
- \(n_G\)：原點重數。

---

# 8. 偏軸正障礙

## 8.1 軸上與偏軸生成元

一個軌道位於 \(A=\operatorname{Fix}(j)\) 當且僅當其穩定子包含 \(j\)。

在目前可實現型別中：

- \(\langle j\rangle\) 包含 \(j\)；
- \(G\) 包含 \(j\)；
- \(e\) 不包含 \(j\)；
- \(\langle b\rangle\) 不包含 \(j\)。

## 8.2 正投影

定義加法么半群同態：

\[
\pi_{\mathrm{off}}^+:
A^+(G)
\to
\mathbb N_0^2,
\]

使：

\[
\pi_{\mathrm{off}}^+([G/e])=(1,0),
\]

\[
\pi_{\mathrm{off}}^+([G/\langle b\rangle])=(0,1),
\]

\[
\pi_{\mathrm{off}}^+([G/\langle j\rangle])=(0,0),
\]

\[
\pi_{\mathrm{off}}^+([G/G])=(0,0).
\]

因此：

\[
\pi_{\mathrm{off}}^+\tau_W(D)
=
(n_e(W),n_b(W)).
\]

## 8.3 無抵消性

### 定理 8.1

\[
\pi_{\mathrm{off}}^+\tau_W(D)=0
\]

當且僅當 \(D\) 在 \(W\) 中沒有偏軸軌道。

### 證明

因係數皆為非負整數，

\[
(n_e,n_b)=(0,0)
\]

當且僅當兩類偏軸軌道係數均為零。不存在負係數可將其抵消。證畢。

## 8.4 為何不直接進入 Burnside 環

Burnside 環 \(A(G)\) 是 \(A^+(G)\) 的 Grothendieck 群化，允許形式差：

\[
[X]-[Y].
\]

群化適合研究穩定代數關係，但可能產生：

\[
\text{非零正障礙}
+
\text{負形式項}
=
0.
\]

此種代數消去不代表真實偏軸零點消失。

所以本文採取：

> **先在正半環中完成存在判定，再視需要進行群化。**

## 8.5 視窗 RH 條件

對 \(D_F\)：

\[
\pi_{\mathrm{off}}^+\tau_W(D_F)=0
\]

等價於 \(W\) 中沒有偏軸零點。

這是一個有限視窗判定，不是全域 RH。

---

# 9. 直接偏軸質量障礙

## 9.1 偏軸限制

定義：

\[
D^{\mathrm{off}}
=
D|_{S\setminus A}.
\]

它仍為正局部有限除子。

## 9.2 全域正障礙

定義：

\[
\mathfrak O(D)=D^{\mathrm{off}}.
\]

則：

\[
\mathfrak O(D)=0
\iff
\operatorname{supp}D\subseteq A.
\]

因此：

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak O(D_F)=0.
}
\]

## 9.3 與除子差障礙的區別

先前可定義形式差：

\[
\Theta(D)=D-\mathcal R(D).
\]

但 \(\Theta(D)\) 位於整係數除子群中，具有正負項。

本文認為更基礎的障礙應是：

\[
\mathfrak O(D)=D|_{S\setminus A},
\]

因為它保持正性，而且：

\[
\mathfrak O(D)=0
\]

直接表示偏軸支撐為空。

\(\Theta\) 可作比較差，但不應取代正障礙。

---

# 10. 高度過濾

## 10.1 緊高度視窗

對 \(T\ge0\)，定義：

\[
S_T
=
\left\{
z\in S:
|\operatorname{Im}z|\le T
\right\}.
\]

因 \(S\) 水平方向有界，\(S_T\) 為緊集。

## 10.2 截斷除子

定義：

\[
D_{\le T}=D|_{S_T}.
\]

其總質量有限。

## 10.3 偏軸質量輪廓

定義：

\[
\beta_D(T)
=
D(S_T\setminus A).
\]

則：

\[
\beta_D(T)\in\mathbb N_0.
\]

## 10.4 單調性

若

\[
T_1\le T_2,
\]

則

\[
S_{T_1}\subseteq S_{T_2},
\]

故：

\[
\beta_D(T_1)
\le
\beta_D(T_2).
\]

## 10.5 階梯結構

因 \(D\) 在每個 \(S_T\) 中只有有限支撐，\(\beta_D\) 只會在高度

\[
T=|\operatorname{Im}\rho|
\]

穿越偏軸零點時跳升。

因此它是一個非負整數值的單調階梯輪廓。

在不含邊界零點的區間內，它局部常值。

## 10.6 RH 的過濾形式

### 定理 10.1

\[
\boxed{
\mathrm{RH}
\iff
\beta_{D_F}(T)=0
\quad
\forall T\ge0.
}
\]

### 證明

若 RH 成立，偏軸限制為零，故所有高度質量為零。

反之，若存在偏軸零點 \(\rho\)，取

\[
T\ge|\operatorname{Im}\rho|,
\]

則

\[
\beta_{D_F}(T)\ge m_\rho>0.
\]

證畢。

## 10.7 有限驗證的真實地位

若數值或形式化方法證明：

\[
\beta_{D_F}(T_0)=0,
\]

只表示：

\[
|\operatorname{Im}\rho|\le T_0
\]

內無偏軸零點。

它不推出：

\[
\beta_{D_F}(T)=0
\qquad
\forall T>T_0.
\]

要完成全域 RH，仍需獨立尾部定理。

---

# 11. 軌道型高度輪廓

## 11.1 Burnside 值過濾

定義：

\[
\tau_T(D)
=
\tau_{S_T}(D)
\in A^+(G).
\]

展開：

\[
\tau_T(D)
=
n_e(T)[G/e]
+
n_b(T)[G/\langle b\rangle]
+
n_j(T)[G/\langle j\rangle]
+
n_G(T)[G/G].
\]

## 11.2 偏軸軌道輪廓

定義：

\[
\gamma_D(T)
=
\pi_{\mathrm{off}}^+\tau_T(D)
=
(n_e(T),n_b(T)).
\]

此輪廓比 \(\beta_D(T)\) 更精細，因為它區分：

- 一般四點偏軸軌道；
- 實軸二點偏軸軌道。

## 11.3 點質量與軌道質量

若需要按點重數計算，可定義：

\[
\beta_D(T)
=
4n_e(T)+2n_b(T),
\]

前提是 \(n_e,n_b\) 已按每個軌道的共同點重數加權。

軌道計數與點計數各有用途：

- 軌道計數描述對稱結構；
- 點計數對接辯值原理與零點總數。

---

# 12. 組態分解與軌道型閉包

## 12.1 軸上子空間

定義：

\[
\mathscr D_{\mathrm{axis}}
=
\left\{
D\in\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G:
\operatorname{supp}D\subseteq A
\right\}.
\]

由固定點定理：

\[
\mathscr D_{\mathrm{axis}}
=
\operatorname{Fix}(\mathcal R).
\]

## 12.2 混合子空間

定義：

\[
\mathscr D_{\mathrm{mixed}}
=
\left\{
D:
D|_A\ne0,
\ D|_{S\setminus A}\ne0
\right\}.
\]

## 12.3 純偏軸子空間

定義：

\[
\mathscr D_{\mathrm{off}}
=
\left\{
D:
D|_A=0,
\ D\ne0
\right\}.
\]

## 12.4 分解

除零除子外，可寫：

\[
\mathscr D^G
=
\mathscr D_{\mathrm{axis}}
\sqcup
\mathscr D_{\mathrm{mixed}}
\sqcup
\mathscr D_{\mathrm{off}}.
\]

## 12.5 軸上子空間的閉性

### 命題 12.1

在 vague 拓樸下，

\[
\mathscr D_{\mathrm{axis}}
\]

為閉集。

### 證明要點

因 \(A\) 為閉集，若 \(D_n\) 全部支撐於 \(A\) 且 \(D_n\xrightarrow v D\)，則對任意支撐於 \(S\setminus A\) 的非負測試函數 \(\varphi\)，有：

\[
\int\varphi\,dD_n=0.
\]

極限給出：

\[
\int\varphi\,dD=0.
\]

故 \(D\) 在 \(S\setminus A\) 無質量。

## 12.6 軸上子空間不是開集

一般偏軸四元軌道可向虛軸退化，因此任何軸上多重組態附近可能存在偏軸組態。

這說明：

- RH 組態空間是閉條件；
- 但未必具有對任意函數擾動的開穩定性；
- 單靠小擾動穩定不能證明 RH。

---

# 13. 解析函數空間到零點組態空間

## 13.1 對稱整函數類

定義：

\[
\mathcal E_G
=
\left\{
f\in\operatorname{Hol}(\mathbb C):
f(-z)=f(z),
f(\overline z)=\overline{f(z)}
\right\}.
\]

賦予 compact-open 拓樸，即在每個緊集上一致收斂。

## 13.2 零點除子映射

對非零 \(f\in\mathcal E_G\)，定義：

\[
\mathfrak Z(f)
=
D_f|_X.
\]

抽象地：

\[
\mathfrak Z:
\mathcal E_G\setminus\{0\}
\to
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G.
\]

## 13.3 局部穩定性

令 \(U\Subset X\) 為相對緊區域，且

\[
f(z)\ne0
\qquad
z\in\partial U.
\]

若 \(f_n\to f\) 在 \(\overline U\) 上一致，則由 Rouché 定理，對充分大的 \(n\)：

\[
D_{f_n}(U)=D_f(U)
\]

按重數計算。

這意味在零點自由邊界內，總零點數局部穩定。

## 13.4 更精細的組態收斂

在適當條件下，Hurwitz 定理與局部因子分解可將：

\[
f_n\to f
\]

轉化為零點除子在相對緊視窗中的 vague 收斂。

因此，解析函數空間與零點組態空間之間存在局部穩定接口。

## 13.5 限制

零點除子映射並非在所有情形下無條件全域連續：

- 零點可穿越視窗邊界；
- 零點可逃向無窮遠；
- 極限函數可能恆等於零；
- 多重零點會造成局部軌道型改變。

所以後續任何動力學或參數族研究，都必須附帶正則視窗與邊界控制。

---

# 14. 與繞數障礙的接口

## 14.1 正則區域

令 \(U\Subset X\setminus A\) 為有界區域，且：

\[
F(z)\ne0
\qquad
z\in\partial U.
\]

定義：

\[
\omega_U(F)
=
\frac{1}{2\pi i}
\oint_{\partial U}
\frac{F'(z)}{F(z)}\,dz.
\]

## 14.2 零點計數

由辯值原理：

\[
\omega_U(F)
=
D_F(U).
\]

因此繞數是正除子在區域 \(U\) 上的總質量。

## 14.3 與組態障礙的關係

若 \(U\subset S\setminus A\)，則：

\[
\omega_U(F)>0
\]

表示：

\[
\mathfrak O(D_F)(U)>0.
\]

故：

\[
\text{繞數證書}
\]

是偏軸正障礙的邊界表示。

## 14.4 分工

- 除子組態保存位置、重數與軌道型；
- Burnside 值保存對稱軌道類型；
- 繞數保存區域內的總正質量；
- 高度過濾保存障礙隨尺度的出現。

它們不是競爭表示，而是同一障礙的不同投影。

---

# 15. M6 不動點方法的精確移植

## 15.1 母域

M6 先建立：

\[
M6^*
\]

作為候選母域。

本文建立：

\[
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G
\]

作為零點組態母域。

## 15.2 目標子集

M6 中質數只是母域真子集。

本文中軸上組態：

\[
\mathscr D_{\mathrm{axis}}
\]

只是整個組態母域的真子集。

## 15.3 非循環算子

\(\mathcal R\) 的定義只使用：

- 閉臨界帶 \(S\)；
- 對合 \(j\)；
- 固定集 \(A\)；
- 軸向收縮 \(r\)。

它不使用「\(D\) 已滿足 RH」。

## 15.4 定位與證明的區分

\[
\operatorname{Fix}(\mathcal R)
=
\mathscr D_{\mathrm{axis}}
\]

完成的是唯一定位。

但要證明：

\[
D_F\in\operatorname{Fix}(\mathcal R),
\]

仍需額外數學內容。

因此本文沿用：

> **一肢定位，不冒充證明。**

---

# 16. TOPO 纖維檢查在組態空間中的版本

## 16.1 粗化映射

設：

\[
Q:
\operatorname{Div}_{\mathrm{lf}}^+(S;X)^G
\to
\mathcal T
\]

遺忘部分資料。

例如 \(Q\) 可能只保留：

- 總零點數；
- 軌道數；
- 高度分布；
- 某種拓樸同構類；
- 某種平均密度。

## 16.2 軸上判定

定義：

\[
P(D)
=
\begin{cases}
1,&D\in\mathscr D_{\mathrm{axis}},\\
0,&\text{否則}.
\end{cases}
\]

若存在：

\[
D_1,D_2
\]

使：

\[
Q(D_1)=Q(D_2),
\]

但：

\[
P(D_1)\ne P(D_2),
\]

則 \(Q\) 不足以判定 RH。

## 16.3 正障礙的資訊優勢

\[
\mathfrak O(D)=D|_{S\setminus A}
\]

對軸上判定是完備的，因為：

\[
P(D)=1
\iff
\mathfrak O(D)=0.
\]

但它幾乎保留全部偏軸除子，因此不是高度壓縮的判定量。

研究上的問題變成：

> 是否存在比完整偏軸除子更壓縮，但仍對 \(P\) 纖維常值的不變量？

Burnside 軌道型、高度輪廓與繞數族是三種候選壓縮。

---

# 17. 本文不使用的過強結論

## 17.1 不宣稱軌道型分層證明 RH

軌道型只分類可能性。

## 17.2 不宣稱閉性導致必然性

\(\mathscr D_{\mathrm{axis}}\) 為閉集，不表示 \(D_F\) 必須落入其中。

## 17.3 不宣稱收縮等於真實零點運動

\(r\) 是診斷映射，不是 \(\xi\) 零點的物理或解析演化。

## 17.4 不宣稱四點軌道退化必然發生

組態空間允許這種極限，不表示 \(F\) 的零點實際沿某個參數族如此移動。

## 17.5 不將多重零點視為 RH 失敗

RH 與零點單純性是不同命題。

## 17.6 不把有限高度零障礙提升為全域

缺少尾部控制時，只能得到有限視窗結果。

---

# 18. 後續可用的研究接口

## 18.1 層化接口

對開集 \(U\subset S\)，定義：

\[
\mathscr Z_{\mathrm{off}}(U)
=
\operatorname{Div}_{\mathrm{lf}}^+(U\setminus A).
\]

後續可研究其限制映射與零截面黏合。

## 18.2 軌道空間接口

定義：

\[
Y=S/G.
\]

\(G\)-不變除子可下降為 \(Y\) 上帶軌道型標記的正離散測度。

後續可在：

\[
Y_{\mathrm{off}}
\]

中局部化偏軸軌道。

## 18.3 測試函數接口

對：

\[
\varphi\in C_c(S\setminus A),
\qquad
\varphi\ge0,
\]

定義：

\[
\langle\mathfrak O(D),\varphi\rangle
=
\int\varphi\,dD.
\]

若 \(\mathfrak O(D)\ne0\)，則存在非負緊支撐連續函數 \(\varphi\) 使：

\[
\int\varphi\,dD>0.
\]

這是後續「拓樸分離」的最基本形式。

真正困難的是將 \(\varphi\) 提升為顯式公式允許的解析測試函數。

## 18.4 算術接口

最終需要某個映射：

\[
\mathfrak A:
\mathcal H_{\mathrm{adm}}
\to
\mathbb R,
\]

同時具有：

- 零點側表示；
- 質數側表示；
- 對偏軸正障礙的檢出能力；
- 可由算術側控制的符號。

本文不建立此映射，只為其提供組態輸入。

---

# 19. 形式化規格

## 19.1 基本型別

建議在 Lean 中建立：

```text
ClosedCriticalStrip
OpenCriticalStrip
KleinFourAction
CriticalInvolution
LocallyFiniteEffectiveDivisor
InvariantDivisor
OrbitType
PositiveOrbitSemiring
OffAxisObstruction
HeightRestriction
```

## 19.2 核心定理

需形式化：

1. \(j^2=\mathrm{id}\)；
2. \(\operatorname{Fix}(j)=A\)；
3. \(D_F\) 的 \(G\)-不變性；
4. \(r\) 的 properness；
5. \(\mathcal R\) 的良定義；
6. \(\mathcal R^2=\mathcal R\)；
7. 固定點與軸上支撐等價；
8. 軌道型分類；
9. 正障礙零值與偏軸軌道不存在等價；
10. 高度障礙單調性；
11. 全高度零障礙與 RH 等價。

## 19.3 不應形式化為公理的內容

下列內容不能直接作為未證公理混入主庫：

\[
\mathfrak O(D_F)=0,
\]

\[
\mathcal R(D_F)=D_F,
\]

\[
\beta_{D_F}(T)=0
\quad
\forall T.
\]

它們就是 RH 的等價形式。

若為測試需要暫時假設，必須隔離在明確標記的假設檔案。

---

# 20. 研究評價

## 20.1 本文真正新增的部分

相對於前置判定域論文，本文新增：

1. 以閉臨界帶修正軸向推前的 properness 問題；
2. 將零點除子空間建成 vague 拓樸組態空間；
3. 完整分類 Klein 四群下的可實現穩定子型別；
4. 將 RH 表為特定軌道型支撐條件；
5. 引入正 Burnside 半環避免障礙抵消；
6. 建立偏軸正投影；
7. 建立高度單調障礙輪廓；
8. 分離 RH 與零點單純性；
9. 建立解析函數空間到零點組態空間的局部穩定接口。

## 20.2 尚未新增的部分

本文沒有提供：

- 偏軸正障礙為零的解析原因；
- 質數側符號定理；
- 新的零點自由區；
- 全高度估計；
- RH 證明。

## 20.3 研究價值

本文的價值是將「零點在哪裡」轉成一個具備下列特性的母結構：

- 有拓樸；
- 有群作用；
- 有重數；
- 有正性；
- 有軌道型；
- 有有限視窗；
- 有高度過濾；
- 有解析擾動接口；
- 有形式化規格。

後續研究不必再以模糊的「零點鎖定」作為共同語言。

---

# 21. 結論

本文建立了黎曼猜想歸心後的等變零點組態拓樸。

基本資料為：

\[
S
=
\left\{
\left|\operatorname{Re}z\right|\le\frac12
\right\},
\]

\[
G
=
\langle z\mapsto-z,
\ z\mapsto\overline z\rangle
\cong C_2\times C_2,
\]

\[
j(z)=-\overline z,
\]

\[
A=\operatorname{Fix}(j)=i\mathbb R,
\]

\[
D_F=\operatorname{div}_0(F).
\]

RH 的固定點形式為：

\[
\boxed{
\mathrm{RH}
\iff
\mathcal R(D_F)=D_F.
}
\]

RH 的正障礙形式為：

\[
\boxed{
\mathrm{RH}
\iff
\mathfrak O(D_F)=0.
}
\]

RH 的高度過濾形式為：

\[
\boxed{
\mathrm{RH}
\iff
\beta_{D_F}(T)=0
\quad
\forall T\ge0.
}
\]

RH 的軌道型形式為：

\[
\boxed{
\mathrm{RH}
\iff
\pi_{\mathrm{off}}^+\tau_{S_T}(D_F)=0
\quad
\forall T\ge0.
}
\]

這些形式共同完成：

- 零點集合的等變組態化；
- 軸上與偏軸軌道的分層；
- 重數的保存；
- 正障礙的不可抵消化；
- 無限命題的高度過濾化。

但它們仍然只是合法判定框架。

真正尚待完成的核心仍是：

\[
\boxed{
\text{\(\xi\) 的獨立解析／算術結構}
\Longrightarrow
\mathfrak O(D_F)=0.
}
\]

下一階段應研究：

# 《層化零點障礙與局部—全域提升》

其任務是把本文的有限視窗正障礙、邊界繞數與局部除子資料組織為層與餘層式結構，並精確分析：

\[
\text{局部零障礙}
\;\dashrightarrow\;
\text{全域零障礙}
\]

所缺少的黏合條件、無窮遠控制與尾部定理。

---

# 附錄 A：主要符號

| 符號 | 意義 |
|---|---|
| \(S\) | 歸心後閉臨界帶 |
| \(X\) | 閉臨界帶內部 |
| \(G\) | Klein 四群 |
| \(a\) | 中心反演 \(z\mapsto-z\) |
| \(b\) | 共軛 \(z\mapsto\overline z\) |
| \(j\) | 臨界反射 \(z\mapsto-\overline z\) |
| \(A\) | \(j\) 的固定點集，即虛軸 |
| \(D_F\) | \(F\) 的非平凡零點除子 |
| \(\mathcal R\) | 軸向收縮的除子推前 |
| \(A^+(G)\) | 正 Burnside 半環 |
| \(\tau_W(D)\) | 視窗內軌道型值 |
| \(\pi_{\mathrm{off}}^+\) | 偏軸軌道正投影 |
| \(\mathfrak O(D)\) | 偏軸正除子 |
| \(S_T\) | 高度 \(T\) 的緊視窗 |
| \(\beta_D(T)\) | 偏軸點重數輪廓 |
| \(\gamma_D(T)\) | 偏軸軌道型輪廓 |
| \(\mathfrak Z\) | 解析函數到零點除子的映射 |

---

# 附錄 B：邏輯強度表

| 命題 | 性質 |
|---|---|
| \(D_F\) 為 \(G\)-不變 | 已知對稱的直接結果 |
| \(\operatorname{Fix}(j)=i\mathbb R\) | 直接計算 |
| \(\mathcal R^2=\mathcal R\) | 定義結果 |
| \(\mathcal R(D)=D\iff\operatorname{supp}D\subseteq A\) | 一般除子定理 |
| \(\mathfrak O(D)=0\iff\operatorname{supp}D\subseteq A\) | 一般正障礙定理 |
| \(\beta_D(T)\) 單調 | 集合包含的直接結果 |
| RH \(\iff\mathfrak O(D_F)=0\) | 等價重述 |
| RH \(\iff\beta_{D_F}\equiv0\) | 等價重述 |
| \(\mathfrak O(D_F)=0\) | 尚未證明；等價於 RH |
| 全部偏軸軌道不存在 | 尚未證明；等價於 RH |

---

# 附錄 C：後續接口

本文向下一篇輸出：

\[
\left(
S,
A,
G,
\mathscr D^G,
\mathfrak O,
\tau_T,
\beta_T,
\omega_U
\right).
\]

下一篇需要加入：

- 開集範疇；
- 除子層；
- 偏軸障礙層；
- 邊界繞數資料；
- 局部證書黏合；
- 無窮遠控制；
- 尾部提升條件。

---

# 附錄 D：版本邊界

v0.1 已完成：

- 閉臨界帶與 proper 軸向投影；
- vague 拓樸；
- 軌道型分類；
- 有效除子組態；
- 正 Burnside 半環；
- 偏軸正障礙；
- 高度輪廓；
- RH 與障礙消失的等價鏈；
- 形式化規格。

v0.1 尚未完成：

- Lean 4 實作；
- 組態空間的完整度量化；
- 軌道型分解的 Whitney 條件；
- 層與餘層形式化；
- 顯式公式測試函數；
- 算術符號定理；
- 任何 RH 證明。
