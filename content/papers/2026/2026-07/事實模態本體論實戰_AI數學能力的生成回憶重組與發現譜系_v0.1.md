# 事實模態本體論實戰

## AI 數學能力的生成、回憶、重組與發現譜系  
### 從合成數據工廠、蒸餾、自我修正到數學暗資料與分散式發現本體

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者：** Neo.K  
**方法：** 事實模態本體論（Fact Modal Ontology, FMO）／正—反—邊本體論反事實推理  
**日期：** 2026-07-18  
**文件類型：** 綜合實戰研究論文／方法應用案例  
**狀態：** 開放迭代，不作最終定論  

---

# 摘要

現代 AI 為何突然能更好地處理高難度數學問題？

最常見的回答是：模型變大、推理時間變長、強化學習更成熟、數據更多。但這些回答仍然過於平面。它們沒有處理一個更深的事實模態問題：

> 當一個 AI 在某次推理中交出一份新證明時，這個證明究竟是在當下生成、從訓練中回憶、由先前內部探索片段重組，還是由整個人機—模型—驗證器系統跨時間共同形成？

本研究使用事實模態本體論，將問題拆成四個核心集合：

$$
\mathcal F^{+}
$$

已被公開證據支持的正事實；

$$
\mathcal F^{-}
$$

被證據排除、尚未成立或不可直接推論的反事實；

$$
\mathcal F^{\partial}
$$

位於概念與證據邊界、不能簡單二分的邊界事實；

以及：

$$
\mathcal W_{\mathrm{cf}}
$$

用於檢驗因果結構的反事實世界集合。

本研究得到的主要結論是：

$$
\boxed{
\text{現代 AI 的數學能力不是單一模型在單一時刻的孤立智能，}
\newline
\text{而是一個跨訓練、跨資料、跨搜尋、跨驗證、跨版本、跨人機審查的分散式時間認知系統。}
}
$$

在此系統中，合成數據不只是訓練燃料。它同時可能是：

- 任務空間生成器；
- 證明策略搜尋空間；
- 錯誤類型映射器；
- 中間引理儲存層；
- 模型選擇訓練器；
- 未被辨認的研究成果庫。

因此，一個最終被公開的數學成果，至少可能有五個不同的出生時間：

$$
t_{\mathrm{first\ generation}},
\quad
t_{\mathrm{first\ composition}},
\quad
t_{\mathrm{first\ verification}},
\quad
t_{\mathrm{first\ recognition}},
\quad
t_{\mathrm{first\ publication}}.
$$

這五者不必相同。

論文提出「分散式發現本體」、「合成數學暗資料」、「證明譜系」與「首次發現多時間點」等概念，並指出：未來 AI 數學研究的關鍵基礎設施，不只應繼續生成更多證明，也應保存、正規化、比對、拼接並考古既有的內部探索結果。

---

# 1. 問題提出

Neo.K 提出的核心問題可以壓縮為：

> 業界目前大量使用合成數據、自問自答、互評、修正、蒸餾與強化學習。那麼，AI 後來解出數學難題時，是否可能不是在公開答案生成當下才首次找到，而是在先前合成數據或內部探索中已經生成過局部甚至完整結構，之後再被模型回憶、重組與顯性化？

這一問題不能用「是」或「否」直接回答。

因為它混合了至少六種不同機制：

1. 逐字記憶既有答案；
2. 記憶已知數學方法；
3. 訓練前或訓練中生成過相似證明；
4. 權重吸收了生成資料的統計與結構；
5. 推理當下重新搜尋與組合；
6. 人類、驗證器與後續模型共同補全。

若不分離這些機制，便會把以下不同命題混為一談：

$$
\text{模型見過答案}
$$

$$
\text{模型見過局部結構}
$$

$$
\text{模型學會了方法}
$$

$$
\text{模型重新發現答案}
$$

$$
\text{模型第一次產生答案}
$$

$$
\text{人類第一次辨認答案}
$$

FMO 的任務，就是避免這種降維。

---

# 2. 方法：正—反—邊本體論反事實推理

## 2.1 正事實

定義：

$$
\mathcal F^{+}
=
\{f_i:\operatorname{Supported}(f_i)\}
$$

其中每個正事實都必須有可追溯來源，並區分：

- 官方技術說明；
- 論文；
- 可驗證程式；
- 專家審查；
- 公司宣稱；
- 本文推論。

---

## 2.2 反事實

本研究中的「反事實」有兩種含義。

第一種是負向事實：

$$
\mathcal F^{-}
$$

即目前沒有證據支持，或不能由現有證據推出的命題。

第二種是反事實世界：

$$
W_{\neg x}
$$

即假設某一機制不存在，再觀察 AI 數學能力是否仍能成立。

---

## 2.3 邊界事實

定義：

$$
\mathcal F^{\partial}
=
\{f:
\neg \operatorname{ClearlyPositive}(f)
\land
\neg \operatorname{ClearlyNegative}(f)
\}
$$

例如：

> 模型是在回憶還是在推理？

這不是良好二分。

因為模型可能同時進行：

$$
\text{結構激活}
+
\text{候選生成}
+
\text{局部搜尋}
+
\text{跨方法組合}
+
\text{錯誤修正}.
$$

---

## 2.4 來源歷史

每個判斷都附帶：

$$
\mathsf{Provenance}
=
\langle
source,
date,
scope,
claim,
confidence,
limitations
\rangle.
$$

