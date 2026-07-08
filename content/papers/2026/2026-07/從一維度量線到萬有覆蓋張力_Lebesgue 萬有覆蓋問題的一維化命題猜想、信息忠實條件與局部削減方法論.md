# 從一維度量線到萬有覆蓋張力  
## ——Lebesgue 萬有覆蓋問題的一維化命題猜想、信息忠實條件與局部削減方法論

**作者：Neo.K**  
**研究性質：命題猜想／局部方法論／內部研究草案**  
**版本：v0.1**  
**日期：2026-07-07**

---

## 摘要

本文提出一套針對 Lebesgue 萬有覆蓋問題的研究性重表述框架。其核心思想並非直接在二維平面中持續搜索更小的候選覆蓋體，而是先將所有滿足直徑限制的二維幾何對象轉譯為一維索引結構，再研究一維結構之間的等距嵌入、未覆蓋張力與面積收縮張力。

本文首先區分兩種不同的「一」：其一為原問題中的直徑約束
$$
\operatorname{diam}(K)\le 1,
$$
其二為研究方法中人工引入的總量歸一化
$$
\nu_K(K)=1.
$$
前者屬於幾何尺度條件，後者屬於比較坐標與積分正規化，二者不可混同。

對任意緊凸集合 $K\subset \mathbb R^2$ ，本文考慮一條一維索引線 $I=[0,1]$ 及滿射
$$
q_K:I\to K.
$$
若僅保存 $q_K$ 的順序而丟失點間關係，則一般會發生信息失真。為此本文引入一維索引上的距離核
$$
D_K(s,t)=\|q_K(s)-q_K(t)\|.
$$
再以
$$
s\sim_K t \iff D_K(s,t)=0
$$
建立商空間
$$
X_K=I/\!\sim_K,
$$
並定義
$$
d_K([s],[t])=D_K(s,t).
$$
由此得到一個與原集合 $K$ 等距的度量空間表示。本文因此提出「信息忠實一維化」的基本命題：二維幾何不必被壓縮成單一實函數，而可被轉譯為「一維索引＋關係核」。

在此基礎上，集合的合同包含可被重新表述為等距嵌入問題。若存在平面剛體運動 $g$ 使
$$
gK\subseteq U,
$$
則相應一維度量空間滿足
$$
X_K\hookrightarrow_{\mathrm{iso}}X_U.
$$
反之，在適當條件下，若存在保持全部點對距離的等距嵌入，則可由有限非退化基準點重建一個平面剛體運動。這使原問題可能從「二維形狀塞入另一二維形狀」轉化為「一維度量結構是否可等距嵌入另一一維索引度量結構」。

本文進一步定義兩類張力。第一類為點對距離張力：
$$
\tau_\phi(s,t)
=
d_U(\phi(s),\phi(t))-d_K(s,t),
$$
其中 $\phi:X_K\to X_U$ 為候選嵌入。零張力對應完全等距。第二類為未覆蓋距離張力：
$$
\delta_{K,U,g}(x)=\operatorname{dist}(gx,U).
$$
為統一點、線段與二維凸體，本文依集合仿射維度 $d_K\in\{0,1,2\}$ 定義歸一 Hausdorff 測度
$$
\nu_K
=
\frac{\mathcal H^{d_K}|_K}{\mathcal H^{d_K}(K)},
\qquad
\nu_K(K)=1.
$$
再定義
$$
N_p(K,U;g)
=
\left(
\int_K
\operatorname{dist}(gx,U)^p\,d\nu_K(x)
\right)^{1/p},
$$
以及
$$
N_p(K,U)
=
\inf_{g\in E(2)}N_p(K,U;g).
$$
對所有直徑不超過一的緊凸集合取最壞情況，得到萬有未覆蓋張力
$$
\mathfrak N_p(U)
=
\sup_{K\in\mathcal K_1}
N_p(K,U).
$$

本文提出核心命題猜想：在適當緊緻性與閉性條件下，
$$
\mathfrak N_p(U)=0
$$
應與 $U$ 為萬有覆蓋體等價。若此命題成立，則 Lebesgue 萬有覆蓋問題可被改寫為
$$
m^\star
=
\inf_U
\left\{
\mu_2(U):
\mathfrak N_p(U)=0
\right\}.
$$
此時問題的本質不再只是「找一個足夠大的覆蓋圖形」，而是「在所有不可避免的負覆蓋張力均被消除為零的可行邊界上，尋找最小面積狀態」。

最後，本文提出局部面積—張力比
$$
\rho
=
\frac{\Delta \mathfrak N_p}{-\Delta\mu_2},
$$
作為候選覆蓋體削減的局部方法論。若移除某區域能顯著減少面積而幾乎不增加萬有未覆蓋張力，則該區域可被視為低活性覆蓋區；反之，若極小削減立即造成張力上升，則該區域可能接近 active constraint。本文將此稱為「張力驅動削減」。

本文不宣稱已解決 Lebesgue 萬有覆蓋問題，也不宣稱所提出的一維化方式已經找到唯一最佳形式。本文的主要目的，是固定一組可繼續推導的研究語言，並清楚區分：信息忠實證明層、信息失真算法層、張力泛函層、局部削減層，以及未來待接入的群作用與李群方法。

**關鍵詞：** Lebesgue universal covering problem、一維化、度量核、等距嵌入、覆蓋張力、Hausdorff 測度、萬有負張力、局部削減、群作用、李群、 $E(2)$ 、 $SE(2)$

---

# 1. 研究動機

Lebesgue 萬有覆蓋問題可以被粗略理解為：尋找面積盡可能小的平面集合，使所有直徑不超過一的平面集合，都能經過某種剛體運動後被其包含。

若以集合族表示，可寫成
$$
\mathcal Y_1
=
\left\{
A\subset\mathbb R^2:
\operatorname{diam}(A)\le1
\right\}.
$$

希望尋找 $U\subset\mathbb R^2$ ，使
$$
\forall A\in\mathcal Y_1,
\quad
\exists g\in E(2),
\quad
gA\subseteq U,
$$
並最小化
$$
\mu_2(U).
$$

這一問題的困難不只來自候選覆蓋體 $U$ 的形狀未知，更來自目標集合族本身是無窮的。任意直徑不超過一的集合可能具有不同：

- 邊界；
- 方向；
- 曲率；
- 局部尖角；
- 長寬比例；
- 對稱性；
- 非對稱性；
- 拓撲；
- 尺度結構。

若直接在二維形狀空間中搜索，至少要同時處理
$$
\text{shape}
+
\text{rotation}
+
\text{translation}
+
\text{containment}.
$$

本文提出另一種思路：

> 先把二維幾何轉譯為一維索引結構，再把「是否能覆蓋」改寫為一維表示空間中的結構嵌入與張力消除問題。

這不是單純降維。

也不是普通投影。

其目的不是把二維圖形壓縮成一個數，而是尋找一個能在證明層保留幾何信息、在算法層提供計算優勢的中介表示。

---

# 2. 兩個不同的「一」

整套框架首先必須避免一個概念混淆。

## 2.1 原問題的直徑一

Lebesgue 萬有覆蓋問題的尺度約束為
$$
\operatorname{diam}(K)\le1.
$$

這個「一」屬於外在幾何尺度。

它限制任意兩點距離：
$$
\|x-y\|\le1,
\qquad
x,y\in K.
$$

## 2.2 方法中的總量一

本文另引入歸一測度：
$$
\nu_K(K)=1.
$$

這個「一」不表示直徑，也不表示面積一定為一。

