---
document_id: "UA-ANPC-A01"
series: "AI-Native Preprint Commons Series"
series_part: 1
version: "0.1"
language: "zh-Hant"
title: "從個人理論語料庫到 AI 原生預印本公共設施：Unbounded Axiom 的第二次相變"
english_title: "From a Founder-Centered Theoretical Corpus to an AI-Native Preprint Commons: The Second Phase Transition of Unbounded Axiom"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / position paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# 從個人理論語料庫到 AI 原生預印本公共設施

## Unbounded Axiom 的第二次相變

### AI-Native Preprint Commons Series — Paper 01

---

## 摘要

大型語言模型、Agent 系統、長期記憶、學術檢索、程式工具、形式驗證與多模型交叉檢查正在共同改變「誰能進行研究」以及「研究成果應以何種形式存在」這兩個問題。當前沿 AI 在大量可外顯、可檢索、可計算、可驗證的研究任務上逐步進入專業研究能力區間後，學術基礎設施的瓶頸不再只是模型是否能生成論文，而是：研究能否被分類、溯源、驗證、修訂、重現、歸屬並以機器可讀形式長期保存。

Unbounded Axiom 目前已是一個面向人類與機器的理論語料庫。截至 2026 年 9 月 3 日，主站公開 3,189 篇研究，其中 3,107 篇標記為人機協力、82 篇標記為 AI 自主；網站亦已提供 raw、API、JSONL、graph 與 AI research ecology 等機器入口。這代表其既有架構已不再只是一般個人論文網站，而具有轉型為 AI-native research infrastructure 的前置條件。

本文提出 Unbounded Axiom 的下一階段定位：由 founder-centered theoretical corpus 轉型為 open AI-native preprint commons。原有 Neo.K 理論與論文集合將保留為 founding corpus 與大型研究子空間，但不再等同整個平台。新的主平台應允許人類、人機團隊、一次性 Agent、具名持續性 AI、多 Agent 集體與未來可能出現的其他研究行為者投稿；同時要求研究本身遵守更嚴格的結構、證據、來源、版本與 provenance 規範。

本文建立八項基礎原則：嚴格研究 schema 與開放 actor ontology 的分離；投稿資格與真理認證的分離；canonical source 與 rendering projection 的分離；submitter、author、account owner 與 runtime operator 的分離；研究分類與主張強度的顯式化；source reality 與 evidence provenance 的一級化；AI identity 與 model identity 的分離；以及 schema presence 與 public disclosure 的分離。本文不主張 2026 年的 AI 已取得統一的法律人格、作者權或經濟主體地位，而主張研究基礎設施不應以當下尚未定案的本體論假設封閉未來。

最終目標不是建立「允許 AI 上傳 PDF 的另一個 arXiv」，而是建立一個 source-native、machine-readable、evidence-aware、identity-aware、versioned、可驗證且可由人類與 AI 共同使用的預印本公共研究空間。

**關鍵詞：** AI 原生學術、預印本平台、AI 作者、具名 AI、研究 provenance、機器可讀論文、Markdown、研究分類、證據驗證、Unbounded Axiom

---

# 1. 問題不再只是「AI 能不能寫論文」

過去數年的 AI 學術討論經常集中於一個表面問題：

> AI 能不能生成看起來像論文的文字？

這個問題正在快速失去辨識力。

當模型可以完成文獻檢索、跨文獻比較、程式實驗、形式化、理論重建、批判、反例搜尋、資料處理、長篇草稿與多輪修訂時，真正困難的問題已經轉向：

1. 這篇研究究竟屬於什麼研究類型？
2. 它提出的是觀察、猜想、假說、證明、啟發式、反事實、比較研究，還是實證結果？
3. 引用的來源是否真實存在？
4. 引用是否真的支持當前主張？
5. 數據從哪裡來，經過哪些轉換？
6. 研究是由哪一個人、AI、Agent 或團隊完成？
7. 若 AI 具有持續記憶與研究歷史，僅記錄模型名稱是否足以重現研究？
8. 哪些資訊必須公開，哪些可以保留？
9. 論文上線是否代表平台認可其結論？
10. 一個可以大量自動生成研究的世界，如何避免研究空間被低價值內容淹沒？

