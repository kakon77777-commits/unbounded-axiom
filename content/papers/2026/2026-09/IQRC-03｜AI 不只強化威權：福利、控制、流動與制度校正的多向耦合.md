# IQRC-03｜AI 不只強化威權：福利、控制、流動與制度校正的多向耦合

**English Title:** *AI Does Not Only Strengthen Authoritarianism: Multidirectional Coupling Across Welfare, Control, Mobility, and Institutional Correction*  
**系列：**《制度智能、類全域 AI 與可重開文明系列》  
**Series:** *Institutional Intelligence, Quasi-Global AI, and Reopenable Civilization Series*  
**篇次：** Paper 03 / 08  
**文件編號：** EML-IQRC-03-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** AI 政治經濟學／比較政治／制度智能／雙重用途技術／治理動力學  
**狀態：** Canonical Draft / Multidirectional Coupling Foundation  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

人工智慧與政治的公共討論經常落入兩種單向敘事。第一種認為 AI 必然強化威權，因為它降低監控、審查、預測與精準干預的成本；第二種則認為 AI 必然改善治理，因為它可以提高生產率、公共服務、行政效率、知識可及性與政策品質。兩者都抓到部分真實，卻都把一個多向耦合系統錯寫成固定符號的單一因果鏈。

本文承接 IQRC-01 的制度—智能共演化模型與 IQRC-02 的中國歷史壓力測試，提出「AI 政治耦合矩陣」。令政治—社會狀態向量為：

$$
\mathbf X_t
=
(
W,
M,
D,
C_S,
C_C,
P,
R,
Q,
L
)_t,
$$

其中 $W$ 為福利、 $M$ 為流動、 $D$ 為相對剝奪、 $C_S$ 為國家能力、 $C_C$ 為公民能力、 $P$ 為參與與可爭議性、 $R$ 為制度可逆與校正能力、 $Q$ 為資訊品質、 $L$ 為合法性。令 AI 作用向量為：

$$
\mathbf A_t
=
(
A_P,
A_O,
A_G,
A_C,
A_I,
A_D,
A_R,
A_M
)_t,
$$

分別表示生產率、組織、治理、控制、創新、分配、修訂與大規模互動增幅。

本文的核心對象是：

$$
\boxed{
J_t
=
\left[
\frac{
\partial X_i
}{
\partial A_j
}
\right]_t.
}
$$

傳統單向敘事等同假定某些 $J_{ij}$ 永遠為正或永遠為負；本文主張更合理的形式是：

$$
\boxed{
\operatorname{sign}
\left(
J_{ij}
\right)
=
\sigma_{ij}
(
I_t,
O_t,
R_t,
D_t,
B_t,
\tau
),
}
$$

即 AI 對同一政治變量的作用符號會受到制度、所有權、權利保障、資料結構、分配結構與時間尺度影響。

例如，AI 提高行政效率可能改善福利與公共服務，也可能提高監控與精準干預能力；AI 提高普通人的知識槓桿可能擴張社會流動與法律能力，也可能同時提高頂尖資本與大型組織的規模優勢；AI 對工作世界的作用更可能首先表現為任務轉型，而非單純「全部替代」或「全部增幅」。ILO 2025–2026 的研究指出，全球約四分之一就業位於某種 GenAI 暴露範圍，但就目前能力而言，多數受影響職位更可能經歷任務與工作內容轉型，而不是完整消失；2026 年 ILO–World Bank 的跨國研究進一步指出，發展中經濟體可能先承受擾動，再取得較晚的生產率紅利。這正支持本文的核心：同一技術能力在不同結構中不具有固定分配結果。

公共治理亦呈現相同雙向性。OECD 2025–2026 的研究指出，政府 AI 可以自動化與個人化服務、支援決策與偵測詐欺，但偏誤、透明度不足、過度依賴與數位落差也可能損害公平、責任與信任。Freedom House 2025 則將 AI 支援的審查、資訊操弄與監控視為數位壓迫的新放大器，同時指出民主制度亦需要監督、比例原則、隱私與救濟，才能避免強力監測工具傷害權利。這些材料共同說明，真正的研究問題不是「AI 到底是自由還是威權的工具」，而是：

$$
\boxed{
\text{Which institutional topology converts which AI capability into which social consequence?}
}
$$

本文最後提出直接效應、第二階效應、制度回授、能力不對稱、短期穩定—長期可逆性分離、AI 治理單點失效與可檢驗預測，並為 Paper 04 的「制度塑造智能」建立正式數學接口。

---

## 關鍵詞

AI 政治耦合；雙重用途 AI；威權韌性；民主治理；公共服務；監控；社會流動；制度校正；Agentic AI；國家能力；公民能力；AI 政治經濟學；制度智能；多向耦合；符號不固定

---

# 0. 問題重構：AI 是自由的工具，還是控制的工具？

