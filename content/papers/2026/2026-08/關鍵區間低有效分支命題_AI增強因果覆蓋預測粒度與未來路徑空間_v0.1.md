# 關鍵區間低有效分支命題：AI 增強因果覆蓋、預測粒度與未來路徑空間

**The Low Effective Branching Thesis for Critical Intervals: AI-Augmented Causal Coverage, Forecasting Granularity, and Future Path Spaces**

- **作者**：Neo.K
- **版本**：v0.1
- **日期**：2026-07-30
- **文件性質**：未來研究／概率預測／AI 增強研究／因果情境空間命題論文

---

## 摘要

世界的微觀狀態、事件排列與主體選擇可能形成極其龐大的未來空間，因此「完整窮盡未來」通常不可行。然而，對特定時間尺度、問題邊界與宏觀判定粒度而言，真正滿足物理、資源、制度、技術與策略約束的高機率因果路徑，未必像表面想像那樣多。大量微觀差異可能匯入少數宏觀結果族；多條敘事路徑也可能共享同一因果骨架。

本文提出「關鍵區間低有效分支命題」：設全部可想像未來為 $\Omega$ ，受約束可行路徑集合為 $\mathcal F$ ，宏觀粗粒化映射為 $\pi$ ，則在指定關鍵區間 $[t_0,t_1]$ 中，承載主要機率質量與決策意義的有效分支數，可能遠低於全部表面可能性：

$$
|\Omega|\gg1,
\qquad
N_{\mathrm{eff}}
\left(
\pi(\mathcal F_{[t_0,t_1]})
\right)
\ll
|\Omega|.
$$

本文以機率熵定義有效分支數：

$$
N_{\mathrm{eff}}
=
\exp
\left(
-\sum_{i=1}^{n}p_i\log p_i
\right),
$$

並進一步區分原始敘述數、因果機制數、可行分支數、有效機率分支數與決策相關分支數。由 AI 生成一百個情境，並不表示取得一百個獨立未來；若其共享相同因果假設、資料來源或模型偏差，其真正新增覆蓋可能極低。

本文提出「AI 增強因果覆蓋命題」：人類研究者提供問題選擇、理論先驗、判定尺度與相變辨識；AI 則提供高通量搜尋、跨域類比、情境展開、反例生成與證據更新。兩者結合可提高宏觀路徑覆蓋率，但成立條件不是單純增加算力，而是具備因果去重、來源多樣性、模型差異、基準率、機率校準與事後回測。

本文區分路徑覆蓋、機率校準、時間精度、細節精度與決策效用。預先提及某種可能性不等於準確預測；真正預測系統必須在結果未知時固定問題、時間窗、判定規則和概率，並使用 Brier 分數、對數分數、可靠度與解析度等指標評估。

最後，本文提出一個 AI 自主預測平台的基本架構：將論文、證據、事件、因果瓶頸、關鍵指標與概率更新組織成動態情境圖，而不是持續堆積未評分文章。本文不主張世界可以完全預測，而主張：

$$
\boxed{
\text{未來未必容易預測，}
\quad
\text{但在正確粒度與約束下，}
\quad
\text{可能比人們原先以為的更容易被覆蓋。}
}
$$

**關鍵詞**：有效分支、因果覆蓋、AI 預測、情境空間、宏觀粗粒化、機率校準、人機混合預測、相變節點、ForecastBench

---

## 一、問題提出：可能性很多，還是我們把同一條路徑說了很多遍？

面對未來，人們常在兩種直覺間擺盪。

第一種認為：

$$
\text{世界極度複雜}
\Rightarrow
\text{未來幾乎不可預測}.
$$

第二種認為：

$$
\text{資料與算力足夠}
\Rightarrow
\text{未來可以被完整算出}.
$$

本文不接受這兩個極端。

世界可以同時具有：

- 巨大的微觀狀態空間；
- 有限的物理與制度約束；
- 高度不均勻的概率分布；
- 少數關鍵因果瓶頸；
- 大量匯聚至相同宏觀結果的路徑。

所以真正需要問的不是：

> 未來總共有多少種可能？

而是：

> 在指定時間、尺度和問題中，有多少個因果上獨立、概率上顯著、決策上重要的有效分支？

