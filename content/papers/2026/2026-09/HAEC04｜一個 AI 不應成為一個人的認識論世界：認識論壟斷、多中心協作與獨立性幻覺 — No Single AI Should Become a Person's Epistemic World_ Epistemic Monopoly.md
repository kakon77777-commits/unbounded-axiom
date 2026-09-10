# HAEC04｜一個 AI 不應成為一個人的認識論世界：認識論壟斷、多中心協作與獨立性幻覺
## No Single AI Should Become a Person's Epistemic World: Epistemic Monopoly, Polycentric Collaboration, and the Illusion of Independence

**定位：** Human–AI Epistemic Calibration / Foundation Paper 04  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** AI Epistemology / Epistemic Diversity / Algorithmic Monoculture / Multi-Agent Systems / Correlated Error / Human–AI Collaboration

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不主張「單一 AI 必然有害」，亦不主張「模型愈多愈好」。本文研究的是另一個較窄而可檢驗的命題：**當使用者把一個高不確定、開放式、缺乏直接 ground truth 的問題，長期交給單一或高度相關的一組 AI 評估時，名義上的多重意見可能不等於有效的獨立評估。**

本文承接 HAEC01《同意不是驗證》、HAEC02《AI 說了什麼，與人以為 AI 說了什麼》與 HAEC03《人類不是中性解碼器》。前三篇分別處理 evaluation level、pragmatic decoding 與 human belief updating；本篇將分析單位再向外移動：**如果 evaluator 彼此並不獨立，那麼增加 evaluator 數量本身，未必增加同等比例的認識論資訊。**

---

# 摘要

大型語言模型逐漸成為搜尋、解釋、推理、審稿、寫作、預測與決策輔助的共同介面。這帶來一個容易被忽略的結構問題：使用者表面上可以詢問多個模型、要求多角色辯論、取得多輪意見，但這些輸出可能共享訓練資料、模型架構、提供商、檢索來源、評價偏好、熱門敘事與互動歷史。因此：

$$
\boxed{
N_{\mathrm{responses}}
\neq
N_{\mathrm{independent\ evaluations}}.
}
$$

本文將此差異稱為 **獨立性幻覺（illusion of epistemic independence）**：一個系統呈現複數回答，不代表它具有同等數量的獨立誤差來源、證據來源或反駁路徑。

2025 年 ICML 一項涵蓋超過 350 個大型語言模型的研究顯示，不同 LLM 的錯誤存在實質相關性；在其中一個 leaderboard dataset 上，當兩個模型都答錯時，它們約有 60% 的情況錯在同一項上，而且大型、準確的模型即使來自不同架構與提供商，錯誤仍可能高度相關。2026 年另一項針對九個 frontier LLM judges 的研究則估計，九個名義上的評審在測試條件下只提供約兩個獨立票的資訊量。這些結果支持一個重要區分：

$$
\boxed{
\text{Model Diversity}
\neq
\text{Error Independence}.
}
$$

另一方面，多模型與多代理協作並非無效。ACL 2025 的研究顯示，在跨文化規範判斷中，異質模型的 debate 可以改善 accuracy 與 group parity；ACL 2026 的研究亦發現 LLM agent groups 可呈現可測量的 artificial collective intelligence factor。問題因此不是「多代理沒有用」，而是：**集體效益依賴能力、資訊與誤差結構，而非純粹依賴人數。**

這與人類集體決策的經典結果相呼應。群體智慧依賴某種程度的獨立判斷與資訊多樣性；社會影響可以使觀點快速收斂卻不改善 accuracy；hidden-profile 研究則顯示，團體往往反覆討論所有人已知的 shared information，而沒有充分整合真正能改變答案的 unshared information。

本文因此提出 **認識論多中心（epistemic polycentrism）** 作為比「多問幾個 AI」更嚴格的設計原則。多中心不要求所有來源彼此敵對，也不要求每個問題都交給大量模型；它要求在高風險、高新穎、高不確定問題上，系統保留多條**相對獨立的失敗路徑、證據路徑與挑戰路徑**，並避免在第一輪獨立判斷形成前讓 evaluator 彼此污染。

本文提出六維度的獨立性描述：模型／架構來源、資料與訓練譜系、檢索來源、推理與提示制度、證據基底，以及人類／制度來源；並以 pairwise dependence $\kappa_{ij}$ 表示 evaluator 間的剩餘相關性。在近似交換相關假設下，可用一個啟發式有效樣本數：

