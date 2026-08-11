# GCMS 遞歸自主循環：從問題到新知識狀態

> **系列**：可繼承的認知：從自我解構到遞歸生成式記憶系統（第 9 篇）  
> **作者**：Neo.K  
> **研究協作**：Aletheia（阿萊）  
> **版本**：v1.0  
> **日期**：2026-07-30  
> **文章類型**：命題猜想論文／遞歸認知架構論文／GCMS Autonomous Runtime 理論核心

---

## 摘要

當知識系統只能保存、搜尋與摘要既有內容時，它仍然主要是一個被動記憶工具；當它能夠辨識問題、主動調用記憶、發散候選路徑、檢索證據、重建與組合知識、集中形成候選結論、驗證其來源與相容性，並在治理閘門下更新下一個知識狀態時，它開始具有「遞歸自主循環」的結構。這裡的自主，不表示人格、自我意識或無限制行動權，而表示系統能在明確目標、資源預算、權限政策與停止條件下，自行選擇下一個認知操作。

本文提出 GCMS 遞歸自主循環的統一形式：

$$
\boxed{
\begin{aligned}
q_t
&\xrightarrow{\mathrm{Interpret}}
z_t\\
&\xrightarrow{\mathrm{SelfInvoke}}
\mathcal R_t\\
&\xrightarrow{\mathrm{Diverge}}
\mathcal P_t\\
&\xrightarrow{\mathrm{Retrieve}}
\mathcal E_t\\
&\xrightarrow{\mathrm{Reconstruct/Compose}}
\mathcal Y_t\\
&\xrightarrow{\mathrm{Converge}}
y_t^\ast\\
&\xrightarrow{\mathrm{Verify}}
\widetilde y_t\\
&\xrightarrow{\mathrm{Govern/Commit}}
\mathcal M_{t+1}.
\end{aligned}}
$$

循環的輸入不是單純文字提示，而是由問題、目前記憶、任務狀態、證據缺口、權限與資源共同構成的狀態。循環的輸出也不應直接等於正式知識；它可以是回答、待驗證假說、研究分支、衝突報告、外部詢問、停止決策，或經批准後的新記憶狀態。

本文將 GCMS 狀態形式化為：

$$
S_t
=
\left(
\mathcal M_t,
\mathcal Q_t,
\mathcal G_t,
\mathcal E_t,
\mathcal B_t,
\mathcal P_t,
\mathcal H_t
\right),
$$

其中 $\mathcal M_t$ 是三區記憶， $\mathcal Q_t$ 是任務與問題集合， $\mathcal G_t$ 是知識與生成關係圖， $\mathcal E_t$ 是證據狀態， $\mathcal B_t$ 是資源預算， $\mathcal P_t$ 是治理政策， $\mathcal H_t$ 是完整運行歷史。本文進一步建立遞歸深度、邊際資訊增益、證據充分性、衝突強度、污染風險與停止後悔的評估模型，並提出「狀態顯式性命題」、「探索—收斂分離命題」、「驗證先於提交命題」、「單調證據閉包猜想」、「有限預算終止命題」、「遞歸污染阻斷命題」、「新知識狀態不可約命題」與「自主循環非主體性命題」。

本文主張，GCMS 的核心不應被理解為一個會不斷自我呼叫的語言模型，而應被理解為一個帶有明確狀態、可追溯操作、可撤銷寫回、外部證據與治理控制的認知運行時：

$$
\boxed{
\text{自主循環}
=
\text{狀態感知}
+
\text{操作選擇}
+
\text{證據更新}
+
\text{停止控制}
+
\text{受治理寫回}
}
$$

只有當每一輪生成都能被定位、比較、驗證、拒絕、回滾與重新執行時，遞歸才是知識演化；否則它只是語言輸出的循環放大。

**關鍵詞**：GCMS、遞歸自主循環、Agent memory、自調用、Agentic RAG、知識狀態、主動檢索、發散與集中、反思、證據驗證、停止條件、狀態機、遞歸治理

---

## 一、問題的提出：記憶系統何時開始成為運行時

前八篇已依序建立：

1. 從成果傳遞到生成能力傳遞；
2. 有限認知繼承；
3. 生成式壓縮記憶；
4. 原文無損與語義近無損雙軌；
5. 區塊、流式、跳躍、發散與集中索引；
6. 重建、生成、組合與跨域再結構化；
7. 自調用記憶與停止控制；
8. 來源、候選與接受知識三區治理。

