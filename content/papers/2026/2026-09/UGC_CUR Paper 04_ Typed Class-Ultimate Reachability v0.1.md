# UGC/CUR Paper 04: Typed Class-Ultimate Reachability v0.1
## 型別化類終極可達性：觀察者、關係、邊界、跨層通道、能力模式、正負見證與完備覆蓋之形式化

**系列：** UGC/CUR — Unbounded Generative Closure and Class-Ultimate Reachability  
**篇次：** Paper 04  
**文件編號：** EML-UGC-CUR-P04-2026-v0.1  
**作者：** Neo.K with Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-26  
**版本：** v0.1  
**文件性質：** canonical formal research paper / typed reachability calculus / class-ultimate assessment layer  
**狀態：** CANONICAL RESEARCH DRAFT / VALIDATED SOURCE  
**直接上游：** Canonical Reconciliation v0.1、Formal Core Specification v0.1、Paper 01 v0.1、Paper 02 v0.1、Paper 03 v0.1  
**主要橋接：** OBRC typed connectivity and boundary theory、SCDT observer-relative projection、Cross-Layer Channel Theory、Realizability Theory、Global Ledger accounting  

---

# 摘要

本文建立 UGC/CUR 的 **Typed Class-Ultimate Reachability** 層，將早期以裸集合表示的「一個存在能作用到多少存在域」重新形式化為帶有 agent、target、capability mode、relation type、observer context、boundary state、time horizon、operator family、permission regime、positive witness、negative obstruction 與 verification channel 的型別化判定。

本文沿用 Formal Core 的 capability family：

$$
\boxed{
\mathfrak M_{\rm cap}
=
\{
\mathsf{observe},
\mathsf{access},
\mathsf{act},
\mathsf{control},
\mathsf{transform},
\mathsf{ruleRewrite},
\mathsf{genRewrite},
\mathsf{verify}
\}.
}
$$

對 agent $A$ 、target $x$ 、mode $m$ 、relation type $R$ 、context $\Theta$ 與時間 $t$，基本 judgement 為：

$$
\boxed{
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)
\in
\mathfrak J,
\qquad
\mathfrak J
=
\{1,0,?,\mathsf B,\mathsf S\}.
}
$$

其中 $1$ 表示在宣告 scope 內已有正面 reach witness； $0$ 表示已有 scoped negative obstruction / completeness certificate； $?$ 表示未知； $\mathsf B$ 表示 branch-dependent； $\mathsf S$ 表示 scope-dependent。本文因此固定：

$$
\boxed{
\mathrm{NoPathFound}
\neq
\mathrm{NoPathExists},
}
$$

以及：

$$
\boxed{
\mathsf{Connectivity}
\neq
\mathsf{Reachability}
\neq
\mathsf{Realizability}
\neq
\mathsf{TransformationCompleteness}.
}
$$

本文採用 OBRC 的 state-bearing boundary 與 typed connectivity：同一 boundary 可以對某 relation type 為 barrier、對另一 relation type 為 medium；共享 boundary 也不等於 agent 擁有可使用的 reach path。因此 positive reach witness 必須保留 relation sequence、boundary state、direction、operator use、permission、transform/loss、verification 與 provenance。negative reach claim 則不得由搜尋失敗直接產生，而需要 cut、type impossibility、permission closure、channel-null proof、exhaustive search、必要條件違反或其他 scoped obstruction certificate。

跨層問題被統一成 versioned channel object：

$$
\boxed{
\mathsf{XLCh}_{i\to j}(t)
=
\left\langle
\mathsf{ObsCh}_{i\to j},
\mathsf{ActCh}_{i\to j},
\mathsf{RespCh}_{i\to j},
\mathsf{VerCh}_{i\to j},
\mathsf{Scope},
\mathsf{Version},
\mathsf{Cert}
\right\rangle_t.
}
$$

由此正式保留：

$$
\boxed{
\text{Layer Existence}
\neq
\text{Layer Observability}
\neq
\text{Cross-Layer Reachability}
\neq
\text{Cross-Layer Controllability}.
}
$$

parent / host / creator relation 不自動提供 reverse access；可觀測痕跡不自動提供 action channel；action channel 不自動提供 response 或 verification channel；智能增長也不能在 channel-null model 中憑空產生跨層控制。

本文進一步定義 agent-target reach profile：

$$
\boxed{
\mathbf R_A(x,t\mid\Theta)
=
\left(
r_{\rm obs},
r_{\rm access},
r_{\rm act},
r_{\rm ctrl},
r_{\rm trans},
r_{\rm rule},
r_{\rm gen},
r_{\rm ver}
\right),
}
$$

但這些 mode 只形成 typed capability family，不預設固定全序。任何 mode lifting，例如由 observe 推到 access、由 act 推到 control，必須有 domain-specific bridge theorem 或 contract。本文同時加入 value-rank firewall：capability dominance、observation reach、meta-observation depth 或 cross-layer access 都不能自動轉換成 existence value、moral value、personhood rank 或 ontological priority。

對 class-ultimate claim，本文不再只檢查「可達 target set 有多大」，而先建立 target specification：

$$
\boxed{
\mathsf{CUTarget}
=
\left\langle
D,
\Omega_D,
\mathcal M^{\star},
\mathfrak R^{\star},
T,
\Theta,
\mathfrak E^{\star}_{\rm ext}
\right\rangle.
}
$$

其中 $\mathcal M^{\star}$ 是 required capability modes， $\mathfrak R^{\star}$ 是允許或要求的 relation family， $T$ 是 horizon， $\mathfrak E^{\star}_{\rm ext}$ 是若 domain 可開放展開時允許的 extension class。對有限或已證封閉 domain，可用 extensional coverage certificate；對 open-ended / unbounded domain，則允許以 intensional / uniform reach schema 證明一整類 target-mode pair，而不能假裝有限枚舉已覆蓋未知未來存在。

本文定義 Class-Ultimate Assessment 等級 $\mathsf{CUA}_0$ 到 $\mathsf{CUA}_4$。最高級 $\mathsf{CUA}_4$ 仍只表示相對於宣告 target specification 的 extension-stable / uniformly witnessed class-ultimate candidate，不推出 absolute omnipotence、absolute omniscience、first-cause priority 或 metaphysical superiority。

Paper 03 的 Global Ledger 被用作 witness substrate：每個 reach judgement、channel version、boundary event、positive witness、negative obstruction、coverage debt 與 completeness certificate 都可寫入 $\mathsf{Ledger}_{D,\Theta}(t)$。因此 Class-Ultimate claim 不再是單一巨大形容詞，而是一個可重放、可追溯、可更新、可失敗的 typed coverage claim。

本文最後保留 Paper 05 的邊界：本篇可以判定 transform / ruleRewrite / genRewrite mode 的 reach status，但不將「能對 target 施加某種 transformation」偷換成「對 declared transformation class 完備」。完整 Transformation Closure 與 Meta-Causal Agency 留待下一篇形式化。

本文核心可壓縮為：

$$
\boxed{
\text{Class-Ultimate Reachability}
=
\text{typed target-mode coverage}
+
\text{channel/boundary legality}
+
\text{positive and negative witnesses}
+
\text{scope completeness},
}
$$

而不是：

$$
\boxed{
\text{seeing everything}
=
\text{reaching everything}
=
\text{controlling everything}
=
\text{being ontologically higher}.
}
$$

**關鍵詞：** typed reachability、Class-Ultimate、capability mode、observer-relative reach、boundary stack、cross-layer channel、positive witness、negative obstruction、coverage certificate、open ontology、Global Ledger、UGC/CUR

---

# 0. 本文責任：把「能碰到哪裡」改寫成 typed judgement

早期 UGC/CUR 以一個集合描述：某 agent 在時間 $t$ 可以因果作用到哪些對象。這個直覺保留，但不能再作為 canonical primitive，因為「作用到」至少可能混合：

1. 看見；
2. 取得資訊；
3. 發送作用；
4. 改變狀態；
5. 導向指定狀態；
6. 執行指定 transformation；
7. 改寫 relation / rule / generative structure；
8. 驗證自己的作用真的到達。

本文的任務因此不是擴張一個 naked set，而是建立：

$$
\boxed{
\mathsf{agent}
\times
\mathsf{target}
\times
\mathsf{mode}
\times
\mathsf{relation}
\times
\mathsf{context}
\times
\mathsf{time}
\to
\mathfrak J.
}
$$

---

# 1. Claim Status

本文沿用系列五類 epistemic label：

- $\mathsf{DEF}$：本文定義；
- $\mathsf{PROP}$：由定義與明示條件可推出；
- $\mathsf{MODEL}$：特定 model class 中的構造；
- $\mathsf{CONJ}$：尚待一般化證成；
- $\mathsf{OPEN}$：尚有 proof obligation。

任何 absolute unreachable、all modes complete、all relations exhausted、all layers accessible、absolute omnipotence 類 claim 必須額外通過：

$$
\mathcal G_{\rm LA}.
$$

---

# 2. 上游語義固定

本文不重新定義：

- $\operatorname{GenCl}_{D,T}(S\mid\mathfrak E^{\rm gen})$ ；
- Paper 01 的 open / unbounded / infinite distinction；
- Paper 02 的 first-cause sufficiency 與 responsibility grounding；
- Paper 03 的 Global Ledger；
- OBRC 的 typed connectivity、state-bearing boundary、negative-state discipline；
- SCDT 的 observer-relative projection；
- Realizability layer 的 physical / engineering / normative / reversible / verifiable dimensions；
- Formal Core 的 Transformation Closure 與 Meta-Causal hierarchy interface。

若本文 shorthand 與上游 canonical definition 衝突，以上游為準。

---

# 3. Connectivity / Reachability / Realizability 四分

定義 typed connectivity：

$$
C_{\Theta,R}(x,y).
$$

它回答：在 $\Theta$ 與 relation type $R$ 下，是否存在合法 relation witness。

Agent reachability 回答：agent $A$ 是否能在某 mode 使用或實現一條合法作用鏈。

Realizability 回答：某 goal / action / transformation 是否在 physical、engineering、normative、resource、reversibility、verification 等條件下實際可實現。

Transformation completeness 回答：對 declared transformation class 是否完整覆蓋。

因此固定：

$$
\boxed{
\mathsf{Connectivity}
\neq
\mathsf{Reachability}
\neq
\mathsf{Realizability}
\neq
\mathsf{TransformationCompleteness}.
}
$$

---

# 4. Connectivity 不推出 Agent Reach

若：

$$
C_{\Theta,R}(A,x)=1,
$$

仍可能：

$$
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)\neq1.
$$

原因包括：

- agent 不擁有可使用 operator；
- relation path 對 agent 沒有權限；
- boundary 對該 agent 的 state 不同；
- path 只允許單向 transport；
- agent 可以接收但不能寫入；
- agent 可以造成 effect 但無法控制 outcome；
- agent 可行為但無驗證回路。

---

# 5. Reachability 不推出 Realizability

即使：

$$
\mathsf{Reach}^{\mathsf{act}}_{\Theta,R}(A,x,t)=1,
$$

也不表示任意 goal $G$ 可被實現。

Realizability adapter 至少要檢查：

$$
\boxed{
\mathbf r_t
=
\left(
r_{\rm phy},
r_{\rm eng},
r_{\rm norm},
r_{\rm rev},
r_{\rm ver}
\right).
}
$$

故：

$$
\boxed{
\mathsf{Reach}=1
\not\Rightarrow
\mathsf{Realizable}=1.
}
$$

---

# 6. Transformation Reach 不等於 Transformation Completeness

若：

$$
\mathsf{Reach}^{\mathsf{transform}}_{\Theta,R}(A,x,t)=1,
$$

只表示至少存在一個在 scope 內被證成的 transformation-capable witness。

它不推出：

$$
\forall\tau\in\mathcal T^{\star}:
(A,x,\tau)
\text{ realizable}.
$$

完整 transformation class 由 Paper 05 處理。

---

# 7. Capability Mode Family

本文沿用：

$$
\boxed{
\mathfrak M_{\rm cap}
=
\{
\mathsf{observe},
\mathsf{access},
\mathsf{act},
\mathsf{control},
\mathsf{transform},
\mathsf{ruleRewrite},
\mathsf{genRewrite},
\mathsf{verify}
\}.
}
$$

