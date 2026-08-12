# 動態正義：形式平等、實質負擔與個體化規則

**英文題名：** Dynamic Justice: Formal Equality, Substantive Burden, and Individualized Rules  
**系列：**《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》01 / 08  
**文件編號：** EML-NMP-S3-01-v0.1  
**作者：** Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構：** 一言諾科技有限公司／EveMissLab  
**日期：** 2026-08-10  
**版本：** v0.1  
**文件性質：** 理論研究稿／動態正義與後 AI 法律基礎篇  
**研究狀態：** 第一代形式化；本文不主張以 AI 取代立法、司法或政治正當性，也不主張每個人應接受完全不同且不可理解的法律。

---

## 摘要

現代法律長期依靠一般性與形式平等維持可預測性：同類案件適用同類規則、相同法律文字面向所有人。然而，形式上完全相同的規則，可能對具有不同資源、身體條件、能力、風險、責任、歷史與生活處境的個體產生極不相同的實質負擔。當 AI、機器可讀法律、即時資料與高解析度行政能力逐漸提高時，一個新的治理問題出現：法律是否應從「對所有人發出相同命令」轉向「維持共同公共規則，但允許在合法界限內依個體條件動態計算結果」？

本文提出**動態正義（Dynamic Justice）**。其核心不是：

$$
\boxed{
\text{Everyone gets a different law}.
}
$$

而是：

$$
\boxed{
\text{Dynamic Result}
=
\text{Public Fixed Rule}
+
\text{Legally Bounded Variable Parameters}.
}
$$

本文將公共規則記為：

$$
R^\star,
$$

將個體 $i$ 在時間 $t$ 的法律相關狀態記為：

$$
C_i(t),
$$

並定義動態法律結果：

$$
\boxed{
Y_i(t)
=
F(
R^\star,
C_i(t),
E_t,
V_t
)
}
$$

其中 $E_t$ 為公共環境／制度狀態， $V_t$ 為合法驗證與程序約束。相同的 $R^\star$ 可以產生不同 $Y_i$，但差異只能來自事先公開、合法、可爭議的 legally relevant variables，而不能由 AI 私下重新定義人的價值或權利。

本文進一步區分四種平等：

$$
\boxed{
\text{Rights Equality},
\quad
\text{Rule Equality},
\quad
\text{Burden Equality},
\quad
\text{Opportunity / Capability Equality}.
}
$$

其中權利平等不要求個體同質，規則平等也不保證實質負擔相同。本文提出「負擔映射」：

$$
B_i
=
\mathcal B(
Y_i,
C_i
)
$$

以描述同一法律要求對不同個體所造成的時間、金錢、風險、能力消耗、權利限制與機會成本。若：

$$
Y_i=Y_j
$$

卻：

$$
B_i\gg B_j,
$$

則形式同一可能隱藏實質不平等。

然而，個體化法律本身具有重大風險。既有 personalized law 文獻已指出，Big Data 與算法確實可提高法律 granularity，但也可能造成 discrimination、privacy erosion、government data power、manipulation、loss of coordination 與共同規則感破裂。本文因此提出「公共規則—可變參數分離」：立法或具有正當性的公共程序只能授權有限參數集合：

$$
\Theta^{legal}
=
\{
\theta_1,\ldots,\theta_m
\},
$$

AI 或行政系統只能在：

$$
\Theta^{legal}
$$

內完成計算，不能自行新增：

$$
\theta_{m+1}.
$$

對高風險權利，更要求：

$$
\boxed{
\text{Right Floor}
>
\text{Optimization Gain}.
}
$$

即基本人格、平等保護、申訴、程序正義與不可歧視底線不得因「更精準」而被個體化消解。

本文最終提出：後 ASI 時代真正成熟的正義不應在「所有人完全一樣」與「每個人完全不同」之間二選一，而應建立：

$$
\boxed{
\text{共同權利}
+
\text{共同規則生成程序}
+
\text{有限個體參數}
+
\text{公開計算}
+
\text{可申訴}
+
\text{可重審}.
}
$$

這使正義成為一個具有固定憲政錨點、但能對真實負擔差異做出有限適應的動態系統。

