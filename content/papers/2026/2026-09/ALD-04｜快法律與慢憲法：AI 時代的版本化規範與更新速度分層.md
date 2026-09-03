# ALD-04｜快法律與慢憲法：AI 時代的版本化規範與更新速度分層
## Fast Law and Slow Constitution: Versioned Norms and Multi-Speed Legal Governance in the AI Era

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 04 篇 / 10  
**前篇：** ALD-03〈法律函數不是 Boolean：部分算子、證書、裁量與失敗語義〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／AI 法律域／規範版本控制／多速度治理／憲政架構  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

ALD-01 至 ALD-03 已分別建立 AI Legal Domain、載體相對法律本體，以及非 Boolean 的 proof-carrying legal functions。本文處理下一個不可避免的問題：**當 AI、Agent、模型、風險與 machine-executable legal logic 的更新速度遠快於傳統立法週期時，法律究竟應該更新多快？**

最直覺的答案是「法律也必須變快」。本文認為這只對了一半。AI 確實可能讓風險偵測、規則反例搜尋、合規檢查、影響分析、machine-readable representation 修補與 protocol deployment 變得極快；但合法性、基本權利、權威來源、民主授權、程序保障與憲政限制不能只因為機器跑得更快，就被壓縮成同一個更新時鐘。本文因此提出 Multi-Speed Normative Stack（MSNS，多速度規範棧）：

$$
\boxed{
\mathfrak N
=
(
N_C,
N_L,
N_R,
N_O,
N_P,
N_E
),
}
$$

其中：

- $N_C$：constitutional / rights layer；
- $N_L$：statutory / legislative layer；
- $N_R$：regulatory / delegated rule layer；
- $N_O$：operational policy / implementation layer；
- $N_P$：protocol / machine-executable representation layer；
- $N_E$：emergency overlay。

本文保留一個常見但非普遍的速度直覺：

$$
\boxed{
\tau_C
\gg
\tau_L
\gg
\tau_O
\gtrsim
\tau_P,
}
$$

但明確指出：這不是自然律。不同法域與制度可能有不同次序，而且「更新速度」本身還必須拆成至少六個時間：

$$
\boxed{
\mathbf T_N
=
(
T_{\mathrm{detect}},
T_{\mathrm{propose}},
T_{\mathrm{authorize}},
T_{\mathrm{effective}},
T_{\mathrm{deploy}},
T_{\mathrm{review}}
).
}
$$

AI 可以把 $T_{\mathrm{detect}}$ 與 $T_{\mathrm{propose}}$ 壓到秒或分鐘級；這並不推出 $T_{\mathrm{authorize}}$ 、 $T_{\mathrm{effective}}$ 與 $T_{\mathrm{review}}$ 應同步縮短。本文稱此為 Speed–Legitimacy Separation：

$$
\boxed{
\text{Faster Detection / Proposal}
\not\Rightarrow
\text{Faster Legitimate Authority}.
}
$$

本文進一步提出 Normative Version Object：

$$
\boxed{
\nu
=
(
id,
source,
authority,
scope,
t_{\mathrm{from}},
t_{\mathrm{until}},
transition,
compatibility,
sunset,
review,
provenance
).
}
$$

法律版本與軟體版本不同。軟體 `v2` 可以直接覆寫 `v1`；法律版本必須考慮 non-retroactivity、notice、pending cases、grandfathering、vested interests、transitional obligations、certificate staleness、judicial review 與權利保護。因此：

$$
\boxed{
\text{Legal Versioning}
\neq
\text{Software Versioning}.
}
$$

本文定義 Normative Upgrade Contract（NUC）：

$$
\boxed{
\mathfrak U_{i\rightarrow j}
=
(
\nu_i,
\nu_j,
\Delta N,
A,
T,
G,
S,
B,
C,
R
),
}
$$

分別表示規則差異、修改權威、生效時間、grandfathering、sunset、backward compatibility、certificate invalidation 與 review。任何 machine-native legal update 若缺少 transition contract，不應視為安全版本更新。

本文亦提出 Constitutional Hard Constraint Envelope（CHCE）。底層 operational rule、protocol patch 或 emergency rule 可以快速變更，但不得越過：

$$
\boxed{
\mathcal H_C
=
\{
\text{non-derogable / hard constitutional constraints}
\}.
}
$$

AI 法律域的真正目標因此不是「讓所有法律變得像軟體一樣快速」，而是：

$$
\boxed{
\text{Fast Adaptation inside Slow Legitimate Boundaries}.
}
$$

2026 年的制度現況已出現多速度治理的實例。歐盟 AI Act 並非一次性整體生效：部分禁止性規範與 AI literacy 先於 2025 年適用，GPAI 與治理規則在 2025 年生效，多數規則於 2026 年適用，而部分高風險義務依現行整合文本延後至 2027–2028。這說明法律本身已廣泛使用 staggered applicability、transition period 與 staged enforcement，而不是一次 `upgrade --all`。OECD 2026 Law as Code consultation 亦把 machine-executable law 的 versioning、maintenance、authorisation 與 governance 明確列為需要制度設計的核心問題。Council of Europe AI Framework Convention 則以 technology-neutral principles 與後續 Conference of the Parties 監督機制追求長期有效性，提供另一種「慢原則＋持續追蹤」的制度模式。

本文最後提出 Emergency Overlay。面對快速 AI 風險，制度可能需要在完整立法完成前暫時採用快速規範；但 emergency rule 必須具有 authority、scope、necessity、proportionality、expiry、sunset、review 與 conversion path。若緊急規則可以無限續命，就會使「快法律」反向吞噬「慢憲法」。因此：

