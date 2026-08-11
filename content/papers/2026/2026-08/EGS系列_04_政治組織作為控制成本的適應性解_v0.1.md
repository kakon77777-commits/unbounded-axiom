# 04｜政治組織作為控制成本的適應性解
## 中央、代理、地方自治與多層治理的控制拓撲
### Political Organization as an Adaptive Solution to Control Costs: Centralization, Delegation, Local Autonomy, and Governance Topology

**系列**：有效治理空間與政治尺度  
**篇次**：04 / 12  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-07  
**版本**：v0.1  
**狀態**：探索性模型論文／待驗證假說  
**前置論文**：  
- 01｜異質地形下的有效治理空間模型（EGS-HT）  
- 02｜通信成本與帝國尺度：從治理延遲到政治有效距離  
- 03｜國家作為主動感知系統：觀察、注意力、決策與行動的治理閉環  

**研究性質**：本文提出一個治理拓撲模型，用於比較中央集權、行政分權、聯邦、封建、總督制、間接統治與多層治理。本文不主張制度可被單一成本函數完全決定；歷史制度仍受到合法性、階級、軍事、文化、繼承、意識形態與路徑依賴影響。本文只主張：任何治理制度都必須在有限信息、有限注意力、有限通信、有限執行能力與代理人風險之下運作，因此政治組織形式可被部分理解為對控制成本結構的適應。

---

## 摘要

政治制度通常被分類為中央集權、地方分權、封建、聯邦、間接統治、總督制或官僚制，但這些名稱往往混合了不同層次的權力分配。本文提出「治理控制拓撲」（Governance Control Topology, GCT）模型，將政治組織拆解為資訊、注意力、決策、財政、執行、監督與最終主權等可分離權限，並分析它們如何在不同節點與層級之間配置。

本文的核心主張是：

$$
\boxed{
\text{Centralization}
\neq
\text{one-dimensional variable}.
}
$$

一個政治體可以中央化資訊與監督，卻分散日常決策；可以中央制定標準，卻地方執行；可以地方徵收部分財源，卻由中央控制軍事與外交；也可以保留地方統治者，但由中央掌握外部主權與貢賦。因此，更合理的制度描述不是「中央化程度」單一標量，而是一個權限配置向量：

$$
\mathbf Z
=
(
z_O,
z_A,
z_D,
z_F,
z_E,
z_V,
z_S
),
$$

其中分別表示觀察、注意力、決策、財政、執行、驗證與主權的集中程度。

本文進一步定義治理總成本：

$$
C_{\mathrm{gov}}
=
C_O+
C_A+
C_C+
C_D+
C_E+
C_V+
C_{\mathrm{agency}}+
C_{\mathrm{coord}}+
C_{\mathrm{capture}}+
C_{\mathrm{secession}},
$$

並提出政治組織可被視為在制度可行集合中尋找局部最適治理拓撲：

$$
\mathcal T^*
=
\arg\min_{\mathcal T\in\mathbb T}
C_{\mathrm{gov}}(\mathcal T)
$$

subject to legitimacy, capability, security, and constitutional constraints.

此模型可以統一理解多種歷史與現代制度。直接中央治理降低地方代理人的主權風險，但提高中央注意力、資訊與執行負荷；地方授權降低反應延遲並利用地方知識，但提高代理偏離與地方俘獲風險；行政層級壓縮資訊與決策負荷，但增加中介失真；間接統治降低直接治理投入，卻可能降低問責與公共品供給；聯邦與多層治理則把不同類型權力分配給不同尺度。

因此，本文提出：

> 政治組織在一定程度上，是治理控制成本結構的適應性解。

這不是制度決定論，而是一個可以被歷史資料、比較政治與代理模型進一步反駁和修正的中層理論。

**關鍵詞**：治理拓撲、中央集權、分權、聯邦、代理人問題、間接統治、地方自治、控制成本、有限注意力、多層治理

---

# 1. 問題：中央化到底是什麼？

「中央集權」常被當成單一變量：

$$
z\in[0,1].
$$

其中：

$$
z=1
$$

表示完全中央化，

$$
z=0
$$

表示完全地方化。

但實際政治制度並不是如此。

一個國家可能：

- 外交完全中央化；
- 軍事大致中央化；
- 教育標準中央制定；
- 學校由地方管理；
- 地方擁有部分稅源；
- 警察由地方指揮；
- 統計資料中央集中；
- 土地規劃地方決策。

因此：

$$
\boxed{
\text{Centralization}
\neq
\text{single scalar}.
}
$$

本文改以向量表示：

$$
\mathbf Z
=
(
z_O,
z_A,
z_D,
z_F,
z_E,
z_V,
z_S
).
$$

其中：