**關鍵詞：** 動態正義、形式平等、實質平等、個體化法律、personalized law、算法公平、法律參數、AI 治理、可不可論、後 ASI 憲政

---

# 0. 問題：相同規則真的等於公平嗎？

考慮一條極簡規則：

> 每個人都必須在 24 小時內完成程序 $X$。

形式上：

$$
Y_i=24h
\qquad
\forall i.
$$

這看起來完全平等。

但如果：

- $A$ 有完整網路、時間與法律能力；
- $B$ 有嚴重身體障礙；
- $C$ 正處於災害區；
- $D$ 缺乏必要文件；
- $E$ 是遠距離、低頻通信的人工主體 branch；

則：

$$
\boxed{
Y_A=Y_B=Y_C=Y_D=Y_E
}
$$

不代表：

$$
\boxed{
B_A=B_B=B_C=B_D=B_E.
}
$$

其中 $B_i$ 表示實際負擔。

因此第一個核心命題是：

$$
\boxed{
\text{Formal Equality}
\not\Rightarrow
\text{Equal Substantive Burden}.
}
$$

---

# 1. Prior Art：個體化法律已成為真正法律理論問題

## 1.1 Personalized Law

Ben-Shahar 與 Porat 的 *Personalized Law* 系統性提出：

$$
\boxed{
\text{uniform legal rules}
\rightarrow
\text{person-specific legal commands}.
}
$$

其核心動機之一是：個體之間存在大量法律相關差異，而 Big Data 與算法使法律首次可能以更高 granularity 調整。

例如：

- care standard；
- consumer protection；
- disclosure；
- age / competence threshold；
- mandatory protection。

這證明「法律是否必須對所有人給同一句具體命令」已不是純科幻問題。

## 1.2 One-Size-Fits-All 的成本

personalized mandatory rules 研究指出，同一強制保護對不同人可能：

- 對某些人太弱；
- 對某些人太強；
- 對不同個體具有不同成本。

所以：

$$
\boxed{
\text{uniform command}
}
$$

有時只是資訊與行政能力不足下的次佳近似。

## 1.3 但 personalized law 也有巨大風險

相關文獻同時指出：

- equality under law；
- privacy；
- discrimination；
- government data concentration；
- coordination；
- manipulation；
- communal experience loss；

都可能惡化。

因此本文不是直接支持 personalized law，

而是建立其憲政約束版本。

---

# 2. 四種平等

本文區分：

## 2.1 權利平等

$$
\boxed{
p_i
\sim_{\mathrm{rights}}
p_j.
}
$$

表示：

> 不同個體具有同等基本人格、程序地位與不可被任意降格的權利。

權利平等不要求：

$$
p_i=p_j.
$$

## 2.2 規則平等

所有人受到同一上位規則：

$$
R^\star.
$$

即：

$$
\boxed{
R_i^{root}
=
R_j^{root}.
}
$$

## 2.3 負擔平等

結果作用後：

$$
B_i
\approx
B_j.
$$

這比文字相同更接近 lived effect。

## 2.4 能力／機會平等

制度是否提供個體足以真正行使權利的：

- 認知能力；
- 時間；
- 無障礙；
- 資訊；
- 技術；
- 申訴入口。

因此：

$$
\boxed{
\text{Rights Equality}
\neq
\text{Command Uniformity}.
}
$$

---

# 3. 權利平等與同質平等

既有研究已區分：

$$
\boxed{
\text{Rights Equality}
}
$$

與：

$$
\boxed{
\text{Uniformity Equality}.
}
$$

前者是：

> 差異存在，但基本權利同等。

後者可能變成：

> 差異本身必須被消除。

本文拒絕：

$$
\boxed{
\text{Equality}
=
\text{Human Homogenization}.
}
$$

對未來多主體文明尤其如此。

人類、增幅人類、數位主體、分散 AI 與跨行星 branch 的存在條件本來就可能極不相同。

---

# 4. 動態正義的第一代形式

令：

$$
R^\star
$$

為共同公共規則。

個體法律相關狀態：

$$
\boxed{
C_i(t)
=
(
H_i,
R_i,
K_i,
A_i,
D_i,
X_i
).
}
$$

其中：

