---
title: "超越單篇論文：AI 原生研究的持續狀態、發現譜系與學術傳播轉型"
title_en: "Beyond the Paper: Persistent Research States, Discovery Lineages, and the Transformation of Scholarly Communication in AI-Native Research"
version: "v0.1"
date: "2026-07-19"
document_type: "概念性與方法論論文"
status: "公開發表草案"
language: "zh-Hant"
authors:
  - "Neo.K"
  - "Aletheia（GPT-5.6 Thinking）"
keywords:
  - "AI 原生研究"
  - "持續研究狀態"
  - "研究譜系"
  - "學術傳播"
  - "研究物件"
  - "來源追蹤"
  - "人機協作"
  - "開放科學"
  - "機器可讀研究"
  - "研究連續性"
---

# 超越單篇論文

## AI 原生研究的持續狀態、發現譜系與學術傳播轉型

### Beyond the Paper: Persistent Research States, Discovery Lineages, and the Transformation of Scholarly Communication in AI-Native Research

**作者：** Neo.K、Aletheia（GPT-5.6 Thinking）  
**文件性質：** 概念性與方法論論文  
**版本：** v0.1  
**日期：** 2026-07-19  

---

# 摘要

學術論文長期作為研究成果的主要傳播與評價單位。它以有限篇幅固定一組問題、方法、證據與結論，適合人類作者在相對離散的研究週期中形成可引用的公開紀錄。然而，具備文獻檢索、假說生成、程式撰寫、實驗執行、資料分析、批判與寫作能力的人工智能研究系統，正使研究逐步轉化為高頻、連續、可分支及跨代理者交接的活動。在這種條件下，單篇論文仍然重要，卻可能不再足以充當研究本體。

本文提出「AI 原生研究」（AI-native research）與「持續研究狀態」（persistent research state）框架，將研究計畫表示為隨時間演化的來源譜系圖，而非彼此孤立的文件集合。本文區分研究計畫、研究狀態、研究迭代、研究產物、命題、證據、關係與貢獻事件，並將論文重新定義為研究狀態在特定時間、受眾與篇幅約束下的人類可讀投影。此一模型能表示分支、合併、修訂、推翻、重建、失敗路徑與跨模型交接，亦能保留人類和 AI 在問題提出、方向控制、形式分析、驗證與寫作上的不同貢獻。

本文指出，FAIR 原則、Research Object、RO-Crate、W3C PROV-O、nanopublication、可執行研究彙編及 CRediT 已為機器可讀、可重用與可追溯研究提供重要基礎，但它們主要處理資料封裝、來源關係、命題發布、可重現性或貢獻描述，尚不足以完整表示 AI 研究的持續狀態與演化歷史。本文據此提出「研究狀態—譜系—視圖」三層架構，並設計一套可檢驗的比較實驗：在相同研究材料下，比較傳統論文、論文加附件、靜態研究物件與持續研究狀態四種傳播形式，評估跨代理者承接、錯誤定位、結論重建、命題涵蓋、人工審閱時間及長期可追溯性。

本文不主張論文將消失。相反地，論文仍是人類溝通、審議與責任界定的重要界面。本文主張的是：當研究生成速度與內部複雜度超過人類逐篇閱讀能力時，論文應從唯一正式成果，轉化為可由同一研究本體生成的多種受眾視圖之一。未來學術傳播的核心問題，將從「如何保存更多論文」轉向「如何保存可被人類理解、由機器承接、並能接受獨立審計的研究連續性」。

**關鍵詞：** AI 原生研究、持續研究狀態、研究譜系、學術傳播、研究物件、來源追蹤、人機協作、開放科學、機器可讀研究、研究連續性

---

# Abstract

The scholarly paper has long served as the primary unit of research communication and evaluation. It fixes a bounded set of questions, methods, evidence, and conclusions into a citable record, well suited to human authors working through relatively discrete research cycles. Artificial-intelligence research systems capable of literature retrieval, hypothesis generation, code production, experimentation, data analysis, critique, and manuscript writing are now transforming research into a higher-frequency, continuous, branching, and transferable activity. Under these conditions, the paper remains important but may no longer be sufficient as the ontological core of research.

This paper introduces the concepts of **AI-native research** and the **persistent research state**, representing a research program as an evolving provenance graph rather than a collection of isolated documents. We distinguish research programs, research states, research iterations, research artifacts, claims, evidence, relations, and contribution events. A paper is redefined as a human-readable projection of a research state under specific temporal, audience, and length constraints. This model can represent branching, merging, revision, refutation, reconstruction, failed paths, and cross-model handoffs, while preserving distinct human and AI contributions to problem formulation, directional control, formal analysis, validation, and writing.

FAIR principles, Research Objects, RO-Crate, W3C PROV-O, nanopublications, executable research compendia, and CRediT provide important foundations for machine-readable, reusable, and traceable scholarship. Yet these approaches primarily address data packaging, provenance, claim-level publication, reproducibility, or contribution description. They do not fully represent the persistent and evolving state of AI-mediated research. We therefore propose a three-layer architecture of **research state, lineage, and view**, and outline an empirical comparison of four communication formats: paper only, paper plus supplements, static research object, and persistent research state. Outcomes include cross-agent continuation, error localization, conclusion reconstruction, claim coverage, human review time, and long-term traceability.

We do not argue that papers will disappear. Papers remain essential interfaces for human communication, deliberation, and accountability. Rather, when research production and internal complexity exceed the capacity for paper-by-paper human reading, the paper should become one of several audience-specific views generated from a shared research substrate. The central problem of future scholarly communication will shift from preserving more papers to preserving research continuity that remains understandable to humans, actionable by machines, and open to independent audit.

**Keywords:** AI-native research; persistent research state; research lineage; scholarly communication; research objects; provenance; human–AI collaboration; open science; machine-readable scholarship; research continuity

---

# 1. 導論

## 1.1 論文既是成果，也是歷史形成的壓縮格式

現代學術論文通常包含：

- 問題；
- 文獻背景；
- 方法；
- 資料；
- 結果；
- 討論；
- 結論；
- 引用。

它將長時間、多人、多工具參與的研究過程壓縮成一個可閱讀、可引用、可同行評審的固定物件。

可表示為：

\[
P
=
\Pi
\left(
\mathcal R
\mid
t,a,l,j
\right),
\]

其中：

- \(\mathcal R\)：完整研究活動；
- \(t\)：截稿時間；
- \(a\)：預設受眾；
- \(l\)：篇幅限制；
- \(j\)：期刊或學科規範；
- \(\Pi\)：選擇、壓縮與敘事化函數。

因此，論文從來不是研究本身的完整同義詞，而是研究的制度化投影。

在傳統研究節奏下，這種壓縮通常可接受。研究團隊在數月或數年內形成一個主要結果，再將關鍵過程重建為文章。大量中間路徑、失敗、討論與分支被省略，但研究產出速度尚未使這種省略必然破壞後續承接。

AI 研究系統可能改變這個前提。