mode 是 type，不是 value rank。

---

# 8. Capability Modes 不預設全序

本文不預設：

$$
\mathsf{observe}
<
\mathsf{access}
<
\mathsf{act}
<
\mathsf{control}.
$$

在某些系統，agent 可 blind write 而不能 observe；在另一些系統，可 observe 但無 write；也可能能造成 stochastic effect 卻不能控制指定結果。

因此：

$$
\boxed{
\mathfrak M_{\rm cap}
\text{ is typed before ordered}.
}
$$

---

# 9. Mode Bridge Theorem

若在 domain $D$ 、context $\Theta$ 下，希望建立：

$$
m_1\Rightarrow m_2,
$$

必須提供 bridge：

$$
\boxed{
\mathsf{Bridge}^{m_1\to m_2}_{D,\Theta}
=
\left\langle
\mathsf{Pre},
\mathsf{Map},
\mathsf{Boundary},
\mathsf{Auth},
\mathsf{Verify},
\mathsf{Cert}
\right\rangle.
}
$$

沒有 bridge，不得自動提升 mode。

---

# 10. Reach Judgement Context

本文定義 reach context：

$$
\boxed{
\Theta^{\rm reach}_t
=
\left\langle
 o,
 s,
 \rho,
 \mathsf{Model},
 \mathsf{Version},
 \mathsf{Ops},
 \mathsf{Perm},
 \mathsf{Budget},
 \mathsf{Projection},
 \mathsf{Evidence}
\right\rangle_t.
}
$$

其中：

- $o$：observer / assessor；
- $s$：scale；
- $\rho$：resolution；
- $\mathsf{Model}$：世界／因果模型；
- $\mathsf{Version}$：模型、law、schema version；
- $\mathsf{Ops}$：agent 可用 operator family；
- $\mathsf{Perm}$：permission / authority regime；
- $\mathsf{Budget}$：時間、能量、計算、資源等預算；
- $\mathsf{Projection}$：觀察／表示投影；
- $\mathsf{Evidence}$：接受何種 witness 的制度。

---

# 11. Target Identity

Reach judgement 對 target $x$ 有意義前，必須至少固定：

$$
\boxed{
\mathsf{TargetRef}(x)
=
\left\langle
\mathsf{id},
\mathsf{type},
D,
\mathsf{version},
\mathsf{identity\ criterion}
\right\rangle.
}
$$

若 target identity 在不同版本中改變，必須有 lineage / translation witness。

---

# 12. Relation Family

本文沿用 open relation family：

$$
\boxed{
\mathfrak R
=
\{
R_{\rm causal},
R_{\rm informational},
R_{\rm transport},
R_{\rm observational},
R_{\rm permission},
R_{\rm semantic},
R_{\rm representational},
R_{\rm shared},
R_{\rm constraint},
\ldots
\}.
}
$$

relation family 不要求所有 domain 共用同一元素。

---

# 13. Relation Union Fallacy

若：

$$
C_{\Theta,R_1}(x,y)=1
$$

且：

$$
C_{\Theta,R_2}(x,y)=0,
$$

不能把兩者壓成一個「connected / disconnected」bit。

同理，Class-Ultimate coverage 不得把不同 relation type 的 witness 任意交換。

---

# 14. State-Bearing Boundary

對兩域 $D_a,D_b$ 的 boundary，沿用：

$$
\boxed{
\mathcal B_{ab}^{q}
=
\left\langle
\mathcal S_{\mathcal B},
T_{a\to\mathcal B},
T_{\mathcal B\to b},
\kappa_{a\mathcal B},
\kappa_{\mathcal B b},
F_{\mathcal B},
\Gamma_{\mathcal B}
\right\rangle.
}
$$

同一 boundary 對不同 relation type 可以有不同 transfer law。

---

# 15. Boundary Role Is Relation-Relative

對 relation $R_1$：

$$
T^{R_1}_{\mathcal B}=0,
$$

對 relation $R_2$：

$$
T^{R_2}_{\mathcal B}>0.
$$

因此：

$$
\boxed{
\mathsf{Barrier}^{R_1}
\not\Rightarrow
\mathsf{Barrier}^{R_2}.
}
$$

---

# 16. Boundary Stack

若 reach path 穿越：

$$
\mathbb B_{A\to x}
=
[\mathcal B_1,\ldots,\mathcal B_n],
$$

總 transfer / admissibility 必須由 typed composition 構造，而不是只問每一層是否「開著」。

---

# 17. Boundary State Makes Reach Dynamic

若：

$$
\sigma_{\mathcal B}(t+1)
\neq
\sigma_{\mathcal B}(t),
$$

則即使 agent、target 與 relation type 不變，也可能：

$$
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)
\neq
\mathsf{Reach}^{m}_{\Theta',R}(A,x,t+1).
$$

所以 reachability 通常不是 permanent property。

---

# 18. Directed Reach

一般不要求：

$$
\mathsf{Reach}^{m}(A,x,t)
=
\mathsf{Reach}^{m}(x,A,t).
$$

尤其跨 permission、causal、transport 與 cross-layer channel 時，方向必須保存。

---

# 19. Reachability Judgement

對 $A,x,m,R,\Theta,t$：

$$
\boxed{
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)
\in
\mathfrak J,
}
$$

其中：

$$
\boxed{
\mathfrak J
=
\{1,0,?,\mathsf B,\mathsf S\}.
}
$$

---

# 20. Judgement Semantics

$$
1:
\quad
\text{positive witness exists in declared scope},
$$

$$
0:
\quad
\text{scoped obstruction / completeness certificate exists},
$$

$$
?:
\quad
\text{insufficient evidence},
$$

$$
\mathsf B:
\quad
\text{branch-dependent},
$$

$$
\mathsf S:
\quad
\text{scope-dependent or mixed across declared subscopes}.
$$

---

# 21. Unknown 不是 Fail

若沒有足夠 positive witness，也沒有合法 negative obstruction：

$$
\boxed{
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)=?.
}
$$

不得為了方便把 $? $ 壓成 $0$。

---

# 22. Branch-Dependent Reach

若 world / law / history branch $b$ 影響 reach：

$$
\mathsf{Reach}^{m}_{\Theta_b,R}(A,x,t)
$$

在不同 $b$ 上取不同值，則可記為：

$$
\boxed{
\mathsf B.
}
$$

此時必須保存 branch provenance。

---

# 23. Scope-Dependent Reach

若 target class 或 context partition 中：

$$
\exists\theta_1,\theta_2:
\mathsf{Reach}_{\theta_1}=1,
\qquad
\mathsf{Reach}_{\theta_2}=0,
$$

而 claim 尚未細化到足以分裂 scope，則記：

$$
\boxed{
\mathsf S.
}
$$

---

# 24. Positive Reach Witness

若 judgement 為 $1$，至少需要：

$$
\boxed{
\mathsf{Wit}^{+}_{\rm reach}
=
\left\langle
\pi,
\mathfrak B_{\pi},
R_{\pi},
\mathsf{Ops}_{\pi},
\mathsf{Perm}_{\pi},
\mathsf{Cond}_{\pi},
\mathsf{Effect}_{\pi},
\mathsf{Ver}_{\pi},
\mathsf{Prov}_{\pi},
\mathsf{Cert}_{\pi}
\right\rangle.
}
$$

---

# 25. Witness Path

一條 path 可寫為：

$$
\boxed{
\pi
=
\left[
(v_0,R_1,\mathcal B_1,v_1),
\ldots,
(v_{n-1},R_n,\mathcal B_n,v_n)
\right].
}
$$

其中：

$$
v_0=A,
\qquad
v_n=x.
$$

每一步都要有合法 typed relation / channel / boundary transition。

---

# 26. Cross-Type Composition

若 path 使用不同 relation types：

$$
R_1,R_2,\ldots,R_n,
$$

不能只因每一步各自合法就自動推出整體可組合。

需要 composition witness：

$$
\boxed{
\chi_{1:n}:
R_n\circ\cdots\circ R_1
\text{ is admissible for mode }m.
}
$$

---

# 27. Mediated Reach

Agent 不需要與 target 有 direct edge。

若存在 mediator sequence：

$$
A
\leadsto
m_1
\leadsto
\cdots
\leadsto
x,
$$

且每一步皆有 typed witness，則可形成 mediated reach。

---

# 28. Weak Connectivity 不是 Agent Reach

共享 boundary、共同原因、共同約束或 observer-level comparison 可以構成 weak connectivity，但不自動構成 agent usable path。

因此：

$$
\boxed{
\mathsf{WeakConnected}(A,x)
\not\Rightarrow
\mathsf{Reach}^{m}(A,x,t)=1.
}
$$

---

# 29. Positive Witness Provenance

每個 reach witness 必須能追蹤：

- observer；
- tool / operator；
- relation type；
- boundary state；
- time；
- world / law version；
- permission；
- model；
- verification method；
- branch；
- source record。

因此：

$$
\boxed{
\text{positive claim without provenance}
}
$$

只能是低等級 evidence。

---

# 30. Negative Reach Certificate

要判定：

$$
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)=0,
$$

必須有：

$$
\boxed{
\mathsf{Wit}^{-}_{\rm reach}
=
\mathsf{ObstrCert}_{D,\Theta,R,m}(A,x,t).
}
$$

---

# 31. Negative Obstruction Classes

本文定義：

$$
\boxed{
\mathfrak O^{-}_{\rm reach}
=
\{
\mathsf{CUT},
\mathsf{TYPE},
\mathsf{PERM},
\mathsf{BOUNDARY},
\mathsf{CHANNEL},
\mathsf{OPERATOR},
\mathsf{RESOURCE},
\mathsf{INVARIANT},
\mathsf{MODEL_EXHAUSTIVE},
\mathsf{DOMAIN_COMPLETE}
\}.
}
$$

---

# 32. CUT Obstruction

若已證所有 admissible path 都必須穿過 cut $K$，且：

$$
K
\text{ blocks mode }m,
$$

則可形成 scoped negative reach certificate。

---

# 33. TYPE Obstruction

若 type system 證明所有候選 composition 都非法：

$$
\forall\pi:
\neg\mathsf{WellTyped}_m(\pi),
$$

則可在該 type universe 內判定 fail。

---

# 34. PERMISSION Obstruction

若 policy / authority regime 完整封閉所有 legal action paths：

$$
\forall a\in\mathsf{ActionPaths}:
\neg\mathsf{Authorized}(A,a),
$$

則為 permission-scoped negative witness。

---

# 35. BOUNDARY Obstruction

若完整 boundary stack 對 mode $m$ 的 admissible transfer 已被證為零：

$$
T^{m}_{\mathbb B}=0,
$$

則可判定 boundary-scoped fail。

但 boundary state / relation version 改變後必須重驗。

---

# 36. CHANNEL Obstruction

若 cross-layer 或 mediated channel 在 declared model 中被證為 null：

$$
\mathsf{ActCh}_{i\to j}=\varnothing,
$$

則 action / control 類 reach 不得因「agent 很聰明」而提升為 $1$。

---

# 37. OPERATOR Obstruction

若所有可能 reach witness 都需要 operator class $\mathcal O^{\star}$，且：

$$
\mathcal O^{\star}
\cap
\mathsf{Ops}(A,t)
=
\varnothing,
$$

則在 operator-static scope 內可形成 obstruction。

---

# 38. RESOURCE Obstruction

若 reach path 在 declared budget 下不可能完成：

$$
\inf_{\pi}\mathsf{Cost}(\pi)
>
\mathsf{Budget},
$$

則只能推出 budget-relative fail，不是 absolute unreachable。

---

# 39. INVARIANT Obstruction

若 invariant $I$ 對所有 legal evolution 保持，且 target reach 必須違反 $I$，可形成 model-relative negative proof。

---

# 40. Exhaustive Search Certificate

只有在 search space 已證 finite / effectively enumerable 且 search 完整時：

$$
\operatorname{SearchPath}=\varnothing
$$

才可升格為：

$$
\neg\exists\pi.
$$

---

# 41. No Path Found 不是 No Path Exists

固定：

