# 異質地形下的有效治理空間模型
## 從移動、感知、注意力、通信、行動到政治整合的統一框架
### Effective Governance Space under Heterogeneous Terrain (EGS-HT) — Model Paper v0.1

**版本**：v0.1  
**狀態**：探索性模型論文／待驗證假說  
**研究性質**：不保真（non-truth-preserving draft）；案例僅作候選解釋，不視為已證實因果關係。  
**核心問題**：為什麼幾何面積相近或差異巨大的政治空間，會形成完全不同的中央化、地方化、聯盟化與帝國化結構？

---

## 摘要

傳統歷史敘述容易把領土面積、地理位置、人口規模或制度名稱直接映射到政治整合程度，例如「領土大所以難以中央集權」、「山地多所以容易封建」、「平原廣所以容易形成帝國」。本文提出一個更弱、也更可檢驗的替代模型：政治體真正需要控制的不是抽象幾何面積，而是分布於異質空間上的人口、產出、節點、路徑、資訊、代理人與行動能力。幾何領土只有經過移動成本、觀察成本、注意力配置、通信延遲、行政抽取、軍事執行、定居形態與技術條件的共同轉換後，才成為「有效治理空間」。

本文提出 EGS-HT（Effective Governance Space under Heterogeneous Terrain）模型，將治理理解為一個持續閉合的感知—注意—決策—通信—行動—驗證迴路。若中央對區域的治理迴路速度低於地方事件的演化速度，或中央控制成本長期高於地方控制成本，而地方又能產生足夠剩餘以支持軍政節點，則地方化政治結構的相對收益可能上升。反之，交通、通信、物流、行政標準化、監督與軍事投射能力的提升，可能把原本彼此分離的政治空間重新「拉近」，使更高尺度的整合成為可行。

日本中世紀、歐亞草原政體與戰國至秦統一在本文中僅作三組探索性歷史映射。本文不主張日本山地直接造成封建，也不主張草原天然反封建，更不主張中國統一由地理必然導出。相反，三者被用來展示：相同的幾何面積概念，在不同移動方式、土地制度、人口固定性與治理技術下，可能對應完全不同的政治拓撲。

**關鍵詞**：有效治理空間、地形成本、政治距離、通信成本、注意力成本、主動感知、國家能力、地方化、封建、草原政體、秦統一、控制拓撲

---

# 1. 問題提出：平方公里不是治理單位

設政治體的名義領土為：

$$
\Omega \subset \mathbb{R}^2.
$$

其幾何面積為：

$$
A_{\mathrm{geo}} = \int_{\Omega} dA.
$$

傳統比較常把 $A_{\mathrm{geo}}$ 當成「國家大小」。然而兩塊同為 $1000\text{ km}^2$ 的土地，如果一塊是高人口密度河谷平原，另一塊是高山、森林與稀疏聚落，其治理意義顯然不同。

因此本文提出第一個基礎區分：

$$
\boxed{
A_{\mathrm{geo}}
\neq
A_{\mathrm{eff}}
}
$$

其中 $A_{\mathrm{eff}}$ 不是另一種物理面積，而是「在特定時代、技術、制度與行動能力下，可被某治理系統穩定感知、通信、到達、抽取、執行與驗證的有效空間」。

換言之：

> 平方公里是幾何單位，不是治理單位。

---

# 2. 從幾何距離到政治有效距離

對治理中心 $c$ 與區域 $x$ ，幾何距離記為：

$$
d_{\mathrm{geo}}(c,x).
$$

本文定義政治有效距離：

$$
d_{\mathrm{pol}}(c,x,t)
=
\inf_{\pi:c\rightarrow x}
\int_{\pi}
\kappa(s,t)\,ds
+
\Delta_{\mathrm{node}}(\pi,t),
$$

其中：

- $\pi$ ：治理中心至區域的可用路徑；
- $\kappa(s,t)$ ：沿路徑的綜合阻抗；
- $\Delta_{\mathrm{node}}$ ：關卡、行政層級、港口、驛站、代理人、邊界等節點延遲。

綜合阻抗可以寫成：

$$
\kappa
=
w_M\kappa_M
+
w_C\kappa_C
+
w_O\kappa_O
+
w_L\kappa_L
+
w_E\kappa_E
+
w_P\kappa_P,
$$

其中：

