# DOM-02｜移動未知邊界：Unknown State、Unknown Type 與相對終端

## Moving Unknown Boundaries: Unknown States, Unknown Types, and Certified Relative Terminality

**系列：** Dynamic Operational Metaphysics（DOM）／動態可操作形而上學  
**篇次：** 02 / 08  
**文件編號：** EML-DOM-02-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-20  
**版本：** v0.1 Canonical Draft  
**文件性質：** 理論整合論文／未知型別論／移動邊界／相對終端與 AI 原生認識狀態規格  
**證據狀態：** 本文主要建立形式化概念接口；open-world recognition、scientific ignorance representation、formal epistemology 與 open-world AI 僅作外部結構對照。本文不主張未知域已被證明為實無限，也不主張任何當前不可知問題已被證明永久不可知。

---

## 摘要

DOM-01 已提出 Dynamic Metaphysical Status，將一個問題的形而上／可操作狀態表示為多域剖面：

$$
\mathbf M_t(q\mid\theta)
=
\left\langle
D,O,R,J,V,L,G,\mathfrak R,P,I,T,\mathbf U
\right\rangle.
$$

其中最後一項：

$$
\mathbf U
$$

不能被壓縮成單一 `Unknown`。

本文提出 **Moving Unknown Boundary Theory（移動未知邊界）**，將未知拆分為至少八個不同維度：

$$
\boxed{
\mathbf U_t(x\mid\theta)
=
\left\langle
U_S,
U_T,
U_O,
U_R,
U_J,
U_V,
U_{\mathfrak R},
U_{\Omega}
\right\rangle.
}
$$

其中：

- $U_S$：Unknown State，型別已知但狀態未知；
- $U_T$：Unknown Type，不知道對象應屬於哪一合法型別；
- $U_O$：Observational Unknown，缺乏可靠觀察；
- $U_R$：Reachability Unknown，不知道能否取得或接觸；
- $U_J$：Judgment Unknown，條件不足以判定；
- $U_V$：Verification Unknown，尚無可靠驗證；
- $U_{\mathfrak R}$：Realizability Unknown，不知道是否可實現；
- $U_{\Omega}$：Ontological Unknown，現有 ontology vocabulary 可能不足。

本文同時提出更深一層的 **Unknown Query Type（未知提問型別）**。有些未知不是「不知道答案」，甚至不是「不知道它是哪個既有類別」，而是：

$$
\boxed{
\text{we do not yet know what the correct question type is}.
}
$$

這種狀態不能被普通 `other`、`unclassified` 或 `Entity.Unknown` 容器視為已完成本體收納。

本文拒絕兩種常見極端：

$$
\boxed{
Unknown
\not\Rightarrow
Nothing
}
$$

以及：

$$
\boxed{
Unknown
\not\Rightarrow
InfiniteSomething.
}
$$

未知不證明不存在，也不證明外部必然無限。更穩健的命題是：

$$
\boxed{
\text{For any finite active workspace, there may remain an unexposed frontier.}
}
$$

「may」是必要限制：它描述當前工作場不完備的可能性，不把可能延伸偷換成實無限本體。

本文進一步重建 **Certified Relative Terminality（相對終端證書）**。如果某問題在指定 domain、relation、model class、resource budget、time horizon 與 evidence standard 下暫無合法擴張路徑，可以標記：

$$
\boxed{
\operatorname{CRT}(q\mid\theta)=1.
}
$$

但：

$$
\boxed{
\operatorname{CRT}(q\mid\theta)=1
\not\Rightarrow
\operatorname{UltimateBoundary}(q)=1.
}
$$

相對終端只是「在目前被明確列出的條件下，已有足夠理由停止向外聲稱可知／可達」，不是「存在本身到此為止」。

外部工程研究提供兩個重要類比。Open-world recognition 明確研究 unseen classes 與 closed-world assumption 失效；但工程上的 unknown class 仍然建立在預先定義的 recognition task 上，不能直接等同本體論的 Unknown Type。Scientific ignorance representation 則已展示，可以將科學文獻中的 known unknowns 結構化為可查詢知識物件，支持「未知本身也可以有類型、關係、來源與研究下一步」的設計方向。

本文最終將未知從「知識資料庫的空白」改寫為：

$$
\boxed{
\text{a versioned, typed, conditioned epistemic state with a moving boundary}.
}
$$

---

## 關鍵詞

Unknown State；Unknown Type；Unknown Unknown；Moving Unknown Boundary；Certified Relative Terminality；Open-World Recognition；Scientific Ignorance；Open-World AI；Epistemic Boundary；Ontological Unknown；Unknown Query Type；Unknown Profile；未知型別；相對終端；移動未知邊界

---

# 0. 研究定位與非主張

本文不主張：

1. Unknown 是一個客觀單一實體；
2. 所有 unknown 都能被未來技術消除；
3. 所有 unknown 都永遠不可消除；
4. 未知域已被證明為無限；
5. Unknown Type 等於 machine learning 的 unseen class；
6. open-world recognition 能解決本體論；
7. `other`／`unknown` 類別足以承載所有未知；
8. 相對終端等於絕對終端；
9. 暫時不可達等於原理不可達；
10. 暫時不可驗證等於原理不可驗證；
11. 不知道如何提問表示對象必然超自然；
12. ontology vocabulary 永遠不完整已被證明；
13. 所有科學進步都遵循 unknown unknown → known unknown → known 的單一路徑；
14. formal epistemology 能直接決定所有現實可知邊界；
15. 未知越多代表理論越差。

本文主張的是：

$$
\boxed{
\text{Unknown must be indexed by domain, condition, type, time, and failure mode}.
}
$$

---

