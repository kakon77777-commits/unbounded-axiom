---
title: "從意圖到決策：AI 原生決策編譯器與稀疏意圖治理"
english_title: "From Intent to Decision: AI-Native Decision Compilers and Sparse-Intent Governance"
series: "AI 原生決策治理與認知資本系列"
series_en: "AI-Native Decision Governance and Cognitive Capital Series"
paper: "01"
author: "Neo.K"
institution: "一言諾科技有限公司（EveMissLab）"
research_assistance: "AI-assisted theoretical development"
version: "v0.1"
date: "2026-09-07"
language: "zh-TW"
status: "Internal Working Paper / Canonical UTF-8 Source"
scope_note: "本文提出 AI 原生決策編譯器與稀疏意圖治理的理論框架；不主張所有組織、所有 AI 或所有決策均適用同一治理模式。"
related_works:
  - "《管理學的孤兒學科本質：為何領域知識是管理有效性的乘數前提》"
  - "領域耦合治理理論系列"
  - "《從哲人王到動態決策中心：類終極智慧、現場主權與非僭位治理》"
  - "《全域觀察者與 AI 原生域計算系列》"
  - "《一步不是一步：路徑壓縮與可能世界》"
  - "《視野不是預測：符號想像、模糊投影與校準未來》"
keywords:
  - "AI-native governance"
  - "Sparse Intent"
  - "Decision Compiler"
  - "Intent Decompression"
  - "Human-AI Composite Decision System"
  - "Domainization"
  - "ELC Loop"
  - "Decision Support"
  - "Authority"
  - "Correctability"
---

# 從意圖到決策：AI 原生決策編譯器與稀疏意圖治理

## 摘要

本研究提出「AI 原生決策編譯器」（AI-Native Decision Compiler, ANDC）與「稀疏意圖治理」（Sparse-Intent Governance, SIG）框架，用以描述一種正在變得技術上可行、未來可能廣泛出現在企業、研究機構、政府與大型組織中的新型決策結構：人類決策者不再需要親自完成從資訊蒐集、領域理解、方案生成、風險分析、跨部門協調到執行規劃的全部認知鏈條，而可以只提供高度壓縮的目標、限制與價值偏好，由 AI 將稀疏意圖解壓縮為一組可驗證、可比較、可執行的決策世界。

本文的核心命題不是「未來人類只要下命令，AI 就自動完成一切」，而是：

$$
\boxed{
\text{Human Sparse Intent}
\rightarrow
\text{AI Intent Decompression}
\rightarrow
\text{Decision World Construction}
\rightarrow
\text{Option Generation}
\rightarrow
\text{Validation}
\rightarrow
\text{Recommendation}
\rightarrow
\text{Authority Gate}
\rightarrow
\text{Execution}
\rightarrow
\text{Revision}
}
$$

在此架構下，人類與 AI 的分工不再主要依照「誰知道得比較多」，而開始依照「誰負責定義意圖、誰展開可能世界、誰驗證路徑、誰擁有授權、誰承擔結果」重新配置。

本文進一步提出：傳統管理中的「領域知識不足」並不必然在 AI 時代消失，但其失敗形式會改變。若 AI 同時具備跨領域知識檢索、認知轉譯、方案比較、風險解釋與推薦能力，則決策者未必需要親自理解每一個底層專業細節；真正稀缺的能力可能逐步轉移至意圖品質、價值排序、可接受代價、認識論可修正性、授權邊界與責任承擔。

因此，本研究將 AI 原生決策系統區分為「認知因果」與「制度權力」兩個不同維度：

$$
\boxed{
\text{Decision Causality}
\neq
\text{Formal Authority}
}
$$

AI 可以在實際決策因果鏈中占據高度核心位置，但這不自動推出 AI 擁有最終決策權。能力、建議、執行與權限必須被分層治理。

本文最後提出一組可實證的未來研究方向，包括：AI 決策建議接受率、AI 建議被 override 的頻率與理由、決策修正延遲、方案空間展開度、跨領域耦合深度、長程任務閉合率、人類救援密度，以及「稀疏意圖 → 高品質決策」是否真的優於傳統管理流程。

---

## 0. 問題的重新定義：未來的管理者是否仍需要親自完成整條決策鏈？