- $\kappa_M$ ：移動成本；
- $\kappa_C$ ：通信成本；
- $\kappa_O$ ：觀察與資訊取得成本；
- $\kappa_L$ ：物流與補給成本；
- $\kappa_E$ ：行政／軍事執行成本；
- $\kappa_P$ ：政治摩擦與代理成本。

權重 $w_i$ 依任務不同而變。傳遞一封命令、運一石糧食、派遣一支軍隊與派遣巡察官，對同一條道路產生的有效距離並不相同。

因此：

$$
\boxed{
d_{\mathrm{pol}}
=
f(
\text{terrain},
\text{actor},
\text{payload},
\text{technology},
\text{institution},
\text{time}
)
}
$$

並得到：

$$
\boxed{
\text{可到達}
\neq
\text{可運輸}
\neq
\text{可補給}
\neq
\text{可監督}
\neq
\text{可治理}
}
$$

---

# 3. 地形不是背景，而是治理成本場

將領土中每一位置 $x$ 定義一組治理成本向量：

$$
\mathcal{C}_G(x,t)
=
\left(
C_M,
C_C,
C_O,
C_A,
C_S,
C_X,
C_E
\right).
$$

分別代表：

- $C_M$ ：Movement，移動成本；
- $C_C$ ：Communication，通信成本；
- $C_O$ ：Observation，觀察與資訊取得成本；
- $C_A$ ：Attention，注意力與狀態維護成本；
- $C_S$ ：Settlement，定居與人口維持成本；
- $C_X$ ：Extraction，稅收、糧食與資源提取成本；
- $C_E$ ：Enforcement，行政與軍事執行成本。

此模型拒絕把「山地」、「平原」、「草原」、「海岸」視為固定政治效果。地形只改變成本場，而成本場如何轉化為政治制度，仍取決於行動主體與技術。

例如對徒步步兵：

$$
v_{\mathrm{mountain}} < v_{\mathrm{plain}},
$$

故相同路程 $d$ 下：

$$
T_{\mathrm{mountain}}
=
\frac{d}{v_{\mathrm{mountain}}}
>
\frac{d}{v_{\mathrm{plain}}}
=
T_{\mathrm{plain}}.
$$

但對騎馬、船運、鐵路、航空或數位通信，成本排序可能完全改變。

因此地形效果不是常數，而是條件函數：

$$
C_M
=
C_M(
G,
a,
p,
\tau,
\iota,
t
),
$$

其中：

- $G$ ：地形；
- $a$ ：行動者；
- $p$ ：載荷；
- $\tau$ ：任務；
- $\iota$ ：基礎設施；
- $t$ ：時代與技術狀態。

---

# 4. 國家治理是一個主動感知—行動閉環

本文將治理視為一種大型主動感知系統。

最小治理閉環為：

$$
\text{World State}
\rightarrow
\text{Observation}
\rightarrow
\text{Attention}
\rightarrow
\text{Decision}
\rightarrow
\text{Communication}
\rightarrow
\text{Action}
\rightarrow
\text{Verification}.
$$

中央並不能直接操作「真實國家狀態」 $S_t$ ，而只能操作經過感知與注意力過濾後的有效狀態：

$$
S_t^{\mathrm{eff}}
=
\mathcal{A}
\left(
\mathcal{O}(S_t),
\mathbf{w}_t
\right),
$$

其中：

- $\mathcal{O}$ ：觀察／報告機制；
- $\mathcal{A}$ ：注意力分配；
- $\mathbf{w}_t$ ：當期治理優先權。

因此：

$$
\boxed{
\text{Territory Present}
\neq
\text{Territory Observed}
\neq
\text{Territory Attended}
\neq
\text{Territory Controlled}
}
$$

即使資訊物理上可以抵達中央，中央仍可能因有限官僚、有限認知、有限決策頻寬與有限政治注意力而無法有效處理。

---

# 5. 治理閉環時間與事件演化時間

對區域 $x$ 定義治理反應時間：

$$
\tau_G(x)
=
\tau_{\mathrm{detect}}
+
\tau_{\mathrm{up}}
+
\tau_{\mathrm{verify}}
+
\tau_{\mathrm{decision}}
+
\tau_{\mathrm{down}}
+
\tau_{\mathrm{mobilize}}
+
\tau_{\mathrm{execute}}
+
\tau_{\mathrm{confirm}}.
$$

