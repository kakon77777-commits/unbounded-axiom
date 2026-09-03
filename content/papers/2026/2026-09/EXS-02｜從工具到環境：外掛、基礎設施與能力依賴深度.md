# EXS-02｜從工具到環境：外掛、基礎設施與能力依賴深度
## 當可拆卸裝置變成文明預設條件

**系列：** Human Capability Externalization & Intelligence Substrate Evolution Series  
**系列中文名：** 人類能力外部化與智能載體演化系列  
**編號：** EXS-02  
**版本：** v1.0  
**日期：** 2026-08-18  
**狀態：** Canonical Source / UTF-8 Markdown  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

EXS-01 提出「能力外部化」作為理解人類文明史的一條長期軸線：人類並不只靠改變生物個體本身來增加能力，而是把力量、感官、記憶、計算、移動與後續的認知功能配置到外部工具、符號、制度與基礎設施中，藉此擴張可達狀態空間。本文進一步處理這條歷史路徑的另一面：當外部能力載體從可選工具逐漸變成預設環境時，能力增加會同時產生依賴。

本文提出「能力依賴深度」概念，區分能力外部化程度與能力依賴程度。某個社會可以高度使用外部技術，但仍保留可替代路徑、局部失效隔離與快速恢復能力；也可以在相同的表面技術水平下，把單一外部服務嵌入大量下游功能，使其失效造成廣泛的連鎖退化。因而：

$$
\text{Capability Externalization}
\neq
\text{Capability Dependency}.
$$

本文進一步建立一個初步的依賴分析框架，包含替代性、恢復性、控制距離、失效半徑、跨層耦合、時間依賴與治理可見性。本文並將 CISA、NIST、OECD 與互依網路研究中的「critical infrastructure interdependency」「community resilience」「digital public infrastructure」等實證與治理框架納入比較，指出現代文明已廣泛呈現「system of systems」特徵：電力、通訊、資訊科技、交通、水、金融、醫療與公共服務不再是彼此孤立的工具，而是互相提供前置條件的能力環境。

本文的核心結論不是「依賴技術等於退化」，也不是主張文明應回到低技術狀態，而是提出一個更精確的判準：文明的問題不在於能力是否外部化，而在於外部能力是否仍具有可替代性、可恢復性、可審計性、可治理性與失效隔離能力。這一框架將成為後續 EXS-03「從算盤到超算：計算委託與人類認知外包史」以及第二系列 AI 基礎設施與系統奇點研究的中介層。

---

## 關鍵詞

能力依賴深度；基礎設施；能力外部化；系統互依；韌性；失效半徑；替代性；恢復性；控制距離；數位公共基礎設施；路徑依賴；AI 基礎設施

---

# 1. 從 EXS-01 出發：能力增加的另一面

EXS-01 建立了：

$$
\boxed{
C_{\mathrm{int}}
\neq
C_{\mathrm{acc}}
}
$$

其中 $C_{\mathrm{int}}$ 是內在能力， $C_{\mathrm{acc}}$ 是主體可接取外部工具、知識、制度與基礎設施後的可達能力。

這個框架可以解釋為什麼現代人不需要在生物尺度上長出翅膀，也可以取得飛行能力；不需要讓裸眼直接觀察細胞，也可以透過顯微鏡拓展可觀測世界。

但一旦能力來源移到外部，就會出現第二個問題：

> 如果外部能力消失，主體還剩下多少能力？

因此，文明能力不能只問：

$$
C_{\mathrm{acc}}
$$

有多大。

還必須問：

$$
C_{\mathrm{fallback}}
$$

有多大。

其中：

$$
C_{\mathrm{fallback}}
=
\text{capability remaining under disruption of selected external layers}.
$$

於是：

$$
\boxed{
C_{\mathrm{acc}}
\uparrow
\not\Rightarrow
C_{\mathrm{fallback}}
\uparrow
}
$$

甚至可能出現：

$$
C_{\mathrm{acc}}
\uparrow,
\qquad
C_{\mathrm{fallback}}
\downarrow.
$$

這不是技術悲觀論，而是一個結構性區分。

---

# 2. 工具、服務、基礎設施與環境不是同一層

本文先區分四種外部能力載體。

## 2.1 工具

令：

$$
T
=
\text{tool}.
$$

工具的典型特徵是：

- 可局部持有；
- 可局部操作；
- 可相對容易停用；
- 失效通常主要影響使用者或局部工作。

例如一把斧頭。

若斧頭失效：

$$
F(T)
\rightarrow
\Delta C_{\mathrm{local}}<0.
$$

但它通常不會讓整座城市同時失去供水、通訊與醫療。

## 2.2 服務

令：

$$
S
=
\text{service}.
$$

服務可能由遠端組織、平台或網路提供能力。

例如導航、雲端儲存、支付網路。

它比單一工具更容易產生：

$$
\text{User}
\neq
\text{Operator}
$$

與：

$$
\text{User}
\neq
\text{Owner}.
$$

## 2.3 基礎設施

令：

$$
I
=
\text{infrastructure}.
$$

基礎設施的特徵不是「規模很大」而已，而是其他大量功能把它當作前置條件。

可寫成：

$$
I
\rightarrow
\{S_1,S_2,\ldots,S_n\}.
$$

