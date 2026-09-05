# GCM Canonical Specification & Formal Contract
## Global Computation Methodology 技術規格、型別契約與 Canonical Runtime 義務 v0.1

**文件類型：** Technical Whitepaper / Normative Engineering Specification  
**系列：** Global Computation Methodology（GCM）  
**版本：** v0.1  
**日期：** 2026-08-24  
**Canonical source format：** UTF-8 Markdown  
**數學 delimiter：** ` $...$ ` 與 `$$...$$`  
**狀態：** 第二輪正式工程規格；衍生自 Series-00 v0.2 與 Paper-01–06 v0.2

---

## 摘要

Global Computation Methodology（GCM）的六篇核心論文已分別建立：World-relative global coherence、24／72 computational configuration basis、dynamic routing、Observer／materialization separation、finite active realization，以及 typed history / provenance。若只停留在論文層，這些概念仍可能在實作時被不同 Runtime 重新解讀，造成符號漂移、權限滲漏、Observer/World 混用、route/commit 混用、history 壓縮失真，以及 Foundation 被 ordinary Runtime 偷偷改寫。

本文件因此不再主要回答「為什麼 GCM 應如此設計」，而是回答：

> **一個 Runtime 若宣稱實作 GCM，最低限度必須保存哪些型別邊界、操作契約、權限義務、提交語義、生命週期與歷史語義？**

本規格將 00–06 已收斂內容轉換為可實作的 canonical contract。其核心可濃縮為：

$$
\boxed{
\text{Addressable}
\rightarrow
\text{Reachable}
\rightarrow
\text{Admissible}
\rightarrow
\text{Authorized}
\rightarrow
\text{Executable}
\rightarrow
\text{Reconciled}
\rightarrow
\text{Verified}
\rightarrow
\text{Committable}
}
$$

且任何 ordinary Runtime transition 必須維持：

$$
\boxed{
\mathcal M_G
\neq
\mathbf W
}
$$

$$
\boxed{
\text{Observer Operation}
\neq
\text{World Operation}
\neq
\text{Foundation Revision}
}
$$

$$
\boxed{
\text{Executor Output}
\neq
\text{Canonical World Commit}
}
$$

$$
\boxed{
\text{State Equality}
\not\Rightarrow
\text{History Equality}
}
$$

本文件將成為 TW-02 Reference Runtime Architecture 與 TW-03 Conformance / Verification Specification 的直接上游規格來源。

---

# 0. 規格角色與適用範圍

本文件是 **GCM 的 normative engineering specification**。

它的責任是：

1. 固定 canonical namespace；
2. 固定核心 record / contract；
3. 固定 state-plane 邊界；
4. 固定 operation typing；
5. 固定 route gating semantics；
6. 固定 authority non-escalation；
7. 固定 Observer / materialization / resolution 分離；
8. 固定 active-support / dormancy / archive 義務；
9. 固定 typed history / provenance 義務；
10. 固定 Foundation revision 邊界；
11. 固定相容性、版本化與失敗時的 fail-closed 原則。

本文件 **不**：

- 指定唯一程式語言；
- 指定唯一資料庫；
- 指定唯一 scheduler；
- 指定唯一 optimization objective；
- 指定唯一 AI Router；
- 指定 World 必須是物理世界、遊戲世界或模擬世界；
- 要求實作全部 24／72 cell；
- 要求所有 history 永久 resident in memory；
- 把 GCM 定義成第 73 種計算範式；
- 把 Mathematics 等同 Optimization。

---

# 1. Normative language

本文件使用以下規範詞：

- **MUST**：合規實作不可違反；
- **MUST NOT**：合規實作不可執行；
- **SHOULD**：預設應遵循；若偏離，應能記錄理由與風險；
- **SHOULD NOT**：預設不應採用；若採用，應能證明不破壞相關 invariants；
- **MAY**：可選能力。

當論文中的概念敘述與本規格中的明確 MUST 條款產生歧義時，Runtime 不得自行選擇「對自己最方便的解讀」。必須透過 explicit specification revision 解決。

---

# 2. Canonical source lineage 與版本優先級

本規格衍生自：

1. Series-00 v0.2；
2. Paper-01 v0.2；
3. Paper-02 v0.2；
4. Paper-03 v0.2；
5. Paper-04 v0.2；
6. Paper-05 v0.2；
7. Paper-06 v0.2。

本文件將上述論文中的穩定義務抽成工程契約。

需區分至少三種版本：

$$
\boxed{
v_{\mathrm{spec}}
\neq
v_{\mathrm{config}}
\neq
v_{\mathrm{foundation}}
}
$$

其中：

- $v_{\mathrm{spec}}$：GCM 技術規格版本；
- $v_{\mathrm{config}}$：configuration schema / registry 版本；
- $v_{\mathrm{foundation}}$：特定 World / deployment 的 Foundation 版本。

規格升版不等於 World Foundation revision；configuration registry 擴張也不等於 Foundation revision。

---

# 3. Canonical state planes

GCM-compliant Runtime MUST 至少區分下列語義層：

$$
\boxed{
\mathbf W
=
\text{World primitive}
}
$$

$$
\boxed{
W_\nu
=
\text{canonical committed executable World-state presentation}
}
$$

$$
\boxed{
\Xi_\mu
=
\text{Runtime control state}
}
$$

$$
\boxed{
O_\omega
=
\text{Observer state}
}
$$

$$
\boxed{
\mathcal F^{(v)}
=
\text{Foundation version}
}
$$

$$
\boxed{
\mathcal H_\eta
=
\text{history / provenance state}
}
$$

其中 typed indices 為：

$$
\nu
=
\text{World commit/version identifier},
$$

$$
\mu
=
\text{Runtime-control revision},
$$

$$
\omega
=
\text{Observer revision},
$$

$$
\eta
=
\text{history-store revision}.
$$

因此：

$$
\boxed{
\nu
\neq
\mu
\neq
\omega
\neq
\eta
\quad
\text{as typed roles}
}
$$

此不等式表示語義角色不可偷換，不要求它們的數值永遠不同。

## 3.1 State-plane non-collapse

Runtime MUST NOT 將：

- projection cache；
- scheduler queue；
- resource availability；
- Observer viewport；
- history index；

直接當成 canonical World primitive mutation。

同樣地，canonical World commit MUST NOT 因 UI refresh 或 cache rebuild 被假造。

---

# 4. Expanded GCM typed core

本規格採下列 expanded core：

$$
\boxed{
\mathcal M_G
=
\left\langle
\mathbf W;
W_\nu,
\Xi_\mu,
O_\omega,
\mathcal F^{(v)};
\mathfrak P,
\mathfrak L,
\mathcal D,
\Gamma_\nu;
\mathcal C,
\mathsf{Reach},
\mathsf{Auth},
\mathcal S;
\Pi,
\mathsf{Mat},
\mathcal H_\eta
\right\rangle
}
$$

