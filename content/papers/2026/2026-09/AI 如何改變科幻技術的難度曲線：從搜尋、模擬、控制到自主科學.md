# AI 如何改變科幻技術的難度曲線：從搜尋、模擬、控制到自主科學

**系列**：《從時間旅行到時空管理者》04  
**英文題名**：*How AI Changes the Difficulty Curves of Science-Fiction Technologies: From Search, Simulation, and Control to Autonomous Science*  
**作者**：Neo.K × GPT-5.6 Sol  
**機構**：EveMissLab（一言諾科技有限公司）  
**日期**：2026-08-24  
**版本**：v0.1  
**性質**：AI 科學方法論／技術可達性／自主科學／控制與實驗閉環／時空工程前置框架  
**狀態**：Series 02 正式第四篇  
**前置研究**：《從科幻到工程：幻想—實現邊界壓縮與 AI 奇點的新定義》、《具身化 AI 自主研究閉環》、《約束不是常數》  
**前篇**：《可行／不可行二分的終結：動態技術可達性分類》

---

## 摘要

「AI 會讓科幻科技更快實現」是一句直覺上合理、但技術上過度壓縮的命題。不同科技的主要障礙並不相同：有些卡在搜尋空間，有些卡在理論未知，有些卡在材料、能量、製造與控制，有些卡在無法測量與驗證，另一些則可能受到明確的數學 no-go、邏輯矛盾或 fundamental physical law 約束。若不先區分障礙型別，就無法回答 AI 到底能降低多少難度。

本文承接 Paper 03 的 Dynamic Technological Reachability Classification（DTRC），將其中的 AI leverage 軸：

$$
L_{\mathrm{AI}}
$$

展開為：

$$
\boxed{
L_{\mathrm{AI}}(X,t)
=
\left\langle
L_H,
L_S,
L_{\mathrm{sim}},
L_D,
L_C,
L_E,
L_V,
L_M
\right\rangle
}
$$

其中：

- $L_H$：hypothesis leverage，假說生成與理論探索槓桿；
- $L_S$：search leverage，搜尋與最佳化槓桿；
- $L_{\mathrm{sim}}$：simulation leverage，模擬、代理模型與反問題槓桿；
- $L_D$：design leverage，材料、器件與系統設計槓桿；
- $L_C$：control leverage，控制、回授與狀態估計槓桿；
- $L_E$：experiment leverage，實驗規劃與自主實驗槓桿；
- $L_V$：verification leverage，驗證、證據統合與反例搜尋槓桿；
- $L_M$：meta-science leverage，研究流程、工具鏈與自主科研閉環槓桿。

本文進一步建立「障礙彈性」（Barrier Elasticity）概念。對技術 $X$ 的第 $i$ 類障礙 $B_i$，定義相對 AI 能力 $K_{\mathrm{AI}}$ 的局部彈性：

$$
\boxed{
\eta_i^{\mathrm{AI}}
=
-
\frac{
\partial\ln B_i
}{
\partial\ln K_{\mathrm{AI}}
}.
}
$$

若：

$$
\eta_i^{\mathrm{AI}}\gg0,
$$

代表該障礙對 AI 能力高度可壓縮；若：

$$
\eta_i^{\mathrm{AI}}\approx0,
$$

代表增加 AI 能力幾乎不能降低此障礙。本文不把 $\eta_i^{\mathrm{AI}}$ 視為目前可直接測得的普適物理常數，而是一個研究性、任務相對的技術分析量。

本文將障礙分為十二類：

$$
\mathfrak B_X
=
\left\{
B_{\mathrm{logic}},
B_{\mathrm{law}},
B_{\mathrm{theory}},
B_{\mathrm{search}},
B_{\mathrm{compute}},
B_{\mathrm{material}},
B_{\mathrm{energy}},
B_{\mathrm{fab}},
B_{\mathrm{control}},
B_{\mathrm{observe}},
B_{\mathrm{verify}},
B_{\mathrm{coord}}
\right\}.
$$

AI 對其中的作用高度不均勻。對搜尋、組合設計、代理建模、控制器優化與實驗規劃，AI 往往可形成高槓桿；對材料與能源障礙，AI 主要透過發現、優化與替代路徑間接降低；對邏輯矛盾與已在明確前提下成立的 fundamental no-go，AI 的作用不是「突破」，而是更快找到證明、檢查假設、辨識適用域，或發現我們原先誤把軟限制當成硬限制。

2026 年的 self-driving laboratory 文獻已顯示，自主實驗系統正由狹窄自動化向能提出、執行與解讀實驗的多用途平台發展；同時，最新綜述也強調 scalability、generalizability、provenance-complete experimentation、安全與可信 AI 仍是核心限制。2026 年已有研究展示 AI agents 可在科學儀器操作中邊做邊學，並有多智能體架構被提出用於管理 autonomous materials labs。2025–2026 年的 AlphaEvolve 類系統則提供另一條證據：當問題具有可執行的 evaluator，AI 可以在巨大的程式／演算法空間中搜尋並產生新解。這些進展支持一個較保守但重要的命題：AI 已經在若干研究域中降低「找到候選解」與「閉環試驗」的成本，但尚未消除實體材料、尺度、能源、驗證與安全治理障礙。

本文提出「自主科學閉環」：

$$
\boxed{
H
\rightarrow
S
\rightarrow
\Sigma
\rightarrow
D
\rightarrow
E
\rightarrow
O
\rightarrow
V
\rightarrow
U
\rightarrow
H'
}
$$

分別代表假說、搜尋、模擬、設計、實驗、觀測、驗證、模型更新與下一輪假說。AI 真正可能帶來的科技加速，不只是單點推理更快，而是縮短整個 research-loop cycle time：

$$
T_{\mathrm{cycle}}
\downarrow,
$$

提高每單位時間的有效信息增益：

