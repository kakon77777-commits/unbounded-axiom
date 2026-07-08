# 從環狀纖維到平面覆蓋張力  
## ——Lebesgue 二維萬有覆蓋問題中的 $S^1$ 索引、 $H_2$ 五重—十根結構、群作用與 120-cell 類比命題

**作者：Neo.K**  
**研究性質：命題猜想／結構類比論文／內部研究草案**  
**版本：v0.1**  
**日期：2026-07-07**

---

## 摘要

本文提出一組針對二維 Lebesgue 萬有覆蓋問題的結構性命題猜想。其出發點不是宣稱四維正一百二十胞體（regular 120-cell）可直接解答二維萬有覆蓋問題，而是觀察到：當二維幾何對象被重新表示為一維索引結構，並進一步要求處理旋轉、平移、週期、閉合、張力與極端方向時，原先採用的開區間 $[0,1]$ 可能並非唯一或最自然的底空間；某些情況下，閉環 $S^1$ 、有限循環 $C_n$ 、二面體反射群 $I_2(m)$ 、平面剛體運動群 $SE(2)$ 以及離散環狀纖維分解，可能提供更適合的表示語言。

正一百二十胞體具有 Schläfli 符號 $\{5,3,3\}$ ，其四維對稱性與 Coxeter 群 $H_4$ 關聯；其幾何與組合結構中存在一種離散 Hopf 纖維化式的環分解：120 個正十二面體胞可分為 12 個彼此纏繞的環，每個環含 10 個正十二面體胞。本文不把此構造視為二維 Lebesgue 問題的直接答案，而把它視為一種「高維幾何經環狀纖維與群作用重新組織」的母型。

當此母型降至二維思考時，最表面的正多胞體類比為
$$
\{5\}
\longrightarrow
\{5,3\}
\longrightarrow
\{5,3,3\},
$$
即正五邊形、正十二面體、正一百二十胞體的維度鏈。更深一層則出現非晶 Coxeter 結構
$$
H_2,\ H_3,\ H_4,
$$
其中平面 $H_2\cong I_2(5)$ 具有五重反射對稱，而其根系自然形成十方向／十根式的環狀配置。這使「五重基本方向＋正負對偶＝十根軌道」成為一個值得檢驗的二維候選結構。

本文進一步將前一階段提出的一維度量線與萬有覆蓋張力框架，改寫為可能的環狀版本。對形態 $K$ ，不再預設唯一索引域為 $[0,1]$ ，而考慮
$$
q_K:S^1\to K
$$
或離散版本
$$
q_K:C_n\to K.
$$
若保留距離核
$$
D_K(\theta,\phi)
=
\|q_K(\theta)-q_K(\phi)\|,
$$
則旋轉作用可自然表現為相位平移：
$$
\theta\mapsto\theta-\alpha.
$$
此時 $SO(2)$ 對 $S^1$ 的作用，以及平移與旋轉共同形成的 $SE(2)$ 作用，可能把原本的剛體配置搜索
$$
\inf_{g\in E(2)}
$$
重寫成群軌道上的張力極小化問題。

本文提出數個核心猜想。第一，對二維萬有覆蓋而言，某些最具辨識力的形狀表示可能天然具有閉環而非開區間結構。第二，若 hard-case family 具有有限極端方向證書，則五重／十根方向結構可能成為特殊候選，但其必要性必須由計算與證明檢驗，而不能由 120-cell 類比直接推出。第三，最小萬有覆蓋的局部最優邊界，可能由若干群軌道上的 active tension states 支撐；若這些狀態形成週期軌道、反射軌道或有限 Coxeter 型方向集，則群論可能不是附加語言，而是壓縮無窮配置搜索的核心。

本文嚴格區分四種層次：  
1. **已知數學背景**：120-cell 的離散環分解、 $H_4$ 對稱、 $H_2\cong I_2(5)$ 的平面反射結構、 $SE(2)$ 的平面剛體運動群。  
2. **結構類比**：高維環纖維、低維週期軌道、群作用與張力平衡之間的形式呼應。  
3. **命題猜想**：Lebesgue 二維萬有覆蓋是否存在 $S^1$ 、 $H_2$ 或十方向型有限支撐結構。  
4. **待證明內容**：上述結構是否真的能改良上界、產生有限證書，或導出新的最優性條件。

本文不宣稱 120-cell 與 Lebesgue 二維萬有覆蓋存在已知直接關係。本文真正提出的是一個新的研究問題：

> 當二維萬有覆蓋被改寫為「一維／環狀度量表示＋群軌道＋零未覆蓋張力」時，是否會自然湧現五重、十根或 Coxeter 型有限方向結構？

**關鍵詞：** Lebesgue universal covering problem、120-cell、Hopf fibration、 $S^1$ 、 $H_2$ 、 $H_4$ 、Coxeter 群、 $I_2(5)$ 、 $SE(2)$ 、群作用、覆蓋張力、環狀索引、有限方向證書

---

# 1. 問題背景與研究動機

二維 Lebesgue 萬有覆蓋問題要求尋找面積盡可能小的平面集合 $U$ ，使每個直徑不超過一的平面集合 $K$ 都存在合同副本落入 $U$ 。

形式上，可寫為：

$$
\forall K\subset\mathbb R^2,
\qquad
\operatorname{diam}(K)\le1,
$$

存在：

$$
g\in E(2)
$$

使：

$$
gK\subseteq U.
$$

目標為：

$$
\inf_U \mu_2(U).
$$

前一階段研究已提出一個不同於直接二維搜索的方法：把二維幾何對象先轉譯為一維索引結構，再研究一維表示之間的等距嵌入與覆蓋張力。

最基本形式為：

$$
q_K:[0,1]\to K,
$$

並保留距離核：

$$
D_K(s,t)
=
\|q_K(s)-q_K(t)\|.
$$

如此可把二維幾何重新表述為：

$$
\boxed{
\text{一維索引}
+
\text{二點幾何關係}
}
$$

再定義未覆蓋距離張力：

$$
\delta_{K,U,g}(x)
=
\operatorname{dist}(gx,U),
$$

