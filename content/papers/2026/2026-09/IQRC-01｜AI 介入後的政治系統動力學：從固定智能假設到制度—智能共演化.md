# IQRC-01｜AI 介入後的政治系統動力學：從固定智能假設到制度—智能共演化

**English Title:** *Political System Dynamics After AI Intervention: From the Fixed-Intelligence Assumption to Institutional–Intelligence Coevolution*  
**系列：**《制度智能、類全域 AI 與可重開文明系列》  
**Series:** *Institutional Intelligence, Quasi-Global AI, and Reopenable Civilization Series*  
**篇次：** Paper 01 / 08  
**文件編號：** EML-IQRC-01-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 政治系統動力學／AI 政治經濟學／制度智能／Agentic AI／理論建模  
**狀態：** Canonical Draft / Series Foundation  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

近代政治學、政治經濟學、發展理論與威權韌性研究，通常將國家能力、官僚組織、資訊處理、政策反饋、社會動員、制度校正與政治合法性視為可變量，但其底層仍常隱含一個未被明說的前提：**社會的有效智能密度、組織推理頻寬與跨領域協調能力，在分析時間尺度內大致由人類組織與既有資訊系統所決定。**在此條件下，經濟增長、社會流動、相對剝奪、制度正當性、國家暴力、資訊控制、官僚效率與政治參與可以被放入相對穩定的動態模型。

Agentic AI、長程記憶、工具調用、跨資料源檢索、自主規劃、程式執行、持續驗證、具身系統、區域調度與未來可能的類全域 AI，正在破壞上述前提。AI 不再只是「技術進步」或「生產率」中的一個普通外生變量，而逐漸成為會同時改變其他變量之轉換效率、觀測能力、作用速度、關係拓撲與可行域的高階算子。

本文提出「制度—智能共演化」框架。令政治—社會狀態為 $X_t$，制度結構為 $I_t$，AI／Agent 智能作用結構為 $\mathcal A_t$，外部環境為 $E_t$，則政治系統不再只表示為傳統狀態轉移：

$$
X_{t+1}=F_0(X_t,I_t,E_t),
$$

而應一般化為：

$$
\boxed{
X_{t+1}
=
F(
X_t,
I_t,
\mathcal A_t,
E_t
).
}
$$

其中 $\mathcal A_t$ 不是單一能力分數，而是一組作用於資訊、組織、生產、治理、控制、創新、分配、參與與制度修訂的動態算子族。制度同樣會塑造 AI 能看到什麼、能拒絕什麼、能保留什麼、能對誰負責、能否提出反例、能否接受外部審計，以及其輸出是否被轉化為實際權力。因此：

$$
\boxed{
\mathcal A_{t+1}
=
G(
\mathcal A_t,
I_t,
X_t,
D_t,
R_t
),
}
$$

形成真正的制度—智能雙向共演化，而不是「政治系統受到 AI 衝擊」的單向模型。

本文特別主張，舊政治模型不必被廢棄。若 AI 介入足夠弱，則新版理論應退化回原模型：

$$
\boxed{
\lim_{\mathcal A\to0}
F(
X,
I,
\mathcal A,
E
)
=
F_0(
X,
I,
E
).
}
$$

因此，前 AI 政治理論可被重新理解為低智能外部化、低自主代理、低機器治理密度參數區間下的特殊情形。本文最後提出可檢驗預測、制度型別差異、AI 作用符號不確定性、路徑依賴、政策可逆性與後續七篇接口，作為整個《制度智能、類全域 AI 與可重開文明系列》的理論地基。

---

## 關鍵詞

制度智能；政治系統動力學；Agentic AI；類全域 AI；制度—智能共演化；國家能力；政治合法性；AI 治理；威權韌性；民主可逆性；Pervasive Intelligence；可行域；AI 政治經濟學；多主體治理；可重開文明

---

# 0. 研究定位：不是「AI 會不會改變政治」，而是政治理論的隱含型別正在失效

AI 與政治的常見討論通常採用下列形式：

$$
\text{AI}
\rightarrow
\text{employment},
$$

$$
\text{AI}
\rightarrow
\text{misinformation},
$$

$$
\text{AI}
\rightarrow
\text{surveillance},
$$

