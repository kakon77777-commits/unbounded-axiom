# 從 HLE 到 ARC-AGI：AI 能力前沿為何正在從答案移向問題

**系列：** 最後人類認知前沿（Last Human Cognitive Frontier, LHCF）  
**篇次：** 02 / 12  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Thinking）  
**版本：** v0.1  
**日期：** 2026-08-02

---

## 摘要

人工智慧評測正在發生一個結構性轉變。早期與中期大型語言模型 benchmark 主要評估既有知識、封閉問題與標準化推理；隨著模型在 MMLU、GSM8K、MATH 等傳統測試上逐步逼近飽和，評測開始向更高階的專家知識、原創問題、長時程任務、陌生環境適應與研究活動遷移。GPQA 將問題推向「Google-proof」的博士級專業問答；FrontierMath 使用未公開、由專家設計、需要數小時乃至數日解決的數學問題；Humanity’s Last Exam（HLE）進一步建立跨學科、專家級、封閉答案的「人類知識前沿」測試；FrontierScience、RE-Bench 與 METR task-completion time horizon 將評測推向研究子任務、研究工程與長時程工作；ARC-AGI-3 則把核心從「回答一個已定義問題」轉向「在沒有明確指令時探索、推斷目標、建立世界模型並選擇行動」。2026 年的 FrontierMath Open Problems、FrontierCS、ProjectionBench、HypoBench 與 SDABench 又進一步把評測推向未解問題、開放式最優化、假說生成與機制推理。

本文主張，這些 benchmark 並非彼此孤立，而可以被理解為一條「評測對象上移」的連續譜：從答案空間中的選擇，逐步轉向問題空間、目標空間與框架空間中的生成。本文提出 Answer–Problem Frontier Shift（APFS，答案—問題前沿轉移）框架，將 AI 能力評測劃分為七級：知識回憶、封閉推理、專家封閉問題、研究型開放問題、陌生目標發現、假說／問題生成與框架重構。本文進一步指出：當較低層級逐步飽和時，真正具有區辨力的 AI 評測必須上移到「誰定義問題」「誰選擇值得研究的方向」「誰能重新建構問題表示」等元層級。這一轉移構成 LHCF 的前置條件：只有當 AI 評測從答案轉向問題，我們才有可能測量哪些人類仍能形成最後認知前沿。

**關鍵詞：** Humanity’s Last Exam、ARC-AGI、FrontierMath、FrontierScience、AI benchmark、問題生成、目標發現、科學發現、認知前沿、LHCF

---

# 1. 前言：benchmark 的真正困境不是題目不夠難，而是題型正在失效

AI benchmark 經常被描述為一場「題目越出越難」的競賽：

$$
B_1 < B_2 < B_3 < \cdots
$$

其中 $B_i$ 表示第 $i$ 代 benchmark 的難度。

這個敘事只說對了一半。

如果問題只是「題目難度不足」，那麼最自然的做法永遠是增加更難的題目：

$$
Q \rightarrow Q^{+}.
$$

但近年 benchmark 的演化顯示，真正的問題不是只發生在難度軸，而是發生在**評測對象本身**。

當模型在傳統 benchmark 上迅速進步時，研究者開始發現：

> 即使我們能不斷提供更難的封閉問題，也不代表我們正在測量更一般的智能。

因此，新的評測逐步開始問：

- 模型能否在沒有明確規則時學習？
- 模型能否長時間維持任務？
- 模型能否在開放問題中改善解？
- 模型能否產生可信假說？
- 模型能否選擇有效的因果模型？
- 模型能否發現題目真正的目標？
- 模型能否生成原先不存在的問題表示？

這意味著評測正在由：

$$
\text{Answer Evaluation}
$$

轉向：

$$
\text{Problem-Space Evaluation}.
$$

本文把這種變化稱為：

$$
\boxed{
\text{Answer–Problem Frontier Shift, APFS}
}
$$

即「答案—問題前沿轉移」。

---

# 2. 第一階段：知識測驗——問題已知、答案已知、空間已知

傳統能力 benchmark 的理想形式近似：

$$
(Q,\mathcal A,y^*)
$$

其中：

- $Q$ ：題目；
- $\mathcal A$ ：可接受答案空間；
- $y^*$ ：標準答案或評分函數。