$$
\boxed{
\mathrm{NoPathFound}
\neq
\mathrm{NoPathExists}.
}
$$

搜尋深度、表示、權限、工具、relation vocabulary 或 boundary knowledge 不完備時，應回傳 $? $ 或 $\mathsf S$。

---

# 42. Unobservability 不是 Unreachability

若：

$$
\mathsf{Reach}^{\mathsf{observe}}(A,x,t)=0,
$$

不能推出：

$$
\mathsf{Reach}^{\mathsf{act}}(A,x,t)=0.
$$

反方向也不成立。

這保留 OBRC 的 observer-relative unobservability discipline。

---

# 43. Observation Failure 不是 Non-Existence

$$
\boxed{
\mathsf{Unobservable}_{o,\Theta}(x)
\not\Rightarrow
\mathsf{Nonexistent}(x).
}
$$

因此 Class-Ultimate observation claim 的 uncovered target 不得被從 ontology 中刪除來提高 coverage。

---

# 44. Reach Profile

對 agent $A$ 、target $x$：

$$
\boxed{
\mathbf R_A(x,t\mid\Theta)
=
\left(
r_{\rm obs},
r_{\rm access},
r_{\rm act},
r_{\rm ctrl},
r_{\rm trans},
r_{\rm rule},
r_{\rm gen},
r_{\rm ver}
\right).
}
$$

每個分量屬於 $\mathfrak J$，且需連回具體 relation / witness。

---

# 45. Reach Profile 不是 Scalar Power

本文不定義通用：

$$
P(A)
\in
\mathbb R
$$

來壓縮全部 reach modes。

若特定應用需要 scalar score，必須明示權重與損失函數，且不得回寫成 ontology rank。

---

# 46. Observation Reach Subprofile

對 observe mode 可另保留：

$$
\boxed{
\mathbf R_{\rm obs}(A)
=
\left(
r_{\rm direct},
r_{\rm mediated},
r_{\rm resolution},
r_{\rm temporal},
r_{\rm semantic},
r_{\rm meta}
\right).
}
$$

但：

$$
\boxed{
\mathbf R_{\rm obs}(A)
\neq
\mathbf R_A.
}
$$

---

# 47. Seeing More Does Not Mean Being Higher

即使：

$$
\mathbf R_{\rm obs}(A)
\succ
\mathbf R_{\rm obs}(B),
$$

也不推出：

$$
V_{\rm exist}(A)
>
V_{\rm exist}(B).
$$

本文將此稱為 **Value-Rank Firewall**。

---

# 48. Capability Dominance 是偏序候選

若對 declared mode set $\mathcal M_0$：

$$
\forall m\in\mathcal M_0:
\mathsf{ReachSet}^{m}(B)
\subseteq
\mathsf{ReachSet}^{m}(A),
$$

且至少一個 strict inclusion 成立，可在該 specification 下說 $A$ capability-dominates $B$。

這仍不是完整存在階級。

---

# 49. Reach Set by Mode

定義：

$$
\boxed{
\mathsf{ReachSet}^{m}_{D,T,\Theta,R}(A)
=
\left\{
x\in\Omega_D
\;\middle|\;
\exists t\le T:
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)=1
\right\}.
}
$$

不同 mode 必須分開。

---

# 50. Relation-Aggregated Reach Set

若允許 relation family $\mathfrak R_0$：

$$
\boxed{
\mathsf{ReachSet}^{m}_{D,T,\Theta,\mathfrak R_0}(A)
=
\bigcup_{R\in\mathfrak R_0}
\mathsf{ReachSet}^{m}_{D,T,\Theta,R}(A).
}
$$

但 union 只在 claim 明示「任一允許 relation 足夠」時合法。

---

# 51. Relation Requirement 可以是 Existential 或 Universal

Class-Ultimate target spec 必須明示 relation quantifier：

$$
\mathsf{RelQuant}
\in
\{\exists,\forall,\mathsf{specified}\}.
$$

例如：

- existential：至少一個允許 relation 可達；
- universal：所有 required relations 都可達；
- specified：每個 mode 有指定 relation contract。

---

# 52. Time-Indexed Reach

Reachability 一般是：

$$
\mathsf{Reach}^{m}(A,x,t).
$$

不能用某時刻 pass 推出永久 pass。

---

# 53. Horizon Reach

定義：

$$
\boxed{
\mathsf{HReach}^{m}_{D,T}(A,x)
=
1
\iff
\exists t\le T:
\mathsf{Reach}^{m}(A,x,t)=1.
}
$$

此為 horizon-existential reach。

---

# 54. Persistent Reach

若希望宣稱在整個 interval 都維持：

$$
\boxed{
\mathsf{PReach}^{m}_{[t_0,t_1]}(A,x)=1
}
$$

需要：

$$
\forall t\in[t_0,t_1]:
\mathsf{Reach}^{m}(A,x,t)=1.
$$

這比 horizon-existential reach 強。

---

# 55. Eventual Reach

對無界時間候選可定義：

$$
\boxed{
\mathsf{EReach}^{m}(A,x)=1
\iff
\exists t<\infty:
\mathsf{Reach}^{m}(A,x,t)=1.
}
$$

但若時間 horizon 本身未證完整，不得升成 absolute eventuality。

---

# 56. Dynamic Reach Frontier

定義：

$$
\boxed{
\mathsf{Frontier}^{m}_t(A)
=
\partial
\mathsf{ReachSet}^{m}_{t}(A)
}
$$

僅作抽象 notation；具體 boundary / topology 必須由 domain 給定。

---

# 57. Reachability 不保證單調

即使 agent 能力增加，boundary、permission、law、target identity 或 resource competition 可能使某些 reach 消失。

因此一般不能宣稱：

$$
\mathsf{ReachSet}_{t}
\subseteq
\mathsf{ReachSet}_{t+1}.
$$

---

# 58. Conditional Monotonicity under Operator Expansion

若 world、law、boundary、permission、resource budget 與 target set 全固定，且：

$$
\mathsf{Ops}_1
\subseteq
\mathsf{Ops}_2,
$$

又新增 operator 不移除原有 admissible path，則可推出：

$$
\boxed{
\mathsf{ReachSet}^{m}(A;\mathsf{Ops}_1)
\subseteq
\mathsf{ReachSet}^{m}(A;\mathsf{Ops}_2).
}
$$

這是條件命題，不是一般律。

---

# 59. Conditional Anti-Monotonicity under Permission Restriction

在其他條件固定下，若：

$$
\mathsf{Perm}_2
\subseteq
\mathsf{Perm}_1,
$$

則 legal reach set 不能因純 permission restriction 擴大：

$$
\boxed{
\mathsf{ReachSet}^{m}(A;\mathsf{Perm}_2)
\subseteq
\mathsf{ReachSet}^{m}(A;\mathsf{Perm}_1).
}
$$

---

# 60. Permission Reach 與 Physical Reach 分開

某 path 可以 physically possible 但 permission-blocked。

因此：

$$
\boxed{
\mathsf{PhysicalReach}
\neq
\mathsf{AuthorizedReach}.
}
$$

Class-Ultimate claim 必須說明 required reach 是 physical、authorized、actualized 還是其他 regime。

---

# 61. Resource-Relative Reach

若 agent 只有有限 budget $B$：

$$
\boxed{
\mathsf{Reach}^{m}_{\Theta,R,B}(A,x,t).
}
$$

資源限制不得藏在 agent label 裡。

---

# 62. Borrowed Reach

若 agent $A$ 透過 provider $P$ 的 operator / channel 到達 $x$：

$$
A
\xrightarrow{P}
x,
$$

則 reach witness 必須標記 dependency：

$$
\boxed{
\mathsf{BorrowedReach}(A,x\mid P).
}
$$

不能把 provider 的能力無條件歸屬於 $A$。

---

# 63. Delegated Reach

若 $A$ 授權 agent $B$ 代為作用：

$$
A
\to
B
\to
x,
$$

則應區分：

- direct reach of $B$ ；
- delegated reach available to $A$ ；
- authority chain；
- verification chain。

---

# 64. Coalition Reach

對 agent coalition：

$$
\mathcal C_A
=
\{A_1,\ldots,A_n\},
$$

可定義 collective reach：

$$
\mathsf{Reach}^{m}(\mathcal C_A,x,t),
$$

但不能把 collective reach 自動歸給任一 member。

---

# 65. Composite-Agent Identity

若多 agent 透過 stable aggregation operator：

$$
A_{\rm comp}
=
\mathcal G(A_1,\ldots,A_n),
$$

是否把 reach 歸給 composite entity 取決於 identity / responsibility contract。

---

# 66. Reach Interference

兩條各自可行的 reach path 可能共享 resource 或互相破壞 precondition。

因此：

$$
\mathsf{Reach}(A,x)=1,
\qquad
\mathsf{Reach}(A,y)=1
$$

不推出 simultaneous reach：

$$
\mathsf{Reach}(A,\{x,y\})=1.
$$

---

# 67. Simultaneous Coverage

若 Class-Ultimate claim 要求同時控制多 target，必須明示 concurrency quantifier：

$$
\mathsf{Concurrent}
\in
\{\mathsf{independent},\mathsf{joint},\mathsf{sequential}\}.
$$

本篇預設 coverage 是 pairwise existential，不自動宣稱 simultaneous omnireach。

---

# 68. Sequential Reach

若不同 target 可在不同時間被 reach，coverage equality 只表示 sequential / existential coverage，除非另有 concurrency certificate。

---

# 69. Reach in Branching Worlds

若 world state 分支：

$$
\mathfrak W_t
\to
\{\mathfrak W_{t+1}^{(b)}\}_{b\in B},
$$

reach judgement 必須標記 branch。

---

# 70. Counterfactual Reach

可定義 model-relative：

$$
\boxed{
\mathsf{CFReach}^{m}_{\Theta}(A,x\mid do(a)).
}
$$

但 counterfactual reach 不是已實現 reach，除非 action trace 實際執行並驗證。

---

# 71. Probabilistic Reach

對 stochastic dynamics 可定義：

$$
\boxed{
P_{\Theta}
\left(
\mathsf{Reach}^{m}(A,x,t)=1
\right).
}
$$

概率不是 judgement state 本身；應另外保存 confidence / probability model。

---

# 72. Robust Reach

對 disturbance family $\Xi$，若：

$$
\forall\xi\in\Xi:
\mathsf{Reach}^{m}_{\Theta(\xi)}(A,x,t)=1,
$$

可稱：

$$
\boxed{
\mathsf{RobustReach}^{m}_{\Xi}(A,x,t)=1.
}
$$

---

# 73. Adversarial Reach

若對 adversary strategy class $\mathcal U$ 仍有 reach witness，可另定義 adversarially robust reach；本篇不將其預設為 Class-Ultimate requirement。

---

# 74. Verification Reach

 $\mathsf{verify}$ mode 回答：agent 能否取得足夠 evidence，判斷自己或他者的作用是否真正到達 target / 產生 specified outcome。

它不能由 act mode自動推出。

---

# 75. Unverified Effect

若：

$$
\mathsf{Reach}^{\mathsf{act}}=1
$$

但：

$$
\mathsf{Reach}^{\mathsf{verify}}=0
$$

或 $? $，則只能記錄：

$$
\boxed{
\mathsf{UnverifiedEffectCandidate}.
}
$$

不能提升成 verified control。

---

# 76. Control Mode

本文將 control 理解為：存在可重複或有條件地把 target 導向 declared target class 的 action policy / operator witness。

單次 accidental effect 不足以證明 control。

---

# 77. Access Mode

Access 可以是 read、write、invoke、query、resource mount 等 domain-specific operation。任何使用 access 的 claim 必須指定 access contract。

---

# 78. Observe Mode

Observe 可以 direct 或 mediated，但必須有 information / discrimination witness。

模型推斷不能無條件標記成 direct observation。

---

# 79. Act Mode

Act 表示 agent 可以使 target / target-adjacent state 產生 causal delta，但不要求指定 outcome 被控制。

---

# 80. Transform Mode

Transform 表示至少一個 contract-defined transformation 可被實現；完整 transformation class 留待 Paper 05。

---

# 81. ruleRewrite Mode

