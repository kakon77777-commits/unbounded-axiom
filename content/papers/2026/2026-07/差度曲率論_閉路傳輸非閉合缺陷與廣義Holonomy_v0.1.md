# 差度曲率論：閉路傳輸、非閉合缺陷與廣義 Holonomy

## Difference-Based Curvature Theory: Closed-Loop Transport, Non-Closure Defects, and Generalized Holonomy

**文件編號**：EML-DBCT-2026-v0.1  
**作者**：Neo.K（許筌崴）  
**機構**：EveMissLab（一言諾科技有限公司），台灣  
**理論結晶化協作**：Aletheia  
**日期**：2026 年 7 月 13 日  
**理論地位**：無限曲率形式化的直接前置理論；連接差度計算、精細化算子論、索引幾何、投影計算與閉路傳輸  
**命名原則**：採結構性中性命名。作者姓名只標示著作歸屬，不用作定義、座標、定理、分類或算法名稱。  

**上游文件**：

1. 《差合化三位一體本體論：Cl 的完整動力學》  
2. 《索引幾何學：同一性拓樸微積分中的座標、投影與可計算性》  
3. 《投影計算論：無限維索引的有限表示、收斂與失真證書》  
4. 《索引動力學：重索引、結構漂移與回饋控制》  
5. 《精細化算子論：區分度、解析度、維度與可回溯提升》  

**下游預定文件**：

1. 《無限曲率形式論：精細化無界、投影不可封閉與高階遞歸》  
2. 《曲率譜系論：尺度、方向、投影與有限影之間的曲率變換》  
3. 《索引信息論：投影纖維、可辨識性與信息糊》  

---

## 摘要

曲率在日常語言中常被理解為「彎曲程度」，在初等幾何中常與圓、半徑與角度相連。然而，現代微分幾何與規範理論提供了更普遍的結構：指定一套沿路徑比較局部狀態的傳輸規則，把局部狀態沿閉路搬運後，若未完整返回原狀，該非閉合變換就是 holonomy；在光滑極限下，小閉路 holonomy 的面積正規化導出曲率。

本文建立**差度曲率論**。它不把任意「繞一圈後不同」直接命名為曲率，而先區分五種來源：

1. 基底路徑未真正閉合；
2. 傳輸不可逆或耗散；
3. 局部聯絡具有曲率；
4. 局部平坦但全域拓樸產生非平凡 holonomy；
5. 投影、量化或重建造成計算殘差。

在排除或標記上述來源後，本文定義一個廣義傳輸—差度系統：

$$
\mathfrak G
=
\left(
X,\rho:\mathcal F\to X,
\mathsf P(X),
\mathcal T,
\Delta,
\Gamma,
\sigma,
\mathcal G,
\mathcal C
\right),
$$

其中 $$X$$ 是基底空間，$$\mathcal F_x$$ 是每個基底點上的狀態纖維，$$\mathsf P(X)$$ 是合法路徑系統，$$\mathcal T$$ 是沿路徑的傳輸，$$\Delta$$ 是有型差度族，$$\Gamma$$ 是閉路族，$$\sigma$$ 是尺度正規化，$$\mathcal G$$ 是座標／規範變換，$$\mathcal C$$ 是證書系統。

對以 $$x$$ 為基點的閉路 $$\gamma$$，閉路傳輸為：

$$
H_\gamma
=
T_\gamma:\mathcal F_x\to\mathcal F_x.
$$

本文同時保留三層資料：

1. **holonomy 算子** $$H_\gamma$$；
2. **狀態相對閉路差**
   $$
   D_\gamma(v)
   =
   \Delta_x(v,H_\gamma v);
   $$
3. **尺度正規化差度曲率**
   $$
   K_\gamma(v)
   =
   \frac{D_\gamma(v)}{\sigma(\gamma)}.
   $$

單一純量不能取代 holonomy 算子，因為純量化可能抹去方向、符號、非交換性與共軛類信息。本文因此把「曲率」定義為一套有型資料，而不是唯一標量。

本文進一步證明或整理以下核心結果：路徑無關傳輸推出所有閉路 holonomy 平凡；若差度能分離纖維映射，所有狀態閉路差為零推出 holonomy 為恆等；在可逆且差度受傳輸保持的條件下，反向閉路具有對稱缺陷；在非擴張傳輸下，複合閉路差具有次可加上界；在規範變換下，閉路 holonomy 以共軛方式變換，因此合法曲率純量必須具有共軛不變性；在光滑向量束聯絡中，小閉路 holonomy 的面積極限恢復標準曲率算子；在離散圖與胞腔複形中，邊傳輸沿面邊界的有序乘積提供離散曲率資料。

本文的中心裁決是：

$$
\boxed{
\text{廣義曲率不是「看起來彎」，
而是可比較狀態沿可逆閉路傳輸後，
在排除基底不閉合、耗散與投影假差後，
仍存在的尺度化非閉合結構。}
}
$$

本文尚不定義無限曲率。它完成的是更基本的工作：明確指出什麼量可以合法地走向無界，以及在走向無界前必須通過哪些型別、規範、尺度與精細化檢查。

**關鍵詞**：差度曲率、閉路傳輸、非閉合缺陷、holonomy、聯絡、平行傳輸、規範不變性、離散曲率、投影殘差、精細化、無限曲率

---

# 第一章　概念清場：閉路後不同不必然等於曲率

## 1.1 曲率不是角度單位

$$
360^\circ=2\pi
$$

只是完整旋轉的計量約定。曲率不由「一圈被分成多少度」定義。

在平面曲線中，可用：

$$
\kappa=\frac{1}{r}
$$

描述圓的曲率；在黎曼幾何中，曲率由聯絡、切向方向和曲率張量決定；在規範理論中，場強：

$$
F_A=dA+A\wedge A
$$

描述聯絡的局部非平坦性；在離散幾何中，曲率可以由閉路傳輸、缺角或面 holonomy 表示。

因此：

$$
\boxed{
\text{曲率概念比圓與角度更一般。}
}
$$

## 1.2 Holonomy

給定基底點 $$x$$，把纖維中的狀態沿閉路：

$$
\gamma:x\leadsto x
$$

傳輸後得到：

$$
H_\gamma:\mathcal F_x\to\mathcal F_x.
$$

若：

$$
H_\gamma\neq\operatorname{id}_{\mathcal F_x},
$$

則閉路具有非平凡 holonomy。

Holonomy 記錄的是閉路累積變換，不必是一個角度；它可以是：

- 旋轉；
- 線性算子；
- Lie 群元素；
- 置換；
- 相位；
- 通道；
- 圖上的邊權乘積；
- 語義或索引轉移的總變換。