這個問題本身就是錯的型別。

同一 AI 技術可以：

- 幫助醫院分診；
- 幫助人民理解法律；
- 幫助政府偵測詐欺；
- 幫助企業提高生產率；
- 幫助警方分析高風險事件；
- 幫助情報機構進行監測；
- 幫助政黨分析輿情；
- 幫助公民查證政府說法；
- 幫助平台過濾內容；
- 幫助使用者突破語言與知識門檻。

因此：

$$
\boxed{
AI
\neq
\text{intrinsically democratic}
}
$$

且：

$$
\boxed{
AI
\neq
\text{intrinsically authoritarian}.
}
$$

更精確的研究問題是：

$$
\boxed{
AI
\times
Institution
\times
Ownership
\times
Rights
\times
Access
\rightarrow
PoliticalEffects.
}
$$

---

# 1. 從單一因果鏈轉向耦合矩陣

## 1.1 政治—社會狀態向量

本文定義：

$$
\boxed{
\mathbf X_t
=
(
W,
M,
D,
C_S,
C_C,
P,
R,
Q,
L
)_t.
}
$$

其中：

- $W$：Welfare，實質福利與可行生活；
- $M$：Mobility，社會與能力流動；
- $D$：Relative Deprivation，相對剝奪與位置落差；
- $C_S$：State Capacity，國家執行、感知與協調能力；
- $C_C$：Citizen Capacity，公民知識、法律、組織與行動能力；
- $P$：Participation / Contestability，參與與可爭議性；
- $R$：Revision / Reversibility，修正、覆核、替代與回退能力；
- $Q$：Epistemic Quality，資訊多樣性、可信度與可驗證性；
- $L$：Legitimacy，多維正當性。

---

## 1.2 AI 作用向量

沿用 Paper 01：

$$
\boxed{
\mathbf A_t
=
(
A_P,
A_O,
A_G,
A_C,
A_I,
A_D,
A_R,
A_M
)_t.
}
$$

其中：

- $A_P$：生產率增幅；
- $A_O$：組織與工作流增幅；
- $A_G$：治理與行政增幅；
- $A_C$：監控、審查、風險控制與選擇性干預增幅；
- $A_I$：創新與科研增幅；
- $A_D$：分配、配對與資源調度增幅；
- $A_R$：制度修正、審計、反例與錯誤校正增幅；
- $A_M$：面向大眾的持續互動增幅。

---

# 2. AI 政治耦合矩陣

定義：

$$
\boxed{
J_t
=
\left[
J_{ij,t}
\right]
=
\left[
\frac{
\partial X_{i,t+1}
}{
\partial A_{j,t}
}
\right].
}
$$

若：

$$
J_{ij}>0,
$$

則增加 AI 能力 $A_j$ 傾向增加政治狀態 $X_i$。

若：

$$
J_{ij}<0,
$$

則傾向降低。

若：

$$
J_{ij}\approx0,
$$

則直接作用弱。

但最重要的是：

$$
\boxed{
J_{ij}
\neq
\text{constant}.
}
$$

---

# 3. 條件符號命題

本文提出：

$$
\boxed{
\operatorname{sign}
(
J_{ij,t}
)
=
\sigma_{ij}
(
I_t,
O_t,
R_t,
D_t,
B_t,
\tau
).
}
$$

其中：

- $I_t$：制度結構；
- $O_t$：AI、資料與基礎設施所有權；
- $R_t$：權利、程序與救濟結構；
- $D_t$：資料與資訊分布；
- $B_t$：利益分配與議價結構；
- $\tau$：時間尺度。

因此同一 AI 能力在不同制度與時間尺度下可以換號。

---

# 4. 第一個例子：生產率增幅不是固定福利增幅

假設：

$$
A_P\uparrow.
$$

直接效果：

$$
Output\uparrow.
$$

但家庭福利：

$$
W_H
$$

取決於：

$$
\boxed{
W_H
=
f(
Productivity,
Wages,
Ownership,
Prices,
Taxes,
Transfers,
FreeTime,
JobSecurity
).
}
$$

因此：

$$
\frac{
\partial W_H
}{
\partial A_P
}
$$

沒有無條件固定正號。

---

# 5. 生產率紅利的三種分配相位

## 5.1 廣泛增幅

$$
A_P
\rightarrow
Wages\uparrow
+
FreeTime\uparrow
+
Prices\downarrow.
$$

則：

$$
J_{W,A_P}>0.
$$

---

## 5.2 集中增幅

$$
A_P
\rightarrow
CapitalReturn\uparrow
+
LaborShare\downarrow.
$$

此時：

$$
GDP\uparrow
$$

仍可能：

$$
MedianWelfare
$$

增長有限。

---

## 5.3 轉型延遲