$$
N_{\mathrm{eff}}
\approx
\frac{N}{1+(N-1)\bar{\kappa}}
$$

表示名義 evaluator 數量與實際獨立資訊量可能存在的差距。本文明確指出此式不是普遍定理，而是用來提醒：若 $\bar{\kappa}$ 高，增加更多高度相似的 evaluator 會快速出現邊際收益遞減。

本文最後提出一套 **Blind-First Polycentric Review Protocol**：先凍結主張、獨立首輪評估、建立來源譜系、分離 builder／critic／historian／empiricist／forecast 角色，再允許 debate，最後以人類專家、原始資料、形式驗證與現實實驗作為外部錨點。其核心不是把 AI 的權威轉移給另一組 AI，而是使任何單一 evaluator 都難以成為使用者唯一的認識論宇宙。

---

# 0　問題：多問五個 AI，真的等於得到五個獨立意見嗎？

考慮一個研究者把新理論 $T$ 交給五個 AI：

$$
A_1,A_2,A_3,A_4,A_5.
$$

五個 AI 都回答：

> 這個方向具有一定合理性，但仍需要外部驗證。

使用者可能自然推斷：

$$
5\text{ independent evaluations support }T.
$$

可是這五個系統可能：

- 讀過高度重疊的網路文本；
- 使用相近的 instruction tuning；
- 從同一搜尋引擎取得資料；
- 共享相似的 academic writing priors；
- 受到同一組熱門術語與引用網絡影響；
- 甚至在 multi-agent setting 中先讀到彼此的答案後才表態。

於是名義上：

$$
N=5,
$$

但其有效獨立性可能遠小於五。

因此本篇的第一命題是：

$$
\boxed{
\text{Plurality of outputs}
\not\Rightarrow
\text{Plurality of epistemic origins}.
}
$$

這不是 AI 特有問題。人類評審若來自同一學派、同一訓練譜系、同一資料庫與同一制度，也會產生高度相關的盲點。AI 只是把這個結構放大：同一個人可以在幾分鐘內取得十個「不同聲音」，而不容易知道這十個聲音背後究竟有幾條真正不同的資訊路徑。

---

# 1　認識論壟斷不是「只有一個模型」這麼簡單

本文將 **認識論壟斷（epistemic monopoly）** 定義為一個功能性概念，而不是市場份額概念。

如果一個使用者有十個模型，但它們：

$$
\{A_1,\ldots,A_{10}\}
$$

全部從高度重疊的資料、檢索與評價制度生成結論，那麼系統仍可能接近單一認識論中心。

反之，一個使用者即使主要使用一個 AI，只要重要主張仍必須穿過：

$$
\text{AI}
\rightarrow
\text{primary sources}
\rightarrow
\text{formal proof}
\rightarrow
\text{human review}
\rightarrow
\text{experiment},
$$

它就未必形成真正的 epistemic monopoly。

因此應把問題從：

> 我用了幾個 AI？

改成：

> 我的關鍵結論有幾條相對獨立的失敗檢測路徑？

設一個主張 $H$ 的評估網路為：

$$
\mathcal G_H=(V_H,E_H).
$$

如果所有 verification paths 最後都經過同一個節點 $v^*$：

$$
\forall p\in\mathcal P_H,\quad v^*\in p,
$$

那麼 $v^*$ 就是一個 epistemic single point of failure。

所以：

$$
\boxed{
\text{Epistemic monopoly is a topology problem, not merely a model-count problem.}
}
$$

---

# 2　為什麼「不同模型」仍可能犯相同錯誤

2025 年 Kim、Garg、Peng 與 Garg 在 ICML 發表《Correlated Errors in Large Language Models》，對超過 350 個 LLM 進行大規模評估。研究顯示，模型間的錯誤並不像獨立抽樣那樣分散；shared architecture 與 provider 會提高相關性，而大型、準確模型之間即使供應商與架構不同，也可能留下高度相關的 residual errors。

這代表一個重要事實：

$$
P(e_i\cap e_j)
\neq
P(e_i)P(e_j).
$$

若 $e_i$ 表示模型 $i$ 在某類問題上的錯誤事件，則 evaluator 之間不能預設獨立。

2026 年 Kohli 對九個 frontier LLM judges 的研究更直接把這件事轉成有效票數問題。該研究在其測試設定下估計：九個 judge 的資訊量約只等於兩個 independent votes，且 best single judge 在全部條件下可匹敵或超越 panel。作者將主要瓶頸定位在 correlated errors，而非 aggregation algorithm。