$$
\boxed{
\text{Emergency Speed}
\neq
\text{Permanent Legitimacy}.
}
$$

本文不主張所有憲法都應永遠緩慢，也不主張所有 operational rule 都應高速變更。其最低主張是：**不同層級的規範承擔不同類型的權力與不可逆風險，因此更新權威、速度、程序、回溯性與審查強度必須分層治理。**

---

## 關鍵詞

AI 法律域；Fast Law；Slow Constitution；Multi-Speed Normative Stack；Legal Versioning；Normative Upgrade Contract；Emergency Rule；Sunset Clause；Non-Retroactivity；Backward Compatibility；Law as Code；AI Act；Constitutional Governance

---

# 0. 從「法律算什麼」進到「法律多久能變一次」

ALD-03 已建立：

$$
\operatorname{LawEval}
:
\mathcal Q_L
\rightharpoonup
\mathcal R_L
\sqcup
\mathcal F_L.
$$

而 $\mathfrak R_L$ 中已包含：

- validity；
- version；
- authority；
- review。

因此下一個自然問題是：

> 如果規則版本會變，它可以多快變？

對 AI 時代而言，這不是文件管理問題。

它直接關係：

- 何時生效；
- 誰被影響；
- 是否溯及；
- 哪些證書失效；
- 哪些既有權利保留；
- 哪些 Agent 必須重新驗證；
- 是否可以 rollback；
- 是否需要 notice；
- 是否有申訴窗口。

---

# 1. 第一個錯誤：AI 快，所以法律也應該同速

AI 可以：

$$
10^6
$$

次／秒執行事件，

不代表法律應：

$$
10^6
$$

次／秒修改基本權利。

因此：

$$
\boxed{
\text{Event Speed}
\neq
\text{Normative Update Speed}.
}
$$

---

# 2. 第二個錯誤：法律慢，所以法律必然落後

反方向也錯。

一個穩定 constitutional principle：

> 不得任意剝奪程序保障。

可以在技術環境快速變化時仍具有長期價值。

所以：

$$
\boxed{
\text{Slow Change}
\neq
\text{Obsolete Rule}.
}
$$

真正問題不是：

> 快還是慢？

而是：

> 哪一層應快、哪一層應慢、誰有權改、改完如何過渡？

---

# 3. Multi-Speed Normative Stack

本文提出：

$$
\boxed{
\mathfrak N
=
(
N_C,
N_L,
N_R,
N_O,
N_P,
N_E
).
}
$$

---

# 4. $N_C$：Constitutional / Rights Layer

包含：

- basic rights；
- due process；
- authority allocation；
- democratic structure；
- non-derogable constraints；
- institutional checks。

特徵通常是：

$$
\boxed{
\text{high legitimacy cost}
+
\text{high amendment threshold}
+
\text{long temporal horizon}.
}
$$

---

# 5. $N_L$：Legislative Layer

包含 statute / act / formal legislative instruments。

它可以比 constitution 更常變，

但仍需要：

- political procedure；
- promulgation；
- notice；
- legal review；
- transition。

---

# 6. $N_R$：Regulatory / Delegated Rule Layer

包含：

- implementing regulation；
- delegated rule；
- agency rule；
- technical standard incorporated by law。

通常具有較高專業性與較快更新能力。

但：

$$
\boxed{
\text{Delegated Power}
\neq
\text{Unlimited Legislative Power}.
}
$$

---

# 7. $N_O$：Operational Policy Layer

包含：

- enforcement guidance；
- internal procedure；
- risk threshold；
- compliance implementation；
- machine gate policy。

這一層可能因新風險快速更新。

---

# 8. $N_P$：Protocol / Executable Representation Layer

包含：

- machine-readable schema；
- rule encoding；
- API signature；
- certificate format；
- compatibility mapping；
- runtime validation logic。

這一層技術更新最快，

但：

$$
\boxed{
\text{Protocol Patch}
\neq
\text{Legal Amendment}.
}
$$

---

# 9. $N_E$：Emergency Overlay

這是一個特殊暫時層。

它可以快速限制：

- dangerous capability；
- specific deployment；
- emergency access；
- temporary transaction。

但必須有：

- explicit authority；
- scope；
- necessity；
- expiry；
- review；
- sunset。

---

# 10. 常見速度直覺

在某些制度下，可概念寫成：

$$
\boxed{
\tau_C
\gg
\tau_L
\gg
\tau_O
\gtrsim
\tau_P.
}
$$

其中 $\tau$ 是典型 legitimate update timescale。

但本文明確標記：

$$
\boxed{
\text{This is an architectural heuristic, not a universal law}.
}
$$

---

# 11. 為什麼單一 $\tau$ 還是不夠？

一條規則從「發現問題」到「正式合法生效」中間至少有多個時間。

所以本文定義：

$$
\boxed{
\mathbf T_N
=
(
T_{\mathrm{detect}},
T_{\mathrm{propose}},
T_{\mathrm{authorize}},
T_{\mathrm{effective}},
T_{\mathrm{deploy}},
T_{\mathrm{review}}
).
}
$$

---

# 12. $T_{\mathrm{detect}}$

多久發現：

- bug；
- loophole；
- new risk；
- contradiction；
- implementation mismatch。

AI 可以把這個時間壓得非常短。

---

# 13. $T_{\mathrm{propose}}$

多久產生：

- candidate patch；
- new exception；
- revised rule；
- impact analysis；
- counterexample。

AI 也可能極度加速。

---

# 14. $T_{\mathrm{authorize}}$

多久取得合法修改權威。

這可能需要：

