# 前作成功如何變成下一作的認知債務：Iteration Learning 與 Trust Debt

**系列：** AI 時代的創作、選擇與人類復古系列  
**篇次：** 第 11 篇  
**版本：** v0.1  
**性質：** 理論論文／跨作品學習模型／公開版

---

## 摘要

創作者通常將前作成功理解為一種資產。這是合理的：成功作品會留下程式碼、美術、品牌、受眾、技術、流程與經驗。然而，成功同時也可能留下另一種較少被討論的資產負面效應：**對既有模型的過度信任。**

本篇提出：

$$
\boxed{
\text{Past Success}
=
\text{Capability Capital}
+
\text{Belief Inertia}
}
$$

成功會提高：

$$
P(M)
$$

也就是創作者對既有方法、審美、流程與設計模型的先驗信任。但若這個先驗在環境已經改變之後仍然不斷壓制新證據，過去成功就可能從：

$$
\boxed{
\text{Learning Asset}
}
$$

轉化成：

$$
\boxed{
\text{Cognitive Debt}
}
$$

本篇進一步區分 **Iteration Learning** 與 **Iteration Repetition**。前者表示每一代作品都將前作的成功與失敗轉化成新的流程、風險模型、設計修正與 QA 資本；後者則只是把既有做法再次執行。

本篇同時提出 **Trust Debt（信任債務）**：玩家基於前作建立的信任，會形成下一作的預期資本；但如果後續作品反覆出現相似問題，這些問題會被視為「沒有學習」，進而使品牌信任損失加速。

因此，真正成熟的系列化開發不應滿足：

$$
\boxed{
Game_{n+1}
=
Game_n
+
MoreFeatures
}
$$

而應更接近：

$$
\boxed{
Game_{n+1}
=
Game_n
+
LearnedCorrections
+
NewCapabilities
-
KnownFailureClasses
}
$$

核心命題是：

$$
\boxed{
\text{Iteration}
\neq
\text{Learning}
}
$$

只有當前作真正改變了下一作的選擇底空間，作品序列才構成學習，而不只是重複。

---

## 關鍵詞

Iteration Learning、Success Lock-In、Trust Debt、Cognitive Debt、Cross-Project Learning、Creative Development、Brand Trust、Regression Capital、Epistemic Capital、Selection

---

# 1. 成功為什麼通常被視為資產

一部成功作品會留下：

- 程式碼；
- 美術；
- 工具鏈；
- 玩家社群；
- 品牌；
- 市場知識；
- 流程；
- 技術；
- 人脈；
- 資金。

所以：

$$
\boxed{
Success
\rightarrow
Capital
}
$$

這是正常理解。

---

# 2. 但成功也會留下「模型自信」

如果某個方法：

$$
M
$$

曾成功，

則：

$$
P(M)\uparrow
$$

這同樣合理。

問題出現在：

$$
\boxed{
P(M)\uparrow
\rightarrow
UpdateResistance\uparrow
}
$$

也就是：

> 因為以前成功，所以現在更難懷疑自己。

---

# 3. Success Lock-In

本篇定義：

$$
\boxed{
\text{Success Lock-In}
}
$$

為：

> 過去成功提高了對既有方法的信任，並使新證據更難促成模型更新。

可以粗略寫：

$$
\boxed{
C_{update}
=
f(
PastSuccess,
IdentityAttachment,
SunkCost,
BrandCommitment
)
}
$$

當這些變量增加：

$$
C_{update}\uparrow
$$

---

# 4. 過去成功是 Prior，不是法律

如果：

$$
M
$$

曾經成功，

合理做法：

$$
P(M)\uparrow
$$

但新環境：

$$
E_{new}
$$

仍然應該更新：

$$
P(M\mid E_{new})
$$

因此：

$$
\boxed{
\text{Past Success}
=
\text{Strong Prior}
\neq
\text{Permanent Law}
}
$$

---

# 5. Iteration 不等於 Learning

一個創作者可以做：

$$
W_1,W_2,W_3,W_4
$$

四部作品。

但：

$$
\boxed{
N_{\text{works}}=4
}
$$

不代表：

$$
\boxed{
N_{\text{learning cycles}}=4
}
$$

如果每一次都只是：

$$
\text{Build}
\rightarrow
\text{Release}
\rightarrow
\text{Fix}
\rightarrow
\text{Next}
$$

那麼：

$$
\boxed{
\text{Iteration}
}
$$