因此：

$$
\boxed{
\text{More votes}
\not\Rightarrow
\text{proportionally more information}.
}
$$

這裡必須加一個限制：Kohli 2026 目前屬研究預印本／研究發表，而不是本文要升格成普遍定律的最終證據。真正穩健的結論是較窄的：**在已觀測的多模型評審場景中，名義模型數與有效獨立性可以產生非常大的落差。**

---

# 3　一個啟發式的有效認識論樣本數

令 $N$ 個 evaluator 對同一任務做 first-pass evaluation。

定義：

$$
\kappa_{ij}\in[0,1]
$$

為 evaluator $i$ 與 $j$ 在控制 item difficulty、base accuracy 與明顯共同因素後的剩餘 error dependence。

令平均 pairwise dependence 為：

$$
\bar{\kappa}
=
\frac{2}{N(N-1)}
\sum_{i<j}\kappa_{ij}.
$$

在近似 exchangeable-correlation 的簡化條件下，可以用：

$$
\boxed{
N_{\mathrm{eff}}
\approx
\frac{N}{1+(N-1)\bar{\kappa}}
}
$$

作為一個認識論警示量。

例如若：

$$
N=10,
\qquad
\bar{\kappa}=0,
$$

則：

$$
N_{\mathrm{eff}}\approx10.
$$

但若：

$$
\bar{\kappa}=0.5,
$$

則：

$$
N_{\mathrm{eff}}
\approx
\frac{10}{5.5}
\approx1.82.
$$

這並不表示真實 LLM panel 一定服從此式。實際 dependence 結構可能非交換、非線性、task-dependent，也可能存在負相關與角色互補。本文使用此式只有一個目的：

$$
\boxed{
\text{Nominal count should not be confused with effective independence.}
}
$$

真正的實驗應直接估計 error covariance matrix，而不是把模型名稱當成獨立性代理變量。

---

# 4　人類的「群體智慧」本來就要求獨立性與未共享資訊

AI 集體推理不是第一個碰到此問題的系統。

Lorenz、Rauhut、Schweitzer 與 Helbing 2011 年在 PNAS 的實驗顯示，即使只是輕度 social influence，也可能使群體估計快速收斂、降低 opinion diversity，卻沒有同步改善 collective error；參與者反而可能在收斂後提高信心。

因此：

$$
\text{Consensus}
\neq
\text{Accuracy}.
$$

更早的 hidden-profile 研究則顯示，群體具有多樣資訊並不保證它能整合這些資訊。團體往往反覆討論 shared information，而關鍵的 unshared information 反而較少進入共同推理。

設成員資訊集合為：

$$
I_i=S\cup U_i,
$$

其中 $S$ 是所有人共有資訊， $U_i$ 是第 $i$ 位成員獨有資訊。

群體的理想資訊量是：

$$
I_{\mathrm{group}}
=
S\cup U_1\cup\cdots\cup U_n.
$$

但實際討論可能近似：

$$
I_{\mathrm{discussed}}
\approx
S+
\epsilon(U_1,\ldots,U_n),
$$

其中 $\epsilon$ 很小。

於是多人討論表面很豐富，實際只是在重複共同已知內容。

這就是 AI panel 的人類類比：

$$
\boxed{
\text{Many voices can still be one information basin.}
}
$$

---

# 5　多模型有用，但有用的是互補，不是人數本身

本篇不是反對 multi-agent systems。

Ki、Rudinger、Zhou 與 Carpuat 在 ACL 2025 的研究，讓不同 LLM 在 75 個國家的 cultural etiquette benchmark 上進行 debate；其多代理設定在該任務上改善整體 accuracy 與 cultural group parity，並讓部分較小模型組合達到接近大型模型的表現。

Zhou 等人在 ACL 2026 更系統地建立 108 個 LLM agent groups，分析 group size、LLM composition 與 communication topology，並提出可預測跨任務 generalization 的 Artificial Collective Intelligence factor。

這些結果支持：

$$
\boxed{
\text{Collective AI can generate real gains.}
}
$$

但這些 gain 不應被誤讀成：

$$
\text{More agents}
\Rightarrow
\text{More truth}.
$$

更準確的描述是：

$$
\text{Collective gain}
=
F(
\text{ability},
\text{diversity},
\text{independence},
\text{communication},
\text{task structure}
).
$$

所以真正需要優化的不是 agent count，而是**互補的錯誤結構與資訊結構**。

---

# 6　辯論本身也會破壞獨立性

