# RLMM-02：複合語義與認知操作的可組合性
## Compositional Semantics and the Composability of Cognitive Operations

**系列：Recursive Linguistic Metacognition Methodology（RLMM）／遞歸語言元認知方法論**  
**版本：v0.1**  
**日期：2026-08-20**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

RLMM-01 提出：語言不只是認知內容的表示媒介，也可以作為顯式、可修正的元認知介面。若此命題成立，下一個立即出現的問題是：語言化的認知操作是否能像語義結構、程式函數或形式算子一樣被組合、嵌套與重用？

本文提出「複合語義—認知操作可組合性」框架，區分四個層次：文字串接（textual concatenation）、語義組合（semantic composition）、操作組合（operational composition）與遞歸組合（recursive composition）。本文主張，只有當多個語言單元的組合能產生穩定的輸入條件、操作次序、狀態轉移、失敗條件與展開契約時，才應視為新的認知操作結構，而非單純更長的文字。

本文進一步提出：認知操作的可組合性不是無條件的。兩個局部合理的操作，在組合後可能產生衝突、環路、過度保守、無限延後、資訊重複與錯誤放大。因此 RLMM 需要一個操作代數層，描述順序、條件、並行、分支、遞歸與停止。本文建立第一版自然語言操作語法，並提出「可展開、可執行、可檢查、可中止、可替換」五項組合判準，作為未來 RLMM Language Protocol 與元認知算子結晶的基礎。

---

## 關鍵詞

RLMM；複合語義；認知操作；可組合性；元認知算子；遞歸；操作代數；自然語言協議；語義結晶；方法論

---

# 1. 從「一句話能改變思考」到「多個操作能不能組合」

RLMM-01 的核心結論可以寫成：

$$
\boxed{
\text{Language}
\rightarrow
\text{Metacognitive Operation}
}
$$

例如：

> 列出目前結論的隱含假設。

可以對應到：

$$
O_1=\operatorname{ExposeAssumption}.
$$

又例如：

> 為每個假設建立至少一個獨立反例路徑。

可以對應到：

$$
O_2=\operatorname{GenerateCounterexample}.
$$

問題立刻出現：

> 如果把 $O_1$ 與 $O_2$ 放在一起，是否就形成一個更高階的新操作？

直覺上可以寫：

$$
O_2\circ O_1.
$$

但這個符號本身還不夠。

因為「把兩句話接在一起」與「形成一個穩定的新認知程序」並不是同一件事。

因此本文首先區分：

$$
\boxed{
\text{Textual Concatenation}
\neq
\text{Operational Composition}
}
$$

---

# 2. 四層組合：從文字到遞歸操作

RLMM 將複合語言分成四個層級。

---

## 2.1 第一層：文字串接

最弱的組合形式是：

$$
L_1 + L_2.
$$

例如：

> 列出假設。  
> 尋找反例。

這只表示兩段文字被放在一起。

它並沒有自動定義：

- 哪一步先做；
- 第二步使用第一步的什麼輸出；
- 若第一步失敗，第二步是否還執行；
- 何時停止；
- 是否允許回頭修改第一步。

因此：

$$
\boxed{
L_1+L_2
\not\Rightarrow
O_2\circ O_1
}
$$

---

## 2.2 第二層：語義組合

若兩段語言之間存在可理解的語義關係：

> 先找假設，再對每個假設找反例。

則它形成：

$$
S(L_1,L_2),
$$

其中第二段的語義依賴第一段輸出。

此時已經不只是字串相鄰，而是：

$$
\text{Assumptions}
\rightarrow
\text{Counterexample Search}.
$$

但這仍然不必然等於一個可執行的完整操作。

---

## 2.3 第三層：操作組合

真正的操作組合要求：

$$
O_1:C\rightarrow C_1
$$

$$
O_2:C_1\rightarrow C_2.
$$

因此：

$$
O_{2\circ1}
=
O_2\circ O_1
$$

而：

$$
O_{2\circ1}:C\rightarrow C_2.
$$

例如：

$$
\operatorname{CounterAssumptions}
=
\operatorname{GenerateCounterexample}
\circ
\operatorname{ExposeAssumption}.
$$

這時新的複合操作具有：

- 可辨識輸入；
- 明確中間狀態；
- 明確輸出；
- 明確失敗位置。

這才真正進入 RLMM 的操作層。

---

## 2.4 第四層：遞歸組合

更高階的組合不是單純：

