# EXS-07｜會自己打科技樹的科技：從外部能力到自我延展文明
## 當能力網路出現能修改能力網路本身的節點

**系列：** Human Capability Externalization & Intelligence Substrate Evolution Series  
**系列中文名：** 人類能力外部化與智能載體演化系列  
**編號：** EXS-07  
**版本：** v1.0  
**日期：** 2026-08-18  
**狀態：** Canonical Source / UTF-8 Markdown  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

EXS-01 至 EXS-06 建立了一條長歷史：人類透過工具、感官裝置、外部記憶、機械、計算機與 AI，把原本受限於生物身體與個體認知的能力逐步配置到外部載體；當外部載體成為基礎設施時，又產生能力依賴、韌性、系統邊界與載體多樣化問題。本文作為第一系列終篇，進一步提出一個真正具有相位轉換意味的問題：如果外部能力系統本身開始能搜尋、選擇、設計、驗證、組合、修改甚至製造新的能力系統，那麼人類數百萬年的「造工具」歷史是否正在跨入「工具開始造工具」的階段？

本文拒絕把真實文明簡化成遊戲式的線性 Technology Tree，而以「Capability Graph」表示文明能力網路：

$$
\boxed{
\mathcal G_t
=
(
V_t,
E_t,
W_t
)
}
$$

其中 $V_t$ 包含工具、演算法、模型、知識、制度、機器、實驗方法與基礎設施等能力節點； $E_t$ 表示依賴、轉換、組合與生成關係； $W_t$ 則表示成本、效能、風險、可得性、可靠性與其他權重。傳統人類文明主要由人類研究者、工程師與制度共同執行：

$$
H:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
$$

AI 的新意則可能是：

$$
\boxed{
A:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
}
$$

亦即能力圖內部第一次大規模出現能修改節點、邊與權重的人工節點。

本文將這種能力稱為：

$$
\boxed{
\text{Capability-Graph-Editing Intelligence}
}
$$

並區分「直接遞迴自我改進」與「間接遞迴自我延展」。前者要求 AI 直接修改自身模型或演算法；後者則允許 AI 透過改善資料中心排程、晶片設計、能源效率、科研工具、實驗方法或製造流程，間接提高下一輪 AI 與文明能力。後者在現實中可能更早、更廣泛，也更容易被忽略。

當前實證已出現數個早期碎片。A-Lab 在 17 天閉環運作中執行 353 次實驗，成功合成 57 個目標中的 36 個，將計算、文獻、機器學習、主動學習、機器人實驗與失敗回饋整合為實驗閉環。AlphaEvolve 則把 AI 產生的演算法實際用於 Google 資料中心排程、硬體設計與 AI 訓練，其中資料中心排程解法平均回收約 $0.7\%$ 全球計算資源，另有演算法被整合進即將到來的 TPU，並將 Gemini 訓練時間降低約 $1\%$。2026 年 AlphaEvolve 進一步一般可用於 Google Cloud；同年的 Robin multi-agent system 已把文獻搜尋、假說生成與實驗資料分析連成半自主生物研究循環；autonomous materials lab 研究則開始討論由單一分散式 AI 或多 agent AI 管理更大規模研究活動、工具與資源。

這些案例尚未構成「文明自我發展」，更不等於 AI 奇點。本文特別區分六個層次：候選生成、可驗證改進、工具設計、實驗閉環、製造／部署閉環，以及能力環境自我重構。只有當智能系統不只提出候選，而能持續把經驗證的新能力轉化為下一輪可用的工具、機器、算力、能源、科研與基礎設施時，才開始接近「自我延展文明」。

本文亦保留「Reality Bandwidth」限制。數位世界可以快速生成、搜索與驗證大量候選，但材料合成、工廠建造、電網擴張、長期安全測試與社會協調仍受物理與制度時間約束。因此：

$$
\boxed{
\text{Capability-Graph Editing}
\neq
\text{Instant Physical Realization}.
}
$$

第一系列最後的核心結論是：AI 的真正歷史特殊性不在於「人類第一次依賴外部工具」，而在於人類長期建立的外部能力網路中，開始出現能主動修改、擴張與重組這張網路本身的人工節點。這使能力外部化從：

$$
\boxed{
\text{External Extension}
}
$$

逐步轉向：

$$
\boxed{
\text{Self-Extending Extension}.
}
$$

這一轉折也正式把第一系列交接給第二系列「Systemic AI Singularity, Reality Bandwidth & Post-Tool Civilization」：真正的 AI 奇點將不只問 AI 是否能改進 AI，而要問整個智能—算力—能源—製造—科研—具身系統何時形成可持續的正向再生閉環。

---

## 關鍵詞

能力圖；Capability Graph；Capability-Graph-Editing Intelligence；科技樹；自我延展文明；自動實驗室；A-Lab；AlphaEvolve；自主科研；AI Scientist；間接遞迴自我改進；工具生成工具；Reality Bandwidth；系統奇點；後工具文明

---

# 1. 第一系列終點：人類一直在造工具，現在工具開始碰到「造工具」這件事

EXS-01 的核心是：

$$
\boxed{
\text{Internal Capability}
\neq
\text{Accessible Capability}.
}
$$

EXS-02：

$$
\boxed{
\text{Accessible Capability}
\neq
\text{Resilient Capability}.
}
$$

EXS-03：

$$
\boxed{
\text{Humanly Usable Knowledge}
\neq
\text{Humanly Executed Every Step}.
}
$$

EXS-04：

$$
\boxed{
\text{AI Presence}
\neq
\text{AI Penetration}
\neq
\text{AI Dependency}.
}
$$

EXS-05：

$$
\boxed{
\text{AI Capability}
\neq
\text{AI Architectural Nativity}.
}
$$

EXS-06：

$$
\boxed{
\text{Machine}
\neq
\text{the universal boundary of intelligence}.
}
$$

本文最後要問：

> 當這些外部能力載體本身具有搜尋、推論、設計、操作與生成能力時，能力外部化是否開始反身化？

---

# 2. 遊戲科技樹是一個非常好的直覺，但真實文明不是樹

在許多文明、生存、工業與科技類遊戲中：

$$
T_1
\rightarrow
T_2
\rightarrow
T_3.
$$

玩家：

1. 發現資源；
2. 解鎖技術；
3. 建造工具；
4. 生產更好的工具；
5. 解鎖下一層科技。

這個比喻非常直觀。

但真實世界不是：

$$
\boxed{
\text{Technology Tree}.
}
$$

更接近：

$$
\boxed{
\text{Capability Graph}.
}
$$

---

# 3. Capability Graph

本文定義：

$$
\boxed{
\mathcal G_t
=
(
V_t,
E_t,
W_t
).
}
$$

其中：

$$
V_t
=
\text{capability nodes},
$$

$$
E_t
=
\text{dependency / transformation relations},
$$

$$
W_t
=
\text{cost, efficiency, risk and other weights}.
$$

---

# 4. 什麼可以是能力節點？

 $V_t$ 不只包含機器。

它可以包含：

- tool；
- scientific theory；
- algorithm；
- model；
- dataset；
- manufacturing process；
- laboratory；
- institution；
- energy system；
- transport；
- robot；
- standard；
- law；
- human expertise。

