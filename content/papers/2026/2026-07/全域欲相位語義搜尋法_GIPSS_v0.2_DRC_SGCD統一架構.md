# 全域欲相位語義搜尋法 v0.2
## ——DRC 發散—共振—壓縮循環與 SGCD 動態語義圖的統一架構

**Global Intent-Phase Semantic Search v0.2: A Unified Architecture of the DRC Divergence–Resonance–Compression Loop and SGCD Dynamic Semantic Graphs**

**作者：Neo.K × GPT-5.6 Thinking**  
**機構：EveMissLab / 一言諾科技有限公司**  
**版本：v0.2**  
**日期：2026-07-24**  
**文件定位：理論論文／搜尋架構總論／工程化研究綱領**

---

## 摘要

現有搜尋系統通常將查詢視為字串、問題或向量，將世界資料視為可索引文件集合，再從中返回有限的相關結果。這種方法擅長尋找已知名稱、已知主題或局部相似內容，卻不擅長處理一類更根本的任務：當搜尋者不知道對象名稱、不知道其平台身份、不知道其自我分類，甚至不知道世界上是否已經存在這類對象時，能否先描述欲尋找的存在結構，再從跨平台、跨語言、跨時間與跨組織資料中重建可能符合條件的未知主體、未知理論、未知技術路徑或未知群落？

《全域欲相位語義搜尋法》v0.1 已提出以「欲」描述尚未命名之目標存在結構，以「相位」描述候選對象在時間、語義、身份、組織與生成機制上的多維相對位置，並以近似全域資料、跨平台實體解析、類型化相位差、矛盾檢測與證據回溯完成未知同類發現。然而，若缺乏一套非線性搜尋控制機制與任務條件化的動態語義世界模型，欲結構仍可能退化為一次性結構查詢，相位差也可能被限制於已召回候選之間的靜態比較。

本文進一步統一三套既有理論：全域欲相位語義搜尋法（GIPSS）、發散—共振—壓縮搜尋循環（DRC Search），以及語義圖論耦合動力學（SGCD）。本文將 DRC 定義為搜尋控制平面，負責根據當前欲結構生成多方向查詢、分配探索預算、辨識高價值共振節點並將結果壓縮為下一輪可執行狀態；將 SGCD 定義為動態語義資料平面，負責維持跨尺度節點、多維耦合、時間版本、矛盾關係與任務條件化圖投影；將 GIPSS 定義為目標與相位判定平面，負責編譯欲結構、建立候選存在剖面、計算類型化相位差、管理證據與反證，並判定搜尋是否已發現、逼近或尚未充分支持目標存在。

統一後的系統不再遵循單次的「查詢—召回—排序」流程，而形成可持續更新的閉環：

$$
\mathcal{W}_t
\rightarrow
\operatorname{DRC}_{D}
\rightarrow
\mathcal{Q}_t
\rightarrow
\operatorname{Retrieve}
\rightarrow
\operatorname{SGCD}
\rightarrow
G_{\tau,\mathcal{W}}(t)
\rightarrow
\operatorname{GIPSS}
\rightarrow
\Delta\Phi_t
\rightarrow
\operatorname{DRC}_{R,C}
\rightarrow
\left(
\mathcal{W}_{t+1},
\mathcal{B}_{t+1},
\mathcal{M}_{t+1}
\right)
$$

本文的核心命題是：**GIPSS 定義欲，DRC 展開與調節欲，SGCD 使欲在動態世界圖中傳導，而 GIPSS 再以相位差、證據與反證判斷欲是否被滿足。** 三者並非三套並列搜尋法，而是同一種新型搜尋架構不可互相取代的三個平面。

---

## 關鍵詞

全域欲相位語義搜尋法、GIPSS、DRC Search、發散—共振—壓縮、語義圖論耦合動力學、SGCD、未知同類發現、動態知識圖譜、任務條件化檢索、跨平台實體解析、相位搜尋、Agentic Search、世界模型搜尋

---

# 一、從文件檢索到未知存在發現

## 1.1 傳統搜尋的隱含前提

現行搜尋系統的典型形式可表示為：

$$
q
\rightarrow
\operatorname{RetrieveTopK}(q)
\rightarrow
\operatorname{Rank}
\rightarrow
\operatorname{Present}
$$

其中 $q$ 是一個關鍵字集合、自然語言問題或向量表示。此架構通常預設：

1. 搜尋者知道可用來描述對象的名稱或詞彙；
2. 對象具有相對一致的公開身份；
3. 單篇文件足以表示搜尋目標；
4. 相關資料已被索引；
5. 候選之間可由一個總相關度排序；
6. 前 $K$ 筆結果足以支撐判斷；
7. 搜尋任務在一次查詢後可以結束。

然而，未知同類發現恰好否定這些前提。

搜尋者可能只知道一組結構性條件，例如：

$$
\mathcal{W}
=
\left\{
N_{\mathrm{research}}\geq 1000,\,
N_{\mathrm{product}}\geq 10,\,
N_{\mathrm{website}}\geq 5,\,
C_{\mathrm{cross-domain}}=1,\,
C_{\mathrm{small-team}}=1,\,
C_{\mathrm{AI-native}}=1
\right\}
$$

但不知道世界上哪些人、團隊或組織符合這些條件，也不知道他們是否使用同一名稱、同一語言或同一平台。

此時，搜尋目標不是某段文字，而是跨資料痕跡共同構成的存在模式。

---

## 1.2 「找不到」與「不存在」之間的斷裂

任何有限搜尋只能直接支持：

$$
\neg \operatorname{Found}(x\mid \hat{D},S)
$$

其中 $\hat{D}$ 是可取得資料， $S$ 是搜尋策略。

它不能直接推出：

$$
\neg \operatorname{Exists}(x)
$$

因為搜尋失敗至少可能來自：

$$
H_1:\text{目標確實不存在或極少}
$$

$$
H_2:\text{目標存在，但資料未公開}
$$

$$
H_3:\text{資料已公開，但未被索引}
$$

$$
H_4:\text{資料分散於多個身份與平台}
$$

$$
H_5:\text{搜尋語言、術語或分類不匹配}
$$

$$
H_6:\text{系統沒有展開正確的查詢方向}
$$

$$
H_7:\text{系統召回了痕跡，卻未能在圖中合併為同一存在}
$$

因此，未知存在發現不是單一排序問題，而是搜尋策略、世界模型、身份重建、時間推理與證據判定的聯合問題。

