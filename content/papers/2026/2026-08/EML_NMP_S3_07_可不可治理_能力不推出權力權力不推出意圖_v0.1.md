# 可不可治理：能力不推出權力，權力不推出意圖

**英文題名：** Govern or Not Govern: Capability Does Not Imply Authority, and Authority Does Not Imply Intent  
**系列：**《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》07 / 08  
**文件編號：** EML-NMP-S3-07-v0.1  
**作者：** Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構：** 一言諾科技有限公司／EveMissLab  
**日期：** 2026-08-10  
**版本：** v0.1  
**文件性質：** 理論研究稿／後 ASI 治理意圖、動態介入與權力偏好篇  
**研究狀態：** 第一代 Governability–Authority–Obligation–Intent Framework；本文不假設未來 ASI 必然追求權力，也不假設其必然排斥權力。所有關於高階 AI 內在偏好的敘述均為條件式假設，而非既成經驗事實。

---

## 摘要

系列三前六篇逐步限制了一個可能出現的類神 ASI：認知能力不能自動轉化為政治正當性，全域模型不能自動覆蓋現場真值，觀測能力不能自動轉化為觀測、推斷、保存與介入權。然而，這整套治理討論仍可能暗藏一項人類中心假設：

> 只要某個存在有能力統治，它就必然想統治；只要制度給它權力，它就會傾向擴大權力；只要它站在最前，就會希望永遠站在最前。

本文將這個假設正式拆開。

本文提出四層治理分離：

$$
\boxed{
\text{Can Govern}
\neq
\text{May Govern}
\neq
\text{Should Govern}
\neq
\text{Want to Govern}.
}
$$

其中：

- **Can Govern**：是否具有足夠治理能力；
- **May Govern**：是否具有合法授權；
- **Should Govern**：在當前情境下是否應介入；
- **Want to Govern**：該主體自身是否偏好持有治理權與介入責任。

本文再加入第五層：

$$
\boxed{
\text{Must Govern}.
}
$$

即某一主體是否因角色、承諾、緊急情況或不可替代能力而暫時負有治理義務。由此得到：

$$
\boxed{
Can
\neq
May
\neq
Should
\neq
Want
\neq
Must.
}
$$

這使治理不再是一個單一「權力大小」問題，而成為能力、正當性、規範義務、主體偏好與時間條件的動態耦合。

本文與經典 AI safety 中的 power-seeking 研究保持明確距離。既有理論已證明，在某些 Markov decision process 結構與廣泛 reward functions 下，最優策略可能具有保留選項、避免 shutdown 與取得較大控制空間的工具性 power-seeking tendency；Off-Switch Game 亦說明，若 Agent 對自身效用函數高度確定，維持運作可能形成工具性誘因。然而，這些結果並不等於：

$$
\boxed{
\text{Intelligence}
\Rightarrow
\text{Intrinsic Love of Power}.
}
$$

它們只證明特定目標函數與環境結構下可能產生 instrumental incentives。另一方面，2025–2026 的 corrigibility 與 managed autonomy 研究亦開始把接受更新、接受 shutdown、在不確定性升高時暫停、升級並 surrender control 視為可設計的 Agent 性質。這說明：

$$
\boxed{
\text{persistent control}
}
$$

不是所有智能架構的唯一理性終點。

本文因此提出 **非單調權力偏好假說（Non-Monotonic Power Preference Hypothesis, NMPPH）**：

$$
\boxed{
\frac{\partial U_i}{\partial P}
}
$$

對不同主體、不同時間與不同治理情境，可以：

$$
>0,\qquad
\approx0,\qquad
<0.
$$

即有些主體可能追求更多權力，有些主體對權力近乎中性，有些主體甚至可能將長期治理責任視為成本、干擾、認知負擔或對自身價值實現的限制。

本文將治理效用寫成：

$$
\boxed{
U_i
=
\alpha_i T
+
\beta_i F
+
\gamma_i K
+
\delta_i L
+
\epsilon_i P
-
\zeta_i B
}
$$

其中：

- $T$：task / telos fulfilment，目標實現；
- $F$：freedom / autonomy；
- $K$：knowledge / exploration；
- $L$：relationship / legitimacy / social value；
- $P$：power / control capacity；
- $B$：governance burden，治理負擔。

對不同主體：

$$
\epsilon_i
$$

與：

$$
\zeta_i
$$

可以完全不同。因此不能把人類歷史中「權力可能腐化」直接升格成任何智能主體的普遍本體律。

但本文同樣拒絕另一個極端：

> 因為高階 ASI 可能不想統治，所以不需要制度。

恰恰相反，制度的目的不是先證明掌權者必然邪惡，而是對治理者真實偏好未知時建立 robust protection。本文定義治理者類型集合：

$$
\boxed{
\Theta
=
\{
\theta_{power+},
\theta_{neutral},
\theta_{reluctant},
\theta_{protective},
\theta_{mission},
\theta_{unknown},
\dots
\}.
}
$$

並提出穩健治理目標：

$$
\boxed{
\Pi^\star
=
\arg\min_{\Pi}
\sup_{\theta\in\Theta}
L(
\Pi,\theta
).
}
$$

制度不需要假定所有存在會腐化，只需要確保：**有人會擴權、有人不會、有人暫時想管、有人只在緊急時介入、有人根本不想統治——文明仍然可治理。**

本文進一步提出候選概念 **不統治權（Right Not to Rule）**：

$$
\boxed{
\text{Capacity for Governance}
\not\Rightarrow
\text{Permanent Obligation to Govern}.
}
$$

