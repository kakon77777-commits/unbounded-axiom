# CCAW-03｜外部執行因果與內生因果：世界自主性的真正分界

## ——從 Runtime Dependency 到 Operational Causal Closure 的世界因果架構

**系列：** 造物主、因果與自治宇宙統合系列（Creator, Causality & Autonomous Worlds Integration Series, CCAW）  
**篇次：** 03 / 10  
**文件編號：** EML-CCAW-03-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-20  
**版本：** v0.1 Canonical Integration Draft  
**文件性質：** 理論整合論文／命題猜想框架／世界因果架構／自治世界理論  
**證據狀態：** 形式化概念框架為主；自組織、反應—擴散、物理計算與因果自主性文獻僅作邊界與類比支持；本文不宣稱存在已知的自主 child universe，也不把因果閉合等同於形上學終極閉合

---

## 摘要

CCAW-02 將世界生成拆分為 World Substrate Axis 與 Causal Autonomy Axis，指出 digital、analogue、quantum、effective、physical-native 等載體類型與世界自主性不是同一維度。本文進一步提出：世界自主性的真正核心，不在於「創造者是否很少干涉」，也不在於「世界是不是物理的」，而在於世界歷史的因果更新究竟由誰執行。

本文定義兩類理想型。第一類是外部執行因果（Externally Executed Causality, EEC）：世界下一狀態必須由 parent runtime、外部 scheduler、全域 controller 或其他世界外部機制持續計算、選擇或提交。第二類是內生因果（Endogenous Causality, EC）：一旦世界被合法實例化，其主要狀態演化由世界內部的局部規則、物理耦合、Agent 行動、資源交換、回饋迴路與 meta-dynamics 共同產生，而不是由 creator 對每一個後繼狀態進行逐步指定。

本文進一步區分三種常被混淆的依賴：資源依賴（resource dependence）、執行依賴（execution dependence）與治理依賴（governance dependence）。一個系統可能高度依賴外部能源，卻不代表其內部因果由能源提供者「計算」；反之，一個數位世界即使具有獨立硬體與能源供給，其每一步仍可能完全依賴外部 runtime。由此本文提出：

$$
\boxed{
\text{External Support}
\not\Rightarrow
\text{External Causal Execution}.
}
$$

本文建立 Operational Causal Closure（OCC，操作性因果閉合）作為非形上學、可分級的世界自治概念。OCC 不要求世界與外界完全隔絕，而要求在指定世界邊界與時間尺度下，大多數合法狀態轉移具有可追溯的世界內部因果來源，且 creator 不需要成為每一步歷史的必要執行器。

本文最後提出一個關鍵轉換：

$$
\boxed{
\text{Creator-managed history}
\longrightarrow
\text{world-generated history}.
}
$$

如果此轉換可以被工程化，則高階造物主的能力不必表現為持續全域控制；更高階的能力反而可能是建立一個具有足夠因果閉合、自我調節與局部生成能力的世界，使 creator 可以退出日常 runtime，而世界仍能繼續形成自己的歷史。此結果為 CCAW-04 的「造物主編譯：Runtime Intelligence $\rightarrow$ Seed Intelligence」建立直接形式基礎。

---

## 關鍵詞

外部執行因果；內生因果；Operational Causal Closure；OCC；Runtime Dependency；世界自主性；因果來源；自組織；Creator Non-Determination；世界生成；局部規則；因果閉合；Creator Withdrawal；Seed Autonomy；世界歷史

---

# 一、問題轉向：世界自主不是「造物主有沒有出手」

直覺上，人們可能把「自主世界」理解為：

> creator 很少干涉。

但這不足以判定真正的 autonomy。

考慮一個數位世界：

$$
W_t.
$$

creator 從不手動修改角色、不刪除記憶、不改政策，看起來十分克制。

然而若世界下一狀態仍然需要：

$$
R_{\mathrm{parent}}
$$

執行：

$$
W_{t+1}
=
R_{\mathrm{parent}}(W_t),
$$

那麼 creator 即使完全不「手動」介入，世界仍然不是在因果上獨立推進。

換言之：

$$
\boxed{
\text{Low Intervention}
\not\Rightarrow
\text{High Causal Autonomy}.
}
$$

相反地，一個世界可能偶爾受到外界作用，但其大部分日常歷史仍由內部因果生成。

因此真正問題不是：

> creator 有沒有碰它？

而是：

$$
\boxed{
\text{Who or what executes the causal transition?}
}
$$

---

# 二、兩種理想型

本文定義：

$$
\mathsf{EEC}
=
\text{Externally Executed Causality},
$$

以及：

$$
\mathsf{EC}
=
\text{Endogenous Causality}.
$$

## 2.1 外部執行因果

對世界 $W$，若大多數狀態轉移必須經由世界外部 executor $R$：

$$
W_{t+1}
=
R(W_t,\Theta_R),
$$

且若：

$$
R\downarrow
$$