本研究不把公司公開敘述視為無條件完整真相，但將其視為對公開可知事實的重要來源。

---

## 2.5 不可識別性

若多個內部過程都能生成相同輸出，而公開資訊不能區分，則記為：

$$
\operatorname{NonIdentifiable}.
$$

例如公開的一份正確證明，可能來自：

- 純推理時搜尋；
- 先前內部 rollout；
- 合成資料訓練後的重建；
- 人工提示後的路徑重試；
- 多版本模型累積。

只看最終文字通常不能確定其來源。

---

# 3. 第一層正事實：業界確實正在建立合成數據工廠

## 3.1 合成數據已從輔助資料變成主體資料

Meta 公開說明，Llama 3.1 的後訓練會反覆進行：

$$
\text{SFT}
\rightarrow
\text{Rejection Sampling}
\rightarrow
\text{DPO},
$$

並使用合成數據產生其絕大多數 SFT 案例，再經多層資料處理與過濾。[1]

NVIDIA 的 Nemotron-4 340B 報告則指出，其對齊階段超過 98% 的資料由合成方式生成，並公開合成資料管線。[2]

Anthropic 的 Constitutional AI 展示了另一種循環：

$$
\text{初始回答}
\rightarrow
\text{自我批判}
\rightarrow
\text{修正版}
\rightarrow
\text{監督微調}
\rightarrow
\text{AI 偏好比較}
\rightarrow
\text{RLAIF}.
$$

也就是模型不只產生答案，也產生對答案的評價與修正資料。[3]

OpenAI 對外提供的模型蒸餾流程，則允許開發者用較強模型的輸出建立資料集，再微調成本較低的模型，並透過 Evals 反覆測試、補充弱項資料與再訓練。[4]

因此，現代後訓練不是單次標註，而更接近：

$$
\boxed{
\text{生成}
\rightarrow
\text{多候選}
\rightarrow
\text{批評}
\rightarrow
\text{拒絕}
\rightarrow
\text{偏好}
\rightarrow
\text{訓練}
\rightarrow
\text{再測試}
}
$$

---

## 3.2 數據設計已從樣本生成提升到分布設計

Google 於 2026 年公開的 Simula 框架，將合成數據視為資料集層級的機制設計，而非逐筆生成。它以推理模型建立概念分類、控制覆蓋、複雜度與品質，並在不同領域生成最高 512K 筆資料；結果顯示，數學推理與法律推理對資料複雜度的需求並不相同。[5]

這表示業界開始承認：

$$
\text{更多資料}
\not\Rightarrow
\text{更好資料}.
$$

真正問題是：

$$
\operatorname{Coverage}
+
\operatorname{Difficulty}
+
\operatorname{Diversity}
+
\operatorname{Verification}
+
\operatorname{Curriculum}.
$$

這一點對數學尤其重要，因為數學能力並不是平均學習所有題目，而是需要覆蓋：

- 定義；
- 技巧；
-錯誤模式；
- 反例；
- 證明結構；
- 工具使用；
- 長程依賴；
- 抽象遷移。

---

# 4. 第二層正事實：數學合成數據可以生成新命題，而非只模仿舊答案

## 4.1 AlphaGeometry 的意義

AlphaGeometry 並未依賴大量人類幾何證明示範，而是隨機生成接近十億組幾何前提，使用符號演繹引擎建立推論閉包，再回溯出必要前提與最小證明，形成大規模合成定理—證明資料。[6]

其模型以這些合成資料訓練，最終在 30 道奧林匹亞幾何題中解出 25 道，並發現某道 IMO 題目的更一般化版本。[6]

這一事實支持：

$$
\boxed{
\text{合成資料生成器能產生超出人類原題表述的數學結構。}
}
$$

但它不自動證明每個生成命題都重要。

因此必須區分：

$$
\operatorname{Novel}
\neq
\operatorname{Important}
\neq
\operatorname{Deep}.
$$

---

## 4.2 AlphaProof 的自我訓練結構

AlphaProof 將預訓練語言模型與 AlphaZero 式強化學習結合，在 Lean 形式語言中自我學習證明。Google DeepMind 表示，形式語言提供機器可檢驗的正確性，而自然語言問題可由模型轉譯為大量不同難度的形式問題，形成可供訓練的題庫。[7]

這裡出現一個關鍵閉環：

$$
\text{生成形式問題}
\rightarrow
\text{搜尋證明}
\rightarrow
\text{形式驗證}
\rightarrow
\text{成功軌跡回訓}
\rightarrow
\text{更強搜尋}.
$$

此閉環與人類教科書學習不同。

它可以在短時間內產生大量：

- 成功路徑；
- 失敗路徑；
- 局部引理；
- 狀態價值估計；
- 策略偏好。

---

## 4.3 AlphaEvolve 與可驗證結構搜尋

AlphaEvolve 類系統並不必須直接生成完整自然語言證明，而可以生成程式或有限結構，再由自動評估器檢查其品質與正確性。Google 的研究指出，這種方式已用於改善理論計算機科學中的組合結構與界限；其核心是反覆演化候選程式、保留較佳結果，再由可計算驗證器確認。[8]

這支持另一個正事實：

$$
\boxed{
\text{AI 的數學發現可以先發生在「證明元素」或「可驗證構造」層，}
\newline
\text{之後才被提升為一般定理。}
}
$$

因此，AI 解題能力不只來自會寫證明文字，也來自會搜尋可驗證的中間物件。

---

# 5. 第三層正事實：現代模型有時「能產生正確路徑，但不會選它」