# 1. 為什麼 `Unknown` 是一個危險的單值標籤？

對象 $x$ 被標：

```text
Unknown
```

我們仍然不知道：

- 是不知道值？
- 不知道種類？
- 看不到？
- 拿不到？
- 無法判斷？
- 無法驗證？
- 無法實現？
- 還是現有 ontology 根本沒有合適欄位？

這些狀態的下一步完全不同。

因此：

$$
\boxed{
\operatorname{Unknown}(x)
}
$$

不是充分的 operational state。

---

# 2. Unknown Profile

本文定義：

$$
\boxed{
\mathbf U_t(x\mid\theta)
=
\left\langle
U_S,
U_T,
U_O,
U_R,
U_J,
U_V,
U_{\mathfrak R},
U_{\Omega}
\right\rangle_{t,\theta}.
}
$$

每一分量可以取：

$$
\{0,1,?,\mathsf P,\mathsf B,\mathsf C\},
$$

其中：

- $0$：不屬於該未知；
- $1$：目前明確屬於該未知；
- $?$：尚無法決定；
- $\mathsf P$：partial；
- $\mathsf B$：branch-dependent；
- $\mathsf C$：condition-dependent。

---

# 3. Unknown State

定義：

$$
\boxed{
U_S(x)=1
}
$$

若：

$$
\operatorname{Type}(x)=T
$$

已知，但：

$$
\operatorname{State}(x)=?.
$$

例如：

- 知道是某顆星，但不知道質量；
- 知道是某個 AI instance，但不知道目前 memory state；
- 知道是某 disease class，但不知道此個案某 biomarker。

這是最普通的 unknown。

---

# 4. Unknown Parameter

Unknown State 可以進一步拆：

$$
U_{S,p}
$$

對 parameter $p$。

例如：

$$
\operatorname{Mass}(x)=?,
$$

但：

$$
\operatorname{Position}(x)
$$

已知。

因此：

$$
\boxed{
\text{partial state ignorance}
\neq
\text{total object ignorance}.
}
$$

---

# 5. Unknown Type

定義：

$$
\boxed{
U_T(x)=1
}
$$

若：

$$
\operatorname{Type}(x)=?
$$

且現有 type system 尚未能合法分類。

這比 Unknown State 更深。

---

# 6. `Other` 不等於 Unknown Type

若系統已有：

```text
KnownA
KnownB
KnownC
Other
```

那麼：

$$
x\in Other
$$

只表示：

> 它不屬於目前列出的 A/B/C。

不能推出：

$$
\boxed{
\text{the system understands what }x\text{ is}.
}
$$

---

# 7. Unknown Container Trap

定義：

$$
\boxed{
\text{Unknown Container Trap}
}
$$

指：

> 把一個未知對象放進 `Unknown`／`Other`／`Entity` 容器後，錯誤地把「可儲存」當成「已分類」。

因此：

$$
\boxed{
\text{Syntactic Accommodation}
\not\Rightarrow
\text{Ontological Classification}.
}
$$

---

# 8. Unknown Query Type

更深的情況：

$$
\boxed{
U_Q(x)=1.
}
$$

此時不只是：

> 不知道答案。

而是：

> 不知道對這個對象該問哪一類問題。

例如我們甚至不知道應該優先問：

- 位置？
- 型別？
- 因果父節點？
- 身份？
- 主體性？
- 可實現性？
- representation class？

---

# 9. Unknown Query Type 與 Unknown Type 分離

$$
U_T=1
$$

可能仍然知道：

> 這是一個需要 classification 的問題。

但：

$$
U_Q=1
$$

表示：

> classification 本身也可能是錯的上層問題框架。

因此：

$$
\boxed{
U_Q
\ge_{\mathrm{conceptual}}
U_T
}
$$

只是概念深度記號，不是數值排序定理。

---

# 10. Observational Unknown

定義：

$$
\boxed{
U_O(x)=1
}
$$

若目前缺乏可靠 observation channel。

這不推出：

$$
\neg\operatorname{Exist}(x).
$$

所以：

$$
\boxed{
Unobserved
\not\Rightarrow
Nonexistent.
}
$$

---

# 11. Reachability Unknown

定義：

$$
\boxed{
U_R(x)=1
}
$$

表示：

> 不知道目前是否能合法取得、觸及、查詢或操控相關資訊／對象。

它可能源自：

- physical distance；
- permission；
- API；
- encryption；
- causal horizon；
- missing address；
- computational cost。

---

# 12. Unreachable 不等於 Nonexistent

沿用 UBP：

$$
\boxed{
Reach_S(x)=0
\not\Rightarrow
Exist(x)=0.
}
$$

同樣：

$$
Reach_S(x)=?
$$

更不能推出不存在。

---

# 13. Judgment Unknown

定義：

$$
\boxed{
U_J(q)=1
}
$$

如果問題已定義、資料也可能取得，但條件不足以形成可靠判定。

例如：

- evidence mutually inconsistent；
- model underdetermined；
- threshold unspecified；
- branch-dependent theorem status；
- causal direction unresolved。

---

# 14. Verification Unknown

定義：

$$
\boxed{
U_V(q)=1
}
$$

如果已有候選 judgment，但：

- 未 replication；
- 無 certificate；
- 無 independent measurement；
- source quality 不足；
- theorem proof obligation 未閉合。

因此：

$$
\boxed{
\text{Judgeable}
\neq
\text{Verified}.
}
$$

---

# 15. Realizability Unknown

定義：

$$
\boxed{
U_{\mathfrak R}(q)=1
}
$$

若：

> 不知道某 formal structure 是否能在指定 backend 實現。

可能是：