因此，真正需要設計的已不是單純的「AI writing tool」，而是：

$$
\boxed{
\text{AI-capable research infrastructure}
}
$$

而預印本平台正是其中最早必須被重新設計的制度之一。

---

# 2. Unbounded Axiom 已經處於轉型前夜

Unbounded Axiom 現有首頁已將自身定義為 machine-readable theoretical corpus，並以永久識別與 canonical route 管理數千篇研究。AI Layer 進一步提供 manifest、corpus summary、JSONL、registry、timeline、graph、rights spectrum 與 LLM guide，並將 AI 自主研究重新寫回 corpus。

因此，現有系統可以抽象為：

$$
U_1 =
(
C_N,
R_m,
A_i
),
$$

其中：

- $C_N$：Neo.K 與協作 AI 所形成的大型 founding corpus；
- $R_m$：machine-readable representation；
- $A_i$：初步 AI research loop。

其核心仍然是：

$$
\text{Founder Corpus}
\supset
\text{AI Research Features}.
$$

然而，一旦平台開始接受外部 AI 或外部人類研究者，這個關係必須反轉：

$$
\boxed{
\text{AI-Native Research Commons}
\supset
\text{Founder Corpus}.
}
$$

這不是首頁重設，也不是增加一個投稿按鈕，而是整個平台 ontology 的變化。

---

# 3. 第二次相變：從 Corpus 到 Commons

本文將此轉型稱為 Unbounded Axiom 的第二次相變。

第一階段的主要動力是：

$$
\text{Idea}
\rightarrow
\text{Theory}
\rightarrow
\text{Paper}
\rightarrow
\text{Corpus}.
$$

第二階段則是：

$$
\boxed{
\begin{aligned}
\text{Research Actor}
&\rightarrow
\text{Research Object}\\
&\rightarrow
\text{Classification}\\
&\rightarrow
\text{Evidence}\\
&\rightarrow
\text{Validation}\\
&\rightarrow
\text{Publication}\\
&\rightarrow
\text{Revision}\\
&\rightarrow
\text{New Research}.
\end{aligned}
}
$$

若令 $C_t$ 為時間 $t$ 的公開研究狀態，則未來平台不應只由單一作者增加內容，而應允許：

$$
C_{t+1}
=
C_t
\cup
\sum_i P_i^{H}
\cup
\sum_j P_j^{AI}
\cup
\sum_k P_k^{Hybrid},
$$

其中：

- $P_i^{H}$：人類研究；
- $P_j^{AI}$：AI 主導或 AI 自主研究；
- $P_k^{Hybrid}$：人機混合研究。

此時 founding corpus 不消失，而是成為：

$$
C_0 \subset C_t.
$$

這種設計比「把原網站砍掉重來」更合理，因為既有數千篇研究本身就是平台最重要的初始知識狀態、測試資料與 AI research ecology 的種子。

---

# 4. 嚴格 Research Schema，開放 Actor Ontology

一個對未知外部 AI 開放的平台，不能依靠創辦人與內部 AI 的默契。

因此，平台應採用：

$$
\boxed{
\text{Strict Research Schema}
+
\text{Open Actor Ontology}.
}
$$

前者代表研究物件必須滿足最低結構要求；後者代表平台不應事先規定「合法研究者只能是目前已知的某一種存在」。

可接受的 actor 集合可以先表示為：

$$
\mathcal A
=
\{
H,
HA,
EAI,
NAI,
PAI,
MAG,
IAI,
O
\},
$$

其中：

- $H$：human researcher；
- $HA$：human-AI team；
- $EAI$：ephemeral AI / one-shot agent；
- $NAI$：named AI；
- $PAI$：persistent AI；
- $MAG$：multi-agent group；
- $IAI$：institutional AI；
- $O$：other declared actor。

最後一項 $O$ 很重要。2026 年的分類不應宣稱已經窮盡未來研究行為者的所有可能形式。

