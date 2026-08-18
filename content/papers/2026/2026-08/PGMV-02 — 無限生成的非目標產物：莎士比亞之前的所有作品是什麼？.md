# PGMV-02 — 無限生成的非目標產物：莎士比亞之前的所有作品是什麼？

## The Non-Target Products of Infinite Generation: What Are All the Works Before Shakespeare?

**系列：** 後生成文明的意義與價值理論 / Post-Generative Meaning and Value Theory  
**系列代碼：** PGMV  
**論文序號：** 02  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** Target-Residual Corpus / Non-Target Ontology Foundational Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文研究的是目標導向生成系統中「未命中指定 target 的全部產物」應如何分類、去重、驗證與重新估值。本文不主張所有非目標輸出都有價值，也不主張失敗應一律保存。本文亦不把 Quality-Diversity、Novelty Search 或 open-ended evolution 直接等同於本文的 Target-Residual Corpus 理論；它們提供的是相鄰工程證據：單一 objective optimum 並非所有探索問題的唯一合理輸出，而多樣性、niche、archive 與 evaluator 可以成為一等設計變量。本文對「莎士比亞」的使用仍是有限字串 target 的思想實驗，不涉及對文學價值的客觀化宣稱。

---

## 摘要

PGMV-01 將無限猴子問題拆成兩個不同命題。第一問是經典 target-hit 問題：

$$
\exists t:\ X_t=T?
$$

第二問則追問：

$$
\mathcal R_T(N)
=
\{X_t:1\le t\le N,\ X_t\neq T\}
$$

究竟是什麼。

傳統 target-hit formulation 對所有非目標產物使用同一判定：

$$
J_T(x)=\mathbf 1[x=T].
$$

只要：

$$
x\neq T,
$$

便得到：

$$
J_T(x)=0.
$$

然而這個零值只表示：

> $x$ 不是指定 target。

它完全沒有證明 $x$ 沒有真值、知識價值、文學價值、工具價值、轉移價值、反例價值、替代終態價值或歷史價值。

本文因此提出：

$$
\boxed{
\textbf{Target Failure}
\neq
\textbf{General Value Failure}.
}
$$

並把這條原則稱為 **Target-Value Non-Collapse Principle**，即「目標—價值非坍縮原則」。

本文將 Target-Residual Corpus：

$$
\mathcal R_T
$$

從單純的「失敗集合」改寫為一個需要多層 quotient 與 audit 的結構空間。對每個 artifact $x$，至少建立：

$$
\mathbf v(x)
=
(
M_T,Q,N,K,X,H,P,R
),
$$

其中 $M_T$ 為對指定 target 的匹配度， $Q$ 為 quality， $N$ 為 novelty， $K$ 為 knowledge / truth-bearing status， $X$ 為 transferability， $H$ 為 hazard， $P$ 為 provenance， $R$ 為 relational / contextual significance。因此即使：

$$
M_T(x)=0,
$$

其他維度仍可能顯著非零。

本文進一步把非目標產物分成八種主要類別：

$$
\boxed{
\mathcal R_T
=
\mathcal N
\cup
\mathcal D
\cup
\mathcal A
\cup
\mathcal K
\cup
\mathcal O
\cup
\mathcal B
\cup
\mathcal H
\cup
\mathcal U,
}
$$

其中 $\mathcal N$ 是 noise， $\mathcal D$ 是 duplicate / semantic recurrence， $\mathcal A$ 是 alternate valuable artifact， $\mathcal K$ 是 verified knowledge， $\mathcal O$ 是 obstruction / negative knowledge， $\mathcal B$ 是 bridge / transferable structure， $\mathcal H$ 是 hazardous artifact， $\mathcal U$ 是 unknown / unaudited。這些類別不要求互斥。

本文最重要的新概念是 **Residual Revaluation Operator**：

$$
\boxed{
\mathcal V_T:
\mathcal R_T
\longrightarrow
\mathcal P(
\mathcal N,
\mathcal D,
\mathcal A,
\mathcal K,
\mathcal O,
\mathcal B,
\mathcal H,
\mathcal U
).
}
$$

它不改變「是否命中 $T$ 」這件事，而是重新回答：

> 沒命中 $T$ 的 artifact，是否在其他判定軸上具有獨立地位？

這一框架與 Quality-Diversity / MAP-Elites 類方法形成重要對照。單一 objective optimization 常只保留最大 fitness candidate；Quality-Diversity 則試圖在不同 behavioral niches 中保留高品質解集合。Novelty Search 更早提出，在 deceptive objective landscape 中，過度追逐單一 objective 可能阻礙真正創新路徑。2024--2026 年的 QD、open-ended artificial life 與 LLM-assisted QD 研究延續了「archive of diverse high-quality solutions」的工程方向。這些工作不能直接證明本文的價值哲學，但支持一個方法論事實：

$$
\boxed{
\text{A search process may rationally preserve non-winning candidates if they occupy distinct, useful regions of the search space.}
}
$$

2026 年 LLM 創意研究又顯示，在 iterative generation-selection 中，單純增加 iteration 數並不保證 creativity 上升，in-loop evaluator 的設計反而可能是主要變量。這正好說明：當候選供應充足後，系統性能越來越取決於 evaluation architecture，而不是 generation count。