$$
O_1\rightarrow O_2\rightarrow O_3.
$$

而是：

$$
O_i
\rightarrow
\mathcal M(O_i)
\rightarrow
O_i'.
$$

也就是操作本身被另一個操作檢查、改寫或升階。

例如：

> 尋找反例。

如果反例搜尋一直只在同一資料源中進行，則對反例搜尋本身執行：

$$
\operatorname{CheckIndependence}
(
\operatorname{GenerateCounterexample}
).
$$

因此：

$$
\boxed{
\text{Recursive Composition}
=
\text{Operations acting on operations.}
}
$$

這是 RLMM 真正與一般工作流不同的地方。

---

# 3. 認知操作的基本型別

為了讓語言化方法可組合，必須先區分操作型別。

第一版 RLMM 可以使用五類基本操作。

---

## 3.1 Transform

改變認知內容：

$$
T:C\rightarrow C'.
$$

例如：

$$
\operatorname{Reframe}(C).
$$

---

## 3.2 Extract

從認知內容中抽取結構：

$$
E:C\rightarrow X.
$$

例如：

$$
\operatorname{ExtractAssumptions}(C)
=
A.
$$

---

## 3.3 Evaluate

對認知狀態進行判定：

$$
V:C\rightarrow D,
$$

其中 $D$ 是某種判定值。

例如：

$$
\operatorname{CheckEvidenceIndependence}(C)
\rightarrow
\{\text{pass},\text{fail},\text{uncertain}\}.
$$

---

## 3.4 Query

產生新的資訊需求：

$$
Q:C\rightarrow q.
$$

並透過環境或工具得到：

$$
q\rightarrow E.
$$

---

## 3.5 Control

決定下一步做什麼：

$$
K:C\rightarrow O_i.
$$

例如：

$$
\operatorname{RecurseOrStop}(C)
\rightarrow
\{\operatorname{Meta},\operatorname{Stop}\}.
$$

這五類操作共同構成第一版：

$$
\boxed{
\mathcal O
=
\{T,E,V,Q,K\}.
}
$$

---

# 4. 組合不是自由的：需要型別相容

若：

$$
O_1:C\rightarrow A
$$

而：

$$
O_2:E\rightarrow C',
$$

則 $O_2\circ O_1$ 可能根本沒有定義。

因此：

$$
\boxed{
\operatorname{codomain}(O_1)
\sim
\operatorname{domain}(O_2)
}
$$

是操作組合的基本條件。

自然語言中這個問題常被隱藏。

例如：

> 「列出假設，然後驗證證據。」

若「驗證證據」需要的是 evidence graph，而不是 assumptions list，則這兩步其實沒有直接資料接口。

因此成熟的 RLMM 不只要寫：

> 做 A，再做 B。

而要寫：

> A 的輸出中哪一部分成為 B 的輸入？

這可表示為：

$$
O_2\circ P\circ O_1,
$$

其中 $P$ 是一個中間投影或轉換。

---

# 5. 五項「真正組合」判準

一個語言複合結構若要被視為新的元認知算子，至少應滿足五個條件。

---

## 5.1 可展開性（Expandability）

壓縮後的操作名稱必須能展開回足夠完整的方法。

例如：

$$
\operatorname{IndependentChallenge}
$$

不能只是個標題。

它至少應能展開為：

1. 找出目前主要證據；
2. 建立 provenance graph；
3. 判斷是否存在共同來源；
4. 搜尋真正獨立來源；
5. 比較結果；
6. 在衝突時保留分支而非強制合併。

因此：

$$
\boxed{
\operatorname{Expand}(O_c)
\approx
[O_1,\ldots,O_n].
}
$$

---

## 5.2 可執行性（Executability）

操作必須能改變後續認知流程。

也就是：

$$
\mathcal E(O,C)\neq C
$$

在合理輸入下至少有可能成立。

如果一個算子永遠只產生漂亮敘述，而不改變：

- evidence selection；
- branching；
- confidence；
- decision；
- query；

那它不是有實質作用的認知操作。

---

## 5.3 可檢查性（Inspectability）

複合操作必須能被拆開檢查：

$$
O_c
=
O_n\circ\cdots\circ O_1.
$$

若失敗，至少應能回答：

> 是哪一步失敗？

否則組合會變成新的黑箱。

---

## 5.4 可中止性（Interruptibility）

成熟的複合操作不能只有：

$$
START\rightarrow\cdots\rightarrow END.
$$