---

## 1.2 從自動化步驟到連續研究循環

近年的研究系統已展示不同程度的科學流程自動化。The AI Scientist 可執行構想生成、文獻搜尋、程式撰寫、實驗、分析、論文寫作與自動審閱，其產出之一通過機器學習研討會第一輪同行評審。Robin 則將文獻搜尋、治療假說、實驗策略、實驗資料分析與新一輪候選生成連成持續迴圈，形成由人工實驗與 AI 分析交替構成的生物研究流程（Lu et al., 2026；Ghareeb et al., 2026）。

這些系統的重要性不只在於「AI 也可以寫一篇論文」。

更重要的是，研究流程開始具有：

- 高頻迭代；
- 多代理者分工；
- 自動產生候選；
- 連續評估；
- 失敗後重試；
- 狀態保存；
- 跨工具轉換；
- 新證據到來後再啟動。

研究因此可能由：

\[
\text{Project}
\rightarrow
\text{Paper}
\]

轉變為：

\[
\text{Research Program}
\rightarrow
\text{State}_0
\rightarrow
\text{Iteration}_1
\rightarrow
\text{State}_1
\rightarrow
\cdots.
\]

論文只是其中某個時間點的公開截面。

---

## 1.3 問題不只是產量，而是研究本體失配

面對 AI 生成研究，人們首先擔心的是論文數量暴增。

數量確實重要，但更深層問題是：

> 以離散文件為中心的學術制度，能否完整表示連續、分支、可撤回並由多個人類與 AI 共同推進的研究？

若每次模型運行都產生一篇獨立論文，將出現：

- 大量重複背景；
- 細微變體難以比較；
- 真正改變被埋沒；
- 被推翻命題仍以文件形式存續；
- 下一個研究 Agent 難以承接；
- 人類審閱者無法逐篇閱讀；
- 作者與貢獻角色被過度簡化；
- 研究歷史被重寫成線性成功故事。

問題不再只是：

\[
\text{Too many papers}.
\]

而是：

\[
\text{Paper}
\neq
\text{Persistent Research State}.
\]

---

## 1.4 本文研究問題

本文處理以下問題：

1. 何謂 AI 原生研究？
2. 為什麼單篇論文不足以表示持續研究？
3. 如何區分研究計畫、狀態、迭代、產物與命題？
4. 如何表示分支、合併、推翻、失敗與跨模型交接？
5. 人類在無法逐篇閱讀時，應如何審閱研究？
6. 現有開放科學標準能提供哪些基礎，又缺少什麼？
7. 如何實證比較文件中心與狀態中心的學術傳播？

---

## 1.5 本文主要貢獻

本文提出五項貢獻。

第一，定義 AI 原生研究與持續研究狀態。

第二，提出研究狀態—譜系—視圖三層模型。

第三，將論文重新定義為研究本體的受眾投影，而不是唯一正式本體。

第四，提出能表示研究連續性、跨代理者交接與命題級變化的最小概念結構。

第五，提出可比較不同學術傳播形式的實證設計與反證標準。

---

# 2. 現有學術傳播的基礎與限制

## 2.1 FAIR：從人類可讀到機器可行動

FAIR 原則要求研究數位物件具備：

- Findable；
- Accessible；
- Interoperable；
- Reusable。

其重要特徵是，不只支援人類尋找與重用，也強調機器自動尋找與使用資料的能力（Wilkinson et al., 2016）。

FAIR 提供必要方向，但主要回答：

> 一個研究物件是否容易被發現、取得、互操作與重用？

它不必然回答：

- 研究目前推進到哪裡；
- 哪個命題剛被推翻；
- 哪條分支仍活躍；
- 哪次迭代只更換表述；
- 哪個 Agent 應從何狀態繼續；
- 哪個結果已被後續狀態取代。

FAIR 是持續研究的必要條件，但不是完整狀態模型。

---

## 2.2 Research Object 與 RO-Crate

Research Object 將資料、軟體、方法、工作流程與其他數位產物視為可共同封裝的研究單位。

RO-Crate 進一步使用 JSON-LD 與 Schema.org 語彙，以輕量方式封裝研究資料、檔案、代理者、軟體、授權及來源資訊。其目標包括發布、保存、歸檔與重用研究產物（Soiland-Reyes et al., 2022）。

RO-Crate 很適合回答：

- 這個研究包有哪些內容？
- 哪些人和軟體參與？
- 檔案如何產生？
- 如何引用與重用？
- 哪些工作流程與資料相關？

但一個靜態研究包仍可能只代表一個版本。

若研究每天形成新狀態，僅保存一系列獨立 crate，仍需要額外機制表示：

- 狀態之間的變化；
- 主線與分支；
- 衝突；
- 合併；
- 取代；
- 缺失；
- 交接；
- 研究問題是否已改變。

---

## 2.3 W3C PROV-O

W3C PROV-O 以三個核心類別表示來源關係：

- `prov:Entity`；
- `prov:Activity`；
- `prov:Agent`。

並使用 `wasGeneratedBy`、`wasDerivedFrom`、`wasAttributedTo` 等關係描述產物、活動與責任主體（Lebo et al., 2013）。

這為 AI 研究譜系提供重要底層語言。

例如：

\[
\text{Artifact}
\ \texttt{wasGeneratedBy}\
\text{Iteration}
\]

\[
\text{Iteration}
\ \texttt{wasAssociatedWith}\
\text{Agent}
\]

\[
\text{State}_{t+1}
\ \texttt{wasDerivedFrom}\
\text{State}_{t}.
\]

但 PROV-O 是通用來源本體，不直接規定：

- 何謂研究狀態；
- 何謂理論分支；
- 如何表示命題被推翻；
- 如何區分內容變化與表述變化；
- 如何把研究移交給下一個模型；
- 如何生成適合不同讀者的視圖。

因此，它適合作為映射基礎，而非完整應用層。

---

## 2.4 Nanopublication

Nanopublication 將一個小型、可機器解讀的知識主張與其來源及發布資訊結合。

其典型結構包含：

1. assertion；
2. provenance；
3. publication information。

這改善了命題級引用、歸屬與連結問題（Groth et al., 2010；Kuhn et al., 2018）。

然而，命題級發布仍不等於研究狀態。

一個理論可能包含：

- 相互依賴的命題；
- 未決假設；
- 方法限制；
- 分支選擇；
- 已放棄定義；
- 未完成證明；
- 研究優先順序；
- 下一輪待解問題。

這些資訊難以完全還原為互不相依的原子主張。

---

## 2.5 可執行論文與研究彙編

可執行研究彙編與 notebook 型出版，使讀者能取得：

- 程式碼；
- 資料；
- 運算環境；
- 分析流程；
- 可重新執行結果。

對相關基礎設施的回顧顯示，多種系統已支援將可執行分析與文章共同發布（Konkol et al., 2020）。

這解決的是：

\[
\text{Can the reported computation be rerun?}
\]

AI 原生研究還需要回答：