本文亦引入 **Residual Corpus Compression Ratio**：

$$
\operatorname{RCR}
=
1-
\frac{
N_{\mathrm{residual,eff}}
}{
N_{\mathrm{residual,raw}}
},
$$

用以測量大量非目標輸出經語義、結構、功能或證明路徑 quotient 後，究竟有多少只是重採樣。

本文最後提出 **Residual Conservation Principle** 的弱版本：

> 在 audit 之前，不應把所有非目標 artifact 全部摧毀成單一 failure bit；至少應保存足以重建其生成來源、target relation、semantic class 與驗證狀態的最小骨架。

這不是要求永久保存全部 raw text，而是要求：

$$
\boxed{
\text{lossless-at-source when feasible,
compressed-at-navigation,
typed-at-status}.
}
$$

因此，無限猴子第二問真正對 AI 時代提出的挑戰並不是「垃圾太多」，而是：

$$
\boxed{
\textbf{When generation becomes abundant, how do we know which failures are actually noise, which are repetitions, and which are undiscovered alternative successes?}
}
$$

**關鍵詞：** Infinite Monkey Residual Corpus Problem、Target-Residual Corpus、non-target artifacts、Target-Value Non-Collapse、Quality-Diversity、MAP-Elites、Novelty Search、open-ended search、semantic quotient、selection、evaluation、alternative success、AI generation

---

# 1. 問題的重新提出

假設猴子最後真的打出：

$$
T=\text{Hamlet}.
$$

傳統問題完成。

但整個生成歷史：

$$
H_N=(X_1,X_2,\ldots,X_N)
$$

並沒有消失。

# 2. Target hit 只使用一個 bit

$$
J_T(X_i)\in\{0,1\}.
$$

# 3. 這個 bit 丟掉巨大資訊

它不記距離、語義、品質、真值、新穎性、功能與 provenance。

# 4. Target evaluation 是有損投影

$$
\boxed{
\Pi_T:\mathcal X\rightarrow\{0,1\}.
}
$$

# 5. Residual corpus

$$
\mathcal R_T=\Pi_T^{-1}(0).
$$

# 6. 這個集合通常極端異質

其中可能同時存在：

$$
\text{noise}
$$

與：

$$
\text{masterpiece}.
$$

# 7. 第一條核心原則

$$
\boxed{
\textbf{Target Failure}
\neq
\textbf{General Failure}.
}
$$

# 8. Target-Value Non-Collapse Principle

若：

$$
J_T(x)=0,
$$

不能推出：

$$
V_j(x)=0
$$

對所有其他價值維度 $j$。

# 9. 形式化

$$
\boxed{
J_T(x)=0
\not\Rightarrow
\mathbf V(x)=\mathbf 0.
}
$$

# 10. Objective-Induced Blindness

如果評估函數只記：

$$
\mathbf 1[x=T],
$$

那麼所有非目標內部差異都被壓平。本文稱此為：

$$
\boxed{
\textbf{Objective-Induced Blindness}.
}
$$

# 11. 失敗是 task-relative

應寫：

$$
S(x\mid T),
$$

而不是不帶任務地宣告：

$$
S(x).
$$

若有兩個 target：

$$
T_1,T_2,
$$

完全可能：

$$
J_{T_1}(x)=0,
\qquad
J_{T_2}(x)=1.
$$

所以：

$$
\boxed{
\text{Failure is relative to a task contract.}
}
$$

# 12. 從 target 點到終態集合

沿用解空間幾何，可把成功定義成：

$$
G_T=\{z:z\sim_T g\}.
$$

如此 exact-string mismatch 不必等於 task failure。

但新的 residual 仍存在：

$$
\mathcal R_{G_T}
=
\{x:x\notin G_T\}.
$$

---

# 13. 八類 residual taxonomy

本文使用：

$$
\mathcal N,\mathcal D,\mathcal A,\mathcal K,\mathcal O,\mathcal B,\mathcal H,\mathcal U.
$$

# 14. $\mathcal N$：Noise

沒有穩定 syntax、semantics、function 或 reuse。

但：

$$
\mathcal N=\mathcal N(D,R)
$$

依 domain 與 regime 而變。一個領域的 noise 可能是另一領域的 signal。

# 15. $\mathcal D$：Duplicate / Recurrence

表面不同，但 quotient 後相同，例如 punctuation variants、paraphrase、same plot skeleton、same proof route、same obstruction。

# 16. $\mathcal A$：Alternate Valuable Artifact

不是當前 target，但滿足另一個有價值功能。

例如原本要解 A，過程中得到能有效處理 B 的工具。

# 17. $\mathcal K$：Verified Knowledge

包括可證 theorem、正確 observation、validated relation 或 formally checked local result。即使與 target 無關，也可能進 knowledge base。

# 18. $\mathcal O$：Obstruction / Negative Knowledge

失敗 artifact 可能形成：

> 在條件 $A$ 下，方法族 $M$ 無法跨越障礙 $O$。

若能形式化，它是高價值 negative result。

# 19. $\mathcal B$：Bridge / Transfer Structure

artifact 本身不是解，但建立：