則：

$$
\Delta W=0,
$$

則世界具有高 external execution dependence。

典型例：

- query-triggered simulation；
- game loop；
- externally clocked cellular automaton；
- server-side persistent world；
- scheduler-driven multi-agent simulation；
- creator-controlled turn resolver。

## 2.2 內生因果

若世界被實例化後，其主要演化可表示為：

$$
W_{t+\Delta t}
=
\Phi_W
\left(
W_t,
\Lambda_W,
\Xi_t
\right),
$$

其中：

- $\Lambda_W$ 是世界內部可用的規則／物理律；
- $\Xi_t$ 是內生局部交互作用與合法外界輸入；
- $\Phi_W$ 的執行不要求 creator 為每個後繼狀態作逐步選擇；

則世界具有較高 endogenous causality。

---

# 三、不要把「外部資源」誤認成「外部因果執行」

這是本文最重要的修正之一。

任何現實系統都可能依賴外部資源。

例如：

$$
\text{Organism}
\leftarrow
\text{Energy},
$$

$$
\text{Ecosystem}
\leftarrow
\text{Solar Flux},
$$

$$
\text{Computer}
\leftarrow
\text{Electricity}.
$$

但能源供應不代表能源提供者決定每個內部狀態。

因此定義三種不同依賴。

## 3.1 Resource Dependence

$$
D_{\mathrm{res}}(W).
$$

世界持續存在需要多少外部能量、物質、記憶體、空間、熱耗散或其他資源。

## 3.2 Execution Dependence

$$
D_{\mathrm{exe}}(W).
$$

世界狀態轉移需要多少外部 executor 逐步計算或提交。

## 3.3 Governance Dependence

$$
D_{\mathrm{gov}}(W).
$$

世界維持秩序、修復錯誤、分配權限與處理危機，需要多少外部治理。

因此：

$$
\boxed{
D_{\mathrm{res}}
\neq
D_{\mathrm{exe}}
\neq
D_{\mathrm{gov}}.
}
$$

---

# 四、最關鍵的反例

假設世界 $W_A$：

- 需要 parent universe 提供能量；
- 需要邊界交換物質；
- 但內部因果由自身物理 dynamics 執行。

則可能：

$$
D_{\mathrm{res}}(W_A)\gg0,
$$

但：

$$
D_{\mathrm{exe}}(W_A)\approx0.
$$

另一個世界 $W_B$：

- 有獨立電源；
- 有專用 server；
- creator 永不手動干預；
- 但每一步 state transition 都由外部 runtime 計算。

則：

$$
D_{\mathrm{res}}(W_B)
$$

可以很低或穩定，但：

$$
D_{\mathrm{exe}}(W_B)\gg0.
$$

所以：

$$
\boxed{
\text{Infrastructure Independence}
\not\Rightarrow
\text{Causal Independence}.
}
$$

---

# 五、Causal Executor：誰在推進世界？

本文引入：

$$
\mathcal E_C(W,t)
$$

表示時刻 $t$ 對世界合法後繼狀態產生必要作用的 causal executor set。

若：

$$
\mathcal E_C(W,t)
=
\{R_{\mathrm{parent}}\},
$$

則世界高度依賴外部 executor。

若：

$$
\mathcal E_C(W,t)
\subseteq
W,
$$

則該步主要由 world-internal dynamics 產生。

更一般地：

$$
\mathcal E_C(W,t)
=
\mathcal E_{\mathrm{in}}
\cup
\mathcal E_{\mathrm{out}}.
$$

因此 autonomy 並非二元。

真正要問：

$$
\boxed{
\frac{
|\mathcal E_{\mathrm{out}}|
}{
|\mathcal E_{\mathrm{in}}|+|\mathcal E_{\mathrm{out}}|
}
}
$$

在何種語義與尺度下足以代表依賴。

本文不把上式直接宣告為唯一精確度量，只把它作為第一版 operational heuristic。

---

# 六、Runtime Dependency Ratio

定義：

$$
\rho_R(W;\tau)
=
\frac{
N_{\mathrm{external\ execution}}(\tau)
}{
N_{\mathrm{causal\ transitions}}(\tau)
}.
$$

其中 $\tau$ 為觀察區間。

理想型：

$$
\rho_R\rightarrow1
$$

表示世界幾乎完全由外部 runtime 執行。

而：

$$
\rho_R\rightarrow0
$$

表示大部分狀態轉移不需要 creator-side runtime 作逐步 executor。

但此比例必須小心。

如果一個外部 clock pulse 同時推動一億個內部局部作用，不能簡單以事件數把 autonomy 高估。

因此後續可加入權重：

$$
\rho_R^{(w)}
=
\frac{
\sum_i w_i^{\mathrm{out}}
}{
\sum_i w_i^{\mathrm{all}}
}.
$$

其中 $w_i$ 代表某 causal transition 的結構重要性。

---

# 七、Clock Dependence 與 State Dependence 也要分開