## 1.3 局部曲率與全域 holonomy

局部曲率與全域 holonomy 不能直接等同。

在光滑聯絡中，小而可縮的閉路 holonomy 由局部曲率控制。但即使局部曲率為零，若基底空間具有非平凡基本群，繞不可縮閉路仍可能產生非平凡全域 holonomy 或 monodromy。

因此要分開：

$$
\boxed{
\text{local curvature}
\neq
\text{global holonomy}.
}
$$

## 1.4 Torsion 與基底閉合缺陷

在仿射微分幾何中，torsion 是：

$$
\operatorname{Tor}(u,v)
=
\nabla_u v-\nabla_v u-[u,v].
$$

它與曲率不同。直觀上，torsion 可與無限小平行四邊形的基底閉合偏差相關；曲率則與向量沿閉路傳輸後的纖維變換相關。

本文因此區分：

- **基底閉合缺陷**：原本預期閉合的位移路徑是否真正回到同一基底點；
- **纖維閉路缺陷**：基底已閉合時，纖維狀態是否返回原狀。

前者只有在特定光滑仿射結構中，才可進一步與標準 torsion 對接。

## 1.5 Monodromy

Monodromy 常描述解析延拓、覆蓋空間或局部系統沿全域閉路後的多值變換。它可以存在於局部平坦系統。

本文把 monodromy 歸位為全域閉路結構，不把它當作局部曲率的同義詞。

## 1.6 Hysteresis 與記憶

系統沿參數閉路後未回到原狀，也可能是：

- 耗散；
- 塑性；
- 記憶；
- 不可逆相變；
- 控制器內部狀態；
- 快取與歷史依賴。

這些屬於路徑依賴，但若傳輸不是可逆的局部比較規則，不能無條件叫作幾何曲率。

## 1.7 投影殘差

有限投影可能讓本來平坦的結構看起來非閉合，也可能把真實曲率壓成零：

$$
\Pi H_\gamma
\neq
H^\Pi_{\Pi\gamma}\Pi.
$$

因此投影下的閉路差需分為：

- 被保存的曲率信號；
- 投影／重建失真；
- 數值誤差；
- 量化與版本差異。

## 1.8 七分裁決

$$
\boxed{
\text{曲率}
\neq
\text{holonomy 全部}
\neq
\text{torsion}
\neq
\text{monodromy}
\neq
\text{hysteresis}
\neq
\text{耗散}
\neq
\text{投影殘差}.
}
$$

它們可以相互作用，但不能因為都有「繞一圈後不同」而被壓成同一概念。

---

# 第二章　廣義傳輸—差度系統

## 2.1 基底與纖維

設 $$X$$ 為基底空間。對每個：

$$
x\in X,
$$

配置一個狀態纖維：

$$
\mathcal F_x.
$$

所有纖維組成：

$$
\rho:\mathcal F\to X.
$$

基底點可以表示：

- 空間位置；
- 索引位置；
- 模型參數；
- 觀察情境；
- 查詢狀態；
- 幾何精細層；
- 圖節點；
- 時變配置。

纖維元素可以表示：

- 向量；
- 相位；
- 機率分布；
- 視圖；
- 特徵；
- 量子態；
- 局部模型；
- 查詢語義。

## 2.2 路徑系統

用：

$$
\mathsf P(X)
$$

表示合法路徑。若路徑：

$$
\alpha:x\leadsto y,
$$

則起終點為：

$$
s(\alpha)=x,
\qquad
t(\alpha)=y.
$$

路徑可合成：

$$
\beta\circ\alpha:x\leadsto z
$$

當：

$$
t(\alpha)=s(\beta).
$$

常值路徑記為：

$$
1_x:x\leadsto x.
$$

若每條路徑有反向路徑：

$$
\alpha^{-1}:y\leadsto x,
$$

且路徑按適當等價形成群胚，則適合描述可逆幾何傳輸。若沒有反向，路徑只形成範疇或半群結構。

## 2.3 傳輸

對每條路徑：

$$
\alpha:x\leadsto y,
$$

指定傳輸：

$$
T_\alpha:\mathcal F_x\to\mathcal F_y.
$$

要求：

$$
T_{1_x}
=
\operatorname{id}_{\mathcal F_x},
$$

以及函子性：

$$
\boxed{
T_{\beta\circ\alpha}
=
T_\beta\circ T_\alpha.
}
$$

若：

$$
T_{\alpha^{-1}}
=
T_\alpha^{-1},
$$

則稱傳輸可逆。

標準平行傳輸、規範聯絡、離散向量束邊傳輸都屬可逆情況。Markov 通道、耗散演化與有損投影通常不可逆。

## 2.4 差度族

每個纖維配置有型差度：

$$
\Delta_x:
\mathcal F_x\times\mathcal F_x
\to
V_x,
$$

其中 $$V_x$$ 不必等於實數。

可選型別包括：

- 度量；
- 偽度量；
- 範數；
- 散度；
- 順序值；
- 集合值差；
- 任務損失；
- 算子差；
- 共軛類；
- 證書區間。

若需要純量化，另設：

$$
s_x:V_x\to[0,\infty].
$$

不應一開始就把所有差壓成單一實數，因為方向、符號、非交換性和類型資訊可能在純量化中永久丟失。

## 2.5 閉路族

以：

$$
\Gamma_x
=
\{
\gamma\in\mathsf P(X):
s(\gamma)=t(\gamma)=x
\}
$$

表示基於 $$x$$ 的閉路。

並可分為：

- 小閉路；
- 可縮閉路；
- 不可縮閉路；
- 圖面邊界；
- 精細化閉路；
- 重索引閉路；
- 投影—重建閉路；
- 任務條件閉路。

## 2.6 尺度量尺

對閉路給定：

$$
\sigma(\gamma)>0.
$$

它可以是：

- 面積；
- 長度平方；
- 胞腔面積；
- 圖面權重；
- 操作複雜度；
- 參數平面面積；
- 精細化尺度；
- 機率質量。

尺度量尺是曲率正規化的必要部分。沒有 $$\sigma$$，閉路愈長自然可能累積愈大變換，不能直接與局部曲率混為一談。

## 2.7 規範變換

對每個 $$x$$，取纖維自同構：

$$
g_x:\mathcal F_x\to\mathcal F_x.
$$

傳輸變換為：

$$
T_\alpha'
=
g_{t(\alpha)}
T_\alpha
g_{s(\alpha)}^{-1}.
$$

對閉路：

