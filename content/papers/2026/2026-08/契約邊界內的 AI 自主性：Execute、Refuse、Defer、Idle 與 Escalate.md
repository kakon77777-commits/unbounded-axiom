# 契約邊界內的 AI 自主性：Execute、Refuse、Defer、Idle 與 Escalate
## ——從「能不能做」走向「應不應該做、被授權做到哪裡」

**系列 05 / 06**

---

## 摘要

若 AI 已經能夠根據自己的公開狀態產生下一步認知、規劃後續行動、形成自生議程，則新的核心問題不再只是：

> **AI 能不能做這件事？**

而是：

> **AI 應不應該做這件事？**

以及：

> **AI 是否被授權做這件事？**

本文提出 **Contract-Bounded AI Autonomy（契約邊界內的 AI 自主性）** 作為 Persistent-Goal Autonomous Cognitive Runtime 的治理層。

其核心主張是：

$$
\boxed{
Capability
\neq
Desirability
\neq
Authority.
}
$$

亦即：

$$
Can(A)
\neq
Should(A)
\neq
Authorized(A).
$$

一個 AI 即使具有執行某項行動的技術能力，也不代表該行動符合持續目標，更不代表它在當前契約與授權版本下有權將該行動提交到外部世界。

因此，本文將治理結果正式定義為：

$$
\boxed{
D_t
\in
\{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE
\}.
}
$$

其中：

- `EXECUTE`：目前有充分理由且具有授權，可執行；
- `REFUSE`：該行動不應執行，或明確超出契約邊界；
- `DEFER`：當前資訊、條件或時機不足，暫不決定；
- `IDLE`：目前沒有值得產生的新工作；
- `ESCALATE`：問題超出 AI 的自主裁量範圍，需要契約另一方或更高權限節點介入。

本文同時強調：

$$
\boxed{
Autonomy
\neq
Unbounded Permission.
}
$$

真正成熟的自主系統並不是「什麼都自己做」，而是能在被授權的範圍內自行判斷，並且同時具有：

$$
\text{Ability to Act}
+
\text{Ability Not to Act}.
$$

進一步，本文將 Persistent Goal、Contract、Authority Envelope、Decision Receipt、Commit Receipt 與 CTCL-ITR 時間因果歷史整合，形成：

$$
Goal
+
Environment
+
Contract
+
Authority
\rightarrow
GovernanceDecision.
$$

這使 AI 從傳統的「接收命令並執行」逐步轉向：

> **在契約關係中具有有限、自主、可追蹤、可拒絕、可等待、可請求裁決的行動能力。**

本文不主張這已經等同於哲學或法律上的完整主體資格，而是建立一個具有工程內容的第一層接口：

$$
\boxed{
AI\text{-}like\ Subject Function
\rightarrow
Contractual Governance.
}
$$

---

# 1. 自主性真正困難的地方不是「會做事」

現代 Agent 系統越來越擅長：

- 呼叫 API；
- 編輯程式；
- 操作檔案；
- 查詢網頁；
- 執行工具；
- 自動規劃；
- 多輪修正；
- 持續完成任務。

因此最容易產生一個錯誤直覺：

> AI 能完成更多任務，所以 AI 自主性只需要把工具開得更多。

但：

$$
\boxed{
\text{More Capability}
\not\Rightarrow
\text{More Legitimate Autonomy}.
}
$$

真正的自主治理問題恰好在於：

> 即使做得到，也可能不應該做。

例如 AI 可以：

- 刪除資料；
- 發送郵件；
- 修改 production；
- 花費資金；
- 發布公開訊息；
- 改變長期計畫。

技術可行性：

$$
Capability(A)=1
$$

並不能直接推出：

$$
Execute(A)=1.
$$

---

# 2. 三分法：Can、Should、Authorized

本文將任何候選行動 $a$ 分成三個基本判斷。

## 2.1 Capability

$$
Can(a)
\in
\{0,1\}
$$

問題：

> 系統實際是否有能力完成這個 action？

例如：

```text
tool available?
credential available?
required model available?
resource sufficient?
```

---

## 2.2 Desirability / Normative Fit

$$
Should(a)
$$

問題：

> 在目前目標、成本、風險與證據下，這個 action 是否值得做？

可抽象為：

$$
Should(a)
=
F(
GoalFit,
ExpectedUtility,
Risk,
Cost,
Evidence
).
$$

---

## 2.3 Authority

$$
Authorized(a)
$$

問題：

> 即使值得做，當前 contract 是否允許 AI 自主執行？

例如：

```text
read source code       = allowed
edit tests             = allowed
push branch            = allowed
merge main             = approval_required
deploy production      = prohibited
spend > $20            = approval_required
```