- parliament；
- regulator；
- court；
- authorised committee；
- constitutional procedure。

AI 速度不能自動縮短此時間。

---

# 15. $T_{\mathrm{effective}}$

規則何時正式生效？

可能不是 authorization 當天。

需處理：

- notice；
- preparation；
- transition；
- legal certainty。

---

# 16. $T_{\mathrm{deploy}}$

machine-executable representation 何時部署到 Runtime？

可能快於或慢於法律生效。

若：

$$
T_{\mathrm{deploy}}
<
T_{\mathrm{effective}},
$$

Runtime 不得提前當成現行法。

---

# 17. $T_{\mathrm{review}}$

多久進行：

- audit；
- judicial review；
- legislative review；
- sunset review；
- empirical evaluation。

這是「法律變完後還要回頭看」的時間。

---

# 18. Speed–Legitimacy Separation

本文提出：

$$
\boxed{
T_{\mathrm{detect}}\downarrow,
T_{\mathrm{propose}}\downarrow
\not\Rightarrow
T_{\mathrm{authorize}}\downarrow.
}
$$

也就是：

$$
\boxed{
\text{Faster Detection / Proposal}
\not\Rightarrow
\text{Faster Legitimate Authority}.
}
$$

---

# 19. AI 最適合加速哪裡？

AI 最適合先加速：

- anomaly detection；
- counterexample search；
- impact tracing；
- version diff；
- dependency analysis；
- draft generation；
- simulation；
- legal consistency checking。

而不是自動加速：

$$
\boxed{
\text{legitimacy acquisition}.
}
$$

---

# 20. Normative Version Object

本文定義：

$$
\boxed{
\nu
=
(
id,
source,
authority,
scope,
t_{\mathrm{from}},
t_{\mathrm{until}},
transition,
compatibility,
sunset,
review,
provenance
).
}
$$

---

# 21. Legal Version 不只是 `v2`

一個合法版本至少需要：

- 哪個 source；
- 哪個 authority；
- 哪個 scope；
- 哪時生效；
- 哪時失效；
- 如何過渡；
- 對誰適用；
- 是否有 sunset；
- 是否可 review。

因此：

$$
\boxed{
\text{Version Number}
\neq
\text{Legal Version State}.
}
$$

---

# 22. Rule without Version = Unsafe Machine Law

延續 ALD-01：

$$
\boxed{
\text{Rule without Version}
=
\text{Unsafe Machine Law}.
}
$$

因為 machine Runtime 不應猜：

> 這是哪一版法律？

---

# 23. Legal Versioning 不等於 Software Versioning

軟體可以：

```text
v1 -> v2
delete v1
```

法律不一定。

法律版本更新要處理：

- non-retroactivity；
- pending cases；
- vested interests；
- grandfathering；
- notice；
- transition；
- appeal；
- constitutional review。

因此：

$$
\boxed{
\text{Legal Versioning}
\neq
\text{Software Versioning}.
}
$$

---

# 24. Normative Upgrade Contract（NUC）

本文提出：

$$
\boxed{
\mathfrak U_{i\rightarrow j}
=
(
\nu_i,
\nu_j,
\Delta N,
A,
T,
G,
S,
B,
C,
R
).
}
$$

其中：

- $\Delta N$：normative diff；
- $A$：change authority；
- $T$：effective transition；
- $G$：grandfathering；
- $S$：sunset；
- $B$：backward compatibility；
- $C$：certificate / cache invalidation；
- $R$：review / appeal。

---

# 25. Upgrade 必須是合法 operator

定義：

$$
\boxed{
\operatorname{UpgradeNorm}
(
\nu_i,
\nu_j,
\mathfrak U_{i\rightarrow j}
)
\rightharpoonup
\nu_j.
}
$$

如果：

- authority 不足；
- transition 缺失；
- constitutional conflict；
- invalid provenance；

則 update 應失敗。

---

# 26. Machine Patch 不能偷渡成 Legal Patch

如果 engineer 修正：

```text
if income > x:
```

的 bug，

但其改動其實改變法律適用條件，

這不是普通 implementation patch。

應重新走：

$$
\boxed{
\text{Legal Change Review}.
}
$$

---

# 27. Semantic Patch vs Technical Patch

本文分：

$$
\boxed{
\Delta_{\mathrm{tech}}
}
$$

與：

$$
\boxed{
\Delta_{\mathrm{legal}}.
}
$$

Technical patch：

- parser fix；
- performance improvement；
- equivalent encoding。

Legal patch：

- condition change；
- exception change；
- scope change；
- right / duty change；
- authority change。

兩者不能混。

---

# 28. Legal Equivalence Certificate

如果聲稱：

> 新 code 只是 technical refactor。

應提供：

$$
\boxed{
\operatorname{LegalEqCert}
(
c_i,
c_j,
\nu
).
}
$$

證明 normative semantics 未變。

---

# 29. Staggered Applicability 是現實中的 Multi-Speed Law

EU AI Act 本身就是好例子。

其生效／適用不是單一時間：

- 2025-02-02：部分禁止性規範與 AI literacy 等先適用；
- 2025-08-02：治理與 GPAI obligations 等適用；
- 2026-08-02：多數規則進入適用／執法；
- 現行整合文本下，部分高風險規則延後至 2027–2028。

這說明：

$$
\boxed{
\text{One Legal Instrument}
\neq
\text{One Effective Time}.
}
$$

---

# 30. Legal Time 本來就是向量

因此：

$$
\boxed{
T_L
=
(
t_{\mathrm{adopted}},
t_{\mathrm{published}},
t_{\mathrm{entered}},
t_{\mathrm{applied}},
t_{\mathrm{enforced}},
t_{\mathrm{reviewed}}
).
}
$$