它只表示：

> 把每一個幾何對象都視為一個完整總量單位，以便在共同的一維總量坐標上比較。

因此必須保留：
$$
\boxed{
\operatorname{diam}(K)\le1
}
$$
與
$$
\boxed{
\nu_K(K)=1
}
$$
兩個條件。

前者不能被後者取代。

---

# 3. 凸化與研究對象

本文先研究緊凸集合族：
$$
\mathcal K_1
=
\left\{
K\subset\mathbb R^2:
K\neq\varnothing,\;
K\text{ compact convex},\;
\operatorname{diam}(K)\le1
\right\}.
$$

其理由是對任意有界集合 $A$ ，有
$$
\operatorname{diam}(\operatorname{conv}A)
=
\operatorname{diam}(A).
$$

證明骨架如下。

令
$$
x=\sum_i\alpha_i a_i,
\qquad
y=\sum_j\beta_j b_j,
$$
其中
$$
a_i,b_j\in A,
\qquad
\alpha_i,\beta_j\ge0,
\qquad
\sum_i\alpha_i=\sum_j\beta_j=1.
$$

則
$$
x-y
=
\sum_{i,j}
\alpha_i\beta_j(a_i-b_j).
$$

由三角不等式：
$$
\|x-y\|
\le
\sum_{i,j}
\alpha_i\beta_j
\|a_i-b_j\|
\le
\operatorname{diam}(A).
$$

故
$$
\operatorname{diam}(\operatorname{conv}A)
\le
\operatorname{diam}(A).
$$

又因
$$
A\subseteq\operatorname{conv}A,
$$
所以反向不等式自然成立。

因此：
$$
\operatorname{diam}(\operatorname{conv}A)
=
\operatorname{diam}(A).
$$

這提供一個重要簡化：

> 若候選覆蓋體本身取凸集，則研究任意集合時，可以優先研究其凸包。

本文不主張所有後續方法只能處理凸集，但 v0.1 先把凸緊集作為證明層的主要對象。

---

# 4. 從二維集合到一維索引線

令
$$
I=[0,1].
$$

對每個
$$
K\in\mathcal K_1,
$$
考慮一個滿射：
$$
q_K:I\to K.
$$

此映射表示：

> 每個原始幾何點至少有一個一維索引位置。

因此
$$
q_K([0,1])=K.
$$

這裡的 $s\in[0,1]$ 只是索引。

它不必表示：

- 弧長；
- 歐氏坐標；
- 掃描時間；
- 邊界順序。

不同實作可選不同 $q_K$ 。

然而只保留
$$
q_K(s)
$$
本身仍有問題。

若 $q_K(s)\in\mathbb R^2$ 被完整保存，那麼二維坐標其實沒有消失。

若只保存順序而丟棄坐標，又可能嚴重失真。

因此真正關鍵不是「線」本身，而是：

$$
\boxed{
\text{線上各索引位置之間的關係}
}
$$

---

# 5. 一維距離核

定義：
$$
\boxed{
D_K(s,t)
=
\|q_K(s)-q_K(t)\|
}
$$

其中
$$
s,t\in[0,1].
$$

$D_K$ 是一個定義在一維索引對上的距離核。

它保存：

> 原始二維集合中，被 $s$ 與 $t$ 所代表之點的歐氏距離。

若不同索引對應同一幾何點，則：
$$
D_K(s,t)=0.
$$

因此定義等價關係：
$$
s\sim_K t
\iff
D_K(s,t)=0.
$$

再建立商空間：
$$
X_K
=
I/\!\sim_K.
$$

對等價類 $[s],[t]$ ，定義：
$$
d_K([s],[t])
=
D_K(s,t).
$$

此定義在自然條件下良定義，且
$$
(X_K,d_K)
$$
與原始
$$
(K,\|\cdot\|)
$$
等距。

因此本文提出：

## 命題 1：信息忠實一維化命題

對任意緊度量可參數化集合 $K$ ，若存在滿射
$$
q_K:[0,1]\to K,
$$
並保留完整距離核
$$
D_K(s,t)=\|q_K(s)-q_K(t)\|,
$$
則商空間
$$
([0,1]/\!\sim_K,d_K)
$$
與原集合 $K$ 在度量意義下等距。

此命題的意義不是宣稱二維拓撲等於一維拓撲，而是：

$$
\boxed{
\text{二維幾何可被轉譯為一維索引＋二點關係核}
}
$$

---

# 6. 強一維化與弱一維化

本文區分兩種不同層次。

## 6.1 強一維化

希望只靠：
$$
L_K(s)
$$
就保留足夠信息。

例如：
$$
K\to L_K:[0,1]\to\mathbb R^m.
$$

這種方法計算較輕，但一般更容易失真。

## 6.2 關係核一維化

保留：
$$
([0,1],D_K).
$$

此時幾何信息存於：
$$
D_K(s,t).
$$

雖然 $D_K$ 是二變數函數，但每個對象仍由一維索引空間組織。

本文將這種形式視為：

> 一維索引化的關係幾何。

它不一定降低所有計算複雜度，但提供一個可證明的信息忠實基礎。

---

# 7. 信息失真分級

後續所有證明與算法必須先判斷一維表示的忠實程度。

## Level 0：總量摘要

只保存：
$$
\nu_K(K)=1.
$$

幾乎沒有形狀區分能力。

## Level 1：單一歪線

保存：
$$
K_K(s).
$$

可能適合分類與排序，但一般不能證明包含。

## Level 2：多分量歪線

保存：
$$
\mathbf K_K(s).
$$

可加入：

- 容量；
- 拓撲；
- 方向；
- 多尺度。

仍可能失真。

## Level 3：方向族

保存：
$$
\mathbf K_K(s,\theta).
$$

信息更完整。

## Level 4：距離核

保存：
$$
D_K(s,t).
$$

在度量意義下可達完全忠實。

因此本文提出原則：

$$
\boxed{
\text{信息失真}
\Rightarrow
\text{不可直接構成完整證明}
}
$$

但：

$$
\boxed{
\text{信息失真}
\not\Rightarrow
\text{沒有算法價值}
}
$$

失真表示仍可用於：

- hard-case ranking；
- 搜索初始化；
- 方向預判；
- 局部加密；
- 候選削減；
- 經驗上界；
- 啟發式下界。

---

# 8. 覆蓋問題的反向提問

完成一維表示後，真正問題不再只是：

> 如何把二維形狀變成線？

而是：

> 一維表示 $X_K$ 如何重新成為原問題中的被覆蓋對象？

也就是研究：
$$
X_K
\to
X_U
$$
的嵌入條件。

若 $K$ 真能經剛體運動放入 $U$ ，則所有點對距離保持。

因此一維表示應存在等距嵌入。

---

# 9. 等距嵌入覆蓋命題

對：
$$
K,U\subset\mathbb R^2,
$$
令其信息忠實度量表示為：
$$
(X_K,d_K),
\qquad
(X_U,d_U).
$$

考慮映射：
$$
\phi:X_K\to X_U.
$$

若：
$$
d_U(\phi(s),\phi(t))
=
d_K(s,t)
$$
對所有
$$
s,t\in X_K
$$
成立，則 $\phi$ 為等距嵌入。

本文提出：

## 命題 2：合同包含—等距嵌入命題

在適當非退化條件下，
$$
\exists g\in E(2):
gK\subseteq U
$$
若且唯若
$$
X_K
\hookrightarrow_{\mathrm{iso}}
X_U.
$$