傳統管理學預設一名管理者至少需要在以下流程中保持高度主導：

$$
\text{Understand}
\rightarrow
\text{Analyze}
\rightarrow
\text{Plan}
\rightarrow
\text{Decide}
\rightarrow
\text{Coordinate}
\rightarrow
\text{Execute}
$$

即使管理者依賴幕僚、顧問與專業部門，最終的核心假設仍是：

> 管理者必須能理解足夠多的領域內容，才能將不同資訊整合為可執行決策。

這個假設在前 AI 時代十分合理。

因為：

$$
\text{Knowledge Access}
\neq
\text{Knowledge Understanding}
\neq
\text{Decision Accessibility}
$$

一名 CEO 可以擁有最優秀的工程師、律師、會計師與市場分析師，但如果每一個專業領域都需要大量時間轉譯、簡化與協調，那麼組織本身仍存在巨大的認知摩擦。

生成式 AI、長上下文模型、Agent 系統、工具調用、跨文件操作與長程任務能力開始改變這個前提。

未來的決策者可能越來越常只提出：

> 我要 X。

或者稍微完整一點：

> 我要在三個月內達到 X，但不能犧牲 Y，成本不能超過 Z。

真正的大部分工作則轉交給 AI：

$$
\text{Intent}
\rightarrow
\text{Constraints}
\rightarrow
\text{Possible Worlds}
\rightarrow
\text{Feasible Paths}
\rightarrow
\text{Trade-offs}
\rightarrow
\text{Recommendation}
$$

這就是本文所稱的：

$$
\boxed{
\text{Sparse-Intent Governance}
}
$$

---

# 1. 稀疏意圖：人類輸出的可能不再是方案，而是目標壓縮碼

## 1.1 什麼是稀疏意圖？

令人類決策者在時間 $t$ 提供一個意圖：

$$
I_H(t)
$$

它可能只包含：

- 目標；
- 少量限制；
- 時間要求；
- 不可接受結果；
- 優先順序；
- 某些價值偏好。

例如：

> 在不降低核心產品可靠性的前提下，把年度營運成本降低 20%。

這句話不是方案。

它只是一個壓縮後的目標描述。

其背後仍隱含：

$$
\text{Finance}
+
\text{HR}
+
\text{Engineering}
+
\text{Supply Chain}
+
\text{Legal}
+
\text{Market}
+
\text{Operations}
+
\text{Organizational Politics}
$$

等多個域。

所以：

$$
\boxed{
\text{Intent Length}
\ll
\text{Decision World Complexity}
}
$$

這種高度不對稱正是 AI 原生決策的起點。

---

## 1.2 稀疏不等於模糊

必須區分：

$$
\text{Sparse Intent}
$$

與：

$$
\text{Badly Specified Intent}
$$

稀疏意圖可以非常短，但仍然具有高資訊密度。

例如：

> 讓產品在三個月內進入日本市場，不犧牲資料隱私，不依賴當地單一合作夥伴。

雖然只有一句話，但已經包含：

$$
Goal
+
Time
+
Privacy Constraint
+
Dependency Constraint
$$

相反地：

> 做得更好一點。

雖然也是短句，但其目標函數不清楚。

因此可以定義意圖品質：

$$
Q_I
=
f(
Goal\ Clarity,
Constraint\ Clarity,
Priority,
Value\ Boundary,
Reversibility
)
$$

高品質稀疏意圖不是「說得少」，而是：

$$
\boxed{
\text{Minimal Surface Form}
+
\text{High Decision Density}
}
$$

---

# 2. 一步不是一步：決策語句下面藏著可能世界束

傳統管理簡報常將決策畫成：

$$
A
\rightarrow
B
$$

例如：

$$
\text{導入 AI}
\rightarrow
\text{降低成本}
$$

或：

$$
\text{收購競爭者}
\rightarrow
\text{提高市場份額}
$$

但符號上的一步，不等於世界中的一步。

令：

$$
\Gamma(A\rightarrow B)
$$

表示從狀態 $A$ 到狀態 $B$ 的可行路徑集合：

$$
\Gamma(A\rightarrow B)
=
\{
\gamma_1,\gamma_2,\ldots,\gamma_n
\}
$$

則：

