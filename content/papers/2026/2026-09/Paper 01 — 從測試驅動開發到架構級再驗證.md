# Paper 01 — 從測試驅動開發到架構級再驗證

## From Test-Driven Development to Architecture-Level Revalidation

**系列：** TDD × MSSP Architecture Backtrace and Fresh Reconstruction  
**系列代號：** ABFR Series  
**文件版本：** v0.1  
**日期：** 2026-08-28  
**作者：** Neo.K / EveMissLab  

---

## 摘要

測試驅動開發（Test-Driven Development, TDD）提供了一種以可執行行為要求約束實作的工程循環。當測試先於或伴隨實作被建立時，開發者可以將需求轉換為可失敗、可重複執行的判準，並以 Red-Green-Refactor 的方式逐步建立行為閉包。然而，測試通過並不等同於架構描述完整，也不保證系統可以在移除原始開發上下文、工作區殘留狀態、未宣告依賴與作者隱性知識後，由其宣告的架構重新構成。

本文提出一個研究問題：軟體工程是否需要在 TDD 的行為驗證之後，再加入一個「架構級再驗證」階段，用以驗證已完成實作是否能由其顯式架構狀態重新生成。本文將此方法族暫稱為 **Architecture Backtrace and Fresh Reconstruction（ABFR，架構回溯與新鮮重建）**。ABFR 不取代 TDD、架構重建、架構導向測試、mutation testing 或 metamorphic testing；它試圖將這些相鄰思想之間尚未被固定成日常工程 gate 的一個缺口形式化：先由測試確認局部與行為契約，再由架構回溯比較 declared、observed 與 effective structure，接著在 fresh boundary 下依最小充分架構集合重新構成系統，最後以 replay 與 attack 驗證重建結果及驗證器本身的辨識能力。

本文首先定義「行為正確不推出架構可重建」的基本命題，再提出 Behavioral Closure、Structural Reconstruction Closure 與後續 Discriminative Closure 的分層關係。本文亦說明 MSSP（Mother-Set and Subset Paradigm）為何特別適合作為 ABFR 的第一個實作載體：MSSP 原先將大型系統的狀態邊界轉換為可觀察、可操作、可按需載入與可機械驗證的集合結構，原本主要用於降低人類認知複查成本與加速局部驗證；同一性質卻可被 AI 反向用於結構化全域遍歷、架構回溯與 fresh reconstruction。本文不主張 ABFR 已被證明為通用方法，而將其定位為一個待由跨專案、跨 AI 與對照實驗驗證的方法論假說。

**關鍵詞：** Test-Driven Development；Software Architecture；Architecture Reconstruction；Architecture-Based Testing；MSSP；ABFR；AI Coding Agent；Fresh Reconstruction；Replay；Structural Validation

---

# 1. 問題：測試全綠之後，架構真的成立了嗎？

現代軟體工程已經擁有大量測試技術。單元測試、整合測試、端對端測試、property-based testing、mutation testing 與 metamorphic testing 分別從不同角度約束程式行為。TDD 更進一步把測試放進開發循環，使「預期行為」在實作完成以前就能被寫成可執行判準。

然而，一個重要區分經常被工程實務壓縮成同一件事：

$$
\text{Behavioral Correctness}
\neq
\text{Architectural Reconstructibility}
$$

設一個已實作系統為 $P$，其測試集合為 $T$，目前工作環境為 $E$。若：

$$
T(P,E)=\text{PASS}
$$

我們最多能說，在測試覆蓋到的觀察條件與目前環境下， $P$ 滿足了 $T$ 所表達的要求。

但這並不能直接推出：

$$
A_d
\Rightarrow
P
$$

其中 $A_d$ 是系統所**宣告的架構狀態**。

原因是實際執行中的系統可能依賴：

- 未被架構文件宣告的模組；
- 工作區中偶然存在的檔案；
- 本機環境變數；
- 開發者手動完成但未記錄的初始化；
- 測試未觸及的 runtime path；
- 被其他模組間接提供的 hidden dependency；
- 前一輪 Agent 或開發者仍保留的上下文；
- 已被實作使用、但未進入 canonical specification 的規則；
- UI 或整合層暫時遮蔽的耦合。

因此可能同時成立：

$$
T(P,E)=\text{PASS}
$$

以及：

$$
\operatorname{Reconstruct}(A_d,E_f)=\text{FAIL}
$$

