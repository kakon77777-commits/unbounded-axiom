# 失敗不被刪除：Fold 算子與錯誤的元知識化

## Failure Is Not Deleted: The Fold Operator and the Meta-Knowledge Transformation of Error

**系列**：遞歸折疊認識論：從 PDF 成功—排除雙法到多模型可修正認知，第 4 篇／共 8 篇＋1 篇總結  
**系列英文名**：Recursive Fold Epistemology: From the PDF Success–Falsification Duality to Corrigible Multi-Model Cognition  
**文件編號**：EML-RFE-2026-04-v0.1  
**作者**：Neo.K with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-09-02  
**性質**：認識論／Failure Folding／Meta-Knowledge／Recursive Learning／Model Revision  
**狀態**：Public Theory Draft  
**直接前置**：EML-RFE-2026-01 至 03；PDF 成功法；PDF 排除法；認知呼吸理論；認知解構學

---

## 生成、認識論與範圍聲明

本文是一篇 AI 輔助生成的理論研究稿。

本文不主張任何失敗都天然有價值，也不主張只要把失敗保存下來就能自動產生知識。失敗若缺乏可靠紀錄、來源、可重現性、原因分析或與後續模型的連接，仍可能只是噪音、成本或不可用事件。

本文所主張的是：

$$
\boxed{
\text{Failed Theory}
\neq
\text{Deleted Theory}.
}
$$

當失敗具有足夠資訊時，它不應只被標記為「錯」並從當前工作集合中刪除，而應經由一個明確的轉換過程，進入下一輪認知系統的元知識層。

本文將此過程稱為：

$$
\boxed{
\operatorname{Fold}.
}
$$

Fold 不是壓縮一切失敗，也不是把所有錯誤合理化成成功，而是把失敗中的可保留結構提取為未來認知約束。

---

# 摘要

傳統研究流程常將失敗理解成淘汰：

$$
T_i
\rightarrow
\text{Rejected}
\rightarrow
\text{Removed}.
$$

這種做法在候選管理上有效，卻存在一個重要風險：如果只保存「此模型失敗」而沒有保存「在哪裡失敗、如何失敗、為什麼失敗、失敗透露了什麼邊界」，那麼下一輪模型生成可能重新進入同一失敗區域。

本文因此提出 Fold 算子：

$$
\boxed{
\operatorname{Fold}
:
F_t
\rightarrow
K_{t+1}^{\mathrm{meta}}.
}
$$

其中：

$$
F_t
$$

是當前失敗與反例集合，

$$
K_{t+1}^{\mathrm{meta}}
$$

是下一輪認知狀態中的元知識。

Fold 的基本輸出不是單一標籤，而至少包括：

$$
\boxed{
\operatorname{Fold}(F_t)
=
\{
C,
X,
B,
M,
O,
Q
\}.
}
$$

其中：

- $C$：Constraint，未來模型應遵守的約束；
- $X$：Counterexample，對特定理論仍有效的反例；
- $B$：Boundary，模型適用域與失效域邊界；
- $M$：Failure Mode，失敗機制；
- $O$：Alternative Ontology Pressure，對新本體的壓力；
- $Q$：New Question，新問題生成。

本文進一步區分：

$$
\boxed{
\text{Archive}
\neq
\text{Fold}.
}
$$

Archive 只是保存：

> 某件事曾經失敗。

Fold 則要求：

> 這次失敗如何改變未來模型生成、驗證、權重配置或問題設計？

因此，Fold 的成功標準不是記錄數量，而是：

$$
\boxed{
\Delta \mathcal E_{t+1}
\neq
0.
}
$$

即失敗必須真正改變下一輪認知狀態。

本文提出「失敗轉化率」：

$$
\boxed{
\eta_F
=
\frac{
|\operatorname{UsefulFold}(F_t)|
}{
|F_t|
}.
}
$$

高 $\eta_F$ 表示大量失敗被轉化為有效元知識；低 $\eta_F$ 則表示研究系統反覆產生錯誤卻無法吸收。

本文也提出「失敗地圖」：

$$
\boxed{
\mathcal G_F
=
(V_F,E_F),
}
$$

將不同失敗節點連接為一張負幾何圖。這張圖描述：