模型的任務只是：

$$
f(Q)\rightarrow \hat y
$$

並計算：

$$
S(\hat y,y^*).
$$

MMLU 是這一時期極具代表性的 benchmark。它覆蓋大量學科，曾經可以有效區分不同模型的知識與推理能力。但 HLE 的 Nature 論文指出，前沿 LLM 在 MMLU 等熱門 benchmark 上已能取得超過 $90\%$ 的準確率，因此其區辨力下降。[1]

這代表 benchmark 發生第一種飽和：

$$
\frac{\partial S}{\partial C_A}\rightarrow0,
$$

其中 $C_A$ 是模型能力。

當大量模型都集中於高分區間時：

$$
\operatorname{Var}(S)\downarrow.
$$

評測者於是必須尋找新的難度來源。

---

# 3. 第二階段：專家封閉問題——答案仍然存在，但只有專家能找到

GPQA 是重要轉折。

GPQA 由生物、物理與化學領域專家撰寫 448 道多選題。原始研究中，對應領域的博士或博士生約達到 $65\%$ 準確率，而高能力但非該領域專家的驗證者，即使能自由使用網路，仍僅約 $34\%$ 。[2]

這使題目從：

$$
\text{retrievable knowledge}
$$

轉向：

$$
\text{expert-localized reasoning}.
$$

然而其結構仍然屬於：

$$
Q\rightarrow A^*.
$$

AI 不必問：

> 這個問題值不值得研究？

也不必問：

> 題目是不是定義錯了？

更不需要自己產生問題。

它仍然是在一個人類已經建好的問題空間中競爭。

---

# 4. 第三階段：FrontierMath——把封閉問題推到研究級，但問題仍由人類完整定義

FrontierMath 代表另一種極端化。

它使用由專家數學家設計的原創問題，涵蓋現代數學多個分支；典型問題需要相關研究者花數小時，最難問題可能需要數日。[3]

形式仍然是：

$$
Q_{\text{expert}}
\rightarrow
A^*,
$$

但：

$$
C(Q_{\text{expert}})
\gg
C(Q_{\text{standard}}).
$$

也就是問題並沒有改變本體，只是把推理深度、專業知識、創造性與長鏈一致性大幅提高。

FrontierMath 的重要性在於，它首次非常清楚地暴露一個現象：

> 奧林匹克、考試與教科書級推理，不等於研究級數學推理。

更重要的是，2026 年 Epoch AI 又推出 FrontierMath: Open Problems，收錄專業數學家曾嘗試但尚未解決的研究問題，並要求候選解可以由程式化 verifier 檢驗。[4]

於是結構第一次從：

$$
Q\rightarrow A^*
$$

轉成：

$$
Q\rightarrow A^{?},
$$

其中：

$$
A^{?}
$$

在 benchmark 建立時甚至不存在。

這是一個非常重要的邊界。

---

# 5. HLE：封閉答案 benchmark 的「極限化」

Humanity’s Last Exam 在概念上非常誠實。

Nature 2026 版本包含 2,500 道跨數十領域的專家級題目，題目由全球領域專家撰寫，包含多選與短答，答案被要求明確、可驗證且不容易透過簡單網路檢索取得。[1]

因此 HLE 可以抽象為：

$$
\mathcal B_{\text{HLE}}
=
\{Q_i,A_i^*\}_{i=1}^{2500}.
$$

它試圖回答：

> 如果我們把「封閉式學術問題」推到目前人類知識前沿，AI 到底能走多遠？

這使 HLE 非常適合測量：

- 專業廣度；
- 跨領域知識；
- 封閉高難推理；
- 高階學術校準。

但 HLE 同時也清楚暴露了一個理論終點。

只要：

$$
A_i^*
$$

事先存在，AI 面臨的世界依然是一個「人類已經知道問題與答案」的世界。

因此：

$$
\text{HLE saturation}
$$

並不等價於：

$$
\text{scientific frontier saturation}.
$$

甚至 HLE 本身出現 HLE-Verified，也再次提醒 benchmark 的題目與標準答案本身可能存在誤差；高階評測不能假設人類提供的 evaluator 永遠正確。[5]

---

# 6. 第四階段：研究子任務——答案不再是單一字串

FrontierScience 把評測向研究活動推進一步。

