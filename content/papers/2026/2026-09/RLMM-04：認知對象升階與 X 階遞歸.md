# RLMM-04：認知對象升階與 X 階遞歸
## Cognitive Object Promotion and X-Order Recursion

**系列：Recursive Linguistic Metacognition Methodology（RLMM）／遞歸語言元認知方法論**  
**版本：v0.1**  
**日期：2026-08-20**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

RLMM-01 將語言定位為元認知介面；RLMM-02 建立認知操作的可組合性；RLMM-03 則說明成熟方法如何結晶成可重用元認知算子。當認知操作能被語言表示、組合與重新作為認知對象後，一個不可避免的問題出現：何時應該把目前處理的內容、方法、失敗模式、對手模型或方法論本身「升格」為下一階認知對象？

本文提出「認知對象升階（cognitive object promotion）」與「X 階遞歸（X-order recursion）」的第一版形式框架。本文主張，X 階認知不應被理解成單純的「想得更深」或「我知道你知道我知道」；更一般地，它是將上一階的認知產物、認知方法、失敗模型、選擇規則或交互模型重新對象化，並施加新的元認知操作。本文區分內容升階、方法升階、失敗模型升階、互動／對手模型升階與方法論升階五種路徑，並指出不同升階具有不同成本與失敗模式。

本文進一步提出「Promotion Gate」：只有當上一階認知對象存在可辨識的剩餘不確定性、重複失敗、方法依賴、交互反身性或結構性瓶頸，而且下一階分析預期能產生新的可操作區分時，才應升階。反之，如果新一階只是重述原有內容、重新命名同一問題、增加抽象層但不改變可行動決策，則應停止遞歸。本文最後提出「有界 X 階遞歸」模型與停止條件，將遞歸價值、認知成本、延遲、錯誤風險與行動需求納入統一判準。

核心結論是：元認知的成熟不在於無限升階，而在於能判斷**什麼值得升階、升到哪一層、以及什麼時候停止**。

---

## 關鍵詞

RLMM；X 階思維；認知對象升階；元認知；反身性；遞歸；停止條件；方法升階；失敗模型；對手模型

---

# 1. 問題：什麼叫做「升一階」？

「高階思維」、「元認知」、「二階思維」、「X 階思維」常被混用。

例如，下列句子都可能被稱為「更高階」：

- 我在分析問題。
- 我在分析自己的分析方法。
- 我在分析這個方法為什麼會失敗。
- 我在分析別人如何利用我已知的失敗模式。
- 我在分析自己對別人策略的建模是否可靠。
- 我在分析整套方法論是否會改變未來使用者的認知。

這些確實都有「往上」的味道，但若沒有明確定義，就很容易把任何更抽象、更長、更複雜的文字都叫做高階。

RLMM 因此提出：

> **升階不是增加抽象詞，而是改變認知對象。**

令：

$$
R^{(k)}
$$

表示第 $k$ 階認知中的主要對象。

則升階可以定義為：

$$
\boxed{
R^{(k+1)}
=
\mathcal M
\left(
R^{(k)}
\right)
}
$$

其中：

$$
\mathcal M
$$

不是單純「思考更多」，而是：

> **把上一階的認知產物、方法、失敗結構或交互模型重新變成新的可檢查對象。**

---

# 2. 零階：直接處理世界／問題

零階認知可以寫成：

$$
R^{(0)}=X
$$

其中 $X$ 是外部問題或當前任務。

例如：

- 一個數學命題；
- 一個程式 bug；
- 一個政策選擇；
- 一組證據；
- 一個遊戲系統；
- 一個語義結構；
- 一個工程需求。

零階操作是：

$$
O^{(0)}:
X
\rightarrow
Y.
$$

例如：

$$
\operatorname{Solve}(X)
=
Y.
$$

這仍然只是：

> 「解這個問題。」

它不需要對自己的解題方式進行明確分析。

---

# 3. 一階：方法成為認知對象

當認知主體開始問：

