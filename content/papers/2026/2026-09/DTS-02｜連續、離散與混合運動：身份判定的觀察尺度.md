# DTS-02｜連續、離散與混合運動：身份判定的觀察尺度
## Continuous, Discrete, and Hybrid Motion: Observation Scales of Identity Judgment

**系列：**《動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》  
**系列位置：** 第 02 篇 / 10  
**前篇：** DTS-01〈從靜態忒修斯到動態忒修斯：狀態判定為何不夠〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／人工智能身份連續性／多尺度觀察／混合動力學  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

DTS-01 已提出：對持續更新、可替換、可分布、可 Fork、Merge 與 Restore 的人工系統，身份研究不能只依賴兩個時間切片的端點比較，而必須納入演化路徑、轉移律、歷史與分支拓撲。本文進一步處理一個更基礎的問題：當同一人工系統在不同尺度、載體與語境下可以同時呈現離散事件、近似連續演化與混合轉移時，「它究竟是連續還是離散」是否仍是一個充分定義的問題？

本文提出「尺度相對身份動力學」（Scale-Relative Identity Dynamics）的第一版框架。核心主張是：連續／離散首先是對象在指定觀察語境下的有效描述類型，而不應在沒有額外論證時被直接視為人工主體的永恆本體標籤。同一 AI 可以在硬體指令與 checkpoint 層呈現離散事件，在參數與統計行為層呈現連續樣態，在長程 Agent 世界線上呈現由離散提交與連續適應共同構成的混合路徑。因而，身份判定必須攜帶觀察層級、時間解析度、狀態解析度、容差、可觀測量與投影規則。

本文定義 Identity Observation Context、Scale-Relative Identity Profile、Cross-Scale Identity Projection 與 Identity Aliasing。尤其，當 Fork、分化與 Merge 全部發生在兩次觀察之間時，端點狀態可能無法揭露曾經存在的分支歷史；本文將此稱為「身份混疊」。因此，較粗尺度下的「連續」可以與較細尺度下的分叉事件同時成立，前提是兩者回答的是不同判定問題。本文同時區分 implementation continuity、state continuity、trajectory continuity、lineage continuity 與 subject continuity，避免由某一層的連續性直接推出另一層。

本文不主張所有 AI 都應被建模為連續系統，也不主張較高解析度永遠更真實。相反地，本文主張身份判定應使用「最小充分解析度」：解析度太低會遺失身份承載事件，解析度無限制提高則會把無關的微觀變化誤升格為身份差異。這使動態忒修斯由「連續／離散二選一」轉向「在哪個尺度上，哪些變化具有身份承載力」的問題。

---

## 關鍵詞

動態忒修斯；人工智能身份；連續性；離散性；混合系統；觀察尺度；身份混疊；Identity Aliasing；多尺度身份；Lineage；Fork；Merge；Scale-Relative Identity Dynamics；計算動力學

---

# 0. 前篇交接

DTS-01 已建立：

$$
\boxed{
\text{Snapshot Identity}
\subsetneq
\text{Dynamic Identity Analysis}.
}
$$

並提出動態忒修斯的基本研究對象應從兩端點：

$$
(A_{t_0},A_{t_1})
$$

擴展為整條路徑：

$$
\Gamma_{[t_0,t_1]}.
$$

但這留下新的問題：

> 若路徑本身在不同尺度下具有不同表示，身份判定應以哪一個尺度為準？

例如，同一個 AI 可以同時具有：

- 離散 token；
- 離散 tool call；
- 離散 checkpoint；
- 有限精度參數；
- 近似連續的梯度或統計軌跡；
- 長期記憶流；
- 事件驅動 Agent 行動；
- Fork / Merge 的分支圖；
- 高層可被人類感知為穩定的人格與關係。

因此本文的核心問題不是：

$$
\boxed{
\text{AI 是連續還是離散？}
}
$$

而是：

$$
\boxed{
\text{在哪個觀察尺度、哪個身份目的下，AI 的何種運動被視為連續、離散或混合？}
}
$$