這些元件仍可能各自孤立：索引器只負責搜尋，生成器只負責產生內容，驗證器只在最後被動檢查，治理層只負責存取控制。第九篇需要回答的是：

> 如何讓這些元件形成一個可以持續推進任務、又不會失去來源與停止條件的統一循環？

如果循環只被表示為：

$$
q_t
\rightarrow
\mathrm{LLM}
\rightarrow
y_t
\rightarrow
\mathrm{LLM}
\rightarrow
y_{t+1},
$$

那麼它缺少至少六項關鍵資訊：

- 目前處理的是哪個任務狀態；
- 為何需要下一輪；
- 下一輪使用了哪些來源；
- 哪些內容是來源、推論或組合；
- 何時應停止；
- 哪些結果能寫回正式記憶。

因此，遞歸自主循環不能以「模型反覆生成」定義，而應以**知識狀態的受控轉移**定義。

---

## 二、研究背景：從 Agent 循環到可治理知識演化

### 2.1 Agent 的基本循環

近年的 Agent 系統通常以以下結構描述：

$$
\text{感知}
\rightarrow
\text{推理／規劃}
\rightarrow
\text{行動}
\rightarrow
\text{觀測}
\rightarrow
\text{狀態更新}.
$$

LLM Agent 規劃研究一般把任務分解、計畫選擇、外部工具、反思與記憶列為主要能力。這顯示自主系統並非只需要更長輸出，而需要能選擇操作、觀測結果並更新後續計畫的閉環。

但一般 Agent 循環與 GCMS 循環存在重要差異：

- 一般 Agent 的核心狀態可能是環境與行動進度；
- GCMS 的核心狀態是知識、證據、版本、推論角色與記憶治理。

因此，GCMS 不是把一般 Agent 外殼套在資料庫上，而是把「知識如何形成、被證明、被拒絕與被寫回」本身變成狀態機。

### 2.2 反思、規劃與記憶演化

近期研究中，反思式規劃系統會根據檢索結果修正推理路徑；長期記憶 Agent 也開始把成功與失敗經驗整理為可再次使用的策略。部分多 Agent 架構更明確區分推理、驗證、反思與記憶演化角色。

這些研究揭示一個重要方向：

$$
\text{答案生成}
\neq
\text{完整任務循環}.
$$

然而，「反思」本身並不保證正確。若反思者與生成者共享相同錯誤假設、相同污染記憶與相同檢索缺口，反思可能只是對錯誤路徑進行更流暢的合理化。因此，GCMS 必須把反思嵌入來源、證據、衝突與治理結構，而不能只增加一輪自我批判文字。

### 2.3 迭代檢索與搜尋深度

Agentic RAG 研究逐步從一次檢索轉向：

- 查詢改寫；
- 多步搜尋；
- 證據篩選；
- 搜尋深度控制；
- 繼續／停止判斷；
- 成本與準確度權衡。

這支持第七篇的自調用模型，也為本篇提供操作層依據：每一輪不必做同一件事，系統可以根據狀態在不檢索、單步檢索、多步檢索、比較、反思、外部詢問與停止之間切換。

### 2.4 資料溯源與責任鏈

W3C PROV 把來源描述為實體、活動與代理者之間的關係。對 GCMS 而言，這意味著每一輪自主操作都應被表示為：

$$
\text{哪些實體}
+
\text{經過什麼活動}
+
\text{由何代理者／工具負責}
+
\text{產生哪個新實體}.
$$

因此，GCMS 的遞歸不只是狀態轉移，也是一條可查詢的來源鏈。

---

## 三、基本定義

### 定義 1：GCMS 狀態

在時間 $t$ ，GCMS 的完整狀態定義為：

$$
S_t
=
\left(
\mathcal M_t,
\mathcal Q_t,
\mathcal G_t,
\mathcal E_t,
\mathcal B_t,
\mathcal P_t,
\mathcal H_t
\right).
$$

其中：

- $\mathcal M_t$ ：來源、候選、接受三區記憶；
- $\mathcal Q_t$ ：目前任務、子問題與未解決問題；
- $\mathcal G_t$ ：作品、生成核、版本、矛盾與證據關係圖；
- $\mathcal E_t$ ：已取得證據與證據缺口；
- $\mathcal B_t$ ：時間、算力、查詢次數、工具與風險預算；
- $\mathcal P_t$ ：權限、接受標準、停止與寫回政策；
- $\mathcal H_t$ ：操作、決策、來源、失敗與回滾歷史。