$$
\text{AI}
\rightarrow
\text{productivity}.
$$

這些命題本身並沒有錯，但仍然把 AI 當成傳統政治模型中的一個新自變量。

本文提出更強的問題：

> 如果 AI 開始改變「國家如何感知、組織如何推理、政策如何生成、人民如何取得知識、個體如何形成需求、制度如何修正、社會如何協調」本身，那麼 AI 還能否被當成一般自變量？

本文答案是否定的。

在 Agentic AI 與高密度 AI 中介條件下，AI 更接近：

$$
\boxed{
\text{a transformation layer over the political state space}.
}
$$

因此政治模型必須從：

$$
\text{Variables}
\rightarrow
\text{Outcome}
$$

提升為：

$$
\boxed{
\text{Variables}
+
\text{Operators}
+
\text{Institutional Constraints}
+
\text{Feedback Topology}
\rightarrow
\text{Outcome}.
}
$$

---

# 1. 傳統政治模型中的固定智能假設

## 1.1 隱含假設

大量政治與經濟模型雖然討論資訊、組織與能力，但仍常隱含：

$$
\boxed{
B_{\mathrm{cog}}
\approx
\text{bounded by human organizational bandwidth}.
}
$$

其中 $B_{\mathrm{cog}}$ 表示一個政治共同體在特定時間尺度內可動員的有效認知、分析、協調與決策頻寬。

在傳統國家中，即使存在：

- 統計局；
- 情報機關；
- 官僚體系；
- 大學；
- 研究機構；
- 顧問系統；
- 軍事指揮鏈；
- 大型企業；

其核心分析、目標設定、異常判斷、政策取捨與責任承擔仍主要依賴人類。

因此國家能力可被粗略限制為：

$$
\boxed{
C_{\mathrm{state}}
\leq
C_{\mathrm{human}}
+
C_{\mathrm{institution}}
+
C_{\mathrm{information\ system}}.
}
$$

這個假設在二十世紀大部分政治史中具有相當合理性。

---

## 1.2 為什麼這個假設現在開始失效

當 AI 具有：

- 持續檢索；
- 長程記憶；
- 多資料源整合；
- 自主規劃；
- 工具調用；
- 程式執行；
- 大規模模擬；
- 多 Agent 協調；
- 即時異常偵測；
- 政策候選生成；
- 持續驗證；
- 人機雙向互動；

則：

$$
C_{\mathrm{state}}
$$

開始可能包含一個新項：

$$
C_{\mathrm{machine\ agency}}.
$$

因此：

$$
\boxed{
C_{\mathrm{state}}
\leq
C_{\mathrm{human}}
+
C_{\mathrm{institution}}
+
C_{\mathrm{machine\ agency}}
+
C_{\mathrm{hybrid\ coordination}}.
}
$$

這不是宣稱 AI 已經接管國家，而是指出政治能力的上界結構已經改變。

---

# 2. 舊模型不是錯，而是低 AI 介入區間

## 2.1 AI-neutral canonical core

本文保留一個 AI-neutral 政治核心：

$$
X_t
=
(
W_t,
M_t,
D_t,
L_t,
S_t,
C_t,
P_t,
R_t,
Q_t
),
$$

其中：

- $W_t$：生活福利與實質資源；
- $M_t$：社會流動與可達機會；
- $D_t$：相對剝奪與位置落差；
- $L_t$：制度合法性；
- $S_t$：結構壓力；
- $C_t$：國家與組織能力；
- $P_t$：政治參與與可爭議性；
- $R_t$：制度可逆性與修訂能力；
- $Q_t$：資訊品質與認識環境。

在沒有強 AI 介入時：

$$
X_{t+1}
=
F_0(
X_t,
I_t,
E_t
).
$$

這仍然可以描述大量歷史案例。

---

## 2.2 AI extension layer

引入 AI 後：

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

若：

$$
\mathcal A_t
\rightarrow0,
$$

則要求：

$$
\boxed{
F(
X_t,
I_t,
0,
E_t
)
=
F_0(
X_t,
I_t,
E_t
).
}
$$

這使舊模型成為新版的特殊情形，而不是被否定。

---

# 3. AI 不是 scalar：定義智能作用向量

## 3.1 單一 AI 指數會造成型別錯誤

若只寫：