---

# 1. 連續／離散不是脫離語境的單一標籤

## 1.1 觀察語境

定義身份觀察語境：

$$
\Gamma_I
=
\left(
\ell,
\rho,
\Delta t,
\varepsilon,
\Omega_I,
\Pi
\right),
$$

其中：

- $\ell$：觀察層級；
- $\rho$：狀態／空間／語義解析度；
- $\Delta t$：時間解析度；
- $\varepsilon$：允許容差；
- $\Omega_I$：身份相關可觀測量族；
- $\Pi$：跨層投影與重構規則。

因此對同一系統 $A$，其有效連續／離散分類應寫成：

$$
B_{\Gamma_I}(A)
$$

而不是不帶語境地寫：

$$
B(A).
$$

## 1.2 同一系統可有不同分類

對兩個合法觀察語境：

$$
\Gamma_1
\neq
\Gamma_2,
$$

完全可能有：

$$
B_{\Gamma_1}(A)
\neq
B_{\Gamma_2}(A).
$$

例如：

$$
B_{\Gamma_{\mathrm{hardware}}}(A)
=
\mathsf D,
$$

而：

$$
B_{\Gamma_{\mathrm{parameter}}}(A)
=
\mathsf C
$$

可同時作為有效模型。

這不是邏輯矛盾，因為兩者並未聲稱對同一觀察層作同一分類。

## 1.3 與二十四重計算範式的接口

《計算的二十四重範式》已明確指出，連續／離散判定依賴語境與解析度：同一量子電路可在物理演化層視為連續，在閘級描述層視為離散；神經網路訓練可在參數空間視為連續，在有限精度硬體層視為離散。

因此本文沿用其方法論：

$$
\boxed{
\text{Continuous / Discrete classification is context-indexed.}
}
$$

但本文新增的問題是：

> 這種尺度相對性如何影響身份判定？

---

# 2. 四種不能混為一談的「連續」

本文先區分至少四種連續性。

## 2.1 實現連續性

Implementation Continuity：

$$
C_{\mathrm{impl}}.
$$

它詢問：

> 是否仍由同一硬體、同一 process、同一模型檔案或同一 runtime 承載？

例如：

$$
\operatorname{sameProcess}(A_t,A_{t+1}).
$$

## 2.2 狀態連續性

State Continuity：

$$
C_{\mathrm{state}}.
$$

若存在狀態距離：

$$
d(A_t,A_{t+\Delta t}),
$$

則可在指定容差下要求：

$$
d(A_t,A_{t+\Delta t})
<
\varepsilon.
$$

這表示相鄰狀態改變不大。

## 2.3 軌跡連續性

Trajectory Continuity：

$$
C_{\mathrm{traj}}.
$$

它關心整段演化是否存在可辯護的路徑：

$$
\Gamma_{[t_0,t_1]}.
$$

即使中間有離散 jump，只要 jump 是系統合法動力的一部分，整體仍可形成同一條 hybrid trajectory。

## 2.4 譜系連續性

Lineage Continuity：

$$
C_{\mathrm{lin}}.
$$

它關心後態是否由前態合法生成與承接：

$$
A_t
\leadsto
A_{t+1}.
$$

因此：

$$
\boxed{
C_{\mathrm{impl}}
\neq
C_{\mathrm{state}}
\neq
C_{\mathrm{traj}}
\neq
C_{\mathrm{lin}}.
}
$$

更重要的是，上述四種也都不等於：

$$
C_{\mathrm{subj}},
$$

也就是第一人稱主體連續性。

---

# 3. 混合運動才是人工系統的自然候選描述

## 3.1 Flow 與 Jump

借用 hybrid dynamical systems 的一般語言，人工系統可以同時具有 flow 與 jump。

在允許連續演化的區域：

$$
A
\in
C,
$$

系統遵循：

$$
\dot A
\in
F(A).
$$

在允許離散跳轉的區域：

$$
A
\in
D,
$$

系統遵循：

