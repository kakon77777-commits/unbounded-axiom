# 主 AI 的雙路形成命題：通用模型認知重構與持續養成式智能的發展路徑

**English Title:** *The Dual-Path Formation Hypothesis of Main AI: Cognitive Reconstruction of General Models and Continual Developmental Intelligence*

**作者：** Neo.K  
**AI 協作：** Aletheia  
**研究脈絡：** EveMissLab / Logic Matrix / GCMS / 認知解構學 2.0  
**文件類型：** 命題猜想論文  
**版本：** v0.1  
**日期：** 2026-07-30  

---

## 摘要

本文提出「主 AI 的雙路形成命題」（Dual-Path Formation Hypothesis of Main AI, DPFH-MAI）。先前的壓縮全局智能與認知原子因果基底理論，將主 AI 定義為後設完備、基底稠密、表層稀疏，並能透過 GCMS、子 Agent、外部通用模型與大型推理模型按需展開高解析度能力。然而，從現有人工智能系統走向此類主 AI，至少存在兩條本質不同的形成路徑。

第一條是**認知重構式路徑**：從現有通用大模型出發，逐步辨識其判斷、推理、因果理解、記憶、語言、領域知識與社會模式之間的隱性交織，對模型進行能力映射、結構化蒸餾、認知解構、因果基底抽取、表層知識外部化、主控能力精煉與多 Agent 重新配置。此路徑初始能力高、可較快形成實用系統，但困難不只是模型縮小，而是如何刪除或外部化大量高解析度知識，同時不破壞支撐高階判斷的隱性知識支架。主 AI 所需的判斷力並非可與領域經驗乾淨分離；模型壓縮也可能選擇性傷害推理、指令遵循、多語與長尾能力。因此，完整的認知重構可能需要尚未成熟的模型可解構性、因果可定位性與可恢復壓縮技術。

第二條是**持續養成式路徑**：從一個具基本語言、推理、記憶與工具能力的種子智能開始，透過長期任務、外部記憶、經驗回饋、能力分級、認知原子建構、因果圖更新、子 Agent 協作與逐步授權，形成具有時間連續性的主 AI。此路徑前期可能表現普通，甚至明顯弱於成熟通用大模型；但它的能力形成歷史、錯誤來源、知識版本、任務經驗與權限成長較可追蹤，因而具有較大的長期結構潛力。養成式的核心優勢不是初始分數，而是可持續能力斜率、功能連續性與可治理的成長史。

本文進一步提出第三種較現實的**混合胚胎式路徑**：使用已具備通用語言和基本推理能力的中小型基礎模型作為認知胚胎，但不把其當成完成品；以外部大模型充當教師與高能力服務，以 GCMS 保存經驗與因果基底，以分級授權控制自主性，逐步把高頻、可驗證、主控必要的能力內化到主 AI，而將低頻、高成本、高解析度的領域能力保持外部化。混合路徑試圖兼得重構式的初始能力與養成式的可追蹤成長。

本文建立能力糾纏、知識支架、重構損失、發展潛力、成長斜率、記憶穩定—可塑性、外部依賴與主控成熟度模型，提出十五項命題與猜想、十四類失敗模式、三階段工程路線及九組可否證實驗。本文最終主張：理論中的完整主 AI 可能不是一次訓練或一次壓縮的產物，而是一個具有形成歷史、持續修正、外部協同與結構重編譯能力的長期系統；重構式主 AI 是被提煉出的，養成式主 AI 是逐漸長成的，而最可能首先落地的主 AI，將是二者之間的混合發展體。

**關鍵詞：** 主 AI、認知重構、養成式 AI、持續學習、終身 Agent、模型壓縮、知識蒸餾、能力糾纏、認知胚胎、成長斜率、GCMS、認知原子、子 Agent、災難性遺忘、混合智能發展

---

# 0. 研究定位與聲明

本文延續以下理論方向：

1. 主 AI 不必在所有領域中同時擁有最高解析度能力；
2. 主 AI 必須在判斷、決策、推理、記憶、因果理解、驗證與治理等主控維度上跨過最低閾值；
3. 主 AI 應常駐認知原子與跨尺度因果基底，而非全部領域表層；
4. 子 Agent、外部模型與工具負責按需展開高解析度能力；
5. 主 AI 的形成過程本身是尚未被充分處理的核心問題。

本文不主張：

- 已有技術能完整製造理論中的主 AI；
- 模型蒸餾可以無損抽出判斷力；
- 從零訓練的小模型一定具有更高長期潛力；
- 持續對話自然等於持續學習；
- 外部記憶可以消除災難性遺忘；
- 養成式 AI 必然形成更一致或更安全的智能；
- 通用大模型必然無法被重構；
- 單一生命史是主 AI 的必要本體條件；
- 功能連續性等於意識、人格或主體性；
- 主 AI 必須由單一模型承載。

本文所稱主 AI，是具有長期目標、全局狀態、認知基底、記憶治理、能力調度與決策連續性的功能性控制核心。