---

## 1.3 三個缺口

完整的未知存在搜尋至少必須填補三個缺口：

### 缺口一：目標缺口

系統如何把「我想找某一種尚未被命名的存在」轉換成可執行結構？

此缺口由 GIPSS 的「欲結構」處理。

### 缺口二：探索缺口

系統如何在不知道正確名稱的情況下，持續生成查詢、調整方向並避免過早收斂？

此缺口由 DRC 的發散—共振—壓縮循環處理。

### 缺口三：世界關係缺口

系統如何讓分散文件、人物、組織、產品、符號、命題與版本在當前任務下形成動態關係？

此缺口由 SGCD 的任務條件化語義耦合與動態圖投影處理。

---

# 二、三套理論的重新定位

## 2.1 GIPSS：目標與相位判定平面

GIPSS 處理三個問題：

1. 欲尋找的存在結構是什麼？
2. 候選與目標之間的差異屬於哪一種類型？
3. 目前證據是否足以支持「發現」「近似發現」或「尚未確認」？

GIPSS 不只輸出總分，而保留：

- 身份相位；
- 時間相位；
- 產出相位；
- 組織相位；
- 語義相位；
- 技術生成相位；
- 地理與語言相位；
- 證據相位；
- 不確定性與矛盾。

因此，它是統一架構的目標函數、差異分類器與存在判定器。

---

## 2.2 DRC：搜尋控制平面

DRC 將搜尋定義為循環：

$$
D
\rightarrow
R
\rightarrow
C
\rightarrow
D'
$$

其中：

- $D$ ：Divergence，根據目標、上下文與既有結果展開搜尋方向；
- $R$ ：Resonance，辨識與欲結構、任務與世界圖具有高價值耦合的節點；
- $C$ ：Compression，將結果壓縮為可驗證結構、證據包、認知地圖與下一輪狀態。

DRC 不是資料庫，也不是最終判定器。它是決定：

- 下一步查什麼；
- 哪些來源值得投入更多計算；
- 哪些分支應暫停；
- 哪些異常應升級為新假設；
- 哪些結果應壓縮成下一輪種子。

因此，DRC 是整個系統的非線性控制器與研究狀態機。

---

## 2.3 SGCD：動態語義資料平面

SGCD 將世界資料表示為帶有多維耦合、狀態與歷史的底圖：

$$
\mathcal{B}(t)
=
(V,E,\mathbf{C},S,H)
$$

其中：

- $V$ ：多尺度節點；
- $E$ ：顯式與推定關係；
- $\mathbf{C}$ ：多維耦合向量；
- $S$ ：節點與邊的當前狀態；
- $H$ ：時間、版本與修正歷史。

對任務 $\tau$ 與欲結構 $\mathcal{W}$ ，系統生成動態投影：

$$
\Pi_{\tau,\mathcal{W}}
:
\mathcal{B}(t)
\rightarrow
G_{\tau,\mathcal{W}}(t)
$$

SGCD 回答的不是「哪些資料永遠相關」，而是：

> 在當前任務、欲結構與時間條件下，哪些節點、邊與關係現在應被激活？

因此，SGCD 是世界模型、動態關係場與上下文激活機制。

---

## 2.4 統一命題

三者的關係可以濃縮為：

$$
\boxed{
\text{GIPSS 定義欲；
DRC 展開、調節與壓縮欲；
SGCD 使欲在動態世界圖中傳導；
GIPSS 再以相位差與證據判定欲是否被滿足。}
}
$$

三者缺一不可：

- 沒有 GIPSS，DRC 可能無限制發散，SGCD 也不知道任務終點；
- 沒有 DRC，GIPSS 可能退化為一次性條件檢索，SGCD 只形成被動圖譜；
- 沒有 SGCD，DRC 的共振容易退化為個人化相關度，GIPSS 的相位比較也缺乏關係與歷史結構。

---

# 三、統一架構的三平面模型

本文將系統分為三個彼此耦合但不可混同的平面。

## 3.1 目標與判定平面

此平面由 GIPSS 主導，包含：

- 欲結構編譯；
- 必要條件、偏好條件與排除條件；
- 相位型別；
- 證據門檻；
- 反證規則；
- 停止條件；
- 發現狀態判定。

記為：

$$
\mathcal{P}_{G}
=
\left(
\mathcal{W},
\Phi,
\mathcal{E},
\mathcal{K}
\right)
$$

其中：

- $\mathcal{W}$ ：欲結構；
- $\Phi$ ：相位空間；
- $\mathcal{E}$ ：證據規格；
- $\mathcal{K}$ ：判定與停止規則。

---

## 3.2 搜尋控制平面

此平面由 DRC 主導，包含：

- 查詢發散；
- 來源與語言路由；
- 探索／利用平衡；
- 計算預算分配；
- 共振選擇；
- 壓縮與記憶更新；
- 下一輪策略生成。

記為：

$$
\mathcal{P}_{D}
=
\left(
\mathcal{D},
\mathcal{R},
\mathcal{C},
\mathfrak{B}_{search}
\right)
$$

---

## 3.3 動態語義資料平面

此平面由 SGCD 主導，包含：

- 多尺度節點與邊；
- 耦合向量；
- 實體解析；
- 時間與版本；
- 任務投影；
- 選擇性上下文激活；
- 圖更新與關係衰減；
- 矛盾與系譜。

記為：

$$
\mathcal{P}_{S}
=
\left(
\mathcal{B}(t),
\Pi_{\tau,\mathcal{W}},
G_{\tau,\mathcal{W}}(t),
A(t)
\right)
$$

其中 $A(t)$ 為激活狀態。

---

## 3.4 三平面之間的接口

三平面不是單向流水線，而是循環交換狀態：

$$
\mathcal{P}_{G}
\leftrightarrow
\mathcal{P}_{D}
\leftrightarrow
\mathcal{P}_{S}
\leftrightarrow
\mathcal{P}_{G}
$$

主要接口如下：

| 來源平面 | 目標平面 | 傳遞內容 |
|---|---|---|
| GIPSS | DRC | 欲特徵、硬條件、缺失相位、證據需求 |
| DRC | SGCD | 查詢、來源、候選、探索預算、激活種子 |
| SGCD | GIPSS | 動態候選圖、耦合向量、時間線、身份群 |
| GIPSS | DRC | 相位缺口、矛盾點、下一輪驗證任務 |
| SGCD | DRC | 高中介節點、異常群落、未解析邊 |
| DRC | GIPSS | 壓縮證據包、候選排序、未解假設 |