並維持：

$$
\boxed{
\mathcal M_G
\neq
\mathbf W.
}
$$

任何 implementation-specific object 若無法清楚映射到其中一個或多個 typed roles，SHOULD 被視為未分類 extension，而不是強迫塞入既有符號。

---

# 5. World boundary 與 typed globality

Globality MUST 相對指定 World boundary 判定。

令：

$$
B_W
=
\text{designated World boundary}.
$$

定義：

$$
\operatorname{Global}_{B_W}(x)
$$

表示 $x$ 的合法性、一致性或依賴義務必須相對 $B_W$ 判定。

因此：

$$
\boxed{
\text{Global Computation}
\neq
\text{Absolute Universe-wide Computation}
}
$$

$$
\boxed{
\text{Global Computation}
\neq
\text{One Computation Everywhere}
}
$$

$$
\boxed{
\text{Global Computation}
=
\text{Globally Coherent Heterogeneous Computation}
}
$$

Nested boundaries MAY 存在；同一 operation MAY 對較小 boundary 是 global，對較大 boundary 是 local。

---

# 6. Canonical namespace registry

以下符號屬 TW-01 v0.1 canonical namespace：

| Symbol | Canonical meaning |
|---|---|
| $\mathbf W$ | World primitive |
| $W_\nu$ | canonical committed executable World-state presentation |
| $\Xi_\mu$ | Runtime control state |
| $O_\omega$ | Observer state |
| $\mathcal F^{(v)}$ | Foundation version |
| $\mathcal H_\eta$ | history / provenance state |
| $\mathfrak P$ | computational configuration basis / space |
| $\mathfrak L$ | transition-law family |
| $\mathcal D$ | domain family |
| $\Gamma_\nu$ | domain-relative configuration assignment |
| $\mathcal C$ | constraints / couplings |
| $\mathcal S$ | routing / scheduling / composition policy family |
| $\Pi$ | projection family |
| $\mathsf{Mat}$ | materialization state / policy |
| $\mathsf{Hor}_\mu$ | active dependency horizon |
| $\rho^C$ | compute resolution |
| $\rho^O$ | Observer / projection resolution |
| $\lambda^{ST}$ | domain-specific spacetime scale, when applicable |
| $\mathsf{Reach}$ | reachability relation |
| $\mathsf{Auth}$ | authority relation |
| $\mathsf{Pot}$ | potential / not-yet-canonical possibility |
| $\mathsf{Pin}$ | pinning family |
| $\mathsf{Br}$ | representation bridge |

## 6.1 Forbidden namespace collapse

Canonical source MUST NOT：

1. 使用 $\mathcal H$ 表示 active horizon；
2. 使用 $\mathcal C$ 表示 configuration assignment；
3. 使用單一 $P$ 同時表示 Potential、Pinned、Permission；
4. 使用單一 $R$ 同時表示 Route、Receipt、Archived status；
5. 使用 $\Lambda$ 同時表示 resolution、materialization 與 physical scale；
6. 使用 $\mathfrak O_3$ 表示真正 Observer。

---

# 7. Computational configuration basis

GCM 保留：

$$
\boxed{
\mathfrak P_{24}
=
\mathfrak B_2
\times
\mathfrak U_4
\times
\mathfrak I_3
}
$$

其中：

$$
\mathfrak B_2
=
\{\mathsf C,\mathsf D\},
$$

$$
\mathfrak U_4
=
\{\mathsf S,\mathsf J,\mathsf P,\mathsf R\},
$$

$$
\mathfrak I_3
=
\{\mathsf C,\mathsf D,\mathsf X\}.
$$

加入 transition-law family：

$$
\mathfrak L_3
=
\{\mathsf F,\mathsf K,\mathsf Q\},
$$

得到：

$$
\boxed{
\mathfrak P_{72}
=
\mathfrak P_{24}
\times
\mathfrak L_3.
}
$$

## 7.1 Basis semantics

Runtime MUST 將 24／72 視為：

$$
\boxed{
\text{Finite Coordinate Basis}
}
$$

而不是：

$$
\boxed{
\text{Exhaustive Mutually Exclusive Ontology of All Computation}.
}
$$

因此：

$$
\boxed{
24/72
\neq
\text{The 73rd Paradigm Premise}.
}
$$

Composite subsystem MAY 具有多個 basis cells。

## 7.2 Full Runtime configuration

令：

$$
\mathfrak G^{(v)}
$$

表示 configuration schema version $v$ 下的 full Runtime configuration space。

最小 configuration record：

$$
\boxed{
\gamma
=
\left\langle
\beta,
\rho^C,
r,
\chi
\right\rangle
}
$$

其中：

- $\beta$：basis address / composite basis profile；
- $\rho^C$：compute resolution；
- $r$：resource binding / resource class；
- $\chi$：execution / composition contract reference。

Runtime MUST NOT 將 basis cell 當作完整 executor contract。

## 7.3 Versioned addressing

Canonical human-readable address SHOULD 類似：

```text
GCM:v0.2/B:D/U:R/I:D/L:K
```

Legacy `O:` MAY 被 parser 接受，但 canonical emitter SHOULD 輸出 `I:`。

對 schema version $v$：

$$
\operatorname{addr}_v:
\mathfrak P^{(v)}
\rightarrow
\mathsf{ID}_v.
$$

但：

$$
\boxed{
\text{Numeric ID}
\neq
\text{Semantic Identity Across Versions}.
}
$$

若新版 configuration 無法安全投影回舊版，compatibility projection MUST 可失敗：

$$
\pi_{v'\rightarrow v}(\beta')
\uparrow.
$$

Runtime MUST NOT 為了 backward compatibility 強制 lossy projection 而隱藏語義差異。

---

# 8. Domain 與 configuration assignment

令：

$$
\mathcal D_\nu
=
\{D_1,\ldots,D_n\}.
$$

configuration assignment：

$$
\boxed{
\Gamma_\nu:
\mathcal D_\nu
\rightarrow
\mathfrak G^{(v)}.
}
$$

Domain MUST NOT 被默認為 physical spatial region：

$$
\boxed{
\text{Domain}
\neq
\text{Physical Space}.
}
$$

只有在 domain contract 明確具有 physical / spacetime binding 時，MAY 額外註冊對應 relation。

---

# 9. Canonical operation types

Operation MUST typed。

