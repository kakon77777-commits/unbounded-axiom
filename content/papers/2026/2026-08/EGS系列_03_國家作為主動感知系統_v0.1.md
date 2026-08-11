# 03｜國家作為主動感知系統
## 觀察、注意力、決策、行動與回饋的治理閉環
### The State as an Active Perception System: Observation, Attention, Decision, Action, and Feedback

**系列**：有效治理空間與政治尺度  
**篇次**：03 / 12  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-07  
**版本**：v0.1  
**狀態**：探索性模型論文／待驗證假說  
**前置論文**：  
- 01｜異質地形下的有效治理空間模型（EGS-HT）  
- 02｜通信成本與帝國尺度：從治理延遲到政治有效距離  

**研究性質**：本文提出一個跨政治學、組織理論、控制論與主動感知的統一模型。本文不主張國家具有單一意識、人格或統一認知主體；「國家作為主動感知系統」是一個功能性與計算性抽象，用於描述分散式制度如何選擇資訊、分配注意、形成決策並改變環境。

---

## 摘要

政治學通常把國家能力拆解為稅收、軍事、法律執行、官僚體系、資訊能力與公共服務等不同面向，但較少以統一的感知—注意—決策—行動閉環描述它們之間的共同結構。本文提出「國家作為主動感知系統」（State as Active Perception System, SAPS）模型：國家並非被動接收完整世界資訊，也無法直接操作真實社會狀態；它只能透過人口登記、統計、地圖、地方官員、警察、情報、傳媒、稅務資料與其他感測通道，取得部分、延遲且可能失真的觀察，再以有限政治注意力選擇其中一部分進入決策，最後透過行政、法律、財政、警務、軍事或基礎設施行動改變環境，並再次觀察結果。

此模型將治理表示為：

$$
S_t
\rightarrow
O_t
\rightarrow
A_t
\rightarrow
B_t
\rightarrow
D_t
\rightarrow
X_t
\rightarrow
S_{t+1}
\rightarrow
O_{t+1},
$$

其中 $S_t$ 為真實社會狀態， $O_t$ 為可觀察資訊， $A_t$ 為注意力分配， $B_t$ 為內部信念或狀態估計， $D_t$ 為決策， $X_t$ 為政策與執行行動。國家能力因此不只取決於「知道多少」，而取決於能否主動決定「還需要知道什麼」、「下一步應觀察哪裡」、「哪些資訊值得驗證」，以及「哪個行動能同時改變世界並改善下一輪資訊」。

本文進一步定義感知覆蓋、可讀性、注意力頻寬、觀察誤差、狀態估計誤差、政策選擇延遲、執行頻寬與回饋閉合率，並提出「治理盲區」、「注意力稀釋」、「模型化失真」、「感知—行動脫鉤」與「政策感測行動」等概念。本文特別強調：提高國家可讀性並不必然提高治理品質。過度簡化真實社會以追求可讀性，可能降低狀態估計的真實度；因此，高容量治理並非最大化觀察量，而是提高任務相關資訊的可用性、驗證性與行動適配性。

本文最核心的命題為：

$$
\boxed{
\text{Effective Governance}
\neq
\text{More Information}
}
$$

而更接近：

$$
\boxed{
\text{Effective Governance}
=
\text{Task-relevant sensing}
+
\text{attention allocation}
+
\text{state estimation}
+
\text{timely action}
+
\text{closed-loop correction}.
}
$$

---

# 1. 問題：國家真的「看得到」自己的領土嗎？

在現代地圖上，一個國家的疆界似乎非常清楚。

然而「疆界存在」不代表中央知道疆界內發生了什麼。

對時間 $t$ 的真實社會狀態，記為：

$$
S_t.
$$

它可能包含：

- 人口；
- 財產；
- 生產；
- 交易；
- 健康；
- 地方衝突；
- 犯罪；
- 軍事活動；
- 社會關係；
- 地方政治；
- 基礎設施；
- 氣候與災害；
- 非正式制度。

任何治理系統都不可能直接取得完整：

$$
S_t.
$$