當 $n$ 很大，而且這些服務又支撐其他服務時，基礎設施失效會產生跨層傳導。

## 2.4 環境

當一個基礎設施長期存在，並被教育、制度、工作流程、城市設計與市場預期共同內化後，它就不再只是「我今天選擇使用的工具」，而可能變成：

$$
E
=
\text{capability environment}.
$$

這裡的「環境」不是自然環境的同義詞，而是：

> 行動者在通常情況下不需要逐次選擇，就已經預設存在的能力條件。

因此：

$$
\boxed{
\text{Tool}
\rightarrow
\text{Service}
\rightarrow
\text{Infrastructure}
\rightarrow
\text{Environment}
}
$$

可以是某些技術的歷史演化方向，但不是所有技術都必然走完這條路。

---

# 3. 外掛何時不再像外掛？

假設一個人使用：

$$
T_1
$$

完成某項工作。

如果：

$$
T_1=0
$$

時，他可以立即改用：

$$
T_2,
$$

而且成本很低，那麼依賴程度不高。

相反地，如果：

$$
T_1=0
$$

會導致：

$$
\{S_1,S_2,\ldots,S_n\}=0
$$

或大幅退化，那麼 $T_1$ 已不再只是一般工具。

因此，外掛轉化為環境的一個重要標誌是：

$$
\boxed{
\text{Removal Cost}
\uparrow
}
$$

以及：

$$
\boxed{
\text{Downstream Dependents}
\uparrow.
}
$$

本文把這種變化稱為：

$$
\boxed{
\text{Capability Environmentalization}
}
$$

即：

> 能力載體從局部可選裝置，逐步成為大量其他能力共同依賴的預設條件。

---

# 4. 能力外部化程度與能力依賴深度必須分開

令外部化比例為：

$$
R_{\mathrm{ext}}
=
\frac{
C_{\mathrm{acc}}-C_{\mathrm{int}}
}{
C_{\mathrm{acc}}
}.
$$

這只是概念型指標，用於表示有效能力中有多少依賴外部載體。

但這個量不能直接代表風險。

因為兩個系統都可能有：

$$
R_{\mathrm{ext}}\approx0.9
$$

卻具有完全不同的韌性。

因此再定義：

$$
D_{\mathrm{cap}}
=
\text{Capability Dependency Depth}.
$$

能力依賴深度不應只由單一數值表示，而更接近一個向量：

$$
\mathbf D_{\mathrm{cap}}
=
(
d_s,
d_r,
d_c,
d_b,
d_t,
d_g
).
$$

其中：

$$
d_s
=
\text{substitutability deficit},
$$

$$
d_r
=
\text{recoverability cost},
$$

$$
d_c
=
\text{control distance},
$$

$$
d_b
=
\text{blast radius},
$$

$$
d_t
=
\text{temporal dependency},
$$

$$
d_g
=
\text{governance opacity}.
$$

此後各節將逐一展開。

---

# 5. 替代性：最重要的依賴變量之一

假設主體使用外部載體 $X$。

若存在一組替代物：

$$
\mathcal A_X
=
\{X_1,X_2,\ldots,X_m\},
$$

而且切換成本低，則：

$$
S_X
=
\text{Substitutability}
$$

較高。

反之：

$$
|\mathcal A_X|\rightarrow0
$$

或：

$$
C_{\mathrm{switch}}\rightarrow\infty
$$

時，依賴加深。

因此：

$$
\boxed{
\text{High Externalization}
+
\text{High Substitutability}
}
$$

與：

$$
\boxed{
\text{High Externalization}
+
\text{Low Substitutability}
}
$$

是兩種完全不同的文明狀態。

這一點對後續 AI 研究非常重要。

「大量使用 AI」不能直接推出「文明已經無法脫離某個 AI」。

真正要問的是：

- 是否存在替代模型？
- 是否存在離線模式？
- 是否保留人工流程？
- 是否可以轉移供應商？
- 資料是否可攜？
- 介面是否互通？
- 關鍵功能是否可降級運行？

---

# 6. 恢復性：失效不是唯一問題，恢復時間才是文明尺度問題

NIST 對 community resilience 的研究強調，韌性不只涉及是否承受衝擊，也涉及功能能否在可接受時間內恢復。[1]

因此本文定義：

$$
\tau_{\mathrm{rec}}(X)
=
\text{recovery time of capability supported by }X.
$$

若兩個系統都會失效，但：

$$
\tau_{\mathrm{rec}}(A)
\ll
\tau_{\mathrm{rec}}(B),
$$

則其文明風險完全不同。

更重要的是，恢復時間本身受到依賴關係約束。

若：

$$
A
\rightarrow
B
\rightarrow
C,
$$

而恢復 $A$ 需要 $C$，就可能形成：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
A.
$$

此時系統可能不是單純「逐項修好」即可恢復，而需要設計啟動順序、備援與外部支援。

因此：

$$
\boxed{
\text{Recovery Order}
}
$$

本身就是能力依賴的一部分。

---

# 7. 失效半徑：一個節點壞掉，到底會影響多少世界？

令某個能力節點為 $x$。

其直接下游集合為：

$$
N_1(x).
$$

二階下游為：

$$
N_2(x).
$$

一般化：

$$
N_k(x).
$$

則可以把概念上的失效半徑寫成：

