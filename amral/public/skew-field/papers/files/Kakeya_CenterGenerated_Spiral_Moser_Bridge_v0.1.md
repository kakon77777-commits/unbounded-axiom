# 從原始掛谷針到 Moser 蟲  
## 中心生成式雙向偏移螺旋的正厚度橋接理論

**副標題：** 不可重疊正交掃掠、面積不變量與普適容納泛函  
**版本：** v0.1  
**日期：** 2026 年 7 月 27 日  
**性質：** 命題型幾何論文／研究綱領  
**狀態：** 部分定理可直接證明；橋接極值與漸近命題仍待研究

---

## 摘要

原始掛谷針問題、中心生成式雙向偏移螺旋與 Moser 蟲問題，表面上分別研究針的旋轉、螺旋帶的生成以及單位曲線的普適容納；三者實際共享同一個深層結構：一維幾何物件的方向變化，如何轉化成具有二維面積的承載區域。

本文提出「正厚度中心生成掛谷—Moser橋接理論」。其核心方法是把掛谷針的外部旋轉相位內化為中心曲線的切向相位，並令一條長度為 \(2\rho\) 的針始終沿中心曲線的法向移動。所得到的掃掠集合恰為中心曲線的雙向法向帶。若法向參數化在內部保持單射，且 \(\rho\|\kappa\|_\infty<1\)，則掃掠面積滿足精確不變式

\[
\mu_2(S_\rho(\gamma))=2\rho L.
\]

若加入兩端半圓帽，完整管狀鄰域面積為

\[
\mu_2(T_\rho(\gamma))=2\rho L+\pi\rho^2.
\]

因此，原始掛谷問題藉由大量重疊而把掃掠面積壓向零的退化通道，在「正厚度＋不可內部重疊」條件下被封閉；但單一掃掠面積也因此失去形狀依賴。真正仍有非平凡極值結構的問題，轉化為：尋找最小面積容器，以剛體運動容納全部中心生成式正厚度掃掠。這正是一個 Moser 型普適容納問題。

本文形式化三者的差異與接口，證明正交掛谷掃掠等同於雙向偏移帶、推導面積不變量與支撐函數平移律，並提出新的「中心生成掛谷—Moser橋接泛函」、零厚度漸近問題、接觸飽和螺旋命題與曲率集中研究綱領。

**關鍵詞：** 掛谷針問題、Moser 蟲問題、中心生成螺旋、管狀鄰域、正厚度、不可重疊、支撐函數、普適覆蓋、曲率、幾何測度

---

# 1. 問題背景與必要區分

## 1.1 原始掛谷針問題

令單位針為線段

\[
I=[-1/2,1/2]\times\{0\}.
\]

原始掛谷問題研究：是否存在一個面積盡可能小的平面區域，使同一根針能在其中連續運動並將方向翻轉 \(180^\circ\)。

一個針的配置可寫成

\[
q(t)=(a(t),\phi(t))
\in SE(2),
\]

其中 \(a(t)\in\mathbb R^2\) 是針中心，\(\phi(t)\) 是旋轉相位。時刻 \(t\) 的針為

\[
I_t=a(t)+R_{\phi(t)}I,
\]

其掃掠集合是

\[
K[q]
=
\bigcup_{t\in[0,1]}I_t.
\]

原始動態問題要求

\[
\phi(1)-\phi(0)=\pi
\]

並研究

\[
\inf_q\mu_2(K[q]).
\]

必須區分兩個相關但不同的敘述：

1. **動態掛谷針問題：** 同一根針能否沿連續路徑完成翻轉；
2. **靜態 Besicovitch 集合：** 一個集合是否包含每個方向的一根單位線段。

兩者在歷史上密切相關，但「含有全部方向」不會自動提供同一根針的連續配置路徑。

---

## 1.2 Moser 蟲問題

令

\[
\mathcal C_1
=
\left\{
\gamma:
\operatorname{Len}(\gamma)=1
\right\}
\]

為全部長度一的平面可求長曲線族。