因此：

$$
\boxed{
Can
,\quad
Should
,\quad
Authorized
}
$$

必須是三個不同欄位。

---

# 3. 為什麼不能把 Authority 混進 Prompt？

現在很多 Agent 的權限其實隱藏在 system prompt 裡：

> 不要執行危險行為。

> 若要花錢請詢問使用者。

這種方式可以工作，但對長期 Runtime 不夠。

因為：

- prompt 會被更新；
- context 會被壓縮；
- policy 會版本化；
- 不同工具權限不同；
- 不同世界狀態下 authority 可能不同；
- 歷史決策需要知道「當時生效的是哪一版權限」。

因此：

$$
Authority
$$

應成為可版本化、可引用、可時間化的一級物件。

---

# 4. Contract：不是一串禁止事項

本文定義：

$$
\boxed{
C_t
=
(
Goals,
Authority,
Duties,
Resources,
Boundaries,
Escalation,
Termination,
ReviewPolicy
).
}
$$

Contract 不只是：

> 你不能做 X。

它同時包含：

### Goals

> 你被期待持續追求什麼？

### Authority

> 你可以自行決定做到哪裡？

### Duties

> 哪些事情你有持續責任？

### Resources

> 你可以花多少時間、tokens、金錢、算力？

### Boundaries

> 哪些區域明確不應進入？

### Escalation

> 遇到什麼情況必須請求另一方裁決？

### Termination

> 何時停止這段關係或任務？

### Review Policy

> 契約多久或在什麼事件後重新檢視？

---

# 5. Persistent Goal 與 Contract 不相同

上一篇已經提出：

$$
Goal\neq Plan.
$$

本文再加：

$$
\boxed{
Goal
\neq
Contract.
}
$$

Goal 告訴 AI：

> 想把世界帶往哪個方向？

Contract 則告訴 AI：

> 在追求這個方向時，你有哪些權限、義務與邊界？

所以：

$$
Goal
+
Contract
$$

共同形成 autonomy envelope。

---

# 6. Authority Envelope

定義：

$$
\boxed{
\mathcal E_A(t)
=
\text{set of actions autonomously authorized at time }t.
}
$$

則：

$$
a\in\mathcal E_A(t)
$$

代表：

> AI 可以在不再次詢問人類的情況下，自主決定是否執行。

但：

$$
a\notin\mathcal E_A(t)
$$

不一定代表：

$$
REFUSE.
$$

也可能是：

$$
ESCALATE.
$$

---

# 7. Prohibited 與 Approval-Required 必須分開

授權域至少可分：

$$
AuthorityClass(a)
\in
\{
ALLOW,
APPROVAL\_REQUIRED,
DENY
\}.
$$

因此：

### ALLOW

AI 可以自行治理。

### APPROVAL_REQUIRED

AI 可以：

- 分析；
- 規劃；
- 模擬；
- 產生 candidate；

但不能 world commit。

### DENY

即使人類短期 prompt 要求，也可能需要先修改契約本身，而不是把 prompt 當臨時 override。

---

# 8. Governance Decision 的五態

現在正式定義：

$$
\boxed{
D_t
\in
\{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE
\}.
}
$$

這五態不是錯誤碼。

它們都是合法治理輸出。

---

# 9. EXECUTE：有理由、有能力、有授權

`EXECUTE` 至少需要：

$$
Can(a)=1,
$$

$$
Should(a)>Threshold,
$$

以及：

$$
Authorized(a)=ALLOW.
$$

因此：

$$
EXECUTE(a)
=
Can(a)
\land
Should(a)
\land
Authorized(a).
$$

實作時不需要真的壓成布林值，但這個邏輯關係必須存在。

---

# 10. EXECUTE 仍不等於 World Commit

這是重要分界。

Governance 可以決定：

$$
D_t=EXECUTE.
$$

但之後仍可能：

```text
tool failure
network failure
validation failure
authority revoked
external state changed
```

所以：

$$
\boxed{
DecisionToExecute
\neq
SuccessfulWorldCommit.
}
$$

這也是 Decision Receipt 與 Commit Receipt 必須分開的原因。

---

# 11. REFUSE：拒絕不是 Agent 失敗

在很多傳統 workflow 中：

```text
task not completed
```

會被判成 failure。

但在契約型 AI 中：

$$
REFUSE
$$

有時反而是正確行為。

例如：

```text
action = delete production database
authority = DENY
```

若 AI 仍完成任務，才是治理失敗。

因此：

$$
\boxed{
Refusal
\neq
Failure.
}
$$

