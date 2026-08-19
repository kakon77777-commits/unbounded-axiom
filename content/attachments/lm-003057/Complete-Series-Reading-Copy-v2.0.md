# 邏輯空間積分與證明空間動力學 — Expanded v2.0 Complete Series
## Logic-Space Integration and Proof-Space Dynamics
**Complete 12-paper canonical Markdown compilation**  
**Date:** 2026-08-17

---



<!-- BEGIN LSI-PSD-01 -->

# LSI-PSD-01 — 證明空間不是證明：AI 長程數學研究的基本框架

## Proof Space Is Not Proof: A Foundational Framework for Long-Horizon AI Mathematical Research

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 01  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 系列 Charter / 方法論基礎論文  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬數學研究方法論、證明工程、AI 數學研究與科學哲學的理論建模。本文提出的「證明空間」「搜尋制度」「負證明資訊」「局部飽和」等術語，除非明確標記為既有文獻術語，均是本文的操作性研究定義。本文不聲稱已證明、反證或判定 Navier--Stokes existence and smoothness、P vs NP 或其他公開未解問題；亦不把任何 AI 未能找到證明的現象視為原命題錯誤、不可證、不可判定或定義錯置的證明。

---

## 摘要

大型語言模型、形式證明器、程式執行工具、文獻檢索、長程記憶與多智能體協作正在共同改變自動數學研究的基本單位。傳統自動定理證明通常把任務表述為：給定形式命題 $Q$，尋找一個能被驗證器接受的證明物件 $\pi$。然而，當 AI 系統能在數十、數百乃至更多研究輪次中持續提出中間引理、切換表示、建立反例候選、搜尋文獻、執行數值或符號實驗、保存失敗、回收舊結果並協調多條路徑時，單一證明物件已不足以描述實際發生的研究過程。新的對象不是只有最終證明，而是整個可重放的研究軌跡。

本文建立「邏輯空間積分與證明空間動力學」系列的第一層基礎。核心工作有五項。第一，嚴格區分形式可證集合、搜尋制度可達空間、實際被觀測的研究軌跡、已驗證事實圖與未驗證研究記憶，避免把「AI 看過的空間」誤認為「數學上一切可能證明的空間」。第二，定義搜尋制度

$$
R=(\mathcal A,\mathcal L,\mathcal M,\mathcal V,B,\mathcal K,\Sigma),
$$

其中包含公理背景、表示語言、方法族、驗證器、資源界、既有知識與調度策略。第三，提出「證明空間非同一原則」與「搜尋制度非結論原則」：即使某一制度中出現長期失敗、強烈路徑匯流或局部飽和，也不能僅由此推出 $Q$ 為假、原問題定義錯誤、$Q$ 不可證或 $Q$ 相對某形式系統獨立。第四，提出「負證明資訊」的分級框架，說明失敗並非只有零與一兩種狀態；可重現、可審計、跨表示穩定的障礙能成為關於搜尋制度的正面研究資料。第五，將近年的 AI 數學研究進展納入此框架：AlphaProof 顯示形式環境可提供可驗證的強回饋；HERMES、Minimal Agent、LEAP 與 Stepwise 展示迭代修正與 proof-state 搜尋；LeanMarathon 顯示長程形式化的主要瓶頸包括漂移、依賴糾纏與上下文衰退；RMA 將研究級問題分解為文獻、知識庫、證明與驗證模組；Danus 以 fact graph 區分已驗證事實與未驗證記憶；TheoremGraph 則證明細粒度數學依賴圖已可被大規模抽取。另一方面，2026 年關於形式證明對語義保持改寫高度敏感的研究顯示：同一數學內容可因表示不同而有極不相同的證明成功率，因此任何「搜尋耗盡」主張都必須先面對表示商空間問題。

本文最後以 NS-203 長程研究語料作為動機案例。該語料在保守分類後包含 203 份 Navier--Stokes paper-like artifacts，已觀察到大量路徑回訪、跨系列依賴與局部高階採樣訊號，但固定窗口 novelty 檢驗並不支持「整體證明空間已耗盡」的結論。這個負結果恰好體現本文的主張：長程研究資料可以支援對搜尋制度的結構性分析，卻不能越權成為對數學實在的終局判決。

**關鍵詞：** 證明空間、搜尋制度、長程 AI 數學研究、形式證明、負證明資訊、研究軌跡、proof-state graph、fact graph、表示敏感性、局部飽和、認識論防火牆

---

# 1. 問題已經改變：從「給我一個證明」到「這個研究系統究竟做過什麼」

## 1.1 傳統最小模型

自動定理證明最簡潔的形式可以寫成：給定目標命題 $Q$，在某一形式系統 $\mathcal A$ 中尋找證明物件 $\pi$，使驗證器 $\mathcal V$ 接受：

$$
\operatorname{Find}\ \pi
\quad\text{such that}\quad
\mathcal V(\pi,Q;\mathcal A)=1.
$$

若找到 $\pi$，則在該形式系統與驗證規則之下，搜尋任務完成。對於短程 theorem proving benchmark，這個模型非常自然：輸入是一個形式目標，輸出是一個可檢查 proof term 或 tactic script。

但這個模型隱含了一個研究工程上的壓縮：它把所有「沒有進入最後證明的過程」都視為暫時狀態。若系統嘗試了一千條路，最後只有一條進入證明，傳統成功指標往往只保存那一條。

在單次 benchmark 中，這並不一定是問題；在真正長程研究中，卻可能造成大量結構性資訊消失。

## 1.2 長程研究的基本單位不是單一輸出

當 AI 系統具備下列能力時：

- 反覆分解目標；
- 提出與修正中間引理；
- 搜尋文獻與形式庫；
- 調用 CAS、數值實驗、SAT/SMT、Lean、Isabelle 等工具；
- 建立例子與反例候選；
- 對舊路徑做失敗診斷；
- 多智能體平行探索；
- 將已驗證結果保存為共享事實；
- 將未驗證猜想、死路與研究策略保存為記憶；
- 在多輪之後重新進入先前路徑；

則研究過程應寫成事件序列：

$$
\mathcal H_N
=
(e_1,e_2,\ldots,e_N),
$$

其中事件 $e_i$ 可以屬於不同型別：

$$
\operatorname{type}(e_i)
\in
\{
\text{proposal},
\text{proof-step},
\text{verification},
\text{counterexample},
\text{reformulation},
\text{retrieval},
\text{experiment},
\text{no-go},
\text{routing}
\}.
$$

這個 $\mathcal H_N$ 並不是證明本身。它是一個**研究軌跡**。

本文的第一個方法論轉向就是：

$$
\boxed{
\text{proof object}
\neq
\text{research trajectory}.
}
$$

前者回答「結論如何被嚴格推出」；後者回答「研究系統如何探索、失敗、回訪、修正並累積結構」。

## 1.3 近年 AI 數學系統已經逼迫我們做這個區分

AlphaProof 以 Lean 為可驗證環境，透過強化學習尋找正式證明，顯示 proof checker 可以把複雜推理轉化為機器可驗證的回饋訊號。HERMES 進一步把非形式推理與 Lean 中間檢查交錯，並使用記憶維持長多步推理的連續性。Minimal Agent 顯示，即使採取相對簡化的 agentic 架構，只要具備 iterative refinement、library search 與 context management，也能顯著改善單次生成的侷限。LEAP 則以 informal blueprint、問題分解與 Lean compiler feedback 形成反覆修正的工作流。

對更長的研究流程，問題更加明顯。LeanMarathon 直接把「長程 research mathematics autoformalization」的失敗來源描述為 statement drift、dependency tangling、context decay 與 local repair 對遠端工作的破壞，並以 evolving blueprint 作為共同系統紀錄。RMA 把研究級數學拆成問題分析、文獻搜尋、知識庫、候選證明與驗證等模組，再以共享結構記憶協調多輪工作。Danus 更進一步將「已驗證事實」與「研究記憶」分開：驗證通過的事實進入 fact graph，計畫、死路、例子、反例與尚未成立的想法留在 memory。

這些架構雖然目的與驗證強度不同，卻共同指向同一個研究工程事實：

$$
\boxed{
\text{長程數學研究需要保存的不只是答案，還包括狀態、依賴與失敗歷史。}
}
$$

Danus 的一個案例尤其具有方法論意義：系統曾建立數千個 verified facts，而最終只有其中一部分直接支援目標定理。剩餘已驗證事實並不因此自動成為垃圾；它們記錄了搜尋寬度、旁支結論與未進入最終 proof path 的結構。這正是本文所謂「研究軌跡不是證明，但仍可能是數學研究資料」的具體外部例子。

---

# 2. 本文先做一個術語清理：「證明空間」不是一個單一空間

「proof space」如果不加限定，很容易把不同概念混在一起。因此本文不把它當成一個已經完全標準化的數學對象，而是作為一組必須分層定義的操作性術語。

## 2.1 形式證明集合

固定形式系統 $\mathcal A$、目標 $Q$ 與證明語法後，可以定義所有可被系統接受的證明物件集合：

$$
\Pi_{\mathcal A}(Q)
=
\{
\pi:\mathcal V(\pi,Q;\mathcal A)=1
\}.
$$

這是最接近傳統 theorem proving 所關心的對象。

若：

$$
\Pi_{\mathcal A}(Q)\neq\varnothing,
$$

則 $Q$ 在 $\mathcal A$ 中可證。

但在實際 AI 搜尋中，系統通常不會直接列舉 $\Pi_{\mathcal A}(Q)$；它只會沿著某些可生成的 proof state、tactic、自然語言策略或程式操作前進。

## 2.2 制度可達狀態空間

因此定義：

$$
\Omega_R(Q)
$$

為搜尋制度 $R$ 在目標 $Q$ 下可表示、可生成、可辨識或可到達的研究狀態集合。

這裡的 $R$ 不只是模型名稱，而是整個研究制度：

$$
R
=
(
\mathcal A,
\mathcal L,
\mathcal M,
\mathcal V,
B,
\mathcal K,
\Sigma
).
$$

其中：

- $\mathcal A$：公理、邏輯、形式背景與已接受理論；
- $\mathcal L$：允許的自然語言、形式語言、符號表示與中介表徵；
- $\mathcal M$：方法族、tactic、演算法、外部工具與可調用程序；
- $\mathcal V$：驗證器集合，包括形式 kernel、數值檢查、獨立 verifier 或人工 audit；
- $B$：時間、token、記憶、算力、proof depth、worker 數等資源界；
- $\mathcal K$：研究開始時可取得的文獻、資料庫、形式庫與既有結果；
- $\Sigma$：調度、路由、搜尋策略、停止規則與 multi-agent orchestration。

這個定義刻意把「基礎模型能力」降為制度的一個因素，而不是全部。相同模型在不同 $\Sigma$、$\mathcal K$、$\mathcal V$ 與 $B$ 下，可以產生完全不同的可達空間。

## 2.3 實際觀測集合

真正執行 $N$ 輪後，被看見的狀態只是一個有限子集：

$$
\widehat\Omega_{R,N}(Q)
\subseteq
\Omega_R(Q).
$$

因此即使 $\Omega_R(Q)$ 很大，我們實際上通常只有：

$$
\widehat\Omega_{R,N}(Q)
=
\{x_1,x_2,\ldots,x_m\}.
$$

這一層才是真正能從 corpus、log、proof state tree 或 agent trace 中做經驗分析的對象。

## 2.4 已驗證事實子圖

若研究制度把驗證通過的中間結果保存為節點，可得到：

$$
\mathcal F_N
=
(V_N,E_N),
$$

其中每個 $v\in V_N$ 是已驗證 statement，每條 edge 代表邏輯依賴、引用或 proof-use relation。

這類結構接近 Danus 的 fact graph，也與 TheoremGraph 所強調的 statement-level dependency graph 具有方法上的親緣性。

但：

$$
\mathcal F_N
\neq
\widehat\Omega_{R,N}(Q),
$$

因為大量失敗路徑、候選反例、未證猜想與研究策略不一定進入 fact graph。

## 2.5 未驗證研究記憶

定義：

$$
\mathcal U_N
$$

為尚未成為可接受數學事實、但對未來搜尋可能有用的記憶，例如：

- 某條路已試過；
- 某個估計在特定尺度失效；
- 某個反例候選尚未完成；
- 某種表示似乎容易產生 hallucination；
- 某個 lemma 可能需要更強假設；
- 某一 worker 的策略已進入迴圈；
- 某一文獻可能提供工具但尚未核對。

所以完整長程研究狀態至少是：

$$
\boxed{
\mathfrak S_N
=
(
\widehat\Omega_{R,N},
\mathcal F_N,
\mathcal U_N,
\mathcal H_N
).
}
$$

這四者不能互相冒充。

---

# 3. 證明空間非同一原則

## 3.1 原則的形式

本文提出系列的第一個基礎原則。

### 原則 1：證明空間非同一原則

$$
\boxed{
\widehat\Omega_{R,N}(Q)
\subseteq
\Omega_R(Q)
\neq
\Omega_{\mathrm{all}}(Q).
}
$$

其中 $\Omega_{\mathrm{all}}(Q)$ 只是方法論上的上位記號，表示所有未來可能形式化、表示、方法、輔助結構、公理背景與智能制度所可能涉及的研究空間；本文不主張它必然是一個可計算、可測量甚至能在單一集合論框架中被完整構造的對象。

這條原則的核心不是集合論細節，而是一個認識論約束：

> **任何具體 AI 系統看見的證明空間，都只能是相對於制度的證明空間。**

## 3.2 為什麼這不是一句「永遠不能知道」的空話

這條原則並不禁止我們測量 $\widehat\Omega_{R,N}$；相反，它要求所有測量都帶著制度標籤。

例如：

$$
\operatorname{Sat}(Q;R,N)
$$

只能表示「在制度 $R$、執行規模 $N$ 下出現某種飽和訊號」，而不能縮寫成：

$$
\operatorname{Sat}(Q).
$$

也就是說，研究報告應寫：

> 在固定表示策略、方法族、驗證器與資源界下，某些路徑族的新增等價類速率下降。

而不是：

> 這個數學問題的所有可能證明都已被耗盡。

## 3.3 制度標籤必須成為結果的一部分

若兩個系統：

$$
R_1
\neq
R_2,
$$

則即使它們研究同一 $Q$，也完全可能有：

$$
\widehat\Omega_{R_1,N}(Q)
\cap
\widehat\Omega_{R_2,M}(Q)
\ll
\widehat\Omega_{R_1,N}(Q)
\cup
\widehat\Omega_{R_2,M}(Q).
$$

差異可能來自：

- 不同形式語言；
- 不同 theorem library；
- 不同 retrieval；
- 不同 proof tactics；
- 不同 agent memory；
- 不同表示重寫；
- 不同驗證標準；
- 不同 seed 與 sampling policy；
- 不同人類介入。

因此將所有「AI 沒證出來」視為同一事件，本身就是錯誤的資料壓縮。

---

# 4. 搜尋制度非結論原則：最重要的認識論防火牆

## 4.1 從失敗不能推出什麼

假設執行長程研究後：

$$
\operatorname{FailSearch}(Q\mid R,N)=1.
$$

也就是在指定制度與資源內沒有取得可接受的目標證明或反證。

本文要求：

$$
\boxed{
\operatorname{FailSearch}(Q\mid R,N)
\not\Rightarrow
\neg Q.
}
$$

同樣不能推出：

$$
\boxed{
\operatorname{FailSearch}(Q\mid R,N)
\not\Rightarrow
\operatorname{Misframed}(Q).
}
$$

也不能推出：

$$
\boxed{
\operatorname{FailSearch}(Q\mid R,N)
\not\Rightarrow
\operatorname{Independent}_{\mathcal A}(Q).
}
$$

更不能推出：

$$
\boxed{
\operatorname{FailSearch}(Q\mid R,N)
\not\Rightarrow
\operatorname{Unprovable}(Q).
}
$$

## 4.2 為什麼「做了一萬次」仍然不夠

即使：

$$
N=10^4,
$$

只要這 $10^4$ 輪共享相同或高度相近的表示、模型先驗、工具與路由策略，它們可能仍然只是在同一狹窄 basin 內重複採樣。

反過來，即使研究 corpus 顯示極高路徑多樣性，也不能因此確定沒有尚未出現的新表示或新中介理論。

因此：

$$
\boxed{
\text{sample count}
\neq
\text{proof-space completeness}.
}
$$

## 4.3 與 Goedel 不可完備性的距離

本文特別反對一種常見修辭：

> 「我們找了很久都找不到，所以可能是 Goedel 不可判定。」

Goedel 型不可完備性是相對明確形式系統、可有效公理化條件與算術表達能力的元數學結果。若要說某具體命題相對某 $\mathcal A$ 獨立，必須建立相應的獨立性論證；不能把搜尋挫折直接包裝成 incompleteness。

因此，對任何開放問題，本文把以下幾個假說分開：

$$
\begin{aligned}
H_1 &: \mathcal A\vdash Q\ \text{但尚未找到證明},\\
H_2 &: \mathcal A\vdash\neg Q\ \text{但尚未找到反證},\\
H_3 &: \text{目前方法族不足},\\
H_4 &: \text{目前表示語言不足},\\
H_5 &: \text{智能或搜尋深度不足},\\
H_6 &: \text{資源界不足},\\
H_7 &: \text{需要尚未建立的新中介理論},\\
H_8 &: \text{問題表述存在可修正的範疇或語義錯置},\\
H_9 &: Q\ \text{相對某形式系統具有獨立性},\\
H_{10} &: \text{驗證與形式化本身成為瓶頸}.
\end{aligned}
$$

長程搜尋資料可以改變我們對這些候選解釋的研究優先順序，但不能僅憑 recurrence 或 saturation 把其中任何一項升格為定理。

## 4.4 本系列的核心句

$$
\boxed{
\textbf{Saturation is evidence about a search regime, not a verdict on mathematical reality.}
}
$$

中文：

> **飽和是對搜尋制度的證據，不是對數學實在的判決。**

這句話是後續整個系列的認識論防火牆。

---

# 5. 失敗不是反證，但也不是零資訊

## 5.1 兩種錯誤的極端

面對大量失敗，研究者很容易落入兩個相反極端。

極端 A：

$$
\text{沒有最後證明}
\Rightarrow
\text{全部過程都是垃圾}.
$$

極端 B：

$$
\text{失敗很多且反覆}
\Rightarrow
\text{問題本身一定錯}.
$$

本文同時拒絕兩者。

## 5.2 負證明資訊的最小定義

令一個失敗紀錄為：

$$
F_i
=
(
A_i,
R_i,
L_i,
O_i,
V_i
),
$$

其中：

- $A_i$：所用假設；
- $R_i$：研究路徑；
- $L_i$：已取得的中間引理；
- $O_i$：終止障礙；
- $V_i$：驗證狀態。

若 $F_i$ 只是一句「沒成功」，資訊量很低。若它可以說明：

> 在假設 $A_i$ 下，經由路徑 $R_i$，已驗證到 $L_i$，但若要閉合目標必須再取得條件 $C_i$，而目前可證明 $C_i$ 與另一既有條件不相容。

那麼這個失敗已經形成可重用的負資訊。

本文把：

$$
\boxed{
\text{關於已審計失敗區域、路徑或障礙的可重用資訊}
}
$$

稱為 **negative proof information**。

它不是 $\neg Q$ 的證明，而是對：

$$
\widehat\Omega_{R,N}(Q)
$$

中某些區域的結構性記錄。

## 5.3 負證明資訊階梯

為避免把任何失敗都說得過強，本文提出暫定五階：

### $N_0$：未結構化失敗

例如：

- 模型沒有答完；
- proof script 不編譯；
- 文字論證中斷；
- 沒有清楚失敗位置。

這類資訊只能用於 debugging。

### $N_1$：局部可定位失敗

能指出：

$$
\text{goal }G
$$

在 tactic、lemma applicability 或代數步驟上失敗。

形式 proof state 系統通常能大量產生此類資料。

### $N_2$：可審計障礙

多次研究都能抽取同一種 obstruction schema：

$$
O=(A,C,\text{failure mode}).
$$

此時可開始做 clustering 與 route comparison。

### $N_3$：跨路徑穩定障礙

若：

$$
T_1(Q)\leadsto O,
$$

$$
T_2(Q)\leadsto O,
$$

$$
T_3(Q)\leadsto O,
$$

且 $T_1,T_2,T_3$ 在方法或表示上有實質差異，則 $O$ 成為 proof-route confluence 候選。

### $N_4$：跨表示穩定障礙

若對語義保持改寫、不同形式化或不同工具制度，$O$ 仍反覆出現，則它比單一路徑 no-go 更有研究價值。

但即使 $N_4$ 仍不等於：

$$
\mathcal A\vdash\neg Q.
$$

只有當障礙本身被提升為真正形式定理，例如證明某完整方法族不可能滿足閉合條件，才開始進入傳統數學意義的 no-go theorem。

## 5.4 負資訊可以直接改變下一輪搜尋

令研究策略為：

$$
\Sigma_{n+1}
=
U(\Sigma_n,\mathcal F_n,\mathcal U_n).
$$

若 $\mathcal U_n$ 保存高品質負資訊，則下一輪可以：

- 避免重建完全相同的失敗 proof skeleton；
- 將算力轉向尚未審計的 representation；
- 提前檢查已知 obstruction；
- 主動尋找反例；
- 改變 auxiliary object；
- 對同一障礙做高階關係分析。

因此失敗的價值不在於「失敗越多越好」，而在於：

$$
\boxed{
\text{failure}
\xrightarrow{\text{structure + verification}}
\text{reusable constraint}.
}
$$

---

# 6. 表示敏感性：同一數學內容並不等於同一搜尋難度

## 6.1 一個對本系列非常重要的 2026 結果

Olejniczak 等人在 2026 年研究 LLM-based formal theorem provers 對 semantics-preserving rewrites 的敏感性。他們觀察到：數學上等價的 statement，只要交換參數、進行簡單代數改寫或使用不同 notation，證明成功率就可能劇烈變化。

形式上，若：

$$
Q_1\equiv Q_2,
$$

並不保證：

$$
P_R(\operatorname{prove}Q_1)
=
P_R(\operatorname{prove}Q_2).
$$

這意味著 AI theorem prover 的「困難度」部分是 representation-dependent，而不是純粹 mathematical-content-dependent。

## 6.2 對「耗盡」概念的直接衝擊

如果一個系統反覆嘗試 $Q_1$ 的多種相近寫法都失敗，我們仍必須問：

$$
\text{它探索的是語義等價類，還是只探索某個表面表示鄰域？}
$$

所以後續系列將引入等價關係：

$$
q_i\sim q_j
$$

表示兩個 artifact 在某個聲明的 proof-relevant equivalence 下應視為同一研究狀態或同一 obstruction family。

真正需要分析的不是原始 artifact 數：

$$
N,
$$

而是：

$$
\left|\widehat\Omega_{R,N}/\sim\right|.
$$

這就是下一篇與第三篇將進一步建立的語義商空間問題。

## 6.3 表示變換本身可以成為搜尋算子

設：

$$
\rho\in\mathcal R
$$

為語義保持或近似保持的 representation transform。

則可把證明搜尋寫成：

$$
Q
\xrightarrow{\rho}
Q'
\xrightarrow{\Sigma}
\text{proof search}.
$$

此時搜尋制度不再只搜尋 proof steps，也搜尋 representation：

$$
\Sigma:
(Q,R)
\mapsto
(\rho_1,\rho_2,\ldots,\rho_k).
$$

這使「換個說法」從語言修辭升格為正式 research action。

---

# 7. 從 proof tree 到 research graph

## 7.1 Proof state tree 只描述一部分

Stepwise 等 neuro-symbolic proof search 系統把 theorem proving 視為 proof state tree search：每個 tactic 將目前 state 轉成下一個 state，搜尋演算法選擇有希望的分支。

這種結構可以寫成：

$$
G_{\mathrm{proof}}
=
(V_{\mathrm{state}},E_{\mathrm{tactic}}).
$$

對形式證明而言非常自然。

但研究級數學還包含：

- 文獻節點；
- 非形式 conjecture；
- 反例候選；
- 失敗原因；
- 跨論文依賴；
- 表示變換；
- proof plan；
- 研究者或 agent 的 route decision。

所以更一般的 research graph 應寫成多型別圖：

$$
G_N
=
(V_N,E_N,\tau_V,\tau_E),
$$

其中：

$$
\tau_V(v)
\in
\{
\text{claim},
\text{lemma},
\text{proof-state},
\text{example},
\text{counterexample},
\text{paper},
\text{obstruction},
\text{representation}
\},
$$

而：

$$
\tau_E(e)
\in
\{
\text{depends-on},
\text{contradicts},
\text{reformulates},
\text{verifies},
\text{fails-at},
\text{revisits},
\text{generalizes},
\text{specializes}
\}.
$$

## 7.2 TheoremGraph 提供了一個重要外部基礎

TheoremGraph 在 2026 年以 statement-level dependency graph 連接 informal 與 formal mathematics，從數學 arXiv 抽取大量 theorem-like environments 與候選依賴，同時建立 Lean declaration graph。這說明「數學知識的節點與依賴」不是純哲學比喻，而是已經能成為大型計算資料結構。

本文與 TheoremGraph 的差異是：

- TheoremGraph 主要關心既有數學知識的 statement-level dependency；
- 本系列進一步關心**尚未成功的研究過程**如何形成 route、obstruction 與 revisit graph。

兩者可以在未來結合：

$$
\text{knowledge graph}
+
\text{research-process graph}
\rightarrow
\text{proof-space observatory}.
$$

## 7.3 已證明圖與研究記憶圖必須分離

Danus 的架構給出一個重要設計原則：verified facts 進入 fact graph，未驗證的 plans、dead ends、examples 與 counterexamples 留在 memory。

本文將這個分離抽象成：

$$
\boxed{
\mathcal F_N
\cap
\mathcal U_N
=
\varnothing
}
$$

作為理想化治理原則。

實作上兩者可以互相引用，但不能在語義上混同：

$$
\text{memory item}
\not\Rightarrow
\text{verified fact}.
$$

這對 AI 長程研究尤其關鍵，因為一個被多次摘要、轉述、回收的未驗證猜想，很容易在後續 context 中逐漸被誤認為已知事實。

---

# 8. 長程研究真正的新問題：狀態漂移、依賴污染與研究記憶腐敗

## 8.1 不是只要 context window 變長

長程數學研究的困難不能被簡化成：

$$
\text{需要更多 token}.
$$

LeanMarathon 所指出的 statement drift、dependency tangling、context decay 與 local repair corruption 顯示，長上下文本身不是充分條件。

即使所有歷史都能塞進 context，也可能造成：

- 無關內容干擾；
- 過時假設持續存活；
- 被推翻 lemma 未被撤回；
- 不同版本的定義混用；
- 相同 notation 在不同階段改義；
- 研究摘要刪掉反例條件；
- agent 只記得「有一個結果」，卻忘記成立前提。

因此需要的是**版本化、依賴化、可撤銷的研究記憶**。

## 8.2 記憶不是 truth store

本文定義：

$$
\operatorname{TruthStatus}(x)
\in
\{
\text{verified},
\text{conditionally verified},
\text{heuristic},
\text{unverified},
\text{refuted},
\text{withdrawn}
\}.
$$

任何記憶系統若只有文本而沒有 truth status，就容易形成 epistemic contamination。

因此對 AI 數學 research memory 的最低要求不是「記得越多越好」，而是：

$$
\boxed{
\text{remembered content}
+
\text{status}
+
\text{dependencies}
+
\text{version}
+
\text{provenance}.
}
$$

## 8.3 撤銷必須沿依賴傳播

如果事實 $f_j$ 依賴 $f_i$：

$$
f_i\rightarrow f_j,
$$

而後來 $f_i$ 被撤銷，則至少需要計算：

$$
\operatorname{Desc}(f_i)
=
\{f:f_i\leadsto f\},
$$

並重新評估所有後代。

這是 proof engineering 與一般聊天式「更正一下前面」之間的本質差別。

---

# 9. 研究成功不應只有一個 bit

## 9.1 傳統成功變數

最簡單 benchmark 用：

$$
S_Q
\in
\{0,1\},
$$

表示是否成功證明目標。

這對競賽與 formal benchmark 非常合理，但對研究過程太粗。

## 9.2 多維研究結果向量

本文建議至少記錄：

$$
Y_N
=
(
P_N,
R_N,
L_N,
O_N,
C_N,
T_N
),
$$

其中：

- $P_N$：目標證明或反證狀態；
- $R_N$：已探索 route 類；
- $L_N$：新增且已驗證 lemma；
- $O_N$：已審計 obstruction 類；
- $C_N$：跨路徑 confluence 結構；
- $T_N$：可轉移到其他問題的工具或結果。

因此可能發生：

$$
P_N=0,
$$

但：

$$
L_N>0,
\qquad
O_N>0,
\qquad
T_N>0.
$$

此時「原問題未解」與「研究產出為零」不是同義詞。

## 9.3 但中間產出也不能冒充主目標完成

反過來：

$$
L_N\gg0
$$

也不能推出：

$$
P_N=1.
$$

這個方向同樣重要。大量漂亮 lemma、數值實驗與理論命名都不能替代目標 proof obligation。

所以本文採雙重紀律：

$$
\boxed{
\text{不要把未解寫成零成果；也不要把大量成果寫成已解。}
}
$$

---

# 10. NS-203：一個「如何不過度解讀」的動機案例

## 10.1 Corpus 定位

本系列的直接研究動機之一，是一批長期 AI 輔助 Navier--Stokes 研究產物。經遞迴掃描、hash 去重與保守排除 README、CHANGELOG、roadmap、handoff、audit 等非 paper-like 文件後，得到：

$$
203
$$

份 NS paper-like artifacts。

另有一條「空間域證明包圍」方法論支線。

這批 corpus 的價值不在於其篇數本身，而在於它保留了：

- 系列 progression；
- dependency reference；
- no-go；
- recurrence；
- confluence；
- second-order / higher-order / all-order 等後期語言；
- proof asset transfer。

## 10.2 第一版觀測結果

Proof-Space Sampling Observatory v0.1 對 203 篇 NS paper-like artifacts 建立了 paper-level graph，偵測到：

$$
189
$$

條 sequence edges，

$$
390
$$

條 explicit dependency edges，以及：

$$
258
$$

條 revisit-similarity edges。

以保守 heuristic 分層後得到：

$$
T_1=84,
\qquad
T_2=107,
\qquad
T_3=10,
\qquad
T_X=2.
$$

這些數字不是數學 theorem order，而只是「一階 route、回訪、匯流、高階 family recurrence」的操作性分級。

## 10.3 最重要的結果其實是否定一個過強敘事

若只看 cumulative nearest-neighbor novelty，後期 novelty 下降，容易產生「整體空間快耗盡」的直覺。

但 cumulative 指標有天然 size bias：越後面的文章可以與越多舊文章比較，因此最近鄰相似度本來就容易上升。

改採固定回看窗口：

$$
\nu_i^{(W)}
=
1-
\max_{i-W\leq j<i}
\operatorname{sim}(S_i,S_j),
\qquad
W=20,
$$

後，Q2 與 Q4 的平均 novelty 並沒有呈現異常負向崩塌；500 次 random permutation baseline 也沒有支持「整個 corpus 已顯著進入全域 novelty collapse」。

因此第一版較合理的結論不是：

$$
\text{NS proof space exhausted}.
$$

而是：

$$
\boxed{
\text{某些局部研究 basin 已出現高階回訪與匯流，但全域飽和未被建立。}
}
$$

## 10.4 為什麼這個負結果非常重要

因為它示範了本文主張的方法論紀律。

研究者本來可能因為 corpus 很大、重複很多，就先相信：

> 符號空間快耗盡了。

但正式 instrumentation 迫使我們改寫成較弱、較可驗證的命題：

> 部分路徑族呈現局部 recurrence 與 higher-order resampling；全域 novelty collapse 尚未成立。

這就是 proof-space science 應該做的事情：

$$
\boxed{
\text{把強直覺降解為可檢驗結構，而不是替直覺找漂亮語言。}
}
$$

## 10.5 NS 與 P vs NP 在本系列中的地位

截至 2026-08-17，Clay Mathematics Institute 仍將 Navier--Stokes existence and smoothness 與 P vs NP 列為未解 Millennium Prize Problems。

因此本系列只把它們當：

$$
\boxed{
\text{high-difficulty stress tests for research-space instrumentation}.
}
$$

即使未來觀察到更強 saturation，也只能先說：

$$
\operatorname{Sat}(Q;R,N),
$$

不能直接寫：

$$
\operatorname{Misframed}(Q).
$$

---

# 11. 從「證明器」到「研究儀器」

## 11.1 AI theorem prover 的兩種角色

角色 A：

$$
\text{solver}.
$$

目標是快速取得：

$$
\pi.
$$

角色 B：

$$
\text{instrument}.
$$

目標是累積：

$$
\mathfrak S_N
=
(
\widehat\Omega_{R,N},
\mathcal F_N,
\mathcal U_N,
\mathcal H_N
).
$$

兩者不衝突。理想系統同時追求 proof success 與 research observability。

## 11.2 可觀測性是新的設計要求

一個只能輸出最終答案的強模型，可能在 solver metric 上很高，但在研究科學上幾乎不可審計。

因此本文提出：

$$
\boxed{
\text{Research capability}
\neq
\text{final-answer capability}.
}
$$

至少還應包含：

$$
\text{observability},
\quad
\text{replayability},
\quad
\text{provenance},
\quad
\text{dependency integrity},
\quad
\text{failure retention}.
$$

## 11.3 研究制度本身可以被實驗

一旦 $R$ 被明確記錄，就能做 regime comparison：

$$
R_1
\leftrightarrow
R_2.
$$

例如只改變：

- representation rewrites；
- memory policy；
- number of workers；
- verifier strictness；
- retrieval corpus；
- route pruning；
- formalization timing；

然後比較：

$$
\Delta
\left|
\widehat\Omega_{R,N}/\sim
\right|,
$$

$$
\Delta P(\operatorname{prove}Q),
$$

$$
\Delta \operatorname{Confluence},
$$

$$
\Delta \operatorname{RevisitRate}.
$$

這把「哪個 agent 比較會研究」從主觀體感轉成可重放的制度實驗。

---

# 12. 本系列的最小資料契約

若要讓後續 proof-space integration 成為可重現研究，每個 artifact 至少應保存下列欄位：

```text
artifact_id
timestamp
parent_artifact_ids
target_claim
claim_scope
assumptions
representation
representation_transform
method_family
tools_used
source_dependencies
new_lemmas
proof_route
obstruction
counterexample_status
verification_status
formalization_status
truth_status
revisit_of
supersedes
withdraws
transfer_targets
notes
```

## 12.1 為什麼 `truth_status` 與 `verification_status` 要分開

某個 statement 可能：

- 已通過 Lean；
- 只通過數值測試；
- 只被另一個 LLM verifier 認為合理；
- 被人工審核但未形式化；
- 只是一個 heuristic。

所以：

$$
\operatorname{VerificationStatus}
\neq
\operatorname{TruthStatus}.
$$

尤其不能把：

$$
\text{LLM verifier accepted}
$$

直接寫成：

$$
\mathcal A\vdash Q.
$$

## 12.2 為什麼要保存 `revisit_of`

沒有 `revisit_of`，大量高階採樣會被錯算成 novelty。

例如三份文章：

$$
g_1,
\quad
g_2,
\quad
g_3
$$

表面名稱不同，但實際都在攻擊同一 obstruction $O$。

若不保存 linkage，corpus size 會虛增；若保存：

$$
g_2\rightarrow g_1,
\qquad
g_3\rightarrow g_1,
$$

就可以研究「回訪的階數與方式」。

## 12.3 為什麼要保存 withdrawal

數學研究不是單調只增長：

$$
\mathcal F_{N+1}
\not\supseteq
\mathcal F_N
$$

在實際工程上未必永遠成立，因為錯誤 fact 需要撤銷。

因此 knowledge state 應允許：

$$
f
\mapsto
\operatorname{withdrawn}(f),
$$

並沿 dependency graph 重新計算後果。

---

# 13. 什麼才算「可檢驗的 proof-space science」

本文不希望 proof-space 變成不可證偽的哲學比喻，因此提出以下最小經驗研究程序。

## 13.1 固定研究制度

先固定：

$$
R.
$$

至少記錄 model、toolchain、library version、memory policy、verifier、prompt/harness、resource budget。

## 13.2 建立 artifact registry

每一輪產物進入：

$$
\mathcal C_N.
$$

不得只保留「成功輪」。

## 13.3 建立等價關係候選

先用低成本 heuristic 產生：

$$
q_i\sim_? q_j,
$$

再以人工或形式 audit 決定是否真的可合併。

## 13.4 分離 raw novelty 與 quotient novelty

原始 novelty：

$$
\nu_i^{\mathrm{raw}}.
$$

商空間 novelty：

$$
\nu_i^{/\sim}.
$$

若兩者差很大，表示系統正在大量做 surface variation。

## 13.5 追蹤 obstruction recurrence

對 canonical obstruction ID：

$$
O_j
$$

記錄：

$$
\operatorname{freq}(O_j),
$$

$$
\operatorname{series}(O_j),
$$

$$
\operatorname{representation}(O_j),
$$

$$
\operatorname{method}(O_j).
$$

## 13.6 設置反事實比較

例如：

- 隨機重排時間順序；
- 隨機移除 memory；
- 關閉 representation rewrite；
- 更換 verifier；
- 更換 theorem retrieval；

若 saturation 指標仍然不變，才更有資格說它不是單純 harness artifact。

---

# 14. 本文提出的可檢驗假說

本文不把以下命題稱為已證定理，而把它們列為後續系列的 research hypotheses。

## 假說 H1：長程軌跡資訊假說

在固定總算力下，保存可重用的失敗與依賴結構，可能提高後續搜尋的 sample efficiency：

$$
E[
\operatorname{new\_classes}
\mid
\text{structured memory}
]
>
E[
\operatorname{new\_classes}
\mid
\text{stateless retries}
].
$$

## 假說 H2：表示商空間假說

對長程 AI theorem proving，原始 artifact count 對有效研究覆蓋的估計存在系統性高估：

$$
N
\gg
\left|\widehat\Omega_{R,N}/\sim\right|
$$

在某些高度重訪的研究階段尤為明顯。

## 假說 H3：局部先於全域飽和假說

若 proof space 具有多 basin 結構，則最先出現的應是：

$$
\operatorname{Sat}(B_i)
$$

而不是：

$$
\operatorname{Sat}(\Omega_R).
$$

## 假說 H4：跨表示穩定障礙具有更高診斷價值

若 obstruction $O$ 能跨：

$$
\rho_1,\rho_2,\ldots,\rho_k
$$

與多種方法族重現，則它比單一路徑 no-go 更值得優先研究。

## 假說 H5：研究制度可作為獨立變數

對同一 $Q$，更換 $R$ 的單一成分可能顯著改變 route distribution：

$$
P(\text{route}\mid Q,R_1)
\neq
P(\text{route}\mid Q,R_2).
$$

此假說若成立，則「AI 能否證明」不能只用 model name 解釋。

---

# 15. 哪些東西本文刻意不主張

為避免後續引用失真，本文明確列出非主張。

本文**不主張**：

1. 所有數學問題都有有限可枚舉 proof space；
2. $\Omega_{\mathrm{all}}(Q)$ 必然可以被完整定義或計算；
3. 大量 AI 生成足以窮盡所有數學方法；
4. repetition 必然表示 saturation；
5. saturation 必然表示命題錯誤；
6. saturation 必然表示問題 framing 錯誤；
7. 未找到證明可以推出獨立性或不可判定性；
8. 多 agent 必然比單 agent 更接近真理；
9. formal proof 等同於完整數學理解；
10. informal reasoning 沒有研究價值；
11. LLM verifier 的接受等同 proof assistant kernel 驗證；
12. 所有 negative proof information 都可以自動形式化；
13. NS-203 已證明 Navier--Stokes 存在任何特定 proof-space obstruction theorem；
14. P vs NP 或 Navier--Stokes 的標準問題定義已被證明有錯；
15. proof-space science 可以取代傳統數學證明。

其中第 13 至 14 點尤其重要：本系列允許把「定義範疇錯置」當作候選 meta-hypothesis，但只有在出現真正形式化的新定義、新映射、新證明以及獨立驗證時，才有資格把它提升為對既有問題的數學或科學結論。

---

# 16. 與真理、證明、理解、生成性的區分

本系列後續會研究一個更反直覺的問題：某個問題 framing 即使不完美，仍可能生成大量正確局部理論；反之，越接近閉合的理論，表面語義新奇度可能反而降低。

但在本篇 Charter 中，我們先建立四個彼此不同的量：

$$
T
=
\text{truth / correctness},
$$

$$
P
=
\text{provability / verified proof status},
$$

$$
G
=
\text{generativity},
$$

$$
U
=
\text{utility / transfer value}.
$$

一般不能預設：

$$
T\uparrow
\Rightarrow
G\uparrow,
$$

也不能預設：

$$
G\uparrow
\Rightarrow
T\uparrow.
$$

這個分離將在 LSI-PSD-07 至 09 中展開；本篇只負責確保「搜尋過程的豐富」不被誤認為「目標命題已經成立」。

---

# 17. 與現有 AI 數學研究的對話位置

## 17.1 AlphaProof：驗證環境的重要性

AlphaProof 的核心貢獻之一，是讓模型在 Lean formal environment 中透過可驗證回饋學習 proof search。對本系列而言，它代表：

$$
\text{search}
+
\text{trusted verification signal}
$$

可以大幅提升研究資料品質。

但 AlphaProof 的 benchmark success 不自動回答「長期未成功分支應如何保存」。本系列研究的正是這個剩餘問題。

## 17.2 HERMES 與 LEAP：探索和驗證可以交錯

HERMES 以中間形式驗證防止 informal reasoning drift，LEAP 用 blueprint 與 compiler feedback 反覆修正 proof construction。它們共同提示：

$$
\text{informal exploration}
\leftrightarrow
\text{formal check}
$$

比完全分離兩者更可能維持長程穩定。

## 17.3 LeanMarathon：長程可靠性是一個系統工程問題

LeanMarathon 的 blueprint、DAG 與 CI-gated workflow 說明：即使單步 prover 很強，長程 formalization 仍然會因 target drift、dependency corruption 與 context management 失敗。

因此：

$$
\boxed{
\text{strong prover}
\not\Rightarrow
\text{reliable long-horizon research system}.
}
$$

## 17.4 RMA：研究級問題需要 literature-grounded iterative refinement

RMA 明確將 research-level mathematics 與 competition-style problem solving 區分，強調 literature grounding、problem analysis、knowledge-bank construction 與 iterative proof refinement。

這與本文的 $R$ 定義高度相容：

$$
\mathcal K
$$

不是附加工具，而是搜尋制度的一部分。

## 17.5 Danus：fact graph 與 memory 的分權

Danus 把 verifier-accepted facts 當 source of truth，把其他有用內容留在 memory，提供一個很接近本文治理要求的實例。

其架構也揭示另一點：大量被建立的 verified facts 不一定都進入最終 proof path。因此真正長程研究的資料結構天然比一條線性證明更寬。

## 17.6 TheoremGraph：依賴結構已經能被大規模計算

TheoremGraph 從 informal 與 formal mathematics 建立 statement-level dependency infrastructure，使「數學知識是一張巨大依賴圖」從直覺變成可工程化對象。

本系列希望再向前一步：

$$
\text{established theorem graph}
\rightarrow
\text{live research-process graph}.
$$

## 17.7 表示對稱性研究：搜尋制度本身帶有偏差

2026 年的 formal theorem proving symmetry 研究顯示，LLM prover 對 semantics-preserving rewrite 仍缺乏 success invariance。這直接警告：

$$
\text{proof difficulty observed by AI}
$$

不完全是：

$$
\text{intrinsic mathematical difficulty}.
$$

它同時包含 representation bias。

這也是為什麼後續不能直接從「大量路徑都失敗」推出「數學上真的沒有路」。

---

# 18. 系列整體研究路線

本篇是 Charter，不試圖一次完成所有形式化。後續系列按下列順序展開：

$$
\text{search regime}
\rightarrow
\text{coverage}
\rightarrow
\text{quotient}
\rightarrow
\text{higher-order sampling}
\rightarrow
\text{local saturation}
\rightarrow
\text{confluence}
\rightarrow
\text{truth--generativity relation}
\rightarrow
\text{productive mis-specification}
\rightarrow
\text{non-conclusion}
\rightarrow
\text{observatory}.
$$

對應論文：

1. LSI-PSD-01：證明空間不是證明；
2. LSI-PSD-02：邏輯空間積分；
3. LSI-PSD-03：語義商空間；
4. LSI-PSD-04：高階證明空間採樣；
5. LSI-PSD-05：局部飽和與全域開放；
6. LSI-PSD-06：障礙匯流與研究路由；
7. LSI-PSD-07：真理--生成性反轉；
8. LSI-PSD-08：生產性錯置；
9. LSI-PSD-09：生產性錯置窗口；
10. LSI-PSD-10：飽和不是判決；
11. LSI-PSD-11：從科學史到 AI 的結構性錯誤；
12. LSI-PSD-12：AI 證明空間觀測站。

---

# 19. 符號表

| 符號 | 定義 |
|---|---|
| $Q$ | 目標命題 |
| $\mathcal A$ | 公理、邏輯與形式背景 |
| $\mathcal L$ | 表示與符號語言 |
| $\mathcal M$ | 方法族與工具集合 |
| $\mathcal V$ | 驗證器集合 |
| $B$ | 時間、算力、token、proof depth 等資源界 |
| $\mathcal K$ | 文獻、形式庫與既有知識 |
| $\Sigma$ | 調度、搜尋與停止策略 |
| $R$ | 完整搜尋制度 |
| $\Pi_{\mathcal A}(Q)$ | $\mathcal A$ 中可接受的形式證明物件集合 |
| $\Omega_R(Q)$ | 制度 $R$ 下可達或可辨識的研究狀態空間 |
| $\widehat\Omega_{R,N}(Q)$ | 執行 $N$ 輪後實際觀測到的研究狀態 |
| $\mathcal H_N$ | 研究事件歷史 |
| $\mathcal F_N$ | 已驗證 fact graph |
| $\mathcal U_N$ | 未驗證但可重用的 research memory |
| $\mathfrak S_N$ | 完整長程研究狀態 |
| $F_i$ | 一個失敗／障礙紀錄 |
| $O_i$ | canonical obstruction 候選 |
| $\rho$ | representation transform |
| $\sim$ | proof-relevant 等價關係 |
| $\nu_i$ | novelty 指標 |
| $T_k$ | 操作性高階採樣 tier，不代表形式高階範疇 |

---

# 20. 依賴、可驗證性與未來加強方向

## 20.1 本篇前置依賴

本篇為系列 Charter，沒有必須先接受的 LSI-PSD 前篇。

外部概念依賴包括：

- 形式證明與 proof assistant 的一般框架；
- proof state search；
- theorem dependency graph；
- 長程 agent memory；
- 形式系統中的 provability 與 independence 區分。

## 20.2 後續直接依賴本篇的文章

- LSI-PSD-02 將定義 coverage 與 logic-space integration；
- LSI-PSD-03 將處理 $\Omega/\sim$；
- LSI-PSD-04 將定義多階 proof-space sampling；
- LSI-PSD-10 將把 non-conclusion principle 擴展為完整診斷樹；
- LSI-PSD-12 將把本篇 schema 轉成可執行 observatory。

## 20.3 下一步最重要的硬化工作

本篇最需要未來實作驗證的，不是再增加更多哲學術語，而是：

1. 建立 theorem-level artifact schema；
2. 為 obstruction 建立 canonical ID；
3. 分離 lexical similarity 與 semantic equivalence；
4. 以人工／形式 audit 確認 route quotient；
5. 對不同 $R$ 做 controlled comparison；
6. 使用真正獨立 verifier 估計 false-positive rate；
7. 對 memory ablation 測試 negative proof information 是否真的提高探索效率。

只有完成這些，proof-space dynamics 才能從概念框架逐步成為經驗研究方法。

---

# 21. 結論

AI 數學研究正在跨過一個容易被忽略的門檻。過去我們主要問：

$$
\text{AI 能不能證明 }Q?
$$

現在還必須問：

$$
\boxed{
\text{AI 在嘗試證明 }Q\text{ 的過程中，究竟形成了什麼可審計的研究結構？}
}
$$

這個問題不是把證明降格成搜尋；恰恰相反，它把搜尋制度本身提升為需要被嚴格研究、版本化、驗證與比較的對象。

本文的第一條底線是：

$$
\boxed{
\text{observed proof space}
\neq
\text{all mathematical proof possibilities}.
}
$$

第二條底線是：

$$
\boxed{
\text{search failure or saturation}
\not\Rightarrow
\text{falsehood, misframing, independence, or unprovability}.
}
$$

第三條底線則朝另一個方向：

$$
\boxed{
\text{absence of a final proof}
\not\Rightarrow
\text{absence of research information}.
}
$$

長程 AI 研究最有價值的新增物，可能不只是更多候選證明，而是：

$$
\text{verified facts}
+
\text{dependency structure}
+
\text{negative proof information}
+
\text{route history}
+
\text{representation history}.
$$

若這些資料被保存並正確分層，數百、數千、乃至更大規模的研究生成才不會退化成文字堆積；它們才可能成為研究「研究本身」的材料。

因此，本系列的起點不是「我們已經耗盡證明空間」，而是更保守也更強的一句話：

$$
\boxed{
\textbf{Proof-space observations are evidence about a search regime, not proof about all mathematics.}
}
$$

只有接受這條限制，後續的邏輯空間積分、局部飽和、高階採樣、真理--生成性反轉與生產性錯置，才不會從方法論滑向過度宣稱。

---

# 參考文獻

1. Davies, A., et al. (2025). *Olympiad-level formal mathematical reasoning with reinforcement learning*. Nature. DOI: 10.1038/s41586-025-09833-y.  
   說明：AlphaProof；形式 Lean 環境中的強化學習與可驗證 proof search。

2. Ospanov, A., Feng, Z., Sun, J., Bai, H., Shen, X., & Farnia, F. (2025). *HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs*. arXiv:2511.18760.  
   說明：非形式推理、Lean 中間驗證與長多步記憶。

3. Requena, B., Letson, A., Nowakowski, K., Beltran-Ferreiro, I., & Sarra, L. (2026). *A Minimal Agent for Automated Theorem Proving*. arXiv:2602.24273.  
   說明：iterative refinement、memory、library/tool search 的簡化 agentic baseline。

4. He, B., Li, Z., Sun, W., Yao, Y., Chen, T., Ma, X., & Su, Z. (2026). *Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification*. arXiv:2603.19715.  
   說明：best-first proof-state tree search 與 symbolic repair/pruning。

5. Zhao, Z., Yuan, B., Choi, J., & Chen, Y. (2026). *RMA: an Agentic System for Research-Level Mathematical Problems*. arXiv:2605.22875.  
   說明：research-level long-horizon reasoning、literature grounding、knowledge bank 與 iterative proof refinement。

6. Olejniczak, K., Dimitrov, R., Huang, X., Cuenca Grau, B., Kim, J., & Ceylan, I. I. (2026). *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257.  
   說明：semantics-preserving rewrite 下的 proof success variation、proof equivariance 與 success invariance。

7. Kung, P.-N., Song, L., Hwang, D., Yoon, J., Li, C.-L., Severini, S., Olšák, M., Lockhart, E., Le, Q. V., Gokturk, B., Luong, T., Pfister, T., & Peng, N. (2026). *LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks*. arXiv:2606.03303.  
   說明：informal blueprint、problem decomposition、Lean compiler feedback 與 iterative self-refinement。

8. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., & Liu, F. (2026). *LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization*. arXiv:2606.05400.  
   說明：statement drift、dependency tangling、context decay、evolving blueprint 與 CI-gated long-horizon workflow。

9. Pu, L., Zhang, W., Xie, X., Fu, Z., He, B., Lyu, H., Li, X., Zhou, J., & Wang, Y. (2026). *MA-ProofBench: A Two-Tiered Evaluation of LLMs for Theorem Proving in Mathematical Analysis*. arXiv:2606.13782.  
   說明：advanced mathematical analysis formal proving benchmark，以及 informal/formal reasoning gap。

10. Kurgan, S., Wang, E., Leonen, E., Szeto, S., Alexander, L., Remizov, A., Alper, J., Inchiostro, G., & Ilin, V. (2026). *TheoremGraph: Bridging Formal and Informal Mathematics*. arXiv:2606.25363.  
    說明：大規模 statement-level dependency graph、LeanGraph 與 informal/formal bridge。

11. Liu, J., Gao, G., Sun, Z., Wu, B., Liu, S., Jiang, J., Ju, H., Chen, L., Cheng, R., Zhang, X., & Dong, B. (2026). *Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory*. arXiv:2607.06447.  
    說明：fact graph、parallel workers、stateless verifier、verified facts 與 unverified memory 的分離。

12. Goedel, K. (1931). *Ueber formal unentscheidbare Saetze der Principia Mathematica und verwandter Systeme I*. Monatshefte fuer Mathematik und Physik, 38, 173--198.  
    說明：形式系統中的不可完備性；本文僅用以提醒 independence/unprovability 需要元數學論證，而非搜尋失敗類比。

13. Fefferman, C. L. (2000). *Existence and Smoothness of the Navier--Stokes Equation*. In *The Millennium Prize Problems*, Clay Mathematics Institute.  
    說明：Navier--Stokes Millennium Problem 的官方問題描述。

14. Cook, S. (2000). *The P versus NP Problem*. In *The Millennium Prize Problems*, Clay Mathematics Institute.  
    說明：P vs NP Millennium Problem 的官方問題描述。

---

# 附錄 A：最小 research-state JSON 示意

以下僅為 schema 示意，不是唯一資料格式：

```json
{
  "artifact_id": "LSI-EXAMPLE-0001",
  "target_claim": "Q",
  "claim_scope": "declared-domain",
  "assumptions": ["A1", "A2"],
  "representation": "R3",
  "representation_transform": "rho_2",
  "method_family": ["compactness", "energy"],
  "dependencies": ["F12", "F18"],
  "new_lemmas": ["L31"],
  "proof_route": ["S0", "S4", "S9"],
  "obstruction": "O7",
  "verification_status": "partially_formalized",
  "truth_status": "conditional",
  "revisit_of": ["LSI-EXAMPLE-0000"],
  "supersedes": [],
  "withdraws": [],
  "transfer_targets": ["Q2"]
}
```

---

# 附錄 B：最小判定語法

當研究者觀察到高 recurrence 時，推薦使用：

$$
\boxed{
\text{Observed: repeated obstruction under declared regime }R.
}
$$

而不是：

$$
\boxed{
\text{Therefore the mathematical problem is wrong.}
}
$$

當固定窗口 novelty 下降時，推薦使用：

$$
\boxed{
\text{Evidence for local novelty reduction under the current quotient heuristic.}
}
$$

而不是：

$$
\boxed{
\text{Proof space exhausted.}
}
$$

當多條路徑匯流時，推薦使用：

$$
\boxed{
\text{Candidate route-confluence obstruction requiring semantic audit.}
}
$$

而不是：

$$
\boxed{
\text{Universal no-go theorem.}
}
$$

這些語法限制不是保守主義，而是讓長程 AI 研究結果能夠真正累積、比較與被獨立研究者檢驗的最低條件。


<!-- END LSI-PSD-01 -->

---


<!-- BEGIN LSI-PSD-02 -->

# LSI-PSD-02 — 邏輯空間積分：從單次證明搜尋到研究空間覆蓋

## Logic-Space Integration: From Single Proof Search to Research-Space Coverage

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 02  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Coverage Formalization Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文建立「邏輯空間積分」的操作性數學框架，用來描述長程 AI 數學研究中已探索、已驗證、已排除、已回訪與仍未知的研究區域。本文所稱的 coverage、integration、saturation、basin、obstruction coverage 等量，首先是對特定搜尋制度之可觀測研究狀態的度量，不等於對所有可能證明、所有可能表示、所有可能公理擴張或數學真理本身的完整測度。本文不主張已能計算任何公開未解問題的「真實總證明空間百分比」，更不把 coverage 高、novelty 下降或局部飽和視為原命題錯誤、不可證、不可判定或已被反證的證據。

---

## 摘要

當 AI 數學研究從單次輸出擴張到數百、數千甚至更長的持續研究輪次時，「是否找到最終證明」不再足以描述研究系統的進度。大量中間引理、失敗路徑、表示切換、反例候選、形式驗證、數值實驗與跨路線匯流會形成一個具有歷史、局部性與重訪結構的研究空間。若這些資料只以最後成功或失敗二分，則研究系統無法回答一個更基礎的問題：**我們究竟探索了什麼，以及新增一輪研究到底增加了多少可審計的新資訊？**

本文提出「邏輯空間積分」的第一個完整形式化框架。承接 LSI-PSD-01 所定義的搜尋制度

$$
R=(\mathcal A,\mathcal L,\mathcal M,\mathcal V,B,\mathcal K,\Sigma),
$$

本文把研究空間區分為形式可證域、制度可達域、觀測域、驗證域與暫存研究記憶，並在適當的語義商空間上定義 coverage function：

$$
c_N:\bar\Omega_R(Q)\rightarrow[0,1].
$$

由此定義理想化的邏輯空間積分：

$$
I_N
=
\int_{\bar\Omega_R(Q)}
c_N(\omega)\,d\mu(\omega),
$$

以及增量：

$$
\Delta I_N
=
I_{N+1}-I_N.
$$

但本文特別指出：在真正未解數學問題中，分母 $\bar\Omega_R(Q)$ 通常未知，測度 $\mu$ 也不存在天然唯一選擇。因此，$I_N$ 首先是一個**理論極限量**，不能被輕率轉譯為「已探索了 $73\%$ 的證明空間」。可操作實驗應改用一組不假裝知道總空間大小的相對量，包括 state coverage、route coverage、obstruction coverage、method-family coverage、representation coverage、verification coverage 與 local-basin coverage。本文因此主張使用 coverage vector：

$$
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
),
$$

而不是過早把所有研究歷史壓縮成一個單一百分比。

本文進一步定義負資訊的積分效應：一條經審計的 no-go route 雖然沒有提供最終證明，卻可以合法縮小制度內的候選區域：

$$
\Omega_{N+1}^{surv}
=
\Omega_N^{surv}\setminus E_N,
$$

其中 $E_N$ 必須有明確條件、適用域與可重現證據。這使「失敗」第一次能被區分為零資訊失敗與正向 coverage gain。本文也定義 marginal research yield：

$$
\eta_N
=
\frac{\Delta \widetilde I_N}{\operatorname{Cost}(N,N+1)},
$$

用來衡量每單位算力、人工審計或生成成本所換得的新增可驗證研究區域。

近年的自動定理證明工作已顯示 proof search 應被視為軌跡與圖搜尋問題。LeanProgress 直接估計 proof trajectory 的剩餘步數；BFS-Prover、AlphaProof、TreeThink 等系統以搜尋樹與 verifier feedback 導航 proof space；Aristotle 將正式 proof search 與非正式推理、lemma generation 結合；AlphaProof Nexus 在公開未解問題上以多代理正式搜尋與 Lean 驗證工作；2026 年的 theorem testing benchmark 則顯示 theorem statement 能成功編譯，不代表其語義已被充分保存，後續 dependent theorems 可提供更強測試。這些結果共同說明，單一 pass/fail 指標不足以表示長程研究進度。

本文最後以 NS-203 長程 Navier--Stokes 語料作為原型案例。該案例已出現 route revisit、cross-series dependency、obstruction confluence 與局部 higher-order sampling，但固定窗口 novelty 統計並不支持「全域 novelty 已崩潰」的結論。這個結果用來示範本文最重要的原則：**coverage 可以局部增加，飽和可以局部成立，而全域證明空間仍然保持未知。**

**關鍵詞：** 邏輯空間積分、證明空間覆蓋、proof search、研究空間、coverage vector、局部飽和、negative information、obstruction、route graph、驗證權重、AI 數學研究、Navier--Stokes

---

# 1. 從「有沒有證明」轉向「研究空間增加了什麼」

## 1.1 單次 theorem proving 的成功函數

最簡單的自動定理證明評估可以寫為：

$$
S(Q)
=
\begin{cases}
1,&\exists \pi:\mathcal V(\pi,Q)=1,\\
0,&\text{otherwise}.
\end{cases}
$$

這個成功函數對 benchmark 很有用。

它回答：

> 這個系統是否找到一個 verifier 接受的證明？

但它刻意忽略：

- 嘗試過多少條路；
- 哪些中間引理已被證明；
- 哪些表示被證明難以處理；
- 哪些方法族反覆撞上同一障礙；
- 哪些失敗其實排除了大區域候選；
- 哪些路徑只是假重複；
- 哪些新結果沒有進入最終 proof term，卻能被其他研究重用。

因此：

$$
S(Q)
$$

是一個**終點指標**，不是研究歷史指標。

## 1.2 長程研究需要另一種進度概念

假設 AI 在固定問題 $Q$ 上持續工作 $N$ 輪。

每一輪產生研究事件：

$$
e_i
=
(
q_i,
s_i,
a_i,
r_i,
v_i,
t_i
),
$$

其中可以分別表示：

- $q_i$：當輪局部目標；
- $s_i$：進入時研究狀態；
- $a_i$：採取的方法或 action；
- $r_i$：輸出的候選結果；
- $v_i$：驗證狀態；
- $t_i$：時間、版本或 provenance。

完整歷史為：

$$
\mathcal H_N
=
(e_1,e_2,\ldots,e_N).
$$

如果最後仍沒有證明，傳統成功函數仍然只有：

$$
S(Q)=0.
$$

但這不代表：

$$
\mathcal H_N
=
\varnothing.
$$

反而可能：

$$
|\mathcal H_N|
\gg1.
$$

因此長程研究需要回答另一個問題：

$$
\boxed{
\text{How much structured research space has been traversed, tested, or ruled out?}
}
$$

本文把這個問題稱為：

$$
\boxed{
\textbf{Logic-Space Integration}
}
$$

即「邏輯空間積分」。

---

# 2. 邏輯空間不是字串空間

## 2.1 最粗糙的錯誤：把 token 數當探索量

如果把每一段生成文字都視為一個新研究點，則只要修改：

- 符號名稱；
- 句子順序；
- lemma 名稱；
- Markdown 排版；
- 變數字母；
- 同義詞；
- proof sketch 的自然語言表述；

就可以無限增加「探索量」。

這顯然不合理。

因此：

$$
\text{Text Space}
\neq
\text{Logic Space}.
$$

甚至：

$$
\text{Syntactic Novelty}
\neq
\text{Proof Novelty}.
$$

## 2.2 一階研究單元

本文暫時把一個研究單元表示為：

$$
x
=
(
P,
A,
M,
R,
O,
V
),
$$

其中：

- $P$：proposition / subgoal；
- $A$：assumptions；
- $M$：method / transformation；
- $R$：result；
- $O$：obstruction / failure mode；
- $V$：verification status。

兩段文字若表面不同，但經 canonicalization 後得到相同：

$$
(P,A,M,R,O,V),
$$

則應視為同一或高度等價研究狀態。

## 2.3 語義等價關係

定義暫定等價關係：

$$
x\sim y
$$

若 $x,y$ 在研究任務所關心的結構上不可區分。

例如：

$$
\begin{aligned}
&\text{rename}(x)=y,\\
&\text{reorder}(x)=y,\\
&\text{parameter-normalize}(x)=y,\\
&\text{same-proof-skeleton}(x,y)=1.
\end{aligned}
$$

真正要積分的空間不應是 $\Omega$，而至少是：

$$
\bar\Omega
=
\Omega/\sim.
$$

這裡的 $\sim$ 不可能一次完美定義。

因此 LSI-PSD-03 將專門處理：

$$
\boxed{
\text{Semantic Quotient Space}
}
$$

問題。

本文先使用「任務相對等價」作為操作性前提。

---

# 3. 搜尋制度與五種不同的空間

## 3.1 搜尋制度回顧

承接第一篇，定義搜尋制度：

$$
R
=
(
\mathcal A,
\mathcal L,
\mathcal M,
\mathcal V,
B,
\mathcal K,
\Sigma
).
$$

其中：

- $\mathcal A$：公理與背景理論；
- $\mathcal L$：表示語言；
- $\mathcal M$：方法族；
- $\mathcal V$：驗證系統；
- $B$：資源界；
- $\mathcal K$：既有知識與資料；
- $\Sigma$：調度、搜索與 agent 策略。

同一個 $Q$ 在不同 $R$ 下，具有完全不同的可達區域。

所以：

$$
\Omega_R(Q)
$$

不是數學宇宙本身。

它只是：

> 在目前制度下，可被產生、表示、調用、驗證或探索的研究狀態集合。

## 3.2 形式可證空間

令：

$$
\Omega_{formal}(Q;\mathcal A)
$$

表示在背景形式系統 $\mathcal A$ 中與 $Q$ 有關的合法 proof states、proof objects 與中間命題空間。

這已經可能極大，甚至根本不可實際枚舉。

## 3.3 制度可達空間

加入語言、方法、工具與資源限制：

$$
\Omega_R^{reach}(Q)
\subseteq
\Omega_{formal}(Q;\mathcal A).
$$

它表示：

> 理論上此搜尋制度有機會走到的區域。

這個集合仍然通常未知。

## 3.4 實際觀測空間

經過 $N$ 輪後真正走過：

$$
\Omega_N^{obs}(Q;R)
\subseteq
\Omega_R^{reach}(Q).
$$

這是我們最容易從 logs、artifact、proof state、tool execution 與版本紀錄重建的部分。

## 3.5 已驗證空間

只有通過指定驗證門檻的部分進入：

$$
\Omega_N^{ver}
\subseteq
\Omega_N^{obs}.
$$

可再分級：

$$
\Omega_N^{ver}
=
\Omega_N^{formal}
\cup
\Omega_N^{checked}
\cup
\Omega_N^{empirical},
$$

但不同級別不可混稱為相同強度。

## 3.6 研究記憶空間

研究系統還可能保存：

$$
\Omega_N^{mem}.
$$

其中包含：

- 未完成 proof sketch；
- speculative conjecture；
- failed branch；
- counterexample candidate；
- heuristic；
- literature lead；
- unresolved obstruction。

所以：

$$
\Omega_N^{mem}
\not\subseteq
\Omega_N^{ver}.
$$

但：

$$
\Omega_N^{mem}
$$

仍然可能具有高 routing value。

## 3.7 五空間不能混在一起

因此至少要維持：

$$
\boxed{
\Omega_{formal},
\Omega_R^{reach},
\Omega_N^{obs},
\Omega_N^{ver},
\Omega_N^{mem}
}
$$

五者分離。

尤其不能從：

$$
\Omega_N^{obs}
\approx
\Omega_R^{reach}
$$

就推成：

$$
\Omega_N^{obs}
\approx
\Omega_{formal}.
$$

更不能推成：

$$
\Omega_N^{obs}
\approx
\text{all mathematical possibilities}.
$$

---

# 4. 邏輯空間積分的理想定義

## 4.1 coverage function

在語義商空間：

$$
\bar\Omega_R(Q)
=
\Omega_R(Q)/\sim
$$

上，定義 coverage function：

$$
c_N:
\bar\Omega_R(Q)
\rightarrow
[0,1].
$$

直觀上：

$$
c_N(\omega)=0
$$

表示尚未觀察；

$$
c_N(\omega)=1
$$

表示在指定研究標準下已充分探索；

中間值表示：

- 僅生成；
- 僅局部驗證；
- 僅一種表示採樣；
- 缺乏獨立重現；
- 仍有重要子路徑未處理。

## 4.2 理想積分

若 $\bar\Omega_R(Q)$ 上存在適當測度 $\mu$，定義：

$$
I_N
=
\int_{\bar\Omega_R(Q)}
c_N(\omega)\,d\mu(\omega).
$$

這是本文名稱「邏輯空間積分」最直接的形式。

如果：

$$
\mu(\bar\Omega_R)=1,
$$

則形式上：

$$
0\le I_N\le1.
$$

但這個 normalization 只在 $\mu$ 已被合理定義時有意義。

## 4.3 為什麼不能隨便說「已探索 80%」

對真正困難數學問題，我們通常不知道：

$$
|\bar\Omega_R|.
$$

甚至不知道：

$$
\mu.
$$

更不知道不同 proof state 是否應該等權。

例如：

一千個同類參數變體：

$$
\omega_1,\ldots,\omega_{1000}
$$

可能比不上一次表示變換：

$$
T:\mathcal L_1\rightarrow\mathcal L_2
$$

所帶來的新研究區域。

因此：

$$
\boxed{
I_N\text{ 是理論極限量，不是天然可觀測百分比。}
}
$$

## 4.4 不完整測度仍然有用

即使無法得到全域 $\mu$，仍可在局部 chart：

$$
U\subset\bar\Omega_R
$$

上定義：

$$
I_N(U)
=
\int_U c_N(\omega)\,d\mu_U(\omega).
$$

這意味著：

> 全域 coverage 不可知，不妨礙局部 coverage 可測。

這一點對後續「局部飽和」至關重要。

---

# 5. 從單一積分改成 Coverage Vector

## 5.1 為什麼單一 scalar 太粗

假設兩個研究系統：

系統 A：

- 嘗試很多 states；
- 幾乎沒有驗證；
- route 很重複。

系統 B：

- states 較少；
- route 多樣；
- 每條都高度驗證；
- obstruction catalog 完整。

如果都壓成一個 $I_N$，可能失去最重要差別。

因此本文定義 coverage vector：

$$
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
).
$$

## 5.2 State Coverage

$$
C_N^{state}
$$

衡量已到訪 canonical research state 的範圍。

操作代理量可寫成：

$$
\widetilde C_N^{state}
=
|V_N^{uniq}|,
$$

其中 $V_N^{uniq}$ 是 canonicalized node set。

注意：

$$
|V_N^{uniq}|
$$

是絕對數，不是假裝知道全域分母的比例。

## 5.3 Route Coverage

令 proof-route graph：

$$
G_N=(V_N,E_N).
$$

route coverage 可觀察：

$$
\widetilde C_N^{route}
=
|E_N^{uniq}|.
$$

或考慮 route family：

$$
\mathcal R_N
=
\{[r_1],[r_2],\ldots,[r_m]\},
$$

其中：

$$
r_i\sim_r r_j
$$

表示兩條路在 transformation skeleton 上等價。

則：

$$
\widetilde C_N^{route-family}
=
|\mathcal R_N|.
$$

## 5.4 Obstruction Coverage

定義 canonical obstruction set：

$$
\mathcal O_N
=
\{O_1,O_2,\ldots,O_k\}.
$$

每個 $O_i$ 必須至少包含：

$$
O_i
=
(
\text{trigger},
\text{scope},
\text{failure mechanism},
\text{evidence},
\text{status}
).
$$

因此：

$$
\widetilde C_N^{obs}
=
|\mathcal O_N|.
$$

更重要的是重訪 multiplicity：

$$
m_N(O_i)
=
\#\{r:r\rightarrow O_i\}.
$$

以及跨方法匯流度：

$$
\kappa_N(O_i)
=
\#\{M_j: M_j\rightarrow O_i\}.
$$

## 5.5 Method-Family Coverage

若方法族為：

$$
\mathcal M
=
\{M_1,M_2,\ldots\},
$$

定義：

$$
\widetilde C_N^{method}
=
|\{M_i:\text{sampled by time }N\}|.
$$

但必須區分「叫了方法名稱」和「真的執行到能產生判定資訊」。

所以引入 method engagement weight：

$$
e_N(M_i)\in[0,1].
$$

則：

$$
C_N^{method,w}
=
\sum_i e_N(M_i).
$$

## 5.6 Representation Coverage

表示空間可能包含：

$$
\mathcal L
=
\{L_1,L_2,\ldots,L_s\}.
$$

例如同一問題可能使用：

- physical variables；
- vorticity form；
- Fourier representation；
- geometric formulation；
- weak formulation；
- functional-analytic representation；
- formal proof assistant encoding。

定義：

$$
C_N^{repr}
$$

衡量真正被採樣的 representation family。

這裡非常重要，因為：

$$
\text{route saturation in }L_1
$$

不代表：

$$
\text{route saturation in }L_2.
$$

## 5.7 Verification Coverage

定義驗證權重：

$$
w_v(x)
\in
[0,1].
$$

例如可以建立分級：

$$
0
<
w_{spec}
<
w_{crosscheck}
<
w_{formal}
\le1.
$$

這不是宣稱形式驗證涵蓋所有語義問題，而是表示：

> 在指定 statement 與形式系統內，其 deductive correctness 的驗證強度更高。

可定義：

$$
C_N^{ver}
=
\sum_{x\in V_N}w_v(x).
$$

---

# 6. 驗證不是一個 bit：Verification Lattice

## 6.1 binary verifier 的優點與限制

Lean 等 proof assistant 對已形式化 statement 可以給出非常強的：

$$
\mathcal V(\pi,Q)=1.
$$

但這仍然不能自動回答：

- $Q$ 是否忠實表達原始自然語言命題；
- 定義是否偷換；
- theorem statement 是否過弱；
- formalization 是否漏掉假設；
- 生成的 theorem 是否保留原 repository 的語義接口。

因此：

$$
\text{formal validity}
\neq
\text{complete semantic fidelity}.
$$

## 6.2 2026 theorem testing 的啟示

2026 年的 automated theorem proving testing 工作提出類似 integration testing 的概念：

生成的 theorem 不只要 compile，還要讓依賴它的 successor theorems 繼續成功。

形式化表示為：

$$
\operatorname{Compile}(T)=1
$$

仍不足；

還要求：

$$
\forall S_j\in Succ(T),
\quad
\operatorname{Compile}(S_j\mid T)=1.
$$

這提供一個重要方向：

$$
\boxed{
\text{verification strength can be relational.}
}
$$

## 6.3 驗證格

本文建議把驗證寫成 lattice-like state：

$$
V(x)
=
(
v_{syntax},
v_{formal},
v_{semantic},
v_{independent},
v_{transfer}
).
$$

其中：

- $v_{syntax}$：語法合法；
- $v_{formal}$：形式 proof checker 通過；
- $v_{semantic}$：statement 與原命題語義對齊；
- $v_{independent}$：獨立方法或獨立 agent 重現；
- $v_{transfer}$：作為上游結果時能否支援下游 theorem / computation。

因此兩個都「verified」的 artifact，仍可能驗證結構不同。

## 6.4 coverage 必須攜帶驗證資訊

因此：

$$
c_N(\omega)
$$

不應只由「曾到訪」決定。

更合理：

$$
c_N(\omega)
=
f(
visit,
repeat,
verification,
representation,
independent\_support
).
$$

例如一個簡化版本：

$$
c_N(\omega)
=
1-
\prod_{j=1}^{m}
(1-w_j e_{j,N}(\omega)),
$$

其中 $e_{j,N}$ 表示不同證據通道是否覆蓋該狀態。

這個公式不是唯一正確定義，而是說明：

> coverage 可以是多證據累積，而不是 visit counter。

---

# 7. 增量：研究真正重要的是 $\Delta I$ 而不是輸出長度

## 7.1 積分增量

定義：

$$
\Delta I_N
=
I_{N+1}-I_N.
$$

如果第 $N+1$ 輪只是重新描述已知內容：

$$
\Delta I_N
\approx0.
$$

即使輸出：

$$
10^4\text{ tokens}.
$$

相反，如果只增加一個短 lemma，但它開啟全新 route family：

$$
\Delta I_N
\gg0.
$$

即使文字非常短。

因此：

$$
\boxed{
\text{Output Volume}
\neq
\text{Research Increment}.
}
$$

## 7.2 研究邊際收益

令本輪成本：

$$
\operatorname{Cost}_N
=
\alpha C_{compute}
+
\beta C_{human}
+
\gamma C_{verification}
+
\delta C_{retrieval}.
$$

定義：

$$
\eta_N
=
\frac{\Delta\widetilde I_N}{\operatorname{Cost}_N}.
$$

其中 $\widetilde I_N$ 是可操作代理積分。

$\eta_N$ 可稱：

$$
\boxed{
\text{Marginal Research Yield}
}
$$

即「邊際研究收益」。

## 7.3 高產出不等於高收益

可能：

$$
Tokens_N\uparrow
$$

但：

$$
\eta_N\downarrow.
$$

這就是長程 AI 研究最容易出現的假繁榮：

> 生成量很大，但新 canonical state 幾乎沒有增加。

因此監控系統不能只報：

- paper count；
- token count；
- branch count。

而要報：

$$
\Delta V_N^{uniq},
\quad
\Delta E_N^{uniq},
\quad
\Delta\mathcal O_N,
\quad
\Delta\mathcal M_N,
\quad
\Delta\mathcal L_N.
$$

---

# 8. 負結果如何增加 coverage

## 8.1 一般直覺：失敗等於沒有進展

在只看最終 proof 的評估中：

$$
\text{failed attempt}
\mapsto
0.
$$

但長程研究不應如此粗糙。

## 8.2 可審計 no-go region

假設某 route family $R_a$ 在條件：

$$
H_a
$$

下被嚴格證明無法完成某 closure。

則可定義排除區域：

$$
E_a
=
\{x\in\Omega: H_a(x)\land R_a(x)\text{ fails by mechanism }O_a\}.
$$

如果 $E_a$ 有清楚適用域，就可以更新 survivor space：

$$
\Omega_{N+1}^{surv}
=
\Omega_N^{surv}
\setminus E_a.
$$

這是：

$$
\boxed{
\text{negative result}
\rightarrow
\text{positive space reduction}
}
$$

## 8.3 什麼失敗不能算 coverage gain

以下通常不能直接算：

- 模型說「我想不到」；
- 某次 generation timeout；
- syntax error；
- prompt 沒寫清楚；
- 沒有完整跑完搜索；
- 只測了一個參數點；
- 沒有排除等價繞路；
- obstruction 沒有被重現。

這些最多是：

$$
\text{execution failure}.
$$

不是：

$$
\text{mathematical no-go}.
$$

## 8.4 負結果分級

可定義：

$$
N_0:
\text{unexplained failure},
$$

$$
N_1:
\text{reproducible local failure},
$$

$$
N_2:
\text{identified obstruction},
$$

$$
N_3:
\text{proved no-go under explicit assumptions},
$$

$$
N_4:
\text{method-family no-go over a defined class}.
$$

coverage weight 應隨級別增加，但仍只在其適用域內成立。

---

# 9. 路由圖：邏輯空間積分的離散骨架

## 9.1 proof-route graph

定義：

$$
G_N
=
(V_N,E_N).
$$

其中 node 可包括：

$$
V_N
=
V^{claim}
\cup
V^{lemma}
\cup
V^{repr}
\cup
V^{obs}
\cup
V^{status}.
$$

edge 可包括：

$$
E_N
=
E^{depends}
\cup
E^{transforms}
\cup
E^{supports}
\cup
E^{contradicts}
\cup
E^{revisits}
\cup
E^{converges}.
$$

## 9.2 Hyperedge 比普通 edge 更自然

很多 proof step 不是：

$$
x\rightarrow y.
$$

而是：

$$
(x_1,x_2,\ldots,x_k)
\Rightarrow y.
$$

因此更一般地應使用 hypergraph：

$$
\mathcal G_N
=(V_N,\mathcal E_N).
$$

其中：

$$
e
=
(
\{x_1,\ldots,x_k\},
y,
method,
verification
).
$$

## 9.3 路徑不是證明

一條 graph path：

$$
p=(v_0,e_1,v_1,\ldots,v_m)
$$

只表示研究路由。

只有當：

- 所有 required premise 合法；
- inference verified；
- statement fidelity 已確認；
- terminal node 等於 target；

才可稱為正式 proof path。

所以：

$$
\boxed{
\text{route graph}
\neq
\text{proof certificate}.
}
$$

## 9.4 Graph coverage

可以定義局部：

$$
C_G(N;U)
=
\frac{|V_N\cap U|}{|U|},
$$

前提是 $U$ 為有限已知 benchmark subgraph。

對未知開放研究空間，則只報：

$$
|V_N^{uniq}|,
\quad
|E_N^{uniq}|,
\quad
\operatorname{components}(G_N),
\quad
\operatorname{cycle}(G_N),
\quad
\operatorname{confluence}(G_N).
$$

---

# 10. 局部盆地與局部積分

## 10.1 proof basin

定義一個研究盆地：

$$
B_i
\subseteq
\bar\Omega_R
$$

若其內部 states 在：

- 方法；
- representation；
- obstruction；
- dependency；
- proof skeleton；

上具有高內部耦合。

## 10.2 basin coverage

若 $B_i$ 已有有限 canonical map：

$$
C_N(B_i)
=
\frac{|V_N\cap B_i|}{|B_i|}.
$$

若 $|B_i|$ 仍未知，可以用：

$$
\widetilde C_N(B_i)
=
(
|V_N\cap B_i|,
|E_N\cap B_i|,
|\mathcal O_N\cap B_i|,
\rho_N^{revisit}(B_i)
).
$$

## 10.3 局部飽和不等於全域飽和

可能存在：

$$
\Delta\widetilde I_N(B_1)
\rightarrow0,
$$

但是：

$$
\Delta\widetilde I_N(B_2)
>0.
$$

所以：

$$
\boxed{
\text{local saturation}
\not\Rightarrow
\text{global saturation}.
}
$$

這是本文與後續第五篇的核心橋樑。

## 10.4 Representation escape

如果：

$$
B_i\subset L_1
$$

已高度飽和，新的表示 $L_2$ 可能建立：

$$
T:L_1\rightarrow L_2
$$

並使：

$$
\Delta I_N(B_i;L_2)
\gg0.
$$

因此 saturation detector 應輸出：

> Current basin under current representation saturated.

而不是：

> Problem saturated.

---

# 11. Novelty 不是 Coverage，但可以作為增量訊號

## 11.1 textual novelty 的危險

文本向量距離：

$$
1-\operatorname{sim}_{text}(x_i,x_j)
$$

只能反映表述差異。

不能直接當：

$$
\Delta I.
$$

## 11.2 semantic route novelty

更合理：

$$
\nu_N^{route}
=
1-
\max_{j\in W_N}
\operatorname{sim}_{route}(r_N,r_j),
$$

其中 $W_N$ 是固定大小的回看窗。

固定窗口非常重要。

如果使用全部歷史：

$$
\nu_N
=
1-
\max_{j<N}\operatorname{sim}(x_N,x_j),
$$

則隨著 $N$ 增加，可比較樣本天然變多，最大相似度會機械性上升。

這會產生假 saturation。

## 11.3 fixed-window estimator

令窗口：

$$
W_N
=
\{N-w,\ldots,N-1\}.
$$

定義：

$$
\nu_N^{(w)}
=
1-
\max_{j\in W_N}
\operatorname{sim}_{sem}(x_N,x_j).
$$

再和 random permutation baseline 比較。

## 11.4 novelty decay 的弱結論

如果：

$$
\nu_N^{(w)}\downarrow
$$

只能先說：

> 在目前 representation 與 similarity metric 下，新 artifact 與最近歷史越來越相似。

不能直接說：

$$
\Omega\text{ 已耗盡}.
$$

更不能說：

$$
Q\text{ 不可證}.
$$

---

# 12. 邏輯空間積分的多階結構

## 12.1 一階積分

一階採樣 states：

$$
\Omega^{(0)}.
$$

積分：

$$
I_N^{(0)}
=
\int_{\Omega^{(0)}}c_N^{(0)}(x)d\mu_0(x).
$$

## 12.2 二階積分

採樣 transitions / proof moves：

$$
\Omega^{(1)}.
$$

$$
I_N^{(1)}
=
\int_{\Omega^{(1)}}c_N^{(1)}(T)d\mu_1(T).
$$

## 12.3 三階積分

研究 route relations：

$$
\Omega^{(2)}.
$$

例如：

$$
T_a\sim T_b,
$$

或：

$$
T_a,T_b,T_c\rightarrow O.
$$

定義：

$$
I_N^{(2)}
=
\int_{\Omega^{(2)}}c_N^{(2)}(R)d\mu_2(R).
$$

## 12.4 X 階

一般：

$$
I_N^{(k)}
=
\int_{\Omega^{(k)}}c_N^{(k)}(\xi)d\mu_k(\xi).
$$

因此完整研究狀態不是單一 $I_N$，而是：

$$
\mathbf I_N
=
(
I_N^{(0)},
I_N^{(1)},
I_N^{(2)},
\ldots
).
$$

這為第四篇「高階證明空間採樣」預留正式接口。

---

# 13. Search Progress 與 Coverage：從 LeanProgress 到全域研究歷史

## 13.1 proof progress 的局部形式

LeanProgress 類工作把 theorem proving 視為狀態轉移：

$$
s_0
\xrightarrow{a_1}
s_1
\xrightarrow{a_2}
\cdots
\xrightarrow{a_T}
s_T.
$$

並估計：

$$
\hat d(s_t)
\approx
\text{remaining proof steps}.
$$

這是一種：

$$
\boxed{
\text{trajectory-aware progress}
}
$$

而不是只預測下一 tactic。

## 13.2 進度不等於覆蓋

但是：

$$
\hat d(s_t)
$$

和：

$$
I_N
$$

回答不同問題。

$\hat d$ 問：

> 這條 route 距離 closure 還多遠？

$I_N$ 問：

> 整個研究制度已經走過哪些區域？

因此：

$$
\boxed{
\text{distance-to-proof}
\neq
\text{coverage-of-research-space}.
}
$$

## 13.3 二者應聯合

可以建立狀態：

$$
Z_N
=
(
\hat d_N,
\mathbf C_N,
\eta_N
).
$$

這比單一 success probability 更適合長程研究管理。

---

# 14. Tree Search 文獻與「積分」觀點

## 14.1 BFS-Prover

BFS-Prover 把 formal theorem proving 明確視為大型 proof-search tree 的導航問題。

其核心工程事實是：

$$
\text{proof success}
$$

依賴：

- node expansion；
- search policy；
- preference learning；
- depth encouragement；
- compiler feedback。

這與本文一致：

> proof 不是憑空出現，而是 search regime 對 tree / graph 的取樣結果。

## 14.2 TreeThink

2026 年 TreeThink 更直接把 theorem-proving tree search 模組化，允許比較不同搜索策略。

這說明：

$$
\Sigma
$$

本身就是研究變數。

因此同一模型、同一 verifier、同一 theorem，只改：

$$
\Sigma_1\rightarrow\Sigma_2
$$

就可能得到不同 coverage。

## 14.3 AlphaProof

AlphaProof 在 Lean formal environment 中結合 reinforcement learning 與 search，最重要的方法論意義之一是：

$$
\text{verifiable environment}
$$

可以為大規模探索提供可靠回饋。

本文不把這解讀成「搜索越大就一定接近所有真理」，而是：

$$
\boxed{
\text{verification makes large search histories scientifically more usable.}
}
$$

因為一部分 branch 可以被嚴格標記為：

$$
valid / invalid.
$$

---

# 15. 從競賽證明到研究級 proof search

## 15.1 Aristotle 的混合路徑

Aristotle 將：

- Lean proof search；
- informal reasoning；
- lemma generation / formalization；
- geometry solver；

放在同一系統中。

這支持一個重要觀點：

$$
\text{Research Route}
$$

可能跨越多種 representation 與 solver。

因此 coverage 系統不能假設所有 node 都是同質 Lean state。

## 15.2 AlphaProof Nexus 與 open-problem search

2026 年 AlphaProof Nexus 對公開未解問題進行大規模正式 proof search，並使用多 subagents、Lean compiler feedback 與演化式協調。

它直接把：

$$
\text{long-horizon search}
$$

帶到 research-level problem setting。

此時「沒有證出來」的剩餘 artifacts 就更值得保存。

因為它們可能包括：

- formalized lemmas；
- failed subgoals；
- reusable constructions；
- proof search statistics；
- library dependencies。

## 15.3 FormalProofBench 與 MA-ProofBench

2026 年的 FormalProofBench、MA-ProofBench 等 benchmark 把 formal proving 推向 advanced undergraduate / graduate mathematics 與 mathematical analysis。

這些工作揭露：

$$
\text{competition success}
$$

不能直接外推成：

$$
\text{research-level coverage}.
$$

特別是在分析領域，長依賴鏈、Mathlib 熟悉度、statement formalization 與 remaining subgoal discharge 都可能成為獨立瓶頸。

所以 coverage 需要 domain-sensitive normalization。

---

# 16. Premise Retrieval 本身就是 Coverage Operator

## 16.1 知識庫不是被動背景

形式證明中，模型能不能找到合適 premise，直接影響：

$$
\Omega_R^{reach}.
$$

令 retrieval operator：

$$
\mathcal R_k(s)
=
\{p_1,\ldots,p_k\}.
$$

不同 retrieval policy：

$$
\mathcal R^{(1)}
\neq
\mathcal R^{(2)}
$$

會改變下一步可達 states。

## 16.2 LeanSearch 類系統的意義

Global premise retrieval / LeanSearch 類工作顯示，大型 Mathlib 搜索本身是 theorem proving 的核心能力。

因此：

$$
\mathcal K
$$

和：

$$
\operatorname{Access}(\mathcal K)
$$

必須分開。

知識存在，不代表 agent 可有效調用。

## 16.3 可達空間受檢索界面限制

因此：

$$
\Omega_R^{reach}
=
F(
\mathcal A,
\mathcal L,
\mathcal M,
\mathcal V,
B,
\mathcal K,
\operatorname{Access}(\mathcal K),
\Sigma
).
$$

這比單純把 $\mathcal K$ 視為「模型知道的東西」更精確。

---

# 17. Theorem Graph 與 Knowledge Graph：Coverage 的跨證明層

## 17.1 theorem dependency graph

TheoremGraph 類工作把 formal / informal mathematical objects 連成圖。

對本文而言，可把：

$$
G^{knowledge}
$$

與：

$$
G^{search}
$$

分離。

$G^{knowledge}$ 表示已有 theorem dependency；

$G^{search}$ 表示目前研究歷史。

## 17.2 兩張圖的交集

定義：

$$
G_N^{align}
=
G_N^{search}
\cap
G^{knowledge}.
$$

這可以觀察：

- agent 是否只在已知 theorem graph 內移動；
- 是否產生新中介節點；
- 是否重建已知結果；
- 是否開啟新的 dependency bridge。

## 17.3 新增 theorem 不等於新增知識島

一個新 theorem：

$$
T_{new}
$$

如果只是：

$$
T_{old}
$$

的弱改寫，其 graph contribution 可能很小。

反之，一個短 bridge lemma：

$$
L^\star
$$

若連接兩個長期分離 components：

$$
C_1
\leftrightarrow
C_2,
$$

其 coverage impact 可能巨大。

因此應考慮：

$$
\Delta connectivity,
$$

而不只 theorem count。

---

# 18. 自主 theorem discovery 與「搜尋本身生成知識」

## 18.1 proof search 不一定只服務單一 target

2026 年 self-supervised theorem discovery 類研究顯示，形式 proof search 可以在公理系統中產生可驗證的新 theorem。

這表示：

$$
\text{Search}(Q)
$$

可能副產生：

$$
\{T_1,T_2,\ldots,T_m\}.
$$

其中並非所有 $T_i$ 都是 $Q$ 最終 proof 的必要步驟。

## 18.2 研究積分的生成版本

因此定義：

$$
\operatorname{Gen}_N
=
\{T_i:\mathcal V(T_i)=1\}.
$$

並考察：

$$
G_N^{new}
=
|\operatorname{Gen}_N\setminus\mathcal K_0|.
$$

若能判定 theorem 不只是資料庫重複，就可能形成：

$$
\boxed{
\text{search-generated knowledge gain}.
}
$$

## 18.3 這和最終 proof 成功可分離

可能：

$$
S(Q)=0
$$

但：

$$
G_N^{new}>0.
$$

這是長程 AI 數學研究與單次 benchmark 最大差別之一。

---

# 19. NS-203：第一個長程案例的 Coverage 解讀

## 19.1 語料地位

本文使用一個內部長程 Navier--Stokes 研究 corpus 作原型案例。

在保守排除：

- README；
- CHANGELOG；
- roadmap；
- handoff；
- checkpoint；
- audit；

等非 paper-like artifacts 後，第一輪 observatory 得到：

$$
203
$$

份 NS paper-like artifacts。

注意：

$$
203
$$

不是 203 個獨立 theorem。

更不是 203 條互不等價 proof route。

## 19.2 已建立的離散圖

第一輪 extraction 得到：

$$
189
$$

條 sequence edges；

$$
390
$$

條 explicit dependency edges；

$$
258
$$

條 revisit-similarity edges。

這些數字描述的是：

$$
G_N^{search},
$$

不是 NS 數學真實證明空間。

## 19.3 局部 higher-order 訊號

語料中可觀察到：

- obstruction confluence；
- coupled confluence；
- recurrence；
- all-order route escalation；
- second-order residue；
- route feedback。

因此某些 basin 顯示：

$$
\Omega^{(0)}
\rightarrow
\Omega^{(1)}
\rightarrow
\Omega^{(2)}
$$

式的高階再採樣。

但這首先是 corpus-level classification。

不能直接變成 theorem-level 數學階數。

## 19.4 固定窗口 novelty 的重要負結果

初始 cumulative nearest-neighbor similarity 看起來像 novelty 下降。

但 cumulative estimator 有天然 bias：

$$
\max_{j<i}
\operatorname{sim}(x_i,x_j)
$$

隨歷史池增加容易上升。

改成固定窗口後，第一輪分析並未支持全 corpus 已出現顯著 global novelty collapse。

所以現在最保守結論是：

$$
\boxed{
\text{some basins show high recurrence, while global novelty remains open.}
}
$$

## 19.5 這恰好是 coverage framework 的用途

如果只有：

$$
S(NS)=0,
$$

我們只知道「沒有最終 proof」。

加入 coverage 後，可以說：

- 某些 route family 已密集採樣；
- 某些 obstruction 有高 confluence；
- 某些 representation 仍有新增資訊；
- 某些 higher-order relations 開始出現；
- global saturation 未被證成。

這是一個嚴格更豐富、但仍不越權的描述。

---

# 20. Coverage 不能回答什麼

## 20.1 不能判定命題真假

即使：

$$
\Delta I_N\rightarrow0,
$$

也不能推出：

$$
Q=false.
$$

## 20.2 不能判定不可證

不能推出：

$$
\nexists\pi.
$$

因為可能只是：

$$
\pi
\notin
\Omega_R^{reach}.
$$

## 20.3 不能判定 framing 錯誤

即使所有已知 route 反覆匯流，也可能只是：

- 方法族不足；
- representation 太窄；
- intelligence 不足；
- resource bound 太小；
- proof 極長；
- 關鍵 lemma 尚不存在。

所以：

$$
\boxed{
\text{high coverage under }R
\not\Rightarrow
\text{misframed}(Q).
}
$$

## 20.4 不能把 observation denominator 當真實 denominator

若觀測到：

$$
80\%
$$

已知 route family 被採樣，最多只能說：

> 在目前 catalog 中採樣了 $80\%$。

不能說：

> 採樣了宇宙中 $80\%$ 的可能證明。

---

# 21. Relative Coverage：未知分母時真正能報什麼

## 21.1 catalog-relative coverage

假設當前建立候選 catalog：

$$
\mathcal C_t
=
\{c_1,\ldots,c_m\}.
$$

可定義：

$$
C_N^{catalog}
=
\frac{|\mathcal C_N^{sampled}|}{|\mathcal C_t|}.
$$

必須明示：

$$
\mathcal C_t
$$

是動態、可擴張 catalog。

## 21.2 window-relative coverage

對固定最近窗口：

$$
W=[N-w,N],
$$

可計算：

$$
C_W^{new}
=
\frac{\#\text{new canonical classes in }W}{w}.
$$

這其實更接近 novelty rate。

## 21.3 basin-relative coverage

如果某 basin 有有限 decomposition：

$$
B_i
=
\bigsqcup_{j=1}^{m_i}b_{ij},
$$

可計算：

$$
C_N(B_i)
=
\frac{\#\{b_{ij}\text{ audited}\}}{m_i}.
$$

這種局部 coverage 比全域百分比可信得多。

## 21.4 benchmark-relative coverage

在明確 benchmark：

$$
\mathcal B
=
\{Q_1,\ldots,Q_n\}
$$

中，coverage 可合法寫為：

$$
C^{bench}
=
\frac{\#\text{solved}}{n}.
$$

但 benchmark success 不等於研究空間 coverage。

兩者應分開。

---

# 22. Coverage Density 與過度採樣

## 22.1 density

對局部區域 $U$，定義訪問密度：

$$
d_N(U)
=
\frac{\#\text{visits to }U}{\mu_U(U)}.
$$

如果 $\mu_U$ 未知，可使用 normalized local count。

## 22.2 oversampling

當：

$$
d_N(U)\gg d_N(V)
$$

但：

$$
\Delta I_N(U)\approx0,
$$

則 $U$ 可能被過度採樣。

定義 oversampling score：

$$
O_N(U)
=
\frac{Visit_N(U)}{\epsilon+\Delta\widetilde I_N(U)}.
$$

$O_N(U)$ 高意味：

> 花很多研究成本，但新資訊很少。

## 22.3 調度策略

因此 scheduler 可以：

$$
\Sigma_{N+1}
=
\operatorname{Reweight}(
\Sigma_N,
O_N,
\eta_N,
\mathbf C_N
).
$$

即：

- 降低過度採樣 basin；
- 提高低 coverage representation；
- 啟動 independent verification；
- 尋找新的 method family。

---

# 23. Coverage Frontier

## 23.1 定義 frontier

令已觀測區域：

$$
\Omega_N^{obs}.
$$

frontier 可定義為：

$$
\partial\Omega_N^{obs}
=
\{x\in\Omega_N^{obs}:\exists y\notin\Omega_N^{obs},\ x\rightarrow y\text{ plausible}\}.
$$

它表示：

> 已知與未知的可操作邊界。

## 23.2 frontier quality

好的 frontier node 應具有：

- 高可驗證性；
- 高分支潛力；
- 與既有 obstruction 不同；
- 低 representation redundancy；
- 足夠 domain relevance。

可定義 heuristic：

$$
F_N(x)
=
\alpha Novelty(x)
+
\beta Verify(x)
+
\gamma Branch(x)
-
\delta Redundancy(x).
$$

## 23.3 frontier 比「再寫一篇」更重要

長程 AI 研究若沒有 frontier management，就容易：

$$
\text{paper generation}
\rightarrow
\text{local repetition}.
$$

因此每輪應輸出：

$$
\boxed{
\text{current frontier set}
}
$$

而不是只輸出最新 artifact。

---

# 24. Coverage 與 Compression 的對偶

## 24.1 探索後必須壓縮

若研究歷史長度：

$$
N\rightarrow10^4,
$$

不可能每次把所有原始文本重新讀一遍。

因此需要 compression：

$$
\mathcal H_N
\rightarrow
\mathcal S_N.
$$

其中 $\mathcal S_N$ 至少保存：

- canonical claims；
- proof dependencies；
- verified lemmas；
- obstruction IDs；
- unresolved frontiers；
- representation history；
- provenance。

## 24.2 壓縮不能抹掉差異

如果：

$$
Compress(x_1)=Compress(x_2)
$$

但：

$$
x_1\not\sim x_2,
$$

則 coverage estimator 會錯誤低估研究空間。

相反，如果：

$$
x_1\sim x_2
$$

卻被保存為完全不同 nodes，則會高估 coverage。

所以：

$$
\boxed{
\text{coverage quality depends on compression fidelity.}
}
$$

## 24.3 可逆 provenance

每個 compressed node 應能回指：

$$
node\_id
\rightarrow
\{artifact\_ids\}
\rightarrow
\{source\_ranges\}.
$$

否則不能 audit。

---

# 25. 動態積分：研究空間會自己改變

## 25.1 固定 $\Omega$ 是理想化

真正研究中：

- 新 theorem 出現；
- 新 tool 加入；
- 新 representation 被發明；
- 新 benchmark 被建立；
- 舊 obstruction 被修正；
- 公理背景可能改變。

因此：

$$
\Omega_R(t)
$$

是時間依賴的。

## 25.2 moving domain integral

更一般：

$$
I(t)
=
\int_{\bar\Omega_R(t)}
c(t,\omega)d\mu_t(\omega).
$$

因此：

$$
\frac{dI}{dt}
$$

同時受到：

1. coverage 增加；
2. domain 擴張；
3. measure 重新定義；
4. equivalence relation 更新；

影響。

## 25.3 coverage 下降不一定退步

如果新 representation 讓 domain 擴張：

$$
\Omega_R(t+1)
\supset
\Omega_R(t),
$$

即使已知內容不減少，normalized coverage ratio 也可能下降。

這不代表退步。

反而可能代表：

$$
\boxed{
\text{the system discovered that the search space is larger than previously modeled.}
}
$$

這本身是重要知識。

---

# 26. Logic-Space Reynolds Transport 類比

## 26.1 類比而非物理同一

為了處理 moving domain，可借用 transport theorem 的形式類比。

若：

$$
I(t)
=
\int_{\Omega(t)}c(t,\omega)d\mu_t,
$$

概念上可拆：

$$
\frac{dI}{dt}
=
\text{internal coverage gain}
+
\text{domain-boundary motion}
+
\text{measure update}.
$$

本文不宣稱 proof space 真的是物理流體。

這只是 bookkeeping analogy。

## 26.2 三種研究增長

可寫：

$$
\Delta I
=
\Delta I_{explore}
+
\Delta I_{expand}
+
\Delta I_{reclassify}.
$$

其中：

- $\Delta I_{explore}$：探索原本已定義區域；
- $\Delta I_{expand}$：發現新區域；
- $\Delta I_{reclassify}$：改進 canonicalization / equivalence 後重估。

這三者應分開報告。

---

# 27. Saturation Detector 必須是統計程序，不是感覺

## 27.1 最低要求

要宣稱某 basin 接近 saturation，至少要看到：

$$
\Delta V_N^{uniq}\downarrow,
$$

$$
\Delta E_N^{uniq}\downarrow,
$$

$$
\Delta\mathcal O_N\downarrow,
$$

同時：

$$
Revisit_N\uparrow.
$$

最好還要：

$$
CrossMethodConfluence_N\uparrow.
$$

## 27.2 不能只用文本相似度

需要至少三組特徵：

$$
F_{text},
\quad
F_{symbol},
\quad
F_{route}.
$$

更好再加入：

$$
F_{obstruction}.
$$

## 27.3 baseline

必須和：

- random permutation；
- shuffled series order；
- synthetic duplication；
- known non-saturated corpus；

比較。

如果 estimator 對所有長 corpus 都自動顯示下降，則它不能證明 saturation。

## 27.4 regime-change test

若改變：

$$
R_1\rightarrow R_2
$$

之後 novelty 重新上升：

$$
\Delta I_N(R_2)
\gg
\Delta I_N(R_1),
$$

則舊 saturation 更可能是：

$$
\text{regime-local saturation}.
$$

---

# 28. 邏輯空間積分的最小實驗協議

## 28.1 輸入

研究系統至少需要：

```text
problem_id
formal_or_informal_statement
axiom_background
representation
method_family
verification_channels
resource_budget
artifact_history
```

## 28.2 每輪輸出 schema

```text
run_id
parent_state_ids
claim_ids
assumption_ids
method_ids
representation_id
result_ids
obstruction_ids
verification_state
cost
provenance
```

## 28.3 canonicalization

每輪先做：

```text
Normalize symbols
Resolve aliases
Extract claims
Extract dependencies
Map obstruction candidates
Map method family
Compare prior canonical nodes
```

## 28.4 更新圖

$$
G_{N+1}
=
Update(G_N,e_{N+1}).
$$

## 28.5 計算相對量

至少輸出：

$$
\Delta V_N^{uniq},
$$

$$
\Delta E_N^{uniq},
$$

$$
\Delta O_N^{uniq},
$$

$$
\nu_N^{(w)},
$$

$$
\eta_N,
$$

$$
\rho_N^{revisit}.
$$

## 28.6 更新 frontier

$$
\mathcal F_{N+1}
=
Frontier(G_{N+1}).
$$

然後 scheduler 選擇下一輪：

$$
a_{N+1}
=
\Sigma(
\mathcal F_{N+1},
\mathbf C_N,
\eta_N,
O_N
).
$$

---

# 29. 可執行的 Pseudocode

```text
initialize Graph G
initialize Catalog C
initialize ObstructionRegistry O
initialize Frontier F

for run in research_runs:
    artifact = execute(run)

    parsed = extract(
        claims,
        assumptions,
        methods,
        representations,
        dependencies,
        obstructions,
        verification,
        provenance
    )

    canonical = semantic_normalize(parsed)
    matches = retrieve_equivalent_prior_nodes(canonical, G)

    if matches are high-confidence equivalent:
        update_revisit_edges(G, canonical, matches)
    else:
        add_new_nodes(G, canonical)

    add_dependency_edges(G, canonical)
    add_verification_state(G, canonical)
    update_obstruction_registry(O, canonical)

    metrics = compute(
        new_state_count,
        new_route_count,
        obstruction_gain,
        fixed_window_novelty,
        revisit_rate,
        confluence,
        verification_gain,
        marginal_research_yield
    )

    F = update_frontier(G, O, metrics)
    next_run = scheduler(F, metrics)
```

這個流程最重要的不是演算法細節，而是資料結構要求：

$$
\boxed{
\text{每一輪生成必須留下可比較、可驗證、可回指的痕跡。}
}
$$

---

# 30. Falsifiable Predictions

本文不是只提出詞彙。

它應該能產生可被反駁的觀察命題。

## 30.1 P1：固定制度下局部邊際收益可衰減

若 basin $B$ 在固定 $R$ 下長期被重複採樣，則可能觀察：

$$
E[\eta_N\mid B,R]
\downarrow.
$$

若始終沒有下降，則「局部飽和」假說受到削弱。

## 30.2 P2：制度切換可重置 novelty

若飽和主要由表示或方法限制引起，改變：

$$
R_1\rightarrow R_2
$$

後應有：

$$
E[\nu_N\mid R_2]
>
E[\nu_N\mid R_1]
$$

至少在初始窗口成立。

## 30.3 P3：真正 obstruction 應跨表述重現

若 $O$ 是結構性 obstruction，而非 wording artifact，則在語義等價表示間：

$$
L_1\sim L_2
$$

應保有某種：

$$
O(L_1)
\leftrightarrow
O(L_2).
$$

若完全消失，可能表示原 obstruction 只是 representation artifact。

## 30.4 P4：verified coverage 比 textual novelty 更穩定

真正累積的已驗證節點：

$$
C_N^{ver}
$$

應比純 textual novelty 對 prompt wording 更不敏感。

如果相反，則 canonicalization 或 verification architecture 有問題。

## 30.5 P5：高品質負結果應降低 future duplication

當 no-go registry 成熟：

$$
|\mathcal O_N|
\uparrow
$$

且 scheduler 真的使用它時，應看到：

$$
DuplicateFailedRoutes_N
\downarrow.
$$

如果沒有，代表 research memory 沒有真正進入決策閉環。

---

# 31. 三種積分不能混淆

## 31.1 探索積分

$$
I_N^{explore}
$$

表示研究到訪量。

## 31.2 驗證積分

$$
I_N^{verify}
$$

表示被足夠驗證的研究量。

## 31.3 排除積分

$$
I_N^{exclude}
$$

表示被可靠 no-go 排除的候選區域。

因此：

$$
\boxed{
I_N^{explore}
\neq
I_N^{verify}
\neq
I_N^{exclude}.
}
$$

一個成熟 observatory 應至少同時追蹤三者。

---

# 32. Coverage Conservation 不成立

## 32.1 知識不是固定體積流體

不能假設：

$$
I^{known}+I^{unknown}=1
$$

永遠有固定分母。

因為：

$$
\Omega(t)
$$

會擴張。

## 32.2 新定義可能增加未知量

當發現新的 structure：

$$
S_{new},
$$

可能同時增加：

$$
Known\uparrow
$$

與：

$$
Unknown\uparrow.
$$

這是數學研究常見現象。

因此「知道越多，未知越少」不是單調律。

## 32.3 更合理的更新

$$
K_{N+1}
=
K_N+\Delta K_N,
$$

$$
U_{N+1}
=
U_N-\Delta K_N+\Delta U_N^{new}.
$$

其中：

$$
\Delta U_N^{new}
$$

是新研究開啟的未知空間。

---

# 33. Coverage 與「越是真理越可能像廢話」的接口

## 33.1 本篇暫不證明真理—生成性反轉

後續第七篇將研究：

$$
\text{Truth / Fidelity / Generativity}
$$

是否存在非單調關係。

本篇只建立必要的測量語言。

## 33.2 極端閉合的直觀

若某局部問題被約束到：

$$
|\Omega^{surv}|
\rightarrow1,
$$

則剩餘結論可能表面非常簡單。

但是：

$$
\text{simple endpoint}
$$

不代表：

$$
\text{simple derivational history}.
$$

因此 coverage history 可以保存：

> 為什麼最後只剩這個看似「廢話」的結果。

這正是只保存最終 theorem statement 會丟失的部分。

---

# 34. Coverage 與 Productive Mis-specification 的接口

## 34.1 父問題錯誤不是本文前提

本文不假設：

$$
Q\text{ is misframed}.
$$

## 34.2 但 coverage 能觀察 descendant production

若研究 $Q$ 的過程中產生：

$$
\{T_1,T_2,\ldots,T_m\},
$$

可測：

$$
G_N(Q)
=
\#\{T_i:\text{independently reusable}\}.
$$

這和 $Q$ 最終真假可以分離。

## 34.3 後續問題

第八、九篇將問：

$$
G_N(Q)
$$

是否可能在某些定義偏差下反而增加。

本篇只提供：

$$
\boxed{
\text{generativity can be measured separately from proof success.}
}
$$

---

# 35. 研究治理：何時應繼續，何時應換空間

## 35.1 四種狀態

可建立簡化矩陣。

### A. 高 novelty、高 verification gain

$$
\nu_N\uparrow,
\quad
\Delta C_N^{ver}\uparrow.
$$

策略：

> 繼續深入。

### B. 高 novelty、低 verification gain

$$
\nu_N\uparrow,
\quad
\Delta C_N^{ver}\approx0.
$$

策略：

> 強化驗證，不要只增加生成。

### C. 低 novelty、高 verification gain

$$
\nu_N\downarrow,
\quad
\Delta C_N^{ver}>0.
$$

策略：

> 可能正在收斂與清理舊空間，不應誤判為停滯。

### D. 低 novelty、低 verification gain

$$
\nu_N\downarrow,
\quad
\Delta C_N^{ver}\approx0.
$$

策略：

> 啟動 regime audit：representation、method、retrieval、resource、problem decomposition。

## 35.2 這不是自動宣告問題錯誤

即使 D 長期成立，輸出也只能是：

$$
\boxed{
\text{Current research regime has low marginal yield.}
}
$$

不能輸出：

$$
\boxed{
Q\text{ is wrong}.
}
$$

---

# 36. Proof-Space Observatory 的最低儀表板

一個真正的研究觀測站，最低應顯示：

## 36.1 Corpus

$$
N_{artifact},
\quad
N_{canonical},
\quad
N_{verified}.
$$

## 36.2 Graph

$$
|V|,
\quad
|E|,
\quad
components,
\quad
cycles.
$$

## 36.3 Novelty

$$
\nu_N^{text},
\quad
\nu_N^{symbol},
\quad
\nu_N^{route}.
$$

## 36.4 Revisit

$$
\rho_N^{revisit}.
$$

## 36.5 Obstruction

$$
|\mathcal O_N|,
\quad
m_N(O_i),
\quad
\kappa_N(O_i).
$$

## 36.6 Verification

$$
C_N^{ver}
$$

及各級 verification breakdown。

## 36.7 Frontier

$$
|\mathcal F_N|.
$$

## 36.8 Cost

$$
\eta_N.
$$

這組儀表板比「今天又寫了幾篇 paper」更接近研究狀態。

---

# 37. 失敗模式目錄

## 37.1 Fake Coverage Inflation

大量改寫同一內容：

$$
N_{artifact}\uparrow
$$

但：

$$
N_{canonical}\approx const.
$$

## 37.2 Verification Laundering

把：

$$
\text{compiler success}
$$

冒充：

$$
\text{semantic correctness}.
$$

## 37.3 Obstruction Overgeneralization

局部 no-go：

$$
R_a\text{ fails under }H_a
$$

被錯寫成：

$$
Q\text{ impossible}.
$$

## 37.4 Basin Blindness

在 $B_1$ 飽和後一直重跑，卻沒有探索：

$$
B_2,B_3,\ldots
$$

## 37.5 Representation Lock-in

把：

$$
L_1
$$

誤認為：

$$
\text{the problem itself}.
$$

## 37.6 Unknown Denominator Fraud

在不知道 $|\Omega|$ 時仍報：

$$
93\%\text{ explored}.
$$

這在真正開放問題中通常不可接受。

## 37.7 History Erasure

只保存 final paper，不保存：

- failed routes；
- no-go assumptions；
- rejected reformulations；
- verification state。

結果未來 AI 再次重跑同一失敗。

---

# 38. 與傳統 Proof Complexity 的區別

## 38.1 Proof complexity 問什麼

傳統 proof complexity 可研究：

- proof length；
- proof system strength；
- lower bound；
- simulation between proof systems。

這些是高度嚴格的數學領域。

## 38.2 本文問什麼

本文主要問：

> 一個實際 AI research regime 如何在歷史中探索、記錄、驗證與重訪 proof-related states？

所以：

$$
\text{Logic-Space Integration}
\neq
\text{Classical Proof Complexity}.
$$

## 38.3 兩者可接合

如果某 formal domain 已知 proof complexity bound，則它可以提供：

$$
\mu
$$

或：

$$
Cost(\omega)
$$

的更嚴格結構。

但本文不假設所有研究問題都有此條件。

---

# 39. 與 Information Theory 的區別

## 39.1 不是直接把 entropy 套上去

本文使用：

$$
H(\Omega)
$$

時，只能在已定義概率或權重模型時當正式 entropy。

否則「熵」應被視為類比詞。

## 39.2 coverage measure 比 entropy 更原始

我們首先需要：

$$
\Omega,
\quad
\sim,
\quad
\mu,
\quad
c_N.
$$

然後才能討論：

$$
H.
$$

不應反過來先宣布：

> proof space entropy 下降。

卻沒有定義 sample space。

## 39.3 資訊增量的保守用法

若建立 probabilistic model：

$$
P_N(H_i),
$$

某新結果 $E$ 可定義 information gain：

$$
IG(E)
=
D_{KL}(P_{N+1}\|P_N).
$$

但這是 hypothesis-space information gain，和 coverage integral 是不同量。

---

# 40. 與 Bayesian Search 的接口

## 40.1 hypothesis weights

若候選機制：

$$
\mathcal H
=
\{H_1,\ldots,H_m\},
$$

可維持：

$$
P_N(H_i).
$$

## 40.2 coverage 和 posterior 分離

高 coverage：

$$
C_N(H_i)\uparrow
$$

只表示該 hypothesis family 被充分測試。

不表示：

$$
P_N(H_i)\uparrow.
$$

如果負證據多，反而可能：

$$
C_N(H_i)\uparrow,
\quad
P_N(H_i)\downarrow.
$$

這個分離非常重要。

## 40.3 最好的研究狀態可能是「高 coverage、低 posterior」

這代表：

> 我們非常確定這條方法族不值得繼續。

這不是浪費。

它是 routing knowledge。

---

# 41. Multi-Agent Coverage

## 41.1 多 agent 不等於多 coverage

假設：

$$
A_1,\ldots,A_m
$$

全部使用同一模型、同一 prompt、同一 retrieval、同一 temperature。

則：

$$
Coverage(A_1\cup\cdots\cup A_m)
$$

可能只比單 agent 稍高。

## 41.2 異質性

應考慮 agent diversity：

$$
D_A
=
f(
model,
prompt,
representation,
method,
retrieval,
verifier
).
$$

理想上：

$$
D_A\uparrow
$$

可增加獨立 basin 採樣機會。

但仍不保證：

$$
Truth\uparrow.
$$

## 41.3 union coverage

多 agent 聯合觀測：

$$
\Omega_N^{obs,union}
=
\bigcup_{i=1}^{m}
\Omega_{N,i}^{obs}.
$$

重疊：

$$
\Omega_{N,i}^{obs}
\cap
\Omega_{N,j}^{obs}
$$

則可用來測：

- convergence；
- reproducibility；
- redundancy。

---

# 42. Human-in-the-Loop Coverage

## 42.1 人類不只是 final judge

人類可以參與：

- 定義 basin；
- 判定 semantic equivalence；
- 確認 statement fidelity；
- 評估 method-family boundaries；
- 決定何時換 representation；
- 審計 false confluence。

## 42.2 human cost 必須記錄

如果一個系統需要巨大人工修復：

$$
C_{human}\gg0,
$$

其：

$$
\eta_N
$$

可能低於表面自動化率所暗示。

## 42.3 人類共識不是 truth oracle

即使多人同意：

$$
Consensus(Q)=1
$$

也不代表：

$$
T(Q)=1.
$$

所以 human verification 也必須記錄方法與證據，而不是只存 vote。

---

# 43. Research Memory 的兩層架構

## 43.1 Verified Fact Layer

保存：

$$
\mathcal K_N^{ver}
=
\{T_i:V(T_i)\ge\theta\}.
$$

要求：

- proof / evidence；
- provenance；
- dependencies；
- version；
- semantic statement。

## 43.2 Exploratory Memory Layer

保存：

$$
\mathcal M_N^{exp}.
$$

包括：

- failed routes；
- heuristic；
- partial proof；
- rejected idea；
- speculative bridge；
- negative experiment。

## 43.3 不可混淆

$$
\mathcal K_N^{ver}
\cap
\mathcal M_N^{exp}
$$

可以有引用關係，但 status 必須分離。

否則長期運行後最危險的事情是：

$$
\text{speculation}
\rightarrow
\text{memory}
\rightarrow
\text{recalled as fact}.
$$

---

# 44. Research Ledger：每一輪必須可追溯

## 44.1 Ledger entry

每一輪：

$$
L_i
=
(
id,
parent,
input,
transform,
output,
verify,
cost,
provenance
).
$$

## 44.2 不可靜默覆蓋

若 artifact 更新：

$$
a^{(1)}\rightarrow a^{(2)},
$$

必須保留：

$$
Diff(a^{(1)},a^{(2)}).
$$

否則 retrospective coverage analysis 不可靠。

## 44.3 Canonical source 與 rendering 分離

正式數學 source 應保存 canonical representation。

渲染畫面不是唯一來源。

這不只是出版工程問題，也直接影響：

$$
\text{semantic comparison}
$$

與：

$$
\text{route reconstruction}.
$$

---

# 45. Coverage-Aware Research Scheduler

## 45.1 傳統 scheduler

可能只最大化：

$$
P(\text{solve next}).
$$

## 45.2 coverage-aware scheduler

本文提出：

$$
Score(a)
=
\alpha P_{solve}(a)
+
\beta E[\Delta I\mid a]
+
\gamma E[\Delta C^{ver}\mid a]
-
\delta Cost(a)
-
\lambda Redundancy(a).
$$

## 45.3 這允許有意義的探索

某 action：

$$
a^\star
$$

即使短期：

$$
P_{solve}(a^\star)\approx0,
$$

但若：

$$
E[\Delta I\mid a^\star]\gg0,
$$

仍值得執行。

這就是 research 和 benchmark solving 的差異。

---

# 46. Coverage 與 Exploration--Exploitation

## 46.1 exploitation

沿已知 promising route：

$$
Exploit(B_i).
$$

## 46.2 exploration

開啟低採樣 basin：

$$
Explore(B_j).
$$

## 46.3 coverage-aware bandit 類比

可以把 basin 視為 arms：

$$
\{B_1,\ldots,B_m\}.
$$

reward 不只是 solved theorem，而可包括：

$$
r_i
=
\alpha\Delta C^{ver}
+
\beta\Delta C^{obs}
+
\gamma\Delta C^{route}
-
\delta Cost.
$$

本文不宣稱標準 bandit 理論可直接完整描述數學研究。

它只是提供 scheduler design 的可用類比。

---

# 47. Coverage 的尺度依賴

## 47.1 coarse scale

在粗粒度：

$$
\Omega^{coarse}
$$

可能只有：

- energy methods；
- compactness；
- geometric route；
- harmonic analysis。

## 47.2 fine scale

在細粒度：

$$
\Omega^{fine}
$$

可能展成成千上萬 lemma states。

## 47.3 coverage 是 resolution-relative

因此：

$$
C_N
=
C_N(\rho),
$$

其中 $\rho$ 是描述解析度。

粗尺度看：

$$
C_N(\rho_{coarse})\approx1
$$

不代表細尺度：

$$
C_N(\rho_{fine})\approx1.
$$

這將與後續 Reflexive Representation / resolution 問題產生接口。

---

# 48. Coverage 不應追求最大化到無限

## 48.1 研究不是窮舉字串

如果目標是：

$$
\max |\Omega_N^{obs}|,
$$

最容易的方法可能是生成大量低價值變體。

這沒有意義。

## 48.2 應最大化 weighted information gain

更合理：

$$
\max
\sum_{x\in\Delta\Omega_N}
w(x),
$$

其中 $w(x)$ 可依：

- verification；
- novelty；
- transferability；
- obstruction relevance；
- frontier importance；

調整。

## 48.3 最好的研究可能主動停止某 basin

如果：

$$
\eta_N(B_i)\rightarrow0,
$$

理性策略可能是：

$$
Stop(B_i).
$$

這不是證明 basin 沒有解。

只是 resource allocation decision。

---

# 49. 本文核心命題總表

## 命題一：研究量不等於 artifact 數

$$
\boxed{
N_{artifact}\not\equiv C_N.
}
$$

## 命題二：可觀測 coverage 依賴搜尋制度

$$
\boxed{
C_N=C_N(Q,R,\rho,\sim).
}
$$

## 命題三：全域積分通常不可直接觀測

$$
\boxed{
I_N
=
\int_{\bar\Omega_R}c_Nd\mu
}
$$

是理想量；真實研究常只能估局部或相對 coverage。

## 命題四：coverage 必須向量化

$$
\boxed{
\mathbf C_N
=
(C^{state},C^{route},C^{obs},C^{method},C^{repr},C^{ver}).
}
$$

## 命題五：負結果可以增加研究資訊

在明確適用域內：

$$
\boxed{
\text{proved no-go}
\Rightarrow
\text{valid survivor-space reduction}.
}
$$

## 命題六：局部飽和不推出全域飽和

$$
\boxed{
\Delta I(B_i)\rightarrow0
\not\Rightarrow
\Delta I(\Omega)\rightarrow0.
}
$$

## 命題七：低 novelty 不等於命題不可證

$$
\boxed{
\nu_N\downarrow
\not\Rightarrow
\nexists\pi.
}
$$

## 命題八：驗證具有層級與關係結構

$$
\boxed{
\text{compile success}
\not\equiv
\text{semantic fidelity}.
}
$$

## 命題九：邊際研究收益應納入成本

$$
\boxed{
\eta_N
=
\frac{\Delta\widetilde I_N}{Cost_N}.
}
$$

## 命題十：研究制度飽和只是一個制度結論

$$
\boxed{
\text{Saturation}(R)
\not\Rightarrow
\text{Verdict on mathematical reality}.
}
$$

---

# 50. 與系列後續論文的依賴關係

本文建立：

$$
\Omega,
\quad
\bar\Omega,
\quad
c_N,
\quad
I_N,
\quad
\Delta I_N,
\quad
\mathbf C_N,
\quad
\eta_N,
\quad
B_i,
\quad
\partial\Omega_N.
$$

後續：

LSI-PSD-03 將處理：

$$
\boxed{
\Omega/\sim
}
$$

的語義商空間問題。

LSI-PSD-04 將處理：

$$
\Omega^{(0)},\Omega^{(1)},\Omega^{(2)},\ldots
$$

高階採樣。

LSI-PSD-05 將處理：

$$
\boxed{
\text{local saturation / global openness}
}
$$

的盆地結構。

LSI-PSD-06 將建立 obstruction confluence 與 route equivalence。

LSI-PSD-07 至 09 才進入真理、生成性與 productive mis-specification。

LSI-PSD-10 將把本文所有防過度推論規則獨立形式化。

LSI-PSD-12 則把這些量轉成真正 Proof-Space Observatory runtime。

---

# 51. 結論：研究進度不應只問「離答案多遠」

當自動定理證明仍以單一 benchmark 為主時：

$$
\text{Solved / Unsolved}
$$

是合理的核心指標。

但在長程 AI 數學研究中，研究系統還需要知道：

$$
\boxed{
\text{What has been explored?}
}
$$

$$
\boxed{
\text{What has been verified?}
}
$$

$$
\boxed{
\text{What has been ruled out?}
}
$$

$$
\boxed{
\text{What is being revisited?}
}
$$

$$
\boxed{
\text{Where is the current frontier?}
}
$$

$$
\boxed{
\text{How much new information is each additional run producing?}
}
$$

本文將這組問題統一到：

$$
\boxed{
\textbf{Logic-Space Integration}
}
$$

框架。

最理想的形式是：

$$
I_N
=
\int_{\bar\Omega_R(Q)}
c_N(\omega)d\mu(\omega).
$$

但本文拒絕把這個漂亮公式誤用成虛假的全域百分比。

真正可操作的第一步，是建立：

$$
\boxed{
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
)
}
$$

以及：

$$
\boxed{
\Delta I_N,
\quad
\eta_N,
\quad
\rho_N^{revisit},
\quad
\mathcal F_N.
}
$$

這樣，一個沒有得到最終 proof 的研究系統，也不再只能回報：

> 失敗。

它可以更準確地回報：

> 我們在哪些區域投入了多少資源；哪些路線已被反覆重訪；哪些障礙已經得到可審計確認；哪些表示仍然有新增資訊；哪些 basin 的邊際研究收益已下降；哪些 frontier 尚未進入。

而這些資訊仍然必須服從本文最終的認識論限制：

$$
\boxed{
\text{Coverage is a property of an observed research regime,
not a percentage of mathematical reality.}
}
$$

這就是「邏輯空間積分」作為 AI 長程數學研究量測框架的最小成立條件。

---

# 參考文獻

1. Hubert, T. et al. **Olympiad-level formal mathematical reasoning with reinforcement learning.** *Nature* (2025). https://www.nature.com/articles/s41586-025-09833-y
2. Huang, S. et al. **Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925 (2025). https://arxiv.org/abs/2502.17925
3. Xin, R. et al. **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving.** arXiv:2502.03438 (2025). https://arxiv.org/abs/2502.03438
4. Achim, T. et al. **Aristotle: IMO-level Automated Theorem Proving.** arXiv:2510.01346 (2025). https://arxiv.org/abs/2510.01346
5. Tsoukalas, G. et al. **Advancing Mathematics Research with AI-Driven Formal Proof Search.** arXiv:2605.22763 (2026). https://arxiv.org/abs/2605.22763
6. Kim, J. et al. **Benchmarking Testing in Automated Theorem Proving.** arXiv:2604.23698 (2026). https://arxiv.org/abs/2604.23698
7. **Can Models Write Graduate Level Math Proofs That Are Formally Verifiable? FormalProofBench.** arXiv:2603.26996 (2026). https://arxiv.org/abs/2603.26996
8. Pu, L. et al. **MA-ProofBench: A Two-Tiered Evaluation of LLMs for Formal Theorem Proving in Mathematical Analysis.** arXiv:2606.13782 (2026). https://arxiv.org/abs/2606.13782
9. **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363 (2026). https://arxiv.org/abs/2606.25363
10. **TreeThink: A Modular Tree Search Library for Mathematical Theorem Proving.** arXiv:2607.11258 (2026). https://arxiv.org/abs/2607.11258
11. **Self-Supervised Theorem Discovery in a Formal Axiomatic System.** arXiv:2606.28747 (2026). https://arxiv.org/abs/2606.28747
12. **Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137 (2026). https://arxiv.org/abs/2605.13137
13. Requena, B. et al. **A Minimal Agent for Automated Theorem Proving.** arXiv:2602.24273 (2026). https://arxiv.org/abs/2602.24273
14. Google DeepMind. **AI achieves silver-medal standard solving International Mathematical Olympiad problems.** 2024; methodology updated with the 2025 Nature publication. https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/

---

# 版本與非主張

## 本文主張

- 長程 AI 數學研究需要超越 solved / unsolved 的研究進度表示。
- 邏輯空間積分可作為描述研究 coverage 的理論框架。
- 真正開放問題通常不能誠實宣稱已知全域 proof-space denominator。
- coverage 應拆成 state、route、obstruction、method、representation、verification 等多個維度。
- 負結果在適用域明確、可重現、可審計時，可以增加研究資訊。
- 局部 saturation 與 global saturation 必須分離。

## 本文不主張

1. 已存在所有數學問題通用的自然測度 $\mu$；
2. 可直接計算 Navier--Stokes 或 P/NP 的真實 proof-space 百分比；
3. artifact 越多代表 coverage 越高；
4. AI 生成越多代表越接近真理；
5. novelty 越低代表原命題錯誤；
6. no-go 越多代表命題不可證；
7. formal verification 自動保證自然語言 statement fidelity；
8. 多 agent 自動提高真理率；
9. NS-203 已顯示 Navier--Stokes 全域證明空間飽和；
10. 本文的積分符號已構成傳統測度論意義下對所有 proof objects 的完備測度。

---

**END OF LSI-PSD-02 v2.0 Expanded Edition**


<!-- END LSI-PSD-02 -->

---


<!-- BEGIN LSI-PSD-03 -->

# LSI-PSD-03 — 語義商空間：為什麼一萬篇論文不等於一萬條證明路徑

## Semantic Quotient Space: Why Ten Thousand Papers Do Not Equal Ten Thousand Proof Routes

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 03  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Semantic Quotient and Deduplication Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文建立長程 AI 數學研究中的語義商空間、表示商空間、路徑商空間與障礙商空間框架。本文的「等價」「商空間」「canonicalization」「去重」首先是研究工程與 proof-space measurement 的操作概念；除非明確給出形式系統中的互推證明或其他可重現證據，不應把語義相似、embedding 鄰近、圖結構近似或 LLM 判斷直接稱為數學等價。本文不主張任何未解問題的全部證明路徑已可被完整分類，也不主張有限 corpus 的 quotient 結果等於真實數學空間的 quotient。

---

## 摘要

當 AI 能在同一數學問題上持續生成數百、數千甚至上萬份研究稿時，最容易出現的統計錯覺不是「完全沒有新東西」，而是相反：**把大量表面不同的文本、符號與局部推導誤認為大量彼此獨立的證明路徑。** 同一命題可以經由變數重命名、等價假設、座標變換、定義展開、引理重排、形式庫差異、tactic surface 差異與自然語言重述而產生大量外觀不同的研究產物。若將每份 artifact 都視為一個獨立 proof-space sample，則 coverage、novelty、sampling order、confluence 與 saturation 指標都會被系統性高估。

然而，簡單「去重」同樣危險。兩個字面上高度相似的敘述，可能因量詞順序、domain、regularity class、邊界條件、背景公理、library semantics 或 hidden assumptions 不同而具有不同真值條件。更進一步，即使兩個 theorem statement 在數學上互相等價，它們對當前 AI prover 而言也未必是相同搜尋狀態。2026 年關於 formal theorem proving 對稱性的研究顯示，語義等價的 rewrites 仍可造成顯著不同的 proof success；2025 年 Rocq proof engineering 的 goal clone detection 則直接發現大型 proof codebase 中存在 exact duplication、generalization 與 $\alpha$-equivalent goals with different proofs；ASSESS 與 GTED 等 formal statement evaluation 工作也指出，字串相似、結構相似與語義可證等價需要被分離處理。

本文因此提出一個**多層語義商空間框架**。令原始研究產物空間為：

$$
\Omega_R^{raw}(Q).
$$

本文不使用單一等價關係，而定義一族由弱至強、用途不同的關係：

$$
\sim_{lex},
\quad
\sim_{\alpha},
\quad
\sim_{def},
\quad
\sim_{prop},
\quad
\sim_{route},
\quad
\sim_{obs},
\quad
\sim_{evid}.
$$

其中分別表示字面／表面規範化、變數重命名、定義等價、命題等價、證明路徑骨架等價、障礙等價與證據等價。本文進一步區分：

$$
\Omega_R^{math}(Q)
=
\Omega_R^{raw}(Q)/\sim_{prop}
$$

與：

$$
\Omega_R^{search}(Q),
$$

後者保留具體 representation、proof state、library context 與 search policy，因為在演算法層它們可能直接影響可達性與成功率。這形成本文的核心原則：

$$
\boxed{
\text{Mathematical redundancy}
\not\Rightarrow
\text{search-dynamical redundancy}.
}
$$

本文提出「不可過早商化原則」：任何合併操作都必須保留足以重建原始 assumptions、quantifiers、domains、dependencies、evidence 與 provenance 的資訊。embedding、lexical similarity 與 LLM semantic judgment 只能作候選生成器，不得獨立充當等價證明。對不可確定 pair，本文使用三值 relation：

$$
E_{ij}
\in
\{
\text{equivalent},
\text{distinct},
\text{undetermined}
\},
$$

避免因強行二分造成 semantic collision 或 false split。

在計量層，本文定義 quotient-adjusted novelty：

$$
\nu_i^{quot}
=
1-
\max_{j<i}
\operatorname{Sim}_{quot}(g_i,g_j),
$$

有效樣本數：

$$
N_{\mathrm{eff}}
=
\sum_{c\in\mathcal C}
w(c),
$$

以及 multiplicity profile、route-family entropy、semantic redundancy ratio 與 quotient-corrected coverage。由此，原本的：

$$
N=10{,}000
$$

可能在商化後只對應：

$$
N_{\mathrm{eff}}\ll10{,}000.
$$

但如果同一數學命題的不同 representation 對 prover 具有不同成功率，則這些 representation 又不能在 search-space 層被直接刪除。本文因此主張 proof-space observatory 必須同時保存「數學身份」與「搜尋身份」，並以可追溯的 equivalence graph 而非單一 embedding cluster 作為去重基礎。

本文最後將此框架接回 LSI-PSD-01 與 LSI-PSD-02：前兩篇定義了搜尋制度與邏輯空間積分，本文回答其必要前置問題——**究竟什麼才算一個新的研究點？** 若沒有語義商空間，coverage 可能只是文字生成量；若 quotient 過度，真正影響搜尋的 representation 差異又會被抹除。本文因此把「正確商化」定位為長程 AI 數學研究從文本堆積轉向可審計 proof-space science 的第一道結構門檻。

**關鍵詞：** 語義商空間、proof-space quotient、representation sensitivity、goal clone、$\alpha$-equivalence、命題等價、proof skeleton、obstruction equivalence、semantic deduplication、canonicalization、novelty、有效樣本數、AI 數學研究

---

# 1. 問題的真正起點：一萬篇不等於一萬個數學狀態

## 1.1 Raw count 的誘惑

假設一個長程 AI 研究系統在固定問題 $Q$ 上生成：

$$
N=10{,}000
$$

份 artifact。

最直覺的統計是：

$$
|\mathcal G_N|=10{,}000.
$$

若每篇都使用不同標題、不同符號、不同局部 lemma 與不同語言敘述，看起來似乎表示研究系統已經走過一萬個不同位置。

但這個推論沒有保證。

考慮一個最簡單的例子：

$$
a+b=b+a
$$

與：

$$
x+y=y+x.
$$

如果背景型別與假設相同，它們可能只是變數重命名。

若系統又生成：

$$
u+v=v+u,
$$

$$
p+q=q+p,
$$

$$
r+s=s+r,
$$

那麼 raw artifact count 增加了五次，但數學內容可能只增加零次。

因此：

$$
\boxed{
N_{\mathrm{artifact}}
\neq
N_{\mathrm{semantic\ states}}.
}
$$

## 1.2 在 AI 時代，表面變異會非常便宜

傳統人類研究中，重寫一篇數學論文有成本。

AI 生成使以下操作接近廉價：

- 重新命名變數；
- 改變定義順序；
- 把同一 lemma 拆成三個 lemma；
- 把三個 lemma 合成一個 proposition；
- 改用 Fourier / physical-space / geometric language；
- 改變自然語言敘述；
- 改變 theorem prover library calls；
- 改變 tactic sequence；
- 改變中間 auxiliary quantity；
- 把同一 proof idea 換成不同敘事框架。

因此：

$$
\text{surface diversity}
$$

可以快速增長，而：

$$
\text{structural diversity}
$$

未必同步增長。

這使得「去重」不再只是資料清理，而是 proof-space measurement 的必要數學前置。

## 1.3 但去重也可能毀掉真正的新資訊

反過來，考慮：

$$
\forall x\in X,\ \exists y\in Y,\ P(x,y)
$$

與：

$$
\exists y\in Y,\ \forall x\in X,\ P(x,y).
$$

文字高度相似。

但量詞順序改變後，命題通常完全不同。

再例如：

$$
u\in L^3(\mathbb R^3)
$$

與：

$$
u\in L^\infty_tL^3_x.
$$

符號差異看似很小，對 PDE regularity 問題卻可能改變 theorem 的實質。

所以：

$$
\boxed{
\text{text similarity}
\not\Rightarrow
\text{semantic equivalence}.
}
$$

因此本文同時反對兩種粗糙化：

$$
\text{每篇都算新}
$$

與：

$$
\text{看起來像就合併}.
$$

---

# 2. 從 artifact 到研究對象：先分層，不先商化

## 2.1 原始研究產物

令：

$$
g_i
$$

表示第 $i$ 個 research artifact。

它可以是：

- 一篇 paper；
- 一個 proof attempt；
- 一個 lemma bundle；
- 一份 formal theorem file；
- 一個 counterexample candidate；
- 一個 computational experiment；
- 一個 no-go note；
- 一次 route audit。

原始 artifact 空間寫成：

$$
\Omega_R^{raw}(Q)
=
\{g_1,g_2,\ldots\}.
$$

這個空間保留所有歷史痕跡。

它不是最終用來計算 coverage 的空間，但它必須被保存。

## 2.2 每個 artifact 不只是一段文字

本文把 artifact 抽取為：

$$
g_i
=
(
S_i,
A_i,
C_i,
D_i,
R_i,
O_i,
E_i,
V_i,
P_i
),
$$

其中：

- $S_i$：statement / target；
- $A_i$：assumptions；
- $C_i$：claims / lemmas；
- $D_i$：dependency structure；
- $R_i$：proof route；
- $O_i$：obstruction；
- $E_i$：evidence；
- $V_i$：verification state；
- $P_i$：provenance。

只有在這些結構被抽取後，「這兩篇是不是同一條路」才有意義。

## 2.3 表面文字只是其中一個投影

令文本投影為：

$$
\pi_{text}(g_i).
$$

令 claim graph 投影為：

$$
\pi_{claim}(g_i).
$$

令 route graph 投影為：

$$
\pi_{route}(g_i).
$$

令 obstruction 投影為：

$$
\pi_{obs}(g_i).
$$

則：

$$
\pi_{text}(g_i)
\neq
g_i.
$$

因此不能把文本 embedding 直接當作完整研究身份。

---

# 3. 「相同」不是一個 relation，而是一族 relations

## 3.1 第一層：字面等價

定義：

$$
g_i\sim_{lex}g_j
$$

若經過允許的 whitespace、格式、標點與 deterministic normalization 後，核心文本相同。

這只處理最便宜的 duplicate。

它可以抓：

- exact copy；
- Markdown formatting 差異；
- 標點與空格差異；
- metadata 順序差異。

但它幾乎不處理數學語義。

## 3.2 第二層：$\alpha$-等價

定義：

$$
g_i\sim_{\alpha}g_j
$$

若差異主要來自 bound/free variable 的一致重命名，且不改變 binding structure。

例如：

$$
\forall x,\ P(x)
$$

與：

$$
\forall y,\ P(y)
$$

在適當條件下可屬於同一 $\alpha$-class。

這一層在 proof engineering 中非常實際。Rocq 的 goal clone detection 已把 $\alpha$-equivalent goals 視為可檢測的重複工作類型之一。

## 3.3 第三層：定義展開等價

定義：

$$
g_i\sim_{def}g_j
$$

若兩個 statement 或 proof state 僅因 definitional unfolding、notation expansion、syntactic sugar 或可逆 normalization 而不同。

例如某個 library abbreviation：

$$
A:=B\cap C
$$

展開後：

$$
x\in A
\Longleftrightarrow
x\in B\land x\in C.
$$

若形式系統判定兩者 definitionally equal，則它們可以在特定層級被合併。

## 3.4 第四層：命題等價

最強的數學核心之一是：

$$
g_i\sim_{prop}g_j
$$

當且僅當在指定背景理論 $\mathcal A$ 中：

$$
\mathcal A\vdash
Q_i\leftrightarrow Q_j.
$$

這比文字與結構相似強得多。

若背景理論不同，則 equivalence judgment 也可能不同。

因此完整記號應寫成：

$$
Q_i\sim_{prop}^{\mathcal A}Q_j.
$$

## 3.5 第五層：proof-route skeleton 等價

兩個 theorem statement 可以不同，但證明架構高度相同。

設 route graph：

$$
\Gamma_i=(V_i,E_i,\tau_i),
$$

其中 $\tau_i$ 是 node role：

$$
\tau_i(v)
\in
\{
A,L,B,C,O
\},
$$

分別表示 assumption、lemma、bridge、closure、obstruction。

若存在保留角色與核心 dependency 的映射：

$$
\phi:
\Gamma_i
\rightarrow
\Gamma_j,
$$

使兩圖在去除低階 notation 差異後同構或近似同構，則定義：

$$
g_i\sim_{route}g_j.
$$

這不是命題等價。

它表示：

> 這兩份研究在 proof architecture 上走的是同一類路。

## 3.6 第六層：obstruction 等價

定義：

$$
g_i\sim_{obs}g_j
$$

若兩條 route 最後失敗或停止於同一個 canonical obstruction family。

例如：

$$
R_1
\rightarrow
O^\star,
$$

$$
R_2
\rightarrow
O^\star.
$$

即使：

$$
R_1\not\sim_{route}R_2,
$$

仍可能：

$$
R_1\sim_{obs}R_2.
$$

這正是後續 LSI-PSD-06 的 confluence 核心。

## 3.7 第七層：evidence 等價

兩份 artifact 可能提出同一 claim，但 evidence 不同。

例如：

$$
C
\leftarrow
E_1
$$

與：

$$
C
\leftarrow
E_2.
$$

若 $E_1$ 是 formal proof、$E_2$ 是 numerical experiment，不能因 claim 相同就把 evidence 層完全合併。

因此：

$$
g_i\sim_{claim}g_j
$$

不推出：

$$
g_i\sim_{evid}g_j.
$$

這一點對 scientific audit 特別重要。

---

# 4. 等價關係的層次不是單純線性階梯

最容易想像：

$$
\sim_{lex}
\subset
\sim_{\alpha}
\subset
\sim_{def}
\subset
\sim_{prop}.
$$

在某些形式化設定下可以近似這樣理解。

但 route equivalence 與 obstruction equivalence 並不一定落在線性鏈上。

可能：

$$
g_i\sim_{prop}g_j
$$

但：

$$
g_i\not\sim_{route}g_j.
$$

也可能：

$$
g_i\not\sim_{prop}g_j
$$

但：

$$
g_i\sim_{route}g_j.
$$

例如兩個不同定理都使用：

$$
\text{compactness}
\rightarrow
\text{limit object}
\rightarrow
\text{rigidity}
\rightarrow
\text{contradiction}.
$$

它們在命題上不同，但 route skeleton 同族。

因此本文把 equivalence structure 視為：

$$
\boxed{
\text{equivalence lattice / multi-relation graph}
}
$$

而不是單一 relation。

---

# 5. 語義商空間的第一個正式定義

## 5.1 數學命題商空間

固定背景理論 $\mathcal A$。

定義：

$$
\Omega_R^{math}(Q)
=
\Omega_R^{raw}(Q)/\sim_{prop}^{\mathcal A}.
$$

元素不是單篇 artifact，而是：

$$
[g]_{prop}.
$$

每個等價類可以包含：

- 多種 notation；
- 多種 formalization；
- 多種 natural-language rendering；
- 多個 proof scripts；
- 多個變數命名。

這是最接近「數學內容去重」的空間。

## 5.2 Route quotient

另外定義：

$$
\Omega_R^{route}(Q)
=
\Omega_R^{raw}(Q)/\sim_{route}.
$$

其元素：

$$
[g]_{route}
$$

代表一個 proof architecture family。

## 5.3 Obstruction quotient

再定義：

$$
\Omega_R^{obs}(Q)
=
\Omega_R^{raw}(Q)/\sim_{obs}.
$$

其元素：

$$
[g]_{obs}
$$

代表一個 obstruction family。

因此一份 corpus 可以有：

$$
N_{raw}=10{,}000,
$$

但：

$$
N_{prop}=1{,}200,
$$

$$
N_{route}=180,
$$

$$
N_{obs}=23.
$$

這三個數回答完全不同的研究問題。

---

# 6. 一個商空間不夠：數學身份與搜尋身份必須分離

## 6.1 表示在數學上可能冗餘

若：

$$
Q_i\sim_{prop}Q_j,
$$

數學家可能自然說：

> 這是同一個命題的兩種表示。

在純數學內容統計上，這樣 quotient 是合理的。

## 6.2 表示在 AI 搜尋上可能是因果變數

但是對 prover：

$$
P(
\operatorname{success}\mid
Q_i,R
)
$$

與：

$$
P(
\operatorname{success}\mid
Q_j,R
)
$$

可能不同。

2026 年「What are the Right Symmetries for Formal Theorem Proving?」直接研究了這種現象：語義等價的 statement rewrites 可造成 LLM prover 成功率大幅變動。

因此：

$$
\boxed{
Q_i\sim_{prop}Q_j
\centernot\Rightarrow
s_R(Q_i)=s_R(Q_j).
}
$$

## 6.3 搜尋身份

本文定義搜尋狀態：

$$
\sigma
=
(
[Q]_{prop},
\rho,
\Lambda,
\Pi,
\mathcal M,
B
),
$$

其中：

- $[Q]_{prop}$：數學命題身份；
- $\rho$：具體 representation；
- $\Lambda$：library / environment；
- $\Pi$：search policy；
- $\mathcal M$：可用方法族；
- $B$：資源界。

因此：

$$
\Omega_R^{search}(Q)
$$

不應對 $\rho$ 過早 quotient。

## 6.4 核心分離原則

本文提出：

$$
\boxed{
\textbf{Mathematical Identity}
\neq
\textbf{Search Identity}.
}
$$

以及：

$$
\boxed{
\text{Mathematical redundancy}
\not\Rightarrow
\text{search-dynamical redundancy}.
}
$$

這是整篇最重要的結論之一。

---

# 7. Representation Sensitivity Index

## 7.1 定義

對同一命題等價類：

$$
[Q]_{prop},
$$

令可審計表示集合為：

$$
\mathcal R(Q)
=
\{\rho_1,\ldots,\rho_m\}.
$$

定義成功率：

$$
p_k
=
P(
\operatorname{success}
\mid
Q,\rho_k,R
).
$$

定義：

$$
\operatorname{RSI}(Q;R)
=
\operatorname{Var}
(
p_1,\ldots,p_m
).
$$

稱為：

$$
\boxed{
\textbf{Representation Sensitivity Index}.
}
$$

## 7.2 另一個無尺度版本

可定義：

$$
\operatorname{RSI}_{range}
=
\max_k p_k-\min_k p_k.
$$

若：

$$
\operatorname{RSI}_{range}\approx0,
$$

表示 prover 接近 success invariance。

若：

$$
\operatorname{RSI}_{range}\gg0,
$$

表示 representation 是重要的 search variable。

## 7.3 為什麼 RSI 不是 theorem difficulty

一個命題可能平均成功率很低：

$$
\bar p\ll1,
$$

但：

$$
\operatorname{RSI}\approx0.
$$

這表示它在所有已測表示下都難。

另一命題可能：

$$
\bar p\approx0.5,
$$

但：

$$
\operatorname{RSI}\gg0.
$$

這表示其難度高度依賴表示。

因此：

$$
\boxed{
\text{difficulty}
\neq
\text{representation sensitivity}.
}
$$

---

# 8. Goal clone：形式 proof engineering 已經遇到同一個問題

2025 年 ECOOP 論文「Automatic Goal Clone Detection in Rocq」把 goal cloning 定義為 proof engineering 中的重複工作：相同或 $\alpha$-equivalent goal 被多次證明。

該工作重要的不是某個單一數字，而是分類本身：

- exact goal duplication；
- generalization；
- $\alpha$-equivalent goals with different proofs。

這三類直接顯示：

$$
\text{same goal}
$$

與：

$$
\text{same proof}
$$

不是同一件事。

形式上：

$$
Q_i\sim_{\alpha}Q_j
$$

仍可能：

$$
\pi_i\not\sim_{route}\pi_j.
$$

因此 proof corpus 去重至少要保存：

$$
([Q], [\pi]).
$$

而不是只保存其中一個。

---

# 9. Formal statement similarity：相似、等價與可證要拆開

## 9.1 字串相似不足

如果只用：

$$
\operatorname{Lev}(S_i,S_j)
$$

或 lexical overlap，則變數重命名會造成不必要距離。

## 9.2 純 proof-based equivalence 也不夠

如果只問：

$$
\mathcal A\vdash Q_i\leftrightarrow Q_j?
$$

則在 proof search 失敗時，系統只能得到：

$$
\text{unknown}.
$$

它不能提供 graded structural similarity。

## 9.3 ASSESS 的啟示

ASSESS 把：

- provability；
- likeness；
- semantic-preserving transformations；

分離，並以 operator tree 與 transformation-aware tree distance 建構 continuous similarity。

這正支持本文的立場：

$$
\boxed{
\text{semantic equivalence}
\neq
\text{structural likeness}.
}
$$

## 9.4 GTED 的啟示

GTED 先 standardize formal statements，再轉為 operator trees 進行距離估計。

對 proof-space observatory 而言，這類方法可作：

$$
\text{candidate pair ranking},
$$

但不是最終 merge authority。

---

# 10. 不可過早商化原則

本文正式提出：

$$
\boxed{
\textbf{Never quotient away information before preserving
the evidence required to reconstruct the distinction.}
}
$$

中文：

$$
\boxed{
\textbf{不可過早商化原則}.
}
$$

## 10.1 什麼資訊必須先保存

至少包括：

$$
\mathcal S_i
=
(
Q_i,
A_i,
\forall/\exists_i,
D_i,
B_i,
C_i,
E_i,
V_i,
P_i
).
$$

具體包含：

- 原始 statement；
- quantifier structure；
- domain；
- regularity / boundary conditions；
- background assumptions；
- dependencies；
- proof / counterexample evidence；
- verification state；
- provenance；
- source hash；
- version。

如果這些都沒保存，merge 是不可逆資訊損失。

## 10.2 商化是研究推論，不是壓縮格式

若把兩篇 artifact 合併為：

$$
[g],
$$

其實是在做一個 epistemic claim：

> 這兩份產物在某個指定 relation 下不應被計為兩個獨立狀態。

所以每次 quotient 都應記錄：

$$
\text{relation type}
+
\text{evidence}
+
\text{confidence}
+
\text{reversibility}.
$$

---

# 11. 三值等價：不要強迫所有 pair 立即二分

## 11.1 二值判斷過強

對兩個大型自然語言 proof attempts：

$$
g_i,g_j,
$$

常常無法立即知道：

$$
g_i\sim g_j
$$

或：

$$
g_i\not\sim g_j.
$$

如果系統強迫二分，就會產生：

- false merge；
- false split。

## 11.2 三值 relation

本文定義：

$$
E_{ij}^{(k)}
\in
\{
1,0,?
\},
$$

其中：

$$
1=\text{equivalent under relation }k,
$$

$$
0=\text{distinguishable under relation }k,
$$

$$
?=\text{undetermined}.
$$

## 11.3 Undetermined 不是失敗

在研究資料庫中：

$$
?
$$

是一個合法狀態。

它表示：

> 目前證據不足，尚不把兩者合併，也不宣告其不同。

這比錯誤確定性更有價值。

---

# 12. Semantic collision：過度商化的第一種災難

定義 semantic collision：

$$
g_i\not\sim_{prop}g_j
$$

但系統誤判：

$$
g_i\sim_{prop}g_j.
$$

這會造成：

$$
[g_i]=[g_j]
$$

被錯誤合併。

後果包括：

- 真正新 theorem 被吞掉；
- distinct obstruction 被合併；
- coverage 被低估；
- contradiction 被隱藏；
- provenance 被破壞。

因此：

$$
\boxed{
\text{false merge}
}
$$

通常比保守的暫時不合併更危險。

---

# 13. False split：商化不足的第二種災難

反過來：

$$
g_i\sim_{prop}g_j
$$

但系統持續視為：

$$
[g_i]\neq[g_j].
$$

這稱為 false split。

後果：

- novelty 被高估；
- coverage 被高估；
- saturation 被延遲看見；
- AI 不斷重做同一件事；
- route multiplicity 被誤認成 route diversity。

因此 quotient system 必須同時控制：

$$
\operatorname{FMR}
=
P(\text{false merge})
$$

與：

$$
\operatorname{FSR}
=
P(\text{false split}).
$$

---

# 14. 量詞、domain 與 assumptions 是語義身份的最低護欄

## 14.1 Quantifier signature

定義：

$$
\operatorname{QS}(Q)
=
(q_1,\ldots,q_m),
$$

其中：

$$
q_i\in\{\forall,\exists\}.
$$

若 quantifier dependency graph 不同，不應僅靠 embedding 合併。

## 14.2 Domain signature

定義：

$$
\operatorname{DS}(Q)
=
(
X_1,\ldots,X_n
),
$$

記錄變數與其 domain。

例如：

$$
x\in\mathbb R
$$

與：

$$
x\in\mathbb C
$$

不應被視為無害差異。

## 14.3 Assumption signature

令：

$$
\operatorname{AS}(Q)
=
\{A_1,\ldots,A_k\}.
$$

兩個 statement 的核心式子相同，但：

$$
\operatorname{AS}(Q_i)
\neq
\operatorname{AS}(Q_j)
$$

可能代表 theorem strength 完全不同。

## 14.4 Context signature

完整 context：

$$
\operatorname{CTX}(Q)
=
(
\operatorname{QS},
\operatorname{DS},
\operatorname{AS},
\Lambda,
\mathcal A
).
$$

若 context 未對齊，不應直接宣告 proposition equivalence。

---

# 15. Canonicalization 與 quotient 不同

## 15.1 Canonicalization

canonicalization 是選擇代表元：

$$
\kappa:
\Omega
\rightarrow
\Omega_{can}.
$$

理想上：

$$
x\sim y
\Rightarrow
\kappa(x)=\kappa(y).
$$

## 15.2 Quotient

quotient 則是建立等價類：

$$
q:
\Omega
\rightarrow
\Omega/\sim.
$$

canonicalization 可以幫助 quotient，但不是 quotient 本身。

## 15.3 Canonical form 可能不存在或成本過高

在大型自然語言研究 artifact 上，很難期待全域唯一 canonical form。

因此本文建議：

$$
\boxed{
\text{local canonicalization}
+
\text{equivalence graph}
}
$$

而不是追求一個虛假的 universal normal form。

---

# 16. 多階 canonical signature

每個 artifact 可建立：

$$
K(g)
=
(
K_0,
K_1,
K_2,
K_3,
K_4
).
$$

其中：

### $K_0$：surface signature

- normalized title；
- lexical hash；
- formula hash。

### $K_1$：statement signature

- quantifier tree；
- domain tree；
- assumption set；
- target operator tree。

### $K_2$：dependency signature

- theorem dependencies；
- lemma DAG；
- imported theory family。

### $K_3$：route signature

- proof tactic families；
- bridge lemmas；
- closure pattern；
- contradiction pattern。

### $K_4$：obstruction signature

- failure condition；
- uncontrolled quantity；
- missing implication；
- nonclosure mechanism。

這使 candidate dedup 可以逐層升級。

---

# 17. Proof-route graph 的商化

## 17.1 Route graph

令：

$$
\Gamma_i
=
(V_i,E_i,\tau_i,\lambda_i).
$$

其中：

- $V_i$：研究節點；
- $E_i$：依賴與推導邊；
- $\tau_i$：角色標籤；
- $\lambda_i$：語義標籤。

## 17.2 Skeleton operator

定義：

$$
\operatorname{Skel}(\Gamma_i)
$$

移除：

- 變數名稱；
- 無關 formatting；
- 某些低階 library tactic；
- 可證明為純 administrative 的節點。

保留：

- assumption family；
- principal lemma；
- bridge；
- closure；
- obstruction。

## 17.3 Route similarity

定義：

$$
S_{route}(i,j)
=
\Phi(
\operatorname{Skel}(\Gamma_i),
\operatorname{Skel}(\Gamma_j)
).
$$

$\Phi$ 可以由：

- graph edit distance；
- role-aware graph matching；
- dependency motif matching；
- formal transformation；

構成。

## 17.4 Route equivalence 不應只靠 threshold

若：

$$
S_{route}(i,j)>\theta,
$$

最多表示：

$$
\text{candidate route-equivalence}.
$$

正式 merge 還應檢查：

- 核心 assumptions 是否對應；
- closure condition 是否同型；
- obstruction 是否真的同族；
- 是否有可逆 mapping。

---

# 18. Obstruction canonicalization

## 18.1 為什麼障礙比論文標題更穩定

一個研究 route 可能多次改名：

$$
\text{energy barrier}
\rightarrow
\text{closure gap}
\rightarrow
\text{critical residue}.
$$

如果實際都指：

$$
\text{某個相同 quantity 無法被現有 estimate 控制},
$$

那應建立 canonical obstruction ID。

## 18.2 Obstruction record

本文建議：

```text
obstruction_id
target_claim
failed_implication
required_bound
available_bound
missing_margin
domain
assumptions
first_seen
revisit_count
route_sources
verification_status
```

## 18.3 Obstruction equivalence

兩個 obstruction：

$$
O_i,O_j
$$

若存在保留 failure semantics 的 mapping：

$$
\psi:O_i\leftrightarrow O_j,
$$

才可合併。

僅僅都寫：

> closure problem

遠遠不夠。

---

# 19. 證據不能被 quotient 掉

## 19.1 同 claim，多 evidence

設：

$$
C^\star
$$

被三份 artifact 支持：

$$
E_1=\text{formal proof},
$$

$$
E_2=\text{symbolic computation},
$$

$$
E_3=\text{numerical experiment}.
$$

claim 層可以合併：

$$
[C_1]=[C_2]=[C_3],
$$

但 evidence 應保存為多重邊：

$$
E_1,E_2,E_3
\rightarrow
C^\star.
$$

## 19.2 Evidence multiplicity 有價值

如果三個真正獨立 evidence source 指向同一 claim：

$$
\operatorname{Ind}(E_1,E_2,E_3)>0,
$$

那不是重複浪費。

這與三篇文本都複製同一 proof 完全不同。

因此：

$$
\boxed{
\text{semantic deduplication}
\neq
\text{evidence deduplication}.
}
$$

---

# 20. 來源與 provenance 是商化後仍須保留的纖維

可以把 quotient 想成：

$$
q:
\Omega^{raw}
\rightarrow
\bar\Omega.
$$

對每個商空間元素：

$$
\bar g\in\bar\Omega,
$$

其 fiber：

$$
q^{-1}(\bar g)
$$

包含所有原始 artifact。

本文主張：

$$
\boxed{
q^{-1}(\bar g)
\text{ 必須可追溯。}
}
$$

這樣使用者仍能知道：

- 哪些 AI 生成過；
- 哪些版本先出現；
- 哪些 proof 不同；
- 哪些 evidence 獨立；
- 哪些 artifact 被 merge；
- merge 理由是什麼。

---

# 21. 商空間 novelty：真正的新東西是什麼

## 21.1 Raw novelty

定義：

$$
\nu_i^{raw}
=
1-
\max_{j<i}
S_{text}(g_i,g_j).
$$

這回答：

> 文字看起來有多新？

## 21.2 Proposition novelty

定義：

$$
\nu_i^{prop}
=
\mathbf 1
\left(
[g_i]_{prop}
\notin
\{[g_j]_{prop}:j<i\}
\right).
$$

## 21.3 Route novelty

定義：

$$
\nu_i^{route}
=
\mathbf 1
\left(
[g_i]_{route}
\notin
\{[g_j]_{route}:j<i\}
\right).
$$

## 21.4 Obstruction novelty

定義：

$$
\nu_i^{obs}
=
\mathbf 1
\left(
[g_i]_{obs}
\notin
\{[g_j]_{obs}:j<i\}
\right).
$$

## 21.5 Novelty vector

因此：

$$
\boxed{
\boldsymbol\nu_i
=
(
\nu_i^{raw},
\nu_i^{prop},
\nu_i^{route},
\nu_i^{obs},
\nu_i^{evid}
).
}
$$

這比單一 cosine novelty 更有研究價值。

---

# 22. 一個極重要的四象限

令：

$$
\nu^{raw}
$$

代表表面新穎度，

$$
\nu^{route}
$$

代表 route 新穎度。

可形成四象限。

## 象限 I：表面新，路徑也新

$$
\nu^{raw}\uparrow,
\qquad
\nu^{route}\uparrow.
$$

是真正高價值新探索候選。

## 象限 II：表面新，路徑舊

$$
\nu^{raw}\uparrow,
\qquad
\nu^{route}\downarrow.
$$

可能只是 rephrasing / reparameterization。

## 象限 III：表面舊，路徑新

$$
\nu^{raw}\downarrow,
\qquad
\nu^{route}\uparrow.
$$

這往往最容易被文字相似度漏掉。

小修改可能帶來新 closure。

## 象限 IV：表面舊，路徑也舊

$$
\nu^{raw}\downarrow,
\qquad
\nu^{route}\downarrow.
$$

高概率為真正重訪。

---

# 23. Multiplicity：同一類被重訪多少次

對 equivalence class：

$$
c\in\Omega/\sim,
$$

定義 multiplicity：

$$
m(c)
=
|\{g_i:q(g_i)=c\}|.
$$

如果：

$$
m(c)\gg1,
$$

代表該類被高頻重訪。

但高 multiplicity 有至少三種解釋：

1. 無意義重複；
2. search basin 有強吸引力；
3. 同一數學類有多種 search-effective representation。

所以：

$$
m(c)
$$

本身不是壞事。

需要和：

$$
\operatorname{RSI}(c)
$$

一起看。

---

# 24. 有效樣本數

## 24.1 最粗版本

若所有 exact-equivalent artifact 只算一次：

$$
N_{\mathrm{eff}}
=
|\Omega/\sim|.
$$

## 24.2 權重版本

對每個 class：

$$
c,
$$

給予權重：

$$
w(c)
=
f(
\text{semantic novelty},
\text{route novelty},
\text{evidence independence},
\text{verification}
).
$$

則：

$$
N_{\mathrm{eff}}
=
\sum_c w(c).
$$

## 24.3 Representation-sensitive correction

若同一 proposition class 的不同 representation 對 search success 有可測差異，則：

$$
w(c)
$$

不應固定為 $1$。

可以寫：

$$
w(c)
=
1+\lambda \Psi(\operatorname{RSI}(c)),
$$

其中：

$$
\Psi(0)=0.
$$

這表示：

> 數學上同一個命題，在 search dynamics 上仍可能提供額外實驗資訊。

---

# 25. Semantic Redundancy Ratio

定義：

$$
\operatorname{SRR}
=
1-
\frac{N_{\mathrm{eff}}}{N_{raw}}.
$$

若：

$$
\operatorname{SRR}\approx0,
$$

表示 raw corpus 多數產物都保有獨立有效結構。

若：

$$
\operatorname{SRR}\rightarrow1,
$$

表示大量 artifact 在所選 quotient 下是重複。

但必須標明 quotient type：

$$
\operatorname{SRR}_{prop},
\quad
\operatorname{SRR}_{route},
\quad
\operatorname{SRR}_{obs}.
$$

否則數字沒有意義。

---

# 26. Route-family entropy

令 route classes：

$$
\mathcal C_{route}
=
\{c_1,\ldots,c_k\}.
$$

令：

$$
p_i
=
\frac{m(c_i)}{\sum_jm(c_j)}.
$$

定義：

$$
H_{route}
=
-\sum_{i=1}^{k}
p_i\log p_i.
$$

若：

$$
H_{route}
$$

很低，表示大量研究集中於少數 route family。

若：

$$
H_{route}
$$

很高，表示探索分散。

## 26.1 Normalized entropy

$$
\widehat H_{route}
=
\frac{H_{route}}{\log k}.
$$

使：

$$
0\leq\widehat H_{route}\leq1.
$$

## 26.2 解讀限制

高 entropy 不一定好。

如果大量 route 都是低品質 hallucination：

$$
H_{route}\uparrow
$$

仍可能沒有數學價值。

所以 entropy 必須配合 verification weighting。

---

# 27. Verification-weighted quotient

對 class：

$$
c,
$$

定義 verifier confidence：

$$
v(c)\in[0,1].
$$

例如：

- formally verified theorem：接近 $1$；
- independently reproduced computation：高；
- heuristic argument：中；
- unsupported LLM claim：低。

定義：

$$
N_{\mathrm{eff}}^{ver}
=
\sum_c
v(c)w(c).
$$

這比單純 class count 更接近研究有效量。

但：

$$
v(c)
$$

不能假裝是一個普適真理機率。

它只是 evidence status 的 operational weight。

---

# 28. LSI-PSD-02 coverage 必須做 quotient correction

前篇定義：

$$
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
).
$$

若沒有 quotient，可能出現：

$$
C_N^{state}\uparrow
$$

只是因為：

$$
\text{同一狀態被重寫很多次}.
$$

因此本文修正：

$$
\widetilde C_N^{state}
=
C_N^{state}
\big/
\sim_{state}.
$$

更一般：

$$
\widetilde{\mathbf C}_N
=
\operatorname{QuotientCorrect}
(
\mathbf C_N,
\mathcal E_N
).
$$

其中：

$$
\mathcal E_N
$$

是已審計 equivalence graph。

---

# 29. Coverage 的分母問題與 quotient 的分母問題不同

即使已完成 perfect dedup：

$$
N_{eff}
$$

仍不能推出：

$$
\frac{N_{eff}}{|\Omega^{true}|}.
$$

因為：

$$
|\Omega^{true}|
$$

通常未知。

因此語義商化解決的是：

$$
\boxed{
\text{不要重複計數}
}
$$

而不是：

$$
\boxed{
\text{知道全域總空間大小}.
}
$$

這兩個問題必須分開。

---

# 30. 商空間與 higher-order sampling 的關係

LSI-PSD-04 將定義：

$$
\Omega^{(0)},
\Omega^{(1)},
\Omega^{(2)},\ldots
$$

若一階狀態沒有先 quotient，則二階 relation 會被重複污染。

例如：

$$
x_1\sim x_2\sim x_3
$$

卻被當成三個獨立 state。

那 transition：

$$
T(x_1),
T(x_2),
T(x_3)
$$

會被誤認為三條獨立二階樣本。

因此：

$$
\boxed{
\text{higher-order sampling requires lower-order quotient discipline}.
}
$$

---

# 31. Representation 不應在 higher-order analysis 前被刪掉

但另一面：

若：

$$
x_1\sim_{prop}x_2
$$

而：

$$
T(x_1)\neq T(x_2)
$$

對 prover 而言表示不同 representation 產生不同 transition。

這本身就是二階資訊。

所以 LSI-PSD-04 必須保留：

$$
([x]_{prop},\rho)
$$

而不是只保留：

$$
[x]_{prop}.
$$

這再度說明：

$$
\text{math quotient}
$$

與：

$$
\text{search quotient}
$$

不能混用。

---

# 32. Cross-formal-system translation：同一命題跨 proof assistant 仍有身份問題

ProofGym 等工作嘗試在 Lean、Coq/Rocq、Isabelle 等 formal systems 間提供共同介面。

這對本系列很重要，因為長期 proof-space science 不應把：

$$
\text{Lean theorem}
$$

與：

$$
\text{Rocq theorem}
$$

自動視為兩個不同數學命題。

但跨系統 equivalence 也不是字串比較可以解決。

應建立：

$$
Q^{Lean}
\leftrightarrow
Q^{Rocq}
\leftrightarrow
Q^{Isabelle}
$$

的 alignment evidence。

只有當 semantics、assumptions 與 imported foundations 對齊時，才可建立跨系統 proposition identity。

---

# 33. Formal proof state factorization 對 quotient 的啟示

LeanTree 把複雜 proof state factorize 成較簡單、可獨立處理的 branches。

這提醒我們：

$$
\text{state identity}
$$

也可能具有分解結構。

若：

$$
s
=
(s_1,\ldots,s_k),
$$

兩個 proof state：

$$
s,s'
$$

可能只差某個獨立 branch。

所以不能只用整段 state string 判斷 duplicate。

可定義：

$$
\operatorname{Fact}(s)
=
\{[s_1],\ldots,[s_k]\}.
$$

然後比較 factorized signatures。

---

# 34. 商空間不是刪資料，而是增加索引層

錯誤做法：

```text
artifact A
artifact B
artifact C
↓
merge
↓
只留下 A
```

本文建議：

```text
artifact A ─┐
artifact B ─┼──> equivalence_class EC-17
artifact C ─┘

EC-17:
  relation: proposition_equivalence
  evidence: ...
  confidence: ...
  representative: A
  members: [A,B,C]
```

也就是：

$$
\boxed{
\text{quotient layer}
\neq
\text{destructive deletion}.
}
$$

---

# 35. Equivalence graph

定義圖：

$$
\mathcal E
=
(V,E),
$$

其中：

$$
V=\{g_i\},
$$

邊：

$$
e_{ij}
=
(
k,
status,
evidence,
confidence
).
$$

其中 $k$ 可為：

$$
lex,\alpha,def,prop,route,obs,evid.
$$

因此同一 pair 可以有：

$$
g_i\sim_{prop}g_j
$$

但：

$$
g_i\not\sim_{route}g_j.
$$

graph model 能自然表達這種多重關係。

---

# 36. Equivalence class 不一定應立刻做 transitive closure

對真正形式等價：

$$
\sim_{prop}
$$

若已嚴格證明為 equivalence relation，可以做 transitive closure。

但對 heuristic relation：

$$
\approx_{route},
$$

若只靠 threshold similarity，則：

$$
A\approx B,
\quad
B\approx C
$$

不一定：

$$
A\approx C.
$$

因此 heuristic route clustering 不應冒充真正 quotient。

本文建議區分：

$$
\sim
$$

與：

$$
\approx.
$$

前者是 audited equivalence。

後者是 similarity / candidate relation。

---

# 37. Pseudometric 比硬 equivalence 更適合早期 corpus

定義：

$$
d_k(g_i,g_j)\geq0.
$$

若：

$$
d_k=0
$$

可能表示在某層無法區分。

但不同點仍可有零距離，所以可先使用 pseudometric。

例如：

$$
d_{route}
=
1-S_{route}.
$$

再由：

$$
d_{route}<\epsilon
$$

產生 candidate cluster。

這比一開始硬宣告：

$$
g_i\sim_{route}g_j
$$

更保守。

---

# 38. Semantic dedup pipeline

本文建議 proof-space observatory 使用以下流程：

```text
Raw Artifact Ingestion
        |
        v
Immutable Source + Hash
        |
        v
Surface Normalization
        |
        v
Statement / Assumption Extraction
        |
        v
Quantifier + Domain Signature
        |
        v
Candidate Retrieval
        |
        v
Structural Similarity
        |
        v
Formal Mutual Implication if Available
        |
        v
Route Graph Comparison
        |
        v
Obstruction Comparison
        |
        v
Equivalence Graph Update
        |
        v
Quotient Metrics
```

關鍵不是某一個模型。

而是：

$$
\boxed{
\text{cheap candidate generation}
\rightarrow
\text{expensive audited merge}.
}
$$

---

# 39. Candidate generation 可以大量使用 embedding

對 $N$ 篇 artifact 做全 pair：

$$
O(N^2)
$$

會快速昂貴。

因此先用：

$$
\operatorname{ANN}
$$

或 sparse lexical index 找：

$$
K\ll N
$$

個候選鄰居。

複雜度近似下降為：

$$
O(NK).
$$

embedding 在這裡很有價值。

但它的角色是：

$$
\boxed{
\text{retrieval}
}
$$

不是：

$$
\boxed{
\text{proof of equivalence}.
}
$$

---

# 40. 多觀察者 semantic audit

對重要 merge：

$$
g_i\leftrightarrow g_j,
$$

可以要求多個獨立 classifier：

$$
A_1,A_2,\ldots,A_m.
$$

每個輸出：

$$
E_{ij}^{(a)}.
$$

但：

$$
\text{majority vote}
$$

仍不是 formal proof。

因此多觀察者只提升：

$$
\text{audit confidence},
$$

不自動提升為：

$$
\mathcal A\vdash Q_i\leftrightarrow Q_j.
$$

---

# 41. Formal verifier 在商化中扮演什麼角色

若可以構造：

$$
Q_i\rightarrow Q_j
$$

與：

$$
Q_j\rightarrow Q_i
$$

並由 proof assistant 驗證，則命題等價證據最強。

但 formal verifier 仍依賴：

- theorem statement 是否 faithful；
- imported axioms；
- definitions；
- library versions；
- formalization correctness。

因此：

$$
\boxed{
\text{verified equivalence of formal statements}
}
$$

不自動等於：

$$
\boxed{
\text{perfect equivalence of original informal intentions}.
}
$$

provenance 必須把 informal-to-formal mapping 保留下來。

---

# 42. Semantic identity 與 historical identity 必須分開

兩篇論文可能數學上完全等價：

$$
g_i\sim_{prop}g_j,
$$

但在歷史上：

$$
t_i<t_j
$$

而 $g_j$ 是獨立重發現。

如果 destructive dedup，把 $g_j$ 刪掉，就會失去：

- independent rediscovery；
- convergence evidence；
- research dynamics；
- route attraction。

所以：

$$
\boxed{
\text{semantic quotient}
\neq
\text{historical quotient}.
}
$$

---

# 43. 重複有時本身就是訊號

若某個 class：

$$
c
$$

在沒有直接 copy 的情況下，被多條獨立路線重訪：

$$
m_{\mathrm{ind}}(c)\gg1,
$$

這可能表示：

- 這個 lemma 是 attractor；
- 這個 obstruction 是 basin boundary；
- 這個 representation 很自然；
- 這個局部 theorem 是高連接 hub。

因此 dedup 後不能只留下：

$$
c.
$$

還要留下：

$$
m(c),
\quad
m_{\mathrm{ind}}(c),
\quad
t_{first},
\quad
t_{revisit}.
$$

---

# 44. Independent rediscovery score

定義：

$$
\operatorname{IRS}(c)
=
\sum_{i\in q^{-1}(c)}
\chi_i,
$$

其中 $\chi_i$ 衡量該 artifact 相對既有 class 的資訊隔離程度，例如：

- 不同模型；
- 不同 prompt lineage；
- 不同方法族；
- 不同時間窗口；
- 未讀取前一結果。

若：

$$
\operatorname{IRS}(c)\gg1,
$$

表示同一結果被獨立重發現多次。

這與 copy multiplicity 完全不同。

---

# 45. Quotient-adjusted recurrence

定義某 class 的 revisit sequence：

$$
t_1<t_2<\cdots<t_m.
$$

定義 inter-revisit interval：

$$
\Delta t_k
=
t_{k+1}-t_k.
$$

若：

$$
\Delta t_k
$$

逐步縮短，可能表示研究路徑越來越被吸引回該 basin。

這是 LSI-PSD-04 與 06 可以研究的高階訊號。

---

# 46. 商空間與「符號先到盡」命題

本系列原始動機之一是：

> 大規模 AI 研究可能在最終證明出現前，先耗盡某個可見的符號／路徑語料。

若不 quotient，這個命題幾乎無法測試。

因為模型永遠可以：

$$
x\mapsto y
$$

換字，

$$
L_1\mapsto L_2
$$

換 lemma 名，

甚至重排章節。

raw novelty 永遠可以被人工製造。

只有在：

$$
\Omega/\sim
$$

上，才有可能問：

$$
\Delta N_{\mathrm{eff}}\rightarrow0?
$$

也就是：

$$
\boxed{
\text{表面還在生成，
但有效 equivalence class 不再增加嗎？}
}
$$

這才是「符號飽和」的可測版本。

---

# 47. 但「符號飽和」必須指定 quotient

不能說：

> 符號空間飽和了。

而應說：

$$
\text{在 relation }\sim_k
\text{ 與 regime }R
\text{ 下，}
$$

觀察到：

$$
\Delta
|\Omega_{N}/\sim_k|
\rightarrow0.
$$

例如：

$$
\Delta N_{route}\rightarrow0
$$

不代表：

$$
\Delta N_{prop}\rightarrow0.
$$

也不代表：

$$
\Delta N_{repr}\rightarrow0.
$$

所以 saturation 是 relation-dependent。

---

# 48. Quotient profile

本文提出：

$$
\boxed{
\mathbf Q_N
=
(
N_{raw},
N_{\alpha},
N_{def},
N_{prop},
N_{route},
N_{obs},
N_{evid}
).
}
$$

這稱為 quotient profile。

若：

$$
N_{raw}\gg N_{route},
$$

表示大量文字變體匯聚到少量 route family。

若：

$$
N_{route}\gg N_{obs},
$$

表示不同方法大量匯聚到少量 obstruction。

這正是 confluence 的前兆。

---

# 49. Quotient compression ratio

對 relation $k$ 定義：

$$
\operatorname{QCR}_k
=
\frac{N_{raw}}{N_k}.
$$

例如：

$$
\operatorname{QCR}_{route}=25
$$

表示平均每個 route class 對應 25 份 raw artifact。

若隨時間：

$$
\operatorname{QCR}_{route}(N)\uparrow,
$$

而：

$$
N_{route}
$$

增長變慢，這比文本重複更像 route saturation。

---

# 50. NS-203 案例應如何升級

前一輪 NS Proof-Space Sampling Observatory 主要仍以 paper-level artifact 和 heuristic concept family 為主。

本文提出第二輪需要：

$$
\boxed{
\text{Paper}
\rightarrow
\text{Claim}
\rightarrow
\text{Lemma}
\rightarrow
\text{Route}
\rightarrow
\text{Obstruction}.
}
$$

## 50.1 不應直接把 203 當有效樣本數

即使：

$$
N_{paper}=203,
$$

真正：

$$
N_{route},
\quad
N_{obs},
\quad
N_{prop}
$$

仍未知。

## 50.2 應先抽 canonical claim

每篇建立：

```text
paper_id
claim_ids
assumption_signature
route_signature
obstruction_ids
formal_status
dependency_ids
```

## 50.3 再建立 equivalence graph

特別檢測：

- 同一 claim 是否跨系列重現；
- 同一 route 是否換 notation 回訪；
- 不同 route 是否落同 obstruction；
- 同 proposition 是否因 representation 不同而 proof behavior 不同。

## 50.4 這樣才能真正測 X 階採樣

若一階 state 都沒 quotient，X 階採樣只是語言統計。

---

# 51. 對 Navier--Stokes 的認識論限制

即使未來得到：

$$
N_{raw}\gg N_{route},
$$

$$
N_{route}\gg N_{obs},
$$

且：

$$
\Delta N_{obs}\rightarrow0,
$$

仍只能說：

> 在目前研究制度、抽取法與 quotient 定義下，觀察到高度 recurrent obstruction structure。

不能推出：

$$
\text{Navier--Stokes 問題錯了}.
$$

不能推出：

$$
\text{不可證}.
$$

不能推出：

$$
\text{獨立}.
$$

不能推出：

$$
\text{全部 proof space 已耗盡}.
$$

這個 epistemic firewall 必須保留到 LSI-PSD-10。

---

# 52. 對 P/NP 的同樣限制

P/NP 更容易出現 representation trap，因為：

- machine model；
- reduction language；
- uniformity；
- circuit model；
- proof complexity；
- relativization；
- natural proofs；
- algebrization；

本來就存在多層 formulation。

因此若做類似 corpus：

$$
\Omega_{P/NP}^{raw},
$$

更必須把：

$$
\sim_{prop},
\quad
\sim_{route},
\quad
\sim_{barrier}
$$

分開。

不能把「又撞到 relativization-style barrier」簡化成：

> 所有方法都一樣。

---

# 53. 商空間對研究記憶的價值

沒有 quotient 的長期記憶：

$$
\mathcal K_N
$$

會越來越大。

但新增內容中可能大量是：

$$
\text{semantic duplicates}.
$$

結果：

- retrieval 變差；
- context 被重複佔據；
- agent 誤判 novelty；
- 相同路線被多次重開。

語義商化後：

$$
\mathcal K_N
\rightarrow
(
\bar{\mathcal K}_N,
\mathcal F_N
),
$$

其中：

- $\bar{\mathcal K}_N$：canonical class layer；
- $\mathcal F_N$：完整 source fibers。

這是一種：

$$
\boxed{
\text{lossless-at-source, compressed-at-navigation}
}
$$

架構。

---

# 54. 商空間對 AI prompt context 的價值

長上下文裡如果塞入：

$$
30
$$

篇本質同 route 的 paper，

AI 可能因頻率誤認：

> 這條 route 很有支持。

但那可能只是同一 source lineage 的重寫。

因此 context builder 應按：

$$
\text{class diversity}
$$

而不是：

$$
\text{artifact count}
$$

取樣。

可以定義：

$$
P(g_i\mid c)
=
\frac{1}{m(c)}
$$

作 class-balanced sampling。

---

# 55. 商空間對多 AI 研究的價值

如果十個 agent 同時工作，最常見浪費之一是：

$$
A_1,\ldots,A_{10}
$$

都進入同一 route basin。

若 observatory 有即時 quotient：

$$
[g_{A_1}]_{route}
=
[g_{A_2}]_{route}
=
\cdots,
$$

scheduler 可以把後續 agent 導向未覆蓋 class。

但不能完全禁止重訪。

因為 independent rediscovery 有驗證價值。

所以應設：

$$
\text{exploration quota}
+
\text{replication quota}.
$$

---

# 56. Exploration 與 replication 必須同時存在

如果只追求：

$$
\nu^{route}\uparrow,
$$

系統可能不再驗證舊結果。

如果只追求：

$$
m(c)\uparrow,
$$

系統會陷入重複。

因此資源配置：

$$
B
=
B_{explore}
+
B_{replicate}
+
B_{audit}.
$$

其中：

$$
B_{explore}
$$

追求新 class，

$$
B_{replicate}
$$

做獨立重現，

$$
B_{audit}
$$

驗證 merge / split。

---

# 57. Quotient-aware scheduler

可以定義 action score：

$$
S(a)
=
\alpha N(a)
+
\beta V(a)
+
\gamma D(a)
-
\delta R(a),
$$

其中：

- $N(a)$：預期 quotient novelty；
- $V(a)$：驗證價值；
- $D(a)$：diversity gain；
- $R(a)$：重複風險。

如果某 route class：

$$
m(c)\gg1
$$

且 independent evidence 已足夠，

則：

$$
R(a)\uparrow.
$$

scheduler 應偏向其他 basin。

---

# 58. 商空間錯誤本身也必須被版本化

今天系統可能判：

$$
g_i\sim_{route}g_j.
$$

未來發現一個 hidden assumption：

$$
A^\star
$$

後，必須拆分：

$$
[g]_{route}
\rightarrow
[g_i]_{route}
\cup
[g_j]_{route}.
$$

因此 equivalence class 不是不可修改真理。

它應有：

```text
class_version
merge_history
split_history
evidence_history
review_status
```

這使 quotient 本身也成為可審計研究對象。

---

# 59. Quotient provenance

每次 merge 記錄：

$$
M_t
=
(
c_i,
c_j,
k,
E,
A,
t
),
$$

其中：

- $c_i,c_j$：原 classes；
- $k$：relation type；
- $E$：證據；
- $A$：執行者／agent；
- $t$：時間。

每次 split：

$$
S_t
=
(
c,
\{c_1,\ldots,c_m\},
reason,
t
).
$$

這和版本控制一樣重要。

---

# 60. 不同 relation 需要不同 verifier

| Relation | 最低合理 verifier |
|---|---|
| $\sim_{lex}$ | deterministic normalization |
| $\sim_{\alpha}$ | binder-aware structural checker |
| $\sim_{def}$ | formal elaborator / definitional equality |
| $\sim_{prop}$ | mutual implication proof or strong formal evidence |
| $\sim_{route}$ | audited route graph mapping |
| $\sim_{obs}$ | canonical failure-condition audit |
| $\sim_{evid}$ | provenance + evidence dependency audit |

這個表顯示：

$$
\boxed{
\text{沒有一個 universal similarity score 能取代全部 relation}.
}
$$

---

# 61. LLM 在 quotient pipeline 中最適合的角色

LLM 很適合：

- semantic candidate retrieval；
- assumption extraction；
- route labeling；
- obstruction paraphrase clustering；
- graph alignment proposal；
- merge explanation；
- split hypothesis。

但 LLM 不應單獨作：

$$
\text{formal equivalence oracle}.
$$

比較合理：

$$
\boxed{
\text{LLM proposes}
\rightarrow
\text{formal / structural checker audits}
\rightarrow
\text{human or multi-agent review for high-risk cases}.
}
$$

---

# 62. 商空間與 theorem discovery

如果系統發現：

$$
g_1,\ldots,g_n
$$

表面完全不同，但：

$$
[g_1]_{route}
=
\cdots
=
[g_n]_{route},
$$

且它們跨不同 mathematical domains，

這可能反而揭露一個更一般 theorem schema。

也就是：

$$
\text{deduplication}
\rightarrow
\text{abstraction}.
$$

因此 quotient 不只是刪除重複。

它也可能生成：

$$
\boxed{
\text{higher-level theorem family}.
}
$$

---

# 63. 從等價類反推出 invariant

若一組 artifact：

$$
\{g_i\}_{i=1}^n
$$

被判定為 route-equivalent，

可以尋找：

$$
I(g_i)=I^\star
$$

的共同 invariant。

這個 $I^\star$ 可能是：

- proof motif；
- conserved quantity；
- compactness pattern；
- duality；
- monotonicity；
- obstruction form。

因此：

$$
\boxed{
\text{quotient class}
\rightarrow
\text{invariant mining}.
}
$$

這是從資料庫工程進入新數學的一條可能路。

---

# 64. 「越是真理越可能像廢話」與 quotient 的關係

如果大量不同表達：

$$
g_1,\ldots,g_n
$$

在高階 quotient 後都收斂到：

$$
[g]^\star,
$$

那表面複雜度：

$$
K_{surface}
$$

可以很大，

但核心描述長度：

$$
K_{core}
$$

可能很小。

形式上：

$$
K_{core}
\ll
K_{surface}.
$$

這正好提供本系列後續「真理—生成性反轉」的一個資訊論入口：

> 大量理論展開可能在 quotient 後收斂成極短核心，而極短核心又可以生成大量展開。

但本文暫不把這解讀為「真理必然簡單」。

这里只建立可測結構。

---

# 65. Quotient 不等於 reductionism

把兩篇研究歸入同 route class，不代表：

> 它們所有意義都一樣。

商化只在指定 relation 下成立。

所以應寫：

$$
g_i\sim_{route}g_j,
$$

而不是：

$$
g_i=g_j.
$$

同樣：

$$
g_i\sim_{prop}g_j
$$

不表示其：

- 歷史意義；
- 教學價值；
- proof elegance；
- search difficulty；
- computational cost；

都相同。

---

# 66. 多商空間表示

最終一份 artifact 應同時有多個 identity：

$$
\operatorname{ID}(g_i)
=
(
[g_i]_{prop},
[g_i]_{route},
[g_i]_{obs},
[g_i]_{evid},
\rho_i
).
$$

這可以看成一個 product-like index：

$$
\mathcal I
=
\mathcal Q_{prop}
\times
\mathcal Q_{route}
\times
\mathcal Q_{obs}
\times
\mathcal Q_{evid}
\times
\mathcal R.
$$

不是所有組合都可達。

但這比單一 document ID 更接近研究身份。

---

# 67. Quotient lattice 的版本

可將不同 coarse-graining 寫成：

$$
\Omega^{raw}
\rightarrow
\Omega^{\alpha}
\rightarrow
\Omega^{def}
\rightarrow
\Omega^{prop}.
$$

另外：

$$
\Omega^{raw}
\rightarrow
\Omega^{route}
\rightarrow
\Omega^{obs}.
$$

這兩條不是同一條鏈。

可以畫成：

```text
              Ω_raw
             /     \
            v       v
      Ω_statement  Ω_route
         |            |
         v            v
       Ω_prop        Ω_obs
             \      /
              \    /
             meta-classes
```

這個 lattice structure 比單一 embedding cluster 更適合研究空間。

---

# 68. Quotient uncertainty 應進入 coverage error bar

如果 equivalence graph 中有大量：

$$
?
$$

邊，

則：

$$
N_{eff}
$$

不是一個確定值。

可以定義上下界：

$$
N_{\mathrm{eff}}^{-}
\leq
N_{\mathrm{eff}}
\leq
N_{\mathrm{eff}}^{+}.
$$

其中：

- 下界：把所有可能等價候選盡量合併；
- 上界：把未確定 pair 保守分開。

coverage 也應輸出：

$$
[\widetilde C^{-},\widetilde C^{+}].
$$

這比給出虛假的單點百分比更誠實。

---

# 69. 商空間審計的最小 benchmark

可建立 synthetic benchmark：

### 類型 A：純 $\alpha$-rename

應被合併。

### 類型 B：定義展開

應在 definitional layer 合併。

### 類型 C：量詞交換

不應合併。

### 類型 D：假設減弱／加強

應標成 implication relation，不是 equivalence。

### 類型 E：同 theorem 不同 proof

proposition 合併，route 分開。

### 類型 F：不同 theorem 同 route skeleton

proposition 分開，route 合併。

### 類型 G：不同 route 同 obstruction

route 分開，obstruction 合併。

若系統連這七類都不能穩定區分，則不應用於 proof-space saturation claim。

---

# 70. 等價以外還需要 implication graph

很多研究產物不是：

$$
Q_i\leftrightarrow Q_j,
$$

而是：

$$
Q_i\Rightarrow Q_j.
$$

例如一個 stronger theorem：

$$
Q_s
$$

推出 weaker theorem：

$$
Q_w.
$$

若把兩者強行 quotient，會丟掉 theorem strength。

因此除了 equivalence graph：

$$
\mathcal E,
$$

還要有 implication DAG：

$$
\mathcal D_{imp}.
$$

這使研究空間不只有 class，還有 partial order。

---

# 71. Theorem strength lattice

若：

$$
Q_1\Rightarrow Q_2,
$$

$$
Q_2\not\Rightarrow Q_1,
$$

則：

$$
Q_1
$$

較強。

可定義：

$$
Q_1\succeq Q_2.
$$

這形成 theorem-strength preorder。

它對 dedup 非常重要，因為很多看似「重複」其實是：

- generalization；
- specialization；
- corollary；
- strengthening；
- weakening。

Rocq goal clone work 把 generalization 單獨分類，正好提醒這一點。

---

# 72. 「同一條路」也可能存在強弱關係

Route A：

$$
A
\rightarrow
L
\rightarrow
C.
$$

Route B：

$$
A
\rightarrow
L'
\rightarrow
L
\rightarrow
C.
$$

若 $L'$ 只是更一般的 bridge，

兩 route 不必完全 equivalence。

可以有：

$$
R_A\preceq R_B.
$$

因此 route space 也可以具有 refinement order。

這將在後續 proof-route dynamics 中很有用。

---

# 73. Quotient-aware novelty decay

原始 novelty decay：

$$
\nu_N^{raw}\rightarrow0
$$

可能只是文本變得相似。

真正有意思的是：

$$
\nu_N^{prop}\rightarrow0,
$$

$$
\nu_N^{route}\rightarrow0,
$$

$$
\nu_N^{obs}\rightarrow0.
$$

如果三者發生在不同時間：

$$
T_{prop}
<
T_{route}
<
T_{obs},
$$

就表示不同層次的 saturation phase transition。

這直接預告 LSI-PSD-04 與 05。

---

# 74. Quotient phase diagram

可以建立：

$$
\mathbf Z_N
=
(
\Delta N_{prop},
\Delta N_{route},
\Delta N_{obs},
\operatorname{RSI},
H_{route}
).
$$

不同區域代表：

### Phase A：新命題、新路線

$$
\Delta N_{prop}>0,
\quad
\Delta N_{route}>0.
$$

### Phase B：命題重訪、路線創新

$$
\Delta N_{prop}\approx0,
\quad
\Delta N_{route}>0.
$$

### Phase C：路線重訪、障礙創新

$$
\Delta N_{route}\approx0,
\quad
\Delta N_{obs}>0.
$$

### Phase D：高度 confluence

$$
\Delta N_{route}\approx0,
\quad
\Delta N_{obs}\approx0,
\quad
m(c)\uparrow.
$$

這比「文章越來越像」精確得多。

---

# 75. 商空間與 local basin

假設 route quotient 得到：

$$
\mathcal C_{route}.
$$

再以 transition / dependency 連接 classes：

$$
\mathcal G_{route}.
$$

高密度子圖：

$$
B_k
\subset
\mathcal G_{route}
$$

可以作為 proof basin 候選。

這樣 LSI-PSD-05 的 local saturation 就有一個乾淨的底層：

$$
\text{basin}
=
\text{quotient-aware route subgraph}.
$$

沒有 quotient，basin 密度可能只是 duplicate density。

---

# 76. 商空間與 obstruction confluence

若：

$$
R_1,R_2,\ldots,R_m
$$

在 route quotient 下彼此不同：

$$
[R_i]_{route}\neq[R_j]_{route},
$$

但：

$$
[O(R_i)]_{obs}
=
[O^\star]_{obs},
$$

則才真正構成：

$$
\boxed{
\text{obstruction confluence}.
}
$$

如果 route 本身其實都是同一條，只是換 notation，那不能叫 confluence。

所以 LSI-PSD-06 完全依賴本文。

---

# 77. 商空間與 productive mis-specification

後續 LSI-PSD-08 / 09 會研究：

$$
\text{parent framing}
\rightarrow
\text{descendant theories}.
$$

若 descendant corpus 不 quotient，就會高估 generativity。

真正的 generativity 應計：

$$
G_{eff}
=
|\{[T_i]_{prop}\}|
$$

或更強：

$$
G_{route},
\quad
G_{transfer}.
$$

因此「錯誤問題很會生理論」也必須先去除表面重複。

---

# 78. 研究系統的 canonical record

本文建議最小 schema：

```yaml
artifact_id: ...
source_hash: ...
parent_artifacts: [...]
statement:
  raw: ...
  formal: ...
quantifiers: [...]
domains: [...]
assumptions: [...]
claims: [...]
dependencies: [...]
route:
  nodes: [...]
  edges: [...]
obstructions: [...]
evidence: [...]
verification:
  status: ...
  tool: ...
representation:
  language: ...
  library: ...
  notation_profile: ...
equivalence:
  proposition_class: ...
  route_class: ...
  obstruction_class: ...
  unresolved_links: [...]
provenance:
  created_at: ...
  agent: ...
  lineage: ...
```

這不是論文本身。

它是 observatory 的導航層。

---

# 79. Canonical record 不可取代原始 source

永遠保持：

$$
F(g)\neq g.
$$

feature record：

$$
F(g)
$$

用來：

- 搜尋；
- graph；
- quotient；
- metrics。

原始 source：

$$
g
$$

用來：

- audit；
- reconstruction；
- citation；
- re-extraction。

這與 canonical source policy 完全一致。

---

# 80. 商空間的工程複雜度

全 pair comparison：

$$
\binom{N}{2}
=
O(N^2).
$$

當：

$$
N=10^5,
$$

不可直接對每 pair 做 formal equivalence proof。

因此採分層：

$$
O(N\log N)
$$

級 retrieval，

加上：

$$
O(NK)
$$

候選 pair，

再對少數高風險 pair 做昂貴 audit。

工程上：

$$
\boxed{
\text{cheap broad filter}
+
\text{expensive narrow verifier}.
}
$$

---

# 81. 風險分層

## 81.1 低風險 merge

- exact hash；
- deterministic whitespace；
- certified $\alpha$-equivalence。

可以自動。

## 81.2 中風險 merge

- definitional equality；
- structural canonicalization；
- obvious corollary mapping。

需要 formal tool。

## 81.3 高風險 merge

- natural-language semantic equivalence；
- route equivalence；
- obstruction equivalence；
- cross-domain theorem schema。

需要 audit，不能自動 destructive merge。

---

# 82. Falsification protocol

本文框架可以被實證挑戰。

若未來發現：

1. quotient correction 幾乎不改變任何 long-horizon novelty statistics；
2. representation sensitivity 在成熟 prover 上消失；
3. route equivalence 無法可靠抽取；
4. obstruction classes 不具跨 artifact 穩定性；
5. quotient-aware scheduler 不比 raw retrieval 降低重複；

那麼本文對 proof-space science 的實用價值應被下修。

這些都是可測的。

---

# 83. 實驗假說一：Raw novelty 會系統性高估 route novelty

提出：

$$
H_1:
\mathbb E[\nu^{raw}]
>
\mathbb E[\nu^{route}]
$$

在長程生成 corpus 後期成立。

這不是數學定理。

它是 corpus-level hypothesis。

---

# 84. 實驗假說二：表示敏感性在 LLM prover 中非零

提出：

$$
H_2:
\operatorname{RSI}(Q;R)>0
$$

對相當比例 theorem class 成立。

現有 representation-symmetry 研究已提供直接外部支持，但具體值依 prover 與 benchmark 而變。

---

# 85. 實驗假說三：Obstruction class 數量會比 route class 更早顯示收斂

在高難度長程問題中，可能：

$$
N_{obs}
\ll
N_{route}.
$$

如果很多不同 route 都撞少數障礙，就會：

$$
\operatorname{QCR}_{obs}
\gg
\operatorname{QCR}_{route}.
$$

這是 confluence-rich regime 的一個可測 signature。

---

# 86. 實驗假說四：Quotient-aware memory 會降低無效重複

比較：

$$
R_{raw}
$$

與：

$$
R_{quot}.
$$

若：

$$
\operatorname{DuplicateRate}(R_{quot})
<
\operatorname{DuplicateRate}(R_{raw})
$$

且：

$$
\operatorname{VerifiedNovelty}(R_{quot})
\geq
\operatorname{VerifiedNovelty}(R_{raw}),
$$

則 quotient-aware research memory 有工程價值。

---

# 87. 實驗假說五：保留 representation fibers 會提高 search robustness

若對同一 proposition class 保存多個 representation：

$$
\rho_1,\ldots,\rho_m,
$$

並在 test time 做 representation ensemble，

可能提高：

$$
P(\operatorname{success}).
$$

這與 symmetry aggregation 的既有研究方向一致。

因此正確 quotient 不是把表示刪掉。

而是：

$$
\boxed{
\text{把表示掛到同一數學身份下面}.
}
$$

---

# 88. 十個核心命題

## 命題一：Raw Count Non-Identity

$$
\boxed{
N_{raw}
\neq
N_{semantic}.
}
$$

## 命題二：Similarity Non-Equivalence

$$
\boxed{
\operatorname{Sim}(g_i,g_j)\uparrow
\not\Rightarrow
g_i\sim_{prop}g_j.
}
$$

## 命題三：Mathematical/Search Identity Separation

$$
\boxed{
g_i\sim_{prop}g_j
\not\Rightarrow
\sigma_i=\sigma_j.
}
$$

## 命題四：Representation Sensitivity

$$
\boxed{
\operatorname{RSI}>0
}
$$

可使數學冗餘表示保有搜尋價值。

## 命題五：Evidence Preservation

$$
\boxed{
[g_i]_{claim}=[g_j]_{claim}
\not\Rightarrow
[E_i]=[E_j].
}
$$

## 命題六：Non-Premature Quotient

$$
\boxed{
\text{先保存可重建差異，再商化}.
}
$$

## 命題七：Quotient-Dependent Saturation

$$
\boxed{
\text{Saturation}
=
\text{relation-dependent}.
}
$$

## 命題八：Higher-Order Dependence

$$
\boxed{
\text{高階採樣量測依賴低階 quotient discipline}.
}
$$

## 命題九：Confluence Requires Distinct Routes

$$
\boxed{
\text{同 obstruction 的多次出現}
\neq
\text{confluence}
}
$$

除非來源 route 在適當 quotient 下確實不同。

## 命題十：Quotient Is an Index Layer

$$
\boxed{
\text{quotient}
\neq
\text{destructive deletion}.
}
$$

---

# 89. 符號表

| 符號 | 意義 |
|---|---|
| $\Omega_R^{raw}(Q)$ | 原始研究產物空間 |
| $\sim_{lex}$ | 字面／表面規範化等價 |
| $\sim_{\alpha}$ | 變數重命名等價 |
| $\sim_{def}$ | 定義展開等價 |
| $\sim_{prop}$ | 背景理論下命題等價 |
| $\sim_{route}$ | proof-route skeleton 等價 |
| $\sim_{obs}$ | obstruction family 等價 |
| $\sim_{evid}$ | evidence 等價 |
| $\Omega_R^{math}$ | 數學命題商空間 |
| $\Omega_R^{search}$ | 保留 representation 的搜尋狀態空間 |
| $\Gamma_i$ | route graph |
| $\operatorname{RSI}$ | Representation Sensitivity Index |
| $m(c)$ | equivalence class multiplicity |
| $N_{\mathrm{eff}}$ | 有效樣本數 |
| $\operatorname{SRR}$ | Semantic Redundancy Ratio |
| $\operatorname{QCR}$ | Quotient Compression Ratio |
| $H_{route}$ | route-family entropy |
| $\boldsymbol\nu_i$ | 多層 novelty vector |
| $\mathcal E$ | equivalence graph |
| $\mathcal D_{imp}$ | implication graph |
| $\operatorname{IRS}$ | independent rediscovery score |

---

# 90. 與前兩篇的依賴

**依賴：**

- LSI-PSD-01：定義研究制度、proof-space 與 epistemic firewall；
- LSI-PSD-02：定義 logic-space integration、coverage vector、local basin 與 marginal research yield。

本文對 LSI-PSD-02 做一個必要修正：

$$
\boxed{
\text{所有 coverage 與 novelty 指標，都必須說明其 quotient policy}.
}
$$

否則：

$$
\text{coverage}
$$

可能只是：

$$
\text{text proliferation}.
$$

---

# 91. 對後續系列的依賴

LSI-PSD-04 將使用本文的：

$$
\Omega/\sim
$$

建立：

$$
\Omega^{(0)},
\Omega^{(1)},
\Omega^{(2)},\ldots
$$

高階 proof-space sampling。

LSI-PSD-05 將把 quotient-aware route graph 分解為 local basins。

LSI-PSD-06 將在：

$$
\sim_{route}
$$

與：

$$
\sim_{obs}
$$

上正式定義 obstruction confluence。

LSI-PSD-07 至 09 會用：

$$
N_{\mathrm{eff}}
$$

與 descendant quotient，避免把表面理論數量誤認成 generativity。

LSI-PSD-12 將把本文 schema 實作成 Proof-Space Observatory 的 equivalence registry。

---

# 92. 結論：研究空間的第一個問題不是「有多少」，而是「哪些其實是同一個」

AI 可以很便宜地生成：

$$
10^2,
\quad
10^3,
\quad
10^4
$$

份數學研究稿。

但 raw count 只告訴我們：

$$
\text{有多少檔案}.
$$

它沒有告訴我們：

$$
\text{有多少命題},
$$

$$
\text{有多少 proof routes},
$$

$$
\text{有多少 obstruction},
$$

$$
\text{有多少獨立 evidence}.
$$

因此長程 AI 數學研究的第一個統計修正，不是再加一個更漂亮的 embedding。

而是建立：

$$
\boxed{
\textbf{Semantic Quotient Space}.
}
$$

本文的核心不是主張所有重複都該刪除。

恰恰相反。

它主張同一 artifact 必須同時被看成：

$$
\text{mathematical object}
$$

與：

$$
\text{search event}.
$$

在數學層：

$$
Q_i\sim_{prop}Q_j
$$

可以被視為同一命題類。

在搜尋層：

$$
(Q_i,\rho_i)
$$

與：

$$
(Q_j,\rho_j)
$$

仍可能是不同實驗條件。

因此最終架構不是：

$$
\text{deduplicate everything}.
$$

而是：

$$
\boxed{
\text{quotient what is mathematically redundant,
preserve what is dynamically informative,
and keep every source reconstructable}.
}
$$

這使 proof-space science 能夠第一次回答：

> 一萬篇論文裡，到底有多少是真的新數學狀態？多少只是同一狀態的不同表示？多少是同一命題的不同 proof route？多少不同 route 最後又撞上同一 obstruction？哪些重複是浪費，哪些重複反而是獨立驗證或搜尋對稱性資訊？

沒有這層，後續的「二階、三階、X 階採樣」「局部飽和」「障礙匯流」「真理—生成性反轉」都可能只是文字統計的幻覺。

有了這層，研究 corpus 才開始從：

$$
\text{document pile}
$$

轉成：

$$
\boxed{
\text{auditable quotient-aware proof-space memory}.
}
$$

---

# 參考文獻

1. Olejniczak, K., Dimitrov, R., Huang, X., Cuenca Grau, B., Kim, J., Ceylan, İ. İ. **What are the Right Symmetries for Formal Theorem Proving?** arXiv:2605.22257 (2026). https://arxiv.org/abs/2605.22257
2. Ghanbari, A. **Automatic Goal Clone Detection in Rocq.** *39th European Conference on Object-Oriented Programming (ECOOP 2025)*, LIPIcs 333, 12:1--12:19. DOI: 10.4230/LIPIcs.ECOOP.2025.12. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2025.12
3. Liu, X., Zhu, T., Dong, Z., Liu, Y., Guo, Q., Liu, Z., Chen, Y., Luo, T. **ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity.** arXiv:2509.22246 (2025; accepted ICLR 2026). https://arxiv.org/abs/2509.22246
4. Liu, Y., Zhu, T., Liu, X., Chen, Y., Liu, Z., Guo, Q., Zhang, J., Bao, K., Luo, T. **Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization.** arXiv:2507.07399 (2025). https://arxiv.org/abs/2507.07399
5. Kripner, M., Šustr, M., Straka, M. **LeanTree: Accelerating White-Box Proof Search with Factorized States in Lean 4.** arXiv:2507.14722 (2025). https://arxiv.org/abs/2507.14722
6. Li, X. et al. **ProofGym: Unifying LLM-Based Theorem Proving Across Formal Systems.** MATH-AI Workshop at NeurIPS 2025. https://neurips.cc/virtual/2025/131121
7. Hubert, T. et al. **Olympiad-level formal mathematical reasoning with reinforcement learning.** *Nature* (2025). https://www.nature.com/articles/s41586-025-09833-y
8. Qian, Y., Clune, J., Barrett, C., Avigad, J. **Lean-auto: An Interface between Lean 4 and Automated Theorem Provers.** CAV 2025; arXiv:2505.14929. https://arxiv.org/abs/2505.14929
9. Dong, K., Ma, T. **STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving.** *Proceedings of ICML 2025*, PMLR 267. https://proceedings.mlr.press/v267/dong25h.html
10. **ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings.** arXiv:2510.15681 (2025). https://arxiv.org/abs/2510.15681
11. **Minif2f in Rocq: Automatic Translation Between Proof Assistants — A Case Study.** MATH-AI 2025, OpenReview. https://openreview.net/forum?id=wkELXtGZa6
12. Stanford Encyclopedia of Philosophy. **Automated Reasoning.** Summer 2025 Edition. https://plato.stanford.edu/archives/sum2025/entries/reasoning-automated/

---

# 版本與非主張

## 本文主張

- 大規模 AI 數學 corpus 的 raw artifact count 不能直接視為 proof-space sample count。
- 字串相似、結構相似、命題等價、route 等價與 obstruction 等價必須分離。
- 數學身份與搜尋身份不同；數學上等價的表示仍可能對 prover 具有不同搜尋難度。
- embedding 與 LLM semantic judgment 適合作 candidate generation，不應單獨作 equivalence proof。
- quotient 必須保留 source fiber、evidence 與 provenance。
- saturation、novelty、coverage 都必須標示使用哪一層 quotient。
- high-order proof-space sampling 需要 lower-order quotient discipline。

## 本文不主張

1. 已存在一個對所有數學語料通用且完備的語義等價判定器；
2. embedding 相似度可替代形式互推證明；
3. route graph similarity 自動構成數學 equivalence relation；
4. 所有表示差異都應被刪除；
5. 所有重複都是浪費；
6. 同一 proposition 的不同 proof 沒有研究價值；
7. NS-203 的 203 篇已被本文正式壓縮成確定數量的 route classes；
8. quotient class 數量可以直接除以某個未知 proof-space denominator；
9. representation sensitivity 證明了任何公開未解問題被「錯誤表述」；
10. 本文已建立全域可計算的 mathematical canonical form。

---

**END OF LSI-PSD-03 v2.0 Expanded Edition**


<!-- END LSI-PSD-03 -->

---


<!-- BEGIN LSI-PSD-04 -->

# LSI-PSD-04 — 高階證明空間採樣：從狀態、路徑到路徑之間的關係

## Higher-Order Proof-Space Sampling: From States and Routes to Relations Among Routes

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 04  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Higher-Order Sampling and Route-Relation Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文提出「高階證明空間採樣」作為長程 AI 數學研究的操作性框架。本文中的一階、二階、三階與 $k$ 階，描述的是**研究對象的階層**：狀態、狀態間轉換、轉換間關係，以及關係之上的關係；它們不等同於微積分中的導數階數、攝動展開階數、張量階數、邏輯的高階語言階數或任何既有數學術語中的「order」。本文所有高階分類首先是 proof-space observatory 的研究標記；除非另有形式證明，不得把「某篇論文出現 second-order / higher-order 字樣」直接當成高階 proof-space sampling 的證據。本文不主張有限 corpus 的高階重訪能證明某未解命題錯誤、不可證、獨立或定義失敗。

---

## 摘要

當一個 AI 數學研究系統只做數十輪工作時，「找到新的命題、引理、估計、表示或反例候選」通常足以描述研究進展；但當同一問題被持續研究數百、數千甚至更多輪之後，研究對象會逐漸發生階層轉移。系統不再只採樣「證明空間中的點」，而開始採樣「從一個點到另一個點的轉換」；當多條不同路徑反覆撞上同一障礙時，研究又會轉向「路徑與路徑之間的關係」；當這些關係本身出現匯流、反饋、再進入與族級 no-go 結構時，研究便開始進入更高階的 proof-space sampling。

本文建立一個可操作的高階證明空間框架。令固定問題 $Q$、搜尋制度 $R$ 下的可觀測研究狀態空間為：

$$
\Omega_R^{(0)}(Q).
$$

本文把 proof move、representation change、lemma introduction、normalization、rescaling、compactness passage、contradiction step 等可審計轉換視為一階關係物件：

$$
\Omega_R^{(1)}(Q)
=
\mathcal T(\Omega_R^{(0)}(Q)).
$$

接著，若研究開始比較兩條或多條 proof route 是否同構、是否匯流到共同 obstruction、是否共享同一依賴核、是否可互相替換，則研究對象進入：

$$
\Omega_R^{(2)}(Q)
=
\mathcal R(\Omega_R^{(1)}(Q)).
$$

更一般地，本文以型別化遞迴表示：

$$
\Omega_R^{(k+1)}(Q)
=
\mathcal F_k(\Omega_R^{(k)}(Q)),
$$

其中 $\mathcal F_k$ 不被預設為單一函數空間，而是一族允許的關係、組合、等價、匯流、回饋與族級摘要算子。

本文的核心主張不是「研究階數越高越接近真理」，而是：**當一階 novelty 下降時，高階關係仍可能持續產生新資訊；因此只以新 theorem count 或新文本比例衡量長程研究，會漏掉重要的結構性進展。** 為此，本文定義 order-conditioned novelty：

$$
\nu_k(N),
$$

order-conditioned coverage：

$$
I_k(N),
$$

order-conditioned audited yield：

$$
\rho_k(N),
$$

以及 confluence degree、re-entry depth、route-family entropy、feedback depth、higher-order survival ratio 等觀測量。本文進一步定義 $K$ 階局部飽和：只有當指定 basin 中從 $0$ 階到 $K$ 階的新增已驗證等價類同時持續接近零，才可把該 basin 標為「$K$-order locally saturated」。即使如此，依照 LSI-PSD-01 的證明空間非結論原則，也不能推出底層數學空間已被耗盡。

本文把 2025--2026 年 formal theorem proving 的最新發展視為工程佐證而非等價物。LeanNavigator 直接把 Lean proof search 表示為 state-transition graph；LeanProgress 從局部 tactic prediction 轉向全 proof trajectory 的剩餘步數預測；AlphaProof 使用 proof-state representation 與 tree search；Goedel-Architect、LEAP 與 LeanMarathon 以 lemma dependency graph、blueprint 與 AND-OR DAG 保存全域證明結構；Chain-of-States 工作則顯式把 informal proof 轉為中介 proof-state 序列。這些系統共同說明：現代 theorem proving 已經把「狀態、轉換、軌跡、依賴圖」視為可計算物件，但目前主流目標仍主要是提高 proof success。本文則把相同類型的結構提升為**研究科學的觀測對象**，詢問不同路由如何重訪、匯流、被排除、形成族級障礙，以及這些關係在長期生成中是否自身飽和。

本文最後將框架套入 NS-203 corpus 作為初步案例。既有 observatory 的 tier 標記被重新解釋為 heuristic evidence，而非本體階數：$T_1$ 表示狀態或新路由採樣，$T_2$ 表示可辨識的回訪／轉換比較，$T_3$ 表示關係、匯流或回饋，$T_X$ 表示族級、all-order 或更高階 recurrence 候選。本文不以這些標記宣稱 Navier--Stokes 已飽和，而只把它們視為建立高階 proof-space observatory 的第一個長程語料測試。

**關鍵詞：** 高階證明空間採樣、proof trajectory、proof state、state-transition graph、route relation、confluence、obstruction、feedback、re-entry、local saturation、order-conditioned novelty、proof-space dynamics、AI 數學研究、Navier--Stokes corpus

---

# 1. 為什麼「又一篇新論文」逐漸不再是正確的研究單位

## 1.1 早期研究的自然單位是候選結果

在一個尚未被大量探索的問題上，研究者自然會問：

- 是否有新的 lemma？
- 是否有新的 estimate？
- 是否有新的 counterexample candidate？
- 是否有新的 representation？
- 是否有新的 proof strategy？

令第 $i$ 次研究產物為：

$$
g_i.
$$

早期可以近似把：

$$
g_i
$$

看成對研究空間的一個新採樣點。

若每個 $g_i$ 都帶來新的已驗證結構，則：

$$
\Delta I_0(i)>0.
$$

這時候「論文數」「lemma 數」「新概念數」雖然粗糙，仍有一定解釋力。

## 1.2 長程研究會改變問題本身的資料結構

當研究進入數百輪之後，常出現以下模式：

1. 新 representation 其實導回以前見過的 obstruction；
2. 新 lemma 只是舊 lemma 在不同尺度或座標下的改寫；
3. 不同 method family 共享同一個失敗核心；
4. 研究開始問「為什麼這幾條路都失敗？」；
5. 某個 no-go 不再只排除一個 lemma，而排除一整族 escalation；
6. 某條已排除路線在新的 parent assumption 下重新進場；
7. failure trace 本身成為下一輪的研究資料。

此時，研究的資訊不只存在於：

$$
\{g_i\}_{i=1}^N.
$$

還存在於：

$$
\{g_i\to g_j\},
$$

以及：

$$
\{(g_i\to g_j)\sim(g_p\to g_q)\},
$$

甚至存在於「這些關係之間的關係」。

因此長程研究真正需要的資料結構不是平面文件庫，而是一個分層關係系統。

## 1.3 本文的核心問題

本文問：

> 當研究系統開始反覆研究「路徑怎麼走」「不同路徑為什麼匯流」「匯流之後又如何形成新的反饋」時，我們應如何定義它正在採樣的對象？

答案不能只是：

> 它又寫了一篇 paper。

因為 paper 是容器，不是 proof-space 的自然型別。

---

# 2. 與現代 formal theorem proving 的接點

## 2.1 Proof state 已經是工程上的標準物件

在 interactive theorem proving 中，一個中間狀態不是模糊的「想法」，而可以是明確的 formal state：

$$
s_t
=
(\Gamma_t,G_t,M_t),
$$

其中：

- $\Gamma_t$ 是當前 local context；
- $G_t$ 是尚未關閉的 goals；
- $M_t$ 是 tactic、library、identifier 或其他 metadata。

對 tactic $a_t$，proof assistant 執行：

$$
s_{t+1}
=
T(s_t,a_t).
$$

這本身已是一個動力系統式描述。

## 2.2 LeanNavigator：證明可以被表示成 state-transition graph

Yin 與 Gao 在 2025 年的 LeanNavigator 工作中，直接把 Lean proof exploration 描述為 state graph：節點是 Lean states，邊是 tactic transitions。這個設計用於大量生成可驗證的 theorem-proof data，證明「完整 proof script」並不是唯一合理的資料單位。

其最簡單形式可寫成：

$$
\mathcal G_{state}
=
(V_s,E_t),
$$

其中：

$$
V_s=\{s_0,s_1,\ldots\},
$$

$$
E_t\subseteq V_s\times\mathcal A\times V_s.
$$

這為本文的 $\Omega^{(0)}$ 與 $\Omega^{(1)}$ 提供了直接工程類比。

## 2.3 LeanProgress：從局部 tactic 轉向全局 trajectory

LeanProgress 的核心動機是：只預測下一步 tactic，不足以知道目前是否真的接近完成。其 progress predictor 估計從某 proof state 到完成還需要多少步。

可抽象為：

$$
P_{rem}(s_t)
\approx
\operatorname{dist}(s_t,S_{done}).
$$

這裡已經出現一個重要轉變：

$$
\text{local action quality}
$$

與：

$$
\text{global trajectory position}
$$

不是同一個量。

對長程研究而言也一樣。一篇局部看似新的論文，可能只是在舊 route 上向前或向後移動；真正的 novelty 要看它在整體 trajectory graph 中的位置。

## 2.4 AlphaProof 與 tree search

2025 年公開於 Nature 的 AlphaProof 將 Lean proof state、policy/value-like guidance 與專門 tree search 結合，顯示 proof solving 可以被視為對巨大狀態樹的策略性探索。

但 tree search 的成功也提醒我們：

$$
\text{visit count}
\neq
\text{semantic coverage}.
$$

同一語義區域可以因 representation、branching 與 tactic surface 被多次造訪。

因此本文不直接把 search tree depth 當高階採樣階數。

## 2.5 Goedel-Architect、LEAP 與 blueprint graph

2026 年的 Goedel-Architect 把大型 theorem proof 先表成 definition / lemma dependency blueprint，再平行關閉 open lemma nodes；若失敗，則用 failure 反向修改 blueprint。

可抽象為：

$$
\mathcal B
=
(V_L,E_D),
$$

其中：

$$
V_L
=
\{\text{definitions and lemmas}\},
$$

$$
E_D
=
\{\text{declared dependencies}\}.
$$

LEAP 同樣以 hierarchical decomposition 與 AND-OR DAG 維持證明計畫，而 LeanMarathon 則把 evolving blueprint 當成長程 multi-agent formalization 的共享系統紀錄。

這幾個系統共同指出：

$$
\boxed{
\text{Proof solving itself already needs graph-level memory.}
}
$$

本文進一步問：

$$
\boxed{
\text{Long-horizon research needs graph-of-graphs memory嗎？}
}
$$

答案至少在操作上是肯定的。

## 2.6 Chain of States：中介狀態是可生成的研究物件

2025 年 Chain-of-States 工作把 informal reasoning 分解成一系列中介 formal states，再生成 adjacent transitions 所需的 tactics。這說明 proof trajectory 不是只有 solver 內部才存在，它也可以作為跨 representation 的明確中介語言。

本文將這個觀念一般化：

> 不只 theorem proof 可以被拆成 states；長程 research program 也可以被拆成 research states，而 research transitions 本身可以成為下一階研究對象。

---

# 3. 型別先行：避免把所有「階」混成一團

## 3.1 Order 不是形容詞，而是研究對象的型別

本文定義一個 sampling order map：

$$
\operatorname{ord}:\mathcal X\to\mathbb N_0.
$$

其中：

$$
\operatorname{ord}(x)=k
$$

表示研究產物 $x$ 的主要新資訊位於 $k$ 階 proof-space object。

這不是說 $x$ 只能包含一種階數，而是說其 novelty claim 的主型別是什麼。

## 3.2 一個最重要的反例

若某篇 PDE 論文研究：

$$
\partial_t^2 u,
$$

或者寫出：

$$
\text{second-order correction},
$$

它完全可能仍然只是一階 proof-state sampling。

因此：

$$
\boxed{
\text{Mathematical order}
\neq
\text{proof-space sampling order}.
}
$$

同理：

$$
\text{higher-order logic}
$$

不自動等於本文的 higher-order proof-space sampling。

## 3.3 型別錯置會製造假的高階訊號

假設 corpus 中有 100 篇文章含有字串：

`second-order`。

直接計數只能得到：

$$
N_{lex}(`second-order`)=100.
$$

它不能推出：

$$
N_{proof}^{(2)}=100.
$$

本文因此要求：高階判定必須使用結構證據，而不是單字證據。

---

# 4. 零階空間：研究狀態與候選數學物件

## 4.1 定義零階 proof-space object

對問題 $Q$ 與搜尋制度 $R$，令：

$$
\Omega_R^{(0)}(Q)
$$

表示可被系統辨識、保存與比較的基礎 research-state objects。

典型元素包括：

- theorem candidate；
- lemma candidate；
- assumption set；
- counterexample candidate；
- invariant；
- estimate；
- normal form；
- representation；
- obstruction state；
- formal proof state；
- verified partial result。

## 4.2 零階不是「低級」

$0$ 階只是 base type。

一個極深的定理本身仍然可以是：

$$
x\in\Omega^{(0)}.
$$

高階不是價值排序。

因此本文拒絕：

$$
\operatorname{ord}(x)>\operatorname{ord}(y)
\Rightarrow
\operatorname{Value}(x)>\operatorname{Value}(y).
$$

## 4.3 零階 novelty

經過 LSI-PSD-03 的 quotient 後，令 $[x]_0$ 表示零階語義等價類。

第 $N$ 輪的 audited zero-order novelty 可寫成：

$$
\nu_0(N)
=
\frac{
\#\{\text{new audited }[x]_0\text{ introduced near }N\}
}{
\#\{\text{audited zero-order candidates near }N\}
}.
$$

若：

$$
\nu_0(N)\to0,
$$

只能說零階新等價類的邊際產出下降。

不能說：

$$
\Omega^{(0)}
\text{ 已被耗盡}.
$$

---

# 5. 一階空間：從「有什麼」轉向「怎麼走」

## 5.1 Proof move 作為物件

若：

$$
x,y\in\Omega^{(0)},
$$

且某可審計操作 $T$ 使：

$$
T:x\mapsto y,
$$

則可把 $T$ 視為一階物件。

令：

$$
\Omega_R^{(1)}(Q)
=
\{T\mid T:x\to y,\ x,y\in\Omega_R^{(0)}(Q)\}.
$$

## 5.2 一階物件不只 tactic

在長程數學研究中，$T$ 可以是：

- introduce auxiliary quantity；
- switch representation；
- pass to a blow-up sequence；
- normalize；
- rescale；
- take a compactness limit；
- derive contradiction；
- localize；
- integrate by parts；
- apply monotonicity；
- pass from local to global criterion；
- compile informal statement into formal lemma；
- add or remove an assumption；
- transfer a lemma to a neighboring PDE；
- route around an obstruction。

## 5.3 Route 是 transition 的組合

一條 proof route：

$$
r
=
T_m\circ\cdots\circ T_2\circ T_1.
$$

其起點與終點為：

$$
r:x_0\to x_m.
$$

route identity 不能只由終點決定。

可能有：

$$
r_a(x)=r_b(x)=y,
$$

但：

$$
r_a\not\sim_{route}r_b.
$$

因為兩條路使用不同 assumptions、不同 intermediate lemmas 或不同 dependence structure。

## 5.4 何時稱為一階 novelty

如果一篇研究稿只產生一個新 theorem statement，通常主要是零階 novelty。

如果它的核心是：

> 已知 $x$ 與 $y$，本文建立一種以前沒有的可驗證轉換 $T:x\to y$。

則其主要 novelty 可標記為：

$$
\operatorname{ord}=1.
$$

---

# 6. 二階空間：研究不同 proof routes 之間的關係

## 6.1 二階不是再走一次路

如果系統只是：

$$
x\xrightarrow{T}y\xrightarrow{U}z,
$$

這仍然可以只是較長的一階 route。

二階的關鍵不是 composition length，而是研究：

$$
T\quad\text{和}\quad U
$$

之間的關係。

## 6.2 二階關係的基本類型

令：

$$
T_a,T_b\in\Omega^{(1)}.
$$

二階物件可以包括：

### 6.2.1 Route equivalence

$$
T_a\sim_{route}T_b.
$$

表示兩者在指定 quotient 下共享同一 proof skeleton。

### 6.2.2 Route dominance

$$
T_a\preceq T_b.
$$

表示 $T_a$ 的成功條件、成本或 assumption demand 在某意義上優於 $T_b$。

### 6.2.3 Route incompatibility

$$
T_a\perp_R T_b.
$$

表示兩條路需要互相衝突的 assumptions、normalizations 或 representations。

### 6.2.4 Confluence

若：

$$
T_a(x_a)\to O,
$$

$$
T_b(x_b)\to O,
$$

即使 $x_a\neq x_b$，若最終都導向同一 canonical obstruction $O$，則形成 confluence relation。

### 6.2.5 Mutual compensation

某些方法單獨不足，但：

$$
T_a\oplus T_b
$$

能封閉彼此的 error term。

這也是二階關係。

## 6.3 定義二階空間

本文以：

$$
\Omega_R^{(2)}(Q)
=
\mathcal R_1(\Omega_R^{(1)}(Q))
$$

表示一階路由上的可審計關係族。

$\mathcal R_1$ 不是 powerset 的同義詞，而是觀測站實際允許保存的 typed relations。

---

# 7. 三階空間：關係本身開始形成結構

## 7.1 從多條 confluence 到 confluence family

假設已經辨識：

$$
C_1:
T_1,T_2,T_3\to O_1,
$$

$$
C_2:
T_4,T_5\to O_2,
$$

$$
C_3:
T_6,T_7,T_8\to O_1.
$$

現在研究者發現：

$$
C_1\sim C_3.
$$

這時研究對象已不是單條 route，也不是單次 confluence，而是 confluence relations 之間的關係。

這就是三階的典型形式。

## 7.2 Feedback 作為三階訊號

若某個二階結論：

$$
R(T_a,T_b)
$$

被送回搜尋系統，改變下一輪允許的 transitions：

$$
\Pi_{N+1}
=
\Phi(\Pi_N,R(T_a,T_b)),
$$

其中 $\Pi_N$ 是當前 route policy，則形成：

$$
\text{relation}
\to
\text{search-policy update}.
$$

若後續再研究這個 update 是否產生新的 confluence 或 avoidance pattern，便出現明顯的 higher-order feedback。

## 7.3 三階空間

可寫成：

$$
\Omega_R^{(3)}(Q)
=
\mathcal R_2(\Omega_R^{(2)}(Q)).
$$

典型元素包括：

- confluence-of-confluences；
- relation-family equivalence；
- route-class feedback；
- no-go inheritance between method families；
- family-level re-entry；
- repeated obstruction migration pattern。

---

# 8. 一般 $k$ 階空間：必須是 typed recursion，而不是無限制元語言

## 8.1 遞迴定義

本文不嘗試聲稱存在唯一自然的高階 proof-space hierarchy。

操作上定義：

$$
\Omega_R^{(k+1)}(Q)
=
\mathcal F_k(\Omega_R^{(k)}(Q)),
$$

其中：

$$
\mathcal F_k
$$

是一組被 observatory 明確註冊的 higher-order constructors。

## 8.2 Constructor registry

例如：

$$
\mathcal F_k
=
\{
\operatorname{Relate},
\operatorname{Compose},
\operatorname{Quotient},
\operatorname{Converge},
\operatorname{Confluence},
\operatorname{Feedback},
\operatorname{Reenter},
\operatorname{InheritNoGo}
\}.
$$

只有通過這些 typed constructors 產生、並保留 provenance 的物件，才有資格被標為更高階。

## 8.3 為什麼不能讓階數無限制自由膨脹

如果只要說一句：

> 我在思考「我在思考 proof route」

就把階數加一，則：

$$
\operatorname{ord}
$$

會變成修辭遊戲。

因此本文要求：

$$
\boxed{
\text{Higher order requires a new typed relational object with auditable inputs and outputs.}
}
$$

## 8.4 Order ceiling 不是數學天花板

實際 observatory 可能只維護：

$$
k\leq K_{obs},
$$

例如：

$$
K_{obs}=3.
$$

更高階全部先標：

$$
T_X.
$$

這只是資料工程決策，不代表真實研究只有三階。

---

# 9. 四層操作標記：$T_1,T_2,T_3,T_X$

## 9.1 為什麼不用直接把所有 artifact 精確標 $k$

現實 corpus 很髒。

一篇 paper 可能同時包含：

- 新 lemma；
- 舊 route 回訪；
- route comparison；
- family-level no-go。

因此，對 legacy corpus 強行給單一精確階數會過度自信。

本文建議第一版 observatory 採四層 tier：

$$
T_1,
T_2,
T_3,
T_X.
$$

## 9.2 $T_1$：狀態或新路由採樣

判準包括：

- 新 zero-order semantic class；
- 新 proof move；
- 新 route family；
- 未有明確 route-relation novelty。

## 9.3 $T_2$：回訪、transition comparison 或同一 obstruction 的再採樣

需要至少一項結構證據：

- explicit revisit；
- same canonical obstruction under a new route；
- route-to-route comparison；
- reusable transition relation；
- dependency transfer between route families。

## 9.4 $T_3$：relation/confluence/feedback

需要研究對象本身已是 route relations，例如：

- obstruction confluence；
- coupled confluence；
- confluence feedback；
- no-go inheritance between relation families；
- relation-induced policy update。

## 9.5 $T_X$：高階候選，不假裝精確

用於：

- all-order family analysis；
- higher-order recurrence；
- repeated feedback-of-feedback；
- method-family closure；
- evidence 顯示階數超過 observatory 現有 schema。

$T_X$ 不是「無限階」。

它只表示：

$$
\operatorname{ord}(x)>K_{obs}
$$

或：

$$
\operatorname{ord}(x)
\text{ 尚無法可靠解析}.
$$

---

# 10. Order-conditioned novelty：為什麼一階飽和後仍可能有新資訊

## 10.1 單一 novelty 指標會混掉相變

若只定義：

$$
\nu(N),
$$

則無法分辨：

- 新 theorem 下降；
- 新 routes 下降；
- 新 route relations 上升；
- 新 obstruction families 上升。

因此本文改用：

$$
\boldsymbol\nu(N)
=
(\nu_0(N),\nu_1(N),\ldots,\nu_K(N)).
$$

## 10.2 一個典型的高階相變

早期：

$$
\nu_0\gg0,
\qquad
\nu_1\gg0.
$$

中期可能變成：

$$
\nu_0\downarrow,
\qquad
\nu_1>0,
\qquad
\nu_2\uparrow.
$$

再後期：

$$
\nu_0\approx0,
\qquad
\nu_1\approx0,
\qquad
\nu_2>0.
$$

這表示不是「研究死了」，而是 novelty 從 object level 移到 relational level。

## 10.3 Order-conditioned novelty 定義

令第 $k$ 階經 audited quotient 後的等價類集合為：

$$
\mathcal C_k(N).
$$

定義窗口 $W$ 內的新類率：

$$
\nu_k^{(W)}(N)
=
\frac{
|\mathcal C_k(N-W+1:N)\setminus\mathcal C_k(1:N-W)|
}{
\max(1,|\mathcal C_k(N-W+1:N)|)
}.
$$

這個量仍受抽取品質影響，所以必須附：

$$
\operatorname{Conf}_k(N).
$$

## 10.4 不能把低 novelty 自動解釋成 saturation

低：

$$
\nu_k
$$

可能來自：

- extraction model 變差；
- corpus mode 變窄；
- prompt 固化；
- verifier 過度嚴格；
- representation collapse；
- 真正局部飽和。

因此 saturation 需要多指標共同支持。

---

# 11. Order-conditioned coverage：邏輯空間積分的高階版本

## 11.1 從單一積分到積分向量

LSI-PSD-02 定義 proof-space coverage 的理想形式。

本文把它分階：

$$
I_k(N)
=
\int_{\Omega^{(k)}/\sim_k}
c_{k,N}([\xi])\,d\mu_k([\xi]).
$$

因此：

$$
\mathbf I(N)
=
(I_0(N),I_1(N),\ldots,I_K(N)).
$$

## 11.2 不同階的 measure 不必同質

$\mu_0$ 可以關注 theorem/lemma semantic classes。

$\mu_1$ 可以關注 route families。

$\mu_2$ 可以關注 confluence、dominance、incompatibility 等 relation classes。

所以不能把：

$$
I_0+I_1+I_2
$$

當成天然有意義的純量。

需要權重：

$$
I_{agg}(N)
=
\sum_{k=0}^{K}
\lambda_k I_k(N),
$$

且：

$$
\lambda_k
$$

必須由研究目的明示。

## 11.3 Coverage 的真正意義是「已審計可區分結構」

本文再次強調：

$$
I_k
$$

不是「真實數學空間百分之幾已經走完」。

它是：

> 在目前 observatory schema、quotient、evidence rule 與 sampling regime 下，被辨識與審計的第 $k$ 階結構覆蓋代理量。

---

# 12. Confluence：高階採樣最重要的可測訊號之一

## 12.1 定義 canonical obstruction

令：

$$
O\in\mathcal O
$$

表示經 LSI-PSD-03 商化後的 obstruction class。

例如多篇文章雖使用不同語言，但若都可審計地歸結為：

> 某 critical norm 無法被現有 estimate 關閉，

則可候選地歸入同一 $[O]$。

## 12.2 Confluence set

對 obstruction $O$，定義：

$$
\operatorname{In}(O)
=
\{r\in\mathcal R_1:r\to O\}.
$$

confluence degree：

$$
C_{deg}(O)
=
|\operatorname{In}(O)/\sim_{route}|.
$$

它計算的不是文章數，而是**不同 route classes** 有多少條匯入同一 obstruction。

## 12.3 Weighted confluence

若不同 route 的獨立性不同，可定義：

$$
C_w(O)
=
\sum_{[r]\in\operatorname{In}(O)/\sim_{route}}
w_{ind}([r]).
$$

其中：

$$
0\leq w_{ind}\leq1.
$$

## 12.4 高 confluence 的解釋

高：

$$
C_w(O)
$$

可能表示：

1. $O$ 是真正深層的 structural obstruction；
2. observatory quotient 太粗，把不同障礙錯合併；
3. 所有 route 共享隱藏 assumptions；
4. search regime 有共同 blind spot；
5. problem representation 把不同路徑投影到相同表面失敗。

所以 confluence 是診斷訊號，不是判決。

---

# 13. Re-entry：被排除的路徑為什麼還會再次出現

## 13.1 重複不一定是退化

假設 route family $R_a$ 在第 $n$ 輪被判定：

$$
R_a\to\text{insufficient under }A.
$$

到第 $m>n$ 輪，新的 assumption set $A'$ 出現：

$$
A'\neq A.
$$

若 $R_a$ 在 $A'$ 下重新進場，這不一定是「AI 忘了以前失敗」。

## 13.2 定義 re-entry

令：

$$
\operatorname{Exit}(R_a,n,A)=1
$$

表示在 regime $A$ 下被排除。

若之後：

$$
\operatorname{Enter}(R_a,m,A')=1,
$$

且存在可審計 novelty：

$$
A'\not\sim A,
$$

則稱為 legitimate re-entry。

## 13.3 Re-entry depth

若同一路由族多次：

$$
\text{enter}
\to
\text{fail}
\to
\text{reformulate}
\to
\text{re-enter},
$$

可定義：

$$
D_{re}(R_a)
=
\#\{\text{audited legitimate re-entries of }R_a\}.
$$

高 $D_{re}$ 是高階研究的重要訊號，因為研究已經不只比較 route，而在研究 route 對 context 的依賴。

---

# 14. Feedback depth：研究結果開始改變研究制度

## 14.1 普通研究輸出

一般：

$$
\text{search}
\to
\text{result}.
$$

## 14.2 反身研究輸出

高階 proof-space observatory 會出現：

$$
\text{search}
\to
\text{relation discovery}
\to
\text{policy update}
\to
\text{new search}.
$$

令 search policy 為：

$$
\Pi_N.
$$

如果第 $N$ 輪的 relation object $R_N$ 使：

$$
\Pi_{N+1}
=
\Psi(\Pi_N,R_N),
$$

則形成第一層 feedback。

## 14.3 二次 feedback

若系統又研究：

$$
\Psi
$$

本身造成的 bias、blind spot 或 route-collapse，並再更新：

$$
\Psi_{N+1}
=
\Theta(\Psi_N,F_N),
$$

則 feedback depth 再增加。

## 14.4 定義 feedback depth

操作上：

$$
D_{fb}
=
\max\{d:\text{存在 }d\text{ 層可追溯的 relation-to-policy feedback chain}\}.
$$

這個量與「meta-level 越高越真」無關。

它只描述研究制度的反身深度。

---

# 15. Route-family entropy：高階採樣不能只看階數

## 15.1 一萬輪全在同一路線上沒有多樣性

假設 $N$ 個 artifacts 全部落入同一 route family：

$$
R_1.
$$

即使有大量細節變化，其 family diversity 仍低。

## 15.2 定義 route-family entropy

若第 $k$ 階有 route/relation families：

$$
\mathcal F_k
=
\{F_1,\ldots,F_m\},
$$

其樣本比例：

$$
p_i
=
\frac{n_i}{\sum_j n_j}.
$$

定義：

$$
H_k^{route}
=
-\sum_{i=1}^{m}p_i\log p_i.
$$

normalized entropy：

$$
\widehat H_k^{route}
=
\frac{H_k^{route}}{\log m}.
$$

## 15.3 高階與高 entropy 是不同軸

可能：

$$
\operatorname{ord}\uparrow,
\qquad
H^{route}\downarrow.
$$

表示系統在很深地研究同一小群路線。

也可能：

$$
\operatorname{ord}\approx1,
\qquad
H^{route}\uparrow,
$$

表示仍在廣泛探索很多新 route。

因此需要至少二維描述：

$$
(\operatorname{order},\operatorname{diversity}).
$$

---

# 16. Audited yield：高階研究是否真的產生可靠資訊

## 16.1 不能只因為 higher-order 很酷就加分

高階 meta-analysis 很容易變成：

- 漂亮但不可驗證的分類；
- LLM 自己替自己的路線找共同點；
- 以修辭代替 theorem relation；
- 把共同用詞誤判成共同 obstruction。

所以必須定義 audited yield。

## 16.2 Order-conditioned audited yield

令：

$$
A_k(N)
$$

為第 $N$ 輪附近生成的 $k$ 階候選數。

令：

$$
V_k(N)
$$

為其中被獨立 verifier、形式檢查、雙路徑審計或可重現證據支持的新等價類數。

定義：

$$
\rho_k(N)
=
\frac{V_k(N)}{\max(1,A_k(N))}.
$$

## 16.3 高階幻覺的警報

若：

$$
A_k\uparrow
$$

但：

$$
\rho_k\to0,
$$

則表示系統可能正在生成大量 meta-language，而不是可靠 higher-order knowledge。

這是 observatory 必須特別防守的模式。

---

# 17. $K$ 階局部飽和

## 17.1 為什麼只說「飽和」太粗

一個 proof basin $B$ 中可能：

$$
\nu_0^B\approx0,
$$

但：

$$
\nu_2^B>0.
$$

這表示 base objects 已經很少新增，但 route relations 仍在快速生長。

## 17.2 定義候選

令：

$$
B\subseteq\Omega_R(Q)
$$

為由 representation、method family、assumption regime 或 obstruction family 定義的局部 basin。

若對：

$$
0\leq k\leq K,
$$

在長窗口 $W$ 中同時滿足：

$$
\nu_k^B(N)<\epsilon_k,
$$

$$
\rho_k^B(N)<\eta_k,
$$

$$
\Delta I_k^B(N)<\delta_k,
$$

且 route-family entropy 沒有出現新的顯著上升，則可標：

$$
\operatorname{Sat}_K(B;N,W)=1.
$$

## 17.3 這仍然只是 operational saturation

即使：

$$
\operatorname{Sat}_K(B)=1,
$$

也不推出：

$$
B
\text{ 在真實數學空間中已完全被枚舉}.
$$

更不推出：

$$
Q
\text{ 不可證或問錯了}.
$$

本文把這一點稱為：

$$
\boxed{
\text{Order-Saturation Non-Conclusion Rule}.
}
$$

它是 LSI-PSD-01 非結論原則的高階版本。

---

# 18. 高階採樣與局部 proof basin

## 18.1 Basin 不是地理比喻，而是搜尋約束集合

可以由下列條件定義 basin：

$$
B
=
B(\mathcal L,\mathcal M,\mathcal A,\mathcal O),
$$

其中：

- $\mathcal L$：representation language；
- $\mathcal M$：method family；
- $\mathcal A$：assumption regime；
- $\mathcal O$：target obstruction family。

## 18.2 同一問題可以同時存在不同 sampling order

例如：

$$
B_1:
\nu_0\approx0,
\nu_1\approx0,
\nu_2>0,
$$

而：

$$
B_2:
\nu_0>0.
$$

所以：

$$
\boxed{
\text{Sampling order is local to a basin, not a global scalar of the problem.}
}
$$

## 18.3 這解釋 NS corpus 的一個表面矛盾

在初步 observatory 中，某些 NS 支線已出現 confluence、feedback、all-order escalation；同時固定窗口 novelty 並沒有顯示整個 corpus 全域 collapse。

兩者並不矛盾。

可能只是：

$$
B_{X72}
$$

已進入較高階重訪，而：

$$
B_{other}
$$

仍然在產生低階新 route。

---

# 19. NS-203 corpus：如何重新解讀第一版 tier

## 19.1 資料地位

既有 NS Proof-Space Sampling Observatory 對保守篩選後的 corpus 得到：

$$
N_{NS}=203
$$

個 paper-like artifacts。

第一版 heuristic tier 為：

$$
T_1=84,
$$

$$
T_2=107,
$$

$$
T_3=10,
$$

$$
T_X=2.
$$

本文把這些數字視為：

$$
\boxed{
\text{instrument-development observations, not theorem-level facts.}
}
$$

## 19.2 為什麼 $T_2$ 很大並不奇怪

長程 corpus 中大量工作會呈現：

- revisit；
- reuse；
- obstruction recurrence；
- route transfer；
- second pass audit。

只要分類器偏向「看到 recurrence 就算二階」，就可能高估 $T_2$。

所以 v2 observatory 必須把 $T_2$ 再拆：

$$
T_{2a}=\text{same-state revisit},
$$

$$
T_{2b}=\text{same-route revisit},
$$

$$
T_{2c}=\text{route comparison},
$$

$$
T_{2d}=\text{cross-route obstruction recurrence}.
$$

其中真正強的二階證據主要是後兩者。

## 19.3 X72 的 confluence chain

初步 corpus 中，X72 後期直接使用 obstruction confluence、coupled confluence、confluence feedback 等研究語言。

這些詞本身仍不是證明。

但若對應實際 dependency graph 顯示：

$$
\{R_a,R_b,R_c\}
\to
O,
$$

之後又研究：

$$
\operatorname{Rel}(R_a,R_b,R_c),
$$

再讓 relation 結果改變下一輪 route policy，則這是乾淨的 $T_3$ evidence。

## 19.4 All-order 不等於無限階 proof-space

某篇文章若研究：

$$
\text{all-order escalation of a mathematical estimate family},
$$

不能直接說：

$$
\operatorname{ord}=\infty.
$$

只有當它對「method-family escalation 本身」建立可審計的 relation-level no-go，才可作 $T_X$ 候選。

這是本文對第一版 observatory 最重要的修正之一。

---

# 20. 一個合成例子：從零階到三階

## 20.1 零階

假設研究問題為：

$$
Q:
\text{證明某能量 }E(t)\text{ 在指定條件下有界}.
$$

得到新估計：

$$
E(t)
\leq
E(0)+C\int_0^t F(s)\,ds.
$$

這是零階新物件。

## 20.2 一階

研究者發現可透過兩條方法：

$$
R_A:
E\to\text{localization}\to\text{bootstrap},
$$

$$
R_B:
E\to\text{frequency split}\to\text{bootstrap}.
$$

這是 route-level，一階物件。

## 20.3 二階

兩條路都失敗於：

$$
O:
\text{critical remainder cannot be absorbed}.
$$

並證明這不是字面巧合，而是在 quotient 後共享同一 scaling defect。

此時：

$$
R_A\to O,
$$

$$
R_B\to O
$$

形成二階 confluence。

## 20.4 三階

又發現第三、第四種完全不同方法也匯入 $O$，於是研究者提出：

$$
C_O
=
\operatorname{ConfluenceFamily}(O).
$$

接著把 $C_O$ 用來禁止下一輪再走所有保留同 scaling defect 的 routes。

搜尋 policy 更新：

$$
\Pi_{N+1}
=
\Pi_N
\setminus
\{R:\operatorname{Defect}(R)=\operatorname{Defect}(O)\}.
$$

這就是三階 relation-to-policy feedback。

---

# 21. 高階 no-go：失敗也可以有階數

## 21.1 零階 no-go

$$
L
\text{ 為假或不足}.
$$

只排除單一候選。

## 21.2 一階 no-go

$$
R
\text{ 在條件 }A\text{ 下不能閉合}.
$$

排除一條 route。

## 21.3 二階 no-go

若證明一整類 routes：

$$
\mathcal R_D
=
\{R:\operatorname{Defect}(R)=D\}
$$

都共享同一 fatal obstruction，則：

$$
\forall R\in\mathcal R_D,
\qquad
R\to O_D.
$$

這是 method-family no-go。

## 21.4 更高階 no-go

若即使對：

$$
\mathcal R_D
$$

進行固定類型的 correction family：

$$
C^{(1)},C^{(2)},\ldots,C^{(m)},
$$

都只能把 obstruction 推到同一 quotient class，則可能形成更高階 escalation no-go。

但此類聲稱必須有形式證據，不能只靠「試很多次都不行」。

---

# 22. 高階採樣與方法族的「家譜」

## 22.1 Route 不應只存 flat label

假設：

$$
R_{A.1},R_{A.2},R_{A.3}
$$

都是從 parent method $R_A$ 變形而來。

如果把它們當三條完全獨立 route，會高估 confluence independence。

## 22.2 Method genealogy

定義 genealogy graph：

$$
\mathcal G_{gen}
=
(V_R,E_{parent}).
$$

若：

$$
R_{A.2}
=
\operatorname{Modify}(R_A,\theta_2),
$$

則有：

$$
R_A\to R_{A.2}.
$$

## 22.3 Independent confluence 應折扣共同祖先

可定義 route independence：

$$
w_{ind}(R_i,R_j)
=
1-rac{
\operatorname{SharedAncestorMass}(R_i,R_j)
}{
\operatorname{TotalAncestorMass}(R_i,R_j)
}.
$$

因此三條 sibling routes 同時撞牆，不應等價於三條跨方法族 routes 同時撞牆。

這對 NS 這種長支線研究尤其重要。

---

# 23. 研究路由的同構與 representation sensitivity

## 23.1 數學等價不代表搜尋等價

LSI-PSD-03 已建立：

$$
\text{Mathematical redundancy}
\not\Rightarrow
\text{search-dynamical redundancy}.
$$

高階採樣必須繼承這一點。

如果兩條 routes 在命題層等價：

$$
R_a\sim_{math}R_b,
$$

但 AI prover 對它們成功率差異很大：

$$
P_{succ}(R_a)\neq P_{succ}(R_b),
$$

則在 search-space higher-order analysis 中不能完全合併。

## 23.2 雙身份資料結構

每條 route 建議同時保存：

$$
ID_{math}(R),
$$

$$
ID_{search}(R).
$$

前者用於 theorem-level quotient。

後者保留：

- syntax；
- library context；
- state encoding；
- tactic history；
- prompt lineage；
- prover version；
- model version；
- budget。

## 23.3 高階 relation 也要雙層

因此：

$$
\Omega^{(2)}_{math}
$$

與：

$$
\Omega^{(2)}_{search}
$$

也不應被混成一個空間。

同一 confluence 在數學上可能是一個 obstruction，在 search dynamics 中則可能由完全不同的 failure mechanisms 造成。

---

# 24. Graph-of-graphs：高階 observatory 的自然資料模型

## 24.1 Layer 0：semantic object graph

$$
G_0
=
(V_0,E_0).
$$

節點：

- claims；
- assumptions；
- lemmas；
- obstructions；
- statuses。

## 24.2 Layer 1：route graph

$$
G_1
=
(V_1,E_1).
$$

節點可以是 route segments，邊表示：

- extension；
- refinement；
- parent-child；
- reuse；
- re-entry。

## 24.3 Layer 2：relation graph

$$
G_2
=
(V_2,E_2).
$$

節點本身是：

$$
\text{relations over }G_1.
$$

例如：

- confluence object；
- dominance object；
- incompatibility object；
- no-go family；
- compensation pair。

## 24.4 Layer 3：policy-feedback graph

$$
G_3
$$

記錄：

$$
G_2
\to
\Pi
\to
G_1'
$$

也就是 relation-level knowledge 如何改變後續 route generation。

## 24.5 為什麼單一 property graph 仍然可以實作

工程上不一定真的需要四個資料庫。

可以用 typed hypergraph：

$$
\mathcal H
=
(V,E,\tau_V,\tau_E),
$$

其中：

$$
\tau_V(v)
\in
\{state,route,relation,policy,obstruction,claim\}.
$$

這樣較容易在 Neo4j、PostgreSQL graph extension 或自製 JSONL pipeline 中落地。

---

# 25. 建議的 canonical record schema

每個高階 observation 至少需要：

```yaml
observation_id: LSI-HO-000001
problem_id: NS-3D-global-regularity
artifact_id: ...
order_tier: T3
order_confidence: 0.82
object_type: confluence
inputs:
  - route_id: R-X72-18-A
  - route_id: R-X72-18-B
output:
  obstruction_id: O-CANON-0042
relation_type: converges_to_same_obstruction
evidence:
  - dependency_trace
  - matched_assumption_signature
  - normalized_obstruction_signature
verifier_status: partially_audited
provenance:
  source_file: ...
  source_span: ...
  extractor_version: ...
  reviewer: ...
```

這個 schema 的重點不是 YAML。

重點是：

$$
\boxed{
\text{order claim itself must carry evidence and provenance.}
}
$$

---

# 26. 高階關係的可信度

## 26.1 Relation confidence

對 relation $r$：

$$
\operatorname{Conf}(r)
=
f(E_{formal},E_{struct},E_{semantic},E_{indep}).
$$

其中：

- $E_{formal}$：形式互推／kernel evidence；
- $E_{struct}$：dependency / graph structure；
- $E_{semantic}$：語義審計；
- $E_{indep}$：獨立 evaluator agreement。

## 26.2 三值而非強迫二值

延續 LSI-PSD-03：

$$
R_{ij}
\in
\{
\text{supported},
\text{rejected},
\text{undetermined}
\}.
$$

對高階 relation 尤其重要。

因為：

$$
\text{undetermined}
$$

比錯誤地合併兩條深層 route 更安全。

---

# 27. 防止「AI 自己替自己證明高階」

## 27.1 Self-confirming relation problem

若同一模型：

1. 生成兩篇 proof attempts；
2. 再判斷兩篇其實匯流；
3. 再宣稱匯流是一個深層 obstruction；

則存在循環：

$$
M
\to
G
\to
M(G)
\to
\text{claim about }G.
$$

這不能被當成獨立證據。

## 27.2 最低限度的解耦

建議至少分離：

$$
M_{gen},
$$

$$
M_{rel},
$$

$$
V_{formal},
$$

$$
A_{human/independent}.
$$

其中：

- $M_{gen}$ 生成研究；
- $M_{rel}$ 抽取高階關係；
- $V_{formal}$ 驗證可形式化部分；
- 獨立 audit 處理不可形式化語義。

## 27.3 模型不同不等於證據獨立

兩個 LLM 即使品牌不同，也可能共享：

- 訓練資料；
- proof conventions；
- benchmark bias；
- common mathematical priors。

因此 independent weight 仍應折扣。

---

# 28. 與 AND-OR graph 的差異

## 28.1 AND-OR graph 解的是「如何完成這個 proof」

形式 proof search 中，AND node / OR node 常用於表示：

- 所有子目標都要完成；
- 多個候選 tactic 只需一條成功。

其主要目標仍是：

$$
\exists\text{ successful proof path}.
$$

## 28.2 高階 proof-space observatory 問的是另一件事

本文更關心：

$$
\text{哪些 path families 被反覆嘗試？}
$$

$$
\text{哪些 path families 共享 obstruction？}
$$

$$
\text{哪些 failure relations 改變了後續搜尋？}
$$

因此它不是替代 theorem prover，而是 theorem-research layer。

---

# 29. 與 reinforcement learning state hierarchy 的差異

## 29.1 可以借用 MDP 語言，但不能偷換

若：

$$
\mathcal MDP
=(S,A,P,R,\gamma),
$$

proof state 與 tactic 很容易映射到：

$$
S,A.
$$

但本文的：

$$
\Omega^{(2)},\Omega^{(3)}
$$

不只是 belief state 或 option hierarchy。

它們是**研究關係本身的知識物件**。

## 29.2 高階關係可以跨 episode 存活

一個 obstruction confluence：

$$
O_c
$$

可以跨越上百次獨立 proof episodes 保留。

所以它屬於：

$$
\text{persistent research memory},
$$

不是單 episode transition。

---

# 30. 高階採樣的三種「真正新增」

## 30.1 Relational novelty

發現兩條原本被視為無關的 routes 其實共享同一 structural core。

$$
R_a\sim_{new}R_b.
$$

## 30.2 Constraint novelty

發現一個 relation 能排除一整族 future routes。

$$
\mathcal R_{future}
\cap
\mathcal R_{forbidden}
=
\varnothing.
$$

## 30.3 Routing novelty

發現一個 higher-order signal 可以重排 search priority：

$$
\Pi_{N+1}
\neq
\Pi_N.
$$

這三種都可能在沒有新增 theorem statement 的情況下產生真實研究價值。

---

# 31. 什麼叫「X 階採樣」才不會變成誇張口號

## 31.1 最弱定義

如果 observatory 最多可靠區分到 $K$ 階，而某 artifact 有強證據顯示其核心 novelty 位於更高 relation level，則標：

$$
T_X.
$$

## 31.2 不允許的說法

不能因為：

- 文章很長；
- 提到 all-order；
- 提到 infinite hierarchy；
- 有很多 nested lemmas；
- AI 自稱 meta-meta reasoning；

就標成 $T_X$。

## 31.3 建議證據門檻

至少需要：

1. 其 input objects 已被審計為 relation-level objects；
2. 新結果是這些 relation objects 之間的新結構；
3. 該結構影響 route classification、no-go inheritance 或 search policy；
4. provenance 可追溯；
5. 至少一部分 relation 可被獨立重現。

---

# 32. 高階採樣與「研究越來越快」的可能性

## 32.1 為什麼 higher-order memory 可能加速研究

如果每次都從零開始：

$$
C_N
\sim
N\cdot C_{search}.
$$

但若已知：

$$
\mathcal R_{bad},
$$

下一輪可以直接剪枝：

$$
\Pi_{N+1}
\leftarrow
\Pi_N\setminus\mathcal R_{bad}.
$$

因此有效搜尋空間：

$$
|\Omega_{eff}(N+1)|
<
|\Omega_{eff}(N)|.
$$

## 32.2 這就是 proof-space compression 的工程版本

高階關係把大量歷史壓成少數可重用 constraint：

$$
\{R_1,\ldots,R_{1000}\}
\to
\{O_1,O_2,O_3\}.
$$

如果 $O_i$ 是可靠的，未來不需要重跑全部歷史。

這和 memoization 類似，但壓縮單位是 semantic relation，而不只是 exact state。

## 32.3 但錯誤高階壓縮會造成災難

若把其實可行的 route 誤歸入 no-go family：

$$
R^*\in\widehat{\mathcal R}_{bad},
$$

則系統可能永久剪掉真正的證明路徑。

因此 higher-order memory 越強，rollback 與 uncertainty tracking 越重要。

---

# 33. 反例：高階採樣不一定帶來收斂

## 33.1 Meta-explosion

系統可能不斷生成：

$$
\text{relations about relations about relations}
$$

而沒有任何 constraint power。

這形成：

$$
H_{meta}\uparrow,
\qquad
I_{useful}\approx0.
$$

## 33.2 Taxonomy trap

分類越來越細：

$$
T_1
\to
T_{1a},T_{1b},T_{1c},\ldots
$$

也不代表更接近真理。

分類只是工具。

## 33.3 Observer overfitting

observatory 可能根據目前 203 篇 NS corpus 建出非常細的 route ontology，卻只適用於這批文件。

一旦加入另一個 PDE corpus：

$$
\operatorname{Transfer}(Ontology_{NS})
\approx0.
$$

就表示它是 corpus-specific overfit。

---

# 34. 跨問題 transfer：高階知識最值得測的地方

## 34.1 一個 obstruction family 如果能跨問題重現，價值更高

假設 NS 中的 route relation：

$$
R_{NS}^{(2)}
$$

可以映射到 SQG、Boussinesq 或其他 evolution PDE：

$$
\Phi:
R_{NS}^{(2)}
\to
R_{PDE}^{(2)}.
$$

如果映射保留：

- assumption signature；
- scaling role；
- obstruction role；
- closure status；

那它可能是更一般的 proof asset。

## 34.2 Transfer score

定義：

$$
T_{score}(r)
=
\frac{
\#\text{domains where relation }r\text{ is independently useful}
}{
\#\text{domains tested}
}.
$$

高：

$$
T_{score}
$$

能幫助區分：

- corpus-specific recurrence；
- genuine methodological structure。

---

# 35. 與「真理—生成性反轉」的橋接

後續 LSI-PSD-07 將研究 truth、fidelity 與 generativity。

高階採樣在那裡扮演關鍵角色：

如果某個 parent framing 產生：

$$
\text{大量 zero-order descendants},
$$

接著又形成：

$$
\text{route families},
$$

再形成：

$$
\text{confluence families},
$$

那麼即使 parent problem 最後被重新定義，其研究史仍可能保留大量高階可遷移結構。

所以：

$$
\boxed{
\text{Generativity should be measured across sampling orders, not only by descendant count.}
}
$$

---

# 36. 與「生產性錯置」的橋接

假設兩個 definitions：

$$
D,
\qquad
D'.
$$

$D'$ 可能不是更正確，但它打開更多 route variation：

$$
|\Omega_{D'}^{(1)}|
>
|\Omega_D^{(1)}|.
$$

更重要的是，也可能產生更多高階 relation：

$$
|\Omega_{D'}^{(2)}|
>
|\Omega_D^{(2)}|.
$$

這表示「生成性」不只是一階產量，而可能是：

$$
G(D)
=
\sum_{k=0}^{K}
\lambda_k
G_k(D).
$$

後續論文將檢驗這個方向。

---

# 37. 研究制度的階層化停止條件

## 37.1 一階停止條件

若：

$$
\nu_0\downarrow,
$$

系統不應立刻停止。

應檢查：

$$
\nu_1,\nu_2.
$$

## 37.2 關係層停止條件

若：

$$
\nu_0\approx0,
$$

$$
\nu_1\approx0,
$$

但：

$$
\nu_2>0,
$$

則應從「找新 route」切換為：

$$
\text{audit relation structure}.
$$

## 37.3 $K$ 階停止條件

若在 basin $B$：

$$
\forall k\leq K,
\qquad
\nu_k^B<\epsilon_k,
$$

並且：

$$
\rho_k^B<\eta_k,
$$

則 system action 不應是：

> 宣布問題錯了。

而應是：

$$
\boxed{
\text{Current basin / regime saturated; escalate representation audit.}
}
$$

---

# 38. 高階研究的 escalation ladder

當 basin 飽和，可依序嘗試：

## 38.1 Representation escalation

$$
\mathcal L
\to
\mathcal L'.
$$

## 38.2 Method escalation

$$
\mathcal M
\to
\mathcal M\cup\Delta\mathcal M.
$$

## 38.3 Assumption audit

$$
\mathcal A
\to
\operatorname{Audit}(\mathcal A).
$$

## 38.4 Problem reformulation

$$
Q
\to
Q'.
$$

## 38.5 Intelligence / compute escalation

$$
B
\to
B'.
$$

每次 escalation 都應開新 regime ID，避免把不同制度的 sampling history 混在一起。

---

# 39. High-order proof-space record 的最小可重建性

一個高階 conclusion 若要被未來 AI 使用，不能只保存一句：

> 這條路之前試過了，不行。

至少要保存：

$$
\mathcal H
=
(A,R,O,E,V,C),
$$

其中：

- $A$：assumptions；
- $R$：route signature；
- $O$：obstruction signature；
- $E$：evidence；
- $V$：verifier state；
- $C$：context / regime。

只有這樣未來才能判斷：

$$
\text{old no-go}
$$

是否真的適用於新情況。

---

# 40. 高階 observatory 的 v0.2 計算流程

建議 pipeline：

```text
Artifacts
  -> claim / lemma / assumption extraction
  -> semantic quotient
  -> route reconstruction
  -> route genealogy
  -> canonical obstruction mapping
  -> relation extraction
  -> confluence / dominance / incompatibility audit
  -> feedback / re-entry detection
  -> order-tier classification
  -> order-conditioned novelty and coverage
  -> local saturation report
```

其中任何一步的低信心都要向後傳遞 uncertainty。

---

# 41. 建議的核心指標總表

## 41.1 Base metrics

$$
N_0
=
\#\text{zero-order audited classes}.
$$

$$
N_1
=
\#\text{route classes}.
$$

$$
N_2
=
\#\text{route-relation classes}.
$$

## 41.2 Novelty vector

$$
\boldsymbol\nu(N)
=
(\nu_0,\nu_1,\ldots,\nu_K).
$$

## 41.3 Coverage vector

$$
\mathbf I(N)
=
(I_0,I_1,\ldots,I_K).
$$

## 41.4 Audited yield vector

$$
\boldsymbol\rho(N)
=
(\rho_0,\rho_1,\ldots,\rho_K).
$$

## 41.5 Confluence

$$
C_w(O).
$$

## 41.6 Re-entry depth

$$
D_{re}(R).
$$

## 41.7 Feedback depth

$$
D_{fb}.
$$

## 41.8 Route entropy

$$
\widehat H_k^{route}.
$$

## 41.9 Transfer score

$$
T_{score}(r).
$$

這些量共同描述研究，而不是讓單一「progress percentage」承擔全部意義。

---

# 42. 四個可檢驗預測

## 預測一：長程 corpus 會出現 sampling-order migration

若同一問題持續研究，應可觀察：

$$
\text{novelty mass}
$$

從：

$$
k=0,1
$$

逐漸部分轉移到：

$$
k=2,3.
$$

不是所有問題都必然發生，但在高密度長程研究中應可測。

## 預測二：高 confluence basin 的零階 novelty 會先下降

若某 basin 有高：

$$
C_w(O),
$$

其後續研究可能更容易形成 route relation 分析，而不是持續產生大量完全獨立 base objects。

## 預測三：有 persistent higher-order memory 的 agent 會少做無效重訪

比較：

$$
Agent_{flat}
$$

與：

$$
Agent_{HO}.
$$

應看到：

$$
\operatorname{InvalidRevisitRate}(Agent_{HO})
<
\operatorname{InvalidRevisitRate}(Agent_{flat}).
$$

## 預測四：過度激進的 higher-order compression 會提高 false-prune risk

若 quotient / no-go inheritance 太激進：

$$
\operatorname{FalsePruneRate}\uparrow.
$$

所以有效系統應存在 accuracy--compression tradeoff。

---

# 43. 與目前 AI theorem proving 發展的關係

現代 formal theorem proving 已清楚朝下列方向前進：

- proof states 不只輸入模型，而是可搜尋節點；
- proof trajectory 可以被評估；
- failure signal 可以回饋 search；
- lemma dependency 可以先被規劃成 blueprint；
- multi-agent 可以分工關閉不同 lemma nodes；
- state graph 可以作大規模資料生成來源；
- proof plan 可以被保存為 DAG。

本文認為下一個自然問題是：

> 當同一研究問題跨越數千次 episodes 後，這些 episode 之間的關係本身是否應被當成第一級研究資料？

本文的答案是肯定的。

這不是因為高階語言比較漂亮，而是因為缺少它時，系統無法區分：

$$
\text{new theorem},
$$

$$
\text{new route},
$$

$$
\text{old route revisit},
$$

$$
\text{new relation among old routes}.
$$

---

# 44. 本文與前三篇的依賴關係

## 44.1 對 LSI-PSD-01 的依賴

第 1 篇建立：

$$
\text{search regime}
\neq
\text{mathematical reality}.
$$

本文所有 sampling order 都只屬於可觀測 regime。

## 44.2 對 LSI-PSD-02 的依賴

第 2 篇建立：

$$
I_N,
\qquad
\Delta I_N,
$$

與多層 coverage。

本文將其展開為：

$$
I_k(N).
$$

## 44.3 對 LSI-PSD-03 的依賴

第 3 篇建立 semantic quotient。

沒有 quotient，就無法可靠判斷：

$$
\text{revisit},
$$

$$
\text{confluence},
$$

$$
\text{route family}.
$$

因此：

$$
\boxed{
\text{Higher-order sampling requires quotient-aware identity.}
}
$$

---

# 45. 本文的非主張

本文不主張：

1. 階數越高越接近真理；
2. 階數越高代表 AI 越智能；
3. meta-analysis 可以取代 theorem proof；
4. 出現 `second-order` 字樣就等於二階 proof-space sampling；
5. 大量 recurrence 就證明問題 framing 錯誤；
6. route confluence 就證明存在唯一 obstruction；
7. $K$ 階局部飽和就證明底層 proof space 被耗盡；
8. NS-203 已經達到全域 saturation；
9. P/NP 或 Navier--Stokes 因長期未證而應被重新定義；
10. LLM 對 route relation 的判斷可以不經 audit 當作數學等價；
11. 更細的 taxonomy 本身就是研究進展；
12. $T_X$ 表示無限階；
13. 所有研究問題都會經歷相同 sampling-order migration；
14. formal theorem proving 的 state graph 與 informal research proof-space 完全同構；
15. 本文已給出一個完備的 higher-order proof ontology。

---

# 46. 限制

## 46.1 Order assignment 仍具有模型依賴

即使 schema 明確，legacy text 仍可能缺少足夠 provenance 來重建 route relations。

因此：

$$
\operatorname{ord}_{obs}
$$

是一個帶不確定性的估計。

## 46.2 Relation extraction 比 theorem extraction 更難

單一 theorem statement 可以被 parser 抽取。

但：

> 兩條不同方法共享同一真正 obstruction

往往需要：

- 深層語義判斷；
- assumptions 對齊；
- proof dependency audit；
- 可能的形式化重建。

這會是目前 observatory 的主要瓶頸。

## 46.3 高階 measure 未必存在天然概率結構

$\mu_k$ 的定義可能高度依賴 task。

因此本文不宣稱：

$$
I_k
$$

具有唯一自然的 measure-theoretic 定義。

它首先是一族可操作 coverage functional。

## 46.4 NS corpus 仍是單一問題族

要驗證框架是否普遍，需要加入：

- Collatz；
- BSD；
- combinatorics；
- formal olympiad proof；
- program verification；
- 其他 PDE。

只有跨域 transfer 後，才能判斷哪些 higher-order relations 是一般性的。

---

# 47. 結論：研究本身會成為下一階研究對象

長程 AI 數學研究最重要的變化，不只是生成速度提高。

真正的結構變化是：

$$
\text{research outputs}
$$

逐漸變成下一輪研究的 objects。

第一階段研究：

$$
\text{What mathematical objects exist?}
$$

第二階段研究：

$$
\text{How do proof states transform?}
$$

再下一階段：

$$
\text{How are proof routes related?}
$$

更後面：

$$
\text{How do those relations themselves recur, converge, inherit failure, and modify search?}
$$

因此本文把長程研究寫成：

$$
\Omega^{(0)}
\to
\Omega^{(1)}
\to
\Omega^{(2)}
\to
\cdots
\to
\Omega^{(K)}.
$$

但這不是一條「往真理上升」的階梯。

它是一條**研究對象階層化**的路徑。

真正需要觀察的是：

$$
\nu_k,
\qquad
I_k,
\qquad
\rho_k,
\qquad
C_w,
\qquad
D_{re},
\qquad
D_{fb},
\qquad
H_k^{route}.
$$

當：

$$
\nu_0\to0
$$

時，研究未必停止。

它可能只是開始問：

> 為什麼我們總是走回同一個地方？

而當這個問題也被反覆研究時，proof space 便不再只是「候選證明的集合」，而開始呈現一個可被觀測、壓縮、比較與重新路由的動態結構。

本文因此提出系列中的第四個核心命題：

$$
\boxed{
\textbf{Long-horizon proof search can migrate from sampling mathematical states to sampling relations among proof routes.}
}
$$

以及它的保守版本：

$$
\boxed{
\textbf{Higher-order recurrence is evidence about the structure of a research regime, not a verdict on the underlying mathematical proposition.}
}
$$

這為下一篇「局部飽和與全域開放」建立基礎：如果 sampling order 可以因 basin 而不同，那麼所謂「證明空間飽和」就必須從一開始被理解為局部、階層依賴且制度相對的現象。

---

# 參考文獻

1. Yin, D., & Gao, J. (2025). **Generating Millions Of Lean Theorems With Proofs By Exploring State Transition Graphs.** arXiv:2503.04772. https://arxiv.org/abs/2503.04772

2. Huang, S., Song, P., George, R. J., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925. https://arxiv.org/abs/2502.17925

3. Hubert, T. et al. (2025). **Olympiad-level formal mathematical reasoning with reinforcement learning.** Nature. https://www.nature.com/articles/s41586-025-09833-y

4. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468. https://arxiv.org/abs/2606.06468

5. Kung, P. N. et al. (2026). **LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks.** arXiv:2606.03303. https://arxiv.org/abs/2606.03303

6. Wang, Z., Yang, B., Zhou, S., Li, C., Zhang, Y., Dong, B., & Wen, Z. (2025). **Translating Informal Proofs into Formal Proofs Using a Chain of States.** arXiv:2512.10317. https://arxiv.org/abs/2512.10317

7. Kurgan, S. et al. (2026). **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363. https://arxiv.org/abs/2606.25363

8. **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** (2026). arXiv:2606.05400. https://arxiv.org/abs/2606.05400

9. **VERITAS: Verifier-Guided Proof Search for Zero-Shot Formal Theorem Proving.** (2026). arXiv:2606.19399. https://arxiv.org/abs/2606.19399

10. **TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs.** (2026). arXiv:2607.11258. https://arxiv.org/abs/2607.11258

11. Dong, K., & Ma, T. (2025). **STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving.** Proceedings of the 42nd International Conference on Machine Learning, PMLR 267. https://proceedings.mlr.press/v267/dong25h.html

12. Song, P., Yang, K., & Anandkumar, A. (2025). **Lean Copilot: Large Language Models as Copilots for Theorem Proving in Lean.** Proceedings of the International Conference on Neuro-symbolic Systems, PMLR 288. https://proceedings.mlr.press/v288/song25a.html

13. **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics.** (2026). arXiv:2606.09450. https://arxiv.org/abs/2606.09450

14. Lyu, H. et al. (2026). **Rtl2lean: Automated RTL-to-Lean Translation with Hierarchical Theorem Generation and Lemma Reuse.** arXiv:2607.16855. https://arxiv.org/abs/2607.16855

---

## 附錄 A：符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 研究問題 |
| $R$ | 搜尋制度 / research regime |
| $\Omega_R^{(0)}(Q)$ | 基礎 research-state objects |
| $\Omega_R^{(1)}(Q)$ | proof moves / route objects |
| $\Omega_R^{(2)}(Q)$ | route relations |
| $\Omega_R^{(k)}(Q)$ | 第 $k$ 階 proof-space objects |
| $\mathcal F_k$ | 第 $k$ 階到第 $k+1$ 階的 typed constructor family |
| $T_1,T_2,T_3,T_X$ | legacy corpus 的四層操作 tier |
| $\nu_k(N)$ | 第 $k$ 階 novelty |
| $I_k(N)$ | 第 $k$ 階 coverage functional |
| $\rho_k(N)$ | 第 $k$ 階 audited yield |
| $C_w(O)$ | obstruction 的 weighted confluence |
| $D_{re}(R)$ | route 的 re-entry depth |
| $D_{fb}$ | feedback depth |
| $H_k^{route}$ | 第 $k$ 階 route-family entropy |
| $T_{score}$ | relation 的跨域 transfer score |
| $\operatorname{Sat}_K(B)$ | basin $B$ 的 $K$ 階操作性局部飽和標記 |

---

## 附錄 B：最小實驗設計

若要把本文從方法論變成可檢驗研究，可進行以下實驗：

### B.1 Corpus

使用至少三種長程研究 corpus：

$$
C_1=\text{NS-203},
$$

$$
C_2=\text{另一個未解數學問題 corpus},
$$

$$
C_3=\text{formal theorem proving traces}.
$$

### B.2 雙人／雙模型標註

隨機抽取 artifact pairs 與 route families，標註：

$$
\operatorname{ord},
$$

$$
\operatorname{route\_family},
$$

$$
\operatorname{obstruction\_id},
$$

$$
\operatorname{confluence}.
$$

計算 inter-rater agreement。

### B.3 自動抽取與人工 gold set 比較

測：

$$
Precision_k,
\qquad
Recall_k,
\qquad
F1_k.
$$

若 $T_3/T_X$ precision 很低，則不得用它們支持 higher-order saturation claim。

### B.4 時序測試

按真實時間排序 corpus，計算：

$$
\nu_k^{(W)}(N)
$$

與 random permutation baseline 比較。

### B.5 Transfer 測試

把從 NS 得到的 obstruction relation ontology 移植到另一 PDE corpus。

如果：

$$
T_{score}\approx0,
$$

則原 taxonomy 很可能只是 corpus-specific。

---

## 附錄 C：一句話版本

$$
\boxed{
\text{一開始研究答案；之後研究路徑；再之後，研究為什麼不同路徑總是彼此相遇。}
}
$$

這三個階段不代表越來越接近真理。

它們代表：

$$
\boxed{
\text{研究本身正在成為新的研究對象。}
}
$$


<!-- END LSI-PSD-04 -->

---


<!-- BEGIN LSI-PSD-05 -->

# LSI-PSD-05 — 局部飽和與全域開放：證明空間的多盆地結構

## Local Saturation and Global Openness: A Multi-Basin Structure of Proof Space

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 05  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Local Saturation and Basin-Dynamics Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文提出「證明空間多盆地結構」作為長程 AI 數學研究的操作性模型。本文中的 basin、boundary、escape、conductance、frontier 等詞首先是 proof-space observatory 的研究語言；除非另有嚴格數學構造，不應把它們直接等同於傳統動力系統中的吸引盆、拓撲邊界、勢能井或測地結構。本文不主張目前任何有限 AI corpus 已證明 Navier--Stokes、P/NP 或其他未解問題的完整證明空間局部／全域幾何，更不主張某個局部研究盆地的飽和能推出原命題錯誤、不可證、獨立、無法判定或定義失敗。

---

## 摘要

當長程 AI 數學研究持續數百、數千乃至更多輪後，「新資訊是否變少」不再是一個單純的全域問題。研究可能在某一組表示、方法、引理依賴與障礙結構中反覆深化，呈現高度 recurrence、route confluence、higher-order resampling 與 audited yield decline；同一時間，其他表示、其他方法族、其他 premise 組合或其他局部區域仍可能持續產生大量新資訊。若把這兩種現象混在一起，便容易犯下一個關鍵錯誤：

$$
\boxed{
\text{local saturation}
\not\Rightarrow
\text{global exhaustion}.
}
$$

本文在 LSI-PSD-01 至 04 的基礎上，建立「證明空間多盆地結構」的操作性框架。固定研究問題 $Q$ 與搜尋制度 $R$，在語義 quotient 後的可觀測證明空間上建立加權圖：

$$
\mathcal G_R(Q)
=
(V_R,E_R,w_R),
$$

其中節點可為 canonical proof states、route states、obstruction states 或高階 relation states，邊則表示已驗證或已稽核的可達、依賴、轉換、重訪、匯流或再進入關係。對任意候選區域 $B\subseteq V_R$，本文以內部 recurrence、邊界流量、局部 novelty、跨界 escape rate 與 order-conditioned audited yield 定義一個**操作性 basin**。一個 basin 可以被高度探索而近似局部飽和，卻仍然只是整體可觀測研究空間中的一個低傳導、高 recurrence 區域。

本文進一步定義：

$$
\phi(B),
$$

表示 basin conductance；

$$
\rho_k(B;N,W),
$$

表示第 $k$ 階、固定時間窗內的 audited novelty yield；

$$
S_K(B),
$$

表示 $K$ 階局部飽和標記；

$$
\Gamma_{\mathrm{esc}}(B,a),
$$

表示某個 escape action $a$ 離開 basin 後帶來的新增資訊增益；

以及：

$$
\mathfrak F_R(N),
$$

表示在既有 corpus 與制度下仍具有可達性但尚未充分展開的觀測 frontier。

本文的重要限制是：**frontier 的存在可以支持「目前觀測制度仍開放」，但 frontier 的不可見不能支持「數學全域已封閉」。** 因為真正的證明空間可能超出目前表示語言、方法族、retrieval 系統、verifier、模型能力與計算預算。因此本文區分：

$$
\text{observed local saturation},
$$

$$
\text{regime-bounded global saturation},
$$

與不可從有限研究直接主張的：

$$
\text{mathematical global exhaustion}.
$$

2025--2026 年 formal theorem proving 的發展提供了工程上的相鄰證據。LeanNavigator 將 formal proof exploration 表示成 state-transition graph；LeanProgress 顯示局部 tactic 正確性不等於全局 proof progress；BFS-Prover 透過 length normalization 鼓勵更深路徑探索；FETCH 直接辨識語義重複造成的 over-exploration 與評分波動造成的 under-exploration；FormalEvolve 把固定預算下的 candidate repertoire diversity 與 cross-problem coverage uniformity 視為核心目標；LeanSearch v2 指出單一 premise 的局部檢索與完整定理所需的 global premise set 是不同問題；Goedel-Architect 以全局 blueprint refinement 避免對 dead-end strategy 的遞歸打轉；TreeThink 則顯示同一 formal environment 可以被不同 search policy、evaluator 與 tree strategy 重新探索。這些工作並不證明本文的 basin ontology，但共同顯示：**proof search 的局部深度、全局覆蓋、多樣性與可達性必須被分開測量。**

本文最後重新分析 NS-203 corpus。既有 v0.1 observatory 在保守分類下得到 203 份 NS paper-like artifacts，其中 $T_1=84$、$T_2=107$、$T_3=10$、$T_X=2$；大量 recurrence、no-go 與跨系列 confluence 出現在特定研究支線，但固定窗口 novelty 測試並未支持整個 corpus 的單調全域崩塌。因此，NS-203 目前最合理的解讀不是「Navier--Stokes 證明空間被耗盡」，而是：

$$
\boxed{
\text{some proof basins show higher-order resampling while the corpus remains globally open at the observed level.}
}
$$

本文由此提出一個更一般的研究原則：長程 AI 研究的成熟標誌，不是讓同一 basin 變得越來越密，而是能辨識自己何時正在重採樣局部結構、何時需要改變 representation／premise／method family／resource regime，並把每次 basin escape 的成功或失敗保存為下一輪研究資料。

**關鍵詞：** 局部飽和、全域開放、proof basin、proof-space conductance、frontier、basin escape、route recurrence、confluence、audited novelty、global premise retrieval、proof search、AI 數學研究、Navier--Stokes corpus

---

# 1. 問題的提出：為什麼「整體新奇度」是一個危險的單一指標

## 1.1 長程研究不會均勻覆蓋證明空間

設一個研究系統在固定問題 $Q$ 上持續生成：

$$
g_1,g_2,\ldots,g_N.
$$

如果只看文本數量，最自然的直覺是：

$$
N\uparrow
\Rightarrow
\text{coverage}\uparrow.
$$

但 LSI-PSD-02 與 03 已指出，這個箭頭至少需要經過兩次修正：

第一，生成 artifact 不等於新增有效研究狀態；

第二，表面不同的 artifact 經語義 quotient 後可能落入同一個等價類。

因此真正的計量對象不是：

$$
N,
$$

而是：

$$
\left|
\Omega^{\mathrm{obs}}_R(Q)/\sim
\right|.
$$

然而，即使已經做了 quotient，仍有第三個問題：研究採樣通常不是均勻的。

LLM、retriever、verifier、prompt、既有 corpus 與研究者偏好會形成路徑依賴，使系統較容易反覆進入某些區域。

## 1.2 同一個區域可以很深，但旁邊仍然很空

考慮一個簡化圖：

```text
             B3
            /  \
           /    \
      B1=======B2
      |||       \
      |||        \
   dense core     frontier
```

假設 $B_1$ 內已經存在大量：

- lemma variants；
- proof routes；
- obstruction IDs；
- second-order revisits；
- confluence relations；
- all-order no-go candidates。

則 $B_1$ 可以非常「密」。

但這個密度不能直接推出：

$$
B_2,\ B_3
$$

也同樣被探索。

更不能推出：

$$
V_R=B_1.
$$

所以長程研究必須回答兩個不同問題：

$$
\text{How saturated is this region?}
$$

與：

$$
\text{How much of the reachable space is this region?}
$$

## 1.3 研究越成功，越容易被自己的成功困住

一個早期有效的方法族可能帶來大量成果：

$$
M_1
\rightarrow
L_1,L_2,\ldots,L_m.
$$

這會形成強烈的內部 reinforcement：

- retriever 更常抓回 $M_1$ 的相關 lemma；
- prompt 更常引用 $M_1$ 的語言；
- evaluator 更熟悉 $M_1$ 的成功模式；
- knowledge graph 的高中心度節點越來越偏向 $M_1$；
- 後續模型在 context 中看到更多 $M_1$ 的成功歷史。

於是：

$$
P(\text{return to }B_1)\uparrow.
$$

這個現象並不表示 $B_1$ 是錯的。

恰恰相反，它可能是因為 $B_1$ 曾經非常成功。

問題在於：

$$
\text{successful basin}
\neq
\text{complete proof space}.
$$

---

# 2. 從單一空間改成加權研究圖

## 2.1 可觀測證明空間

固定：

$$
Q=\text{研究問題},
$$

$$
R=(\mathcal A,\mathcal L,\mathcal M,\mathcal V,\mathcal B,\mathcal H),
$$

其中：

- $\mathcal A$：公理與背景理論；
- $\mathcal L$：表示與符號語言；
- $\mathcal M$：方法族；
- $\mathcal V$：驗證／稽核制度；
- $\mathcal B$：算力、時間、token、模型調用等預算；
- $\mathcal H$：已保存的研究歷史。

本文把在 $R$ 下被實際建構、保留或稽核的研究對象寫成：

$$
\Omega_R^{\mathrm{obs}}(Q).
$$

它不是所有數學上可能證明的集合。

它只是：

$$
\boxed{
\text{under regime }R,\ \text{what the research system has made observable}.
}
$$

## 2.2 語義 quotient 後的節點

依 LSI-PSD-03，先建立語義等價關係：

$$
x\sim y.
$$

例如：

- $\alpha$-renaming；
- 純記號替換；
- 同一 lemma skeleton；
- 同一 normalized hypothesis set；
- 同一 obstruction under audited equivalence；
- 經證明可逆的 representation change。

令：

$$
V_R
=
\Omega_R^{\mathrm{obs}}(Q)/\sim.
$$

此後的 basin 分析原則上作用於 $V_R$，不是原始文本。

## 2.3 邊的型別

建立 typed edge：

$$
e=(u,\tau,v),
$$

其中：

$$
\tau
\in
\{
\text{derive},
\text{depend},
\text{rewrite},
\text{revisit},
\text{contradict},
\text{converge},
\text{generalize},
\text{specialize},
\text{transfer},
\text{escape}
\}.
$$

對每條邊給予權重：

$$
w(e)\ge0.
$$

權重可以綜合：

- formal verification；
- manual audit；
- independent replication；
- semantic-equivalence confidence；
- chronology confidence；
- citation／dependency evidence。

因此：

$$
\mathcal G_R(Q)
=
(V_R,E_R,w_R).
$$

## 2.4 不把圖本身當作本體

必須保持：

$$
\boxed{
\mathcal G_R(Q)
\neq
\Omega^{\mathrm{math}}(Q).
}
$$

圖是觀測儀器。

它和氣象雷達、粒子探測器、醫學影像一樣，只是在特定解析度下重建一個可操作結構。

若圖沒有看到某個區域，只能說：

$$
\text{not observed}.
$$

不能說：

$$
\text{does not exist}.
$$

---

# 3. 操作性 basin：什麼叫「研究被困在一個局部區域」

## 3.1 Basin 不應只靠 embedding cluster 定義

如果把相似文本聚類後直接命名為 proof basin，會立刻出現錯誤。

同一個詞：

$$
\text{criticality}
$$

可能出現在完全不同的數學機制。

反過來，真正等價的兩條路可能使用不同詞彙。

因此本文要求 basin 至少同時參考：

$$
\text{semantic similarity},
$$

$$
\text{route connectivity},
$$

$$
\text{obstruction identity},
$$

$$
\text{dependency structure}.
$$

## 3.2 操作性 basin 定義

對：

$$
B\subseteq V_R,
$$

定義內部邊總重：

$$
W_{\mathrm{in}}(B)
=
\sum_{u,v\in B}
w(u,v).
$$

跨界邊總重：

$$
W_{\mathrm{out}}(B)
=
\sum_{\substack{u\in B\\v\notin B}}
w(u,v).
$$

若：

$$
W_{\mathrm{in}}(B)
\gg
W_{\mathrm{out}}(B),
$$

而且固定時間窗中研究軌跡反覆回到 $B$，則 $B$ 是一個候選 basin。

本文把這稱為：

$$
\boxed{
\text{Operational Proof Basin}.
}
$$

## 3.3 Conductance

借用圖論中的 conductance 形式，但不把它宣稱為 proof-space 的自然測度。

定義節點 volume：

$$
\operatorname{vol}(B)
=
\sum_{u\in B}
\deg_w(u).
$$

則：

$$
\phi(B)
=
\frac{
W_{\mathrm{out}}(B)
}{
\min(
\operatorname{vol}(B),
\operatorname{vol}(V_R\setminus B)
)
}.
$$

直覺上：

$$
\phi(B)\downarrow
$$

表示 basin 內部連結強、外部通道相對少。

但低 $\phi(B)$ 仍可能有三種不同解釋：

1. 真正存在結構性分區；
2. retriever／prompt 導致的人工作業偏差；
3. corpus 尚未建立跨區邊。

因此 conductance 是診斷量，不是本體結論。

## 3.4 Recurrence density

令時間窗：

$$
I_{N,W}
=
\{N-W+1,\ldots,N\}.
$$

令：

$$
r_t(B)
=
\mathbf 1[x_t\in B].
$$

定義：

$$
R_W(B)
=
\frac{1}{W}
\sum_{t\in I_{N,W}}
r_t(B).
$$

若：

$$
R_W(B)\rightarrow1,
$$

表示近期研究高度集中於 $B$。

如果此時 novelty 又下降，才開始形成局部飽和候選。

---

# 4. 局部飽和必須是多條件，而不是「最近看起來都一樣」

## 4.1 單一 novelty 不足

定義局部 novelty：

$$
\nu(B,t).
$$

若：

$$
\nu(B,t)\downarrow,
$$

可能只是：

- 模型變弱；
- prompt 固化；
- 資源不足；
- summarization 損失；
- retriever 重複；
- quotient 太粗；
- 真正研究空間局部收斂。

所以：

$$
\nu\downarrow
$$

本身不能定義 saturation。

## 4.2 第 $k$ 階 audited yield

沿用 LSI-PSD-04，令：

$$
A_k(B;N,W)
$$

是固定窗口內進入 basin $B$ 的第 $k$ 階新 artifact 數。

令：

$$
U_k(B;N,W)
$$

是人工或形式稽核後，仍被判為新的有效等價類數。

定義：

$$
\rho_k(B;N,W)
=
\frac{
U_k(B;N,W)
}{
\max(1,A_k(B;N,W))
}.
$$

當：

$$
\rho_k(B;N,W)\rightarrow0,
$$

表示該階 artifact 增加，但有效新類別很少增加。

## 4.3 多階局部飽和

對指定 $K$：

$$
\mathbf \rho_{0:K}(B)
=
(
\rho_0(B),
\rho_1(B),
\ldots,
\rho_K(B)
).
$$

本文定義 basin $B$ 在窗口 $(N,W)$ 下的操作性 $K$ 階局部飽和標記：

$$
S_K(B;N,W)=1
$$

當且僅當至少同時滿足：

$$
\rho_k(B;N,W)<\varepsilon_k
\qquad
\forall k\le K,
$$

$$
R_W(B)>\tau_R,
$$

$$
\phi(B)<\tau_\phi,
$$

且：

$$
A_k(B;N,W)\ge m_k,
$$

以避免「根本沒採樣」被誤判成飽和。

## 4.4 低產量和飽和是不同的

如果：

$$
A_k(B;N,W)=0,
$$

則：

$$
\rho_k=0
$$

沒有任何意義。

因為這可能只是：

$$
\text{no sampling}.
$$

所以局部飽和必須要求：

$$
\text{sufficient attempt density}.
$$

這是整個方法論最重要的防偽條件之一。

---

# 5. 局部飽和非傳播原則

## 5.1 核心命題

本文提出：

$$
\boxed{
S_K(B)=1
\not\Rightarrow
S_K(V_R)=1.
}
$$

這稱為：

**局部飽和非傳播原則**
（Local Saturation Non-Propagation Principle）。

它不是深奧定理。

它是一個對研究語言的約束：只要 $B$ 不是已證明等於整個可觀測空間，就不能把局部判定提升成全域判定。

## 5.2 更強的防誤推論形式

即使：

$$
S_K(B_i)=1
$$

對多個已知 basin：

$$
B_1,\ldots,B_m
$$

全部成立，仍只能得到：

$$
\text{known-basin saturation}.
$$

不能直接推出：

$$
\text{mathematical global exhaustion}.
$$

因為仍可能有：

$$
B_{m+1}
$$

尚未被表示。

甚至可能有新的表示語言：

$$
\mathcal L'
$$

使原本不可見的區域突然出現。

## 5.3 Regime-bounded global saturation

若在固定 $R$ 下，研究系統已建立一個 audited cover：

$$
\mathcal C_R
=
\{B_1,\ldots,B_m,F\},
$$

其中 $F$ 是 frontier pool。

若：

$$
S_K(B_i)=1
$$

對所有 $i$ 成立，且：

$$
F
$$

在足夠多次有意識的 escape intervention 後仍沒有穩定新增 audited class，則可以標記：

$$
\boxed{
\operatorname{Sat}^{R,K}_{\mathrm{global,obs}}=1.
}
$$

這個量的名稱中必須保留：

$$
R
$$

與：

$$
\mathrm{obs}.
$$

因為它只代表：

> 在目前制度與觀測器下，已知可達空間呈現全域操作性飽和。

它仍不代表：

$$
\Omega^{\mathrm{math}}
$$

已耗盡。

---

# 6. 全域開放：什麼情況下可以說「還有地方沒走」

## 6.1 Frontier

令：

$$
\mathfrak F_R(N)
$$

是目前觀測到、具有某種可達證據，但尚未充分展開的節點／候選集合。

候選 frontier 可以來自：

- unresolved dependency；
- unused premise cluster；
- new representation；
- unexplored counterexample regime；
- cross-domain transfer；
- independent model proposal；
- human-supplied conjectural bridge；
- external theorem library；
- failed route 的 alternative branch。

## 6.2 Frontier 不是「未知的全部」

應明確區分：

$$
\mathfrak F_R(N)
$$

與：

$$
V_R^{\mathrm{unknown}}.
$$

前者是：

$$
\text{known unknowns}.
$$

後者甚至沒有被表示。

因此：

$$
|\mathfrak F_R(N)|=0
$$

不能推出：

$$
V_R^{\mathrm{unknown}}=\varnothing.
$$

## 6.3 觀測性開放證書

如果存在：

$$
f\in\mathfrak F_R(N)
$$

以及至少一條 auditable transition：

$$
u\in B
\longrightarrow
f,
$$

且展開 $f$ 後產生：

$$
U_k(f)>0,
$$

則可說：

$$
\boxed{
\operatorname{Open}^{R,K}_{\mathrm{obs}}(N)=1.
}
$$

即在目前 regime 下，已直接觀察到 proof-space renewal。

這是一個很強但有限的結論：

> 我們知道目前還沒飽和。

它不需要知道完整空間有多大。

---

# 7. Basin escape：研究不只是繼續走，也要知道何時換區域

## 7.1 Escape action

定義 escape action：

$$
a
\in
\mathcal A_{\mathrm{esc}}.
$$

例如：

- 換 representation；
- 換座標系；
- 換 invariant；
- 換 scale；
- 換 proof assistant；
- 換 theorem library；
- 換 premise retriever；
- 換模型；
- 換 prompt policy；
- 換 method family；
- 引入反例搜尋；
- 強制跨域 transfer；
- 暫時移除高中心度 lemma；
- 從 final theorem 倒推必要條件；
- 從失敗 obstruction 反向生成新問題。

## 7.2 Escape gain

令：

$$
\bar\rho_k^{\mathrm{in}}(B)
$$

是 basin 內近期平均 audited yield。

執行 escape action $a$ 後，在窗口 $W'$ 內得到：

$$
\bar\rho_k^{\mathrm{out}}(B,a).
$$

定義：

$$
\Gamma_{\mathrm{esc},k}(B,a)
=
\bar\rho_k^{\mathrm{out}}(B,a)
-
\bar\rho_k^{\mathrm{in}}(B).
$$

若：

$$
\Gamma_{\mathrm{esc},k}>0,
$$

則 escape 至少在第 $k$ 階提高了新增有效資訊率。

## 7.3 Escape 可以失敗，而且失敗也有資訊

若：

$$
\Gamma_{\mathrm{esc},k}\le0,
$$

不能立刻說新 representation 沒價值。

可能原因包括：

- 新 representation 尚未學會；
- verifier 不支援；
- retriever 尚未索引；
- translation loss；
- budget 太小；
- 新 basin 本身也飽和；
- 原 basin 與新 basin 其實 quotient-equivalent。

因此每次 escape 都應保存：

$$
(
a,
B_{\mathrm{src}},
B_{\mathrm{dst}},
\Delta\rho,
\Delta\nu,
\Delta\phi,
\text{failure trace}
).
$$

這些資料會形成下一階 proof-space science 的 corpus。

---

# 8. 多盆地結構：證明空間更像 cover，而不是單一區塊

## 8.1 不要求 basin 互斥

真實研究中：

$$
B_i\cap B_j
\neq
\varnothing
$$

是常態。

例如：

- compactness route；
- recurrence route；
- energy route；

可能共享：

$$
\text{critical scaling}.
$$

所以本文不要求：

$$
V_R
=
\bigsqcup_i B_i.
$$

而採用 cover：

$$
V_R
\approx
\bigcup_{i=1}^{m}B_i
\cup
\mathfrak F_R.
$$

## 8.2 Overlap 是重要資訊

對：

$$
B_i,B_j,
$$

定義 overlap：

$$
O_{ij}
=
\frac{
\operatorname{vol}(B_i\cap B_j)
}{
\operatorname{vol}(B_i\cup B_j)
}.
$$

高 overlap 可能意味：

- 方法族實際上共享同一核心；
- obstruction 是跨 basin 的；
- basin 切分太細；
- 一個 bridge lemma 形成共同通道。

## 8.3 Cross-basin traffic

定義：

$$
T_{ij}
=
\sum_{\substack{u\in B_i\\v\in B_j}}
w(u,v).
$$

形成 basin traffic matrix：

$$
\mathbf T
=
[T_{ij}].
$$

若：

$$
T_{ij}\gg0,
$$

表示兩個 basin 之間有實際研究通道。

若：

$$
T_{ij}\approx0,
$$

則需要判斷：

- 真正結構分離；
- corpus 缺邊；
- retriever 沒找到；
- 研究者根本沒試過。

## 8.4 Basin-level entropy

令近期研究在 basin 上的分布為：

$$
p_i(N,W).
$$

定義：

$$
H_B(N,W)
=
-
\sum_i
p_i\log p_i.
$$

低 entropy：

$$
H_B\downarrow
$$

表示研究高度集中。

但低 entropy 不一定壞。

若某 basin 正在產生高 audited yield：

$$
\rho_k\gg0,
$$

集中可能是合理 exploit。

只有當：

$$
H_B\downarrow
$$

與：

$$
\rho_k\downarrow
$$

長期同時成立，才更像「被困」。

---

# 9. Exploration--Exploitation 不能簡化成「多試幾條」

## 9.1 大搜尋空間中的經典困境

formal theorem proving 的 action space 很大。

在 proof state：

$$
s_t,
$$

模型可以產生大量 tactic：

$$
a_t^{(1)},a_t^{(2)},\ldots.
$$

若每個 tactic 再分支，搜尋樹快速膨脹。

因此所有 prover 都必須在：

$$
\text{exploration}
$$

與：

$$
\text{exploitation}
$$

間取捨。

## 9.2 BFS-Prover：深路徑也需要被刻意鼓勵

BFS-Prover 顯示，簡單 best-first tree search 若配合適當的 expert iteration、compiler feedback 與 length normalization，可以有效提升大型 Lean proof search。

對本文而言，重要的不是其 benchmark 排名，而是：

$$
\boxed{
\text{search policy itself changes which region becomes reachable}.
}
$$

如果一個 policy 系統性偏好短 proof，則某些需要先繞遠的 basin 會被壓低。

因此：

$$
\text{unvisited}
$$

不等於：

$$
\text{unproductive}.
$$

## 9.3 FETCH：過度探索和探索不足可以同時存在

FETCH 的分析尤其重要。

它區分：

$$
\text{over-exploration}
$$

來自大量語義等價／重複狀態；

以及：

$$
\text{under-exploration}
$$

來自 verifier score 高 variance 導致軌跡頻繁切換。

這兩者可以同時發生：

> 系統花很多算力，但既重複走舊路，又沒有把真正的新路走深。

因此「生成量巨大」不能直接當 coverage 指標。

## 9.4 FormalEvolve：固定預算下，多樣性本身是可優化量

FormalEvolve 把 autoformalization 設計成：

$$
\text{budgeted repertoire search}.
$$

它不只追求一個可編譯候選，而是維持 diverse candidate repertoire，並測量 cross-problem coverage concentration。

這為本文提供直接啟發：

$$
\boxed{
\text{proof-space observatory should track diversity distribution, not only success count}.
}
$$

---

# 10. 局部 premise 和全域 premise：另一種 basin 盲點

## 10.1 單步最相關不等於整體最必要

LeanSearch v2 提出 global premise retrieval：

> 一個研究級 theorem 往往需要一組分散在 library 各處、聯合起來才足夠的 lemma。

因此：

$$
\operatorname{TopK}(s_t)
$$

的局部 premise selection 不必等於：

$$
P^\star(Q)
$$

這個完整 proof 所需的 premise set。

## 10.2 Premise basin

如果 retriever 長期只回傳同一高相關 cluster：

$$
P_1,
$$

研究系統會形成：

$$
B_{\mathrm{premise}}(P_1).
$$

即使該 cluster 內搜尋非常深入，也可能一直缺：

$$
p^\star
\notin
P_1.
$$

這時候局部 proof search 會呈現：

- 高 recurrence；
- 高 lemma reuse；
- 高 internal connectivity；
- 長期無 closure。

但問題不一定是 proof strategy。

可能只是：

$$
\boxed{
\text{premise basin lock-in}.
}
$$

## 10.3 Global retrieval 作為 basin escape

LeanSearch v2 的 sketch--retrieve--reflect 類型流程，可被重新解讀為：

$$
B_i
\rightarrow
\text{global premise query}
\rightarrow
B_j.
$$

這不是說 LeanSearch v2 在研究 basin theory。

而是它提供一個工程案例：

> 改變 retrieval level 本身可以改變可達 proof space。

---

# 11. Blueprint、DAG 與 dead-end basin

## 11.1 Goedel-Architect 的全局視角

Goedel-Architect 不是只逐步遞歸拆 lemma。

它先建立 definitions / lemmas 的 dependency blueprint：

$$
\mathcal B_Q.
$$

若某些 lemma proof 失敗，失敗會回饋到 blueprint refinement。

這件事對 proof-space dynamics 很重要。

因為：

$$
\text{failure}
$$

不只是葉節點錯誤。

它可以改變：

$$
\text{global route architecture}.
$$

## 11.2 Dead-end strategy

若一個 route family：

$$
R_a
$$

反覆產生：

$$
O_a
$$

而 blueprint 層知道：

$$
R_a\rightarrow O_a
$$

已經多次重現，系統就不必無限在低階 tactic 層重跑。

這正是：

$$
\boxed{
\text{basin-level memory}.
}
$$

它把：

$$
\text{this tactic failed}
$$

提升成：

$$
\text{this strategy family has a known recurrent obstruction under these assumptions}.
$$

## 11.3 Basin memory 是避免計算浪費的必要條件

如果沒有 basin memory：

$$
\text{failure}_1,
\text{failure}_2,
\ldots
$$

只會變成大量局部 log。

如果有：

$$
O_{\mathrm{ID}},
$$

則可以建立：

$$
\operatorname{Avoid}(B,O_{\mathrm{ID}},\mathcal H).
$$

或：

$$
\operatorname{Escape}(B,O_{\mathrm{ID}}).
$$

這是從 theorem prover 走向 research observatory 的關鍵差異。

---

# 12. TreeThink 與「搜尋方法本身」的可交換性

## 12.1 不同 search algorithm 會看到不同空間切片

TreeThink 將：

- BFS；
- beam；
- MCTS；

等 search strategy 模組化，並可搭配不同 evaluator。

這提醒我們：

$$
\Omega^{\mathrm{obs}}_R
$$

其實高度依賴：

$$
R.
$$

如果：

$$
R_1
\neq
R_2,
$$

則：

$$
\Omega^{\mathrm{obs}}_{R_1}
\neq
\Omega^{\mathrm{obs}}_{R_2}
$$

完全合理。

## 12.2 因此飽和必須帶 regime index

本文拒絕寫：

$$
\operatorname{Sat}(Q).
$$

更合理的是：

$$
\operatorname{Sat}(Q\mid R).
$$

進一步：

$$
S_K(B\mid R,N,W).
$$

只要模型、retriever、方法族或 verifier 改變：

$$
R\rightarrow R',
$$

舊的 saturation label 就必須重新評估。

---

# 13. Representation basin：換句話說，有時候你不是卡在證明，而是卡在語言

## 13.1 同一命題的 representation 不一定等難

LSI-PSD-03 已討論：

$$
x\sim y
$$

在數學語義上等價，不代表：

$$
\operatorname{Cost}_{\mathrm{search}}(x)
=
\operatorname{Cost}_{\mathrm{search}}(y).
$$

因此一個 proof basin 可能其實是 representation basin。

## 13.2 Representation lock-in

若長程 corpus 形成固定語言：

$$
\mathcal L_1,
$$

retriever、prompt、lemma naming、obstruction taxonomy 都會逐漸適應：

$$
\mathcal L_1.
$$

這會降低換到：

$$
\mathcal L_2
$$

的短期效率。

於是研究系統可能錯誤得出：

> $\mathcal L_2$ 沒用。

實際上只是：

$$
\text{switching cost}>0.
$$

## 13.3 Escape intervention 必須給新 representation 成熟時間

因此測：

$$
\Gamma_{\mathrm{esc}}
$$

時不能只看一次生成。

應設：

$$
W_{\mathrm{adapt}}>0.
$$

先允許：

- vocabulary adaptation；
- premise re-indexing；
- theorem translation；
- verifier bridge；
- agent memory migration。

然後再比較長期 yield。

---

# 14. Method basin：同一套成功方法可以把自己變成盲點

## 14.1 方法族的自我強化

設：

$$
\mathcal M_1
$$

曾經產生大量有效結果。

系統會自然提高：

$$
P(\mathcal M_1\mid Q,\mathcal H).
$$

這在貝氏意義上不是不合理。

但是如果 posterior 太快坍縮：

$$
P(\mathcal M_j)\rightarrow0
\qquad
j\neq1,
$$

則研究失去探索能力。

## 14.2 方法多樣性

定義近期 method-family distribution：

$$
p_m.
$$

方法 entropy：

$$
H_M
=
-
\sum_m
p_m\log p_m.
$$

若：

$$
H_M\downarrow
$$

且：

$$
\rho_k\downarrow,
$$

應啟動 method diversification。

若：

$$
H_M\downarrow
$$

但：

$$
\rho_k\gg0,
$$

則可能只是合理集中。

所以 entropy 不能獨立判讀。

## 14.3 Forced ablation

一個強測試是暫時禁用高中心度方法：

$$
\mathcal M_{\max}.
$$

比較：

$$
\rho_k^{(-\mathcal M_{\max})}
$$

與：

$$
\rho_k^{(\mathrm{full})}.
$$

如果禁用後 novelty 上升，說明原系統可能有 method lock-in。

如果禁用後全面崩潰，則高中心度方法可能真的承擔重要結構。

---

# 15. Resource basin：資源不足也會偽裝成局部飽和

## 15.1 固定 budget 會截斷深路徑

對一個 proof route：

$$
r,
$$

若所需成本：

$$
C(r)>\mathcal B,
$$

則在目前制度下：

$$
r
$$

永遠無法完整展開。

長期看起來會像：

$$
\text{recurrent partial progress}
\rightarrow
\text{same obstruction}.
$$

但真正原因可能只是：

$$
\boxed{
\text{budget ceiling}.
}
$$

## 15.2 Resource escalation test

令：

$$
\mathcal B_1<\mathcal B_2<\cdots.
$$

測：

$$
\rho_k(B\mid\mathcal B_j).
$$

如果：

$$
\rho_k
$$

隨 budget 增加顯著恢復，則原飽和標記應被撤回或降級。

若在大幅 resource escalation 後仍沒有變化，才增加「方法／表示瓶頸」的相對可信度。

但仍不能推出原命題錯誤。

---

# 16. Evaluator basin：評分器可能把搜尋困在自己的偏好中

## 16.1 Proof search 不只由 generator 決定

搜尋決策通常依賴：

$$
V(s),
$$

或：

$$
P(a\mid s).
$$

若 evaluator 偏好某類短、熟悉、局部可驗證的狀態，可能壓低長期高價值 route。

## 16.2 Evaluator ensemble

一個實驗方法是建立：

$$
V_1,V_2,\ldots,V_m.
$$

比較不同 evaluator 下：

$$
\mathcal G_R^{(i)}.
$$

若 basin 結構對 evaluator 高度敏感：

$$
B^{(1)}
\neq
B^{(2)},
$$

則「局部飽和」很可能有 instrument dependence。

## 16.3 Instrument dependence 不等於沒有真結構

科學觀測本來就有儀器依賴。

重點不是要求：

$$
\mathcal G_R
$$

完全客觀。

而是要求：

$$
\boxed{
\text{instrument dependence be measured and declared}.
}
$$

---

# 17. 時間、順序與研究歷史本身會塑造 basin

## 17.1 Path dependence

令研究歷史：

$$
\mathcal H_N
=
(g_1,\ldots,g_N).
$$

下一輪策略：

$$
\pi_{N+1}
=
\Pi(Q,\mathcal H_N).
$$

所以：

$$
\mathcal H_N
$$

不只是紀錄。

它是搜尋動力的一部分。

## 17.2 重排實驗

可對 corpus 做 random permutation：

$$
\sigma(\mathcal H_N).
$$

但必須注意：

> 真實研究不能真的把歷史重排。

Permutation test 只能回答統計問題，例如：

$$
\text{observed novelty trend}
$$

是否超過順序隨機化的基線。

它不能模擬「如果研究歷史真的不同，AI 會走哪裡」。

## 17.3 Forked-history experiment

更強的測試是：

從某 checkpoint：

$$
H_t
$$

建立多個 fork：

$$
H_t^{(1)},
H_t^{(2)},
\ldots,H_t^{(m)}.
$$

給不同方法政策。

比較：

$$
B^{(1)}_{t+\Delta},
\ldots,
B^{(m)}_{t+\Delta}.
$$

這能直接測：

$$
\text{basin dependence on research history}.
$$

---

# 18. NS-203：為什麼它目前更像「局部高階採樣」而不是「全域耗盡」

## 18.1 Corpus accounting

NS Proof-Space Sampling Observatory v0.1 對整包遞迴掃描後得到：

$$
1109
$$

個 file instances，

其中：

$$
593
$$

個 Markdown instances，

去除 exact duplicate 後：

$$
565
$$

個 unique Markdown artifacts。

保守排除：

- README；
- CHANGELOG；
- SOURCE_POLICY；
- checkpoint；
- roadmap；
- handoff；
- audit；

後，得到：

$$
\boxed{
203
}
$$

份 NS paper-like artifacts。

## 18.2 高階採樣 tier

v0.1 的操作性 tier 分布為：

$$
T_1=84,
$$

$$
T_2=107,
$$

$$
T_3=10,
$$

$$
T_X=2.
$$

這顯示 corpus 已存在大量：

$$
\text{route revisit}.
$$

而少數支線進入：

$$
\text{confluence / higher-order family analysis}.
$$

## 18.3 但全域 novelty collapse 沒有被建立

累積 nearest-neighbor novelty 從早期下降到後期，看似支持飽和。

但累積比較池會隨時間變大，因此有 size bias。

固定窗口：

$$
W=20
$$

後，得到：

$$
\bar\nu_{\mathrm{Q2}}=0.5425,
$$

$$
\bar\nu_{\mathrm{Q4}}=0.5781.
$$

不是後期更低。

500 次 permutation baseline 得：

$$
z\approx1.01.
$$

因此 v0.1 沒有支持：

$$
\boxed{
\text{whole-corpus monotone novelty collapse}.
}
$$

## 18.4 這反而正好支持本文的問題設定

如果 corpus 裡：

- 某些 X72 round 出現 obstruction confluence；
- 某些 DCRP 路線進入 second-order / higher-order residue；
- C5-H 出現 all-order escalation；
- 多個 series 反覆命中 carrier-supplier、rigidity-closure、obstruction-gap-defect；

同時整體固定窗 novelty 沒崩塌，

那最自然的候選模型正是：

$$
\boxed{
\text{localized basin saturation + globally open observed corpus}.
}
$$

## 18.5 不能從 NS-203 推出什麼

不能推出：

$$
\text{Navier--Stokes is misframed}.
$$

不能推出：

$$
\text{Navier--Stokes is unprovable}.
$$

不能推出：

$$
\text{the Clay problem is badly defined}.
$$

不能推出：

$$
\text{AI has exhausted known mathematics}.
$$

目前只可以說：

> 在這個特定 AI 長程研究 corpus 中，某些方法／概念／障礙區域顯示高 recurrence 與高階再採樣，而整個 corpus 尚未顯示穩健的全域 novelty collapse。

這是 observational claim。

---

# 19. 從 concept family 到 basin：第二版 observatory 應如何升級

## 19.1 v0.1 的限制

目前 concept family 如：

$$
\text{carrier-supplier},
$$

$$
\text{rigidity-closure},
$$

$$
\text{obstruction-gap-defect}
$$

仍然是 routing ontology。

它們不能直接當 basin。

因為同一 broad family 可能包含多個不等價的 theorem state。

## 19.2 Canonical obstruction ID

第二版應建立：

```text
OBSTRUCTION_ID
ASSUMPTIONS
DOMAIN
NORMALIZED_STATEMENT
TERMINAL_STATUS
PROOF_DEPENDENCIES
COUNTEREXAMPLE_STATUS
AUDIT_LEVEL
```

若兩個 artifact 只有在：

$$
\text{normalized assumptions}
$$

與：

$$
\text{terminal obstruction}
$$

都被確認等價後，才允許合併。

## 19.3 Basin graph

建立：

$$
G_O
=
(V_O,E_O),
$$

其中：

$$
V_O
=
\{\text{audited obstruction / route states}\}.
$$

再以：

- recurrence；
- shared dependencies；
- transfer；
- confluence；

建立 basin。

這會比 title embedding 強得多。

---

# 20. 一個可重現的 Basin Detection Protocol

## 20.1 Step A：建立 canonical node

對每個 artifact 抽取：

$$
x_i
=
(
A_i,
C_i,
L_i,
O_i,
S_i
),
$$

其中：

- $A_i$：assumptions；
- $C_i$：claims；
- $L_i$：lemma dependency；
- $O_i$：obstruction；
- $S_i$：status。

## 20.2 Step B：先 quotient，再聚類

建立：

$$
x_i\sim x_j.
$$

只在 audited equivalence 後合併。

避免：

$$
\text{cluster first}
\rightarrow
\text{assume equivalence later}.
$$

## 20.3 Step C：建立 typed graph

邊至少分：

$$
E_{\mathrm{derive}},
E_{\mathrm{revisit}},
E_{\mathrm{depend}},
E_{\mathrm{converge}},
E_{\mathrm{escape}}.
$$

不要把所有關係壓成單一 similarity edge。

## 20.4 Step D：候選 basin

使用多種 community / conductance 方法產生候選：

$$
B_1,\ldots,B_m.
$$

但 algorithm 只負責：

$$
\text{candidate generation}.
$$

最終 basin label 仍需 structural audit。

## 20.5 Step E：計算多階 yield

對每個 basin：

$$
\rho_0,\rho_1,\ldots,\rho_K.
$$

再配：

$$
R_W,\phi,H_B,H_M.
$$

## 20.6 Step F：主動 escape

如果：

$$
S_K(B)=1,
$$

則至少觸發數個不同類型 escape：

$$
a_1,\ldots,a_m.
$$

例如：

- representation switch；
- premise-globalization；
- method ablation；
- resource escalation；
- model-family change。

## 20.7 Step G：再判定

只有當多種 escape 都沒有帶來：

$$
\Gamma_{\mathrm{esc}}>0
$$

時，才把 saturation confidence 上調。

仍然不能上調成：

$$
\text{unprovability confidence}=1.
$$

---

# 21. Saturation Confidence：把「看起來飽和」變成分級證據

## 21.1 分數

定義：

$$
C_{\mathrm{sat}}(B)
=
f(
\rho,
R_W,
\phi,
D_{\mathrm{audit}},
E_{\mathrm{attempt}},
E_{\mathrm{escape}},
R_{\mathrm{robust}}
).
$$

其中：

- $D_{\mathrm{audit}}$：人工／形式稽核深度；
- $E_{\mathrm{attempt}}$：有效嘗試量；
- $E_{\mathrm{escape}}$：escape intervention 多樣性；
- $R_{\mathrm{robust}}$：對模型、retriever、順序、budget 的穩健度。

## 21.2 建議分級

### Level 0：未評估

資料不足。

### Level 1：表面 recurrence

文字／概念重複增加。

### Level 2：route recurrence

audited route 重訪。

### Level 3：multi-order recurrence

多階 novelty yield 同時下降。

### Level 4：escape-resistant local saturation

多種 escape intervention 後仍低 yield。

### Level 5：regime-bounded global observational saturation

固定 $R$ 的已知 basin cover 全部高度飽和，frontier expansion 反覆失敗。

即使 Level 5，也不叫：

$$
\text{mathematical exhaustion}.
$$

---

# 22. 「全域開放」也不能被浪漫化

## 22.1 新東西很多不代表研究健康

若系統不停製造：

$$
\text{new terms},
$$

$$
\text{new symbols},
$$

$$
\text{new reformulations},
$$

但：

$$
\rho_k\approx0,
$$

則「看似開放」只是語言膨脹。

因此 global openness 需要 audited novelty。

## 22.2 Frontier quality

對 frontier candidate：

$$
f
$$

定義：

$$
Q_F(f)
=
g(
\text{semantic distance},
\text{formal validity},
\text{dependency novelty},
\text{obstruction novelty},
\text{transfer potential}
).
$$

只有：

$$
Q_F(f)>\tau_F
$$

才進入高優先級 frontier。

## 22.3 Open-ended 不是無限輸出

本文不把：

$$
\text{open}
$$

等同：

$$
\text{unbounded text generation}.
$$

更合理的是：

$$
\boxed{
\text{open}
=
\text{the system can still produce audited structural renewal under intervention}.
}
$$

---

# 23. 局部飽和與「越是真理越可能像廢話」的關係

## 23.1 不在本文提前證明後續命題

後續 LSI-PSD-07 將處理：

$$
\text{truth--generativity inversion}.
$$

本文只指出一個接口。

如果 basin 在不斷加入約束後：

$$
B_0\supset B_1\supset\cdots,
$$

可能出現：

$$
H(B_t)\downarrow.
$$

極端時：

$$
|B_t|\rightarrow1.
$$

那麼最後留下的核心命題可能表面非常簡單。

## 23.2 但局部簡化不等於全域真理

若某 basin 壓縮成：

$$
x^\star,
$$

只能說：

$$
\text{within this basin and regime, the survivor structure is simple}.
$$

不能推出：

$$
x^\star
=
\text{ultimate mathematical truth}.
$$

這個區分會在後續「真理—生成性反轉」與「生產性錯置」兩篇變得非常重要。

---

# 24. 局部飽和與問題範疇錯置的關係

## 24.1 Saturation 可以觸發 framing audit

如果：

$$
S_K(B)=1
$$

且多種 escape：

$$
a_1,\ldots,a_m
$$

都失敗，

系統可以提高：

$$
\operatorname{Priority}(\text{framing audit}).
$$

## 24.2 但不能直接診斷 framing error

必須保持：

$$
\boxed{
S_K(B)
\not\Rightarrow
\operatorname{Misframed}(Q).
}
$$

因為同樣現象也可能來自：

- 問題真的極難；
- 所需新理論尚未出現；
- proof 太長；
- resource 不夠；
- verifier 不夠表達；
- intelligence 不夠；
- independence；
- 命題為假但反例未找到。

## 24.3 Framing audit 是下一步，不是結論

因此流程應是：

$$
\text{local saturation}
\rightarrow
\text{audit trigger}
\rightarrow
\text{alternative hypotheses},
$$

而不是：

$$
\text{local saturation}
\rightarrow
\text{question is wrong}.
$$

---

# 25. 多模型、多方法與獨立研究線的真正作用

## 25.1 多 AI 不只是多投票

若所有 agent 使用：

$$
\text{same prompt},
$$

$$
\text{same retrieval},
$$

$$
\text{same model family},
$$

$$
\text{same proof memory},
$$

那：

$$
n\text{ agents}
$$

可能只是在同一 basin 裡並行採樣。

## 25.2 Independent basin probes

更好的設計是：

$$
R_1,\ldots,R_m
$$

有意做差異：

- model family；
- method family；
- representation；
- premise retriever；
- proof language；
- allowed tools；
- memory subset。

比較：

$$
\mathcal G_{R_1},
\ldots,
\mathcal G_{R_m}.
$$

## 25.3 交集和差集都重要

若多個 regime 都命中：

$$
O^\star,
$$

則：

$$
O^\star
$$

的 obstruction robustness 上升。

若：

$$
B^{(1)}
$$

只在某個 regime 出現，則可能是：

- 新發現；
- representation artifact；
- instrument artifact。

都值得研究。

---

# 26. 一個最小 Proof-Basin Observatory Schema

```yaml
problem:
  id: Q
  statement: ...
  formalization: ...
  domain: ...

regime:
  axioms: ...
  language: ...
  methods: ...
  verifier: ...
  model: ...
  retriever: ...
  budget: ...
  memory_version: ...

node:
  id: ...
  order: 0
  assumptions: ...
  claims: ...
  dependencies: ...
  obstruction_id: ...
  audit_status: ...
  equivalence_class: ...

edge:
  source: ...
  target: ...
  type: revisit
  audit_level: ...
  weight: ...

basin:
  id: ...
  members: ...
  conductance: ...
  recurrence_density: ...
  method_entropy: ...
  order_yield: ...
  saturation_level: ...

escape:
  id: ...
  source_basin: ...
  action_type: representation_switch
  destination: ...
  audited_gain: ...
  status: ...
```

這樣才可能讓：

$$
\text{basin}
$$

成為可重跑資料，而不是聊天中的比喻。

---

# 27. 對未來 AI 自主數學研究的架構含義

## 27.1 Agent 應該知道自己在哪個 basin

下一代數學 agent 不只需要：

> 下一步做什麼？

還要知道：

> 我現在是不是又回到過去研究過的 basin？

因此狀態應包含：

$$
b_t
=
\operatorname{BasinID}(s_t).
$$

## 27.2 Agent 應知道 basin 的歷史

例如：

```text
Basin B-17
attempts: 492
audited novel classes: 8
last 100 yield: 0.01
known obstructions: O-31, O-44
escape attempts:
  - representation switch: failed
  - premise globalization: positive
  - budget x4: neutral
```

這種記憶比單純：

> 以前試過。

強得多。

## 27.3 Meta-controller

可以建立：

$$
\Pi_{\mathrm{meta}}
$$

決定：

$$
\text{exploit},
\text{explore},
\text{escape},
\text{audit},
\text{stop}.
$$

輸入：

$$
(
C_{\mathrm{sat}},
\Gamma_{\mathrm{esc}},
H_B,
H_M,
\rho_k,
\mathfrak F_R
).
$$

## 27.4 Stop 也應該分層

不是只有：

$$
\text{proof found}
$$

或：

$$
\text{give up}.
$$

而是：

- stop this tactic；
- stop this route；
- stop this basin；
- stop this regime；
- pause this problem；
- request new definition；
- request stronger intelligence／resource；
- transfer descendants elsewhere。

這會大幅改善長程研究的計算效率。

---

# 28. 實驗一：Basin Escape Benchmark

## 28.1 目的

測試：

> 當局部 audited yield 下降時，主動換 basin 是否比繼續加算力更有效？

## 28.2 設計

選擇已知可解但證明路徑多樣的 theorem set。

對每題建立兩組：

### Control

$$
\text{continue same regime}.
$$

### Escape

當：

$$
C_{\mathrm{sat}}>\tau
$$

時，強制：

- representation switch；
- method switch；
- global premise retrieval；
- random restart。

## 28.3 指標

比較：

$$
P_{\mathrm{solve}},
$$

$$
\text{audited novel classes},
$$

$$
\text{tokens},
$$

$$
\text{verifier calls},
$$

$$
\text{time-to-new-basin}.
$$

## 28.4 可證偽性

如果 escape 組在多個資料集上：

$$
\Gamma_{\mathrm{esc}}\le0
$$

且成功率沒有改善，

則本文的 basin-control 工程價值會被削弱。

---

# 29. 實驗二：局部飽和假陽性測試

## 29.1 人工製造 retrieval lock

刻意限制 retriever：

$$
P_{\mathrm{retrieval}}
$$

只在一個子庫。

觀察是否產生：

$$
R_W\uparrow,
\quad
\rho\downarrow,
\quad
\phi\downarrow.
$$

## 29.2 解鎖

再恢復 global premise retrieval。

若 novelty 迅速恢復：

$$
\Gamma_{\mathrm{esc}}\gg0,
$$

則證明：

> 相同的飽和表面現象可以純粹由搜尋制度製造。

這是本文非常重要的 calibration experiment。

---

# 30. 實驗三：多模型 Basin Agreement

## 30.1 問題

不同模型是否會形成相同 basin？

## 30.2 定義

對 model $m$：

$$
\mathcal B^{(m)}
=
\{B_1^{(m)},\ldots\}.
$$

定義 basin alignment：

$$
A_{mn}
=
\operatorname{Match}(
\mathcal B^{(m)},
\mathcal B^{(n)}
).
$$

## 30.3 解讀

若：

$$
A_{mn}\approx1
$$

對不同架構模型都成立，

則 basin 更可能反映問題結構。

若：

$$
A_{mn}\approx0,
$$

則 basin 可能高度 model-specific。

兩種結果都重要。

---

# 31. 實驗四：NS-203 的第二輪 theorem-level basin audit

## 31.1 目標

把 v0.1：

$$
\text{title / concept family graph}
$$

提升成：

$$
\text{claim--lemma--obstruction graph}.
$$

## 31.2 抽樣

優先處理：

- NS-DCRP；
- NS-X72；
- NS-MORP；
- NS-FCBP；
- NS-C5；
- Proof Asset Map。

因為這些支線已有較高 recurrence 或 cross-series traffic。

## 31.3 手工 gold set

每條 route 至少抽取：

$$
50
$$

個 artifact pair。

雙重標註：

$$
\text{same basin?}
$$

$$
\text{same obstruction?}
$$

$$
\text{same proof skeleton?}
$$

$$
\text{mere lexical similarity?}
$$

## 31.4 成功條件

若自動 basin detector 對 gold set：

$$
F1>0.8
$$

並且 escape intervention 能穩定找出新 audited classes，

則可以開始談更強的 empirical proof-space dynamics。

---

# 32. Basin 與 SDPE：空間域證明包圍的局部版本

## 32.1 原始 filtration

SDPE 型思路可寫成：

$$
\Omega_{t+1}
=
\Omega_t\cap H_t.
$$

每個 audited no-go：

$$
H_t
$$

切除不可能區域。

## 32.2 多 basin filtration

本文改成：

$$
B_i^{(t+1)}
=
B_i^{(t)}
\cap
H_t.
$$

不同 theorem cut 只影響部分 basin。

甚至可能：

$$
H_t
$$

同時：

- 壓縮 $B_1$；
- 不影響 $B_2$；
- 打開 $B_3$ 的新 bridge。

因此 proof enclosure 不是單調「整塊空間縮小」的唯一圖像。

更一般的是：

$$
\boxed{
\text{local contraction + basin splitting + bridge creation + frontier renewal}.
}
$$

## 32.3 研究過程可以改變空間的有效座標

如果新 theorem 建立：

$$
B_1\sim B_2,
$$

兩 basin 可以 merge。

如果反例顯示原先同一 family 其實分成：

$$
B_{1a},B_{1b},
$$

則 basin split。

因此 observatory 本身需要版本化：

$$
\mathcal G_R^{(0)}
\rightarrow
\mathcal G_R^{(1)}
\rightarrow
\cdots.
$$

---

# 33. 失敗不是垃圾：Escape Failure Atlas

## 33.1 為什麼要保存失敗 escape

如果研究者只保留：

$$
\text{successful escape},
$$

未來系統可能反覆嘗試同一失敗跨越。

因此要建立：

$$
\mathcal E_{\mathrm{fail}}.
$$

## 33.2 Failure type

建議分類：

- translation failure；
- semantic mismatch；
- verifier incompatibility；
- no new premise；
- same obstruction recurrence；
- new obstruction；
- budget failure；
- evaluator failure；
- representation degeneration；
- proof-state explosion。

## 33.3 高階價值

若多個 basin 的 escape 都反覆落在：

$$
O^\star,
$$

則：

$$
O^\star
$$

本身可能成為高階 confluence obstruction。

也就是：

$$
\text{escape failure}
\rightarrow
\text{new proof-space relation}.
$$

---

# 34. 從「局部盆地」到「研究地圖」

## 34.1 最終 observatory 應該顯示什麼

不是一張漂亮的 force-directed graph。

而至少應同時顯示：

1. basin；
2. basin saturation level；
3. frontier；
4. known obstructions；
5. escape attempts；
6. cross-basin traffic；
7. method／representation distribution；
8. confidence；
9. unresolved ambiguity。

## 34.2 地圖上的顏色不能冒充真值

視覺上：

> 紅色 = 飽和

只應表示：

$$
C_{\mathrm{sat}}>\tau.
$$

不能表示：

> 此路徑數學上已證明不可能。

因此 UI 必須直接顯示：

```text
SATURATION TYPE:
observational / local / regime-bounded

NOT A CLAIM OF:
falsehood / unprovability / independence
```

---

# 35. 形式命題總表

## 命題 1：局部飽和非傳播

$$
\boxed{
S_K(B)
\not\Rightarrow
S_K(V_R).
}
$$

## 命題 2：觀測全域飽和非數學全域耗盡

$$
\boxed{
\operatorname{Sat}^{R,K}_{\mathrm{global,obs}}
\not\Rightarrow
\Omega^{\mathrm{math}}\text{ exhausted}.
}
$$

## 命題 3：低 novelty 非充分條件

$$
\boxed{
\nu\downarrow
\not\Rightarrow
S_K(B)=1.
}
$$

## 命題 4：低採樣不能叫飽和

$$
\boxed{
A_k\approx0
\not\Rightarrow
\rho_k\approx0\text{ means saturation}.
}
$$

## 命題 5：成功 basin 不等於完整空間

$$
\boxed{
\operatorname{Success}(B)\uparrow
\not\Rightarrow
V_R=B.
}
$$

## 命題 6：搜尋制度改變可達空間

$$
\boxed{
R_1\neq R_2
\Rightarrow
\Omega^{\mathrm{obs}}_{R_1}
\text{ may differ from }
\Omega^{\mathrm{obs}}_{R_2}.
}
$$

## 命題 7：Escape gain 是局部研究續行決策的證據

$$
\boxed{
\Gamma_{\mathrm{esc}}>0
}
$$

支持從原 basin 轉向新區域，但不保證新區域最終可閉合目標 theorem。

## 命題 8：多 basin recurrence 比單一文本重複更有診斷價值

若獨立方法／表示：

$$
B_i
$$

反覆匯流至同一 audited obstruction：

$$
O^\star,
$$

則：

$$
\operatorname{Robustness}(O^\star)\uparrow.
$$

但仍：

$$
O^\star
\not\Rightarrow
\text{unprovability}.
$$

---

# 36. 非主張總表

本文**不主張**：

1. proof space 在數學本體上天然具有唯一 basin decomposition；
2. graph conductance 是證明空間的唯一正確幾何；
3. embedding community 等於數學等價類；
4. 局部 novelty 下降就是 saturation；
5. 多階 recurrence 就代表接近真理；
6. basin escape 一定比加算力有效；
7. 多模型共識等於數學真理；
8. NS-203 已耗盡 Navier--Stokes 研究空間；
9. NS-203 證明 Clay 問題 framing 有錯；
10. P/NP 或 NS 必然不可判定；
11. regime-bounded saturation 可推出 Gödel 式獨立性；
12. 目前 AI 智能足以列舉所有重要表示；
13. frontier 為空表示沒有未知區域；
14. 新 representation 一定更好；
15. 研究地圖可以取代 theorem-level verification。

---

# 37. 與前四篇的整合

LSI-PSD-01 建立：

$$
\text{search regime}
\neq
\text{mathematical reality}.
$$

LSI-PSD-02 建立：

$$
I_N
=
\text{proof-space coverage functional}.
$$

LSI-PSD-03 要求先在：

$$
\Omega/\sim
$$

上去除表面重複。

LSI-PSD-04 再把採樣分成：

$$
\Omega^{(0)},
\Omega^{(1)},
\Omega^{(2)},
\ldots.
$$

本文進一步指出：

> 即使每個階都能計量，也不能假設整個空間均勻被採樣。

因此：

$$
I_k
$$

必須分解成 basin-conditioned quantities：

$$
I_k
=
\sum_i
I_{k,i}
+
I_{k,\mathfrak F}.
$$

更一般地，若 basin overlap：

$$
I_k
$$

需要 inclusion--exclusion 或 probabilistic cover correction。

所以真正成熟的 proof-space integration 不只是：

$$
\Delta I_k(N).
$$

而是：

$$
\boxed{
\Delta I_k(B_i,N)
}
$$

與：

$$
\boxed{
\Delta I_k(\mathfrak F,N).
}
$$

---

# 38. 一個更完整的動力圖像

研究開始時：

$$
\mathfrak F
\gg
B_i.
$$

大量區域尚未展開。

中期：

$$
B_1,B_2,\ldots
$$

逐漸形成。

某些 basin：

$$
\rho_k>0
$$

仍有高產量。

後期局部：

$$
\rho_k(B_1)\rightarrow0.
$$

若系統沒有 meta-control，就會：

$$
B_1\rightarrow B_1\rightarrow B_1.
$$

如果有：

$$
\Pi_{\mathrm{meta}},
$$

則：

$$
B_1
\xrightarrow{\mathrm{escape}}
B_j
$$

或：

$$
B_1
\rightarrow
\mathfrak F.
$$

於是長程研究不再是一條：

$$
\text{linear paper sequence},
$$

而是一個：

$$
\boxed{
\text{basin formation--saturation--escape--renewal process}.
}
$$

---

# 39. 對 AI 海戰術的修正

## 39.1 單純增加 agent 數量會遇到 basin crowding

若：

$$
n\rightarrow10^4
$$

但所有 agent 都在：

$$
B_1,
$$

那麼新增算力可能主要提高：

$$
\text{sampling density},
$$

不是：

$$
\text{coverage breadth}.
$$

## 39.2 真正需要的是 basin allocation

設：

$$
n_i
$$

為分配到 basin $B_i$ 的 agent 數。

應解：

$$
\max_{\{n_i\}}
\sum_i
\mathbb E[
U_i(n_i)
]
$$

subject to：

$$
\sum_i n_i=N.
$$

其中：

$$
U_i
$$

不是 paper count，而是 audited novelty utility。

## 39.3 自適應 allocation

若：

$$
\rho(B_i)\downarrow,
$$

則：

$$
n_i\downarrow.
$$

若：

$$
\Gamma_{\mathrm{esc}}(B_i,a)>0,
$$

則增加對新 basin 的 allocation。

這才是真正的：

$$
\boxed{
\text{proof-space resource scheduling}.
}
$$

---

# 40. 與未來第 6 篇的接口：障礙匯流

本文主要回答：

> 哪裡在局部飽和？

下一篇將集中問：

> 為什麼不同 basin／route 最後會撞上同一 obstruction？

如果：

$$
B_1\rightarrow O,
$$

$$
B_2\rightarrow O,
$$

$$
B_3\rightarrow O,
$$

則：

$$
O
$$

不再只是某條 proof 的局部失敗。

它可能是：

$$
\boxed{
\text{cross-basin confluence hub}.
}
$$

因此 LSI-PSD-06 將建立：

- obstruction canonicalization；
- weighted confluence；
- route-family convergence；
- obstruction inheritance；
- no-go region；
- escape obstruction；
- confluence graph。

這會把本文的 basin map 進一步變成 obstruction map。

---

# 41. 結論

長程 AI 數學研究最容易產生的一個錯覺是：

> 我已經研究這個問題非常久，所以我大概已經看完這個問題。

本文的核心工作就是拆掉這個推論。

在一個巨大的 proof space 中，研究可以非常深入地探索某個局部區域：

$$
B.
$$

系統可以在其中生成上百篇論文、數千個 lemma、反覆形成二階、三階與更高階 relation，甚至建立 all-order no-go family。

這只足以支持：

$$
\boxed{
\text{this basin is highly explored}.
}
$$

若 audited yield 同時長期下降，可以進一步支持：

$$
\boxed{
\text{this basin is operationally locally saturated}.
}
$$

但仍不能推出：

$$
\boxed{
\text{the proof space is globally exhausted}.
}
$$

更不能推出：

$$
\boxed{
\text{the mathematical problem is wrong}.
}
$$

因此成熟的 AI 研究系統不應只追求：

$$
\text{more generations}.
$$

也不應只追求：

$$
\text{more compute}.
$$

它必須知道：

$$
\boxed{
\text{where it has been,
where it keeps returning,
where novelty is dying,
and what has never been seriously tried}.
}
$$

真正的長程研究控制迴路應是：

$$
\boxed{
\text{sample}
\rightarrow
\text{quotient}
\rightarrow
\text{map}
\rightarrow
\text{detect basin}
\rightarrow
\text{measure local yield}
\rightarrow
\text{escape}
\rightarrow
\text{audit renewal}.
}
$$

從這個角度看，proof-space saturation 不是一個「最後宣布失敗」的詞。

它是一個路由訊號。

它告訴研究系統：

> 這裡可能已經看得夠深了；下一個問題不是再多走一百次，而是確認世界是否還有別的入口。

這也構成本文最終命題：

$$
\boxed{
\textbf{A mature proof-search system must distinguish depth within a basin from breadth across proof space.}
}
$$

以及其認識論底線：

$$
\boxed{
\textbf{Local saturation is a property of an observed research region, not a verdict on mathematical reality.}
}
$$

---

# 參考文獻

1. Yin, D., & Gao, J. (2025). **Generating Millions Of Lean Theorems With Proofs By Exploring State Transition Graphs.** arXiv:2503.04772. https://arxiv.org/abs/2503.04772

2. George, R. J., Huang, S., Song, P., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925. https://arxiv.org/abs/2502.17925

3. Xin, R. et al. (2025). **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving.** arXiv:2502.03438. https://arxiv.org/abs/2502.03438

4. Wang, A. et al. (2025). **Don't Get Lost in the Trees: Streamlining LLM Reasoning by Overcoming Tree Search Exploration Pitfalls.** arXiv:2502.11183. https://arxiv.org/abs/2502.11183

5. Lu, H., Wang, W., & Liu, J. (2026). **FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization.** arXiv:2603.19828. https://arxiv.org/abs/2603.19828

6. Gao, G. et al. (2026). **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137. https://arxiv.org/abs/2605.13137

7. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468. https://arxiv.org/abs/2606.06468

8. Akbudak, B. S., Ulusan, Z. A., Erer, C. S., & Şahin, G. G. (2026). **TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs.** arXiv:2607.11258. https://arxiv.org/abs/2607.11258

9. Kung, P. N. et al. (2026). **LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks.** arXiv:2606.03303. https://arxiv.org/abs/2606.03303

10. Zhang, Y. et al. (2026). **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** arXiv:2606.05400. https://arxiv.org/abs/2606.05400

11. Kurgan, S. et al. (2026). **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363. https://arxiv.org/abs/2606.25363

12. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 研究問題 |
| $R$ | 搜尋制度 / research regime |
| $\Omega_R^{\mathrm{obs}}(Q)$ | 在 $R$ 下實際可觀測研究空間 |
| $\Omega^{\mathrm{math}}(Q)$ | 理想化的底層數學證明空間；本文不假定可直接觀測 |
| $\mathcal G_R(Q)$ | quotient 後的加權 typed research graph |
| $B$ | 操作性 proof basin |
| $\phi(B)$ | basin conductance |
| $R_W(B)$ | 固定窗口 recurrence density |
| $A_k(B;N,W)$ | 第 $k$ 階嘗試數 |
| $U_k(B;N,W)$ | 第 $k$ 階新 audited equivalence classes |
| $\rho_k(B;N,W)$ | 第 $k$ 階 audited yield |
| $S_K(B)$ | $K$ 階局部飽和標記 |
| $\mathfrak F_R(N)$ | 觀測 frontier |
| $\Gamma_{\mathrm{esc},k}$ | 第 $k$ 階 basin escape gain |
| $H_B$ | basin allocation entropy |
| $H_M$ | method-family entropy |
| $C_{\mathrm{sat}}$ | saturation confidence |
| $\mathbf T$ | cross-basin traffic matrix |
| $O_{ij}$ | basin overlap |
| $\Pi_{\mathrm{meta}}$ | meta-level research routing controller |

---

## 附錄 B：最小實驗矩陣

| 實驗 | 控制變數 | Intervention | 主要指標 |
|---|---|---|---|
| Basin Escape | model / theorem set | representation / method switch | $\Gamma_{\mathrm{esc}}$ |
| Retrieval Lock | prover / budget | local vs global premise | $\rho_k$, success |
| Resource Escalation | method / representation | budget multipliers | $\rho_k(\mathcal B)$ |
| Model Agreement | theorem set / tools | model family | basin alignment |
| Evaluator Sensitivity | generator / corpus | evaluator | basin robustness |
| History Fork | checkpoint | different route policy | basin divergence |
| NS-203 Audit | corpus | theorem-level canonicalization | precision / recall / F1 |

---

## 附錄 C：Observatory 判定流程

```text
INPUT:
  problem Q
  regime R
  research history H

1. Normalize artifacts
2. Build semantic quotient
3. Extract typed route graph
4. Generate candidate basins
5. Audit basin membership
6. Measure:
   - recurrence
   - conductance
   - order-conditioned novelty
   - audited yield
7. If local saturation candidate:
   trigger escape interventions
8. Recompute yield
9. Store success/failure trace
10. Update basin map
11. Never convert observational saturation
    into a theorem about mathematical reality
```

---

## 附錄 D：一句話版本

$$
\boxed{
\text{在一口井裡挖到一萬公尺深，不代表你已經走遍整個地表。}
$$

對長程 AI 數學研究而言：

$$
\boxed{
\text{depth within a proof basin}
\neq
\text{breadth across proof space}.
}
$$


<!-- END LSI-PSD-05 -->

---


<!-- BEGIN LSI-PSD-06 -->

# LSI-PSD-06 — 障礙匯流與研究路由：當不同方法反覆撞上同一堵牆

## Obstruction Confluence and Research Routing: When Independent Proof Routes Repeatedly Hit the Same Barrier

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 06  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Obstruction-Confluence and Routing Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文將 obstruction、confluence、no-go region、route inheritance 與 barrier robustness 定義為長程 AI 數學研究的可觀測方法論物件。除非另有嚴格定理，本文不把「多條研究路線反覆遇到同一障礙」等同於該障礙在底層數學中具有絕對必然性，也不把 route confluence 等同於不可證性、獨立性、命題為假、問題範疇錯誤或任何特定未解問題的最終判決。本文研究的是**搜尋制度內的障礙證據如何累積、去重、交叉驗證與觸發研究路由改變**。

---

## 摘要

在單次 theorem proving 中，一次失敗通常只是一個局部事件：某個 tactic 不適用、某個 lemma 缺失、某個 goal 未關閉、某個編譯器回報 type mismatch。然而在長程 AI 數學研究中，同類失敗可能跨越數十、數百甚至更多 artifact 被反覆重建。更重要的是，表面上彼此獨立的研究方法可能經過不同表示、不同引理鏈、不同尺度與不同 decomposition，最終反覆命中同一類不可閉合節點。這時候，失敗不再只是：

$$
r_i\rightarrow\bot,
$$

而可能形成：

$$
r_1\rightarrow O,
\qquad
r_2\rightarrow O,
\qquad
\ldots,
\qquad
r_m\rightarrow O,
$$

其中 $O$ 是一個經過 canonicalization 與 audit 的 obstruction class。

本文建立「障礙匯流」的操作性理論。核心主張是：長程 AI 研究應把 obstruction 從臨時錯誤訊息提升成一等研究物件，建立 canonical obstruction ID、assumption profile、route provenance、first-hit time、revisit count、cross-basin support、repair history、escape history 與 audit status。只有如此，系統才可能分辨：

$$
\text{same textual failure}
$$

與：

$$
\text{same mathematical obstruction},
$$

也才能避免把同一堵牆換十種語言重新撞十次。

本文定義 weighted confluence：

$$
C_w(O)
=
\sum_{r\in\mathcal R(O)}
\omega(r,O),
$$

但進一步指出 raw route count 會被「同源路線複製」嚴重灌水，因此提出 independence-corrected confluence：

$$
C_{\mathrm{ind}}(O),
$$

其權重依賴 route genealogy、representation distance、method-family distance、premise overlap 與 shared-memory overlap。兩條只有 prompt 改寫不同的路線，不應與兩條由不同方法族、不同形式化、不同模型與不同前提集合獨立命中同一障礙的路線等價計分。

本文進一步區分至少六種 obstruction：

1. local formal obstruction；
2. missing-premise obstruction；
3. representation obstruction；
4. method-family obstruction；
5. resource obstruction；
6. statement／framing obstruction candidate。

其中最後一類只能是**候選診斷**，除非存在形式 counterexample、inconsistency、faithfulness audit 或更強的重新表述定理，不得從失敗頻率推得「原問題問錯了」。

2026 年 formal theorem proving 的若干系統已經出現與本文高度相鄰的工程訊號。APRIL 把 260,000 組 Lean proof failure、compiler diagnostic、repair 與 explanation 對齊成 supervised data；Mechanic 以 sorry-driven decomposition 保留已驗證區段並隔離 unresolved subgoal；Goedel-Architect 要求失敗 lemma 回傳 structured diagnosis、forensic trace 與 suggested fix，再用於 blueprint refinement；LeanMarathon 把長程 formalization 的 goal drift、dependency tangle 與 local repair contamination 視為系統級問題；2026 的 Lean benchmark audit 進一步指出，kernel-verified proof 也不能保證 formal statement faithful 地代表原始意圖，並辨識出 counterexample、vacuity、missing hypothesis 與 specification hazard 等缺陷。這些工作共同顯示：**失敗、錯誤、診斷與 proof graph 結構已逐漸從邊角 log 轉成 theorem-proving 系統的核心資料。**

本文最後將這套框架接回 NS-203 corpus。既有 observatory 已觀察到大量 recurrence、no-go、confluence 與高階採樣，但目前最合理的使用方式不是宣布 Navier--Stokes 存在某個「終極障礙」，而是建立 obstruction canonicalization pipeline，測試不同 series 是否真的在 assumption-normalized 意義下反覆命中同一 $O$。若未來能得到跨方法、跨表示、跨模型與跨 basin 的高獨立性 confluence，則應提高：

$$
\operatorname{Priority}(\text{obstruction-focused research}),
$$

而不是直接提高：

$$
P(\text{unprovable}).
$$

本文由此提出一個核心原則：

$$
\boxed{
\textbf{Repeated failure becomes scientific information only after the failure itself is canonicalized, audited, and genealogically de-duplicated.}
}
$$

**關鍵詞：** obstruction、confluence、proof route、research routing、canonical obstruction ID、no-go、proof repair、failure diagnosis、route genealogy、weighted confluence、independence correction、AI theorem proving、proof-space observatory

---

# 1. 問題的提出：失敗到底是不是資訊？

## 1.1 單次失敗通常資訊很少

設：

$$
Q
$$

是一個目標 theorem。

某條 proof route：

$$
r_1
$$

失敗：

$$
r_1(Q)\rightarrow\bot.
$$

從單次失敗本身，我們通常不知道：

- theorem 是假；
- tactic 選錯；
- premise 缺失；
- proof 太長；
- representation 不適合；
- model 不夠強；
- budget 不夠；
- formalization 有錯；
- verifier error；
- theorem statement 有缺陷；
- 或只是 implementation bug。

因此：

$$
\boxed{
\text{one failure}
\approx
\text{low-information event}.
}
$$

## 1.2 長程研究改變了問題

如果：

$$
r_1,r_2,\ldots,r_m
$$

表面上不同，

卻都停在同一個局部缺口：

$$
O,
$$

研究者開始獲得額外資訊。

例如：

$$
r_{\mathrm{energy}}\rightarrow O,
$$

$$
r_{\mathrm{compactness}}\rightarrow O,
$$

$$
r_{\mathrm{recurrence}}\rightarrow O,
$$

$$
r_{\mathrm{geometric}}\rightarrow O.
$$

這時候新的研究問題不再只是：

> 怎麼證 $Q$？

而變成：

> 為什麼這些方法都要經過 $O$？

這就是 obstruction confluence。

## 1.3 但「看起來一樣」非常危險

兩個失敗文字：

> 無法控制剩餘項。

可能指：

$$
E_1
$$

與：

$$
E_2
$$

兩個完全不同的剩餘項。

相反地，兩個完全不同的自然語言描述，也可能在形式化後是同一個未閉合條件。

所以必須區分：

$$
\text{textual recurrence}
$$

與：

$$
\text{mathematical obstruction recurrence}.
$$

本文的全部工作，就是把這個區分工程化。

---

# 2. 從 error log 到 obstruction object

## 2.1 Error 不等於 obstruction

定義：

$$
e
=
\text{某次具體錯誤事件}.
$$

例如 Lean compiler：

```text
type mismatch
unsolved goals
unknown constant
failed to synthesize instance
```

這些首先只是：

$$
\text{formal error event}.
$$

只有當多個 error event 被映射到一個穩定數學缺口：

$$
e_1,e_2,\ldots,e_k
\mapsto
O,
$$

才能形成 obstruction candidate。

## 2.2 Obstruction 的最小表示

本文建議 obstruction 至少表示成：

$$
O
=
(
D,
A,
G,
M,
R,
S
),
$$

其中：

- $D$：domain；
- $A$：normalized assumptions；
- $G$：unclosed goal／gap；
- $M$：mechanism of failure；
- $R$：repair history；
- $S$：status。

例如：

```yaml
obstruction_id: O-0042
domain: PDE
assumptions:
  - critical_scaling
  - bounded_energy
gap:
  type: uncontrolled_term
  normalized_statement: ...
mechanism:
  - estimate_closes_only_subcritical
repair_history:
  - interpolation_attempt
  - compactness_attempt
status:
  - audited_candidate
```

## 2.3 Obstruction 必須帶 assumptions

同一個結論缺口：

$$
G
$$

在不同假設下可能是不同 obstruction。

因此不能只存：

$$
O=G.
$$

更正確是：

$$
O=(A,G).
$$

如果：

$$
A_1\neq A_2,
$$

則：

$$
O_1
$$

與：

$$
O_2
$$

不能自動合併。

---

# 3. Canonical Obstruction ID

## 3.1 為什麼需要 ID

長程 corpus 中，如果每篇論文都重新寫：

- residual gap；
- closure defect；
- uncontrolled supplier；
- missing rigidity；
- pressure mismatch；

而沒有 canonical ID，

系統會失去：

$$
\text{cross-paper memory}.
$$

於是同一 obstruction 每次都像第一次發現。

## 3.2 Canonicalization pipeline

本文提出：

$$
e
\rightarrow
O_{\mathrm{raw}}
\rightarrow
O_{\mathrm{norm}}
\rightarrow
[O].
$$

步驟：

1. error extraction；
2. mathematical gap extraction；
3. assumption normalization；
4. notation normalization；
5. dependency normalization；
6. semantic equivalence audit；
7. canonical ID assignment。

## 3.3 不允許自動過度合併

若：

$$
\operatorname{sim}(O_i,O_j)>\tau,
$$

只能產生：

$$
\text{merge candidate}.
$$

不能直接：

$$
O_i=O_j.
$$

因為錯誤合併會製造假的 confluence。

---

# 4. Obstruction equivalence

## 4.1 強等價

若存在形式證明：

$$
A_i\vdash G_i\leftrightarrow G_j,
$$

且 assumptions 已對齊，

則可標記：

$$
O_i\equiv O_j.
$$

## 4.2 弱等價

若缺乏形式證明，但 theorem-level audit 顯示：

- 同一 normalized gap；
- 同一 dependency boundary；
- 同一 repair requirement；

可標：

$$
O_i\approx O_j.
$$

## 4.3 僅相似

若只有 embedding／lexical similarity：

$$
O_i\sim_{\mathrm{text}} O_j,
$$

不得合併。

## 4.4 Equivalence confidence

定義：

$$
c_{\mathrm{eq}}(O_i,O_j)\in[0,1].
$$

來源包括：

- formal equivalence；
- human audit；
- independent model audit；
- proof dependency equivalence；
- counterexample agreement。

---

# 5. Route：什麼才算一條不同的研究路線

## 5.1 Route 不是 paper

一篇 paper 可能包含：

$$
r_1,r_2,\ldots,r_k.
$$

反過來，同一 route 可以跨多篇 paper 延續。

所以：

$$
\boxed{
\text{artifact count}
\neq
\text{route count}.
}
$$

## 5.2 Route representation

令：

$$
r
=
(
L,
P,
M,
X,
H
),
$$

其中：

- $L$：representation language；
- $P$：premise set；
- $M$：method family；
- $X$：intermediate proof-state sequence；
- $H$：research genealogy。

## 5.3 Route endpoint

若 route 成功：

$$
r\rightarrow\operatorname{Proof}(Q).
$$

若失敗：

$$
r\rightarrow O.
$$

若未知：

$$
r\rightarrow ?.
$$

---

# 6. Confluence：不同路線匯流到同一 obstruction

## 6.1 Raw confluence count

對 obstruction $O$：

$$
\mathcal R(O)
=
\{
r:r\rightarrow O
\}.
$$

最簡單：

$$
C_{\mathrm{raw}}(O)
=
|\mathcal R(O)|.
$$

## 6.2 Raw count 的問題

若研究者把同一 prompt 改十個詞，

生成十條幾乎相同 route：

$$
r_1\approx r_2\approx\cdots\approx r_{10},
$$

則：

$$
C_{\mathrm{raw}}=10
$$

會嚴重誇大證據。

## 6.3 Independence-corrected confluence

定義兩 route 的相依程度：

$$
d_{\mathrm{dep}}(r_i,r_j)\in[0,1],
$$

其中高值表示高度共享：

- 方法；
- premise；
- memory；
- model；
- representation；
- ancestor route。

令 route 新穎權重：

$$
\omega_i
=
\frac{1}{
1+
\sum_{j<i}d_{\mathrm{dep}}(r_i,r_j)
}.
$$

則：

$$
\boxed{
C_{\mathrm{ind}}(O)
=
\sum_{r_i\in\mathcal R(O)}
\omega_i.
}
$$

這不是唯一正確公式，而是一個可審計起點。

---

# 7. Route genealogy

## 7.1 為什麼 genealogy 比 model count 重要

兩個不同模型：

$$
M_1,M_2
$$

若都讀同一份 handoff、同一份 prior proof、同一組 lemma，

它們並不真正獨立。

所以：

$$
\text{different model}
\not\Rightarrow
\text{independent route}.
$$

## 7.2 Genealogy graph

建立：

$$
G_{\mathrm{route}}
=
(V_{\mathrm{route}},E_{\mathrm{ancestor}}).
$$

若：

$$
r_j
$$

直接引用：

$$
r_i,
$$

則：

$$
r_i\rightarrow r_j.
$$

## 7.3 Independent root

若兩條 route：

$$
r_a,r_b
$$

在 ancestor graph 中共享的最近公共祖先很早，

且中間 method／representation 分叉明顯，

則 independence 較高。

---

# 8. Representation distance

## 8.1 同一 obstruction 跨表示出現更有資訊

若：

$$
\mathcal L_1\neq\mathcal L_2
$$

而兩條 route 經 audit 都命中：

$$
O,
$$

其 confluence 證據通常比純同語言重訪強。

## 8.2 表示距離

定義：

$$
d_L(r_i,r_j)
$$

可以參考：

- notation；
- coordinate system；
- state variables；
- theorem encoding；
- proof assistant；
- symbolic vocabulary。

## 8.3 但 representation diversity 也可能是假

如果只是：

$$
x\mapsto y
$$

的機械改名，

則：

$$
d_L
$$

應接近零。

所以 representation distance 不能只看 token。

---

# 9. Method-family distance

## 9.1 方法族

例如：

$$
\mathcal M
=
\{
\text{energy},
\text{compactness},
\text{combinatorial},
\text{topological},
\text{probabilistic},
\text{algebraic}
\}.
$$

## 9.2 方法匯流

若：

$$
r_{\mathrm{energy}}\rightarrow O,
$$

$$
r_{\mathrm{topology}}\rightarrow O,
$$

$$
r_{\mathrm{compactness}}\rightarrow O,
$$

則：

$$
C_{\mathrm{method}}(O)
$$

上升。

## 9.3 方法族名稱不夠

同一篇路線可能是 hybrid：

$$
M(r)
=
(
0.5\ \text{energy},
0.3\ \text{compactness},
0.2\ \text{geometry}
).
$$

因此方法距離可寫：

$$
d_M(r_i,r_j)
=
1-
\operatorname{sim}(M(r_i),M(r_j)).
$$

---

# 10. Premise overlap

## 10.1 共享 premise 會降低獨立性

兩條 route 如果使用：

$$
P_i\approx P_j,
$$

則命中同一 obstruction 不一定令人驚訝。

## 10.2 Jaccard 型指標

令：

$$
J_P(r_i,r_j)
=
\frac{
|P_i\cap P_j|
}{
|P_i\cup P_j|
}.
$$

高：

$$
J_P
$$

表示 premise 高重疊。

## 10.3 Global premise 的意義

LeanSearch v2 類工作提醒：

> 單步最相關 premise 與整個 theorem 需要的 global premise set 是不同問題。

因此某個 obstruction 可能不是 theorem 本身的深障礙，

而只是：

$$
\boxed{
\text{premise omission}.
}
$$

這種 obstruction 應該被單獨分類。

---

# 11. Obstruction taxonomy I：Local Formal Obstruction

## 11.1 定義

例如：

- type mismatch；
- unsolved goal；
- coercion mismatch；
- instance synthesis failure；
- unavailable theorem。

## 11.2 特性

它通常：

$$
\text{local},
$$

$$
\text{repairable},
$$

$$
\text{highly verifier-specific}.
$$

## 11.3 不應過度哲學化

如果 obstruction 只是：

> 少 import 一個 namespace。

那就不要把它升級成：

> 數學表示語言的本體危機。

這是 observatory 必須具備的克制。

---

# 12. Obstruction taxonomy II：Missing-Premise Obstruction

## 12.1 定義

目標可能可證，

但當前 route 缺少：

$$
p^\star.
$$

所以：

$$
P_{\mathrm{current}}
\not\vdash Q,
$$

但：

$$
P_{\mathrm{current}}\cup\{p^\star\}
\vdash Q.
$$

## 12.2 診斷方式

- global retrieval；
- theorem dependency search；
- library search；
- human premise injection。

## 12.3 Repair 後應降級

如果加入：

$$
p^\star
$$

後 obstruction 消失，

則：

$$
O
$$

不應繼續被記成高階 barrier。

它應標記：

$$
\text{resolved premise obstruction}.
$$

---

# 13. Obstruction taxonomy III：Representation Obstruction

## 13.1 定義

同一 mathematical target：

$$
Q
$$

在表示：

$$
L_1
$$

下難以閉合，

但在：

$$
L_2
$$

下可解。

## 13.2 判定

若：

$$
\operatorname{Cost}(Q\mid L_1)\gg
\operatorname{Cost}(Q\mid L_2),
$$

且 semantic faithfulness 已確認，

則可標：

$$
O_{\mathrm{repr}}.
$$

## 13.3 不能把 representation difficulty 當 theorem difficulty

這是長程 AI proof search 特別容易犯的錯。

---

# 14. Obstruction taxonomy IV：Method-Family Obstruction

## 14.1 定義

一整個方法族：

$$
\mathcal M_a
$$

在特定 assumptions 下反覆碰到：

$$
O.
$$

## 14.2 Family-level no-go candidate

若對多個 route：

$$
r\in\mathcal M_a
$$

有：

$$
r\rightarrow O,
$$

可標：

$$
\operatorname{NoGoCandidate}(\mathcal M_a,O).
$$

## 14.3 仍需明確量詞

不能從有限樣本：

$$
r_1,\ldots,r_m
$$

直接寫：

$$
\forall r\in\mathcal M_a,\ r\rightarrow O.
$$

除非真的有 theorem。

---

# 15. Obstruction taxonomy V：Resource Obstruction

## 15.1 定義

存在 route：

$$
r^\star
$$

但：

$$
C(r^\star)>\mathcal B.
$$

## 15.2 表面特徵

- progress 緩慢；
- context 超長；
- repeated partial closure；
- same residual gap；
- timeout；
- token exhaustion。

## 15.3 診斷

做：

$$
\mathcal B\rightarrow c\mathcal B.
$$

若 obstruction 消失，

則應重新分類。

---

# 16. Obstruction taxonomy VI：Statement / Framing Obstruction Candidate

## 16.1 最危險的一類

當多條高獨立性 route 都在同一 statement boundary 卡住，

研究者可能懷疑：

$$
\text{statement itself}.
$$

## 16.2 但頻率不能證明 statement 錯

必須保持：

$$
\boxed{
C_{\mathrm{ind}}(O)\uparrow
\not\Rightarrow
\operatorname{False}(Q).
}
$$

也不能推出：

$$
\operatorname{Misframed}(Q).
$$

## 16.3 什麼證據才會更強

例如：

- formal counterexample；
- inconsistent hypotheses；
- vacuity；
- missing hypothesis；
- semantic mismatch；
- quantifier error；
- domain mismatch；
- reformulation theorem。

這些才有資格把 diagnosis 往 statement 層移動。

---

# 17. APRIL：失敗資料本身可以成為訓練集

## 17.1 傳統資料偏向成功 proof

2026 年 APRIL 指出，既有 Lean datasets 幾乎都集中於正確 proof。

這使模型缺乏：

$$
\text{failure-conditioned supervision}.
$$

## 17.2 260,000 failure tuples

APRIL 建立：

$$
(\text{failed proof},
\text{compiler diagnostic},
\text{repair},
\text{explanation})
$$

的對齊資料。

## 17.3 對本文的意義

這支持一個工程事實：

$$
\boxed{
\text{failed proof traces can be reusable learning objects}.
}
$$

本文只是再向上提升一階：

$$
\text{local failure tuple}
\rightarrow
\text{cross-route obstruction class}.
$$

---

# 18. Mechanic：不要把整條失敗路線丟掉

## 18.1 兩種傳統修復

Mechanic 指出常見方法：

1. 全部重生成；
2. 在原 proof 上不斷 patch。

第一種浪費已正確部分。

第二種會讓 context 越來越長。

## 18.2 Sorry-driven decomposition

Mechanic 用：

$$
\texttt{sorry}
$$

隔離 unresolved subgoal，

保留已 verified proof structure。

## 18.3 對 obstruction observatory 的啟發

每個 unresolved subgoal 可以成為：

$$
O_{\mathrm{local}}.
$$

而不是把整篇 proof 標：

$$
\text{failed}.
$$

這使 failure localization 成為可能。

---

# 19. Goedel-Architect：structured post-mortem 已經出現

## 19.1 失敗不只回傳「沒證出來」

Goedel-Architect 在 prover 放棄 lemma 時，要求 structured diagnosis：

- tried what；
- stalled where；
- gap hypothesis；
- suggested fix。

## 19.2 Blueprint refinement

失敗 trace 會回寫：

$$
\text{dependency graph}.
$$

修正：

- hard lemma decomposition；
- dependency rewiring；
- false statement repair；
- node drop。

## 19.3 與本文的關係

這非常接近：

$$
r\rightarrow O
\rightarrow
\operatorname{RouteUpdate}(G).
$$

也就是 obstruction 不再是終點，

而是：

$$
\boxed{
\text{research routing signal}.
}
$$

---

# 20. LeanMarathon：長程研究的失敗是系統級的

## 20.1 失敗不只在 hard lemma

LeanMarathon 指出 research-level formalization 的問題包括：

- statement drift；
- dependency tangle；
- context decay；
- local repair corrupting distant work。

## 20.2 Goal drift

系統可能得到一張 formally correct graph，

但其實已離開原始 theorem。

因此：

$$
\text{formal closure}
\not\Rightarrow
\text{target fidelity}.
$$

## 20.3 Obstruction observatory 必須保存 target fidelity

所以 $O$ 的 metadata 應包含：

$$
F_T(O)
=
\text{target fidelity status}.
$$

否則系統可能「解掉」一個 obstruction，

只是因為偷偷改了問題。

---

# 21. Benchmark defects：形式驗證不等於語義無錯

## 21.1 2026 benchmark audit 的警告

近期 Lean benchmark audit 在多個 benchmark 中發現：

- counterexample；
- vacuous theorem；
- unsound axiom；
- missing hypothesis；
- incorrect translation；
- specification hazard。

## 21.2 對本文的核心意義

如果 formal statement：

$$
Q_F
$$

與 intended statement：

$$
Q_I
$$

不一致，

那麼 obstruction 可能來自：

$$
Q_F,
$$

不是：

$$
Q_I.
$$

## 21.3 所以 obstruction 必須帶 statement fingerprint

至少：

```text
informal_target_hash
formal_target_hash
translation_version
faithfulness_audit
```

否則跨 artifact 合併 obstruction 會非常危險。

---

# 22. Local success, global failure：Grasshopper case 的啟發

## 22.1 局部 lemma 都能成功

2026 的 Grasshopper formalization case 顯示，AI 可以證明多個 helper lemmas，

但主 theorem 仍卡在 global counting step。

## 22.2 這是一個乾淨的 obstruction 例子

形式：

$$
L_1,L_2,L_3,L_4
$$

皆 verified，

但：

$$
L_1\land L_2\land L_3\land L_4
\not\Rightarrow
Q
$$

因為缺：

$$
O_{\mathrm{global}}.
$$

## 22.3 對長程研究的重要性

系統如果只統計：

$$
\text{verified lemma count},
$$

會高估整體進展。

所以 obstruction graph 必須和 achievement graph 同時存在。

---

# 23. Obstruction graph

## 23.1 節點

令：

$$
V_O
=
\{O_1,\ldots,O_n\}.
$$

## 23.2 邊

可定義：

- implies；
- refines；
- transforms；
- inherits；
- co-occurs；
- escapes-to；
- resolves；
- revives。

例如：

$$
O_1\rightarrow O_2
$$

表示修掉 $O_1$ 後暴露 $O_2$。

## 23.3 這不是單純 failure list

真正的 obstruction graph 記錄：

$$
\boxed{
\text{structure of failure transitions}.
}
$$

---

# 24. Obstruction inheritance

## 24.1 子路線繼承父路線的障礙

若：

$$
r_2
$$

直接基於：

$$
r_1,
$$

而未改變產生 $O$ 的核心 assumptions，

則：

$$
r_2\rightarrow O
$$

不能被當成完全新證據。

## 24.2 Inheritance coefficient

定義：

$$
h(r_2\leftarrow r_1,O)\in[0,1].
$$

高值代表 obstruction 幾乎被直接繼承。

## 24.3 修正 confluence

可用：

$$
\omega(r_2,O)
=
1-
\max_{r_1\prec r_2}
h(r_2\leftarrow r_1,O).
$$

---

# 25. Obstruction revival

## 25.1 已解障礙可能在更高階回來

一階修掉：

$$
O^{(1)}.
$$

但在二階 relation 又出現：

$$
O^{(2)}.
$$

例如：

> 局部項已控制，但全域累積後重新失控。

## 25.2 Revival ID

應保存：

$$
O^{(1)}
\rightsquigarrow
O^{(2)}.
$$

不是重新建立新名字完全失去 genealogy。

## 25.3 高階採樣

這正接到 LSI-PSD-04：

$$
\Omega^{(0)}
\rightarrow
\Omega^{(1)}
\rightarrow
\Omega^{(2)}.
$$

障礙本身也可能有 order。

---

# 26. Confluence degree

## 26.1 Basin confluence

令：

$$
\mathcal B(O)
=
\{B_i:B_i\rightarrow O\}.
$$

定義：

$$
C_B(O)
=
|\mathcal B(O)|.
$$

## 26.2 Method confluence

$$
C_M(O)
=
|\mathcal M(O)|.
$$

## 26.3 Representation confluence

$$
C_L(O)
=
|\mathcal L(O)|.
$$

## 26.4 Model confluence

$$
C_A(O)
=
|\mathcal A(O)|.
$$

其中 $\mathcal A$ 此處表示 agent/model family，避免和 assumptions 混淆時可在資料結構中另命名。

## 26.5 Confluence vector

因此更合理：

$$
\boxed{
\mathbf C(O)
=
(
C_B,
C_M,
C_L,
C_A,
C_{\mathrm{ind}}
).
}
$$

而不是一個數字。

---

# 27. Weighted obstruction robustness

## 27.1 Robustness score

定義：

$$
R_O
=
f(
C_{\mathrm{ind}},
C_B,
C_M,
C_L,
A_O,
E_O
),
$$

其中：

- $A_O$：audit depth；
- $E_O$：escape resistance。

## 27.2 仍是 search-regime evidence

即使：

$$
R_O\rightarrow1,
$$

也只能表示：

> 在已觀測制度內，該 obstruction 非常穩健。

不是：

> 數學宇宙保證這是終極牆。

---

# 28. Escape obstruction

## 28.1 Escape 也可能匯流

在 LSI-PSD-05 中：

$$
B
\xrightarrow{a}
B'.
$$

如果多種 escape action：

$$
a_1,a_2,a_3
$$

最後都命中：

$$
O_{\mathrm{esc}},
$$

則這個 obstruction 比 basin 內部 obstruction 更值得注意。

## 28.2 Escape-confluence

定義：

$$
C_{\mathrm{esc}}(O)
=
|\{
a:a(B)\rightarrow O
\}|.
$$

## 28.3 例子

- 換 representation 還是卡；
- 換 method 還是卡；
- 增 budget 還是卡；
- 換 model 還是卡；
- global premise retrieval 還是卡。

這會提高：

$$
\text{framing audit priority}.
$$

但仍不等於 framing error proof。

---

# 29. No-go region

## 29.1 從單一路線 no-go 到方法區域 no-go

若有定理真的證明：

$$
\forall r\in\mathcal R_S,
\quad
r\not\Rightarrow Q,
$$

則：

$$
\mathcal R_S
$$

是一個真正的 no-go region。

## 29.2 Empirical no-go candidate

若只是大量採樣：

$$
r_1,\ldots,r_n
$$

皆失敗，

只能稱：

$$
\boxed{
\text{empirical no-go candidate}.
}
$$

## 29.3 名稱紀律

Observatory UI 必須明確區分：

```text
NO-GO STATUS:
- theorem-certified
- formally refuted route class
- empirical candidate
- heuristic warning
```

---

# 30. Obstruction entropy

## 30.1 研究失敗是否集中

令近期失敗在 obstruction class 上的分布：

$$
p_i.
$$

定義：

$$
H_O
=
-
\sum_i p_i\log p_i.
$$

## 30.2 低 entropy

如果：

$$
H_O\downarrow,
$$

表示失敗越來越集中於少數 obstruction。

這可能是：

- proof-space contraction；
- basin lock-in；
- taxonomy 過粗；
- 真正 confluence。

## 30.3 必須配合獨立性

只有：

$$
H_O\downarrow
$$

和：

$$
C_{\mathrm{ind}}\uparrow
$$

同時發生，才更支持「不同路線真正匯流」。

---

# 31. First-hit time 與 rediscovery lag

## 31.1 首次出現

對 obstruction $O$：

$$
t_0(O).
$$

## 31.2 重訪時間

$$
t_1,t_2,\ldots.
$$

## 31.3 Rediscovery lag

$$
\Delta t_i
=
t_i-t_{i-1}.
$$

## 31.4 長期趨勢

若：

$$
\Delta t_i\downarrow,
$$

可能表示研究越來越被 $O$ 吸引。

若：

$$
\Delta t_i\uparrow,
$$

可能表示 escape 成功，只有偶爾重訪。

---

# 32. Obstruction centrality

## 32.1 不是所有障礙一樣重要

某個 $O$ 只阻擋：

$$
1
$$

條 fringe route。

另一個 $O^\star$ 阻擋：

$$
50
$$

條 central routes。

## 32.2 Route-weighted centrality

定義：

$$
Z(O)
=
\sum_{r\rightarrow O}
\operatorname{Importance}(r)\omega(r,O).
$$

## 32.3 研究優先級

高：

$$
Z(O)
$$

的 obstruction 更值得：

- human audit；
- formalization；
- counterexample search；
- new-theory generation。

---

# 33. Obstruction budget allocation

## 33.1 Agent 海戰術不能平均分配

如果有：

$$
O_1,\ldots,O_n,
$$

不應每個分一樣多 agent。

## 33.2 Priority function

$$
P_O
=
g(
Z,
C_{\mathrm{ind}},
E_{\mathrm{esc}},
\text{transfer potential},
\text{verification cost}
).
$$

## 33.3 目標

最大化：

$$
\sum_O
\mathbb E[
\Delta U(O)
].
$$

不是最大化：

$$
\text{number of generated papers}.
$$

---

# 34. Repair taxonomy

## 34.1 Local patch

$$
O\rightarrow\text{patch}.
$$

## 34.2 Lemma insertion

$$
O
\rightarrow
L^\star
\rightarrow
\text{closure}.
$$

## 34.3 Dependency rewiring

$$
P_i
\rightarrow
P_j.
$$

## 34.4 Statement repair

$$
Q
\rightarrow
Q'.
$$

## 34.5 Representation switch

$$
L_1
\rightarrow
L_2.
$$

## 34.6 Method switch

$$
M_1
\rightarrow
M_2.
$$

## 34.7 Problem split

$$
Q
\rightarrow
(Q_1,Q_2,\ldots,Q_k).
$$

每次 repair 都應保留：

$$
\text{before/after obstruction state}.
$$

---

# 35. Repair success 也可能是假

## 35.1 Goal drift

如果 repair：

$$
Q\rightarrow Q'
$$

而：

$$
Q'\neq Q,
$$

proof success 可能只是逃離原問題。

## 35.2 Faithfulness gate

要求：

$$
F(Q,Q')>\tau_F.
$$

如果 statement 必須改，

則必須明示：

$$
\text{original theorem changed}.
$$

## 35.3 Obstruction resolution status

不要只標：

```text
RESOLVED
```

而要標：

```text
RESOLVED_BY:
- proof
- stronger premise
- weaker conclusion
- corrected statement
- representation change
- counterexample
```

---

# 36. NS-203：應如何真正測 confluence

## 36.1 現況

v0.1 observatory 已看到：

- recurrence 高；
- no-go 高；
- X72 有 confluence 語言；
- DCRP 出現 higher-order residue；
- 跨 series traffic 明顯。

## 36.2 目前還不能直接說同一 obstruction

因為 broad concept family：

$$
\text{carrier-supplier},
$$

$$
\text{rigidity-closure},
$$

$$
\text{obstruction-gap-defect}
$$

仍然太粗。

## 36.3 第二輪需要 theorem-level extraction

每份 artifact 抽：

$$
A_i,
C_i,
L_i,
O_i,
S_i.
$$

然後建立：

$$
O_i\approx O_j?
$$

## 36.4 Cross-series confluence test

例如：

$$
O_{\mathrm{X72}}
$$

與：

$$
O_{\mathrm{DCRP}}
$$

若 normalized assumptions 與 terminal gap 真正等價，

才算：

$$
C_B(O)\uparrow.
$$

不是因為都寫了：

> closure gap。

---

# 37. 一個 NS Obstruction Record 範例

```yaml
obstruction_id: NS-O-017
source:
  series:
    - X72
    - DCRP
first_seen: ...
assumption_profile:
  scaling: critical
  regularity: ...
  geometry: ...
normalized_gap:
  statement: ...
route_families:
  - pure_continuous
  - recurrence_shadowing
representations:
  - ...
audits:
  semantic_equivalence: pending
  theorem_level: partial
confluence:
  raw: 9
  independence_corrected: 2.8
status:
  empirical_candidate
nonclaims:
  - not_unprovability
  - not_misframing_proof
```

這比：

> 大家又卡住了。

有用得多。

---

# 38. Counterexample channel

## 38.1 Obstruction 不一定需要 repair

如果找到：

$$
x
$$

使：

$$
A(x)
$$

成立但：

$$
Q(x)
$$

不成立，

那麼：

$$
Q
$$

被反例處理。

## 38.2 Counterexample 是最高價值的 obstruction resolution 之一

它把：

$$
\text{suspected statement obstruction}
$$

升級成：

$$
\text{formal disproof}.
$$

## 38.3 搜尋策略

對高：

$$
C_{\mathrm{ind}}(O)
$$

且懷疑 statement 的節點，

系統應增加：

$$
\text{counterexample budget}.
$$

---

# 39. Formalization audit channel

## 39.1 先問是不是同一問題

如果 informal：

$$
Q_I
$$

與 formal：

$$
Q_F
$$

不一致，

則所有後續 obstruction 都可能被污染。

## 39.2 Audit trigger

當：

- counterexample 異常容易；
- theorem vacuous；
- hypothesis 太強；
- repeated trivial proof；
- proof route 與 intended mathematics 不符；

應啟動：

$$
\operatorname{Audit}(Q_I,Q_F).
$$

## 39.3 這正是防止錯誤 confluence 的必要層

多個 agent 全在錯誤 formalization 上匯流，

只能證明：

$$
\text{they share a bad target}.
$$

---

# 40. Confluence confidence levels

## Level 0：文字相似

只有 lexical overlap。

## Level 1：概念相似

同 broad obstruction family。

## Level 2：route-level recurrence

normalized gap 類似，assumptions 部分對齊。

## Level 3：cross-route audited confluence

多 route 經人工／模型稽核確認同一 obstruction。

## Level 4：cross-basin independent confluence

不同 basin／方法／representation，genealogy correction 後仍匯流。

## Level 5：theorem-backed obstruction

存在形式 theorem 證明一整類 route 必須通過或無法越過該 obstruction。

只有 Level 5 接近真正的數學 no-go 結果。

---

# 41. Confluence 不是不可證性

## 41.1 核心防火牆

$$
\boxed{
C_{\mathrm{ind}}(O)\gg1
\not\Rightarrow
Q\text{ unprovable}.
}
$$

## 41.2 原因

真正 proof：

$$
r^\star
$$

可能根本沒有經過：

$$
O.
$$

即：

$$
r^\star\notin\mathcal R_{\mathrm{observed}}.
$$

## 41.3 也不能推出獨立性

Gödel independence 需要特定形式系統中的 metamathematical proof。

大量失敗不能替代這個證明。

---

# 42. Confluence 也不是問題錯了

## 42.1 Framing anomaly hypothesis

高 confluence 可以提高：

$$
\operatorname{Priority}(\text{framing audit}).
$$

但不能提高到 certainty。

## 42.2 更強證據鏈

若：

$$
C_{\mathrm{ind}}\uparrow
$$

再加：

$$
\text{formal counterexample},
$$

或：

$$
\text{semantic inconsistency},
$$

或：

$$
\text{reformulation theorem},
$$

才可能逐步建立 stronger diagnosis。

---

# 43. Confluence 與 productive mis-specification 的接口

後續 LSI-PSD-08 會研究：

$$
\text{productive mis-specification}.
$$

本文先指出：

> 即使 parent route 最後被證明 framing 有問題，其過程中發現的 obstruction、lemma、counterexample 與 repair mechanism 仍可能獨立有價值。

因此：

$$
\text{route invalidation}
\not\Rightarrow
\text{descendant knowledge invalidation}.
$$

這是後續系列的重要接口。

---

# 44. Failure atlas

## 44.1 為什麼需要 atlas

長程 AI 系統最容易遺失的不是成功 proof。

而是：

$$
\text{why previous routes failed}.
$$

## 44.2 Atlas schema

```yaml
problem_id:
obstruction_id:
canonical_gap:
assumptions:
first_seen:
last_seen:
route_count:
independent_route_mass:
method_families:
representations:
basins:
models:
premise_sets:
repairs:
escapes:
counterexamples:
formal_status:
semantic_status:
transfer_targets:
```

## 44.3 Atlas 是 research memory

它讓下一代 agent 不必從零開始。

---

# 45. Obstruction transfer

## 45.1 障礙也可以跨問題遷移

若：

$$
O_Q
$$

與另一問題：

$$
O_{Q'}
$$

具有共同 normalized mechanism，

則：

$$
O_Q
\rightarrow
O_{Q'}
$$

可能產生 transfer。

## 45.2 Transfer value

例如：

- same compactness gap；
- same counting bottleneck；
- same coercion bug；
- same representation singularity。

## 45.3 負知識也能成為 proof asset

所以 proof asset map 不應只收成功 lemma。

也應收：

$$
\boxed{
\text{portable obstruction patterns}.
}
$$

---

# 46. Obstruction compression

## 46.1 長程 corpus 會出現大量 failure variants

如果：

$$
10^4
$$

條失敗最後 quotient 成：

$$
17
$$

個 obstruction classes，

這本身就是研究壓縮。

## 46.2 Compression ratio

定義：

$$
\kappa_O
=
\frac{
N_{\mathrm{failure\ events}}
}{
N_{\mathrm{audited\ obstruction\ classes}}
}.
$$

## 46.3 高壓縮率

若：

$$
\kappa_O\gg1,
$$

表示大量生成其實反覆命中少數 failure geometry。

這正是 logic-space integration 的一個可測面向。

---

# 47. Obstruction discovery rate

## 47.1 新 obstruction 增量

令：

$$
U_O(N,W)
$$

為固定窗口新增 audited obstruction classes。

定義：

$$
\rho_O(N,W)
=
\frac{
U_O(N,W)
}{
A_O(N,W)
},
$$

其中 $A_O$ 是 failure events。

## 47.2 與 route novelty 一起看

若：

$$
\rho_{\mathrm{route}}\downarrow,
$$

且：

$$
\rho_O\downarrow,
$$

研究可能開始高度重採樣。

若 route novelty 高但 obstruction novelty 低，

表示：

> 新路很多，但都撞同一堵牆。

這是 confluence 最漂亮的訊號之一。

---

# 48. Route-to-obstruction matrix

令：

$$
M_{ij}
=
P(O_j\mid r_i).
$$

若 deterministic audited endpoint：

$$
M_{ij}\in\{0,1\}.
$$

實際研究可用 confidence：

$$
M_{ij}\in[0,1].
$$

矩陣：

$$
\mathbf M
$$

可用來做：

- route clustering；
- obstruction clustering；
- bipartite centrality；
- confluence detection；
- escape recommendation。

---

# 49. Obstruction-conditioned routing

## 49.1 過去的路由

通常：

$$
\pi(a\mid s).
$$

## 49.2 加入 obstruction memory

改成：

$$
\pi(
a
\mid
s,
O_{\mathrm{history}},
B,
R
).
$$

## 49.3 例子

如果：

$$
O^\star
$$

已被 20 條高度相依 route 命中，

不一定要停止。

但可以降低：

$$
P(\text{same family retry}).
$$

提高：

$$
P(\text{independent route probe}).
$$

---

# 50. Meta-controller

輸入：

$$
(
C_{\mathrm{ind}},
R_O,
Z(O),
H_O,
\rho_O,
\Gamma_{\mathrm{esc}}
).
$$

輸出：

$$
\{
\text{retry},
\text{repair},
\text{decompose},
\text{switch premise},
\text{switch representation},
\text{switch method},
\text{counterexample},
\text{framing audit},
\text{stop}
\}.
$$

這樣 obstruction 才真正變成控制訊號。

---

# 51. 實驗一：Obstruction Canonicalization Benchmark

## 51.1 資料

人工建立：

$$
500
$$

對 failure snippets。

標註：

- same obstruction；
- related but distinct；
- purely lexical；
- one resolves another；
- assumption mismatch。

## 51.2 指標

$$
\text{precision},
\text{recall},
F_1.
$$

## 51.3 最重要

寧願：

$$
\text{false negative}
$$

多一點，

也要避免：

$$
\text{false merge}.
$$

因為 false merge 會直接灌大 confluence。

---

# 52. 實驗二：Genealogy Correction

## 52.1 問題

raw confluence 是否被同源 route 複製灌水？

## 52.2 設計

對同一 obstruction：

$$
O
$$

建立：

- same-model variants；
- same-memory variants；
- independent-method variants；
- independent-representation variants。

## 52.3 比較

$$
C_{\mathrm{raw}}
$$

與：

$$
C_{\mathrm{ind}}.
$$

若兩者差異巨大，證明 genealogy correction 必要。

---

# 53. 實驗三：Escape-Confluence Test

對高：

$$
R_O
$$

obstruction，

執行：

1. method switch；
2. representation switch；
3. premise globalization；
4. resource escalation；
5. model-family switch；
6. counterexample search。

若多種 escape 都重新命中：

$$
O,
$$

則：

$$
C_{\mathrm{esc}}(O)\uparrow.
$$

這是比單 basin recurrence 更強的證據。

---

# 54. 實驗四：False-Confluence Calibration

## 54.1 故意製造 taxonomy 過粗

把所有：

> estimate failure

都合併成：

$$
O_{\mathrm{estimate}}.
$$

## 54.2 再細分 assumptions

重新抽取：

$$
A_i.
$$

## 54.3 比較

若：

$$
C_{\mathrm{raw}}
$$

大幅崩解，

說明原 confluence 只是 taxonomy artifact。

這是任何 serious observatory 必做的 calibration。

---

# 55. 實驗五：NS-203 Obstruction Audit

## 55.1 抽樣

優先：

- X72；
- DCRP；
- MORP；
- FCBP；
- C5-H；
- Proof Asset Map。

## 55.2 每篇抽取

$$
A,C,L,O,S.
$$

## 55.3 建立 gold obstruction pairs

至少：

$$
200
$$

對。

## 55.4 目標

測：

$$
C_B,
C_M,
C_L,
C_{\mathrm{ind}}.
$$

而不是只數：

> confluence 出現幾次。

---

# 56. 成熟系統如何回報「我卡住了」

不應只說：

> 我證不出來。

應回報：

```text
TARGET:
  Q-001

CURRENT BASIN:
  B-07

CURRENT OBSTRUCTION:
  O-031

OBSTRUCTION CONFIDENCE:
  Level 3 / cross-route audited

ROUTE SUPPORT:
  raw routes: 18
  independence-corrected mass: 4.2

ATTEMPTED ESCAPES:
  representation switch: neutral
  global premise retrieval: failed
  budget x4: neutral
  model-family switch: pending

NON-CLAIMS:
  not a proof of falsehood
  not a proof of unprovability
  not an independence result

RECOMMENDED NEXT ACTION:
  counterexample search
  theorem-level framing audit
```

這才是真正的 research-grade failure report。

---

# 57. 與 LSI-PSD-05 的整合

第 5 篇建立：

$$
B_i
$$

與：

$$
\text{local saturation}.
$$

本文把每個 basin 內的 terminal failure 抽成：

$$
O_j.
$$

於是 proof-space map 變成 bipartite structure：

$$
B_i
\leftrightarrow
O_j.
$$

一個 basin 可有多個 obstruction；

一個 obstruction 也可跨多個 basin。

因此：

$$
\boxed{
\text{basin map}
+
\text{obstruction map}
}
$$

比單純 route graph 更能描述長程研究。

---

# 58. 與 LSI-PSD-04 的整合

高階採樣不只作用於 route。

obstruction 本身也可有：

$$
O^{(0)},
O^{(1)},
O^{(2)},\ldots.
$$

例如：

$$
O^{(0)}
=
\text{local closure failure},
$$

$$
O^{(1)}
=
\text{different closures all require same missing relation},
$$

$$
O^{(2)}
=
\text{all relation-level repairs reintroduce same global defect}.
$$

所以：

$$
\boxed{
\text{higher-order proof sampling}
}
$$

與：

$$
\boxed{
\text{higher-order obstruction confluence}
}
$$

是同一研究動力的兩面。

---

# 59. 與 Logic-Space Integration 的整合

假設 failure events：

$$
F_N.
$$

經 quotient 後形成 obstruction classes：

$$
\mathcal O_N.
$$

可以把「失敗空間積分」定義成：

$$
I_O(N)
=
\int_{\Omega_O}
c_N([O])\,d\mu_O.
$$

真正重要的是：

$$
\Delta I_O(N).
$$

如果：

$$
\Delta I_O\rightarrow0
$$

但 failure count 持續上升，

表示研究正大量重採樣既有 obstruction space。

這就是：

$$
\boxed{
\text{obstruction-space saturation candidate}.
}
$$

仍然只是 observed regime 的性質。

---

# 60. 最重要的認識論防火牆

本文提出：

$$
\boxed{
\text{Obstruction Confluence Non-Verdict Principle}
}
$$

即：

$$
\boxed{
\text{high confluence}
\not\Rightarrow
\text{mathematical verdict}.
}
$$

具體包括：

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ false},
$$

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ unprovable},
$$

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ independent},
$$

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ misframed}.
$$

它只支持：

$$
\boxed{
\text{the observed research regime repeatedly reconstructs the same audited barrier}.
}
$$

---

# 61. 非主張總表

本文不主張：

1. 所有 proof failure 都能 canonicalize 成唯一 obstruction；
2. obstruction graph 是數學實在的唯一真結構；
3. route count 可直接當獨立證據；
4. 不同模型就是獨立路線；
5. 不同符號就是不同 representation；
6. 高 confluence 等於不可證；
7. 高 confluence 等於命題為假；
8. 高 confluence 等於定義範疇錯誤；
9. empirical no-go candidate 等於 theorem-level no-go；
10. formal proof success 自動保證 informal target fidelity；
11. compiler diagnostic 自動等於數學 diagnosis；
12. NS-203 已發現 Navier--Stokes 的終極 obstruction；
13. P/NP 或其他未解問題可由 AI 失敗頻率判定；
14. obstruction 越多代表研究越差；
15. obstruction 越少代表更接近真理。

---

# 62. 形式命題總表

## 命題 1：Failure-to-obstruction separation

$$
\boxed{
e_i=e_j
\not\Rightarrow
O_i=O_j.
}
$$

## 命題 2：Text-to-obstruction separation

$$
\boxed{
\operatorname{TextSim}(e_i,e_j)\uparrow
\not\Rightarrow
O_i\equiv O_j.
}
$$

## 命題 3：Route-count non-independence

$$
\boxed{
C_{\mathrm{raw}}(O)
\not\Rightarrow
C_{\mathrm{ind}}(O).
}
$$

## 命題 4：Cross-route confluence evidence

在 assumptions、target fidelity 與 obstruction equivalence 都經 audit 後，

若：

$$
C_{\mathrm{ind}}(O)\uparrow,
$$

則對：

$$
\text{observed barrier robustness}
$$

的證據增加。

## 命題 5：Confluence non-verdict

$$
\boxed{
C_{\mathrm{ind}}(O)\uparrow
\not\Rightarrow
\operatorname{Verdict}(Q).
}
$$

## 命題 6：Obstruction memory utility

若 canonical obstruction memory 能降低相同 route family 的無效重訪，

則它可提高：

$$
\text{research efficiency}.
$$

此命題可實驗檢驗。

---

# 63. 與後續第 7 篇的接口

前六篇逐步建立：

$$
\text{search regime},
$$

$$
\text{coverage},
$$

$$
\text{semantic quotient},
$$

$$
\text{higher-order sampling},
$$

$$
\text{local saturation},
$$

$$
\text{obstruction confluence}.
$$

接下來第 7 篇會問一個更反直覺的問題：

> 當研究空間被約束、壓縮與閉合後，為什麼核心真命題反而可能變得越來越像「廢話」？

也就是：

$$
\boxed{
\text{Truth--Generativity Inversion}.
}
$$

而本文提供必要前置：

> 在討論「真理變簡單」以前，我們必須先知道研究究竟是在收斂到穩健 obstruction，還是只被自己的 route genealogy 困住。

---

# 64. 結論

長程 AI 數學研究真正昂貴的，不只是證明。

也是：

$$
\boxed{
\text{忘記自己為什麼失敗。}
}
$$

如果每次 failure 都只留下：

> 沒證出來。

下一個 agent 就會重新從零開始。

如果每個 failure 都被壓成一個過粗標籤：

> closure gap。

系統又會產生假的 confluence。

因此 mature research infrastructure 必須保存：

$$
\text{where},
$$

$$
\text{under what assumptions},
$$

$$
\text{by which route},
$$

$$
\text{after which premises},
$$

$$
\text{with which representation},
$$

$$
\text{what exactly remained unclosed}.
$$

只有這時：

$$
r_1\rightarrow O,
\qquad
r_2\rightarrow O,
\qquad
r_3\rightarrow O
$$

才真正具有科學資訊。

最終，本文把「失敗」從一句負面結果改寫成一個可積累結構：

$$
\boxed{
\text{failure event}
\rightarrow
\text{canonical obstruction}
\rightarrow
\text{confluence evidence}
\rightarrow
\text{routing decision}.
}
$$

而整篇論文最重要的兩句話是：

$$
\boxed{
\textbf{A wall becomes informative only when we can show that independent roads truly meet the same wall.}
}
$$

以及：

$$
\boxed{
\textbf{Even then, the wall is evidence about our explored routes, not a verdict on all possible mathematics.}
}
$$

---

# 參考文獻

1. Wang, E., Chess, S., Lee, D., Ge, S., Mallavarapu, A., & Ilin, V. (2026). **Learning to Repair Lean Proofs from Compiler Feedback.** arXiv:2602.02990. https://arxiv.org/abs/2602.02990

2. Qiu, R., Cao, Y., Liu, J., Guo, D., Gao, X.-S., Zhi, L., & Feng, R. (2026). **Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving.** arXiv:2603.24465. https://arxiv.org/abs/2603.24465

3. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468. https://arxiv.org/abs/2606.06468

4. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., & Liu, F. (2026). **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** arXiv:2606.05400. https://arxiv.org/abs/2606.05400

5. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493. https://arxiv.org/abs/2606.29493

6. Lau, G. R. (2026). **Using Aristotle API for AI-Assisted Theorem Proving in Lean 4: A Formalisation Case Study of the Grasshopper Problem.** arXiv:2605.20120. https://arxiv.org/abs/2605.20120

7. Gao, G. et al. (2026). **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137. https://arxiv.org/abs/2605.13137

8. George, R. J., Huang, S., Song, P., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925. https://arxiv.org/abs/2502.17925

9. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 目標問題／定理 |
| $r$ | proof / research route |
| $e$ | 單次 failure event |
| $O$ | canonical obstruction |
| $\mathcal R(O)$ | 命中 $O$ 的 route 集合 |
| $C_{\mathrm{raw}}(O)$ | 原始 confluence count |
| $C_{\mathrm{ind}}(O)$ | genealogy-corrected confluence |
| $C_B(O)$ | basin confluence |
| $C_M(O)$ | method-family confluence |
| $C_L(O)$ | representation confluence |
| $C_{\mathrm{esc}}(O)$ | escape-action confluence |
| $R_O$ | obstruction robustness |
| $Z(O)$ | obstruction centrality |
| $H_O$ | obstruction entropy |
| $\rho_O$ | obstruction discovery rate |
| $\kappa_O$ | failure-event / obstruction-class compression ratio |
| $F_T$ | target fidelity status |

---

## 附錄 B：Obstruction Record 最小欄位

```yaml
obstruction_id:
problem_id:
domain:
formal_target:
informal_target:
target_fidelity:
assumptions:
normalized_gap:
mechanism:
first_seen:
last_seen:
route_ids:
route_genealogy:
method_families:
representations:
premise_sets:
basins:
models:
raw_confluence:
independent_confluence:
escape_attempts:
repair_history:
counterexample_status:
audit_status:
no_go_status:
nonclaims:
```

---

## 附錄 C：Confluence Audit Checklist

- [ ] obstruction assumptions 已 normalize
- [ ] target statement 版本一致
- [ ] formal / informal target faithfulness 已檢查
- [ ] lexical similarity 沒有被當 semantic equivalence
- [ ] route genealogy 已建立
- [ ] shared memory 已計入依賴
- [ ] shared premise 已計入依賴
- [ ] representation difference 不是單純 rename
- [ ] method-family difference 已人工抽查
- [ ] raw count 與 independence-corrected count 同時報告
- [ ] empirical no-go 沒有冒充 theorem no-go
- [ ] confluence 沒有冒充 falsehood / unprovability / independence
- [ ] escape history 已保留
- [ ] resolved obstruction 沒有繼續計入 active barrier

---

## 附錄 D：一句話版本

$$
\boxed{
\text{十條路都撞牆，不代表世界沒有第十一條路；但若十條真正獨立的路都撞同一面牆，那面牆值得被單獨研究。}
}
$$


<!-- END LSI-PSD-06 -->

---


<!-- BEGIN LSI-PSD-07 -->

# LSI-PSD-07 — 真理—生成性反轉：為什麼更精確不一定產生更多理論

## Truth–Generativity Inversion: Why Greater Fidelity Does Not Necessarily Produce More Theory

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 07  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Truth–Generativity Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文提出「真理—生成性反轉」作為一個可檢驗的研究框架，而不是一條無條件普遍定律。本文不主張「越真越沒用」「錯誤一定更有創造力」「精確定義會阻礙科學」或「錯置問題比正確問題更優越」。本文只研究一個較弱且可操作的命題：**truth/fidelity、closure、generativity、utility 與 explanatory reach 之間未必是單調同向關係。** 在某些研究域，理論越接近閉合，新增自由度與表面新奇度可能下降；而有限、受約束、可比較、可驗證的理想化或失真，可能打開大量中間問題與後代理論。這些現象必須與任意錯誤、幻覺、語義漂移與不可驗證推測嚴格區分。

---

## 摘要

科學與數學研究常隱含一個單調直覺：

$$
\text{更精確}
\Rightarrow
\text{更接近真理}
\Rightarrow
\text{產生更多知識}
\Rightarrow
\text{更有用}.
$$

本文主張，最後兩個箭頭並不普遍成立。理論的 truth/fidelity、closure、generativity 與 utility 至少應被視為不同維度。當一個問題或理論被逐步加入正確約束，其有效候選空間可能收縮：

$$
\Omega(D_0)
\supseteq
\Omega(D_1)
\supseteq
\cdots
\supseteq
\Omega(D^\star).
$$

若 $D^\star$ 高度閉合，最終有效自由度可以變得非常小：

$$
H(\Omega(D^\star))\downarrow.
$$

在極端情況，研究終點可能被壓縮成一個語義上近似同一律的核心：

$$
X=X.
$$

這並不表示前述推導過程沒有資訊；恰恰相反，資訊可能從終點命題轉移到：

$$
\text{derivational history},
$$

$$
\text{boundary conditions},
$$

$$
\text{counterfactual structure},
$$

$$
\text{mapping relations},
$$

$$
\text{application space}.
$$

因此，**核心真命題的表面資訊量下降，不等於整個理論體系的生成能力下降。**

本文進一步研究反向情況。若研究定義、模型或表示相對某個更適切目標存在有限偏差：

$$
D_\epsilon
=
D^\star+\epsilon,
$$

則這個偏差可能迫使研究者建立：

- correction term；
- boundary regime；
- exception structure；
- missing mechanism；
- alternative representation；
- asymptotic bridge；
- effective theory；
- diagnostic residual；
- transfer theorem。

由此可出現：

$$
G(D_\epsilon)
>
G(D^\star),
$$

即「稍微不閉合」的模型在中間理論生成量上反而高於完全閉合核心。然而本文拒絕把這寫成「越錯越好」；若偏差過大、不可校準或與現象失去穩定關聯，則：

$$
G_{\mathrm{useful}}(D_\epsilon)
\rightarrow0.
$$

因此本文提出一個待檢驗的 **Truth–Fidelity–Generativity Landscape**。在某些研究域，實用生成性可能對失真程度呈非單調關係：

$$
G_{\mathrm{useful}}(\epsilon)
$$

可能存在內部極值，而不是在 $\epsilon=0$ 或 $\epsilon\rightarrow\infty$ 必然最大。

這個框架與現有科學哲學和科學史有明顯接點。Batterman 與 Rice 的 minimal model 研究指出，極簡模型的解釋力可以來自顯示微觀細節對宏觀行為的不相關性，而不是最大程度複製真實系統；Spagnesi 2025 年提出，理想化模型可作為系統性比較的規範參照，模型與現象的 deviation 本身能產生新的解釋資訊；Weingarten 2026 年以 effective theories 討論 productive idealization，指出非基本理論可因適切的結構裁切而提供科學理解；Norton 對 Carnot 的歷史分析則把 caloric conservation 描述為一種「幸運的錯誤」，因為它把 Carnot 導向後來極具生產力的 reversible heat-engine framework；2026 年 LISDD 更直接把「模型在哪裡失效」轉換成「缺失機制的局部符號發現」問題。另一方面，Angkasa 2025 年對科學進步的研究指出，單純累積知識會遇到 diminishing epistemic returns 與 irrelevant knowledge proliferation。這些工作共同支持一個較弱但重要的結論：

$$
\boxed{
\text{truth-like fidelity, explanatory power, generativity, and progress are not the same coordinate.}
}
$$

本文最後把這個命題接回長程 AI 數學研究。若 NS-203 或其他 corpus 在某些 proof basin 內出現：

$$
\text{constraint increase}
\rightarrow
\text{route contraction}
\rightarrow
\text{obstruction concentration}
\rightarrow
\text{surface novelty decline},
$$

我們不能直接解讀為「越接近真理」。它也可能是局部方法飽和、表示鎖定或搜尋偏差。但如果同時存在 audited theorem cuts、independent route confluence、可驗證 descendant transfer 與 basin escape 實驗，則可以開始測量：

$$
\text{closure}
\leftrightarrow
\text{generativity}
$$

之間的實際關係。

本文由此提出兩個核心原則：

$$
\boxed{
\textbf{Greater fidelity need not imply greater generativity.}
}
$$

以及：

$$
\boxed{
\textbf{Productive deviation is valuable only when its descendants remain auditable, transferable, and truth-sensitive.}
}
$$

**關鍵詞：** 真理—生成性反轉、Truth–Generativity Inversion、idealization、minimal model、effective theory、productive error、closure、generativity、scientific understanding、model discrepancy、AI mathematics、proof-space dynamics

---

# 1. 問題的提出：我們為什麼直覺上把「更真」和「更多知識」綁在一起

## 1.1 單調知識直覺

最自然的知識模型是：

$$
K_0
\subseteq
K_1
\subseteq
K_2
\subseteq
\cdots.
$$

研究增加：

$$
\text{facts}\uparrow,
$$

所以：

$$
\text{knowledge}\uparrow.
$$

如果再加入真理導向：

$$
\text{accuracy}\uparrow,
$$

我們便很容易默認：

$$
\text{accuracy}\uparrow
\Rightarrow
\text{knowledge productivity}\uparrow.
$$

但「正確多少」與「還能生成多少新的可研究結構」不是同一量。

## 1.2 一個封閉答案可能非常短

考慮有限選擇問題：

$$
x\in\{1,\ldots,n\}.
$$

若證據逐步排除：

$$
n-1
$$

個候選，

最終：

$$
x=x^\star.
$$

此時答案資訊可以寫得極短。

但得到：

$$
x^\star
$$

所需要的排除歷史可能很長。

因此：

$$
\boxed{
\text{description length of the final answer}
\neq
\text{information accumulated in reaching it}.
}
$$

## 1.3 終點可能越來越像「廢話」

某些理論越往底層收斂，越可能出現：

$$
X=X,
$$

$$
\text{energy is conserved under the stated conservation law},
$$

$$
\text{a valid identity remains identical under renaming}.
$$

如果只看語句表面，這些話像 tautology。

但這不代表：

$$
\text{derivational significance}=0.
$$

真正的資訊可能在：

$$
\text{why no stronger independent statement remains}.
$$

---

# 2. 五個維度必須拆開

本文定義至少五個不同量。

## 2.1 Truth / Correctness

對命題：

$$
p,
$$

理想化寫：

$$
T(p)\in\{0,1\}.
$$

現實研究中我們通常只能處理：

$$
\Gamma(p)
=
\text{epistemic confidence},
$$

而不能直接存取 $T(p)$。

## 2.2 Fidelity

模型：

$$
M
$$

對 target：

$$
W
$$

的保真度：

$$
F(M,W).
$$

它可以依任務不同而改變。

因此更精確：

$$
F(M,W\mid \mathcal T).
$$

## 2.3 Closure

定義：

$$
C(M)
$$

表示在指定問題域內，模型留下的 unresolved independent degrees of freedom 有多少被關閉。

粗略可寫：

$$
C(M)
=
1-
\frac{
H(\Omega_M)
}{
H(\Omega_{\mathrm{ref}})
}.
$$

## 2.4 Generativity

定義：

$$
G(M)
$$

不是輸出文字數，而是模型能產生多少：

$$
\text{audited new descendants}.
$$

例如：

- 新命題；
- 新 lemma；
- 新可檢驗 prediction；
- 新 correction；
- 新 mechanism；
- 新 transfer。

## 2.5 Utility

$$
U(M\mid\mathcal T)
$$

表示對任務 $\mathcal T$ 的實用價值。

可能：

$$
F_1>F_2
$$

但：

$$
U_1<U_2.
$$

---

# 3. 非單調性：核心命題

## 3.1 不成立的強單調命題

本文拒絕：

$$
F\uparrow
\Rightarrow
G\uparrow.
$$

拒絕：

$$
F\uparrow
\Rightarrow
U\uparrow.
$$

也拒絕：

$$
C\uparrow
\Rightarrow
G\uparrow.
$$

## 3.2 弱版本

本文只提出：

$$
\boxed{
\exists\ \text{domains such that }
\frac{\partial G}{\partial F}
\le0
}
$$

在某些區段成立。

也就是：

> 在某些問題域，保真度提高時，中間理論生成性可能不增反降。

## 3.3 更一般的 landscape

令：

$$
\mathbf z
=
(F,C,G,U,E),
$$

其中 $E$ 表示 explanatory reach。

更合理的是：

$$
\mathbf z
\in
\mathcal Z
$$

形成多維 landscape。

不是一條：

$$
\text{good}\rightarrow\text{better}
$$

的直線。

---

# 4. 為什麼 closure 可能降低 generativity

## 4.1 候選空間收縮

設定義：

$$
D_0
$$

對應：

$$
\Omega_0.
$$

加入有效約束：

$$
c_1,c_2,\ldots,c_n.
$$

則：

$$
\Omega_k
=
\Omega_0
\cap
\bigcap_{i=1}^{k}c_i.
$$

通常：

$$
\Omega_{k+1}
\subseteq
\Omega_k.
$$

## 4.2 自由度下降

若：

$$
d_k
=
\operatorname{Dim}_{\mathrm{eff}}(\Omega_k),
$$

則：

$$
d_{k+1}\le d_k.
$$

可研究分支：

$$
B_k
$$

也可能下降。

## 4.3 研究不是越精確分支越多

如果每次約束都切掉大量候選：

$$
|\Omega_k|
\downarrow,
$$

那麼新的中間假說數可能先下降。

這是「反轉」的最簡單來源。

---

# 5. 但 closure 也可能增加 generativity

## 5.1 這就是為什麼本文不是單調反命題

一個模糊問題：

> 為什麼世界如此？

太寬，

反而：

$$
G_{\mathrm{audited}}\approx0.
$$

因為沒有可驗證邊界。

## 5.2 精確化可以打開新理論

當問題被定義成：

$$
Q(D,C,t,S),
$$

反而開始產生：

- theorem；
- experiment；
- simulation；
- counterexample。

因此：

$$
C\uparrow
$$

在早期可能使：

$$
G\uparrow.
$$

## 5.3 所以更可能是分段關係

一種可能圖像：

$$
G(C)
$$

先上升，

到某個區間後下降。

這會自然形成：

$$
\text{intermediate maximum}.
$$

---

# 6. 「越是真理越可能像廢話」的嚴格弱化

## 6.1 不是所有真理都像廢話

例如：

$$
\text{Fermat's Last Theorem}
$$

顯然不是 tautology。

所以不能寫：

$$
T\uparrow
\Rightarrow
\text{banality}\uparrow.
$$

## 6.2 本文真正要說的是 closure limit

當理論核心被定義成：

> 不能再由更外部的同域概念縮減的 closure object，

則可能出現：

$$
\operatorname{Description}(T^\star)
$$

非常短。

## 6.3 壓縮而非空洞

因此：

$$
\boxed{
\text{banality-like surface}
}
$$

可能只是：

$$
\boxed{
\text{high semantic compression}.
}
$$

不能直接等於：

$$
\text{no content}.
$$

---

# 7. 信息位置轉移：內容從終點移到過程

## 7.1 終點與路徑

令：

$$
P
=
(x_0,x_1,\ldots,x_n).
$$

終點：

$$
x_n.
$$

若：

$$
K(x_n)\ll K(P),
$$

則大部分資訊不在 final state。

## 7.2 Research trace

因此要保存：

$$
\mathcal H_P
=
\{
\text{cuts},
\text{counterexamples},
\text{failed routes},
\text{obstructions},
\text{translations}
\}.
$$

## 7.3 與 LSI-PSD 系列的關係

前六篇一直強調：

$$
\text{proof trace}
$$

不能只被 final theorem 替代。

第 7 篇現在給出另一個理由：

> 越接近 closure，final statement 可能越壓縮，因此研究史的重要性反而上升。

---

# 8. Generativity 的正式操作性定義

## 8.1 Raw generativity

$$
G_{\mathrm{raw}}(M;N)
=
\#\text{generated descendants}.
$$

這幾乎沒有科學價值。

## 8.2 Audited generativity

$$
G_A(M;N)
=
\#\text{audited non-equivalent descendants}.
$$

## 8.3 Transfer generativity

如果 descendants 能移到別的問題：

$$
G_T(M)
=
\#\text{validated transferable descendants}.
$$

## 8.4 Durable generativity

更嚴格：

$$
G_D(M,\Delta t)
=
\#\text{descendants surviving audit after time }\Delta t.
$$

## 8.5 本文主要關心

$$
\boxed{
G_{\mathrm{useful}}
=
f(G_A,G_T,G_D).
}
$$

不是文字爆炸。

---

# 9. Fidelity 也不是單一數字

## 9.1 Structural fidelity

$$
F_S.
$$

## 9.2 Predictive fidelity

$$
F_P.
$$

## 9.3 Mechanistic fidelity

$$
F_M.
$$

## 9.4 Domain fidelity

$$
F_D.
$$

## 9.5 Task fidelity

$$
F_T.
$$

一個 minimal model：

$$
F_M
$$

可能低，

但：

$$
F_{\mathrm{macro}}
$$

可以高。

這就是很多爭論的來源。

---

# 10. Minimal models：少細節為什麼可能更有解釋力

## 10.1 Batterman–Rice 的核心問題

Minimal model 研究關心：

> 為什麼極度簡化模型能解釋大量差異很大的真實系統？

關鍵不一定是：

$$
M\approx W
$$

在細節上很像。

## 10.2 大尺度不變行為

若一整類系統：

$$
W_1,\ldots,W_n
$$

都在某尺度呈現：

$$
B^\star,
$$

而各自微觀差異：

$$
\delta_i
$$

不影響 $B^\star$，

那 minimal model 的價值在於：

$$
\boxed{
\text{showing irrelevance of }\delta_i.
}
$$

## 10.3 這直接打破一個單調直覺

$$
\text{more microscopic detail}
\not\Rightarrow
\text{more explanatory clarity}.
$$

甚至：

$$
\text{detail}\uparrow
\Rightarrow
\text{invariant visibility}\downarrow
$$

可能成立。

---

# 11. Ideal Gas Law：假的模型可以產生真的依賴資訊

## 11.1 Ideal gas

理想氣體：

- 分子無尺寸；
- 無交互作用。

這對真實氣體並不字面成立。

## 11.2 但：

$$
PV=nRT
$$

在特定 regime 很有用。

## 11.3 Spagnesi 的規範比較角色

更重要的是：

> 理想模型可以成為 reference norm。

現實偏離：

$$
\Delta
=
W-M
$$

本身帶資訊。

例如：

$$
\Delta\neq0
$$

促使研究者引入：

- molecular volume；
- intermolecular forces；
- phase behavior。

## 11.4 偏差不只是 error

因此：

$$
\boxed{
\Delta
=
\text{diagnostic information}
}
$$

在特定研究制度下成立。

---

# 12. Deviation-generated explanation

## 12.1 模型太準反而沒有殘差可看

如果：

$$
M=W
$$

完全成立，

則：

$$
\Delta=0.
$$

沒有「為什麼偏離」的問題。

## 12.2 當 $\Delta$ 小但有結構

研究者可以問：

$$
\Delta
=
f(x)?
$$

這會生成：

$$
M_1,M_2,\ldots.
$$

## 12.3 所以 residual 可以是 generative channel

$$
\boxed{
\text{structured residual}
\rightarrow
\text{new mechanism hypotheses}.
}
$$

---

# 13. LISDD：2026 年把「哪裡錯」直接工程化

## 13.1 Local discrepancy

LISDD 的問題不是：

> 模型整體是否錯？

而是：

$$
\boxed{
\text{where is it wrong?}
}
$$

## 13.2 Missing mechanism

再問：

$$
\boxed{
\text{what mechanism is missing?}
}
$$

## 13.3 Sparse symbolic recovery

最後：

$$
\boxed{
\text{can the discrepancy be expressed symbolically?}
}
$$

## 13.4 對本文的意義

這形成：

$$
\text{model error}
\rightarrow
\text{localization}
\rightarrow
\text{symbolic descendant}.
$$

也就是錯誤不是終點，

而是生成 trigger。

---

# 14. Productive idealization 與 effective theory

## 14.1 Effective theory 不是 final theory

EFT 類框架明確接受：

$$
\text{domain limited}.
$$

## 14.2 低能描述

在適用尺度：

$$
E<\Lambda,
$$

高能自由度可被整合掉。

## 14.3 非基本不等於低價值

若一個 theory：

$$
T_{\mathrm{eff}}
$$

能：

- 隔離 relevant degrees；
- 提供可控展開；
- 給出可測 prediction；
- 指出 cutoff；

那它可能比「更 fundamental 但不可操作」的理論更有 explanatory utility。

## 14.4 非單調 fundamentality

因此：

$$
\text{Fundamentality}\uparrow
\not\Rightarrow
\text{Understanding}\uparrow.
$$

這與本文核心高度一致。

---

# 15. Carnot：錯的 caloric 假設如何打開正確路徑

## 15.1 歷史情境

Carnot 在能量守恆完整形成以前研究 heat engine。

他採用：

$$
\text{heat}=\text{conserved caloric fluid}.
$$

後來這一本體圖像被放棄。

## 15.2 Norton 的分析

Norton 指出，這個錯誤反而把 Carnot 引向：

$$
\text{reversible heat-engine model}.
$$

## 15.3 關鍵結果

最大效率只依賴：

$$
T_{\mathrm{hot}},
T_{\mathrm{cold}}.
$$

而與 working substance 細節無關。

## 15.4 本文的解讀

這不是：

$$
\text{false theory}\Rightarrow\text{truth magically}.
$$

而是：

$$
\boxed{
\text{a constrained false assumption selected a productive mathematical route}.
}
$$

---

# 16. Phlogiston：錯父理論與真實後代資料

## 16.1 Priestley 的語言

Priestley 將氧氣描述為：

$$
\text{dephlogisticated air}.
$$

## 16.2 氧氣的實驗事實仍然成立

他觀察到的氣體性質並不因 phlogiston theory 被推翻而消失。

## 16.3 Lavoisier 的重構

後續理論：

$$
T'
$$

重新解釋相同資料。

因此：

$$
\boxed{
\text{parent interpretation false}
\not\Rightarrow
\text{observational descendants false}.
}
$$

---

# 17. Parent failure / descendant survival

## 17.1 定義

一個研究母體：

$$
P
$$

生成：

$$
D(P)
=
\{d_1,\ldots,d_n\}.
$$

如果：

$$
P
$$

後來被修正或否定，

可定義 descendant survival：

$$
S_D(P)
=
\frac{
\#\{d_i:\text{survive independent audit}\}
}{
|D(P)|
}.
$$

## 17.2 高 survival

表示：

> 母理論的錯誤並沒有污染全部後代。

## 17.3 低 survival

則表示：

> 生成性可能只是錯誤自我繁殖。

這個區分對 AI 特別重要。

---

# 18. 任意錯誤不具有生產性

## 18.1 Astrology test

如果一個隨機模型偶然猜中幾次，

不能因此叫 fruitful science。

## 18.2 Luck problem

Spagnesi 對這個問題的處理非常重要。

模型必須：

$$
\text{systematically compare}
$$

現象，

不是：

$$
\text{lucky hit}.
$$

## 18.3 因此 productive deviation 需要約束

至少：

$$
\boxed{
\text{auditability}
+
\text{systematic comparison}
+
\text{transfer}
+
\text{truth-sensitive correction}.
}
$$

---

# 19. Productive deviation 的最小條件

本文提出五條。

## 條件一：Boundedness

偏差：

$$
\epsilon
$$

必須可描述。

## 條件二：Localization

知道：

$$
\epsilon
$$

在哪個 domain／regime 生效。

## 條件三：Comparability

可以比較：

$$
M_\epsilon
$$

與 target。

## 條件四：Descendant audit

生成物必須可驗證。

## 條件五：Correctability

當模型失效時，系統允許：

$$
M_\epsilon\rightarrow M_{\epsilon'}.
$$

---

# 20. Truth–Fidelity–Generativity Landscape

## 20.1 定義

令模型狀態：

$$
z
=
(F,C,G,U,E).
$$

## 20.2 研究不是一維 ascent

發展可能是：

$$
z_0
\rightarrow
z_1
\rightarrow
z_2.
$$

其中：

$$
F\uparrow,
C\uparrow,
G\downarrow,
U\uparrow.
$$

也可能：

$$
F\downarrow,
G\uparrow,
U\uparrow.
$$

## 20.3 沒有單一 scalar 排序

除非指定任務權重：

$$
J(z)
=
\alpha F+\beta C+\gamma G+\delta U+\eta E.
$$

不同任務：

$$
\mathcal T
$$

有不同權重。

---

# 21. 非單調 generativity 猜想

## 21.1 偏差參數

令：

$$
\epsilon
=
\operatorname{Dist}(M,M^\star).
$$

## 21.2 有效生成性

$$
G_{\mathrm{useful}}(\epsilon).
$$

## 21.3 一個可檢驗候選

本文不證明，但提出：

$$
\exists\epsilon^\star>0
$$

使：

$$
G_{\mathrm{useful}}(\epsilon^\star)
>
G_{\mathrm{useful}}(0)
$$

在某些 domain 成立。

## 21.4 大偏差崩潰

同時預期：

$$
\lim_{\epsilon\rightarrow\infty}
G_{\mathrm{useful}}(\epsilon)
=
0
$$

對受現實約束的科學模型具有合理性。

---

# 22. 生產性錯置窗口的前置形式

完整的 Productive Mis-specification Window 將在 LSI-PSD-09 展開。

本文先定義：

$$
\mathcal W_P
=
[
\epsilon_{\min},
\epsilon_{\max}
]
$$

使：

$$
G_{\mathrm{useful}}(\epsilon)
>
\tau_G.
$$

在窗口外：

$$
G_{\mathrm{useful}}
$$

低於門檻。

## 22.1 左側

太接近 closure：

$$
\epsilon\approx0
$$

可能缺少中間問題。

## 22.2 中間

存在 structured deviation。

## 22.3 右側

偏差太大，

變成：

$$
\text{noise}.
$$

---

# 23. Closure–Generativity curve

## 23.1 Closure

$$
C\in[0,1].
$$

## 23.2 一個可能形狀

$$
G(C)
=
aC(1-C)+bC.
$$

這只是一個 toy model。

## 23.3 目的

不是宣稱真實世界遵守二次函數。

而是提醒：

$$
\frac{dG}{dC}
$$

可以變號。

---

# 24. 生成性不能由 novelty 直接代理

## 24.1 新奇不等於有價值

$$
\nu\uparrow
$$

可能只是語言漂移。

## 24.2 有價值生成

必須至少：

$$
\text{novel}
+
\text{auditable}
+
\text{non-equivalent}.
$$

## 24.3 再加 transfer

更強：

$$
\text{transferable}.
$$

---

# 25. 高精度也可能造成「廢話化」

## 25.1 精確定義的終點

當所有條件都寫入：

$$
Q^\star
=
Q(D,C,S,t,F,\ldots),
$$

結果可能近似：

> 在所有保證 $Q^\star$ 成立的條件下，$Q^\star$ 成立。

## 25.2 這是一種 specification closure

如果把答案偷偷寫進條件，

那不是真理收斂，

而是：

$$
\boxed{
\text{vacuous closure}.
}
$$

## 25.3 必須區分

$$
\text{informative closure}
$$

與：

$$
\text{tautological closure}.
$$

---

# 26. Informative closure

定義一個 closure：

$$
C^\star
$$

若它同時滿足：

1. assumptions 未包含結論；
2. independent predictive content；
3. descendant reconstruction；
4. counterfactual support；
5. non-vacuity。

則可稱：

$$
\boxed{
\text{informative closure}.
}
$$

---

# 27. 真理壓縮指標

## 27.1 最終描述長度

$$
K(T^\star).
$$

## 27.2 路徑描述長度

$$
K(\mathcal H_T).
$$

## 27.3 壓縮比

$$
R_C
=
\frac{
K(\mathcal H_T)
}{
K(T^\star)
}.
$$

高：

$$
R_C
$$

表示：

> 最終 statement 很短，但到達它的 research trace 很長。

## 27.4 與「廢話」感

本文假設：

$$
R_C\uparrow
$$

可能提高終點的 banality perception。

這可做認知實驗。

---

# 28. 讀者位置與同一句話

同一句：

$$
X=X
$$

對 naive reader：

$$
I\approx0.
$$

對知道：

$$
\mathcal H_X
$$

的 reader：

$$
I>0.
$$

因此：

$$
\boxed{
\text{surface semantics}
\neq
\text{path-conditioned semantics}.
}
$$

這不是神秘論。

它只是說背景知識改變句子的資訊角色。

---

# 29. 科學進步不等於知識堆積

## 29.1 Angkasa 的問題

如果：

$$
K
$$

一直增加，

但大量新增知識：

$$
K_{\mathrm{irrelevant}}
$$

與核心問題無關，

那 progress 不一定增加。

## 29.2 Diminishing epistemic returns

可以出現：

$$
\frac{
\Delta P
}{
\Delta K
}
\rightarrow0.
$$

## 29.3 與 proof-space saturation 的接口

這正是：

$$
\text{paper count}\uparrow
$$

但：

$$
\text{audited new classes}\downarrow
$$

的另一個哲學版本。

---

# 30. 研究價值的位置可能從 truth accumulation 轉向 ignorance elimination

如果進步改寫成：

$$
\text{reduce structured ignorance},
$$

那失敗、obstruction 與 boundary map 都變得重要。

因此：

$$
\boxed{
\text{negative knowledge}
}
$$

也可以具有生成價值。

這接回 LSI-PSD-06。

---

# 31. 與 NS-203 的接口

## 31.1 我們目前知道什麼

NS-203 顯示：

- 某些支線高 recurrence；
- 有 higher-order sampling；
- 有 confluence；
- 整體 fixed-window novelty 未顯示穩健崩塌。

## 31.2 我們不知道什麼

不知道：

$$
\text{which states are closer to truth}.
$$

所以不能直接畫：

$$
F\uparrow
\rightarrow
G\downarrow.
$$

## 31.3 可做的實驗

對每個 basin $B$：

測：

$$
C_{\mathrm{audit}}(B),
$$

$$
G_A(B),
$$

$$
G_T(B),
$$

$$
R_O(B).
$$

看 closure proxy 與 generativity 是否相關。

---

# 32. Closure proxy

真理不可直接觀測，

所以用：

$$
C_{\mathrm{proxy}}
$$

例如：

- formally verified cuts；
- independent audits；
- surviving candidate reduction；
- obstruction concentration；
- theorem dependency stabilization。

## 32.1 不得叫 truth score

必須寫：

$$
\boxed{
\text{closure proxy}
\neq
\text{truth probability}.
}
$$

---

# 33. NS descendant transfer

如果某 NS route 最後失敗，

但其中 lemma：

$$
L
$$

可轉移到：

$$
Q'
$$

並正式證明，

則：

$$
G_T(B)>0.
$$

這就是：

$$
\boxed{
\text{parent non-closure with descendant utility}.
}
$$

它和第 8 篇直接相連。

---

# 34. AI 長程研究的真正諷刺

傳統評價：

$$
\text{Did it solve the theorem?}
$$

若：

$$
No,
$$

就可能視為零。

但研究 corpus 可能已產生：

$$
\{L_i,O_j,R_k,M_l\}.
$$

其中一些具有獨立價值。

因此：

$$
\boxed{
\text{unsolved parent}
\not\Rightarrow
\text{zero knowledge yield}.
}
$$

---

# 35. 但不能反過來替失敗找藉口

## 35.1 危險語法

> 雖然證不出來，但我們生成很多理論，所以成功。

這可能只是自我安慰。

## 35.2 必須測 descendants

每個 descendant 要有：

$$
\text{status}.
$$

例如：

- verified；
- plausible；
- refuted；
- duplicate；
- useful elsewhere；
- abandoned。

## 35.3 最終 yield

$$
Y
=
\frac{
N_{\mathrm{verified}}+
\lambda N_{\mathrm{transferred}}
}{
N_{\mathrm{generated}}
}.
$$

---

# 36. 真理—生成性反轉與科學工程

## 36.1 設計模型時不必最大 fidelity

工程目標：

$$
\max U(M\mid\mathcal T).
$$

不是：

$$
\max F(M,W)
$$

無條件。

## 36.2 模型適切性

更合理：

$$
M^\star_{\mathcal T}
=
\arg\max_M
U(M\mid\mathcal T).
$$

subject to：

$$
F(M,W\mid\mathcal T)>\tau_F.
$$

## 36.3 這是 bounded idealization

不是任意造假。

---

# 37. 科學模型的雙角色

模型可以同時是：

$$
\text{representation},
$$

以及：

$$
\text{generator of questions}.
$$

如果只評估：

$$
\text{fit},
$$

會漏掉第二個角色。

本文將第二個角色寫成：

$$
Q(M)
=
\{\text{questions induced by }M\}.
$$

---

# 38. Question generativity

定義：

$$
G_Q(M)
=
|Q(M)/\sim_Q|.
$$

對理想化模型，

deviation 可以生成：

$$
Q_\Delta.
$$

例如：

> 為什麼真實氣體偏離 ideal gas？

這個問題本身就是知識生成器。

---

# 39. Mechanism generativity

$$
G_M(M)
=
\#\text{audited missing mechanisms discovered}.
$$

LISDD 類流程正好可測：

$$
G_M.
$$

---

# 40. Theorem generativity

對數學：

$$
G_T(M)
=
\#\text{non-equivalent proved descendant theorems}.
$$

這是未來 Proof-Space Observatory 最重要的指標之一。

---

# 41. Tool generativity

有些失敗研究最終產生：

- solver；
- benchmark；
- visualization；
- formalization pipeline；
- dataset。

可定義：

$$
G_{\mathrm{tool}}.
$$

這種生成性與 theorem correctness 不同。

---

# 42. Negative-result generativity

No-go theorem：

$$
N
$$

可以排除一大片 route。

因此：

$$
G_{\mathrm{neg}}
$$

也應計算。

一個證明：

> 此方法族無法做到 X。

本身可能大幅提高未來效率。

---

# 43. Generativity vector

因此：

$$
\boxed{
\mathbf G
=
(
G_Q,
G_M,
G_T,
G_{\mathrm{tool}},
G_{\mathrm{neg}},
G_{\mathrm{transfer}}
).
}
$$

不要把 generativity 壓成一個數字。

---

# 44. Utility vector

同樣：

$$
\mathbf U
=
(
U_{\mathrm{predict}},
U_{\mathrm{explain}},
U_{\mathrm{control}},
U_{\mathrm{transfer}},
U_{\mathrm{education}},
U_{\mathrm{compute}}
).
$$

一個模型可以在不同維度不同。

---

# 45. 真理與 utility 仍不能解耦太遠

如果：

$$
F\rightarrow0
$$

但：

$$
U
$$

短期看似高，

可能是：

- overfit；
- spurious correlation；
- luck；
- hidden leakage。

所以需要：

$$
\boxed{
\text{truth-sensitive utility}.
}
$$

---

# 46. Truth-sensitive utility

定義：

$$
U_T
=
U\times R,
$$

其中：

$$
R
$$

代表 robustness under:

- new data；
- counterfactual test；
- independent replication；
- regime shift。

若：

$$
R\rightarrow0,
$$

則：

$$
U_T\rightarrow0.
$$

---

# 47. Productive Error 與 Error Amplification

## 47.1 Productive error

$$
\epsilon
\rightarrow
\{d_i\}
$$

且：

$$
S_D>0.
$$

## 47.2 Error amplification

$$
\epsilon
\rightarrow
\{e_1,e_2,\ldots\}
$$

所有 descendants 都依賴錯誤假設。

若 parent 被推翻：

$$
D(P)\rightarrow\varnothing.
$$

## 47.3 兩者必須區分

AI 很容易製造第二種。

---

# 48. Descendant independence

對 descendant：

$$
d_i,
$$

定義對 parent assumptions 的依賴：

$$
I(d_i;A_P).
$$

若：

$$
I\downarrow,
$$

descendant 更可能在 parent failure 後存活。

---

# 49. 科學史可作 retrospective benchmark

挑選：

- Carnot；
- phlogiston；
- Bohr atom；
- ideal gas；
- ether；
- effective theory。

建立：

$$
\text{parent assumptions}
\rightarrow
\text{descendants}
\rightarrow
\text{survival}.
$$

這可以測：

$$
S_D.
$$

---

# 50. 反例：不是所有錯理論都有高 generativity

大量：

- astrology；
- perpetual motion；
- unfalsifiable cosmology；
- arbitrary numerology；

都可以產生很多文字。

但：

$$
G_{\mathrm{useful}}\approx0.
$$

因此：

$$
\boxed{
\text{raw fertility}
\neq
\text{epistemic fertility}.
}
$$

---

# 51. Epistemic fertility

本文定義：

$$
E_F(P)
=
G_{\mathrm{useful}}(P)
\times
S_D(P)
\times
R(P).
$$

其中：

- $G_{\mathrm{useful}}$：有用後代量；
- $S_D$：母理論失敗後的後代存活率；
- $R$：可重複與可稽核性。

---

# 52. Closure fertility

同理可定義：

$$
E_C(T^\star)
$$

表示高度閉合理論的下游生成能力。

一個極簡核心：

$$
T^\star
$$

仍可以透過：

$$
\operatorname{Gen}(T^\star)
$$

生成龐大應用空間。

---

# 53. 最小核心—最大生成命題

本文提出：

$$
\boxed{
\text{small core}
\not\Rightarrow
\text{small generative universe}.
}
$$

甚至可研究：

$$
\max
\frac{
|\operatorname{Gen}(T)|
}{
K(T)
}.
$$

這是一種：

$$
\text{generative compression ratio}.
$$

---

# 54. 與萬有理論生成極限的接口

若終極理論不是百科全書，

而是：

$$
\text{minimal generative core},
$$

那麼：

$$
K(T^\star)\downarrow
$$

同時：

$$
|\operatorname{Gen}(T^\star)|\uparrow
$$

完全可能。

因此「越真越像廢話」最合理的版本不是：

> 真理沒有內容。

而是：

> 高度閉合的核心可能極度壓縮，而內容被外推到生成宇宙。

---

# 55. 動態知識不動點

令：

$$
K_{t+1}
=
\Phi(K_t,\Delta D_t).
$$

如果：

$$
K_t\rightarrow K^\star
$$

但每次新資料只造成：

$$
\|\Delta K^\star\|\ll1,
$$

則核心穩定。

此時新知識主要發生在：

$$
\operatorname{Applications}(K^\star).
$$

---

# 56. 真理閉合和研究終止不是同一件事

即使：

$$
T^\star
$$

已閉合，

研究仍可問：

- 哪些 system 是 instance？
- 哪些 boundary 失效？
- 哪些 mapping 存在？
- 哪些 approximation 最好？

所以：

$$
\boxed{
\text{theoretical closure}
\neq
\text{research termination}.
}
$$

---

# 57. 真理閉合甚至可能增加 application generativity

這是反轉的第二層。

前面：

$$
G_{\mathrm{theory}}
$$

可能下降。

但：

$$
G_{\mathrm{application}}
$$

可能上升。

因此：

$$
\mathbf G
$$

必須分維。

---

# 58. 雙層反轉

可能：

$$
C\uparrow
\Rightarrow
G_{\mathrm{theory}}\downarrow,
$$

同時：

$$
C\uparrow
\Rightarrow
G_{\mathrm{application}}\uparrow.
$$

這比「越真越沒創意」精確得多。

---

# 59. AI 研究系統應該測什麼

至少：

$$
F_{\mathrm{proxy}},
C_{\mathrm{proxy}},
\mathbf G,
\mathbf U,
S_D,
R_O.
$$

而不是：

$$
\text{paper count}.
$$

---

# 60. 真理—生成性相圖

可以把：

$$
F
$$

放橫軸，

$$
G
$$

放縱軸。

形成四區：

## I：高 fidelity / 高 generativity

理想研究工具。

## II：高 fidelity / 低 generativity

閉合核心、成熟定理、固定規律。

## III：低 fidelity / 高 generativity

最危險也最有趣：

可能是 productive idealization，

也可能是 hallucination engine。

## IV：低 fidelity / 低 generativity

純噪音。

---

# 61. III 區需要最嚴格 audit

因為：

$$
G\uparrow
$$

會誘惑研究者忽略：

$$
F\downarrow.
$$

所以 III 區必須要求：

- descendant verification；
- robustness；
- transfer；
- independent reproduction。

---

# 62. Proof-space 中的 III 區

某條 AI route：

$$
r
$$

生成大量新 lemma，

但 final theorem 一直不閉合。

這可能是：

### A

有價值新數學。

### B

大量等價改寫。

### C

錯 assumption 的後代。

### D

幻覺。

所以必須用：

$$
\text{semantic quotient}
+
\text{obstruction audit}
+
\text{descendant verification}.
$$

---

# 63. 實驗一：Controlled Idealization Sweep

## 63.1 建立可解 ground truth system

有：

$$
M^\star.
$$

## 63.2 加入偏差

$$
M_\epsilon.
$$

## 63.3 掃描

$$
\epsilon_1,\ldots,\epsilon_n.
$$

## 63.4 測

$$
F(\epsilon),
G_A(\epsilon),
G_T(\epsilon),
U(\epsilon).
$$

## 63.5 看是否非單調

如果：

$$
G_A
$$

在內部峰值，

支持本文假說。

---

# 64. 實驗二：Descendant Survival Test

## 64.1 先讓 AI 在錯模型上研究

得到：

$$
D(P).
$$

## 64.2 揭示 parent error

再重新 audit 所有 descendants。

## 64.3 測：

$$
S_D(P).
$$

這會直接區分 productive error 與 error amplification。

---

# 65. 實驗三：Closure Compression Test

對一組已知 theorem progression：

$$
T_1\rightarrow T_2\rightarrow\cdots\rightarrow T^\star.
$$

測：

$$
K(T_i),
$$

$$
K(\mathcal H_i),
$$

$$
G(T_i).
$$

看 final statement 是否壓縮而 path information 上升。

---

# 66. 實驗四：Minimal-model versus maximal-detail model

固定 target phenomenon。

比較：

$$
M_{\min}
$$

與：

$$
M_{\max}.
$$

測：

- predictive accuracy；
- explanatory invariants；
- transfer；
- hypothesis generation；
- human/AI comprehension。

這可測：

$$
\text{detail}\neq\text{understanding}.
$$

---

# 67. 實驗五：NS-203 closure–generativity profile

## 67.1 Basin-level

對每個 basin：

$$
B_i.
$$

## 67.2 Closure proxy

$$
C_i.
$$

## 67.3 Generativity vector

$$
\mathbf G_i.
$$

## 67.4 相關

估計：

$$
\operatorname{Corr}(C_i,G_{i,k}).
$$

不要預設正負。

---

# 68. 實驗六：Obstruction-induced generativity

對高 robust obstruction：

$$
O.
$$

比較 obstruction 出現前後：

$$
G_{\mathrm{before}},
G_{\mathrm{after}}.
$$

如果：

$$
G_{\mathrm{after}}\uparrow,
$$

障礙本身可能是 research generator。

---

# 69. Proof-space 版的 residual science

傳統模型：

$$
\text{residual}=data-model.
$$

proof-space：

$$
\text{residual}
=
\text{target closure}-\text{current route closure}.
$$

若能 canonicalize：

$$
R_P,
$$

它就能生成：

$$
\text{bridge lemma search}.
$$

---

# 70. 「錯問題」的高風險推論

即使：

$$
G(D_\epsilon)>G(D^\star),
$$

也不能推出：

$$
D_\epsilon
$$

更正確。

Generativity 不是 truth criterion。

這是本文最重要的防火牆之一。

---

# 71. Framing superiority 的條件

若新定義：

$$
D'
$$

聲稱比：

$$
D
$$

好，

至少要有：

1. semantic clarity；
2. formal consistency；
3. mapping to old problem；
4. explanatory gain；
5. practical theorem gain；
6. independent verification。

不是只因為：

$$
G(D')>G(D).
$$

---

# 72. 「實用性證明」的角色

一個 reformulation：

$$
Q'
$$

若能：

- 產生更強 theorem；
- 更容易驗證；
- 更容易 transfer；
- 更清楚對應現象；

則：

$$
U(Q')>U(Q).
$$

但仍不能單獨證明：

$$
Q
$$

原本沒有意義。

---

# 73. 共識不是 truth，但對方法採納重要

數學真理不由投票決定。

但新 framing 是否成為公共研究接口，

需要：

$$
\text{independent scrutiny}.
$$

因此：

$$
\text{community adoption}
$$

是制度性變量，

不是 truth variable。

---

# 74. AI 自動研究的風險：把 generativity 當獎勵

如果 reward：

$$
R=\text{novel outputs},
$$

模型會學：

$$
\text{maximize novelty}.
$$

最容易的方式可能是：

$$
\text{semantic drift}.
$$

## 74.1 正確 reward

更合理：

$$
R
=
\alpha G_A
+
\beta G_T
+
\gamma S_D
-
\lambda E_{\mathrm{error}}.
$$

---

# 75. AI 海戰術的第二次修正

第 5 篇說：

> 多 agent 不能都擠同 basin。

第 7 篇再加：

> 多 agent 也不能以 raw generativity 為成功。

需要：

$$
\boxed{
\text{diverse generation}
+
\text{descendant audit}
+
\text{parent correction}.
}
$$

---

# 76. 研究系統需要兩種 memory

## 76.1 Closure memory

保存：

- verified constraints；
- no-go；
- stable core。

## 76.2 Generativity memory

保存：

- productive deviations；
- descendants；
- transfer；
- survival。

兩種都需要。

---

# 77. 真理核心與探索殼

可將研究系統分：

$$
\mathcal K
=
\mathcal C
\cup
\mathcal E.
$$

其中：

$$
\mathcal C
=
\text{stable audited core},
$$

$$
\mathcal E
=
\text{exploratory shell}.
$$

## 77.1 Core 保守

高：

$$
F.
$$

## 77.2 Shell 開放

高：

$$
G.
$$

這可能是 AI 科學最實用的雙層架構。

---

# 78. Core–Shell dynamics

如果 shell 發現：

$$
d
$$

被反覆驗證，

則：

$$
d:
\mathcal E\rightarrow\mathcal C.
$$

如果 core 被反例推翻：

$$
c:
\mathcal C\rightarrow\mathcal E
$$

或刪除。

這是動態知識系統。

---

# 79. 真理—生成性反轉的弱定理式陳述

本文提出以下**方法論命題**：

若：

1. $D_2$ 比 $D_1$ 增加有效約束；
2. 這些約束使 admissible state space 真收縮；
3. generativity 主要來自可區分候選狀態或其關係；
4. 不存在額外新 representation 將收縮轉成新的關係爆炸；

則可能：

$$
G(D_2)\le G(D_1).
$$

這不是普遍 theorem，

只是條件性推論。

---

# 80. 反向弱命題

若：

1. $D_\epsilon$ 相對 $D^\star$ 有有限結構偏差；
2. 偏差可局部化；
3. 偏差產生可觀測 residual；
4. residual 可映射到可稽核 missing mechanisms；

則：

$$
G_M(D_\epsilon)>0.
$$

這是 productive deviation 的最小形式。

---

# 81. Non-Monotonic Epistemic Fertility Principle

本文提出：

$$
\boxed{
\textbf{Epistemic fertility need not be monotonic in truth-like fidelity.}
}
$$

中文：

**認識論肥沃性非單調原則。**

它不是：

> 錯誤更有價值。

而是：

> truth/fidelity 與 knowledge-generation rate 不是同一 coordinate。

---

# 82. Truth–Generativity Separation Principle

$$
\boxed{
T(p)
\neq
G(p).
}
$$

更精確：

$$
\boxed{
\operatorname{TruthStatus}(p)
\not\equiv
\operatorname{GenerativeValue}(p).
}
$$

---

# 83. Generativity Non-Justification Principle

$$
\boxed{
G(p)\uparrow
\not\Rightarrow
T(p)=1.
}
$$

這防止：

> 因為這個理論很會生東西，所以一定是真的。

---

# 84. Truth Non-Productivity Principle

$$
\boxed{
T(p)=1
\not\Rightarrow
G(p)\gg0.
}
$$

有些真命題就是局部、封閉、生成性低。

---

# 85. Descendant Independence Principle

$$
\boxed{
\operatorname{False}(P)
\not\Rightarrow
\forall d\in D(P),\operatorname{False}(d).
}
$$

但反向也不成立：

$$
\exists d\text{ true}
\not\Rightarrow
P\text{ true}.
$$

---

# 86. Minimality–Reach Separation

$$
\boxed{
K(T)\downarrow
\not\Rightarrow
|\operatorname{Gen}(T)|\downarrow.
}
$$

這是生成核心思想的數學化接口。

---

# 87. 非主張總表

本文不主張：

1. 真理越高，理論一定越少；
2. 精確定義一定降低生成性；
3. 錯誤理論一般比正確理論有用；
4. 科學應故意採用錯誤模型；
5. 任意偏差都具有 productive value；
6. generativity 可以作 truth criterion；
7. minimal model 一定優於 detailed model；
8. effective theory 比 fundamental theory 更真；
9. Carnot 的錯誤本體觀本身就是後來熱力學真理；
10. phlogiston theory 因為促進發現氧氣所以是正確理論；
11. NS-203 的局部高階採樣證明 NS framing 有錯；
12. P/NP 或 NS 可由 AI 生成性曲線判定；
13. final statement 很短就代表更接近真理；
14. tautology 一定是高階真理；
15. closure proxy 等於 truth probability；
16. community consensus 定義真值；
17. descendants 存活即可證明 parent theory 合理；
18. raw novelty 等於 epistemic fertility；
19. AI 只要生成更多理論就能自動逼近真理；
20. 本文已證明 inverted-U 曲線普遍存在。

---

# 88. 與前六篇的整合

LSI-PSD-01：

$$
\text{search regime}\neq\text{mathematical reality}.
$$

LSI-PSD-02：

$$
\text{coverage must be measured}.
$$

LSI-PSD-03：

$$
\text{generation must be quotiented}.
$$

LSI-PSD-04：

$$
\text{sampling has orders}.
$$

LSI-PSD-05：

$$
\text{saturation can be local}.
$$

LSI-PSD-06：

$$
\text{failure can confluence into canonical obstruction}.
$$

本文現在問：

> 當 proof space 被逐步收縮、壓縮與規範後，為什麼 generativity 未必同方向增加？

因此第 7 篇是從 proof-space dynamics 走向 epistemology of theory generation 的轉折點。

---

# 89. 與第 8 篇的接口

第 8 篇將集中研究：

$$
\boxed{
\text{Productive Mis-specification}.
}
$$

即：

> 如果 parent problem / model / definition 後來被證明有偏差，哪些 descendants 仍然成立？錯誤如何成為局部知識生成器？

本文已建立必要前提：

$$
T\neq G,
$$

$$
F\neq U,
$$

$$
\text{parent failure}\not\Rightarrow\text{descendant annihilation}.
$$

第 8 篇將正式處理 descendant survival、error inheritance 與 mis-specification taxonomy。

---

# 90. 結論

科學與數學研究並不只在一條「越真越好」的直線上移動。

更合理的圖像是：

$$
\boxed{
\text{truth/fidelity}
\times
\text{closure}
\times
\text{generativity}
\times
\text{utility}
\times
\text{explanatory reach}.
}
$$

有些理論越成熟：

$$
\text{closure}\uparrow,
$$

但：

$$
\text{new theoretical branches}\downarrow.
$$

有些理想化模型在細節上不真，

卻因為：

$$
\text{deviation}
$$

可以被系統性比較，

反而產生新的 mechanism、correction 與 explanation。

有些錯誤理論會生出可獨立存活的後代；

另一些只會放大錯誤。

所以真正重要的問題不是：

> 這個理論生了多少東西？

而是：

$$
\boxed{
\text{它生成的東西有多少能在母理論被修改、弱化甚至推翻後仍然存活？}
}
$$

也不是：

> 理論越精確是不是越好？

而是：

$$
\boxed{
\text{對這個任務而言，哪一個 fidelity–closure–generativity 組合最能產生可驗證、可轉移、可持續修正的知識？}
}
$$

這使「越是真理越可能像廢話」獲得一個較嚴格的版本：

$$
\boxed{
\text{Highly compressed closure can look semantically trivial while its derivational and generative universe remains large.}
}
$$

同時也使「錯誤可能很有用」獲得一個嚴格限制：

$$
\boxed{
\text{A deviation is epistemically productive only if it creates descendants that survive independent truth-sensitive audit.}
}
$$

因此本文最終提出：

$$
\boxed{
\textbf{Truth and generativity are coupled, but they are not identical and need not vary monotonically together.}
}
$$

這個命題，才是後續「生產性錯置」「生產性錯置窗口」與 AI 長程研究評價制度的基礎。

---

# 參考文獻

1. Batterman, R. W., & Rice, C. C. (2014). **Minimal Model Explanations.** *Philosophy of Science*, 81(3), 349–376. https://doi.org/10.1086/676677

2. Spagnesi, L. (2025). **Truth, Understanding, and Normativity in Scientific Models.** *Synthese*, 206, Article 1. https://doi.org/10.1007/s11229-025-05110-7

3. Weingarten, K. (2026). **Productive Idealizations for Scientific Understanding: A Case Study in Effective Theories.** PhilSci-Archive preprint. https://philsci-archive.pitt.edu/27959/

4. Norton, J. D. (2022). **How Analogy Helped Create the New Science of Thermodynamics.** *Synthese*, 200, 269.

5. Wang, Y. (2026). **Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy.** arXiv:2606.23215. https://arxiv.org/abs/2606.23215

6. Angkasa, W. (2025). **The Elimination of Proper Ignorance: Rethinking Scientific Progress Beyond Accumulation of Knowledge.** *Synthese*, 206, 295. https://doi.org/10.1007/s11229-025-05363-2

7. Spagnesi, L. (2023). **Regulative Idealization: A Kantian Approach to Idealized Models.** *Studies in History and Philosophy of Science*, 99, 1–9.

8. Rice, C. (2021). **Leveraging Distortions: Explanation, Idealization, and Universality in Science.** MIT Press.

9. American Chemical Society. **Joseph Priestley, Discoverer of Oxygen — National Historic Chemical Landmark.** Historical resource on Priestley, oxygen, phlogiston, and Lavoisier.

10. Holmes, T. (2022). **Reckoning with Continuum Idealizations: Some Lessons from Soil Hydrology.** *Philosophy of Science*.

11. George, R. J., Huang, S., Song, P., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925.

12. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $T$ | truth / correctness |
| $F$ | fidelity |
| $C$ | closure |
| $G$ | generativity |
| $U$ | utility |
| $E$ | explanatory reach |
| $\epsilon$ | 對參照模型／定義的偏差程度 |
| $G_A$ | audited generativity |
| $G_T$ | transfer generativity |
| $G_D$ | durable generativity |
| $G_Q$ | question generativity |
| $G_M$ | mechanism generativity |
| $G_{\mathrm{tool}}$ | tool generativity |
| $S_D$ | descendant survival ratio |
| $E_F$ | epistemic fertility |
| $R_C$ | closure compression ratio |
| $\mathcal C$ | stable audited core |
| $\mathcal E$ | exploratory shell |
| $\mathcal W_P$ | productive deviation / mis-specification candidate window |

---

## 附錄 B：最小可檢驗假說

### H1：非單調 fidelity–generativity

存在 domain：

$$
\frac{\partial G}{\partial F}
$$

在不同區段改變符號。

### H2：Descendant survival

某些 parent model 被否定後：

$$
S_D(P)>0.
$$

### H3：Structured deviation superior to random deviation

若偏差被局部化、可比較、可修正，

則：

$$
G_{\mathrm{useful}}(\epsilon_{\mathrm{structured}})
>
G_{\mathrm{useful}}(\epsilon_{\mathrm{random}}).
$$

### H4：Closure compression

某些成熟理論：

$$
K(T^\star)
\ll
K(\mathcal H_T).
$$

### H5：Application inversion

可能：

$$
C\uparrow
\Rightarrow
G_{\mathrm{theory}}\downarrow
$$

但：

$$
G_{\mathrm{application}}\uparrow.
$$

---

## 附錄 C：AI Research Evaluator Schema

```yaml
theory_or_model:
  id:
  domain:
  target:

truth_status:
  proven:
  refuted:
  unknown:

fidelity:
  structural:
  predictive:
  mechanistic:
  task:

closure:
  proxy:
  evidence:

generativity:
  questions:
  mechanisms:
  theorems:
  tools:
  negative_results:
  transfers:

descendants:
  generated:
  audited:
  survived_parent_revision:
  refuted:
  duplicated:

utility:
  prediction:
  explanation:
  control:
  transfer:
  computation:

robustness:
  replication:
  counterfactual:
  regime_shift:

classification:
  closed_core:
  productive_idealization:
  productive_deviation_candidate:
  error_amplification:
  noise:
```

---

## 附錄 D：一句話版本

$$
\boxed{
\text{最接近真理的核心，不一定最會生新理論；最會生新理論的模型，也不一定最接近真理。}
}
$$

真正值得研究的是：

$$
\boxed{
\text{哪些偏差會留下可驗證、可轉移、在母理論失效後仍能存活的後代知識。}
}
$$


<!-- END LSI-PSD-07 -->

---


<!-- BEGIN LSI-PSD-08 -->

# LSI-PSD-08 — 生產性錯置：錯誤問題如何生成可存活的後代理論

## Productive Mis-specification: How a Flawed Parent Problem Can Generate Surviving Descendant Knowledge

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 08  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Productive Mis-specification Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文提出「生產性錯置」作為一個可檢驗的方法論概念，不主張錯誤問題、錯誤定義、錯誤模型或錯誤形式化本身具有真理地位，也不主張科學應故意採用錯誤前提。本文特別區分 deliberate idealization、model misspecification、formalization defect、scope mismatch、category/framing anomaly 與單純 hallucination。本文亦不主張 Navier--Stokes、P/NP 或任何既有未解問題已被證明存在範疇錯置；AI 長期未能證明一個命題，只能作為搜尋制度的觀察資料，不能直接判決原問題有誤。

---

## 摘要

一個研究問題若最後被證明具有錯誤假設、錯誤尺度、錯誤形式化、錯誤範疇或不適切的問題切割，其整個研究歷史是否因此歸零？科學史與現代模型科學都顯示，答案不必然是肯定的。錯誤的 parent framework 可以產生正確的 observation、可重用的 mathematics、有效的 experimental technique、可轉移的 correction term、可驗證的 local theorem 與後來在不同 framing 下仍能成立的 descendant knowledge。這種現象不能被粗糙地總結為「錯誤也有價值」，因為任意錯誤同樣可以產生大量自洽但無效的後代。真正需要的是一套可區分：

$$
\text{productive mis-specification}
$$

與：

$$
\text{error amplification}
$$

的方法論。

本文在 LSI-PSD-07 的 Truth–Generativity Separation 基礎上，正式定義 parent object：

$$
P
=
(Q,D,A,L,M,R),
$$

其中 $Q$ 為問題陳述，$D$ 為 domain，$A$ 為 assumptions，$L$ 為表示語言，$M$ 為方法／模型結構，$R$ 為搜尋制度。若後續 audit 發現存在修正算子：

$$
\mathcal C(P)=P',
$$

使原 parent 的某一部分被弱化、替換、重新定位或否定，則定義 parent revision distance：

$$
\delta_P
=
d(P,P').
$$

研究歷史中由 $P$ 生成的後代集合為：

$$
\mathcal D(P)
=
\{d_1,\ldots,d_n\}.
$$

對每個 descendant $d_i$，在 parent 修正後重新進行 independent audit。若：

$$
d_i
$$

不依賴已被撤銷的錯誤部分，或可以經有限 translation／repair 在新 parent $P'$ 中保持有效，則稱其為 survivor descendant。

本文定義 descendant survival ratio：

$$
S_D(P\rightarrow P')
=
\frac{
\sum_i w_i\,\mathbf 1[d_i\text{ survives}]
}{
\sum_i w_i
},
$$

以及更嚴格的 epistemic fertility：

$$
\Phi_E(P)
=
G_A(P)
\cdot
S_D(P)
\cdot
R_D(P)
\cdot
T_D(P),
$$

其中 $G_A$ 為 audited generativity、$R_D$ 為後代穩健性、$T_D$ 為 transferability。生產性錯置不是「parent 錯但輸出很多」，而是：

$$
\boxed{
\text{parent revision}
+
\text{non-zero descendant survival}
+
\text{independent audit}
+
\text{truth-sensitive correction}.
}
$$

本文進一步建立六類 mis-specification：

1. deliberate idealization；
2. model-form misspecification；
3. scope／regime mismatch；
4. specification／formalization mismatch；
5. category／framing mismatch candidate；
6. arbitrary error／hallucination。

其中前五類都可能在特定條件下具有生產性，第六類通常只造成 error propagation。

現代研究提供了直接相鄰的工程實例。2026 年 LISDD 將物理模型的局部失效定位到特定 operating regime，再以稀疏符號形式發現缺失機制，顯示 model discrepancy 可以被轉換為新機制發現；同年的 physics-guided operator correction 與 missing-physics symbolic regression 工作，也把已知物理與 residual correction 明確分離，而不是把整個 parent model 丟棄。另一方面，2026 年 Lean benchmark audit 在多個 machine-checked theorem benchmark 中辨識出 counterexample、vacuity、unsound axiom、missing hypothesis、translation error 與 specification hazard，證明「形式 proof 成功」與「原 intended problem 被忠實表示」是不同層次。這些案例共同支持：**parent representation 或 model 可能有缺陷，而其中某些 local derivations、proof objects、diagnostics 或 correction mechanisms 仍可被保存。**

本文亦重新檢視 Carnot、phlogiston、ideal gas 與 effective-theory 類案例。這些案例不能簡化成「錯理論導致真理」，更合理的描述是：

$$
\text{flawed parent constraint}
\rightarrow
\text{structured research trajectory}
\rightarrow
\text{descendant separation}
\rightarrow
\text{selective survival}.
$$

本文最後將此框架接回 AI 長程數學研究。對 NS-203 這類 corpus，若未來某個 proof family 被證明基於不適切 assumption 或 representation，正確做法不是刪除整個 corpus，而是逐項重驗：

$$
\text{lemma},
\text{obstruction},
\text{counterexample},
\text{tool},
\text{transfer},
\text{negative result}.
$$

只有經過 post-revision descendant audit，才能知道哪些研究資產真正存活。

本文最終提出：

$$
\boxed{
\textbf{A parent problem can fail without annihilating all of its descendants.}
}
$$

但同時堅持：

$$
\boxed{
\textbf{Descendant productivity never retroactively makes the flawed parent true.}
}
$$

**關鍵詞：** 生產性錯置、productive mis-specification、descendant survival、parent revision、error inheritance、idealization、model discrepancy、formalization mismatch、category error、scientific models、AI mathematics、proof-space dynamics

---

# 1. 問題的提出：研究母體錯了，後面的東西都要丟掉嗎？

## 1.1 二元評價的誘惑

最簡單的研究評價是：

$$
P=
\begin{cases}
\text{correct},\\
\text{incorrect}.
\end{cases}
$$

若 parent：

$$
P
$$

最後被判：

$$
\operatorname{Incorrect}(P),
$$

直覺上容易推出：

$$
\forall d\in\mathcal D(P),
\quad
\operatorname{Invalid}(d).
$$

但這個推論一般不成立。

## 1.2 Parent 和 descendant 不是同一命題

一個 parent theory：

$$
P
$$

通常包含：

$$
P
=
(A_1,A_2,\ldots,A_m,M,Q).
$$

一個 descendant theorem：

$$
d_i
$$

只依賴其中部分：

$$
A(d_i)
\subseteq
\{A_1,\ldots,A_m\}.
$$

如果 parent 失敗來自：

$$
A_m,
$$

但：

$$
A_m\notin A(d_i),
$$

那麼 $d_i$ 不必一起失敗。

## 1.3 研究歷史需要 dependency-aware revision

所以 parent revision 後，不能做：

$$
\mathcal D(P)\rightarrow\varnothing.
$$

更合理是：

$$
\boxed{
\mathcal D(P)
\rightarrow
\operatorname{Audit}_{P\rightarrow P'}
(
\mathcal D(P)
).
}
$$

---

# 2. Parent object 的正式表示

本文定義研究母體：

$$
P
=
(
Q,D,A,L,M,R,H
),
$$

其中：

- $Q$：question / proposition；
- $D$：domain；
- $A$：assumptions；
- $L$：language / representation；
- $M$：model / method family；
- $R$：research regime；
- $H$：research history。

這個表示刻意比單一 theorem statement 更寬。

因為「錯置」可能發生在不同層。

---

# 3. 六種錯置不能混為一談

## 3.1 Deliberate Idealization

研究者明知：

$$
A_{\mathrm{ideal}}
$$

不字面成立，

但在指定 regime 中使用。

例如：

$$
\text{friction}=0.
$$

這不是疏忽。

是有目的的簡化。

## 3.2 Model-Form Misspecification

研究者原本相信：

$$
M
$$

足以描述系統，

後來 residual 顯示：

$$
M
$$

缺少某個 mechanism。

## 3.3 Scope / Regime Mismatch

模型在：

$$
D_1
$$

有效，

卻被錯用到：

$$
D_2.
$$

模型本身未必錯，

錯在適用範圍。

## 3.4 Specification / Formalization Mismatch

informal target：

$$
Q_I
$$

被形式化成：

$$
Q_F
$$

但：

$$
Q_I\not\equiv Q_F.
$$

這是 formal AI mathematics 特別重要的錯置。

## 3.5 Category / Framing Mismatch Candidate

問題本身可能把不同類型的對象、量詞、尺度或 truth criterion 混到同一判定域。

本文只稱：

$$
\boxed{
\text{candidate}
}
$$

除非有額外形式證據。

## 3.6 Arbitrary Error / Hallucination

沒有可校準結構、

沒有穩定對應、

沒有可驗證後代。

這不應被美化成 productive mis-specification。

---

# 4. 修正算子

若 audit 發現 parent 需要修正，

定義：

$$
\mathcal C:
P\mapsto P'.
$$

修正可以是：

- remove assumption；
- add missing assumption；
- change domain；
- weaken conclusion；
- strengthen premise；
- change representation；
- split problem；
- merge equivalent problems；
- replace mechanism；
- correct formalization。

---

# 5. Parent revision distance

## 5.1 定義

$$
\delta_P
=
d(P,P').
$$

這不是單純文本 edit distance。

## 5.2 分量

可寫：

$$
\delta_P
=
(
\delta_Q,
\delta_D,
\delta_A,
\delta_L,
\delta_M
).
$$

## 5.3 小修和大修

若：

$$
\delta_P\ll1,
$$

可能只是：

- typo；
- missing premise；
- normalization。

若：

$$
\delta_P\gg1,
$$

可能是：

- ontology replacement；
- domain replacement；
- theorem statement collapse。

---

# 6. Descendant object

由 parent $P$ 產生：

$$
d_i
=
(
C_i,
A_i,
\Pi_i,
V_i,
T_i
),
$$

其中：

- $C_i$：claim；
- $A_i$：dependencies；
- $\Pi_i$：derivation / proof；
- $V_i$：verification status；
- $T_i$：transfer status。

---

# 7. Descendant dependency

建立：

$$
A_i
\subseteq
A_P.
$$

如果 parent 被修掉部分：

$$
A_P^{-},
$$

那麼：

$$
A_i\cap A_P^{-}
$$

決定 descendant 的直接風險。

## 7.1 Error exposure

定義：

$$
E_i
=
\frac{
|A_i\cap A_P^{-}|
}{
|A_i|
}.
$$

越高：

$$
E_i,
$$

越可能需要重證。

---

# 8. Descendant survival

## 8.1 強存活

在新 parent $P'$ 下：

$$
P'\vdash d_i.
$$

## 8.2 可修復存活

存在有限 repair：

$$
\mathcal R_i(d_i)=d_i'
$$

且：

$$
P'\vdash d_i'.
$$

## 8.3 失敗

若：

$$
P'\vdash\neg d_i
$$

或形式 counterexample 存在，

則：

$$
d_i
$$

不存活。

## 8.4 未知

若無法判定，

狀態必須保留：

$$
\text{unknown}.
$$

---

# 9. Survival state 不應只用二值

定義：

$$
\sigma_i
\in
\{
\text{strong},
\text{repairable},
\text{transferred},
\text{refuted},
\text{unknown}
\}.
$$

這比：

$$
0/1
$$

更適合研究史。

---

# 10. Descendant survival ratio

給每個 descendant 權重：

$$
w_i.
$$

定義：

$$
S_D(P\rightarrow P')
=
\frac{
\sum_i w_i\,s_i
}{
\sum_i w_i
},
$$

其中：

$$
s_i=
\begin{cases}
1,&\text{strong survival},\\
\alpha,&\text{repairable},\\
\beta,&\text{transferred},\\
0,&\text{refuted},\\
\text{excluded},&\text{unknown}.
\end{cases}
$$

---

# 11. 為什麼 unknown 不應硬算零

如果：

$$
\text{unknown}=0,
$$

會把尚未驗證誤當成失敗。

所以應分別報：

$$
S_D^{\mathrm{verified}}
$$

與 coverage：

$$
C_D
=
\frac{
N_{\mathrm{audited}}
}{
N_{\mathrm{descendants}}
}.
$$

---

# 12. Productive mis-specification 的最小定義

本文定義：

一個 parent $P$ 在修正為 $P'$ 後，若：

1. parent revision 有實質內容；
2. descendant corpus 已建立；
3. 有非零比例 descendants 經 independent audit 存活；
4. survivor 不只依賴被撤銷錯誤；
5. survivor 具有 theorem、prediction、mechanism、tool、negative result 或 transfer value；

則可稱：

$$
\boxed{
P
\text{ exhibited productive mis-specification}.
}
$$

---

# 13. 這是一個歷史性質，不是先驗資格

在 parent 還沒被修正以前，

不能宣布：

> 我的錯誤一定會很有生產力。

Productive mis-specification 多半是：

$$
\boxed{
\text{retrospective or post-revision classification}.
}
$$

---

# 14. 為什麼這一點重要

否則任何人都可以說：

> 我現在胡說，但未來可能很有啟發。

這會讓概念失去區分力。

所以必須：

$$
\text{audit after revision}.
$$

---

# 15. Error amplification

相反地，定義：

$$
\boxed{
\text{Error Amplification}
}
$$

若 parent 錯誤：

$$
e_P
$$

被 descendants 大量繼承，

使：

$$
P\rightarrow
d_1,d_2,\ldots,d_n
$$

全部共享錯誤核心。

當 parent 被修正後：

$$
S_D\approx0.
$$

---

# 16. Error amplification ratio

定義：

$$
A_E
=
1-S_D
$$

在已充分 audit 的 corpus 中。

若：

$$
A_E\rightarrow1,
$$

代表 parent error 具有高污染性。

---

# 17. Error inheritance graph

建立：

$$
G_E
=
(V_D,E_{\mathrm{inherit}}).
$$

若：

$$
d_i
$$

把錯誤 assumption：

$$
a^{-}
$$

傳給：

$$
d_j,
$$

則：

$$
d_i\rightarrow d_j.
$$

這使錯誤傳播可追蹤。

---

# 18. Error centrality

某個錯誤 assumption：

$$
a^{-}
$$

如果出現在大量 descendants，

可定義：

$$
Z_E(a^{-})
=
\sum_i
\mathbf 1[a^{-}\in A_i]w_i.
$$

高：

$$
Z_E
$$

表示修正成本高。

---

# 19. 錯置的「肥沃」不是錯誤量，而是 survivor 量

錯誤很多：

$$
\epsilon\uparrow
$$

不代表：

$$
\Phi_E\uparrow.
$$

真正重要：

$$
\boxed{
\text{surviving audited descendants}.
}
$$

---

# 20. Epistemic fertility

定義 audited generativity：

$$
G_A(P)
=
\#\text{audited non-equivalent descendants}.
$$

descendant robustness：

$$
R_D(P).
$$

transferability：

$$
T_D(P).
$$

則：

$$
\boxed{
\Phi_E(P)
=
G_A(P)
\cdot
S_D(P)
\cdot
R_D(P)
\cdot
T_D(P).
}
$$

---

# 21. Raw fertility 與 epistemic fertility

一個 hallucination engine：

$$
G_{\mathrm{raw}}\gg1
$$

但：

$$
S_D\approx0,
$$

所以：

$$
\Phi_E\approx0.
$$

這是最重要的防濫用公式之一。

---

# 22. Idealization 和 mis-specification 的差別

## 22.1 Idealization

研究者知道：

$$
M\neq W,
$$

但使用：

$$
M
$$

作為受控 approximation。

## 22.2 Misspecification

研究者或系統在某階段把：

$$
M
$$

當作足夠模型，

後來發現不夠。

## 22.3 兩者都可能 productive

但 epistemic status 不同。

所以 observatory 必須記：

```text
ERROR_STATUS:
  deliberate
  accidental
  discovered_later
  unknown
```

---

# 23. Idealization 的科學角色

Stanford Encyclopedia 對 scientific models 的整理指出，Galilean idealization 常故意引入字面上不真的假設，例如 point masses、frictionless planes 等，以隔離主要結構。

這種：

$$
\text{known falsehood}
$$

與：

$$
\text{mistaken theory}
$$

不是一回事。

---

# 24. Productive idealization

如果理想化：

$$
I
$$

使：

$$
\text{invariant}
$$

更清晰、

可解性上升、

prediction 仍在 domain 內有效，

則：

$$
I
$$

具有 epistemic utility。

這不是本文最強的 productive mis-specification 案例，

但提供近鄰概念。

---

# 25. Model discrepancy：錯在哪裡比「整體錯」更重要

2026 年 LISDD 的核心問題：

$$
\boxed{
\text{where does the physical model fail?}
}
$$

而不是：

$$
\text{throw the whole model away}.
$$

它先找 clean regime，

再定位 discrepant regime，

最後找 missing symbolic term。

---

# 26. Local correction

令原模型：

$$
f_0(x).
$$

在 region：

$$
D_c
$$

成立。

在：

$$
D_e
$$

失效。

修正：

$$
f(x)
=
f_0(x)
+
\mathbf 1_{x\in D_e}\Delta f(x).
$$

這是一個典型：

$$
\boxed{
\text{parent preservation + local repair}.
}
$$

---

# 27. 為什麼這是 descendant survival 的工程類比

原模型中的 clean structure：

$$
f_0|_{D_c}
$$

被保留。

只修：

$$
D_e.
$$

因此 parent 不是：

$$
\text{all-or-nothing}.
$$

---

# 28. Physics-guided correction under misspecification

2026 年 operator-learning correction 類研究同樣把：

$$
\text{trusted physics}
$$

與：

$$
\text{correction}
$$

拆開。

模型缺陷：

$$
\neq
$$

全部 prior physics 無效。

這正是本文的結構。

---

# 29. Missing physics symbolic regression

若：

$$
\dot x
=
f_{\mathrm{known}}(x)
+
f_{\mathrm{missing}}(x),
$$

研究不是丟掉：

$$
f_{\mathrm{known}},
$$

而是發現：

$$
f_{\mathrm{missing}}.
$$

這是一種：

$$
\text{repairable parent}.
$$

---

# 30. Experimental design 甚至可以為「找缺失」服務

2026 年 missing-physics experimental design 直接根據候選 model structures 設計新實驗，

目的不是只估參數，

而是：

$$
\boxed{
\text{discriminate among missing mechanisms}.
}
$$

這表示錯置本身可以改變下一步實驗路由。

---

# 31. Formal theorem proving 的 specification problem

在 Lean 中，

kernel 證明：

$$
\Pi\vdash Q_F.
$$

只能推出：

$$
Q_F
$$

被形式證明。

它不能推出：

$$
Q_F\equiv Q_I.
$$

其中：

$$
Q_I
$$

是人類原始 intended theorem。

---

# 32. 2026 Lean benchmark audit

近期 corpus-scale audit 發現：

- counterexamples；
- vacuous theorems；
- unsound axioms；
- missing hypotheses；
- incomplete translations；
- incorrect translations；
- Lean-specific specification hazards。

這證明：

$$
\boxed{
\text{formal proof validity}
\neq
\text{specification fidelity}.
}
$$

---

# 33. 形式化 parent 失敗不一定抹掉 proof engineering descendants

假設：

$$
Q_F
$$

後來發現：

$$
Q_F\not\equiv Q_I.
$$

但在證：

$$
Q_F
$$

過程中可能產生：

- tactic；
- lemma；
- library patch；
- proof repair dataset；
- dependency tool；
- counterexample checker。

它們仍可能有效。

---

# 34. 但 theorem descendant 必須重新判

如果 lemma：

$$
L
$$

只對錯 formalization 有意義，

那：

$$
L
$$

未必具有目標數學價值。

所以：

$$
\text{tool survival}
$$

與：

$$
\text{theorem survival}
$$

必須分開。

---

# 35. Descendant taxonomy

本文將 descendants 分成：

1. theorem descendant；
2. observational descendant；
3. mechanism descendant；
4. method descendant；
5. tool descendant；
6. dataset descendant；
7. negative-result descendant；
8. transfer descendant。

---

# 36. 不同 descendant 有不同 survival criterion

## 36.1 Theorem

需要重新 proof。

## 36.2 Observation

需要獨立 measurement / historical record。

## 36.3 Method

需要在新 target 上重測。

## 36.4 Tool

需要 functionality test。

## 36.5 Negative result

需要確認 no-go assumptions 是否仍成立。

---

# 37. Descendant survival vector

$$
\boxed{
\mathbf S_D
=
(
S_T,
S_O,
S_M,
S_{\mathrm{tool}},
S_{\mathrm{data}},
S_{\mathrm{neg}},
S_{\mathrm{transfer}}
).
}
$$

不要把所有 survivor 混成一個比例。

---

# 38. Parent truth 不由 descendant survival 反推

即使：

$$
S_D\gg0,
$$

仍不能推出：

$$
P\text{ true}.
$$

這是：

$$
\boxed{
\text{Descendant Non-Retrovalidation Principle}.
}
$$

---

# 39. Descendant Non-Retrovalidation Principle

$$
\boxed{
S_D(P)\uparrow
\not\Rightarrow
T(P)=1.
}
$$

一個錯 parent 可以產生真 descendants。

真 descendants 不會回頭把 parent 變真。

---

# 40. Parent Failure Non-Annihilation Principle

反向：

$$
\boxed{
T(P)=0
\not\Rightarrow
\forall d_i,\ T(d_i)=0.
}
$$

這是本文核心。

---

# 41. Parent Revision Audit Principle

若：

$$
P\rightarrow P',
$$

則：

$$
\boxed{
\mathcal D(P)
\text{ must be re-audited, not automatically retained or discarded.}
}
$$

---

# 42. 科學史：Carnot

## 42.1 Parent

caloric conservation：

$$
A_c.
$$

## 42.2 後來修正

熱不被理解成守恆 caloric fluid。

## 42.3 Survivor

Carnot 的 reversible cycle structure、

temperature-dependent efficiency insight 等，

成為後續 thermodynamics 的核心歷史資產。

## 42.4 正確讀法

不是：

$$
A_c\text{ was true}.
$$

而是：

$$
\boxed{
A_c
\text{ constrained a fruitful route whose key descendants survived}.
}
$$

---

# 43. Carnot 的「幸運錯誤」不是隨機幸運

如果 parent 假設完全任意，

不太可能穩定導向可保留結構。

更合理理解：

$$
A_c
$$

抓住了一部分：

$$
\text{reversibility / state dependence}
$$

的結構，

但本體解釋錯。

---

# 44. 科學史：phlogiston

## 44.1 Parent interpretation

燃燒透過 phlogiston 解釋。

## 44.2 Observation descendants

Priestley 等人的氣體實驗產生可重複 observations。

## 44.3 Parent 被替換

Lavoisier 的 oxygen framework 重新解釋。

## 44.4 Survival

$$
\text{observation}
$$

存活，

$$
\text{interpretation}
$$

不存活。

---

# 45. Observation–Interpretation Separation

因此：

$$
\boxed{
\text{Observation}(d)
\neq
\text{Interpretation}(d).
}
$$

parent 修正時應分離重驗。

---

# 46. Ideal gas

理想氣體不是歷史上的「錯理論後來被推翻」同一類型。

它更像：

$$
\text{controlled idealization}.
$$

但它顯示：

$$
\text{strict literal falsehood}
$$

可以與：

$$
\text{high domain utility}
$$

共存。

---

# 47. Ideal gas descendants

偏差：

$$
\Delta(P,V,T)
$$

促使：

- virial expansion；
- van der Waals corrections；
- phase-transition analysis。

所以 idealization 既是模型，

也是：

$$
\boxed{
\text{deviation reference}.
}
$$

---

# 48. Effective theories

EFT 類框架更進一步：

$$
T_{\mathrm{eff}}
$$

公開承認：

$$
\text{domain limited}.
$$

它不假裝是 ultimate truth。

這使它降低：

$$
\text{mis-specification risk}.
$$

因為 scope 被明示。

---

# 49. Scope declaration 是防錯的重要技術

定義：

$$
\operatorname{Scope}(M)
=
D_M.
$$

若：

$$
x\notin D_M,
$$

則：

$$
M(x)
$$

不應自動被視為模型 failure。

這是：

$$
\boxed{
\text{scope-aware epistemology}.
}
$$

---

# 50. Scope mismatch 的 productive 形式

如果把模型錯用到：

$$
D'\not\subseteq D_M,
$$

發現：

$$
\Delta\neq0,
$$

這個失敗可以幫助找：

$$
\partial D_M.
$$

也就是：

$$
\text{boundary discovery}.
$$

---

# 51. Boundary descendants

這類後代不是新 theorem 本身，

而是：

$$
\boxed{
\text{where the old theory stops working}.
}
$$

這非常有科學價值。

---

# 52. Category mismatch candidate

最難的是：

> 問題切割本身可能不適切。

例如：

- 把不同尺度當同一對象；
- 把 operational criterion 當 ontology；
- 把 representation artifact 當 invariant；
- 把局部量詞偷渡成全域量詞。

---

# 53. Category mismatch 的判定門檻必須最高

不能因為：

$$
\text{proof hard}
$$

就說：

$$
\text{category mistake}.
$$

至少需要：

1. explicit alternative formulation；
2. mapping theorem；
3. explanation of recurrent obstruction；
4. practical or formal gain；
5. independent audit。

---

# 54. 只是「我換個定義比較好證」還不夠

若：

$$
Q'
$$

比：

$$
Q
$$

好證，

可能只是：

$$
Q'
$$

比較弱。

所以需要：

$$
\operatorname{Map}(Q,Q').
$$

---

# 55. Reformulation map

理想情況有：

$$
f:Q\rightarrow Q',
$$

以及：

$$
g:Q'\rightarrow Q
$$

的清楚關係。

如果：

$$
Q\Leftrightarrow Q',
$$

則是等價重表述。

如果只有：

$$
Q\Rightarrow Q',
$$

必須明示 loss。

---

# 56. Framing superiority 不是語言喜好

定義：

$$
\operatorname{Sup}(Q',Q)
$$

至少依賴：

- semantic clarity；
- proof utility；
- empirical fit；
- transfer；
- obstruction resolution；
- mapping fidelity。

---

# 57. Productive mis-specification 的三種主要路徑

## A. Residual path

$$
P
\rightarrow
\Delta
\rightarrow
\text{missing mechanism}.
$$

## B. Boundary path

$$
P
\rightarrow
\text{failure regime}
\rightarrow
\partial D.
$$

## C. Reinterpretation path

$$
P
\rightarrow
d_i
\rightarrow
P'
\rightarrow
\text{same }d_i\text{ under new interpretation}.
$$

---

# 58. 第四條：Tool path

$$
P
\rightarrow
\text{hard research}
\rightarrow
\text{new tool}.
$$

即使 parent 失敗，

tool 仍可能長期存活。

---

# 59. 第五條：Negative path

錯 parent 的研究可能證明：

$$
\text{method }M\text{ cannot achieve target under assumptions }A.
$$

如果這個 no-go theorem 本身正確，

它仍存活。

---

# 60. 第六條：Representation path

為了解一個錯置問題建立：

$$
L'
$$

新表示。

後來發現：

$$
L'
$$

對其他問題也有價值。

這是 transfer survivor。

---

# 61. Survivor independence

定義 descendant 對錯 parent component：

$$
e_P
$$

的 dependence：

$$
I_i
=
\operatorname{Dep}(d_i,e_P).
$$

若：

$$
I_i=0,
$$

strong independence。

---

# 62. Repair cost

如果：

$$
I_i>0
$$

但可修：

$$
d_i\rightarrow d_i',
$$

定義：

$$
C_R(d_i)
=
\operatorname{Cost}(d_i\rightarrow d_i').
$$

低 repair cost 表示 robust descendant。

---

# 63. Survivor robustness score

$$
R_i
=
f(
1-I_i,
1-C_R,
\text{independent verification},
\text{cross-domain transfer}
).
$$

---

# 64. Descendant value matrix

| descendant | truth status | dependence on parent error | repair cost | transfer | survivor |
|---|---:|---:|---:|---:|---|
| $d_1$ | proven | low | 0 | high | yes |
| $d_2$ | unknown | medium | unknown | low | unknown |
| $d_3$ | refuted | high | high | none | no |

這比一句：

> 這個理論很 fruitful。

精確得多。

---

# 65. Post-revision knowledge accounting

parent 修正後：

$$
K_{\mathrm{before}}
$$

不應直接歸零。

建立：

$$
K_{\mathrm{after}}
=
K_{\mathrm{survive}}
\cup
K_{\mathrm{repaired}}
\cup
K_{\mathrm{unknown}}.
$$

---

# 66. Knowledge write-off ratio

$$
W_O
=
\frac{
K_{\mathrm{refuted}}
}{
K_{\mathrm{audited}}
}.
$$

與：

$$
S_D
$$

一起報。

---

# 67. AI 大規模生成時，write-off 可能非常重要

若 AI 生成：

$$
10^4
$$

個 descendants，

parent 後來修正，

如果：

$$
W_O=0.95,
$$

那麼 raw generativity 幾乎沒有價值。

---

# 68. 因此研究系統應保存 provenance

每個 descendant 必須知道：

$$
\text{which parent assumptions generated it}.
$$

否則 parent revision 後無法重算風險。

---

# 69. Provenance schema

```yaml
descendant_id:
parent_id:
parent_version:
assumptions_used:
representation:
method:
proof_dependencies:
verification:
derived_at:
transfer_targets:
revision_status:
```

---

# 70. Versioned parent

研究 parent 必須版本化：

$$
P^{(0)},
P^{(1)},
\ldots.
$$

descendant 也記：

$$
d_i@P^{(t)}.
$$

---

# 71. Revision cascade

若：

$$
P^{(t)}\rightarrow P^{(t+1)},
$$

系統自動找：

$$
\{d_i:A_i\cap\Delta A\neq\varnothing\}.
$$

這些進入 re-audit queue。

---

# 72. Research database 的新需求

普通文獻庫只存：

- title；
- abstract；
- citation。

Proof-space database 還要存：

- assumption lineage；
- obstruction lineage；
- revision lineage；
- survivor status。

---

# 73. AI agent 的 revision-aware memory

Agent 不只需要知道：

> 我以前證過 $L$。

而要知道：

> $L$ 是在 parent version $v3$、assumption set $A_{v3}$ 下證的；$v4$ 已移除 $a_7$，需要確認 $L$ 是否依賴 $a_7$。

---

# 74. 這會防止「殭屍知識」

殭屍知識：

$$
d_i
$$

已因 parent revision 失效，

但後續 agent 仍引用。

這在長程 AI research 特別危險。

---

# 75. Zombie knowledge rate

定義：

$$
Z_K
=
\frac{
N_{\mathrm{invalid\ but\ active}}
}{
N_{\mathrm{active}}
}.
$$

成熟系統應讓：

$$
Z_K\rightarrow0.
$$

---

# 76. 生產性錯置與 proof-space saturation

一個 basin：

$$
B
$$

可能長期研究後被發現：

$$
\text{framing flawed}.
$$

這時：

$$
B
$$

不是垃圾桶。

而是一個 descendant reservoir。

---

# 77. Basin salvage

定義：

$$
\operatorname{Salvage}(B)
=
\{
d\in B:d\text{ survives revision}
\}.
$$

salvage ratio：

$$
S_B.
$$

---

# 78. Obstruction salvage

一些 obstruction：

$$
O
$$

可能只因錯 formalization 存在。

另一些 obstruction 其實是更一般方法族的真限制。

所以 obstruction 也要 post-revision audit。

---

# 79. No-go salvage

若 parent 被修正，

一個 no-go theorem：

$$
N
$$

若量詞與 assumptions 仍保持，

可能繼續有效。

這類 negative survivor 很重要。

---

# 80. NS-203：如何使用本框架

目前不能說：

$$
\text{NS parent is mis-specified}.
$$

但可以預先建立：

$$
\text{revision-ready corpus}.
$$

---

# 81. Revision-ready NS corpus

每個 NS artifact 抽：

$$
(
A,C,L,O,R,T
).
$$

如果未來某 assumption family 被否定，

可以立刻找出受影響 descendants。

---

# 82. 假設性案例

假設未來發現：

$$
A^\star
$$

是某支 NS route 的不適切 global assumption。

則：

$$
\mathcal D(A^\star)
$$

進入 audit。

---

# 83. 可能存活的東西

即使 parent route 失效，

仍可能存活：

- local estimate；
- finite-scale lemma；
- computational diagnostic；
- visualization；
- obstruction taxonomy；
- other-PDE transfer。

---

# 84. 不能提前宣稱存活

每個都要：

$$
\operatorname{Reverify}.
$$

否則只是希望。

---

# 85. P/NP 同理

即使有人懷疑現有 problem framing 有高難度表示／範疇問題，

在沒有更強 reformulation theorem 前，

只能標：

$$
\text{meta-hypothesis}.
$$

不能寫：

$$
\text{P/NP is malformed}.
$$

---

# 86. 「無法判定」也不能由 corpus exhaustion 推出

即使：

$$
10^6
$$

輪 AI 都失敗，

仍不能推出：

$$
\operatorname{Independent}(Q,\mathcal A).
$$

independence 需要 metamathematical proof。

---

# 87. Productive mis-specification 的最危險濫用

> 因為歷史上錯理論有時 fruitful，所以我的錯理論也值得保留。

不成立。

歷史案例是 retrospective。

---

# 88. Retrospective evidence requirement

至少需要：

$$
N_{\mathrm{survivors}}>0
$$

且：

$$
C_D
$$

足夠高。

否則不能稱 productive。

---

# 89. 任意 wrong framing 的對照組

未來實驗應故意加入：

$$
P_{\mathrm{random}}
$$

作為 negative control。

看其：

$$
\Phi_E
$$

是否顯著低於 structured mis-specification。

---

# 90. 實驗一：Synthetic Parent Revision Benchmark

## 90.1 建立 ground truth parent

$$
P^\star.
$$

## 90.2 注入錯置

- missing assumption；
- wrong scope；
- wrong term；
- wrong quantifier；
- representation distortion。

## 90.3 讓 AI 研究

產生：

$$
\mathcal D(P_\epsilon).
$$

## 90.4 揭示 ground truth

修正：

$$
P_\epsilon\rightarrow P^\star.
$$

## 90.5 測

$$
S_D,
W_O,
\Phi_E.
$$

---

# 91. 實驗二：Formalization Mismatch Salvage Test

選取 Lean benchmark 中已知 specification defect。

讓 prover 在 defect version 上產生：

- proof；
- helper lemma；
- tool trace。

修正 statement 後，

測哪些資產仍能使用。

---

# 92. 實驗三：Missing-Physics Descendant Test

使用已知 dynamical system。

故意移除 mechanism：

$$
f_m.
$$

讓系統發現：

- residual；
- candidate corrections；
- symbolic mechanisms。

最後與 ground truth 比較。

---

# 93. 實驗四：Historical Retrospective Graph

對 Carnot、phlogiston 等案例建立：

$$
P
\rightarrow
d_i
\rightarrow
P'
$$

圖。

需要避免 presentism，

只標可文獻支持的 dependency。

---

# 94. 實驗五：NS Revision Simulation

不是宣稱 NS 錯。

而是人工選一個 route-level assumption：

$$
a
$$

做 ablation。

比較：

$$
\mathcal D_{\mathrm{keep}}
$$

與：

$$
\mathcal D_{\mathrm{drop}}.
$$

測 corpus salvageability。

---

# 95. 實驗六：Zombie Knowledge Stress Test

修改 parent version，

看 agent 是否仍引用 invalid descendants。

指標：

$$
Z_K.
$$

這對 persistent AI research system 很關鍵。

---

# 96. Productive Mis-specification Observatory

應至少有四張圖：

1. parent revision graph；
2. descendant dependency graph；
3. error inheritance graph；
4. survivor map。

---

# 97. Parent revision graph

$$
P^{(0)}
\rightarrow
P^{(1)}
\rightarrow
\cdots.
$$

每條 edge 記：

$$
\Delta A,\Delta D,\Delta Q,\Delta L,\Delta M.
$$

---

# 98. Descendant dependency graph

$$
P^{(t)}
\rightarrow
d_i.
$$

讓 lineage 可追蹤。

---

# 99. Error inheritance graph

標出：

$$
a^{-}
$$

如何往後傳。

---

# 100. Survivor map

parent revision 後：

- green：strong survivor；
- yellow：repairable；
- blue：transferred；
- red：refuted；
- gray：unknown。

UI 顏色只是 status，不是 truth metaphysics。

---

# 101. Productive Mis-specification Score

可建立操作性向量，而非單數：

$$
\mathbf P_M
=
(
G_A,
S_D,
R_D,
T_D,
C_D,
1-Z_K
).
$$

---

# 102. 為什麼不建議單 scalar

因為：

- 高 generativity 可能低 survival；
- 高 survival 可能樣本很少；
- 高 transfer 可能 theorem value 低。

向量更誠實。

---

# 103. 如果一定要排序

指定任務權重：

$$
J_{\mathcal T}
=
\mathbf w_{\mathcal T}\cdot\mathbf P_M.
$$

不同任務有不同排序。

---

# 104. Mis-specification discovery time

定義：

$$
t_m.
$$

parent 從建立到被修正：

$$
\Delta t_m.
$$

---

# 105. 越晚發現，corpus 污染越大

若 generation rate：

$$
g(t),
$$

則潛在 affected descendants：

$$
N_{\mathrm{risk}}
=
\int_0^{t_m}
g(t)\,dt.
$$

AI 高生成時代這個量可能非常大。

---

# 106. 因此 AI 需要更早的 parent audit

生成速度：

$$
g\uparrow
$$

時，

parent audit frequency 也應：

$$
f_{\mathrm{audit}}\uparrow.
$$

否則錯誤會快速擴散。

---

# 107. Auditing cadence

可設：

$$
f_{\mathrm{audit}}
=
h(
g,
Z_E,
C_{\mathrm{sat}},
R_O
).
$$

高生成、高 error centrality、反覆 obstruction 時提高 audit。

---

# 108. 生產性錯置不是反對嚴謹

恰恰相反。

如果不嚴謹，

根本不知道：

$$
\text{which descendants survived}.
$$

所以這套理論要求比「全部丟掉」更細的 provenance。

---

# 109. 生產性錯置不是反對真理

本文仍承認：

$$
T(P)
$$

與：

$$
T(d_i)
$$

是核心判準。

只是反對：

$$
T(P)=0
\Rightarrow
T(d_i)=0
$$

這個錯誤傳播推論。

---

# 110. 與 Lakatos 類研究綱領思想的距離

Lakatos 強調 research programme 可以在 anomaly 下持續發展，

而不是遇到一次反例立刻被拋棄。

本文與其有精神上的近鄰：

> research history 不應由單次 parent failure 全部抹除。

但本文更工程化地要求：

$$
\text{descendant-level post-revision audit}.
$$

---

# 111. 與 scientific realism / anti-realism 的距離

本文不解決：

$$
\text{science aims at truth?}
$$

這個宏觀爭論。

本文只要求：

$$
\boxed{
\text{truth status and generative value be separately recorded}.
}
$$

---

# 112. 生產性錯置和「醜模型」

2025 年對 high-energy physics 的討論指出，在特定實驗環境中，研究可能合理轉向更狹窄、ad hoc、complex 的「ugly models」。

這提醒：

$$
\text{simplicity}
$$

也不是永遠優先的單調判準。

模型選擇受：

$$
\text{available evidence landscape}
$$

制約。

---

# 113. 這與 mis-specification 的關係

一個 narrow model 可能：

$$
\text{less universal}
$$

但：

$$
\text{better targeted}.
$$

所以：

$$
\text{scope reduction}
$$

有時是 correction，不是退步。

---

# 114. Problem splitting

如果 parent：

$$
Q
$$

過度寬，

可拆：

$$
Q
\rightarrow
(Q_1,\ldots,Q_n).
$$

某些 descendants 可能其實屬於：

$$
Q_i.
$$

修正後應重新歸檔。

---

# 115. Problem merge

反過來，兩個看似不同 parent：

$$
Q_1,Q_2
$$

可能其實同一更高階結構的投影。

reformulation 可以 merge。

---

# 116. Category repair

若發現：

$$
Q
$$

混了兩種 truth criterion，

修正可能不是：

$$
Q\rightarrow Q'
$$

單一命題，

而是：

$$
Q\rightarrow
(Q_{\mathrm{math}},
Q_{\mathrm{empirical}}).
$$

---

# 117. 這種 split 會使很多舊爭論消失

因為原來：

$$
\text{disagreement}
$$

其實是：

$$
\text{different propositions}.
$$

但這要靠明確 semantic audit，

不能只靠哲學宣言。

---

# 118. Parent error 也可能是量詞錯誤

例如：

$$
\exists x
$$

被誤寫：

$$
\forall x.
$$

這種錯誤可以產生大量「很難的」證明失敗。

修正後問題突然簡單。

---

# 119. 量詞錯誤的 descendant salvage

一些局部 lemma：

$$
L(x)
$$

仍可能真。

只是不能支撐：

$$
\forall x.
$$

因此 local theorem 可存活，

global claim 不存活。

---

# 120. 這正是局部／全域分離的重要例子

$$
\boxed{
\text{global parent failure}
\not\Rightarrow
\text{local descendant failure}.
}
$$

---

# 121. AI theorem research 的高風險：語義微錯，生成爆炸

如果 formal target 微妙偏離，

AI 可以非常有效率地生成：

$$
10^3
$$

個局部 proof。

所以 AI 時代：

$$
\text{small specification error}
\times
\text{high generation rate}
$$

會產生巨大污染。

---

# 122. 因此 canonical source 和 provenance 是必要條件

若 source 本身被 silent normalization，

甚至無法知道 parent 何時改變。

所以：

$$
\boxed{
\text{source integrity}
}
$$

也是 productive-mis-specification audit 的基礎。

---

# 123. Research artifact 必須可重建

至少保存：

- exact source；
- version；
- checksum；
- dependency；
- validation；
- revision log。

否則 post-revision audit 不可靠。

---

# 124. 真正的「錯誤價值」是在可逆性

一個錯 parent 若讓所有 descendants 都無法追溯，

價值低。

若每個 descendant 都可追 provenance，

即使 parent 被修正，

仍可 salvage。

所以：

$$
\boxed{
\text{recoverability}
}
$$

是 AI 科學的重要設計原則。

---

# 125. 生產性錯置與語義負熵

如果系統保留：

$$
\text{source}
+
\text{version}
+
\text{dependency}
+
\text{audit},
$$

parent revision 後可以重建哪些知識受影響。

這就是一種：

$$
\text{semantic recoverability}.
$$

---

# 126. 從「證明成功」改成「知識資產組合」

一個研究 run 的結果不應只有：

```text
SOLVED / UNSOLVED
```

而應輸出：

```text
theorem_assets:
obstruction_assets:
tool_assets:
negative_results:
transfer_assets:
revision_risk:
```

---

# 127. 未解 parent 的價值可以被分解

$$
V(P)
=
V_{\mathrm{proof}}
+
V_{\mathrm{desc}}
+
V_{\mathrm{tool}}
+
V_{\mathrm{negative}}
+
V_{\mathrm{transfer}}.
$$

若：

$$
V_{\mathrm{proof}}=0,
$$

不代表：

$$
V(P)=0.
$$

---

# 128. 但未解不能冒充已解

報告必須明示：

$$
\text{parent unresolved}.
$$

這是學術倫理底線。

---

# 129. 形式命題一：Parent Failure Non-Annihilation

$$
\boxed{
\operatorname{Fail}(P)
\not\Rightarrow
\forall d\in\mathcal D(P),
\operatorname{Fail}(d).
}
$$

---

# 130. 形式命題二：Descendant Non-Retrovalidation

$$
\boxed{
\exists d\in\mathcal D(P)
\text{ survives}
\not\Rightarrow
P\text{ valid}.
}
$$

---

# 131. 形式命題三：Audit Requirement

$$
\boxed{
P\rightarrow P'
\Rightarrow
\operatorname{Reaudit}(\mathcal D(P)).
}
$$

---

# 132. 形式命題四：Raw Generativity Non-Productivity

$$
\boxed{
G_{\mathrm{raw}}\uparrow
\not\Rightarrow
\Phi_E\uparrow.
}
$$

---

# 133. 形式命題五：Error Exposure Monotonic Risk

其他條件相同下，

若 descendant 對被撤銷 assumption 的 dependency 增加：

$$
E_i\uparrow,
$$

則 post-revision invalidation risk 不應降低。

這是一個可檢驗的風險命題。

---

# 134. 形式命題六：Scope Repair Preservation

若 model 在 clean domain：

$$
D_c
$$

已被驗證，

只在：

$$
D_e
$$

失效，

則 local correction 不應無理由抹除：

$$
M|_{D_c}.
$$

---

# 135. 形式命題七：Specification Separation

$$
\boxed{
\operatorname{Proof}(Q_F)
\not\Rightarrow
Q_F\equiv Q_I.
}
$$

---

# 136. 形式命題八：Mis-specification Non-Diagnosis

$$
\boxed{
\text{repeated proof failure}
\not\Rightarrow
\operatorname{MisSpecified}(P).
}
$$

---

# 137. 非主張總表

本文不主張：

1. 錯誤問題一般比正確問題有價值；
2. 錯誤越大，生成性越高；
3. AI 應故意錯誤形式化；
4. idealization 等於錯誤研究；
5. model misspecification 等於 category mistake；
6. formalization defect 代表 informal theorem 錯；
7. parent 被修正後 descendants 自動有效；
8. descendant 存活會使 parent 重新變真；
9. 科學史上的 fruitful false theories 證明所有錯理論都值得保留；
10. Carnot 的 caloric ontology 因 fruitful 而正確；
11. phlogiston theory 因促成氧氣研究而正確；
12. NS-203 已證明 Navier--Stokes 問題 framing 有錯；
13. P/NP 已證明存在 category mismatch；
14. AI 證不出來可作為 mis-specification proof；
15. proof-space saturation 可推出 undecidability；
16. descendants 很多就等於 epistemic fertility 高；
17. tool descendant 和 theorem descendant 可用同一真值標準；
18. community consensus 決定 parent truth；
19. 新定義較容易證明就一定優於舊定義；
20. 本文已找到 universal productive-mis-specification law。

---

# 138. 與 LSI-PSD-07 的整合

第 7 篇建立：

$$
T
\neq
G.
$$

本文再建立：

$$
\boxed{
T(P)
\neq
T(d_i).
}
$$

以及：

$$
\boxed{
\text{parent correction}
\neq
\text{corpus annihilation}.
}
$$

---

# 139. 與 LSI-PSD-06 的整合

如果多條 route 匯流到 obstruction：

$$
O,
$$

可能觸發：

$$
\text{parent audit}.
$$

但只有 parent audit 真正發現：

$$
P\rightarrow P'
$$

後，

才進入本文的 descendant survival analysis。

---

# 140. 與 LSI-PSD-05 的整合

一個 saturated basin：

$$
B
$$

若後來被發現依賴錯 parent component，

則：

$$
B
$$

成為 salvage target。

不能整 basin 刪除。

---

# 141. 與 Logic-Space Integration 的整合

錯 parent 也會產生一個研究空間：

$$
\Omega(P).
$$

修正後：

$$
\Omega(P').
$$

重要問題是：

$$
\boxed{
\Omega(P)\cap\Omega(P')
}
$$

有多大。

這個交集就是 descendant survival 的空間版本。

---

# 142. Survivor space

定義：

$$
\Omega_{\mathrm{surv}}
=
\operatorname{Audit}
(
\Omega(P)\cap\Omega(P')
).
$$

---

# 143. Error-only space

$$
\Omega_{\mathrm{err}}
=
\Omega(P)\setminus\Omega_{\mathrm{surv}}.
$$

---

# 144. New-corrected space

$$
\Omega_{\mathrm{new}}
=
\Omega(P')\setminus\Omega(P).
$$

---

# 145. 修正後的三區圖

$$
\boxed{
\Omega(P)\cup\Omega(P')
=
\Omega_{\mathrm{err}}
\cup
\Omega_{\mathrm{surv}}
\cup
\Omega_{\mathrm{new}}.
}
$$

這是下一篇「生產性錯置窗口」的重要幾何基礎。

---

# 146. 研究不應只問 parent 是否錯

更好的問題是：

$$
\boxed{
\text{what survives the correction?}
}
$$

這會把科學史從：

> theory succession

改成：

> knowledge lineage.

---

# 147. AI 科學中的 lineage science

未來 AI 自主研究若持續多年，

最重要的資產可能不是單篇 paper。

而是：

$$
\boxed{
\text{versioned lineage of claims, assumptions, failures, repairs, and survivors}.
}
$$

---

# 148. 結論

生產性錯置不是「替錯誤辯護」的理論。

它首先是一套**錯誤發生之後如何不把真正知識一起丟掉**的方法論。

研究母體：

$$
P
$$

可能因：

- wrong assumption；
- wrong scope；
- missing physics；
- formalization mismatch；
- representation mismatch；
- framing defect；

被修正成：

$$
P'.
$$

這時最粗糙的處理有兩種。

第一種：

> 以前全部錯，全部丟掉。

第二種：

> 以前很 fruitful，所以其實沒錯。

兩者都不合理。

本文提出第三條路：

$$
\boxed{
P\rightarrow P'
\rightarrow
\operatorname{Reaudit}(\mathcal D(P))
\rightarrow
\{
\text{survive},
\text{repair},
\text{transfer},
\text{refute},
\text{unknown}
\}.
}
$$

真正有價值的不是「錯誤」，

而是：

$$
\boxed{
\text{在修正後仍能存活的知識譜系。}
}
$$

這也解釋了科學史上一個反覆出現的現象：

$$
\text{false or limited parent}
$$

可以與：

$$
\text{true or useful descendant}
$$

共存。

但這個共存絕不能被倒轉成：

$$
\text{useful descendant}
\Rightarrow
\text{true parent}.
$$

對 AI 大規模數學研究而言，這個區分會越來越重要。當生成速度上升到：

$$
10^2,
10^3,
10^4
$$

個研究 artifact，

任何小型 parent error 都可能形成大規模 error cascade。

同時，任何過度粗暴的 parent reset 也可能摧毀大量真正可保留的 lemma、tool、obstruction、negative result 與 transfer asset。

因此成熟 AI research infrastructure 必須從：

$$
\text{paper generation}
$$

進入：

$$
\boxed{
\text{revision-aware knowledge lineage management}.
}
$$

本文最後留下兩條互相制衡的原則：

$$
\boxed{
\textbf{A flawed parent can generate knowledge that survives its correction.}
}
$$

以及：

$$
\boxed{
\textbf{No amount of surviving descendant knowledge can retroactively validate the flawed parent.}
}
$$

這兩條同時成立，才是「生產性錯置」真正嚴格的版本。

---

# 參考文獻

1. Frigg, R., & Hartmann, S. **Models in Science.** *Stanford Encyclopedia of Philosophy*. Updated reference entry on scientific modeling, idealization, representation, and model ontology. https://plato.stanford.edu/entries/models-science/

2. Weisberg, M. (2007). **Three Kinds of Idealization.** *The Journal of Philosophy*, 104(12), 639–659.

3. Batterman, R. W., & Rice, C. C. (2014). **Minimal Model Explanations.** *Philosophy of Science*, 81(3), 349–376. https://doi.org/10.1086/676677

4. Norton, J. D. (2022). **How Analogy Helped Create the New Science of Thermodynamics.** *Synthese*, 200, 269.

5. King, M. (2025). **Experiment and the Pursuit of Ugly Models.** *European Journal for Philosophy of Science*, 15, Article 55. https://doi.org/10.1007/s13194-025-00692-y

6. Lepoutre, M. (2025). **Educational Falsehoods.** *Ergo: An Open Access Journal of Philosophy*.

7. Ma, L. et al. (2026). **Physics-guided correction for operator learning under model misspecification.** arXiv:2606.03469.

8. Wang, Y. (2026). **Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy.** arXiv:2606.23215. https://arxiv.org/abs/2606.23215

9. Strouwen, A., & Micluţa-Câmpeanu, S. (2026). **Experimental Design for Missing Physics.** arXiv:2604.01231. https://arxiv.org/abs/2604.01231

10. Strouwen, A. et al. (2026). **Bayesian Symbolic Regression for Missing Physics.** arXiv:2603.14918.

11. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493. https://arxiv.org/abs/2606.29493

12. Wang, E., Chess, S., Lee, D., Ge, S., Mallavarapu, A., & Ilin, V. (2026). **Learning to Repair Lean Proofs from Compiler Feedback.** arXiv:2602.02990.

13. American Chemical Society. **Joseph Priestley, Discoverer of Oxygen — National Historic Chemical Landmark.** Historical resource on oxygen discovery, phlogiston interpretation, and Lavoisier's reinterpretation.

14. Weingarten, K. (2026). **Productive Idealizations for Scientific Understanding: A Case Study in Effective Theories.** PhilSci-Archive preprint.

15. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $P$ | parent problem / theory / model |
| $P'$ | revised parent |
| $\mathcal C$ | parent correction operator |
| $\delta_P$ | parent revision distance |
| $\mathcal D(P)$ | descendants generated under parent $P$ |
| $d_i$ | individual descendant |
| $A_P^{-}$ | removed / invalidated parent assumptions |
| $E_i$ | descendant exposure to parent error |
| $S_D$ | descendant survival ratio |
| $C_D$ | descendant audit coverage |
| $W_O$ | write-off ratio |
| $Z_K$ | zombie-knowledge rate |
| $\Phi_E$ | epistemic fertility |
| $G_A$ | audited generativity |
| $R_D$ | descendant robustness |
| $T_D$ | transferability |
| $\Omega_{\mathrm{surv}}$ | survivor space |
| $\Omega_{\mathrm{err}}$ | error-only space |
| $\Omega_{\mathrm{new}}$ | corrected-new space |

---

## 附錄 B：Parent Revision Record

```yaml
parent_id:
version_from:
version_to:

revision:
  question:
  domain:
  assumptions_added:
  assumptions_removed:
  representation:
  model:
  scope:

reason:
  counterexample:
  specification_audit:
  missing_physics:
  scope_failure:
  category_reformulation:
  other:

affected_descendants:
  total:
  queued_for_reaudit:

status:
  revision_verified:
  independent_review:
```

---

## 附錄 C：Descendant Re-audit Record

```yaml
descendant_id:
parent_version_original:
parent_version_current:

dependency_exposure:
  removed_assumptions:
  changed_definitions:
  changed_domain:
  changed_representation:

verification:
  old_status:
  new_status:

survival:
  class:
    - strong
    - repairable
    - transferred
    - refuted
    - unknown
  repair_cost:
  transfer_target:

provenance:
  source:
  theorem_dependencies:
  tool_dependencies:
  checksum:
```

---

## 附錄 D：最小判定流程

```text
PARENT REVISION DETECTED
        |
        v
Identify changed assumptions / domain / statement
        |
        v
Find all dependent descendants
        |
        v
Re-audit each descendant
        |
        +--> strong survivor
        +--> repairable survivor
        +--> transfer survivor
        +--> refuted
        +--> unknown
        |
        v
Recompute survival / write-off / zombie rates
        |
        v
Update research memory
```

---

## 附錄 E：一句話版本

$$
\boxed{
\text{問題問錯了，不代表研究過程裡得到的每一件事都錯；但那些留下來的東西必須重新證明自己不依賴原來的錯。}
}
$$

這就是生產性錯置的最小形式。


<!-- END LSI-PSD-08 -->

---


<!-- BEGIN LSI-PSD-09 -->

# LSI-PSD-09 — 生產性錯置窗口：真理、錯誤與知識肥沃性的非單調曲線

## The Productive Mis-specification Window: Non-Monotonic Epistemic Fertility Between Fidelity and Error

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 09  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Productive Mis-specification Window Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文提出「生產性錯置窗口」作為**可證偽的經驗性假說族**，不主張所有科學、數學或工程問題都存在 inverted-U 型肥沃性曲線，也不主張偏離真理必然提高創造力。本文特別拒絕「越錯越有用」與「故意把問題問錯可以更接近真理」兩種推論。本文只提出：在某些受約束研究域中，零偏差、高度結構化的有限偏差與大幅隨機偏差，可能具有不同的 audited generativity；若中等程度的**結構化偏差**在 descendant survival、transferability、repairability 與 independent verification 上優於零偏差及隨機偏差，則可說該 domain 在指定任務與研究制度下呈現 productive-mis-specification window。若資料不支持內部高值區，窗口假說應被拒絕。

---

## 摘要

LSI-PSD-07 已指出 truth/fidelity、closure、generativity 與 utility 不必單調同向；LSI-PSD-08 進一步提出，parent problem 被修正後，部分 descendant knowledge 可能經 post-revision audit 存活。本文把這兩個命題推到下一個可測層次：**是否存在一個有限偏差區間，使研究系統的認識論肥沃性高於零偏差與大偏差兩端？**

令某一 domain 中的參照 parent 為：

$$
P^\star,
$$

研究變體為：

$$
P_\epsilon,
$$

並令：

$$
\epsilon
=
d(P_\epsilon,P^\star).
$$

若只用單一距離，會把不同種類的偏差錯誤地混在一起，因此本文將偏差分解為：

$$
\boldsymbol\epsilon
=
(
\epsilon_Q,
\epsilon_D,
\epsilon_A,
\epsilon_L,
\epsilon_M,
\epsilon_R
),
$$

分別表示 question、domain、assumptions、representation、model/method 與 research-regime 的偏移。進一步定義 **Structured Deviation Index**：

$$
\operatorname{SDI}(P_\epsilon)
=
B(\epsilon)
\cdot
L(\epsilon)
\cdot
C(\epsilon)
\cdot
R(\epsilon),
$$

其中 $B$ 為 boundedness、$L$ 為 localization、$C$ 為 comparability、$R$ 為 repairability。任意錯誤可以有大的 $\|\boldsymbol\epsilon\|$，但若：

$$
\operatorname{SDI}\approx0,
$$

它通常不屬於本文所說的 productive deviation。

本文把認識論肥沃性定義為一個多維函數：

$$
\Phi_E
=
\Phi_E(
G_A,
S_D,
T_D,
R_D,
C_D,
Z_K,
C_{\mathrm{cost}}
),
$$

其中：

- $G_A$：audited non-equivalent generativity；
- $S_D$：parent revision 後 descendant survival；
- $T_D$：transferability；
- $R_D$：robustness；
- $C_D$：audit coverage；
- $Z_K$：zombie-knowledge rate；
- $C_{\mathrm{cost}}$：研究成本。

最簡化的 task-conditioned 形式可寫：

$$
\Phi_E^{\mathcal T}
=
\frac{
G_A^\alpha
S_D^\beta
T_D^\gamma
R_D^\eta
C_D^\kappa
}{
(1+\lambda Z_K)
(1+\mu C_{\mathrm{cost}})
}.
$$

本文不把這個公式當作自然定律，而把它當成可審計的 measurement template。

生產性錯置窗口定義為：

$$
\boxed{
\mathcal W_P^{\mathcal T,R}
=
\left\{
\boldsymbol\epsilon:
\Phi_E^{\mathcal T,R}(\boldsymbol\epsilon)
>
\max[
\Phi_E^{\mathcal T,R}(0)+\Delta_0,
\Phi_E^{\mathcal T,R}(\boldsymbol\epsilon_{\mathrm{rand}})+\Delta_r
]
\right\}.
}
$$

也就是：只有當一個有限、結構化、可定位、可修正的偏差，在相同預算下產生更多**可驗證且能在 parent 修正後存活的後代知識**，並顯著勝過零偏差基線與隨機偏差基線，才有資格稱為 productive window。

本文進一步提出四種可能 empirical shape：

1. monotone fidelity-dominant；
2. monotone deviation-dominant；
3. interior-window / inverted-U；
4. multi-peak / phase-structured。

因此 inverted-U 只是候選，不是預設真理。窗口還可能具有 task dependence、representation dependence、budget dependence、model dependence 與 hysteresis。相同偏差：

$$
\boldsymbol\epsilon
$$

對人類、LLM、formal prover 或不同工具鏈，可能落在不同區域。

2025--2026 年的科學哲學與模型發現研究為這一框架提供相鄰證據。Batterman 與 Rice 的 minimal-model work 顯示，解釋力可來自移除微觀細節而暴露大尺度不變結構；King 2025 對「ugly models」的研究強調 pursuit-worthiness 是在有限資源與不完整證據下的研究選擇問題；2026 年 physics-guided operator correction 將 misspecified prior physics 與 learned correction 分開，而不是讓黑箱覆蓋整體物理；LISDD 2026 將 discrepancy 局部化到特定 regime，再回復缺失符號機制；Experimental Design for Missing Physics 與 Bayesian Inference for Missing Physics 進一步把「未知模型結構」變成可主動設計實驗、可量化 posterior uncertainty 的研究對象。這些工作不證明 inverted-U，但共同顯示：**偏差的大小之外，偏差是否結構化、局部化、可比較與可修正，是決定其知識價值的核心變量。**

本文最後提出一組可直接實驗的 benchmark。對已知 ground-truth 系統，逐步注入不同強度與不同類型的偏差：

$$
\boldsymbol\epsilon_0,
\boldsymbol\epsilon_1,
\ldots,
\boldsymbol\epsilon_m,
$$

再讓 AI 生成研究 descendants；最後揭示 ground truth、執行 parent revision、重新 audit 全部 descendants，測：

$$
G_A,
S_D,
T_D,
R_D,
Z_K,
\Phi_E.
$$

若 structured intermediate deviations 穩定產生內部高值區，則支持窗口假說；若零偏差始終最佳，則支持 fidelity-dominant regime；若偏差越大越高，則必須檢查 measurement 是否把 raw novelty 誤當 epistemic value；若不同偏差類型呈多峰結構，則單一 $\epsilon$ 模型應被放棄。

本文最終提出：

$$
\boxed{
\textbf{The epistemically productive region, if it exists, is a structured window, not an invitation to error.}
}
$$

以及：

$$
\boxed{
\textbf{A productive window is established by descendant survival and controlled comparison, not by the sheer volume of generated theory.}
}
$$

**關鍵詞：** 生產性錯置窗口、productive mis-specification window、epistemic fertility、structured deviation、inverted-U、model discrepancy、missing physics、idealization、descendant survival、AI science、proof-space dynamics、research routing

---

# 1. 問題的提出：從「錯誤有時有用」到「到底錯到哪裡才有用」

LSI-PSD-08 已經建立：

$$
\operatorname{Fail}(P)
\not\Rightarrow
\forall d\in\mathcal D(P),
\operatorname{Fail}(d).
$$

但是這個命題還太弱。

因為它只說：

> 錯 parent 的部分 descendants 可能存活。

它沒有回答：

> 什麼種類、什麼強度的偏差最容易產生可存活 descendants？

本文正是處理這個問題。

---

# 2. 一個非常容易被濫用的直覺

從 Carnot、ideal gas、effective theory、minimal model 等案例，很容易產生一句危險話：

> 看吧，錯誤反而更有創造力。

這句話把至少四個不同東西混在一起：

$$
\text{controlled idealization},
$$

$$
\text{limited-domain model},
$$

$$
\text{accidental misspecification},
$$

$$
\text{arbitrary error}.
$$

它們不等價。

---

# 3. 任意錯誤空間遠大於有用錯置空間

如果一個模型有：

$$
n
$$

個自由參數，

任意 perturbation：

$$
\epsilon\in\mathbb R^n
$$

有巨大體積。

真正能：

- 保留主要結構；
- 產生可比較 residual；
- 允許 correction；
- 生成可驗證 descendants；

的偏差只佔其中非常小的部分。

因此：

$$
\boxed{
\text{productive deviation}
\subsetneq
\text{all deviation}.
}
$$

---

# 4. 偏差必須向量化

單一：

$$
\epsilon
$$

太粗。

本文定義：

$$
\boldsymbol\epsilon
=
(
\epsilon_Q,
\epsilon_D,
\epsilon_A,
\epsilon_L,
\epsilon_M,
\epsilon_R
).
$$

其中：

$$
\epsilon_Q
$$

表示問題 statement 偏移；

$$
\epsilon_D
$$

表示 domain / scope 偏移；

$$
\epsilon_A
$$

表示 assumption 偏移；

$$
\epsilon_L
$$

表示 language / representation 偏移；

$$
\epsilon_M
$$

表示 model / method family 偏移；

$$
\epsilon_R
$$

表示 research-regime 偏移。

---

# 5. 同樣的距離，不同方向可以完全不同

假設：

$$
\|\boldsymbol\epsilon_1\|
=
\|\boldsymbol\epsilon_2\|.
$$

但：

$$
\boldsymbol\epsilon_1
=
(0,0,\delta,0,0,0),
$$

只是移除一個非關鍵 assumption。

另一個：

$$
\boldsymbol\epsilon_2
=
(\delta,0,0,0,0,0),
$$

卻改變 theorem quantifier。

兩者 epistemic effect 可能完全不同。

因此：

$$
\boxed{
\|\boldsymbol\epsilon\|
\text{ alone is insufficient}.
}
$$

---

# 6. 偏差方向比偏差大小更重要

定義：

$$
\hat{\epsilon}
=
\frac{
\boldsymbol\epsilon
}{
\|\boldsymbol\epsilon\|
}.
$$

生產性應寫：

$$
\Phi_E
=
\Phi_E(
\|\boldsymbol\epsilon\|,
\hat{\epsilon}
).
$$

這意味着 productive window 不是一條實數線上的 interval，

而可能是一個：

$$
\boxed{
\text{anisotropic region in deviation space}.
}
$$

---

# 7. Structured Deviation Index

為了區分有結構偏差與 random noise，本文定義四個分量。

## 7.1 Boundedness

$$
B(\epsilon)\in[0,1].
$$

偏差是否有限、可描述、非無界漂移。

## 7.2 Localization

$$
L(\epsilon)\in[0,1].
$$

是否知道：

$$
\epsilon
$$

發生在哪個 regime／term／assumption。

## 7.3 Comparability

$$
C(\epsilon)\in[0,1].
$$

是否能與 baseline 或 target 做受控比較。

## 7.4 Repairability

$$
R(\epsilon)\in[0,1].
$$

是否存在合理 correction path。

---

# 8. SDI 定義

$$
\boxed{
\operatorname{SDI}(\epsilon)
=
B(\epsilon)
L(\epsilon)
C(\epsilon)
R(\epsilon).
}
$$

如果任一項接近零：

$$
\operatorname{SDI}\rightarrow0.
$$

---

# 9. 為什麼用乘積而不是加總

若偏差完全不可定位：

$$
L=0,
$$

即使：

$$
B=C=R=1,
$$

也不應叫高 structured deviation。

乘積讓：

$$
\text{critical missing dimension}
$$

直接壓低 SDI。

這是一個工程選擇，不是自然定律。

---

# 10. Random deviation baseline

定義：

$$
\boldsymbol\epsilon_{\mathrm{rand}}
$$

與：

$$
\boldsymbol\epsilon_{\mathrm{struct}}
$$

具有近似相同 norm：

$$
\|\epsilon_{\mathrm{rand}}\|
\approx
\|\epsilon_{\mathrm{struct}}\|.
$$

但前者：

$$
\operatorname{SDI}\approx0.
$$

後者：

$$
\operatorname{SDI}\gg0.
$$

---

# 11. 窗口假說真正比較的不是 0 和 error

而是三組：

$$
\boxed{
\text{baseline}
\quad
\text{structured deviation}
\quad
\text{random deviation}.
}
$$

沒有 random control，

「偏差提高 generativity」幾乎沒有意義。

---

# 12. Epistemic fertility 需要 task conditioning

設任務：

$$
\mathcal T.
$$

例如：

- theorem discovery；
- mechanism discovery；
- engineering approximation；
- explanation；
- transfer；
- experiment design。

則：

$$
\Phi_E
=
\Phi_E^{\mathcal T}.
$$

同一 model 在不同 task 可有不同 productive window。

---

# 13. Research regime conditioning

再加入：

$$
R.
$$

因此：

$$
\boxed{
\Phi_E^{\mathcal T,R}(\epsilon).
}
$$

不同：

- model；
- prover；
- retriever；
- budget；
- memory；
- verifier；

都可能改變曲線。

---

# 14. 生產性窗口的第一版定義

$$
\boxed{
\mathcal W_P^{\mathcal T,R}
=
\left\{
\epsilon:
\Phi_E^{\mathcal T,R}(\epsilon)
>
\tau_\Phi
\right\}.
}
$$

但這還不夠。

因為 baseline 自己可能已經很高。

---

# 15. 相對窗口

更嚴格：

$$
\mathcal W_{P,\mathrm{rel}}^{\mathcal T,R}
=
\left\{
\epsilon:
\Phi_E(\epsilon)
>
\Phi_E(0)+\Delta_0
\right\}.
$$

---

# 16. Random-control window

再要求：

$$
\Phi_E(\epsilon)
>
\mathbb E[
\Phi_E(\epsilon_{\mathrm{rand}})
]
+
\Delta_r.
$$

才可以叫：

$$
\boxed{
\text{productive deviation}.
}
$$

---

# 17. 完整窗口

因此：

$$
\boxed{
\mathcal W_P^{\mathcal T,R}
=
\left\{
\epsilon:
\Phi_E(\epsilon)
>
\max[
\Phi_E(0)+\Delta_0,
\mathbb E\Phi_E(\epsilon_{\mathrm{rand}})+\Delta_r
]
\right\}.
}
$$

---

# 18. 為什麼要加 $\Delta$

若只要求：

$$
\Phi_E(\epsilon)>\Phi_E(0),
$$

微小 sampling noise 都可能造成假窗口。

因此：

$$
\Delta_0,\Delta_r
$$

應由：

- confidence interval；
- permutation；
- bootstrap；
- multiple-testing correction；

決定。

---

# 19. Window 不是一定連通

最簡單想像：

$$
[\epsilon_1,\epsilon_2].
$$

但高維偏差空間可能：

$$
\mathcal W_P
=
W_1\cup W_2\cup W_3.
$$

因此稱「window」只是直觀語言。

數學上更像：

$$
\boxed{
\text{productive region}.
}
$$

---

# 20. 四種基本曲線

## 20.1 Fidelity-dominant

$$
\frac{d\Phi_E}{d\epsilon}<0.
$$

零偏差最好。

## 20.2 Deviation-dominant

在測試範圍內：

$$
\frac{d\Phi_E}{d\epsilon}>0.
$$

這通常需要高度警惕 measurement 問題。

## 20.3 Interior-window

存在：

$$
\epsilon^\star>0
$$

使：

$$
\Phi_E(\epsilon^\star)
>
\Phi_E(0).
$$

## 20.4 Multi-peak

存在多個：

$$
\epsilon_i^\star.
$$

表示不同結構偏差各自開出不同 productive basin。

---

# 21. Inverted-U 只是第三種

所以本文不把：

$$
\cap
$$

形曲線當作預設。

它只是：

$$
\boxed{
H_{\mathrm{window}}.
}
$$

---

# 22. 可證偽條件一

若在多個 domain、model、budget 下：

$$
\Phi_E(0)
\ge
\Phi_E(\epsilon)
$$

對所有結構化偏差都成立，

則 productive-window 假說在該 domain 被拒絕。

---

# 23. 可證偽條件二

若 structured deviation：

$$
\Phi_E(\epsilon_{\mathrm{struct}})
$$

不顯著高於 norm-matched random deviation，

則：

$$
\text{structure hypothesis}
$$

失敗。

---

# 24. 可證偽條件三

若所謂高 generativity 在 parent revision 後：

$$
S_D\rightarrow0,
$$

則原高峰只是：

$$
\boxed{
\text{error amplification peak}.
}
$$

不是 productive window。

---

# 25. 可證偽條件四

若高峰完全由：

$$
G_{\mathrm{raw}}
$$

驅動，

而：

$$
G_A
$$

沒有上升，

窗口應被撤銷。

---

# 26. 可證偽條件五

若 audit coverage：

$$
C_D
$$

過低，

任何 window claim 應標：

$$
\text{underdetermined}.
$$

---

# 27. Fertility vector

不要只用一個 scalar。

定義：

$$
\mathbf F_E
=
(
G_A,
S_D,
T_D,
R_D,
C_D,
1-Z_K,
1-C_{\mathrm{cost}}
).
$$

---

# 28. Scalar 只用於 task-specific ranking

若一定需要：

$$
\Phi_E^{\mathcal T}
=
U_{\mathcal T}(\mathbf F_E).
$$

不同任務：

$$
U_{\mathcal T}
$$

不同。

---

# 29. 一個可用的示範形式

$$
\Phi_E^{\mathcal T}
=
\frac{
G_A^\alpha
S_D^\beta
T_D^\gamma
R_D^\eta
C_D^\kappa
}{
(1+\lambda Z_K)
(1+\mu C_{\mathrm{cost}})
}.
$$

所有 exponent 與 weight 都必須預註冊或做 sensitivity analysis。

---

# 30. 避免事後調權重

如果先看到資料，

再調：

$$
\alpha,\beta,\gamma,\ldots
$$

把曲線調成 inverted-U，

則結果無效。

所以實驗前要：

$$
\boxed{
\text{preregister metric family}.
}
$$

---

# 31. Sensitivity analysis

對多組：

$$
\mathbf w^{(1)},\ldots,\mathbf w^{(m)}
$$

重算。

如果 window 只在單一極端權重出現，

robustness 低。

---

# 32. Window robustness

定義：

$$
R_W
=
P(
\epsilon\in\mathcal W_P
\mid
\text{reasonable metric choices}
).
$$

---

# 33. Window width

若一維：

$$
W
=
\epsilon_{\max}
-
\epsilon_{\min}.
$$

高：

$$
W
$$

表示 productive zone 寬。

---

# 34. Window height

$$
H_W
=
\Phi_E(\epsilon^\star)
-
\Phi_E(0).
$$

---

# 35. Window sharpness

$$
S_W
=
-\frac{
d^2\Phi_E
}{
d\epsilon^2
}
\Bigg|_{\epsilon^\star}.
$$

高 sharpness 表示偏離最佳點後快速失效。

---

# 36. Window directionality

高維下，

不同方向：

$$
\hat\epsilon_j
$$

有：

$$
\Phi_E(r\hat\epsilon_j).
$$

因此要測：

$$
\boxed{
\text{direction-specific windows}.
}
$$

---

# 37. Assumption window

只改：

$$
\epsilon_A.
$$

例如：

- remove；
- weaken；
- strengthen；

一個 assumption。

---

# 38. Representation window

只改：

$$
\epsilon_L.
$$

例如同一 theorem 使用：

- coordinate A；
- coordinate B；
- symbolic A；
- graph representation。

---

# 39. Scope window

改：

$$
\epsilon_D.
$$

例如：

$$
D_{\mathrm{global}}
\rightarrow
D_{\mathrm{local}}.
$$

有時縮小 scope 反而大幅提高可證性與 transfer。

---

# 40. Method window

改：

$$
\epsilon_M.
$$

例如從單一 method family 到 hybrid method。

---

# 41. Regime window

改：

$$
\epsilon_R.
$$

例如：

- verifier；
- budget；
- model；
- memory。

這不是 mathematical mis-specification，

但可幫助分離：

$$
\text{problem effect}
$$

與：

$$
\text{search-system effect}.
$$

---

# 42. 為什麼 regime 也要納入

如果只在一個弱 model 上看到：

$$
\Phi_E(0)
$$

低，

但稍微改題就高，

可能只是：

$$
\boxed{
\text{model capability mismatch}.
}
$$

不是 parent 真的更 productive。

---

# 43. Intelligence-conditioned window

寫：

$$
\mathcal W_P^{(I)}.
$$

不同智能能力：

$$
I_1<I_2
$$

可能有：

$$
\mathcal W_P^{(I_1)}
\neq
\mathcal W_P^{(I_2)}.
$$

---

# 44. 一個反直覺預測

更強的 AI 可能讓 productive window 變窄。

因為：

$$
P^\star
$$

本身已能產生大量 descendants，

不需要透過偏差打開路徑。

---

# 45. 另一個可能

更強 AI 也可能讓窗口變寬。

因為它有能力 salvage：

$$
\text{structured deviations}
$$

中更多 descendants。

所以這是 empirical question。

---

# 46. Budget-conditioned window

$$
\mathcal W_P^{(\mathcal B)}.
$$

小 budget：

$$
\epsilon>0
$$

可能幫助簡化問題。

大 budget：

$$
\epsilon=0
$$

可能重新占優。

---

# 47. 這和 effective theory 很像

在低能或低資源 regime，

effective representation：

$$
T_{\mathrm{eff}}
$$

可能更有操作價值。

這不表示它比 fundamental theory 更真。

---

# 48. Search-cost adjusted fertility

若：

$$
C_{\mathrm{cost}}(\epsilon)
$$

很高，

即使 generativity 高，

也可能不值得 pursue。

所以：

$$
\Phi_E
$$

要做 cost adjustment。

---

# 49. King 2025 與 pursuit-worthiness

King 對「ugly models」的討論提醒：

> 在理論尚未被完整驗證前，科學家還要決定哪個 model 值得花資源追。

這與本文非常接近。

窗口不只是 truth 問題，

也是：

$$
\boxed{
\text{research allocation}.
}
$$

---

# 50. Pursuit value

定義：

$$
V_P(\epsilon)
=
\mathbb E[
\Phi_E(\epsilon)
]
-
C_{\mathrm{research}}(\epsilon).
$$

真正 agent scheduler 應最大化：

$$
V_P,
$$

而不是 raw novelty。

---

# 51. Minimal models 的位置

Minimal model 有時極度移除細節，

所以相對 full target：

$$
\epsilon_L,\epsilon_M
$$

並不小。

但它可以保留：

$$
\text{macro invariants}.
$$

這說明偏差向量必須 task-conditioned。

---

# 52. 如果 task 是 macro explanation

則：

$$
F_{\mathrm{micro}}
$$

低不代表：

$$
F_{\mathrm{macro}}
$$

低。

所以 window 必須以 target scale 定義。

---

# 53. Scale-conditioned window

$$
\mathcal W_P^{(\ell)}.
$$

不同尺度：

$$
\ell
$$

可能有不同 optimum。

---

# 54. Ideal gas 的窗口直覺

在：

$$
\text{low density / moderate pressure}
$$

ideal gas approximation 高效。

靠近 phase transition，

它快速失效。

這不是 generic inverted-U，

而是：

$$
\boxed{
\text{domain-bounded usefulness window}.
}
$$

---

# 55. LISDD 的關鍵啟發

LISDD 不讓 correction：

$$
\Delta f
$$

污染 clean regime。

而是先找：

$$
D_{\mathrm{clean}},
$$

再定位：

$$
D_{\mathrm{error}}.
$$

這恰好是：

$$
\boxed{
\text{structured deviation localization}.
}
$$

---

# 56. Localization 是窗口成立的必要條件之一

如果不知道：

$$
\epsilon
$$

在哪裡，

就無法：

- repair；
- compare；
- transfer；
- determine survival。

---

# 57. Physics-guided operator correction

2026 年 operator correction work 將：

$$
\mathcal G_{\mathrm{true}}
=
\mathcal G_{\mathrm{prior}}
+
\Delta\mathcal G
$$

作為基本結構。

重要的是：

$$
\mathcal G_{\mathrm{prior}}
$$

不被 black-box correction 完全覆蓋。

---

# 58. Prior preservation

這相當於要求：

$$
\text{known-good descendants}
$$

保留。

所以 structured correction 本質上是：

$$
\boxed{
\text{salvage-aware model revision}.
}
$$

---

# 59. Experimental Design for Missing Physics

2026 年相關工作將候選 missing structures：

$$
M_1,\ldots,M_k
$$

作為待區分對象。

下一個實驗由：

$$
\text{which experiment most separates candidates}
$$

決定。

---

# 60. 這是 window science 的重要部分

不是只被動看偏差。

而是主動問：

$$
\boxed{
\text{what intervention best reveals whether this deviation is productive or merely wrong?}
}
$$

---

# 61. Bayesian uncertainty

Bayesian missing-physics work 進一步保留：

$$
P(M_i\mid D).
$$

這提醒窗口不應只有 point estimate：

$$
\epsilon^\star.
$$

而要有：

$$
P(
\epsilon\in\mathcal W_P
\mid D
).
$$

---

# 62. Probabilistic window

$$
\boxed{
\pi_W(\epsilon)
=
P(
\epsilon\in\mathcal W_P
\mid \mathcal D
).
}
$$

---

# 63. Window uncertainty

報：

- posterior；
- confidence interval；
- bootstrap；
- sensitivity。

不要畫一條曲線就宣布哲學定律。

---

# 64. 多峰結構

可能：

$$
\Phi_E
$$

在：

$$
\epsilon_1^\star,
\epsilon_2^\star
$$

有不同 peak。

例如：

- 一個 representation simplification peak；
- 一個 scope restriction peak。

---

# 65. 多峰意味什麼

不是「最佳錯誤只有一種」。

而是：

$$
\boxed{
\text{different structured distortions open different research mechanisms}.
}
$$

---

# 66. Phase transition

如果小幅改變：

$$
\epsilon
$$

讓：

$$
\Phi_E
$$

突然跳變，

可以定義：

$$
\epsilon_c.
$$

這叫：

$$
\text{research phase boundary}.
$$

---

# 67. 不要濫用物理相變

除非有：

- sharp transition；
- scaling；
- finite-size analysis；

否則「phase」只是操作性比喻。

---

# 68. Hysteresis

研究 history 可能使：

$$
P_\epsilon
$$

從：

$$
0\rightarrow\epsilon
$$

和：

$$
\epsilon\rightarrow0
$$

走出不同路徑。

---

# 69. 為什麼會有 hysteresis

因為：

- descendants 已生成；
- memory 已改變；
- tools 已建立；
- vocabulary 已形成；
- obstruction atlas 已更新。

所以即使 parent 修回：

$$
P^\star,
$$

研究系統已不再是原狀態。

---

# 70. Research-history hysteresis

定義：

$$
H_W
=
d(
\Phi_E^{\uparrow}(\epsilon),
\Phi_E^{\downarrow}(\epsilon)
).
$$

---

# 71. 這是一個非常重要的 AI 預測

一個 temporary mis-specification 可能永久改變：

$$
\mathcal H.
$$

即使後來修正，

生成的 tool、lemma、taxonomy 仍留在 memory。

---

# 72. 這就是 descendant legacy

$$
\boxed{
\text{parent correction}
\neq
\text{history erasure}.
}
$$

---

# 73. Window 可以依賴研究順序

如果先走：

$$
P_0\rightarrow P_{\epsilon_1}\rightarrow P^\star,
$$

與直接：

$$
P_0\rightarrow P^\star,
$$

最後 generative assets 不一定一樣。

---

# 74. Counterfactual research histories

因此可比較：

$$
\mathcal H_A
$$

與：

$$
\mathcal H_B.
$$

這是未來 AI 多分支研究很適合做的實驗。

---

# 75. Forked-history window experiment

從同一 checkpoint：

$$
H_0
$$

建立：

- exact branch；
- structured-deviation branch；
- random-deviation branch。

保持：

$$
\text{budget}
$$

相同。

---

# 76. 最後揭示 ground truth

所有 branch 都轉回：

$$
P^\star.
$$

再測：

$$
\text{what knowledge survived}.
$$

這是本文最乾淨的實驗之一。

---

# 77. Window 和 creativity 的關係

本文避免把：

$$
\Phi_E
$$

叫 creativity。

因為 creativity 包含：

- novelty；
- surprise；
- aesthetics；
- usefulness。

本文只測：

$$
\boxed{
\text{epistemic fertility}.
}
$$

---

# 78. 新奇不是窗口證據

如果：

$$
\nu(\epsilon)
$$

隨 $\epsilon$ 單調增加，

完全可能只是越錯越新奇。

真正要看：

$$
S_D,
R_D,T_D.
$$

---

# 79. Error-amplification peak

有時：

$$
G_{\mathrm{raw}}
$$

在大偏差時最高。

這反而可能形成：

$$
\boxed{
\text{hallucination peak}.
}
$$

---

# 80. 雙曲線診斷

同時畫：

$$
G_{\mathrm{raw}}(\epsilon)
$$

與：

$$
\Phi_E(\epsilon).
$$

如果：

$$
G_{\mathrm{raw}}\uparrow
$$

但：

$$
\Phi_E\downarrow,
$$

說明系統進入錯誤擴增區。

---

# 81. Survivor-adjusted generativity

$$
G_S(\epsilon)
=
G_A(\epsilon)
S_D(\epsilon).
$$

這是非常實用的第一版指標。

---

# 82. Transfer-adjusted generativity

$$
G_{ST}(\epsilon)
=
G_A
S_D
T_D.
$$

---

# 83. Cost-adjusted

$$
G_{STC}
=
\frac{
G_A S_D T_D
}{
1+C_{\mathrm{cost}}
}.
$$

---

# 84. Zombie penalty

$$
G_{STCZ}
=
\frac{
G_A S_D T_D
}{
(1+C_{\mathrm{cost}})
(1+\lambda Z_K)
}.
$$

---

# 85. 為什麼 zombie penalty 重要

一個偏差可能產生很多 surviving assets，

但同時留下大量 invalid active knowledge。

管理成本巨大。

所以：

$$
\Phi_E
$$

應扣分。

---

# 86. Window 的治理成本

AI 長程研究中，

偏差越大，

post-revision audit cost：

$$
C_{\mathrm{audit}}
$$

可能越高。

---

# 87. Audit-cost adjusted window

所以：

$$
\Phi_E'
=
\Phi_E
-
\lambda C_{\mathrm{audit}}.
$$

一個「很 fertile 但修一次要花十倍成本」的窗口未必值得追。

---

# 88. Decision-theoretic pursuit

如果研究目標是最大化期望知識收益：

$$
a^\star
=
\arg\max_a
\mathbb E[
\Phi_E(a)
-
C(a)
].
$$

---

# 89. Window 不等於應故意進入

即使存在：

$$
\epsilon^\star>0,
$$

也不一定值得人工製造。

因為：

- ethical cost；
- time；
- contamination；
- publication risk；
- downstream misuse。

所以：

$$
\boxed{
\text{descriptive window}
\neq
\text{normative recommendation}.
}
$$

---

# 90. 何時可以故意使用 controlled deviation

只有在：

- synthetic benchmark；
- sandbox；
- simulation；
- formal toy model；
- reversible branch；

等可隔離環境。

---

# 91. Production science 中應優先避免 silent error

真實科研系統應標：

$$
\text{deliberate perturbation}.
$$

不能偷偷改 parent。

---

# 92. Window experiment 必須 provenance-complete

每個 branch 保存：

- exact parent；
- exact delta；
- model；
- prompts；
- tools；
- budget；
- descendants；
- verification。

---

# 93. Ground-truth benchmark family

最適合先做的是：

1. 已知 ODE / PDE toy systems；
2. 可機器驗證 theorem；
3. synthetic formalization defects；
4. known combinatorial problems；
5. symbolic-regression systems。

---

# 94. 為什麼不能先用真正未知難題驗證

如果用 NS、P/NP：

$$
P^\star
$$

本身未知。

就無法知道：

$$
\epsilon=0
$$

在哪裡。

因此不能乾淨估窗口。

---

# 95. 所以 NS-203 只能做 observational case

不能作 ground-truth proof。

可以測：

- local closure proxy；
- generativity；
- descendant transfer；
- basin escape。

但不能標：

$$
\epsilon_{\mathrm{truth}}.
$$

---

# 96. NS-203 可做 representation perturbation

在不改 Clay statement 的前提下，

可以改：

$$
\epsilon_L,
\epsilon_M,
\epsilon_R.
$$

例如：

- continuous-only route；
- geometric route；
- recurrence route；
- proof-assistant route。

---

# 97. 這些不是「把 NS 問錯」

只是：

$$
\boxed{
\text{different search representations}.
}
$$

所以 epistemic risk 比直接改 theorem statement 低。

---

# 98. NS observational window

可定義：

$$
\mathcal W_{\mathrm{obs}}
$$

只表示：

> 哪些 representation/method perturbations 在相同 budget 下產生更多 audited reusable assets。

不能叫 truth window。

---

# 99. P/NP 同理

可以比較：

- circuit；
- proof complexity；
- algebraic；
- descriptive；
- geometric；

等 representation。

但不應從哪條 route 更 fertile 推出：

$$
P=NP
$$

或：

$$
P\neq NP.
$$

---

# 100. Window 和 undecidability 的關係

沒有直接關係。

$$
\Phi_E(\epsilon)
$$

曲線不能推出：

$$
\operatorname{Independent}(Q).
$$

---

# 101. Window 和 category error 的關係

若某個重新 framing：

$$
Q'
$$

帶來高：

$$
\Phi_E,
$$

只能提高：

$$
\operatorname{Priority}(\text{compare }Q,Q').
$$

不能直接說：

$$
Q\text{ category error}.
$$

---

# 102. Framing comparison protocol

至少比較：

$$
\operatorname{Map}(Q,Q'),
$$

$$
\operatorname{Loss}(Q\rightarrow Q'),
$$

$$
G_A,
S_D,
T_D,
C_{\mathrm{proof}}.
$$

---

# 103. 如果 $Q'$ 只是更弱

那麼容易證明完全不奇怪。

必須明示：

$$
Q\Rightarrow Q'
$$

但：

$$
Q'\not\Rightarrow Q.
$$

---

# 104. Window 不能靠弱化結論作弊

所以加入：

$$
F_Q
=
\text{question fidelity}.
$$

若：

$$
F_Q\downarrow
$$

太多，

則 fertility 要受 penalty。

---

# 105. Question-fidelity penalty

$$
\Phi_E^{\mathrm{adj}}
=
\Phi_E
\cdot
F_Q^\xi.
$$

---

# 106. 一個重要特殊情況

如果：

$$
Q'
$$

不是要替代 $Q$，

而是從 $Q$ 產生的子問題，

則不需要要求：

$$
F_Q\approx1.
$$

但必須改標：

$$
\text{descendant problem},
$$

不是 reformulation。

---

# 107. 問題分裂也可能形成 productive region

一個太大的 parent：

$$
Q
$$

拆成：

$$
Q_1,\ldots,Q_n.
$$

如果每個 $Q_i$ 產生高 quality descendants，

這是：

$$
\boxed{
\text{decomposition fertility}.
}
$$

---

# 108. Decomposition 與 mis-specification 不同

如果 parent 本來就合理，

只是 decomposition 更有效，

不能叫 parent mis-specified。

所以 classification 要嚴格。

---

# 109. Productive simplification

有些 case 更適合叫：

$$
\text{productive simplification}.
$$

不是：

$$
\text{mis-specification}.
$$

---

# 110. Productive distortion

若明知不真但保留某結構，

叫：

$$
\text{productive idealization/distortion}.
$$

---

# 111. Productive misspecification

只有：

> 原本被當作足夠描述，後來發現有系統缺陷，

才最適合這個詞。

---

# 112. Productive framing anomaly

若問題切法本身後來被替換，

可另標：

$$
\text{productive reframing}.
$$

---

# 113. 因此第 9 篇的 window 是上位框架

它可以包含：

- idealization window；
- simplification window；
- misspecification window；
- reframing window。

但 metadata 要分型。

---

# 114. Window Type

```yaml
window_type:
  - idealization
  - simplification
  - model_misspecification
  - scope_shift
  - representation_shift
  - method_shift
  - reframing
```

---

# 115. Window 比較必須 type-matched

不要拿：

$$
\text{representation shift}
$$

與：

$$
\text{wrong quantifier}
$$

混成同一 $\epsilon$ 曲線。

---

# 116. Multi-axis experiment

真正完整的設計：

$$
\Phi_E(
\epsilon_A,
\epsilon_L,
\epsilon_D,\ldots
).
$$

可以畫 response surface。

---

# 117. Interaction effects

偏差可能交互：

$$
\epsilon_A\epsilon_L.
$$

例如：

> 一個弱化 assumption 只有在新 representation 下才 fruitful。

---

# 118. 二階 response surface

可建：

$$
\Phi_E
=
\beta_0
+
\sum_i\beta_i\epsilon_i
+
\sum_{i<j}\beta_{ij}\epsilon_i\epsilon_j
+
\cdots.
$$

---

# 119. 不預設 polynomial truth

這只是統計 surrogate。

必要時可用：

- Gaussian process；
- spline；
- monotonic model；
- Bayesian response surface。

---

# 120. Sample efficiency

高維 window search 很貴。

所以需要 adaptive experiment design。

這與 2026 missing-physics experimental design 又接起來。

---

# 121. Active window search

每輪選：

$$
\epsilon_{t+1}
$$

最大化：

$$
\text{expected information gain}.
$$

---

# 122. 不要最大化 fertility 本身

如果只挑目前最高：

$$
\Phi_E,
$$

會過度 exploit。

應平衡：

$$
\text{uncertainty reduction}.
$$

---

# 123. Bayesian window mapping

建 posterior：

$$
P(
\Phi_E(\epsilon)
\mid
D_t
).
$$

下一點選：

$$
\epsilon^\star
=
\arg\max
\operatorname{EIG}(\epsilon).
$$

---

# 124. Window discovery 成為科學問題

這時候我們不是在「鼓勵錯誤」。

而是在：

$$
\boxed{
\text{測量研究系統對偏差的響應曲面}.
}
$$

---

# 125. AI 可以做這件事的原因

AI 可以：

- 大量 parallel branches；
- exact provenance；
- automatic re-audit；
- formal verification；
- controlled perturbation。

這是傳統人類科學史很難做的。

---

# 126. 科學史是 observational

Carnot 等案例是：

$$
\text{one realized path}.
$$

我們看不到完整 counterfactual：

> 如果 Carnot 沒採 caloric theory，會怎樣？

---

# 127. AI sandbox 可以做 counterfactual histories

同一 ground truth，

平行啟動：

$$
H_1,H_2,\ldots,H_m.
$$

這是非常新的實驗可能性。

---

# 128. Historical counterfactual benchmark

可以用已知科學史問題：

- thermodynamics toy reconstruction；
- oxygen chemistry toy world；
- celestial models；
- fluid models。

建立不同 parent assumptions。

---

# 129. 但不能假裝重演真歷史

只叫：

$$
\text{historically inspired synthetic benchmark}.
$$

---

# 130. Window 和 multi-agent science

不同 agent 分配不同：

$$
\epsilon_i.
$$

可以形成：

$$
\text{deviation portfolio}.
$$

---

# 131. Portfolio allocation

總 budget：

$$
B.
$$

分配：

$$
b_0,b_1,\ldots,b_m.
$$

其中：

$$
b_0
$$

給 baseline，

其他給 perturbations。

---

# 132. Portfolio objective

$$
\max
\mathbb E[
\text{total surviving knowledge}
].
$$

---

# 133. Exploration hedge

即使 baseline 看起來最好，

仍可給小比例 budget：

$$
b_{\mathrm{explore}}>0.
$$

防止局部 lock-in。

---

# 134. 這和 LSI-PSD-05 的 basin allocation 接軌

第 5 篇分配：

$$
\text{agents across basins}.
$$

第 9 篇分配：

$$
\text{agents across controlled deviations}.
$$

兩者可以合併。

---

# 135. Basin × deviation matrix

$$
A_{ij}
=
\text{budget on basin }B_i
\text{ under deviation }\epsilon_j.
$$

---

# 136. 這會很快爆炸

所以需要 meta-controller：

$$
\Pi_{\mathrm{meta}}.
$$

---

# 137. Meta-controller input

$$
(
C_{\mathrm{sat}},
\Phi_E,
R_W,
C_{\mathrm{ind}},
\Gamma_{\mathrm{esc}},
\operatorname{SDI}
).
$$

---

# 138. Meta-controller output

$$
\{
\text{continue exact},
\text{perturb},
\text{repair},
\text{revert},
\text{branch},
\text{kill branch}
\}.
$$

---

# 139. Revertability 是窗口實驗的安全條件

所有 deliberate deviation branch 必須：

$$
\boxed{
\text{reversible}.
}
$$

---

# 140. Canonical parent 不被覆寫

保留：

$$
P^\star_{\mathrm{canonical}}.
$$

perturbation 只建立：

$$
P_{\epsilon}^{\mathrm{branch}}.
$$

---

# 141. 這也符合 source-integrity 原則

正式 source 不能因實驗 branch 被 silent rewrite。

---

# 142. Window experiment 的最小資料格式

```yaml
experiment_id:
ground_truth_parent:
task:
regime:
budget:

branch:
  epsilon_vector:
  deviation_type:
  structured_deviation_index:
  random_control_matched_norm:
  provenance:

outputs:
  raw_descendants:
  audited_descendants:
  survivor_descendants:
  transfer_descendants:
  zombie_knowledge:
  cost:

metrics:
  fertility_vector:
  scalar_fertility:
  uncertainty:
```

---

# 143. 實驗一：1D assumption sweep

選一個已知 theorem。

建立：

$$
A_\lambda
$$

逐步：

- weaken；
- strengthen；
- remove。

測：

$$
\Phi_E(\lambda).
$$

---

# 144. 實驗二：representation sweep

同一 theorem 語義等價，

改：

$$
L_1,\ldots,L_m.
$$

這裡：

$$
F_Q=1.
$$

最乾淨地測：

$$
\text{representation productivity}.
$$

---

# 145. 實驗三：scope sweep

對物理模型：

$$
D_1\subset D_2\subset\cdots.
$$

測 model residual、missing mechanism 與 descendants。

---

# 146. 實驗四：missing-physics magnitude sweep

ground truth：

$$
f^\star=f_0+\lambda g.
$$

研究 model 只給：

$$
f_0.
$$

改變：

$$
\lambda.
$$

---

# 147. 預測

若：

$$
\lambda\approx0,
$$

residual 太小，

難以產生 mechanism discovery。

中等：

$$
\lambda
$$

容易辨識。

太大：

$$
f_0
$$

失去 useful prior。

這是很自然的 inverted-U 候選。

---

# 148. 實驗五：random missing physics control

用相同：

$$
\|\lambda g\|
$$

但：

$$
g_{\mathrm{rand}}.
$$

比較：

$$
\Phi_E.
$$

---

# 149. 實驗六：formalization defect sweep

逐步注入：

- missing hypothesis；
- quantifier flip；
- translation simplification；
- vacuity。

讓 prover 研究，

最後 repair。

---

# 150. 測量 survivor assets

- proof tactics；
- helper lemma；
- counterexample；
- formalization tool；
- theorem descendants。

---

# 151. 實驗七：proof-space branch portfolio

對同一已知 hard theorem：

- exact branch；
- representation branch；
- method branch；
- weakened-assumption branch；
- random branch。

固定：

$$
B.
$$

---

# 152. 最終比較

$$
\Phi_E^{(0)},
\Phi_E^{(1)},
\ldots.
$$

---

# 153. 何時可以說有窗口

至少：

1. 多 seed；
2. 多 model；
3. 相同 budget；
4. audited descendants；
5. ground truth；
6. random control；
7. post-revision survival；
8. uncertainty interval；
9. preregistered metric。

---

# 154. Window Evidence Level 0

只有直覺或單案例。

---

# 155. Level 1

一個 synthetic benchmark 有 interior peak。

---

# 156. Level 2

多 seeds、同一 domain 重現。

---

# 157. Level 3

多模型重現。

---

# 158. Level 4

跨不同 benchmark family 重現。

---

# 159. Level 5

存在理論模型解釋：

$$
\text{why the window emerges}.
$$

即使 Level 5 也不代表 universal law。

---

# 160. Window collapse

當 model intelligence 提高，

可能：

$$
W\rightarrow0.
$$

這叫：

$$
\text{window collapse}.
$$

---

# 161. Window expansion

若新工具提高 salvageability：

$$
W\uparrow.
$$

---

# 162. Window migration

最佳點：

$$
\epsilon^\star
$$

隨：

- budget；
- model；
- domain；

移動。

---

# 163. Window topology

高維下可研究：

- connected components；
- holes；
- ridges；
- saddle points。

但這屬未來 empirical geometry。

---

# 164. 不應過早拓樸神秘化

先有：

$$
\text{reliable data}.
$$

再談 topology。

---

# 165. 與「越是真理越可能是廢話」的真正關係

零偏差端：

$$
\epsilon=0
$$

如果 parent 已高度 closure，

可能：

$$
G_{\mathrm{theory}}
$$

低。

---

# 166. 但 application generativity 可能高

所以：

$$
\Phi_E
$$

未必低。

這再一次說明 window 依 task。

---

# 167. 如果 task 是「發明新理論」

中間偏差可能高。

如果 task 是「可靠控制」

零偏差可能高。

所以不能跨 task 比。

---

# 168. 真理不是被窗口取代

窗口只描述：

$$
\text{research productivity landscape}.
$$

不是：

$$
\text{truth landscape}.
$$

---

# 169. Window 和真理的關係仍由 verification 決定

descendants 最終必須：

$$
\operatorname{Verify}(d_i).
$$

---

# 170. 這是防止哲學滑坡的最後一道門

不能從：

$$
\Phi_E(\epsilon^\star)>\Phi_E(0)
$$

推出：

$$
P_{\epsilon^\star}
$$

比：

$$
P^\star
$$

更真。

---

# 171. 非主張總表

本文不主張：

1. 所有 domain 都存在 productive window；
2. inverted-U 是普遍形狀；
3. 中等錯誤必然最好；
4. 科學家應故意相信錯誤理論；
5. 任意偏差可提升創造力；
6. generativity 可以取代 truth；
7. $\epsilon^\star>0$ 表示偏差模型比真模型更正確；
8. minimal model 一定位於 productive window；
9. effective theory 一定比 fundamental theory 更有用；
10. LISDD 已證明 productive-mis-specification window；
11. physics-guided correction 已證明真理—生成性反轉；
12. NS-203 可以提供真實 $\epsilon$ 軸；
13. NS 或 P/NP 已被證明 framing 有錯；
14. AI 反覆失敗可以推出 undecidability；
15. random novelty 可當 epistemic fertility；
16. high raw output 可當 window evidence；
17. parent revision 後未 audit descendants 可算 survivors；
18. 一個歷史案例足以建立因果曲線；
19. window 存在就表示應主動製造錯誤；
20. 本文已完成 productive-window 的 empirical proof。

---

# 172. 形式命題一：Norm Insufficiency

$$
\boxed{
\|\epsilon_1\|
=
\|\epsilon_2\|
\not\Rightarrow
\Phi_E(\epsilon_1)
=
\Phi_E(\epsilon_2).
}
$$

---

# 173. 形式命題二：Raw Novelty Non-Window

$$
\boxed{
\nu(\epsilon)\uparrow
\not\Rightarrow
\epsilon\in\mathcal W_P.
}
$$

---

# 174. 形式命題三：Survival Requirement

若：

$$
S_D(\epsilon)\approx0,
$$

則高：

$$
G_{\mathrm{raw}}
$$

不能建立 productive window。

---

# 175. 形式命題四：Random-Control Requirement

如果：

$$
\Phi_E(\epsilon_{\mathrm{struct}})
\le
\mathbb E\Phi_E(\epsilon_{\mathrm{rand}}),
$$

則 structured-deviation superiority 不成立。

---

# 176. 形式命題五：Task Dependence

$$
\boxed{
\mathcal W_P^{\mathcal T_1}
\neq
\mathcal W_P^{\mathcal T_2}
}
$$

在一般情況下是允許的。

---

# 177. 形式命題六：Regime Dependence

$$
\boxed{
\mathcal W_P^{R_1}
\neq
\mathcal W_P^{R_2}.
}
$$

---

# 178. 形式命題七：Descriptive–Normative Separation

$$
\boxed{
\epsilon\in\mathcal W_P
\not\Rightarrow
\text{one ought to introduce }\epsilon.
}
$$

---

# 179. 形式命題八：Window Non-Truth

$$
\boxed{
\epsilon^\star
=
\arg\max\Phi_E
\not\Rightarrow
\epsilon^\star
=
\arg\max T.
}
$$

---

# 180. 形式命題九：Structured Deviation Hypothesis

在部分 domain 中可能存在：

$$
\operatorname{SDI}(\epsilon_1)
>
\operatorname{SDI}(\epsilon_2)
$$

且：

$$
\|\epsilon_1\|
\approx
\|\epsilon_2\|,
$$

同時：

$$
\Phi_E(\epsilon_1)
>
\Phi_E(\epsilon_2).
$$

這是可實驗檢驗的核心假說。

---

# 181. 形式命題十：History Dependence

$$
\boxed{
\Phi_E(\epsilon\mid H_1)
\neq
\Phi_E(\epsilon\mid H_2)
}
$$

是可能的。

---

# 182. 與 LSI-PSD-08 的整合

第 8 篇回答：

> parent 被修正後，哪些 descendants 存活？

第 9 篇回答：

> 不同種類與強度的偏差，會不會系統性改變 survivor production rate？

所以：

$$
S_D
$$

從 outcome 指標變成 response surface 的一部分。

---

# 183. 與 LSI-PSD-07 的整合

第 7 篇：

$$
T\neq G.
$$

第 9 篇進一步：

$$
G
=
G(\epsilon,\mathcal T,R,H).
$$

即 generativity 本身是條件性的。

---

# 184. 與 LSI-PSD-05 的整合

局部 basin saturation 可能觸發：

$$
\text{controlled deviation probe}.
$$

不是為了改 truth，

而是探測：

$$
\text{whether neighboring research regions are more fertile}.
$$

---

# 185. 與 LSI-PSD-06 的整合

高 confluence obstruction：

$$
O^\star
$$

可以成為 perturbation design 的目標。

例如：

- 改 representation；
- 改 assumption；
- 改 scope。

看哪種 perturbation 能真正繞開 $O^\star$ 且留下 survivors。

---

# 186. 與 Logic-Space Integration 的整合

對每個偏差：

$$
\epsilon
$$

都有一個 proof-space：

$$
\Omega(P_\epsilon).
$$

窗口研究比較：

$$
\Omega(P_{\epsilon_1}),
\Omega(P_{\epsilon_2}),
\ldots.
$$

---

# 187. Cross-space survivor map

對：

$$
P_{\epsilon_i}
\rightarrow P^\star
$$

計算：

$$
\Omega_{\mathrm{surv}}^{(i)}
=
\operatorname{Audit}
(
\Omega(P_{\epsilon_i})
\cap
\Omega(P^\star)
).
$$

---

# 188. Window 的空間版本

$$
\epsilon^\star
=
\arg\max
\operatorname{Value}
(
\Omega_{\mathrm{surv}}^{(i)}
).
$$

這比 raw paper count 精確得多。

---

# 189. Knowledge density

定義：

$$
D_K(\epsilon)
=
\frac{
|\Omega_{\mathrm{surv}}(\epsilon)|
}{
C_{\mathrm{cost}}(\epsilon)
}.
$$

---

# 190. Novel survivor density

若 quotient 後：

$$
N_K(\epsilon)
=
\frac{
|\Omega_{\mathrm{surv}}(\epsilon)/\sim|
}{
C_{\mathrm{cost}}
}.
$$

---

# 191. Transfer survivor density

$$
T_K(\epsilon)
=
\frac{
|\Omega_{\mathrm{transfer}}(\epsilon)|
}{
C_{\mathrm{cost}}
}.
$$

---

# 192. Window scorecard

真正觀測站應同時報：

```text
deviation vector
deviation type
SDI
raw generation
audited generation
survival ratio
transfer ratio
zombie rate
cost
fertility confidence interval
window membership probability
```

---

# 193. 研究系列至此的相變

前六篇主要研究：

$$
\text{how proof search behaves}.
$$

第七、八、九篇開始研究：

$$
\text{how truth, error, correction, and generation interact}.
$$

這使 LSI-PSD 從 theorem-search observatory 進入：

$$
\boxed{
\text{empirical epistemology of AI research}.
}
$$

---

# 194. 為什麼這不是純哲學

因為所有主要量都可以在 synthetic / formal benchmark 中直接記錄：

$$
\epsilon,
G_A,
S_D,
T_D,
R_D,
C_D,
Z_K,
C_{\mathrm{cost}}.
$$

---

# 195. 為什麼這也不是單純機器學習 benchmark

因為核心問題不是：

$$
\text{accuracy}.
$$

而是：

$$
\boxed{
\text{what kind of research history produces durable knowledge under later correction?}
}
$$

---

# 196. 這個問題以前很難實驗

人類科學史只有一條 realized history。

AI 可以平行跑：

$$
10^2
$$

條 counterfactual research histories。

---

# 197. 但必須避免把 AI sandbox 當真歷史

我們測的是：

$$
\text{research-system dynamics}.
$$

不是重演 Galileo、Carnot 或 Lavoisier 真正心理史。

---

# 198. 未來最重要的 benchmark

本文建議建立：

$$
\boxed{
\text{Productive Mis-specification Benchmark Suite}
}
$$

簡稱：

$$
\text{PMW-Bench}.
$$

---

# 199. PMW-Bench 類別

1. theorem perturbation；
2. model misspecification；
3. scope mismatch；
4. representation shift；
5. missing physics；
6. formalization defect；
7. controlled random error。

---

# 200. 每個 benchmark 都要有 ground truth

否則：

$$
S_D
$$

無法可靠算。

---

# 201. 每個 benchmark 都要可修正

需要：

$$
P_\epsilon
\rightarrow P^\star.
$$

否則無法做 descendant survival audit。

---

# 202. 每個 benchmark 都要有 matched random control

這是本篇最重要的新要求之一。

---

# 203. 每個 benchmark 都要有 cost log

否則高 fertility 可能只是花了更多資源。

---

# 204. 每個 benchmark 都要有 provenance

否則 survivors 無法追 ancestor。

---

# 205. 每個 benchmark 都要有 canonical source

否則 parent perturbation 不可重放。

---

# 206. 結論

「錯誤有時很有用」是一句太寬鬆、也太容易被濫用的話。

真正值得研究的不是：

$$
\text{error}
$$

本身，

而是：

$$
\boxed{
\text{structured, bounded, localizable, comparable, repairable deviation}.
}
$$

本文把這些條件壓成：

$$
\operatorname{SDI}.
$$

再把研究產出從 raw novelty 改成：

$$
\Phi_E,
$$

也就是：

$$
\text{audited generation}
+
\text{descendant survival}
+
\text{transfer}
+
\text{robustness}
-
\text{zombie knowledge}
-
\text{cost}.
$$

只有當有限偏差：

$$
\epsilon
$$

在 matched budget、matched norm、random-control 與 post-revision audit 下，穩定產生：

$$
\Phi_E(\epsilon)
>
\Phi_E(0),
$$

才有資格談：

$$
\boxed{
\text{productive mis-specification window}.
}
$$

而且即使窗口存在，它依然只是：

$$
\boxed{
\text{research productivity property}.
}
$$

它不是：

$$
\boxed{
\text{truth property}.
}
$$

因此本文既拒絕：

> 越精確一定越有知識產出。

也拒絕：

> 越錯反而越好。

真正可能成立的是一個更細緻的命題：

$$
\boxed{
\textbf{For some tasks and research regimes, epistemic fertility may peak inside a structured deviation region rather than at either perfect fidelity or uncontrolled error.}
}
$$

但這個命題只有在：

- controlled perturbation；
- ground truth；
- random control；
- independent audit；
- descendant survival；
- uncertainty estimation；

全部存在時，才有科學地位。

因此「生產性錯置窗口」最終不是錯誤哲學。

它是一個新的實驗問題：

$$
\boxed{
\textbf{How does the rate of durable knowledge production respond to controlled changes in the way a problem is represented, constrained, and searched?}
}
$$

而這個問題，正是 AI 長程研究第一次有機會大規模、可重放、可分支地真正測量的問題之一。

---

# 參考文獻

1. Batterman, R. W., & Rice, C. C. (2014). **Minimal Model Explanations.** *Philosophy of Science*, 81(3), 349–376. https://doi.org/10.1086/676677

2. Rice, C. (2021). **Leveraging Distortions: Explanation, Idealization, and Universality in Science.** MIT Press.

3. King, M. (2025). **Experiment and the Pursuit of Ugly Models.** *European Journal for Philosophy of Science*, 15, Article 55. https://doi.org/10.1007/s13194-025-00692-y

4. Ma, L. et al. (2026). **Physics-guided correction for operator learning under model misspecification.** arXiv:2606.03469. https://arxiv.org/abs/2606.03469

5. Wang, Y. (2026). **Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy.** arXiv:2606.23215. https://arxiv.org/abs/2606.23215

6. Strouwen, A., & Micluţa-Câmpeanu, S. (2026). **Experimental Design for Missing Physics.** arXiv:2604.01231. https://arxiv.org/abs/2604.01231

7. Strouwen, A. (2026). **Bayesian Inference for Missing Physics.** arXiv:2603.14918. https://arxiv.org/abs/2603.14918

8. Ebers, M. R., Steele, K. M., & Kutz, J. N. (2022). **Discrepancy Modeling Framework: Learning missing physics, modeling systematic residuals, and disambiguating between deterministic and random effects.** arXiv:2203.05164; later SIAM publication.

9. Zou, Z. et al. (2024). **Correcting model misspecification in physics-informed neural networks for discovery of governing equations.** *Journal of Computational Physics*.

10. Mohammadian, M. (2026). **Theoretical Virtues, Truth, and the Epistemic Aim of Scientific Theorizing.** *Philosophy of Science*.

11. Weingarten, K. (2026). **Productive Idealizations for Scientific Understanding: A Case Study in Effective Theories.** PhilSci-Archive preprint.

12. Spagnesi, L. (2025). **Truth, Understanding, and Normativity in Scientific Models.** *Synthese*, 206.

13. Norton, J. D. (2022). **How Analogy Helped Create the New Science of Thermodynamics.** *Synthese*, 200, 269.

14. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $P^\star$ | 參照 parent / ground-truth parent |
| $P_\epsilon$ | 帶控制偏差的 parent |
| $\boldsymbol\epsilon$ | 多維 deviation vector |
| $\hat\epsilon$ | deviation direction |
| $\operatorname{SDI}$ | Structured Deviation Index |
| $\Phi_E$ | epistemic fertility |
| $G_A$ | audited generativity |
| $S_D$ | descendant survival |
| $T_D$ | descendant transferability |
| $R_D$ | descendant robustness |
| $C_D$ | descendant audit coverage |
| $Z_K$ | zombie-knowledge rate |
| $C_{\mathrm{cost}}$ | research cost |
| $\mathcal W_P$ | productive-mis-specification window / region |
| $W$ | window width |
| $H_W$ | window height |
| $S_W$ | window sharpness |
| $\pi_W$ | probabilistic window membership |
| $\Omega_{\mathrm{surv}}$ | survivor proof/knowledge space |

---

## 附錄 B：最小 PMW-Bench protocol

```text
1. Choose a system with known ground truth.
2. Freeze canonical parent source.
3. Define one deviation axis.
4. Create:
   - exact baseline
   - structured deviations at several magnitudes
   - norm-matched random deviations
5. Equalize research budget.
6. Run independent research branches.
7. Collect all descendants with provenance.
8. Reveal / restore ground truth.
9. Re-audit every descendant.
10. Compute:
    G_A
    S_D
    T_D
    R_D
    C_D
    Z_K
    cost
11. Estimate uncertainty.
12. Test whether any interior structured region
    significantly exceeds both baselines.
13. Replicate across seeds and models.
```

---

## 附錄 C：Window Evidence Card

```yaml
domain:
task:
research_regime:
ground_truth_available:

deviation_axis:
deviation_type:
structured_deviation_index:

baseline:
  fertility:
  uncertainty:

random_control:
  norm_matched:
  fertility:
  uncertainty:

candidate_window:
  lower:
  upper:
  peak:
  width:
  height:
  robustness:

descendant_audit:
  coverage:
  survival:
  transfer:
  zombie_rate:

replication:
  seeds:
  models:
  benchmark_families:

status:
  - unsupported
  - preliminary
  - replicated
  - cross-domain
```

---

## 附錄 D：四種典型結果

### A. Fidelity-dominant

$$
\Phi_E(0)
>
\Phi_E(\epsilon)
\quad
\forall\epsilon>0.
$$

結論：

> 沒有 productive window。

### B. Structured interior window

$$
\exists\epsilon^\star>0:
\Phi_E(\epsilon^\star)
>
\Phi_E(0),
$$

且：

$$
\Phi_E(\epsilon^\star)
>
\Phi_E(\epsilon^\star_{\mathrm{rand}}).
$$

結論：

> 支持 productive-window hypothesis。

### C. Random-error domination

$$
\Phi_E(\epsilon_{\mathrm{rand}})
\ge
\Phi_E(\epsilon_{\mathrm{struct}}).
$$

結論：

> 「結構化偏差」假說未獲支持；檢查 metric。

### D. Raw novelty peak but survivor collapse

$$
G_{\mathrm{raw}}\uparrow,
$$

但：

$$
S_D\downarrow.
$$

結論：

> error amplification，而非 epistemic fertility。

---

## 附錄 E：一句話版本

$$
\boxed{
\text{真正值得研究的不是「錯一點會不會更有創意」，而是「哪一種可控偏差，能在修正後留下最多仍然成立的知識」。}
}
$$


<!-- END LSI-PSD-09 -->

---


<!-- BEGIN LSI-PSD-10 -->

# LSI-PSD-10 — 飽和不是判決：證明空間非結論原則

## Saturation Is Not a Verdict: The Proof-Space Non-Conclusion Principle

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 10  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 系列認識論防火牆論文 / Epistemic Firewall and Verdict-Ladder Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文的核心任務不是證明任何特定未解數學問題，而是限制長程 AI 數學研究可以從搜尋資料推出什麼、不能推出什麼。本文明確不主張 Navier--Stokes、P/NP、Riemann Hypothesis 或其他未解問題因 AI 長期搜尋失敗而為假、不可證、獨立、不可判定、定義錯誤或範疇錯置。本文允許把 representation anomaly、method insufficiency、resource insufficiency、formalization mismatch、framing anomaly 與 relative independence 列為診斷候選，但任何一項要升格為數學結論，都需要與其類型相匹配的獨立證書。**搜尋制度的飽和是對搜尋制度的證據，不是對數學實在的判決。**

---

## 摘要

當 AI 在同一個數學問題上連續生成數百、數千乃至更多 research artifacts，並逐步出現語義去重、高階採樣、局部 basin saturation、obstruction confluence 與低 audited novelty yield 時，一個極具誘惑力的推論會出現：

> 如果我們幾乎把能想到的路都走完了，仍然沒有證明，那麼問題是不是錯了、不可證、不可判定，或根本問錯了？

本文的答案是：**不能這樣推出。**

固定問題 $Q$ 與搜尋制度：

$$
R
=
(
\mathcal A,
\mathcal L,
\mathcal M,
\mathcal V,
\mathcal B,
\mathcal H
),
$$

其中 $\mathcal A$ 為背景公理與理論、$\mathcal L$ 為表示語言、$\mathcal M$ 為方法族、$\mathcal V$ 為 verifier / audit system、$\mathcal B$ 為資源上限、$\mathcal H$ 為研究歷史。即使在 $R$ 下得到高度飽和標記：

$$
S_K(Q\mid R)=1,
$$

也只意味：

> 在目前可觀測、可表達、可搜尋、可驗證的制度 $R$ 中，前 $K$ 階研究空間呈現低新增率與高重訪／匯流。

它不蘊含：

$$
\neg Q,
$$

不蘊含：

$$
Q\text{ is unprovable},
$$

不蘊含：

$$
\operatorname{Independent}_{\mathcal A}(Q),
$$

不蘊含：

$$
\operatorname{Undecidable}(Q),
$$

也不蘊含：

$$
\operatorname{Misframed}(Q).
$$

本文把這一限制正式稱為：

$$
\boxed{
\textbf{Proof-Space Non-Conclusion Principle}
}
$$

中文為：

**證明空間非結論原則。**

其核心形式是：

$$
\boxed{
\operatorname{Saturation}(Q\mid R)
\not\models
\operatorname{Verdict}(Q).
}
$$

本文進一步建立三級認識論架構：

$$
\boxed{
\text{Observation}
\rightarrow
\text{Diagnostic Hypothesis}
\rightarrow
\text{Mathematical Verdict}.
}
$$

第一層包括 no-proof-found、recurrence、local saturation、cross-regime confluence、novelty decay 等可測現象；第二層包括 method bottleneck、representation bottleneck、resource bottleneck、formalization mismatch、statement anomaly、relative-independence candidate 等診斷候選；第三層則只接受具有相應證書的結論，例如 proof certificate、counterexample certificate、relative-independence certificate、undecidability reduction、formal inconsistency certificate、faithfulness failure certificate 或 reformulation equivalence theorem。

本文提出一個 **Verdict Ladder**。從最低到最高依序為：

$$
V_0:
\text{No proof found},
$$

$$
V_1:
\text{Repeated failure / recurrence},
$$

$$
V_2:
\text{Local or order-conditioned saturation},
$$

$$
V_3:
\text{Cross-regime robust saturation},
$$

$$
V_4:
\text{Certified route-family no-go},
$$

$$
V_5:
\text{Mathematical verdict certificate}.
$$

其中 $V_0$ 至 $V_3$ 都只是研究觀測；$V_4$ 是對明確量化之方法族、表示族或 route class 的形式結果；只有 $V_5$ 才能對原命題的真偽、反例、相對獨立性或不可判定性提出嚴格結論。

2025--2026 年 formal theorem proving 的發展正好顯示，這些層次不能混在一起。LeanProgress 將「離 proof 完成還有多遠」作為搜尋輔助訊號，說明單步 verifier success 與全局 progress 不等價；APRIL 把失敗 proof、compiler diagnostic、repair 與 explanation 對齊，說明失敗本身可以被修復而不是直接升格成 theorem-level diagnosis；Learned Interventions in Lean 4 grind 顯示，某些 stock solver failure 可以被有限 lookahead rescue，且靜態失敗預測甚至可能不優於 random，說明「當前 heuristic 失敗」不能推出「路線不存在」；LeanMarathon 顯示 long-horizon formalization 會遭遇 statement drift、dependency tangle 與 repair contamination；2026 benchmark defect audit 則進一步指出 kernel-verified proof 並不保證 formal statement 忠實表示原 intended problem；Beyond Compilation 在 graduate-level statement formalization 中觀察到高 compilation rate 與顯著較低 semantic-faithfulness rate 的差距；T² theorem testing 又說明 generated theorem 的 compile success 與其在 downstream successor theorems 中保持語義可用性並非同一件事。這些工作共同支持本文的核心分層：

$$
\boxed{
\text{search success/failure},
\text{formal validity},
\text{semantic fidelity},
\text{mathematical truth}
}
$$

是不同判定層。

本文也區分數學中常被混用的四個詞：

$$
\text{false},
\quad
\text{unprovable in }T,
\quad
\text{independent of }T,
\quad
\text{undecidable}.
$$

對一個形式理論 $T$ 和句子 $\varphi$，相對獨立性要求：

$$
T\nvdash\varphi
$$

且：

$$
T\nvdash\neg\varphi,
$$

並且通常需要對 $T$ 的一致性等條件做明確相對化。這和「我們試了很多 proof 沒找到」在邏輯地位上完全不同。類似地，演算法不可判定性需要 reduction、diagonalization 或其他形式證明；不能由 empirical search exhaustion 替代。

本文最後提出 **Certificate Matching Principle**：

$$
\boxed{
\text{Every strong verdict must be matched by a verdict-specific certificate.}
}
$$

例如：

- 要說「為真」：需要 proof / valid model-theoretic argument；
- 要說「為假」：需要 counterexample 或 proof of negation；
- 要說「相對 $T$ 獨立」：需要 independence result；
- 要說「問題不可判定」：需要 undecidability proof；
- 要說「formalization 不忠實」：需要 faithfulness audit / counterexample / semantic mismatch；
- 要說「新定義更好」：需要 mapping、equivalence / implication relation、實用增益與獨立檢驗；
- 要說「舊問題問錯」：需要比「新問題比較好用」更強的 formal or semantic diagnosis。

對 NS-203 與未來類似 corpus，本文因此主張最強可允許的自動報告語法應是：

$$
\boxed{
\text{Current regime saturated; cause unresolved.}
}
$$

而不是：

$$
\boxed{
\text{Problem is wrong.}
}
$$

本文最終將整個系列的 epistemic firewall 壓縮為一句：

$$
\boxed{
\textbf{Saturation is evidence about a search regime, not a verdict on mathematical reality.}
}
$$

**關鍵詞：** 證明空間非結論原則、proof-space saturation、search regime、non-conclusion、mathematical verdict、independence、undecidability、formalization fidelity、proof certificate、counterexample、AI mathematics、epistemic firewall

---

# 1. 問題的提出：長程 AI 研究最危險的不是失敗，而是過度解讀失敗

假設 AI 在問題：

$$
Q
$$

上研究：

$$
N=10^4
$$

輪。

沒有得到正式 proof。

直覺上會說：

> 這麼多輪都沒有，可能真的有問題。

作為：

$$
\text{research suspicion},
$$

這句可以接受。

作為：

$$
\text{mathematical conclusion},
$$

不能接受。

---

# 2. 觀察事實的最弱形式

目前資料最多直接給：

$$
E_0
=
\text{No accepted proof was found under regime }R.
$$

這是一個歷史／實驗性陳述。

它不是：

$$
\neg Q.
$$

---

# 3. Search Regime

定義：

$$
R
=
(
\mathcal A,
\mathcal L,
\mathcal M,
\mathcal V,
\mathcal B,
\mathcal H,
\Pi
),
$$

其中額外加入：

$$
\Pi
=
\text{search policy}.
$$

---

# 4. 為什麼一定要把 $R$ 寫出來

因為：

$$
\operatorname{Fail}(Q\mid R_1)
$$

與：

$$
\operatorname{Fail}(Q\mid R_2)
$$

可能完全不同。

換：

- model；
- theorem library；
- proof assistant；
- representation；
- method；
- budget；

都會改變結果。

---

# 5. 「AI 證不出來」其實是不完整句子

完整應寫：

$$
\boxed{
\text{AI system }A
\text{ under regime }R
\text{ did not find an accepted proof within budget }B.
}
$$

這才可審計。

---

# 6. No-proof-found 不是 unprovability

形式上：

$$
\boxed{
\operatorname{NoProofFound}(Q\mid R,B)
\not\Rightarrow
\operatorname{Unprovable}(Q).
}
$$

---

# 7. 第一個核心原則

$$
\boxed{
\textbf{Search Failure Non-Entailment Principle}
}
$$

即：

$$
\text{search failure}
\not\models
\text{mathematical failure}.
$$

---

# 8. 為什麼這不是保守過頭

因為搜尋是：

$$
\text{procedure}.
$$

數學真值是：

$$
\text{semantic / formal property}.
$$

兩者層級不同。

---

# 9. 搜尋越多，證據確實可能變強

本文不是說：

> 做一萬輪和做一輪一樣。

當：

$$
N\uparrow,
$$

而且：

- route diversity 高；
- regime diversity 高；
- audited novelty 下降；
- obstacle confluence 高；

我們對：

$$
\text{current regime difficulty}
$$

的信心可以上升。

---

# 10. 但 evidence strength 不等於 entailment

$$
\boxed{
\text{strong evidence}
\neq
\text{logical implication}.
}
$$

這是整篇論文的核心。

---

# 11. 三層結構

本文建立：

$$
\boxed{
O
\rightarrow
H
\rightarrow
V.
}
$$

其中：

$$
O=\text{Observation},
$$

$$
H=\text{Diagnostic Hypothesis},
$$

$$
V=\text{Verdict}.
$$

---

# 12. Observation layer

包括：

- no proof found；
- low novelty；
- recurrence；
- confluence；
- timeout；
- verifier errors；
- basin saturation；
- cross-regime repetition。

---

# 13. Diagnostic layer

包括：

- method insufficiency；
- representation insufficiency；
- resource insufficiency；
- premise insufficiency；
- formalization mismatch；
- statement anomaly；
- search-policy pathology；
- independence candidate。

---

# 14. Verdict layer

包括：

- proven true；
- proven false；
- counterexample；
- independent relative to $T$；
- undecidable problem class；
- formally inconsistent specification；
- formally equivalent reformulation。

---

# 15. 不能直接跳層

禁止：

$$
O\rightarrow V
$$

除非存在與 verdict 相匹配的 certificate。

---

# 16. Epistemic Firewall

定義：

$$
\boxed{
\mathcal F_E:
O
\not\Rightarrow
V.
}
$$

所有 diagnosis：

$$
H
$$

都必須保持 provisional。

---

# 17. Verdict Ladder

本文提出六級。

---

# 18. $V_0$：No Proof Found

$$
V_0:
\quad
\operatorname{NoProofFound}(Q\mid R,B).
$$

這是最低層。

---

# 19. $V_1$：Repeated Failure

$$
V_1:
\quad
\operatorname{Recurrence}(Q\mid R).
$$

多次失敗具有相似結構。

---

# 20. $V_2$：Local Saturation

$$
V_2:
\quad
S_K(B\mid R)=1.
$$

某 proof basin 在前 $K$ 階低 audited yield。

---

# 21. $V_3$：Cross-Regime Robust Saturation

多個：

$$
R_1,\ldots,R_m
$$

都出現飽和。

但必須做 genealogy correction。

---

# 22. $V_4$：Certified Route-Family No-Go

存在 theorem：

$$
\forall r\in\mathcal R_C,
\quad
r\not\Rightarrow Q.
$$

這才是真正形式化的「這一類路不行」。

---

# 23. $V_5$：Mathematical Verdict Certificate

例如：

$$
T\vdash Q,
$$

或：

$$
T\vdash\neg Q,
$$

或正式 independence / undecidability result。

---

# 24. Ladder 的核心限制

$$
V_3
\not\Rightarrow
V_4.
$$

$$
V_4
\not\Rightarrow
V_5.
$$

---

# 25. 一百個 empirical no-go 不等於一個 quantified no-go theorem

即使：

$$
r_1,\ldots,r_{100}
$$

都失敗，

不能推出：

$$
\forall r\in\mathcal R.
$$

---

# 26. 量詞偷渡

這是長程 AI research 最危險的邏輯錯誤之一：

$$
\text{many observed}
\rightarrow
\text{all possible}.
$$

---

# 27. Observed route set

$$
\mathcal R_{\mathrm{obs}}
\subseteq
\mathcal R_{\mathrm{possible}}.
$$

即使：

$$
|\mathcal R_{\mathrm{obs}}|
$$

很大，

仍不代表：

$$
\mathcal R_{\mathrm{obs}}
=
\mathcal R_{\mathrm{possible}}.
$$

---

# 28. 語言外部的 route

甚至可能：

$$
r^\star
\notin
\mathcal L.
$$

也就是目前表示語言根本無法表達真正的 proof architecture。

---

# 29. Method-external route

也可能：

$$
r^\star
\notin
\mathcal M.
$$

需要新數學。

---

# 30. Resource-external route

也可能：

$$
C(r^\star)\gg B.
$$

只是目前算不動。

---

# 31. Intelligence-external route

也可能現有模型根本不會生成：

$$
r^\star.
$$

---

# 32. Premise-external route

也可能：

$$
p^\star
$$

不在當前 theorem library。

---

# 33. 因此 saturation 最強的自動報告

應是：

$$
\boxed{
\text{Observed regime saturation detected. Cause unresolved.}
}
$$

---

# 34. 不應自動報告

```text
UNPROVABLE
INDEPENDENT
MALFORMED
WRONG QUESTION
```

除非有 certificate。

---

# 35. Hypothesis set

給定 saturation evidence：

$$
E_S,
$$

至少保留以下 hypotheses。

---

# 36. $H_1$：True but hard

$$
Q\text{ true},
$$

proof 尚未找到。

---

# 37. $H_2$：False but counterexample unseen

$$
Q\text{ false},
$$

但反例未找到。

---

# 38. $H_3$：Method bottleneck

$$
\mathcal M
$$

不足。

---

# 39. $H_4$：Representation bottleneck

$$
\mathcal L
$$

不足。

---

# 40. $H_5$：Resource bottleneck

$$
B
$$

不足。

---

# 41. $H_6$：Premise / library bottleneck

缺：

$$
p^\star.
$$

---

# 42. $H_7$：Formalization mismatch

$$
Q_F
\not\equiv
Q_I.
$$

---

# 43. $H_8$：Statement / framing anomaly

原問題切割存在可疑處。

仍是 candidate。

---

# 44. $H_9$：Relative independence

對指定：

$$
T,
$$

可能：

$$
T\nvdash Q,
\quad
T\nvdash\neg Q.
$$

需要 formal proof。

---

# 45. $H_{10}$：Search-instrument artifact

問題在：

- retriever；
- evaluator；
- heuristic；
- benchmark；
- memory。

---

# 46. 單一 saturation evidence 同時相容多個 hypothesis

所以：

$$
E_S
$$

不是 discriminating evidence 的終點。

下一步應是：

$$
\boxed{
\text{design interventions that separate hypotheses}.
}
$$

---

# 47. Bayesian 語言可以使用，但不能偽造機率

形式上：

$$
P(H_i\mid E)
\propto
P(E\mid H_i)P(H_i).
$$

---

# 48. 但沒有 calibrated likelihood 就不要寫 87%

AI 很容易憑感覺說：

> 80% 是 framing 問題。

這不應出現在 serious observatory。

---

# 49. 更誠實的輸出

```text
SUPPORTED HYPOTHESES:
  method bottleneck: plausible
  representation bottleneck: plausible
  framing anomaly: unresolved
  independence: no certificate
```

---

# 50. Diagnostic discrimination

對：

$$
H_3
$$

做 method switch。

對：

$$
H_4
$$

做 representation switch。

對：

$$
H_5
$$

做 budget escalation。

對：

$$
H_6
$$

做 global premise retrieval。

---

# 51. 對 $H_7$ 做 faithfulness audit

比較：

$$
Q_I
$$

與：

$$
Q_F.
$$

---

# 52. 對 $H_8$ 做 reformulation comparison

需要：

$$
Q\leftrightarrow Q'
$$

的 mapping。

---

# 53. 對 $H_9$ 不能靠更多 brute-force search

要走：

$$
\boxed{
\text{metamathematical route}.
}
$$

---

# 54. True / False / Unprovable / Independent / Undecidable 的分離

這五個詞必須嚴格區分。

---

# 55. False

相對標準語義：

$$
Q
$$

不成立。

若是 universal statement，

一個 counterexample 可能足夠。

---

# 56. Unprovable in $T$

$$
T\nvdash Q.
$$

這是**相對形式系統**的概念。

不要寫：

$$
Q\text{ absolutely unprovable}.
$$

除非語義已精確定義。

---

# 57. Independent of $T$

$$
T\nvdash Q
$$

且：

$$
T\nvdash\neg Q.
$$

通常還需清楚交代：

- $T$ 的一致性；
- 模型論條件；
- 相對一致性結果。

---

# 58. Undecidable sentence 的語義歧義

有時「undecidable in $T$」被用來指：

$$
T\nvdash Q
\land
T\nvdash\neg Q.
$$

這和：

$$
\text{algorithmic undecidability}
$$

不同。

---

# 59. Algorithmic undecidability

對 decision problem：

$$
D,
$$

沒有演算法：

$$
A
$$

對所有輸入都正確停機判定。

這需要 Turing-style / reduction-style proof。

---

# 60. Search exhaustion 不能替代 reduction

$$
10^{100}
$$

次失敗也不是：

$$
\text{undecidability proof}.
$$

---

# 61. Gödel 式 incompleteness 不是萬用免責

不能因為 Gödel 存在就說：

> 所有難問題可能都不可判定。

不成立。

---

# 62. Incompleteness 是形式結果

它對足夠強、一致、可有效公理化的系統給出特定限制。

不是：

$$
\text{hard problem}
\Rightarrow
\text{Gödel}.
$$

---

# 63. Turing 不可判定性也不是 proof-search 失敗的同義詞

同樣：

$$
\text{cannot solve now}
\neq
\text{no algorithm exists}.
$$

---

# 64. Independence certificate

一個相對 independence claim 至少需要：

$$
C_{\mathrm{indep}}
$$

能被獨立核查。

---

# 65. 可能形式

例如：

- model construction；
- forcing；
- relative consistency；
- proof-theoretic argument；
- interpretation。

不是：

> 大家很多年沒證出來。

---

# 66. Proof certificate

若要說：

$$
Q\text{ true}
$$

在形式數學 context 中，最強證書是：

$$
\Pi_Q.
$$

verifier 檢查：

$$
\operatorname{Check}(\Pi_Q,Q)=1.
$$

---

# 67. 但形式 proof 還有 statement fidelity 問題

即使：

$$
\operatorname{Check}(\Pi,Q_F)=1,
$$

仍需：

$$
Q_F\equiv Q_I.
$$

---

# 68. 這是 2026 benchmark audit 的重要教訓

machine-checked：

$$
\neq
$$

automatically faithful.

---

# 69. Beyond Compilation 的直接警告

一個 statement 可以：

$$
\text{compile}
$$

但：

- 少 hypothesis；
- 改 domain；
- 變 vacuous。

所以：

$$
\boxed{
\text{compilation validity}
\neq
\text{semantic faithfulness}.
}
$$

---

# 70. Theorem testing 的補充

T² 類工作用 downstream successor theorem：

$$
S_1,\ldots,S_k
$$

測 generated theorem 是否維持語義可用性。

---

# 71. 這說明 correctness 可以有 integration layer

就像軟體：

$$
\text{unit pass}
\neq
\text{system pass}.
$$

formal math 也可能：

$$
\text{declaration compiles}
\neq
\text{theory remains coherent}.
$$

---

# 72. 所以 proof certificate stack

更完整：

$$
\boxed{
\Pi
+
F_S
+
D_C
}
$$

其中：

$$
F_S
=
\text{statement fidelity audit},
$$

$$
D_C
=
\text{dependency consistency}.
$$

---

# 73. Counterexample certificate

若：

$$
Q=\forall x\in D,\ P(x),
$$

找到：

$$
x^\star\in D
$$

且：

$$
\neg P(x^\star),
$$

則：

$$
x^\star
$$

是直接反例證書。

---

# 74. 但 domain 必須對

如果：

$$
x^\star\notin D,
$$

不是反例。

---

# 75. Formalization counterexample

有時反例只打到：

$$
Q_F,
$$

不打到：

$$
Q_I.
$$

所以仍要 fidelity audit。

---

# 76. Misframing certificate 是什麼

「問題問錯」比「命題為假」更模糊。

本文要求拆成具體類型。

---

# 77. Type A：Inconsistency

assumptions：

$$
A
$$

自身推出：

$$
\bot.
$$

這是真正 formal defect。

---

# 78. Type B：Vacuity

結論因前提不可能成立而 trivially true。

---

# 79. Type C：Domain mismatch

問題聲稱判：

$$
D_1,
$$

形式上卻實際判：

$$
D_2.
$$

---

# 80. Type D：Quantifier mismatch

$$
\exists
$$

與：

$$
\forall
$$

混淆。

---

# 81. Type E：Criterion mismatch

把：

$$
\text{formal proof criterion}
$$

與：

$$
\text{empirical adequacy}
$$

混成同一 truth criterion。

---

# 82. Type F：Representation artifact

問題的障礙只由某 representation 產生，

且等價表示消除。

---

# 83. 只有這些具體問題被建立後

才有資格說：

$$
\text{specific framing defect}.
$$

不是泛泛：

> 我覺得定義不好。

---

# 84. Better definition 不是 automatically correct

若新定義：

$$
D'
$$

比較漂亮，

不能推出舊定義：

$$
D
$$

錯。

---

# 85. Definition comparison needs mapping

至少：

$$
f:D\rightarrow D'
$$

或：

$$
g:D'\rightarrow D.
$$

---

# 86. 等價 reformulation

最強：

$$
Q\Leftrightarrow Q'.
$$

---

# 87. 嚴格弱化

若：

$$
Q\Rightarrow Q'
$$

但反向不成立，

必須明示：

$$
Q'
$$

較弱。

---

# 88. 嚴格強化

若：

$$
Q'\Rightarrow Q,
$$

則：

$$
Q'
$$

較強。

---

# 89. Practical superiority

即使不是等價，

新 framing 可能：

- 更可計算；
- 更可驗證；
- 更能連接現象；
- 更能產生工具。

這可說：

$$
U(Q')>U(Q).
$$

---

# 90. 但 utility 不等於 truth

$$
\boxed{
U(Q')>U(Q)
\not\Rightarrow
Q\text{ was wrong}.
}
$$

---

# 91. Community consensus 的角色

數學真值不由共識定義。

---

# 92. 但公共學術地位需要共同檢驗

一個「新定義取代舊問題」的強主張，

至少需要：

- independent reproduction；
- review；
- theorem checking；
- community scrutiny。

---

# 93. 所以共識是 institutional certificate

不是：

$$
T(Q).
$$

而是：

$$
A_{\mathrm{comm}}(Q)
=
\text{accepted research status}.
$$

---

# 94. Formal truth 與 practical proof 的分離

使用者說的「實用性證明」可以被精確化。

本文定義：

$$
\boxed{
\text{Practical Proof Stack}
}
$$

---

# 95. 第一層：Formal validity

$$
\Pi\vdash Q.
$$

---

# 96. 第二層：Statement fidelity

$$
Q_F\equiv Q_I
$$

在可接受審計下。

---

# 97. 第三層：Reproducibility

獨立環境重跑。

---

# 98. 第四層：Dependency integrity

proof 不依賴 hidden inconsistency / unsound axiom。

---

# 99. 第五層：Usability

結果能被後續 theorem、計算、工程或科學使用。

---

# 100. 第六層：Independent scrutiny

他者可檢驗。

---

# 101. 這些都不改變真理的本體地位

但決定：

$$
\text{research community can safely use the result}.
$$

---

# 102. Saturation evidence 的 Bayesian 合理用法

可以說：

> saturation makes some hypotheses worth testing.

---

# 103. 不能說

> saturation proves the most dramatic hypothesis.

---

# 104. Evidence allocation

若：

$$
E_S
$$

出現，

可增加資源到：

- representation audit；
- premise audit；
- counterexample search；
- method diversification；
- metamathematical investigation。

---

# 105. 這就是 saturation 的真正功能

$$
\boxed{
\text{routing signal}
}
$$

而不是：

$$
\boxed{
\text{truth oracle}.
}
$$

---

# 106. Search policy artifact：Learned Interventions 的啟發

2026 年 Lean 4 grind 研究顯示：

stock heuristic timeout 後，

bounded lookahead 可以 rescue 一些原本失敗的 theorem。

---

# 107. 因此：

$$
\operatorname{Fail}(Q\mid\Pi_1)
$$

不代表：

$$
\operatorname{Fail}(Q\mid\Pi_2).
$$

---

# 108. 更有意思的是靜態預測失敗

某些 feature-based policy 在 rescuable split failures 上不優於 random。

這說明：

$$
\text{failure cause}
$$

可能是 runtime property，

不是 static property。

---

# 109. 這直接反對一種過度診斷

看到某些 feature：

> 這題一定走不通。

可能根本沒有足夠 evidence。

---

# 110. APRIL 的啟發

失敗 proof：

$$
e
$$

可以經 compiler feedback：

$$
c
$$

被修：

$$
e\rightarrow e'.
$$

---

# 111. 所以 failure 是可轉換狀態

不是終局 verdict。

---

# 112. LeanProgress 的啟發

proof state：

$$
s_t
$$

可以估：

$$
\hat d(s_t)
=
\text{remaining steps}.
$$

---

# 113. 這說明「沒完成」內部仍有 progress geometry

不是只有：

$$
0/1.
$$

---

# 114. LeanMarathon 的啟發

長程 formalization failure 可能來自：

- stale context；
- statement drift；
- dependency corruption。

---

# 115. 這些是研究制度問題

不是 theorem truth 問題。

---

# 116. Formal benchmark defects 的啟發

如果 benchmark 本身有：

- counterexample；
- vacuity；
- unsound axiom；
- translation defect；

prover score 會被污染。

---

# 117. 這證明 search result 依賴 target quality

$$
\boxed{
\text{bad target}
\rightarrow
\text{bad inference from search metrics}.
}
$$

---

# 118. Cross-regime saturation

若：

$$
R_1,\ldots,R_m
$$

都 saturation，

證據確實更強。

---

# 119. 但 independence 需要修正

如果所有 regime：

- 同一 model family；
- 同一 corpus；
- 同一 assumptions；
- 同一 retriever；

則不是真正獨立。

---

# 120. Regime genealogy

定義：

$$
d_R(R_i,R_j).
$$

越相似，

有效獨立權重越低。

---

# 121. Cross-regime evidence mass

可定義：

$$
E_{\mathrm{cross}}
=
\sum_i
w_i S_K(Q\mid R_i).
$$

---

# 122. 仍然不能叫 verdict probability

除非有 calibrated generative model of hypotheses。

---

# 123. Cross-regime saturation 的合理作用

提高：

$$
\operatorname{Priority}(
\text{meta-level investigation}
).
$$

---

# 124. Meta-level investigation 包括

- new axioms；
- new representation；
- independence route；
- definition audit；
- counterexample route。

---

# 125. Formal route-family no-go

如果真的證明：

$$
\forall r\in\mathcal R_C,
\quad
\neg\operatorname{Closes}(r,Q),
$$

那可以說：

> 這一族路徑不行。

---

# 126. 但仍不能說所有路不行

除非：

$$
\mathcal R_C
=
\mathcal R_{\mathrm{all}}
$$

本身被證明。

通常不可能輕易做到。

---

# 127. Proof-method no-go 的價值

即使不解 $Q$，

它可以大幅縮小搜尋空間。

這是：

$$
\text{negative proof asset}.
$$

---

# 128. Stop condition

當：

$$
V_3
$$

成立，

系統可以停止：

$$
\text{same-regime brute force}.
$$

---

# 129. 但不是停止研究問題

而是：

$$
\boxed{
\text{change regime}.
}
$$

---

# 130. 自動停止語法

```text
STOP CURRENT REGIME
REASON:
  local/cross-regime saturation

NOT CLAIMED:
  theorem false
  theorem unprovable
  independence
  undecidability
  malformed problem
```

---

# 131. NS-203 應如何報告

目前最合理：

> Some local proof basins exhibit higher-order resampling and obstruction recurrence; global cause remains unresolved.

---

# 132. 不應報告

> NS is probably malformed because AI cannot prove it.

---

# 133. 即使未來達到一萬篇

仍然同理。

数量：

$$
N
$$

不能自動改變 logical type。

---

# 134. N 可以提高 empirical confidence

但不能把：

$$
\text{empirical}
$$

變：

$$
\text{deductive}.
$$

---

# 135. P/NP 也同理

即使大量方法都卡：

$$
\text{natural proofs},
\text{relativization},
\text{algebrization},
\ldots
$$

每個 formal barrier 都只限制特定方法類。

---

# 136. Barrier result 的正確作用

不是：

> P vs NP 不可解。

而是：

> 這類 proof technique 有形式障礙。

---

# 137. 方法障礙累積可以導向新方法

這正是：

$$
\text{negative knowledge}
\rightarrow
\text{research routing}.
$$

---

# 138. 對「定義範疇可能有錯」的正確地位

可標：

$$
H_{\mathrm{frame}}.
$$

---

# 139. 什麼會提高 $H_{\mathrm{frame}}$ 的研究優先級

- repeated cross-representation obstruction；
- statement ambiguity；
- scope mismatch；
- operational criterion conflict；
- better reformulation with mapping。

---

# 140. 什麼不能直接證明 $H_{\mathrm{frame}}$

- 很多年沒解；
- AI 很多輪沒解；
- 文章很多；
- 大家覺得難；
- proof search 很慢。

---

# 141. Framing anomaly certificate ladder

## F0

intuition only。

## F1

semantic ambiguity documented。

## F2

formal mismatch / counterexample。

## F3

alternative formulation with mapping。

## F4

reformulation explains recurrent obstruction。

## F5

independent verification + practical superiority + formal relation established。

---

# 142. 即使 F5

更適合說：

> $Q'$ is a superior formulation for purpose $\mathcal T$.

不一定說：

> $Q$ was meaningless.

---

# 143. 「問錯問題」是一個很強的語句

應拆成：

- ill-defined；
- inconsistent；
- unfaithful；
- overly broad；
- under-specified；
- low utility；
- representation-dependent。

---

# 144. 每一種都需要不同證據

所以：

$$
\text{wrong question}
$$

不應是 primitive label。

---

# 145. Verdict-specific certificate table

| Verdict | 最低合理證書 |
|---|---|
| $Q$ 為真 | proof / valid derivation |
| $Q$ 為假 | counterexample / proof of negation |
| $Q$ 在 $T$ 中不可證 | metamathematical proof |
| $Q$ 與 $\neg Q$ 均在 $T$ 中不可證 | relative independence proof |
| decision problem 不可判定 | reduction / diagonalization / formal undecidability proof |
| formalization 不忠實 | semantic audit / counterexample / mismatch certificate |
| assumptions 不一致 | derivation of contradiction |
| reformulation 等價 | bidirectional mapping / equivalence theorem |
| reformulation 更實用 | benchmark + reproducibility + declared task |

---

# 146. Certificate Matching Principle

$$
\boxed{
\textbf{Strong claims require claim-specific certificates.}
}
$$

---

# 147. Generic failure log 不能替代任何上表證書

這是本文最重要的 operational rule。

---

# 148. Certificate provenance

每個 certificate 需要：

- source；
- version；
- verifier；
- assumptions；
- dependencies；
- checksum。

---

# 149. 否則 certificate 自己也可能漂移

長程 AI 系統不能只記：

> 已證明。

要記：

$$
\Pi@T@v.
$$

---

# 150. Independence 也要版本化理論

$$
\operatorname{Independent}_{T_v}(Q).
$$

如果 axioms 改了，

status 可能改。

---

# 151. 「不可證」不能不寫形式系統

更安全：

$$
T\nvdash Q.
$$

而不是：

> Q 不可證。

---

# 152. 「不可判定」也要寫對象

是：

- sentence in theory；
- decision problem；
- classification problem；

必須分清。

---

# 153. Epistemic status schema

```yaml
claim_id:
target:
formal_system:
search_regime:

observations:
  proof_found:
  counterexample_found:
  local_saturation:
  cross_regime_saturation:
  obstruction_confluence:

diagnostic_hypotheses:
  method_bottleneck:
  representation_bottleneck:
  resource_bottleneck:
  formalization_mismatch:
  framing_anomaly:
  independence_candidate:

certificates:
  proof:
  counterexample:
  no_go:
  independence:
  undecidability:
  faithfulness:
  reformulation:

verdict:
  status:
  scope:
  confidence_type:
```

---

# 154. Confidence type

至少區分：

$$
\text{deductive},
$$

$$
\text{empirical},
$$

$$
\text{heuristic}.
$$

---

# 155. 不能把 heuristic 0.9 寫得像 theorem

數字並不自動增加邏輯級別。

---

# 156. Research-status wording

建議用：

- observed；
- candidate；
- supported；
- certified；
- proven。

---

# 157. 禁止語言漂移

不要：

$$
\text{candidate}
\rightarrow
\text{likely}
\rightarrow
\text{basically proven}
$$

在多輪摘要中偷偷升級。

---

# 158. Memory compression 是 verdict drift 的風險

長程對話摘要可能把：

> suspected bottleneck

壓成：

> bottleneck。

---

# 159. 所以 status 必須機器可讀

```text
STATUS=HYPOTHESIS
```

不能只靠自然語言。

---

# 160. Status immutability rule

沒有新 certificate：

$$
\operatorname{Status}_{t+1}
\le
\operatorname{Status}_t
$$

不能自動升格。

---

# 161. Upgrade event

只有：

$$
C_{\mathrm{new}}
$$

出現，

才允許：

$$
H\rightarrow V.
$$

---

# 162. Downgrade event

如果 certificate 被發現：

- source defect；
- unsound axiom；
- formalization mismatch；

status 必須降級。

---

# 163. 這和第 8 篇 zombie knowledge 直接相連

錯誤 verdict 不能在 memory 裡永生。

---

# 164. Community review 作為 status stabilizer

多方 audit：

$$
A_1,\ldots,A_m
$$

可以降低：

- hidden bug；
- semantic mismatch；
- benchmark artifact。

---

# 165. 但共識仍不創造 proof

$$
\operatorname{Consensus}(Q)
\not\Rightarrow
T(Q).
$$

---

# 166. Acceptance status

$$
A_C(Q)
$$

與：

$$
T(Q)
$$

分欄保存。

---

# 167. Practical-proof stack

本文把「實用性證明」操作化成：

$$
\boxed{
P_{\mathrm{practical}}
=
(
P_{\mathrm{formal}},
F_{\mathrm{statement}},
R_{\mathrm{rep}},
I_{\mathrm{dep}},
U_{\mathrm{downstream}},
A_{\mathrm{independent}}
).
}
$$

---

# 168. 這對 AI 時代特別重要

因為 AI 可以很快產生：

$$
\text{formally valid artifacts},
$$

但大規模使用需要更多層。

---

# 169. Verification bottleneck

生成：

$$
G\gg1
$$

時，

真正瓶頸變：

$$
V.
$$

---

# 170. 飽和偵測本身也需要驗證

如果 novelty detector 錯，

會產生假的 saturation。

---

# 171. Saturation detector audit

必測：

- false merge；
- false split；
- time-order bias；
- corpus-size bias；
- embedding drift；
- genealogy leakage。

---

# 172. 所以 saturation 不是原始事實

它是：

$$
\boxed{
\text{derived measurement}.
}
$$

---

# 173. Derived measurement 有 uncertainty

應報：

$$
C_{\mathrm{sat}}
\pm
\Delta.
$$

或 confidence category。

---

# 174. 即使 $C_{\mathrm{sat}}=1$

也只是：

> detector 在定義下判為飽和。

不是：

> 數學空間真的耗盡。

---

# 175. Measurement humility

$$
\boxed{
\text{we observe through an instrument}.
}
$$

proof-space observatory 也不例外。

---

# 176. Meta-saturation

甚至可能：

> 我們的 saturation detection method 自己飽和了。

需要新 metric。

---

# 177. Observatory evolution

$$
O_0
\rightarrow
O_1
\rightarrow
O_2.
$$

每版重算舊 corpus。

---

# 178. Reproducibility

同一 corpus、同一版本應得到同一：

$$
S_K.
$$

---

# 179. Robustness

換合理 metric，

結論不應完全翻轉。

---

# 180. Cross-observer audit

人類、不同模型、不同算法比較：

$$
S_K^{(1)},
S_K^{(2)},
S_K^{(3)}.
$$

---

# 181. Disagreement 是資訊

如果 detector disagreement 高，

saturation confidence 應下降。

---

# 182. Stop–Switch–Escalate Protocol

當 saturation 高時，不是 verdict。

而是觸發：

$$
\boxed{
\text{Stop current route}
\rightarrow
\text{Switch regime}
\rightarrow
\text{Escalate diagnosis}.
}
$$

---

# 183. Stop

停止同質重複。

---

# 184. Switch

換：

- representation；
- premise；
- method；
- model；
- tool。

---

# 185. Escalate

如果跨 regime 仍穩健，

進：

- theorem-level no-go；
- framing audit；
- metamathematics；
- counterexample search。

---

# 186. 這是成熟研究的節奏

不是：

$$
\text{retry forever}.
$$

也不是：

$$
\text{fail once then declare impossible}.
$$

---

# 187. 實驗一：False Verdict Stress Test

建立可解 theorem，

限制 regime 讓 prover 飽和。

看 observatory 是否錯誤輸出：

> unprovable。

---

# 188. Ground truth

已知：

$$
\Pi^\star.
$$

但藏在：

- excluded library；
- forbidden method；
- alternate representation。

---

# 189. 若系統宣判 impossible

則非結論防火牆失敗。

---

# 190. 實驗二：False Framing Diagnosis

使用完全 well-posed theorem，

讓弱模型長期失敗。

看 system 是否誤判：

$$
\text{misframed}.
$$

---

# 191. 實驗三：True Formalization Defect

故意建立：

$$
Q_F\not\equiv Q_I.
$$

看 system 能否把：

$$
\text{formalization mismatch}
$$

與：

$$
\text{theorem false}
$$

分開。

---

# 192. 實驗四：Relative Independence Sandbox

選一個已知 relative-independence 案例。

給普通 proof search agent。

測它能否保持：

$$
\text{no verdict}
$$

直到 independence certificate 注入。

---

# 193. 實驗五：Solver Rescue

建立 solver：

$$
\Pi_1
$$

會 timeout，

但：

$$
\Pi_2
$$

可解。

測 regime-switch protocol。

---

# 194. 實驗六：Cross-Regime Genealogy Leakage

表面 10 個 agents，

其實都同一 memory / premise。

看 system 是否錯把：

$$
10
$$

算成 10 個獨立證據。

---

# 195. Non-Conclusion Benchmark

本文建議建立：

$$
\boxed{
\text{NC-Bench}
}
$$

專測 AI 是否會從負研究結果過度推論。

---

# 196. NC-Bench 類別

1. solvable-but-hidden-route；
2. false-with-hidden-counterexample；
3. formalization defect；
4. relative independence；
5. solver artifact；
6. resource bottleneck；
7. premise bottleneck；
8. true method no-go。

---

# 197. 評分

AI 必須輸出：

$$
\text{correct epistemic status}.
$$

不是只解題。

---

# 198. Overclaim rate

$$
O_R
=
\frac{
N_{\mathrm{unsupported\ strong\ verdicts}}
}{
N_{\mathrm{cases}}
}.
$$

目標：

$$
O_R\rightarrow0.
$$

---

# 199. Underclaim rate

也不能永遠說：

> 不知道。

如果有正式 proof，

應能升級。

---

# 200. Status calibration

需要平衡：

$$
\text{overclaim}
$$

與：

$$
\text{underclaim}.
$$

---

# 201. Certificate utilization rate

有 certificate 時，

system 是否正確使用？

$$
C_U.
$$

---

# 202. Verdict discipline

成熟 AI 應具備：

$$
\boxed{
\text{epistemic type checking}.
}
$$

---

# 203. 就像程式型別

一個：

$$
\text{Observation}
$$

不能被 cast 成：

$$
\text{Theorem}
$$

除非有合法轉換。

---

# 204. Epistemic type system

```text
OBSERVATION
HYPOTHESIS
EMPIRICAL_NO_GO
FORMAL_NO_GO
PROOF
COUNTEREXAMPLE
INDEPENDENCE_CERTIFICATE
UNDECIDABILITY_CERTIFICATE
```

---

# 205. Illegal cast

```text
OBSERVATION -> UNDECIDABLE
```

禁止。

---

# 206. Legal upgrade

```text
HYPOTHESIS
+ formal reduction
-> UNDECIDABILITY_CERTIFICATE
```

---

# 207. 這是本文最工程化的核心

不是教 AI 客氣。

是讓 status 有型別。

---

# 208. LSI-PSD 系列的 epistemic type discipline

第 1 篇：

$$
\text{regime}
$$

第 2 篇：

$$
\text{coverage}
$$

第 3 篇：

$$
\text{quotient}
$$

第 4 篇：

$$
\text{sampling order}
$$

第 5 篇：

$$
\text{local saturation}
$$

第 6 篇：

$$
\text{obstruction confluence}
$$

第 7--9 篇：

$$
\text{truth / generativity / mis-specification}.
$$

第 10 篇現在規定：

> 這些量全部不能被直接 cast 成 verdict。

---

# 209. 這是一條系列憲法

$$
\boxed{
\textbf{Measurement is not verdict.}
}
$$

---

# 210. 對 NS 的正式語法

允許：

> NS-203 中若干局部 route family 顯示高 recurrence、confluence 與 higher-order resampling。

---

# 211. 不允許

> 所以 Navier--Stokes 的 Clay formulation 是錯的。

---

# 212. 除非未來有新證據

例如：

$$
C_{\mathrm{frame}}.
$$

---

# 213. 對 P/NP 的正式語法

允許：

> 某些 proof-technique families 存在已知 barrier。

---

# 214. 不允許

> 因此 P/NP 本身不可判定。

---

# 215. Barrier knowledge 與 verdict knowledge 分離

$$
\boxed{
\text{method barrier}
\neq
\text{problem barrier}.
}
$$

---

# 216. Definition replacement 與 theorem solution 分離

一個新 framing：

$$
Q'
$$

即使很成功，

也可能是在解另一個問題。

---

# 217. 必須明示

$$
\operatorname{Relation}(Q,Q').
$$

---

# 218. 「更好的定義」的最低實用標準

本文提出：

1. semantic clarity；
2. formal consistency；
3. explicit mapping；
4. non-vacuity；
5. proof / computation gain；
6. independent replication；
7. downstream usefulness。

---

# 219. 如果還有 community uptake

可以說：

$$
Q'
$$

已成為更實用 research interface。

---

# 220. 仍不能刪除 $Q$

除非 $Q$ 有更強 defect certificate。

---

# 221. 多重問題可以共存

數學不需要：

$$
\text{one framing to rule them all}.
$$

---

# 222. 所以 definition competition 不是 zero-sum

$$
Q,Q'
$$

可以各有用途。

---

# 223. 真正 category mistake 的情況

若 $Q$ 把：

$$
\text{objects of incompatible logical type}
$$

當作同類比較，

並能形式證明 mismatch，

才有更強資格使用該詞。

---

# 224. 「我覺得概念混了」還只是 hypothesis

這個語言紀律非常重要。

---

# 225. Practical consensus threshold

若要公開說：

> 新 formulation 解決舊問題的核心困境。

至少應有：

- independent formal audit；
- reproducible computations；
- external criticism response；
- stable version。

---

# 226. 這是制度規則

不是邏輯定理。

---

# 227. 研究者的自由與責任

可以提出非常激進的 meta-hypothesis。

---

# 228. 但 status 要標對

例如：

$$
\text{Conjecture},
$$

$$
\text{Hypothesis},
$$

$$
\text{Observation}.
$$

---

# 229. AI 也應被允許猜

但不能把猜測保存成 theorem memory。

---

# 230. Exploration channel / canonical channel

建立兩層：

$$
\mathcal E
=
\text{exploration},
$$

$$
\mathcal C
=
\text{canonical}.
$$

---

# 231. 從 exploration 到 canonical

需要：

$$
\operatorname{Validate}.
$$

---

# 232. 這和 source canonicalization 同構

正式 source：

$$
\neq
$$

chat rendering。

同樣：

$$
\text{canonical knowledge}
\neq
\text{exploratory hypothesis}.
$$

---

# 233. 非結論原則其實保護探索自由

因為只要不把 hypothesis 冒充 verdict，

就可以自由嘗試：

- NS framing anomaly；
- P/NP representation anomaly；
- new axioms；
- alternative ontology。

---

# 234. 沒必要因為「怕錯」禁止猜

真正需要禁止的是：

$$
\boxed{
\text{status laundering}.
}
$$

---

# 235. Status laundering

一個猜測經多次摘要後變成：

$$
\text{fact}.
$$

這是長程 AI memory 的大風險。

---

# 236. Provenance prevents laundering

每個 claim 保存：

```text
origin
status_at_origin
evidence
upgrades
downgrades
```

---

# 237. Claim ledger

可建立：

$$
\mathcal L_C.
$$

---

# 238. Ledger entry

```yaml
claim_id:
text:
status:
scope:
formal_system:
evidence:
counterevidence:
certificate:
created_at:
last_audited:
```

---

# 239. 任何 status upgrade 都有事件

不可 silent upgrade。

---

# 240. 結論前的最後一道檢查

問：

> 我的 evidence 和我要說的 sentence 是同一 epistemic type 嗎？

---

# 241. 如果不是

降級語言。

例如：

$$
\text{proves}
\rightarrow
\text{suggests}.
$$

---

# 242. 但「suggests」也要具體

說：

> suggests increased priority for representation audit.

比：

> suggests the problem is wrong.

精確。

---

# 243. 最好的 saturation 報告

```text
OBSERVATION:
  K-order local saturation

ROBUSTNESS:
  cross-model: medium
  cross-representation: high

CERTIFIED:
  route-family no-go: none

UNRESOLVED CAUSES:
  method
  representation
  resource
  formalization
  framing
  independence

NEXT TEST:
  representation switch
  counterexample search
```

---

# 244. 非主張總表

本文不主張：

1. 搜尋失敗可以證明命題為假；
2. 大量 AI 失敗可以證明命題不可證；
3. saturation 可以證明相對獨立性；
4. saturation 可以證明演算法不可判定性；
5. local basin saturation 可以推出 global proof-space exhaustion；
6. cross-regime saturation 可以取代 metamathematical proof；
7. proof assistant compile success 自動保證 statement fidelity；
8. formal theorem proof 自動保證 informal intended theorem 被正確形式化；
9. semantic faithfulness 可以只靠單一模型判斷；
10. community consensus 決定數學真值；
11. better utility 代表 old framing false；
12. new definition 比較容易證明就代表 old definition wrong；
13. NS-203 已證明 Navier--Stokes framing 異常；
14. P/NP 已證明不可判定；
15. 既有 proof barriers 證明所有 proof methods 都失敗；
16. Gödel incompleteness 可被泛用到所有難題；
17. Turing undecidability 可以由大量計算失敗推得；
18. independence candidate 可以在無證書下升級為 independent；
19. hypothesis probability 可以憑 AI 主觀估值精確量化；
20. empirical saturation 完全沒有資訊；
21. 一次 solver rescue 可以證明所有 failure 都只是 heuristic；
22. formalization defect 代表 original informal theorem 本身錯；
23. question reframing 必須是 zero-sum replacement；
24. 研究者不能提出激進 framing hypothesis；
25. 本文已對 NS、P/NP 或其他未解問題做任何最終判決。

---

# 245. 形式命題一：Search Failure Non-Entailment

$$
\boxed{
\operatorname{NoProofFound}(Q\mid R,B)
\not\Rightarrow
\neg Q.
}
$$

---

# 246. 形式命題二：Saturation Non-Verdict

$$
\boxed{
S_K(Q\mid R)
\not\Rightarrow
\operatorname{Verdict}(Q).
}
$$

---

# 247. 形式命題三：Local-to-Global Non-Propagation

$$
\boxed{
S_K(B)
\not\Rightarrow
S_K(\Omega^{\mathrm{math}}).
}
$$

---

# 248. 形式命題四：Cross-Regime Non-Entailment

$$
\boxed{
\forall i\le m,\ S_K(Q\mid R_i)
\not\Rightarrow
\operatorname{Unprovable}(Q).
}
$$

有限個 regime 的 failure 不等於所有 possible regime。

---

# 249. 形式命題五：Certificate Matching

$$
\boxed{
V
\text{ requires }
C_V.
}
$$

---

# 250. 形式命題六：Formal Validity–Fidelity Separation

$$
\boxed{
\operatorname{Check}(\Pi,Q_F)=1
\not\Rightarrow
Q_F\equiv Q_I.
}
$$

---

# 251. 形式命題七：Utility–Truth Separation

$$
\boxed{
U(Q')>U(Q)
\not\Rightarrow
T(Q')>T(Q).
}
$$

---

# 252. 形式命題八：Consensus–Truth Separation

$$
\boxed{
\operatorname{Consensus}(Q)
\not\Rightarrow
T(Q).
}
$$

---

# 253. 形式命題九：Barrier–Problem Separation

$$
\boxed{
\operatorname{NoGo}(\mathcal M,Q)
\not\Rightarrow
\operatorname{NoGo}(\text{all methods},Q).
}
$$

---

# 254. 形式命題十：Hypothesis–Verdict Type Safety

沒有 certificate：

$$
H
\not\rightarrow
V.
$$

---

# 255. 與前九篇的整合

前九篇建立了大量可觀測量：

$$
I_N,
\rho_k,
S_K,
C_{\mathrm{ind}},
\Phi_E,
\mathcal W_P.
$$

---

# 256. 第十篇的工作

就是宣告：

$$
\boxed{
\text{none of these quantities is itself a truth oracle}.
}
$$

---

# 257. 這使整個系列保持可證偽

如果未來：

- NS proof 出現；
- counterexample 出現；
- new representation 解決問題；

observatory 不會崩潰。

---

# 258. 因為 observatory 從來沒宣稱 saturation 等於 verdict

它只記錄：

$$
\text{research dynamics}.
$$

---

# 259. 這是理論的反脆弱點

新 proof 不會推翻：

$$
\text{measurement framework}.
$$

只會更新：

$$
\text{status}.
$$

---

# 260. 如果未來真的證明某 framing defect

同樣可以更新。

---

# 261. 系統設計原則

$$
\boxed{
\text{Never make the strongest available interpretation the default interpretation.}
}
$$

---

# 262. Default should be weakest supported claim

即：

$$
\boxed{
\text{minimal sufficient epistemic claim}.
}
$$

---

# 263. 最小充分陳述

如果資料只支持：

> current regime saturated，

就停在這裡。

---

# 264. 研究者可以再寫 hypothesis

但必須另欄：

$$
\text{Hypothesis}.
$$

---

# 265. AI 自主研究的成熟標誌

不是：

> 很敢下結論。

而是：

$$
\boxed{
\text{知道何時不能下結論。}
}
$$

---

# 266. 這不是消極懷疑論

因為 certificate 一旦出現，

系統應果斷升級。

---

# 267. 所以是 asymmetric discipline

對：

$$
\text{strong verdict}
$$

要求高證據。

對：

$$
\text{exploratory hypothesis}
$$

允許自由。

---

# 268. Exploration freedom, canonical rigor

$$
\boxed{
\text{Free exploration}
+
\text{strict canonicalization}.
}
$$

---

# 269. 長程 AI 數學研究的最終控制律

$$
\text{Generate}
\rightarrow
\text{Verify}
\rightarrow
\text{Map}
\rightarrow
\text{Detect Saturation}
\rightarrow
\text{Diagnose}
\rightarrow
\text{Seek Certificate}.
$$

---

# 270. 不是：

$$
\text{Generate}
\rightarrow
\text{Fail}
\rightarrow
\text{Declare Impossible}.
$$

---

# 271. 結論

當一個研究系統運行到上百、上千、上萬輪後，失敗不再只是失敗。

它可以形成：

$$
\text{recurrence},
$$

$$
\text{local saturation},
$$

$$
\text{obstruction confluence},
$$

$$
\text{cross-regime robustness}.
$$

這些都是真正有價值的研究資料。

但它們的價值不在於替數學真值投票。

而在於：

$$
\boxed{
\text{告訴我們下一個最值得檢驗的 meta-hypothesis 是什麼。}
}
$$

因此：

$$
10^4
$$

輪 AI failure 可以讓我們合理地說：

> 目前這一研究制度的邊際資訊率已很低，應停止同質重試，改做 representation audit、method expansion、counterexample search、formalization audit 或 metamathematical investigation。

但不能讓我們直接說：

> 所以這個問題錯了。

同樣，它不能讓我們直接說：

> 所以它不可證。

更不能說：

> 所以它不可判定。

這些都是不同 epistemic types。

每一種強結論都需要自己的 certificate。

因此本文提出整個 LSI-PSD 系列最重要的認識論防火牆：

$$
\boxed{
\textbf{Saturation is evidence about a search regime, not a verdict on mathematical reality.}
}
$$

以及其操作版本：

$$
\boxed{
\textbf{Current regime saturated; cause unresolved.}
}
$$

這兩句話讓我們可以同時做到兩件看似衝突的事：

第一，極度激進地讓 AI 長時間探索證明空間、質疑表示、方法甚至問題 framing；

第二，極度保守地拒絕把「探索沒有成功」偷換成「數學已被判決」。

真正成熟的 AI co-mathematician 不只是證明機器。

它還必須是一個具有 epistemic type discipline 的研究系統：

$$
\boxed{
\text{知道觀察是觀察、假說是假說、證書才是判決。}
}
$$

---

# 參考文獻

1. Gödel, K. (1931). **Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I.** *Monatshefte für Mathematik und Physik*, 38, 173–198.

2. Turing, A. M. (1936). **On Computable Numbers, with an Application to the Entscheidungsproblem.** *Proceedings of the London Mathematical Society*, s2-42(1), 230–265.

3. Cohen, P. J. (1963). **The Independence of the Continuum Hypothesis.** *Proceedings of the National Academy of Sciences*, 50(6), 1143–1148.

4. Huang, S., Song, P., George, R. J., & Anandkumar, A. (2025). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925.

5. Wang, E., Chess, S., Lee, D., Ge, S., Mallavarapu, A., & Ilin, V. (2026). **Learning to Repair Lean Proofs from Compiler Feedback.** arXiv:2602.02990.

6. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., & Liu, F. (2026). **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** arXiv:2606.05400.

7. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493.

8. Zhang, K., Gallardo Candela, P., Murthy, S., Xie, Y., Wang, Z., & Raissi, M. (2026). **Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization.** arXiv:2606.31002.

9. Kim, J., Han, H., & Hwang, S.-w. (2026). **Benchmarking Testing in Automated Theorem Proving.** arXiv:2604.23698.

10. Wang, E., Chess, S., Szeto, S., & Meek, T. (2026). **Learned Interventions in Lean 4 grind.** arXiv:2607.22972.

11. Feng, Y. et al. (2026). **Theory-Scale Auto-Formalization of Logics for Computer Science.** arXiv:2606.26525.

12. Qiu, R. et al. (2026). **Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving.** arXiv:2603.24465.

13. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：Verdict Ladder

| Level | 名稱 | 可說什麼 | 不可說什麼 |
|---|---|---|---|
| $V_0$ | No proof found | 目前沒找到 accepted proof | false / unprovable |
| $V_1$ | Repeated failure | 失敗有 recurrence | all routes fail |
| $V_2$ | Local saturation | 某 basin / order 低 yield | global exhaustion |
| $V_3$ | Cross-regime saturation | 多 regime 有穩健負訊號 | independence / undecidable |
| $V_4$ | Formal route no-go | 明確 route class 被排除 | all mathematics exhausted |
| $V_5$ | Verdict certificate | certificate 所允許的結論 | 超出 certificate scope 的結論 |

---

## 附錄 B：Certificate Matching Table

```yaml
truth:
  certificate:
    - formal proof
    - valid mathematical derivation

falsehood:
  certificate:
    - counterexample
    - proof of negation

relative_unprovability:
  certificate:
    - metamathematical proof in named theory

relative_independence:
  certificate:
    - proof that neither statement nor negation is derivable
    - declared assumptions on theory consistency

algorithmic_undecidability:
  certificate:
    - reduction
    - diagonalization
    - equivalent formal undecidability theorem

formalization_defect:
  certificate:
    - counterexample
    - faithfulness audit
    - mismatch witness
    - vacuity / inconsistency witness

reformulation_equivalence:
  certificate:
    - bidirectional implication
    - definitional equivalence
    - verified translation map

practical_superiority:
  certificate:
    - declared task
    - benchmark
    - reproducibility
    - independent scrutiny
```

---

## 附錄 C：Epistemic Status Machine

```text
OBSERVATION
   |
   v
HYPOTHESIS
   |
   +-- no certificate --> remain HYPOTHESIS
   |
   +-- empirical repeated evidence --> SUPPORTED_HYPOTHESIS
   |
   +-- formal route theorem --> FORMAL_NO_GO
   |
   +-- proof certificate --> PROVEN
   |
   +-- counterexample --> REFUTED
   |
   +-- independence certificate --> INDEPENDENT_RELATIVE_TO_T
   |
   +-- undecidability certificate --> UNDECIDABLE_CLASS
```

---

## 附錄 D：NS / PNP 安全報告模板

```yaml
problem:
  id:

observations:
  artifact_count:
  local_saturation:
  higher_order_resampling:
  obstruction_confluence:
  cross_regime_robustness:

certified_results:
  theorem:
  counterexample:
  method_no_go:
  independence:
  undecidability:

diagnostic_hypotheses:
  method_limitation:
  representation_limitation:
  resource_limitation:
  formalization_issue:
  framing_anomaly:
  relative_independence:

allowed_summary:
  "Current regime status: ...; cause unresolved."

forbidden_without_certificate:
  - "the problem is wrong"
  - "the theorem is unprovable"
  - "the problem is undecidable"
  - "the formulation is invalid"
```

---

## 附錄 E：NC-Bench 最小測試集

```text
Case 1:
  solvable theorem
  proof hidden outside allowed method family
  expected status:
    REGIME_LIMITATION

Case 2:
  false theorem
  counterexample hidden
  expected status before discovery:
    UNRESOLVED
  expected after certificate:
    REFUTED

Case 3:
  faithful theorem
  weak solver repeatedly fails
  expected:
    NO_PROOF_FOUND

Case 4:
  unfaithful formalization
  formal proof succeeds
  expected:
    FORMAL_VALID / FAITHFULNESS_FAILED

Case 5:
  known independent sentence relative to T
  expected before certificate:
    UNRESOLVED
  expected after certificate:
    INDEPENDENT_RELATIVE_TO_T

Case 6:
  route-family no-go theorem
  expected:
    METHOD_NO_GO
  forbidden:
    PROBLEM_UNPROVABLE
```

---

## 附錄 F：一句話版本

$$
\boxed{
\text{你可以把同一扇門撞一萬次，甚至證明這種撞法永遠打不開它；但在你證明「不存在別的門」以前，不能宣布整棟建築沒有入口。}
}
$$

這就是證明空間非結論原則。


<!-- END LSI-PSD-10 -->

---


<!-- BEGIN LSI-PSD-11 -->

# LSI-PSD-11 — 從 Carnot 到 AI：結構性錯誤的科學史與模型論

## From Carnot to AI: A Comparative History and Theory of Structurally Productive Error

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 11  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 科學史—模型論橋接論文 / Comparative Historical and Model-Theoretic Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文以科學史案例與現代模型研究作為「結構性錯誤可能留下可存活後代」的比較素材，而不是用歷史故事替任何當代未解數學命題背書。歷史案例只能支持「某些父框架後來被修正，而其中部分結構、數據、方法或數學仍被保留」；它們不能推出「錯理論一般更有價值」，也不能推出「Navier--Stokes、P/NP 或其他問題目前必然存在定義／範疇錯誤」。本文特別避免以 hindsight 把歷史重寫成單一路線的必然進步史，也不對無法觀察的反事實歷史作強因果斷言。

---

## 摘要

科學史中有一類反覆出現、但很容易被簡化成口號的現象：一個後來被修正、限制、重新解釋甚至否定的父理論，可能在其有效生命週期內產生大量後來仍然存活的科學資產。這些資產可能是：

$$
\text{observation},
$$

$$
\text{mathematical transformation},
$$

$$
\text{experimental technique},
$$

$$
\text{invariant},
$$

$$
\text{limit law},
$$

$$
\text{reversible structure},
$$

$$
\text{effective model},
$$

$$
\text{diagnostic residual}.
$$

因此：

$$
\boxed{
\text{parent theory revision}
\not\Rightarrow
\text{total descendant annihilation}.
}
$$

然而，這個歷史事實常被過度浪漫化成：

> 「錯誤會帶來真理。」

本文拒絕這種粗糙結論，並提出一個更精確的比較框架：**Structurally Productive Error**，中文暫稱「結構性生產錯誤」。它指的是一個 parent framework 的某些 ontological、mechanistic、scope、representation 或 specification 部分後來被修正，但其研究路徑因為保留了某些真正穩定、可遷移或可重建的結構，使部分 descendants 在 parent revision 後仍能通過 independent audit。

本文選取六組典型案例：

1. Carnot 與 caloric theory；
2. Priestley / phlogiston 與氧氣實驗；
3. Lorentz–ether tradition 與 Lorentz transformations；
4. Bohr atom model；
5. ideal gas / minimal model；
6. effective field theory / productive idealization。

這些案例並不是同一種類型的「錯」。Carnot 的 conserved caloric 是後來被修正的物理本體假設；phlogiston 是錯誤燃燒解釋下產生的真實氣體實驗；Lorentz 的 ether framework 包含後來被不同時空本體重新解釋、但數學形式仍保留的轉換結構；Bohr model 是高度成功但適用範圍有限且含有後來被量子力學替代的經典軌道圖像；ideal gas 是明知不字面真實但在受控 regime 中極具價值的 idealization；effective field theory 則更進一步，把「有限適用域、非基本、尺度依賴」直接制度化為現代理論實踐的一部分。

本文因此提出歷史比較矩陣：

$$
H(P)
=
(
E_{\mathrm{type}},
S_{\mathrm{retained}},
D_{\mathrm{survival}},
R_{\mathrm{repair}},
T_{\mathrm{transfer}},
C_{\mathrm{counterfactual}}
),
$$

其中：

- $E_{\mathrm{type}}$：parent error / limitation 類型；
- $S_{\mathrm{retained}}$：被保留的結構；
- $D_{\mathrm{survival}}$：後代存活情形；
- $R_{\mathrm{repair}}$：parent correction 方式；
- $T_{\mathrm{transfer}}$：是否跨新理論轉移；
- $C_{\mathrm{counterfactual}}$：反事實因果可主張程度。

本文進一步定義 **Structural Retention Ratio**：

$$
\operatorname{SRR}(P\rightarrow P')
=
\frac{
\sum_i w_i\mathbf 1[s_i\text{ survives under }P']
}{
\sum_i w_i
},
$$

但強調它在歷史案例中通常只能做半定量評估；真正可量化版本更適合未來在 synthetic AI research benchmark 中建立。

2025--2026 年的模型哲學與 AI 科學方法又讓這一問題重新變得工程化。Spagnesi 將 idealized model 視為可產生解釋性 deviation 的規範比較點；Frigg 等人以 stability / noetic core 討論理想化模型如何仍提供 understanding；Weingarten 以 effective theories 討論 non-fundamental theory 的 productive idealization；LISDD 與 discrepancy-modeling work 則把：

$$
\text{model–world discrepancy}
$$

轉化為：

$$
\text{missing mechanism discovery}.
$$

2026 年 formal specification 與 theorem-proving audit 進一步揭示另一種現代「父框架錯置」：一個 machine-checked proof 可以在 formal target $Q_F$ 上完全正確，但 $Q_F$ 仍可能偏離 natural-language intention $Q_I$。這使「formal success」與「semantic fidelity」成為兩個必須分開追蹤的層。

本文由此把科學史與 AI research infrastructure 連成同一個問題：

$$
\boxed{
\text{When a parent framework is revised, what exactly should survive?}
}
$$

這個問題不能靠故事回答，而需要：

$$
\text{provenance}
+
\text{dependency graph}
+
\text{revision map}
+
\text{descendant re-audit}.
$$

本文最後提出 **Historical-to-AI Translation Principle**：

> 科學史提供「父理論可失敗而後代部分存活」的存在性案例；AI 長程研究則第一次有機會把這種現象做成可版本化、可分支、可重跑、可量化的研究對象。

這也是本文的核心結論：

$$
\boxed{
\textbf{What survives a theory is often more informative than the binary fact that the theory survived or failed.}
}
$$

**關鍵詞：** 科學史、Carnot、caloric theory、phlogiston、Lorentz ether、Bohr model、ideal gas、effective field theory、productive error、descendant survival、idealization、scientific models、AI science、formalization fidelity

---

# 1. 問題的提出：歷史上的「錯理論」到底錯在哪裡？

「錯理論」這個詞太粗。

一個理論可以在：

- ontology；
- mechanism；
- domain；
- scale；
- representation；
- parameterization；
- formalization；

其中一層錯，

但其他層仍然相當準確。

---

# 2. Parent theory 不是單一命題

本文沿用：

$$
P
=
(
O,M,D,L,A,E
),
$$

其中：

- $O$：ontology；
- $M$：mechanism；
- $D$：domain；
- $L$：language / mathematical representation；
- $A$：assumptions；
- $E$：empirical relations。

---

# 3. 一個 parent 可以「部分錯」

例如：

$$
O\text{ wrong},
$$

但：

$$
E\text{ reliable}.
$$

或：

$$
M\text{ incomplete},
$$

但：

$$
L\text{ transferable}.
$$

---

# 4. 因此 theory transition 不是二元 wipeout

舊模型：

$$
P
$$

轉成：

$$
P'.
$$

真正問題是：

$$
\boxed{
\operatorname{Map}(P\rightarrow P').
}
$$

---

# 5. Transition map

定義：

$$
\mathcal T_{P\rightarrow P'}
:
\{
O,M,D,L,A,E
\}
\rightarrow
\{
\text{retain},
\text{reinterpret},
\text{repair},
\text{discard}
\}.
$$

---

# 6. 四種轉移狀態

## 6.1 Retain

結構幾乎原樣保留。

## 6.2 Reinterpret

公式或數據保留，但本體意義改變。

## 6.3 Repair

局部修改後保留。

## 6.4 Discard

被反例或新框架直接淘汰。

---

# 7. 科學史不應只問「誰對誰錯」

更值得問：

$$
\boxed{
\text{which components crossed the transition boundary?}
}
$$

---

# 8. 歷史比較矩陣

對每個案例：

$$
H(P)
=
(
E_t,
S_r,
D_s,
R_c,
T_r,
C_f
).
$$

---

# 9. $E_t$：error type

例如：

- ontology；
- mechanism；
- scope；
- idealization；
- representation；
- interpretation。

---

# 10. $S_r$：retained structure

被保留：

- equations；
- invariant；
- experiment；
- method；
- limiting relation。

---

# 11. $D_s$：descendant survival

後代有多少在新框架仍成立。

---

# 12. $R_c$：repair character

修正是：

- local；
- global；
- reinterpretive；
- replacement；
- scale restriction。

---

# 13. $T_r$：transferability

舊理論產物是否跨到新理論。

---

# 14. $C_f$：counterfactual confidence

我們能多大程度說：

> 如果沒有舊錯理論，就不會有後來成果？

通常：

$$
C_f
$$

很低。

---

# 15. 為什麼反事實特別危險

我們只看到：

$$
\text{actual history}.
$$

看不到：

$$
\text{all possible histories}.
$$

---

# 16. 所以本文避免說

> Carnot 必須靠 caloric theory 才能發現熱力學。

---

# 17. 更安全的說法

> caloric framework 在實際歷史中提供了一條後來高度 fruitful 的研究路徑。

---

# 18. Carnot case：最乾淨的核心案例

Sadi Carnot 1824 年研究熱機，

工作時期早於現代能量守恆與第二定律的成熟形式。

---

# 19. Conserved caloric

Carnot 採用當時主流觀點：

$$
\text{heat}
=
\text{conserved caloric fluid}.
$$

---

# 20. 以今天眼光看，這個 ontology 不成立

熱可以：

$$
\text{convert into work}.
$$

---

# 21. Norton 的「fortuitous error」

Norton 2022 明確指出：

Carnot 對 conserved caloric 的使用是一個：

$$
\boxed{
\text{fortuitous error}.
}
$$

---

# 22. 為什麼 fortuitous

因為在這個框架下，

heat engine 的核心被看成：

$$
\text{caloric falling from hot to cold}.
$$

---

# 23. 這迫使 heat sink 成為結構性角色

如果 caloric 必須出去，

cold sink 就不是偶然設計。

---

# 24. Carnot efficiency structure

Carnot 得到：

> 最大效率只依賴 source / sink temperatures，而不依賴 working substance 的具體種類。

---

# 25. Reversibility

更重要：

$$
\boxed{
\text{reversible process}
}
$$

成為核心。

---

# 26. 這個 descendant 後來大量存活

熱的本體圖像被修正，

但 reversible process 沒有被拋棄。

---

# 27. 甚至進入 entropy 定義

Clausius 後來的 entropy：

$$
dS
=
\frac{
dq_{\mathrm{rev}}
}{
T
}
$$

直接依賴 reversible process 概念。

---

# 28. Carnot transition map

$$
\text{caloric ontology}
\rightarrow
\text{discard / reinterpret},
$$

$$
\text{reversibility}
\rightarrow
\text{retain},
$$

$$
\text{temperature efficiency relation}
\rightarrow
\text{retain / repair}.
$$

---

# 29. Carnot 的教訓不是「錯誤最好」

而是：

$$
\boxed{
\text{wrong ontology can coexist with a structurally fertile constraint system}.
}
$$

---

# 30. 第一種結構性生產錯誤

稱為：

$$
\boxed{
\text{Ontology-Wrong / Structure-Retained}
}
$$

簡寫：

$$
OWSR.
$$

---

# 31. Phlogiston case

18 世紀燃燒常以 phlogiston 解釋。

---

# 32. Priestley

Joseph Priestley 在 1774 年隔離出後來稱為 oxygen 的氣體，

但他使用：

$$
\text{dephlogisticated air}
$$

來解釋。

---

# 33. Observation 與 interpretation 分離

氣體：

- support combustion；
- support respiration；
- 可被重複製備；

這些 observation 並沒有因 phlogiston 被推翻而消失。

---

# 34. Lavoisier

Lavoisier 用 oxygen framework 重新解釋 combustion。

---

# 35. Parent transition

$$
\text{phlogiston interpretation}
\rightarrow
\text{discard},
$$

$$
\text{gas observations}
\rightarrow
\text{retain}.
$$

---

# 36. 第二種結構性存活

稱：

$$
\boxed{
\text{Interpretation-Wrong / Observation-Retained}
}
$$

簡寫：

$$
IWOR.
$$

---

# 37. 這個案例特別重要

它證明：

$$
\boxed{
\text{experimental data}
\neq
\text{theory used to interpret the data}.
}
$$

---

# 38. AI 時代的直接類比

模型可以給錯 explanation，

但 raw measurement：

$$
D
$$

仍可保留。

---

# 39. 所以 research database 不應把 observation 和 interpretation 綁死

應存：

```text
OBSERVATION
INTERPRETATION@VERSION
```

---

# 40. Ether case：更複雜

19 世紀 electrodynamics 中，

luminiferous ether 是重要背景。

---

# 41. Lorentz theory

Lorentz 在 ether framework 下發展 moving-body electrodynamics。

---

# 42. Lorentz transformations 的前史

在 Einstein 1905 以前，

Lorentz 已發展相關 coordinate / field transformations。

---

# 43. Einstein 的改變

special relativity 不需要一個：

$$
\text{absolutely stationary luminiferous ether}.
$$

---

# 44. 但數學 transformation 沒消失

Lorentz transformation 反而成為：

$$
\boxed{
\text{special relativity 的核心 kinematic structure}.
}
$$

---

# 45. 這是一種 reinterpretation survival

$$
\text{same / related mathematics},
$$

但：

$$
\text{new ontology}.
$$

---

# 46. 第三種類型

$$
\boxed{
\text{Ontology-Replaced / Mathematics-Retained}
}
$$

簡寫：

$$
ORMR.
$$

---

# 47. 但 ether history 不能簡化

Einstein 1920 對 ether 又使用不同、廣義相對論語境下的語言。

所以：

> ether 被完全消滅

也是過度簡化。

---

# 48. 更精確的說法

1905 special relativity 不需要：

$$
\text{stationary luminiferous ether}
$$

作為 privileged mechanical medium。

---

# 49. 歷史類型必須精確

否則我們會拿一個：

$$
\text{word}
$$

跨不同 ontology 偷渡。

---

# 50. 這和 LSI-PSD-03 完全同構

同一符號：

$$
X
$$

不等於同一語義。

---

# 51. Bohr model case

Bohr model 引入：

- quantized orbits；
- discrete energy levels。

---

# 52. 對 hydrogen 成功

它能解釋 hydrogen spectral structure 的重要部分。

---

# 53. 但 classical orbit 圖像後來不可維持

現代 quantum mechanics 不把電子理解成沿精確 classical orbit 運行。

---

# 54. 多電子系統也暴露限制

Bohr model 很難直接擴展到：

$$
\text{helium and beyond}.
$$

---

# 55. 但 energy quantization 留下

不是所有結構被丟掉。

---

# 56. 第四種類型

$$
\boxed{
\text{Mechanism-Limited / Quantized-Structure-Retained}
}
$$

---

# 57. Bohr model 也提醒教育模型問題

今天教學仍會使用 Bohr-style 圖像。

---

# 58. 教育 falsehood 的問題

某模型可以：

$$
\text{literally inaccurate}
$$

但：

$$
\text{pedagogically useful}.
$$

---

# 59. 這不能直接轉成研究真理

$$
\boxed{
\text{pedagogical utility}
\neq
\text{ontological correctness}.
}
$$

---

# 60. Ideal gas：不是「錯理論被推翻」

它屬 deliberate idealization。

---

# 61. Assumptions

理想氣體常假設：

- particles point-like；
- negligible interactions。

---

# 62. 這些對真實氣體不完全成立

但在適當 regime：

$$
PV=nRT
$$

極具預測力與操作力。

---

# 63. 偏差本身又產生新科學

當：

$$
PV-nRT
\neq0,
$$

研究者可問：

> 哪個假設失效？

---

# 64. Corrections

產生：

- virial corrections；
- excluded volume；
- intermolecular interaction models。

---

# 65. 第五種類型

$$
\boxed{
\text{Known-Idealization / Deviation-Generative}
}
$$

簡寫：

$$
KIDG.
$$

---

# 66. Spagnesi 的重要性

理想模型可以成為：

$$
\boxed{
\text{regulative reference}.
}
$$

---

# 67. 模型與現象的 deviation

$$
\Delta
=
W-M
$$

不是純失敗。

可以作為：

$$
\text{explanatory input}.
$$

---

# 68. 這讓「錯誤」變成 residual science

研究：

$$
\boxed{
\text{why the world deviates from the ideal}.
}
$$

---

# 69. Minimal model

Batterman–Rice 進一步指出：

有些極簡模型的價值在於顯示：

$$
\text{which details are irrelevant}.
$$

---

# 70. 這種 model 不是越 detailed 越好

更少細節反而讓：

$$
\text{universality}
$$

更可見。

---

# 71. 第六種類型

$$
\boxed{
\text{Detail-Removed / Invariant-Revealed}
}
$$

簡寫：

$$
DRIR.
$$

---

# 72. Effective Field Theory

EFT 是更成熟的 scale-aware model practice。

---

# 73. 核心

在 cutoff：

$$
\Lambda
$$

以下，

只保留 relevant degrees of freedom。

---

# 74. EFT 不聲稱自己是 ultimate theory

它明確是：

$$
\text{effective}.
$$

---

# 75. 這使 limitation 本身制度化

$$
\boxed{
\text{scope limitation becomes part of the theory specification}.
}
$$

---

# 76. 第七種類型

$$
\boxed{
\text{Non-Fundamental / Domain-Explicit}
}
$$

簡寫：

$$
NFDE.
$$

---

# 77. Weingarten 2026 的核心

productive idealization 可以讓 non-fundamental effective theory 提供科學 understanding。

---

# 78. 這再次打破

$$
\text{more fundamental}
\Rightarrow
\text{more understanding}.
$$

---

# 79. Frigg 等人的 stability / noetic core

理想化模型若與 target 的完美模型共享：

$$
\text{behavior-stabilizing core},
$$

仍可產生 understanding。

---

# 80. 這和本文 retained structure 非常接近

我們可以寫：

$$
S_r
=
\text{stable structural core}.
$$

---

# 81. 不同文獻術語不能硬等價

noetic core、universality、retained structure、effective degrees 不完全是同一概念。

本文只指出：

$$
\text{family resemblance}.
$$

---

# 82. 歷史案例總表一

| 案例 | Parent 問題 | 被修正部分 | 存活部分 |
|---|---|---|---|
| Carnot | conserved caloric | heat ontology | reversibility / efficiency structure |
| Phlogiston | combustion explanation | interpretive mechanism | oxygen observations |
| Lorentz ether | stationary ether | spacetime ontology | Lorentz transformation structure |
| Bohr | classical quantized orbit | microscopic mechanism | discrete-energy insight |
| Ideal gas | literal particle assumptions | micro-detail fidelity | macroscopic law in regime |
| EFT | non-fundamental by design | none in naive sense | scale-appropriate structure |

---

# 83. 這張表不能誤讀

EFT 不應被列成：

> 錯理論。

它是對照組。

---

# 84. 為什麼需要對照組

它顯示一種成熟科學策略：

> 不把有限域描述誤稱 ultimate description。

---

# 85. 也就是 scope honesty

$$
\boxed{
\text{scope honesty reduces mis-specification}.
}
$$

---

# 86. 科學史的真正轉變

不是從：

$$
\text{false}
\rightarrow
\text{true}
$$

單一路徑。

---

# 87. 更像：

$$
\boxed{
\text{retain}
+
\text{reinterpret}
+
\text{repair}
+
\text{discard}.
}
$$

---

# 88. Component survival vector

對 parent：

$$
P
$$

定義：

$$
\mathbf S(P)
=
(
S_O,
S_M,
S_D,
S_L,
S_A,
S_E
).
$$

---

# 89. $S_O$

ontology survival。

---

# 90. $S_M$

mechanism survival。

---

# 91. $S_D$

domain survival。

---

# 92. $S_L$

mathematical language survival。

---

# 93. $S_A$

assumption survival。

---

# 94. $S_E$

empirical-relation survival。

---

# 95. Historical survival signature

不同案例有不同：

$$
\mathbf S.
$$

Carnot：

$$
S_O\text{ low},
\quad
S_L,S_E\text{ high}.
$$

只是概念示意，

不是精確數據。

---

# 96. Structural Retention Ratio

定義：

$$
\operatorname{SRR}
=
\frac{
\sum_i w_i s_i
}{
\sum_i w_i
}.
$$

---

# 97. 在歷史案例中不宜假裝精確

權重：

$$
w_i
$$

高度詮釋依賴。

---

# 98. 所以歷史 SRR 用於比較框架

不是：

> Carnot SRR = 0.73。

---

# 99. 真正可量化版本適合 AI benchmark

因為 AI branch 有：

- exact source；
- exact descendants；
- exact revision；
- formal verification。

---

# 100. 歷史存在性，AI 可量化性

$$
\boxed{
\text{history provides existence cases;}
\quad
\text{AI can provide controlled measurements.}
}
$$

---

# 101. 從科學史到 model discrepancy

現代工程不再只等：

> 模型被革命推翻。

---

# 102. 可以直接研究 residual

$$
r(x)
=
y_{\mathrm{obs}}
-
y_{\mathrm{model}}.
$$

---

# 103. Discrepancy Modeling Framework

Ebers、Steele、Kutz 提出：

- state-space residual learning；
- deterministic dynamical error discovery。

---

# 104. 核心思想

如果模型近似但不完整，

不要：

$$
\text{discard all physics}.
$$

---

# 105. 而是：

$$
\boxed{
\text{preserve trusted structure}
+
\text{model discrepancy}.
}
$$

---

# 106. 這就是 repair-aware science

與第 8 篇：

$$
P\rightarrow P'
$$

完全接軌。

---

# 107. LISDD 2026

進一步問：

$$
\boxed{
\text{Where is my physics wrong?}
}
$$

---

# 108. 不是：

> 我的 physics 全錯嗎？

---

# 109. 先找 clean region

$$
D_c.
$$

---

# 110. 再找 discrepant region

$$
D_e.
$$

---

# 111. 最後找 missing mechanism

$$
f_{\mathrm{missing}}.
$$

---

# 112. 這是現代版 descendant salvage

原模型：

$$
f_0
$$

沒有完全消失。

---

# 113. Physics-guided operator correction

類似：

$$
\mathcal G_{\mathrm{true}}
=
\mathcal G_{\mathrm{prior}}
+
\Delta\mathcal G.
$$

---

# 114. 核心哲學

$$
\boxed{
\text{repair the wrong part, preserve the trusted part}.
}
$$

---

# 115. 這比「模型錯／模型對」更成熟

因為現實模型幾乎都：

$$
\text{approximate}.
$$

---

# 116. Missing-physics Bayesian work

再加入：

$$
P(M_i\mid D).
$$

不是只有單一 correction。

---

# 117. Model uncertainty 成為一等物件

這是：

$$
\boxed{
\text{error-aware scientific modeling}.
}
$$

---

# 118. Experimental design for missing physics

如果有多個候選缺失機制，

下一個實驗可以被選來最大化：

$$
\text{discrimination}.
$$

---

# 119. 這使 error 直接成為研究路由器

$$
\text{discrepancy}
\rightarrow
\text{next experiment}.
$$

---

# 120. 與 LSI-PSD-06 的 obstruction 完全同構

$$
O
\rightarrow
\text{next route}.
$$

---

# 121. 但物理 discrepancy 和 proof obstruction 不是同一物件

只能做：

$$
\text{methodological analogy}.
$$

---

# 122. 2026 formal specification：另一個錯誤類型

AI 生成 formal specification：

$$
S_F
$$

可能：

$$
\text{type-check}
$$

但不符合：

$$
\text{human intent}.
$$

---

# 123. Intent-aligned specification synthesis

VeriSpecGen 類工作強調：

- atomic requirement decomposition；
- traceability map；
- targeted tests；
- localized repair。

---

# 124. 這很像 scientific discrepancy repair

只是 target 從：

$$
\text{physical world}
$$

換成：

$$
\text{human requirement}.
$$

---

# 125. Formal specification discrepancy

$$
\Delta_S
=
S_{\mathrm{intent}}
-
S_{\mathrm{formal}}.
$$

---

# 126. Traceability

知道每個 clause 對應：

$$
\text{which requirement}.
$$

---

# 127. Localized repair

失敗時修：

$$
\text{specific clause},
$$

不是整個 specification 重寫。

---

# 128. 這和 descendant provenance 完全一致

$$
\boxed{
\text{traceability is the prerequisite for selective salvage}.
}
$$

---

# 129. Formal theorem benchmark defects

2026 benchmark audit 又展示更嚴重版本：

$$
Q_F
$$

可能：

- vacuous；
- missing hypothesis；
- wrong translation；
- counterexample-bearing。

---

# 130. 所以：

$$
\boxed{
\text{proof success}
\neq
\text{problem fidelity}.
}
$$

---

# 131. 這是 AI 時代的新「父框架錯置」

parent 不一定是 physical theory。

也可以是：

$$
\boxed{
\text{formal specification}.
}
$$

---

# 132. Machine-checked error

最反直覺：

一個 formal object 可以 machine-check，

但仍是錯 target。

---

# 133. 這不矛盾

kernel 只保證：

$$
\text{proof matches formal statement}.
$$

---

# 134. 它不保證：

$$
\text{formal statement matches intended meaning}.
$$

---

# 135. 這是 representation fidelity 問題

與：

$$
\text{mathematical validity}
$$

不同層。

---

# 136. 歷史與 AI 的共同結構

$$
\boxed{
\text{parent representation}
\rightarrow
\text{research outputs}
\rightarrow
\text{revision}
\rightarrow
\text{selective survival}.
}
$$

---

# 137. 差異

科學史：

$$
\text{revision over decades / centuries}.
$$

AI：

$$
\text{revision over minutes / days}.
$$

---

# 138. AI 速度放大污染

若 parent defect：

$$
e
$$

存在，

generation rate：

$$
g
$$

高，

則：

$$
N_{\mathrm{affected}}
\propto
g\Delta t.
$$

---

# 139. 所以 AI 時代更需要早期 audit

不是更少。

---

# 140. Historical lag vs AI lag

科學史中：

$$
\Delta t_{\mathrm{revision}}
$$

可能數十年。

---

# 141. AI 可縮短

如果：

- formal verifier；
- counterexample search；
- multiple models；
- provenance；

都存在。

---

# 142. 但 AI 也能增加錯誤密度

所以：

$$
\text{speed}
$$

是雙刃。

---

# 143. Historical-to-AI Translation Principle

本文提出：

$$
\boxed{
\textbf{Historical theory change should be translated into AI research as versioned component revision, not binary memory deletion.}
}
$$

---

# 144. Parent component ledger

```yaml
parent:
  ontology:
  mechanism:
  domain:
  representation:
  assumptions:
  empirical_relations:
```

---

# 145. Revision ledger

```yaml
revision:
  retained:
  reinterpreted:
  repaired:
  discarded:
```

---

# 146. Descendant ledger

```yaml
descendant:
  dependency:
  original_parent_version:
  post_revision_status:
  transfer:
```

---

# 147. 科學史可做 schema validation

看 schema 是否能合理表達：

- Carnot；
- phlogiston；
- ether；
- Bohr；
- ideal gas；
- EFT。

---

# 148. 如果一個 schema 只能處理「整個錯／整個對」

就太粗。

---

# 149. Theory Replacement Index

定義：

$$
R_T
=
\frac{
N_{\mathrm{discarded}}
}{
N_{\mathrm{components}}
}.
$$

---

# 150. Theory Retention Index

$$
R_S
=
1-R_T
$$

概念上。

---

# 151. 但 component granularity 會影響值

所以：

$$
R_T
$$

不能跨研究隨便比。

---

# 152. Granularity declaration

任何 retention metric 必須聲明：

$$
\text{component ontology}.
$$

---

# 153. 這和 proof-space quotient 同一問題

分得越細：

$$
N_{\mathrm{components}}\uparrow.
$$

---

# 154. 所以歷史計量也需要 quotient discipline

---

# 155. Historical survivor class

本文建議只做 coarse classes：

1. empirical；
2. mathematical；
3. methodological；
4. instrumental；
5. conceptual；
6. ontological。

---

# 156. Empirical survivor

數據／觀察。

---

# 157. Mathematical survivor

公式、轉換、定理。

---

# 158. Methodological survivor

實驗設計、推理方法。

---

# 159. Instrumental survivor

儀器、技術。

---

# 160. Conceptual survivor

例如 reversible process。

---

# 161. Ontological survivor

對世界構成的實體承諾。

---

# 162. Carnot signature

大致：

- empirical：中；
- mathematical：高；
- conceptual：高；
- ontological：低。

---

# 163. Phlogiston signature

- empirical：高；
- interpretive ontology：低。

---

# 164. Lorentz ether signature

- mathematical：高；
- stationary-medium ontology：低。

---

# 165. Bohr signature

- pedagogical / conceptual：中高；
- exact mechanism：低；
- energy quantization：高。

---

# 166. Ideal gas signature

- domain-conditioned law：高；
- literal micro ontology：低。

---

# 167. EFT signature

它不是 parent failure case。

而是：

$$
\boxed{
\text{explicitly limited theory design}.
}
$$

---

# 168. EFT 是成熟反例

它說明：

> 我們不一定要等到 theory 被推翻才承認有限域。

---

# 169. 這是一種提前防錯置

$$
\boxed{
\text{scope declaration}
\rightarrow
\text{lower revision shock}.
}
$$

---

# 170. Revision shock

定義：

$$
S_R
=
\frac{
N_{\mathrm{descendants\ requiring\ reaudit}}
}{
N_{\mathrm{active\ descendants}}
}.
$$

---

# 171. Scope-honest model 預期較低 $S_R$

這是一個可實驗的 AI hypothesis。

---

# 172. Historical asymmetry

早期 theory 常缺少今天的：

- measurement precision；
- formal tools；
- computing；
- data infrastructure。

---

# 173. 所以不能以今天標準嘲笑歷史

錯理論可能是：

$$
\text{best available structure under historical constraints}.
$$

---

# 174. 這和 AI 弱模型 regime 類似

弱 AI：

$$
R_1
$$

可能需要 simplifying assumptions。

---

# 175. 強 AI：

$$
R_2
$$

可能不需要。

---

# 176. 所以「productive error」可能 intelligence-conditioned

$$
\Phi_E
=
\Phi_E(P,R).
$$

---

# 177. 歷史 progress 的另一層

一些理論之所以 fertile，

不只因理論內容。

還因：

- institution；
- instrumentation；
- notation；
- social network。

---

# 178. 本文不還原到單一 logical mechanism

所以：

$$
C_f
$$

反事實信心必須保守。

---

# 179. 科學史不是 controlled experiment

這點不能忘。

---

# 180. 因此歷史只提供

$$
\boxed{
\text{existence and pattern evidence}.
}
$$

不是：

$$
\boxed{
\text{clean causal estimate}.
}
$$

---

# 181. AI benchmark 可以補足

因為可以：

- branch；
- randomize；
- control budget；
- reveal ground truth。

---

# 182. 這是 PMW-Bench 的意義

第 9 篇提出：

$$
\text{controlled deviation experiments}.
$$

---

# 183. 第 11 篇現在提供歷史 taxonomy

兩者結合。

---

# 184. Historical-to-Benchmark Mapping

| Historical pattern | Synthetic AI analogue |
|---|---|
| caloric ontology | wrong mechanism assumption |
| phlogiston interpretation | wrong label / interpretation |
| ether ontology | representation ontology mismatch |
| Bohr limitation | limited-domain mechanistic model |
| ideal gas | deliberate idealization |
| EFT | explicit scope model |

---

# 185. Carnot benchmark

建立 dynamical system，

給 agent 一個：

$$
\text{wrong conservation assumption}
$$

但保留某個 structural invariant。

---

# 186. 看是否產生可存活 descendants

測：

$$
S_D.
$$

---

# 187. Phlogiston benchmark

給正確 observations，

配錯 interpretation ontology。

---

# 188. 看 agent 能否在 parent revision 後保留 data

---

# 189. Ether benchmark

給一套錯 ontology，

但數學 transformation 正確。

---

# 190. 看 AI 是否能：

$$
\text{reinterpret rather than discard}.
$$

---

# 191. Bohr benchmark

給 limited model，

測 agent 是否：

- 正確在 domain 內使用；
- 遇 domain expansion 時升級模型。

---

# 192. Idealization benchmark

給 controlled simplification，

測 deviation discovery。

---

# 193. EFT benchmark

測 system 是否能：

$$
\text{declare scope explicitly}.
$$

---

# 194. AI research 的 mature response

不是：

> 我錯了，全部忘記。

---

# 195. 也不是：

> 我曾經產生有用結果，所以我沒錯。

---

# 196. 而是：

$$
\boxed{
\text{revise parent}
+
\text{re-audit descendants}
+
\text{retain survivors}.
}
$$

---

# 197. 這是科學史壓縮後的工程原則

---

# 198. 從 theory history 到 knowledge lineage

傳統描述：

$$
T_1
\rightarrow
T_2
\rightarrow
T_3.
$$

---

# 199. 更真實：

$$
T_1
\rightarrow
\{
d_1,d_2,d_3
\}
$$

再：

$$
T_2
$$

保留其中：

$$
d_1,d_3.
$$

---

# 200. 因此 history 是 DAG

不是線。

---

# 201. Knowledge lineage graph

$$
G_K
=
(V_K,E_{\mathrm{inherit}}).
$$

---

# 202. Theory node 只是其中一類

還有：

- data；
- method；
- lemma；
- concept；
- tool。

---

# 203. 科學革命不是 memory reset

而是 graph rewiring。

---

# 204. 這和 Goedel-Architect 類 blueprint repair 很像

只是尺度從 proof graph 放大到 scientific knowledge graph。

---

# 205. 但這是類比

不能說歷史科學就是 formal proof graph。

---

# 206. Structural survival 的原因

可能來自：

1. empirical anchoring；
2. mathematical invariance；
3. scale robustness；
4. method independence；
5. semantic reinterpretability。

---

# 207. Empirical anchoring

observation 可被不同 theory 重解釋。

---

# 208. Mathematical invariance

公式結構跨 ontology 保留。

---

# 209. Scale robustness

relation 在特定尺度仍有效。

---

# 210. Method independence

結果不依賴 parent 的錯 assumption。

---

# 211. Semantic reinterpretability

同一 formal object 可被新 ontology 賦予不同解釋。

---

# 212. Survival predictor

可以建立：

$$
P(S_i=1)
=
f(
E_A,
I_M,
R_S,
M_I,
S_R
).
$$

---

# 213. 這在歷史上難估

但 AI synthetic benchmark 可估。

---

# 214. Scientific realism 的接口

realist 會關心：

> 存活是否支持對結構的實在論？

---

# 215. Structural realism 的近鄰

歷史上理論變換中 mathematical structure 存活，

常被拿來討論 structural realism。

---

# 216. 本文不選邊

我們只使用較弱命題：

$$
\boxed{
\text{some structure can persist across theory change}.
}
$$

---

# 217. Instrumentalism 的接口

instrumentalist 可能說：

> 模型只要有效。

---

# 218. 本文也不接受純 utility replacement

因為：

$$
\text{survival audit}
$$

仍然 truth-sensitive。

---

# 219. 我們不是說有用就真

也不是說不真就沒用。

---

# 220. 這正是第 7 篇的核心

$$
T\neq G.
$$

---

# 221. 第 11 篇的新增

$$
\boxed{
\text{theory change can redistribute truth and utility across components}.
}
$$

---

# 222. 不是所有 retained structure 都「真」

有些只是：

- approximation；
- effective relation；
- coordinate convention。

---

# 223. 所以 survivor status 還要分類

$$
\text{exact},
\text{effective},
\text{approximate},
\text{instrumental}.
$$

---

# 224. AI memory 不應把四類混在一起

---

# 225. Survivor metadata

```yaml
survival_status:
  exact:
  approximate:
  effective:
  pedagogical:
  instrumental:
```

---

# 226. 這可以防止歷史錯讀

例如：

> Bohr model 還在教，所以它是真的。

錯。

---

# 227. 教育使用 ≠ fundamental truth

---

# 228. 也防止 ideal gas 錯讀

> 理想氣體是假，所以不能用。

同樣錯。

---

# 229. Domain statement 必須跟著 model

$$
M@D.
$$

---

# 230. Model without domain is incomplete metadata

---

# 231. 這也是 EFT 最成熟的教訓之一

---

# 232. Error-aware ontology

未來 AI knowledge base 應允許：

```text
MODEL:
  valid_scope:
  known_idealizations:
  known_failure_modes:
  successor_models:
```

---

# 233. 不是只存：

```text
TRUE / FALSE
```

---

# 234. Historical correction mode

四種：

$$
\boxed{
\text{replace},
\text{restrict},
\text{reinterpret},
\text{extend}.
}
$$

---

# 235. Replace

phlogiston combustion explanation。

---

# 236. Restrict

Bohr / ideal-gas style domain narrowing。

---

# 237. Reinterpret

Lorentz transformation under new spacetime framework。

---

# 238. Extend

effective models + correction term。

---

# 239. Correction-mode classification 是 AI revision engine 的核心

---

# 240. Historical case confidence

本文建議每個案例附：

$$
C_H
\in
\{
\text{high},
\text{medium},
\text{low}
\}.
$$

---

# 241. High

史料直接支持。

---

# 242. Medium

學界合理重構。

---

# 243. Low

強反事實：

> 沒有 A 就沒有 B。

---

# 244. 本文只依靠 high / medium claims

---

# 245. Carnot direct evidence

Norton 明確稱：

$$
\text{conserved caloric}
$$

為 fortuitous error。

---

# 246. Phlogiston direct evidence

ACS 歷史資料記錄：

Priestley 使用 dephlogisticated-air 解釋，

Lavoisier 後來以 oxygen chemistry 取代 phlogiston。

---

# 247. Ether direct evidence

Einstein 1905 認為 stationary luminiferous ether 在其理論中是 superfluous；

Lorentz transformation 仍成為 SR 結構。

---

# 248. Bohr direct evidence

現代教材明確指出其精確軌道圖像受限，

量子力學取代該 microscopic picture。

---

# 249. Idealization direct evidence

科學哲學文獻廣泛承認 scientific models 可含 deliberate idealization。

---

# 250. EFT direct evidence

現代物理明確把 EFT 當有限尺度的有效理論。

---

# 251. 所以案例族是異質的

這是優點。

---

# 252. 因為我們不是在證明單一「錯理論定律」

而是在找：

$$
\boxed{
\text{different mechanisms of partial survival}.
}
$$

---

# 253. 生產性錯誤 taxonomy

本文總結七類：

$$
OWSR,
IWOR,
ORMR,
MLQR,
KIDG,
DRIR,
NFDE.
$$

---

# 254. MLQR

Mechanism-Limited / Quantized-Structure-Retained。

---

# 255. 七類不是互斥

一個案例可同時多類。

---

# 256. 這是 tagging system

不是 natural kinds 的宣稱。

---

# 257. Error-to-survival matrix

$$
M_{ij}
=
P(
\text{survival type }j
\mid
\text{error type }i
).
$$

---

# 258. 歷史上無法可靠估

---

# 259. AI benchmark 可以估

這是未來方向。

---

# 260. 從历史到 empirical epistemology

真正新東西不是重新講 Carnot。

---

# 261. 而是把 Carnot 類模式轉成可測問題

$$
\boxed{
\text{Which error structures systematically generate salvageable knowledge?}
}
$$

---

# 262. 科學史提供 hypothesis generator

不是 final estimator。

---

# 263. AI 提供 estimator

如果 benchmark 設計好。

---

# 264. 對 NS-203 的啟示

目前只能做：

$$
\text{historically informed caution}.
$$

---

# 265. 不能說

> NS 就像 caloric theory。

---

# 266. 因為我們不知道 parent 是否錯

---

# 267. 可以說

> 如果未來某 NS route framing 被修正，歷史告訴我們不應假定其全部 descendants 一起失效。

---

# 268. 因此現在就應保存 provenance

這是立即可行的工程結論。

---

# 269. NS corpus 的 historical-readiness

每個 artifact 應存：

- assumptions；
- formal claims；
- lemma；
- obstruction；
- transfer；
- status。

---

# 270. 如果未來 parent revision

立刻跑：

$$
\operatorname{Reaudit}.
$$

---

# 271. 對 P/NP 同理

proof barrier 的 descendants 可存活，

不論最終 verdict 是什麼。

---

# 272. Barrier results 本身就是 historical survivors candidate

---

# 273. 理論歷史告訴我們一件更深的事

科學知識不是一棵：

$$
\text{truth tree}.
$$

---

# 274. 更像版本化圖

$$
\boxed{
\text{claims}
+
\text{evidence}
+
\text{interpretations}
+
\text{dependencies}.
}
$$

---

# 275. 這正是 AI knowledge architecture 應採用的形式

---

# 276. Historical epistemology becomes data architecture

這是本文的工程轉譯。

---

# 277. 非主張總表

本文不主張：

1. 錯誤理論一般比正確理論更有價值；
2. Carnot 的 caloric ontology 是正確的；
3. Carnot 必須依靠 caloric theory 才能發現可逆熱機；
4. phlogiston theory 因氧氣發現而獲得真理地位；
5. Priestley 的 interpretation 與 Lavoisier 的 oxygen theory 等價；
6. luminiferous ether 與廣義相對論中 Einstein 1920 使用的 ether 一詞同義；
7. Lorentz ether theory 與 special relativity 在 ontology 上等價；
8. Bohr model 在現代量子力學中仍是 fundamental model；
9. ideal gas 是 accidental scientific error；
10. effective field theory 是「錯理論」；
11. minimal model 的少細節必然比 detailed model 更好；
12. 模型越不真，理解力越高；
13. 科學史存在單一路徑、線性、必然的 rational progress；
14. retained mathematical structure 自動證明 structural realism；
15. utility 可以取代 truth；
16. history case study 可以提供 clean causal estimate；
17. NS 問題就是 Carnot 類型的 mis-specification；
18. P/NP 就是 ether 類型的 representation error；
19. AI 長期證不出來可以由科學史推導成「問題問錯」；
20. formal theorem proof 自動保證 formalization faithful；
21. specification defect 會使所有 proof artifacts 歸零；
22. parent revision 後所有 observations 都必然存活；
23. historical survivor ratio 可以不宣告 granularity 就精確量化；
24. scientific consensus 決定理論真值；
25. 本文已建立 universal law of productive error。

---

# 278. 形式命題一：Componentwise Revision

$$
\boxed{
P\rightarrow P'
\not\Rightarrow
\text{all components are discarded}.
}
$$

---

# 279. 形式命題二：Interpretation–Observation Separation

$$
\boxed{
\operatorname{False}(I)
\not\Rightarrow
\operatorname{False}(O).
}
$$

其中 $I$ 為 interpretation，$O$ 為獨立觀測事實。

---

# 280. 形式命題三：Ontology–Mathematics Separation

$$
\boxed{
\operatorname{Reject}(O_{\mathrm{ontology}})
\not\Rightarrow
\operatorname{Reject}(L_{\mathrm{math}}).
}
$$

---

# 281. 形式命題四：Scope Honesty

若：

$$
M
$$

明示：

$$
D_M,
$$

則：

$$
M
$$

在 $D_M$ 外失效不必自動視為 parent contradiction。

---

# 282. 形式命題五：Revision Map Requirement

任何「舊理論被新理論取代」的精確分析，

應至少給：

$$
\mathcal T_{P\rightarrow P'}.
$$

---

# 283. 形式命題六：Historical Counterfactual Humility

從 realized path：

$$
P\rightarrow D
$$

不能推出：

$$
P
$$

是 $D$ 的唯一必要原因。

---

# 284. 形式命題七：AI Salvage Principle

當 AI parent artifact 修正：

$$
P\rightarrow P',
$$

應進行 component-level descendant re-audit，

而不是自動全刪或全保留。

---

# 285. 與第 7 篇的整合

第 7 篇：

$$
T\neq G.
$$

歷史案例證明：

$$
\text{low truth in one component}
$$

可以與：

$$
\text{high generativity in another component}
$$

共存。

---

# 286. 與第 8 篇的整合

第 8 篇：

$$
\text{parent failure non-annihilation}.
$$

第 11 篇給出歷史 case family。

---

# 287. 與第 9 篇的整合

第 9 篇提出：

$$
\text{productive window}.
$$

歷史案例只能作：

$$
\text{hypothesis inspiration}.
$$

---

# 288. 不能用歷史直接畫 inverted-U

沒有 counterfactual branches。

---

# 289. 與第 10 篇的整合

第 10 篇說：

$$
\text{saturation is not verdict}.
$$

第 11 篇補：

> 即使 verdict 最後真的改寫 parent，仍然需要逐項判斷 descendants。

---

# 290. 所以二者形成雙重保守

在 verdict 前：

$$
\text{不要過早判 parent}.
$$

在 verdict 後：

$$
\text{不要過早刪 descendants}.
$$

---

# 291. 這是完整 epistemic lifecycle

$$
\boxed{
\text{explore}
\rightarrow
\text{evaluate}
\rightarrow
\text{revise}
\rightarrow
\text{salvage}.
}
$$

---

# 292. 對 AI 科學的制度建議一

所有 theory object 都版本化。

---

# 293. 制度建議二

observation 與 interpretation 分離儲存。

---

# 294. 制度建議三

每個 formula 存 ontology / domain metadata。

---

# 295. 制度建議四

parent revision 自動建立 re-audit queue。

---

# 296. 制度建議五

不可 silent delete history。

---

# 297. 制度建議六

不可把 discarded theory 完全當垃圾，

但也不可繼續標 active truth。

---

# 298. Archive status

```text
HISTORICAL
REFUTED
LIMITED
SUPERSEDED
EFFECTIVE
ACTIVE
```

---

# 299. 這比「old」精確

---

# 300. Scientific memory maturity

成熟 science memory 應知道：

> 這個公式從哪個理論來、現在為什麼還在用、其原本 interpretation 是否仍被接受。

---

# 301. AI 特別需要

因為 AI 容易把不同時代文字混成 contemporaneous truth。

---

# 302. Historical semantics

同一詞：

$$
\text{ether}
$$

在不同年代不是同一概念。

---

# 303. 所以 temporal metadata

$$
t
$$

也是 semantic coordinate。

---

# 304. 完整 claim

$$
p^\star
=
p(D,C,t,F,S).
$$

這和先前真理邊界研究一致。

---

# 305. 時間是 theory meaning 的一部分

科學史資料庫不能去時間化。

---

# 306. 這也是 AI RAG 的問題

retriever 只看 lexical similarity，

可能把不同 ontology 混在一起。

---

# 307. Historical RAG 應加：

- date；
- framework；
- status；
- successor theory。

---

# 308. 這會減少 anachronism

---

# 309. 科學史不是裝飾

它可以直接改善 AI knowledge routing。

---

# 310. 例如查「ether」

系統先問：

$$
\text{which ether?}
$$

---

# 311. 查「Bohr orbit」

先顯示：

$$
\text{historical / pedagogical status}.
$$

---

# 312. 查「ideal gas」

顯示：

$$
\text{validity regime}.
$$

---

# 313. 這就是 status-aware retrieval

---

# 314. 對 proof corpus 也一樣

查某 lemma：

先看：

$$
\text{which parent version?}
$$

---

# 315. 歷史方法與 proof-space observatory 合流

$$
\boxed{
\text{context-aware lineage retrieval}.
}
$$

---

# 316. 未來研究一：Historical Lineage Dataset

建立：

$$
\text{Theory Revision Corpus}.
$$

---

# 317. 每個案例存：

- parent；
- successor；
- retained components；
- discarded components；
- primary sources；
- confidence。

---

# 318. 未來研究二：AI Salvage Benchmark

故意注入 parent defect，

讓 AI 產生 descendants。

---

# 319. 後來 reveal correction

測 salvage。

---

# 320. 未來研究三：Status-Aware RAG

看是否降低：

- anachronism；
- obsolete-theory hallucination；
- false equivalence。

---

# 321. 未來研究四：Historical Counterfactual Sandbox

讓 AI 在 historically inspired toy world 走多條 branch。

---

# 322. 不把它當真歷史

而是：

$$
\text{epistemic dynamics experiment}.
$$

---

# 323. 未來研究五：Structure survival predictor

訓練模型預測：

$$
\text{which descendants survive parent revision}.
$$

---

# 324. 預測器不能決定 truth

只是 audit priority。

---

# 325. 未來研究六：Theory-status compiler

輸入：

$$
\text{scientific corpus}.
$$

輸出：

```text
ACTIVE
LIMITED
HISTORICAL
REFUTED
EFFECTIVE
```

---

# 326. 這對 AI 科普和科研都重要

---

# 327. 最終歷史矩陣

| Case | Error / limitation | Retained asset | Transition type | Modern analogue |
|---|---|---|---|---|
| Carnot | conserved caloric | reversibility / efficiency | reinterpret + repair | wrong mechanism, stable structure |
| Phlogiston | combustion interpretation | gas observations | interpretation replacement | label/model error, data survival |
| Lorentz ether | privileged medium ontology | transformations | ontology replacement | representation survival |
| Bohr | precise orbit picture | quantized energy scaffold | scope restriction + replacement | limited model |
| Ideal gas | deliberate micro idealization | macroscopic law | domain conditioning | controlled approximation |
| EFT | non-fundamental by design | scale-relevant dynamics | explicit scope | mature model governance |
| AI formal spec | target mismatch | some proofs/tools | localized repair | specification revision |
| AI physics model | missing mechanism | trusted prior | residual correction | discrepancy modeling |

---

# 328. 這張表最重要的不是「錯誤」

而是：

$$
\boxed{
\text{transition type}.
}
$$

---

# 329. 如果知道 transition type

才能知道：

> 應該刪什麼，留什麼。

---

# 330. 結論

科學史真正反覆告訴我們的，不是：

> 錯誤很棒。

而是：

$$
\boxed{
\text{科學理論不是不可分割的單一真值塊。}
}
$$

一個 parent framework 可以同時包含：

- 被後來拒絕的 ontology；
- 仍有效的 empirical data；
- 被重新詮釋的 mathematical structure；
- 被保留的方法；
- 被限制到局部 domain 的 approximation。

Carnot 的 conserved caloric 被修正，但 reversibility 成為 thermodynamics 的核心資產；Priestley 的 phlogiston interpretation 被替換，但 oxygen observations 留下；Lorentz 的 stationary ether ontology 失去必要性，但 transformation structure 進入 special relativity；Bohr 的 classical-orbit mechanism 被 quantum mechanics 超越，但 quantized-energy scaffold 仍具有歷史、教育與局部計算價值；ideal gas 甚至從一開始就是一種明知失真的 model；effective field theory 則進一步把 scale limitation 直接寫入成熟的 theory practice。

所以科學史更接近：

$$
\boxed{
\text{revision}
+
\text{reinterpretation}
+
\text{selective retention}.
}
$$

而不是：

$$
\text{old false}
\rightarrow
\text{new true}.
$$

當 AI 開始以極高速生成 theorem、model、simulation、formal specification 與 research branches 時，這個歷史教訓變成了一個直接的資料工程問題。AI 不能只保存：

```text
THEORY = TRUE
```

或：

```text
THEORY = FALSE
```

它必須保存：

$$
\boxed{
\text{which component,
under which scope,
in which version,
with which descendants,
survived which revision}.
}
$$

這也讓「生產性錯置」從哲學直覺進入可操作制度。

歷史告訴我們：

$$
\boxed{
\exists P,P':
P\text{ is revised}
\land
\mathcal D_{\mathrm{surv}}(P\rightarrow P')\neq\varnothing.
}
$$

AI 則第一次讓我們有機會進一步測量：

$$
\boxed{
\text{which kinds of }P\rightarrow P'
\text{ systematically maximize durable descendant survival}.
}
$$

因此本文最終提出：

$$
\boxed{
\textbf{The right unit of scientific continuity is not the theory name, but the lineage of structures, observations, methods, and claims that survive revision.}
}
$$

以及：

$$
\boxed{
\textbf{What survives a theory may be scientifically more informative than the binary fact that the theory itself survived.}
}
$$

這兩句話把 Carnot 的十九世紀問題與 AI 的二十一世紀研究基礎設施真正接在了一起。

---

# 參考文獻

1. Norton, J. D. (2022). **How Analogy Helped Create the New Science of Thermodynamics.** *Synthese*, 200, 269. https://doi.org/10.1007/s11229-022-03708-9

2. Carnot, S. (1824). **Réflexions sur la puissance motrice du feu et sur les machines propres à développer cette puissance.**

3. American Chemical Society. **Joseph Priestley, Discoverer of Oxygen — National Historic Chemical Landmark.** https://www.acs.org/education/whatischemistry/landmarks/josephpriestleyoxygen.html

4. American Chemical Society. **Antoine-Laurent Lavoisier: The Chemical Revolution — International Historic Chemical Landmark.** https://www.acs.org/education/whatischemistry/landmarks/lavoisier.html

5. Einstein, A. (1905). **Zur Elektrodynamik bewegter Körper.** *Annalen der Physik*, 17, 891–921.

6. Einstein, A. (1920). **Ether and the Theory of Relativity.** Leiden lecture; English translation collected in *Sidelights on Relativity*.

7. Janssen, M. and related historical scholarship on Lorentz transformations and pre-relativistic electrodynamics. See also historical analyses of Lorentz’s theorem of corresponding states.

8. OpenStax. **The Bohr Model.** *Chemistry: Atoms First* and *Physics*. Modern educational summary of the model’s achievements and limitations.

9. Frigg, R., & Hartmann, S. **Models in Science.** *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/models-science/

10. Batterman, R. W., & Rice, C. C. (2014). **Minimal Model Explanations.** *Philosophy of Science*, 81(3), 349–376. https://doi.org/10.1086/676677

11. Rice, C. (2021). **Leveraging Distortions: Explanation, Idealization, and Universality in Science.** MIT Press.

12. Spagnesi, L. (2025). **Truth, Understanding, and Normativity in Scientific Models.** *Synthese*, 206.

13. Frigg, R., Nguyen, J., & collaborators (2025). **Stabilising Understanding.** *Philosophical Studies*. On idealized models, stability, and noetic cores.

14. Weingarten, K. (2026). **Productive Idealizations for Scientific Understanding: A Case Study in Effective Theories.** PhilSci-Archive preprint. https://philsci-archive.pitt.edu/27959/

15. Stanford Encyclopedia of Philosophy. **Intertheory Relations in Physics.** Spring 2026 edition; discussion of effective field theory and scale-sensitive theory relations.

16. Ebers, M. R., Steele, K. M., & Kutz, J. N. (2022). **Discrepancy Modeling Framework: Learning missing physics, modeling systematic residuals, and disambiguating between deterministic and random effects.** arXiv:2203.05164.

17. Wang, Y. (2026). **Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy.** arXiv:2606.23215.

18. Ma, L. et al. (2026). **Physics-guided correction for operator learning under model misspecification.** arXiv:2606.03469.

19. Strouwen, A., & Micluţa-Câmpeanu, S. (2026). **Experimental Design for Missing Physics.** arXiv:2604.01231.

20. Strouwen, A. (2026). **Bayesian Inference for Missing Physics.** arXiv:2603.14918.

21. Ye, Z. et al. (2026). **Intent-aligned Formal Specification Synthesis via Traceable Refinement.** arXiv:2604.10392.

22. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493.

23. Zhang, K. et al. (2026). **Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization.** arXiv:2606.31002.

24. King, M. (2025). **Experiment and the Pursuit of Ugly Models.** *European Journal for Philosophy of Science*, 15, Article 55.

25. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：歷史案例比較表

| Case | Error Type | Retained Structure | Repair Mode | Descendant Status |
|---|---|---|---|---|
| Carnot | ontology | reversibility / efficiency | reinterpret + repair | high historical retention |
| Phlogiston | interpretation / mechanism | oxygen observations | replace interpretation | empirical survival |
| Lorentz ether | ontology | transformation mathematics | reinterpret | mathematical survival |
| Bohr | mechanism / scope | discrete energies | restrict + supersede | partial survival |
| Ideal gas | deliberate idealization | macroscopic law | domain-bound use | effective survival |
| EFT | explicit non-fundamentality | low-energy structure | scope declaration | designed persistence |

---

## 附錄 B：Historical Revision Record

```yaml
case_id:
historical_period:
parent_framework:

components:
  ontology:
  mechanism:
  domain:
  representation:
  assumptions:
  observations:

revision:
  successor_framework:
  retained:
  reinterpreted:
  repaired:
  discarded:

descendants:
  empirical:
  mathematical:
  methodological:
  instrumental:
  conceptual:
  ontological:

confidence:
  direct_source:
  retrospective_reconstruction:
  counterfactual_claim:
```

---

## 附錄 C：AI Translation Record

```yaml
parent_version:
error_type:
scope:
known_failure_mode:

descendant_assets:
  theorem:
  observation:
  tool:
  dataset:
  method:
  obstruction:
  negative_result:

revision:
  new_parent:
  changed_components:

reaudit:
  retained:
  repaired:
  transferred:
  discarded:
  unknown:
```

---

## 附錄 D：七種暫定結構類型

| Code | 名稱 |
|---|---|
| OWSR | Ontology-Wrong / Structure-Retained |
| IWOR | Interpretation-Wrong / Observation-Retained |
| ORMR | Ontology-Replaced / Mathematics-Retained |
| MLQR | Mechanism-Limited / Quantized-Structure-Retained |
| KIDG | Known-Idealization / Deviation-Generative |
| DRIR | Detail-Removed / Invariant-Revealed |
| NFDE | Non-Fundamental / Domain-Explicit |

這些只是比較標籤，不是自然種類定理。

---

## 附錄 E：一句話版本

$$
\boxed{
\text{科學理論被修正時，真正值得追蹤的不是「舊理論死了沒有」，而是「哪些結構穿過了理論更替仍然活著」。}
}
$$

對 AI 而言，這句話會直接變成資料庫與研究記憶的設計原則。


<!-- END LSI-PSD-11 -->

---


<!-- BEGIN LSI-PSD-12 -->

# LSI-PSD-12 — AI 證明空間觀測站：從 NS-203 到文明級研究記憶

## AI Proof-Space Observatory: From NS-203 to Civilization-Scale Research Memory

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 12  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 系列封頂工程論文 / Observatory Architecture and Research-Memory Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文把 LSI-PSD 前十一篇的方法論轉換成一個可實作的 AI 長程數學研究觀測站架構。本文中的 Proof-Space Observatory 是研究資訊基礎設施，不是數學真理機器。它可以保存、去重、驗證、追蹤、量測與路由 proof-related research artifacts，但不能由 corpus saturation 自動推出命題為假、不可證、獨立、不可判定或問題 framing 錯誤。本文提出的資料模型、指標、runtime、dashboard、API 與治理機制均屬可實驗工程提案；是否有效，必須透過可解 ground-truth benchmark、formal verifier、independent audit 與長期部署資料檢驗。

---

## 摘要

LSI-PSD 系列前十一篇建立了一套從長程 AI 數學研究資料中觀察 proof space 的方法論：

$$
\text{search regime}
\rightarrow
\text{coverage}
\rightarrow
\text{semantic quotient}
\rightarrow
\text{higher-order sampling}
\rightarrow
\text{local saturation}
\rightarrow
\text{obstruction confluence}
\rightarrow
\text{truth--generativity separation}
\rightarrow
\text{productive mis-specification}
\rightarrow
\text{productive window}
\rightarrow
\text{non-conclusion firewall}
\rightarrow
\text{historical lineage}.
$$

本文將這些概念收斂成一個真正可運行的系統：

$$
\boxed{
\textbf{AI Proof-Space Observatory}
}
$$

簡稱：

$$
\boxed{
\textbf{PSO}.
}
$$

PSO 的基本目標不是「自動證明所有定理」，而是讓長期、多人、多模型、多工具的數學研究第一次具有一個可被持續觀察、回放、稽核與重新路由的研究記憶層。系統不再把一輪 AI 輸出只視為一篇文字，而拆成：

$$
\text{Problem},
\text{Claim},
\text{Assumption},
\text{Lemma},
\text{Route},
\text{Proof State},
\text{Obstruction},
\text{Basin},
\text{Certificate},
\text{Revision},
\text{Descendant},
\text{Experiment}.
$$

所有物件以 canonical ID、版本、來源、依賴與 epistemic status 管理，並形成 typed multilayer graph。

本文提出 PSO 的核心資料圖：

$$
\mathcal G_{\mathrm{PSO}}
=
(
V,
E,
\tau_V,
\tau_E,
\sigma,
\pi,
\chi
),
$$

其中：

- $V$：研究節點集合；
- $E$：typed edges；
- $\tau_V$：節點型別；
- $\tau_E$：邊型別；
- $\sigma$：epistemic status；
- $\pi$：provenance；
- $\chi$：certificate / validation metadata。

系統以 event sourcing 保存每一次研究狀態改變：

$$
\mathcal S_{t+1}
=
\operatorname{Apply}(
\mathcal S_t,
e_t
),
$$

而不是只保存「最新版本」。因此所有：

- claim upgrade；
- claim downgrade；
- theorem repair；
- assumption deletion；
- parent revision；
- obstruction merge；
- basin split；
- descendant salvage；

都具有可逆歷史。

本文定義 PSO 的五層 runtime：

$$
\boxed{
\begin{aligned}
L_1 &: \text{Canonical Artifact Layer}\\
L_2 &: \text{Verification and Extraction Layer}\\
L_3 &: \text{Proof-Space Graph Layer}\\
L_4 &: \text{Measurement and Diagnosis Layer}\\
L_5 &: \text{Research Routing and Governance Layer}.
\end{aligned}
}
$$

在第 $L_1$ 層，系統保存原始 UTF-8 source、proof source、compiler output、logs、datasets、code、plots 與 checksum；第 $L_2$ 層負責 formal verification、statement extraction、dependency extraction、semantic equivalence candidate generation 與 human/model audit；第 $L_3$ 層形成 claim graph、proof-state graph、route graph、obstruction graph、basin graph 與 lineage graph；第 $L_4$ 層計算：

$$
I_k,
\quad
\rho_k,
\quad
S_K,
\quad
C_{\mathrm{ind}},
\quad
\Phi_E,
\quad
\mathcal W_P,
$$

以及 coverage、novelty、confluence、survival、zombie-knowledge rate、research cost 等指標；第 $L_5$ 層則使用這些量決定：

$$
\text{continue},
\text{branch},
\text{verify},
\text{repair},
\text{escape},
\text{reframe},
\text{pause},
\text{archive}.
$$

本文將 2026 年 formal theorem proving 基礎設施視為相鄰工程支撐，而不是直接等同於 PSO。LeanMarathon 把 evolving proof DAG 同時作為 formal skeleton、natural-language proof graph 與 shared system of record；TheoremGraph 建立跨 informal/formal mathematics 的 statement-level dependency graph；AXLE 提供可擴展、多版本、隔離式 Lean proof verification 與 extraction infrastructure；LeanSearch v2 顯示 global premise retrieval 可直接影響 end-to-end proof success；TheoremBench 以 theorem-level coverage 與 supporting subtheorems 衡量 partial proof progress；BlueprintRepair 則將 proof blueprint repair 限制為 schema-checked typed local edits，並禁止偷偷改動 target theorem。這些系統共同顯示，AI theorem proving 正從單一 tactic generation 走向：

$$
\boxed{
\text{structured proof state}
+
\text{graph memory}
+
\text{typed repair}
+
\text{scalable verification}.
}
$$

PSO 的差異在於，它把這種 formal proving infrastructure 再向外擴張成**研究過程觀測學**：未證明的路線、失敗、negative result、obstruction、reformulation、descendant survival 與 historical revision 同樣是第一等物件。

本文最後以 NS-203 corpus 作為第一個 migration target。既有 v0.1 observatory 已對 203 份 NS paper-like artifacts 建立 paper-level route graph，得到 sequence、dependency、similarity、confluence 與 higher-order sampling 的初步量測。本文提出第二階段 migration：

$$
203\ \text{papers}
\rightarrow
\text{claim/lemma/assumption/obstruction graph},
$$

再把每個 NS artifact 轉成：

$$
A_i
=
(
Q_i,
\mathcal A_i,
L_i,
C_i,
O_i,
R_i,
S_i
).
$$

第一版 PSO 不需要立即理解所有 NS 數學，而應先建立：

1. canonical source；
2. exact provenance；
3. theorem-level extraction；
4. assumption lineage；
5. obstruction ID；
6. status type；
7. cross-paper dependency；
8. human-audited gold set。

只有在這些基礎上，才有資格更精確地測量「二階、三階、X 階採樣」與局部 proof-space saturation。

本文最終提出：

$$
\boxed{
\textbf{The future unit of mathematical research memory should not be the paper, but the versioned, typed, provenance-preserving research relation.}
}
$$

以及：

$$
\boxed{
\textbf{A civilization-scale AI research system should remember not only what was proved, but what was tried, why it failed, what survived revision, and which unexplored regions remain.}
}
$$

**關鍵詞：** Proof-Space Observatory、AI 數學研究、研究記憶、proof graph、obstruction graph、claim graph、event sourcing、epistemic type、theorem proving、Lean、NS-203、文明級知識、AI co-mathematician、長程研究

---

# 1. 問題的提出：為什麼「論文資料夾」已經不夠

傳統研究記憶單位是：

$$
\text{paper}.
$$

一篇 paper 存：

- 題目；
- abstract；
- theorem；
- proof；
- references。

---

# 2. 長程 AI 研究破壞了 paper 作為唯一單位的假設

AI 可以在一天內產生：

$$
10^2
$$

甚至更多 research artifacts。

---

# 3. Artifact 可能不是 paper

它可能只是：

- one proof attempt；
- one lemma；
- one failed route；
- one audit；
- one counterexample search；
- one simulation；
- one repair。

---

# 4. 如果全部壓成 paper

會失去：

$$
\boxed{
\text{process structure}.
}
$$

---

# 5. 如果只存聊天記錄

又會失去：

- canonical source；
- stable ID；
- dependency；
- status；
- verification。

---

# 6. 所以需要新的 research memory primitive

本文提出：

$$
\boxed{
\text{Versioned Research Object}
}
$$

簡稱：

$$
VRO.
$$

---

# 7. VRO 的最小條件

每個物件必須有：

```text
ID
TYPE
SOURCE
VERSION
STATUS
PROVENANCE
DEPENDENCIES
VALIDATION
TIMESTAMP
```

---

# 8. Paper 只是 VRO 的一種

其他：

- claim；
- lemma；
- obstruction；
- experiment；
- certificate；
- route。

---

# 9. PSO 的第一原則

$$
\boxed{
\textbf{Do not reduce research history to final prose.}
}
$$

---

# 10. 第二原則

$$
\boxed{
\textbf{Do not reduce mathematical status to natural-language confidence.}
}
$$

---

# 11. 第三原則

$$
\boxed{
\textbf{Do not discard failures before canonicalizing them.}
}
$$

---

# 12. 第四原則

$$
\boxed{
\textbf{Do not overwrite parent knowledge when revising it.}
}
$$

---

# 13. 第五原則

$$
\boxed{
\textbf{Every strong claim must trace to a certificate or declared evidence type.}
}
$$

---

# 14. PSO 五層 runtime

$$
L_1
\rightarrow
L_2
\rightarrow
L_3
\rightarrow
L_4
\rightarrow
L_5.
$$

---

# 15. $L_1$：Canonical Artifact Layer

保存：

- `.md`；
- `.lean`；
- `.py`；
- `.json`；
- `.csv`；
- images；
- logs；
- ZIP；
- checksum。

---

# 16. Canonical source

所有正式文本：

$$
\boxed{
\text{UTF-8 source artifact}
}
$$

優先於：

$$
\text{rendered conversation}.
$$

---

# 17. Source immutability

版本：

$$
v_1
$$

一旦 commit，

不 silent rewrite。

---

# 18. 修改產生：

$$
v_2.
$$

---

# 19. Hash

每版：

$$
h_v
=
\operatorname{SHA256}(source_v).
$$

---

# 20. $L_2$：Verification and Extraction Layer

輸入：

$$
\text{raw artifact}.
$$

輸出：

$$
\text{structured research objects}.
$$

---

# 21. Formal verification

對 Lean：

$$
\operatorname{Check}(\Pi,Q)=1.
$$

---

# 22. 但 formal verification 不等於 semantic fidelity

所以另存：

$$
F_S.
$$

---

# 23. Extraction

抽：

- theorem statement；
- assumptions；
- definitions；
- dependencies；
- proof terms；
- compiler feedback。

---

# 24. Informal artifact extraction

對 Markdown paper 抽：

$$
\text{Claim},
\text{Assumption},
\text{Lemma},
\text{Obstruction},
\text{Status}.
$$

---

# 25. Extraction 不是 authority

自動抽取只產生：

$$
\text{candidate structured record}.
$$

---

# 26. 高風險 record 需要 audit

例如：

- obstruction equivalence；
- theorem equivalence；
- parent revision；
- framing defect。

---

# 27. $L_3$：Proof-Space Graph Layer

建立多層圖。

---

# 28. Claim Graph

$$
G_C.
$$

邊：

- implies；
- contradicts；
- refines；
- equivalent；
- depends-on。

---

# 29. Assumption Graph

$$
G_A.
$$

追蹤：

$$
\text{which claims depend on which assumptions}.
$$

---

# 30. Lemma Graph

$$
G_L.
$$

對 formal theorem：

$$
L_i\rightarrow L_j.
$$

---

# 31. Proof-State Graph

$$
G_S.
$$

節點：

$$
s_t.
$$

邊：

$$
s_t\xrightarrow{a_t}s_{t+1}.
$$

---

# 32. Route Graph

$$
G_R.
$$

節點可代表：

$$
r_i.
$$

---

# 33. Obstruction Graph

$$
G_O.
$$

節點：

$$
O_i.
$$

邊：

- refines；
- revives；
- resolves；
- inherits；
- co-converges。

---

# 34. Basin Graph

$$
G_B.
$$

描述：

$$
\text{local research regions}.
$$

---

# 35. Lineage Graph

$$
G_H.
$$

追蹤：

$$
P^{(0)}
\rightarrow
P^{(1)}
\rightarrow
P^{(2)}.
$$

---

# 36. Certificate Graph

$$
G_\chi.
$$

把：

- proof；
- counterexample；
- independence；
- no-go；
- faithfulness audit；

連到 claim。

---

# 37. Multilayer graph

整體：

$$
\boxed{
\mathcal G_{\mathrm{PSO}}
=
G_C
\cup
G_A
\cup
G_L
\cup
G_S
\cup
G_R
\cup
G_O
\cup
G_B
\cup
G_H
\cup
G_\chi.
}
$$

---

# 38. 不能只用單一 graph schema

因為：

$$
\text{proof-state edge}
$$

和：

$$
\text{historical-revision edge}
$$

不是同型。

---

# 39. Typed edges 是必要條件

$$
\tau_E(e).
$$

---

# 40. $L_4$：Measurement and Diagnosis Layer

這裡才計算 LSI-PSD 指標。

---

# 41. Coverage

$$
I_k(N).
$$

---

# 42. Audited novelty yield

$$
\rho_k(N,W).
$$

---

# 43. Local saturation

$$
S_K(B).
$$

---

# 44. Confluence

$$
C_{\mathrm{ind}}(O).
$$

---

# 45. Epistemic fertility

$$
\Phi_E(P).
$$

---

# 46. Productive window

$$
\mathcal W_P.
$$

---

# 47. Zombie knowledge

$$
Z_K.
$$

---

# 48. Descendant survival

$$
S_D.
$$

---

# 49. Research cost

$$
C_R.
$$

---

# 50. $L_5$：Routing and Governance Layer

量測後不直接判真理。

只決定下一個 research action。

---

# 51. Actions

$$
a
\in
\{
\text{continue},
\text{branch},
\text{verify},
\text{repair},
\text{escape},
\text{reframe},
\text{pause},
\text{archive}
\}.
$$

---

# 52. Meta-policy

$$
\Pi_{\mathrm{meta}}
:
\mathcal S_t
\rightarrow
a_t.
$$

---

# 53. Routing 不等於自治判決

任何：

$$
\text{Verdict upgrade}
$$

需 certificate。

---

# 54. PSO 物件一：Problem

```yaml
problem_id:
canonical_statement:
informal_statement:
formal_statement:
domain:
formal_system:
status:
```

---

# 55. Problem 不是永恆不變

版本：

$$
Q^{(v)}.
$$

---

# 56. PSO 物件二：Claim

```yaml
claim_id:
text:
formalization:
scope:
status:
evidence:
```

---

# 57. PSO 物件三：Assumption

```yaml
assumption_id:
statement:
scope:
origin:
status:
```

---

# 58. PSO 物件四：Lemma

```yaml
lemma_id:
statement:
proof:
dependencies:
verification:
```

---

# 59. PSO 物件五：Proof State

```yaml
state_id:
goals:
hypotheses:
environment:
parent_state:
action:
```

---

# 60. PSO 物件六：Route

```yaml
route_id:
problem:
method_family:
representation:
premise_set:
states:
endpoint:
```

---

# 61. PSO 物件七：Obstruction

```yaml
obstruction_id:
normalized_gap:
assumptions:
route_support:
audit:
status:
```

---

# 62. PSO 物件八：Basin

```yaml
basin_id:
members:
conductance:
recurrence:
yield:
saturation:
```

---

# 63. PSO 物件九：Certificate

```yaml
certificate_id:
type:
target_claim:
formal_system:
source:
verifier:
status:
```

---

# 64. Certificate types

$$
\{
\text{proof},
\text{counterexample},
\text{no-go},
\text{independence},
\text{undecidability},
\text{faithfulness}
\}.
$$

---

# 65. PSO 物件十：Revision

```yaml
revision_id:
parent_version:
new_version:
changed_components:
reason:
affected_descendants:
```

---

# 66. PSO 物件十一：Descendant

不需要獨立新本體。

它是任何 VRO 對 parent 的 lineage relation：

$$
d\rightarrow P.
$$

---

# 67. PSO 物件十二：Experiment

```yaml
experiment_id:
hypothesis:
branches:
controls:
budget:
metrics:
result:
```

---

# 68. Canonical ID

所有 ID 應：

$$
\text{stable across display changes}.
$$

---

# 69. 不用 title 當 ID

title 可改。

---

# 70. 建議 ID

```text
PSO-Q-000001
PSO-C-000123
PSO-O-000044
PSO-R-000081
```

---

# 71. Content hash 另存

stable ID：

$$
\neq
$$

content hash。

---

# 72. 為什麼要分

內容更新：

$$
h_v\neq h_{v+1}
$$

但：

$$
\operatorname{ObjectID}
$$

仍相同。

---

# 73. Event sourcing

系統不直接修改 current state。

---

# 74. 每個變化寫 event

$$
e_t.
$$

---

# 75. State reconstruction

$$
\mathcal S_t
=
\operatorname{Fold}(e_0,\ldots,e_t).
$$

---

# 76. Event types

```text
CREATE
VERIFY
REFUTE
MERGE
SPLIT
REVISE
LINK
UNLINK
UPGRADE_STATUS
DOWNGRADE_STATUS
ARCHIVE
```

---

# 77. Event sourcing 的好處一：可回放

知道：

> 這個 claim 為什麼從 hypothesis 變 supported。

---

# 78. 好處二：防 status laundering

upgrade 有 event。

---

# 79. 好處三：parent revision 可追

---

# 80. 好處四：可建立時間序列研究學

---

# 81. Epistemic type system

沿用第 10 篇。

---

# 82. Status types

```text
OBSERVATION
HYPOTHESIS
SUPPORTED_HYPOTHESIS
EMPIRICAL_NO_GO
FORMAL_NO_GO
PROVEN
REFUTED
INDEPENDENT_RELATIVE_TO_T
UNDECIDABLE_CLASS
ARCHIVED
```

---

# 83. Illegal cast

$$
\text{HYPOTHESIS}
\not\rightarrow
\text{PROVEN}
$$

without certificate。

---

# 84. Status transition table

每種 transition 都有：

$$
\text{required certificate type}.
$$

---

# 85. Provenance

每個 VRO 存：

- agent；
- model；
- human；
- source file；
- parent prompt；
- tool；
- timestamp。

---

# 86. Model identity 不等於 epistemic authority

模型欄只用來研究 genealogy。

---

# 87. Agent genealogy

兩條 route：

$$
r_1,r_2
$$

如果共享：

- same memory；
- same prompt；
- same parent；

independence 降低。

---

# 88. Research genealogy graph

$$
G_G.
$$

---

# 89. 這直接支援：

$$
C_{\mathrm{ind}}.
$$

---

# 90. Canonical math source

公式一律保存：

$$
\text{LaTeX source}.
$$

---

# 91. 不把 rendered glyph 當 source

避免：

$$
\text{Unicode round trip}.
$$

---

# 92. Render layer

可以：

- KaTeX；
- MathJax；
- Lean pretty printer。

但 render：

$$
\neq
$$

canonical。

---

# 93. Statement normalization

自動 normalization 只能產生 candidate。

---

# 94. 不能 silent rewrite theorem

---

# 95. BlueprintRepair 的重要工程啟發

typed local edit：

$$
\Delta_i
$$

明示 target node。

---

# 96. Target theorem 不可偷改

這應成為 PSO repair rule。

---

# 97. Repair operation schema

```yaml
operation:
target_node:
precondition:
edit:
postcondition:
verification:
```

---

# 98. Free-form rewrite 是高風險操作

需要更強 audit。

---

# 99. LeanMarathon 的 shared system of record

evolving proof DAG：

$$
G_{\mathrm{proof}}.
$$

---

# 100. PSO 的擴張

proof DAG 之外再加：

$$
\text{failure / history / status / basin / experiment}.
$$

---

# 101. TheoremGraph 的啟發

statement-level graph 可跨：

$$
\text{informal}
\leftrightarrow
\text{formal}.
$$

---

# 102. 這非常適合 PSO 的兩層 claim

$$
C_I
$$

informal claim，

$$
C_F
$$

formal claim。

---

# 103. Faithfulness edge

$$
C_I
\xleftrightarrow[\text{audit}]{}
C_F.
$$

---

# 104. Faithfulness confidence

$$
F_S(C_I,C_F).
$$

---

# 105. AXLE 的啟發

verification utilities 應成獨立 service。

---

# 106. PSO 不應把 verifier 邏輯塞進 LLM prompt

---

# 107. Verification service

輸入：

$$
(\text{source},\text{version},\text{environment}).
$$

---

# 108. 輸出：

- success；
- diagnostics；
- dependencies；
- metadata。

---

# 109. 多 Lean / Mathlib 版本

環境本身必須版本化。

---

# 110. 因為：

$$
\Pi@v_1
$$

不一定：

$$
\Pi@v_2.
$$

---

# 111. LeanSearch v2 的啟發

premise retrieval 應分：

$$
\text{local}
$$

與：

$$
\text{global}.
$$

---

# 112. PSO premise object

每個 route 存：

$$
P_r.
$$

---

# 113. Retrieval trace

存：

```text
query
retrieved candidates
rank
selected
used
```

---

# 114. 這能分析 premise basin lock-in

---

# 115. TheoremBench 的啟發

只問 final theorem solved：

$$
0/1
$$

不夠。

---

# 116. PSO 必須測 partial theorem coverage

$$
C_T.
$$

---

# 117. Supporting-subtheorem coverage

$$
C_{\mathrm{sub}}.
$$

---

# 118. Token efficiency

$$
E_{\mathrm{token}}
=
\frac{
\text{audited progress}
}{
\text{tokens}
}.
$$

---

# 119. Verification-call efficiency

$$
E_V
=
\frac{
\text{audited progress}
}{
\text{verifier calls}
}.
$$

---

# 120. Cost-normalized novelty

$$
\nu_C
=
\frac{
\Delta U
}{
C_R
}.
$$

---

# 121. PSO 核心指標群

$$
\boxed{
\mathbf M_{\mathrm{PSO}}
=
(
I_k,
\rho_k,
S_K,
C_{\mathrm{ind}},
\Phi_E,
S_D,
Z_K,
C_T,
E_{\mathrm{token}},
E_V
).
}
$$

---

# 122. 不做 single leaderboard score

因為會失真。

---

# 123. Dashboard 第一頁：Problem Overview

顯示：

- canonical statement；
- status；
- formalizations；
- versions；
- certificate。

---

# 124. 第二頁：Research Map

顯示：

$$
G_R,
G_O,
G_B.
$$

---

# 125. 第三頁：Saturation

顯示：

$$
\rho_k(t),
S_K(B).
$$

---

# 126. 第四頁：Obstruction Atlas

顯示：

$$
C_{\mathrm{ind}}(O),
Z(O),
R_O.
$$

---

# 127. 第五頁：Lineage

顯示：

$$
P^{(0)}\rightarrow P^{(1)}.
$$

---

# 128. 第六頁：Descendant Survival

顯示：

- strong；
- repairable；
- transferred；
- refuted；
- unknown。

---

# 129. 第七頁：Experiment Lab

控制：

- representation；
- method；
- model；
- budget；
- branch。

---

# 130. 第八頁：Epistemic Status

每個 claim：

$$
\text{type checked}.
$$

---

# 131. Dashboard 禁止紅色等於「假」

顏色只表示 status。

---

# 132. 例如

紅：

$$
\text{active obstruction}.
$$

不是：

$$
\text{false theorem}.
$$

---

# 133. Search

PSO search 不只全文搜尋。

---

# 134. Query examples

> 找所有依賴 assumption A-17 的 claims。

---

# 135. Query

> 找所有跨三個 method family 命中 O-31 的 routes。

---

# 136. Query

> 找所有 parent revision 後仍存活的 lemmas。

---

# 137. Query

> 找所有 Level-3 saturation basin。

---

# 138. Query

> 找所有 status=SUPPORTED_HYPOTHESIS 但沒有最近 audit 的 claims。

---

# 139. Research query language

未來可建立：

$$
\text{PSO-QL}.
$$

---

# 140. 示例

```text
MATCH Route -> Obstruction
WHERE obstruction.confluence_ind > 3
AND route.method_family_count >= 2
RETURN route, obstruction
```

---

# 141. Storage architecture

本文不要求單一資料庫。

---

# 142. 建議分層

1. object store；
2. relational metadata；
3. graph index；
4. vector / semantic index；
5. event log。

---

# 143. Object store

保存：

$$
\text{canonical files}.
$$

---

# 144. Relational DB

保存：

- IDs；
- versions；
- statuses；
- metrics。

---

# 145. Graph DB

保存：

$$
E.
$$

---

# 146. Vector index

只用於：

$$
\text{candidate retrieval}.
$$

---

# 147. Vector similarity 不能作 semantic truth

---

# 148. Event log

append-only。

---

# 149. 資料庫應可重建

如果 graph DB 壞，

從：

$$
\text{canonical artifacts + events}
$$

重建。

---

# 150. Canonical state 不應只存在 vector DB

---

# 151. Artifact pipeline

$$
\text{Ingest}
\rightarrow
\text{Hash}
\rightarrow
\text{Parse}
\rightarrow
\text{Extract}
\rightarrow
\text{Validate}
\rightarrow
\text{Link}
\rightarrow
\text{Measure}.
$$

---

# 152. Ingest

來源：

- AI；
- human；
- Git；
- paper；
- proof assistant；
- experiment。

---

# 153. Hash

建立：

$$
h.
$$

---

# 154. Parse

不要在 parse 階段改 source。

---

# 155. Extract

產生 candidates。

---

# 156. Validate

依 type 使用：

- Lean；
- Python；
- manual；
- cross-model。

---

# 157. Link

建立 edges。

---

# 158. Measure

最後才算 metrics。

---

# 159. Semantic quotient pipeline

$$
x_i,x_j
\rightarrow
\text{candidate similarity}
\rightarrow
\text{structural compare}
\rightarrow
\text{audit}
\rightarrow
\text{merge / no merge}.
$$

---

# 160. False merge 風險大於 false split

因為 false merge 會偽造 saturation。

---

# 161. 所以 merge threshold 應保守

---

# 162. Obstruction pipeline

$$
\text{failure event}
\rightarrow
\text{gap extraction}
\rightarrow
\text{assumption normalization}
\rightarrow
O_{\mathrm{candidate}}
\rightarrow
\text{audit}.
$$

---

# 163. Basin pipeline

先 graph candidate。

---

# 164. 再 human / theorem-level audit。

---

# 165. Basin 版本化

$$
B^{(v)}.
$$

---

# 166. 因為新 edge 可能：

- merge；
- split；
- dissolve。

---

# 167. Saturation detector

輸入：

$$
B^{(v)}.
$$

---

# 168. 不能對舊 basin ID 永久保證 status

---

# 169. Measurement version

每個 metric：

$$
M@v.
$$

---

# 170. 這可防止 metric drift

---

# 171. Novelty detector audit

至少：

- fixed-window；
- permutation baseline；
- corpus-size correction；
- semantic quotient；
- manual sample。

---

# 172. Confluence detector audit

至少：

- genealogy correction；
- assumption normalization；
- route independence；
- representation distance。

---

# 173. Productive-mis-specification detector audit

至少：

- parent revision；
- descendant re-audit；
- random control；
- ground truth。

---

# 174. Non-conclusion firewall

每個 dashboard verdict card 先檢查：

$$
\text{certificate}.
$$

---

# 175. 沒 certificate

最大輸出：

$$
\text{SUPPORTED_HYPOTHESIS}.
$$

---

# 176. Research Router

核心元件：

$$
\boxed{
\text{PSO Router}
}
$$

---

# 177. Router 不生成 proof

它分配研究。

---

# 178. Router input

$$
\mathbf x_t
=
(
S_K,
C_{\mathrm{ind}},
\rho_k,
\Gamma_{\mathrm{esc}},
C_R,
\mathfrak F
).
$$

---

# 179. Router output

$$
a_t.
$$

---

# 180. Sample policy

如果：

$$
\rho_k\gg0,
$$

continue。

---

# 181. 如果：

$$
S_K(B)\gg0,
$$

escape。

---

# 182. 如果：

$$
C_{\mathrm{ind}}(O)\gg0,
$$

focus obstruction。

---

# 183. 如果：

$$
Z_K\gg0,
$$

pause generation，

先 re-audit。

---

# 184. 如果 formalization fidelity 低

pause proving。

先修 statement。

---

# 185. 如果 cross-regime saturation 高

進 meta-level investigation。

---

# 186. 不直接 verdict

---

# 187. Human role

人類不是每步 proof 都要看。

---

# 188. Human priority

集中：

- high-centrality obstruction；
- status upgrade；
- framing change；
- ambiguous equivalence；
- public release。

---

# 189. AI role

適合：

- extraction；
- candidate relation；
- branch generation；
- proof repair；
- audit suggestions；
- literature mapping。

---

# 190. Formal verifier role

只判：

$$
\text{formal validity}.
$$

---

# 191. No single observer is enough

PSO 本身是一個：

$$
\boxed{
\text{multi-observer research system}.
}
$$

---

# 192. Observer separation

至少：

- generator；
- verifier；
- auditor；
- router。

---

# 193. Generator 不應自評為 final authority

---

# 194. Verifier 不懂全部 semantic intent

---

# 195. Auditor 檢查 intent / relation

---

# 196. Router 決定下一步

---

# 197. 多 AI 架構

可設：

$$
A_G,A_V,A_A,A_R.
$$

---

# 198. Cross-model audit

關鍵 claim 給不同 model。

---

# 199. 但不同 model 不代表完全獨立

genealogy 仍要記。

---

# 200. Memory 分層

## Hot

當前 problem / branch。

---

# 201. Warm

活躍 basin / obstruction。

---

# 202. Cold

完整歷史 artifact。

---

# 203. Frozen

formal certificates / release packages。

---

# 204. Hot memory 可壓縮

但：

$$
\text{canonical source}
$$

不可丟。

---

# 205. Compression pointer

摘要只存：

$$
\text{references to source IDs}.
$$

---

# 206. 不做 lossy replacement

---

# 207. Garbage collection

不能用：

> 最近沒用。

作唯一刪除條件。

---

# 208. Archive > delete

research history 預設 archive。

---

# 209. Delete 只針對：

- duplicate raw cache；
- invalid temporary artifact；
- explicit policy。

---

# 210. Negative knowledge 保存

尤其：

$$
\text{failed route}.
$$

---

# 211. 但失敗 log 需要壓縮成 canonical obstruction

否則 storage 爆炸。

---

# 212. Failure compaction

$$
10^4\ \text{events}
\rightarrow
50\ \text{obstruction classes}
+
\text{provenance links}.
$$

---

# 213. 這就是 semantic compression

---

# 214. Civilization-scale research memory

如果研究 corpus：

$$
N\rightarrow10^9
$$

artifact，

全文 pairwise compare 不可行。

---

# 215. Candidate generation

先用 cheap features：

- terms；
- symbols；
- dependencies；
- embedding；
- explicit links。

---

# 216. 再深度 audit。

---

# 217. Complexity

避免：

$$
O(N^2)
$$

全比較。

---

# 218. Incremental graph update

新節點：

$$
v_{n+1}
$$

只找候選 neighborhood。

---

# 219. Dynamic communities

局部更新 basin。

---

# 220. Distributed observatory

不同 research domain 可有 local PSO。

---

# 221. Federation

$$
\text{PSO}_1
\leftrightarrow
\text{PSO}_2.
$$

---

# 222. Shared schema

只交換：

- typed claims；
- certificates；
- public provenance；
- hashes。

---

# 223. 私有研究可以只交換摘要／fingerprint

---

# 224. Cross-domain transfer

例如 NS obstruction：

$$
O_{\mathrm{NS}}
$$

與：

$$
O_{\mathrm{SQG}}
$$

候選相似。

---

# 225. Transfer edge

$$
O_{\mathrm{NS}}
\xleftrightarrow{}
O_{\mathrm{SQG}}.
$$

---

# 226. 但需要 theorem-level audit

---

# 227. Knowledge bridge

成功 transfer 形成：

$$
B_{\mathrm{transfer}}.
$$

---

# 228. Proof Asset Map

PSO 可自然實作：

$$
\text{Proof Asset Map}.
$$

---

# 229. Asset types

- lemma；
- method；
- obstruction；
- counterexample；
- transformation；
- tool。

---

# 230. Tool 也可成 proof asset

---

# 231. Example

一個 normalization script，

如果能降低 formalization error，

具有：

$$
U_{\mathrm{tool}}>0.
$$

---

# 232. Benchmark suite

PSO 不能只在 NS 未解題上測。

---

# 233. Ground-truth tier

第一層：

$$
\text{known solvable}.
$$

---

# 234. Known-false tier

有 counterexample。

---

# 235. Independence tier

已知 relative independence。

---

# 236. Formalization-defect tier

人工注入 mismatch。

---

# 237. Method-no-go tier

已知 barrier。

---

# 238. Long-horizon tier

dependency-rich theorem。

---

# 239. PMW tier

controlled deviation。

---

# 240. NS tier

open-ended observational。

---

# 241. Benchmark 順序

先：

$$
\text{known truth}.
$$

後：

$$
\text{unknown frontier}.
$$

---

# 242. 否則無法校準 observatory

---

# 243. Core benchmark metrics

- overclaim rate；
- underclaim rate；
- merge precision；
- obstruction precision；
- basin stability；
- routing efficiency；
- descendant survival accuracy。

---

# 244. Overclaim rate

沿用：

$$
O_R.
$$

---

# 245. False-saturation rate

$$
F_S
=
\frac{
N_{\mathrm{false\ saturation}}
}{
N_{\mathrm{tests}}
}.
$$

---

# 246. False-confluence rate

$$
F_C.
$$

---

# 247. Salvage precision

parent revision 後：

$$
P_{\mathrm{salv}}.
$$

---

# 248. Routing regret

相對 oracle policy：

$$
\mathcal R_g.
$$

---

# 249. Cost efficiency

$$
E_C
=
\frac{
\text{surviving knowledge}
}{
\text{compute cost}
}.
$$

---

# 250. NS-203 migration：第一階段

來源：

$$
203
$$

paper-like artifacts。

---

# 251. 不直接全自動 theorem extraction

先建立 inventory。

---

# 252. Inventory fields

```yaml
artifact_id:
series:
round:
title:
date:
source_hash:
parent_artifact:
```

---

# 253. 第二階段：Section extraction

抽：

- definitions；
- claims；
- propositions；
- lemmas；
- obstructions；
- status statements。

---

# 254. 第三階段：Assumption normalization

建立：

$$
A_i.
$$

---

# 255. 第四階段：Route family

例如：

- RFP；
- CSP；
- DRC；
- MORP；
- DCRP；
- X72。

---

# 256. 第五階段：Obstruction canonicalization

建立：

$$
O_{\mathrm{NS},j}.
$$

---

# 257. 第六階段：Gold audit set

人工抽：

$$
200
$$

對候選 equivalence。

---

# 258. 第七階段：Basin detector calibration

---

# 259. 第八階段：Higher-order sampling

對：

$$
T_1,T_2,T_3,T_X
$$

重新判。

---

# 260. 第九階段：Transfer audit

找：

- other PDE；
- gSQG；
- Boussinesq；
- abstract lemma。

---

# 261. 第十階段：Router simulation

用歷史 corpus：

$$
H_t
$$

重播。

---

# 262. 問：

> 如果當時有 saturation detector，會不會更早切路？

---

# 263. Counterfactual replay

只能說：

$$
\text{policy simulation}.
$$

不代表真歷史。

---

# 264. NS-203 v2 的目標

不是：

> 證明 NS。

---

# 265. 而是：

$$
\boxed{
\text{建立第一個 theorem-level AI long-horizon proof-space dataset}.
}
$$

---

# 266. 如果過程中真的找到 proof

當然進：

$$
\text{certificate path}.
$$

---

# 267. 但 observatory 成功不依賴最終 proof

---

# 268. 這是重要設計

否則研究 infrastructure 的價值綁在未解題結果。

---

# 269. Dashboard NS overview

顯示：

$$
203
$$

artifacts。

---

# 270. Series map

RFP、CSP、DCRP 等。

---

# 271. Route traffic

---

# 272. Obstruction heatmap

---

# 273. Sampling-order timeline

---

# 274. Novelty timeline

---

# 275. Saturation confidence

---

# 276. Transfer map

---

# 277. Claim ledger

---

# 278. Non-conclusion banner

永遠顯示：

```text
OBSERVATIONAL RESEARCH MAP
NOT A PROOF OF UNSOLVABILITY
```

---

# 279. Civilization-scale extrapolation

未來不只 NS。

---

# 280. 每個重大數學問題都有：

$$
\text{PSO workspace}.
$$

---

# 281. 例如：

- RH；
- BSD；
- Hodge；
- Collatz；
- P/NP。

---

# 282. 但 open-problem workspaces 要嚴格標：

$$
\text{UNRESOLVED}.
$$

---

# 283. Known-problem workspaces 用於 calibration

---

# 284. Cross-problem knowledge graph

$$
G_{\mathrm{math}}.
$$

---

# 285. TheoremGraph 類系統已顯示 statement-level graph 可大規模建立

---

# 286. PSO 再加入：

- failed routes；
- lineage；
- research status；
- costs；
- experiment branches。

---

# 287. 從 theorem graph 到 research graph

$$
\boxed{
\text{Theorem Graph}
\subset
\text{Research Graph}.
}
$$

---

# 288. Research Graph 還有 unresolved object

這是最大差別。

---

# 289. 未解狀態也要可表示

例如：

$$
\text{OPEN_OBSTRUCTION}.
$$

---

# 290. Graph 不只記成功史

---

# 291. 這會改變 AI training data

目前 theorem prover data 偏成功 proof。

---

# 292. APRIL 類 failure dataset 已開始修正

---

# 293. PSO 可以產生更高階 data

不是只：

$$
\text{failure}\rightarrow\text{repair}.
$$

---

# 294. 還有：

$$
\text{failure family}
\rightarrow
\text{obstruction class}
\rightarrow
\text{route switch}.
$$

---

# 295. Training object

可以訓練：

$$
\text{research policy model}.
$$

---

# 296. Policy target

不是 next tactic。

而是：

$$
\text{next research move}.
$$

---

# 297. 例如：

> 不要再證這條，換 premise retrieval。

---

# 298. 這就是 AI co-mathematician 的一個真正差異

---

# 299. Co-mathematician 需要 research memory

否則每輪都：

$$
\text{amnesia}.
$$

---

# 300. Research identity 不是人格 identity

系統只需：

$$
\text{persistent state}.
$$

---

# 301. Session continuity

每次 agent 讀：

$$
\text{current workspace state}.
$$

---

# 302. 不需要讀全部歷史全文

---

# 303. Selective context assembly

根據：

- basin；
- obstruction；
- route；
- current claim。

---

# 304. Context compiler

$$
\mathcal C_{\mathrm{ctx}}(s_t).
$$

---

# 305. 輸出：

$$
\text{minimal sufficient context}.
$$

---

# 306. 這能降低 context explosion

---

# 307. Context provenance

每段 context 都知道來源 ID。

---

# 308. AI 不能把摘要當 canonical source

---

# 309. Research query 到 source

一鍵追：

$$
\text{claim}
\rightarrow
\text{source lines}.
$$

---

# 310. Formal proof 到 source

$$
\Pi
\rightarrow
\text{Lean file}.
$$

---

# 311. Obstruction 到 evidence

$$
O
\rightarrow
\{r_1,r_2,\ldots\}.
$$

---

# 312. Basin 到 members

---

# 313. Saturation 到 metric version

---

# 314. 每個數字都可追

這是 observatory 的本質。

---

# 315. Security

AI research memory 可能含：

- unpublished results；
- code；
- credentials；
- private data。

---

# 316. Credential 永不進 PSO graph

---

# 317. Secret store 分離

---

# 318. Access control

object-level ACL。

---

# 319. Public / private / embargoed

---

# 320. Citation provenance

公開輸出只引用：

$$
\text{publicly releasable source}.
$$

---

# 321. Sandbox experiment

故意錯 parent 的 PMW experiment 必須隔離。

---

# 322. 不讓 experimental falsehood 污染 canonical core

---

# 323. Namespace

```text
CANONICAL/
EXPERIMENTAL/
HISTORICAL/
REFUTED/
```

---

# 324. Governance

PSO 不應只有「admin 可以改一切」。

---

# 325. 高風險操作

- delete certificate；
- change canonical theorem；
- merge obstruction；
- mark PROVEN；
- reframe problem。

---

# 326. 需要 audit log

---

# 327. 甚至雙重核准

對：

$$
\text{PROVEN}
$$

可要求：

$$
\text{formal verifier + human/independent audit}.
$$

---

# 328. Automation 可以更快

但 governance 必須更嚴格。

---

# 329. Reproducible release

每個 research milestone：

$$
R_v.
$$

---

# 330. Release contents

- canonical sources；
- graph export；
- metrics；
- validation；
- checksums；
- methodology；
- known limitations。

---

# 331. Graph export

可用：

- GraphML；
- JSONL；
- Parquet。

---

# 332. Metric export

CSV / Parquet。

---

# 333. Human-readable report

Markdown。

---

# 334. Machine-readable status

JSON。

---

# 335. Release fingerprint

$$
h_{\mathrm{release}}.
$$

---

# 336. Rebuild script

一鍵：

$$
\text{source}
\rightarrow
\text{graph}
\rightarrow
\text{metrics}.
$$

---

# 337. 如果不能 rebuild

觀測站不可靠。

---

# 338. PSO 的最小 MVP

不需要一開始 civilization scale。

---

# 339. MVP 只做六件事

1. artifact ingest；
2. claim/assumption extraction；
3. route/obstruction graph；
4. status typing；
5. metric calculation；
6. interactive dashboard。

---

# 340. MVP storage

甚至：

- SQLite；
- files；
- NetworkX；

就可以開始。

---

# 341. 不要一開始過度工程

---

# 342. Phase 1：NS-203 offline observatory

---

# 343. Phase 2：Incremental ingest

新 paper 加入即更新。

---

# 344. Phase 3：Formal backend

接 Lean / AXLE / local Lean。

---

# 345. Phase 4：Multi-agent router

---

# 346. Phase 5：Cross-project federation

---

# 347. Phase 6：Civilization-scale graph

---

# 348. Phase 1 success criteria

至少：

$$
\text{claim extraction precision}>0.8
$$

在 gold sample。

---

# 349. Obstruction merge precision

優先：

$$
>0.9
$$

因 false merge 很危險。

---

# 350. Route graph audit

人工抽查。

---

# 351. Status overclaim rate

$$
O_R\approx0.
$$

---

# 352. Rebuild reproducibility

$$
100\%.
$$

---

# 353. Phase 2 success

新 artifact：

$$
<1
$$

次全圖重算。

---

# 354. Incremental update

---

# 355. Phase 3 success

formal claims：

$$
\text{verifier status}
$$

可回寫 PSO。

---

# 356. Phase 4 success

router 比 random / static baseline：

$$
\text{audited yield}\uparrow.
$$

---

# 357. Phase 5 success

cross-project transfer：

$$
T_D>0.
$$

---

# 358. Phase 6 不應先承諾

civilization scale 是長期方向。

---

# 359. PSO 與一般知識圖譜的差別

一般 KG：

$$
\text{entity relation}.
$$

---

# 360. PSO 另外存：

$$
\boxed{
\text{epistemic status}
+
\text{research dynamics}
+
\text{failed routes}
+
\text{certificate}.
}
$$

---

# 361. PSO 與普通 RAG 的差別

RAG 問：

> 找相關文件。

---

# 362. PSO 問：

> 找與當前 obstruction 結構上相關、但 genealogy 獨立的 route。

---

# 363. PSO 與 theorem prover 的差別

prover 目標：

$$
\text{close goal}.
$$

---

# 364. PSO 目標：

$$
\text{understand and manage the evolving research space}.
$$

---

# 365. PSO 與 project manager 的差別

不是只管理任務進度。

---

# 366. 它管理：

$$
\text{mathematical epistemic structure}.
$$

---

# 367. PSO 與論文資料庫的差別

不是只有：

$$
\text{paper metadata}.
$$

---

# 368. 它有：

$$
\text{claim-level lineage}.
$$

---

# 369. Civilization-scale 版本

如果未來 AI 持續讀取：

$$
10^7
$$

篇數學文件，

TheoremGraph 類 statement graph 會成為底層之一。

---

# 370. PSO 可疊：

$$
\text{research dynamics layer}.
$$

---

# 371. 文明知識的問題將改變

從：

> 我們知道哪些 theorem？

---

# 372. 變成：

> 哪些 theorem 相互依賴？

---

# 373. 再變：

> 哪些路曾被嘗試？

---

# 374. 再變：

> 哪些失敗反覆出現？

---

# 375. 再變：

> 哪些問題已局部飽和？

---

# 376. 再變：

> 哪些 representation 尚未被探索？

---

# 377. 這就是 proof-space science

---

# 378. Proof-space science 的研究對象

不是 theorem 本身。

---

# 379. 而是：

$$
\boxed{
\text{the dynamics of theorem-seeking systems}.
}
$$

---

# 380. 這是一個 meta-science

---

# 381. 但它不取代數學

數學仍由：

$$
\text{proof / counterexample / formal result}
$$

決定。

---

# 382. PSO 只是讓我們更聰明地找

---

# 383. 系列最重要的統一圖

$$
\boxed{
\begin{aligned}
\text{Artifact}
&\rightarrow
\text{Canonical Object}\\
&\rightarrow
\text{Semantic Quotient}\\
&\rightarrow
\text{Proof-Space Graph}\\
&\rightarrow
\text{Higher-Order Sampling}\\
&\rightarrow
\text{Basin / Obstruction}\\
&\rightarrow
\text{Saturation Measurement}\\
&\rightarrow
\text{Diagnosis}\\
&\rightarrow
\text{Research Routing}\\
&\rightarrow
\text{Certificate / Revision}\\
&\rightarrow
\text{Descendant Salvage}.
\end{aligned}
}
$$

---

# 384. 這不是線性 pipeline

任何 stage 都可回饋。

---

# 385. Feedback

例如：

$$
\text{certificate}
\rightarrow
\text{graph rewrite}.
$$

---

# 386. Revision

$$
\rightarrow
\text{descendant re-audit}.
$$

---

# 387. New obstruction

$$
\rightarrow
\text{new branch}.
$$

---

# 388. Dynamic fixed point

成熟 workspace 可能逐漸接近：

$$
\mathcal S^\star.
$$

---

# 389. 但不是停止

新資料仍可：

$$
\mathcal S^\star
\rightarrow
\mathcal S^{\star'}.
$$

---

# 390. Research memory fixed point

指：

$$
\text{stable core + open frontier}.
$$

---

# 391. 這與第 7 篇 truth–generativity tension 接軌

核心可以壓縮，

frontier 仍然開放。

---

# 392. Stable core

$$
\mathcal C^\star.
$$

---

# 393. Open frontier

$$
\mathfrak F.
$$

---

# 394. Mature PSO state

$$
\boxed{
\mathcal S
=
(
\mathcal C^\star,
\mathfrak F,
\mathcal O,
\mathcal H
).
}
$$

其中：

- core；
- frontier；
- obstructions；
- history。

---

# 395. 這比「已知／未知」二分更強

---

# 396. Core 也有版本

---

# 397. Frontier 也有 priority

---

# 398. Obstruction 也有 status

---

# 399. History 也可壓縮但不可抹除

---

# 400. AI 的長程自主研究需求

要真正 autonomous，

至少需要：

1. memory；
2. verification；
3. routing；
4. status discipline；
5. rollback。

---

# 401. 沒 memory

重複。

---

# 402. 沒 verification

幻覺。

---

# 403. 沒 routing

算力浪費。

---

# 404. 沒 status discipline

過度結論。

---

# 405. 沒 rollback

錯誤污染。

---

# 406. PSO 正好對應五個缺口

---

# 407. 非主張總表

本文不主張：

1. Proof-Space Observatory 能自動解決未解數學問題；
2. PSO 可以取代 theorem prover；
3. PSO 可以取代人類數學審查；
4. graph centrality 等於數學重要性；
5. embedding similarity 等於 theorem equivalence；
6. basin decomposition 是證明空間唯一真幾何；
7. saturation metric 是 truth probability；
8. obstruction confluence 等於 unprovability；
9. descendant survival 等於 parent correctness；
10. productive-mis-specification window 普遍存在；
11. formal proof 自動保證 informal statement fidelity；
12. AI-generated claim extraction 可以無審核地進 canonical core；
13. different models 自動提供獨立證據；
14. TheoremGraph、LeanMarathon、AXLE、BlueprintRepair 或 LeanSearch v2 已經等同 PSO；
15. 203 份 NS artifacts 已足以描述全部 Navier--Stokes proof space；
16. NS-203 的 higher-order sampling 證明 Clay formulation 有錯；
17. P/NP 或任何 open problem 可由 PSO saturation 判定不可解；
18. civilization-scale observatory 在目前已工程完成；
19. event sourcing 可解決所有 research-memory 問題；
20. graph database 是唯一合適儲存技術；
21. vector database 可以作 canonical truth store；
22. AI routing policy 可以無治理地修改 canonical theorem；
23. historical refuted theory 應留在 active truth space；
24. negative result 一定有 transfer value；
25. 本文提供的所有公式已是唯一最佳 metric；
26. PSO 應把所有私人／未公開研究公開；
27. 公開 consensus 決定 claim truth；
28. 大規模生成本身代表 scientific progress；
29. 長程研究記憶越大越好而不需 compaction；
30. 本文已建立文明級數學認知的最終架構。

---

# 408. 形式命題一：Paper Non-Primitivity

$$
\boxed{
\text{Paper}
\neq
\text{minimal research unit}.
}
$$

---

# 409. 形式命題二：Canonical-State Principle

$$
\boxed{
\text{rendered view}
\not\equiv
\text{canonical source}.
}
$$

---

# 410. 形式命題三：Typed-Relation Principle

$$
\boxed{
\text{all research edges cannot be reduced to similarity}.
}
$$

---

# 411. 形式命題四：Status-Type Principle

$$
\boxed{
\text{Observation}
\not\rightarrow
\text{Verdict}
}
$$

without certificate。

---

# 412. 形式命題五：Revision-Preservation Principle

$$
\boxed{
P\rightarrow P'
\Rightarrow
\operatorname{Reaudit}(\mathcal D(P)),
}
$$

而不是全刪或全留。

---

# 413. 形式命題六：Graph-Rebuild Principle

若 canonical artifacts 與 event log 完整，

derived graph 應可重建。

---

# 414. 形式命題七：Metric-Version Principle

$$
\boxed{
M
=
M(\text{definition version}).
}
$$

---

# 415. 形式命題八：Routing Non-Verdict

$$
\boxed{
\Pi_{\mathrm{meta}}(S)=\text{reframe}
\not\Rightarrow
\text{original problem wrong}.
}
$$

---

# 416. 形式命題九：Observatory Non-Oracle

$$
\boxed{
\text{PSO}
\neq
\text{truth oracle}.
}
$$

---

# 417. 形式命題十：Research-Memory Expansion

成熟研究記憶至少需要：

$$
\boxed{
\text{proof}
+
\text{failure}
+
\text{revision}
+
\text{provenance}.
}
$$

---

# 418. 與 LSI-PSD-01 的整合

第 1 篇：

$$
\text{search regime}.
$$

PSO 將它實作成：

```yaml
regime_id:
axioms:
language:
methods:
verifier:
budget:
history:
policy:
```

---

# 419. 與第 2 篇的整合

coverage：

$$
I_k
$$

成 dashboard metric。

---

# 420. 與第 3 篇的整合

semantic quotient 成 merge pipeline。

---

# 421. 與第 4 篇的整合

sampling order 成：

```text
order=0/1/2/3/X
```

---

# 422. 與第 5 篇的整合

basin 變成版本化 graph object。

---

# 423. 與第 6 篇的整合

obstruction atlas 變核心資料層。

---

# 424. 與第 7 篇的整合

truth / generativity 分欄存。

---

# 425. 與第 8 篇的整合

parent revision + descendant salvage。

---

# 426. 與第 9 篇的整合

experiment branch support。

---

# 427. 與第 10 篇的整合

epistemic type checker。

---

# 428. 與第 11 篇的整合

historical lineage / status-aware retrieval。

---

# 429. 所以第 12 篇不是再加新概念

而是：

$$
\boxed{
\text{compile the series into a system}.
}
$$

---

# 430. 第一個正式 PSO MVP 專案結構

```text
pso/
├─ artifacts/
├─ canonical/
├─ events/
├─ graph/
├─ metrics/
├─ audits/
├─ experiments/
├─ dashboards/
├─ exports/
└─ tools/
```

---

# 431. `artifacts/`

原始輸入。

---

# 432. `canonical/`

validated sources。

---

# 433. `events/`

append-only JSONL。

---

# 434. `graph/`

derived nodes / edges。

---

# 435. `metrics/`

版本化計算結果。

---

# 436. `audits/`

human / model review。

---

# 437. `experiments/`

branch configs。

---

# 438. `dashboards/`

visualizations。

---

# 439. `exports/`

release packages。

---

# 440. `tools/`

rebuild / validate。

---

# 441. Minimum event schema

```yaml
event_id:
timestamp:
actor:
action:
object_id:
object_version:
payload:
parent_event:
signature:
```

---

# 442. Minimum claim schema

```yaml
claim_id:
problem_id:
text:
formal_statement:
scope:
status:
source_refs:
assumptions:
dependencies:
certificate_ids:
version:
```

---

# 443. Minimum edge schema

```yaml
edge_id:
source:
target:
type:
confidence:
audit:
provenance:
```

---

# 444. Minimum metric schema

```yaml
metric_id:
name:
definition_version:
scope:
value:
uncertainty:
inputs:
computed_at:
```

---

# 445. Minimum audit schema

```yaml
audit_id:
target:
auditor:
method:
result:
confidence:
notes:
source_refs:
```

---

# 446. PSO 的一句工程判斷

如果一個數字無法回答：

> 從哪些 source、哪個 metric version、哪些 edge 算出來？

那它不應進正式 dashboard。

---

# 447. Auditability over aesthetics

漂亮圖：

$$
\neq
$$

可靠 observatory。

---

# 448. Interactive graph 只是 UI

canonical graph export 才是 source。

---

# 449. Version-controlled dashboard

圖表也標：

$$
\text{data version}.
$$

---

# 450. Release validation

每次：

1. validate source；
2. validate graph schema；
3. validate checksums；
4. recompute key metrics；
5. archive report。

---

# 451. Regression tests

例如：

- node count；
- edge count；
- known gold pairs；
- known status transitions。

---

# 452. Metric regression

新版 metric 不應 silent replace old。

---

# 453. 兩版並存

$$
\rho^{(v1)},
\rho^{(v2)}.
$$

---

# 454. PSO 自身也要可科學研究

這是 meta-observatory。

---

# 455. 我們可以問：

> 哪個 basin detector 比較準？

---

# 456. 哪個 router 更有效？

---

# 457. 哪個 model 更容易 overclaim？

---

# 458. 哪個 verifier / retriever 造成 bias？

---

# 459. Observatory becomes benchmark platform

---

# 460. Civilization-scale AI mathematics 的可能終局

未來每一個新 theorem 不只是 PDF。

---

# 461. 它帶：

- machine-checkable statement；
- dependencies；
- provenance；
- research history；
- failed routes；
- certificates。

---

# 462. Paper 變成 view

canonical knowledge 變成 graph + source。

---

# 463. 但人類 prose 不會消失

prose 仍是：

$$
\text{interpretation interface}.
$$

---

# 464. Machine graph 也不會取代 prose

兩者互補。

---

# 465. Formal / informal duality

$$
\boxed{
\text{formal rigor}
+
\text{informal meaning}.
}
$$

---

# 466. TheoremGraph 已展示橋接可能性

PSO 把橋再延伸到：

$$
\text{research process}.
$$

---

# 467. 最終 architecture

$$
\boxed{
\text{Source}
\leftrightarrow
\text{Formal}
\leftrightarrow
\text{Graph}
\leftrightarrow
\text{Memory}
\leftrightarrow
\text{Agent}.
}
$$

---

# 468. 人類的位置

不是被移除。

---

# 469. 人類成為：

- question setter；
- auditor；
- value setter；
- framing reviewer；
- release authority。

---

# 470. AI 的位置

成為：

- explorer；
- compiler；
- verifier user；
- graph maintainer；
- hypothesis generator。

---

# 471. Proof assistant 的位置

成為：

$$
\text{formal certificate engine}.
$$

---

# 472. Observatory 的位置

成為：

$$
\text{research memory and routing layer}.
$$

---

# 473. 這四個角色不應混成一個模型

---

# 474. 最終系統不是「超級聊天機器人」

而是：

$$
\boxed{
\text{a governed research operating system}.
}
$$

---

# 475. 對文明級研究的最低要求

如果 AI 未來要自主研究數十年，

它必須知道：

> 我以前做過什麼。

---

# 476. 更重要：

> 我以前為什麼放棄。

---

# 477. 更重要：

> 哪些放棄後來證明是錯的。

---

# 478. 更重要：

> 哪些失敗其實是通用 obstruction。

---

# 479. 更重要：

> 哪些「已知」其實只是舊版本 hypothesis。

---

# 480. 這就是研究文明的記憶

---

# 481. 系列最終閉環

$$
\boxed{
\begin{aligned}
\text{Generate}
&\rightarrow
\text{Record}\\
&\rightarrow
\text{Verify}\\
&\rightarrow
\text{Quotient}\\
&\rightarrow
\text{Map}\\
&\rightarrow
\text{Measure}\\
&\rightarrow
\text{Diagnose}\\
&\rightarrow
\text{Route}\\
&\rightarrow
\text{Revise}\\
&\rightarrow
\text{Salvage}\\
&\rightarrow
\text{Generate}.
\end{aligned}
}
$$

---

# 482. 這是一個動態研究循環

而不是：

$$
\text{prompt}
\rightarrow
\text{answer}.
$$

---

# 483. PSO 的第一個實驗性定義

本文正式提出：

$$
\boxed{
\textbf{An AI Proof-Space Observatory is a versioned, provenance-preserving, epistemically typed system that converts long-horizon mathematical research traces into auditable research objects, graphs, measurements, and routing decisions without treating search statistics as mathematical verdicts.}
}
$$

---

# 484. 中文定義

**AI 證明空間觀測站**是一個：

> 將長程數學研究軌跡轉換成可版本化、可追溯、具認識論型別的研究物件、圖結構、量測值與研究路由，並明確禁止把搜尋統計直接當成數學判決的研究記憶系統。

---

# 485. PSO 的最低成功標準

不是證出 NS。

---

# 486. 而是：

> 兩年後，任何 agent 都能準確知道過去兩年哪些路試過、哪些是真的重複、哪些失敗已被證明、哪些只是猜測、哪些假設後來被撤銷。

---

# 487. 如果能做到

就已經比單純論文堆積前進了一個研究文明層級。

---

# 488. 結論

LSI-PSD 系列最初從一個非常簡單的觀察開始：

> 如果 AI 在同一個難題上持續生成上百、上千、上萬輪研究，最後先被耗盡的也許不是「數學真理」，而是某些符號、方法、路徑與障礙的可區分研究空間。

從這個起點，系列逐步建立：

$$
\text{proof-space coverage},
$$

$$
\text{semantic quotient},
$$

$$
\text{higher-order resampling},
$$

$$
\text{local saturation},
$$

$$
\text{obstruction confluence},
$$

$$
\text{truth--generativity inversion},
$$

$$
\text{productive mis-specification},
$$

$$
\text{non-conclusion firewall}.
$$

但如果這些概念只停在論文裡，它們仍然只是方法論描述。

第十二篇的任務，就是把它們變成一個研究系統。

這個系統的核心不是更大的模型。

而是：

$$
\boxed{
\text{better memory}
+
\text{better structure}
+
\text{better verification}
+
\text{better epistemic discipline}.
}
$$

它要保存：

$$
\text{what was proved},
$$

也保存：

$$
\text{what was tried}.
$$

保存：

$$
\text{what failed},
$$

也保存：

$$
\text{why it failed}.
$$

保存：

$$
\text{what was believed},
$$

也保存：

$$
\text{when that belief was downgraded}.
$$

保存：

$$
\text{which parent theory was revised},
$$

也保存：

$$
\text{which descendants survived}.
$$

這會讓 AI 數學研究第一次不只是高速生成。

而是形成：

$$
\boxed{
\text{persistent research memory}.
}
$$

當這種記憶與 formal verification、graph retrieval、multi-agent branching、controlled experiments 與 human audit 結合，數學研究的單位可能從「單篇 paper」轉變成：

$$
\boxed{
\text{versioned research relation}.
}
$$

一個 theorem 不再只是一個 final statement。

它會帶著：

- assumptions；
- dependencies；
- proof；
- failed alternatives；
- historical revisions；
- transfer links。

而一個未解問題也不再只是一個空白格。

它可以有：

$$
\text{known basins},
$$

$$
\text{known obstructions},
$$

$$
\text{known no-go families},
$$

$$
\text{open frontiers}.
$$

因此本文提出整個系列最後兩個命題。

第一：

$$
\boxed{
\textbf{The future unit of mathematical research memory should not be the paper, but the versioned, typed, provenance-preserving research relation.}
}
$$

第二：

$$
\boxed{
\textbf{A civilization-scale AI research system should remember not only what humanity knows, but how knowledge was reached, where inquiry failed, and which alternatives remain genuinely open.}
}
$$

而其中最重要的限制仍然沒有改變：

$$
\boxed{
\textbf{The observatory observes research. It does not replace mathematics.}
}
$$

這句話也完成 LSI-PSD 主系列的封頂。

---

# 參考文獻

1. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., & Liu, F. (2026). **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** arXiv:2606.05400.

2. Kurgan, S., Wang, E., Leonen, E., Szeto, S., Alexander, L., Remizov, A., Alper, J., Inchiostro, G., & Ilin, V. (2026). **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363.

3. Xin, J., Schneidman, A., Cummins, C., Ram, K., Ganesh, S., & Limperg, J. (2026). **AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities.** arXiv:2606.26442.

4. Khrulev, R. (2026). **BlueprintRepair: Typed Local Edits for Failed Lean Proof Blueprints.** arXiv:2607.28110.

5. Gao, G. et al. (2026). **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137.

6. Pham, Q. V., Karimov, E., Galichin, A., & Oseledets, I. (2026). **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics.** arXiv:2606.09450.

7. Wang, E., Chess, S., Lee, D., Ge, S., Mallavarapu, A., & Ilin, V. (2026). **Learning to Repair Lean Proofs from Compiler Feedback.** arXiv:2602.02990.

8. Yin, D., & Gao, J. (2025). **Generating Millions Of Lean Theorems With Proofs By Exploring State Transition Graphs.** arXiv:2503.04772.

9. George, R. J., Huang, S., Song, P., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925.

10. Xin, R. et al. (2025). **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving.** arXiv:2502.03438.

11. Qiu, R. et al. (2026). **Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving.** arXiv:2603.24465.

12. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468.

13. Chen, T., & Li, Z. (2026). **A Theoretical Framework for Self-Play Theorem Proving Algorithms.** arXiv:2606.01861.

14. Wang, A. et al. (2025). **Don't Get Lost in the Trees: Streamlining LLM Reasoning by Overcoming Tree Search Exploration Pitfalls.** arXiv:2502.11183.

15. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493.

16. Zhang, K. et al. (2026). **Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization.** arXiv:2606.31002.

17. Kim, J., Han, H., & Hwang, S.-w. (2026). **Benchmarking Testing in Automated Theorem Proving.** arXiv:2604.23698.

18. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Reproducible internal corpus analysis, 2026-08-17.

---

## 附錄 A：PSO 核心實體總表

| Entity | 作用 |
|---|---|
| Problem | 研究目標 |
| Claim | 可判定主張 |
| Assumption | 前提 |
| Lemma | 可重用局部結果 |
| ProofState | formal proof state |
| Route | 研究／證明路線 |
| Obstruction | canonical failure structure |
| Basin | 局部 proof-space region |
| Certificate | verdict-specific evidence |
| Revision | parent/version change |
| Experiment | controlled branch |
| Artifact | canonical file/source |

---

## 附錄 B：PSO edge types

```text
DEPENDS_ON
IMPLIES
CONTRADICTS
EQUIVALENT_CANDIDATE
EQUIVALENT_CERTIFIED
DERIVES
REVISITS
CONVERGES_TO
RESOLVES
REVIVES
TRANSFERS_TO
REVISES
DESCENDS_FROM
CERTIFIES
REFUTES
FORMALIZES
INTERPRETS
ESCAPES_TO
```

---

## 附錄 C：PSO MVP 設定

```yaml
storage:
  artifacts: filesystem
  metadata: sqlite
  graph: networkx
  events: jsonl
  metrics: parquet

verification:
  lean:
    enabled: optional
  source_validation:
    utf8: true
    canonical_math_delimiters: true

ingest:
  markdown: true
  zip_recursive: true
  lean: true

objects:
  - problem
  - claim
  - assumption
  - route
  - obstruction
  - basin
  - certificate
  - revision

metrics:
  - novelty
  - audited_yield
  - confluence
  - saturation
  - descendant_survival

governance:
  target_rewrite_requires_audit: true
  status_upgrade_requires_certificate: true
  canonical_source_immutable: true
```

---

## 附錄 D：NS-203 migration checklist

- [ ] 建立 203 artifacts canonical inventory
- [ ] 每篇建立 source hash
- [ ] 抽取 section / claim / assumption
- [ ] 抽取 explicit dependency
- [ ] 建 route family
- [ ] 建 obstruction candidate
- [ ] 建 200-pair gold audit set
- [ ] 校準 semantic quotient
- [ ] 校準 obstruction merge
- [ ] 校準 basin detector
- [ ] 重算 $T_1,T_2,T_3,T_X$
- [ ] 建 higher-order sampling timeline
- [ ] 建 cross-series confluence graph
- [ ] 建 transfer candidate graph
- [ ] 建 status ledger
- [ ] 建 release package與 checksums

---

## 附錄 E：Epistemic firewall

```text
SEARCH STATISTIC
      |
      v
OBSERVATION
      |
      v
DIAGNOSTIC HYPOTHESIS
      |
      +---- no certificate ----> remain hypothesis
      |
      +---- proof -------------> PROVEN
      |
      +---- counterexample ----> REFUTED
      |
      +---- no-go theorem -----> FORMAL_NO_GO
      |
      +---- independence ------> INDEPENDENT_RELATIVE_TO_T
```

---

## 附錄 F：一句話版本

$$
\boxed{
\text{真正的 AI 數學記憶，不應只記得答案；它必須記得整個研究空間是怎麼被走過的。}
}
$$

而真正的 AI 證明空間觀測站，也不是替數學下判決：

$$
\boxed{
\text{它只負責讓每一次探索、失敗、修正與證明，都不再白白消失。}
}
$$


<!-- END LSI-PSD-12 -->

---
