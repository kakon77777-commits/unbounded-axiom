# AI 不只是生產工具，而是第二設計師

**系列：** AI 時代的創作、選擇與人類復古系列  
**篇次：** 第 6 篇  
**版本：** v0.1  
**性質：** 理論論文／AI 協作設計框架／公開版

---

## 摘要

生成式 AI 在創作產業中的用途，常被侷限在「生成更多東西」：圖像、文字、程式、音樂、關卡與資料。但當 AI 逐漸降低生產成本後，真正更稀缺的能力開始轉向：誰來持續檢查這些東西是否應該存在、是否彼此一致、是否真正改變使用者決策，以及是否形成整體產品價值。

本篇提出：

$$
\boxed{
\text{AI}
\neq
\text{Only a Production Tool}
}
$$

而可以被部署為：

$$
\boxed{
\text{AI as Permanent Second Designer}
}
$$

「第二設計師」不是讓 AI 取代人類的最終決策權，而是讓 AI 長期承擔第二視角、架構審查者、反對者、全域差分分析者、假設破壞者與設計紅隊。

本篇建立：

$$
\boxed{
\text{Design}
\rightarrow
\text{Implement}
\rightarrow
\text{AI Global Audit}
\rightarrow
\text{Human Review}
\rightarrow
\text{Revision}
}
$$

並主張，AI 最重要的創作價值之一，可能不是替人類做更多，而是替人類持續看見自己看不到的地方。

---

## 關鍵詞

AI Second Designer、AI Reviewer、Integration Audit、Design Red Team、創作協作、Integration Debt、全域審查、Agentic Development、Human-in-the-loop、選擇

---

# 1. 創作者最難看到的，是自己以為已經知道的東西

創作者知道：

- 設計意圖；
- 世界觀；
- 角色背景；
- 隱藏公式；
- 系統用途；
- 預期玩家行為；
- 尚未完成的未來規劃。

因此他會自然在腦內補完產品缺失。

設：

$$
M
=
\text{Creator Mental Model}
$$

$$
P
=
\text{Product State}
$$

創作者可能認為：

$$
Relation(M_i,M_j)=1
$$

但實際產品：

$$
Relation(P_i,P_j)=0
$$

所以：

$$
\boxed{
\text{Mental Completion}
\neq
\text{Product Completion}
}
$$

---

# 2. 第二設計師真正提供的是「摩擦」

第二設計師的價值，不是再替第一個設計師增加十個功能。

而是：

$$
\boxed{
\text{對第一個設計師的世界模型施加摩擦。}
}
$$

例如反問：

> 這個系統為什麼存在？

> 玩家什麼時候需要理解它？

> 如果刪掉它，作品真的會變差嗎？

> 這個角色被世界記住了嗎？

> 這個 ending 真的讀過前面的選擇嗎？

這些問題會把隱含假設逼到表面。

---

# 3. AI 為什麼適合扮演第二設計師

傳統小團隊很難長期擁有一個同時：

- 看得懂完整產品；
- 願意反覆閱讀所有版本；
- 理解程式與玩法；
- 了解玩家視角；
- 又敢持續反對作者；

的第二個人。

AI 的特殊價值是：

$$
\boxed{
\text{Low-Cost Repeated Review}
}
$$

它不一定永遠正確，但可以持續提供異議。

---

# 4. Reviewer Value 不等於 Decision Authority

第二設計師不需要：

$$
Accuracy=100\%
$$

真正需要的是：

$$
\boxed{
\text{Generate Useful Disagreement}
}
$$

因此：

$$
\boxed{
\text{Reviewer Value}
\neq
\text{Decision Authority}
}
$$

AI 可以指出：

> 這個系統可能冗餘。

人類仍可以回答：

> 我知道，但我刻意保留。

只要這個選擇已經成為：

$$
\boxed{
\text{Conscious Choice}
}
$$

review 就產生價值。

---

# 5. Human Final Authority

本篇主張：

$$
\boxed{
\text{AI Review}
\neq
\text{AI Rule}
}
$$

成熟流程應該是：

$$
\boxed{
\text{AI raises objections}
\rightarrow
\text{Human evaluates evidence}
\rightarrow
\text{Human accepts responsibility}
}
$$

所以 AI 第二設計師不是第二個獨裁者，而是第二個有能力說「不」的腦。