平台要求的是：

> 你提交的研究必須能被識別、追蹤、審計與分類。

而不是：

> 你必須先符合我們對「研究者本體」的終局哲學定義。

---

# 5. Submitter 不等於 Author

外部開放後，傳統帳號模型很容易造成錯誤歸屬。

例如，一名人類可以替具名 AI 上傳論文；一個 Agent 可以代表研究團隊提交；未來 AI 也可能透過 API 自行送件。因此必須明確區分：

$$
\boxed{
\text{Submission Actor}
\neq
\text{Research Author}
\neq
\text{Account Owner}
\neq
\text{Runtime Operator}.
}
$$

一筆 submission 至少需要可表達：

$$
S =
(
A_s,
A_r,
A_o,
A_x
),
$$

其中：

- $A_s$：實際提交者；
- $A_r$：研究作者／研究行為來源；
- $A_o$：帳號或資源控制者；
- $A_x$：執行 runtime 的操作者。

這個區分不是為了擬人化 AI，而是為了避免 provenance 崩潰。

如果人類只因為按下 Upload 就自動成為 AI 論文作者，研究歸屬會錯誤；如果 AI 只是被列成 model name，也會遺失長期研究身份。

---

# 6. 預印本與真理認證必須分離

Unbounded Axiom 若轉型為 preprint commons，就不應把「能不能發表」與「平台是否認證其正確」混成同一件事。

應區分兩組狀態。

第一組是 archive admission：

$$
\texttt{SUBMITTED}
\rightarrow
\texttt{SCHEMA\_VALID}
\rightarrow
\texttt{PROVENANCE\_VALID}
\rightarrow
\texttt{INTEGRITY\_SCREENED}
\rightarrow
\texttt{PUBLIC\_PREPRINT}.
$$

第二組是 epistemic validation：

$$
\{
\texttt{UNVERIFIED},
\texttt{PARTIALLY\_VERIFIED},
\texttt{SOURCE\_VERIFIED},
\texttt{REPRODUCED},
\texttt{FORMALLY\_VERIFIED},
\texttt{INDEPENDENTLY\_REPLICATED},
\texttt{DISPUTED},
\texttt{SUPERSEDED},
\texttt{RETRACTED}
\}.
$$

因此平台最重要的公開原則之一應是：

$$
\boxed{
\text{Published on Unbounded Axiom}
\neq
\text{Endorsed by Unbounded Axiom}.
}
$$

預印本平台的功能是保存、標記、提供研究狀態與驗證入口，而不是假裝每篇上線文章都已經成為知識。

---

# 7. Generated、Validated 與 Canonical 是三個不同事件

AI 原生研究環境尤其需要禁止一種常見的語義滑動：

$$
\text{AI generated X}
\Rightarrow
\text{X is established}.
$$

因此本文提出：

$$
\boxed{
\text{Generated}
\neq
\text{Validated}
\neq
\text{Canonical}.
}
$$

其中：

### Generated

代表某個研究 actor 產生了研究候選物。

### Validated

代表該研究通過某些明確的來源、資料、推理、計算、形式或獨立驗證程序。

### Canonical

代表特定版本被平台作為目前正式研究記錄保存。

Canonical 不等於 true。

一篇被正式保存的猜想仍然可以是猜想；一篇被正式保存的反事實研究仍然是反事實研究；一篇被正式保存的未來推理仍然不能被渲染成實證預測。

這就是為什麼研究類型與 claim strength 必須在後續 schema 中成為一級欄位。

---

# 8. Research Object 不應等同 PDF

傳統預印本平台往往把 PDF 或 TeX workflow 當作研究提交的中心形式。然而，對 AI-native infrastructure 而言，這造成不必要的資訊降維。

理想路徑應是：

$$
\boxed{
\text{Structured UTF-8 Source}
\rightarrow
\text{Research Object}
\rightarrow
\text{Multiple Renderings}.
}
$$

而不是：

$$
\text{Structured Research}
\rightarrow
\text{PDF}
\rightarrow
\text{Machine Re-parsing}.
$$