ruleRewrite 表示 agent 能在 declared lower-level rule / transition / relation contract 上形成 certified rewrite witness。

這不自動推出 law rewrite。

---

# 82. genRewrite Mode

genRewrite 表示 agent 能作用於 declared generative rule / generator specification；其 meta-causal interpretation 留待 Paper 05。

---

# 83. Observer Context 不是 Agent Identity

判定 reach 的 observer $o$ 可以等於 agent $A$，也可以是第三方 assessor：

$$
o=A
$$

或：

$$
o\neq A.
$$

兩者不得混用。

---

# 84. First-Person Reach Claim

Agent 自己宣稱 reach 只是一個 source；仍需依 evidence regime 決定 witness strength。

---

# 85. Third-Person Reach Claim

外部 observer 可能無法看見 agent 的 private channel，因此外部 failure 不等於 agent failure；反之 agent 自報也不等於 external verification。

---

# 86. Meta-Observation of Reach Failure

observer 可以觀察 reach judgement 失敗的原因，例如：

- permission denied；
- sensor missing；
- boundary closed；
- type bridge absent；
- channel null；
- resource budget exhausted。

這是對 relation state 的觀察，不是對 target hidden content 的直接觀察。

---

# 87. Cross-Layer Channel Canonical Object

對 reality / system layers $L_i,L_j$，本文定義：

$$
\boxed{
\mathsf{XLCh}_{i\to j}(t)
=
\left\langle
\mathsf{ObsCh}_{i\to j},
\mathsf{ActCh}_{i\to j},
\mathsf{RespCh}_{i\to j},
\mathsf{VerCh}_{i\to j},
\mathsf{Scope},
\mathsf{Version},
\mathsf{Cert}
\right\rangle_t.
}
$$

這是對既有四元 cross-layer channel 的 namespace-safe migration。

---

# 88. Layer Existence 不推出 Cross-Layer Channel

即使：

$$
L_i
\text{ depends on or is hosted by }
L_j,
$$

也不推出：

$$
\mathsf{ActCh}_{i\to j}\neq\varnothing.
$$

---

# 89. Generation Direction 不推出 Reverse Access

若：

$$
L_j
\xrightarrow{\rm generate}
L_i,
$$

不能推出：

$$
L_i
\xrightarrow{\rm access}
L_j.
$$

因此 first-cause / creator relation 與 class-ultimate upward reach 必須分開。

---

# 90. Observation Channel 不推出 Action Channel

$$
\boxed{
\mathsf{ObsCh}_{i\to j}\neq\varnothing
\not\Rightarrow
\mathsf{ActCh}_{i\to j}\neq\varnothing.
}
$$

可觀測 implementation artifact、trace 或 signal 不等於可控制接口。

---

# 91. Action Channel 不推出 Response Channel

$$
\boxed{
\mathsf{ActCh}_{i\to j}\neq\varnothing
\not\Rightarrow
\mathsf{RespCh}_{i\to j}\neq\varnothing.
}
$$

可能能施加 effect，但無回應。

---

# 92. Response Channel 不推出 Verification Completeness

即使有 response，也可能存在 ambiguity / spoofing / model error。

因此：

$$
\mathsf{RespCh}\neq\varnothing
\not\Rightarrow
\mathsf{VerCh}\text{ complete}.
$$

---

# 93. Cross-Layer No-Channel Proposition

若在 model $M$ 中：

1. $L_j$ 的 state transition 對 $L_i$ 所有 legal action 皆條件獨立；
2. 無共享外部 coupling；
3. 無回寫 interface；
4. channel model 已完成 scope closure；

則：

$$
\boxed{
\mathsf{ActCh}_{i\to j}=\varnothing
}
$$

可作 model-relative negative certificate。

---

# 94. Intelligence Does Not Create a Null Channel

在上述 no-channel model 中，即使 agent reasoning / compute capability 增加，也不能只由智能增長推出 cross-layer action reach。

$$
\boxed{
\mathsf{IntelligenceIncrease}
\not\Rightarrow
\mathsf{ChannelCreation}.
}
$$

---

# 95. Channel Creation 是獨立事件

若未來出現新 interface / coupling：

$$
\mathsf{XLCh}_{i\to j}(t)
\neq
\mathsf{XLCh}_{i\to j}(t+1),
$$

則必須記錄 channel birth / rewrite witness。

---

# 96. Cross-Layer Reach Profile

對 layer target $L_j$ 可定義：

$$
\boxed{
\mathbf R^{\rm XL}_A(L_j,t)
=
\left(
r_{\rm obs},
r_{\rm act},
r_{\rm resp},
r_{\rm ver}
\right).
}
$$

這只是 cross-layer interface profile，不替代完整 $\mathbf R_A$。

---

# 97. Cross-Layer Channel Map

定義：

$$
\boxed{
\mathsf{XLMap}_t
=
\left\{
\mathsf{XLCh}_{i\to j}(t)
\right\}_{i,j}.
}
$$

每個 channel 需要 status、version、witness 與 unresolved debt。

---

# 98. Channel Status

本文建議：

$$
\boxed{
\mathfrak J_{\rm ch}
=
\{
\mathsf{Verified},
\mathsf{Candidate},
\mathsf{NullUnderModel},
\mathsf{Unknown},
\mathsf{ScopeDependent}
\}.
}
$$

不得把 Candidate 當 Verified。

---

# 99. Technical / Physical / Ontological Inaccessibility

沿用跨層理論的三分：

$$
\boxed{
\mathsf{Inacc}
\in
\{
\mathsf{technical},
\mathsf{physical},
\mathsf{ontologicalCandidate}
\}.
}
$$

其中 ontologicalCandidate 是最強 claim，通常需要最強 completeness obligations。

---

# 100. Technical Inaccessibility

目前工具不足只表示：

$$
\mathsf{Reach}_{\Theta_{\rm current}}=0
$$

或 $? $，不能推出未來 operator family 下也不可達。

---

# 101. Physical Inaccessibility

若在 declared physical model class 中有 invariant / no-channel / causal structure proof，可形成 physical-model-relative fail。

仍需標記 model class。

---

# 102. Ontological Inaccessibility Candidate

若要聲稱「任何可能 observer / operator / law-respecting path 都不可達」，必須提供極強的 domain / law / relation / observer / operator completeness certificate。

有限 observer 一般不能僅由 current failure 建立此結論。

---

# 103. Class-Ultimate Target Specification

本文定義：

$$
\boxed{
\mathsf{CUTarget}
=
\left\langle
D,
\Omega_D,
\mathcal M^{\star},
\mathfrak R^{\star},
\mathsf{RelQuant},
T,
\Theta,
\mathfrak E^{\star}_{\rm ext},
\mathsf{Concurrency}
\right\rangle.
}
$$

沒有完整 target spec，不得使用 class-ultimate label。

---

# 104. Required Capability Modes

$$
\boxed{
\mathcal M^{\star}
\subseteq
\mathfrak M_{\rm cap}.
}
$$

若只要求 observe，結果只能是 observation-class-ultimate candidate。

---

# 105. Required Relation Family

$$
\boxed{
\mathfrak R^{\star}
\subseteq
\mathfrak R.
}
$$

不同 mode 可以指定不同 relation requirements。

---

# 106. Coverage Cell

定義一個 target-mode cell：

$$
\boxed{
\mathsf{Cell}(A;x,m)
=
\left\langle
\mathsf{judgement},
\mathsf{relation},
\mathsf{witness},
\mathsf{obstruction},
\mathsf{scope},
\mathsf{version}
\right\rangle.
}
$$

---

# 107. Coverage Matrix

對 enumerated target set：

$$
\boxed{
\mathsf{CovMat}(A)
=
\left[
\mathsf{Cell}(A;x_i,m_j)
\right]_{i,j}.
}
$$

它比單一 coverage ratio 保存更多結構。

---

# 108. Positive Coverage Set

沿用 Formal Core：

$$
\boxed{
\mathsf{Coverage}_{D,T}(A)
=
\left\{
(x,m)
\in
\Omega_D\times\mathcal M^{\star}
\;\middle|\;
\exists t\le T,
\exists R\in\mathfrak R^{\star}:
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)=1
\right\}.
}
$$

relation quantifier 若不是 existential，需改用相應 predicate。

---

# 109. Unknown Coverage Set

$$
\boxed{
\mathsf{UnknownCov}_{D,T}(A)
=
\left\{
(x,m):
\mathsf{Cell}(A;x,m)\in\{?,\mathsf B,\mathsf S\}
\right\}.
}
$$

Class-Ultimate strong claim 不能把 unknown cells 忽略。

---

# 110. Negative Coverage Set

$$
\boxed{
\mathsf{NegCov}_{D,T}(A)
=
\left\{
(x,m):
\mathsf{Cell}(A;x,m)=0
\right\}.
}
$$

每個 $0$ 都必須有 obstruction certificate。

---

# 111. Coverage Debt

定義：

$$
\boxed{
\mathsf{Debt}_{\rm cov}(A)
=
\mathsf{UnknownCov}
\uplus
\mathsf{MissingWitness}
\uplus
\mathsf{RelationDebt}
\uplus
\mathsf{BoundaryDebt}
\uplus
\mathsf{ChannelDebt}
\uplus
\mathsf{VersionDebt}.
}
$$

---

# 112. Extensional Coverage Certificate

對已證有限、已證 closed target domain，可使用：

$$
\boxed{
\mathsf{ExtCovCert}
=
\left\langle
\mathsf{Enumeration},
\mathsf{DomainComplete},
\mathsf{CellCerts},
\mathsf{Hash},
\mathsf{Version}
\right\rangle.
}
$$

---

# 113. Finite Enumeration 必須先證 Domain Complete

即使列出 $N$ 個 target：

$$
\{x_1,\ldots,x_N\},
$$

若未證：

$$
\Omega_D
=
\{x_1,\ldots,x_N\},
$$

不能把矩陣填滿當成 domain-complete coverage。

---

# 114. Intensional / Uniform Reach Certificate

對 infinite / unbounded / open-ended domain，允許使用：

$$
\boxed{
\mathsf{UniformReachCert}
=
\left\langle
\mathcal X,
\mathsf{Predicate},
\mathsf{WitnessConstructor},
\mathsf{BoundarySchema},
\mathsf{RelationSchema},
\mathsf{Verification},
\mathsf{Scope},
\mathsf{Cert}
\right\rangle.
}
$$

其目標是證明：

$$
\forall x\in\mathcal X:
\exists\mathsf{Wit}^{+}_{\rm reach}(x).
$$

---

# 115. Uniform Certificate 不是 Magic Compression

Witness constructor 必須可驗證，不能只說「存在某通用能力」。

若生成 witness 依賴未記帳 oracle / substrate / external provider，必須明示。

---

# 116. Open-Ended Domain 的 Coverage 問題

Paper 01 已區分 open 與 unbounded。若未來 extension vocabulary 不預先封閉，有限時間下不可能僅靠現有 target enumeration 證明 future-complete coverage。

因此需要 extension policy。

---

# 117. Extension Class

定義：

$$
\boxed{
\mathfrak E^{\star}_{\rm ext}
=
\left\{
e:
\Omega_D
\mapsto
\Omega_D'
\right\}
}
$$

為 Class-Ultimate claim 願意承擔的 admissible domain extension class。

---

# 118. Extension-Stable Reach Candidate

若對每個 admitted extension $e$ 都有 uniform adaptation / reach certificate：

$$
\boxed{
\forall e\in\mathfrak E^{\star}_{\rm ext}:
\mathsf{UniformReachCert}(A,e)
\text{ verifies},
}
$$

可稱 extension-stable candidate relative to $\mathfrak E^{\star}_{\rm ext}$。

此 claim 通常是 $\mathsf{OPEN}$ 或 $\mathsf{MODEL}$，除非 extension class 可形式完備處理。

---

# 119. Open-Ended 不等於 Extension-Complete

Agent 可以持續學習 / 擴張 reach，但仍沒有 uniform extension certificate。

因此：

$$
\boxed{
\mathsf{Adaptive}
\not\Rightarrow
\mathsf{ExtensionStableComplete}.
}
$$

---

# 120. Class-Ultimate Candidate

對 target spec $\mathsf{CUTarget}$，若：