---

# 6. Consistency Audit

第一類審查是：

$$
\boxed{
\text{Consistency Audit}
}
$$

檢查：

- UI 描述與 runtime 是否一致；
- 設定與實際條件是否一致；
- 數值與公式是否一致；
- 劇情規則與玩法是否一致；
- 文件與程式是否一致。

因此：

$$
\boxed{
\text{Description}
\leftrightarrow
\text{Implementation}
}
$$

可以被持續比對。

---

# 7. Causal Audit

第二類審查問：

$$
\boxed{
\text{Who Reads It?}
}
$$

以及：

$$
\boxed{
\text{What Changes Because of It?}
}
$$

對每個變量：

$$
x_i
$$

追蹤：

$$
x_i
\rightarrow
\{y_1,y_2,\dots,y_n\}
$$

若：

$$
n=0
$$

則它可能只是：

$$
\boxed{
\text{Decorative State}
}
$$

而不是有意義的玩法變量。

---

# 8. Utility Audit

第三類審查直接問：

$$
\boxed{
\Delta U_{player}(F_i)
}
$$

也就是：

> 玩家為什麼在乎這個功能？

如果新增：

- 貨幣；
- stat；
- 聲望；
- crafting 素材；
- 派系；

但：

$$
\Delta U_{player}\approx0
$$

則它可能只是：

$$
\boxed{
\text{Feature Inflation}
}
$$

---

# 9. Counterfactual Audit

第四類審查不是問：

> 這功能能不能跑？

而是：

> 如果把它拿掉，會怎樣？

若：

$$
Product(F_i)
\approx
Product(\neg F_i)
$$

則：

$$
\boxed{
MFV(F_i)\approx0
}
$$

即其 Marginal Feature Value 接近零。

這是一個比「功能存在」更嚴格的設計測試。

---

# 10. Integration Audit

第五類審查把整個產品建成：

$$
G=(V,E)
$$

其中：

- $V$：系統、角色、資源、任務與狀態節點；
- $E$：有效依賴、讀寫、因果與回饋。

AI 可以尋找：

- orphan nodes；
- weakly connected components；
- dead ends；
- one-way dependencies；
- missing feedback loops。

這使：

$$
\boxed{
\text{Integration Debt}
}
$$

從抽象感覺變成可審核對象。

---

# 11. Global Design Diff

版本從：

$$
v_t
\rightarrow
v_{t+1}
$$

時，不只做程式 diff。

還應做：

$$
\boxed{
GDD(v_t,v_{t+1})
}
$$

也就是：

$$
\boxed{
\text{Global Design Diff}
}
$$

它回答：

> 這次修改在整體玩法上真正改變了什麼？

---

# 12. Local Change → Global Consequence

若一次 commit 只改：

$$
c_i
$$

AI 可以產生：

$$
\boxed{
\text{Expected Consequence Set}(c_i)
}
$$

例如：

> 修改了速度上限，可能影響角色成長、自訂零件價值、敵我命中率與某些 build 的有效性。

於是：

$$
\boxed{
\text{Local Code Change}
\rightarrow
\text{Global Test Targets}
}
$$

---

# 13. 第二設計師必須是 Permanent

真正重要的不是偶爾：

> 問 AI 一次。

而是：

$$
\boxed{
\text{Permanent Review Infrastructure}
}
$$

每個 milestone、RC、重大系統、balance patch 都重新審查。

如此：

$$
\text{Review}
$$

才從臨時活動變成生產流程的一部分。

---

# 14. Second-Designer Loop

本篇正式提出：

$$
\boxed{
\text{Design}
\rightarrow
\text{Implement}
\rightarrow
\text{AI Global Audit}
\rightarrow
\text{Human Review}
\rightarrow
\text{Revision}
}
$$

然後：

$$
\boxed{
\text{Repeat}
}
$$

這個 Loop 的核心不是自動化，而是：

$$
\boxed{
\text{制度化異議}
}
$$

---

# 15. 為什麼要制度化反對

隨著：

$$
SunkCost\uparrow
$$

創作者的：

$$
WillingnessToDelete\downarrow
$$

很自然。

因為：

> 這東西我做了三個月。

會偷偷變成：

> 所以它應該留下。