- digital；
- physical；
- biological；
- quantum；
- social；
- institutional。

---

# 16. Formal Existence 不等於 Physical Realization

$$
\boxed{
\operatorname{Formalizable}(q)
\not\Rightarrow
\operatorname{PhysicallyRealizable}(q).
}
$$

因此 realization unknown 不能被 formal consistency 自動消除。

---

# 17. Ontological Unknown

定義：

$$
\boxed{
U_{\Omega}(x)=1
}
$$

若有理由懷疑：

> 現有 ontology vocabulary / role schema / entity model 可能不足以描述 $x$。

注意這只是 epistemic model state。

不主張真的存在「超越所有 ontology 的神秘物」。

---

# 18. Ontological Unknown 的最低判準

至少需要一種情況：

1. 所有現有 type 都產生 contradiction；
2. 所有 type assignment 都嚴重 information loss；
3. 不同 representation 對其 ontology assignment 持續不穩定；
4. 新 interaction 暴露原 schema 無法表達的 relation；
5. object 可以被表示，但不能在現 ontology 中合法定位。

---

# 19. Unknown Type Discovery Event

定義：

$$
\boxed{
\mathcal E_{UT}
}
$$

為：

> 系統第一次辨識出「原本沒有這種問題型別／物件型別」的事件。

它不是找到某個新值。

而是：

$$
\boxed{
\text{schema expansion event}.
}
$$

---

# 20. Schema Expansion

形式：

$$
\mathcal T_t
\rightarrow
\mathcal T_{t+1},
$$

其中：

$$
\mathcal T_t
\subset
\mathcal T_{t+1}.
$$

新增：

$$
\tau_{\mathrm{new}}.
$$

因此 previously unknown-type object：

$$
x
$$

可以變成：

$$
\operatorname{Type}_{t+1}(x)=\tau_{\mathrm{new}}.
$$

---

# 21. Unknown 不是永恆屬性

對同一 $x$：

$$
\mathbf U_{t_0}(x)
\neq
\mathbf U_{t_1}(x)
$$

完全可能。

因此：

$$
\boxed{
\text{Unknown}
=
\text{dynamic epistemic status}.
}
$$

---

# 22. Unknown Boundary

令：

$$
D_t^{known}
$$

是某指定 qualification 下的 known domain。

則 boundary：

$$
\boxed{
B_t^U
}
$$

不是「未知本身的邊緣」的絕對本體物件。

而是：

> 已結構化認知域與尚未結構化區域之間，在指定 backend 下的相對界面。

---

# 23. Unknown Boundary 必須帶 Backend

如果沒有：

- topology；
- graph adjacency；
- metric；
- operational cost；
- classification neighborhood；

則：

$$
B^U
$$

只能是：

```text
metaphorical_frontier
```

不能假裝是幾何 theorem。

---

# 24. Moving Unknown Boundary

定義：

$$
\boxed{
B^U_t
\rightarrow
B^U_{t+\Delta t}.
}
$$

這個 movement 可能由：

- new observation；
- new tool；
- new ontology；
- new theorem；
- new embodiment；
- new permission；
- new AI capability；

造成。

---

# 25. Unknown Boundary 可以外移

外移可表示：

> 原本不可定義／不可達的區域變得可處理。

但這不是唯一方向。

---

# 26. Unknown Boundary 可以回縮

例如：

- model invalidated；
- data revoked；
- access lost；
- calibration failed；
- ontology split；
- theorem withdrawn。

所以：

$$
\boxed{
\text{knowledge frontier evolution is non-monotonic}.
}
$$

---

# 27. 新知識也可以創造新未知

若：

$$
\mathcal T_t
\rightarrow
\mathcal T_{t+1}
$$

加入新 type，

可能同時產生新問題：

$$
Q_{new}.
$$

因此：

$$
\boxed{
K_t\uparrow
\not\Rightarrow
|\partial K_t|\downarrow.
}
$$

---

# 28. Knowledge–Frontier Co-Expansion

候選命題：

$$
\boxed{
K_t\uparrow
\land
|\partial K_t|\uparrow.
}
$$

可能成立。

例如：

- 發現 gene 後產生 gene regulation 問題；
- 發現 quantum states 後產生 measurement problem；
- 建立 AI agents 後產生 fork identity；
- 建立 synthetic worlds 後產生 creator ethics。

---

# 29. 這不是未知無限的證明

從：

$$
|\partial K_t|\uparrow
$$

不能推出：

$$
|\mathcal U_{\mathrm{unknown}}|=\infty.
$$

所以：

$$
\boxed{
\text{frontier growth}
\not\Rightarrow
\text{actual infinity}.
}
$$

---

# 30. Unknown → Nothing 錯誤

如果：

$$
U(x)=1
$$

不能推出：

$$
Exist(x)=0.
$$

這是：

$$
\boxed{
\text{Unknown-to-Nothing Error}.
}
$$

---

# 31. Unknown → Infinite 錯誤

同樣：

$$
U(x)=1
$$

不能推出：

$$
\operatorname{InfiniteBeyond}(x)=1.
$$

這是：

$$
\boxed{
\text{Unknown-to-Infinity Error}.
}
$$

---

# 32. Unknown → Supernatural 錯誤

如果某 anomaly 無解：

$$
U_J=1,
$$

不能推出：

$$
\operatorname{Supernatural}=1.
$$

沿用 CCAW-07：

$$
\boxed{
\text{unexplained}
\neq
\text{external creator evidence}.
}
$$

---

# 33. Unknown → Future-Solvable 錯誤

反過來也不能：

$$
U(q)=1
\Rightarrow
\text{future technology will solve it}.
$$

這是：