它只能透過觀察算子：

$$
\mathcal O_t
$$

得到：

$$
O_t
=
\mathcal O_t(S_t)
+
\eta_t,
$$

其中：

$$
\eta_t
$$

代表：

- 測量誤差；
- 遺漏；
- 延遲；
- 錯誤報告；
- 欺瞞；
- 分類失真；
- 制度盲區。

因此第一個基本區分是：

$$
\boxed{
S_t
\neq
O_t.
}
$$

真實社會不等於國家看到的社會。

---

# 2. 可讀性：國家能力的資訊基礎

政治學已有「legibility」概念，描述國家對人民及其活動具有多大程度的可觀察性、可分類性與可處理性。

在本文中，定義區域 $x$ 的治理可讀性：

$$
L(x,t)\in[0,1].
$$

 $L$ 越高，代表政治系統越能可靠取得該區域的：

- 人口；
- 財產；
- 身分；
- 生產；
- 法律事件；
- 行政狀態。

但：

$$
L\uparrow
$$

並不必然意味：

$$
\text{truth accuracy}\uparrow.
$$

因為可讀性通常需要分類、標準化與壓縮。

因此本文區分：

$$
L_{\mathrm{admin}}
$$

與：

$$
L_{\mathrm{reality}}.
$$

前者表示「容易被制度讀取」，後者表示「對真實世界的描述保真度」。

可能存在：

$$
L_{\mathrm{admin}}\uparrow
\quad\text{但}\quad
L_{\mathrm{reality}}\downarrow.
$$

這是治理模型必須避免的一個核心陷阱。

---

# 3. 國家不是全知，而是有限感知系統

設國家在時間 $t$ 的總可用觀察容量：

$$
B_O(t)<\infty.
$$

即使真實世界產生資訊流：

$$
I_S(t)
$$

只要：

$$
I_S(t)>B_O(t),
$$

就必須捨棄、壓縮或延遲部分資訊。

因此：

$$
\boxed{
\text{World Information}
>
\text{State Observation Capacity}
}
$$

在複雜社會通常是常態。

國家因此必須建立：

- 統計；
- 報表；
- 分類；
- 行政層級；
- 地方代理；
- 事件警報；
- 優先級；
- 例外上報制度。

這些機制本質上都是：

$$
\boxed{
\text{information compression mechanisms}.
}
$$

---

# 4. 注意力：看到不等於處理

即使資訊成功進入中央系統，也不代表它會成為政策問題。

設觀察集合為：

$$
O_t=\{o_1,o_2,\ldots,o_n\}.
$$

國家在時間 $t$ 的政治／行政注意力預算為：

$$
B_A(t)<\infty.
$$

對各資訊分配：

$$
a_i(t)\ge0
$$

且：

$$
\sum_{i=1}^{n}a_i(t)\le B_A(t).
$$

真正進入決策的有效資訊為：

$$
O_t^{\mathrm{eff}}
=
\mathcal A(O_t,\mathbf a_t).
$$

因此：

$$
\boxed{
\text{Observed}
\neq
\text{Attended}.
}
$$

這一區分是本文最重要的模型擴展之一。

---

# 5. 治理注意力稀釋

若政治體的：

- 人口；
- 領土；
- 政策領域；
- 事件頻率；
- 法規；
- 行政責任；

持續增加，

但：

$$
B_A
$$

沒有同比增加，

則每一治理問題平均可取得的注意力：

$$
\bar a
=
\frac{B_A}{N_{\mathrm{relevant}}}
$$

下降。

因此：

$$
N_{\mathrm{relevant}}\uparrow
\Rightarrow
\bar a\downarrow.
$$

本文稱為：

# Governance Attention Dilution  
# 治理注意力稀釋

這意味著政治尺度的上限不只受到通信與物流約束，也受到：

$$
\boxed{
\text{attention bandwidth}.
}
$$

---

# 6. 行政階層作為注意力壓縮器

為解決：

$$
N_{\mathrm{citizen}}\gg B_A,
$$

國家通常不直接建立：

