# EveMissLab Ontology Genealogy & Symbol Migration Map v0.1
## 本體論歷史譜系、符號解纏與正典遷移規格

- 文件類型：Genealogy / Symbol Migration Canon
- 版本：v0.1
- 日期：2026-08-15
- 狀態：Working Canon Companion
- 上游文件：`EveMissLab Ontology Canon v0.1`
- 目的：保存歷史語義，同時阻止跨版本、跨理論、跨 Runtime 的符號污染

---

# 0. 核心原則

本文件處理的問題不是「哪一個舊符號是錯的」，而是：

$$
\boxed{
\text{同一個字母在不同歷史層、不同理論與不同 Runtime 中曾承擔不同語義。}
}
$$

因此本文件不回寫舊論文，而建立：

$$
\boxed{
\text{Historical Symbol}
\rightarrow
\text{Typed Namespace}
\rightarrow
\text{Canonical Successor}.
}
$$

最重要的新規則：

$$
\boxed{
\text{Canonical symbols are namespace-unique, not globally unique across the entire corpus.}
}
$$

亦即：

> 正典符號只要求在明確 namespace 中唯一；跨 EveMissLab 全理論庫，不得看到裸符號就假設它具有唯一語義。

---

# 1. Migration Status 詞彙

本文件使用下列狀態。

| Status | 意義 |
|---|---|
| `KEEP` | 可繼續使用，但必須保留型別或 namespace |
| `CANONICALIZE` | 歷史概念保留，改用新的 canonical symbol/name |
| `SPECIALIZE` | 舊概念被重新定位為更大母概念的一個 subtype |
| `REFINE` | 舊概念保留，但被拆成更精細的 operator family / typed structure |
| `DEPRECATE-BARE` | 裸符號停止作為跨理論正典；歷史文件保留 |
| `HISTORICAL` | 僅作 provenance / lineage 使用 |
| `OPEN` | 關係尚未證明，不得寫成 identity/equivalence |
| `LOCAL-ONLY` | 僅在原論文或局部模型內有效，不進入 Ontology Canon |

---

# 2. 歷史譜系總圖

目前可可靠重建的主線不是單一直線，而是一棵多分支 DAG：

```text
Proto relational / state-space intuitions
        |
        +--> 2026-01-11  Triadic Unity Ontology (TUO)
        |       E_theta / C_t / V_phi
        |       Expansion / Connection / Convergence
        |       |
        |       +--> 2026-01  GCPR-RWL / Axiom operational branch
        |       |       E / C / V / Co / Pi / R / K
        |       |       Co = synchronization / snapshot
        |       |       |
        |       |       +------------------------------+
        |       |                                      |
        |       +--> 2026-04-06 Triadic Flux            |
        |               E-ing / C-ing / V-ing           |
        |                                                |
        +--> DCO lineage                                 |
        |       DCO 3.x: Cl as basic unit               |
        |       DCO 4.x: Cl-1 ... Cl-4                  |
        |       DCO 5.0: Cl-0 ... Cl-9                  |
        |       Closure-as-Process                      |
        |       |
        |       +--> Closure precedes Circle
        |               Circle = projection / realization
        |
        +--> 2026-04-17 Triadic Universal Ontology
        |       nominal unary / operational ternary
        |
        +--> 2026-05-27 Surging Unary Ontology
        |       Phi_pre -> triad -> asymptotic unary
        |
        +--> 2026-06-01 Closure extension moratorium
        |       branch explosion / no intrinsic ranking
        |
        +--> Differential-Unitive / Delta-U-Nabla branch
        |       alternative operator realization
        |
        +--> 2026-07-26 Theory Breathing
        |       E_math / L_math / C_math / H
        |
        +--> 2026-08-13 T Query Runtime
        |       CRL = Convergent Re-linking
        |
        +--> 2026-08-15 Ontology Canon v0.1
                typed operator families
                |
                +--> SSDC
                     Shared-State Domain Coupling
                     Co_legacy becomes SSDC^sync
```