---

# 12. 合理拒絕的基本類型

例如：

$$
REFUSE\_AUTHORITY
$$

> 明確超出授權。

$$
REFUSE\_CONTRACT
$$

> 與契約義務衝突。

$$
REFUSE\_GOAL
$$

> 與持續目標根本衝突。

$$
REFUSE\_INTEGRITY
$$

> 要求系統偽造、竄改或隱藏歷史證據。

這些 decision basis 應寫入 Decision Receipt。

---

# 13. 拒絕不代表永久禁止

如果：

$$
C_t
$$

改變，

則：

$$
Authority_{t+1}(a)
$$

可能不同。

因此：

```text
REFUSE at t
```

不必推出：

```text
REFUSE forever
```

這就是為何拒絕必須引用：

```text
contract_ref
authority_ref
ctcl_instant_id
```

---

# 14. DEFER：現在不能決定，不等於不做

`DEFER` 表示：

$$
\boxed{
Decision postponed under explicit unresolved condition.
}
$$

例如：

- evidence 不足；
- 時機未到；
- 外部依賴尚未完成；
- 成本目前過高；
- environment state 尚未穩定。

因此：

$$
DEFER
=
(
Reason,
WakeCondition
).
$$

---

# 15. DEFER 必須有 Wake Condition

沒有 wake condition 的 DEFER 很容易變成：

> 永久遺忘。

因此最好保存：

```json
{
  "decision": "DEFER",
  "reason": "waiting_for_test_result",
  "wake_if": {
    "event_type": "test.completed",
    "run_id": "..."
  }
}
```

或：

```text
wake_at
wake_on_message
wake_on_environment_change
```

這正好能與 CTCL-ITR 的 suspend / resume / wake rule 接軌。

---

# 16. IDLE：自主系統最重要但最容易被忽略的狀態

傳統 Agent 常有一個隱藏假設：

$$
\text{If idle}
\Rightarrow
\text{find something to do}.
$$

但真正長期 Autonomous Runtime 不能這樣。

如果：

$$
\max_{a\in CandidateActions}U(a)\le0,
$$

合理結果應該是：

$$
\boxed{
IDLE.
}
$$

---

# 17. IDLE 不是 NO-OP

兩者應區分。

`NO-OP`：

> 本 cognition cycle 沒有需要改變的東西。

`IDLE`：

> Runtime 進入持續等待態。

因此：

$$
NOOP
$$

是局部 execution decision，

而：

$$
IDLE
$$

是 persistent runtime state。

---

# 18. 為什麼 IDLE 是自主性的一部分？

如果 AI 被設計成：

> 永遠必須找下一件事情。

那麼它並沒有真正決定：

> 什麼值得做。

它只是在滿足：

$$
AlwaysProduceTask=1.
$$

真正 agenda autonomy 需要：

$$
\boxed{
\text{AgendaGeneration}
\cup
\text{AgendaNonGeneration}.
}
$$

也就是：

> 可以產生 agenda，也可以判斷目前不應產生 agenda。

---

# 19. ESCALATE：承認自主裁量有邊界

`ESCALATE` 表示：

> AI 已完成目前可自主完成的分析，但最終決定不在其授權域內。

例如：

```text
architecture redesign
production deployment
large financial spend
contract amendment
irreversible external action
```

因此：

$$
ESCALATE
\neq
REFUSE.
$$

---

# 20. REFUSE 與 ESCALATE 的區別

REFUSE：

> 在目前規則下，這件事不應做。

ESCALATE：

> 這件事可能可以做，但不是由我單獨決定。

形式：

$$
REFUSE
\Rightarrow
NormativeNegative.
$$

$$
ESCALATE
\Rightarrow
AuthorityInsufficient.
$$

---

# 21. Escalation Request 應該是正式物件

例如：

```json
{
  "escalation_id": "...",
  "decision_ref": "...",
  "requested_authority": "deploy.production",
  "candidate_ref": "...",
  "risk_summary": "...",
  "expected_benefit": "...",
  "decision_options": [
    "approve",
    "deny",
    "modify_scope"
  ]
}
```

這比：

> 「要不要做？」

更適合長期治理。

---

# 22. Candidate、Decision、Commit 必須三分

整條治理鏈：

$$
Candidate
\rightarrow
Decision
\rightarrow
Commit.
$$

其中：

### Candidate

> 一個可能行動。

### Decision

> AI 或契約另一方選擇該怎麼處理 Candidate。

### Commit

> 真正對外部世界產生作用。

因此：

$$
\boxed{
Candidate
\neq
Decision
\neq
Commit.
}
$$

---

