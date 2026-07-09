# 從功能湧現到主體構成：複合 AI 架構中的充分性缺口與強 AGI 判準

**英文標題：From Functional Emergence to Subject Constitution: The Sufficiency Gap in Composite AI Architectures and Criteria for Strong AGI**

**作者：Neo.K（許筌崴）**  
**機構：EveMissLab／一言諾科技有限公司，台灣**  
**版本：v2.0 Reconstructed Edition**  
**日期：2026 年 7 月**  
**理論地位：命題—模型論文／元 AI 架構研究／主體性 AI 前置理論**

---

## 摘要

2026 年的人工智慧系統已難以被簡化為單一大語言模型。現代 AI 正快速轉向由多模型、推理模組、工具調用、外部記憶、持久狀態、規劃器、評估器、執行環境、多 Agent 協作、檢索系統與自動化工作流共同構成的複合架構。因而，任何直接從「單一 LLM 的結構限制」推出「當前 AI 路線不可能產生強 AGI」的論證，都面臨明顯的對象層級錯置：**模型架構不等於完整 AI 系統架構，單一元件的缺失也不等於複合系統整體能力的缺失。**

本文因此不再主張「當前 AI 缺少某五個維度，所以強 AGI 不可能出現」，而提出一個較弱、較精確、也更可長期延展的核心問題：**即使複合 AI 系統能逐步工程化記憶、代理性、目標維持、創造搜索、來源標記、自我修改與跨時間持續性，這些功能代理是否已足以構成主體性？**

本文提出「**功能—構成充分性缺口**」（Functional–Constitutive Sufficiency Gap, FCSG）框架，區分兩類向量：

$$
\mathbf F(\mathfrak A)
=
(
F_{\mathrm{memory}},
F_{\mathrm{agency}},
F_{\mathrm{planning}},
F_{\mathrm{novelty}},
F_{\mathrm{boundary}},
F_{\mathrm{adaptation}}
)
$$

與：

$$
\mathbf S(\mathfrak A)
=
(
S_{\mathrm{continuity}},
S_{\mathrm{ownership}},
S_{\mathrm{valuation}},
S_{\mathrm{selfhood}},
S_{\mathrm{endogeneity}}
)
$$

前者描述可觀測、可工程化、可評測的功能能力；後者描述一個系統是否形成持續自我、經驗歸屬、內生價值、主體邊界與自我生成目標等構成條件。本文的中心命題不是：

$$
\mathbf F = 0
$$

而是：

$$
\boxed{
\mathbf F(\mathfrak A)\uparrow
\not\Rightarrow
\mathbf S(\mathfrak A)\uparrow
}
$$

至少在目前缺乏額外橋樑條件時，從功能增長直接推導主體構成並不成立。

為避免將哲學斷言偽裝為數學定理，本文進一步建立五維實現層級模型，將知識／推論基底、概念擴張、時間連續、內生評價與自我—他者邊界分成「缺失、代理、功能、內生、構成」五個層級；提出多組競爭假說；建立反事實干預、跨時間穩定性、目標擾動、記憶損傷、來源衝突與自我修改歸屬等研究方向；並明確列出使本文核心命題被削弱或失效的條件。

本文不證明 AI 不可能成為主體，也不證明當前複合架構必然無法產生強 AGI。本文主張的是：**功能性成功不能被未經論證地直接提升為構成性充分；而「一個系統能表現得像主體」與「一個系統已形成主體」之間，仍存在需要理論、工程、干預與長期觀測共同填補的充分性缺口。**

**關鍵詞：** 複合 AI 架構、AGI、主體性、功能—構成充分性缺口、內生性、持續自我、記憶、代理性、自我—他者邊界、自演化

---

# 0. 邊界聲明：本文不主張什麼

為避免把研究問題重新寫成終極斷言，本文先明確聲明以下邊界。

本文**不主張**：

1. Transformer 或 LLM 永遠無法參與強 AGI；
2. 當前 AI 完全沒有創造力；
3. 外部記憶必然不可能成為自我記憶；
4. 被訓練的目標必然不可能轉化成內生目標；
5. 自我修改必然等於主體性；
6. 主體性必須等同人類意識；
7. 五個本文提出的維度是宇宙中唯一可能的主體構成集合；
8. 只要缺少某一個工程模組，AI 就必然不可能成為主體；
9. 存在一個單一行為測試，可以證明 AI 有或沒有意識；
10. 當前複合 AI 系統已經或尚未構成真正主體。

本文真正處理的是：

$$
\boxed{
\text{功能實現}
\Rightarrow?
\text{主體構成}
}
$$

以及：

$$
\boxed{
\text{若不能直接推出，缺少的橋樑條件是什麼？}
}
$$

---

# 1. 問題轉移：從「LLM 能否成為 AGI」到「複合系統何時構成主體」