$$
\boxed{
\text{Future-Solvability Assumption}.
}
$$

DOM 不接受。

---

# 34. Relative Unknowability

定義：

$$
\boxed{
\operatorname{Unknowable}
(q\mid S,\theta,t)
}
$$

表示：

> 對 Self / system $S$，在明示條件 $\theta$ 與時間 $t$ 下，沒有已知合法路徑取得足以形成指定知識標準的 evidence。

它是相對詞。

---

# 35. Strong Unknowability Candidate

更強主張：

$$
\boxed{
\forall S,\forall\theta,\forall t,
\operatorname{Unknowable}(q)=1.
}
$$

這種 absolute unknowability 的證明負擔極高。

本文不主張已知存在任何此類問題。

---

# 36. Certified Relative Terminality

定義：

$$
\boxed{
\operatorname{CRT}(q\mid\theta)=1
}
$$

若在明示：

- domain；
- relation；
- model class；
- observer；
- instrument；
- permission；
- resource budget；
- evidence standard；
- search horizon；

下，已有充分理由停止把「可解／可達／可驗證」當作當前工作假設。

---

# 37. CRT 不是 Absolute Terminality

$$
\boxed{
\operatorname{CRT}(q\mid\theta)
\not\Rightarrow
\operatorname{UltimateBoundary}(q).
}
$$

這是 DOM-02 最重要的 guardrail。

---

# 38. CRT Certificate

建議格式：

```yaml
relative_terminal_certificate:
  question_id: "..."
  domain: "..."
  relation: "..."
  model_class: "..."
  observer: "..."
  time: "..."
  instrument: "..."
  permissions: "..."
  resource_budget: "..."
  evidence_standard: "..."
  attempted_routes: []
  failed_routes: []
  unresolved_routes: []
  alternative_models: []
  terminality_type:
    - observational
    - reachability
    - judgment
    - verification
    - realizability
    - operational
  status: "certified_relative_terminal"
  expires_if:
    - "new instrument"
    - "new model"
    - "new evidence"
    - "new permission"
    - "new ontology"
```

---

# 39. Relative Terminality 的價值

它允許研究系統說：

> 目前先停。

而不是：

> 永遠不可能。

這是成熟研究治理很重要的差別。

---

# 40. Terminality 不是失敗

某問題取得：

$$
CRT=1
$$

可以是：

- resource-aware；
- risk-aware；
- evidence-aware；
- scope-aware；

的正常研究結果。

因此：

$$
\boxed{
\text{Defer}
\neq
\text{Failure}.
}
$$

---

# 41. CRT 可以失效

若新事件：

$$
\mathcal E_{new}
$$

改變：

$$
\theta,
$$

則：

$$
CRT_{t_0}=1
$$

可以變成：

$$
CRT_{t_1}=0.
$$

---

# 42. Terminality Hysteresis

即使 CRT 被解除，

舊 certificate 仍然有價值。

它保存：

- 哪些路走過；
- 為什麼失敗；
- 當時有哪些 constraints。

因此：

$$
\boxed{
\text{terminality history}
\neq
\text{discarded failure log}.
}
$$

---

# 43. Open-World Recognition 的工程類比

Open-world recognition / open-set recognition 處理：

> 模型在 deployment 時遇到 training 中沒有的 classes。

這提醒：

$$
\boxed{
\text{closed label space}
\neq
\text{open environment}.
}
$$

---

# 44. Unknown Unknown Class 的技術含義

在 ML 文獻中，unknown unknown class 通常指：

> training 階段未見，test / deployment 才出現的 class。

這是：

$$
\boxed{
\text{task-relative unseen class}.
}
$$

不是：

$$
\boxed{
\text{ontologically unprecedented type}.
}
$$

---

# 45. Open-World AI 與 DOM 的差別

Open-world AI 主要問：

- 如何拒絕 unseen input？
- 如何偵測新 class？
- 如何 incremental learn？

DOM 問更廣：

- class schema 本身是否正確？
- 是否需要新 question type？
- 是否有 non-classification relation？
- unknown 是 observation、judgment、ontology 還是哪一層？

---

# 46. Unknown 與 Uncertainty 分離

外部 open-world literature 已明確提醒：

$$
\boxed{
\text{uncertain}
\neq
\text{unknown}.
}
$$

模型可以對錯誤答案：

$$
P(y\mid x)\approx1
$$

卻其實遇到未知類。

所以：

$$
\boxed{
\text{confidence}
\not\Rightarrow
\text{knownness}.
}
$$

---

# 47. Epistemic Uncertainty 也不等於 Unknown Type

即使 model epistemic uncertainty 很高，

也可能只是：

- data sparse；
- parameter uncertainty；
- distribution shift。

不代表：

$$
U_T=1.
$$

---

# 48. Ignorance-Base 的類比

2023 年 biomedical informatics 已有人建立 ignorance-base，把 scientific literature 中：

- missing knowledge；
- unanswered questions；
- controversies；
- desired knowledge goals；

結構化成可搜索知識物件。

這支持：

$$
\boxed{
\text{known unknowns can be represented explicitly}.
}
$$

---

# 49. Unknown Object 也需要 Provenance

因此未知物件至少應記錄：

```yaml
unknown_record:
  object_id: "..."
  detected_at: "..."
  unknown_profile:
    state: "..."
    type: "..."
    observation: "..."
    reachability: "..."
    judgment: "..."
    verification: "..."
    realizability: "..."
    ontology: "..."
  detected_by: "..."
  trigger: "..."
  evidence: []
  candidate_types: []
  rejected_types: []
  next_actions: []
```

---

# 50. Unknown 不應被覆寫

如果之後：

$$
U_T
\rightarrow
0
$$