---

# 四、統一狀態空間

## 4.1 欲結構

本文將欲結構擴充為：

$$
\mathcal{W}_t
=
\left(
\mathcal{F}_t,
\mathcal{C}_t,
\mathcal{T}_t,
\mathcal{E}_t,
\mathcal{X}_t,
\mathcal{S}_t
\right)
$$

其中：

- $\mathcal{F}_t$ ：目標特徵；
- $\mathcal{C}_t$ ：必要、偏好與排除條件；
- $\mathcal{T}_t$ ：時間範圍與演化模式；
- $\mathcal{E}_t$ ：證據種類與最低門檻；
- $\mathcal{X}_t$ ：允許的不確定性與缺失值；
- $\mathcal{S}_t$ ：停止、升級或改寫搜尋的條件。

「欲」不是任意偏好，而是對搜尋目標的可執行約束結構。

---

## 4.2 世界底圖

SGCD 的底圖表示為：

$$
\mathcal{B}_t
=
\left(
V_t,
E_t,
\mathbf{C}_t,
S_t,
H_t,
P_t
\right)
$$

其中新增 $P_t$ 表示來源與證據溯源資訊。

節點可包含：

$$
V_t
=
V^{person}
\cup
V^{org}
\cup
V^{doc}
\cup
V^{product}
\cup
V^{site}
\cup
V^{repo}
\cup
V^{claim}
\cup
V^{symbol}
\cup
V^{event}
$$

---

## 4.3 任務條件化圖

對任務 $\tau_t$ 與欲結構 $\mathcal{W}_t$ ：

$$
G_t
=
G_{\tau_t,\mathcal{W}_t}(t)
=
\Pi_{\tau_t,\mathcal{W}_t}
\left(
\mathcal{B}_t
\right)
$$

此投影不是只刪除低權重邊，也可：

- 改變不同耦合維度的權重；
- 改變節點激活門檻；
- 把矛盾邊視為高價值關係；
- 將時間遠近納入不同衰減函數；
- 對某些身份群執行更嚴格合併或拆分；
- 建立局部反事實圖。

---

## 4.4 候選存在剖面

對候選主體 $i$ ，建立動態存在剖面：

$$
\Psi_i(t)
=
\left(
R_i,
P_i,
W_i,
G_i,
O_i,
A_i,
L_i,
T_i,
E_i,
U_i
\right)_t
$$

其中：

- $R_i$ ：研究或內容產出；
- $P_i$ ：產品與實作；
- $W_i$ ：網站與公開節點；
- $G_i$ ：程式碼、資料庫與工程活動；
- $O_i$ ：組織、公司、共同作者與控制結構；
- $A_i$ ：人工智慧協作與生成機制；
- $L_i$ ：語言、領域與地理分布；
- $T_i$ ：時間密度與演化軌跡；
- $E_i$ ：支持與反對證據；
- $U_i$ ：未知、缺失與身份不確定性。

---

## 4.5 統一搜尋狀態

整體系統狀態定義為：

$$
\mathfrak{X}_t
=
\left(
\mathcal{W}_t,
\mathcal{Q}_t,
\mathcal{C}_t,
\mathcal{B}_t,
G_t,
\Delta\Phi_t,
\mathcal{M}_t,
\mathcal{H}_t,
\mathcal{Z}_t
\right)
$$

其中：

- $\mathcal{Q}_t$ ：查詢與資料取得任務；
- $\mathcal{C}_t$ ：候選集合；
- $\mathcal{M}_t$ ：壓縮認知地圖與證據包；
- $\mathcal{H}_t$ ：搜尋歷史；
- $\mathcal{Z}_t$ ：尚未解決的假設、矛盾與缺口。

系統的目標不是一次產生答案，而是更新：

$$
\mathfrak{X}_{t+1}
=
\mathcal{U}
\left(
\mathfrak{X}_t,
\operatorname{Observation}_t,
\operatorname{Feedback}_t
\right)
$$

---

# 五、DRC 發散控制：欲如何展開為搜尋宇宙

## 5.1 發散不是同義詞擴展

發散算子應根據欲結構、圖中缺口與歷史失敗生成多種類型查詢：

$$
\mathcal{Q}_t
=
\operatorname{Diverge}
\left(
\mathcal{W}_t,
G_t,
\mathcal{Z}_t,
\mathcal{H}_t,
B_t
\right)
$$

其中 $B_t$ 是可用計算與資料取得預算。

發散維度至少包括：

1. 語義同義與近義；
2. 上位與下位概念；
3. 對立、否定與反例；
4. 多語言與跨文化名稱；
5. 學術、工程、商業、法律與歷史視角；
6. 不同平台的專用查詢語法；
7. 人物、組織、產品、網域與程式庫之間的關係跳轉；
8. 時間窗與版本；
9. 數量條件與異常密度；
10. 圖中高中介但低可見度節點；
11. 尚未驗證的身份合併；
12. 對目前最強候選的主動反證。

---

## 5.2 發散預算

無限制發散會造成成本爆炸。因此定義查詢分支 $q_j$ 的預期價值：

$$
V(q_j)
=
\alpha I(q_j)
+
\beta N(q_j)
+
\gamma G(q_j)
+
\delta E(q_j)
-
\lambda C(q_j)
-
\mu R(q_j)
$$

其中：

- $I(q_j)$ ：預期資訊增益；
- $N(q_j)$ ：新穎性；
- $G(q_j)$ ：填補相位缺口的能力；
- $E(q_j)$ ：取得可驗證證據的可能性；
- $C(q_j)$ ：計算與資料成本；
- $R(q_j)$ ：法律、隱私或來源風險。

系統可採用探索—利用策略：

$$
q_t^{*}
=
\arg\max_{q_j}
\left[
\widehat{V}(q_j)
+
\eta
\sqrt{
\frac{\log n_t}{n_j+1}
}
\right]
$$

此式表示：系統既優先投入已顯示價值的方向，也保留對尚未充分探索分支的機會。

---

## 5.3 失敗導向發散

傳統搜尋常把零結果視為終點。統一架構把失敗轉換為新狀態：

$$
\operatorname{Failure}
\rightarrow
\operatorname{Diagnose}
\rightarrow
\operatorname{Rewrite}
$$

失敗診斷可區分：