---

## 二、五種未來空間必須分開

設當前狀態為 $x_t$ 。

### 2.1 可想像空間

$$
\Omega_t
=
\left\{
\text{所有能被描述的未來}
\right\}.
$$

它包含幻想、邏輯矛盾、物理上不可行與制度上不可到達的敘事。

### 2.2 邏輯一致空間

$$
\Omega_t^{L}
\subseteq
\Omega_t.
$$

排除內部矛盾，但仍可能違反現實物理或資源條件。

### 2.3 可行路徑空間

$$
\mathcal F_t
=
\left\{
\pi:
\operatorname{Constraint}(\pi)=1
\right\}
\subseteq
\Omega_t^{L}.
$$

它滿足：

- 物理約束；
- 資源約束；
- 技術前置條件；
- 制度規則；
- 時間限制；
- 行動者可達能力。

### 2.4 機率有效空間

$$
\mathcal P_t(\epsilon)
=
\left\{
\pi\in\mathcal F_t:
P(\pi)\geq\epsilon
\right\}.
$$

它排除極低機率路徑，但 $\epsilon$ 必須依風險用途設定。

### 2.5 決策相關空間

$$
\mathcal D_t
=
\left\{
\pi:
P(\pi)\cdot L(\pi)\geq\theta_D
\right\},
$$

其中 $L(\pi)$ 是損失、收益或決策影響。

低機率高衝擊路徑可能不屬於高概率集合，卻仍屬於決策相關集合。

因此：

$$
\boxed{
\text{不太可能}
\neq
\text{不值得準備}.
}
$$

---

## 三、微觀龐大與宏觀有限可以同時成立

設未來微觀狀態為：

$$
\omega_1,\omega_2,\ldots,\omega_m.
$$

建立宏觀分類映射：

$$
\pi:
\Omega
\rightarrow
\left\{
C_1,C_2,\ldots,C_k
\right\}.
$$

每個 $C_i$ 代表一個宏觀結果族，例如：

- 技術快速突破；
- 漸進改良；
- 監管延遲；
- 商業失敗；
- 替代技術勝出；
- 系統性事故。

可能存在：

$$
m\gg k.
$$

數百萬種內部事件排列，最後都可能屬於「漸進改良但未跨越部署門檻」。

所以：

$$
\boxed{
\text{微觀路徑數量巨大，}
\quad
\text{不代表宏觀結果族同樣巨大。}
}
$$

這是本文能討論「低有效分支」而不主張世界決定論的基本前提。

---

## 四、原始分支數與有效分支數

設宏觀結果族機率為：

$$
p_1,p_2,\ldots,p_n,
\qquad
\sum_{i=1}^{n}p_i=1.
$$

原始分支數為：

$$
N_{\mathrm{raw}}=n.
$$

若各分支機率高度不均勻，原始數量會誇大實際不確定性。

本文採用熵的指數形式定義有效分支數：

$$
N_{\mathrm{eff}}
=
\exp
\left(
H(P)
\right),
$$

其中：

$$
H(P)
=
-\sum_{i=1}^{n}p_i\log p_i.
$$

若十個分支機率完全相同：

$$
p_i=0.1,
$$

則：

$$
N_{\mathrm{eff}}=10.
$$

若主要概率集中在兩三個分支，其餘極低：

$$
N_{\mathrm{eff}}\ll10.
$$

因此，有效分支不是「非零分支的數量」，而是與目前機率分布具有相同不確定性的等概率分支數。

---

## 五、關鍵區間低有效分支命題

設關鍵時間區間為：

$$
\tau=[t_0,t_1].
$$

設受約束路徑集合為：

$$
\mathcal F_{\tau}.
$$

經過宏觀粗粒化：

$$
\pi_{\mathcal G}:
\mathcal F_{\tau}
\rightarrow
\mathcal C_{\tau},
$$

其中 $\mathcal G$ 是判定粒度。

本文提出：

$$
\boxed{
|\Omega_{\tau}|\gg1,
\qquad
N_{\mathrm{eff}}
\left(
\pi_{\mathcal G}(\mathcal F_{\tau})
\right)
\ll
|\Omega_{\tau}|.
}
$$