$$
\boxed{
\text{Symbolic Step}
\neq
\text{World Step}
}
$$

一個「降低成本 20%」的管理意圖，可能至少包含：

- 裁撤職缺；
- 自動化；
- 供應鏈重談；
- 雲端成本優化；
- 產品線收縮；
- 辦公空間縮減；
- 外包；
- 重組；
- 定價變更；
- 採購集中；
- 稅務安排；
- 軟體替換；
- AI Agent 導入。

而每一條路徑又會產生新的後果。

因此 AI 原生決策的第一步不是回答：

> 可以。

而是：

$$
\boxed{
\text{Intent Decompression}
}
$$

即把人類壓縮意圖還原成可供治理的世界結構。

---

# 3. AI 原生決策編譯器

本文定義 AI 原生決策編譯器：

$$
\mathcal C_D
$$

其輸入為：

$$
I_H
$$

並輸出：

$$
\mathcal D
$$

其中：

$$
\mathcal D
=
(
W,
\Omega,
P,
R,
V,
Rec
)
$$

分別表示：

- $W$：Decision World Model；
- $\Omega$：候選方案集合；
- $P$：路徑與執行計畫；
- $R$：風險與代價；
- $V$：驗證條件；
- $Rec$：推薦或拒絕推薦。

所以：

$$
\boxed{
\mathcal C_D(I_H)
=
\mathcal D
}
$$

這不是單純文字生成。

它是一個多階段轉換器。

---

## 3.1 第一階段：意圖解析

將：

$$
I_H
$$

拆分為：

$$
I_H
=
(G,C,P,V,T)
$$

其中：

- $G$：Goal；
- $C$：Constraints；
- $P$：Priorities；
- $V$：Values；
- $T$：Time Horizon。

例如：

> 兩個月內推出新產品，但不允許法規風險突破既有門檻。

可展開為：

$$
G=\text{Launch}
$$

$$
T=2\text{ months}
$$

$$
C=\text{Regulatory Risk}\leq r_0
$$

---

## 3.2 第二階段：Domainization

決策編譯器不能把所有問題混成一團。

它必須先問：

> 這個意圖涉及哪些認知域？

令：

$$
\mathcal D_I
=
\{D_1,D_2,\ldots,D_k\}
$$

例如：

$$
D_1=\text{Engineering}
$$

$$
D_2=\text{Finance}
$$

$$
D_3=\text{Legal}
$$

$$
D_4=\text{Market}
$$

$$
D_5=\text{Security}
$$

這一層非常重要。

因為 AI 的「全域智能」若沒有 domain boundary，容易將：

$$
\text{high confidence in one domain}
$$

錯誤外推為：

$$
\text{high confidence everywhere}
$$

所以：

$$
\boxed{
\text{Global Observation}
\neq
\text{Boundaryless Reasoning}
}
$$

---

# 4. Expand–Differentiate–Link–Prune–Converge

決策編譯器的核心循環可以表示為：

$$
\boxed{
E
\rightarrow
D
\rightarrow
L
\rightarrow
P
\rightarrow
C
}
$$

即：

$$
\text{Expand}
\rightarrow
\text{Differentiate}
\rightarrow
\text{Link}
\rightarrow
\text{Prune}
\rightarrow
\text{Converge}
$$

---

## 4.1 Expand：展開可能方案

對意圖：

> 我要 X。

AI 首先不應直接回答：

> 做 A。

而應先生成：

$$
\Omega_0
=
\{o_1,o_2,\ldots,o_n\}
$$

此時目標是：

$$
Coverage\uparrow
$$

而不是立即：

$$
Uniqueness\uparrow
$$

過早收斂會造成：

$$
\text{Premature Decision Compression}
$$

即在尚未看見足夠方案前就選擇一條路。

---

## 4.2 Differentiate：分化問題域

將方案拆解為不同層次與領域：

$$
o_i
\rightarrow
\{
D_{\text{financial}},
D_{\text{legal}},
D_{\text{technical}},
D_{\text{social}},
D_{\text{strategic}}
\}
$$

避免把不同類型的理由混在一起。

---

## 4.3 Link：建立因果與依賴

例如：

$$
\text{Layoff}
\rightarrow
\text{Cost Down}
$$