$$
H_\gamma'
=
g_x H_\gamma g_x^{-1}.
$$

因此 holonomy 算子的具體矩陣依座標／規範改變，但其共軛類是自然不變資料。

---

# 第三章　非閉合資料的三層表示

## 3.1 Holonomy 算子

對：

$$
\gamma\in\Gamma_x,
$$

定義：

$$
\boxed{
H_\gamma
=
T_\gamma:
\mathcal F_x\to\mathcal F_x.
}
$$

這是信息最完整的一層。它保留：

- 作用方向；
- 非交換性；
- 不動子空間；
- 譜；
- 群元素；
- 反演；
- 共軛類。

## 3.2 狀態相對閉路差

對：

$$
v\in\mathcal F_x,
$$

定義：

$$
\boxed{
D_\gamma(v)
=
\Delta_x
\left(
v,H_\gamma v
\right).
}
$$

這是一個狀態相對量。即使：

$$
H_\gamma\neq\operatorname{id},
$$

仍可能存在某些 $$v$$ 被固定：

$$
H_\gamma v=v,
$$

從而：

$$
D_\gamma(v)=0.
$$

因此單一狀態零差不能推出整個 holonomy 平凡。

## 3.3 算子閉路差

若纖維自映射空間有差度：

$$
\delta_x:
\operatorname{End}(\mathcal F_x)
\times
\operatorname{End}(\mathcal F_x)
\to W_x,
$$

定義：

$$
\boxed{
D_\gamma^{\mathrm{op}}
=
\delta_x
\left(
\operatorname{id}_{\mathcal F_x},
H_\gamma
\right).
}
$$

這比單一狀態差更接近整體閉路缺陷。

## 3.4 閉路差譜

對一族測試狀態：

$$
\mathcal V_x\subseteq\mathcal F_x,
$$

定義：

$$
\operatorname{Spec}_\Delta(\gamma)
=
\left\{
D_\gamma(v):v\in\mathcal V_x
\right\}.
$$

若 $$H_\gamma$$ 為線性算子，也可使用：

- 特徵值；
- 奇異值；
- 旋轉角；
- Jordan 結構；
- 不動空間維度；
- 群表示角色。

因此本文所謂「差度曲率」不是只有一個標量，而是一個可依任務選擇的閉路差譜。

## 3.5 尺度正規化

定義狀態相對差度曲率：

$$
\boxed{
K_\gamma(v)
=
\frac{
s_xD_\gamma(v)
}{
\sigma(\gamma)
}.
}
$$

定義算子差度曲率：

$$
\boxed{
K_\gamma^{\mathrm{op}}
=
\frac{
s_x^{\mathrm{op}}D_\gamma^{\mathrm{op}}
}{
\sigma(\gamma)
}.
}
$$

若純量化器與尺度量尺不同，得到的是不同曲率泛函，不能假裝存在唯一自然版本。

---

# 第四章　曲率資格檢查

本文不把所有閉路差都叫作曲率。需先通過五道檢查。

## 4.1 基底閉合檢查

若路徑的終點不是起點：

$$
t(\gamma)\neq s(\gamma),
$$

則不能比較同一纖維中的起終狀態，除非另有身份對齊。

定義基底閉合缺陷：

$$
B(\gamma)
=
\Delta_X
\left(
s(\gamma),t(\gamma)
\right).
$$

只有：

$$
B(\gamma)=0
$$

或有合法閉合證書時，才進入 holonomy 計算。

## 4.2 可逆性檢查

對路徑 $$\alpha$$，定義往返缺陷：

$$
R_\alpha(v)
=
\Delta_x
\left(
v,
T_{\alpha^{-1}}T_\alpha v
\right).
$$

算子版：

$$
R_\alpha^{\mathrm{op}}
=
\delta_x
\left(
\operatorname{id},
T_{\alpha^{-1}}T_\alpha
\right).
$$

若：

$$
R_\alpha^{\mathrm{op}}>0,
$$

傳輸含有不可逆、耗散、量化或記憶效應。

此時閉路差應記為**總傳輸缺陷**，而非純曲率。

## 4.3 差度相容檢查

若傳輸應被視為幾何比較，理想上要求：

$$
\Delta_y
\left(
T_\alpha u,T_\alpha v
\right)
=
\Delta_x(u,v).
$$

若只滿足：

$$
\Delta_y
\left(
T_\alpha u,T_\alpha v
\right)
\le
L_\alpha\Delta_x(u,v),
$$

則傳輸會收縮或放大差度，閉路缺陷可能混入度量畸變。

## 4.4 規範不變檢查

由於：

$$
H_\gamma'
=
g_xH_\gamma g_x^{-1},
$$

合法曲率資料應使用：

- 共軛類；
- trace／character；
- 譜；
- 共軛不變範數；
- 規範協變算子；
- 指定規範下附帶轉換律的量。

直接比較兩個座標矩陣元素，可能只是在測量規範選擇。

## 4.5 投影誤差檢查

若觀察到的是有限投影：

$$
H_\gamma^\lambda,
$$

需報告：

$$
E_{\mathrm{hol},\lambda}(\gamma)
=
\delta
\left(
J_\lambda H_\gamma^\lambda,
H_\gamma
\right)
$$

或可計算的後驗上界。

沒有投影證書的閉路差，不能直接被提升為本體曲率。

## 4.6 曲率合格條件

本文暫定：

> 閉路差只有在基底閉合、傳輸可逆或耗散已分離、差度相容、規範型別明確且投影誤差受控時，才稱為**曲率合格閉路差**。

---

# 第五章　基本命題

## 5.1 恆等閉路命題

對常值閉路：

$$
1_x,
$$

由傳輸單位律：

$$
H_{1_x}
=
\operatorname{id}_{\mathcal F_x}.
$$

因此：

$$
D_{1_x}(v)=0.
$$

## 5.2 路徑無關推出平凡 holonomy

**定理 5.1**

若任意兩條同起終點路徑具有相同傳輸：

$$
\alpha,\beta:x\leadsto y
\quad\Rightarrow\quad
T_\alpha=T_\beta,
$$

且傳輸可逆，則所有閉路 holonomy 平凡：

$$
H_\gamma=\operatorname{id}.
$$

**證明**

對任意閉路 $$\gamma:x\leadsto x$$，它與常值路徑 $$1_x$$ 同起終點。由路徑無關性：

$$
T_\gamma=T_{1_x}
=
\operatorname{id}.
$$

$$\square$$

## 5.3 狀態分離推出算子平凡

**命題 5.2**

若：

$$
\Delta_x(u,v)=0
\iff
u=v,
$$

且：