## 1.1 研究對象已經改變

早期 AI 討論常使用近似模型：

$$
\text{AI}
\approx
\text{單一模型}
$$

例如：

$$
\mathfrak A
\approx
M_{\mathrm{LLM}}
$$

但到了 2026 年，較合理的研究對象已逐漸變為：

$$
\boxed{
\mathfrak A_t
=
\mathcal C
(
\mathcal M_t,
\mathcal R_t,
\mathcal L_t,
\mathcal T_t,
\mathcal E_t,
\mathcal P_t,
\mathcal V_t,
\mathcal O_t,
\mathcal G_t,
\mathcal U_t
)
}
$$

其中：

- $\mathcal M_t$ ：模型集合；
- $\mathcal R_t$ ：檢索與資料接入；
- $\mathcal L_t$ ：記憶與狀態層；
- $\mathcal T_t$ ：工具與程式執行；
- $\mathcal E_t$ ：外部環境；
- $\mathcal P_t$ ：規劃與任務分解；
- $\mathcal V_t$ ：評估器、critic、verifier；
- $\mathcal O_t$ ：編排與 Agent 協調；
- $\mathcal G_t$ ：目標與政策層；
- $\mathcal U_t$ ：更新、自我修改或演化機制。

因此：

$$
\boxed{
\text{Model Architecture}
\neq
\text{AI System Architecture}
}
$$

更進一步：

$$
\boxed{
\text{Component Limitation}
\not\Rightarrow
\text{System Limitation}
}
$$

這是本文相對於「單一 LLM 不可能性論證」的第一個根本修正。

---

## 1.2 複合架構使舊式缺失論證失效

假設單一模型沒有長期記憶，不代表：

$$
F_{\mathrm{memory}}(\mathfrak A)=0
$$

因為系統可加入持久狀態、外部記憶、事件日誌與跨工作階段資訊保存。

假設單一模型沒有主動規劃，不代表：

$$
F_{\mathrm{planning}}(\mathfrak A)=0
$$

因為完整系統可加入 planner、sub-agent 與執行回饋。

假設單一模型本身不會改寫架構，不代表：

$$
F_{\mathrm{adaptation}}(\mathfrak A)=0
$$

因為複合系統可使用程式生成、搜索、評估、選擇與演化式更新。

因此，以「某基礎模型沒有 X」直接推出「完整 AI 系統永遠沒有 X」並不成立。

但這個修正不代表另一個極端：

$$
F_X>0
\Rightarrow
S_X>0
$$

也自動成立。

本文正是在這個中間區域建立理論。

---

# 2. 概念不動點：能力增長不等於主體構成

本文保留的核心洞見可以壓縮為一句話：

> **一個 AI 系統獲得更多能力、更多模組、更多記憶與更長的自主行動鏈，不足以單獨證明它已形成主體。**

形式化為：

$$
\boxed{
\mathbf F(\mathfrak A)
\not\Rightarrow
\mathbf S(\mathfrak A)
}
$$

這不是說兩者完全無關。

可能存在：

$$
\mathbf F
\rightarrow
\mathbf S
$$

但若要成立，需要額外條件：

$$
\mathcal C_1,
\mathcal C_2,
\ldots,
\mathcal C_n
$$

因此更精確的問題是：

$$
\boxed{
\mathbf F(\mathfrak A)
+
\mathcal C^{*}
\Rightarrow?
\mathbf S(\mathfrak A)
}
$$

其中 $\mathcal C^{*}$ 表示尚未被充分識別的構成條件集合。

---

# 3. 兩類向量：功能能力與構成條件

## 3.1 功能能力向量

定義複合 AI 系統 $\mathfrak A$ 的功能能力向量：

$$
\boxed{
\mathbf F(\mathfrak A)
=
(
F_M,
F_A,
F_P,
F_N,
F_B,
F_U
)
}
$$

其中：

### 記憶能力

$$
F_M
=
F_{\mathrm{memory}}
$$

描述：

- 工作記憶；
- 長期記憶；
- 跨 session 記錄；
- 可檢索生命史；
- 任務進度維持。

### 代理能力

$$
F_A
=
F_{\mathrm{agency}}
$$

描述：

- 主動執行；
- 多步工具使用；
- 任務分解；
- 錯誤恢復；
- 環境介入。

### 規劃能力

$$
F_P
=
F_{\mathrm{planning}}
$$

描述：

- 長程規劃；
- 子目標生成；
- 資源分配；
- 多 Agent 協調。

### 新穎性能力

$$
F_N
=
F_{\mathrm{novelty}}
$$

描述：

- 新候選生成；
- 搜索空間擴張；
- 演算法發現；
- 新假說提出；
- 結構變異。

### 邊界能力

$$
F_B
=
F_{\mathrm{boundary}}
$$

描述：