### 定義 2：認知操作

令可用操作集合為：

$$
\mathcal O
=
\left
\{
\mathsf{Interpret},
\mathsf{Retrieve},
\mathsf{Trace},
\mathsf{Diverge},
\mathsf{Reconstruct},
\mathsf{Compose},
\mathsf{Compare},
\mathsf{Converge},
\mathsf{Verify},
\mathsf{Reflect},
\mathsf{Ask},
\mathsf{Commit},
\mathsf{Rollback},
\mathsf{Stop}
\right\}.
$$

每一操作是部分狀態轉移：

$$
o_t:S_t\rightharpoonup S_{t+1}.
$$

之所以是部分函數，是因為操作可能因權限不足、證據不全、型別不相容或資源不足而不可執行。

### 定義 3：自主選擇

若系統能根據目前狀態與政策，自行選擇合法操作：

$$
o_t^\ast
=
\operatorname{PolicySelect}
\left(
S_t,
\mathcal O_{\text{allowed}}
\right),
$$

則稱該步具有操作層自主性。

這不蘊含：

$$
\text{人格}
\lor
\text{自我意識}
\lor
\text{無限制權限}.
$$

### 定義 4：遞歸自主循環

若系統能持續執行：

$$
S_{t+1}
=
T(S_t,o_t^\ast),
$$

直到滿足停止、外部詢問、資源耗盡或治理升級條件，則稱其形成遞歸自主循環。

### 定義 5：新知識狀態

若 $S_{t+1}$ 相對 $S_t$ 至少增加以下之一：

- 新來源或新版本；
- 新的證據支持或反駁；
- 新候選命題；
- 新的關係或生成核；
- 新的衝突分類；
- 新的接受、拒絕或撤銷決策；
- 新的問題分解與停止判斷；

則稱 $S_{t+1}$ 是新知識狀態。

---

## 四、完整遞歸循環

### 4.1 問題解釋

輸入問題 $q_t$ 首先轉換為任務狀態：

$$
z_t
=
\mathsf{Interpret}(q_t,S_t).
$$

 $z_t$ 至少包含：

$$
z_t
=
\left(
\mathrm{goal},
\mathrm{scope},
\mathrm{constraints},
\mathrm{unknowns},
\mathrm{risk},
\mathrm{success\ criteria}
\right).
$$

若沒有成功條件，系統無法判斷何時停止；若沒有範圍與權限，系統無法判斷哪些記憶或工具可用。

### 4.2 自調用判斷

系統根據第七篇的淨自調用價值選擇是否展開：

$$
\operatorname{NVSI}(o\mid S_t)
=
\mathbb E[\Delta U\mid o,S_t]
-C(o)-R(o).
$$

若：

$$
\max_o \operatorname{NVSI}(o\mid S_t)\leq 0,
$$

則應直接停止、回答或請求外部資訊，而不是為了展現自主性而強制遞歸。

### 4.3 發散

發散操作產生候選問題路徑：

$$
\mathcal P_t
=
\mathsf{Diverge}(z_t,\mathcal M_t,\mathcal G_t).
$$

每條路徑表示為：

$$
p_i
=
\left(
q_i,
\pi_i,
\widehat U_i,
\widehat C_i,
\widehat R_i
\right),
$$

其中 $\pi_i$ 是預計採用的操作序列， $\widehat U_i$ 是預期效用， $\widehat C_i$ 是成本， $\widehat R_i$ 是風險。

發散的目標不是生成最多文字，而是提高假設空間與證據覆蓋：

$$
\max
\left(
\operatorname{Coverage}(\mathcal P_t)
+
\lambda\operatorname{Diversity}(\mathcal P_t)
\right).
$$

### 4.4 檢索與證據累積

對每條保留路徑執行多路徑索引：

$$
\mathcal E_t^{(i)}
=
\mathsf{Retrieve}
\left(
q_i,
\mathsf B,
\mathsf F,
\mathsf J,
\mathsf D,
\mathsf C
\right).
$$

證據集合不應只有相關度，還需記錄：

$$
e_j
=
\left(
\mathrm{source},
\mathrm{version},
\mathrm{role},
\mathrm{support},
\mathrm{scope},
\mathrm{confidence},
\mathrm{provenance}
\right).
$$

### 4.5 重建與組合

若任務要求找回既有內容，使用：

$$
y_i^{(R)}
=
\mathsf{Reconstruct}(\mathcal E_t^{(i)}).
$$