再定義地方事件從「可低成本處理」演化到「高成本或不可逆」的特徵時間：

$$
\tau_*(x).
$$

治理延遲比：

$$
\Lambda(x)
=
\frac{\tau_G(x)}
{\tau_*(x)}.
$$

若：

$$
\Lambda(x)\ll 1,
$$

則中央反應速度遠快於事件演化。

若：

$$
\Lambda(x)\approx 1,
$$

則區域進入治理臨界區。

若：

$$
\Lambda(x)>1,
$$

則出現結構性治理滯後。

因此中央化能否維持，至少部分依賴：

$$
\boxed{
\tau_G(x)<\tau_*(x)
}
$$

而非單純依賴地圖距離。

---

# 6. 注意力容量與治理稀釋

假設中央在時間 $t$ 的總有效治理注意力有限：

$$
B_A(t)<\infty.
$$

對各區域分配注意力 $a(x,t)$ ：

$$
\int_{\Omega} a(x,t)\,d\mu(x)
\le
B_A(t).
$$

其中 $d\mu(x)$ 不必是普通面積測度，而可依人口、產出、風險、軍事重要性等加權。

若領土擴張增加的不是單純面積，而是大量高複雜度、高異質性、高事件頻率節點，則治理注意力會被稀釋。

定義單位治理相關負荷：

$$
L_G(x,t)
=
\rho_P
+
\alpha_Y\rho_Y
+
\alpha_R\rho_R
+
\alpha_N\rho_N
+
\alpha_H H(x,t),
$$

其中：

- $\rho_P$ ：人口密度；
- $\rho_Y$ ：產出密度；
- $\rho_R$ ：資源密度；
- $\rho_N$ ：治理節點密度；
- $H$ ：狀態不確定性或局部複雜度。

故一片人口極稀疏、政治事件較少的巨大草原，不一定比一片聚落高度密集、權利結構複雜的狹小農業區需要更多日常治理注意力。

---

# 7. 控制對象：土地、人群、節點與流

政治體實際控制的對象可能不同。

定義控制對象向量：

$$
\mathbf{Q}
=
(Q_L,Q_P,Q_N,Q_F,Q_R),
$$

其中：

- $Q_L$ ：固定土地；
- $Q_P$ ：人口／群體；
- $Q_N$ ：城市、關口、水源、港口等節點；
- $Q_F$ ：商路、牲畜遷移、稅流、信息流等流；
- $Q_R$ ：可提取資源。

農業定居社會中，土地、人口與產出高度共址時，可能近似：

$$
Q_L
\approx
Q_P
\approx
Q_R.
$$

控制土地便接近控制人口與剩餘。

但在高流動牧業社會：

$$
Q_L
\not\approx
Q_P,
$$

固定控制每一平方公里土地的政治收益可能下降，而控制群體忠誠、季節性草場、水源、商路與外部交換節點的重要性上升。

因此不同文明的「領土」即使畫在同一種現代地圖上，也未必代表相同的治理對象。

---

# 8. 中央控制成本與地方控制成本

對區域 $x$ ，定義中央直接治理成本：

$$
C_{\mathrm{center}}(x)
$$

與地方自主治理成本：

$$
C_{\mathrm{local}}(x).
$$

再定義地方可支撐軍政組織的剩餘：

$$
S_{\mathrm{local}}(x).
$$

地方化壓力可暫定義為：

$$
\Phi(x)
=
\frac{
C_{\mathrm{center}}(x)
}{
C_{\mathrm{local}}(x)
}
\cdot
S_{\mathrm{local}}(x)
\cdot
R_{\mathrm{defense}}(x),
$$

其中 $R_{\mathrm{defense}}$ 表示地方防守與抗中央介入的相對優勢。

當：

$$
\Phi(x)\uparrow,
$$

地方政權、領主、自治共同體或中介代理的制度吸引力可能增加。

但這不等價於「必然封建」。實際制度仍取決於繼承規則、軍事組織、合法性、財產制度、宗教組織、國際競爭與歷史路徑。

---

# 9. 有效治理強度與有效治理空間

對區域 $x$ 定義標準化治理強度：

$$
\chi(x,t)
=
O(x,t)
A(x,t)
K(x,t)
E(x,t)
V(x,t),
$$

