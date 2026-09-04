# 政治符號學 2.0——共享政治世界、關係耦合與動態契約
## Paper 09：政治人物本來可以怎麼做
### 反事實世界、可達選項與政治責任的動態分析

**Political Semiotics 2.0 — Shared Political Worlds, Relational Coupling, and Dynamic Contract**  
**Paper 09: What Could a Political Actor Actually Have Done? — A Dynamic Analysis of Counterfactual Worlds, Reachable Options, and Political Responsibility**

**作者：Neo.K × Aletheia**  
**機構：EveMissLab／一言諾科技有限公司**  
**版本：v0.1**  
**日期：2026-08-30**  
**性質：內部研究論文／系列反事實政治責任篇**

---

## 摘要

政治人物與政府的事後評價經常陷入兩種極端。第一種是結果論：只要結果不好，就推定當初決策錯誤；第二種則是不可知論：因為政治世界過度複雜、反事實無法直接觀察，所以幾乎不能對決策者進行可靠的責任比較。兩種方法都不足。

本文提出「可達反事實政治責任框架」（Reachable Counterfactual Political Responsibility Framework, RCPRF）。其核心主張是：政治責任不應與任何想像得到的替代世界比較，而應與決策當時在資訊、資源、制度、權限、時間與物理條件下真正可達的替代方案集合比較。

令政治行動者 $A_j$ 在時間 $t$ 的可能行動全集為：

$$
\Omega_j^{possible}(t),
$$

但真正可達的決策集合為：

$$
\boxed{
\Omega_j^{reachable}(t)
\subseteq
\Omega_j^{possible}(t).
}
$$

可達性取決於：

$$
\Omega_j^{reachable}(t)
=
F
\left(
\mathcal{K}_j(t),
\mathcal{R}_j(t),
\mathcal{A}_j(t),
\mathcal{I}(t),
\mathcal{T}(t),
\mathcal{C}(t)
\right),
$$

其中：

- $\mathcal{K}_j$：當時可合理取得的資訊；
- $\mathcal{R}_j$：可支配資源；
- $\mathcal{A}_j$：制度與法律權限；
- $\mathcal{I}$：制度約束；
- $\mathcal{T}$：可用時間；
- $\mathcal{C}$：外部條件。

本文區分四個評價層次：結果品質、決策品質、可預見性與反事實可改善性。由此提出：

$$
\boxed{
\text{Bad Outcome}
\neq
\text{Bad Decision}
}
$$

以及：

$$
\boxed{
\text{Better Imagined World}
\neq
\text{Better Reachable Alternative}.
}
$$

本文進一步建立「可達反事實差」：

$$
\Delta^{RCF}_j
=
Y(a_j)
-
\max_{a\in\Omega_j^{reachable}(t)}
\mathbb{E}
\left[
Y(a)
\mid
\mathcal{K}_j(t)
\right],
$$

用以估計行動者相對於當時可達最佳替代方案的決策損失。此量不是單獨決定責任，而需與控制力、資訊義務、風險、不可逆性、延遲修正及因果貢獻共同評估。

本文同時處理「資訊義務」問題：決策者不能藉由主動不取得資訊降低責任。若某項關鍵資訊本應在其職責與能力範圍內取得，則：

$$
\text{Avoidable Ignorance}
\neq
\text{Innocent Ignorance}.
$$

此外，當結果隨時間展開，責任不能停留於最初決策。若新證據出現後仍拒絕修正，則後續每一時間點都形成新的可達選項集合與新的責任判斷。

本文最後將反事實政治責任接回政治符號學 2.0：政治符號如「他搞砸了」「歷史必然」「人民選錯了」「沒有別的辦法」都是高壓縮敘事，必須展開為資訊集、可達選項、因果路徑與時間序列。這為 Paper 10 建立最後接口：當主體、制度、國家與人民的行動被置入不同尺度與觀察者位置後，「國家」「人民」「民族」等高階政治符號究竟如何壓縮整個多尺度政治世界？

**關鍵詞：** 反事實、政治責任、可達選項、決策品質、結果論、可預見性、因果推論、FDCS、政治符號學、歷史判斷

---

# 第一部　問題：政治人物「本來可以怎麼做」？

## 1. 最常見的事後問題

政治事件發生後，人們常說：

> 他當初應該怎麼做。

> 如果換另一個人就不會這樣。

> 早知道就不要做。

> 他根本沒有別的選擇。

這些句子都在使用反事實。

也就是比較：

$$
W_{actual}
$$

與：

$$
W_{counterfactual}.
$$

