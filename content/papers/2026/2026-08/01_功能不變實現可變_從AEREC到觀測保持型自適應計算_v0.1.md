# 功能不變，實現可變
## 從 AEREC 到觀測保持型自適應計算

**English Title:** *Stable Function, Mutable Implementation: From AEREC to Observer-Preserving Adaptive Computation*  
**系列：**《觀測保持型自適應計算》（Observer-Preserving Adaptive Computation, OPAC）第 1 篇  
**系列編號：** EML-OPAC-2026-01  
**作者：** Neo.K  
**協作整理：** Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-10  
**文件定位：** AEREC × CDI 橋接母論文／Runtime 身分與實現分離／觀測保持型在線演化  
**證據成熟度：** E0–E1。AEREC 已完成跨代身分、觀測等價、候選驗證與回滾框架；JIT、tiered compilation、runtime profiling 等公開技術證明「執行期可改變實現」本身已有成熟前例。本文新增的是將功能契約、觀測等價與 CDI Runtime 治理統一成更廣義的在線實現演化框架，尚需工程驗證。

---

## 摘要

如果一個程式的原始碼、演算法、資料結構、中介表示、編譯方式、Runtime 策略、硬體映射與平行化拓撲都可以改變，那麼「同一個程式」究竟由什麼保持？

《AI 自適應封裝與遞歸演化計算論》（AEREC）已提出一個明確答案：應用身分不等於某一份 source code、EXE 或單一實現，而由權威身分根、功能契約、合法觀測者、語義版本、治理規則與可追溯歷史共同構成。AEREC 允許每一代改變演算法、資料結構、IR、編譯、執行時、封裝與硬體映射，只要求新版本在指定契約與觀測條件下保持等價。

近期 CDI / AIVS 研究則從另一個方向到達相近結構：AI 不必親自完成所有計算，而可以成為計算域的語義—因果控制面；Runtime 可以依當前 world state、dependency、hardware state、profiling evidence 與 resource policy 改變 execution plan，並透過 Candidate → Verify → Commit 保持正式狀態安全。

本文指出，這兩條研究線之間存在一個更一般的共同形式：

$$
\boxed{
\text{Stable Observable Identity}
+
\text{Mutable Implementation Form}.
}
$$

AEREC 主要處理：

$$
\boxed{
\text{跨代實現演化}
}
$$

而 CDI 開始處理：

$$
\boxed{
\text{執行期實現演化}.
}
$$

本文因此提出 **觀測保持型自適應計算**（Observer-Preserving Adaptive Computation, OPAC）作為橋接框架。

令應用身分為：

$$
\mathcal I_{\mathrm{app}}
=
(
 r^\ast,
 \mathcal C,
 \Omega,
 v_s,
 \mathcal G,
 H
),
$$

令當前具體執行實現為：

$$
\pi_t.
$$

OPAC 不要求：

$$
\pi_{t+1}=\pi_t.
$$

它要求的是：