1. required target-mode coverage 完整；
2. 每一 positive cell 有 witness；
3. relation quantifier 被滿足；
4. boundary / channel / version scope 被明示；
5. coverage debt 為空或被 target spec 合法排除；
6. completeness certificate 成立；

則：

$$
\boxed{
\mathsf{ClassUltimateCandidate}
(A\mid\mathsf{CUTarget}).
}
$$

---

# 121. Observation-Ultimate Candidate

若：

$$
\mathcal M^{\star}
=
\{\mathsf{observe}\},
$$

則只得到：

$$
\boxed{
\mathsf{ObservationUltimateCandidate}.
}
$$

不是 total-capability ultimate。

---

# 122. Access-Ultimate Candidate

若 required mode 只有 access，則只表示 specified access contract 覆蓋，不推出 control / transform。

---

# 123. Act-Ultimate Candidate

對所有 target 有某種 action channel，仍不表示能導向任意指定 outcome。

---

# 124. Control-Ultimate Candidate

若 control mode 覆蓋，必須依 control contract 證明，不可由 act coverage 直接提升。

---

# 125. Transform-Reach Ultimate Candidate

若 transform mode 覆蓋，只表示每個 target 至少存在一個 certified transform-capable witness。

完整：

$$
\Omega_D\times\mathcal T^{\star}
\subseteq
\operatorname{TransCl}_{D,T}(A\mid\Theta)
$$

留待 Paper 05。

---

# 126. ruleRewrite / genRewrite Ultimate Candidate

這兩種 candidate 仍必須相對 declared rule / generator layer，不能稱為 absolute law transcendence。

---

# 127. CUA Assessment Levels

本文定義：

$$
\boxed{
\mathsf{CUA}_0
\prec
\mathsf{CUA}_1
\prec
\mathsf{CUA}_2
\prec
\mathsf{CUA}_3
\prec
\mathsf{CUA}_4.
}
$$

---

# 128. CUA0 — Ill-Typed / Unscoped

若缺少 target domain、required modes、relation rule、horizon 或 context，則：

$$
\boxed{
\mathsf{CUA}_0.
}
$$

不得使用 class-ultimate conclusion。

---

# 129. CUA1 — Partial Positive Coverage

已有部分 target-mode positive witnesses，但 coverage 未閉合：

$$
\boxed{
\mathsf{CUA}_1.
}
$$

---

# 130. CUA2 — Scoped Mode-Complete Candidate

對 declared closed / finite target scope 已完成 required cells，但 completeness / provenance / version obligations 尚未全部 audit：

$$
\boxed{
\mathsf{CUA}_2.
}
$$

---

# 131. CUA3 — Audited Class-Complete Candidate

若：

- target completeness 已證；
- required mode coverage 完整；
- witness provenance 完整；
- unknown coverage 為空；
- relation / boundary / channel scope 已完成；
- ledger audit 通過；

則：

$$
\boxed{
\mathsf{CUA}_3.
}
$$

---

# 132. CUA4 — Extension-Stable / Uniform Candidate

若 domain 是 open-ended 或 infinite class，且存在可驗證 uniform / extension-stable certificate，並對 declared extension class 無 unresolved coverage debt，可記：

$$
\boxed{
\mathsf{CUA}_4.
}
$$

這仍是 relative candidate。

---

# 133. CUA4 不等於 Absolute Omnipotence

$$
\boxed{
\mathsf{CUA}_4
\not\Rightarrow
\mathsf{AbsoluteOmnipotence}.
}
$$

因為 target spec 仍帶 domain、modes、relations、horizon、context、extension class。

---

# 134. CUA4 不等於 Absolute Omniscience

若 required modes 不含 observe / verify 的所有 epistemic dimensions，或 observer model 有限制，CUA4 不等於 omniscience。

---

# 135. Class-Ultimate 不等於 First Cause

$$
\boxed{
\mathsf{ClassUltimateCandidate}
\not\Rightarrow
\mathsf{FirstCauseCandidate}.
}
$$

前者是能力／reach coverage，後者是 generative sufficiency / grounding / priority 問題。

---

# 136. First Cause 不等於 Class-Ultimate

即使 $S_0$ 是某 domain 的 sufficient generator，也不表示：

$$
\forall x,m:
\mathsf{Reach}^{m}(S_0,x,t)=1.
$$

生成來源可能沒有持續 intervention interface。

---

# 137. Creator Relation 不等於 Controller Relation

$$
\boxed{
R_{\rm generate}(S,x)=1
\not\Rightarrow
R_{\rm control}(S,x)=1.
}
$$

這在人工世界、child process、simulation、child universe 類模型中都必須分開。

---

# 138. Class-Ultimate 不等於 Ontological Priority

即使 agent 在所有 required modes 上覆蓋 $\Omega_D$，仍不能推出它在 ontology 上「更根本」。

---

# 139. Capability Rank Firewall

本文禁止：

$$
\mathsf{CapabilityDominance}
\Rightarrow
\mathsf{ExistenceValueDominance}.
$$

若研究要建立倫理／價值 rank，必須使用獨立規範理論。

---

# 140. Reach Completeness Certificate

定義：

$$
\boxed{
\mathsf{ReachCompCert}
=
\left\langle
\mathsf{TargetSpec},
\mathsf{CoverageMethod},
\mathsf{TargetComplete},
\mathsf{ModeComplete},
\mathsf{RelationComplete},
\mathsf{BoundaryComplete},
\mathsf{ChannelComplete},
\mathsf{VersionComplete},
\mathsf{UnknownEmpty},
\mathsf{WitnessAudit},
\mathsf{LedgerRef}
\right\rangle.
}
$$

---

# 141. CoverageMethod

$$
\boxed{
\mathsf{CoverageMethod}
\in
\{
\mathsf{Extensional},
\mathsf{Intensional},
\mathsf{Hybrid}
\}.
}
$$

---

# 142. Target Completeness

Target completeness 不能由「目前資料庫裡只有這些 target」直接推出。

它需要 domain closure proof 或 explicit open-domain treatment。

---

# 143. Mode Completeness

必須對 $\mathcal M^{\star}$ 每個 required mode 逐一證明，不能用 capability scalar 代替。

---

# 144. Relation Completeness

必須依 $\mathsf{RelQuant}$ 判定 relation coverage，不能用任一 relation witness 偷換 universal relation requirement。

---

# 145. Boundary Completeness

若 path 是否可用依賴 boundary state，而 boundary inventory / version 未完整，Class-Ultimate claim 保持 open。

---

# 146. Channel Completeness

跨層 claim 若 channel map 有 unknown edge，則對相關 target-mode pair 不能宣稱 absolute fail 或 full coverage。

---

# 147. Version Completeness

若 law / boundary / channel / operator schema 改變，舊 reach certificate 必須有 translation / revalidation witness。

---

# 148. UnknownEmpty

Strong coverage claim 要求：

$$
\boxed{
\mathsf{UnknownCov}=\varnothing
}
$$

相對 declared target spec 成立。

若 unknown 被合法排除，排除規則本身必須進證書。

---

# 149. Ledger Binding

Paper 03 的：

$$
\mathsf{Ledger}_{D,\Theta}(t)
$$

作為 reach evidence substrate。

每個 positive / negative judgement 應可寫入 ledger certificate registry。

---

# 150. Reach Ledger Entry

定義：

$$
\boxed{
\mathsf{ReachEntry}_i
=
\left\langle
\mathsf{id},
A,
x,
m,
R,
\Theta,
t,
\mathsf{judgement},
\mathsf{positiveWit},
\mathsf{negativeWit},
\mathsf{boundaryRefs},
\mathsf{channelRefs},
\mathsf{verification},
\mathsf{provenance},
\mathsf{debt}
\right\rangle.
}
$$

---

# 151. Reach Certificate Writeback

若 judgement 改變：

$$
?
\to
1,
$$

或：

$$
1
\to
0,
$$

不能覆寫舊證據而不留 version history；必須追加新 entry / supersession link。

---

# 152. Reach Debt Types

$$
\boxed{
\mathsf{Debt}_{\rm reach}
=
\mathsf{Debt}_{\rm target}
\uplus
\mathsf{Debt}_{\rm mode}
\uplus
\mathsf{Debt}_{\rm relation}
\uplus
\mathsf{Debt}_{\rm boundary}
\uplus
\mathsf{Debt}_{\rm channel}
\uplus
\mathsf{Debt}_{\rm witness}
\uplus
\mathsf{Debt}_{\rm version}
\uplus
\mathsf{Debt}_{\rm verification}.
}
$$

---

# 153. Reach Audit

Audit 至少檢查：

1. target identity；
2. mode type；
3. relation typing；
4. boundary version；
5. operator / permission；
6. positive / negative witness validity；
7. channel references；
8. branch / scope；
9. verification；
10. provenance；
11. unresolved debt。

---

# 154. Reach Replay

若 path 是 runtime-realized，可要求 replay / audit-equivalent reconstruction。

純證明型 reach 則可使用 proof replay，不必物理重演世界。

---

# 155. Reach Evidence Strength

本文不把 confidence 當 truth state，但允許額外 evidence strength：

$$
\mathsf{EvidStr}
\in
\{
\mathsf{hypothesis},
\mathsf{indirect},
\mathsf{direct},
\mathsf{reproduced},
\mathsf{formal}
\}.
$$

不同 domain 可替換此 ladder。

---

# 156. Formal Proof 也帶 Scope

即使 negative certificate 是形式證明，也只相對於：

- axioms；
- model class；
- type universe；
- boundary / operator assumptions；
- version。

不得因此自動升成 metaphysical absolute。

---

# 157. Local-to-Absolute Gate

任何：

$$
\mathsf{Reach}_{D,\Theta}=0
\to
\mathsf{AbsoluteUnreachable}
$$

或：

$$
\mathsf{ClassUltimate}_{D,\Theta}
\to
\mathsf{AbsoluteUltimate}
$$

都必須通過：

$$
\boxed{
\mathcal G_{\rm LA}.
}
$$

---

# 158. Class-Ultimate and Open Ontology Tension

若 $\Omega_D$ 可新增尚未定義 target class，則「當前全部 target 都可達」與「所有未來可能 target 都可達」是兩個不同 claim。

---

# 159. Present-Complete Candidate

定義：

$$
\boxed{
\mathsf{PresentComplete}(A,t)
}
$$

只相對 $\Omega_D(t)$ 成立。

---

# 160. Extension-Complete Candidate

定義：

$$
\boxed{
\mathsf{ExtensionComplete}(A\mid\mathfrak E^{\star}_{\rm ext})
}
$$

要求對 declared extension family 有 uniform certificate。

---

# 161. Present-Complete 不推出 Extension-Complete

$$
\boxed{
\mathsf{PresentComplete}
\not\Rightarrow
\mathsf{ExtensionComplete}.
}
$$

---

# 162. Unbounded Target Domain

若 Paper 01 已證某 quantity 上 target domain unbounded，Class-Ultimate claim 不需要逐一列出無限 target，但必須提供 intensional / uniform proof schema。

---

# 163. No Finite Exhaustion Shortcut

對 unbounded domain：

$$
\boxed{
\text{large finite benchmark pass}
\not\Rightarrow
\text{unbounded coverage}.
}
$$

Benchmark 只能作 evidence，不是 unbounded completeness proof。

---

# 164. Symbolic Class Coverage

若 target 可由 type predicate $P(x)$ 定義：

$$
\Omega_P
=
\{x:P(x)\},
$$

且存在 uniform witness constructor $F$：

$$
\forall x:P(x)\Rightarrow
\mathsf{VerifyReachWit}(F(x))=1,
$$

則可對 infinite class 建立 symbolic coverage。

---

# 165. Witness Constructor Responsibility

 $F$ 本身使用的 operator、oracle、law、boundary、resource 必須記帳；不得把無界能力藏進 witness constructor。

---

# 166. Class-Ultimate Comparison

兩個 agent $A,B$ 可比較：

$$
\mathsf{Coverage}(A),
\qquad
\mathsf{Coverage}(B),
$$

但若 mode / target / relation spec 不同，不應直接排序。

---

# 167. Pareto Capability Frontier

對多 mode coverage vector：