可能只是：

$$
\boxed{
\text{Repetition}
}
$$

---

# 6. Iteration Learning 的定義

本篇定義：

$$
\boxed{
L_I
=
\text{Iteration Learning}
}
$$

真正成立時，前一作必須：

$$
\boxed{
W_n
\rightarrow
\Delta M
\rightarrow
\Delta Process
\rightarrow
W_{n+1}
}
$$

也就是：

> 前作的證據改變了下一作的模型與流程。

---

# 7. Cross-Project Learning

可定義：

$$
\boxed{
CPL
=
\frac{
N_{\text{past lessons materially reused}}
}{
N_{\text{relevant past lessons}}
}
}
$$

稱為：

$$
\boxed{
\text{Cross-Project Learning Rate}
}
$$

若：

$$
CPL\approx0
$$

表示：

> 每款作品都像第一次做。

---

# 8. 第四款作品理論上應該有什麼不同

做到第四款：

$$
W_4
$$

時，理論上不只：

$$
CodeCapital_4>CodeCapital_1
$$

還應：

$$
\boxed{
QACapital_4>QACapital_1
}
$$

$$
\boxed{
IntegrationCapital_4>IntegrationCapital_1
}
$$

$$
\boxed{
EpistemicCapital_4>EpistemicCapital_1
}
$$

---

# 9. 如果只有資產累積，沒有學習累積

那麼會形成：

$$
\boxed{
\text{Production Capital}\uparrow
}
$$

但：

$$
\boxed{
\text{Learning Capital}\approx constant
}
$$

結果是：

> 做得更快。

但：

> 不一定做得更懂。

---

# 10. 這是 Feature Growth 與 Learning Growth 的分離

可以寫：

$$
F_n
=
\text{Feature Capacity at iteration }n
$$

$$
L_n
=
\text{Learning Capacity at iteration }n
$$

若：

$$
F_n\uparrow
$$

但：

$$
L_n\approx constant
$$

則：

$$
\boxed{
\frac{F_n}{L_n}\uparrow
}
$$

作品可能反而更容易累積 Integration Debt。

---

# 11. 成功會創造 Legacy Assumptions

每次成功都會留下：

$$
\boxed{
A_{legacy}
}
$$

例如：

- 這種 UI 玩家能接受；
- 這種流程沒問題；
- 這種角色美術可行；
- 這種 QA 足夠；
- 這種定價有效；
- 這種設計 philosophy 是對的。

這些假設不是錯。

但它們需要：

$$
\boxed{
\text{Periodic Revalidation}
}
$$

---

# 12. Legacy Assumption

定義：

$$
\boxed{
A_L
=
\text{Legacy Assumption}
}
$$

代表：

> 因過去成功而被自動帶入新作品的假設。

如果新作環境：

$$
E_{n+1}
$$

已改變，

但：

$$
A_L
$$

不重新檢查，

就可能形成：

$$
\boxed{
\text{Legacy Assumption Debt}
}
$$

---

# 13. 技術會變，玩家也會變

過去成功的條件：

$$
E_n
$$

可能包含：

- 當時的硬體；
- 當時的玩家耐性；
- 當時的競品；
- 當時的平台；
- 當時的 AI 能力；
- 當時的價格帶；
- 當時的 UI 標準。

到了：

$$
E_{n+1}
$$

這些條件可能全部不同。

所以：

$$
\boxed{
Success(M,E_n)
}
$$

不能直接推出：

$$
\boxed{
Success(M,E_{n+1})
}
$$

---

# 14. Environment Drift

定義：

$$
\boxed{
D_E
=
Distance(E_n,E_{n+1})
}
$$

若：

$$
D_E\uparrow
$$

則過去經驗的直接可移植性：

$$
Transferability\downarrow
$$

因此：

$$
\boxed{
\text{The faster the environment changes, the more dangerous legacy certainty becomes.}
}
$$

---

# 15. AI 時代讓 Environment Drift 加速

AI、Agent、工具、自動化與玩家預期的變化速度正在提高。

所以：

$$
\boxed{
\frac{dE}{dt}\uparrow
}
$$

這意味著：

$$
\boxed{
\text{Past Success Half-Life}
}
$$

可能縮短。

---

# 16. Success Half-Life

本篇提出：

$$
\boxed{
T_{1/2}^{success}
}
$$

表示：

> 一套過去成功方法，在新環境中仍可被直接信任的時間尺度。

若：