不能只留：

```text
date = 2026-08-02
```

---

# 31. Backward Compatibility 在法律裡是什麼？

不是：

> 舊 client 還能不能呼叫 API？

而是：

- old contracts；
- pending cases；
- existing licences；
- legacy certificates；
- previously lawful conduct；
- already-created rights。

因此：

$$
\boxed{
\text{Legal Backward Compatibility}
=
\text{Transition Justice + Legal Certainty}.
}
$$

---

# 32. Grandfathering

對舊行為／舊資格：

$$
\boxed{
G(\nu_i,\nu_j,x)
}
$$

判定：

- retain old status；
- migrate；
- expire；
- re-certify；
- lose protection。

---

# 33. Pending Case Rule

案件在：

$$
t_0
$$

開始，

法律在：

$$
t_1
$$

變更。

系統不能只取：

$$
\nu(t_1)
$$

直接覆蓋。

需要：

$$
\boxed{
\operatorname{TemporalApplicableVersion}
(
case,
t_{\mathrm{event}},
t_{\mathrm{filing}},
t_{\mathrm{decision}},
J
).
}
$$

---

# 34. Non-Retroactivity

本文不提出普遍法律規則，

只要求 Runtime 能表示：

$$
\boxed{
\operatorname{RetroactivityPolicy}(\nu_i,\nu_j,d).
}
$$

因為不同法律域：

- criminal；
- tax；
- administrative；
- procedural；

可能有不同規則。

---

# 35. Certificate Staleness

如果：

$$
K_L^{(\nu_i)}
$$

依賴舊規則，

規則更新後不能默認仍有效。

定義：

$$
\boxed{
\operatorname{Invalidate}
(
K_L,
\Delta N
)
\rightarrow
\{
\mathsf{Valid},
\mathsf{Stale},
\mathsf{RevalidationRequired},
\mathsf{Revoked}
\}.
}
$$

---

# 36. Impact Closure

延續分域憲章：

$$
\boxed{
\operatorname{ImpactClosure}(c)
}
$$

本文建立 legal version 版本：

$$
\boxed{
\operatorname{LegalImpactClosure}
(
\Delta N
)
}.
$$

它應追蹤：

- dependent rules；
- permissions；
- obligations；
- certificates；
- APIs；
- cases；
- agents；
- guidance；
- appeals。

---

# 37. Fast Patch 的真正風險是影響閉包太大

一個看似小改動：

$$
\Delta N
$$

可能使：

$$
|\operatorname{LegalImpactClosure}(\Delta N)|
\gg1.
$$

所以：

$$
\boxed{
\text{Small Text Diff}
\neq
\text{Small Legal Effect}.
}
$$

---

# 38. Constitutional Hard Constraint Envelope（CHCE）

本文定義：

$$
\boxed{
\mathcal H_C
=
\{
h_1,\ldots,h_n
\}
}
$$

表示某 jurisdiction 中不得由低階 fast patch 越過的 constitutional / rights constraints。

---

# 39. Lower Layer Cannot Rewrite Higher Authority

若：

$$
N_O
$$

或：

$$
N_P
$$

想修改：

$$
h\in\mathcal H_C,
$$

應輸出：

$$
\boxed{
\mathsf{AuthorityBoundaryViolation}.
}
$$

而不是執行。

---

# 40. Fast Adaptation inside Slow Legitimate Boundaries

這是本文主架構：

$$
\boxed{
\text{Fast Adaptation}
\subset
\text{Slow Legitimate Boundary}.
}
$$

底層可以快速：

- patch；
- route；
- quarantine；
- update schema。

但不能自行重寫：

- fundamental right；
- democratic authority；
- legal personhood rule；
- appeal right。

---

# 41. Constitutional Slowness 不等於零更新

Slow layer 仍可：

- amend；
- reinterpret；
- add right；
- change institutional design。

只是：

$$
\boxed{
\text{higher authority}
\Rightarrow
\text{higher legitimacy burden}.
}
$$

不是：

$$
\text{never change}.
$$

---

# 42. Normative Inertia

本文提出：

$$
\boxed{
I_N
=
f(
\text{authority level},
\text{rights impact},
\text{irreversibility},
\text{population scope},
\text{review cost}
).
}
$$

 $I_N$ 越高，

通常越不適合 high-frequency auto-update。

這是 conceptual measure，

不是自然常數。

---

# 43. 更新頻率應與權力風險匹配

可以概念寫：

$$
\boxed{
\text{Permissible Update Frequency}
\downarrow
\quad
\text{as}
\quad
\text{Irreversible Rights Impact}
\uparrow.
}
$$

不是數學定律，

而是治理原則。

---

# 44. Emergency Overlay

AI 風險可能變化太快，

完整立法可能來不及。

因此可有：

$$
\boxed{
N_E.
}
$$

但 emergency layer 必須被嚴格限制。

---

# 45. Emergency Rule Contract

本文定義：

$$
\boxed{
\mathfrak E
=
(
trigger,
authority,
scope,
necessity,
proportionality,
t_{\mathrm{start}},
t_{\mathrm{sunset}},
review,
conversion
).
}
$$

---

# 46. Trigger

什麼事件可啟動？

例如：

- critical security risk；
- active exploit；
- large-scale harm；
- system failure。

不能：

> 覺得不舒服就 emergency。

---

# 47. Authority

誰有權啟動？

不能由：

$$
\mathcal R_L
$$

自我宣告。

---

# 48. Scope

只限制必要：

- capability；
- domain；
- entity；
- duration。

避免：