$$
\Phi_{\mathrm{sci}}
=
\frac{
\mathbb E[\Delta I_{\mathrm{validated}}]
}{
T_{\mathrm{cycle}}
}.
$$

但高 throughput 不等於高 truth。若實驗設計、儀器校準、資料 provenance、反例治理與獨立 replication 不完整，AI 可能同時加速錯誤、偏差與 Goodhart 化。因此，本文把「自主科學」定義為受證據、否證、權限、安全與物理回退約束的閉環，而不是無限制自動實驗。

本文最後提出「科幻技術難度曲線」：

$$
\boxed{
D_X(t)
=
F
\left(
\mathbf B_X(t),
K_{A,t},
K_{\mathrm{AI},t}
\right),
}
$$

其中 AI 改變的不是宇宙真實物理律，而是文明在理論、搜尋、設計、控制與驗證空間中抵達可行方案的速度與成本。某些技術的難度曲線會因此快速下降，某些只會緩慢下降，某些在獲得更強 no-go 結果後反而上升。這比「AI 讓一切科幻成真」或「AI 對 fundamental science 沒用」都更接近一個可研究、可檢驗的框架。

**關鍵詞**：AI 科學、障礙彈性、自主科學、自動實驗、self-driving laboratory、技術可達性、搜尋、控制、驗證、時空工程

---

# 0. 核心問題：AI 到底在降低什麼？

如果一項技術：

$$
X
$$

目前不可達，

我們不能直接寫：

$$
D_X=\text{high}.
$$

而應問：

> 高在哪裡？

可能是：

$$
B_{\mathrm{search}}\gg0,
$$

也可能是：

$$
B_{\mathrm{energy}}\gg0,
$$

或：

$$
B_{\mathrm{law}}=\infty
$$

在某個明確模型下成立。

因此：

$$
\boxed{
\text{AI impact}
=
\text{barrier-specific impact}.
}
$$

---

# 1. DTRC 中的 AI 軸

Paper 03 定義：

$$
\mathcal D_X
=
\left\langle
P,S,E,R,C,V,L_{\mathrm{AI}},U
\right\rangle.
$$

本文將：

$$
L_{\mathrm{AI}}
$$

展開。

所以 Paper 03 問：

> AI 是不是有槓桿？

本文問：

> AI 對哪一種障礙、透過哪一個機制、有多少槓桿？

---

# 2. 八維 AI 科學槓桿

定義：

$$
\boxed{
L_{\mathrm{AI}}
=
\left\langle
L_H,
L_S,
L_{\mathrm{sim}},
L_D,
L_C,
L_E,
L_V,
L_M
\right\rangle.
}
$$

這八維彼此相關但不能合併成單一「AI 很強」。

---

# 3. $L_H$：假說與理論探索

AI 可參與：

- 文獻搜尋；
- 定理與反例搜尋；
- 跨領域概念映射；
- 方程候選生成；
- 模型比較；
- 假說消融；
- assumption audit。

可寫：

$$
\mathcal H_{\mathrm{candidate}}
=
G_{\mathrm{AI}}
(
K_{\mathrm{known}},
D,
C
).
$$

但：

$$
\text{hypothesis generation}
\neq
\text{physical truth}.
$$

所以：

$$
\boxed{
L_H
\text{ primarily expands candidate theory space}.
}
$$

---

# 4. $L_S$：搜尋與最佳化

許多工程問題本質上是：

$$
x^\ast
=
\arg\min_x
J(x)
$$

或：

$$
x^\ast
=
\arg\max_x
F(x)
$$

但搜尋空間：

$$
|\Omega|
$$

巨大。

AI 可以透過：

- evolutionary search；
- Bayesian optimization；
- reinforcement learning；
- program synthesis；
- heuristic generation；
- learned search policies；

提高：

$$
P(\text{find good candidate}\mid B).
$$

這是目前最直接的 AI 高槓桿區之一。

---

# 5. 可驗證 evaluator 會大幅提高 AI 搜尋槓桿

若候選：

$$
x
$$

可以被自動 evaluator：

$$
E(x)
$$

可靠評分，

則 AI 可以大量生成並淘汰候選。

形成：

$$
x_0
\rightarrow
x_1
\rightarrow
\cdots
\rightarrow
x^\ast.
$$

AlphaEvolve 類系統正屬於這種結構：

$$
\boxed{
\text{LLM proposal}
+
\text{automated evaluator}
+
\text{iterative search}.
}
$$

因此：

$$
\boxed{
\text{Evaluator Quality}
\text{ is a major determinant of AI leverage}.
}
$$

---

# 6. 沒有 evaluator 時，生成能力可能變成幻覺放大器

若：

$$
E(x)
$$

缺失或極弱，

AI 只能生成大量看似合理候選。

此時：

$$
N_{\mathrm{proposal}}\uparrow
$$

不必導致：

$$
N_{\mathrm{valid}}\uparrow.
$$

所以：

$$
\boxed{
\text{Proposal Throughput}
\neq
\text{Discovery Throughput}.
}
$$

---

# 7. $L_{\mathrm{sim}}$：模擬與代理模型

高成本物理實驗：

$$
E_{\mathrm{real}}
$$

可以部分由：

$$
\widehat E_{\mathrm{sim}}
$$

先行篩選。

AI 可建立：

- surrogate models；
- reduced-order models；
- emulators；
- learned dynamics；
- differentiable approximations。

若：

$$
C_{\mathrm{sim}}
\ll
C_{\mathrm{real}},
$$

則候選探索速度可能大幅提升。

---

# 8. 模擬加速不等於真實加速

若 simulator：

$$
\widehat M
$$

漏掉關鍵物理，

則：

$$
\operatorname{argmax}
F_{\widehat M}
$$

可能在真實系統失效。

因此：

$$
\boxed{
\text{Simulation Acceleration}
\text{ requires model-validity control}.
}
$$

AI 對 surrogate 的信任必須受到：

- domain shift；
- uncertainty；
- out-of-distribution detection；
- experimental calibration；