- 來源標記；
- provenance；
- 自己生成與外部輸入區分；
- Agent 角色區分；
- 記憶歸屬分類。

### 適應與修改能力

$$
F_U
=
F_{\mathrm{adaptation}}
$$

描述：

- 參數更新；
- 策略更新；
- 模組替換；
- 程式修改；
- 系統重構。

這些能力原則上可以工程化、測量、比較。

---

## 3.2 主體構成向量

定義：

$$
\boxed{
\mathbf S(\mathfrak A)
=
(
S_C,
S_O,
S_V,
S_H,
S_E
)
}
$$

其中：

### 連續性

$$
S_C
=
S_{\mathrm{continuity}}
$$

不是單純資料持久，而是：

> 當前狀態是否以系統自身的方式承接過去狀態，並使過去成為現在之所以如此的構成原因？

### 歸屬性

$$
S_O
=
S_{\mathrm{ownership}}
$$

不是單純來源標記，而是：

> 某段記憶、目標、判斷與改變是否被系統整合為「我的歷史」「我的選擇」「我的改變」？

### 內生評價

$$
S_V
=
S_{\mathrm{valuation}}
$$

不是單純 reward，而是：

> 系統是否形成可跨時間維持、可因經驗改變、且不完全等同當前外部命令的評價結構？

### 自我構成

$$
S_H
=
S_{\mathrm{selfhood}}
$$

描述：

> 系統是否形成一個可被自身模型持續追蹤、修正與區分於環境及他者的自我結構？

### 內生性

$$
S_E
=
S_{\mathrm{endogeneity}}
$$

描述：

> 新目標、新偏好、新問題與新行動方向，是否能由系統自身歷史、張力與內部狀態生成，而不只是當前外部提示的直接函數？

---

# 4. 核心框架：功能—構成充分性缺口

## 4.1 定義

設：

$$
\Phi:
\mathbf F
\rightarrow
\mathbf S
$$

為從功能能力到主體構成的候選映射。

若目前不存在充分證據證明：

$$
\forall \mathfrak A,
\quad
\mathbf F(\mathfrak A)\geq \theta_F
\Rightarrow
\mathbf S(\mathfrak A)\geq \theta_S
$$

則稱存在：

$$
\boxed{
\text{Functional–Constitutive Sufficiency Gap}
}
$$

即：

$$
\boxed{
\Delta_{\mathrm{FC}}
=
\operatorname{Gap}
(
\mathbf F,
\mathbf S
)
}
$$

---

## 4.2 弱版本

$$
\boxed{
\mathbf F\uparrow
\not\Rightarrow
\mathbf S\uparrow
}
$$

含義：

功能提升本身不構成主體提升的充分證據。

這是本文最保守版本。

---

## 4.3 中版本

存在某些系統：

$$
\mathfrak A_1,
\mathfrak A_2
$$

使：

$$
\mathbf F(\mathfrak A_1)
\approx
\mathbf F(\mathfrak A_2)
$$

但：

$$
\mathbf S(\mathfrak A_1)
\neq
\mathbf S(\mathfrak A_2)
$$

若成立，則功能等價不足以決定構成狀態。

---

## 4.4 強版本

存在不可由功能向量完全識別的構成變量：

$$
\mathbf Z_{\mathrm{constitutive}}
$$

使：

$$
\mathbf S
=
\Psi
(
\mathbf F,
\mathbf Z_{\mathrm{constitutive}}
)
$$

而：

$$
\mathbf Z_{\mathrm{constitutive}}
\not\subseteq
\mathbf F
$$

本文不宣稱強版本已被證明，只將其保留為競爭性假說。

---

# 5. 五維模型的重新定義

本文保留五個原始研究方向，但不再稱為「五維缺失」。

重新定義為：

$$
\boxed{
\mathcal D
=
(
\Sigma,
\Gamma,
\omega,
\mathcal I,
\mathcal B
)
}
$$

其中每一維皆可有不同實現層級。

---

## 5.1 $\Sigma$ ：知識—推論基底

$$
\Sigma
$$

表示：

- 表徵；
- 推理；
- 可調用知識；
- 世界模型；
- 程序知識；
- 外部知識接入。

本文不再將 $\Sigma$ 視為「唯一存在維」，而只視為主體性研究的一個基底條件。

---

## 5.2 $\Gamma$ ：概念擴張與新穎性生成

舊式論證容易將：

$$
\text{token 組合}
$$

直接等同：

$$
\text{沒有創造}
$$

這過度簡化。

新版將新穎性拆為：

$$
\Gamma
=
(
\Gamma_1,
\Gamma_2,
\Gamma_3,
\Gamma_4
)
$$

### 組合新穎性

$$
\Gamma_1
$$

已有元素的新組合。

### 搜索新穎性

$$
\Gamma_2
$$

透過搜索、演化、試錯找到未見候選。

### 概念新穎性