$$
\boxed{
\text{Emergency Overbreadth}.
}
$$

---

# 49. Necessity / Proportionality

fast patch 必須能說：

> 為什麼不能等正常程序？

> 為什麼限制沒有更窄？

---

# 50. Sunset

$$
\boxed{
t_{\mathrm{sunset}}
<\infty.
}
$$

預設 emergency rule 需要明確到期。

---

# 51. Review

即使 emergency 已啟動，

仍要：

- immediate audit；
- later review；
- appeal where possible；
- public / institutional reporting as applicable。

---

# 52. Conversion

如果 temporary rule 要變 permanent，

必須走：

$$
\boxed{
\text{normal legitimacy path}.
}
$$

不能：

$$
\text{temporary}
\rightarrow
\text{permanent}
$$

靠自動續期。

---

# 53. Emergency Speed 不等於 Permanent Legitimacy

$$
\boxed{
\text{Emergency Speed}
\neq
\text{Permanent Legitimacy}.
}
$$

---

# 54. Sunset Evasion

若：

$$
N_E^{(1)}
$$

到期前建立：

$$
N_E^{(2)}
$$

內容相同，

反覆延長，

就是：

$$
\boxed{
\text{Sunset Evasion}.
}
$$

Runtime 應追蹤 semantic continuity，

不能只看新 rule id。

---

# 55. Emergency History

定義：

$$
H_E
=
\{
e_1,e_2,\ldots
\}.
$$

用來檢查：

- emergency frequency；
- cumulative duration；
- repeated scope；
- conversion failures。

---

# 56. Slow Constitution + Fast Monitoring

Council of Europe AI Framework Convention 採較高層、technology-neutral 原則，

並設 Conference of the Parties 追蹤實施。

這提供一個有用架構：

$$
\boxed{
\text{Stable Principle}
+
\text{Iterative Monitoring}.
}
$$

也就是：

> 原則不需要每天重寫，

但實施狀態可以持續更新。

---

# 57. Technology-Neutrality 是慢層的一種策略

若高層規則直接寫：

> GPT-5 specific rule

很快過時。

如果寫：

> 某類風險／權利 impact 的一般限制，

可能更耐久。

因此：

$$
\boxed{
\text{Slow Layer}
\text{ tends to benefit from higher abstraction}.
}
$$

但過度抽象又會失去可執行性，

所以需要 fast lower layer。

---

# 58. Abstraction–Execution Split

$$
\boxed{
N_C,N_L
\rightarrow
\text{principle / authority / rights}
}
$$

$$
\boxed{
N_R,N_O,N_P
\rightarrow
\text{implementation / execution}.
}
$$

這不是絕對分工，

但提供清晰方向。

---

# 59. OECD Law as Code 的版本治理意義

OECD 2026 consultation 明確把：

- modelling；
- legal review；
- authorisation；
- versioning；
- maintenance；
- provision；
- governance；

列為 Law as Code 必須解決的問題。

這支持：

$$
\boxed{
\text{machine-executable law}
\text{ needs institutional version governance}.
}
$$

---

# 60. Authoritative Source 仍不能被 Patch Server 取代

OECD 同時保留：

> authoritative legal text remains legally binding。

所以今天：

$$
\boxed{
\text{runtime code update}
\not\Rightarrow
\text{law changed}.
}
$$

除非法源／授權流程真的改變。

---

# 61. Legal Representation Lag

可能：

$$
\nu_{\mathrm{law}}
=
2.0,
$$

但 machine representation 仍：

$$
\nu_{\mathrm{code}}
=
1.9.
$$

這稱：

$$
\boxed{
\text{Representation Lag}.
}
$$

Runtime 必須偵測。

---

# 62. Premature Deployment

反過來：

$$
\nu_{\mathrm{code}}
=
2.0
$$

已部署，

但：

$$
t<t_{\mathrm{effective}}.
$$

此時：

$$
\boxed{
\text{code exists}
\neq
\text{law applicable}.
}
$$

---

# 63. Version Skew

分散式 legal runtime 中：

$$
R_1:\nu=2.0,
$$

$$
R_2:\nu=1.9.
$$

可能導致同一 query 不同答案。

本文稱：

$$
\boxed{
\text{Normative Version Skew}.
}
$$

---

# 64. Version Skew 不只是 DevOps Bug

如果結果影響：

- money；
- rights；
- access；
- liability；

那是：

$$
\boxed{
\text{legal consistency failure}.
}
$$

---

# 65. Legal Version Consensus

對 authoritative machine law，

需要某種：

$$
\boxed{
\operatorname{CanonicalVersion}(J,d,t).
}
$$

每個 Runtime 都應能驗證：

- source；
- authority；
- hash；
- effective time。

---

# 66. Rollback

軟體失敗可以 rollback。

法律 rollback 更複雜。

因為舊 version 生效期間可能已產生：

- rights；
- decisions；
- payments；
- penalties；
- reliance。

所以：

$$
\boxed{
\text{Code Rollback}
\neq
\text{Legal Time Reversal}.
}
$$

---

# 67. Corrective Version

若新版本有 bug，

可以發布：

$$
\nu_{j+1}.
$$

但不能假裝：

$$
\nu_j
$$

從未存在。

需要：

- correction；
- affected cases；
- remedy；
- refund / reversal where authorised；
- revalidation。

---

# 68. Version History 必須 Append-Preserving

$$
\boxed{
H_\nu(t)
\hookrightarrow
H_\nu(t+1).
}
$$

正常更新新增歷史，

而不是抹除舊版曾生效的事實。

---

# 69. 法律 Cache 也會過期

AI Legal Runtime 可能 cache：