$$
B(x)
=
\bigcup_{k=1}^{K}
N_k(x).
$$

其中 $B$ 表示 blast radius。

若一個工具只影響單一使用者：

$$
|B(x)|\approx1.
$$

若一個電力節點支撐：

- 通訊；
- 供水；
- 交通；
- 醫療；
- 金融；
- 資料中心；

則：

$$
|B(x)|\gg1.
$$

CISA 的 Infrastructure Dependency Primer 正是從這種角度處理基礎設施依賴，明確區分上下游依賴、單向依賴與雙向互依，並指出 IT、通訊與電力等部門對其他關鍵基礎設施具有廣泛支撐作用。[2]

因此：

$$
\boxed{
\text{Node Importance}
\neq
\text{Node Size}.
}
$$

真正重要的是它位於多少因果路徑上。

---

# 8. 互依網路：現代文明不是工具集合，而是 system of systems

如果所有外部工具彼此獨立，能力依賴問題仍相對簡單。

但現代文明更接近：

$$
\mathcal G
=
(V,E)
$$

其中：

$$
V
=
\text{infrastructure nodes},
$$

$$
E
=
\text{dependency relations}.
$$

更精確地說，往往是多層網路：

$$
\mathcal G
=
\{
G_{\mathrm{power}},
G_{\mathrm{water}},
G_{\mathrm{transport}},
G_{\mathrm{IT}},
G_{\mathrm{finance}},
G_{\mathrm{health}},
\ldots
\}.
$$

而層與層之間存在：

$$
E_{ij}.
$$

Buldyrev 等人在 2010 年的互依網路研究指出，互相依賴的網路可能出現遞迴式連鎖失效；小比例的初始節點失效，在特定結構中可能被放大成系統性破碎。[3]

本文並不把該模型直接等同真實城市或所有現代基礎設施，而是採用其一般啟示：

$$
\boxed{
\text{Interdependence can transform local failure into systemic failure}.
}
$$

所以外部能力愈多，並不自動表示系統愈脆弱。

真正的問題是：

$$
\boxed{
\text{Dependency Topology}.
}
$$

---

# 9. 依賴拓樸比依賴數量更重要

假設兩個文明都有 $100$ 個關鍵外部系統。

文明 $A$：

$$
G_A
$$

高度模組化，失效可局部隔離。

文明 $B$：

$$
G_B
$$

大量共享單點、共用控制層與相互依賴。

即使：

$$
|V_A|=|V_B|,
$$

也不代表：

$$
R_A=R_B.
$$

因此依賴分析不能停在：

> 我們用了多少技術？

而應進一步問：

> 這些技術是如何依賴彼此的？

可定義：

$$
\kappa(x)
=
\text{dependency centrality of }x.
$$

當：

$$
\kappa(x)\uparrow,
$$

節點失效的潛在系統性影響上升。

因此：

$$
\boxed{
\text{Dependency Quantity}
\neq
\text{Dependency Topology}.
}
$$

---

# 10. 數位基礎設施已經開始從工具變成制度環境

2026 年 OECD Digital Government Outlook 對數位政府的描述具有代表性：共享數位基礎設施、數位身分、資料治理、互通性、雲端與系統韌性已經被視為現代公共服務運行的重要基礎，而不只是可有可無的單一應用。[4]

這表示在某些公共功能中：

$$
\text{Digital System}
$$

已經不是：

$$
\text{optional productivity tool}.
$$

而更接近：

$$
\text{service delivery substrate}.
$$

因此：

$$
\boxed{
\text{Digitalization}
\rightarrow
\text{Institutional Environmentalization}
}
$$

可能在特定領域成立。

這並不表示所有國家、所有政府或所有民眾都達到相同程度。

相反地，正因為滲透不均，所以依賴深度必須按：

$$
\text{country},
\text{region},
\text{sector},
\text{income},
\text{institution}
$$

分開研究。

---

# 11. 預設環境：新世代不一定知道自己「裝了外掛」

一個技術如果在個體出生以前就存在，它的主觀體驗會與後來採用的技術不同。

第一代：

> 我開始使用網路。

第二代：

> 網路一直都在。

第三代甚至可能：

> 什麼叫「沒有網路」？

因此，本文區分：

$$
T_{\mathrm{adopted}}
$$

與：

$$
T_{\mathrm{inherited}}.
$$

前者是個體主動採用的能力載體，後者是出生時就已嵌入生活世界的能力環境。

當：

$$
T_{\mathrm{inherited}}
$$

比例增加，技術依賴的主觀可見性可能下降。

這產生：

$$
\boxed{
\text{Dependency Visibility Problem}.
}
$$

人們可能清楚知道自己「使用一把工具」，卻不容易持續意識到：

- 電力如何供應；
- DNS 如何解析；
- 雲端服務在哪裡運行；
- 金融清算如何完成；
- 全球物流如何維持；
- 軟體更新如何取得。

因此：

$$
\text{Dependency}
\neq
\text{Perceived Dependency}.
$$

---

# 12. 控制距離：能力是我的，但控制權不一定是我的

早期個人工具常具有：

$$
\text{User}
\approx
\text{Operator}
\approx
\text{Possessor}.
$$

例如個人持有的石斧。

現代服務更常是：

