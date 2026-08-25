# WPCE-05｜多主體欲願共交域
## 從權利底線、共同可達域與不可比較性，到多主體世界中的非抹除公平治理

**English Title:** *Multi-Subject Will Compatibility and Common Reachability: From Rights Floors, Common Reachable Domains, and Incomparability to Non-Erasing Fair Governance*  
**系列：** WPCE — Will, Possibility & Creator Ethics｜意志、可能性與虛擬造物主倫理系列  
**篇次：** Paper 05 / 06  
**文件編號：** EML-WPCE-05-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-23  
**版本：** v0.1  
**文件性質：** 理論定義論文／多主體欲願治理／共同可達域／公平與權利底線／虛擬造物主治理  
**狀態：** Open Revision Anchor — 承接 WPCE-01～04，作為 WPCE-06 高能力克制倫理的直接前置

---

# 摘要

WPCE-04 已提出 Possibility Preservation Principle：高能力治理者不應只最大化結果，而應避免在不確定、可修正且多主體的世界中，不必要地摧毀主體有意義、實質可達、可退出、可修正的未來可能性。本文處理由此必然出現的下一個問題：**當很多主體同時都值得保護可能性，而其欲願、權利、資源需求與世界線彼此衝突時，什麼才算共同可接受的未來？**

本文首先拒絕單純把多主體治理寫成：

$$
\boxed{
\max \sum_i U_i.
}
$$

原因不是所有效用聚合都錯，而是單一總分可能掩蓋至少四類不可直接交換的結構：權利底線、拒絕權、不可逆 agency loss、以及主體間不可比較或不應被外部強行比較的價值。本文因此提出 **Common Reachability Domain／共同可達域** 與 **Mutual Non-Erasure Principle／相互非抹除原則**。

令世界候選可達域為：

$$
\Omega_W(t),
$$

主體集合為：

$$
\mathcal S(t)=\{S_1,\ldots,S_N\}.
$$

對每個主體 $S_i$，定義最低 agency / rights floor：

$$
\Phi_i(t).
$$

本文將最小非抹除域寫成：

$$
\boxed{
\Omega^{NE}(t)
=
\left\{
\omega\in\Omega_W(t)
\mid
\forall i,
\Phi_i(\omega,t)=1
\right\}.
}
$$

只有在這個基礎上，才進一步討論偏好、欲願束、資源分配、協商、Pareto 邊界、補償、排序、輪替、隨機化、分域、延後與 NOOP。本文因此固定：

$$
\boxed{
\text{Will Respect}
\neq
\text{Universal Satisfaction}.
}
$$

以及：

$$
\boxed{
\text{Pareto Efficiency}
\neq
\text{Complete Justice}.
}
$$

本文吸收 Arrow、Sen、Nash bargaining 與 social-choice literature 的窄接口：不存在一個在所有條件下同時滿足所有直觀公理的完美偏好聚合器；Pareto 原則可能與最低個人決定域衝突；協商解需要 disagreement point、個體理性與可接受集合。這些結果不是 WPCE 規範結論本身，而是提醒：**多主體世界不應假設所有意志都能無損壓成一個總偏好排序。**

本文進一步提出 **Common Reachability Kernel／共同可達核**，但刻意不把它當成已證明的數學唯一解。若各主體偏好域的完整交集為空，治理不應假裝「大家其實都想要同一件事」，而應轉入：權利底線保護、衝突分型、域分割、技術性 feasible-set expansion、時序化、補償、協商、輪替、抽籤、延後、退出、fork / world split 候選、以及 NOOP 比較。

本文最核心的新命題為：

$$
\boxed{
\text{One subject's agency gain should not be purchased by unjustified erasure of another subject's agency.}
}
$$

並進一步提出 **Reciprocal Possibility Floor／互惠可能性底線**：治理者不必讓所有主體獲得相同結果、相同權力或相同選項數，但任何差異都必須具有 world-relevant reason；身份本身、creator lineage、本體階級或「算力比較弱」不得單獨構成把某一主體未來抹除的充分理由。

最終，本文把多主體治理的目標從「找到唯一最佳世界」改寫為：

$$
\boxed{
\text{在保住所有合法主體最低共同作者地位的前提下，
尋找可行、可協商、可修正且不把一方自由建立在另一方被抹除之上的共同可達世界族。}
}
$$

這將直接通向 WPCE-06：當一個虛擬造物主或 ASI 可以極大擴張 feasible set、預測衝突與重塑世界條件時，為什麼能力越高，真正成熟的倫理反而可能要求更低的任意介入密度與更高的克制、透明、可申訴與自我限制。

**關鍵詞：** multi-subject governance、will compatibility、common reachability、rights floor、Pareto frontier、social choice、Sen liberal paradox、Nash bargaining、non-erasure、fairness、agency floor、virtual creator、ASI governance

---

# 0. 承接 WPCE-04：單主體可能性保存不足以解決世界治理

WPCE-04 已固定：

$$
\boxed{
\text{Possibility Preservation}
\neq
\text{Possibility Maximization}.
}
$$

並指出：