- $z_O$ ：Observation，資訊與觀察集中程度；
- $z_A$ ：Attention，議程與注意力集中程度；
- $z_D$ ：Decision，政策決策集中程度；
- $z_F$ ：Fiscal，財政集中程度；
- $z_E$ ：Execution，執行權集中程度；
- $z_V$ ：Verification，監督與驗證集中程度；
- $z_S$ ：Sovereignty，最終主權集中程度。

不同政治制度可以具有完全不同的：

$$
\mathbf Z.
$$

---

# 2. 治理拓撲而非制度標籤

設政治體由節點集合：

$$
V=\{v_0,v_1,\ldots,v_n\}
$$

構成。

其中：

- $v_0$ ：中央；
- $v_i$ ：省、州、郡、縣、領主、部族、城市、地方代理或其他治理節點。

建立多層網路：

$$
\mathcal T
=
(
V,
E_O,
E_D,
E_F,
E_E,
E_V
).
$$

其中：

- $E_O$ ：資訊流；
- $E_D$ ：決策權流；
- $E_F$ ：財政流；
- $E_E$ ：執行命令流；
- $E_V$ ：監督與驗證流。

因此同一政治體實際上不是一棵單一行政樹，而是多張疊合網路。

例如：

$$
E_O
$$

可能高度向中央集中，

但：

$$
E_D
$$

可能部分地方化。

所以制度真正重要的問題不是：

> 「這是不是中央集權？」

而是：

> **哪些權力，在什麼尺度，以什麼方式，被哪些節點持有？**

---

# 3. 治理成本函數

定義某治理拓撲 $\mathcal T$ 的總成本：

$$
C_{\mathrm{gov}}(\mathcal T)
=
C_O
+
C_A
+
C_C
+
C_D
+
C_E
+
C_V
+
C_{\mathrm{agency}}
+
C_{\mathrm{coord}}
+
C_{\mathrm{capture}}
+
C_{\mathrm{secession}}.
$$

分別表示：

- $C_O$ ：資訊取得成本；
- $C_A$ ：注意力負荷；
- $C_C$ ：通信與協調成本；
- $C_D$ ：決策成本；
- $C_E$ ：執行成本；
- $C_V$ ：監督驗證成本；
- $C_{\mathrm{agency}}$ ：代理人偏離成本；
- $C_{\mathrm{coord}}$ ：跨區域協調成本；
- $C_{\mathrm{capture}}$ ：地方利益俘獲風險；
- $C_{\mathrm{secession}}$ ：離心、割據或分離風險。

政治體並不是純粹最小化金錢。

這裡的「成本」是廣義控制摩擦。

---

# 4. 制度設計作為受約束最適化

定義制度可行集合：

$$
\mathbb T.
$$

政治體的候選治理拓撲：

$$
\mathcal T\in\mathbb T.
$$

最簡化地：

$$
\boxed{
\mathcal T^*
=
\arg\min_{\mathcal T\in\mathbb T}
C_{\mathrm{gov}}(\mathcal T)
}
$$

但必須滿足：

$$
L(\mathcal T)\ge L_{\min},
$$

$$
S(\mathcal T)\ge S_{\min},
$$

$$
K(\mathcal T)\ge K_{\min},
$$

其中：

- $L$ ：合法性；
- $S$ ：安全與穩定；
- $K$ ：制度與人員能力。

因此制度不是純成本最小化問題，而是：

$$
\boxed{
\text{constrained governance optimization}.
}
$$

---

# 5. 完全中央化的收益

在高度中央化模型中：

$$
z_D,z_F,z_E,z_V\rightarrow1.
$$

中央直接控制大部分重要權力。

其主要優勢包括：

### 5.1 統一政策

$$
C_{\mathrm{policy\ divergence}}\downarrow.
$$

### 5.2 降低地方主權化

$$
C_{\mathrm{secession}}\downarrow.
$$

### 5.3 統一資源配置

中央可以跨區域重新分配：

$$
R_i\rightarrow R_j.
$$

### 5.4 建立共同標準

例如：

- 法律；
- 度量衡；
- 軍制；
- 稅制；
- 文書；
- 基礎設施。

因此高度中央化特別適合：

$$
\text{high cross-regional externality}
$$

與：

$$
\text{high coordination demand}
$$

的任務。

---

# 6. 完全中央化的成本

中央化也把更多問題推進中央：

$$
N_{\mathrm{central\ decisions}}\uparrow.
$$

因此：

$$
C_A\uparrow,
$$

$$
C_O\uparrow,
$$

$$
C_D\uparrow.
$$

而中央距離地方越遠：

$$
K_{\mathrm{local}}\downarrow
$$

的風險越大。

當中央必須直接處理過多異質問題：