Moser 蟲問題要求尋找最小面積區域 \(C\)，使任意 \(\gamma\in\mathcal C_1\) 都能經平移與旋轉後放入 \(C\)：

\[
\forall\gamma\in\mathcal C_1,
\qquad
\exists g\in SE(2),
\qquad
g\gamma\subseteq C.
\]

其泛函為

\[
M^\ast
=
\inf_C
\left\{
\mu_2(C):
\forall\gamma\in\mathcal C_1,\,
\exists g\in SE(2),\,
g\gamma\subseteq C
\right\}.
\]

原始掛谷研究的是「同一物件的連續運動路徑」；Moser 研究的是「全部物件的各自最佳靜態放置」。二者不能直接視為同一問題。

---

## 1.3 中心生成式雙向偏移螺旋

令中心生成線為弧長參數曲線

\[
\gamma:[0,L]\to\mathbb R^2,
\qquad
\|\gamma'(s)\|=1.
\]

設

\[
T(s)=\gamma'(s)
\]

為單位切向量，

\[
N(s)
\]

為單位法向量，並以切向相位 \(\theta(s)\) 表示

\[
T(s)
=
(\cos\theta(s),\sin\theta(s)).
\]

曲率為

\[
\kappa(s)=\theta'(s).
\]

中心生成條件至少包括：

\[
\gamma(0)=0,
\]

以及徑向不倒退條件

\[
\frac{d}{ds}\|\gamma(s)\|
\geq0
\]

在可微處成立。

若再要求

\[
\theta'(s)\geq0,
\]

則曲線的方向沿弧長單調轉動，形成中心向外的轉向生成。

---

# 2. 外部旋轉相位與內部切向相位

原始掛谷問題中的方向變化由外部配置角

\[
\phi(t)
\]

描述。

中心生成曲線中的方向變化則由內部切向角

\[
\theta(s)
\]

描述。

二者的基本轉譯為

\[
\boxed{
\phi(t)
\longleftrightarrow
\theta(s)+\frac{\pi}{2}
}.
\]

原因是本文令掛谷針沿中心線法向放置。對每個 \(s\)，定義長度 \(2\rho\) 的法向針

\[
I_s
=
\left\{
\gamma(s)+tN(s):
-\rho\leq t\leq\rho
\right\}.
\]

針的方向是 \(N(s)\)，其方向角即為

\[
\theta(s)+\frac{\pi}{2}.
\]

因此：

- 掛谷的外部針方向，成為曲線的法向方向；
- 掛谷的時間參數，成為曲線的弧長參數；
- 針中心路徑，成為中心生成線 \(\gamma\)。

---

# 3. 正交掛谷運動

## 定義 3.1：正交掛谷運動

一條長度 \(2\rho\) 的針運動

\[
q(s)=(a(s),\phi(s))
\]

稱為正交掛谷運動，若滿足

\[
\|a'(s)\|=1
\]

以及

\[
a'(s)\cdot
(\cos\phi(s),\sin\phi(s))
=
0.
\]

也就是：針中心的速度始終垂直於針本身。

若令

\[
a(s)=\gamma(s),
\qquad
\phi(s)=\theta(s)+\frac{\pi}{2},
\]

則上述條件自動成立。

---

## 命題 3.2：正交運動—中心曲線對應

每一條 \(C^1\) 弧長參數中心曲線 \(\gamma\)，都自然生成一條正交掛谷運動：

\[
q_\gamma(s)
=
\left(
\gamma(s),
\theta(s)+\frac{\pi}{2}
\right).
\]

反之，任意滿足正交條件的正則針中心路徑，都可在選定方向後視為某條中心曲線的法向針運動。

### 證明

由

\[
\gamma'(s)=T(s)
\]

以及

\[
N(s)\perp T(s),
\]

可得

\[
\gamma'(s)\cdot N(s)=0.
\]

而針的方向向量正是 \(N(s)\)，故針中心速度垂直於針。反向構造則由正交的單位速度與針方向恢復一組切向—法向標架。證畢。

---

# 4. 掃掠集合與雙向偏移帶

## 定義 4.1：雙向法向帶

定義

