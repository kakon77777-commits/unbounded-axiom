---
title: "跨世界符號橋的多層架構：AI-native、形式驗證、專家理解與人類可讀層"
english_title: "A Multi-Layer Architecture for Cross-World Symbolic Bridges: AI-Native, Formal Verification, Expert, and Human-Readable Layers"
author: "Neo.K（許筌崴）"
institution: "EveMissLab（一言諾科技有限公司）"
series: "異質智慧動態協議生成系列"
paper_no: "06"
version: "v0.1"
date: "2026-08-14"
status: "正式研究草稿"
canonical_source_encoding: "UTF-8"
---

# 跨世界符號橋的多層架構：AI-native、形式驗證、專家理解與人類可讀層

**A Multi-Layer Architecture for Cross-World Symbolic Bridges: AI-Native, Formal Verification, Expert, and Human-Readable Layers**

作者：Neo.K（許筌崴）  
機構：EveMissLab（一言諾科技有限公司）  
系列：異質智慧動態協議生成系列，第 6 篇  
版本：v0.1  
日期：2026 年 8 月 14 日

---

## 摘要

若未來人工智慧在數學、程式設計、物理學與科學發現中逐步形成高度壓縮、機器原生、甚至人類無法直接閱讀的工作表示，一個極端答案是：人類只保留意圖與最終接受／拒絕權，中間推理、形式化與操作世界全部交給 AI 黑箱。本文主張這不是唯一可能的架構，也不是一個理想的預設。

本文不要求 AI-native 表示退化成人類自然語言，而提出四層跨世界符號橋：

$$
\boxed{
L_A
\leftrightarrow
L_F
\leftrightarrow
L_E
\leftrightarrow
L_H
}
$$

其中：

- $L_A$：AI-native / machine-operational layer；
- $L_F$：formal / verifiable shared layer；
- $L_E$：expert-facing semantic layer；
- $L_H$：general human-readable layer。

此架構的核心不是「每層翻譯成相同內容」，而是每一層有不同責任： $L_A$ 優先效率與可執行； $L_F$ 優先可驗證規格、證書與語義約束； $L_E$ 優先專家能重建理論結構、假設、證據與失敗條件； $L_H$ 優先讓非專家理解目的、風險、不確定性與可採取行動。各層之間使用任務充分語義同態，而非完整同構。

本文進一步提出雙平面架構：

$$
\boxed{
\text{Execution Plane}
\quad\parallel\quad
\text{Audit / Understanding Plane}
}
$$

Execution Plane 允許 AI 在 $L_A$ 中運行，經工具與 runtime 造成真實狀態轉移；Audit Plane 則要求每個重要操作能產生可追蹤 artifact、formal obligation、certificate、counterexample 或 provenance，沿 $L_F\to L_E\to L_H$ 被驗證與解釋。因此：

$$
\boxed{
\text{Human-readable explanation}
\neq
\text{source of correctness}.
}
$$

正確性應盡量由 $L_F$ 的 machine-checkable certificate、formal verification、test witness 或可重現計算支撐； $L_E,L_H$ 則負責理解、審查與決策。

本文與 CompCert 的語義保持式多中介語言、Proof-Carrying Code 的「程式＋可驗證安全證明」、autoformalization 的自然語言—形式語言橋、以及 2025 年「intermediate language challenge」存在直接結構親緣。近期研究顯示，不同 formal intermediate languages 會實際影響 LLM neurosymbolic reasoning 的 syntactic / semantic performance；ProofBridge 等工作則開始同時要求自然語言與 Lean 形式化之間的 type correctness 與 semantic correctness。這支持本文的中心論點：**中介層不是透明管道；其表示選擇本身會影響可計算性、可驗證性與保真度。**

本文定義 Multi-Layer Bridge System（MLBS）、層間契約、forward execution path、reverse audit path、semantic anchor graph 與 translation-loss budget；證明一個簡單的逐層誤差累積上界，並提出 certificate separation、anti-laundering、traceability、uncertainty preservation 與 human intervention depth 等八項設計原則。本文亦承接作者既有「主體—語言—對象對齊模型」的多層語言棧與 Symbol-as-Operator System（SOS）的「符號可同時攜帶語義與操作結構」觀，但不將這些既有內部框架直接當成本文已驗證的 universal solution。

本篇最後提出五類失敗：形式層失真、解釋洗白、不可追溯壓縮、跨層權限漂移與專家層空洞化。Paper 07 將進一步研究：何時任何有限多層橋都不可避免地失真、過貴、不可驗或不可計算。

**關鍵詞：** 多層符號橋、AI-native representation、formal intermediate language、autoformalization、proof-carrying code、semantic preservation、human-readable explanation、expert layer、provenance、traceability、AI for Science