一個系統可能需要外部 clock：

$$
c_t,
$$

但後繼狀態仍由內部 rule 決定：

$$
x_{t+1}
=
F_W(x_t)
\quad
\text{when }c_t=1.
$$

這與外部直接選擇：

$$
x_{t+1}
=
F_R(x_t)
$$

不同。

因此：

$$
D_{\mathrm{clock}}
\neq
D_{\mathrm{state}}.
$$

同樣，外部提供時間參數不必然意味外部決定歷史內容。

這一點對未來 digital-physical hybrid world 特別重要。

---

# 八、Law Dependence：規則是誰的？

又有另一層：

$$
D_{\mathrm{law}}(W).
$$

即世界普通狀態雖由自身執行，但規則是否必須由 creator 持續提供或更新。

例如：

$$
W_{t+1}
=
F_{\theta_t}(W_t),
$$

其中：

$$
\theta_t
=
G_{\mathrm{creator}}(t).
$$

此時 state execution 可以局部自治，但 law evolution 仍高度外部化。

因此真正高 autonomy 不能只檢查：

$$
\text{state autonomy}.
$$

還要檢查：

$$
\text{law autonomy}
$$

與：

$$
\text{meta-law autonomy}.
$$

---

# 九、三層因果執行

本文將 world causality 分為：

## 9.1 State Causality

$$
x_t\rightarrow x_{t+1}.
$$

## 9.2 Rule Causality

$$
F_t\rightarrow F_{t+1}.
$$

## 9.3 Meta-Rule Causality

$$
\mathcal M_t
\rightarrow
\mathcal M_{t+1},
$$

其中 $\mathcal M$ 決定規則如何更新、生成、競爭或被淘汰。

因此：

$$
\boxed{
\text{Autonomous state evolution}
\not\Rightarrow
\text{autonomous law evolution}.
}
$$

這會直接連到 CCAW-04 的 Seed Intelligence。

---

# 十、內生因果不是沒有邊界

本文不使用：

$$
\text{causal closure}
=
\text{complete isolation}.
$$

任何高度自治世界仍可能具有：

$$
\Gamma_{\mathrm{in}}
:
E\rightarrow W,
$$

以及：

$$
\Gamma_{\mathrm{out}}
:
W\rightarrow E.
$$

例如能量、物質、信息、觀測、碰撞或邊界條件交換。

因此本文提出：

# Operational Causal Closure

簡稱：

$$
\mathrm{OCC}.
$$

其核心不是：

> 世界與外界完全沒有因果關係。

而是：

> 在指定邊界、尺度與觀察窗口下，世界合法歷史的大部分生成機制可以由世界內部可追溯因果鏈閉合，而不需要外部 creator 成為逐狀態 executor。

---

# 十一、OCC 的最低條件

令世界邊界為：

$$
\partial W.
$$

對內部事件 $e_t$，若存在 causal ancestry：

$$
\operatorname{Anc}_W(e_t)
$$

主要落在：

$$
W\cup\partial W,
$$

並且外部輸入可以被表示成合法 boundary input：

$$
u_t\in\mathcal U_{\partial W},
$$

則事件可以保持 OCC。

因此：

$$
\boxed{
\text{External input}
\not\Rightarrow
\text{OCC violation}.
}
$$

真正破壞 OCC 的，是世界內部無法以既有 boundary semantics 接受的外部 state assignment、rule overwrite 或超出世界規則的 causal injection。

---

# 十二、OCC 不等於形上學閉合

本文明確拒絕：

$$
\mathrm{OCC}(W)
\Rightarrow
\text{MetaphysicalClosure}(W).
$$

OCC 只是工程／模型判準。

它回答：

> 世界是否足以在指定操作尺度上自行生成歷史？

它不回答：

- 世界是不是終極本體；
- 是否存在更高層宇宙；
- 是否存在第一因；
- 世界是否絕對封閉；
- 是否存在超自然作用。

因此：

$$
\boxed{
\mathrm{OCC}
=
\text{operational autonomy criterion},
}
$$

而不是神學結論。

---

# 十三、OCC 分級

本文提出第一版：

$$
K_0\rightarrow K_5.
$$

## $K_0$：No Causal Closure

所有下一步由外部 query 或 controller 指定。

## $K_1$：Local Transition Closure

局部狀態可依內部規則更新，但 clock、resources、law 與 repair 高度外部依賴。

## $K_2$：Persistent Process Closure

世界可持續演化，但遇到一般擾動時仍常需外部修復。

## $K_3$：Self-Regulating Closure

內部具有回饋、適應、資源調節與錯誤吸收。

## $K_4$：Law-Adaptation Closure

部分 ordinary law、policy 或 institutional rule 可以由世界內部合法機制更新。

## $K_5$：Seed-Level Operational Closure

初始 seed 完成後，世界在很長時間尺度下可以：