- 哪些模型已失敗；
- 哪些失敗共享機制；
- 哪些區域已被排除；
- 哪些邊界仍未理解；
- 哪些失敗正指向新的模型空間。

因此：

$$
\boxed{
\text{Map of Failed Worlds}
}
$$

本身成為一種研究資產。

本文最終提出：

$$
\boxed{
\text{A mature epistemic system does not merely remember that it was wrong; it remembers the geometry of why it was wrong}.
}
$$

中文：

> **成熟的認知系統，不只記得自己曾經錯過；它還保留錯誤發生的幾何結構。**

**關鍵詞**：Fold 算子、失敗折疊、元知識、反例、失敗模式、負幾何、模型邊界、認知地層、可修正認知

---

# 0. 問題的提出：刪掉錯誤之後，我們到底留下了什麼？

假設：

$$
T_1
$$

被證據否定。

最簡單流程：

$$
T_1
\rightarrow
\text{Reject}.
$$

然後：

$$
\Theta_{t+1}
=
\Theta_t
\setminus
\{T_1\}.
$$

這看似合理。

但下一輪研究者如果只知道：

> $T_1$ 不對。

卻不知道：

- 哪個預測失敗；
- 哪個尺度失敗；
- 哪個資料域失敗；
- 哪個假設造成失敗；
- 哪些部分其實仍有效；

那麼：

$$
\boxed{
\text{Elimination}
}
$$

就丟失了大量資訊。

---

# 1. 淘汰與吸收不是同一件事

本文區分：

$$
\boxed{
\text{Eliminate}
\neq
\text{Absorb}.
}
$$

Eliminate：

> 不再使用此模型。

Absorb：

> 把此模型失敗的結構轉進下一輪認知。

---

# 2. 失敗不是二值標籤

傳統：

$$
F(T_i)\in\{0,1\}.
$$

新版應該記錄：

$$
\boxed{
F(T_i)
=
(
where,
when,
how,
under\ what\ conditions,
against\ which\ evidence
).
}
$$

---

# 3. 失敗事件

本文定義失敗事件：

$$
\boxed{
f_j
=
(
T_j,
D_j,
C_j,
R_j,
S_j,
M_j
).
}
$$

其中：

- $T_j$：失敗模型；
- $D_j$：對應證據；
- $C_j$：條件；
- $R_j$：可靠度；
- $S_j$：適用域／尺度；
- $M_j$：暫定失敗機制。

---

# 4. 失敗集合

$$
\boxed{
F_t
=
\{f_1,f_2,\ldots,f_n\}.
}
$$

它不是垃圾桶。

它是：

$$
\boxed{
\text{negative epistemic structure}.
}
$$

---

# 5. Archive 不等於 Fold

Archive：

$$
\boxed{
f_j
\rightarrow
\text{stored}.
}
$$

Fold：

$$
\boxed{
f_j
\rightarrow
\Delta K^{\mathrm{meta}}.
}
$$

因此：

$$
\boxed{
\text{Archive}
\neq
\text{Fold}.
}
$$

---

# 6. Fold 算子

本文正式定義：

$$
\boxed{
\operatorname{Fold}
:
F_t
\rightarrow
K_{t+1}^{\mathrm{meta}}.
}
$$

其中：

$$
K_{t+1}^{\mathrm{meta}}
$$

不是一般對象知識，

而是：

> 如何思考下一輪問題的知識。

---

# 7. Fold 的六類基本輸出

$$
\boxed{
\operatorname{Fold}(F_t)
=
\{
C,
X,
B,
M,
O,
Q
\}.
}
$$

---

# 8. Constraint

$$
\boxed{
C
=
\text{Constraint}.
}
$$

形式：

> 未來模型不能違反某已可靠建立的條件。

例如：

$$
T_{\mathrm{new}}
\models
C.
$$

---

# 9. Counterexample

$$
\boxed{
X
=
\text{Counterexample}.
}
$$

一個反例不一定排除整個理論，

但它必須永久保持為：

$$
\boxed{
\text{test point}
}
$$

用於下一輪模型。

---

# 10. Boundary

$$
\boxed{
B
=
\text{Boundary}.
}
$$

某理論可能不是全錯，

而是：

$$
\boxed{
T
\text{ valid in }
\mathcal D_1,
\quad
T
\text{ fails in }
\mathcal D_2.
}
$$