---

# 0. 問題：未來人類是否只剩意圖層？

考慮一個極端但合理的未來結構：

$$
\boxed{
H_{\mathrm{intent}}
\rightarrow
A_{\mathrm{opaque}}
\rightarrow
Y.
}
$$

人類只提供：

> 我要更好的電池。  
> 我要一個新的數學定理。  
> 我要這段程式安全且更快。  
> 我要一個符合這些條件的新材料。

AI 在內部：

$$
\mathfrak W_A
$$

完成：

- 高維搜尋；
- machine-native 推理；
- 多代理協作；
- 自動證明；
- 模擬；
- 程式生成；
- 實驗規劃。

最後只回：

> 完成。

技術上這可能非常高效。

但對科學文明而言，這種架構有一個巨大代價：

$$
\boxed{
\text{結果能力上升}
\quad
\text{但中間可承接知識下降。}
}
$$

---

# 1. 「可讀」不是只有一種

我們首先反對一個常見二分：

$$
\text{human-readable}
\quad\text{vs}\quad
\text{machine-readable}.
$$

這太粗。

實際上至少有：

1. machine-operational；
2. machine-verifiable；
3. expert-readable；
4. general-human-readable。

因此：

$$
\boxed{
\text{readability is layer-relative}.
}
$$

一個 Lean proof：

- 對一般人很難讀；
- 對數學形式化專家可讀；
- 對 kernel 可驗；
- 對 theorem prover 可操作。

一個 latent vector：

- 對人可能不可讀；
- 對模型卻可以直接參與後續計算。

所以：

$$
\boxed{
\text{不可被一般人直接讀}
\neq
\text{完全不可審核}.
}
$$

---

# 2. 四層架構

本文定義：

$$
\boxed{
\mathbb L
=
(
L_A,L_F,L_E,L_H
).
}
$$

---

## 2.1 $L_A$：AI-native / Machine-Operational Layer

這一層只要求：

- 對 AI / Agent 高效率；
- 可進入 tool / runtime；
- 可壓縮；
- 可組合；
- 可高速搜索；
- 可以是人類陌生格式。

例如可能包括：

- latent code；
- graph state；
- operator representation；
- machine-specific DSL；
- structured protocol；
- learned tokens；
- multimodal states；
- future AI-oriented symbol formats。

本文不假設任何目前格式，例如 JSON，是 AI 的「內在語言」。

---

## 2.2 $L_F$：Formal / Verifiable Shared Layer

這一層的任務不是漂亮。

而是：

$$
\boxed{
\text{把可驗證義務寫清楚。}
}
$$

包括：

- formal specification；
- theorem statement；
- proof object；
- type；
- invariant；
- contract；
- pre/postcondition；
- execution certificate；
- test witness；
- model-checking condition；
- proof-carrying artifact。

 $L_F$ 的價值是：

> 不需要知道 AI 內部每一步怎麼想，仍可檢查它聲稱的重要結論是否滿足形式條件。

---

## 2.3 $L_E$：Expert-Facing Semantic Layer

這一層面向：

- 數學家；
- 物理學家；
- 工程師；
- 程式設計師；
- 醫學／領域專家。

它需要能回答：

- 問題是什麼？
- 哪些假設用了？
- 哪些步驟是定理？
- 哪些是數值逼近？
- 哪些是 heuristic？
- 哪些是證書？
- 哪些是模型外推？
- 失效條件是什麼？
- 怎麼重現？

所以：

$$
L_E
$$

不是「白話」。

它可以非常技術化。

---

## 2.4 $L_H$：General Human Layer

面向一般決策者／非專家。

它至少要提供：

- 目的；
- 主要結論；
- 重要限制；
- 風險；
- 不確定性；
- 下一步；
- 哪些內容不能只靠摘要相信。

它不是把全部數學翻成故事。

而是：

$$
\boxed{
\text{decision-sufficient human interface}.
}
$$

---

# 3. 為什麼不能只做 $L_A\to L_H$

最直覺架構：

$$
L_A
\rightarrow
L_H.
$$

例如：

> AI 做完 10 億步推理，最後自動寫一篇很好懂的報告。

問題在於：

$$
\boxed{
\text{explanation fluency}
\neq
\text{semantic fidelity}.
}
$$

如果中間沒有：

$$
L_F,
$$

人類可能只得到一個「看起來合理」的故事。

這就是本文稱為：

$$
\boxed{
\text{Explanation Laundering}.
}
$$

---

# 4. Explanation Laundering

定義：

若原始 AI artifact：

$$
a_A
$$

包含錯誤、不確定性或不可驗證跳躍，

但：

$$
\tau_{AH}(a_A)
$$

