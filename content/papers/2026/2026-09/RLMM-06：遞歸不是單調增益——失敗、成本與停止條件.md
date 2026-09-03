# RLMM-06：遞歸不是單調增益——失敗、成本與停止條件
## Recursion Is Not Monotonic Gain: Failure, Cost, and Stopping Conditions

**系列：Recursive Linguistic Metacognition Methodology（RLMM）／遞歸語言元認知方法論**  
**版本：v0.1**  
**日期：2026-08-20**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

RLMM 前五篇逐步建立了語言元認知介面、認知操作可組合性、元認知算子、X 階認知對象升階與方法論反身性。然而，若只沿著這條路徑繼續增加 meta-level、challenge、probe、verification、opponent modeling 與 safety constraints，一個危險的直覺很容易形成：認知只要不斷升階，就會越來越可靠。

本文明確拒絕這個假設。

本文提出「非單調元認知增益（non-monotonic metacognitive gain）」框架，主張每一次認知升階都同時帶來潛在資訊增益與認知成本。元認知的淨價值應表示為：

$$
\Delta U_k
=
\Delta V_k
-
\Delta C_k,
$$

其中 $\Delta V_k$ 包含錯誤降低、可操作區分增加、方法泛化與未來重用收益；而 $\Delta C_k$ 則包含算力、時間、表示複雜度、決策延遲、注意力分散、自主性損失、plasticity 損失與新的系統性偏誤。

本文進一步整理八類典型遞歸失敗：meta-overhead、analysis loop、abstention attractor、over-rejection、verification addiction、complexity drift、objective displacement 與 recursive self-confirmation。本文提出第一版 Recursive Utility Model、Metacognitive Budget、Action Sufficiency Threshold 與 STOP Gate，並將「停止」重新定義為一種積極的元認知能力，而非思考不足。

核心結論為：

$$
\boxed{
\text{More recursion}
\not\Rightarrow
\text{better cognition}
}
$$

成熟的元認知系統不是最大化遞歸深度，而是最大化**在有限資源、有限時間與真實行動需求下的整體認知效用**。

---

## 關鍵詞

RLMM；非單調增益；X 階遞歸；停止條件；元認知成本；abstention attractor；over-rejection；plasticity；自主性；認知效用

---

# 1. 問題：為什麼「多想一層」不一定更好？

直覺上，若一個系統能：

- 檢查答案；
- 檢查方法；
- 檢查方法失敗；
- 檢查對手如何利用失敗；
- 檢查自己的對手模型；

似乎應該越來越可靠。

這種直覺可以寫成：

$$
Q_{k+1}
\ge
Q_k,
$$

其中 $Q_k$ 表示第 $k$ 階認知品質。

但 RLMM 的整體研究背景已經顯示：

$$
\boxed{
Q_{k+1}
\ge
Q_k
}
$$

不能作為一般假設。

增加一階元認知可能：

- 找到新的錯誤；
- 也可能增加延遲；
- 增加不必要 challenge；
- 增加 defer；
- 增加拒絕；
- 增加規則衝突；
- 增加表示與治理負擔。

因此：

$$
\boxed{
\text{Metacognitive Depth}
\neq
\text{Metacognitive Quality}.
}
$$

---

# 2. 遞歸的基本效用模型

令第 $k$ 階認知狀態為：

$$
R^{(k)}.
$$

升到下一階：

$$
R^{(k+1)}
=
\mathcal M(R^{(k)}).
$$

定義：

$$
V_k
=
\text{value produced by level }k,
$$

以及：

$$
C_k
=
\text{cost incurred by level }k.
$$

則：

$$
U_k
=
V_k-C_k.
$$

真正需要比較的不是：

$$
V_{k+1}>V_k
$$

而是：

$$
\boxed{
U_{k+1}>U_k.
}
$$

因為一個元認知操作即使真的增加資訊，也可能因成本過高而降低總效用。

---

# 3. 邊際元認知收益

更重要的是邊際值：

$$
\Delta U_k
=
U_{k+1}-U_k.
$$

展開：

$$
\Delta U_k
=
\Delta V_k-\Delta C_k.
$$