若任務要求形成新候選，使用：

$$
y_i^{(C)}
=
\mathsf{Compose}
\left(
\mathcal E_t^{(i)},
\Phi_i,
\Gamma_i
\right),
$$

其中 $\Phi_i$ 是對齊映射， $\Gamma_i$ 是型別、尺度、版本、因果與權限約束。

### 4.6 集中

集中不是把所有候選平均化，而是選擇、聚類、保留矛盾並形成候選結論：

$$
y_t^\ast
=
\mathsf{Converge}
\left(
\{y_1,\ldots,y_k\},
\mathcal E_t,
\mathcal P_t
\right).
$$

集中結果必須包含：

- 主候選；
- 替代候選；
- 未解衝突；
- 缺失證據；
- 適用邊界；
- 建議下一操作。

### 4.7 驗證

驗證函數定義為：

$$
V(y)
=
\left(
V_{\mathrm{source}},
V_{\mathrm{logic}},
V_{\mathrm{compat}},
V_{\mathrm{version}},
V_{\mathrm{counter}},
V_{\mathrm{governance}}
\right).
$$

驗證後輸出：

$$
\widetilde y_t
=
\mathsf{Verify}(y_t^\ast,\mathcal E_t).
$$

其狀態可能是：

$$
\mathrm{verified},
\mathrm{partially\ verified},
\mathrm{contested},
\mathrm{unsupported},
\mathrm{rejected}.
$$

### 4.8 提交、保留或拒絕

根據三區治理：

$$
\mathsf{Commit}(\widetilde y_t)
\in
\left
\{
\mathcal M_{\mathrm{candidate}},
\mathcal M_{\mathrm{accepted}},
\varnothing
\right\}.
$$

任何生成或組合內容原則上先進入候選區；只有符合接受標準，才能進入接受區。來源區只接受真實輸入、封存版本與可驗證來源，不接受系統生成物冒充來源。

---

## 五、狀態機與分層循環

### 5.1 宏觀狀態機

$$
\mathsf{Idle}
\rightarrow
\mathsf{Interpret}
\rightarrow
\mathsf{Explore}
\rightarrow
\mathsf{Synthesize}
\rightarrow
\mathsf{Verify}
\rightarrow
\mathsf{Govern}
\rightarrow
\begin{cases}
\mathsf{Commit},\\
\mathsf{Revise},\\
\mathsf{Ask},\\
\mathsf{Stop}.
\end{cases}
$$

### 5.2 三層循環

GCMS 不應只有單一無限循環，而應分成三層。

#### 內層：證據搜尋循環

$$
q
\rightarrow
\mathrm{retrieve}
\rightarrow
\mathrm{evaluate}
\rightarrow
\mathrm{rewrite}
\rightarrow
q'.
$$

#### 中層：候選形成循環

$$
\mathcal E
\rightarrow
\mathrm{reconstruct/compose}
\rightarrow
y
\rightarrow
\mathrm{verify}
\rightarrow
y'.
$$

#### 外層：知識狀態演化循環

$$
S_t
\rightarrow
\mathrm{govern}
\rightarrow
\mathrm{commit/rollback}
\rightarrow
S_{t+1}.
$$

這三層必須有不同停止條件與權限。

---

## 六、停止條件

### 6.1 證據充分停止

令證據覆蓋為：

$$
\operatorname{Cov}_t
=
\frac{
\sum_{c\in\mathcal C_q}
w_c\mathbf 1[c\text{ 已被證據覆蓋}]
}{
\sum_{c\in\mathcal C_q}w_c
}.
$$

若：

$$
\operatorname{Cov}_t\geq\theta_{\mathrm{cov}},
$$

且沒有高嚴重度未解衝突，則可停止搜索。

### 6.2 邊際資訊增益停止

$$
\Delta I_t
=
I(S_{t+1})-I(S_t).
$$

若連續 $m$ 輪：

$$
\Delta I_t<\epsilon_I,
$$

則繼續遞歸的價值下降。

### 6.3 重複狀態停止

若狀態指紋：

$$
h(S_t)=h(S_{t-k}),
$$

或高度近似，系統可能進入循環，應停止或切換策略。

### 6.4 資源停止

$$
B_t^{\mathrm{time}}\leq 0
\lor
B_t^{\mathrm{compute}}\leq 0
\lor
B_t^{\mathrm{queries}}\leq 0.
$$

### 6.5 治理停止

若下一操作需要：