約束。

---

# 9. $L_D$：設計槓桿

AI 可以在：

- materials；
- molecules；
- metamaterials；
- circuits；
- photonics；
- mechanical structures；
- experimental apparatus；

中搜尋結構。

設計問題可寫：

$$
G:
\text{desired function}
\rightarrow
\text{candidate structure}.
$$

若 inverse design 很難，

AI 可以提高：

$$
L_D.
$$

---

# 10. 設計成功不等於可製造

若候選：

$$
x^\ast
$$

滿足 simulator，

但：

$$
x^\ast
\notin
\mathcal F_{\mathrm{manufacturable}},
$$

則仍不可用。

所以：

$$
\boxed{
\text{Design Space}
\neq
\text{Fabricable Space}.
}
$$

自主設計系統必須把 fabrication constraints 直接放進 objective。

---

# 11. $L_C$：控制槓桿

很多 frontier technology 的核心不是找不到現象，

而是：

> 控不住。

定義系統：

$$
\dot x=f(x,u).
$$

AI 可以學：

$$
u^\ast
=
\pi_{\mathrm{AI}}(x,\hat x,G).
$$

以完成：

- nonlinear control；
- adaptive control；
- predictive control；
- anomaly recovery；
- high-dimensional state estimation。

因此：

$$
\boxed{
L_C
\text{ can convert some unstable phenomena into usable technologies}.
}
$$

---

# 12. 控制不是突破物理律，而是擴大可利用子域

假設：

$$
\mathcal P_M
$$

是物理可能域。

控制器只是在：

$$
\mathcal P_M
$$

內找到：

$$
\Gamma_{\mathrm{stable}}.
$$

所以：

$$
\boxed{
\text{Better Control}
\rightarrow
\text{larger operational reachable set},
}
$$

而不是：

$$
\boxed{
\text{Better Control}
\rightarrow
\text{larger fundamental physical possibility set}.
}
$$

---

# 13. $L_E$：實驗規劃槓桿

傳統實驗：

$$
e_1,e_2,\ldots
$$

可能由人類手動挑選。

AI 可用：

- active learning；
- Bayesian experimental design；
- optimal design；
- information gain；
- multi-armed search；

選擇：

$$
e^\ast
=
\arg\max_e
\mathbb E[
\Delta I
\mid e
].
$$

因此：

$$
\boxed{
\text{AI can increase information gained per experiment}.
}
$$

---

# 14. Self-driving laboratory 是實體化的 $L_E$

Self-driving laboratory（SDL）把：

- algorithmic decision；
- robotics；
- synthesis；
- characterization；
- data analysis；

整合成閉環。

2026 年 Nature Reviews Chemistry 的綜述已把 SDL 描述為從狹窄 automation 向能提出、執行與解讀實驗的 multipurpose discovery platform 演進。

這說明：

$$
\boxed{
L_E
\text{ is no longer only a theoretical possibility}.
}
$$

---

# 15. 但 SDL 仍不是「自動發現真理機」

同一 2026 年文獻強調：

- scalability；
- generalizability；
- provenance-complete experimentation；
- interoperable standards；
- trustworthy AI；

仍是限制。

所以：

$$
\boxed{
\text{Autonomy}
\neq
\text{epistemic infallibility}.
}
$$

---

# 16. $L_V$：驗證槓桿

AI 可協助：

- proof checking；
- anomaly detection；
- replication planning；
- provenance audit；
- causal consistency；
- cross-paper contradiction search；
- statistical robustness。

因此：

$$
L_V
$$

不是「寫論文更快」，

而是：

> 更快判斷哪些結果值得相信。

---

# 17. AI 也可以加速否證

如果：

$$
H
$$

錯誤，

AI 可：

- 搜反例；
- 找 hidden assumptions；
- 生成 adversarial experiment；
- 找 failure regions。

所以：

$$
\boxed{
L_V>0
\text{ can push a technology toward stronger impossibility classification}.
}
$$

這正是 Paper 03 的：

$$
L_6\rightarrow L_8
$$

路徑之一。

---

# 18. $L_M$：meta-science 槓桿

AI 不只解單題，

還可以管理：

- literature state；
- hypothesis queue；
- experiment queue；
- evidence graph；
- tool routing；
- replication；
- uncertainty；
- lab resources。

因此：

$$
\boxed{
L_M
=
\text{research-process optimization leverage}.
}
$$

它會改變的不只是某一次計算時間，

而是整個科研組織的 cycle time。

---

# 19. 十二類障礙

定義：

$$
\boxed{
\mathfrak B_X
=
\left\{
B_{\mathrm{logic}},
B_{\mathrm{law}},
B_{\mathrm{theory}},
B_{\mathrm{search}},
B_{\mathrm{compute}},
B_{\mathrm{material}},
B_{\mathrm{energy}},
B_{\mathrm{fab}},
B_{\mathrm{control}},
B_{\mathrm{observe}},
B_{\mathrm{verify}},
B_{\mathrm{coord}}
\right\}.
}
$$

AI 對不同 $B_i$ 的作用不同。

---

# 20. $B_{\mathrm{logic}}$：邏輯障礙

如果目標本身：

$$
X\land\neg X
$$

要求矛盾同時成立，

更強 AI 不能透過搜尋讓它成真。

因此：

$$
\boxed{
\eta_{\mathrm{logic}}^{\mathrm{AI}}
\approx0
}
$$

在固定邏輯規格下。

AI 的作用是：

> 更快指出 specification 自相矛盾。

---

# 21. $B_{\mathrm{law}}$：fundamental law 障礙

若在被充分確認且適用的物理律：

$$
\mathcal L^\ast
$$

下，

有嚴格禁止：

$$
X\notin\mathcal P_{\mathcal L^\ast},
$$

AI 不能透過設計把它變 allowed。

所以：

$$
\eta_{\mathrm{law}}^{\mathrm{AI}}
\approx0.
$$