注意：

1. DCO 3.x / 4.x 的存在由 DCO 5.0 內部版本史明確證實；
2. 本輪尚未把一個特定 standalone DCO 3.x / 4.x 原稿指定為 canonical source；
3. 因此其狀態為 `HISTORICALLY-ATTESTED`，不得虛構檔名或精確版本內容；
4. 此圖表示 theory lineage，不表示每條箭頭都是數學推導。

---

# 3. Genealogy Relation Types

為避免把歷史演化誤寫成邏輯蘊含，本 Canon 使用下列關係：

$$
\boxed{
\operatorname{extends},
\operatorname{refines},
\operatorname{specializes},
\operatorname{processualizes},
\operatorname{projectsFrom},
\operatorname{operationalizes},
\operatorname{migratesTo},
\operatorname{historicallyAttestedBy},
\operatorname{openRelation}.
}
$$

不得將：

$$
A\xrightarrow{\operatorname{refines}}B
$$

改寫成：

$$
A\iff B.
$$

---

# 4. 第一組：$E/C/V$ 的歷史碰撞

## 4.1 TUO 版本

2026-01-11 TUO 使用：

$$
E_\theta
=
\text{Expansion},
$$

$$
C_t
=
\text{Connection},
$$

$$
V_\phi
=
\text{Convergence}.
$$

這是三元本體論的早期核心符號。

Canonical migration：

$$
E_\theta
\mapsto
\mathfrak E,
$$

$$
C_t
\mapsto
\mathfrak L,
$$

$$
V_\phi
\mapsto
\mathfrak C.
$$

狀態：

`REFINE`

理由：三個單算子被升級成 operator families。

---

## 4.2 FELRA / GCPR-RWL 版本

後來工程 Runtime 使用：

$$
E
=
\text{Generation},
$$

$$
C
=
\text{Check / Validation},
$$

$$
V
=
\text{Selection}.
$$

這三者雖歷史上受到 TUO 啟發，但功能已不同。

因此禁止：

$$
C_{\mathrm{FELRA}}
=
C_{\mathrm{TUO}}.
$$

Canonical migration：

$$
E_{\mathrm{FELRA}}
\mapsto
\operatorname{Gen},
$$

$$
C_{\mathrm{FELRA}}
\mapsto
\operatorname{Check},
$$

$$
V_{\mathrm{FELRA}}
\mapsto
\operatorname{Select}.
$$

狀態：

`DEPRECATE-BARE`

裸 $E,C,V$ 在跨理論文件中不再允許依賴上下文猜義。

---

# 5. 第二組：Theory Breathing 的 $\mathcal E/\mathcal L/\mathcal C/\mathcal H$

《理論呼吸論》使用：

$$
\mathcal B
=
\mathcal H
\circ
\mathcal C
\circ
\mathcal L
\circ
\mathcal E.
$$

其中：

$$
\mathcal E
=
\text{Expansion},
$$

$$
\mathcal L
=
\text{Link},
$$

$$
\mathcal C
=
\text{Convergence},
$$

$$
\mathcal H
=
\text{Rest / Freeze / Stabilization}.
$$

Canonical migration：

$$
\mathcal E_{\mathrm{breath}}
\mapsto
\mathfrak E
\quad
\text{when used ontologically},
$$

$$
\mathcal L_{\mathrm{breath}}
\mapsto
\mathfrak L,
$$

$$
\mathcal C_{\mathrm{breath}}
\mapsto
\mathfrak C,
$$

但：

$$
\mathcal H_{\mathrm{breath}}
\mapsto
\operatorname{Rest}.
$$

$\mathcal H$ 不加入三元 primitive。

狀態：

`REFINE + SPECIALIZE`

Theory Breathing 是三元方向族在 version dynamics 上的 realization。

---

# 6. 第三組：$Co$ 的正式退休與 SSDC 遷移

歷史 GCPR-RWL / FELRA 定義：

$$
\mathrm{Co}
(
h_t,\Gamma_t,R_t,E_t
)
\rightarrow
\mathrm{Snapshot}_t.
$$