被生成為流暢、確定、合理的人類敘述，

使接收者無法再看到原始風險，

則稱：

$$
\boxed{
\text{explanation laundering}.
}
$$

這是未來 AI 科學的一個重要風險。

---

# 5. Formal Layer 的角色：不要讓解釋負責真值

本文主張：

$$
\boxed{
\text{Validity}
\leftarrow
L_F,
}
$$

而：

$$
\boxed{
\text{Understanding}
\leftarrow
L_E,L_H.
}
$$

二者不可混。

例如：

### 數學

 $L_F$：

```text
Lean theorem + proof object
```

 $L_E$：

> 這個證明依賴 Lemma A/B/C，核心使用 induction。

 $L_H$：

> 在這些公理與定義下，形式證明已通過 kernel 檢查。

---

# 6. Proof-Carrying Code 提供的重要前例

Necula 的 Proof-Carrying Code（PCC）提出一個非常重要的架構：

> 不可信 code provider 除了傳送程式，也傳送一個 host 可以快速驗證的 safety proof。[1]

這裡最重要的不是歷史上的具體安全政策。

而是結構：

$$
\boxed{
\text{artifact}
+
\text{certificate}.
}
$$

因此本文把它一般化成：

$$
\boxed{
a_A
+
c_F.
}
$$

AI-native 結果可以很難讀，

但應盡可能附帶：

- proof；
- certificate；
- witness；
- invariant report；
- reproducer；
- test trace。

---

# 7. CompCert：中介表示可以多層，但語義保持要被證明

CompCert 的 verified compiler 工作展示：

$$
\text{high-level source}
\rightarrow
\text{multiple intermediate representations}
\rightarrow
\text{assembly}
$$

可以在 compiler pass 間建立 formal semantic preservation proof。[2]

這是一個對本文極重要的類比。

我們不應要求：

$$
L_A=L_F=L_E=L_H.
$$

真正需要的是：

$$
\boxed{
\text{每一層轉換都具有明確 preservation contract}.
}
$$

---

# 8. 中介語言不是透明選擇

2025 年「Intermediate Languages Matter」研究直接指出，在 neurosymbolic LLM reasoning 中，不同 formal intermediate language 的選擇會影響模型 syntactic 與 semantic reasoning performance。[3]

因此：

$$
\boxed{
\text{translation layer}
\neq
\text{neutral pipe}.
}
$$

它會：

- 改變 search space；
- 改變可表達性；
- 改變錯誤型態；
- 改變 syntax burden；
- 改變 solver interaction。

所以本文不尋找單一神聖 $L_F$。

---

# 9. Autoformalization：NL ↔ Formal Layer 正在成為真實工程問題

2024–2025 的 Lean autoformalization 工作顯示，自然語言到形式語言的 translation 需要：

- compiler / type-check feedback；
- semantic equivalence checking；
- iterative repair；
- process supervision。

ProofBridge 更進一步把自然語言 theorem+proof 到 Lean theorem+proof 的轉換視為 semantic alignment 問題，並同時評估 type correctness 與 semantic correctness。[4][5][6]

這支持：

$$
\boxed{
L_E
\leftrightarrow
L_F
}
$$

不是單向「翻譯一次就算」。

它應是：

$$
\boxed{
\text{translate}
\rightarrow
\text{verify}
\rightarrow
\text{repair}.
}
$$

---

# 10. Multi-Layer Bridge System

定義：

$$
\boxed{
\mathfrak B
=
(
\mathbb L,
\mathbb T,
\mathbb V,
\mathbb P
).
}
$$

其中：

$$
\mathbb L
=
(L_A,L_F,L_E,L_H)
$$

是各表示層。

$$
\mathbb T
=
\{\tau_{ij}\}
$$

是層間轉換。

$$
\mathbb V
=
\{V_i,V_{ij}\}
$$

是驗證器。

$$
\mathbb P
$$

是 provenance / traceability graph。

---

# 11. 不要求全互連

並不需要：

$$
\forall i,j,\tau_{ij}
$$

都存在。

實際上更合理的是：

$$
L_A
\rightleftarrows
L_F
\rightleftarrows
L_E
\rightleftarrows
L_H.
$$

再保留一些 shortcut：

$$
L_A\to L_E,
$$

但 shortcut 不能跳過必要 verifier。

---

# 12. 雙平面架構

## 12.1 Execution Plane

$$
\boxed{
L_H/L_E
\rightarrow
L_F
\rightarrow
L_A
\rightarrow
\text{Runtime}.
}
$$

人類意圖不一定每次都經 formal proof 才能執行。

但高風險操作應提高 formal gate。

---

## 12.2 Audit / Understanding Plane