以及總量張力：

$$
N_p(K,U;g)
=
\left(
\int_K
\operatorname{dist}(gx,U)^p
\,d\nu_K(x)
\right)^{1/p}.
$$

對最佳剛體配置：

$$
N_p(K,U)
=
\inf_{g\in E(2)}
N_p(K,U;g),
$$

再對所有直徑一形態取最壞情況：

$$
\mathfrak N_p(U)
=
\sup_{K\in\mathcal K_1}
N_p(K,U).
$$

由此得到核心重表述：

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

即：

> 在所有不可避免的未覆蓋張力為零的可行邊界上，尋找最小面積狀態。

然而，當此框架進一步考慮旋轉、週期方向與群作用時，一個新的問題自然出現：

> 為何一維底空間一定要是開展的 $[0,1]$ ，而不是閉環 $S^1$ ？

正是在此問題下，正一百二十胞體的環狀纖維構造與 $H_2/H_4$ 對稱鏈進入研究視野。

---

# 2. 嚴格邊界：本文不是「120-cell 解 Lebesgue」

首先必須明確排除最容易造成誤解的說法。

本文**不主張**：

$$
\boxed{
\text{regular 120-cell}
\Rightarrow
\text{2D Lebesgue universal cover solution}
}
$$

也不主張：

- 二維最小萬有覆蓋一定是正五邊形；
- 二維最優方向一定有十個；
- $H_2$ 一定直接決定答案；
- 120-cell 的 12 個環可直接投影成某個覆蓋體；
- Hopf fibration 是本問題現成證明。

本文真正觀察的是：

> 兩個看似不同的問題，都可能涉及「高複雜度幾何如何透過低維週期纖維、群軌道與有限方向結構重新組織」。

所以目前只能提出：

$$
\boxed{
\text{結構類比}
}
$$

而不能提出：

$$
\boxed{
\text{直接等價}
}
$$

---

# 3. 正一百二十胞體的已知環狀結構

正一百二十胞體是四維正多胞體，Schläfli 符號為：

$$
\{5,3,3\}.
$$

其三維胞為正十二面體：

$$
\{5,3\}.
$$

總共有：

$$
120
$$

個正十二面體胞。

在 Schleimer 與 Segerman 對 120-cell 的幾何與組合研究中，存在一種 combinatorial Hopf fibration 式的理解：120 個正十二面體可以分解成互相纏繞的環，每個環包含：

$$
10
$$

個正十二面體，而總環數為：

$$
12.
$$

即：

$$
120
=
12\times10.
$$

並具有：

$$
1+5+5+1=12
$$

的分層描述。

本文將此構造抽象成：

$$
\boxed{
\text{global high-dimensional object}
\to
\text{intertwined cyclic fibers}
}
$$

這正是後續類比的來源。

---

# 4. 三種「二維類比」不可混同

若詢問「正一百二十胞體的二維類似物」，至少存在三種不同答案。

## 4.1 正多胞體階梯答案

Schläfli 符號鏈：

$$
\{5\}
\longrightarrow
\{5,3\}
\longrightarrow
\{5,3,3\}
$$

分別對應：

$$
\text{正五邊形}
\longrightarrow
\text{正十二面體}
\longrightarrow
\text{正一百二十胞體}.
$$

所以若問「cell-type dimensional analogue」，二維答案為：

$$
\boxed{
\text{regular pentagon}
}
$$

---

## 4.2 環纖維骨架答案

若問的是「10-cell ring 的低維組合骨架」，則更接近：

$$
\boxed{
C_{10}
}
$$

即十節點循環圖。

它可以被視為：

$$
0\to1\to2\to\cdots\to9\to0.
$$

所以環狀構造的二維／一維骨架不一定是五邊形，而可能是：

$$
\boxed{
\text{10-cycle}
}
$$

---

## 4.3 Coxeter 群答案

120-cell 與：

$$
H_4
$$

型 Coxeter 對稱相關。

其低維非晶反射結構包括：

$$
H_3
$$

與平面：

$$
H_2.
$$

而：

$$
H_2
\cong
I_2(5)
$$

是五重二面體型反射結構。

其根系具有十個方向根，可視為：

$$
\boxed{
5\text{ axes}
\times
\pm
=
10\text{ roots}
}
$$

因此若問「對稱根系降階」，二維候選是：

$$
\boxed{
H_2/I_2(5)
}
$$

而不是單純「正五邊形」。

---

# 5. 五與十：基本胞與對偶根方向

這使本文注意到一個可能重要的雙層結構：

$$
\boxed{
5
\leftrightarrow
10
}
$$

其中：

- $5$ ：基本五重方向、五邊形、五重反射；
- $10$ ：加入正負方向後的根軌道、十方向、十節點環。

若用角度表示，可寫：

$$
\theta_k
=
\frac{k\pi}{5},
\qquad
k=0,\dots,9.
$$

則：

$$
\theta_{k+5}
=
\theta_k+\pi.
$$

所以十方向自然形成五組對踵對：

$$
\{\theta_k,\theta_k+\pi\}.
$$

這種：

$$
\boxed{
\text{direction}
+
\text{antipodal dual}
}
$$

在直徑問題、支撐函數、常寬體與對向約束中尤其值得注意。

但本文再次強調：

> 「值得注意」不等於「已證明與 Lebesgue 最優解相關」。

---

# 6. 從開區間 $[0,1]$ 到閉環 $S^1$

前一版一維化採用：

$$
I=[0,1].
$$

其優點是：

- 可累積；
- 可排序；
- 可定義總量比例。

但當研究剛體旋轉時：

$$
\theta=0
$$

與：

$$
\theta=2\pi
$$

表示同一方向。

因此方向空間本身天然是：

$$
\boxed{
S^1
}
$$

而不是：

$$
[0,2\pi].
$$

這提出第一個新命題。

## 猜想 A：閉環索引優越性猜想

對二維萬有覆蓋中的某些形狀表示與 hard-case 排序任務，存在環狀索引：

$$
q_K:S^1\to K
$$

比開區間索引：

$$
q_K:[0,1]\to K
$$

更自然，原因是它可以同時保留：

