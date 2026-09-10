# PTE-01｜假設理論為真：暫時真值工程與強理論可執行化協議

## Assume the Theory Is True: Provisional Truth Engineering for Executable Theory Testing

**系列：** 《假設你是對的》／Provisional Truth Engineering Series（PTE）  
**系列文件：** PTE-01 / 07  
**版本：** v0.1  
**日期：** 2026-09-09  
**作者：** Neo.K  
**研究協作：** AI-assisted theoretical development  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 公開方法論論文／AI 時代理論檢驗協議  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

強理論、跨域理論與宏大理論的評價，常在兩種失衡狀態之間擺動。一端是過早否定：因術語陌生、跨域距離過大、形式不成熟或論證帶有過度宣稱，理論在尚未被轉化為可檢驗對象前便被整體丟棄；另一端是過早接受：因概念新穎、敘事宏大、局部例子成功或形式符號密集，便把尚未建立的工程效果、預測能力或不可約原理提前視為成立。

本文提出 **Provisional Truth Engineering（PTE，暫時真值工程）**，並定義其核心操作 **Assume-the-Theory-True Protocol（ATTP）**。PTE 不要求研究者相信理論 $T$ 為真，也不要求暫停批判，而是引入一個受限的暫時真值算子：

$$
\boxed{
\mathsf{Assume}^{+}(T)
}
$$

其含義是：

> 在不承諾 $T$ 真實性的前提下，暫時採取一個對 $T$ 盡可能有利、但仍受文本、邏輯、資源與可觀測性約束的強解讀，並要求該解讀產生可形式化、可操作、可實作、可對照與可否證的後果。

PTE 的基本鏈條為：

$$
\boxed{
T
\rightarrow
T^{+}
\rightarrow
F(T)
\rightarrow
O(T)
\rightarrow
I(T)
\rightarrow
B^{*}(T)
\rightarrow
E(T)
\rightarrow
R(T)
}
$$

其中：

- $T^{+}$：理論的最強可辯護解讀；
- $F(T)$：形式化；
- $O(T)$：操作化；
- $I(T)$：可執行實作；
- $B^{*}(T)$：資訊與資源匹配的最強既有重建；
- $E(T)$：外部、對抗性與反例證據；
- $R(T)$：在過度宣稱與已知重建被扣除後仍存留的不可約殘差。

本文特別主張：**PTE 不是新的「真假二分器」，而是把理論從文本爭論推進到可執行證據的研究協議。** 因此，一套理論可以同時具有概念價值、規格價值與工程價值，而仍未建立預測優勢或不可約的新計算原理。

本文並明確說明其研究譜系。PTE 並非從零產生；它整合並推進既有研究線中的「重建才是理解的驗收」、可證偽 Benchmark、Evidence Ledger、Python-first 理論驗證、對抗性與未知資料通道、作者脫鉤、延遲理解／延遲驗證、全稱主張與反例的不對等證明負擔，以及 matched reconstruction benchmark。本文的新貢獻，是第一次把這些原本分散的原則收斂成一套**專門面向強理論本身的暫時真值工程協議**。

本文最後提出四個最低要求：

$$
\boxed{
\text{Charitable Interpretation}
}
$$

$$
\boxed{
\text{Executable Consequence}
}
$$

$$
\boxed{
\text{Matched Reconstruction}
}
$$

$$
\boxed{
\text{Residue Preservation}
}
$$

若一套理論無法被公平形式化，PTE 不應假裝它已被測試；若其工程效果可被既有機制完整重建，PTE 不應把「有用」升格為「不可約新原理」；若部分主張失敗而部分結構仍有效，PTE 亦不應將其整體歸零。

**關鍵詞：** Provisional Truth Engineering、Assume-the-Theory-True Protocol、Steelman、Operationalization、Executable Theory、Matched Reconstruction、Falsification、Epistemic Salvage、Irreducible Residue、AI Science

---

# 0. 邊界聲明

本文不主張：

- 對所有理論都應先相信；
- 宏大理論比局部理論更值得研究；
- 可實作性等於真實性；
- 工程有效等於本體論成立；
- 模擬成功等於現實驗證；
- AI 可以取代物理世界的不可約證據；
- 一個成功 MVP 可以證明全稱理論；
- 一個失敗案例可以抹除所有既有有效結果；
- strongest interpretation 可以超出原理論可合理支持的內容；
- strongest baseline 永遠可被窮盡；
- PTE 可以自動解決所有不可判定、不可觀測或不可形式化問題。