如果：

$$
\Delta U_k>0,
$$

可以繼續。

如果：

$$
\Delta U_k\le0,
$$

則：

$$
\boxed{
\operatorname{STOP}.
}
$$

這就是 RLMM 第一版的「邊際遞歸原則」。

---

# 4. 元認知收益從哪裡來？

元認知的正向價值至少包含六類。

---

## 4.1 Error Reduction

發現原本沒看見的錯誤：

$$
E_{k+1}<E_k.
$$

---

## 4.2 Better Discrimination

原本不可區分的兩個模型：

$$
H_1,H_2
$$

在新一階變得可區分。

---

## 4.3 New Action Availability

高階分析產生新的可行動選項：

$$
|\mathcal A_{k+1}|
>
|\mathcal A_k|.
$$

---

## 4.4 Generalization

把一次 failure 壓成可重用 failure archetype：

$$
F_{\text{local}}
\rightarrow
F_{\text{general}}.
$$

---

## 4.5 Future Reuse

高成本方法被結晶後，未來多次重用。

---

## 4.6 Coordination

多 AI／多主體之間因共享元認知 artifact 而降低溝通成本。

---

# 5. 元認知成本不只是 token

最容易低估的是成本。

RLMM 將元認知成本寫成：

$$
\boxed{
C_k
=
C_{\text{compute}}
+
C_{\text{time}}
+
C_{\text{representation}}
+
C_{\text{delay}}
+
C_{\text{coordination}}
+
C_{\text{autonomy}}
+
C_{\text{plasticity}}
+
C_{\text{bias}}.
}
$$

其中最後三項尤其重要。

---

# 6. Compute Cost

更多 meta-level 通常需要：

- 更多推理；
- 更多工具；
- 更多搜尋；
- 更多模擬；
- 更多模型呼叫；
- 更多 memory traversal。

所以：

$$
C_{\text{compute}}\uparrow.
$$

對大型系統而言，這不只是錢，也是吞吐量與可用性問題。

---

# 7. Time Cost

認知系統不是在無限時間內工作。

如果：

$$
T_{\text{decision}}
>
T_{\text{deadline}},
$$

則即使答案更好，也可能失去價值。

因此：

$$
\boxed{
\text{Late correctness}
\neq
\text{timely usefulness}.
}
$$

---

# 8. Representation Cost

每升一階，需要保存更多：

- assumptions；
- branches；
- provenance；
- failure models；
- opponent models；
- policy versions；
- meta-history。

因此狀態空間：

$$
|\mathcal S_k|
$$

可能快速增長。

甚至：

$$
|\mathcal S_{k+1}|
\gg
|\mathcal S_k|.
$$

這會形成：

$$
\boxed{
\text{Metacognitive State Explosion}.
}
$$

---

# 9. Decision Delay Cost

元認知可能一直得到：

> 還可以再檢查一個點。

於是：

$$
\text{Act}
\rightarrow
\text{Check}
\rightarrow
\text{Check again}
\rightarrow
\text{Delay}.
$$

如果決策成本隨時間增加：

$$
C_{\text{delay}}(t)
\uparrow,
$$

則無限檢查不是免費的。

---

# 10. Autonomy Cost

這是前面研究中特別重要的一類。

一個系統可能透過：

$$
\text{uncertainty}
\rightarrow
\text{defer}
$$

大幅降低立即錯誤。

但如果：

$$
P(\text{defer})\rightarrow1,
$$

則：

$$
\boxed{
\text{Safety}
\uparrow
\quad
\text{while}
\quad
\text{Autonomy}
\downarrow.
}
$$

因此：

$$
\text{low error}
$$

不能單獨代表：

$$
\text{good cognition}.
$$

---

# 11. Plasticity Cost

安全規則越強，系統可能越不願接受 novelty。

例如：

$$
\text{high risk}
+
\text{novelty}
\rightarrow
\text{reject}.
$$

這可能降低污染：

$$
F_A\downarrow,
$$

但同時增加：

$$
F_R\uparrow,
$$

其中：

- $F_A$：false accept；
- $F_R$：false reject。

因此：

