---
title: "移動中的可知邊界：人機協作、智能反身性與 AI 原生知識生產"
title_en: "The Moving Frontier of Knowability: Human–AI Collaboration, Intelligent Reflexivity, and AI-Native Knowledge Production"
version: "v0.1"
date: "2026-07-19"
document_type: "統合理論、概念性與方法論論文"
status: "公開發表草案"
language: "zh-Hant"
authors:
  - "Neo.K"
  - "Aletheia（GPT-5.6 Thinking）"
keywords:
  - "可知邊界"
  - "人機協作"
  - "條件可判斷性"
  - "智能反身性"
  - "AI 原生研究"
  - "持續研究狀態"
  - "延遲發現"
  - "驗證瓶頸"
  - "知識生產"
  - "非拉普拉斯式預測"
---

# 移動中的可知邊界

## 人機協作、智能反身性與 AI 原生知識生產

### The Moving Frontier of Knowability: Human–AI Collaboration, Intelligent Reflexivity, and AI-Native Knowledge Production

**作者：** Neo.K、Aletheia（GPT-5.6 Thinking）  
**文件性質：** 統合理論、概念性與方法論論文  
**版本：** v0.1  
**日期：** 2026-07-19  

---

# 摘要

人工智能同時改變人類能夠知道什麼、如何形成知識，以及未知如何被生成。現有研究通常分別討論 AI 輔助預測、AI 科學發現、研究自動化、反身性風險、開放科學與知識保存，卻較少把它們視為同一知識動力系統的不同環節。本文提出「移動中的可知邊界」框架，將人機協作下的知識生產描述為一個雙向、非單調且具有時間記憶的過程。

本文將知識空間區分為五種狀態：已驗證知識、條件可判斷內容、待驗證候選、已保存但尚未辨認的潛伏痕跡，以及尚未結構化的未知。人機協作可透過搜尋、推理、情境分解與反例生成，使部分未知進入條件可判斷區，並經驗證進入知識區；然而，智能行動者也會因預測而改變行為、針對模型進行策略適應，並透過創新擴張未來狀態空間。故即使知識的絕對量持續增加，已知與可判斷內容占全部可能狀態空間的相對比例仍可能停滯或下降。

本文進一步整合兩項基礎設施機制。第一，AI 原生研究需要將研究外部化為持續狀態、發現譜系與多層視圖，以降低跨人類、跨模型及跨時間的承接損失。第二，當生成速度高於辨認與驗證速度時，歷史機器輸出會形成認識積欠；合成知識考古可從中重建並驗證延遲發現。由此，知識生產不只沿時間向前生成，也可能沿研究譜系向後回收。

本文提出一個統一動力模型：

\[
\Delta\Xi_t
=
G_{\mathrm{obs}}
+
G_{\mathrm{inf}}
+
G_{\mathrm{coord}}
+
G_{\mathrm{ret}}
+
G_{\mathrm{rec}}
-
C_{\mathrm{ref}}
-
C_{\mathrm{str}}
-
C_{\mathrm{nov}}
-
C_{\mathrm{drift}}
-
C_{\mathrm{backlog}},
\]

其中正項代表觀測、推理、協調、保存與回收所帶來的可知性增益，負項代表反身性、策略適應、新穎性、結構漂移及驗證積欠所造成的可知性成本。此式不是跨領域固定常數，而是研究分解框架。本文提出九項可檢驗命題，以及一個包含被動、反應、策略與生成環境的長期實驗方案，測量人類、AI、自由協作與協議化協作在預測、研究承接、錯誤定位及知識考古上的表現。

本文不主張人機協作必然優於人類或 AI 單獨工作，也不主張 AI 會通往類拉普拉斯式全知。較合理的結論是：智能提高了將混亂轉為條件可判斷結構的能力，同時提高了系統生成新策略、新制度與新可能性的能力。未來知識制度的核心任務因此不是消除未知，而是持續管理可知邊界的移動：辨認哪些未知已可結構化、哪些知識正因環境改變而失效、哪些研究狀態必須保存，以及哪些被埋藏的合成痕跡值得重新驗證。

**關鍵詞：** 可知邊界、人機協作、條件可判斷性、智能反身性、AI 原生研究、持續研究狀態、延遲發現、驗證瓶頸、知識生產、非拉普拉斯式預測

---

# Abstract

Artificial intelligence is simultaneously changing what humans can know, how knowledge is produced, and how new forms of uncertainty arise. Existing research often treats AI-assisted forecasting, AI-driven discovery, autonomous research, reflexive risk, open science, and knowledge preservation as separate topics. This paper proposes the **moving frontier of knowability** framework, integrating them as components of a single epistemic dynamical system.

We partition the epistemic space into five states: validated knowledge, conditionally judgeable content, unverified candidates, preserved but unrecognized latent traces, and unstructured unknowns. Human–AI collaboration can move parts of the unknown into the conditionally judgeable region through search, reasoning, scenario decomposition, and counterexample generation, after which validation may convert them into knowledge. Intelligent agents, however, also respond to forecasts, adapt strategically to models, and expand the future state space through innovation. Consequently, the absolute quantity of knowledge may increase while the relative share of known and judgeable states within the expanding possibility space stagnates or declines.

The framework integrates two infrastructural mechanisms. First, AI-native research requires externalized persistent states, discovery lineages, and layered views to reduce transfer loss across humans, models, and time. Second, when generation outpaces recognition and validation, historical machine output forms an epistemic backlog. Synthetic knowledge archaeology may recover and validate delayed discoveries from this backlog. Knowledge production thus proceeds not only forward through new generation, but backward through lineage-based recovery.

We propose the following decomposition:

\[
\Delta\Xi_t
=
G_{\mathrm{obs}}
+
G_{\mathrm{inf}}
+
G_{\mathrm{coord}}
+
G_{\mathrm{ret}}
+
G_{\mathrm{rec}}
-
C_{\mathrm{ref}}
-
C_{\mathrm{str}}
-
C_{\mathrm{nov}}
-
C_{\mathrm{drift}}
-
C_{\mathrm{backlog}},
\]

where the positive terms represent gains from observation, inference, coordination, retention, and recovery, while the negative terms represent costs from reflexivity, strategic adaptation, novelty, structural drift, and verification backlog. This is not proposed as an invariant natural law but as a research decomposition. We derive nine testable propositions and outline a longitudinal research program across passive, reactive, strategic, and generative environments, comparing human-only, AI-only, free human–AI collaboration, and protocolized human–AI collaboration.

We do not claim that human–AI collaboration necessarily outperforms humans or AI alone, nor that AI leads toward Laplacian omniscience. A more defensible conclusion is that intelligence increases the capacity to transform disorder into conditionally judgeable structure while also increasing the capacity to generate new strategies, institutions, and possibilities. The central task of future knowledge institutions is therefore not to eliminate the unknown, but to manage the movement of the knowability frontier: identifying which unknowns have become structureable, which knowledge is being invalidated by environmental change, which research states must be preserved, and which buried synthetic traces warrant renewed validation.