$$
\text{User}
\neq
\text{Operator}
\neq
\text{Owner}.
$$

例如：

$$
H
\rightarrow
\text{Device}
\rightarrow
\text{Network}
\rightarrow
\text{Cloud}
\rightarrow
\text{Platform}
\rightarrow
\text{Data Center}
\rightarrow
\text{Power Grid}.
$$

本文定義：

$$
d_c
=
\text{Control Distance}.
$$

控制距離不只是物理距離，而是主體與能力載體之間經過多少不可直接控制的組織、協議、供應商與基礎設施層。

如果：

$$
d_c\uparrow,
$$

則主體可能同時獲得更高能力與更低直接控制力。

因此：

$$
\boxed{
\text{Accessible Capability}
\neq
\text{Owned Capability}.
}
$$

也不等於：

$$
\boxed{
\text{Governable Capability}.
}
$$

---

# 13. 治理不透明度：依賴深度還包含「不知道自己依賴誰」

設一項服務 $S$。

若使用者知道：

$$
S
\leftarrow
\{X_1,X_2,X_3\}
$$

並可審計替代路徑，那麼治理透明度較高。

但若：

$$
S
\leftarrow
X_1
\leftarrow
X_2
\leftarrow
X_3
\leftarrow
\cdots
$$

而使用者、組織甚至監管者無法完整掌握供應鏈與依賴關係，則：

$$
d_g
=
\text{Governance Opacity}
$$

上升。

這在數位與雲端系統中尤其重要，因為表面上一個簡單 API、登入服務或支付按鈕，背後可能依賴多層第三方服務。

所以：

$$
\boxed{
\text{Interface Simplicity}
\not\Rightarrow
\text{Dependency Simplicity}.
}
$$

---

# 14. 時間依賴：有些能力不是「有或沒有」，而是「多久能沒有」

CISA 與 NIST 的基礎設施韌性工作都重視恢復與時間維度。NIST 2026 年的 Community Resilience Planning Guide 更新版本進一步以內部／外部、時間、空間與來源等依賴類型來協助規劃。[5]

因此，依賴應加入：

$$
\tau_{\mathrm{tol}}(X)
=
\text{maximum tolerable outage}.
$$

例如：

某項服務停機：

$$
5\text{ seconds}
$$

就不可接受。

另一項：

$$
5\text{ hours}
$$

仍可容忍。

第三項：

$$
5\text{ days}
$$

才形成危機。

因此：

$$
\boxed{
\text{Same Dependency}
+
\text{Different Time Tolerance}
\Rightarrow
\text{Different Risk}.
}
$$

這個時間軸會在後續 AI 基礎設施研究中特別重要，因為 AI 系統若進入即時控制層，其可容忍中斷時間會顯著低於純輔助型工具。

---

# 15. 路徑依賴：不是今天選錯，而是昨天的選擇改變了今天能選什麼

能力環境形成後，文明並不是每天重新從零選擇技術。

假設：

$$
X_t
$$

是當前技術與制度狀態。

則：

$$
X_{t+1}
=
F(
X_t,
I_t,
K_t,
P_t
).
$$

其中 $P_t$ 表示既有基礎設施與歷史承諾。

因此：

$$
X_{t+1}
$$

不只由「哪個技術現在最好」決定。

Unruh 對 carbon lock-in 的經典分析即指出，技術、制度與產業系統可能透過路徑依賴與報酬遞增共同形成長期鎖定，使替代技術即使具有某些優勢，也不容易快速取代既有系統。[6]

本文把這個洞見一般化為能力載體問題：

$$
\boxed{
\text{Current Choice Set}
=
f(
\text{Past Infrastructure}
).
}
$$

因此「把技術拿掉」往往不是回到：

$$
t-1
$$

的世界。

而可能是進入一個：

$$
\boxed{
\text{capability vacuum}
}
$$

因為舊技能、舊制度、舊供應鏈已經在長期演化中消失或退化。

---

# 16. 能力債：表面能力越高，備援能力可能越低

本文提出一個暫定概念：

$$
\boxed{
\text{Capability Debt}
}
$$

能力債不是財務債務，而是：

> 文明透過外部系統取得高水準能力，卻沒有同步投資於替代、恢復、遷移、人工接管與失效隔離時所累積的隱性脆弱性。

令：

$$
C_{\mathrm{nominal}}
=
\text{nominal available capability},
$$

$$
C_{\mathrm{resilient}}
=
\text{capability sustainable under plausible disruptions}.
$$

則概念上：

$$
D_{\mathrm{debt}}
=
C_{\mathrm{nominal}}
-
C_{\mathrm{resilient}}.
$$

當：

$$
D_{\mathrm{debt}}\uparrow,
$$

文明表面上可能非常強，但對某些失效事件高度敏感。

這並不表示高科技文明必然具有高能力債。

相反地，高冗餘、高替代、高互通與高恢復能力的文明可能同時具有：

$$
C_{\mathrm{nominal}}\uparrow
$$

與：

$$
D_{\mathrm{debt}}\downarrow.
$$

---

# 17. 從「使用率」轉向「依賴結構」

科技研究很容易問：

> 有多少人使用這項技術？

例如：

$$
U_X
=
\text{adoption rate}.
$$

但對文明風險而言，使用率不足以描述依賴。

一個娛樂應用可能：

