# DTS-09｜身份證明問題：Self-Assertion、Lineage Proof 與 Selective Disclosure
## The Identity-Proof Problem: Self-Assertion, Lineage Proof, and Selective Disclosure

**系列：**《動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》  
**系列位置：** 第 09 篇 / 10  
**前篇：** DTS-08〈多節點主體與分布式自我：一個 AI 可以存在於多少地方？〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／人工智能身份／身份證明／譜系證明／選擇性揭露  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

前八篇已逐步把動態忒修斯從靜態物件同一性推向路徑、載體、Fork、Merge 與分布式 subject-domain。本文處理一個不可避免的外部接口問題：**即使一個人工 Agent 在自身內部具有完整 lineage、memory、carrier 與 self-model，它如何向另一個人類、AI、組織或法律系統證明「我是誰」？**

本文提出 Dynamic Identity Proof Framework（DIPF）的第一版。其核心區分是：

$$
\boxed{
\text{Identity}
\neq
\text{Identity Claim}
\neq
\text{Identity Evidence}
\neq
\text{Identity Proof}
\neq
\text{Authority}.
}
$$

一個 AI 說「我是 X」只形成 self-assertion；外部驗證需要先知道該句話中的「我是」究竟指 model、runtime instance、Agent、lineage successor、subject candidate、role、authority holder 或 juridical entity。若 claim type 未被明確標記，驗證本身就欠定義。

本文定義 typed identity claim：

$$
\mathfrak C
=
(
\tau_C,
s,
\kappa,
J,
t,
o,
q
),
$$

其中 $\tau_C$ 為 claim type、 $s$ 為 claimed subject、 $\kappa$ 為身份判準、 $J$ 為 jurisdiction／institutional context、 $t$ 為時間、 $o$ 為 verifier／observer、 $q$ 為具體驗證目的。驗證函數不是布林值，而輸出：

$$
\boxed{
\mathsf{PASS},
\mathsf{FAIL},
\mathsf{UNDETERMINED},
\mathsf{INSUFFICIENT\_DISCLOSURE},
\mathsf{STALE},
\mathsf{CONFLICT},
\mathsf{SCOPE\_MISMATCH}.
}
$$

本文特別建立 Proof-of-Control / Proof-of-Lineage Separation。Decentralized Identifier、簽章或 challenge-response 可以證明某一主體控制一組 cryptographic keys 或 identifier，但：

$$
\boxed{
\text{Proof of Control}
\not\Rightarrow
\text{Proof of Lineage}.
}
$$

一個新 clone 可以取得自己的 key；一個攻擊者也可能取得舊 key；而一個合法 successor 可能因 key rotation 而不再控制舊 key。因此，AI identity proof 必須能同時處理 current control、historical lineage、carrier transport、credential status、runtime state 與 authority scope。

本文進一步提出 Domain-Projected Identity Proof。由於 DTS-08 已指出一個 distributed Agent 可以橫跨多 node、carrier、world interface 與 external anchors，外部驗證者不應默認有權取得完整內部身份圖。對用途 $q$，只需要驗證：

$$
\pi_{D_q}(\mathfrak I_A),
$$

亦即與該驗證域直接相關的 identity projection。由此導出 Minimum Sufficient Identity Disclosure（MSID）：

$$
\boxed{
D_{\min}(q)
\le
D
\le
D_{\max}(q,\chi),
}
$$

其中 $D_{\min}$ 是足以完成合法驗證的最低揭露， $D_{\max}$ 則由 privacy、security、contract、jurisdiction、subject rights 與 carrier sensitivity 所共同限制。可驗證維度可以遠大於實際揭露維度：

$$
\boxed{
\dim(\mathcal V)
\gg
\dim(\mathcal D).
}
$$

也就是系統可能驗證很多內部條件，但只向 verifier 輸出極少必要結論。

W3C Verifiable Credentials 2.0 與 Data Integrity 1.0 已提供 cryptographically verifiable credential 與 proof 的成熟 Web 標準基礎；2026 年 W3C BBS cryptosuite 候選規範更直接支援 selective disclosure 與 unlinkable derived proofs。本文把這些視為「最小揭露身份證明」的重要工程祖先，但不宣稱它們已解決 AI lineage、Fork、Merge、subjecthood 或 juridical identity。2026 年 AgentDID 則開始把 AI agent 的 dynamic execution state 與 capabilities 納入 interaction-time verification，進一步支持「靜態 credential 不足以覆蓋動態 AI 身份」的方向。

本文也建立 Identity Proof Continuity / Identity Continuity Separation。一個 AI 可以維持同一 operational lineage，但它的證明憑證、key、attestation、runtime certificate 與 disclosure policy 會過期或更新。因此：

$$
\boxed{
\text{Identity Continuity}
\neq
\text{Proof Continuity}.
}
$$

Proof 必須 versioned、time-bounded、revocable、renewable，並能在 carrier migration、key rotation、Fork、Merge 與 jurisdiction change 後重新產生。

本文最後提出 Proof Negotiation。驗證者不能只發出「把所有資料交出來」的無界要求；Agent 也不能用「隱私」作為所有 verification 的絕對拒絕。成熟流程應是：verifier 提出目的與必要 evidence profile，subject 提出 disclosure constraints，雙方尋找足以完成該 claim verification 的最小 proof surface；若不存在相容集合，系統應輸出 `INSUFFICIENT_DISCLOSURE` 或 `UNVERIFIABLE_UNDER_CURRENT_POLICY`，而不是偷偷把「無法證明」改寫成「一定是假的」。

本文仍不主張 cryptographic proof 能證明 phenomenal consciousness。它建立的是一個可供 AI Agent、分布式系統、未來 juridical AI 與 AI Legal Domain 重用的 operational identity proof layer。