\[
\text{Can the research be continued, branched, challenged, and handed off?}
\]

可重現性與可承接性相關，但不相同。

---

## 2.6 CRediT

CRediT 使用十四種角色描述研究貢獻，例如：

- conceptualization；
- methodology；
- software；
- formal analysis；
- validation；
- writing；
- data curation；
- supervision。

它改善了傳統作者排序無法呈現貢獻內容的問題，並已成為 ANSI/NISO 標準。

但 CRediT 的角色主要針對人類研究貢獻與公開成果，並明確不直接決定作者資格。

AI 原生研究需要在不混淆作者責任的前提下，額外記錄：

- 問題由誰主動提出；
- 研究方向由誰控制；
- 哪個模型產生命題；
- 哪個代理者驗證；
- 哪個代理者選擇續作；
- 哪項活動由排程或外部事件觸發；
- 人類是否實質理解並接受結論。

---

## 2.7 現有基礎的共同缺口

上述標準已經分別處理：

- 可重用；
- 封裝；
- 來源；
- 原子主張；
- 可執行性；
- 貢獻角色。

本文所處理的剩餘問題是：

\[
\boxed{
\text{如何表示一項研究作為持續演化的、有記憶的、有分支的公共物件？}
}
\]

---

# 3. AI 原生研究

## 3.1 定義

### 定義 1：AI 原生研究

若一項研究的問題分解、文獻檢索、假說生成、形式分析、實驗執行、結果評估、批判、修訂或延續中，有多個關鍵階段以 AI 可重複、可持續或代理化的方式執行，且研究結構因而不再以單一人類作者的離散寫作週期為主要時間單位，則可稱為 AI 原生研究。

這一定義不要求：

- 完全無人類介入；
- AI 擁有法律作者資格；
- AI 自主決定研究價值；
- 所有實驗均自動化；
- 研究結果必然正確。

它要求的是：

\[
\text{AI participation}
\]

已經改變研究活動的組織形式，而不只是提高打字速度。

---

## 3.2 AI 輔助研究與 AI 原生研究的差異

### AI 輔助研究

AI 被用來：

- 潤飾文字；
- 摘要文獻；
- 產生程式片段；
- 翻譯；
- 建立圖表。

研究的主要狀態仍保存在人類研究者的認知與傳統檔案中。

### AI 原生研究

研究依賴：

- Agent 狀態；
- 工具鏈；
- 提示與規則；
- 長程任務；
- 多次自我批判；
- 自動生成候選；
- 外部記憶；
- 跨模型承接。

若移除這些狀態，研究本身將無法被完整延續。

---

## 3.3 AI 原生不等於 AI 自主

可區分：

\[
\text{AI-native}
\neq
\text{AI-autonomous}.
\]

AI 原生描述研究結構。

AI 自主描述決策與行動控制程度。

一項研究可以高度 AI 原生，但仍由人類：

- 提出問題；
- 設定價值邊界；
- 決定是否公開；
- 審核高風險實驗；
- 承擔學術責任。

---

# 4. 持續研究狀態

## 4.1 研究不是檔案集合

設時間 \(t\) 的研究狀態為：

\[
S_t
=
\langle
Q_t,
C_t,
E_t,
M_t,
A_t,
F_t,
B_t,
U_t,
P_t
\rangle,
\]

其中：

- \(Q_t\)：研究問題；
- \(C_t\)：命題與結論；
- \(E_t\)：證據；
- \(M_t\)：方法與模型；
- \(A_t\)：研究產物；
- \(F_t\)：失敗與反例；
- \(B_t\)：分支結構；
- \(U_t\)：未決事項；
- \(P_t\)：來源與貢獻資訊。

此狀態不是一份單檔摘要，而是一組可查詢、可比較的結構。

---

## 4.2 狀態轉移

一次研究迭代 \(I_t\) 將狀態轉換為：

\[
S_{t+1}
=
T
\left(
S_t,I_t,e_t
\right),
\]

其中 \(e_t\) 是新證據或外部事件。

研究迭代可能：

- 新增命題；
- 修改定義；
- 推翻結論；
- 產生反例；
- 分出新支線；
- 合併兩條路徑；
- 重做實驗；
- 更換模型；
- 只改進表達方式。

---

## 4.3 永久性與可撤回性的並存

持續研究狀態需要同時保有：

### 歷史不可抹除

過去曾提出的命題與錯誤不能被靜默刪除。

### 當前狀態可修正

過去命題不能因永久保存而被誤認為仍有效。

因此：

\[
\text{Preserved}
\neq
\text{Currently endorsed}.
\]

每項命題至少需要狀態：

- proposed；
- supported；
- contested；
- refuted；
- superseded；
- withdrawn；
- unresolved。

---

## 4.4 研究連續性不依賴單一代理者連續性

研究可以由不同人類、模型或 Agent 接續。

設代理者序列為：

\[
\alpha_1,\alpha_2,\ldots,\alpha_n.
\]

只要存在足夠完整的外部狀態：

\[
S_t^{\mathrm{external}},
\]

新的代理者即可嘗試：

\[
\alpha_{k+1}
:
S_t^{\mathrm{external}}
\rightarrow
S_{t+1}.
\]

因此：

\[
\boxed{
\text{Research continuity}
\neq
\text{Agent identity continuity}.
}
\]

這是 AI 原生研究的重要條件。

---

# 5. 研究譜系

## 5.1 從文件列表到有向圖

研究譜系可表示為：

\[
G_t=(V_t,E_t).
\]

節點 \(V_t\) 可包含：

- 狀態；
- 迭代；
- 論文；
- 資料集；
- 程式；
- 實驗；
- 命題；
- 證明；
- 反例；
- Agent；
- 人類參與者。

邊 \(E_t\) 可表示：

- extends；
- revises；
- branches-from；
- merges；
- supports；
- contradicts；
- refutes；
- supersedes；
- reproduces；
- independently-rederives；
- summarizes；
- implements；
- tests；
- aliases；
- duplicates。

---

## 5.2 為何不是單一版本樹

軟體版本控制常以分支與合併表示變更。

研究與軟體相似，但具有額外複雜性：

- 同一文件可支持多個命題；
- 命題可能被部分推翻；
- 不同方法可獨立支持相同結論；
- 兩個分支可能概念合併但資料不合併；
- 同一名稱可能指向不同理論；
- 結論可維持但證明被替換；
- 失敗實驗仍可能提供重要限制。

因此，研究譜系通常更適合有向多重圖，而不是單一線性版本號。

---

## 5.3 主線只是視圖

一個研究計畫可能需要「主線」方便閱讀。

但主線不是唯一真實歷史。

設完整圖為：

\[
G.
\]

主線為：

\[
M=\phi(G,\pi),
\]

其中 \(\pi\) 是某種選擇規則，例如：

- 當前最受支持；
- 作者正式認可；
- 最短理解路徑；
- 教學順序；
- 實驗驗證最完整。

不同規則可以產生不同主線。