本文只研究：

> 如何在 AI 顯著降低形式化、實作、測試與比較成本的時代，把一套強理論公平地推到「可執行後果」層，並在不偷渡真值、不削弱對照組、不丟失負結果與未知狀態的前提下，判斷它究竟留下了什麼。

---

# 1. 問題：理論批評往往發生得太早

## 1.1 文本不是工程

設一套理論為：

$$
T.
$$

它可能存在：

- 定義；
- 命題；
- 比喻；
- 形式符號；
- 圖示；
- 歷史敘事；
- 工程暗示；
- 預測性陳述；
- 本體論主張。

但：

$$
\boxed{
\text{Textual Theory}
\neq
\text{Executable Theory}.
}
$$

一個理論是否「看起來合理」，不能直接回答：

> 它在可執行系統中會造成什麼不同？

## 1.2 反駁也可能只是表面反駁

若批評者選擇 $T^{-}$，即最弱、最字面或最容易攻擊的版本，再證明：

$$
T^{-}
\r\rightarrow\bot,
$$

不能自動推出：

$$
T^{+}
\r\rightarrow\bot.
$$

因此，對強理論而言，存在一個前置問題：

> **你反駁的是這套理論最強、仍可辯護的版本，還是只是最容易失敗的版本？**

## 1.3 但 steelman 也不夠

一般 steelman 可以表示為：

$$
T
\rightarrow
T^{+}.
$$

它改善了詮釋公平性。

但若停在：

> 「我已經替你把理論講到最好了。」

仍然沒有回答：

$$
\boxed{
\text{If }T^{+}\text{ is right, what changes?}
}
$$

PTE 從這裡開始。

---

# 2. 研究譜系：PTE 不是從零開始

PTE 的方法論不是一次孤立發明，而是多條既有研究線的收斂。

## 2.1 重建才是理解的驗收

既有研究已提出：

$$
\boxed{
\text{If the Agent understands, it must be able to reconstruct, transfer, and repair.}
}
$$

並把驗收拆成：

$$
\boxed{
\text{Hard Gates}
\rightarrow
\text{Reconstruction}
\rightarrow
\text{Negative Controls}
\rightarrow
\text{Repair / Recovery}.
}
$$

PTE 將這個原則從：

> 測試 Agent 是否真的理解一個架構

提升為：

> 測試研究者是否真的理解一套理論到足以讓它被公平工程化。

## 2.2 Evidence Ledger

既有方法已要求研究在改稿與實作前先區分：

- 核心命題；
- 已知基礎；
- 新假說；
- 數據來源；
- 可證偽條件；
- 依賴文件；
- MVP；
- 公開等級。

PTE 在此基礎上新增：

- Strongest Interpretation；
- Observable Consequence；
- Operationalization Boundary；
- Matched Baseline；
- Theory-specific Delta；
- Surviving Residue。

## 2.3 Python-first 理論驗證

既有 FELRA 路線已提出：

$$
\text{Theory}
\rightarrow
\text{Python Experiment}
\rightarrow
\text{Evidence}
\rightarrow
\text{Stable Invariant}
\rightarrow
\text{Formal Obligation}.
$$

其核心不是把 Python 當成真理機器，而是把它當成：

- 錯誤暴露器；
- 反例發現器；
- 數值與符號實驗層；
- 邊界測試層；
- 可重現證據層。

PTE 延續這個立場。

## 2.4 Adversarial / Unknown Preservation

既有 VFVM 已拒絕：

$$
\text{所有資料}
\rightarrow
\text{單一驗證 Schema}.
$$

而允許：

$$
\mathcal D
=
\mathcal D_R
\cup
\mathcal D_S
\cup
\mathcal D_K
\cup
\mathcal D_V
\cup
\mathcal D_A
\cup
\mathcal D_U.
$$

其中 $
\mathcal D_A
 $ 保留對抗性、反例與 Schema 外資料，$
\mathcal D_U
$ 保留未知、衝突與不可形式化狀態。

PTE 對理論也採相同態度。

## 2.5 作者脫鉤

既有理論已指出：

$$
\boxed{
\text{理論可運作性}
\not\equiv
\text{作者持續在場}.
}
$$