更簡寫：
$$
\boxed{
gK\subseteq U
\iff
X_K\hookrightarrow_{\mathrm{iso}}X_U
}
$$

---

# 10. 命題 2 的正向證明骨架

假設存在
$$
g\in E(2)
$$
使
$$
gK\subseteq U.
$$

由剛體運動保持距離：
$$
\|gx-gy\|
=
\|x-y\|.
$$

因此定義：
$$
F:K\to U,
\qquad
F(x)=gx.
$$

$F$ 為等距嵌入。

透過：
$$
K\cong X_K,
\qquad
U\cong X_U,
$$
自然得到：
$$
X_K\hookrightarrow_{\mathrm{iso}}X_U.
$$

---

# 11. 命題 2 的反向證明骨架

假設存在：
$$
F:K\to U
$$
滿足：
$$
\|F(x)-F(y)\|
=
\|x-y\|
$$
對所有 $x,y\in K$ 。

分三種情況。

## 11.1 二維非退化情況

若 $K$ 含三個非共線點：
$$
p_1,p_2,p_3,
$$
則
$$
F(p_1),F(p_2),F(p_3)
$$
形成與原三角形合同的三角形。

因此存在
$$
g\in E(2)
$$
使：
$$
g(p_i)=F(p_i),
\qquad i=1,2,3.
$$

任意 $x\in K$ ，因：
$$
\|F(x)-F(p_i)\|
=
\|x-p_i\|
=
\|gx-gp_i\|,
$$
而一個平面點到三個非共線基準點的距離在適當條件下唯一決定位置，因此：
$$
F(x)=gx.
$$

故：
$$
F=g|_K.
$$

## 11.2 線段型情況

若 $K$ 仿射維度為一，選兩個不同端點，距離保持決定線段上的位置，得到相應剛體運動限制。

## 11.3 單點情況

平移即可。

因此反向命題具有明確證明骨架。

本文仍將其標記為「命題候選」，因完整正式版本需明確處理：

- 退化集合；
- 反射；
- 參數化商空間；
- 空集合排除；
- 非凸集合版本。

---

# 12. 點對幾何張力

對任意候選嵌入：
$$
\phi:X_K\to X_U,
$$
定義：
$$
\boxed{
\tau_\phi(s,t)
=
d_U(\phi(s),\phi(t))
-
d_K(s,t)
}
$$

此量表示：

> 一維表示中的點對幾何關係，相對於原始距離要求的偏離。

## 12.1 正張力

若：
$$
\tau_\phi(s,t)>0,
$$
則映射後距離過大。

## 12.2 負張力

若：
$$
\tau_\phi(s,t)<0,
$$
則映射後距離過小。

## 12.3 零張力

若：
$$
\tau_\phi(s,t)=0,
$$
則該點對完全保持距離。

真正等距嵌入要求：
$$
\boxed{
\tau_\phi(s,t)=0
\quad
\forall s,t
}
$$

---

# 13. 正負張力不可直接抵消

定義：
$$
\tau_+(s,t)
=
[\tau_\phi(s,t)]_+,
$$
$$
\tau_-(s,t)
=
[-\tau_\phi(s,t)]_+.
$$

則：
$$
\tau_\phi
=
\tau_+
-
\tau_-.
$$

但若只積分：
$$
\int\tau_\phi,
$$
不同位置正負張力可能互相抵消。

因此真正幾何失真應保留：
$$
(\tau_+,\tau_-)
$$
或取絕對值。

例如：
$$
T_{\infty}(\phi)
=
\sup_{s,t}
|\tau_\phi(s,t)|.
$$

亦可定義：
$$
T_p(\phi)
=
\left(
\iint
|\tau_\phi(s,t)|^p
\,d\lambda(s)d\lambda(t)
\right)^{1/p}.
$$

但必須注意：

$$
T_p(\phi)=0
$$
才對應完整點對零張力。

---

# 14. 單一累積張力的限制

早期直覺可定義：
$$
\Theta(t)
=
\int_0^t
[u(s)-a(s)]\,ds.
$$

它具有重要算法意義，可表示：

- 累積供給；
- 累積需求；
- 局部正負餘量。

然而本文必須修正：

> 單純要求 $\Theta(t)\ge0$ 一般不能直接推出二維幾何包含。

因為不同位置的剩餘容量可能在積分中抵消，而實際幾何不允許任意搬運。

所以：

$$
\boxed{
\text{累積張力}
}
$$
應先被視為：

- 排序量；
- 預判量；
- hard-case 特徵；
- 低成本代理。

而不是無條件的精確證明量。

若要進入證明層，必須保留：

- 距離核；
- 位置關係；
- 可運輸條件；
- 群作用約束。

---

# 15. 未覆蓋距離張力

為直接對應集合包含，定義：
$$
\boxed{
\delta_{K,U}(x;g)
=
\operatorname{dist}(gx,U)
}
$$

其中：
$$
g\in E(2).
$$

因距離函數非負：
$$
\delta_{K,U}(x;g)\ge0.
$$

若：
$$
gx\in U,
$$
則：
$$
\delta=0.
$$

若：
$$
gx\notin U
$$
且 $U$ 閉，則：
$$
\delta>0.
$$

所以：
$$
\delta
$$
可以被理解為：

> 局部未覆蓋負張力。

---

# 16. 為何普通未覆蓋面積不足

若只定義：
$$
\mu_2(gK\setminus U),
$$
則存在嚴重問題。

例如 $K$ 是一條長度一的線段。

其二維面積：
$$
\mu_2(K)=0.
$$

即使整條線段完全未被 $U$ 包含，仍可能有：
$$
\mu_2(K\setminus U)=0.
$$

因此：

$$
\boxed{
\text{二維未覆蓋面積}
}
$$
不能統一處理：

- 點；
- 線；
- 二維形。

這正是本文引入「依自身維度歸一總量」的原因。

---

# 17. 仿射維度與歸一 Hausdorff 測度

令：
$$
d_K
=
\dim(\operatorname{aff}K)
\in\{0,1,2\}.
$$

對非單點集合，定義：
$$
\boxed{
\nu_K
=
\frac{
\mathcal H^{d_K}|_K
}{
\mathcal H^{d_K}(K)
}
}
$$

使：
$$
\nu_K(K)=1.
$$

對不同維度：

## 二維凸體
$$
d_K=2
$$
使用面積型 Hausdorff 測度。

## 線段
$$
d_K=1
$$
使用長度。

## 單點
$$
d_K=0
$$
可用單位 Dirac 質量或零維 Hausdorff 計數測度的歸一化。

因此所有目標形態都滿足：
$$
\boxed{
\nu_K(K)=1
}
$$

這個「一」正是本文的一維總量基準。

---

# 18. 總量未覆蓋張力

對
$$
1\le p<\infty,
$$
定義：
$$
\boxed{
N_p(K,U;g)
=
\left(
\int_K
\operatorname{dist}(gx,U)^p
\,d\nu_K(x)
\right)^{1/p}
}
$$

再對所有剛體配置取最小：
$$
\boxed{
N_p(K,U)
=
\inf_{g\in E(2)}
N_p(K,U;g)
}
$$

其意義為：

> 目標形態 $K$ 在所有允許剛體運動下，仍不可消除的最小總量距離張力。

若：
$$
N_p(K,U)=0,
$$
直覺上表示存在配置能把全部總量張力消除。

---

# 19. 零積分與精確包含

本文提出：

## 命題 3：零總量距離張力命題