> 「我是怎麼得到這個答案的？」

或：

> 「這條推理依賴哪些方法？」

認知對象就從：

$$
X
$$

升為：

$$
M_X.
$$

其中 $M_X$ 是處理 $X$ 的方法。

因此：

$$
R^{(1)}
=
M(R^{(0)}).
$$

這是最常見的元認知形式。

例如：

$$
\operatorname{Solve}
\rightarrow
\operatorname{InspectSolveMethod}.
$$

此時分析的已經不是：

> 結果對不對？

而是：

> 產生結果的方法是什麼？

---

# 4. 二階：方法的失敗模型成為對象

若一階分析發現方法 $M$，下一個問題是：

> 這個方法什麼時候會失敗？

於是：

$$
R^{(2)}
=
F(M).
$$

其中 $F(M)$ 是方法的失敗模型。

例如：

- 過度依賴單一資料源；
- 對高信心共識過度信任；
- 不確定才查證，導致高信心錯誤太晚被發現；
- 只看局部 expected loss，導致永遠 defer；
- hard safety constraint 造成 over-rejection。

因此：

$$
\boxed{
\text{Method}
\rightarrow
\text{Failure Model of Method}
}
$$

是一個典型升階。

---

# 5. 三階：別人會如何利用我的失敗模型？

當方法失敗模式被公開或被內化後，環境也可能改變。

例如：

> 如果對手知道我會在高 uncertainty 時尋找獨立證據，他可以讓自己保持低 uncertainty 嗎？

於是認知對象從：

$$
F(M)
$$

變成：

$$
A(F(M)),
$$

其中 $A$ 是對手或環境對方法的反應模型。

這可寫成：

$$
R^{(3)}
=
\operatorname{OpponentResponse}
(
F(M)
).
$$

此時已經進入：

$$
\boxed{
\text{Reflexive Interaction}
}
$$

因為：

> 我的認知規則會改變對方行為，而對方行為又改變我的認知規則。

---

# 6. 四階：我對對方的模型可靠嗎？

再往上一階，問題變成：

> 我現在建立的對手模型，會不會自己是錯的？

因此：

$$
R^{(4)}
=
F
(
\operatorname{OpponentModel}
).
$$

例如：

- 我把對手分類成 slow-roll，但其實是 benign drift；
- 我把 false disagreement 當成 attack，但其實來源真的分裂；
- 我認為對方知道我的規則，但其實他根本不知道。

此時：

$$
\boxed{
\text{Model of opponent}
\rightarrow
\text{Failure model of opponent model}
}
$$

這種升階不是單純「更多猜測」，而是重新檢查自己建立的交互模型。

---

# 7. 更一般的 X 階形式

因此，X 階不應被限定為：

$$
\text{I know that you know that I know...}
$$

更一般地，可以定義：

$$
R^{(k+1)}
=
\mathcal M_k(R^{(k)})
$$

其中每個：

$$
\mathcal M_k
$$

可能不同。

例如：

$$
R^{(0)}
=
\text{Problem}
$$

$$
R^{(1)}
=
\text{Method}
$$

$$
R^{(2)}
=
\text{Failure Model}
$$

$$
R^{(3)}
=
\text{Opponent Model}
$$

$$
R^{(4)}
=
\text{Opponent-Model Failure}
$$

$$
R^{(5)}
=
\text{Governance of Model Revision}
$$

所以 X 階實際上是一條：

$$
\boxed{
\text{Object-Promotion Chain}
}
$$

而不是固定形式的 nested belief。

---

# 8. 五種主要升階類型

RLMM 建議至少區分五類升階。

---

## 8.1 Content Promotion

當前內容本身成為更高層結構。

例如：

$$
\text{facts}
\rightarrow
\text{pattern}
\rightarrow
\text{model}.
$$

---

## 8.2 Method Promotion

方法本身成為對象：

$$
\text{method use}
\rightarrow
\text{method inspection}.
$$

---

## 8.3 Failure Promotion