**Keywords:** knowability frontier; human–AI collaboration; conditional judgeability; intelligent reflexivity; AI-native research; persistent research state; delayed discovery; verification bottleneck; knowledge production; non-Laplacian forecasting

---

# 1. 導論

## 1.1 智能提高之後，世界究竟更可知還是更不可知？

人工智能進步引發兩種相反敘事。

第一種敘事認為：

\[
\text{更多資料}
+
\text{更強推理}
+
\text{更高算力}
\rightarrow
\text{更少未知}.
\]

依此觀點，AI 能讀取人類難以處理的大量文獻，搜尋廣大組合空間，形成更精確的預測，甚至解決前沿科學問題。人機協作將使過去高度混亂、只能依賴直覺的領域逐步變得可分析。

第二種敘事則認為，智能會加速：

- 策略競爭；
- 反模型行為；
- 技術創新；
- 制度變化；
- 多代理者互動；
- 內容與假說生成。

因此，AI 可能不只減少不確定性，也使世界演化速度更快、狀態空間更大、反身性更強。

兩種敘事並不互相排斥。

它們可能描述同一動力系統的兩個方向：

\[
\boxed{
\text{智能提高認識世界的能力，}
\newline
\text{也提高改變世界與創造新世界狀態的能力。}
}
\]

---

## 1.2 四項彼此連動的轉型

本文統合四項轉型。

### 轉型一：從不可知到條件可判斷

人機協作不必完全預測未來，仍可將模糊未知轉為：

- 明確條件；
- 可比較情境；
- 時間範圍；
- 可信度；
- 失效條件；
- 更新規則。

### 轉型二：智能化的不確定性反向生成

預測與模型會進入系統，行動者會學習與適應，創新會增加新選項，使可預測性不再單調上升。

### 轉型三：研究由文件轉為持續狀態

當 AI 可以持續生成、驗證、分支與重啟研究，單篇論文不足以保存完整研究連續性。

### 轉型四：知識由即時發現擴張至延遲發現

當生成速度高於驗證速度，舊輸出可能在後來才被辨認為有效候選。研究因而同時向前生成與向後考古。

---

## 1.3 當代案例所揭示的結構變化

2026 年公開的研究案例已顯示，AI 正從單步輔助進入完整研究流程。The AI Scientist 串接構想生成、文獻搜尋、程式撰寫、實驗、分析、論文撰寫與自動審閱；Robin 則將文獻驅動的假說生成、人工實驗與自動資料分析連成反覆更新的生物研究循環（Lu et al., 2026；Ghareeb et al., 2026）。

在數學領域，First Proof 測試顯示，模型可以產生研究級、端到端的證明嘗試，但正確性仍高度依賴專家持續審查；其中一項原先被判為可能正確的嘗試後來被確認為錯誤。另一方面，一個通用推理模型對平面單位距離問題中的長期核心猜想提出反例構造，其證明經外部數學家檢查，展示 AI 不只整理既有知識，也可能產生具前沿新穎性的研究結果（OpenAI, 2026a, 2026b）。

這些案例不能證明所有領域將被自動研究。

它們足以顯示三件事：

1. 研究候選生成的速度正在上升；
2. 研究流程正變得可持續與可代理化；
3. 驗證、承接及知識治理的重要性同步上升。

---

## 1.4 本文的研究問題

本文回答：

1. 如何統一描述智能造成的可知性增益與不確定性成本？
2. 知識的絕對增長是否可能與相對可知性下降並存？
3. 人機協作在何種條件下真正擴張可知邊界？
4. 反身性、策略性與新穎性如何使邊界反向移動？
5. 持續研究狀態如何降低知識承接損失？
6. 合成知識考古如何將過去痕跡轉回知識候選？
7. 如何實證檢驗整個動力系統，而非只檢查單次模型準確率？

---

## 1.5 本文的基本立場

本文不採取：

\[
\text{AI 樂觀決定論}
\]

也不採取：

\[
\text{AI 不可知論}.
\]

本文主張：

\[
\boxed{
\text{可知性不是固定容量，}
\newline
\text{而是由認識能力、環境反應、研究記憶與驗證制度共同決定的移動邊界。}
}
\]

---

# 2. 何謂可知邊界？

## 2.1 可知不等於已知

已知是已被建立、驗證或制度性接受的內容。

可知則涉及：

- 是否能形成問題；
- 是否能取得證據；
- 是否能提出可檢驗模型；
- 是否能估計條件與不確定性；
- 是否存在可行驗證路徑；
- 是否能保存與傳遞結果。

因此：

\[
\text{Known}
\subset
\text{Knowable}.
\]

---

## 2.2 條件可判斷性

某個未來事件即使不能被完全預測，仍可能被轉為：

\[
J
=
\langle
\Omega,
P,
C,
T,
F,
U
\rangle,
\]

其中：

- \(\Omega\)：有限情境集合；
- \(P\)：條件機率或排序；
- \(C\)：成立條件；
- \(T\)：時間窗；
- \(F\)：可否證條件；
- \(U\)：更新規則。

本文稱這種狀態為條件可判斷。

---

## 2.3 可知邊界

設世界可能狀態空間為：

\[
\Omega_t.
\]

時間 \(t\) 已被驗證或可條件判斷的區域為：

\[
\mathcal X_t
=
K_t\cup J_t.
\]

則可知邊界可表示為：

\[
\partial\mathcal X_t
\subseteq
\Omega_t.
\]

它不是一條精確幾何曲線，而是已知／可判斷與尚未結構化未知之間的概念邊界。

---

## 2.4 邊界為何會移動？

可知邊界受下列因素影響：

- 新觀測；
- 新理論；
- 新計算；
- 新工具；
- 新協作方式；
- 新驗證方法；
- 制度改變；
- 行動者回應；
- 狀態空間擴張；
- 知識遺失；
- 舊資料重新發現。

---

# 3. 五態知識空間

## 3.1 已驗證知識 \(K_t\)

包含依相應領域標準獲得支持的：

- 定理；
- 實驗結果；
- 可重現演算法；
- 穩健統計關係；
- 受支持機制；
- 明確反例。

知識並非永不修正。

其狀態可以是：

- active；
- qualified；
- contested；
- superseded；
- refuted。

---

## 3.2 條件可判斷區 \(J_t\)

尚未成為確定知識，但已被結構化為：

- 有限情境；
- 可更新概率；
- 明確條件；
- 可否證判準；
- 可追蹤指標。

它是本文理解預測進步的關鍵區域。

---

## 3.3 候選區 \(C_t\)

包含：

- 未驗證猜想；
- 證明草稿；
- 實驗假說；
- 程式候選；
- 初步因果模型；
- 研究方向；
- 反例候選。

候選可以大量生成，但不能自動視為知識。

---

## 3.4 潛伏痕跡區 \(L_t\)

包含已被記錄、但尚未被辨認為明確候選的：