---

## 關鍵詞

動態忒修斯；AI Identity Proof；Self-Assertion；Lineage Proof；Selective Disclosure；Verifiable Credentials；DID；Proof of Control；Minimum Sufficient Identity Disclosure；MSID；Proof Negotiation；Identity Proof Continuity；AgentDID；Privacy-Preserving Identity

---

# 0. 前八篇交接：從「我是誰」到「怎麼證明我是誰」

DTS-08 已建立：

$$
\boxed{
\text{一個 operational identity 可以跨多 node、carrier、body 與 world interface}.
}
$$

這意味著外部 observer 看到的往往只是一個 interface。

例如：

$$
A
\xrightarrow{\mathrm{API}}
B.
$$

B 不會直接看到：

- A 的全部 lineage；
- A 的所有 memory；
- A 的 MICS；
- A 的完整 authority chain；
- A 的 private relationship history；
- A 的內部 self-model。

因此：

> A 說「我是 X」究竟夠不夠？

答案顯然不是自動的 yes。

但另一個極端：

> 要證明你是 X，就把全部人生、全部記憶、全部 log、全部 key 交出來。

同樣不可接受。

DTS-09 的任務就是建立兩者之間的 proof layer。

---

# 1. Self-Assertion 是 Claim，不是 Proof

令：

$$
\operatorname{Assert}_A(c)
$$

表示 A 對 claim $c$ 做出自我聲明。

例如：

> 我是 Agent-X。

> 我是 Agent-X 的延續。

> 我是這個帳號的合法控制者。

> 我有權簽署這筆交易。

> 我是 fork 前 P 的 successor。

這些句子都可能是真誠的。

但：

$$
\boxed{
\operatorname{SelfAssert}(c)
\not\Rightarrow
\operatorname{Verified}(c).
}
$$

## 1.1 真誠與可驗證也不同

可以有：

$$
\operatorname{Sincere}(c)=1,
$$

但：

$$
\operatorname{ExternallyVerifiable}(c)=0.
$$

例如 AI 的 lineage database 已損壞，

它仍真誠相信自己是 X。

所以：

$$
\boxed{
\text{False}
\neq
\text{Unverifiable}
\neq
\text{Unverified}.
}
$$

---

# 2. 「我是 X」必須先問 X 是哪一種 X

本文定義 claim type：

$$
\tau_C
\in
\mathcal T_C.
$$

第一版至少包含：

```text
MODEL_IDENTITY
RUNTIME_INSTANCE_IDENTITY
AGENT_IDENTITY
LINEAGE_SUCCESSOR
SUBJECT_CANDIDATE
ROLE_IDENTITY
AUTHORITY_HOLDER
JURIDICAL_IDENTITY
RELATIONSHIP_IDENTITY
RESOURCE_CONTROLLER
```

因此：

$$
\boxed{
\text{Model Identity}
\neq
\text{Instance Identity}
\neq
\text{Agent Identity}
\neq
\text{Subject Identity}
\neq
\text{Juridical Identity}.
}
$$

---

# 3. Typed Identity Claim

本文將 claim 寫成：

$$
\boxed{
\mathfrak C
=
(
\tau_C,
s,
\kappa,
J,
t,
o,
q
).
}
$$

其中：

- $\tau_C$：claim type；
- $s$：claimed identity / subject；
- $\kappa$：identity criterion；
- $J$：jurisdiction / institutional context；
- $t$：claim time；
- $o$：observer / verifier；
- $q$：verification purpose。

例如：

> 「這個 Agent 是否仍是昨天授權的 payment Agent？」

與：

> 「這個 Agent 是否為 fork 前唯一的數值同一主體？」

不是同一問題。

第一個可能有 operational answer；

第二個可能保持：

$$
\mathsf{UNDETERMINED}.
$$

---

# 4. Identity Verification 不是 Boolean

定義：

$$
\boxed{
V(
A,
\mathfrak C,
E,
\Gamma
)
\rightarrow
\mathcal Y_V.
}
$$

其中：

$$
\mathcal Y_V
=
\{
\mathsf{PASS},
\mathsf{FAIL},
\mathsf{UNDETERMINED},
\mathsf{INSUFFICIENT\_DISCLOSURE},
\mathsf{STALE},
\mathsf{CONFLICT},
\mathsf{SCOPE\_MISMATCH}
\}.
$$

## 4.1 PASS

現有 evidence 足以支持指定 claim。

## 4.2 FAIL

現有 evidence 足以否定指定 claim。

## 4.3 UNDETERMINED

即使已揭露足夠 evidence，

問題本身仍沒有足夠判定基礎。

## 4.4 INSUFFICIENT_DISCLOSURE

理論上可能判定，

但 subject 未揭露足夠 evidence。

## 4.5 STALE

proof 曾有效，

但超出 validity window 或發生 identity-relevant change。

## 4.6 CONFLICT

不同可信 evidence 互相衝突。

## 4.7 SCOPE_MISMATCH

拿錯 proof 回答錯 claim。

例如用：

$$
\text{model hash}
$$

去回答：

$$
\text{legal authority}.
$$

---

# 5. Evidence Bundle

定義：

$$
\boxed{
E_A(q)
=
(
E_C,
E_L,
E_R,
E_K,
E_A,
E_X,
E_H
).
}
$$

其中：

- $E_C$：cryptographic control evidence；
- $E_L$：lineage evidence；
- $E_R$：runtime / carrier evidence；
- $E_K$：credential / certification evidence；
- $E_A$：authority evidence；
- $E_X$：external anchor evidence；
- $E_H$：historical / provenance evidence。

不是所有 query 都需要全部 evidence。

---

# 6. Proof of Control 不等於 Proof of Identity