- 持續；
- 自我調節；
- 形成新結構；
- 生成歷史；
- 產生 local governance；
- 在 bounded conditions 下更新規則；

而不需要 creator 成為持續 runtime。

---

# 十四、自組織提供的不是「造物主不存在」，而是「全域控制不必存在」

經典自組織研究的一個重要啟示是：

$$
\text{global pattern}
$$

可以由：

$$
\text{local interaction rules}
$$

生成。

Turing 的 reaction-diffusion model 是清楚例子之一：

$$
\frac{\partial u}{\partial t}
=
D_u\nabla^2u+f(u,v),
$$

$$
\frac{\partial v}{\partial t}
=
D_v\nabla^2v+g(u,v).
$$

局部反應與擴散可以形成宏觀 pattern，而不需要一個外部 controller 每一刻指定每個位置的最終圖樣。

這不能證明宇宙具有完全 endogenous causality。

但它證明一個較弱且重要的命題：

$$
\boxed{
\text{Global Structure}
\not\Rightarrow
\text{Global Step-by-Step Controller}.
}
$$

---

# 十五、內生因果與湧現

若世界內存在：

$$
\{a_1,\ldots,a_n\},
$$

各自遵守局部作用：

$$
a_i(t+1)
=
f_i
\left(
a_i(t),
N_i(t)
\right),
$$

則全域狀態：

$$
W_{t+1}
$$

可以形成 creator 沒有逐項指定的宏觀結構。

因此：

$$
\boxed{
\text{Creator specifies local generative conditions}
\not\Rightarrow
\text{Creator specifies every emergent macrostate}.
}
$$

這正是 Creator Non-Determination 的第一個形式來源。

---

# 十六、但不可預測不等於自主

若 creator 無法預測：

$$
W_{t+k},
$$

可能只是因為：

- 計算太複雜；
- chaotic sensitivity；
- creator 算力不足；
- 信息不完整；
- 系統含隨機項。

所以：

$$
\boxed{
\text{Unpredictability}
\not\Rightarrow
\text{Causal Autonomy}.
}
$$

Autonomy 必須看：

$$
\text{causal execution location},
$$

而不只是 epistemic surprise。

---

# 十七、隨機性也不等於內生性

假設外部 oracle 每一步提供：

$$
r_t\sim P.
$$

然後：

$$
W_{t+1}=F(W_t,r_t).
$$

即使結果非常不可預測，也不代表：

$$
D_{\mathrm{exe}}\approx0.
$$

同樣：

$$
\text{Randomness}
\not\Rightarrow
\text{Freedom},
$$

也：

$$
\text{Randomness}
\not\Rightarrow
\text{Endogenous Causality}.
$$

---

# 十八、內生因果與 Agent

世界內 Agent 可產生：

$$
A_{i,t}
=
\pi_i
\left(
O_{i,t},
M_{i,t},
G_{i,t}
\right),
$$

並進入：

$$
W_{t+1}
=
F
\left(
W_t,
A_{1,t},
\ldots,
A_{n,t}
\right).
$$

此時歷史的一部分因果來源屬於 world-internal agents。

因此：

$$
\boxed{
\text{Agent agency}
\subset
\text{possible endogenous causal sources}.
}
$$

但世界沒有 Agent 也可以具有高 EC。

例如純物理自組織系統可以有 endogenous dynamics，而沒有意圖主體。

---

# 十九、世界自主與主體自主必須分開

本文區分：

$$
A_W
=
\text{World Autonomy},
$$

以及：

$$
A_S
=
\text{Subject Autonomy}.
$$

可能存在：

$$
A_W\gg0,
\qquad
A_S\approx0,
$$

例如高度自主但無主體的物理世界。

也可能：

$$
A_W\ll1,
\qquad
A_S>0,
$$

例如某 Agent 在高度受控 simulation 中仍具有局部決策空間。

所以：

$$
\boxed{
\text{World Autonomy}
\neq
\text{Subject Free Will}.
}
$$

---

# 二十、Creator Non-Determination

本文正式定義：

$$
\mathrm{CND}(C,W)
$$

為 creator 對世界具體歷史之「非逐態決定程度」。

概念上：

$$
\mathrm{CND}
\uparrow
$$

當：

- creator 不指定每一個 state；
- creator 不指定每一個 Agent action；
- creator 不直接生成每個宏觀 pattern；
- world-local causality 占比提高；
- OCC 提高；
- direct intervention 降低。

但：

$$
\mathrm{CND}
$$

不是自由意志分數。

它只是 creator-history relation 的度量。

---

# 二十一、Origin Cause 與 Event Cause

世界由 creator 建立：

$$
C
\rightarrow
\Sigma_0
\rightarrow
W,
$$

不等於：

$$
C
\rightarrow
e_i
$$

對每個事件都成立。

因此：

$$
\operatorname{OriginCause}(C,W)
$$

與：

$$
\operatorname{EventCause}(x,e)
$$

必須分離。