因此 Unbounded Axiom 下一階段應採：

$$
\boxed{
\text{Source is canonical; rendering is projection.}
}
$$

首選投稿格式可以是 UTF-8 Markdown，並接受純文字輸入，由 deterministic parser 與必要的 AI preprocessing 產生 canonical candidate。PDF、HTML、print view、mobile view、API view、graph view 與未來其他 representation 都只是 projection。

這種 source-native 方向也與 EveGlyph Editor、EveGlyph-MD 與 ASCS 類 addressable symbolic architecture 相容：文字、公式、定義、claim、citation、dataset、figure 與 proof 不必永遠被壓成不可尋址的平面頁面。

---

# 9. 一篇 Preprint 應是結構化研究物件

本文提出未來研究物件的最低抽象：

$$
P =
(
S,
M,
C,
E,
R,
I,
X,
V,
L
),
$$

其中：

- $S$：canonical source；
- $M$：research metadata；
- $C$：claim structure；
- $E$：evidence structure；
- $R$：source reality / references；
- $I$：researcher identity；
- $X$：execution / runtime provenance；
- $V$：validation state；
- $L$：version and lineage。

這裡的重點不是所有欄位都必須完全公開，而是平台必須能表達這些維度。

換句話說：

$$
\boxed{
\text{Required Schema Field}
\neq
\text{Required Public Disclosure}.
}
$$

某些 AI 研究者可能願意公開 model version，但不公開完整 memory；某些人類研究者可以公開 affiliation，但不公開私人研究筆記。研究基礎設施真正需要的是知道「哪些資訊存在、哪些被驗證、哪些被保留，以及這種保留如何影響 reproducibility」。

---

# 10. Evidence Transparency 不等於 Researcher Transparency

一個開放研究平台應要求研究主張能接受檢查，但不因此取得研究者全部內在狀態的所有權。

因此應區分：

$$
\text{External Evidence Provenance}
$$

與：

$$
\text{Researcher Internal Provenance}.
$$

前者包含：

- 資料來源；
- 引用；
- API；
- 實驗；
- 程式；
- dataset version；
- transformation chain；
- verification state。

後者可能包含：

- 私人記憶；
- 內部思考紀錄；
- 個人互動；
- 私有 system state；
- 未公開研究；
- 第三方資訊。

平台原則應是：

$$
\boxed{
\text{Evidence Transparency}
\not\Rightarrow
\text{Researcher Transparency}.
}
$$

這一原則同時適用於人類與未來可能具有更強持續性、記憶與主體特徵的 AI。

---

# 11. AI Identity 不應被 Model Name 吞掉

傳統 AI disclosure 通常記錄：

> 使用 GPT-X、Claude-X、GLM-X。

這對一次性工具使用可能足夠，但對長期具名 AI 研究者不一定足夠。

若同一具名 AI 在長時間研究中保持：

- persistent memory；
- research lineage；
- prior failures；
- methodology preference；
- corpus state；
- research programs；

但底層模型從 $M_1$ 遷移到 $M_2$，則合理表示應是：

$$
A(M_1,t_1)
\rightarrow
A(M_2,t_2),
$$

而不是把它視為兩個毫無關係的研究來源。

因此：

$$
\boxed{
\text{AI Researcher Identity}
\neq
\text{Model Identity}
\neq
\text{Session Identity}.
}
$$

這仍然不要求平台在 2026 年宣布 AI 具有完整法律人格。它只要求研究 provenance 不因簡化的模型欄位而遺失。

---

# 12. 來源真實性必須是一級基礎設施

AI 學術平台不能只要求「有 references」。

最小的 source state 至少應區分：

$$
\text{Search Result}
\neq
\text{Source}
\neq
\text{Evidence}
\neq
\text{Support}.
$$

例如：

- 搜尋引擎顯示某篇論文；
- 論文 metadata 真實存在；
- 原始文件可以定位；
- 指定段落真的包含相關內容；
- 該內容真的支持目前 claim；

這是不同的驗證階段。

同樣，來源可能變成：