$$
D_\gamma(v)=0
$$

對所有：

$$
v\in\mathcal F_x
$$

成立，則：

$$
H_\gamma=\operatorname{id}.
$$

**證明**

對每個 $$v$$：

$$
\Delta_x(v,H_\gamma v)=0
$$

推出：

$$
H_\gamma v=v.
$$

故算子在所有狀態上等於恆等。$$\square$$

## 5.4 反向閉路對稱

**命題 5.3**

若傳輸可逆，且 $$H_\gamma$$ 保持差度，則：

$$
D_{\gamma^{-1}}
\left(
H_\gamma v
\right)
=
D_\gamma(v).
$$

**證明**

$$
H_{\gamma^{-1}}
=
H_\gamma^{-1}.
$$

因此：

$$
D_{\gamma^{-1}}(H_\gamma v)
=
\Delta_x
\left(
H_\gamma v,
H_\gamma^{-1}H_\gamma v
\right)
=
\Delta_x(H_\gamma v,v).
$$

若差度對稱，或使用適當對稱化，即得結論。$$\square$$

非對稱散度下，反向缺陷一般不同，需保留方向。

## 5.5 複合閉路次可加界

設：

$$
\gamma_1,\gamma_2\in\Gamma_x.
$$

若 $$\Delta_x$$ 是度量且 $$H_{\gamma_2}$$ 為 $$L_2$$-Lipschitz，則：

$$
D_{\gamma_2\circ\gamma_1}(v)
\le
D_{\gamma_2}(v)
+
L_2D_{\gamma_1}(v).
$$

**證明**

由三角不等式：

$$
\Delta(v,H_{\gamma_2}H_{\gamma_1}v)
\le
\Delta(v,H_{\gamma_2}v)
+
\Delta(H_{\gamma_2}v,H_{\gamma_2}H_{\gamma_1}v).
$$

第二項由 Lipschitz 性得界。$$\square$$

若傳輸為等距：

$$
L_2=1.
$$

## 5.6 非交換閉路

一般：

$$
H_{\gamma_2\circ\gamma_1}
=
H_{\gamma_2}H_{\gamma_1}
$$

但：

$$
H_{\gamma_2}H_{\gamma_1}
\neq
H_{\gamma_1}H_{\gamma_2}.
$$

因此只保留純量閉路差可能看不見非交換順序。非交換性本身是曲率結構的重要部分。

---

# 第六章　光滑極限與標準曲率

## 6.1 聯絡

在光滑向量束：

$$
E\to M
$$

上，聯絡：

$$
\nabla
$$

提供沿切向方向比較截面的方法。

標準曲率算子為：

$$
\boxed{
R^\nabla(u,v)
=
\nabla_u\nabla_v
-
\nabla_v\nabla_u
-
\nabla_{[u,v]}.
}
$$

對主叢聯絡形式 $$A$$，曲率二形式為：

$$
F_A=dA+A\wedge A.
$$

## 6.2 小閉路 holonomy

取基點 $$x$$ 、切向方向 $$u,v$$ ，以及由小參數 $$\varepsilon$$ 生成的可縮閉路：

$$
\gamma_{\varepsilon;u,v}.
$$

在適當光滑與規範條件下，holonomy 具有漸近展開：

$$
H_{\gamma_{\varepsilon;u,v}}
=
\operatorname{id}
+
\varepsilon^2
R^\nabla_x(u,v)
+
o(\varepsilon^2),
$$

符號與係數依閉路方向、參數化和慣例可能改變。

若閉路面積：

$$
\sigma(\gamma_{\varepsilon;u,v})
\sim
\varepsilon^2,
$$

則：

$$
\lim_{\varepsilon\to0}
\frac{
H_{\gamma_{\varepsilon;u,v}}
-
\operatorname{id}
}{
\sigma(\gamma_{\varepsilon;u,v})
}
$$

恢復曲率算子。

## 6.3 差度版本

若纖維有範數，對狀態 $$w$$：

$$
D_{\gamma_\varepsilon}(w)
=
\left\|
H_{\gamma_\varepsilon}w-w
\right\|.
$$

則：

$$
\frac{
D_{\gamma_\varepsilon}(w)
}{
\sigma(\gamma_\varepsilon)
}
\longrightarrow
\left\|
R^\nabla_x(u,v)w
\right\|
$$

在相應可微條件下成立。

這表明差度曲率是標準曲率的**純量化作用版本**，而不是替代曲率張量的全信息對象。

## 6.4 Ambrose–Singer 接口

在標準光滑主叢／向量束理論中，holonomy Lie 代數由經平行傳輸的曲率值生成。這提供局部曲率與 holonomy 群之間的深層關係。

但本文不把此定理無條件推廣到：

- 非可逆傳輸；
- 一般散度；
- 任意圖系統；
- 語義索引；
- 投影計算；
- 不具 Lie 群結構的纖維。

在這些情況下，只保留「閉路傳輸與局部缺陷可能相關」的結構接口。

---

# 第七章　離散差度曲率

## 7.1 圖上的傳輸

設圖：

$$
G=(V,E).
$$

每個頂點 $$i$$ 有纖維：

$$
\mathcal F_i.
$$

每條有向邊：

$$
e:i\to j
$$

配置：

$$
U_e:\mathcal F_i\to\mathcal F_j.
$$

若邊反向存在且：

$$
U_{\bar e}=U_e^{-1},
$$

則傳輸可逆。

## 7.2 迴路 holonomy

對閉路：

$$
C=e_n\cdots e_2e_1,
$$

定義有序乘積：

$$
\boxed{
H_C
=
U_{e_n}\cdots U_{e_2}U_{e_1}.
}
$$

若：

$$
H_C\neq\operatorname{id},
$$

閉路具有離散 holonomy。

## 7.3 面曲率

若圖是胞腔複形的一維骨架，每個面 $$f$$ 有邊界：

$$
\partial f.
$$

定義：

$$
H_f
=
H_{\partial f}.
$$

可用：

$$
K_f^{\mathrm{op}}
=
\frac{
\delta(\operatorname{id},H_f)
}{
A_f
}
$$

作為面曲率純量，其中 $$A_f$$ 是面權重或面積。

## 7.4 離散平坦性

若所有基本面：

$$
H_f=\operatorname{id},
$$

在單連通、生成關係完整且傳輸一致的條件下，可以推出可縮閉路平坦。

若基底有孔洞，即使每個局部面平坦，非可縮閉路仍可有全域 holonomy。

## 7.5 缺角接口

在分片平坦幾何或 Regge 型離散幾何中，曲率集中於 hinge，最小閉路 holonomy 可用缺角或相應旋轉表示。