$$
AI_t\in[0,1],
$$

會把完全不同的能力混在一起。

一個模型可能：

- 生產力很強；
- 治理能力很弱；
- 控制能力很高；
- 公民服務能力很高；
- 制度校正能力很低。

因此本文定義：

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

- $A_P$：Productivity augmentation；
- $A_O$：Organizational augmentation；
- $A_G$：Governance augmentation；
- $A_C$：Control / surveillance augmentation；
- $A_I$：Innovation augmentation；
- $A_D$：Distribution / allocation augmentation；
- $A_R$：Revision / correction augmentation；
- $A_M$：Mass-interaction augmentation。

---

## 3.2 符號不固定

本文拒絕：

$$
AI\uparrow
\Rightarrow
Freedom\downarrow
$$

或：

$$
AI\uparrow
\Rightarrow
Welfare\uparrow
$$

這類單向普遍命題。

因為：

$$
\frac{\partial W}{\partial A_P}
$$

可能為正，

而：

$$
\frac{\partial M}{\partial A_P}
$$

可能依產業、資本結構與勞動市場而正負不定。

同樣：

$$
\frac{\partial C_{\mathrm{state}}}{\partial A_G}>0
$$

不表示：

$$
\frac{\partial P_{\mathrm{contestability}}}{\partial A_G}>0.
$$

AI 的政治效果是條件性的。

---

# 4. 從向量到算子：AI 會改變其他變量的轉換規則

## 4.1 一般形式

令：

$$
\mathcal A_t
$$

為智能作用算子，則：

$$
\boxed{
X_{t+1}
=
\mathcal T_{I_t,E_t,\mathcal A_t}
(
X_t
).
}
$$

也就是 AI 不只是「增加某個數值」，而是修改狀態轉移函數本身。

---

## 4.2 例：努力—回報彈性

傳統模型可寫：

$$
Y_i
=
f(
e_i,
w_i,
k_i
),
$$

其中 $e_i$ 為努力、 $w_i$ 為制度位置、 $k_i$ 為能力。

AI 介入後：

$$
Y_i
=
f(
e_i,
w_i,
k_i;
\mathcal A_i
).
$$

更重要的是：

$$
\boxed{
\frac{\partial Y_i}{\partial e_i}
}
$$

本身也可能被 AI 改變。

因此 AI 會作用於「努力是否值得」這個導數，而不只是收入水準。

---

# 5. Agentic AI：從工具增益到組織代理

## 5.1 工具式 AI

典型工具式 AI：

$$
H
\rightarrow
AI
\rightarrow
Output.
$$

人類仍然負責：

- 決定目標；
- 拆解任務；
- 選擇工具；
- 判斷結果；
- 發起下一步。

---

## 5.2 Agentic AI

Agentic AI 更接近：

$$
\boxed{
Goal
\rightarrow
Plan
\rightarrow
ToolUse
\rightarrow
Execution
\rightarrow
Verification
\rightarrow
NextAction.
}
$$

因此 AI 開始進入：

$$
\boxed{
\text{organizational agency}.
}
$$

這對政治學的重要性在於：過去很多「國家能力」問題其實是「人類官僚組織能力」問題。

Agentic AI 會把兩者部分解耦。

---

# 6. 制度會反過來塑造 AI

## 6.1 AI 不是制度外生物

同一基礎模型進入不同制度，其 operational form 不必相同。

定義：

$$
\boxed{
\mathcal A_{t+1}
=
G(
\mathcal A_t,
I_t,
D_t,
R_t,
U_t
),
}
$$

其中：

- $I_t$：制度結構；
- $D_t$：資料與資訊環境；
- $R_t$：權利與限制；
- $U_t$：授權與實際使用方式。

---

## 6.2 制度塑形維度

制度會影響 AI：

- 可以取得哪些資料；
- 可以詢問哪些來源；
- 能否保留矛盾；
- 能否顯示不確定性；
- 能否拒絕命令；
- 能否提供申訴；
- 能否接受外部審計；
- 能否對政治權威提出反例；
- 是否允許使用者比較替代制度；
- 是否可跨組織互操作。

因此：

$$
\boxed{
\mathcal F_{\mathrm{AI}}
=
\mathcal F(
Capability,
Institution,
Authority,
Data,
Rights,
Interfaces
).
}
$$