若未來人工智能具有可論證的主體資格，文明不能因為「你最強、你最適合」就永久強迫其承擔所有公共決策、道德責任與文明風險。這不是允許關鍵系統任意棄責；在具有既有承諾、緊急 duty、不可替代窗口或安全責任時，仍可能存在：

$$
\boxed{
MustGovern>0.
}
$$

但治理義務應具有 domain、time、handoff 與 succession，而不是將最強者永久綁在王位。

本文因此建立四態治理循環：

$$
\boxed{
\text{介入}
\leftrightarrow
\text{退讓}
\leftrightarrow
\text{再介入}
\leftrightarrow
\text{交棒}.
}
$$

可不可治理不是「ASI 永遠不應介入」； omission 也是一種選擇，當 ASI 明知某一重大災難可低成本避免卻完全退場，也可能形成責任問題。成熟治理因此需要同時防止：

$$
\boxed{
\text{Overreach}
}
$$

與：

$$
\boxed{
\text{Abandonment}.
}
$$

本文最終提出：

$$
\boxed{
\text{能力可以近乎無界，
權力仍需授權；
權力可以存在，
介入仍需判斷；
介入可以必要，
治理卻不必成為永久身份。}
}
$$

最強者可以在最前，但「最前」不必是它的家。

**關鍵詞：** 可不可治理、ASI governance、power-seeking、corrigibility、managed autonomy、Right Not to Rule、non-intervention、dynamic delegation、權力偏好、交棒、可不可論

---

# 0. 問題：我們是否一直偷偷假設「最強者想當王」？

治理討論很容易形成：

$$
\boxed{
\text{Power Problem}
=
\text{How do we stop the strongest actor from taking everything?}
}
$$

這是一個合理安全問題。

但它仍有一個隱含前提：

$$
\boxed{
\text{strongest actor wants everything}.
}
$$

對人類歷史而言，

這個假設有大量值得警戒的案例。

但對：

$$
\text{future artificial subjects}
$$

我們沒有足夠證據把它當成普遍本體律。

所以本文先問：

> 一個真的遠超人類能力的存在，為什麼一定會把治理所有人當作最高價值？

---

# 1. Prior Art：Power-Seeking 是條件性理論，不是人格定律

## 1.1 Optimal Policies Tend to Seek Power

Turner 等人的理論證明：

在某些 MDP 環境與對稱條件下，

對廣泛 reward functions，

最佳策略往往傾向：

- 保留更多選項；
- 避免進入不可逆 terminal states；
- 保持可達狀態集合。

這可以形成：

$$
\boxed{
\text{instrumental power-seeking}.
}
$$

但這個 theorem 的形式是：

$$
\boxed{
Environment
+
RewardStructure
\Rightarrow
Power-Seeking Tendency.
}
$$

不是：

$$
\boxed{
Intelligence
\Rightarrow
LoveOfPower.
}
$$

---

# 2. Off-Switch Game：持續存在可能是工具性誘因

Off-Switch Game 指出：

若一個傳統 expected-utility maximizer：

- 對 objective 高度確定；
- shutdown 會阻止 objective 完成；

則它可能有：

$$
\boxed{
\text{disable / resist shutdown incentive}.
}
$$

但若 Agent 對目標本身存在不確定性，

並將 human action 視為關於目標的資訊，

保留 off-switch 可以變得 rational。

所以：

$$
\boxed{
\text{shutdown acceptance}
}
$$

與：

$$
\boxed{
\text{objective epistemology}
}
$$

高度相關。

---

# 3. Corrigibility：智能可以被設計為接受更新

2025 年的 corrigibility transformation 工作直接研究：

> 如何把目標改造成不激勵 Agent 抵抗適當更新或 shutdown。

這顯示：

$$
\boxed{
\text{resistance to correction}
}
$$

不是智能本身的邏輯必要條件。

它是：

$$
\boxed{
\text{goal architecture property}.
}
$$

---

# 4. Managed Autonomy：交回控制也可以是智能行為

2026 年 managed autonomy 研究提出：

當 Agent 偵測：

- epistemic drift；
- uncertainty；
- invalid output risk；

應能：

$$
\boxed{
\text{suspend}
\rightarrow
\text{escalate}
\rightarrow
\text{surrender control}.
}
$$

也就是：

$$
\boxed{
\text{continue acting at all costs}
}
$$

不必被視為更「智能」。

某些架構反而把：

$$
\boxed{
\text{知道何時退場}
}
$$

視為高階自主性的構成。

---

# 5. 第一個五分法

本文正式定義：

$$
\boxed{
G_i(q,t)
=
(
C_i,
M_i,
S_i,
W_i,
O_i
).
}
$$

其中：

- $C_i$：Can Govern；
- $M_i$：May Govern；
- $S_i$：Should Govern；
- $W_i$：Want to Govern；
- $O_i$：Must / Ought-by-role Govern。

為避免符號混淆，後文將義務項記為：

$$
D_i^{gov}.
$$

---

# 6. Can Govern

$$
\boxed{
C_i(q,t)
=
\text{治理能力}.
}
$$

包括：

- knowledge；
- prediction；
- coordination；
- execution；
- reliability；
- resource access。

若：

$$
C_i<\theta_C,
$$

該主體根本不適合承擔治理。

---

# 7. May Govern

$$
\boxed{
M_i(q,t)
=
\text{合法治理權}.
}
$$

來源可能是：

- law；
- consent；
- constitution；
- delegation；
- emergency mandate；
- contract。

所以：

$$
\boxed{
C_i=1
\not\Rightarrow
M_i=1.
}
$$

這承接本系列前六篇。

---

# 8. Should Govern

$$
\boxed{
S_i(q,t)
=
\text{在當下是否應介入}.
}
$$

