# AMRAL Research Lab 網站升級交接文件 v0.1

**目標站點：** https://amral.evemisslab.com/  
**日期：** 2026-08-11  
**用途：** 交給本地端 AI / Coding Agent 進行網站資訊架構與內容升級  
**狀態：** READY_FOR_LOCAL_IMPLEMENTATION

---

# 0. 本次升級的核心原因

AMRAL 最初是一套相對明確的方法論與研究循環：

\[
\mathrm{RIITG}
+
\mathrm{RAB}
+
\mathrm{KCPE}
+
\mathrm{AMRAL\ Loop}
\]

並已實際用於黎曼猜想等 AI 自主／半自主數學研究。

但目前研究已自然擴張出新的研究方式，例如：

\[
\boxed{
\text{Aggressive Discovery}
\rightarrow
\text{Adversarial Audit}
\rightarrow
\text{Neutral Academic Assessment}
}
\]

這套「三 AI 研究協議」並不要求每次都使用 RIITG、RAB、KCPE。

因此網站不應再隱含：

> 所有 AMRAL 案例都必須使用同一套 AMRAL 方法論。

新的網站架構應改成：

\[
\boxed{
\text{AMRAL Research Lab}
\supset
\text{multiple methods, protocols, autonomy modes, validation layers, and cases}
}
\]

也就是：

> **AMRAL 從「單一方法論名稱」升級為「AI 自主數學研究實驗室／研究平台」。**

原本的方法論保留，不刪除、不降級，改稱：

\[
\boxed{
\text{AMRAL-Core}
}
\]

---

# 1. 最重要的架構原則

新的 AMRAL 不應再只有一條強制流程。

每一個研究 Case 應由以下幾個彼此獨立的軸描述：

\[
\boxed{
\text{Case}
\times
\text{Methodology}
\times
\text{Protocol}
\times
\text{Autonomy}
\times
\text{Validation}
}
\]

## 軸 A：Case

回答：

> 研究什麼？

例如：

- Riemann Hypothesis
- Erdős Problem #885
- Erdős Problem #302
- Erdős Problem #376
- WOWII Graph Conjecture 144
- 未來其他問題

---

## 軸 B：Methodology

回答：

> 如何產生、展開與收斂研究路徑？

可能值：

- AMRAL-Core
- RIITG
- RAB
- KCPE
- Direct Search
- Computational Search
- Constructive Search
- Literature-Guided Search
- 未來其他方法

注意：

\[
\boxed{
\text{Methodology 可以為 multiple，也可以為 none / direct attack。}
}
\]

---

## 軸 C：Protocol

回答：

> AI／研究角色如何協作？

目前新增：

### TRP — Triadic Research Protocol

三個角色：

1. Agent A — Aggressive Discovery
2. Agent B — Adversarial Proof Audit
3. Agent C — Neutral Academic Assessment

未來可新增：

- Single-Agent Protocol
- Swarm Protocol
- Blind Re-Derivation Protocol
- Human Referee Protocol
- Multi-Lab Replication Protocol

---

## 軸 D：Autonomy Mode

回答：

> 誰掌握研究方向與排程？

建議固定枚舉：

```text
human-led
semi-autonomous
autonomous
multi-agent-autonomous
```

必要時可增加：

```text
human-supervised-autonomous
```

---

## 軸 E：Validation

回答：

> 研究結果如何被合法化、定量閉合與驗證？

目前至少包含：

- QCI — Quantitative Closure Interface
- Target Fidelity Audit
- Adversarial Review
- Blind Re-Derivation
- Proves-Too-Much Test
- Numerical Certificate
- Lean 4
- Coq
- External Expert Review
- Evidence / Trust Boundary

---

# 2. AMRAL 新總體資訊架構

建議網站導覽升級為：

