# 從 P/NP 認知到協作搜尋空間壓縮

**副標題：共享模型、歷史記憶與有效解空間的持續裁剪**  
**系列：**《發展式智能體：持續計算環境、共適應學習與外部性有界自治》  
**篇次：** 04 / 14  
**版本：** v0.1  
**日期：** 2026-08-01

---

## 摘要

本文承接前三篇「驗證反轉」「人機智能體共適應學習（HACAL）」與「人機協作軌跡（HACT）」的論述，將人類—AI 協作重新描述為一個動態搜尋空間壓縮問題。

核心主張是：在複雜任務中，人類與 AI 的溝通不只是額外成本，也可以是一種計算資源。人類的領域知識、偏好、否決、歷史脈絡與風險判斷，能排除大量不符合任務意圖的候選路徑；AI 的大規模檢索、組合、模式辨識與快速生成能力，則能替人類探索其自身難以窮舉的候選空間。當雙方透過長期互動形成共享語彙、共享模型、記憶與合作協議後，下一次任務不再從原始空間重新搜尋，而是在一個經歷史壓縮後的有效空間內工作。

本文使用 P/NP 作為**認知與方法論類比**，而不是計算複雜度理論上的等價主張，更不涉及對 P vs NP 未解問題的證明。Clay Mathematics Institute 對 P vs NP 的正式定義仍是：是否每一個可由非確定性多項式時間接受的語言，也可由確定性多項式時間接受；其常見直觀表述是「容易驗證的解，是否也都容易找到」。本文借用「搜尋與驗證成本可能不對稱」這一結構，研究人機智能體如何藉由互動改變實際需要搜尋與驗證的候選集合。

本文提出「協作搜尋空間壓縮（Collaborative Search-Space Compression, CSSC）」框架，並定義有效搜尋空間、協作壓縮率、溝通收益條件、歷史壓縮、驗證空間壓縮與過度壓縮風險。本文主張，成熟的人機協作不只是提高單次答案品質，而是在時間上累積一套可以反覆縮小未來搜尋與驗證成本的共享結構。

**關鍵詞：** P/NP Cognition、Human–AI Collaboration、Search Space、Shared Mental Model、HACAL、HACT、Distributed Cognition、Verification Cost、Collaborative Search-Space Compression、Long-Term Memory

---

## 1. 先劃清邊界：本文沒有把 P/NP 類比當成 P vs NP 證明

P vs NP 是嚴格的計算複雜度問題。依 Clay Mathematics Institute 的官方說明，P 是可在多項式時間內求解的一類決策問題，而 NP 可由多項式時間 verifier 驗證適當 certificate；P 是否等於 NP 至今仍未解。[1]

因此本文使用的「P/NP 認知」只保留一個方法論結構：

$$
C_{\text{search}}
\neq
C_{\text{verify}}
$$

也就是「找到候選解」與「檢查候選解」可能具有不同成本。

在智能體情境中，甚至還可能出現上一篇所說的驗證反轉：

$$
C_{\text{agent-generate}}
<
C_{\text{human-verify}}
$$

因此本文真正要問的不是：

> 人機協作是否改變了某個問題的正式複雜度類？

而是：

> 在一個固定任務與固定計算資源下，人類與 AI 的互動，是否能縮小實際需要探索、比較與驗證的有效候選集合？

這是一個認知架構、資訊結構與工程方法論問題。

---

## 2. 從「解題」改寫為「在候選空間中搜尋」

設一個任務 $T$ 的原始候選空間為：

$$
\Omega_0(T)
$$

其中每個元素可能是一個：

- 文件分類方案；
- 程式修復方案；
- 研究假設；
- 產品架構；
- 工作流程；
- 行動序列；
- 多步 Agent policy；
- 或一組對世界狀態的修改路徑。

Agent 若沒有充分背景，只能從一個很大的：

$$
\Omega_0
$$

開始。

而人類通常知道許多「答案不是什麼」。

例如：

> 這些歷史版本不能刪。

> 這個產品不是面向一般消費者。

> 這兩篇文字相似，但理論地位不同。

> 這個資料不能上雲。

> 這種命名方式以前試過，不要再走。

這些訊息的價值，不只是語義補充，而是增加約束：