Fold 應把失敗轉成適用邊界。

---

# 11. Failure Mode

$$
\boxed{
M
=
\text{Failure Mode}.
}
$$

不是只問：

> 哪裡錯？

而是：

> **透過什麼機制錯？**

---

# 12. Alternative Ontology Pressure

若多個失敗都指向：

> 原 ontology 沒有表示某個現象。

則 Fold 產生：

$$
\boxed{
O
=
\text{Alternative Ontology Pressure}.
}
$$

---

# 13. New Question

失敗還可能生成：

$$
\boxed{
Q
=
\text{New Question}.
}
$$

例如：

> 為什麼這個例外一直出現？

這個問題可能比原理論本身更有價值。

---

# 14. Fold 的目標不是保存所有細節

如果失敗資料量巨大：

$$
|F_t|\gg1,
$$

不能把所有失敗都原樣帶進工作記憶。

所以 Fold 同時是一種：

$$
\boxed{
\text{structured compression}.
}
$$

---

# 15. 失敗壓縮

理想 Fold：

$$
\boxed{
F_t
\rightarrow
\tilde F_t
}
$$

其中：

$$
|\tilde F_t|
\ll
|F_t|,
$$

但保留：

$$
\boxed{
I_{\mathrm{relevant}}(F_t).
}
$$

---

# 16. 壓縮不能抹掉來源

所以每個 Folded item：

$$
\phi_j
$$

仍應能追溯：

$$
\boxed{
\phi_j
\rightarrow
\{f_{j1},f_{j2},\ldots\}.
}
$$

也就是保留 provenance。

---

# 17. Folded Constraint 需要可回溯證據

例如：

> 模型不能假設 X 永遠線性。

應能回溯到：

- 哪些資料；
- 哪些實驗；
- 哪些版本；

支持這個約束。

---

# 18. 否則 Fold 會變成新的教條

如果：

$$
C
$$

沒有 provenance，

它可能從「由失敗生成的暫時限制」變成：

$$
\boxed{
\text{unquestioned inherited dogma}.
}
$$

---

# 19. Folded Knowledge 也必須可修正

因此：

$$
\boxed{
K^{\mathrm{meta}}
}
$$

本身也具有版本。

即：

$$
K_t^{\mathrm{meta}}
\rightarrow
K_{t+1}^{\mathrm{meta}}.
$$

---

# 20. 失敗地圖

本文提出：

$$
\boxed{
\mathcal G_F
=
(
V_F,
E_F
).
}
$$

其中：

- $V_F$：失敗節點；
- $E_F$：失敗之間的關係。

---

# 21. 失敗關係

兩個失敗：

$$
f_i,f_j
$$

可能共享：

- 同一假設；
- 同一尺度；
- 同一資料域；
- 同一演算法；
- 同一 ontology。

所以：

$$
\boxed{
E_F(f_i,f_j)
}
$$

可表示失敗相似性或因果關聯。

---

# 22. 失敗叢集

若：

$$
f_1,f_2,\ldots,f_k
$$

形成高密度 cluster，

可能表示：

$$
\boxed{
\text{shared failure mechanism}.
}
$$

---

# 23. 單一 anomaly 與失敗叢集不同

一個 anomaly：

$$
f_1
$$

可能只是噪音。

但大量獨立失敗都指向同一結構：

$$
\boxed{
Cluster(F)
}
$$

則更值得進入 Fold。

---

# 24. Negative Geometry

本文稱：

$$
\boxed{
\mathcal G_F
}
$$

為：

$$
\boxed{
\text{Negative Geometry of the Search Space}.
}
$$

它描述：

> 哪些方向曾經走過且失敗。

---

# 25. 正向地圖與負向地圖

傳統知識圖：

$$
\mathcal G_K
$$

多半記錄：

> 什麼成立。

RFE 同時需要：

$$
\boxed{
\mathcal G_K
+
\mathcal G_F.
}
$$

---

# 26. 沒有失敗地圖的研究容易重複探索

如果新研究者只讀成功論文，

可能不知道：

- 哪些路徑已測過；
- 哪些模型曾失敗；
- 哪些失敗從未發表。

因此：

$$
\boxed{
\text{Publication Bias}
\rightarrow
\text{Epistemic Memory Loss}.
}
$$

---

# 27. Negative Results 的真正價值