它必須允許：

$$
\operatorname{STOP},
\quad
\operatorname{PAUSE},
\quad
\operatorname{BRANCH},
\quad
\operatorname{ROLLBACK}.
$$

尤其元認知流程很容易陷入：

$$
\text{inspect}
\rightarrow
\text{inspect inspection}
\rightarrow
\text{inspect inspection of inspection}
\rightarrow\cdots
$$

因此每個複合操作都需要局部停止條件。

---

## 5.5 可替換性（Substitutability）

如果一個子操作：

$$
O_i
$$

被證明不適合某環境，應能替換為：

$$
O_i'
$$

而不必重寫整個方法。

因此：

$$
O_c
=
O_3\circ O_2\circ O_1
$$

應允許：

$$
O_c'
=
O_3\circ O_2'\circ O_1.
$$

這使 RLMM 具有版本化與局部修正能力。

---

# 6. 複合操作的基本語法

RLMM 可以先用自然語言對應幾種基本控制結構。

---

## 6.1 Sequence

$$
O_1;O_2
$$

自然語言：

> 先做 $O_1$，再做 $O_2$。

---

## 6.2 Conditional

$$
\operatorname{IF}(D)
\{O_1\}
\operatorname{ELSE}
\{O_2\}
$$

自然語言：

> 如果證據獨立性不足，尋找新來源；否則進入下一階段。

---

## 6.3 Parallel

$$
O_1\parallel O_2.
$$

自然語言：

> 同時建立支持路徑與反例路徑。

這比先做支持、再做反例更能降低順序偏誤。

---

## 6.4 Loop

$$
\operatorname{WHILE}(D)\{O\}.
$$

自然語言：

> 在主要不確定來源仍未被區分前，持續尋找最有辨識力的證據。

但必須附：

$$
\operatorname{StopCondition}.
$$

---

## 6.5 Branch

$$
C
\rightarrow
\{C_1,C_2,\ldots,C_n\}.
$$

自然語言：

> 如果兩個模型目前都無法排除，保留兩個分支，不強迫過早合併。

---

## 6.6 Meta

$$
\mathcal M(O).
$$

自然語言：

> 如果同一操作反覆失敗，把該操作本身變成下一輪分析對象。

---

# 7. 「複合語言」什麼時候真的產生新結構？

這是本文最核心的判準。

設兩個語言操作：

$$
L_A,\quad L_B.
$$

如果只是：

$$
L_A+L_B,
$$

則只有表面增長。

但若組合後產生：

1. 新的輸入條件；
2. 新的狀態轉移；
3. 新的分支邏輯；
4. 新的停止條件；
5. 新的可重用行為；

則：

$$
\boxed{
\operatorname{Compose}(L_A,L_B)
=
O_{AB}
}
$$

其中：

$$
O_{AB}
\neq
O_A+O_B
$$

在操作意義上是一個新的結構。

例如：

### A

> 找出目前假設。

### B

> 尋找反例。

若只是放在一起：

> 找假設。找反例。

結構仍很弱。

但如果變成：

> 對每個會改變最終結論的假設，生成一個最小反例；如果某假設沒有可區分的反例路徑，標記為當前不可驗證；只對可區分假設進一步查證。

則已產生：

- relevance filter；
- per-assumption loop；
- falsifiability classification；
- routing rule。

這就是新的複合元認知操作。

---

# 8. 組合也會製造新的失敗模式

「可組合」不代表「組合後一定更好」。

這點非常重要。

---

## 8.1 局部正確，全域錯誤

可能有：

$$
O_1=\text{合理}
$$

$$
O_2=\text{合理}
$$

但：

$$
O_2\circ O_1=\text{有害}.
$$

例如：

> 高風險時增加驗證。

與：

> 不確定時延後決策。

各自合理。

但若串接成：

> 高風險 → 更多驗證 → 更高不確定 → 延後 → 再驗證 → 再延後。

就可能形成：

$$
\boxed{
\text{Abstention Loop}
}
$$

---

## 8.2 重複計數

兩個「獨立檢查」若實際依賴同一 provenance root：

$$
O_A,O_B
$$

表面上是兩條路徑，實際上：

$$
\operatorname{Source}(O_A)
=
\operatorname{Source}(O_B).
$$

因此：

$$
2\text{ checks}
\neq
2\text{ independent checks}.
$$

---

## 8.3 遞歸爆炸

若每個操作都要求：

