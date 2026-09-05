# Paper 03 — 架構回溯與新鮮重建

## Architecture Backtrace and Fresh Reconstruction

**系列：** TDD × MSSP Architecture Backtrace and Fresh Reconstruction  
**系列代號：** ABFR Series  
**文件版本：** v0.1  
**日期：** 2026-08-28  
**作者：** Neo.K / EveMissLab  

---

## 摘要

Paper 01 提出一個基本區分：測試通過不等同於架構可重建；Paper 02 進一步提出 MSSP 可由人類認知減壓架構反向轉化為 AI 的結構注意力基底。本文進入 ABFR（Architecture Backtrace and Fresh Reconstruction，架構回溯與新鮮重建）的形式核心，回答五個尚未被嚴格固定的問題：

1. 架構回溯究竟從哪一個對象開始？
2. 回溯到什麼條件才算結束？
3. 什麼是足以重新構成目標行為的架構集合？
4. 什麼條件下可以稱為 fresh reconstruction？
5. 重建後需要達到什麼等價關係，才能稱為 replay 成功？

本文將 software architecture 表示為一組帶有 entity、relation、role、authority、state、evidence 與 governance semantics 的架構 assertion，並區分 declared、observed 與 effective 三個層次。Architecture Backtrace 從代表性輸出、測試、狀態轉移或架構 claim 出發，沿 dependency、authority、state provenance、evidence 與 execution relation 反向展開 frontier，直到每一條必要因果鏈都抵達 canonical root、受控 external contract，或被明確標記為 unresolved。本文將此狀態稱為 **Backtrace Closure**。

在回溯結果上，本文定義 **Minimal Sufficient Reconstruction Set（MSRS，最小充分重建集合）**。重要的是，MSRS 不被假設為唯一。若多個可替換 backend 都可以滿足同一組行為與架構不變量，則可能存在多個 inclusion-minimal sufficient sets。因而正確對象不是單一 $S^*$，而是一個集合族：

$$
\mathfrak M_Q
=
\{
S
\mid
S
\text{ is sufficient for }Q
\text{ and inclusion-minimal}
\}
$$

本文接著提出 **Freshness Contract**。Fresh 不被定義為「新資料夾」或「換一個 AI 聊天」，而被定義為移除前一開發狀態中的未宣告因果支援。允許重用已被 canonical specification、hash、lockfile、provenance 或明確 external contract 宣告的材料；不允許依賴上一個 Agent 的私人上下文、偶然 cache、未記錄環境變數、手動初始化、隱藏憑證、歷史工作區殘留或未宣告服務狀態。這使 freshness 成為 causal property，而非視覺上的環境乾淨程度。

最後，本文定義 **Replay Equivalence**。ABFR 不要求所有專案都達到 bit-for-bit identical output。可重現建置（reproducible builds）處理的是在相同來源、建置環境與建置指令下重建指定 artifacts 的 bitwise reproducibility；ABFR 的 replay target 可以是行為、接口、authority、state transition、architecture invariant 或 evidence semantics。因此其等價關係必須在 replay 前明示，而不能在結果出來後重新解釋。

本文將上述元素組合為一個候選 architecture gate，並提供演算法骨架、失敗分類、成本模型與可證偽命題。ABFR v0.1 不宣稱完成形式驗證，也不宣稱任何一次 replay 能證明架構完整；其目的在於把「重新理解並重新建立系統」從一次性的人工活動，轉換成可以由 AI 重複執行、可產生證據、可在後續 Paper 04 中接受 mutation attack 的工程程序。

**關鍵詞：** Architecture Reconstruction；Architecture Backtrace；Fresh Reconstruction；Replay；MSSP；Software Structural Dynamics；Declared Architecture；Observed Architecture；Effective Architecture；Reproducibility；AI Coding Agent；ABFR

---

# 1. 本文在系列中的位置

ABFR Series 的前三篇形成三層關係。

Paper 01 提出：

$$
\text{Behavioral Correctness}
\neq
\text{Architectural Reconstructibility}
$$

並定義：

$$
C_B
=
\text{Behavioral Closure}
$$

與：

$$
C_S
=
\text{Structural Reconstruction Closure}
$$

Paper 02 回答：

> AI 要如何在大型 repository 上，以有限 active context 完成 architecture-wide reasoning？

其候選答案為：

$$
\text{Structured Global Attention}
$$

Paper 03 則回答：

> 如果我們真的要執行 architecture backtrace 與 fresh reconstruction，方法本身到底是什麼？

因此本文的角色不是增加更多概念，而是收斂操作語義。

---

# 2. 與既有 Architecture Reconstruction 的關係

Software Architecture Reconstruction 不是新問題。

SEI 將 architecture reconstruction 定義為：從已實作系統取得其 as-built architecture，利用抽取出的資訊逐步建立更高層的 architectural representation。成功的 reconstruction 可以用於重新文件化、比較 as-built 與 as-designed architecture、分析系統、支援 reengineering 與 reuse。

因此 ABFR 不宣稱發明：

$$
\text{as-built}
\leftrightarrow
\text{as-designed}
$$

的比較。

ABFR 真正增加的是一個方向反轉。

傳統 reconstruction 的典型終點是：

$$
\text{Implemented System}
\rightarrow
\text{Recovered Architecture}
$$

ABFR 要求 recovered / reconciled architecture 再成為新的 execution input：

$$
\boxed{
\text{Implemented System}
\rightarrow
\text{Backtrace}
\rightarrow
\text{Reconciled Architecture}
\rightarrow
\text{Fresh Reconstruction}
\rightarrow
\text{Replay}
}
$$

因此本文把「能否得到有用的 architecture representation」與「該 representation 是否具有 reconstruction sufficiency」分開。

---

# 3. 基本架構宇宙

令一個專案在時間 $t$ 、context $c$ 下的架構 universe 為：

$$
\mathcal U(t,c)
$$

其元素不是只有 source file。

在本文的抽象中，architecture assertion 可以來自：

$$
\mathcal U
=
\mathcal E
\cup
\mathcal R
\cup
\mathcal L
\cup
\mathcal A
\cup
\mathcal S
\cup
\mathcal V
\cup
\mathcal G
$$

其中：

- $\mathcal E$：entities；
- $\mathcal R$：typed relations；
- $\mathcal L$：roles / responsibilities；
- $\mathcal A$：authorities；
- $\mathcal S$：runtime / persistent states；
- $\mathcal V$：evidence；
- $\mathcal G$：governance events。