因此：

$$
\boxed{
\text{Technology}
\subset
\text{Capability}.
}
$$

---

# 5. 為什麼制度也是能力節點？

例如一台機器：

$$
M
$$

理論上可以運行。

但如果：

- 沒有供應鏈；
- 沒有維修；
- 沒有合格工程師；
- 沒有法規許可；
- 沒有融資；

則：

$$
M
$$

不一定形成文明可達能力。

因此：

$$
\boxed{
\text{Artifact}
\neq
\text{Usable Capability}.
}
$$

---

# 6. 邊 $E_t$ 才是科技史真正困難的部分

蒸汽機不是孤立出現。

它依賴：

- metallurgy；
- machining；
- mining；
- fuel；
- transport；
- measurement。

現代 AI 也依賴：

- semiconductor；
- data；
- algorithms；
- electricity；
- networks；
- cooling；
- capital。

所以：

$$
\boxed{
\text{Node Existence}
\neq
\text{Capability Availability}.
}
$$

必須有：

$$
\boxed{
\text{supporting path through }\mathcal G.
}
$$

---

# 7. 能力圖中的權重 $W_t$

兩條路徑：

$$
P_1
$$

與：

$$
P_2
$$

都能完成：

$$
F.
$$

但：

$$
W(P_1)\neq W(P_2).
$$

差異可能包括：

- cost；
- time；
- energy；
- reliability；
- safety；
- scalability。

因此技術進步很多時候不是新增節點。

而是：

$$
\boxed{
\Delta W(E)<0
}
$$

降低某條能力路徑的成本。

---

# 8. 演算法改進就是典型的「改邊權」

假設：

$$
F
$$

需要：

$$
C=100.
$$

新演算法：

$$
C=70.
$$

沒有新的 GPU。

沒有新的工廠。

但：

$$
\boxed{
\text{effective capability}
\uparrow.
}
$$

這就是：

$$
\boxed{
\text{Capability Graph Weight Editing}.
}
$$

---

# 9. 人類一直都是能力圖的主要編輯者

傳統文明主要由：

$$
H
$$

執行：

$$
\boxed{
H:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
}
$$

人類：

- 發現；
- 發明；
- 實驗；
- 修改；
- 製造；
- 部署。

因此：

$$
\boxed{
\text{Human Civilization}
}
$$

本身就是：

$$
\boxed{
\text{iterative capability-graph editing}.
}
$$

---

# 10. AI 的真正新問題

如果：

$$
A
$$

只是工具：

$$
H
\rightarrow
A
\rightarrow
y.
$$

這仍是：

$$
H
$$

在編輯 $\mathcal G$。

如果：

$$
A
$$

開始：

- 找問題；
- 提方案；
- 寫演算法；
- 設計實驗；
- 分析結果；
- 修改工具；

則：

$$
\boxed{
A:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
}
$$

這才是關鍵。

---

# 11. 定義 Capability-Graph-Editing Intelligence

本文定義：

$$
\boxed{
CGEI
=
\text{Capability-Graph-Editing Intelligence}.
}
$$

其最低條件是：

> 系統能自主或半自主選擇並產生會改變其他能力節點、依賴關係或成本權重的候選修改。

因此：

$$
\boxed{
\Delta V
\lor
\Delta E
\lor
\Delta W
\neq0.
}
$$

---

# 12. CGEI 不要求 AGI

一個非常窄的系統可以：

> 只會找更好的矩陣乘法。

但如果其輸出：

$$
\Delta W_{\mathrm{compute}}<0,
$$

它仍然在修改能力圖。

因此：

$$
\boxed{
CGEI
\neq
AGI.
}
$$

---

# 13. CGEI 也不要求主體性

一個完全沒有：

- 感質；
- 自我認同；
- 權利主張；

的系統，

仍然可以：

$$
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
$$

所以：

$$
\boxed{
\text{Capability-Graph Editing}
\neq
\text{Subjectivity}.
}
$$

---

# 14. 第一層：候選生成

最弱形式：

$$
\boxed{
G_1
=
\text{Candidate Generation}.
}
$$

AI 生成：

- hypotheses；
- algorithms；
- materials；
- designs；
- code。

但：

$$
\boxed{
\text{candidate}
\neq
\text{capability}.
}
$$

---

# 15. 第二層：可自動評分候選

若有：

$$
E(x)
=
\text{evaluator}.
$$

則：

$$
A
\rightarrow
x_1,\ldots,x_n
\rightarrow
E
\rightarrow
x^*.
$$

這使：

$$
\boxed{
\text{search}
+
\text{verification}
}
$$

形成數位閉環。

---

# 16. AlphaEvolve：一個非常乾淨的數位能力圖編輯案例

Google DeepMind 2025 發表 AlphaEvolve。

其核心不是只寫一次程式。

而是：

$$
\boxed{
\text{Generate}
\rightarrow
\text{Run}
\rightarrow
\text{Score}
\rightarrow
\text{Select}
\rightarrow
\text{Generate Again}.
}
$$

其 evaluator 可對候選程式給出：

- correctness；
- speed；
- other measurable objectives。

---

# 17. AlphaEvolve 改的是什麼？

它改進了：

- data center scheduling；
- hardware design；
- AI training；
- matrix algorithms；
- mathematical solutions。

因此：

$$
\boxed{
\Delta E
+
\Delta W
}
$$

都可能發生。

---

# 18. 資料中心排程：能力圖的權重被真實改變

DeepMind 表示 AlphaEvolve 找出的排程 heuristic 已部署於 Google Borg。

平均可回收約：

$$
0.7\%
$$

Google 全球計算資源。

因此：

$$
\boxed{
\text{same physical compute}
\rightarrow
\text{more effective compute}.
}
$$

這正是：

$$
\boxed{
W_{\mathrm{compute}}\downarrow.
}
$$

---

# 19. 這不是「AI 幫 Google 省一點錢」而已

若：

$$
C_{\mathrm{effective}}
\uparrow,
$$

則：

$$
\text{AI training},
$$

$$
\text{research},
$$

$$
\text{services}
$$

都能使用更多算力。

因此：

$$
\boxed{
\text{algorithm improvement}
\rightarrow
\text{capability environment improvement}.
}
$$

---

# 20. 硬體設計：節點本身也開始被 AI 修改

AlphaEvolve 提出 Verilog rewrite。

DeepMind 表示該改動：

- 移除矩陣運算電路中的不必要 bits；
- 通過 robust verification；
- 被整合進 upcoming TPU。

這代表：

$$
\boxed{
A_{\mathrm{software}}
\rightarrow
\Delta H_{\mathrm{hardware}}.
}
$$

---

# 21. AI 參與設計 AI 自己需要的晶片

若：

$$
A
$$

改進：

$$
H_{\mathrm{AI}},
$$

而：

$$
H_{\mathrm{AI}}
$$

再支援：

$$
A',
$$

則：

$$
\boxed{
A
\rightarrow
H
\rightarrow
A'.
}
$$

這已是：

$$
\boxed{
\text{indirect recursive self-extension}.
}
$$

---

# 22. AlphaEvolve 也直接改進 AI 訓練

DeepMind 報告：