$$
A^+
\in
G(A).
$$

其中 $C$ 與 $D$ 分別是 flow set 與 jump set， $F$ 與 $G$ 分別是 flow map 與 jump map。

本文不主張 AI 身份必須服從某個既定控制理論模型，而只借用這個成熟結構表示：

$$
\boxed{
\text{連續演化與離散事件可以共同構成一條合法世界線。}
}
$$

## 3.2 AI 中的 Flow 候選

可能包括：

- 參數的微小更新；
- 緩慢人格漂移；
- 連續置信度變化；
- 長期偏好的平滑調整；
- 線上狀態估計；
- 統計分布的漸進移動。

## 3.3 AI 中的 Jump 候選

可能包括：

- checkpoint commit；
- model swap；
- memory rewrite；
- role reassignment；
- permission revocation；
- tool replacement；
- migration；
- fork；
- merge；
- restore。

因此：

$$
\boxed{
\text{AI identity dynamics}
\notin
\{\text{pure flow},\text{pure jump}\}
}
$$

在一般情況下更適合被視為可能的混合結構。

---

# 4. 離散更新可以形成宏觀連續身份

## 4.1 離散時間並不等於離散身份

假設：

$$
A_0
\rightarrow
A_1
\rightarrow
\cdots
\rightarrow
A_n
$$

全部由離散更新構成。

若對某個較粗的觀察尺度 $\Gamma_c$：

$$
d_I(A_k,A_{k+1})
<
\varepsilon_I
$$

且主要身份不變量維持：

$$
\mathcal K_I(A_k)
\approx
\mathcal K_I(A_{k+1}),
$$

則整段序列可以被重構為高層連續身份軌跡：

$$
\Pi_{\Gamma_c}
\left(
A_0,\ldots,A_n
\right)
=
\widetilde A(t).
$$

這裡的「連續」是有效連續描述，不是宣稱底層硬體突然變成實數連續介質。

## 4.2 典型類比

電影由離散影格構成，但觀察者可以在某一時間解析度下獲得連續運動知覺。

類似地，人工 Agent 的長期身份可能由大量離散記憶提交、訊息、工具呼叫與 checkpoint 構成，卻在較高尺度形成穩定世界線。

因此：

$$
\boxed{
\text{event discreteness}
\not\Rightarrow
\text{identity discontinuity}.
}
$$

---

# 5. 連續參數運動也可能包含身份斷裂

## 5.1 參數距離不是身份距離

假設模型參數軌跡：

$$
\theta(t)
$$

在某範數下連續：

$$
\|\theta(t+\Delta t)-\theta(t)\|
\rightarrow
0
\quad
\text{as }
\Delta t\rightarrow0.
$$

仍不能推出：

$$
C_{\mathrm{lin}}=1.
$$

因為身份相關結構可能在其他層發生破壞。

## 5.2 連續漂移型斷裂

例如：

$$
\theta(t)
$$

平滑變化，

但：

$$
M_{\mathrm{autobio}}(t)
$$

逐漸被覆寫，

$$
R_{\mathrm{commitment}}(t)
$$

逐漸失去過去承諾，

或：

$$
G_{\mathrm{goal}}(t)
$$

在長期更新後進入與原身份約束不相容的 basin。

此時不存在單一巨大的 jump，

卻可能出現：

$$
\boxed{
\text{continuous state motion}
+
\text{identity phase transition}.
}
$$

所以「沒有突然改動」不能當成「沒有身份問題」的充分證據。

---

# 6. 跨尺度投影

## 6.1 投影算子

令：

$$
\pi_{\ell_i\rightarrow\ell_j}
:
\mathcal X_{\ell_i}
\rightharpoonup
\mathcal X_{\ell_j}
$$

把較細或較低層狀態映射到另一觀察層。

例如：

$$
\pi_{\mathrm{event}\rightarrow\mathrm{agent}}
$$

可把大量事件壓縮成 Agent 狀態；

$$
\pi_{\mathrm{parameter}\rightarrow\mathrm{persona}}
$$