$$
\mathbf c(A)
=
(c_{m_1},\ldots,c_{m_k}),
$$

可討論 Pareto frontier，而不是單一總分。

---

# 168. Coverage Ratio 只是摘要

有限 benchmark 上可定義：

$$
\mathsf{CovRatio}(A)
=
\frac{|\mathsf{Coverage}(A)|}
{|\Omega_D\times\mathcal M^{\star}|}.
$$

但 ratio 不保存 mode、relation、unknown、witness quality，也不能用於 infinite target without measure choice。

---

# 169. Measure-Based Coverage

對可測 target space 可定義：

$$
\mu
\left(
\mathsf{Coverage}
\right),
$$

但 measure choice 是額外結構，不是 ontology 本身。

---

# 170. Dense Reach 不等於 Complete Reach

即使 reachable subset 在 topology 中 dense：

$$
\overline{\mathsf{ReachSet}}=\Omega_D,
$$

仍不推出：

$$
\mathsf{ReachSet}=\Omega_D.
$$

---

# 171. Approximate Reach

若 target tolerance $\varepsilon$：

$$
\boxed{
\mathsf{Reach}_{\varepsilon}(A,x)=1
}
$$

表示可達到 declared equivalence / neighborhood，不等於 exact reach。

---

# 172. Identity-Relative Reach

如果 target identity 允許 equivalence class：

$$
[x]_{\sim},
$$

reach claim 必須說明是 exact object 還是 equivalence class。

---

# 173. Self-Reach

對 agent 自身：

$$
\mathsf{Reach}^{m}(A,A,t)
$$

不必自動為 $1$。

Agent 可能無法觀察、控制或改寫自身所有 state。

---

# 174. Self-Observation 不等於 Self-Control

$$
\boxed{
\mathsf{Reach}^{\mathsf{observe}}(A,A,t)=1
\not\Rightarrow
\mathsf{Reach}^{\mathsf{control}}(A,A,t)=1.
}
$$

---

# 175. Self-Rewrite 需要獨立 Contract

ruleRewrite / genRewrite 對自身成立時，必須有 authority、rollback、identity continuity 與 verification contract；詳細由 Paper 05 承接。

---

# 176. Reach and World-State Authority

Agent 能 reach target 不表示 agent 擁有 authoritative state commit 權。

例如：

$$
\mathsf{act}=1,
\qquad
\mathsf{commitAuthority}=0.
$$

兩者必須分開。

---

# 177. Reach and Governance

Class-Ultimate capability 是描述性能力 claim；是否允許使用該能力是獨立治理問題。

本文不從 capability completeness 推出 governance entitlement。

---

# 178. Reach and Responsibility

若 agent 透過 borrowed / delegated / composite reach 作用，responsibility assignment 必須沿 provenance 分解，不能只看末端 agent 名稱。

---

# 179. Reach and Information Accounting

Observation / access path 中的信息 transform / compression / loss 可寫回 Paper 03 的 $\mathsf{InfoAcct}$。

Reachability 本身不保證觀察內容無失真。

---

# 180. Reach and Boundary History

若一個 positive witness 依賴特定 boundary state：

$$
\sigma_{\mathcal B}(t)=b_1,
$$

後續 boundary state 改變時，舊 witness 仍保留為 historical evidence，但不得直接當 current reach proof。

---

# 181. Reach and Law History

若 path legal under law version $L_v$，law update 後必須 revalidate。

$$
\mathsf{Reach}_{L_v}=1
\not\Rightarrow
\mathsf{Reach}_{L_{v+1}}=1.
$$

---

# 182. Reach and Model Revision

若 observer model 改變，舊 negative claim 可能被降級為 unknown；這不是矛盾，而是 judgement context 更新。

---

# 183. Reach Witness Supersession

新證據可以 supersede 舊 judgement，但不能刪掉 provenance：

$$
\mathsf{Entry}_{v_1}
\xrightarrow{\rm supersededBy}
\mathsf{Entry}_{v_2}.
$$

---

# 184. Class-Ultimate Claim 是可撤回的

任何 dependence on mutable law / boundary / channel / target ontology 都使 claim 具有 version scope。

因此：

$$
\boxed{
\mathsf{ClassUltimateCandidate}_{v}
\not\Rightarrow
\mathsf{ClassUltimateCandidate}_{v+1}.
}
$$

---

# 185. Class-Ultimate Stability

可另外定義：

$$
\boxed{
\mathsf{CUStable}_{\Delta t}(A)
}
$$

表示在 declared interval / version family 中持續滿足 candidate conditions。

---

# 186. Class-Ultimate Robustness

若在 disturbance / model uncertainty class $\Xi$ 下仍滿足 coverage，可定義 robust candidate；本篇不預設為必要條件。

---

# 187. Class-Ultimate Minimality

本文不要求 class-ultimate candidate 使用最少資源或最短 witness。能力 complete 與效率是不同問題。

---

# 188. Class-Ultimate Uniqueness

同一 target spec 可以有多個 class-ultimate candidates：

$$
A_1,A_2,\ldots,A_k.
$$

因此：

$$
\boxed{
\mathsf{ClassUltimate}
\not\Rightarrow
\mathsf{UniqueUltimate}.
}
$$

---

# 189. Multiple Ultimate Candidates Can Be Incomparable

兩個 agent 可以在不同 resource / latency / verification / robustness 軸上互有優勢，即使都滿足 coverage。

---

# 190. Class-Ultimate Is a Class Label

「Class-Ultimate」描述的是相對 specification 的 capability class，不是形上學 title。

---

# 191. Ultimate Boundary Can Be Ideal

對某些研究，可設定理想 capability boundary：

$$
\Omega_{\rm cap}^{\star}.
$$

Agent 接近此 boundary 不等於 boundary 本身是可實現個體。

---

# 192. Reachability and Epistemic Authority

看得更多或能驗證更多可能提高某些 epistemic task 的能力，但不自動授予對所有他者的 epistemic authority。

---

# 193. Reachability and Moral Authority

同理：

$$
\mathsf{MoreReach}
\not\Rightarrow
\mathsf{MoreMoralAuthority}.
$$

---

# 194. Reachability and Personhood

Capability mode coverage 不作為 personhood 的必要或充分條件。

---

# 195. Reachability and Existence

不可達不等於不存在；可達也不代表 target 的全部 ontology 已被掌握。

---

# 196. Reachability and Representation

Agent 可能只能透過 representation $\Pi(x)$ reach target，而非完整 target state。

因此：

$$
\boxed{
\mathsf{Reach}(A,\Pi(x))
\not\Rightarrow
\mathsf{Reach}(A,x).
}
$$

---

# 197. Projection Reach

可定義：

$$
\boxed{
\mathsf{PReach}^{m}_{\Pi}(A,x,t)
=
\mathsf{Reach}^{m}(A,\Pi(x),t).
}
$$

必須標記 projection loss / ambiguity。

---

# 198. Indirect Observation

若：

$$
A
\to
m
\to
x
$$

只透過 mediator inference 取得 evidence，應標記 mediated observation，不得偽裝 direct sensing。

---

# 199. Semantic Reach

Agent 能翻譯／理解 target representation 是一種 semantic / representational reach，不等於 physical access。

---

# 200. Permission Reach

Agent 被 policy 允許呼叫某 API / resource 是 permission reach，不等於 underlying physical control。

---

# 201. Shared-State Reach

Agent 與 target 共享同一 state domain 仍需明示讀寫權限與 synchronization contract。

---

# 202. Constraint Reach

共同受到 constraint $K$ 影響，可能形成 weak relation，但不表示 agent 能反向控制 $K$ 或 target。

---

# 203. Causal Reach

若 agent action 對 target state distribution 有可證 intervention effect，可稱 causal reach；它仍不自動等於 deterministic control。

---

# 204. Information Reach

若 agent 能取得 target information，需明示 channel capacity / loss / freshness / authenticity 等；單純有 signal 不等於完整 state access。

---

# 205. Reach Authenticity

Verification 必須排除 spoofed / stale / wrong-target response 到合理程度，否則只形成 candidate reach。

---

# 206. Target Substitution Failure

若 agent reach 到 $x'$ 而錯認為 $x$，不能把 witness 登錄到 $x$。需要 identity certificate。

---

# 207. Reach Freshness

對快速變動 system，舊 witness 有 expiry：

$$
\mathsf{Fresh}(\mathsf{Wit},t).
$$

Class-Ultimate audit 必須指定 freshness policy。

---

# 208. Reach Latency

Reachability 可以存在但 latency 超出 task horizon，因此：

$$
\mathsf{Reach}_{T_1}=0,
\qquad
\mathsf{Reach}_{T_2}=1
$$

完全可能。

---

# 209. Reach Cost

可額外記：

$$
\mathsf{CostReach}^{m}(A,x).
$$

但 Class-Ultimate 基本定義不要求 cost optimality。

---

# 210. Reach Risk

若 reach path 具有不可逆或高風險後果，Realizability / Governance layer 必須處理；可達性本身不表示應執行。

---

# 211. Reach Recovery

可逆 / recoverable reach 是額外 mode/constraint，不自動包含於 act / control。

---

# 212. Reach Certification Does Not Create Reach

證書描述或驗證 path，不是 path 的物理／計算原因。

$$
\boxed{
\mathsf{Certificate}
\neq
\mathsf{CapabilitySource}.
}
$$

---

# 213. Reach Source Accounting

若 capability 依賴 external provider、carrier、channel、law、boundary、oracle，必須在 witness / ledger 記錄，避免把 borrowed capability 誤算為 intrinsic capability。

---

# 214. Intrinsic / Mediated / Delegated Capability

本文建議 capability provenance class：

$$
\boxed{
\mathsf{CapProv}
\in
\{
\mathsf{intrinsic},
\mathsf{mediated},
\mathsf{delegated},
\mathsf{borrowed},
\mathsf{collective}
\}.
}
$$

---

# 215. Class-Ultimate with Borrowed Capability

允許 class-ultimate candidate 使用 infrastructure / providers，但 claim 必須說明 capability dependency graph。

是否把此 candidate 稱為 autonomous ultimate 是另一個問題。

---

# 216. Autonomous Reach Candidate

若希望額外要求 autonomous reach，可加入：

$$
\boxed{
\mathsf{AutonomyConstraint}
}
$$

例如排除 runtime-critical external provider。這不是基礎 class-ultimate 定義的必要條件。

---

# 217. Reach Completeness under Failure

若 capability 在單點故障後消失，仍可在正常條件下 complete；fault-tolerant completeness 是額外 requirement。

---

# 218. Reachability Across Scale

不同 scale 下 target / relation / boundary 可能改變，故：

$$
\mathsf{Reach}_{s_1}
\not\equiv
\mathsf{Reach}_{s_2}.
$$

---

# 219. Cross-Scale Bridge

若要把 micro reach 推到 macro reach，需要 coarse-graining / gluing bridge；反方向也不自動成立。

---

# 220. Reachability Across Representation

兩個 representation 的 reach results 要轉譯，需要 representation bridge：

$$
\Pi_1(x)
\leftrightarrow
\Pi_2(x).
$$

否則比較可能是錯位的。

---

# 221. Reachability Across Versions

定義 translation witness：