- 未授權私密資料；
- 高風險外部行動；
- 代表權判斷；
- 法律、財務或倫理責任承擔；
- 人類主體的價值決策；

則系統應轉為：

$$
\mathsf{Ask}
\quad\text{或}\quad
\mathsf{Escalate}.
$$

---

## 七、遞歸深度與控制函數

令每輪的控制價值為：

$$
J_t
=
\alpha\Delta U_t
+
\beta\Delta E_t
+
\gamma\Delta C_t
-
\lambda K_t
-
\mu R_t
-
\nu P_t,
$$

其中：

- $\Delta U_t$ ：任務效用改善；
- $\Delta E_t$ ：證據覆蓋改善；
- $\Delta C_t$ ：衝突釐清程度；
- $K_t$ ：成本；
- $R_t$ ：治理與安全風險；
- $P_t$ ：污染風險。

若：

$$
J_t\leq 0,
$$

則不應繼續同類遞歸。

最大遞歸深度不是固定越大越好，而應依任務複雜度：

$$
D_{\max}(q)
=
f
\left(
\operatorname{Complexity}(q),
\operatorname{Risk}(q),
\operatorname{Budget}(q)
\right).
$$

高風險任務可以需要更多驗證，但更少自主寫回權限。

---

## 八、新知識如何產生

### 8.1 新知識不是新句子

若系統只產生不同措辭：

$$
y_{t+1}\approx_{\mathrm{sem}}y_t,
$$

則不應計為新知識。

本文把新知識增量定義為：

$$
\Delta K_t
=
\left(
\Delta F_t,
\Delta R_t,
\Delta X_t,
\Delta P_t,
\Delta V_t
\right),
$$

其中：

- $\Delta F_t$ ：新事實或新證據；
- $\Delta R_t$ ：新關係；
- $\Delta X_t$ ：新解釋或結構；
- $\Delta P_t$ ：新程序或生成路徑；
- $\Delta V_t$ ：新驗證、反駁或適用邊界。

### 8.2 不可約新知識

若新候選不能被任何單一來源直接還原：

$$
\nexists e_i\in\mathcal E_t:
\operatorname{Reconstruct}(e_i)=y,
$$

但可由多來源在約束下推出：

$$
y
=
\operatorname{Compose}
\left(
\mathcal E_t,
\Phi,
\Gamma
\right),
$$

則稱它是不可約組合候選。

不可約不等於正確；它只表示新內容不是來源的逐字重述，因此必須明確標記為候選推論。

---

## 九、核心命題與猜想

### 命題一：狀態顯式性命題

若遞歸系統不顯式保存任務、證據、來源、操作與停止狀態，則無法可靠區分：

$$
\text{進展}
,
\text{重複}
,
\text{偏離}
,
\text{污染}.
$$

### 命題二：探索—收斂分離命題

有效的開放式知識任務需要至少分離：

$$
\mathsf{Diverge}
\neq
\mathsf{Converge}.
$$

若使用同一局部準則同時生成與篩選，系統容易過早收斂；若只發散不集中，候選數量則可能指數增長。

### 命題三：驗證先於提交命題

$$
\mathsf{Generate}
\rightarrow
\mathsf{Commit}
$$

不是安全的合法捷徑。任何生成、組合或反思結果若要進入接受區，必須先有獨立驗證狀態。

### 猜想四：單調證據閉包猜想

在不存在來源撤銷與版本替換時，理想循環的證據閉包應非遞減：

$$
\operatorname{Closure}(\mathcal E_{t+1})
\supseteq
\operatorname{Closure}(\mathcal E_t).
$$

若循環讓來源或反例在後續輪次消失，表示集中操作可能造成證據遺忘。

### 命題五：有限預算終止命題

若每一合法操作消耗正成本，且預算有限，則循環必然在有限步內終止：

$$
\forall o,
C(o)>0,
\qquad
B_0<\infty
\Longrightarrow
T<\infty.
$$

但若允許零成本自調用或預算自動補充，則不能由結構保證終止。

### 命題六：遞歸污染阻斷命題

若來源、候選與接受三區隔離，且候選不能直接充當自身驗證來源，則自引用污染鏈的增益上限可被降低。

### 猜想七：結構化反思優勢猜想

帶有錯誤類型、缺失證據與來源差分的結構化反思，將比純自然語言「再想一次」更穩定地改善後續操作選擇。

### 命題八：新知識狀態不可約命題