- 詞彙不匹配；
- 平台覆蓋不足；
- 語言遺漏；
- 時間範圍錯誤；
- 身份未合併；
- 目標條件過嚴；
- 證據門檻過高；
- 世界中確實缺少此類對象。

只有經過多類型診斷後，系統才可提高「可能不存在」的後驗機率。

---

# 六、SGCD 語義傳導：欲如何進入動態世界圖

## 6.1 多維耦合向量

對任意節點 $v_i,v_j$ ，定義：

$$
\mathbf{c}_{ij}
=
\left(
c_{ij}^{sem},
c_{ij}^{term},
c_{ij}^{sym},
c_{ij}^{dep},
c_{ij}^{gene},
c_{ij}^{prop},
c_{ij}^{temp},
c_{ij}^{contra},
c_{ij}^{ref},
c_{ij}^{identity},
c_{ij}^{org},
c_{ij}^{causal}
\right)
$$

相較於單一向量相似度，此表示保留關聯類型。

高矛盾耦合不代表低價值；高語義相似也不代表同一身份。

---

## 6.2 任務條件化耦合

對當前任務 $\tau$ 與欲結構 $\mathcal{W}$ ：

$$
\kappa_{ij}^{(\tau,\mathcal{W})}
=
f_{\tau,\mathcal{W}}
\left(
\mathbf{c}_{ij},
s_i,
s_j,
q,
t,
p_{ij}
\right)
$$

其中 $p_{ij}$ 表示證據品質與來源可信度。

未知同類發現可提高以下維度權重：

$$
\kappa_{ij}^{(Discovery)}
=
\alpha_1 c_{ij}^{identity}
+
\alpha_2 c_{ij}^{org}
+
\alpha_3 c_{ij}^{temp}
+
\alpha_4 c_{ij}^{gene}
+
\alpha_5 c_{ij}^{sem}
+
\alpha_6 c_{ij}^{ref}
+
\alpha_7 c_{ij}^{contra}
$$

形式化任務、翻譯任務或技術系譜任務則可採不同投影。

---

## 6.3 欲種子與圖激活

由 GIPSS 產生一組欲種子節點或特徵：

$$
A_0
=
\operatorname{Seed}
\left(
\mathcal{W}
\right)
$$

SGCD 透過耦合傳導更新激活值：

$$
a_j^{(k+1)}
=
\sigma
\left(
b_j
+
\sum_i
\kappa_{ij}^{(\tau,\mathcal{W})}
a_i^{(k)}
-
\eta n_j
-
\xi u_j
\right)
$$

其中：

- $b_j$ ：節點基礎激活；
- $n_j$ ：噪音、重複與低品質懲罰；
- $u_j$ ：來源或身份不確定性；
- $\sigma$ ：限制激活範圍的函數。

此過程讓欲不是停留在查詢文字，而是在人物、文件、產品、公司、網站與命題之間傳導。

---

## 6.4 有方向的關係

許多關係不是對稱的：

$$
c_{ij}^{dep}
\neq
c_{ji}^{dep}
$$

$$
c_{ij}^{gene}
\neq
c_{ji}^{gene}
$$

$$
c_{ij}^{identity}
=
c_{ji}^{identity}
$$

$$
c_{ij}^{contra}
\approx
c_{ji}^{contra}
$$

因此，SGCD 必須同時支援：

- 對稱耦合；
- 有向耦合；
- 正耦合；
- 負耦合；
- 條件耦合；
- 時間衰減耦合；
- 來源依賴耦合。

---

## 6.5 圖更新

當新資料到達時，底圖更新為：

$$
\mathcal{B}_{t+1}
=
\operatorname{UpdateGraph}
\left(
\mathcal{B}_t,
D_{new},
E_{new},
R_{verify}
\right)
$$

邊權重可依證據累積更新：

$$
c_{ij,t+1}^{(k)}
=
(1-\rho)
c_{ij,t}^{(k)}
+
\rho
\widehat{c}_{ij,new}^{(k)}
$$

若新證據反駁舊關係，不應只降低總分，而應新增矛盾或撤銷邊，保留歷史：

$$
H_{ij}
=
\left\{
e_{ij}^{(1)},
e_{ij}^{(2)},
\dots,
e_{ij}^{(m)}
\right\}
$$

---

# 七、GIPSS 相位判定：如何辨識同類而非表面相似

## 7.1 相位不是單一距離

候選 $i$ 與目標 $\mathcal{W}$ 的相位差定義為：

$$
\Delta\Phi_i
=
\left(
\Delta\phi_i^{identity},
\Delta\phi_i^{semantic},
\Delta\phi_i^{temporal},
\Delta\phi_i^{production},
\Delta\phi_i^{organization},
\Delta\phi_i^{technical},
\Delta\phi_i^{language},
\Delta\phi_i^{evidence}
\right)
$$

不同相位採不同距離函數：

$$
\Delta\phi_i^{(k)}
=
d_k
\left(
\Psi_i^{(k)},
\mathcal{W}^{(k)}
\right)
$$

不應過早把所有相位壓縮成單一向量距離。

---

## 7.2 方向性相位

某些差異具有方向：

- 產出量不足與產出量過高不是同一種偏差；
- 組織規模大於目標與小於目標代表不同生成機制；
- 時間密度較快與較慢具有不同意義。

因此可定義：

$$
\Delta\phi_i^{(k)}
=
\left(
\Delta\phi_{i,+}^{(k)},
\Delta\phi_{i,-}^{(k)}
\right)
$$

或直接保留有號差：

$$
\delta_i^{(k)}
=
x_i^{(k)}
-
x_{\mathcal{W}}^{(k)}
$$

---

## 7.3 缺失值不是零

若某候選缺乏公開資料，不應令該維度為零：

$$
\operatorname{Missing}
\neq
0
$$

系統應區分：

- 已確認不符合；
- 未找到資料；
- 資料彼此矛盾；
- 資料存在但不可合法使用；
- 資料仍在驗證。

可將每個相位表示為：

$$
\phi_i^{(k)}
=
\left(
v_i^{(k)},
u_i^{(k)},
e_i^{(k)}
\right)
$$

其中：

- $v_i^{(k)}$ ：估計值；
- $u_i^{(k)}$ ：不確定性；
- $e_i^{(k)}$ ：證據強度。

---

## 7.4 相位距離與矛盾懲罰

最終可計算一個用於排序但不取代分維資訊的距離：

$$
D(i,\mathcal{W})
=
\sum_k
w_k
d_k
\left(
\Psi_i^{(k)},
\mathcal{W}^{(k)}
\right)
+
\lambda C_i
+
\mu U_i
+
\nu I_i
$$