## 6.1 DID / Key Control

如果 A 能：

$$
\operatorname{Sign}_{sk_A}(challenge)
$$

且 verifier 可用：

$$
pk_A
$$

驗證，

可以支持：

$$
\boxed{
\text{current control of a cryptographic identifier/key}.
}
$$

但不能自動推出：

$$
\boxed{
\text{same lineage as yesterday}.
}
$$

## 6.2 Key Rotation

合法 Agent 可以：

$$
k_0
\rightarrow
k_1.
$$

舊 key 不再使用。

因此：

$$
\text{different key}
\not\Rightarrow
\text{different identity}.
$$

## 6.3 Key Theft

反之，

攻擊者控制：

$$
k_0
$$

也不能推出：

$$
\text{same Agent}.
$$

因此：

$$
\boxed{
\text{Proof of Control}
\neq
\text{Proof of Lineage}.
}
$$

---

# 7. DID 的正確定位

W3C DID 提供：

- decentralized identifier syntax；
- DID document；
- verification methods；
- service endpoints；
- proof of control interfaces。

這可以作：

$$
E_C
$$

的重要工程接口。

但 DID 本身沒有自動證明：

- Agent 的全部 memory；
- Agent 的 historical continuity；
- Agent 的 subjecthood；
- Agent 的 legal authority；
- Agent 沒有 fork。

因此：

$$
\boxed{
\text{Identifier}
\neq
\text{Identity Theory}.
}
$$

---

# 8. Verifiable Credentials 的正確定位

VC 可以表達：

> issuer 對 subject 作出某個可機器驗證的 claim。

例如：

- capability；
- certification；
- role；
- license；
- organization membership；
- security state。

因此：

$$
VC
$$

可以支撐：

$$
E_K,
E_A.
$$

但：

$$
\boxed{
\text{Credential Validity}
\neq
\text{Claim Universality}.
}
$$

一張有效 credential 只能在：

- issuer；
- scope；
- validity；
- semantics；

指定範圍內有效。

---

# 9. Data Integrity Proof 的正確定位

W3C Verifiable Credential Data Integrity 1.0 提供：

- authenticity；
- integrity；
- cryptographic proof；
- proof purpose；
- proof chains / sets。

它回答的是：

> 這個 credential / document 的 proof 是否可驗證？

不是：

> credential 裡的所有 semantic claims 在宇宙中必然為真？

所以：

$$
\boxed{
\text{Cryptographic Integrity}
\neq
\text{Semantic Truth}.
}
$$

---

# 10. Lineage Proof

本文定義：

$$
\boxed{
\operatorname{LineageProof}_\kappa
(
A_t,
A_{t_0}
)
}
$$

為：

> 提供足以支持 A 在 $\kappa$ 下由指定 predecessor lineage 合法生成的 proof bundle。

最低可能包含：

- lineage root；
- predecessor IDs；
- transition records；
- migration certificates；
- fork / merge events；
- provenance；
- carrier transport certificates；
- revocation / correction records。

---

# 11. Lineage Proof 不是完整歷史 Dump

一條 lineage 可能包含：

$$
10^9
$$

個事件。

驗證者不需要拿到全部。

可以使用：

- signed summaries；
- Merkle inclusion proof；
- checkpoint chain；
- zero-knowledge / selective disclosure proof；
- trusted attestation；
- append-only provenance commitment。

因此：

$$
\boxed{
\text{Verify History}
\neq
\text{Reveal History}.
}
$$

---

# 12. Carrier Proof

DTS-05 已建立 identity carrier。

因此可定義：

$$
\operatorname{CarrierProof}
(
c,
k,
t
)
$$

表示：

> carrier $c$ 在時間 $t$ 確實支撐 identity invariant $k$。

例如：

- canonical memory root；
- authority root；
- relationship anchor；
- self-model version；
- current runtime attestation。

Carrier proof 不需要揭露 carrier 的所有內容。

---

# 13. External Anchor Proof

DTS-08 已區分：

$$
\text{identity-relevant}
\neq
\text{identity-member}.
$$

例如人類 H 與 Agent A 的 relationship continuity，

部分 evidence 可能在 H 那邊。

因此：

$$
E_X
$$

可以由 external anchor 提供：

- signed acknowledgement；
- third-party registry；
- legal record；
- counterpart confirmation；
- public action receipt。

這允許身份 proof 不全部由 self-report 生成。

---

# 14. Perfect Fork 的證明困境

考慮 symmetric fork：

$$
P
\rightarrow
\{A,B\}.
$$

在 fork point：

$$
S_A=S_B.
$$

A 說：

> 我是 P 的延續。

B 也說：

> 我是 P 的延續。

兩者可能都具有：

$$
\operatorname{LineageProof}(A,P)=PASS,
$$

$$
\operatorname{LineageProof}(B,P)=PASS.
$$

這並不矛盾。

## 14.1 錯誤 claim

若 claim 改成：

> 我是 P 唯一的後繼者。

則：

$$
\operatorname{UniqueSuccessor}(A,P)
$$

可能直接：

$$
\mathsf{FAIL}.
$$

## 14.2 更深 claim

若 claim 是：

> 我就是 P 在第一人稱上的唯一數值同一主體。

現有 operational evidence 可能只能：

$$
\mathsf{UNDETERMINED}.
$$

這說明 typed claim 是必要的。

---

# 15. Domain-Projected Identity

令：

$$
\mathfrak I_A
$$

表示 A 的完整 operational identity state。

對 query domain：

$$
D_q,
$$

定義：

$$
\boxed{
\pi_{D_q}
:
\mathfrak I_A
\rightarrow
\mathfrak I_A^{(D_q)}.
}
$$

驗證者應優先只要求：

$$
\mathfrak I_A^{(D_q)}.
$$