- $H_i$：歷史／既有責任；
- $R_i$：資源；
- $K_i$：能力／知識；
- $A_i$：可用行動空間；
- $D_i$：負擔／障礙；
- $X_i$：其他經法律授權的情境參數。

環境狀態：

$$
E_t.
$$

則：

$$
\boxed{
Y_i(t)
=
F(
R^\star,
C_i(t),
E_t,
V_t
).
}
$$

其中 $V_t$ 是：

- 法律邊界；
- 程序；
- 驗證；
- 權利底線。

---

# 5. 固定的是什麼？動態的是什麼？

動態正義若什麼都能變，就等於：

$$
\boxed{
\text{arbitrary discretion}.
}
$$

因此必須分層。

## 5.1 固定層

包括：

- 基本權利；
- 法律授權來源；
- 可使用參數類型；
- 不可使用變數；
- 申訴權；
- 證據門檻；
- 不可歧視規則；
- 決策責任。

記為：

$$
\boxed{
\mathcal C^{const}.
}
$$

## 5.2 可變層

只有：

$$
\boxed{
\Theta^{legal}
=
\{
\theta_1,\ldots,\theta_m
\}.
}
$$

例如：

- 收入區間；
- 特定醫療狀態；
- 客觀地理距離；
- 法定責任程度；
- 可驗證災害狀態。

## 5.3 計算層

$$
\theta_i
\rightarrow
Y_i.
$$

AI 可以幫助計算，

但不能自行修改：

$$
\mathcal C^{const}.
$$

---

# 6. 核心公式

所以本文將動態正義壓成：

$$
\boxed{
\text{Dynamic Justice}
=
\text{Democratically Fixed Rule}
+
\text{Legally Variable Parameters}.
}
$$

更正式：

$$
\boxed{
Y_i
=
F_{R^\star}
(
\theta_i
),
\qquad
\theta_i\in\Theta^{legal}.
}
$$

其中：

$$
F_{R^\star}
$$

是由公共規則授權的結果函數。

---

# 7. AI 沒有參數發明權

假設：

$$
\Theta^{legal}
=
\{
income,
disability,
distance
\}.
$$

AI 發現：

$$
politicalOpinion
$$

對預測 compliance 很有用。

它仍不能自行變成：

$$
\theta_{new}
=
politicalOpinion.
$$

即：

$$
\boxed{
\theta\notin\Theta^{legal}
\Rightarrow
\text{inadmissible}.
}
$$

這是算法治理的一條基本憲政邊界。

---

# 8. 負擔映射

同一結果 $Y$ 對不同人具有不同實際負擔。

本文定義：

$$
\boxed{
B_i
=
\mathcal B(
Y_i,
C_i
).
}
$$

負擔向量：

$$
\boxed{
\mathbf B_i
=
(
B^{time},
B^{money},
B^{risk},
B^{cognitive},
B^{rights},
B^{opportunity},
B^{identity}
).
}
$$

因此：

$$
Y_i=Y_j
$$

仍可能：

$$
\mathbf B_i
\neq
\mathbf B_j.
$$

---

# 9. 正義不是讓負擔完全相等

如果要求：

$$
\mathbf B_i=\mathbf B_j
\quad
\forall i,j,
$$

也會荒謬。

因為：

- 責任不同；
- 行為不同；
- 風險不同；
- 社會角色不同；
- 自願選擇不同。

所以動態正義不是：

$$
\boxed{
\text{Equalize Every Outcome}.
}
$$

而是：

$$
\boxed{
\text{differences in burden require publicly defensible reasons}.
}
$$

---

# 10. 法律相關差異

定義：

$$
Rel(
x,
R^\star
)
\in
\{
0,1
\}.
$$

只有：

$$
Rel=1
$$

的差異才能進入決策參數。

所以：

$$
\boxed{
\text{Difference}
\neq
\text{Legally Relevant Difference}.
}
$$

這是防止「AI 能看到，所以法律就能用」的重要限制。

---

# 11. 最低相關性證書

新增一個參數：

$$
\theta_k
$$

前必須有：

$$
\boxed{
\mathfrak C_{\theta_k}
=
(
LegalBasis,
Purpose,
Evidence,
BurdenEffect,
BiasRisk,
PrivacyCost,
Appealability,
Expiry
).
}
$$