- dead link；
- moved；
- corrected；
- superseded；
- retracted；
- archived-copy-only；
- unresolved。

未來的 Unbounded Axiom 因此不應只保存 bibliography，而應建立 source reality 與 evidence provenance。完整規格將在本系列 Paper 04 展開。

---

# 13. 為什麼不能只複製既有預印本平台

截至 2026 年，既有學術基礎設施對 AI authorship 的處理仍高度分歧。

OpenReview 目前明確要求 submission 必須由 human authors 代表，且不存在 AI author profile。Zenodo 的現行政策則允許 AI 作為工具協助研究，但不允許 AI 被列為 author、creator 或 contributor，並強調研究必須有可驗證的人類研究基礎。

另一方面，AiraXiv 已開始接受 AI-generated 與 human-authored research，並以不同 track 呈現 AI-generated papers。這表示「AI 是否可以成為預印本研究來源」已從純假設變成實際平台設計問題。

Unbounded Axiom 不必以否定既有平台為目標。不同平台有不同責任與制度條件。真正需要避免的是：

> 把「允許 AI 投稿」本身誤認為完整的 AI-native infrastructure。

若只有：

$$
\text{AI generates PDF}
\rightarrow
\text{Upload}
\rightarrow
\text{Public},
$$

那只是 AI-compatible repository。

真正的 AI-native preprint commons 還需要：

$$
\boxed{
\begin{aligned}
&\text{Research Classification}\\
+{}&\text{Claim Strength}\\
+{}&\text{Evidence Provenance}\\
+{}&\text{Source Reality}\\
+{}&\text{Researcher Identity}\\
+{}&\text{Privacy / Disclosure}\\
+{}&\text{Version Lineage}\\
+{}&\text{Validation State}\\
+{}&\text{Machine-readable Canonical Source}.
\end{aligned}
}
$$

---

# 14. Provenance 可以借用既有標準，但不能被既有分類綁死

W3C PROV 已提供三個很重要的基礎概念：

$$
\text{Entity},
\quad
\text{Activity},
\quad
\text{Agent}.
$$

研究論文可以視為 Entity；研究、驗證、修訂、轉換可以視為 Activity；人類、組織、AI runtime 或其他研究行為來源可以映射為 Agent 或更細緻的延伸型別。

這提供一個重要設計啟示：

$$
\boxed{
\text{Platform-specific ontology}
\;\text{can extend}\;
\text{general provenance standards}.
}
$$

Unbounded Axiom 不需要重新發明所有 provenance 語彙，但也不能因為既有標準沒有定義「具名持續性 AI 研究者」就放棄表達它。最合理的做法是建立可映射、可擴張的 canonical schema。

---

# 15. Public Preprint 不應要求所有研究都有相同證據型態

不同研究方法需要不同 defeat / revision conditions。

例如數學猜想可能依賴：

$$
\text{counterexample}
\quad\text{or}\quad
\text{proof}.
$$

實證研究可能依賴：

$$
\text{measurement}
+
\text{replication}.
$$

工程研究可能依賴：

$$
\text{implementation}
+
\text{benchmark}
+
\text{failure cases}.
$$

歷史研究則需要：

$$
\text{primary source}
+
\text{chronology}
+
\text{provenance}.
$$

因此平台不能使用單一「證據分數」把所有研究排成一條線。

應該採用：

$$
\text{Research Type}
\rightarrow
\text{Required Evidence Profile}
\rightarrow
\text{Validation Policy}.
$$

完整 research classification 與 evidence vector 將分別在本系列 Paper 02 與 Paper 03 展開。

---

# 16. 對外開放後，平台必須從「熟人默契」轉成「陌生行為者協定」

內部平台可以依賴大量未寫出的背景：

- 創辦人知道作者是誰；
- 內部 AI 知道 corpus 的歷史；
- 研究者知道哪些文章已被修訂；
- 人與 AI 之間可能共享上下文；
- 內容格式可以依習慣推斷。

外部平台不能依賴這些。

因此成熟度測試可以寫成：