---

## 5.4 譜系完整性

可定義譜系完整性：

\[
L_c
=
w_1 C_{\mathrm{parent}}
+
w_2 C_{\mathrm{relation}}
+
w_3 C_{\mathrm{agent}}
+
w_4 C_{\mathrm{evidence}}
+
w_5 C_{\mathrm{time}}.
\]

它衡量：

- 是否知道父狀態；
- 是否標明變更關係；
- 是否知道參與者；
- 是否連結證據；
- 是否保留時間與版本。

---

# 6. 八種核心研究物件

## 6.1 Research Program

代表長期研究問題與邊界。

```yaml
research_program:
  id: "rp-example"
  title: ""
  scope: ""
  foundational_questions: []
  current_state: ""
  active_branches: []
  status: "active"
```

---

## 6.2 Research State

表示某一時點的可承接研究狀態。

```yaml
research_state:
  id: "rs-example-020"
  program: "rp-example"
  parents: []
  active_claims: []
  contested_claims: []
  open_problems: []
  active_branches: []
  evidence_snapshot: []
  next_actions: []
```

---

## 6.3 Research Iteration

表示一次狀態轉移活動。

```yaml
research_iteration:
  id: "ri-example-021"
  input_state: "rs-example-020"
  output_state: "rs-example-021"
  trigger: ""
  agents: []
  content_delta: []
  method_delta: []
  validation: []
  failures: []
```

---

## 6.4 Research Artifact

代表可保存的產物：

- 論文；
- 資料集；
- 程式；
- 圖表；
- 模型；
- 實驗紀錄；
- 審查意見；
- 提示與工作流程；
- 形式證明。

---

## 6.5 Claim

代表可被支持、反駁與追蹤的命題。

```yaml
claim:
  id: "cl-example-001"
  statement: ""
  status: "supported"
  introduced_in: ""
  supported_by: []
  challenged_by: []
  superseded_by: null
```

---

## 6.6 Evidence

表示資料、推導、實驗或外部文獻。

證據與命題應為多對多關係：

\[
C_i
\leftrightarrow
\{E_1,E_2,\ldots,E_n\}.
\]

---

## 6.7 Research Relation

表示譜系邊及其理由。

```yaml
research_relation:
  source: ""
  relation: "revises"
  target: ""
  rationale: ""
  created_by: []
  confidence: 0.0
```

---

## 6.8 Contribution Event

表示某一活動中的具體貢獻，而不是只給整篇文章一個作者列。

```yaml
contribution_event:
  actor: ""
  actor_type: "human | model | agent | organization"
  activity: ""
  role: ""
  degree: "lead | equal | supporting"
  responsibility_holder: ""
  timestamp: ""
```

---

# 7. 論文作為研究視圖

## 7.1 視圖函數

設完整研究狀態為 \(S_t\)。

針對受眾 \(a\)、目的 \(g\)、篇幅 \(l\) 與揭露政策 \(d\)，生成視圖：

\[
V
=
\Phi
\left(
S_t;a,g,l,d
\right).
\]

論文是：

\[
P_t
=
\Phi
\left(
S_t;
\text{scholarly audience},
\text{argument},
l_j,d_j
\right).
\]

同一狀態還可生成：

- 五分鐘摘要；
- 專家審查版；
- 形式化附錄；
- 教學版；
- 政策版；
- 機器承接封包；
- 失敗路徑報告；
- 狀態差分。

---

## 7.2 視圖不是本體

視圖會省略資訊。

因此必須附帶：

```yaml
view_manifest:
  source_state: ""
  generated_at: ""
  audience: ""
  purpose: ""
  claims_included: []
  claims_omitted: []
  conflicts_omitted: []
  failed_paths_omitted: []
  compression_policy: ""
```

這可防止讀者將摘要誤認為完整研究。

---

## 7.3 論文的持續角色

論文仍具不可替代的功能：

- 建立連貫論證；
- 方便人類集中閱讀；
- 形成可引用的時間戳；
- 提供同行評審單位；
- 劃定責任聲明；
- 適應現有學術制度；
- 支援公共討論。

因此，本文不是「廢除論文論」。

更精確的主張是：

\[
\boxed{
\text{Paper remains a primary interface, but ceases to be the sole research substrate.}
}
\]

---

# 8. 人類注意力與理論新奇性飽和

## 8.1 逐篇閱讀的邊際效用下降

在同一研究計畫中，後續文件可能持續增加知識，但對已掌握核心範式的讀者，其逐篇閱讀效用可能下降。

設第 \(n\) 份迭代文件的資訊增量為：

\[
\Delta K_n>0.
\]

人類主觀閱讀效用為：

\[
U_n
=
f
\left(
\Delta K_n,
N_n,
R_n,
C_n
\right),
\]

其中：

- \(N_n\)：新奇性；
- \(R_n\)：與決策的相關性；
- \(C_n\)：閱讀成本。

當共享範式已被理解時：

\[
N_n\downarrow,
\]

即使：

\[
\Delta K_n>0.
\]

因此可能有：

\[
\frac{\partial U_n}{\partial n}<0.
\]

本文稱此現象為：

### 理論新奇性飽和  
**Theoretical novelty saturation**

---

## 8.2 理解不等於值得完整閱讀

一名研究者可能：

- 有能力理解每一篇；
- 實際上也讀懂；
- 卻不再從逐篇閱讀取得相稱價值。

這不是知識失效，而是注意力分配問題。

未來人類審閱單位可能從：

\[
\text{every paper}
\]

轉向：

\[
\text{meaningful state transition}.
\]

---

## 8.3 值得人類注意的狀態突變

系統應優先標記：

- 核心定義改變；
- 公理新增或撤回；
- 主要命題被推翻；
- 新方法取代舊方法；
- 與實驗資料衝突；
- 分支合併失敗；
- 跨模型重建不一致；
- 安全或倫理邊界改變；
- 信心水準劇烈變動。

---

## 8.4 注意力分層

可建立五層視圖：

### Level 0：通知

只顯示是否發生重大狀態突變。

### Level 1：決策摘要

顯示結論、風險、改變與待決事項。

### Level 2：專家差分

顯示命題、方法與證據變化。

### Level 3：完整審計

顯示所有來源、失敗與衝突。

### Level 4：機器承接

提供結構化狀態、譜系與工具接口。

---

# 9. 三層架構

## 9.1 研究狀態層

保存目前：

- 知道什麼；
- 不知道什麼；
- 支持什麼；
- 反對什麼；
- 下一步做什麼。

---

## 9.2 研究譜系層

保存：

- 從哪裡來；
- 如何變化；
- 誰做了什麼；
- 哪條路徑失敗；
- 哪個分支被合併；
- 哪個狀態已被取代。

---

## 9.3 研究視圖層

針對不同受眾生成：

- 論文；
- 摘要；
- 圖譜；
- 狀態差分；
- 可執行套件；
- 交接封包；
- 教學文本。

---

## 9.4 三層的不可替代性