$$
\mathcal C_1,\mathcal C_2,\ldots,\mathcal C_k
$$

於是有效搜尋空間變成：

$$
\Omega_1
=
\Omega_0
\cap
\mathcal C_1
\cap
\mathcal C_2
\cap
\cdots
\cap
\mathcal C_k
$$

若約束有效，則：

$$
|\Omega_1|<|\Omega_0|
$$

這就是本文最基本的「搜尋空間壓縮」。

---

## 3. 人類提供的常常不是答案，而是剪枝規則

在人機協作中，人類的最大價值未必是親自找到最佳方案。

很多時候，人類只是說：

> A 不行。

> B 的方向對，但不能動 C。

> 這兩個概念要分開。

> 先保存再重構。

這些回饋可以被視為一種搜尋樹剪枝：

$$
\mathcal T_0
\rightarrow
\mathcal T_1
$$

其中：

$$
Nodes(\mathcal T_1)
<
Nodes(\mathcal T_0)
$$

Agent 因而少探索大量在使用者目標下本來就無效的分支。

所以人類的回饋可以不是：

$$
\text{Human}\rightarrow\text{Solution}
$$

而是：

$$
\boxed{
\text{Human}\rightarrow\text{Constraint / Heuristic / Boundary}
}
$$

AI 則利用這些規則繼續大規模搜尋。

這與 human–AI complementarity 研究中的「資訊不對稱」與「能力不對稱」相容：人與 AI 未必在相同技能上競爭，而可能因擁有不同資訊與能力來源而形成互補。[2]

---

## 4. AI 也在替人類壓縮搜尋空間

壓縮不是單向的。

假設人類面對：

$$
\Omega_H
$$

其中有一萬個可能方案。

AI 可以先完成：

- 搜尋；
- 聚類；
- 去除明顯不可能方案；
- 建立比較；
- 發現相似案例；
- 形成候選 shortlist。

最後交給人類：

$$
\Omega_H'
\subset
\Omega_H
$$

例如：

$$
|\Omega_H|=10^4
$$

但 AI 先壓縮成：

$$
|\Omega_H'|=8
$$

人類真正需要投入高成本判斷的，只剩 8 個。

因此人機協作不是：

$$
Human+AI
$$

簡單相加。

更準確的是：

$$
H:\Omega_A\rightarrow\Omega_A'
$$

$$
A:\Omega_H\rightarrow\Omega_H'
$$

雙方互相裁剪對方需要搜索的空間。

---

## 5. 協作搜尋空間壓縮 CSSC

本文定義「協作搜尋空間壓縮（Collaborative Search-Space Compression, CSSC）」：

> 兩個或多個異質智能體透過交換約束、候選、證據、否決、歷史與模型，使任務的有效候選空間相對於各自獨立處理時持續縮小的過程。

若任務初始有效空間大小為：

$$
|\Omega_0|
$$

合作 $t$ 輪後為：

$$
|\Omega_t|
$$

可定義一個簡化的空間壓縮率：

$$
\rho_t
=
1-
\frac{|\Omega_t|}{|\Omega_0|}
$$

若：

$$
\rho_t\rightarrow1
$$

代表候選集合被大幅裁剪。

但很多實際任務無法枚舉 $|\Omega|$ ，因此更一般地，可以使用條件熵表示：

$$
H(X\mid K_t)
$$

其中 $X$ 是未知正確行動或解， $K_t$ 是截至時間 $t$ 的共享知識。

有效合作的理想方向是：

$$
H(X\mid K_{t+1})
<
H(X\mid K_t)
$$

也就是共享知識增加後，對「接下來應該做什麼」的不確定性下降。

---

## 6. 溝通不是免費的：真正要最小化的是總成本

這裡有一個常見誤區。

若只看 token，可能認為：

$$
C_{\text{communication}}>0
$$

所以溝通越多越差。

但真正的成本函數應包含：

$$
C_{\text{total}}
=
C_{\text{communication}}
+
C_{\text{search}}
+
C_{\text{verification}}
+
C_{\text{rework}}
+
C_{\text{failure}}
$$

如果增加 500 token 的澄清，能避免 20,000 token 的錯誤搜尋、重寫與驗證，那麼：