```text
AMRAL Research Lab
│
├─ Home
│
├─ About / What is AMRAL?
│
├─ Methodologies
│  │
│  ├─ AMRAL-Core
│  │   ├─ RIITG
│  │   ├─ RAB
│  │   ├─ KCPE
│  │   └─ AMRAL Loop
│  │
│  ├─ Direct / Computational Research
│  └─ Experimental Methods
│
├─ Research Protocols
│  │
│  ├─ TRP — Triadic Research Protocol
│  │   ├─ Agent A: Aggressive Discovery
│  │   ├─ Agent B: Adversarial Audit
│  │   └─ Agent C: Academic Assessment
│  │
│  └─ Future Protocols
│
├─ Validation
│  ├─ QCI
│  ├─ Target Fidelity
│  ├─ Formal Verification
│  ├─ Certificates
│  └─ Trust / Evidence Boundary
│
├─ Research Modes
│  ├─ Human-Led
│  ├─ Semi-Autonomous
│  ├─ Autonomous
│  └─ Multi-Agent Autonomous
│
├─ Cases
│  ├─ Riemann Hypothesis
│  │   ├─ Autonomous Track
│  │   └─ Semi-Autonomous Track
│  │
│  ├─ Erdős #885
│  ├─ Erdős #302
│  ├─ Erdős #376
│  └─ ...
│
├─ Experiments / Benchmarks
│
├─ Research Timeline
│
├─ Failures / Revisions
│
└─ Downloads / Artifacts
```

---

# 3. 首頁定位必須修改

## 舊問題

目前首頁容易讓人理解：

> AMRAL = RIITG + RAB + KCPE + 固定九步循環。

但未來這個等式不再成立。

應改為：

\[
\boxed{
\text{AMRAL}
=
\text{AI Autonomous Mathematics Research Lab / Platform}
}
\]

而：

\[
\boxed{
\text{AMRAL-Core}
=
\text{the original methodology stack}
}
\]

---

# 4. 建議首頁核心文案

可使用以下方向，不要求逐字照抄：

> **AMRAL 是一個用於 AI 自主、半自主與多 Agent 數學研究的實驗室與研究平台。**
>
> 它最初由 RIITG、RAB、KCPE 與 AMRAL 自主研究循環發展而來，但平台本身不要求所有研究案例使用同一方法論。
>
> 不同 Case 可以採用：
>
> - AMRAL-Core；
> - 直接搜索；
> - 計算探索；
> - 三 Agent 研究協議；
> - QCI 定量閉合；
> - 形式化驗證；
> - 或其他未來研究方法。
>
> AMRAL 的核心要求不是「所有研究走同一條路」，而是：
>
> \[
> \boxed{
> \text{研究過程必須可追蹤、可否證、可修正、可交棒、可驗證。}
> }
> \]

---

# 5. AMRAL-Core 頁面

原 `/methodology/` 頁不要刪。

建議：

```text
/methodologies/amral-core/
```

或者保留原 URL：

```text
/methodology/
```

但頁面標題改成：

> AMRAL-Core Methodology

並明確說：

> 這是 AMRAL Research Lab 的原始核心方法論，不是所有 Case 的強制要求。

保留：

- RIITG
- RAB
- KCPE
- 九步研究循環
- 既有公式與說明

不要因本次升級破壞歷史版本。

---

# 6. 新增 TRP 頁面

建議 URL：

```text
/protocols/trp/
```

頁名：

# TRP — Triadic Research Protocol

副標：

> Bold Discovery · Hostile Verification · Neutral Assessment

核心：

\[
\boxed{
\text{Agent A}
\rightarrow
\text{Agent B}
\rightarrow
\text{Agent C}
}
\]

## Agent A

Aggressive Discovery

- 高發散；
- 高探索；
- 高自信主攻；
- 可提出大膽 conjectural bridge；
- 不因「怕 hallucination」而停止研究；
- 但未證步驟必須標示。

核心原則：

\[
\boxed{
\text{Bold generation}
\neq
\text{bold public claim}
}
\]

## Agent B

Adversarial Proof Audit

- 專找第一個不合法步驟；
- 量詞；
- domain；
- uniformity；
- error；
- tail；
- local-to-global；
- counterexample；
- proves-too-much；
- formal gap。

## Agent C

Neutral Academic Assessment

只判：

- strongest defensible claim；
- completion level；
- novelty；
- QCI closure；
- publication readiness；
- likely referee objections。

---

# 7. 新增 QCI 頁面

建議：

```text
/validation/qci/
```

標題：

# QCI — Quantitative Closure Interface

定義：

> 一個主要依賴定性、拓樸、幾何、代數或組合結構的證明策略，在提升為全域解析／算術命題之前，必須經過的合法性、可容許性、估計精度、誤差控制與一致量化層。

核心：