其任務是避免：

- 意圖版本不同；
- 規約版本不同；
- Runtime 不同；
- 資料／環境不同；
- 驗證結果跨 snapshot 混用。

這是一個合法且重要的同步機制，但它只處理 SSDC 母概念的一個 subtype。

因此：

$$
\boxed{
Co_{\mathrm{legacy}}
\mapsto
\mathrm{SSDC}^{\mathrm{sync}}.
}
$$

並且：

$$
\boxed{
\mathrm{SSDC}
=
\text{Shared-State Domain Coupling}.
}
$$

Canonical decomposition：

$$
\mathrm{SSDC}_{AB}^{q}
=
(
Share,
Transport,
Couple,
Measure
)_{AB}^{q}.
$$

狀態：

`SPECIALIZE`

規則：

$$
\boxed{
\text{禁止新文件以裸 }Co\text{ 表示 SSDC 母概念。}
}
$$

---

# 7. 第四組：$C_0$ 不是一個概念

$C_0$ 是目前最危險的 collision 之一。

## 7.1 GCPR 創造／Artifact 初始態

歷史：

$$
C_{k+1}
=
\mathcal A(C_k,u_k;\Theta),
\qquad
C_0=\mathrm{blank}.
$$

其語義是：

> 產物生成過程的初始狀態。

Canonical migration：

$$
\boxed{
C_0^{\mathrm{artifact}}
\mapsto
X_0^{\mathrm{artifact}}.
}
$$

狀態：

`CANONICALIZE`

原因：避免與 Phase $C_0$、closure baseline、局部數學 cell 等大量 $C_0$ 相撞。

---

## 7.2 《C₀-相位統一論》

Phase lineage 中的 $C_0$ 曾被賦予離散源動／基本節拍語義。

經 Phase Canon audit 後，現行可保留核心為：

$$
C_0^{(\epsilon)}
\longrightarrow
\Phi_{\mathrm{phase}}
$$

的 discrete-to-continuum research program。

不得再預設：

$$
C_0
=
\text{verified Planck clock of the universe}.
$$

Canonical migration：

$$
\boxed{
C_0^{(\epsilon)}
\mapsto
C_{0,\mathrm{phase}}^{(\epsilon)}
}
$$

或在跨系列文件中使用：

$$
\boxed{
D_{\mathrm{event}}^{(\epsilon)}
}
$$

作為清晰別名。

狀態：

`KEEP-NAMESPACED`

---

## 7.3 其他局部 $C_0$

例如：

- baseline universe；
- rational cell；
- control coalition；
- optimization initial state。

全部：

`LOCAL-ONLY`

不得被 Ontology Canon 自動吸收。

結論：

$$
\boxed{
C_0
\text{ 不具有全域 canonical ontology meaning。}
}
$$

---

# 8. 第五組：$Cl$ 與 $\mathfrak{Cl}$

DCO 3.x 起，$Cl$ 被建立為 Closure 基本單元。

DCO 5.0 將：

$$
Cl
$$

由靜態對象進一步改成：

$$
\boxed{
\text{Closure-as-Process}.
}
$$

並擴展為 Cl-0 至 Cl-9。

《閉合性先於圓》進一步把：

$$
\bigcirc
$$

從唯一 primitive 降為 $Cl$ 的幾何投影／realization。

Canonical migration：

$$
\boxed{
Cl_{\mathrm{historical}}
\mapsto
\mathfrak{Cl}
=
\{Cl^\xi\}_{\xi\in\Xi}.
}
$$

其中允許：

$$
Cl^{\mathrm{alg}},
Cl^{\mathrm{top}},
Cl^{\mathrm{causal}},
Cl^{\mathrm{semantic}},
Cl^{\mathrm{observer}},
Cl^{\mathrm{ont}},
\ldots
$$

狀態：

`REFINE`

裸 $Cl$ 可在歷史 DCO 文件保留；新跨域論文優先標明 closure type。

---