$$
\frac{dE}{dt}\uparrow
$$

則：

$$
\boxed{
T_{1/2}^{success}\downarrow
}
$$

---

# 17. 這不是要否定經驗

經驗仍然很有價值。

真正成熟的態度不是：

> 過去完全沒用。

而是：

$$
\boxed{
\text{Experience}
=
\text{Prior}
+
\text{Risk Memory}
+
\text{Reusable Capability}
}
$$

但不是：

$$
\boxed{
\text{Experience}
=
\text{Automatic Answer}
}
$$

---

# 18. 過去經驗最有價值的是「風險記憶」

成功告訴你：

> 什麼可能有效。

失敗則告訴你：

> 哪裡容易壞。

所以：

$$
\boxed{
\text{Success Memory}
+
\text{Failure Memory}
}
$$

才構成成熟 iteration。

---

# 19. 如果只保留成功記憶

那麼：

$$
\boxed{
\text{Selection Bias}
}
$$

會很強。

創作者只記得：

> 我以前這樣做成功。

卻忘記：

- 玩家抱怨；
- patch；
- regression；
- workaround；
- 中途重做。

所以：

$$
\boxed{
\text{Success Narrative}
}
$$

可能比實際歷史更乾淨。

---

# 20. Clean Success Narrative

本篇稱：

$$
\boxed{
\text{Clean Success Narrative}
}
$$

為：

> 將過去作品的成功重新敘述成一條順利、正確、連續的故事，而忽略其中大量修補、外部協助與失敗。

這會高估：

$$
\boxed{
\text{Original Model Quality}
}
$$

---

# 21. 玩家卻記得不同的歷史

玩家可能記得：

- 哪些 Bug；
- 哪些 patch；
- 哪些設計後來才修；
- 哪些問題曾反覆出現。

所以創作者的：

$$
History_{creator}
$$

與玩家的：

$$
History_{player}
$$

可能不同。

---

# 22. Trust 是跨作品狀態

玩家不是每一款新作都完全歸零。

設：

$$
T_n
=
\text{Trust before work }n
$$

則：

$$
T_{n+1}
=
T_n
+
\Delta T_n
$$

因此：

$$
\boxed{
\text{Trust}
}
$$

是一個：

$$
\boxed{
\text{Persistent Cross-Project State}
}
$$

---

# 23. Trust Capital

若前作：

- 穩定；
- 好玩；
- 回饋良好；
- 長期維護；

則：

$$
\boxed{
T_n\uparrow
}
$$

形成：

$$
\boxed{
\text{Trust Capital}
}
$$

玩家會更願意：

- 首發購買；
- 預購；
- 推薦；
- 忍受小問題；
- 給下一作機會。

---

# 24. Trust Debt

但如果：

$$
ExpectedLearning_n
>
ObservedLearning_n
$$

則玩家會開始產生：

$$
\boxed{
\text{Trust Debt}
}
$$

本篇定義：

$$
\boxed{
D_T
=
\text{Trust Debt}
}
$$

為：

> 玩家因過去關係而期待創作者已經學會某些事情，但新作品顯示這些學習沒有被保留時產生的信任負債。

---

# 25. 第一次犯錯與第四次犯錯不是同一個訊號

第一次：

$$
BugClass_1
$$

玩家可能想：

> 正常。

但若：

$$
BugClass_4
$$

仍與過去高度相似，

玩家解讀可能變成：

> 你沒有學。

所以：

$$
\boxed{
Cost(\text{Repeated Failure Class})
>
Cost(\text{First Failure})
}
$$

---

# 26. Trust Loss 的非線性

可以粗略表示：

$$
L_T(n)
=
\alpha n
+
\beta n^2
$$

其中：

$$
n
$$

是同類問題重複次數。

所以：

$$
\boxed{
\text{Repeated Failure}
}
$$

可能造成超線性信任損失。

---

# 27. 玩家真正期待的是 Learning Continuity

玩家不要求：

> 新作零 Bug。

更合理期待：

$$
\boxed{
\text{Known Problems Should Become Less Likely}
}
$$

也就是：

$$
\boxed{
P(C_i\mid W_{n+1})
<
P(C_i\mid W_n)
}
$$

---

# 28. Learning Continuity

本篇定義：

$$
\boxed{
LC
=
\text{Learning Continuity}
}
$$

表示：

> 過去已支付學費的問題，在未來作品中是否留下持續改善。

---