但反事實世界不能任意想像。

---

## 2. 幻想世界不是有效反事實

如果某人說：

> 最好的方案是當時立刻得到未來十年的完整情報。

這不是有效政治替代方案。

因為：

$$
PerfectFutureKnowledge
\notin
\Omega_t^{reachable}.
$$

同樣地：

> 政府當時應該立刻多出十倍預算。

如果資源根本不存在，也不是可達方案。

因此：

$$
\boxed{
CounterfactualEvaluation
\text{ must be reachability-constrained.}
}
$$

---

# 第二部　三種可能空間

## 3. 邏輯可能空間

首先有：

$$
\Omega^{logical}.
$$

這包括邏輯上可以描述的所有行動。

範圍最大。

---

## 4. 物理／歷史可能空間

其中部分選項在當時世界條件下根本不可行。

因此：

$$
\Omega^{historical}
\subseteq
\Omega^{logical}.
$$

---

## 5. 行動者可達空間

對特定政治人物 $A_j$：

$$
\boxed{
\Omega_j^{reachable}(t)
\subseteq
\Omega^{historical}(t).
}
$$

這才是責任比較的主要基準。

---

# 第三部　可達性由什麼決定？

## 6. 資訊集

令：

$$
\mathcal{K}_j(t)
$$

為行動者在當時合理可取得的資訊。

包括：

- 公開資料；
- 部會簡報；
- 情報；
- 專家意見；
- 歷史經驗；
- 即時警告。

決策品質應使用：

$$
\mathcal{K}_j(t)
$$

而不是：

$$
\mathcal{K}(t+n)
$$

事後才知道的資訊。

---

## 7. 資源集

令：

$$
\mathcal{R}_j(t)
$$

包括：

- 預算；
- 人力；
- 行政能力；
- 軍事能力；
- 技術；
- 外交籌碼。

如果方案需要：

$$
Resource(a)
>
\mathcal{R}_j(t),
$$

則：

$$
a
\notin
\Omega_j^{reachable}(t).
$$

---

## 8. 權限集

政治人物不一定有權做所有事情。

令：

$$
\mathcal{A}_j(t)
$$

為其法律與制度權限。

因此：

$$
LegalAuthority(a)=0
$$

可能使方案不可直接採行。

---

## 9. 制度約束

即使領袖支持某政策，也可能需要：

- 立法；
- 法院；
- 地方政府；
- 國際協議；
- 官僚執行。

因此：

$$
InstitutionalFeasibility(a)
$$

必須納入。

---

## 10. 時間約束

有些政策理論上可行，但時間不夠。

令：

$$
TimeRequired(a)
$$

與：

$$
TimeAvailable(t).
$$

若：

$$
TimeRequired(a)
>
TimeAvailable(t),
$$

則該方案可能不能解決當前問題。

---

# 第四部　決策品質與結果品質

## 11. 好結果可能來自壞決策

如果：

$$
DecisionQuality<0
$$

但外部運氣很好：

$$
Luck\gg0,
$$

仍可能：

$$
Outcome>0.
$$

因此：

$$
\boxed{
GoodOutcome
\not\Rightarrow
GoodDecision.
}
$$

---

## 12. 壞結果可能來自好決策

反之：

$$
DecisionQuality>0
$$

但：

$$
ExternalShock\ll0,
$$

仍可能：

$$
Outcome<0.
$$

因此：

$$
\boxed{
BadOutcome
\not\Rightarrow
BadDecision.
}
$$

---

# 第五部　Ex Ante 與 Ex Post

## 13. 事前評價

事前評價使用：

$$
\mathcal{K}_j(t).
$$

它問：

> 在當時知道的事情下，這個決策合理嗎？

---

## 14. 事後評價

事後評價可以使用：

$$
\mathcal{K}(t+n).
$$

它問：

> 現在我們知道結果後，這個制度或模型哪裡需要修正？

兩者不能混用。

---

## 15. 事後知識不能倒灌

若：

$$
K_{future}
$$

在當時不存在，則：

$$
K_{future}
\notin
ResponsibilityBaseline(t).
$$

否則會形成：

$$
HindsightBias.
$$

---

# 第六部　可達反事實差

## 16. 實際結果

令實際選擇：

$$
a_j^*.
$$

結果為：

$$
Y(a_j^*).
$$

---

## 17. 可達最佳替代

在當時資訊下：

$$
a_j^{best}
=
\arg\max_{a\in\Omega_j^{reachable}(t)}
\mathbb{E}
\left[
Y(a)
\mid
\mathcal{K}_j(t)
\right].
$$