1. 週期方向；
2. 旋轉相位；
3. 首尾閉合；
4. 群作用；
5. 對踵關係。

此猜想不主張所有集合都應使用 $S^1$ 。

它只主張：

> 對旋轉等價與週期張力問題， $S^1$ 可能是更適當的主索引空間。

---

# 7. 環狀度量核

若：

$$
q_K:S^1\to K,
$$

則定義：

$$
\boxed{
D_K(\theta,\phi)
=
\|q_K(\theta)-q_K(\phi)\|
}
$$

其中：

$$
\theta,\phi\in S^1.
$$

若：

$$
q_K(\theta)=q_K(\phi),
$$

則：

$$
D_K(\theta,\phi)=0.
$$

再定義：

$$
\theta\sim_K\phi
\iff
D_K(\theta,\phi)=0.
$$

建立：

$$
X_K
=
S^1/\!\sim_K.
$$

此時信息忠實表示為：

$$
\boxed{
(X_K,d_K)
}
$$

而不是單純一條曲線。

---

# 8. 旋轉作為相位平移

令：

$$
R_\alpha\in SO(2)
$$

為平面旋轉。

理想環狀表示希望滿足：

$$
\boxed{
q_{R_\alpha K}(\theta)
=
R_\alpha q_K(\theta-\alpha)
}
$$

或更一般地：

$$
\mathfrak U(R_\alpha K)
=
T_\alpha\mathfrak U(K),
$$

其中：

$$
T_\alpha:
\theta\mapsto\theta-\alpha.
$$

因此：

$$
\boxed{
\text{2D rotation}
\to
\text{phase shift on }S^1
}
$$

這不是視覺比喻，而是群作用候選。

---

# 9. $SO(2)$ 對 $S^1$ 的作用

定義：

$$
SO(2)\curvearrowright S^1.
$$

對：

$$
R_\alpha\in SO(2)
$$

與：

$$
e^{i\theta}\in S^1,
$$

作用為：

$$
R_\alpha\cdot e^{i\theta}
=
e^{i(\theta+\alpha)}.
$$

若形狀張力表示為：

$$
\tau_K:S^1\to\mathbb R,
$$

則旋轉後：

$$
(R_\alpha\cdot\tau_K)(\theta)
=
\tau_K(\theta-\alpha).
$$

因此最佳旋轉搜索：

$$
\inf_{\alpha\in[0,2\pi)}
$$

可被理解為：

$$
\boxed{
\text{群軌道上的相位對齊}
}
$$

---

# 10. 從 $SO(2)$ 到 $SE(2)$

平面定向保持剛體運動包含：

- 旋轉；
- 平移。

其群為：

$$
\boxed{
SE(2)
=
\mathbb R^2\rtimes SO(2)
}
$$

一個元素可寫為：

$$
g=(R_\alpha,t).
$$

作用：

$$
g\cdot x
=
R_\alpha x+t.
$$

因此原始最佳配置：

$$
N_p(K,U)
=
\inf_{g\in E(2)}
N_p(K,U;g)
$$

的連續定向保持部分可寫成：

$$
\inf_{g\in SE(2)}.
$$

完整合同還需另處理反射分支。

---

# 11. 猜想 B：群軌道張力猜想

對固定目標形態 $K$ 與候選覆蓋 $U$ ，定義：

$$
F_{K,U}(g)
=
N_p(K,U;g),
\qquad
g\in SE(2).
$$

則：

$$
N_p(K,U)
=
\inf_{g\in SE(2)}
F_{K,U}(g)
$$

可被視為：

> 在 $SE(2)$ 群軌道上尋找最小未覆蓋張力。

本文猜想：

$$
\boxed{
\text{若 }F_{K,U}\text{ 具有適當正則性，}
}
$$

則 hard-case placement 的主要結構可透過：

- 群軌道；
- 穩定子群；
- 李代數方向；
- 臨界點；
- 對稱性商空間；

加以分析。

這可能比把：

$$
(x,y,\theta)
$$

視為三個獨立暴力網格更有效。

---

# 12. 李代數局部坐標接口

$SE(2)$ 的李代數可記為：

$$
\mathfrak{se}(2).
$$

局部元素可用：

$$
\xi
=
(v_x,v_y,\omega)
$$

表示。

透過指數映射：

$$
g(\varepsilon)
=
\exp(\varepsilon\xi)
$$

生成局部群運動。

因此可研究張力方向導數：

$$
\left.
\frac{d}{d\varepsilon}
F_{K,U}
\bigl(
g\exp(\varepsilon\xi)
\bigr)
\right|_{\varepsilon=0}.
$$

這形成：

$$
\boxed{
\text{Lie-directional coverage tension}
}
$$

本文暫不推導完整公式，但將其列為後續主接口。

---

# 13. 120-cell 類比的真正可能意義

正一百二十胞體的環狀纖維構造對本文的啟發，不是「直接拿 120-cell 投影」。

真正可能的結構母型是：

$$
\boxed{
\text{巨大幾何對象}
\to
\text{有限環狀 fiber family}
\to
\text{群作用組織}
}
$$

對 Lebesgue 問題，類比後的研究問題是：

$$
\boxed{
\text{無窮形狀族}
\to
\text{有限或低複雜度週期軌道族}
\to
\text{張力證書}
}
$$

若成立，才是真正有價值的橋。

---

# 14. 猜想 C：纖維化壓縮猜想

設：

$$
\mathcal K_1
=
\{
K:
\operatorname{diam}(K)\le1
\}
$$

為目標形態族。

本文猜想可能存在某種任務相依映射：

$$
\Pi:
\mathcal K_1
\to
\mathcal F
$$

使 $\mathcal F$ 不是任意高維形狀空間，而是由：

- 若干 $S^1$ 纖維；
- 群軌道；
- 有限方向事件；
- 張力函數；

組成。

即：

$$
\boxed{
\mathcal K_1
\to
\{
\text{cyclic fibers with group action}
\}
}
$$

若信息忠實，可能進入證明。

若信息失真，仍可作算法壓縮。

---

# 15. 與 Hopf fibration 的邊界