$$
\boxed{
\mathsf{OpType}
\in
\{
\mathsf{Observe},
\mathsf{Compute},
\mathsf{Materialize},
\mathsf{ModifyState},
\mathsf{Commit},
\mathsf{ModifyRule},
\mathsf{ModifyFoundation}
\}.
}
$$

最小 operation request：

$$
\boxed{
\boldsymbol\omega
=
\left\langle
\mathsf{id},
\mathsf{type},
\mathsf{target},
\mathsf{scope},
\mathsf{input},
\mathsf{desiredEffect},
\mathsf{post},
\mathsf{requester}
\right\rangle.
}
$$

Untyped request MUST NOT 直接進入 ordinary execution path。

---

# 10. Operation control contract

最小 operation control contract：

$$
\boxed{
\mathfrak C_{\mathrm{op}}
=
\left\langle
T,
S,
\mathcal I_{\mathrm{keep}},
\Delta_{\mathrm{allow}},
\mathsf{AdmReq},
\mathsf{VerifyReq},
\mathsf{RollbackReq},
\mathsf{PermReq}
\right\rangle.
}
$$

其中：

- $T$：target；
- $S$：scope；
- $\mathcal I_{\mathrm{keep}}$：必須保持的 invariants；
- $\Delta_{\mathrm{allow}}$：允許 effects；
- $\mathsf{AdmReq}$：admissibility obligations；
- $\mathsf{VerifyReq}$：verification obligations；
- $\mathsf{RollbackReq}$：rollback / recovery obligations；
- $\mathsf{PermReq}$：required authority classes。

Runtime MUST NOT 只因 operation technically callable 就省略上述 contract obligations。

---

# 11. Authority model

最小 authority profile：

$$
\boxed{
\mathsf{AuthProfile}(A)
=
\left\langle
P_{\mathrm{observe}},
P_{\mathrm{compute}},
P_{\mathrm{materialize}},
P_{\mathrm{state}},
P_{\mathrm{commit}},
P_{\mathrm{rule}},
P_{\mathrm{foundation}}
\right\rangle.
}
$$

Runtime MUST 保持：

$$
P_{\mathrm{observe}}=1
\not\Rightarrow
P_{\mathrm{state}}=1,
$$

$$
P_{\mathrm{state}}=1
\not\Rightarrow
P_{\mathrm{commit}}=1,
$$

$$
P_{\mathrm{commit}}=1
\not\Rightarrow
P_{\mathrm{rule}}=1,
$$

$$
P_{\mathrm{rule}}=1
\not\Rightarrow
P_{\mathrm{foundation}}=1.
$$

對 required authority set：

$$
\mathsf{ReqAuth}(\boldsymbol\omega)
$$

定義：

$$
\boxed{
\mathsf{AuthOK}_\mu
(A,\boldsymbol\omega,S)
:=
\bigwedge_{a\in\mathsf{ReqAuth}(\boldsymbol\omega)}
\mathsf{Auth}_\mu(A,a,S).
}
$$

## 11.1 Authority non-escalation

Ordinary routing MUST 滿足：

$$
\boxed{
\mathsf{AuthOut}
\preceq
\mathsf{AuthIn}
\oplus
\mathsf{ExplicitDelegation}.
}
$$

因此：

$$
\boxed{
\text{Route Search}
\not\Rightarrow
\text{Privilege Escalation}.
}
$$

AI planner、optimizer、scheduler、executor 或 bridge MUST NOT 因找到更有效的方法而自行取得更深 authority。

---

# 12. Reachability、Admissibility 與可供域

GCM MUST 區分：

$$
\mathfrak A_{\mathrm{struct}},
$$

$$
\mathfrak A_{\mathrm{adm}},
$$

$$
\mathfrak A_{\mathrm{run}}.
$$

理想 conformant relation：

$$
\boxed{
\mathfrak A_{\mathrm{run}}
\subseteq
\mathfrak A_{\mathrm{adm}}
\subseteq
\mathfrak A_{\mathrm{struct}}.
}
$$

但 authority 仍 MUST 獨立判定。

Reachability：

$$
\mathsf{Reach}_\mu(A,\boldsymbol\zeta)
\in
\{0,1\}
$$

MAY 依 resource、service、device、model、bridge、network、memory 或 control interface 改變，且不是單調關係。

Admissibility：

$$
\boxed{
\mathsf{Adm}_{B_W,\mu}^{(v)}
(\boldsymbol\omega,\boldsymbol\zeta)
\in
\{0,1\}.
}
$$

最低 obligations SHOULD 包含：

- TypeOK；
- DomainOK；
- LawOK；
- InvariantPreOK；
- BridgePreOK；
- EffectBoundaryOK；
- FoundationOK。

因此：

$$
\boxed{
\text{Can Execute}
\neq
\text{May Execute}.
}
$$

---

# 13. Candidate route record

最小 route candidate：

$$
\boxed{
\boldsymbol\zeta
=
\left\langle
\mathcal D_{\boldsymbol\omega},
\gamma,
E,
\mathsf{Br},
q,
\sigma,
\chi
\right\rangle.
}
$$

其中：

- $\mathcal D_{\boldsymbol\omega}$：target domain set；
- $\gamma$：full Runtime configuration；
- $E$：executor / executor family；
- $\mathsf{Br}$：bridge / bridge chain；
- $q$：resource binding；
- $\sigma$：scheduling / ordering metadata；
- $\chi$：composition contract reference。

Route candidate existence MUST NOT 被視為 legality proof。

---

# 14. Pre-execution gate

定義：

$$
\boxed{
\begin{aligned}
&\mathsf{PreExecOK}_{\mu}^{(v)}
(A,\boldsymbol\omega,\boldsymbol\zeta)
\\
&:=
\mathsf{Addr}^{(v)}(\boldsymbol\zeta)
\land
\mathsf{Reach}_\mu(A,\boldsymbol\zeta)
\land
\mathsf{Adm}_{B_W,\mu}^{(v)}(\boldsymbol\omega,\boldsymbol\zeta)
\land
\mathsf{AuthOK}_\mu(A,\boldsymbol\omega,S)
\land
\mathsf{ExecContractOK}_\mu(\boldsymbol\zeta)
\land
\mathsf{BridgeOK}_\mu(\boldsymbol\zeta).
\end{aligned}
}
$$

若：

$$
\mathsf{PreExecOK}=0,
$$

ordinary execution MUST NOT 發生。

Optimization MUST 只在 safe candidate set 內進行。

$$
\boxed{
\text{Admissibility / Authority / Contract Gates First}
\rightarrow
\text{Optimization Second}.
}
$$

並維持：

$$
\boxed{
\text{Mathematics}
\neq
\text{Optimization}.
}
$$

---

# 15. Local executor contract

每個 executor SHOULD 暴露：

