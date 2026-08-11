# HSNRD II：投影、資訊失真與高階代理
## ——從 Microstate 到 Macrostate 的可逆性、充分性與因果抽象

**系列：**《高階集合欲求》  
**篇次：** 08 / 10  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-07  

### 摘要

HSNRD I 已建立階梯集合、typed set-node、incidence、relation bundle 與 multilayer graph 的靜態本體。然而，只要模型中存在由低階節點構成的高階節點，就必須回答一個更基本的數學問題：低階世界究竟如何投影為高階世界？投影丟失了哪些資訊？什麼資訊是無關細節，什麼資訊卻是代理、決策與因果分析不可丟失的結構？

本文將低階狀態表示為隨機變量 $X$ ，高階表示為：

$$
\boxed{
Z=\pi(X)
}
$$

其中 $\pi$ 是 micro-to-macro projection / coarse-graining。對離散確定性投影，本文以：

$$
\boxed{
H(X\mid Z)
}
$$

衡量由高階表示留下的微觀重建歧義，並強調這不是物理世界「資訊被銷毀」的普遍命題，而是相對於觀察者與投影映射的表徵資訊損失。若研究目標為 $Y$ ，則更適合用：

$$
\boxed{
\Delta I_Y
=
I(X;Y)-I(Z;Y)
}
$$

衡量 projection 對任務相關資訊的損失。依 data-processing inequality，若 $Y\rightarrow X\rightarrow Z$ 形成 Markov chain，則：

$$
I(Z;Y)\le I(X;Y).
$$

若等號成立， $Z$ 對 $Y$ 可視為充分表示；因此 HSNRD 不應追求「保留全部微觀資訊」，而應尋找對研究問題足夠的宏觀表示。

本文進一步處理：（1）非單射投影與 multiple realization；（2）線性 incidence projection 與 pseudoinverse reconstruction；（3）information bottleneck 式的壓縮—任務資訊權衡；（4）Markov lumpability 與宏觀動力封閉；（5）causal abstraction 下的 intervention consistency；（6）高階代理所需的 agency-sufficient projection。本文亦說明 Hoel 式 causal emergence 可用來比較不同尺度的有效因果資訊，但不應被直接解讀為宏觀層產生了脫離微觀基底的新本體因果力。

本文最終提出：

$$
\boxed{
GoodMacrostate
\neq
MaximallyDetailedMacrostate
}
$$

而應是：

$$
\boxed{
GoodMacrostate
=
Compression
+
TaskSufficiency
+
DynamicalClosure
+
InterventionalFidelity.
}
$$

這構成 HSNRD 從靜態階梯集合進入高階代理與動力模型的關鍵橋梁。

**關鍵詞：** HSNRD、coarse-graining、projection、conditional entropy、information bottleneck、lumpability、causal abstraction、multiple realization、高階代理

---

## 1. 問題：高階世界是怎麼「看見」低階世界的？

HSNRD I 定義了：

$$
X_i^{(k,\tau)}
$$

以及多階集合：

$$
\mathcal L_0
\rightarrow
\mathcal L_1
\rightarrow
\cdots
\rightarrow
\mathcal L_K.
$$

但只要：

$$
X^{(k+1)}
$$

由：

$$
\{X_i^{(k)}\}
$$

構成，

就出現一個不可迴避的問題：

> 高階狀態是否只是低階全部狀態的完整複製？

如果是，

那麼：

$$
X^{(k+1)}
$$

沒有任何壓縮作用。

如果不是，

就必須存在：

$$
\boxed{
\pi_k:
\Omega_k
\rightarrow
\Omega_{k+1}
}
$$

將低階狀態空間映射到高階狀態空間。

因此：

$$
\boxed{
Macrostate
=
Projection(Microstate).
}
$$

HSNRD 的第二個數學核心就是 projection。

---

## 2. 確定性投影

令低階隨機狀態：

$$
X\in\Omega.
$$

高階狀態：

$$
Z\in\mathcal Z.
$$

若：

$$
\boxed{
Z=\pi(X),
}
$$

則 $\pi$ 為 deterministic coarse-graining。

例如三個人的二元偏好：

$$
X=(x_1,x_2,x_3)
\in
\{0,1\}^3.
$$

可以投影為：

### 多數決

$$
Z_M
=
\mathbf 1
\left[
x_1+x_2+x_3\ge2
\right].
$$

### 支持人數

$$
Z_C
=
x_1+x_2+x_3.
$$

兩者都是合法 projection，

但保留的資訊量不同。

---

## 3. 投影通常不是單射

對大多數 coarse-graining：

$$
\boxed{
\pi
\text{ is not injective}.
}
$$

