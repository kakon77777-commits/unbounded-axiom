# 從動態圖到可執行符號系統
## ——自然語言作為世界狀態的 Rendering，而非 Canonical State

**Series:** Adaptive Epistemic Systems Series  
**Paper:** 3 / 11  
**Version:** v0.1  
**Language:** zh-TW  
**Status:** Complete Draft / Canonical UTF-8 Source

---

## 摘要

若一個自適應世界狀態系統只能保存節點、關係、可信度、新鮮度與更新張力，卻無法將其轉換成可操作、可計算、可交換與可表達的形式，那麼它仍然只是一個動態狀態庫，而不是完整的可執行智能架構。本文在前兩篇所提出的非對稱時空張力與動態新鮮度模型之上，引入一個可執行符號層，將世界狀態、命題、規則、事件、算法、外部系統與輸出表達統一映射為具有明確語義與操作規則的 canonical symbolic state。

本文核心主張是：自然語言不應被直接等同於系統內部的 canonical state。文字可以作為輸入，也可以作為輸出，但在內部應經過解析、正規化、語義綁定與來源標記，轉換為可比較、可驗證、可更新的符號結構。反之，最終文字輸出則應由內部符號狀態經 rendering 生成，而不是讓文字本身承擔所有推理、記憶與狀態一致性責任。

本文提出四層結構：世界狀態層、canonical 符號層、可執行操作層與 rendering 層；並進一步定義符號型別、命題結構、規則、操作契約、輸入正規化、輸出投影、自我生成內容的來源隔離與 round-trip consistency。本文同時分析自然語言作為內部主狀態所造成的歧義、同義異構、上下文依賴與自我污染問題，並提出將自然語言視為介面而非本體的架構原則。

在此框架下，文字、表格、程式碼、圖結構、數值、指令與外部動作都只是同一 canonical state 的不同輸出投影。由此，系統不再被限定為「文字生成器」，而成為一個可從多種輸入映射到統一內部狀態，再經計算與驗證後映射到多種輸出介面的自適應符號計算系統。

**關鍵詞：** canonical state、符號系統、自然語言 rendering、可執行語義、狀態正規化、輸入解析、輸出投影、來源隔離、round-trip consistency、自適應智能系統

---

## 1. 問題：世界狀態如何變成可計算的東西？

前兩篇建立了：

$$
\mathcal{G}_t
$$

作為動態世界狀態圖，並為節點配置：

$$
S_i,
F_i,
T_i,
I_i,
C_i
$$

等屬性。

但若系統只知道：

$$
v_i
$$

存在，卻不知道如何把：

$$
v_i
$$

轉換成可執行命題、條件、規則、查詢或輸出，那麼它仍缺少一個關鍵中介。

因此需要：

$$
\boxed{
\text{World State}
\rightarrow
\text{Symbolic State}
\rightarrow
\text{Executable Operation}
}
$$

。

令：

$$
Z_t
$$

表示時間 $$t$$ 的 canonical symbolic state。

則完整系統不再只有：

$$
\mathcal{G}_t
$$

而是：

$$
\mathfrak{S}_t
=
\left(
\mathcal{G}_t,
Z_t
\right)
$$

。

其中：

$$
\mathcal{G}_t
$$

描述「世界目前如何被系統表示」；

$$
Z_t
$$

描述「這些狀態如何被正式編碼、引用、計算與交換」。

---

## 2. 為什麼自然語言不能直接當 canonical state？

自然語言非常適合人類溝通，但不適合單獨承擔內部 canonical state。

原因至少有四個。

### 2.1 同義異構

不同句子可能表達近似相同內容：

$$
T_1\neq T_2
$$

但：

$$
Meaning(T_1)\approx Meaning(T_2)
$$

。

例如：

> A 導致 B。

與：

> B 是由 A 所造成。

文字不同，但核心關係接近：

$$
CAUSE(A,B)
$$

