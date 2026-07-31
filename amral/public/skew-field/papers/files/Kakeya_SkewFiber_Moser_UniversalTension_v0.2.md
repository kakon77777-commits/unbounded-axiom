# 從原始掛谷針到 Moser 蟲 II  
## 量度守恆歪線纖維、信息忠實核與普適覆蓋張力

**副標題：** 中心生成式雙向偏移螺旋橋接理論的統一擴展  
**作者：** Neo.K  
**版本：** v0.2  
**日期：** 2026 年 7 月 27 日  
**研究性質：** 命題型幾何論文／統一框架／後續證明接口  
**狀態：** 管狀幾何部分含可直接證明定理；普適極值、漸近律與最優曲線仍屬開放命題

---

## 摘要

本文將三套原先分開發展的研究語言統一為同一個幾何框架：

1. 原始掛谷針問題中的方向完備運動；
2. 中心生成式雙向偏移螺旋的正厚度掃掠；
3. Moser 型普適容納問題中的覆蓋張力。

本文同時吸收「從二維總量到一維歪線」與「從一維度量線到萬有覆蓋張力」兩套既有方法，提出：

\[
\boxed{
\text{量度守恆歪線纖維—萬有覆蓋張力理論}
}
\]

其核心幾何物件為一條弧長參數中心曲線

\[
\gamma:[0,L]\to\mathbb R^2
\]

及其雙向法向帶

\[
S_\rho(\gamma)
=
\left\{
\gamma(s)+tN(s):
0\le s\le L,\;
-\rho\le t\le\rho
\right\}.
\]

若

\[
\operatorname{reach}(\gamma)>\rho,
\]

則法向座標是單射的，面積元素為

\[
d\mu_2
=
\left(
1-t\kappa(s)
\right)ds\,dt.
\]

由此立即得到面積不變式：

\[
\mu_2(S_\rho(\gamma))=2\rho L.
\]

本文進一步證明一個更強的量度展開結果：將歸一化二維面積投影到中心線弧長參數後，所得邊際測度恰為均勻測度

\[
\frac{ds}{L}.
\]

曲率資訊並未因總量均勻化而消失，而是轉移到每條法向纖維內的條件密度：

\[
p_s(t)
=
\frac{1-t\kappa(s)}{2\rho}.
\]

其一階矩滿足

\[
\mathbb E[t\mid s]
=
-\frac{\rho^2}{3}\kappa(s),
\]

故

\[
\boxed{
\kappa(s)
=
-\frac{3}{\rho^2}
\mathbb E[t\mid s].
}
\]

因此，在已知 \(L,\rho\) 的合法管狀曲線類中，纖維偏斜的一維函數可以恢復曲率，再由 Frenet 積分恢復中心曲線，僅差一個剛體運動。這使「二維總量的一維歪線展開」在此受限幾何類中得到一個信息忠實、可逆且量度守恆的精確特例。

為處理一般參數化、接觸退化及合同包含，本文再引入信息忠實距離核：