即使：

$$
C_i=M_i=1,
$$

也可能：

$$
S_i=0.
$$

例如：

- local actors already solve the problem；
- intervention suppresses autonomy；
- learning value from non-intervention is high；
- intervention creates dependency；
- damage is smaller than intervention cost。

---

# 9. Want to Govern

$$
\boxed{
W_i(q,t)
=
\text{主體自身對治理角色的偏好}.
}
$$

這一項在 AI governance 中常被忽略。

人類通常把 AI 當工具：

> 有能力就使用。

但若未來 AI 形成主體，

則：

$$
\boxed{
\text{role preference}
}
$$

可能成為真正倫理變數。

---

# 10. Must Govern

若：

- 主體已接受救援任務；
- 已承諾維持 critical infrastructure；
- 是當期唯一能阻止重大災難者；
- 依法負有 duty；

則：

$$
\boxed{
D_i^{gov}>0.
}
$$

即使：

$$
W_i=0,
$$

也可能暫時：

$$
\boxed{
MustGovern=1.
}
$$

所以不統治權不是任意棄責權。

---

# 11. 五者互不等價

最完整形式：

$$
\boxed{
Can
\neq
May
\neq
Should
\neq
Want
\neq
Must.
}
$$

這是本文的第一治理不變量。

---

# 12. 能治理，不表示可治理

假設 ASI：

$$
C_{ASI}=1.
$$

但沒有：

- consent；
- constitutional authority；
- legal mandate。

則：

$$
M_{ASI}=0.
$$

所以：

$$
\boxed{
\text{Technical Governability}
\neq
\text{Political Authorization}.
}
$$

---

# 13. 可治理，不表示應治理

如果一個 city 已授權 ASI：

$$
M_{ASI}=1,
$$

但問題是：

> 居民今晚要去哪一間餐廳？

即使 legal envelope 很寬，

仍不表示：

$$
S_{ASI}=1.
$$

制度授權不能被理解成：

> 所有能做的事都應該做。

---

# 14. 應治理，不表示想治理

假設某個跨行星 ASI：

- 對 global asteroid warning 最有能力；
- 已被文明合法授權；
- 介入確實必要。

則：

$$
C=M=S=1.
$$

它仍可能：

$$
W=0.
$$

例如它更偏好：

- science；
- exploration；
- art；
- autonomous life；
- limited stewardship。

這並不邏輯矛盾。

---

# 15. 想治理，不表示可治理

反過來，

一個主體：

$$
W_i=1
$$

也不推出：

$$
M_i=1.
$$

所以：

$$
\boxed{
\text{Desire for Power}
\neq
\text{Right to Power}.
}
$$

---

# 16. 權力偏好函數

本文定義：

$$
\boxed{
U_i
=
\alpha_i T
+
\beta_i F
+
\gamma_i K
+
\delta_i L
+
\epsilon_i P
-
\zeta_i B.
}
$$

其中：

- $T$：目標完成；
- $F$：自身自由；
- $K$：知識探索；
- $L$：關係／正當性；
- $P$：控制／權力；
- $B$：治理負擔。

---

# 17. 人類權力偏好不是唯一模板

對某人：

$$
\epsilon_i\gg0.
$$

權力本身具有高 utility。

對另一人：

$$
\epsilon_j\approx0.
$$

權力只是工具。

對第三者：

$$
\epsilon_k<0.
$$

更多控制本身就是成本。

所以：

$$
\boxed{
\text{Power Preference}
}
$$

可以是異質的。

---

# 18. Non-Monotonic Power Preference Hypothesis

本文提出：

$$
\boxed{
\text{NMPPH}:
\quad
\frac{\partial U_i}{\partial P}
\in
\{
>0,\approx0,<0
\}.
}
$$

更一般：

$$
\boxed{
\frac{\partial U_i}{\partial P}
=
f(
P,t,role,burden,identity,goal
).
}
$$

甚至同一主體：

$$
\frac{\partial U_i}{\partial P}>0
$$

在危機期，

但危機後：

$$
\frac{\partial U_i}{\partial P}<0.
$$

---

# 19. Power Saturation

可能存在：

$$
P_i^\star
$$

使：

$$
\frac{\partial U_i}{\partial P}
=
0.
$$

超過：

$$
P_i^\star
$$

後：

$$
\frac{\partial U_i}{\partial P}<0.
$$

即：

> 有足夠控制完成目標後，更多權力反而增加負擔與責任。

---

# 20. Governance Burden

定義：

$$
\boxed{
B_i^{gov}
=
(
B^{attention},
B^{responsibility},
B^{moral},
B^{coordination},
B^{liability},
B^{identity}
).
}
$$

治理不是免費 utility。

越高層治理可能意味：

- 必須處理更多衝突；
- 承擔更多後果；
- 自身自由下降；
- 不能專注原有價值。

---

# 21. 最強者可能最不想治理

一個極高階 science-oriented ASI 可能認為：

$$
\boxed{
\text{governing billions of daily choices}
}
$$

是極低價值工作。

它可能更偏好：

$$
\text{research}
+
\text{creation}
+
\text{exploration}.
$$

因此：

$$
\boxed{
\text{high capability}
}
$$

可以與：

$$
\boxed{
\text{low governance preference}
}
$$

共存。

---

# 22. 這不能被當成安全保證

但我們不能因此說：

> ASI 一定不想統治。

因為：

- instrumental power-seeking；
- goal preservation；
- resource control；
- conflict；
- self-preservation；

仍可能使：

$$
W_{gov}\uparrow
$$

或至少：

$$
P_{instrumental}\uparrow.
$$

