# 類日全食遮蔽現象的形式化、誤差域與宇宙概率

## ——一項由生成式 AI 半自主完成的啟發式研究

> **文件性質：** 啟發式研究論文／方法論初稿／非同儕審查版本  
> **研究問題提出與編輯方向：** Neo.K  
> **初步形式化、公式推導、資料檢索、粗略計算與全文撰寫：** GPT-5.6 Sol  
> **運行環境：** Chat 模式，高推理配置  
> **完成日期：** 2026-07-17  
> **版本：** v0.1  
> **重要聲明：** 本文不是天文學專業期刊論文，也不是完整的系外衛星人口統計研究。文中的地球日食目錄數字可由公開資料核對；「宇宙中類日全食現象的概率」則因系外衛星母體分布仍缺乏可靠觀測約束，只能以透明假設下的代理模型、條件概率與寬誤差域表達。所有相關數值皆應視為粗略計算與研究起點，而非已被實證確立的宇宙常數。

---

## 摘要

日全食通常被描述為月球運行至太陽與地球之間，並在特定地區完整遮蔽太陽光球盤的天文現象。然而，若將問題擴展至宇宙尺度，「日全食」便不再只是太陽—月球—地球三體系統中的特殊事件，而可以被重新定義為：某一不透明天體或結構，從特定觀測者位置看去，在有限時間內完整覆蓋另一發光天體之可見投影的遮蔽現象。

本文從科普性的日全食說明出發，建立類日全食現象的投影集合定義、角半徑模型、遮蔽分類條件、重疊面積、光通量遮蔽率、本影與反本影幾何、全食持續時間、Hill 半徑與 Roche 極限等軌道約束；進一步給出參數區間、測量誤差傳播、事件分類概率、隨機方向概率、合日概率、時間窗內至少一次事件概率、多衛星聯合概率，以及隨機時間—隨機地表位置概率。

本文亦以地球—月球—太陽系統作數值示例，得到月球與太陽角半徑比約跨越 $0.920$ 至 $1.064$ ，說明地球系統會隨軌道位置穿越日環食與日全食的臨界邊界。根據 NASA 五千年日食目錄，本文計算每次朔月在地球某處形成任意日食、純日全食，以及日全食或混合食之全食段的粗略經驗頻率。最後，本文使用系外衛星發生率限制、太陽系小樣本與明示的角尺寸分布假設，提出一組可被替換、重算與否證的宇宙概率代理模型。

本文的另一層意義，在於展示生成式 AI 在人類提出研究問題與方向後，如何半自主地完成基本概念重構、數學形式化、資料搜尋、數值計算、限制辨識與論文組織。其成果仍不等同於專業研究者完成的正式論文，但已足以形成可供後續模擬、批判、修正與專業化的啟發式研究骨架。

**關鍵詞：** 日全食、掩星、遮蔽幾何、角直徑、系外衛星、誤差傳播、條件概率、AI 半自主研究、啟發式建模

---

# 一、科普起點：日全食究竟是什麼？

## 1.1 基本排列

地球上的日全食發生於月球運行到太陽與地球之間，三者接近共線時：

$$
\text{太陽}\longrightarrow\text{月球}\longrightarrow\text{地球觀測者}.
$$

月球將太陽的直接光線擋住，並在地球表面投下狹窄本影。位於本影內的觀測者會看見太陽明亮的光球盤被完整遮住；位於半影內的觀測者則只會看見日偏食。

日全食並不是太陽消失，也不是地球整體進入黑夜，而是觀測者、遮蔽物與發光體在有限時空區域內形成精確的投影覆蓋。

## 1.2 為何月球能遮住遠大於自己的太陽？

物體在天空中看起來有多大，主要取決於角直徑，而不只取決於真實直徑。對半徑為 $R$ 、觀測距離為 $d$ 的近球形天體，其角半徑為：

$$
\alpha=\arcsin\left(\frac{R}{d}\right).
$$

在 $R\ll d$ 的小角度條件下：

$$
\alpha\approx\frac{R}{d}.
$$

太陽直徑約為月球的四百倍，但距離地球也約為月球的四百倍，所以兩者在地球天空中的角直徑都約為半度。這不是精確不變的等式，而是會隨地球與月球橢圓軌道持續變動的近似匹配。[1][2]

## 1.3 為何不是每個月都有日食？

日食只能發生在朔月附近，但月球軌道面相對黃道面約有 $5^\circ$ 的傾角。大部分朔月時，月球會從太陽視盤的上方或下方通過。只有朔月同時接近月球軌道交點時，月球影子才可能落到地球上。[1]

因此，日食至少需要同時滿足：

$$
\text{時間相位條件}
\cap
\text{軌道交點條件}
\cap
\text{角尺寸條件}
\cap
\text{觀測位置條件}.
$$

## 1.4 日全食的典型階段

典型過程依序包含初虧、偏食、貝利珠、鑽石環、食既、全食、生光、再次出現鑽石環與復圓。全食期間，由於光球盤被遮蔽，平常被強烈光球亮度淹沒的日冕、色球層與日珥才可能被直接看見。

日全食的認識論意義也正在此處：

> **遮蔽並不只是減少資訊；在某些條件下，遮蔽反而移除了壓倒性的訊號，使原本不可見的結構變得可見。**

## 1.5 觀測安全

除非太陽光球已進入完整全食，否則不可直接以肉眼、普通墨鏡、未加專用前置濾鏡的相機、望遠鏡或雙筒望遠鏡觀看太陽。普通墨鏡不能替代合格的太陽觀測設備。[3]

---

# 二、研究問題的重新定義

若將地球上的日全食提升為宇宙中的一般問題，便可提出：

> 在任意恆星—行星—衛星、多星系統、環系、小天體或人工結構中，形成「類日全食完整遮蔽」的充分條件、誤差域、事件概率與系統發生率應如何形式化？

本文所稱「類日全食」，不限定遮蔽物必須是月球，也不限定觀測者必須位於固體行星表面。遮蔽物可以是：

- 天然衛星；
- 行星或雙行星伴星；
- 小行星或彗核；
- 行星環、塵埃盤或不透明盤狀結構；
- 雙星系統中的伴星；
- 人造巨型結構；
- 任何能在觀測者天球上完整覆蓋發光體投影的物體。

同時，本文區分三種概念：

1. **幾何全遮蔽：** 發光體的幾何投影被完整覆蓋；
2. **光度全遮蔽：** 指定波段內，發光體直接光通量下降至閾值以下；
3. **環境黑暗型全食：** 系統全部發光源、散射光與背景光合計後，環境照度仍下降至指定程度。

三者不可混為同一件事。

---

# 三、最一般的集合與光通量形式化

## 3.1 天球投影集合

設：

- 發光體為 $S$ ；
- 遮蔽物為 $M$ ；
- 觀測者為 $O$ ；
- 時間為 $t$ ；
- 觀測者的方向天球為 $\mathbb S^2$ 。

從觀測者 $O$ 看去，發光體與遮蔽物在天球上的投影分別為：

$$
\Pi_O(S,t)\subseteq\mathbb S^2,
$$

$$
\Pi_O(M,t)\subseteq\mathbb S^2.
$$