\[
D_{\gamma,\rho}
\left(
(s,t),(s',t')
\right)
=
\left\|
\gamma(s)+tN(s)
-
\gamma(s')-t'N(s')
\right\|.
\]

最後，對候選容器 \(C\) 定義正厚度橋接族的萬有未覆蓋張力：

\[
\mathfrak T_p
(C;L,\rho,\tau)
=
\sup_{\gamma\in\Gamma_{\mathrm{CG}}(L,\rho,\tau)}
\inf_{g\in E(2)}
\left[
\int_{T_\rho(\gamma)}
\operatorname{dist}(gx,C)^p
\,d\nu_{\gamma,\rho}(x)
\right]^{1/p}.
\]

橋接普適容納問題遂可精確改寫為：

\[
\mathfrak B(L,\rho,\tau)
=
\inf_C
\left\{
\mu_2(C):
\mathfrak T_p(C;L,\rho,\tau)=0
\right\}.
\]

本文的主要結論是：在正厚度與不可重疊條件下，單體掃掠面積被固定為守恆量；不同幾何物件的差異不再表現在總面積，而轉移為纖維歪度、距離核、支撐壓力與普適覆蓋張力。掛谷型面積極值因此自然轉化為 Moser 型普適容納極值。

**關鍵詞：** 掛谷針問題、Moser 蟲問題、量度守恆、歪線、纖維幾何、中心生成螺旋、管狀鄰域、距離核、覆蓋張力、支撐函數、曲率重建

---

# 1. 理論來源與統一問題

本文建立在三個先前研究節點上。

## 1.1 正厚度掛谷—Moser 橋接

第一個節點把掛谷針的外部方向運動轉化為中心曲線的內部切向轉動，並令一條正厚度針沿中心曲線法向移動。

其基本對應為：

\[
\phi(s)
=
\theta(s)+\frac{\pi}{2}.
\]

其中：

- \(\phi(s)\) 是針的方向；
- \(\theta(s)\) 是中心曲線切向角。

針掃掠出的區域恰為中心曲線的雙向法向帶。

## 1.2 二維總量的一維歪線展開

第二個節點提出：二維集合可以在總量守恆條件下，轉化為一維參數域上的容量、拓撲、分岔、方向與多尺度歪度結構。

核心問題是：

\[
\text{同樣的總量一，如何以不同幾何方式分布？}
\]

但一般二維集合的一維展開不必唯一，也未必信息忠實。

## 1.3 一維索引、距離核與覆蓋張力

第三個節點指出：若只保留一維順序，通常會失去原始幾何；若加入完整二點距離核

\[
D(s,t),
\]

則可在商空間上恢復原始度量結構。

合同包含也可改寫成等距嵌入，而未覆蓋部分可用距離張力衡量。

---

# 2. 本文的核心統一

本文把三者組成以下鏈條：

\[
\boxed{
\begin{aligned}
\text{掛谷外部方向相位}
&\longrightarrow
\text{中心線內部切向相位}\\
&\longrightarrow
\text{雙向法向正厚度掃掠}\\
&\longrightarrow
\text{量度守恆歪線纖維}\\
&\longrightarrow
\text{信息忠實距離核}\\
&\longrightarrow
\text{普適覆蓋張力}\\
&\longrightarrow
\text{Moser 型最小容器}.
\end{aligned}
}
\]

這條鏈條的關鍵不只是概念相似，而是每一層都有明確數學接口。

---

# 3. 中心曲線與 Frenet 標架

令

\[
\gamma:[0,L]\to\mathbb R^2
\]

為 \(C^2\) 弧長參數曲線：

\[
\|\gamma'(s)\|=1.
\]

定義切向量：

\[
T(s)=\gamma'(s),
\]

法向量：

\[
N(s)=R_{\pi/2}T(s),
\]

並令：

\[
T(s)
=
(\cos\theta(s),\sin\theta(s)).
\]

曲率為：

\[
\kappa(s)=\theta'(s).
\]

Frenet 公式為：

\[
T'(s)=\kappa(s)N(s),
\]

\[
N'(s)=-\kappa(s)T(s).
\]

---

# 4. 正交掛谷運動

## 定義 4.1

給定厚度半徑 \(\rho>0\)，對每個 \(s\) 定義法向針：

\[
I_s
=
\left\{
\gamma(s)+tN(s):
-\rho\le t\le\rho
\right\}.
\]

其長度為：

\[
2\rho.
\]

針的方向角為：

\[
\phi(s)=\theta(s)+\frac{\pi}{2}.
\]

因為：

\[
T(s)\cdot N(s)=0,
\]

針中心速度始終垂直於針的方向。

這稱為由 \(\gamma\) 生成的正交掛谷運動。

---

## 命題 4.2：方向完備性

若：

\[
\theta(L)-\theta(0)\ge\pi,
\]

則法向針經歷全部無向方向。

若：

\[
\theta(L)-\theta(0)\ge2\pi,
\]

則法向針經歷全部有向方向。

---

# 5. 雙向法向帶與完整管狀鄰域

定義法向參數化：

\[
F_\rho(s,t)
=
\gamma(s)+tN(s).
\]

雙向法向帶為：

\[
S_\rho(\gamma)
=
F_\rho
\left(
[0,L]\times[-\rho,\rho]
\right).
\]

若加入兩端半徑為 \(\rho\) 的半圓帽，則得到完整管狀鄰域：

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B.
\]

必須區分：

- \(S_\rho(\gamma)\)：法向截線的直接掃掠；
- \(T_\rho(\gamma)\)：與半徑 \(\rho\) 圓盤作 Minkowski 和後的完整厚化。

支撐函數的簡單平移律適用於 \(T_\rho(\gamma)\)。

---

# 6. 合法管狀條件

若：

\[
\operatorname{reach}(\gamma)>\rho,
\]

則每個距離中心線小於 \(\rho\) 的點都具有唯一最近中心點。

這保證：

1. 法向帶內部不自重疊；
2. \(F_\rho\) 在參數矩形內單射；
3. 局部曲率半徑大於 \(\rho\)；
4. Jacobian 不會改變符號。

本文所有精確面積與可逆展開定理，均先在：

\[
\operatorname{reach}(\gamma)>\rho
\]

條件下陳述。

接觸飽和情況：

\[
\operatorname{reach}(\gamma)=\rho
\]

則作為其邊界極限研究。

---

# 7. 面積不變量

## 定理 7.1：不可重疊正交掃掠面積不變量

若：

\[
\operatorname{reach}(\gamma)>\rho,
\]

則：

\[
\boxed{
\mu_2(S_\rho(\gamma))
=
2\rho L.
}
\]

### 證明

對法向參數化：

\[
F_\rho(s,t)=\gamma(s)+tN(s),
\]

有：

\[
\partial_sF_\rho
=
T(s)+tN'(s)
=
(1-t\kappa(s))T(s),
\]

以及：

\[
\partial_tF_\rho=N(s).
\]

故 Jacobian：

\[
J_\rho(s,t)
=
\det
\left(
\partial_sF_\rho,\partial_tF_\rho
\right)
=
1-t\kappa(s).
\]

由 reach 條件：

\[
1-t\kappa(s)>0.
\]

因此：

\[
\begin{aligned}
\mu_2(S_\rho(\gamma))
&=
\int_0^L
\int_{-\rho}^{\rho}
(1-t\kappa(s))
\,dt\,ds\\
&=
\int_0^L
2\rho\,ds\\
&=
2\rho L.
\end{aligned}
\]

證畢。

---

## 推論 7.2：含端帽管狀鄰域

對開曲線：

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L+\pi\rho^2.
}
\]