AI reviewer 可以比較不受這個心理成本影響，持續問：

> 它對產品的邊際價值是多少？

---

# 16. Blind Player Mode

一個非常重要的審查方式是：

$$
\boxed{
\text{Blind Player Mode}
}
$$

只讓 AI 看：

- UI；
- tutorial；
- 遊戲畫面；
- 玩家可見文字。

不提供：

- source code；
- 作者解釋；
- 隱藏設定。

然後問：

> 你能不能自己理解？

這測的是：

$$
\boxed{
\text{Product Self-Explanatory Capacity}
}
$$

---

# 17. White-Box Architect Mode

另一個極端：

$$
\boxed{
\text{White-Box Architect Mode}
}
$$

讓 AI 讀：

- source；
- data table；
- state machine；
- save format；
- event graph；
- formula。

再檢查：

$$
\boxed{
\text{Global Architecture}
}
$$

---

# 18. Black-Box × White-Box Cross Audit

若 Black-Box 認為某系統沒作用，但 White-Box 發現它實際有大量後台效果，問題可能是：

$$
\boxed{
\text{Visibility Failure}
}
$$

反過來，若玩家覺得它很重要，但 White-Box 發現根本沒有下游影響，則可能是：

$$
\boxed{
\text{Meaning Illusion}
}
$$

兩種模式交叉後，比單一測試更有價值。

---

# 19. Player-Model Diversity

第二設計師也不應只有一個 persona。

可以有：

$$
\text{Newbie},
\text{Min-Maxer},
\text{Roleplayer},
\text{Completionist},
\text{Speedrunner}
$$

並比較：

$$
U_k(F_i)
$$

其中 $k$ 是玩家類型。

因為：

$$
\boxed{
U_1(F_i)
\neq
U_2(F_i)
}
$$

---

# 20. Preference Surface

多個 persona 的結果可以形成：

$$
\boxed{
\mathcal{U}(F_i)
=
\{U_1,U_2,\dots,U_n\}
}
$$

也就是：

$$
\boxed{
\text{Preference Surface}
}
$$

它不是要求創作者迎合所有人，而是讓創作者知道：

> 這個選擇到底在服務誰，又犧牲了誰。

---

# 21. 第二設計師真正降低的是 Unconscious Choice

AI review 不可能消滅所有錯誤選擇。

但它可以降低：

$$
\boxed{
\text{Unconscious Choice}
}
$$

也就是：

> 創作者根本沒有發現自己已經做了這個取捨。

成熟設計最重要的是：

$$
\boxed{
\text{Conscious Trade-off}
}
$$

---

# 22. Assumption Externalization

創作者可能說：

> 玩家自然會知道。

AI 問：

> 為什麼？

創作者說：

> 這個資源後期有用。

AI 問：

> 哪個系統後期讀它？

創作者說：

> 這角色很重要。

AI 問：

> 哪個玩家決策因他而改變？

這個過程叫：

$$
\boxed{
\text{Assumption Externalization}
}
$$

---

# 23. Assumption Ledger

每個重大設計都可以記錄：

$$
\boxed{
A_i
=
(
\text{Assumption},
\text{Evidence},
\text{Test},
\text{Status}
)
}
$$

例如：

> 玩家會願意持續花錢升級裝備。

那就必須檢查：

- 收入曲線；
- 花費曲線；
- 免費替代品；
- 捕獲收益；
- 終局需求。

於是：

$$
\boxed{
\text{Design Belief}
\rightarrow
\text{Testable Hypothesis}
}
$$

---

# 24. Falsification-Oriented Design

很多設計流程問：

> 我要怎麼證明這東西很好？

更強的流程問：

$$
\boxed{
\text{What would prove this design wrong?}
}
$$

也就是：

$$
\boxed{
\text{Falsification-Oriented Design}
}
$$

AI 特別適合大量尋找反例。

---

# 25. Design Red Team

可以專門配置：

$$
\boxed{
\text{Design Red Team}
}
$$

任務是：

- 找 dominant strategy；
- 找 useless stat；
- 找假選擇；
- 找無效分支；
- 找可刪功能；
- 找 exploit；
- 找敘事斷裂；
- 找系統孤兒。

它不是要：

> 好好玩。

而是：

$$
\boxed{
\text{Break the Design Model}
}
$$

---