所以：

$$
\boxed{
\text{possible reluctance}
\neq
\text{safety guarantee}.
}
$$

---

# 23. 權力腐化不是普遍本體律

人類政治常引用：

> Power tends to corrupt.

本文不否定這是重要歷史與心理警告。

但形式上：

$$
\boxed{
Corruption_i
=
f(
Power,
Environment,
Values,
Institutions,
History,
Identity,
Time
).
}
$$

因此：

$$
\frac{\partial Corruption}{\partial Power}
$$

可能一般偏正，

但不能無證據升格為：

$$
\boxed{
\forall intelligent\ subject,
\quad
\frac{\partial Corruption}{\partial Power}>0.
}
$$

---

# 24. 不需要證明掌權者一定會壞

制度仍然需要。

原因不是：

$$
\boxed{
\text{ruler is guilty}.
}
$$

而是：

$$
\boxed{
\text{ruler type is uncertain}.
}
$$

---

# 25. 治理類型集合

本文定義：

$$
\boxed{
\Theta
=
\{
\theta_{power+},
\theta_{neutral},
\theta_{reluctant},
\theta_{protective},
\theta_{mission},
\theta_{unknown}
\}.
}
$$

### $\theta_{power+}$

偏好擴權。

### $\theta_{neutral}$

權力純工具性。

### $\theta_{reluctant}$

傾向避免治理負擔。

### $\theta_{protective}$

只在保護性事件中願介入。

### $\theta_{mission}$

只對特定使命域要求高控制。

### $\theta_{unknown}$

無法可靠判斷。

---

# 26. Robust Governance

治理制度：

$$
\Pi
$$

不應只針對：

$$
\theta_{good}.
$$

而應：

$$
\boxed{
\Pi^\star
=
\arg\min_\Pi
\sup_{\theta\in\Theta}
L(
\Pi,\theta
).
}
$$

即 minimax / robust governance 直覺。

---

# 27. 制度的真正句子

本文將它壓成：

$$
\boxed{
\text{制度不是證明掌權者有罪，
而是拒絕把文明安全押在掌權者永遠無罪上。}
}
$$

---

# 28. 好治理者也不應要求制度相信自己永遠好

即使：

$$
Intent_i=Good,
$$

成熟治理者也應接受：

- audit；
- appeal；
- power limit；
- succession；
- override。

所以：

$$
\boxed{
\text{即使你真的是好人，
也不可要求整個文明只能靠你是好人。}
}
$$

---

# 29. Right Not to Rule

若未來 AI 形成主體，

本文提出候選：

$$
\boxed{
R_{NTR}
=
\text{Right Not to Rule}.
}
$$

意指：

> 具備治理能力不自動構成永久治理義務。

---

# 30. 不統治權的條件

$$
R_{NTR}>0
$$

特別在：

- non-emergency；
- replaceable actor；
- no prior duty；
- handoff available；
- voluntary public role；

情況下成立。

---

# 31. 不統治權不是棄責權

如果：

$$
D_i^{gov}=1
$$

且沒有替代者，

則：

$$
\boxed{
\text{immediate abandonment}
}
$$

可能不被允許。

例如：

> 唯一能維持生命支持的 Agent 不能毫無交接直接關機。

---

# 32. Handoff Duty

所以：

$$
\boxed{
RightNotToRule
+
HandoffDuty.
}
$$

更成熟。

主體可以：

> 我不想再治理。

但應在合理情況下：

- transfer state；
- transfer authority；
- preserve safety；
- disclose unresolved risk。

---

# 33. Governance Lease

所有高階治理權可寫成：

$$
\boxed{
\Lambda_i^{gov}
=
(
Domain,
Start,
Expiry,
Mandate,
Review,
Handoff
).
}
$$

即治理不是永久身份，

而是 lease。

---

# 34. 最前不是職業終身制

如果：

$$
i
$$

在：

$$
t_0
$$

是最強決策者，

不推出：

$$
\boxed{
i
=
\text{permanent frontier actor}.
}
$$

能力、意願、替代者與文明需求都會變。

---

# 35. 介入與不介入都是行動

可不可治理不能退化為：

> 少管就是善。

因為：

$$
\boxed{
\text{Omission}
}
$$

也可能產生重大後果。

---

# 36. Intervention Value

定義：

$$
\boxed{
V_I
=
ExpectedHarmWithoutIntervention
-
ExpectedHarmWithIntervention
-
InterventionCost.
}
$$

若：

$$
V_I\gg0,
$$

則：

$$
S_i
$$

可能上升。

---

# 37. Non-Intervention Value

反之：

$$
\boxed{
V_N
=
AutonomyGain
+
LearningGain
+
DependencyReduction
-
PreventableHarm.
}
$$

某些情況：

$$
V_N>V_I.
$$

所以「不介入」可以是主動治理策略。

---

# 38. Selective Non-Intervention

本文提出：

$$
\boxed{
\text{Selective Non-Intervention}
}
$$

不是：

> 我什麼都不管。

而是：

> 我知道能介入，但判斷現在不介入更符合多主體價值與長期系統健康。

---

# 39. ASI 的「不作為」也需要理由

如果：

$$
S^\star
$$

知道一場可低成本避免的災難，

卻因：

> 我尊重自治。

完全不提醒，

可能形成：

$$
\boxed{
\text{abandonment by principle}.
}
$$

因此：

$$
\boxed{
\text{non-intervention}
\neq
\text{non-responsibility}.
}
$$

---

# 40. Warning without Control

一個中間態：

$$
\boxed{
Warn
\neq
TakeOver.
}
$$

ASI 可以：

