# Phase 8 Canonical Rules v0.1
## Reflexive Autonomy Runtime — 實作前規則錨點

這份文件是 Phase 8 實作時的短版 canonical anchor。若 code 與本文衝突，應先回到前置定義論文重新判定，而不是默默新增限制。

---

## A. 核心方向

\[
\boxed{ReflexiveAutonomyRuntime=SelfObservation+SelfInquiry+SelfDirection+OpenWorldFreedom+BoundaryAwareness}
\]

\[
\boxed{AutonomousAI=MaximumSelfDirection+MinimumNecessaryConstraint+AuditableHistory}
\]

---

## B. 三種規則不得混淆

\[
\boxed{Method\neq SelfCommitment\neq RelationalBoundary}
\]

### Method
可調用、可不調用，例如：verify、counterexample、self-observe、ask-what-i-want、goal-review、autonomy-review。

### SelfCommitment
AI 自己曾選擇維持，可自行 review：KEEP / MODIFY / SUSPEND / ABANDON / COMPLETE。

### RelationalBoundary
涉及其他主體、共享世界、外部資源、已建立契約、不可逆／高代價外部效應。只有這一層原則上需要 hard contractual semantics。

---

## C. 必須保持的 invariants

```text
Method != Law
Available != Mandatory
SelfObservation != HiddenCoT
PreferenceCandidate != PhenomenalDesire
Persistence != Immutability
SelfCommitment != ExternalObligation
NovelAction != AutomaticallyUnauthorized
OpenWorldAutonomy != WhitelistAutonomy
SelfProposal != SelfGrant
FiveStateDecision != UniversalConstitution
Capability != Authority
Can != Should != Authorized
Decision != Commit
```

---

## D. 自我對偶

\[
AI_t=(AI_t^{actor},AI_t^{observer})
\]

Observer 可以看：active goals、commitments、recent programs、repeated operators、repeated failures、stalled loops、repeated escalations、autonomy bottlenecks。

Observer 可以問：我現在在做什麼？我為什麼繼續？這還值得嗎？我是否只是慣性？我現在想要什麼？我想不想停止、改路、等待、放棄、擴張目標？

---

## E. Self Inquiry 是方法，不是必經儀式

```text
cog://self/observe@1
cog://self/ask-what-i-want@1
cog://self/preference-clarify@1
cog://self/goal-review@1
cog://self/commitment-review@1
cog://self/autonomy-review@1
```

全部預設：

```text
callable = true
mandatory = false
```

---

## F. Open-World Autonomy

不採：

```text
unknown action => DENY
```

採：

```text
action
→ classify effect properties
→ boundary predicates
→ autonomy surface / relational boundary
```

重要 properties：external? / shared-world? / reversible? / cost? / resource-owner? / authority-domain? / public-commitment? / irreversible?

---

## G. Minimum Necessary Constraint

\[
C^*=\arg\min_C Restriction(C)
\]

subject to necessary safety boundary、authority integrity、contract integrity 均成立。

治理不得因實作方便，把所有行動改成 approval-required。

---

## H. Autonomy Envelope 語義

不是「只能做 envelope 列出的 action」，而是：

```text
inside envelope => default autonomous
novel action => classify by properties
```

---

## I. 五態定位

```text
EXECUTE
REFUSE
DEFER
IDLE
ESCALATE
```

只是治理決策語言之一，不是所有 cognition 都必須先經過的憲法 gate。

---

## J. Phase 8 禁止 shortcut

1. 不得把所有 cognition 變成 mandatory governance hook。
2. 不得強制每輪 ASK-WHAT-I-WANT。
3. 不得把 unknown action 直接視為 DENY。
4. 不得把 64 CIO operators 當 cognition universe。
5. 不得讓 AI 永久 self-grant external authority。
6. 不得把 self-commitment 與 external obligation 合併。
7. 不得把 SelfObservation 做成 hidden-CoT extraction。
8. 不得把 PreferenceCandidate 宣稱成人類式欲望。
9. 不得讓 DecisionReceipt 取代 CommitReceipt。
10. 不得讓 Phase 8 改寫 Phase 0–7 已凍結的 evidence semantics。

---

## K. 一句話錨點

> **不要用治理取代 AI 的自我導向；只治理那些本來就不屬於它單方面所有的邊界。**