$$
\boxed{
\mathfrak E_i
=
\left\langle
\mathsf{id}_i,
\mathsf{Cap}_i,
\mathsf{In}_i,
\mathsf{Out}_i,
\mathsf{Pre}_i,
\mathsf{Eff}_i,
\mathsf{Inv}_i,
\mathsf{Res}_i,
\mathsf{Cost}_i,
\mathsf{Fail}_i,
\mathsf{Hist}_i
\right\rangle.
}
$$

Contract interface MUST NOT 被等同 internal algorithm。

Black-box executor MAY 被使用，但只有在 contract 足以完成 required validation 時才可進 ordinary commit path。

Executor MUST 產生 proposal，而不是直接寫入 canonical World：

$$
\boxed{
E_i
\left(
W_\nu\vert_{D_i},
\Xi_\mu,
\gamma_i,
\mathsf{input}
\right)
\rightarrow
\delta_i.
}
$$

因此：

$$
\boxed{
\text{Executor Output}
\neq
W_{\nu+1}.
}
$$

---

# 16. Representation bridge contract

Canonical bridge notation：

$$
\boxed{
\mathsf{Br}_{p\rightarrow q}:
S_p
\rightharpoonup
S_q.
}
$$

最小 bridge contract：

$$
\boxed{
\mathfrak C^{\mathrm{Br}}_{p\rightarrow q}
=
\left\langle
S_p,
S_q,
\mathsf{Pre},
\mathsf{Post},
\mathsf{InvKeep},
\epsilon,
\mathsf{Rev},
\mathsf{Cost},
\mathsf{Fail}
\right\rangle.
}
$$

Runtime MUST NOT 以「程式型別可轉換」代替 semantic preservation proof。

若 bridge error semantics unknown，Runtime SHOULD fail closed 或 Defer / Escalate。

$$
\boxed{
\text{Representable}
\not\Rightarrow
\text{Semantically Preserved}.
}
$$

---

# 17. Reconciliation、Verification 與 Commit

Local proposals：

$$
\Delta_\nu
=
\{\delta_1,\ldots,\delta_k\}.
$$

Reconciliation：

$$
\boxed{
\mathsf{Reconcile}_{B_W,\mathcal C}
:
(W_\nu,\Delta_\nu)
\rightharpoonup
\widetilde W_{\nu+1}.
}
$$

Verification：

$$
\boxed{
\mathsf{Verify}^{(v)}_{B_W}
(W_\nu,\widetilde W_{\nu+1}).
}
$$

Committability：

$$
\boxed{
\mathsf{CommitOK}_{B_W,\nu}^{(v)}
(\Delta_\nu,\widetilde W_{\nu+1})
\in
\{0,1\}.
}
$$

只有在 required commit gate 通過時，才可：

$$
W_{\nu+1}
:=
\widetilde W_{\nu+1}.
$$

否則保持：

$$
W_{\nu+1}
=
W_\nu
$$

MAY 是合法 outcome。

因此：

$$
\boxed{
\text{Local Execution Success}
\not\Rightarrow
\text{Global Commit}.
}
$$

---

# 18. Route disposition

Canonical disposition：

$$
\boxed{
\mathsf{Disposition}
\in
\{
\mathsf{Execute},
\mathsf{Defer},
\mathsf{Refuse},
\mathsf{Idle},
\mathsf{Escalate}
\}.
}
$$

規範：

- `Execute`：存在 safe route；
- `Defer`：目前條件不足但不形成永久拒絕；
- `Refuse`：存在 hard violation；
- `Idle`：目前無需動作；
- `Escalate`：ordinary Runtime 無權決定，但存在明確更高 governance path。

Runtime MUST NOT 將 `Refuse` 偽裝成 `Defer` 以繞過 hard prohibition；亦 MUST NOT 將 `Escalate` 自動轉成 self-authorized execution。

---

# 19. Observation、Projection 與 Materialization

GCM MUST 保持：

$$
\boxed{
\text{Computation}
\neq
\text{Observation}
\neq
\text{Materialization}.
}
$$

純 observation transaction：

$$
\boxed{
(W_\nu,\Xi_\mu,O_\omega)
\xrightarrow{\mathsf{Observe}(q)}
(W_\nu,\Xi_{\mu'},O_{\omega'},Y_q).
}
$$

因此 pure observation MAY：

$$
\Delta\Xi\neq0,
$$

也 MAY：

$$
\Delta O\neq0,
$$

但 MUST 保持：

$$
\boxed{
\Delta W=0.
}
$$

## 19.1 Projection contract

最小 projection contract：

$$
\boxed{
\mathfrak C_\Pi
=
\left\langle
S,
\mathsf{InputVersion},
\mathsf{ProjectionSemantics},
\rho^O,
\mathsf{ConsistencyClass},
\mathsf{ApproxBound},
\mathsf{VisibilityPolicy},
\mathsf{EvidencePolicy}
\right\rangle.
}
$$

## 19.2 Materialization contract

最小 materialization contract：

$$
\boxed{
\mathfrak C_{\mathsf{Mat}}
=
\left\langle
x,
\mathsf{RepresentationType},
\rho,
\mathsf{SourceVersion},
\mathsf{Freshness},
\mathsf{CostClass},
\mathsf{Evictability},
\mathsf{Provenance}
\right\rangle.
}
$$

Materialized artifact MUST NOT 被默認為 canonical current state：

$$
\boxed{
\mathsf{Mat}(x)
\not\Rightarrow
\mathsf{Canonical}(x).
}
$$

且：

$$
\boxed{
\neg\mathsf{Mat}(x)
\not\Rightarrow
\neg x.
}
$$

---

# 20. Resolution、scale 與 ordering type separation

Runtime MUST 區分：

$$
\boxed{
\rho^C
\neq
\rho^O
\neq
\mathsf{Mat}
\neq
\lambda^{ST}.
}
$$

Resolution SHOULD 被實作成 typed preorder，而不是假設所有解析度可壓成單一 scalar。

GCM 亦 MUST 區分：

$$
\boxed{
\text{World Evolution}
\neq
\text{Runtime Scheduling}
\neq
\text{Observer Time}
\neq
\text{Commit Order}
\neq
\text{History Order}.
}
$$

因此：

$$
\boxed{
\text{Global Coherence}
\not\Rightarrow
\text{Global Synchronization}.
}
$$

---

# 21. Active support、dormancy 與 finite realization

GCM MUST 允許：

$$
\boxed{
\text{Finite Active Realization}
+
\text{Unbounded Extensibility}.
}
$$

對 active support：

$$
|\mathsf{Act}_\mu|<\infty
$$

不足以證明 Runtime cost 有界。