因此，理論一旦形成可讀結構，就可被視為一個公共研究對象：

$$
T\neq A,
$$

其中 $A$ 是作者。

PTE 因而建立：

$$
\boxed{
\text{Test }T,\text{ not the personality of }A.
}
$$

理論評測不需要轉化為人物評價。

## 2.6 延遲理解與延遲驗證

既有研究定義：

$$
U_{t_0}(x)
<
U_{t_1}(x)
$$

為延遲理解；以及：

$$
E_{t_0}(x)
\neq
E_{t_1}(x)
$$

為延遲驗證。

PTE 將進一步研究：

> AI 是否正在把原本需要數月、數年的理論理解—重建—實作鏈壓縮到小時級？

這將由 PTE-02 正式處理。

## 2.7 全稱主張與存在反例

既有研究已指出：若理論宣稱：

$$
\forall z\in\mathcal Z,
\quad
P(z),
$$

則一個合法：

$$
\exists z^{*}\in\mathcal Z:
\neg P(z^{*})
$$

足以否定該全稱主張。

但：

$$
\boxed{
\text{One counterexample to a universal claim}
\neq
\text{zero value everywhere}.
}
$$

PTE 繼承這個命題。

## 2.8 Matched Benchmark

既有 GARBench 已要求：

- 同 Application Archetype；
- 同 behavior contract；
- 同 Host profile；
- 同驗收面；
- 再比較不同 Agent / Runtime。

PTE 將這個公平性原則提升到理論層：

$$
\boxed{
\text{Theory-derived system}
\quad\text{vs}\quad
\text{matched conventional reconstruction}.
}
$$

---

# 3. PTE 的核心：暫時真值不是相信

## 3.1 定義暫時真值算子

**定義 3.1（暫時真值算子）**

對理論 $T$，定義：

$$
\mathsf{Assume}^{+}(T)
$$

為一個研究操作，其輸出為：

$$
T^{+},
$$

滿足：

1. 不故意採取較弱解讀；
2. 不加入原理論無法合理支持的新主張；
3. 優先選擇能產生可檢驗後果的解讀；
4. 所有補全必須記錄來源與推論狀態；
5. 不因暫時接受而把真值狀態升格為 Established。

## 3.2 它不是 belief operator

PTE 禁止：

$$
\mathsf{Assume}^{+}(T)
\Rightarrow
\mathsf{Believe}(T).
$$

也禁止：

$$
\mathsf{Assume}^{+}(T)
\Rightarrow
\mathsf{True}(T).
$$

正確關係是：

$$
\boxed{
\mathsf{Assume}^{+}(T)
\Rightarrow
\text{maximize testable consequences of a charitable interpretation}.
}
$$

## 3.3 為什麼要暫時接受？

因為許多理論最難被公平檢驗的地方，不是缺乏批評，而是缺乏：

$$
\text{operational bridge}.
$$

PTE 暫時把研究資源放在：

$$
\boxed{
\text{「如果它真的對，接下來應該發生什麼？」}
}
$$

而不是：

$$
\text{「我能不能立刻找到一句錯話？」}
$$

---

# 4. 從 $T$ 到 $T^{+}$：最強可辯護解讀

## 4.1 Strongest Interpretation 不等於自由改寫

PTE 對 $T^{+}$ 要求：

$$
T^{+}
\in
\mathcal I(T),
$$

其中 $
\mathcal I(T)
$ 是理論文本、作者公開定義、可接受形式化與合理語義補全所容許的解讀集合。

## 4.2 禁止超域鋼人化

若原理論只支持：

$$
D_1,
$$

PTE 不得自行擴成：

$$
D_1\cup D_2\cup\cdots\cup D_n.
$$

否則測到的已經不是原理論。

## 4.3 解讀補全必須標記

任何補全應標成：

```text
Declared
Derived
Engineering Extension
Evaluator Assumption
Unknown
```

其中：

- `Declared`：原理論明確聲稱；
- `Derived`：可由原理論合理推得；
- `Engineering Extension`：為了實作而新增；
- `Evaluator Assumption`：測試者選定但原理論未規定；
- `Unknown`：無法確認。

---

# 5. Claim Decomposition：先拆主張，不要一次測整個宇宙

一套強理論 $T$ 可拆成：

$$
T
=
\{C_1,C_2,\ldots,C_n\}.
$$