其中 $E_f$ 是刻意移除原始工作區殘留與隱性上下文的 fresh environment。

這正是本文欲處理的缺口。

---

# 2. TDD 已經解決了什麼，又沒有保證什麼？

TDD 的核心價值不應被低估。它把需求從敘述轉換成可執行失敗條件，並建立短週期回饋：

$$
\text{Requirement}
\rightarrow
\text{Test}
\rightarrow
\text{Red}
\rightarrow
\text{Implementation}
\rightarrow
\text{Green}
\rightarrow
\text{Refactor}
$$

近年的 agentic software engineering 亦顯示，當大型語言模型被置於受到約束的 test-driven workflow 中時，可以顯著提升 repository-scale repair 的可控性。Han 等人的 TDFlow 將 repository repair 重新表述為 test-resolution workflow，證明「測試作為 Agent 行為錨點」已經不是概念性主張，而是具有實際工程效力的方向。

但 TDD 的 test oracle 通常仍主要描述「什麼行為應該發生」，不必然描述「這個行為只能依哪些架構成分而成立」。

考慮兩個實作：

$$
P_1 = f(A,B)
$$

$$
P_2 = f(A,B,C_{\text{hidden}})
$$

若現有測試只觀察輸出，而且 $C_{\text{hidden}}$ 在開發環境始終存在，則可能有：

$$
T(P_1)=T(P_2)=\text{PASS}
$$

但它們的架構性質不同。

 $P_1$ 的宣告架構可能充分； $P_2$ 則可能具有未宣告依賴。

因此：

$$
\boxed{
\text{Test Pass}
\not\Rightarrow
\text{Architecture Complete}
}
$$

這不是 TDD 的缺陷，而是驗證層級不同。若要求 TDD 本身證明所有架構性質，反而會混淆測試責任。

本文主張應將兩者接成序列，而非互相取代。

---

# 3. 行為閉包與架構重建閉包

本文先提出兩種不同的閉包。

## 3.1 Behavioral Closure

令需求集合為 $R$，測試集合為 $T$，實作為 $P$。

若對目前聲稱需要滿足的行為要求而言：

$$
\forall r_i \in R,
\quad
\exists t_j \in T
$$

使得 $t_j$ 能有效區分符合與不符合 $r_i$ 的實作，且當前實作通過相關測試，則稱其在指定範圍內達成 Behavioral Closure：

$$
C_B(P,T,R)=1
$$

這不是宣稱程式絕對正確，而是表示目前行為契約形成了可執行閉環。

---

## 3.2 Structural Reconstruction Closure

令：

- $A_d$：declared architecture；
- $A_o$：observed architecture；
- $A_e$：effective architecture；
- $E_f$：fresh environment；
- $P'$：依 declared architecture 在 $E_f$ 中重新構成的系統。

ABFR 要求的不只是從原始碼抽取「as-built architecture」，而是先從已完成系統回溯實際結構，再以顯式架構作為正向重建輸入。

反向回溯：

$$
P
\rightarrow
A_e
\rightarrow
A_o
\rightarrow
A_d
$$

正向重建：

$$
A_d
\rightarrow
\operatorname{Reconstruct}(A_d,E_f)
\rightarrow
P'
$$

若 $P'$ 能在事先定義的 equivalence relation $\simeq$ 下，重現目標系統所要求的行為與架構約束，則稱達成 Structural Reconstruction Closure：

$$
C_S(A_d,P,E_f)=1
$$

其最小要求為：

$$
P' \simeq P_{\text{expected}}
$$

以及所有被宣告為必要的 architecture invariants 在 fresh reconstruction 中成立。

此處 $\simeq$ 不要求 byte-for-byte identical。不同建置時間、暫存 ID、非語義性排序或可替代 backend 都可能不同。等價關係必須由專案預先定義，例如：

- 行為等價；
- interface contract 等價；
- dependency boundary 等價；
- authority semantics 等價；
- state transition 等價；
- audit evidence 等價。

---

# 4. Architecture Backtrace and Fresh Reconstruction

本文將方法核心暫定義為 ABFR。

$$
\boxed{
\text{ABFR}
=
\text{Architecture Backtrace}
+
\text{Fresh Reconstruction}
+
\text{Replay Validation}
}
$$

其目標不是產生更多文件，而是讓架構宣稱具有可執行後果。