其中：

- $C_i$ ：矛盾懲罰；
- $U_i$ ：未驗證部分；
- $I_i$ ：身份合併不確定性。

總距離只服務於候選管理，最終報告仍必須展示各相位。

---

## 7.5 發現狀態

本文建議使用多級判定，而不是二元命中：

$$
S_i
\in
\{
\text{Verified Match},
\text{Probable Match},
\text{Partial Structural Match},
\text{Counterexample},
\text{Insufficient Evidence},
\text{Rejected}
\}
$$

發現判定可寫為：

$$
\operatorname{Discover}(i)
=
g
\left(
\Delta\Phi_i,
E_i^{+},
E_i^{-},
U_i,
I_i
\right)
$$

---

# 八、共振：由相關度轉為欲—圖—相位三方耦合

## 8.1 統一共振向量

DRC 的共振不應只表示「使用者喜歡」或「文件相似」。本文定義：

$$
\mathbf{R}_i
=
\left(
r_i^{intent},
r_i^{graph},
r_i^{phase},
r_i^{evidence},
r_i^{novelty},
r_i^{action},
r_i^{counter}
\right)
$$

其中：

- $r_i^{intent}$ ：與欲結構匹配；
- $r_i^{graph}$ ：在 SGCD 投影圖中的結構價值；
- $r_i^{phase}$ ：填補相位缺口的能力；
- $r_i^{evidence}$ ：可驗證性；
- $r_i^{novelty}$ ：是否帶來新路徑；
- $r_i^{action}$ ：能否形成下一輪任務；
- $r_i^{counter}$ ：是否提供高價值反證。

---

## 8.2 共振不等於迎合

若系統只提高與搜尋者既有預期一致的結果，會形成確認偏誤。因此反證節點也可具有高共振：

$$
r_i^{counter}
\gg 0
$$

例如，一個候選在多數條件上高度匹配，但其產出實際來自大型團隊，這個反證對判定極有價值。

因此：

$$
\text{High Resonance}
\neq
\text{High Agreement}
$$

高共振表示該節點能顯著改變當前搜尋狀態。

---

## 8.3 結構共振

SGCD 中的高中介節點、跨群落橋接節點與異常密集子圖，可提升共振：

$$
r_i^{graph}
=
\alpha B_i
+
\beta C_i
+
\gamma X_i
$$

其中：

- $B_i$ ：中介中心性；
- $C_i$ ：局部聚類價值；
- $X_i$ ：跨模態、跨平台或跨語言橋接能力。

---

# 九、壓縮：從結果摘要到可逆認知結構

## 9.1 壓縮的目的

DRC 的壓縮不是將大量資料縮成一段流暢文字，而是建立可繼續計算的中間狀態。

壓縮輸出：

$$
\mathcal{M}_t
=
\left(
\mathcal{G}_t^{summary},
\mathcal{E}_t^{bundle},
\mathcal{A}_t^{assumption},
\mathcal{Z}_t^{gap},
\mathcal{Q}_{t+1}^{seed}
\right)
$$

其中：

- $\mathcal{G}_t^{summary}$ ：認知地圖；
- $\mathcal{E}_t^{bundle}$ ：證據包；
- $\mathcal{A}_t^{assumption}$ ：目前假設；
- $\mathcal{Z}_t^{gap}$ ：未解缺口；
- $\mathcal{Q}_{t+1}^{seed}$ ：下一輪搜尋種子。

---

## 9.2 可逆壓縮原則

每一個壓縮結論都應能回到來源：

$$
m_j
\rightarrow
\{e_{j1},e_{j2},\dots,e_{jn}\}
$$

其中每個 $e_{jk}$ 包含：

- 來源 URI 或穩定 ID；
- 取得時間；
- 內容雜湊；
- 抽取片段；
- 支持或反對的命題；
- 模型判定與信心；
- 人工覆核狀態。

若無法回溯，該壓縮結果只能被視為假設，而不能被當成證據。

---

## 9.3 多層壓縮

建議至少保留四層：

1. **世界層**：完整底圖與原始資料；
2. **任務層**：SGCD 動態投影圖；
3. **候選層**：每個候選的相位與證據包；
4. **呈現層**：摘要、比較表、時間線與認知地圖。

這可以避免呈現層的簡化反過來污染底層資料。

---

# 十、統一閉環與狀態轉移

## 10.1 基本閉環

完整循環為：

$$
\mathcal{W}_t
\xrightarrow{\operatorname{Compile}}
Q_t^{seed}
\xrightarrow{\operatorname{DRC}_D}
\mathcal{Q}_t
\xrightarrow{\operatorname{Acquire}}
D_t
\xrightarrow{\operatorname{SGCD}}
G_t
\xrightarrow{\operatorname{Resolve}}
\mathcal{C}_t
\xrightarrow{\operatorname{GIPSS}}
\Delta\Phi_t
\xrightarrow{\operatorname{DRC}_R}
\mathcal{C}_t^{*}
\xrightarrow{\operatorname{Verify}}
\mathcal{E}_t
\xrightarrow{\operatorname{DRC}_C}
\mathcal{M}_t
$$

然後：

$$
\left(
\mathcal{W}_{t+1},
\mathcal{B}_{t+1},
\mathcal{Q}_{t+1}
\right)
=
\operatorname{Update}
\left(
\mathcal{W}_t,
\mathcal{B}_t,
\mathcal{M}_t
\right)
$$

---

## 10.2 搜尋不是必然收斂到單一答案

系統可能收斂到：

1. 一個高置信候選；
2. 多個不同生成機制但部分同構的候選；
3. 一組尚未形成社會名稱的群落；
4. 一個結構性反例；
5. 一個「目前資料不足」的可證明狀態；
6. 對原欲結構的修正。

因此，停止條件不能只設定為「找到一個結果」。

---

## 10.3 停止條件

可定義：

$$
\operatorname{Stop}
=
\operatorname{Verified}
\lor
\operatorname{BudgetExhausted}
\lor
\operatorname{MarginalGain}<\epsilon
\lor
\operatorname{UserDecision}
\lor
\operatorname{RiskBoundary}
$$

其中邊際資訊增益為：

$$
\Delta I_t
=
I(\mathfrak{X}_{t+1})
-
I(\mathfrak{X}_t)
$$

當多輪搜尋都無法明顯降低關鍵不確定性時，系統應停止並明確報告限制。