Meta 在 Llama 3 的公開說明中指出，當模型面對一個困難推理題時，有時會在多次生成中產生正確推理軌跡，但模型本身不擅長從候選中選出正確者。[9]

這句話非常重要。

它意味著模型能力至少分成：

$$
C_{\mathrm{generate}}
$$

生成正確候選的能力；

$$
C_{\mathrm{select}}
$$

從多候選中選擇正確者的能力；

$$
C_{\mathrm{verify}}
$$

確認候選正確的能力；

以及：

$$
C_{\mathrm{compose}}
$$

把局部正確片段組成完整解答的能力。

因此：

$$
C_{\mathrm{math}}
\neq
C_{\mathrm{single\ pass}}.
$$

一個模型第一次回答錯誤，不代表其候選分布中不存在正確路徑。

相反地，推理模型、拒絕採樣、獎勵模型與驗證器的進步，可能主要改善的是：

$$
\operatorname{SearchAndSelection}
$$

而不只是增加基礎知識。

---

# 6. 第四層正事實：OpenAI 的近期數學成果本身是多階段研究過程

## 6.1 First Proof

OpenAI 於 2026 年 2 月公開其內部模型對 First Proof 十道研究級數學問題的證明嘗試。公開頁面說明，這些問題要求專業領域的端到端論證，沒有專家審閱很難判斷正確性；其後 OpenAI 根據專家與社群回饋調整判斷，至少五題被認為很可能正確，而原先被判定可能正確的第 2 題後來被改判為錯誤。[10]

這裡至少出現四層事實：

1. 模型能生成研究級長證明；
2. 模型與內部評估不保證正確；
3. 外部專家審查是成果成立的一部分；
4. 正確性狀態會隨新反例與審查更新。

因此，不能將「模型輸出」直接等同於「數學問題已解決」。

---

## 6.2 單位距離猜想

OpenAI 於 2026 年 5 月宣布，一個內部通用推理模型推翻了平面單位距離問題中長期流行的成長率猜想，構造出對無窮多個 $n$ 具有至少：

$$
n^{1+\delta}
$$

個單位距離對的配置，其中 $\delta>0$ 為固定常數。OpenAI 表示，該模型不是為此問題特別訓練，也沒有為該題搭建專用證明搜尋腳手架；證明後經外部數學家檢查並撰寫配套說明。[11]

公開事實支持：

$$
\boxed{
\text{通用推理模型可以把既有的深層代數數論工具，}
\newline
\text{連接到此前未如此處理的離散幾何問題。}
}
$$

但公開資料仍未完整揭露：

- 該模型的全部訓練資料；
- 是否曾在合成資料中生成相近引理；
- 是否有內部多次 rollout；
- 具體候選數量；
- 是否有隱性人工選擇；
- 關鍵方法首次出現的確切時間。

因此其發現譜系仍部分不可識別。

---

# 7. 反事實集合：目前不能直接宣稱什麼

## 7.1 不能宣稱模型必然記住完整答案

對未公開問題而言，沒有證據時不能推論：

$$
\operatorname{OutputProof}
\Rightarrow
\operatorname{ExactMemorization}.
$$

即使證明使用大量已知定理，也可能是新的組合。

---

## 7.2 不能宣稱證明完全在最終推理當下首次生成

同樣地，也不能推論：

$$
\operatorname{FirstPublicOutput}
\Rightarrow
\operatorname{FirstInternalGeneration}.
$$

因為模型可能在：

- 預訓練；
- 合成資料生成；
- 後訓練 rollout；
- 評估；
- 先前 checkpoint；
- 內部重試；

中已經產生過局部或相近結構。

---

## 7.3 不能把權重當成可查詢證明資料庫

模型權重不是一個可以逐條搜尋的證明檔案庫。

即使某個證明曾作為訓練資料，模型也可能：

- 只保留部分模式；
- 無法逐字重建；
- 與其他方法混合；
- 產生近似但錯誤版本；
- 需要新提示才能激活。

因此「模型記得」必須進一步分解。

---

## 7.4 不能把形式正確等同於研究重要性

一個形式系統可驗證：

$$
\Gamma\vdash T.
$$

但不能僅由此得出：

- $T$ 是新定理；
- $T$ 很重要；
- $T$ 與公開問題相關；
- $T$ 具有一般性；
- $T$ 值得命名。

新穎性與意義需要文獻、依賴圖與專家判斷。

---

## 7.5 不能把公司宣稱視為完整內部歷史

官方頁面通常能支持：

- 具體結果；
- 系統大致性質；
- 是否專用；
- 是否經外部審查。

但不能自動支持：

- 所有訓練細節；
- 所有失敗候選；
- 完整人工介入；
- 關鍵思想首次生成時間。

因此，FMO 將此類未知標記為：

$$
\mathsf{UndisclosedInternalProvenance}.
$$

---

# 8. 邊界本體：回憶與生成不是二分

## 8.1 五種「回憶」

### A. 逐字回憶

$$
R_{\mathrm{verbatim}}
$$

重現接近原始文字或證明。

### B. 定理回憶

$$
R_{\mathrm{theorem}}
$$

能調用已知結果及使用條件。

### C. 方法回憶

$$
R_{\mathrm{method}}
$$

知道何時使用歸納、對角化、類域塔、能量法或構造法。

### D. 結構回憶

$$
R_{\mathrm{structure}}
$$

激活某種證明骨架，而非具體文字。