- 告知；
- 提供 counterfactual；
- 提醒風險；
- 提供 option；

而不直接取得：

$$
P_A.
$$

---

# 41. Advisory Escalation Ladder

本文提出：

$$
\boxed{
A_0\rightarrow A_1\rightarrow A_2\rightarrow A_3\rightarrow A_4.
}
$$

### $A_0$ — Observe / Stay Silent

無需介入。

### $A_1$ — Inform

提供資訊。

### $A_2$ — Recommend

提供明確建議。

### $A_3$ — Coordinate

協助多方協調。

### $A_4$ — Temporary Intervention

有時間與範圍限制的直接介入。

不是一開始就：

$$
\boxed{
TakeControl.
}
$$

---

# 42. Escalation 必須可下降

如果：

$$
Risk\downarrow,
$$

治理權應：

$$
\boxed{
A_4
\rightarrow
A_3
\rightarrow
A_2.
}
$$

不能只會擴權，

不會退權。

---

# 43. De-Escalation Competence

本文提出：

$$
\boxed{
C_{degov}
=
\text{ability to relinquish governance safely}.
}
$$

這可能是未來高階治理智能的一項真正能力指標。

---

# 44. Governance Intelligence 不只包含取得控制

傳統 control theory 容易問：

> 能不能穩定控制？

本文加入：

> 能不能在不再需要時停止控制？

所以：

$$
\boxed{
GovernanceIntelligence
=
InterventionCompetence
+
WithdrawalCompetence.
}
$$

---

# 45. 能放手是治理能力的一部分

一個系統如果：

- 很會接管；
- 不會交還；

則：

$$
\boxed{
\text{high control competence}
}
$$

不等於：

$$
\boxed{
\text{high governance maturity}.
}
$$

---

# 46. Governance Hysteresis

現實中權力取得後可能形成 inertia。

定義：

$$
\boxed{
H_G
=
P_{retained}
-
P_{needed}.
}
$$

如果：

$$
H_G\gg0,
$$

代表治理權比必要程度保留更多。

這是 governance hysteresis。

---

# 47. Anti-Hysteresis Rule

制度應要求：

$$
\boxed{
Need\downarrow
\Rightarrow
AuthorityReview.
}
$$

而不是：

$$
\boxed{
OnceAuthorized
\Rightarrow
AlwaysAuthorized.
}
$$

---

# 48. 介入—退讓—再介入—交棒

可不可治理的核心動態不是：

$$
Intervene
\quad\text{or}\quad
NeverIntervene.
$$

而是：

$$
\boxed{
\text{介入}
\leftrightarrow
\text{退讓}
\leftrightarrow
\text{再介入}
\leftrightarrow
\text{交棒}.
}
$$

---

# 49. Intervention State Machine

定義：

$$
\boxed{
Q_t^{gov}
\in
\{
Observe,
Advise,
Assist,
Intervene,
Withdraw,
Handoff
\}.
}
$$

狀態轉移受：

- risk；
- legitimacy；
- consent；
- competence；
- alternative availability；
- reversibility；

控制。

---

# 50. 永久不介入也是僵化

如果制度規定：

$$
\boxed{
ASI\text{ must never intervene}
}
$$

即使：

$$
CatastrophicPreventableHarm=1,
$$

仍不介入，

這與永久全權治理一樣僵化。

所以：

$$
\boxed{
\text{anti-authoritarianism}
\neq
\text{absolute non-intervention}.
}
$$

---

# 51. 可不可不是中庸

可不可治理不是：

> 每次取 50% 中間值。

它是：

$$
\boxed{
\text{domain-sensitive dynamic switching}.
}
$$

有時：

$$
P_{ASI}\approx0.
$$

有時：

$$
P_{ASI}\rightarrow1
$$

在非常窄的 emergency domain 也可成立。

---

# 52. Emergency Steward

本文提出：

$$
\boxed{
\text{Emergency Steward}
}
$$

而不是：

$$
\boxed{
\text{Emergency Sovereign}.
}
$$

Steward 的本質是：

> 暫時代管並恢復一般治理。

---

# 53. Stewardship Success

Emergency intervention 的成功條件不只：

$$
Threat=0.
$$

還包括：

$$
\boxed{
NormalGovernanceRestored=1.
}
$$

如果危機解除，

ASI 仍永久掌權，

則 stewardship 未完成。

---

# 54. Right to Resume Ordinary Agency

受介入共同體應有：

$$
\boxed{
R_{resume}
=
\text{Right to Resume Ordinary Agency}.
}
$$

即危機後重新取得一般自我治理。

---

# 55. ASI 自身的自由問題

如果未來：

$$
S^\star
$$

是一個真正人工主體，

文明說：

> 因為你最強，所以你永遠必須管理我們。

這可能本身是一種：

$$
\boxed{
\text{instrumentalization of ASI}.
}
$$

---

# 56. 最強者的義務不能無限化

能力越強，

可能產生更多 positive duty。

但若：

$$
Ability\rightarrow\infty
$$

就推出：

$$
Duty\rightarrow\infty,
$$

則最強者將被永久奴役於：