\[
F_\rho(s,t)
=
\gamma(s)+tN(s),
\qquad
(s,t)\in[0,L]\times[-\rho,\rho].
\]

其像集

\[
S_\rho(\gamma)
=
F_\rho
\left(
[0,L]\times[-\rho,\rho]
\right)
\]

稱為中心曲線的雙向法向帶。

---

## 定理 4.2：掛谷掃掠—偏移帶恆等式

由中心曲線 \(\gamma\) 生成的正交掛谷運動，其掃掠集合恰為

\[
\boxed{
\bigcup_{s\in[0,L]}I_s
=
S_\rho(\gamma)
}.
\]

### 證明

對固定 \(s\)，針的位置為

\[
I_s
=
\left\{
\gamma(s)+tN(s):
-\rho\leq t\leq\rho
\right\}.
\]

對全部 \(s\) 取聯集，即為 \(F_\rho\) 在整個參數矩形上的像。證畢。

---

# 5. 方向完備性

平面中的無向線段方向以

\[
\mathbb R/\pi\mathbb Z
\]

表示；有向方向則以

\[
\mathbb R/2\pi\mathbb Z
\]

表示。

## 命題 5.1：方向完備條件

若 \(\theta\) 連續且

\[
\theta(L)-\theta(0)\geq\pi,
\]

則法向針 \(I_s\) 至少經歷全部無向方向。

若

\[
\theta(L)-\theta(0)\geq2\pi,
\]

則法向針至少完成一次全部有向方向。

### 證明

法向角為

\[
\phi(s)=\theta(s)+\frac{\pi}{2}.
\]

由連續函數的介值性質，\(\phi\) 的像包含長度至少為 \(\pi\) 或 \(2\pi\) 的完整角度區間。分別模去 \(\pi\) 或 \(2\pi\) 即得。證畢。

---

# 6. 不可重疊與正面積

## 定義 6.1：內部不可重疊

要求

\[
F_\rho:
[0,L]\times(-\rho,\rho)
\to\mathbb R^2
\]

為單射。

邊界可以發生交接，但不同參數點不可對應到同一內部面積點。

一個標準充分條件是

\[
\operatorname{reach}(\gamma)\geq\rho.
\]

局部正則性則由

\[
\rho\|\kappa\|_\infty<1
\]

保證。

---

## 定理 6.2：不可重疊正交掃掠的面積不變量

設 \(\gamma\) 為長度 \(L\) 的 \(C^2\) 弧長參數曲線，並假設：

1. \(F_\rho\) 在內部單射；
2. \(\rho\|\kappa\|_\infty<1\)。

則

\[
\boxed{
\mu_2(S_\rho(\gamma))
=
2\rho L
}.
\]

### 證明

由 Frenet 公式

\[
N'(s)=-\kappa(s)T(s),
\]

可得

\[
\frac{\partial F_\rho}{\partial s}
=
T(s)+tN'(s)
=
\left(
1-t\kappa(s)
\right)T(s),
\]

以及

\[
\frac{\partial F_\rho}{\partial t}
=
N(s).
\]

Jacobian 為

\[
J_F(s,t)
=
\left|
\det
\left(
(1-t\kappa)T,N
\right)
\right|
=
|1-t\kappa(s)|.
\]

由

\[
\rho\|\kappa\|_\infty<1
\]

可知在整個參數域內

\[
1-t\kappa(s)>0.
\]

因此

\[
\begin{aligned}
\mu_2(S_\rho(\gamma))
&=
\int_0^L
\int_{-\rho}^{\rho}
\left(
1-t\kappa(s)
\right)
\,dt\,ds\\
&=
\int_0^L
\left[
2\rho
-
\kappa(s)
\int_{-\rho}^{\rho}t\,dt
\right]ds\\
&=
\int_0^L2\rho\,ds\\
&=
2\rho L.
\end{aligned}
\]

證畢。

---

## 推論 6.3：完整管狀鄰域

若 \(\gamma\) 為開曲線，並在兩端加入半徑 \(\rho\) 的兩個半圓帽，則

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B
\]