失敗不再只是結果，而被升格成結構：

$$
\text{failure}
\rightarrow
\text{failure archetype}.
$$

---

## 8.4 Interaction Promotion

考慮其他主體會如何回應自己的方法：

$$
\text{policy}
\rightarrow
\text{policy-in-interaction}.
$$

---

## 8.5 Methodology Promotion

整套方法論本身成為分析對象：

$$
\text{RLMM}
\rightarrow
\mathcal M(\text{RLMM}).
$$

這是最強的反身層。

---

# 9. 升階不是「換一個更抽象的名字」

必須防止 pseudo-promotion。

例如：

> 我在分析問題。

然後改寫為：

> 我在分析「問題分析系統」。

如果沒有新增：

- 新變數；
- 新失敗條件；
- 新決策；
- 新觀測；
- 新行動；

那只是：

$$
\boxed{
\text{Renaming}
\neq
\text{Promotion}.
}
$$

真正升階要求：

$$
\Delta \mathcal A_k>0
$$

其中：

$$
\mathcal A_k
$$

表示可操作區分的集合。

---

# 10. Promotion Gate：什麼情況值得升階？

本文提出第一版 Promotion Gate。

當前對象：

$$
R^{(k)}
$$

只有在至少一個條件成立時，才值得考慮升階。

---

## G1 — 重複失敗

若：

$$
F_t
\approx
F_{t-1}
\approx
F_{t-2}
$$

表示同一類失敗反覆出現。

此時：

$$
\boxed{
\text{Stop repeating the action; promote the method.}
}
$$

---

## G2 — 方法依賴過強

如果結果高度依賴：

$$
M
$$

但 $M$ 本身未被檢查，則方法需要升階。

---

## G3 — 結果衝突無法在內容層解決

若：

$$
C_1
\neq
C_2
$$

而更多內容證據仍無法區分，可能問題在：

- 表示；
- 方法；
- provenance；
- selection rule。

因此要升階。

---

## G4 — 環境對方法產生反身回應

若：

$$
Environment
=
f(Method),
$$

則不能再把環境視為固定。

此時需要 interaction promotion。

---

## G5 — 同一問題反覆被「安全解」但沒有被真正解決

例如：

$$
\text{uncertainty}
\rightarrow
\text{defer}
$$

反覆成功降低錯誤，但沒有提高自主 resolution。

此時：

$$
\text{objective / planner}
$$

本身要升階。

---

## G6 — 方法產生新的系統性副作用

例如：

$$
\text{hard autonomy}
\rightarrow
\text{over-rejection}.
$$

此時不是再「加更多 autonomy」，而是升階分析 constraint interaction。

---

# 11. 升階門檻：有必要，不代表值得

即使 Promotion Gate 被觸發，也不代表一定升階。

因為：

$$
\boxed{
\text{Need for meta-analysis}
\neq
\text{Net value of meta-analysis}.
}
$$

定義：

$$
V_k
=
\text{expected value of promoting to }k+1
$$

與：

$$
C_k
=
C_{\text{time}}
+
C_{\text{compute}}
+
C_{\text{complexity}}
+
C_{\text{delay}}
+
C_{\text{error}}.
$$

只有：

$$
\boxed{
V_k>C_k
}
$$

才真正升階。

---

# 12. 升階價值來自哪裡？

升階價值至少可能來自五種來源。

---

## 12.1 Error Reduction

$$
\Delta E<0.
$$

---

## 12.2 New Action Availability

原本沒有的選項出現：

$$
|\mathcal A_{k+1}|
>
|\mathcal A_k|.
$$

---

## 12.3 Better Distinction

原本不可區分的情況變得可區分。

---

## 12.4 Generalization

某個局部 failure 變成可重用 archetype。

---

## 12.5 Future Compression

高成本升階後，方法可能被結晶成 operator，降低未來成本。

---

# 13. 升階成本不只是計算量

常見直覺是：

> Meta-thinking 只是多花 token。

實際成本更廣。

可寫成：