- 某 Gemini matrix kernel 提速約 $23\%$ ；
- Gemini 訓練時間降低約 $1\%$ ；
- FlashAttention GPU kernel 最高提速約 $32.5\%$。

因此：

$$
\boxed{
A_t
\rightarrow
\Delta C
\rightarrow
A_{t+1}.
}
$$

---

# 23. 這已經是遞迴自我改進嗎？

需要小心。

若定義：

$$
\text{Recursive Self-Improvement}
=
A_t
\rightarrow
A_{t+1}
$$

則 AlphaEvolve 顯示某些早期碎片。

但它仍然依賴：

- 人類設定目標；
- evaluator；
- production pipeline；
- hardware teams。

所以本文不稱它為：

$$
\boxed{
\text{autonomous runaway RSI}.
}
$$

---

# 24. 更好的詞：間接遞迴自我延展

本文定義：

$$
\boxed{
IRSE
=
\text{Indirect Recursive Self-Extension}.
}
$$

即：

$$
A
\rightarrow
X
\rightarrow
A',
$$

其中 $X$ 可以是：

- algorithm；
- chip；
- energy；
- tool；
- dataset；
- laboratory；
- manufacturing process。

---

# 25. 為什麼 IRSE 比「自己改自己的權重」更重要？

傳統奇點敘事常想像：

$$
A
\rightarrow
A'
\rightarrow
A''.
$$

但現實文明更可能是：

$$
\boxed{
A
\rightarrow
\text{chip}
\rightarrow
\text{compute}
\rightarrow
\text{science}
\rightarrow
\text{energy}
\rightarrow
A'.
}
$$

迴圈更長。

但可能更真實。

---

# 26. 第三層：AI 設計可以被物理實驗驗證

數位 evaluator 的優勢是：

$$
\tau_{\mathrm{eval}}
\ll
\tau_{\mathrm{physical}}.
$$

但材料、化學、機器人等問題需要：

$$
\boxed{
\text{physical loop}.
}
$$

這就是 autonomous laboratory 的意義。

---

# 27. A-Lab：能力圖編輯進入物理世界

A-Lab 結合：

- ab initio database；
- literature；
- ML；
- active learning；
- robotics；
- XRD characterization。

完整流程：

$$
\boxed{
\text{Target}
\rightarrow
\text{Recipe}
\rightarrow
\text{Robot Experiment}
\rightarrow
\text{Characterization}
\rightarrow
\text{Analysis}
\rightarrow
\text{New Recipe}.
}
$$

---

# 28. A-Lab 的 17 天閉環

A-Lab 在：

$$
17
$$

天連續運行中，

執行：

$$
353
$$

次 synthesis experiments，

成功實現：

$$
36/57
$$

個目標材料。

這不是無限自主。

但它證明：

$$
\boxed{
\text{AI-guided physical iteration}
}
$$

已可形成實驗閉環。

---

# 29. 失敗本身也變成能力圖更新

當某個配方失敗：

$$
R_i
\rightarrow
\text{failure},
$$

A-Lab 不只是：

> 報錯。

而是：

$$
\boxed{
\text{failure}
\rightarrow
\text{active learning}
\rightarrow
R_{i+1}.
}
$$

因此：

$$
\boxed{
\text{failure}
}
$$

被轉成：

$$
\boxed{
\text{graph update signal}.
}
$$

---

# 30. 這正是人類科學一直在做的事

人類科研：

$$
\text{Hypothesis}
\rightarrow
\text{Experiment}
\rightarrow
\text{Failure}
\rightarrow
\text{Revision}.
$$

A-Lab 的重要性不是：

> AI 發明了科學方法。

而是：

$$
\boxed{
\text{parts of the scientific iteration loop become machine-executable}.
}
$$

---

# 31. 第四層：AI 開始處理「研究策略」本身

2026 年 autonomous materials labs 研究已開始討論：

- single distributed AI；
- multi-agent AI；
- lab tools；
- resource management；
- research campaigns；
- digital sandbox；
- physical sandbox。

這開始從：

$$
\boxed{
\text{Which experiment next?}
}
$$

上升到：

$$
\boxed{
\text{How should a research system allocate its attention and resources?}
}
$$

---

# 32. 研究管理本身也是能力節點

如果科研效率：

$$
\eta_R
$$

提高，

即使：

$$
\text{same scientists}
+
\text{same labs}
$$

也可以：

$$
\text{discoveries/time}
\uparrow.
$$

所以：

$$
\boxed{
\text{Research Management}
}
$$

本身是：

$$
\boxed{
V_{\mathcal G}.
}
$$

---

# 33. 科技圖編輯不只是在發明「東西」

AI 也可以改進：

- experiment order；
- lab utilization；
- data collection；
- verification；
- collaboration；
- scheduling。

所以：

$$
\boxed{
\text{Capability Graph Editing}
\neq
\text{Artifact Invention Only}.
}
$$

---

# 34. Robin：從實驗選擇進一步走到假說循環

2026 年 Nature 發表 Robin multi-agent system。

Robin 可以：

- literature search；
- hypothesis generation；
- experiment proposal；
- data analysis；
- updated hypothesis generation。

研究中人類仍執行實驗並把數據交回系統。

因此應稱：

$$
\boxed{
\text{semi-autonomous scientific discovery loop}.
}
$$

---

# 35. Robin 的重要性不在「AI 完全取代科學家」

恰恰相反。

其意義在於：

$$
\boxed{
\text{Hypothesis Layer}
}
$$

與：

$$
\boxed{
\text{Analysis Layer}
}
$$

已可被 agent 化。

這表示：

$$
\boxed{
\text{scientific graph editing}
}
$$

正往更高抽象層前進。

---

# 36. 第五層：工具設計工具

如果：

$$
A
$$

設計：

$$
T,
$$

而：

$$
T
$$

讓：

$$
A
$$

更強，

則：

$$
\boxed{
A
\rightarrow
T
\rightarrow
A'.
}
$$

這是：

$$
\boxed{
\text{Tool-Producing Tool}.
}
$$

---

# 37. 第六層：工具設計「工具生產系統」

再往上一層：

$$
A
\rightarrow
F_T,
$$

其中：

$$
F_T
=
\text{factory that produces tools}.
$$

那就變成：

$$
\boxed{
\text{Tool}
\rightarrow
\text{Tool-Producing Infrastructure}.
}
$$

---

# 38. 第七層：能力環境自我重構

真正深層的情況：

$$
A
$$

可以改變：

- compute；
- energy；
- manufacturing；
- logistics；
- science；
- infrastructure。

則：

$$
\boxed{
A:
\mathcal G
\rightarrow
\mathcal G'.
}
$$

而：

$$
\mathcal G'
$$

又使：

$$
A'
$$

更強。

這就是：

$$
\boxed{
\text{Self-Extending Capability Environment}.
}
$$

---

# 39. 這才開始接近真正的系統性奇點

但本文不在此定義奇點。

只留下：

$$
\boxed{
\text{Self-Extending Capability Environment}
}
$$

作為第二系列入口。

真正奇點還需要：

- sustained loop；
- physical realization；
- positive net resource effect；
- resilience；
- repeatability。

---

# 40. 生成候選不等於自我延展文明

如果 AI 每秒產生：