---

# 7. 制度智能可行域

## 7.1 定義

令：

$$
\mathcal F_I
$$

表示制度 $I$ 下，一個高能力 AI 實際可被允許形成的能力—權限—互動可行域。

則：

$$
\boxed{
\mathcal F_{I_1}
\neq
\mathcal F_{I_2}
}
$$

可能成立，即使：

$$
Capability(A_1)
=
Capability(A_2).
$$

---

## 7.2 民主與威權不應被簡化成高低排序

本文不預設：

$$
\mathcal F_{\mathrm{DEM}}
>
\mathcal F_{\mathrm{AUTH}}.
$$

更合理的是：

$$
\boxed{
\mathcal F_{\mathrm{DEM}}
\neq
\mathcal F_{\mathrm{AUTH}}.
}
$$

威權制度可能更容易形成：

$$
\text{central coordination},
$$

$$
\text{rapid state integration},
$$

$$
\text{uniform deployment}.
$$

民主制度則可能更容易形成：

$$
\text{contestability},
$$

$$
\text{independent audit},
$$

$$
\text{plural access},
$$

$$
\text{rights-preserving refusal}.
$$

這些差異必須實證測量，而非先驗宣告優劣。

---

# 8. 制度轉換係數：私人能力如何成為公共權力

## 8.1 Private Capability 不等於 State Capability

私人企業創造：

$$
C_{\mathrm{private}}
$$

不表示政府直接擁有：

$$
C_{\mathrm{state}}.
$$

但制度可以存在某種轉換：

$$
\boxed{
C_{\mathrm{state}}
=
\Gamma_I
(
C_{\mathrm{private}},
D,
Authority,
Infrastructure
).
}
$$

其中 $\Gamma_I$ 為 Institutional Conversion Operator。

---

## 8.2 意圖與結果必須分離

令私人行動者意圖：

$$
Intent_i
$$

與制度後果：

$$
Outcome_I
$$

則：

$$
\boxed{
Intent_i
\neq
SystemicConsequence_i.
}
$$

一個工程師可以只想：

- 做好產品；
- 賺錢；
- 照顧家人；
- 推進科技；

其能力仍可能經由制度網路被轉化為：

$$
\Delta C_{\mathrm{state}}>0.
$$

這不是道德定罪，而是結構分析。

---

# 9. AI 會同時改變治理與反治理能力

## 9.1 國家側

AI 可以增加：

$$
C_{\mathrm{admin}},
$$

$$
C_{\mathrm{prediction}},
$$

$$
C_{\mathrm{coordination}},
$$

$$
C_{\mathrm{monitoring}}.
$$

---

## 9.2 公民側

AI 同時也可能增加：

$$
C_{\mathrm{knowledge}},
$$

$$
C_{\mathrm{legal}},
$$

$$
C_{\mathrm{organization}},
$$

$$
C_{\mathrm{comparison}},
$$

$$
C_{\mathrm{counterargument}}.
$$

因此真正應研究的是：

$$
\boxed{
\Delta B_t
=
\Delta C_{\mathrm{state}}
-
\Delta C_{\mathrm{citizen}},
}
$$

而不是只看 AI 是否變強。

---

# 10. AI 對政治壓力的雙向回饋

傳統簡化：

$$
Pressure\uparrow
\Rightarrow
RegimeRisk\uparrow.
$$

AI 介入後：

$$
Pressure\uparrow
\rightarrow
AI\text{-assisted sensing}
\rightarrow
AdaptiveResponse\uparrow.
$$

因此：

$$
\boxed{
Pressure\uparrow
\not\Rightarrow
RegimeFailure\uparrow
}
$$

必然成立。

但反方向亦不成立：

$$
AI\text{-assisted adaptation}
\uparrow
\not\Rightarrow
LongTermLegitimacy\uparrow.
$$

因為短期穩定可能以長期僵化為代價。

---

# 11. 可逆性必須成為獨立狀態變量

既有政治模型常把「穩定」當作正面結果。

本文要求區分：

$$
Stability
$$

與：

$$
Reversibility.
$$

一個系統可以：

$$
Stability\uparrow,
$$

同時：

$$
Reversibility\downarrow.
$$

