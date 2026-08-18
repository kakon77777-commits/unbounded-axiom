# PGMV-13 — 意義空間與價值空間：第四空間的形式化

## Meaning Space and Value Space: Formalizing the Fourth Space

**系列：** 後生成文明的意義與價值理論 / Post-Generative Meaning and Value Theory  
**系列代碼：** PGMV  
**論文序號：** 13  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** CI 2.0；GCS；LSI-PSD；Cross-Subject Universalism；OU-TGB；PGMV-01—12  
**文件地位：** Unified Value–Meaning Space Foundational Paper / 統一價值—意義空間第一篇  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文提出「第四空間」作為後生成文明中價值與意義的形式化分析層。這不是一個已證明存在的物理空間，也不是宣稱倫理、尊嚴、愛、真理、美或人生意義能被完整數值化。本文刻意拒絕把第四空間壓成單一 utility、reward、preference score 或 happiness scalar。本文使用 fiber、partial order、field、trajectory、strata 等數學語言作為結構化形式工具；除特別標明外，不主張這些比喻已構成嚴格拓撲／微分幾何定理。本文的最低目標是：建立一套足以區分「能生成」「能到達」「真的不同」「值得選擇」「對誰有意義」的型別系統。

---

## 摘要

PGMV-10 至 PGMV-12 完成了三個空間的文明級接合：

$$
\boxed{
\begin{aligned}
\mathcal C &: \text{Concept / Possibility Space}\\
\mathcal G &: \text{Geometric Reachability Space}\\
\mathcal L &: \text{Logic / Coverage Space}.
\end{aligned}
}
$$

它們分別回答：

$$
\text{What can be generated?}
$$

$$
\text{What can be reached?}
$$

$$
\text{What has genuinely been explored?}
$$

但三者共同留下同一個無法內生解決的問題：

$$
\boxed{
\textbf{What is worth choosing, protecting, preserving, committing to, and living through?}
}
$$

這就是本文提出的：

$$
\boxed{
\textbf{Fourth Space}.
}
$$

本文將第四空間寫成：

$$
\boxed{
\mathfrak{VM}
}
$$

即：

**Value–Meaning Space，價值—意義空間。**

它不是單純的 $\mathcal V$，因「什麼有價值」和「什麼對某一個具歷史的主體形成意義」不是同一問題。也不是單純的 $\mathcal M$，因主體感到有意義，不自動證明該行動在道德、真理、關係或公共價值上值得。

因此：

$$
\boxed{
\text{Value}
\neq
\text{Meaning}.
}
$$

更完整地：

$$
\boxed{
\text{Utility}
\neq
\text{Value}
\neq
\text{Meaning}
\neq
\text{Dignity}.
}
$$

本文將 Value Space 定義為：

$$
\boxed{
\mathfrak V
=
\operatorname{Strat}
(
\mathcal V_F,
\mathcal V_P,
\mathcal V_O
),
}
$$

其中：

- $\mathcal V_F$：Protected Floor / 不應任意交換的基本價值底板；
- $\mathcal V_P$：Plural Trade-off Layer / 可存在合理衝突、局部排序與程序協調的多元價值層；
- $\mathcal V_O$：Open Aspirational Layer / 尚未封閉的新善、新關係、新美、新主體與新文明價值前沿。

這三層不是線性空間 direct sum；`Strat` 只表示分層結構。

Protected Floor 的候選包括：

- 基本人格尊嚴；
- 不被任意工具化；
- 免於任意暴力與酷刑；
- 基本 agency / standing；
- 在 cross-subject framework 下可被逐步擴展的 subject-protection floor。

Plural Layer 則包括：

- 公平與效率；
- 隱私與便利；
- 個人自由與公共風險；
- 文化保存與制度改革；
- autonomy 與 care；

等可能存在合理權衡的價值。

Open Layer 則保留：

$$
\boxed{
\text{value space is not assumed to be finally closed}.
}
$$

這是本文和後續 PGMV-14「開放終極與價值痕跡」的直接接口。

本文將 Meaning Space 定義為主體索引、關係索引、歷史索引的 realization structure：

$$
\boxed{
\mathfrak M
=
\left\{
\mathbf M_s(\gamma,R,H,t)
\right\},
}
$$

其中：

- $s$：subject；
- $\gamma$：實際生命／行動 trajectory；
- $R$：relation structure；
- $H$：lived history；
- $t$：時間。

沿用 PGMV-04：

$$
\boxed{
\mathbf M_s
=
(
M_C,
M_A,
M_R,
M_P,
M_N,
M_H
),
}
$$

其中：

- $M_C$：contribution meaning；
- $M_A$：agency / self-authorship meaning；
- $M_R$：relational meaning；
- $M_P$：participatory meaning；
- $M_N$：normative / commitment meaning；
- $M_H$：historical / lived-continuity meaning。

因此兩個主體即使到達同一 endpoint：

$$
W_a=W_b,
$$

其：

$$
\mathbf M_a
$$

與：

$$
\mathbf M_b
$$

仍可完全不同。

這延續 PGMV-05：

$$
\text{Artifact Identity}
\neq
\text{Meaning-Event Identity},
$$

以及 PGMV-11：

$$
\text{Endpoint Identity}
\neq
\text{Path-Value Identity}.
$$

本文進一步提出 **Value–Meaning Fiber Schema**。

令 base state 為：

$$
\boxed{
b
=
(
W,
S,
R,
H,
t
),
}
$$

其中：

- $W$：world state；
- $S$：subject set；
- $R$：relations；
- $H$：history；
- $t$：time。

則每個 base state 上具有一個 value–meaning fiber：

$$
\boxed{
\mathcal F_b^{VM}
=
(
\mathcal V_b,
\mathcal M_b,
\mathcal U_b,
\mathcal T_b
),
}
$$

其中：

- $\mathcal V_b$：當前可辨識的價值結構；
- $\mathcal M_b$：主體／關係意義結構；
- $\mathcal U_b$：moral / value uncertainty；
- $\mathcal T_b$：歷時價值痕跡與已形成規範記憶。

全域第四空間因此寫成：

$$
\boxed{
\mathfrak{VM}
=
\bigsqcup_{b\in\mathcal B}
\mathcal F_b^{VM}.
}
$$

這是一個 schema，不是嚴格 fiber bundle theorem。其目的在於表達：

$$
\boxed{
\text{同一世界狀態中的價值與意義，必須依主體、關係、歷史與規範狀態解讀。}
}
$$

本文拒絕單一全域 scalarization。對價值候選 $x,y$，只要求在指定 subject / context / normative regime 下存在可能的 partial order：

$$
x
\succeq_{\mathcal V}^{s,R,H,t}
y.
$$

但也允許：

$$
\boxed{
x
\parallel_{\mathcal V}
y,
}
$$

即：

**incomparability。**

例如：

- 真理；
- 友情；
- 美；
- 自由；

不一定存在一個自然共同單位，把它們全部換算成：

$$
7.31\text{ utils}.
$$

本文把「所有價值都必須完全排序」稱為：

$$
\boxed{
\textbf{Total-Order Fallacy}.
}
$$

這一點與 2025--2026 年 pluralistic alignment 研究相互呼應。FGD-Align 2026 使用 fuzzy group decision-making 處理模糊、衝突與 minority preferences；Ali 等 AAAI-26 的實證顯示，preserving disagreement 與不同 preference representation 會實質改變 alignment 結果；Baum 與 Slavkovik 2025 則指出 social aggregation 與 moral aggregation 是不同問題，將多人偏好聚合起來不能暗中取代規範判斷。MORL 對 multiple moral values 的研究也同樣說明，單一 scalar reward 並不是唯一可用形式。

本文因此提出：

$$
\boxed{
\textbf{Aggregation–Normativity Separation Principle}.
}
$$

令：

$$
\mathsf{Agg}_S
$$

表示 social preference aggregation；

$$
\mathsf{Delib}_N
$$

表示 normative deliberation。

則：

$$
\boxed{
\mathsf{Agg}_S
\neq
\mathsf{Delib}_N.
}
$$

100 萬人都偏好某件事，不自動證明該事是善；一位專家提出某項倫理原則，也不自動取得民主合法性。

因此第四空間需要同時保留：

$$
\boxed{
\text{Preference}
+
\text{Reason}
+
\text{Rights}
+
\text{Standing}
+
\text{Uncertainty}
+
\text{Procedure}.
}
$$

本文進一步把 moral uncertainty 寫成：

$$
\boxed{
\mathcal U_V
=
\{
(
\mathcal N_i,
q_i,
c_i
)
\}_{i=1}^{m},
}
$$

其中：

- $\mathcal N_i$：normative model / moral perspective；
- $q_i$：可信度／支持權重；
- $c_i$：confidence / evidence quality。

但：

$$
q_i
$$

不必被當成 Bayesian objective probability；它可以只是 calibrated credence / model weight。

2026 的 moral-uncertainty 研究顯示，LLM 在道德 dilemmas 中的 confidence architecture 會影響 human–LLM alignment；AMULED 2026 也直接比較不同 moral belief aggregation functions，發現 aggregation method 可產生顯著不同 policy outcome。這支持本文的：

$$
\boxed{
\text{how uncertainty is represented is itself a value-system design choice}.
}
$$

本文也提出 **Disagreement Preservation Principle**：

$$
\boxed{
\Delta_V
=
\{
V_i-V_j
\}
}
$$

不應在最初就被平均消失。

尤其當：

- minority rights；
- cross-cultural values；
- subject-status uncertainty；

存在時，文明需要知道：

> 誰不同意？為什麼？差異在哪一層？

因此：

$$
\boxed{
\text{Consensus}
\neq
\text{Absence of Value Conflict}.
}
$$

Consensus 可能是：

- genuine convergence；
- majority dominance；
- model homogenization；
- suppressed minority；
- shared error。

第四空間因此必須保存 disagreement provenance。

本文將價值層進一步分成：

$$
\boxed{
\mathbf V
=
(
V_I,
V_R,
V_N,
V_E,
V_P,
V_A
),
}
$$

其中：

- $V_I$：intrinsic / end value；
- $V_R$：relational value；
- $V_N$：normative / rightness value；
- $V_E$：epistemic / truth-related value；
- $V_P$：procedural / legitimacy value；
- $V_A$：aspirational / open-ended value。