這與 Dynamic MSSP / SSD 的 neutral architecture state 一致：MSSP taxonomy 可以被替換，但架構實體、關係、責任、權限、證據、狀態與治理仍需可表示。

因此：

$$
\boxed{
\text{ABFR does not require FMS/SMS/TMS names}
}
$$

但 ABFR 要求至少有足夠結構能回答：

- 什麼東西存在？
- 誰依賴誰？
- 誰負責什麼？
- 誰有權做什麼？
- 哪個狀態影響結果？
- 哪個 claim 有什麼證據？
- 哪些是宣告、觀察與實際生效的狀態？

---

# 4. Architecture Assertion

為了避免把「架構」當成模糊整體，本文把最小推理單位稱為 architecture assertion。

一個 assertion 可表示為：

$$
a
=
(
s,
p,
o,
\ell,
c,
\tau,
v
)
$$

其中：

- $s$：subject；
- $p$：predicate / relation type；
- $o$：object / value；
- $\ell$：layer；
- $c$：context；
- $\tau$：time / validity interval；
- $v$：evidence references。

layer 至少可取：

$$
\ell
\in
\{
d,o,e
\}
$$

分別表示：

$$
d=\text{declared}
$$

$$
o=\text{observed}
$$

$$
e=\text{effective}
$$

因此「payment-service 可以寫 payment-state」不是一個沒有來源的句子，而是一個可指出：

- 是誰宣告的；
- runtime 是否觀察到；
- 在什麼 context 生效；
- 有什麼 evidence；
- 是否仍在 validity interval；

的 architecture assertion。

---

# 5. Declared / Observed / Effective

令：

$$
A_d
\subseteq
\mathcal U
$$

表示 declared architecture assertion 集合；

$$
A_o
\subseteq
\mathcal U
$$

表示 observed assertion 集合；

$$
A_e
\subseteq
\mathcal U
$$

表示在目前 governance / runtime semantics 下實際有效的 assertion 集合。

三者不要求相等。

典型情況包括：

$$
A_o
\setminus
A_d
\neq
\varnothing
$$

表示出現未宣告的 observed structure；

以及：

$$
A_d
\setminus
A_o
\neq
\varnothing
$$

表示某些 declared structure 沒有被觀察到。

但：

$$
A_e
\neq
A_o
$$

也完全可能成立。

例如某 service 被 telemetry 觀察到嘗試寫入某資料表，但 policy 拒絕其權限，則：

$$
\text{observed write attempt}
\in
A_o
$$

不代表：

$$
\text{effective write authority}
\in
A_e
$$

因此：

$$
\boxed{
\text{Observed}
\neq
\text{Effective}
}
$$

是 ABFR 必須保留的語義。

---

# 6. Architecture State

本文將某一時刻的 architecture state 抽象為：

$$
\mathcal A(t,c)
=
(
A_d,
A_o,
A_e,
V,
G
)
$$

其中：

- $V$ 是 supporting evidence；
- $G$ 是 governance events / decisions。

這不是宣稱所有架構都能完全被五個變量捕捉，而是定義 ABFR 的最低操作界面。

MSSP / SSD 可以保留更完整的 state，例如 compensation、burden、snapshot 與 profile-specific role；其他架構方法也可以加入自己的 primitive。

ABFR 只要求：

$$
\operatorname{Project}_{ABFR}
(
\mathcal A_{\text{native}}
)
$$

能投影出足以執行 backtrace、reconstruction 與 replay 的 neutral state。

---

# 7. Backtrace Target

Architecture Backtrace 不應從「整個 repository」這個模糊目標開始。

定義 target set：

$$
Q
=
\{
q_1,q_2,\ldots,q_m
\}
$$

每一個 $q_i$ 可以是：

- 一個通過的 test；
- 一個 runtime output；
- 一個 API contract；
- 一個 state transition；
- 一個 security / authority invariant；
- 一個 architecture claim；
- 一個 failure；
- 一個 user-visible capability；
- 一個 deployable artifact；
- 一個代表性 workflow。

例如：

$$
q_1=
\text{POST /payment returns accepted}
$$

或：

$$
q_2=
\text{TMS-A can run without TMS-B}
$$

或：

$$
q_3=
\text{only CommitGate may write World state}
$$

ABFR 的回溯問題不是：

> 這個 repository 有哪些檔案？

而是：

$$
\boxed{
\text{What structural support makes }Q\text{ true?}
}
$$

---

# 8. Backtrace Frontier

令初始 frontier 為：

$$
F_0
=
\operatorname{Seed}(Q)
$$

其中 Seed 將 target 對應到可追蹤 architecture entities / assertions。

在第 $k$ 輪：

$$
F_k
\subseteq
\mathcal U
$$

Agent 對每一個：

$$
x\in F_k
$$

執行 predecessor expansion。

定義：

$$
\operatorname{Pred}(x)
$$

可以沿至少下列 relation 展開：

- compile dependency；
- runtime dependency；
- data read；
- data write；
- event publish / consume；
- interface；
- permission / authority；
- deployment；
- test / fixture；
- external service；
- AI context；
- recovery；
- compensation；
- evidence provenance；
- state provenance；
- configuration origin。

因此：

$$
F_{k+1}
=
\left(
\bigcup_{x\in F_k}
\operatorname{Pred}(x)
\right)
\setminus
V_k
$$

其中：

$$
V_k
$$

為已拜訪的 structural assertions / entities。

更新：

$$
V_{k+1}
=
V_k
\cup
F_k
$$

---

# 9. 為什麼 Backtrace 不是單純 Dependency Graph

如果 ABFR 只追：

$$
\text{import}
$$

或：

$$
\text{call graph}
$$

那麼它只能找到部分 architecture support。

例如某 operation 的成功可能取決於：

$$
\text{Source}
+
\text{Config}
+
\text{Credential}
+
\text{Policy}
+
\text{Database State}
+
\text{External Contract}
$$

其中只有 Source 與 Config 可能出現在 static dependency graph。

因此本文採：

$$
D_{\text{effective}}
\supseteq
D_{\text{static}}
$$

作為預設假設。

Architecture Backtrace 必須允許 relation types 超出程式 import。

否則：

$$
\text{Backtrace Closure}
$$

只會變成：

$$
\text{Static Graph Closure}
$$

兩者不能混為一談。

---

# 10. Grounded Root

Backtrace 不可能無限向外追。