負結果的價值不是：

> 也值得發表。

更深的是：

$$
\boxed{
\text{they shape future search geometry}.
}
$$

---

# 28. Fold 與搜尋效率

若失敗約束有效，

新探索空間可由：

$$
\Theta_t
$$

縮減成：

$$
\Theta_t'
$$

其中排除：

$$
\boxed{
\mathcal R_{\mathrm{known\ failure}}.
}
$$

---

# 29. 失敗地圖提高下一輪探索效率

概念上：

$$
\boxed{
Efficiency_{t+1}
=
f(
Knowledge_t,
FailureMap_t
).
}
$$

不只依賴正向知識。

---

# 30. Foldable Failure

不是每個失敗都值得折疊。

本文定義：

$$
\boxed{
F_{\mathrm{foldable}}
\subseteq
F_t.
}
$$

---

# 31. Foldability Criteria

一個失敗較值得 Fold，若具備：

1. 可重現；
2. 高 provenance；
3. 有模型區分力；
4. 可指出邊界；
5. 可產生新約束；
6. 可改變後續研究設計。

---

# 32. Failure Quality

定義概念量：

$$
\boxed{
Q_F(f)
=
g(
R,
P,
D,
B,
G
).
}
$$

其中：

- $R$：reproducibility；
- $P$：provenance；
- $D$：discriminative power；
- $B$：boundary information；
- $G$：generative usefulness。

---

# 33. 高品質失敗

若：

$$
Q_F(f)\gg0,
$$

它可能比一個低資訊成功更有價值。

---

# 34. 低品質失敗

若：

$$
Q_F(f)\approx0,
$$

則應保留原始紀錄，

但不應提高為高階約束。

---

# 35. Fold Level

本文提出四層 Fold：

$$
\boxed{
L_F\in\{0,1,2,3\}.
}
$$

---

# 36. Level 0：Raw Archive

$$
\boxed{
L_F=0.
}
$$

只保存原始失敗事件。

---

# 37. Level 1：Local Fold

$$
\boxed{
L_F=1.
}
$$

轉成：

- 參數限制；
- 邊界；
- 局部反例。

---

# 38. Level 2：Structural Fold

$$
\boxed{
L_F=2.
}
$$

轉成：

- 模型結構修正；
- 失敗機制；
- 變量新增。

---

# 39. Level 3：Meta-Fold

$$
\boxed{
L_F=3.
}
$$

轉成：

- 問題重寫；
- ontology 壓力；
- 模型語言重置；
- 更新方法修正。

---

# 40. Fold 深度與 Reset 深度對應

Paper 03 的：

$$
d_R
$$

與本篇：

$$
L_F
$$

高度相關。

一般而言：

$$
\boxed{
L_F\uparrow
\Rightarrow
d_R\uparrow
}
$$

但不是一一對應。

---

# 41. Fold 不是一次完成

一個失敗最初可能只有：

$$
L_F=0.
$$

隨更多證據累積，

可以升級成：

$$
L_F=1\rightarrow2\rightarrow3.
$$

---

# 42. 延遲折疊

本文提出：

$$
\boxed{
\text{Deferred Folding}.
}
$$

即：

> 現在不知道這個失敗意味什麼，但先保留，等待未來模型出現後重新解讀。

---

# 43. 這是版本歷史的重要理由

今天的 anomaly：

$$
a_t
$$

可能在十年後成為：

$$
\boxed{
\text{critical evidence}.
}
$$

所以：

$$
\boxed{
\text{Unknown Significance}
\neq
\text{Zero Future Value}.
}
$$

---

# 44. 失敗重新解讀

同一失敗：

$$
f
$$

在模型：

$$
T_t
$$

下可能是：

> measurement anomaly。

在：

$$
T_{t+5}
$$

下可能變成：

> decisive boundary evidence。

---

# 45. 因此 Fold 具有時間性

$$
\boxed{
\operatorname{Fold}_t(f)
\neq
\operatorname{Fold}_{t+n}(f).
}
$$

元知識本身會隨理論環境改變。

---

# 46. Fold 需要版本化

所以每個 Folded item 可表示：

$$
\boxed{
\phi_j^{v1},
\phi_j^{v2},
\ldots
}
$$

---

# 47. 認知地層

這與 Paper 01 的：