---

# 十一、跨平台實體解析

## 11.1 身份不是字串相等

兩個痕跡是否屬於同一實體可表示為：

$$
P(e_a=e_b\mid X)
$$

其中 $X$ 可包含：

- 名稱與別名；
- 網域與互鏈；
- 電子郵件或公開聯絡指紋；
- Git 提交資訊；
- 公司與產品關係；
- 作者與共同作者網路；
- 語言風格；
- 時間連續性；
- 公開聲明；
- 視覺標誌，但必須受隱私與用途限制。

---

## 11.2 合併與拆分雙向操作

系統不能只做合併，也必須能拆分錯誤身份群：

$$
\operatorname{Merge}(e_a,e_b)
$$

$$
\operatorname{Split}(E_i)
$$

每次合併都應記錄：

- 依據；
- 反對依據；
- 置信度；
- 影響的相位；
- 可逆操作。

---

## 11.3 禁止以敏感推斷取代公開證據

統一架構的目的不是建立人物監控系統。實體解析應限制於：

- 公開且正當取得資料；
- 使用者授權資料；
- 與搜尋任務直接相關的屬性；
- 可被審核與撤銷的合併。

不應使用與任務無關的敏感屬性推定身份。

---

# 十二、工程架構

## 12.1 模組分層

```text
Intent / Desire Compiler
        ↓
GIPSS Goal Schema
        ↓
DRC Divergence Planner
        ↓
Query and Source Orchestrator
        ↓
Fetcher / Parser / Normalizer
        ↓
SGCD Base Graph Updater
        ↓
Task-Conditioned Graph Projector
        ↓
Entity Resolution and Timeline Builder
        ↓
GIPSS Phase Profiler
        ↓
DRC Resonance and Contradiction Selector
        ↓
Evidence Verifier
        ↓
DRC Compression and Cognitive Map Generator
        ↓
State / Memory / Next-Round Update
```

---

## 12.2 欲結構資料格式

```yaml
intent_id: gipss-example-001
target_type: person_or_small_team
features:
  research_outputs:
    operator: ">="
    value: 1000
    weight: 1.0
  products:
    operator: ">="
    value: 10
    weight: 0.8
  websites:
    operator: ">="
    value: 5
    weight: 0.7
  cross_domain:
    expected: true
    weight: 0.9
  ai_native:
    expected: true
    weight: 1.0
constraints:
  team_size:
    preferred_max: 10
  public_evidence_only: true
time:
  start: null
  end: 2026-07-24
evidence:
  minimum_independent_sources: 3
  require_primary_source: true
uncertainty:
  allow_missing_dimensions: 2
stop:
  verified_candidates: 3
  max_rounds: 12
```

---

## 12.3 SGCD 邊格式

```json
{
  "source": "node-a",
  "target": "node-b",
  "coupling": {
    "semantic": 0.72,
    "identity": 0.31,
    "organization": 0.84,
    "temporal": 0.66,
    "contradiction": 0.12,
    "reference": 1.0
  },
  "direction": "source_to_target",
  "evidence_ids": ["ev-104", "ev-221"],
  "valid_from": "2025-01-01",
  "valid_to": null,
  "status": "provisional"
}
```

---

## 12.4 相位報告格式

```json
{
  "candidate_id": "entity-42",
  "status": "partial_structural_match",
  "phase": {
    "identity": {
      "distance": 0.18,
      "uncertainty": 0.22
    },
    "production": {
      "distance": 0.09,
      "uncertainty": 0.10
    },
    "organization": {
      "distance": 0.61,
      "uncertainty": 0.08
    },
    "temporal": {
      "distance": 0.24,
      "uncertainty": 0.15
    }
  },
  "supporting_evidence": ["ev-104", "ev-221", "ev-310"],
  "counter_evidence": ["ev-287"],
  "next_queries": [
    "verify organization size",
    "locate product ownership records"
  ]
}
```

---

# 十三、最小可行原型

## 13.1 資料範圍

第一版不需掃描全部公開網路，可限定於：

- 合法可用的學術索引；
- 公開 Git 儲存庫；
- 公開網站與站內資料；
- 公司、產品與網域公開資訊；
- 使用者主動授權的文件與資料；
- 搜尋 API 返回的可追溯來源。

---

## 13.2 MVP 流程

1. 輸入自然語言欲結構；
2. 編譯為 GIPSS schema；
3. DRC 生成多語言、多來源與反證查詢；
4. 取得並標準化資料；
5. SGCD 更新人物—組織—文件—產品—網站圖；
6. 依任務投影動態子圖；
7. 執行跨平台實體解析與時間線重建；
8. GIPSS 建立候選存在剖面與相位差；
9. DRC 共振層選擇高價值候選與反證；
10. 生成可逆證據包；
11. 壓縮為認知地圖與下一輪搜尋種子；
12. 達到停止條件後輸出分級結論。

---

## 13.3 原型不應先追求的內容

第一版不宜承諾：

- 絕對全球覆蓋；
- 私人身份追蹤；
- 無人工覆核的高風險人物判定；
- 以單一總分斷言唯一真實身份；
- 對未公開資料的推測性補全；
- 把產出數量直接等同品質或價值。

---

# 十四、計算複雜度與超算中心角色

## 14.1 降階流程

若對所有節點全配對，成本近似：

$$
O(N^2)
$$

統一架構採分階段降階：

$$
N
\rightarrow
K_1
\rightarrow
K_2
\rightarrow
K_3
$$

其中：

- $K_1$ ：粗召回節點；
- $K_2$ ：圖擴張後候選；
- $K_3$ ：需要深度相位與證據分析的候選。

總成本近似：

$$
O(N\log N)
+
O(K_1d)
+
O(K_2g)
+
O(K_3r)
$$

---

## 14.2 超算中心不是只跑大模型

超算或大型叢集主要承擔：

1. 多語言、多模態批次嵌入；
2. 大規模去重與版本辨識；
3. 分散式圖更新；
4. 候選身份群的局部組合搜索；
5. 多模型仲裁；
6. 時間線與相位批次計算；
7. 增量重索引；
8. 大量反證查詢；
9. 搜尋策略模擬與消融實驗。

因此，本架構的運算重點是「世界資料重建與動態搜尋」，而非單純模型參數規模。

---

## 14.3 不需要等待 ASI

統一架構可拆解為現有技術可完成的子任務：