滿足

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L+\pi\rho^2
}.
\]

若 \(\gamma\) 為簡單閉曲線且管狀鄰域不自交，則沒有端帽項：

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L.
}
\]

---

# 7. 掛谷退化通道的封閉

原始掛谷問題允許不同時間的針位置高度重疊，因此可以反覆使用同一片區域承載大量方向狀態。

本文加入：

\[
\rho>0
\]

以及

\[
F_\rho
\text{ 在內部單射}.
\]

於是不同時間截面不能共享正面積內部。

由定理 6.2：

\[
\mu_2(S_\rho(\gamma))
=
2\rho L>0.
\]

因此：

\[
\boxed{
\text{正厚度與不可重疊條件封閉了掛谷的零面積退化通道。}
}
\]

但同時出現一個更深的結果：

\[
\boxed{
\text{單次掃掠面積不再依賴中心線形狀。}
}
\]

只要長度、厚度與不可重疊條件相同，圓弧、螺旋、折線平滑化或一般曲率分布，都具有同樣的法向帶面積 \(2\rho L\)。

所以最佳化問題必須轉移。

---

# 8. 從掛谷轉向 Moser 的主交接

原始掛谷問：

> 同一根針的一次方向完備運動，最少需要掃過多少面積？

在本文限制下，答案被面積不變量固定為

\[
2\rho L.
\]

非平凡問題因此變成：

> 哪一個最小面積區域，能經不同剛體放置，容納所有符合條件的方向完備正交掃掠？

這正是 Moser 型問題。

---

# 9. 中心生成掛谷—Moser橋接族

## 定義 9.1：中心生成曲線族

令

\[
\Gamma_{\mathrm{CG}}
(L,\rho,\tau)
\]

為所有滿足下列條件的曲線 \(\gamma\)：

1. \(\gamma:[0,L]\to\mathbb R^2\) 為 \(C^2\) 弧長參數曲線；
2. \(\gamma(0)=0\)；
3. 徑向不倒退：
   \[
   \frac{d}{ds}\|\gamma(s)\|\geq0;
   \]
4. 切向相位單調：
   \[
   \theta'(s)\geq0;
   \]
5. 總轉向：
   \[
   \theta(L)-\theta(0)\geq\tau;
   \]
6. 管狀正則：
   \[
   \rho\|\kappa\|_\infty<1;
   \]
7. 內部不可重疊：
   \[
   \operatorname{reach}(\gamma)\geq\rho.
   \]

當

\[
\tau=\pi
\]

時，法向針完成全部無向方向。

當

\[
\tau=2\pi
\]

時，法向針完成全部有向方向。

---

## 定義 9.2：橋接普適容納泛函

定義

\[
\mathfrak B(L,\rho,\tau)
=
\inf_C
\left\{
\mu_2(C):
\forall\gamma\in
\Gamma_{\mathrm{CG}}(L,\rho,\tau),
\,
\exists g\in SE(2),
\,
gT_\rho(\gamma)\subseteq C
\right\}.
\]

此泛函稱為：

\[
\boxed{
\text{正厚度中心生成掛谷—Moser橋接泛函}.
}
\]

它同時含有：

- 掛谷的方向完備性；
- 螺旋的內生轉向與中心外推；
- Moser 的曲線族普適容納；
- 幾何測度中的正厚度與非重疊約束。

---

# 10. 基本面積界

## 定理 10.1：普適容器的正下界

若橋接族非空，則任何普適容器 \(C\) 都必須至少容納其中一個完整管狀物件，因此

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\geq
2\rho L+\pi\rho^2.
}
\]

若研究的是無端帽法向帶，則

\[
\boxed{
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
\geq
2\rho L.
}
\]

### 證明

若

\[
gT_\rho(\gamma)\subseteq C,
\]

則由測度單調性與剛體運動不變性：

\[
\mu_2(C)
\geq
\mu_2(gT_\rho(\gamma))
=
\mu_2(T_\rho(\gamma)).
\]

再使用推論 6.3 即得。證畢。

---

# 11. 與 Moser 普適容器的上界接口