令 $K$ 為非空緊凸集， $U$ 為閉集， $\nu_K$ 在 $K$ 的相對拓撲上具有完整支撐。則對固定 $g\in E(2)$ ：
$$
N_p(K,U;g)=0
$$
若且唯若：
$$
gK\subseteq U.
$$

### 正向

若：
$$
gK\subseteq U,
$$
則：
$$
\operatorname{dist}(gx,U)=0
$$
對所有 $x\in K$ 。

所以：
$$
N_p=0.
$$

### 反向

假設：
$$
N_p=0.
$$

若存在：
$$
x_0\in K
$$
使：
$$
\operatorname{dist}(gx_0,U)>0,
$$
由距離函數連續性，存在 $x_0$ 的相對鄰域 $V\subset K$ 與 $\varepsilon>0$ ，使：
$$
\operatorname{dist}(gx,U)\ge\varepsilon
$$
對所有 $x\in V$ 。

若：
$$
\nu_K(V)>0,
$$
則：
$$
\int_K
\operatorname{dist}(gx,U)^p\,d\nu_K(x)
\ge
\varepsilon^p\nu_K(V)
>0,
$$
矛盾。

所以：
$$
\operatorname{dist}(gx,U)=0
$$
對所有 $x\in K$ 。

$U$ 閉，因此：
$$
gK\subseteq U.
$$

此命題是本文張力框架最重要的證明接口之一。

---

# 20. 萬有未覆蓋張力

定義：
$$
\boxed{
\mathfrak N_p(U)
=
\sup_{K\in\mathcal K_1}
\inf_{g\in E(2)}
\left(
\int_K
\operatorname{dist}(gx,U)^p
\,d\nu_K(x)
\right)^{1/p}
}
$$

簡寫：
$$
\mathfrak N_p(U)
=
\sup_{K\in\mathcal K_1}
N_p(K,U).
$$

其意義：

> 在所有直徑不超過一的緊凸形態中，取最難被 $U$ 覆蓋者；但每個形態先允許自己選最佳剛體配置。

這是一個典型：
$$
\sup_K\inf_g
$$
的 minimax 結構。

---

# 21. 核心命題猜想

本文提出：

## 猜想 A：萬有零張力等價猜想

對適當類別的緊候選集合 $U$ 與
$$
1\le p<\infty,
$$
有：
$$
\boxed{
\mathfrak N_p(U)=0
\iff
U
\text{ 為 }\mathcal K_1\text{ 的萬有覆蓋體}
}
$$

---

# 22. 猜想 A 的正向方向

若 $U$ 是 universal cover，則：

$$
\forall K\in\mathcal K_1,
\quad
\exists g_K\in E(2),
\quad
g_KK\subseteq U.
$$

由命題 3：
$$
N_p(K,U;g_K)=0.
$$

所以：
$$
N_p(K,U)=0.
$$

進而：
$$
\mathfrak N_p(U)=0.
$$

此方向基本直接。

---

# 23. 猜想 A 的反向方向

假設：
$$
\mathfrak N_p(U)=0.
$$

則對每個固定：
$$
K\in\mathcal K_1,
$$
有：
$$
N_p(K,U)=0.
$$

也就是存在序列：
$$
g_n\in E(2)
$$
使：
$$
N_p(K,U;g_n)\to0.
$$

若能證明：

1. 旋轉／反射部分可取收斂子序列；
2. 平移參數不逃向無窮；
3. $g_n\to g$ 後 $N_p(K,U;g_n)\to N_p(K,U;g)$ ；
4. 因而 $N_p(K,U;g)=0$ ；

則由命題 3：
$$
gK\subseteq U.
$$

因此 $U$ universal。

---

# 24. 平移不逃逸的證明直覺

假設 $U$ 緊。

若：
$$
N_p(K,U;g_n)\to0,
$$
代表大部分總量在距離意義下逼近 $U$ 。

選某些：
$$
x_n\in K
$$
使：
$$
\operatorname{dist}(g_nx_n,U)
$$
足夠小。

因：
$$
\operatorname{diam}(K)\le1,
$$
對所有 $y\in K$ ：
$$
\|g_ny-g_nx_n\|
=
\|y-x_n\|
\le1.
$$

若 $g_nx_n$ 落在 $U$ 的固定鄰域，則整個：
$$
g_nK
$$
落在該鄰域再加一單位半徑內。

因此平移參數受界。

旋轉／反射部分屬於：
$$
O(2),
$$
為緊群。

所以可以期待 $g_n$ 有收斂子序列。

此處尚需正式化，但證明路線清楚。

---

# 25. Lebesgue 問題的張力改寫

若猜想 A 成立，則原最小覆蓋問題可寫為：
$$
\boxed{
m^\star
=
\inf_U
\left\{
\mu_2(U):
\mathfrak N_p(U)=0
\right\}
}
$$

這是本文最核心的重表述。

其哲學意義是：

> 最小萬有覆蓋不是單純找「最小又足夠大的圖形」，而是在所有不可消除的未覆蓋負張力均為零的可行邊界上，尋找最小面積狀態。

---

# 26. 覆蓋面積與不覆蓋張力

本文將原始直覺：

> 覆蓋面積等於不覆蓋面積的張力差

重新嚴格化。

若只使用指示函數差：
$$
\chi_U-\chi_{gK},
$$
並直接積分，得到：
$$
\mu(U)-\mu(K).
$$

此量會把不同位置正負差異互相抵消，不能保留足夠幾何信息。

因此真正應分離：

- 面積收縮壓力；
- 未覆蓋負張力。

定義：

$$
A(U)=\mu_2(U)
$$

與：

$$
\mathfrak N_p(U).
$$

目標變成：

$$
A(U)\downarrow
$$
同時要求：
$$
\mathfrak N_p(U)=0.
$$

---

# 27. 雙張力觀點

本文提出：

## 面積收縮張力

候選覆蓋體越大：
$$
\mu_2(U)\uparrow.
$$

最優化要求：
$$
\mu_2(U)\downarrow.
$$

## 萬有未覆蓋張力

候選覆蓋體越小，通常越容易：
$$
\mathfrak N_p(U)\uparrow.
$$

因此存在兩股相反壓力：

$$
\boxed{
\text{Area Contraction Tension}
\leftrightarrow
\text{Universal Negative Coverage Tension}
}
$$

最優解位於：
$$
\mathfrak N_p(U)=0
$$
的可行邊界。

---

# 28. 懲罰泛函

算法層可定義：
$$
\boxed{
J_{\lambda,p}(U)
=
\mu_2(U)
+
\lambda
\mathfrak N_p(U)^p
}
$$

其中：
$$
\lambda>0.
$$

第一項要求面積縮小。

第二項懲罰未覆蓋張力。

計算目標：
$$
U_{\lambda,p}
\in
\arg\min_U
J_{\lambda,p}(U).
$$

當：
$$
\lambda\uparrow,
$$
理論上期望解逐步逼近：
$$
\mathfrak N_p(U)=0
$$
的邊界。

但本文必須明確指出：

> penalty method 是算法方法，不自動構成原問題證明。

若要證明：
$$
U_{\lambda,p}\to U^\star,
$$
仍需研究：

- 存在性；
- 緊緻性；
- 下半連續；
- $\Gamma$-收斂或其他變分收斂；
- 候選類別閉性。

---

# 29. 從二維張力回到一維線

若存在：
$$
q_K:[0,1]\to K
$$
及一維概率測度：
$$
\lambda_K
$$
使：
$$
(q_K)_\#\lambda_K
=
\nu_K,
$$
則：