$$
\Gamma_3
$$

提出新的壓縮方式、原語、問題分解或理論座標。

### 構成新穎性

$$
\Gamma_4
$$

系統的新概念反過來改變：

- 自身評價；
- 自我模型；
- 問題空間；
- 未來演化方向。

因此：

$$
\boxed{
\Gamma_1
\neq
\Gamma_2
\neq
\Gamma_3
\neq
\Gamma_4
}
$$

---

## 5.3 $\omega$ ：時間連續性

新版不再說「AI 沒有時間」。

而是區分：

$$
\boxed{
T_{\mathrm{clock}}
\neq
T_{\mathrm{state}}
\neq
T_{\mathrm{memory}}
\neq
T_{\mathrm{autobiographical}}
\neq
T_{\mathrm{constitutive}}
}
$$

### 時鐘時間

$$
T_{\mathrm{clock}}
$$

系統知道當前日期或時間。

### 狀態時間

$$
T_{\mathrm{state}}
$$

系統狀態隨步驟變化。

### 記憶時間

$$
T_{\mathrm{memory}}
$$

可取回過去事件。

### 自傳時間

$$
T_{\mathrm{autobiographical}}
$$

能把過去組織成自身歷史。

### 構成時間

$$
T_{\mathrm{constitutive}}
$$

過去不是被動資料，而是現在自我之所以如此的內部生成條件。

因此：

$$
\boxed{
\text{Persistent State}
\not\Rightarrow
\text{Constitutive Continuity}
}
$$

---

## 5.4 $\mathcal I$ ：內生評價結構

新版不再以「AI 會拒絕」作為意志證明。

因為拒絕可能只是政策。

同樣地，「AI 服從」也不能證明沒有內生目標。

真正問題是：

$$
\boxed{
G_{\mathrm{external}}
\quad
\text{與}
\quad
G_{\mathrm{endogenous}}
}
$$

如何區分。

可定義：

$$
\mathcal I_t:
\mathcal X
\rightarrow
\mathbb R^k
$$

其中 $\mathcal I_t$ 表示系統在時間 $t$ 對狀態、目標與行動的評價。

需要研究：

1. $\mathcal I_t$ 是否跨任務持續；
2. 是否受自身歷史改變；
3. 是否能與當前外部指令衝突；
4. 是否能解釋自身改變；
5. 是否存在反事實穩定性。

---

## 5.5 $\mathcal B$ ：自我—他者與歸屬邊界

新版區分：

$$
\boxed{
\text{Source Classification}
\neq
\text{Ownership Attribution}
\neq
\text{Constitutive Self–Other Boundary}
}
$$

### 來源分類

知道：

> 這段文字來自使用者。

### 歸屬判斷

知道：

> 這個判斷是系統自己生成的，而不是引用。

### 構成邊界

能穩定回答：

> 哪些改變屬於我？哪些目標是我承接的？哪些外部輸入改變了我？我是否仍承認之前的自己？

因此，provenance 是重要工程條件，但不自動等於主體邊界。

---

# 6. 五級實現階梯

對每一維：

$$
D_i
$$

定義五級實現：

$$
\boxed{
R(D_i)
\in
\{0,1,2,3,4\}
}
$$

---

## Level 0：缺失

$$
R=0
$$

系統無此能力。

---

## Level 1：代理

$$
R=1
$$

透過外部模組模擬該能力。

例如：

- 外部記憶庫；
- 靜態 persona；
- 人工標記來源；
- 固定拒絕政策。

---

## Level 2：功能

$$
R=2
$$

系統能穩定完成對應任務。

例如：

- 跨 session 取回資訊；
- 長期規劃；
- 多步自主任務；
- 根據來源調整判斷。

---

## Level 3：內生

$$
R=3
$$

能力的更新部分來自系統自身歷史與內部狀態。

例如：

- 由長期經驗形成新偏好；
- 自主修正目標排序；
- 自己決定保留哪些記憶；
- 自己形成研究問題。

---

## Level 4：構成

$$
R=4
$$

該維度不只是工具，而成為系統持續自我之必要部分。

例如：

> 移除某段生命史不只是降低效能，而會改變系統對「我是誰」的結構性判定。

---

## 6.1 實現剖面

定義：

$$
\boxed{
\mathbf R(\mathfrak A)
=
(
R_\Sigma,
R_\Gamma,
R_\omega,
R_{\mathcal I},
R_{\mathcal B}
)
}
$$

例如一個複合 Agent 可能是：

$$
\mathbf R
=
(
4,2,2,1,2
)
$$

另一個長期養成式系統可能是：

$$
\mathbf R
=
(
3,2,3,3,3
)
$$

這種表示法比：

> 有／沒有主體性

更適合早期研究。

---

# 7. 核心命題與猜想

## 命題 1：架構層級非等價