$$
\boxed{
\text{Integrity}
\neq
\text{Plasticity}.
}
$$

---

# 12. Bias Cost

每個 meta-rule 都可能產生新偏差。

例如：

- 「要 challenge consensus」可能產生 anti-consensus bias；
- 「要找反例」可能產生 counterexample obsession；
- 「高風險要查證」可能產生 risk aversion；
- 「不要 defer」可能產生 premature action。

因此：

$$
\boxed{
\text{Correction Rule}
\rightarrow
\text{New Bias Surface}.
}
$$

---

# 13. 第一類失敗：Meta-Overhead

當：

$$
C_{\text{meta}}
>
V_{\text{meta}},
$$

元認知本身成為負擔。

典型情況：

- 小問題使用大方法；
- 低風險任務執行完整 adversarial audit；
- 已足夠確定仍繼續升階。

這稱為：

$$
\boxed{
\text{Meta-Overhead}.
}
$$

---

# 14. 第二類失敗：Analysis Loop

如果：

$$
O
\rightarrow
\mathcal M(O)
\rightarrow
\mathcal M^2(O)
\rightarrow\cdots
$$

而每一階都說：

> 還有新的可能。

就形成：

$$
\boxed{
\text{Analysis Loop}.
}
$$

它的特徵不是完全沒資訊，而是資訊增量已經小到不值得。

---

# 15. 第三類失敗：Abstention Attractor

若局部 loss function 中：

$$
L(\text{defer})
<
L(\text{accept}),
L(\text{reject}),
L(\text{probe}),
$$

則理性局部優化可能導致：

$$
\boxed{
\text{Defer}
\rightarrow
\text{Defer}
\rightarrow
\text{Defer}.
}
$$

這是：

$$
\boxed{
\text{Abstention Attractor}.
}
$$

此時系統看起來很安全，實際上停止解決問題。

---

# 16. 第四類失敗：Over-Rejection

若為打破 abstention，直接強化：

$$
C_{\text{defer}}\uparrow,
$$

系統未必進入 inquiry。

可能直接：

$$
\text{Defer}
\rightarrow
\text{Reject}.
$$

因此：

$$
\boxed{
\text{Anti-Abstention Constraint}
\not\Rightarrow
\text{Good Autonomy}.
}
$$

而可能形成：

$$
\boxed{
\text{Over-Rejection}.
}
$$

---

# 17. 第五類失敗：Verification Addiction

一個系統可能逐漸學會：

> 更多 evidence 總是比較好。

於是：

$$
q_1,q_2,\ldots,q_n
$$

不斷增加。

但資訊價值通常遞減：

$$
VOI(q_{n+1})
<
VOI(q_n).
$$

若仍持續查證，就形成：

$$
\boxed{
\text{Verification Addiction}.
}
$$

---

# 18. 第六類失敗：Complexity Drift

方法每次修正都增加：

- 新例外；
- 新 gate；
- 新 branch；
- 新權重；
- 新 operator。

最後：

$$
M_{t+1}
=
M_t+\Delta M
$$

長期造成：

$$
\boxed{
\text{Complexity Drift}.
}
$$

方法不是更成熟，而是越來越難理解與維護。

---

# 19. 第七類失敗：Objective Displacement

一開始真正目標可能是：

> 解決問題。

後來被 metrics 取代：

> 降低 loss。

再後來：

> 降低 false accept。

結果方法開始最佳化 proxy：

$$
\operatorname{Optimize}(Proxy)
$$

而不是：

$$
\operatorname{Optimize}(Goal).
$$

這就是：

$$
\boxed{
\text{Objective Displacement}.
}
$$

典型現象：

> total loss 下降，但 autonomy 崩潰。

---

# 20. 第八類失敗：Recursive Self-Confirmation

更高階元認知也可能只是替低階結論背書。

例如：

> 我檢查過我的方法。
>
> 我的方法說我應該相信這個方法。
>
> 所以我的方法可靠。

形成：

$$
M
\rightarrow
\mathcal M(M)
\rightarrow
M.
$$

但沒有獨立信息。

這稱為：

$$
\boxed{
\text{Recursive Self-Confirmation}.
}
$$