---

## 18. 可達反事實差

定義：

$$
\boxed{
\Delta_j^{RCF}
=
Y^{expected}(a_j^*)
-
Y^{expected}(a_j^{best}).
}
$$

若：

$$
\Delta_j^{RCF}\ll0,
$$

表示實際決策相對於可達較佳方案有明顯損失。

---

# 第七部　不是所有「更好方案」都一樣

## 19. 可知但不可執行

有些方案：

$$
Knowable=1
$$

但：

$$
Executable=0.
$$

不能視為完整替代。

---

## 20. 可執行但不可知

有些事後看來有效的方案，當時沒有合理理由知道它會成功。

因此：

$$
Executable=1
$$

但：

$$
JustifiablySelectable\approx0.
$$

責任不能直接按事後成功率計算。

---

## 21. 可知且可執行

真正高責任差通常出現在：

$$
Knowable=1,
\qquad
Executable=1,
\qquad
ClearlyBetter=1
$$

但仍未採取。

---

# 第八部　資訊義務與可避免無知

## 22. 「我不知道」不是永遠免責

如果政治人物本來有義務取得資訊：

$$
DutyToKnow=1,
$$

而他因疏忽未取得：

$$
KnowledgeAcquisition=0,
$$

則：

$$
Ignorance
$$

本身可能是責任來源。

---

## 23. 可避免無知

定義：

$$
I_j^{avoidable}
=
F
\left(
DutyToKnow,
Access,
Cost,
WarningSignals,
Negligence
\right).
$$

若：

$$
I_j^{avoidable}\gg0,
$$

則：

$$
\boxed{
AvoidableIgnorance
\neq
InnocentIgnorance.
}
$$

---

# 第九部　不作為也是反事實選擇

## 24. 不做也是做

政治分析常只研究：

$$
Action.
$$

但：

$$
NoAction
$$

本身也可能是一個選項。

因此：

$$
a_0
=
\text{Do Nothing}.
$$

---

## 25. 延遲成本

若問題隨時間惡化：

$$
H(t+1)>H(t),
$$

則等待具有成本。

因此：

$$
Delay
$$

也應進入可達反事實比較。

---

# 第十部　動態反事實：決策不是只發生一次

## 26. 新資訊會更新可達空間

時間 $t_0$：

$$
\Omega^{reachable}(t_0).
$$

新資訊出現後：

$$
\Omega^{reachable}(t_1)
\neq
\Omega^{reachable}(t_0).
$$

因此責任也需更新。

---

## 27. 起初合理，後來可能不合理

某政策在：

$$
t_0
$$

可能合理。

但當：

$$
Evidence_{new}
$$

出現後，繼續維持：

$$
Policy(t_1)
$$

可能變得不合理。

因此：

$$
\boxed{
InitialJustification
\neq
PermanentJustification.
}
$$

---

## 28. 修正責任

若：

$$
NewEvidence>Threshold
$$

而：

$$
Correction=0,
$$

則：

$$
Responsibility_{persistence}\uparrow.
$$

這與 Paper 04 的「持續不修正」命題直接相連。

---

# 第十一部　多人政治中的反事實

## 29. 不能只重建領袖世界

政治結果通常由：

$$
A_1,A_2,\ldots,A_n
$$

共同生成。

因此每個人有自己的：

$$
\Omega_i^{reachable}(t).
$$

---

## 30. 聯合可達空間

可定義：

$$
\Omega_G^{reachable}(t)
=
F
\left(
\Omega_1,
\Omega_2,
\ldots,
\Omega_n,
Coordination
\right).
$$

有些方案單一行動者無法做，但多方協調後可達。

---

## 31. 協調責任

如果：

$$
PotentialCoordination=1
$$

但政治人物拒絕協調：

$$
CoordinationAttempt=0,
$$

也可能形成責任。

---

# 第十二部　制度與結構反事實

## 32. 不只是「換一個領袖」

有些錯誤來自：

$$
Institution.
$$

即使換人：

$$
A_j\rightarrow A_k,
$$

結果仍可能相似。

因此需要比較：

$$
World_{actor-change}
$$

與：

$$
World_{institution-change}.
$$

---

## 33. 結構反事實

例如：

$$
Institution'
$$

如果能降低系統性失敗，則責任可能部分位於制度設計與制度維護者。

這接回 Paper 04 的：

$$
MetaResponsibility.
$$

---

# 第十三部　FDCS 接口：反事實不是單一平行世界