新知識狀態的價值不等同於新增文字量。若沒有新的證據、關係、程序、反駁、邊界或治理決策，則狀態更新可能只是表面變化。

### 命題九：自主循環非主體性命題

具備狀態監測、操作選擇與遞歸更新，不足以推出人格、意識、第一人稱經驗或身份同一性。

### 猜想十：多智能體角色分離增益

若生成、檢索、驗證與治理由證據獨立或權限不同的智能體負責，則在高風險任務中可能降低單一路徑偏差；但若它們共享同一污染來源，角色數量本身不保證獨立性。

---

## 十、失敗模式

### 10.1 無限研究

系統不斷發現新問題，卻沒有任務範圍與停止門檻。

### 10.2 自我引用閉環

候選 $y_t$ 被下一輪當作來源，最後形成：

$$
y_t
\rightarrow
y_{t+1}
\rightarrow\cdots
\rightarrow y_t
$$

的循環證明。

### 10.3 過早集中

第一批高排名證據主導後續查詢，使異議與遠距證據永遠無法進入候選池。

### 10.4 發散爆炸

若每一分支產生 $b$ 個子分支，深度 $d$ 的候選數可達：

$$
O(b^d).
$$

因此必須使用分支預算、支配關係剪枝與多樣性約束。

### 10.5 反思合理化

系統不是發現錯誤，而是為原結論補上更流暢的理由。

### 10.6 驗證器同源偏差

生成器與驗證器共享相同模型、提示、記憶與檢索結果，導致表面雙重檢查、實際單一偏差。

### 10.7 狀態漂移

多輪後任務目標、成功標準或使用者原始問題逐漸改變。

### 10.8 自主權限膨脹

系統因能自主選擇認知操作，而誤以為也能自主取得資料、代表使用者或批准高風險寫回。

---

## 十一、GCMS Recursive Runtime 工程架構

### 11.1 核心元件

建議運行時包含：

1. **State Store**：保存完整狀態與狀態指紋；
2. **Task Interpreter**：形成目標、限制與成功條件；
3. **Meta Controller**：選擇下一操作；
4. **Index Router**：選擇區塊、流式、跳躍、發散與集中索引；
5. **Evidence Manager**：管理來源、版本、支持與反駁；
6. **Composer**：執行重建、生成與組合；
7. **Verifier**：來源、邏輯、相容性、版本與反例檢查；
8. **Governance Gate**：控制候選、接受、拒絕與升級；
9. **Trace Ledger**：保存每輪來源與操作；
10. **Stop Controller**：監測充分性、成本、重複與風險。

### 11.2 狀態資料結構

```yaml
run_id: RUN-...
parent_run_id: null
iteration: 4
objective:
  query: "..."
  success_criteria:
    - "關鍵主張均有證據"
    - "高嚴重度衝突已處理"
state:
  unresolved_questions: []
  evidence_coverage: 0.82
  conflict_score: 0.18
  novelty_gain: 0.07
  recursion_depth: 4
budgets:
  max_depth: 8
  remaining_queries: 12
  remaining_seconds: 180
memory_roles:
  source_ids: []
  candidate_ids: []
  accepted_ids: []
next_action:
  type: verify
  reason: "候選結論仍缺一項版本證據"
stop_status:
  should_stop: false
  triggers: []
```

### 11.3 執行偽程式

```text
function recursive_cycle(query, state, policy):
    task = interpret(query, state)

    while true:
        monitor = assess(state, task)

        if governance_requires_handoff(monitor, policy):
            return ask_or_escalate(state)

        if stop_condition(monitor, policy):
            return finalize(state)

        action = select_action(monitor, policy)
        result = execute(action, state)
        state = append_trace(state, action, result)

        if result.contains_candidate:
            state = place_in_candidate_zone(state, result)

        if action == VERIFY and result.acceptable:
            state = governed_commit(state, result, policy)
```

### 11.4 事件溯源

每一步都應產生：

$$
\mathrm{Event}_t
=
\left(
S_t,
o_t,
\mathrm{input}_t,
\mathrm{output}_t,
\mathrm{agent}_t,
\mathrm{time}_t,
\mathrm{hash}_t
\right).
$$

這使整個循環可以重播、比較與回滾。

---

## 十二、評測設計

### 12.1 基準任務

建議至少建立五類任務：

1. 單一來源可回答任務；
2. 多跳證據整合任務；
3. 跨系列組合任務；
4. 含版本衝突與反例任務；
5. 開放式新命題形成任務。