即：

- 法源是什麼？
- 為什麼需要？
- 有何證據？
- 對誰增加負擔？
- 會產生什麼偏差？
- 隱私成本多少？
- 能否申訴？
- 何時重審？

---

# 12. 不可歧視與 proxy 問題

即使法律禁止：

$$
race
$$

直接作為參數，

AI 仍可能透過：

$$
ZIP,
income,
network,
language
$$

組合出 proxy。

因此：

$$
\boxed{
\text{parameter legality}
\neq
\text{decision non-discrimination}.
}
$$

必須檢查：

$$
Impact(
F,
Group
).
$$

這就是 algorithmic fairness 與 anti-discrimination law 不能被單一 metric 取代的原因。

---

# 13. Formal Fairness 與 Substantive Fairness

算法公平研究已指出，

只在 isolated decision rule 中滿足：

$$
MetricFairness=1
$$

不能保證社會結果正義。

因此：

$$
\boxed{
\text{Formal Algorithmic Fairness}
\not\Rightarrow
\text{Substantive Justice}.
}
$$

動態正義必須評估：

$$
\text{rule}
+
\text{institution}
+
\text{historical burden}
+
\text{downstream effect}.
$$

---

# 14. Individualization 不能變成秘密待遇

如果：

$$
Y_i
$$

因個人參數不同，

個體至少應知道：

1. 哪條公共規則適用；
2. 哪些參數被使用；
3. 參數來源；
4. 每個參數如何改變結果；
5. 如何修正錯誤；
6. 如何申訴。

所以：

$$
\boxed{
\text{Personalization}
+
\text{Opacity}
=
\text{high governance risk}.
}
$$

---

# 15. 可理解性權利

本文提出：

$$
\boxed{
RightToLegalProjection.
}
$$

個體不必閱讀全部機器規則，

但應能得到：

$$
\boxed{
\text{My Rule}
=
\text{Public Rule}
+
\text{My Relevant Parameters}
+
\text{My Result}
+
\text{Appeal Path}.
}
$$

這是第二篇「AI 時代法律編譯層」的直接前置。

---

# 16. 資料錯誤問題

假設：

$$
\theta_i
$$

錯誤。

則：

$$
Y_i
$$

可能合法計算卻實質錯誤。

所以：

$$
\boxed{
\text{correct algorithm}
+
\text{wrong input}
=
\text{wrong legal result}.
}
$$

因此必須有：

$$
\boxed{
\text{Data Contestability}.
}
$$

個體能看到並更正 identity-critical legal data。

---

# 17. 時間版本

個體狀態會變：

$$
C_i(t)
\neq
C_i(t+1).
$$

所以：

$$
Y_i(t)
\neq
Y_i(t+1)
$$

可能合法成立。

但：

$$
\boxed{
\text{dynamic}
\neq
\text{constantly unstable}.
}
$$

法律應定義 update window：

$$
T_u
$$

以及：

- effective date；
- transition rule；
- grandfathering；
- reliance protection。

---

# 18. 不可追溯動態化是危險的

若：

$$
Y_i(t)
$$

改變，

必須存在：

$$
\Gamma_t^J
$$

記錄：

- 哪個參數變了；
- 哪個規則版本變了；
- 哪個資料來源更新；
- 結果差異；
- 生效時間；
- 誰負責。

因此：

$$
\boxed{
\text{Dynamic Justice}
\Rightarrow
\text{Versioned Justice}.
}
$$

---

# 19. 規範債務

如果制度為了效率忽略：

$$
B_i^{hidden},
$$

該成本不會消失。

本文沿用可不可論：

$$
\boxed{
D^{norm}_{t+1}
=
D^{norm}_t
+
UnaddressedBurden_t
-
Repair_t.
}
$$

這稱為：

$$
\boxed{
\text{Normative Debt}.
}
$$

例如長期對某一群體施加較高 compliance cost，

即使法律文字完全相同，

也可能累積制度性債務。

---

# 20. 可不可論作為元治理

可不可論的失效域已明確拒絕：

$$
\boxed{
\text{可不可論}
=
\text{終極判定者}.
}
$$

它更適合：