$$
\boxed{
\pi_{t+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
\pi_t,
}
$$

並為避免多代／多時段漂移，同時維持：

$$
\boxed{
\pi_{t+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
\pi_0.
}
$$

因此，Runtime 可以在合法等價類中改變演算法、串行／並行拓撲、CPU/GPU/NPU 映射、tick frequency、simulation resolution、cache/retrieval、precision、speculation、data representation、verification depth 與 AI attention allocation，只要所有契約承認的觀測者仍得到可接受的功能、狀態、行為、副作用、安全、時間、錯誤與恢復語義。

本文特別反對一個過度簡化：

$$
\boxed{
\text{使用者看不到}
\not\Rightarrow
\text{內部可以任意改}.
}
$$

合法觀測者不只有使用者，也包括 API、state observer、security、operator、auditor 與 environment。真正的自由度存在於：

$$
\boxed{
\text{契約未區分、且所有必要觀測保持等價的實現空間}.
}
$$

本文最後建立 OPAC 的母形式、在線適應算子、執行等價類、漂移防護與 AEREC/CDI 對接關係，為下一篇《程式作為動態渲染：執行等價類、觀測纖維與 Runtime 重實現》建立形式地基。

---

## 關鍵詞

觀測保持型自適應計算、OPAC、AEREC、CDI、程式身分、功能契約、觀測等價、Runtime adaptation、dynamic implementation、JIT、adaptive compilation、Candidate/Commit、execution rendering

---

# 0. 系列定位

本系列固定四篇：

1. **《功能不變，實現可變：從 AEREC 到觀測保持型自適應計算》**
2. **《程式作為動態渲染：執行等價類、觀測纖維與 Runtime 重實現》**
3. **《觀察者看不到的自由度：從功能契約到自適應世界狀態機》**
4. **《從跨代演化到在線遞歸：AEREC × CDI × ACR × AIVS 的統一 Runtime》**

第 1 篇建立母命題；第 2 篇建立等價類／觀測纖維與「動態渲染」形式；第 3 篇進入遊戲、沙盒與世界狀態機；第 4 篇統一 Runtime 後封頂。

---

# 1. 問題不是「程式能不能改」

現代計算系統早已證明 Runtime 不是完全靜態。JIT compiler 可以 runtime compile、lazy compile、profile hot code、tiered optimize、invalidate assumptions、deoptimize、recompile。

因此本文不是主張：

> 程式執行時可以產生不同 machine code。

這不是新的。

真正的問題是：

> **如果 AI 可以跨越多個抽象層改變實現，究竟什麼仍使它保持為同一個應用？**

---

# 2. 程式身分不能再綁定單一實現物

若只改：

$$
MachineCode_A\rightarrow MachineCode_B,
$$

而高階語義顯然一致，問題相對簡單。

但如果 AI 可以改：

$$
\boxed{
Algorithm
+
DataStructure
+
IR
+
Runtime
+
Parallelism
+
HardwareMapping,
}
$$

「同一程式」不能再依 source hash、binary hash、file name 或 process image 定義。

---

# 3. AEREC 已給出身分核心

AEREC 將應用身分寫成：

$$
\boxed{
\mathcal I_{\mathrm{app}}
=
(
 r^\ast,
 \mathcal C,
 \Omega,
 v_s,
 \mathcal G,
 H
).
}
$$

其中：

- $r^\ast$：權威身分根；
- $\mathcal C$：功能／觀測契約；
- $\Omega$：合法觀測者集合；
- $v_s$：語義版本；
- $\mathcal G$：治理與遷移規則；
- $H$：可追溯歷史。

這是 OPAC 的身分地基。

---

# 4. 功能契約不是只有輸入／輸出

AEREC 的功能契約可表示為：

$$
\boxed{
\mathcal C
=
(
\mathcal I,
\mathcal O,
\mathcal S,
\mathcal E,
\mathcal P,
\mathcal Q,
\mathcal R,
\mathcal T,
\mathcal A,
\mathcal X
).
}
$$

分別涵蓋輸入、輸出、狀態、副作用、權限、品質、錯誤、時間、可用性與外部依賴。

所以：

$$
\boxed{
SameOutput
}
$$

只是：

$$
\boxed{
SameApplication
}
$$

的一小部分。

---

# 5. 觀測者集合

AEREC 定義：

$$
\Omega
=
\{
\omega_{\mathrm{user}},
\omega_{\mathrm{api}},
\omega_{\mathrm{state}},
\omega_{\mathrm{security}},
\omega_{\mathrm{operator}},
\omega_{\mathrm{auditor}},
\omega_{\mathrm{environment}}
\}.
$$

不同觀測者看到不同投影。

對每個 $\omega\in\Omega$：

$$
\operatorname{Obs}_{\omega}
:
\operatorname{Run}(P,x,e)
\rightarrow
Y_\omega.
$$

完整觀測：

$$
\boxed{
\operatorname{Obs}_{\Omega}
=
\prod_{\omega\in\Omega}
\operatorname{Obs}_{\omega}.
}
$$

---

# 6. 「使用者看不到」為什麼太弱？

假設新 implementation：

- 使用者輸出完全相同；
- 但偷寫額外檔案；
- 增加網路傳輸；
- 改變 RNG；
- 破壞 rollback；
- latency 增加十倍。

則：

$$
Obs_{\mathrm{user}}(P_a)
=
Obs_{\mathrm{user}}(P_b)
$$

不表示：

$$
P_a
\equiv_{\mathcal C,\Omega}
P_b.
$$

因此真正的自由度不是「玩家現在沒看到」，而是「契約承認的全部必要觀測都沒有把兩個實現區分開」。

---

# 7. 實現自由度

本文定義：

$$
\boxed{
ImplementationFreedom
=
\text{契約未區分的內部差異}.
}
$$

更精確地：若

$$
P_a
\equiv_{\mathcal C,\Omega,D,\epsilon}
P_b,
$$

則 $P_a$ 與 $P_b$ 的內部差異在該契約語境下可被視為合法實現自由。

---

# 8. 等價是相對的

$$
\boxed{
P_a
\equiv_{\mathcal C,\Omega,D,\epsilon}
P_b
}
$$

依賴：

- $\mathcal C$：契約；
- $\Omega$：觀測者；
- $D$：適用域；
- $\epsilon$：容許誤差。

不是宇宙絕對不可區分。

---

# 9. 適用域 $D$

如果新實現只在：

$$
x\in D_1
$$

等價，而原應用要求：

$$
x\in D_0,
\quad D_1\subset D_0,
$$

就不能偷偷把 $D_0$ 縮成 $D_1$，再宣稱「功能不變」。

---

# 10. 誤差 $\epsilon$

純整數函數可能要求：

$$
\epsilon=0.
$$

浮點 simulation 可能允許：

$$
\epsilon>0.
$$

但 $\epsilon$ 必須由契約決定，而不能由 optimizer 為了 speedup 自行放寬。

---

# 11. AEREC 的跨代形式

AEREC 原本要求：

$$
\boxed{
P_{n+1}
\equiv_{\mathcal C}
P_n.
}
$$

更完整地可寫：

$$
P_{n+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
P_n.
$$

---

# 12. 防止逐代漂移

只比較相鄰代：

$$
P_{n+1}\equiv P_n
$$

仍可能累積 drift。

因此還要維持：

$$
\boxed{
P_{n+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
P_0.
}
$$

並要求歷史 invariant：

$$
\operatorname{Inv}_H(P_{n+1})=1.
$$

---

# 13. AEREC 的真正對象

所以 AEREC 的對象不是：

$$
\boxed{OneBinary.}
$$

而是：

$$
\boxed{
OneApplicationIdentity
+
ManyLegalImplementations.
}
$$

---

# 14. CDI 帶來的新問題

CDI 不只問：

> 下一版怎麼改？

它開始問：

> **這一刻應該用哪個 execution form？**

令：

$$
\pi_t
$$

為時刻 $t$ 的具體執行實現。

---

# 15. $\pi_t$ 可以是什麼？

例如：

$$
\boxed{
\pi_t
=
(
Algorithm_t,
Topology_t,
Backend_t,
Resolution_t,
Frequency_t,
Precision_t,
Cache_t,
Verification_t
).
}
$$

---

# 16. 下一刻不必相同

$$
\boxed{
\pi_{t+1}
\neq
\pi_t.
}
$$

但應用身分仍可能保持：

$$
\boxed{
\mathcal I_{\mathrm{app}}(t+1)
=
\mathcal I_{\mathrm{app}}(t).
}
$$

---

# 17. OPAC 母命題

> **只要一個新的執行實現在指定功能契約、合法觀測者、適用域與誤差容忍下保持觀測等價，那麼實現形態可以在執行期間持續改變，而不必將每一次改變視為新的應用身分。**

形式：

$$
\boxed{
\pi_{t+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
\pi_t.
}
$$

---

# 18. Root Equivalence

同時要求：

$$
\boxed{
\pi_{t+1}
\equiv_{\mathcal C,\Omega,D,\epsilon}
\pi_0.
}
$$

避免 runtime adaptation 逐步漂移。

---

# 19. Runtime Adaptation Operator

定義：

$$
\boxed{
\Phi:
(
\pi_t,
S_t,
H_t,
E_t,
G_t
)
\rightarrow
\pi_{t+1}^{cand}.
}
$$

其中：

- $\pi_t$：當前實現；
- $S_t$：應用／世界狀態；
- $H_t$：硬體／backend 狀態；
- $E_t$：證據與 profiling；
- $G_t$：目標／policy；
- $\pi_{t+1}^{cand}$：候選新實現。

---

# 20. 為什麼是 Candidate？

因為：

$$
\boxed{
AIProposal
\neq
ValidImplementation.
}
$$

所以 $\pi_{t+1}^{cand}$ 不能立即取代 $\pi_t$。

---

# 21. 驗證與提交

需要：

$$
\boxed{
Verify(
\pi_t,
\pi_{t+1}^{cand},
\mathcal C,
\Omega,
D,
\epsilon
).
}
$$

只有：

$$
Verify=PASS
$$

才：

$$
\boxed{
\pi_{t+1}
=
Commit(
\pi_{t+1}^{cand}
).
}
$$

若失敗：

$$
\pi_{t+1}=\pi_t
$$

或執行 fallback。

---

# 22. OPAC 基本閉環

$$
\boxed{
Observe
\rightarrow
Diagnose
\rightarrow
Generate
\rightarrow
Shadow
\rightarrow
Verify
\rightarrow
Commit
\rightarrow
Observe.
}
$$

這直接承接 AEREC 的跨代改良閉環，只是將時間索引從「版本代」移到「Runtime 狀態」。

---

# 23. AEREC 與 OPAC 的差別

AEREC 主要索引：

$$
n=\text{generation/version}.
$$

OPAC 主要索引：

$$
t=\text{runtime state/time}.
$$

AEREC：

$$
P_0\rightarrow P_1\rightarrow P_2\rightarrow\cdots
$$

OPAC：

$$
\pi_0\rightarrow\pi_{t_1}\rightarrow\pi_{t_2}\rightarrow\cdots
$$

並且可以在同一次長期 process / world execution 中完成。

---

# 24. 雙時間尺度

更完整的軟體演化有兩個時間尺度：

$$
\boxed{
n:\text{跨版本慢時間}}
$$

與：

$$
\boxed{
t:\text{執行期快時間}}.
$$

---

# 25. 雙層遞歸

跨代：

$$
\boxed{
P_{n+1}
=
\Psi(P_n,\text{long-term evidence}).
}
$$

每個版本內：

$$
\boxed{
\pi_{t+1}
=
\Phi(\pi_t,\text{runtime evidence}).
}
$$

---

# 26. Runtime 學習與版本演化

Runtime 蒐集：

- successful routes；
- failed routes；
- workload profiles；
- drift；
- rollback；
- performance。

這些可回到：

$$
P_{n+1}.
$$

而新版本又可把歷史成功 route 編入 policy、cache、classifier、compiler hints。

因此：

$$
\boxed{
RuntimeLearning
\leftrightarrow
VersionEvolution.
}
$$

---

# 27. JIT 與 OPAC 的關係

現有 JIT 已可 runtime profile、hot code compilation、lazy compilation、tiered optimization 與 deoptimization。

這些可視為 OPAC 的部分低階前例或相鄰實作模式。

但本文不宣稱：

$$
JIT=OPAC.
$$

---

# 28. 差異一：改變尺度

傳統 JIT 多半改：

$$
IR/MachineCode/Inlining/Optimization.
$$

OPAC 希望允許更廣：

$$
Algorithm
+
DataStructure
+
TaskTopology
+
Resolution
+
Backend
+
Frequency.
$$

---

# 29. 差異二：身分治理

JIT 的 correctness 一般由 compiler / VM semantics 保證。

OPAC 因 AI 可能提出跨抽象層新實現，額外需要：

$$
\boxed{
\mathcal C+\Omega+D+\epsilon.
}
$$

---

# 30. 差異三：觀測多元

OPAC 不只優化 execution time。

它可能契約化：

- state；
- security；
- permission；
- energy；
- quality；
- recoverability；
- external effects。

---

# 31. 差異四：候選治理

OPAC 明確要求：

$$
\boxed{
Candidate
\rightarrow
Evidence
\rightarrow
Commit.
}
$$

AI 無法以「我認為等價」取代驗證。

---

# 32. 現有 Runtime 最佳化仍然重要

LLVM ORC、HotSpot 與 GraalVM 類系統的意義不是替 OPAC 提供完整證明，而是證明：

$$
\boxed{
ImplementationForm
}
$$

本來就不必完全固定。

OPAC 是把 adaptive compilation 的自由度進一步擴大並契約化。

---

# 33. ACR 的接口

如果每個 state change 都重新分析所有 implementation，成本會失控。

因此 ACR 可控制：

- adaptation frequency；
- analysis depth；
- evidence retrieval；
- verifier strength；
- model cost。

OPAC 不要求每時每刻都改。

若：

$$
ExpectedGain
\le
AdaptationCost,
$$

合法 action：

$$
\boxed{NOOP.}
$$

---

# 34. 穩定本身也是選擇

成熟 adaptive system 不應：

$$
\boxed{ChangeForTheSakeOfChange.}
$$

而應：

$$
\boxed{ChangeOnlyWhenExpectedUtilityPositive.}
$$

---

# 35. Utility

定義：

$$
\boxed{
U(\pi')
=
Benefit(\pi')
-
TransitionCost
-
VerificationCost
-
Risk.
}
$$

只考慮：

$$
U>0.
$$

---

# 36. 觀測等價不等於 bit equality

某些純函數要求 Exact；某些 simulation 允許 Approximate；某些 stochastic systems 要求 Distributional。

所以 equivalence level 必須由 contract 決定。

值等價：

$$
f_a(x)=_\epsilon f_b(x).
$$

行為等價可要求公開 trace 保持一致或指定 partial-order 等價。

狀態等價：

$$
\boxed{
\alpha(S_a^{t+1})
=
\alpha(S_b^{t+1}).
}
$$

其中 $\alpha$ 是契約承認的狀態抽象。

---

# 37. 為什麼只比較當下畫面不夠？

可能：

$$
Obs(S_a^t)=Obs(S_b^t)
$$

但內部 RNG／latent state 不同，造成：

$$
Obs(S_a^{t+1})
\neq
Obs(S_b^{t+1}).
$$

所以 OPAC 必須關注：

$$
\boxed{TraceEquivalence}
$$

而不只 snapshot equivalence。

---

# 38. Rolling Horizon

對長期運行系統，完整無限未來等價通常不能直接工程驗證。

可使用：

$$
\boxed{Horizon_T}
$$

配合：

- invariants；
- replay；
- differential tests；
- runtime monitoring；
- rollback。

---

# 39. OPAC 的證明責任

本文不宣稱：

> 所有 implementation equivalence 都可被完全判定。

相反，OPAC 需要：

$$
\boxed{LayeredEvidence.}
$$

例如：

$$
E_0:\text{output sample}
$$

$$
E_1:\text{unit/property tests}
$$

$$
E_2:\text{state/trace differential}
$$

$$
E_3:\text{invariants/static proof}
$$

$$
E_4:\text{shadow runtime}
$$

$$
E_5:\text{repeated production evidence}.
$$

---

# 40. 權限與證據耦合

$$
\boxed{
AdaptationAuthority
\le
EvidenceStrength.
}
$$

低證據：Observe / Advise。

中證據：Shadow。

高證據：Low-Risk Commit。

高風險領域仍可要求 Human / External Authority。

---

# 41. 身分變更與實現變更

如果：

$$
\mathcal C
$$

真的要改，那不是 implementation optimization，而是：

$$
\boxed{SemanticMigration.}
$$

Semantic Migration 必須顯式改變：

$$
v_s.
$$

---

# 42. 不能偷偷改契約

AI 不可以為了 speedup 偷改：

- 品質；
- 世界規則；
- input domain；
- tolerance；
- security observer；
- rollback requirement。

否則：

$$
\boxed{
Optimization
\rightarrow
SemanticDrift.
}
$$

---

# 43. 合法實現等價類

令：

$$
\boxed{
[P]_{\mathcal C,\Omega,D,\epsilon}
=
\{
Q:
Q\equiv_{\mathcal C,\Omega,D,\epsilon}P
\}.
}
$$

這是所有合法實現的等價類。

---

# 44. OPAC 的在線搜尋空間

AI 不應在：

$$
AllPrograms
$$

中自由亂走。

而應在：

$$
\boxed{
[P]_{\mathcal C,\Omega,D,\epsilon}
}
$$

附近生成 candidate。

Candidate 可以暫時出界，但不能直接成為 active implementation。

---

# 45. Commit Gate

只有當：

$$
Q^{cand}
$$

有足夠證據位於可接受等價區，才：

$$
Commit(Q^{cand}).
$$

---

# 46. OPAC 核心 Invariants

## I1 — Identity Root Stable

 $r^\ast$ 不由 optimizer 偷改。

## I2 — Contract Governed

 $\mathcal C$ 只能經顯式 migration 改變。

## I3 — Observer Set Governed

不能偷偷刪掉 security / state / audit observer。

## I4 — Root Equivalence

不能只保持相鄰版本。

## I5 — Candidate Before Commit

新實現先是 candidate。

## I6 — Evidence Retained

證據可回溯。

## I7 — Rollback Exists

適用時必須可恢復。

---

# 47. OPAC 與 CDI

CDI 提供：

$$
\boxed{
\text{Implementation Selection / Routing Mechanism}.
}
$$

OPAC 提供：

$$
\boxed{
\text{什麼改變仍然算合法同一應用}.
}
$$

CDI without OPAC 的風險是：route 變快了，但功能語義也變了。

OPAC without CDI 則只有身分／等價理論，缺少 Runtime observation、routing、AIVS 與 commit mechanism。

---

# 48. 合併

$$
\boxed{
OPAC
=
AERECIdentity
+
CDIRuntimeAdaptation
+
EquivalenceGovernance.
}
$$

---

# 49. OPAC 與 AIVS

AIVS 回答：

> 什麼變化值得被 AI 看？

OPAC 回答：

> 看完後，什麼變化仍可被當成同一功能？

---

# 50. OPAC 與 Candidate/Commit

OPAC 不信任 Generation 本身。

它信任：

$$
\boxed{
Generation
+
Verification
+
GovernedCommit.
}
$$

---

# 51. OPAC 與 24／72

24／72 可以描述：

$$
\pi_t
$$

目前的計算形態。

但：

$$
p(\pi_t)
\neq
\mathcal I_{\mathrm{app}}.
$$

計算範式可以變，應用身分不一定變。

例如：

$$
\mathsf S\rightarrow\mathsf P
$$

序列變並行；或：

$$
\mathsf J/\mathsf S\rightarrow\mathsf R
$$

搜尋變 retrieval。只要契約保持，仍可屬同一應用。

---

# 52. CPU → GPU 不是身分變更

硬體映射：

$$
CPU\rightarrow GPU
$$

本身不是 semantic migration。

前提仍是：

$$
Equivalent.
$$

---

# 53. 高解析 → 低解析更敏感

如果：

$$
Resolution\downarrow
$$

仍在：

$$
\epsilon
$$

內，可合法。

否則就是 Contract Change，而不是單純最佳化。

---

# 54. 可反駁命題 H1

若在實際系統中，任何有意義的跨演算法／拓撲／解析度 Runtime 改變都無法在合理成本下建立足夠觀測等價證據，則 OPAC 的工程適用範圍非常窄。

---

# 55. 可反駁命題 H2

若：

$$
AdaptationCost\ge Benefit
$$

在絕大多數 workload 中成立，在線 adaptation 不具優勢。

---

# 56. 可反駁命題 H3

若跨代 AEREC 已足以處理所有有價值 adaptation，Runtime 級 OPAC 沒有額外價值。

---

# 57. 可反駁命題 H4

若合法觀測契約必須完整描述全部 internal state 才能安全，則：

$$
ImplementationFreedom\rightarrow0.
$$

OPAC 的自由度消失。

---

# 58. 可反駁命題 H5

若 AI 候選錯誤率／驗證成本過高，則 AI 未必適合作 controller。

OPAC 可退化為：

- deterministic optimizer；
- search；
- compiler policy；
- learned router；
- hybrid controller。

所以：

$$
\boxed{OPAC\neq AIOnly.}
$$

---

# 59. 公開技術前例的正確位置

LLVM ORC：lazy JIT、concurrent compilation、IR optimization layer、remote execution。

HotSpot：runtime profiling、tiered compilation、adaptive compilation。

GraalVM：hotspot detection、optimizing compiler、partial evaluation / runtime optimization。

它們支持：

$$
\boxed{RuntimeImplementationCanAdapt.}
$$

---

# 60. 它們不能直接支持什麼？

不能直接推出：

- 任意演算法可在線替換；
- 任意資料結構可在線改變；
- 任意世界模擬可降解析；
- 觀測等價一定可驗證；
- AI governance 一定有淨收益。

這些仍是 OPAC 的研究問題。

---

# 61. 「動態渲染」在本篇只作預告

本文先確定：

$$
\boxed{Identity\neq Implementation.}
$$

下一篇才把：

$$
[P]_{\mathcal C,\Omega,D,\epsilon}
$$

看成 Runtime 可渲染的實現空間。

---

# 62. 下一篇核心問題

如果所有合法 implementation 形成等價類 $[P]$，那麼：

> **AI 是否可以把當前 world / hardware / context 當成「渲染條件」，在 $[P]$ 中選擇一個當下最適實現？**

下一篇將引入：

- 觀測纖維；
- 等價類；
- implementation graph / geometry；
- Execution Rendering；
- runtime re-materialization；
- current-state vs future-trace equivalence；
- observer-relative freedom。

---

# 63. 本篇最核心的一句

$$
\boxed{
\text{程式的身分可以穩定，
而程式的實現可以持續改變。}
}
$$

---

# 64. 更精確的一句

$$
\boxed{
\text{真正被保存的，不必是程式碼；
可以是可追溯、可治理、可驗證的觀測功能身分。}
}
$$

---

# 65. 結論

AEREC 已經建立：

$$
\boxed{
\text{程式完成}
\not\Rightarrow
\text{程式停止演化}.
}
$$

CDI 則進一步提出：

$$
\boxed{
\text{程式正在執行}
\not\Rightarrow
\text{執行形態必須固定}.
}
$$

兩者交會後得到：

$$
\boxed{
\text{Stable Observable Identity}
+
\text{Mutable Runtime Implementation}.
}
$$

本文將其命名為：

# **Observer-Preserving Adaptive Computation**
# **觀測保持型自適應計算（OPAC）**

OPAC 的核心不是允許 AI 任意修改程式，而是建立一個受約束的自由空間：

$$
\boxed{
[P]_{\mathcal C,\Omega,D,\epsilon}.
}
$$

AI／controller 可以在這個空間裡搜索、分叉、shadow、比較、切換與回退，但正式 active implementation 必須持續滿足：

$$
\boxed{
\pi_t
\equiv_{\mathcal C,\Omega,D,\epsilon}
\pi_0.
}
$$

因此真正不變的不是 Source、Binary、Algorithm、Topology 或 Hardware；真正不變的是：

$$
\boxed{
\text{Contracted Observable Identity}.
}
$$

這也為下一篇建立最直接的入口：

> 如果身分是一個觀測等價類，那麼一個正在運行的程式，就可以被理解成在同一等價類中持續「重新渲染」其當下實現。

---

## 參考資料

### 內部研究線

1. Neo.K with Aletheia，《程式完成之後：AI 自適應封裝與遞歸演化計算論的總命題》，2026。
2. Neo.K with Aletheia，《同一個應用是什麼：功能契約、觀測等價與程式身分》，2026。
3. Neo.K with Aletheia，《無限遞歸改良動力學：觀測、診斷、生成、驗證與提交》，2026。
4. Neo.K with Aletheia，《功能不變如何被證明：等價證書、差分驗證與安全回滾》，2026。
5. Neo.K with Aletheia，《AI 自適應封裝與遞歸演化系統技術架構白皮書》，2026。
6. Neo.K with Aletheia，《計算域支配智能：AI 語義控制面與自適應多 X 計算》系列，2026。
7. Neo.K with Aletheia，《Adaptive Cognitive Runtime 工程白皮書》，2026。

### 2026-08-10 Fresh Technical References

8. LLVM Project, *ORC Design and Implementation*, current LLVM documentation。
9. LLVM Project, *Building an ORC-based JIT*, current LLVM documentation。
10. Oracle, *Java HotSpot Virtual Machine Performance Enhancements*, Java 17 documentation。
11. GraalVM, *GraalVM as a Java Virtual Machine*, current reference manual。
12. GraalVM, *Optimizing Truffle Interpreters*, current reference manual。

---

## 版本紀錄

- **v0.1 / 2026-08-10**：建立 OPAC 母命題、AEREC 跨代演化與 CDI 在線演化之雙時間尺度、Contracted Observable Identity、Runtime Adaptation Operator、Root Equivalence、Evidence/Authority 邊界、OPAC 與 JIT/HotSpot/GraalVM 的差異，以及下一篇 Execution Rendering 接口。