Hopf fibration 經典形式涉及：

$$
S^3\to S^2
$$

且纖維為：

$$
S^1.
$$

120-cell 的環分解被研究者描述為 combinatorial Hopf fibration 式構造。

本文不把二維 Lebesgue 問題硬塞進：

$$
S^3\to S^2.
$$

真正借用的只有抽象精神：

$$
\boxed{
\text{複雜整體}
=
\text{由閉合纖維族組織}
}
$$

因此本文使用：

> **Hopf-like cyclic organization**

而非宣稱真正 Hopf fibration 已存在於本問題。

---

# 16. $H_2$ 作為二維候選對稱

若研究 $H_4$ 的低維類比，平面上最值得注意的是：

$$
H_2
\cong
I_2(5).
$$

它是五重二面體型反射群。

其基本幾何可由兩條反射軸生成，夾角與五重對稱相關。

在根系語言中，存在十個根方向。

因此可定義候選方向集：

$$
\boxed{
\Theta_{10}
=
\left\{
\frac{k\pi}{5}
:
k=0,\dots,9
\right\}
}
$$

這是最簡十方向環。

---

# 17. 猜想 D：十方向有限證書猜想

本文提出一個高風險、必須嚴格驗證的猜想：

> 對某些二維萬有覆蓋候選 $U$ ，最危險形態或局部 active tension 的主要方向，可能被一個十方向型集合有效捕捉。

形式上，若：

$$
\Theta_{10}
=
\left\{
k\pi/5
\right\}_{k=0}^{9},
$$

則可能存在：

$$
E_{\mathrm{dir}}
$$

使：

$$
\sup_{\theta\in S^1}
\mathcal T(\theta)
\approx
\max_{\theta\in\Theta_{10}}
\mathcal T(\theta)
+
E_{\mathrm{dir}}.
$$

若能證明：

$$
E_{\mathrm{dir}}\le\varepsilon,
$$

則十方向集可成為有限證書網格的一部分。

然而目前沒有理由保證：

$$
10
$$

必然最優。

因此此猜想必須與：

$$
n=6,8,10,12,16,\dots
$$

比較。

---

# 18. 猜想 D 的可證偽方式

若十方向只是視覺巧合，計算應揭示：

1. $n=10$ 不比鄰近 $n$ 更有效；
2. hard cases 不集中於五重方向；
3. 旋轉最優相位不形成五重／十重穩定模態；
4. 張力頻譜中無顯著 $k=5$ 或 $k=10$ 模態；
5. 其他方向網格以更少節點達到更低誤差。

因此：

$$
\boxed{
H_2\text{ 猜想是高度可證偽的}
}
$$

這是好事。

---

# 19. Fourier 模態接口

對環狀張力：

$$
\tau(\theta)
$$

可作 Fourier 展開：

$$
\tau(\theta)
=
a_0
+
\sum_{n=1}^{\infty}
\left(
a_n\cos n\theta
+
b_n\sin n\theta
\right).
$$

若五重結構重要，可能出現：

$$
n=5
$$

模態增強。

若十方向根軌道重要，可能出現：

$$
n=10
$$

或其相關諧波。

因此可以定義：

$$
P_n
=
a_n^2+b_n^2.
$$

檢驗：

$$
P_5,\ P_{10}
$$

是否對 hard-case ranking 特別有預測力。

---

# 20. 猜想 E：五重—十重譜模態猜想

對某些 near-optimal 候選 $U$ 與其最危險形態族，張力場：

$$
\tau_{K,U}(\theta)
$$

的頻譜可能在：

$$
n=5
$$

或：

$$
n=10
$$

出現異常高能量。

若成立，則：

$$
H_2
$$

不只是一個圖形類比，而可能在頻譜上留下可測特徵。

若不成立，則應放棄此方向。

---

# 21. 對踵關係與直徑一

直徑條件：

$$
\operatorname{diam}(K)\le1
$$

天然涉及任意點對：

$$
x,y\in K.
$$

在方向表示中，對踵方向：

$$
\theta
\quad\text{與}\quad
\theta+\pi
$$

尤其重要。

對凸體支撐函數：

$$
h_K(\theta)
$$

可定義方向寬度：

$$
w_K(\theta)
=
h_K(\theta)+h_K(\theta+\pi).
$$

直徑條件與最大方向寬度密切相關。

因此：

$$
\boxed{
\theta\leftrightarrow\theta+\pi
}
$$

並非人為加入。

十根系中的五對正負根，恰好與這類對踵關係形成形式呼應。

本文不把此呼應當證明，但認為值得計算。

---

# 22. 常寬體接口

對常寬一體：

$$
w_K(\theta)=1.
$$

即：

$$
h_K(\theta)
+
h_K(\theta+\pi)
=
1.
$$

若採用十方向：

$$
\theta_k
=
k\pi/5,
$$

則：

$$
\theta_{k+5}
=
\theta_k+\pi.
$$

所以十方向自然分成五個對踵寬度約束。

這可能形成：

$$
\boxed{
5\text{ independent antipodal pairs}
}
$$

的有限離散骨架。

---

# 23. 猜想 F：五對對踵約束骨架

對常寬 hard-case family 或其低階近似，可能存在五對對踵方向：

$$
(\theta_k,\theta_k+\pi),
\qquad
k=0,\dots,4,
$$

在局部最優覆蓋張力中形成 active set。

此猜想比「120-cell 直接相關」更具體，也更容易驗證。

可測：

- active directions 是否聚集成五對；
- 是否穩定於不同候選 $U$ ；
- 是否隨解析度增加仍存在；
- 是否只是初始形狀偏差造成。

---

# 24. 從十方向到循環圖 $C_{10}$

若離散化：

$$
S^1
\to
C_{10},
$$

則節點：

$$
v_0,\dots,v_9
$$

首尾相接。

群作用可由循環位移表示：

$$
\sigma(v_k)=v_{k+1}.
$$

反射：

$$
r(v_k)=v_{-k}.
$$

這生成二面體群：

$$
D_{10}
$$

或依記號慣例與：

$$
I_2(5)
$$

相關。

因此：