$$
B_A<N_{\mathrm{required}},
$$

可能形成：

# Central Attention Overload  
# 中央注意力超載

即：

$$
\boxed{
\text{Decision Rights}
>
\text{Decision Capacity}.
}
$$

---

# 7. 分權的資訊優勢

地方節點：

$$
v_i
$$

通常更接近：

$$
S_i.
$$

因此可能具有：

$$
d_{\mathrm{info}}(v_i,S_i)
<
d_{\mathrm{info}}(v_0,S_i).
$$

也就是地方具有高解析知識：

$$
K_i^{\mathrm{local}}.
$$

若把決策權：

$$
D_i
$$

移向地方：

$$
v_0\rightarrow v_i,
$$

則：

$$
\tau_D\downarrow
$$

與：

$$
C_O\downarrow.
$$

因此分權的一個核心理由不是政治價值，而是：

$$
\boxed{
\text{local information advantage}.
}
$$

---

# 8. 分權的代理與俘獲成本

但地方更接近資訊，也更接近地方利益網絡。

地方代理人的效用：

$$
U_i
=
U_{\mathrm{center}}
+
\alpha_iU_{\mathrm{local}}
+
\beta_iU_{\mathrm{private}}.
$$

當：

$$
\beta_i\uparrow,
$$

代理偏離風險：

$$
R_A\uparrow.
$$

當地方精英控制政治與經濟資源：

$$
C_{\mathrm{capture}}\uparrow.
$$

因此：

$$
\boxed{
\text{Local Knowledge Advantage}
\neq
\text{Local Accountability}.
}
$$

分權可以提高資訊適配，同時提高地方俘獲。

---

# 9. 代理治理的基本交換

對中央而言，授權地方可降低：

$$
C_O+C_A+C_D+C_E,
$$

卻可能提高：

$$
C_{\mathrm{agency}}
+
C_{\mathrm{capture}}
+
C_{\mathrm{secession}}.
$$

因此代理程度：

$$
\delta
$$

存在潛在最適值：

$$
\delta^*
=
\arg\min_{\delta}
C_{\mathrm{gov}}(\delta).
$$

這提供一個比：

> 「中央好還是地方好？」

更精確的問題：

> **在哪些治理任務上，授權到哪一層的總控制成本最低？**

---

# 10. 中央監督＋地方決策

第 02 篇已指出：

$$
M\uparrow
$$

可能允許：

$$
D_{\mathrm{local}}\uparrow.
$$

因此通信技術改善後，不一定是：

$$
\text{centralization}\uparrow.
$$

反而可能形成：

$$
\boxed{
\text{Centralized Monitoring}
+
\text{Decentralized Decision}.
}
$$

這是一個極重要的治理拓撲。

中央負責：

- 數據；
- 標準；
- 審計；
- 監督；
- 跨區協調。

地方負責：

- 日常執行；
- 快速反應；
- 情境適配；
- 地方服務。

這種結構可以同時利用：

$$
K_{\mathrm{central}}
$$

與：

$$
K_{\mathrm{local}}.
$$

---

# 11. 中央標準＋地方執行

另一種常見結構：

$$
z_D\uparrow,
\quad
z_E\downarrow.
$$

即：

$$
\boxed{
\text{Central Standard}
+
\text{Local Implementation}.
}
$$

中央決定：

$$
\theta
$$

即最低標準。

地方選擇：

$$
x_i
$$

作為實施方式。

因此：

$$
x_i
=
\pi_i(\theta,S_i).
$$

這可以降低：

$$
C_{\mathrm{coord}}
$$

同時保留：

$$
K_{\mathrm{local}}.
$$

---

# 12. 行政分層的壓縮功能

若中央直接面對：

$$
N
$$

個地方節點：

$$
C\rightarrow\{L_1,\ldots,L_N\},
$$

中央通信負荷近似：

$$
O(N).
$$

建立中介層：

$$
C\rightarrow R_j\rightarrow L_i,
$$

可將部分資訊、注意力與決策壓縮至區域節點。

因此行政層級是：

$$
\boxed{
\text{control hierarchy}
+
\text{information hierarchy}.
}
$$

其優勢：

$$
C_A^{\mathrm{center}}\downarrow.
$$

其代價：

$$
\tau_{\mathrm{layer}}\uparrow,
$$

$$
\epsilon_{\mathrm{compression}}\uparrow.
$$

---

# 13. 層級不是越多越好

設行政層級數：

$$
h.
$$

中央注意力負荷：

$$
C_A(h)
$$

可能隨：

$$
h
$$

增加而下降。

但傳遞延遲與資訊失真：

$$
C_L(h)
$$

可能隨：

$$
h
$$