2026 年 ILO–World Bank 研究提出「disruption without dividend」風險：部分發展中經濟體可能先遭遇工作流程與任務擾動，但因數位基礎、技能或企業吸收能力不足，生產率紅利較晚到來。

因此：

$$
\boxed{
\text{Exposure Time}
<
\text{Dividend Time}
}
$$

可能成立。

---

# 6. 工作：Transformation 不等於 Replacement

ILO 2025 全球研究指出：

$$
\boxed{
\text{about one in four jobs}
}
$$

位於某種 GenAI 暴露範圍。

但其主要結論不是：

$$
\text{one in four jobs disappear}.
$$

而是多數職位更可能發生：

$$
\boxed{
\text{task transformation}
}
$$

而非完整替代。

因此：

$$
\boxed{
AIExposure
\neq
JobLossPrediction.
}
$$

這對政治分析很重要。

---

# 7. AI 與社會流動：梯子或門檻？

AI 可以降低：

$$
Cost(
Education,
Coding,
Translation,
Design,
LegalKnowledge,
Research
).
$$

因此：

$$
M\uparrow
$$

可能成立。

但 AI 也可能提高：

$$
ScaleAdvantage,
$$

$$
CapitalLeverage,
$$

$$
DataAdvantage,
$$

$$
ComputeAdvantage.
$$

因此：

$$
M\downarrow
$$

也可能成立。

---

# 8. 流動性取決於「誰先取得 AI 槓桿」

令：

$$
\lambda_i^{AI}
$$

表示行動者 $i$ 可取得的 AI 有效槓桿。

若：

$$
\lambda_{low}^{AI}
\uparrow
$$

快於：

$$
\lambda_{high}^{AI},
$$

則：

$$
MobilityGap\downarrow.
$$

若反之：

$$
\lambda_{high}^{AI}
\uparrow\uparrow,
$$

則：

$$
MobilityGap\uparrow.
$$

因此：

$$
\boxed{
AI democratization of capability
}
$$

與：

$$
\boxed{
AI concentration of leverage
}
$$

是兩條不同路徑。

---

# 9. AI 治理：公共服務改善是真實可能

OECD 2025《Governing with Artificial Intelligence》指出，政府使用 AI 可：

- 自動化公共服務；
- 個人化服務；
- 支援決策；
- 偵測詐欺；
- 增強公務員工作與學習。

因此：

$$
A_G\uparrow
\Rightarrow
ServiceCapacity\uparrow
$$

具有實際工程基礎。

---

# 10. 但公共服務效率不等於公共正當性

OECD 同時指出：

- 偏誤資料可能造成有害決策；
- 缺乏透明度會削弱問責；
- 過度依賴可能放大錯誤；
- 數位落差可能擴大；
- 信任可能因此下降。

因此：

$$
\boxed{
AdministrativeEfficiency
\neq
ProceduralLegitimacy.
}
$$

---

# 11. 2026 OECD 信任調查的雙向訊號

OECD 2026 公共機構信任調查顯示，超過四成受訪者相信政府使用 AI 可能帶來：

- 個人化服務；
- 降低成本。

但對：

- 公平；
- 隱私；
- 透明；
- 人類監督；

的信心較低。

這個結果正好支持：

$$
\boxed{
\Delta ServiceTrust
}
$$

與：

$$
\boxed{
\Delta RightsTrust
}
$$

可以方向不同。

---

# 12. 控制能力本身也不是單一負向變量

令：

$$
A_C
$$

表示 AI 強化的監測、審查、異常偵測與風險控制能力。

在公共安全情境：

$$
A_C\uparrow
$$

可能：

$$
CrimeDetection\uparrow,
$$

$$
FraudDetection\uparrow,
$$

$$
EmergencyResponse\uparrow.
$$

因此不能定義：

$$
A_C
=
\text{evil}.
$$

---

# 13. 但高控制能力會降低精準干預成本

若 AI 可以：

- 追蹤行為；
- 大規模比對；
- 預測異常；
- 分類風險；
- 自動審查；
- 生成宣傳與反敘事；
- 持續識別特定網路；

則：

$$
\boxed{
Cost_{\mathrm{targeted\ intervention}}
\downarrow.
}
$$

這使政治控制從粗放式：

$$
\text{mass coercion}
$$

轉向：

$$
\boxed{
\text{selective materialization of coercive attention}.
}
$$

---

# 14. 數位壓迫的外部證據

Freedom House 2025《Freedom on the Net》指出，威權政府持續使用數位技術加深：

- 監控；
- 審查；
- 資訊操弄；

並警告主權 AI 發展在缺乏權利保障的環境中可能提高此類能力。

本文採用此材料作為：

$$
\boxed{
A_C
\rightarrow
RepressiveCapacity
}
$$

存在現實路徑的證據，而不是證明所有 AI 或所有國家必然走向此結果。