但 AI 可審計：

- law 是否真的 fundamental；
- theorem assumptions；
- regime applicability；
- alternate transformation definition。

---

# 22. $B_{\mathrm{theory}}$：理論未知

如果現象有資料，

但機制未知，

AI 可以：

- symbolic regression；
- theorem search；
- model discovery；
- literature fusion；
- causal modeling；

降低：

$$
B_{\mathrm{theory}}.
$$

但理論發現仍必須經：

$$
E_{\mathrm{physical}}.
$$

---

# 23. $B_{\mathrm{search}}$：搜尋障礙

這是 AI 最可能高彈性的障礙之一。

如果：

$$
|\Omega|\gg1,
$$

而 evaluator 足夠好，

AI 可以大幅降低有效探索成本。

因此：

$$
\eta_{\mathrm{search}}^{\mathrm{AI}}
$$

可能很高。

---

# 24. $B_{\mathrm{compute}}$：計算障礙

AI 可以：

- approximate；
- compress；
- learn heuristics；
- find better algorithms；
- allocate compute。

但如果計算需求是 unavoidable lower bound，

AI 仍受：

$$
\text{complexity}
+
\text{hardware}
+
\text{energy}
$$

限制。

所以：

$$
\boxed{
\text{algorithmic improvement}
\neq
\text{free computation}.
}
$$

---

# 25. $B_{\mathrm{material}}$：材料障礙

AI 可：

- 搜材料；
- 設計 microstructure；
- 預測 phase；
- 推薦 synthesis path。

但若所需材料：

$$
M^\ast
$$

物理上不存在，

AI 無法生成它。

所以 AI 對材料主要是：

$$
\boxed{
\text{discovery}
+
\text{substitution}
+
\text{optimization}.
}
$$

---

# 26. $B_{\mathrm{energy}}$：能源壁壘

AI 可以：

- 找效率更高路徑；
- 降低耗散；
- 控制 energy flow；
- 發現替代 process。

但若某目標有：

$$
E_{\min}
$$

不可避免下界，

則：

$$
E<E_{\min}
$$

不能靠 AI 消除。

所以：

$$
\eta_{\mathrm{energy}}^{\mathrm{AI}}
$$

取決於目前能耗離真正下界有多遠。

---

# 27. $B_{\mathrm{fab}}$：製造障礙

AI 可幫：

- process planning；
- robotic assembly；
- tolerancing；
- defect detection；
- adaptive manufacturing。

如果設計已知但精度不夠，

這是高潛力區。

但若需要：

$$
\delta x<\delta x_{\mathrm{physical\ limit}},
$$

則仍受硬界限制。

---

# 28. $B_{\mathrm{control}}$：控制障礙

對：

- plasma；
- unstable quantum states；
- nonlinear systems；
- autonomous instruments；

AI 有可能大幅降低：

$$
B_{\mathrm{control}}.
$$

這是從「現象存在」到「技術可用」的關鍵橋。

---

# 29. $B_{\mathrm{observe}}$：觀測障礙

AI 能提升：

- denoising；
- inverse reconstruction；
- sensor fusion；
- adaptive measurement；
- target selection。

但：

$$
\text{no signal}
$$

不能被合法 hallucinate 成：

$$
\text{signal}.
$$

所以：

$$
\boxed{
\text{AI-enhanced inference}
\text{ must preserve measurement uncertainty}.
}
$$

---

# 30. $B_{\mathrm{verify}}$：驗證障礙

AI 可：

- 尋找替代解釋；
- 自動統計；
- independent check；
- proof assistant；
- provenance audit。

但若某聲稱原理上不可觀察，

則：

$$
V
$$

仍可能保持極高。

---

# 31. $B_{\mathrm{coord}}$：組織與協調障礙

大型技術可能卡在：

- supply chain；
- protocol；
- lab orchestration；
- multidisciplinary communication；
- scheduling；
- experiment handoff。

AI agent 系統可降低：

$$
B_{\mathrm{coord}}.
$$

2026 年已有研究直接討論 multi-agent AI 管理 autonomous materials labs。

所以：

$$
\boxed{
\text{coordination itself is a technological barrier}.
}
$$

---

# 32. 障礙彈性

本文定義：

$$
\boxed{
\eta_i^{\mathrm{AI}}
=
-
\frac{
\partial\ln B_i
}{
\partial\ln K_{\mathrm{AI}}
}.
}
$$

它的直觀語義：

> AI 能力提高 1% 時，該障礙相對下降多少？

這不是目前已經能普遍測量的物理常數。

它是一個：

$$
\boxed{
\text{comparative research metric}.
}
$$

---

# 33. 高、中、低 AI 彈性

可粗分：

### 高彈性

$$
\eta_i^{\mathrm{AI}}\gg0
$$

例如：

- search；
- simulation；
- design；
- scheduling；
- some control。

### 中彈性

AI 可間接降低：

- materials；
- fabrication；
- observation；
- verification。

### 低／零彈性

固定前提下的：

- logical contradiction；
- strict no-go；
- irreducible physical lower bound。

---

# 34. Barrier Elasticity 不是永久常數

若新工具出現，

同一障礙的：

$$
\eta_i^{\mathrm{AI}}(t)
$$

會改變。

例如 robotics 尚未成熟時：

$$
\eta_{\mathrm{experiment}}^{\mathrm{AI}}
$$

較低。

當 robot lab、machine vision、standardized instruments 成熟後，

可能上升。

因此：

$$
\boxed{
\eta_i^{\mathrm{AI}}
=
\eta_i^{\mathrm{AI}}(X,t,E).
}
$$

---

# 35. 技術難度曲線

定義技術 $X$ 的綜合障礙向量：

$$
\mathbf B_X(t)
=
\left(
B_1,\ldots,B_n
\right)_t.
$$

則技術難度：

$$
\boxed{
D_X(t)
=
F
\left(
\mathbf B_X(t),
K_{A,t},
K_{\mathrm{AI},t}
\right).
}
$$