$$
\boxed{
\text{rotation}
+
\text{reflection}
}
$$

在離散環上具有天然群表示。

---

# 25. 離散張力

對：

$$
C_n
$$

上的張力值：

$$
\tau_k
=
\tau(v_k),
$$

定義：

$$
\|\tau\|_p
=
\left(
\frac1n
\sum_{k=0}^{n-1}
|\tau_k|^p
\right)^{1/p}.
$$

旋轉相位：

$$
(\sigma^m\tau)_k
=
\tau_{k-m}.
$$

最佳相位：

$$
\min_{m\in\mathbb Z_n}
\|\tau_U-\sigma^m\tau_K\|_p.
$$

這是非常低成本的離散群軌道匹配。

---

# 26. 從離散環到連續群

離散：

$$
C_n
$$

可視為：

$$
S^1
$$

的有限取樣。

當：

$$
n\to\infty,
$$

離散相位平移逼近：

$$
SO(2)
$$

作用。

因此可建立兩層：

$$
\boxed{
C_n
\to
S^1
}
$$

再加平移：

$$
\boxed{
S^1
\to
SE(2)
}
$$

這可能成為：

- 粗搜索；
- 精搜索；
- 證書化；

的分層算法。

---

# 27. 群軌道與 hard cases

設一個形態 $K$ 的群軌道：

$$
\mathcal O_K
=
\{
gK:
g\in SE(2)
\}.
$$

其最佳覆蓋張力：

$$
N_p(K,U)
=
\inf_{g\in SE(2)}
N_p(K,U;g)
$$

就是：

> 在整個軌道上找距離 $U$ 最近的狀態。

因此 hard case 定義：

$$
K^\star
\in
\arg\max_K
\inf_g
N_p(K,U;g).
$$

即：

$$
\boxed{
\text{最難被任何群軌道配置消除張力的形態}
}
$$

---

# 28. 猜想 G：active orbit support 猜想

若 $U^\star$ 為局部最優 universal cover，則可能存在有限或低複雜度軌道族：

$$
\mathcal O_{K_1},
\dots,
\mathcal O_{K_m}
$$

支撐其邊界最優性。

也就是：

> 不是所有形態都同等重要，而是少數 hard-case orbits 形成 active coverage tension。

這與前一版本的 active hard-case 猜想一致，但群論化後更精確。

---

# 29. 穩定子群

對形態 $K$ ，定義穩定子：

$$
\operatorname{Stab}(K)
=
\{
g\in SE(2):
gK=K
\}.
$$

若 $K$ 有高對稱性，則：

$$
\operatorname{Stab}(K)
$$

較大。

群軌道：

$$
SE(2)/\operatorname{Stab}(K)
$$

實際自由度下降。

因此正多邊形、常寬高對稱體與 $H_2$ 型形態在計算上可能具有特殊簡化。

---

# 30. 雙陪集接口

若候選覆蓋 $U$ 與目標 $K$ 分別有對稱群：

$$
G_U,
\qquad
G_K,
$$

則配置可能只需在：

$$
G_U\backslash E(2)/G_K
$$

上搜索。

這可消除重複配置。

因此群論價值之一是：

$$
\boxed{
\text{去除對稱冗餘}
}
$$

而不是只提供漂亮名詞。

---

# 31. 從張力差到群變分

前一版本定義局部面積—張力比：

$$
\rho_p
=
\frac{
\Delta\mathfrak N_p
}{
-\Delta\mu_2
}.
$$

現在加入群軌道後：

$$
\mathfrak N_p(U)
=
\sup_K
\inf_{g\in E(2)}
N_p(K,U;g).
$$

因此局部變形 $U_\varepsilon$ 會同時引起：

1. 候選覆蓋邊界變化；
2. 最佳群配置 $g^\star$ 跳動；
3. hard-case identity 改變。

所以真正的局部張力不是普通導數，而可能是：

$$
\boxed{
\text{nonsmooth minimax group variation}
}
$$

這是後續重要分析問題。

---

# 32. 猜想 H：群軌道相變猜想

當 $U$ 被逐步削減時，最佳配置：

$$
g^\star(K,U)
$$

可能不是平滑移動，而會在不同局部極小軌道之間跳轉。

形式上：

$$
g^\star_1
\to
g^\star_2
$$

產生配置相變。

這種跳轉可能正對應：

- 張力突升；
- active set 改變；
- hard case 轉換。

若成立，則只做局部梯度可能漏掉重要事件。

---

# 33. 環狀索引與相變

若最佳旋轉相位：

$$
\alpha^\star
$$

定義在：

$$
S^1,
$$

則不同局部極小值可能位於：

$$
\alpha_1,
\alpha_2,\dots
$$

當候選 $U$ 改變時，最優相位可能突然從：

$$
\alpha_i
$$

跳到：

$$
\alpha_j.
$$

因此環狀張力曲線：

$$
F(\alpha)
=
N_p(K,U;R_\alpha)
$$

本身值得研究。

---

# 34. 五重對稱的可觀測信號

若 $H_2$ 結構真的重要，至少應出現某些可測信號：

## 信號 1

$$
F(\alpha)
\approx
F(\alpha+2\pi/5).
$$

## 信號 2

張力峰值／谷值接近：

$$
\alpha_k
=
\alpha_0+k\frac{2\pi}{5}.
$$

## 信號 3

Fourier：

$$
P_5
$$

顯著。

## 信號 4

加入對踵後：

$$
P_{10}
$$

顯著。

## 信號 5

十方向有限網格異常高效。

若這些都不存在，應放棄 $H_2$ 猜想。

---

# 35. 120-cell 類比的更保守版本

本文真正願意保留的最小命題是：

## 命題類比 A

120-cell 顯示了一個高維幾何對象可以被重新理解為有限個互相纏繞的週期環族。

## 命題類比 B

二維萬有覆蓋的無窮配置族，也許可以被群軌道與週期張力族重新組織。

## 命題類比 C

兩者之間目前只有方法論類比，不存在已證明直接映射。

這三條是本文最安全的表述。

---

# 36. 更激進的命題：低維影子