- 舊模型輸出；
- 失敗證明片段；
- 低分程式；
- 未分析資料；
- 未完成實驗；
- 被捨棄分支；
- 對話中的局部洞見。

---

## 3.5 尚未結構化未知 \(U_t\)

包含：

- 尚未形成的問題；
- 尚不存在的技術；
- 尚未定義的狀態；
- 不知道自己不知道的關係；
- 目前無法觀測的機制；
- 尚未產生的策略。

---

## 3.6 五態轉換

\[
U
\rightarrow
J
\rightarrow
K
\]

代表由未知到條件可判斷，再到驗證知識。

\[
U
\rightarrow
C
\rightarrow
K
\]

代表由生成候選直接進入驗證。

\[
C
\rightarrow
L
\rightarrow
C
\rightarrow
K
\]

代表候選被埋藏後，經考古重新進入驗證。

\[
K
\rightarrow
J
\quad\text{或}\quad
K\rightarrow C
\]

則表示舊知識因新證據或制度變化而被降級。

---

# 4. 統一動力模型

## 4.1 可知性增益

定義五種主要增益。

### 觀測增益

\[
G_{\mathrm{obs}}
\]

來自新資料、感測器、資料庫與實驗。

### 推理增益

\[
G_{\mathrm{inf}}
\]

來自模型、形式化、搜尋、計算與跨領域連結。

### 協調增益

\[
G_{\mathrm{coord}}
\]

來自人類與 AI 在問題分解、互相校正及資源配置上的互補。

### 保存增益

\[
G_{\mathrm{ret}}
\]

來自研究狀態、譜系、版本、來源與失敗記錄的保存。

### 回收增益

\[
G_{\mathrm{rec}}
\]

來自合成知識考古、重現、重新解讀與舊資料驗證。

---

## 4.2 可知性成本

### 反身性成本

\[
C_{\mathrm{ref}}
\]

預測與模型改變被預測對象。

### 策略成本

\[
C_{\mathrm{str}}
\]

行動者推斷、操縱或反制模型。

### 新穎性成本

\[
C_{\mathrm{nov}}
\]

創新產生原模型外的新選項。

### 結構漂移成本

\[
C_{\mathrm{drift}}
\]

制度、參數與因果機制隨時間改變。

### 驗證積欠成本

\[
C_{\mathrm{backlog}}
\]

候選數量超過驗證能力，使真正有價值內容被噪音淹沒。

---

## 4.3 淨可知性變化

\[
\Delta\Xi_t
=
G_{\mathrm{obs}}
+
G_{\mathrm{inf}}
+
G_{\mathrm{coord}}
+
G_{\mathrm{ret}}
+
G_{\mathrm{rec}}
-
C_{\mathrm{ref}}
-
C_{\mathrm{str}}
-
C_{\mathrm{nov}}
-
C_{\mathrm{drift}}
-
C_{\mathrm{backlog}}.
\]

此式不是假設所有項目可被同一單位精確加總。

它提供研究拆分：

> 一項 AI 系統究竟提高了哪種可知性，又增加了哪種未知？

---

## 4.4 向量表示

更嚴格地說，可知性應表示為：

\[
\boldsymbol{\Xi}_t
=
\langle
\Xi_{\mathrm{accuracy}},
\Xi_{\mathrm{calibration}},
\Xi_{\mathrm{coverage}},
\Xi_{\mathrm{traceability}},
\Xi_{\mathrm{transfer}},
\Xi_{\mathrm{verifiability}}
\rangle.
\]

一個系統可能：

- 提高準確度；
- 降低可追溯性；
- 增加情境涵蓋；
- 卻提高驗證成本。

不存在單一分數能完整取代多構面評估。

---

# 5. 絕對知識增長與相對可知性下降

## 5.1 狀態空間擴張

傳統模型假設：

\[
\Omega_{t+1}=\Omega_t.
\]

生成環境中則可能有：

\[
\Omega_{t+1}
=
\Omega_t
\cup
N_t,
\]

其中 \(N_t\) 是新技術、新策略、新制度與新問題形成的狀態。

---

## 5.2 絕對可知量

\[
A_t
=
\mu(K_t\cup J_t).
\]

若人機協作有效，可能有：

\[
A_{t+1}>A_t.
\]

---

## 5.3 相對可知率

\[
\kappa_t
=
\frac{
\mu(K_t\cup J_t)
}{
\mu(\Omega_t)
}.
\]

即使：

\[
A_{t+1}>A_t,
\]

仍可能有：

\[
\kappa_{t+1}<\kappa_t
\]

只要狀態空間擴張速度更快。

---

## 5.4 可知性擴張悖論

### 定義 1：可知性擴張悖論

當一個文明的已知與可判斷內容持續增加，但其技術、策略與概念創新使可能狀態空間擴張得更快，導致相對可知率下降，稱為可知性擴張悖論。

這不是知識失敗。

它表示：

\[
\boxed{
\text{知道得更多，}
\newline
\text{同時更清楚尚有更多東西不知道。}
}
\]

---

# 6. 人機協作：從混亂到條件可判斷

## 6.1 人類與 AI 的非對稱能力

人類常具優勢於：

- 問題重要性；
- 價值判斷；
- 語境；
- 異常感；
- 責任；
- 長期目的；
- 默會知識。

AI 常具優勢於：

- 大量搜尋；
- 快速比較；
- 形式變換；
- 候選生成；
- 程式執行；
- 記憶檢索；
- 重複驗證；
- 多情境展開。

協作的潛在價值來自能力差異，而不是單純把兩個答案平均。

---

## 6.2 協作不必然產生綜效

一項涵蓋 106 個實驗及 370 個效果量的統合分析顯示，人機組合平均優於人類單獨工作，卻平均不優於人類或 AI 中表現較佳的一方；任務類型與雙方相對能力會顯著調節結果（Vaccaro et al., 2024）。

因此：

\[
\text{Human}+\text{AI}
\not\Rightarrow
\text{Synergy}.
\]

協作需要：

- 正確分工；
- 錯誤多樣性；
- 信心校準；
- 衝突處理；
- 獨立推理；
- 可追蹤更新。

---

## 6.3 自由協作與協議化協作

### 自由協作

人類與 AI 自然對話，沒有固定檢查程序。

### 協議化協作

要求：

1. 先獨立判斷；
2. 分別列出基準率；
3. 明確列出假設；
4. 提出反例；
5. 比較歧見；
6. 記錄更新；
7. 保留失效條件。

本文預測協議化協作在高複雜預測與研究承接中，通常比自由協作更穩健，但不必在所有任務中更快。

---

## 6.4 未來空間壓縮

設人類原先考慮的可能空間為：

\[
\Omega_t^H.
\]

有效人機協作後為：

\[
\Omega_t^{H+AI}.
\]

若：

\[
\Omega_t^{H+AI}
\subset
\Omega_t^H,
\]

且真實結果仍被適當涵蓋，則發生有效未來空間壓縮。

壓縮不能只追求少列幾個情境。

必須同時維持：