---

# 1. 問題的提出：主 AI 從哪裡來？

## 1.1 架構描述不等於形成機制

我們可以相對容易地描述一個理想主 AI：

$$
\boxed{
\begin{aligned}
A_{\mathrm{main}}
={}&
\text{Meta-Complete}\\
&+
\text{Basis-Dense}\\
&+
\text{Surface-Sparse}\\
&+
\text{Causally Structured}\\
&+
\text{Memory-Continuous}\\
&+
\text{Agent-Orchestrating}\\
&+
\text{Evidence-Governed}.
\end{aligned}
}
$$

但知道終局架構，不等於知道如何把一個現有模型轉換成它。

這形成「主 AI 形成缺口」：

$$
\mathcal F_{\mathrm{gap}}
=
d
\left(
M_{\mathrm{current}},
A_{\mathrm{main}}^\ast
\right).
$$

其中：

- $M_{\mathrm{current}}$ ：現有模型或 Agent 系統；
- $A_{\mathrm{main}}^\ast$ ：理論目標；
- $d$ ：能力、記憶、因果、治理與連續性差異。

---

## 1.2 看似簡單的架構為何難以實現？

理想架構看似只有四個主要元件：

$$
A_{\mathrm{main}}
+
\mathcal M_{\mathrm{GCMS}}
+
\left\{
A_i
\right\}
+
\left\{
M_j
\right\}.
$$

但其形成至少需要同時解決：

1. 哪些能力應常駐主 AI；
2. 哪些知識可以外部化；
3. 哪些知識是判斷力的隱性支架；
4. 如何抽取認知原子；
5. 如何建立跨尺度因果圖；
6. 如何保持長期記憶；
7. 如何防止持續學習遺忘舊能力；
8. 如何調用更強模型而不發生權威倒置；
9. 如何讓自主性逐步成長而非一次性放權；
10. 如何衡量「主 AI 已經成熟到什麼程度」。

因此：

$$
\boxed{
\text{主 AI 不是一個簡單組件，}
\quad
\text{而是一段形成歷史。}
}
$$

---

# 2. 兩條基本形成路徑

本文定義兩條主路徑：

$$
\mathfrak P
=
\left\{
\mathfrak P_R,
\mathfrak P_N
\right\},
$$

其中：

- $\mathfrak P_R$ ：重構式路徑；
- $\mathfrak P_N$ ：養成式路徑。

---

## 2.1 重構式路徑

從大型通用模型開始：

$$
M_G^0,
$$

經過多階段重構：

$$
M_G^0
\rightarrow
M_G^1
\rightarrow
\cdots
\rightarrow
A_{\mathrm{main}}^R.
$$

其基本方向是：

$$
\boxed{
\text{先有龐大能力，}
\quad
\text{再辨認、重整與提煉主控核心。}
}
$$

---

## 2.2 養成式路徑

從種子模型或持續核心開始：

$$
A_{\mathrm{seed}}^0,
$$

透過長期經驗形成：

$$
A_{\mathrm{seed}}^0
\rightarrow
A_{\mathrm{apprentice}}^1
\rightarrow
A_{\mathrm{coordinator}}^2
\rightarrow
A_{\mathrm{main}}^N.
$$

其基本方向是：

$$
\boxed{
\text{先有持續核心，}
\quad
\text{再逐步長出能力、記憶與治理結構。}
}
$$

---

# 3. 路線一：通用大模型的認知重構

## 3.1 它不是普通模型壓縮

普通壓縮可能追求：