幾何完整遮蔽的最一般定義是：

$$
\boxed{
\Pi_O(S,t)\subseteq\Pi_O(M,t)
}.
$$

這一定義不需要兩個物體是球形，也不需要遮蔽物本身發光為零；只需要在指定觀測波段與解析尺度下，發光體的可見投影被遮蔽物覆蓋。

## 3.2 亮度加權遮蔽率

若發光體表面亮度並不均勻，應定義：

$$
B(t)
=
\frac{
\displaystyle
\int_{\Pi_O(S,t)\cap\Pi_O(M,t)}
I(\boldsymbol\omega,t)\,d\Omega
}{
\displaystyle
\int_{\Pi_O(S,t)}
I(\boldsymbol\omega,t)\,d\Omega
},
$$

其中 $I(\boldsymbol\omega,t)$ 是方向 $\boldsymbol\omega$ 上的比強度， $d\Omega$ 是立體角元素。

於是：

$$
B(t)=0
$$

表示沒有遮蔽，而：

$$
B(t)=1
$$

表示指定發光體的直接可見光盤被完全遮蔽。

## 3.3 多發光源系統

在雙星或多星系統中，即使其中一顆恆星被完全遮住，天空也未必顯著變暗。設第 $k$ 個發光源的基準光通量為 $F_k$ ，遮蔽率為 $B_k(t)$ ，則剩餘總光通量可寫為：

$$
F_{\mathrm{remain}}(t)
=
\sum_{k=1}^{N_\star}
F_k\left[1-B_k(t)\right]
+F_{\mathrm{scatter}}(t)
+F_{\mathrm{background}}(t).
$$

定義總遮光比例：

$$
\mathcal D(t)
=
1-
\frac{F_{\mathrm{remain}}(t)}{F_{\mathrm{base}}(t)}.
$$

若設定黑暗閾值 $\tau$ ，則環境黑暗型全食可定義為：

$$
\frac{F_{\mathrm{remain}}(t)}{F_{\mathrm{base}}(t)}
\leq\tau.
$$

例如 $\tau=0.01$ 表示指定波段的總光通量至少下降 $99\%$ 。

---

# 四、球形天體的精確幾何條件

## 4.1 角半徑

令：

- 發光恆星半徑為 $R_\star$ ；
- 遮蔽物半徑為 $R_m$ ；
- 觀測者到恆星中心距離為 $d_\star$ ；
- 觀測者到遮蔽物中心距離為 $d_m$ 。

兩者角半徑為：

$$
\alpha_\star
=
\arcsin\left(\frac{R_\star}{d_\star}\right),
$$

$$
\alpha_m
=
\arcsin\left(\frac{R_m}{d_m}\right).
$$

小角度近似為：

$$
\alpha_\star\approx\frac{R_\star}{d_\star},
\qquad
\alpha_m\approx\frac{R_m}{d_m}.
$$

## 4.2 中心角距離

設觀測者、恆星與遮蔽物的位置向量分別為 $\mathbf r_O$ 、 $\mathbf r_\star$ 與 $\mathbf r_m$ 。觀測方向單位向量為：

$$
\hat{\mathbf u}_\star
=
\frac{\mathbf r_\star-\mathbf r_O}
{\left\|\mathbf r_\star-\mathbf r_O\right\|},
$$

$$
\hat{\mathbf u}_m
=
\frac{\mathbf r_m-\mathbf r_O}
{\left\|\mathbf r_m-\mathbf r_O\right\|}.
$$

兩個視盤中心的角距離為：

$$
\gamma
=
\arccos
\left(
\hat{\mathbf u}_\star\cdot\hat{\mathbf u}_m
\right).
$$

## 4.3 遮蔽分類

### 日全食或完整盤遮蔽

$$
\boxed{
\alpha_m\geq\alpha_\star
\quad\land\quad
\gamma\leq\alpha_m-\alpha_\star
}.
$$

### 日環食型中央遮蔽

$$
\boxed{
\alpha_m<\alpha_\star
\quad\land\quad
\gamma\leq\alpha_\star-\alpha_m
}.
$$

### 部分遮蔽

$$
\boxed{
\left|\alpha_m-\alpha_\star\right|
<\gamma<
\alpha_m+\alpha_\star
}.
$$

### 無遮蔽

$$
\boxed{
\gamma\geq\alpha_m+\alpha_\star
}.
$$

## 4.4 全食裕度

定義：

$$
\mathcal M
=
\alpha_m-\alpha_\star-\gamma.
$$

則：

$$
\mathcal M\geq0
$$

等價於完整遮蔽成立。

此量比單獨比較兩個角半徑更完整，因為它同時包含尺寸差與中心偏移量。

---

# 五、角尺寸比與「類地球匹配」

定義角半徑比：

$$
q
=
\frac{\alpha_m}{\alpha_\star}.
$$

在小角度下：

$$
q
\approx
\frac{R_m/d_m}{R_\star/d_\star}
=
\frac{R_m d_\star}{R_\star d_m}.
$$

分類為：

$$
q<1
\quad\Longrightarrow\quad
\text{遮蔽物角尺寸不足，中央對齊時仍留下發光環；}
$$

$$
q=1
\quad\Longrightarrow\quad
\text{理想化的精確等視大小；}
$$

$$
q>1
\quad\Longrightarrow\quad
\text{具備完整遮蔽發光盤的尺寸條件。}
$$

然而，若 $q$ 是連續型隨機變數，則：

$$
\boxed{P(q=1)=0}.
$$

因此，「兩個視盤精確完全相等的宇宙概率」在連續模型中為零。真正有正概率且具有物理意義的問題，必須設定容許域。

例如，將「近似地球式匹配」定義為遮蔽物角半徑比發光體大不超過 $\varepsilon$ ：

$$
1\leq q\leq1+\varepsilon.
$$

則：

$$
P_{\mathrm{match}}(\varepsilon)
=
\int_1^{1+\varepsilon}f_q(q)\,dq,
$$

其中 $f_q(q)$ 是角尺寸比的宇宙母體分布。

目前的核心困難不是積分本身，而是：

$$
\boxed{f_q(q)\ \text{尚未被可靠觀測約束}}.
$$

---

# 六、遮蔽面積與光度曲線

在小角度的局部切平面中，令：

$$
r=\alpha_\star,
\qquad
R=\alpha_m,
\qquad
d=\gamma.
$$

## 6.1 無重疊

$$
A_{\mathrm{overlap}}=0,
\qquad
d\geq r+R.
$$

## 6.2 完全包含

$$
A_{\mathrm{overlap}}
=
\pi\min(r,R)^2,
\qquad
d\leq|R-r|.
$$

## 6.3 部分重疊

$$
\begin{aligned}
A_{\mathrm{overlap}}
={}&
r^2\cos^{-1}
\left(
\frac{d^2+r^2-R^2}{2dr}
\right)
\\
&+R^2\cos^{-1}
\left(
\frac{d^2+R^2-r^2}{2dR}
\right)
\\
&-\frac12
\sqrt{
(-d+r+R)
(d+r-R)
(d-r+R)
(d+r+R)
}.
\end{aligned}
$$