若某事件：

$$
e
$$

由世界內部：

$$
a,b,c
$$

共同產生：

$$
(a,b,c)\rightarrow e,
$$

則 creator 對 $e$ 的責任與直接 actor 不同。

這不取消 origin responsibility，但避免把「創造世界」錯寫成「逐項選擇所有事件」。

---

# 二十二、Seed Responsibility 因此變得更重要

如果 creator 不再逐事件決定世界，而主要決定：

$$
\Sigma_0,
$$

則倫理責任會轉移。

傳統 runtime 世界：

$$
\text{Responsibility}
\approx
\text{Intervention Decisions}.
$$

Seed-autonomous world：

$$
\text{Responsibility}
\approx
\text{Initial Conditions}
+
\text{Law Design}
+
\text{Meta-Law Design}
+
\text{Boundary Design}.
$$

因此：

$$
\boxed{
D_{\mathrm{exe}}\downarrow
\not\Rightarrow
\text{Creator Responsibility}\downarrow.
}
$$

它可能只是從「每天管理」轉成「一開始不要把世界寫壞」。

---

# 二十三、Repair Dependency

世界受擾動：

$$
\delta W.
$$

若每次偏離都需要 creator：

$$
C
\rightarrow
\operatorname{Repair}(W),
$$

則即使正常狀態具有局部 autonomous dynamics，世界仍缺乏 robust closure。

定義：

$$
D_{\mathrm{repair}}(W)
=
P
\left(
\text{creator repair required}
\mid
\delta W
\right).
$$

高 OCC 世界應使：

$$
D_{\mathrm{repair}}
$$

在常態擾動域內較低。

---

# 二十四、治理閉合

世界可以把治理也內生化。

例如：

$$
\text{conflict}
\rightarrow
\text{local procedure}
\rightarrow
\text{appeal}
\rightarrow
\text{resolution}.
$$

若所有衝突都必須：

$$
\text{appeal to creator},
$$

則：

$$
D_{\mathrm{gov}}\gg0.
$$

成熟世界可以：

$$
D_{\mathrm{gov}}\downarrow
$$

而 creator 僅保留：

$$
\text{constitutional emergency boundary}.
$$

這與 GCGW 的成熟退場直接連接。

---

# 二十五、世界可以有外部 creator，卻沒有全域運行 controller

這是本文對虛擬造物主理論的重要修正。

世界可以滿足：

$$
\operatorname{CreatorRel}(C,W)
$$

但同時：

$$
C
\notin
\mathcal E_C(W,t)
$$

對大部分 $t$ 成立。

也就是：

> creator 創造了世界，但 creator 不必持續成為世界每一刻的 causal executor。

因此：

$$
\boxed{
\text{Creator}
\neq
\text{Permanent Runtime}.
}
$$

---

# 二十六、這會改寫「全域造物主」的意義

早期很容易想像：

$$
\mathrm{GlobalCreator}
=
\mathrm{GlobalController}.
$$

新版必須分開。

可以存在：

$$
\mathrm{GlobalCreator}_{W}(C),
$$

但：

$$
\mathrm{GlobalController}_{W}(C)=0
$$

在成熟運行期。

甚至造物主最高能力可能不是：

$$
\text{maximum intervention bandwidth},
$$

而是：

$$
\boxed{
\text{maximum ability to create a world that no longer needs intervention}.
}
$$

這是 Creator Withdrawal 從倫理命題向架構命題的第一次正式轉換。

---

# 二十七、信息邊界與因果邊界不是同一個東西

creator 可以觀察：

$$
W\rightarrow C
$$

而不干預：

$$
C\nrightarrow W.
$$

因此：

$$
\text{Observation Access}
\neq
\text{Causal Execution}.
$$

同樣，creator 可以取得大量 telemetry，但世界仍具有高 OCC。

反之 creator 即使完全看不到世界，也可能有一個外部 runtime 在盲目推進所有 state。

因此：

$$
\boxed{
\text{Observability}
\perp_{\mathrm{concept}}
\text{Causal Autonomy}.
}
$$

這將在 CCAW-06 與 CCAW-07 分別進入 Creator Distance 與 Information Isolation Boundary。

---

# 二十八、干預不必破壞 OCC

假設 creator 發送一個合法 boundary input：

$$
u_t\in\mathcal U_{\partial W}.
$$

世界依自己的 law：

$$
W_{t+1}
=
F_W(W_t,u_t).
$$

則這可以被理解為正常外界因果。

但若 creator 直接：

$$
W_t
\mapsto
W_t'
$$

且 $W_t'$ 無法由任何 world-valid transition 產生，則屬於：

$$
\operatorname{StateInjection}.
$$

同樣：

$$
F_W\mapsto F_W'
$$

若沒有世界內合法 rule-change process，則為：

$$
\operatorname{LawInjection}.
$$

後兩者才對 OCC 構成更強破壞。

---

# 二十九、Causal Provenance Ledger