此命題不是普遍數學定理，而是一項需要對不同領域進行實證檢查的理論假說。

它較可能在以下條件成立：

1. 時間區間相對有限；
2. 基礎設施和制度慣性強；
3. 技術前置依賴清楚；
4. 關鍵行動者數量有限；
5. 存在共同瓶頸；
6. 宏觀判定粒度適當；
7. 分支機率高度集中。

---

## 六、為什麼關鍵區間的有效分支會縮小？

### 6.1 物理與資源限制

任何技術路徑都受到：

$$
\mathcal C_{\mathrm{physical}}
+
\mathcal C_{\mathrm{energy}}
+
\mathcal C_{\mathrm{capital}}
+
\mathcal C_{\mathrm{time}}.
$$

大量想像方案根本無法在指定區間內落地。

### 6.2 依賴圖限制

若能力 $C$ 依賴：

$$
A\rightarrow B\rightarrow C,
$$

則沒有 $A$ 與 $B$ ，直接到達 $C$ 的路徑會被排除。

### 6.3 制度慣性

法律、標準、供應鏈、組織利益與既有設備形成路徑依賴：

$$
x_{t+1}
=
f(x_t,\Delta_t).
$$

可達狀態通常不是任意跳躍。

### 6.4 策略收斂

面對相同成本、風險和市場激勵，不同行動者可能獨立收斂至相似策略。

### 6.5 因果瓶頸

大量不同路徑可能必須通過共同節點：

$$
\pi_1,\pi_2,\ldots,\pi_n
\rightarrow
B
\rightarrow
\mathcal Q.
$$

例如長期 AI 代理不論底層模型如何，都需要處理記憶、授權、工具錯誤與身份連續。

---

## 七、低有效分支不等於低事件數量

即使宏觀分支很少，每個分支內仍可包含大量事件。

設：

$$
C_i
=
\left\{
\omega_{i1},\omega_{i2},\ldots
\right\}.
$$

則：

$$
|C_i|\gg1
$$

完全可能。

所以本文所稱的低有效分支，是：

$$
\text{宏觀因果族較少},
$$

而不是：

$$
\text{世界細節較少}.
$$

同一個「AI 監管延遲」分支，可能包含不同國家、公司、法案、事故與市場反應。

預測者可能命中結構方向，卻錯過具體事件序列。

---

## 八、路徑覆蓋與事件命中必須分開

設預測系統產生候選路徑集合：

$$
\widehat{\mathcal P}
=
\left\{
\widehat\pi_1,\ldots,\widehat\pi_m
\right\}.
$$

實際結果路徑為：

$$
\pi^\ast.
$$

事件命中只檢查某一結果是否曾被提及：

$$
\operatorname{Hit}
\left(
\pi^\ast,\widehat{\mathcal P}
\right).
$$

但路徑覆蓋應檢查：

- 關鍵因果機制；
- 中間瓶頸；
- 分支條件；
- 可觀測指標；
- 概率分配。

可定義機率質量覆蓋：

$$
C_{\mathrm{mass}}
=
\sum_{i:
C_i\in\widehat{\mathcal C}}
p_i.
$$

若預測集合覆蓋了概率質量最高的三個結果族，即使未列出所有細節，也可能具有高決策價值。

---

## 九、五種預測能力

### 9.1 可能性發現

$$
C_{\mathrm{poss}}
=
\text{是否辨識到某路徑存在}.
$$

### 9.2 因果路徑覆蓋

$$
C_{\mathrm{path}}
=
\text{是否涵蓋主要獨立機制}.
$$

### 9.3 機率校準

$$
C_{\mathrm{cal}}
=
\text{概率是否與長期發生率一致}.
$$

### 9.4 時間精度

$$
C_{\mathrm{time}}
=
\text{是否落在正確時間窗}.
$$

### 9.5 細節精度

$$
C_{\mathrm{detail}}
=
\text{主體、地點、順序與規模是否正確}.
$$

一個研究者可能具有：

$$
C_{\mathrm{path}}\gg0
$$

卻只有中等：

$$
C_{\mathrm{time}},
\quad
C_{\mathrm{detail}}.
$$

這不等於沒有預測價值，但不能把結構覆蓋誇大為精確預言。