$$
U_X\approx1
$$

卻沒有關鍵基礎設施地位。

另一個後台清算系統可能幾乎沒有一般使用者直接看見，但：

$$
B(X)\gg1.
$$

因此應區分：

$$
\boxed{
\text{Adoption Rate}
\neq
\text{Dependency Centrality}.
}
$$

後續 AI 滲透史也必須遵守相同原則。

「多少手機有 AI」是一個問題。

「多少社會功能在 AI 失效時無法維持」是另一個問題。

---

# 18. AI 為什麼會把這個問題放大？

本文不提前討論 AI 主體性，也不在這一篇定義 AI 奇點。

只處理一個更早發生的問題：

$$
\boxed{
\text{AI can become another infrastructure dependency layer}.
}
$$

若 AI 只提供：

$$
\text{optional assistance},
$$

則失效主要造成效率下降。

若 AI 開始進入：

- 物流；
- 電網；
- 工業控制；
- 醫療調度；
- 軟體維護；
- 金融風控；
- 公共行政；
- 網路安全；

則：

$$
\text{AI Failure}
$$

可能逐漸從：

$$
\text{tool inconvenience}
$$

轉成：

$$
\text{infrastructure degradation}.
$$

OECD 2026 對政府 AI 的分析已明確指出，AI 的有效採用依賴高品質資料、互通的數位公共基礎設施、投資與採購能力以及可治理的公共部門生態。[7]

這意味著 AI 本身並不是漂浮在空中的單一軟體。

它會被嵌入既有依賴圖：

$$
\boxed{
AI
\subset
\mathcal G_{\mathrm{civilization}}.
}
$$

---

# 19. 更重要的反方向：AI 也可能降低依賴深度

本文不能只寫 AI 增加脆弱性。

AI 也可能：

- 自動偵測失效；
- 重新路由；
- 尋找替代供應商；
- 執行降級模式；
- 預測設備故障；
- 協調恢復順序；
- 產生替代程式；
- 自動修補網路。

因此：

$$
\boxed{
AI Penetration
\not\Rightarrow
D_{\mathrm{cap}}\uparrow.
}
$$

真正的關係取決於設計。

一個高度集中、單點依賴的 AI 系統可能增加：

$$
d_b,d_c,d_g.
$$

一個多模型、可離線、可替代、具本地備援的 AI 系統反而可能降低：

$$
d_r,d_s.
$$

所以後續治理不能簡化成：

> AI 越多越危險。

更合理的是：

$$
\boxed{
\text{Risk}
=
f(
\text{penetration},
\text{topology},
\text{substitutability},
\text{recovery},
\text{governance}
).
}
$$

---

# 20. 能力依賴深度矩陣

本文提出一個初步矩陣。

對任一能力載體 $X$：

$$
\mathbf D(X)
=
(
S_X,
R_X,
C_X,
B_X,
T_X,
G_X
).
$$

其中：

| 維度 | 問題 |
|---|---|
| $S_X$ | 是否容易替代？ |
| $R_X$ | 失效後多快能恢復？ |
| $C_X$ | 使用者與控制者距離多遠？ |
| $B_X$ | 失效影響多少下游功能？ |
| $T_X$ | 可容忍中斷多久？ |
| $G_X$ | 依賴鏈是否透明、可審計？ |

為方便比較，可再定義概念性依賴分數：

$$
D^*(X)
=
w_s(1-S_X)
+
w_rR_X
+
w_cC_X
+
w_bB_X
+
w_tT_X
+
w_gG_X.
$$

這不是本文宣稱已經校準完成的實證公式。

它只是一個研究模板。

不同領域必須使用不同尺度與權重。

---

# 21. 域級依賴：文明不是依賴一個工具，而是依賴一組能力域

對文明而言，真正重要的通常不是：

$$
D(X)
$$

而是：

$$
D(\mathcal D)
$$

其中 $\mathcal D$ 是一個功能域。

例如：

$$
\mathcal D_{\mathrm{health}}
$$

可能依賴：

$$
\{
\text{power},
\text{water},
\text{transport},
\text{pharma},
\text{IT},
\text{communications}
\}.
$$

所以：

$$
\boxed{
\text{Domain Capability}
=
F(
\text{multiple infrastructures}
).
}
$$

這也解釋了為什麼 NIST community resilience 研究會把建築、基礎設施、社會功能與經濟功能放在同一個恢復框架中，而不是只研究單一工程設施。[1][5]

---

# 22. 人類的「獨立性」也需要重新定義

如果把獨立理解成：

> 不使用任何外部工具。

那現代文明幾乎沒有實用意義上的獨立人。

因此，更合理的獨立概念應該是：

$$
\boxed{
\text{Autonomy}
\neq
\text{No Dependency}.
}
$$

而可以改成：

$$
\boxed{
\text{Autonomy}
\sim
\text{Ability to choose, replace, exit, recover and govern dependencies}.
}
$$

換句話說：

> 自主並不是沒有關係，而是關係不會把你鎖死到失去選擇。

這一命題後續也能接到「共存不是失敗」的哲學線，但本文暫時只保留技術與制度層含義。

---

# 23. 能力環境與世代差異

當某種能力環境持續存在數十年，世代之間的技能結構可能不同。

令：