本文提出一個高風險猜想：

## 猜想 I：低維影子猜想

某些高維正多胞體／Coxeter 結構之所以反覆出現於低維幾何優化，未必是因為低維問題直接「來自」高維物體，而可能因為：

$$
\boxed{
\text{有限群軌道}
+
\text{極端方向}
+
\text{對偶約束}
+
\text{週期閉合}
}
$$

在不同維度重複產生相似組合骨架。

因此 $H_2$ 與 $H_4$ 的形式呼應，可能反映的是：

> 同一類群作用與根方向組織原理的不同維度表現。

此猜想目前沒有證明。

---

# 37. 研究方法：不要先相信 120-cell

本文提出的實驗策略不是：

> 先假定答案是十方向。

而是：

$$
\boxed{
\text{讓十方向與其他方向數公平競爭}
}
$$

例如比較：

$$
n\in
\{
4,5,6,8,10,12,16,20,24,32
\}.
$$

對每個 $n$ ，建立：

$$
\Theta_n
=
\left\{
\frac{2\pi k}{n}
\right\}_{k=0}^{n-1}.
$$

測：

- hard-case ranking；
- 最壞殘差；
- 方向證書誤差；
- 群搜索成本；
- active direction 穩定性。

---

# 38. 十方向效率指標

定義：

$$
E_n(U)
=
\sup_K
\left|
\sup_{\theta\in S^1}
T_{K,U}(\theta)
-
\max_{\theta\in\Theta_n}
T_{K,U}(\theta)
\right|.
$$

若：

$$
E_{10}
$$

相對其節點數異常低，才支持十方向候選。

可比較效率：

$$
\eta_n
=
\frac{1}{nE_n}.
$$

若：

$$
\eta_{10}
$$

顯著高於鄰近 $n$ ，才有進一步理由。

---

# 39. 群軌道覆蓋張力

對環狀表示：

$$
q_K:S^1\to K,
$$

定義：

$$
\delta_{K,U,g}(\theta)
=
\operatorname{dist}
\bigl(
gq_K(\theta),U
\bigr).
$$

總張力：

$$
N_p(K,U;g)
=
\left(
\int_{S^1}
\delta_{K,U,g}(\theta)^p
\,d\lambda(\theta)
\right)^{1/p}.
$$

最佳群軌道：

$$
N_p(K,U)
=
\inf_{g\in SE(2)}
N_p(K,U;g).
$$

萬有張力：

$$
\mathfrak N_p(U)
=
\sup_K
N_p(K,U).
$$

因此最小覆蓋：

$$
m^\star
=
\inf_U
\{
\mu_2(U):
\mathfrak N_p(U)=0
\}.
$$

---

# 40. 離散 $C_{10}$ 原型

若暫採十方向：

$$
\theta_k
=
\frac{k\pi}{5},
$$

定義：

$$
\delta_k
=
\operatorname{dist}
\bigl(
gq_K(\theta_k),U
\bigr).
$$

離散張力：

$$
N_{p,10}
=
\left(
\frac1{10}
\sum_{k=0}^{9}
\delta_k^p
\right)^{1/p}.
$$

最佳離散相位：

$$
\min_{m\in\mathbb Z_{10}}
N_{p,10}(\sigma^m K,U).
$$

這是一個最簡原型，不是證明。

---

# 41. $H_2$ 反射接口

若加入反射生成元：

$$
r_1,\ r_2,
$$

則群軌道不只包含循環位移，也包含鏡射。

因此可研究：

$$
\min_{w\in W(H_2)}
N_{p,10}(wK,U).
$$

這對完整合同中的反射分支具有形式上的接口。

但要注意：

$$
W(H_2)
$$

只是有限反射群，而：

$$
E(2)
$$

包含連續平移與旋轉。

所以：

$$
W(H_2)
$$

最多是有限方向骨架，不是完整剛體運動群替代品。

---

# 42. $H_2$ 與 $SE(2)$ 的角色分工

本文提出一個重要區分：

$$
\boxed{
H_2
}
$$

可能負責：

- 有限方向骨架；
- 反射／旋轉離散對稱；
- root orbit；
- 候選證書節點。

而：

$$
\boxed{
SE(2)
}
$$

負責：

- 完整連續平移；
- 完整連續旋轉；
- 真實剛體配置軌道。

因此成熟方法可能是：

$$
\boxed{
H_2\text{ coarse skeleton}
+
SE(2)\text{ continuous refinement}
}
$$

---

# 43. 猜想 J：粗骨架—連續細化猜想

對某些 hard cases，最佳計算方法可能先用有限 Coxeter 型方向骨架定位：

$$
g_0,
$$

再在：

$$
SE(2)
$$

上局部細化：

$$
g^\star
=
g_0\exp(\xi^\star).
$$

即：

$$
\boxed{
\text{discrete symmetry seed}
\to
\text{Lie-group refinement}
}
$$

這是非常具體的算法命題。

---

# 44. 與前一版「左右極端預判」的關係

前一階段已研究：

- 左右端；
- 極端方向；
- 預判剪枝。

現在群論化後，可重新理解為：

$$
\boxed{
\text{先在有限方向軌道找極端}
\to
\text{再做連續群搜索}
}
$$

若十方向骨架有效，則可能把原先經驗式極端預判提升為群結構預判。

---

# 45. active tension 與 root directions

設局部邊界變形方向為：

$$
V.
$$

若 active hard cases 對某些法向方向特別敏感，可得到方向集：

$$
\mathcal A_U
=
\{
u_1,\dots,u_m
\}.
$$

若：

$$
\mathcal A_U
$$

經常接近 $H_2$ root directions，才支持本文猜想。

否則：

$$
H_2
$$

應被視為無效類比。

---

# 46. 猜想 K：active-root correspondence 猜想

對 near-optimal 候選 $U$ ，存在 active boundary normals：

$$
n_1,\dots,n_m
$$

使其在適當相位與尺度下近似某有限根軌道。

最激進版本：

$$
\{n_i\}
\approx
\Phi(H_2).
$$

本文將此列為：

$$
\boxed{
\text{高風險猜想}
}
$$