增加而上升。

因此總成本：

$$
C(h)
=
C_A(h)+C_L(h).
$$

可能存在：

$$
h^*
=
\arg\min_h C(h).
$$

所以：

$$
\boxed{
\text{Optimal hierarchy depth}
}
$$

是一個條件性變量。

---

# 14. 封建作為一種治理拓撲，而不是單一制度

本文不把「封建」視為跨文化完全相同的固定制度。

只抽象其中一種可能結構：

$$
C
\rightarrow
L_i
\rightarrow
P_i.
$$

其中地方領主：

$$
L_i
$$

同時擁有：

- 土地收入；
- 軍事能力；
- 地方司法；
- 地方行政；
- 政治忠誠義務。

這種結構在：

$$
C_E^{\mathrm{center}}\gg C_E^{\mathrm{local}}
$$

時可能具有成本優勢。

中央不用直接：

$$
C\rightarrow P_i.
$$

而只需控制：

$$
C\rightarrow L_i.
$$

因此：

$$
N_{\mathrm{control\ targets}}\downarrow.
$$

---

# 15. 封建型代理的核心風險

但地方領主同時掌握：

$$
R_i+M_i+A_i,
$$

即資源、軍事與行政。

因此：

$$
C_{\mathrm{agency}}
$$

與：

$$
C_{\mathrm{secession}}
$$

可能非常高。

若中央控制能力下降：

$$
M_C\downarrow,
$$

地方節點可能由：

$$
\text{agent}
$$

逐漸轉化為：

$$
\text{autonomous principal}.
$$

即：

$$
L_i:
\text{agent}
\rightarrow
\text{quasi-sovereign}.
$$

這是高度地方化制度的一個典型拓撲風險。

---

# 16. 郡縣式官僚治理

另一種拓撲是：

$$
C
\rightarrow
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
L.
$$

地方官：

$$
B_i
$$

不是世襲主權節點，而是可替換代理人。

中央試圖將：

$$
\text{office}
$$

與：

$$
\text{person}
$$

分離。

因此：

$$
C_{\mathrm{secession}}\downarrow.
$$

但代價是必須建立：

- 任命；
- 文書；
- 考核；
- 薪酬；
- 監督；
- 通信；
- 法規；
- 檔案。

所以官僚制要求更高：

$$
C_{\mathrm{infrastructure}}
+
C_{\mathrm{information}}.
$$

---

# 17. 世襲代理與任命代理

可以建立兩種簡化模型。

## 世襲代理

$$
P(L_{t+1}=L_t)\approx1.
$$

優點：

- 地方知識積累；
- 地方穩定；
- 中央任命成本低。

缺點：

- 地方權力固化；
- 中央替換能力低。

## 任命代理

$$
P(B_{t+1}=B_t)<1.
$$

優點：

- 中央控制人事；
- 降低地方主權固化。

缺點：

- 地方知識可能較弱；
- 人員輪調成本；
- 官員可能短期化掠奪。

因此：

$$
\boxed{
\text{Hereditary vs Appointed}
}
$$

也是代理成本配置問題。

---

# 18. 聯邦不是單純「更分權」

聯邦可以表示為：

$$
\mathcal F
=
(C,R_1,\ldots,R_n)
$$

且中央與區域都擁有部分：

$$
z_S>0.
$$

即權力並非純粹由中央可隨時收回的行政授權，而可能受到憲法保護。

因此聯邦與普通行政分權的差別之一是：

$$
\boxed{
\text{delegation}
\neq
\text{constitutionally protected autonomy}.
}
$$

聯邦制度的真正問題是：

> 哪些任務的最適治理尺度不同？

---

# 19. 任務尺度匹配

對治理任務：

$$
m
$$

定義最適空間尺度：

$$
s_m^*.
$$

例如：

- 國防：大尺度；
- 外交：大尺度；
- 流行病：跨區尺度；
- 垃圾收運：地方尺度；
- 土地使用：高度地方化；
- 跨境河流：區域尺度。

若決策尺度：

$$
s_D
$$

與問題尺度：

$$
s_m
$$

嚴重不匹配，

則：

$$
C_{\mathrm{coord}}\uparrow
$$

或：

$$
C_{\mathrm{local\ mismatch}}\uparrow.
$$

因此：

$$
\boxed{
\text{Governance Scale}
\approx
\text{Problem Scale}.
}
$$

是一個重要方向性原則。

---

# 20. 外溢效應與中央化需求

若地方 $i$ 的行動：

$$
x_i
$$

對地方 $j$ 有高度影響：

$$
\frac{\partial U_j}{\partial x_i}\gg0,
$$

則單純地方決策可能忽略外部性。

因此：