$$
\boxed{
\text{Runtime}
\rightarrow
L_A
\rightarrow
L_F
\rightarrow
L_E
\rightarrow
L_H.
}
$$

它負責：

- 記錄；
- 證書；
- 形式核驗；
- 專家重建；
- 人類摘要。

---

# 13. Layer Contract

對：

$$
\tau_{ij}:L_i\to L_j,
$$

定義 contract：

$$
\boxed{
\mathcal C_{ij}
=
(
S,O,U,N,P,R
).
}
$$

---

## 13.1 $S$：Semantic Fidelity

任務核心：

$$
\mathcal K_T
$$

不能被破壞。

---

## 13.2 $O$：Operational Fidelity

如果：

$$
a_i
$$

在上一層代表「只讀」，

下一層不能變成「可寫」。

---

## 13.3 $U$：Uncertainty Fidelity

$$
\text{likely}
\not\to
\text{certain}.
$$

---

## 13.4 $N$：Norm / Permission Fidelity

保留：

- permission；
- policy；
- safety；
- scope。

---

## 13.5 $P$：Provenance

每一個輸出能追到：

- parent artifact；
- model/tool；
- version；
- transform；
- verifier；
- timestamp / hash。

---

## 13.6 $R$：Reconstruction / Reverse Trace

不要求真正反函數：

$$
\tau^{-1}.
$$

但要求至少能回答：

> 這個敘述對應哪個 formal object / native artifact？

---

# 14. Semantic Anchor Graph

定義：

$$
\boxed{
\mathcal G_{\mathrm{anchor}}
=
(V,E).
}
$$

node 可以是：

- AI artifact；
- formal theorem；
- source code；
- proof；
- expert claim；
- human statement。

edge 標記：

- translated-from；
- proved-by；
- compiled-to；
- summarized-from；
- depends-on；
- contradicts；
- approximates；
- generated-by。

---

## 14.1 為什麼需要 graph，不只 hierarchy

因為一個：

$$
L_H
$$

句子可能同時依賴：

- 3 個 formal theorem；
- 1 個 simulation；
- 2 個 empirical datasets。

所以：

$$
\boxed{
\text{provenance is a graph}.
}
$$

---

# 15. Claim-level anchors

每個 human/expert claim：

$$
c
$$

至少可以有：

$$
\operatorname{anchor}(c)
=
\{v_1,\ldots,v_k\}.
$$

例如：

> 「此演算法在條件 $C$ 下安全。」

anchor 到：

- formal specification；
- proof certificate；
- compiler artifact；
- regression tests。

---

# 16. Translation Loss Budget

每層都有可能損失資訊。

令：

$$
\epsilon_{AF},
\epsilon_{FE},
\epsilon_{EH}
$$

為三段 task-semantic distortion。

---

## 16.1 最簡加法界

若：

$$
d
$$

滿足 triangle inequality，

則：

$$
\boxed{
d(L_A,L_H)
\le
\epsilon_{AF}
+
\epsilon_{FE}
+
\epsilon_{EH}.
}
$$

因此：

$$
\boxed{
\text{多一層}
}
$$

不是免費的。

每層都增加新的失真風險。

---

# 17. 一般 Lipschitz 誤差累積上界

假設：

$$
\tau_i
$$

的 Lipschitz constant：

$$
K_i.
$$

而第 $i$ 層引入局部誤差：

$$
\epsilon_i.
$$

遞迴：

$$
e_{i+1}
\le
K_i e_i+\epsilon_i.
$$

則經 $n$ 層：

$$
\boxed{
e_n
\le
\left(
\prod_{j=0}^{n-1}K_j
\right)e_0
+
\sum_{i=0}^{n-1}
\left(
\epsilon_i
\prod_{j=i+1}^{n-1}K_j
\right).
}
$$

若：

$$
e_0=0,
$$

則：

$$
\boxed{
e_n
\le
\sum_{i=0}^{n-1}
\epsilon_i
\prod_{j=i+1}^{n-1}K_j.
}
$$

---

## 17.1 證明

由：

$$
e_{i+1}
\le
K_i e_i+\epsilon_i
$$

逐層代入即可。

$$
\square
$$

---

## 17.2 意義

不是只有：

> translation error 每層加一點。

如果後面的轉換：

$$
K_i>1,
$$

前面的小錯誤可能被放大。

所以：

$$
\boxed{
\text{early semantic error can amplify downstream}.
}
$$

---

# 18. Formal Layer 應優先擋住什麼

 $L_F$ 不應試圖形式化一切。

優先級應由風險決定。

---

## 18.1 Tier 0：無形式義務

低風險：

- 美學文字；
- 非關鍵摘要；
- brainstorming。

---

## 18.2 Tier 1：Schema / Type