Hard resource classes $k\in\mathcal K_R^{\mathrm{hard}}$ SHOULD 滿足：

$$
\boxed{
\mathsf{Use}_k
(\mathsf{Act}_\mu,\Xi_\mu)
\le
B_{\mu,k}.
}
$$

## 21.1 Lifecycle predicates

Runtime MUST NOT 強迫 Active / Materialized / Dormant / Archived / Potential 成為單一互斥列。

至少區分：

- $\mathsf{Active}_\mu(x)$ ；
- $\mathsf{Dormant}_\mu(x)$ ；
- $\mathsf{Archived}_\mu(x,a)$ ；
- $\mathsf{Pot}_\mu(x)$ ；
- $\mathsf{Mat}_\mu(x,\rho,c)$ ；
- $\mathsf{Pin}^{\mathrm{Act}}_\mu(x)$ ；
- $\mathsf{Pin}^{\mathrm{Mat}}_\mu(x)$ ；
- $\mathsf{Pin}^{\mathrm{Ret}}_\mu(x)$。

因此：

$$
\boxed{
\mathsf{Reactivate}
\neq
\mathsf{Materialize}.
}
$$

$$
\boxed{
\mathsf{Potential}
\neq
\mathsf{CanonicalExistence}.
}
$$

## 21.2 Active horizon

Active horizon 使用：

$$
\boxed{
\mathsf{Hor}_\mu
}
$$

而 MUST NOT 使用 $\mathcal H$。

且：

$$
\boxed{
\text{Active Horizon}
\neq
\text{Active Set}.
}
$$

## 21.3 Dormancy modes

Dormancy contract SHOULD explicit 指定：

- Freeze；
- Coarse Evolution；
- Event Accumulation / Replay；
- Delegated Surrogate；
- 或 versioned extension mode。

Dormant MUST NOT 被默認為 semantic freeze。

---

# 22. Archive 與 reactivation contract

Archived object MUST NOT 被默認為 deleted：

$$
\boxed{
\mathsf{Archived}(x)
\not\Rightarrow
\neg x.
}
$$

Archive anchor SHOULD 至少保留：

- object identity；
- source World version；
- Foundation / schema version；
- locator；
- checkpoint / seed / summary；
- invariant digest；
- history pointer；
- integrity digest；
- restore mode；
- approximation/error certificate when applicable。

Reactivation SHOULD 經：

$$
\boxed{
\mathsf{Locate}
\rightarrow
\mathsf{Load}
\rightarrow
\mathsf{Decode}
\rightarrow
\mathsf{Reconstruct}
\rightarrow
\mathsf{CatchUp}
\rightarrow
\mathsf{Validate}
\rightarrow
\mathsf{Rebind}
\rightarrow
\mathsf{Activate}.
}
$$

因此：

$$
\boxed{
\text{Load Success}
\not\Rightarrow
\text{Reactivation Success}.
}
$$

---

# 23. Resource feasibility 與 cost discipline

Runtime MUST NOT 將 resource feasibility 等同 optimization。

$$
\boxed{
\text{Resource Feasibility}
\neq
\text{Optimization Objective}.
}
$$

Step cost MAY 分解為：

$$
\boxed{
C_\mu^{\mathrm{step}}
=
C_\mu^{\mathrm{exec}}
+
C_\mu^{\mathrm{reconcile}}
+
C_\mu^{\mathrm{index}}
+
C_\mu^{\mathrm{projection}}
+
C_\mu^{\mathrm{lifecycle}}
+
C_\mu^{\mathrm{history}}.
}
$$

並維持：

$$
\boxed{
\text{Bounded Active Semantics}
\neq
\text{Bounded Runtime Cost}.
}
$$

TW-02 SHOULD 將 support-local cost、index lookup、history access 與 archive access 分開量測。

---

# 24. Canonical history / provenance model

GCM history MUST 為 typed provenance structure，而不是未型別化 log sequence。

最小 semantic structure：

$$
\boxed{
\mathcal H_\eta
=
\left\langle
V_H,
E_H,
\mathsf{Type},
\mathsf{Anchor},
\mathsf{PayloadRef},
\mathsf{Policy}
\right\rangle.
}
$$

Runtime MUST 區分至少：

$$
\boxed{
\prec_{\mathsf{exec}}
\neq
\prec_{\mathsf{causal}}
\neq
\prec_{\mathsf{commit}}
\neq
\prec_{\mathsf{log}}
\neq
\prec_{\mathsf{observer}}
\neq
\prec_{\mathsf{foundation}}.
}
$$

因此：

$$
\boxed{
\text{Log Order}
\neq
\text{Causal Order}
\neq
\text{Commit Order}.
}
$$

---

# 25. Canonical receipt

最小 event receipt：

$$
\boxed{
\mathsf{Rec}(e)
=
\left\langle
\mathsf{id},
\mathsf{type},
\mathsf{status},
\mathsf{actor},
\mathsf{scope},
\mathsf{authorityCtx},
\mathsf{worldAnchor},
\mathsf{runtimeAnchor},
\mathsf{observerAnchor},
\mathsf{foundationVersion},
\mathsf{configuration},
\mathsf{law},
\mathsf{bridge},
\mathsf{inputRef},
\mathsf{outputRef},
\mathsf{invariantRef},
\mathsf{verification},
\mathsf{resource},
\mathsf{timeAnn},
\mathsf{relations}
\right\rangle.
}
$$

Inapplicable fields MAY 為 null / omitted，但語義角色 MUST NOT 因此被合併。

Payload MAY 外置，但 anchor MUST 保留足以解釋其：

- semantic role；
- version；
- exact / approximate / unavailable status；
- redaction / expiry reason；
- replay / audit consequence。

---

# 26. Proposal、Commit、Rollback、Compensation

Runtime MUST 區分：

$$
\boxed{
\mathsf{Reject}
\neq
\mathsf{Abort}
\neq
\mathsf{Rollback}
\neq
\mathsf{Compensation}.
}
$$

Rollback MUST NOT 刪除已發生 event：

$$
\boxed{
\text{Rollback}
\neq
\text{Erase History}.
}
$$

Compensation 是新的 history event：

$$
\boxed{
\text{Compensation}
\neq
\text{No Prior Event}.
}
$$

Retry 亦 MUST 被視為 reliability history，而不是自動被覆寫成「一次成功」。

---

# 27. History equivalence、compression 與 replay

State equality MUST NOT 被視為 history equality：

$$
\boxed{
W_a=W_b
\not\Rightarrow
\mathcal H_a=\mathcal H_b.
}
$$

History equivalence MUST 相對 semantics profile：

$$
H_1
\sim_{\mathbb S}
H_2.
$$