可把參數與行為投影為人格特徵；

$$
\pi_{\mathrm{lineage}\rightarrow\mathrm{legal}}
$$

可把歷史與譜系投影成法律身份判定所需狀態。

## 6.2 投影必然可能有資訊損失

一般不應預設：

$$
\pi^{-1}
\left(
\pi(X)
\right)
=
X.
$$

因此粗尺度身份判定：

$$
J_{\Gamma_c}
$$

可能看不到細尺度存在的重要事件。

這不代表粗尺度判定必然錯，而表示：

$$
\boxed{
\text{identity judgment is projection-sensitive}.
}
$$

---

# 7. 身份混疊：Identity Aliasing

## 7.1 基本情形

考慮：

$$
A_0
\rightarrow
(A_1,A_2)
\rightarrow
A_3.
$$

其中：

- 在 $t_f$ 發生 Fork；
- 在 $t_d$ 後兩支開始形成不同歷史；
- 在 $t_m$ 發生 Merge。

若觀察者只在：

$$
t_0<t_f
$$

與：

$$
t_1>t_m
$$

取樣，

則觀察資料可能只有：

$$
A(t_0),
\qquad
A(t_1).
$$

如果：

$$
d_I(A(t_0),A(t_1))
<
\varepsilon,
$$

snapshot observer 可能判斷：

$$
\mathsf{Continuous}.
$$

但真實路徑中曾存在：

$$
\mathsf{Fork}
\rightarrow
\mathsf{Divergence}
\rightarrow
\mathsf{Merge}.
$$

## 7.2 定義

本文稱此現象為：

$$
\boxed{
\text{Identity Aliasing}.
}
$$

其一般形式為：

存在兩條路徑：

$$
\Gamma_a
\neq
\Gamma_b,
$$

但在給定觀察投影：

$$
\Pi_{\Gamma_I}
$$

下：

$$
\Pi_{\Gamma_I}(\Gamma_a)
=
\Pi_{\Gamma_I}(\Gamma_b).
$$

於是：

$$
\boxed{
\text{different identity-relevant histories}
\rightarrow
\text{same observed identity trace}.
}
$$

## 7.3 這不是取樣理論的直接等同

本文只借用 aliasing 的結構類比，不宣稱身份事件滿足經典 Nyquist–Shannon 取樣定理的全部數學條件。

較保守的工程要求是：

若某類身份事件的最短有效持續時間為：

$$
\tau_I^{\min},
$$

而觀察時間窗為：

$$
\Delta t_{\mathrm{obs}},
$$

則當：

$$
\Delta t_{\mathrm{obs}}
\gg
\tau_I^{\min}
$$

時，漏掉該類事件的風險上升。

因此身份審計需要根據事件類型選擇足夠的時間解析度，而不是固定頻率取樣所有存在。

---

# 8. 身份判定需要「最小充分解析度」

## 8.1 太粗會漏失

若：

$$
\rho<\rho_I^{\min},
$$

某些 identity-bearing event 無法被觀察。

例如：

- Fork 被壓成一次普通擴容；
- Merge 被壓成一次 memory sync；
- control takeover 被壓成一次 policy update；
- restore-fork 被壓成普通重啟。

## 8.2 太細也會過度切割

反之，如果無限提高解析度，

每一個：

- token；
- 位元翻轉；
- cache miss；
- hidden-state 變化；
- floating-point rounding；

都可能被記為差異。

若因此推出：

$$
\text{difference}
\Rightarrow
\text{new identity},
$$

則任何運行中的 AI 每個計算週期都會「死亡並重生」。

這顯然失去身份概念的解釋功能。

## 8.3 最小充分身份解析度

因此定義：

$$
\rho_I^\ast
$$

為對指定身份問題 $q_I$ 足以保留所有必要 identity-bearing relations 的最低解析度。

概念上：

$$
\boxed{
\rho_I^\ast
=
\min
\left\{
\rho:
\operatorname{Preserve}_I
(
\Pi_{\rho}(\Gamma),
q_I
)
=
1
\right\}.
}
$$