$$
A\leftrightarrow B
$$

或縮短其他問題的有效距離。

# 20. $\mathcal H$：Hazard

包含危險 falsehood、deception、unsafe consequence 或其他需要隔離的內容。高 novelty 絕不代表低 hazard。

# 21. $\mathcal U$：Unknown / Unaudited

沒有足夠 evidence。

$$
\boxed{
\operatorname{Unknown}(x)
\not\Rightarrow
\operatorname{Noise}(x)
}
$$

且：

$$
\boxed{
\operatorname{Unknown}(x)
\not\Rightarrow
\operatorname{Valuable}(x).
}
$$

Unknown 必須保持 unknown。

---

# 22. Residual feature vector

定義：

$$
\mathbf v(x)
=
(
m_T,q,n,k,x_f,h,p,r
).
$$

更合理的 value representation 是：

$$
\mathbf V(x)
=
(
V_T,V_K,V_X,V_A,V_R,V_H
).
$$

數學、文學、政策與工程不應被預設使用同一個 scalar value function。

---

# 23. Residual Revaluation Operator

$$
\boxed{
\mathcal V_T:
\mathcal R_T
\longrightarrow
\mathcal C_{\mathrm{typed}}.
}
$$

完整流程：

$$
\boxed{
\mathcal R_T
\rightarrow
\text{Type}
\rightarrow
/\sim
\rightarrow
\text{Verify}
\rightarrow
\text{Transfer}
\rightarrow
\text{Retain/Discard}.
}
$$

早期 quotient 只能是：

$$
\sim_{\mathrm{candidate}},
$$

高風險 equivalence 經 audit 才能升成：

$$
\sim_{\mathrm{certified}}.
$$

---

# 24. Residual Corpus Compression Ratio

$$
N_R^{\mathrm{eff}}
=
|\mathcal R_T/\sim|.
$$

定義：

$$
\boxed{
\operatorname{RCR}
=
1-
\frac{
N_R^{\mathrm{eff}}
}{
N_R^{\mathrm{raw}}
}.
}
$$

高 RCR 代表大量 residual 只是重複；低 RCR 代表 structural diversity 較高。

但：

$$
\boxed{
\text{Diversity}\neq\text{Quality}.
}
$$

---

# 25. Quality-Diversity 的相鄰啟發

傳統單 objective：

$$
\max_x f(x).
$$

QD 則維護不同 behavioral niches 中的高品質候選：

$$
\{x_i^\star\}.
$$

MAP-Elites 把 behavior space 切成 cells，每個 cell 保存 elite。

這和本文的相似點是：

> 不是所有沒有成為總冠軍的候選都丟掉。

差異則是：PGMV 的 residual descriptors 可能是 emergent、semantic、historical、relational、value-dependent，因此不能直接套用固定 MAP-Elites niche。

---

# 26. Novelty Search 的相鄰啟發

在 deceptive objective landscape 中，過度追 target 可能妨礙探索。

典型 novelty：

$$
\rho(x)
=
\frac1k
\sum_{i=1}^k
d(x,\mu_i).
$$

Novelty Search 問：

> detour 是否幫助搜尋？

PGMV-02 再問：

> detour artifact 本身是否具有可保留價值？

---

# 27. Open-endedness 不等於無限亂數

$$
\boxed{
\text{unbounded generation}
\neq
\text{open-ended evolution}.
}
$$

open-ended process 還需要 variation、retention、selection、structure 與 cumulative novelty。猴子沒有 cumulative retention。

---

# 28. LLM-assisted QD

2024 的 LLM + Quality-Diversity work 已把 generator、archive、diversity examples 組成可執行系統。PGMV 在此之上還需要：

$$
\text{verification}
+
\text{provenance}
+
\text{value type}.
$$

---

# 29. Iterative generation-selection 的 2026 證據

近期 creative-search work 顯示，更多 iteration 並不自動帶來更高 creativity；in-loop evaluator 的設計可以是更重要變量。

因此：

$$
\boxed{
\text{Generation Count is not a sufficient optimization variable.}
}
$$

猴子的極端正是：

$$
N\rightarrow\infty,
\qquad
E_{\mathrm{judge}}=0.
$$

---

# 30. Evaluator 也需要 audit

Generator + Evaluator 仍不是完整系統，因 evaluator 可能偏誤。需要：

$$
E_2(E_1)
$$

式 meta-evaluation，以及不同 evaluator 的 disagreement：

$$
D_E(x).
$$

高 disagreement 不是高價值證明，但可以作為 human-audit routing signal。

---

# 31. Semantic entropy 的限制

2026 open-ended creativity evaluation 使用 semantic entropy 作 divergent creativity proxy，但：

$$
\boxed{
H_{\mathrm{semantic}}\neq V.
}
$$

高 entropy 也可能是亂碼，因此仍要配 task fulfilment、quality、truth 或 domain-specific verification。

---

# 32. 生成式 AI 的多樣性悖論

2026 的 real-world generative-search research 顯示：生成式 AI 可以擴張傳統搜尋不易表達的 inquiry 類型，但在可比較的 searchable queries 上，回答 diversity 可能低於 traditional search results。

因此：