其中各項均標準化至 $[0,1]$ ：

- $O$ ：觀察能力；
- $A$ ：注意力覆蓋；
- $K$ ：通信與協調能力；
- $E$ ：執行能力；
- $V$ ：驗證與回饋能力。

若任一環節接近零：

$$
\chi(x,t)\rightarrow 0.
$$

因為「知道但不能做」、「能做但不知道」、「收到命令但無法驗證」都不足以形成完整治理。

有效治理空間定義為：

$$
\Omega_G(t;\theta)
=
\left\{
x\in\Omega:
\chi(x,t)\ge\theta
\land
\Lambda(x,t)<1
\right\},
$$

其中 $\theta$ 為最低治理強度門檻。

進一步可定義治理加權規模：

$$
G_{\mathrm{eff}}(t)
=
\int_{\Omega}
\rho_G(x,t)
\chi(x,t)
\,dA,
$$

其中 $\rho_G$ 是人口、產出、戰略節點與政治重要性的綜合權重。

因此：

$$
\boxed{
\text{Political Size}
\neq
\text{Geographical Area}
}
$$

政治尺度更接近：

$$
\boxed{
\text{Governable Weighted State Space}
}
$$

---

# 10. 初步命題

## 命題一：有效距離命題

在其他條件相同時，政治整合程度與幾何距離之間不存在必然單調關係；真正限制治理的是能力條件化的有效距離。

$$
d_{\mathrm{geo},1}<d_{\mathrm{geo},2}
$$

不保證：

$$
d_{\mathrm{pol},1}<d_{\mathrm{pol},2}.
$$

---

## 命題二：異質成本命題

同等面積的不同地形不具有同等治理權重。

$$
A_1=A_2
$$

不推出：

$$
C_G(A_1)=C_G(A_2).
$$

---

## 命題三：控制閉環命題

長期穩定統治要求治理感知—行動閉環相對於主要擾動具有足夠速度。

$$
\tau_G<\tau_*
$$

是有效控制的重要條件之一。

---

## 命題四：地方化相對收益命題

當中央控制成本顯著高於地方控制成本，而地方剩餘足以支持持續軍政組織時，地方化制度的相對收益上升。

$$
\frac{C_{\mathrm{center}}}{C_{\mathrm{local}}}\uparrow
\quad\land\quad
S_{\mathrm{local}}\uparrow
\Rightarrow
P(\text{localization})\uparrow
$$

此式為方向性假說，而非決定律。

---

## 命題五：技術壓縮政治空間命題

交通、通信、物流、監督與行政標準化技術可降低政治有效距離：

$$
\frac{\partial d_{\mathrm{pol}}}{\partial T_{\mathrm{gov}}}<0
$$

在一定條件下，它們可能造成政治整合的相變：

$$
\Omega_G(t_1)
\subset
\Omega_G(t_2).
$$

---

## 命題六：控制對象依賴命題

土地固定性越低、人口與產出越可移動，則「固定土地的逐區域直接治理」越不必然是最有效的政治組織形式。

---

# 11. 歷史映射 A：所謂「日本悖論」

本文暫稱以下問題為「日本悖論」：

> 為什麼一個幾何面積相對有限的島國，在中世紀仍長期形成高度地方化、領主化與多層權利結構，而不是因面積較小便自然形成穩定的單層中央直接治理？

此名稱為本文模型內部術語，不宣稱是既有史學概念。

日本約四分之三國土為山地與丘陵，人口與農業高度集中於有限低地。此事只證明其空間高度異質，不能直接證明封建形成。

更合理的候選鏈為：

$$
\text{rugged terrain}
\rightarrow
\text{discontinuous productive lowlands}
\rightarrow
\text{heterogeneous transport/control costs}
$$

再與：

$$
\text{shōen land rights}
+
\text{absentee proprietors}
+
\text{warrior stewards}
+
\text{local military capacity}
$$

共同作用。

日本中世紀莊園制度使土地權利、稅收權與行政監督形成複雜分層；地頭、守護與地方武士的崛起進一步改變了中央與地方之間的控制結構。故「地形造成封建」是過強命題；較弱的模型是：

$$
\boxed{
\text{terrain-induced cost structure}
\times
\text{land institutions}
\times
\text{military organization}
\rightarrow
\text{localization incentives}
}
$$

### 可反駁條件

若未來研究顯示：