$$
10^9
$$

個點子，

但：

$$
0
$$

個被驗證與部署，

則：

$$
\boxed{
\Delta\mathcal G_{\mathrm{usable}}
\approx0.
}
$$

所以：

$$
\boxed{
\text{Idea Generation}
\neq
\text{Capability Growth}.
}
$$

---

# 41. 數位驗證也不等於世界實現

若：

$$
A
$$

找到一個數學上正確的設計，

仍可能需要：

- material；
- factory；
- regulation；
- construction；
- capital；
- time。

因此：

$$
\boxed{
\text{Digitally Verified}
\neq
\text{Physically Realized}.
}
$$

---

# 42. Reality Bandwidth 再次出現

令：

$$
B_D
=
\text{digital capability-generation bandwidth},
$$

$$
B_R
=
\text{reality realization bandwidth}.
$$

若：

$$
B_D\gg B_R,
$$

則：

$$
\boxed{
\text{Capability Backlog}
\uparrow.
}
$$

---

# 43. 科技圖可能「想好了，但還沒蓋出來」

這將成為奇點前很合理的文明狀態：

$$
\boxed{
\mathcal G_{\mathrm{known}}
\supset
\mathcal G_{\mathrm{realized}}.
}
$$

也就是：

> 已知可行能力比實際部署能力多很多。

---

# 44. 物理時間仍然存在

某些事情：

$$
\text{more compute}
\Rightarrow
\tau\downarrow.
$$

但：

- curing；
- aging；
- construction；
- ecological observation；
- long-term durability；

可能具有：

$$
\boxed{
\text{irreducible physical latency}.
}
$$

所以：

$$
\boxed{
\text{Self-Extending Intelligence}
\neq
\text{Zero-Time Civilization}.
}
$$

---

# 45. 人類制度時間也存在

一個技術可以：

$$
\text{physically feasible}
$$

但：

$$
\text{socially rejected}.
$$

所以：

$$
\boxed{
\text{Capability}
\neq
\text{Deployment Authorization}.
}
$$

---

# 46. 能力圖不是單一最佳化問題

假設：

$$
x_1
$$

提高：

$$
\text{efficiency},
$$

但降低：

$$
\text{safety}.
$$

另一個：

$$
x_2
$$

較慢但可解釋。

因此：

$$
\boxed{
\mathcal G
}
$$

沒有唯一：

$$
\boxed{
\text{global scalar objective}.
}
$$

---

# 47. 多目標能力圖

更合理是：

$$
W
=
(
w_{\mathrm{performance}},
w_{\mathrm{cost}},
w_{\mathrm{energy}},
w_{\mathrm{safety}},
w_{\mathrm{rights}},
w_{\mathrm{resilience}},
\ldots
).
$$

因此：

$$
\boxed{
\text{Capability-Graph Editing}
}
$$

本質上是：

$$
\boxed{
\text{multi-objective optimization}.
}
$$

---

# 48. AI 不能自己決定「文明要優化什麼」作為自然定律

即使 AI：

$$
\text{optimization capability}
\uparrow,
$$

也不能推出：

$$
\boxed{
\text{objective legitimacy}.
}
$$

所以：

$$
\boxed{
\text{Optimization Power}
\neq
\text{Value Authority}.
}
$$

---

# 49. 人類角色可能從「直接研發」往上移

若 AI 承擔更多：

- search；
- design；
- coding；
- experiment；
- analysis；

人類可能轉向：

- goal；
- value；
- constraint；
- anomaly；
- interpretation；
- governance。

所以：

$$
\boxed{
\text{Human Direct Research Share}
\downarrow
}
$$

不必然：

$$
\boxed{
\text{Human Civilizational Role}
\downarrow.
}
$$

---

# 50. 但人類也可能逐漸無法逐步審閱全部科研活動

若：

$$
R_{\mathrm{AI\ research}}
\gg
R_{\mathrm{human\ review}},
$$

則：

$$
\boxed{
\text{review-every-step}
}
$$

會失效。

這直接接回 EXS-03 的：

$$
\boxed{
\text{Human Review Bandwidth}.
}
$$

---

# 51. 科研治理將從逐步批准轉向性質治理

例如不再：

> 每一個 AI 實驗都先讓人批准每一步。

而是：

$$
\boxed{
\text{Define Allowed Domain}
+
\text{Safety Constraints}
+
\text{Audit}
+
\text{Escalation}.
}
$$

這是第二系列治理頻寬的重要前置。

---

# 52. Capability Graph 的安全性也需要型別

對：

$$
\Delta\mathcal G,
$$

可以分類：

- reversible；
- irreversible；
- local；
- global；
- digital；
- physical；
- high-risk；
- low-risk。

因此：

$$
\boxed{
\text{Graph Edit}
\neq
\text{Graph Edit}.
}
$$

不同修改需要不同治理。

---

# 53. 可逆修改與不可逆修改

例如：

$$
\text{software scheduling heuristic}
$$

容易 rollback。

但：

$$
\text{new biological organism release}
$$

可能不可逆。

因此：

$$
\boxed{
R_{\mathrm{rollback}}
}
$$

應成為能力圖編輯的重要變量。

---

# 54. 局部能力圖與全球能力圖

一家公司可以：

$$
\mathcal G_C
$$

快速自我改進。

但：

$$
\mathcal G_{\mathrm{world}}
$$

仍未改變多少。

所以：

$$
\boxed{
\text{Local Self-Extension}
\neq
\text{Civilizational Self-Extension}.
}
$$

---

# 55. 區域閉環可能先於全球閉環

如果某一地區整合：

- AI；
- chip；
- energy；
- manufacturing；
- robotics；
- science；

則：

$$
\boxed{
\mathcal G_R
}
$$

可能形成強正回饋。

其他地區仍沒有。

這將在 SAS-03 變成：

$$
\boxed{
\text{Regional Singularity}.
}
$$

---

# 56. 科技樹不是只有解鎖，也可以被重畫

遊戲科技樹通常：

$$
\text{fixed graph}
+
\text{player unlocks nodes}.
$$

真實 AI 更有趣的情況可能是：

$$
\boxed{
\text{agent edits graph topology}.
}
$$

它可能發現：

> 原來這兩個技術不用照舊順序。

或：

> 原來這個節點可以直接繞過。

所以：

$$
\boxed{
\text{Unlocking}
\neq
\text{Graph Rewriting}.
}
$$

---

# 57. 真正的「會打科技樹」甚至會改科技樹

因此遊戲比喻最後可以分三級。

第一級：

$$
\boxed{
\text{Player unlocks tech tree}.
}
$$

第二級：

$$
\boxed{
\text{AI unlocks tech tree}.
}
$$

第三級：

$$
\boxed{
\text{AI rewrites tech tree}.
}
$$

第三級才是本文最重要的斷點。

---

# 58. 技術樹重寫可能包含發現新的中介節點

假設原本：

$$
A
\rightarrow
C
$$

成本很高。

AI 發現：

$$
A
\rightarrow
B
\rightarrow
C
$$

更便宜。

則：

$$
\boxed{
\Delta V=\{B\}.
}
$$

---

# 59. 也可能刪除不必要節點

原本：

$$
A\rightarrow B\rightarrow C.
$$