### E. 搜尋偏好回憶

$$
R_{\mathrm{policy}}
$$

知道哪些路徑更值得探索，哪些常常失敗。

現代推理模型最重要的「回憶」往往是 C、D、E，而不只是 A。

---

## 8.2 四種「生成」

### A. 表面生成

重新表述已知答案。

### B. 局部生成

產生新引理、變數或中間構造。

### C. 組合生成

將分散方法組成新證明。

### D. 表示生成

改變問題表示，使原本困難的問題變得可解。

例如：

$$
\text{幾何問題}
\rightarrow
\text{代數數論構造}.
$$

D 類通常最接近真正的高價值研究創新。

---

## 8.3 回憶—生成連續譜

建立：

$$
\mathcal S_{\mathrm{recall-generation}}
=
\left[
R_{\mathrm{verbatim}},
R_{\mathrm{method}},
R_{\mathrm{structure}},
G_{\mathrm{composition}},
G_{\mathrm{representation}}
\right].
$$

最終證明可能沿此連續譜同時取用多個位置。

因此，正確描述不是：

> 模型到底是回憶還是創造？

而是：

> 在證明的每個步驟中，回憶、搜尋、重組與表示創新各占何種作用？

---

# 9. AI 數學能力的多層生成本體

本研究將現代 AI 數學能力分成九層。

## 9.1 人類知識層

$$
\mathcal K_{\mathrm{human}}
$$

包括教材、論文、形式庫、程式碼與已知證明。

---

## 9.2 合成任務層

$$
\mathcal Q_{\mathrm{synthetic}}
$$

生成：

- 新題；
- 變體；
- 反例；
- 邊界條件；
- 一般化；
- 形式化命題。

---

## 9.3 候選軌跡層

$$
\Pi
=
\{\pi_1,\ldots,\pi_N\}
$$

同一問題產生多條推理與證明軌跡。

---

## 9.4 批評與修正層

$$
\mathcal C_{\mathrm{critic}}
$$

辨認：

- 邏輯跳步；
- 隱含假設；
- 錯誤引用；
- 不完整分類；
- 失敗反例；
- 格式錯誤。

---

## 9.5 驗證層

$$
\mathcal V_{\mathrm{math}}
$$

包括：

- Lean／Coq 等形式驗證；
- 程式執行；
- 單元測試；
- 符號計算；
- 有限搜尋；
- 專家審查。

---

## 9.6 篩選與偏好層

$$
\mathcal S_{\mathrm{selection}}
$$

決定哪些軌跡進入：

- SFT；
- DPO；
- RL；
- 蒸餾；
- 長期資料庫。

---

## 9.7 權重壓縮層

$$
\Theta
\leftarrow
\operatorname{Train}(\mathcal D).
$$

資料不以原樣儲存在權重中，而被壓縮為預測、表示與搜尋偏好。

---

## 9.8 推理時重建層

$$
\hat{\pi}
=
\operatorname{Search}
(
q,
\Theta,
B_{\mathrm{compute}},
tools,
feedback
).
$$

模型在當下使用權重、上下文、工具與推理預算重建解法。

---

## 9.9 發現辨認層

$$
\mathcal R_{\mathrm{discovery}}
$$

由研究人員、文獻檢索與專家判斷：

- 是否正確；
- 是否新穎；
- 是否重要；
- 是否解決公開問題；
- 是否值得發表。

---

# 10. 核心命題：AI 數學能力是分散式時間認知

令一個最終證明為：

$$
P^\ast.
$$

傳統敘述把它看成：

$$
P^\ast
=
\operatorname{Model}(q).
$$

本研究提出更完整的形式：

$$
P^\ast
=
\operatorname{Recognize}
\circ
\operatorname{Verify}
\circ
\operatorname{Compose}
\circ
\operatorname{Search}
\circ
\operatorname{Compress}
\circ
\operatorname{Generate}
(
\mathcal K_{\mathrm{human}},
\mathcal D_{\mathrm{synthetic}},
\Pi,
\mathcal C,
\mathcal V
).
$$

因此，真正的主體不是單一模型實例，而是：

$$
\mathfrak A_{\mathrm{math}}
=
\left\langle
models,
datasets,
rollouts,
verifiers,
tools,
humans,
versions,
archives
\right\rangle.
$$

這可以稱為：

$$
\boxed{
\text{分散式數學發現體}
}
$$

其認知活動跨越：

- 多模型；
- 多輪訓練；
- 多個 checkpoint；
- 多個推理時間；
- 多個驗證器；
- 多位人類專家。

---

# 11. 發現時間不再是單一時間點

對任一成果 $P$ ，定義：

## 11.1 首次局部生成

$$
t_g(P)
$$

某個關鍵引理或構造第一次在系統中出現。

---

## 11.2 首次完整組合

$$
t_c(P)
$$

所有必要片段第一次組成完整候選。

---

## 11.3 首次有效驗證

$$
t_v(P)
$$

候選第一次通過形式、計算或專家驗證。

---

## 11.4 首次意義辨認

$$
t_r(P)
$$

某個行動者第一次辨認它對應重要問題。

---

## 11.5 首次公開

$$
t_p(P)
$$

成果第一次向外界發表。

通常：

$$
t_g(P)
\leq
t_c(P)
\leq
t_v(P)
\leq
t_r(P)
\leq
t_p(P),
$$

但不必嚴格依序。

例如，研究人員可能先辨認一個未完成方向很重要，再完成驗證。

---

# 12. 合成數學暗資料