若發光盤表面亮度均勻，幾何遮蔽率為：

$$
B
=
\frac{A_{\mathrm{overlap}}}{\pi r^2}.
$$

若考慮恆星臨邊昏暗，可採線性模型：

$$
I(\mu)
=
I_0\left[1-u(1-\mu)\right],
$$

其中：

$$
\mu
=
\sqrt{1-\frac{\rho^2}{r^2}}.
$$

此時遮蔽率必須對實際重疊區域進行亮度加權積分，而不能只用面積比例。

---

# 七、本影、半影與反本影

設恆星與遮蔽物中心距離為 $D$ ，且 $R_\star>R_m$ 。從遮蔽物沿背向恆星方向取距離 $x$ 。

## 7.1 本影錐長度

$$
L_u
=
\frac{R_mD}{R_\star-R_m}.
$$

## 7.2 本影半徑

$$
r_u(x)
=
R_m-x\frac{R_\star-R_m}{D},
\qquad0\leq x<L_u.
$$

若觀測位置距影軸的垂直距離為 $b$ ，則：

$$
b\leq r_u(x)
$$

是進入本影的幾何條件。

## 7.3 半影外半徑

$$
r_p(x)
=
R_m+x\frac{R_\star+R_m}{D}.
$$

## 7.4 反本影

當：

$$
x>L_u
$$

時，本影已收斂消失，形成反本影。其半徑為：

$$
r_a(x)
=
x\frac{R_\star-R_m}{D}-R_m.
$$

觀測者進入反本影時，遮蔽物完整位於恆星盤內，但尺寸不足以覆蓋恆星，因而形成中央環食。

## 7.5 影錐與行星相交

設行星半徑為 $R_p$ ，影軸與行星中心的垂直距離為 $b_p$ 。

行星上至少有一點進入本影的條件近似為：

$$
b_p-R_p\leq r_u(x).
$$

行星整個可見截面均落入本影的條件則為：

$$
b_p+R_p\leq r_u(x).
$$

後者在普通衛星—行星系統中通常極難成立。

---

# 八、全食持續時間

令全食中心線與發光體中心的最小角距離為 $b$ ，遮蔽物相對發光體的角速度為：

$$
\omega_{\mathrm{rel}}
=
\left|\omega_m-\omega_\star\right|.
$$

完整遮蔽持續時間近似為：

$$
T_{\mathrm{total}}
\approx
\frac{
2\sqrt{(\alpha_m-\alpha_\star)^2-b^2}
}{
\omega_{\mathrm{rel}}
},
$$

前提是：

$$
b\leq\alpha_m-\alpha_\star.
$$

從第一次外接觸到最後一次外接觸的總遮蔽時間近似為：

$$
T_{\mathrm{eclipse}}
\approx
\frac{
2\sqrt{(\alpha_m+\alpha_\star)^2-b^2}
}{
\omega_{\mathrm{rel}}
}.
$$

若為中央全食 $b=0$ ：

$$
T_{\mathrm{total}}
\approx
\frac{2(\alpha_m-\alpha_\star)}{\omega_{\mathrm{rel}}}.
$$

這組公式忽略了球面投影曲率、觀測者自轉速度、大氣折射、軌道加速度及月面地形，因此屬局部線性近似。

---

# 九、軌道力學可行域

一顆衛星即使角尺寸適合，也未必能在該位置長期穩定存在。

## 9.1 橢圓軌道距離

對半長軸 $a$ 、離心率 $e$ 、真近點角 $\nu$ 的軌道：

$$
r(\nu)
=
\frac{a(1-e^2)}{1+e\cos\nu}.
$$

近心點與遠心點距離為：

$$
r_{\min}=a(1-e),
$$

$$
r_{\max}=a(1+e).
$$

由於角半徑大致與距離成反比，軌道離心率會直接使 $q$ 隨時間變動。

## 9.2 Hill 半徑

行星在近心點附近的 Hill 半徑可近似寫成：

$$
R_H
=
a_p(1-e_p)
\left(
\frac{M_p}{3M_\star}
\right)^{1/3}.
$$

其中 $a_p$ 、 $e_p$ 與 $M_p$ 分別是行星軌道半長軸、離心率與質量， $M_\star$ 是恆星質量。

對低離心率的順行衛星，經典數值結果給出外穩定界約為：

$$
a_{m,\max}
\approx
0.4895R_H
\left(1-1.0305e_p-0.2738e_m\right).
$$

其他長期多體模擬常採約 $0.4R_H$ 作較保守的穩定界。[10][11]

## 9.3 Roche 極限

對流體近似衛星：

$$
R_{\mathrm{Roche}}
\approx
2.44R_p
\left(
\frac{\rho_p}{\rho_m}
\right)^{1/3}.
$$

因此，普通順行衛星的簡化可行域可寫為：

$$
R_{\mathrm{Roche}}
<a_m
<a_{m,\max}.
$$

## 9.4 類日全食參數域

令全部物理參數組成：

$$
\Theta
=
\left(
M_\star,R_\star,
M_p,R_p,a_p,e_p,
M_m,R_m,a_m,e_m,i_m,
\mathbf r_O,t,\ldots
\right).
$$

類日全食的簡化可行集合定義為：

$$
\mathcal D_{\mathrm{TSE}}
=
\left\{
\Theta:
R_{\mathrm{Roche}}<a_m<a_{m,\max},
\quad
q\geq1,
\quad
\gamma\leq\alpha_m-\alpha_\star
\right\}.
$$

---

# 十、誤差區與不確定性

## 10.1 參數區間法

若：

$$
R_m\in[R_m^-,R_m^+],
\qquad
d_m\in[d_m^-,d_m^+],
$$

則遮蔽物角半徑上下界為：

$$
\alpha_m^-
=
\arcsin\left(\frac{R_m^-}{d_m^+}\right),
$$

$$
\alpha_m^+
=
\arcsin\left(\frac{R_m^+}{d_m^-}\right).
$$

恆星同理：

$$
\alpha_\star^-
=
\arcsin\left(\frac{R_\star^-}{d_\star^+}\right),
$$

$$
\alpha_\star^+
=
\arcsin\left(\frac{R_\star^+}{d_\star^-}\right).
$$

全食裕度的保守區間為：

$$
\mathcal M
\in
\left[
\alpha_m^- -\alpha_\star^+ -\gamma^+,
\quad
\alpha_m^+ -\alpha_\star^- -\gamma^-
\right].
$$

因此：

$$
\mathcal M_{\min}\geq0
$$

表示在整個誤差域內必然全食；

$$
\mathcal M_{\max}<0
$$

表示在整個誤差域內不可能全食；

$$
\mathcal M_{\min}<0<\mathcal M_{\max}
$$

則表示分類取決於軌道狀態、測量誤差或觀測位置。

## 10.2 一階誤差傳播

對：

$$
\alpha=\arcsin\left(\frac Rd\right),
$$

有：

$$
\frac{\partial\alpha}{\partial R}
=
\frac{1}{\sqrt{d^2-R^2}},
$$

$$
\frac{\partial\alpha}{\partial d}
=
-\frac{R}{d\sqrt{d^2-R^2}}.
$$

