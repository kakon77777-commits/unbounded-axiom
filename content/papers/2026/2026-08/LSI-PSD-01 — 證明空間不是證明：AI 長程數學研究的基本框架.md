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
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文屬數學研究方法論、證明工程、AI 數學研究與科學哲學的理論建模。本文提出的「證明空間」「搜尋制度」「負證明資訊」「局部飽和」等術語，除非明確標記為既有文獻術語，均是本文的操作性研究定義。本文不聲稱已證明、反證或判定 Navier--Stokes existence and smoothness、P vs NP 或其他公開未解問題；亦不把任何 AI 未能找到證明的現象視為原命題錯誤、不可證、不可判定或定義錯置的證明。

---

## 摘要

大型語言模型、形式證明器、程式執行工具、文獻檢索、長程記憶與多智能體協作正在共同改變自動數學研究的基本單位。傳統自動定理證明通常把任務表述為：給定形式命題 $Q$，尋找一個能被驗證器接受的證明物件 $\pi$。然而，當 AI 系統能在數十、數百乃至更多研究輪次中持續提出中間引理、切換表示、建立反例候選、搜尋文獻、執行數值或符號實驗、保存失敗、回收舊結果並協調多條路徑時，單一證明物件已不足以描述實際發生的研究過程。新的對象不是只有最終證明，而是整個可重放的研究軌跡。

本文建立「邏輯空間積分與證明空間動力學」系列的第一層基礎。核心工作有五項。第一，嚴格區分形式可證集合、搜尋制度可達空間、實際被觀測的研究軌跡、已驗證事實圖與未驗證研究記憶，避免把「AI 看過的空間」誤認為「數學上一切可能證明的空間」。第二，定義搜尋制度

$$
R=(\mathcal A,\mathcal L,\mathcal M,\mathcal V,B,\mathcal K,\Sigma),
$$

其中包含公理背景、表示語言、方法族、驗證器、資源界、既有知識與調度策略。第三，提出「證明空間非同一原則」與「搜尋制度非結論原則」：即使某一制度中出現長期失敗、強烈路徑匯流或局部飽和，也不能僅由此推出 $Q$ 為假、原問題定義錯誤、 $Q$ 不可證或 $Q$ 相對某形式系統獨立。第四，提出「負證明資訊」的分級框架，說明失敗並非只有零與一兩種狀態；可重現、可審計、跨表示穩定的障礙能成為關於搜尋制度的正面研究資料。第五，將近年的 AI 數學研究進展納入此框架：AlphaProof 顯示形式環境可提供可驗證的強回饋；HERMES、Minimal Agent、LEAP 與 Stepwise 展示迭代修正與 proof-state 搜尋；LeanMarathon 顯示長程形式化的主要瓶頸包括漂移、依賴糾纏與上下文衰退；RMA 將研究級問題分解為文獻、知識庫、證明與驗證模組；Danus 以 fact graph 區分已驗證事實與未驗證記憶；TheoremGraph 則證明細粒度數學依賴圖已可被大規模抽取。另一方面，2026 年關於形式證明對語義保持改寫高度敏感的研究顯示：同一數學內容可因表示不同而有極不相同的證明成功率，因此任何「搜尋耗盡」主張都必須先面對表示商空間問題。

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

固定形式系統 $\mathcal A$ 、目標 $Q$ 與證明語法後，可以定義所有可被系統接受的證明物件集合：

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

但在實際 AI 搜尋中，系統通常不會直接列舉 $\Pi_{\mathcal A}(Q)$ ；它只會沿著某些可生成的 proof state、tactic、自然語言策略或程式操作前進。

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

這個定義刻意把「基礎模型能力」降為制度的一個因素，而不是全部。相同模型在不同 $\Sigma$ 、 $\mathcal K$ 、 $\mathcal V$ 與 $B$ 下，可以產生完全不同的可達空間。

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

這條原則並不禁止我們測量 $\widehat\Omega_{R,N}$ ；相反，它要求所有測量都帶著制度標籤。

例如：

$$
\operatorname{Sat}(Q;R,N)
$$

只能表示「在制度 $R$ 、執行規模 $N$ 下出現某種飽和訊號」，而不能縮寫成：

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

若對語義保持改寫、不同形式化或不同工具制度， $O$ 仍反覆出現，則它比單一路徑 no-go 更有研究價值。

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
- LSI-PSD-03 將處理 $\Omega/\sim$ ；
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