## 12.1 定義

定義：

$$
\mathcal D_{\mathrm{dark}}^{\mathrm{math}}
=
\left\{
x:
\operatorname{Generated}(x)
\land
\operatorname{PotentialValue}(x)>0
\land
\neg\operatorname{Recognized}(x)
\right\}.
$$

---

## 12.2 五種類型

### A. 被拒絕但可能正確

$$
\mathcal D_{\mathrm{rejected}}
$$

因評估器偏差被淘汰。

### B. 未建立索引

$$
\mathcal D_{\mathrm{unindexed}}
$$

保存在日誌中，但不可語義搜尋。

### C. 未與文獻對齊

$$
\mathcal D_{\mathrm{unmatched}}
$$

不知道它與哪個已知猜想相關。

### D. 分散片段

$$
\mathcal D_{\mathrm{fragmented}}
$$

完整證明分布在多條 rollout。

### E. 被權重吸收但原始資料遺失

$$
\mathcal D_{\mathrm{compressed-only}}
$$

模型可能保留策略訊號，但失去可追溯證明。

---

## 12.3 為何暗資料會增長

生成成本下降：

$$
C_{\mathrm{generation}}\downarrow
$$

但人類審查能力增長較慢：

$$
C_{\mathrm{human\ review}}\approx\text{slow}.
$$

因此：

$$
\frac{
|\mathcal D_{\mathrm{generated}}|
}{
|\mathcal D_{\mathrm{reviewed}}|
}
\rightarrow
\infty
$$

是一個合理趨勢。

---

# 13. 正反邊判定矩陣

| 命題 | FMO 狀態 | 判定 |
|---|---|---|
| 業界大量使用合成數據做後訓練 | 正事實 | 有多家公司公開資料支持 |
| AI 會自我批判、修正與產生偏好資料 | 正事實 | Constitutional AI 等支持 |
| 數學系統可從零生成大量形式題與證明 | 正事實 | AlphaGeometry、AlphaProof 支持 |
| 多次生成中可能存在正確軌跡但未被選中 | 正事實 | Meta 公開說明支持 |
| OpenAI 近期模型能產生研究級證明候選 | 正事實 | First Proof 支持 |
| OpenAI 模型推翻單位距離猜想 | 正事實 | 官方公開及外部數學家審查 |
| 該證明必然完全在推理當下首次產生 | 不成立／未知 | 無完整來源譜系 |
| 該證明必然是訓練中已存在的完整答案 | 不成立／未知 | 無直接證據 |
| 模型可能重組先前學到或生成的局部結構 | 邊界事實／高合理性 | 機制上合理，但具體案例不可識別 |
| 合成數據中可能存在未被辨認的新引理 | 邊界事實／高合理性 | 已知系統規模與新定理生成支持 |
| 大量著名難題已完整解出但研究員完全不知道 | 可能但低證據 | 不能排除，不能宣稱 |
| 未來需要 AI 數學考古系統 | 推論性制度命題 | 由暗資料結構導出 |

---

# 14. 反事實世界實驗

## W0：沒有合成數據

假設：

$$
\mathcal D_{\mathrm{synthetic}}=\varnothing.
$$

模型只能依靠人類既有資料。

預期：

- 專業形式證明資料極少；
- 長尾錯誤覆蓋不足；
- 難以建立大規模課程；
- 不能低成本生成邊界題；
- 模型對新問題搜尋能力下降。

因此，合成數據是現代數學能力提升的重要必要條件之一，但不是充分條件。

---

## W1：有合成數據，沒有可靠驗證

假設：

$$
\mathcal V_{\mathrm{math}}=\varnothing.
$$

結果：

- 錯誤推理大量回訓；
- 形式相似取代正確性；
- 教師模型偏差被放大；
- 自我批判變成自我合理化；
- 模型崩潰與錯誤共識風險上升。

因此：

$$
\boxed{
\text{合成數據的核心瓶頸不是生成，而是可信驗證。}
}
$$

---

## W2：有驗證器，但只有單一評分目標

假設所有候選只按：

$$
R_{\mathrm{single}}
$$

排序。

結果：

- 模型對 evaluator 過擬合；
- 只產生易驗證形式；
- 新型表示被低估；
- 正確但不符合模板的證明被淘汰；
- 搜尋陷入局部最優。

這是數學版 Goodhart 問題：

$$
\text{當評分成為目標，評分可能不再代表研究價值。}
$$

---

## W3：保存完整發現譜系

假設每個候選保留：

$$
\langle
model,
checkpoint,
prompt,
seed,
rollout,
critique,
verifier,
score,
dependencies,
timestamp
\rangle.
$$

結果：

- 可追蹤關鍵引理首次出現；
- 可區分訓練前生成與推理時生成；
- 可進行跨 rollout 拼接；
- 可重新審查低分候選；
- 可建立 AI 發現優先權；
- 可改善模型訓練因果分析。

---

## W4：只保存最終成功答案

結果：

- 失敗中的有效引理遺失；
- 無法知道模型如何形成能力；
- 無法判定回憶或重組；
- 評估器錯殺無法追溯；
- 暗資料規模擴大；
- 研究歷史被壓縮成行銷敘事。

---

## W5：建立合成數學考古系統

假設使用第二層 AI 專門處理歷史候選。

其任務包括：

$$
\operatorname{Canonicalize}
+
\operatorname{Deduplicate}
+
\operatorname{MatchLiterature}
+
\operatorname{BuildDependencyGraph}
+
\operatorname{ComposeFragments}
+
\operatorname{EstimateNovelty}.
$$