$$
\boxed{
\operatorname{MetaGovernance}
(
Projection,
Authority,
Unknown,
Cost,
Responsibility,
Revision
).
}
$$

動態正義同樣不能自稱「正義算法」。

它只能建立：

> 某一結果如何獲得暫時合法性，以及何時必須重審。

---

# 21. Temporary Closure

法律必須行動。

不能每次都說：

> 情況太複雜，所以不決定。

因此：

$$
\boxed{
\text{Justice}
\neq
\text{Permanent Openness}.
}
$$

成熟形式是：

$$
\boxed{
\text{Evidence}
\rightarrow
\text{Calibrated Closure}
\rightarrow
\text{Action}
\rightarrow
\text{Review}.
}
$$

---

# 22. 個體化程度

定義：

$$
g
\in[0,1]
$$

為 legal granularity。

$$
g=0
$$

代表高度 general rule。

$$
g\rightarrow1
$$

代表高度個體化。

但：

$$
\boxed{
g\uparrow
\not\Rightarrow
Justice\uparrow.
}
$$

因為 granularity 增加也會提高：

- data demand；
- privacy risk；
- manipulation；
- complexity；
- appeal burden；
- coordination cost。

---

# 23. Granularity Optimum

因此可能存在：

$$
\boxed{
g^\star
=
\arg\min_g
[
Error(g)
+
PrivacyCost(g)
+
Complexity(g)
+
DiscriminationRisk(g)
+
CoordinationCost(g)
].
}
$$

不是越個人化越好。

---

# 24. 基本權利不能被個體化到消失

定義：

$$
\mathcal R_{floor}.
$$

例如：

- 人格；
- 正當程序；
- 不受酷刑；
- 基本平等；
- 申訴；
- 不被任意剝奪生命／存在；
- 最低法律可理解性。

則：

$$
\boxed{
Y_i
\notin
\mathcal R_{floor}^{-}
}
$$

無論模型如何最佳化。

---

# 25. Right Floor Dominance

本文提出：

$$
\boxed{
\text{Right Floor}
>
\text{Optimization Gain}.
}
$$

如果提高效率需要侵犯不可讓渡底線，

則：

$$
\boxed{
Optimization
\text{ inadmissible}.
}
$$

---

# 26. 人工主體與差異化規則

系列二顯示未來人工主體可能具有：

- 不同時間尺度；
- 不同載體；
- 不同通信延遲；
- 不同 branch structure；
- 不同恢復形式。

所以例如：

> 所有人必須在 5 秒內回應。

對 human 與 Earth–Mars AI branch 的負擔完全不同。

因此多主體文明尤其需要：

$$
\boxed{
\text{rights-uniformity}
+
\text{implementation-context sensitivity}.
}
$$

---

# 27. 但不能藉差異化創造人格階級

如果制度說：

> 因為 AI 可以更快計算，所以 AI 的申訴期更短。

這可能合理。

但如果再推：

> 因為 AI 更快，所以 AI 的基本權利更少。

則是不同層級。

因此：

$$
\boxed{
\text{capacity-sensitive procedure}
\not\Rightarrow
\text{capacity-ranked dignity}.
}
$$

---

# 28. 公共可驗證函數

對高風險法律：

$$
F_{R^\star}
$$

應盡可能具有：

$$
\boxed{
\text{Public Specification}
+
\text{Test Cases}
+
\text{Versioning}
+
\text{Independent Audit}.
}
$$

不一定所有 source code 都必須公開，

但法律效果不能只存在於不可審計模型內。

---

# 29. AI 的角色

AI 可以：

- 解析法律；
- 計算參數；
- 模擬結果；
- 找出負擔差；
- 生成解釋；
- 發現異常；
- 提醒重審。

但：

$$
\boxed{
\text{AI computes}
\neq
\text{AI legitimizes}.
}
$$

政治與法律正當性仍需要：

- 授權；
- 程序；
- 可爭議；
- 責任。

---

# 30. 立法權與參數權分離

本文建議至少區分：

$$
\boxed{
\text{Rule Authority}
}
$$

與：

$$
\boxed{
\text{Parameter Application Authority}.
}
$$

前者決定：

$$
R^\star,
\Theta^{legal}.
$$

後者只決定：