$$
\text{spillover}\uparrow
\Rightarrow
\text{coordination scale}\uparrow.
$$

這解釋為何某些事務即使地方資訊非常重要，仍需要更高層級協調。

---

# 21. 間接統治作為低成本治理

間接統治可抽象為：

$$
C\rightarrow E_i\rightarrow P_i,
$$

其中：

$$
E_i
$$

是既有地方政治精英、王公、酋長或制度。

中央不直接重建整套地方行政，

而是利用既有節點。

因此：

$$
C_{\mathrm{direct}}\downarrow.
$$

它特別適合：

$$
\text{low central capacity}
$$

或：

$$
\text{high annexation cost}.
$$

---

# 22. 間接統治的治理深度交換

中央在間接統治中可能只要求：

$$
Q=
(\text{tax},
\text{tribute},
\text{military loyalty},
\text{external obedience}).
$$

而不深入控制：

$$
\text{daily local governance}.
$$

因此：

$$
\theta_G\downarrow.
$$

即降低治理深度門檻。

這使：

$$
C_{\mathrm{gov}}\downarrow.
$$

但也意味：

$$
\chi_{\mathrm{local}}
$$

與中央政策一致性下降。

---

# 23. 間接統治的代理風險

地方精英拥有自己的：

$$
U_E.
$$

如果中央監督弱：

$$
M\downarrow,
$$

則地方代理可能优先：

$$
U_E
$$

而不是：

$$
U_C.
$$

因此：

$$
C_{\mathrm{agency}}\uparrow.
$$

實證研究也顯示，直接與間接統治的問責結構差異可能留下長期公共品供給差異。

所以：

$$
\boxed{
\text{Cheap Rule}
\neq
\text{High-quality Rule}.
}
$$

---

# 24. 地方合法性作為資產

間接治理之所以有時有效，不只因中央懶得管。

既有地方制度可能擁有：

$$
L_i^{\mathrm{local}}\gg L_C^{\mathrm{local}}.
$$

即地方合法性。

中央若摧毀既有制度重新建構，

可能支付：

$$
C_{\mathrm{legitimacy}}.
$$

所以保留地方節點可能是在利用：

$$
\boxed{
\text{pre-existing legitimacy capital}.
}
$$

---

# 25. 分權不等於無中心

分權系統仍需要協調。

若所有節點：

$$
v_i
$$

完全自主，

跨區問題可能形成：

$$
C_{\mathrm{coord}}\uparrow.
$$

所以：

$$
\boxed{
\text{Decentralization}
\neq
\text{absence of coordination}.
}
$$

一個可擴展分權系統往往仍需要：

- 協議；
- 標準；
- 仲裁；
- 財政轉移；
- 聯合決策；
- 共同基礎設施。

---

# 26. 中心也可以是服務節點

傳統想像：

$$
C
$$

是命令節點。

但在某些治理拓撲中：

$$
C
$$

也可以主要提供：

- 共享資料；
- 標準；
- 安全；
- 清算；
- 仲裁；
- 跨區基礎設施；
- 危機支援。

因此中央的角色可能從：

$$
\text{Command Center}
$$

轉為：

$$
\boxed{
\text{Coordination and Service Hub}.
}
$$

這是一個重要的非二元化方向。

---

# 27. 非對稱治理

不同區域：

$$
i,j
$$

可能具有不同：

- 地形；
- 文化；
- 人口；
- 治理能力；
- 地方合法性；
- 經濟結構。

因此：

$$
\mathbf Z_i
\neq
\mathbf Z_j.
$$

也就是非對稱分權。

這可以被視為：

$$
\boxed{
\text{heterogeneous governance matching}.
}
$$

而不是制度不一致的例外。

---

# 28. 治理拓撲的動態變化

政治拓撲不是固定不變。

令：

$$
\mathcal T_t.
$$

當通信改善：

$$
C_C\downarrow,
$$

可能出現：

$$
\mathcal T_t
\rightarrow
\mathcal T_{t+1}.
$$

但方向不唯一。

可能：

$$
\text{recentralization}
$$

也可能：

$$
\text{safe delegation}.
$$

因此：

$$
\boxed{
\frac{\partial \mathcal T}{\partial C_C}
}
$$

不是固定符號。

---

# 29. 戰爭與緊急狀態

危機期間：

$$
\tau_*\downarrow.
$$

為使：

$$
\Lambda<1,
$$

政治體可能暫時：

$$
z_D\uparrow,
$$

$$
z_E\uparrow.
$$

即集中決策與執行。

所以：

$$
\boxed{
\text{optimal topology is state-dependent}.
}
$$

和平時最適制度不一定是戰爭時最適制度。

---

# 30. 地方實驗與制度學習

分散式政治體還有一個潛在優勢：