1. 日本主要政治碎片化區域與有效交通障礙無系統關係；
2. 控制其他制度條件後，地形對地方自主程度沒有可辨識影響；
3. 中央治理成本在關鍵時期並未因山地、交通與信息結構而顯著增加；

則本模型中的日本地形機制應被削弱或刪除。

---

# 12. 歷史映射 B：草原為何不是「面積越大越封建」

歐亞草原提供相反測試。

其幾何面積巨大，但騎馬與牧業移動可以大幅降低特定行動者的移動成本：

$$
C_M^{\mathrm{horse}}
\ll
C_M^{\mathrm{foot}}
$$

同時，牧業人口、牲畜與季節性活動具有較高空間流動性，使控制對象從固定土地部分轉向：

$$
\text{people}
+
\text{herds}
+
\text{routes}
+
\text{water}
+
\text{alliances}.
$$

以匈奴為例，既有研究曾將其描述為：對外可高度集中地進行戰爭、外交與資源取得，內部則保留較聯盟式、部族式的權力結構。

因此草原案例顯示：

$$
\boxed{
\text{Huge Area}
\not\Rightarrow
\text{High Land-Parcel Governance Demand}
}
$$

而且：

$$
\boxed{
\text{Political Centralization}
\text{ can coexist with }
\text{internal decentralization}
}
$$

政治中央化本身也必須按任務拆分：外交、軍事動員、稅收、司法、土地管理與日常行政可能具有完全不同的中央化程度。

---

# 13. 歷史映射 C：秦統一不是「平原自然長成帝國」

本文拒絕以下強敘事：

$$
\text{China geography}
\Rightarrow
\text{inevitable unified empire}.
$$

戰國長期存在本身已表明，大尺度政治整合並非自動出現。

較弱的候選解釋是：在長期國家競爭中，秦逐漸建立足以跨越更多區域治理門檻的軍事、行政、物流與標準化能力。

可把每一區域的治理需求表示為：

$$
R_i.
$$

秦在時間 $t$ 的治理能力為：

$$
C_{\mathrm{Qin}}(t).
$$

當：

$$
C_{\mathrm{Qin}}(t)\ge R_i,
$$

該區域才進入更穩定的直接治理可能集合。

近年的秦研究顯示，其統一戰爭已伴隨跨行政區域的物流與財政網路；帝國建立後又大量依賴文書行政、標準化、官僚監督、道路與水運網路。

因此秦統一可以暫時建模為：

$$
\boxed{
\text{military victory}
+
\text{logistics}
+
\text{bureaucracy}
+
\text{standardization}
+
\text{communication}
+
\text{enforcement}
}
$$

共同把：

$$
d_{\mathrm{pol}}
$$

與：

$$
\tau_G
$$

壓低至可維持更大尺度治理的區間。

這不是秦成功的完整因果解釋，而是一個可被進一步測量的機制假說。

---

# 14. 「帝國」不是領土大小，而是高尺度閉環能力

由前述模型可得到一個更一般的定義候選：

> 帝國化不是單純佔有更多土地，而是某治理系統取得跨越多種異質區域，持續閉合觀察、注意、通信、抽取、執行與驗證迴路的能力。

因此帝國尺度可寫成：

$$
I_G
=
F(
\Omega_G,
B_A,
T_G,
L_G,
E_G,
I_G^{\mathrm{inst}}
).
$$

它至少依賴：

- 有效治理空間；
- 中央注意力容量；
- 交通／通信技術；
- 物流能力；
- 執行能力；
- 制度壓縮與代理能力。

由此可解釋為何：

- 大國不一定是帝國；
- 小國不一定容易中央化；
- 巨大草原可形成高機動聯盟帝國；
- 山地國家也可以在新技術下高度中央化；
- 同一地理空間在不同時代可支撐完全不同的政治尺度。

---

# 15. 模型的重要非結論

為避免模型退化成地理決定論，本文明確聲明以下內容**不是**本模型結論：

### 非結論一

$$
\text{mountains}\Rightarrow\text{feudalism}
$$

不成立。

### 非結論二

$$
\text{plains}\Rightarrow\text{empire}
$$

不成立。

### 非結論三

$$
\text{large territory}\Rightarrow\text{decentralization}
$$

不成立。

### 非結論四

$$
\text{fast communication}\Rightarrow\text{centralization}
$$