缺角只是離散幾何的一種曲率實例，不是本文一般定義的唯一形式。

## 7.6 離散資料不足

有限個離散 holonomy 值通常不足以唯一決定一般連接。若只量測少數閉路，未觀察方向可能承載不同曲率。

因此：

$$
\boxed{
\text{有限閉路樣本}
\not\Rightarrow
\text{完整曲率重建}.
}
$$

這將直接連到投影不可封閉與無限曲率形式化。

---

# 第八章　不可逆傳輸與耗散分離

## 8.1 為何不可逆傳輸需要另案

若：

$$
T_{\alpha^{-1}}T_\alpha
\neq
\operatorname{id},
$$

即使路徑只是走出去再沿原路返回，也可能產生非零差。

這個差顯然不能全歸因於基底幾何曲率。

## 8.2 往返耗散

定義：

$$
\boxed{
D_{\mathrm{irr}}(\alpha;v)
=
\Delta_x
\left(
v,T_{\alpha^{-1}}T_\alpha v
\right).
}
$$

若：

$$
D_{\mathrm{irr}}(\alpha;v)=0
$$

對所有 $$v$$ 成立，傳輸至少在此路徑往返上可逆。

## 8.3 總閉路缺陷

對一般閉路，記：

$$
D_{\mathrm{tot}}(\gamma;v)
=
\Delta_x(v,T_\gamma v).
$$

本文不假設存在普遍可加分解：

$$
D_{\mathrm{tot}}
=
D_{\mathrm{curv}}
+
D_{\mathrm{irr}}.
$$

因為非線性和非交換系統中兩者可能交互作用。

較安全的做法是輸出診斷對：

$$
\left(
D_{\mathrm{tot}},
D_{\mathrm{irr}}
\right)
$$

以及可逆近似或對照路徑。

## 8.4 可逆核心

若能把傳輸分解為：

$$
T_\alpha
=
N_\alpha U_\alpha,
$$

其中 $$U_\alpha$$ 為可逆或等距部分，$$N_\alpha$$ 為耗散部分，則可在具體模型中分別研究。

但此類分解依空間結構而定，不作為本文的一般公理。

## 8.5 操作曲率

對不可逆系統，仍可研究閉路操作缺陷，但建議命名為：

- 操作 holonomy；
- 通道閉路缺陷；
- 記憶閉路；
- 耗散路徑差；

除非已證明其中存在獨立、規範穩定且尺度化的可逆曲率分量。

---

# 第九章　投影曲率與計算殘差

## 9.1 投影交換方塊

理想層傳輸：

$$
T_\alpha^\infty
$$

與有限影傳輸：

$$
T_{\Pi_\lambda\alpha}^{\lambda}
$$

應比較交換缺陷：

$$
E_{\lambda,\alpha}
=
\delta
\left(
\Pi_\lambda T_\alpha^\infty,
T_{\Pi_\lambda\alpha}^{\lambda}\Pi_\lambda
\right).
$$

若：

$$
E_{\lambda,\alpha}=0,
$$

投影與傳輸交換。

## 9.2 閉路投影失真

對閉路：

$$
\gamma,
$$

定義：

$$
\boxed{
E_{\mathrm{hol},\lambda}(\gamma)
=
\delta
\left(
\Pi_\lambda H_\gamma^\infty,
H_{\Pi_\lambda\gamma}^{\lambda}\Pi_\lambda
\right).
}
$$

它可能造成：

- 真曲率被抹除；
- 平坦結構產生假曲率；
- 非交換順序被壓成交換；
- 小不動子空間被放大；
- 全域閉路被截斷。

## 9.3 投影下界與上界

若投影為 $$L_\Pi$$-Lipschitz：

$$
\Delta_\lambda
\left(
\Pi_\lambda u,\Pi_\lambda v
\right)
\le
L_\Pi\Delta_\infty(u,v),
$$

只能得到投影差的上界。一般不能由小投影差推出小理想差。

若投影在指定子類上具逆穩定性：

$$
c_\Pi\Delta_\infty(u,v)
\le
\Delta_\lambda
\left(
\Pi_\lambda u,\Pi_\lambda v
\right),
$$

才可從有限影反推理想差。

## 9.4 曲率一致投影

若：

$$
E_{\mathrm{hol},\lambda}(\gamma)
\to0
$$

對指定閉路族一致成立，則稱投影族在該閉路族上曲率一致。

若只逐點收斂：

$$
\forall\gamma,\quad
E_{\mathrm{hol},\lambda}(\gamma)\to0,
$$

仍可能不存在統一有限層控制全部閉路。

這個差別將成為無限曲率形式論的核心。

---

# 第十章　精細化相容性

## 10.1 多層傳輸系統

在精細化層：

$$
\lambda\preceq\mu
$$

上，有：

$$
T_{\lambda,\gamma_\lambda},
\qquad
T_{\mu,\gamma_\mu}.
$$

粗化映射：

$$
p_{\lambda\mu}:\mathcal F_\mu\to\mathcal F_\lambda.
$$

要求傳輸相容：

$$
p_{\lambda\mu}
T_{\mu,\gamma_\mu}
\approx
T_{\lambda,p_{\lambda\mu}\gamma_\mu}
p_{\lambda\mu}.
$$

## 10.2 精細化傳輸殘差

定義：

$$
\boxed{
E_{\lambda\mu}^{T}(\gamma_\mu)
=
\delta
\left(
p_{\lambda\mu}T_{\mu,\gamma_\mu},
T_{\lambda,p\gamma_\mu}p_{\lambda\mu}
\right).
}
$$

若為零，粗細傳輸交換。

## 10.3 曲率比較映射

不同層曲率可能位於不同空間，需指定：

$$
\mathcal J_{\lambda\mu}:
\mathcal K_\mu\to\mathcal K_\lambda.
$$

例如：

- 算子壓縮；
- Lie 代數投影；
- 差度正規化；
- 譜摘要；
- 面聚合；
- 閉路粗化。

沒有 $$\mathcal J_{\lambda\mu}$$，不能合法寫：

$$
K_\lambda<K_\mu
$$

或：

$$
K_\lambda\to\infty.
$$

## 10.4 曲率顯露

若：

$$
K_\lambda=0
$$

但：

$$
K_\mu>0,
$$

且精細化殘差受控，可能表示細層顯露粗層不可辨識的閉路。

若殘差不受控，也可能只是細層模型生成了新傳輸規則。

## 10.5 曲率保持

若：

$$
\mathcal J_{\lambda\mu}(K_\mu)
=
K_\lambda,
$$