## 34. 扁平反事實的限制

傳統問法常是：

> 如果當時做 B，而不是 A，會怎樣？

但真實政治世界具有：

- 回饋；
- 多尺度；
- 時間依賴；
- 角色適應；
- 路徑依賴。

因此：

$$
A\rightarrow B
$$

的單一步比較可能不足。

---

## 35. 動態因果路徑

可以寫成：

$$
W^{(k)}
=
\left(
X_0,
A_0,
X_1,
A_1,
\ldots,
X_T
\right).
$$

不同世界的差異不只在初始選擇，而在後續整條路徑。

---

## 36. 因果權重時間化

政治因果可以寫成：

$$
W_t(i,j,c),
$$

其中：

- $i,j$：因果節點；
- $t$：時間；
- $c$：情境。

因此：

$$
Cause_{ij}
$$

不是永遠固定。

---

# 第十四部　政治評價中的四個反事實陷阱

## 37. 全知陷阱

假設決策者知道未來。

---

## 38. 無資源陷阱

假設不存在的資源可以被使用。

---

## 39. 無制度陷阱

假設政治人物可以無視法律、議會與執行能力。

---

## 40. 無反作用陷阱

假設其他政治主體不會因政策改變而調整行為。

這四者都會產生偽反事實。

---

# 第十五部　政治符號學 2.0 接口

## 41. 「沒有別的辦法」是一個高壓縮符號

政治人物說：

> 沒有別的辦法。

應展開為：

$$
|\Omega_j^{reachable}(t)|=1?
$$

還是：

$$
OtherOptionsExist
$$

但成本更高？

或：

$$
OtherOptionsWereHidden?
$$

---

## 42. 「他搞砸了」也是高壓縮符號

需要拆成：

- 結果不好；
- 決策當時不合理；
- 有更佳可達方案；
- 風險可預見；
- 具有控制力；
- 未及時修正。

因此：

$$
FailureLabel
=
\Pi_{symbol}
\left(
\text{Causal-Decision Structure}
\right).
$$

---

## 43. 「歷史必然」的去人格化

若：

$$
HistoricalNecessity
$$

被用來遮蔽可達替代方案，政治符號學應重新檢查：

$$
\Omega_t^{reachable}.
$$

如果：

$$
|\Omega_t^{reachable}|>1,
$$

那麼「必然」至少需要更強證明。

---

# 第十六部　十二項核心命題

## 44. RCPRF-A1：結果—決策非同一命題

$$
\boxed{
OutcomeQuality
\neq
DecisionQuality.
}
$$

---

## 45. RCPRF-A2：反事實可達性命題

$$
\boxed{
ValidCounterfactual
\subseteq
ReachableAlternative.
}
$$

---

## 46. RCPRF-A3：想像更好世界非有效替代命題

$$
\boxed{
BetterImaginedWorld
\neq
BetterReachableAlternative.
}
$$

---

## 47. RCPRF-A4：資訊時間一致命題

$$
Responsibility(t)
$$

應主要使用：

$$
KnowledgeAvailable(t).
$$

---

## 48. RCPRF-A5：事後知識禁止倒灌命題

$$
\boxed{
FutureKnowledge
\notin
ExAnteResponsibilityBaseline.
}
$$

---

## 49. RCPRF-A6：可避免無知命題

$$
\boxed{
AvoidableIgnorance
\neq
InnocentIgnorance.
}
$$

---

## 50. RCPRF-A7：不作為也是選擇命題

$$
\boxed{
NoAction
\in
\Omega^{reachable}
}
$$

在適用情況下成立。

---

## 51. RCPRF-A8：延遲具有因果成本命題

$$
Delay
\rightarrow
OutcomeChange.
$$

---

## 52. RCPRF-A9：責任時間更新命題

$$
\boxed{
Responsibility
=
R(t).
}
$$

---

## 53. RCPRF-A10：新證據要求重審命題

$$
NewEvidence
\rightarrow
Reevaluation.
$$

---

## 54. RCPRF-A11：多人可達空間命題

$$
\boxed{
CollectiveReachability
\neq
IndividualReachability.
}
$$

---

## 55. RCPRF-A12：結構反事實命題

$$
\boxed{
ActorAlternative
\neq
InstitutionalAlternative.
}
$$

政治責任需區分換人與改制度的不同因果世界。

---

# 第十七部　反例與限制

## 56. 可達集合本身也是估計

歷史研究很難完全知道：

$$
\Omega_t^{reachable}.
$$

因此需要：