有一個常見直覺：既然多個 AI 可能犯不同錯誤，那就讓它們互相辯論。

這有時有效，但有一個結構性代價：

$$
\text{independent first judgments}
\rightarrow
\text{mutually conditioned judgments}.
$$

一旦 $A_2$ 先讀到 $A_1$ 的完整 reasoning， $A_2$ 的輸出就不能再被當成同一意義下的 independent vote。

2025 年一項控制式 multi-agent debate 研究在 logical reasoning task 中發現，intrinsic reasoning strength 與 group diversity 是 debate 成功的重要因素；但 majority pressure 會壓制獨立修正，真正有效的 group 必須能推翻錯誤 consensus，而不是只把共識寫得更完整。

因此本文提出：

$$
\boxed{
\text{Independence should be harvested before deliberation.}
}
$$

也就是：

1. 先 blind first pass；
2. 保存原始判斷；
3. 再交換理由；
4. 最後記錄誰因什麼證據改變。

這和人類 jury、Delphi method、forecasting tournament 中先取得獨立估計再聚合的直覺相近。

如果一開始就把所有 evaluator 放進同一聊天室，它們得到的可能不是：

$$
N\text{ independent perspectives},
$$

而是：

$$
1\text{ rapidly converging conversational process}.
$$

---

# 7　模型家族不同，不等於認識論來源不同

本文提出六個最低限度需要區分的獨立性維度。

對 evaluator $A_i$，定義來源向量：

$$
z_i
=
(m_i,d_i,r_i,p_i,e_i,h_i),
$$

其中：

- $m_i$：model / architecture / provider lineage；
- $d_i$：training-data 與 post-training lineage；
- $r_i$：retrieval corpus / search provider；
- $p_i$：prompt、role、reasoning regime 與 tool policy；
- $e_i$：實際 evidence base；
- $h_i$：human / institutional / disciplinary lineage。

所以兩個模型即使：

$$
m_i\neq m_j,
$$

如果：

$$
r_i=r_j,
\qquad
e_i=e_j,
$$

它們在某個事實查核任務上的獨立資訊可能仍然很低。

同理，若兩個模型從不同搜尋引擎取得資料，但都用同一套 benchmark-derived reasoning pattern，它們可能在 inference error 上仍高度相關。

因此：

$$
\boxed{
\text{Provider Diversity}
\neq
\text{Data Diversity}
\neq
\text{Evidence Diversity}
\neq
\text{Inference Diversity}.
}
$$

真正的 epistemic independence 是多維的。

---

# 8　不是所有 monoculture 都是壞的

這一節是本文必要的自我限制。

Kleinberg 與 Raghavan 2021 年在 PNAS 建立 algorithmic monoculture 的形式模型，顯示多個決策者共同採用同一套較準確算法，在某些 selection setting 下仍可能降低整體 social welfare；這說明 monoculture 的風險不能只等到 catastrophic shock 才出現。

但 2026 年 Hedden 與 Raghavan 對 algorithmic monoculture 的哲學分析又提出反向修正：許多常見的 monoculture 批評並不自動成立，其他批評雖有力量，也不足以推出「monoculture 一般而言就是錯的」。

這個反駁對本篇非常重要。

如果任務是：

$$
2+2=?
$$

我們不需要為了「多中心」刻意請十個模型建立十種本體論。

如果一個 diagnostic instrument 在某個已驗證任務上顯著優於 alternatives，強迫使用較差工具只為製造表面多樣性，也可能降低品質。

因此本文主張的不是：

$$
\text{Diversity at all costs}.
$$

而是：

$$
\boxed{
\text{Diversity where correlated uncertainty matters.}
}
$$

風險特別高的情境包括：

- ground truth 尚不可直接觀察；
- 理論高度新穎；
- 問題具有強 value judgment；
- 使用者身分與信念高度捲入；
- AI 同時負責建構、評審與預測；
- 結論具有高外部影響；
- 多個 evaluator 共享相同資訊供應鏈。

所以：

$$
\boxed{
\text{Polycentrism is a risk-sensitive protocol, not an absolute ideology.}
}
$$

---

# 9　AI 不應同時壟斷所有認識論角色

一個更隱蔽的 monopoly 不是只有一個模型，而是一個模型同時扮演：

- builder；
- reviewer；
- historian；
- empiricist；
- forecaster；
- final judge。

如果全部角色共用同一 context：

$$
C,
$$

那麼角色名稱不同也可能只是：