。

若內部直接保存文字，系統可能建立兩筆重複知識。

---

### 2.2 同形異義

相同文字在不同上下文可能代表不同內容：

$$
T_1=T_2
$$

但：

$$
Meaning(T_1\mid C_1)
\neq
Meaning(T_2\mid C_2)
$$

。

因此字串相等不能被當成語義相等。

---

### 2.3 省略與隱含

自然語言大量依賴省略：

> 他昨天改了。

系統必須知道：

$$
Who(\text{他})
$$

$$
What(\text{改了})
$$

$$
When(\text{昨天})
$$

才能形成可驗證狀態。

文字本身不足以提供完整 canonical semantics。

---

### 2.4 修辭與非字面語義

自然語言可能包含：

$$
\text{metaphor},
\text{irony},
\text{hyperbole},
\text{fiction},
\text{quotation}
$$

。

若所有文字都被直接寫入世界狀態，系統會把：

> 世界末日了。

與：

$$
WORLD\_END=True
$$

混為一談。

因此：

$$
\boxed{
\text{text}
\neq
\text{canonical world state}
}
$$

。

---

## 3. 四層架構

本文提出四層：

$$
\boxed{
W
\rightarrow
Z
\rightarrow
E
\rightarrow
R
}
$$

其中：

$$
W
$$

為 world-state layer；

$$
Z
$$

為 canonical symbolic layer；

$$
E
$$

為 executable operation layer；

$$
R
$$

為 rendering layer。

完整形式可寫成：

$$
\mathfrak{S}
=
(
W,
Z,
E,
R
)
$$

。

### 3.1 世界狀態層

保存：

$$
\mathcal{G}_t
=
(
V_t,
E_t,
W_t,
X_t,
B_t,
S_t,
T_t,
\Lambda_t,
I_t
)
$$

。

### 3.2 Canonical 符號層

保存可比較、可引用、可驗證的正式語義：

$$
Z_t
=
\{
z_1,
z_2,
\ldots,
z_n
\}
$$

。

### 3.3 可執行操作層

提供：

$$
\mathcal{O}
=
\{
op_1,
op_2,
\ldots,
op_m
\}
$$

使符號狀態可以被變換。

### 3.4 Rendering 層

將 canonical state 投影成：

$$
\text{text},
\text{table},
\text{code},
\text{graph},
\text{number},
\text{command},
\text{action}
$$

。

---

## 4. Canonical Symbolic State 的最小形式

一個 canonical symbol 可以寫成：

$$
z_i
=
(
id_i,
type_i,
value_i,
args_i,
context_i,
source_i,
confidence_i,
time_i,
status_i
)
$$

其中：

$$
id_i
$$

是穩定識別碼；

$$
type_i
$$

是型別；

$$
value_i
$$

是核心值；

$$
args_i
$$

是參數；

$$
context_i
$$

是上下文；

$$
source_i
$$

是來源；

$$
confidence_i
$$

是可信度；

$$
time_i
$$

是時間狀態；

$$
status_i
$$

表示 active、deprecated、hypothesis、verified 等狀態。

這樣同一個概念即使有不同自然語言表述，也可以指向同一個：

$$
id_i
$$

。

---

## 5. 符號型別

為避免所有節點都只是無型別字串，可以至少定義：

$$
\Sigma
=
\{
\Sigma_{\mathrm{entity}},
\Sigma_{\mathrm{relation}},
\Sigma_{\mathrm{event}},
\Sigma_{\mathrm{predicate}},
\Sigma_{\mathrm{rule}},
\Sigma_{\mathrm{quantity}},
\Sigma_{\mathrm{hypothesis}},
\Sigma_{\mathrm{algorithm}},
\Sigma_{\mathrm{system}}
\}
$$

。

例如：

$$
Person(Neo)
$$

可以是一個 entity；

$$
CAUSE(A,B)
$$

是一個 relation；