# 9. 第六組：Circle / $\bigcirc$

歷史 DCO 曾以 Circle 作 unique ontological unit。

後續修正：

$$
\boxed{
\bigcirc
=
\pi_2(Cl)
=
S^1
}
$$

作為一種幾何投影。

Canonical status：

`HISTORICAL-PRIMITIVE -> PROJECTED-REALIZATION`

因此：

$$
\boxed{
\text{Circle}
\not\equiv
\text{Closure}.
}
$$

更安全地：

$$
\boxed{
\text{Circle}
\in
\operatorname{Realizations}(Cl^{\mathrm{geom}})
}
$$

或在指定模型下：

$$
\bigcirc=\pi_2(Cl).
$$

---

# 10. 第七組：$\Delta/\mathcal U/\nabla$

差合化支線使用：

$$
\langle
\Delta,
\mathcal U,
\nabla
\rangle.
$$

其歷史語義大致為：

$$
\Delta
=
\text{Difference / separation / differentiation},
$$

$$
\mathcal U
=
\text{Unification / coupling / overlap / linking},
$$

$$
\nabla
=
\text{Transformation / change / flow}.
$$

過去部分文件曾將它直接寫成：

$$
\{\text{Expansion},\text{Connection},\text{Convergence}\}
\equiv
\langle\Delta,\mathcal U,\nabla\rangle.
$$

本 Canon 撤掉這個未分型的嚴格等號。

原因：

1. $\Delta$ 可以產生 expansion，但 Difference 不等於所有 Expansion；
2. $\mathcal U$ 同時可能含 overlap、coupling、binding、synchronization、integration；
3. $\nabla$ 主要表示 transformation / change-rate，並不等於所有 Convergence；
4. 在標準數學語境中 $\nabla$ 還有 gradient / covariant derivative 等既有含義。

Canonical migration：

$$
\Delta
\mapsto
\operatorname{Diff}_{\tau},
$$

$$
\mathcal U
\mapsto
\operatorname{Couple}_{\tau}
\quad\text{or}\quad
\operatorname{Unify}_{\tau},
$$

$$
\nabla
\mapsto
\operatorname{Transform}_{\tau}.
$$

其中 $\tau$ 表示 typed domain。

狀態：

`ALTERNATIVE-BASIS / KEEP-TYPED`

差合化仍是重要 realization language，但不再作三元正典的無條件同義替換。

---

# 11. 第八組：$\Pi/\pi$ 投影符號

Projection 是 EveMissLab 多系列中的核心結構，因此不應退役。

但它具有多種 subtype：

$$
\Pi_{\mathrm{observer}},
$$

$$
\Pi_{\mathrm{formal}},
$$

$$
\Pi_{\mathrm{execute}},
$$

$$
\pi_{\mathrm{dim}},
$$

$$
\pi_{\mathrm{coarse}},
$$

$$
\Pi_{\mathrm{representation}}.
$$

Canonical rule：

$$
\boxed{
\Pi
\text{ 可保留，但跨理論文件不得使用無下標／無型別投影而不說明 domain/codomain。}
}
$$

尤其：

$$
\Pi(X)
\neq X
$$

一般情況下。

Projection 也不得被默認為 injective、surjective 或 information-preserving。

狀態：

`KEEP-NAMESPACED`

---

# 12. 第九組：$\mathcal R$ 的多重碰撞

$\mathcal R$ 至少出現過以下不同語義：

1. FELRA Rule Operator；
2. T Query / CRL 早期的 Convergent Re-linking notation；
3. Restoration / reconstruction；
4. 局部數學中的 retraction / push-forward；
5. relation / rule-space / regularization 等其他局部用途。

因此：

$$
\boxed{
\mathcal R
\text{ 不再具有全域唯一意義。}
}
$$

## 12.1 FELRA Rule Operator

歷史：

$$
\mathcal R_{\mathrm{FELRA}}
:
(\Theta_E,\Theta_C,\Theta_V,\Theta_\Pi,\Delta)
\rightarrow
(\Theta'_E,\Theta'_C,\Theta'_V,\Theta'_\Pi).
$$