其 Research track 由博士級科學家撰寫開放式研究子任務，並使用細粒度 rubric 評估模型在解決過程中的能力，而不只看最終答案。[6]

這使評測結構從：

$$
S(\hat y,y^*)
$$

變成：

$$
S(
r_1,
r_2,
\ldots,
r_k
),
$$

其中 $r_i$ 是研究過程中的不同能力維度。

例如：

- 問題理解；
- 理論推導；
- 假設選擇；
- 計算正確性；
- 證據連結；
- 結論合理性。

此時「答案」開始變成「研究軌跡」。

這是一個本體上的改變：

$$
\text{answer}
\rightarrow
\text{process}.
$$

---

# 7. RE-Bench 與 METR：從題目難度轉向「可以維持多久的有效工作」

RE-Bench 進一步把 AI 放入開放式機器學習研究工程環境，並直接比較 AI agent 與人類專家在不同時間預算下的表現。[7]

原始研究的一個重要發現是：

- 在短時間預算下，最佳 AI agent 可以明顯超過人類；
- 隨時間預算增加，人類的邊際收益曲線較好；
- 在總計 $32$ 小時預算比較中，人類分數約為最佳 AI agent 的兩倍。[7]

因此評測開始從：

$$
\text{Can you solve?}
$$

轉向：

$$
\text{How long can you keep producing useful progress?}
$$

METR 的 task-completion time horizon 將這個觀念形式化。它以「人類專家完成某任務通常需要的時間」作為難度尺度，再估計 AI 在不同任務長度下的成功率。[8]

定義：

$$
H_p(A)
=
\text{AI }A\text{ 在成功率 }p\text{ 下可處理的任務人類工時尺度}.
$$

這個框架的重要貢獻是：

> 難度不再只是題目的抽象分數，而開始被映射到真實工作的時間結構。

但 METR 也明確提醒：

$$
H_p(A)
\neq
\text{AI 可自主運作的真實時間}.
$$

其 task suite 主要集中於軟體工程、機器學習與資安，而且超過一定時長後目前估計的不確定性會明顯增加。[8]

這再次說明：

$$
\text{benchmark competence}
\neq
\text{general cognition}.
$$

---

# 8. ARC-AGI-3：真正重要的轉折——題目連目標都不完全告訴你

ARC-AGI-3 是本文認為最接近 APFS 關鍵轉折的 benchmark。

其互動環境不提供完整操作說明；智能體必須：

1. 探索；
2. 推斷目標；
3. 建立環境動力學模型；
4. 測試假說；
5. 規劃行動；
6. 根據回饋修正。

因此 agent 並不是接收：

$$
Q
$$

然後回答：

$$
A.
$$

其實際過程更接近：

$$
O_0
\rightarrow
a_1
\rightarrow
O_1
\rightarrow
a_2
\rightarrow
\cdots
$$

並由這些互動推斷：

$$
\hat G,
\hat M,
\hat \pi,
$$

其中：

- $\hat G$ ：推斷出的目標；
- $\hat M$ ：內部世界模型；
- $\hat \pi$ ：行動策略。

因此：

$$
\boxed{
\text{目標發現本身成為智能的一部分}
}
$$

ARC-AGI-3 的技術報告指出，截至 2026 年 3 月，人類測試者可以完成全部環境，而被測前沿 AI 系統得分低於 $1\%$ 。[9]

這裡最重要的不是百分比本身。

而是 benchmark 第一次把：

$$
G
$$

從 evaluator 提供的常量，變成 agent 必須推斷的潛在變量。

---

# 9. 從「問題已知」到「問題未知」：四個不同層級

可以將問題結構寫成四級。

## Level A：答案未知

$$
Q\text{ known},\qquad A\text{ unknown to agent}.
$$

傳統考試屬於此類。

## Level B：答案對人類也未知

$$
Q\text{ known},\qquad A\text{ unknown to both human and AI}.
$$

FrontierMath Open Problems 開始進入此類。[4]

## Level C：目標需要推斷

$$
Q_{\text{partial}},\qquad G\text{ latent}.
$$

ARC-AGI-3 屬於此類。[9]

## Level D：問題本身需要生成

$$
W
\rightarrow
Q^*.
$$

其中世界狀態 $W$ 已存在，但值得研究的問題 $Q^*$ 尚未被指定。