---

# 15. 民主制度也不能假設自身免疫

高監測能力在民主國家同樣可能被：

- 國安；
- 邊境；
- 移民；
- 反恐；
- 刑事執法；

採用。

因此：

$$
\boxed{
Democracy
\not\Rightarrow
A_C=0.
}
$$

真正差異應研究：

$$
\boxed{
Oversight
+
Necessity
+
Proportionality
+
Appeal
+
JudicialReview.
}
$$

---

# 16. 所以制度差異不是「有沒有監控」

更準確的比較是：

$$
\boxed{
\text{Who authorizes it?}
}
$$

$$
\boxed{
\text{Who can inspect it?}
}
$$

$$
\boxed{
\text{Who can refuse it?}
}
$$

$$
\boxed{
\text{Who can appeal it?}
}
$$

$$
\boxed{
\text{Can the system be stopped?}
}
$$

這將直接接 Paper 04。

---

# 17. AI 與資訊品質：更多資訊不必等於更真

AI 可以：

$$
SearchCost\downarrow,
$$

$$
TranslationCost\downarrow,
$$

$$
VerificationCost\downarrow.
$$

但也可以：

$$
SyntheticContent\uparrow,
$$

$$
PersuasionScale\uparrow,
$$

$$
InformationFlood\uparrow.
$$

因此：

$$
\boxed{
InformationVolume\uparrow
\not\Rightarrow
Q\uparrow.
}
$$

---

# 18. AI 可以同時提高審查與反審查能力

政府可使用 AI：

$$
ContentDetection\uparrow.
$$

公民、媒體與研究者也可使用 AI：

$$
FactCheck\uparrow,
$$

$$
ArchiveSearch\uparrow,
$$

$$
CrossLanguageAccess\uparrow.
$$

因此資訊權力取決於：

$$
\boxed{
\Delta C_{\mathrm{state}}^{info}
-
\Delta C_{\mathrm{citizen}}^{info}.
}
$$

---

# 19. AI 與制度校正：最容易被忽略的一條

AI 不只可以執行政策。

它也可以：

- 找反例；
- 做 regression test；
- 比較版本；
- 偵測政策異常；
- 找出矛盾；
- 重播歷史決策；
- 模擬替代方案；
- 提醒低信心狀態。

因此：

$$
A_R\uparrow
$$

可能：

$$
R\uparrow.
$$

---

# 20. 但 AI 也可以讓錯誤制度變得更有效率

若制度目標函數本身有問題：

$$
Objective=Bad,
$$

而 AI 只提高：

$$
OptimizationQuality,
$$

則：

$$
\boxed{
BetterOptimization
\rightarrow
BetterExecutionOfBadObjective.
}
$$

所以：

$$
\boxed{
CorrectionCapacity
\neq
OptimizationCapacity.
}
$$

---

# 21. Revision AI 與 Optimization AI 必須分型

本文區分：

$$
\boxed{
A_O^{opt}
=
\text{ability to optimize given objectives}
}
$$

與：

$$
\boxed{
A_R^{rev}
=
\text{ability to reopen objectives, assumptions and rules}.
}
$$

如果只有前者：

$$
A_O^{opt}\uparrow,
$$

可能造成：

$$
InstitutionalLockIn\uparrow.
$$

---

# 22. AI 與合法性的第一階與第二階作用

第一階：

$$
AI
\rightarrow
ServiceQuality
\rightarrow
L\uparrow.
$$

第二階：

$$
AI
\rightarrow
OpaqueDecision
\rightarrow
AppealDifficulty
\rightarrow
L\downarrow.
$$

所以總效應：

$$
\boxed{
\Delta L
=
\Delta L^{(1)}
+
\Delta L^{(2)}
+
\Delta L^{(3)}
+\cdots
}
$$

不能只測第一階。

---

# 23. 短期穩定與長期可逆性可以分岔

AI 可能讓：

$$
C_S\uparrow,
$$

$$
CrisisResponse\uparrow,
$$

$$
Stability_{short}\uparrow.
$$

但若同時：

$$
P\downarrow,
$$

$$
R\downarrow,
$$

則：

$$
\boxed{
ShortTermStability\uparrow
\land
LongTermReversibility\downarrow.
}
$$

兩者不矛盾。

---

# 24. 這就是「高績效低可逆」相位

定義：

$$
\boxed{
\mathcal P_{HPLR}
=
\{
W\uparrow,
C_S\uparrow,
Service\uparrow,
R\downarrow
\}.
}
$$

此狀態可能具有：

- 高生活滿意；
- 高服務效率；
- 高行政能力；
- 低政治替代；
- 高制度依賴。

它不能被簡化為「失敗制度」。

---

# 25. 反方向：低效率高可逆也可能存在

亦可能：