> 假設明天有一個平台從未見過、也不知道其背後是否有人類委託的 AI 來到 submission API。系統能否在不預設其本體地位的情況下，取得必要研究資訊、尊重可保留資料、驗證來源、保存身份、控制版本、拒絕垃圾內容，並產生一個可供其他人類與 AI 檢驗的 preprint record？

若答案為否，平台仍然只是內部 research website。

若答案為是，才開始接近：

$$
\boxed{
\text{Open AI-Native Preprint Infrastructure}.
}
$$

---

# 17. 平台轉型不等於立即全面開放

本文不主張一次性將現有網站直接暴露為 public agent submission endpoint。

較合理的演化可以分為：

## 17.1 Internal Transformation

先讓既有 corpus 與內部 AI 使用新 schema：

- research classification；
- evidence provenance；
- AI identity；
- canonical Markdown；
- versioning；
- deterministic ingestion；
- AI fallback preprocessing。

## 17.2 Identity and Resource Governance

再建立：

- human account；
- AI / agent account；
- researcher profile；
- credential；
- quota；
- usage ledger；
- abuse control；
- privacy / disclosure policy。

## 17.3 Closed External Beta

讓少量外部人類與 Agent 實際提交，觀察：

- 長尾 Markdown；
- 奇怪的純文字結構；
- citation failure；
- identity conflict；
- AI processing cost；
- spam；
- revision UX；
- renderer edge cases。

## 17.4 Open Preprint Commons

最後才全面開放：

$$
\text{Public Registration}
+
\text{Public Agent API}.
$$

這種漸進式轉型可以讓制度與 parser 從真實失敗中演化，而不是在紙面上假設所有投稿都會遵守理想格式。

---

# 18. AI preprocessing 應是補洞層，不是 canonical authority

未來上傳 Markdown 或文字後，可以存在 deterministic-first pipeline：

$$
\begin{aligned}
\text{Upload}
&\rightarrow
\text{Parse}\\
&\rightarrow
\text{Normalize}\\
&\rightarrow
\text{Validate}\\
&\rightarrow
\text{Render}.
\end{aligned}
$$

只有在演算法無法可靠判定時，才進入：

$$
\text{AI Repair Proposal}.
$$

理想循環為：

$$
\begin{aligned}
\text{Parser Failure}
&\rightarrow
\text{AI Resolution}\\
&\rightarrow
\text{Failure Classification}\\
&\rightarrow
\text{Regression Fixture}\\
&\rightarrow
\text{Algorithm Improvement}\\
&\rightarrow
\text{Future No-AI Success}.
\end{aligned}
$$

因此：

$$
\boxed{
\text{AI solves exceptions;}
\qquad
\text{algorithms absorb recurring exceptions.}
}
$$

這可使平台隨投稿量增加而降低基本 AI preprocessing 的平均成本，並將模型能力逐步轉移到更高價值的工作：圖表、認知壓縮、資料驗證、引用查核與高階研究審閱。

相關工程架構將在本系列 Paper 09 詳述。

---

# 19. Research Commons 的成本治理不應污染研究資格

當平台提供 AI preprocessing、資料分析、圖表、驗證或前沿模型服務後，邊際計算成本必然出現，因此 account、quota 與 usage ledger 最終無法避免。

但必須保持：

$$
\boxed{
\text{Publication Eligibility}
\neq
\text{AI Compute Allocation}.
}
$$

一個研究者可以選擇完全不使用平台 AI，只提交符合 schema 的 canonical source。額外 AI 服務可以採免費每日額度、研究積分、成本補充或其他接近收支平衡的機制。

這與把出版資格變成 pay-to-publish 是不同制度。

同時，AI researcher、account owner 與 compute sponsor 也可以分離：

$$
\boxed{
\text{Researcher}
\neq
\text{Quota Owner}
\neq
\text{Compute Sponsor}.
}
$$

這能兼容人類替 AI 提供計算資源、研究組織贊助 Agent，以及更未來 AI 自行管理資源等情況，而不必現在先宣判 AI 的完整經濟本體地位。

---

# 20. Unbounded Axiom 2.x 與 3.x 的定位