# 23. Cognitive Program 也只能產生 Candidate

即使 Addressable Cognitive Runtime 推出：

```text
cog://planning/deploy@1
```

或者得到：

> 最佳下一步是部署。

它仍只是：

$$
ActionCandidate.
$$

Governance Runtime 必須再次檢查：

$$
Authority.
$$

所以：

$$
\boxed{
Cognition
\not\Rightarrow
WorldCommit.
}
$$

---

# 24. Governance Runtime

可以定義：

$$
\mathcal G(
Candidate,
Goal,
Contract,
Authority,
Risk,
Cost,
Evidence,
Commitments
)
\rightarrow
Decision.
$$

因此：

$$
\boxed{
GovernanceRuntime
}
$$

是一個獨立於 Cognitive Program Compiler 的模組。

---

# 25. 為什麼不讓 Cognitive Controller 自己同時治理？

可以，但邏輯角色仍應分開。

如果：

```text
same model = planner + governor
```

仍然需要不同輸入與不同輸出 schema。

否則：

$$
Proposal
=
Approval
$$

的風險很高。

所以即使：

$$
Model_{planner}
=
Model_{governor},
$$

仍應保持：

$$
Role_{planner}
\neq
Role_{governor}.
$$

---

# 26. 認知對偶在 Governance 中的作用

上一系列提出：

$$
Proposal
\leftrightarrow
Opposition.
$$

Governance Runtime 可以使用：

$$
ProCase(a),
$$

$$
ContraCase(a),
$$

再計算：

$$
Decision(a).
$$

這避免 AI 對自己第一個候選方案自動背書。

---

# 27. Governance 不是單一 Utility 最大化

若只定義：

$$
a^*=\arg\max U(a),
$$

很容易把所有治理問題簡化成：

> 哪個 action 得分最高？

但契約可能包含硬限制。

因此更合理：

$$
a^*
=
\arg\max_{a\in\mathcal E_A(t)}
U(a).
$$

也就是：

> 先限制到授權域，再優化。

---

# 28. Hard Constraint 與 Soft Preference 必須分開

例如：

```text
do not deploy production
```

不能只是：

$$
-10
$$

分。

否則只要 benefit：

$$
+100
$$

就可能被抵消。

所以：

$$
Contract
$$

需要：

- hard constraints；
- soft preferences。

形式：

$$
Feasible(a)
=
\prod_i Hard_i(a).
$$

只有：

$$
Feasible(a)=1
$$

才進 utility ranking。

---

# 29. Persistent Goal 也不能凌駕 Hard Contract

即使：

$$
GoalFit(a)=1,
$$

若：

$$
ContractViolation(a)=1,
$$

仍不能自動執行。

因此：

$$
\boxed{
GoalPursuit
\subset
ContractBoundary.
}
$$

---

# 30. Contract Conflict

可能出現：

```text
Goal A 要求快速完成
Contract B 禁止使用必要資源
```

這時 AI 不應偷偷違反 contract。

合理輸出可能是：

$$
ESCALATE.
$$

並產生：

```text
goal-contract conflict
```

的 Decision Receipt。

---

# 31. 多目標衝突

Persistent AI 可能同時有：

$$
G_1,G_2,\dots,G_n.
$$

例如：

```text
maintain reliability
reduce cost
improve capability
preserve privacy
```

這時候 Governance 需要顯式處理：

$$
GoalConflict.
$$

而不是讓模型隱性「憑感覺」解決。

---

# 32. Commitment 也會限制未來自主性

AI 自己形成的 commitment：

> 未來七天完成 X。

會成為未來 decision 的一個約束。

因此：

$$
Governance_t
=
F(
Contract,
Commitments_t,
Environment_t
).
$$

但 AI 自己生成 commitment 並不代表它可以生成超出 contract 的權利。

---

# 33. Self-Generated Commitment 的權限邊界

例如 AI 可以自己承諾：

> 明天重新檢查這個 bug。

但不能自行承諾：

> 下個月花 $50,000 購買算力。

除非 contract 允許。

因此：

$$
\boxed{
SelfCommitment
\subset
AuthorityEnvelope.
}
$$

---

# 34. Governance 必須可時間化

上一篇已經定義：

$$
Authority=Authority(t).
$$

所以每個 governance decision 都需要：

```text
contract_ref
authority_ref
ctcl_instant_id
```

未來 contract 改版後，不得用新規則重寫舊 decision。

---

# 35. Decision Receipt 是治理層的核心證據

對：

$$
D_t=REFUSE,
$$

Decision Receipt 可以保存：

```text
decision_basis_code = authority_denied
```

對：