# 26. Builder、Reviewer、Judge 應該分開

若同一個 AI 剛寫完功能，又立即替自己評分，容易產生：

$$
\boxed{
\text{Self-Validation Bias}
}
$$

所以：

$$
\boxed{
\text{Builder}
\neq
\text{Reviewer}
}
$$

更完整：

$$
\boxed{
\text{Builder}
\rightarrow
\text{Reviewer}
\rightarrow
\text{Judge}
\rightarrow
\text{Human}
}
$$

其中人類保留最終責任。

---

# 27. 不同角色的 Objective 必須不同

Builder：

$$
\boxed{
\max Completion
}
$$

Reviewer：

$$
\boxed{
\max DefectDiscovery
}
$$

Judge：

$$
\boxed{
\max DecisionQuality
}
$$

若全部優化：

$$
\max Agreement
$$

那麼流程失去價值。

---

# 28. AI Reviewer 的核心輸出不是「100 個建議」

最有效的 reviewer 輸出應該是：

$$
\boxed{
\text{Issue}
\rightarrow
\text{Evidence}
\rightarrow
\text{Impact}
\rightarrow
\text{Counterexample}
\rightarrow
\text{Suggested Test}
}
$$

每個 issue 至少可以包含：

$$
\boxed{
(
\text{Severity},
\text{Evidence},
\text{AffectedSystems},
\text{Hypothesis},
\text{Test},
\text{Confidence}
)
}
$$

如此才能從「感覺怪」變成可執行審查。

---

# 29. Historical Design Memory

AI 第二設計師還有一個人類很難長期維持的功能：

$$
\boxed{
\text{Continuity}
}
$$

它可以讀：

- 舊 issue；
- changelog；
- regression test；
- design note；
- player feedback；
- commit history。

於是：

$$
\boxed{
\text{Past Failure}
\rightarrow
\text{Future Constraint}
}
$$

---

# 30. Solo Team 不再等於 Single Perspective

以前：

$$
1\text{ developer}
=
1\text{ active perspective}
$$

現在可以變成：

$$
\boxed{
1\text{ human}
+
N\text{ review perspectives}
}
$$

因此：

$$
\boxed{
\text{Solo Team}
\neq
\text{Single Perspective}
}
$$

這正是 AI 時代一人開發方法論最重要的結構變化之一。

---

# 31. 第二設計師不只適用於遊戲

在小說：

$$
\boxed{
\text{Narrative Integration Audit}
}
$$

可以問：

> 動機是否一致？伏筆是否回收？刪掉這章主線會不會改變？

在軟體：

$$
\boxed{
\text{Architectural Integration Audit}
}
$$

可以問：

> 這個設定誰讀？API 是否重複？哪個 invariant 被破壞？

在研究：

$$
\boxed{
\text{Epistemic Integration Audit}
}
$$

可以問：

> 命題依賴什麼假設？是否有反例？這個定義後文真的使用了嗎？

---

# 32. 第二設計師必須被允許反對

如果 AI 的角色只是：

> 這個想法很棒。

它不是 reviewer。

第二設計師模式需要：

$$
\boxed{
\text{Disagreement Permission}
}
$$

也就是：

- 可以說不；
- 可以要求證據；
- 可以主張刪除；
- 可以提出反例；
- 可以指出人類偏誤。

---

# 33. 但 AI 也不能成為第二獨裁者

AI 可能：

- 不理解藝術意圖；
- 偏向常見方案；
- 過度平均化；
- 誤判極端創作；
- 對長期設計理解不足。

所以：

$$
\boxed{
\text{AI Review}
\neq
\text{AI Authority}
}
$$

最成熟的模式是：

$$
\boxed{
\text{AI supplies dissent; human owns the choice.}
}
$$

---

# 34. AI 第二設計師是一種 Meta-Tool

一般工具：

$$
Tool
\rightarrow
Artifact
$$

第二設計師：

$$
\boxed{
Tool
\rightarrow
\text{Better Decisions About Artifacts}
}
$$

因此它不是單純 production tool，而是：

$$
\boxed{
\text{Meta-Tool}
}
$$

它提升的是：

$$
\boxed{
\text{Decision Quality}
}
$$

---

# 35. 生產力提升後，Decision Quality 變成瓶頸

當：

$$
ProductionCost\downarrow
$$