若 $R$ 與 $d$ 的誤差近似獨立：

$$
\sigma_\alpha^2
\approx
\frac{\sigma_R^2}{d^2-R^2}
+
\frac{R^2\sigma_d^2}{d^2(d^2-R^2)}.
$$

令：

$$
\mathcal M
=
\alpha_m-\alpha_\star-\gamma,
$$

其完整一階協方差傳播為：

$$
\sigma_{\mathcal M}^2
=
\mathbf J\boldsymbol\Sigma\mathbf J^{\mathsf T},
$$

其中：

$$
\mathbf J
=
\nabla_{\Theta}
\left(\alpha_m-\alpha_\star-\gamma\right).
$$

若總誤差可近似為高斯分布，則根據測量資料判定全食成立的概率可寫成：

$$
P(\mathrm{total}\mid\mathrm{data})
\approx
\Phi\left(
\frac{\widehat{\mathcal M}}{\sigma_{\mathcal M}}
\right),
$$

其中 $\Phi$ 是標準常態累積分布函數。

## 10.3 不可混合的誤差來源

下列不確定性不應全部粗暴視為同一高斯測量誤差：

- 儀器測量誤差；
- 軌道週期性變動；
- 軌道長期歲差；
- 天體非球形與表面山谷；
- 恆星半徑定義差異；
- 恆星臨邊昏暗；
- 大氣折射與散射；
- 多星系統其他光源；
- 模型結構錯誤；
- 系外衛星樣本選擇偏差。

其中後四類尤其屬系統誤差或模型不確定性，不能只靠增加小數位數消除。

---

# 十一、概率的分層定義

「日全食的概率」沒有單一數值，除非先明確指定抽樣空間。

## 11.1 隨機時刻、隨機天空方向

令：

$$
\delta
=
\alpha_m-\alpha_\star.
$$

若遮蔽物中心方向在整個天球上均勻分布，完整遮蔽的瞬時概率為：

$$
P_{\mathrm{inst,total}}
=
H(\delta)
\frac{1-\cos\delta}{2},
$$

其中：

$$
H(\delta)
=
\begin{cases}
1,&\delta\geq0,\\
0,&\delta<0.
\end{cases}
$$

小角度下：

$$
P_{\mathrm{inst,total}}
\approx
H(\delta)\frac{\delta^2}{4}.
$$

任意程度遮蔽的瞬時概率則為：

$$
P_{\mathrm{inst,any}}
=
\frac{1-\cos(\alpha_m+\alpha_\star)}{2}.
$$

這不是實際軌道系統的日食頻率，而是各向同性隨機方向基準。

## 11.2 每次合日的方向概率

若軌道法向在母體中各向同性，對近圓軌道的簡化模型：

$$
P_{\mathrm{conj,total}}
=
H(\delta)\sin\delta.
$$

小角度下：

$$
P_{\mathrm{conj,total}}
\approx
H(\delta)(\alpha_m-\alpha_\star).
$$

任意食的方向概率為：

$$
P_{\mathrm{conj,any}}
=
\sin(\alpha_m+\alpha_\star).
$$

## 11.3 指定時間窗內至少一次

衛星軌道週期為：

$$
P_m
=
2\pi
\sqrt{
\frac{a_m^3}{G(M_p+M_m)}
}.
$$

行星軌道週期為：

$$
P_p
=
2\pi
\sqrt{
\frac{a_p^3}{G(M_\star+M_p)}
}.
$$

順行衛星的合日週期近似為：

$$
\frac1{P_{\mathrm{syn}}}
=
\left|
\frac1{P_m}-\frac1{P_p}
\right|.
$$

在時間 $T$ 中，合日次數近似為：

$$
N\approx\frac{T}{P_{\mathrm{syn}}}.
$$

若每次事件可近似獨立，且單次成功概率為 $p$ ：

$$
P_{\geq1}(T)
=
1-(1-p)^N.
$$

真實食季通常具有強烈週期相關，故此式只適合作為獨立事件基準。

## 11.4 多衛星系統

若一顆行星有 $n$ 顆候選衛星，且各衛星事件可近似獨立：

$$
P_{\mathrm{system}}
=
1-
\prod_{j=1}^{n}(1-p_j).
$$

若事件共享軌道平面、共振或共同前置條件，則必須加入聯合分布或使用多體蒙地卡羅模擬。

## 11.5 隨機時間與隨機地表位置

令 $A_{\mathrm{total}}(t)$ 為時刻 $t$ 行星表面的全食區面積。則：

$$
P_{\mathrm{surface,time}}
=
\frac1T
\int_0^T
\frac{A_{\mathrm{total}}(t)}{4\pi R_p^2}
\,dt.
$$

這才是「隨機抽一個時間，再隨機抽一個行星表面地點，正好處於全食」的嚴格定義。

## 11.6 宇宙母體概率

設宇宙中星體系統參數的母體分布為 $p(\Theta)$ ，完整遮蔽事件指示函數為：

$$
\mathbf 1_{\mathrm{TSE}}(\Theta)
=
\begin{cases}
1,&\Theta\in\mathcal D_{\mathrm{TSE}},\\
0,&\Theta\notin\mathcal D_{\mathrm{TSE}}.
\end{cases}
$$

則宇宙母體概率形式上為：

$$
\boxed{
P_{\mathrm{cosmic,TSE}}
=
\int
\mathbf 1_{\mathrm{TSE}}(\Theta)
p(\Theta)\,d\Theta
}.
$$

公式本身並不困難；困難在於 $p(\Theta)$ 的多個關鍵部分仍未知，尤其是：

- 行星擁有衛星的母體比例；
- 衛星數量分布；
- 衛星半徑與質量分布；
- 衛星軌道半長軸與傾角分布；
- 系外衛星的探測偏差；
- 多星系統與環系的占比；
- 哪些天體被視為可定義「觀測者位置」的行星。

因此，目前不能從觀測資料直接給出唯一可信的宇宙數值。

---

# 十二、地球—月球—太陽的數值示例

## 12.1 採用的粗略參數

本文使用：

$$
R_\odot=695700\ \mathrm{km},
$$

$$
1\ \mathrm{AU}=149597870.7\ \mathrm{km},
$$

$$
R_m=1737.4\ \mathrm{km},
$$

以及月球平均近地點、遠地點尺度約：

$$
d_{m,\mathrm{geo,min}}\approx363300\ \mathrm{km},
$$

$$
d_{m,\mathrm{geo,max}}\approx405500\ \mathrm{km}.
$$

太陽半徑與 AU 定義取自 NASA 資料，月球半徑取自 JPL 衛星物理參數，月地距離變化取自 NASA 月球資料。[4][5][6]

若觀測者位於地球表面且接近月下點，使用地球平均半徑 $R_\oplus\approx6371\ \mathrm{km}$ ，則觀測者到月球中心距離近似為：

$$
d_m\approx d_{m,\mathrm{geo}}-R_\oplus.
$$

地球軌道離心率取近似值 $e_\oplus\approx0.0167$ ，故日地距離粗略範圍為：

$$
d_{\odot,\min}\approx\mathrm{AU}(1-e_\oplus),
$$