$$
\boxed{
\text{expanded inquiry}
+
\text{compressed exposure diversity}
}
$$

可以同時成立。

---

# 33. 高吞吐不等於廣 support

$$
\boxed{
\text{High throughput}\neq\text{Broad support}.
}
$$

LLM 可能在合理文字區具有高 useful density，卻因 distribution concentration 長期重採樣相似結構。

---

# 34. Monkey 與 LLM 是互補極限

猴子：

$$
\text{support broad},
\qquad
\text{useful density tiny}.
$$

LLM：

$$
\text{useful density high},
\qquad
\text{support may be concentrated}.
$$

理想探索器需要同時關心：

$$
\boxed{
(Q,D,V)
}
$$

quality、diversity、verification。

---

# 35. 三角失衡

高 Q、低 D：

$$
\text{homogenization}.
$$

高 D、低 Q：

$$
\text{garbage ocean}.
$$

高 Q、高 D、低 V：

$$
\text{truth uncertainty}.
$$

這三種都可能發生於後生成系統。

---

# 36. Residual density vector

$$
\rho_Q
=
\frac{N_{\mathrm{quality}}}{N_R^{\mathrm{raw}}},
$$

$$
\rho_K
=
\frac{N_{\mathrm{verified\ knowledge}}}{N_R^{\mathrm{raw}}},
$$

$$
\rho_X
=
\frac{N_{\mathrm{transferable}}}{N_R^{\mathrm{eff}}},
$$

再加入：

$$
\rho_H.
$$

得到：

$$
\boxed{
\boldsymbol\rho_R
=
(
\rho_Q,\rho_K,\rho_X,\rho_H,\operatorname{RCR}
).
}
$$

---

# 37. Near-target artifact

Residual 內還應有：

$$
\mathcal P_T
=
\text{partial-progress class}.
$$

例如 proof 只差一個 lemma，不能和純 random failure 同類：

$$
\text{unfinished}\neq\text{zero progress}.
$$

---

# 38. Objective Escape

有些非目標產物會指出：

> 原 target 不是最值得追的方向。

本文稱：

$$
\boxed{
\textbf{Objective Escape}.
}
$$

它可以由 CI 的 Reframe 或 GCS 的 Bypass 觸發。

但它可能只是逃避主任務，因此狀態應分：

- justified；
- transferred；
- evasion；
- unknown。

---

# 39. Residual genealogy

一個 residual artifact：

$$
x
$$

可能成為新 parent：

$$
x\rightarrow\mathcal D(x).
$$

所以 residual 不一定是 terminal garbage。

---

# 40. Residual fertility

定義：

$$
\Phi_R(x)
=
G_A(x)S_D(x)T_D(x).
$$

可能：

$$
J_T(x)=0
$$

但：

$$
\Phi_R(x)\gg0.
$$

這就是最強的 alternate-value case。

---

# 41. Value 可以時間依賴

$$
V_t(x).
$$

當下無用的 artifact 未來可能重要，因此立即 hard-delete 有 future-value loss；但保存所有 raw corpus 又會製造新的 Babel。

---

# 42. Residual Conservation Principle

$$
\boxed{
\textbf{Do not collapse an unaudited residual artifact to a single failure bit if its provenance and structural class can be preserved at reasonable cost.}
}
$$

它不是永久全文保存要求，而是 minimal reconstructible skeleton 要求。

---

# 43. 記憶策略

$$
\boxed{
\text{lossless-at-source when feasible}
}
$$

$$
\boxed{
\text{compressed-at-navigation}
}
$$

$$
\boxed{
\text{typed-at-status}.
}
$$

---

# 44. Residual archive 也可能變成 Babel

記憶的目標不是最大容量，而是最大：

$$
\boxed{
\text{recoverable useful structure}.
}
$$

定義：

$$
U_A
=
\frac{
\text{recoverable valuable structure}
}{
\text{storage+retrieval cost}
}.
$$

若 compression distortion 為 $D_A$：

$$
\max U_A
\quad
\text{subject to}
\quad
D_A\le\epsilon.
$$

---

# 45. 「有多少不同故事？」沒有單一答案

因 equivalence relation 不同：

$$
N_{\mathrm{eff}}^{(\mathrm{plot})}
\neq
N_{\mathrm{eff}}^{(\mathrm{style})}
\neq
N_{\mathrm{eff}}^{(\mathrm{theme})}.
$$

因此：

$$
\boxed{
\text{Novelty is relation-dependent.}
}
$$

應寫：

$$
N(x\mid\sim).
$$

---

# 46. Quality–Novelty 四象限

| | 高新穎 | 低新穎 |
|---|---|---|
| 高品質 | innovation | refinement |
| 低品質 | noisy exploration | duplication |

再加入 truth、transfer、hazard 後，真正 residual space 是高維的。

---

# 47. Goodhart risk

只獎 novelty：

$$
\rightarrow
\text{strangeness}.
$$

只獎 quality：

$$
\rightarrow
\text{homogenization}.
$$

只獎 target proximity：

$$
\rightarrow
\text{alternate-value blindness}.
$$

所以探索階段通常比單一 scalar 更需要 archive-based multi-objective management。

---

# 48. Target Channel + Residual Channel