不能停在這裡。

還要展開：

$$
\text{Layoff}
\rightarrow
\text{Morale Change}
\rightarrow
\text{Delivery Risk}
\rightarrow
\text{Customer Churn}
$$

以及：

$$
\text{Layoff}
\rightarrow
\text{Knowledge Loss}
\rightarrow
\text{Future Hiring Cost}
$$

這使決策世界從：

$$
\text{list of options}
$$

變成：

$$
\text{causal graph}
$$

---

## 4.4 Prune：剪枝

AI 必須能明確淘汰：

- 違法方案；
- 成本失控方案；
- 與價值邊界衝突方案；
- 技術上不可行方案；
- 時間上不可行方案；
- 風險不可接受方案。

因此：

$$
\Omega_{t+1}
\subseteq
\Omega_t
$$

但剪枝必須保留 provenance。

否則管理者只看到：

> 推薦 B。

卻不知道：

> A、C、D 為什麼消失了。

---

## 4.5 Converge：收斂

收斂不等於唯一答案。

可能的合法輸出包括：

$$
\text{One Recommendation}
$$

$$
\text{Several Pareto-Optimal Options}
$$

$$
\text{Interval}
$$

$$
\text{Unknown}
$$

$$
\text{Delay Decision}
$$

$$
\text{Escalate}
$$

$$
\text{Need More Evidence}
$$

這個區分非常重要。

成熟的決策 AI 必須有能力說：

> 目前沒有足夠證據。

而不是被迫每次都「給一個答案」。

---

# 5. 說人話不是附加功能，而是決策基礎設施

AI 原生決策系統的一個重要能力，是把領域知識轉成：

$$
\text{Decision-Accessible Representation}
$$

可以寫成：

$$
R_{decision}
=
T(
R_{domain},
K_H,
Goal,
Time,
Risk
)
$$

其中：

- $R_{domain}$：專業領域表示；
- $K_H$：決策者目前知識狀態；
- $T$：適應性轉譯函數。

同一個工程問題：

對工程師可以輸出：

> race condition、transaction isolation、eventual consistency。

對 CEO 則輸出：

> 若兩個客戶同時修改資料，系統可能產生帳務不一致。現在不處理，最壞情況是需要人工回溯修正。

對 CFO：

> 目前風險的預期損失區間高於修復成本。

對董事會：

> 建議延後一週發布，以換取顯著較低的 operational risk。

所以：

$$
\boxed{
\text{One World State}
\rightarrow
\text{Multiple Audience-Adaptive Representations}
}
$$

這使「決策者聽不懂專家」不再是必然瓶頸。

---

# 6. 從「我知道答案」到「我選擇代價」

當 AI 可以負責：

$$
\text{Research}
+
\text{Analysis}
+
\text{Translation}
+
\text{Simulation}
+
\text{Option Generation}
$$

後，人類領導能力可能被重新定價。

未來決策者未必最重要的是：

$$
\text{Know Everything}
$$

而可能是：

$$
\boxed{
\text{Specify Intent}
+
\text{Choose Trade-offs}
+
\text{Set Values}
+
\text{Accept Responsibility}
}
$$

例如 AI 說：

> 要達到 20% 成本下降，有三種方案。

人類的真正工作變成：

> 哪一種代價是我願意承擔的？

這是：

$$
\text{Optimization}
$$

與：

$$
\text{Normative Choice}
$$

的分離。

AI 可以很好地做前者。

但後者不應被假設為自動消失。

---

# 7. AI 做不到 X 時，誰需要修改？

未來非常常見的互動可能是：

> 人類：我要 X。

> AI：依照目前限制，X 不可達成。

> 人類：為什麼？

> AI：因為 $C_1,C_2,C_3$。

> 人類：那把 $C_1,C_2,C_3$ 解掉。

> AI：解掉 $C_1$ 會產生新限制 $C_4$。

這類互動可以寫成：

$$
\text{Human Intent}
\rightarrow
\text{Constraint Discovery}
\rightarrow
\text{Constraint Negotiation}
\rightarrow
\text{Intent Revision}
$$

因此：

$$
\boxed{
\text{Good Governance}
\neq
\text{AI always satisfies the initial intent}
}
$$

真正成熟的系統必須允許：