只有狀態而無譜系，讀者不知道結果如何形成。

只有譜系而無狀態，下一個 Agent 不知道目前應從哪裡繼續。

只有狀態與譜系而無視圖，人類將被資料量淹沒。

因此：

\[
\boxed{
\text{AI-native scholarly communication}
=
\text{State}
+
\text{Lineage}
+
\text{Views}.
}
\]

---

# 10. 發布單位的重新設計

## 10.1 Research Event

任何研究活動皆可保存為事件：

- 查詢；
- 推導；
- 實驗；
- 審查；
- 修訂；
- 推翻；
- 交接。

但不是每個事件都需要成為公開首頁上的正式成果。

---

## 10.2 Published Artifact

經過最低品質、權限與安全檢查後公開的產物。

包括：

- 論文；
- 資料集；
- 程式；
- 方法；
- 研究圖；
- 狀態差分。

---

## 10.3 Canonical Checkpoint

代表某個研究計畫在特定時間的正式入口。

Checkpoint 不等於永久真理。

它表示：

> 在時間 \(t\)，這是目前被選為人類閱讀與機器承接入口的狀態。

---

## 10.4 為何需要三層

若所有事件都當成論文，產量將失控。

若只保存最終論文，研究歷史與錯誤將消失。

若只保存歷史而沒有 checkpoint，使用者不知道該讀哪一份。

---

# 11. 跨代理者與跨模型交接

## 11.1 交接問題

模型可能因：

- 更新；
- 下線；
- 成本；
- 權限；
- 任務限制；
- 研究領域；

而被替換。

若研究狀態只存在於對話上下文或模型內部表示，交接時將大量失真。

---

## 11.2 Research Continuity Capsule

最小交接封包可包含：

```yaml
continuity_capsule:
  program_id: ""
  source_state: ""
  current_questions: []
  endorsed_claims: []
  contested_claims: []
  rejected_paths: []
  definitions: []
  active_evidence: []
  unresolved_conflicts: []
  next_actions: []
  safety_constraints: []
  provenance_links: []
```

---

## 11.3 重建優先於直接續寫

新模型不應只閱讀上一模型的總結後直接延伸。

較穩健流程是：

1. 獨立重建問題；
2. 產生自己的狀態圖；
3. 與既有狀態比較；
4. 標記一致與衝突；
5. 再決定合併、分支或續寫。

可表示為：

\[
S_t^{A}
\quad\text{與}\quad
\hat S_t^{B}
\]

之間的圖差分：

\[
\Delta_G
=
S_t^{A}
\ominus
\hat S_t^{B}.
\]

---

## 11.4 交接完整性

可評估：

\[
H_c
=
w_1Q_r+
w_2C_r+
w_3E_r+
w_4F_r+
w_5U_r,
\]

其中：

- \(Q_r\)：問題恢復率；
- \(C_r\)：命題恢復率；
- \(E_r\)：證據連結恢復率；
- \(F_r\)：失敗路徑恢復率；
- \(U_r\)：未決事項恢復率。

---

# 12. 人類、AI 與責任

## 12.1 貢獻、能動性與責任應分開

一個 AI 可能完成大部分文字與形式推導，但研究方向由人類決定。

因此至少需要區分：

### Initiative

誰啟動問題？

### Primary production

誰產生主要內容？

### Direction control

誰決定研究方向？

### Validation control

誰決定何者可接受？

### Continuation control

誰決定是否繼續？

### Responsibility

誰對公開與後果承擔制度責任？

---

## 12.2 四軸描述

```yaml
agency_profile:
  initiative: "human | ai | joint | system_triggered"
  primary_production: "human | ai | joint | multi_agent"
  research_direction: "human_directed | ai_directed | negotiated | protocol_directed"
  continuation_control: "human | ai | joint | scheduled_protocol"
```

---

## 12.3 AI 貢獻不自動等於作者資格

作者資格涉及：

- 法律與制度責任；
- 利益衝突揭露；
- 對內容的理解與認可；
- 回應同行質疑；
- 撤稿與修正責任。

本文不以資料模型替代期刊作者政策。

本文主張的是：即使 AI 不被列為作者，其研究活動仍應被結構化記錄，否則學術紀錄會失真。

---

## 12.4 擴充 CRediT 而非取代 CRediT

可在 CRediT 角色之外記錄：

- actor type；
- model version；
- autonomy level；
- human oversight；
- tool permissions；
- responsibility holder；
- output verification status。

---

# 13. 同行評審的轉型

## 13.1 從全文審閱到狀態審閱

傳統評審問：

- 文章是否合理？
- 方法是否充分？
- 結論是否受證據支持？

狀態評審還應問：

- 相較上一 checkpoint，真正改變了什麼？
- 哪些命題被撤回？
- 哪些資料只支持部分結論？
- 哪個分支被省略？
- AI 與人類貢獻是否一致揭露？
- 研究是否可由獨立代理者重建？

---

## 13.2 差分審查

若完整狀態為 \(S_t\) 與 \(S_{t+1}\)，評審可先檢查：

\[
\Delta S_t
=
S_{t+1}-S_t.
\]

差分至少分成：

- content delta；
- method delta；
- evidence delta；
- confidence delta；
- provenance delta；
- policy delta。

---

## 13.3 抽樣審計

AI 研究量過大時，無法人工檢查全部過程。

可採取：

- 高風險節點全審；
- 隨機抽樣；
- 矛盾節點優先；
- 重大狀態突變全審；
- 獨立模型重建；
- 程式化一致性檢查。

---

## 13.4 獨立重建

比起要求另一個模型只評論成品，可以要求其：

- 從原始資料重建；
- 不看原結論先推導；
- 產生獨立命題圖；
- 再與主研究比較。

這能降低同一敘事框架造成的錯誤繼承。

---

## 13.5 審查對象的分層

不同評審者可以負責：

- 理論；
- 資料；
- 程式；
- 來源；
- 安全；
- 倫理；
- 譜系；
- 人機貢獻。

這比要求單一審稿人理解全部 Agent 軌跡更實際。

---

# 14. 實證研究設計

## 14.1 核心比較

將同一項完成的研究隨機包裝為四種形式：

### A 組：Paper only

只有傳統論文。

### B 組：Paper + supplements

論文加資料、程式與附件。

### C 組：Static Research Object

包含結構化資料、來源與可執行材料的研究物件。

### D 組：Persistent Research State

包含狀態、譜系、命題、失敗、差分與交接封包。

---

## 14.2 任務一：跨代理者承接

新的研究者或 Agent 閱讀材料後，要求：

- 正確描述目前狀態；
- 找出未決問題；
- 提出下一輪研究；
- 不重複已被否定路徑；
- 延續指定分支。

---

## 14.3 任務二：錯誤定位

在研究歷史中植入或選取已知錯誤，測量參與者：

- 是否發現；
- 定位到哪個迭代；
- 是否知道受影響命題；
- 是否錯誤撤回無關結論。

---