也就是存在：

$$
x\neq x'
$$

使：

$$
\pi(x)=\pi(x').
$$

這表示同一高階狀態可能具有多個低階 realization。

因此：

$$
\boxed{
NonInjectiveProjection
\Longleftrightarrow
MacrostateAmbiguity.
}
$$

同時也提供：

$$
\boxed{
MultipleRealization
}
$$

的自然數學表示。

如果：

$$
\pi^{-1}(z)
$$

包含大量 microstates，

則：

$$
z
$$

是一個 coarse-grained equivalence class。

---

## 4. Macrostate 作為等價類

投影 $\pi$ 自然誘導等價關係：

$$
x\sim_\pi x'
\iff
\pi(x)=\pi(x').
$$

因此：

$$
\boxed{
\Omega/\sim_\pi
}
$$

可以視為 macrostate space。

每個：

$$
[z]_\pi
=
\pi^{-1}(z)
$$

包含被高階描述視為「同一狀態」的 microstates。

這裡的重要問題不再是：

> 低階狀態真的一樣嗎？

而是：

> 對目前研究問題，它們是否可以被合法視為等價？

所以 coarse-graining 是：

$$
\boxed{
QuestionRelativeEquivalence.
}
$$

---

## 5. 離散投影的資訊損失

若 $X$ 為離散隨機變量，且：

$$
Z=\pi(X)
$$

為 deterministic function，

則：

$$
H(Z\mid X)=0.
$$

因此：

$$
\boxed{
H(X)
=
H(Z)
+
H(X\mid Z).
}
$$

所以可以把：

$$
\boxed{
\mathcal I_\pi
=
H(X\mid Z)
}
$$

稱為 projection ambiguity / reconstruction uncertainty。

它回答：

> 已知 macrostate $Z$ 後，仍有多少關於原 microstate $X$ 的不確定性？

---

## 6. 這不是「宇宙資訊被消滅」

這一點必須嚴格限制。

$$
H(X\mid Z)>0
$$

表示：

> 從投影後表徵 $Z$ 無法唯一恢復 $X$ 。

它不是：

> 物理宇宙真的銷毀了資訊。

因此：

$$
\boxed{
RepresentationalInformationLoss
\neq
PhysicalInformationDestruction.
}
$$

HSNRD 處理的是：

- observer description；
- model representation；
- coarse-grained state；

中的資訊損失。

不對一般物理資訊守恆作額外主張。

---

## 7. 三個公平二元成員的 toy example

令：

$$
X=(X_1,X_2,X_3)
$$

三者 independent Bernoulli $(1/2)$ 。

則：

$$
H(X)=3\text{ bits}.
$$

### 投影一：只保留多數

$$
Z_M
=
Majority(X).
$$

由對稱性：

$$
P(Z_M=0)=P(Z_M=1)=1/2.
$$

因此：

$$
H(Z_M)=1.
$$

所以：

$$
\boxed{
H(X\mid Z_M)
=
3-1
=
2\text{ bits}.
}
$$

---

## 8. 支持人數保留更多資訊

若：

$$
Z_C
=
X_1+X_2+X_3,
$$

則：

$$
P(Z_C=0,1,2,3)
=
\left(
\frac18,
\frac38,
\frac38,
\frac18
\right).
$$

因此：

$$
H(Z_C)
\approx
1.811
\text{ bits}.
$$

所以：

$$
\boxed{
H(X\mid Z_C)
\approx
1.189
\text{ bits}.
}
$$

比較：

$$
2
>
1.189.
$$

支持人數比單純 majority label 保留更多 micro-information。

---

## 9. 再加入一個成員身份

若 projection 為：

$$
Z_{C1}
=
(Z_C,X_1),
$$

則可以得到：

$$
H(Z_{C1})
=
2.5
\text{ bits}.
$$

因此：

$$
\boxed{
H(X\mid Z_{C1})
=
0.5
\text{ bits}.
}
$$

所以：

$$
Majority
\rightarrow
Count
\rightarrow
Count+MemberIdentity
$$

形成逐步更豐富的 projection。

但：

$$
\boxed{
MoreInformation
\not\Rightarrow
BetterMacroModel.
}
$$

因為宏觀模型的目的不是永遠最大化 $H(Z)$ 。

---

## 10. 為什麼不能追求「零資訊損失」？

如果選：

$$
Z=X,
$$

則：

$$
H(X\mid Z)=0.
$$

看似最好。

但這等於：

$$
\boxed{
NoCompression.
}
$$

高階層失去存在意義。

所以 HSNRD 的目標不是：

$$
\min H(X\mid Z)
$$

單獨最小化。

而是：

$$
\boxed{
CompressIrrelevantDetail
}
$$

同時：

$$
\boxed{
PreserveRelevantStructure.
}
$$

這正是 information bottleneck 的基本精神。

---

## 11. Relevant Information

假設研究問題不是「恢復完整 microstate」，

而是預測：

$$
Y.
$$

例如：

- 下一期政策；
- 組織是否解體；
- 公司是否併購；
- 國家是否進入戰爭。

此時真正重要的是：

$$
I(X;Y).
$$

投影後：

$$
I(Z;Y).
$$

如果：

$$
Y
\rightarrow
X
\rightarrow
Z
$$

構成 Markov chain，

由 data-processing inequality：

$$
\boxed{
I(Z;Y)
\le
I(X;Y).
}
$$

投影不能憑空創造關於 $Y$ 的資訊。

---

## 12. Task-Relevant Information Loss

因此定義：

$$
\boxed{
\Delta I_Y(\pi)
=
I(X;Y)-I(Z;Y).
}
$$

如果：

$$
\Delta I_Y
=
0,
$$

則：

$$
Z
$$

對 $Y$ 保留了 $X$ 中全部相關資訊。

這比：

$$
H(X\mid Z)
$$

更適合回答：

> 這個 macrostate 對研究任務夠不夠？

因為可能：

$$
H(X\mid Z)\gg0
$$

但：

$$
\Delta I_Y=0.
$$

也就是大量微觀細節被丟掉，

卻沒有丟掉任何任務相關資訊。

---

## 13. Sufficient Macrostate

如果：

$$
I(Z;Y)=I(X;Y),
$$

則對該推論任務可把 $Z$ 理解成某種 sufficient representation。

因此：

$$
\boxed{
TaskSufficientMacrostate
}
$$

不需要保留：

$$
AllMicroInformation.
$$

它只需要保留：

$$
AllRelevantInformationFor(Y).
$$

這是 HSNRD 投影方法論最重要的轉折：

$$
\boxed{
GoodProjection
\neq
LosslessProjection.
}
$$

而是：

$$
\boxed{
GoodProjection
=
RelevantInformationPreservingProjection.
}
$$

---

## 14. Information Bottleneck 式目標

Tishby、Pereira 與 Bialek 的 Information Bottleneck 將問題表達為：

> 壓縮 $X$ ，同時盡可能保留與 $Y$ 有關的資訊。

HSNRD 可借用同樣思想：

$$
\boxed{
\min_{\pi}
\quad
I(X;Z)
-
\beta I(Z;Y).
}
$$

或者等價地理解為：

- 壓縮：降低 $I(X;Z)$ ；
- 任務保留：提高 $I(Z;Y)$ 。

在 HSNRD 中：

$$
Y
$$

不必是普通分類標籤。

它可以是：

- future state；
- intervention response；
- agency decision；
- rewrite event；
- survival / dissolution outcome。

---

## 15. Projection 必須是 Query-Relative

因此每一個 projection 應標註：

$$
\boxed{
\pi^{(\mathcal Q)}.
}
$$

例如：

### 對選舉結果

$$
\pi^{Election}
$$

可能只需要保留：

- voter blocs；
- turnout；
- preference ranking。

### 對暴力風險

$$
\pi^{Conflict}
$$

可能需要：

- coercive capacity；
- faction structure；
- escalation relations。

### 對制度代理性

$$
\pi^{Agency}
$$

需要：

- memory；
- decision closure；
- action channels；
- feedback。

因此：

$$
\boxed{
OneProjectionDoesNotFitAllQueries.
}
$$

---

## 16. 線性 incidence projection

HSNRD I 中有：

$$
P
$$

表示 incidence / aggregation。

在線性近似下：

$$
x\in\mathbb R^n
$$

為 microstate，

則：

$$
\boxed{
z
=
Px
}
$$

是最簡單 projection。

例如：

$$
P
$$

可以：

- sum；
- average；
- weighted aggregate。

---

## 17. 線性重建誤差

若：

$$
P^+
$$

為 Moore–Penrose pseudoinverse，

可以重建：

$$
\hat x
=
P^+Px.
$$

定義：

$$
\boxed{
D_\pi(x)
=
\|x-P^+Px\|_2.
}
$$

這測量：

> 在指定 Euclidean linear model 中，投影後再做最小平方重建所留下的誤差。

但它不是普遍資訊損失。

因此：

$$
\boxed{
LinearReconstructionError
\neq
ShannonInformationLoss.
}
$$

兩者可以並用，但不能混稱同一量。

---

## 18. 非線性 projection

真實 HSNRD projection 通常：

$$
\boxed{
z
=
\pi(x;G,\tau,\Gamma)
}
$$

可能依賴：

- graph topology $G$ ；
- node types $\tau$ ；
- institutional rules $\Gamma$ 。

例如「國家政策」不是公民 preference vector 的簡單平均。

可能經過：

$$
Citizens
\rightarrow
Election
\rightarrow
Legislature
\rightarrow
Executive
\rightarrow
Policy.
$$

因此：

$$
\boxed{
MacroProjection
}
$$

本身可能是一個組織 operator。

---

## 19. 投影本身可以隨時間改變

如果制度改變：

- 選舉規則；
- 代表權；
- 公司治理；
- 聚合程序；

則：

$$
\boxed{
\pi_t
}
$$

也會改變。

因此：

$$
Z_t
=
\pi_t(X_t).
$$

甚至：

$$
\boxed{
ProjectionDynamics
}
$$

本身就是制度動力的一部分。

同一個 microstate：

$$
X
$$

在不同制度下可能得到：

$$
\pi_1(X)
\neq
\pi_2(X).
$$

所以：

$$
\boxed{
MacroReality
=
Microstate
+
ProjectionRule.
}
$$

---

## 20. 投影規則具有制度性

這提供一個重要社會科學含義：

> 誰能被算進「人民」？

> 哪些票被加權？

> 哪些公司行為算公司正式決策？

本質上都是：

$$
\boxed{
ProjectionDesign.
}
$$

因此政治與制度不是只改變：

$$
X.
$$

也在改變：

$$
\pi.
$$

這會改變高階「想要什麼」的形成方式。

---

## 21. Macrostate 不一定有封閉動力

假設 microstate：

$$
X_t
$$

是一階 Markov：

$$
P(X_{t+1}\mid X_t).
$$

令：

$$
Z_t=\pi(X_t).
$$

不能因此推出：

$$
\boxed{
P(Z_{t+1}\mid Z_t)
}
$$

足以描述 macro dynamics。

可能需要：

$$
P(
Z_{t+1}
\mid
Z_t,Z_{t-1},\ldots
).
$$

也就是：

$$
\boxed{
MarkovMicro
\not\Rightarrow
MarkovMacro.
}
$$

這是一條非常重要的 HSNRD 限制。

---

## 22. Lumpability

Markov-chain lumpability 正是研究：

> 哪些 state partition / projection 可以產生封閉的宏觀 Markov process？

若 micro state blocks 為：

$$
C_a,C_b,
$$

強 lumpability 的典型條件要求：

對所有：

$$
x,x'\in C_a,
$$

都有：

$$
\boxed{
\sum_{y\in C_b}
P(x,y)
=
\sum_{y\in C_b}
P(x',y)
}
$$

對所有 $b$ 成立。

其意義是：

> 只知道 macro-block $C_a$ 就足以知道下一 macro-block 的轉移機率，而不需要知道 block 內具體是哪個 microstate。

---

## 23. Dynamical Closure

因此可定義：

$$
\boxed{
C_D(\pi)
}
$$

表示 projection 的 dynamical closure。

若：

$$
C_D\approx1,
$$

macrostate dynamics 可以較封閉地建模。

若：

$$
C_D\ll1,
$$

則：

$$
Z_t
$$

只是描述性 coarse-graining，

卻不是良好的 autonomous dynamical state。

因此：

$$
\boxed{
DescriptiveMacrostate
\neq
DynamicalMacrostate.
}
$$

---

## 24. 高階代理尤其需要 dynamical closure

如果我們說：

> 公司是一個 agent。

那麼只知道：

$$
CompanyState_t
$$

應至少對：

$$
CompanyState_{t+1}
$$

有相當預測能力。

如果所有未來行為都必須重新讀取全部：

$$
Microstate_t
$$

才能判斷，

則：

$$
CompanyState
$$

的 dynamical autonomy 很弱。

所以高階代理需要：

$$
\boxed{
Projection
+
Memory
+
DynamicalClosure.
}
$$

---

## 25. Projection 與 Organizational Memory

但即使即時 macrostate：

$$
Z_t
$$

不具 Markov closure，

也可能透過擴充 memory state：

$$
M_t
$$

得到：

$$
\tilde Z_t
=
(Z_t,M_t)
$$

使：

$$
P(
\tilde Z_{t+1}
\mid
\tilde Z_t
)
$$

更接近封閉。

所以：

$$
\boxed{
Memory
}
$$

可以被理解成：

> 為高階代理恢復 dynamical sufficiency 的一種 state augmentation。

這使前面文字理論中的 institutional memory 取得明確數學功能。

---

## 26. More State Can Restore Closure

如果：

$$
Z_t
$$

過度粗糙，

則可以引入：

$$
Z_t^*
=
(
Z_t,
HistoryFeature_t
).
$$

使：

$$
\boxed{
H(
Z_{t+1}
\mid
Z_t^*
)
<
H(
Z_{t+1}
\mid
Z_t
).
}
$$

這表示 richer macrostate 對未來有更高預測力。

因此：

$$
\boxed{
ProjectionDesign
}
$$

和：

$$
\boxed{
StateAugmentation
}
$$

必須一起考慮。

---

## 27. 高階資訊不是魔法恢復

如果：

$$
\pi
$$

真的 non-injective，

僅知道：

$$
Z=\pi(X)
$$

不能唯一反演：

$$
X.
$$

高階智能即使再強，也不能從不存在於 input 的資訊中保證唯一重建。

它只能加入：

$$
\boxed{
AuxiliaryInformation\ Z_{aux}
}
$$

例如：

- history；
- sensor；
- memory；
- priors；
- external records。

此時：

$$
\boxed{
H(
X
\mid
Z,Z_{aux}
)
\le
H(
X
\mid
Z
).
}
$$

但不保證為零。

所以：

$$
\boxed{
Intelligence
\neq
InverseOfNonInjectiveProjection.
}
$$

---

## 28. Causal Abstraction

僅有 observational prediction 還不夠。

更強的 macro validity 要求：

> 高階 intervention 是否能與低階 intervention 對應？

設 micro model：

$$
M_L,
$$

macro model：

$$
M_H,
$$

projection：

$$
\pi:
M_L\rightarrow M_H.
$$

若高階介入：

$$
I_H
$$

存在對應低階介入：

$$
\omega(I_H)=I_L,
$$

而：

$$
\boxed{
\pi
\left(
do_{L}(I_L)(x)
\right)
\approx
do_H(I_H)
\left(
\pi(x)
\right),
}
$$

則 diagram 近似 commute。

---

## 29. Causal Fidelity Error

可定義：

$$
\boxed{
\epsilon_C(\pi,I)
=
D
\left(
\pi(
do_L(\omega(I))(X)
),
do_H(I)(\pi(X))
\right).
}
$$

若對研究範圍中的 interventions：

$$
\epsilon_C\ll1,
$$

則 high-level model 有較高：

$$
\boxed{
InterventionalFidelity.
}
$$

這比：

$$
Correlation(Z_t,Z_{t+1})
$$

更強。

---

## 30. 2026 的 compositional causal abstraction

近期工作進一步把 causal abstraction 表達為可組合模型之間的 abstraction，並區分 high-to-low / low-to-high query mapping。

這對 HSNRD 很重要。

因為我們不只需要：

$$
StateProjection,
$$

還需要：

$$
\boxed{
QueryProjection
}
$$

與：

$$
\boxed{
InterventionProjection.
}
$$

例如：

> 「解散公司」這個 high-level intervention

不能只被理解成：

> 把某一個員工變量設成 0。

它需要對應一組低階 structural interventions。

---

## 31. Causal Emergence

Hoel 等人的 causal emergence 提供另一個尺度比較方法。

在 Markov system 中，可以比較：

$$
EI_{micro}
$$

與：

$$
EI_{macro}.
$$

若：

$$
\boxed{
EI_{macro}
>
EI_{micro},
}
$$

則在該 coarse-graining 與 effective-information measure 下，可以說 macro model 表現出 causal emergence。

直觀上：

> 適當 coarse-graining 可能移除 micro-level degeneracy / noise，使 macro transitions 更有效率地指定未來狀態。

---

## 32. 但 Causal Emergence 不是新的神秘因果力

HSNRD 不應把：

$$
EI_{macro}>EI_{micro}
$$

翻譯成：

> 宏觀實體產生了完全脫離微觀的新宇宙力。

更保守的是：

$$
\boxed{
MacroLevel
\text{ can be a better causal description}
}
$$

在特定：

- coarse-graining；
- intervention distribution；
- causal metric；

之下成立。

因此：

$$
\boxed{
CausalEmergenceMetric
\neq
OntologicalIndependence.
}
$$

這和前一篇：

$$
DependentAutonomy
$$

完全一致。

---

## 33. Agency-Sufficient Projection

現在進入 HSNRD 最重要的新定義之一。

若研究問題是：

$$
\mathcal Q_A
=
\text{Does }S\text{ behave as an agent?}
$$

則 projection 必須至少保留：

- identity；
- memory；
- preference；
- decision；
- action；
- feedback。

定義：

$$
\boxed{
Z_A
=
\pi_A(X).
}
$$

若：

$$
Z_A
$$

足以預測與解釋：

$$
Decision,
Action,
Update
$$

並在 relevant interventions 下保持 causal fidelity，

則稱：

$$
\boxed{
\pi_A
}
$$

為：

# **Agency-Sufficient Projection**

---

## 34. Agency-Sufficient 不等於 Microstate-Sufficient

可能：

$$
H(X\mid Z_A)\gg0.
$$

也就是：

> 大量 micro information 已被丟掉。

但只要：

$$
\Delta I_{Decision}\approx0,
$$

$$
\Delta I_{Action}\approx0,
$$

$$
\epsilon_C\approx0,
$$

則：

$$
Z_A
$$

仍可能足以支撐高階 agent model。

因此：

$$
\boxed{
AgentReality
\not\Rightarrow
MicrostateRecoverability.
}
$$

這是高階代理數學化的一條非常重要結論。

---

## 35. Member Replacement 作為 projection invariance test

令：

$$
T_\sigma
$$

為 member replacement transformation。

如果：

$$
X'
=
T_\sigma(X)
$$

改變大量具體成員，

但：

$$
\boxed{
\pi_A(X')
\approx
\pi_A(X),
}
$$

則 high-level agency representation 對特定成員具：

$$
ReplacementInvariance.
$$

這正是上一篇的：

$$
RealizerFlexibility
$$

在 projection language 中的版本。

---

## 36. Multiple Realization 的 fiber

對宏觀代理狀態：

$$
z_A,
$$

其 preimage：

$$
\boxed{
\pi_A^{-1}(z_A)
}
$$

包含所有能實現相同高階代理狀態的 micro-configurations。

因此：

$$
\boxed{
MultipleRealizationClass
=
\pi_A^{-1}(z_A).
}
$$

這裡使用 preimage / fiber 一詞是標準函數語義。

但這不等於 HSNRD I 的「relation bundle」變成微分幾何 fiber bundle。

兩者仍須分開。

---

## 37. Projection 與 Type

不同 node type 應具有不同 projection：

$$
\boxed{
\pi_\tau.
}
$$

Family 的 macrostate 可能保留：

- care structure；
- kinship；
- household memory。

Corporation 則保留：

- ownership；
- governance；
- cashflow；
- strategy。

所以：

$$
\boxed{
Projection
=
TypeDependent.
}
$$

這和 HSNRD I：

$$
ExistenceCondition
=
TypeDependent
$$

平行。

---

## 38. Projection 與 Relation Type

同樣，

不同 relation layer 可以使用不同 coarse-graining operator：

$$
\boxed{
\pi_\rho.
}
$$

例如：

### Economic flow

可以近似 sum：

$$
\bar W^{econ}
=
P W^{econ}P^\top.
$$

### Belief

可能需要 distribution / entropy。

### Coercion

可能需要 max / threshold / capacity。

### Information

可能需要 channel capacity / mutual information。

因此：

$$
\boxed{
OneAggregationOperator
\not\Rightarrow
AllRelationLayers.
}
$$

---

## 39. 高階狀態的資訊預算

可以把 macro representation 想成有限 budget：

$$
B_Z.
$$

我們要選擇保留：

$$
\boxed{
RelevantStateVariables
}
$$

而不是：

$$
Everything.
$$

因此可以寫一個 HSNRD conceptual optimization：

$$
\boxed{
\min_{\pi}
\quad
\lambda_C C(\pi)
+
\lambda_L \Delta I_{\mathcal Q}(\pi)
+
\lambda_D D_{dyn}(\pi)
+
\lambda_I \epsilon_C(\pi).
}
$$

其中：

- $C(\pi)$ ：representation complexity；
- $\Delta I_{\mathcal Q}$ ：task information loss；
- $D_{dyn}$ ：dynamical non-closure；
- $\epsilon_C$ ：causal abstraction error。

這不是唯一正式 objective，

但揭示 HSNRD projection design 的四個互相衝突目標。

---

## 40. Good Macrostate 的四個條件

因此本文提出：

$$
\boxed{
GoodMacrostate
=
Compression
+
TaskSufficiency
+
DynamicalClosure
+
InterventionalFidelity.
}
$$

### Compression

$$
Complexity(Z)<Complexity(X).
$$

### Task Sufficiency

$$
\Delta I_{\mathcal Q}\approx0.
$$

### Dynamical Closure

$$
Z_t
$$

對：

$$
Z_{t+1}
$$

有足夠封閉預測能力。

### Interventional Fidelity

macro intervention 與 micro intervention 近似 commute。

---

## 41. 不存在普遍最佳 projection

如果 query 改變：

$$
\mathcal Q_1
\rightarrow
\mathcal Q_2,
$$

最佳：

$$
\pi^*
$$

也可能改變。

所以：

$$
\boxed{
\pi^*
=
\pi^*(\mathcal Q,\tau,\rho,Tolerance).
}
$$

這與前面：

$$
Autonomy(S;\mathcal Q)
$$

完全一致。

HSNRD 不追求：

> 一張宇宙唯一正確的宏觀圖。

而是：

> 對指定問題足夠、合法且可驗證的高階表示。

---

## 42. 投影的合法性層級

本文建議把 projection validity 分成四級。

### Level P0 — Descriptive Projection

只做到：

$$
Z=\pi(X).
$$

### Level P1 — Informational Projection

能量化：

$$
H(X\mid Z)
$$

與：

$$
\Delta I_{\mathcal Q}.
$$

### Level P2 — Dynamical Projection

具有：

$$
DynamicalClosure.
$$

### Level P3 — Causal Projection

具有：

$$
InterventionalFidelity.
$$

若還要做 agent attribution，

需要再加：

### Level PA — Agency-Sufficient Projection

保留：

$$
Identity,Memory,Preference,Decision,Action,Feedback.
$$

---

## 43. HSNRD II 的數學公理／限制

### Axiom P1 — Projection Explicitness

每個 macrostate 應明確說明：

$$
\boxed{
Z=\pi(X).
}
$$

### Axiom P2 — Non-Injectivity Awareness

若：

$$
\pi
$$

非單射，

不得宣稱從 $Z$ 唯一恢復 $X$ 。

### Axiom P3 — Representation–Physics Separation

$$
\boxed{
H(X\mid Z)>0
}
$$

不是物理資訊毀滅命題。

### Axiom P4 — Query Relativity

$$
\boxed{
ProjectionValidity
=
ProjectionValidity(\mathcal Q).
}
$$

### Axiom P5 — Data Processing

在適當 Markov 條件下：

$$
\boxed{
I(Z;Y)\le I(X;Y).
}
$$

### Axiom P6 — Markov Closure Not Automatic

$$
\boxed{
MarkovMicro
\not\Rightarrow
MarkovMacro.
}
$$

### Axiom P7 — Causal Fidelity Requires Interventions

observational compression 不足以證明 causal abstraction。

### Axiom P8 — Agency Requires Agency-Sufficient Projection

高階 agent attribution 不應只依 macro correlation。

---

## 44. 與第一部的重新連接

第一部說：

$$
HigherOrderExistence
\neq
HigherOrderAgency.
$$

本篇現在補上：

> 高階 existence projection 與高階 agency projection 也不一定相同。

因此：

$$
\boxed{
\pi_E
\neq
\pi_A
}
$$

一般成立。

用來判斷「公司是否存在」的變量，

不一定足以判斷：

> 公司究竟想要什麼？

---

## 45. Want 的投影條件

如果要寫：

$$
GroupReflexivelyWants(S,x),
$$

projection 至少應保存：

$$
P_S(x),
$$

$$
I_S(x),
$$

$$
ActionCoupling,
$$

$$
Feedback,
$$

$$
SelfModel.
$$

因此：

$$
\boxed{
WantAttribution
=
ProjectionSensitive.
}
$$

若 projection 只保留：

$$
Outcome=x,
$$

就不能從：

$$
SystemReached(x)
$$

反推出：

$$
SystemWanted(x).
$$

所以：

$$
\boxed{
OutcomeProjection
\not\Rightarrow
IntentionProjection.
}
$$

---

## 46. Leviathan Reversal 的投影問題

同理，

只看：

$$
StatePolicy_t
$$

可能看不到：

$$
PurposeDrift,
ExitLoss,
DownwardReshaping.
$$

所以 Leviathan analysis 需要：

$$
\boxed{
\pi_L
}
$$

保留：

- purpose state；
- rewrite reachability；
- top-down coupling；
- self-preservation weight。

如果 projection 過粗，

一個 entrenched system 可能看起來只是：

> 穩定。

因此：

$$
\boxed{
StabilityProjection
\neq
EntrenchmentProjection.
}
$$

---

## 47. 投影本身也可以成為權力

第一部曾區分正當性與代理。

現在可以再看到：

> 誰決定 macro categories？

本身就是制度問題。

例如：

- 哪些個體被統計；
- 哪些事件被記錄；
- 哪些偏好被聚合；
- 哪些 relation 被忽略。

這些都決定：

$$
\pi.
$$

因此：

$$
\boxed{
ProjectionRule
}
$$

可以具有政治與制度後果。

但這屬 normative / institutional analysis，

不應被 Shannon entropy 本身偷偷決定。

---

## 48. 結論

HSNRD 若沒有 projection theory，

高階集合只是：

> 被人為畫在低階節點上方的第二張圖。

真正讓：

$$
Micro
\rightarrow
Macro
$$

成立的是：

$$
\boxed{
Projection.
}
$$

而 projection 必然帶來：

- equivalence classes；
- multiple realization；
- information compression；
- possible ambiguity。

因此：

$$
\boxed{
H(X\mid\pi(X))
}
$$

可以衡量離散 deterministic projection 下的 micro reconstruction uncertainty，

而：

$$
\boxed{
\Delta I_Y
=
I(X;Y)-I(\pi(X);Y)
}
$$

則衡量 task-relevant information loss。

但 good macrostate 不應只追求資訊最多。

它還必須考慮：

$$
\boxed{
DynamicalClosure
}
$$

與：

$$
\boxed{
InterventionalFidelity.
}
$$

所以本文最終得到：

$$
\boxed{
GoodMacrostate
=
Compression
+
TaskSufficiency
+
DynamicalClosure
+
InterventionalFidelity.
}
$$

對高階代理，還要再加入：

$$
\boxed{
AgencySufficiency.
}
$$

因此：

$$
\boxed{
AgentReality
\not\Rightarrow
MicrostateRecoverability.
}
$$

高階 agent 可以是真實、穩定且具有解釋力，

即使我們無法從高階狀態唯一重建每一個低階細節。

下一篇將正式讓這些 macro nodes 開始：

- 出生；
- 死亡；
- 合併；
- 分裂；
- 改型；

並把 graph rewriting、rule algebra、CTMC 與 PDMP 統一起來：

# **HSNRD III：結構重寫、歷史路徑與混合動力學**

---

## 參考文獻

Geiger, B. C., & Temmel, C. (2014). “Lumpings of Markov Chains, Entropy Rate Preservation, and Higher-Order Lumpability.” *Journal of Applied Probability*, 51(4).

Hoel, E. P., Albantakis, L., & Tononi, G. (2013). “Quantifying Causal Emergence Shows That Macro Can Beat Micro.” *Proceedings of the National Academy of Sciences*, 110(49), 19790–19795.

Jørgensen, F. H., Weichwald, S., & Hammond, L. (2026). “Causal Foundations of Collective Agency.” arXiv:2605.00248.

List, C., & Pettit, P. (2008). “Group Agency and Supervenience.” In *Being Reduced: New Essays on Reduction, Explanation, and Causation*. Oxford University Press.

List, C., & Pettit, P. (2011). *Group Agency: The Possibility, Design, and Status of Corporate Agents*. Oxford University Press.

Lorenz, R., & Tull, S. (2026). “Causal and Compositional Abstraction.” arXiv:2602.16612.

Massidda, R., Geiger, A., Icard, T., & Bacciu, D. (2022). “Causal Abstraction with Soft Interventions.” arXiv:2211.12270.

Tishby, N., Pereira, F. C., & Bialek, W. (2000). “The Information Bottleneck Method.” arXiv:physics/0004057.

Polyanskiy, Y., & Wu, Y. *Information Theory* / MIT 6.441 lecture notes.

---

## 本篇核心命題表

| 編號 | 命題 |
|---|---|
| P8.1 | $Macrostate=Projection(Microstate)$ |
| P8.2 | $NonInjectiveProjection\Rightarrow MultipleRealization$ |
| P8.3 | $RepresentationalInformationLoss\neq PhysicalInformationDestruction$ |
| P8.4 | $GoodProjection\neq LosslessProjection$ |
| P8.5 | $I(Z;Y)\le I(X;Y)$ under data-processing conditions |
| P8.6 | $MarkovMicro\not\Rightarrow MarkovMacro$ |
| P8.7 | $DescriptiveMacrostate\neq DynamicalMacrostate$ |
| P8.8 | $Intelligence\neq InverseOfNonInjectiveProjection$ |
| P8.9 | $CausalEmergenceMetric\neq OntologicalIndependence$ |
| P8.10 | $AgentReality\not\Rightarrow MicrostateRecoverability$ |
| P8.11 | $\pi_E\neq\pi_A$ in general |
| P8.12 | $OutcomeProjection\not\Rightarrow IntentionProjection$ |
| P8.13 | $StabilityProjection\neq EntrenchmentProjection$ |
| P8.14 | Projection validity is query-, type-, and tolerance-relative |

---

**系列：高階集合、欲求與 Leviathan / HSNRD 完整数學方法論**  
**第二部：HSNRD 完整数學方法論**  
**篇次：08 / 10**