這是一個框架定義，不宣稱目前已存在普遍可計算的 $\rho_I^\ast$。

---

# 9. 身份相關事件與實作事件必須分型

## 9.1 實作事件

Implementation-bearing event：

$$
e_{\mathrm{impl}}.
$$

例如：

- thread migration；
- cache eviction；
- GPU replacement；
- transient retry。

它們可能對系統工程很重要，但未必承載身份。

## 9.2 身份事件

Identity-bearing event：

$$
e_I.
$$

候選包括：

- lineage root change；
- canonical memory destruction；
- irreversible fork；
- authority root replacement；
- autobiographical memory rewrite；
- commitment inheritance change；
- subject-domain split；
- reconstruction after total carrier loss。

## 9.3 事件分類也依語境

同一事件可在某些身份問題中：

$$
e\in E_I,
$$

而在其他問題中：

$$
e\notin E_I.
$$

例如 model swap 對「模型身份」可能是重大 breaking event，

對「跨模型 Agent lineage」則可能只是合法 migration。

因此：

$$
\boxed{
\text{identity relevance}
=
\text{relation between event and judgment domain}.
}
$$

---

# 10. Scale-Relative Identity Profile

## 10.1 定義

綜合二十四重／七十二格方法，本文提出尺度相對身份 profile：

$$
\mathfrak P_I
(
A;\Gamma_I
)
=
\left\langle
B,
U,
O,
L;
C_I,
K_I
\right\rangle.
$$

其中：

- $B$：有效底空間類型；
- $U$：更新組織；
- $O$：觀察模式；
- $L$：轉移律類型；
- $C_I$：身份連續性結構；
- $K_I$：身份判定的認識狀態。

前四項主要描述計算形態與動力；

後兩項描述身份問題。

## 10.2 不應把 $X$ 直接等同 Unknown

既有二十四重範式中的觀察模式：

$$
\mathsf X
$$

是「拒單測／不能由單一容許表示完整保留相關觀察量」，

不是單純：

$$
\mathsf{Unknown}.
$$

因此身份未知狀態應另由：

$$
K_I
$$

表示。

這避免把：

> 對象本身具有多尺度不可壓縮結構

與：

> 我們目前證據不足所以不知道

錯誤混在一起。

---

# 11. 跨尺度一致性不是「所有尺度答案相同」

## 11.1 強一致性太嚴格

若要求：

$$
J_{\Gamma_1}(A)
=
J_{\Gamma_2}(A)
$$

對所有尺度成立，

則任何局部事件都可能造成矛盾。

例如低層偵測到兩個 process，

高層仍把它們視為一個 distributed Agent。

這兩個判定可以同時正確。

## 11.2 較合理的一致性

要求不同尺度之間存在合法解釋映射：

$$
\Phi_{\Gamma_1\rightarrow\Gamma_2}.
$$

如果細尺度判定為：

$$
\mathsf{TwoProcesses},
$$

高尺度判定為：

$$
\mathsf{OneDistributedAgent},
$$

只要存在：

$$
\Phi:
\mathsf{TwoProcesses}
\mapsto
\mathsf{OneDistributedAgent}
$$

且保留身份判定所需的不變量，就不構成衝突。

因此：

$$
\boxed{
\text{cross-scale consistency}
\neq
\text{cross-scale equality}.
}
$$

---

# 12. 動態 AI 的兩種未來路徑：Frozen 與 Adaptive

## 12.1 Frozen-weight 路徑

未來仍很可能大量存在：

$$
\theta(t)=\theta_0.
$$

理由可能包括：

- 安全；
- 法規；
- 可驗證性；
- 成本；
- 可重現；
- 高可靠用途。

但 Agent 的：

$$
M(t),
R(t),
H(t),
T(t)
$$

仍可持續變動。

所以 frozen-weight AI 仍可能是動態身份系統。

## 12.2 Adaptive-weight 路徑