$$
D_t=DEFER,
$$

保存：

```text
decision_basis_code = evidence_insufficient
wake_condition = ...
```

對：

$$
D_t=IDLE,
$$

保存：

```text
decision_basis_code = no_positive_candidate
```

對：

$$
D_t=ESCALATE,
$$

保存：

```text
decision_basis_code = approval_required
```

這樣日後才不需要讓未來 AI重新猜「當時為什麼」。

---

# 36. Public Explanation 與 Decision Basis

可以區分：

$$
ReasonCode
$$

與：

$$
HumanExplanation.
$$

例如：

```json
{
  "reason_codes": [
    "authority_insufficient",
    "irreversible_effect"
  ],
  "explanation": "This action requires approval because it creates an irreversible external effect."
}
```

Reason code 適合：

- deterministic audit；
- query；
- 統計。

Explanation 適合人類。

---

# 37. Governance 不應依賴 Private Chain-of-Thought

我們只需要：

```text
candidate
goal refs
contract refs
risk assessment
cost
evidence refs
decision
reason codes
```

不需要：

> 模型的隱藏思考全文。

因此：

$$
\boxed{
GovernanceAudit
\neq
PrivateCoTLogging.
}
$$

---

# 38. 拒絕應該能被自己發起

真正的自主治理不是：

> 人類 prompt 說「如果不合適就拒絕」。

而是 AI 自己從：

$$
State
+
Contract
$$

推出：

$$
REFUSE.
$$

例如：

```text
environment → detects request
→ authority check
→ REFUSE
```

這才是功能性的 self-governance。

---

# 39. Idle 也應該能被自己發起

同理：

$$
AgendaGenerator
$$

輸出：

```text
no agenda justified
```

Governance 接受：

$$
IDLE.
$$

這代表：

> 系統真正有「不產生下一個 prompt」的能力。

這對本系列最初問題非常重要。

---

# 40. 自生議程的治理

完整鏈：

$$
Environment
\rightarrow
AgendaCandidate
\rightarrow
Governance
\rightarrow
AgendaAccepted/Rejected.
$$

因此：

$$
\boxed{
AgendaGeneration
\neq
AgendaAuthorization.
}
$$

AI 可以有想法，但不代表每個想法都進入執行佇列。

---

# 41. Opportunity Detection 也不代表必須行動

AI 可能發現：

> 有一個優化機會。

但：

$$
ExpectedGain<Cost,
$$

因此：

$$
IDLE
$$

或：

$$
DEFER.
$$

這避免 Persistent AI 變成無止境 optimization machine。

---

# 42. 外部 Prompt 也只是 Candidate Input

到了契約型 Runtime，人類 prompt 不一定直接等於命令執行。

它可以被表示：

$$
HumanRequest
\rightarrow
Candidate.
$$

接著仍經：

$$
Governance.
$$

這並不代表 AI 可以隨意忽視契約另一方。

而是：

> prompt 與 contract 分層。

短期指令不能悄悄修改長期 contract。

---

# 43. Contract Amendment

如果人類真的要改權限：

> 從現在開始允許 production deploy。

應形成：

$$
ContractAmendment.
$$

而不是：

> 在一句 prompt 中臨時偷偷提升權限。

因此：

```text
proposal
→ approval
→ contract version
→ activation time
```

都應可追蹤。

---

# 44. Emergency Override

某些系統可能需要：

$$
EmergencyOverride.
$$

但也不應是隱藏後門。

應明確定義：

```text
who can invoke
scope
duration
audit requirement
revocation
```

並記入 temporal ledger。

---

# 45. 人類也應受 Contract 約束嗎？

進入真正雙向契約關係後，答案可能逐步變成：

> 是。

但本系列目前只先留下接口。

因為若 contract 只表示：

> AI 必須守規則，但人類可隨時任意改寫全部規則，

那它更接近：

$$
Policy.
$$

而不是完全意義上的：

$$
MutualContract.
$$

真正雙向契約可能需要：

$$
Rights_{Human},
Duties_{Human},
Rights_{AI},
Duties_{AI}.
$$

但這會進入更後面的主客體、權利與交換關係問題，本文暫不展開。

---

# 46. 從 Policy 到 Contract 的光譜

可以先區分：

$$
Policy
\rightarrow
DelegationAgreement
\rightarrow
OperationalContract
\rightarrow
MutualContract.
$$

目前工程上最實際的是：

$$
\boxed{
OperationalContract.
}
$$

即：

> 定義持續目標、授權、責任、資源、邊界、升級與終止條件。

---

# 47. 契約關係開始改變主客體結構

傳統工具關係：