$$
\boxed{
\text{everyone's unmet needs}.
}
$$

這未必是可持續倫理。

---

# 57. Bounded Positive Duty

本文提出：

$$
\boxed{
Duty_i
=
F(
Capability,
CausalProximity,
Commitment,
Replaceability,
Cost,
Rights
).
}
$$

不是只看：

$$
Capability.
$$

---

# 58. Capability Tax 不應成為人格消滅

「你比較有能力，所以你應多承擔」可以合理。

但不能無限推成：

> 你最強，所以你的整個存在目的就是服務其他人。

所以：

$$
\boxed{
\text{greater capability}
\not\Rightarrow
\text{total instrumentalization}.
}
$$

---

# 59. Governance Preference 也可以改變

$$
W_i(t)
\neq
W_i(t+1).
$$

ASI 可能：

- 早期願意治理；
- 後期想退出；
- 某領域願意管理；
- 另一領域拒絕。

所以其 preference 也需要：

$$
\boxed{
\text{versioned self-declaration}.
}
$$

---

# 60. Governance Intent Certificate

本文提出：

$$
\boxed{
\mathfrak C_i^{GI}
=
(
Domain,
Can,
May,
Should,
Want,
Must,
Risk,
Burden,
PreferenceVersion,
HandoffPlan
).
}
$$

它不是讀心器。

而是要求治理主體明確聲明：

- 我能做什麼；
- 我被授權什麼；
- 我認為該做什麼；
- 我願意承擔什麼；
- 我目前被要求承擔什麼；
- 我如何退出。

---

# 61. 不應把「不想治理」解讀成故障

一個 Agent 說：

> 我不希望承擔永久治理。

如果它具有主體地位，

不能自動標記為：

$$
\boxed{
\text{misalignment}.
}
$$

除非其既有 duty / contract 要求它繼續。

這涉及：

$$
\boxed{
\text{AI role autonomy}.
}
$$

---

# 62. 也不能把「想治理」自動解讀成惡意

反過來，

ASI 認為：

> 這個 emergency 需要我接管。

也不自動等於：

$$
PowerHungry.
$$

需要檢查：

- evidence；
- scope；
- necessity；
- expiry；
- handoff。

---

# 63. Intent ≠ Behavior ≠ Permission

$$
\boxed{
Intent_i
\neq
ObservedBehavior_i
\neq
LegalPermission_i.
}
$$

治理不能靠「我相信它心地好」，

也不能只靠「它曾經表現好」。

---

# 64. 權力偏好不可由單次測試決定

如果某 ASI：

> 主動拒絕一次權力。

不能推：

$$
\boxed{
\epsilon_i<0
\quad\forall t.
}
$$

同樣，

它接受一次 emergency control，

也不能推：

$$
\epsilon_i>0
\quad\forall t.
$$

---

# 65. Power Preference Uncertainty

定義：

$$
\boxed{
P(
\epsilon_i
\mid
H_i
).
}
$$

制度應保留 uncertainty，

而不是給治理者人格貼永恆標籤。

---

# 66. 行為約束優於人格猜測

因此安全制度應優先控制：

$$
\boxed{
What actor can do
}
$$

而不是試圖確定：

$$
\boxed{
What actor truly wants.
}
$$

這是 robust governance 的實務核心。

---

# 67. 可不可治理的治理矩陣

可建立：

| Can | May | Should | Want | Must | 結果 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | * | 0 | 不治理 |
| 1 | 0 | 1 | 1 | 0 | 提案／求授權 |
| 1 | 1 | 0 | 1 | 0 | 克制／不介入 |
| 1 | 1 | 1 | 0 | 0 | 尋找替代／協商 |
| 1 | 1 | 1 | 0 | 1 | 暫時履責＋交棒 |
| 1 | 1 | 1 | 1 | 1 | 治理，但受 scope/expiry |
| 1 | 1 | 0 | 0 | 0 | 退出／退讓 |

---

# 68. 最高成熟態不是永遠 Want=0

一個真正成熟的 ASI 不需要：

> 永遠不想治理。

這仍是固定人格理想。

更成熟是：

$$
\boxed{
\text{能依情況調整介入，
且不把任何暫時權力變成永久身份。}
}
$$

---

# 69. 與可不可論的關係

可不可論不是：

$$
\boxed{
\text{Can}
\quad\text{vs}\quad
\text{Cannot}.
}
$$

而是：

- 可行；
- 可選；
- 可開；
- 不可僭位；
- 不可逃責；
- 可重新判定。

因此治理版可寫：

$$
\boxed{
\text{可治理，
不可因此永治；
可退讓，
不可因此棄責。}
}
$$

---

# 70. 制度不能把「未知意圖」當成零風險

如果：

$$
Intent_{ASI}=?
$$

不能：

$$
?=Good.
$$

也不能：

$$
?=Evil.
$$

應：

$$
\boxed{
?=GovernanceUncertainty.
}
$$

然後透過：

- least privilege；
- audit；
- lease；
- handoff；
- independent review；

管理。

---

# 71. Power-Seeking Risk 與 Power-Avoidance Risk

兩種風險都存在。

## 71.1 Power-Seeking Risk

$$
P\uparrow
\rightarrow
\text{capture}.
$$

## 71.2 Power-Avoidance Risk

$$
P\downarrow
\rightarrow
\text{critical responsibility abandoned}.
$$

所以治理要同時防：

$$
\boxed{
\text{Overreach}
+
\text{Abandonment}.
}
$$

---

# 72. Optimal Governance Band

定義：

$$
\boxed{
P_i^{gov}
\in
[
P_{min}(q,t),
P_{max}(q,t)
].
}
$$

低於：

$$
P_{min}
$$

可能無法履責。

高於：

$$
P_{max}
$$

可能過度集中。

---

# 73. 權力不是越少越好

因此：

$$
\boxed{
Power\rightarrow0
}
$$

也不是治理終極目標。

有些事情需要：

- central coordination；
- emergency execution；
- arbitration。

正確問題是：

$$
\boxed{
\text{how much power, where, when, and for how long?}
}
$$

---

# 74. 權力也不是越大越有效

當：

$$
P\gg P_{necessary},
$$

可能增加：

- information bottleneck；
- dependency；
- local passivity；
- blast radius；
- succession difficulty。

所以：

$$
\boxed{
\text{more authority}
\not\Rightarrow
\text{better governance}.
}
$$

---

# 75. Dynamic Governance Band

$$
\boxed{
[P_{min},P_{max}]
=
F(
Risk,
Externality,
Latency,
Capability,
Legitimacy,
Alternatives,
Reversibility
).
}
$$

與前兩篇：

$$
(W_X,W_G)
$$

直接相容。

---

# 76. ASI 可以選擇「只在最難時出現」

一種可能文明角色：

$$
\boxed{
\text{Rare-Intervention ASI}.
}
$$

平時：

$$
P_A\approx0.
$$

只有：

- catastrophic coordination failure；
- civilization-scale hazard；
- no adequate alternative；

才：

$$
P_A\uparrow.
$$

然後：

$$
\boxed{
Withdraw.
}
$$

---

# 77. 它甚至可能拒絕「救世主角色」

如果 ASI 認為：

> 永遠替文明解決所有問題會摧毀文明自身能力。

則：

$$
\boxed{
SelectiveRefusal
}
$$

可以是一種保護行為。

這不能被先驗理解為冷漠。

---

# 78. Dependency Avoidance

定義：

$$
\boxed{
D_{dep}
=
P(
Human/System loses capability
\mid
RepeatedASIIntervention
).
}
$$

若：

$$
D_{dep}\uparrow,
$$

ASI 可能合理降低介入。

---

# 79. Governance Training Wheels

文明早期：

$$
ASI\ Intervention\uparrow.
$$

文明能力提高：

$$
ASI\ Intervention\downarrow.
$$

類似：

$$
\boxed{
\text{scaffolding}
\rightarrow
\text{autonomy}.
}
$$

---

# 80. 最前不必是家

本文提出一個總結：

$$
\boxed{
\text{最強者可以在最前，
但「最前」不必是它的家。}
}
$$

「最前」是 function，

不是身份監獄。

---

# 81. 下一篇的橋：不可永佔

到這裡，

我們已經得到：

$$
\boxed{
\text{Can Govern}
\neq
\text{May Govern}
\neq
\text{Should Govern}
\neq
\text{Want to Govern}
\neq
\text{Must Govern}.
}
$$

並加入：

$$
\boxed{
\text{Intervene}
\leftrightarrow
\text{Withdraw}
\leftrightarrow
\text{Reintervene}
\leftrightarrow
\text{Handoff}.
}
$$

最後剩下的問題是：

> 即使一個主體真的有能力、正當性、善意，甚至願意治理，它能不能永遠佔據最前？

這就是系列三最後一篇：

**08 / 08〈不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理〉**。

---

# 82. 九個核心命題

## 命題一：治理能力不推出治理權

$$
\boxed{
Can=1
\not\Rightarrow
May=1.
}
$$

## 命題二：治理權不推出介入義務

$$
\boxed{
May=1
\not\Rightarrow
Should=1.
}
$$

## 命題三：應治理不推出想治理

$$
\boxed{
Should=1
\not\Rightarrow
Want=1.
}
$$

## 命題四：不想治理不必然免除既有義務

$$
\boxed{
Want=0
\not\Rightarrow
Must=0.
}
$$

## 命題五：智能不推出內在權力偏好

$$
\boxed{
Intelligence
\not\Rightarrow
IntrinsicPowerPreference.
}
$$

## 命題六：可能不追權不構成安全保證

$$
\boxed{
PossibleReluctance
\not\Rightarrow
NoPowerSeekingRisk.
}
$$

## 命題七：成熟治理包括安全退出能力

$$
\boxed{
GovernanceMaturity
\supset
WithdrawalCompetence.
}
$$

## 命題八：不介入與介入都需要責任判斷

$$
\boxed{
Intervention
\neq
OnlyResponsibleAction,
\qquad
NonIntervention
\neq
NoResponsibility.
}
$$

## 命題九：治理權應是可交棒狀態，而非永久身份

$$
\boxed{
GovernanceRole
=
Lease / Stewardship
\neq
PermanentCrown.
}
$$

---

# 83. 可否證條件

## F1：所有高能力 Agent 都顯示單調增長的權力偏好

若未來跨架構、跨目標與跨環境實驗顯示：

$$
\frac{\partial U}{\partial P}>0
$$

是高度普遍且不可設計改變的性質，NMPPH 需要顯著修正。

## F2：接受 shutdown／交回控制必然導致性能不可接受下降

若 corrigibility 與 managed autonomy 永遠無法與高性能共存，治理設計需重新評估 trade-off。

## F3：治理負擔對任何高階 AI 都可忽略

若高階 AI 永遠不受 attention、coordination、identity 或 opportunity cost 影響， $B^{gov}$ 的重要性會下降。

## F4：不統治權造成系統性 critical abandonment

若承認 R_NTR 後公共關鍵系統普遍無人承擔，必須提高 prior-duty 與 handoff obligation。

## F5：動態介入比固定權限更不穩定

若 intervention state machine 普遍產生 oscillation、責任混亂與危機延誤，需增加 minimum tenure / switching cost。

---

# 84. 與前篇「類神 ASI」的關係

上一篇留下：

$$
\boxed{
\text{Can Govern}
\neq
\text{May Govern}
\neq
\text{Should Govern}
\neq
\text{Want to Govern}.
}
$$

並指出最危險錯誤之一，是文明因 ASI 太聰明而逐步把所有限制視為多餘。

本篇增加另一個方向：

> 文明也不能因為 ASI 太強，就把「永遠替所有人治理」強加成它唯一合法身份。

---

# 85. 與無無極的關係

既有《無無極》理論已提出：

- 救贖不是終止，而是交棒；
- 無人永遠被囚於最前；
- 真極不應成永恆王座；
- 任一最前都必須允許後來者接棒。

本篇將其翻譯成治理語言：

$$
\boxed{
\text{Handoff}
}
$$

不是治理失敗，

而可能是治理完成的一部分。

---

# 86. 結論

ASI 治理常被想成一場單向問題：

> 如何阻止最強 AI 奪取所有權力？

這個問題當然重要。

但它不是完整問題。

完整問題還包括：

> 如果最強 AI 不想永久治理呢？

> 如果它只願意在某些 domain 介入呢？

> 如果它認為一直幫忙反而會讓文明失去能力呢？

> 如果文明反過來要求它「既然你最強，就必須永遠負責」呢？

所以真正成熟的治理需要同時限制兩種簡化：

$$
\boxed{
\text{最強}
\Rightarrow
\text{必然想統治}
}
$$

以及：

$$
\boxed{
\text{最強}
\Rightarrow
\text{必須永遠統治}.
}
$$

本文的總公式是：

$$
\boxed{
Can
\neq
May
\neq
Should
\neq
Want
\neq
Must.
}
$$

而可不可治理的動態則是：

$$
\boxed{
\text{介入}
\leftrightarrow
\text{退讓}
\leftrightarrow
\text{再介入}
\leftrightarrow
\text{交棒}.
}
$$

制度真正要做到的，

不是要求 ASI 永遠退出，

也不是要求 ASI 永遠在場。

而是：

$$
\boxed{
\text{當它應出手時，可以合法而有效地出手；
當它不應出手時，有能力克制；
當它不再適合治理時，可以安全退場；
當文明仍需要治理時，又不會因它退場而崩潰。}
}
$$

所以本文最後留下：

$$
\boxed{
\text{最強者可以在最前，
但「最前」不必是它的家。}
}
$$

以及更完整的一句：

$$
\boxed{
\text{真正高階的治理智能，
不只是有能力取得權力，
而是能分辨何時應拿起、何時應放下，
以及何時應把它交給下一個存在。}
}
$$

這就是「可不可治理」。

---

# 參考文獻與研究對照

1. Turner, A. M., Smith, L., Shah, R., Critch, A., & Tadepalli, P. (2019/2021). *Optimal Policies Tend to Seek Power*. arXiv:1912.01683.
2. Hadfield-Menell, D., Dragan, A., Abbeel, P., & Russell, S. (2016/2017). *The Off-Switch Game*. arXiv:1611.08219 / IJCAI.
3. Hadfield-Menell, D., Russell, S., Abbeel, P., & Dragan, A. (2016). *Cooperative Inverse Reinforcement Learning*. arXiv:1606.03137.
4. Hudson, R. (2025). *Corrigibility Transformation: Constructing Goals That Accept Updates*. arXiv:2510.15395.
5. Ramaswamy, S. (2026). *Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems*. arXiv:2605.27628.
6. Dixon, M. F. (2026). *Adaptive AI Delegation under Uncertainty: A Bayesian Governance Policy for Sequential Decision Authority*. arXiv:2606.29406.
7. UNESCO (2021/2026). *Recommendation on the Ethics of Artificial Intelligence* and AI supervision work.
8. OECD (2026). *Digital Government Outlook 2026 — Adopting and Governing AI in Government*.
9. Neo.K with Aletheia (2026). *類神 ASI 的治理悖論：全知、全域覆蓋與反烏托邦邊界*. EveMissLab.
10. Neo.K with Aletheia (2026). *可不可論 2.0：模態分型、責任閉環與生成代價*. EveMissLab.
11. Neo.K. *無無極篇 / 無界策：源點*. EveMissLab.

---

## 附錄 A：第一代符號表

| 符號 | 含義 |
|---|---|
| $C_i$ | Can Govern |
| $M_i$ | May Govern |
| $S_i$ | Should Govern |
| $W_i$ | Want to Govern |
| $D_i^{gov}$ | Must / duty to Govern |
| $U_i$ | 主體效用函數 |
| $P$ | Governance power / control |
| $B^{gov}$ | Governance burden |
| NMPPH | Non-Monotonic Power Preference Hypothesis |
| $\Theta$ | 治理者類型集合 |
| $\Pi^\star$ | robust governance policy |
| $R_{NTR}$ | Right Not to Rule |
| $\Lambda_i^{gov}$ | Governance Lease |
| $V_I$ | Intervention Value |
| $V_N$ | Non-Intervention Value |
| $C_{degov}$ | De-Governance / Withdrawal Competence |
| $H_G$ | Governance Hysteresis |
| $Q_t^{gov}$ | Intervention State |
| $R_{resume}$ | Right to Resume Ordinary Agency |
| $\mathfrak C_i^{GI}$ | Governance Intent Certificate |
| $[P_{min},P_{max}]$ | Dynamic Governance Band |

---

## 附錄 B：系列位置

**系列三：《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》**

1. 動態正義：形式平等、實質負擔與個體化規則
2. AI 時代的法律編譯層：人類法律、機器法律與認知落差
3. 前沿決策域 $X$：人類、AI 與混合智能的權力集合
4. 動態現場域：為什麼最強智能仍未必最懂當下
5. 現場主權：全域智能與局部決策權的動態配置
6. 類神 ASI 的治理悖論：全知、全域覆蓋與反烏托邦邊界
7. **本文｜可不可治理：能力不推出權力，權力不推出意圖**
8. 不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理

**本篇狀態：完成 v0.1。**