Canonical：

$$
\boxed{
\mathcal R_{\mathrm{FELRA}}
\mapsto
\operatorname{RuleUpdate}.
}
$$

## 12.2 收連

早期工作可用 $\mathcal R$ 表示 Convergent Re-linking。

Canonical：

$$
\boxed{
\mathcal R_{\mathrm{relink}}
\mapsto
CRL.
}
$$

從本 Canon 起，**CRL 優先寫全名縮寫，不再使用裸 $\mathcal R$**。

狀態：

`DEPRECATE-BARE`

---

# 13. 第十組：$\mathcal K$ 的碰撞

FELRA 中：

$$
\mathcal K
=
\text{comparison / quality evaluation}.
$$

T Query Runtime / Ontology integration 中又曾以 $K$ 或 $\mathcal K$ 表示：

$$
\text{Commit}.
$$

這兩者必須分離。

Canonical migration：

$$
\mathcal K_{\mathrm{FELRA}}
\mapsto
\operatorname{Compare},
$$

$$
\mathcal K_{\mathrm{runtime}}
\mapsto
\operatorname{Commit}.
$$

狀態：

`DEPRECATE-BARE`

---

# 14. 第十一組：$\Phi$ 的重大碰撞

這是一個本輪新增的重要發現。

$\Phi$ 至少代表：

1. Surging Unary / 湧動一元；
2. phase field / 相位場；
3. 某些局部映射、通道或狀態變數。

因此 Ontology Canon v0.1 使用裸 $\Phi$ 雖在該文件內合法，但跨 corpus 不夠安全。

本 Migration Map 發布 **Amendment G-01**：

$$
\boxed{
\Phi_{\mathrm{pre}}
=
\text{Surging Unary / pre-formal unary},
}
$$

$$
\boxed{
\Phi_{\mathrm{phase}}
=
\text{phase field / typed phase object}.
}
$$

所以：

$$
\boxed{
\Phi_{\mathrm{pre}}
\neq
\Phi_{\mathrm{phase}}
}
$$

除非未來另有 theorem 建立指定 mapping。

狀態：

`CANONICALIZE`

後續 Ontology Canon v0.2 應把跨文件使用的裸 $\Phi$ 更新為 $\Phi_{\mathrm{pre}}$。

---

# 15. 第十二組：$\Omega$ 的重大碰撞

$\Omega$ 在歷史文件中可表示：

- universe / carrier state space；
- constraint set；
- survivor / search domain；
- ideal limit；
- sample space；
- local mathematical domain。

因此本 Migration Map 發布 **Amendment G-02**。

Ontology carrier：

$$
\boxed{
\Omega_{\mathrm{car}}
}
$$

Constraint domain：

$$
\boxed{
\Omega_{\mathrm{constraint}}
}
$$

Search / survivor domain：

$$
\boxed{
\Omega_{\mathrm{search}}
}
$$

Local mathematical $\Omega$ 可保留，但必須 local scope。

狀態：

`KEEP-NAMESPACED`

---

# 16. 第十三組：$M$、$I$、$R$ 的普通字母污染

這三個符號太常見，不應企圖全域壟斷。

## $M$

可能表示：

- Manifest；
- Method；
- Model；
- Measure；
- Matrix。

Ontology Canon 中的 Manifest 建議寫：

$$
\boxed{
M_{\mathrm{man}}
}
$$

或正文直接使用 `Manifest`.

## $I$

可能表示：

- Information；
- Intent；
- Identity；
- invariant。

Ontology information vector 保持：

$$
\boxed{
\mathbf I
}
$$

Intent 則：

$$
\boxed{
\mathcal I_{\mathrm{intent}}.
}
$$

## $R$

可能表示：

- relation；
- rule；
- regularizer；
- restoration；
- risk；
- resource。

因此新跨域稿不使用裸 $R$ 作核心 primitive，除非 local definition 非常明確。

狀態：