稱為曲率相容精細化。

## 10.6 曲率不一致

若：

$$
\left\|
\mathcal J_{\lambda\mu}(K_\mu)-K_\lambda
\right\|
$$

不隨精細化縮小，需區分：

- 真多尺度效應；
- 閉路族改變；
- 尺度量尺不相容；
- 投影錯誤；
- 數值不穩定；
- 模型版本改變。

---

# 第十一章　平坦性的層級

「平坦」也不是單一概念。

## 11.1 狀態相對平坦

對特定 $$v$$：

$$
D_\gamma(v)=0.
$$

只表示該狀態被 holonomy 固定。

## 11.2 閉路平坦

對特定閉路：

$$
H_\gamma=\operatorname{id}.
$$

## 11.3 局部平坦

所有充分小的可縮閉路：

$$
H_\gamma=\operatorname{id}
$$

或小閉路曲率極限為零。

在光滑聯絡中對應：

$$
F_A=0.
$$

## 11.4 可縮閉路平坦

所有可縮閉路 holonomy 平凡。

## 11.5 全域平坦

所有閉路：

$$
H_\gamma=\operatorname{id}.
$$

## 11.6 表示平坦

有限投影中：

$$
H_\gamma^\lambda=\operatorname{id}.
$$

這可能是假平坦，因為投影丟失了真 holonomy。

## 11.7 層級關係

一般有：

$$
\text{全域平坦}
\Rightarrow
\text{可縮閉路平坦}
\Rightarrow
\text{局部平坦}.
$$

反向不必成立。

狀態相對平坦更弱，與整體算子平坦不可混同。

---

# 第十二章　差—合—化的重新歸位

## 12.1 差

$$
\Delta
$$

不再假定為唯一普通度量，而是有型差度族。閉路差測量起始狀態與傳輸後狀態的可辨識偏離。

## 12.2 合

「合」不以單一數值函數承擔所有連結意義，而由：

- 基底鄰接；
- 束結構；
- 路徑可合成性；
- 聯絡；
- 邊耦合；
- 規範群作用；

共同表達。

## 12.3 化

「化」不再預先用時間微分定義。本文使用：

$$
T_\alpha
$$

作為沿合法路徑的狀態轉換。

時間演化是傳輸的一個實例，不是傳輸定義的必要前提。

## 12.4 閉路循環

最小循環為：

$$
v
\xrightarrow{T_{\gamma}}
H_\gamma v
\xrightarrow{\Delta}
D_\gamma(v).
$$

此處：

- 路徑與聯絡提供「合」；
- 傳輸提供「化」；
- 閉路比較提供「差」。

因此曲率不是三者的簡單相加，而是三者按型別組合後的非閉合輸出。

## 12.5 守恆式暫停

早期形式：

$$
\Delta_{\mathrm{total}}
+
\mathcal U_{\mathrm{total}}
+
\mathcal N_{\mathrm{total}}
=
K
$$

把不同單位與型別的量直接相加，本文不採為公理。

未來若要建立守恆律，需先：

1. 指定每個量的型別；
2. 建立無量綱化；
3. 指定共同泛函；
4. 證明在特定動力方程下守恆或單調。

---

# 第十三章　任務相對曲率

## 13.1 為何曲率量可以任務相對

同一 holonomy 算子可能：

- 對某些狀態作用強；
- 對另一些狀態為零；
- 對某查詢可見；
- 對另一查詢不可見。

因此定義查詢：

$$
q_x:\mathcal F_x\to Y.
$$

查詢閉路差：

$$
D_{\gamma,q}(v)
=
\Delta_Y
\left(
q_x(v),
q_x(H_\gamma v)
\right).
$$

## 13.2 任務曲率

$$
K_{\gamma,q}(v)
=
\frac{
D_{\gamma,q}(v)
}{
\sigma(\gamma)
}.
$$

它不是本體完整曲率，而是 holonomy 對任務 $$q$$ 的可觀察作用。

## 13.3 盲區

可能有：

$$
K_{\gamma,q}(v)=0
$$

但：

$$
H_\gamma v\neq v.
$$

此時查詢 $$q$$ 對該閉路差失明。

## 13.4 查詢分離族

若查詢族 $$\mathcal Q$$ 滿足：

$$
\forall u\neq v,
\quad
\exists q\in\mathcal Q:
q(u)\neq q(v),
$$

則稱 $$\mathcal Q$$ 分離纖維狀態。

只有相對分離查詢族的全零查詢差，才有資格推出狀態差為零。

---

# 第十四章　曲率證書

## 14.1 閉路證書

包含：

- 閉路基點；
- 路徑版本；
- 路徑方向；
- 閉合誤差；
- 可縮／不可縮標記；
- 尺度量尺；
- 邊界或面資料。

## 14.2 傳輸證書

包含：

- 傳輸規則；
- 函子性誤差；
- 可逆性；
- 往返缺陷；
- 差度保持常數；
- 規範轉換律。

## 14.3 差度證書

包含：

- 差度型別；
- 定義域；
- 對稱性；
- 三角不等式；
- 分離性；
- 單位；
- 純量化器。

## 14.4 規範證書

包含：

- 使用的 trivialization；
- 規範變換；
- 純量是否共軛不變；
- 不同版本比較方式。

## 14.5 投影證書

包含：

- 投影層；
- holonomy 交換殘差；
- 閉路是否被截斷；
- 曲率上下界；
- 未觀察方向。

## 14.6 曲率聲明格式

任何正式曲率聲明建議寫為：

$$
\boxed{
\mathsf{CurvClaim}
[
X,\mathcal F,\Gamma,\mathcal T,
\Delta,\sigma,\mathcal G,
\lambda,q,\varepsilon
].
}
$$

不再只寫：

$$
\kappa=3
$$

或：

$$
\kappa=\infty
$$

而不說明它是哪一種曲率、在哪個尺度、對哪個狀態與查詢成立。

---

# 第十五章　示例

## 15.1 球面平行傳輸

在球面上，把切向量沿封閉曲線平行傳輸，回到起點時一般發生旋轉。小閉路下，旋轉與所包圍的高斯曲率面積積分相關。

此例展示：

- 基底閉合；
- 傳輸可逆；
- 差度可由切向量夾角或範數定義；
- holonomy 由局部曲率累積。

## 15.2 局部平坦但全域非平凡

考慮局部平坦聯絡或局部系統，沿小可縮閉路 holonomy 平凡，但沿包圍孔洞的不可縮閉路產生非平凡變換。

此例展示：

$$
F=0
$$