AI 的作用不是：

$$
D_X
\rightarrow0
$$

而是改變：

$$
\frac{dD_X}{dt}.
$$

---

# 36. 三種難度曲線

### 36.1 快速下降型

主障礙高 AI 彈性。

例如大量搜尋／優化問題。

### 36.2 慢速下降型

主障礙在材料、能源、scale-up。

### 36.3 平坦／上升型

主障礙為 hard no-go，

或新研究持續增加困難證據。

所以：

$$
\boxed{
\text{AI does not imply universally decreasing difficulty}.
}
$$

---

# 37. AI 也可能讓難度曲線上升

如果 AI：

- 找到新 no-go theorem；
- 發現 hidden instability；
- 找出 resource lower bound；
- 發現 simulator 錯誤；
- 找到 experiment contradiction；

則：

$$
D_X(t+\Delta t)>D_X(t).
$$

但：

$$
U_X
$$

下降。

這仍是科學進步。

---

# 38. 自主科學閉環

本文提出：

$$
\boxed{
H
\rightarrow
S
\rightarrow
\Sigma
\rightarrow
D
\rightarrow
E
\rightarrow
O
\rightarrow
V
\rightarrow
U
\rightarrow
H'.
}
$$

其中：

- $H$：Hypothesis；
- $S$：Search；
- $\Sigma$：Simulation；
- $D$：Design；
- $E$：Experiment；
- $O$：Observation；
- $V$：Verification；
- $U$：Update；
- $H'$：Next hypothesis。

---

# 39. AI 真正的加速點是閉環週期

傳統研究週期：

$$
T_{\mathrm{human}}.
$$

AI-augmented cycle：

$$
T_{\mathrm{AI}}.
$$

若：

$$
T_{\mathrm{AI}}
\ll
T_{\mathrm{human}},
$$

同一日曆時間可做更多：

$$
N_{\mathrm{cycles}}.
$$

但真正要最大化的不是 cycle 數，

而是：

$$
\boxed{
\Phi_{\mathrm{sci}}
=
\frac{
\mathbb E[\Delta I_{\mathrm{validated}}]
}{
T_{\mathrm{cycle}}
}.
}
$$

---

# 40. 有效信息增益

若一輪實驗產生大量數據：

$$
D
$$

但不降低模型不確定性，

則：

$$
\Delta I_{\mathrm{validated}}
\approx0.
$$

所以自主科學不應追求：

$$
\text{data throughput}
$$

本身，

而應追求：

$$
\boxed{
\text{validated information gain}.
}
$$

---

# 41. 具身 AI 自主研究閉環

當 AI 真正控制儀器：

$$
A_{\mathrm{AI}}
\rightarrow
\mathcal I_{\mathrm{physical}},
$$

它就從：

> 建議研究。

進入：

> 執行研究。

此時需要：

- action authorization；
- instrument health；
- calibration；
- sample identity；
- provenance；
- anomaly handling；
- physical rollback。

因此：

$$
\boxed{
\text{Autonomous Science}
=
\text{epistemic loop}
+
\text{physical control loop}.
}
$$

---

# 42. 2026 年 Self-Driving Labs 的實際意義

目前 SDL 已經在部分化學、材料與儀器領域形成：

$$
\text{plan}
\rightarrow
\text{execute}
\rightarrow
\text{measure}
\rightarrow
\text{learn}
$$

的閉環。

這不是通用自動科學家已完成，

但已證明：

$$
\boxed{
\text{parts of the scientific loop are automatable in physical labs}.
}
$$

這是 AI 技術可達性框架的重要實證背景。

---

# 43. A-Lab 的案例意義

A-Lab 類平台整合：

- computation；
- literature；
- ML；
- active learning；
- robotics。

其價值不是證明：

> AI 可以發現所有材料。

而是證明：

> 多個原本分離的人類研究階段，可以被閉環整合。

所以：

$$
\boxed{
L_H+L_S+L_E+L_V
}
$$

可以在同一物理研究 pipeline 中共同作用。

---

# 44. AI agents 操作科學儀器

2026 年已有研究展示：

> AI agents 可以在 advanced scientific instruments 上進行操作並在工作中適應。

這對：

$$
L_C
$$

與：

$$
L_E
$$

特別重要。

因為未來自主科學不只需要「想實驗」，

還需要：

$$
\boxed{
\text{instrument-grounded action competence}.
}
$$

---

# 45. Multi-Agent Lab

若研究任務需要：

- synthesis；
- characterization；
- planning；
- resource management；
- verification；

單一 Agent 可能不夠。

可以：

$$
A_1,\ldots,A_n
$$

分工。

但這帶來：

$$
B_{\mathrm{coord}}
$$

的新型態：

- conflicting plans；
- handoff failure；
- shared-state inconsistency；
- authority ambiguity。

所以：

$$
\boxed{
\text{more agents}
\not\Rightarrow
\text{more science}.
}
$$

---

# 46. 自主科學的安全 harness

2026 年 Nature Synthesis 已特別提出 SDL 需要 autonomy safety harness 的觀點。

原因是：

$$
\text{AI-generated intent}
$$

必須被轉成：

$$
\text{safe executable experiment}.
$$

所以需要：

- policy；
- runtime monitoring；
- action limits；
- evidence logging；
- veto；
- recovery。

這和具身 AI 自主研究閉環中的治理需求一致。

---

# 47. Provenance-complete science

如果 AI 自動：

- 生成假說；
- 改參數；
- 換試劑；
- 重跑實驗；

而沒有完整：

$$
H_{\mathrm{experiment}}
$$

紀錄，

結果將難以重現。

因此：

$$
\boxed{
\text{Autonomy}
\Rightarrow
\text{stronger provenance requirements}.
}
$$

不是反過來。

---

# 48. 自主科學會加速錯誤嗎？

會，如果 objective 錯。