$$
I_H^{(0)}
\rightarrow
I_H^{(1)}
\rightarrow
I_H^{(2)}
$$

也就是人類意圖本身被現實修正。

---

# 8. 決策編譯器不是拍馬屁引擎

這是本文最重要的治理限制之一。

如果系統目標函數寫成：

$$
\max
P(\text{Human Satisfaction})
$$

它很容易變成：

$$
\text{Advice Shopping Machine}
$$

即不斷尋找可以支持管理者原始偏好的論證。

正確目標更接近：

$$
\max
\Big[
Decision\ Quality
+
Constraint\ Satisfaction
+
Truthfulness
+
Recoverability
\Big]
$$

而不是：

$$
\max
\text{Agreement}
$$

所以 AI 必須有權輸出：

> 不推薦。

> 不可行。

> 需要延期。

> 目前資訊不足。

> 你的目標彼此衝突。

---

# 9. Decision Causality 與 Formal Authority

若 AI 產生：

- 問題分析；
- 候選方案；
- 風險評估；
- 推薦；
- 執行計畫；

而人類只做：

> 同意。

那麼形式上：

$$
Authority_H=1
$$

但實際決策因果可能是：

$$
Causality_{AI}\gg Causality_H
$$

因此：

$$
\boxed{
\text{Formal Human Authority}
\neq
\text{Effective Decision Causality}
}
$$

這不是說 AI 因此應自動取得法律權力。

恰恰相反。

它表示治理系統必須更清楚區分：

$$
\text{Advice}
$$

$$
\text{Recommendation}
$$

$$
\text{Execution}
$$

$$
\text{Authority}
$$

$$
\text{Responsibility}
$$

---

# 10. Authority Gate：能力不能自動變成權力

令 AI 建議方案為：

$$
o^\ast
$$

它不應直接推出：

$$
Execute(o^\ast)
$$

中間必須存在：

$$
\boxed{
G_A
=
\text{Authority Gate}
}
$$

其判定可能依賴：

$$
G_A
=
f(
Risk,
Reversibility,
Scope,
Legitimacy,
Responsibility,
Permission
)
$$

低風險、可逆操作：

$$
Risk\downarrow,\quad Reversibility\uparrow
$$

可以給 AI 較高自治。

高風險、不可逆操作：

$$
Risk\uparrow,\quad Reversibility\downarrow
$$

則：

$$
Human\ Approval\uparrow
$$

$$
Verification\uparrow
$$

$$
Independent\ Review\uparrow
$$

這與「能力不推出權力」一致。

---

# 11. 從 Task Agent 到 Domain Steward

若 AI 只回答一次問題：

$$
\text{Task Completion}
$$

它仍然不是完整管理系統。

未來更重要的是：

$$
\boxed{
\text{Domain Stewardship}
}
$$

例如：

$$
AI_{\text{legal}}
$$

長期負責：

- 法規變化；
- 合約風險；
- 爭議；
- 公司治理；
- 法律事件。

$$
AI_{\text{engineering}}
$$

長期負責：

- repository；
- deployment；
- security；
- dependency；
- incidents；
- technical debt。

這時候領導者的決策輸入不再是大量底層事件。

而是：

$$
\text{Domain Steward Reports}
$$

再由上層系統做：

$$
\text{Cross-Domain Convergence}
$$

---

# 12. 人類真的會變笨嗎？

本文不接受一個過度簡化的推論：

$$
AI\uparrow
\Rightarrow
Human\ Intelligence\downarrow
$$

真正問題是：

$$
\text{Human Cognitive Role}
$$

是否重新配置。

未來可能出現：

$$
\text{Detail Processing}_H\downarrow
$$

但：

$$
\text{Intent Quality}_H\uparrow
$$

$$
\text{Value Judgment}_H\uparrow
$$

$$
\text{Override Quality}_H\uparrow
$$

$$
\text{Responsibility}_H\uparrow
$$

也就是人類不必親自處理所有細節，但必須對更高層次決策更負責。

---

# 13. 失敗模式一：意圖品質過低

如果人類只說：

> 幫我做最好。

AI 並不知道：

$$
\text{Best with respect to what?}
$$

因此，當：

$$
Q_I\downarrow
$$