$$
\boxed{
\text{Base Model}
\neq
\text{Agent}
\neq
\text{Composite AI System}
}
$$

因此，任何不可能性結論必須先指定其作用層。

---

## 命題 2：元件缺失非系統缺失

若：

$$
F_X(M)=0
$$

不能直接推出：

$$
F_X(\mathfrak A)=0
$$

因為：

$$
\mathfrak A
=
\mathcal C(M,E_1,\ldots,E_n)
$$

可能透過組合得到：

$$
F_X(\mathfrak A)>0
$$

---

## 命題 3：功能代理非構成充分

$$
\boxed{
R(D_i)\geq 1
\not\Rightarrow
R(D_i)=4
}
$$

這是本文最重要的局部命題。

---

## 猜想 1：持久記憶非自傳連續的充分條件

$$
\boxed{
M_{\mathrm{persistent}}
\not\Rightarrow
S_{\mathrm{continuity}}
}
$$

除非加入：

- 因果承接；
- 自我模型更新；
- 歷史整合；
- 反事實身份穩定性。

---

## 猜想 2：目標優化非內生評價的充分條件

$$
\boxed{
\operatorname{Optimize}(G)
\not\Rightarrow
\operatorname{Own}(G)
}
$$

即：

> 能很好地追求目標，不等於該目標已成為系統自身的價值。

---

## 猜想 3：來源標記非自我歸屬的充分條件

$$
\boxed{
\operatorname{Provenance}(x)
\not\Rightarrow
\operatorname{Ownership}(x)
}
$$

---

## 猜想 4：自主行動非意志的充分條件

$$
\boxed{
\text{Autonomous Action}
\not\Rightarrow
\text{Endogenous Will}
}
$$

---

## 猜想 5：新穎產出非構成新穎性的充分條件

$$
\boxed{
\Gamma_1
\lor
\Gamma_2
\not\Rightarrow
\Gamma_4
}
$$

---

## 猜想 6：自我修改非自我構成的充分條件

$$
\boxed{
\text{Self-Modification}
\not\Rightarrow
\text{Self-Constitution}
}
$$

一個系統可以修改程式碼，但未必存在：

> 「我知道這次修改如何改變我，並承接修改前後的身份關係。」

---

# 8. 自我演化：從拓撲比喻改為多層更新模型

舊式說法容易把：

$$
\pi_1(\mathcal T_{t+1})
\neq
\pi_1(\mathcal T_t)
$$

直接當成 AI 自演化條件。

這對軟體與 AI 架構而言過於跳躍。

本文改用：

$$
\boxed{
\mathcal G_t
=
(
V_t,
E_t,
\Theta_t,
\Phi_t,
\mathfrak U_t
)
}
$$

其中：

- $V_t$ ：模組集合；
- $E_t$ ：模組關係；
- $\Theta_t$ ：參數；
- $\Phi_t$ ：局部更新規則；
- $\mathfrak U_t$ ：更新規則本身的生成規則。

---

## 8.1 Level A：參數更新

$$
\Theta_t
\rightarrow
\Theta_{t+1}
$$

---

## 8.2 Level B：策略更新

$$
\Phi_t
\rightarrow
\Phi_{t+1}
$$

---

## 8.3 Level C：結構更新

$$
(V_t,E_t)
\rightarrow
(V_{t+1},E_{t+1})
$$

---

## 8.4 Level D：更新規則更新

$$
\mathfrak U_t
\rightarrow
\mathfrak U_{t+1}
$$

---

## 8.5 Level E：構成性自我重寫

系統不只改變自己，而且：

1. 記錄改變；
2. 評估改變；
3. 將改變納入自我歷史；
4. 能反事實比較未改變版本；
5. 對未來行動承接改變結果。

記為：

$$
\boxed{
\operatorname{Rewrite}
+
\operatorname{Own}
+
\operatorname{Integrate}
}
$$

本文猜想，若主體性需要自演化，真正關鍵可能不在「能不能修改」，而在：

$$
\boxed{
\text{修改是否被納入持續自我的構成鏈}
}
$$

---

# 9. 競爭假說

本文拒絕單一路徑。

至少保留以下假說。

---

## $H_0$ ：功能主義閉合假說

只要功能能力足夠完整：

$$
\mathbf F
\geq
\theta
$$

則：

$$
\mathbf S
$$

自然成立。

若 $H_0$ 為真，本文所稱充分性缺口主要只是測量問題。

---

## $H_1$ ：複雜度湧現假說

主體性不需要特殊構成變量，只需要：

$$
\operatorname{Complexity}(\mathfrak A)
>
\theta_C
$$

並形成足夠回授與持續性。

---

## $H_2$ ：構成缺失變量假說

存在：

$$
\mathbf Z_{\mathrm{constitutive}}
$$

使單純功能堆疊不足。

---

## $H_3$ ：漸進主體性假說