---

## 4.1 Architecture Backtrace

Architecture Backtrace 從已完成或暫時穩定的實作向後追問：

1. 這個輸出實際依賴哪些 entity？
2. 哪些 dependency 是 declared？
3. 哪些 dependency 只在 runtime observed？
4. 哪些 dependency 在實際閉環中是 effective？
5. 哪些 authority 決定了可讀、可寫、可修改與可部署範圍？
6. 哪些狀態是必要輸入？
7. 哪些狀態只是環境殘留？
8. 哪些測試依賴未宣告 fixture？
9. 哪些模組聲稱可獨立，實際卻依賴 sibling module？
10. 哪些架構決策只存在於原作者或前一個 Agent 的上下文？

可形式化為：

$$
B(P)=
\{
A_d,
A_o,
A_e,
H,
U
\}
$$

其中：

- $H$ 為 hidden structural assumptions；
- $U$ 為 unresolved structural claims。

ABFR 不要求一開始就完全消滅 $H$ 與 $U$，但要求它們不能繼續偽裝成已驗證架構。

---

## 4.2 Fresh Reconstruction

Fresh Reconstruction 不是「重新執行同一個 workspace」。

Fresh 的最低語義是：

$$
E_f
\cap
E_{\text{incidental}}
=
\varnothing
$$

其中 $E_{\text{incidental}}$ 包含不應成為 canonical architecture 一部分的偶然狀態。

在 AI 工程情境中還必須加入：

$$
C_{\text{hidden}}=0
$$

即新的執行者不應依賴：

- 前一輪聊天記憶；
- 原作者額外口頭補充；
- 未寫入 canonical artifact 的操作順序；
- 未聲明的本機檔案；
- 既有 Agent 在 private scratch state 中保留的判斷。

Fresh Reconstruction 的輸入應盡可能收斂為：

$$
I_f =
\{
A_d,
S_c,
T,
D,
K
\}
$$

其中：

- $A_d$：declared architecture；
- $S_c$：canonical source；
- $T$：測試；
- $D$：明示資料與依賴；
- $K$：允許使用的工具與權限邊界。

---

## 4.3 Replay Validation

重建完成後，不以「可以啟動」作為完成條件，而應重新執行代表性行為與架構 probes。

$$
P'
\rightarrow
\operatorname{Replay}(Q)
\rightarrow
O'
$$

其中 $Q$ 為代表性任務、測試、事件序列或狀態轉移。

然後比較：

$$
O' \simeq O_{\text{expected}}
$$

並再次觀察：

$$
A'_o
\quad\text{與}\quad
A'_e
$$

若 fresh replay 後再次產生新的 hidden dependency，則原本 declared architecture 仍不充分。

---

# 5. 為什麼需要「先 TDD，再 ABFR」

本文提出的順序不是任意的：

$$
\boxed{
\text{TDD}
\rightarrow
\text{ABFR}
\rightarrow
\text{Runtime/UI Projection}
}
$$

而非：

$$
\text{TDD}
\rightarrow
\text{UI}
\rightarrow
\text{Architecture Review}
$$

原因在於 UI 與高階 runtime 往往具有遮蔽效應。當多個 service、adapter、cache、mock、browser state 或 operator action 同時存在時，系統可以「看起來工作」，卻無法說明其最小充分結構。

因此 ABFR 被放置在 Direct Runtime 或 UI 擴張之前，具有工程 gate 的意義：

$$
G_{\text{architecture}}
=
C_B
\land
C_S
$$

只有在：

$$
G_{\text{architecture}}=1
$$

時，才進入下一個 projection layer。

這並不表示所有 UI 都必須等待整個產品架構永久定案，而是表示：對一個被宣稱已完成基本設計閉環的 milestone，不應在架構可重建性尚未驗證前，用更多 projection complexity 掩蓋底層狀態。

---

# 6. MSSP 為何成為第一個自然載體

MSSP（Mother-Set and Subset Paradigm）原先處理的是大型專案超出人類工作記憶後的結構問題。其核心不是「把程式切碎」，而是讓狀態邊界成為可看見、可操作、可按需載入與可機械檢查的結構。

在 MSSP 的早期實作中，FMS、SCL、SMS、TMS 與 DMS 被定義為角色，而非必須存在的固定資料夾。這個差異很重要：其目的不是建立命名慣例，而是把核心、可替換能力、權限、可觀察結果與系統描述分離，從而讓局部載入、孤島測試與機械結構檢查成為可能。