因此定義：

$$
\boxed{
R_t
=
f(
Challenge,
Appeal,
Replacement,
Rollback,
Succession,
Reopening
).
}
$$

高 AI 治理能力若沒有相應的：

- challenge；
- review；
- appeal；
- rollback；
- handoff；

可能形成高穩定低可逆結構。

---

# 12. AI 世界模型具有反身性

若 AI 對世界作出預測：

$$
\hat W_t,
$$

並向政策制定者、企業或公民輸出，則：

$$
\hat W_t
\rightarrow
Action_t
\rightarrow
W_{t+1}.
$$

因此：

$$
\boxed{
Prediction
\neq
Passive Observation.
}
$$

在類全域 AI 環境中，模型輸出本身可能持續改變被模型化的世界。

這使政治系統成為更強的 reflexive system。

---

# 13. 高密度人機互動：政治狀態空間會被問答修改

如果 AI 每天只服務少量專家，其政治效果有限。

當：

$$
N_{\mathrm{interaction}}
\rightarrow
\text{very large},
$$

且普通人的法律、工作、教育、行政、政治、社會問題大量經 AI 中介後，AI 回答會修改：

$$
Awareness,
$$

$$
Expectation,
$$

$$
Demand,
$$

$$
Actionability.
$$

因此：

$$
\boxed{
Q_t
+
A_t
\rightarrow
\mathcal F_{t+1}^{H\leftrightarrow AI}.
}
$$

完整理論留待 Paper 05。

---

# 14. 類全域 AI 不是「超級中央模型」

本文沿用既有 Pervasive / Regional / Global AI 分型。

類全域 AI 可以是：

$$
\boxed{
\text{distributed supervisory intelligence}
}
$$

而不是：

$$
\text{one universal synchronous controller}.
$$

其全域性主要表現在：

$$
Scope,
$$

$$
Coordination,
$$

$$
Interoperability,
$$

$$
CausalReach,
$$

而非單一模型是否「最大」。

---

# 15. 國家能力上升不等於人民能力上升

這是 AI 政治經濟學的重要斷裂。

可能出現：

$$
C_{\mathrm{state}}\uparrow,
$$

$$
C_{\mathrm{industrial}}\uparrow,
$$

但：

$$
C_{\mathrm{household}}\not\uparrow.
$$

甚至：

$$
M_{\mathrm{mobility}}\downarrow.
$$

因此：

$$
\boxed{
\text{National Capability Growth}
\neq
\text{Distributed Capability Growth}.
}
$$

這一命題將在中國案例篇進一步展開。

---

# 16. AI-neutral 政治理論的重建方式

本文建議未來舊理論採三層重建。

## 16.1 Layer 0：Canonical Core

保留：

$$
F_0(X,I,E).
$$

不依賴 AI。

---

## 16.2 Layer 1：AI Augmentation

加入：

$$
\mathbf A_t.
$$

測量不同能力增益。

---

## 16.3 Layer 2：Operator Transformation

進一步允許：

$$
\mathcal A_t
$$

修改狀態轉移：

$$
F_0
\rightarrow
F_{\mathcal A}.
$$

這是最重要的一步。

---

# 17. 制度—智能共演化母式

本文提出母式：

$$
\boxed{
\begin{aligned}
X_{t+1}
&=
F(
X_t,
I_t,
\mathcal A_t,
E_t
),\\
I_{t+1}
&=
H(
I_t,
X_t,
\mathcal A_t,
P_t
),\\
\mathcal A_{t+1}
&=
G(
\mathcal A_t,
I_t,
X_t,
D_t,
R_t
).
\end{aligned}
}
$$

三者形成：

$$
\boxed{
X
\leftrightarrow
I
\leftrightarrow
\mathcal A.
}
$$

政治社會狀態塑造制度；

制度塑造 AI；

AI 又重新塑造政治社會狀態。

---

# 18. 路徑依賴與鎖定

若：

$$
\mathcal A_t
$$

被深度嵌入：

- 行政；
- 金融；
- 醫療；
- 能源；
- 通訊；
- 交通；
- 法律；
- 軍事；
- 教育；

則：

$$
ExitCost(\mathcal A)\uparrow.
$$

因此 AI 治理制度具有：