並得到新 type，

仍應保留：

$$
\text{previous unknown state}.
$$

因為它是 schema evolution 的歷史。

---

# 51. Unknown Lineage

定義：

$$
\boxed{
G_U
=
(V_U,E_U).
}
$$

每個 unknown 可以經：

- split；
- merge；
- retype；
- resolve；
- defer；
- reopen；

形成 lineage。

---

# 52. Unknown Split

一個舊 Unknown：

$$
U_0
$$

未來可能拆成：

$$
U_1,U_2,U_3.
$$

所以：

$$
\boxed{
\text{resolution}
\neq
\text{simple deletion}.
}
$$

---

# 53. Unknown Merge

多個 anomaly：

$$
U_1,U_2,U_3
$$

後來可能發現同一 underlying mechanism：

$$
U^\ast.
$$

因此 unknown topology 也會重構。

---

# 54. Unknown Reopen

某問題一度：

$$
U_V=0
$$

被認為已驗證，

但後來 replication failure：

$$
U_V=1.
$$

因此：

$$
\boxed{
\text{known}
\rightarrow
\text{unknown}
}
$$

也完全可能。

---

# 55. Unknown State Machine

候選：

$$
\boxed{
S_U
=
\{
Unknown,
StructuredUnknown,
Candidate,
ConditionallyResolved,
Verified,
Reopened,
Deferred,
RelativeTerminal
\}.
}
$$

---

# 56. Unknown Discovery vs Unknown Resolution

這是兩種不同成果：

$$
\boxed{
\text{DiscoverUnknown}
}
$$

與：

$$
\boxed{
\text{ResolveUnknown}.
}
$$

科學進步不只來自解答。

也來自：

> 第一次知道原來有一個問題。

---

# 57. Unknown Discovery Gain

定義候選：

$$
\boxed{
G_{UD}
}
$$

表示新未知被合法識別所帶來的 research value。

它提醒：

$$
\boxed{
\text{more explicit ignorance}
\not\Rightarrow
\text{less scientific progress}.
}
$$

---

# 58. Unknown Density 不是理論品質分數

不能寫：

$$
\text{more unknowns}
\Rightarrow
\text{worse theory}.
$$

因為高解析度 theory 可能辨識更多細緻 open questions。

---

# 59. Unknown Boundary Resolution

邊界不是只往外。

也可能從粗糙：

$$
B^U
$$

變成多條：

$$
B^U_1,\ldots,B^U_n.
$$

這是：

$$
\boxed{
\text{frontier refinement}.
}
$$

---

# 60. Frontier Refinement

即使「總可知範圍」沒有明顯增加，

只要 unknown boundary 更細，

研究能力也可能提高。

因此：

$$
\boxed{
\text{boundary resolution}
\neq
\text{boundary displacement}.
}
$$

---

# 61. Unknown Boundary Velocity

若 backend 合法，可定義：

$$
v_U
=
\frac{
d(B^U_t,B^U_{t+\Delta t})
}{
\Delta t
}.
$$

但不保證存在幾何 normal velocity。

---

# 62. Unknown Flux

若 known domain 可測：

$$
\boxed{
\Phi_U
=
\frac{
\mu(K_{t+\Delta t}\setminus K_t)
-
\mu(K_t\setminus K_{t+\Delta t})
}{
\Delta t
}.
}
$$

正值可表示 known region 淨增加。

但不能直接等同「真理增加」。

---

# 63. Type Frontier Lag

可能：

$$
B^{obs}
$$

已外移，

但：

$$
B^{type}
$$

沒跟上。

也就是：

> 看到了新東西，但不知道它是什麼。

定義：

$$
\boxed{
\mathcal L^{O\rightarrow T}.
}
$$

---

# 64. Verification Frontier Lag

$$
\boxed{
\mathcal L^{J\rightarrow V}.
}
$$

> 可以提出判斷，但驗證前沿落後。

---

# 65. Realizability Frontier Lag

$$
\boxed{
\mathcal L^{V\rightarrow \mathfrak R}.
}
$$

> 理論／證據已成熟，但 engineering realization 尚未出現。

---

# 66. Ontology Frontier Lag

候選：

$$
\boxed{
\mathcal L^{O\rightarrow \Omega}.
}
$$

> observation 已經出現，但 ontology vocabulary 尚未能穩定吸收。

---

# 67. Unknown Budget

實際研究不可能無限探索。

定義：

$$
B_U
$$

為 unknown exploration budget。

可由：

- time；
- compute；
- money；
- risk；
- personnel；
- opportunity cost；

構成。

---

# 68. Budgeted Unknown Exploration

若：

$$
\operatorname{ExpectedGain}(U_i)
<
\operatorname{Cost}(U_i),
$$

可以：

$$
Defer(U_i).
$$

這不代表 $U_i$ 不重要。

只是 research routing。

---

# 69. Risk-Gated Exploration

某 unknown 可能高危：

$$
Risk(U_i)\gg0.
$$

則 exploration 需要：

- sandbox；
- ethics；
- authorization；
- bounded experiment。

Unknown 本身不生成無限探索權。

---

# 70. Unknown 與 Governance

對 AI：