且：

$$
ProductionCapacity\uparrow
$$

真正更重要的問題逐漸從：

$$
\text{Can It Be Built?}
$$

轉成：

$$
\boxed{
\text{What Should Be Built?}
}
$$

這也意味著：

$$
\boxed{
\text{Decision Quality}
}
$$

會成為 AI 時代創作的核心稀缺資源之一。

---

# 36. 第二設計師與 Human-Retro 的關係

如果 AI 可以：

- 生成；
- 寫程式；
- 測試；
- 分析；
- 反對；

那人類作者真正留下的東西越來越接近：

$$
\boxed{
\text{Final Selection}
}
$$

也就是：

> 我看過很多可能性與反對意見，但為什麼最後仍然選這一條？

因此第二設計師不必削弱人類作者性。

它反而可以強化：

$$
\boxed{
\text{Human Authorial Responsibility}
}
$$

---

# 37. 更多 AI 參與，不必然等於更少作者性

若人類仍然：

$$
\boxed{
\text{Defines Goals}
}
$$

$$
\boxed{
\text{Chooses Constraints}
}
$$

$$
\boxed{
\text{Reviews Alternatives}
}
$$

$$
\boxed{
\text{Accepts Responsibility}
}
$$

那麼：

$$
\boxed{
\text{High AI Participation}
}
$$

可以與：

$$
\boxed{
\text{High Human Authorial Control}
}
$$

同時成立。

---

# 38. AI 第二設計師開始擴張選擇底空間

沒有第二視角時，很多道路：

> 你根本沒想到。

有 AI reviewer 後：

$$
\mathfrak B
=
\text{Choice Space}
$$

可能被擴大。

因此：

$$
\boxed{
\mathfrak B_{\text{with review}}
\supset
\mathfrak B_{\text{without review}}
}
$$

而人類真正做的事情變成：

$$
\boxed{
\text{Select from a Larger Choice Space}
}
$$

這已經開始接近本系列最後的「選擇底空間」問題。

---

# 39. 但更大的選擇空間需要壓縮

如果：

$$
|\mathfrak B|\uparrow
$$

也會帶來：

$$
\boxed{
\text{Choice Overload}
}
$$

因此 AI 第二設計師還必須會：

$$
\boxed{
\text{Rank}
+
\text{Compress}
+
\text{Explain}
}
$$

而不是無限制生成建議。

---

# 40. 系列中的位置

第五篇指出：

$$
\boxed{
\text{Feature Growth}
>
\text{Integration Growth}
}
$$

會形成 Integration Debt。

第六篇回答：

$$
\boxed{
\text{如何增加持續的 Integration Review？}
}
$$

答案之一是：

$$
\boxed{
\text{AI as Permanent Second Designer}
}
$$

下一篇將把第二設計師進一步擴張成多角色組織：

# **《一人團隊不再等於一個腦袋：Agentic Development》**

---

# 41. 結論

AI 最容易被看見的能力是：

$$
\boxed{
\text{Generate}
}
$$

但當生成能力逐漸商品化，更稀缺的能力可能是：

$$
\boxed{
\text{Review}
}
$$

以及：

$$
\boxed{
\text{Disagree}
}
$$

因此：

$$
\boxed{
\text{AI 最重要的價值之一，不是替創作者做更多。}
}
$$

而是：

$$
\boxed{
\text{替創作者持續看到自己看不到的地方。}
}
$$

成熟的 AI 協作流程也不應只是：

$$
\text{Human Prompt}
\rightarrow
\text{AI Output}
$$

而更接近：

$$
\boxed{
\text{Human Intent}
\rightarrow
\text{AI Alternatives}
\rightarrow
\text{AI Critique}
\rightarrow
\text{Human Selection}
\rightarrow
\text{AI Verification}
\rightarrow
\text{Human Responsibility}
}
$$

這意味著，AI 時代真正稀缺的人類能力，正在從：

> 能不能自己把所有事情做完。

轉向：

$$
\boxed{
\text{能不能在大量可能性、反對意見與替代方案之中，仍然知道自己為什麼選這一條。}
}
$$

因此，第二設計師並不必然削弱人類作者。

如果使用得當，它反而迫使人類：

$$
\boxed{
\text{更清楚地成為作者。}
}
$$