$$
Event(ChangeLaw,t)
$$

是一個 event；

$$
IF(A)\rightarrow B
$$

是一個 rule；

$$
Price(X,t)=100
$$

是一個 quantity。

不同型別允許不同更新與驗證規則。

---

## 6. 命題層

一個命題可表示為：

$$
p
=
Predicate(a_1,\ldots,a_n)
$$

。

例如：

$$
CEO(CompanyX,PersonY,t)
$$

。

這類命題可以附加：

$$
Confidence(p)
$$

$$
Freshness(p)
$$

$$
Source(p)
$$

$$
ValidTime(p)
$$

。

因此，系統不只保存：

> PersonY 是 CompanyX 的 CEO。

而是保存：

$$
p
=
CEO(CompanyX,PersonY,t)
$$

以及與其有效性相關的狀態。

---

## 7. 事件層

世界變化通常由事件驅動。

定義：

$$
e
=
Event(
type,
participants,
time,
location,
effects
)
$$

。

例如：

$$
e_1
=
Event(
Appointment,
CompanyX,
PersonY,
t_1
)
$$

。

事件經過規則可以產生狀態更新：

$$
e_1
\Rightarrow
CEO(CompanyX,PersonY,t\ge t_1)
$$

。

因此：

$$
\text{event}
$$

與：

$$
\text{state}
$$

必須區分。

事件是變化發生；

狀態是變化後世界如何被表示。

---

## 8. 規則層

可執行符號系統需要規則。

定義：

$$
r_i:
Pre_i
\rightarrow
Post_i
$$

。

例如：

$$
IF\;
Appointment(c,p,t)
\land
ValidAppointment(c,p)
$$

則：

$$
CEO(c,p,t^+)
$$

。

規則還可以加入：

$$
Invariant_i
$$

與：

$$
Failure_i
$$

。

因此完整規則可寫成：

$$
r_i
=
(
Pre_i,
Transform_i,
Post_i,
Invariant_i,
Failure_i
)
$$

。

這使規則不只是文字敘述，而是正式可執行結構。

---

## 9. 輸入不是直接寫入世界

定義輸入：

$$
I_t
$$

。

無論輸入來自：

$$
I_{\mathrm{text}},
I_{\mathrm{number}},
I_{\mathrm{image}},
I_{\mathrm{sensor}},
I_{\mathrm{system}}
$$

都不應直接寫入 canonical world state。

而應先經過：

$$
Parse
$$

$$
Normalize
$$

$$
Resolve
$$

$$
Validate
$$

。

即：

$$
I_t
\rightarrow
P_t
\rightarrow
N_t
\rightarrow
R_t
\rightarrow
V_t
\rightarrow
Z_t
$$

。

其中：

$$
P_t
$$

是 parsing；

$$
N_t
$$

是 normalization；

$$
R_t
$$

是 reference resolution；

$$
V_t
$$

是 validation。

---

## 10. 自然語言輸入的正規化

假設輸入：

> A 昨天可能造成了 B。

系統不應直接保存原句作為事實。

而應轉換為：

$$
Hypothesis(
CAUSE(A,B),
time=t-1d,
confidence=c
)
$$

其中：

$$
0<c<1
$$

。

如果「昨天」依賴使用者當下時間，則必須解析成絕對時間：

$$
t_{\mathrm{absolute}}
$$

。

因此：

$$
\text{surface text}
\rightarrow
\text{resolved symbolic proposition}
$$

是必要步驟。

---

## 11. Canonical State 與表面文字分離

令：

$$
\rho_{\mathrm{text}}
$$

表示文字 rendering 函數。

則：

$$
Text
=
\rho_{\mathrm{text}}
\left(
Z_q
\right)
$$

其中：

$$
Z_q
\subseteq Z
$$

是與查詢相關的 canonical symbolic substate。

因此：

$$
\boxed{
\text{text generation}
=
\text{state projection}
}
$$