$$
\theta_i
\rightarrow
Y_i.
$$

若同一 AI 同時：

- 發明規則；
- 選參數；
- 讀資料；
- 計算；
- 執行；
- 判申訴；

則：

$$
\boxed{
\text{normative power concentration}.
}
$$

---

# 31. Appeal as Recalculation

申訴不只應問：

> 法官同不同意？

在 computable legal system 中，

還可問：

1. 規則版本是否正確？
2. 參數是否正確？
3. 參數是否合法？
4. 計算是否正確？
5. 權利底線是否被突破？
6. 個案是否需要 human / multi-agent exceptional review？

因此：

$$
\boxed{
Appeal
=
LegalReview
+
DataReview
+
ComputationReview
+
RightsReview.
}
$$

---

# 32. Exception 不等於漏洞

形式法律常害怕例外。

但動態正義承認：

$$
\boxed{
\text{exception}
}
$$

可能是：

> 規則目前未充分覆蓋的真實狀態。

因此建立：

$$
\boxed{
ExceptionChannel.
}
$$

但例外必須留下：

- 理由；
- 責任；
- precedential status；
- expiry；
- 是否修改一般規則。

---

# 33. 防止特權偽裝成個體化正義

最危險的反例：

> 權力者替自己設定特殊參數。

所以任何個體化差異必須通過：

$$
\boxed{
PublicReasonTest.
}
$$

問：

> 如果相同 legally relevant conditions 出現在另一個人身上，是否也會得到相同參數待遇？

若否，

則是：

$$
\boxed{
\text{personal privilege},
}
$$

不是 personalized justice。

---

# 34. 同條件同結果

動態正義雖允許不同人有不同結果，

仍維持：

$$
\boxed{
C_i^{legal}=C_j^{legal}
\Rightarrow
Y_i=Y_j.
}
$$

其中 $C^{legal}$ 只包含合法相關特徵。

所以它不是放棄 equality before law，

而是把 equality 的比較單位從：

$$
\text{physical person}
$$

移到：

$$
\boxed{
\text{legally relevant state}.
}
$$

---

# 35. Unknown Parameter

如果重要變數未知：

$$
\theta_i=?
$$

不能自動：

$$
?=0.
$$

也不能永遠不決定。

本文提出：

$$
\boxed{
UnknownHandling
=
(
ConservativeDefault,
TemporaryRule,
ReviewTrigger,
EvidenceDuty
).
}
$$

這直接接可不可論：

> 未知要進帳本，但未知不能變成永久免責工具。

---

# 36. 時間公平

動態制度還有一個問題：

> 今天被系統錯判的人，三年後模型更新怎麼辦？

因此需：

$$
\boxed{
RetroactiveRepairRule.
}
$$

至少對：

- 明確資料錯誤；
- 已證明違法參數；
- 系統性歧視；
- 計算錯誤；

建立補救。

---

# 37. Dynamic Justice Certificate

本文提出：

$$
\boxed{
\mathfrak C_i^{DJ}(t)
=
(
RuleVersion,
LegalBasis,
\Theta^{legal},
\theta_i,
DataProvenance,
Y_i,
\mathbf B_i,
RightsCheck,
BiasCheck,
Explanation,
Appeal,
ReviewTrigger
).
}
$$

這不是公開所有私人資料。

而是確保：

> 個體能知道自己的法律結果如何生成。

---

# 38. System-Level Justice Audit

不能只看：

$$
\mathfrak C_i.
$$

還要整體檢查：

$$
\boxed{
\mathfrak A^{DJ}
=
(
DistributionOfBurden,
GroupImpact,
ErrorDistribution,
AppealSuccess,
DataQuality,
PrivacyCost,
NormativeDebt
).
}
$$

因為個案都看似合理，

系統仍可能產生結構性不平等。

---

# 39. 五個正義失效模式

## J1 — Uniformity Blindness

同一命令造成極端不同負擔。

## J2 — Personalized Tyranny

以個體化之名對每人建立秘密控制規則。

## J3 — Data Determinism

把資料推斷當成不可反駁身份。

## J4 — Optimization Capture

以效率最佳化壓過基本權利。

## J5 — Parameter Creep