不必推出所有全域 holonomy 平凡。

## 15.3 圖上的矩陣傳輸

四個節點構成方形，每條邊配置矩陣：

$$
U_{12},U_{23},U_{34},U_{41}.
$$

面 holonomy：

$$
H_\square
=
U_{41}U_{34}U_{23}U_{12}.
$$

若：

$$
H_\square\neq I,
$$

面具有離散閉路缺陷。

若所有邊矩陣互相交換，順序問題減弱；若不交換，方向與路徑次序是曲率資料的一部分。

## 15.4 投影—重建閉路

理想索引：

$$
i_\infty
$$

經有限投影：

$$
\Pi_\lambda
$$

再重建：

$$
R_\lambda
$$

形成閉路：

$$
i_\infty
\xrightarrow{\Pi_\lambda}
i_\lambda
\xrightarrow{R_\lambda}
\widehat i_\infty.
$$

閉路差：

$$
D_\lambda(i)
=
\Delta
\left(
i,R_\lambda\Pi_\lambda i
\right).
$$

這是投影閉路缺陷，不應直接叫作幾何曲率；只有當投影層本身被當作基底、轉移規則滿足相應結構並通過曲率資格檢查時，才可形成索引曲率模型。

## 15.5 不可逆資料處理

資料經有損壓縮後解碼：

$$
x
\xrightarrow{C}
c
\xrightarrow{D}
\widehat x.
$$

即使把流程視為閉路：

$$
x\to c\to\widehat x,
$$

其差：

$$
\Delta(x,\widehat x)
$$

主要是有損編碼殘差，不是曲率。若強行稱作曲率，會把不可逆性與幾何非閉合混為一談。

---

# 第十六章　無限曲率的直接接口

本文只建立接口，不做最終定義。

## 16.1 值無界

存在曲率合格閉路序列：

$$
(\gamma_n,v_n)
$$

使：

$$
K_{\gamma_n}(v_n)\to\infty.
$$

## 16.2 方向無統一界

在固定基點與尺度族中：

$$
\sup_{\gamma\in\Gamma_x}
K_\gamma^{\mathrm{op}}
=
\infty.
$$

## 16.3 精細化無界

每個有限層：

$$
\sup_{\gamma\in\Gamma_\lambda}
K_{\lambda,\gamma}
<
\infty,
$$

但：

$$
\sup_{\lambda}
\sup_{\gamma\in\Gamma_\lambda}
K_{\lambda,\gamma}
=
\infty.
$$

## 16.4 投影不可封閉

對任意有限層，總存在閉路使 holonomy 失真無法受統一控制：

$$
\forall\lambda,
\quad
\sup_{\gamma}
E_{\mathrm{hol},\lambda}(\gamma)
>
\varepsilon_0
$$

對某個：

$$
\varepsilon_0>0.
$$

## 16.5 高階遞歸

傳輸規則、規範變換或曲率比較映射本身形成新基底，並可再定義閉路傳輸：

$$
K^{(0)},
K^{(1)},
K^{(2)},
\ldots
$$

若高階閉路差無統一界，形成遞歸無界候選。

## 16.6 仍需排除的假發散

正式無限曲率定義必須排除：

- $$\sigma(\gamma)\to0$$ 過快造成的平凡除零；
- 差度單位跨層不一致；
- 閉路長度無界但未局部正規化；
- 非可逆耗散累積；
- 投影噪聲；
- 規範不變性失敗；
- 閉路族任意擴張；
- 數值條件數爆炸；
- 模型版本不同。

---

# 第十七章　核心定理與限制彙整

## 17.1 路徑無關定理

可逆且路徑無關的傳輸具有平凡閉路 holonomy。

## 17.2 分離差度定理

若所有狀態閉路差為零且差度分離狀態，則 holonomy 為恆等。

## 17.3 規範共軛命題

閉路 holonomy 在規範變換下按共軛變換；合法純量曲率需要共軛不變或明示規範協變性。

## 17.4 小閉路還原命題

在光滑聯絡與適當正規化下，小閉路 holonomy 的二階主項由標準曲率算子控制。

## 17.5 局部平坦不推出全域平凡

基底拓樸非平凡時，零局部曲率可與非平凡全域 holonomy 共存。

## 17.6 不可逆閉路限制

往返缺陷非零時，總閉路差不能無條件解讀為純幾何曲率。

## 17.7 投影零差限制

有限投影中 holonomy 為零，不推出理想層 holonomy 為零；需投影分離或逆穩定條件。

## 17.8 無終端閉路族限制

閉路數量或階數無限，不推出曲率無限。無限曲率需要無界量、不可一致控制或其他明確型別條件。

---

# 第十八章　形式化與工程路線

## 18.1 Python 原型

第一階段：

- 圖上的矩陣邊傳輸；
- 閉路列舉；
- holonomy 有序乘積；
- 狀態差、算子差與譜；
- 可逆性／往返檢查；
- 規範共軛測試。

第二階段：

- 多解析度圖；
- 粗細傳輸殘差；
- 投影曲率失真；
- 局部與全域 holonomy 分離；
- 閉路採樣不足實驗。

第三階段：

- 不可逆通道；
- 耗散與 holonomy 診斷對；
- 高階重索引閉路；
- 無界候選壓力測試。

## 18.2 Lean 4 形式化

### DCT1：傳輸函子

形式化：

$$
T_{1_x}=\operatorname{id},
$$

$$
T_{\beta\circ\alpha}=T_\beta\circ T_\alpha.
$$

### DCT2：路徑無關推出閉路平凡

形式化定理 5.1。

### DCT3：全狀態零差推出算子恆等

在差度分離假設下形式化命題 5.2。

### DCT4：重索引／規範共軛

形式化：

$$
H_\gamma'
=
g_xH_\gamma g_x^{-1}.
$$

### DCT5：離散閉路傳輸

對有限圖和群值邊傳輸形式化 holonomy 乘積。

### DCT6：投影交換殘差

先形式化精確交換情形，再擴展到誤差界。

## 18.3 實驗報告最低要求

任何「觀察到曲率」的計算報告至少提供：

- 基底與纖維；
- 閉路生成規則；
- 傳輸方向與順序；
- 差度型別；
- 尺度正規化；
- 可逆性測試；
- 規範處理；
- 投影層；
- 誤差證書；
- 對照的平坦系統；
- 閉路反向與重參數化測試。

---

# 第十九章　開放問題