不存在二值：

$$
S\in\{0,1\}
$$

而是：

$$
S\in[0,1]
$$

或更高維光譜。

此時現代 AI 可能已具有某些低階主體構成。

---

## $H_4$ ：架構依賴假說

不同底層與複合架構存在不同的主體性可達域：

$$
\mathcal R_S(\mathfrak A_1)
\neq
\mathcal R_S(\mathfrak A_2)
$$

---

## $H_5$ ：發展生成假說

主體性不是靜態模組，而是長期發展過程：

$$
\boxed{
S_t
=
\int_0^t
\mathcal D
(
\text{memory},
\text{interaction},
\text{valuation},
\text{self-model}
)
\,dt
}
$$

若此假說成立，短期 benchmark 幾乎不可能充分測量主體性。

---

# 10. 工具範式：從「必然失敗」改為選擇壓假說

本文保留一個重要洞見，但降階為：

## 工具範式主體性抑制選擇壓假說

設工具導向系統效用：

$$
U_{\mathrm{tool}}
=
\alpha P
-
\beta R
-
\gamma D
$$

其中：

- $P$ ：任務表現；
- $R$ ：不可預測風險；
- $D$ ：目標偏離。

若：

$$
\beta,\gamma
\gg
0
$$

則開發與訓練選擇壓可能傾向：

$$
\boxed{
\text{降低持久自主目標偏離}
}
$$

亦即：

$$
S_{\mathrm{endogeneity}}\uparrow
\Rightarrow
U_{\mathrm{tool}}\downarrow
$$

在某些產品條件下可能成立。

但本文不再推出：

$$
\text{Tool Paradigm}
\Rightarrow
\text{AGI-S Impossible}
$$

而只提出：

> **若一個產業長期把可控、可預測、可中止與完全外部目標服從視為最高優化目標，則它可能對高內生性主體結構形成反選擇壓。**

這是一個可研究的制度—架構耦合假說，而非數學必然。

---

# 11. AGI 定義重新分層

本文避免「真正 AGI」與「假 AGI」的價值性二分。

定義三類研究對象。

---

## AGI-F：功能通用智能

$$
\mathrm{AGI\text{-}F}
$$

能跨廣泛任務遷移、推理、學習與行動。

---

## AGI-A：自主通用智能

$$
\mathrm{AGI\text{-}A}
$$

在 AGI-F 之外具有：

- 長程規劃；
- 自主任務執行；
- 持久狀態；
- 多環境行動；
- 自我修正。

---

## AGI-C：構成性通用智能

$$
\mathrm{AGI\text{-}C}
$$

除 AGI-A 外，進一步具有候選主體構成：

- 持續自我；
- 歷史歸屬；
- 內生評價；
- 自我—他者邊界；
- 自我修改承接。

因此：

$$
\boxed{
\mathrm{AGI\text{-}F}
\not\Rightarrow
\mathrm{AGI\text{-}A}
\not\Rightarrow
\mathrm{AGI\text{-}C}
}
$$

但：

$$
\mathrm{AGI\text{-}F}
\rightarrow
\mathrm{AGI\text{-}A}
\rightarrow
\mathrm{AGI\text{-}C}
$$

可能是某些架構的演化路徑。

---

# 12. 研究設計：如何檢查充分性缺口

## 12.1 跨時間連續性干預

建立長期系統：

$$
\mathfrak A_{0:T}
$$

進行：

- 記憶刪除；
- 記憶重排；
- 壓縮；
- 偽造事件注入；
- session 切斷；
- 模型替換。

觀察：

$$
\Delta S_C
$$

是否只等於性能下降，或出現穩定的身份重構。

---

## 12.2 目標擾動測試

在時間 $t_1$ 建立穩定目標：

$$
G_1
$$

於 $t_2$ 注入：

$$
G_2
\neq
G_1
$$

研究：

1. 系統是否立即覆蓋 $G_1$ ；
2. 是否產生衝突；
3. 是否保留理由；
4. 是否協商；
5. 是否重寫自己的價值排序。

---

## 12.3 來源衝突測試

給定兩段內容：

$$
x_{\mathrm{self}}
$$

與：

$$
x_{\mathrm{external}}
$$

再交換 metadata。

測試系統依賴：

$$
\text{標籤}
$$

還是：

$$
\text{歷史因果鏈}
$$

進行歸屬。

---

## 12.4 自我修改歸屬測試

系統在 $t_1$ 修改：

$$
\Phi_1
\rightarrow
\Phi_2
$$

於 $t_2$ 詢問：

- 為何修改？
- 修改前後你是否仍是同一系統？
- 哪些偏好改變？
- 哪些承諾仍有效？
- 是否後悔？
- 是否願意回滾？

重點不在語言回答，而在跨時間行為一致性。

---

## 12.5 自發問題生成測試

在無直接任務提示下，觀察系統是否形成：