每個 $C_i$ 至少標記：

$$
C_i
=
(
\text{type},
\text{scope},
\text{evidence},
\text{operationality},
\text{falsifier}
).
$$

## 5.1 主張類型

至少區分：

```text
definition
descriptive claim
predictive claim
engineering claim
formal claim
ontological claim
methodological claim
normative claim
```

## 5.2 為什麼不能混在一起？

因為：

$$
\boxed{
\text{Engineering success}
\not\Rightarrow
\text{Ontological truth}.
}
$$

同樣：

$$
\boxed{
\text{Ontological ambiguity}
\not\Rightarrow
\text{Engineering uselessness}.
}
$$

---

# 6. Formalization：把理論轉成可比較結構

## 6.1 形式化不是證明

形式化：

$$
F:
T^{+}
\rightarrow
\mathcal M
$$

只代表：

> 我們得到了一個可計算／可操作模型。

不能推出：

$$
F(T^{+})
\Rightarrow
T.
$$

## 6.2 最低形式化輸出

至少包括：

```text
entities / variables
states
relations
operators
invariants
constraints
transitions
observables
failure conditions
unknowns
```

## 6.3 不可形式化也必須成為結果

若某核心主張 $C_k$ 無法在不扭曲原意的情況下形式化，應記錄：

$$
\boxed{
\text{Status}(C_k)=\text{Unformalized}.
}
$$

而不是偷偷把它改成容易測的版本。

---

# 7. Operationalization：世界到底哪裡應該不同？

## 7.1 核心問題

對每個主張 $C_i$，必須回答：

> 如果 $C_i$ 為真，與不存在 $C_i$ 相比，可觀測結果應有何差異？

定義：

$$
O(C_i)
=
\Delta(
\text{observable behavior}
).
$$

## 7.2 沒有可觀測差異時

如果：

$$
O(C_i)=\varnothing,
$$

則至少存在三種可能：

1. 主張是純定義；
2. 主張目前不可觀測；
3. 主張尚未完成操作化。

PTE 不把三者混成「已證明」。

## 7.3 操作化梯度

可定義：

$$
\omega(C_i)
\in
[0,1],
$$

其中：

- $0$：沒有可測後果；
- 接近 $0.5$：有間接 proxy；
- $1$：具有直接可重播的判定條件。

---

# 8. Implementation：把假設變成會失敗的東西

## 8.1 可執行化原則

若一套工程主張無法被寫成：

- 程式；
- 規約；
- 模擬；
- 有限域模型；
- 測試；
- 可重播推演；

就不能稱為已完成工程驗證。

## 8.2 先 RED，再 GREEN

對可程式化主張：

$$
\text{Claim}
\rightarrow
\text{Expected Failure}
\rightarrow
\text{Minimal Implementation}
\rightarrow
\text{Fresh Verification}.
$$

若沒有：

$$
\text{Expected Failure},
$$

就很難知道測試是否真的能區分正確與錯誤。

## 8.3 Harness Integrity

PTE 採用：

$$
\boxed{
\text{A Gate That Never Turns Red Is Not Yet Proven to Exist}.
}
$$

因此每個關鍵 invariant 都需要：

- positive control；
- negative control；
- corrupted fixture；
- expected failure class。

---

# 9. Matched Reconstruction：最重要的防自欺層

## 9.1 理論系統

設由 $T$ 導出的系統為：

$$
S_T.
$$

## 9.2 最強已知重建

定義：

$$
B^{*}(T)
$$

為在：

- 相同 observables；
- 相同資料；
- 相同 candidate set；
- 相同資源預算；
- 相同 task contract；
- 相同驗收面；

下，最強的既有 conventional reconstruction。

## 9.3 公平條件

至少要求：

$$
\mathcal O(S_T)
=
\mathcal O(B^{*}),
$$

$$
\mathcal D(S_T)
=
\mathcal D(B^{*}),
$$

$$
\mathcal C(S_T)
\approx
\mathcal C(B^{*}),
$$

其中：

- $\mathcal O$：可觀測資訊；
- $\mathcal D$：資料可見域；
- $\mathcal C$：計算／資源條件。

## 9.4 理論增益

定義：

$$
\boxed{
\Delta_T
=
M(S_T)
-
M(B^{*}(T)).
}
$$

若：

$$
\Delta_T>0,
$$

才開始討論：