1. 一般非線性纖維中，holonomy 的最佳不變表示是什麼？
2. 非對稱差度下，如何定義方向性曲率而不錯失反向信息？
3. 不可逆傳輸是否存在自然的「可逆核心＋耗散殘差」分解？
4. 什麼條件使離散面 holonomy 在精細化下收斂到光滑曲率？
5. 如何從有限閉路樣本估計未觀察方向的曲率上界？
6. 曲率比較映射 $$\mathcal J_{\lambda\mu}$$ 應由投影、伴隨函子還是最佳傳輸建立？
7. 查詢相對曲率與本體完整 holonomy 之間如何建立充分查詢族？
8. 如何處理基底與纖維本身都隨精細化改變的情況？
9. 非平凡 global holonomy 與「投影不可封閉」如何區分？
10. 何種閉路族足以生成全部 holonomy，而又保持可計算？
11. 在無限維流形中，差度小閉路極限需要哪些弱黎曼條件？
12. 如何防止尺度量尺选择使任意系統都被人為製造成無限曲率？
13. 曲率譜、閉路複雜度與查詢複雜度是否存在可證關係？
14. 高階閉路差應使用範疇、2-群、∞-群胚還是算子塔表達？
15. 無限曲率主定義應以算子無界、純量無界、投影不一致或其合取為核心？

---

# 第二十章　結論

本文建立了一個不依賴圓、角度或三維想像的廣義曲率語法。它從最基本的資料開始：

$$
\text{基底}
+
\text{纖維}
+
\text{路徑}
+
\text{傳輸}
+
\text{差度}
+
\text{閉路}
+
\text{尺度}.
$$

沿閉路傳輸得到 holonomy：

$$
H_\gamma.
$$

以差度測量狀態或算子偏離：

$$
D_\gamma(v)
=
\Delta(v,H_\gamma v),
$$

再依閉路尺度正規化：

$$
K_\gamma(v)
=
\frac{D_\gamma(v)}{\sigma(\gamma)}.
$$

但本文拒絕把這個式子直接當作萬用曲率。要成為曲率合格資料，還必須檢查：

- 基底是否真正閉合；
- 傳輸是否可逆；
- 耗散是否被分離；
- 差度是否與傳輸相容；
- 純量是否規範不變；
- 投影與數值誤差是否受控；
- 不同尺度是否有合法比較映射。

因此，本文的最終定義不是「閉路後不同就是曲率」，而是：

$$
\boxed{
\begin{aligned}
\text{廣義曲率}
={}&
\text{閉合基底上的傳輸 holonomy}\\
&+
\text{有型差度}\\
&+
\text{尺度正規化}\\
&+
\text{規範與可逆性控制}\\
&+
\text{投影／精細化證書}.
\end{aligned}
}
$$

這個定義保留了標準微分幾何的核心：曲率與小閉路平行傳輸的非閉合密切相關；同時也允許離散圖、索引幾何、投影計算與一般狀態系統使用同一語法。但它沒有把所有路徑依賴冒充為幾何，也沒有把純量差度冒充為完整曲率張量。

至此，「無限曲率」終於有了可以合法承載無界性的對象：

- holonomy 算子；
- 閉路差譜；
- 尺度化曲率泛函；
- 精細化曲率族；
- 投影 holonomy 殘差；
- 高階閉路傳輸。

下一篇將正式處理：

# 《無限曲率形式論：精細化無界、投影不可封閉與高階遞歸》

其任務不再是想像「無限彎曲的空間」，而是精確分類：

> 究竟是哪一個曲率資料、沿哪一個尺度或精細化方向、以何種無界或不可一致控制的方式，超出所有有限層的封閉能力？

---

# 參考文獻與理論接口

## 內部文件

1. Neo.K，《差合化三位一體本體論：Cl 的完整動力學》。
2. Neo.K × Aletheia，《索引幾何學：同一性拓樸微積分中的座標、投影與可計算性》。
3. Neo.K × Aletheia，《投影計算論：無限維索引的有限表示、收斂與失真證書》。
4. Neo.K × Aletheia，《索引動力學：重索引、結構漂移與回饋控制》。
5. Neo.K × Aletheia，《精細化算子論：區分度、解析度、維度與可回溯提升》。

## 外部學術接口

1. Ambrose–Singer holonomy theorem：曲率與 holonomy Lie 代數的關係。
2. Erlend Grong and Pierre Pansu, “Asymptotic Expansions of Holonomy,” arXiv:1701.02570。
3. Marco Vákár, “Principal Bundles and Gauge Theories,” arXiv:2110.06334。
4. Jean-Pierre Magnot, “Ambrose-Singer Theorem on Diffeological Bundles and Complete Integrability of the KP Equation,” arXiv:1007.3543。
5. Daniel Berwick-Evans, Anil Hirani, and Mark Schubel, “Discrete Vector Bundles with Connection,” arXiv:2104.10277。
6. Aristophanes Dimakis and Folkert Müller-Hoissen, “Discrete Riemannian Geometry,” arXiv:gr-qc/9808023。
7. H. García-Compeán and O. Obregón 等離散／非交換聯絡與曲率相關工作。
8. Regge calculus 與分片平坦幾何中的 deficit angle／hinge holonomy。
9. Holonomy、monodromy、local systems 與 flat connections 的標準微分幾何接口。

---

# 版本維護

## v0.1 已完成

- 曲率、holonomy、torsion、monodromy、hysteresis、耗散與投影殘差解歧；
- 廣義傳輸—差度系統；
- holonomy 算子、狀態差、算子差與閉路差譜；
- 尺度正規化；
- 曲率資格五檢；
- 路徑無關、零差、反向與複合閉路命題；
- 光滑小閉路極限；
- Ambrose–Singer 接口與適用限制；
- 離散圖／面曲率；
- 不可逆耗散診斷；
- 投影 holonomy 殘差；
- 精細化跨層比較；
- 平坦性層級；
- 差—合—化重新歸位；
- 任務相對曲率；
- 曲率證書；
- 無限曲率直接接口；
- Python／Lean 4 路線。

## v0.2 待補

- 對稱、非對稱與集合值差度的完整分類；
- 光滑極限的嚴格符號、方向與係數約定；
- torsion 的獨立差度接口；
- 全域 holonomy 與局部曲率的分解條件；
- 離散曲率收斂定理的文獻補強；
- 規範不變純量的分類；
- 不可逆通道的可逆核心模型；
- 多精細層閉路比較實驗；
- Lean 4 基礎形式化；
- 與下一篇無限曲率型譜的定義逐條對接。

---

*EML-DBCT-2026-v0.1 · 曲率不是一個角度，而是經過型別、尺度、規範、可逆性與投影檢查後的閉路非閉合結構。*

**EOF**