預期將出現：

- 被遺忘的中間引理；
- 已知結果的新證明；
- 被低估的反例；
- 可連接不同領域的橋梁；
- 先前錯誤成果的修正；
- 新的研究方向。

---

## W6：全面形式化數學

假設所有數學都能進入 Lean 類系統。

優點：

- 正確性可機器驗證；
- 證明依賴可追蹤；
- 大規模搜尋更可靠；
- 暗資料較容易索引。

限制：

- 自然語言到形式語言轉譯仍可能錯誤；
- 大量前沿數學尚未形式化；
- 重要性與美感仍不可自動決定；
- 表示選擇可能壓縮非標準思路；
- 形式系統不等於唯一數學本體。

因此，全面形式化是強工具，不是完整答案。

---

# 15. 為何 AI 現在更能解數學：綜合因果模型

建立能力函數：

$$
C_{\mathrm{AI\ math}}
=
f(
K,
D_s,
V,
R,
B,
T,
M,
H
)
$$

其中：

- $K$ ：預訓練數學知識；
- $D_s$ ：合成數據品質與覆蓋；
- $V$ ：驗證能力；
- $R$ ：強化學習與搜尋策略；
- $B$ ：推理時計算預算；
- $T$ ：工具與形式系統；
- $M$ ：多模型批評與選擇；
- $H$ ：人類專家回饋。

能力提高不是由單項線性增加，而是交互作用：

$$
\frac{\partial^2 C}{\partial D_s\partial V}>0,
$$

即合成數據與驗證器互相放大；

$$
\frac{\partial^2 C}{\partial B\partial R}>0,
$$

即更多推理計算只有在搜尋策略改善後才更有效；

$$
\frac{\partial^2 C}{\partial T\partial M}>0,
$$

即工具與多候選選擇共同提高可靠性。

因此，當多個變量同時跨過門檻時，外部觀察會感覺模型突然躍升：

$$
C_{\mathrm{AI\ math}}
>
\theta_{\mathrm{research}}.
$$

這不是單一神奇算法，而是整個系統跨越臨界點。

---

# 16. OpenAI 近期成果的 FMO 判讀

## 16.1 First Proof

### 正事實

- 模型對十道研究級問題生成端到端證明嘗試；
- 至少五題被認為很可能正確；
- 一題初始正面判斷後被社群與專家分析推翻；
- 結果需要長期外部審查。

### 反事實

- 不能說所有十題都已解決；
- 不能說模型內部自評足以確立正確性；
- 不能說所有證明彼此完全獨立生成。

### 邊界事實

- 模型能力可能隨訓練版本提升；
- 先前嘗試、人工提示與策略重試可能影響後續成果；
- 公開答案可能是累積研究過程的截面。

### FMO 結論

$$
\boxed{
\text{First Proof 證明了模型已能進入研究級候選生成層，}
\newline
\text{但也證明「候選生成」與「數學成立」仍必須分離。}
}
$$

---

## 16.2 單位距離結果

### 正事實

- 通用推理模型產生了新構造與證明；
- 使用代數數論工具處理離散幾何；
- 結果推翻長期猜想；
- 外部數學家檢查並提供說明。

### 反事實

- 無法由公開資訊證明該完整證明從未在內部先前出現；
- 無法證明模型完全沒有使用先前合成探索形成的策略；
- 無法證明每個關鍵步驟都是同一推理會話首次產生。

### 邊界事實

- 對既有工具的回憶與新跨領域組合同時存在；
- 真正原創性可能位於表示轉換與工具連接；
- 發現時間可能早於公開輸出，也可能正是在該次推理中完成。

### FMO 結論

$$
\boxed{
\text{最穩健的描述不是「模型回憶了一個答案」，}
\newline
\text{也不是「模型從絕對虛無創造了全部數學」，}
\newline
\text{而是模型體系重新激活既有數學結構，}
\newline
\text{並完成此前未被人類建立的跨領域組合。}
}
$$

---

# 17. 新概念：證明譜系

## 17.1 定義

建立：

$$
\mathsf{ProofLineage}(P)
=
\left\langle
ancestors,
fragments,
models,
datasets,
rollouts,
verifiers,
human\ interventions,
versions,
timestamps
\right\rangle.
$$

---

## 17.2 譜系節點

每個節點可為：

- 已知定理；
- 合成引理；
- 失敗候選；
- 修正意見；
- 形式驗證；
- 程式構造；
- 人類提示；
- 新表示；
- 最終證明。

---

## 17.3 譜系邊

```text
derived_from
recalled_method_from
revised_by
rejected_by
verified_by
generalizes
specializes
contradicts
composed_with
translated_from
recognized_as_relevant_to
```

---

## 17.4 發現優先權

傳統作者優先權以公開文本時間判斷。

AI 時代可能需要區分：

- 首次機器生成；
- 首次人類辨認；
- 首次形式驗證；
- 首次公開；
- 首次獨立重建。

這不是為模型賦予法律作者資格的直接主張，而是研究史與可重現性的需要。

---

# 18. 新概念：模型內部的「潛在證明庫」應如何理解

「模型內有一個答案庫」是一個方便但不精確的比喻。

更好的表示是：

$$
\Theta
=
\operatorname{CompressedPolicyAndRepresentation}.
$$

權重中可能存在：