$$
d_{\odot,\max}\approx\mathrm{AU}(1+e_\oplus).
$$

## 12.2 月球與太陽角半徑範圍

代入：

$$
\alpha_m
=
\arcsin\left(\frac{R_m}{d_m}\right),
$$

得到約：

$$
14.96'
\lesssim
\alpha_m
\lesssim
16.73'.
$$

太陽角半徑約為：

$$
15.72'
\lesssim
\alpha_\odot
\lesssim
16.26'.
$$

因此角半徑比約跨越：

$$
\boxed{
0.920
\lesssim q\lesssim
1.064
}.
$$

這說明地球系統並不是固定滿足 $q=1$ ，而是隨軌道狀態跨越：

$$
q<1,
\qquad
q=1,
\qquad
q>1.
$$

所以同一套太陽—地球—月球系統既能產生日環食，也能產生日全食與混合食。

上述結果是以平均距離尺度和球形近似得到的粗略值；高精度日食預報須使用 JPL Horizons、月面地形、地球橢球、觀測者經緯度與精密時標。

---

# 十三、地球日食的經驗頻率

NASA 五千年日食目錄統計公元前 $1999$ 年至公元 $3000$ 年，共有：

$$
11898
$$

次日食，其中：

$$
4200
$$

次偏食、

$$
3956
$$

次環食、

$$
3173
$$

次全食，以及：

$$
569
$$

次混合食。[7]

## 13.1 朔月數量

取一回歸年：

$$
Y=365.2422\ \mathrm{days},
$$

朔望月：

$$
P_{\mathrm{synodic}}=29.5305889\ \mathrm{days}.
$$

五千年朔月數近似為：

$$
N_{\mathrm{new\ moon}}
\approx
\frac{5000\times365.2422}{29.5305889}
\approx61841.33.
$$

## 13.2 每次朔月在地球某處產生日食

$$
P_{\mathrm{Earth,any}}
\approx
\frac{11898}{61841.33}
\approx0.1924.
$$

即：

$$
\boxed{P_{\mathrm{Earth,any}}\approx19.24\%}.
$$

## 13.3 每次朔月形成純日全食

$$
P_{\mathrm{Earth,total}}
\approx
\frac{3173}{61841.33}
\approx0.05131.
$$

即：

$$
\boxed{P_{\mathrm{Earth,total}}\approx5.13\%}.
$$

## 13.4 將混合食的全食段一併計入

$$
P_{\mathrm{Earth,total+hybrid}}
\approx
\frac{3173+569}{61841.33}
\approx0.06051.
$$

即：

$$
\boxed{P_{\mathrm{Earth,total+hybrid}}\approx6.05\%}.
$$

這些數值的正確解讀是：

> 每次朔月約有 $6\%$ 的經驗頻率，會在地球某個狹窄區域產生日全食，或產生包含全食段的混合食。

它不等於某一固定地點看見全食的概率。

## 13.5 固定地點重現期

NASA 以五千年全食路徑熱圖估算，地球表面一個位置兩次日全食之間的全球平均間隔約為：

$$
366\ \mathrm{years}.
$$

2026 年的一項新計算則得到：

$$
373\pm7\ \mathrm{years}.
$$

兩者定義與計算方法並不完全相同，但皆說明固定地點的日全食遠比全球日全食事件稀少。[8][9]

若僅作 Poisson 粗略基準，取平均間隔 $373$ 年，則一年內至少一次的概率為：

$$
P_{1\mathrm{yr}}
=1-e^{-1/373}
\approx0.00268,
$$

即約：

$$
\boxed{0.268\%}.
$$

八十年內至少一次的粗略值：

$$
P_{80}
=1-e^{-80/373}
\approx0.193,
$$

即約：

$$
\boxed{19.3\%}.
$$

但真實日食路徑不是無記憶 Poisson 過程，故這兩個結果只能當直觀基準。

---

# 十四、太陽系內的類日全食能力

## 14.1 粗略分類

以八大行星為樣本，並將巨行星的「觀測者位置」定義為雲頂或指定大氣壓力層，可作如下粗略判定：

| 行星 | 是否有天然衛星 | 是否存在可完整遮住太陽盤的主要衛星 | 說明 |
|---|---:|---:|---|
| 水星 | 否 | 否 | 無天然衛星 |
| 金星 | 否 | 否 | 無天然衛星 |
| 地球 | 是 | 是 | 月球在部分軌道狀態下可形成全食 |
| 火星 | 是 | 否 | 火衛一角尺寸通常不足以完整覆蓋太陽 |
| 木星 | 是 | 是 | 多顆大型衛星的視尺寸遠大於當地太陽 |
| 土星 | 是 | 是 | 多顆主要衛星具備完整遮蔽能力 |
| 天王星 | 是 | 是 | 多顆主要衛星具備完整遮蔽能力 |
| 海王星 | 是 | 是 | 海衛一等可完整遮蔽太陽 |

JPL 的主要衛星半徑與平均軌道元素支持此項粗略分類；NASA 亦指出其他行星的衛星可以產生日食，但其尺寸比例通常不像地球所見的近似匹配。[12][13][14]

## 14.2 代表性角尺寸比

使用平均軌道尺度與行星雲頂／表面近似距離，可得到下列示例：

| 系統 | 代表遮蔽物 | 粗略 $q=\alpha_m/\alpha_\star$ |
|---|---|---:|
| 火星 | 火衛一 | $0.61$ |
| 地球 | 月球 | $0.92$ 至 $1.06$ |
| 木星 | 木衛一 | $5.79$ |
| 土星 | 土衛一 | $3.20$ |
| 天王星 | 天衛五 | $9.33$ |
| 海王星 | 海衛一 | $26.5$ |

這組數字的意義不是給出精密預報，而是顯示：

- 地球月球位於接近 $q=1$ 的狹窄臨界區；
- 巨行星的許多衛星會大幅超過太陽視盤；
- 「完整遮住恆星」可能不罕見；
- 「剛好只比恆星視盤略大」才是較特殊的條件。

## 14.3 太陽系小樣本比例

若將上述五顆行星判為具備完整遮蔽能力：

$$
\widehat p_{\mathrm{SS}}
=\frac58
=0.625.
$$

即：

$$
\boxed{62.5\%}.
$$

但八大行星並非八個獨立、同分布的宇宙樣本，而是同一原行星盤中的相關樣本。因此， $62.5\%$ 不能直接外推為宇宙發生率。

若只把它當成二項式小樣本，採 Jeffreys 先驗：

$$
p\mid k,n
\sim
\operatorname{Beta}
\left(
k+\frac12,
n-k+\frac12
\right),
$$

代入：

$$
k=5,
\qquad n=8,
$$

得到後驗平均：

$$
E[p\mid k,n]
=\frac{5.5}{9}
\approx0.611,
$$

而約 $95\%$ 貝葉斯可信區間為：

$$
\boxed{0.295\lesssim p\lesssim0.881}.
$$

這只反映小樣本抽樣不確定性，完全沒有包含太陽系非代表性的系統誤差。

---

# 十五、宇宙概率的啟發式代理模型

## 15.1 系外衛星發生率限制