因此需要定義何時一條 frontier 可以合法停止。

若 assertion / entity $x$ 滿足下列任一條件，稱：

$$
\operatorname{Grounded}(x)=1
$$

### G1. Canonical Source Root

 $x$ 已由 canonical repository、canonical specification、版本化 schema 或正式 artifact 定義。

### G2. Pinned Dependency Root

 $x$ 是明確版本、digest、lockfile、container image 或可驗證材料。

### G3. Controlled External Contract

 $x$ 是刻意保留在重建邊界之外的 external service，但其 interface、authority、版本要求與 mock / acceptance semantics 已明示。

### G4. Declared Runtime Primitive

 $x$ 是可接受的 runtime primitive，例如 OS facility、language runtime、database engine，但其使用條件已被 reconstruction contract 明示。

### G5. Explicit Unresolved Root

 $x$ 尚未被充分理解，但被標記：

$$
\operatorname{status}(x)=\text{UNRESOLVED}
$$

且不允許在 closure decision 中被當成已解決。

這一條非常重要。

Backtrace 可以結束於「不知道」，但不能：

$$
\boxed{
\text{unknown}
\rightarrow
\text{silently treated as known}
}
$$

---

# 11. Backtrace Closure

令 unresolved frontier：

$$
U_k
=
\{
x\in F_k
\mid
\operatorname{Grounded}(x)=0
\}
$$

若：

$$
U_k=\varnothing
$$

則 traversal 可以停止。

但這仍不等於通過。

定義：

$$
C_{BT}=1
$$

需要：

1. 所有 target $Q$ 已有 structural support path；
2. 所有必要 predecessor 已被拜訪或明示排除；
3. 所有停止節點皆為 grounded root；
4. unresolved items 已被明示；
5. declared / observed divergence 已被記錄；
6. evidence provenance 足以追查重要非 deterministic claim。

因此若仍存在：

$$
U_{\text{explicit}}
\neq
\varnothing
$$

可以得到：

$$
C_{BT}=\text{PARTIAL}
$$

而不是 PASS。

---

# 12. Backtrace Result

Architecture Backtrace 的輸出不是一篇摘要，而是一個結構化結果：

$$
B_Q
=
(
V_Q,
E_Q,
D_Q,
U_Q,
P_Q
)
$$

其中：

- $V_Q$：visited structural nodes；
- $E_Q$：typed relations；
- $D_Q$：declared / observed / effective divergences；
- $U_Q$：unresolved claims；
- $P_Q$：evidence / provenance references。

其最重要用途是產生下一階段：

$$
\text{Reconstruction Candidates}
$$

而不是供人閱讀後結案。

---

# 13. Sufficiency

令：

$$
S
\subseteq
B_Q
$$

是一組 reconstruction inputs。

定義 reconstruction operator：

$$
\mathcal R(S,E_f)
=
P_S
$$

其中：

- $S$：架構與資源集合；
- $E_f$：fresh environment；
- $P_S$：重建後系統。

若 $P_S$ 能對 target set $Q$ 滿足預先定義的 replay equivalence 與 architecture invariants，則稱：

$$
\operatorname{Sufficient}(S,Q)=1
$$

形式上：

$$
\operatorname{Sufficient}(S,Q)
\iff
\left[
\mathcal O_Q(P_S,E_f)
\simeq_Q
\mathcal O_Q(P_{\text{ref}},E_{\text{ref}})
\right]
\land
\left[
\mathcal I_Q(P_S)=1
\right]
$$

其中：

- $\mathcal O_Q$：對 $Q$ 的 observable projection；
- $\simeq_Q$：預先定義的 replay equivalence；
- $\mathcal I_Q$：對 $Q$ 必須成立的 architecture invariants。

---

# 14. Minimal Sufficient Reconstruction Set

這一概念是 ABFR 的核心。

一個集合：

$$
S
$$

若滿足：

$$
\operatorname{Sufficient}(S,Q)=1
$$

且對任意 proper subset：

$$
S'
\subsetneq
S
$$

都有：