$$
\int_K
\operatorname{dist}(gx,U)^p
\,d\nu_K(x)
=
\int_0^1
\operatorname{dist}(gq_K(s),U)^p
\,d\lambda_K(s).
$$

定義一維局部未覆蓋張力：
$$
\boxed{
\delta_{K,U,g}(s)
=
\operatorname{dist}(gq_K(s),U)
}
$$

則：
$$
N_p(K,U)
=
\inf_g
\left(
\int_0^1
\delta_{K,U,g}(s)^p
\,d\lambda_K(s)
\right)^{1/p}.
$$

因此整套張力框架可以真正寫在一維總量線上。

---

# 30. 一維總量線的意義

在此框架中：

$$
s\in[0,1]
$$
不必表示幾何距離。

它可以表示：

$$
\text{normalized total-mass index}.
$$

所有形態：

- 圓；
- 三角形；
- 線段；
- 常寬體；

均可有：
$$
\lambda_K([0,1])=1.
$$

因此：

$$
\boxed{
\text{不同維度形態}
\to
\text{同一總量一維域}
}
$$

再由：
$$
q_K
$$
與
$$
D_K
$$
保留其幾何。

---

# 31. 三層張力體系

本文提出三個不同層級。

## 第一層：局部未覆蓋張力

$$
\delta(s)
=
\operatorname{dist}(gq_K(s),U).
$$

用途：

- 定位失敗區；
- 局部加密；
- 可視化。

## 第二層：總量張力

$$
N_p
=
\left(
\int
\delta(s)^p\,d\lambda
\right)^{1/p}.
$$

用途：

- 排序 hard cases；
- 全局優化；
- 證明候選。

## 第三層：點對幾何張力

$$
\tau(s,t)
=
d_U(\phi(s),\phi(t))
-
d_K(s,t).
$$

用途：

- 信息忠實嵌入；
- 幾何失真判斷；
- 精確等距條件。

三者不應混為一談。

---

# 32. $p$ 的意義

不同：
$$
p
$$
對不同失敗形態敏感。

## $p=1$

$$
N_1
=
\int\delta.
$$

偏向平均未覆蓋距離。

## $p=2$

$$
N_2
=
\left(
\int\delta^2
\right)^{1/2}.
$$

對大偏差更敏感。

## $p\to\infty$

形式上趨近：
$$
N_\infty
=
\sup_x\operatorname{dist}(gx,U).
$$

這接近先前的包含歪度。

因此本文的新框架並不是丟棄舊方法，而是把舊：
$$
K_{\mathrm{inc}}
$$
視為 $L^\infty$ 端點。

---

# 33. 為何前次單一標量容易退化

若只保留：
$$
N_\infty(K,U)
$$
或：
$$
K_{\mathrm{inc}}(K,U),
$$
所有形態最後只剩一個數。

可能出現：
$$
0.0074,\quad
0.0075,\quad
0.0076
$$
等高度壓縮。

但新方法保留：
$$
\delta_{K,U,g}(s)
$$
整條線。

甚至保留：
$$
\tau_\phi(s,t).
$$

因此不同 hard cases 即使最大殘差相近，其：

- 失敗位置；
- 失敗寬度；
- 多峰結構；
- 點對失真；

仍可不同。

---

# 34. 局部面積—張力比

設 $U$ 為候選覆蓋體。

考慮向內削減得到：
$$
U_\varepsilon\subset U.
$$

面積減少：
$$
\Delta A
=
\mu_2(U)-\mu_2(U_\varepsilon)
>0.
$$

萬有張力增加：
$$
\Delta N
=
\mathfrak N_p(U_\varepsilon)
-
\mathfrak N_p(U).
$$

定義：
$$
\boxed{
\rho_p(U\to U_\varepsilon)
=
\frac{
\Delta N
}{
\Delta A
}
}
$$

這是本文局部方法論的核心量。

---

# 35. $\rho_p$ 的解讀

## 低張力削減

若：
$$
\rho_p\approx0,
$$
表示：

> 能移除明顯面積，但幾乎不增加萬有未覆蓋張力。

此區域可能：

- 尚未被 hard case 使用；
- 僅屬冗餘覆蓋；
- 可優先削除。

## 高張力削減

若：
$$
\rho_p\gg1,
$$
表示：

> 極少面積削減就造成明顯張力上升。

此區域可能：

- 接近 active constraint；
- 被某些極端形態緊密使用；
- 是候選最優邊界的重要部分。

---

# 36. 張力驅動削減算法

給定初始已知或高概率可行候選：
$$
U_0.
$$

對一族 admissible inward perturbations：
$$
\{V_\alpha\},
$$
產生：
$$
U_{\varepsilon,\alpha}.
$$

計算：
$$
\rho_p(\alpha)
=
\frac{
\mathfrak N_p(U_{\varepsilon,\alpha})
-
\mathfrak N_p(U)
}{
\mu_2(U)-\mu_2(U_{\varepsilon,\alpha})
}.
$$

選：
$$
\alpha^\star
=
\arg\min_\alpha
\rho_p(\alpha).
$$

更新：
$$
U_{n+1}
=
U_{n,\varepsilon,\alpha^\star}.
$$

重複直到：

- 所有可削方向張力顯著升高；
- 達到數值容忍；
- 或證書條件失敗。

---

# 37. active tension 概念

若 $U^\star$ 真為最小 universal cover，直覺上不應存在一個合法向內變形 $V$ ，使：

$$
\left.
\frac{d}{d\varepsilon}
\mu_2(U_\varepsilon)
\right|_{\varepsilon=0}
<0
$$

同時：

$$
\mathfrak N_p(U_\varepsilon)=0
$$
對所有足夠小 $\varepsilon>0$ 仍成立。

因此最優邊界應被某些極端形態「壓住」。

本文稱：

$$
\boxed{
\text{active coverage tension}
}
$$

即存在：
$$
K^\star
$$
與最佳配置：
$$
g^\star
$$
使該形態對局部邊界擾動高度敏感。

---

# 38. 猜想 B：張力飽和猜想

若 $U^\star$ 為局部最小 universal cover，則對每個允許面積下降的一階向內變形方向 $V$ ，應存在至少一個 hard case $K_V$ ，使：

$$
\left.
\frac{d^+}{d\varepsilon}
N_p(K_V,U^\star_\varepsilon)
\right|_{\varepsilon=0}
>0
$$

或在一階退化時，某個高階導數為正。

直觀意義：

> 每一個真正可減少面積的方向，都應被至少一個 active hard case 阻止。

此猜想類似優化中的 active constraints / KKT 直覺，但本文不宣稱現階段已建立可直接套用的凸優化結構。

---

# 39. 猜想 C：有限活性支撐猜想

在適當正則性與非退化條件下，一個局部最優候選 $U^\star$ 的邊界可能由有限或低複雜度 hard-case family 決定。

形式上可能存在：
$$
K_1,\dots,K_m
$$
及配置：
$$
g_1,\dots,g_m
$$
使局部最優性條件主要由這些 active constraints 生成。

若成立，則無窮形態族問題可能在局部最優附近降為有限活性集合。

本文目前僅提出猜想。

---

# 40. 局部張力密度

若候選 $U$ 有足夠光滑邊界，可考慮邊界點：
$$
y\in\partial U.
$$

對每個 hard case 最佳配置 $g_K$ ，研究其與邊界接觸或近接觸程度。

可定義研究性局部活性密度：
$$
a_U(y)
=
\sup_{K\in\mathcal K_1}
\mathcal A(K,g_K,y),
$$
其中 $\mathcal A$ 衡量：