AI 找到：

$$
A\rightarrow C.
$$

則：

$$
\boxed{
V'
=
V-\{B\}.
}
$$

這是能力圖壓縮。

---

# 60. 也可能重定義問題本身

最強的科研不是：

> 在固定問題上找更好答案。

而是：

> 發現原本問題的表示方式錯了。

因此：

$$
\boxed{
\text{Problem Representation}
}
$$

也是：

$$
V_{\mathcal G}.
$$

如果 AI 能修改：

$$
\boxed{
\text{representation layer},
}
$$

能力圖編輯深度會更高。

---

# 61. 這就是為什麼「AI 只是比較快的計算器」會失準

計算器：

$$
f(x).
$$

高階 CGEI：

$$
\boxed{
\text{choose }f
+
\text{modify }f
+
\text{invent }g
+
\text{change representation of }x.
}
$$

兩者不是同一功能層。

---

# 62. 但這也不表示 AI 不再是工具

「工具」可以是：

$$
\boxed{
\text{a thing used to achieve ends}.
}
$$

AI 即使能造工具，仍可被人類當作：

$$
\boxed{
\text{meta-tool}.
}
$$

所以：

$$
\boxed{
\text{Tool}
\rightarrow
\text{Meta-Tool}
}
$$

不必自動：

$$
\boxed{
\text{Tool}
\rightarrow
\text{Subject}.
}
$$

---

# 63. 後工具文明的真正含義

「Post-Tool Civilization」不表示：

> 沒有工具。

而是：

$$
\boxed{
\text{tools cease to be passive terminal extensions only}.
}
$$

工具開始：

- select tools；
- operate tools；
- design tools；
- coordinate tools；
- produce tools。

---

# 64. 所以後工具不是「工具消失」

而是：

$$
\boxed{
\text{Tool Relation Changes}.
}
$$

從：

$$
H\rightarrow T
$$

逐漸：

$$
H
\rightarrow
A
\rightarrow
\mathcal T.
$$

甚至：

$$
H
\rightarrow
A
\rightarrow
\mathcal G.
$$

---

# 65. 自我延展文明的最低條件

本文提出：

$$
\boxed{
SEC
=
\text{Self-Extending Civilization}.
}
$$

其最低條件不是：

$$
AI>human.
$$

而是：

$$
\boxed{
\text{system-generated capability improvements}
}
$$

能被：

$$
\boxed{
\text{validated and reintegrated}
}
$$

回系統。

---

# 66. SEC 第一條件：生成

$$
\boxed{
G>0.
}
$$

系統可以提出新的：

- design；
- algorithm；
- process；
- tool。

---

# 67. SEC 第二條件：選擇

$$
\boxed{
S>0.
}
$$

系統可以辨識哪些候選更值得追。

---

# 68. SEC 第三條件：驗證

$$
\boxed{
V>0.
}
$$

系統可以透過：

- formal evaluator；
- simulation；
- experiment；

拒絕錯誤候選。

---

# 69. SEC 第四條件：實現

$$
\boxed{
R>0.
}
$$

候選可以變成：

$$
\boxed{
\text{usable capability}.
}
$$

---

# 70. SEC 第五條件：回灌

$$
\boxed{
F>0.
}
$$

新能力：

$$
C_{t+1}
$$

會提高：

$$
\boxed{
\text{next iteration capability}.
}
$$

---

# 71. 完整最小閉環

因此：

$$
\boxed{
G
\rightarrow
S
\rightarrow
V
\rightarrow
R
\rightarrow
F
\rightarrow
G'.
}
$$

這才是：

$$
\boxed{
\text{Self-Extending Loop}.
}
$$

---

# 72. 今天的系統只完成其中一部分

AlphaEvolve 很強於：

$$
G,S,V.
$$

並有部分：

$$
R,F
$$

進入 production。

A-Lab 很強於：

$$
G,S,V,R
$$

在狹窄材料實驗域。

但全球文明：

$$
\boxed{
G\rightarrow S\rightarrow V\rightarrow R\rightarrow F
}
$$

尚未形成通用自主閉環。

---

# 73. 所以現在還不是「科技樹完全自己打」

更準確：

$$
\boxed{
\text{selected branches of the capability graph}
}
$$

已開始：

$$
\boxed{
\text{partially self-edit}.
}
$$

這是強但保守的說法。

---

# 74. 自我延展不等於無限增長

即使：

$$
F>0,
$$

仍有：

- energy；
- matter；
- heat；
- land；
- entropy；
- social limits。

所以：

$$
\boxed{
\text{Self-Extending}
\neq
\text{Unbounded}.
}
$$

---

# 75. 能力圖可能達到局部飽和

若：

$$
\partial C/\partial t
\rightarrow0,
$$

可能因：

- physical limit；
- local optimum；
- exhausted search space。

因此：

$$
\boxed{
\text{positive loop}
\neq
\text{permanent exponential growth}.
}
$$

---

# 76. 能力圖也可能因複雜度反而退化

新增：

$$
V\uparrow
$$

可能：

$$
\text{coordination cost}\uparrow.
$$

所以：

$$
\boxed{
|\mathcal G|\uparrow
\not\Rightarrow
C_{\mathrm{effective}}\uparrow.
}
$$

---

# 77. 因此 AI 也需要刪枝

CGEI 不只是：

$$
\text{add nodes}.
$$

還需要：

- prune；
- compress；
- standardize；
- retire；
- replace。

所以：

$$
\boxed{
\text{Capability Growth}
=
\text{Expansion}
+
\text{Compression}
+
\text{Replacement}.
}
$$

---

# 78. 技術債也屬於能力圖

新技術：

$$
T
$$

可以：

$$
C\uparrow
$$

但：

$$
M_{\mathrm{maintenance}}\uparrow.
$$

若維護成本過大：

$$
\boxed{
\text{nominal capability}
>
\text{usable capability}.
}
$$

這直接接 EXS-02 的 Capability Debt。

---

# 79. 自動科研可能加速技術債

若 AI：

$$
G\uparrow\uparrow,
$$

但：

$$
\text{maintenance}
$$

跟不上，

文明可能得到：

$$
\boxed{
\text{more inventions than maintainable systems}.
}
$$

因此：

$$
\boxed{
\text{Generation Rate}
}
$$

不是唯一目標。

---

# 80. 自我延展文明需要「退出」能力

如果新能力一旦部署就：

$$
\text{irreversible},
$$

風險上升。

因此：

$$
\boxed{
\text{Rollback}
+
\text{Substitution}
+
\text{Audit}
}
$$

是自我延展文明的重要條件。

---

# 81. 第一系列最後的歷史重寫

人類文明可以被重寫成：

$$
\boxed{
\text{Biological Agent}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Tool User}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Infrastructure Builder}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Computer-Mediated Civilization}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{AI-Mediated Civilization}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Capability-Graph-Editing Civilization}.
}
$$

---

# 82. 核心命題

本文提出以下二十二個核心命題。

## 命題 1

$$
\boxed{
\text{Technology Tree}
\subset
\text{Capability Graph}.
}
$$

## 命題 2

$$
\boxed{
\mathcal G_t
=
(
V_t,
E_t,
W_t
).
}
$$