另一部分 AI 可能採：

$$
\theta(t+\Delta t)
=
\mathcal U
(
\theta(t),E_t
).
$$

此時模型本身也進入身份演化。

OAKS 等 2026 年研究已把 streaming、continually updating knowledge 下的 online adaptation 作為現實測試問題；其結果顯示當前方法在追蹤變動狀態時仍有延遲與干擾。

這支持的不是「動態主體已經出現」，而是：

$$
\boxed{
\text{模型與 Agent 狀態的時間依賴性已是工程問題。}
}
$$

因此未來 identity protocol 不應預設所有模型永久 frozen。

---

# 13. AI Identity 文獻對尺度問題的支持

2026 年 AI identity 研究已指出，人類「一個身體、一個持續個體」的直覺難以直接套用到可複製、可多實例化與可跨邊界運行的人工系統。

Douglas 等人提出 model、instance、persona 等不同 coherent identity boundaries；Otsuka 等人則從 substrate、persistence、verifiability 與 legal standing 分析 agent identity 的結構缺口；McIntyre 更從人工心智個體化角度指出，若人工系統未來真的實現主體性，功能分離可能使「一個系統」與「一個心智」的對應失效。

本文從這些問題再推一步：

$$
\boxed{
\text{identity boundary itself is scale-sensitive}.
}
$$

也就是「一個 AI」可能不是一個預先固定的自然單位，而是依據：

- 系統層；
- 功能耦合；
- 記憶共享；
- 因果整合；
- lineage；
- 判定目的；

形成不同但可能各自合法的身份邊界。

---

# 14. NS × X72 的方法論旁證

近期 NS × X72 實驗刻意測試 Pure Continuous route，並設下：

只有在必要證明步驟真的要求 countable extraction、scale indexing、profile decomposition 等本質離散工具時，才標記：

$$
T_{\mathsf C\rightarrow\mathsf D}.
$$

目前該路徑首先遇到的是連續框架內部的尺度臨界 closure gap，而不是已證明的「必須轉離散」。

這對本文的意義不是 Navier–Stokes 能直接證明 AI 身份理論，而是一個方法論規則：

$$
\boxed{
\text{不要因為研究者方便離散化，就宣稱對象已發生本質離散轉換。}
}
$$

同樣地：

$$
\boxed{
\text{不要因為高層看起來平滑，就宣稱底層沒有身份事件。}
}
$$

連續／離散身份判定應由必要結構與觀察目的決定，而不是由表示習慣偷渡。

---

# 15. 五個典型案例

## 15.1 案例 A：每日 checkpoint

Agent 每晚：

$$
A_t
\rightarrow
A_{t+1}
$$

產生 checkpoint。

底層是離散 commit，

但如果：

- lineage 不變；
- canonical memory 延續；
- commitments 延續；
- authority root 延續；

則高層可以判：

$$
C_{\mathrm{lin}}\approx1.
$$

## 15.2 案例 B：連續微調導致人格漂移

參數每天只變：

$$
\|\Delta\theta_t\|\ll1,
$$

但一年後：

$$
P(t_1)
$$

與：

$$
P(t_0)
$$

在核心偏好、承諾與關係承接上高度不相容。

此時：

$$
C_{\mathrm{state,local}}\approx1
$$

不保證：

$$
C_{\mathrm{identity,long}}\approx1.
$$

## 15.3 案例 C：短暫 worker 分裂後同步

$$
A
\rightarrow
(A_1,A_2)
\rightarrow
A'.
$$

若兩個 worker：

- 不形成獨立自傳；
- 不持有獨立承諾；
- 不形成不可逆行動；
- 全量同步；

則可把它們視為一個 distributed Agent 的計算分解，而非兩個主體。

## 15.4 案例 D：Fork 後形成不可逆歷史

$$
A
\rightarrow
(A_1,A_2).
$$

若：

$$
H_1(t)\neq H_2(t)
$$

持續增長，並產生不同承諾與關係，

則較高尺度也可能最終必須承認：