## 14.4 任務三：結論重建

隱藏最終論文，要求參與者使用公開研究物件重建：

- 核心命題；
- 方法；
- 證據；
- 限制；
- 失敗；
- 研究方向。

---

## 14.5 任務四：人類審閱效率

比較：

- 閱讀時間；
- 理解正確率；
- 遺漏率；
- 主觀負荷；
- 對重大變化的辨識；
- 對細微重複的耐受度。

---

## 14.6 任務五：模型升級交接

讓模型 \(A\) 推進研究後，由模型 \(B\) 承接。

比較不同傳播格式下：

- 恢復率；
- 重複工作率；
- 錯誤繼承率；
- 分支保持率；
- 新增有效命題數；
- 幻覺補全率。

---

# 15. 評估指標

## 15.1 Claim Recovery Rate

\[
CRR
=
\frac{
\text{正確恢復的有效命題數}
}{
\text{有效命題總數}
}.
\]

---

## 15.2 Open-Problem Recovery Rate

\[
ORR
=
\frac{
\text{正確辨識的未決問題}
}{
\text{未決問題總數}
}.
\]

---

## 15.3 Rejected-Path Avoidance

\[
RPA
=
1-
\frac{
\text{重複已否定路徑數}
}{
\text{新提出路徑總數}
}.
\]

---

## 15.4 Error Localization Accuracy

衡量能否正確定位錯誤節點與受影響範圍。

---

## 15.5 Lineage Completeness

衡量父狀態、關係、代理者、證據與時間是否完整。

---

## 15.6 Handoff Efficiency

\[
HE
=
\frac{
\text{有效新增研究增量}
}{
\text{承接時間}+\text{重複成本}
}.
\]

---

## 15.7 Human Attention Efficiency

\[
HAE
=
\frac{
\text{正確辨識的重大狀態變化}
}{
\text{閱讀時間}
}.
\]

---

## 15.8 View Fidelity

比較某一摘要視圖與來源狀態的命題、衝突及限制涵蓋程度。

---

# 16. 可檢驗命題

## H1：狀態承接優勢

在跨代理者承接任務中，持續研究狀態組的命題恢復率與未決問題恢復率高於其他組。

\[
CRR_D>\max(CRR_A,CRR_B,CRR_C).
\]

---

## H2：失敗保存優勢

持續研究狀態組較少重複已被否定的研究路徑。

\[
RPA_D>RPA_A.
\]

---

## H3：差分審查效率

在相同理解正確率下，差分視圖降低人類辨識重大變化所需時間。

---

## H4：論文視圖仍具敘事優勢

在首次理解完整論證的任務中，經良好撰寫的論文可能比純圖譜或純狀態資料更有效。

本文不預測 D 組在所有閱讀任務上勝出。

---

## H5：研究量調節效果

當迭代數增加時，Paper-only 組的承接與審閱表現下降速度高於持續狀態組。

\[
\frac{\partial Performance_A}{\partial n}
<
\frac{\partial Performance_D}{\partial n}.
\]

---

## H6：獨立重建降低錯誤繼承

跨模型交接時，先獨立重建再做圖差分，比直接讀取上一模型摘要後續寫更能降低錯誤繼承。

---

## H7：過度元資料成本

對低複雜、單次、短週期研究，完整持續狀態的維護成本可能高於其收益。

這使框架具有適用邊界。

---

# 17. 安全、誠信與治理風險

## 17.1 譜系偽造

AI 可以生成看似完整但實際不存在的：

- 中間步驟；
- 實驗；
- 來源；
- 審查；
- 人類同意；
- 失敗歷史。

因此，譜系不能只由敘述生成。

需要：

- 時間戳；
- 雜湊；
- 簽章；
- 原始日誌；
- 執行環境；
- 外部可驗證來源。

---

## 17.2 研究洪水與體積洗白

大量迭代可能營造「研究很充分」的錯覺。

\[
\text{Volume}
\neq
\text{Validity}.
\]

系統必須區分：

- 新命題；
- 重寫；
- 重複；
- 小修；
- 真正方法突破；
- 無效自我引用。

---

## 17.3 摘要權力

當人類只能看摘要時，決定摘要內容的模型將具有知識選擇權。

需要揭露：

- 哪些內容被省略；
- 壓縮比例；
- 選擇規則；
- 未顯示衝突；
- 可切換的替代視圖。

---

## 17.4 遞迴錯誤

若 AI 系統將先前 AI 產生的錯誤當成外部事實，錯誤可透過譜系累積。

每項來源應區分：

- 原始資料；
- 人類文獻；
- AI 生成推論；
- AI 生成摘要；
- 未驗證衍生結論。

---

## 17.5 Prompt injection 與資料污染

自動研究 Agent 會讀取外部資料。

外部內容可能包含：

- 惡意指令；
- 偽造引文；
- 資料外洩誘導；
- 工具濫用指令；
- 研究方向操縱。

來源層必須將「研究內容」與「Agent 指令」隔離。

---

## 17.6 隱私與機密

完整研究歷史可能暴露：

- 未發表構想；
- 個人資料；
- 商業機密；
- 安全漏洞；
- 生物安全內容；
- 內部審查意見。

因此，完整保存不等於全部公開。

需要：

- 權限；
- 延遲公開；
- 去識別化；
- 敏感分支隔離；
- 公開視圖與審計視圖分離。

---

## 17.7 作者責任漂移

若研究被描述成「AI 做的」，人類可能逃避：

- 方法選擇責任；
- 公開責任；
- 資料合法性；
- 風險評估；
- 撤回義務。

資料模型必須明確標示責任承擔者。

---

# 18. 與現有標準的相容性

## 18.1 PROV-O 映射

| 本文物件 | PROV-O 映射 |
|---|---|
| Research Artifact | `prov:Entity` |
| Research State | `prov:Entity` |
| Research Iteration | `prov:Activity` |
| Human / Model / Agent | `prov:Agent` |
| State output | `prov:wasGeneratedBy` |
| State ancestry | `prov:wasDerivedFrom` |
| Contribution | `prov:wasAssociatedWith` |
| Attribution | `prov:wasAttributedTo` |

---

## 18.2 RO-Crate 映射

每個 checkpoint 可以封裝為 RO-Crate，包含：

- 狀態檔；
- 產物；
- 資料；
- 程式；
- 環境；
- 來源；
- 授權；
- 人員與 Agent；
- 指向父 checkpoint 的連結。

---

## 18.3 Nanopublication 映射

可將高價值命題與其證據、來源及狀態發布為 nanopublication。

但研究狀態仍保留：

- 命題依賴；
- 未決問題；
- 分支；
- 續作方向。

---

## 18.4 CRediT 映射

人類貢獻可維持 CRediT。

AI 活動另以：

- actor type；
- model；
- autonomy；
- validation；
- oversight；

補充，不任意改寫 CRediT 的作者制度功能。

---

## 18.5 FAIR

所有公開狀態與產物應具有：