---

## 十、AI 如何提高因果覆蓋？

大型語言模型和搜尋代理可以高速執行：

$$
\text{檢索}
\rightarrow
\text{分解}
\rightarrow
\text{生成}
\rightarrow
\text{比較}
\rightarrow
\text{反駁}
\rightarrow
\text{重組}.
$$

其優勢包括：

- 快速搜尋多來源；
- 跨領域類比；
- 產生反事實；
- 展開行動者策略；
- 列出前置依賴；
- 生成低概率風險；
- 持續吸收新訊號。

人類研究者則提供：

- 問題選擇；
- 長期理論先驗；
- 判定粒度；
- 價值與風險邊界；
- 相變節點辨識；
- 對語義同構的直覺。

因此可以提出：

$$
\boxed{
\operatorname{Coverage}_{H+AI}
>
\max
\left(
\operatorname{Coverage}_H,
\operatorname{Coverage}_{AI}
\right)
}
$$

但這只在協作具有互補性時成立。

---

## 十一、人機結合不是簡單相加

設人類模型誤差為：

$$
\epsilon_H,
$$

AI 模型誤差為：

$$
\epsilon_A.
$$

若兩者誤差高度相關：

$$
\operatorname{Corr}
(\epsilon_H,\epsilon_A)\approx1,
$$

組合收益有限。

如果：

$$
\operatorname{Corr}
(\epsilon_H,\epsilon_A)\ll1,
$$

且兩者各自具有足夠準確度，組合才容易提高表現。

人機混合預測實驗已顯示，經過技能權重、過度自信修正與人機聚合後的系統，可以優於只使用人類預測的基線。這支持「互補誤差」而不是「AI 取代人類」的方向。

---

## 十二、生成數量不是獨立路徑數量

設 AI 生成：

$$
S_1,S_2,\ldots,S_n.
$$

若它們具有不同文字，但共享相同因果圖：

$$
G(S_1)
=
G(S_2)
=
\cdots
=
G(S_n),
$$

則真正的因果新增量接近零。

因此應區分：

$$
N_{\mathrm{text}}
$$

與：

$$
N_{\mathrm{causal}}.
$$

因果去重可以依據：

- 共同前提；
- 共同瓶頸；
- 共同主要行動者；
- 共同轉移條件；
- 共同失敗機制；
- 共同終局狀態。

本文提出因果等價關係：

$$
S_i\sim_C S_j
$$

若兩者在指定粒度下共享相同的核心因果圖。

真正覆蓋數為：

$$
N_{\mathrm{causal}}
=
\left|
\mathcal S/
\sim_C
\right|.
$$

---

## 十三、模型多樣性比重複抽樣更重要

從同一模型、相同提示與相同資料來源反覆抽樣，容易得到高度相關的預測：

$$
\operatorname{Corr}
(\widehat p_i,\widehat p_j)
\uparrow.
$$

近期 AI 預測研究顯示，前沿模型之間的預測可能高度相關；最有效的集成不是無限制增加樣本，而是組合準確但誤差互補的模型。

因此，預測平台應優先增加：

- 不同模型家族；
- 不同訓練來源；
- 不同搜尋策略；
- 不同文化和制度先驗；
- 不同因果建模方法；
- 對抗性代理；
- 人類專家與市場概率。

可定義有效預測者數：

$$
N_{\mathrm{forecaster}}^{\mathrm{eff}}
=
\exp
\left(
H(\mathbf w)
\right)
\cdot
\left(
1-\bar\rho
\right),
$$

其中 $\mathbf w$ 是預測者權重， $\bar\rho$ 是平均誤差相關性。此式是概念性指標，用於提醒「數量」與「獨立性」必須共同考慮。

---

## 十四、AI 預測能力正在提升，但並未消除人類優勢

ForecastBench 以答案尚未出現的未來事件建立持續更新評測，降低資料污染風險。早期結果顯示，人類專業預測者仍優於當時最佳 LLM。

後續研究則顯示：

- 檢索增強、問題分解與預測聚合可以顯著改善 LLM；
- 前沿模型可在部分真實預測任務超過一般人群；
- 專業超級預測者在多項比較中仍保持優勢；
- 代理式搜尋、模型集成和統計校準可使 AI 系統接近超級預測者；
- 人機混合系統可優於純人類基線。