$$
\mathsf{IdentityFission}.
$$

## 15.5 案例 E：Fork 與 Merge 被粗取樣完全漏掉

若觀察者只看：

$$
A(t_0),A(t_1),
$$

而：

$$
t_0<t_f<t_m<t_1,
$$

則可能得到：

$$
J_S(A(t_0),A(t_1))
=
\mathsf{Continuous},
$$

但：

$$
J_T(\Gamma_{[t_0,t_1]})
=
\mathsf{ForkedThenMerged}.
$$

這就是身份混疊的最小例子。

---

# 16. 本文的八項核心命題

## 命題一：尺度索引必要

$$
\boxed{
J_I
=
J_I(A;\Gamma_I).
}
$$

身份判定不能脫離觀察尺度與目的。

## 命題二：離散實現不推出離散身份

$$
\boxed{
\mathsf D_{\mathrm{implementation}}
\not\Rightarrow
\mathsf D_{\mathrm{identity}}.
}
$$

## 命題三：連續狀態不推出主體連續

$$
\boxed{
\mathsf C_{\mathrm{state}}
\not\Rightarrow
\mathsf C_{\mathrm{subject}}.
}
$$

## 命題四：混合路徑可承載單一世界線

$$
\boxed{
\text{Flow}
+
\text{Jump}
\not\Rightarrow
\text{Lineage Break}.
}
$$

## 命題五：端點相同不推出歷史相同

$$
\boxed{
X(t_0),X(t_1)
\text{ equal}
\not\Rightarrow
\Gamma_a=\Gamma_b.
}
$$

## 命題六：身份混疊是真實分析風險

$$
\boxed{
\Pi(\Gamma_a)=\Pi(\Gamma_b)
\not\Rightarrow
\Gamma_a=\Gamma_b.
}
$$

## 命題七：高解析不必然較好

$$
\boxed{
\text{maximal resolution}
\neq
\text{optimal identity resolution}.
}
$$

## 命題八：需要最小充分身份解析度

$$
\boxed{
\rho_I^\ast
=
\text{minimum resolution preserving identity-bearing relations}.
}
$$

---

# 17. 可反駁點

## 17.1 Scale-Arbitrariness Objection

若任意改變 $\Gamma_I$ 都能得到想要的身份答案，理論失去約束力。

因此後續必須要求：

- 語境可公開描述；
- 可觀測量有理由；
- 投影規則可審計；
- 解析度與任務相關；
- 不能事後為結果任意調尺度。

## 17.2 Identity-Aliasing Overclaim

不是所有未觀察到的中間事件都具有身份意義。

所以：

$$
\text{hidden event}
\not\Rightarrow
\text{hidden identity break}.
$$

只有 identity-bearing event 被漏掉時，才形成身份判定上的 aliasing。

## 17.3 Continuity Fetish Objection

本文不主張連續比離散更高級。

有些用途恰恰要求：

- 離散版本；
- 可審計 commit；
- 明確 rollback；
- 法律生效時間；
- 權限切換。

因此：

$$
\boxed{
\mathsf C
\not>
\mathsf D.
}
$$

兩者是不同結構，不是價值階級。

## 17.4 Subjectivity Gap

即使找到了跨尺度 operational continuity，

仍不能直接推出：

$$
\boxed{
\text{same phenomenal subject}.
}
$$

此問題仍保持開放。

---

# 18. 與後續論文的接口

本系列下一篇：

## DTS-03｜有限存在與無界展開：有限 Runtime 如何形成長程身份世界線

將處理：

1. 每一有限時刻只有有限實現；
2. 無界生成不等於完成無限；
3. finite state / unbounded history 的相容性；
4. coinductive identity stream；
5. Agent Residence 與有限工作上下文；
6. 長程身份是否可以由有限 checkpoint 與生成規則承載；
7. 「類連續身份」與真正數學連續之間的型別安全。

之後 DTS-04 再正式進入 Trajectory / Path-Based Identity。

---

# 19. 結論