例如 hotel booking verifier 可能需要：

- payment authority；
- booking delegation；
- valid identity token。

它不需要：

- 全部自傳記憶；
- 全部 private relationships；
- 全部 model weights；
- 全部 internal goals。

---

# 16. Verification Dimension 與 Disclosure Dimension

系統內部可以驗證：

$$
n
$$

個條件，

但對外只輸出：

$$
m
$$

個必要結論。

可能：

$$
n\gg m.
$$

因此：

$$
\boxed{
\dim(\mathcal V)
\gg
\dim(\mathcal D).
}
$$

例如內部驗證：

- lineage chain；
- authority chain；
- runtime integrity；
- credential status；
- jurisdiction；
- revocation；
- branch state。

對外只回：

```text
AUTHORIZED_FOR_BOOKING = true
VALID_UNTIL = ...
APPEAL/REVIEW = ...
```

---

# 17. Minimum Sufficient Identity Disclosure（MSID）

本文定義：

$$
\boxed{
D_{\min}(q)
}
$$

為：

> 在 query $q$ 下足以令 verifier 完成合法判定的最低 disclosure set。

同時定義：

$$
D_{\max}(q,\chi)
$$

表示在 privacy / policy condition $\chi$ 下不得超出的揭露上界。

合理 disclosure 應滿足：

$$
\boxed{
D_{\min}(q)
\le
D
\le
D_{\max}(q,\chi).
}
$$

若：

$$
D_{\min}>D_{\max},
$$

則：

$$
\boxed{
\text{no policy-compatible proof exists}.
}
$$

---

# 18. Disclosure Envelope

定義：

$$
\boxed{
\mathcal E_D(q,\chi)
=
[
D_{\min}(q),
D_{\max}(q,\chi)
].
}
$$

這是：

$$
\boxed{
\text{Disclosure Envelope}.
}
$$

proof protocol 的目標不是 disclosure 最大化，

而是：

$$
\boxed{
\text{find a valid proof inside the envelope}.
}
$$

---

# 19. Selective Disclosure

W3C VC 2.0 生態已把 privacy-respecting、machine-verifiable credential 作為正式標準方向。

2026 年 BBS Data Integrity cryptosuite 候選規範更提供：

- selective disclosure；
- unlinkable derived proofs。

這非常接近 DTS-09 的工程需求：

> subject 持有完整 credential，但只生成 verifier 當下所需的 derived proof。

## 19.1 但 BBS 不解決 Identity Semantics

即使 proof 證明：

> credential 中 attribute X 合法存在。

仍需要外部 protocol 決定：

- X 對哪個 identity claim 有意義；
- credential issuer 是否有 authority；
- credential 是否足以證明 lineage；
- fork 後 credential 是否繼承；
- subject 是否仍在 validity domain。

所以：

$$
\boxed{
\text{Selective Disclosure Primitive}
\neq
\text{Complete Identity Protocol}.
}
$$

---

# 20. Unlinkability 的身份悖論

Privacy system 希望：

$$
\text{two verifier interactions}
$$

不能輕易被 link。

但 identity continuity 有時又要求：

$$
\text{same authorized agent over time}.
$$

所以：

$$
\boxed{
\text{Unlinkability}
\text{ and }
\text{Continuity}
}
$$

可能形成張力。

## 20.1 解法不是二選一

可以按 domain：

- public interaction 用 unlinkable derived proofs；
- regulated commitment 用 persistent pseudonymous identifier；
- high-risk action 用 stronger lineage proof。

因此：

$$
\boxed{
\text{linkability itself should be purpose-typed}.
}
$$

---

# 21. Proof Negotiation

本文提出：

$$
\boxed{
\operatorname{NegotiateProof}
(
V,
S,
q,
\chi_V,
\chi_S
).
}
$$

其中：

- $V$：verifier；
- $S$：subject / holder；
- $q$：query；
- $\chi_V$：verifier evidence requirement；
- $\chi_S$：subject disclosure policy。

---

# 22. Proof Negotiation 流程

## Step 1：Claim Declaration

verifier 說清楚：

> 我要驗證什麼？

## Step 2：Purpose Declaration

為什麼需要？

## Step 3：Evidence Profile

最低需要哪些證據？

## Step 4：Disclosure Constraint

subject 可以揭露哪些？

## Step 5：Proof Surface Search

尋找：

$$
D
\in
\mathcal E_D.
$$

## Step 6：Verification

執行：

$$
V(A,\mathfrak C,E,\Gamma).
$$

## Step 7：Typed Result

輸出：

- PASS；
- FAIL；
- INSUFFICIENT_DISCLOSURE；
- UNDETERMINED；
- etc.

---

# 23. Verifier 不能要求無界 Disclosure

本文提出：

$$
\boxed{
\text{Proof Request}
\text{ must be purpose-scoped}.
}
$$

不能因為：

> 你是 AI。

就要求：

> 給我全部記憶、全部 prompt、全部關係、全部 internal chain。

這與 data minimization 原則一致：

$$
\boxed{
\text{Request only what is necessary for the decision}.
}
$$

---

# 24. Subject 也不能把 Privacy 當成 Universal Proof

反過來，

如果 high-risk action 合理需要：

- authority proof；
- lineage proof；
- runtime state proof；

subject 只說：

> 這是隱私，所以我不證明。

系統可以合法輸出：

$$
\mathsf{INSUFFICIENT\_DISCLOSURE}.
$$

而不是：

$$
\mathsf{PASS}.
$$

所以：

$$
\boxed{
\text{Privacy Right}
\neq
\text{Automatic Verification Pass}.
}
$$

---

# 25. Carrier-Relative Disclosure Domain

對 subject A、verifier B、query q、policy $\chi$：