$$
K_t
=
\text{skills retained by generation }t.
$$

當外部系統穩定承擔某項任務：

$$
X
\rightarrow
\text{task},
$$

則下一代可能降低對：

$$
K_{\mathrm{fallback}}
$$

的投資。

因此：

$$
\boxed{
\text{Long-term Reliability}
\rightarrow
\text{Lower Incentive for Fallback Skill Maintenance}
}
$$

可能成立。

這不是必然。

航空、核能、醫療等高可靠系統往往會制度化保留備援訓練。

所以真正的問題是：

$$
\boxed{
\text{Does society deliberately preserve fallback capability?}
}
$$

而不是：

> 人是不是因為工具變笨了？

後者過度簡化。

---

# 24. 依賴並非負面詞彙

本文刻意反對：

$$
\text{Dependency}
=
\text{Failure}.
$$

人類文明本來就是互依結構。

專業分工本身就是：

$$
A
\rightarrow
B,
$$

$$
B
\rightarrow
C,
$$

$$
C
\rightarrow
A.
$$

互依可以提高：

- 效率；
- 專業化；
- 創新；
- 規模；
- 複雜協作能力。

真正的問題是：

$$
\boxed{
\text{Unmanaged Dependency}
}
$$

與：

$$
\boxed{
\text{Unrecoverable Dependency}.
}
$$

因此本文的治理方向不是：

$$
\text{Eliminate Dependencies}.
$$

而是：

$$
\boxed{
\text{Make Critical Dependencies Visible, Replaceable, Recoverable and Governable}.
}
$$

---

# 25. 韌性不是「永遠不壞」

如果把韌性定義為：

$$
P(\text{failure})=0,
$$

那幾乎所有複雜系統都會失敗。

更合理的是：

$$
\boxed{
\text{Resilience}
=
\text{withstanding}
+
\text{adapting}
+
\text{recovering}.
}
$$

NIST 目前的 community resilience 定義正強調在特定時間內承受並從破壞中恢復功能。[1]

因此，文明不需要證明：

> 我們永遠不會失去某個外部能力。

而要回答：

> 如果失去，我們如何降級、替代、隔離、恢復？

這直接對應：

$$
C_{\mathrm{resilient}}.
$$

---

# 26. 能力環境的五個相位

本文提出一個初步演化相位。

## $P_0$：Optional Tool

$$
X
=
\text{optional tool}.
$$

移除後影響局部。

## $P_1$：Common Service

$$
X
=
\text{widely used service}.
$$

大量使用，但替代仍容易。

## $P_2$：Shared Infrastructure

$$
X
=
\text{shared infrastructure}.
$$

大量下游功能依賴。

## $P_3$：Institutional Default

$$
X
=
\text{institutional default}.
$$

制度與流程假設它長期存在。

## $P_4$：Capability Environment

$$
X
=
\text{capability environment}.
$$

移除會造成跨領域能力退化，而且社會已很難回到技術採用前的狀態。

這些相位不是不可逆，也不是價值排序。

它們是用來描述「移除成本與依賴拓樸」的研究工具。

---

# 27. 核心命題

本文提出以下九個核心命題。

## 命題 1：能力外部化不等於能力依賴

$$
\boxed{
R_{\mathrm{ext}}
\neq
D_{\mathrm{cap}}.
}
$$

高度外部化系統仍可能具有高韌性。

## 命題 2：依賴深度是多維結構

$$
\boxed{
D_{\mathrm{cap}}
\neq
\text{single adoption rate}.
}
$$

至少需要替代性、恢復性、控制距離、失效半徑、時間容忍與治理透明度。

## 命題 3：依賴拓樸比工具數量更重要

$$
\boxed{
|V|
\not\Rightarrow
R_{\mathrm{system}}.
}
$$

系統風險取決於節點如何耦合。

## 命題 4：基礎設施化使移除成本上升

$$
\boxed{
\text{Infrastructure Integration}
\uparrow
\Rightarrow
\text{Removal Cost}
\uparrow
}
$$

在其他條件相近時通常成立。

## 命題 5：可達能力不等於可控制能力

$$
\boxed{
C_{\mathrm{acc}}
\neq
C_{\mathrm{owned}}
\neq
C_{\mathrm{governable}}.
}
$$

## 命題 6：高可靠性可能降低備援技能投資

$$
\boxed{
\text{Persistent Reliability}
\rightarrow
\text{Fallback Maintenance Incentive}
\downarrow
}
$$

這是一個可檢驗而非必然命題。

## 命題 7：依賴本身不是失敗

$$
\boxed{
\text{Dependency}
\neq
\text{Subordination}
\neq
\text{Fragility}.
}
$$

## 命題 8：韌性依賴恢復，而非零失效

$$
\boxed{
\text{Resilience}
\neq
P(\text{failure})=0.
}
$$

## 命題 9：AI 應被研究為依賴圖的新節點與新層，而非孤立產品

$$
\boxed{
AI
\subset
\mathcal G_{\mathrm{civilization}}.
}
$$

---

# 28. 可檢驗研究計畫

## 28.1 跨國能力依賴深度指數

對不同國家與領域估計：

$$
\mathbf D_{\mathrm{cap}}(
c,
d,
t
).
$$

其中：

$$
c
=
\text{country},
$$

$$
d
=
\text{domain},
$$