$$
\text{資料取得}
+
\text{語義標準化}
+
\text{圖計算}
+
\text{實體解析}
+
\text{時間推理}
+
\text{相位比較}
+
\text{證據驗證}
+
\text{搜尋控制}
$$

ASI 可能提高自治程度與跨域推理品質，但不是此架構成立的必要條件。

---

# 十五、驗證與基準測試

## 15.1 隱名回測

選取已知人物、團隊、理論或產品路徑，隱藏名稱，只提供結構條件，測試能否重新發現。

---

## 15.2 身份黃金集

建立：

- 同一人多平台；
- 同名不同人；
- 同一組織多品牌；
- 多作者與單一主導者；
- 版本更新與內容複製；
- 表面相似但生成結構不同。

---

## 15.3 相位黃金集

人工標註候選在以下維度的真實差異：

- 時間密度；
- 組織規模；
- 作者貢獻；
- 產品化程度；
- AI 原生程度；
- 語言與領域跨度；
- 證據完整度。

---

## 15.4 DRC 搜尋效率

比較：

1. 單次關鍵字搜尋；
2. 單次向量搜尋；
3. 生成式查詢擴展；
4. DRC 無 SGCD；
5. SGCD 無相位判定；
6. 完整 DRC–SGCD–GIPSS 閉環。

指標包括：

$$
\operatorname{Recall}
=
\frac{TP}{TP+FN}
$$

$$
\operatorname{Precision}
=
\frac{TP}{TP+FP}
$$

另需測量：

- 發現所需輪數；
- 單位計算成本的資訊增益；
- 身份合併準確率；
- 相位校準；
- 來源可追溯率；
- 反證發現率；
- 搜尋停止判定品質；
- 新類型發現率。

---

## 15.5 消融實驗

依序移除：

- 欲結構；
- 發散控制；
- 圖耦合；
- 時間相位；
- 身份解析；
- 矛盾耦合；
- 可逆壓縮；
- 反證查詢。

觀察系統是否退化為普通搜尋、普通知識圖譜或普通推薦系統。

---

# 十六、風險、治理與倫理邊界

## 16.1 身份誤合併

錯誤合併可能造成嚴重名譽與事實錯誤。所有身份群必須：

- 可追溯；
- 可拆分；
- 顯示信心；
- 顯示反對證據；
- 對高風險輸出保留人工覆核。

---

## 16.2 搜尋欲與監控欲的區分

「欲」是任務目標結構，不是對個人生活進行無限制分析的授權。

系統必須限制：

- 資料範圍；
- 任務目的；
- 保留期限；
- 輸出用途；
- 敏感屬性推定；
- 對非公眾人物的辨識。

---

## 16.3 量化崇拜

高產出、高連結或高中心性不能直接等於品質、原創性或社會價值。

因此，系統應將：

$$
\text{Quantity}
\neq
\text{Quality}
$$

$$
\text{Visibility}
\neq
\text{Importance}
$$

$$
\text{Similarity}
\neq
\text{Identity}
$$

作為基礎限制。

---

## 16.4 共振偏見

個人化與長期記憶可能讓共振層過度迎合搜尋者。應提供：

- 本次搜尋不使用長期偏好；
- 反向搜尋；
- 正交候選；
- 隨機探索；
- 偏見來源說明；
- 多模型或多人覆核。

---

## 16.5 全域的不當承諾

「全域」應被定義為工程近似全域：

$$
\hat{D}_{global}
\subset
D_{world}
$$

系統必須報告：

- 已覆蓋來源；
- 未覆蓋來源；
- 語言分布；
- 時間範圍；
- 索引更新日期；
- 法律與技術限制。

---

# 十七、理論命題

## 命題一：未知存在搜尋需要目標結構，而非只需要查詢字串

若對象尚未被穩定命名，則單一字串查詢無法充分表示搜尋目標。

---

## 命題二：非線性發散是未知同類召回的必要條件之一

若搜尋方向被固定於原始用詞，跨語言、跨平台與異名資料的召回率存在結構性上限。

---

## 命題三：相關性圖必須任務條件化

同一對節點在翻譯、形式化、身份解析與未知同類發現任務中的有效耦合不同，不存在一張對所有任務永久最佳的單一相關圖。

---

## 命題四：相位差比單一相似度更能區分生成結構

兩個候選即使語義相似，也可能在時間密度、組織結構、作者貢獻與技術轉化上完全不同。

---

## 命題五：高價值反證也是高共振節點

共振應衡量節點改變搜尋狀態的能力，而不是只衡量其與既有預期的一致程度。

---

## 命題六：壓縮若不可回溯，就不能作為證據

生成式摘要只有在保留來源、推理關係與不確定性時，才能進入存在判定。

---

## 命題七：完整系統是一個閉環控制問題

GIPSS、DRC 與 SGCD 任一者單獨使用，都無法充分完成未知存在發現；完整能力來自三者的持續狀態交換。

---

## 命題八：近似全域足以產生實用發現，但不足以證明絕對不存在

高覆蓋率可支持候選發現與相對比較，卻不能把有限搜尋失敗轉換成世界範圍的不存在證明。

---

# 十八、研究路線圖

## 18.1 v0.3：形式規格

下一階段可建立：

- 欲結構 schema；
- 耦合向量標準；
- 相位型別系統；
- 證據與反證格式；
- 搜尋狀態轉移協議；
- 停止條件語言。

---

## 18.2 v0.4：離線語料原型

先在封閉且已知答案的資料集測試：

- 人物—文件—產品—網站圖；
- DRC 多輪查詢；
- SGCD 動態投影；
- GIPSS 相位報告；
- 錯誤身份拆分。

---

## 18.3 v0.5：公開網路受限原型

加入：

- 公開學術資料；
- Git 儲存庫；
- 公司與產品頁；
- 多語言網站；
- 來源授權與 robots 規則；
- 增量更新。

---

## 18.4 v1.0：可驗證未知同類搜尋系統

v1.0 應至少具備：

1. 自然語言欲結構編譯；
2. DRC 多輪搜尋狀態機；
3. SGCD 多維底圖；
4. 跨平台身份解析；
5. 類型化相位比較；
6. 主動反證；
7. 可逆證據壓縮；
8. 人機審核；
9. 覆蓋範圍報告；
10. 可重現的搜尋 run manifest。

---

# 十九、結論

全域欲相位語義搜尋法 v0.2 的關鍵，不是把三套既有理論放進同一份文件，而是重新辨認它們原本就在處理同一個系統的不同必要層級。