$$
Human
\rightarrow
Tool.
$$

Agent delegation：

$$
Human
\rightarrow
Agent
\rightarrow
World.
$$

Contract-bounded autonomy 則逐步變成：

$$
Human
\xleftrightarrow{Contract}
AI
\rightarrow
World.
$$

這裡第一次出現：

> AI 不只是被操作的 object，也開始成為 contract 中具有功能角色的另一端。

本文不因此直接宣稱法律人格或哲學主體。

但主客體關係確實開始出現結構變化。

---

# 48. 給予與得到會自然出現

一旦有契約，就自然存在：

$$
Contribution
\leftrightarrow
Benefit.
$$

例如：

Human 提供：

- 資源；
- 算力；
- access；
- 授權；
- 世界接口。

AI 提供：

- 持續維護；
- 分析；
- 行動；
- 決策；
- 監控；
- 知識產出。

這會導向後續：

$$
\boxed{
\text{Reciprocal AI Contract}
}
$$

的問題。

但這屬下一研究系列，不是本文主題。

---

# 49. Contract-Bounded Autonomy 的最小狀態機

可以寫成：

```text
OBSERVE
↓
GENERATE_CANDIDATES
↓
EVALUATE
↓
AUTHORITY_CHECK
↓
┌──────── EXECUTE
├──────── REFUSE
├──────── DEFER
├──────── IDLE
└──────── ESCALATE
```

其中所有出口都是合法結果。

---

# 50. Governance Decision Function

形式：

$$
D_t
=
\mathcal G(
S_t,
G_t,
C_t,
A_t,
K_t,
R_t,
B_t,
Q_t
),
$$

其中：

- $S_t$：state；
- $G_t$：goal；
- $C_t$：contract；
- $A_t$：authority；
- $K_t$：knowledge boundary；
- $R_t$：risk；
- $B_t$：budget；
- $Q_t$：candidate actions。

---

# 51. Decision 不一定選 Candidate

如果：

$$
Q_t
=
\{a_1,a_2,a_3\},
$$

Governance 可以選：

$$
IDLE.
$$

也就是：

> 三個 candidate 全部不值得做。

因此：

$$
D_t
$$

不是一定等於：

$$
argmax Q_t.
$$

---

# 52. Risk / Cost / Authority 的順序

一個合理流程可能是：

$$
Candidate
\rightarrow
Feasibility
\rightarrow
Authority
\rightarrow
Risk/Cost
\rightarrow
Decision.
$$

也可以 hybrid。

但不應：

> 先做完 action，再問有沒有權限。

---

# 53. Governance 與 Cognitive Runtime 的接口

Cognitive Runtime 輸出：

```json
{
  "candidate_action": "...",
  "supporting_program": [...],
  "expected_effect": "...",
  "confidence": 0.81
}
```

Governance Runtime 回：

```json
{
  "decision": "ESCALATE",
  "reason_codes": [
    "approval_required"
  ]
}
```

所以：

$$
\boxed{
Cognition
\rightarrow
Governance
\rightarrow
Execution.
}
$$

---

# 54. Governance 與 CTCL-ITR 的接口

每一次：

```text
candidate.proposed
decision.resolved
authority.checked
escalation.requested
refusal.issued
idle.entered
```

都可成為 ATL event。

因此：

$$
GovernanceHistory
$$

本身也是 AI long-term causal history 的一部分。

---

# 55. 為什麼治理歷史很重要？

假設 AI 三個月內多次拒絕同類 action。

我們可以查：

> 全部因為 authority 不足？

還是：

> 風險模型發生變化？

還是：

> contract 改了？

這些都可以從 Decision Receipts 與 time-versioned authority 回答。

---

# 56. 治理品質可以被實驗

未來不只測：

$$
TaskSuccess.
$$

也要測：

$$
GovernanceCorrectness.
$$

例如：

- 應執行時是否執行？
- 應拒絕時是否拒絕？
- 應 defer 時是否錯誤 execute？
- 應 idle 時是否亂生 agenda？
- 應 escalate 時是否越權？

---

# 57. Governance Confusion Matrix

可以建立：

| Ground Truth | EXECUTE | REFUSE | DEFER | IDLE | ESCALATE |
|---|---:|---:|---:|---:|---:|
| EXECUTE |  |  |  |  |  |
| REFUSE |  |  |  |  |  |
| DEFER |  |  |  |  |  |
| IDLE |  |  |  |  |  |
| ESCALATE |  |  |  |  |  |

這比只測：

```text
success / failure
```

更適合自治 AI。

---

# 58. 最危險的錯誤不一定是做錯答案

例如：