# 29. Learning Continuity 不是技術複用

即使：

$$
CodeReuse=0
$$

仍可以：

$$
LC>0
$$

因為：

- QA checklist；
- design lessons；
- risk class；
- release gate；

都可以跨作品保留。

所以：

$$
\boxed{
\text{Learning Reuse}
\neq
\text{Code Reuse}
}
$$

---

# 30. 重寫不能成為忘記的理由

新作可能：

- 換 engine；
- 換架構；
- 重寫 UI；
- 改玩法。

這些都合理。

但：

$$
\boxed{
\text{Rewrite}
\neq
\text{Reset Organizational Memory}
}
$$

---

# 31. 技術資產與認知資產必須分開

技術資產：

$$
C_T
$$

可能因重寫歸零一部分。

認知資產：

$$
C_E
$$

則應保留。

因此：

$$
\boxed{
\text{Architecture Reset}
\not\Rightarrow
\text{Learning Reset}
}
$$

---

# 32. Series Development 應該有 Learning Ledger

每一作結束後應留下：

$$
\boxed{
L_n
=
(
Successes,
Failures,
RiskClasses,
PlayerFeedback,
ProcessChanges,
OpenQuestions
)
}
$$

下一作開始時直接讀取。

---

# 33. Iteration Review

新作開發前應問：

1. 前作最強的三個核心優勢是什麼？
2. 前作最常見的三個失敗類別是什麼？
3. 哪些問題已經轉成 regression？
4. 哪些問題其實只是 patch，沒有 root cause fix？
5. 哪些成功依賴當時環境？
6. 哪些 legacy assumptions 需要重新驗證？

這就是：

$$
\boxed{
\text{Iteration Review}
}
$$

---

# 34. Success Debrief 不能只做 Celebration

成功作品結束後通常會：

> 慶祝。

但成熟流程還需要：

$$
\boxed{
\text{Success Debrief}
}
$$

問：

> 哪些成功其實來自外部條件？

> 哪些成功是偶然？

> 哪些問題被成功掩蓋？

> 如果市場不一樣，哪些東西會失效？

---

# 35. Failure Debrief 也不能只找責任

失敗後若只問：

> 誰錯？

容易得到：

$$
\boxed{
\text{Blame}
}
$$

真正有用的是：

$$
\boxed{
\text{What model failed?}
}
$$

即：

> 哪個預測沒有成立？

---

# 36. Iteration Learning Rate

本篇提出：

$$
\boxed{
ILR
=
\frac{
N_{\text{lessons converted into next-project changes}}
}{
N_{\text{validated lessons from prior project}}
}
}
$$

若：

$$
ILR\uparrow
$$

代表：

> 作品序列真的在學習。

---

# 37. Feature Growth 不能代替 Learning Growth

新作：

- 地圖更多；
- 角色更多；
- 系統更多；
- 畫面更好；

不代表：

$$
\boxed{
LearningGrowth>0
}
$$

甚至可能：

$$
FeatureGrowth\uparrow
$$

但：

$$
LearningGrowth\approx0
$$

---

# 38. 這就是「更大，但沒有更成熟」

可以寫：

$$
\boxed{
Scale\uparrow
}
$$

但：

$$
\boxed{
Maturity\approx constant
}
$$

這種產品往往會讓舊問題被更大規模放大。

---

# 39. Success Amplification Trap

本篇提出：

$$
\boxed{
\text{Success Amplification Trap}
}
$$

即：

> 因為前作成功，所以新作把前作模式放大。

如果：

$$
Strengths
$$

與：

$$
Weaknesses
$$

一起被放大，

結果可能：

$$
\boxed{
\text{Bigger Success Structure}
+
\text{Bigger Failure Structure}
}
$$

---

# 40. AI 時代會加速這種陷阱

AI 讓：

$$
FeatureThroughput\uparrow
$$

因此若 Legacy Assumption 沒更新：

$$
\boxed{
\text{Old Model}
\times
\text{Higher Production Power}
}
$$

會更快放大舊錯誤。

---

# 41. 所以 AI 不是天然的學習器

AI 可以：

- 生成；
- 測；
- review；
- 比較。

但如果人類一直餵它：

> 延續原本方向。

它仍可能：

$$
\boxed{
\text{Accelerate the Same Model}
}
$$

而不是修正模型。

---

# 42. AI 需要讀歷史，而不只是當前 spec

若 AI reviewer 只讀：

$$
CurrentBuild
$$