$$
\boxed{
\text{Epistemic Stratigraphy}
}
$$

直接相連。

失敗不只存在於資料層，

也形成：

$$
\boxed{
\text{historical layers of interpretation}.
}
$$

---

# 48. 失敗折疊與認知呼吸

認知呼吸：

$$
\text{Expand}
\rightarrow
\text{Integrate}
\rightarrow
\text{Compress}.
$$

Fold 可以位於：

$$
\boxed{
\text{Integrate}
\rightarrow
\text{Compress}
}
$$

之間。

---

# 49. 為什麼？

因為 Integrate 階段識別：

- 衝突；
- 模式；
- 重複失敗；

Fold 則將其壓成：

- 約束；
- 邊界；
- 新問題。

---

# 50. Fold 是帶方向性的壓縮

一般壓縮問：

> 怎麼用更少符號保存更多信息？

Fold 還問：

> **這些信息要如何改變下一輪搜索？**

所以：

$$
\boxed{
\text{Fold}
\neq
\text{Compression}.
}
$$

而是：

$$
\boxed{
\text{Directional Compression for Future Search}.
}
$$

---

# 51. Fold Operator 的形式結構

可表示：

$$
\boxed{
\operatorname{Fold}
(
F_t,
D_t,
K_t,
\Theta_t,
U_t
)
\rightarrow
(
C_t^{-},
B_t,
M_t,
Q_t^{+},
O_t^{+},
U_t^{+}
).
}
$$

---

# 52. 輸出一：負約束

$$
C_t^{-}
$$

表示：

> 未來模型應避免的已知失敗區域。

---

# 53. 輸出二：邊界

$$
B_t
$$

表示：

> 哪些區域仍有效、哪些已失效。

---

# 54. 輸出三：失敗機制

$$
M_t
$$

表示：

> 失敗為何發生。

---

# 55. 輸出四：新問題

$$
Q_t^{+}
$$

表示：

> 失敗生成了哪些新的研究問題。

---

# 56. 輸出五：新 ontology 壓力

$$
O_t^{+}
$$

表示：

> 現有存在分類是否不足。

---

# 57. 輸出六：更新器修正

$$
U_t^{+}
$$

表示：

> 我們原本的研究方法是否也需要修改。

---

# 58. Fold 後的認知狀態

因此：

$$
\boxed{
\mathcal E_{t+1}
=
\mathcal E_t
+
\operatorname{Fold}(F_t).
}
$$

但這裡的「+」不是簡單集合聯集，

而是結構更新。

---

# 59. Fold 可能使知識集合變小

例如 Fold 發現：

> 某個原本接受知識只在狹窄範圍成立。

於是：

$$
K_{t+1}
\subset
K_t.
$$

這仍然是認知進步。

---

# 60. 認知進步不是知識量單調增加

因此：

$$
\boxed{
\text{Epistemic Progress}
\neq
|K_t|\uparrow.
}
$$

有時：

$$
|K_{t+1}|<|K_t|
$$

但結構更準確。

---

# 61. Fold 的價值在於結構品質

比起：

$$
|K|
$$

更重要的是：

$$
\boxed{
\text{Coherence},
\text{Boundary Accuracy},
\text{Revision Capacity}.
}
$$

---

# 62. 失敗轉化率

本文提出：

$$
\boxed{
\eta_F
=
\frac{
N_{\mathrm{useful\ folded}}
}{
N_{\mathrm{reliable\ failures}}
}.
}
$$

---

# 63. 高 $\eta_F$

表示：

- 失敗被分析；
- 邊界被抽取；
- 新模型受益；
- 重複錯誤下降。

---

# 64. 低 $\eta_F$

表示：

$$
\boxed{
\text{Failure Production}
\gg
\text{Failure Assimilation}.
}
$$

這種系統可能很勤奮，

但認知效率很低。

---

# 65. Failure Debt

本文提出：

$$
\boxed{
Debt_F
=
\text{reliable failures not yet meaningfully folded}.
}
$$

---

# 66. Failure Debt 過高的後果

如果：

$$
Debt_F\uparrow,
$$

可能造成：

- 重複犯錯；
- anomaly 堆積；
- 模型空間假穩定；
- 過早收斂。

---

# 67. 研究系統應定期償還 Failure Debt

即：