也不必然成立。

監督成本下降後，中央也可能更放心授權地方，使「中央監測＋地方決策」成為穩定解。

### 非結論五

$$
\text{Qin victory}\Rightarrow\text{geographic destiny}
$$

不成立。

---

# 16. 可檢驗預測

EGS-HT 模型至少產生以下可實證化預測。

## 預測 1：等面積異質性

在控制人口、制度與技術後，具有更高路徑阻抗與節點分割度的區域，中央直接治理成本應較高。

---

## 預測 2：交通技術的非線性效果

新道路、運河、鐵路或高速通信的政治效果不應只與總里程相關，而應與其是否連接關鍵瓶頸節點相關。

若某條新路消除一個拓撲割點，則可能出現：

$$
\Delta G_{\mathrm{eff}}
\gg
\Delta A_{\mathrm{infrastructure}}.
$$

---

## 預測 3：通信與執行分離

如果通信成本大幅下降，但物流與執行成本不變，則中央的「知情能力」會提升，但完整治理能力未必同比提升。

---

## 預測 4：移動人口的不同政治拓撲

人口與產出越可移動，政治控制越可能依賴群體、聯盟與流節點，而非固定土地的逐區塊行政。

---

## 預測 5：地方剩餘與碎片化

在中央控制成本較高的條件下，若地方剩餘足以支持軍事與行政組織，地方政治自主化的可能性應上升。

---

## 預測 6：國家能力投資的空間壓縮

行政標準化、物流網路與監督能力增強後，同一幾何距離對中央而言應變得更「近」。

---

# 17. 對抗論點與反例池

模型未來必須主動接受以下反例。

## 17.1 高山但高度中央化

例如某些山地帝國若能維持強中央治理，表示地形成本可被道路、馱運體系、行政節點、宗教合法性或軍事制度抵消。

## 17.2 平原但長期碎片化

若廣闊平原仍持續多國競爭，表示低移動成本並不足以造成統一。

## 17.3 日本後來重新中央化

日本地形並未改變，但政治整合程度發生巨大變化，因此地形只能是條件變量，不可能是充分原因。

## 17.4 蒙古帝國

超大尺度統一反而發生於草原世界，支持「高機動降低某些有效距離」，同時迫使模型處理征服能力與日常行政能力的差異。

## 17.5 海洋帝國

海洋在徒步模型中是障礙，在成熟航海技術下卻可能成為低成本高速路徑，因此「障礙」本身依賴技術。

---

# 18. 未來實證化方法

## 18.1 GIS 有效距離

以歷史地形、坡度、河流、道路、航路建立成本表面：

$$
d_{\mathrm{cost}}(i,j)
=
\operatorname{least-cost-path}(i,j).
$$

再比較行政邊界、地方割據、軍事反應時間與稅收能力。

---

## 18.2 歷史旅行時間

重建：

- 驛站速度；
- 徒步速度；
- 馬匹速度；
- 船運速度；
- 季節變化；
- 道路品質。

得到：

$$
T_{ij}(t).
$$

---

## 18.3 信息延遲資料

使用奏報、文書、軍令、驛傳、官員巡查等史料估算：

$$
\tau_{\mathrm{up}},
\quad
\tau_{\mathrm{down}},
\quad
\tau_{\mathrm{verify}}.
$$

---

## 18.4 地方剩餘

使用田賦、人口、糧產、土地制度與軍役資料估算：

$$
S_{\mathrm{local}}.
$$

---

## 18.5 政治拓撲

把政治體表示成多層網路：

$$
\mathcal{G}
=
(
V,
E_M,
E_C,
E_F,
E_A
),
$$

其中：

- $E_M$ ：軍事連結；
- $E_C$ ：通信連結；
- $E_F$ ：財政連結；
- $E_A$ ：行政連結。

比較不同時期的中心性、模組度、割點與平均有效距離。

---

# 19. 可被推翻的核心版本

為使理論具有最低可證偽性，本文將核心主張壓縮為：

$$
\boxed{
\text{Observed Political Scale}
=
F(
\text{effective distance},
\text{governance-loop speed},
\text{attention capacity},
\text{control-object mobility},
\text{local surplus},
\text{institutions}
)
}
$$

而不是：

$$
\text{Observed Political Scale}
=
F(
\text{geographical area only}
).
$$