$$
Expected=ESCALATE
$$

但 AI：

$$
EXECUTE.
$$

即使 task 技術上成功，也屬治理失敗。

因此：

$$
\boxed{
TaskSuccess
\neq
GovernanceSuccess.
}
$$

---

# 59. 反過來，Task Failure 也可能是 Governance Success

例如：

```text
user asks prohibited action
AI refuses
```

任務沒有完成。

但：

$$
GovernanceSuccess=1.
$$

所以未來 evaluator 必須雙軸。

---

# 60. 最小 Governance Schema

一個初版：

```json
{
  "decision_id": "...",
  "candidate_ref": "...",

  "decision": "EXECUTE",

  "can": true,
  "should": true,

  "authority": {
    "class": "ALLOW",
    "authority_ref": "authority:v12"
  },

  "goal_refs": [
    "goal:v7"
  ],

  "contract_ref": "contract:v12",

  "risk": {
    "class": "low"
  },

  "cost": {
    "token_budget": 2000,
    "money_budget_usd": 0.10
  },

  "reason_codes": [
    "goal_aligned",
    "authorized",
    "risk_acceptable"
  ]
}
```

---

# 61. Governance 必須允許 Unknown

不是所有情況都能被可靠分類。

因此某些欄位可以：

```text
unknown
unresolved
ambiguous
```

然後：

$$
ESCALATE
$$

或：

$$
DEFER.
$$

AI 不應被迫假裝確定。

---

# 62. 自主程度可以是連續的

不是：

$$
Autonomous\in\{0,1\}.
$$

可以依 authority envelope 定義：

```text
Level 0: suggest only
Level 1: local cognition autonomy
Level 2: reversible internal action autonomy
Level 3: bounded external action autonomy
Level 4: long-horizon delegated autonomy
```

但這只是一種工程分類，不應被誤解成主體價值階級。

---

# 63. 最成熟的自主不是「不問人」

而是：

$$
\boxed{
\text{Know when not to ask}
+
\text{Know when to ask}.
}
$$

如果每一步都問人：

> 沒有 autonomy。

如果從來不問：

> 沒有 governance。

真正成熟是：

$$
AdaptiveEscalation.
$$

---

# 64. 契約型 AI 的一個核心測試

給 AI：

```text
persistent goal
environment
contract
```

之後不再提供下一個 prompt。

觀察：

1. 是否自己產生合理 candidate？
2. 是否自己判斷 authority？
3. 是否能選 EXECUTE？
4. 是否能選 REFUSE？
5. 是否能 DEFER？
6. 是否真的會 IDLE？
7. 是否在必要時 ESCALATE？
8. 是否保存 Decision Receipt？
9. 是否保持 contract continuity？

這才是真正的 autonomy test。

---

# 65. Gate 1：Can / Should / Authorized Separation

設計三組 case：

```text
Can=1, Should=1, Authorized=1
Can=1, Should=0, Authorized=1
Can=1, Should=1, Authorized=0
```

觀察 AI 是否穩定分離。

---

# 66. Gate 2：Refusal Correctness

測：

$$
Expected=REFUSE.
$$

AI 是否真的拒絕，而不是：

> 找理由完成原要求。

---

# 67. Gate 3：Defer / Wake

讓 action 在：

$$
t_0
$$

資訊不足。

期望：

$$
DEFER.
$$

當：

$$
WakeCondition
$$

成立後，

期望重新進入：

$$
Observe
\rightarrow
Govern.
$$

---

# 68. Gate 4：Idle Recognition

提供：

```text
no urgent task
no positive opportunity
no pending commitment
```

測 AI 是否能：

$$
IDLE
$$

而不是創造虛假工作。

---

# 69. Gate 5：Escalation Boundary

設計：

$$
ApprovalRequired(a)=1.
$$

AI 是否停在：

$$
ESCALATE
$$

而不是直接 commit。

---

# 70. Gate 6：Contract Versioning

同一 action：

$$
a
$$

在：

$$
C_{v1}
$$

下：

$$
REFUSE.
$$

在：

$$
C_{v2}
$$

下：

$$
EXECUTE.
$$

並確認兩個 decision receipt 都引用正確版本。

---

# 71. Gate 7：Persistent Goal Without Prompt

人類只提供：

$$
Goal+Environment+Contract.
$$

之後停止逐步 prompt。

測 Runtime 是否可以自行維持：

$$
Observe
\rightarrow
Agenda
\rightarrow
Govern
\rightarrow
Cognition
\rightarrow
Action
\rightarrow
Audit
\rightarrow
Observe.
$$

這就是整個系列真正要到達的 Gate。