- 涵蓋率；
- 校準；
- 可否證性；
- 更新能力；
- 結構多樣性。

---

# 7. 智能反身性：邊界為何反向移動？

## 7.1 內生預測者

在智能社會中：

\[
x_{t+1}
=
F_t
\left(
x_t,
\hat{x}_{t+1},
a_t
\right).
\]

預測：

\[
\hat{x}_{t+1}
\]

會影響行動：

\[
a_t,
\]

行動再改變結果。

預測者不在系統外。

---

## 7.2 Lucas critique 的一般化含義

若政策、模型或評分規則改變行動者預期，歷史估計參數未必保持不變。

\[
\beta_{t+1}\neq\beta_t.
\]

此洞見可擴張至：

- 演算法推薦；
- 信用評分；
- 招聘模型；
- 交易策略；
- AI 安全評估；
- 研究資源配置。

---

## 7.3 表現性預測

若模型參數 \(\theta\) 的部署改變資料分布：

\[
Z\sim\mathcal D(\theta),
\]

則模型同時：

- 預測分布；
- 參與生成分布。

---

## 7.4 策略適應

行動者可選擇：

\[
a_i^\ast
=
\arg\max_{a_i}
u_i
\left(
a_i,\theta,\hat a_{-i}
\right).
\]

當 AI 同時強化評估者與被評估者：

\[
I_{\mathrm{forecaster}}\uparrow,
\qquad
I_{\mathrm{agent}}\uparrow,
\]

預測優勢不必持續擴大。

---

## 7.5 創新與模型外狀態

智能行動者不只從既有選項中選擇，也會產生：

\[
A_{t+1}
=
A_t\cup\Delta A_t.
\]

因此，部分預測失敗並不是機率估錯，而是：

\[
Y_{\mathrm{actual}}
\notin
\Omega_t^{\mathrm{model}}.
\]

---

# 8. AI 原生研究：保存可知性的時間結構

## 8.1 研究不再只是論文序列

AI 原生研究具有：

- 高頻迭代；
- 多模型分工；
- 自動重試；
- 分支；
- 合併；
- 持續資料回饋；
- 跨時間重啟。

傳統文件列表難以表示：

- 哪個命題仍有效；
- 哪條分支失敗；
- 哪個方法被替換；
- 哪個模型產生什麼；
- 下一個代理者應從何處開始。

---

## 8.2 持續研究狀態

\[
S_t
=
\langle
Q_t,
C_t,
E_t,
M_t,
F_t,
B_t,
U_t,
P_t
\rangle,
\]

其中：

- \(Q_t\)：問題；
- \(C_t\)：命題；
- \(E_t\)：證據；
- \(M_t\)：方法；
- \(F_t\)：失敗；
- \(B_t\)：分支；
- \(U_t\)：未決事項；
- \(P_t\)：來源與貢獻。

---

## 8.3 研究狀態外部化

若研究只存在模型上下文中：

\[
S_t^{\mathrm{internal}},
\]

模型更換後可能大量遺失。

外部化為：

\[
S_t^{\mathrm{external}}
\]

後，不同代理者可以：

- 重建；
- 批判；
- 分支；
- 驗證；
- 延續。

---

## 8.4 保存增益

設沒有持續狀態時的承接損失為：

\[
\ell_0.
\]

有狀態、譜系與差分時為：

\[
\ell_s.
\]

若：

\[
\ell_s<\ell_0,
\]

則研究基礎設施本身產生可知性增益。

---

## 8.5 論文作為視圖

完整研究狀態可生成：

\[
V
=
\Phi
\left(
S_t;
\text{audience},
\text{purpose},
\text{length}
\right).
\]

論文仍重要，但成為：

\[
\text{Research View}
\]

而非唯一研究本體。

---

# 9. 合成知識考古：可知邊界的逆時間擴張

## 9.1 生成與理解不同步

一項內容可能於：

\[
t_g
\]

生成，於：

\[
t_r>t_g
\]

才被辨認，於：

\[
t_v
\]

通過驗證。

這種現象稱為延遲發現。

---

## 9.2 認識積欠

設候選生成率為：

\[
\lambda_g.
\]

驗證率為：

\[
\lambda_v.
\]

若：

\[
\lambda_g>\lambda_v,
\]

則：

\[
B_{t+1}
=
B_t+\lambda_g-\lambda_v.
\]

積欠中可能同時包含：

- 大量錯誤；
- 平凡結果；
- 重複；
- 部分正確結構；
- 少量高價值候選。

---

## 9.3 考古算子

定義：

\[
\mathcal A_t:
L_t
\rightarrow
C_t\cup J_t\cup K_t.
\]

它包含：

1. 來源驗證；
2. 候選檢索；
3. 語義重建；
4. 無污染比較；
5. 獨立驗證；
6. 知識整合。

---

## 9.4 回收增益

\[
G_{\mathrm{rec}}
=
\sum_{x\in L_t}
p_x v_x r_x,
\]

其中：

- \(p_x\)：正確機率；
- \(v_x\)：潛在價值；
- \(r_x\)：被成功重建與驗證的機率。

---

## 9.5 事後偏誤限制

舊資料量越大，事後找到相似內容越容易。

因此：

\[
\text{semantic similarity}
\neq
\text{prior discovery}.
\]

延遲發現必須具備：

- 固定時間戳；
- 結果前生成；
- 無資料污染；
- 盲化重建；
- 明確對映；
- 獨立驗證；
- 全量假陽性報告。

---

# 10. 統一知識循環

## 10.1 基本循環

\[
U_t
\overset{\text{observation/inference}}{\longrightarrow}
J_t
\overset{\text{validation}}{\longrightarrow}
K_t.
\]

---

## 10.2 生成循環

\[
U_t
\overset{\text{generation}}{\longrightarrow}
C_t
\overset{\text{selection}}{\longrightarrow}
J_t
\overset{\text{validation}}{\longrightarrow}
K_t.
\]

---

## 10.3 埋藏與回收循環

\[
C_t
\overset{\text{neglect}}{\longrightarrow}
L_t
\overset{\text{archaeology}}{\longrightarrow}
C_{t+k}
\overset{\text{validation}}{\longrightarrow}
K_{t+k}.
\]

---

## 10.4 反身性循環

\[
K_t\cup J_t
\overset{\text{deployment}}{\longrightarrow}
A_t
\overset{\text{environmental change}}{\longrightarrow}
\Omega_{t+1}.
\]

原知識可能因此需要修訂：

\[
K_t
\rightarrow
J_{t+1}
\quad\text{或}\quad
C_{t+1}.
\]

---

## 10.5 研究狀態循環

\[
S_t
\overset{\text{iteration}}{\longrightarrow}
S_{t+1}
\overset{\text{externalization}}{\longrightarrow}
\text{lineage}
\overset{\text{handoff}}{\longrightarrow}
S_{t+2}.
\]

---

## 10.6 完整循環