後生成 AI 可以分：

$$
\boxed{
\text{Target Channel}
+
\text{Residual Channel}.
}
$$

Target Channel 主要追：

$$
J_T.
$$

Residual Channel 使用少量 budget 保存高潛力、未知但結構新穎、或可轉移的候選。

---

# 49. Residual Budget Hypothesis

設探索資源：

$$
B_R.
$$

$$
B_R=0
$$

是 target-only。

本文提出可證偽假說：

$$
\exists\ D:
B_R^\star>0
$$

使 residual-aware policy 的長期總知識收益高於 target-only policy。

---

# 50. Residual Recognition Problem

$$
\boxed{
\textbf{Given a huge residual corpus, how can a finite system recognize rare valuable artifacts without being overwhelmed by noise, duplication, or hazard?}
}
$$

中文：

**殘餘識別問題。**

這可能比 generation problem 更接近後生成時代核心。

---

# 51. Recognition complexity

$$
C_{\mathrm{recog}}(x).
$$

當：

$$
C_{\mathrm{gen}}
\ll
C_{\mathrm{recog}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{integrate}},
$$

生成便不再是主要瓶頸。

---

# 52. Residual triage

可以用：

$$
\operatorname{Priority}(x)
=
f(N,Q,D_E,X,H,C).
$$

但 triage 必須測：

$$
F_D
=
\frac{
N_{\mathrm{valuable\ discarded}}
}{
N_{\mathrm{valuable}}
}
$$

與 false retain rate。

---

# 53. Rare Value Recall

$$
R_{\mathrm{rare}}
=
\frac{
N_{\mathrm{rare\ valuable\ retained}}
}{
N_{\mathrm{rare\ valuable}}
}.
$$

如果：

$$
R_{\mathrm{rare}}\approx0,
$$

系統會把真正異常的新東西全部丟掉。

如果全保留，archive 又爆炸。

---

# 54. Alternative Success

若：

$$
x\notin G_T
$$

但存在：

$$
T'\in\mathcal F
$$

使：