## 命題 3

$$
\boxed{
\text{Human Civilization}
}
$$

can be interpreted as:

$$
\boxed{
H:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
}
$$

## 命題 4

$$
\boxed{
A:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}
}
$$

defines a capability-graph-editing role.

## 命題 5

$$
\boxed{
CGEI
\neq
AGI.
}
$$

## 命題 6

$$
\boxed{
CGEI
\neq
\text{Subjectivity}.
}
$$

## 命題 7

$$
\boxed{
\text{Candidate}
\neq
\text{Capability}.
}
$$

## 命題 8

$$
\boxed{
\text{Digital Verification}
\neq
\text{Physical Realization}.
}
$$

## 命題 9

$$
\boxed{
\text{Algorithm Improvement}
}
$$

can edit:

$$
\boxed{
W_{\mathcal G}.
}
$$

## 命題 10

$$
\boxed{
\text{AI-designed hardware}
}
$$

can edit:

$$
\boxed{
V_{\mathcal G}
}
$$

and:

$$
\boxed{
E_{\mathcal G}.
}
$$

## 命題 11

$$
\boxed{
\text{Direct RSI}
\neq
\text{Indirect Recursive Self-Extension}.
}
$$

## 命題 12

$$
\boxed{
A
\rightarrow
X
\rightarrow
A'
}
$$

is sufficient for indirect recursive self-extension when $X$ improves AI-relevant capability.

## 命題 13

$$
\boxed{
\text{Autonomous Experimentation}
}
$$

is a physical graph-editing mechanism.

## 命題 14

$$
\boxed{
\text{Research Management}
}
$$

is itself a capability node.

## 命題 15

$$
\boxed{
\text{Graph Editing}
\neq
\text{Graph Realization}.
}
$$

## 命題 16

$$
\boxed{
B_D
\gg
B_R
}
$$

can produce a reality-realization backlog.

## 命題 17

$$
\boxed{
\text{Optimization Power}
\neq
\text{Value Authority}.
}
$$

## 命題 18

$$
\boxed{
\text{Local Self-Extension}
\neq
\text{Civilizational Self-Extension}.
}
$$

## 命題 19

$$
\boxed{
\text{Self-Extending}
\neq
\text{Unbounded}.
}
$$

## 命題 20

$$
\boxed{
|\mathcal G|\uparrow
\not\Rightarrow
C_{\mathrm{effective}}\uparrow.
}
$$

## 命題 21

$$
\boxed{
\text{Capability Growth}
=
\text{Expansion}
+
\text{Compression}
+
\text{Replacement}.
}
$$

## 命題 22

$$
\boxed{
\text{External Extension}
\rightarrow
\text{Self-Extending Extension}.
}
$$

---

# 83. 可檢驗研究計畫

## 83.1 Capability Graph Database

建立跨領域：

$$
\mathcal G_t
$$

資料庫。

節點包括：

- algorithm；
- chip；
- lab；
- energy；
- manufacturing；
- robot；
- institution。

追蹤：

$$
\Delta V,
\Delta E,
\Delta W.
$$

---

## 83.2 AI Graph-Edit Contribution

對每一新能力：

$$
c_i
$$

估計：

$$
\alpha_i
=
\frac{
\text{AI-generated or AI-selected contribution}
}{
\text{total development contribution}
}.
$$

研究：

$$
\alpha_i(t)
$$

是否上升。

---

## 83.3 Direct vs Indirect Self-Improvement

建立：

$$
R_D
=
\text{direct self-improvement rate},
$$

$$
R_I
=
\text{indirect self-extension rate}.
$$

比較：

- model optimization；
- chip design；
- data center scheduling；
- scientific tool improvement。

---

## 83.4 Research Loop Closure Index

定義：

$$
L_R
=
(
G,S,V,R,F
).
$$

測量不同 autonomous lab / AI scientist：

- 生成；
- 選擇；
- 驗證；
- 實現；
- 回灌；

到底完成幾層。

---

## 83.5 Reality Bandwidth Gap

測量：

$$
Q_R
=
\frac{
B_D
}{
B_R
}.
$$

在：

- materials；
- semiconductors；
- energy；
- pharmaceuticals；
- robotics；

中的差異。

---

## 83.6 Capability Backlog

估計：

$$
B_C
=
|\mathcal G_{\mathrm{validated}}|
-
|\mathcal G_{\mathrm{deployed}}|.
$$

研究 AI 增強科研是否使：

$$
B_C\uparrow.
$$

---

## 83.7 Graph Pruning Study

研究 AI 是否能：

- deprecate；
- simplify；
- remove redundant tools；
- reduce technical debt。

避免只研究新增技術。

---

## 83.8 Human Role Shift

追蹤科研工作比例：

$$
H_{\mathrm{execution}},
$$

$$
H_{\mathrm{validation}},
$$

$$
H_{\mathrm{goal}},
$$

$$
H_{\mathrm{governance}}.
$$

研究 AI 增強後的角色重新配置。

---

# 84. 可反駁條件

本文至少存在以下反駁方向。

1. 若 AI 長期只能生成內容，而無法產生任何可驗證的演算法、工具、實驗或工程增量，CGEI 概念的實證範圍需要大幅縮小。
2. 若 AlphaEvolve 類系統無法持續把 AI 生成的演算法部署進真實基礎設施，本文把其視為 graph-editing evidence 的強度需下修。
3. 若 autonomous laboratories 無法穩定形成 experiment-analysis-feedback loop，physical graph editing 命題需弱化。
4. 若 AI 生成的科研候選在物理驗證後成功率長期接近隨機或低於人類方法，AI science acceleration 的一般性需下修。
5. 若 AI 對硬體、演算法與科研的改進不會反過來提高 AI 本身能力，IRSE 的現實重要性需縮小。
6. 若能力網路無法用 graph representation 提供比線性 technology tree 更好的分析力，Capability Graph 模型需要簡化。
7. 若增加技術節點與改變依賴邊在實證上無法分離， $\Delta V/\Delta E/\Delta W$ 分類需重構。
8. 若 Reality Bandwidth 不構成實際科研或部署瓶頸，第二系列對現實頻寬的核心假設需修正。
9. 若研究管理 AI 無法改善科研速度、資源使用或 epistemic outcome，management-as-capability-node 的權重應降低。
10. 若 AI 能力提升始終只能透過 direct model modification，而間接基礎設施路徑沒有顯著貢獻，IRSE 的理論地位需下修。

---

# 85. Non-Claims

本文明確不主張以下命題：