$$
C
\rightarrow
P_1,P_2,\ldots,P_N.
$$

而建立：

$$
C
\rightarrow
M_1,\ldots,M_k
\rightarrow
L_1,\ldots,L_m
\rightarrow
P.
$$

其中：

- $C$ ：中央；
- $M$ ：中層行政；
- $L$ ：地方行政；
- $P$ ：人口與基層事件。

因此行政層級的一個重要功能可以寫成：

$$
\boxed{
\text{many states}
\rightarrow
\text{compressed summaries}
\rightarrow
\text{central attention}.
}
$$

即：

$$
\mathcal C:
S_{\mathrm{local}}
\rightarrow
\hat S_{\mathrm{regional}}.
$$

這不是只有權力分層，也是一種資訊處理架構。

---

# 7. 但壓縮會失真

任何壓縮都可能丟失資訊。

定義地方真實狀態：

$$
S_L
$$

與中央收到的摘要：

$$
\hat S_C.
$$

資訊失真：

$$
\epsilon_C
=
d(S_L,\hat S_C).
$$

增加行政層級可能降低：

$$
B_A
$$

負荷，

但同時提高：

$$
\epsilon_C.
$$

因此存在一個基本 trade-off：

$$
\boxed{
\text{Compression Efficiency}
\leftrightarrow
\text{Reality Fidelity}.
}
$$

治理架構不是層級越少越好，也不是越多越好。

---

# 8. 從被動觀察到主動感知

傳統模型常默認：

$$
S_t
\rightarrow
O_t.
$$

也就是世界發生事件，國家被動接收資訊。

但主動感知模型認為：

> 行動者可以選擇如何觀察世界，以降低不確定性。

因此加入感知政策：

$$
\pi_O.
$$

下一個觀察行動：

$$
q_{t+1}
=
\pi_O(B_t,U_t),
$$

其中：

- $B_t$ ：目前信念；
- $U_t$ ：不確定性。

例如國家可以主動：

- 派巡察官；
- 做人口普查；
- 審計；
- 重新測量土地；
- 增加感測器；
- 要求地方補件；
- 設立調查委員會；
- 派情報人員；
- 抽樣調查；
- 實地訪視。

因此：

$$
\boxed{
\text{Observation itself is a policy choice}.
}
$$

---

# 9. 主動感知的最小形式

令國家對世界狀態的信念為：

$$
B_t(S).
$$

其不確定性為：

$$
H(B_t).
$$

觀察行動 $q$ 的價值可以寫成預期信息增益：

$$
IG(q)
=
H(B_t)
-
\mathbb E
\left[
H(B_{t+1}\mid q)
\right].
$$

若觀察也有成本：

$$
C_O(q),
$$

則最簡化的主動感知策略為：

$$
q^*
=
\arg\max_q
\left[
IG(q)
-
\lambda C_O(q)
\right].
$$

這意味着有限治理系統不應「什麼都查」。

而應選擇：

$$
\boxed{
\text{highest-value next observation}.
}
$$

---

# 10. 國家的真正狀態估計

國家收到觀察：

$$
O_t
$$

並結合先前信念：

$$
B_{t-1}
$$

得到新的狀態估計：

$$
B_t
=
\mathcal U
(
B_{t-1},
O_t
).
$$

因此政策決策並不是對：

$$
S_t
$$

直接做函數，

而是：

$$
D_t
=
\pi_D(B_t).
$$

如果：

$$
B_t
$$

錯了，

再聰明的決策函數：

$$
\pi_D
$$

也可能產生錯誤行動。

因此：

$$
\boxed{
\text{Decision Quality}
\le
f(\text{State Estimation Quality}).
}
$$

---

# 11. 模型化國家與真實社會

中央通常需要建立一個可計算世界模型：

$$
M_t.
$$

例如：

- 人口模型；
- 稅收模型；
- 經濟模型；
- 犯罪模型；
- 軍事情報圖；
- 土地資料；
- 風險分級。

於是：

$$
M_t
=
\mathcal M(O_t).
$$

但：

$$
M_t
\neq
S_t.
$$