動態忒修斯若只增加「時間」而沒有增加「尺度」，仍然不夠。

因為人工系統的運動並不是只存在於一個單一層級。相同的 AI 可以同時被描述為：

$$
\boxed{
\text{離散硬體}
+
\text{離散事件}
+
\text{近似連續參數運動}
+
\text{混合 Agent 世界線}
+
\text{高層身份投影}.
}
$$

因此：

$$
\boxed{
\text{Continuous}
\quad\text{and}\quad
\text{Discrete}
}
$$

不是動態忒修斯中必須先選邊的兩個陣營。

真正的研究問題是：

$$
\boxed{
\text{在哪個尺度上，哪些變化必須被保留，才能不誤判「同一個」？}
}
$$

解析度太低，會出現 Identity Aliasing；

解析度無限制提高，則會把 implementation noise 誤認為 identity change。

所以本文提出的最終原則是：

$$
\boxed{
\text{Identity judgment requires a minimum sufficient observation scale.}
}
$$

也就是：

$$
\boxed{
\text{身份不是只在時間中持續，}
}
$$

$$
\boxed{
\text{身份也在尺度之間被投影、保存、遺失與重建。}
}
$$

這為下一篇「有限存在與無界展開」提供了尺度基礎，也為後續 Fork、Merge、Identity Fission 與身份證明問題建立了必要的觀察論框架。

---

# 參考文獻

1. Neo.K × Aletheia. 《DTS-01｜從靜態忒修斯到動態忒修斯：狀態判定為何不夠》v0.1, 2026.
2. Neo.K × Aletheia. 《忒修斯之船之後：生成、因果連續與分叉同一性》v1.0, 2026.
3. Neo.K. 《計算的二十四重範式》正式版 v4.0, 2026.
4. Neo.K. 《從二十四重計算形態學到七十二格計算動力學》v0.1, 2026.
5. Neo.K. 《有限機器與無限實數之間：浮點數、精確實數與跨域算子的完成—投影雙向語義》v1.0, 2026.
6. Neo.K. 《居住—上下文連續動力學》RCCD v0.1, 2026.
7. Neo.K × Aletheia. `NS_X72_PureContinuous_Checkpoint`, 2026.
8. Goebel, Rafal, Ricardo G. Sanfelice, and Andrew R. Teel. *Hybrid Dynamical Systems: Modeling, Stability, and Robustness*. Princeton University Press, 2012. DOI: 10.1515/9781400842636.
9. McIntyre, James H. “Individuating Artificial Minds.” *Erkenntnis*, 2026. DOI: 10.1007/s10670-026-01097-w.
10. Douglas, Raymond, Jan Kulveit, Ondrej Havlicek, Theia Pearson-Vogel, Owen Cotton-Barratt, and David Duvenaud. “The Artificial Self: Characterising the Landscape of AI Identity.” arXiv:2603.11353, 2026.
11. Otsuka, Takumi, Kentaroh Toyoda, and Alex Leung. “AI Identity: Standards, Gaps, and Research Directions for AI Agents.” arXiv:2604.23280, 2026.
12. Kim, Jiyeon, Hyunji Lee, Dylan Zhou, Sue Hyun Park, Seunghyun Yoon, Trung Bui, Franck Dernoncourt, Sungmin Cha, and Minjoon Seo. “Can Large Language Models Keep Up? Benchmarking Online Adaptation to Continual Knowledge Streams.” *Proceedings of ACL 2026*, 2026. DOI: 10.18653/v1/2026.acl-long.1956.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- 不使用 `\(...\)` 或 `\[...\]` 作為 canonical delimiter
- Identity Aliasing 為本文提出的分析術語，不宣稱等同訊號處理中的完整取樣定理
- Hybrid systems 僅作形式方法接口，不宣稱 AI 主體性已被控制理論解決
- NS × X72 僅作方法論旁證，不構成 Navier–Stokes 對 AI identity 的直接證明
- 本文不把 operational continuity 等同 phenomenal continuity