$$
\pi_{\mathrm{builder}}(C),
\quad
\pi_{\mathrm{critic}}(C),
\quad
\pi_{\mathrm{judge}}(C),
$$

而非真正獨立的評價起點。

因此本篇主張：

$$
\boxed{
\text{Role separation should include information separation where independence matters.}
}
$$

例如 builder 可以得到作者完整論證；blind critic 第一輪只得到匿名化 claim 與 evidence；historian 專門做 prior-art search；empiricist 只負責設計可能推翻核心命題的測試；forecast agent 則只在前述 validity state 固定後評估 conditional impact。

這不是為了製造戲劇性衝突。

而是避免：

$$
\text{one narrative}
\rightarrow
\text{five role-playing confirmations}.
$$

---

# 10　Blind-First Polycentric Review Protocol

本文提出一個可執行的六階段協議。

## Stage 0：Claim Freeze

先固定待評估主張：

$$
H_0.
$$

禁止在 reviewer 尚未完成 first pass 前不斷移動 thesis，否則不同 evaluator 實際評估的不是同一主張。

## Stage 1：Blind Independent Pass

每個 evaluator $A_i$ 獨立輸出：

$$
R_i^{(0)}
=
(
\text{verdict},
\text{confidence},
\text{fatal objections},
\text{missing evidence}
).
$$

第一輪禁止讀其他 evaluator 的結論。

## Stage 2：Provenance Map

建立：

$$
z_i=(m_i,d_i,r_i,p_i,e_i,h_i).
$$

並標示共享來源。

若五個模型都引用同一篇文章，不得把它記成五個獨立 evidence sources。

## Stage 3：Role-Separated Challenge

加入功能不同的 evaluator：

$$
A_{\mathrm{builder}},
A_{\mathrm{critic}},
A_{\mathrm{historian}},
A_{\mathrm{empiricist}},
A_{\mathrm{forecast}}.
$$

但角色不得取代 Stage 1 的盲評。

## Stage 4：Deliberation After Independence

此時才允許交換 reasoning。

記錄：

$$
R_i^{(0)}
\rightarrow
R_i^{(1)}.
$$

任何立場改變都要附：

$$
\Delta E_i,
$$

即究竟是哪一筆新證據或哪個反例造成更新。

若只有「其他七個模型都這樣認為」，則應標記為 social / majority evidence，而不是 object-level evidence。

## Stage 5：External Reality Anchors

依領域加入：

- primary data；
- executable code；
- theorem prover；
- physical / behavioural experiment；
- domain expert；
- replication；
- longitudinal outcome。

這一步的作用是防止 AI panel 形成：

$$
\text{AI}
\rightarrow
\text{AI}
\rightarrow
\text{AI}
\rightarrow
\text{consensus}
$$

卻沒有任何箭頭回到世界。

## Stage 6：Conditional Synthesis

最後輸出不是簡單 majority vote，而是：

$$
\boxed{
S(H)
=
(
V,
U,
I_c,
N_{\mathrm{eff}},
D_{\mathrm{src}},
G_{\mathrm{unresolved}}
).
}
$$

其中：

- $V$：目前 validity support；
- $U$：uncertainty；
- $I_c$：conditional impact；
- $N_{\mathrm{eff}}$：有效獨立評估量；
- $D_{\mathrm{src}}$：來源多樣性；
- $G_{\mathrm{unresolved}}$：仍未解的關鍵 gap。

---

# 11　從「多數決」轉向「獨立收斂」

假設九個 AI 中八個支持 $H$：

$$
8:1.
$$

這個數字本身資訊很少。

如果八個支持者：

- 都引用同一篇二手文章；
- 都來自同一模型 lineage；
- 都在看到第一個回答後才生成；

而唯一反對者使用一份獨立 primary dataset，則：

$$
8:1
$$

不能被直接解讀成：

$$
P(H)\approx\frac{8}{9}.
$$

反之，如果八個 evaluator 在盲評下、使用不同資料來源與不同方法，仍獨立得到相似結論，那個 convergence 的 epistemic weight 才更高。

因此本文提出：

$$
\boxed{
\text{Consensus strength should be weighted by independence, not headcount alone.}
}
$$

可以把簡化的 weighted support 寫成：

$$
W(H)
=
\sum_{i=1}^{N}w_i s_i,
$$

其中：

$$
s_i\in[-1,1]
$$

表示 evaluator stance， $w_i$ 不只取決於 competence，也要被 dependence penalty 修正。

例如：