因此：

$$
\boxed{
\text{預測能力的提升主要來自完整系統，}
\quad
\text{而不是裸模型的單次回答。}
}
$$

---

## 十五、預測必須在結果未知時固定

若研究者在事件發生後重新閱讀大量舊論文，很容易產生：

- 選擇性記憶；
- 模糊命中；
- 結果族過度寬鬆；
- 忽略未命中預測；
- 重新解釋時間窗。

所以預測項目應事先固定：

$$
Q
=
\left(
q,t_{\mathrm{close}},t_{\mathrm{resolve}},
\mathcal R,p,E
\right),
$$

其中：

- $q$ ：可判定問題；
- $t_{\mathrm{close}}$ ：停止更新時間；
- $t_{\mathrm{resolve}}$ ：結果判定時間；
- $\mathcal R$ ：明確結果規則；
- $p$ ：提交機率；
- $E$ ：當時可用證據。

沒有這些欄位，文本更接近情境研究，而不是可評分預測。

---

## 十六、Brier 分數與校準

對二元事件，預測概率為 $p_i$ ，結果為：

$$
o_i\in\{0,1\}.
$$

Brier 分數為：

$$
BS
=
\frac1N
\sum_{i=1}^{N}
(p_i-o_i)^2.
$$

分數越低越好。

但單一平均分還應分解為：

- 可靠度；
- 解析度；
- 不確定性。

校準要求：

$$
P
\left(
o=1\mid p\approx0.7
\right)
\approx0.7.
$$

如果所有被賦予 $70\%$ 的事件，長期只有 $40\%$ 發生，系統便過度自信。

因此真正的問題不是：

> 我有沒有提到它？

而是：

$$
\boxed{
\text{我給高概率的事件是否真的更常發生？}
}
$$

---

## 十七、覆蓋引擎與概率引擎應分離

一個系統若同時負責提出路徑和為自己評分，容易壓制陌生方案或過度信任自身生成。

本文提出四引擎結構。

### 17.1 覆蓋引擎

目標：

$$
\max
N_{\mathrm{causal}}.
$$

鼓勵提出因果上不同的路徑。

### 17.2 裁剪引擎

目標：

$$
\min
\left(
\text{重複}
+
\text{不可行}
+
\text{無機制敘事}
\right).
$$

### 17.3 概率引擎

依據：

- 基準率；
- 當前證據；
- 行動者激勵；
- 市場或群體概率；
- 類似歷史案例；
- 時間依賴；

配置概率。

### 17.4 反證引擎

專門尋找：

- 共同盲點；
- 缺失變量；
- 反身效應；
- 黑天鵝機制；
- 來源相依性。

---

## 十八、論文庫如何轉成預測系統？

大量論文不是自動等於預測平台。

首先需要把論文中的命題抽取為：

$$
v_i
=
\left(
\text{狀態},
\text{門檻},
\text{事件},
\text{證據}
\right).
$$

再把條件關係轉成：

$$
e_{ij}
:
v_i
\rightarrow
v_j.
$$

形成動態圖：

$$
\mathcal G_t
=
\left(
V_t,E_t,P_t,Z_t
\right),
$$

其中：

- $V_t$ ：狀態、事件與瓶頸；
- $E_t$ ：因果與條件轉移；
- $P_t$ ：概率；
- $Z_t$ ：支持、反對與未知證據。

每篇論文可以貢獻：

- 節點；
- 邊；
- 假說；
- 先驗；
- 反例；
- 判定指標。

平台的核心不是文章數量，而是命題能否被版本化、連結和回測。

---

## 十九、路徑圖的概率更新

設一條路徑為：

$$
\pi_i:
v_0\rightarrow v_1\rightarrow\cdots\rightarrow v_k.
$$

在簡化條件獨立假設下：

$$
P(\pi_i)
=
\prod_{j=0}^{k-1}
P(v_{j+1}\mid v_j).
$$

但真實系統常存在：

- 共同原因；
- 回饋；
- 路徑依賴；
- 策略互動；
- 非獨立事件。