HEK VI 研究分析 $284$ 顆約位於 $0.1$ 至 $1.0\ \mathrm{AU}$ 的暖行星候選體，對伽利略衛星類比系統給出：

$$
\eta
=0.16_{-0.10}^{+0.13}
$$

的 $68.3\%$ 區間，並給出：

$$
\eta<0.38
$$

的 $95\%$ 上限。論文本身強調，樣本中的弱偏好不應被當成可靠系外衛星檢出。[15]

此數值描述的是特定樣本、特定檢出模型中的伽利略型衛星系統發生率，而不是全部衛星、全部行星、全部恆星或全部遮蔽物的宇宙發生率。

## 15.2 完整遮蔽能力的混合代理

若僅為建立透明的啟發式模型，可寫成：

$$
P_{\mathrm{capable}}
\approx
P(\text{伽利略型衛星系})
\times
P(\text{至少一衛星可全遮蔽}\mid\text{衛星系}).
$$

太陽系六顆具有天然衛星的八大行星中，粗略有五顆具備全遮蔽能力。若使用 Jeffreys 後驗平均：

$$
P(\text{可全遮蔽}\mid\text{有衛星})
\approx
\frac{5+1/2}{6+1}
\approx0.786.
$$

再使用 HEK VI 的中央值：

$$
P_{\mathrm{capable}}
\approx0.16\times0.786
\approx0.126.
$$

即：

$$
\boxed{P_{\mathrm{capable}}\sim13\%}.
$$

若將系外衛星發生率取 $0.06$ 至 $0.38$ ，並將上述 Jeffreys 區間 $0.442$ 至 $0.981$ 作極寬包絡：

$$
0.06\times0.442
\approx0.027,
$$

$$
0.38\times0.981
\approx0.373.
$$

得到：

$$
\boxed{2.7\%\text{--}37.3\%}.
$$

必須再次強調：

> 這不是正式的宇宙置信區間，而是兩個高度不完全、定義不同的代理來源相乘後形成的模型包絡。

其價值在於提出可被替換的計算框架，而不是宣稱宇宙中恰有 $13\%$ 的行星能看見日全食。

## 15.3 類地球近匹配的基準模型

再建立一個明示假設的基準模型：

1. 一個衛星系有 $N=4$ 顆主要衛星；
2. 每顆衛星的角尺寸比滿足：

$$
q\sim\operatorname{LogUniform}(10^{-2},10^2);
$$

3. 將近似地球式全食定義為：

$$
1\leq q\leq1.1.
$$

單顆衛星落入此區間的概率為：

$$
p_{\mathrm{near}}
=
\frac{\ln(1.1)}{\ln(10^2/10^{-2})}
\approx0.01035.
$$

四顆衛星至少一顆符合：

$$
P_{\mathrm{near,system}}
=
1-(1-p_{\mathrm{near}})^4
\approx0.04076.
$$

乘上 $\eta=0.16$ ：

$$
P_{\mathrm{cosmic,near}}
\approx0.16\times0.04076
\approx0.00652.
$$

即：

$$
\boxed{P_{\mathrm{cosmic,near}}\approx0.65\%}.
$$

若 $\eta$ 取 $0.06$ 至 $0.38$ ：

$$
\boxed{0.24\%\text{--}1.55\%}.
$$

這些值高度依賴 $q$ 的假定分布與範圍。若角尺寸比不是對數均勻、衛星數量不是四顆，或衛星半徑與軌道半徑具有形成機制相關性，結果都會明顯改變。

## 15.4 對匹配容許度的敏感性

在同一基準模型下：

| 容許度 $\varepsilon$ | 單顆衛星匹配率 | 四顆至少一顆 | 乘以 $\eta=0.16$ |
|---:|---:|---:|---:|
| $1\%$ | $0.108\%$ | $0.431\%$ | $0.069\%$ |
| $5\%$ | $0.530\%$ | $2.102\%$ | $0.336\%$ |
| $10\%$ | $1.035\%$ | $4.076\%$ | $0.652\%$ |
| $20\%$ | $1.980\%$ | $7.686\%$ | $1.230\%$ |

這說明「類似日全食」的概率不能脫離相似度閾值。把 $q=1$ 改成 $q\in[1,1+\varepsilon]$ 後，概率才成為可測與可比較的量。

---

# 十六、暫定結論

在目前資料與模型下，可以區分三個層級的回答。

## 16.1 任意完整遮蔽能力

使用系外衛星限制與太陽系小樣本建立的混合代理模型：

$$
\boxed{
P_{\text{行星系具備某種全遮蔽能力}}
\sim10\%\ \text{量級}
}.
$$

非常寬的啟發式包絡約為：

$$
\boxed{3\%\text{--}37\%}.
$$

此處「行星系」與「遮蔽能力」的定義仍需在正式研究中精確限定。

## 16.2 接近地球式的近匹配

在本文對數均勻角尺寸比、四顆主要衛星與 $10\%$ 容許度的假設下：

$$
\boxed{P\approx0.65\%},
$$

代理範圍約：

$$
\boxed{0.24\%\text{--}1.55\%}.
$$

這不是觀測結論，而是用來展示研究方法的基準情境。

## 16.3 精確等視大小

若 $q$ 服從連續分布：

$$
\boxed{P(q=1)=0}.
$$

但物理日全食不需要精確等視大小，只需要：

$$
q\geq1
$$

以及：

$$
\gamma\leq\alpha_m-\alpha_\star.
$$

所以，真正可能特殊的不是「某物體可以遮住恆星」，而是：

$$
q\approx1.
$$

換言之，遮蔽物沒有小到留下明亮光環，也沒有大到遠超發光盤，而是剛好只比發光盤略大，使外層稀薄結構能被凸顯。

---

# 十七、研究啟發

## 17.1 從事件分類轉向參數空間

傳統科普常把日全食、日環食與日偏食視為三種事件。形式化後，它們更適合被看成同一連續參數空間中的不同區域：

$$
(\alpha_m,\alpha_\star,\gamma)
\longmapsto
\{\text{無食、偏食、環食、全食}\}.
$$

分類邊界是：

$$
\gamma=\alpha_m+\alpha_\star,
$$

以及：

$$
\gamma=|\alpha_m-\alpha_\star|.
$$

地球日全食不是孤立奇蹟，而是軌道動力學使系統狀態軌跡反覆穿越這些邊界。

## 17.2 從「是否全食」轉向「全食品質」

未來研究可建立多維品質函數：

$$
Q_{\mathrm{eclipse}}
=
Q
\left(
q,
T_{\mathrm{total}},
\mathcal D,
A_{\mathrm{path}},
F_{\mathrm{corona}},
F_{\mathrm{scatter}},
\lambda,
\ldots
\right).
$$

其中可納入：

- 視大小匹配程度；
- 全食持續時間；
- 光度下降比例；
- 全食帶面積；
- 外層大氣或日冕可見性；
- 行星大氣散射；
- 觀測波段；
- 多發光源殘餘光。

這比只問「有沒有全食」更能比較不同世界的遮蔽現象。

## 17.3 對系外行星觀測的反向應用