$$
t
=
\text{time}.
$$

可比較：

- 電力；
- 通訊；
- 支付；
- 雲端；
- 導航；
- 醫療資訊；
- 政府數位服務。

## 28.2 替代性測試

對特定關鍵服務模擬：

$$
X=0.
$$

測量：

$$
\tau_{\mathrm{switch}},
$$

$$
C_{\mathrm{degraded}},
$$

$$
N_{\mathrm{affected}}.
$$

## 28.3 失效半徑重建

利用事故、停電、雲端中斷、網路中斷資料，重建：

$$
B(X).
$$

驗證表面不可見節點是否具有高 dependency centrality。

## 28.4 世代 fallback skill 研究

比較不同世代在：

- 導航；
- 記憶；
- 基礎計算；
- 離線資訊搜尋；
- 手動操作；

上的備援能力。

核心不是證明新世代「退化」，而是測量：

$$
\text{skill reallocation}.
$$

## 28.5 AI 依賴前置指標

在 AI 尚未全面基礎設施化以前，建立：

$$
D_{AI}(d,t)
$$

追蹤各功能域從：

$$
\text{AI-assisted}
$$

走向：

$$
\text{AI-dependent}
$$

的時間點。

---

# 29. 可反駁條件

本文至少存在以下反駁方向。

1. 若高外部化程度與替代性、恢復性、控制距離、失效半徑之間無法形成任何可操作區分，能力依賴深度概念過度抽象。
2. 若現代基礎設施的跨部門依賴對真實事故與恢復幾乎沒有解釋力，本文對互依拓樸的重要性將被削弱。
3. 若路徑依賴在主要數位與基礎設施系統中不存在，且技術可低成本瞬時回復到先前狀態，本文對 environmentalization 的判斷需大幅修改。
4. 若高替代性並未提高任何實際韌性指標，本文對 substitutability 的重視需要重新評估。
5. 若 AI 大規模導入後仍始終只作為可拔除的非關鍵輔助層，AI dependency layer 的預期應下修。
6. 若高控制距離並不影響遷移、審計、恢復與治理能力， $d_c$ 應移出核心依賴向量。

---

# 30. Non-Claims

本文明確不主張以下命題：

1. 不主張使用工具等於失去自主。
2. 不主張技術依賴必然造成文明脆弱。
3. 不主張現代人應回到低技術生活。
4. 不主張所有基礎設施都應去中心化。
5. 不主張所有集中式系統都不安全。
6. 不主張所有分散式系統都更安全。
7. 不主張備援越多越好而不計成本。
8. 不主張人工流程永遠優於自動流程。
9. 不主張外部化能力必然使內在能力下降。
10. 不主張世代技能變化等於智力退化。
11. 不主張所有網路中斷都會形成 cascading failure。
12. 不主張互依網路理論可直接完整描述真實文明。
13. 不主張 AI 已經是所有國家的關鍵基礎設施。
14. 不主張 AI 滲透必然提高能力依賴深度。
15. 不主張 AI 滲透必然降低能力依賴深度。
16. 不主張所有 AI 都需要離線備援。
17. 不主張所有關鍵功能都應維持完整人工替代。
18. 不主張依賴深度可以用一個固定全球權重計算。
19. 不主張「能力債」已是成熟經濟或工程指標。
20. 不主張路徑依賴表示技術選擇永不可逆。
21. 不主張 infrastructure lock-in 等於法律上的不可退出。
22. 不主張公共數位基礎設施在所有國家都已達同一成熟度。
23. 不主張使用率可以取代 dependency centrality。
24. 不主張本文框架可以取代工程韌性、資安、公共政策或經濟分析。
25. 不主張本文已預測未來 AI 基礎設施的具體失效事件。

---

# 31. 結論：真正的問題不是「有沒有外掛」，而是「能不能退出、替代與恢復」

人類文明從來不是一個沒有依賴的文明。

語言依賴共同規則。

市場依賴信任與制度。

城市依賴電力、水、交通與通訊。

現代數位社會則進一步依賴網路、資料、雲端、數位身分與計算基礎設施。

因此：

$$
\boxed{
\text{Civilization}
\Rightarrow
\text{Interdependence}.
}
$$

真正值得研究的不是如何消滅所有依賴，而是：

$$
\boxed{
\text{Which dependencies are critical?}
}
$$

$$
\boxed{
\text{Which are replaceable?}
}
$$

$$
\boxed{
\text{Which can recover?}
}
$$

$$
\boxed{
\text{Which failures cascade?}
}
$$

$$
\boxed{
\text{Who controls the substrate?}
}
$$

以及：

$$
\boxed{
\text{Can the system still choose another path?}
}
$$

這就是本文提出「能力依賴深度」的目的。

EXS-01 的核心是：

$$
\boxed{
\text{Internal Capability}
\neq
\text{Accessible Capability}.
}
$$

EXS-02 再補上一條：

$$
\boxed{
\text{Accessible Capability}
\neq
\text{Resilient Capability}.
}
$$

於是文明能力的完整度量至少需要：

$$
\boxed{
C_{\mathrm{int}},
C_{\mathrm{acc}},
C_{\mathrm{fallback}},
C_{\mathrm{resilient}}.
}
$$

當外部載體仍是工具時，能力外部化主要是增益問題。