對簡單閉曲線：

\[
\boxed{
\mu_2(T_\rho(\gamma))
=
2\rho L.
}
\]

---

# 8. 量度守恆展開

令法向參數矩形為：

\[
Q_{\rho,L}
=
[0,L]\times[-\rho,\rho].
\]

在 \(Q_{\rho,L}\) 上定義測度：

\[
d\lambda_{\gamma,\rho}
=
(1-t\kappa(s))\,ds\,dt.
\]

由面積公式：

\[
(F_\rho)_*
\lambda_{\gamma,\rho}
=
\mu_2|_{S_\rho(\gamma)}.
\]

因此二維面積不是被近似成一維資料，而是被精確拉回到：

\[
\boxed{
\text{一維中心底空間}
\times
\text{一維法向纖維}
}
\]

上的帶權測度。

---

## 定義 8.1：量度守恆歪線纖維展開

定義：

\[
\mathfrak U_\rho
\left(
S_\rho(\gamma)
\right)
=
\left(
[0,L],
\{\mathcal F_s\}_{s\in[0,L]},
J_\gamma,
D_{\gamma,\rho}
\right),
\]

其中：

\[
\mathcal F_s=[-\rho,\rho],
\]

\[
J_\gamma(s,t)=1-t\kappa(s),
\]

而 \(D_{\gamma,\rho}\) 為後文定義的距離核。

此展開不是普通投影，也不是只保留中心線，而是：

\[
\boxed{
\text{一維基底}
+
\text{法向纖維}
+
\text{量度 Jacobian}
+
\text{幾何關係核}.
}
\]

---

# 9. 基底邊際均勻定理

對法向帶的歸一化面積測度，定義：

\[
\nu_{\gamma,\rho}
=
\frac{\mu_2|_{S_\rho(\gamma)}}{2\rho L}.
\]

令：

\[
\pi_s:
Q_{\rho,L}\to[0,L],
\qquad
\pi_s(s,t)=s.
\]

## 定理 9.1：基底邊際均勻性

歸一化二維面積沿中心參數投影後，得到：

\[
\boxed{
(\pi_s)_*
(F_\rho^{-1})_*
\nu_{\gamma,\rho}
=
\frac{ds}{L}.
}
\]

### 證明

對任意可測集合 \(E\subset[0,L]\)：

\[
\begin{aligned}
\nu_{\gamma,\rho}
\left(
F_\rho(E\times[-\rho,\rho])
\right)
&=
\frac{1}{2\rho L}
\int_E
\int_{-\rho}^{\rho}
(1-t\kappa(s))
\,dt\,ds\\
&=
\frac{1}{2\rho L}
\int_E2\rho\,ds\\
&=
\frac{|E|}{L}.
\end{aligned}
\]

證畢。

---

## 解釋

這一定理表示：

\[
\boxed{
\text{每一單位弧長都承載相同的總面積 }2\rho\,ds.
}
\]

因此，歸一化後的二維總量被精確展開成一條均勻的一維容量線。

這正是「二維總量歸一後展開為一」在管狀幾何中的精確實現。

---

# 10. 曲率不消失：它轉移到纖維偏斜

雖然基底邊際是均勻的，但固定 \(s\) 時，纖維上的條件密度為：

\[
\boxed{
p_s(t)
=
\frac{1-t\kappa(s)}{2\rho},
\qquad
-\rho\le t\le\rho.
}
\]

此密度在 \(t\) 上是線性的。

若：

\[
\kappa(s)=0,
\]

則：

\[
p_s(t)=\frac{1}{2\rho},
\]