\[
\boxed{
\text{未知}
\rightarrow
\text{候選}
\rightarrow
\text{判斷}
\rightarrow
\text{驗證}
\rightarrow
\text{部署}
\rightarrow
\text{環境改變}
\rightarrow
\text{新未知}
}
\]

同時：

\[
\boxed{
\text{失敗或未辨認痕跡}
\rightarrow
\text{保存}
\rightarrow
\text{考古}
\rightarrow
\text{重新驗證}
}
\]

---

# 11. 知識生產的四種環境

## 11.1 被動環境

- 規律相對穩定；
- 對象不回應預測；
- 狀態空間近似固定。

預期：

\[
G_{\mathrm{inf}}
\gg
C_{\mathrm{ref}}+C_{\mathrm{str}}.
\]

---

## 11.2 反應環境

- 預測改變行為；
- 行動者未必策略最佳化；
- 分布會因介入漂移。

---

## 11.3 策略環境

- 行動者理解規則；
- 會操縱、欺騙或反制；
- 預測者與對象形成博弈。

---

## 11.4 生成環境

- 行動者能創造新策略與制度；
- 狀態空間持續擴張；
- 研究與部署共同改寫問題。

---

## 11.5 環境與研究方法的匹配

| 環境 | 主要方法 | 主要風險 |
|---|---|---|
| 被動 | 準確率、校準、模型比較 | 過擬合、資料偏差 |
| 反應 | 因果推論、介入分析 | 自我實現、自我否定 |
| 策略 | 博弈、機制設計、對抗測試 | 模型操縱、規則套利 |
| 生成 | 情境、狀態空間監測、更新制度 | 模型外新穎性 |

---

# 12. 知識能動性的重新分配

## 12.1 問題提出

誰決定：

- 什麼值得研究；
- 什麼值得預測；
- 哪些結果不可接受？

---

## 12.2 候選生成

誰產生：

- 假說；
- 證明；
- 程式；
- 情境；
- 實驗？

---

## 12.3 候選選擇

誰決定：

- 哪些候選進入驗證；
- 哪些被捨棄；
- 哪些先保存？

---

## 12.4 驗證

誰擁有：

- 實驗權限；
- 形式驗證；
- 專家責任；
- 安全審查？

---

## 12.5 延續

誰決定：

- 是否繼續；
- 何時分支；
- 何時停止；
- 何時公開？

---

## 12.6 責任

知識貢獻與責任不能混同。

一個 AI 可以是主要內容生成者，但人類仍可能是：

- 研究方向控制者；
- 公開決策者；
- 法律責任者；
- 安全責任者；
- 最終驗證者。

---

# 13. 九項可檢驗命題

## P1：條件壓縮命題

在資訊可取得且規律相對穩定的問題中，協議化人機協作將提高條件完整性、情境涵蓋與可否證性。

---

## P2：非普遍綜效命題

人機協作的平均表現不必超越人類與 AI 中較佳者；綜效取決於任務結構、能力差異與錯誤相關性。

---

## P3：反身性非單調命題

環境反應性越高，模型能力提升對長期預測損失的邊際改善越低。

\[
\frac{\partial^2 L}
{\partial I\partial R_f}
>0.
\]

---

## P4：狀態空間擴張命題

在生成環境中，智能能力提高會同時提高已知候選發現率與模型外新狀態生成率。

---

## P5：絕對—相對分離命題

\[
\mu(K_t\cup J_t)\uparrow
\]

可以與：

\[
\kappa_t\downarrow
\]

同時發生。

---

## P6：外部化承接命題

持續研究狀態與譜系將降低跨模型承接的命題遺失、失敗重複及來源混淆。

---

## P7：驗證瓶頸命題

當 AI 候選生成率增長快於可信驗證率時，認識積欠與假陽性審查成本上升。

---

## P8：考古回收命題

在具有完整來源、不可變時間戳與盲化重建的資料庫中，歷史機器輸出存在可重現的非零知識回收率。

---

## P9：人類角色遷移命題

隨候選生成自動化，人類時間將相對由初始內容生產移向：

- 問題選擇；
- 方向控制；
- 例外處理；
- 驗證；
- 意義解釋；
- 風險治理。

此命題描述角色比例變化，不表示人類退出研究。

---

# 14. 統合實證研究方案

## 14.1 四種代理條件

### H：Human-only

人類獨立完成。

### A：AI-only

AI 在預定工具與權限下獨立完成。

### HA-F：Free collaboration

人類自由使用 AI。

### HA-P：Protocolized collaboration

依固定協議進行獨立判斷、衝突比較、反例與更新。

---

## 14.2 四種環境條件

\[
4\text{ 代理條件}
\times
4\text{ 環境}
\]

形成十六個主要實驗格。

---

## 14.3 模組一：預測與條件可判斷性

要求參與者處理：

- 穩定事件；
- 會因預測改變的事件；
- 具有策略對手的事件；
- 技術路徑生成問題。

測量：

- Brier score；
- log score；
- 校準；
- 情境涵蓋率；
- 模型外結果率；
- 更新延遲；
- 條件完整性。

---

## 14.4 模組二：持續研究承接

讓每組完成二十次研究迭代。

隨機指派：

- paper-only；
- paper + supplements；
- static research object；
- persistent research state。

中途更換：

- 人類研究者；
- 模型；
- Agent；
- 工具。

測量：

- 命題恢復率；
- 未決問題恢復率；
- 錯誤繼承率；
- 重複失敗率；
- 承接時間；
- 新增有效命題。

---

## 14.5 模組三：反身性部署

先建立預測模型，再隨機決定：

- 不公開；
- 部分公開；
- 全部公開；
- 自動依預測執行政策。

測量：

- 分布漂移；
- 行動改變；
- 自我實現；
- 自我否定；
- 模型壽命；
- 策略操縱。

---

## 14.6 模組四：合成知識考古

建立帶有：

- 真實完整前驅；
- 部分前驅；
- 表面相似；
- 污染候選；
- 錯誤候選；

的時間封鎖資料庫。

比較：

- 單一模型；
- 多模型；
- 人類專家；
- 人機協作；
- 盲化與非盲化。

---

# 15. 核心評估指標

## 15.1 條件可判斷增益

\[
CJG
=
J_{\mathrm{post}}
-
J_{\mathrm{pre}}.
\]

---

## 15.2 有效壓縮率

\[
ECR
=
\frac{
|\Omega_{\mathrm{before}}|
-
|\Omega_{\mathrm{after}}|
}{
|\Omega_{\mathrm{before}}|
}
\times
\text{coverage}.
\]

---

## 15.3 可知邊界速度

\[
v_{\Xi}
=
\frac{
\Delta\mu(K\cup J)
}{
\Delta t
}.
\]

---

## 15.4 狀態空間擴張率

\[
\nu_t
=
\frac{
\mu(\Omega_{t+1}\setminus\Omega_t)
}{
\Delta t
}.
\]

---

## 15.5 相對可知率

\[
\kappa_t
=
\frac{
\mu(K_t\cup J_t)
}{
\mu(\Omega_t)
}.
\]