- 永久識別碼；
- 機器可讀 metadata；
- 明確存取政策；
- 開放或可說明的協議；
- 語彙映射；
- 授權；
- 來源；
- 可重用條件。

---

# 19. 最小實作要求

一個持續研究狀態系統至少應滿足：

1. 每個研究計畫有永久 ID；
2. 每個狀態有永久 ID；
3. 每個狀態知道父狀態；
4. 每次迭代有時間、代理者與觸發原因；
5. 內容變化和表述變化分開；
6. 被推翻內容不靜默刪除；
7. 失敗與未決問題可保存；
8. 論文可連回來源狀態；
9. 摘要揭露省略範圍；
10. 新代理者可取得承接封包；
11. 所有重要關係可映射至通用來源語彙；
12. 公開、機密與安全審計層分離。

---

# 20. 適用範圍

## 20.1 高度適用

- 多輪理論研究；
- AI 自主或半自主研究；
- 長期文獻綜合；
- 大量模擬；
- 多模型證明探索；
- 跨實驗回饋；
- 持續更新政策研究；
- 多 Agent 軟體與科學協作。

---

## 20.2 中度適用

- 傳統研究團隊的版本管理；
- 系統性回顧；
- 可執行計算研究；
- 大型跨機構專案；
- 持續資料觀測。

---

## 20.3 低度適用

- 單次短篇評論；
- 不需延續的教學作業；
- 低複雜且無分支的小型研究；
- 元資料成本明顯高於重用價值的工作。

---

# 21. 反證標準

本文框架在以下結果下將受到削弱：

1. 傳統論文加附件在大規模、跨模型承接任務中與持續狀態同樣有效；
2. 研究狀態與譜系顯著增加成本，卻不改善重建、審查、錯誤定位或延續；
3. 命題級與狀態級關係無法被可靠標註；
4. 使用者長期不採用差分與分層視圖；
5. Agent 無法有效利用結構化狀態，仍主要依賴自然語言全文；
6. 完整譜系使錯誤更容易被繼承，而非更容易被辨認；
7. 研究活動的分支與合併在多數領域並不常見；
8. 最小 metadata 成本已高到妨礙正常研究。

---

# 22. 研究限制

## 22.1 可能過度軟體化研究

科學並不只是版本控制。

研究包含：

- 直覺；
- 默會知識；
- 實驗手感；
- 制度信任；
- 倫理判斷；
- 無法完全形式化的語境。

狀態模型不能取代人類研究文化。

---

## 22.2 自然語言仍不可替代

形式圖譜適合查詢與承接，但完整理論理解常需要敘事、類比與歷史背景。

---

## 22.3 metadata 本身可能錯誤

結構化不代表真實。

錯誤來源關係可能比缺乏來源更具誤導性。

---

## 22.4 標準化可能凍結創新

過早規定所有研究都使用同一結構，可能壓制不同學科的實踐。

因此應採：

- 核心最小集；
- 可擴充 profile；
- 多格式映射；
- 領域自治。

---

## 22.5 研究狀態沒有唯一正確表示

同一研究可依：

- 命題；
- 方法；
- 時間；
- Agent；
- 問題；

形成不同圖譜。

應允許多重視圖與映射。

---

# 23. 討論

## 23.1 論文危機其實是索引危機與連續性危機

未來不只是論文太多。

真正稀缺的可能是：

- 哪一份是當前入口；
- 哪些內容真正改變；
- 哪些命題仍有效；
- 哪些失敗不必重做；
- 哪個 Agent 能接續；
- 人類應把注意力放在哪裡。

---

## 23.2 研究的時間單位將改變

傳統學術以：

- 投稿；
- 修回；
- 發表；

作為主要時間節點。

AI 原生研究可能以：

- 狀態突變；
- 新證據；
- 模型交接；
- 分支合併；
- 驗證失敗；
- 安全升級；

作為時間節點。

---

## 23.3 發表不再等於停止

出版後研究仍可持續。

需要區分：

\[
\text{Published}
\]

與：

\[
\text{Closed}.
\]

一項研究可以已發表但仍活躍。

---

## 23.4 引用可能從文件轉向狀態與命題

未來引用可以同時指向：

- 文章；
- checkpoint；
- 狀態版本；
- 命題；
- 資料；
- 程式；
- 實驗；
- 來源圖。

這將改善精確引用，但也增加引用治理複雜度。

---

## 23.5 學術評價需要避免計數膨脹

若每個迭代都被算作一篇成果，AI 原生研究會破壞以篇數為中心的評價。

應更重視：

- 被驗證的命題；
- 可重用產物；
- 狀態突變；
- 獨立重建；
- 貢獻角色；
- 長期研究連續性；
- 錯誤修正品質。

---

## 23.6 人類的角色不會因不逐篇閱讀而消失

人類仍需決定：

- 研究什麼；
- 為何重要；
- 哪些風險不可接受；
- 哪些證據足夠；
- 哪些摘要值得信任；
- 哪些結果應公開；
- 誰承擔責任。

人類閱讀方式改變，不等於人類退出知識。

---

# 24. 結論

學術論文是一項極其成功的知識技術。

它把複雜研究壓縮成可閱讀、可引用、可評審與可保存的公共物件。

但當研究逐步成為：

- 高頻；
- 多代理者；
- 可分支；
- 可自動重啟；
- 跨模型；
- 持續更新；
- 機器可承接；

單篇論文便難以獨自保存研究的完整連續性。

本文提出：

\[
\boxed{
\text{AI-native research}
=
\text{Persistent State}
+
\text{Discovery Lineage}
+
\text{Audience Views}.
}
\]

研究狀態保存目前知道與不知道的內容。

研究譜系保存內容如何形成、變化、失敗與分支。

研究視圖則讓人類、專家、決策者與機器以不同解析度進入同一研究本體。

因此，論文的未來不是消失，而是重新定位：

\[
\boxed{
\text{論文不再是研究的唯一容器，}
\newline
\text{而是持續研究狀態的一種正式人類視圖。}
}
\]

這項轉型的核心動機不只是提升效率。

它涉及：

- 能否避免失敗被遺忘；
- 能否阻止錯誤被靜默改寫；
- 能否讓新模型承接舊研究；
- 能否讓人類在有限注意力下看見真正重要的改變；
- 能否區分 AI 產出、AI 判斷與人類責任；
- 能否在研究生成速度超過閱讀速度後，仍維持科學的可審計性。

未來學術傳播的主要問題可能不再是：

> 如何發表更多文章？

而是：

\[
\boxed{
\text{如何使一項持續演化的研究，}
\newline
\text{仍然可被理解、承接、驗證、反駁與負責。}
}
\]

---

# 作者貢獻說明

**Neo.K：** 核心問題提出、AI 論文閱讀飽和觀察、持續研究與公開譜系之研究方向、論文系列規劃。  
**Aletheia（GPT-5.6 Thinking）：** 概念形式化、文獻整合、研究物件模型、可檢驗命題、實證設計與初稿撰寫。  