而非主結論。

---

# 47. 可能的失敗原因

本研究方向可能完全失敗，原因包括：

1. Lebesgue hard cases 無五重結構；
2. 十方向只是 120-cell 數字投射；
3. $S^1$ 只適合方向，不適合完整形狀索引；
4. 群軌道張力高度非光滑；
5. active set 無有限結構；
6. 距離核壓縮後失真過大；
7. $H_2$ 對算法沒有優勢；
8. 最優覆蓋的真實對稱性完全不同。

本文明確接受上述失敗可能。

---

# 48. 可證偽研究流程

## Step 1

建立一般 $S^1$ 張力表示，不加入 $H_2$ 。

## Step 2

生成 hard-case family。

## Step 3

計算：

$$
F_{K,U}(\alpha)
$$

的完整旋轉張力曲線。

## Step 4

做 Fourier 頻譜。

## Step 5

檢查：

$$
n=5,\ 10
$$

是否異常。

## Step 6

比較不同方向數：

$$
n=4,6,8,10,12,16,\dots
$$

## Step 7

只有在 $n=10$ 顯著時，才引入 $H_2$ 解釋。

這可避免確認偏誤。

---

# 49. 群論實驗

對固定 $K,U$ ：

$$
F(g)
=
N_p(K,U;g).
$$

在：

$$
SE(2)
$$

上做：

- 隨機搜索；
- 多起點局部搜索；
- 李代數梯度；
- 軌道臨界點統計。

觀察：

- 臨界點數；
- 穩定子群；
- 相位分布；
- 對稱倍數。

---

# 50. $S^1$ 與一維總量線的統合

前一版的：

$$
[0,1]
$$

主要表示總量累積。

本版：

$$
S^1
$$

主要表示週期方向／閉環。

兩者不必二選一。

可以使用：

$$
\boxed{
[0,1]\times S^1
}
$$

其中：

- $s\in[0,1]$ ：總量位置；
- $\theta\in S^1$ ：方向相位。

張力場：

$$
\delta(s,\theta).
$$

這可能比單一環更完整。

---

# 51. 圓柱型索引

完整表示可寫為：

$$
\boxed{
\mathcal C
=
[0,1]\times S^1
}
$$

即圓柱。

對每個：

$$
(s,\theta)
$$

記錄局部容量與方向張力。

此時：

$$
SO(2)
$$

只作用於 $\theta$ ：

$$
(s,\theta)
\mapsto
(s,\theta+\alpha).
$$

這是一個自然群作用。

---

# 52. 猜想 L：圓柱索引猜想

對二維 Lebesgue hard-case 分析，最小充分表示可能不是：

$$
[0,1]
$$

也不是：

$$
S^1
$$

而是：

$$
\boxed{
[0,1]\times S^1
}
$$

其中總量與方向分離。

若再保留距離核：

$$
D((s,\theta),(t,\phi)),
$$

可形成更完整表示。

---

# 53. 從圓柱到環面

如果第二個變數也具有週期性，例如：

- 邊界週期；
- 相位；
- 方向；

則可能出現：

$$
\boxed{
T^2
=
S^1\times S^1
}
$$

即二維環面。

這可能正是「120 胞環面」直覺需要被重新澄清的地方。

本文不主張最終答案一定是 torus。

但若：

1. 一個 $S^1$ 表示形狀閉合順序；
2. 另一個 $S^1$ 表示旋轉相位；

則自然得到：

$$
T^2.
$$

---

# 54. 猜想 M：雙週期環面猜想

對閉合形狀的週期索引：

$$
\varphi\in S^1
$$

與剛體旋轉相位：

$$
\theta\in S^1,
$$

可形成：

$$
(\varphi,\theta)\in T^2.
$$

覆蓋張力：

$$
\tau(\varphi,\theta).
$$

此時：

$$
\boxed{
\text{shape phase}
\times
\text{rotation phase}
}
$$

形成真正環面張力場。

這是目前最接近「環面」直覺的嚴格候選。

---

# 55. 為何環面可能比 120-cell 更直接

如果本問題真的出現 torus，最直接來源不必是 120-cell。

它可能只是：

$$
S^1\times S^1.
$$

即兩個週期自由度的乘積。

因此研究時應優先檢驗：

$$
\boxed{
\text{雙週期結構}
}
$$

而不是先宣稱：

$$
\boxed{
\text{120-cell 投影}
}
$$

這是重要的理性修正。

---

# 56. 120-cell 作為「提醒」，不是答案

因此本文最終給 120-cell 的定位是：

> 它提醒我們，高維複雜幾何可能存在非直觀的環狀纖維分解，而群論與週期纖維可能比直接坐標描述更接近結構核心。

這個提醒促使我們重新檢查：

- $S^1$ ；
- $C_n$ ；
- $T^2$ ；
- $H_2$ ；
- $SE(2)$ 。

但真正答案必須由 Lebesgue 問題自身決定。

---

# 57. 核心總猜想

本文將全部思想濃縮為：

## 總猜想

二維 Lebesgue 萬有覆蓋問題可能存在一個以：

$$
\boxed{
\text{環狀／週期索引}
+
\text{群作用}
+
\text{覆蓋張力}
}
$$

為核心的等價或近似重表述。

在信息忠實版本中，應保留足夠度量關係，使：

$$
\mathfrak N_p(U)=0
$$

與 universal coverage 等價。

在算法版本中，可能使用：

$$
S^1,
\quad
C_n,
\quad
H_2,
\quad
SE(2)
$$

降低搜索成本。

其中 $H_2$ 的五重—十根結構只是特殊候選，不是預設答案。

---

# 58. 最簡公式鏈

原問題：

$$
\forall K, 
\operatorname{diam}(K)\le1,
 
\exists g\in E(2):
gK\subseteq U.
$$

環狀表示：

$$
q_K:S^1\to K.
$$

距離核：

$$
D_K(\theta,\phi)
=
\|q_K(\theta)-q_K(\phi)\|.
$$

局部張力：

$$
\delta_{K,U,g}(\theta)
=
\operatorname{dist}(gq_K(\theta),U).
$$