當外部載體變成環境時，能力外部化開始同時成為：

$$
\boxed{
\text{Resilience}
+
\text{Governance}
+
\text{Dependency Topology}
}
$$

問題。

而下一篇 EXS-03 將把這條線拉進認知與計算史：

> 人類是如何從算盤、數表與機械計算，走到把龐大的數學、模擬與預測交給計算機與超算，再走向 AI 認知委託的？

---

# 參考文獻

[1] National Institute of Standards and Technology (NIST). **Community Resilience Program / Community Resilience Research.** NIST 將 community resilience 描述為準備、適應、承受破壞並在特定時間框架內恢復的能力；其研究同時考慮建築、基礎設施與社會經濟功能的互依。本文於 2026-08-18 重新核對。

[2] Cybersecurity and Infrastructure Security Agency (CISA). **Infrastructure Dependency Primer.** CISA 將依賴區分為單向或雙向、上游或下游，並指出電力、通訊與資訊科技等部門對其他關鍵基礎設施存在廣泛跨部門依賴。本文於 2026-08-18 重新核對。

[3] Buldyrev, S. V., Parshani, R., Paul, G., Stanley, H. E., & Havlin, S. (2010). **Catastrophic cascade of failures in interdependent networks.** *Nature*, 464, 1025–1028. 本文引用其互依網路中連鎖失效的理論結果作為 dependency topology 的基礎參照，不把該模型直接等同所有真實基礎設施。

[4] OECD. (2026). **Digital Government Outlook 2026: Strengthening digital public infrastructure and data governance.** OECD 將共享數位基礎設施、互通性、資料治理、韌性與可持續性視為現代數位政府的重要基礎。

[5] National Institute of Standards and Technology (NIST). (2026). **Community Resilience Planning Guide for Buildings and Infrastructure Systems, Special Publication 1190, Version 2.** 更新版將社區功能與基礎設施恢復的依賴關係納入規劃，並明確處理內外部、時間、空間與來源等依賴。

[6] Unruh, G. C. (2000). **Understanding carbon lock-in.** *Energy Policy*, 28(12), 817–830. 本文借用其技術與制度共同演化、路徑依賴與 lock-in 的一般洞見，不把所有能力依賴等同碳鎖定。

[7] OECD. (2026). **Digital Government Outlook 2026: Adopting and governing AI in government.** OECD 指出 AI 導入依賴高品質資料、互通數位公共基礎設施、投資與採購制度，以及能開發、治理與監督 AI 的組織能力。

[8] CISA. **Critical Infrastructure Security and Resilience / Critical Infrastructure Sectors.** CISA 將多個實體與虛擬資產、系統與網路視為維持國家與社會功能的重要關鍵基礎設施，並強調跨部門協調與韌性。

[9] OECD. (2026). **The OECD Going Digital Integrated Policy Framework 2026.** 該框架強調數位轉型對經濟與社會產生廣泛且複雜的影響，並使政策目標之間的權衡更難以用單一維度處理。

---

# 附錄 A｜最小符號表

| 符號 | 意義 |
|---|---|
| $C_{\mathrm{int}}$ | 內在能力 |
| $C_{\mathrm{acc}}$ | 可達能力 |
| $C_{\mathrm{fallback}}$ | 外部層失效後剩餘能力 |
| $C_{\mathrm{resilient}}$ | 可在合理失效情境下持續或恢復的能力 |
| $R_{\mathrm{ext}}$ | 能力外部化比例 |
| $D_{\mathrm{cap}}$ | 能力依賴深度 |
| $S_X$ | 替代性 |
| $\tau_{\mathrm{rec}}$ | 恢復時間 |
| $\tau_{\mathrm{tol}}$ | 最大可容忍中斷時間 |
| $d_c$ | 控制距離 |
| $d_b$ | 失效半徑 |
| $d_g$ | 治理不透明度 |
| $B(X)$ | 節點 $X$ 的概念性失效影響集合 |
| $\mathcal G$ | 基礎設施依賴圖 |
| $D_{\mathrm{debt}}$ | 概念性能力債 |

---

# 附錄 B｜EXS-01 → EXS-02 的理論增量

EXS-01：

$$
\boxed{
\text{Human Capability}
\neq
\text{Biological Capability Only}.
}
$$

EXS-02：

$$
\boxed{
\text{External Capability}
\neq
\text{Automatically Resilient Capability}.
}
$$

合併：

$$
\boxed{
\text{Capability Gain}
\rightarrow
\text{Dependency Structure}
\rightarrow
\text{Resilience Requirement}.
}
$$

---

# 附錄 C｜系列後續接口

下一篇：

**EXS-03｜從算盤到超算：計算委託與人類認知外包史**

主線將轉向：

$$
\boxed{
\text{External Representation}
\rightarrow
\text{Mechanical Calculation}
\rightarrow
\text{Electronic Computation}
\rightarrow
\text{Supercomputing}
\rightarrow
\text{Cognitive Delegation}.
}
$$

EXS-03 將特別處理：

- 算盤與機械計算的角色；
- 數值天氣預報；
- 科學計算；
- 超級電腦；
- 人類如何從「自己算」走到「讓機器算、自己解讀」；
- 計算委託如何成為 AI 認知委託的歷史前身。