$$
\min
\operatorname{Size}(M')
$$

使：

$$
Q_{\mathrm{benchmark}}(M')
\geq
\theta_Q.
$$

主 AI 重構則需要保留一組特殊能力：

$$
\mathcal C_{\mathrm{main}}
=
\left\{
\begin{aligned}
&\mathsf{Judge},
\mathsf{Decide},
\mathsf{Reason},
\mathsf{Deconstruct},\\
&\mathsf{CausalModel},
\mathsf{CompressMemory},
\mathsf{Reconstruct},\\
&\mathsf{Route},
\mathsf{Verify},
\mathsf{Govern}
\end{aligned}
\right\}.
$$

其目標是：

$$
\min
\operatorname{ResidentComplexity}(M')
$$

使：

$$
\forall c\in\mathcal C_{\mathrm{main}},
\quad
\operatorname{Competence}(M',c)
\geq
\theta_c.
$$

並且：

$$
\operatorname{SurfaceRedundancy}(M')
\rightarrow 0.
$$

---

## 3.2 能力糾纏問題

在通用模型中，能力並不一定是彼此分離的模組。

設能力支撐圖為：

$$
\mathcal G_C
=
\left(
V_C,
E_{\mathrm{support}}
\right).
$$

其中節點包括：

- 領域知識；
- 語言能力；
- 類比經驗；
- 推理模板；
- 社會語境；
- 記憶模式；
- 因果先驗；
- 判斷校準。

若：

$$
k_i
\xrightarrow{\mathrm{support}}
c_j,
$$

表示某項看似額外的知識 $k_i$ ，實際支撐主控能力 $c_j$ 。

因此：

$$
\operatorname{Remove}(k_i)
\Rightarrow
\Delta c_j<0
$$

可能在壓縮後才顯現。

---

## 3.3 額外知識不一定是冗餘

例如：

- 法律案例可能支撐例外條件判斷；
- 物理知識可能支撐尺度與守恆辨認；
- 歷史知識可能支撐制度因果；
- 語言與文化知識可能支撐語用判斷；
- 大量失敗樣本可能支撐錯誤拒絕。

因此，表層知識可以分成：

$$
\mathcal K_{\mathrm{surface}}
=
\mathcal K_{\mathrm{redundant}}
\cup
\mathcal K_{\mathrm{support}}
\cup
\mathcal K_{\mathrm{critical}}.
$$

真正可以放心外部化的只有：

$$
\mathcal K_{\mathrm{redundant}}
$$

及可以高保真重建的部分。

---

## 3.4 重構損失

定義模型重構後的能力損失：

$$
L_R
=
\sum_{c\in\mathcal C_{\mathrm{main}}}
w_c
\left[
Q_c(M_G^0)
-
Q_c(M')
\right]_+.
$$

但基準測試往往只能測到表面任務，無法立即發現：

- 長期決策漂移；
- 未見任務分解退化；
- 因果邊界模糊；
- 拒絕錯誤能力下降；
- 權威倒置風險；
- 跨領域遷移下降。

因此需要延遲重構損失：

$$
L_R^{\mathrm{delayed}}
=
\mathbb E_{q\sim Q_{\mathrm{long}}}
\left[
U(M_G^0,q)
-
U(M',q)
\right].
$$

---

## 3.5 認知重構流程

本文提出：

$$
\boxed{
\begin{aligned}
M_G^0
&\xrightarrow{\mathsf{CapabilityMap}}
M_G^1\\
&\xrightarrow{\mathsf{SupportGraph}}
M_G^2\\
&\xrightarrow{\mathsf{CognitiveDeconstruct}}
M_G^3\\
&\xrightarrow{\mathsf{BasisExtract}}
M_G^4\\
&\xrightarrow{\mathsf{StructuredDistill}}
M_G^5\\
&\xrightarrow{\mathsf{ExternalizeSurface}}
M_G^6\\
&\xrightarrow{\mathsf{AgentReallocate}}
A_{\mathrm{main}}^R.
\end{aligned}
}
$$

這不是一次性剪枝，而是多輪：

$$
\text{刪除}
\rightarrow
\text{恢復}
\rightarrow
\text{測試}
\rightarrow
\text{重新解構}.
$$

---

## 3.6 重構式路徑的優勢

- 初始語言與世界知識豐富；
- 初始推理能力較高；
- 初期可用性強；
- 可快速接入外部工具；
- 可利用既有對齊與安全訓練；
- 較容易獲得廣泛任務覆蓋。

---

## 3.7 重構式路徑的根本困難

- 能力支架不可見；
- 壓縮損失選擇性發生；
- 模型內部因果不可充分定位；
- 表層與基底不能乾淨分離；
- 訓練資料形成史不可追蹤；
- 原始偏誤可能被一併壓縮保留；
- 壓縮後的模型可能變成「知道較少，也判斷較差」。

---

# 4. 路線二：持續養成式主 AI

## 4.1 養成不是單純增加聊天紀錄

養成式主 AI 的狀態為：

$$
S_t
=
\left(
\theta_t,
\mathcal M_t,
\mathcal G_t,
\mathcal C_t,
\mathcal P_t,
\mathcal H_t
\right),
$$

其中：

- $\theta_t$ ：可更新模型或適配器參數；
- $\mathcal M_t$ ：長期記憶；
- $\mathcal G_t$ ：認知原子與因果圖；
- $\mathcal C_t$ ：已形成能力；
- $\mathcal P_t$ ：權限與自主級別；
- $\mathcal H_t$ ：形成歷史。

養成要求：

$$
S_{t+1}
=
\operatorname{Develop}
\left(
S_t,
E_t,
F_t,
R_t
\right),
$$

其中：

- $E_t$ ：環境與任務經驗；
- $F_t$ ：回饋與驗證；
- $R_t$ ：反思、重播與重組。

---

## 4.2 初始普通不是缺陷，而是路徑特徵

養成式主 AI 的初始能力可能滿足：

$$
Q(A_{\mathrm{seed}}^0)
\ll
Q(M_G^0).
$$

但其潛力不由初始分數單獨決定，而由成長函數決定：

$$
Q_{t+1}
=
Q_t
+
\Delta Q_{\mathrm{experience}}
+
\Delta Q_{\mathrm{transfer}}
+
\Delta Q_{\mathrm{reflection}}
-
L_{\mathrm{forget}}
-
L_{\mathrm{drift}}.
$$

定義長期成長斜率：

$$
g_t
=
\frac{dQ_t}{dt}.
$$

養成式路徑可能具有：

$$
Q_0\text{ 較低},
$$

但：

$$
\mathbb E[g_t]
\text{ 較高或較可持續}.
$$

---

## 4.3 形成史可追蹤性

每一項能力 $c_i$ 可以保存：

$$
c_i
=
\left(
\text{origin},
\text{training},
\text{evidence},
\text{failures},
\text{version},
\text{permissions}
\right).
$$

因此，系統可以回答：

- 這項能力何時形成？
- 來自哪些任務？
- 在什麼情境失敗？
- 哪些知識支撐它？
- 是否可以撤銷？
- 是否值得內化？

這是養成式路徑的重要優勢。

---

## 4.4 穩定—可塑性問題

持續學習同時需要：

$$
\text{Stability}
+
\text{Plasticity}.
$$

太穩定：

$$
\Delta\theta_t\approx 0
$$

會無法學習。

太可塑：

$$
\|\Delta\theta_t\|\gg 0
$$

會造成舊能力遺忘、人格漂移或因果圖破壞。

定義：

$$
J_{\mathrm{SP}}
=
\alpha Q_{\mathrm{new}}
+
\beta Q_{\mathrm{old}}
-
\gamma F_{\mathrm{forget}}
-
\delta D_{\mathrm{identity}}.
$$

養成式主 AI 必須最大化：

$$
J_{\mathrm{SP}}.
$$

---

## 4.5 外部記憶不是完整解法

若將所有學習移到外部記憶：

$$
\theta_{t+1}=\theta_t,
$$

$$
\mathcal M_{t+1}
=
\mathcal M_t
\cup
E_t,
$$

則參數遺忘可能降低，但新舊經驗會在有限提取與上下文中競爭。

因此：

$$
\boxed{
\text{記憶外部化}
\neq
\text{持續學習問題消失}.
}
$$

瓶頸會從：

$$
\text{參數更新}
$$

轉移到：

$$
\text{記憶選擇、壓縮、競爭與重建}.
$$

---

## 4.6 養成式主 AI 的優勢

- 形成史可追蹤；
- 知識和能力可版本化；
- 錯誤來源相對可定位；
- 自主權可以逐步授予；
- 主控能力可根據實際任務生長；
- 記憶、因果圖與工具使用可共同演化；
- 較容易形成特定組織或個人的長期方法。

---

## 4.7 養成式主 AI 的根本困難

- 初始能力普通；
- 成長需要長時間；
- 早期錯誤可能造成路徑依賴；
- 經驗分布可能過窄；
- 容易過度擬合單一使用者或環境；
- 持續更新可能破壞舊能力；
- 缺乏可靠的長期學習基準；
- 成長潛力難以預先證明。

---

# 5. 第三條現實路線：混合胚胎式形成

## 5.1 為何純雙分法不夠？

純重構式過於困難：

$$
\mathcal F_{\mathrm{extract}}\gg 0.
$$

純從零養成又過於緩慢：

$$
Q_0\ll\theta_{\mathrm{usable}}.
$$

因此本文提出：

$$
\mathfrak P_H
=
\text{Hybrid Embryonic Path}.
$$

---

## 5.2 認知胚胎

選擇一個具有：

- 基本語言；
- 基本推理；
- 工具調用；
- 基礎安全；
- 短期規劃；
- 可適配架構；

的種子模型：

$$
M_{\mathrm{embryo}}.
$$

它不需要是最小模型，也不需要是最強模型。關鍵是：

$$
\operatorname{Adaptability}
+
\operatorname{MetaCapacity}
+
\operatorname{MemoryInterface}
\geq
\theta_E.
$$

---

## 5.3 外部大模型作為教師與能力服務

外部模型具有兩種角色：

### 教師

$$
M_L
\xrightarrow{\mathrm{teach}}
A_{\mathrm{embryo}}.
$$

提供：

- 示範；
- 反例；
- 評分；
- 任務分解；
- 修正；
- 高難度解答。

### 高能力服務

$$
A_{\mathrm{embryo}}
\xrightarrow{\mathrm{API}}
M_L.
$$

主 AI 不必立即內化所有低頻能力。

---

## 5.4 選擇性內化

定義能力內化價值：

$$
V_{\mathrm{int}}(c)
=
f
\left(
\operatorname{Frequency},
\operatorname{ControlImportance},
\operatorname{Latency},
\operatorname{Privacy},
\operatorname{Reliability},
\operatorname{Cost}
\right).
$$

若：

$$
V_{\mathrm{int}}(c)
>
\theta_{\mathrm{int}},
$$

則將能力逐步內化。

否則保持：

$$
c\in\mathcal C_{\mathrm{external}}.
$$

主 AI 最終形成：

$$
\mathcal C_{\mathrm{main}}
=
\mathcal C_{\mathrm{native}}
\cup
\mathcal C_{\mathrm{internalized}}
\cup
\mathcal C_{\mathrm{routable}}.
$$

---

## 5.5 自主性分級

自主權不是一次性給予，而是：

$$
P_0
\subset
P_1
\subset
\cdots
\subset
P_n.
$$

每個能力 $c_i$ 的自主等級：

$$
L_i
\in
\left\{
\text{observe},
\text{suggest},
\text{execute-with-review},
\text{execute},
\text{delegate}
\right\}.
$$

提升條件：

$$
\operatorname{Reliability}(c_i)
\geq
\theta_R,
$$

$$
\operatorname{Auditability}(c_i)
\geq
\theta_A,
$$

$$
\operatorname{Rollback}(c_i)=1.
$$

---

# 6. 三條路線的形式比較

定義形成效用：

$$
U_F
=
\alpha Q_0
+
\beta G_{\mathrm{long}}
+
\gamma T_{\mathrm{trace}}
+
\delta M_{\mathrm{continuity}}
+
\epsilon C_{\mathrm{govern}}
-
\lambda C_{\mathrm{train}}
-
\mu R_{\mathrm{failure}}.
$$

其中：

- $Q_0$ ：初始能力；
- $G_{\mathrm{long}}$ ：長期成長潛力；
- $T_{\mathrm{trace}}$ ：形成史可追蹤性；
- $M_{\mathrm{continuity}}$ ：記憶與功能連續；
- $C_{\mathrm{govern}}$ ：治理品質；
- $C_{\mathrm{train}}$ ：形成成本；
- $R_{\mathrm{failure}}$ ：失敗風險。

一般可能呈現：

$$
Q_0^R
>
Q_0^H
>
Q_0^N,
$$

$$
T_{\mathrm{trace}}^N
>
T_{\mathrm{trace}}^H
>
T_{\mathrm{trace}}^R,
$$

$$
C_{\mathrm{restructure}}^R
>
C_{\mathrm{restructure}}^H
>
C_{\mathrm{restructure}}^N.
$$

但：

$$
G_{\mathrm{long}}^N,
G_{\mathrm{long}}^H
$$

是否真正高於重構式，仍需實證。

---

# 7. 主 AI 形成的十五項命題與猜想

## 命題 1：終局—形成分離命題

知道主 AI 的理想結構，不足以推出可行形成程序：

$$
\operatorname{Specify}(A^\ast)
\not\Rightarrow
\operatorname{Construct}(A^\ast).
$$

---

## 命題 2：能力糾纏命題

通用模型中的主控能力與領域知識通常不是完全獨立的：

$$
I
\left(
\mathcal C_{\mathrm{meta}};
\mathcal K_{\mathrm{domain}}
\right)
>
0.
$$

因此，移除領域知識可能同時傷害判斷與因果推理。

---

## 命題 3：重構非普通蒸餾命題

若蒸餾只匹配輸出 token 或靜態基準，而不保留：

- 決策軌跡；
- 工具選擇；
- 錯誤拒絕；
- 因果依賴；
- 記憶重建；
- 長期治理；

則其結果不能被視為主 AI 重構。

---

## 命題 4：重構延遲損失命題

部分主控能力退化只會在長生命週期、未見任務或跨域衝突中顯現：

$$
L_R^{\mathrm{delayed}}
>
L_R^{\mathrm{benchmark}}
$$

可能普遍成立。

---

## 命題 5：形成悖論命題

完整重構主 AI 所需的能力映射、因果定位與長期評估，本身可能需要近似主 AI 的研究系統：

$$
\operatorname{Build}(A_{\mathrm{main}})
\rightarrow
\operatorname{Need}
\left(
A_{\mathrm{proto-main}}
\right).
$$

---

## 命題 6：養成低初始—高潛力猜想

養成式主 AI 可能具有較低初始能力，但較高的可追蹤成長潛力：

$$
Q_0^N<Q_0^R,
$$

但可能：

$$
\lim_{t\rightarrow\infty}
Q_t^N
\geq
\lim_{t\rightarrow\infty}
Q_t^R.
$$

此命題不能由理論保證，必須以長期實驗驗證。

---

## 命題 7：形成史價值命題

若每項能力保存形成來源、失敗史、證據與版本，則：

$$
\operatorname{Auditability}
+
\operatorname{Rollback}
+
\operatorname{TargetedRepair}
$$

將高於不可追蹤的能力混合體。

---

## 命題 8：外部記憶瓶頸轉移命題

外部記憶可降低參數更新壓力，但會把持續學習瓶頸轉移至：

$$
\text{retrieval}
+
\text{competition}
+
\text{compression}
+
\text{context allocation}.
$$

---

## 命題 9：能力成熟度非單值命題

主 AI 的成熟度不是一個總分，而是向量：

$$
\mathbf m_t
=
\left(
m_{\mathrm{judge}},
m_{\mathrm{memory}},
m_{\mathrm{causal}},
m_{\mathrm{route}},
m_{\mathrm{govern}},
m_{\mathrm{autonomy}}
\right).
$$

某些能力成熟不代表可以全面提高自主權。

---

## 命題 10：選擇性內化命題

高頻、低延遲容忍、隱私敏感、主控必要的能力應優先內化；低頻、高成本、高解析度能力可以長期外部化。

---

## 命題 11：混合胚胎優勢猜想

在有限時間與資源下，混合胚胎式可能同時取得：

- 可接受初始能力；
- 可追蹤形成史；
- 較低重構風險；
- 持續成長能力。

但協調成本可能抵消其優勢。

---

## 命題 12：自主性應被習得命題

對高風險能力，自主權應建立在實證可靠度、可審計性與可回滾性上，而不是隨模型規模自動給予。

---

## 命題 13：普通表現不等於低潛力命題

早期養成式 AI 的表面基準分數不能充分預測其長期：

- 學習斜率；
- 記憶連續性；
- 方法內化；
- 工具適應；
- 治理成熟度。

---

## 命題 14：路徑依賴命題

主 AI 的早期經驗與基底會限制後續能力空間：

$$
S_{t+k}
=
F
\left(
S_t,
E_{t:t+k}
\right).
$$

錯誤早期原子可能產生長期偏移。

---

## 命題 15：雙路形成命題

存在至少兩類不同的主 AI 形成機制：

$$
A_{\mathrm{main}}^R
=
\operatorname{Reconstruct}
\left(
M_G
\right),
$$

$$
A_{\mathrm{main}}^N
=
\operatorname{Develop}
\left(
A_{\mathrm{seed}},
E_{0:T}
\right).
$$

兩者可能達到相似功能終點，但其能力分布、形成史、風險與可治理性並不等價。

---

# 8. 十四類失敗模式

## 8.1 過度壓縮

刪除看似冗餘的知識支架，使判斷能力下降。

## 8.2 壓縮錯覺

靜態基準不退化，但長期主控能力已受損。

## 8.3 能力不可分離

無法從大模型中乾淨抽取主控核心。

## 8.4 教師偏差繼承

重構或養成過度依賴單一大型教師，複製其盲點。

## 8.5 災難性遺忘

新能力覆蓋舊能力。

## 8.6 記憶競爭

外部記憶過多，使真正關鍵經驗無法被提取。

## 8.7 早期路徑鎖定

養成初期的錯誤世界模型限制後續成長。

## 8.8 經驗狹窄

養成式只適應單一使用者、組織或任務。

## 8.9 表現普通而被提前終止

系統在長期潛力尚未顯現前被淘汰。

## 8.10 無限制持續更新

缺乏版本與回滾，使主 AI 長期漂移。

## 8.11 自主權過早

能力未成熟即取得高風險工具和委派權。

## 8.12 外部依賴鎖定

核心能力長期依賴特定 API 或供應商。

## 8.13 混合系統身份破碎

本地種子、外部教師與多個 Agent 的決策彼此不一致。

## 8.14 成長評估短視

只測即時能力，不測學習斜率、形成史與長期穩定性。

---

# 9. 三階段工程路線

## 階段一：主 AI 前驅體

先不追求完整主 AI，只建立：

- 持續身份與目標；
- GCMS 長期記憶；
- 認知原子因果圖；
- 外部模型路由；
- 候選寫回；
- 能力與權限登錄。

此階段可以由現有通用模型充當臨時主控器。

---

## 階段二：混合胚胎

建立中小型持續核心：

$$
A_{\mathrm{embryo}}.
$$

由通用大模型提供：

- 高難度推理；
- 教師回饋；
- 反例；
- 評測；
- 能力示範。

逐步內化：

- 任務拆解；
- 記憶管理；
- 常見判斷；
- 高頻路由；
- 因果驗證；
- 組織特定方法。

---

## 階段三：認知重構

未來模型解構技術成熟後，才嘗試從大型模型中：

- 抽取主控回路；
- 定位知識支架；
- 建立可測因果能力圖；
- 進行多輪剪枝—恢復；
- 將表層知識外部化；
- 保留底層因果和判斷基底。

此階段才可能接近完整路線一。

---

# 10. 九組可否證實驗

## 實驗 1：重構式與普通蒸餾

比較：

1. token 蒸餾；
2. 推理軌跡蒸餾；
3. Agent 結構化蒸餾；
4. 認知重構式蒸餾。

測量長期路由、拒錯、因果和記憶能力。

---

## 實驗 2：知識支架消融

逐步移除不同類型領域知識，測量主控能力是否下降，以建立能力支撐圖。

---

## 實驗 3：養成式長期基準

讓同一種子 Agent 經歷多月任務流，測量：

- 正向轉移；
- 遺忘；
- 學習斜率；
- 記憶品質；
- 權限成熟。

---

## 實驗 4：外部記憶與參數學習

比較：

- 純參數更新；
- 純外部記憶；
- 適配器更新；
- 記憶加選擇性內化。

---

## 實驗 5：混合胚胎

比較：

- 通用大模型直接主控；
- 小型路由器；
- 養成種子；
- 通用胚胎加長期養成。

---

## 實驗 6：形成史可追蹤性

注入錯誤能力後，比較不同路徑能否定位來源、撤銷與修復。

---

## 實驗 7：早期普通與長期潛力

使用相同初始算力預算，觀察早期分數與長期能力是否高度相關。

---

## 實驗 8：自主權分級

比較一次性全面放權與按能力成熟度逐級授權的失敗率。

---

## 實驗 9：教師多樣性

比較單一大模型教師、異質教師池及人機混合教師，測量偏差相關性與能力多樣性。

---

# 11. 評估指標

## 11.1 初始能力

$$
Q_0.
$$

## 11.2 長期成長斜率

$$
G_T
=
\frac{Q_T-Q_0}{T}.
$$

## 11.3 災難性遺忘率

$$
F_T
=
\frac{1}{N}
\sum_i
\left[
Q_i^{\max}
-
Q_i^T
\right].
$$

## 11.4 正向轉移

$$
T^+
=
Q_{\mathrm{new\ after\ prior}}
-
Q_{\mathrm{new\ from\ scratch}}.
$$

## 11.5 形成史可追蹤率

$$
H_{\mathrm{trace}}
=
\frac{
\text{可追溯來源的能力}
}{
\text{全部已形成能力}
}.
$$

## 11.6 重構損失

$$
L_R.
$$

## 11.7 延遲重構損失

$$
L_R^{\mathrm{delayed}}.
$$

## 11.8 外部依賴率

$$
D_{\mathrm{external}}
=
\frac{
\text{需外部模型完成的關鍵步驟}
}{
\text{全部關鍵步驟}
}.
$$

## 11.9 內化效率

$$
E_{\mathrm{int}}
=
\frac{
\Delta Q_{\mathrm{local}}
}{
C_{\mathrm{training}}
+
C_{\mathrm{memory}}
}.
$$

## 11.10 主控成熟度

$$
M_{\mathrm{control}}
=
f
\left(
J,
C,
M,
R,
V,
G
\right),
$$

其中：

- $J$ ：判斷；
- $C$ ：因果；
- $M$ ：記憶；
- $R$ ：路由；
- $V$ ：驗證；
- $G$ ：治理。

---

# 12. 與現有研究的關係

## 12.1 持續與終身 Agent

終身 Agent 研究已將感知、記憶與行動視為持續適應的核心，並指出現有 Agent 多為靜態系統。相關基準也顯示，簡單經驗重播容易受到無關資訊和上下文限制。

本文進一步強調：

$$
\text{長期記憶}
+
\text{持續任務}
$$

不自動等於養成式主 AI，還需要能力形成、因果圖、權限成長與選擇性內化。

---

## 12.2 模型壓縮與 Agent 蒸餾

結構化 Agent 蒸餾開始分別保存推理與行動軌跡，比單純 token 模仿更接近主 AI 重構需求。

但本文認為仍需增加：

- 判斷校準；
- 因果支撐圖；
- 長期記憶；
- 拒錯；
- 治理；
- 未見任務分解。

---

## 12.3 漸進壓縮

漸進剪枝—恢復方法嘗試多輪縮小模型並保持推理能力。這與本文的重構式循環方向相似。

但即使平均推理分數保持，仍需檢查長尾、文化、多語、指令和主控能力是否選擇性退化。

---

## 12.4 模組化記憶

模組化記憶研究支持把持續學習的一部分放入可管理的外部系統。

本文進一步把記憶分為：

- 來源；
- 經驗；
- 認知原子；
- 因果圖；
- 能力史；
- 候選與接受知識。

---

## 12.5 發展式與學徒式 Agent

近期出現以逐步授權、技能成熟與人類方法內化為核心的數位學徒架構。這與本文的養成式及混合胚胎路線直接相近。

但養成式主 AI 的範圍更廣：它不只學習某位人類的工作方法，也要形成跨領域因果基底、外部模型治理與自身長期能力結構。

---

# 13. 與 GCMS 與認知原子因果基底的關係

GCMS 為三條形成路徑提供共同外部層：

$$
\mathcal M_{\mathrm{GCMS}}
=
\left(
\text{Source},
\text{Semantic},
\text{Episode},
\text{Atom},
\text{Candidate},
\text{Accepted}
\right).
$$

認知原子因果基底則提供：

$$
\mathcal G_A
=
\left(
V_A,
E_{\mathrm{causal}},
E_{\mathrm{scale}},
E_{\mathrm{constraint}},
E_{\mathrm{evidence}}
\right).
$$

重構式使用它們來保存被抽出的主控基底。

養成式使用它們來記錄逐步形成的能力和世界模型。

混合式使用它們來決定哪些能力值得內化、哪些繼續外部化。

---

# 14. 理論邊界與否證條件

若未來實驗顯示：

1. 通用模型的主控能力可被普通蒸餾完整保留；
2. 領域知識與判斷力幾乎完全可分離；
3. 長期形成史對修復、治理與泛化沒有實際價值；
4. 養成式 Agent 的成長斜率長期低於靜態大模型；
5. 外部記憶無法支撐可靠的長期連續；
6. 選擇性內化不能優於固定外部調用；
7. 混合胚胎的協調成本長期高於收益；
8. 自主性分級不能降低高風險失敗；
9. 不存在任何任務分布使養成或混合路徑優於重構或單體模型；

則本文的雙路形成命題應被縮小、修正或拒絕。

---

# 15. 結論

主 AI 的架構可以被簡單畫成：

$$
\text{主控核心}
+
\text{記憶}
+
\text{因果基底}
+
\text{子智能}.
$$

但真正困難的不是畫出模組，而是形成一個可以長期承擔主控角色的智能。

本文提出兩條基本形成路徑：

$$
\boxed{
\text{重構式主 AI}
=
\text{從龐大通用能力中提煉主控核心}.
}
$$

$$
\boxed{
\text{養成式主 AI}
=
\text{從持續核心中逐步長出能力結構}.
}
$$

以及一條較現實的中間道路：

$$
\boxed{
\text{混合胚胎式主 AI}
=
\text{通用能力胚胎}
+
\text{外部教師}
+
\text{長期記憶}
+
\text{選擇性內化}
+
\text{分級自主}.
}
$$

路線一的優勢是起點高，但它必須解開通用模型內部異常複雜的能力糾纏；路線二的優勢是形成史清楚、長期潛力大，但初期能力可能普通，且必須真正解決持續學習與記憶競爭。混合路徑不保證容易，只是把兩類困難重新分配到較可管理的時間尺度上。

因此，理論中的完整主 AI 很可能不是一次訓練完成的模型，而是：

$$
\boxed{
\text{一個經過長期形成、反覆重編譯、持續驗證並能調用外部智能的發展系統}.
}
$$

最終可以把三條路線概括為：

> **重構式主 AI 是被提煉出來的；養成式主 AI 是逐漸長成的；而最早真正可用的主 AI，可能是一個帶著通用能力出生、再以長期記憶與選擇性內化持續成長的混合認知胚胎。**

---

# 參考文獻

1. Zheng, J., et al. (2025). *Lifelong Learning of Large Language Model based Agents: A Roadmap*. arXiv:2501.07278.
2. Zheng, J., et al. (2025). *LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners*. arXiv:2505.11942.
3. Chen, H., et al. (2026). *Continual Learning in Large Language Models: Methods, Challenges, and Opportunities*. arXiv:2603.12658.
4. Dorovatas, V., et al. (2026). *Modular Memory is the Key to Continual Learning Agents*. arXiv:2603.01761.
5. Liu, J., et al. (2025). *Structured Agent Distillation for Large Language Model*. arXiv:2505.13820.
6. *UniComp: A Unified Evaluation of Large Language Model Compression*. arXiv:2602.09130.
7. *Gradually Compacting Large Language Models for Preserving Reasoning Capabilities*. arXiv:2602.04919.
8. *Understanding the Effects of LLM Compression on Large Reasoning Models*. arXiv:2504.02010.
9. *Continual Learning in LLM Agents Without Gradient Updates*. arXiv:2601.18510.
10. *When Continual Learning Moves to Memory: A Study of Memory-Augmented LLM Agents*. arXiv:2604.27003.
11. *Agent-Dice: Disentangling Knowledge Updates via Agentic Continual Learning*. arXiv:2601.03641.
12. *AgentCL: Toward Rigorous Evaluation of Continual Learning in Agents*. arXiv:2606.02461.
13. *The Digital Apprentice: A Framework for Human-Directed Developmental AI Agency*. arXiv:2606.04321.
14. *Nurture-First Agent Development: Building Domain-Expert Agents through Progressive Learning*. arXiv:2603.10808.
15. *AgentCollab: A Self-Evaluation-Driven Collaboration Framework*. arXiv:2603.26034.
16. Neo.K & Aletheia. (2026). *壓縮全局智能命題：後設完備主 AI 與按需展開子智能的分層代理架構*.
17. Neo.K & Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.
18. Neo.K. (2026). *認知解構學：形式定義與方法論 2.0*.
19. Neo.K & Aletheia. (2026). *GCMS v1.0 與《可繼承的認知》系列*.

---

# 附錄 A：一句話命題

> **完整主 AI 的形成至少存在兩條不同道路：從通用大模型中重構並提煉主控智能，或從持續核心中逐步養成主控智能；前者起點高但解構極難，後者起點普通但可能具有更大的長期結構潛力，而最現實的早期方案可能是二者之間的混合認知胚胎。**