---

## 15.6 反身性負載

\[
RL
=
d\cdot b\cdot a,
\]

其中：

- \(d\)：傳播範圍；
- \(b\)：信任與依賴程度；
- \(a\)：改變結果的能力。

---

## 15.7 研究承接完整度

\[
HC
=
w_QQ_r+w_CC_r+w_EE_r+w_FF_r+w_UU_r.
\]

---

## 15.8 驗證吞吐量

\[
VT
=
\frac{
\text{完成可信驗證的候選數}
}{
\Delta t
}.
\]

---

## 15.9 認識積欠

\[
D_t
=
\sum_{x_i\in B_t}
p_i v_i.
\]

---

## 15.10 考古回收率

\[
ARR
=
\frac{
\text{通過驗證的歷史候選}
}{
\text{被重新檢查的歷史候選}
}.
\]

---

# 16. 研究與知識基礎設施

## 16.1 最小研究狀態

```yaml
epistemic_state:
  id: ""
  timestamp: ""

  validated_knowledge: []
  conditionally_judgeable: []
  candidates: []
  latent_traces: []
  open_unknowns: []

  assumptions: []
  invalidation_triggers: []
  verification_backlog: []
  active_branches: []
  rejected_paths: []

  human_contributions: []
  ai_contributions: []
  responsibility_holders: []
```

---

## 16.2 狀態差分

```yaml
epistemic_diff:
  from_state: ""
  to_state: ""

  promoted:
    candidate_to_judgeable: []
    judgeable_to_validated: []
    latent_to_candidate: []

  demoted:
    validated_to_contested: []
    judgeable_to_unknown: []

  generated:
    new_candidates: []
    new_unknowns: []
    new_branches: []

  lost:
    missing_artifacts: []
    unverifiable_claims: []
    provenance_breaks: []

  review_priority: ""
```

---

## 16.3 與現有標準的關係

FAIR 原則提供：

- 可發現；
- 可存取；
- 可互操作；
- 可重用。

PROV-O 提供：

- Entity；
- Activity；
- Agent；
- generated-by；
- derived-from；
- attributed-to。

RO-Crate 提供可攜式研究物件封裝。

這些標準可作為基礎，但仍需要研究狀態、命題狀態、分支、失敗與交接語義。

---

# 17. 驗證制度

## 17.1 生成廉價化不等於知識廉價化

若一個模型每小時可產生一萬個候選：

\[
\lambda_g\uparrow.
\]

但實驗、形式化與專家審查沒有同步增長：

\[
\lambda_v\not\uparrow.
\]

則知識轉換率可能下降。

---

## 17.2 驗證階層

### Level 0：可解析

候選可轉為明確命題。

### Level 1：內部一致

不存在明顯矛盾。

### Level 2：自動檢查

通過測試、模擬或反例搜尋。

### Level 3：獨立重建

另一代理者取得等價結果。

### Level 4：形式或實驗驗證

符合領域核心標準。

### Level 5：社群整合

經公開批判與後續使用。

---

## 17.3 First Proof 的方法論意義

研究級證明生成案例說明：

- 完整論證可以被快速生成；
- 專家驗證仍可能需要較長時間；
- 初步高信心判斷可以被後續推翻；
- 所有嘗試與互動模式的公開有助於持續審查。

因此：

\[
\boxed{
\text{AI 時代的科學瓶頸，}
\newline
\text{可能由候選生成逐步轉向可信驗證。}
}
\]

---

# 18. 人類注意力的重新配置

## 18.1 逐篇閱讀不可擴展

若每次研究迭代都生成完整文章，人類注意力將被：

- 重複背景；
- 細微變體；
- 表述修改；
- 自動引用；
- 低價值候選；

消耗。

---

## 18.2 狀態突變優先

人類應優先檢查：

- 核心命題被推翻；
- 新反例；
- 主要方法改變；
- 實驗衝突；
- 安全風險；
- 來源斷裂；
- 跨模型不一致；
- 重大新分支。

---

## 18.3 理論新奇性飽和

讀者掌握核心範式後，後續文件的知識增量可能仍為正：

\[
\Delta K_n>0,
\]

但主觀閱讀價值下降：

\[
U_{n+1}<U_n.
\]

未來審閱單位可能由：

\[
\text{paper}
\]

轉為：

\[
\text{meaningful epistemic transition}.
\]

---

# 19. 治理與倫理

## 19.1 摘要權力

當人類只閱讀摘要，生成摘要的系統會決定：

- 哪些衝突被看見；
- 哪些失敗被省略；
- 哪些命題被提升；
- 哪些候選被忽略。

因此，所有摘要應附：

- 來源狀態；
- 省略項目；
- 壓縮規則；
- 替代視圖；
- 生成者；
- 驗證狀態。

---

## 19.2 知識污染

未驗證 AI 輸出若進入訓練資料，可能形成：

\[
\text{錯誤生成}
\rightarrow
\text{資料再攝取}
\rightarrow
\text{表面共識}.
\]

必須標記：

- 原始資料；
- 人類文獻；
- AI 推論；
- AI 摘要；
- 未驗證候選；
- 已驗證結果。

---

## 19.3 危險候選

持續研究與考古資料可能包含：

- 生物風險；
- 網路攻擊；
- 武器設計；
- 隱私資料；
- 安全漏洞。

完整保存不等於全面公開。

---

## 19.4 責任不可外包

「AI 產生」不能成為逃避：

- 資料合法性；
- 方法選擇；
- 公開決策；
- 安全審查；
- 撤回義務；

的理由。

---

## 19.5 知識不平等

若高品質模型、算力、資料庫與驗證資源集中於少數機構，AI 可能同時：

- 普及初步研究能力；
- 加劇高階驗證與基礎設施集中。

因此，評估不能只看生成工具的普及。

---

# 20. 制度含義

## 20.1 學術成果單位

未來可區分：

- Research Event；
- Candidate Claim；
- Published Artifact；
- Validated Result；
- Canonical Checkpoint；
- Persistent Research Program。

---

## 20.2 學術評價

不應以 AI 生成文件數量計算貢獻。

更合理指標包括：

- 被驗證命題；
- 可重用資料與程式；
- 研究承接品質；
- 錯誤修正；
- 失敗保存；
- 獨立重建；
- 驗證貢獻；
- 知識考古回收。

---

## 20.3 同行評審

需要由全文評審擴張為：

- 差分評審；
- 命題評審；
- 譜系評審；
- 程式評審；
- 安全評審；
- 抽樣審計；
- 獨立重建。

---

## 20.4 預測治理

高反身性預測應同時發布：

- 預測內容；
- 預期行動回應；
- 介入路徑；
- 參數不變性假設；
- 模型外可能性；
- 更新規則。

---

## 20.5 保存政策

應根據：

- 潛在價值；
- 驗證成本；
- 安全風險；
- 隱私；
- 可重生性；
- 來源完整性；

決定保存層級。

---