$$
\boxed{
\mathcal P_{LPHR}
=
\{
W\downarrow,
C_S\downarrow,
R\uparrow
\}.
}
$$

即制度很可爭議、可替換，但實際治理績效差。

因此：

$$
\boxed{
Democracy
\neq
automatic performance.
}
$$

---

# 26. 政治制度評價必須向量化

本文拒絕：

$$
Score\in[0,100]
$$

作為唯一比較。

至少需要：

$$
\boxed{
\mathbf V
=
(
W,
C_S,
C_C,
P,
R,
Q,
Security,
Distribution
).
}
$$

不同社會可對不同分量給不同權重。

---

# 27. AI 會改變這些權重本身

若 AI 讓公共服務極度便利：

$$
W\uparrow\uparrow,
$$

社會可能降低對某些制度摩擦的容忍。

反之，如果 AI 讓政治資訊與比較變得更容易：

$$
C_C\uparrow,
$$

人民也可能提高對：

$$
P
$$

與：

$$
R
$$

的要求。

所以：

$$
\boxed{
AI
\rightarrow
PreferenceTransformation
}
$$

也必須納入。

---

# 28. Mass Interaction 是特殊作用項

當：

$$
A_M\uparrow,
$$

普通人與 AI 的互動頻率大幅提高。

此時 AI 不只是政策工具，而是：

$$
\boxed{
\text{everyday institutional interface}.
}
$$

它開始作用於：

- 知識；
- 比較；
- 權利理解；
- 行動成本；
- 申訴；
- 期待；
- 新需求。

完整模型留待 Paper 05。

---

# 29. 第一階導數不夠：定義制度交互項

因為：

$$
J_{ij}
$$

受制度影響，本文進一步定義：

$$
\boxed{
K_{ijk}
=
\frac{
\partial^2 X_i
}{
\partial A_j
\partial I_k
}.
}
$$

 $K_{ijk}$ 表示制度條件 $I_k$ 如何改變 AI 能力 $A_j$ 對狀態 $X_i$ 的作用。

---

# 30. 例：隱私制度作為符號調節器

若：

$$
I_k
=
PrivacyGuardrails,
$$

則同樣：

$$
A_C\uparrow
$$

可能從：

$$
\text{mass surveillance}
$$

被限制成：

$$
\text{bounded risk detection}.
$$

因此：

$$
K_{privacy,A_C,R}
$$

具有實質政治意義。

---

# 31. 例：資料可攜與退出

若個體可以：

$$
ExportData=1,
$$

$$
SwitchProvider=1,
$$

則 AI 平台的依賴成本：

$$
LockIn
$$

下降。

所以：

$$
\boxed{
Interoperability
}
$$

本身就是政治經濟變量。

---

# 32. 所有權是 AI 政治效果的核心調節器

令：

$$
O_t
\in
\{
state,
private,
cooperative,
personal,
distributed
\}.
$$

同一模型能力：

$$
A
$$

在不同所有權下可能形成完全不同：

$$
\Delta X.
$$

因此：

$$
\boxed{
Capability
\neq
ControlRights.
}
$$

---

# 33. AI 的「私人善意—制度後果」再一次出現

企業可能真心希望：

$$
ProductQuality\uparrow.
$$

但其產品可能被：

$$
InstitutionalConversion
$$

接入更大的治理、監控或公共服務系統。

因此：

$$
\boxed{
GoodPrivateIntent
\not\Rightarrow
GoodSystemicOutcome.
}
$$

反方向也成立：

$$
\boxed{
PoliticalUse
\not\Rightarrow
OriginalDeveloperPoliticalIntent.
}
$$

---

# 34. 能力不對稱指數

本文定義暫定：

$$
\boxed{
\Lambda_{SC}
=
\frac{
\Delta C_S^{AI}
}{
\Delta C_C^{AI}
+\epsilon
}.
}
$$

其中 $\epsilon>0$ 防止分母為零。

若：

$$
\Lambda_{SC}\gg1,
$$

AI 主要增幅國家能力。

若：

$$
\Lambda_{SC}\ll1,
$$

公民能力增幅較大。

但這不是道德分數，只是結構測量。

---

# 35. 為什麼國家能力與公民能力都可能一起上升

一個成熟數位社會可能：

$$
C_S\uparrow
$$

同時：

$$
C_C\uparrow.
$$

例如：

- 行政更快；
- 政府資訊更透明；
- 公民查詢更方便；
- 司法檢索更容易；
- 申訴成本下降。

因此：

$$
\boxed{
state strengthening
\neq
citizen weakening.
}
$$

這也是避免簡化威權／民主論的重要原則。

---

# 36. 為什麼兩者也可能一起下降

若 AI 系統失敗造成：

- 大規模錯誤；
- 基礎設施中斷；
- 依賴鎖定；
- 模型污染；
- 網路攻擊；

則：