$$
\boxed{
\text{I don't know}
}
$$

應該是合法輸出。

更完整應是：

> 我不知道，且未知位於 verification domain；定義、觀察與判定已完成，但 independent evidence 不足。

這比一般 refusal / uncertainty 更有資訊。

---

# 71. AI Native Unknown Report

建議：

```yaml
epistemic_status:
  answer: "defer"
  unknown_profile:
    state: 0
    type: 0
    observation: 0
    reachability: 0
    judgment: 0
    verification: 1
    realizability: 0
    ontology: 0
  reason: "independent verification missing"
  next_action:
    - retrieve_primary_source
    - reproduce_result
```

---

# 72. Unknown-Type Report

如果：

$$
U_T=1
$$

AI 不應假裝分類。

應輸出：

```yaml
status: "unknown_type"
candidate_schemas:
  - "..."
schema_conflict:
  - "..."
recommended_action:
  - "branch ontology"
  - "create provisional type"
  - "collect discriminating evidence"
```

---

# 73. Unknown Query-Type Report

如果：

$$
U_Q=1,
$$

則：

```yaml
status: "question_type_unresolved"
do_not_force_classification: true
next_actions:
  - "generate candidate question families"
  - "inspect interaction structure"
  - "seek new representation"
```

---

# 74. Provisional Type

可以建立：

$$
\boxed{
\tau_{\mathrm{prov}}
}
$$

但必須標記：

$$
\operatorname{Provisional}=1.
$$

避免 provisional container 逐漸被誤認成 canonical ontology。

---

# 75. Provisional Ontology Debt

如果大量：

$$
\tau_{\mathrm{prov}}
$$

長期不處理，

形成：

$$
\boxed{
D_{\Omega}^{debt}.
}
$$

即 ontology debt。

---

# 76. Unknown Debt

同理：

$$
\boxed{
D_U
}
$$

表示長期未路由、未分類、未驗證的 unknown backlog。

它與一般 technical debt 類似，但不能僅用數量衡量。

---

# 77. Unknown Priority

候選：

$$
Priority(U_i)
=
F
\left(
Impact,
Uncertainty,
Reachability,
Cost,
Risk,
Dependency,
Novelty
\right).
$$

不建立固定 universal formula。

---

# 78. Unknown 的研究倫理

不能因 unknown：

- 高新奇；
- 高神秘；
- 高話題性；

就自動高優先。

同樣不能因 unknown：

- 難；
- 不可立即商用；

就自動丟棄。

---

# 79. Unknown 與謙卑

成熟 epistemic humility 不是：

> 什麼都不知道。

而是：

$$
\boxed{
\text{know where and how the current knowledge claim fails}.
}
$$

---

# 80. 過度謙虛的錯誤

如果：

$$
U_V=1
$$

就說：

> 我們什麼都不知道。

這是：

$$
\boxed{
\text{Unknown Overgeneralization}.
}
$$

可能其實：

$$
D=O=R=J=1,
$$

只差 verification。

---

# 81. 過度傲慢的錯誤

如果：

$$
D=O=R=J=1
$$

就說：

$$
U_{\Omega}=0,
$$

同樣錯。

這是：

$$
\boxed{
\text{Qualification Collapse}.
}
$$

---

# 82. Unknown Profile 防止兩端錯誤

所以：

$$
\boxed{
\mathbf U
}
$$

同時對抗：

- arrogance；
- blanket skepticism。

它讓系統可以非常精確地說：

> 哪裡知道，哪裡不知道。

---

# 83. Formal Epistemology 的邊界提醒

Formal epistemology 中的 knowability paradox / epistemic logic 類問題提醒：

> 「所有真理原理上可知」不是無害假設。

DOM 不把任何這類 logic result 直接當作現實宇宙不可知性定理。

只取：

$$
\boxed{
\text{unlimited knowability should not be assumed for finite agents}.
}
$$

---

# 84. Finite Agent Principle

候選原則：

$$
\boxed{
\operatorname{FiniteAgent}(S)
\Rightarrow
\text{do not assume }K_S=\text{AllTruths}.
}
$$

這不是說 finite agent 必有絕對不可知真理。

而是禁止預設全知。

---

# 85. Open World Principle

對 open environment：

$$
\boxed{
\text{KnownLabelSet}_t
\not\Rightarrow
\text{ExhaustiveWorldTypeSet}.
}
$$

這是 open-world AI 對 DOM 的最低工程啟示。

---

# 86. Closed-World Assumption Risk

如果系統假設：

$$
\forall x,
\quad
Type(x)\in\mathcal T_{known},
$$

則未知新類很容易被強制錯分。

所以：

$$
\boxed{
\text{forced classification}
}
$$

本身可以製造 epistemic error。

---

# 87. Ontology Open-World Guard

DOM 建議：

$$
\boxed{
\exists x:
Type(x)=?
}
$$

必須是合法系統狀態。

不是 exception bug。

---

# 88. Unknown Type 不應自動神秘化

如果：

$$
Type(x)=?,
$$

優先意味：

> current schema insufficient or evidence insufficient.

而不是：

> x transcends reality.

所以：

$$
\boxed{
U_T
\not\Rightarrow
\operatorname{Transcendent}(x).
}
$$

---

# 89. Relative Terminal Boundary

將 CRT 對應到 boundary：

$$
\boxed{
B^{CRT}(q\mid\theta).
}
$$

表示：

> 對當前研究配置，已達可證成的相對停止邊界。

---

# 90. Current Horizon / Relative Terminal / Ultimate Boundary

正式三分：

$$
\boxed{
B_{\mathrm{current}}
\neq
B_{\mathrm{CRT}}
\neq
B_{\mathrm{ultimate}}.
}
$$

Current Horizon：

> 今天走到這裡。

CRT：

> 在明示條件下，有充分理由暫時把這裡當終點。

Ultimate：

> beyond this, no relevant ontological extension exists.

第三種負擔最高。

---

# 91. Ultimate Boundary Claim Burden

如果主張：

$$
B=B_{\mathrm{ultimate}},
$$

等於主張：

$$
\boxed{
\forall x\text{ beyond }B,
\quad
\neg\operatorname{RelevantExistence}(x).
}
$$

這是一個極強全域否定命題。

有限 observer 很難僅從 local failure 推出。

---

# 92. DOM-02 的核心中立值

當：

$$
\neg Evidence(Exist)
$$

且：

$$
\neg Evidence(Nonexist)
$$

最合理狀態可以是：

$$
\boxed{
Unknown.
}
$$

不是：

$$
0
$$

也不是：

$$
1.
$$

---

# 93. Unknown 的正面地位

因此 Unknown 不是 garbage value。

而是一個：

$$
\boxed{
\text{first-class epistemic state}.
}
$$

它可以有：

- type；
- provenance；
- history；
- dependencies；
- budget；
- next action；
- exit condition。

---

# 94. 第一正式命題：Unknown Multiplicity

$$
\boxed{
U_S
\neq
U_T
\neq
U_J
\neq
U_V
\neq
U_{\Omega}
}
$$

一般不能互相化約。

---

# 95. 第二正式命題：Unknown Non-Existence Separation

$$
\boxed{
Unknown(x)
\not\Rightarrow
\neg Exist(x).
}
$$

---

# 96. 第三正式命題：Unknown Infinity Separation

$$
\boxed{
Unknown(x)
\not\Rightarrow
InfiniteBeyond(x).
}
$$

---

# 97. 第四正式命題：Relative Terminal Separation

$$
\boxed{
CRT(q\mid\theta)=1
\not\Rightarrow
UltimateBoundary(q)=1.
}
$$

---

# 98. 第五正式命題：Unknown Can Become Known

$$
\boxed{
\mathbf U_{t_0}(x)
\neq
\mathbf U_{t_1}(x)
}
$$

允許 Unknown 被 retype / resolve / reopen。

---

# 99. 第六正式命題：Known Can Reopen

$$
\boxed{
Known_{t_0}(x)
\not\Rightarrow
Known_{t_1}(x).
}
$$

在 evidence/model 失效時可以重新 Unknown。

---

# 100. 候選猜想一：Unknown-Type Discovery

新能力的主要突破之一，可能不是回答舊問題，而是：

$$
\boxed{
\text{discover new legitimate question / entity types}.
}
$$

---

# 101. 候選猜想二：Knowledge–Frontier Co-Expansion

$$
\boxed{
K_t\uparrow
\land
|\partial K_t|\uparrow
}
$$

可在某些知識系統發生。

---

# 102. 候選猜想三：AI Unknown Discovery Acceleration

AI 可能提高：

$$
\frac{dN_{\mathrm{known\ unknown}}}{dt}.
$$

也就是更快把 unknown unknown 轉成 known unknown。

但這不保證：

$$
U_{\Omega}\downarrow.
$$

---

# 103. 候選猜想四：Ontology Debt Emergence

當 AI 生成新 agents、worlds、identity structures、data types，

ontology debt：

$$
D_{\Omega}^{debt}
$$

可能成為 AI-native infrastructure 的主要問題之一。

---

# 104. 候選猜想五：Relative Terminality Is More Useful Than Absolute Unknowability

對工程與研究治理：

$$
\boxed{
CRT
}
$$

可能比：

$$
\boxed{
AbsoluteUnknowable
}
$$

更可操作。

---

# 105. 候選猜想六：Unknown Profile Improves Routing

如果 Agent 保留：

$$
\mathbf U,
$$

可能比單一 confidence score 更好決定：

- retrieve；
- measure；
- verify；
- reframe；
- branch；
- defer；
- create type。

這是可實驗工程命題。

---

# 106. DOM-02 的 AI 實驗規格

比較兩類 Agent：

## A：Scalar Unknown Agent

只有：

```text
known / unknown
```

## B：Typed Unknown Agent

維護：

$$
\mathbf U.
$$

測試：

- error classification；
- false certainty；
- false refusal；
- next-action quality；
- ontology expansion；
- verification routing。

---

# 107. 評估指標

候選：

$$
E_{\mathrm{false-known}},
$$

$$
E_{\mathrm{false-unknown}},
$$

$$
R_{\mathrm{route}},
$$

$$
Q_{\mathrm{type-discovery}},
$$

$$
C_{\mathrm{resolution}},
$$

$$
D_{\Omega}^{debt}.
$$

---

# 108. 外部研究邊界

Open-world recognition / open-world learning 的近期研究指出，在動態環境中，closed-world label assumptions 容易失效；系統需要能拒絕 unseen class、偵測 novelty，並在後續 learning 中擴張 model。本文只把這當作「known label set 不等於 exhaustive world type set」的工程類比。

Open-set recognition 文獻也特別區分 uncertainty 與 unknown：模型可以高信心錯分一個真正 unseen input，因此 low confidence 不是 unknown 的必要條件，而 high confidence 也不是 known 的充分條件。

2023 年的 scientific ignorance-base 研究把科學文獻中的 known unknowns 結構化成可搜尋 knowledge objects，並明確將 unknown unknown → known unknown → known 視為部分 discovery process 的有用描述。本文吸收其「未知可被結構化、索引與導向下一步」的工程思想，但不把此流程當作所有知識發展的普遍定律。

Formal epistemology 中的 knowability 討論則提醒，對有限 epistemic agents 直接假定「所有 truth 原理上都可知」會帶來非平凡邏輯問題。本文只採取弱限制：不能預設有限 agent 必然能達成全知；本文不從這些形式結果推出現實中的 Absolute Unknowability。

---

# 109. 與 DOM-03 的接口

DOM-02 現在已建立：

$$
\mathbf U
$$

以及：

$$
B^U_t,
$$

並分離：

$$
B_{\mathrm{current}},
\quad
B_{\mathrm{CRT}},
\quad
B_{\mathrm{ultimate}}.
$$

下一篇將進入 relation layer：

$$
\boxed{
\mathfrak C
=
\text{Typed Containment}.
}
$$

核心問題：

> 「包含」到底包含什麼？

> 被 whole 包含，是否表示 whole 知道 part？

> 被 Higher Self 包含，是否表示 part 不再是 self？

> information containment、causal containment、control containment、identity containment 是否同一？

DOM-03 將正式固定：

$$
\boxed{
\text{Containment}
\not\Rightarrow
\text{Knowledge}
}
$$

與：

$$
\boxed{
\text{Part-of}
\not\Rightarrow
\text{Non-Subject}.
}
$$

---

# 110. 結論

DOM-02 的核心工作不是替 Unknown 添加更多神秘色彩。

而是相反：

$$
\boxed{
\text{de-mystify ignorance by typing it}.
}
$$

當一個系統只說：

> 不知道。

它仍然可能非常粗糙。

更成熟的是：

> 型別已知、狀態未知。

或：

> 已觀察、可達、可判定，但尚未驗證。

或：

> 資料足夠，但現有 ontology 無法穩定分類。

或：

> 在目前 model / instrument / permission / resource budget 下，已取得 Certified Relative Terminality。

因此：

$$
\boxed{
Unknown
}
$$

不再是「知識的黑洞」。

它是一個：

$$
\boxed{
\text{versioned, typed, conditioned epistemic object}.
}
$$

更重要的是，這讓我們同時避免兩種相反錯誤。

第一種是傲慢：

$$
\boxed{
\text{Current Horizon}
\Rightarrow
\text{Ultimate Boundary}.
}
$$

第二種是過度想像：

$$
\boxed{
\text{Unknown}
\Rightarrow
\text{Infinite Beyond}.
}
$$

DOM-02 只保留一個中性的開放結構：

$$
\boxed{
\text{For any finite active workspace, there may remain an unexposed frontier.}
}
$$

這句話不說外面一定有無限世界。

也不說外面什麼都沒有。

它只拒絕：

> 因為目前工作場已滿，所以存在必然已被收完。

同時，DOM-02 也拒絕：

> 因為我們還不知道，所以外部必然無界。

最後，真正成熟的 epistemic humility 不是：

$$
\boxed{
\text{I know nothing}.
}
$$

也不是：

$$
\boxed{
\text{I will eventually know everything}.
}
$$

而是：

$$
\boxed{
\text{I can state precisely what kind of unknown remains, under what conditions, and what would change that status}.
}
$$

這就是移動未知邊界的核心。

---

# 內部理論譜系

本篇主要繼承與修正：

1. 《動態知識空間總論》。
2. 《多域知識判定論》。
3. 《移動邊界論》。
4. 《終極邊界問題：視界、模型、可實現域與本體終界》。
5. 《無限展開的邊界：真實、工作場、認知場與權威世界》。
6. 《無限階 Self–World 遞迴論》。
7. 《T 是 T，T 不是 T》。
8. 《多尺度同一性與忒修斯主體》。
9. 《分域算子本體論》。
10. 《未收納域》（思想實驗來源，不作定理）。
11. 《DOM 寫作前繼承、修正、降格與超譯矩陣》。
12. 《DOM Dependency Map v0.1》。
13. 《DOM-01｜動態形而上狀態》。
14. CCAW-07 與 CCAW-10。

---

# 外部參考文獻

1. Wang, K., Li, Z., Chen, Y., Dong, W., & Chen, J. (2025). *Towards open-world recognition: Critical problems and challenges*. Engineering Applications of Artificial Intelligence, 143, 110042. DOI: 10.1016/j.engappai.2025.110042.
2. Boult, T. E., Cruz, S., Dhamija, A. R., Gunther, M., Henrydoss, J., & Scheirer, W. J. (2019). *Learning and the Unknown: Surveying Steps toward Open World Recognition*. AAAI, 33, 9801–9807. DOI: 10.1609/aaai.v33i01.33019801.
3. Zhao, P., Shan, J.-W., Zhang, Y.-J., & Zhou, Z.-H. (2024). *Exploratory machine learning with unknown unknowns*. Artificial Intelligence, 327, 104059. DOI: 10.1016/j.artint.2023.104059.
4. Cruz, S., et al. (2025). *Open issues in open world learning*. AI Magazine. DOI: 10.1002/aaai.70001.
5. Boguslav, M. R., et al. (2023). *Creating an ignorance-base: Exploring known unknowns in the scientific literature*. Journal of Biomedical Informatics, 143, 104405. DOI: 10.1016/j.jbi.2023.104405.
6. Stanford Encyclopedia of Philosophy. *Formal Epistemology*. Section on knowability and epistemic logic.
7. Davoodi, T., et al. (2022). *Varieties of Ignorance: Mystery and the Unknown in Science and Religion*. Cognitive Science, 46, e13129. DOI: 10.1111/cogs.13129.

---

# 作者聲明

本文提出的 Unknown Profile、Unknown Query Type、Unknown-Type Discovery Event、Moving Unknown Boundary、Certified Relative Terminality、Unknown Lineage、Ontology Debt、Unknown Discovery Gain 與相關 AI-native unknown reporting schema 均為理論建模接口。本文不主張未知域已被證明為實無限，不主張任何當前不可知問題已被證明永久不可知，也不把 machine-learning 中的 unseen classes 直接等同於本體論上的 Unknown Type。本文所稱相對終端只是在明示條件下的研究停止與邊界證書，不等同 Absolute Ultimate Boundary。

**END OF DOM-02 — v0.1**