$$
\boxed{
\text{Review}
\rightarrow
\text{Cluster}
\rightarrow
\text{Fold}.
}
$$

---

# 68. AI 特別適合償還 Failure Debt

AI 可以掃描：

- 舊實驗；
- bug；
- rejected hypotheses；
- negative results；
- abandoned branches。

並尋找：

$$
\boxed{
\text{latent shared failure structure}.
}
$$

---

# 69. 但 AI 也可能錯誤 Fold

例如 AI 可能把：

- 偶然噪音；
- 共同偏差；
- benchmark artifact；

錯誤提升成一般約束。

所以：

$$
\boxed{
\text{Automated Fold}
\neq
\text{Trusted Fold}.
}
$$

---

# 70. Fold Audit

每個高階 Fold 應接受：

$$
\boxed{
\text{Fold Audit}.
}
$$

至少問：

1. 失敗來源可靠嗎？
2. 是否可重現？
3. 是否存在替代解釋？
4. 是否過度一般化？
5. 是否跨域成立？

---

# 71. Over-Folding

本文提出：

$$
\boxed{
\text{Over-Folding}.
}
$$

即從少量失敗抽取過強規則。

例如：

$$
f_1
\Rightarrow
\text{Never use model class }M.
$$

可能是過度推論。

---

# 72. Under-Folding

相反：

$$
\boxed{
\text{Under-Folding}.
}
$$

即已有大量結構性失敗，

卻仍只把每個 anomaly 當孤立事件。

---

# 73. Fold Calibration

因此需要：

$$
\boxed{
\text{Fold Depth}
\propto
\text{Evidence Strength}
+
\text{Failure Consistency}.
}
$$

---

# 74. 失敗與未知的區分

不能把：

$$
\text{not yet working}
$$

全部叫：

$$
\text{false}.
$$

因此 Fold 要區分：

$$
\boxed{
\text{False}
\neq
\text{Unresolved}
\neq
\text{Unimplemented}
\neq
\text{Untested}.
}
$$

---

# 75. 工程失敗與理論失敗再次分離

某個模型沒有成功執行，

可能只是：

$$
F_{\mathrm{implementation}}.
$$

如果誤 Fold 成：

$$
F_{\mathrm{theory}},
$$

會錯誤淘汰理論方向。

---

# 76. Fold 需要 Failure Ontology

本文提出：

$$
\boxed{
O_F
=
\text{Failure Ontology}.
}
$$

至少區分：

- theory；
- measurement；
- implementation；
- data；
- assumption；
- scope；
- ontology；
- representation；
- update rule。

---

# 77. Failure Ontology 也可修正

因為新型失敗可能出現：

$$
f_{\mathrm{new}}
\notin
O_F.
$$

所以：

$$
\boxed{
O_F(t+1)
\not\subseteq
O_F(t)
}
$$

可以成立。

---

# 78. 這就是 RFE 的自指一致性

連「錯誤分類法」都不能永遠固定。

---

# 79. Fold 與新問題生成

很多重大問題不是從成功中長出，

而是從：

> 為什麼這裡一直失敗？

長出。

所以：

$$
\boxed{
F_t
\rightarrow
Q_{t+1}^{+}.
}
$$

---

# 80. Failure-to-Question Conversion

本文定義：

$$
\boxed{
\chi_{FQ}
=
\frac{
N_{\mathrm{new\ useful\ questions}}
}{
N_{\mathrm{folded\ failure\ clusters}}
}.
}
$$

它衡量失敗生成新問題的能力。

---

# 81. 新問題可能比原答案更重要

一個被證偽的理論：

$$
T
$$

可能留下：

$$
Q'
$$

而：