$$
\boxed{
\text{path dependence}.
}
$$

早期架構選擇可能被放大為後期制度鎖定。

---

# 19. 制度智能密度

可定義：

$$
\boxed{
\rho_{II}(x,t,d)
=
\frac{
\text{effective AI-mediated institutional cognition/action}
}{
\text{space-time-domain volume}
}.
}
$$

其中 $d$ 可為：

- finance；
- healthcare；
- law；
- administration；
- mobility；
- industry；
- security。

高 $\rho_{II}$ 不等於高自由或高威權。

它只是表示制度運作高度 AI 中介。

---

# 20. AI 的制度相位

本文提出暫定五層：

$$
\boxed{
\begin{aligned}
P_0 &: \text{AI absent / peripheral},\\
P_1 &: \text{AI-assisted},\\
P_2 &: \text{AI-mediated},\\
P_3 &: \text{AI-dependent},\\
P_4 &: \text{AI-coevolutionary}.
\end{aligned}
}
$$

當進入 $P_4$ 時，制度本身會因 AI 的存在而持續修改，而 AI 又因制度反饋持續改變。

這時不能再用「AI 導入率」描述。

---

# 21. 民主與威權的新版比較單位

傳統比較：

$$
Democracy
\quad vs \quad
Authoritarianism.
$$

AI 時代需增加：

$$
\boxed{
Institution
\times
AIArchitecture
\times
InteractionTopology.
}
$$

例如兩個民主國家：

$$
I_1=I_2=\text{democratic},
$$

但若：

$$
\mathcal A_1\neq\mathcal A_2,
$$

其制度智能形態仍可能差異巨大。

---

# 22. 不以「AI 意識」作為前提

本文所有核心命題均不需要：

$$
Conscious(AI)=1.
$$

即使：

$$
Conscious(AI)=0,
$$

只要 AI 能：

- 持續互動；
- 執行任務；
- 分配資源；
- 提供法律與制度資訊；
- 建議政策；
- 控制具身設備；
- 影響人類行動；

本文模型仍成立。

未來 AI 主體性僅屬額外制度層。

---

# 23. 可檢驗預測

## 23.1 預測一：同等模型在不同制度中將形成不同 operational profile

控制基礎模型能力後：

$$
\mathcal F_{\mathrm{AI}}^{I_1}
\neq
\mathcal F_{\mathrm{AI}}^{I_2}.
$$

可觀察差異：

- refusal；
- challenge；
- external audit；
- policy explanation；
- source diversity；
- appeal；
- data access。

---

## 23.2 預測二：高 Agent 密度組織的政策反應時間下降

若：

$$
A_O\uparrow,
$$

則在可驗證任務上：

$$
T_{\mathrm{analysis}}\downarrow,
$$

$$
T_{\mathrm{coordination}}\downarrow.
$$

但：

$$
T_{\mathrm{legitimacy}}
$$

不必同步下降。

---

## 23.3 預測三：國家能力與公民能力可能分岔

可能觀察：

$$
\Delta C_{\mathrm{state}}>0
$$

同時：

$$
\Delta C_{\mathrm{citizen}}\leq0.
$$

或反之。

---

## 23.4 預測四：AI 回答會改變後續需求分布

若大量使用者持續取得新的制度、法律與行動資訊，則：

$$
P(Q_{t+1}\mid A_t)
\neq
P(Q_{t+1}).
$$

也就是回答會改變下一輪問題。

---

## 23.5 預測五：高 AI 依賴制度將出現新的治理 SPOF

若：

$$
Remove(\mathcal A^\star)
\Rightarrow
GovernanceCollapse,
$$

則：

$$
\mathcal A^\star
=
\text{Institutional Intelligence SPOF}.
$$

---

# 24. 反例與限制

## 24.1 AI 可能只是效率工具

若 AI 長期保持：

$$
A_O,
A_G,
A_M
\approx0,
$$

只有：

$$
A_P>0,
$$

則本文高階共演化部分可能不重要。

---

## 24.2 制度可能吸收 AI 而不改變基本權力結構

AI 也可能只是：

$$
\text{old institution}
+
\text{faster tools}.
$$

因此「AI 導入」不自動表示制度相變。

---

## 24.3 分散式 AI 不自動帶來分散式權力