> 再檢查這個操作是否可靠。

則：

$$
O
\rightarrow
\mathcal M(O)
\rightarrow
\mathcal M^2(O)
\rightarrow\cdots
$$

可能無限增長。

所以遞歸操作必須帶：

$$
\boxed{
\operatorname{RecurseBudget}.
}
$$

---

## 8.4 保守性放大

多個安全操作組合後可能產生：

$$
\text{Reject}
+
\text{Defer}
+
\text{Challenge}
+
\text{RequireMoreEvidence}
$$

最後得到：

$$
\boxed{
\text{Safe but unusable cognition}.
}
$$

因此 RLMM 必須評估組合後的全域行為，而不是只看每個局部規則是否合理。

---

# 9. 認知操作的代數視角

因此 RLMM 未來可以把元認知方法表示成一個操作代數：

$$
\mathfrak O
=
(
\mathcal O,
\circ,
\parallel,
\oplus,
\mathcal M,
\operatorname{Stop}
).
$$

其中：

- $\circ$：順序組合；
- $\parallel$：並行組合；
- $\oplus$：條件分支；
- $\mathcal M$：升階／反身算子；
- $\operatorname{Stop}$：終止。

一個方法可以寫成：

$$
P
=
\operatorname{Stop}
\circ
\operatorname{Update}
\circ
\operatorname{Inquire}
\circ
\operatorname{Challenge}
\circ
\operatorname{Inspect}
\circ
\operatorname{Externalize}.
$$

但實際上通常不是線性鏈，而更像：

$$
P:C
\rightarrow
G(C),
$$

其中 $G(C)$ 是一個動態認知圖。

所以：

$$
\boxed{
\text{RLMM method}
\approx
\text{dynamic cognitive graph}
}
$$

而非固定 checklist。

---

# 10. 自然語言作為「弱型別認知程式」

自然語言與程式語言不同。

它具有：

- 歧義；
- 隱含前提；
- 上下文依賴；
- 非固定執行語義。

因此不能說：

$$
\text{Natural Language}
=
\text{Programming Language}.
$$

但在方法論層，可以更保守地說：

$$
\boxed{
\text{Natural-language metacognitive protocol}
\approx
\text{weakly typed cognitive program}.
}
$$

它不是精確執行碼，但可以提供：

- 操作名稱；
- 輸入預期；
- 輸出預期；
- 執行順序；
- 分支規則；
- 失敗條件；
- 停止條件。

這使它足以成為人類與 AI 共享的中間層。

---

# 11. 組合的語言模板

第一版 RLMM 可以直接提供幾個自然語言模板。

---

## Template A — Sequential Composition

> 先【操作 A】；把其輸出中【欄位 X】作為【操作 B】的輸入；若 A 無法產生 X，停止並回報失敗原因。

---

## Template B — Conditional Composition

> 執行【判定 D】。若 D 成立，執行【操作 A】；若 D 不成立，執行【操作 B】；若 D 不可判定，進入【操作 C】。

---

## Template C — Independent Parallelism

> 以互不共享主要證據來源的兩條路徑同時處理問題；最後只比較結果，不共享中間推理。

---

## Template D — Reflexive Lift

> 若同一類失敗在【操作 O】中重複出現至少 $n$ 次，把 O 本身變成新的分析對象，而不是再次執行 O。

---

## Template E — Bounded Recursion

> 只有當下一階元認知預期能產生新的可操作區分時才升階；若只是重述已知限制，停止。

---

# 12. 組合品質的第一版評分

未來可建立一個簡單的組合品質向量：

$$
Q(O)
=
(
E_x,
X_e,
I_n,
S_t,
R_u
)
$$

其中：

- $E_x$：Expandability，可展開性；
- $X_e$：Executability，可執行性；
- $I_n$：Inspectability，可檢查性；
- $S_t$：Stoppability，可停止性；
- $R_u$：Reusability，可重用性。

只有當：

$$
Q(O)
$$

在主要維度上超過最低標準時，才值得把一段複合自然語言「結晶」成新的元認知算子。

這避免：

> 每寫一大段方法，就創一個新名詞。

真正的算子必須有結構價值。

---

# 13. 與語義結晶的重新連接

這一點讓 RLMM 與最早的 SCL 問題重新閉合。

最早的問題是：

$$
\text{長語義}
\rightarrow
\text{短符號}
$$

是否能保留可恢復結構。

現在 RLMM 對方法做同樣的事：