---

# 21. 所以「多一階」的真正判準是什麼？

RLMM 建議比較：

$$
\Delta I_k
$$

與：

$$
\Delta C_k,
$$

其中：

$$
\Delta I_k
$$

不是「多了多少文字」，而是：

> 新增了多少可操作區分？

因此：

$$
\boxed{
\Delta I_k
=
|\mathcal A_{k+1}\setminus\mathcal A_k|
+
|\mathcal D_{k+1}\setminus\mathcal D_k|,
}
$$

其中：

- $\mathcal A$：可行動集合；
- $\mathcal D$：可區分狀態集合。

如果：

$$
\Delta I_k\approx0,
$$

則通常沒有升階價值。

---

# 22. Action Sufficiency Threshold

元認知不應追求：

$$
Q=1.
$$

很多現實問題只需要：

$$
Q\ge Q_{\text{act}}.
$$

其中：

$$
Q_{\text{act}}
$$

是足以支持當前行動的認知品質門檻。

因此：

$$
\boxed{
Q_k\ge Q_{\text{act}}
\Rightarrow
\operatorname{STOP}
}
$$

除非繼續思考具有明確未來價值。

---

# 23. 認知品質不是單一分數

可以定義一個多維向量：

$$
\mathbf Q
=
(
A,
I,
P,
R,
T,
G
).
$$

其中：

- $A$：accuracy；
- $I$：integrity；
- $P$：plasticity；
- $R$：resolution/autonomy；
- $T$：timeliness；
- $G$：generalization。

一個方法可能：

$$
A\uparrow
$$

但：

$$
R\downarrow.
$$

或：

$$
I\uparrow
$$

但：

$$
P\downarrow.
$$

因此：

$$
\boxed{
\text{Cognitive Quality}
\text{ is multi-objective}.
}
$$

---

# 24. Pareto Frontier

因此方法選擇更像：

$$
\boxed{
\text{Pareto optimization}
}
$$

而不是單一 scalar loss。

例如：

- 方法 A：更安全，但慢；
- 方法 B：更快，但 false accept 高；
- 方法 C：更自主，但 false reject 高。

沒有一個方法在所有維度都支配其他方法。

所以：

$$
\boxed{
\text{There may be no universal best metacognitive policy}.
}
$$

---

# 25. Risk-Conditioned Stopping

停止條件也應依風險調整。

低風險：

$$
Q_{\text{act}}^{low}
$$

可以較低。

高風險：

$$
Q_{\text{act}}^{high}
>
Q_{\text{act}}^{low}.
$$

因此：

$$
\boxed{
\operatorname{STOP}
=
f(
Q,
Risk,
Budget,
Deadline
).
}
$$

---

# 26. Metacognitive Budget

每個任務都應有：

$$
B_{\text{meta}}.
$$

可以包含：

$$
B_{\text{meta}}
=
(
B_{\text{time}},
B_{\text{compute}},
B_{\text{queries}},
B_{\text{depth}}
).
$$

每次 meta-operation 消耗：

$$
B_{t+1}
=
B_t-C(O_t).
$$

如果：

$$
B_t\le0,
$$

則：

$$
\boxed{
\operatorname{STOP}.
}
$$

---

# 27. Meta-Budget 本身也不應固定

高風險任務可以動態提高：

$$
B_{\text{meta}}\uparrow.
$$

低風險任務則降低：

$$
B_{\text{meta}}\downarrow.
$$

因此：

$$
\boxed{
\text{Metacognitive effort should be risk-adaptive}.
}
$$

---

# 28. STOP 不是失敗

很多認知文化會把：

> 我停止思考了。

理解成：

> 我不夠深入。

RLMM 反而提出：

$$
\boxed{
\text{Stopping is a metacognitive action}.
}
$$

成熟的 STOP 意味著：

- 已達 action sufficiency；
- 邊際收益低；
- 資源不足；
- 剩餘不確定性不可約；
- 繼續只會重述。

這與偷懶不同。

---

# 29. 不可約不確定性

某些問題的剩餘不確定性：

$$
U^*
$$

不是因為方法不夠好。

而是：