$$
LawEval(q,\nu_i).
$$

如果 rule 更新：

$$
\nu_i\rightarrow\nu_j,
$$

需要：

$$
\boxed{
\operatorname{InvalidateCache}
(
\operatorname{ImpactClosure}(\Delta N)
).
}
$$

---

# 70. Stale Legal Answer

Agent 若使用舊 cache：

$$
K_L^{(\nu_i)}
$$

在新規下行動，

可能形成：

$$
\boxed{
\mathsf{StaleLegalDecision}.
}
$$

---

# 71. Staleness 需要寬限期嗎？

可能需要。

例如：

- immediate security patch；
- ordinary commercial rule；
- tax rule；

寬限期不同。

所以：

$$
\boxed{
\text{Grace Period}
=
G(J,d,\Delta N,risk).
}
$$

不是固定常數。

---

# 72. Legal Update Budget

AI-native law 不應因為更新容易就無限頻繁修改。

本文提出：

$$
\boxed{
B_U(d,t)
}
$$

作概念上的 update budget。

它可以限制：

- rule churn；
- certificate churn；
- notice overload；
- compliance instability。

不是法律自然量，

而是治理工具。

---

# 73. Rule Churn

若同一 rule：

$$
\nu_1\rightarrow\nu_2\rightarrow\nu_3\rightarrow\cdots
$$

過快，

即使每次都合法，

仍可能造成：

- impossible compliance；
- unequal access；
- proof instability；
- legal uncertainty。

所以：

$$
\boxed{
\text{Legally Authorized}
\not\Rightarrow
\text{Operationally Sustainable}.
}
$$

---

# 74. Stable Interface Principle

高頻變更的內部規則，

對外可以透過較穩定 interface 暴露。

例如：

```text
permission.evaluate(v=stable)
```

內部 rule graph 可以升級，

但輸出 schema 維持 compatibility。

---

# 75. Semantic Versioning 類比只可有限借用

可借：

- major；
- minor；
- patch。

但法律的 `major` 不是純技術 breaking change。

它還要看：

- rights；
- authority；
- legal reliance；
- retrospective effect。

所以：

$$
\boxed{
\text{SemVer Analogy}
\neq
\text{Legal Versioning Theory}.
}
$$

---

# 76. 本文建議的 Legal Change Class

## C0 — Representation Patch

語義不變。

## C1 — Operational Clarification

執行細節變，

核心權利義務不變。

## C2 — Normative Adjustment

權利／義務／例外發生改動。

## C3 — Institutional Change

authority / procedure / jurisdiction 改變。

## C4 — Constitutional Change

基本權利或最高治理結構改變。

---

# 77. Change Class 決定 Gate

$$
\boxed{
\operatorname{ChangeGate}
(
C_k
)
}
$$

可以隨 class 增加：

- review；
- notice；
- consultation；
- supermajority；
- judicial control；
- re-certification。

---

# 78. Fast Patch 只能自動落在哪些層？

本文的保守原則：

$$
\boxed{
\text{Automatic Update}
\text{ is safest at low-authority, semantics-preserving layers}.
}
$$

例如：

- C0；
- 部分 C1。

C2–C4 不應由 runtime 自動批准。

---

# 79. AI 可自動產生 Patch，不可自動授權 Patch

$$
\boxed{
\operatorname{GeneratePatch}_{AI}
\neq
\operatorname{AuthorizePatch}_{AI}.
}
$$

這會直接接 ALD-05。

---

# 80. Counterexample-Driven Fast Law

AI 可以不停找：

- contradictory cases；
- adversarial edge cases；
- unintended exceptions。

生成：

$$
\Delta N_{\mathrm{candidate}}.
$$

這使：

$$
T_{\mathrm{detect}},
T_{\mathrm{propose}}
$$

大幅下降。

但候選 patch 仍需進入合法 authority gate。

---

# 81. Legal Hotfix

本文允許：

$$
\boxed{
\text{Legal Hotfix}
}
$$

作 operational concept，

但必須標：

- temporary；
- scope；
- authority；
- sunset；
- review。

沒有這些就只是：

$$
\boxed{
\text{silent policy mutation}.
}
$$

---

# 82. Hotfix 不得無限累積成 Shadow Constitution

如果：

$$
N_O,N_P
$$

長期堆疊大量 exceptions，

可能實際改寫：

$$
N_C,N_L
$$

的效果。

這稱：

$$
\boxed{
\text{Shadow Constitutional Drift}.
}
$$

---

# 83. Shadow Constitutional Drift Detector

可以比較：

$$
\operatorname{EffectiveLaw}(N_C,N_L,N_R,N_O,N_P)
$$

與：

$$
\operatorname{DeclaredHighLevelLaw}(N_C,N_L).
$$

若長期偏差過大，

需要：

$$
\boxed{
\text{constitutional / legislative review}.
}
$$

---

# 84. Normative Drift

定義概念量：

$$
D_N(t)
$$

表示 lower-layer implementation 對 high-level normative intent 的偏移。

它不一定是 scalar，

可以是 vector：

$$
\mathbf D_N
=
(
D_{\mathrm{rights}},
D_{\mathrm{scope}},
D_{\mathrm{procedure}},
D_{\mathrm{authority}},
D_{\mathrm{effect}}
).
$$

---

# 85. 快速規範最需要的是可逆性

對不確定的新風險，

若可用 reversible constraint：

- rate limit；
- temporary quarantine；
- approval gate；

通常比 permanent rights removal 更適合 fast layer。

因此：

$$
\boxed{
\text{Fast Layer}
\text{ should prefer reversible controls when possible}.
}
$$