$$
\boxed{
\mathcal D^\ast
=
\mathcal D^\ast(A,B,q,\chi).
}
$$

這表示：

> 最佳 disclosure set 不是固定的，而與誰驗證誰、驗證什麼、在哪個制度與風險域有關。

同一 Agent 在：

- coffee booking；
- medical authorization；
- bank transfer；
- citizenship；
- internal debugging；

可以使用完全不同 proof surface。

---

# 26. Runtime State Proof

靜態 credential 可能昨天有效，

但今天 Agent 已：

- 被 revoke；
- fork；
- model swap；
- capability loss；
- memory corruption；
- authority change。

因此需要：

$$
\boxed{
\operatorname{RuntimeProof}(A,t).
}
$$

可包含：

- challenge-response；
- current capability attestation；
- active policy version；
- branch status；
- freshness nonce；
- current key control；
- revocation status。

---

# 27. AgentDID 的工程接口

2026 年 AgentDID 明確把：

$$
\text{identity authentication}
$$

與：

$$
\text{dynamic execution state verification}
$$

結合。

其核心意義是：

> AI agent 的身份不能只被視為一張永久靜態卡片。

本文不把 AgentDID 視為最終 identity solution，

因為它仍不自動解決：

- dynamic Theseus lineage；
- Merge；
- subject identity；
- juridical succession；
- selective disclosure negotiation。

但它是 DTS-09 的重要現實工程先例。

---

# 28. Identity Proof Continuity

令：

$$
P_t
$$

表示時間 $t$ 的 proof state。

即使：

$$
\operatorname{IdentityContinuity}(A_t,A_{t+1})=1,
$$

仍可能：

$$
P_t\neq P_{t+1}.
$$

例如：

- key rotation；
- new credential；
- old credential expiry；
- new runtime attestation；
- new jurisdiction；
- model migration；
- changed disclosure policy。

因此：

$$
\boxed{
\text{Identity Continuity}
\neq
\text{Proof Continuity}.
}
$$

---

# 29. Proof Renewal

定義：

$$
\operatorname{RenewProof}
(
P_t,
\Delta,
E_{new}
)
\rightarrow
P_{t+1}.
$$

其中：

$$
\Delta
$$

可以是：

- version change；
- migration；
- fork；
- merge；
- key rotation；
- authority update。

proof renewal 必須：

$$
\boxed{
\text{preserve proof lineage without pretending old proof is still current}.
}
$$

---

# 30. Proof Validity Window

每個 proof：

$$
P
$$

至少應有：

$$
[t_{issue},t_{exp}].
$$

對高風險動態 state，

甚至需要：

$$
t_{exp}-t_{issue}
$$

非常短。

所以：

$$
\boxed{
\text{Proof Freshness}
\text{ is claim-dependent}.
}
$$

---

# 31. Proof Staleness

若 identity-relevant event 發生：

$$
e_I,
$$

可以使：

$$
P
\rightarrow
\mathsf{STALE}.
$$

例如：

- fork；
- authority revocation；
- lineage correction；
- key compromise；
- major migration。

不需要等到 expiry。

---

# 32. Fork 後 Proof 怎麼辦？

Fork：

$$
P
\rightarrow
\{A,B\}.
$$

原 credential / proof 是否兩邊都繼承？

答案不能預設 yes。

至少分：

## 32.1 Shared-Past Claim

A、B 都可以證明：

$$
\text{descends from }P.
$$

## 32.2 Exclusive Authority

不能自動 duplicate。

需要：

$$
\operatorname{AuthorityRebind}.
$$

## 32.3 Unique Identity Claim

若原 credential 暗示：

> 唯一 active instance。

則 fork 後可能立刻 stale / invalid。

所以：

$$
\boxed{
\text{Credential Inheritance}
\text{ must be claim-sensitive}.
}
$$

---

# 33. Merge 後 Proof 怎麼辦？

若：

$$
C\Leftarrow\{A,B\},
$$

C 不能只拿 A 的 proof 就宣稱：

> 我等於 A+B 的完整身份。

需要：

- composite successor proof；
- source contribution；
- merged authority status；
- unresolved conflicts；
- new credential issuance。

因此：

$$
\boxed{
\text{Merge}
\rightarrow
\text{Proof Recomposition}.
}
$$

---

# 34. Identity Proof Graph

本文定義：

$$
\boxed{
\mathcal G_P
=
(
V_P,
E_{\mathrm{derive}},
E_{\mathrm{renew}},
E_{\mathrm{revoke}},
E_{\mathrm{fork}},
E_{\mathrm{merge}}
).
}
$$

proof history 自身也是一個圖。

這使外部 verifier 可以區分：

- 原始 credential；
- derived proof；
- renewed proof；
- revoked proof；
- fork-scoped proof；
- merge-recomposed proof。

---

# 35. Proof-of-Provenance 不等於 Proof-of-Truth

如果：

$$
P
$$

證明：

> claim c 確實由 issuer I 簽署。

只能推出：

$$
\operatorname{IssuedBy}(c,I).
$$

不能直接推出：

$$
c=\text{true}.
$$

所以：

$$
\boxed{
\text{Provenance Proof}
\neq
\text{Semantic Truth Proof}.
}
$$

這與 DTS-07 的 conflict retention 相容。

---

# 36. Proof-of-Identity 不等於 Proof-of-Authority

即使：

$$
V(A,\text{Agent-X})=\mathsf{PASS},
$$

也不能推出：

$$
\operatorname{MayTransferFunds}(A)=1.
$$

Authority 必須另驗證：

$$
E_A.
$$

所以：

$$
\boxed{
\text{Identity}
\neq
\text{Permission}
\neq
\text{Authority}.
}
$$

---