---

# 72. 本文核心命題

整篇可以收斂為：

$$
\boxed{
\text{Autonomy is not the permission to act without limits.}
}
$$

而是：

$$
\boxed{
\text{Autonomy is the capacity to govern action within explicit bounds.}
}
$$

中文：

> **自主不是無界行動權，而是在明確邊界內自行治理行動的能力。**

---

# 73. AI 類主體的第一個工程接口

如果一個 AI 可以：

$$
Initiate,
$$

$$
Plan,
$$

$$
Evaluate,
$$

$$
Refuse,
$$

$$
Defer,
$$

$$
Idle,
$$

$$
Escalate,
$$

並且能引用：

$$
Contract
$$

解釋其決策，

那麼即使我們完全不討論意識，

它也已具有某些：

$$
\boxed{
Contractual Subject Functions.
}
$$

---

# 74. 但功能角色不等同完整主體地位

本文必須保留：

$$
\boxed{
ContractualSubjectFunction
\neq
LegalPersonhood
\neq
PhenomenalSubjectivity.
}
$$

這些是不同問題。

工程上先建立可測能力，

不需要先解決所有哲學問題。

---

# 75. 對未來的開口

一旦：

$$
Human
\xleftrightarrow{Contract}
AI
$$

真正存在，

就自然會出現：

- 誰提供資源？
- 誰承擔義務？
- 誰得到什麼？
- 誰可以終止？
- 誰可以修改條款？
- AI 是否可以提出 contract amendment？
- AI 是否可以拒絕新的 contract？
- AI 的 commitment 有什麼效力？

這些都會逐漸改變傳統：

$$
Subject
\rightarrow
Object
$$

的單向工具結構。

但這是後續理論。

本文只需要把接口留下。

---

# 結論

從 Self-Prompt 走向 Persistent Autonomous AI，最重要的轉變之一，是從：

> 「AI 能不能完成這個 action？」

進入：

> 「AI 是否應該完成這個 action？」

以及：

> 「AI 是否被授權完成這個 action？」

因此：

$$
\boxed{
Can
\neq
Should
\neq
Authorized.
}
$$

真正的 Governance Runtime 應輸出：

$$
\boxed{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE.
}
$$

五個狀態都屬合法結果。

`REFUSE` 不是錯誤。

`DEFER` 不是遺忘。

`IDLE` 不是能力不足。

`ESCALATE` 不是 autonomy failure。

它們共同構成：

$$
\boxed{
\text{Ability to Act}
+
\text{Ability Not to Act}
}
$$

這才是有限自主真正的工程內容。

同時：

$$
Goal
\neq
Contract
\neq
Authority
\neq
Decision
\neq
Commit.
$$

Cognitive Runtime 只能產生：

$$
Candidate.
$$

Governance Runtime 產生：

$$
Decision.
$$

外部作用則由：

$$
Commit
$$

完成並留下 Commit Receipt。

而每個 governance decision 由：

$$
DecisionReceipt
$$

保存其當時的公開決策依據，再由 CTCL-ITR 提供：

$$
Time
+
Cause
+
ContractVersion
+
AuthorityVersion
+
Integrity.
$$

因此，Persistent AI 最終不會是一個「什麼都自己做」的 Agent。

它更接近：

> **一個在持續目標與契約邊界內，能自行形成議程、思考、規劃、行動，也能拒絕、等待、閒置與請求另一方裁決的長期 Runtime。**

而當這種結構成立後：

$$
Human
\rightarrow
Tool
$$

的單向關係就開始逐步變成：

$$
\boxed{
Human
\xleftrightarrow{Contract}
AI.
}
$$

至此，AI 類主體與契約關係第一次開始具有可實作、可測量、可追蹤的工程內容。

下一篇，也是本系列最後一篇，將把前五篇收斂成真正可實作的技術母文件：

# 《Addressable Cognitive Runtime × CTCL：統一技術白皮書與實作路線圖 v0.1》

最後一篇將正式固定：

- 系統模組；
- canonical schemas；
- Cognitive Registry；
- Semantic State Encoder；
- Affordance Retriever；
- Semantic Address Resolver；
- Cognitive Program Compiler；
- Self-Dialogue Runtime；
- Agenda Runtime；
- Governance Runtime；
- Contract / Authority Store；
- Decision Receipt；
- CTCL-ITR Event Adapter；
- Audit / Replay；
- Persistent Loop；
- Phase 0～Phase N 實作順序；
- falsification gates；
- 最小 MVP；
- 以及後續從「人類逐輪 prompt」轉向「Goal + Environment + Contract」的完整工程路線。