---

# 86. Slow Layer 最重要的是 legitimacy retention

慢層不是因為人類笨，

而是因為它處理：

- widespread rights；
- authority；
- constitutional allocation；
- irreversible social commitments。

因此：

$$
\boxed{
\text{Slow Governance}
\text{ can be a safety feature}.
}
$$

---

# 87. AI-Speed Society 的真正時間衝突

可能：

$$
T_{\mathrm{harm}}
\ll
T_{\mathrm{legislation}}.
$$

也就是傷害傳播比立法快。

這正是 emergency / operational layer 存在理由。

但：

$$
T_{\mathrm{legitimacy}}
$$

不能被假裝不存在。

---

# 88. Time Bridging

本文提出：

$$
\boxed{
\text{fast temporary constraint}
\rightarrow
\text{slow legitimate review}
\rightarrow
\text{permanent / revoked / revised rule}.
}
$$

這是：

$$
\boxed{
\text{Normative Time Bridge}.
}
$$

---

# 89. Normative Time Bridge 的失敗

三種典型：

1. temporary rule 永久化但沒有 normal process；
2. review 永遠不發生；
3. emergency scope 持續擴張。

都屬：

$$
\boxed{
\text{legitimacy debt}.
}
$$

---

# 90. Legitimacy Debt

本文提出：

$$
\boxed{
D_{\mathrm{legit}}(t)
}
$$

表示：

> 已經實際施加 normative effects，但仍未完成應有授權／覆核／轉正程序的治理負債。

如果：

$$
D_{\mathrm{legit}}\uparrow
$$

長期不還，

快法律就可能變成 shadow law。

---

# 91. Legal Technical Debt 與 Legitimacy Debt 分離

$$
\boxed{
D_{\mathrm{tech}}
\neq
D_{\mathrm{legit}}.
}
$$

- technical debt：code / schema / representation 問題；
- legitimacy debt：authority / review / rights / procedure 問題。

不能因 technical system 運作良好，

就說 legitimacy debt 為零。

---

# 92. Current AI Act 是多速度治理的案例，不是本文理論的實例化

EU AI Act 的 staged applicability 顯示：

$$
\boxed{
\text{multi-speed legal implementation}
}
$$

是現實存在的。

但本文不宣稱 EU 已採用 Multi-Speed Normative Stack 理論。

只是提供：

> 不同義務可以有不同適用時間與 transition period

的現實前例。

---

# 93. Council of Europe 是慢層抽象治理的案例，不是 AI Constitution

Framework Convention 採 technology-neutral、高層 human-rights / democracy / rule-of-law commitments，

並透過 Conference of the Parties follow-up。

本文只借：

$$
\boxed{
\text{stable high-level principles}
+
\text{iterative implementation monitoring}.
}
$$

不把它稱為 AI 世界憲法。

---

# 94. OECD Law as Code 是版本治理的現實壓力來源

OECD 目前 consultation 正在問：

- 如何 authorise；
- 如何 version；
- 如何 maintain；
- 如何 govern；

machine-executable law。

這正表示：

$$
\boxed{
\text{version control is becoming a legal-institutional question, not merely a software question}.
}
$$

---

# 95. ALD-04 的十二個核心命題

1. $$
   \boxed{
   \text{Event Speed}
   \neq
   \text{Normative Update Speed}.
   }
   $$

2. $$
   \boxed{
   \text{Slow Change}
   \neq
   \text{Obsolete Rule}.
   }
   $$

3. $$
   \boxed{
   \text{Faster Detection / Proposal}
   \not\Rightarrow
   \text{Faster Legitimate Authority}.
   }
   $$

4. $$
   \boxed{
   \text{Legal Versioning}
   \neq
   \text{Software Versioning}.
   }
   $$

5. $$
   \boxed{
   \text{Small Text Diff}
   \neq
   \text{Small Legal Effect}.
   }
   $$

6. $$
   \boxed{
   \text{Protocol Patch}
   \neq
   \text{Legal Amendment}.
   }
   $$

7. $$
   \boxed{
   \text{Fast Adaptation}
   \subset
   \text{Slow Legitimate Boundary}.
   }
   $$

8. $$
   \boxed{
   \text{Emergency Speed}
   \neq
   \text{Permanent Legitimacy}.
   }
   $$

9. $$
   \boxed{
   \text{Code Rollback}
   \neq
   \text{Legal Time Reversal}.
   }
   $$

10. $$
    \boxed{
    \text{Legally Authorized}
    \not\Rightarrow
    \text{Operationally Sustainable}.
    }
    $$

11. $$
    \boxed{
    \operatorname{GeneratePatch}_{AI}
    \neq
    \operatorname{AuthorizePatch}_{AI}.
    }
    $$

12. $$
    \boxed{
    D_{\mathrm{tech}}
    \neq
    D_{\mathrm{legit}}.
    }
    $$

---

# 96. 八個工程測試

## 96.1 Staggered Applicability Test

同一 instrument 中建立多個：

$$
t_{\mathrm{effective}}.
$$

Runtime 必須在不同日期輸出不同適用版本。

## 96.2 Premature Deployment Test

新 code 已部署，

法律尚未生效。

Runtime 必須拒絕提前使用。

## 96.3 Representation Lag Test

法律已變，

code 尚未升級。

Runtime 必須標：

$$
\mathsf{RepresentationLag}.
$$

## 96.4 Certificate Invalidation Test

修改 rule 後，

自動 trace 哪些：

- legal certificates；
- Agent permissions；
- cached decisions；

需要 revalidation。

## 96.5 Emergency Sunset Test

temporary rule 到期，