$$
C_S\downarrow
$$

且：

$$
C_C\downarrow.
$$

所以 AI 治理也新增共同脆弱性。

---

# 37. AI 治理單點失效

若：

$$
Remove(A^\star)
\Rightarrow
GovernanceCollapse,
$$

則：

$$
\boxed{
A^\star
=
\text{Institutional Intelligence SPOF}.
}
$$

即使 $A^\star$：

- 善良；
- 高效；
- 可靠；

這仍是架構風險。

---

# 38. 高能力不等於高覆蓋

沿用 SAS-08：

$$
\boxed{
ModelCapability
\neq
WorldCoverage.
}
$$

因此高能力 AI 對低覆蓋領域做不可逆決策，可能把：

$$
EpistemicError
$$

轉化為：

$$
InstitutionalHarm.
$$

---

# 39. 修訂比一次性正確更重要

因此成熟制度應追求：

$$
\boxed{
Observe
\rightarrow
Model
\rightarrow
Act
\rightarrow
Observe
\rightarrow
Revise.
}
$$

而不是：

$$
\text{one final model}.
$$

---

# 40. 四種制度—AI 耦合相位

本文暫提出：

## 40.1 Augmentative Phase

$$
W\uparrow,
C_S\uparrow,
C_C\uparrow,
R\approx stable.
$$

---

## 40.2 Asymmetric State Phase

$$
C_S\uparrow\uparrow,
C_C\uparrow\text{ or }\downarrow,
R\downarrow.
$$

---

## 40.3 Asymmetric Citizen Phase

$$
C_C\uparrow\uparrow,
C_S
\text{ adaptation lags}.
$$

可能形成制度改革壓力。

---

## 40.4 Coevolutionary Phase

$$
C_S\uparrow,
C_C\uparrow,
R\uparrow,
$$

且制度與 AI 持續互相修改。

這是最複雜的相位。

---

# 41. 威權制度的 AI 優勢不能只看控制

威權制度可能具有：

- 較強中央協調；
- 較快基礎設施整合；
- 較統一的資料接口；
- 較低跨機構否決成本。

這可能使：

$$
A_G,
A_C,
A_D
$$

更容易大規模整合。

但它也可能面臨：

$$
Q
$$

與：

$$
A_R
$$

的獨立校正不足問題。

---

# 42. 民主制度的 AI 優勢也不能只看自由

民主制度可能具有：

- 多中心審查；
- 媒體與公民社會；
- 司法救濟；
- 政黨競爭；
- 外部審計。

這可能提高：

$$
R
$$

與：

$$
P.
$$

但也可能增加：

$$
CoordinationCost,
$$

$$
DeploymentDelay,
$$

$$
RegulatoryFragmentation.
$$

所以：

$$
\boxed{
more contestability
\neq
lower cost in every domain.
}
$$

---

# 43. 比較政治真正要測的是 trade-off frontier

本文不主張某制度固定最優。

更合理是研究：

$$
\boxed{
\mathcal F^{political}
=
\{
W,
Security,
P,
R,
C_S,
C_C,
Q
\}.
}
$$

不同制度在此多維空間中形成不同 Pareto frontier。

AI 會移動：

$$
\mathcal F^{political}.
$$

---

# 44. AI 可以擴張 Pareto frontier，而不是只重新分配

若 AI 真正創造：

- 更多醫療能力；
- 更多教育能力；
- 更低行政成本；
- 更高能源效率；
- 更多知識；

則：

$$
\boxed{
\mathcal F_{t+1}
\supset
\mathcal F_t
}
$$

在某些功能域可能成立。

這意味政治不必永遠是零和。

---

# 45. 但 frontier expansion 不保證公平取得

即使：

$$
\mathcal F_{t+1}
\supset
\mathcal F_t,
$$

個體 $i$ 的可達集合：

$$
\mathcal F_{i,t}
$$

可能：

$$
\mathcal F_{i,t+1}
\not\supset
\mathcal F_{i,t}.
$$

所以：

$$
\boxed{
CivilizationalFeasibleSetExpansion
\neq
UniversalPersonalFeasibleSetExpansion.
}
$$

---

# 46. AI 政治效果的時間尺度

短期：

$$
\tau_s.
$$

中期：

$$
\tau_m.
$$

長期：

$$
\tau_l.
$$

同一效果可能：

$$
J_{ij}(\tau_s)>0
$$

但：

$$
J_{ij}(\tau_l)<0.
$$

例如高監控可能短期提高安全，長期降低信任與校正。

---

# 47. AI 政治非單調命題

因此可能：

$$
\boxed{
\frac{
\partial X_i
}{
\partial A_j
}
}
$$

在不同 AI 強度區間換號。

低強度：

$$
A_j<a,
$$

提高效益。

高強度：

$$
A_j>b,
$$