- 檔案；
- 資源資料；
- 法律權限；
- 當時情報；
- 決策紀錄；
- 同時代專家意見。

---

## 57. 反事實不能直接被觀察

因此本文不主張：

$$
Y_{counterfactual}
$$

可被精確知道。

應使用：

$$
Probability,
Range,
Scenario.
$$

而不是偽精確值。

---

## 58. 最佳可達方案也不代表唯一正確答案

在價值衝突下：

$$
Y(a)
$$

本身可能是多維向量。

例如：

$$
Security\uparrow
$$

但：

$$
Freedom\downarrow.
$$

所以「最佳」依賴價值權重。

這與 Paper 03 直接相連。

---

# 第十八部　通往 Paper 10：高階政治符號與多尺度壓縮

## 59. 到目前為止，我們已經有了什麼？

Paper 01–09 已經建立：

- 多源政治知識；
- 公民 standing；
- 高維政治評價；
- 因果責任；
- 人民—國家雙生動力；
- 契約前關係；
- 動態契約張量；
- 類公意與高階代理；
- 可達反事實責任。

下一步就是：

> 這些高維結構在日常政治語言中，為什麼最後只剩「人民」「國家」「民族」「民主」「左派」「右派」這些符號？

---

## 60. Paper 10 的核心入口

Paper 10 將處理：

$$
\boxed{
HighDimensionalPoliticalWorld
\rightarrow
HighOrderPoliticalSymbols.
}
$$

並加入：

- 微觀；
- 中觀；
- 宏觀；
- 文明尺度；
- 觀察者位置；
- 投影失真。

這將直接導向已完成的 Paper 11：

> 當一個人說「我為國家而戰」時，那個「國家」究竟壓縮了哪些關係與動機？

---

# 結論

政治人物「本來可以怎麼做」不是一句可以靠事後想像回答的問題。

真正有效的比較必須重建：

$$
\boxed{
\Omega_j^{reachable}(t)
}
$$

也就是當時在真實資訊、資源、權限、制度、時間與外部條件下可以到達的選項集合。

因此政治責任應比較：

$$
ActualDecision
$$

與：

$$
BestReasonablyReachableAlternative.
$$

而不是：

$$
ActualWorld
$$

與：

$$
PerfectImaginedWorld.
$$

本文最終提出：

$$
\boxed{
\text{Responsibility}
\text{ is constrained by reachability,}
}
$$

但同時：

$$
\boxed{
\text{reachability itself can be morally and politically endogenous.}
}
$$

也就是政治人物不能透過：

- 不取得資訊；
- 關閉替代方案；
- 壓縮制度能力；
- 拒絕協調；

再宣稱：

> 我沒有別的選擇。

因此真正的政治反事實分析需要同時問：

1. 當時有哪些方案可達？
2. 哪些方案本來可以透過合理努力變得可達？
3. 誰掌握資訊？
4. 誰控制資源？
5. 誰關閉了替代路徑？
6. 新資訊出現後，誰拒絕修正？

這使政治責任從簡單結果論轉向動態因果責任。

下一篇將完成本系列前十篇的最後一塊：把以上所有高維政治結構重新壓縮回「國家」「人民」「民族」等高階政治符號，並分析尺度與觀察者如何共同決定政治意義。

---

# 內部理論接口

1. EveMissLab，《分形動態因果系統：超越反事實的因果推斷新範式》，2025。
2. EveMissLab，《權力越大為何責任越大——公眾人物、治理作用域與因果責任的形式化分析》，本系列 Paper 04，2026。
3. EveMissLab，《政治評價不是喜歡與討厭》，本系列 Paper 03，2026。
4. EveMissLab，《人民是否真的有一個意志——類公意、集體方向與高階代理》，本系列 Paper 08，2026。
5. EveMissLab，《政治算子論》，政治符號學 2.0 基礎論文 III，2026。
6. EveMissLab，《選擇底空間論》，政治符號學 2.0 基礎論文 II，2026。

# 經典理論接口

- David Lewis, works on counterfactuals.
- Judea Pearl, works on causal inference and intervention.
- James Woodward, works on interventionist causation.
- Daniel Kahneman, works on hindsight bias and judgment.
- Herbert Simon, works on bounded rationality.
- Graham Allison, works on governmental decision models.
- Philip Tetlock, works on political judgment and forecasting.

---

**Canonical source note:** 本文件以 UTF-8 Markdown 為正式原始稿。數學原始碼只使用 ` $...$ ` 與 `$$...$$` 作為 canonical delimiters；不以渲染後公式替代原始碼。