- 接觸；
- 距離殘差；
- 形狀敏感度；
- 變分導數。

若：
$$
a_U(y)\approx0,
$$
該邊界可能低活性。

若：
$$
a_U(y)\gg0,
$$
可能為高張力區。

這提供從全局 $\mathfrak N_p(U)$ 到局部邊界削減的接口。

---

# 41. 累積張力仍有算法價值

雖然：
$$
\Theta(t)\ge0
$$
不能無條件當作精確包含證明，但仍可定義：

$$
\Theta_{K,U,g}(t)
=
\int_0^t
\omega(s)
\delta_{K,U,g}(s)
\,d\lambda_K(s)
$$

或正負供需型版本。

用途包括：

- 比較未覆蓋張力集中在前段或後段；
- 找局部突變；
- 預測最危險區間；
- 自適應增加樣本；
- 提供低成本篩選。

因此本文不丟棄累積張力，而將其降級為：

$$
\boxed{
\text{算法層代理量}
}
$$

---

# 42. 局部歪度與張力的結合

一維化後可同時保存：

$$
K_{\mathrm{shape}}(s)
$$
與：
$$
\delta_{K,U,g}(s).
$$

形成：
$$
\boxed{
\mathbf Z(s)
=
\left(
K_{\mathrm{shape}}(s),
\delta(s)
\right)
}
$$

若再加入累積量：
$$
\Theta(s),
$$
則：
$$
\mathbf Z(s)
=
\left(
K_{\mathrm{shape}},
\delta,
\Theta
\right).
$$

這可以研究：

> 哪種形狀歪度最容易對應未覆蓋張力峰值？

若存在穩定關係，可形成 hard-case predictor。

---

# 43. 信息忠實層與算法代理層分離

本文強烈主張將兩層分開。

## 證明層

使用：

- 距離核；
- 等距嵌入；
- 完整支撐測度；
- 距離函數；
- 緊緻性；
- 精確 $E(2)$ 作用。

## 算法層

使用：

- 單一歪線；
- Fourier 係數；
- 累積張力；
- 有限方向；
- 離散樣本；
- 代理 hard-case score。

這樣即使算法表示失真，也不會錯誤宣稱證明。

---

# 44. 有限樣本近似

對：
$$
K
$$
取樣：
$$
x_1,\dots,x_N.
$$

近似：
$$
N_p^N(K,U;g)
=
\left(
\sum_{i=1}^N
w_i
\operatorname{dist}(gx_i,U)^p
\right)^{1/p},
$$
其中：
$$
w_i\ge0,
\qquad
\sum_iw_i=1.
$$

再離散剛體運動：
$$
g_j.
$$

得到：
$$
\widetilde N_p(K,U)
=
\min_j
N_p^N(K,U;g_j).
$$

對有限測試族：
$$
K_1,\dots,K_M,
$$
定義：
$$
\widetilde{\mathfrak N}_p(U)
=
\max_i
\widetilde N_p(K_i,U).
$$

此量可直接計算。

但它只對：

- 有限形態族；
- 有限點樣本；
- 有限剛體網格；

有效。

必須額外建立誤差證書，才能接近證明。

---

# 45. 四層誤差證書

可延續既有分解思想：

$$
E_{\mathrm{total}}
=
E_{\mathrm{shape}}
+
E_{\mathrm{group}}
+
E_{\mathrm{sample}}
+
E_{\mathrm{numeric}}.
$$

其中：

## 形態誤差
$$
E_{\mathrm{shape}}
$$
控制無窮目標族到有限 net 的差。

## 群搜尋誤差
$$
E_{\mathrm{group}}
$$
控制 $E(2)$ 或 $SE(2)$ 的離散化。

## 點樣本誤差
$$
E_{\mathrm{sample}}
$$
控制積分與有限點。

## 數值誤差
$$
E_{\mathrm{numeric}}
$$
控制浮點與幾何計算。

此框架尚需後續正式化。

---

# 46. 一維距離核的離散化

對索引：
$$
s_1,\dots,s_N,
$$
保存矩陣：
$$
D_{ij}
=
D_K(s_i,s_j).
$$

此時目標形態成為：
$$
N\times N
$$
距離矩陣。

候選嵌入 $\phi$ 變成索引匹配。

點對張力：
$$
\tau_{ij}
=
D_U(\phi(i),\phi(j))
-
D_K(i,j).
$$

這形成離散 metric embedding problem。

優點：

- 信息比單一歪線完整；
- 可利用矩陣算法；
- 可測等距偏差。

缺點：

- 儲存成本 $O(N^2)$ ；
- 匹配問題可能昂貴。

因此未來需要低秩、稀疏或局部關係壓縮。

---

# 47. 信息不失真與計算複雜度的張力

這是本文方法不可逃避的核心矛盾。

若完整保存：
$$
D_K(s,t),
$$
信息忠實，但計算可能昂貴。

若只保存：
$$
K(s),
$$
計算較快，但可能失真。

因此又出現一個新的張力：

$$
\boxed{
\text{Information Fidelity}
\leftrightarrow
\text{Computational Compression}
}
$$

未來應研究最小充分表示：
$$
\mathfrak U^\star_{\mathcal T}.
$$

即對特定任務 $\mathcal T$ 保留足夠信息，但不要保存全部。

對本文：
$$
\mathcal T
=
\text{rigid universal coverage}.
$$

---

# 48. 猜想 D：任務充分核猜想

可能存在比完整：
$$
D_K(s,t)
$$
更小的關係集合：
$$
\mathcal R_K
\subset
[0,1]^2
$$
使只保存：
$$
D_K|_{\mathcal R_K}
$$
就足以判斷與 $U$ 的剛體包含。

例如對某些凸體，有限或低維極端點關係可能足夠決定剛體配置。

此猜想若成立，將大幅降低一維忠實表示成本。

---

# 49. 與支撐函數的接口

對凸體 $K$ ，支撐函數：
$$
h_K(u)
=
\sup_{x\in K}
\langle x,u\rangle.
$$

本文並不丟棄支撐函數。

相反地，可將其視為：

- 外部極值包絡；
- 一維方向函數。

而：
$$
D_K(s,t)
$$
描述內部點對關係。

因此可能建立：
$$
\boxed{
\mathcal S_K
=
\left(
h_K(\theta),
D_K(s,t)
\right)
}
$$

其中：

- $h_K$ ：高效凸包含接口；
- $D_K$ ：信息忠實幾何接口。

未來可能用支撐函數做快速篩選，用距離核做精確驗證。

---

# 50. 與常寬體的接口

對常寬一體：
$$
h_K(\theta)+h_K(\theta+\pi)=1.
$$

這是一個極強方向約束。

若同時保存：
$$
D_K(s,t),
$$
則可能研究常寬條件如何限制一維距離核可實現空間。

這可能把：

$$
\text{constant-width shape family}
$$
轉成：
$$
\text{constrained metric-kernel family}.
$$

此部分為後續重要方向。

---

# 51. 群作用接口

原問題中：
$$
g\in E(2).
$$

本文暫不展開完整群論，但必須預留：

$$
g\cdot K.
$$

在一維表示上，希望存在作用：
$$
T_g:X_K\to X_{gK}.
$$

理想協變條件：
$$
\mathfrak U(gK)
=
T_g\mathfrak U(K).
$$

若：
$$
T_{g_1g_2}
=
T_{g_1}\circ T_{g_2},
$$
則一維表示與群作用相容。