$$
R_1,\ldots,R_n
$$

可以同時測試：

$$
p_1,\ldots,p_n.
$$

形成：

$$
\text{parallel policy experimentation}.
$$

若中央能觀察結果：

$$
O_i
$$

再推廣高績效方案，

則：

$$
\boxed{
\text{decentralization}
+
\text{central learning}
}
$$

可能產生制度搜索優勢。

但若地方無法可靠比較：

$$
R_F\downarrow,
$$

這個優勢可能消失。

---

# 31. 多中心治理

不是所有系統都需要：

$$
1
$$

個唯一中央。

可以存在：

$$
C_1,C_2,\ldots,C_k.
$$

不同中心處理不同功能。

例如：

$$
C_{\mathrm{military}},
C_{\mathrm{fiscal}},
C_{\mathrm{religious}},
C_{\mathrm{judicial}}.
$$

因此：

$$
\boxed{
\text{polycentric governance}
}
$$

可以被表示為多中心控制拓撲。

這也提醒：

> 「國家」不一定是一個單節點控制器。

---

# 32. 治理拓撲穩定性

定義治理拓撲：

$$
\mathcal T
$$

的穩定性：

$$
\Sigma(\mathcal T).
$$

它可以依賴：

$$
\Sigma
=
f(
C_{\mathrm{gov}},
L,
R_A,
R_S,
K,
E
).
$$

若：

$$
C_{\mathrm{gov}}\uparrow
$$

或：

$$
R_S\uparrow
$$

超過系統承受能力，

可能發生：

$$
\mathcal T
\rightarrow
\mathcal T'.
$$

例如：

- 再中央化；
- 分權；
- 聯邦化；
- 地方割據；
- 帝國瓦解。

---

# 33. 制度相變

令某控制拓撲的效用：

$$
U(\mathcal T;\theta)
$$

受環境參數：

$$
\theta
$$

影響。

當：

$$
\theta
$$

跨過臨界值：

$$
\theta_c,
$$

可能：

$$
U(\mathcal T_1)
<
U(\mathcal T_2).
$$

原有制度就可能失去相對優勢。

例如：

$$
C_C\downarrow
$$

足以讓中央直接任命與監督地方官員後，

原先依賴高自主地方領主的制度可能不再是低成本解。

所以：

$$
\boxed{
\text{Institutional Change}
}
$$

可以部分理解為控制成本排序改變。

---

# 34. 不是地理決定制度

本文特別拒絕：

$$
\text{mountain}
\Rightarrow
\text{decentralization}.
$$

更合理的是：

$$
\text{mountain}
\rightarrow
C_M,C_C,C_E
$$

再與：

$$
T,I,L,K
$$

互動。

因此：

$$
\boxed{
\text{Geography changes the payoff landscape;}
}
$$

但不單獨選出制度。

---

# 35. 不是科技決定中央集權

同樣拒絕：

$$
\text{better communication}
\Rightarrow
\text{centralization}.
$$

可能真正發生的是：

$$
\text{better communication}
\Rightarrow
\mathbb T_{\mathrm{feasible}}\uparrow.
$$

即：

# 可行治理拓撲集合擴張

中央可以選擇：

- 更中央化；
- 更分權；
- 中央監督＋地方執行；
- 多中心；
- 動態授權。

因此技術增加的是：

$$
\boxed{
\text{organizational degrees of freedom}.
}
$$

---

# 36. 控制深度與控制廣度

政治體還必須在：

$$
\text{breadth}
$$

與：

$$
\text{depth}
$$

之間選擇。

治理廣度：

$$
B_G
=
|\Omega_N|.
$$

治理深度：

$$
D_G
=
\mathbb E[\chi(x)].
$$

可能存在：

$$
B_G\uparrow
\Rightarrow
D_G\downarrow
$$

的歷史 trade-off。

因此大型帝國可能選擇：

$$
\text{wide but shallow}
$$

而小型國家可能：

$$
\text{narrow but deep}.
$$

這比單純比較領土更有意義。

---

# 37. 治理拓撲的五種理想型

本文提出五種理想型。

## Type I：直接中央型

$$
C\rightarrow P.
$$

特徵：

$$
z_D,z_E,z_V\uparrow.
$$

## Type II：官僚層級型

$$
C\rightarrow B_1\rightarrow B_2\rightarrow P.
$$

特徵：任命代理＋文書監督。

## Type III：領主／間接代理型

$$
C\rightarrow L_i\rightarrow P_i.
$$

特徵：地方高自主、低中央直接成本。

## Type IV：聯邦／多層型

$$
C\leftrightarrow R_i.
$$

特徵：多尺度權限分工。

## Type V：多中心網路型