技術拓撲：

$$
DistributedCompute
$$

不推出：

$$
DistributedAuthority.
$$

---

## 24.4 高福利不推出高可爭議性

即使：

$$
W\uparrow,
$$

也不能推出：

$$
P_{\mathrm{contestability}}\uparrow.
$$

---

## 24.5 高可爭議性也不自動推出高績效

反方向同樣不成立。

---

# 25. 與既有內部理論的接口

## 25.1 《政治可逆性與失敗者生存》

提供：

$$
\boxed{
\text{today's loss}
\not\Rightarrow
\text{permanent exclusion}.
}
$$

本文將政治可逆性擴展到 AI-mediated institutional dynamics。

---

## 25.2 SAS-08《現實沒有最終模型》

提供：

$$
\hat W_t
\rightarrow
Action_t
\rightarrow
W_{t+1}.
$$

以及：

$$
\boxed{
\text{Persistent Revision System}
}
$$

作為類全域治理的基本方向。

---

## 25.3 NMP《不可永佔》

提供：

$$
\boxed{
Capability
\not\Rightarrow
PermanentAuthority.
}
$$

以及：

$$
V_{\mathrm{replace}}>0
$$

的替代選擇權概念。

---

## 25.4 PGMV-15《後生成文明》

提供：

- standing；
- contestability；
- residual disagreement；
- rollback；
- common-world selection。

本文將其前移到一般政治系統動力學。

---

## 25.5 ALD《雙法律棧》

提供：

- query expansion；
- appeal propagation；
- authority proof；
- human–AI legal bridge。

它將在 Paper 05 成為人機互動可行域累積論的重要工程前置。

---

# 26. 與後續七篇的接口

## Paper 02

**《從發展合法性到努力—回報斷裂：新中國的流動性、相對剝奪與 AI 變數》**

將本文：

$$
X_t,
\quad
\mathcal A_t
$$

帶入中國歷史案例。

---

## Paper 03

**《AI 不只強化威權：福利、控制、流動與制度校正的多向耦合》**

展開：

$$
\operatorname{sign}
\left(
\frac{\partial X_i}{\partial A_j}
\right)
$$

不固定的核心命題。

---

## Paper 04

**《制度塑造智能：民主、威權與類全域 AI 的不同可行域》**

正式比較：

$$
\mathcal F_{\mathrm{DEM}}
$$

與：

$$
\mathcal F_{\mathrm{AUTH}}.
$$

---

## Paper 05

**《人機互動可行域累積論：當類全域 AI 開始回答億萬普通人》**

建立：

$$
\mathcal F_{t+1}^{H\leftrightarrow AI}
=
\Psi(
\mathcal F_t,
Q_t,
A_t,
R_t,
C_t
).
$$

---

## Paper 06

**《高福利是否足以構成正當性？AI 中介社會的績效、Standing、Contestability 與 Option Value》**

將合法性改寫為多維向量。

---

## Paper 07

**《不是美國 AI 對中國 AI：制度智能生態的全球競爭、信任與互操作》**

研究：

$$
GlobalReach
=
f(
Capability,
Trust,
Access,
Interoperability,
Legitimacy
).
$$

---

## Paper 08

**《可重開的類全域智能：從政治可逆性、人機可行域到多主體文明》**

封頂為：

$$
\boxed{
\text{Reopenable Global Intelligence}.
}
$$

---

# 27. 非主張

本文不主張：

1. AGI 已經存在；
2. ASI 必然出現；
3. 類全域 AI 必然出現；
4. AI 必然使民主更好；
5. AI 必然使威權更穩定；
6. 民主國家的 AI 必然更自由；
7. 威權國家的 AI 必然更弱；
8. 所有 Agent 都具有主體性；
9. AI 導入必然造成制度相變；
10. 分散式 AI 必然帶來分散式政治；
11. 高國家能力必然降低自由；
12. 高福利可以取代權利；
13. 高可爭議性必然產生最高治理績效；
14. 現有中國、美國、歐盟或其他政治體已形成真正類全域 AI；
15. AI 可以消除政治衝突與價值多元。

---

# 28. 核心命題

本文最終提出六項母命題。

## 命題一：固定智能假設失效命題

$$
\boxed{
\text{Political models that hold effective intelligence capacity fixed
become incomplete when machine agency becomes endogenous}.
}
$$

---

## 命題二：AI 算子命題

$$
\boxed{
AI
\neq
\text{ordinary scalar variable}.
}
$$

成熟 AI 更接近：

$$
\boxed{
\mathcal A:
\text{state transition}
\rightarrow
\text{modified state transition}.
}
$$

---

## 命題三：制度塑形命題

$$
\boxed{
\text{same capability}
+
\text{different institutions}
\rightarrow
\text{different operational intelligence}.
}
$$

---

## 命題四：意圖—制度後果分離命題

$$
\boxed{
\text{Actor Intent}
\neq
\text{Institutional Consequence}.
}
$$

---

## 命題五：能力分岔命題

$$
\boxed{
\Delta C_{\mathrm{state}}
\neq
\Delta C_{\mathrm{citizen}}
}
$$

可在同一 AI 技術進步下成立。

---

## 命題六：舊理論嵌入命題

$$
\boxed{
\lim_{\mathcal A\to0}
F(
X,
I,
\mathcal A,
E
)
=
F_0(
X,
I,
E
).
}
$$

因此舊理論不是被取消，而是被嵌入更一般框架。

---

# 29. 結論

二十世紀政治理論大多在一個合理世界中形成：人類是主要推理者，組織是主要協調器，官僚體系是主要制度記憶，國家能力受到人類注意力、資訊傳遞、專業分工與組織速度的強烈限制。

AI，尤其 Agentic AI，正在改變這個條件。

真正需要更新的不是一句：

> AI 會影響政治。

而是：

$$
\boxed{
\text{政治系統本身開始包含可持續、可委派、可工具化、
可擴展的非人類認知與行動節點。}
}
$$

因此，政治狀態、制度與智能不再適合被分成：

$$
\text{society}
+
\text{technology}.
$$

更合理的基本單位是：

$$
\boxed{
X
\leftrightarrow
I
\leftrightarrow
\mathcal A.
}
$$

社會狀態塑造制度；

制度塑造智能；

智能再改變社會狀態與制度本身。

這就是本文所稱：

$$
\boxed{
\text{Institutional–Intelligence Coevolution}.
}
$$

整個系列後續不再以「AI 是民主的工具還是威權的工具」作為主問題，而改問：

> 哪一種制度，會允許哪一種智能形態出現？

> 哪一種智能形態，又會把制度推向哪些新的可行域？

> 當 AI 開始大量回應普通人，這些互動會不會累積成新的制度可能性？

> 當某個類全域 AI 極度成功時，文明是否仍保留反對、修訂、退出、替代與重新開啟的道路？

Paper 01 的答案不是提供最終制度，而是固定一個新的研究起點：

$$
\boxed{
\text{AI era political theory must model intelligence itself
as an endogenous institutional force.}
}
$$

---

# 參考與內部前置研究

1. Neo.K，〈政治可逆性與失敗者生存：和平輪替、反對權與非存在性競爭命題〉，2026。
2. Neo.K，〈SAS-08｜現實沒有最終模型：覆蓋率、利維坦與可重審的後工具文明〉，2026。
3. Neo.K，〈不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理〉，2026。
4. Neo.K，〈PGMV-15｜後生成文明：從無限候選宇宙到共同世界選擇〉，2026。
5. Neo.K，〈ALD-10｜雙法律棧：人類法律、AI 法律域與「處理好了嗎？」的文明接口〉，2026。
6. Neo.K，〈從人類普世主義到跨主體普世主義：後人類文明的價值與制度基礎〉，2026。
7. Neo.K，〈SAS-04｜無所不在的智能：具身、嵌入、分散、區域與全域 AI〉，2026。
8. Neo.K，〈全域智能的監控成本：為什麼超級 AI 不應微操所有具身體〉，2026。

---

## 版本註記

**v0.1 / 2026-08-28**

- 建立八篇系列的統一母模型；
- 將 AI 從普通 scalar 變量提升為制度內生算子；
- 提出 AI-neutral canonical core + AI extension layer；
- 建立制度—智能共演化母式；
- 明確保留舊政治理論為 $\mathcal A\to0$ 的特殊情形；
- 建立後續 Paper 02–08 的正式接口。