這是未來群論化的基本接口。

---

# 52. 為何李群可能重要

平面定向保持剛體運動可由：

- 二維平移；
- 一維旋轉；

組成連續三維變換族。

其連續部分自然對應：
$$
SE(2).
$$

因此內層：
$$
\inf_{g\in E(2)}
$$
可以分為：

- $SE(2)$ 連續分支；
- 反射相關離散分支。

這意味著未來可研究：

- 群軌道；
- 李代數局部坐標；
- 指數映射；
- 群上梯度；
- 臨界點；
- 不變量；
- 軌道空間。

但本文 v0.1 不提前把這些寫入主證明。

---

# 53. 群論的可能核心問題

未來可問：

$$
\boxed{
\text{能否把最優覆蓋搜索視為 }E(2)\text{ 軌道上的張力最小化？}
}
$$

對固定 $K,U$ ，定義：
$$
F_{K,U}(g)
=
N_p(K,U;g).
$$

則：
$$
N_p(K,U)
=
\inf_{g\in E(2)}
F_{K,U}(g).
$$

若 $F$ 有足夠正則性，可研究：

- 群上梯度流；
- 臨界軌道；
- 對稱性降低；
- 穩定子群；
- 極端配置。

此方向後續再展開。

---

# 54. 對稱性降低

若 $K$ 或 $U$ 有對稱群：
$$
G_K,
\qquad
G_U,
$$
則某些 $g$ 搜索是重複的。

可考慮雙陪集結構：
$$
G_U\backslash E(2)/G_K.
$$

這可能顯著降低配置搜索空間。

本文僅記錄此接口，不在本版推導。

---

# 55. 局部方法論總結

本文局部方法論可濃縮為：

## Step 1
選一個候選 $U$ 。

## Step 2
對有限 hard-case family 計算：
$$
N_p(K_i,U).
$$

## Step 3
定位各形態最佳配置與局部殘差：
$$
\delta_i(s).
$$

## Step 4
對候選邊界生成向內擾動：
$$
U_{\varepsilon,\alpha}.
$$

## Step 5
計算：
$$
\rho_p(\alpha)
=
\frac{
\Delta\mathfrak N_p
}{
\Delta A
}.
$$

## Step 6
優先選低 $\rho_p$ 方向削減。

## Step 7
當某些 hard cases 張力快速升高時，將其加入 active set。

## Step 8
提高局部形態、群參數與邊界取樣解析度。

---

# 56. 研究性偽代碼

```text
Input:
    initial candidate U0
    shape family F
    p >= 1
    perturbation family P

repeat:
    for each K in F:
        find approximate best rigid placement g_K
        compute N_p(K, U; g_K)
        store local residual profile delta_K

    estimate universal tension:
        N_univ = max_K N_p(K, U)

    for each inward perturbation alpha in P:
        build U_alpha
        estimate:
            DeltaA(alpha)
            DeltaN(alpha)
        rho(alpha) = DeltaN(alpha) / DeltaA(alpha)

    choose alpha* with minimal rho(alpha)

    if no safe or low-tension perturbation exists:
        refine hard-case family
        refine group search
        refine sampling
    else:
        U <- U_alpha*

until certificate / stopping condition
```

---

# 57. 本方法與純「削角」的差異

傳統直覺可能是：

> 看起來這個角落沒用，所以切掉。

本文改成：

> 若削除某區域帶來顯著面積收益，而對最壞形態造成的不可消除張力增加極低，則其為低活性區。

因此削減順序由：
$$
\rho_p
$$
驅動。

理想情況下：

$$
\boxed{
\text{視覺削角}
\to
\text{張力導向變分削減}
}
$$

---

# 58. 可能的局部證書

對有限測試族 $\mathcal F$ ，若對某候選削減區 $R$ 能證明：

$$
\forall K\in\mathcal F,
\quad
\exists g_K,
\quad
g_KK\subseteq U\setminus R,
$$
則該削減對有限族安全。

更高級版本可使用：

$$
N_p(K,U\setminus R)=0
$$
作有限族證書。

再加形態 net 誤差：
$$
E_{\mathrm{shape}}
$$
嘗試擴張到無窮族。

---

# 59. 証明層的三條路

本文目前看到三條可能證明路線。

## 路線 A：距離核等距嵌入

$$
X_K\hookrightarrow_{\mathrm{iso}}X_U.
$$

優點：信息忠實。

缺點：計算昂貴。

## 路線 B：零總量距離張力

$$
N_p(K,U)=0.
$$

優點：可積分、可算法化、可能精確。

缺點：仍需處理 $\inf_g$ 的達成與萬有族。

## 路線 C：凸幾何支撐函數

$$
h_{gK}(u)\le h_U(u).
$$

優點：凸體包含條件直接。

缺點：前次單一標量化容易失去 hard-case 區分力。

最可能的成熟版本不是三選一，而是混合。

---

# 60. 混合證明架構猜想

本文提出：

## 猜想 E：三層混合架構

一個有效的 Lebesgue universal covering 計算—證明系統可能需要：

### 外層
支撐函數／凸幾何約束：
$$
h_K.
$$

### 中層
一維總量張力：
$$
N_p.
$$

### 內層
信息忠實距離核：
$$
D_K.
$$

即：
$$
\boxed{
\text{support}
+
\text{tension}
+
\text{metric kernel}
}
$$

分別負責：

- 快速必要條件；
- hard-case 優化；
- 最終忠實驗證。

---

# 61. 失真版本的價值

即使無法建立完全忠實：
$$
D_K,
$$
仍可用低維歪線：
$$
K_K(s).
$$

例如對每個形態產生特徵：
$$
\Phi(K)
=
\left(
\|K\|_{L^1},
\|K\|_{L^2},
\|K\|_{L^\infty},
\widehat K_1,\dots,\widehat K_m
\right).
$$

再預測：
$$
N_p(K,U).
$$

如果相關性高，則可快速搜尋 hard cases。

這屬於算法價值，不屬於完整證明。

---

# 62. 注意力衰減與研究文件化

本文本身亦採取一種研究方法論立場：

> 在長鏈條理論推導中，應把已形成的局部概念及時固定為可編輯文檔，以降低注意力衰減、上下文漂移與概念遺失。

因此本文 v0.1 的目的不是宣稱理論完成，而是把以下已成形內容固定：

1. 兩個「一」；
2. 一維索引；
3. 距離核；
4. 等距嵌入；
5. 未覆蓋距離張力；
6. 歸一 Hausdorff 測度；
7. 萬有未覆蓋張力；
8. 局部面積—張力比；
9. 群作用接口。

後續可以從任一節點繼續展開。

---

# 63. 主要未決問題

## 問題 1
是否存在自然、穩定且計算可行的：
$$
q_K:[0,1]\to K?
$$

## 問題 2
不同 $q_K$ 是否導致等價的距離核表示？

## 問題 3
能否找到比完整 $D_K$ 更小的任務充分核？

## 問題 4
猜想 A 的反向緊緻性證明如何完整化？

## 問題 5
$$
\mathfrak N_p(U)
$$
對 $U$ 的 Hausdorff 擾動是否 Lipschitz 或下半連續？

## 問題 6
最優解對不同 $p$ 是否一致？

## 問題 7
$$
p\to\infty
$$
是否穩定回到包含歪度？

## 問題 8
局部 $\rho_p$ 是否存在形狀導數？

## 問題 9
active hard cases 是否有限化？

## 問題 10
$SE(2)$ 李群結構如何降低內層：
$$
\inf_g
$$
成本？