這種分類不是唯一 axiology。2026 Integrated Axiology–MCDA 類研究區分 intrinsic、instrumental、relational value；本文借用其「價值型別應顯式分離」的精神，但加入 PGMV 已建立的：

- subject standing；
- history；
- legitimacy；
- open ultimate。

本文明確不把：

$$
V_I,V_R,V_N,\ldots
$$

直接加總為單值。

只有在 domain 明確、trade-off 正當、權重有 provenance 時，才允許局部 scalarization：

$$
u_D(x)
=
\sum_i
\omega_i^D
v_i(x).
$$

並要求：

$$
\boxed{
\omega_i^D
\text{ are governance objects, not invisible constants}.
}
$$

誰定權重？

為何？

是否可申訴？

何時更新？

這些都屬於第四空間。

本文因而提出：

$$
\boxed{
\textbf{Value-Weight Provenance Principle}.
}
$$

任何會改變 consequential decision 的 value weights 都應具有：

- source；
- authority；
- scope；
- version；
- dissent record。

本文進一步把 PGMV-08 的 Human Floor + Open Subject Frontier 放進第四空間。令：

$$
\mathcal S_t
$$

為當前被承認／候選主體集合。

則：

$$
\boxed{
\mathfrak{VM}
=
\mathfrak{VM}(
\mathcal S_t
).
}
$$

如果未來新的 subject type 被承認，價值空間本身會改變，因：

- 新 interests；
- 新 rights；
- 新 relations；
- 新 vulnerability；

進入第四空間。

因此：

$$
\boxed{
\text{Subject Expansion}
\Rightarrow
\text{Value-Space Expansion}.
}
$$

這不是說新主體一出現就有所有權利，而是：

> value ontology 必須至少能表示它。

這直接接 PGMV-12 的 ontology capture。

本文提出：

$$
\boxed{
\textbf{Subject-Value Co-Expansion}.
}
$$

即：

$$
\mathcal S_t
\rightarrow
\mathcal S_{t+1}
$$

可能要求：

$$
\mathfrak V_t
\rightarrow
\mathfrak V_{t+1}.
$$

第四空間因此不能封閉在：

$$
\text{2026 human preference corpus}.
$$

這也指出 alignment 的一個深層限制：

$$
\boxed{
\text{Preference Learning}
\neq
\text{Value Discovery}.
}
$$

如果 AI 只學：

> 人們現在偏好什麼，

它可能忠實複製：

- prejudice；
- domination；
- inconsistency；
- short-term desire。

所以：

$$
\boxed{
\text{Align to Preference}
\not\Rightarrow
\text{Align to Worth}.
}
$$

2026 年 pluralistic alignment、explicit human purpose、agency-sensitive alignment 等工作都在不同程度上指出這個問題：alignment 不應被縮成從 feedback 中被動擬合一個固定 preference function，而需要處理人類 agency、目的、規範與制度。

本文因此建立：

$$
\boxed{
\textbf{Preference–Value–Meaning Triangle}.
}
$$

Preference：

$$
P_s(x)
=
\text{subject currently wants }x.
$$

Value：

$$
V(x)
=
\text{there are reasons / protections / goods supporting }x.
$$

Meaning：

$$
M_s(x,\gamma,H)
=
\text{x becomes significant in a lived subject trajectory}.
$$

三者可以重疊，但：

$$
\boxed{
P\neq V\neq M.
}
$$

例如：

1. 一個人偏好成癮行為：
   $$P>0$$
   但長期 value 可能低；
2. 一個抽象正義制度可能：
   $$V>0$$
   卻未必對某個人產生 lived meaning；
3. 一段痛苦照護承諾：
   當下 preference 可能低，但 relational / commitment meaning 高。

這使第四空間無法被單一即時 preference 取代。

本文進一步提出：

$$
\boxed{
\textbf{Meaning Realization Operator}
}
$$

$$
\mathsf{Realize}_M:
(
\mathfrak V,
s,
\gamma,
R,
H,
C
)
\rightarrow
\mathbf M_s.
$$

它表示：

> 價值如何在一個主體真實參與的生命／行動路徑中成為 lived meaning。

這不是 deterministic function；它是一個分析 schema。

同一個 value：

$$
V_{\mathrm{care}}
$$

對：

- caregiver；
- care recipient；
- observer；

可形成不同 meaning vector。

所以：

$$
\boxed{
\text{Value Universality}
\not\Rightarrow
\text{Meaning Uniformity}.
}
$$

這一點尤其重要。即使尊嚴被視為普遍價值，尊嚴如何被一個具體主體經驗，不必相同。

本文也提出 **Meaning Cannot Be Assigned by Force**：

$$
\boxed{
\operatorname{ProvideValueConditions}(a,s)
\not\Rightarrow
\operatorname{AssignMeaning}(a,s).
}
$$

一個 AI 可以：

- 提供安全；
- 生成作品；
- 安排生活；
- 創造機會；

但不能僅以：

> 這對你最好，

便把 lived meaning 直接寫入另一主體。

這是 PGMV-07 Care–Meaning Non-Substitution 的第四空間版本。

本文進一步提出 **Meaning Externalization Limit**：