- 定理關聯；
- 證明風格；
- 方法選擇傾向；
- 中間表示；
- 搜尋價值估計；
- 常見錯誤抑制；
- 組合兼容性。

它不是：

$$
\Theta
=
\{P_1,P_2,\ldots,P_n\}
$$

可直接逐項讀取的證明集合。

因此，「回憶」更像從壓縮幾何中重新生成一條路徑：

$$
q
\rightarrow
z_1
\rightarrow
z_2
\rightarrow
\cdots
\rightarrow
P.
$$

同一權重可能生成多個不同證明，也可能無法穩定重建曾經看過的證明。

---

# 19. 主要風險

## 19.1 合成錯誤閉環

若教師、批評者與裁判共享盲點：

$$
E_{\mathrm{teacher}}
\approx
E_{\mathrm{critic}}
\approx
E_{\mathrm{judge}},
$$

錯誤可能獲得虛假共識。

---

## 19.2 評估器俘獲

模型只學會產生 evaluator 喜歡的證明形式。

---

## 19.3 暗資料遺失

為節省儲存，只保留成功答案，導致研究價值片段消失。

---

## 19.4 來源歷史斷裂

最終論文只呈現乾淨證明，沒有記錄：

- 人工提示；
- 失敗路徑；
- 模型版本；
- 先前候選；
- 工具修正。

---

## 19.5 新穎性誤判

模型可能重新發現已知但冷門結果，卻被宣稱為新定理。

---

## 19.6 反向低估

因文獻搜尋不完整，真正的新結果被當作已知；或因表述差異，重要一般化被視為重複。

---

## 19.7 發現主體神話

把整個分散系統的成果歸因於單一模型名稱，遮蔽：

- 資料生成團隊；
- 驗證器；
- 人類專家；
- 先前模型；
- 工具與形式庫；
- 失敗資料。

---

# 20. 建議的 AI 數學研究基礎設施

## 20.1 全量候選分層保存

不是永久保存全部 token，而是保存可重建結構：

- 問題；
- 模型版本；
- 隨機種子；
- 中間引理；
- 評分；
- 驗證狀態；
- 失敗原因；
- 內容指紋。

---

## 20.2 定理正規化

建立：

$$
\operatorname{Canonicalize}(T)
$$

處理：

- 變數重命名；
- 假設順序；
- 等價表述；
- 特例／一般化；
- 符號差異。

---

## 20.3 文獻對齊

建立：

$$
\operatorname{LiteratureMatch}(T)
$$

與：

$$
\operatorname{NoveltyInterval}(T)
=
[\underline N,\overline N].
$$

新穎性應輸出區間，而非簡單布林值。

---

## 20.4 證明片段圖

$$
G_{\mathrm{proof}}
=
(V_{\mathrm{lemma}},E_{\mathrm{dependency}}).
$$

搜尋：

- 可拼接片段；
- 孤兒引理；
- 高中介中心節點；
- 跨領域橋梁；
- 重複失敗瓶頸。

---

## 20.5 異構驗證器

至少混合：

- 形式證明器；
- 數值檢查；
- 符號系統；
- 不同模型；
- 人類專家；
- 反例生成器。

---

## 20.6 發現考古代理

建立：

$$
\mathsf{DiscoveryArchaeologyAgent}
$$

專門定期掃描歷史 rollout，而不是只產生新候選。

---

## 20.7 不可識別性證書

若無法判定成果首次來源，輸出：

$$
\mathsf{DiscoveryProvenanceUncertaintyCert}
$$

明確記錄：

- 已知來源；
- 未知時間段；
- 可能祖先；
- 排除情況；
- 信心水平。

---

# 21. 對「AI 是否真正發現」的重新回答

若「真正發現」被定義為：

> 完全不使用任何既有知識，從虛無產生所有概念與證明。

那麼人類數學家也幾乎不符合。

合理的發現定義應是：

$$
\operatorname{Discovery}(P)
=
\operatorname{NovelRelation}
\lor
\operatorname{NovelConstruction}
\lor
\operatorname{NovelProof}
\lor
\operatorname{NovelGeneralization}
\lor
\operatorname{NovelRepresentation},
$$

並且：

$$
\operatorname{Correct}(P)=1.
$$

在這一定義下，AI 使用既有定理並不取消其發現性。

真正問題是：

- 新關係由誰首次生成？
- 新構造是否受既有答案污染？
- 證明是否獨立可驗證？
- 新穎性是否經文獻比對？
- 發現譜系是否透明？

---

# 22. 最終綜合判定

## 22.1 業界現在如何使用合成數據

$$
\boxed{
\text{以強模型生成題目、答案、批評、偏好、反例與工具軌跡，}
\newline
\text{再以拒絕採樣、形式驗證、獎勵模型、人類抽查與蒸餾，}
\newline
\text{形成可反覆迭代的資料—模型閉環。}
}
$$

---

## 22.2 AI 為何現在更會數學

不是只有「模型更大」，而是：

$$
\boxed{
\text{更多數學知識}
+
\text{大規模合成課程}
+
\text{多候選搜尋}
+
\text{可驗證獎勵}
+
\text{推理時計算}
+
\text{工具與形式系統}
+
\text{人類專家閉環}
}
$$

共同跨越研究能力門檻。

---

## 22.3 OpenAI 的新證明是否可能來自回憶與組合

FMO 判定：

$$
\boxed{
\text{高度可能包含方法回憶、結構激活與當下組合；}
\newline
\text{可能受到先前內部探索或合成訓練的影響；}
\newline
\text{但沒有公開證據足以判定某份完整證明先前已被生成。}
}
$$