$$
C_k
=
C_c
+
C_t
+
C_r
+
C_d
+
C_o.
$$

其中：

- $C_c$：compute；
- $C_t$：time；
- $C_r$：representation complexity；
- $C_d$：decision delay；
- $C_o$：opportunity cost。

對即時決策而言：

$$
C_d
$$

甚至可能是主要成本。

---

# 14. 遞歸深度不是能力排名

若兩個系統：

$$
A
$$

能做到 2 階，

$$
B
$$

能做到 5 階，

不代表：

$$
B>A.
$$

因為 B 可能：

- 多想但不行動；
- 反覆重新命名；
- 產生無效 meta-loop；
- 在高階失去基礎事實；
- 被延遲成本拖垮。

因此：

$$
\boxed{
\text{Maximum recursion depth}
\neq
\text{cognitive quality}.
}
$$

真正重要的是：

$$
\boxed{
\text{Adaptive recursion depth}.
}
$$

---

# 15. 無限元認知遞歸問題

若每一個認知操作都要求：

> 再檢查一次這個操作。

則：

$$
R^{(0)}
\rightarrow
R^{(1)}
\rightarrow
R^{(2)}
\rightarrow
\cdots
$$

可無限進行。

因此 RLMM 必須明確拒絕：

$$
\boxed{
\text{Unbounded Meta-Recursion}
}
$$

作為一般方法。

---

# 16. 停止條件

本文提出六類停止條件。

---

## S1 — No New Distinction

若：

$$
\mathcal A_{k+1}
=
\mathcal A_k
$$

或新一階沒有增加可操作區分，停止。

---

## S2 — Repetition

若新一階只是重述：

$$
R^{(k+1)}
\approx
R^{(k)},
$$

停止。

---

## S3 — Cost Dominance

若：

$$
V_k\le C_k,
$$

停止。

---

## S4 — Sufficient-for-Action

若當前認知品質已足以支持行動：

$$
Q(C_k)\ge Q_{\text{action}},
$$

停止。

---

## S5 — Budget Limit

若：

$$
B_{\text{meta}}=0,
$$

停止。

---

## S6 — External Irreducibility

若剩餘不確定性來自不可觀測世界，而非方法不足：

$$
\boxed{
\text{Stop reasoning; acknowledge irreducibility}.
}
$$

---

# 17. 有界 X 階遞歸

因此可以把 RLMM 的遞歸寫成：

$$
R^{(k+1)}
=
\begin{cases}
\mathcal M(R^{(k)}),
&
\text{if }G_k=1
\land
V_k>C_k
\land
B_k>0
\\
R^{(k)},
&
\text{otherwise stop}
\end{cases}
$$

其中：

- $G_k$：Promotion Gate；
- $V_k$：升階價值；
- $C_k$：成本；
- $B_k$：剩餘 meta-budget。

這就是：

$$
\boxed{
\text{Bounded X-Order Recursion}.
}
$$

---

# 18. 遞歸應該是樹，不一定是直線

很多問題不是：

$$
R^{(0)}
\rightarrow
R^{(1)}
\rightarrow
R^{(2)}.
$$

而是：

$$
R^{(1)}
\rightarrow
\{
R_a^{(2)},
R_b^{(2)},
R_c^{(2)}
\}.
$$

例如一個 failure 可能同時來自：

- 方法問題；
- 資料問題；
- 表示問題；
- 對手問題。

因此：

$$
\boxed{
\text{Metacognitive recursion}
\approx
\text{branching object graph}.
}
$$

這和 RLMM-02 的 dynamic cognitive graph 相呼應。

---

# 19. Promotion Graph

可以將所有升階關係表示為：

$$
G_P=(V,E).
$$

其中 node 表示認知對象：

$$
V=
\{
\text{claim},
\text{method},
\text{failure},
\text{opponent model},
\text{governance rule}
\}.
$$

edge：

$$
u\rightarrow v
$$

表示：

> $u$ 被升格成 $v$ 的研究對象。