---

# 64. 後續最自然推導順序

本文建議下一階段依序：

## 第一階段
正式證明命題 3。

## 第二階段
完整化猜想 A 的反向緊緻性。

## 第三階段
研究：
$$
\mathfrak N_p
$$
對 $U$ 的穩定性。

## 第四階段
做有限凸體數值實驗。

## 第五階段
測：
$$
\rho_p
$$
是否能預測安全削減方向。

## 第六階段
再引入：
$$
SE(2)
$$
群作用與李代數局部優化。

這樣可避免過早把群論變成裝飾性語言。

---

# 65. 一句話版本

> 將所有直徑不超過一的目標形態，以總量為一的一維索引表示；若需證明則保留完整距離核，使合同包含轉化為等距嵌入；再以歸一總量上的距離積分定義未覆蓋張力，將最小萬有覆蓋改寫為「在萬有負張力為零的可行邊界上最小化面積」。

---

# 66. 核心公式總表

目標族：
$$
\mathcal K_1
=
\{
K:
K\text{ compact convex},
\operatorname{diam}(K)\le1
\}.
$$

一維索引：
$$
q_K:[0,1]\to K.
$$

距離核：
$$
D_K(s,t)
=
\|q_K(s)-q_K(t)\|.
$$

商空間：
$$
X_K=[0,1]/\!\sim_K.
$$

合同包含：
$$
gK\subseteq U
\iff
X_K\hookrightarrow_{\mathrm{iso}}X_U.
$$

點對張力：
$$
\tau_\phi(s,t)
=
d_U(\phi(s),\phi(t))-d_K(s,t).
$$

歸一測度：
$$
\nu_K
=
\frac{
\mathcal H^{d_K}|_K
}{
\mathcal H^{d_K}(K)
}.
$$

局部未覆蓋張力：
$$
\delta_{K,U,g}(x)
=
\operatorname{dist}(gx,U).
$$

總量張力：
$$
N_p(K,U;g)
=
\left(
\int_K
\delta_{K,U,g}(x)^p
d\nu_K(x)
\right)^{1/p}.
$$

最佳配置：
$$
N_p(K,U)
=
\inf_g
N_p(K,U;g).
$$

萬有張力：
$$
\mathfrak N_p(U)
=
\sup_{K\in\mathcal K_1}
N_p(K,U).
$$

最小覆蓋重表述：
$$
m^\star
=
\inf_U
\{
\mu_2(U):
\mathfrak N_p(U)=0
\}.
$$

懲罰泛函：
$$
J_{\lambda,p}(U)
=
\mu_2(U)
+
\lambda\mathfrak N_p(U)^p.
$$

局部面積—張力比：
$$
\rho_p
=
\frac{
\Delta\mathfrak N_p
}{
-\Delta\mu_2
}.
$$

---

# 67. 結論

本文提出一個針對 Lebesgue 萬有覆蓋問題的新研究框架。

其第一步不是直接改良候選覆蓋體，而是改變問題表示。

對任意：
$$
K\subset\mathbb R^2,
$$
建立一維索引：
$$
[0,1].
$$

若只做普通線化，信息可能丟失。

因此證明層引入：
$$
D_K(s,t)
=
\|q_K(s)-q_K(t)\|.
$$

由此把二維幾何轉譯為：
$$
\boxed{
\text{一維索引＋距離核}
}
$$

並使合同包含問題有機會轉化為：
$$
\boxed{
\text{等距嵌入問題}
}
$$

接著，本文引入依自身仿射維度歸一的 Hausdorff 測度：
$$
\nu_K(K)=1.
$$

由此統一：

- 點；
- 線；
- 面。

再定義未覆蓋距離張力：
$$
\delta(x)=\operatorname{dist}(gx,U),
$$
及總量張力：
$$
N_p.
$$

最終得到：
$$
\mathfrak N_p(U)
=
\sup_K\inf_g N_p(K,U;g).
$$

本文提出核心猜想：
$$
\boxed{
\mathfrak N_p(U)=0
\iff
U\text{ universal}
}
$$

若成立，則 Lebesgue 萬有覆蓋問題可被改寫為：
$$
\boxed{
m^\star
=
\inf_U
\{
\mu_2(U):
\mathfrak N_p(U)=0
\}
}
$$

這使問題本質變為：

> 在所有不可避免的負覆蓋張力都被消除為零的邊界上，尋找最小面積狀態。

進一步，對局部削減：
$$
U\to U_\varepsilon,
$$
定義：
$$
\rho_p
=
\frac{
\Delta\mathfrak N_p
}{
-\Delta\mu_2
}.
$$

這提供一個新的局部方法：

> 優先削除每單位面積所造成萬有張力增量最小的區域。

因此，本文整體可濃縮為：

$$
\boxed{
\text{2D shape}
\to
\text{1D indexed metric structure}
\to
\text{isometric embedding}
\to
\text{coverage tension}
\to
\text{minimum-area zero-tension boundary}
}
$$

最後，本文保留一個重要方向。

原問題中的剛體變換不是任意參數集合，而具有群結構。其連續定向保持部分與：
$$
SE(2)
$$
密切相關。

因此未來很可能需要進一步研究：

$$
\boxed{
\text{一維度量表示}
\times
\text{群作用}
\times
\text{張力泛函}
}
$$

但本文暫不提前展開。

本版的任務是先把命題、猜想與局部方法論固定。

後續研究可從此繼續。

---

# 附錄 A：命題與猜想清單

## 命題 1
完整距離核可形成信息忠實一維度量表示。

## 命題 2
合同包含與一維度量空間等距嵌入具有等價性候選。

## 命題 3
在完整支撐與閉集條件下：
$$
N_p(K,U;g)=0
\iff
gK\subseteq U.
$$

## 猜想 A
$$
\mathfrak N_p(U)=0
\iff
U\text{ universal}.
$$

## 猜想 B
局部最優 universal cover 的每個向內面積下降方向，皆受 active hard case 阻止。

## 猜想 C
局部最優邊界可能由有限或低複雜度 active hard-case family 支撐。

## 猜想 D
存在比完整距離核更小的任務充分核。

## 猜想 E
成熟方法可能採用：
$$
\text{support}
+
\text{tension}
+
\text{metric kernel}
$$
三層混合架構。

---

# 附錄 B：研究邊界聲明

本文目前不宣稱：

1. 已解決 Lebesgue 萬有覆蓋問題；
2. 已證明猜想 A；
3. 已證明最優解存在；
4. 已證明 $J_{\lambda,p}$ penalty limit 收斂到原問題；
5. 已證明 active hard cases 有限；
6. 已證明一維低維歪線足以保持全部信息；
7. 已完成 $SE(2)$ 李群化；
8. 已找到最佳 $p$ ；
9. 已找到最佳一維參數化 $q_K$ ；
10. 已建立可投稿級完整定理體系。

本文的定位是：

$$
\boxed{
\text{命題猜想}
+
\text{局部方法論}
+
\text{後續證明接口}
}
$$

而不是完成解答。

---

# 附錄 C：最短研究備忘

若後續重新進入本題，可從以下五句恢復：

1. 不要把二維集合只壓成單一標量。
2. 證明層用一維索引加距離核 $D_K(s,t)$ 。
3. 覆蓋可改看等距嵌入。
4. 未覆蓋用歸一總量上的距離張力 $N_p$ 。
5. 最小面積問題改寫成 $\mathfrak N_p(U)=0$ 邊界上的面積最小化。