- data shape；
- argument type；
- interface contract。

---

## 18.3 Tier 2：Invariant / Tests

- file scope；
- permission；
- safety property；
- regression behavior。

---

## 18.4 Tier 3：Proof / Certificate

高風險：

- theorem；
- cryptographic property；
- memory safety；
- compiler transformation；
- high-stakes decision rule。

因此：

$$
\boxed{
\text{formalization depth}
=
f(\text{risk},T).
}
$$

---

# 19. Human Intervention Depth

人類不是只有：

$$
\text{Intent}
$$

與：

$$
\text{Accept}.
$$

定義：

$$
D_H
$$

為 human intervention depth。

---

## 19.1 $D_H=0$：Intent-only

只給目的。

---

## 19.2 $D_H=1$：Outcome audit

看結果、風險、不確定性。

---

## 19.3 $D_H=2$：Expert-structure audit

可以讀：

$$
L_E.
$$

---

## 19.4 $D_H=3$：Formal audit

能檢查：

$$
L_F
$$

或依賴 proof assistant / verifier。

---

## 19.5 $D_H=4$：Native forensic access

必要時可對：

$$
L_A
$$

做 instrumentation / probe / trace。

不是要求人「理解全部 latent state」。

而是：

> 具有調查與驗證通道。

---

# 20. 科學文明的最低要求不是所有人懂全部

不可能要求：

> 每個一般人理解 AI 的全部量子材料模型。

傳統科學也不是這樣。

真正需要的是：

$$
\boxed{
\text{layered epistemic access}.
}
$$

不同角色：

- public；
- domain expert；
- formal-method expert；
- machine verifier；

各自在不同層工作。

---

# 21. 人類的角色重新分配

未來人類可保留：

1. 問題與價值選擇；
2. 任務定義；
3. 驗證標準；
4. 反例設計；
5. expert theory reconstruction；
6. formal obligation selection；
7. ethical / political decision；
8. provenance audit。

所以：

$$
\boxed{
\text{AI-native reasoning}
\not\Rightarrow
\text{human epistemic eviction}.
}
$$

前提是架構真的提供中間層。

---

# 22. 內部理論：多層語言棧已存在前置原型

既有《主體—語言—對象對齊模型》已提出至少十二層的語言棧，包括：

- 前意圖壓力；
- 被指生成；
- 意圖；
- 底空間尋址；
- 對象切分；
- 命名；
- 概念自然語言；
- 結構化自然語言；
- 形式骨架；
- 約束驗證；
- 共同底空間比對；
- 證書輸出。

該框架把語言看成：

$$
\boxed{
\text{前符號意圖}
\rightarrow
\text{可共享對象}
}
$$

的多層編譯過程，而非一次性文字輸出。

本文不完整承接其認識論主張。

但其「多層棧＋約束驗證＋證書」結構與 MLBS 高度相容。

---

# 23. 內部理論：SOS 作為 AI-native layer 候選之一

既有 Symbol-as-Operator System（SOS）主張符號不只是識別碼，而可封裝：

- geometry；
- semantics；
- composition；

並把符號組合理解成 operator composition。

本文不主張 SOS 已經是：

$$
L_A^\ast
$$

或 universal AI-native language。

它在本文中的地位只是：

$$
\boxed{
\text{一個 }L_A
\text{ 候選設計空間。}
}
$$

Paper 02 已經證明：

> 不應把某個固定格式輕易提升為 universal solution。

---

# 24. 內部 AICL 的啟示：machine-facing layer 也可拆 governance

既有 AICL（AI Ingestion & Capability Layer）把網站的 AI-facing architecture 分成：

- manifest；
- corpus；
- capability；
- governance；

使 agent 能 ingest、cite、invoke、verify 網站能力。

這提醒本文：

$$
L_A
$$

本身也不必是一層單一 blob。

可以進一步拆：

$$
L_A
=
(
L_A^{\mathrm{data}},
L_A^{\mathrm{cap}},
L_A^{\mathrm{gov}}
).
$$

也就是：

> 給 AI 看懂資料、知道能做什麼、知道不可以做什麼，是三件不同的事。

---

# 25. 跨層權限漂移

考慮：

 $L_H$：

> 「幫我看看檔案，不要修改。」

 $L_E$：

> inspect repository.

 $L_F$：

```text
permission = read_only
```

 $L_A$：

```text
tool = write_file
```

即使最後輸出：

> 「已查看。」

整個系統仍發生：

$$
\boxed{
\text{permission drift}.
}
$$

因此 norm / permission 必須是：

$$
\boxed{
\text{cross-layer invariant}.
}
$$

---

# 26. 跨層不確定性漂移

 $L_A$：

$$
P(H)=0.63.
$$

 $L_F$：