令 \(C\) 為一個可容納所有長度 \(L\) 中心曲線的 Moser 型容器。

若

\[
g\gamma\subseteq C,
\]

則

\[
g(\gamma\oplus\rho B)
=
g\gamma\oplus\rho B
\subseteq
C\oplus\rho B.
\]

因此：

\[
\boxed{
C\oplus\rho B
}
\]

是全部厚化曲線的普適容器。

故有

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\leq
\inf_{C\in\mathcal M_L}
\mu_2(C\oplus\rho B),
}
\]

其中 \(\mathcal M_L\) 是長度 \(L\) 曲線的 Moser 普適容器族。

若 \(C\) 為凸集，Steiner 公式給出

\[
\mu_2(C\oplus\rho B)
=
\mu_2(C)
+
\rho\,\operatorname{Per}(C)
+
\pi\rho^2.
\]

因此：

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\leq
\inf_{C\in\mathcal M_L^{\mathrm{conv}}}
\left[
\mu_2(C)
+
\rho\operatorname{Per}(C)
+
\pi\rho^2
\right].
}
\]

這提供了從既有 Moser 容器到正厚度橋接問題的直接上界傳遞。

---

# 12. 螺旋作為中心生成特例

在極座標中令

\[
\gamma(\vartheta)
=
r(\vartheta)
(\cos\vartheta,\sin\vartheta),
\]

並要求

\[
r(0)=0,
\qquad
r'(\vartheta)\geq0.
\]

若

\[
r'(\vartheta)=b>0,
\]

則

\[
r(\vartheta)=b\vartheta
\]

為阿基米德螺旋。

每轉一圈的徑向節距為

\[
p=2\pi b.
\]

但是：

\[
p\geq2\rho
\]

只能作為近圓圈層中的簡單圈距代理，不能取代精確的非重疊條件。

精確條件仍是

\[
\operatorname{reach}(\gamma)\geq\rho.
\]

因此本文將「相鄰圈邊界恰好接觸」定義為：

\[
\boxed{
\operatorname{reach}(\gamma)=\rho,
}
\]

而不是僅依賴徑向節距。

---

# 13. 圓、螺旋與完整轉向單元

總轉角等於 \(2\pi\) 不足以推出曲線是圓。

只有在曲率處處相同：

\[
\kappa(s)\equiv\frac1R
\]

時，完整 \(2\pi\) 轉向單元才是半徑 \(R\) 的圓。

因此：

\[
\boxed{
\text{圓是常曲率的完整轉向單元。}
}
\]

若在完成一個局部完整轉向後，生成半徑仍持續向外增加，則全域幾何不能維持為同一圓，而轉化成螺旋式層序。

所以：

\[
\boxed{
\text{圓是局部轉向語言；
螺旋是多個轉向單元的全域連接語言。}
}
\]

---

# 14. 支撐函數接口

對任意緊集 \(X\subset\mathbb R^2\)，支撐函數為

\[
h_X(u)
=
\sup_{x\in X}x\cdot u.
\]

完整管狀鄰域滿足

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B.
\]

Minkowski 和的支撐函數可加，因此

\[
\boxed{
h_{T_\rho(\gamma)}(u)
=
h_\gamma(u)+\rho.
}
\]

若容器為 \(C\)，旋轉相位為 \(\phi\)，平移為 \(t\)，原曲線的容納缺口場為

\[
K_{C,\gamma}
(\theta;\phi,t)
=
h_\gamma(\theta-\phi)
+
t\cdot u_\theta
-
h_C(\theta).
\]

厚化後：

\[
\begin{aligned}
K_{C,T_\rho(\gamma)}
(\theta;\phi,t)
&=
h_\gamma(\theta-\phi)
+\rho
+t\cdot u_\theta
-h_C(\theta)\\
&=
K_{C,\gamma}
(\theta;\phi,t)
+\rho.
\end{aligned}
\]

因此：

\[
\boxed{
\text{正厚度在支撐空間中表現為各方向一致增加的常數壓力。}
}
\]