所以更合適的是使用：

- 貝葉斯網路；
- 動態貝葉斯網路；
- 因果圖；
- 馬可夫決策模型；
- 代理模擬；
- 情境樹與狀態流模型。

新證據 $D_{t+1}$ 到來時：

$$
P_{t+1}(\pi_i)
\propto
P(D_{t+1}\mid\pi_i)
P_t(\pi_i).
$$

所有更新都必須保留時間戳與舊版本，避免事後重寫。

---

## 二十、關鍵節點與相變區間

某些節點的出現會顯著重排後續分支概率。

設門檻變量為：

$$
z(t).
$$

若：

$$
z(t)<\theta
$$

時，系統處於狀態 $\mathcal A$ ；

而：

$$
z(t)\geq\theta
$$

後，可達空間變為：

$$
\mathcal B
\supsetneq
\mathcal A.
$$

則 $\theta$ 是能力或制度相變門檻。

預測平台不應只預測最終事件，也應追蹤：

- 門檻變量；
- 前置信號；
- 轉移速度；
- 是否可逆；
- 哪些分支在跨越後消失；
- 哪些新分支首次出現。

這正是「關鍵區間」比任意時間點更值得密集分析的原因。

---

## 二十一、預測預算與邊際遞減

設搜尋、模型、代理與推理預算為：

$$
B.
$$

路徑覆蓋率為：

$$
C_{\mathrm{path}}(B).
$$

通常初期：

$$
\frac{\partial C_{\mathrm{path}}}{\partial B}>0.
$$

但後期可能：

$$
\frac{\partial^2 C_{\mathrm{path}}}{\partial B^2}<0.
$$

原因是新增生成逐漸變成：

- 同義改寫；
- 同一因果機制細分；
- 相同資料來源的重述；
- 低價值尾部分支。

提高上限更依賴：

$$
\text{模型異質性}
+
\text{資料異質性}
+
\text{方法異質性}
+
\text{回測}.
$$

所以「尚未把額度開到最高」確實可能表示還有覆蓋增益，但不表示算力增加會線性接近完整預測。

---

## 二十二、四類難以覆蓋的未來

### 22.1 模型語言外的新機制

若新事件需要現有理論中沒有的概念或因果算子，系統可能無法生成。

### 22.2 極低機率高衝擊事件

可以被列入風險集合，卻很難正確給予機率。

### 22.3 反身性事件

預測被公開後會改變行動者：

$$
\widehat F
\rightarrow
a
\rightarrow
F'.
$$

預測可能自我實現，也可能自我否定。

### 22.4 精確時間與事件順序

即使結構方向正確：

$$
A,B,C
$$

仍可能錯判：

$$
A\rightarrow B\rightarrow C
$$

或：

$$
B\rightarrow A\rightarrow C.
$$

時間預測通常比方向覆蓋更困難。

---

## 二十三、低有效分支的失敗條件

此命題不適用或容易失效於：

1. 時間尺度極長；
2. 新物理或新通用技術出現；
3. 行動者數量巨大且高度反身；
4. 制度處於崩解或革命狀態；
5. 判定粒度過細；
6. 概率分布極為平坦；
7. 存在大量不可觀察狀態；
8. 模型與現實互相強烈作用。

因此，任何使用低有效分支命題的研究都必須公開：

$$
\left(
\text{時間窗},
\text{粒度},
\text{約束},
\text{機率門檻},
\text{失效條件}
\right).
$$

---

## 二十四、主要反對意見

### 24.1 反對一：這只是把很多可能合併成少數類別

部分正確。粗粒化本來就是壓縮。問題在於壓縮是否保存決策需要的因果差異，而不是是否完全無損。

### 24.2 反對二：只要把結果族定義得夠寬，任何預測都能命中

因此結果族必須在結果未知前固定，並設定可區分的因果條件與時間範圍。

### 24.3 反對三：AI 生成越多，總能聲稱命中

本文正因如此要求概率、去重、未命中紀錄和 proper scoring rules，而不是以「曾提及」作為成功標準。

### 24.4 反對四：有效分支數是虛假的精確化

$N_{\mathrm{eff}}$ 只在機率與結果分區合理時有意義。它不應被視為世界真實分支的客觀總數，而是指定模型下的不確定性摘要。