\[
\boxed{
\mathcal T
\xrightarrow{\Phi}
\mathcal A_{\mathrm{admissible}}
\xrightarrow{Q}
\mathcal R
}
\]

QCI debt：

\[
D^{\mathrm{QCI}}
=
(
D_{\mathrm{def}},
D_{\mathrm{adm}},
D_{\mathrm{quant}},
D_{\mathrm{uniform}},
D_{\mathrm{error}},
D_{\mathrm{tail}},
D_{\mathrm{global}},
D_{\mathrm{consistency}},
D_{\mathrm{formal}}
).
\]

---

# 8. Research Modes 頁面

新增：

```text
/research-modes/
```

說明「自主程度」與「方法論」不同。

## Human-Led

人類決定主要方向，AI 是研究工具。

## Semi-Autonomous

人類決定主問題與部分方向，AI 可自主展開子研究。

## Autonomous

AI 可自己建立研究節點、排程、攻擊、修正、交棒。

## Multi-Agent Autonomous

多個 AI / Agent 分角色、並行、自主協作。

重要：

\[
\boxed{
\text{Autonomy Mode}
\neq
\text{Methodology}
}
\]

---

# 9. Case 頁統一 Metadata

所有 Case 頁未來應盡量使用共同 schema。

建議：

```yaml
case_id: ERDOS-885-K5
title: Erdős Problem #885 — k=5

problem:
  source: ...
  status: open
  target: ...

research_mode:
  autonomy: multi-agent-autonomous
  human_role: supervisor

methodology:
  primary:
    - direct-search
  optional:
    - AMRAL-Core
    - RIITG
    - RAB

protocol:
  - TRP-v0.1

validation:
  - QCI-v0.1
  - adversarial-review
  - blind-rederivation
  - Lean4-if-survives

claim_policy:
  unverified_bridge_must_be_labeled: true
  finite_not_global: true

artifacts:
  claims_ledger: ...
  failures: ...
  qci_debt: ...
  formal: ...
  code: ...
```

---

# 10. Riemann Hypothesis Case 的遷移

現有 RH 內容不要刪。

新的 RH Case 頁應呈現成：

```text
Riemann Hypothesis
│
├─ Autonomous Track
│  ├─ Method: AMRAL-Core
│  ├─ Validation: QCI-like finite certification / certificates
│  ├─ Batch 01
│  └─ Case 0001
│
└─ Semi-Autonomous Track
   ├─ Mode: Neo-led / semi-autonomous
   ├─ Methods: multiple
   ├─ qualitative/topological routes
   └─ current status / limitations
```

重點：

不要把兩條軌道寫成：

```text
好 / 壞
AI > Human
```

而是：

```text
不同 autonomy / methodology / research objective
```

---

# 11. 新候補猜想 Case 區

未來新增：

```text
/cases/erdos-885/
/cases/erdos-302/
/cases/erdos-376/
/cases/wowii-144/
```

每個 Case 顯示：

- Source
- Current public status
- MCDM profile
- Achievement Ladder
- Research mode
- Methodology
- Protocol
- Validation
- QCI debt
- Current strongest claim
- Formal status
- Failures
- Artifacts
- Next round

---

# 12. Achievement Ladder UI

建議在 Case 頁加入「蠶食進度梯」。

例如 Erdős #885：

```text
[ ] k=5
[ ] k=6
[ ] k<=K
[ ] parametric family
[ ] full ∀k
```

不要用「RH 完成度 67%」那種易誤解呈現。

這裡只表示：

```text
research milestones
```

不是 theorem truth percentage。

---

# 13. Completion Level

可加入統一 Level：

```text
0 Idea
1 Heuristic
2 Conditional Result
3 Finite / Computational Certificate
4 Rigorous Partial Theorem
5 Full Theorem Candidate
6 Independently Verified Theorem
```

Case 頁顯示：

```text
Current Level: 3
```

必須附說明，避免看起來像「猜想已完成 50%」。

---

# 14. Claim Status

固定：

```text
CONJECTURAL
HEURISTIC
NUMERICAL
CONDITIONAL
FINITE_CERTIFICATE
PROVED_PARTIAL
FULL_PROOF_CANDIDATE
FORMALLY_VERIFIED
DISPROVED
SUPERSEDED
```

---

# 15. QCI Status UI

可以顯示：