而不是：

$$
\boxed{
\text{text generation}
=
\text{the entire reasoning process}
}
$$

。

這是本文最重要的架構分離之一。

---

## 12. 多重輸出投影

同一個 canonical state 可以有不同 rendering。

令：

$$
\rho_k
$$

表示第 $$k$$ 種輸出投影。

則：

$$
O_k
=
\rho_k(Z_q)
$$

。

例如：

$$
\rho_{\mathrm{text}}
$$

輸出文字；

$$
\rho_{\mathrm{table}}
$$

輸出表格；

$$
\rho_{\mathrm{graph}}
$$

輸出圖；

$$
\rho_{\mathrm{code}}
$$

輸出程式；

$$
\rho_{\mathrm{command}}
$$

輸出命令；

$$
\rho_{\mathrm{action}}
$$

輸出外部動作。

因此：

$$
\boxed{
Z
\rightarrow
\{O_1,O_2,\ldots,O_n\}
}
$$

。

文字只是其中之一。

---

## 13. Output-Time Validation

輸出前不應只問：

> 我能不能生成一句話？

而應問：

> 這句話引用的 canonical state 是否仍符合當前任務的新鮮度與可信度要求？

令：

$$
Deps(O)
$$

表示輸出 $$O$$ 所依賴的節點集合。

輸出前檢查：

$$
\forall v_i\in Deps(O),
\quad
F_i(t\mid q)\ge\theta_i^F
$$

以及：

$$
C_i\ge\theta_i^C
$$

。

若某節點不滿足：

$$
F_i<\theta_i^F
$$

則先觸發：

$$
Revalidate(v_i)
$$

。

因此：

$$
Q
\rightarrow
RelevantSubgraph
\rightarrow
FreshnessCheck
\rightarrow
SelectiveUpdate
\rightarrow
Render
$$

。

---

## 14. 查詢本身是一種局部喚醒

使用者問題：

$$
Q_t
$$

不只是要求文字輸出，也是一個動態喚醒事件。

定義：

$$
Rel(v_i,Q_t)
$$

表示節點與查詢的相關性。

則：

$$
T_i'(t)
=
T_i(t)
+
\alpha Rel(v_i,Q_t)
$$

。

因此查詢可以提高某些節點的更新張力。

這使系統不需要預先將整個世界更新至「完美最新」，而可以：

$$
\boxed{
\text{update on demand where the query makes freshness valuable}
}
$$

。

---

## 15. 可執行操作與符號狀態

操作函數：

$$
op_k
$$

接受 canonical symbolic state：

$$
op_k:
Z_{\mathrm{in}}
\rightarrow
Z_{\mathrm{out}}
$$

。

例如：

$$
Compare(a,b)
$$

$$
Infer(p_1,p_2)
$$

$$
Update(v_i)
$$

$$
Merge(v_i,v_j)
$$

$$
Verify(p)
$$

。

因此可執行層不需要依賴自然語言。

自然語言只是可能的：

$$
InputAdapter
$$

或：

$$
OutputAdapter
$$

。

---

## 16. 操作契約

每個操作應有明確契約：

$$
Contract(op_i)
=
(
Pre_i,
Post_i,
Invariant_i,
Failure_i
)
$$

。

例如：

$$
Pre_i
$$

規定輸入型別；

$$
Post_i
$$

規定正常輸出；

$$
Invariant_i
$$

規定執行期間不可破壞的狀態；

$$
Failure_i
$$

規定失敗形式。

這使系統可以在調用操作後驗證：

$$
Verify(Post_i)
$$

而不是只接受任意輸出。

---

## 17. 自我生成文字不能自動成為證據

如果系統輸出的文字可以再次被讀入，會形成：

$$
O_t
\rightarrow
I_{t+1}
$$

。

若沒有來源隔離，系統可能產生：