群軌道張力：

$$
N_p(K,U)
=
\inf_{g\in SE(2)}
\left(
\int_{S^1}
\delta_{K,U,g}(\theta)^p
d\lambda(\theta)
\right)^{1/p}.
$$

萬有張力：

$$
\mathfrak N_p(U)
=
\sup_K N_p(K,U).
$$

最小覆蓋：

$$
m^\star
=
\inf_U
\{
\mu_2(U):
\mathfrak N_p(U)=0
\}.
$$

十方向候選：

$$
\Theta_{10}
=
\left\{
\frac{k\pi}{5}
\right\}_{k=0}^{9}.
$$

離散群骨架：

$$
H_2\cong I_2(5).
$$

連續群細化：

$$
SE(2).
$$

---

# 59. 結論

本文提出的不是「120-cell 解答」。

本文提出的是：

> 當二維 Lebesgue 萬有覆蓋問題被一維化並張力化後，週期閉合與群作用可能成為自然結構；而 120-cell 的離散環纖維、 $H_4$ 對稱及其低維 $H_2$ 類比，提供了一個值得檢驗但不可先驗相信的結構母型。

最表面的類比是：

$$
\{5\}
\to
\{5,3\}
\to
\{5,3,3\}.
$$

更深的類比是：

$$
H_2
\to
H_3
\to
H_4.
$$

環狀骨架則提示：

$$
C_{10},
\quad
S^1.
$$

平面剛體配置則自然進入：

$$
SE(2).
$$

若形狀閉合相位與旋轉相位同時存在，甚至可能自然出現：

$$
T^2
=
S^1\times S^1.
$$

因此本文真正的研究路線是：

$$
\boxed{
\text{2D shape family}
\to
\text{1D/cyclic metric representation}
\to
\text{group orbit}
\to
\text{coverage tension}
\to
\text{finite active structure?}
}
$$

最終必須檢驗：

$$
\boxed{
\text{是否真的湧現 }H_2\text{ 型五重—十根結構}
}
$$

若沒有，則放棄。

若有，而且能建立：

- 穩定性；
- 誤差界；
- 有限證書；
- 群作用等價；
- 張力零條件；

則其價值才真正超越類比。

本文 v0.1 的目的，是把這個高風險但可證偽的命題固定下來。

---

# 附錄 A：猜想清單

## 猜想 A：閉環索引優越性猜想
某些旋轉等價與週期張力任務中， $S^1$ 比 $[0,1]$ 更自然。

## 猜想 B：群軌道張力猜想
固定 $K,U$ 的最佳配置可視為 $SE(2)$ 群軌道上的張力極小化。

## 猜想 C：纖維化壓縮猜想
無窮形狀族可能被低複雜度週期纖維族與群軌道重新組織。

## 猜想 D：十方向有限證書猜想
十方向 $H_2$-型骨架可能對某些 hard-case family 異常高效。

## 猜想 E：五重—十重譜模態猜想
張力頻譜可能在 $n=5$ 或 $n=10$ 出現異常模態。

## 猜想 F：五對對踵約束骨架
常寬或近常寬 hard cases 可能形成五對 active antipodal directions。

## 猜想 G：active orbit support
局部最優邊界可能由有限 hard-case group orbits 支撐。

## 猜想 H：群軌道相變
候選削減時最佳配置可能在不同群軌道極小值間跳轉。

## 猜想 I：低維影子猜想
不同維度中相似 Coxeter 骨架可能源於共同群作用原理，而非直接投影。

## 猜想 J：粗骨架—連續細化
有限 $H_2$ 骨架可作 $SE(2)$ 連續搜索種子。

## 猜想 K：active-root correspondence
active boundary normals 可能近似有限 root orbit。

## 猜想 L：圓柱索引
$[0,1]\times S^1$ 可能是總量—方向的最小有效索引。

## 猜想 M：雙週期環面
形狀相位與旋轉相位可能形成 $T^2=S^1\times S^1$ 張力場。

---

# 附錄 B：可證偽條件

本文的 $H_2$ ／十方向猜想應在以下情況被否定：

1. $n=10$ 在方向近似效率上無特殊性；
2. hard-case 最優相位無五重結構；
3. Fourier $P_5,P_{10}$ 無異常；
4. active normals 不接近 root directions；
5. $H_2$ coarse seed 不改善 $SE(2)$ 搜索；
6. 十方向證書誤差顯著劣於其他 $n$ 。

---

# 附錄 C：文獻接口

1. Saul Schleimer, Henry Segerman, **Puzzling the 120-cell**, arXiv:1310.3549.  
   用於 120-cell 幾何、環狀分解與 combinatorial Hopf fibration 背景。

2. Saul Schleimer, Henry Segerman, **Puzzling the 120-Cell**, Notices of the AMS.  
   用於 12 個十胞環的正式敘述。

3. Mehmet Koca et al., **Branching of the $W(H_4)$ Polytopes and Their Dual Polytopes under the Coxeter Groups $W(H_3)$ and $W(A_3)$**, arXiv:1106.2957.  
   用於 $H_4$ 多胞體與低維 subgroup projection 背景。

4. Tamir Bendory et al., **Compactification of the Rigid Motions Group in Image Processing**, arXiv:2106.13505.  
   用於平面旋轉與平移構成 $SE(2)$ 剛體運動群的背景。

5. 其他 Coxeter root-system 文獻用於 $H_2\cong I_2(5)$ 與十根方向的標準背景。

---

# 附錄 D：最短研究備忘

若後續注意力切換後重新回到本題，只需恢復以下七句：

1. 120-cell 不是答案，只是環狀纖維母型。
2. 2D 正多胞體類比是五邊形，但群論類比是 $H_2$ 。
3. $H_2\cong I_2(5)$ ，五重反射對應十根方向。
4. 一維底空間可能從 $[0,1]$ 升級為 $S^1$ 。
5. 旋轉可變成 $S^1$ 上相位平移。
6. 完整剛體配置是 $SE(2)$ 群軌道張力最小化。
7. 真正要驗證的是：Lebesgue hard cases 是否自然湧現五重／十根 active structure。