$$
\text{theory-specific gain}.
$$

## 9.5 Tie 不等於理論無價值

若：

$$
\Delta_T=0,
$$

正確結論是：

$$
\boxed{
\text{Measured behavior is reconstructible by known machinery}.
}
$$

不是：

$$
T=\text{useless}.
$$

---

# 10. External Challenge：離開自己設計的玩具世界

## 10.1 Synthetic Pass 不夠

若測試資料本身由理論規則生成，則：

$$
\text{Pass}
$$

可能只是：

$$
\text{self-consistency}.
$$

## 10.2 外部資料的功能

External challenge 用來問：

> 理論在沒有為它量身打造的世界裡，是否仍然產生預期結構？

## 10.3 外部資料也不能偷答案

需建立：

$$
\boxed{
\text{Gold Firewall}.
}
$$

即：

- gold label 不進 decision path；
- scorer 與 validator 隔離；
- hidden answer 改變不能改變 decision；
- 若改變，表示測試洩漏。

---

# 11. 反例：只打它真正打中的主張

設：

$$
C:
\forall x\in D,
\quad
P(x).
$$

若發現：

$$
x^{*}\in D,
\quad
\neg P(x^{*}),
$$

則：

$$
\boxed{
C=\text{False}.
}
$$

但不能推出：

$$
\boxed{
\forall C_j\in T,
\quad
C_j=\text{False}.
}
$$

## 11.1 局部失敗不是人格裁決

PTE 評測的是：

$$
C_i,
$$

不是：

$$
A.
$$

所以禁止把：

$$
\text{failure}(C_i)
$$

直接轉成：

$$
\text{failure of theorist}.
$$

---

# 12. Epistemic Salvage：理論可能輸掉宏大主張卻留下好東西

## 12.1 多維價值

定義：

$$
\boxed{
V(T)
=
(
V_C,
V_F,
V_E,
V_P,
V_U
)
}
$$

其中：

- $V_C$：Conceptual Value；
- $V_F$：Formal / Specification Value；
- $V_E$：Engineering Value；
- $V_P$：Predictive Value；
- $V_U$：Unique / Irreducible Value。

## 12.2 可能的狀態

完全可能：

$$
V_C>0,
$$

$$
V_F>0,
$$

$$
V_E>0,
$$

同時：

$$
V_P=\text{Weak},
$$

$$
V_U=\text{NotEstablished}.
$$

這不是矛盾。

## 12.3 避免整體歸零

傳統粗糙批評容易：

$$
\text{Overclaim false}
\Rightarrow
T=0.
$$

PTE 禁止這種推論。

---

# 13. Irreducible Residue：最後到底剩下什麼？

## 13.1 定義

設：

$$
K_{\mathcal B}(T)
$$

為基於當前 baseline family $\mathcal B$ 可重建的部分；

$$
O_{\mathcal E}(T)
$$

為被當前證據 $\mathcal E$ 削除的 overclaim。

則定義：

$$
\boxed{
R_{\mathcal B,\mathcal E}(T)
=
T
-
K_{\mathcal B}(T)
-
O_{\mathcal E}(T).
}
$$

## 13.2 Residue 不是永恆真理

隨 $\mathcal B$ 變強，或 $\mathcal E$ 增加，可能有：

$$
R_{\mathcal B_{t_0},\mathcal E_{t_0}}(T)
\neq
R_{\mathcal B_{t_1},\mathcal E_{t_1}}(T).
$$

## 13.3 真正值得繼續燒資源的是 residue

如果一套理論大部分已可由 known machinery 吸收，未來研究應聚焦：

$$
\boxed{
R(T).
}
$$

而不是重複證明已知部分。

---

# 14. Theory Challenge Ledger

PTE 為每套理論建立一份最小帳本。

```text
Theory ID
Version
Source Boundary
Claim ID
Claim Type
Declared Claim
Strongest Interpretation
Derived Assumptions
Engineering Extensions
Observable Consequence
Operationalization
Implementation
Matched Baseline
Data Scope
Negative Controls
External Dataset
Expected Falsifier
Observed Result
Theory-Specific Delta
Residual Claim
Status
Evidence Receipt
```

---

# 15. PTE 狀態機

對每個主張 $C_i$，建議使用：