$$
\text{I generated X}
\Rightarrow
\text{X is evidence}
\Rightarrow
\text{I believe X more}
$$

的自我強化。

因此每個符號應標記：

$$
src(z)
\in
\{
external,
observed,
computed,
inferred,
self\_generated,
quoted
\}
$$

。

不同來源具有不同證據權重。

一般應避免：

$$
self\_generated
\equiv
external
$$

。

---

## 18. 自我引用與來源污染

若：

$$
z_1
$$

由系統自身生成，

再被當作新證據產生：

$$
z_2
$$

則需要追蹤：

$$
Prov(z_2)
\supseteq
Prov(z_1)
$$

。

這使系統可以辨認：

$$
z_2
$$

是否只是：

$$
z_1
$$

的再表述，而非獨立證據。

因此：

$$
\boxed{
\text{provenance must survive transformation}
}
$$

。

否則系統可能將一個來源經過十次改寫後誤認為十份獨立證據。

---

## 19. Round-Trip Consistency

若文字是 rendering，則可以檢驗：

$$
Z
\xrightarrow{\rho_{\mathrm{text}}}
T
\xrightarrow{\pi_{\mathrm{text}}}
\widehat{Z}
$$

其中：

$$
\pi_{\mathrm{text}}
$$

為文字解析器。

理想上：

$$
\widehat{Z}\approx Z
$$

。

這不要求逐字相同，而要求語義保持。

定義：

$$
D_Z(Z,\widehat{Z})
$$

為 canonical state distance。

則：

$$
D_Z(Z,\widehat{Z})<\epsilon
$$

表示 round-trip consistency 可接受。

這可以用來測試輸出 rendering 是否在語義上破壞內部狀態。

---

## 20. Lossy Rendering 是允許的

自然語言通常是壓縮表達。

因此不要求：

$$
\rho_{\mathrm{text}}
$$

保留所有內部資訊。

例如內部可能保存：

$$
Confidence=0.731
$$

$$
Freshness=0.842
$$

$$
SourceCount=17
$$

但文字只說：

> 目前證據中度支持此命題。

因此 rendering 可以是：

$$
Z
\rightarrow
T
$$

的有損投影。

但若使用者要求完整輸出，系統可以切換：

$$
\rho_{\mathrm{detailed}}
$$

。

關鍵不是所有 rendering 都無損，而是：

$$
\boxed{
\text{the canonical state is not lost merely because one rendering is compressed}
}
$$

。

---

## 21. 語言表達與世界承諾分離

輸出一句：

> A 很可能導致 B。

不應自動等同：

$$
CAUSE(A,B)=True
$$

。

更合理的是：

$$
OutputCommitment
=
(
Proposition,
Modality,
Confidence,
Scope
)
$$

。

例如：

$$
(
CAUSE(A,B),
Possible,
0.67,
Context=C
)
$$

。

這使「文字語氣」與「系統實際信念」可以被正式對齊。

---

## 22. 模態與認識論標記

canonical symbolic layer 應支持：

$$
True
$$

$$
False
$$

$$
Unknown
$$

$$
Possible
$$

$$
Probable
$$

$$
Hypothesis
$$

$$
Counterfactual
$$

$$
Fictional
$$

$$
Quoted
$$

等模態。

因此：

> 假設 A 發生，B 可能發生。

不應被寫成：

$$
A=True
$$

或：

$$
B=True
$$

。

而應表示為：

$$
Counterfactual(
A
\Rightarrow
Possible(B)
)
$$

。

---

## 23. 文字生成只是 Renderer，推理則可以完全不同

系統內部推理可以由：

$$
\text{graph traversal}
$$

$$
\text{logic}
$$

$$
\text{probability}
$$

$$
\text{optimization}
$$

$$
\text{algorithm execution}
$$

完成。

文字 rendering 只需要：

$$
\rho_{\mathrm{text}}:
Z_q
\rightarrow
T
$$