$$
x\in G_{T'}
$$

且：

$$
V(x\mid T')>\tau,
$$

則 $x$ 是相對 task family $\mathcal F$ 的 alternate success：

$$
\boxed{
\text{failure here, success elsewhere}.
}
$$

---

# 55. Transfer Success

若 $x$ 是 $T$ 的副產物，後來能降低 $T'$ 的求解成本，則具有：

$$
B(x;T,T')
$$

的 bridge value。

---

# 56. 猴子不會認出 alternate success

這正是猴子與智能的巨大差別。

在理想 infinite corpus 中，alternate successes 可以大量存在，但猴子只提供：

$$
\text{existence},
$$

不提供：

$$
\text{recognition}.
$$

---

# 57. Local Babel Condition

有限文明若面對：

$$
N_{\mathrm{candidate}}
\gg
C_{\mathrm{human\ attention}},
$$

候選空間在功能上已不可遍歷。

本文稱：

$$
\boxed{
\textbf{Local Babel Condition}.
}
$$

其核心是：

$$
\boxed{
\text{availability without accessibility}.
}
$$

---

# 58. 三套理論在 Local Babel 下的分工

CI：

$$
\text{generate and distill}.
$$

GCS：

$$
\text{navigate and reduce effective distance}.
$$

LSI：

$$
\text{quotient and detect recurrence}.
$$

PGMV：

$$
\text{decide which distinctions deserve value attention}.
$$

---

# 59. Residual-aware CI

CI 生成的新候選若被當前 Guard 拒絕，不應只有 DELETE，而應至少分成：

```text
INVALID
IRRELEVANT
DUPLICATE
ALTERNATIVE
UNKNOWN
```

---

# 60. Residual-aware GCS

如果 artifact 沒降低到 $G_T$ 的距離，還可以問：

> 它是否降低到另一個有價值 $G_{T'}$ 的距離？

---

# 61. Residual-aware LSI

LSI 的 semantic quotient、route identity 與 higher-order recurrence 讓 residual archive 不被 surface explosion 淹沒。

---

# 62. 後生成智能的雙重原則

PGMV-01：

$$
\boxed{
\text{Know what need not be generated again.}
}
$$

PGMV-02：

$$
\boxed{
\text{Know which failures must not be discarded.}
}
$$

兩者互相制衡：

$$
\text{too much generation}
\rightarrow
\text{slop},
$$

$$
\text{too much deletion}
\rightarrow
\text{lost novelty}.
$$

成熟智能需要：

$$
\boxed{
\text{generative restraint}
+
\text{residual sensitivity}.
}
$$

---

# 63. 人類創作的 residual 原型

人類創作本來就有：

- drafts；
- abandoned sketches；
- failed melodies；
- side results；
- unexpected observations。

AI 不是發明 residual，而是把 residual scale 放大。

---

# 64. Role bundle 重新配置

後生成創作角色可能拆成：

- generator；
- selector；
- editor；
- verifier；
- integrator；
- commissioner；
- responsible author。

本文不主張人類未來只剩 curator，而是指出 role boundary 會因候選供給增加而改變。

---

# 65. Provenance 是 residual 的一部分

若 artifact 後來變重要，需要知道：

- 誰生成；
- 為哪個 target；
- 為何被拒；
- 當時 status；
- 經過哪些修訂。

所以 artifact bytes 並不窮盡它的歷史與關係價值。

---

# 66. 從作品到文明方案

未來 candidate 可能不是小說，而是：

$$
W_1,\ldots,W_n
$$

政策、制度、城市、教育或文明方案。

若只有一個 official target，其他全部 hard-delete，同樣可能出現 Objective-Induced Blindness。

本文只提出一個弱命題：

$$
\boxed{
\text{One task objective cannot generally stand in for every possible value dimension.}
}
$$

---

# 67. 實驗一：Hidden Alternative Masterpiece

在 synthetic corpus 中埋少量：

$$
x^\star
$$

它們不是 target，但具有高 alternate value。測 residual triage 的 rare-value recall。

# 68. 實驗二：Duplicate Flood

產生：

$$
10^5
$$

surface variants，測 RCR、false merge、false split。

# 69. 實驗三：Target-only vs Residual-aware Search

比較：

$$
\Pi_T
$$

與：

$$
\Pi_{T+R}.
$$

測 target success、alternate discovery、transfer assets 與 total cost。

# 70. 實驗四：Evaluator Bottleneck

固定 generator，只改 evaluator。測 evaluator improvement 是否比單純增加 generation count 更有效。

# 71. 實驗五：Archive Saturation

逐步增加 archive，測 retrieval quality、maintenance cost 與 rare-value recall 是否呈非單調。

# 72. 實驗六：QD-like Residual Archive

對 ground-truth toy domain 比較 single-objective 與 niche archive，看是否找到更多 non-target useful niches。

# 73. 實驗七：Human–AI Joint Curation

比較 human only、AI only、human+AI 的：

$$
R_{\mathrm{rare}},
F_D,
F_R.
$$

---

# 74. PGMV-02 可證偽假說

### H1

部分 target-search domain 存在：

$$
x\notin G_T
$$

但：

$$
V_{\mathrm{transfer}}(x)>0.
$$

### H2

target-only deletion policy 會漏掉可驗證 alternate value。

### H3

semantic quotient 可顯著降低 residual audit cost。

### H4

候選供應充足後，更多 generation iterations 不必然提高 residual epistemic fertility。

### H5

archive-aware / QD-style strategy 在部分 deceptive 或 open-ended domain 產生更多 useful niche discoveries。

如果這些假說在廣泛 benchmark 中失敗，Residual-aware policy 的工程必要性應下修。

---

# 75. 非主張總表

本文不主張：

1. 所有 target failure 都有價值；
2. 所有非目標 artifact 都應永久保存；
3. 無限猴子的垃圾本身具有文化價值；
4. 莎士比亞只是任意 target 而沒有歷史價值；
5. 文學品質能被單一客觀 metric 完整衡量；
6. Quality-Diversity 就是 PGMV residual theory；
7. MAP-Elites niche 可直接等同 semantic class；
8. Novelty Search 可取代 task objective；
9. high novelty 等於 high value；
10. semantic entropy 等於 creativity；
11. open-ended generation 等於無限亂數；
12. LLM 等於 open-ended evolutionary system；
13. non-target artifact 一定是 alternate success；
14. unknown 等於 valuable；
15. unknown 等於 noise；
16. hazard classification 不會誤判；
17. archive 越大越好；
18. compression 不會造成資訊損失；
19. embedding equivalence 可直接證明語義等價；
20. provenance 決定 artifact 全部價值；
21. 人類創作者未來必然只做 curator；
22. AI evaluator 可完全替代人類判斷；
23. rare-value artifact 可被可靠自動識別；
24. residual-aware policy 在所有 domain 都優於 target-only；
25. diversity 永遠比 quality 重要；
26. single objective 一定是錯誤設計；
27. 科學、藝術與政策可共用同一 value function；
28. residual corpus quotient 有唯一自然等價關係；
29. 一個非目標結果一定值得二次研究；
30. 本文已解決後生成文明的最終價值判定問題。

---

# 76. 形式命題一：Target-Value Non-Collapse

$$
\boxed{
J_T(x)=0
\not\Rightarrow
\mathbf V(x)=\mathbf 0.
}
$$

# 77. 形式命題二：Failure Relativity

$$
\boxed{
\operatorname{Fail}(x,T_1)
\not\Rightarrow
\operatorname{Fail}(x,T_2).
}
$$

# 78. 形式命題三：Raw–Effective Residual Separation

$$
\boxed{
N_R^{\mathrm{raw}}
\neq
N_R^{\mathrm{eff}}.
}
$$

# 79. 形式命題四：Novelty–Value Separation

$$
\boxed{
N(x)\uparrow
\not\Rightarrow
V(x)\uparrow.
}
$$

# 80. 形式命題五：Unknown Type Safety

$$
\boxed{
\operatorname{Unknown}(x)
\not\Rightarrow
\operatorname{Noise}(x)
}
$$

且：

$$
\boxed{
\operatorname{Unknown}(x)
\not\Rightarrow
\operatorname{Valuable}(x).
}
$$

# 81. 形式命題六：Archive Non-Monotonicity Candidate

$$
A_2\supset A_1
\not\Rightarrow
U_A(A_2)>U_A(A_1).
$$

# 82. 形式命題七：Alternative Success

存在：

$$
x,T,T'
$$

使：

$$
x\notin G_T,
\qquad
x\in G_{T'}.
$$

# 83. 形式命題八：Recognition Bottleneck

若：

$$
C_{\mathrm{gen}}
\ll
C_{\mathrm{recog}},
$$

提高 generation throughput 的邊際效益可能下降。

# 84. 形式命題九：Residual Budget Hypothesis

部分 domain 可能存在：

$$
B_R^\star>0
$$

使 residual-aware policy 長期總收益高於：

$$
B_R=0.
$$

# 85. 形式命題十：Evaluator First-Order Candidate

在候選供應充足的 regime 中：

$$
\frac{\partial U}{\partial E}
>
\frac{\partial U}{\partial N_{\mathrm{gen}}}
$$

可能成立；它是 empirical hypothesis，不是普遍定理。

---

# 86. 與 CI 的整合

CI 問：

$$
\text{Can we propose new structures?}
$$

PGMV-02 加：

> proposal 沒命中當前 Gap，不代表沒有其他價值。

因此 CI 應有 residual channel，而不只有 accept/delete。

# 87. 與 GCS 的整合

GCS 問：

$$
\text{Does }x\text{ reduce distance to }G_T?
$$

PGMV-02 加：

> 若沒有，它是否降低某個有價值 $G_{T'}$ 的距離？

# 88. 與 LSI 的整合

LSI 的 semantic quotient、route identity、higher-order recurrence 讓 residual archive 不被 surface explosion 淹沒。

# 89. PGMV 新增的東西

CI、GCS、LSI 都不能單獨決定：

$$
\boxed{
\text{Which residual deserves civilizational attention?}
}
$$

這是 PGMV 的 value layer。

# 90. 下一篇 PGMV-03

將正式研究：

$$
\boxed{
\text{Scarcity Migration of Meaning}.
}
$$

如果 residual corpus 中大量存在 alternate value，而 generation 本身快速變便宜，文明稀缺性便會從 production 更明顯地移往 judgment、attention、verification、integration、provenance 與 commitment。

---

# 91. 最終結論

傳統無限猴子問題有一個極度強烈的 target bias。

它把：

$$
T=\text{Hamlet}
$$

設成成功，

把所有：

$$
x\neq T
$$

壓成：

$$
0.
$$

作為精確概率題，這完全合理。作為生成文明的總體描述，卻遠遠不夠。

因為真正的大規模生成歷史中，非目標產物不是同質集合。它們可能是：

$$
\text{noise},
$$

$$
\text{duplicate},
$$

$$
\text{dangerous falsehood},
$$

$$
\text{new knowledge},
$$

$$
\text{failed proof with a reusable obstruction},
$$

甚至：

$$
\boxed{
\text{a direction more valuable than the original target}.
}
$$

所以本文拒絕：

$$
x\neq T
\Rightarrow
x\text{ worthless}.
$$

取而代之的是：

$$
\boxed{
x\neq T
\Rightarrow
x\text{ enters residual evaluation}.
}
$$

這使生成系統從：

$$
\text{winner-takes-all target search}
$$

升級成：

$$
\boxed{
\text{target search}
+
\text{residual discovery}
+
\text{semantic quotient}
+
\text{selective retention}.
}
$$

Quality-Diversity、Novelty Search 與 open-ended evolutionary work 提供了重要工程類比：搜尋系統不一定只能保存一個最優解；不同 niche 中的高品質候選可能具有獨立價值。2026 的生成創意研究又提醒，候選數量充足後，selection/evaluator architecture 可以比「再多生成幾輪」更重要。

所以無限猴子第二問最終不是：

> 猴子在莎士比亞以前打了多少垃圾？

而是：

$$
\boxed{
\textbf{How many undiscovered successes are hidden inside what a narrow objective calls failure?}
}
$$

當生成極度昂貴時，我們可以容忍只保存成功答案。

當生成極度廉價後，這個策略反而可能浪費真正稀缺的東西：

$$
\boxed{
\text{the ability to recognize a rare valuable artifact inside an overwhelming residual universe}.
}
$$

因此 PGMV-02 的最終兩條原則是：

$$
\boxed{
\textbf{A non-target artifact is not yet a failed artifact; it is an artifact whose value has not been exhausted by the current target function.}
}
$$

以及：

$$
\boxed{
\textbf{A mature post-generative intelligence must know both what not to generate again and what not to discard merely because it failed the current target.}
}
$$

---

# 參考文獻

1. Lehman, J., & Stanley, K. O. (2011). **Abandoning Objectives: Evolution Through the Search for Novelty Alone.** *Evolutionary Computation*, 19(2), 189–223. https://doi.org/10.1162/EVCO_a_00025

2. Mouret, J.-B., & Clune, J. (2015). **Illuminating Search Spaces by Mapping Elites.** arXiv:1504.04909.

3. Pugh, J. K., Soros, L. B., & Stanley, K. O. (2016). **Quality Diversity: A New Frontier for Evolutionary Computation.** *Frontiers in Robotics and AI*, 3.

4. Lim, B., Flageat, M., & Cully, A. (2024). **Large Language Models as In-context AI Generators for Quality-Diversity.** arXiv:2404.15794.

5. Faldor, M., & Cully, A. (2024). **Toward Artificial Open-Ended Evolution within Lenia using Quality-Diversity.** arXiv:2406.04235.

6. Templier, P., Grillotti, L., Rachelson, E., Wilson, D. G., & Cully, A. (2024). **Quality with Just Enough Diversity in Evolutionary Policy Search.** arXiv:2405.04308.

7. Anderson, R., Verhoef, T., & Zohrehvand, A. (2026). **Recipes for Creativity: Iterative Generation and Evaluation in Large Language Models.** arXiv:2608.07243.

8. Tan, M. S. et al. (2026). **Automated Creativity Evaluation of Language Models Across Open-Ended Tasks.** arXiv:2606.11762.

9. Yu, Y., Li, Y., Suri, S., & Counts, S. (2026). **From Searchable to Non-Searchable: Generative AI and Information Diversity in Online Information Seeking.** arXiv:2604.10258.

10. Rosen, Y., & Rushkin, I. (2026). **Measuring Creativity in the Age of Generative AI.** arXiv:2604.19799.

11. Baid, N. et al. (2025). **Guiding Evolution of Artificial Life Using Vision-Language Models.** arXiv:2509.22447.

12. Medina, A. et al. (2026). **Motif Diversity in Human Liver ChIP-seq Data Using MAP-Elites.** arXiv:2601.17808.

13. Donaghy, J. et al. (2026). **DEI: Diversity in Evolutionary Inference for Quality-Diversity Search.** arXiv:2605.27130.

14. Woodcock, S. et al. (2024). **A numerical evaluation of the Finite Monkeys Theorem.** *Franklin Open*. https://doi.org/10.1016/j.fraope.2024.100140

15. Neo.K × Aletheia (2026). **PGMV-01 — 無限猴子之後：當生成本身不再稀缺.**

16. Neo.K (2026). **概念積分 2.0：從 Gap 導向候選生成到型別守衛、驗證、黏合與原語提案.** EML-DEST-2026-08.

17. Neo.K with Aletheia (2026). **解空間幾何計算論 / Geometric Computation of Solution Spaces.** EML-GCS series.

18. Neo.K × Aletheia (2026). **邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics.** LSI-PSD Expanded v2.0 series.

---

## 附錄 A：Residual Artifact Schema

```yaml
artifact_id:
source:
generator:
target_id:
target_match:
target_distance:

classification:
  noise:
  duplicate:
  alternate_value:
  verified_knowledge:
  obstruction:
  bridge:
  hazard:
  unknown:

novelty:
  lexical:
  semantic:
  structural:
  functional:

quality:
  task:
  domain:
  evaluator:

verification:
  status:
  method:
  certificate:

transfer:
  candidate_targets:
  validated_targets:

provenance:
  parent:
  branch:
  timestamp:
  source_hash:

retention:
  action:
  compression:
  archive_class:
```

---

## 附錄 B：Residual Revaluation Pipeline

```text
NON-TARGET ARTIFACT
        |
        v
TYPE CLASSIFICATION
        |
        v
CANDIDATE SEMANTIC QUOTIENT
        |
        v
NOVELTY / QUALITY TRIAGE
        |
        +--> NOISE / DUPLICATE --> COMPRESS
        |
        +--> HAZARD -----------> ISOLATE / AUDIT
        |
        +--> UNKNOWN ----------> HOLD MINIMAL PROVENANCE
        |
        +--> ALTERNATE / BRIDGE / KNOWLEDGE
                  |
                  v
              VERIFY
                  |
                  v
              TRANSFER TEST
                  |
                  v
              LONG-TERM ARCHIVE
```

---

## 附錄 C：Target-only vs Residual-aware Policy

| Dimension | Target-only | Residual-aware |
|---|---|---|
| target efficiency | 高優先 | 高優先 |
| alternate discovery | 低 | 額外 budget |
| storage | 低 | 中 |
| audit cost | 低 | 較高 |
| transfer opportunity | 可能遺失 | 可保留 |
| duplicate risk | 低保存量 | 需 quotient |
| rare-value recall | 可能低 | 可優化 |

---

## 附錄 D：PGMV-02 核心分離原則

$$
\boxed{
\begin{aligned}
\text{Target Failure} &\neq \text{General Failure}\\
\text{Novelty} &\neq \text{Value}\\
\text{Unknown} &\neq \text{Noise}\\
\text{Diversity} &\neq \text{Quality}\\
\text{Generation Count} &\neq \text{Effective Discovery}\\
\text{Non-Target} &\neq \text{Non-Useful}.
\end{aligned}
}
$$

---

## 附錄 E：一句話版本

$$
\boxed{
\text{莎士比亞出現之前那些作品，不是因為「不是莎士比亞」就自動成為垃圾；它們首先只是尚未被另一套價值函數重新判定的非目標產物。}
}
$$

而後生成文明真正需要學會的是：

$$
\boxed{
\text{不要把當前任務的失敗，誤當成整個可能世界的無價值。}
}
$$