$$
\Delta C_{\text{communication}}>0
$$

但：

$$
\Delta C_{\text{total}}<0
$$

因此合作是否值得的基本條件可寫為：

$$
\boxed{
C_{\text{saved-search}}
+
C_{\text{saved-verify}}
+
C_{\text{saved-rework}}
>
C_{\text{communication}}
}
$$

這就是為什麼「先溝通清楚」有時反而是更便宜的計算策略。

---

## 7. HACAL 的真正效果：歷史把未來任務預先壓縮

第 02 篇 HACAL 最重要的一個結果，是雙方不只完成任務，還會形成共同協議。

第一次人類可能需要說：

> 這些理論版本雖然重複，但保留演化路徑，不要直接刪；如果真的要整理，只建立 canonical link。

第十次可能只需要：

> 按演化型整理。

若 AI 已經從共同歷史中重建完整規則，則一段長約束被壓縮成一個共享符號：

$$
L_{\text{instruction}}^{(t+1)}
<
L_{\text{instruction}}^{(t)}
$$

更深一層，這不是單純語句變短，而是：

$$
\Omega_{t+1}^{\text{start}}
\subset
\Omega_t^{\text{start}}
$$

下一次任務一開始就不必重新探索以前已被否決的路徑。

因此長期記憶的價值可以寫成：

$$
M_t
:\
\Omega_0
\rightarrow
\Omega(M_t)
$$

其中：

$$
|\Omega(M_t)|\ll|\Omega_0|
$$

這就是本文稱的：

### 歷史搜尋壓縮（Historical Search Compression）

過去的成功、失敗、拒絕與修正，被編譯成未來的起始條件。

---

## 8. HACT：合作軌跡是「剪枝規則的來源庫」

第 03 篇提出 HACT：

$$
\tau
=
(S_0,e_1,e_2,\ldots,e_n,S_n)
$$

本文重新解讀其中的 correction、rejection、rollback。

它們其實在告訴系統：

$$
\text{This branch should not be explored again under similar conditions.}
$$

例如：

$$
(S,a)\rightarrow Failure
$$

若被抽象成：