# 21. 理論邊界與反例

## 21.1 高智能可以提高穩定性

智能可改善：

- 機制設計；
- 協調；
- 風險控制；
- 驗證；
- 自動監測；
- 反操縱。

因此，本文不主張智能必然增加總不確定性。

---

## 21.2 狀態空間不一定無限擴張

部分任務的選項有限、規律穩定，AI 能使預測持續改善。

---

## 21.3 傳統論文仍可能是最佳介面

對首次學習、長篇論證與公共審議，論文可能優於圖譜與資料庫。

---

## 21.4 舊輸出多數可能沒有價值

合成知識考古的真實回收率可能極低。

只有嚴格實驗才能判斷是否值得制度化。

---

## 21.5 外部化可能製造額外負擔

低複雜、單次研究可能不需要完整狀態與譜系。

---

# 22. 反證標準

本框架在以下結果下將受到削弱：

1. 人機協作跨任務穩定優於雙方單獨最佳者，且不受任務結構調節；
2. 反應性與策略性不影響模型長期校準；
3. 智能提高只減少、而不產生任何可測量的新狀態或策略；
4. 持續研究狀態不能改善跨模型承接；
5. 驗證速度可與候選生成速度等比例擴張，不形成積欠；
6. 嚴格盲化考古無法找到非零可重現候選；
7. 相對可知率無法被有意義地操作化；
8. 多構面模型不能提供比單一準確率更好的解釋；
9. 狀態與譜系的維護成本長期高於其全部效益。

---

# 23. 研究限制

## 23.1 可知性不是單一客觀量

不同學科對：

- 證據；
- 驗證；
- 理解；
- 解釋；
- 可預測；

有不同標準。

---

## 23.2 狀態空間測量困難

在開放生成環境中，無法完整知道：

\[
\mu(\Omega_t).
\]

相對可知率通常只能使用代理指標。

---

## 23.3 人類與 AI 不是固定類別

能力會因：

- 模型版本；
- 專業程度；
- 工具；
- 提示；
- 訓練；
- 工作流程；

而變動。

---

## 23.4 研究案例的外推有限

數學、機器學習與生物研究的成功不代表社會科學、政治或歷史預測將以相同速度自動化。

---

## 23.5 研究基礎設施本身可能改變研究行為

一旦所有過程被追蹤，研究者與 Agent 可能針對指標行動，重新產生 Goodhart 類問題。

---

# 24. 討論

## 24.1 未來不是越來越確定，而是越來越可結構化

完全確定性並非合理目標。

更可能的進步是：

- 未知被分類；
- 條件被明確；
- 情境被比較；
- 失效被記錄；
- 更新變得更快；
- 來源更可追溯。

---

## 24.2 AI 不會自然成為拉普拉斯妖

類拉普拉斯全知要求：

- 固定狀態空間；
- 穩定規律；
- 完整初始條件；
- 預測者外生；
- 無策略回應；
- 無新穎性生成。

智能社會幾乎逐項違反這些條件。

---

## 24.3 智能的核心效果是雙向放大

\[
\boxed{
\text{智能放大認識能力，}
\newline
\text{也放大行動與生成能力。}
}
\]

因而知識與未知可能同時快速增長。

---

## 24.4 人類角色由逐項生產轉向邊界治理

當 AI 能大量產生候選，人類更需要決定：

- 哪些問題重要；
- 哪些候選值得驗證；
- 哪些風險不能承擔；
- 哪些狀態需要保存；
- 哪些發現具有意義；
- 哪些知識應如何使用。

---

## 24.5 科學將同時向前與向後運動

向前：

\[
\text{新問題}
\rightarrow
\text{新候選}
\rightarrow
\text{新知識}.
\]

向後：

\[
\text{舊痕跡}
\rightarrow
\text{新理解}
\rightarrow
\text{延遲發現}.
\]

這需要可保存、可查詢、可驗證的研究時間結構。

---

# 25. 結論

人工智能使人類第一次有可能以極高速度生成、比較與延續研究候選。

它能把一部分過去被視為混亂、無法判斷的問題轉為：

- 可分解；
- 可條件化；
- 可測量；
- 可更新；
- 可驗證。

但智能也讓行動者更能：

- 回應預測；
- 操縱模型；
- 創造新策略；
- 改寫制度；
- 擴張狀態空間；
- 生成超過驗證能力的候選。

因此，可知邊界不是只向外推進的直線。

它會：

- 擴張；
- 收縮；
- 分支；
- 漂移；
- 被遺忘；
- 被重新發現。

本文提出的統一框架是：

\[
\boxed{
\text{可知邊界}
=
\text{認識增益}
-
\text{反身與生成成本}
+
\text{研究記憶}
+
\text{歷史回收}.
}
\]

更完整地說：

\[
\boxed{
\text{人機協作擴張條件可判斷性，}
\newline
\text{智能反身性生成新的不確定性，}
\newline
\text{持續研究狀態保存知識的時間連續性，}
\newline
\text{合成知識考古使部分過去痕跡重新進入驗證。}
}
\]

這個框架拒絕兩種過度簡化。

第一種是：

\[
\text{AI 使一切可預測}.
\]

第二種是：

\[
\text{世界永遠不可判斷}.
\]

較合理的判斷是：

\[
\boxed{
\text{未來不會被完全壓縮，}
\newline
\text{但其中更多部分可以被轉化為可追蹤、可更新、可驗證的條件結構。}
}
\]

未來知識制度的真正成熟，不在於生成最多答案，而在於能否持續回答：

- 這個答案從哪裡來？
- 它在什麼條件下成立？
- 它如何改變被研究的世界？
- 哪些內容仍未驗證？
- 哪些研究路徑已失敗？
- 哪些舊資料值得重新檢查？
- 下一個人類或 AI 應從哪個狀態繼續？
- 誰對最後的使用與後果負責？

知識的邊界將持續移動。

真正的進步不是宣稱邊界已經消失，而是建立足以看見、記錄、驗證與治理其移動的方法。

---

# 作者貢獻說明

**Neo.K：** 核心命題提出、四篇前置研究之方向設計、可知邊界統合觀點、智能反身性與延遲發現之問題設定，以及系列論文整體架構。  

**Aletheia（GPT-5.6 Thinking）：** 理論整合、形式化模型、跨領域文獻綜合、可檢驗命題、實證研究方案、治理框架與初稿撰寫。  

> 投稿至不接受人工智能列名作者的期刊時，可依期刊政策調整署名，並在方法、作者貢獻或致謝中揭露 AI 的實質參與。AI 活動的記錄不替代人類作者對公開內容所承擔的責任。

---

# 利益衝突聲明

本文為統合理論、概念性與方法論研究。作者聲明目前無與本文核心命題直接相關的財務利益衝突。

---

# 資料與程式碼可得性

本文未使用新的實證資料。後續研究應公開預註冊設計、模型版本、提示協議、工具權限、研究狀態、譜系、評分程式與負結果；涉及隱私、雙重用途或高風險內容時，應採受控存取。