$$
C_1,C_2,\ldots,C_k.
$$

特徵：功能性中心並存。

現實政治體通常是混合型：

$$
\mathcal T
=
\sum_i
\alpha_i\mathcal T_i.
$$

---

# 38. 任務依賴的最適拓撲

不存在：

$$
\mathcal T^*
$$

對所有任務皆最優。

更精確：

$$
\mathcal T_m^*
=
\arg\min_{\mathcal T}
C_{\mathrm{gov}}(\mathcal T\mid m).
$$

因此：

$$
\mathcal T_{\mathrm{defense}}^*
\neq
\mathcal T_{\mathrm{school}}^*
\neq
\mathcal T_{\mathrm{waste}}^*.
$$

這是本文最重要的形式化結果之一。

---

# 39. 可反駁命題

## 命題 1：多維中央化命題

中央化程度不能被單一標量充分描述。

## 命題 2：地方知識命題

地方資訊優勢越大，適度地方決策的相對收益越高。

## 命題 3：代理風險命題

地方自主越高，而監督能力越弱，代理偏離與地方俘獲風險越可能上升。

## 命題 4：層級壓縮命題

行政層級可以降低中央注意力負荷，但增加信息失真與延遲。

## 命題 5：間接統治交換命題

間接統治降低直接治理成本，但可能以問責與治理深度為代價。

## 命題 6：任務尺度匹配命題

政策問題的空間外溢越大，最適治理尺度越傾向上移。

## 命題 7：監督—授權互補命題

更強監督能力在某些條件下會增加，而非減少，安全授權的可行範圍。

## 命題 8：制度相變命題

交通、通信、軍事與行政技術改變可使不同治理拓撲的成本排序發生反轉。

---

# 40. 可實證預測

1. 地方資訊異質性越高的政策領域，完全中央統一決策的誤配成本應更高。
2. 監督與通信改善後，地方執行權或決策權可能增加，而不一定下降。
3. 行政層級數與中央注意力負荷可能呈負相關，但與資訊延遲／失真呈正相關。
4. 間接治理地區的中央行政投入應較低，但治理品質高度依賴地方代理人激勵。
5. 高外溢問題應更常被提升至較高治理層級。
6. 高地方剩餘、高地方軍事能力與低中央監督能力的組合，应提高地方政治自主化風險。
7. 通信革命後，同一政治體內不同功能可能出現不對稱再中央化與再分權。

---

# 41. 主要反論

## 41.1 制度不是效率產物

正確。

制度可能由：

- 征服；
- 階級利益；
- 宗教；
- 意識形態；
- 偶然；
- 殖民；
- 權力鬥爭；

產生。

本文只主張：

> 制度若要持續存在，仍必須支付其治理控制成本。

起源不等於維持條件。

---

## 41.2 高成本制度也可能長期存在

正確。

路徑依賴、合法性與強制可以使次優制度持續。

因此本文模型描述：

$$
\text{selection pressure}
$$

而不是：

$$
\text{instant optimization}.
$$

---

## 41.3 中央與地方不是統一行動者

正確。

兩者都包含內部多智能體。

所以：

$$
C
$$

與：

$$
L
$$

都是抽象節點。

後續可以展開：

$$
\mathcal T
\rightarrow
\text{nested multi-agent topology}.
$$

---

# 42. 與現有研究的關係

本文與數條既有研究相接。

### 42.1 分權與聯邦

現有聯邦制研究已區分結構、功能、財政與人事等不同分權維度，也指出地方政府通常更接近地方需求與資訊，但分權可能受到能力不足、腐敗與地方俘獲限制。

本文將這些維度進一步表示為：

$$
\mathbf Z.
$$

### 42.2 政治分權理論

政治經濟學對分權的研究長期關注：

- 地方資訊；
- 問責；
- 俘獲；
- 外溢；
- 實驗；
- 財政關係。

本文把它們整合成：

$$
C_{\mathrm{gov}}(\mathcal T).
$$

### 42.3 Principal-Agent

代理理論說明中央與地方官員之間存在目標不一致與監督問題。

本文將代理成本與：

$$
d_{\mathrm{pol}},
B_A,C_V
$$

整合。

### 42.4 間接統治

歷史研究顯示，帝國使用既有地方制度可以避免直接吞併的經濟與政治成本，但不同間接治理結構會改變代理人的激勵、問責與公共品供給。

### 42.5 組織層級

有限理性與組織理論指出，層級可以成為處理複雜協調與資訊問題的一種組織解。

本文把此結構移植至政治治理。

---

# 43. 第一部理論統合

完成第 04 篇後，第一部四篇可以合併成：