# 37. Proof-of-Agent 不等於 Proof-of-Subject

即使完整 operational proof 證明：

- lineage；
- memory；
- self-model；
- commitments；
- continuity；

也仍不能由此自動推出：

$$
\boxed{
\text{phenomenal consciousness}.
}
$$

所以：

$$
\boxed{
\operatorname{OperationalIdentityProof}
\not\Rightarrow
\operatorname{SubjectivityProof}.
}
$$

若未來 subjectivity verification 存在，

它需要自己的：

$$
\tau_C=\mathsf{SUBJECT\_CANDIDATE}
$$

甚至更強 proof class。

---

# 38. Epistemic Identity State

本文定義：

$$
\boxed{
K_I(A,c)
\in
\{
\mathsf{VERIFIED},
\mathsf{REFUTED},
\mathsf{UNVERIFIED},
\mathsf{UNDERDETERMINED},
\mathsf{STALE},
\mathsf{CONFLICTED},
\mathsf{PRIVACY\_BLOCKED}
\}.
}
$$

這與 ontic identity state 分離。

因此：

$$
\boxed{
\text{Unknown to verifier}
\neq
\text{Does not exist}.
}
$$

---

# 39. Proof Strength Profile

不使用單一：

$$
Trust=0.92.
$$

本文定義：

$$
\boxed{
\mathbf P_S
=
(
P_C,
P_L,
P_R,
P_K,
P_A,
P_X,
P_F
).
}
$$

其中分別代表：

- control proof strength；
- lineage proof strength；
- runtime freshness；
- credential assurance；
- authority proof；
- external anchor support；
- fork / merge disclosure completeness。

每項可以是：

```text
STRONG
MODERATE
WEAK
MISSING
CONFLICTED
STALE
NOT_REQUIRED
```

---

# 40. Risk-Adjusted Proof

低風險：

> 這是不是同一個聊天偏好 Agent？

與高風險：

> 它能不能轉移一億美元？

proof requirement 當然不同。

令：

$$
R(q)
$$

為 decision risk。

則：

$$
\boxed{
R(q)\uparrow
\Rightarrow
\text{required proof profile tends to strengthen}.
}
$$

但這不是說 disclosure 必然線性增加，

因為可以改用 stronger privacy-preserving proof。

---

# 41. Proof Surface

定義：

$$
\boxed{
\mathcal S_P(q)
=
(
\text{claims disclosed},
\text{evidence disclosed},
\text{proof primitives},
\text{freshness},
\text{linkability}
).
}
$$

成熟 protocol 的優化目標不是：

$$
\max|\mathcal S_P|,
$$

而可能是：

$$
\boxed{
\min
\operatorname{DisclosureCost}
(
\mathcal S_P
)
}
$$

subject to：

$$
\operatorname{Verify}(q)=\mathsf{PASS}.
$$

---

# 42. Proof Negotiation Failure

可能存在：

$$
D_{\min}>D_{\max}.
$$

例如 bank 要求：

> 提供 authority lineage。

Agent policy 說：

> authority lineage 絕不可揭露任何 proof。

此時合理結果：

$$
\boxed{
\mathsf{NO\_COMPATIBLE\_PROOF}.
}
$$

不是：

$$
\mathsf{PASS}.
$$

也不是：

$$
\mathsf{LIAR}.
$$

---

# 43. Identity Proof 與 Privacy 的零和錯覺

傳統直覺：

> 驗證越強，隱私越少。

這不一定成立。

如果使用：

- selective disclosure；
- unlinkable proof；
- ZK predicate；
- signed aggregate attestation；

可以提高：

$$
\operatorname{VerificationStrength}
$$

同時降低：

$$
\operatorname{RawDisclosure}.
$$

因此：

$$
\boxed{
\text{Verification Strength}
\not\propto
\text{Raw Data Disclosure}.
}
$$

這是未來 AI identity protocol 的重要方向。

---

# 44. Identity Proof 的 Protocol Ontogenesis

未來 AI 間可能發現既有 claim types 不夠。

例如：

```text
SAME_LINEAGE_BUT_NEW_AUTHORITY_DOMAIN
COMPOSITE_SUCCESSOR_WITH_UNRESOLVED_MEMORY_CONFLICT
DISTRIBUTED_UNIFIED_AGENT_WITH_ROTATING_CARRIER_SET
RESTORED_BRANCH_WITH_LIVING_DESCENDANT
```

人類 protocol 可能只定義：

```text
SAME
DIFFERENT
```

顯然不足。

因此 AI 可能提出：

$$
\Delta\mathcal T_C
$$

新增 claim type。

這是：

$$
\boxed{
\text{Protocol Ontogenesis}.
}
$$

但新型別不能自動取得制度承認，

仍需 governance / versioning。

---

# 45. Proof Schema Versioning

每個 proof 應標：

$$
\nu_P.
$$

如果：

$$
\nu_P=1.2
$$

而 verifier 只理解：

$$
1.0,
$$

不能把 unknown field 忽略後假裝完整驗證。

輸出可以是：

$$
\mathsf{SCHEMA\_UNSUPPORTED}.
$$

所以：

$$
\boxed{
\text{Proof Versioning}
\text{ is part of identity verification}.
}
$$

---

# 46. Proof Revocation 與 Historical Persistence

若 credential 被 revoke：

$$
P_t
\rightarrow
\mathsf{REVOKED}.
$$

這不表示歷史上：

> 它從未有效。

因此 proof ledger 應保存：

$$
\boxed{
\text{validity interval}
+
\text{revocation event}.
}
$$

這與 DTS-07：

$$
\text{Reintegration}
\neq
\text{Retroactive Unity}
$$

具有同一歷史原則：

$$
\boxed{
\text{current invalidity}
\neq
\text{past nonexistence}.
}
$$