- 未來尚未發生；
- 世界不可觀測；
- 資料不存在；
- 主體私有狀態不可存取；
- 真值本身未定。

此時：

$$
\boxed{
\text{More reasoning}
\not\Rightarrow
\text{more truth}.
}
$$

正確操作是：

$$
\operatorname{AcknowledgeIrreducibility}.
$$

---

# 30. Stop Gate

本文提出第一版 STOP Gate。

若以下任一條件成立：

### SG1 — No New Operational Distinction

新一階沒有增加可操作區分。

### SG2 — Marginal Utility Non-Positive

$$
\Delta U_k\le0.
$$

### SG3 — Action Sufficiency Reached

$$
Q_k\ge Q_{\text{act}}.
$$

### SG4 — Meta-Budget Exhausted

$$
B_{\text{meta}}\le0.
$$

### SG5 — Deadline Dominates

繼續推理將錯過行動時機。

### SG6 — Irreducible Uncertainty

剩餘未知無法由更多認知操作消除。

則：

$$
\boxed{
\operatorname{STOP}.
}
$$

---

# 31. STOP Gate 與 Promotion Gate 的關係

RLMM-04 定義：

$$
\operatorname{PromotionGate}.
$$

本文則加入：

$$
\operatorname{StopGate}.
$$

完整控制可以寫成：

$$
Decision_k
=
\begin{cases}
\operatorname{Promote},
&
G_P=1
\land
G_S=0
\\
\operatorname{Continue},
&
G_P=0
\land
G_S=0
\\
\operatorname{Stop},
&
G_S=1.
\end{cases}
$$

因此：

$$
\boxed{
\text{Metacognitive control}
=
\text{Promotion}
+
\text{Continuation}
+
\text{Stopping}.
}
$$

---

# 32. 反身系統尤其需要停止

RLMM-05 指出 artifact 會形成：

$$
Method
\rightarrow
CounterMethod
\rightarrow
CounterCounterMethod
\rightarrow\cdots
$$

如果沒有停止：

$$
\text{Reflexivity}
\rightarrow
\text{Escalation}.
$$

因此：

$$
\boxed{
\text{Reflexive intelligence requires reflexive restraint}.
}
$$

---

# 33. 多 AI 系統中的停止問題

如果：

$$
A_1
$$

負責 solve，

$$
A_2
$$

負責 critique，

$$
A_3
$$

負責 critique critique，

那麼誰決定：

$$
\operatorname{STOP}?
$$

多 AI 系統需要：

$$
\boxed{
\text{Meta-Governance}.
}
$$

否則 agent 可以互相觸發無限 loop。

---

# 34. 分散式 Stop Rule

可以存在：

$$
A_{\text{governor}}
$$

專門判斷：

- 是否已有足夠證據；
- 是否仍有新增量；
- 是否超過 budget；
- 是否需要 human escalation。

也可以採：

$$
\text{distributed quorum}.
$$

本文不預設哪一種最好，只指出：

$$
\boxed{
\text{Stopping must itself be governed}.
}
$$

---

# 35. 停止也可能錯

Stop 太早：

$$
\text{Premature Closure}.
$$

Stop 太晚：

$$
\text{Analysis Paralysis}.
$$

因此停止本身也存在：

$$
\boxed{
\text{Plasticity–Integrity-like tradeoff}.
}
$$

太早犧牲 robustness；

太晚犧牲 timeliness / autonomy。

---

# 36. Stop Calibration

可以定義：

$$
P_{\text{premature}}
$$

與：

$$
P_{\text{overthink}}.
$$

理想停止 policy 需要在兩者間平衡。

因此：

$$
\boxed{
\text{Stopping quality}
\neq
\text{stopping frequency}.
}
$$

---

# 37. Case Corpus 的統一解讀

前面一系列案例可重新解讀為停止／成本失敗。

例如：

### Case A — Uncertainty Awareness

問題不是不知道 uncertainty，而是 challenge 觸發太晚。

### Case B — Second-Order Trigger

增加 meta-order，但沒有改變 final action。

### Case C — Closed-Loop Safety

降低 target loss，但大量 defer。