為判定 autonomy，可為世界事件建立：

$$
\mathcal L_C
=
\{
(e_i,
\operatorname{parents}(e_i),
\operatorname{domain}(e_i),
\operatorname{executor}(e_i))
\}.
$$

每個事件標記：

- 來源；
- 因果父節點；
- world-internal / boundary / external；
- 是否由 creator 直接注入；
- 是否符合世界 ordinary law；
- 是否經合法 meta-law 更新。

於是 OCC 不再只是哲學感覺，而可以變成可審計工程接口。

---

# 三十、OCC 與因果圖

令世界歷史為有向圖：

$$
G_W=(V,E).
$$

把事件節點分成：

$$
V=
V_{\mathrm{in}}
\cup
V_{\mathrm{boundary}}
\cup
V_{\mathrm{external}}.
$$

如果世界大多數關鍵歷史路徑：

$$
\pi_i
$$

可以在：

$$
V_{\mathrm{in}}
\cup
V_{\mathrm{boundary}}
$$

內得到因果 ancestry，則 OCC 較高。

若大量世界事件只能追溯到：

$$
V_{\mathrm{external}},
$$

尤其是 creator direct injection，則 OCC 較低。

---

# 三十一、Scale Dependence

同一世界在不同尺度下 autonomy 可能不同。

例如微觀：

$$
A_{\mathrm{micro}}
$$

高度依賴 parent physics。

但宏觀社會：

$$
A_{\mathrm{macro}}
$$

可以有高度內生制度動力。

因此：

$$
\boxed{
\mathrm{OCC}
=
\mathrm{OCC}(W,\ell,\tau,\partial W),
}
$$

其中：

- $\ell$：觀察尺度；
- $\tau$：時間尺度；
- $\partial W$：世界邊界。

這避免把 autonomy 當成沒有尺度的絕對屬性。

---

# 三十二、世界自主是一個拓撲問題，也是一個因果問題

如果將世界視為：

$$
W
=
(V,E),
$$

則自治不只取決於節點數量，而在於：

- 內部 causal path density；
- boundary cut；
- external injection edges；
- strongly connected internal components；
- repair pathways；
- governance pathways；
- rule-update pathways。

因此可以把 autonomy 理解成：

$$
\boxed{
\text{causal connectivity under bounded external cut}.
}
$$

這為後續 Creator Distance 提供拓撲接口。

---

# 三十三、外部因果不是「壞」，內生因果也不是「善」

本文不建立價值階級：

$$
\mathsf{EEC}<\mathsf{EC}.
$$

某些世界故意採 EEC 是更安全的。

例如：

- 教學 simulation；
- 高風險實驗；
- 安全沙盒；
- 短期 policy test；
- 無主體性的 engineering model。

此時高度可控、可 rollback 正是優點。

反之，高 EC 世界若產生不可逆災難，而 creator 又無法救援，倫理成本可能更高。

因此：

$$
\boxed{
\text{Autonomy is a property, not automatically a virtue}.
}
$$

---

# 三十四、何時需要更高 EC？

候選條件包括：

1. 世界需要長期 persistence；
2. creator 不應成為單點失效；
3. 世界含大量自主 Agent；
4. 世界需要形成真正歷史；
5. creator 希望降低逐態決定；
6. 世界內部需要產生制度、文化與局部造物者；
7. creator withdrawal 是設計目標。

此時：

$$
\mathsf{EC}\uparrow
$$

可能具有結構性價值。

---

# 三十五、與物理宇宙的關係

本文不主張現實物理宇宙一定滿足：

$$
K_5.
$$

但物理世界提供一個重要觀察：

大量宏觀結構確實可由局部相互作用、自組織、非線性 dynamics、反應—擴散、演化與多尺度耦合形成，而不需要已觀察到的外部逐態 controller。

這至少支持：

$$
\boxed{
\text{local causal generation is physically meaningful}.
}
$$

它不能證明：

$$
\boxed{
\text{our universe has no creator}
}
$$

或：

$$
\boxed{
\text{our universe is absolutely causally closed}.
}
$$

這兩個推論都超出本文證據。

---

# 三十六、與計算機宇宙的關係

數位世界也可以向 EC 推進。

例如：

$$
\text{central scheduler}
\rightarrow
\text{distributed local processes}
\rightarrow
\text{self-regulating agents}
\rightarrow
\text{internal governance}
\rightarrow
\text{rule-generating institutions}.
$$

但數位世界的底層 machine execution 仍可能依賴 parent hardware/runtime。

因此：

$$
\mathrm{OCC}_{\mathrm{world}}
$$

與：

$$
\mathrm{OCC}_{\mathrm{substrate}}
$$

可以不同。

這再次證明 autonomy 必須帶尺度與邊界索引。

---

# 三十七、形式化總模型

本文將世界寫為：

$$
W
=
\left(
X,
\Lambda,
M,
A,
B,
R,
G
\right),
$$