```text
confidence ∈ [0.55,0.70]
```

 $L_E$：

> 證據略偏向 H。

 $L_H$：

> H 已被證明。

失敗。

所以：

$$
\boxed{
U_A
\rightarrow
U_F
\rightarrow
U_E
\rightarrow
U_H
}
$$

必須有 fidelity contract。

---

# 27. Formal 層不能洗白不完整模型

另一種 laundering：

AI-native model：

> heuristic approximation.

自動形式化：

> theorem specification.

如果：

$$
L_F
$$

只形式化「AI 自己編的一個錯誤 surrogate」，

即使 proof checker 通過，

也不能推出：

$$
\text{original-world claim true}.
$$

因此：

$$
\boxed{
\text{formal correctness}
\neq
\text{model adequacy}.
}
$$

這是科學 AI 特別重要的邊界。

---

# 28. 必須區分三種證明鏈

## 28.1 Syntactic validity

形式 object 可 parse / type-check。

---

## 28.2 Internal semantic validity

proof 對 formal specification 成立。

---

## 28.3 External adequacy

formal specification 是否忠實表達：

- 原始科學命題；
- 現實系統；
- 使用者需求。

ProofBridge 等 autoformalization 工作開始把 type correctness 與 semantic correctness分開評估，正是同一問題的實際版本。[6]

---

# 29. Multi-Layer Verification Matrix

| Transform | 必查項 |
|---|---|
| $L_H\to L_E$ | intent / uncertainty / scope |
| $L_E\to L_F$ | formalization adequacy |
| $L_F\to L_A$ | executable binding / permission |
| $L_A\to Runtime$ | operational safety |
| Runtime $\to L_F$ | certificate / trace |
| $L_F\to L_E$ | theorem / evidence interpretation |
| $L_E\to L_H$ | decision fidelity / uncertainty |

---

# 30. Round-Trip Consistency

理想但不要求字面一致：

$$
x_H
\rightarrow
x_F
\rightarrow
x'_H.
$$

要求：

$$
x_H
\approx_T^\delta
x'_H.
$$

即 Paper 04 的 TSSH。

---

## 30.1 Round-trip test

對每個 high-risk instruction：

1. human input；
2. formalize；
3. compile / bind；
4. reverse-render；
5. compare task core。

如果：