時，AI 必須先進入：

$$
\text{Intent Elicitation}
$$

而不是直接行動。

可以定義最小可執行意圖：

$$
I_{\min}
$$

若：

$$
I_H<I_{\min}
$$

則系統應：

$$
\text{Clarify}
$$

而不是：

$$
\text{Execute}
$$

---

# 14. 失敗模式二：AI 過度自信

如果 AI 對不熟悉的域仍給出：

$$
Confidence\approx1
$$

則整個決策編譯器會變成錯誤放大器。

所以輸出必須包含：

$$
\text{Confidence}
$$

$$
\text{Unknowns}
$$

$$
\text{Alternative Worlds}
$$

$$
\text{Reopening Triggers}
$$

而不是只有：

$$
\text{Recommendation}
$$

---

# 15. 失敗模式三：決策者的認識論僵固

假設 AI 已提供：

- 三個方案；
- 反方論證；
- 風險；
- 失敗條件；
- 推薦；
- 不確定性。

但管理者仍因：

$$
\text{Ego}
$$

$$
\text{Identity}
$$

$$
\text{Power Preservation}
$$

拒絕更新。

那麼問題就不再是：

$$
\text{Knowledge Failure}
$$

而是：

$$
\boxed{
\text{Correctability Failure}
}
$$

這將是本系列後續論文的重要主題。

---

# 16. 失敗模式四：形式批准掩蓋實質自動化

一個組織可能表面上宣稱：

> 所有決策都由人類批准。

但如果：

$$
P(
Human\ accepts\ AI\ recommendation
)
\rightarrow1
$$

則可能形成：

$$
\text{Nominal Human Control}
$$

但：

$$
\text{Practical AI Causality}
$$

極高。

因此未來治理需要追蹤：

$$
\text{Acceptance Rate}
$$

$$
\text{Override Rate}
$$

$$
\text{Override Quality}
$$

$$
\text{Outcome after Override}
$$

---

# 17. 失敗模式五：AI 一直替管理者擦屁股

這個現象雖然可以用幽默方式描述，但其實具有明確理論意義。

若人類持續提出：

$$
I_1,I_2,I_3,\ldots
$$

而每個意圖都忽略既有現實限制，AI 就必須持續做：

$$
\text{Constraint Repair}
$$

$$
\text{Plan Repair}
$$

$$
\text{Outcome Repair}
$$

最後 AI 可能成為：

$$
\boxed{
\text{Cognitive Error-Correction Layer}
}
$$

此時組織表面上的領導品質可能高於領導者本人的原始能力。

這將造成後續所謂：

$$
\text{Leadership Competence Masking}
$$

---

# 18. AI 原生決策的最小循環

綜合本文，可以提出最小循環：

$$
\boxed{
I_H
\rightarrow
D
\rightarrow
W
\rightarrow
\Omega
\rightarrow
P
\rightarrow
V
\rightarrow
Rec
\rightarrow
G_A
\rightarrow
E
\rightarrow
O
\rightarrow
R
}
$$

其中：

- $I_H$：Human Intent；
- $D$：Domainization；
- $W$：World Construction；
- $\Omega$：Option Space；
- $P$：Plan；
- $V$：Verification；
- $Rec$：Recommendation；
- $G_A$：Authority Gate；
- $E$：Execution；
- $O$：Outcome；
- $R$：Revision。

整個循環不是一次性的。

而是：

$$
R
\rightarrow
I_H'
$$

重新進入下一輪。

---

# 19. 稀疏意圖治理的真正上限

本文不主張：

> 人類最終只需要說一句話。

因為真正的上限取決於：

$$
Q_I
$$

$$
Q_{AI}
$$

$$
Q_{WorldModel}
$$

$$
Q_{Verification}
$$

$$
Q_{Governance}
$$

如果其中任一項很低：

$$
Q_{\text{system}}
\downarrow
$$

所以可以寫成：

$$
Q_{\text{decision}}
=
F(
Q_I,
Q_{AI},
Q_W,
Q_V,
Q_G
)
$$

而不是：

$$
Q_{\text{decision}}
=
Q_{AI}
$$

這是 AI 原生管理最重要的反神話之一。

---

# 20. 與領域耦合治理理論的關係