$$
\operatorname{Sufficient}(S',Q)=0
$$

則稱：

$$
S
$$

為 **inclusion-minimal sufficient reconstruction set**。

因此：

$$
\boxed{
\operatorname{MSRS}(S,Q)
}
$$

成立。

---

# 15. Minimal 不等於 Minimum

這裡必須嚴格區分。

**Minimal** 表示：

> 拿掉其中任一必要部分後，就不再充分。

**Minimum** 表示：

> 在所有充分集合裡，它的 cardinality 或成本是全域最小。

ABFR v0.1 只要求 minimal，不要求 minimum。

原因是找到：

$$
\arg\min_S
C(S)
$$

可能本身就是昂貴 combinatorial optimization。

而且架構通常存在多個替代路徑。

例如：

$$
S_A
=
\{
\text{Core},
\text{SQLite Backend}
\}
$$

以及：

$$
S_B
=
\{
\text{Core},
\text{PostgreSQL Backend}
\}
$$

都可能對某個 target $Q$ 充分且 inclusion-minimal。

因此真正的對象是：

$$
\boxed{
\mathfrak M_Q
=
\{
S
\mid
\operatorname{MSRS}(S,Q)
\}
}
$$

而不是假設存在唯一：

$$
S^*
$$

---

# 16. MSRS 與 MSSP Island Test

MSSP 的 island test 已經具有 MSRS 的局部雛形：

1. 只載入宣告的最小 SMS；
2. 恰好載入一個 TMS；
3. 外部工具替換為 stub；
4. 執行代表任務；
5. 驗證輸入、輸出與拒絕權限；
6. 確認沒有其他 TMS 被載入。

它測的是：

$$
\operatorname{Sufficient}
(
SMS_{\min}
+
TMS_i,
q_i
)
$$

以及：

$$
TMS_j
\notin
\operatorname{LoadedSet}
$$

對：

$$
j\neq i
$$

ABFR 將這個局部問題一般化為 system / milestone level：

$$
\text{What is the minimal sufficient structural support for }Q?
$$

因此 island test 可以視為一種 constrained local MSRS probe，但 ABFR 不等同於 island testing。

---

# 17. Freshness：不是「新資料夾」

如果 reconstruction 只是：

- clone 到另一個資料夾；
- 沿用相同 global cache；
- 沿用已登入憑證；
- 依賴前一個 Agent 記得的操作；
- 沿用未宣告資料庫狀態；

那麼它不構成有效 fresh reconstruction。

本文提出：

$$
\boxed{
\text{Freshness is causal, not cosmetic}
}
$$

---

# 18. Prior-State Support

令上一個開發狀態提供的所有因果支援為：

$$
H_{\text{prev}}
$$

其中包含：

- private conversation context；
- workspace residue；
- untracked patch；
- local generated file；
- cache；
- database residue；
- environment variable；
- credential；
- local service；
- manual initialization；
- operator memory；
- implicit tool configuration。

其中已被正式宣告為 reconstruction input 的部分為：

$$
H_{\text{declared}}
\subseteq
H_{\text{prev}}
$$

未宣告部分為：

$$
H_{\text{hidden}}
=
H_{\text{prev}}
\setminus
H_{\text{declared}}
$$

Fresh Reconstruction 的核心要求為：

$$
\boxed{
\operatorname{Support}(P_S)
\cap
H_{\text{hidden}}
=
\varnothing
}
$$

也就是重建結果不能受到上一輪未宣告狀態的必要因果支援。

---

# 19. Freshness Contract

本文定義 Freshness Contract：

$$
\mathcal F
=
(
F_C,
F_W,
F_D,
F_R,
F_A,
F_X,
F_N
)
$$

其中：

### $F_C$ — Context Freshness

新的 AI / human executor 不得取得未納入 canonical artifact 的前序推理。

### $F_W$ — Workspace Freshness

重建 workspace 不得依賴 untracked、temporary 或 previous-run generated state，除非這些已被宣告為正式 material。

### $F_D$ — Dependency Freshness

依賴應由 lockfile、manifest、digest、container、package index policy 或同等機制重建，而非沿用偶然已安裝狀態。

### $F_R$ — Runtime State Freshness

database、queue、cache、filesystem state、session 等必須 reset、fixture-ize、snapshot-pin 或明確標記為 external state contract。

### $F_A$ — Authority Freshness

憑證、token、role、deployment permission 與其他 authority 必須重新依 contract 取得；不能因開發機器「剛好登入」而算成功。

### $F_X$ — External Dependency Freshness

外部 service 必須被 pin、stub、mock、sandbox、contract-test 或 acceptance-test 明確界定。

### $F_N$ — Nondeterminism Control

time、randomness、scheduler、locale、hostname、build path、network variability 等若影響 target，必須固定、允許變異並定義 equivalence，或明確標記為 uncontrolled。

---

# 20. Freshness 不等於不准重用任何東西

Freshness 的目的不是浪費資源。

如果一個 dependency 已經有：

- immutable digest；
- verified container image；
- locked version；
- SLSA / in-toto provenance；
- reproducible artifact；
- canonical snapshot；

那麼它可以被重用。

關鍵不是：

$$
\text{Everything must be newly downloaded}
$$

而是：

$$
\boxed{
\text{Every causal input must be declared or intentionally externalized}
}
$$

因此：

$$
\text{Reuse}
\not\Rightarrow
\text{Not Fresh}
$$

反之：

$$
\text{New Directory}
\not\Rightarrow
\text{Fresh}
$$

---

# 21. Freshness 與 Reproducible Builds 的區分

Reproducible Builds 社群通常把 reproducible build 定義為：給定相同 source code、build environment 與 build instructions，任何一方都能重新建立 bit-for-bit identical 的指定 artifact。

這是一個非常強且重要的 supply-chain / auditability property。

SLSA provenance 也強調：

- source；
- materials；
- parameters；
- environment；
- builder；
- invocation；

應被記錄，以描述 artifact 如何被產生；若 build 可重現，重新執行 invocation 應能得到相同 artifact。

ABFR 直接借用這些思想來收斂因果輸入，但兩者目標不同。

Reproducible Build 主要問：

$$
\text{Can we reproduce the artifact bits?}
$$

ABFR 問：

$$
\text{Can the claimed architecture reconstruct the required system semantics?}
$$

因此：

$$
\boxed{
\text{Bitwise Reproducibility}
\text{ is a possible ABFR replay relation, not the only one}
}
$$

---

# 22. Replay Target

重建後得到：

$$
P_S
$$

接著執行 replay。

Replay workload：

$$
Q
=
\{
q_1,\ldots,q_m
\}
$$

必須在 backtrace 前或至少 replay 前固定。

每個 target 應定義 observable：

$$
\mathcal O_i
$$

以及 invariant：

$$
\mathcal I_i
$$

例如：

### API Target

$$
\mathcal O_i
=
\{
\text{status},
\text{schema},
\text{state transition}
\}
$$

### Architecture Isolation Target

$$
\mathcal O_i
=
\{
\text{loaded modules},
\text{external calls},
\text{authority checks}
\}
$$

### Build Target

$$
\mathcal O_i
=
\{
\text{artifact digest}
\}
$$

### Recovery Target

$$
\mathcal O_i
=
\{
\text{post-crash state},
\text{commit classification},
\text{compensation requirement}
\}
$$

---

# 23. Replay Equivalence

定義：

$$
\mathcal O_Q(P,E)
$$

為系統 $P$ 在環境 $E$ 下對 targets $Q$ 的 observable projection。

若：

$$
\mathcal O_Q(P_S,E_f)
\simeq_Q
\mathcal O_Q(P_{\text{ref}},E_{\text{ref}})
$$

且：

$$
\mathcal I_Q(P_S)=1
$$

則稱 replay equivalent：

$$
P_S
\equiv_{Q,\mathcal I}
P_{\text{ref}}
$$

---

# 24. 等價關係必須事先定義

若結果跑出來後才說：

> 這個差異不重要。

那麼 replay 很容易變成不可證偽。

因此：

$$
\simeq_Q
$$

必須在執行前固定。

可能的 equivalence profile 包括：

### E1. Bitwise Equivalence

$$
h(O')=h(O)
$$

### E2. Schema Equivalence

欄位、型別、required constraints 等價。

### E3. Behavioral Equivalence

代表性輸入下具有相同可觀察結果。

### E4. State-Transition Equivalence

$$
s
\xrightarrow{a}
s'
$$

在允許容差內一致。

### E5. Authority Equivalence

允許 / 拒絕決策與 effect boundary 一致。

### E6. Architecture-Invariant Equivalence

例如：

$$
TMS_A
\nrightarrow
TMS_B
$$

或：

$$
\operatorname{WorldWriter}
=
\{\text{CommitGate}\}
$$

### E7. Evidence Equivalence

不是要求 log 完全相同，而要求必要 claim 都能產生相同類別的可追溯 evidence。

---

# 25. Replay 不是 Deterministic Execution Replay 的同義詞

傳統 deterministic replay 系統主要記錄 nondeterministic inputs，使程式可以重現相同 execution path，常用於 debugging。

ABFR replay 可以使用 deterministic replay 技術，但它的問題層級不同。

Deterministic execution replay 問：

$$
\text{Can we replay this execution?}
$$

ABFR 問：

$$
\text{Can we reconstruct a system that still satisfies the declared architecture and target semantics?}
$$

前者可以在同一 architecture 下重播一次 execution。

後者可能更換：

- machine；
- workspace；
- Agent；
- backend；
- build；
- dependency source；

只要仍滿足：

$$
\simeq_Q
$$

與：

$$
\mathcal I_Q
$$

---

# 26. Reconstruction Closure

本文定義 Structural Reconstruction Closure：

$$
C_S(Q)=1
$$

需要同時滿足：

$$
C_{BT}=1
$$

存在至少一個：

$$
S\in\mathfrak M_Q
$$

Freshness Contract：

$$
\mathcal F=1
$$

以及：

$$
P_S
\equiv_{Q,\mathcal I}
P_{\text{ref}}
$$

因此：

$$
\boxed{
C_S
=
C_{BT}
\land
C_{\text{MSRS}}
\land
C_F
\land
C_R
}
$$

其中：

- $C_{BT}$：Backtrace Closure；
- $C_{\text{MSRS}}$：存在被驗證充分的 minimal reconstruction set；
- $C_F$：Freshness Contract 成立；
- $C_R$：Replay Equivalence 成立。

---

# 27. 與 TDD Closure 結合

Paper 01 定義：

$$
C_B
=
\text{Behavioral Closure}
$$

因此 Paper 03 現在可以把 architecture gate 展開為：

$$
\boxed{
G_{\text{ABFR}}
=
C_B
\land
C_{BT}
\land
C_{\text{MSRS}}
\land
C_F
\land
C_R
}
$$

若：

$$
G_{\text{ABFR}}=1
$$

表示：

- 目標行為已有可執行測試閉包；
- 架構支援已被回溯；
- reconstruction set 已被縮到 inclusion-minimal；
- fresh boundary 已成立；
- 新系統對預定 targets replay equivalent。

Paper 04 再加入：

$$
C_D
=
\text{Discriminative Closure}
$$

變成：

$$
G_{\text{ABFR+Attack}}
=
G_{\text{ABFR}}
\land
C_D
$$

---

# 28. ABFR v0.1 演算法骨架

以下不是唯一實作，而是一個可供其他 AI 重現的方法骨架。

```text
INPUT
  canonical source C
  declared architecture A_d
  tests T
  replay targets Q
  invariants I
  equivalence profile EQ
  freshness contract F

PHASE 1 — Behavioral baseline
  run focused tests
  require baseline green
  freeze commit / artifact identity

PHASE 2 — Seed backtrace
  map Q to structural entities and assertions
  frontier <- seed(Q)
  visited <- empty
  unresolved <- empty

PHASE 3 — Backtrace traversal
  while frontier is not empty:
      take bounded subset of frontier
      inspect declared structure
      inspect observed evidence
      derive effective relations where allowed
      expand dependency / authority / state / evidence predecessors
      mark grounded roots
      record divergences
      record unresolved claims
      update frontier

PHASE 4 — Reconcile
  compare declared / observed / effective
  produce structural support graph B_Q
  fail or mark partial if critical unresolved claims remain

PHASE 5 — Derive reconstruction candidate
  start from structural support set
  remove candidate item
  reconstruct / run focused replay
  if still sufficient:
      keep item removed
  else:
      restore item
  repeat until inclusion-minimal under chosen search order

PHASE 6 — Fresh reconstruction
  create fresh context and workspace
  materialize only declared inputs
  reconstruct dependencies and runtime state
  acquire authority only through declared contract
  initialize external services through declared boundary

PHASE 7 — Replay
  run Q
  evaluate EQ
  evaluate I
  emit evidence

OUTPUT
  backtrace graph
  declared/observed/effective diff
  MSRS candidate
  freshness evidence
  replay evidence
  closure verdict
```

---

# 29. MSRS 搜尋不保證全域最優

上面的 remove-one-by-one 演算法只能產生一個：

$$
\text{inclusion-minimal}
$$

candidate。

它不保證：

$$
\min |S|
$$

也不保證：

$$
\min C(S)
$$

而且搜尋順序不同可能得到不同：

$$
S_i
\in
\mathfrak M_Q
$$

這不是 bug。

如果 project 支援多個合法 architecture profile，那麼多個 MSRS 是合理結果。

因此 ABFR 工具應記錄：

$$
\operatorname{search\ order}
$$

與：

$$
\operatorname{candidate\ derivation}
$$

以便另一個 Agent 重播。

---

# 30. Fresh Reconstruction Evidence

Fresh Reconstruction 不應只回報：

```text
PASS
```

至少需要 evidence packet：

```text
reconstruction:
  baseline_commit: ...
  canonical_sources: ...
  dependency_materials: ...
  workspace_identity: ...
  context_policy: fresh
  previous_workspace_reused: false

freshness:
  context: pass
  workspace: pass
  dependencies: pass
  runtime_state: pass
  authority: pass
  external_contracts: pass
  nondeterminism: controlled | bounded | unresolved

replay:
  targets: ...
  equivalence_profile: ...
  invariants: ...
  results: ...

unresolved:
  ...
```

這使「fresh」本身可被稽核。

---

# 31. Provenance 的角色

ABFR 不要求第一版就建立 cryptographic ledger。

但重要材料至少應能回答：

- 來源是什麼？
- revision / digest 是什麼？
- 何時取得？
- 誰取得？
- 用於哪個 claim？
- 是否仍 fresh？
- 是否存在 counterevidence？

這與 SLSA / in-toto provenance 的精神一致：artifact 的來源、materials、invocation、builder 與 environment 都需要有可追溯描述。

因此：

$$
\boxed{
\text{Replay without provenance}
}
$$

只能提供較弱的 closure confidence。

---

# 32. Failure Semantics

ABFR v0.1 將失敗分成五個階段。

## BT — Backtrace Failures

### BT-01 Missing Seed

target 無法映射到 architecture entity / assertion。

### BT-02 Frontier Explosion

relation 過度寬鬆，frontier 無界擴張。

### BT-03 Ungrounded Root

回溯停在沒有 canonical / external contract 的節點。

### BT-04 Evidence Gap

重要 claim 沒有足夠 evidence。

### BT-05 Declared/Observed Drift

架構宣告與 observed structure 不一致，且尚未治理。

---

## MS — Reconstruction-Set Failures

### MS-01 Hidden Necessary Dependency

刪除後 replay 失敗，證明該 dependency 原本未被標為必要。

### MS-02 False Core

聲稱必要的 entity 被移除後仍完全通過。

### MS-03 Non-Isolatable Module

宣稱可替換的 module 無法在其他 sibling 缺席下重建。

### MS-04 Search-Order Sensitivity

不同縮減順序產生高度不同 MSRS，需要保留多個 candidate。

---

## FR — Freshness Failures

### FR-01 Context Leakage

新的 Agent 依賴前序聊天或私人 reasoning。

### FR-02 Workspace Leakage

依賴 previous-run file、cache 或 local patch。

### FR-03 Dependency Leakage

依賴未 manifest / lock / pin 的本機 package。

### FR-04 Runtime-State Leakage

依賴舊 database、queue、session 或 filesystem state。

### FR-05 Authority Leakage

依賴已登入憑證或人工特權。

### FR-06 External-State Leakage

依賴未受 contract 控制的外部 service。

### FR-07 Nondeterminism Leakage

time、randomness、scheduler 等造成不可解釋 divergence。

---

## RP — Replay Failures

### RP-01 Behavioral Divergence

代表行為不同。

### RP-02 State Divergence

狀態轉移不同。

### RP-03 Authority Divergence

allow / deny semantics 不同。

### RP-04 Architecture-Invariant Violation

重建系統行為看似正常，但 architecture rule 被破壞。

### RP-05 Evidence Divergence

結果成立，但失去原先要求的 traceability。

### RP-06 Undefined Equivalence

執行後才開始決定哪些差異「算相同」。

---

## CL — Closure Failures

### CL-01 Premature Closure

仍有 critical unresolved item 卻宣稱完成。

### CL-02 Single-Executor Closure

只有原始 Agent 能重建，fresh executor 失敗。

### CL-03 Non-Replayable Procedure

步驟依賴一次性人工判斷，沒有被記錄成 procedure / evidence。

---

# 33. Closure Verdict

因此 verdict 不應只有 PASS / FAIL。

本文建議：

$$
V
\in
\{
\text{PASS},
\text{PARTIAL},
\text{FAIL},
\text{INCONCLUSIVE}
\}
$$

### PASS

所有 mandatory closure criteria 成立。

### PARTIAL

核心流程成立，但存在明示、非 blocking unresolved item。

### FAIL

至少一個 mandatory criterion 不成立。

### INCONCLUSIVE

evidence 或 environment 不足以判定。

這比把所有 uncertain state 壓成 boolean 更適合 architecture reasoning。

---

# 34. Architecture Backtrace 的成本

回溯不是免費的。

令：

$$
|V|
$$

為 architecture nodes；

$$
|E|
$$

為 relations。

若做無差別 traversal，成本可能接近：

$$
O(|V|+|E|)
$$

但實務上昂貴部分不只 graph traversal，而是：

- source inspection；
- runtime observation；
- tool execution；
- AI reasoning；
- external contract verification；
- reconstruction attempts。

因此真正成本可寫成：

$$
C_{BT}
=
C_{\text{inspect}}
+
C_{\text{observe}}
+
C_{\text{reason}}
+
C_{\text{tool}}
+
C_{\text{reconcile}}
$$

Paper 02 的 Structural Attention 目的，就是降低不必要的：

$$
C_{\text{inspect}}
$$

與：

$$
C_{\text{revisit}}
$$

---

# 35. Reconstruction 的成本

若 naive 搜尋所有 subset：

$$
2^{|S|}
$$

顯然不可接受。

因此 ABFR v0.1 不追求 exhaustive proof of minimality。

它採：

- architecture-guided elimination；
- dependency-aware pruning；
- role-based priority；
- test impact；
- island testing；
- known substitute profiles；

產生 practical inclusion-minimal candidate。

因此：

$$
\boxed{
\text{ABFR v0.1 is an engineering methodology, not an optimal-set solver}
}
$$

---

# 36. 一個重要命題：Pass 不推出 Declared Sufficiency

考慮：

$$
P
=
f(A,B,H)
$$

其中 $H$ 是 hidden support。

若開發環境總有 $H$，則：

$$
T(P)=\text{PASS}
$$

並不能推出：

$$
\operatorname{Sufficient}(\{A,B\},Q)=1
$$

只有當：

$$
H
$$

被移除，而：

$$
\mathcal R(\{A,B\},E_f)
$$

仍 replay equivalent，才能對 declared sufficiency 提供實證支持。

因此 ABFR 的基本實證邏輯是：

$$
\boxed{
\text{Remove undeclared support}
\rightarrow
\text{reconstruct}
\rightarrow
\text{observe whether the claim survives}
}
$$

---

# 37. 一個重要命題：Backtrace 不應只向後，也應重新向前

如果只做：

$$
P
\rightarrow
A_o
$$

我們得到的是 architecture recovery。

如果再做：

$$
A_o
\leftrightarrow
A_d
$$

我們得到 architecture conformance information。

ABFR 另外要求：

$$
A_r
\rightarrow
P'
$$

其中：

$$
A_r
$$

是 reconciliation 後被選為 reconstruction input 的 architecture state。

所以：

$$
\boxed{
\text{Backtrace}
+
\text{Forward Reconstruction}
}
$$

形成一個雙向驗證環：

$$
P
\rightarrow
A_r
\rightarrow
P'
$$

若：

$$
P'
\not\equiv_{Q,\mathcal I}
P
$$

則：

$$
A_r
$$

對 $Q$ 不充分。

---

# 38. 一個重要命題：Freshness 是對 Hidden Causality 的測試

Freshness 不是追求某種潔癖。

它是要測：

$$
\exists h
\in
H_{\text{hidden}}
$$

使：

$$
h
\rightarrow
q
$$

是否成立。

如果把 $h$ 拿掉後：

$$
q
$$

不再成立，那麼：

$$
h
$$

就是 architecture support 的一部分，應：

1. 被正式宣告；
2. 被替換；
3. 被移除；
4. 或讓 architecture claim 降級。

因此：

$$
\boxed{
\text{Fresh Reconstruction}
=
\text{Hidden-Causality Probe}
}
$$

這是 ABFR 相對普通「重跑一次」更精確的含義。

---

# 39. 一個重要命題：Replay Equivalence 必須 task-relative

要求所有系統：

$$
P'=P
$$

通常太強也沒有必要。

如果一個 backend 被合法替換，只要：

$$
P'
\equiv_{Q,\mathcal I}
P
$$

即可。

因此 architecture reconstructibility 是相對於：

$$
Q
$$

與：

$$
\mathcal I
$$

的性質。

完整寫法應是：

$$
\operatorname{Reconstructible}
(
P,
A,
Q,
\mathcal I,
\mathcal F,
\simeq_Q
)
$$

而不是單獨說：

$$
P
\text{ is reconstructible}
$$

---

# 40. 一個重要命題：架構閉包是分層的

一個專案可以在 feature level 閉包，但在 system level 未閉包。

令：

$$
Q_1
\subset
Q_2
\subset
\cdots
\subset
Q_n
$$

則可能：

$$
C_S(Q_1)=1
$$

但：

$$
C_S(Q_n)=0
$$

所以 ABFR 應支援：

- module-level closure；
- subsystem-level closure；
- milestone-level closure；
- release-level closure。

這和 MSSP 的漸進使用原則一致，不要求小專案一開始就做全域重建。

---

# 41. ABFR 與 AI Context 的特殊條件

對 human executor 而言，fresh 通常是：

- clean checkout；
- clean environment；
- documented build；
- new operator。

對 AI executor，還多一個以前不常被工程方法正式測量的來源：

$$
C_{\text{implicit AI}}
$$

也就是：

- 前一輪 conversation；
- hidden scratch state；
- previous tool observation；
- model-side summary；
- unstated plan。

因此 AI fresh replay 最重要的實驗之一是：

$$
C_{\text{implicit AI}}
\rightarrow
0
$$

再問：

$$
\text{Can canonical architecture regenerate the work state?}
$$

這正是 ABFR 對 AI-native engineering 特別有價值的地方。

---

# 42. Fresh Executor

本文定義 Fresh Executor：

$$
X_f
$$

滿足：

1. 沒有原始 executor 的 private reasoning；
2. 只能取得 protocol 允許的 canonical artifacts；
3. 使用相同或明示不同的工具權限；
4. 所有額外資訊請求都被記錄；
5. 成功不能依賴作者臨時補充。

Fresh Executor 可以是：

- 同一模型的新 session；
- 不同模型；
- human engineer；
- CI automation；
- local agent。

因此跨 AI replay 只是 Fresh Executor 的一種特別案例。

---

# 43. Human Intervention Count

如果 fresh executor 在重建時持續詢問原作者：

> 這裡下一步要做什麼？

則 canonical architecture 顯然仍不充分。

定義：

$$
H_I
=
\text{number of non-canonical human interventions}
$$

理想：

$$
H_I=0
$$

但實驗中可以量測：

$$
H_I
$$

而不是直接把第一次詢問視為失敗。

這可用來比較：

$$
\text{TDD-only handoff}
$$

與：

$$
\text{TDD + ABFR}
$$

---

# 44. Additional Information Requests

對跨 AI 實驗，任何 fresh Agent 的額外查詢都應分類：

### AIR-1 Canonical Navigation

資訊其實存在，只是 Agent 要求定位。

### AIR-2 Missing Documentation

必要資訊不存在 canonical artifact。

### AIR-3 Hidden Environment

必要狀態只存在原 workspace。

### AIR-4 Hidden Decision

必要設計只存在原作者記憶。

### AIR-5 Authority Request

資訊足夠，但執行需要額外權限。

這個分類可以直接作為後續 Spec B 的實驗輸出。

---

# 45. 可證偽假說

本文提出以下假說。

## H1 — Backtrace Finds Non-Test Structural Dependencies

存在：

$$
e
$$

使：

$$
C_B(e)=1
$$

但 architecture backtrace 能發現：

$$
h\in H_{\text{hidden}}
$$

且：

$$
h
$$

未被 TDD baseline 單獨揭露。

---

## H2 — Fresh Reconstruction Exposes Hidden Support

在 controlled benchmark 中注入 hidden dependency $h$：

$$
T(P,E_{\text{dirty}})=\text{PASS}
$$

但：

$$
T(P',E_f)=\text{FAIL}
$$

並能由 ABFR 正確分類為 freshness / reconstruction failure。

---

## H3 — MSRS Produces Smaller Explicit Support

與 full repository / full environment handoff 相比：

$$
|S_{\text{MSRS}}|
<
|S_{\text{handoff-all}}|
$$

且 replay correctness 不降低。

---

## H4 — Multiple Valid MSRS Exist

對具有合法 backend substitution 的專案：

$$
|\mathfrak M_Q|>1
$$

因此任何宣稱「唯一最小架構」的方法應被拒絕。

---

## H5 — Fresh Executor Reduces Author Dependence

完成 ABFR 後：

$$
H_I^{\text{ABFR}}
<
H_I^{\text{baseline handoff}}
$$

---

## H6 — Replay Equivalence Profile Prevents Post-Hoc Success

預先固定：

$$
\simeq_Q
$$

會比執行後自由解釋差異產生更高的 failure detection 與跨 Agent verdict consistency。

---

# 46. 與 Paper 04 的接口

Paper 03 到這裡仍存在一個重大問題：

如果 validator 永遠回 PASS，怎麼辦？

例如：

$$
\text{canonical replay}
\rightarrow
\text{PASS}
$$

但加入已知 hidden coupling 後：

$$
\text{mutated replay}
\rightarrow
\text{PASS}
$$

那麼這個 validator 沒有辨識能力。

因此 Paper 04 將定義：

$$
C_D
=
\text{Discriminative Closure}
$$

至少要求：

$$
\begin{aligned}
\text{canonical state} &\rightarrow \text{PASS}\\
\text{known violating mutation} &\rightarrow \text{FAIL}
\end{aligned}
$$

也就是 ABFR 的 Fresh Replay 必須能被證明：

$$
\boxed{
\text{it can go red}
}
$$

---

# 47. 與 Cross-AI Protocol 的接口

Paper 05 / Spec B 將使用本文定義，要求每個 AI 輸出：

```text
1. target set Q
2. baseline identity
3. backtrace frontier log
4. declared/observed/effective diff
5. unresolved claims
6. MSRS candidate
7. freshness contract evidence
8. replay equivalence profile
9. replay results
10. additional information requests
11. closure verdict
```

並固定：

$$
\text{Execution Mode}
=
\text{Inline Execution}
$$

不提供 sub-agent alternate path，以避免不同 orchestration architecture 成為第一輪實驗的混淆變項。

---

# 48. 不宣稱事項

本文明確不宣稱：

1. ABFR 等同於 formal verification。
2. Backtrace Closure 證明沒有未知 dependency。
3. MSRS 一定唯一。
4. MSRS 一定具有最小 cardinality。
5. Fresh reconstruction 一定要建立全新的 VM。
6. 所有 dependency 都必須重新下載。
7. Replay 一律要求 bitwise identical。
8. semantic equivalence 可以在執行後臨時決定。
9. static dependency graph 足以表示 effective architecture。
10. observed structure 自動等於 effective structure。
11. AI 可以無誤判地推導 effective architecture。
12. 一次 fresh replay 成功足以證明 release correctness。
13. architecture reconstruction、reproducible builds、deterministic replay 或 SLSA 是 ABFR 的子集。
14. ABFR 已被證明優於傳統 architecture review。
15. ABFR 的成本對所有規模專案都合理。

---

# 49. 方法論的最小形式

將本文收斂成一個最小定義。

一個 ABFR instance 為：

$$
\mathfrak A
=
(
P,
A_d,
Q,
\mathcal I,
\mathcal F,
\simeq_Q
)
$$

執行：

$$
\operatorname{Backtrace}(P,Q)
\rightarrow
B_Q
$$

由：

$$
B_Q
$$

導出至少一個：

$$
S\in\mathfrak M_Q
$$

再：

$$
P_S
=
\mathcal R(S,E_f)
$$

若：

$$
\mathcal F=1
$$

且：

$$
P_S
\equiv_{Q,\mathcal I}
P_{\text{ref}}
$$

則：

$$
C_S(Q)=1
$$

若再有：

$$
C_B(Q)=1
$$

則：

$$
G_{\text{ABFR}}(Q)=1
$$

Paper 04 將再要求：

$$
C_D(Q)=1
$$

---

# 50. 結論

Architecture Backtrace and Fresh Reconstruction 的核心不是：

> 把專案重新跑一次。

而是把一個已經工作的系統重新問一遍：

> 它究竟靠什麼成立？

Backtrace 從代表性 target 出發，沿 dependency、authority、state、evidence 與 runtime relation 回溯，直到所有必要支援抵達可接受 root 或被明確標記 unresolved。

接著不把 recovered architecture 留在文件裡，而是嘗試導出：

$$
\mathfrak M_Q
$$

也就是對 targets $Q$ 的 inclusion-minimal sufficient reconstruction sets。

然後在 Freshness Contract 下移除上一輪未宣告因果支援：

$$
\operatorname{Support}(P_S)
\cap
H_{\text{hidden}}
=
\varnothing
$$

最後用事先定義的：

$$
\simeq_Q
$$

與：

$$
\mathcal I_Q
$$

執行 replay。

因此 ABFR 的完整方向不是：

$$
\text{Code}
\rightarrow
\text{Documentation}
$$

而是：

$$
\boxed{
\text{Working System}
\rightarrow
\text{Architecture Backtrace}
\rightarrow
\text{Minimal Sufficient Structural Support}
\rightarrow
\text{Fresh Reconstruction}
\rightarrow
\text{Replay}
}
$$

如果 replay 失敗，失敗本身不是流程失敗。

它是 architecture knowledge 的新 evidence。

這正是 ABFR 與一般「文件補完」最大的差異：

$$
\boxed{
\text{Architecture description must survive reconstruction}
}
$$

Paper 03 因此把 Paper 01 的「Structural Reconstruction Closure」從概念命題收斂成可執行條件：

$$
\boxed{
C_S
=
C_{BT}
\land
C_{\text{MSRS}}
\land
C_F
\land
C_R
}
$$

而整個系列下一步，就是進一步要求這些檢查不只會成功，還必須能被已知破壞證明會失敗。

---

# 參考文獻

[1] Kazman, R., O'Brien, L., & Verhoef, C. (2003). *Architecture Reconstruction Guidelines, Third Edition*. Software Engineering Institute, CMU/SEI-2002-TR-034. DOI: 10.1184/R1/6572027.v1.

[2] O'Brien, L., Stoermer, C., & Verhoef, C. (2002). *Software Architecture Reconstruction: Practice Needs and Current Approaches*. Software Engineering Institute, CMU/SEI-2002-TR-024.

[3] Reproducible Builds Project. *Definitions — When is a build reproducible?* Reproducible-builds.org. Accessed 2026-08-28.

[4] Reproducible Builds Project. *Getting Started / Adding Build Variance*. Reproducible-builds.org. Accessed 2026-08-28.

[5] SLSA / OpenSSF. *SLSA Provenance Specification*. Current specification family referenced via slsa.dev. Accessed 2026-08-28.

[6] Neo.K / EveMissLab. (2026). *MSSP Field Manual 01 — 從這裡開始*. thisoneisneok.com, accessed 2026-08-28.

[7] Neo.K / EveMissLab. (2026). *MSSP Field Manual 02 — 架構與模式*. thisoneisneok.com, accessed 2026-08-28.

[8] Neo.K / EveMissLab. (2026). *MSSP Field Manual 06 — 迭代授權：SSD / Dynamic MSSP 工程規格與 MVP v0.1*. thisoneisneok.com, accessed 2026-08-28.

---

## Canonical status

本文為 **ABFR Series Paper 03 v0.1**。

目前狀態：

- Architecture assertion model: defined for v0.1.
- Declared / observed / effective relation: defined operationally.
- Backtrace frontier and closure: defined for v0.1.
- Minimal Sufficient Reconstruction Set: defined as inclusion-minimal and potentially non-unique.
- Freshness Contract: defined as causal freshness across seven dimensions.
- Replay Equivalence: defined as task-relative and predeclared.
- Structural Reconstruction Closure: defined.
- Mutation / attack discrimination: deferred to Paper 04.
- Cross-AI empirical validation: pending.
- Formal proof of completeness / optimality: not claimed.

後續版本若改變 MSRS、Freshness Contract 或 Replay Equivalence 的核心語義，必須以版本差異明示，不得將既有測試結果靜默重新解釋為新標準。