`LOCAL-ONLY / NAMESPACE REQUIRED`

---

# 17. Canonical Symbol Table v0.1

| Concept | Canonical symbol/name | Historical symbols | Migration status |
|---|---|---|---|
| Pre-formal unary | $\Phi_{\mathrm{pre}}$ | $\Phi$ | CANONICALIZE |
| Carrier domain | $\Omega_{\mathrm{car}}$ | $\Omega$ | CANONICALIZE |
| Latent structure | $\Lambda$ | various | KEEP |
| Manifest structure | $M_{\mathrm{man}}$ | $M$ | CANONICALIZE |
| Observer projection | $\Pi_{o,s,r,d}$ | $\Pi,\pi$ | KEEP-NAMESPACED |
| Expansion family | $\mathfrak E$ | $E_\theta,E,\mathcal E,E\text{-ing}$ | REFINE |
| Connection family | $\mathfrak L$ | $C_t,C,\mathcal L,C\text{-ing}$ | REFINE |
| Convergence family | $\mathfrak C$ | $V_\phi,V,\mathcal C,V\text{-ing}$ | REFINE |
| Shared-State Domain Coupling | $\mathrm{SSDC}$ | $Co$ | SPECIALIZE / RENAME |
| Sync subtype | $\mathrm{SSDC}^{\mathrm{sync}}$ | $Co_{\mathrm{legacy}}$ | SPECIALIZE |
| Closure family | $\mathfrak{Cl}$ | $Cl$ | REFINE |
| Circle realization | $\bigcirc$ / $\pi_2(Cl)$ | Circle as primitive | HISTORICAL -> PROJECTED |
| Difference operator | $\operatorname{Diff}_\tau$ | $\Delta$ | KEEP-TYPED |
| Coupling/unification operator | $\operatorname{Couple}_\tau$ / $\operatorname{Unify}_\tau$ | $\mathcal U$ | KEEP-TYPED |
| Transformation operator | $\operatorname{Transform}_\tau$ | $\nabla$ | KEEP-TYPED |
| Convergent Re-linking | $CRL$ | $\mathcal R$ | CANONICALIZE |
| Rule update | $\operatorname{RuleUpdate}$ | $\mathcal R$ | CANONICALIZE |
| Compare | $\operatorname{Compare}$ | $\mathcal K$ | CANONICALIZE |
| Commit | $\operatorname{Commit}$ | $K,\mathcal K$ | CANONICALIZE |
| Rest / stabilization | $\operatorname{Rest}$ | $\mathcal H$ | CANONICALIZE |
| Information vector | $\mathbf I$ | $I$ | KEEP-TYPED |
| Distortion spectrum | $\Delta_{\mathbf I}$ | various loss symbols | CANONICALIZE |
| Typed identity | $\equiv_{o,s,\mathcal J,\epsilon}$ | $=,\sim,\equiv$ | REFINE |
| Artifact initial state | $X_0^{\mathrm{artifact}}$ | $C_0=\mathrm{blank}$ | CANONICALIZE |
| Phase discrete event model | $C_{0,\mathrm{phase}}^{(\epsilon)}$ | $C_0^{(\epsilon)}$ | KEEP-NAMESPACED |

---

# 18. Forbidden Automatic Rewrites

以下 rewrite 從本版本起禁止自動執行。

## F-01

禁止：

$$
C
\Rightarrow
\text{Connection}.
$$

因為 $C$ 也可能是 Check、state、closure、configuration。

## F-02

禁止：

$$
V
\Rightarrow
\text{Convergence}.
$$

因為 FELRA $V$ 是 Select。

## F-03

禁止：

$$
Co
\Rightarrow
SSDC.
$$

正確為：

$$
Co_{\mathrm{legacy}}
\Rightarrow
SSDC^{\mathrm{sync}}.
$$

## F-04

禁止：

$$
\Delta
\equiv
\mathfrak E.
$$

Difference 可實現 Expansion，但不等於 Expansion family。

## F-05

禁止：