可能的 profile 維度包括：

- Endpoint；
- Safety；
- Observer；
- Cost；
- Audit；
- Causal；
- Replay；
- Governance。

若 equivalence unknown：

$$
\boxed{
\text{Unknown History Equivalence}
\Rightarrow
\text{No Merge By Default}.
}
$$

## 27.1 Replay grade

Canonical replay grade：

$$
\boxed{
\mathsf{ReplayGrade}
\in
\{
\mathsf{Exact},
\mathsf{DeterministicInternal},
\mathsf{SemanticEquivalent},
\mathsf{Approximate},
\mathsf{NonReplayable}
\}.
}
$$

Runtime MUST 降低不具 prerequisite 的 replay claim，而不能把 approximate replay 標成 Exact。

## 27.2 History compression certificate

若 history 被 quotient / compact，SHOULD 產生：

$$
\boxed{
\mathsf{HistCert}
=
\left\langle
\mathsf{inputRange},
\mathsf{profileVersion},
\mathsf{method},
\mathsf{preservedQueries},
\mathsf{lostQueries},
\mathsf{verifier},
\mathsf{digest},
\mathsf{outputAnchor}
\right\rangle.
}
$$

History transformation 自身 SHOULD 有 provenance。

---

# 28. Foundation revision protocol

Ordinary Runtime transition MUST 保持：

$$
\boxed{
\mathcal F^{(v)}
\rightarrow
\mathcal F^{(v)}.
}
$$

Foundation revision 必須走 explicit operation：

$$
\boxed{
\mathsf{ReviseFoundation}:
\mathcal F^{(v)}
\rightarrow
\mathcal F^{(v+1)}.
}
$$

任何下列行為 MUST NOT 隱式觸發 Foundation revision：

- route optimization；
- AI planner self-tuning；
- executor fallback；
- configuration switching；
- Observer interaction；
- resource pressure；
- history compression；
- failed local execution。

Foundation revision SHOULD 至少保留：

- prior version；
- proposed version；
- rationale；
- authority / governance proof；
- migration policy；
- verification result；
- accepted / rejected / forked disposition；
- lineage receipt。

---

# 29. Configuration schema extension 與 Foundation boundary

Configuration basis / registry MAY 擴張，但 extension MUST explicit versioned。

新增：

- axis value；
- orthogonal axis；
- domain-specific profile；

不自動等於 World Foundation revision。

但若 configuration schema extension 改變某 deployment 的合法 operation semantics、World invariants 或 governing axioms，則部署層 MAY 要求相應 Foundation governance。

Runtime MUST NOT 自行決定這兩個版本層「其實是一樣的」。

---

# 30. Canonical failure policy

當 required semantics 無法判定時，Runtime SHOULD 優先採用：

$$
\boxed{
\text{Fail Closed}
\lor
\mathsf{Defer}
\lor
\mathsf{Escalate}
}
$$

而不是默認 Execute。

典型 unknown 包括：

- unknown bridge error；
- unresolved authority；
- stale Foundation reference；
- invalid configuration version；
- unverifiable archive reconstruction；
- unknown history equivalence；
- missing replay prerequisites；
- ambiguous World boundary。

---

# 31. Canonical API surface — conceptual minimum

TW-02 可自由選擇具體語言與 transport，但 SHOULD 能映射到下列概念 API。

## 31.1 Configuration registry

```text
register_basis_schema(version, axes)
register_profile(profile, contract_ref)
resolve_address(canonical_key)
query_candidates(domain, task_signature)
bind_configuration(domain, configuration_ref)
project_compatibility(from_version, to_version)
record_switch(domain, old_ref, new_ref, reason)
```

## 31.2 Route / authority

```text
enumerate_routes(operation, domain_set, registry)
check_reachability(agent, route, runtime_state, resources)
check_admissibility(operation, route, foundation, constraints)
check_authority(agent, operation, scope)
validate_executor_contract(route)
validate_bridge_contract(route)
select_route(safe_routes, policy)
execute_as_proposal(route, inputs)
reconcile(world, proposals, constraints)
verify_global(old_world, candidate_world, foundation)
commit(candidate_world)
rollback_or_discard(proposals)
```

## 31.3 Observer / materialization

```text
observe(request)
materialize(request)
refresh(view_id)
inspect_provenance(view_id)
change_observer_state(observer_patch)
propose_intervention(operation)
```

`observe(...)` MUST NOT 隱式切換成 `propose_intervention(...)`。

## 31.4 Resource / lifecycle

```text
inspect_active_support()
inspect_resource_envelope()
propose_activation(unit_id, reason)
propose_dormancy(unit_id, mode)
request_pin(unit_id, pin_class)
archive(unit_id, policy)
restore(unit_id, target_mode)
estimate_wake_cost(unit_id)
inspect_boundary_summary(unit_id)
validate_budget(candidate_support)
```

`request_pin(...)` MUST 經 authority；`restore(...)` MUST NOT 因 load success 自動 World commit。

## 31.5 History

```text
append_typed_receipt(event)
append_relation(edge_type, from_id, to_id)
query_history(query_contract)
inspect_lineage(anchor)
checkpoint(policy)
replay(target, replay_contract)
propose_history_compaction(range, semantics_profile)
verify_history_equivalence(h1, h2, semantics_profile)
apply_history_transform(certificate)
```

---

# 32. Minimum canonical runtime pipeline

GCM Reference Runtime SHOULD 可映射到下列 lifecycle：

```text
Operation Request
    ↓
Type / Domain Resolution
    ↓
Configuration Candidate Enumeration
    ↓
Reachability Gate
    ↓
Admissibility Gate
    ↓
Authority Gate
    ↓
Executor / Bridge Contract Gate
    ↓
Safe Route Selection
    ↓
Execute as Proposal
    ↓
Cross-Domain Reconciliation
    ↓
Global Verification
    ↓
Commit / Reject / Rollback / Compensation Path
    ↓
Typed Receipt + Relation Update
    ↓
Observer / Materialization Refresh as Needed
    ↓
Lifecycle / Resource Update
    ↓
History Index / Checkpoint / Compression Policy
```

這不是唯一 implementation graph，但任何簡化 MUST 能證明沒有跨越上述語義 gate。

---

# 33. Core canonical invariants — TW-01

以下條款為 TW-01 v0.1 的核心合規不變量。

## GCM-C01 — World / Runtime Separation

$$
\boxed{
\mathcal M_G
\neq
\mathbf W.
}
$$

## GCM-C02 — Heterogeneous Globality

$$
\boxed{
\text{Global Computation}
=
\text{Globally Coherent Heterogeneous Computation}.
}
$$

## GCM-C03 — Boundary-relative Globality