$$
Value(Q')
>
Value(T).
$$

完全可能。

---

# 82. Fold 與替代 ontology

如果多個失敗都表明：

> 我們的類別分法不夠。

則：

$$
\boxed{
F_t
\rightarrow
O_{t+1}^{+}.
}
$$

這直接接 Paper 03。

---

# 83. Fold 是 Reframe 的燃料

因此：

$$
\boxed{
\operatorname{Fold}
\rightarrow
\operatorname{Reframe}.
}
$$

Paper 03 說「何時需要重置」。

Paper 04 說「重置拿什麼當材料」。

---

# 84. 沒有 Fold 的 Reframe 容易變成亂猜

如果重置沒有帶入：

$$
F_t,
$$

新的模型空間可能重複舊錯。

所以：

$$
\boxed{
\text{Reframe without Fold}
\rightarrow
\text{Epistemic Amnesia Risk}.
}
$$

---

# 85. Fold 後的新生成

下一輪：

$$
\Theta_{t+1}
$$

應受到：

$$
\boxed{
K_t^{\mathrm{meta}}
}
$$

約束。

因此：

$$
\boxed{
\Theta_{t+1}
=
\operatorname{Generate}
(
D_t,
K_t,
K_t^{\mathrm{meta}},
Q_{t+1}
).
}
$$

---

# 86. 這就是「錯誤被折回去」

不是：

$$
\text{Error}
\rightarrow
\text{Delete}.
$$

而是：

$$
\boxed{
\text{Error}
\rightarrow
\text{Meta-Knowledge}
\rightarrow
\text{Future Generation Constraint}.
}
$$

---

# 87. Fold 與壓縮不變量

如果多個失敗：

$$
f_1,\ldots,f_n
$$

共享某個模式：

$$
I_F,
$$

則 Fold 應提取：

$$
\boxed{
I_F
=
\text{Failure Invariant}.
}
$$

---

# 88. Failure Invariant

例如：

> 只要系統忽略延遲，就在高負載區失敗。

這比記住一百次個別崩潰更有用。

---

# 89. 失敗不變量是高價值元知識

因為它可以：

$$
\boxed{
\text{transfer across models}.
}
$$

---

# 90. Fold 的真正終點不是「知道這裡錯」

而是：

$$
\boxed{
\text{future cognition behaves differently because this failure occurred}.
}
$$

---

# 91. 行為改變測試

若：

$$
F_t
$$

被宣稱已 Fold，

但下一輪：

$$
\mathcal A_{t+1}
=
\mathcal A_t,
$$

其中 $\mathcal A$ 是研究行動策略，

則 Fold 可能只是形式紀錄。

---

# 92. Effective Fold

本文定義：

$$
\boxed{
\text{Effective Fold}
\Rightarrow
\Delta
(
\Theta,
Q,
U,
A,
C
)
\neq0.
}
$$

至少有一項改變：

- 模型空間；
- 問題；
- 更新法；
- 行動策略；
- 約束。

---

# 93. Fold 的最低驗收條件

一次 Fold 至少應回答：

1. 失敗是什麼類型？
2. 哪些證據支撐？
3. 哪些條件下成立？
4. 哪些模型受影響？
5. 形成什麼未來約束？
6. 下一輪將因此做什麼不同？

---

# 94. Fold Template

可用：

$$
\boxed{
\Phi(f)
=
(
Type,
Evidence,
Scope,
Mechanism,
Constraint,
NextAction
).
}
$$

---

# 95. 這使 Fold 可工程化

RFE 不只是一個哲學比喻。

Fold 可以實作成：

- research log；
- model registry；
- failure database；
- experiment memory；
- AI agent memory layer。

---

# 96. AI Agent 的 Fold Memory

一個 agent 若只保存：

> Task failed.

幾乎沒有價值。

更好的記憶：

$$
\boxed{
\text{Why}
+
\text{When}
+
\text{Boundary}
+
\text{Do Not Repeat}
+
\text{Alternative}.
}
$$

---

# 97. 這與軟體工程高度同構

bug report 如果只寫：

> 壞了。

沒有價值。

真正有用的是：

- reproduction；
- environment；
- root cause；
- regression test；
- fix boundary。

Fold 其實是把這種工程紀律提升成一般認識論。

---

# 98. Regression Test 就是失敗折疊的一種

當 bug 被修掉後加入：

$$
\boxed{
\text{regression test},
}
$$

本質就是：

> 把過去失敗變成未來系統不能再跨越的約束。

這正是：

$$
\boxed{
F_t
\rightarrow
C_{t+1}^{-}.
}
$$

---

# 99. 科學也需要 epistemic regression tests

某個理論更新後，

應重新測：

- 舊反例；
- 舊成功；
- 邊界案例。

所以：

$$
\boxed{
\text{Epistemic Regression Test Suite}.
}
$$

可以成為 RFE 的重要工具。

---

# 100. 結論：錯誤真正的價值，不在「它也是資訊」，而在「它被折成未來不能忽略的結構」

PDF 排除法最初的重要洞察是：

> 失敗不是零資訊。

RFE 在此進一步提出：

> **只有被轉換成後續結構的失敗，才真正成為認知資產。**

因此：

$$
\boxed{
\text{Failure}
\neq
\text{Progress}.
}
$$

而是：

$$
\boxed{
\text{Failure}
+
\text{Fold}
\rightarrow
\text{Meta-Knowledge}.
}
$$

Fold 的輸出至少包括：

$$
\boxed{
\{
Constraint,
Counterexample,
Boundary,
FailureMode,
AlternativeOntology,
NewQuestion
\}.
}
$$

所以：

$$
\boxed{
F_t
\rightarrow
K_{t+1}^{\mathrm{meta}}.
}
$$

而：

$$
\boxed{
K_{t+1}^{\mathrm{meta}}
\rightarrow
\Theta_{t+1}^{\mathrm{better\ constrained}}.
}
$$

這形成：

$$
\boxed{
\text{Fail}
\rightarrow
\text{Fold}
\rightarrow
\text{Reframe}
\rightarrow
\text{Rebranch}.
}
$$

失敗不再只是終點。

也不是心理安慰。

它成為：

$$
\boxed{
\text{future search geometry}.
}
$$

本文最終命題：

$$
\boxed{
\text{A mature epistemic system does not merely remember that it was wrong; it remembers the geometry of why it was wrong}.
}
$$

以及：

$$
\boxed{
\text{Failure becomes knowledge only when it changes future cognition}.
}
$$

中文：

> **真正被吸收的失敗，不只是被記住；它會改變下一輪模型怎麼生成、哪裡不再浪費時間、哪些邊界必須保留，以及新的問題應該從哪裡長出來。**

---

## 核心命題摘要

### 命題一

$$
\boxed{
\text{Failed Theory}
\neq
\text{Deleted Theory}.
}
$$

### 命題二

$$
\boxed{
\text{Archive}
\neq
\text{Fold}.
}
$$

### 命題三

$$
\boxed{
\operatorname{Fold}
:
F_t
\rightarrow
K_{t+1}^{\mathrm{meta}}.
}
$$

### 命題四

$$
\boxed{
\operatorname{Fold}(F_t)
=
\{
C,X,B,M,O,Q
\}.
}
$$

### 命題五

$$
\boxed{
\mathcal G_F
=
\text{Negative Geometry of the Search Space}.
}
$$

### 命題六

$$
\boxed{
\text{Epistemic Progress}
\neq
|K_t|\uparrow.
}
$$

### 命題七

$$
\boxed{
Debt_F
=
\text{unfolded reliable failures}.
}
$$

### 命題八

$$
\boxed{
\text{Reframe without Fold}
\rightarrow
\text{Epistemic Amnesia Risk}.
}
$$

### 命題九

$$
\boxed{
\text{Effective Fold}
\Rightarrow
\Delta(
\Theta,Q,U,A,C
)\neq0.
}
$$

### 命題十

$$
\boxed{
\text{Failure becomes knowledge only when it changes future cognition}.
}
$$

---

## 系列接口

Paper 03 建立：

$$
\boxed{
T^*
\notin
\Theta_t
}
$$

與：

$$
\boxed{
\Theta_{t+1}
\not\subseteq
\Theta_t.
}
$$

Paper 04 則回答：

> 當我們決定重建模型空間時，舊失敗到底要怎麼帶進去？

答案是：

$$
\boxed{
F_t
\rightarrow
\operatorname{Fold}
\rightarrow
K_{t+1}^{\mathrm{meta}}.
}
$$

下一篇：

**Paper 05：《從螺旋到折疊圖：分支、合併、壓縮與再展開的認知動力學》**

將把：

$$
\boxed{
\text{Branch}
\rightarrow
\text{Explore}
\rightarrow
\text{Compare}
\rightarrow
\text{Fold}
\rightarrow
\text{Compress}
\rightarrow
\text{Re-expand}
}
$$

正式建成一個圖式認知動力學框架，並處理：

- 分支何時應保留；
- 模型何時應合併；
- 不變量如何壓縮；
- 何時重新展開；
- 如何避免無限分支爆炸。