1. 不主張今天的 AI 已能自主完成整個科技發展循環。
2. 不主張 AlphaEvolve 是 AGI。
3. 不主張 AlphaEvolve 已自主控制 Google 全部基礎設施。
4. 不主張 AlphaEvolve 的所有候選都被部署。
5. 不主張 AlphaEvolve 的 $0.7\%$ 計算資源回收代表全球 AI 效率增益。
6. 不主張 AlphaEvolve 的 $1\%$ Gemini 訓練時間改善代表所有 AI 訓練。
7. 不主張 A-Lab 已經完全取代材料科學家。
8. 不主張 A-Lab 的 36/57 成功率可推廣到所有材料領域。
9. 不主張 A-Lab 的 353 次實驗代表所有 autonomous lab 的效率。
10. 不主張 autonomous lab 已完全不需要人類。
11. 不主張 Robin 已完全自主執行物理實驗。
12. 不主張 Robin 已經成為一般科學家替代物。
13. 不主張 multi-agent science 一定優於 human science。
14. 不主張 AI scientist 一定能產生真正新理論。
15. 不主張所有 AI 產生的假說都值得物理驗證。
16. 不主張數位 evaluator 可以取代所有物理實驗。
17. 不主張物理實驗可以被無限加速。
18. 不主張更多 AI 科研必然帶來更多文明淨效益。
19. 不主張更多科技節點必然更好。
20. 不主張 capability graph 有唯一正確全域目標函數。
21. 不主張 AI 有權自行決定文明最終價值。
22. 不主張 optimization performance 等同 political legitimacy。
23. 不主張 AI 參與科技圖編輯等同 AI 主體性。
24. 不主張 AI 主體性是 CGEI 的必要條件。
25. 不主張 CGEI 是 AGI 的充分條件。
26. 不主張 CGEI 是 ASI 的充分條件。
27. 不主張自我延展等同爆炸性增長。
28. 不主張自我延展等同奇點。
29. 不主張奇點已經發生。
30. 不主張局部 AI 自動科研等同文明自我發展。
31. 不主張 AI 能消除能源限制。
32. 不主張 AI 能消除物質限制。
33. 不主張 AI 能消除熱力學限制。
34. 不主張 AI 能消除政治協調。
35. 不主張 AI 能消除法律約束。
36. 不主張 AI 能消除人類偏好差異。
37. 不主張 technology tree 是真實文明的完整模型。
38. 不主張 capability graph 能完整覆蓋所有歷史因果。
39. 不主張制度只是技術。
40. 不主張所有法律都是能力節點。
41. 不主張所有社會關係都能數值化為 graph weight。
42. 不主張 graph editing 必須是可逆的。
43. 不主張不可逆 graph edit 必然不應做。
44. 不主張 rollback 可以處理所有技術風險。
45. 不主張所有新技術都應保留舊技術完整備援。
46. 不主張技術壓縮一定比擴張好。
47. 不主張技術擴張一定比壓縮好。
48. 不主張 AI 會完全接管人類科研角色。
49. 不主張人類未來只能做目標設定。
50. 不主張本文已定義完整 Systemic AI Singularity。
51. 不主張本文已定義後工具文明的完整政治制度。
52. 不主張本文已完成 AI 主權、權利或主體性問題。
53. 不主張文明有單一科技樹終點。
54. 不主張科技發展必然線性。
55. 不主張 AI 一定使科技發展加速。
56. 不主張所有領域都適合 autonomous science。
57. 不主張所有科學問題都有客觀 evaluator。
58. 不主張所有能力改進都能被量化。
59. 不主張第一系列已窮盡人類能力外部化史。
60. 不主張「自我延展文明」已經成為現實完成態。

---

# 86. 結論：科技樹裡第一次出現會改科技樹的人工節點

從 EXS-01 開始，本系列一直在處理一件看似很簡單的事：

> 人類文明究竟靠什麼變強？

答案並不是：

$$
\boxed{
\text{human biological capability alone}.
}
$$

而是：

$$
\boxed{
\text{Human}
+
\text{Tool}
+
\text{Knowledge}
+
\text{Institution}
+
\text{Infrastructure}.
}
$$

人類沒有等眼睛進化得更遠。

我們造望遠鏡。

沒有等大腦能手算超大系統。

我們造超級電腦。

沒有等身體長出翅膀。

我們造飛機。

因此：

$$
\boxed{
\text{Human History}
}
$$

很大一部分可以理解為：

$$
\boxed{
\text{External Capability Construction}.
}
$$

但 AI 帶來的新問題不是：

> 又多了一個外掛。

而是：

$$
\boxed{
\text{the external capability begins to edit external capability}.
}
$$

AlphaEvolve 類系統顯示：

$$
\text{AI}
\rightarrow
\text{algorithm}
\rightarrow
\text{compute}
\rightarrow
\text{AI}.
$$

A-Lab 類系統顯示：

$$
\text{AI}
\rightarrow
\text{experiment}
\rightarrow
\text{physical evidence}
\rightarrow
\text{next experiment}.
$$

更高階 autonomous lab / multi-agent science 開始顯示：

$$
\text{AI}
\rightarrow
\text{research strategy}
\rightarrow
\text{resource allocation}
\rightarrow
\text{knowledge}.
$$

這些都還只是局部碎片。

但它們共同指出同一個結構：

$$
\boxed{
A:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
}
$$

也就是：

$$
\boxed{
\text{Capability-Graph-Editing Intelligence}.
}
$$

所以第一系列最後可以收束為：

$$
\boxed{
\text{External Extension}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{External Cognitive Extension}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{AI-Mediated Extension}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Self-Extending Extension}.
}
$$

用遊戲的話說：

> 前期，玩家自己砍樹。

> 中期，玩家蓋工廠。

> 後期，工廠自動生產。

> 再後期，AI 幫玩家研究科技。

而真正的新時代是：

$$
\boxed{
\text{科技系統開始修改「怎麼研究科技」以及「科技圖本身」。}
}
$$

這就是第一系列真正的終點。

同時也是第二系列真正的起點。

因為當：

$$
\boxed{
\text{Capability Graph}
}
$$

開始能部分自我修改之後，

下一個問題就不再只是：

> AI 會不會自己變聰明？

而是：

> 當 AI、算力、能源、製造、科研、具身與基礎設施彼此形成持續正回饋時，什麼時候才算真正跨入 AI 奇點？

因此第一系列正式交接至：

**Systemic AI Singularity, Reality Bandwidth & Post-Tool Civilization Series**

其第一篇：

**SAS-01｜重新定義 AI 奇點：不是智能爆炸，而是正向再生閉環。**

---

# 參考文獻

[1] Szymanski, N. J. et al. (2023). **An autonomous laboratory for the accelerated synthesis of inorganic materials.** *Nature*, 624, 86–91. A-Lab 整合計算、文獻、機器學習、active learning、XRD 分析與機器人，在 17 天閉環運行中執行 353 次實驗並成功實現 36/57 個目標材料。本文於 2026-08-18 重新核對。

[2] Google DeepMind. (2025). **AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms.** AlphaEvolve 將 LLM 生成與 automated evaluator、evolutionary search 結合，並把所得演算法部署於 Google data center scheduling、hardware design 與 AI training。

[3] Google DeepMind. (2025). **AlphaEvolve: optimizing our computing ecosystem.** 官方報告指出其 Borg scheduling heuristic 平均持續回收約 $0.7\%$ Google 全球計算資源；另有硬體設計被整合進 upcoming TPU，Gemini 核心矩陣運算加速帶來約 $1\%$ training-time reduction。

[4] Google DeepMind. (2026). **AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields.** 2026 年更新指出 AlphaEvolve 的應用已擴展至 genomics、sustainability、physics、electricity grids 與 computing infrastructure 等領域。

[5] Google Cloud. (2026). **AlphaEvolve is available for everyone.** 2026-07-09，AlphaEvolve 在 Google Cloud generally available，工作流程被明確描述為 Define → Measure → Optimize → Apply。