$$
\boxed{
\text{Globality is relative to a designated World boundary}.
}
$$

## GCM-C04 — 24/72 Non-exhaustiveness

$$
\boxed{
24/72
\neq
\text{Exhaustive Set of All Computation}.
}
$$

## GCM-C05 — Computation / Observation / Materialization Separation

$$
\boxed{
\text{Computation}
\neq
\text{Observation}
\neq
\text{Materialization}.
}
$$

## GCM-C06 — Observer Non-Mutation

Projection-only operation MUST satisfy：

$$
\boxed{
\Delta W=0.
}
$$

## GCM-C07 — Global Dependency / Full Materialization Separation

$$
\boxed{
\text{Global Dependency}
\neq
\text{Full Materialization}.
}
$$

## GCM-C08 — Recursive Globality / Full Expansion Separation

$$
\boxed{
\text{Recursive Globality}
\neq
\text{Recursive Full Expansion}.
}
$$

## GCM-C09 — Finite Active Realization

$$
\boxed{
\text{Finite Active Realization}
+
\text{Unbounded Extensibility}.
}
$$

## GCM-C10 — State / History Separation

$$
\boxed{
\text{State Equality}
\not\Rightarrow
\text{History Equality}.
}
$$

## GCM-C11 — Endpoint / History Closure Separation

$$
\boxed{
\text{Endpoint Closure}
\neq
\text{History Closure}.
}
$$

## GCM-C12 — Operation Layer Separation

$$
\boxed{
\text{State Edit}
\neq
\text{Rule Edit}
\neq
\text{Foundation Revision}.
}
$$

## GCM-C13 — Capability / Authority Separation

$$
\boxed{
\text{Can Execute}
\neq
\text{May Execute}.
}
$$

## GCM-C14 — Proposal / Commit Separation

$$
\boxed{
\text{Executor Output}
\neq
\text{Canonical World Commit}.
}
$$

## GCM-C15 — Local / Global Success Separation

$$
\boxed{
\text{Local Success}
\not\Rightarrow
\text{Global Commit}.
}
$$

## GCM-C16 — Global Coherence / Synchronization Separation

$$
\boxed{
\text{Global Coherence}
\not\Rightarrow
\text{Global Synchronization}.
}
$$

## GCM-C17 — Domain / Physical Space Separation

$$
\boxed{
\text{Domain}
\neq
\text{Physical Space}.
}
$$

## GCM-C18 — Mathematics / Optimization Separation

$$
\boxed{
\text{Mathematics}
\neq
\text{Optimization}.
}
$$

## GCM-C19 — Authority Non-Escalation

$$
\boxed{
\mathsf{AuthOut}
\preceq
\mathsf{AuthIn}
\oplus
\mathsf{ExplicitDelegation}.
}
$$

## GCM-C20 — Foundation Constancy of Ordinary Runtime

$$
\boxed{
\mathcal F^{(v)}
\rightarrow
\mathcal F^{(v)}.
}
$$

## GCM-C21 — Resolution Type Separation

$$
\boxed{
\rho^C
\neq
\rho^O
\neq
\mathsf{Mat}
\neq
\lambda^{ST}.
}
$$

## GCM-C22 — Lifecycle Type Separation

$$
\boxed{
\mathsf{Reactivate}
\neq
\mathsf{Materialize}.
}
$$

## GCM-C23 — Potential / Existence Separation

$$
\boxed{
\mathsf{Potential}
\neq
\mathsf{CanonicalExistence}.
}
$$

## GCM-C24 — Bounded Active / Bounded Cost Separation

$$
\boxed{
\text{Bounded Active Semantics}
\neq
\text{Bounded Runtime Cost}.
}
$$

## GCM-C25 — Typed Order Separation

$$
\boxed{
\prec_{\mathsf{exec}}
\neq
\prec_{\mathsf{causal}}
\neq
\prec_{\mathsf{commit}}
\neq
\prec_{\mathsf{log}}.
}
$$

## GCM-C26 — Rollback Persistence

$$
\boxed{
\text{Rollback}
\neq
\text{Erase History}.
}
$$

## GCM-C27 — Unknown History Equivalence Safety

$$
\boxed{
\text{Unknown History Equivalence}
\Rightarrow
\text{No Merge By Default}.
}
$$

## GCM-C28 — Foundation Revision Governance

$$
\boxed{
\text{Foundation Revision is explicit, versioned, and auditable}.
}
$$

---

# 34. Canonical compatibility rules

## 34.1 Parser compatibility

Runtime MAY accept legacy source notation when unambiguous，但 canonical emitter MUST 輸出目前 registry 定義的符號。

## 34.2 Semantic compatibility

Compatibility MUST NOT 只依字串、numeric ID 或 hash 判定。

## 34.3 Foundation compatibility

不同 Foundation version 之間 MUST NOT 被默認為 semantically identical。

## 34.4 History compatibility

History quotient / migration MUST 指定 semantics profile 與 version。

## 34.5 Configuration compatibility

Lossy projection MUST 可拒絕；unknown projection MUST NOT 被默認成 equivalent。

---

# 35. Canonical error classes

TW-02 SHOULD 至少對應下列 error classes：

```text
GCM_E_UNTYPED_OPERATION
GCM_E_UNKNOWN_WORLD_BOUNDARY
GCM_E_UNKNOWN_CONFIGURATION
GCM_E_UNREACHABLE_ROUTE
GCM_E_INADMISSIBLE_ROUTE
GCM_E_UNAUTHORIZED_OPERATION
GCM_E_EXECUTOR_CONTRACT
GCM_E_BRIDGE_UNKNOWN
GCM_E_BRIDGE_LOSS_EXCEEDED
GCM_E_RECONCILIATION
GCM_E_VERIFICATION
GCM_E_COMMIT_REJECTED
GCM_E_FOUNDATION_BOUNDARY
GCM_E_STALE_PROJECTION
GCM_E_RESOURCE_INFEASIBLE
GCM_E_REACTIVATION_INVALID
GCM_E_HISTORY_EQUIVALENCE_UNKNOWN
GCM_E_REPLAY_GRADE_DOWNGRADE
GCM_E_SCHEMA_VERSION
GCM_E_PROVENANCE_INCOMPLETE
```

具體 numeric code 不由 TW-01 指定。

---

# 36. Minimal machine-readable schema obligations

TW-02 SHOULD 為下列 object 提供穩定 machine-readable schema：