後續 Dynamic MSSP / SSD 又進一步將具體 taxonomy 降為可替換層，保留更底層的治理語義，例如 Entity、Relation、Role、Authority、Evidence、State 與 GovernanceEvent，並明確區分 declared、observed 與 effective layer。

這使 MSSP 特別適合作為 ABFR 的第一個 implementation profile。

原本的人類導向使用方式是：

$$
\text{Global Complexity}
\rightarrow
\text{Relevant Subset}
\rightarrow
\text{Local Inspection}
$$

其主要收益是：

$$
\operatorname{Cost}_{\text{human review}}
\downarrow
$$

但 AI 可以利用同一結構反向得到：

$$
S_1,S_2,\ldots,S_n
\rightarrow
\text{Traverse}
\rightarrow
\text{Record}
\rightarrow
\text{Reconcile}
$$

也就是：

$$
\boxed{
\text{Human Cognitive Reduction}
\rightarrow
\text{AI Structured Global Attention}
}
$$

這不是因為 AI 必須一次將整個專案永久保留在注意力中，而是因為可枚舉的 structural subsets 提供了導航圖，使 AI 可以依序載入、比較、記錄與回溯。

因此，MSSP 中原本用來「少看一點」的設計，可以被 AI 轉換為「有秩序地看完更多」。

---

# 7. 與既有研究的關係

ABFR 必須與既有工作清楚區分，否則容易把已存在的方法重新命名。

## 7.1 與 TDD 的關係

TDD 為行為契約提供快速、可執行的回饋。近期 agentic TDD 工作顯示，精確測試與受約束 workflow 可以有效指導大型語言模型進行 repository-scale repair。

ABFR 不替代 TDD，而是假設 TDD 已完成第一層閉包，再追問：

$$
\text{Why did the tests pass structurally?}
$$

以及：

$$
\text{Can the claimed architecture reproduce that success from a fresh boundary?}
$$

---

## 7.2 與 Architecture Reconstruction 的關係

Architecture Reconstruction 長期以來已用於從既有系統取得 as-built architecture，並可比較 as-built 與 as-designed architecture。

ABFR 直接承認並繼承這個問題域，但增加兩個工程要求：

第一，backtrace 不以產生架構表示為終點。

第二，回溯得到的結果必須重新進入正向 construction：

$$
\text{Recover}
\rightarrow
\text{Reconcile}
\rightarrow
\text{Reconstruct}
\rightarrow
\text{Replay}
$$

因此，ABFR 的研究焦點不是「我們能否理解 legacy architecture」，而是「架構描述是否足以成為 fresh reconstruction 的可執行輸入」。

---

## 7.3 與 Architecture-Based Testing 的關係

Architecture-Based Testing（ABT）主動使用架構資訊來建立 test model、導出 test case、進行 test selection 或支援測試決策。2026 年的系統性文獻回顧指出，ABT 下一步的重要方向包括可重用且與架構一致的測試策略、architecture-driven coverage criteria，以及可追蹤與可操作的 derivation procedure。

ABFR 與這個方向高度相鄰。

差別在於 ABFR 的主要判準不是「由架構導出更多測試」，而是：

$$
\text{Declared Architecture}
\overset{?}{\Longrightarrow}
\text{Reconstructible System}
$$

因此它可以被視為一種 architecture-level adequacy question，而不是新的單一 test-generation technique。

---

## 7.4 與 Metamorphic Testing 的關係

Metamorphic Testing（MT）透過多次執行之間應滿足的關係建立 oracle，特別適合難以為單次輸出建立完整 ground truth 的系統。2026 年已有研究使用 LLM 協助推導 metamorphic relations 與 follow-up test cases，也已有工作以 logic-grounded metamorphic relations 評估 LLM reasoning reliability。

ABFR 可以使用 MT，但不等同於 MT。

例如 fresh reconstruction 前後可以定義 metamorphic relation：