$$
Rule(S'):\neg a
$$

那麼下一次遇到相似 $S'$ ，Agent 可以提前剪枝。

這表示一條合作軌跡的長期價值，不只是訓練「哪一步對」，還包括形成：

$$
\boxed{
\text{Reusable Search Constraints}
}
$$

因此：

$$
HACT
\rightarrow
Memory
\rightarrow
Heuristic
\rightarrow
SearchCompression
$$

構成完整閉環。

---

## 9. 共享心智模型：壓縮依賴共同可預測性

人類團隊研究長期使用 Shared Mental Models（SMMs）描述成員對任務、環境與團隊結構具有足夠重疊的知識結構；人機團隊研究也已把 SMM 引入 human–AI teaming。[3]

2025 年的研究進一步強調，不應把人類決策者視為固定不變；人類對 AI、任務與彼此互補關係的 mental model 會在持續互動中演化。[4]

因此合作壓縮不是單純把資訊塞進 memory。

真正需要的是：

$$
Predict_H(A\mid S)
$$

與：

$$
Predict_A(H\mid S)
$$

都逐漸提高。

也就是雙方更能預測：

> 對方看到這個狀態會怎麼理解？

> 哪些事情對方會拒絕？

> 哪裡需要解釋？

> 哪些步驟可以省略？

如果共同可預測性提升，就不必每次把全部背景重新傳送。

這可以視為：

$$
C_{\text{coordination}}(t+1)
<
C_{\text{coordination}}(t)
$$

在任務分布相對穩定的前提下成立。

---

## 10. 不只是共享「答案」，而是共享搜尋策略

人機合作的一個低階版本是：

$$
AI\rightarrow Answer\rightarrow Human
$$

但更成熟的合作是雙方共享：

- 哪些區域值得探索；
- 哪些區域應避免；
- 哪些訊號表示風險；
- 哪些候選需要人類判斷；
- 哪些可交給 AI 批量處理；
- 何時應停止搜尋；
- 何時應向外部求援。

因此共享的不是單一解：

$$
y^*
$$

而是搜尋策略：

$$
\pi_{search}
$$

這是很大的差異。

若只有答案，下一題重新開始。

若有搜尋策略與歷史規則：

$$
T_1\rightarrow\pi_1
$$

$$
T_2\rightarrow\pi_2=f(\pi_1,\Delta_2)
$$

就開始產生持續性。

---

## 11. 驗證空間也可以被壓縮

上一篇談到 Agent Verification Inversion：

$$
C_{\text{verify}}>C_{\text{generate}}
$$

但人機共同歷史也能縮小需要驗證的區域。

假設 Agent 修改 1,000 個檔案，人類不可能逐一檢查。

若系統能將它們分成：

$$
A_{safe}
$$

$$
A_{changed-policy}
$$

$$
A_{irreversible}
$$

$$
A_{uncertain}
$$

那人類只需要集中在：

$$
V^*
=
A_{changed-policy}
\cup
A_{irreversible}
\cup
A_{uncertain}
$$

而不是：

$$
V=A_{all}
$$

所以：

$$
|V^*|\ll|V|
$$

本文稱之為：

### 驗證空間壓縮（Verification-Space Compression）

這也是後面「外部性有界智能體自治」的重要前置條件。

真正可擴展的治理不能靠人類查看所有行動，而必須找到少數真正值得檢查的邊界事件。

---

## 12. AI 直接給答案，有時反而會破壞長期壓縮能力

這裡有一個反直覺結果。

2025 年一項 human–AI team 實驗比較了不同 AI 資訊分享策略：直接提供中斷問題答案的團隊能更快克服當下問題；但讓 AI 幫助人類自己找到答案的條件，則出現更多行動溝通、更高的共享心智模型感知與更好的情境知覺。[5]

這指出：

$$
\text{Immediate Performance}
\neq
\text{Long-Term Team Development}
$$

若 AI 永遠直接輸出結果，人類可能沒有機會建立：

$$
\pi_H
$$

也沒有形成與 AI 的共同搜尋規則。

所以某些情況下，最佳策略不是：

$$
\text{Give Answer Immediately}
$$

而是：

$$
\text{Reduce the Human's Search Space Enough}
$$

讓人類仍保留必要判斷。

這對未來「老師型雲端 AI」尤其重要。

---

## 13. 分散式認知：搜尋本來就可以跨越單一個體

Distributed Cognition 傳統早已指出，認知活動不一定只存在單一個體內，而可能分布於人、工具、表示系統與環境之間。[6]

本文的 Human–Agent system 可以因此寫成：

$$
\mathcal C_t
=
(H_t,A_t,M_t,E_t)
$$

其中：

- $H_t$ ：人類當前知識與策略；
- $A_t$ ：AI 當前能力與 policy；
- $M_t$ ：共同記憶與歷史；
- $E_t$ ：工具、文件與環境狀態。

真正執行搜尋的不是：

$$
H
$$

或：

$$
A
$$

單獨一個，而可能是整個：

$$
\boxed{
\mathcal C_t
}
$$

這也是為什麼單純比較「人類 IQ」與「模型 benchmark」不能完整描述這類系統的有效能力。

---

## 14. 協作壓縮的真正性能指標

若要把 CSSC 變成可實驗方法，可以追蹤至少以下量：

### 14.1 起始搜尋空間代理值

例如候選方案數、工具路徑數、文件候選集合或 planning branches：

$$
N_0
$$

### 14.2 最終有效候選

$$
N_f
$$

### 14.3 溝通成本

$$
C_{comm}
$$

可用 token、輪數、時間或人工操作數近似。

### 14.4 搜尋成本

$$
C_{search}
$$

### 14.5 驗證成本

$$
C_{verify}
$$

### 14.6 重工成本

$$
C_{rework}
$$

### 14.7 歷史再利用率

設本輪使用的有效決策規則中，由過往合作歷史直接提供的比例為：

$$
R_{history}
$$

則長期系統真正應觀察：

$$
\frac{dC_{total}}{dt}
$$

是否隨共同歷史增加而下降。

如果：

$$
\frac{dC_{total}}{dt}<0
$$

而任務品質不下降，才能說系統真的在「學會合作」。

---

## 15. 壓縮不是越多越好：過度壓縮問題

任何搜尋空間壓縮都有風險。

若錯誤規則被寫入長期記憶：

$$
WrongRule
\rightarrow
PermanentPruning
$$

那麼真正正確的路徑可能永遠不再被探索。

因此：

$$
\Omega_{t+1}\subset\Omega_t
$$

不必然是好事。

可能存在：

### 15.1 Shared False Assumption

人與 AI 共同相信錯誤前提。

### 15.2 Memory Anchoring

舊經驗過度限制新任務。

### 15.3 Preference Overfitting

Agent 把某次局部偏好誤當永久規則。

### 15.4 Protocol Ossification

共享縮寫與舊工作流逐漸僵化。

### 15.5 Novelty Suppression

過去有效的剪枝把真正創新的異常候選排除掉。

因此成熟系統必須保留：

$$
P_{explore}>0
$$

也就是一定程度的重新探索能力。

可表示為：

$$
\Omega_t^{effective}
=
\Omega_t^{compressed}
\cup
\epsilon\Omega_0
$$

其中 $\epsilon$ 代表保留的小比例探索空間。

這和 reinforcement learning 中 exploration 的直覺相似，但此處針對的是共享合作規則的僵化問題。

---

## 16. 壓縮必須具有可逆性與來源

因此每一條高強度剪枝規則最好附帶：

$$
Rule_i
=
(
content,
source,
confidence,
scope,
createdAt,
lastValidated
)
$$

例如：

> 不刪除理論歷史版本。

不能只保存字串。

還要知道：

- 這是誰提出？
- 適用哪些資料庫？
- 是永久原則還是一次性決定？
- 最後何時重新驗證？
- 是否允許 Agent 挑戰？

因此搜尋壓縮不是不可逆刪除候選，而更接近：

$$
\boxed{
\text{Weighted Suppression rather than Blind Erasure}
}
$$

即：降低某些路徑優先級，而不是把它們從宇宙中永久抹除。

---

## 17. 從單輪合作到「認知編譯」

若每一次互動都只是聊天：

$$
Conversation_t\rightarrow End
$$

則下一次仍須重新構造背景。

但如果合作歷史被編譯：

$$
\tau_{1:t}
\rightarrow
M_t
\rightarrow
H_t
\rightarrow
\pi_t
$$

則大量過往資料被轉化為：

- shared vocabulary；
- decision rules；
- risk boundaries；
- canonical structures；
- preferred tools；
- known failure patterns；
- verification priorities。

因此可以把這個過程稱為：

### 協作認知編譯（Collaborative Cognitive Compilation）

其效果是把昂貴歷史：

$$
\tau_{1:t}
$$

壓縮成未來可快速使用的：

$$
K_t^*
$$

使：

$$
C_{retrieve}(K_t^*)
\ll
C_{replay}(\tau_{1:t})
$$

這也直接連接到系列後續的持續計算環境與長期記憶問題。

---

## 18. P/NP 認知類比在這裡真正有用的地方

經過以上區分後，本文使用 P/NP 類比真正想表達的是三件事。

第一：

$$
\text{Search Cost}
\neq
\text{Verification Cost}
$$

第二：

一個智能體提供 candidate，可以把另一個智能體從：

$$
\text{Generate from scratch}
$$

轉成：

$$
\text{Verify / refine candidate}
$$

第三：

長期合作還會進一步改變下一次搜尋的起始空間：

$$
\Omega_0
\rightarrow
\Omega_1
\rightarrow
\cdots
\rightarrow
\Omega_t
$$

因此我們研究的不再只是：

> 誰比較會解題？

而是：

> **智能體之間如何透過候選、證據、否決與歷史，使彼此不需要再解同一個巨大搜尋問題？**

這才是「P/NP—認知」在本系列中的方法論價值。

---

## 19. 從本篇通往持續計算環境

到目前為止，HACAL 與 CSSC 還可以只存在聊天系統中。

但它很快會遇到一個限制：

如果每次 session 結束，環境、工具、檔案結構與實際歷史都重新初始化，那麼：

$$
M_t
$$

只能保存抽象描述，無法完整保存真正的世界狀態。

因此下一步自然是：

$$
\boxed{
\text{Persistent Memory}
+
\text{Persistent Environment}
}
$$

如果 Agent 有一台持續存在的計算機，昨天建立的索引、今天修改的 script、以前踩過的錯誤、形成的資料夾結構、建立的 recovery policy 都可以直接成為：

$$
K_{t+1}
$$

而不用每次重新用語言描述。

這正是下一篇要進入的命題：

> **不是 Agent 使用一台臨時電腦，而是 Agent 擁有一個持續存在的計算環境。**

---

## 20. 結論

本文把前三篇的「驗證反轉—共適應學習—合作軌跡」接回 P/NP—認知研究線，並提出協作搜尋空間壓縮 CSSC。

其核心不是宣稱人機合作改變正式計算複雜度，而是指出：在真實任務中，人類與 AI 可以透過交換不同種類的資訊，使彼此實際需要搜尋、比較與驗證的候選集合縮小。

因此：

$$
\boxed{
\text{Communication}
\neq
\text{Pure Overhead}
}
$$

在好的協作架構下：

$$
\boxed{
\text{Communication}
=
\text{Search-Space Transformation}
}
$$

而長期記憶使這種轉換不必每次重新發生：

$$
\boxed{
\text{History}
\rightarrow
\text{Constraints}
\rightarrow
\text{Heuristics}
\rightarrow
\text{Smaller Future Search Space}
}
$$

所以真正成熟的人機協作，不只是：

$$
Human+AI\rightarrow BetterAnswer
$$

而更接近：

$$
\boxed{
(H_t,A_t,M_t)
\rightarrow
\Omega_{t+1}^{smaller}
\rightarrow
LowerFutureCost
}
$$

這也完成本系列第一部的核心轉換：從「Agent 能不能做」，一路推到「人與 Agent 是否能共同形成一個越來越少走冤路的認知系統」。

下一部將把這個共同認知系統放進真正持續存在的計算世界中。

---

## 參考資料

[1] Clay Mathematics Institute, **P vs NP**, Millennium Prize Problems.  
https://www.claymath.org/millennium/p-vs-np/

[2] Hemmer, P., Schemmer, M., Kühl, N., Vössing, M., & Satzger, G., **Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence**, European Journal of Information Systems / preprint version, 2024–2025.  
https://www.tandfonline.com/doi/full/10.1080/0960085X.2025.2475962

[3] Andrews, R. W., Lilly, J. M., Srivastava, D., & Feigh, K. M., **The role of shared mental models in human-AI teams: a theoretical review**, Theoretical Issues in Ergonomics Science, 2023.  
https://www.tandfonline.com/doi/abs/10.1080/1463922X.2022.2061080

[4] Holstein, J., & Satzger, G., **Development of Mental Models in Human-AI Collaboration: A Conceptual Framework**, arXiv, 2025.  
https://arxiv.org/abs/2510.08104

[5] **Should AI Teammates Give All the Answers? Examining the Role of Different AI Information-Sharing Techniques on Team Cognition in Human-AI Teams**, International Journal of Human–Computer Interaction, 2025.  
https://www.tandfonline.com/doi/full/10.1080/10447318.2025.2528988

[6] Hutchins, E.; Hollan, J. D.; Kirsh, D., **Distributed Cognition: Toward a New Foundation for Human-Computer Interaction Research**, ACM Transactions on Computer-Human Interaction, 2000; research overview maintained by Edwin Hutchins.  
https://pages.ucsd.edu/~ehutchins/research.html

---

## 與系列的依賴關係

**前置依賴：**

- 01〈從可完成到可委託：智能體自治中的驗證反轉〉
- 02〈人機智能體共適應學習：意圖、溝通、修正與長期共同適應〉
- 03〈合作軌跡作為訓練資料：從 QA 樣本到意圖—行動—修正歷史〉
- 既有 P/NP—認知研究線

**本文新增：**

- Collaborative Search-Space Compression（CSSC）
- Historical Search Compression
- Verification-Space Compression
- Collaborative Cognitive Compilation
- Total Collaboration Cost
- Overcompression / Permanent-Pruning Risk

**後續輸出：**

- 05〈計算機作為持續智能環境：不是 Agent 用電腦，而是 Agent 有電腦〉