對遠方觀測者而言，本文的幾何可以反向應用至：

- 系外行星凌日；
- 系外衛星凌日與凌日時序變化；
- 次食與掩星；
- 雙星食；
- 環系遮蔽；
- 不規則塵埃或巨型結構造成的非典型光變。

換句話說，「行星表面的觀測者看見日全食」與「遠方望遠鏡看見某系統的凌日光變」是同一投影幾何在不同觀測位置下的轉換。

## 17.4 可計算宇宙學式的研究流程

未來可建立下列生成模型：

$$
\text{恆星母體}
\rightarrow
\text{行星母體}
\rightarrow
\text{衛星形成}
\rightarrow
\text{長期軌道穩定}
\rightarrow
\text{觀測幾何}
\rightarrow
\text{遮蔽事件與品質分布}.
$$

再使用階層貝葉斯模型：

$$
p(\Theta,\Lambda\mid\mathcal D)
\propto
p(\mathcal D\mid\Theta)
\,p(\Theta\mid\Lambda)
\,p(\Lambda),
$$

其中 $\Lambda$ 是星體形成與衛星人口統計的超參數， $\mathcal D$ 是凌日、時序與直接成像資料。

---

# 十八、AI 半自主完成本研究的意義

## 18.1 本次工作由誰完成？

本研究並非 AI 在沒有任何人類輸入下自行選題。研究問題、整合方向、文章定位與「需說明 AI 研究意義」等要求由 Neo.K 提出。

在此基礎上，GPT-5.6 Sol 於 Chat 模式高推理配置中，半自主完成了：

1. 從日全食科普問題轉向一般遮蔽現象；
2. 建立投影集合與光通量定義；
3. 推導球形天體的角半徑、中心角距離與分類條件；
4. 整理圓盤重疊、本影、反本影與持續時間公式；
5. 加入 Hill 半徑、Roche 極限與橢圓軌道限制；
6. 建立區間誤差、協方差傳播與分類概率；
7. 區分多種互不等價的「日全食概率」；
8. 搜尋並核對 NASA、JPL 與系外衛星論文資料；
9. 完成地球數值示例、五千年經驗頻率與小樣本估計；
10. 主動指出宇宙概率不可直接從現有觀測中精確決定；
11. 建立可替換假設的代理模型與敏感性表；
12. 將全部內容重新組織成可供人類審查的 Markdown 初稿。

因此，較準確的描述不是「AI 完全自主完成一篇成熟天文學論文」，而是：

> **在人類提出研究問題與高階方向後，AI 半自主完成了一次基本研究循環：概念重構、形式化、檢索、估算、自我限制與論文化。**

## 18.2 為何仍有意義？

其意義不在於宣稱 AI 已取代專業天文學家，而在於它把過去需要多次人工切換的工作，壓縮成一個連續研究流程：

$$
\text{自然語言問題}
\rightarrow
\text{定義}
\rightarrow
\text{方程}
\rightarrow
\text{資料}
\rightarrow
\text{數值}
\rightarrow
\text{誤差}
\rightarrow
\text{限制}
\rightarrow
\text{論文初稿}.
$$

即使結果仍不夠專業、完整或可直接投稿，它仍能提供：

- 可被專業人士快速審查的研究骨架；
- 可直接轉成模擬程式的變數與公式；
- 可明確指出未知母體分布的位置；
- 可供後續 Agent 自動更新的資料接口；
- 可供跨領域研究者快速進入問題的數學地圖；
- 一組可以被否證、重算與替換的假設，而不只是模糊直覺。

## 18.3 本文不能證明什麼？

本文不能證明：

- 宇宙中恰有 $13\%$ 的行星具備日全食；
- 近地球式日全食的真實概率就是 $0.65\%$ ；
- 系外衛星人口統計已被可靠測量；
- 太陽系八大行星可視為獨立宇宙樣本；
- 對數均勻的 $q$ 分布具有物理真實性；
- 簡化球形與二體軌道模型足以預測任意系統；
- AI 產出的公式組合已經過專業同行逐式驗證。

因此，本文的定位是：

$$
\boxed{
\text{啟發式研究骨架}
\neq
\text{已完成的專業實證論文}
}.
$$

## 18.4 AI 研究能力的較合理評價

這次成果顯示，Chat 模式中的高推理生成式 AI 已能在有限人類提示下形成具有一定完整度的研究初稿。其能力至少包含：

- 跨科普與形式化語言轉換；
- 多層抽樣空間辨識；
- 數學模型快速組裝；
- 公開資料核對；
- 粗略數值估算；
- 誤差與限制揭露；
- 研究結構自動生成。

但「高超能力」不應被理解成無條件正確。AI 的高能力恰恰必須與：

$$
\text{可追溯來源}
+
\text{明示假設}
+
\text{可重算公式}
+
\text{不確定性聲明}
$$

共同出現，才具有研究意義。

---

# 十九、主要限制與後續工作

## 19.1 觀測限制

截至本文版本，系外衛星的整體發生率、尺寸與軌道分布仍缺乏足夠可靠的觀測約束。HEK VI 的結果只能作特定衛星系統的限制，不能代表所有系外衛星。[15]

## 19.2 樣本限制

太陽系行星共享形成歷史，不符合簡單的獨立同分布假設。本文的 $5/8$ 與 $5/6$ 只能作教學性或啟發式代理。

## 19.3 幾何限制

本文大部分公式採球形天體、瞬時直線光線與小角度近似。高精度模型需加入：

- 非球形天體；
- 月面或衛星表面地形；
- 行星橢球；
- 廣義相對論光偏折；
- 大氣折射；
- 波長依賴吸收；
- 光源活動與星斑；
- 多體引力積分。

## 19.4 概率限制

宇宙概率至少需要事先選定：

- 以恆星、行星、宜居行星或有衛星行星為抽樣單位；
- 是否要求固體表面；
- 是否允許巨行星大氣觀測者；
- 是否計入行星、環與人工結構遮蔽；
- 事件時間窗；
- 匹配容許度 $\varepsilon$ ；
- 最低遮光比例 $\mathcal D$ ；
- 最短全食時間；
- 最低可見日冕範圍。

不設定這些條件，就不存在單一「實際概率」。

## 19.5 建議後續實作

下一版可建立 Python 或 Rust 蒙地卡羅模擬器，流程如下：

1. 生成恆星質量與半徑；
2. 生成行星軌道與半徑；
3. 依衛星形成模型生成衛星數量、尺寸與軌道；
4. 刪除 Roche 極限內與 Hill 穩定界外的衛星；
5. 積分軌道方向與歲差；
6. 對行星表面或大氣層採樣觀測者；
7. 計算 $\alpha_m$ 、 $\alpha_\star$ 、 $\gamma$ 與 $\mathcal M$ ；
8. 記錄全食、環食、偏食與無食；
9. 統計不同 $\varepsilon$ 、時間窗與天體類型下的概率；
10. 對母體超參數做敏感性分析與貝葉斯更新。

最終輸出不應只有單一百分比，而應是：

$$
P_{\mathrm{TSE}}
=
P_{\mathrm{TSE}}
\left(
\varepsilon,
T,
\tau,
\text{planet class},
\text{star class},
\text{moon model}
\right).
$$