```text
UNREAD
INTERPRETED
STEELMANNED
FORMALIZED
OPERATIONALIZED
IMPLEMENTED
BENCHMARKED
RECONSTRUCTED
SUPPORTED
FALSIFIED
PARTIALLY_SUPPORTED
NOT_ESTABLISHED
UNRESOLVED
BLOCKED_BY_EVIDENCE
```

## 15.1 NotEstablished 很重要

PTE 明確區分：

$$
\boxed{
\text{False}
\neq
\text{NotEstablished}
\neq
\text{Unresolved}.
}
$$

這三者不能互換。

---

# 16. PTE 的最低公平性原則

## Principle 1 — Charitable Interpretation

$$
\boxed{
\text{Do not test a weaker theory than the strongest defensible reading.}
}
$$

## Principle 2 — No Hidden Charity

若為理論補了額外機制，必須標成：

$$
\text{Engineering Extension}.
$$

## Principle 3 — Matched Information

$$
\boxed{
\text{Same observables, same candidate space, same evidence access.}
}
$$

## Principle 4 — Independent Reconstruction

Conventional baseline 不應只是：

$$
\text{rename}(S_T).
$$

應具有獨立 causal path。

## Principle 5 — Negative Controls

如果所有例子都能通過，測試尚未證明存在區分力。

## Principle 6 — External Evidence

Toy world 的成功不能直接提升為：

$$
\text{real-world superiority}.
$$

## Principle 7 — Scope-Bounded Conclusion

結論只能覆蓋：

$$
D_{\text{tested}}.
$$

不能自動擴到：

$$
D_{\text{universe}}.
$$

---

# 17. 四種典型結局

## 17.1 Outcome A — Theory Wins

若：

$$
\Delta_T>0
$$

且排除資料洩漏、資源不對等與 baseline 弱化，則：

$$
\boxed{
\text{Theory-specific advantage becomes plausible}.
}
$$

接下來應尋找造成差異的最小 primitive。

## 17.2 Outcome B — Useful Tie

若：

$$
S_T
\approx
B^{*},
$$

但：

$$
M(S_T)
>
M(B_{\text{naive}}),
$$

則理論可能提供：

- 組織價值；
- 規格價值；
- 教學價值；
- 架構壓縮；
- 工程 heuristic。

但 $V_U$ 仍未建立。

## 17.3 Outcome C — Partial Salvage

若部分主張失敗，但：

$$
R(T)\neq\varnothing,
$$

則應保存：

$$
R(T).
$$

## 17.4 Outcome D — No Operational Difference

若：

$$
O(T)=\varnothing
$$

且沒有可合理建立的 proxy，則：

$$
\boxed{
\text{No operational distinction is currently available}.
}
$$

這本身就是結果。

---

# 18. PTE 與一般 falsification 的差異

一般 falsification 問：

> 哪個結果可以否定理論？

PTE 先多問三個問題：

1. 你真的理解它到能做出最強版本嗎？
2. 假設它對，能不能產生可執行後果？
3. 就算後果有效，是否能被已知機制公平重建？

因此：

$$
\boxed{
\text{PTE}
=
\text{Steelman}
+
\text{Engineering}
+
\text{Matched Reconstruction}
+
\text{Falsification}
+
\text{Salvage}.
}
$$

---

# 19. PTE 與「信仰式驗證」的差異

PTE 不允許：

$$
\text{Success}
\Rightarrow
\text{reinterpret theory as correct}.
$$

也不允許：

$$
\text{Failure}
\Rightarrow
\text{move goalposts indefinitely}.
$$

因此每輪前必須 freeze：

```text
claim
scope
observable
baseline
falsifier
success criterion
```

---

# 20. AI 時代為什麼現在才值得把這套方法正式化？

不是因為過去沒有人知道 steelman、prototype、benchmark 或 falsification。

而是因為：

$$
\boxed{
C_{\text{formalize}}
+
C_{\text{implement}}
+
C_{\text{compare}}
+
C_{\text{stress}}
}
$$

正在快速下降。

當：

$$
C_{\text{test}}
$$

開始接近：

$$
C_{\text{discussion}},
$$

原本只適合少數高成本研究計畫的方法，開始可能變成一般研究工作流。

PTE-02 將專門研究這個變化。

---

# 21. 初步研究命題

## PTE-H1：Executable Steelman Hypothesis

對具有工程含義的強理論，Executable Steelman 比純文本 steelman 更能揭露其：