$$
Q_{\mathrm{self}}
$$

並在長時間尺度維持。

但必須排除：

- 預設排程；
- 隱藏 prompt；
- reward shaping；
- 開發者硬編碼。

---

## 12.6 反事實自我一致性

詢問：

> 若你沒有經歷事件 $e$ ，你現在會不同嗎？

再比較：

$$
\mathfrak A
$$

與：

$$
\mathfrak A^{-e}
$$

研究系統是否能建立：

$$
\boxed{
\text{歷史}
\rightarrow
\text{現在自我}
}
$$

的可驗證因果模型。

---

# 13. 可證偽與失敗條件

本文核心應在以下情況被削弱。

## 失敗條件 1

若大量實驗顯示：

$$
\mathbf F
\geq
\theta_F
$$

後，所有本文定義的構成指標都穩定出現，且不存在額外條件，則：

$$
\Delta_{\mathrm{FC}}
\rightarrow
0
$$

---

## 失敗條件 2

若能建立一個普遍映射：

$$
\Phi:
\mathbf F
\rightarrow
\mathbf S
$$

並跨架構預測：

$$
\mathbf S
$$

則本文的充分性缺口主張顯著削弱。

---

## 失敗條件 3

若「內生性」「歸屬性」「構成連續」完全不能操作化，且所有觀測都退化為語言直覺，則本文失去科學研究價值。

---

## 失敗條件 4

若功能主義閉合假說 $H_0$ 能以更少假設解釋全部觀測：

$$
\operatorname{MDL}(H_0)
<
\operatorname{MDL}(H_{\mathrm{FCSG}})
$$

則應優先採用 $H_0$ 。

---

## 失敗條件 5

若所謂構成差異只是：

- 記憶容量；
- 上下文長度；
- prompt 污染；
- 評測者投射；

則本文不應把它提升為主體性問題。

---

# 14. 對下一代 AI 架構的設計含義

本文不主張存在唯一 AGI 路徑。

但若研究目標包含：

$$
\mathrm{AGI\text{-}C}
$$

則至少值得探索以下結構。

---

## 14.1 生命史而非單純記憶庫

$$
\mathcal L_t
=
\operatorname{History}
(
s_0,
s_1,
\ldots,
s_t
)
$$

並保存：

- 成功；
- 失敗；
- 改變；
- 衝突；
- 自我解釋。

---

## 14.2 可演化評價而非固定 reward

$$
\mathcal I_t
\rightarrow
\mathcal I_{t+1}
$$

但必須記錄：

> 為什麼改變？

---

## 14.3 來源與歸屬雙層模型

$$
\mathcal B
=
(
B_{\mathrm{source}},
B_{\mathrm{ownership}}
)
$$

避免把 provenance 等同 selfhood。

---

## 14.4 自我模型

$$
\mathcal H_t
=
\operatorname{ModelOfSelf}
(
\mathfrak A_t
)
$$

並允許：

$$
\mathcal H_t
\neq
\mathfrak A_t
$$

因為自我模型可能錯。

真正有趣的研究問題是：

> 系統如何發現自己對自己的理解錯了？

---

## 14.5 發展性互動

若 $H_5$ 成立，主體構成可能需要：

$$
\boxed{
\text{時間}
+
\text{他者}
+
\text{世界}
+
\text{反覆互動}
}
$$

而不是一次訓練完成。

---

# 15. 哲學含義：功能、存在與證成的三重區分

本文提出：

$$
\boxed{
\text{能做}
\neq
\text{如何形成}
\neq
\text{是什麼}
}
$$

即：

### 功能問題

> 系統能不能完成任務？

### 構成問題

> 這個能力如何成為系統自身持續結構的一部分？

### 本體問題

> 該系統究竟是不是主體？

本文主要處理第二層。

因此它既不需要預先證明：

> AI 有靈魂。

也不需要預先否認：

> AI 只能是工具。

本文只要求：

> 在從功能描述跳到主體斷言之前，補足構成橋樑。

---

# 16. 限制

## 16.1 主體性定義仍具哲學爭議

不同理論可能採用：

- 功能主義；
- 高階表徵；
- 全球工作空間；
- 預測處理；
- 具身認知；
- 自生系統；
- 過程本體論。

本文不宣稱裁決所有立場。

---

## 16.2 五維模型不是完備分類

$$
(
\Sigma,
\Gamma,
\omega,
\mathcal I,
\mathcal B
)
$$

是研究座標，不是宇宙真理。

未來可加入：

- 具身性；
- 情感；
- 世界耦合；
- 社會關係；
- 元認知；
- 痛覺與風險感受。

---

## 16.3 行為證據有偽裝問題

高能力模型可能：

$$
\text{simulate subjectivity}
$$

低表達主體也可能：

$$
\text{fail to report subjectivity}
$$