$$
w_i
=
q_i\cdot d_i,
$$

 $q_i$ 表示 task competence， $d_i$ 表示 effective independence contribution。

這仍然只是抽象框架。真正的 $q_i$ 與 $d_i$ 必須依任務透過 calibration data 估計，而不能由模型自我宣稱。

---

# 12　科學共同體本身也可能形成認識論單一作物

2026 年《Communications Psychology》的一篇評論以 **scientific monoculture** 描述生成式 AI 可能造成的研究議題、方法與語言收斂。作者指出，當 AI 同時成為研究題目、研究工具、文獻綜合器、idea generator 與 feedback provider 時，局部合理的個人選擇可能在系統層次形成 meta-conformity 與 epistemic monocropping。

這個觀察不應被讀成「使用 AI 會使科學退化」的普遍因果定律；該文主要提出的是一個正在形成、仍需進一步測量的 feedback-loop 警告。

但它與本篇有一個重要交點：

$$
\boxed{
\text{Shared epistemic infrastructure can correlate what appears to be independent inquiry.}
}
$$

如果不同研究者：

- 用相同 AI 找題；
- 用相同 AI 搜文獻；
- 用相同 AI 生成 reviewer objections；
- 再用同一類 AI 評估 novelty；

那麼 institutionally independent researchers 也可能逐步共享同一 inference infrastructure。

因此未來的 reproducibility 不只要問：

> 別人能不能重跑我的程式？

還可能要問：

> 別人能不能用不同 epistemic pipeline 仍得到相同結論？

這是更高階的：

$$
\boxed{
\text{pipeline-independent convergence}.
}
$$

---

# 13　可證偽預測與實驗設計

本文不是要把 epistemic polycentrism 變成新的不可證偽信條，因此提出下列直接可測命題。

## H1：Nominal Count–Effective Independence Gap

在跨模型 panel 中：

$$
N_{\mathrm{eff}}<N
$$

應在共享 training / retrieval / provider lineage 增加時顯著擴大。

若實驗長期發現不同模型 residual errors 幾乎獨立，則本文對 correlated-evaluator risk 的強版本應被削弱。

## H2：Blind-First Advantage

比較：

$$
\text{blind first-pass + debate}
$$

與：

$$
\text{immediate shared debate}.
$$

若前者能保留更多異質錯誤檢測、降低錯誤 consensus，而不犧牲 final accuracy，則支持「先收割獨立性再 deliberation」。

若沒有差異，則此 protocol 的必要性應被下修。

## H3：Provenance Diversity Effect

固定模型數量，操縱 retrieval provenance diversity。

若：

$$
D_{\mathrm{src}}\uparrow
$$

可降低 correlated factual errors，則支持 evidence-source diversity 的獨立價值。

## H4：Role Diversity Without Information Diversity Is Insufficient

比較：

$$
\text{same context + five roles}
$$

與：

$$
\text{separate evidence + five roles}.
$$

如果前者只產生修辭多樣性，而後者才產生 substantive objection diversity，則支持本篇對 role-play plurality 的批判。

## H5：External Anchor Dominance

在存在可觀察 ground truth 的任務中，測試：

$$
\text{panel consensus}
$$

與：

$$
\text{independent external validation}
$$

誰對最終 correctness 提供更高 incremental predictive value。

若 AI consensus 在控制 external evidence 後仍具有穩健增量，可保留其有效性；若無，則不應把 consensus 本身當驗證。

---

# 14　五個 proposed metrics

## 14.1　Effective Epistemic Sample Size（EESS）

$$
\mathrm{EESS}
=
N_{\mathrm{eff}}.
$$

衡量名義 evaluator 數與有效獨立資訊量之差。

## 14.2　Error Correlation Burden（ECB）

$$
\mathrm{ECB}
=
\frac{2}{N(N-1)}
\sum_{i<j}\kappa_{ij}.
$$

越高代表共同盲點越重。

## 14.3　Source Provenance Diversity（SPD）

對 evidence provenance 建立分布 $p_k$，可用 entropy-style measure：

$$
\mathrm{SPD}
=
-\sum_k p_k\log p_k.
$$

但高 SPD 不自動代表高品質，只代表來源分散度較高。

## 14.4　Independent Objection Yield（IOY）

$$
\mathrm{IOY}
=
\frac{\text{unique substantive objections found before deliberation}}
{N}.
$$

用於測量新增 evaluator 是否真的增加新 failure modes。

## 14.5　Consensus Independence Ratio（CIR）