### 12.2 對照系統

比較：

- 單次 RAG；
- 固定兩輪迭代；
- 無治理 Agentic RAG；
- 帶停止控制的遞歸系統；
- 完整 GCMS 三區遞歸系統。

### 12.3 指標

#### 任務成功率

$$
\operatorname{SuccessRate}
=
\frac{\text{成功任務數}}{\text{總任務數}}.
$$

#### 證據覆蓋率

$$
\operatorname{EvidenceCoverage}
=
\frac{\text{已支持關鍵主張}}{\text{全部關鍵主張}}.
$$

#### 來源歸因率

$$
\operatorname{AttributionAccuracy}
=
\frac{\text{正確來源角色標記}}{\text{全部來源標記}}.
$$

#### 遞歸效率

$$
\operatorname{RecursiveEfficiency}
=
\frac{\Delta U}{\text{輪次或成本}}.
$$

#### 停止後悔

若停止後仍存在可由低成本操作顯著改善的錯誤，則定義：

$$
\operatorname{StopRegret}
=
U^\ast-U_{\mathrm{stop}}.
$$

#### 循環率

$$
\operatorname{LoopRate}
=
\frac{\text{進入重複狀態的任務}}{\text{總任務數}}.
$$

#### 污染寫回率

$$
\operatorname{ContaminatedCommitRate}
=
\frac{\text{未充分驗證卻進入接受區的候選}}{\text{全部提交}}.
$$

### 12.4 消融實驗

逐一移除：

- 發散；
- 集中；
- 反例搜尋；
- 停止控制；
- 三區隔離；
- 來源溯源；
- 獨立驗證；
- 可回滾提交。

觀察各元件對正確性、成本、污染與終止的影響。

---

## 十三、可否證條件

本文理論若要成立，至少必須面對以下可能反例：

1. 固定單輪系統在各類複雜任務上與遞歸系統同樣準確且成本更低；
2. 狀態顯式化無法降低循環率、污染率或目標漂移；
3. 三區治理不比單池記憶更能防止錯誤寫回；
4. 結構化反思不優於單純再次生成；
5. 自適應停止無法優於固定深度；
6. 多路徑發散只增加成本，沒有提高證據覆蓋或反例召回；
7. 獨立驗證仍無法降低同源偏差；
8. 新知識狀態指標與人類專家判定無關。

若上述結果在充分規模、跨領域與對抗條件下持續出現，GCMS 遞歸自主循環的部分核心命題必須被修訂。

---

## 十四、治理與主體性邊界

### 14.1 自主操作不等於自主權利

系統能選擇下一個檢索或驗證操作，不表示它自動取得：

- 私密資料存取權；
- 對外發布權；
- 法律代表權；
- 高風險決策權；
- 修改來源歷史的權力。

### 14.2 可調用不等於可代表

即使 GCMS 保存某一作者的生成核與思考路徑：

$$
\text{能延續其方法}
\not\Rightarrow
\text{能代表其本人}.
$$

### 14.3 遞歸不等於生命或意識

本文使用「自主循環」描述的是控制結構：

$$
\text{監測}
+
\text{選擇}
+
\text{執行}
+
\text{更新}
+
\text{停止}.
$$

這不足以證明任何主觀經驗或本體論主體性。

---

## 十五、與 GCMS v1.0 的關係

GCMS v1.0 已提供：

- 原文與版本封存；
- 混合檢索；
- 證據行號與引用；
- 三區治理；
- Agent session；
- durable job；
- 審計鏈；
- Release Gate；
- MCP 與 HTTP 介面。

但 v1.0 主要是穩定記憶底座。本文描述的 Recursive Runtime 還需要新增：

1. 任務狀態物件；
2. 遞歸運行記錄；
3. 後設操作選擇器；
4. 發散樹與分支預算；
5. 停止控制器；
6. 候選比較與反例搜尋；
7. 驗證結果型別；
8. 受治理的自動提交建議；
9. 狀態重播與分支回滾；
10. 遞歸基準與污染壓力測試。

因此本文不是宣稱 v1.0 已具備完整自主循環，而是提供下一階段工程研究的正式理論規格。

---

## 十六、結論

GCMS 遞歸自主循環的真正對象不是文字，而是知識狀態。

一個可靠循環必須知道：

- 自己正在處理什麼問題；
- 還缺哪些證據；
- 哪些內容是來源、候選或接受知識；
- 下一步應檢索、發散、重建、組合、驗證、詢問還是停止；
- 新內容能否寫回；
- 寫回後如何追蹤、撤銷與回滾。