纖維分布完全均勻。

若：

\[
\kappa(s)>0,
\]

則纖維的一側密度增加、另一側密度降低。

因此曲率在一維化後表現為：

\[
\boxed{
\text{法向纖維內的量度歪斜}.
}
\]

---

# 11. 曲率—纖維一階矩定理

## 定理 11.1

纖維條件平均位置滿足：

\[
\boxed{
m_\gamma(s)
:=
\mathbb E[t\mid s]
=
-\frac{\rho^2}{3}\kappa(s).
}
\]

因此：

\[
\boxed{
\kappa(s)
=
-\frac{3}{\rho^2}m_\gamma(s).
}
\]

### 證明

\[
\begin{aligned}
m_\gamma(s)
&=
\int_{-\rho}^{\rho}
t\,p_s(t)\,dt\\
&=
\frac{1}{2\rho}
\int_{-\rho}^{\rho}
t(1-t\kappa(s))\,dt\\
&=
-\frac{\kappa(s)}{2\rho}
\int_{-\rho}^{\rho}t^2\,dt\\
&=
-\frac{\kappa(s)}{2\rho}
\cdot
\frac{2\rho^3}{3}\\
&=
-\frac{\rho^2}{3}\kappa(s).
\end{aligned}
\]

證畢。

---

## 推論 11.2：曲率歪線

可定義一維歪線：

\[
K_{\gamma,\rho}(s)
=
m_\gamma(s).
\]

則：

\[
K_{\gamma,\rho}(s)=0
\]

對應局部直線，

\[
K_{\gamma,\rho}(s)\ne0
\]

對應局部曲率。

此時「歪線」不再只是概念性特徵，而是具有精確幾何反演公式。

---

# 12. 信息忠實重建定理

## 定理 12.1：由纖維歪線重建中心曲線

已知：

1. 曲線長度 \(L\)；
2. 厚度 \(\rho\)；
3. 纖維一階矩函數 \(m_\gamma(s)\)；
4. 初始位置 \(\gamma(0)\)；
5. 初始切向角 \(\theta(0)\)。

則可以唯一重建 \(\gamma\)。

### 證明

由定理 11.1：

\[
\kappa(s)
=
-\frac{3}{\rho^2}m_\gamma(s).
\]

再積分得到：

\[
\theta(s)
=
\theta(0)
+
\int_0^s\kappa(u)\,du.
\]

最後：

\[
\gamma(s)
=
\gamma(0)
+
\int_0^s
(\cos\theta(u),\sin\theta(u))
\,du.
\]

證畢。

---

## 推論 12.2：剛體等價類中的信息忠實性

若忽略初始位置與初始角度，則：

\[
m_\gamma(s)
\]

決定中心曲線直到一個平移與旋轉。

因此，在定向參數固定的合法管狀曲線類中：

\[
\boxed{
(L,\rho,m_\gamma)
}
\]

是中心曲線剛體等價類的一個信息忠實一維表示。

若允許反射或反向參數化，則還需對：

\[
m(s)
\longleftrightarrow
-m(L-s)
\]

建立相應商關係。

---

# 13. 展開—回填對偶

定義回填算子：

\[
\mathfrak T_\rho
(\gamma)
=
S_\rho(\gamma).
\]

定義展開算子：

\[
\mathfrak U_\rho
(S_\rho(\gamma))
=
(L,\rho,m_\gamma,D_{\gamma,\rho}).
\]

在合法管狀類中：

\[
\boxed{
\mathfrak T_\rho
\circ
\mathfrak R_\rho
\circ
\mathfrak U_\rho
=
\operatorname{Id},
}
\]

其中 \(\mathfrak R_\rho\) 表示由 \(m_\gamma\) 重建中心曲線。

換言之：

\[
\boxed{
\text{二維法向帶}
\longrightarrow
\text{一維纖維歪線}
\longrightarrow
\text{中心曲線}
\longrightarrow
\text{二維法向帶}
}
\]

構成量度守恆的展開—回填循環。

需要注意：這不是所有二維集合的一般定理，而是對具有唯一法向管狀結構的集合成立。

---

# 14. 信息忠實距離核

即使纖維一階矩足以重建合法中心曲線，仍需一個更一般的證明層，以處理：

- 接觸飽和；
- 邊界退化；
- 不同參數化；
- 非標準纖維；
- 一般合同嵌入；
- 數值近似後的忠實驗證。

對參數點：

\[
z=(s,t),
\qquad
z'=(s',t'),
\]

定義：