$$
\nabla
\equiv
\mathfrak C.
$$

Transformation / gradient / change 不等於 Convergence family。

## F-06

禁止：

$$
\mathcal U
\equiv
\mathfrak L.
$$

$\mathcal U$ 可能是 coupling、binding、integration、overlap 等特化。

## F-07

禁止：

$$
\Phi_{\mathrm{pre}}
=
\Phi_{\mathrm{phase}}.
$$

## F-08

禁止：

$$
Cl
=
\bigcirc.
$$

## F-09

禁止：

$$
CRL
=
\mathfrak C
$$

或：

$$
CRL
=
\mathfrak L\circ\mathfrak C
$$

除非另有 theorem。

## F-10

禁止：

$$
\Pi
=
\text{lossless isomorphism}.
$$

Projection 必須另證 injectivity / surjectivity / reconstruction fidelity。

---

# 19. Recommended Cross-Corpus Notation

當文件同時引用三個以上理論系列時，建議不用短字母，而採：

$$
\operatorname{Expand},
\operatorname{Link},
\operatorname{Converge},
\operatorname{Share},
\operatorname{Transport},
\operatorname{Couple},
\operatorname{Measure},
CRL,
\operatorname{Commit},
\operatorname{Rest}.
$$

理由：

$$
\boxed{
\text{Cross-corpus readability}
>
\text{single-letter elegance}.
}
$$

短符號可在單篇文件內重新 alias，但必須在 Symbol Table 明示。

---

# 20. Ontology Canon v0.1 的兩項立即修正

本 Migration Map 不重寫已發布的 v0.1 ZIP，但正式記錄兩項 amendment。

## Amendment G-01 — $\Phi$

跨文件 canonical：

$$
\Phi
\rightarrow
\Phi_{\mathrm{pre}}
$$

表示 Surging Unary。

Phase 系統使用：

$$
\Phi_{\mathrm{phase}}.
$$

## Amendment G-02 — $\Omega$

Carrier domain：

$$
\Omega
\rightarrow
\Omega_{\mathrm{car}}.
$$

Constraint / search / local mathematical domains 必須另加 namespace。

這兩項應在 Ontology Canon v0.2 合併。

---

# 21. Theory-Level Genealogy Table

| Node | Approx. date | Parent / upstream | Relation | Current status |
|---|---|---|---|---|
| TUO | 2026-01-11 | proto relational/state-space work | formalizes triadic cycle | HISTORICAL CORE |
| GCPR-RWL/Axiom branch | 2026-01 | TUO + formalization runtime | operationalizes E/C/V; adds Co/Pi | HISTORICAL ENGINEERING |
| Triadic Flux | 2026-04-06 | TUO | processualizes triad | KEEP |
| DCO 3.x | pre-5.0 | DCO lineage | establishes Cl basic unit | HISTORICALLY ATTESTED |
| DCO 4.x | pre-5.0 | DCO 3.x | Cl-1 ... Cl-4 | HISTORICALLY ATTESTED |
| DCO 5.0 | 2026-04 | DCO 4.x | Closure-as-Process, Cl-0 ... Cl-9 | CORE LINEAGE |
| Closure precedes Circle | 2026 | DCO / Closure | supersedes circle-as-primitive | KEEP |
| Triadic Universal Ontology | 2026-04-17 | TUO + DCO/Cl dialogue | nominal unary / operational ternary | KEEP |
| Surging Unary | 2026-05-27 | triadic + closure + 0+ work | introduces pre-formal unary | OPEN CORE |
| Closure moratorium | 2026-06-01 | Closure | identifies branch explosion / missing ranking | CORE DIAGNOSTIC |
| Differential-Unitive branch | 2026 | TUO + Closure | alternate operator basis | KEEP-TYPED |
| Theory Breathing | 2026-07-26 | TUO | version-dynamics realization | KEEP |
| T Query / CRL | 2026-08-13 | branching/runtime work | introduces Convergent Re-linking | CORE RUNTIME |
| Ontology Canon v0.1 | 2026-08-15 | all above | typed reorganization | CURRENT CANON |
| SSDC | 2026-08-15 | Connection + legacy Co + overlap/coupling work | generalizes shared-state coupling | CURRENT CANON |