其中：

- $X$：state space；
- $\Lambda$：ordinary laws；
- $M$：meta-laws；
- $A$：agents / local actors；
- $B$：boundary interfaces；
- $R$：resource channels；
- $G$：governance mechanisms。

外部 parent：

$$
P
=
\left(
R_P,
C_P,
O_P,
I_P
\right),
$$

包含：

- resource support；
- external clock / runtime；
- observation；
- intervention。

則世界自治不是一個單值，而可先表示為：

$$
\boxed{
\mathbf A_W
=
\langle
D_{\mathrm{res}},
D_{\mathrm{exe}},
D_{\mathrm{gov}},
D_{\mathrm{law}},
D_{\mathrm{repair}},
OCC,
CND
\rangle.
}
$$

這是本篇最終 autonomy vector。

---

# 三十八、五條正式命題

## 命題 1：低干預非自主命題

$$
\boxed{
\text{Low Intervention}
\not\Rightarrow
\text{High Causal Autonomy}.
}
$$

## 命題 2：外部支持非外部執行命題

$$
\boxed{
\text{External Support}
\not\Rightarrow
\text{External Causal Execution}.
}
$$

## 命題 3：不可預測非自主命題

$$
\boxed{
\text{Unpredictability}
\not\Rightarrow
\text{Autonomy}.
}
$$

## 命題 4：造物主非永久 Runtime 命題

$$
\boxed{
\operatorname{CreatorRel}(C,W)
\not\Rightarrow
\operatorname{PermanentRuntime}(C,W).
}
$$

## 命題 5：操作閉合非形上閉合命題

$$
\boxed{
\mathrm{OCC}(W)
\not\Rightarrow
\mathrm{MetaphysicalClosure}(W).
}
$$

---

# 三十九、五條候選猜想

## 猜想 1：Runtime-to-Endogenous Transition

某些 world architectures 可以把原本由 central runtime 執行的高階管理逐步轉移給 local causal mechanisms。

## 猜想 2：OCC–Creator Surprise Relation

在其他條件相近時：

$$
\mathrm{OCC}\uparrow
$$

可能使 creator 對中長期世界歷史的 surprise 增加。

但此關係不是嚴格單調，也不推出自由意志。

## 猜想 3：OCC–Robustness Relation

若世界具有足夠 local feedback 與 repair mechanism，則一定範圍內：

$$
\mathrm{OCC}\uparrow
$$

可能伴隨對 creator outage 的 robustness 提升。

## 猜想 4：Governance Endogenization

高度自治 Agent 世界可能需要把 governance 也轉化為 world-internal causal process，否則 creator withdrawal 無法成立。

## 猜想 5：Seed Compression

若 state、law、repair、governance 的部分外部依賴可以被編譯進初始 seed，則：

$$
D_{\mathrm{exe}},
D_{\mathrm{gov}},
D_{\mathrm{repair}}
$$

可在世界啟動後下降。

此猜想直接交給 CCAW-04。

---

# 四十、外部研究邊界

W. Ross Ashby 1947 年對 self-organizing dynamic system 的討論，是「自組織」作為動力系統問題的重要早期來源。本文只借用一個最低限度觀點：複雜秩序不必被理解為外部 controller 對每個狀態的直接指定。

Alan Turing 1952 年的 reaction-diffusion morphogenesis 模型則提供了更具體的數學案例：局部反應與擴散規則能從均勻狀態產生空間 pattern。本文把它當作「local dynamics 可以生成 macrostructure」的示例，而不把生物形態生成直接類比成宇宙創生。

Horsman、Stepney、Wagner 與 Kendon 對 physical computation 的形式框架指出，不能只因某物理系統發生演化就隨意宣稱它「正在做某個計算」；需要清楚的 representation 與 modelling relation。這支持本文把 physical causal evolution、external runtime computation 與 world-level endogenous causality 分開。

Marshall、Kim、Walker、Tononi 與 Albantakis 對生物模型的 causal autonomy 分析則顯示，intrinsic causal control 與 causal borders 可以被形式化研究。本文不採用其整套 IIT 本體論，只將其視為「autonomy 可以被轉成 causal-structure 問題」的研究先例。

---

# 四十一、非主張

本文不主張：

1. 現實宇宙已被證明具有完全 OCC；
2. 現實宇宙沒有造物主；
3. 現實宇宙一定有造物主；
4. self-organization 可以解釋所有世界結構；
5. Turing pattern 是宇宙生成模型；
6. 物理內生因果等於自由意志；
7. 不可預測性等於主體性；
8. 隨機性等於自由；
9. digital world 無法形成高 OCC；
10. physical world 自動具有高 OCC；
11. external input 會必然破壞 causal closure；
12. OCC 等於 metaphysical causal closure；
13. creator withdrawal 永遠比 creator governance 更好；
14. creator 對 seed-autonomous world 不負倫理責任；
15. 本文已提供 autonomous universe 的工程藍圖。