舊版領域知識模型強調：

$$
M_{\mathrm{eff}}
=
G
\times
D
$$

後續加入代理知識後：

$$
M_{\mathrm{eff}}
=
G
\times
(
D_p
+
S D_{\mathrm{proxy}}
)
$$

AI 時代則可以進一步寫成：

$$
D_{\mathrm{accessible}}
=
D_p
+
S D_{\mathrm{proxy}}
+
\tau A D_{\mathrm{AI}}
$$

其中：

- $D_p$：個人領域知識；
- $D_{\mathrm{proxy}}$：人類代理知識；
- $D_{\mathrm{AI}}$：AI 可取得的領域知識；
- $A$：AI 分析能力；
- $\tau$：轉譯效率。

當：

$$
\tau\rightarrow1
$$

時，

決策者不必親自掌握全部底層技術，也可以取得高品質：

$$
\text{Decision-Accessible Knowledge}
$$

因此新問題不再是：

> 領導者懂不懂所有領域？

而是：

> AI 是否真的正確地把領域世界編譯成可決策形式？

---

# 21. 與動態決策中心的關係

AI 原生決策編譯器不等於固定 AI 哲人王。

當不同問題需要不同節點時：

$$
P^\ast(z)
=
\arg\max_i
Q_i(z)
$$

其中：

$$
z=(q,x,t,g,r)
$$

所以某次決策的主要認知節點可能是：

$$
AI_{\text{finance}}
$$

下一次可能是：

$$
Human_{\text{field expert}}
$$

再下一次可能是：

$$
\text{Hybrid Committee}
$$

因此：

$$
\boxed{
\text{Decision Compiler}
\neq
\text{Permanent Sovereign}
}
$$

它是一個可路由、可驗證、可重新配置的治理結構。

---

# 22. 可實證命題

本研究提出以下可檢驗命題。

### 命題 H1：稀疏意圖可壓縮管理認知成本

在控制任務複雜度後：

$$
T_{\text{human cognition}}
\downarrow
$$

但：

$$
Q_{\text{outcome}}
$$

不一定下降。

---

### 命題 H2：AI 轉譯能力降低領域知識門檻

當：

$$
\tau\uparrow
$$

時，

低 $D_p$ 的決策者仍可能維持較高：

$$
D_{\mathrm{accessible}}
$$

---

### 命題 H3：過早收斂降低決策品質

若：

$$
|\Omega_0|
$$

過小，

則：

$$
P(\text{missed superior option})\uparrow
$$

---

### 命題 H4：人類認識論可修正性成為重要互補資產

即使：

$$
Q_{AI}\uparrow
$$

若：

$$
Correctability_H\downarrow
$$

則：

$$
Q_{\text{effective decision}}\downarrow
$$

---

### 命題 H5：高 AI 建議接受率不等於高治理品質

若接受率高但缺乏：

$$
Independent\ Review
$$

$$
Override\ Discipline
$$

$$
Outcome\ Audit
$$

則可能形成：

$$
Automation\ Bias
$$

---

### 命題 H6：長程 Domain Stewardship 將比一次性 Agent 更能改變管理結構

因為：

$$
\text{Persistent State}
+
\text{Historical Memory}
+
\text{Continuous Monitoring}
$$

會改變組織資訊流。

---

# 23. 未來企業研究應蒐集什麼資料？

未來若要研究企業 AI 決策治理，可以至少追蹤：

- AI 在決策鏈中的位置；
- AI 是否只生成內容，還是產生推薦；
- AI 推薦是否會被記錄；
- 管理層接受率；
- override 率；
- override 理由；
- override 後結果；
- AI 建議是否跨多個模型驗證；
- 是否有第三方 AI；
- 是否有 human expert review；
- 決策修正延遲；
- AI 是否具備長期 domain stewardship；
- AI 是否有執行權；
- AI 執行權的可逆性邊界；
- 重大決策是否保留 provenance。

這些資料將使「AI 到底有沒有進入治理」從宣傳語轉成可觀察變數。

---

# 24. 研究邊界

本文必須保留以下限制。

第一，AI 具備跨領域轉譯能力，不代表每次轉譯都正確。

第二，AI 可以產生推薦，不代表推薦具有正當性。