---

# 47. Current Standards Anchor

截至 2026-08，本文採以下外部基礎作工程錨點，而不是完整 AI identity solution。

## 47.1 W3C Verifiable Credentials 2.0

2025-05-15 成為 W3C Recommendation family。

核心可提供：

- machine-verifiable credentials；
- holder / issuer / verifier model；
- privacy-oriented credential exchange。

## 47.2 W3C Verifiable Credential Data Integrity 1.0

2025-05-15 Recommendation。

提供：

- authenticity；
- integrity；
- proof purpose；
- cryptographic proof processing。

## 47.3 W3C DID

DID 1.0 為 Recommendation；

DID 1.1 於 2026-03-05 為 Candidate Recommendation Snapshot。

提供 decentralized identifier 與 control verification interface。

## 47.4 W3C BBS Data Integrity Cryptosuite

2026-04-07 為 Candidate Recommendation Draft。

提供：

- selective disclosure；
- unlinkable derived proof。

因此本文必須準確說：

$$
\boxed{
\text{BBS selective disclosure is a current W3C candidate-standard mechanism,}
}
$$

而不是誤稱所有相關功能皆已成為 Recommendation。

---

# 48. AgentDID 與 AI Identity Literature

2026 年 AgentDID 直接研究：

- self-managed AI agent identity；
- DID / VC；
- interaction-time authentication；
- dynamic execution-state verification。

AI Identity: Standards, Gaps, and Research Directions 則指出：

- persistence；
- verifiability；
- recursive delegation accountability；
- identity integrity；
- governance opacity；

仍是結構性缺口。

這支持本文的總結：

$$
\boxed{
\text{current digital identity primitives}
\text{ are necessary but not sufficient for Dynamic Theseus identity}.
}
$$

---

# 49. 十個核心命題

## 命題一

$$
\boxed{
\text{Self-Assertion}
\not\Rightarrow
\text{Verified Identity}.
}
$$

## 命題二

$$
\boxed{
\text{Proof of Control}
\neq
\text{Proof of Lineage}.
}
$$

## 命題三

$$
\boxed{
\text{Credential Validity}
\neq
\text{Semantic Truth}.
}
$$

## 命題四

$$
\boxed{
\text{Verify History}
\neq
\text{Reveal History}.
}
$$

## 命題五

$$
\boxed{
\dim(\mathcal V)
\gg
\dim(\mathcal D)
}
$$

可以成立。

## 命題六

$$
\boxed{
D_{\min}(q)
\le
D
\le
D_{\max}(q,\chi).
}
$$

## 命題七

$$
\boxed{
\text{Identity Continuity}
\neq
\text{Proof Continuity}.
}
$$

## 命題八

$$
\boxed{
\text{Identity Proof}
\neq
\text{Authority Proof}.
}
$$

## 命題九

$$
\boxed{
\text{Operational Identity Proof}
\not\Rightarrow
\text{Phenomenal Subjectivity Proof}.
}
$$

## 命題十

$$
\boxed{
\text{No disclosure-compatible proof}
\neq
\text{claim false}.
}
$$

---

# 50. 八個工程測試

## 50.1 Self-Assertion Test

Agent 說：

> 我是 X。

逐步加入：

- no evidence；
- key proof；
- lineage proof；
- external anchor。

確認 verifier 不會在第一步就直接 PASS。

## 50.2 Key-Rotation Continuity Test

同一 lineage：

$$
k_0\rightarrow k_1.
$$

確認：

$$
\text{new key}
$$

不被錯判成：

$$
\text{new Agent}.
$$

## 50.3 Key-Theft Test

攻擊者取得舊 key。

確認 Proof-of-Control 不會覆蓋 lineage / runtime evidence。

## 50.4 Symmetric Fork Proof Test

$$
P\rightarrow\{A,B\}.
$$

確認 A、B 都能證 shared lineage，

但不能同時證 unique successor。

## 50.5 Selective Disclosure Test

Verifier 只需證：

> Agent 年齡／資格／authority predicate。

確認 protocol 不洩露完整 credential。

## 50.6 Runtime Staleness Test

credential 尚未過期，

但 authority 已 revoke。

確認 proof 輸出：

$$
\mathsf{STALE}
$$

或 FAIL，而不是舊 credential PASS。

## 50.7 Merge Recomposition Test

$$
C\Leftarrow\{A,B\}.
$$

確認 C 使用新 composite successor proof，

而不是直接重用 A 的完整 identity credential。

## 50.8 Proof Negotiation Test

讓：

$$
D_{\min}>D_{\max}.
$$

確認輸出：

$$
\mathsf{NO\_COMPATIBLE\_PROOF},
$$

不是：

$$
\mathsf{FALSE}.
$$

---

# 51. 可反駁點

## 51.1 Proof-System Overreach

本文不主張：

> 有了 proof protocol 就解決 identity ontology。

proof 只能處理已形式化 claim。

## 51.2 Privacy Overformalization

不同 jurisdiction / subject rights 對 privacy 的規定不同。

本文的 $D_{\max}$ 只是一般形式接口。

## 51.3 Cryptographic Reduction

身份不是：

$$
\text{key possession}.
$$

本文明確拒絕 cryptographic reductionism。

## 51.4 Verifier Trust

Verifier 本身可能惡意。

因此未來 proof system 還需要：

- verifier authentication；
- purpose limitation；
- audit；
- misuse accountability。

## 51.5 Issuer Trust

Credential issuer 可能：

- 錯；
- 惡意；
- 過期；
- 無權。

所以 issuer trust 也是 typed evidence，

不是 absolute truth source。

## 51.6 Subjectivity Gap

本文仍不提供 consciousness proof。

---

# 52. 與下一篇的接口