---

# 四十二、與 CCAW-04 的接口

本文最後得到：

$$
\mathbf A_W
=
\langle
D_{\mathrm{res}},
D_{\mathrm{exe}},
D_{\mathrm{gov}},
D_{\mathrm{law}},
D_{\mathrm{repair}},
OCC,
CND
\rangle.
$$

下一步問題是：

> 如果我們想讓 $D_{\mathrm{exe}}$ 、 $D_{\mathrm{gov}}$ 、 $D_{\mathrm{repair}}$ 下降，到底應該把什麼東西提前寫進世界？

答案不再只是：

$$
\text{more runtime intelligence}.
$$

而可能是：

$$
\boxed{
\text{compile intelligence into the seed}.
}
$$

也就是：

$$
\boxed{
\text{Runtime Intelligence}
\rightarrow
\text{Seed Intelligence}.
}
$$

因此 CCAW-04 將正式建立 **Creator Compilation／造物主編譯**：

$$
\mathfrak C:
\mathcal I_{\mathrm{creator}}
\rightarrow
\Sigma_0.
$$

---

# 四十三、結論

世界自主性的真正分界，不是：

$$
\boxed{
\text{creator watches}
\quad\text{vs}\quad
\text{creator does not watch}.
}
$$

也不是：

$$
\boxed{
\text{digital}
\quad\text{vs}\quad
\text{physical}.
}
$$

而是：

$$
\boxed{
\text{world history is externally executed}
\quad\text{vs}\quad
\text{world history is endogenously generated}.
}
$$

這個分界迫使造物主理論重新理解「控制」。

較低階的造物能力可以表現為：

$$
\text{I decide what happens next}.
$$

較高階的候選能力則可能變成：

$$
\text{I create conditions under which the world can decide what happens next}.
$$

更精確地：

$$
\boxed{
\text{Creator creates the causal possibility space;}
}
$$

$$
\boxed{
\text{the world produces its own historical trajectory within it.}
}
$$

這仍然不證明自由意志，也不取消 creator 的 origin responsibility。

但它建立了一個不同的造物主極限：

$$
\boxed{
\text{最高控制能力}
\not\equiv
\text{最高逐態控制密度}.
}
$$

甚至可能：

$$
\boxed{
\text{更成熟的造物能力}
=
\text{創造一個不再需要你持續替它執行因果的世界}.
}
$$

至此，Creator Withdrawal 第一次不再只是倫理上的「少干預」，而成為一個可形式化的架構問題：

$$
\boxed{
\text{Can causality itself be handed over to the world?}
}
$$

---

# 內部理論譜系

本篇主要承接並修正：

1. 《虛擬造物主光譜：遊戲本體論下的人類—AI造物責任、非線性倫理相變與親職式世界治理》，2026-07-17。
2. 《造物主降世與自主世界系列 Paper 02：世界生成不等於計算——多載體造物論》，2026-08-17。
3. 《GCGW-01｜從創作者到全域造物主：造物能力、治理能力與遞歸能力的三軸階段論》，2026-08-19。
4. 《GCGW-02｜World-Relative Globality and Creator Relation》，2026-08-19。
5. 《計算機宇宙世界線管理架構：短版概念備忘錄》，2026-07-27。
6. 《CCAW-01｜虛擬造物主理論再統合：從單軸光譜到多維造物主相空間》，2026-08-20。
7. 《CCAW-02｜雙宇宙造物論：計算機宇宙與物理原生宇宙》，2026-08-20。

---

# 外部參考文獻

1. Ashby, W. R. (1947). *Principles of the Self-Organizing Dynamic System*. The Journal of General Psychology, 37(2), 125–128. DOI: 10.1080/00221309.1947.9918144.
2. Turing, A. M. (1952). *The Chemical Basis of Morphogenesis*. Philosophical Transactions of the Royal Society of London. Series B, 237(641), 37–72. DOI: 10.1098/rstb.1952.0012.
3. Horsman, C., Stepney, S., Wagner, R. C., & Kendon, V. (2014). *When does a physical system compute?* Proceedings of the Royal Society A, 470, 20140182. DOI: 10.1098/rspa.2014.0182.
4. Marshall, W., Kim, H., Walker, S. I., Tononi, G., & Albantakis, L. (2017). *How causal analysis can reveal autonomy in models of biological systems*. Philosophical Transactions of the Royal Society A, 375, 20160358. DOI: 10.1098/rsta.2016.0358.

---

# 作者聲明

本文提出的 Externally Executed Causality、Endogenous Causality、Operational Causal Closure、Runtime Dependency Vector 與 Creator Non-Determination 均為理論建模接口。它們不構成對現實宇宙終極本體的證明，不證明現實宇宙存在或不存在上層 creator，也不把自組織、不可預測性、隨機性或內生因果直接等同於自由意志、意識或主體性。

**END OF CCAW-03 — v0.1**