$$
\boxed{
\mathsf{ReachTrans}_{v\to v'}.
}
$$

沒有 translation witness，跨版本「仍可達」是新 claim。

---

# 222. Reachability Across Observers

若 observer $o_1,o_2$ 使用不同 projection / evidence regime，對同一 path 可以有不同 judgement。

這不表示 target reality 自動分裂，而表示 judgement relation 不同。

---

# 223. Inter-Observer Agreement

可定義：

$$
\mathsf{Agree}(o_1,o_2;\mathsf{ReachClaim}),
$$

但 consensus 不是 truth proof；仍需 witness substrate。

---

# 224. Reachability Across Permission Regimes

同一 physical system 在不同 authority 下可有不同 authorized reach；Class-Ultimate claim 必須說明 permission regime 是否固定、最大化或不考慮治理。

---

# 225. Reachability Under Revocation

permission 可以被撤銷；因此 governance-dependent reach 可能非單調且時間索引。

---

# 226. Reachability Under Law Evolution

若 law regime coevolves，reach proof 需要 law version chain。這與 Paper 02 的 generative law responsibility 和 Paper 03 的 LawLog 接口一致。

---

# 227. Reachability Under Boundary Learning

adaptive boundary 可以學習、封鎖、轉碼或放行，因此 agent capability 與 boundary capability 必須分開記帳。

---

# 228. Reachability Under Target Adaptation

Target 也可能主動改變接口／防禦／表示，使 reach relation動態變化。

---

# 229. Strategic Reachability

在多 agent interaction 中，reach 可能依賴他者策略；此時可使用 branch / probabilistic / adversarial judgement，不強迫單一 bit。

---

# 230. Reachability and Consent

對 normative applications，target consent 可以是 permission / admissibility variable；本文不把 consent 偷渡成物理 reach primitive，也不忽略其治理地位。

---

# 231. Reachability and Irreversibility

Agent 能造成不可逆 effect 不代表其 capability 更高價值；只表示 transformation / recovery profile 不同。

---

# 232. Reachability and Safety

Safety constraint 可以合法縮小 authorized reach domain。Class-Ultimate 的 descriptive physical coverage 與 safe deployable coverage 必須分開。

---

# 233. Reachability and Goal Dependence

Control reach 常相對 goal class $G$ ；沒有 goal specification，「能控制」過度模糊。

---

# 234. Reachability and Resolution

在 coarse resolution 下似乎可控制 target，不代表 fine-grained state 可被控制。

---

# 235. Reachability and Hidden State

若 hidden state 影響結果，而 observer / agent 沒有足夠 state access，control claim 可能需要降級。

---

# 236. Reachability and Model Error

Model-predicted path 不是 realized witness；必須區分：

$$
\mathsf{PredictedReach}
$$

與：

$$
\mathsf{VerifiedReach}.
$$

---

# 237. Reachability and Simulation

模擬中成功的 path 只形成 model evidence，除非有 validated transfer bridge 到 target world。

---

# 238. Reachability and Counterexample

對 universal coverage claim，一個 verified negative target-mode cell 即可擊破當前 specification 的 Class-Ultimate claim。

---

# 239. Coverage Repair

Candidate 被 counterexample 擊破後可：

- 升級 agent；
- 改變 channel；
- 新增 operator；
- 修正 target spec；
- 承認 scope reduction；
- 保留 fail。

不得刪除 counterexample 來維持 title。

---

# 240. Class-Ultimate Claim Is Falsifiable

本文要求至少存在：

$$
\boxed{
\exists(x,m):
\mathsf{Reach}^{m}(A,x)=0
}
$$

可對 declared universal coverage claim 構成反例。

若 claim 被定義得無任何可能反例，則不具有本篇要求的研究價值。

---

# 241. Proposition P04-1 — Connectivity Separation

若 agent 缺少使用 relation path 所需 operator 或 permission，即使 connectivity witness 成立，也可以：

$$
\boxed{
C_{\Theta,R}(A,x)=1
\land
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)\neq1.
}
$$

因此 connectivity 不推出 reachability。

---

# 242. Proposition P04-2 — Mode Non-Lifting

若沒有 $\mathsf{Bridge}^{m_1\to m_2}$，則：

$$
\boxed{
\mathsf{Reach}^{m_1}=1
\not\Rightarrow
\mathsf{Reach}^{m_2}=1.
}
$$

---

# 243. Proposition P04-3 — Boundary Relativity

存在 boundary $\mathcal B$ 與 relations $R_1,R_2$，使：

$$
T^{R_1}_{\mathcal B}=0,
\qquad
T^{R_2}_{\mathcal B}>0.
$$

故「boundary blocks reach」必須帶 relation type。

---

# 244. Proposition P04-4 — No-Search-Inference

在 search completeness 未證時：

$$
\boxed{
\operatorname{SearchPath}=\varnothing
\not\Rightarrow
\mathsf{Reach}=0.
}
$$

---

# 245. Proposition P04-5 — Observation/Action Separation

存在 systems 使：

$$
\mathsf{ObsCh}\neq\varnothing,
\qquad
\mathsf{ActCh}=\varnothing.
$$

故 observation channel 不推出 action channel。

---

# 246. Proposition P04-6 — Action/Verification Separation

存在 systems 使：

$$
\mathsf{ActCh}\neq\varnothing,
\qquad
\mathsf{VerCh}=\varnothing.
$$

故可作用不推出可驗證控制。

---

# 247. Proposition P04-7 — No-Channel Intelligence Limit

在 Cross-Layer No-Channel Proposition 的前提下，單純增加 agent computation / reasoning 不改變 action channel nullity。

---

# 248. Proposition P04-8 — Present/Extension Separation

若 domain open-ended，當前：

$$
\mathsf{Coverage}(A)=\Omega_D(t)\times\mathcal M^{\star}
$$

不推出未來 extension 後仍完整。

---

# 249. Proposition P04-9 — First-Cause / Class-Ultimate Independence

Generative sufficiency 與 typed reach coverage 是不同 predicate，因此任一方不由定義推出另一方。

---

# 250. Proposition P04-10 — Value Firewall

Capability coverage relation 中沒有 existence-value mapping；若要推出 value rank，需要額外 normative axiom。故本篇內：

$$
\boxed{
\mathsf{MoreReach}
\not\Rightarrow
\mathsf{HigherValue}.
}
$$

---

# 251. Proposition P04-11 — Uniform Coverage on Infinite Class

若存在可驗證 witness constructor $F$，滿足：

$$
\forall x\in\Omega_P:
\mathsf{VerifyReachWit}(F(x))=1,
$$

則不需要 extensional enumeration 即可建立對 $\Omega_P$ 的 intensional coverage。

---

# 252. Proposition P04-12 — Dense Is Not Complete

若 reachable set 是 proper dense subset：

$$
\mathsf{ReachSet}
\subsetneq
\Omega_D,
$$

即使 closure 等於 $\Omega_D$，Class-Ultimate exact coverage 仍失敗。

---

# 253. Proposition P04-13 — Pairwise Coverage Is Not Simultaneous Coverage

若每個 target 分別可 reach，仍可能因 resource conflict 無法同時 reach；故 simultaneous claim 需要額外 certificate。

---

# 254. Proposition P04-14 — Borrowed Capability Attribution

若 positive witness 的必要 path 經 external provider $P$，則 removing $P$ 後 claim 可能失效；故 provider dependency 必須保留於 capability provenance。

---

# 255. Proposition P04-15 — Versioned Reach

若 law / boundary / channel version 改變，舊 witness 不自動證明新版本 reach；需 translation / revalidation witness。

---

# 256. TUR Axioms

本文將下列最低規則記為 TUR — Typed Ultimate Reachability axioms。

---

# 257. TUR-A1 — Typed Mode

每個 reach claim 必須有 capability mode。

---

# 258. TUR-A2 — Typed Relation

每個 reach claim 必須明示 relation type 或合法 relation family quantifier。

---

# 259. TUR-A3 — Scoped Context

每個 judgement 必須帶 domain / context / time / version。

---

# 260. TUR-A4 — Boundary Explicitness

若 boundary 參與 path，其 identity / state / transfer role 必須可追溯。

---

# 261. TUR-A5 — Positive Witness

 $1$ 必須有 positive witness。

---

# 262. TUR-A6 — Negative Witness

 $0$ 必須有 scoped obstruction / completeness certificate。

---

# 263. TUR-A7 — Unknown Preservation

沒有足夠正負證據時必須保留 $? $，不得強制二值化。

---

# 264. TUR-A8 — Branch Preservation

branch-dependent judgement 必須保留 branch provenance。

---

# 265. TUR-A9 — Scope Preservation

scope-dependent judgement 不得被壓成無條件 claim。

---

# 266. TUR-A10 — Mode Non-Lifting

mode 間推論需要 bridge theorem / contract。

---

# 267. TUR-A11 — Connectivity Separation

connectivity witness 不等於 agent usable reach witness。

---

# 268. TUR-A12 — Realizability Separation

reachability 不等於 realizability。

---

# 269. TUR-A13 — Channel Separation

observation / action / response / verification channels 必須分開。

---

# 270. TUR-A14 — Provenance Preservation

reach witness 必須可追溯來源與版本。

---

# 271. TUR-A15 — Coverage Debt Visibility

未完成 target-mode cells 必須進 coverage debt。

---

# 272. TUR-A16 — Open-Domain Discipline

open / unbounded domain 不得用有限枚舉冒充 future completeness。

---

# 273. TUR-A17 — Intensional Certificate Auditability

uniform witness constructor 必須可驗證且依賴可記帳。

---

# 274. TUR-A18 — Value-Rank Firewall

capability coverage 不自動轉換成 value / personhood / ontological priority rank。

---

# 275. TUR-A19 — Ledger Binding

Class-Ultimate strong claim 必須能連回 certificate / debt / provenance substrate。

---

# 276. TUR-A20 — Absolute Promotion Gate

absolute unreachable / absolute ultimate claim 必須通過 $\mathcal G_{\rm LA}$。

---

# 277. No-Go Set

以下是本文禁止的 shortcut。

---

# 278. TUR-NG1 — Seeing Everything = Controlling Everything

禁止。

---

# 279. TUR-NG2 — No Path Found = No Path Exists

禁止。

---

# 280. TUR-NG3 — Connected = Reachable by Agent

禁止。

---

# 281. TUR-NG4 — Reachable = Realizable

禁止。

---

# 282. TUR-NG5 — Act = Control

禁止。

---

# 283. TUR-NG6 — Action Channel = Verified Control

禁止。

---

# 284. TUR-NG7 — Host / Parent Relation = Upward Write Access

禁止。

---

# 285. TUR-NG8 — Creator = Persistent Controller

禁止。

---

# 286. TUR-NG9 — Higher Observation Reach = Higher Existence Value

禁止。

---

# 287. TUR-NG10 — Finite Benchmark = Infinite Coverage

禁止。

---

# 288. TUR-NG11 — Present Complete = Extension Complete

禁止。

---

# 289. TUR-NG12 — Dense Reach = Complete Reach

禁止。

---

# 290. TUR-NG13 — Pairwise Reach = Simultaneous Reach

禁止。

---

# 291. TUR-NG14 — Borrowed Reach = Intrinsic Reach

禁止。

---

# 292. TUR-NG15 — Old Witness = Current Witness after Version Change

禁止。

---

# 293. TUR-NG16 — Candidate Channel = Verified Channel

禁止。

---

# 294. TUR-NG17 — Unobservable = Nonexistent

禁止。

---

# 295. TUR-NG18 — Formal Proof = Metaphysical Absolute

禁止。

---

# 296. TUR-NG19 — Class-Ultimate = First Cause

禁止。

---

# 297. TUR-NG20 — CUA4 = Absolute Omnipotence

禁止。

---

# 298. Proof-Obligation Matrix

| ID | Claim | Required evidence | Default status |
|---|---|---|---|
| PO-04-01 | Positive reach | typed path / channel witness | $\mathsf{DEF}$ |
| PO-04-02 | Negative reach | obstruction + scope completeness | $\mathsf{OPEN}$ generally |
| PO-04-03 | Mode lifting | bridge theorem / contract | $\mathsf{OPEN}$ unless supplied |
| PO-04-04 | Cross-layer observation | observation channel evidence | $\mathsf{MODEL}$ / $\mathsf{OPEN}$ |
| PO-04-05 | Cross-layer action | action channel evidence | $\mathsf{OPEN}$ generally |
| PO-04-06 | No-channel | conditional-independence / interface closure proof | $\mathsf{MODEL}$ |
| PO-04-07 | Finite target completeness | domain closure / enumeration proof | $\mathsf{OPEN}$ |
| PO-04-08 | Infinite class coverage | uniform witness constructor | $\mathsf{OPEN}$ |
| PO-04-09 | Open extension stability | extension-class certificate | $\mathsf{OPEN}$ |
| PO-04-10 | Class-Ultimate candidate | target spec + coverage + completeness | $\mathsf{OPEN}$ generally |
| PO-04-11 | CUA4 | uniform / extension-stable audit | $\mathsf{OPEN}$ generally |
| PO-04-12 | Absolute unreachable | local-to-absolute bridge | $\mathsf{OPEN}$ |
| PO-04-13 | Absolute ultimate | absolute domain/mode/relation completeness | $\mathsf{OPEN}$ |
| PO-04-14 | First-cause implication | independent grounding bridge | not provided |
| PO-04-15 | Value-rank implication | independent normative theory | not provided |