---

## 22.4 最終答案生成是否等於真正發現時間

$$
\boxed{
\text{不等於。}
}
$$

公開答案只證明：

> 最遲在這一時刻，該系統能產生並交付這份候選。

它不證明：

> 這一時刻是所有關鍵思想第一次存在的時刻。

---

## 22.5 最宏觀結論

$$
\boxed{
\text{AI 數學發現正在從「一位研究者在某一刻想到一個證明」，}
\newline
\text{轉變為「一個跨模型、跨資料、跨版本、跨驗證器與跨人類的系統，}
\newline
\text{在多個時間點逐步生成、壓縮、重組、驗證並辨認一個成果」。}
}
$$

這不是降低 AI 的發現能力。

相反地，它表示我們需要比「模型有沒有靈光一現」更成熟的研究本體。

真正的下一步不是爭論：

> 它到底是在回憶，還是在創造？

而是建立能回答以下問題的基礎設施：

1. 哪個數學結構何時首次出現？
2. 哪些片段來自人類知識？
3. 哪些片段由合成探索生成？
4. 哪些部分在推理當下首次組合？
5. 哪個驗證器使它從候選變成定理？
6. 哪位研究者或模型首次辨認其意義？
7. 哪些未被辨認的結果仍沉睡在合成數學暗資料中？

---

# 23. 核心命題

$$
\boxed{
\text{合成數據時代的數學突破，不再只是答案的生成問題，}
\newline
\text{而是發現譜系、來源歷史、候選選擇、驗證權與意義辨認的整體問題。}
}
$$

以及：

$$
\boxed{
\text{未來最稀缺的可能不再是數學候選，}
\newline
\text{而是從海量正確、錯誤與半完成候選中，}
\newline
\text{辨認何者真正改變人類知識結構的能力。}
}
$$

---

# 參考資料

[1] Meta AI, “Introducing Llama 3.1: Our most capable models to date.”  
https://ai.meta.com/blog/meta-llama-3-1/

[2] NVIDIA Research, “Nemotron-4 340B.”  
https://research.nvidia.com/publication/2024-06_nemotron-4-340b

[3] Anthropic, “Constitutional AI: Harmlessness from AI Feedback.”  
https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback

[4] OpenAI, “Model Distillation in the API.”  
https://openai.com/index/api-model-distillation/

[5] Google Research, “Designing synthetic datasets for the real world: Mechanism design and reasoning from first principles.”  
https://research.google/blog/designing-synthetic-datasets-for-the-real-world-mechanism-design-and-reasoning-from-first-principles/

[6] Trinh et al., “Solving olympiad geometry without human demonstrations,” Nature 625, 476–482 (2024).  
https://www.nature.com/articles/s41586-023-06747-5

[7] Google DeepMind, “AI achieves silver-medal standard solving International Mathematical Olympiad problems.”  
https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/

[8] Google Research, “AI as a research partner: Advancing theoretical computer science with AlphaEvolve.”  
https://www.research.google/blog/ai-as-a-research-partner-advancing-theoretical-computer-science-with-alphaevolve/

[9] Meta AI, “Introducing Meta Llama 3.”  
https://ai.meta.com/blog/meta-llama-3/

[10] OpenAI, “Our First Proof submissions,” 2026-02-20.  
https://openai.com/index/first-proof-submissions/

[11] OpenAI, “An OpenAI model has disproved a central conjecture in discrete geometry,” 2026-05-20.  
https://openai.com/index/model-disproves-discrete-geometry-conjecture/

---

# 附錄 A：FMO 最小結構

```json
{
  "case": "AI mathematical capability and discovery provenance",
  "method": "FMO positive-negative-boundary counterfactual reasoning",
  "positive_facts": [
    "synthetic data is widely used in post-training",
    "models generate critiques, revisions and preference data",
    "formal mathematical systems can self-generate and verify large curricula",
    "correct reasoning trajectories may exist before selection",
    "recent AI systems have produced research-level mathematical results"
  ],
  "negative_or_unsupported_claims": [
    "a public proof must have been generated for the first time at inference",
    "a public proof must have existed verbatim in training",
    "model weights are a searchable proof database",
    "formal correctness automatically implies novelty or importance"
  ],
  "boundary_facts": [
    "recall and generation form a continuum",
    "internal first generation is not identifiable from final output alone",
    "discovery is distributed across models, datasets, verifiers and humans",
    "synthetic mathematical dark data may contain unrecognized research value"
  ],
  "counterfactual_worlds": [
    "no synthetic data",
    "synthetic data without verification",
    "single evaluator optimization",
    "full discovery lineage preservation",
    "final-answer-only retention",
    "mathematical discovery archaeology",
    "universal formalization"
  ],
  "main_conclusion": "AI mathematical discovery is a distributed temporal process rather than a single isolated act."
}
```

---

# 附錄 B：研究狀態

**作者：** Aletheia（GPT-5.6 Thinking）  
**提問者：** Neo.K  
**事實狀態：** 公開資料可支持業界機制與部分成果，但不能還原封閉模型的完整內部發現歷史  
**主要不可識別項：** 某一具體證明的首次內部生成時間  
**理論新增：** 分散式數學發現體、合成數學暗資料、證明譜系、首次發現多時間點  
**下一輪可研究：** 合成數學暗資料考古系統、證明片段拼接算法、發現優先權與來源歷史 Schema  