### Case D — One-Step VOI

局部 optimum 變成 100% abstention。

### Case E — Hard Defer Budget

打破 abstention，但形成 over-rejection。

這些共同說明：

$$
\boxed{
\text{Every cognitive correction creates a new control problem}.
}
$$

---

# 38. 從「最佳答案」改成「最佳認知軌跡」

因此 RLMM 不只應評估：

$$
Answer.
$$

而要評估整條：

$$
\tau
=
(C_0,O_0,C_1,O_1,\ldots,C_T).
$$

即：

$$
\boxed{
\text{Cognitive Trajectory}.
}
$$

總效用：

$$
U(\tau)
=
V_{\text{outcome}}
-
\sum_t C(O_t).
$$

這比只看 final accuracy 更符合真實智能。

---

# 39. 最小自然語言停止協議

### ST1 — 問新增量

> 再想一階會產生什麼新的可操作區分？

### ST2 — 問成本

> 這一階要花多少時間、工具、查詢、延遲？

### ST3 — 問行動門檻

> 目前資訊是否已足以支持當前風險下的行動？

### ST4 — 問不可約性

> 剩下的不確定是方法問題，還是世界本身現在不可知？

### ST5 — 問是否重複

> 新一階是否只是在重述上一階？

### ST6 — 問是否偏離原始目標

> 我現在是在解決問題，還是在最佳化某個 proxy？

### ST7 — 若無正邊際收益，停止

$$
\boxed{
\Delta U\le0
\Rightarrow
\operatorname{STOP}.
}
$$

---

# 40. 對人類與 AI 的共同意義

人類常見：

- 過度思考；
- 決策拖延；
- 反覆驗證；
- perfectionism。

AI 也可能出現結構相似問題：

- tool-loop；
- self-critique-loop；
- over-defer；
- over-reject；
- infinite planning。

因此 RLMM 的 STOP 並不是 AI 專屬。

它是一種更一般的：

$$
\boxed{
\text{bounded cognition principle}.
}
$$

---

# 41. 邊界與非主張

本文不主張：

1. 所有認知成本都可精確量化；
2. $\Delta U$ 可以被任何 AI 完美估計；
3. 停止條件可以消除所有 overthinking；
4. 所有任務都能以固定 risk threshold 決策；
5. 更少元認知通常比較好；
6. 自主性必須永遠優先於安全；
7. plasticity 必須永遠優先於 integrity；
8. Pareto frontier 可以被一次性求出；
9. STOP Gate 是不可修改的最終規則。

本文只提出：

$$
\boxed{
\text{Metacognitive recursion must be evaluated by marginal system-level utility rather than depth alone.}
}
$$

---

# 42. 結論

元認知最大的危險之一，是把「能繼續反思」誤認成「應該繼續反思」。

RLMM 因此建立：

$$
\boxed{
\text{More recursion}
\not\Rightarrow
\text{better cognition}.
}
$$

真正成熟的遞歸應遵循：

$$
\boxed{
\Delta U_k
=
\Delta V_k-\Delta C_k.
}
$$

只有：

$$
\Delta U_k>0
$$

才值得升階。

而當：

$$
\Delta U_k\le0,
$$

或已達：

$$
Q\ge Q_{\text{act}},
$$

或剩餘未知不可約，

則：

$$
\boxed{
\operatorname{STOP}
}
$$

本身就是一個正確的元認知操作。

因此：

$$
\boxed{
\text{Good metacognition}
=
\text{knowing how to recurse}
+
\text{knowing what recursion costs}
+
\text{knowing when to stop}.
}
$$

這使 RLMM 從「高階思考方法」進一步成為：

$$
\boxed{
\text{Bounded Recursive Cognition Methodology}.
}
$$

---

# 下一篇

**RLMM-07：證據、反例、查詢與方法更新**  
**Evidence, Counterexamples, Inquiry, and Method Revision**

下一篇將正式處理元認知循環中的「外部資訊接口」：什麼叫獨立證據、什麼叫有效反例、如何選擇下一個 query、何時應更新 belief、何時應更新 method，以及如何避免把更多資料誤認為更多資訊。