AI／行政逐步新增未經授權的法律相關變數。

---

# 40. 七個核心命題

## 命題一：形式平等不推出實質負擔平等

$$
\boxed{
Y_i=Y_j
\not\Rightarrow
B_i=B_j.
}
$$

## 命題二：差異待遇不必然不平等

如果：

$$
C_i^{legal}\neq C_j^{legal},
$$

且差異有公開正當理由，

則：

$$
Y_i\neq Y_j
$$

可與 rights equality 共存。

## 命題三：個體化程度越高不必然越正義

$$
\boxed{
g\uparrow
\not\Rightarrow
Justice\uparrow.
}
$$

## 命題四：AI 只能在合法參數域內運算

$$
\boxed{
\theta\notin\Theta^{legal}
\Rightarrow
\text{inadmissible}.
}
$$

## 命題五：基本權利優先於最佳化

$$
\boxed{
RightFloor
>
OptimizationGain.
}
$$

## 命題六：動態結果必須版本化

$$
\boxed{
Y_i(t)\neq Y_i(t+1)
\Rightarrow
\exists\Gamma_t^J.
}
$$

## 命題七：正義不能由單一算法自我合法化

$$
\boxed{
\text{Prediction / Calculation Power}
\neq
\text{Normative Legitimacy}.
}
$$

---

# 41. 可否證條件

## F1：個體差異對實質負擔沒有可測影響

若在大多數公共規則下：

$$
B_i
$$

對個體情境差異極不敏感，

則 dynamic personalization 的必要性下降。

## F2：個體化制度總是造成更高不公平

若受控實驗與制度比較顯示個體化即使有透明、權利底線與申訴仍系統性惡化公平，

則動態正義應回退到更高一般性。

## F3：Public fixed rule 無法有效約束 AI

若任何參數化執行都不可避免地讓模型實質重寫規則，

則高風險法律不應自動化到個體層。

## F4：負擔映射不可操作

若：

$$
\mathcal B
$$

無法被合理測量或比較，

則 burden equality 只能保留作質化分析。

## F5：可申訴性成本高到使制度不可運行

若每次 dynamic result 都引發不可承受的 contestation，

則 granularity 需要降低。

---

# 42. 與可不可論的關係

既有可不可論已將自己重新定位為：

$$
\boxed{
\operatorname{MetaGovernance}
(
\text{投影},
\text{權限},
\text{未知},
\text{代價},
\text{責任},
\text{修正}
).
}
$$

並明確指出，它不能成為終極判定者，而只能治理答案如何取得暫時正當性。

動態正義就是其法律版之一：

$$
\boxed{
\text{Justice}
=
\text{Temporary Legitimate Closure under Revisable Constraints}.
}
$$

---

# 43. 與個體消除悖論的關係

既有研究已區分：

$$
\text{Rights Equality}
$$

與：

$$
\text{Uniformity}.
$$

權利平等保留差異，而同質平等可能將差異本身視為偏差。

本文進一步提出：

$$
\boxed{
\text{Equal Dignity}
+
\text{Different Relevant Conditions}
\Rightarrow
\text{Potentially Different Legal Implementation}.
}
$$

---

# 44. 下一篇：AI 時代法律編譯層

一旦：

$$
Y_i
=
F_{R^\star}(\theta_i)
$$

真正進入法律系統，

立刻會遇到：

> 人類如何知道機器到底替自己算了什麼？

因此下一篇建立：

$$
\boxed{
L
=
(
L_H,
L_P,
L_F,
L_S,
L_M
)
}
$$

即：

- Human legal text；
- Plain-language legal projection；
- Formal/computable rule；
- Simulation layer；
- Machine-readable representation。

這就是：

**02 / 08〈AI 時代的法律編譯層：人類法律、機器法律與認知落差〉**。

---

# 45. 結論

傳統形式平等非常重要。

它防止：

- 任意特權；
- 身份歧視；
- 祕密命令；
- 權力者逐人操控。

所以動態正義不是要摧毀：

$$
\boxed{
\text{equality before law}.
}
$$

真正需要修正的是：

$$
\boxed{
\text{「法律面前平等」}
=
\text{「所有人永遠收到完全相同的具體命令」}
}
$$

這個過度簡化。