\[
\boxed{
D_{\gamma,\rho}(z,z')
=
\left\|
F_\rho(s,t)-F_\rho(s',t')
\right\|.
}
\]

若法向參數化失去單射性，則 \(D\) 是偽度量。定義：

\[
z\sim z'
\iff
D_{\gamma,\rho}(z,z')=0.
\]

商空間：

\[
X_{\gamma,\rho}
=
Q_{\rho,L}/\!\sim
\]

配上由 \(D\) 誘導的距離後，與法向帶的歐氏度量空間等距。

因此：

\[
\boxed{
\text{歪線纖維是低成本表示層；
距離核是信息忠實證明層。}
}
\]

---

# 15. 全局一維索引化

若需要與一般一維索引理論完全接軌，可取一個滿射：

\[
\eta:[0,1]\to Q_{\rho,L},
\]

再定義：

\[
q_{\gamma,\rho}
=
F_\rho\circ\eta.
\]

一維索引上的距離核為：

\[
\widetilde D_{\gamma,\rho}(u,v)
=
\left\|
q_{\gamma,\rho}(u)
-
q_{\gamma,\rho}(v)
\right\|.
\]

因此完整二維法向帶可以表示成：

\[
\boxed{
[0,1]
+
\widetilde D_{\gamma,\rho}(u,v).
}
\]

但這種全局壓平會隱藏自然的中心線—法向纖維結構。

所以本文主張：

- 幾何建模層使用一維基底＋纖維；
- 信息忠實證明層可使用一維索引＋距離核。

---

# 16. 最小充分歪線

一般二維集合可能需要完整距離核才能忠實表示。

但對本文的合法管狀曲線類，已證明：

\[
m_\gamma(s)
\]

足以恢復曲率與中心線。

因此可提出：

## 命題 16.1：任務充分歪線

對任務：

\[
\mathcal T
=
\text{合法管狀曲線的剛體同一性判定},
\]

表示：

\[
\mathfrak U^\star_{\mathcal T}
(\gamma)
=
(L,\rho,m_\gamma)
\]

在固定定向參數下是信息充分的。

這是「最小充分歪線」構想的一個精確候選。

它比完整距離核更小，但只適用於受限曲線類。

---

# 17. 單體面積守恆與異形張力

對所有合法中心曲線：

\[
\mu_2(S_\rho(\gamma))
=
2\rho L.
\]

因此：

\[
\mu_2(S_\rho(\gamma_1))
=
\mu_2(S_\rho(\gamma_2))
\]

對任意同長、同厚度合法曲線成立。

但它們的：

- 支撐函數；
- 凸包；
- 方向寬度；
- 距離核；
- 容器嵌入難度；

一般不同。

所以：

\[
\boxed{
\text{總量相同}
\not\Rightarrow
\text{容納張力相同}.
}
\]

這導出本文的中心原則：

\[
\boxed{
\text{總量守恆後，形狀差異轉化為歪度與張力差異。}
}
\]

---

# 18. 未覆蓋距離張力

對緊閉容器 \(C\subset\mathbb R^2\)，定義固定配置下的局部未覆蓋張力：

\[
\delta_{\gamma,\rho,C}(x;g)
=
\operatorname{dist}(gx,C).
\]

令：

\[
\nu_{\gamma,\rho}
=
\frac{
\mu_2|_{T_\rho(\gamma)}
}{
\mu_2(T_\rho(\gamma))
}
\]

為厚化曲線的歸一化面積測度。

對：

\[
1\le p<\infty,
\]

定義：

\[
N_p
(T_\rho(\gamma),C;g)
=
\left[
\int_{T_\rho(\gamma)}
\operatorname{dist}(gx,C)^p
\,d\nu_{\gamma,\rho}(x)
\right]^{1/p}.
\]

再對剛體運動取最小：

\[
N_p
(T_\rho(\gamma),C)
=
\inf_{g\in E(2)}
N_p
(T_\rho(\gamma),C;g).
\]

---

## 定理 18.1：零張力與精確包含

若 \(T_\rho(\gamma)\) 為緊集且 \(C\) 為閉集，則：

\[
\boxed{
N_p(T_\rho(\gamma),C)=0
}
\]

在最小值可達或存在零張力極限配置的適當緊緻條件下，等價於存在：

\[
g\in E(2)
\]

使：

\[
gT_\rho(\gamma)\subseteq C.
\]

固定 \(g\) 的版本則直接成立：

\[
N_p(T_\rho(\gamma),C;g)=0
\iff
gT_\rho(\gamma)\subseteq C.
\]

---

# 19. 中心生成橋接族

令：

\[
\Gamma_{\mathrm{CG}}(L,\rho,\tau)
\]

為滿足以下條件的中心曲線族：

1. \(C^2\) 弧長參數；
2. 長度為 \(L\)；
3. \(\gamma(0)=0\)；
4. 徑向不倒退；
5. 切向相位單調；
6. 總轉向至少為 \(\tau\)；
7. \(\operatorname{reach}(\gamma)>\rho\)。

當：

\[
\tau=\pi
\]

時，法向針完成全部無向方向。

當：

\[
\tau=2\pi
\]

時，完成全部有向方向。

---

# 20. 萬有覆蓋張力

定義：

\[
\boxed{
\mathfrak T_p
(C;L,\rho,\tau)
=
\sup_{\gamma\in\Gamma_{\mathrm{CG}}(L,\rho,\tau)}
N_p(T_\rho(\gamma),C).
}
\]

其含義是：

> 在全部合法中心生成厚化曲線中，選取對容器 \(C\) 最難消除未覆蓋張力的物件。

若：

\[
\mathfrak T_p(C;L,\rho,\tau)=0,
\]

則每一條橋接族曲線都可在某個剛體配置下放入 \(C\)。

---

# 21. 橋接普適容納泛函

定義：

\[
\boxed{
\mathfrak B
(L,\rho,\tau)
=
\inf_C
\left\{
\mu_2(C):
\mathfrak T_p(C;L,\rho,\tau)=0
\right\}.
}
\]

這是本文的正厚度中心生成掛谷—Moser橋接問題。

它不是：

- 原始掛谷問題；
- 完整 Moser 蟲問題；
- Lebesgue 萬有覆蓋問題。

它是一個介於方向完備運動與全部單位曲線普適容納之間的受控中介族。

---

# 22. 基本面積下界

任何可容納全部橋接物件的容器，至少必須容納其中一個完整厚化曲線。

因此：

\[
\boxed{
\mathfrak B(L,\rho,\tau)
\ge
2\rho L+\pi\rho^2.
}
\]

對無端帽法向帶版本：

\[
\boxed{
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
\ge
2\rho L.
}
\]

定義普適容納餘量：

\[
\Xi(L,\rho,\tau)
=
\mathfrak B_{\mathrm{strip}}
(L,\rho,\tau)
-
2\rho L.
\]

真正非平凡的問題是：

\[
\boxed{
\Xi(L,\rho,\tau)
\stackrel{?}{>}0.
}
\]

---

# 23. 支撐函數接口

完整管狀鄰域滿足：

\[
T_\rho(\gamma)
=
\gamma\oplus\rho B.
\]

因此：

\[
\boxed{
h_{T_\rho(\gamma)}(u)
=
h_\gamma(u)+\rho.
}
\]

若容器缺口場定義為：

\[
K_{C,\gamma}
(\vartheta;\phi,a)
=
h_\gamma(\vartheta-\phi)
+
a\cdot u_\vartheta
-
h_C(\vartheta),
\]

則厚化後：

\[
\boxed{
K_{C,T_\rho(\gamma)}
=
K_{C,\gamma}+\rho.
}
\]

所以正厚度的作用是：

\[
\boxed{
\text{各方向支撐壓力一致抬升 }\rho.
}
\]

而曲率分布與中心線形狀則決定角向非均勻歪度。

---

# 24. 支撐、張力與距離核三層架構

本文提出三層計算—證明架構。

## 24.1 支撐層

使用：

\[
h_\gamma(\vartheta)
\]

與：

\[
K_{C,\gamma}(\vartheta)
\]

快速分析方向壓力、相位、接觸分支與 hard cases。

## 24.2 張力層

使用：

\[
N_p(T_\rho(\gamma),C)
\]

衡量候選容器仍未消除的整體覆蓋缺口。

## 24.3 距離核層

使用：

\[
D_{\gamma,\rho}
\]

進行信息忠實的幾何同一性、等距嵌入與最終證書驗證。

因此：

\[
\boxed{
\text{support}
+
\text{tension}
+
\text{metric kernel}
}
\]

分別負責：

- 快速必要條件；
- 最壞曲線搜尋與容器優化；
- 最終忠實驗證。

---

# 25. 歪度場與張力泛函的分工

可定義中心生成曲線的一維狀態：

\[
\mathbf K_{\gamma,\rho}(s)
=
\left(
m_\gamma(s),
\kappa(s),
\theta(s),
r(s),
\operatorname{reach}_s(\gamma)
\right).
\]

再加入方向參數：

\[
\mathbf K_{\gamma,\rho}(s,\vartheta)
=
\left(
\mathbf K_{\gamma,\rho}(s),
h_\gamma(\vartheta),
K_{C,\gamma}(\vartheta)
\right).
\]

其中：

\[
\boxed{
\text{歪度場}
}
\]

負責局部結構與候選生成；

\[
\boxed{
\text{覆蓋張力}
}
\]

負責全域可行性與最壞情況判定。

---

# 26. 掛谷、橋接問題與 Moser 的包含關係

令：

- \(\mathcal L\)：單位線段方向族；
- \(\Gamma_{\mathrm{CG}}\)：中心生成方向完備曲線族；
- \(\mathcal C_L\)：全部長度 \(L\) 曲線族。

在中心線層可寫成：

\[
\mathcal L
\subset
\Gamma_{\mathrm{CG}}
\subset
\mathcal C_L
\]

的研究性包含關係，但需要注意：

- 原始掛谷還包含連續運動路徑要求；
- Moser 只要求各曲線分別存在最佳放置；
- 橋接問題加入正厚度、中心生成與不可重疊。

因此三者不是等價問題。

---

# 27. 等量異形張力分離命題

## 命題 27.1

存在同長、同厚度的合法中心曲線：

\[
\gamma_1,\gamma_2
\]

使：

\[
\mu_2(S_\rho(\gamma_1))
=
\mu_2(S_\rho(\gamma_2)),
\]

但其支撐函數不同：

\[
h_{\gamma_1}
\ne
h_{\gamma_2}.
\]

因此存在某些容器 \(C\)，使：

\[
N_p(T_\rho(\gamma_1),C)
\ne
N_p(T_\rho(\gamma_2),C).
\]

### 解釋

面積不變量只保存總量，不保存形狀。

曲率歪線、支撐函數與距離核則保存形狀分布。

---

# 28. 新猜想

## 猜想 28.1：正普適餘量

對某些：

\[
L,\rho,\tau>0,
\]

有：

\[
\boxed{
\Xi(L,\rho,\tau)>0.
}
\]

即不存在一個面積恰等於單體掃掠面積的區域，可以容納全部橋接族物件。

---

## 猜想 28.2：薄厚度正規化極限

研究：

\[
c(L,\tau)
=
\lim_{\rho\to0^+}
\frac{
\mathfrak B_{\mathrm{strip}}(L,\rho,\tau)
}{
2\rho L
},
\]

若極限存在。

可能情形：

\[
c(L,\tau)=1
\]

表示普適餘量是高階小量；

\[
c(L,\tau)>1
\]

表示方向完備性在零厚度正規化後仍留下固定成本。

---

## 猜想 28.3：接觸飽和原則

最具普適容器壓力的曲線可能位於：

\[
\operatorname{reach}(\gamma)=\rho
\]

的邊界。

即相鄰部分剛好接觸，但不發生正面積重疊。

---

## 猜想 28.4：有限寬度曲率集中

橋接族中的 hard case 未必是常曲率螺旋。

可能存在有限寬度曲率層：

\[
\kappa_\varepsilon(s)
\]

比零寬折點或均勻曲率分布產生更高容器張力。

---

## 猜想 28.5：任務充分核

對橋接普適容納任務，可能存在比完整距離核更小的表示：

\[
\mathfrak U^\star_{\mathrm{bridge}}
\]

使其保留判定：

\[
N_p(T_\rho(\gamma),C)=0
\]

所需的全部資訊，但計算成本低於完整 \(D_{\gamma,\rho}\)。

候選內容包括：

\[
(
m_\gamma,
h_\gamma,
\mathcal E_{\mathrm{contact}},
\operatorname{reach}
).
\]

---

# 29. 計算研究架構

## 29.1 曲線生成

以曲率函數為主變數：

\[
\kappa(s).
\]

由：

\[
\theta(s)
=
\theta_0+\int_0^s\kappa(u)\,du
\]

及：

\[
\gamma(s)
=
\gamma_0+
\int_0^s
(\cos\theta(u),\sin\theta(u))
\,du
\]

重建中心線。

## 29.2 合法性檢查

檢查：

\[
\operatorname{reach}(\gamma)\ge\rho,
\]

總轉向：

\[
\int_0^L\kappa(s)\,ds\ge\tau,
\]

以及中心生成條件。

## 29.3 歪線表示

計算：

\[
m_\gamma(s)
=
-\frac{\rho^2}{3}\kappa(s).
\]

## 29.4 支撐壓力

計算：

\[
h_\gamma(\vartheta),
\qquad
K_{C,T_\rho(\gamma)}.
\]

## 29.5 張力優化

計算：

\[
\inf_{g\in E(2)}
N_p(T_\rho(\gamma),C;g).
\]

## 29.6 忠實驗證

對最困難候選建立：

\[
D_{\gamma,\rho}
\]

的離散矩陣、區間證書或形式化合同包含判定。

---

# 30. 證明層級

本文主張應嚴格區分以下層級。

## Level 1：歪線啟發式

使用：

\[
m_\gamma(s),
\quad
\kappa(s),
\quad
h_\gamma
\]

搜尋 hard cases。

## Level 2：張力計算

使用：

\[
N_p
\]

比較候選容器與曲線。

## Level 3：距離核忠實驗證

使用：

\[
D_{\gamma,\rho}
\]

確認幾何未因壓縮表示而失真。

## Level 4：區間算術

包住：

- 曲線積分；
- 支撐極值；
- 剛體配置；
- 張力下界。

## Level 5：形式化證明

在 Lean、Coq 或其他系統中形式化：

- 管狀面積公式；
- 基底邊際均勻性；
- 曲率一階矩反演；
- 零張力包含等價；
- 特定有限證書。

---

# 31. 本文已證明與尚未證明

## 已證明或具有直接標準證明

1. 正交掛谷掃掠等於雙向法向帶；
2. 合法法向帶面積為 \(2\rho L\)；
3. 歸一面積的中心弧長邊際為均勻測度；
4. 纖維條件密度為：
   \[
   p_s(t)=\frac{1-t\kappa(s)}{2\rho};
   \]
5. 纖維一階矩恢復曲率；
6. 曲率與初始標架恢復中心曲線；
7. 完整厚化的支撐函數增加 \(\rho\)；
8. 固定配置下零距離張力等價於精確包含。

## 尚未證明

1. 橋接普適容器的最優形狀；
2. \(\Xi(L,\rho,\tau)>0\)；
3. 薄厚度正規化極限存在；
4. 接觸飽和曲線必為 hard case；
5. 曲率集中族的最優寬度；
6. 最小任務充分核的存在與唯一性；
7. 橋接族能否改進完整 Moser 問題的已知界；
8. 完整形式化證明。

---

# 32. 理論意義

本文得到一個比「二維變一維」更精確的結論。

對合法管狀曲線而言：

\[
\boxed{
\text{二維總量}
=
\text{一維均勻容量基底}
+
\text{法向纖維歪斜}.
}
\]

一維基底保存：

\[
\frac{ds}{L},
\]

纖維歪斜保存：

\[
\kappa(s).
\]

因此：

\[
\boxed{
\text{面積守恆}
\quad\text{與}\quad
\text{形狀信息守恆}
}
\]

在這個受限幾何類中可以同時成立。

而當單體總面積全部相同時，真正需要優化的就不再是單體面積，而是：

\[
\boxed{
\text{多個等量異形物件對同一容器造成的普適覆蓋張力。}
}
\]

---

# 33. 結論

本文將原始掛谷、中心生成螺旋、量度守恆歪線、信息忠實距離核與 Moser 普適容納統一為：

\[
\boxed{
\text{量度守恆歪線纖維—萬有覆蓋張力理論}.
}
\]

其核心鏈條為：

\[
\boxed{
\begin{aligned}
\phi(s)
&=
\theta(s)+\frac{\pi}{2},\\
S_\rho(\gamma)
&=
\bigcup_s I_s,\\
\mu_2(S_\rho(\gamma))
&=
2\rho L,\\
(\pi_s)_*\nu_{\gamma,\rho}
&=
\frac{ds}{L},\\
p_s(t)
&=
\frac{1-t\kappa(s)}{2\rho},\\
\kappa(s)
&=
-\frac{3}{\rho^2}\mathbb E[t\mid s],\\
D_{\gamma,\rho}
&=
\text{信息忠實核},\\
\mathfrak T_p(C)
&=
\text{萬有覆蓋張力},\\
\mathfrak B
&=
\inf\{\mu_2(C):\mathfrak T_p(C)=0\}.
\end{aligned}
}
\]

因此，這個新框架的基本哲學可以濃縮為：

\[
\boxed{
\text{總量守恆後，幾何不會消失；
它會從面積差異轉化為纖維歪度、距離關係與覆蓋張力。}
}
\]

原始掛谷問題中的面積退化，在正厚度與不可重疊條件下被阻斷；單體面積隨之成為不變量。問題的非平凡性因此轉移到 Moser 型問題：

\[
\boxed{
\text{哪個最小容器能同時消除全部等量異形掃掠的覆蓋張力？}
}
\]

這是本文提出的統一橋接問題，也是後續計算、區間證書與形式化研究的起點。

---

# 參考與理論來源

1. Neo.K，〈從二維總量到一維歪線：一種量度守恆的幾何展開框架〉，v0.1。
2. Neo.K，〈從一維度量線到萬有覆蓋張力：Lebesgue 萬有覆蓋問題的一維化命題猜想、信息忠實條件與局部削減方法論〉，v0.1。
3. Neo.K，〈從原始掛谷針到 Moser 蟲：中心生成式雙向偏移螺旋的正厚度橋接理論〉，v0.1。
4. A. S. Besicovitch，關於 Kakeya 問題與方向線段集合的經典研究。
5. R. Norwood、G. Poole、M. Laidacker，關於 Leo Moser 蟲問題的研究。