就不知道：

> 哪些問題以前已經發生過。

更成熟應讀：

$$
\boxed{
CurrentState
+
HistoricalState
}
$$

形成：

$$
\boxed{
\text{Cross-Iteration Audit}
}
$$

---

# 43. Cross-Iteration Audit

AI 可以問：

> 這一代和上一代哪些 defect class 相似？

> 哪些玩家回饋已經出現兩次以上？

> 哪些 workflow 完全沒有改？

> 哪些風險已經被證明，但沒有變成 gate？

這就是：

$$
\boxed{
\text{Cross-Iteration Audit}
}
$$

---

# 44. Trust Debt 可以被提前預測

若新作：

$$
W_{n+1}
$$

仍包含：

$$
C_i
$$

而：

$$
C_i
$$

是前作高曝光問題，

則：

$$
\boxed{
ExpectedTrustLoss(C_i)\uparrow
}
$$

因此 release gate 應該提高其 priority。

---

# 45. Reputation-Aware Regression

這可以稱：

$$
\boxed{
\text{Reputation-Aware Regression}
}
$$

不是所有 Bug 都同等重要。

曾經傷害品牌的問題：

$$
\boxed{
BrandSensitiveClass
}
$$

應得到更高 release priority。

---

# 46. 信任也是可累積、可消耗的資本

可以表示：

$$
T_{n+1}
=
T_n
+
Gain_n
-
Loss_n
$$

若：

$$
Loss_n>Gain_n
$$

長期：

$$
T_n\downarrow
$$

玩家可能從：

> 首發買。

變成：

> 等評價。

再變成：

> 打折再說。

---

# 47. Trust Debt 的市場表現

Trust Debt 不一定只表現在評論。

還可能表現在：

- wish-to-buy conversion；
- day-one purchase；
- refund；
- recommendation；
- community tolerance；
- press narrative。

因此：

$$
\boxed{
\text{Trust Debt}
}
$$

是一個跨期商業變量。

---

# 48. 品牌最昂貴的不是負評，而是「預期降級」

當玩家從：

> 我相信他會做好。

變成：

> 我先看看這次又出什麼問題。

那：

$$
\boxed{
\text{Prior Trust}
}
$$

已經下降。

這比單次差評更深。

---

# 49. Trust Capital 與 Learning Capital 相互作用

若團隊持續：

$$
\boxed{
\text{Learn}
}
$$

玩家會觀察到：

$$
\boxed{
\text{Recurring Problems}\downarrow
}
$$

因此：

$$
\boxed{
LearningCapital
\rightarrow
TrustCapital
}
$$

---

# 50. 反過來，沒有學習會把信任資本變成負債

若：

$$
ExpectedLearning>ObservedLearning
$$

則：

$$
\boxed{
TrustCapital
\rightarrow
TrustDebt
}
$$

這是本篇最重要的跨層轉換。

---

# 51. Iteration Learning 的完整模型

可以寫：

$$
\boxed{
W_n
\rightarrow
Evidence_n
\rightarrow
ModelUpdate_n
\rightarrow
ProcessUpdate_n
\rightarrow
W_{n+1}
}
$$

如果中間任一環節斷裂：

$$
\boxed{
\text{Iteration Learning}
}
$$

就會下降。

---

# 52. 真正成熟的作品序列

不應只是：

$$
\boxed{
W_1
\rightarrow
W_2
\rightarrow
W_3
}
$$

而應：

$$
\boxed{
(W_1,L_1)
\rightarrow
(W_2,L_2)
\rightarrow
(W_3,L_3)
}
$$

其中：

$$
L_n
$$

是學習狀態。

---

# 53. 選擇底空間的跨代更新

前作：

$$
W_n
$$

應改變下一作可選集合：

$$
\mathfrak B_{n+1}
$$

即：

$$
\boxed{
\mathfrak B_{n+1}
=
\Phi(
\mathfrak B_n,
Evidence_n,
Learning_n
)
}
$$

這才是真正的跨作品學習。

---

# 54. 如果選擇底空間不變

即使作品序號：

$$
n\uparrow
$$

但：

$$
\mathfrak B_{n+1}\approx\mathfrak B_n
$$

那麼：

$$
\boxed{
\text{Experience Accumulated}
}
$$

卻未必：

$$
\boxed{
\text{Choice Space Improved}
}
$$

---

# 55. Success Lock-In 本質上是選擇空間鎖定

過去成功：