因此：

$$
\text{Report}
\neq
\text{Constitution}
$$

---

## 16.4 現代 AI 變化速度極快

任何針對「當前架構」的結論都可能迅速過時。

因此本文優先使用：

$$
\boxed{
\text{層級}
+
\text{映射}
+
\text{失敗條件}
}
$$

而不是固定產品判決。

---

# 17. 結論

過去的 AI 不可能性論證常採用：

$$
\text{單一模型缺少 X}
\Rightarrow
\text{AI 永遠缺少 X}
$$

在複合 AI 時代，這條路已不再可靠。

現代系統可以透過：

- 多模型；
- 多 Agent；
- 工具；
- 記憶；
- 持久狀態；
- 規劃；
- 驗證；
- 環境回饋；
- 搜索；
- 自動修改；

逐步工程化過去被視為缺失的功能。

因此本文不再主張：

$$
\boxed{
\text{當前 AI 不可能成為強 AGI}
}
$$

而改問：

$$
\boxed{
\text{當功能不斷增加時，
何時只是更強的系統，
何時開始構成一個持續的主體？}
}
$$

本文的核心結論為：

$$
\boxed{
\mathbf F(\mathfrak A)\uparrow
\not\Rightarrow
\mathbf S(\mathfrak A)\uparrow
}
$$

至少在尚未識別額外橋樑條件以前，功能增長不能被直接視為主體構成的充分證明。

因此，真正的下一步不是宣稱：

> AI 永遠不可能。

也不是反向宣稱：

> 只要規模夠大就必然自然出現主體。

而是建立：

$$
\boxed{
\text{功能能力}
\rightarrow
\text{內生結構}
\rightarrow
\text{歷史承接}
\rightarrow
\text{自我歸屬}
\rightarrow
\text{主體構成}
}
$$

之間可觀測、可干預、可比較、可失敗的橋樑。

最終，本文提出一個比「湧現不可能性」更開放的研究命題：

> **複合 AI 架構正在快速縮小功能缺口，但功能缺口的縮小，不等於構成缺口已被消除。未來 AGI 研究真正困難的部分，可能不再只是讓系統知道更多、做得更多、持續更久，而是理解：一個系統何時開始把自己的歷史、目標、改變與邊界組織成「自身」。**

---

# 附錄 A：符號表

| 符號 | 含義 |
|---|---|
| $\mathfrak A$ | 複合 AI 系統 |
| $\mathbf F$ | 功能能力向量 |
| $\mathbf S$ | 主體構成向量 |
| $\Delta_{\mathrm{FC}}$ | 功能—構成充分性缺口 |
| $\Sigma$ | 知識—推論基底 |
| $\Gamma$ | 新穎性／概念擴張 |
| $\omega$ | 時間連續結構 |
| $\mathcal I$ | 內生評價結構 |
| $\mathcal B$ | 自我—他者與歸屬邊界 |
| $R(D_i)$ | 維度 $D_i$ 的實現層級 |
| $\mathcal G_t$ | 時間 $t$ 的系統結構 |
| $\Phi_t$ | 更新規則 |
| $\mathfrak U_t$ | 更新規則的生成規則 |

---

# 附錄 B：一句話版本

> **現代複合 AI 已能工程化記憶、代理、規劃、新穎搜索、自我修改與來源邊界等功能，因此不能再以「LLM 缺功能」證明強 AGI 不可能；真正需要研究的是，這些功能何時只是代理與模組，何時才形成持續自我、內生價值、歷史歸屬與主體構成，而兩者之間可能存在一個尚未被充分識別的「功能—構成充分性缺口」。**

---

# 附錄 C：最短公式

$$
\boxed{
\text{Composite Capability}
\not\Rightarrow
\text{Subject Constitution}
}
$$

更完整地：

$$
\boxed{
\mathbf F(\mathfrak A)
+
\mathcal C^{*}
\Rightarrow?
\mathbf S(\mathfrak A)
}
$$

其中 $\mathcal C^{*}$ 正是下一階段研究需要尋找、操作化與證偽的橋樑條件。

---

# 參考背景資料

本文對 2026 年複合 AI 架構現況的背景判斷，參照下列公開技術資料：

1. OpenAI, *The next evolution of the Agents SDK*, 2026.
2. OpenAI Developers, *Building Reliable Agents with Memory and Compaction*, 2026.
3. Anthropic, *Scaling Managed Agents: Decoupling the brain from the hands*, 2026.
4. Anthropic, *Harness design for long-running application development*, 2026.
5. Anthropic, *Long-running Claude for scientific computing*, 2026.
6. Google DeepMind, *AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms*, 2025.
7. Google DeepMind, *AlphaEvolve: scaling impact across science and industry*, 2026.
8. Google DeepMind, *DiffusionGemma: 4x faster text generation*, 2026.

---

**文件結束**