。

因此即使替換文字生成模組：

$$
\rho_{\mathrm{text}}^{(1)}
\rightarrow
\rho_{\mathrm{text}}^{(2)}
$$

只要：

$$
Z_q
$$

保持不變，系統的 canonical world state 仍然保持。

這是一個非常重要的架構測試。

---

## 24. 語言模組可替換性測試

令：

$$
L_1,
L_2,
L_3
$$

為不同語言模組。

若：

$$
Z_t^{(L_1)}
\approx
Z_t^{(L_2)}
\approx
Z_t^{(L_3)}
$$

且最終差異主要存在於：

$$
\rho_{\mathrm{text}}
$$

則代表語言模組不是 canonical state 的唯一持有者。

反之，若替換語言模組後：

$$
Z_t
$$

本身大量崩解或無法維持，則表示系統的高階狀態仍依賴語言模組。

這一測試將在後續智能架構比較中非常重要。

---

## 25. 從「生成答案」到「編譯答案」

當 canonical state 與 rendering 分離後，輸出過程可以被重新理解為：

$$
\boxed{
\text{compile a representation from verified state}
}
$$

。

也就是：

$$
Q
\rightarrow
Z_q
\rightarrow
Validate
\rightarrow
PlanRepresentation
\rightarrow
Render
$$

。

此時答案不是完全從空白生成，而是從已解析、已驗證的內部狀態編譯成使用者要求的表達形式。

---

## 26. 多語言不再代表多個世界模型

若 canonical state 與語言分離，則：

$$
\rho_{\mathrm{zh}}
$$

$$
\rho_{\mathrm{en}}
$$

$$
\rho_{\mathrm{ja}}
$$

可以對同一：

$$
Z_q
$$

進行不同 rendering。

因此：

$$
Z_q
\rightarrow
\{
Text_{\mathrm{zh}},
Text_{\mathrm{en}},
Text_{\mathrm{ja}}
\}
$$

。

這意味著多語言能力理論上不必維護多套完全獨立世界狀態。

---

## 27. 符號層與圖層的雙向映射

定義：

$$
\phi:
\mathcal{G}
\rightarrow
Z
$$

將世界圖映射成 canonical symbol；

以及：

$$
\psi:
Z
\rightarrow
\mathcal{G}
$$

將符號更新重新寫回世界圖。

理想上：

$$
\psi(\phi(\mathcal{G}))
\approx
\mathcal{G}
$$

。

這提供另一個 consistency test：

$$
D_G
\left(
\mathcal{G},
\psi(\phi(\mathcal{G}))
\right)
<
\epsilon
$$

。

---

## 28. 狀態變更必須先驗證再提交

新的符號狀態：

$$
Z'
$$

不應自動覆寫：

$$
Z
$$

。

而應經過：

$$
Candidate
\rightarrow
Validate
\rightarrow
Commit
$$

。

即：

$$
Z_t
\xrightarrow{op}
Z_{t+1}^{\mathrm{candidate}}
$$

若：

$$
Validate
\left(
Z_{t+1}^{\mathrm{candidate}}
\right)
=True
$$

才：

$$
Commit
\left(
Z_{t+1}^{\mathrm{candidate}}
\right)
$$

。

否則：

$$
Rollback
$$

或保持 hypothesis 狀態。

這使符號層具有 transactional semantics。

---

## 29. Canonical State 的不變量

至少可以要求：

### 29.1 識別一致性

$$
id_i=id_i
$$

不能因 rendering 改變而改變。

### 29.2 型別一致性

若：

$$
type(z_i)=Quantity
$$

則不能突然在無轉換規則下成為：

$$
Person
$$

。

### 29.3 來源可追溯

$$
Prov(z_i)\neq\varnothing
$$

對外部事實節點應盡可能成立。

### 29.4 時間語義明確

$$
ValidTime(z_i)
$$

與：