$$
\text{Long Metacognitive Procedure}
\rightarrow
\text{Composite Operation}
\rightarrow
\text{Crystallized Operator}.
$$

因此：

$$
\boxed{
\text{Semantic Crystallization}
\subset
\text{Metacognitive Crystallization}
}
$$

至少在方法論工程上，可以把前者看成後者的基礎。

但同樣必須記住：

$$
\boxed{
\text{Name}
\neq
\text{Operator}.
}
$$

只有當新符號能穩定喚回組合結構時，才真正形成新基底。

---

# 14. RLMM Case Corpus 的用途

過去實驗現在可以作為「組合失敗」的具體案例。

例如：

### Case A — Persistence + Agreement

表面上：

$$
\text{Persistence}
+
\text{Consensus}
$$

似乎都合理。

但組合後可能形成：

$$
\text{Persistent False Consensus}.
$$

---

### Case B — Safety + Defer

兩個局部安全操作：

$$
\text{Risk Awareness}
+
\text{Defer}
$$

可能形成：

$$
\text{Abstention Attractor}.
$$

---

### Case C — Hard Autonomy + Safety

加入：

$$
\text{Deferral Budget}
$$

後雖然打破 abstention，卻可能形成：

$$
\text{Over-Rejection}.
$$

因此：

$$
\boxed{
\text{Composition creates emergent failure modes.}
}
$$

這也是 RLMM 為什麼需要自己的 Case Corpus。

---

# 15. 由組合進入遞歸方法論

只要認知操作可以：

1. 被語言表示；
2. 被組合；
3. 被重新當成對象；

那麼遞歸方法論就自然出現。

設：

$$
P_0
=
O_3\circ O_2\circ O_1.
$$

如果 $P_0$ 失敗：

$$
\mathcal M(P_0)
$$

可以分析：

- 是 $O_1$ 失敗；
- 是 $O_2$ 失敗；
- 是接口失敗；
- 是順序失敗；
- 是全域交互作用失敗；
- 還是停止條件失敗。

然後生成：

$$
P_1.
$$

因此：

$$
\boxed{
P_{t+1}
=
\operatorname{Revise}(P_t,F_t).
}
$$

這就是方法論的版本化遞歸。

---

# 16. 邊界與非主張

本文不主張：

1. 自然語言具有形式程式語言同等精確性；
2. 任意兩個認知操作都可安全組合；
3. 局部有效操作組合後必然有效；
4. 認知操作一定具有單一固定輸入／輸出型別；
5. 所有元認知程序都應壓縮成短符號；
6. 所有複合語言都構成新認知結構；
7. 操作代數已經完備；
8. 人類與不同 AI 對同一語言操作具有完全相同執行語義。

本文只提出：

$$
\boxed{
\text{Metacognitive operations can be compositionally structured,
but composition requires explicit contracts and global evaluation.}
}
$$

---

# 17. 結論

語言化的元認知操作若要形成真正的方法論，就不能只是一串建議。

它必須能從：

$$
\text{Sentence}
$$

進一步成為：

$$
\text{Operation}
$$

再形成：

$$
\text{Composite Operation}
$$

最後才可能成為：

$$
\text{Recursive Method}.
$$

因此整條鏈為：

$$
\boxed{
\text{Text}
\rightarrow
\text{Semantic Structure}
\rightarrow
\text{Cognitive Operation}
\rightarrow
\text{Composite Operation}
\rightarrow
\text{Recursive Methodology}
}
$$

而「真正的組合」至少要求：

$$
\boxed{
\text{Expandable}
+
\text{Executable}
+
\text{Inspectable}
+
\text{Interruptible}
+
\text{Substitutable}.
}
$$

最重要的是：

> **可組合性不是免費增益。**

新的操作結構會產生新的能力，也會產生新的失敗模式。

因此成熟的 RLMM 不只是教認知主體：

> 怎麼把方法組合起來。

還必須教：

> 怎麼檢查組合本身是否創造了新的問題。

這正是下一篇的入口。

---

# 下一篇

**RLMM-03：從語義結晶到元認知算子**  
**From Semantic Crystallization to Metacognitive Operators**

下一篇將正式處理：一段成熟、可組合的自然語言元認知程序，何時可以被壓縮成可重用的操作名稱、符號或算子；其展開契約、語義不變量與 anti-pointer gate 應如何定義，從而把最早的語義結晶研究完整接回 RLMM。