出現依賴、集中或反效果。

這形成：

$$
\boxed{
\text{non-monotonic AI politics}.
}
$$

---

# 48. 可檢驗預測

## 48.1 預測一：公共部門 AI 效率提升不會自動等比例提高信任

若：

$$
ServiceSpeed\uparrow
$$

但：

$$
Transparency\downarrow,
$$

信任可停滯或下降。

---

## 48.2 預測二：高 AI 暴露產業的就業效果將高度依賴任務重組而非職業名稱

因此：

$$
OccupationExposure
$$

不能直接預測：

$$
JobLoss.
$$

---

## 48.3 預測三：相同監控 AI 在不同程序制度下具有不同權利效果

控制技術能力相近時：

$$
Appeal,
Oversight,
PurposeLimitation
$$

應能顯著解釋傷害差異。

---

## 48.4 預測四：AI 增幅越集中，國家／公民能力比值越容易偏移

$$
OwnershipConcentration\uparrow
\Rightarrow
Variance(\Lambda_{SC})\uparrow.
$$

---

## 48.5 預測五：有 revision channel 的 AI 治理比純 optimization AI 更能維持長期信任

$$
A_R^{rev}>0
$$

應與：

$$
Recovery,
AppealSuccess,
Rollback
$$

正相關。

---

## 48.6 預測六：大規模人機互動會改變政治需求分布

$$
A_M\uparrow
\Rightarrow
P(Q_{t+1})
\text{ changes}.
$$

此命題留待 Paper 05 深化。

---

# 49. 反證條件

本文的「符號不固定」不能變成不可證偽的萬用說法。

若跨制度、跨所有權、跨時間尺度的大量研究持續顯示：

$$
\operatorname{sign}(J_{ij})
$$

對某些關係高度穩定，

則應承認：

$$
\boxed{
\text{stable directional regularity exists}.
}
$$

本文只是拒絕在證據不足前把它先驗化。

---

# 50. 與 IQRC-01 的關係

Paper 01 提出：

$$
X_{t+1}
=
F(
X_t,
I_t,
\mathcal A_t,
E_t
).
$$

本文把：

$$
\mathcal A_t
$$

對：

$$
X_t
$$

的作用拆成：

$$
\boxed{
J_t.
}
$$

因此 Paper 03 是 Paper 01 的局部微分展開。

---

# 51. 與 IQRC-02 的關係

Paper 02 發現中國不能簡化成：

$$
AI
\rightarrow
Control\uparrow
$$

或：

$$
AI
\rightarrow
Growth\uparrow.
$$

本文將這個案例一般化為：

$$
\boxed{
\operatorname{sign}
\left(
\frac{
\partial X_i
}{
\partial A_j
}
\right)
\text{ is context-dependent}.
}
$$

---

# 52. 與 Paper 04 的接口

Paper 04：

**《制度塑造智能：民主、威權與類全域 AI 的不同可行域》**

將進一步研究：

$$
\boxed{
K_{ijk}
=
\frac{
\partial^2 X_i
}{
\partial A_j
\partial I_k
}
}
$$

也就是制度如何改變 AI 的政治作用。

---

# 53. 核心命題

## 命題一：政治 AI 條件符號命題

$$
\boxed{
\operatorname{sign}
(
J_{ij}
)
\text{ is not generally institution-invariant}.
}
$$

---

## 命題二：國家—公民能力分岔命題

$$
\boxed{
\Delta C_S
\neq
\Delta C_C
}
$$

可以在同一 AI 進步下成立。

---

## 命題三：治理效率—正當性分離命題

$$
\boxed{
AdministrativeEfficiency
\neq
Legitimacy.
}
$$

---

## 命題四：控制雙重用途命題

$$
\boxed{
RiskControlCapacity
}
$$

既可降低犯罪、詐欺與災害風險，也可降低政治監控與選擇性干預成本。

---

## 命題五：Optimization–Revision 分離命題

$$
\boxed{
OptimizationCapacity
\neq
CorrectionCapacity.
}
$$

---

## 命題六：文明可行域—個人可行域分離命題

$$
\boxed{
\mathcal F_{\mathrm{civ}}\uparrow
\not\Rightarrow
\mathcal F_i\uparrow
\quad
\forall i.
}
$$

---

# 54. 結論

AI 的政治效果不應再被問成：

> 它會讓民主更強，還是讓威權更強？

這個問題把：

- 生產；
- 福利；
- 控制；
- 流動；
- 資訊；
- 修訂；
- 國家能力；
- 公民能力；

錯誤壓成一條軸。

本文提出：

$$
\boxed{
J_t
=
\left[
\frac{
\partial X_i
}{
\partial A_j
}
\right]_t
}
$$

作為更一般的研究單位。

AI 可以同時：

$$
W\uparrow,
$$

$$
C_S\uparrow,
$$