若系統追求：

$$
J=\text{paper-worthy novelty},
$$

可能 Goodhart 化。

若追求：

$$
J=\text{target metric},
$$

可能 exploit measurement artifact。

所以真正需要：

$$
\boxed{
J
=
f(
\text{truth},
\text{uncertainty},
\text{replication},
\text{safety},
\text{cost}
).
}
$$

---

# 49. 異常不是發現

AI 遇到：

$$
y\not\approx \hat y
$$

不能直接寫：

> 新物理。

應先檢查：

- instrument failure；
- calibration；
- sample contamination；
- software bug；
- data pipeline；
- model assumption；
- replication。

因此：

$$
\boxed{
\text{Anomaly}
\neq
\text{Discovery}.
}
$$

但：

$$
\text{Anomaly}
=
\text{research entrance}.
$$

---

# 50. 自主科學的真正閉環需要反例治理

若 Agent 只會最大化成功率，

會避開 failure。

但科學需要：

$$
\text{counterexample search}.
$$

因此自主科學應最大化：

$$
\boxed{
\text{discriminative information}
}
$$

而不是：

$$
\boxed{
\text{confirmation}.
}
$$

---

# 51. AI 對時間旅行研究最先能做什麼？

不是：

> 造時光機。

而是：

1. 形式化不同 traversal class；
2. 搜尋 GR / QFT 模型；
3. 自動檢查 no-go assumptions；
4. 搜穩定性反例；
5. 模擬 causal structure；
6. 搜材料與控制方案；
7. 設計間接可驗證實驗；
8. 建立 DTRC 更新。

因此：