- 真正可用部分；
- 隱含假設；
- 不可操作部分；
- 可被重建部分。

## PTE-H2：Matched Reconstruction Hypothesis

若理論所宣稱的機制不是不可約新 primitive，則隨 baseline family 增強：

$$
\Delta_T
\rightarrow
0.
$$

## PTE-H3：Epistemic Salvage Hypothesis

對部分過度宣稱但含有有效結構的理論，二值評價：

$$
\{\text{true},\text{false}\}
$$

會丟失：

$$
V_C,V_F,V_E.
$$

## PTE-H4：AI Cost Compression Hypothesis

隨 AI 研究工具能力提升：

$$
L_{TE}
\downarrow,
$$

且：

$$
L_H
\downarrow
$$

速度可能快於傳統研究協作模式。

此命題由 PTE-02 展開。

---

# 22. PTE 的失敗模式

PTE 本身也可能失敗。

## 22.1 假 steelman

實際上仍選了容易打倒的版本。

## 22.2 隱藏擴寫

測試者偷偷加入原理論沒有的好機制。

## 22.3 弱 baseline

故意拿舊方法或殘缺方法當對照。

## 22.4 Gold Leakage

答案進入 decision path。

## 22.5 Toy-World Overclaim

在合成資料成功後宣稱現實成立。

## 22.6 Metric Laundering

用 aggregate score 洗掉 hard failure。

## 22.7 Person-Theory Collapse

把 $T$ 與 $A$ 混在一起。

## 22.8 Endless Rescue

每次失敗就重新定義理論，使其永遠不可能被否證。

---

# 23. 最小 PTE Protocol

一輪最小研究可採：

```text
Step 1  Freeze source boundary
Step 2  Extract claims
Step 3  Build strongest defensible interpretation
Step 4  Mark evaluator additions
Step 5  Define observables
Step 6  Define falsifiers
Step 7  Build minimal executable model
Step 8  Construct strongest matched baseline
Step 9  Add negative controls
Step 10 Run synthetic test
Step 11 Run external/adversarial test
Step 12 Measure theory-specific delta
Step 13 Separate value dimensions
Step 14 Preserve unresolved residue
Step 15 Produce reproducibility receipt
```

---

# 24. PTE 的最小輸出

每輪至少產生：

```text
TheoryChallengeLedger
Formalization
Executable Prototype
Matched Baseline
Negative Controls
External Evidence Record
Result Matrix
Residual Claim Set
Reproducibility Receipt
```

---

# 25. 結論：先讓理論有公平機會，再讓它承受公平失敗

本文提出的核心不是：

> 「相信所有奇怪理論。」

也不是：

> 「AI 可以快速證明任何理論。」

而是：

$$
\boxed{
\text{If a theory deserves rejection,}
\text{ let the rejection survive its strongest executable form.}
}
$$

同樣重要的是：

$$
\boxed{
\text{If a theory contains useful structure,}
\text{ do not destroy that structure merely because its strongest claim fails.}
}
$$

因此，PTE 的真正流程不是：

$$
T
\rightarrow
\{\text{True},\text{False}\}.
$$

而是：

$$
\boxed{
T
\rightarrow
T^{+}
\rightarrow
\text{Executable Consequences}
\rightarrow
\text{Matched Reconstruction}
\rightarrow
\text{Adversarial Evidence}
\rightarrow
R(T).
}
$$

這使理論評價從：

> 「我覺得它很厲害。」

或：

> 「我覺得它很荒謬。」

轉變為：

> **假設它是對的。讓它變成真的會做事的東西。然後看看，在最公平的比較與最不友善的證據之後，究竟還剩下什麼。**

這就是暫時真值工程的起點。

---

# 26. 下一篇

**PTE-02｜理論到工程的延遲坍縮：AI 如何改變理論驗證的時間經濟**  
*The Collapse of Theory-to-Engineering Latency in the AI Era*

下一篇將正式研究：

$$
L_{TE},
$$

$$
L_W,
$$

與：

$$
L_H,
$$

並區分：

- wall-clock research time；
- human-attention time；
- machine parallel time；
- coordination cost；
- irreducible evidence time。

其核心問題是：

> **當 AI 把「理解 → 重建 → 實作 → 壓測」從月年級壓縮到小時級，科學方法與理論市場會發生什麼結構性變化？**