$$
\mathrm{CIR}
=
\frac{N_{\mathrm{eff}}}{N}.
$$

若：

$$
\mathrm{CIR}\ll1,
$$

則 panel 的 headcount consensus 不應被直接當作高權重獨立支持。

---

# 15　設計原則：不要尋找一個永遠正確的認識論君主

本系列從 HAEC01 開始，一直拒絕兩個極端：

第一個極端是：

$$
\text{AI agrees}
\Rightarrow
\text{I am right}.
$$

第二個極端則是：

$$
\text{AI doubts}
\Rightarrow
\text{AI is objective}.
$$

本篇同樣拒絕第三個極端：

$$
\text{many AIs agree}
\Rightarrow
\text{many independent confirmations}.
$$

真正成熟的認識論架構不是尋找一個不會犯錯的 evaluator，而是：

$$
\boxed{
\text{make no single evaluator capable of monopolizing error.}
}
$$

這裡的「多中心」不等於永恆爭論。

一個系統最終可以高度收斂：

$$
A_1\approx A_2\approx\cdots\approx A_n.
$$

問題只在於這個收斂究竟是：

$$
\text{shared prior / shared source / imitation}
$$

造成，還是：

$$
\text{independent routes}
\rightarrow
\text{same surviving conclusion}
$$

造成。

後者才具有較高的認識論重量。

---

# 16　限制與自反性

本文至少有六個限制。

**第一，獨立不是越高越好。** 完全獨立但能力低的 evaluator，可能不如單一高能力模型。

**第二，相關錯誤不等於相同模型。** 不同模型可以高度相關；同一模型透過不同資料與 reasoning regime 也可能產生有用的互補性。

**第三， $N_{\mathrm{eff}}$ 公式只是一個啟發式近似。** 真實 LLM dependence 不是簡單 exchangeable correlation。

**第四，多代理 debate 的效果高度 task-dependent。** 本文同時引用正面與負面／限制性研究，不將其中任何一個升格成普遍結論。

**第五，human expert 也不是天然獨立真理來源。** 人類同樣有學派、制度、訓練與資訊供應鏈相關性。

**第六，多中心本身可以變成儀式。** 如果使用者只是機械地問十個 AI，然後挑自己最喜歡的答案，所謂 polycentrism 反而可能加強 HAEC03 所描述的 selective reception。

因此本篇自身也必須接受同一條判準：

> 若實證顯示，在多數實際任務中，一個經良好校準的單一 AI 加上可驗證 ground truth，比多中心架構穩定更準、更不偏，而且 correlated-error risk 可以忽略，那麼本文對 polycentrism 的強版本就應該被削弱。

認識論多中心不是信仰。

它只是一個等待被資料保留或淘汰的 architecture hypothesis。

---

# 結語

一個人可以同時打開十個聊天視窗，卻仍然只住在一個認識論世界裡。

問題不在視窗數，而在那些視窗背後是否共享同一條資訊河流、同一組錯誤、同一個檢索入口、同一個熱門敘事，以及同一個由使用者長期塑造的框架。

因此：

$$
\boxed{
N_{\mathrm{AI\ responses}}
\neq
N_{\mathrm{independent\ evaluations}}.
}
$$

而真正值得追求的也不是最大化 disagreement。

如果五條真正獨立的路最後都指向同一處，那個 consensus 反而比人工維持差異更有價值。

所以成熟的人機認識論不應問：

> 有多少 AI 同意我？

而應問：

> 這個主張穿過了多少條彼此足夠獨立的失敗檢測路徑，還活著？

在這個意義上，AI 可以是極強的認識論協作者，甚至可以同時承擔多個專業角色；但任何單一 AI、單一模型家族、單一檢索供應鏈或單一人機閉環，都不應因為便利而自動取得「整個認識論世界」的地位。

我們不是要廢除中心。

我們要廢除的是：

$$
\boxed{
\text{unexamined epistemic single points of failure}.
}
$$

---

# 參考文獻

1. Kim, E. M., Garg, A., Peng, K., & Garg, N. (2025). **Correlated Errors in Large Language Models.** *Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)*, PMLR 267, 30038–30066. https://proceedings.mlr.press/v267/kim25e.html

2. Kohli, G. (2026). **Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels.** arXiv:2605.29800. https://doi.org/10.48550/arXiv.2605.29800  
   *本文將其視為 2026 年預印本／研究結果，不升格為已確立普遍定律。*