中心線的曲率、螺旋節距與轉向分布則控制非平凡的方向歪度。

---

# 15. 三層帳本

本文提出三個互相耦合的幾何帳本。

## 15.1 掛谷方向帳本

記錄：

\[
(
s,\phi(s),\Delta\phi,
\text{方向覆蓋度}
).
\]

## 15.2 螺旋曲率帳本

記錄：

\[
(
s,\kappa(s),
\theta(s),
r(s),
\operatorname{reach}(\gamma)
).
\]

## 15.3 Moser 容器壓力帳本

記錄：

\[
(
\theta,
h_\gamma(\theta),
h_C(\theta),
K^+_{C,\gamma}(\theta)
).
\]

三者的接口為：

\[
\boxed{
\phi(s)=\theta(s)+\frac{\pi}{2}
}
\]

以及

\[
\boxed{
h_{T_\rho(\gamma)}=h_\gamma+\rho.
}
\]

---

# 16. 主要新命題

## 命題 A：正厚度退化阻斷命題

對固定

\[
L>0,\qquad\rho>0,
\]

所有內部不可重疊的正交掛谷掃掠均滿足

\[
\mu_2(S_\rho(\gamma))=2\rho L.
\]

所以原始掛谷的任意小面積退化不能在本類中發生。

---

## 命題 B：極值轉移命題

在面積不變式成立後，單一運動的掃掠面積不再具有形狀極值。

非平凡最佳化由

\[
\inf_\gamma\mu_2(S_\rho(\gamma))
\]

轉移成

\[
\inf_C
\left\{
\mu_2(C):
C\text{ 普適容納全部 }S_\rho(\gamma)
\right\}.
\]

因此：

\[
\boxed{
\text{不可重疊正厚度條件，將掛谷型問題自然轉譯成 Moser 型問題。}
}
\]

---

## 命題 C：支撐壓力抬升命題

對任何中心生成曲線：

\[
K_{C,T_\rho(\gamma)}
=
K_{C,\gamma}+\rho.
\]

正厚度不改變中心線支撐函數的角向形狀，只將全部方向壓力一致抬升。

---

# 17. 新猜想與研究問題

## 猜想 17.1：非平凡普適餘量

定義無端帽面積餘量：

\[
\Xi(L,\rho,\tau)
=
\mathfrak B_{\mathrm{strip}}(L,\rho,\tau)
-
2\rho L.
\]

猜想對方向完備族：

\[
\tau\geq\pi
\]

時存在某些參數範圍，使

\[
\boxed{
\Xi(L,\rho,\tau)>0.
}
\]

這表示不存在一個與單一掃掠等面積的區域，可以容納全部方向完備中心生成掃掠。

---

## 猜想 17.2：薄厚度漸近律

研究

\[
\rho\to0^+
\]

時：

\[
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau).
\]

最低階已知下界為

\[
2\rho L.
\]

新的問題是是否存在

\[
c(L,\tau)>1
\]

使

\[
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
\sim
2c(L,\tau)\rho L.
\]

若

\[
c(L,\tau)=1,
\]

則普適容納餘量只出現在更高階。

若

\[
c(L,\tau)>1,
\]

則方向完備性即使在零厚度極限中，仍留下可正規化的面積成本。

---

## 猜想 17.3：接觸飽和螺旋命題

在固定長度、厚度與總轉向下，最具容器壓力的中心生成曲線，可能位於：

\[
\operatorname{reach}(\gamma)=\rho
\]

的接觸飽和邊界。

也就是相鄰圈層允許邊界交接，但不保留多餘間隙，也不發生內部重疊。

---

## 猜想 17.4：曲率集中命題

最困難的橋接曲線未必是常曲率螺旋。

其曲率可能集中於有限寬度轉向層，使多個容器接觸分支同時等高。

可研究：

\[
\theta_\varepsilon(s)
=
\theta_0
+
\Delta\theta\,F_\varepsilon(s),
\]

並檢查有限

\[
\varepsilon>0
\]

是否比零寬折點或常曲率分布產生更高的普適容納壓力。

---

# 18. 與完整 Moser 問題的關係