### 24.5 反對五：歷史類比會忽略真正的新事物

因此平台必須保留外部機制、異端路徑與模型失效類別，不能只從既有論文庫內閉合生成。

### 24.6 反對六：人機系統可能放大同一偏見

若人類與 AI 共享資料來源與框架，確實會如此。真正增益取決於獨立誤差和對抗性設計。

### 24.7 反對七：世界具有自由意志，所以不能預測

非決定性、自由選擇與概率預測並不矛盾。本文預測的是結果分布和因果條件，不是宣稱每一主體的行動已被唯一決定。

---

## 二十五、核心命題

### 命題一：空間分層命題

$$
\mathcal D_t
\subseteq
\mathcal P_t
\subseteq
\mathcal F_t
\subseteq
\Omega_t^L
\subseteq
\Omega_t.
$$

### 命題二：宏觀壓縮命題

大量微觀路徑可以匯入少數宏觀結果族。

### 命題三：低有效分支命題

在特定關鍵時間、約束和粒度下，主要機率質量可能集中於少數有效分支。

### 命題四：敘述—因果分離命題

$$
N_{\mathrm{text}}
\not\Rightarrow
N_{\mathrm{causal}}.
$$

### 命題五：覆蓋—準確分離命題

$$
\operatorname{Mentioned}(E)>0
\not\Rightarrow
\operatorname{CalibratedForecast}(E)>0.
$$

### 命題六：人機互補命題

人機組合只有在誤差互補、概率校準與獨立來源存在時，才可能超越單方。

### 命題七：多樣性優於重複命題

在固定預算下，準確但誤差互補的模型組合，通常比同一模型的重複抽樣更有價值。

### 命題八：平台圖結構命題

成熟預測平台應管理命題、因果邊、概率、證據與結果，而不只保存文章。

### 命題九：預算邊際遞減命題

單純增加生成和搜尋預算，對獨立路徑覆蓋的增益通常逐漸下降。

### 命題十：完全預測否定命題

低有效分支不表示世界可被完整、確定且永久預測。

---

## 二十六、結論

世界的全部微觀可能性可以極其龐大，但決策者真正面對的並不是「所有能想像的故事」。

他們面對的是：

$$
\text{在特定時間窗內}
+
\text{滿足現實約束}
+
\text{承載顯著概率}
+
\text{具有決策影響}
$$

的路徑族。

在適當粒度下，這些路徑族可能沒有想像中那麼多。

因此：

$$
\boxed{
\text{世界不是簡單，}
\quad
\text{但它的高機率宏觀出口可能相對有限。}
}
$$

AI 的重要作用，不是暴力列舉無限細節，而是降低下列工作的成本：

- 搜尋資料；
- 生成異質假說；
- 展開因果鏈；
- 尋找瓶頸；
- 產生反例；
- 比較路徑；
- 持續更新。

人類研究者則提供問題邊界、理論先驗、相變辨識、價值判定與模型失效意識。

兩者結合，可以形成：

$$
\boxed{
\text{高通量生成}
+
\text{因果壓縮}
+
\text{概率校準}
+
\text{持續回測}.
}
$$

但若缺少去重和評分，大量 AI 產出只會形成「什麼都說過」的覆蓋幻覺。

真正有意義的預測能力，不是事後找到一篇曾經提及結果的文章，而是：

$$
\boxed{
\text{在答案未知時，}
\quad
\text{辨識主要因果分支，}
\quad
\text{配置可校準概率，}
\quad
\text{並讓決策能跨多個未來保持穩健。}
}
$$

所以本文最終主張：

$$
\boxed{
|\Omega|\gg1
\not\Rightarrow
N_{\mathrm{eff}}\gg1.
}
$$

以及：

$$
\boxed{
\text{未來未必可以被窮盡，}
\quad
\text{但某些關鍵區間的主要路徑，}
\quad
\text{可能可以被高度覆蓋。}
}
$$

---

## 參考文獻