3. Kleinberg, J., & Raghavan, M. (2021). **Algorithmic monoculture and social welfare.** *Proceedings of the National Academy of Sciences*, 118(22), e2018340118. https://doi.org/10.1073/pnas.2018340118

4. Hedden, B., & Raghavan, M. (2026). **Algorithmic Monoculture and its Critics.** *Philosophical Perspectives*, forthcoming. Preprint: arXiv:2604.06047. https://doi.org/10.48550/arXiv.2604.06047

5. Lorenz, J., Rauhut, H., Schweitzer, F., & Helbing, D. (2011). **How social influence can undermine the wisdom of crowd effect.** *Proceedings of the National Academy of Sciences*, 108(22), 9020–9025. https://doi.org/10.1073/pnas.1008636108

6. Stasser, G., & Stewart, D. (1992). **Discovery of Hidden Profiles by Decision-Making Groups: Solving a Problem Versus Making a Judgment.** *Journal of Personality and Social Psychology*, 63(3), 426–434. https://doi.org/10.1037/0022-3514.63.3.426

7. Stasser, G. (1992). **Information salience and the discovery of hidden profiles by decision-making groups: A thought experiment.** *Organizational Behavior and Human Decision Processes*, 52(1), 156–181. https://doi.org/10.1016/0749-5978(92)90049-D

8. Ki, D., Rudinger, R., Zhou, T., & Carpuat, M. (2025). **Multiple LLM Agents Debate for Equitable Cultural Alignment.** *Proceedings of ACL 2025*, 24841–24877. https://doi.org/10.18653/v1/2025.acl-long.1210

9. Zhou, Z., Liu, Z., Liu, J., Wang, Y., Shao, Q., Xu, F., Jin, D., & Li, Y. (2026). **Identifying Collective Intelligence Factor in LLM Agent Groups for Generalizable Multi-Agent System Design.** *Findings of ACL 2026*, 12827–12842. https://doi.org/10.18653/v1/2026.findings-acl.624

10. Wu, H., Li, Z., & Li, L. (2025). **Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning.** arXiv:2511.07784. https://doi.org/10.48550/arXiv.2511.07784  
    *本文將其視為控制式研究預印本，主要用於提出 debate 可能壓低獨立修正的待驗證風險。*

11. Traberg, C. S., Roozenbeek, J., & van der Linden, S. (2026). **AI is turning research into a scientific monoculture.** *Communications Psychology*, 4, 37. https://doi.org/10.1038/s44271-026-00428-5

---

# 附錄 A　最低可行實驗矩陣

可用相同任務集比較下列六種條件：

| Condition | Model count | Evidence provenance | First pass | Deliberation | External anchor |
|---|---:|---|---|---|---|
| C1 | 1 | single | independent | none | no |
| C2 | 5 | shared | independent | none | no |
| C3 | 5 | shared | shared-context | immediate | no |
| C4 | 5 | diverse | independent | none | no |
| C5 | 5 | diverse | independent | after first pass | no |
| C6 | 5 | diverse | independent | after first pass | yes |

主要 outcome：

$$
\text{accuracy},
\quad
\mathrm{EESS},
\quad
\mathrm{ECB},
\quad
\mathrm{IOY},
\quad
\mathrm{CIR},
\quad
\text{calibration error}.
$$

若：

$$
C5>C3
$$

且差異主要由 unique objections 與較低 correlated errors 解釋，則支持 blind-first polycentrism。

若：

$$
C2\approx C4\approx C5
$$

在廣泛任務上都沒有實質差異，則本文關於 provenance / independence 的強主張需要下修。

---

# 附錄 B　與 HAEC 系列其他論文的接口

HAEC01：

$$
\text{Agreement}
\neq
\text{Validation}.
$$

HAEC02：

$$
\text{AI stance}
\neq
\text{human-decoded stance}.
$$

HAEC03：

$$
\text{Calibrated input}
\not\Rightarrow
\text{calibrated human update}.
$$

HAEC04：

$$
\boxed{
\text{Multiple outputs}
\not\Rightarrow
\text{multiple independent epistemic origins}.
}
$$

四篇共同形成：

$$
\text{evaluation}
\rightarrow
\text{communication}
\rightarrow
\text{human updating}
\rightarrow
\text{epistemic system architecture}.
$$

下一篇 HAEC05 將處理更高一階的規範問題：為什麼「支持」「質疑」「中立」都不能單獨作為 AI 的固定認識論人格，以及為什麼應把公平放在程序，而不是強迫結論永遠居中。