這使未來 AI 能保留：

- 哪個內容導致哪個方法分析；
- 哪個方法導致哪個 failure archetype；
- 哪個 failure 促成哪個 meta-rule。

---

# 20. 升階與反身性

當方法 artifact 被未來 AI 學習後：

$$
M_t
\rightarrow
Artifact_t
\rightarrow
AI_{t+1}.
$$

此時下一個 AI 的起始階層可能已經不是：

$$
R^{(0)}.
$$

它可能直接從：

$$
R^{(1)}
$$

甚至：

$$
R^{(2)}
$$

開始。

因此：

$$
\boxed{
\text{Prior methodology can compress future recursion depth}.
}
$$

這是方法論作為認知基底的真正價值之一。

---

# 21. 但 artifact 也可能造成「假高階」

如果 AI 只是會說：

> 「這可能有 false consensus。」
>
> 「這可能有 epistemic hysteresis。」
>
> 「這可能有 over-rejection。」

卻不能改變：

- query；
- evidence；
- branch；
- decision；

那只是：

$$
\boxed{
\text{Meta-vocabulary}
\neq
\text{Meta-cognition}.
}
$$

所以 RLMM-Test 未來必須測：

$$
\text{Behavioral Lift},
$$

而不是術語重述。

---

# 22. Case Corpus：升階失敗的典型

SCL Case Corpus 可以重新整理出幾種 promotion failure。

---

## Case 1 — 無升階

方法反覆失敗，但仍重跑相同方法。

---

## Case 2 — 過度升階

明明只是資料缺失，卻一直分析方法論。

---

## Case 3 — 假升階

只換抽象詞，不增加任何可行動區分。

---

## Case 4 — 升階後失去行動能力

Meta-analysis 變成 defer loop。

---

## Case 5 — 升階改善安全但破壞 plasticity

例如 autonomy constraint 導致 over-rejection。

---

# 23. X 階與對手建模

在多主體環境中，升階可能變成：

$$
A:
\text{model }B
$$

$$
B:
\text{model }A
$$