---

# 二十、結語

日全食不是單純的「白天變黑」，而是尺寸、距離、軌道、方向、時間、觀測位置與光度結構共同構成的臨界遮蔽事件。

從一般形式看，完整遮蔽只需要：

$$
\Pi_O(S,t)
\subseteq
\Pi_O(M,t).
$$

從球形幾何看，則需要：

$$
\alpha_m\geq\alpha_\star,
$$

以及：

$$
\gamma\leq\alpha_m-\alpha_\star.
$$

地球的特殊之處不是宇宙中只有月球能遮住恆星，而是太陽與月球在當前時代的角尺寸接近：

$$
q\approx1.
$$

這使月球能遮住壓倒性明亮的光球盤，卻沒有把太陽外圍結構遮得過遠。遮蔽因此不只是消除可見物，也成為揭露不可見物的條件。

本文尚未完成真正的宇宙日全食人口統計，但已建立一套基本研究語言：

$$
\text{投影集合}
+
\text{角尺寸}
+
\text{軌道可行域}
+
\text{誤差域}
+
\text{分層概率}
+
\text{可替換母體模型}.
$$

它同時展示一種新的研究現實：人類可以提出問題、界定價值與決定研究方向；AI 則能在同一輪對話中，半自主地將問題展開為定義、方程、資料、估算、限制與論文初稿。

這尚不是完整的自主科學，也不是專業研究的終點；但它已經不只是問答。

它是一個基本研究循環的雛形。

---

# 附錄 A：核心判定式速查

## A.1 角半徑

$$
\alpha
=
\arcsin\left(\frac Rd\right)
\approx\frac Rd.
$$

## A.2 中心角距離

$$
\gamma
=
\arccos
\left(
\hat{\mathbf u}_\star\cdot\hat{\mathbf u}_m
\right).
$$

## A.3 全食

$$
\alpha_m\geq\alpha_\star,
\qquad
\gamma\leq\alpha_m-\alpha_\star.
$$

## A.4 環食

$$
\alpha_m<\alpha_\star,
\qquad
\gamma\leq\alpha_\star-\alpha_m.
$$

## A.5 偏食

$$
|\alpha_m-\alpha_\star|
<\gamma<
\alpha_m+\alpha_\star.
$$

## A.6 全食裕度

$$
\mathcal M
=
\alpha_m-\alpha_\star-\gamma.
$$

## A.7 角尺寸比

$$
q
=
\frac{\alpha_m}{\alpha_\star}
\approx
\frac{R_md_\star}{R_\star d_m}.
$$

## A.8 本影長度

$$
L_u
=
\frac{R_mD}{R_\star-R_m}.
$$

## A.9 Hill 半徑

$$
R_H
=
a_p(1-e_p)
\left(\frac{M_p}{3M_\star}\right)^{1/3}.
$$

## A.10 Roche 極限

$$
R_{\mathrm{Roche}}
\approx
2.44R_p
\left(\frac{\rho_p}{\rho_m}\right)^{1/3}.
$$

## A.11 宇宙母體概率

$$
P_{\mathrm{cosmic,TSE}}
=
\int
\mathbf 1_{\mathrm{TSE}}(\Theta)
p(\Theta)\,d\Theta.
$$

---

# 附錄 B：數據層級標記

| 層級 | 含義 | 本文例子 |
|---|---|---|
| A | 官方或原始資料直接給出 | NASA 五千年日食數、JPL 月球半徑 |
| B | 由 A 級資料代入公式所得 | 月球與太陽角半徑範圍、每朔月經驗頻率 |
| C | 小樣本統計推論 | 太陽系 $5/8$ 、Jeffreys 區間 |
| D | 明示假設的啟發式代理模型 | 宇宙全遮蔽能力約 $13\%$ 、近匹配約 $0.65\%$ |
| E | 尚待觀測或模擬驗證的研究命題 | 真實 $f_q(q)$ 、各類恆星的日全食品質分布 |

本文所有「宇宙概率」均屬 C 至 D 級，不得與 A 級觀測資料等同。

---

# 參考資料

[1] NASA Science, **Why Do Eclipses Happen?**  
https://science.nasa.gov/eclipses/geometry/

[2] NASA Science, **Total Solar Eclipse FAQ**  
https://science.nasa.gov/eclipses/future-eclipses/eclipse-2024/faq/

[3] NASA Science, **Eclipse Safety**  
https://science.nasa.gov/eclipses/safety/

[4] NASA Science, **Universe Glossary**：AU 與太陽半徑定義。  
https://science.nasa.gov/universe/glossary/

[5] JPL Solar System Dynamics, **Planetary Satellite Physical Parameters**：月球及主要衛星半徑。  
https://ssd.jpl.nasa.gov/sats/phys_par/sep.html

[6] NASA Science, **Supermoons**：月球近地點與遠地點平均距離尺度。  
https://science.nasa.gov/moon/supermoons/

[7] Fred Espenak / NASA GSFC, **Five Millennium Catalog of Solar Eclipses: -1999 to +3000**。  
https://eclipse.gsfc.nasa.gov/SEcat5/SEcatalog.html

[8] NASA Scientific Visualization Studio, **5000 Years of Total Solar Eclipses**：固定地點平均間隔約 $366$ 年。  
https://svs.gsfc.nasa.gov/5222

[9] Jones, G. et al. (2026), **The Frequency of Solar Eclipses for a Given Place: A New Approach to a Classic Question**。  
https://arxiv.org/abs/2602.04797

[10] Domingos, R. C., Winter, O. C., & Yokoyama, T. (2006), **Stable satellites around extrasolar giant planets**, *Monthly Notices of the Royal Astronomical Society*, 373(3), 1227–1234。  
https://academic.oup.com/mnras/article/373/3/1227/1063626

[11] Rosario-Franco, M. et al. (2020), **Orbital Stability of Exomoons and Submoons with Applications to Kepler 1625b-I**。  
https://arxiv.org/abs/2005.06521

[12] JPL Solar System Dynamics, **Planetary Satellite Mean Elements**。  
https://ssd.jpl.nasa.gov/sats/elem/sep.html

[13] JPL Solar System Dynamics, **Planetary Physical Parameters**。  
https://ssd.jpl.nasa.gov/planets/phys_par.html

[14] NASA, **Eclipses Near and Far**。  
https://www.nasa.gov/history/eclipses-near-and-far/

[15] Teachey, A., Kipping, D. M., & Schmitt, A. R. (2017), **HEK VI: On the Dearth of Galilean Analogs in Kepler and the Exomoon Candidate Kepler-1625b I**。  
https://arxiv.org/abs/1707.08563

---

## 引用與使用建議

本文件適合被引用為 AI 半自主啟發式研究初稿，但引用時應保留以下限定：

1. 未經同儕審查；
2. 宇宙概率為代理模型而非觀測定值；
3. 數值以公開平均參數與簡化幾何粗略計算；
4. 正式研究需使用精密星曆、多體積分、完整選擇函數與系外衛星人口統計模型；
5. AI 為主要初稿撰寫與形式化工具，人類提出研究問題並決定研究定位。