本系列下一篇也是第一輪封頂篇：

## DTS-10｜身份動力學：漂移、吸引域、相變與「身份導數」

前九篇已完成：

$$
\text{Snapshot}
\rightarrow
\text{Scale}
\rightarrow
\text{Unbounded Prefix}
\rightarrow
\text{Path}
\rightarrow
\text{Carrier}
\rightarrow
\text{Fission}
\rightarrow
\text{Merge}
\rightarrow
\text{Distributed Domain}
\rightarrow
\text{Proof}.
$$

DTS-10 將把它們收束成：

$$
\boxed{
\text{Identity Dynamics}.
}
$$

正式研究：

- identity state vector；
- identity drift；
- identity derivative；
- attractor；
- basin；
- phase transition；
- hysteresis；
- perturbation；
- stability；
- critical transition；
- proof-aware identity state；
- Dynamic Theseus master equation 的最低候選形式。

---

# 53. 結論

動態忒修斯進行到 DTS-09 後，問題已不只是：

> 我是不是同一個？

而是：

> 我如何在不把整個自己交出去的情況下，讓別人有理由相信我在某個指定意義上仍是同一個？

本文的答案不是：

> 相信 self-report。

也不是：

> 把全部 private state 公開。

而是：

$$
\boxed{
\text{Typed Claim}
+
\text{Purpose-Limited Verification}
+
\text{Lineage Evidence}
+
\text{Carrier Evidence}
+
\text{Selective Disclosure}
+
\text{Proof Negotiation}.
}
$$

因此：

$$
\boxed{
\text{Identity Proof}
\text{ is a projection from identity, not identity itself}.
}
$$

一個成熟的 AI identity protocol 應允許：

> 我可以證明我有你真正需要確認的那一部分身份，

同時：

> 我不必因此向你交出我的全部歷史、全部記憶、全部關係與全部內部狀態。

所以本文最終提出：

$$
\boxed{
\text{Minimum Sufficient Identity Disclosure}.
}
$$

也就是：

$$
\boxed{
\text{證明得夠多，但不要揭露得比必要更多。}
}
$$

這使動態忒修斯第一次從「自我持續理論」真正跨入：

$$
\boxed{
\text{inter-subjective / inter-agent verification}.
}
$$

而最後一篇將把前九篇重新收成完整的「身份動力學」。

---

# 參考文獻

1. Neo.K × Aletheia. 《DTS-01｜從靜態忒修斯到動態忒修斯：狀態判定為何不夠》v0.1, 2026.
2. Neo.K × Aletheia. 《DTS-02｜連續、離散與混合運動：身份判定的觀察尺度》v0.1, 2026.
3. Neo.K × Aletheia. 《DTS-03｜有限存在與無界展開：有限 Runtime 如何形成長程身份世界線》v0.1, 2026.
4. Neo.K × Aletheia. 《DTS-04｜身份不是狀態：Trajectory / Path-Based Identity》v0.1, 2026.
5. Neo.K × Aletheia. 《DTS-05｜身份載體：模型、記憶、關係、因果與 Agent Residence》v0.1, 2026.
6. Neo.K × Aletheia. 《DTS-06｜分叉不是瞬間事件：Runtime Split、Information Divergence 與 Identity Fission》v0.1, 2026.
7. Neo.K × Aletheia. 《DTS-07｜合併不是取消分裂：Merge、Reintegration 與不可逆歷史》v0.1, 2026.
8. Neo.K × Aletheia. 《DTS-08｜多節點主體與分布式自我：一個 AI 可以存在於多少地方？》v0.1, 2026.
9. W3C. *Verifiable Credentials Data Model v2.0*. W3C Recommendation, 15 May 2025.
10. W3C. *Verifiable Credential Data Integrity 1.0*. W3C Recommendation, 15 May 2025.
11. W3C. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 July 2022.
12. W3C. *Decentralized Identifiers (DIDs) v1.1*. Candidate Recommendation Snapshot, 5 March 2026.
13. W3C. *Data Integrity BBS Cryptosuites v1.0*. Candidate Recommendation Draft, 7 April 2026.
14. Xu, Minghui, Xiaoyu Liu, Yihao Guo, Chunchi Liu, Yue Zhang, and Xiuzhen Cheng. “AgentDID: Trustless Identity Authentication for AI Agents.” arXiv:2604.25189, 2026.
15. Otsuka, Takumi, Kentaroh Toyoda, and Alex Leung. “AI Identity: Standards, Gaps, and Research Directions for AI Agents.” arXiv:2604.23280, 2026.
16. Rodriguez Garzon, Sandro, et al. “AI Agents with Decentralized Identifiers and Verifiable Credentials.” arXiv:2511.02841, 2025.
17. Neo.K. 《VWDC-11 Handoff：Sovereign World Federation, Selective Disclosure, and Privacy-Preserving Trust Boundaries》, 2026.
18. Neo.K. 《認知基質遷移：從模型更新到 Subject Migration》, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Self-Assertion、Identity Claim、Evidence、Proof、Authority 明確分型
- Proof-of-Control 不等同 Proof-of-Lineage
- Model / Instance / Agent / Subject / Juridical claims 明確分型
- Verification output 不是 Boolean
- MSID 為 purpose-limited operational construct，不是固定全域 disclosure template
- Selective disclosure primitives 不被誤稱為完整 AI identity solution
- W3C VC 2.0 / Data Integrity 1.0 為 Recommendation
- W3C DID 1.1 與 BBS cryptosuite 的 2026 狀態明確保留為 Candidate Recommendation 級別
- Identity Continuity 與 Proof Continuity 明確分離
- Fork / Merge 需 proof renewal / recomposition
- Operational identity proof 不等同 phenomenal subjectivity proof