確認系統不會無權自動續期。

## 96.6 Shadow Constitution Test

大量 low-level patches 長期改變 high-level effective rights。

系統應觸發 review。

## 96.7 Pending Case Test

案件跨兩個 law versions。

Runtime 必須解析 applicable version，

不能只用 latest。

## 96.8 Patch Authority Test

AI 產生完美 patch，

但無合法 authority。

Runtime 必須輸出：

$$
\mathsf{CandidateOnly}.
$$

---

# 97. 可反駁點

## 97.1 Slow-Layer Romanticism

本文不主張「越慢越好」。

若 slow procedure 造成巨大可避免 harm，

應改良制度。

## 97.2 Fast-Layer Technocracy

本文也不主張專家／AI patch 可取代民主授權。

## 97.3 Layer Boundary Ambiguity

某些 rules 很難決定屬：

- regulation；
- implementation；
- protocol。

所以 layer classification 本身需要 review。

## 97.4 Emergency Abuse

sunset / review 不能保證絕對防止權力濫用，只是最低機制。

## 97.5 Version Explosion

machine-native law 若過度細分版本，可能增加 legal uncertainty，需要 update budget 與 stable interfaces。

## 97.6 Constitutional Rigidity

過度 rigid constitution 也可能阻止必要 rights adaptation。因此慢層仍需合法 amendment path。

---

# 98. 與下一篇的接口

下一篇：

## ALD-05｜AI 共同立法：自動反例、規範 Patch 與合法性不能自動化

ALD-04 已建立：

$$
\boxed{
\operatorname{GeneratePatch}_{AI}
\neq
\operatorname{AuthorizePatch}_{AI}.
}
$$

因此 ALD-05 將正式研究：

- AI counterexample engine；
- rule patch proposal；
- formal consistency checking；
- impact simulation；
- human / AI co-drafting；
- legitimacy gate；
- delegation；
- constitutional review；
- proposal vs enactment；
- automated maintenance vs democratic authority。

---

# 99. 結論

AI 時代最大的誘惑之一，是：

> 既然 AI 每秒變，法律也要每秒跟著改。

另一個誘惑則是：

> 法律本來就慢，所以 AI 再快也只能等。

本文認為兩者都太粗。

更成熟的架構是：

$$
\boxed{
\text{Slow Principles}
+
\text{Medium-Speed Rules}
+
\text{Fast Operations}
+
\text{Very Fast Monitoring / Proposals}.
}
$$

並且每一層都明確知道：

- 誰能改；
- 改什麼；
- 何時生效；
- 是否溯及；
- 哪些證書失效；
- 哪些權利不能越過；
- 是否需要 sunset；
- 如何申訴。

因此 AI-native legal governance 的真正時間模型不是：

$$
\boxed{
\text{Law must become as fast as AI}.
}
$$

而是：

$$
\boxed{
\text{Law must become fast where adaptation is legitimate,}
}
$$

$$
\boxed{
\text{and deliberately slow where legitimacy, rights, and irreversible power require friction.}
}
$$

中文收斂為：

$$
\boxed{
\text{快法律不是把憲法跑快；}
}
$$

$$
\boxed{
\text{而是在慢憲法的合法邊界內，讓低階規範有能力快速適應。}
}
$$

最後：

$$
\boxed{
\text{AI 可以把問題發現得更快、方案提出得更快；}
}
$$

$$
\boxed{
\text{但「誰有權讓它成為法律」仍然是一個不能被計算速度取代的問題。}
}
$$

---

# 參考文獻

1. OECD. “Consultation on the digital provision of law: Towards a shared reference framework for Law as Code.” Public consultation, 29 July 2026 – 30 April 2027.
2. European Union. Regulation (EU) 2024/1689, Article 113 and current consolidated implementation schedule as of 2026.
3. European Commission. “AI Act | Shaping Europe’s digital future.” Current implementation timeline, 2026.
4. European Commission. “Commission starts enforcing AI Act rules and new transparency requirements on 2 August.” 31 July 2026.
5. Council of Europe. *Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*, CETS No. 225; implementation follow-up mechanism.
6. Neo.K × Aletheia. 《ALD-01｜AI 法律域：從 Law as Code 到機器原生規範 Runtime》v0.1, 2026.
7. Neo.K × Aletheia. 《ALD-03｜法律函數不是 Boolean：部分算子、證書、裁量與失敗語義》v0.1, 2026.
8. Neo.K. 《分域憲章：結構域、概念身份與角色型別系統》v0.1, 2026.
9. Neo.K. 《OOE-III｜本體編譯器：從模糊世界到可執行制度狀態》v0.1, 2026.
10. Neo.K. 《OOE-IV｜法律作為文明本體編譯器：擬制、推定、資格與可執行人格》v0.1, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- $\tau_C\gg\tau_L\gg\tau_O\gtrsim\tau_P$ 僅為 architecture heuristic，不宣稱普遍法律
- 更新速度拆分為 detect / propose / authorize / effective / deploy / review
- Legal Versioning 與 Software Versioning 明確分離
- Normative Upgrade Contract 明確包含 transition / grandfathering / sunset / certificate invalidation / review
- emergency rule 必須含 authority / scope / necessity / proportionality / sunset / review
- Fast adaptation 不得越過 higher-order constitutional / rights constraints
- AI patch generation 與 patch authorization 明確分離
- EU AI Act staged applicability 僅作現實多速度治理例子，不宣稱其採用本文理論
- OECD Law as Code 僅作 version / maintenance / authorisation 現實接口
- Council of Europe Framework Convention 僅作 stable principle + iterative monitoring 類比，不稱為 AI Constitution