$$
\boxed{
\text{Terrain}
\rightarrow
\text{Effective Distance}
\rightarrow
\text{Latency}
\rightarrow
\text{Observation}
\rightarrow
\text{Attention}
\rightarrow
\text{Decision}
\rightarrow
\text{Execution}
\rightarrow
\text{Feedback}
\rightarrow
\text{Governance Topology}.
}
$$

其中：

第 01 篇回答：

> 哪些空間真正是可治理空間？

第 02 篇回答：

> 治理閉環能不能快過世界變化？

第 03 篇回答：

> 國家究竟看見並注意了什麼？

第 04 篇回答：

> 權力與控制功能應該放在哪些節點？

因此第一部的總命題可以正式寫成：

$$
\boxed{
\text{Political Organization}
=
\text{a topology for closing governance loops under heterogeneous costs}.
}
$$

---

# 44. 結論

政治制度不應只被視為憲法名稱或意識形態分類。

從控制角度看，它更接近：

$$
\boxed{
\text{a distribution of sensing, decision, fiscal, execution, and verification rights across nodes}.
}
$$

因此：

$$
\text{centralization}
$$

不是一個單一數字。

而是：

$$
\mathbf Z
=
(
z_O,z_A,z_D,z_F,z_E,z_V,z_S
).
$$

政治體面對的核心問題也不是：

> 中央集權比較好，還是地方自治比較好？

而是：

> 在特定的地形、距離、通信、地方知識、監督能力、代理風險、外溢效應與安全條件下，哪些權限應該放在哪一層，才能以最低可持續成本閉合治理迴路？

因此本文提出：

$$
\boxed{
\text{Political organization is partly an adaptive solution to the cost structure of control.}
}
$$

更完整地：

$$
\boxed{
\mathcal T_m^*
=
\arg\min_{\mathcal T\in\mathbb T}
C_{\mathrm{gov}}(\mathcal T\mid m,\theta,t)
}
$$

其中：

- $m$ ：治理任務；
- $\theta$ ：地形、社會、技術與制度條件；
- $t$ ：歷史時代。

這意味著不存在永恆最優的中央化程度。

存在的只可能是：

$$
\boxed{
\text{condition-dependent governance topology}.
}
$$

而歷史上的郡縣、封建、總督、聯邦、自治、間接統治與多中心治理，可以被重新理解為不同文明在不同控制成本環境下所形成的候選解。

第一部至此完成。

下一部將不再主要增加抽象模型，而開始追問：

> 古代與中世紀不同文明，是否已經反覆獨立發現這些控制問題？

第 05 篇將從：

**亞里斯多德、色諾芬、阿契美尼德波斯、羅馬、中世紀巡迴王權到馬基維利**

開始，建立 EGS 系列的思想史前史。

---

# 參考文獻

1. Kincaid, John. “Decentralization.” Center for the Study of Federalism.
2. Mookherjee, Dilip. “Political Decentralization.” *Annual Review of Economics* 7, 2015.
3. Gasparyan, Olga. “Indirect Rule and Public Goods Provision: Evidence from Colonial India.” *Political Science Research and Methods* 12(2), 2024.
4. Bolt, Jutta, Leigh Gardner, Jennifer Kohler, Jack Paine, and James A. Robinson. “Councils and Indirect Rule in British Africa.” NBER Working Paper 30582, revised 2025.
5. Fisher, Michael H. “Indirect Rule in the British Empire: The Foundations of the Residency System in India (1764–1858).” *Modern Asian Studies*.
6. Naseemullah, Adnan & Paul Staniland. “Indirect Rule and Varieties of Governance.” *Governance* 29(1), 2016.
7. Radner, Roy. “The Internal Organization of Complex Teams: Bounded Rationality and the Logic of Hierarchies.” *Journal of Economic Behavior & Organization* 9(4), 1988.
8. Simon, Herbert A. *Administrative Behavior*.
9. Oates, Wallace E. *Fiscal Federalism*.
10. Ostrom, Elinor. *Understanding Institutional Diversity*.
11. 後續需補：中國郡縣與封建的比較資料、日本中世紀守護／地頭治理、羅馬行省授權、鄂圖曼地方行政、聯邦與單一制國家的任務分權比較。

---

# 版本註記

**第一部：理論地基，01–04 完成。**

四篇的共同研究對象已由「領土」逐步推進到「治理拓撲」：

$$
\boxed{
\Omega_{\mathrm{geo}}
\rightarrow
\Omega_G
\rightarrow
\tau_G
\rightarrow
S_t^{\mathrm{eff}}
\rightarrow
\mathcal T.
}
$$

下一篇：

**05｜從亞里斯多德到馬基維利：遠距治理問題的西方思想史前史**

將開始第二部：

**古人的發現——遠距治理的文明收斂。**