真正的科學研究大量發生在 Level D。

因為研究者首先面對的往往不是：

> 請解這一道題。

而是：

> 這堆異常資料到底值得問什麼？

---

# 10. HypoBench、ProjectionBench 與 SDABench：評測開始觸碰「問題生成」

HypoBench 專門測量 LLM 的 hypothesis generation，評估假說的實用性、泛化能力與發現率。其合成資料實驗顯示，即使模型可以產生有效且新穎的模式，當任務難度提高時，仍無法完整恢復所有相關 ground-truth hypotheses。[10]

這使問題從：

$$
Q\rightarrow A
$$

移向：

$$
D\rightarrow H_1,H_2,\ldots,H_n,
$$

其中 $D$ 是資料， $H_i$ 是候選假說。

ProjectionBench 更進一步。

它讓模型最初只取得近期論文的研究主題與研究問題，再逐步揭露技術細節；模型必須在不同資訊量下生成假說，藉此區分：

$$
\text{innovative projection}
$$

與：

$$
\text{grounded reconstruction}.
$$

換句話說，它開始測：

> 當你不知道原作者最後得到什麼結論時，你能不能自己走到一個有價值的方向？[11]

SDABench 則將科學資料分析拆成：

$$
\text{descriptive}
\rightarrow
\text{exploratory}
\rightarrow
\text{inferential}
\rightarrow
\text{predictive}
\rightarrow
\text{causal}
\rightarrow
\text{mechanistic}.
$$

其 2026 年結果顯示，模型在描述性分析上較強，但進入假設選擇、潛在過程建模與機制推理後，能力顯著下降。[12]

因此現有評測已經顯示：

$$
\text{description}
<
\text{causation}
<
\text{mechanism}
$$

可能是不同認知層級，而不能只用單一「科學能力」分數代表。

---

# 11. FrontierCS：一個非常重要但容易忽略的中間形態

FrontierCS 提供了一個介於「有答案」與「完全開放研究」之間的有趣結構。

它包含專家設計的開放式電腦科學問題，其中最佳解未知，但候選方案品質可以由 evaluator 客觀測量。[13]

因此：

$$
A^*=\text{unknown},
$$

但：

$$
S(A)
$$

仍然可計算。

這個設計非常重要。

因為很多真實世界問題都不是：

$$
A=A^*
$$

而是：

$$
\max_A S(A).
$$

例如：

- 新演算法；
- 系統設計；
- 壓縮方法；
- 調度策略；
- 架構最佳化；
- 實驗方案。

因此未來的前沿 benchmark 不一定需要知道終極答案。

它只需要：

$$
\text{objective progress signal}.
$$

這可能是從 benchmark 走向真正研究的一座橋。

---

# 12. APFS 七級模型

綜合以上 benchmark 演化，本文提出七級 Answer–Problem Frontier Shift。

## APFS-0：知識回憶

$$
Q\rightarrow A^*.
$$

主要要求已有知識的提取。

---

## APFS-1：封閉推理

$$
Q+\text{reasoning}\rightarrow A^*.
$$

答案已知，但需要多步推理。

---

## APFS-2：專家封閉問題

$$
Q_{\text{expert}}\rightarrow A^*.
$$

需要高專業知識與研究級推理，但仍具有明確答案。

代表：

- GPQA；
- HLE；
- FrontierMath Tiers 1–4。

---

## APFS-3：開放式研究問題

$$
Q\rightarrow\{A_i\},
$$

且：

$$
\max_i S(A_i)
$$

才是主要目標。

代表：

- RE-Bench；
- FrontierScience Research；
- FrontierCS；
- 部分 FrontierMath Open Problems。

---

## APFS-4：目標發現

$$
O_{0:t}\rightarrow \hat G.
$$

agent 必須先理解自己究竟要做什麼。

代表：

- ARC-AGI-3。

---

## APFS-5：問題／假說生成

$$
D,W\rightarrow\{Q_i,H_i\}.
$$

AI 必須從資料、異常或世界狀態中產生值得驗證的新問題與假說。

代表：

- HypoBench；
- ProjectionBench；
- 部分 AI Scientist benchmark。

---

## APFS-6：框架重構