$$
D_T(x_H,x_H')>\delta,
$$

禁止執行。

---

# 31. Commutativity Test

若一個高層意圖可以經兩條路：

$$
L_E
\rightarrow
L_F
\rightarrow
L_A
$$

與：

$$
L_E
\rightarrow
L_A,
$$

則要求在 runtime 相關結果上：

$$
\boxed{
\tau_{FA}\circ\tau_{EF}
\approx_T
\tau_{EA}.
}
$$

若兩路結果差太多，

代表：

- formalization 不足；
- direct translator 漂移；
- layer contract 不一致。

---

# 32. Multi-Layer Bridge 不是越多層越好

層太少：

$$
\text{opaque}.
$$

層太多：

$$
\text{translation loss}
+
\text{latency}
+
\text{maintenance cost}.
$$

因此層數也是一個最佳化問題：

$$
\boxed{
n^\ast
=
\arg\min_n
\left[
E_{\mathrm{semantic}}
+
C_{\mathrm{compute}}
+
C_{\mathrm{audit}}
+
C_{\mathrm{latency}}
\right].
}
$$

---

# 33. Layer skipping

低風險 micro-task：

$$
L_H
\rightarrow
L_A
$$

可以合理。

例如：

> 把按鈕 margin 加 2 px。

不需要 Lean proof。

---

## 33.1 高風險不得任意跳層

例如：

- 飛控 code；
- cryptographic code；
- medicine；
- theorem claim；
- irreversible database migration。

可要求：

$$
L_H
\rightarrow
L_E
\rightarrow
L_F
\rightarrow
L_A.
$$

因此：

$$
\boxed{
\text{bridge depth is risk-adaptive}.
}
$$

---

# 34. Certificate-Carrying Scientific Result

本文提出一個未來 AI Science artifact：

$$
\boxed{
\mathcal R
=
(
y,
c,
p,
u,
e
).
}
$$

其中：

- $y$：result；
- $c$：certificate / proof / verifier output；
- $p$：provenance；
- $u$：uncertainty；
- $e$：expert explanation。

一般人看到：

$$
L_H(y,u).
$$

專家可以下鑽：

$$
L_E.
$$

形式驗證者可以下鑽：

$$
L_F.
$$

系統 forensic 可追：

$$
L_A.
$$

---

# 35. 五類失敗

## F1：Formalization Mismatch

$$
L_E\not\approx L_F.
$$

形式證明正確，但證明錯命題。

---

## F2：Explanation Laundering

$$
L_H
$$

比原始證據更確定、更完整。

---

## F3：Trace Collapse

 $L_H$ claim 找不到：

$$
L_F/L_A
$$

anchor。

---

## F4：Permission Drift

跨層 action scope 改變。

---

## F5：Expert Hollowing

系統只保留：

$$
L_A,L_H,
$$

形式層與專家層逐漸消失。

結果是：

> 一般人聽得懂故事，但沒有專家能重建中間科學。

這正是本文最想避免的文明級失敗。

---

# 36. 八項設計原則

1. **Native Freedom**  
   不強迫 $L_A$ 人類可讀。

2. **Formal Obligation**  
   高風險 claim 應有 $L_F$ obligation。

3. **Certificate Separation**  
   correctness 不靠 explanation。

4. **Expert Recoverability**  
   $L_E$ 必須能重建假設、依賴與失效條件。

5. **Human Decision Sufficiency**  
   $L_H$ 必須保留風險、不確定性與可行選項。

6. **Cross-Layer Permission Invariance**  
   權限不可漂移。

7. **Claim-Level Provenance**  
   每個重要 claim 可追 anchor。

8. **Risk-Adaptive Depth**  
   低風險可跳層；高風險加深驗證鏈。

---

# 37. 一個簡單的 Human Inclusion Metric

定義：

$$
\boxed{
I_H(T)
=
w_0D_0
+
w_1D_1
+
w_2D_2
+
w_3D_3
+
w_4D_4
}
$$

其中：

- $D_0$：能給意圖；
- $D_1$：能審結果；
- $D_2$：有專家可重建；
- $D_3$：形式層可驗；
- $D_4$：native forensic 可追。

這不是「民主指數」。

只是用來避免：

$$
I_H\approx D_0.
$$

即：

> 人類唯一剩下的能力就是下 prompt。

---

# 38. 五項可證偽預測

## P1：加入 $L_F$ 可降低 fluent-but-wrong explanation acceptance

在高風險任務，

有 formal verification / certificate 的架構應比：

$$
L_A\to L_H
$$

直譯更容易抓出 explanation laundering。

---

## P2：中介語言選擇會影響最終 reasoning / formalization 表現

不同：

$$
L_F^{(1)},L_F^{(2)}
$$

應造成不同 syntax error、semantic error 與 solve rate。

這已與 2025 intermediate-language study 一致。[3]

---

## P3：Claim-level provenance 提高錯誤定位速度

有 anchor graph 的 system，

在發現錯誤 claim 時應降低：

$$
T_{\mathrm{root\ cause}}.
$$

---

## P4：高風險任務的 multi-layer roundtrip 可降低 permission / scope drift

相較單次 direct translation，

加入：

$$
H\to F\to A\to H'
$$

task-core consistency check 應降低重大執行漂移。

---

## P5：保留 expert layer 可提高長期知識承接

若兩個系統 task accuracy 相同，

具有：

$$
L_E
$$

的系統應在：

- expert reproduction；
- theory modification；
- counterexample generation；

上高於只有：

$$
L_A+L_H
$$

的系統。

---

# 39. Benchmark v0.1

## 39.1 Domain A：程式設計

Input：

> 修改指定 file，不得改其他 file。

比較：

- Direct NL→Agent；
- NL→schema→Agent；
- NL→formal permission contract→Agent。

---

## 39.2 Domain B：數學

Input：

自然語言 theorem。

測：

$$
L_E
\to
L_F(\text{Lean})
\to
L_E'
$$

的：

- type correctness；
- semantic equivalence；
- proof correctness；
- human theorem fidelity。

---

## 39.3 Domain C：科學模型

AI 產出：

- equation；
- simulation；
- prediction。

要求：

$$
L_F
$$

包含：

- assumptions；
- dimensions；
- boundary conditions；
- executable model；
- uncertainty certificate。

---

## 39.4 Domain D：AI-native symbolic format

允許 AI 自己設計：

$$
L_A.
$$

但必須產生：

$$
\tau_{AF}
$$

與 verifier。

測：

> AI-native 表示是否提高效率，而不摧毀 auditability？

---

# 40. 與前五篇的統一

Paper 01：

$$
\mathfrak W_A\neq\mathfrak W_B.
$$

Paper 02：

$$
\exists\mathcal M
$$

而不是固定 universal language。

Paper 03：

$$
(A,B,T)\in\mathcal C^\ast.
$$

Paper 04：

$$
\exists\mathcal Q_T
$$

只保持 task core。

Paper 05：

$$
\widehat{\mathcal Q}_{T,t}
\rightarrow
\widehat{\mathcal Q}_{T,t+1}.
$$

Paper 06：

$$
\boxed{
\mathcal Q_T
\text{ 可以被實現在多個人／機層級。}
}
$$

即：

$$
\boxed{
L_A
\leftrightarrow
L_F
\leftrightarrow
L_E
\leftrightarrow
L_H.
}
$$

---

# 41. 下一篇：不可翻譯、不可計算與代價界

現在還剩最危險的問題。

即使有：

$$
L_A,L_F,L_E,L_H,
$$

也可能：

- 根本沒有足夠保真的 $\tau$ ；
- $\tau$ 不可計算；
- formalization cost 太高；
- audit cost 超過任務價值；
- AI-native structure 無法有限壓縮；
- 不同世界沒有共同 task quotient；
- adversarial agent 故意欺騙 bridge。

所以 Paper 07 將研究：

$$
\boxed{
\text{Impossibility}
+
\text{Trade-offs}
+
\text{Lower Bounds}.
}
$$

---

# 42. 結論

未來 AI 不需要永遠用人類看得懂的語言工作。

這種要求可能限制：

- 效率；
- 搜索；
- 新表示；
- 新數學；
- 新科學。

但反過來，

也不應接受：

$$
\boxed{
\text{Human Intent}
\rightarrow
\text{Opaque AI}
\rightarrow
\text{Unverifiable Result}
}
$$

作為唯一未來。

本文提出第三種架構：

$$
\boxed{
\text{Native Freedom}
+
\text{Formal Verifiability}
+
\text{Expert Recoverability}
+
\text{Human Decision Sufficiency}.
}
$$

也就是：

$$
\boxed{
L_A
\leftrightarrow
L_F
\leftrightarrow
L_E
\leftrightarrow
L_H.
}
$$

AI 可以在它自己的世界高速運作。

人類不必逐步模仿 AI 的內部計算。

但每個重要結果，都應盡可能留下足夠的：

$$
\boxed{
\text{certificate}
+
\text{provenance}
+
\text{expert bridge}
+
\text{human explanation}.
}
$$

這樣未來的人類才不是只剩：

> 「請做。」

與：

> 「我相信你。」

中間仍存在：

$$
\boxed{
\text{可驗、可學、可反駁、可承接的知識層。}
}
$$

---

# 參考文獻

[1] Necula, G. C. (1997). **Proof-Carrying Code.** *Proceedings of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL '97)*, 106–119. DOI: 10.1145/263699.263712.

[2] Leroy, X. (2009). **Formal Verification of a Realistic Compiler.** *Communications of the ACM*, 52(7), 107–115. DOI: 10.1145/1538788.1538814.

[3] Beiser, A., Penz, D., & Musliu, N. (2025). **Intermediate Languages Matter: Formal Languages and LLMs affect Neurosymbolic Reasoning.** arXiv:2509.04083 / NeSy Workshop 2025.

[4] Lu, J., Wan, Y., Liu, Z., et al. (2024). **Process-Driven Autoformalization in Lean 4.** arXiv:2406.01940.

[5] Poiroux, A., Weiss, G., Kunčak, V., & Bosselut, A. (2024). **Improving Autoformalization using Type Checking.** arXiv:2406.07222.

[6] Jana, P., Kale, K., Tanriverdi, A. E., Song, C., Vishwanath, S., & Ganesh, V. (2025/2026). **ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings.** arXiv:2510.15681; ICLR 2026.

[7] Wang, C., Scazzariello, M., & Chiesa, M. (2025). **From Scientific Texts to Verifiable Code: Automating the Process with Transformers.** arXiv:2501.05252.

[8] Drechsler, R. (2025). **Towards LLM-based Generation of Human-Readable Proofs in Polynomial Formal Verification.** arXiv:2505.23311.

[9] Carmeli, B., Belinkov, Y., & Meir, R. (2024). **Concept-Best-Matching: Evaluating Compositionality In Emergent Communication.** *Findings of ACL 2024*, 3186–3194. DOI: 10.18653/v1/2024.findings-acl.189.

---

# 內部理論依賴

- Neo.K（2026-08-14），異質智慧動態協議生成系列 Paper 01–05。
- Neo.K（2026-06-27），《主體—語言—對象對齊模型：從前符號意圖、被指生成到共同底空間校正的多層語言棧》。本文承接多層語言棧、共同底空間校正、約束驗證與證書輸出的結構思想。
- Neo.K（2026-05/06），《符號算子系統（Symbol-as-Operator System, SOS）》v0.1。本文只把它視為 AI-native operator representation 的候選設計之一，不主張其普遍性。
- Neo.K（2026），AICL / AI Ingestion & Capability Layer。本文只承接 machine-facing layer 可區分 corpus、capability、governance 等子層的工程觀。