$$
R(P,E)
\simeq
R(P',E_f)
$$

但 ABFR 還要求回溯 dependency、authority、state 與 architecture claims。因此 MT 可以成為 ABFR 的 replay oracle 之一，而不是 ABFR 的完整定義。

---

# 8. 方法論假說

本文提出四個待驗證假說。

## H1：TDD 與 ABFR 捕捉不同錯誤類型

$$
\exists e:
\quad
C_B(e)=1
\land
C_S(e)=0
$$

亦即存在測試全綠、但 fresh reconstruction 失敗的工程狀態。

---

## H2：結構化架構表示能降低 AI 回溯成本

若架構被表示為可枚舉、可選取的 entities、relations、roles、evidence 與 state boundaries，則 AI 執行 architecture-wide review 時，不必依賴單次全量上下文載入。

預期：

$$
\operatorname{Cost}_{\text{structured traversal}}
<
\operatorname{Cost}_{\text{unstructured global reread}}
$$

此處 cost 可以分解為 token、wall-clock、tool calls、遺漏率與重複讀取率。

---

## H3：Fresh Reconstruction 能揭露 context-dependent correctness

若某專案的成功依賴前一個 Agent、作者記憶或原工作區殘留，則：

$$
T(P,E)=\text{PASS}
$$

但：

$$
T(P',E_f)=\text{FAIL}
$$

Fresh Reconstruction 應提高此類 hidden-context defect 的可見性。

---

## H4：ABFR 可以脫離 MSSP 的具體 taxonomy

若 ABFR 的本體需求是：

$$
\{
\text{explicit architecture},
\text{traceable relations},
\text{fresh reconstruction boundary},
\text{replay oracle}
\}
$$

那麼 MSSP 應只是第一個強實作 profile，而非唯一可行表示。

因此需要以 non-MSSP project 作為對照，驗證：

$$
\text{ABFR-MSSP}
\subseteq
\text{ABFR}
$$

是否成立。

---

# 9. 最小工程流程

Paper 01 不固定最終標準，但先提出一個可測試的最小流程：

$$
\begin{aligned}
1.&\ \text{Freeze Baseline}\\
2.&\ \text{Declare Architectural Hypothesis}\\
3.&\ \text{Write Precise TDD Plan}\\
4.&\ \text{Red}\\
5.&\ \text{Implement}\\
6.&\ \text{Green}\\
7.&\ \text{Refactor}\\
8.&\ \text{Architecture Backtrace}\\
9.&\ \text{Reconcile Declared/Observed/Effective}\\
10.&\ \text{Derive Minimal Reconstruction Set}\\
11.&\ \text{Fresh Reconstruction}\\
12.&\ \text{Replay Representative Tasks}\\
13.&\ \text{Record Structural Divergence}\\
14.&\ \text{Decide Architecture Closure}\\
15.&\ \text{Proceed to Runtime/UI Projection}
\end{aligned}
$$

後續 Paper 04 將再加入 mutation / attack，使完整 gate 從雙閉包提升為三閉包：

$$
C_{\text{engineering}}
=
C_B
\land
C_S
\land
C_D
$$

其中 $C_D$ 為 Discriminative Closure，用以避免「驗證器永遠綠燈」被誤認為有效證據。

---

# 10. Fresh 的操作性定義

若 Fresh Reconstruction 要成為通用方法，fresh 必須是可操作定義，而不是語氣詞。

本文提出 v0.1 最低條件：

### F1. Fresh Context

新的 AI 執行者不得取得未納入 canonical artifact 的前序對話推理與操作記憶。

### F2. Fresh Workspace

不得依賴未宣告的 generated file、cache、local patch、temporary database 或 previous-run state。

### F3. Explicit Dependencies

重建所需 dependency 必須可以由 canonical source、lockfile、manifest、container definition 或其他正式機制取得。

### F4. Explicit Authority

若重建需要網路、憑證、部署、資料庫寫入或高風險操作，其 authority 必須明示；「在舊環境剛好有權限」不能算架構成立。

### F5. Replayable Evidence

重建結果至少要產生一組可重新檢查的 test result、probe、trace、snapshot、hash、event log 或同等證據。

因此 Fresh 並不要求所有 machine state 都是物理上首次建立，而是要求：

$$
\boxed{
\text{No undeclared causal support from the previous development state}
}
$$

這是比「換一個資料夾再跑一次」更嚴格的定義。

---

# 11. 失敗分類

ABFR 的價值不應只以 PASS/FAIL 表示。Fresh reconstruction 的失敗至少可分成：

### R1. Missing Declared Dependency

實作需要某依賴，但 declared architecture 沒有記錄。

### R2. Hidden Runtime Coupling

static dependency 看不出問題，但 runtime 依賴其他 service、state 或 side effect。

### R3. Context Leakage

只有原作者或前一個 Agent 知道必要操作。

### R4. Authority Leakage

系統依賴既有 credentials、permissions 或人工特權才能完成。

### R5. State Leakage

結果依賴上一輪 cache、database、filesystem 或 mutable external state。

### R6. Test Fixture Leakage

測試本身依賴開發環境中的未宣告 fixture。

### R7. False Modularity

某模組宣稱可獨立載入，但 fresh subset 無法完成其代表任務。

### R8. Projection Masking

UI 或 integration layer 使底層錯誤暫時不可見。

### R9. Declared/Observed Drift

架構描述仍能重建部分功能，但 observed structure 已經與 declared structure 分離。

### R10. Validator Blindness

replay 或 probe 通過，但加入已知 violating mutation 後仍維持綠燈。此類將在後續 Discriminative Closure 論文中正式處理。

這些分類將成為後續跨 AI 實驗的 error taxonomy 初稿。

---

# 12. 對 AI 軟體工程的意義

人類與 AI 對 MSSP 類結構的收益並不完全相同。

對人類而言，原始收益可寫成：

$$
\text{Large System}
\rightarrow
\text{Relevant Subset}
\rightarrow
\text{Reduced Review Burden}
$$

對 AI 而言，則可能形成另一種使用模式：

$$
\text{Subset}_1
\rightarrow
\text{Subset}_2
\rightarrow
\cdots
\rightarrow
\text{Subset}_n
\rightarrow
\text{Global Reconciliation}
$$

人類通常因 attention switching、工作記憶與複查成本，不會在每個 milestone 都執行完整架構級回溯。

AI 的優勢未必是「一次記住所有東西」，而可能是：

$$
\boxed{
\text{Cheap Repeated Structured Traversal}
}
$$

如果這個假說成立，過去只在重大事故、重構或 architecture review 才執行的高成本活動，可能被降為日常工程 gate。

這正是 ABFR 最值得驗證的地方。

其潛在轉換不是：

$$
\text{AI replaces architect}
$$

而是：

$$
\boxed{
\text{Rare Architecture Audit}
\rightarrow
\text{Routine Architecture Revalidation}
}
$$

---

# 13. 邊界與不宣稱事項

為避免概念膨脹，本文明確不宣稱：

1. ABFR 能證明軟體不存在缺陷。
2. Fresh replay 成功等於正式形式驗證。
3. TDD 可以被 ABFR 取代。
4. MSSP 是執行 ABFR 的唯一架構方法。
5. AI 比所有人類架構師更適合架構推理。
6. 所有專案都值得支付 architecture replay 成本。
7. 一次跨 AI 成功即可證明通用性。
8. Architecture Reconstruction、ABT、MT 或 mutation testing 是 ABFR 的子集。
9. declared、observed 與 effective structure 必然能被完整觀察。
10. 本文已經提供足夠實證支持 ABFR 的普遍效益。

Paper 01 的角色只是提出一個可以被後續實驗證偽的方法論假說：

$$
\boxed{
\text{Behavioral validation alone may be insufficient for AI-scale software construction;}
}
$$

$$
\boxed{
\text{explicit architectural backtrace and fresh reconstruction may provide a second validation closure.}
}
$$

---

# 14. 後續研究

本系列接下來依序處理：

**Paper 02 — MSSP as an AI Structural Attention Substrate**  
研究人類認知減壓結構如何被 AI 重新利用為 structured global attention 與 architecture traversal substrate。

**Paper 03 — Architecture Backtrace and Fresh Reconstruction**  
建立 ABFR 的正式資料模型、等價關係、最小充分重建集合與 failure semantics。

**Paper 04 — Behavioral, Structural, and Discriminative Closure**  
加入 mutation / attack，定義能被證明會失敗的 validator 與三閉包工程 gate。

**Paper 05 — Cross-Agent Reproducibility of Architecture Reasoning**  
定義跨模型、跨 session、跨專案實驗。

**Spec A — ABFR Methodology v0.1**  
提供可直接執行的工程程序。

**Spec B — Cross-AI ABFR Validation Protocol v0.1**  
提供給其他 AI 的盲測協議，固定 canonical inputs、freshness、Inline Execution 與結果格式。

若實驗資料足夠，再撰寫：

**Paper 06 — A Multi-Agent Empirical Evaluation of Architecture Backtrace and Fresh Reconstruction**

---

# 15. 結論

TDD 解決了一個極其重要的問題：如何讓行為要求在程式完成以前就具有可執行的失敗條件。

但 AI 輔助軟體工程的規模擴大後，另一個問題逐漸凸顯：

> 一個通過測試的系統，是否真的可以由它宣稱的架構重新生成？

本文將兩個問題分開。

第一個問題由 Behavioral Closure 處理：

$$
C_B
$$

第二個問題由 Structural Reconstruction Closure 處理：

$$
C_S
$$

並提出：

$$
\boxed{
G_{\text{architecture}}
=
C_B
\land
C_S
}
$$

作為進入後續 runtime/UI projection 前的一種候選 architecture gate。

ABFR 的核心不是「重跑測試」，而是將已完成實作進行架構回溯，顯式比較 declared、observed 與 effective structure，再從 fresh boundary 只依賴 canonical architecture 與明示資源重新構成系統，最後 replay 代表行為。

MSSP 為這個方法提供了一個自然起點。它原先為降低人類在大型系統中的認知複查成本而建立可觀察、可操作、可按需載入的狀態邊界；AI 卻可能利用同一結構執行人類成本過高而不會頻繁進行的全域結構遍歷與回溯。

如果後續實驗能證明這個組合在不同 AI、不同 repository、不同架構表示法下仍持續揭露 TDD-only 無法發現的架構缺陷，那麼它的意義就不只是 MSSP 的一個新用法。

它可能指向一種新的工程常態：

$$
\boxed{
\text{Test-Driven Implementation}
\rightarrow
\text{Architecture-Driven Revalidation}
}
$$

不是用 AI 取代測試，也不是用 AI 取代架構設計，而是利用 AI 將過去成本過高、很少被完整重做的架構複查，轉換成可重複執行的工程閉環。

---

# 參考文獻

[1] Han, K., Maddikayala, S., Knappe, T., Patel, O., Liao, A., & Barati Farimani, A. (2026). *TDFlow: Agentic Workflows for Test Driven Development*. Proceedings of EACL 2026, 1511–1527. DOI: 10.18653/v1/2026.eacl-long.70.

[2] Lee, J., & Kang, S. (2026). *Architecture-based software testing: Systematic literature review*. Information and Software Technology, 198, 108206 (online / assigned to the October 2026 issue). DOI: 10.1016/j.infsof.2026.108206.

[3] Kazman, R., O'Brien, L., & Verhoef, C. (2003). *Architecture Reconstruction Guidelines, Third Edition*. Carnegie Mellon Software Engineering Institute, CMU/SEI-2002-TR-034. DOI: 10.1184/R1/6572027.v1.

[4] Cañizares, P. C., Gómez-Abajo, P., Guerra, E., & de Lara, J. (2026). *Towards metamorphic testing with LLM-based workflows: Metamorphic relation inference and follow-up test case generation*. Information and Software Technology, 196, 108150. DOI: 10.1016/j.infsof.2026.108150.

[5] Zhou, Z., Li, M., Fang, X., Zhou, X., Lin, W., & Zheng, Z. (2026). *LGMT: Logic-Grounded Metamorphic Testing for evaluating the reasoning reliability of LLMs*. Knowledge-Based Systems, 348, 116324. DOI: 10.1016/j.knosys.2026.116324.

[6] Neo.K / EveMissLab. (2026). *MSSP Field Manual: 從這裡開始*. MSSP 1.x public field manual, thisoneisneok.com, accessed 2026-08-28.

[7] Neo.K / EveMissLab. (2026). *SSD / Dynamic MSSP 工程規格與 MVP v0.1 / 迭代授權*. MSSP Field Manual 06, thisoneisneok.com, accessed 2026-08-28.

---

## Canonical status

本文為 **ABFR Series Paper 01 v0.1**。

目前狀態：

- Conceptual foundation: complete for v0.1.
- General-method claim: not yet established.
- Cross-AI validation: pending.
- Non-MSSP validation: pending.
- Empirical comparison against TDD-only: pending.

任何後續版本若改變 ABFR 的核心定義，必須明示版本差異，不以靜默改寫方式取代本版命題。