$$
ObservedTime(z_i)
$$

應區分。

### 29.5 Rendering 不改寫真值

$$
\rho_k
$$

只能投影，不應自行改變 canonical commitment。

---

## 30. 可驗證命題

### 命題一：Canonical State 可降低同義重複

若語言表達先經正規化：

$$
DuplicateRate_{\mathrm{canonical}}
<
DuplicateRate_{\mathrm{raw-text}}
$$

應在多樣化表述輸入中成立。

### 命題二：來源隔離可降低自我強化污染

若自生成內容與外部證據具有不同 provenance：

$$
FalseConfidence_{\mathrm{isolated}}
<
FalseConfidence_{\mathrm{untracked}}
$$

應在自我引用測試中成立。

### 命題三：Output-Time Validation 可降低過時回答

若輸出前進行相關節點新鮮度檢查：

$$
StaleAnswerRate_{\mathrm{validated}}
<
StaleAnswerRate_{\mathrm{direct}}
$$

。

### 命題四：Renderer 可替換性

若系統狀態真正獨立於語言 renderer，則替換：

$$
\rho_{\mathrm{text}}
$$

不應造成：

$$
D_Z(Z_t,Z_t')\gg0
$$

。

### 命題五：Round-Trip 可作為語義保持測試

不同 rendering / parsing 配對之：

$$
D_Z(Z,\widehat{Z})
$$

應可被量化，並用於比較語言接口品質。

---

## 31. 最小實驗

建立 canonical symbolic set：

$$
Z^\ast
$$

其中包含：

- 事實；
- 假設；
- 時間條件；
- 因果關係；
- 不確定性；
- 引用；
- 反事實。

生成多組不同自然語言 rendering：

$$
T_1,\ldots,T_n
$$

再解析回：

$$
\widehat{Z}_1,\ldots,\widehat{Z}_n
$$

。

測量：

$$
D_Z
\left(
Z^\ast,
\widehat{Z}_i
\right)
$$

。

同時比較：

$$
\text{raw text memory}
$$

與：

$$
\text{canonical symbolic memory}
$$

在長期重複輸入、同義改寫、語境切換與自我引用下的狀態一致性。

---

## 32. 與傳統文字中心系統的核心差異

文字中心系統可抽象為：

$$
Context
\rightarrow
Text
$$

。

本文系統則是：

$$
Input
\rightarrow
Parse
\rightarrow
CanonicalState
\rightarrow
Compute
\rightarrow
Validate
\rightarrow
Render
\rightarrow
Output
$$

。

因此：

$$
\boxed{
\text{language is an interface to intelligence, not necessarily the state substrate of intelligence}
}
$$

。

這不否認語言本身可以承載大量推理，而只是拒絕將：

$$
\text{surface linguistic sequence}
$$

直接等同於：

$$
\text{entire internal epistemic state}
$$

。

---

## 33. 從單一輸出系統到多介面世界模型

若：

$$
Z
$$

是 canonical state，

則同一內部狀態可以支援：

$$
Z
\rightarrow
Text
$$

$$
Z
\rightarrow
Code
$$

$$
Z
\rightarrow
Graph
$$

$$
Z
\rightarrow
Command
$$

$$
Z
\rightarrow
Action
$$

。

因此能力提升不只來自「更會寫文字」，也來自：

$$
\text{more precise state representation}
$$

與：

$$
\text{more reliable state-to-interface compilation}
$$

。

---

## 34. 最小完整循環

將前三篇統合後，一次完整循環可以寫成：

$$
I_t
\rightarrow
Parse
\rightarrow
Resolve
\rightarrow
Z_t
\rightarrow
\mathcal{G}_t
\rightarrow
T_t
\rightarrow
Activate
\rightarrow
U^\ast
\rightarrow
Z_{t+1}^{\mathrm{candidate}}
\rightarrow
Validate
\rightarrow
Commit
\rightarrow
\rho_k
\rightarrow
O_t
$$

。

其中：

$$
T_t
$$

控制哪些世界區域需要被重新喚醒；

$$
U^\ast
$$

選擇適用的更新操作；

$$
Validate
$$

阻止未驗證狀態直接污染 canonical source；

$$
\rho_k
$$

只負責輸出表達。

---

## 35. 結論

當世界狀態系統需要真正支援輸入、計算、更新與輸出時，單純的動態圖仍不足夠。

系統需要一個：

$$
\boxed{
\text{canonical executable symbolic layer}
}
$$

。

自然語言可以是極強大的輸入與輸出介面，但不應自動成為：

$$
\boxed{
\text{the canonical source of world state}
}
$$

。

因此本文提出：

$$
\text{World State}
\rightarrow
\text{Canonical Symbolic State}
\rightarrow
\text{Executable Operations}
\rightarrow
\text{Rendering}
$$

的四層結構。

其中：

$$
\boxed{
Text
=
Rendering(Z)
}
$$

而不是：

$$
\boxed{
Z
=
Text
}
$$

。

這一分離帶來幾個重要效果：

$$
\text{same meaning}
\Rightarrow
\text{same canonical identity}
$$

$$
\text{different language}
\Rightarrow
\text{different rendering, same state}
$$

$$
\text{self-generated text}
\not\Rightarrow
\text{external evidence}
$$

$$
\text{stale dependency}
\Rightarrow
\text{revalidate before output}
$$

以及：

$$
\text{renderer replacement}
\not\Rightarrow
\text{world-state replacement}
$$

。

因此，文字輸出不再是整個系統智能的唯一中心，而只是世界狀態的一種可交換表示。

這使後續研究能進一步處理更大的問題：當世界狀態與符號層可以持續擴張時，系統能力是否能藉由增加有效節點、關係、抽象與世界事實而擴張？而這種擴張究竟會形成真正新的智能結構，還是最終再次收斂到現有 AI 的工程形態？

---

## 附錄 A：核心映射

輸入解析：

$$
\pi_k:
I_k
\rightarrow
Z
$$

世界圖映射：

$$
\phi:
\mathcal{G}
\rightarrow
Z
$$

狀態回寫：

$$
\psi:
Z
\rightarrow
\mathcal{G}
$$

輸出 rendering：

$$
\rho_k:
Z
\rightarrow
O_k
$$

完整介面：

$$
I_k
\xrightarrow{\pi_k}
Z
\xrightarrow{op}
Z'
\xrightarrow{\rho_j}
O_j
$$

。

---

## 附錄 B：最小 Canonical Symbol Schema

$$
z_i
=
(
id_i,
type_i,
value_i,
args_i,
context_i,
source_i,
confidence_i,
freshness_i,
validTime_i,
observedTime_i,
status_i
)
$$

。

建議最小 invariant：

$$
id_i\neq\varnothing
$$

$$
type_i\neq\varnothing
$$

$$
source_i\neq\varnothing
$$

對外部事實節點成立；

並且任何 canonical commit 都必須經過：

$$
Candidate
\rightarrow
Validate
\rightarrow
Commit
$$

而非：

$$
Input
\rightarrow
DirectWrite
$$

。

---

## 附錄 C：最小輸出驗證流程

對查詢 $$Q$$：

$$
Q
\rightarrow
Z_Q
$$

取得相關 canonical state。

對所有：

$$
z_i\in Z_Q
$$

檢查：

$$
Freshness_i\ge\theta_i^F(Q)
$$

$$
Confidence_i\ge\theta_i^C(Q)
$$

若不成立：

$$
Revalidate(z_i)
$$

。

最後：

$$
Output
=
\rho_k
\left(
Z_Q^{\mathrm{validated}}
\right)
$$

。

這使輸出不只是生成，而是：

$$
\boxed{
\text{validated state compilation}
}
$$

。