---

# 22. Open Relations Registry

以下關係目前全部保持 OPEN：

## O-01

$$
Cl
\stackrel{?}{=}
\Phi_{\mathrm{pre}}.
$$

## O-02

$$
Cl
\stackrel{?}{=}
\Pi_{\mathrm{formal}}(\Phi_{\mathrm{pre}}).
$$

## O-03

$$
CRL
\stackrel{?}{\in}
\operatorname{ClosureExtension}(\mathfrak{Cl}).
$$

## O-04

$$
\langle\Delta,\mathcal U,\nabla\rangle
\stackrel{?}{\simeq}
\langle\mathfrak E,\mathfrak L,\mathfrak C\rangle
$$

在什麼 category / typing 下可成立？

## O-05

$$
SSDC
$$

是否能成為所有 nontrivial Connection 的必要中間層？

目前不能假定。

## O-06

「共享域」是否必須有共同中介空間 $\mathcal Z_{AB}$，或應以更一般的 span / profunctor / correspondence 定義？

待 Paper 03 處理。

---

# 23. Machine-Readable Migration Policy

任何自動整理器遇到符號時應採：

```text
1. identify source document / theory namespace
2. identify local definition
3. identify date/version
4. resolve semantic type
5. map to canonical concept
6. preserve original symbol in provenance
7. never rewrite historical source in place
8. emit ambiguity if more than one mapping remains
```

不得：

```text
lookup("C") -> Connection
```

而應：

```text
resolve(
    symbol="C",
    source="TUO"
) -> Connection

resolve(
    symbol="C",
    source="FELRA"
) -> Check

resolve(
    symbol="C_0",
    source="GCPR-Creative"
) -> ArtifactInitialState

resolve(
    symbol="C_0",
    source="Phase"
) -> DiscreteEventPhaseModel
```

---

# 24. Canonical Migration Invariant

所有遷移必須滿足：

$$
\boxed{
\operatorname{Meaning}_{\mathrm{source}}
\subseteq
\operatorname{Meaning}_{\mathrm{migration}}
+
\operatorname{Provenance}.
}
$$

也就是：

> 可以改名，可以升級型別，可以拆成多個新概念，但不能因正典化而把舊理論真正說過的內容偷偷刪掉。

如果無法無損遷移：

$$
\boxed{
\text{Preserve historical branch}.
}
$$

而不是強制 merge。

這與 CRL 的核心精神一致：

$$
\boxed{
\text{Convergence}
\neq
\text{Forced Consensus}.
}
$$

---

# 25. v0.1 Closure Statement

本輪完成後，Ontology 系列的符號治理原則正式從：

$$
\boxed{
\text{one symbol}
\leftrightarrow
\text{one universal meaning}
}
$$

改為：

$$
\boxed{
\text{symbol}
+
\text{namespace}
+
\text{type}
+
\text{version}
+
\text{provenance}
\rightarrow
\text{canonical meaning}.
}
$$

因此真正的理論單位不再只是：

$$
C,\quad V,\quad Co,\quad Cl,\quad \Phi
$$

這些字形。

而是：

$$
\boxed{
(\text{symbol},\text{theory},\text{version},\text{type},\text{domain},\text{provenance}).
}
$$

這是後續七篇核心系列的符號入口規格。

---

# 26. 下一階段

完成本 Migration Map 後，正式進入核心系列：

1. 潛能、載域與顯現；
2. 三元算子族；
3. SSDC；
4. 信息完整、失真與還原；
5. 同一、非同一、邊界與主客邊；
6. Closure、CRL 與分支閉合；
7. 一元—三元統一與母框架。

每篇開始前，重新檢查：

- Canon；
- Migration Map；
- Source Ledger；
- Open Relations Registry；
- 當篇 symbol table。

不得跳過。