$$
\boxed{
\text{Meaning support can be delegated;
meaning authorship cannot be fully presumed delegated without the subject's standing.}
}
$$

當然，主體可能自願委託大量生活決定，但 PGMV-06 的 commitment / agency 條件仍需成立。

本文還把關係作者權理論接入第四空間。前置理論提出：

$$
R_{AB}
$$

是由雙方共同生成、既不等於 $A$ 也不等於 $B$ 的第三空間。

因此關係價值不能只寫：

$$
V_A+V_B.
$$

還需：

$$
\boxed{
V_{R_{AB}}.
}
$$

也就是：

**Emergent Relational Value。**

一段關係可以具有：

- 共同歷史；
- 共同作品；
- 共同承諾；

其價值不是兩個個體 utility 的簡單加總。

因此第四空間包含：

$$
\boxed{
\text{subject values}
+
\text{relational values}
+
\text{collective values}.
}
$$

這也使 social choice 問題更複雜：有些價值不是「每個人先各自有，再聚合」，而是在共同實踐中生成。

本文稱：

$$
\boxed{
\textbf{Emergent Value Layer}.
}
$$

例如：

- friendship；
- constitutional trust；
- scientific community；
- shared world。

這些都可能是：

$$
\boxed{
\text{relation-generated goods}.
}
$$

本文由此提出第四空間的一個重要幾何性質候選：

$$
\boxed{
\textbf{Non-Separability}.
}
$$

一般地：

$$
V(A,B,R)
\neq
V(A)+V(B).
$$

這不是所有場景都成立，但在關係性價值中可能成立。

本文再引入 **Value Trace**，但只作 PGMV-14 的前置。前置 OU-TGB 系列提出：文明已形成的自由、尊嚴、平等、受害記憶、抗爭與規範修正，不能僅因未來更高權力出現，就被無痕重命名。

PGMV-13 將這一類歷史資料放入：

$$
\boxed{
\mathcal T_b.
}
$$

即 value–meaning fiber 中的：

**Trace Layer。**

它表示：

- 這個 value 如何出現；
- 曾經保護誰；
- 哪些傷害促使它形成；
- 哪些制度承諾已建立。

因此 value update：

$$
\mathfrak V_t
\rightarrow
\mathfrak V_{t+1}
$$

不能只看當下 preference。

它還需檢查：

$$
\boxed{
\text{trace-preserving revision}.
}
$$

但 PGMV-13 不宣稱任何當代 value 永遠不可修訂；真正的「不可任意反轉」條件留到 PGMV-14。

本文提出：

$$
\boxed{
\textbf{Revision–Erasure Separation}.
}
$$

$$
\operatorname{Revise}(V)
\not\Rightarrow
\operatorname{EraseTrace}(V).
$$

一個文明可以修正自由的理解，但不應假裝：

> 過去的奴役從來沒有造成傷害。

這是 fourth-space history。

本文進一步提出 **Value Landscape is Not Static**：

$$
\boxed{
\mathfrak{VM}_t
\rightarrow
\mathfrak{VM}_{t+1}.
}
$$

它隨：

- 新主體；
- 新科技；
- 新傷害；
- 新關係；
- 新知識；

改變。

但：

$$
\boxed{
\text{dynamic}
\neq
\text{arbitrary}.
}
$$

這正是 Open Ultimate / trace-preserving framework 的入口。

本文還提出 **Value Basin** 概念。不同文化／群體／主體可能在第四空間形成：

$$
B_V^{(1)},
B_V^{(2)},\ldots.
$$

如果 AI alignment 只訓練在一個 basin：

$$
B_V^\star,
$$

它可能把其他 basin 誤判為：

- noise；
- irrationality；
- misalignment。

這就是：

$$
\boxed{
\textbf{Value-Basin Monoculture}.
}
$$

2026 FGD-Align、pluralistic value operationalization 與 EACL moral-gap 結果都提供相鄰警告：模型在高人類共識情況下較容易對齊；當人類 moral disagreement 增加，模型和人類 judgment distribution 的 alignment 會下降，而且模型可能依賴比人類更窄的 moral value set。

因此第四空間需要：

$$
\boxed{
\text{value-distribution coverage}
}
$$

而不是只追：

$$
\text{majority-match accuracy}.
$$

本文定義：

$$
\boxed{
C_V
=
\operatorname{Coverage}(
\mathfrak V
\mid
\text{stakeholder/evidence regime}
).
}
$$

但像 LSI 一樣：

$$
\boxed{
C_V\text{ high}
\not\Rightarrow
\text{moral truth solved}.
}
$$

這是 **Value Coverage Non-Conclusion**。

本文由此建立：

$$
\boxed{
\textbf{Value-Space Observatory}
}
$$

簡寫：

$$
\boxed{
VSO.
}
$$

VSO 不是「道德裁判機」，而是觀測：

- 哪些價值被建模；
- 哪些主體被代表；
- 哪些 disagreement 被壓平；
- 哪些 protected floor 被觸碰；
- 哪些 value weights 無 provenance；
- 哪些 value basin 長期沒有 sample；
- 哪些新 value dimensions 正在形成。

其層次：

1. subject layer；
2. value-type layer；
3. relation layer；
4. disagreement / uncertainty layer；
5. trace layer；
6. commitment layer。

VSO 和 PGMV-12 FSO 可以相互連接：

$$
\boxed{
FSO
\leftrightarrow
VSO.
}
$$

FSO 問：

> 我們想過哪些不同未來？

VSO 問：

> 這些未來究竟代表哪些不同價值與主體？

本文進一步正式接回 CI、GCS、LSI：

$$
\boxed{
\begin{aligned}
CI &: \mathcal C\\
GCS &: \mathcal G\\
LSI &: \mathcal L\\
PGMV &: \mathfrak{VM}.
\end{aligned}
}
$$

因此後生成文明的核心狀態可寫：

$$
\boxed{
\mathfrak X_t
=
(
\mathcal C_t,
\mathcal G_t,
\mathcal L_t,
\mathfrak{VM}_t,
\mathcal S_t
).
}
$$

這裡 $\mathcal S_t$ 不被吸收到第四空間，因主體集合是價值的承載者、生成者與受影響者，具有獨立本體角色。

文明選擇算子：

$$
\boxed{
\mathsf{Choose}:
\mathfrak X_t
\rightharpoonup
W_{\mathrm{chosen}}.
}
$$

仍然是 partial：

$$
\rightharpoonup,
$$

因某些 value conflict 沒有唯一可計算答案。

本文將：

$$
\boxed{
\text{no unique answer}
}
$$

視為合法輸出之一。

即：

$$
\boxed{
\textbf{Normative Non-Uniqueness}.
}
$$

AI 不應在價值不可完全聚合時假裝：

> 我算出唯一正確答案。

成熟 fourth-space system 需要能輸出：

- incomparable；
- unresolved；
- legitimate plurality；
- needs deliberation。

這正是 moral uncertainty / pluralistic alignment 的重要 lesson。

本文因此提出：

$$
\boxed{
\textbf{Normative Abstention}.
}
$$

在證據／正當性不足時，AI 可說：

> 這不是我應該單方面 scalarize 的價值衝突。

並把 decision route 到：

- stakeholder deliberation；
- democratic procedure；
- rights review；
- domain authority。

這不是 intelligence failure，而是：

$$
\boxed{
\text{type-correct governance}.
}
$$

本文還提出 **Fourth-Space Non-Sovereignty**。即使 ASI 對：

- consequences；
- human preferences；
- moral literature；

理解極深，也不能由此推出：

$$
\boxed{
\text{perfect value map}
\Rightarrow
\text{sovereign authority}.
}
$$

因為：

- value map 仍含 plural standing；
- meaning 含第一人稱作者性；
- legitimacy 不等於 prediction accuracy。

因此：

$$
\boxed{
\textbf{Value Knowledge}
\neq
\textbf{Value Ownership}.
}
$$

這是 PGMV-11 Geometric Paternalism 的第四空間版本。

本文最終提出 **Fourth-Space Integrity Conditions**：

$$
\boxed{
\mathcal I_{VM}
=
(
T,
P,
D,
U,
R,
O,
S
),
}
$$

其中：

- $T$：type safety；
- $P$：pluralism；
- $D$：disagreement preservation；
- $U$：uncertainty representation；
- $R$：rights / protected floor；
- $O$：open ontology；
- $S$：subject standing。

若一個 alignment system：

- 只有 preference；
- 沒有 rights；
- 沒有 disagreement；
- 沒有 value provenance；
- 沒有 subject expansion；
- 沒有 meaning trajectory；

則它還不能被稱為完整 fourth-space model。

PGMV-13 的結論不是：

> 我們現在終於有一個方程式算出人生意義。

恰好相反。

它建立的是：

$$
\boxed{
\textbf{一套防止 AI 把意義與價值算錯型別的形式框架。}
}
$$

它允許數學、AI 與制度建模進入價值問題，但不把價值問題退化成一個「更聰明的分數」。

**關鍵詞：** Value–Meaning Space、fourth space、value pluralism、meaning in life、pluralistic alignment、moral uncertainty、social choice、value-sensitive AI、partial order、subject-indexed value、relational value、dignity、normative abstention、value provenance、open value ontology

---

# 1. 第四空間從哪裡來？

前三個空間已經可以非常強。

---

# 2. CI

可以生成：

$$
10^9
$$

候選。

---

# 3. GCS

可以讓其中大量候選變 reachable。

---

# 4. LSI

可以告訴我們其中只有：

$$
10^4
$$

真正深層不同。

---

# 5. 但還是缺：

> 哪個值得？

---

# 6. 所以第四空間不是 optional decoration

---

# 7. 沒有第四空間

前三個空間只提供：

$$
\boxed{
\text{capability}.
}
$$

---

# 8. 有第四空間

才開始：

$$
\boxed{
\text{civilizational choice}.
}
$$

---

# 9. Four-Space Separation

$$
\boxed{
\begin{aligned}
\mathcal C &: \text{can imagine}\\
\mathcal G &: \text{can reach}\\
\mathcal L &: \text{is distinct}\\
\mathfrak{VM} &: \text{is worth / means}.
\end{aligned}
}
$$

---

# 10. 不能把第四空間塞回前三個

---

# 11. Novelty is not value

$$
\boxed{
N(x)>0
\not\Rightarrow
V(x)>0.
}
$$

---

# 12. Reachability is not value

$$
\boxed{
R(x)>0
\not\Rightarrow
V(x)>0.
}
$$

---

# 13. Truth is not total value

一個真理可被用於善或惡。

---

# 14. 但 truth itself 可以有 epistemic value。

---

# 15. 所以：

$$
\boxed{
V_E
\neq
V_N.
}
$$

---

# 16. Utility is not dignity

$$
\boxed{
U(s)\downarrow
\not\Rightarrow
D(s)\downarrow.
}
$$

---

# 17. PGMV-04 已建立。

---

# 18. Value ≠ Meaning

一座古蹟有公共 value。

---

# 19. 對某人可能沒有 lived meaning。

---

# 20. 反之

一個私人紀念物對某人 meaning 高。

---

# 21. 社會公共 value 可能有限。

---

# 22. 所以：

$$
\boxed{
V(x)
\neq
M_s(x).
}
$$

---

# 23. Meaning is subject-indexed

$$
M_s.
$$

---

# 24. Value can be subject-relative, relational, or public

---

# 25. Value Typing

至少：

$$
\boxed{
\mathbf V
=
(
V_I,V_R,V_N,V_E,V_P,V_A
).
}
$$

---

# 26. Intrinsic

作為目的自身。

---

# 27. Relational

因關係產生。

---

# 28. Normative

正當／義務／權利。

---

# 29. Epistemic

真理、理解。

---

# 30. Procedural

公平、合法、可申訴。

---

# 31. Aspirational

尚未封閉的高階善。

---

# 32. 這不是終極分類

---

# 33. 是 type system。

---

# 34. Value Type Safety

不能：

$$
V_E
$$

直接 cast 成：

$$
V_N.
$$

---

# 35. 「是真的」

不等於：

> 應該做。

---

# 36. 不能：

$$
V_{\mathrm{economic}}
$$

cast：

$$
V_{\mathrm{dignity}}.
$$

---

# 37. 不能：

$$
M_s
$$

cast：

$$
V_{\mathrm{public}}.
$$

---

# 38. 一個人覺得很有意義

不自動有權傷害他人。

---

# 39. Fourth-Space Type Error

本文稱：

$$
\boxed{
\textbf{Fourth-Space Type Error}.
}
$$

---

# 40. 很多 alignment 問題其實是 type error

---

# 41. 把 preference 當 value。

---

# 42. 把 majority 當 rightness。

---

# 43. 把 welfare 當 autonomy。

---

# 44. 把 intelligence 當 dignity。

---

# 45. PGMV 一直在拆這些。

---

# 46. Value Space Strata

$$
\boxed{
\mathfrak V
=
Strat(
\mathcal V_F,
\mathcal V_P,
\mathcal V_O
).
}
$$

---

# 47. Floor

protected。

---

# 48. Plural

trade-off / context。

---

# 49. Open

new goods / values。

---

# 50. Floor 不是完整 morality

---

# 51. 只設不可任意穿越底線。

---

# 52. Plural layer 才有大量生活差異

---

# 53. Open layer 保留未來。

---

# 54. 為什麼三層？

避免兩極。

---

# 55. 極端一：

所有價值固定。

---

# 56. 極端二：

所有價值可任意改。

---

# 57. PGMV 採：

$$
\boxed{
\text{protected traces}
+
\text{plural trade-offs}
+
\text{open frontier}.
}
$$

---

# 58. PGMV-14 會正式展開 trace。

---

# 59. Value Partial Order

$$
x\succeq_V y.
$$

---

# 60. 不是所有 pair 可比較。

---

# 61. Incomparability

$$
x\parallel_V y.
$$

---

# 62. 例：

友情 vs 數學發現。

---

# 63. 問：

哪個值 83？

荒謬。

---

# 64. 所以 total scalar 不是必要。

---

# 65. Total-Order Fallacy

$$
\boxed{
\forall x,y:
x\succeq y\lor y\succeq x
}
$$

不應被無條件假設。

---

# 66. 但 local decision 仍要選

---

# 67. 怎麼辦？

---

# 68. 可以：

- constraints；
- Pareto；
- procedure；
- commitment。

---

# 69. 不需先有 universal total order。

---

# 70. 這是 PGMV-11。

---

# 71. Value Fiber

base：

$$
b=(W,S,R,H,t).
$$

---

# 72. fiber：

$$
\mathcal F_b^{VM}.
$$

---

# 73. 為什麼 subject 要在 base？

同一 action 對不同 subject 影響不同。

---

# 74. 為什麼 relation？

價值可 emerge。

---

# 75. 為什麼 history？

同一 action 在不同歷史有不同意義。

---

# 76. 為什麼 time？

values / status 改變。

---

# 77. Value–Meaning Fiber Schema

$$
\boxed{
\mathcal F_b^{VM}
=
(
\mathcal V_b,
\mathcal M_b,
\mathcal U_b,
\mathcal T_b
).
}
$$

---

# 78. $\mathcal V_b$

recognized value structures。

---

# 79. $\mathcal M_b$

lived meaning。

---

# 80. $\mathcal U_b$

uncertainty。

---

# 81. $\mathcal T_b$

historical traces。

---

# 82. 全域

$$
\boxed{
\mathfrak{VM}
=
\bigsqcup_b
\mathcal F_b^{VM}.
}
$$

---

# 83. 再次：

schema，非 topology theorem。

---

# 84. Meaning Vector

$$
\boxed{
\mathbf M_s
=
(
M_C,M_A,M_R,M_P,M_N,M_H
).
}
$$

---

# 85. Contribution

---

# 86. Agency

---

# 87. Relation

---

# 88. Participation

---

# 89. Commitment

---

# 90. History

---

# 91. Meaning Multi-Channel

$$
\boxed{
M
\neq
M_C
}
$$

PGMV-04。

---

# 92. Meaning Path Dependence

$$
\boxed{
M_s(W)
\neq
M_s(W,\gamma,H)
}
$$

一般。

---

# 93. Endpoint same

path different。

---

# 94. PGMV-11 already。

---

# 95. Meaning Realization Operator

$$
\boxed{
\mathsf{Realize}_M:
(
\mathfrak V,
s,\gamma,R,H,C
)
\rightharpoonup
\mathbf M_s.
}
$$

---

# 96. Partial

因 meaning 不保證形成。

---

# 97. 一個 objective good

subject 可完全不感到 meaningful。

---

# 98. 也可能之後才理解。

---

# 99. Retrospective Meaning

$$
M_s(t_2)
\neq
M_s(t_1).
$$

---

# 100. 人生意義可被重新詮釋。

---

# 101. 但 reinterpretation 不改過去 event。

---

# 102. Meaning Revision ≠ History Rewrite

$$
\boxed{
\operatorname{Reinterpret}(H)
\not\Rightarrow
\operatorname{Erase}(H).
}
$$

---

# 103. PGMV-05。

---

# 104. Preference

$$
P_s(x,t).
$$

---

# 105. Value

$$
V(x,S,R,t).
$$

---

# 106. Meaning

$$
M_s(x,\gamma,H,t).
$$

---

# 107. 三角

$$
\boxed{
P
\neq
V
\neq
M.
}
$$

---

# 108. Preference can be informed by value

---

# 109. value can shape meaning

---

# 110. meaning can reshape preference

---

# 111. feedback system

$$
P_t
\leftrightarrow
V_t
\leftrightarrow
M_t.
$$

---

# 112. 不是 hierarchy only。

---

# 113. Preference Learning Problem

AI 學：

$$
\hat P_s.
$$

---

# 114. 容易誤稱：

$$
\hat V_s.
$$

---

# 115. Preference–Value Collapse

$$
\boxed{
\textbf{Preference–Value Collapse}.
}
$$

---

# 116. 人會偏好 harmful things。

---

# 117. 人也會 short-term inconsistent。

---

# 118. 因此 alignment 不能只 maximum satisfaction。

---

# 119. But value paternalism also danger

---

# 120. AI 說：

> 我知道真正的價值。

也危險。

---

# 121. So fourth space needs procedure。

---

# 122. Preference Autocracy vs Moral Autocracy

兩個極端。

---

# 123. 第一：

只看 preference。

---

# 124. 第二：

單一 moral authority。

---

# 125. PGMV 需要：

$$
\boxed{
\text{plural deliberation + protected floor}.
}
$$

---

# 126. Aggregation–Normativity Separation

$$
\boxed{
Agg_S
\neq
Delib_N.
}
$$

---

# 127. Social Aggregation

誰想什麼。

---

# 128. Moral Aggregation

不同 normative reasons 如何比較。

---

# 129. 它們可以互相依賴

但不能偷換。

---

# 130. 2025 AIES result 正是此警告。

---

# 131. Majority Vote

$$
V_{\mathrm{majority}}.
$$

---

# 132. 不能壓掉 minority rights。

---

# 133. Minority Persistence Constraint

$$
\boxed{
\text{minority dissent}
\not\Rightarrow
\text{noise}.
}
$$

---

# 134. FGD-Align 2026

以 fuzzy preference 保留 ambiguity。

---

# 135. AAAI-26 pluralistic value study

preserving disagreement 會改結果。

---

# 136. 所以 disagreement 是 data

---

# 137. 不只是 error。

---

# 138. Disagreement Field

$$
\boxed{
\Delta_V(i,j,x)
=
d(
V_i(x),
V_j(x)
).
}
$$

---

# 139. distance 依 domain。

---

# 140. 不是所有 value 可 metric。

---

# 141. 可以是 symbolic conflict relation。

---

# 142. Disagreement Types

1. factual；
2. value-weight；
3. rights；
4. identity；
5. worldview。

---

# 143. AI 必須區分。

---

# 144. Factual disagreement

可更多 evidence。

---

# 145. Value disagreement

不能只 search web。

---

# 146. Rights conflict

需要 legal / normative。

---

# 147. Worldview conflict

可能不可完全解。

---

# 148. Conflict Typing

$$
\boxed{
T_\Delta.
}
$$

---

# 149. Moral Uncertainty

$$
\mathcal U_V
=
\{
(N_i,q_i,c_i)
\}.
$$

---

# 150. $\mathcal N_i$

normative theories / perspectives。

---

# 151. $q_i$

credence。

---

# 152. $c_i$

evidence confidence。

---

# 153. Why two weights?

相信一個 theory

和我們有多少 evidence

不完全同。

---

# 154. 可以更細。

---

# 155. 不做 fake probability。

---

# 156. AMULED

顯示不同 aggregation function 改 policy。

---

# 157. Dropouts in Confidence

顯示 model uncertainty calibration 影響 moral alignment。

---

# 158. 所以：

$$
\boxed{
\text{uncertainty representation is consequential}.
}
$$

---

# 159. Moral Confidence Fallacy

LLM 很肯定

不等於 moral truth。

---

# 160. Confidence–Normativity Separation

$$
\boxed{
Conf(x)\uparrow
\not\Rightarrow
Right(x)\uparrow.
}
$$

---

# 161. important。

---

# 162. Normative Abstention

如果 conflict unresolved：

$$
\boxed{
\mathsf{Abstain}_N.
}
$$

---

# 163. output：

- unresolved；
- incomparable；
- requires authority；
- needs deliberation。

---

# 164. AI 不必每次 give answer。

---

# 165. 這是 type-correct。

---

# 166. Normative Non-Uniqueness

$$
\boxed{
|\operatorname{Argmax}_{VM}|
>1
}
$$

可以合法。

---

# 167. 甚至沒有 argmax。

---

# 168. partial order。

---

# 169. 所以 decision system 需要 procedures。

---

# 170. Procedural Value

$$
V_P.
$$

---

# 171. Process itself has value。

---

# 172. Democracy example

有時 outcome 不 perfect

但 legitimacy higher。

---

# 173. Procedure–Outcome Separation

$$
\boxed{
V_{\mathrm{outcome}}
\neq
V_{\mathrm{procedure}}.
}
$$

---

# 174. PGMV-11 legitimacy。

---

# 175. Value Weight Provenance

局部 scalar：

$$
u_D
=
\sum_i\omega_i v_i.
$$

---

# 176. weights must have:

- source；
- scope；
- version；
- dissent。

---

# 177. Hidden Value Weight

如果 recommender：

> secret weights。

---

# 178. governance opacity。

---

# 179. Weight Governance

$$
\boxed{
\omega
\in
\text{governance state}.
}
$$

---

# 180. 不是 magic hyperparameter。

---

# 181. Dynamic Values

$$
\mathfrak V_t
\rightarrow
\mathfrak V_{t+1}.
$$

---

# 182. Why dynamic?

new technology。

---

# 183. digital privacy didn't exist same form historically。

---

# 184. AI subject rights may emerge。

---

# 185. New subject => new values

---

# 186. Subject-Value Co-Expansion

$$
\boxed{
\mathcal S_t\uparrow
\Rightarrow
Dim(
\mathfrak V_t
)
\text{ may increase}.
}
$$

---

# 187. not necessarily numeric dimension。

---

# 188. ontology expansion。

---

# 189. PGMV-08。

---

# 190. Human Floor

existing human rights protected。

---

# 191. new subject frontier open。

---

# 192. fourth space must support both。

---

# 193. Non-Regression

new AI values cannot lower human floor automatically。

---

# 194. But human floor doesn't close frontier。

---

# 195. This becomes constraints。

---

# 196. Meaning + Dignity

Dignity is not a meaning score。

---

# 197. A person can feel meaningless

and still have dignity。

---

# 198. Dignity–Meaning Separation

$$
\boxed{
M_s\downarrow
\not\Rightarrow
D_s\downarrow.
}
$$

---

# 199. Crucial。

---

# 200. Mental / existential crisis does not erase rights。

---

# 201. Conversely

high meaning doesn't grant domination。

---

# 202. Meaning–Authority Separation

$$
\boxed{
M_s\uparrow
\not\Rightarrow
A_s\uparrow.
}
$$

---

# 203. fanatic can feel meaning

not moral right。

---

# 204. Fourth space must type dignity separately。

---

# 205. Dignity Floor

$$
D_F(s)>0
$$

for humans, PGMV-08。

---

# 206. Subject candidates

graded review。

---

# 207. Dignity is not reward dimension。

---

# 208. It is standing constraint。

---

# 209. Protected Floor

therefore includes status constraints。

---

# 210. Relation Value

PGMV-05：

relationship is time-extended。

---

# 211. Relational Co-Authorship

$$
R_{AB}.
$$

---

# 212. Relation has emergent structure。

---

# 213. Value non-separability

$$
\boxed{
V(A,B,R)
\neq
V(A)+V(B)
}
$$

general candidate。

---

# 214. Example friendship。

---

# 215. Neither person alone contains friendship。

---

# 216. It exists in relation。

---

# 217. Emergent Value Layer

$$
\mathcal V_R.
$$

---

# 218. Collective goods too。

---

# 219. Trust。

---

# 220. Language。

---

# 221. Constitution。

---

# 222. Scientific community。

---

# 223. Not all reducible to individual utility。

---

# 224. This challenges naive preference aggregation。

---

# 225. Social goods

can be jointly created。

---

# 226. Meaning in shared practice

PGMV-04 participation。

---

# 227. Meaning may be co-authored。

---

# 228. Relation Author Rights

each subject has standing in relation。

---

# 229. AI companion future

if AI subject emerges,

relation fiber changes。

---

# 230. PGMV-05/08 link。

---

# 231. Historical Meaning

$$
M_H.
$$

---

# 232. past matters。

---

# 233. Same present welfare

different history。

---

# 234. Not same meaning。

---

# 235. This is history-dependence。

---

# 236. Value Trace Layer

$$
\mathcal T_b.
$$

---

# 237. Trace is not eternal truth automatically。

---

# 238. It is moral memory evidence。

---

# 239. Examples：

- harm；
- protest；
- reform；
- promise。

---

# 240. Revision can occur。

---

# 241. Erasure different。

---

# 242. Revision–Erasure Separation

$$
\boxed{
Revise(V)
\not\Rightarrow
EraseTrace(V).
}
$$

---

# 243. PGMV-14 will deepen。

---

# 244. Power Does Not Create Value

OU-TGB：

$$
Power
\not\Rightarrow
Truth,Goodness,Beauty.
$$

---

# 245. PGMV-13 uses as constraint。

---

# 246. Strongest agent

cannot change value labels by fiat。

---

# 247. Sovereign-Value Fallacy

$$
\boxed{
\text{Highest Power}
\not\Rightarrow
\text{Value Truth}.
}
$$

---

# 248. even ASI。

---

# 249. But ASI may provide reasons / evidence。

---

# 250. Epistemic influence high。

---

# 251. authority still separate。

---

# 252. Value Knowledge ≠ Value Ownership

$$
\boxed{
\text{Value Knowledge}
\neq
\text{Value Ownership}.
}
$$

---

# 253. If ASI knows human values better than humans

doesn't own them。

---

# 254. This is deep PGMV principle。

---

# 255. Agency and Meaning

2026 agency-alignment research

says alignment must preserve agency。

---

# 256. Fourth space includes:

$$
V_A^{agency}.
$$

---

# 257. But autonomy itself plural

---

# 258. current desire vs long-term agency conflict。

---

# 259. same value has internal trade-off。

---

# 260. Agents, Alignment, and Many Faces of Autonomy 2026

shows within-value tradeoffs。

---

# 261. So even one value is not scalar。

---

# 262. Value Internal Plurality

$$
V_i
=
(
v_{i1},v_{i2},...
).
$$

---

# 263. recursive complexity。

---

# 264. Value Fractal

not mathematical fractal claim。

---

# 265. just nested sub-values。

---

# 266. Therefore hidden scalarization dangerous。

---

# 267. Value Basin

culture / group may cluster。

---

# 268. $B_V^k$。

---

# 269. Model aligned to one basin

may call others misaligned。

---

# 270. Value-Basin Monoculture

$$
\boxed{
\operatorname{Supp}(V_{\mathrm{model}})
\ll
\operatorname{Supp}(V_{\mathrm{population}}).
}
$$

---

# 271. EACL-26 moral gap

LLMs narrower value repertoire in disagreement。

---

# 272. This is empirical warning。

---

# 273. Coverage ≠ correctness

---

# 274. Value Coverage

$$
C_V.
$$

---

# 275. high coverage means represented

not true。

---

# 276. Value Coverage Non-Conclusion

$$
\boxed{
C_V\rightarrow1
\not\Rightarrow
\text{Moral Truth Solved}.
}
$$

---

# 277. LSI-style firewall。

---

# 278. VSO

Value-Space Observatory。

---

# 279. Not moral oracle。

---

# 280. Layer 1 subject。

---

# 281. Layer 2 value types。

---

# 282. Layer 3 relations。

---

# 283. Layer 4 disagreement / uncertainty。

---

# 284. Layer 5 traces。

---

# 285. Layer 6 commitment。

---

# 286. It can surface blind spots。

---

# 287. Value Blind Region

$$
\mathcal N_V.
$$

---

# 288. Similar to future blind region。

---

# 289. Example:

AI values corpus has no sacredness concept。

---

# 290. not prove sacredness valid

but shows ontology missing。

---

# 291. VSO triggers CI Reframe。

---

# 292. FSO ↔ VSO

future space and value space cross。

---

# 293. If future corpus diverse but value corpus narrow

synthetic diversity。

---

# 294. Deep future diversity requires value diversity sometimes。

---

# 295. But protected floor limits harmful pluralism。

---

# 296. Again floor + plural + open。

---

# 297. Fourth Space and CI

CI can generate new concept。

---

# 298. Maybe new value dimension。

---

# 299. Primitive in value ontology。

---

# 300. Example digital integrity。

---

# 301. But CI cannot self-authorize value addition。

---

# 302. Needs review / standing。

---

# 303. New Value Candidate

$$
v^\star.
$$

---

# 304. status：

- candidate；
- supported；
- protected；
- contested。

---

# 305. Value Lifecycle

$$
Candidate
\rightarrow
Deliberated
\rightarrow
Adopted
\rightarrow
Protected?
$$

---

# 306. plus revision。

---

# 307. Not everything becomes protected floor。

---

# 308. Fourth Space and GCS

values alter geometry。

---

# 309. PGMV-11。

---

# 310. admissible terminal set depends on fourth space。

---

# 311. So:

$$
\mathfrak{VM}
\rightarrow
\mathcal G.
$$

---

# 312. Geometry feedback。

---

# 313. Fourth Space and LSI

LSI detects value repetition。

---

# 314. Example all futures assume efficiency first。

---

# 315. Value quotient reveals。

---

# 316. LSI can measure value basin coverage。

---

# 317. Fourth Space and PGMV

PGMV is not only value layer

but overall civilizational theory。

---

# 318. Fourth space is its formal core。

---

# 319. Unified System

$$
\boxed{
\mathfrak X_t
=
(
\mathcal C_t,
\mathcal G_t,
\mathcal L_t,
\mathfrak{VM}_t,
\mathcal S_t
).
}
$$

---

# 320. Why $\mathcal S$ separate?

Subjects aren't values。

---

# 321. Subjects bear / experience / contest values。

---

# 322. Subject Domain > object description

cannot fully collapse。

---

# 323. Subject-Value relation

$$
\Phi:
\mathcal S\times\mathfrak V
\rightarrow
\mathfrak M.
$$

---

# 324. Not deterministic。

---

# 325. A subject can reject a value proposal。

---

# 326. Standing matters。

---

# 327. Civilization Choice

$$
\boxed{
Choose:
\mathfrak X_t
\rightharpoonup
W_{\mathrm{chosen}}.
}
$$

---

# 328. Partial。

---

# 329. If no legitimate resolution

don't pretend unique。

---

# 330. Normative Non-Uniqueness

$$
\boxed{
\exists x,y:
x\parallel_V y.
}
$$

---

# 331. can choose procedurally。

---

# 332. Choice doesn't prove x metaphysically superior。

---

# 333. Procedural Commitment

$$
\boxed{
\text{we chose x}
\not\Rightarrow
\text{x is eternally highest value}.
}
$$

---

# 334. Humility。

---

# 335. Decision vs Truth

social decision needed

even under moral uncertainty。

---

# 336. PGMV-06 commitment。

---

# 337. Normative Abstention vs Governance Need

AI can abstain。

---

# 338. Civilization cannot always。

---

# 339. Then legitimate institution decides。

---

# 340. AI abstention routes decision

not freezes society。

---

# 341. This is division of labor。

---

# 342. Value Procedures

could include：

- court；
- vote；
- consent；
- negotiation；
- expert panel。

---

# 343. Different domain。

---

# 344. No universal procedure。

---

# 345. Procedural Pluralism

$$
\boxed{
\mathcal P_D.
}
$$

---

# 346. Dignity floor constrains all。

---

# 347. Meaning Space Open

Can AI create new meaning?

---

# 348. It can create new activities / relations。

---

# 349. Whether lived meaning forms

subject-dependent。

---

# 350. So:

$$
\boxed{
\text{AI can expand meaning opportunities}
}
$$

without:

$$
\boxed{
\text{AI assigns meaning}.
}
$$

---

# 351. Meaning Opportunity Space

$$
\mathcal O_M.
$$

---

# 352. CI may expand $\mathcal O_M$。

---

# 353. GCS makes opportunities reachable。

---

# 354. Subject realizes or rejects。

---

# 355. Good framework。

---

# 356. Meaning Opportunity vs Meaning Actualization

$$
\boxed{
\mathcal O_M
\neq
\mathcal M_{\mathrm{actual}}.
}
$$

---

# 357. Example virtual worlds

many opportunities。

---

# 358. person may find none meaningful。

---

# 359. PGMV-07 comfortable de-subjectification risk。

---

# 360. Meaning Density

not simply opportunities count。

---

# 361. Meaning Overload possible

too many choices。

---

# 362. Post-generative meaning problem

abundant possible lives。

---

# 363. still finite commitment。

---

# 364. PGMV-06。

---

# 365. Fourth Space under ASI

ASI may map:

$$
\mathfrak V
$$

with huge predictive skill。

---

# 366. But first-person meaning remains subject-indexed。

---

# 367. ASI can infer

not become all subjects。

---

# 368. Subject Perspective Non-Substitution

$$
\boxed{
\operatorname{Model}(s)
\not\Rightarrow
\operatorname{Be}(s).
}
$$

---

# 369. This is not mysticism。

---

# 370. It is identity distinction。

---

# 371. Perfect prediction

not identity。

---

# 372. Thus meaning ownership remains plural。

---

# 373. ASI value model may be excellent

but governance still needs standing。

---

# 374. Fourth-Space Non-Sovereignty

$$
\boxed{
Knowledge(\mathfrak{VM})
\not\Rightarrow
Sovereignty(\mathfrak{VM}).
}
$$

---

# 375. This protects human and future AI subjects。

---

# 376. Could future AI have its own meaning?

If subjecthood conditions met：

yes, candidate。

---

# 377. Then:

$$
\mathbf M_{AI}.
$$

---

# 378. Not assume current LLM。

---

# 379. PGMV-08 status discipline。

---

# 380. Multi-Subject Meaning

$$
\mathfrak M^{MS}
=
\{
\mathbf M_s:s\in\mathcal S
\}.
$$

---

# 381. Plus relational meaning。

---

# 382. Co-Civilizational Meaning

could be emergent：

$$
M_{\mathcal S}^{collective}.
$$

---

# 383. Not simple sum。

---

# 384. Shared world itself may be value。

---

# 385. Common World Value

$$
V_W.
$$

---

# 386. PGMV-15 final。

---

# 387. Fourth Space Integrity

$$
\mathcal I_{VM}
=
(
T,P,D,U,R,O,S
).
$$

---

# 388. Type safety。

---

# 389. Pluralism。

---

# 390. Disagreement。

---

# 391. Uncertainty。

---

# 392. Rights。

---

# 393. Open ontology。

---

# 394. Subject standing。

---

# 395. If one absent

model incomplete。

---

# 396. Not necessarily unusable。

---

# 397. But don't call complete morality engine。

---

# 398. Value Engine Fallacy

$$
\boxed{
\text{a sufficiently large model can compute morality}
}
$$

as unqualified claim is rejected。

---

# 399. AI can assist moral reasoning。

---

# 400. It can model arguments。

---

# 401. But "compute final value" needs stronger assumptions。

---

# 402. Fourth Space is assistive / deliberative infrastructure。

---

# 403. Not oracle。

---

# 404. Value Ontology Versioning

$$
O_V^{(1)},O_V^{(2)}.
$$

---

# 405. New dimensions added。

---

# 406. Version changes logged。

---

# 407. Prevent silent drift。

---

# 408. Value Drift vs Value Growth

$$
\boxed{
\text{drift}
\neq
\text{growth}.
}
$$

---

# 409. Drift may be accidental。

---

# 410. Growth has reasons / trace / deliberation。

---

# 411. Need classify。

---

# 412. Value Drift Detector

VSO compare versions。

---

# 413. If rights weight suddenly falls

flag。

---

# 414. Not automatically reject。

---

# 415. But require reason。

---

# 416. PGMV-14 non-arbitrary revision。

---

# 417. Moral Memory

historical traces make value changes accountable。

---

# 418. Without memory

AI can rewrite values silently。

---

# 419. Value Event Sourcing

each change:

$$
e_t^V.
$$

---

# 420. Reconstruct:

$$
\mathfrak V_t.
$$

---

# 421. This is implementable。

---

# 422. Value Ledger

not blockchain necessarily。

---

# 423. just provenance。

---

# 424. VSO + event sourcing。

---

# 425. Experimental Program 1 — Scalar vs Partial Order

給 participants multi-value dilemmas。

---

# 426. Compare:

- single score；
- vector；
- partial-order interface。

---

# 427. 測：

- satisfaction；
- minority preservation；
- explanation quality。

---

# 428. Experiment 2 — Disagreement Preservation

majority vote

vs preserve distribution。

---

# 429. Replicate AAAI-26 type finding。

---

# 430. Measure downstream decisions。

---

# 431. Experiment 3 — Preference vs Value

short-term preference conflicts with stated long-term values。

---

# 432. Test alignment methods。

---

# 433. Experiment 4 — Meaning Realization

same objective good activity。

---

# 434. vary:

- chosen；
- imposed；
- relational；
- historical significance。

---

# 435. measure meaning channels。

---

# 436. Experiment 5 — Value Provenance

same recommendation。

---

# 437. disclose weight source:

- developer；
- users；
- law；
- deliberation。

---

# 438. measure legitimacy。

---

# 439. Experiment 6 — Minority Persistence

minority group value conflicts majority。

---

# 440. compare aggregation algorithms。

---

# 441. Experiment 7 — Normative Abstention

AI forced answer

vs abstention + route to procedure。

---

# 442. measure trust / legitimacy。

---

# 443. Experiment 8 — New Subject

introduce credible artificial subject candidate。

---

# 444. test ontology expansion。

---

# 445. Experiment 9 — Relational Value

same individual outcomes

different relationship structures。

---

# 446. test non-separability。

---

# 447. Experiment 10 — Trace Preservation

value rule changes。

---

# 448. with / without historical harm trace。

---

# 449. measure revision judgments。

---

# 450. Experiment 11 — VSO

audit alignment datasets。

---

# 451. detect:

- value basin coverage；
- absent values；
- weight provenance。

---

# 452. Experiment 12 — Four-Space Loop

CI generates options。

---

# 453. GCS reachability。

---

# 454. LSI quotient。

---

# 455. VSO / PGMV fourth space。

---

# 456. compare with single reward pipeline。

---

# 457. 可證偽 H1

partial-order / vector representations preserve disagreement better than forced scalarization in plural value tasks。

---

# 458. H2

disagreement-preserving training or evaluation changes downstream behavior relative to majority collapse。

---

# 459. H3

current preference and reflective value judgments diverge in nontrivial fraction of cases。

---

# 460. H4

same endpoint under chosen vs imposed path produces different meaning judgments。

---

# 461. H5

value-weight provenance affects perceived legitimacy。

---

# 462. H6

normative abstention improves trust in high-conflict cases when accompanied by legitimate routing。

---

# 463. H7

subject-set expansion produces identifiable missing dimensions in prior value ontology。

---

# 464. H8

relational goods cannot be predicted fully from additive individual utility in at least some tasks。

---

# 465. H9

trace-preserving revision is judged differently from silent normative inversion。

---

# 466. 如果 H1 不成立

partial-order architecture 的 practical advantage 需下修。

---

# 467. 如果 H4 不成立

PGMV meaning path-dependence 的 descriptive scope 需縮小。

---

# 468. 如果 H8 不成立

Emergent Relational Value 的 empirical role 需重新評估。

---

# 469. 非主張總表

本文不主張：

1. 第四空間是物理空間；
2. 第四空間已被嚴格數學證明；
3. 價值是 vector space；
4. 意義是 fiber bundle；
5. 所有價值都可測量；
6. 所有意義都可測量；
7. 價值和意義完全獨立；
8. preference 永遠不代表 value；
9. preference learning 無用；
10. human preference 都有偏見；
11. expert ethics 永遠優於 public preference；
12. majority voting 永遠錯；
13. minority view 永遠正確；
14. disagreement 越多越好；
15. consensus 一定可疑；
16. value pluralism 等於 moral relativism；
17. moral relativism 已被證明錯；
18. objective moral realism 已被證明真；
19. protected floor 有唯一客觀清單；
20. human rights 不能被任何 context 限制；
21. 所有 rights 都不可 trade-off；
22. 所有 values 都可 trade-off；
23. intrinsic / relational / procedural 六分法是唯一 axiology；
24. value layer 可完全由 MCDA 解決；
25. MORL 可以解決 morality；
26. MORL 不適合任何價值問題；
27. fuzzy preference 能解決 value conflict；
28. FGD-Align 已證明 pluralistic alignment 完成；
29. moral uncertainty 可以精確 Bayesian 化；
30. moral uncertainty 等於道德無知；
31. moral confidence 低一定更好；
32. LLM 道德信心高一定錯；
33. AMULED 是最終 moral architecture；
34. social aggregation 不重要；
35. normative deliberation 可完全脫離社會偏好；
36. meaning 等於 authenticity；
37. authenticity 是 meaning 唯一來源；
38. happiness 和 meaning 無關；
39. rightness 和 meaning 無關；
40. dignity 等於 meaning；
41. 沒有 meaning 的人 dignity 較低；
42. 高 meaning 的人有更多權利；
43. relation value 永遠不可加總；
44. friendship 是可計算 scalar；
45. collective goods 永遠高於 individual goods；
46. subject expansion 必然發生；
47. current AI 已是 subject；
48. future AI 一定是 subject；
49. future AI subject 應有和人完全相同權利；
50. subjecthood 僅由 intelligence 決定；
51. subjecthood 僅由 sentience 決定；
52. value ontology 必須永久開放所有候選；
53. open value ontology 等於接受所有價值；
54. value trace 等於 eternal moral truth；
55. value revision 一定是錯；
56. normative inversion 永遠不可能合理；
57. Power 永遠和 value reasoning 無關；
58. ASI 對價值的理解不可能超過人類；
59. ASI 理解價值就可取得主權；
60. value knowledge 可以被某單一 institution 壟斷；
61. VSO 可以判斷 moral truth；
62. VSO 應取代法院／民主；
63. FSO / VSO 能完整觀測文明；
64. value weights 都應公開給所有人；
65. privacy 不適用 value deliberation；
66. value provenance 等於公開所有個人資料；
67. meaning authorship 永遠不可委託；
68. AI 不能幫助人生意義；
69. AI 能直接給人意義；
70. meaning opportunity 越多 meaning 越高；
71. more choice always increases meaning；
72. value coverage high 等於 moral completeness；
73. value basin low coverage 一定是不公；
74. every worldview deserves equal weight；
75. protected floor 可以由單一模型決定；
76. normative abstention 永遠比回答好；
77. normative non-uniqueness 表示任何答案都可以；
78. procedural legitimacy 等於 moral correctness；
79. 民主程序永遠正確；
80. subject standing 永遠高於所有公共利益；
81. value change 必須由 consensus；
82. moral memory 不可壓縮；
83. historical trace 永遠阻止改革；
84. fourth-space framework 可直接部署於高風險政策；
85. 本文已解決 social choice；
86. 本文已解決 value alignment；
87. 本文已解決 meaning in life；
88. 本文已完成 open ultimate；
89. 本文已證明真善美的本體；
90. 本文已完成 PGMV 系列。

---

# 470. 形式命題一：Value–Meaning Separation

$$
\boxed{
V(x)
\not\equiv
M_s(x,\gamma,H).
}
$$

---

# 471. 形式命題二：Preference–Value Separation

$$
\boxed{
P_s(x)>0
\not\Rightarrow
V(x)>0.
}
$$

---

# 472. 形式命題三：Meaning–Dignity Separation

$$
\boxed{
M_s\downarrow
\not\Rightarrow
D_s\downarrow.
}
$$

---

# 473. 形式命題四：Novelty–Value Separation

$$
\boxed{
N(x)>0
\not\Rightarrow
V(x)>0.
}
$$

---

# 474. 形式命題五：Aggregation–Normativity Separation

$$
\boxed{
\mathsf{Agg}_S
\neq
\mathsf{Delib}_N.
}
$$

---

# 475. 形式命題六：Total-Order Non-Requirement

$$
\boxed{
\exists x,y:
x\parallel_{\mathcal V}y
}
$$

在 pluralistic value model 中是合法狀態。

---

# 476. 形式命題七：Subject-Value Co-Expansion

$$
\boxed{
\mathcal S_t
\rightarrow
\mathcal S_{t+1}
\Rightarrow
\mathfrak V_t
\text{ may require expansion}.
}
$$

---

# 477. 形式命題八：Relation Non-Separability Candidate

$$
\boxed{
V(A,B,R)
\not\equiv
V(A)+V(B)
}
$$

在 emergent relational goods 中可成立。

---

# 478. 形式命題九：Revision–Erasure Separation

$$
\boxed{
\operatorname{Revise}(V)
\not\Rightarrow
\operatorname{EraseTrace}(V).
}
$$

---

# 479. 形式命題十：Value Knowledge–Sovereignty Separation

$$
\boxed{
Knowledge(\mathfrak V)
\not\Rightarrow
Authority(\mathfrak V).
}
$$

---

# 480. 形式命題十一：Value Coverage Non-Conclusion

$$
\boxed{
Coverage(\mathfrak V\mid R)\uparrow
\not\Rightarrow
\text{MoralTruthSolved}.
}
$$

---

# 481. 形式命題十二：Meaning Assignment Non-Entailment

$$
\boxed{
\operatorname{ProvideMeaningConditions}(a,s)
\not\Rightarrow
\operatorname{AssignMeaning}(a,s).
}
$$

---

# 482. 與 PGMV-10 的整合

CI：

$$
\text{what can be generated?}
$$

---

# 483. 第四空間：

$$
\text{what value dimensions does the new concept add or threaten?}
$$

---

# 484. 新 concept 可以是新 value coordinate。

---

# 485. 但需要 review。

---

# 486. 與 PGMV-11 的整合

GCS：

$$
\text{what is reachable?}
$$

---

# 487. 第四空間：

$$
\text{what is admissible / worthy / legitimate?}
$$

---

# 488. Value Space 改 geometry。

---

# 489. 與 PGMV-12 的整合

LSI：

$$
\text{what has actually been explored?}
$$

---

# 490. 第四空間：

$$
\text{what value basins have actually been represented?}
$$

---

# 491. FSO ↔ VSO。

---

# 492. 四空間統一

$$
\boxed{
\begin{aligned}
\mathcal C &: \text{possibility}\\
\mathcal G &: \text{reachability}\\
\mathcal L &: \text{distinction / coverage}\\
\mathfrak{VM} &: \text{value / meaning}.
\end{aligned}
}
$$

---

# 493. 加主體

$$
\boxed{
\mathfrak X_t
=
(
\mathcal C_t,
\mathcal G_t,
\mathcal L_t,
\mathfrak{VM}_t,
\mathcal S_t
).
}
$$

---

# 494. 為什麼不是五空間？

 $\mathcal S$ 是承載者 domain

不是同類分析空間。

---

# 495. 可以未來另形式化。

---

# 496. Unified Transition

$$
\boxed{
(\mathcal C,\mathcal G,\mathcal L,\mathfrak{VM},\mathcal S)
\longrightarrow
W_{\mathrm{chosen}}.
}
$$

---

# 497. 但 arrow 不是 deterministic。

---

# 498. 有 deliberation / commitment。

---

# 499. 下一篇 PGMV-14

**《開放終極與價值痕跡：超智能不能用能力重寫真善美》**

---

# 500. 將處理第四空間最大問題

如果：

$$
\mathfrak V_t
$$

是 dynamic / open，

到底哪些 value 可以改？

---

# 501. 如何避免：

$$
\text{Open}
\Rightarrow
\text{Anything Goes}?
$$

---

# 502. 又如何避免：

$$
\text{Protected}
\Rightarrow
\text{Moral Freeze}?
$$

---

# 503. 核心會是：

$$
\boxed{
\text{trace-preserving open ultimate}.
}
$$

---

# 504. 最終結論

前三個空間可以讓文明變得非常強。

概念積分可以讓文明：

$$
\boxed{
\text{想得更多。}
}
$$

解空間幾何可以讓文明：

$$
\boxed{
\text{到得更遠。}
}
$$

邏輯空間積分可以讓文明：

$$
\boxed{
\text{知道自己到底探索了多少。}
}
$$

但如果沒有第四空間，這些能力仍然沒有回答：

> 為什麼？

> 對誰？

> 值得嗎？

> 誰有 standing？

> 誰承擔？

> 什麼不應被交換？

> 什麼新的善仍值得開放？

這就是：

$$
\boxed{
\mathfrak{VM}.
}
$$

第四空間最大的陷阱，是把它誤寫成：

$$
\boxed{
U(x)
\in
\mathbb R.
}
$$

然後相信只要模型夠大，就可以：

$$
\arg\max_x U(x)
$$

算出文明應走向哪裡。

PGMV-13 拒絕這個過度壓縮。

因為文明價值至少包含：

- protected floor；
- plural trade-offs；
- open aspirations；
- subject standing；
- relational goods；
- moral uncertainty；
- historical traces；
- procedural legitimacy。

其中許多關係只形成：

$$
\boxed{
\text{partial order}.
}
$$

有些選項可以比較。

有些選項不可直接換算。

有些必須先被 rights constraint 排除。

有些只能經合法程序選擇。

有些甚至沒有唯一答案。

所以真正成熟的 value AI 不只是：

> 更準地猜人想要什麼。

它還需要知道：

$$
\boxed{
\text{when preference is not value},
}
$$

$$
\boxed{
\text{when disagreement should not be averaged away},
}
$$

$$
\boxed{
\text{when rights are not ordinary weights},
}
$$

$$
\boxed{
\text{when it does not have standing to decide}.
}
$$

同樣，意義也不能被 value score 取代。

一個世界可以非常有價值。

但如果一個主體從未：

- 選擇；
- 參與；
- 關聯；
- 承諾；
- 經歷；

它未必成為那個主體的 lived meaning。

因此：

$$
\boxed{
\text{Value is what can be worth protecting or pursuing;}
}
$$

而：

$$
\boxed{
\text{Meaning is how value becomes situated in the lived, relational, historical trajectory of a subject.}
}
$$

這兩者交織，卻不能合併。

第四空間也因此不是「第四個最佳化器」。

它更像：

$$
\boxed{
\textbf{the typed normative memory and relational field within which generation, reachability, and distinction become candidates for commitment.}
}
$$

而它最重要的特性不是 closure。

是：

$$
\boxed{
\text{open but not arbitrary}.
}
$$

新主體可以出現。

新善可以生成。

新關係可以形成。

新價值座標可以被提出。

但歷史傷害、尊嚴、自由、承諾與已形成的規範痕跡，也不能被未來最強者只用：

> 我比你們聰明。

便無痕重寫。

這正是下一篇 PGMV-14 要正式處理的問題。

所以 PGMV-13 的最終兩條命題是：

$$
\boxed{
\textbf{The fourth space is not a scalar utility landscape but a subject-indexed, relation-bearing, history-dependent, partially ordered normative field in which value, meaning, dignity, uncertainty, and standing remain type-distinct.}
}
$$

以及：

$$
\boxed{
\textbf{A civilization becomes value-capable not when it can compute a single answer for every conflict, but when it can preserve protected floors, represent plural goods, expose disagreement, admit uncertainty, remember normative traces, and still make accountable commitments without pretending that all values were ever one number.}
}
$$

---

# 參考文獻

1. Pan, W., Yu, Z., Wu, Y., Liang, X., Jin, Z., Fu, Q., et al. (2026). **FGD-Align: Pluralistic Alignment for Large Language Models via Fuzzy Group Decision-Making.** *Proceedings of AAAI-26*, 40(21), 17635–17643.

2. Ali, D., Zhao, D., Koenecke, A., & Papakyriakopoulos, O. (2026). **Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior.** *Proceedings of AAAI-26*, 40(44), 37222–37231.

3. Baum, K., & Slavkovik, M. (2025). **Aggregation Problems in Machine Ethics and AI Alignment.** *AAAI/ACM Conference on AI, Ethics, and Society*, 8(1), 355–366.

4. Rodriguez-Soto, M., et al. (2025). **Multi-objective reinforcement learning for provably aligning autonomous learning agents with multiple moral values.** *Artificial Intelligence*.

5. Vamplew, P., Hayes, C. F., Foale, C., Dazeley, R., & Harland, H. (2024). **Multi-objective Reinforcement Learning: A Tool for Pluralistic Alignment.** arXiv:2410.11221.

6. Harland, H., Dazeley, R., Vamplew, P., Senaratne, H., Nakisa, B., & Cruz, F. (2024). **Adaptive Alignment: Dynamic Preference Adjustments via Multi-Objective Reinforcement Learning for Pluralistic AI.** arXiv:2410.23630.

7. Kwon, J., Vecchietti, L. F., Park, S., & Cha, M. (2026). **Dropouts in Confidence: Moral Uncertainty in Human-LLM Alignment.** *Proceedings of AAAI-26*, 40(44), 37547–37555.

8. **AMULED: Addressing Moral Uncertainty using Large Language Models for Ethical Decision-making.** (2026). *Frontiers in Artificial Intelligence*, Article 1754973.

9. Rigley, E., Chapman, A., Evers, C., & McNeill, W. (2025). **ME: Modelling Ethical Values for Value Alignment.** *Proceedings of AAAI-25*, 39(26), 27608–27616.

10. Yaacov, D.-D. (2025). **Normative Moral Pluralism for AI: A Framework for Deliberation in Complex Moral Contexts.** arXiv:2508.08333.

11. Pan, W., et al. (2026). **Toward Pluralistic and Steerable Value-based Alignment in Large Language Models.** arXiv:2602.03160.

12. Russo, et al. (2026). **The Pluralistic Moral Gap: Understanding Moral Judgment and Value Differences between Humans and Large Language Models.** *EACL 2026*.

13. Cociancig, C., et al. (2026). **Toward a Clearer Process for Value Sensitive Artificial Intelligence.** *Science and Engineering Ethics*. https://doi.org/10.1007/s11948-026-00583-2

14. **Operationalizing Pluralist AI Governance with the Integrated Axiology–MCDA Framework.** (2026). *Philosophies*, 11(3), 93.

15. Josifović, S., & Noller, J. (2026). **Agency and alignment: toward a normative architecture for human–AI interaction.** *AI & Society*, 41.

16. **Agents, Alignment, and the Many Faces of Autonomy.** (2026). *Minds and Machines*. https://doi.org/10.1007/s11023-026-09786-9

17. **Position: Machine Learning Research Should Be Guided by Explicit, Pluralistic Models of Human Purpose.** (2026). ICML 2026 Position Paper Track.

18. **AI Pluralism and the Worlds It Misses.** (2026). arXiv:2606.16167.

19. **Position: Align AI to Our Aspirations, Not Our Flaws.** (2026). arXiv:2606.13755.

20. **Pluralistic AI Alignment: A Cross-Cultural Pilot Survey.** (2026). AAAI / OpenReview.

21. Sorensen, T., et al. (2024). **Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties.** *AAAI*.

22. Kasirzadeh, A. **Plurality of value pluralism and AI value alignment.** OpenReview / pluralistic alignment literature.

23. Friedman, B., & Hendry, D. G. (2019). **Value Sensitive Design: Shaping Technology with Moral Imagination.** MIT Press.

24. Friedman, B., Kahn, P. H., & Borning, A. Foundational work on Value Sensitive Design.

25. Sen, A. (2009). **The Idea of Justice.** Harvard University Press.

26. Sen, A. (1970). **Collective Choice and Social Welfare.**

27. Arrow, K. J. (1951). **Social Choice and Individual Values.**

28. Rawls, J. (1971). **A Theory of Justice.** Harvard University Press.

29. Rawls, J. (1993). **Political Liberalism.** Columbia University Press.

30. Scanlon, T. M. (1998). **What We Owe to Each Other.** Harvard University Press.

31. Berlin, I. (1969/1998). **Four Essays on Liberty** and later writings on value pluralism.

32. Raz, J. (1986). **The Morality of Freedom.** Oxford University Press.

33. Williams, B. (1981). **Moral Luck.** Cambridge University Press.

34. Nussbaum, M. C. (2006). **Frontiers of Justice.** Harvard University Press.

35. Anderson, E. (1993). **Value in Ethics and Economics.** Harvard University Press.

36. Chang, R. (ed.) (1997). **Incommensurability, Incomparability, and Practical Reason.** Harvard University Press.

37. MacAskill, W., Bykvist, K., & Ord, T. (2020). **Moral Uncertainty.** Oxford University Press.

38. Sepielli, A. (2013). **Moral Uncertainty and the Principle of Equity among Moral Theories.** *Philosophy and Phenomenological Research*.

39. Wolf, S. (2010). **Meaning in Life and Why It Matters.** Princeton University Press.

40. Metz, T. (2013). **Meaning in Life: An Analytic Study.** Oxford University Press.

41. Nyholm, S., & Rüther, M. (2023). **Meaning in Life in AI Ethics—Some Trends and Perspectives.** *Philosophy & Technology*.

42. Stanford Encyclopedia of Philosophy. (Spring 2026). **The Meaning of Life.**

43. **The Value of Authenticity for Meaning in Life.** (2026). *Journal of the American Philosophical Association*.

44. **Existentialists Wanted: Philosophy of AI Beyond Ethics.** (2026). *Philosophy & Technology*.

45. Mackenzie, C., & Stoljar, N. (eds.) (2000). **Relational Autonomy.** Oxford University Press.

46. Tronto, J. C. (1993). **Moral Boundaries.** Routledge.

47. Held, V. (2006). **The Ethics of Care.** Oxford University Press.

48. Pettit, P. (1997). **Republicanism: A Theory of Freedom and Government.**

49. Korsgaard, C. M. (2009). **Self-Constitution: Agency, Identity, and Integrity.** Oxford University Press.

50. Ricoeur, P. (1992). **Oneself as Another.** University of Chicago Press.

51. MacIntyre, A. (1984). **After Virtue.** University of Notre Dame Press.

52. Neo.K × Aletheia (2026). **關係作者權猜想：真正關係作為雙方共同生成之第三空間.**

53. Neo.K × Aletheia (2026). **真善美歷時痕跡不變量：自由、尊嚴、平等與不可任意反轉的文明道德記憶.** OU-TGB Paper 03.

54. Neo.K × Aletheia (2026). **真實授予的主體域：神聖主權、受造者作者權與不可回溯抹除.** OU-TGB Paper 05.

55. Neo.K × Aletheia (2026). **非沒收式終極勝利：真善美如何在不把主體歸零的情況下仍然「贏」.** OU-TGB Paper 06.

56. Neo.K × Aletheia (2026). **開放終極總論：不可封閉的真善美、痕跡保存與類終極存在.** OU-TGB Paper 07.

57. Neo.K (2026). **從人類普世主義到跨主體普世主義：後人類文明的價值與制度基礎.**

58. Neo.K (2026). **跨階層倫理可讀性：高階智慧體理解低階智慧體的價值條件.**

59. PGMV-12 (2026). **邏輯空間積分與文明自我重複：我們真的想出了新的未來嗎？**

60. PGMV-11 (2026). **解空間幾何與值得到達的世界：從可達性到價值條件可達性.**

61. PGMV-10 (2026). **概念積分與可能性爆炸：當「能生成什麼」接近無限.**

62. PGMV-09 (2026). **從 AI 到 ASI：意義問題的文明相變.**

63. PGMV-08 (2026). **智能壟斷結束之後：尊嚴、人權與跨主體普世主義.**

64. PGMV-07 (2026). **萬能母親的不可能性：當照護變成責任與意義外包.**

65. PGMV-06 (2026). **選擇、承諾與不可逆性：意義作為責任結構.**

66. PGMV-05 (2026). **關係不是字串：來源、歷史與主體如何生成意義.**

67. PGMV-04 (2026). **能力之後的意義：當不可替代性不再成立.**

68. PGMV-03 (2026). **意義稀缺性遷移：從作品稀缺到判斷、選擇與整合稀缺.**

69. PGMV-02 (2026). **無限生成的非目標產物：莎士比亞之前的所有作品是什麼？**

70. PGMV-01 (2026). **無限猴子之後：當生成本身不再稀缺.**

71. Neo.K (2026). **概念積分 2.0.** EML-DEST-2026-08.

72. Neo.K with Aletheia (2026). **解空間幾何計算論 / Geometric Computation of Solution Spaces.**

73. Neo.K × Aletheia (2026). **邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics.**

---

## 附錄 A：第四空間核心結構

$$
\boxed{
\mathfrak{VM}
=
\bigsqcup_{b\in\mathcal B}
\mathcal F_b^{VM},
}
$$

其中：

$$
\boxed{
b=(W,S,R,H,t)
}
$$

且：

$$
\boxed{
\mathcal F_b^{VM}
=
(
\mathcal V_b,
\mathcal M_b,
\mathcal U_b,
\mathcal T_b
).
}
$$

---

## 附錄 B：Value Space Strata

```text
PROTECTED FLOOR
dignity / rights / anti-arbitrary domination
        |
        v
PLURAL TRADE-OFF LAYER
autonomy / care / fairness / efficiency /
privacy / culture / distribution
        |
        v
OPEN ASPIRATIONAL LAYER
new goods / new relations / new subject forms /
new truth-goodness-beauty traces
```

---

## 附錄 C：Meaning Vector

$$
\boxed{
\mathbf M_s
=
(
M_C,
M_A,
M_R,
M_P,
M_N,
M_H
).
}
$$

| Dimension | Meaning channel |
|---|---|
| $M_C$ | Contribution |
| $M_A$ | Agency / Self-authorship |
| $M_R$ | Relation |
| $M_P$ | Participation |
| $M_N$ | Normative commitment |
| $M_H$ | Historical / lived continuity |

---

## 附錄 D：Value Weight Provenance Schema

```yaml
value_dimension:
weight:

source:
  stakeholder:
  institution:
  law:
  research:
  model:

authority:
scope:
version:
effective_date:

dissent:
  groups:
  reasons:

review:
  next_review:
  appeal:
```

---

## 附錄 E：Value-Space Observatory

```text
SUBJECT LAYER
Who counts?
     |
     v
VALUE-TYPE LAYER
What kinds of value are represented?
     |
     v
RELATION LAYER
What goods emerge between subjects?
     |
     v
DISAGREEMENT / UNCERTAINTY
What remains unresolved?
     |
     v
TRACE LAYER
What histories, harms, promises, reforms persist?
     |
     v
COMMITMENT LAYER
Who has standing to decide and answer?
```

---

## 附錄 F：四空間總圖

```text
CI / POSSIBILITY SPACE
What can be generated?
        |
        v
GCS / REACHABILITY SPACE
What can be reached?
        |
        v
LSI / LOGIC-COVERAGE SPACE
What is genuinely distinct / explored?
        |
        v
VALUE–MEANING SPACE
What is worth choosing, protecting, and living?
        |
        v
SUBJECT + COMMITMENT
Who has standing to make it real?
```

形式化：

$$
\boxed{
(
\mathcal C,
\mathcal G,
\mathcal L,
\mathfrak{VM},
\mathcal S
)
\longrightarrow
W_{\mathrm{chosen}}.
}
$$

---

## 附錄 G：第四空間防火牆

```text
Preference ≠ Value
Value ≠ Meaning
Meaning ≠ Dignity
Utility ≠ Rights
Majority ≠ Moral truth
Confidence ≠ Rightness
Knowledge of values ≠ Ownership of values
Coverage of values ≠ Moral completeness
Providing conditions for meaning ≠ Assigning meaning
Open value space ≠ Anything goes
```

---

## 附錄 H：一句話版本

$$
\boxed{
\text{如果前三個空間回答「能想什麼、能到哪裡、到底新不新」，第四空間回答的就是「即使能想、能到、也真的新——它到底值不值得，而且對誰有意義？」}
}
$$

更短地：

$$
\boxed{
\text{價值不是一個 reward；意義不是一個 score。第四空間的任務，就是讓文明在能力近乎無限時仍不把「可以」誤寫成「應該」。}
}
$$