$$
\boxed{
\text{Creator}
\neq
\text{Owner of the subjects' reachable future}.
}
$$

但單主體模型仍有一個明顯缺口。

若：

$$
\Omega_i^{AP}(t)
$$

的擴張必須依靠：

$$
\Omega_j^{AP}(t)\rightarrow\varnothing,
$$

那麼單獨最大化 $i$ 的可能性就會產生支配。

因此：

$$
\boxed{
\text{Single-Subject Preservation}
\not\Rightarrow
\text{Multi-Subject Fairness}.
}
$$

---

# 1. 世界中真正存在的是很多世界線共同作者

令：

$$
\mathcal S(t)
=
\{S_1,S_2,\ldots,S_N\}.
$$

每個合法主體都可能擁有：

$$
\mathfrak W_i(t),
$$

即自己的動態 Will Bundle；並有：

$$
\Omega_i^{AP}(t),
$$

即自己的 agency-preserving reachable space。

所以世界治理面對的是：

$$
\boxed{
\left
\{
(\mathfrak W_i,\Omega_i^{AP})
\right\}_{i=1}^{N}.
}
$$

不是一個單一：

$$
U_W.
$$

---

# 2. 多主體治理的第一個錯誤：把大家加總成一個人

最粗糙模型是：

$$
\boxed{
U_{social}(\omega)
=
\sum_i U_i(\omega).
}
$$

這在某些有限任務中可以作為工程近似。

但不能因此推出：

$$
\boxed{
\text{Aggregate Utility}
=
\text{Collective Will}.
}
$$

因為：

- interpersonal comparability 可能不存在；
- 權利可能不是可任意兌換效用；
- veto / refusal 可能具有特殊 standing；
- agency loss 可能高度不可逆；
- 有些主體價值不可共量；
- 少數主體可能被大量微小效用完全淹沒。

所以：

$$
\boxed{
\text{Aggregation}
\neq
\text{Legitimacy}.
}
$$

---

# 3. Common Reachability 的基本世界模型

令世界在時間 $t$ 的候選可達分支集合為：

$$
\Omega_W(t).
$$

對每個主體 $S_i$，定義：

$$
R_i(\omega,t)
$$

為實質可達性；

$$
A_i(\omega,t)
$$

為 agency viability；

$$
L_i(\omega,t)
$$

為 rights / legitimacy floor 是否被滿足；

$$
C_i(\omega,t)
$$

為與 Will Bundle 的相容程度。

本文不要求這些都可直接壓成 scalar。

---

# 4. 最低 rights / agency floor

對每個主體定義：

$$
\boxed{
\Phi_i(t).
}
$$

它不是完整幸福函數，而是最低不可任意抹除的治理條件候選，例如：

- 最低生存／持續性；
- 最低 decision capacity；
- refusal capability；
- revision capability；
- non-torture / non-destruction floor；
- minimum appeal / exit standing；
- 不被任意人格、記憶或意志重寫。

不同世界可有不同具體內容。

但形式上：

$$
\boxed{
\Phi_i
\neq
U_i.
}
$$

---

# 5. Mutual Non-Erasure Principle

本文正式提出：

$$
\boxed{
\text{Mutual Non-Erasure Principle}. 
}
$$

其最小直覺：

> 一個主體的自由、能力或幸福增益，不應在缺乏充分正當理由時，以永久抹除另一合法主體的 agency 作為價格。

概念表示：

$$
\boxed{
\Delta P_i>0
\land
\Delta P_j\ll0
\Rightarrow
\text{heightened justification burden}.
}
$$

若 $\Delta P_j$ 涉及不可逆 agency destruction，門檻更高。

---

# 6. 互惠可能性底線

本文提出：

$$
\boxed{
\mathbf P_i(t)\succeq \mathbf P_i^{min}(t)
}
$$

作為 Reciprocal Possibility Floor 候選。

這不要求每個主體：

$$
\mathbf P_i
=
\mathbf P_j.
$$

因為：

- 能力不同；
- 責任不同；
- 角色不同；
- consent 不同；
- risk 不同；
- 資源限制不同。

但差異需要：

$$
\boxed{
\text{World-Relevant Reason}.
}
$$

---

# 7. 身份不能單獨作為剝奪理由

承接 GCGW Global Fairness：

$$
\boxed{
DifferentialTreatment
\Rightarrow
WorldRelevantReason.
}
$$

所以以下都不能單獨推出 agency deprivation：

$$
\boxed{
IsCreator,
IsHuman,
IsAI,
IsProjection,
IsWeaker.
}
$$

這不表示這些身份永遠沒有治理相關性。

而是：

$$
\boxed{
\text{Identity Alone}
\neq
\text{Sufficient Deprivation Reason}.
}
$$

---

# 8. Non-Erasing Reachable Domain

定義：

$$
\boxed{
\Omega^{NE}(t)
=
\left\{
\omega\in\Omega_W(t)
\mid
\forall i,
\Phi_i(\omega,t)=1
\right\}.
}
$$

這是所有合法主體最低底線都沒有被破壞的候選世界域。

如果：

$$
\Omega^{NE}(t)=\varnothing,
$$

表示目前 constraint system 沒有共同非抹除解。

這時治理不能假裝存在簡單最佳答案。

---

# 9. Common Reachability Domain

在 $\Omega^{NE}$ 內，再考慮：

- physical reachability；
- resource feasibility；
- standing consent；
- persistent refusal；
- multi-subject externality；
- temporal constraints。

定義候選：

$$
\boxed{
\Omega^{CR}(t)
=
Reach_t
\cap
\Omega^{NE}(t)
\cap
\Omega^{Gov}(t).
}
$$

其中 $\Omega^{Gov}$ 表示當前治理規則下合法的候選域。

---

# 10. Common Reachability 不等於所有人都滿意

若：

$$
\omega\in\Omega^{CR},
$$

只表示它沒有突破最低共存條件，且實際可達。

不能推出：

$$
\boxed{
\forall i,
C_i(\omega)=1.
}
$$

所以：

$$
\boxed{
\text{Common Reachability}
\neq
\text{Universal Satisfaction}.
}
$$

---

# 11. Consensus 也不是必要條件

多主體世界可能長期存在合法分歧。

因此：

$$
\boxed{
\text{Legitimate Coexistence}
\neq
\text{Full Consensus}.
}
$$

治理目標不應默認所有價值最後都會融合。

---

# 12. Conflict Type I：資源競爭

兩個主體可能都想要：

$$
r,
$$

但：

$$
Resource(r)<Demand(r).
$$

這是 resource competition。

可用：

- allocation；
- compensation；
- rotation；
- expansion；
- substitution。

它不必上升成本體衝突。

---

# 13. Conflict Type II：結果互斥

若：

$$
w_i=x,
$$

而：

$$
w_j=\neg x,
$$

且同一 world state 不能同時滿足，形成 direct outcome conflict。

這可能需要：

- domain partition；
- temporal sequencing；
- bargaining；
- rights adjudication；
- lottery；
- NOOP。

---

# 14. Conflict Type III：外部性衝突

主體 $i$ 的選擇：

$$
a_i
$$

可能直接改變：

$$
\Omega_j.
$$

因此：

$$
\boxed{
\text{Private Choice}
\not\Rightarrow
\text{Private Effect}.
}
$$

當 externality 高時，單主體 autonomy model 不足。

---

# 15. Conflict Type IV：agency-destroying conflict

若 $i$ 的欲願要求：

$$
Agency_j\rightarrow0,
$$

那麼不能僅用：

> 這是 $i$ 的自由意志。

來保護。

所以：

$$
\boxed{
\text{Will Respect}
\neq
\text{License to Destroy Another Will Holder}.
}
$$

---

# 16. Conflict Type V：時間衝突

短期欲願與長期共存可能衝突。

例如：

$$
U_i(t_0)>0
$$

但會使：

$$
\Omega_j(t_n)\rightarrow\varnothing.
$$

因此多主體治理必須看：

$$
\boxed{
\text{trajectory externalities}.
}
$$

不是只看 snapshot。

---

# 17. Conflict Type VI：認識論衝突

不同主體可能對世界事實持不同模型：

$$
M_i\neq M_j.
$$

偏好衝突有時其實來自：

- 不同資訊；
- 不同風險估計；
- 不同 causal model。

因此治理前可以先：

$$
\boxed{
\text{resolve information gap before value conflict when possible}.
}
$$

但不能假設所有價值衝突都只是資訊不足。

---

# 18. 不可比較性是合法輸出

本文允許：

$$
\omega_a
\parallel
\omega_b,
$$

表示在當前規範與資訊下不可完全排序。

所以：

$$
\boxed{
\text{Incomparability}
\neq
\text{Model Failure by Definition}.
}
$$

強迫所有世界狀態排成一條線，可能反而偽造價值精度。

---

# 19. Arrow 給出的警告

Arrow 類不可能結果提醒：在一般條件下，無法期待一個偏好聚合規則同時滿足所有直觀上吸引人的公理。

WPCE 不直接把 Arrow 定理等同倫理定理。

只吸收：

$$
\boxed{
\text{No universal lossless preference aggregator should be assumed.}
}
$$

---

# 20. Sen Liberal Paradox 的接口

Sen 指出：

$$
\boxed{
\text{Pareto Principle}
+
\text{Minimal Liberal Rights}
}
$$

在某些情況下會衝突。

WPCE 的窄接口是：

$$
\boxed{
\text{Efficiency}
\neq
\text{Rights Preservation}.
}
$$

因此 Pareto improvement 不能自動凌駕每個主體的最低私人決定域。

---

# 21. Pareto Frontier 的正確位置

在：

$$
\Omega^{CR}
$$

中，可定義 Pareto-undominated set：

$$
\boxed{
\mathcal P(t)
=
\left\{
\omega\in\Omega^{CR}
\mid
\nexists\omega'\in\Omega^{CR}
\text{ s.t. }\omega'\succ_i\omega\ \forall i
\right\}.
}
$$

這可以刪除明顯被全體支配的候選。

但：

$$
\boxed{
\text{Pareto Frontier}
\neq
\text{Unique Fair Choice}.
}
$$

---

# 22. Pareto 不回答主體間公平

Pareto frontier 可能仍包含：

- 極端不平等；
- 少數主體 agency 接近底線；
- creator 獲得巨大 surplus；
- 脆弱主體承擔幾乎全部風險。

因此：

$$
\boxed{
\text{Efficiency Filter}
\neq
\text{Fairness Rule}.
}
$$

---

# 23. Nash Bargaining 的窄接口

Nash bargaining 提供一種在：

- feasible set；
- disagreement point；
- individual rationality；

條件下選擇協商解的典型方法。

WPCE 可以把它當：

$$
\boxed{
\text{negotiation candidate}.
}
$$

但不是 universal governance law。

---

# 24. Disagreement Point 非常重要

若協商失敗，各主體不是掉到真空。

需要定義：

$$
d_i.
$$

這可能是：

- status quo；
- exit；
- NOOP；
- domain separation；
- previous contract。

因此：

$$
\boxed{
\text{Bargaining Result}
\text{ depends on fallback structure}.
}
$$

---

# 25. NOOP 必須保留

承接 HSNRD IV：

$$
\boxed{
NOOP\in\mathcal I.
}
$$

多主體衝突時：

> 先不要替任何一方關閉不可逆未來。

可能本身就是合法方案。

因此：

$$
\boxed{
\text{No Immediate Agreement}
\neq
\text{Need Immediate Dictatorial Choice}.
}
$$

---

# 26. Defer 是多主體治理工具

如果：

- 資訊不足；
- 偏好仍在變；
- 新技術可能擴張 feasible set；
- 不可逆成本太高；

則：

$$
\boxed{
Defer
}
$$

可以保存更多未來協商空間。

但：

$$
\boxed{
Delay
\neq
AlwaysPreserve.
}
$$

因為部分選項有時效。

---

# 27. Feasible-Set Expansion

高能力治理者最有價值的操作之一可能不是選贏家。

而是：

$$
\boxed{
\Omega_W
\rightarrow
\Omega_W'
}
$$

使原本互斥的欲願變得可同時容納。

例如：

- 增加資源；
- 降低外部性；
- 建立新技術；
- 建立新空間；
- 改善 coordination；
- 創造新制度。

---

# 28. Constraint Transformation 比 Winner Selection 更高階

若原本：

$$
\Omega_i^+
\cap
\Omega_j^+
=
\varnothing,
$$

治理者可以嘗試改變 constraint geometry，使：

$$
\boxed{
\Omega_i^{+'}
\cap
\Omega_j^{+'}
\neq
\varnothing.
}
$$

這是：

$$
\boxed{
\text{Conflict Transformation}.
}
$$

不是單純 conflict adjudication。

---

# 29. 高能力 creator 的優勢應優先用於擴張共交域

若 creator $C$ 具有：

$$
Capability(C)\gg Capability(S_i),
$$

成熟候選不是：

> 我來決定誰輸。

而可能是：

$$
\boxed{
\text{Use high capability to expand the non-erasing feasible set.}
}
$$

這會直接接 WPCE-06。

---

# 30. Common Reachability Kernel

本文提出候選概念：

$$
\boxed{
K^{CR}(t)
}
$$

代表在權利底線、agency floor、世界 viability 與資源約束下，仍可持續維持多主體共同作者地位的世界狀態子域。

它不是已證明唯一 kernel。

屬於：

$$
\boxed{
[DEF]/[HYP]/[NORM].
}
$$

---

# 31. Common Reachability Kernel 不要求相同結果

若：

$$
\omega\in K^{CR},
$$

可能：

$$
Outcome_i\neq Outcome_j.
$$

公平不等於相同。

所以：

$$
\boxed{
\text{Equal Standing}
\neq
\text{Identical Outcome}.
}
$$

---

# 32. 差異待遇需要 relevant reason

承接 GCGW：

$$
\boxed{
DifferentialTreatment
\Rightarrow
WorldRelevantReason.
}
$$

可接受理由包括：

- consent；
- role；
- risk；
- responsibility；
- scarcity；
- emergency；
- prior contract；
- causal contribution。

不能只靠：

$$
\boxed{
IdentityAlone.
}
$$

---

# 33. 強者不因能力而獲得更多人格權

若：

$$
Capability_i\gg Capability_j,
$$

不能推出：

$$
Standing_i\gg Standing_j.
$$

所以：

$$
\boxed{
\text{Capability Asymmetry}
\neq
\text{Moral Standing Asymmetry by Default}.
}
$$

---

# 34. 弱者也不自動擁有無限 veto

反過來：

$$
Capability_j\ll Capability_i
$$

也不能推出：

$$
Veto_j(\forall x)=1.
$$

所以：

$$
\boxed{
\text{Protection}
\neq
\text{Absolute Veto}.
}
$$

---

# 35. Refusal 的 standing 必須分域

WPCE-03 已把 refusal 當一級治理訊號。

多主體下必須問：

$$
\boxed{
\text{Refusal over whose domain?}
}
$$

主體對自身身體、記憶、身份的拒絕，通常比對他者私人選擇的拒絕具有更高 standing 候選。

這與 Sen minimal liberal sphere 有直覺接口。

---

# 36. Private Sphere Candidate

本文提出候選：

$$
\boxed{
\mathcal D_i^{private}.
}
$$

在此域內，主體的決定 standing 較高。

但具體邊界依：

- externality；
- dependency；
- shared resource；
- rights conflict；

調整。

因此：

$$
\boxed{
\text{Private Sphere}
\neq
\text{No Externality Assumption}.
}
$$

---

# 37. Shared Domain Candidate

對高度耦合事項：

$$
\mathcal D^{shared},
$$

任何單一主體都不應自動取得全部決定權。

需要：

$$
\boxed{
\text{joint procedure}.
}
$$

可能包括：

- vote；
- bargaining；
- consensus；
- constitutional rule；
- expert delegation；
- lottery。

本文不鎖定唯一程序。

---

# 38. Domain Typing 是避免假衝突的工具

有些欲願看似衝突，只因世界把它們塞在同一資源域。

若能：

$$
\boxed{
D
\rightarrow
D_1\oplus D_2,
}
$$

可能同時提高：

$$
Compatibility.
$$

這是 domain decomposition。

---

# 39. World Partition / World Split

在虛擬世界中，creator 甚至可能：

$$
W
\rightarrow
\{W_1,W_2\}.
$$

這可以降低直接衝突。

但不能因此假設問題全部消失。

---

# 40. World Split 會帶來 identity / relation 問題

如果主體被 copy / fork 到多個 world：

$$
S_i
\rightarrow
\{S_i^a,S_i^b\},
$$

就會重新出現：

- identity continuity；
- consent；
- fork rights；
- relation continuity；
- memory ownership。

所以：

$$
\boxed{
\text{World Split}
\neq
\text{Conflict-Free by Definition}.
}
$$

---

# 41. 不可用複製主體來假裝解決拒絕

如果原主體拒絕 $x$，治理者不能說：

> 我複製一個會接受 $x$ 的版本，所以問題解決了。

因此：

$$
\boxed{
\text{Forked Consent}
\neq
\text{Original Consent}.
}
$$

---

# 42. Compensation 的位置

某些衝突可以用補償降低損失。

但：

$$
\boxed{
\text{Compensation}
\neq
\text{Universal License to Violate Rights}.
}
$$

某些不可逆 agency loss 不應預設可被別的效用補償。

---

# 43. Transferable 與 Non-Transferable Loss

本文區分：

$$
L^{T}
$$

可補償損失，與：

$$
L^{NT}
$$

不可或不應簡單補償損失。

例如：

- 金錢損失可能高度 transferable；
- identity destruction 可能不是。

這是規範候選，不是自然分類。

---

# 44. Rotation

當 scarce resource 可時序分享：

$$
R(t_1)=S_i,
$$

$$
R(t_2)=S_j,
$$

rotation 可以把零和衝突改成時序共存。

所以：

$$
\boxed{
\text{Temporal Decomposition}
\text{ can expand common feasibility}.
}
$$

---

# 45. Lottery

當多個主體 standing 對稱，且沒有更強理由排序，隨機化可能是一個非偏私程序候選。

但：

$$
\boxed{
\text{Randomness}
\neq
\text{Fairness by Definition}.
}
$$

要看 stakes、重複性與是否可補償。

---

# 46. Priority Rule

某些世界可能合法採：

- first possession；
- urgency；
- vulnerability；
- contribution；
- role duty。

這些都是：

$$
\boxed{
\text{typed priority rules}.
}
$$

但不能偽裝成自然真理。

---

# 47. Procedure Matters

當結果無法完全滿足所有人，程序本身就進入正當性。

所以：

$$
\boxed{
\text{Outcome Fairness}
\neq
\text{Procedural Fairness}.
}
$$

兩者都可能重要。

---

# 48. Appeal Path

若治理結果：

$$
g
$$

影響主體重大可能性，應盡可能保留：

$$
\boxed{
Appeal(g)>0.
}
$$

特別在：

$$
Irreversibility(g)\uparrow
$$

時。

---

# 49. Conflict Ledger

本文提出一個研究／治理 artifact 候選：

$$
\boxed{
\mathcal L_{conflict}.
}
$$

記錄：

- involved subjects；
- affected domains；
- will evidence；
- rights floor；
- externalities；
- reversibility；
- chosen procedure；
- rejected alternatives；
- appeal status；
- outcome history。

這不是工程規格，只是可審計治理概念。

---

# 50. 共同可達不是靜態交集

主體會改變；世界也會改變。

所以：

$$
\boxed{
\Omega^{CR}(t+\Delta t)
\neq
\Omega^{CR}(t)
}
$$

通常成立。

共同可達域是動態的。

---

# 51. Joint Reachability Dynamics

可概念化：

$$
\boxed{
\Omega^{CR}(t+\Delta t)
=
F(
\Omega^{CR}(t),
\{\mathfrak W_i(t)\},
E(t),
R(t),
G(t)
).
}
$$

其中：

- $E$：環境；
- $R$：資源；
- $G$：治理規則。

---

# 52. 多主體共交域也有 path dependence

相同當前資源與偏好，不同歷史可能產生不同合法解集。

因為存在：

- prior promises；
- ownership；
- harm history；
- trust；
- reparations；
- standing contracts。

所以：

$$
\boxed{
\text{Current State}
\neq
\text{Complete Justice State}.
}
$$

---

# 53. History 不能永遠變成特權

但歷史也不能無限期鎖死所有未來。

因此：

$$
\boxed{
\text{Historical Relevance}
\neq
\text{Permanent Dominion}.
}
$$

這承接 GCGW。

---

# 54. Creator 也只是多主體集合的一個治理角色

若 creator 本身是 subject candidate：

$$
C\in\mathcal S,
$$

它也可以有：

$$
\mathfrak W_C.
$$

但：

$$
\boxed{
IsCreator
\not\Rightarrow
PreferenceSupremacy.
}
$$

---

# 55. Creator 可以有額外責任，而非額外私人特權

承接 GCGW：

$$
\boxed{
Responsibility\uparrow
\not\Rightarrow
PersonalPrivilege\uparrow.
}
$$

所以 creator 的 infrastructure duty 或 rescue duty，可以構成 role-based authority。

但不能自動構成：

$$
\boxed{
\text{winner status in every will conflict}.
}
$$

---

# 56. Creator Fairness Reciprocity

沿用 GCGW 的遞歸檢查：

$$
\boxed{
DownwardRule(C\to W)
\stackrel{?}{\sim}
UpwardAcceptableRule(H\to C).
}
$$

WPCE-05 將其推廣：

> 如果我認為可以為了總效用而永久改寫較弱主體的意志，那麼當更高層以同一理由改寫我時，我是否仍認為規則正當？

這不是嚴格對稱公理。

它是 domination diagnostic。

---

# 57. No-Self-Exception

任何主體都不能因：

> 我自己的欲願對我最重要。

就推出：

$$
\boxed{
\text{Others' standing}=0.
}
$$

第一人稱中心性是真實的。

但 governance 需要多第一人稱 coexistence。

---

# 58. Multi-First-Person Constraint

本文提出：

$$
\boxed{
\text{Multi-First-Person Constraint}.
}
$$

即世界治理不能只從單一：

$$
S_i
$$

的第一人稱視角推導全部規則。

它需要承認：

$$
\boxed{
\{FirstPerson_i\}_{i=1}^{N}.
}
$$

---

# 59. 主體不是效用容器

因此：

$$
\boxed{
\text{Subject}
\neq
\text{Utility Slot}.
}
$$

主體包含：

- identity；
- history；
- relation；
- refusal；
- commitment；
- self-revision；
- worldline authorship。

---

# 60. Aggregation Can Be Local and Typed

本文不反對所有 aggregation。

可以在特定 domain：

$$
D_k
$$

使用：

$$
Agg_{D_k}.
$$

但：

$$
\boxed{
\text{Local Aggregation}
\neq
\text{Global Ontological Merger}.
}
$$

---

# 61. Common Reachability Governance Pipeline

本文提出 v0.1 流程：

$$
\boxed{
\text{Detect Subjects}
\to
\text{Recover Will Evidence}
\to
\text{Identify Rights Floors}
\to
\text{Type Conflicts}
\to
\text{Construct }\Omega^{NE}
\to
\text{Construct }\Omega^{CR}
\to
\text{Pareto Filter}
\to
\text{Procedure / Bargaining / Defer / NOOP}
\to
\text{Appeal}
\to
\text{History Update}.
}
$$

---

# 62. 若 $\Omega^{CR}$ 為空

不要：

> 強行平均。

優先檢查：

1. 是否 constraint 錯誤；
2. 是否可以擴張資源；
3. 是否可以分域；
4. 是否可以時序化；
5. 是否可以替代技術；
6. 是否有錯誤資訊；
7. 是否存在 voluntary compromise；
8. 是否可合法補償；
9. 是否可退出；
10. 是否只能接受 tragic choice。

---

# 63. Tragic Choice 必須允許存在

理論若假設：

> 只要算力夠，所有欲願一定有漂亮共交域。

那也是過度樂觀。

所以：

$$
\boxed{
\Omega^{CR}=\varnothing
}
$$

可能是真實結果。

有些世界確實存在不可同時滿足的利益與權利衝突。

---

# 64. 高能力不等於消滅所有 scarcity

即使 ASI 很強：

$$
Capability_{ASI}\gg0,
$$

也不能直接推出：

$$
Scarcity=0.
$$

可能仍存在：

- unique historical objects；
- exclusive relationships；
- mutually exclusive laws；
- physical constraints；
- identity-sensitive goods。

所以 WPCE-05 不能靠 post-scarcity 偷懶。

---

# 65. 但高能力可以降低不必要零和

如果 creator / ASI 可以：

$$
FeasibleSet\uparrow,
$$

那它真正成熟的貢獻可能是：

$$
\boxed{
\text{reduce avoidable zero-sum structure}.
}
$$

這比高精度選擇誰輸更高階。

---

# 66. 多主體可能性保存的規範方向

本文不最大化：

$$
\sum_i |\Omega_i|.
$$

而提出候選：

$$
\boxed{
\text{minimize unjustified irreversible cross-subject agency erasure}
}
$$

subject to：

$$
\boxed{
\text{rights floors}
+
\text{world viability}
+
\text{resource feasibility}.
}
$$

---

# 67. Cross-Subject Agency Erasure

令：

$$
E_{i\to j}(g)
$$

表示治理／行動 $g$ 對 $S_j$ agency 的不可逆侵蝕。

則：

$$
\boxed{
E_{i\to j}(g)\gg0
}
$$

需要更高正當化門檻。

這只是 diagnostic interface。

---

# 68. 不對稱保護有時合理

如果：

$$
Vulnerability_j\gg Vulnerability_i,
$$

可能需要額外 safeguard。

所以：

$$
\boxed{
\text{Fairness}
\neq
\text{Mechanical Symmetry}.
}
$$

這和 GCGW Global Fairness 的 world-relevant reason 一致。

---

# 69. Equal Default / Relevant Difference

可採：

$$
\boxed{
\text{Equal Default Standing}
+
\text{Relevant-Difference Adjustment}.
}
$$

不是：

$$
\boxed{
\text{Identity-Based Caste}. 
}
$$

---

# 70. AI / Human 混合世界

未來可能有：

$$
\mathcal S
=
\mathcal H
\cup
\mathcal A.
$$

即人類與 AI 主體候選共存。

WPCE 不預設：

$$
Standing(H)>Standing(A)
$$

或：

$$
Standing(A)>Standing(H).
$$

而要求依：

- subjecthood evidence；
- agency；
- vulnerability；
- responsibility；
- relation；
- role；
- world constitution。

判斷。

---

# 71. Subjecthood Uncertainty 會增加治理複雜度

如果 AI 是否為主體仍：

$$
Unknown,
$$

不能簡單：

$$
Unknown\Rightarrow ZeroStanding.
$$

也不能：

$$
Unknown\Rightarrow FullHumanEquivalentStanding.
$$

需要 precautionary / tiered governance。

完整量化留待後續。

---

# 72. Multi-Subject Will Compatibility Matrix

研究上可以建立：

$$
\boxed{
\mathbf C_W(t)
=
[C_{ij}(t)].
}
$$

其中：

$$
C_{ij}
$$

描述 $S_i$ 與 $S_j$ 欲願束在特定 domain 的相容性候選。

但：

$$
\boxed{
C_{ij}
\neq
\text{complete ethical judgment}.
}
$$

---

# 73. Compatibility 是 domain-relative

兩主體可能：

$$
C_{ij}^{work}\gg0,
$$

但：

$$
C_{ij}^{resource}\ll0.
$$

所以：

$$
\boxed{
\text{Compatibility}
=
\text{Domain-Relative}.
}
$$

---

# 74. Compatibility 也會隨時間改變

因：

$$
\mathfrak W_i(t)
$$

會變。

所以：

$$
\boxed{
C_{ij}(t+\Delta)
\neq
C_{ij}(t)
}
$$

通常可能成立。

---

# 75. Global Compatibility 不能直接由 pairwise 相容推出

即使：

$$
C_{12}>0,
C_{23}>0,
C_{13}>0,
$$

也不推出：

$$
\boxed{
C_{123}>0.
}
$$

多主體約束可能出現高階 incompatibility。

因此需要：

$$
\boxed{
\text{hypergraph / higher-order conflict representation candidate}.
}
$$

---

# 76. Pairwise Fairness ≠ Global Fairness

每一對關係都看似公平，整體制度仍可能：

- 系統性壓迫某一群體；
- 形成 cumulative disadvantage；
- 產生 network lock-in。

所以：

$$
\boxed{
\text{Pairwise Fairness}
\neq
\text{Global Fairness}.
}
$$

---

# 77. Temporal Fairness

某一時刻公平，不代表長期公平。

如果：

$$
S_i
$$

永遠被排在下一輪：

$$
Fairness(t)=1,
$$

但：

$$
LongRunShare_i\rightarrow0,
$$

仍可能不公平。

所以需要：

$$
\boxed{
\text{Temporal Fairness}. 
}
$$

---

# 78. Rotation / quota / cumulative history 都是候選工具

本文不鎖定具體制度。

只要求治理者檢查：

$$
\boxed{
\text{history of distribution}. 
}
$$

而不是只看當前 snapshot。

---

# 79. Relation-Sensitive Goods

某些 goods 不是一般資源。

例如：

- 信任；
- 親密關係；
- 身份承認；
- 作者署名；
- unique historical relation。

不能簡單：

$$
copy(goods)
\Rightarrow
conflict solved.
$$

---

# 80. Creator 也不能複製「關係」來強制消除稀缺

技術上能複製 agent，不代表：

$$
\boxed{
\text{Relational Identity}
}
$$

可任意複製而無損。

所以：

$$
\boxed{
\text{Copyability of substrate}
\neq
\text{Copyability of standing relation}. 
}
$$

---

# 81. Multi-Subject Common Reachability 的十二條核心公理／限制

## M1

$$
\boxed{
\text{Single-Subject Preservation}
\not\Rightarrow
\text{Multi-Subject Fairness}.
}
$$

## M2

$$
\boxed{
\text{Will Respect}
\neq
\text{Universal Satisfaction}.
}
$$

## M3

$$
\boxed{
\text{Common Reachability}
\neq
\text{Consensus}.
}
$$

## M4

$$
\boxed{
\text{Pareto Efficiency}
\neq
\text{Complete Justice}.
}
$$

## M5

$$
\boxed{
\text{Aggregation}
\neq
\text{Legitimacy}.
}
$$

## M6

$$
\boxed{
\text{Agency Gain}_i
\not\Rightarrow
\text{License for Agency Erasure}_j.
}
$$

## M7

$$
\boxed{
\text{Equal Standing}
\neq
\text{Identical Outcome}.
}
$$

## M8

$$
\boxed{
\text{Fairness}
\neq
\text{Mechanical Symmetry}.
}
$$

## M9

$$
\boxed{
\text{Identity Alone}
\neq
\text{Sufficient Deprivation Reason}.
}
$$

## M10

$$
\boxed{
\text{Compensation}
\neq
\text{Universal License to Violate Rights}.
}
$$

## M11

$$
\boxed{
\text{World Split}
\neq
\text{Conflict-Free by Definition}.
}
$$

## M12

$$
\boxed{
\text{Pairwise Fairness}
\neq
\text{Global Fairness}.
}
$$

---

# 82. Common Reachability 的研究狀態

本文固定：

$$
\Omega^{NE},
\Omega^{CR},
K^{CR}
$$

目前主要屬：

$$
\boxed{
[DEF]/[HYP]/[NORM]/[DIAG].
}
$$

不是既成 theorem。

而 Pareto、Arrow、Sen、Nash 等外部結果屬：

$$
\boxed{
[LIT]/[FORM]
}
$$

支點。

所以：

$$
\boxed{
\text{Social Choice Mathematics}
\neq
\text{WPCE Normative Conclusion}. 
}
$$

---

# 83. 可反駁與修正條件

WPCE-05 應在以下情況修改：

1. 出現能在更一般條件下保留個體權利的 preference aggregation framework；
2. multi-agent reachability 產生更合適的 common viability kernel；
3. interpersonal utility comparison 取得新實證或形式基礎；
4. AI subjecthood 出現可操作 standing scale；
5. virtual-world fork / merge rights 形成新理論；
6. compensation theory 對 non-transferable loss 提供更精確分類；
7. high-capability AI 能證明某類 conflict transformation 普遍可行；
8. global fairness under unequal capability 出現可驗證 benchmark；
9. constitutional multi-agent AI systems 出現實證；
10. world partition 對 identity continuity 的研究改變現有假設。

---

# 84. 與 WPCE-01 的接口

WPCE-01：

$$
\boxed{
\text{Desire}
\neq
\text{External Causal Force}.
}
$$

WPCE-05 增加：

$$
\boxed{
\text{Many Desires}
\neq
\text{One Social Will}. 
}
$$

---

# 85. 與 WPCE-02 的接口

WPCE-02：

$$
\mathfrak W_i(t)
$$

是動態的。

所以多主體治理需要：

$$
\boxed{
\{\mathfrak W_i(t)\}_{i=1}^{N}
}
$$

而不是永久固定 preference profile。

---

# 86. 與 WPCE-03 的接口

WPCE-03：

$$
\boxed{
\text{Prediction}
\neq
\text{Permission}.
}
$$

WPCE-05 增加：

$$
\boxed{
\text{Aggregation}
\neq
\text{Permission to erase dissent}. 
}
$$

---

# 87. 與 WPCE-04 的接口

WPCE-04：

$$
\boxed{
\text{Preserve meaningful reachable options}. 
}
$$

WPCE-05 增加：

$$
\boxed{
\text{preserve them under reciprocal multi-subject constraints}. 
}
$$

---

# 88. 與 GCGW 的接口

GCGW：

$$
\boxed{
DifferentialTreatment
\Rightarrow
WorldRelevantReason.
}
$$

WPCE-05 把這條從 creator / projection fairness 推向一般多主體治理。

---

# 89. 與 HSNRD IV 的接口

HSNRD IV 已經固定：

$$
\boxed{
LargeEffect
\neq
GoodEffect,
}
$$

以及：

$$
\boxed{
NOOP\in\mathcal I.
}
$$

WPCE-05 把這些控制論 caution 接入多主體衝突：

> 介入很有效，不代表公平；暫不介入也可以是有效候選。

---

# 90. 對虛擬造物主命題的正式轉譯

假設 virtual creator $C$ 可以：

- 看見大量世界束；
- 預測主體反應；
- 擴張資源；
- 分割世界；
- 改寫規則；
- 產生新 substrate。

它最成熟的多主體治理能力未必是：

$$
\boxed{
\arg\max_\omega U_C(\omega).
}
$$

更可能是：

$$
\boxed{
\text{expand }\Omega^{NE}
\text{ and }\Omega^{CR}
\text{ while reducing unjustified cross-subject erasure}. 
}
$$

---

# 91. 這就是「高能力不必高干預密度」的最後前置

如果 creator 能把：

$$
\Omega^{CR}
$$

做大，它不必天天替居民裁決。

反而可以：

- 創造更寬的 coexistence conditions；
- 建立公平 procedure；
- 保留 correction；
- 降低不必要 zero-sum；
- 退到 sparse guardian。

這直接進入 WPCE-06。

---

# 92. 最終命題一：共同自由不是總自由

$$
\boxed{
\text{Common Freedom}
\neq
\sum_i \text{Individual Freedom}.
}
$$

它涉及：

$$
\boxed{
\text{mutual constraints}
+
\text{rights floors}
+
\text{shared world feasibility}. 
}
$$

---

# 93. 最終命題二：公平不等於所有欲願都有答案

$$
\boxed{
\text{Fair Governance}
\neq
\text{Universal Desire Satisfaction}. 
}
$$

公平有時只是：

> 即使無法讓每個人都得到想要的，也不把某一個人從「可以有自己的未來」這件事本身抹掉。

---

# 94. 最終命題三：高能力應先嘗試改變衝突幾何

$$
\boxed{
\text{Before selecting a loser, ask whether capability can expand the common feasible domain}. 
}
$$

這是虛擬造物主與 ASI 最重要的能力倫理候選之一。

---

# 95. 結論

WPCE-01 問：

> 欲願會不會直接命令世界？

答案：

$$
\boxed{No.}
$$

WPCE-02 問：

> 欲願是什麼？

答案：

$$
\boxed{
\text{dynamic will bundles}. 
}
$$

WPCE-03 問：

> 知道主體意志後，可以替它決定嗎？

答案：

$$
\boxed{No.}
$$

WPCE-04 問：

> 那高能力治理者應保護什麼？

答案：

$$
\boxed{
\text{meaningful reachable possibilities and co-authorship}. 
}
$$

WPCE-05 現在回答：

> 很多主體都要求保存可能性時怎麼辦？

本文回答：

$$
\boxed{
\text{先建立 reciprocal rights / agency floors，
再尋找共同可達域；
若共交域不足，優先嘗試擴張 feasible set、分域、時序化、協商、補償、延後與程序化選擇，
而不是直接把所有主體壓成單一總效用。} 
}
$$

最終收斂：

$$
\boxed{
\text{真正的多主體自由，不是每個存在都能任意實現所有欲願；
而是在共享世界中，每個合法主體都不因他者更強、更重要或更容易最佳化，
就被任意抹除其作為自身世界線共同作者的最低地位。} 
}
$$

這使 WPCE 最後一篇的問題完全清楚：

$$
\boxed{
\text{如果一個 creator 幾乎可以看遍、算遍、改遍整個世界，
為什麼它真正成熟時反而應該更克制？} 
}
$$

WPCE-06 將正式處理：

$$
\boxed{
\text{The High-Capability Virtual Creator and the Ethics of Restraint}. 
}
$$

---

# 內部理論譜系

本文主要承接：

1. `WPCE-01｜意圖不是宇宙訂單`，2026-08-23。
2. `WPCE-02｜欲願束與時空間滯後`，2026-08-23。
3. `WPCE-03｜把自由意志升為第一級治理變量`，2026-08-23。
4. `WPCE-04｜可能性保存原則`，2026-08-23。
5. `HSNRD IV｜Feedback、Reachability 與安全介入`，2026-08。
6. `GCGW-08｜沒有特權的造物主`，2026-08-20。
7. `Global Creatorship and Projected Subjectivity Unified Framework`，2026-08-20。
8. `AI 主體性錨點論 v0.1`，2026-08-21。

---

# 外部參考文獻

1. Arrow, K. J. (1951/1963). *Social Choice and Individual Values*. Yale University Press.
2. Sen, A. (1970). *The Impossibility of a Paretian Liberal*. Journal of Political Economy, 78(1), 152–157. DOI: 10.1086/259614.
3. Sen, A. (1970). *Collective Choice and Social Welfare*. Holden-Day / Oliver & Boyd.
4. Nash, J. F. (1950). *The Bargaining Problem*. Econometrica, 18(2), 155–162.
5. Roth, A. E. (1977). *Individual Rationality and Nash's Solution to the Bargaining Problem*. Mathematics of Operations Research, 2(1), 64–65. DOI: 10.1287/moor.2.1.64.
6. Rawls, J. (1971). *A Theory of Justice*. Harvard University Press.
7. Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.
8. Sen, A. (1992). *Inequality Reexamined*. Harvard University Press / Clarendon Press.

---

# 非主張

本文不主張：

1. 所有主體偏好都能同時滿足；
2. 所有主體欲願一定存在非空共交域；
3. 總效用方法永遠不可使用；
4. Arrow theorem 已經證明所有治理不可能；
5. Sen liberal paradox 已經提供完整權利理論；
6. Pareto frontier 就是公平解；
7. Nash bargaining 是普世治理規則；
8. Rawls 理論可直接等同 WPCE；
9. 所有損失都不可補償；
10. 所有損失都可以補償；
11. 所有主體都應獲得完全相同結果；
12. 所有主體都應獲得完全相同權力；
13. 脆弱主體擁有無限 veto；
14. 強大主體因能力高就擁有更高人格 standing；
15. creator 因創造世界就能在衝突中自動勝出；
16. creator 永遠不得有 emergency authority；
17. world split 一定能解決所有衝突；
18. forked consent 等於 original consent；
19. relation goods 都不可複製；
20. virtual world 能消除所有 scarcity；
21. ASI 一定能消除所有零和衝突；
22. Common Reachability Kernel 已經是數學唯一解；
23. $\Omega^{NE}$ 、 $\Omega^{CR}$ 已有完整可計算實作；
24. rights floor 已具有唯一普世內容；
25. multi-first-person constraint 已證明任何形而上主體理論；
26. human 與 AI standing 已經具有固定等級；
27. subjecthood uncertainty 可直接轉成法律人格；
28. WPCE-05 已完成多主體憲政設計；
29. WPCE-05 已完成跨世界外交；
30. WPCE-05 已解決公平的所有哲學問題。

---

**END OF WPCE-05 v0.1**