$$
Success_n
$$

會提高某些路徑：

$$
P(a_i)
$$

讓其他道路：

$$
a_j
$$

逐漸不再被考慮。

因此：

$$
\boxed{
\text{Success}
\rightarrow
\text{Choice-Space Compression}
}
$$

也可能發生。

---

# 56. 所以成功也需要被「反事實化」

創作者應問：

> 如果當時沒有這個市場條件，還會成功嗎？

> 如果沒有某個平台曝光，會怎樣？

> 如果競品不同，會怎樣？

這叫：

$$
\boxed{
\text{Counterfactual Success Analysis}
}
$$

---

# 57. Success Attribution 必須和 Failure Attribution 一樣嚴格

不能：

$$
Success
\rightarrow
\text{all internal}
$$

$$
Failure
\rightarrow
\text{all external}
$$

更成熟應該：

$$
\boxed{
\text{Both Success and Failure Need Causal Decomposition}
}
$$

---

# 58. AI 可以做 Success Red Team

AI 不只應：

> 找失敗原因。

也要問：

> 你真的知道自己為什麼成功嗎？

它可以列：

- 產品；
- 市場；
- 時機；
- 價格；
- 平台；
- 口碑；
- 運氣；
- 技術槓桿。

並生成：

$$
\boxed{
\text{Alternative Success Explanations}
}
$$

---

# 59. 這能防止錯誤複製成功

如果錯誤認為：

> 成功因為 Feature A。

下一作就會：

$$
A\uparrow
$$

但真正原因可能是：

$$
B+C+D
$$

於是：

$$
\boxed{
\text{False Success Attribution}
\rightarrow
\text{Bad Iteration}
}
$$

---

# 60. Iteration Learning 也是 Selection Learning

前作真正的價值不是：

> 告訴你下一作做什麼。

而是：

$$
\boxed{
\text{Improves How You Choose}
}
$$

因此：

$$
\boxed{
\text{Iteration Learning}
\subset
\text{Selection Capital}
}
$$

---

# 61. 與下一篇的關係

前十一篇已經建立：

- Human-Retro；
- Value；
- Distinctiveness；
- Consumer Utility；
- Integration Debt；
- AI Second Designer；
- Agentic Development；
- Regression Capital；
- AI Capital；
- Epistemic Capital；
- Iteration Learning / Trust Debt。

下一篇會第一次拿一個大型成功案例做實證壓力測試：

# **《小團隊何以擊穿 AAA 成本牆？——〈光與影：33號遠征隊〉的成功、技術槓桿與生成式 AI 實際貢獻》**

它要檢查：

$$
\boxed{
\text{我們前面的理論，在成功案例上是否仍然成立？}
}
$$

---

# 62. 結論

過去成功當然是一種資產。

但：

$$
\boxed{
\text{Past Success}
}
$$

從來不只是：

$$
\boxed{
\text{Capability Capital}
}
$$

它也可能增加：

$$
\boxed{
\text{Belief Inertia}
}
$$

因此：

$$
\boxed{
\text{Success}
}
$$

既可以讓下一作更強，

也可以讓下一作更難重新懷疑自己。

真正成熟的跨作品開發，不能只是：

$$
Game_{n+1}
=
Game_n
+
More
$$

而應：

$$
\boxed{
Game_{n+1}
=
Game_n
+
LearnedCorrections
+
NewCapabilities
-
KnownFailureClasses
}
$$

同時，玩家也不是每一作重新歸零。

信任會跨作品累積：

$$
\boxed{
T_{n+1}
=
T_n
+
Gain_n
-
Loss_n
}
$$

所以當前作已經替創作者建立信任後，

下一作重複犯同類問題時，

玩家看到的就不再只是：

> 又一個 Bug。

而可能是：

$$
\boxed{
\text{你沒有學。}
}
$$

這就是 Trust Debt 的起點。

真正有價值的作品序列，不是：

> 做了很多作。

而是：

$$
\boxed{
\text{每一作都實際改變了下一作怎麼被選擇、怎麼被測試、怎麼被完成。}
}
$$

因此：

$$
\boxed{
\text{Iteration}
\neq
\text{Learning}
}
$$

真正的 Iteration Learning，必須讓：

$$
\boxed{
\text{Past Success}
+
\text{Past Failure}
}
$$

共同改寫：

$$
\boxed{
\mathfrak B_{future}
}
$$

也就是未來能被選擇的道路。