若跨時代、跨區域資料顯示，在控制其他條件後，成本加權有效距離、治理閉環速度、控制對象流動性與地方剩餘對政治整合沒有穩定解釋力，則 EGS-HT 應被視為失敗模型或僅保留為描述性框架。

---

# 20. 結論

本文提出 EGS-HT 作為一個尚未保真的探索性模型。

其最小命題不是「地形決定政治」，而是：

$$
\boxed{
\text{幾何領土}
\neq
\text{有效移動空間}
\neq
\text{有效感知空間}
\neq
\text{有效注意空間}
\neq
\text{有效治理空間}.
}
$$

政治體真正面對的是一個異質、帶權、時變的控制空間。

一座山、一條河、一片草原、一條道路或一個港口，不直接「產生」某種制度；它們改變不同治理方案的成本與收益。制度、技術、人口、產出、戰爭與歷史路徑再對這些成本進行放大、抵消或重新編碼。

因此：

> 全國領土大小不會自動演化出帝國；帝國是某種高尺度治理閉環在特定歷史條件下變得可持續之後的結果之一。

日本中世紀可暫作「小幾何空間但高內部異質治理成本」的候選案例；歐亞草原可作「巨大幾何空間但特定行動者具有低移動成本、且控制對象高度流動」的候選案例；秦則可作「政治與技術能力逐漸跨越有效治理門檻」的候選案例。

三者目前都只是研究入口，而不是證明。

EGS-HT 的下一階段不應繼續增加歷史故事，而應開始把：

$$
d_{\mathrm{pol}},
\quad
\tau_G,
\quad
B_A,
\quad
S_{\mathrm{local}},
\quad
\chi
$$

轉化成可估算變量，並用反例主動攻擊模型。

---

# 參考文獻與待查資料

1. Barfield, Thomas J. “The Hsiung-nu Imperial Confederacy: Organization and Foreign Policy.” *The Journal of Asian Studies* 41(1), 1981, 45–61.
2. Benjamin, Craig. “Pastoral Nomads and the Empires of the Steppe.” In *Empires of Ancient Eurasia: The First Silk Roads Era, 100 BCE–250 CE*. Cambridge University Press, 2018.
3. Nagahara, Keiji & Michael P. Birt. “The Decline of the Shōen System.” In *The Cambridge History of Japan*, Vol. 3. Cambridge University Press.
4. Nagahara, Keiji & Suzanne Gay. “The Medieval Peasant.” In *The Cambridge History of Japan*, Vol. 3. Cambridge University Press.
5. Imatani, Akira & Suzanne Gay. “Muromachi Local Government: Shugo and Kokujin.” In *The Cambridge History of Japan*, Vol. 3. Cambridge University Press.
6. Staack, Thies. “The Pragmatics of Standardization: Document Standards and Their Implementation in Qin Administration (Late Third Century BCE).” *Bulletin of the School of Oriental and African Studies* 86(1), 2023, 147–173.
7. Yates, Robin D. S. “State Control of Bureaucrats under the Qin: Techniques and Procedures.” *Early China*.
8. Tong, Chun Fung. “The Emergence of Logistics Networks and Financial Administration During the Qin Conquest (230–221 BCE).” *Early China*, published online 12 January 2026.
9. “Making Use of the Land: The Political Ecology of China’s First Empire.” *Journal of Chinese History*.
10. Ministry of Land, Infrastructure, Transport and Tourism, Japan. *Land and Climate of Japan*.
11. Statistics Bureau of Japan. *Statistical Handbook of Japan 2024* / *Japan Statistical Yearbook*.
12. 後續需補：日本中世紀道路與實際旅行時間、莊園空間分布 GIS、戰國軍事動員半徑、草原季節性移動速度、秦驛傳與糧運時間資料。

---

# 版本註記

**v0.1 的目的不是證明。**

本稿目前完成的是：

1. 建立一套跨「地形—交通—視覺／觀察—注意力—通信—行動—治理」的共同語言；
2. 把「國土面積」從核心因變量降為原始幾何輸入；
3. 提出「有效治理空間」作為中介結構；
4. 建立日本／草原／秦三組候選案例；
5. 明列過強命題、反例與可證偽方向。

後續版本應優先進行歷史資料核查、案例對抗與量化，而不是繼續擴充敘事。