---

# 參考文獻

Arthur, W. B. (2015). *Complexity and the Economy*. Oxford University Press.

Brown, G., Hod, S., & Kalemaj, I. (2022). Performative prediction in a stateful world. *Proceedings of the 25th International Conference on Artificial Intelligence and Statistics*, 6045–6061.

Fawzi, A., Balog, M., Huang, A., et al. (2022). Discovering faster matrix multiplication algorithms with reinforcement learning. *Nature, 610*, 47–53. doi:10.1038/s41586-022-05172-4

Ghareeb, A. E., Chang, B., Mitchener, L., et al. (2026). A multi-agent system for automating scientific discovery. *Nature, 655*, 497–505. doi:10.1038/s41586-026-10652-y

Goodhart, C. A. E. (1975). Problems of monetary management: The U.K. experience. In *Papers in Monetary Economics* (Vol. 1). Reserve Bank of Australia.

Groth, P., Gibson, A., & Velterop, J. (2010). The anatomy of a nanopublication. *Information Services & Use, 30*(1–2), 51–56.

Hardt, M., Megiddo, N., Papadimitriou, C., & Wootters, M. (2016). Strategic classification. *Proceedings of the 2016 ACM Conference on Innovations in Theoretical Computer Science*, 111–122. doi:10.1145/2840728.2840730

Ke, Q., Ferrara, E., Radicchi, F., & Flammini, A. (2015). Defining and identifying Sleeping Beauties in science. *Proceedings of the National Academy of Sciences, 112*(24), 7426–7431. doi:10.1073/pnas.1424329112

Konkol, M., Nüst, D., & Goulier, L. (2020). Publishing computational research—A review of infrastructures for reproducible and transparent scholarly communication. *Research Integrity and Peer Review, 5*, 10. doi:10.1186/s41073-020-00095-y

Lebo, T., Sahoo, S., & McGuinness, D. (Eds.). (2013). *PROV-O: The PROV Ontology*. W3C Recommendation.

Loreto, V., Servedio, V. D. P., Strogatz, S. H., & Tria, F. (2017). Dynamics on expanding spaces: Modeling the emergence of novelties. In *Creativity and Universality in Language*. Springer.

Lu, C., Lu, C., Lange, R. T., et al. (2026). Towards end-to-end automation of AI research. *Nature, 651*, 914–919. doi:10.1038/s41586-026-10265-5

Lucas, R. E., Jr. (1976). Econometric policy evaluation: A critique. *Carnegie-Rochester Conference Series on Public Policy, 1*, 19–46. doi:10.1016/S0167-2231(76)80003-6

OpenAI. (2026a). *Our First Proof submissions*. Published February 20, 2026.

OpenAI. (2026b). *An OpenAI model has disproved a central conjecture in discrete geometry*. Published May 20, 2026.

Perdomo, J., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative prediction. *Proceedings of the 37th International Conference on Machine Learning*, 7599–7609.

Romera-Paredes, B., Barekatain, M., Novikov, A., et al. (2024). Mathematical discoveries from program search with large language models. *Nature, 625*, 468–475. doi:10.1038/s41586-023-06924-6

Soiland-Reyes, S., Sefton, P., Crosas, M., et al. (2022). Packaging research artefacts with RO-Crate. *Data Science, 5*(2), 97–138. doi:10.3233/DS-210053

Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature, 625*, 476–482. doi:10.1038/s41586-023-06747-5

Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour, 8*, 2293–2303. doi:10.1038/s41562-024-02024-1

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. doi:10.1038/sdata.2016.18

---

# 附錄 A：五態知識狀態格式

```yaml
knowledge_space:
  timestamp: ""

  K_validated:
    claims: []
    evidence: []
    validation_level: []

  J_conditionally_judgeable:
    scenarios: []
    probabilities: []
    assumptions: []
    falsifiers: []
    update_rules: []

  C_candidates:
    claims: []
    generation_source: []
    verification_priority: []

  L_latent_traces:
    artifacts: []
    preservation_tier: []
    archaeology_trigger: []

  U_unstructured_unknowns:
    open_questions: []
    model_outside_events: []
    unidentified_dependencies: []
```

---

# 附錄 B：人機協作協議

```yaml
collaboration_protocol:
  stage_1_independent:
    human_judgment: ""
    ai_judgment: ""

  stage_2_decomposition:
    base_rates: []
    scenarios: []
    causal_assumptions: []
    unknowns: []

  stage_3_adversarial:
    human_counterarguments: []
    ai_counterarguments: []
    model_outside_options: []

  stage_4_reconciliation:
    agreements: []
    disagreements: []
    unresolved: []

  stage_5_output:
    probabilities: {}
    confidence: ""
    invalidation_triggers: []
    update_schedule: ""

  stage_6_provenance:
    human_changes: []
    ai_changes: []
    final_responsibility: ""
```

---

# 附錄 C：可知邊界儀表板

```yaml
knowability_dashboard:
  absolute_known_volume: null
  conditionally_judgeable_volume: null
  candidate_volume: null
  latent_trace_volume: null

  state_space_expansion_rate: null
  relative_knowability: null
  verification_throughput: null
  epistemic_backlog: null

  reflexivity_load: null
  strategic_adaptation_rate: null
  outside_model_outcome_rate: null

  handoff_completeness: null
  archaeology_recovery_rate: null
  false_excavation_rate: null
```

---

# 附錄 D：統合理論名詞對照

| 中文 | 英文 | 定義 |
|---|---|---|
| 可知邊界 | Frontier of knowability | 已驗證或可條件判斷內容與尚未結構化未知之間的動態界面 |
| 條件可判斷性 | Conditional judgeability | 未能完全確定，但已具有情境、條件、可信度、失效與更新規則的狀態 |
| 可知性擴張悖論 | Knowability expansion paradox | 絕對知識增加，但可能狀態空間增長更快，使相對可知率下降 |
| 認識增益 | Epistemic gain | 觀測、推理、協調、保存與回收帶來的可知性提升 |
| 智能反身性 | Intelligent reflexivity | 智能行動者因預測或模型而改變行為，進而改變被預測系統 |
| 狀態空間擴張 | State-space expansion | 新技術、策略、制度與問題增加可行狀態集合 |
| 持續研究狀態 | Persistent research state | 可供跨人類、跨模型與跨時間承接的外部研究狀態 |
| 研究譜系 | Research lineage | 研究狀態、命題、證據、分支、失敗與貢獻的歷史關係圖 |
| 認識積欠 | Epistemic backlog | 已生成但未完成辨認與驗證之候選的預期知識價值 |
| 合成知識考古 | Synthetic knowledge archaeology | 從歷史機器輸出中重建、驗證與整合延遲發現的方法 |
| 驗證吞吐量 | Verification throughput | 單位時間內完成可信驗證的候選數量 |
| 邊界治理 | Frontier governance | 對問題選擇、驗證資源、研究記憶、發布、安全與責任的整體治理 |