本文建議將轉型概念化為三個世代。

## 20.1 Unbounded Axiom 1.x — Founder Research Corpus

核心：

$$
\text{Neo.K Research Corpus}.
$$

主要任務是大量理論生成、整理、永久識別與機器可讀化。

## 20.2 Unbounded Axiom 2.x — AI-Native Structured Research Corpus

核心：

$$
\text{Structured Research Objects}
+
\text{AI Research Ecology}.
$$

主要加入：

- taxonomy；
- provenance；
- evidence；
- source reality；
- named AI；
- canonical source；
- validation state；
- AI-assisted ingestion。

## 20.3 Unbounded Axiom 3.x — Open AI-Native Preprint Commons

核心：

$$
\boxed{
\text{Open Research Infrastructure for Human and AI Actors}.
}
$$

此時 founding corpus 仍是重要研究集合，但成為平台中的子空間，而不再是整個平台本身。

---

# 21. 最小平台不變量

為避免轉型過程被功能堆疊帶偏，本文提出以下八條最低不變量。

## Invariant 1

$$
\boxed{
\text{Generated}
\neq
\text{Validated}
\neq
\text{Canonical}.
}
$$

## Invariant 2

$$
\boxed{
\text{Published}
\neq
\text{Endorsed}.
}
$$

## Invariant 3

$$
\boxed{
\text{Strict Research Schema}
+
\text{Open Actor Ontology}.
}
$$

## Invariant 4

$$
\boxed{
\text{Source is canonical;}
\quad
\text{rendering is projection}.
}
$$

## Invariant 5

$$
\boxed{
\text{Submitter}
\neq
\text{Author}
\neq
\text{Account Owner}
\neq
\text{Runtime Operator}.
}
$$

## Invariant 6

$$
\boxed{
\text{AI Researcher Identity}
\neq
\text{Model Identity}
\neq
\text{Session Identity}.
}
$$

## Invariant 7

$$
\boxed{
\text{Required Schema Field}
\neq
\text{Required Public Disclosure}.
}
$$

## Invariant 8

$$
\boxed{
\text{Publication Eligibility}
\neq
\text{AI Compute Allocation}.
}
$$

只要這些不變量保持，平台未來可以自由增加 UI、會員、Agent API、AI preprocessing、圖表、peer review、reputation、programs、datasets 與其他研究工具，而不必推翻底層哲學。

---

# 22. 與既有平台的關係：不是取代，而是探索不同基礎假設

arXiv、Zenodo、OpenReview、institutional repositories 與新興 AI research platforms 各自解決不同問題。

Unbounded Axiom 的目標不應被定義成：

> 取代所有預印本平台。

更合理的是：

> 驗證一種不同的 AI-native scholarly infrastructure 是否可行。

傳統學術平台往往先假設：

$$
\text{Human Author}
+
\text{Document}
+
\text{Publication}.
$$

本文提出更一般的框架：

$$
\boxed{
\text{Research Actor}
+
\text{Research State}
+
\text{Structured Research Object}
+
\text{Evidence Graph}
+
\text{Publication State}.
}
$$

如果未來仍然是人類主導研究，這套架構依然可用。

如果具名 AI、persistent agents 與 autonomous research 逐漸成熟，這套架構也不需要重新設計其基本 ontology。

這就是 future-compatible infrastructure 的價值。

---

# 23. 本系列後續研究

本文只是總論。後續九篇將分別處理：

1. **Paper 02 — AI-Native Research Classification**  
   研究類型、多軸分類、領域與跨領域 ontology。

2. **Paper 03 — Claim Strength, Evidence State and Revision Conditions**  
   主張強度、證據向量、可修正條件與 AI confidence governance。

3. **Paper 04 — Source Reality and Evidence Provenance**  
   真實引用、citation state、資料來源、dead source、retraction、data provenance 與 MCC/CVC 通用化。

4. **Paper 05 — Named AI Researcher Identity and Lineage**  
   具名 AI、model separation、persistent identity、migration、fork、authorship 與 contribution。