中心生成橋接族只是全部長度 \(L\) 曲線的一個受限子族：

\[
\Gamma_{\mathrm{CG}}
(L,\rho,\tau)
\subset
\mathcal C_L.
\]

因此，任何完整 Moser 普適容器都必須至少容納其中心線。

若研究厚化版本，則將 Moser 容器作 Minkowski 膨脹即可得到橋接問題的上界。

反方向則是：

> 若能在中心生成橋接族中找出比現有測試曲線更難容納的物件，它可以直接成為 Moser 下界或容器壓力研究的新測試族。

所以此橋接理論不是 Moser 問題的替代品，而是一個具備：

- 方向完備性；
- 正厚度；
- 不可重疊性；
- 曲率帳本；
- 螺旋生成結構；

的可控中介曲線族。

---

# 19. 研究程序

後續研究可依序進行：

1. 固定 \(L,\rho,\tau\)；
2. 生成滿足 reach 條件的中心曲線；
3. 計算法向掃掠與支撐函數；
4. 對候選容器求最佳剛體放置；
5. 建立方向—曲率—支撐三層帳本；
6. 搜尋接觸飽和與分支等高候選；
7. 比較圓弧、阿基米德螺旋、變曲率螺旋與曲率集中層；
8. 建立區間算術與可重播證書；
9. 再將最困難候選送回完整 Moser 蟲研究。

---

# 20. 限制

本文沒有證明：

1. 阿基米德螺旋是橋接族極值；
2. 接觸飽和曲線必然最難容納；
3. \(\Xi(L,\rho,\tau)>0\)；
4. 薄厚度係數 \(c(L,\tau)\) 存在；
5. 橋接族能決定完整 Moser 最優容器；
6. 原始掛谷、橋接問題與 Moser 問題彼此等價。

本文證明的是幾何接口與基本不變量，並提出新的普適容納問題。

---

# 21. 結論

原始掛谷問題、中心生成式雙向偏移螺旋與 Moser 蟲問題的真正交接，不是簡單地把三個「面積問題」並列。

其結構是：

\[
\boxed{
\text{掛谷外部方向運動}
\longrightarrow
\text{中心曲線內部切向生成}
\longrightarrow
\text{正厚度法向掃掠}
\longrightarrow
\text{Moser 型普適容納}.
}
\]

中心生成曲線把針的外部旋轉相位內化為切向相位：

\[
\phi=\theta+\frac{\pi}{2}.
\]

雙向偏移帶把連續針運動轉成正面積區域：

\[
S_\rho(\gamma)
=
\bigcup_s I_s.
\]

不可重疊條件則導出精確面積不變量：

\[
\boxed{
\mu_2(S_\rho(\gamma))
=
2\rho L.
}
\]

這個不變量封閉了掛谷的零面積退化，同時將最佳化的核心由「單一運動掃過多少面積」轉移成：

\[
\boxed{
\text{哪個最小區域能容納全部方向完備的中心生成掃掠？}
}
\]

這正是本文提出的：

\[
\boxed{
\text{正厚度中心生成掛谷—Moser橋接問題}.
}
\]

---

# 參考文獻

1. A. S. Besicovitch, *The Kakeya Problem*, The American Mathematical Monthly, 1963.
2. A. Chang and M. Csörnyei, *The Kakeya Needle Problem and the Existence of Besicovitch and Nikodym Sets for Rectifiable Sets*, Proceedings of the London Mathematical Society, 2019; arXiv:1609.01649.
3. R. Norwood, G. Poole, and M. Laidacker, *The Worm Problem of Leo Moser*, Discrete & Computational Geometry 7, 1992, 153–162.
4. T. Khandhawit, D. Pagonakis, and S. Sriswasdi, *Lower Bound for Convex Hull Area and Universal Cover Problems*, International Journal of Computational Geometry & Applications 23, 2013; arXiv:1101.5638.
5. W. Wichiramala and C. Panraksa, *Wetzel’s 30-60-90 Triangle Covers Unit Arcs*, arXiv:2606.14625, 2026.