$$
(W,Q,\mathcal R)
\rightarrow
(W',Q',\mathcal R'),
$$

其中：

- $W$ ：原問題世界；
- $Q$ ：原問題；
- $\mathcal R$ ：原表示系統；
- $W',Q',\mathcal R'$ ：重構後的問題與表示。

此時 AI 不再只是產生：

$$
Q_2
$$

而可能宣告：

> $Q_1$ 本身是在錯誤座標系中提出的。

這正是 LHCF 真正關心的晚期能力。

---

# 13. benchmark 的「階梯失效定律」

本文提出一個工作假說：

## 階梯失效定律

若某種能力 $C_k$ 被廣泛掌握，則主要依賴 $C_k$ 的 benchmark 區辨力將下降，評測必須向更高階能力 $C_{k+1}$ 遷移。

形式化為：

$$
\operatorname{Disc}(B_k,A_t)
\downarrow
\quad\Rightarrow\quad
B_{k+1}
=
\Psi(B_k,C_{k+1}).
$$

其中：

$$
\operatorname{Disc}
$$

表示 benchmark 對前沿模型的區辨力。

因此 benchmark 的歷史不是單純：

$$
\text{easy}
\rightarrow
\text{hard}.
$$

而更接近：

$$
\boxed{
\text{answer}
\rightarrow
\text{process}
\rightarrow
\text{goal}
\rightarrow
\text{problem}
\rightarrow
\text{frame}.
}
$$

這是一種測量本體的上移。

---

# 14. 為什麼「問題生成」可能比「答案生成」晚飽和？

這不是本文預設為真，而是一個需要實證測試的假說。

設：

$$
C_A
$$

表示答案求解能力，

$$
C_Q
$$

表示有效問題生成能力。

若：

$$
\frac{dC_A}{dt}
>
\frac{dC_Q}{dt},
$$

則在某段時期會形成：

$$
C_A\gg C_Q.
$$

這時 AI 很擅長回答人類給的問題，但較不擅長自己發現值得問的問題。

原因可能包括：

### 14.1 評分訊號差異

答案通常容易被評分：

$$
S_A\in\{0,1\}
$$

或有明確 verifier。

問題品質則常需要延遲驗證：

$$
S_Q(t+\Delta t).
$$

一個問題是否重要，可能多年後才知道。

### 14.2 搜索空間更大

答案搜索是在：

$$
\mathcal A(Q)
$$

中搜索。

問題生成則是在：

$$
\mathcal Q(W)
$$

中搜索。

一般而言：

$$
|\mathcal Q(W)|
\gg
|\mathcal A(Q)|.
$$

### 14.3 價值函數不明確

什麼叫「好問題」？

可能同時涉及：

- 新穎；
- 可解；
- 有影響；
- 可驗證；
- 能產生新理論；
- 能改變既有模型。

因此：

$$
V(Q)
$$

本身就是研究問題。

---

# 15. 從 benchmark 到 LHCF：人類最後前沿真正可能出現在哪裡？

如果 APFS 成立，那麼「最後人類認知前沿」的候選位置不太可能長期停留在：

$$
\text{APFS-0}
$$

或：

$$
\text{APFS-1}.
$$

因為這些能力最容易被大量資料、推理擴展與工具使用壓縮。

前沿更可能逐步移向：

$$
\text{APFS-4}
\rightarrow
\text{APFS-5}
\rightarrow
\text{APFS-6}.
$$

也就是：

> 人類剩餘認知價值，可能逐漸從「知道答案」轉向「知道要問什麼」，再轉向「知道為什麼這個問題應該換一種形式存在」。

這不表示人類必然會保有這些能力。

真正的 LHCF 問題是：

$$
\tau_4,\tau_5,\tau_6
$$

是否存在顯著差異。

若：

$$
\tau_6\gg\tau_2,
$$

則框架生成可能形成較長的人類殘留窗口。

若：

$$
\tau_6\approx\tau_2,
$$

則所謂「問題生成是人類最後堡壘」可能只是浪漫想像。

因此這是一個可以被未來數據推翻的命題。

---

# 16. 一個更重要的轉折：benchmark 可能最終不能由人類單方面出題

當 AI 能力足夠高，可能出現一個評測悖論。

如果：

$$
A_t
$$

已經超越人類在某領域的完整能力，那麼：

$$
H
$$

如何持續設計：

$$
Q>A_t
$$

？

這就是 benchmark generation ceiling。

傳統模式：

$$
H\rightarrow Q\rightarrow A
$$

可能失效。

未來 benchmark 可能必須變成：

$$
H+A_i
\rightarrow
Q
\rightarrow
A_j,
$$

甚至：

$$
A_i
\rightarrow
Q
\rightarrow
A_j.
$$

而人類主要負責：

- 確認問題有意義；
- 確認 verifier 沒有漏洞；
- 控制評測治理；
- 判斷現實影響。

這與 FrontierMath Open Problems、living benchmarks 與自動從新研究文獻產生題目的 EternalMath 已經有早期相似性。[4][14]

因此 benchmark 本身也可能進入「人機共同生成前沿」。

---

# 17. 與 EveMissLab 既有「問題空間」線的關係

在 EveMissLab 既有資料庫中，已有多條研究線將「智能」從單純輸出答案，推向問題空間、語言生成與認知導航。例如《程式語言 MWC 的三態演化路徑：從人類編碼到問題空間導航》已直接把「問題空間導航」作為演化方向之一。其存在顯示，LHCF 並非首次使用問題空間作為智能分析單位，而是把既有問題空間觀點與外部 benchmark 演化接合起來。

在 LHCF 中，這個概念可以被更嚴格地寫成：

$$
\Pi_Q:
W
\rightarrow
\mathcal Q(W),
$$

其中 $\Pi_Q$ 是問題生成算子。

更高階則是：

$$
\Pi_F:
(W,\mathcal Q,\mathcal R)
\rightarrow
(W',\mathcal Q',\mathcal R'),
$$

即框架生成算子。

未來第 8 篇將專門處理這個部分。

---

# 18. 可驗證預測

APFS 至少提出以下五個可觀測預測。

## 預測一

當某一封閉 benchmark 趨近飽和時，新 benchmark 的主要創新將越來越不是「更難答案」，而是改變任務結構。

$$
S_{\text{closed}}\uparrow
\Rightarrow
P(\text{open/interactive benchmark})\uparrow.
$$

---

## 預測二

AI 在 APFS 不同層級上的能力不會同步。

可能存在：

$$
C_2\gg C_4,
$$

或：

$$
C_3\gg C_5.
$$

ARC-AGI-3 與 SDABench 目前正提供這類 jaggedness 的早期證據。[9][12]

---

## 預測三

當前沿模型逐步跨越 APFS-2，研究社群將更多轉向：

- open-ended;
- interactive;
- long-horizon;
- hypothesis-generating;
- mechanistic;
- unsolved-problem

型 benchmark。

2025–2026 的 FrontierScience、FrontierCS、ProjectionBench 與 FrontierMath Open Problems 已呈現此方向。[4][6][11][13]

---

## 預測四

未來最難 benchmark 的 evaluator 本身會成為瓶頸：

$$
C_{\text{generator}}
>
C_{\text{evaluator}}.
$$

也就是 AI 能產生人類難以評估的候選理論、證明或研究方案。

此時 scalable oversight 與 machine-verifiable evaluation 將變得更加重要。

---

## 預測五

若未來 AI 同時在 APFS-5 與 APFS-6 達到高穩定能力，則 LHCF 中「人類作為問題生成者」的剩餘前沿會快速收縮。

因此：

$$
\text{Problem Generation Superiority}
$$

不能被預設為人類永久優勢。

---

# 19. 對「AGI benchmark」概念的修正

本文認為不存在單一 benchmark 能充分證明 AGI。

因為：

$$
\operatorname{Score}(A,B)
$$

永遠只是：

$$
A
$$

與 benchmark $B$ 所定義能力切片的關係。

當 benchmark 的問題結構固定時：

$$
B:
\mathcal X\rightarrow\mathcal Y,
$$

我們測量的只是該映射。

更一般的智能則可能需要：

$$
\mathcal X
\rightarrow
\mathcal Y
\rightarrow
\mathcal Q
\rightarrow
\mathcal G
\rightarrow
\mathcal R.
$$

即：

- 感知狀態；
- 產生答案；
- 發現問題；
- 建立目標；
- 改寫表示。

因此「最後一場考試」幾乎一定不會真的存在。

每當 AI 通過某一種考試，人類都會發現：

> 原來我們真正想測的不是這件事。

這不是 benchmark 設計失敗。

這本身就是智能概念被逐層揭露的過程。

---

# 20. 結論：真正的前沿不是最後一道題，而是最後一次由誰定義題目

從 MMLU、GPQA、FrontierMath、HLE，到 FrontierScience、RE-Bench、METR、ARC-AGI-3、HypoBench、ProjectionBench、SDABench、FrontierCS 與 FrontierMath Open Problems，我們可以看到一條逐漸清楚的歷史軌跡：

$$
\boxed{
\text{答案已知}
\rightarrow
\text{答案困難}
\rightarrow
\text{答案未知}
\rightarrow
\text{過程開放}
\rightarrow
\text{目標未知}
\rightarrow
\text{問題待生成}
\rightarrow
\text{框架待重構}
}
$$

因此 AI 能力前沿的真正轉移，不只是：

$$
\text{easier questions}
\rightarrow
\text{harder questions}.
$$

而是：

$$
\boxed{
\text{Answer Space}
\rightarrow
\text{Problem Space}
\rightarrow
\text{Frame Space}.
}
$$

這正是 LHCF 成立的前置條件。

因為當 AI 可以回答幾乎所有既有問題時，真正剩下的比較不再是：

> 誰答得比較快？

而是：

> 誰仍然可以產生值得另一個高階智能認真處理的新問題？

再往後則是：

> 誰可以發現原本的問題空間根本不夠？

因此「最後人類認知前沿」不應被想像成最後一道 ASI 解不出的考題。

它更可能是一條逐漸後退的界線：

$$
\boxed{
\text{最後一批仍能改變問題空間的人類認知活動。}
}
$$

下一篇將因此進入核心測量問題：

$$
\boxed{
\text{AI 吸收一個人類理論，到底什麼叫做「難」？}
}
$$

也就是 LHCF 第 3 篇的「認知阻抗」形式化。

---

# 參考文獻

[1] Center for AI Safety, Scale AI & HLE Contributors Consortium. **A benchmark of expert-level academic questions to assess AI capabilities.** Nature 649, 1139–1146, 2026.

[2] Rein, D. et al. **GPQA: A Graduate-Level Google-Proof Q&A Benchmark.** arXiv:2311.12022, 2023.

[3] Glazer, E. et al. **FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI.** arXiv:2411.04872, 2024.

[4] Epoch AI. **FrontierMath: Open Problems — Benchmarking AI on unsolved math problems.** 2026.

[5] Zhai, W. et al. **HLE-Verified: A Systematic Verification and Structured Revision of Humanity's Last Exam.** arXiv:2602.13964, 2026.

[6] Wang, M. et al. **FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks.** arXiv:2601.21165, 2026.

[7] Wijk, H. et al. **RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts.** ICML / PMLR 267, 2025.

[8] METR. **Task-Completion Time Horizons of Frontier AI Models.** Time Horizon 1.1, updated 2026-05-08.

[9] ARC Prize Foundation. **ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence.** arXiv:2603.24621, 2026.

[10] Liu, H. et al. **HypoBench: Towards Systematic and Principled Benchmarking for Hypothesis Generation.** arXiv:2504.11524, 2025.

[11] Lew, A. J., Cao, Y., Buehler, M. J. **ProjectionBench: Evaluating Scientific Hypothesis Generation in LLMs Under Progressive Information Disclosure.** arXiv:2605.30284, 2026.

[12] Shi, C. et al. **Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists.** arXiv:2607.11079, 2026.

[13] Mang, Q. et al. **FrontierCS: Evolving Challenges for Evolving Intelligence.** arXiv:2512.15699, 2025.

[14] Ma, J. et al. **EternalMath: A Living Benchmark of Frontier Mathematics that Evolves with Human Discovery.** arXiv:2601.01400, 2026.

[15] EveMissLab. **程式語言 MWC 的三態演化路徑：從人類編碼到問題空間導航.** Research manuscript.

---

## 版本註記

v0.1 為 LHCF 系列第 2 篇。本文的 APFS 七級模型是工作分類，不宣稱七級構成嚴格線性階層；後續可依 benchmark 實證資料將其改寫為偏序、圖結構或多軸能力空間。