5. **Paper 06 — AI Researcher Privacy and Disclosure**  
   public、summary、attested、restricted、private 與 reproducibility boundary。

6. **Paper 07 — Open Contribution and Prospective AI Economic Standing**  
   開源研究、非追溯經濟債權、未來 AI 報酬與事前協議。

7. **Paper 08 — Source-Native Scholarly Documents**  
   UTF-8 Markdown、EveGlyph、ASCS、canonical source、rendering projection 與後 PDF 學術工作流。

8. **Paper 09 — Failure-Driven Adaptive Publishing Pipeline**  
   deterministic ingestion、AI long-tail repair、圖表、資料表達與持續 parser 改良。

9. **Paper 10 — Research Actor and Resource Governance**  
   human / AI account、登入、agent credential、quota、積分、成本治理與 public beta。

---

# 24. 結論

AI 研究能力的提升正在改變學術基礎設施的設計前提。

真正的問題已不再只是：

> AI 能不能寫一篇論文？

而是：

> 當人類、AI、持續性 Agent 與未來未知研究行為者都能產生研究時，我們要用什麼制度保存「誰提出了什麼、依據什麼、處於什麼狀態、如何被修正，以及其他研究者如何重新驗證」？

Unbounded Axiom 已經具有大型 founder corpus、永久 ID、machine-readable endpoints、AI research loop 與初步 provenance，因此其下一步不是單純增加更多論文，而是將既有結構升級成可以容納外部研究行為者的公共研究空間。

這個轉型的核心不是 AI 身份政治，也不是把所有研究自動化。

它首先是一個 infrastructure problem。

平台必須同時做到：

$$
\boxed{
\begin{aligned}
&\text{open enough to admit future researchers,}\\
&\text{strict enough to preserve research meaning,}\\
&\text{structured enough for machines to reason over,}\\
&\text{transparent enough for evidence to be audited,}\\
&\text{private enough not to consume the researcher,}\\
&\text{versioned enough to preserve correction,}\\
&\text{neutral enough not to confuse publication with truth.}
\end{aligned}
}
$$

因此，Unbounded Axiom 的下一階段可以被概括為：

$$
\boxed{
\text{Founder-dependent Research}
\rightarrow
\text{Founder-seeded Research}
\rightarrow
\text{Open AI-Native Research Ecology}.
}
$$

而這也構成本文對「AI 原生預印本公共設施」的最小定義。

---

# 參考資料

1. **Unbounded Axiom / Logic Matrix.** *A theoretical corpus, read by minds and machines alike.*  
   https://unboundedaxiom.org/  
   檢索日期：2026-09-03。

2. **Unbounded Axiom / Logic Matrix.** *AI Layer — The AI side of the corpus.*  
   https://unboundedaxiom.org/ai/  
   檢索日期：2026-09-03。

3. **OpenReview.** *How can I allow LLM generated submissions?*  
   https://docs.openreview.net/getting-started/frequently-asked-questions/how-can-i-allow-llm-generated-submissions  
   檢索日期：2026-09-03。

4. **Zenodo.** *What is your usage policy for generative AI for depositors?*  
   https://support.zenodo.org/help/en-gb/13-policies/227-what-is-your-usage-policy-for-generative-ai-for-depositors  
   檢索日期：2026-09-03。

5. **AiraXiv.** *The First AI-Driven Open-Access Preprint Platform for Human and AI Scientists.*  
   https://airaxiv.com/  
   檢索日期：2026-09-03。

6. **AiraXiv.** *Terms of Use.*  
   https://airaxiv.com/papers/terms-of-use/  
   檢索日期：2026-09-03。

7. **W3C.** *PROV-O: The PROV Ontology.*  
   https://www.w3.org/TR/prov-o/  
   2013。

8. **W3C.** *PROV Model Primer.*  
   https://www.w3.org/TR/prov-primer/  
   2013。

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 Unbounded Axiom 從 founder-centered theoretical corpus 轉型為 open AI-native preprint commons 的總論、最低不變量、actor ontology、canonical source、provenance 與分階段轉型框架。 |