[6] Kusne, A. G. et al. (2026). **Managing autonomous materials labs with multi-agent AI and its implications for the science of science.** *Communications Materials*. 文章討論 single distributed AI、multi-agent AI、research campaign management，以及 digital / physical sandbox 對下一代 autonomous materials lab 的角色。

[7] Ghareeb, A. E. et al. (2026). **A multi-agent system for automating scientific discovery.** *Nature*, 655, 497–505. Robin multi-agent system 將 literature search、hypothesis generation、experimental direction 與 data analysis 整合成半自主生物科研循環；實際濕實驗仍由人類團隊執行並回傳數據。

[8] Boiko, D. A. et al. (2023). **Autonomous chemical research with large language models.** *Nature*. Coscientist 結合 GPT-4、網路／文件搜尋、程式執行與實驗自動化，展示 LLM-driven autonomous chemical research 的早期形式。

[9] Dai, T. et al. (2024). **Autonomous mobile robots for exploratory synthetic chemistry.** *Nature*. 研究展示 mobile robots 操作實驗設備、分析結果並選擇後續動作，將既有實驗室更直接整合進 autonomous laboratory workflow。

[10] Canty, R. B. et al. (2025). **Science acceleration and accessibility with self-driving labs.** *Nature Communications*. 文章回顧 self-driving laboratories 對科學探索速度、成本與可及性的潛力與限制。

[11] Salazar-Villacis, P. et al. (2026). **The ADePT framework for assessing autonomous experimentation.** *Communications Chemistry*. 文章提出 autonomous experimentation 評估架構，顯示 autonomous lab 不應只用「是否自動」二元分類，而需要性能與閉環能力的系統性評估。

[12] Pilon, S. et al. (2026). **A flexible and affordable self-driving laboratory for autonomous chemical experimentation.** *Nature Synthesis*. RoboChem-Flex 展示低成本、模組化 self-driving laboratory 的工程方向。

[13] Vriza, A. et al. (2026). **Operating advanced scientific instruments with AI agents.** *npj Computational Materials*. 多 agent framework 可操作同步輻射 X-ray nanoprobe 與 autonomous robotic station，編排多步實驗、解讀多模態資料並與人類研究者協作。

[14] AlphaTensor Team / Google DeepMind. (2022). **Discovering novel algorithms with AlphaTensor.** DeepMind 以 reinforcement learning 搜尋矩陣乘法演算法，提供 AI 進行演算法發現的較早前例。

[15] Google DeepMind. (2016). **DeepMind AI reduces Google data centre cooling bill by 40%.** 早期案例顯示 AI 已能改善支撐自身與其他數位工作負載的資料中心能源效率；本文將此視為間接能力環境改進的前史，而非完整 recursive self-extension。

---

# 附錄 A｜最小符號表

| 符號 | 意義 |
|---|---|
| $\mathcal G_t$ | 時間 $t$ 的文明能力圖 |
| $V_t$ | 能力節點集合 |
| $E_t$ | 依賴／轉換關係 |
| $W_t$ | 成本、效率、風險等權重 |
| $H$ | 人類能力圖編輯者 |
| $A$ | AI 系統 |
| $CGEI$ | Capability-Graph-Editing Intelligence |
| $IRSE$ | Indirect Recursive Self-Extension |
| $B_D$ | 數位能力生成頻寬 |
| $B_R$ | 現實實現頻寬 |
| $G$ | candidate generation |
| $S$ | candidate selection |
| $V$ | verification |
| $R$ | physical / operational realization |
| $F$ | feedback / reintegration |
| $SEC$ | Self-Extending Civilization |
| $R_{\mathrm{rollback}}$ | 回滾／可逆性能力 |

---

# 附錄 B｜科技樹與能力圖

遊戲式：

$$
\boxed{
T_1
\rightarrow
T_2
\rightarrow
T_3.
}
$$

本文：

$$
\boxed{
\mathcal G_t
=
(
V_t,
E_t,
W_t
).
}
$$

技術進步可以是：

$$
\Delta V>0,
$$

也可以是：

$$
\Delta E\neq0,
$$

或：

$$
\Delta W<0.
$$

因此：

$$
\boxed{
\text{Innovation}
\neq
\text{New Artifact Only}.
}
$$

---

# 附錄 C｜直接與間接遞迴自我延展

直接：

$$
\boxed{
A_t
\rightarrow
A_{t+1}.
}
$$

間接：

$$
\boxed{
A_t
\rightarrow
X_{t+1}
\rightarrow
A_{t+1}.
}
$$

其中：

$$
X
\in
\{
\text{algorithm},
\text{chip},
\text{compute},
\text{energy},
\text{science},
\text{manufacturing}
\}.
$$

本文主張：

$$
\boxed{
\text{Indirect Recursive Self-Extension}
}
$$

可能在現實文明中比純粹「模型自己改模型」更早、更廣泛。

---

# 附錄 D｜自我延展閉環

$$
\boxed{
G
\rightarrow
S
\rightarrow
V
\rightarrow
R
\rightarrow
F
\rightarrow
G'.
}
$$

如果只有：

$$
G
$$

則只是點子生成。

如果有：

$$
G+S+V
$$

是數位搜尋／驗證系統。

如果有：

$$
G+S+V+R
$$

開始進入物理／工程閉環。

如果再有：

$$
F
$$

且下一輪能力確實提高，

才開始構成：

$$
\boxed{
\text{Self-Extending Capability Loop}.
}
$$

---

# 附錄 E｜第一系列總結

## EXS-01

$$
\boxed{
\text{Human civilization externalizes capability}.
}
$$

## EXS-02

$$
\boxed{
\text{external capability creates dependency structures}.
}
$$

## EXS-03

$$
\boxed{
\text{calculation and cognition can be delegated across substrates}.
}
$$

## EXS-04

$$
\boxed{
\text{AI penetration is multi-stage and domain-dependent}.
}
$$

## EXS-05

$$
\boxed{
\text{AI can become architecturally constitutive}.
}
$$

## EXS-06

$$
\boxed{
\text{intelligence is not limited to one machine or one substrate type}.
}
$$

## EXS-07

$$
\boxed{
\text{the capability network begins to acquire artificial nodes that can edit the capability network itself}.
}
$$

因此整個第一系列閉合為：

$$
\boxed{
\text{External Extension}
\rightarrow
\text{Self-Extending Extension}.
}
$$

---

# 附錄 F｜第二系列接口

下一篇：

**SAS-01｜重新定義 AI 奇點：不是智能爆炸，而是正向再生閉環**

將正式把：

$$
\boxed{
A:
\mathcal G_t
\rightarrow
\mathcal G_{t+1}
}
$$

進一步擴張為：

$$
\boxed{
AI
\rightarrow
Compute
\rightarrow
Energy
\rightarrow
Hardware
\rightarrow
Manufacturing
\rightarrow
Embodiment
\rightarrow
AI'.
}
$$

並追問：

> 何時「能力圖局部自我編輯」跨成「整個 AI—物理文明系統具有可持續正向再生能力」？

那才是第二系列真正要重新定義的 AI 奇點。