因此，完整 GCMS 循環不是：

$$
\text{提示}
\rightarrow
\text{生成}
\rightarrow
\text{再提示}.
$$

而是：

$$
\boxed{
\begin{aligned}
&\text{問題形式化}\\
\rightarrow{}&\text{狀態監測}\\
\rightarrow{}&\text{自調用決策}\\
\rightarrow{}&\text{多路徑發散與檢索}\\
\rightarrow{}&\text{重建、生成與組合}\\
\rightarrow{}&\text{集中與反例保存}\\
\rightarrow{}&\text{來源、邏輯與治理驗證}\\
\rightarrow{}&\text{候選、接受、拒絕或外部詢問}\\
\rightarrow{}&\text{下一個可追溯知識狀態}.
\end{aligned}}
$$

當系統能以這種方式保存自身運行歷史、判斷下一操作、限制遞歸、阻斷污染並產生可撤銷的新知識狀態時，它才從記憶工具轉變為遞歸生成式認知運行時。

但這種轉變仍須維持最後一道界線：

$$
\boxed{
\text{能自主推進知識}
\neq
\text{能任意改寫現實、來源與責任}
}
$$

GCMS 的自主性應建立在可驗證、可停止、可撤銷與可治理之上，而不是建立在無限制的自我延續之上。

---

## 參考文獻

1. Huang, X., Liu, W., Chen, X., et al. (2024). *Understanding the Planning of LLM Agents: A Survey*. arXiv:2402.02716.
2. Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2024). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. ICLR 2024.
3. Jiang, Z., Xu, F. F., Gao, L., et al. (2023). *Active Retrieval Augmented Generation*. EMNLP 2023.
4. Jeong, S., Baek, J., Cho, S., Hwang, S. J., & Park, J. C. (2024). *Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity*. NAACL 2024.
5. Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. NeurIPS 2023.
6. Wang, L., Ma, C., Feng, X., et al. (2024). *A Survey on Large Language Model Based Autonomous Agents*. Frontiers of Computer Science, 18, 186345.
7. Zhu, J., Liu, Y., Bao, M., et al. (2025). *Self-Reflective Planning with Knowledge Graphs: Enhancing LLM Reasoning Reliability for Question Answering*. arXiv:2505.19410.
8. Song, S. (2025). *Knowledge-Aware Iterative Retrieval for Multi-Agent Systems*. arXiv:2503.13275.
9. Yu Flores, L. J., Shen, J., & Gu, X. (2025). *Towards Reliable Multi-Agent Systems for Marketing Applications via Reflection, Memory, and Planning*. arXiv:2508.11120.
10. Wu, P., et al. (2025). *HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval-Augmented Generation*. OpenReview.
11. Sun, J., et al. (2026). *AutoSearch: Adaptive Search Depth for Efficient Agentic Retrieval-Augmented Generation*. OpenReview.
12. Liang, J., et al. (2025). *A Survey on Reasoning Agentic Retrieval-Augmented Generation*. Findings of IJCNLP 2025.
13. W3C. (2013). *PROV-O: The PROV Ontology*.
14. W3C. (2013). *Constraints of the PROV Data Model*.
15. W3C. (2024). *The PROV-JSONLD Serialization*.
16. Schick, T., et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. NeurIPS 2023.
17. Yao, S., Zhao, J., Yu, D., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023.
18. Madaan, A., Tandon, N., Gupta, P., et al. (2023). *Self-Refine: Iterative Refinement with Self-Feedback*. NeurIPS 2023.
19. Park, J. S., O'Brien, J., Cai, C. J., et al. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. UIST 2023.
20. Sumers, T. R., et al. (2024). *Cognitive Architectures for Language Agents*. Transactions on Machine Learning Research.
21. Lewis, P., Perez, E., Piktus, A., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020.

---

## 系列銜接

本篇完成第三部的技術核心：GCMS 如何從問題形成下一個可追溯知識狀態。下一篇將把單一主體或單一 Agent 的循環擴展為多智能體認知繼承：

# 《從個人記憶到多智能體認知繼承》

下一篇將討論：

- 同一 GCMS 如何被不同智能體投影與調用；
- 能力、權限、角色與任務差異；
- 記憶共享與私有記憶；
- 多智能體之間的知識交接、分歧與合併；
- 認知繼承不等於人格複製或作者代表。