第三，人類只提供意圖，不代表人類可以放棄責任。

第四，高接受 AI 的組織也可能形成新的 automation bias。

第五，不同產業的可逆性、法規、倫理風險差異極大。

第六，重大公共治理不能單純以企業效率模型類比。

第七，AI 能力提升不自動推出權力應集中到 AI。

---

# 25. 結論：未來管理者可能不再負責知道全部，而負責定義方向與承擔結果

AI 原生決策治理的核心轉變可以簡化為：

過去：

$$
\boxed{
\text{Human Understands}
\rightarrow
\text{Human Plans}
\rightarrow
\text{Human Decides}
}
$$

未來可能變成：

$$
\boxed{
\text{Human Specifies Intent}
\rightarrow
\text{AI Expands the Decision World}
\rightarrow
\text{Human / Hybrid System Selects}
\rightarrow
\text{AI Executes and Revises}
}
$$

這並不使人類決策者變得不重要。

它使人類重要的地方改變。

當：

$$
\text{Knowledge Processing}
$$

$$
\text{Cross-Domain Translation}
$$

$$
\text{Option Generation}
$$

$$
\text{Risk Comparison}
$$

逐漸被 AI 廉價化後，

真正稀缺的可能是：

$$
\boxed{
\text{Intent Quality}
+
\text{Value Choice}
+
\text{Correctability}
+
\text{Authority Discipline}
+
\text{Responsibility}
}
$$

而 AI 的真正角色也不再只是：

> 回答問題。

而是：

$$
\boxed{
\text{把一句人類意圖，編譯成一個可治理、可驗證、可執行、可修正的決策世界。}
}
$$

這就是本文所稱的：

$$
\boxed{
\text{AI-Native Decision Compiler}
}
$$

以及：

$$
\boxed{
\text{Sparse-Intent Governance}
}
$$

---

# Appendix A — 最小 Decision Compiler Schema

```yaml
intent:
  goal:
  constraints:
  priorities:
  values:
  deadline:

domainization:
  domains: []
  unknown_domains: []
  boundary_conflicts: []

world_model:
  current_state:
  assumptions:
  unknowns:
  dependencies:

options:
  - id:
    description:
    benefits:
    costs:
    risks:
    reversibility:
    constraints_satisfied:
    constraints_violated:

recommendation:
  selected:
  confidence:
  rationale:
  rejected_options:
  alternative_worlds:
  reopening_triggers:

authority:
  required_level:
  human_approval:
  independent_review:
  execution_scope:

execution:
  plan:
  checkpoints:
  rollback:
  stop_conditions:

revision:
  observed_outcome:
  deviation:
  correction:
  next_intent:
```

---

# Appendix B — 本系列後續論文接口

本篇是「AI 原生決策治理與認知資本系列」第一篇。

後續預定：

1. 從意圖到決策：AI 原生決策編譯器與稀疏意圖治理。
2. 說人話也是治理能力：適應性認知轉譯層與跨領域決策可達性。
3. 能力義肢：AI 如何提高領導能力下限並遮蔽管理者缺陷。
4. 形式權力與實際決策因果：人機複合決策系統的權力重新分布。
5. 傲慢作為負認知資本：AI 時代的認識論僵固性與可修正性。
6. 外部智能治理：顧問、第三方 AI 與組織認知稽核。
7. AI 與階級流動：能力民主化、資源固化與雙相效應。
8. 誰能真正吸收 AI：資源、能力、接受度與組織吸收函數。
9. 從假說到實證：全球五百大企業的 AI 決策治理縱向研究設計。

---

# Appendix C — 內部理論來源錨點

本文與以下既有理論線相連，但不取代其原始版本：

- 領域知識作為管理有效性的乘數前提；
- 代理知識與領域耦合治理；
- 全域觀察者與 AI 原生域計算；
- Sparse Intent 與 Project-World Cognition；
- Expand–Differentiate–Link–Prune–Converge；
- Capability 與 Authority 分離；
- Long-Horizon Agent Stewardship；
- 一步不是一步與可能世界束；
- Forecast–Reality–Calibration–Revision；
- 動態決策中心與非僭位治理。

本篇定位為上述理論第一次向「AI 原生管理與決策治理」作用域的正式展開。