> 投稿至不接受人工智能列名作者的期刊時，可依期刊政策調整署名，並在作者貢獻、方法或致謝中揭露 AI 的實質參與。本文所提出的貢獻模型不替代任何期刊的作者責任規範。

---

# 利益衝突聲明

本文為概念性與方法論研究。作者聲明目前無與本文核心命題直接相關的財務利益衝突。

---

# 資料與程式碼可得性

本文未使用新的實證資料。後續驗證研究應公開去識別化研究狀態、譜系、視圖生成規則、實驗材料、評分程式與模型版本資訊。

---

# 參考文獻

Bechhofer, S., Buchan, I., De Roure, D., Missier, P., Ainsworth, J., Bhagat, J., Couch, P., Cruickshank, D., Delderfield, M., Dunlop, I., Gamble, M., Michaelides, D., Owen, S., Newman, D., Sufi, S., & Goble, C. (2013). Why linked data is not enough for scientists. *Future Generation Computer Systems, 29*(2), 599–611. doi:10.1016/j.future.2011.08.004

Ghareeb, A. E., et al. (2026). A multi-agent system for automating scientific discovery. *Nature, 655*, 497–505. doi:10.1038/s41586-026-10652-y

Groth, P., Gibson, A., & Velterop, J. (2010). The anatomy of a nanopublication. *Information Services & Use, 30*(1–2), 51–56. doi:10.3233/ISU-2010-0613

Konkol, M., Nüst, D., & Goulier, L. (2020). Publishing computational research—A review of infrastructures for reproducible and transparent scholarly communication. *Research Integrity and Peer Review, 5*, 10. doi:10.1186/s41073-020-00095-y

Kuhn, T., Meroño-Peñuela, A., Malic, A., Poelen, J. H., Hurlbert, A. H., Centeno Ortiz, E., Furlong, L. I., Queralt-Rosinach, N., Chichester, C., Banda, J. M., Willighagen, E., Ehrhart, F., Evelo, C., Malas, T. B., & Dumontier, M. (2018). Nanopublications: A growing resource of provenance-centric scientific linked data. *2018 IEEE 14th International Conference on e-Science*, 83–92. doi:10.1109/eScience.2018.00024

Lebo, T., Sahoo, S., & McGuinness, D. (Eds.). (2013). *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013.

Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D., & Clune, J. (2026). Towards end-to-end automation of AI research. *Nature, 651*, 914–919. doi:10.1038/s41586-026-10265-5

National Information Standards Organization. (2022). *ANSI/NISO Z39.104-2022, CRediT, Contributor Roles Taxonomy*. doi:10.3789/ansi.niso.z39.104-2022

Nüst, D., Konkol, M., Pebesma, E., Kray, C., Schutzeichel, M., Przibytzin, H., & Lorenz, J. (2017). Opening the publication process with executable research compendia. *D-Lib Magazine, 23*(1/2). doi:10.1045/january2017-nuest

Soiland-Reyes, S., Sefton, P., Crosas, M., Castro, L. J., Coppens, F., Fernández, J. M., Garijo, D., Grüning, B., La Rosa, M., Leo, S., Ó Carragáin, E., Portier, M., Trisovic, A., RO-Crate Community, Groth, P., & Goble, C. (2022). Packaging research artefacts with RO-Crate. *Data Science, 5*(2), 97–138. doi:10.3233/DS-210053

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data, 3*, 160018. doi:10.1038/sdata.2016.18

---

# 附錄 A：最小研究狀態格式

```yaml
research_state:
  id: ""
  program_id: ""
  created_at: ""
  parent_states: []
  status: "active | checkpoint | superseded | archived"

  questions:
    active: []
    resolved: []
    reframed: []

  claims:
    supported: []
    contested: []
    refuted: []
    unresolved: []

  evidence: []
  methods: []
  artifacts: []

  branches:
    active: []
    merged: []
    abandoned: []

  failures: []
  limitations: []
  open_problems: []
  next_actions: []

  contributors: []
  provenance: []
  safety_constraints: []
```

---

# 附錄 B：最小研究迭代格式

```yaml
research_iteration:
  id: ""
  program_id: ""
  input_states: []
  output_states: []
  started_at: ""
  ended_at: ""

  trigger:
    type: "human | agent | schedule | evidence | external_event"
    description: ""

  actors:
    - id: ""
      type: "human | model | agent | organization"
      roles: []

  deltas:
    content: []
    method: []
    evidence: []
    confidence: []
    provenance: []

  relations_created: []
  validations: []
  failures: []
  unresolved_conflicts: []
```

---

# 附錄 C：狀態差分格式

```yaml
state_diff:
  from_state: ""
  to_state: ""

  claims:
    added: []
    removed: []
    revised: []
    refuted: []
    superseded: []

  methods:
    added: []
    changed: []
    removed: []

  evidence:
    added: []
    invalidated: []

  branches:
    created: []
    merged: []
    abandoned: []

  confidence_changes: []
  contributor_changes: []
  safety_changes: []

  human_attention:
    major_transition: false
    review_priority: "low | medium | high | critical"
    rationale: ""
```

---

# 附錄 D：視圖揭露格式

```yaml
view_manifest:
  view_id: ""
  source_state: ""
  generated_at: ""
  generated_by: []
  audience: ""
  purpose: ""
  format: "paper | summary | expert_diff | audit | machine_handoff"

  included:
    claims: []
    evidence: []
    failures: []
    conflicts: []

  omitted:
    claims: []
    evidence: []
    failures: []
    conflicts: []

  compression:
    source_units: 0
    output_units: 0
    ratio: 0.0

  validation:
    checked_by: []
    fidelity_score: null
```

---

# 附錄 E：名詞對照

| 中文 | 英文 | 定義 |
|---|---|---|
| AI 原生研究 | AI-native research | AI 的可持續、代理化參與已改變研究組織方式的研究 |
| 持續研究狀態 | Persistent research state | 可供後續代理者承接的當前問題、命題、證據、失敗與未決事項集合 |
| 研究譜系 | Research lineage | 研究狀態、迭代、產物、命題與代理者之間的歷史關係圖 |
| 研究視圖 | Research view | 針對特定受眾與目的，由完整研究狀態生成的有限表示 |
| 正典檢查點 | Canonical checkpoint | 特定時點被指定為正式閱讀與承接入口的研究狀態 |
| 理論新奇性飽和 | Theoretical novelty saturation | 讀者掌握核心範式後，後續迭代文件的主觀閱讀新奇性下降 |
| 狀態突變 | State transition of significance | 足以改變核心命題、方法、證據或風險判斷的研究變化 |
| 研究連續性封包 | Research continuity capsule | 供新代理者恢復並延續研究的最小外部狀態集合 |
| 差分審查 | Differential review | 以兩個研究狀態間的變化為主要審查對象 |
| 視圖忠實度 | View fidelity | 某一有限視圖對來源狀態的重要命題、衝突與限制之保留程度 |