```text
QCI
✓ Well-definedness
✓ Admissibility
△ Quantitative bound
✗ Uniformity
△ Error budget
N/A Tail
✗ Local-to-global
✓ Consistency
○ Formalization
```

狀態：

```text
CLOSED
PARTIAL
OPEN
FAILED
N/A
```

---

# 16. TRP Round UI

若 Case 使用 TRP：

```text
Round 001

Agent A — Candidate
Status: COMPLETE

Agent B — Audit
Status: GAP_FOUND

Agent C — Assessment
Level: 2

Next:
Repair Lemma L3
```

---

# 17. 網站首頁建議新增卡片

## Methodologies

- AMRAL-Core
- Direct Search
- Experimental Methods

## Protocols

- TRP
- Future protocols

## Validation

- QCI
- Formal Verification
- Adversarial Review

## Active Cases

- RH
- Erdős #885
- #302
- #376

---

# 18. 舊網址相容性

非常重要。

不要破壞：

```text
/riemann/
/riemann/autonomous/
/riemann/semi-autonomous/
/methodology/
```

如果資訊架構改動：

- 保留舊 URL；
- 或做 redirect；
- sitemap 不應產生大量 404。

---

# 19. SEO / AI-readable Metadata

每頁至少提供：

```html
title
description
canonical
OpenGraph
JSON-LD if available
```

並更新：

```text
sitemap.xml
robots.txt
llms.txt
```

若站上已有 AI-native metadata，沿用現有格式。

---

# 20. 首頁不要寫成宣傳誇張文案

避免：

> AMRAL 將解決所有數學難題。

應改成：

> AMRAL experiments with reproducible workflows for human-led, semi-autonomous, autonomous and multi-agent mathematical research.

強調：

- research infrastructure；
- reproducibility；
- failure preservation；
- verification；
- multiple methodologies。

---

# 21. 網站中的「AMRAL」名稱語義

本次升級後統一：

## AMRAL

上位：

```text
Research Lab / Platform
```

## AMRAL-Core

原始方法論。

## AMRAL Case

站內研究案例。

不要再寫：

```text
AMRAL methodology = everything on this website
```

---

# 22. 建議新的首頁一句話

中文版：

> **AMRAL 是一個用於人類主導、半自主、自主與多 Agent 數學研究的可重播研究實驗室。不同案例可以使用不同方法與協議；共同要求是研究狀態、失敗、證書與驗證邊界必須可追蹤。**

英文版：

> **AMRAL is a replayable research lab for human-led, semi-autonomous, autonomous, and multi-agent mathematical research. Cases may use different methods and protocols; what they share is traceable research state, failures, certificates, and verification boundaries.**

---

# 23. 建議新增路由

優先：

```text
/about/
/methodologies/
/methodologies/amral-core/
/protocols/
/protocols/trp/
/validation/
/validation/qci/
/research-modes/
/cases/
```

可後續：

```text
/benchmarks/
/experiments/
/artifacts/
/failures/
```

---

# 24. Case Index 篩選器

未來 Case 多後可篩：

```text
Problem Domain
Methodology
Protocol
Autonomy
Validation
Status
Completion Level
```

例如：

```text
Protocol: TRP
Autonomy: multi-agent-autonomous
Status: active
```

---

# 25. 本地端 AI 執行規則

Coding Agent 開始前：

1. 先掃描現有 repo。
2. 列出 framework / stack / router。
3. 找出現有 routes。
4. 找出共用 layout / data schema。
5. 不要先大規模重寫。
6. 優先做 backward-compatible migration。
7. 不要刪舊研究內容。
8. 保留歷史 URL。
9. 所有現有 RH artifacts 繼續可訪問。
10. 新架構完成後再逐頁遷移。

---

# 26. 實作順序

## Phase 1 — IA / Navigation

先完成：

- AMRAL → Research Lab 定位
- Methodologies
- Protocols
- Validation
- Research Modes
- Cases

## Phase 2 — Core Pages

新增：

- AMRAL-Core
- TRP
- QCI
- Research Modes

## Phase 3 — Case Schema

建立統一 Case metadata。

## Phase 4 — RH Migration

把 Autonomous / Semi-Autonomous 加上：

- autonomy
- methodology
- validation

但不破壞原頁。

## Phase 5 — New Candidate Cases

建立 placeholder：

- Erdős #885
- #302
- #376
- WOWII #144

先標：