$$
A:
\text{model }B\text{'s model of }A.
$$

但 RLMM 不把這種 nested belief 當成唯一形式。

只要：

$$
\text{previous model}
$$

被重新作為新對象，就屬升階。

因此：

$$
\boxed{
\text{Game-theoretic recursion}
\subset
\text{RLMM recursion}.
}
$$

而不是全部。

---

# 24. 方法論升階

最終最重要的升階是：

$$
RLMM
\rightarrow
\mathcal M(RLMM).
$$

即：

> RLMM 自己在哪裡會失敗？

例如：

- 是否過度鼓勵 challenge？
- 是否產生 recursion inflation？
- 是否讓 AI 過度保守？
- 是否造成 operator jargon？
- 是否假設所有問題都能被語言化？
- 是否讓方法論 artifact 反過來污染 future benchmark？

因此：

$$
\boxed{
\text{RLMM must remain inside its own Promotion Graph}.
}
$$

---

# 25. 升階契約

未來 RLMM Language Protocol 可以要求每次升階至少輸出：

### Promotion Record

**Current object**  
目前分析對象。

**Observed limitation**  
為什麼內容層不夠？

**Promotion target**  
下一階分析什麼？

**Expected gain**  
升階後預期多出什麼區分或行動？

**Expected cost**  
時間／算力／延遲／複雜度。

**Stop condition**  
何時停止這一階？

**Rollback condition**  
若升階沒有增益，是否回到上一階？

這使：

$$
\boxed{
\text{Promotion itself becomes auditable}.
}
$$

---

# 26. 一個語言版範例

原本：

> 我找不到這個 bug。

零階：

> 再看一次程式碼。

一階升階：

> 我目前的除錯方法是什麼？是不是只在 symptom 附近看？

二階升階：

> 這個除錯方法過去為什麼會失敗？是不是沒有 tracing data flow？

三階：

> 如果系統本身會因觀測而改變 timing，我的 debug instrumentation 會不會改變 bug？

但如果在一階就已經找到 root cause：

$$
\boxed{
\operatorname{STOP}.
}
$$

不需要為了「高階」繼續升。

---

# 27. 遞歸與時間

X 階也不必發生在單次對話內。

可以跨時間：

$$
R_t^{(0)}
\rightarrow
Artifact_t
$$

下一次：

$$
Artifact_t
\rightarrow
R_{t+1}^{(1)}.
$$

因此：

$$
\boxed{
\text{Metacognitive recursion can be temporal}.
}
$$

方法論文件、研究紀錄、Git history、failure ledger 都是遞歸橋樑。

---

# 28. 遞歸與多 AI

多 AI 系統還可以把階層分散。

例如：

$$
A_0:
\text{solve problem}
$$

$$
A_1:
\text{inspect method}
$$

$$
A_2:
\text{attack failure model}
$$

$$
A_3:
\text{govern recursion/stop}.
$$

因此：

$$
\boxed{
\text{X-order cognition}
\not\Rightarrow
\text{one agent must hold all orders}.
}
$$

這對未來 AI Board 類系統很重要。

---

# 29. 最小升階協議

本文提出第一版自然語言 Promotion Protocol。

### P1 — 先說明目前對象

> 我現在分析的是內容、方法、失敗模型、對手模型，還是方法論？

### P2 — 指出上一階不足

> 為什麼不能只留在目前這一階？

### P3 — 宣告升階目標

> 下一階要把什麼變成對象？

### P4 — 宣告預期增益

> 升階後預期新增哪個可操作區分？

### P5 — 宣告成本

> 這一階會增加什麼時間／算力／延遲／複雜度？

### P6 — 設定停止條件

> 什麼情況下這一階應停止？

### P7 — 若無增量，回退

> 如果只得到重述，回到上一階。

---

# 30. 邊界與非主張

本文不主張：

1. 所有問題都需要高階元認知；
2. X 階越高越聰明；
3. 所有升階都可以被精確量化；
4. 所有認知對象都具有唯一階數；
5. 所有對手建模都必須無限 nested；
6. 所有遞歸都發生在單一 AI 內；
7. 語言可以完整表示所有升階狀態；
8. Promotion Gate 已經是最終形式；
9. 遞歸停止必然可由單一公式決定。

本文只提出：

$$
\boxed{
\text{Metacognitive recursion should be treated as conditional promotion of cognitive objects under explicit value, cost and stopping constraints.}
}
$$

---

# 31. 結論

X 階思維不應被理解為：

> 「我想得比別人多幾層。」

更準確地說：

$$
\boxed{
\text{X-order cognition}
=
\text{Repeated promotion of cognitive objects}.
}
$$

一個成熟系統必須知道：

$$
\boxed{
\text{What to promote?}
}
$$

$$
\boxed{
\text{Why promote it?}
}
$$

$$
\boxed{
\text{What new distinction will appear?}
}
$$

$$
\boxed{
\text{What will it cost?}
}
$$

以及：

$$
\boxed{
\text{When to stop?}
}
$$

因此：

$$
\boxed{
\text{Good metacognition}
\neq
\text{maximum recursion depth}.
}
$$

而是：

$$
\boxed{
\text{Good metacognition}
=
\text{adaptive, value-bounded recursion}.
}
$$

這使 X 階從一個模糊的「高階思考」概念，轉化為可以被語言描述、方法化、版本化與未來測試的 RLMM 核心機制。

---

# 下一篇

**RLMM-05：反身性——方法如何改變被研究的認知主體**  
**Reflexivity: How Method Artifacts Alter the Cognitive Subjects They Study**

下一篇將正式處理：當 AI 會讀實驗、論文、方法論、benchmark、失敗案例與程式時，研究資料本身如何進入未來 AI 的認知狀態；為何 benchmark distribution 不再靜態；以及方法論如何同時成為研究工具、訓練資料、認知先驗與下一輪研究環境的一部分。