這一點是 SAPS 模型非常重要的安全條件：

$$
\boxed{
\text{The state's model of society is not society itself}.
}
$$

若治理系統開始把模型當真實世界：

$$
M_t\equiv S_t,
$$

便可能產生：

# Model Substitution Failure  
# 模型替代失敗

即政策開始優化指標，而不是優化真實狀態。

---

# 12. 注意力不是平均分配

有限注意力意味著政治體必須形成：

$$
w_i(t)
$$

的優先權。

例如：

$$
w_{\mathrm{war}}
>
w_{\mathrm{road}}
$$

在戰爭時可能成立；

但災害時可能：

$$
w_{\mathrm{disaster}}
>
w_{\mathrm{routine}}.
$$

因此國家注意力是一個動態場：

$$
\mathbf w_t
=
(w_1,w_2,\ldots,w_n).
$$

可定義注意力分布熵：

$$
H_A(t)
=
-\sum_i
p_i(t)\log p_i(t),
$$

其中：

$$
p_i
=
\frac{a_i}{\sum_j a_j}.
$$

極低：

$$
H_A
$$

代表注意力高度集中。

極高：

$$
H_A
$$

代表注意力高度分散。

兩者都可能失敗。

---

# 13. 過度集中與過度分散

若：

$$
H_A\rightarrow0,
$$

國家高度聚焦少數事件。

優點：

- 快速集中資源；
- 危機反應強。

缺點：

- 其他領域形成盲區；
- 長期問題累積。

若：

$$
H_A\uparrow,
$$

注意力過度平均，

則：

$$
a_i
$$

可能都不足以跨越實際行動門檻。

因此存在任務依賴的最適注意力結構：

$$
H_A^*.
$$

不是：

$$
\min H_A
$$

也不是：

$$
\max H_A.
$$

---

# 14. 治理盲區

定義區域／問題 $i$ 的真實重要性：

$$
r_i
$$

與注意力：

$$
a_i.
$$

治理盲區可定義為：

$$
Z
=
\left\{
i:
r_i\ge r_{\min}
\land
a_i<a_{\min}
\right\}.
$$

即：

> 真正重要，但沒有被治理系統充分注意。

這種情況可能來自：

- 資料不存在；
- 層級阻隔；
- 中央偏好；
- 政治禁忌；
- 指標設計；
- 地理偏遠；
- 媒體不可見；
- 行政分類錯誤。

因此：

$$
\boxed{
\text{Governance Blind Spot}
\neq
\text{No Problem}.
}
$$

---

# 15. 事件顯著性與注意力偏誤

政治注意力並不只由真實重要性：

$$
r_i
$$

決定。

還受到顯著性：

$$
s_i
$$

影響。

可寫成：

$$
a_i
=
f(
r_i,
s_i,
I_i,
P_i,
M_i
),
$$

其中：

- $I_i$ ：制度入口；
- $P_i$ ：政治優先權；
- $M_i$ ：媒體／公共可見度。

因此可能出現：

$$
s_i\gg r_i
$$

卻得到大量注意力，

或：

$$
r_i\gg s_i
$$

卻被忽略。

這使政治注意力本身成為治理品質的一個獨立研究對象。

---

# 16. 從決策到行動

即使：

$$
B_t
$$

正確，

而：

$$
D_t
$$

也合理，

仍不代表政策產生效果。

令：

$$
X_t
=
\mathcal E(D_t,C_t),
$$

其中：

$$
C_t
$$

是執行能力。

若：

$$
C_t\rightarrow0,
$$

則：

$$
D_t
$$

可能只是紙面命令。

所以：

$$
\boxed{
\text{Decision}
\neq
\text{Action}
\neq
\text{Outcome}.
}
$$

完整鏈為：

$$
D_t
\rightarrow
X_t
\rightarrow
S_{t+1}.
$$

---

# 17. 感知—行動脫鉤

定義：

$$
K_{PA}
$$

為 perception-action coupling。

如果國家：

- 看得到問題；
- 有資料；
- 有報告；
- 有會議；

但無法採取行動，

則：

$$
K_{PA}\rightarrow0.
$$

反之，如果可以快速行動但資訊品質極差，也可能形成：

$$
\text{fast wrong action}.
$$

因此有效治理要求：

$$
\boxed{
O
\leftrightarrow
A
\leftrightarrow
D
\leftrightarrow
X
}
$$

保持足夠耦合。

---

# 18. 行動也可以是感知

主動感知最重要的推論之一是：

> 有些行動不只是改變世界，也是為了得到更多資訊。

例如：

- 小規模政策試點；
- 局部巡查；
- 抽樣稽核；
- 小區域軍事偵察；
- A/B 政策實驗；
- 階段性開放；
- 試行法規。

因此定義雙重用途行動：

$$
X_t^{DA}
$$

其效用：

$$
U(X)
=
U_{\mathrm{world}}(X)
+
\beta
U_{\mathrm{information}}(X).
$$

即：

$$
\boxed{
\text{Action}
=
\text{Intervention}
+
\text{Measurement}.
}
$$

這是 SAPS 與一般靜態國家能力模型的重要差異。

---

# 19. 政策試驗作為主動感知

假設政府不知道政策：

$$
p_1
$$

與：

$$
p_2
$$

哪一個更有效。

若直接全國推行：

$$
p_1
$$

風險極高。

可以先選：

$$
x_{\mathrm{pilot}}
$$

執行：

$$
p_1.
$$

取得：

$$
O_{t+1}.
$$

再更新：

$$
B_{t+1}.
$$

因此：

$$
\text{pilot}
\rightarrow
\text{observe}
\rightarrow
\text{update}
\rightarrow
\text{scale}.
$$

這就是治理層級的：

$$
\boxed{
\text{active experimentation}.
}
$$

---

# 20. 回饋閉合率

並非所有政策都有有效回饋。

定義：

$$
R_F
=
\frac{
N_{\mathrm{actions\ with\ verified\ feedback}}
}{
N_{\mathrm{total\ actions}}
}.
$$

若：

$$
R_F\rightarrow0,
$$

國家大量行動卻不知道結果。

這會使系統逐漸開環：

$$
\text{open-loop governance}.
$$

若：

$$
R_F\uparrow,
$$

則更接近：

$$
\text{closed-loop governance}.
$$

---

# 21. 開環治理與閉環治理

## 開環治理

$$
D_t
\rightarrow
X_t
$$

之後缺乏：

$$
O_{t+1}.
$$

此時政策可能長期持續，即使環境早已改變。

## 閉環治理

$$
O_t
\rightarrow
D_t
\rightarrow
X_t
\rightarrow
O_{t+1}.
$$

中央根據結果持續修正。

因此：

$$
\boxed{
\text{Adaptability}
\propto
R_F.
}
$$

---

# 22. 政治體作為多層感測網路

國家不是一個感測器。

更合理的是：

$$
\mathcal N_O
=
(V_O,E_O).
$$

節點可能包含：

- 官員；
- 地方政府；
- 稅務機關；
- 警察；
- 法院；
- 軍方；
- 醫院；
- 學校；
- 統計機構；
- 民間團體；
- 媒體；
- 市民回報；
- 數位感測器。

它們共同形成：

$$
\boxed{
\text{Distributed Observation Network}.
}
$$

因此國家感知能力不只取決於中央，而取決於整張網路。

---

# 23. 感測節點故障與系統性失真

若某節點：

$$
v_i
$$

有偏差：

$$
b_i,
$$

其報告為：

$$
o_i
=
s_i+b_i+\eta_i.
$$

若中央過度依賴該節點：

$$
w_i\gg0,
$$

則局部偏差可能放大成中央模型偏差。

因此：

$$
\boxed{
\text{sensor diversity}
}
$$

可能提高治理韌性。

例如：

$$
O_t
=
w_1O_{\mathrm{bureaucracy}}
+
w_2O_{\mathrm{statistics}}
+
w_3O_{\mathrm{inspection}}
+
w_4O_{\mathrm{citizens}}.
$$

多源交叉驗證可以降低單一代理人的資訊壟斷。

---

# 24. 主動注意力轉移

當目前狀態出現高不確定性區域：

$$
U_i(t)\uparrow,
$$

國家可以提高：

$$
a_i(t+1).
$$

即：

$$
a_i(t+1)
=
f(
a_i(t),
U_i,
R_i,
C_i
).
$$

因此治理注意力不是固定預算表，而應具有：

$$
\boxed{
\text{adaptive reallocation}.
}
$$

這類結構可以用於：

- 災害；
- 戰爭；
- 疫情；
- 金融危機；
- 地方暴力；
- 基礎設施故障。

---

# 25. 感知成本與治理深度

提高可讀性通常需要成本：

$$
C_L(L).
$$

而且：

$$
\frac{dC_L}{dL}>0.
$$

要從：

$$
L=0.8
$$

提高到：

$$
L=0.9
$$

可能比：

$$
0.2\rightarrow0.3
$$

昂貴得多。

因此不存在：

$$
L=1
$$

必然最優。

更合理的是：

$$
L^*
=
\arg\max_L
[
B_G(L)-C_L(L)-C_{\mathrm{privacy}}(L)-C_{\mathrm{distortion}}(L)
].
$$

這提醒模型不能把「國家看得越多越好」當作價值前提。

---

# 26. 可讀性與隱私的邊界

高可讀性：

$$
L\uparrow
$$

可能增加：

- 稅務能力；
- 救災定位；
- 政策精準度；
- 犯罪偵查。

但也可能增加：

- 監控；
- 權力濫用；
- 隱私侵蝕；
- 資訊集中風險。

因此：

$$
\boxed{
\text{State Capacity}
\neq
\text{Maximum State Visibility}.
}
$$

SAPS 是描述模型，而不是主張全知國家。

---

# 27. 國家感知與地方知識

中央資訊通常是壓縮與標準化的。

地方則可能具有：

$$
K_{\mathrm{local}}
$$

這類難以完全形式化的知識。

因此：

$$
K_{\mathrm{central}}
\neq
K_{\mathrm{local}}.
$$

理想治理可能不是完全取代地方知識，而是建立：

$$
\boxed{
\text{central abstraction}
+
\text{local high-resolution knowledge}.
}
$$

這也意味地方授權有一個資訊論理由，而不只是政治妥協。

---

# 28. 主動感知國家的完整模型

本文最終把國家表示為：

$$
\mathcal S_G
=
(
\mathcal O,
\mathcal A,
\mathcal B,
\mathcal D,
\mathcal X,
\mathcal F
).
$$

其中：

- $\mathcal O$ ：觀察系統；
- $\mathcal A$ ：注意力系統；
- $\mathcal B$ ：狀態估計／信念；
- $\mathcal D$ ：決策系統；
- $\mathcal X$ ：行動／執行系統；
- $\mathcal F$ ：回饋與驗證系統。

完整動態：

$$
O_t
=
\mathcal O(S_t,q_t),
$$

$$
A_t
=
\mathcal A(O_t,B_{t-1}),
$$

$$
B_t
=
\mathcal U(B_{t-1},A_t),
$$

$$
D_t
=
\pi_D(B_t),
$$

$$
X_t
=
\mathcal E(D_t),
$$

$$
S_{t+1}
=
\mathcal W(S_t,X_t),
$$

$$
q_{t+1}
=
\pi_O(B_t,U_t).
$$

最後形成：

$$
\boxed{
S_t
\rightarrow
O_t
\rightarrow
A_t
\rightarrow
B_t
\rightarrow
D_t
\rightarrow
X_t
\rightarrow
S_{t+1}
\rightarrow\cdots
}
$$

---

# 29. 與 EGS-HT 的結合

EGS-HT 已提出：

$$
\text{地形}
\rightarrow
\text{有效距離}
\rightarrow
\text{治理成本}.
$$

第 02 篇又加入：

$$
\tau_G.
$$

本文再加入：

$$
B_O,
\quad
B_A,
\quad
L,
\quad
\epsilon,
\quad
R_F.
$$

因此有效治理空間應進一步寫為：

$$
\Omega_G
=
\left\{
x:
\begin{array}{l}
d_{\mathrm{pol}}(x)<d_{\max}\\
\Lambda(x)<1\\
L(x)>L_{\min}\\
A(x)>A_{\min}\\
R_F(x)>R_{\min}
\end{array}
\right\}.
$$

這使「有效治理空間」從純空間—通信模型升級為：

$$
\boxed{
\text{spatial}
+
\text{informational}
+
\text{attentional}
+
\text{temporal}
+
\text{actionable}
}
$$

的多維控制域。

---

# 30. 初步命題群

## 命題 1：觀察不完備命題

$$
S_t\neq O_t.
$$

任何政治體都在部分觀察下治理。

## 命題 2：注意力瓶頸命題

$$
B_A<\infty.
$$

因此被觀察資訊不可能全部進入決策。

## 命題 3：行政壓縮命題

行政層級部分功能是將大量地方狀態壓縮為中央可處理表示。

## 命題 4：壓縮失真命題

資訊壓縮降低注意力成本，但可能提高真實狀態失真。

## 命題 5：主動感知命題

高能力治理系統不只是接收資訊，也會主動選擇下一個高價值觀察。

## 命題 6：感知—行動耦合命題

有效治理要求觀察、注意、決策、執行與回饋形成閉合循環。

## 命題 7：可讀性非單調命題

增加行政可讀性不保證治理品質單調上升。

## 命題 8：地方知識互補命題

中央標準化資訊與地方高解析知識可能是互補而非替代關係。

---

# 31. 可反駁預測

## 預測 A

在其他條件近似時，資訊可讀性更高的地區，國家稅務、法規與公共服務執行能力應更強。

## 預測 B

當中央政策領域數量快速增加但注意力與行政能力未同步增加時，政策遺漏與反應延遲應上升。

## 預測 C

行政層級過度增加時，中央資訊摘要與地方真實狀態之間的失真應提高。

## 預測 D

具備主動稽核、抽樣調查、政策試點與多源交叉驗證的治理系統，應比純被動報表體系更快修正模型錯誤。

## 預測 E

只有提高資料收集而不提高執行與回饋能力時，治理效果改善應有限。

## 預測 F

高度中央化資訊系統若壓低地方高解析知識的輸入，可能在高複雜度政策問題上產生更大的模型替代失敗。

---

# 32. 主要反論

## 32.1 國家不是單一 agent

正確。

本文的「agent」是功能抽象：

$$
\mathcal S_G
$$

實際上是多機構、多層級、多行動者的分散式系統。

因此更精確地說：

$$
\boxed{
\text{State}
=
\text{multi-agent active perception organization}.
}
$$

## 32.2 政治決策不是純資訊處理

正確。

權力、價值、利益、合法性與衝突無法被資訊模型取代。

本文只主張：

> 即使價值與利益固定，任何政治行動仍必須經過有限資訊、注意與行動管道。

## 32.3 高資訊能力可能導向威權監控

正確。

因此本文不把：

$$
L\uparrow
$$

直接視為規範性進步。

## 32.4 地方有時故意保持不可讀

正確。

不可讀性可能是：

- 自主；
- 隱私；
- 抵抗；
- 安全；
- 制度多樣性；

的來源。

因此最優可讀性是政治與制度問題，而不是純工程最大化。

---

# 33. 與既有研究的關係

本文與四條既有研究線相交：

### 33.1 Bounded Rationality

Herbert Simon 的有限理性傳統指出決策者的資訊、時間與計算能力有限。

本文將：

$$
\text{bounded rationality}
$$

擴展到：

$$
\text{bounded state cognition}.
$$

### 33.2 Organizational Attention

組織研究長期認為有限注意力促成階層、任務分工、控制系統與注意力導向機制。

本文將其移植至政治體。

### 33.3 State Legibility

國家能力研究指出國家對人民與活動的可讀性是監督與規則執行的重要資訊基礎。

本文進一步區分：

$$
\text{legibility}
\neq
\text{attention}
\neq
\text{actionability}.
$$

### 33.4 Active Perception

主動感知研究強調感知不是被動取得資料，而是目標導向地選擇感測位置、方式與下一步行動。

本文將此轉換為：

$$
\text{active governance sensing}.
$$

---

# 34. 結論

國家不是站在地圖上方、同時看見所有領土的全知觀察者。

更接近：

$$
\boxed{
\text{a distributed, bandwidth-limited, model-based active perception system}.
}
$$

它必須：

1. 選擇如何看；
2. 決定看什麼；
3. 壓縮大量地方資訊；
4. 建立世界模型；
5. 在不完整資訊下決策；
6. 把決策轉為行動；
7. 再觀察行動後的世界；
8. 修正自己的模型。

因此：

$$
\boxed{
\text{Territory Present}
\neq
\text{Territory Observed}
\neq
\text{Territory Attended}
\neq
\text{Territory Understood}
\neq
\text{Territory Acted Upon}
\neq
\text{Territory Controlled}.
}
$$

這使政治尺度問題不再只是：

> 國家有多大？

而變成：

> 一個有限感知、有限注意、有限計算與有限行動頻寬的組織，究竟能在多大的異質狀態空間內，持續維持可靠的閉環控制？

本文因此提出：

$$
\boxed{
\text{Effective Governance}
=
\text{Selective Perception}
+
\text{Attention}
+
\text{Estimation}
+
\text{Action}
+
\text{Feedback}.
}
$$

而不是：

$$
\text{Effective Governance}
=
\text{Maximum Information}.
$$

這也為下一篇奠定基礎：既然治理是一個有限資源的閉環系統，那麼中央集權、地方自治、代理治理、行政分層與聯邦結構，就可以被重新理解為不同條件下對：

$$
C_O,
C_A,
C_C,
C_V,
C_E,
C_{\mathrm{agency}}
$$

進行重新分配的**控制拓撲選擇**。

---

# 參考文獻

1. Simon, Herbert A. *Administrative Behavior*.
2. Simon, Herbert A. “A Behavioral Model of Rational Choice.”
3. Bajcsy, Ruzena. “Active Perception.” *Proceedings of the IEEE*, 1988.
4. Bajcsy, R., Aloimonos, Y., & Tsotsos, J. K. “Revisiting Active Perception.” 2016.
5. Lee, Melissa M. & Zhang, Nan. “Legibility and the Informational Foundations of State Capacity.” *The Journal of Politics* 79(1), 2017.
6. Scott, James C. *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*.
7. Mortensen, Peter B. “Political Attention and Public Policy: A Study of How Agenda Setting Matters.” *Scandinavian Political Studies* 33(4), 2010.
8. Jonaityte, Inga & Warglien, Massimo. “Attention and Organizations.” In *Routledge Handbook of Bounded Rationality*.
9. Chen, Huirong & Greitens, Sheena Chestnut. “Information Capacity and Social Order: The Local Politics of Information Integration in China.” *Governance*.
10. 後續需補：政治議程資料、政府回饋閉合率、行政層級信息失真、地方與中央資訊解析度比較。

---

# 版本註記

第 03 篇完成後，系列目前的理論鏈為：

$$
\boxed{
\text{Terrain}
\rightarrow
\text{Effective Distance}
\rightarrow
\text{Communication Latency}
\rightarrow
\text{Observation}
\rightarrow
\text{Attention}
\rightarrow
\text{State Estimation}
\rightarrow
\text{Decision}
\rightarrow
\text{Action}
\rightarrow
\text{Feedback}.
}
$$

下一篇：

**04｜政治組織作為控制成本的適應性解：中央、代理與地方自治的拓撲選擇**

將正式處理：

$$
\boxed{
\mathcal T^*
=
\arg\min_{\mathcal T}
C_{\mathrm{governance}}(\mathcal T)
}
$$

以及中央集權、分權、郡縣、封建、聯邦、總督制與間接統治為何可以被放進同一個控制拓撲框架。