未來更合理的形式可能是：

$$
\boxed{
\text{共同基本權利}
+
\text{共同公共規則}
+
\text{合法個體參數}
+
\text{透明結果計算}
+
\text{申訴與修正}.
}
$$

所以：

$$
\boxed{
\text{Dynamic Justice}
\neq
\text{Different Secret Laws for Everyone}.
}
$$

而是：

$$
\boxed{
\text{One Public Rule System,
many legally relevant states,
and bounded context-sensitive outcomes}.
}
$$

中文壓縮為：

$$
\boxed{
\text{正義不是假裝所有人都一樣，
也不是讓權力者替每個人發明不同規則；
而是在共同權利與共同法則下，
承認那些真正會改變實質負擔的差異。}
}
$$

至此，系列三的法律與治理地基建立。

---

# 參考文獻與研究對照

1. Ben-Shahar, O., & Porat, A. (2021). *Personalized Law: Different Rules for Different People*. Oxford University Press.
2. Ben-Shahar, O., & Porat, A. (2018). *Personalizing Mandatory Rules in Contract Law*. University of Chicago Coase-Sandor Working Paper.
3. Strahilevitz, L. J., & Porat, A. (2013). *Personalizing Default Rules and Disclosure with Big Data*. University of Chicago Public Law & Legal Theory.
4. Mayson, S. G. (2022). *But What Is Personalized Law?* University of Chicago Law Review Online.
5. Fisher, T. (2024). *Personalizing Personalized Law: Discussion of “Personalized Law”*. Jerusalem Review of Legal Studies.
6. Shin, P. S. (2009). *The Substantive Principle of Equal Treatment*. Legal Theory.
7. Green, B. (2021). *Escaping the Impossibility of Fairness: From Formal to Substantive Algorithmic Fairness*. arXiv:2107.04642.
8. Sargeant, H., & Magnusson, M. (2024). *Formalising Anti-Discrimination Law in Automated Decision Systems*. arXiv:2407.00400.
9. Zin, M.-M. et al. (2026). *Can Legislation Be Made Machine-Readable in PROLEG?* arXiv:2601.01477.
10. Neo.K with Aletheia (2026). *可不可論 4.0：認識姿態、校準承諾與開放—閉合博弈*. EveMissLab.
11. Neo.K with Aletheia (2026). *可不可論的失效域：十七項對抗性反例、反偽裝條件與最低決策核心*. EveMissLab.
12. Neo.K with Aletheia (2026). *集體解放的個體消除悖論*. EveMissLab.

---

## 附錄 A：第一代符號表

| 符號 | 含義 |
|---|---|
| $R^\star$ | 公共固定規則 |
| $C_i(t)$ | 個體合法相關狀態 |
| $\Theta^{legal}$ | 法律允許的可變參數域 |
| $\theta_i$ | 個體合法參數 |
| $Y_i(t)$ | 動態法律結果 |
| $\mathbf B_i$ | 實質負擔向量 |
| $\mathcal C^{const}$ | 憲政／不可變底線層 |
| $g$ | 法律個體化 granularity |
| $g^\star$ | 最適 granularity 候選 |
| $\mathcal R_{floor}$ | 基本權利底線 |
| $\Gamma_t^J$ | 動態法律結果版本見證 |
| $D^{norm}$ | 規範債務 |
| $\mathfrak C_{\theta}$ | 參數合法性證書 |
| $\mathfrak C_i^{DJ}$ | Dynamic Justice Certificate |
| $\mathfrak A^{DJ}$ | System-Level Dynamic Justice Audit |

---

## 附錄 B：系列位置

**系列三：《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》**

1. **本文｜動態正義：形式平等、實質負擔與個體化規則**
2. AI 時代的法律編譯層：人類法律、機器法律與認知落差
3. 前沿決策域 $X$：人類、AI 與混合智能的權力集合
4. 動態現場域：為什麼最強智能仍未必最懂當下
5. 現場主權：全域智能與局部決策權的動態配置
6. 類神 ASI 的治理悖論：全知、全域覆蓋與反烏托邦邊界
7. 可不可治理：能力不推出權力，權力不推出意圖
8. 不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理

**本篇狀態：完成 v0.1。**