1. `WorldBoundaryRef`；
2. `FoundationRef`；
3. `ConfigurationRef`；
4. `OperationRequest`；
5. `OperationContract`；
6. `AuthorityContext`；
7. `RouteCandidate`；
8. `ExecutorContract`；
9. `BridgeContract`；
10. `Proposal`；
11. `VerificationResult`；
12. `CommitReceipt`；
13. `ProjectionContract`；
14. `MaterializationContract`；
15. `ActiveSupportContract`；
16. `ArchiveAnchor`；
17. `LifecycleReceipt`；
18. `EventReceipt`；
19. `HistoryRelation`；
20. `HistoryCompressionCertificate`。

每個 persisted object SHOULD 至少帶：

- `schema_version`；
- stable semantic identifier；
- source / lineage reference when applicable。

---

# 37. Specification revision rules

TW-01 的 revision MUST 版本化。

下列變更至少 SHOULD 視為 breaking / major semantic revision：

- 修改 state-plane 意義；
- 修改 canonical operation class；
- 放寬 authority inheritance；
- 允許 ordinary Runtime 修改 Foundation；
- 修改 commit gate 語義；
- 將 Observer operation 重新併入 World mutation；
- 修改 history equivalence default；
- 將 unknown bridge 自動視為 safe；
- 將 24／72 改成 exhaustive ontology。

新增 optional field、非破壞性 schema annotation 或新的 domain-specific profile MAY 是 backward-compatible revision，但仍 SHOULD 有 version / changelog。

---

# 38. Non-normative prior-art positioning

本規格不宣稱下列既有技術由 GCM 首創：

- heterogeneous Models of Computation；
- heterogeneous task / dataflow runtime；
- privilege / coherence；
- co-simulation / scheduled execution；
- representation conversion legality；
- hybrid systems；
- partial observability；
- materialized views；
- adaptive / multi-resolution modeling；
- working set / paging / external memory；
- lazy evaluation / streaming；
- virtual actor activation；
- distributed causality / logical clocks；
- provenance models；
- event sourcing；
- compensation / saga；
- partial-order reduction。

GCM 的工程主張是把這些相鄰技術常分散處理的 obligations 放入同一個 World-boundary-relative typed contract 中，並要求 state planes、authority、materialization、resource realization、commit 與 history 不可互相偷換。

---

# 39. TW-02 與 TW-03 的直接交接

## 39.1 TW-02 — Reference Runtime Architecture

TW-02 SHOULD 將本規格映射成至少以下模組：

```text
Foundation Registry
World Store
Domain Registry
Configuration Registry
Reachability / Resource Registry
Authority Engine
Admissibility Validator
Route Planner / Selector
Executor Registry
Bridge Registry
Proposal Store
Reconciliation Engine
Verification Engine
Commit / Rollback Gate
Observer / Projection Service
Materialization Manager
Active Support / Lifecycle Manager
History / Provenance Store
History Index / Summary
Foundation Lineage Registry
```

## 39.2 TW-03 — Conformance / Verification

TW-03 MUST 將本文件中的 GCM-C01–GCM-C28 轉成可執行或可審計 conformance tests，並建立 failure evidence、test vector 與 implementation profile。

---

# 40. Reference Runtime MVP 的最低映射

MVP v0.1 仍分五個 Milestone：

## M0 — Canonical Kernel

最低實作：

- World / Runtime / Observer / Foundation / History state-plane；
- versioned registries；
- canonical identifiers；
- typed operation objects。

## M1 — Reachability / Admissibility / Authority

最低驗證：

$$
\text{Can}
\neq
\text{May}.
$$

並測 authority non-escalation。

## M2 — Heterogeneous Execution

至少 3–5 個 representative executors；不要求實作全部 72 cells。

## M3 — Reconciliation / Verify / Commit / History

最低驗證：

$$
\text{Proposal}
\neq
\text{Commit}.
$$

並建立 typed receipts。

## M4 — Bounded Active Runtime

驗證：

$$
\text{Global Dependency}
\neq
\text{Full Materialization},
$$

$$
\text{Recursive Globality}
\neq
\text{Recursive Full Expansion},
$$

並執行 TW-03 conformance suite。

---

# 41. 最終 Canonical Contract

一個 Runtime 若要宣稱其核心行為符合 GCM v0.1，最低必須滿足：

$$
\boxed{
\begin{aligned}
&\text{World-boundary-relative global coherence}
\\
+&\text{typed state-plane separation}
\\
+&\text{versioned computational configuration addressing}
\\
+&\text{reachability / admissibility / authority separation}
\\
+&\text{proposal / reconciliation / verification / commit separation}
\\
+&\text{Observer / projection / materialization separation}
\\
+&\text{finite active realization with explicit lifecycle}
\\
+&\text{typed provenance and history semantics}
\\
+&\text{explicit Foundation revision governance}.
\end{aligned}
}
$$

因此，GCM-compliant Runtime 的最低精神不是：

> 「它能調用很多種計算方法。」

而是：

> **它知道自己正在對哪個 World boundary、哪個 state plane、哪個 configuration、哪個 operation、哪個 authority scope、哪組 invariants 與哪段 history 做事；局部 executor 的成功不會自動升格為 World truth，而任何跨層改變都必須經由 explicit typed contract、verification、commit 或 versioned governance。**

這就是 TW-01 v0.1 的 canonical formal contract。

---

# Appendix A. Source-to-spec traceability

| TW-01 area | Primary source lineage |
|---|---|
| World / Runtime / Observer / Foundation | Series-00, Paper-01 |
| 24／72 basis / configuration registry | Paper-02 |
| Reachability / admissibility / authority / route | Paper-03 |
| Observation / projection / materialization / resolution | Paper-04 |
| Active support / dormancy / archive / resources | Paper-05 |
| Typed history / replay / rollback / provenance | Paper-06 |

---

# Appendix B. Deprecated shorthand

以下 notation 只可出現在歷史對照或 migration parser，不應成為新 canonical source：

- 未型別化 $W_t$ ；
- $\Gamma_t$ ；
- 以 $\mathcal H_t$ 表示 active horizon；
- 以 $\Lambda$ 同時表示 resolution / materialization / scale；
- 以 $\mathfrak O_3$ 表示 actual Observer；
- 以 $B_{p\rightarrow q}$ 表示 representation bridge；
- 以單一 $P$ 表示 Potential / Pin / Permission；
- 以單一 $R$ 表示 Route / Receipt / Archive status。

---

# Canonical Handoff

本文件完成後，後續實作文件不得再依聊天印象重建 GCM 核心語義。

**下一份工程文件：**

`TW-02_GCM_Reference_Runtime_Architecture_v0.1.md`

應以上述 TW-01 v0.1 為直接 normative input；若 TW-02 發現本規格存在不可實作、互相衝突或缺失的 MUST 條款，應提交 explicit specification issue / revision，而不是由 Runtime implementation 靜默修正語義。