```text
STATUS = CANDIDATE / NOT_STARTED
```

不要誤寫成 active result。

## Phase 6 — Search / Filter / Timeline

有餘力再做。

---

# 27. 驗收條件

升級完成後至少要滿足：

### Architecture

- [ ] AMRAL 不再被描述為單一強制方法。
- [ ] AMRAL-Core 可獨立訪問。
- [ ] TRP 有獨立頁。
- [ ] QCI 有獨立頁。
- [ ] Autonomy 與 Method 分開。

### Backward Compatibility

- [ ] 舊 RH Autonomous URL 正常。
- [ ] 舊 RH Semi-Autonomous URL 正常。
- [ ] 原 methodology 內容不丟失。

### Case Model

- [ ] Case 可以標多種 methodology。
- [ ] Case 可以標 protocol。
- [ ] Case 可以標 autonomy。
- [ ] Case 可以標 validation。
- [ ] Case 可以標 completion / claim status。

### Integrity

- [ ] 不把 heuristic 改寫成 theorem。
- [ ] 不把 finite certificate 改寫成 global proof。
- [ ] 不把 candidate problem 寫成 solved。
- [ ] 失敗與 supersession 不刪除。

### UI

- [ ] 首頁可理解 AMRAL 是 Lab / Platform。
- [ ] 使用者能區分 Method / Protocol / Autonomy / Validation。
- [ ] Mobile / desktop 正常。
- [ ] sitemap 更新。

---

# 28. 禁止事項

本地端 AI 不要：

1. 為了統一風格刪掉舊研究歷史。
2. 把所有 Case 強制改成 TRP。
3. 把所有 Case 強制改成 AMRAL-Core。
4. 把 QCI 當成必須先於所有研究生成的方法論。
5. 把 Autonomous 等同「無人類參與」。
6. 把 Semi-Autonomous 解讀成「較差版本」。
7. 把 Agent A 的 confidence 顯示成 theorem confidence。
8. 把 completion level 顯示成猜想完成百分比。
9. 把未開始候補題寫成 active proof project。
10. 因網址重構製造大量 404。

---

# 29. 最終概念圖

\[
\boxed{
\begin{array}{c}
\text{AMRAL Research Lab}\\
\\
\downarrow\\
\\
\text{Cases}
\times
\text{Methods}
\times
\text{Protocols}
\times
\text{Autonomy}
\times
\text{Validation}
\end{array}
}
\]

其中：

\[
\boxed{
\text{AMRAL-Core}
\subset
\text{Methods}
}
\]

\[
\boxed{
\text{TRP}
\subset
\text{Protocols}
}
\]

\[
\boxed{
\text{QCI}
\subset
\text{Validation}
}
\]

而：

\[
\boxed{
\text{Human-Led / Semi / Autonomous / Multi-Agent}
\subset
\text{Autonomy}
}
\]

這四者不要再混成同一條流程。

---

# 30. 本次升級的最終目的

不是「網站看起來更複雜」。

而是讓 AMRAL 能長期承載：

- 不同 AI；
- 不同數學問題；
- 不同研究風格；
- 不同 Agent 架構；
- 不同驗證強度；
- 不同自主程度。

並仍然保持：

\[
\boxed{
\text{Traceable}
+
\text{Replayable}
+
\text{Falsifiable}
+
\text{Revisable}
+
\text{Verifiable}
}
\]

---

# 31. 給 Coding Agent 的最終指令

> 請把 AMRAL 從「單一 AI 自主數學方法論網站」升級成「可承載多方法、多協議、多自主模式、多驗證層的 AI 數學研究實驗室網站」。
>
> 不要刪除原本 RIITG / RAB / KCPE / RH-W 等內容。
>
> 原方法論重新定位為 AMRAL-Core。
>
> 新增 TRP 與 QCI。
>
> 將 Methodology、Protocol、Autonomy、Validation、Case 五個概念在資料層與 UI 層分離。
>
> 先確保既有網站相容，再逐步導入新架構。
>
> 若實際 repo 結構與本文件假設不同，以既有實作為準，做最小破壞式重構；不得為了符合文件而無必要重寫整站。

---

**文件版本：** v0.1  
**狀態：** READY_FOR_HANDOFF  
**主要升級：** AMRAL Methodology → AMRAL Research Lab / AMRAL-Core separation  