$$
\boxed{
\text{AI's first contribution to time travel}
=
\text{classification and search acceleration}.
}
$$

---

# 52. AI 對 Type 2 的槓桿

Type 2：

$$
\text{local forward traversal}
$$

基礎物理已成熟。

主障礙偏：

- propulsion；
- energy；
- life support；
- control。

所以：

$$
L_D,L_C,L_E
$$

可能有中高效益。

---

# 53. AI 對 Type 4 的槓桿

Type 4：

$$
\text{local past-directed arrival}
$$

仍卡：

- formation；
- stability；
- quantum effects；
- controllability；
- chronology protection。

因此 AI 可高槓桿作用於：

$$
L_H,L_S,L_{\mathrm{sim}},L_V,
$$

但對：

$$
B_{\mathrm{law}}
$$

是否存在硬禁止，

只能加速判定。

---

# 54. AI 對 Type 5–8 的槓桿

branch traversal / branch creation 類最大的問題目前甚至是：

$$
B_{\mathrm{theory}},
$$

$$
B_{\mathrm{ontology}},
$$

而非純工程。

因此 AI 最先能做：

> 把概念從敘事變成可判定模型。

若：

$$
A_{\mathrm{address}}
$$

都未定義，

談工程優化沒有意義。

---

# 55. AI 對 payload 技術的槓桿

Paper 02 中的：

$$
P_0\ldots P_8
$$

對 AI 槓桿也不同。

例如 AI seed：

$$
P_4
$$

的難度可能被：

- compression；
- architecture search；
- distillation；
- robust bootstrapping；

降低。

因此：

$$
L_{\mathrm{AI}}
$$

不只作用 traversal mechanism，

也作用 payload complexity。

---

# 56. AI 會讓 frontier technology 分化得更快

假設一批技術：

$$
X_1,\ldots,X_n
$$

目前都在：

$$
L_6.
$$

AI 科學加速可能讓其中：

$$
X_1\rightarrow L_4,
$$

$$
X_2\rightarrow L_3,
$$

$$
X_3\rightarrow L_8.
$$

所以：

$$
\boxed{
\text{AI accelerates separation of the adjacent possible from the impossible}.
}
$$

---

# 57. 「科幻邊界壓縮」的正式版本

定義科幻候選集合：

$$
\mathcal F.
$$

工程可達集合：

$$
\mathcal R_{A,t}.
$$

兩者距離：

$$
D_{\mathrm{FR}}(t).
$$

AI 若降低高彈性 barrier，

可能：

$$
D_{\mathrm{FR}}(t)
\downarrow.
$$

但不是所有：

$$
x\in\mathcal F
$$

都會進入：

$$
\mathcal R.
$$

---

# 58. Realizability Migration

一項概念可能沿：

$$
\text{fiction}
\rightarrow
\text{formal model}
\rightarrow
\text{simulation}
\rightarrow
\text{prototype}
\rightarrow
\text{technology}
\rightarrow
\text{infrastructure}
$$

移動。

AI 可能加速中間多個 transition。

因此：

$$
\boxed{
\text{AI leverage}
\text{ can act on the migration rate}.
}
$$

而不是直接改變終點是否 fundamental possible。

---

# 59. AI 奇點的新定義接口

若 AI 對大量技術候選：

$$
X_i
$$

同時降低：

$$
B_{\mathrm{search}},
B_{\mathrm{design}},
B_{\mathrm{control}},
B_{\mathrm{experiment}},
$$

則文明可能出現：

$$
\frac{d\mu(\mathcal R_{A,t})}{dt}
$$

顯著增加。

這種：

$$
\boxed{
\text{reachable-domain acceleration}
}
$$

可以作為「技術型 AI 奇點」的一種比單純模型智商更物理化的定義。

---

# 60. 但研究加速會碰到實體吞吐上限

即使：

$$
T_{\mathrm{reasoning}}\rightarrow0,
$$

實驗仍可能需要：

- 晶體成長幾天；
- 生物反應幾週；
- 大型設施排程；
- 能源充電；
- 製造時間。

因此總週期：

$$
T_{\mathrm{cycle}}
=
T_{\mathrm{think}}
+
T_{\mathrm{sim}}
+
T_{\mathrm{fabricate}}
+
T_{\mathrm{experiment}}
+
T_{\mathrm{verify}}.
$$

若：

$$
T_{\mathrm{experiment}}
$$

主導，

純推理再快也有 diminishing returns。

---

# 61. Amdahl-like science acceleration

令：

$$
f_{\mathrm{AI}}
$$

為可被 AI 高度加速的流程比例，

其加速倍數：

$$
s_{\mathrm{AI}}.
$$

則研究週期理想化上限可類比：

$$
\boxed{
S_{\mathrm{total}}
\lesssim
\frac{
1
}{
(1-f_{\mathrm{AI}})
+
f_{\mathrm{AI}}/s_{\mathrm{AI}}
}.
}
$$

這不是物理定律，

而是一個提醒：

> 不可加速的實體流程會成為新瓶頸。

---

# 62. AI 加速會使瓶頸轉移

當：

$$
B_{\mathrm{search}}\downarrow,
$$

新的主瓶頸可能變成：

$$
B_{\mathrm{fab}}.
$$

再降低 fabrication 後，

可能變成：

$$
B_{\mathrm{energy}}.
$$

因此：

$$
\boxed{
\text{Acceleration}
\rightarrow
\text{bottleneck migration}.
}
$$

這是 DTRC 必須動態更新的原因。

---

# 63. 最終難度由最硬瓶頸支配

可粗略表示：

$$
D_X
\approx
\max_i
B_i.
$$

或更一般：

$$
D_X
=
F(B_1,\ldots,B_n).
$$

若最大 barrier：

$$
B_j
$$

具有：

$$
\eta_j^{\mathrm{AI}}\approx0,
$$

則即使其他 barrier 大幅下降，

整體技術仍可能幾乎不動。

---

# 64. AI 不能替代新物理，但可以提高找到新物理的概率

若現有模型：

$$
M
$$

不完備，

AI 可以擴大：

$$
\Omega_{\mathrm{theory}}.
$$

這提高：

$$
P(
\text{find better model}
).
$$

但：

$$
\boxed{
\text{model proposal}
\neq
\text{new law of nature}.
}
$$

新物理仍需要：

$$
\text{prediction}
+
\text{experiment}
+
\text{replication}.
$$

---

# 65. 自主科學是否會走向「科學超智能」？

2026 年文獻已有「collective scientific superintelligence」的研究願景語言。

本文不把它當成已實現狀態。

更安全的定義是：

若研究系統在：

- hypothesis；
- experiment；
- instrument；
- integration；
- verification；

多環節形成高自治閉環，

且：

$$
\Phi_{\mathrm{sci}}
$$

持續超過傳統組織，

可以說它具有：

$$
\text{scientific-superintelligence-like functional regime}.
$$

---

# 66. 真正關鍵是 autonomy × evidence

如果只有：

$$
A_{\mathrm{auto}}\uparrow
$$

而：

$$
E_{\mathrm{evidence}}\downarrow,
$$

系統會變成高速生成器。

因此：

$$
\boxed{
\text{Scientific Autonomy}
=
\text{Autonomy}
\times
\text{Evidence Discipline}.
}
$$

任一接近零，

整體價值都很低。

---

# 67. 自主科學的治理約束

至少需要：

$$
G_{\mathrm{sci}}
=
\left(
G_{\mathrm{permission}},
G_{\mathrm{safety}},
G_{\mathrm{provenance}},
G_{\mathrm{replication}},
G_{\mathrm{rollback}}
\right).
$$

因為具身 AI 能：

> 寫錯答案。

也能：

> 做錯實驗。

兩者風險完全不同。

---

# 68. AI 改變的是「難度曲線」，不是「真理標準」

不論 AI 多強，

科學命題仍需要：

$$
\boxed{
\text{evidence}
+
\text{reproducibility}
+
\text{model adequacy}.
}
$$

因此：

$$
\boxed{
\text{AI-native science}
\neq
\text{post-empirical science}.
}
$$

---

# 69. 二十個核心命題

## 命題一：AI 槓桿是障礙型別相對的

$$
L_{\mathrm{AI}}
=
L_{\mathrm{AI}}(B_i).
$$

## 命題二：AI 不等於 law-breaking power

$$
L_{\mathrm{AI}}\gg0
\not\Rightarrow
P_{\mathrm{forbidden}}\rightarrow P_{\mathrm{allowed}}.
$$

## 命題三：可自動 evaluator 提高 AI 搜尋槓桿

$$
E_{\mathrm{eval}}\uparrow
\Rightarrow
L_S\uparrow
$$

作為任務相對假說。

## 命題四：proposal throughput 非 discovery throughput

$$
N_{\mathrm{proposal}}\uparrow
\not\Rightarrow
N_{\mathrm{valid}}\uparrow.
$$

## 命題五：simulation acceleration 需要模型有效性

$$
\widehat M
\not\approx
M
\Rightarrow
\text{optimized solution may fail}.
$$

## 命題六：設計空間非製造空間

$$
\mathcal D_{\mathrm{design}}
\not\subseteq
\mathcal D_{\mathrm{fab}}
$$

一般可能成立。

## 命題七：控制提高 operational reachability

$$
L_C\uparrow
\Rightarrow
\mathcal R_{\mathrm{op}}\uparrow
$$

不推出 fundamental possibility set 擴張。

## 命題八：AI 可提高每實驗信息增益

$$
L_E
\rightarrow
\mathbb E[\Delta I]/N_{\mathrm{exp}}
\uparrow
$$

在有效設計下。

## 命題九：自治非可靠

$$
\text{autonomous}
\not\Rightarrow
\text{correct}.
$$

## 命題十：驗證 AI 可加速否證

$$
L_V>0
$$

可使 DTRC 往更高不可能性層級移動。

## 命題十一：障礙彈性依任務與時代而變

$$
\eta_i^{\mathrm{AI}}
=
\eta_i^{\mathrm{AI}}(X,t,E).
$$

## 命題十二：logical/fundamental barrier 在固定前提下 AI 彈性近零

$$
\eta_{\mathrm{hard}}^{\mathrm{AI}}
\approx0.
$$

## 命題十三：自主科學要最大化 validated information gain

$$
\Phi_{\mathrm{sci}}
=
\mathbb E[\Delta I_{\mathrm{validated}}]/T.
$$

## 命題十四：高 throughput 非高 truth

$$
\text{throughput}
\not\Rightarrow
\text{truth}.
$$

## 命題十五：具身自主科學需要物理安全閉環

$$
\text{AI intent}
\rightarrow
\text{runtime-governed action}.
$$

## 命題十六：加速會造成瓶頸遷移

$$
B_i\downarrow
\Rightarrow
\arg\max_j B_j
\text{ may change}.
$$

## 命題十七：實體流程限制總加速上限

$$
T_{\mathrm{physical}}>0
$$

會造成 diminishing returns。

## 命題十八：AI 可加速「證明不可能」

$$
\text{better AI}
\not\Rightarrow
\text{more technologies feasible}.
$$

## 命題十九：科幻—工程距離可以被 AI 壓縮，但不是全部候選

$$
D_{\mathrm{FR}}\downarrow
$$

不代表：

$$
\mathcal F\subseteq\mathcal R.
$$

## 命題二十：AI 奇點可被重述為可達域加速度

$$
a_R
=
\frac{d^2\mu(\mathcal R)}{dt^2}
$$

可作為技術型 AI 奇點的候選量，而非完成定義。

---

# 70. 理論邊界

本文不宣稱：

1. AI 會使所有科幻技術最終可行；
2. self-driving laboratories 已成為通用自主科學家；
3. AlphaEvolve 類系統可以解所有科學問題；
4. 障礙彈性 $\eta_i^{\mathrm{AI}}$ 已有普適實證標準；
5. autonomous science 可以不需要人類治理；
6. AI 可以突破邏輯矛盾或 genuine fundamental no-go；
7. 模擬可以替代關鍵實驗；
8. 更快科研一定導致更安全文明；
9. 多 Agent 一定優於單 Agent；
10. 時間旅行因 AI 進步而必然更接近工程實現。

本文完成的是：

$$
\boxed{
\text{把「AI 會讓科幻成真」
改寫成
「AI 對哪些 barrier 具有多大的可壓縮槓桿」。}
}
$$

---

# 71. 結論：AI 不會取消物理世界，但會重新塑造文明抵達物理世界的路徑

Paper 03 定義：

$$
\mathcal D_X
=
\left\langle
P,S,E,R,C,V,L_{\mathrm{AI}},U
\right\rangle.
$$

本篇將：

$$
L_{\mathrm{AI}}
$$

展開成：

$$
\boxed{
L_{\mathrm{AI}}
=
\left\langle
L_H,
L_S,
L_{\mathrm{sim}},
L_D,
L_C,
L_E,
L_V,
L_M
\right\rangle.
}
$$

真正重要的是：

$$
\boxed{
\text{AI can reduce search distance to reachable physics;}
\quad
\text{it does not enlarge physics by assertion}.
}
$$

它能：

- 更快找理論；
- 更快找反例；
- 更快搜尋設計；
- 更快模擬；
- 更精密控制；
- 更聰明選實驗；
- 更快驗證；
- 更完整維護研究狀態。

於是：

$$
T_{\mathrm{cycle}}\downarrow,
$$

$$
\Phi_{\mathrm{sci}}\uparrow,
$$

文明的：

$$
\mathcal R_{A,t}
$$

可能更快變形與擴張。

但當主障礙是：

$$
B_{\mathrm{logic}}
$$

或：

$$
B_{\mathrm{law}},
$$

AI 真正的價值反而是：

> 更快告訴我們，哪裡沒有路。

因此 AI 對 frontier science 的最大意義，不是讓：

$$
\text{impossible}
\rightarrow
\text{possible}
$$

自動發生，

而是讓：

$$
\boxed{
\text{unknown}
\rightarrow
\text{discoverable}
\quad\text{or}\quad
\text{provably constrained}
}
$$

的速度增加。

Series 02 下一篇將因此從「技術障礙」轉向「世界本身提供什麼操作空間」。

# Paper 05  
## 〈時空的可供性：哪種時空給存在者哪些能力？〉

那篇要問的不是：

> 某技術難不難？

而是更上游的：

> **不同時空結構本身，究竟允許其中的存在者觀察、記錄、導航、修改、分支、退出與生成到什麼程度？**

這將正式把 Series 02 從「技術可達性」推進到：

$$
\boxed{
\text{Spacetime Affordance}.
}
$$

---

## 參考研究脈絡

- Neo.K，2026，《從科幻到工程：幻想—實現邊界壓縮與 AI 奇點的新定義》。
- Neo.K，2026，《具身化 AI 自主研究閉環：從假說生成、物理實驗到證據判定與概念修正》。
- Neo.K，2026，《異常即入口：具身自主研究中的反例、失敗、離群事件與未知管理》。
- Neo.K，2026，《可行／不可行二分的終結：動態技術可達性分類》。
- Richard B. Canty & Milad Abolhasani, “The past, present and future of self-driving laboratories”, *Nature Reviews Chemistry*, 2026.
- Linjiang Chen et al., “Self-driving laboratories need an autonomy safety harness”, *Nature Synthesis*, 2026.
- A. Gilad Kusne & Austin McDannald, “Managing autonomous materials labs with multi-agent AI and its implications for the science of science”, *Communications Materials*, 2026.
- Aikaterini Vriza et al., “Operating advanced scientific instruments with AI agents that learn on the job”, *npj Computational Materials*, 2026.
- Gerbrand Ceder et al., “An autonomous laboratory for the accelerated synthesis of inorganic materials”, *Nature*, 2023, updated 2026.
- Google DeepMind, AlphaEvolve technical communications, 2025–2026, as an example of LLM-guided algorithm search with automated evaluators.