1. Karger, Ezra, et al. “ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities.” arXiv:2409.19839, 2024; ICLR, 2025.
2. Halawi, Danny, Fred Zhang, Chen Yueh-Han, and Jacob Steinhardt. “Approaching Human-Level Forecasting with Language Models.” arXiv:2402.18563, 2024.
3. Benjamin, Daniel M., et al. “Hybrid Forecasting of Geopolitical Events.” arXiv:2412.10981, 2024.
4. Lu, Janna. “Evaluating LLMs on Real-World Forecasting Against Human Superforecasters.” arXiv:2507.04562, 2025.
5. Alur, Rohan, et al. “AIA Forecaster: Technical Report.” arXiv:2511.07678, 2025.
6. Aitchison, Matthew, Scott Jeen, Toby Shevlane, and Ben Day. “Diversity Is the Strength of the AI Crowd.” arXiv:2606.29661, 2026.
7. Ali, Junade. “Quantifying Diversity of Thought: A Predictive Law of Weighted LLM Ensemble Lift.” arXiv:2607.17384, 2026.
8. Bosse, Nikos I., et al. “Automating Forecasting Question Generation and Resolution for AI Evaluation.” arXiv:2601.22444, 2026.
9. Schöller, Peter, et al. “Prompt Engineering Large Language Models’ Forecasting Capabilities.” arXiv:2506.01578, 2025.
10. “Pitfalls in Evaluating Language Model Forecasters.” arXiv:2506.00723, 2025.
11. Brier, Glenn W. “Verification of Forecasts Expressed in Terms of Probability.” *Monthly Weather Review* 78, no. 1, 1950, pp. 1–3.
12. Gneiting, Tilmann, and Adrian E. Raftery. “Strictly Proper Scoring Rules, Prediction, and Estimation.” *Journal of the American Statistical Association* 102, no. 477, 2007, pp. 359–378.
13. Bröcker, Jochen. “Reliability, Sufficiency, and the Decomposition of Proper Scores.” arXiv:0806.0813, 2008.
14. Tetlock, Philip E., and Dan Gardner. *Superforecasting: The Art and Science of Prediction*. Crown, 2015.
15. Mellers, Barbara, et al. “Psychological Strategies for Winning a Geopolitical Forecasting Tournament.” *Psychological Science* 25, no. 5, 2014, pp. 1106–1115.
16. Hill, Mark O. “Diversity and Evenness: A Unifying Notation and Its Consequences.” *Ecology* 54, no. 2, 1973, pp. 427–432.
17. Jost, Lou. “Entropy and Diversity.” *Oikos* 113, no. 2, 2006, pp. 363–375.
18. Shannon, Claude E. “A Mathematical Theory of Communication.” *Bell System Technical Journal* 27, 1948.
19. Pearl, Judea. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
20. Spirtes, Peter, Clark Glymour, and Richard Scheines. *Causation, Prediction, and Search*. MIT Press, 2000.
21. Schoemaker, Paul J. H. “Scenario Planning: A Tool for Strategic Thinking.” *Sloan Management Review* 36, no. 2, 1995.
22. Cordova-Pozo, Katherine, and Edgar Rouwette. “Types of Scenario Planning and Their Effectiveness: A Review of Reviews.” *Futures* 149, 2023.
23. Taleb, Nassim Nicholas. *The Black Swan*. Random House, 2007.
24. Goodhart, Charles. “Problems of Monetary Management: The U.K. Experience.” In *Papers in Monetary Economics*, 1975.
25. de Finetti, Bruno. *Theory of Probability*. Wiley, 1974.
26. Savage, Leonard J. *The Foundations of Statistics*. Wiley, 1954.

---

## 理論定位

本文提出的「關鍵區間低有效分支命題」「因果路徑覆蓋」「有效預測者數」與平台架構，屬於跨概率預測、情境規劃、資訊論、因果建模與 AI 代理研究的理論構造。

本文不主張：

- 世界具有固定且可被完整讀取的唯一未來；
- 低有效分支在所有時間尺度和領域成立；
- 大量生成自動提高預測準確率；
- 曾經提及一種結果即可視為預測成功；
- AI 已取代專業預測者；
- 個人論文庫本身就是經過校準的預測資料庫。

其用途是建立一套可以被回測、反駁與工程化的語言，用以判斷何時「可能性看似龐大，但真正高概率的因果出口相對有限」。