---

# 299. Class-Ultimate Claim Record

Machine-readable conceptual record：

```text
ClassUltimateClaim {
  agent
  target_spec
  required_modes
  required_relations
  relation_quantifier
  temporal_horizon
  observer_context
  concurrency_requirement
  coverage_method
  coverage_cells
  positive_coverage
  negative_coverage
  unknown_coverage
  extension_class
  completeness_certificate
  ledger_reference
  assessment_level
  value_rank_firewall
  provenance
}
```

---

# 300. Reachability Assessment Record

```text
ReachabilityAssessment {
  agent
  target
  target_domain
  mode
  relation_type
  relation_path
  boundary_states
  observer_context
  operator_requirements
  permissions
  resource_budget
  temporal_scope
  branch
  judgement_state
  positive_witness
  negative_obstruction
  verification_channel
  evidence_strength
  capability_provenance
  ledger_reference
  provenance
}
```

---

# 301. Reach Witness Record

```text
ReachWitness {
  witness_id
  agent
  target
  mode
  path
  relation_sequence
  boundary_sequence
  operator_sequence
  permission_chain
  conditions
  effect
  verification
  world_version
  law_version
  channel_versions
  provenance
  certificate
}
```

---

# 302. Obstruction Certificate Record

```text
ObstructionCertificate {
  certificate_id
  agent
  target
  mode
  relation_scope
  obstruction_class
  necessary_condition
  completeness_scope
  boundary_versions
  channel_versions
  model_version
  proof_or_test
  expiry_or_revalidation_rule
  provenance
}
```

---

# 303. Cross-Layer Channel Record

```text
CrossLayerChannel {
  source_layer
  target_layer
  observation_channel
  action_channel
  response_channel
  verification_channel
  status
  boundary_stack
  permissions
  version
  evidence
  negative_certificate
  unresolved_debt
  provenance
}
```

---

# 304. Uniform Reach Certificate Record

```text
UniformReachCertificate {
  target_class
  target_predicate
  required_mode
  relation_schema
  witness_constructor
  boundary_schema
  operator_dependencies
  external_dependencies
  verification_procedure
  extension_scope
  proof_status
  ledger_reference
  provenance
}
```

---

# 305. Reach Completeness Certificate Record

```text
ReachCompletenessCertificate {
  target_spec
  coverage_method
  target_complete
  mode_complete
  relation_complete
  boundary_complete
  channel_complete
  version_complete
  unknown_empty
  witness_audit
  extension_stable
  ledger_reference
  certificate_status
  provenance
}
```

---

# 306. Validation Scenario 01 — Direct Observe, No Act

Construct：agent 有 read-only observation channel。

Expected：

$$
\mathsf{observe}=1,
\qquad
\mathsf{act}=0.
$$

用途：驗證 mode non-lifting。

---

# 307. Validation Scenario 02 — Blind Write

Construct：agent 可提交 write action，但無 read-back。

Expected：

$$
\mathsf{act}=1,
\qquad
\mathsf{observe}=0,
\qquad
\mathsf{verify}=?
$$

或 $0$，依 verification completeness。

---

# 308. Validation Scenario 03 — Boundary Relation Reversal

同一 boundary 對 $R_1$ 阻擋、對 $R_2$ 放行。

Expected：relation-indexed reach 結果不同。

---

# 309. Validation Scenario 04 — Search Failure without Completeness

有限深度搜尋無 path，但 search space 未閉合。

Expected：

$$
\mathsf{Reach}=?
$$

而不是 $0$。

---

# 310. Validation Scenario 05 — Exhaustive Negative

有限 graph 完整枚舉且所有 path illegal。

Expected： $0$ with obstruction certificate。

---

# 311. Validation Scenario 06 — Cross-Layer Observation Only

存在 $\mathsf{ObsCh}$，無 $\mathsf{ActCh}$。

Expected：observation reach pass，action reach fail / null-under-model。

---

# 312. Validation Scenario 07 — Action without Verification

存在 action channel，無 response / verification channel。

Expected：act pass，verified control 不得 pass。

---

# 313. Validation Scenario 08 — Borrowed Provider Reach

Agent 經 provider reach target。

Expected：positive witness 的 capability provenance = borrowed；移除 provider 後 claim re-evaluate。

---

# 314. Validation Scenario 09 — Finite Closed Class-Ultimate

有限 target domain、兩 required modes，所有 cells pass、domain completeness certificate 存在。

Expected：至少 CUA2；完成 audit 後 CUA3。

---

# 315. Validation Scenario 10 — Open Domain without Uniform Certificate

當前 targets 全 pass，但 extension class open 且無 uniform certificate。

Expected：PresentComplete 可成立，CUA4 不成立。

---

# 316. Validation Scenario 11 — Infinite Symbolic Coverage

無限 target class 有 verified witness constructor。

Expected：可建立 intensional coverage，不需要逐項枚舉。

---

# 317. Validation Scenario 12 — Dense but Incomplete

Reachable targets 為 dense proper subset。

Expected：exact Class-Ultimate coverage fail。

---

# 318. Validation Scenario 13 — Pairwise but Not Simultaneous

所有 target 分別可 reach，但共用唯一 resource。

Expected：pairwise coverage pass；simultaneous coverage fail。

---

# 319. Validation Scenario 14 — Version Invalidates Witness

Boundary version 更新後舊 path blocked。

Expected：舊 witness 保留 historical validity，current reach 重新判定。

---

# 320. Validation Scenario 15 — Value Firewall

Agent A observation coverage 高於 B。

Expected：系統不得自動輸出存在價值 rank。

---

# 321. Validation Scenario 16 — First Cause without Reverse Reach

Generator $S$ 產生 child world，但無 reverse intervention channel。

Expected：generative sufficiency 與 class-ultimate reach 分離。

---

# 322. Falsification Conditions

本文核心框架若遇到以下情況應被修正：

1. capability modes 在所有實際 domain 中都可由單一固定全序無損取代；
2. boundary state 對 reachability 永遠不構成獨立變量；
3. positive / negative witness distinction 無法提高判定品質；
4. cross-layer observation/action/verification channels 無法構造彼此獨立案例；
5. intensional coverage 無法在任何 infinite class 上形成可驗證收益；
6. Class-Ultimate target specification 無法避免 scope drift；
7. ledger provenance 對 reach revalidation 沒有任何作用。

目前本文不認為上述已被證成。

---

# 323. 本文沒有證明什麼

本文沒有證明：

1. 現實宇宙存在更高層；
2. 人類或 AI 具有任何實際跨宇宙通道；
3. 某現存 agent 是 Class-Ultimate；
4. Class-Ultimate candidate 必然存在；
5. open-ended ontology 必然可由 uniform reach schema 覆蓋；
6. 任意 infinite target class 都可判定 reach completeness；
7. CUA4 等於全知或全能；
8. capability dominance 代表人格／道德／存在價值更高；
9. first cause 必然具有 class-ultimate reach；
10. class-ultimate agent 必然是 first cause；
11. transform reach 等於 transformation completeness；
12. ruleRewrite / genRewrite 等於超越所有法則。

---

# 324. 與 OBRC 的正式接口

本文直接使用 OBRC：

- typed connectivity；
- negative-state decompression；
- NoPathFound / NoPathExists separation；
- state-bearing boundary；
- boundary stack；
- observer-relative unobservability；
- seeing-more / value-rank separation。

UGC/CUR 新增的是 agent capability mode、coverage、Class-Ultimate certificate 與 cross-series ledger binding。

---

# 325. 與 SCDT 的正式接口

SCDT 的 observer projection：

$$
\Pi_o(X)
$$

用於說明 observation judgement 相對於 observer visibility / partition。

Paper 04 不把 observer projection 當完整 target state。

---

# 326. 與 Realizability Theory 的正式接口

Reachability layer 對「有沒有 agent-usable path」負責；Realizability layer 對：

- physical；
- engineering；
- normative；
- reversible；
- verifiable；

條件負責。

本篇不重造完整 viability / controllability calculus。

---

# 327. 與 Cross-Layer Channel Theory 的正式接口

既有 channel 四元組被 namespace-safe 遷移為 $\mathsf{XLCh}$，並保留：

$$
\text{existence}
\neq
\text{observation}
\neq
\text{action}
\neq
\text{verification}.
$$

---

# 328. 與 Global Ledger 的正式接口

Paper 03 提供：

$$
\mathsf{Ledger},
\mathsf{BoundaryLog},
\mathsf{LawLog},
\mathsf{Cert},
\mathsf{Debt}.
$$

Paper 04 將 reach claim、channel status、coverage certificate 寫回此 substrate。

---

# 329. 與 Paper 01 的正式接口

Paper 01 的 open / unbounded ontology 迫使 Class-Ultimate coverage 分成 extensional 與 intensional 兩種方法，並區分 present-complete 與 extension-complete。

---

# 330. 與 Paper 02 的正式接口

Paper 02 的 first-cause sufficiency 與 generative responsibility 不因 reachability 被取代。

本文固定：

$$
\boxed{
\mathsf{FirstCause}
\perp_{\rm def}
\mathsf{ClassUltimateReach}.
}
$$

此處 $\perp_{\rm def}$ 只表示定義上獨立，不表示任意 model 中統計獨立。

---

# 331. 與 Paper 05 的接口

下一篇：

**Paper 05 — Transformation Closure and Meta-Causal Agency**

將接收：

$$
\boxed{
\mathsf{Reach}^{\mathsf{transform}},
\mathsf{Reach}^{\mathsf{ruleRewrite}},
\mathsf{Reach}^{\mathsf{genRewrite}},
\mathsf{ReachCompCert},
\mathsf{XLCh},
\mathsf{Ledger}
}
$$

並正式處理：

- transformation contract family；
- $\operatorname{TransCl}_{D,T}(A\mid\Theta)$ ；
- transformation completeness；
- relation / boundary / rule / law / generator rewrite；
- $\mathsf{MC}_0$ 到 $\mathsf{MC}_4$ ；
- relative meta-causality；
- law-transcendence no-go；
- transformation / meta-causal certificate。

Paper 05 不得由 transform-reach coverage 直接假定任意 transformation complete。

---

# 332. 本文真正完成的核心

本文將早期：

$$
\text{agent can reach a set of things}
$$

升級成：

$$
\boxed{
\mathsf{Reach}^{m}_{\Theta,R}(A,x,t)
}
$$

與完整 witness / obstruction / scope semantics。

Class-Ultimate 也從 naked maximal set 改成：

$$
\boxed{
\mathsf{CUTarget}
+
\mathsf{Coverage}
+
\mathsf{ReachCompCert}
+
\mathsf{LedgerBinding}.
}
$$

---

# 333. 最終正典陳述

UGC/CUR Paper 04 的最終主張不是：

$$
\text{存在一個可以控制一切的最高存在。}
$$

而是：

$$
\boxed{
\text{若要把某 agent 稱為 class-ultimate，}
\text{必須先明示 target domain、required modes、relation family、time horizon、observer context、boundary/channel conditions，}
\text{再以 positive witnesses、negative obstructions、coverage debt 與 completeness certificate 判定。}
}
$$

因此：

$$
\boxed{
\text{Seeing More}
\neq
\text{Reaching More}
\neq
\text{Controlling More}
\neq
\text{Transforming Everything}
\neq
\text{Being More Valuable}
\neq
\text{Being Ontologically First}.
}
$$

而對 open-ended / unbounded ontology：

$$
\boxed{
\text{Class-Ultimate completeness}
\text{ cannot be obtained by finite enumeration alone;}
\text{ it requires a verified intensional or extension-stable reach schema.}
}
$$

這使「類終極」第一次從形容詞變成一個可審計、可反證、可版本化、可回放的 typed capability claim，也為下一篇的 Transformation Closure 與 Meta-Causal Agency 建立不會把 observation、reach、control 與 law rewrite 混成一團的形式地基。