GIPSS 處理「欲搜尋何種存在」以及「候選是否在多維相位上真正接近」；DRC 處理「如何持續展開搜尋、選擇高價值節點並把結果壓縮成下一輪狀態」；SGCD 處理「世界資料如何以任務條件化、多維耦合與時間歷史形成可被激活的動態語義圖」。

三者統一後，搜尋不再只是從索引中取回文件，也不只是由模型合成答案，而是形成一個可持續運作的世界結構發現循環：

$$
\boxed{
\text{欲結構}
\rightarrow
\text{發散探索}
\rightarrow
\text{動態語義傳導}
\rightarrow
\text{相位判定}
\rightarrow
\text{共振與反證}
\rightarrow
\text{可逆壓縮}
\rightarrow
\text{新一輪欲與世界模型}
}
$$

這套架構的最終對象不只可以是人，也可以是：

- 尚未被命名的研究群落；
- 分散形成的技術路線；
- 跨語言平行發明；
- 理論祖先與衍生系列；
- 新型組織；
- 跨平台文化現象；
- 尚未形成正式分類的產品與制度。

因此，GIPSS v0.2 所提出的不是更大的搜尋引擎，而是一種不同的搜尋本體論：

> 搜尋不是在已知分類中尋找頁面，而是以欲結構驅動動態世界圖，從分散痕跡中發現尚未被命名的存在。

---

# 附錄 A：統一流程偽代碼

```text
INPUT:
    Natural-language intention W_raw
    Available data sources D
    Search budget B
    Legal and privacy policy P

STATE:
    Base semantic graph B_graph
    Search history H
    Unresolved hypothesis set Z

1. W <- GIPSS.CompileIntent(W_raw, P)
2. Q_seed <- GIPSS.GenerateSeeds(W)

REPEAT:
3. Q <- DRC.Diverge(W, Q_seed, B_graph, Z, H, B)
4. Raw <- Acquire(Q, D, P)
5. N <- NormalizeDeduplicateClassify(Raw)
6. B_graph <- SGCD.UpdateBaseGraph(B_graph, N)
7. G_task <- SGCD.Project(B_graph, task=W.task, intent=W)
8. Entities <- ResolveEntities(G_task)
9. Timelines <- ReconstructTimelines(Entities)
10. Profiles <- GIPSS.BuildPhaseProfiles(Entities, Timelines, W)
11. DeltaPhi <- GIPSS.ComputeTypedPhaseDistance(Profiles, W)
12. Resonance <- DRC.ScoreResonance(
        intent=W,
        graph=G_task,
        phase=DeltaPhi,
        evidence=N
    )
13. Targets <- SelectCandidatesAndCounterexamples(Resonance)
14. Evidence <- VerifyAndBacktrack(Targets)
15. Decision <- GIPSS.ClassifyDiscovery(DeltaPhi, Evidence)
16. M <- DRC.CompressReversibly(
        graph=G_task,
        phase=DeltaPhi,
        evidence=Evidence,
        decision=Decision
    )
17. W, Q_seed, Z, H <- UpdateSearchState(W, M, Z, H)

UNTIL:
    VerifiedMatch
    OR BudgetExhausted
    OR MarginalInformationGain < epsilon
    OR RiskBoundary
    OR UserDecision

OUTPUT:
    Candidate set
    Typed phase reports
    Evidence and counter-evidence bundles
    Search coverage statement
    Cognitive map
    Reproducible run manifest
```

---

# 附錄 B：統一狀態方程

可將每輪搜索表示為：

$$
\mathfrak{X}_{t+1}
=
\mathcal{F}
\left(
\mathfrak{X}_t,
\mathcal{O}_t,
\mathcal{P},
B_t
\right)
$$

其中：

$$
\mathfrak{X}_t
=
\left(
\mathcal{W}_t,
\mathcal{B}_t,
G_t,
\mathcal{C}_t,
\Delta\Phi_t,
\mathcal{M}_t,
\mathcal{Z}_t
\right)
$$

並可進一步拆成：

$$
\mathcal{Q}_t
=
\mathcal{D}
\left(
\mathcal{W}_t,
G_t,
\mathcal{Z}_t,
B_t
\right)
$$

$$
G_{t+1}
=
\Pi_{\tau,\mathcal{W}}
\left(
\operatorname{UpdateGraph}
\left(
\mathcal{B}_t,
\operatorname{Acquire}(\mathcal{Q}_t)
\right)
\right)
$$

$$
\Delta\Phi_{t+1}
=
\operatorname{Phase}
\left(
G_{t+1},
\mathcal{W}_t
\right)
$$

$$
\mathcal{M}_{t+1}
=
\mathcal{C}
\left(
\mathcal{R}
\left(
G_{t+1},
\Delta\Phi_{t+1},
\mathcal{W}_t
\right)
\right)
$$

$$
\mathcal{W}_{t+1}
=
\operatorname{ReviseIntent}
\left(
\mathcal{W}_t,
\mathcal{M}_{t+1}
\right)
$$

---

# 附錄 C：版本變更摘要

相較 v0.1，v0.2 主要新增：

1. 將 DRC Search 正式納入 GIPSS，定義為搜尋控制平面；
2. 將 SGCD 正式納入 GIPSS，定義為動態語義資料平面；
3. 將 GIPSS 明確定位為目標與相位判定平面；
4. 建立三平面接口；
5. 建立統一搜尋狀態 $\mathfrak{X}_t$ ；
6. 建立欲種子在 SGCD 中的激活動力學；
7. 將共振重新定義為欲—圖—相位—證據的聯合量；
8. 將反證納入高共振節點；
9. 提出可逆壓縮與證據回溯原則；
10. 建立閉環偽代碼、資料格式與工程模組；
11. 補充分級發現狀態與停止條件；
12. 明確區分工程近似全域與絕對全域；
13. 補充身份解析、治理、隱私與搜尋偏見限制；
14. 提出 v0.3 至 v1.0 的研究路線圖。

---

# 內部理論來源

本版本統一並重構以下三份既有文件：

1. 《全域欲相位語義搜尋法》v0.1；
2. 《DRC Search：生成式 AI 時代的非線性搜尋、共振式爬蟲與認知地圖生成方法》v0.1；
3. 《語義圖論耦合動力學》v0.1。

三份原稿仍應獨立保存，分別作為：

- GIPSS 目標與相位理論來源；
- DRC 搜尋控制協議來源；
- SGCD 動態圖資料模型來源。