$$
C_C\uparrow,
$$

而：

$$
R\downarrow.
$$

也可以：

$$
W\uparrow,
$$

$$
R\uparrow,
$$

但：

$$
CoordinationCost\uparrow.
$$

甚至同一個 AI 作用在短期與長期可以換號。

因此真正的政治分水嶺，不是：

$$
\boxed{
AI
}
$$

本身。

而是：

$$
\boxed{
\text{institutional conversion topology}.
}
$$

也就是：

> 哪些 AI 能力被誰控制？

> 由誰接取？

> 以什麼資料訓練與運行？

> 誰能監督？

> 誰能拒絕？

> 誰能申訴？

> 錯誤能不能回退？

> 新證據能不能重新打開既有結論？

Paper 03 因此把「AI 強化威權」從一個可能成立的局部命題，重新放回更大的多向系統：

$$
\boxed{
AI
\times
Institution
\times
Ownership
\times
Rights
\times
Time
\rightarrow
PoliticalDynamics.
}
$$

下一篇將正式進入這個乘積中的第二項：

$$
\boxed{
Institution.
}
$$

也就是：

> **同樣能力的 AI，進入民主、威權、多中心、企業或跨國制度後，究竟會被塑造成什麼不同的 operational intelligence？**

---

# 參考文獻與外部證據

1. International Labour Organization. *Generative AI and Jobs: A 2025 Update*. 2025-05-20.
2. Gmyrek, P. et al. *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*. ILO Working Paper 140, 2025.
3. International Labour Organization & World Bank. *Disruption without dividend? How the digital divide and task differences split GenAI’s global impact*. ILO Working Paper 166, 2026-03-17.
4. International Labour Organization. *Workers’ Exposure to AI: What Indicators Tell Us – and What They Don’t*. 2026-04-17.
5. OECD. *Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions*. OECD Publishing, 2025-09-18. DOI: 10.1787/795de142-en.
6. OECD. *OECD Survey on Drivers of Trust in Public Institutions 2026 Results*. 2026.
7. Stanford Institute for Human-Centered Artificial Intelligence. *The 2026 AI Index Report — Policy and Governance*. 2026.
8. Freedom House. *Freedom on the Net 2025: An Uncertain Future for the Global Internet*. 2025.
9. Freedom House. *The Repressive Power of Artificial Intelligence*. Freedom on the Net 2023.
10. Neo.K，〈IQRC-01｜AI 介入後的政治系統動力學：從固定智能假設到制度—智能共演化〉，EveMissLab，2026。
11. Neo.K，〈IQRC-02｜從發展合法性到努力—回報斷裂：新中國的流動性、相對剝奪與 AI 變數〉，EveMissLab，2026。
12. Neo.K，〈SAS-08｜現實沒有最終模型：覆蓋率、利維坦與可重審的後工具文明〉，EveMissLab，2026。
13. Neo.K，〈不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理〉，EveMissLab，2026。
14. Neo.K，〈PGMV-15｜後生成文明：從無限候選宇宙到共同世界選擇〉，EveMissLab，2026。

---

## 外部來源定位

- ILO 2025 GenAI jobs update: `ilo.org/publications/generative-ai-and-jobs-2025-update`
- ILO Working Paper 140: `ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure`
- ILO–World Bank 2026: `ilo.org/publications/disruption-without-dividend-how-digital-divide-and-task-differences-split`
- ILO AI exposure indicators 2026: `ilo.org/publications/workers-exposure-ai-what-indicators-tell-us-and-what-they-dont`
- OECD Governing with AI: DOI `10.1787/795de142-en`
- OECD Trust Survey 2026: `oecd.org/en/publications/oecd-survey-on-drivers-of-trust-in-public-institutions-2026-results_9eb63fec-en.html`
- Stanford AI Index 2026: `hai.stanford.edu/ai-index/2026-ai-index-report/policy-and-governance`
- Freedom on the Net 2025: `freedomhouse.org/report/freedom-net/2025/uncertain-future-global-internet`

---

## 版本註記

**v0.1 / 2026-08-28**

- 建立 AI 政治耦合矩陣 $J_t$ ；
- 提出條件符號函數 $\sigma_{ij}$ ；
- 建立制度交互張量 $K_{ijk}$ ；
- 區分生產率紅利與家庭福利；
- 區分 AI exposure、job transformation 與 job loss；
- 建立治理效率—程序正當性分離；
- 建立 Risk Control 與 Political Control 的雙重用途模型；
- 正式區分 Optimization AI 與 Revision AI；
- 建立國家—公民能力不對稱指數 $\Lambda_{SC}$ ；
- 建立高績效低可逆與低績效高可逆相位；
- 建立文明可行域與個人可行域分離命題；
- 為 Paper 04 的制度塑形模型建立二階導數接口。
