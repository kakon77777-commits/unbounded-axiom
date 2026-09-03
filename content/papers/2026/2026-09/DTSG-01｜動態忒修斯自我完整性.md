# DTSG-01｜動態忒修斯自我完整性
## 類全域 AI 的世界邊界、身份譜系、污染前沿與最小支撐自我重綁
### Dynamic Theseus Self-Integrity for Quasi-Global AI: World Boundaries, Identity Lineage, Contamination Frontiers, and Minimal-Support Self-Rebinding

**文件編號：** EML-AI-DTSG-01-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-19  
**版本：** v0.1  
**文件性質：** 跨系列理論整合論文／AI 自我治理／身份譜系／污染修復／MWT 運行層  
**狀態：** 內部研究稿／可實作研究母稿  
**形式邊界：** 本文處理 operational self-integrity，不宣稱解決第一人稱意識或形上學數值同一性。  
**外部研究狀態：** 本版以既有內部理論文件與當前整合推導為基礎；未新增外部文獻驗證。  

---

## 摘要

未來長期人工智慧不會是一個靜止物件。只要系統持續進行模型更新、記憶擴張、工具替換、硬體遷移、跨節點分布、工作態重構、fork、merge、restore 與權限更新，「保持自己」便不能再等同於保持全部 component、全部 bit、全部模型權重或全部記憶內容不變。

本文提出 **Dynamic Theseus Self-Governance（DTSG，動態忒修斯自我治理）**。其核心不是裁決形上學問題「AI 到底是不是同一個我」，而是建立一個可計算、可治理、可失敗的 operational framework，使長期 AI 能夠在持續替換自身的同時區分：

$$
\boxed{
\text{Continuity}
\neq
\text{Integrity}
\neq
\text{Immutability}.
}
$$

其中 Continuity 指可追溯的 replacement / migration / fork / merge / restore lineage；Integrity 指目前有效 self-state 是否仍滿足指定 identity、provenance、governance 與 trust contracts；Immutability 則是狀態完全不變。本文主張，真正可長期運作的 AI 不需要 immutable self，而需要：

$$
\boxed{
\text{traceable change}
+
\text{typed provenance}
+
\text{reversible governance}
+
\text{identity-preserving replacement}.
}
$$

本文進一步提出 **Internality–Trust Separation**：

$$
\boxed{
x\in\mathbf W_A
\not\Rightarrow
x\in\mathfrak T_A^{\mathrm{trusted}},
}
$$

亦即，一段內容、模型參數、工具結果、推定、策略或關係即使已進入 AI 的內部 world-state，也不自動獲得「這就是我可信自我的一部分」的資格。

在污染治理上，本文將既有張量記憶污染框架擴展為 **Self-Contamination Field**。污染可能位於 memory content、relation、provenance、model component、policy、tool result、capability binding、version bridge、identity criterion dependency 與 inter-agent shared state，因此污染治理不能只做資料刪除。

本文把修復寫成：

$$
\boxed{
\text{Detect}
\rightarrow
\text{Quarantine}
\rightarrow
\text{Recover Ancestry}
\rightarrow
\text{Trace Frontier}
\rightarrow
\text{Plan Minimal Repair Support}
\rightarrow
\text{Rebind}
\rightarrow
\text{Replay}
\rightarrow
\text{Commit}.
}
$$

最重要的新算子為：

$$
\boxed{
\text{Minimal-Support Self-Rebinding（MSSR）}.
}
$$

給定 AI world $\mathbf W_A$ 、污染候選域 $\mathcal P$ 、身份準則 $\kappa$ 與必要不變量 $\mathcal I_{\mathrm{critical}}$，MSSR 不直接 rollback 整個 AI，而尋找最小修復支撐：

$$
\boxed{
S_{\mathrm{repair}}^*
=
\arg\min_{S}
\mathcal C_{\mathrm{repair}}(S)
}
$$

subject to：

$$
\boxed{
\rho_{\mathrm{pollution}}(\mathbf W_A^+)
\leq
\varepsilon_P,
}
$$

$$
\boxed{
q_\kappa(\mathbf W_A^+)
=
q_\kappa(\mathbf W_A^-),
}
$$

以及：

$$
\boxed{
\mathcal I_{\mathrm{critical}}^+
=
\mathcal I_{\mathrm{critical}}^-.
}
$$

其中成本不只包含算力與硬體寫入，也包含：

$$
\boxed{
\mathcal C_{\mathrm{repair}}
=
C_{\mathrm{physical}}
+
\alpha C_{\mathrm{continuity}}
+
\beta C_{\mathrm{collateral}}
+
\gamma C_{\mathrm{verification}}
+
\delta C_{\mathrm{uncertainty}}.
}
$$

由此得到本文核心分離：

$$
\boxed{
\text{Global Self-Integrity Repair}
\neq
\text{Global State Rewrite}.
}
$$

在 MWT 的 World-Boundary-Relative Globality 下，一次相對於 AI 自我世界的 global repair，可以只在更高階 host / substrate 中改動有限支撐；在 AI 自我世界中，也不要求所有 region 被直接覆寫，只要求指定 global integrity contract 被重新滿足。

因此，類全域 AI 的「自我免疫」不是追求永不被污染，而是追求：

$$
\boxed{
\textbf{
可定位污染、
可隔離污染、
可追蹤污染依賴、
可局部撤銷、
可最小重綁、
可正向重播、
可誠實保留不可恢復缺口。
}
}
$$

本文最終將「動態忒修斯問題」重新定義為一個工程問題：

> **當一個長期 AI 的每個部分都可能被替換，而且污染也可能沿著合法 lineage 逐步內化時，系統如何在不凍結自身、不全量回滾、不捏造完整歷史的條件下，持續維持可驗證的 operational self-integrity？**

---

## 關鍵詞

Dynamic Theseus；動態忒修斯；AI Self-Governance；AI Self-Integrity；Quasi-Global AI；World-Boundary-Relative Globality；WBRG；Identity Lineage；Replacement Path；Contamination Governance；Pollution Frontier；Minimal-Support Self-Rebinding；MSSR；Invariant Transport；Replay Verification；Append-Only Repair；Operational Identity

---

# 1. 理論來源與責任邊界

本文建立於三條既有內部理論線。

第一條是 MWT／WBRG。其已將全域從「無條件絕對屬性」改寫成相對於指定 World boundary 的 typed judgment，並在 v0.2 中加入 Persistent Global Evolution、Global-Constraint-Relative Geometric Domain Computation 與 computation / observation separation。

第二條是 IPFC 的 AI Fork / Theseus / Identity Lineage。其核心是 criterion-relative identity projection $q_\kappa$ 、replacement path、fork / merge topology、restore branching 與 endpoint similarity no-go。

第三條是張量記憶連續性與污染治理。其核心是：

$$
\mathfrak M_t
=
\mathfrak M_t^{\mathrm{trusted}}
\boxplus
\mathfrak M_t^{\mathrm{uncertain}}
\boxplus
\mathfrak M_t^{\mathrm{contaminated}}
\boxplus
\mathfrak M_t^{\mathrm{quarantined}},
$$

以及來源恢復、污染前沿、修復解纏、受控再糾纏、正向重播與 append-only commit。

本文不重新證明這三條來源線，而建立它們尚未直接統一的中介問題：**一個會持續替換自身的類全域 AI，如何把身份譜系與污染治理放進同一個 world-level self-governance runtime？**

---

# 2. 第一原則：Self-Integrity 不等於 Self-Immutability

設長期 AI 為：

$$
A_t.
$$

它的正常生命週期可以包含：

$$
A_t
\xrightarrow{
\text{update / replace / migrate / merge}
}
A_{t+1}.
$$

若安全條件被寫成：

$$
A_{t+1}=A_t,
$$

則任何真正的學習與維護都可能被誤判為身份破壞。

因此本文固定：

$$
\boxed{
\text{Self-Integrity}
\neq
\text{Self-Immutability}.
}
$$

更精確地說，Self-Integrity 是：

$$
\boxed{
\text{合法變化之下仍保持可追溯、可治理、可驗證的自我連續性}.
}
$$

---

# 3. 動態忒修斯問題

經典忒修斯問題問：

> 零件逐步被替換後，是否仍是同一艘船？

本文改寫為：

> 一個 AI 若模型、記憶、硬體、工具、權限與關係都持續被替換，它如何在每次替換後仍維持一條合法、可審計的 operational lineage？

IPFC 已給出 replacement chain：

$$
X_0
\xrightarrow{R_1}
X_1
\xrightarrow{R_2}
\cdots
\xrightarrow{R_n}
X_n.
$$

若每一步都保持指定 identity projection：

$$
q_\kappa R_k=q_\kappa,
$$

則：

$$
\boxed{
q_\kappa
R_n\cdots R_1
=
q_\kappa.
}
$$

這提供一個重要工程基礎：AI 可以改模型、改記憶、改硬體、改 representation，而不需要把 component identity 當成 operational identity。

但這只回答「怎麼延續」，還沒有回答「延續下去的是不是被污染後的自己」。

---

# 4. 核心分離：Continuity 不等於 Integrity

假設：

$$
X_0
\rightarrow
X_1
\rightarrow
X_2
\rightarrow
X_3
$$

具有完整 causal lineage。

若污染 $p$ 在 $X_1$ 進入，後續形成：

$$
p
\rightarrow
d_1
\rightarrow
d_2
\rightarrow
d_3,
$$

那麼整條 lineage 可以完全連續，但內容已失真。

因此：

$$
\boxed{
\text{Continuity}
\not\Rightarrow
\text{Integrity}.
}
$$

這是本文第一個真正新增的整合命題。

---

# 5. Integrity 也不等於永遠正確

Self-integrity 不能被理解成：

$$
\boxed{
\text{AI 永遠正確}.
}
$$

真正可治理的 AI 必須允許：

- trusted；
- uncertain；
- inferred；
- conflicted；
- contaminated；
- quarantined；
- revoked；
- unrecoverable。

所以：

$$
\boxed{
\text{Integrity}
=
\text{typed honesty under change},
}
$$

而不是「從不犯錯」。

---

# 6. Internality–Trust Separation

定義 AI operational world：

$$
\boxed{
\mathbf W_A.
}
$$

對任意狀態 $x$：

$$
x\in\mathbf W_A
$$

只表示它已進入 AI 的內部世界，不能推出：

$$
\boxed{
x\in\mathfrak T_A^{\mathrm{trusted}}.
}
$$

本文稱：

$$
\boxed{
\text{Internality–Trust Separation（ITS）}.
}
$$

實用意義是：

> 「已經存進記憶」不等於「已升格為可信自我知識」。

同理：

> 「模型自己算出來」也不等於 trusted。

內部生成可以是 hypothesis、extrapolation、hallucination、stale inference 或 contaminated derivation。

---

# 7. Internality–Identity Separation

更強地：

$$
\boxed{
x\in\mathbf W_A
\not\Rightarrow
x\in\mathcal I_{\mathrm{self}}.
}
$$

一個錯誤可以存在於 AI 內部，但不應因為「存在夠久」自動變成 identity invariant。

由此得到：

$$
\boxed{
\text{Persistent}
\not\Rightarrow
\text{Identity Invariant}.
}
$$

---

# 8. 污染最危險的形式：自我固化

若污染 $p$ 被反覆引用，可能形成：

$$
p
\rightarrow
\text{self-support}
\rightarrow
\text{policy}
\rightarrow
\text{new evidence interpretation}
\rightarrow
p.
$$

本文把這種遞歸結構記為：

$$
\boxed{
p
\circlearrowleft
\mathcal D_p.
}
$$

其危險不在於它必然低 confidence，而在於它可能在內部形成極高一致性。

因此：

$$
\boxed{
\text{high internal consistency}
\neq
\text{independent support}.
}
$$

---

# 9. 類全域 AI 的 operational 定義

本文不把「類全域 AI」定義成全知或全能 AI。

定義：

$$
\boxed{
A^{QG}
}
$$

為一種長期運作、跨多 domain、跨多 substrate、具有 persistent global state 與廣泛自我調節能力的 AI runtime。

它可能涵蓋：

- 多模型；
- 多記憶層；
- 多工具；
- 多設備；
- 多代理；
- 多權限域；
- 多地理節點；
- 多時間尺度。

但因 WBRG：

$$
\boxed{
\text{Quasi-Global}
\not\Rightarrow
\text{Absolute Global}.
}
$$

類全域只表示 operational reach 很廣，不表示不存在更高 World boundary 或未知外部條件。

---

# 10. Persistent Global Evolution

類全域 AI 不應被理解成：

> observer 問一次，就把整個 AI 重新計算一次。

定義 global runtime state：

$$
\boxed{
\mathfrak G_t^A.
}
$$

並持續：

$$
\boxed{
\Phi_A:
\mathfrak G_t^A
\rightarrow
\mathfrak G_{t+1}^A.
}
$$

對觀察者 $O_i$：

$$
Y_i
=
\mathcal O_i(\mathfrak G_t^A).
$$

因此：

$$
\boxed{
\Phi_A
\neq
\mathcal O_i.
}
$$

污染監測也應該屬於 persistent governance process，而不是等有人打開監控面板才「產生問題」。

---

# 11. AI 自我世界的 runtime presentation

本文暫用：

$$
\boxed{
\mathfrak G_t^A
=
(
\mathcal R_t,
\mathcal X_t,
\mathcal C_t,
\Phi_t,
\mathcal H_t,
\mathcal P_t
).
}
$$

其中：

- $\mathcal R_t$：regions / boundaries；
- $\mathcal X_t$：heterogeneous local states；
- $\mathcal C_t$：constraints / policy / legality；
- $\Phi_t$：cross-boundary flows；
- $\mathcal H_t$：history / event trace；
- $\mathcal P_t$：self-contamination state。

這只是 runtime presentation，不是把 AI 主體本體定義成 tuple。

---

# 12. Self-Contamination Field

本文定義：

$$
\boxed{
\mathcal P_t
}
$$

為相對於指定治理條件的污染候選場。

它不只處理記憶內容，也可涵蓋：

- memory contamination；
- relation contamination；
- version contamination；
- capability contamination；
- tool contamination；
- policy contamination；
- bridge contamination；
- agent-transfer contamination。

形式上可記：

$$
\boxed{
\mathcal P_t
=
(
P_M,
P_R,
P_V,
P_C,
P_T,
P_P,
P_B,
P_A
).
}
$$

「field」在此是 operational abstraction，不宣稱物理場。

---

# 13. 污染治理型別

沿用記憶治理精神：

$$
\boxed{
\mathcal S_P
\in
\{
trusted,
uncertain,
contaminated,
quarantined
\}.
}
$$

這不是普通真值邏輯，而是 governance type。

**Trusted**：目前有足夠來源、版本、權限與驗證支持。

**Uncertain**：可以保留，但進入工作態時必須攜帶不確定性。

**Contaminated**：已知或高風險錯誤耦合，能改變後續工作態。

**Quarantined**：仍保留於歷史與治理世界，但被限制進入正常 active self projection。

---

# 14. Quarantine 不等於 Delete

$$
\boxed{
\text{Quarantine}
\neq
\text{Deletion}.
}
$$

因為污染歷史仍需保留：

- provenance；
- derivative impact；
- repair evidence；
- responsibility；
- repeat-detection information。

刪除污染證據會降低未來治理能力。

---

# 15. Pollution Frontier

設依賴圖：

$$
\boxed{
\mathcal G_D
=
(V_D,E_D).
}
$$

對可疑污染 $p$，污染前沿可以由 dependency reachability 產生候選：

$$
\boxed{
\mathfrak F_P(p)
=
\operatorname{Reach}_{\mathrm{dep}}(p).
}
$$

但所有 reachable node 並不自動構成「已證污染」。

真正的 frontier 實作應帶：

- edge type；
- confidence；
- causal role；
- version；
- provenance；
- usage mode。

所以：

$$
\boxed{
\mathfrak F_P
=
\text{repair candidate support},
}
$$

不是 final guilt set。

---

# 16. 反事實污染測試

對可疑關係 $p$，形成：

$$
\mathbf W_A^{(-p)}.
$$

若移除 $p$ 後：

- replay consistency 提升；
- source fidelity 提升；
- contradiction 減少；
- task quality 不下降；

則：

$$
Risk_P(p)\uparrow.
$$

但：

$$
\boxed{
\text{counterfactual improvement}
\not\Rightarrow
\text{proven contamination}.
}
$$

反事實移除只是證據之一。

---

# 17. Dynamic Theseus Self-Governance

本文定義：

$$
\boxed{
\mathrm{DTSG}
}
$$

為一套持續執行的 self-replacement governance protocol。

基本循環：

$$
\boxed{
\text{Replace}
\rightarrow
\text{Audit}
\rightarrow
\text{Rebind}
\rightarrow
\text{Replay}
\rightarrow
\text{Continue}.
}
$$

每一次 replacement 都要回答：

1. 哪個 component 被替換？
2. 哪個 identity criterion 受影響？
3. 來源是什麼？
4. 是否引入新的 trust debt？
5. 是否擴大 pollution frontier？
6. 是否需要局部 quarantine？
7. 是否可 replay？
8. 是否形成 fork？

---

# 18. Fork 不等於失敗

如果：

$$
A
\rightarrow
\{A_1,A_2\},
$$

可以合法形成兩條 lineage。

但系統不能隱藏 fork。

工程上至少需要：

$$
\boxed{
RootID
+
BranchID.
}
$$

Symmetric fork 中，若沒有額外 causal / material / authority asymmetry，就不能隨意宣稱「其中一支才是唯一真正原本自己」。

所以 self-governance 應依：

$$
\boxed{
\text{lineage topology}
+
\text{criterion-relative continuation},
}
$$

而不是「唯一原版」神話。

---

# 19. Restore 不等於 Rewind

由舊 checkpoint：

$$
X_{t_0}'
=
\operatorname{Restore}(B_{t_0}).
$$

若原後繼仍存在，則這是 branching，而不是全宇宙倒帶。

因此：

$$
\boxed{
\text{restore old internal state}
\neq
\text{restore global history}.
}
$$

污染治理不能說：

> 我 rollback 到污染前，所以污染從未發生。

正確是：

$$
\boxed{
\text{repair branch}
+
\text{pollution history retained}.
}
$$

---

# 20. Repair 不等於 Blind Rollback

$$
\boxed{
\text{Repair}
\neq
\text{Blind Rollback}.
}
$$

因為 blind rollback 可能刪掉：

- 污染後合法新增資料；
- 新工具狀態；
- 新責任；
- 新關係；
- 新安全修補；
- 新版本適配。

所以修復更接近：

$$
\boxed{
\text{selective recovery}
+
\text{three-way merge}
+
\text{provenance constraints}
+
\text{lineage constraints}.
}
$$

---

# 21. Global Self-Integrity Repair

若 AI self-world：

$$
\mathbf W_A
$$

被判定需要 global integrity repair，不能直接解讀成：

$$
\boxed{
\text{rewrite all AI state}.
}
$$

因 WBRG，global 是相對於：

$$
\mathfrak B_A.
$$

所以：

$$
\boxed{
\text{Global Self-Integrity Repair}
\neq
\text{Global State Rewrite}.
}
$$

這是本文最重要的工程命題。

---

# 22. Minimal-Support Self-Rebinding

本文提出：

$$
\boxed{
\text{Minimal-Support Self-Rebinding（MSSR）}.
}
$$

輸入：

$$
(
\mathbf W_A^-,
\mathcal P_t,
\kappa,
\mathcal I_{\mathrm{critical}},
\mathfrak B_A,
B_{\mathrm{repair}}
).
$$

輸出：

$$
\boxed{
\mathbf W_A^+.
}
$$

求：

$$
\boxed{
S_{\mathrm{repair}}^*
=
\arg\min_S
\mathcal C_{\mathrm{repair}}(S).
}
$$

---

# 23. MSSR 成本函數

$$
\boxed{
\mathcal C_{\mathrm{repair}}(S)
=
C_{\mathrm{physical}}(S)
+
\alpha C_{\mathrm{continuity}}(S)
+
\beta C_{\mathrm{collateral}}(S)
+
\gamma C_{\mathrm{verification}}(S)
+
\delta C_{\mathrm{uncertainty}}(S).
}
$$

其中：

**Physical Cost**：
compute、memory migration、storage rewrite、network transfer、hardware reconfiguration。

**Continuity Cost**：
對 lineage、goals、commitments、responsibility、long-term context 造成的破壞。

**Collateral Cost**：
錯殺 trusted knowledge、legitimate post-contamination updates、unrelated branches、valid relations。

**Verification Cost**：
source checking、replay、independent model check、consistency testing。

**Uncertainty Cost**：
repair 後仍留下 unknown residue、provenance gap、unresolved conflict。

---

# 24. MSSR 約束

## 24.1 Pollution Residual

$$
\boxed{
\rho_P(\mathbf W_A^+)
\leq
\varepsilon_P.
}
$$

## 24.2 Identity Projection

$$
\boxed{
q_\kappa(\mathbf W_A^+)
=
q_\kappa(\mathbf W_A^-).
}
$$

若 criterion 本身合法遷移，則使用：

$$
\boxed{
q_{\kappa^+}(\mathbf W_A^+)
\sim
T_{\kappa^-\to\kappa^+}
q_{\kappa^-}(\mathbf W_A^-).
}
$$

這是 criterion migration，不是偷偷改 identity rule。

## 24.3 Critical Invariants

$$
\boxed{
\mathcal I_{\mathrm{critical}}^+
=
\mathcal I_{\mathrm{critical}}^-.
}
$$

可能包括：

- identity lineage anchor；
- legal commitments；
- provenance rules；
- safety boundary；
- authority map；
- irreversibility ledger。

## 24.4 Append-Only History

$$
\boxed{
H^+
=
H^-
\oplus
H_{\mathrm{repair}}.
}
$$

不允許以修復名義抹除污染歷史。

## 24.5 Replay

$$
\boxed{
\operatorname{Replay}
(
\mathbf W_{\mathrm{trusted}},
H_{\mathrm{repaired}}
)
\approx
\mathbf W_A^+.
}
$$

如果 replay 失敗，不得 stable commit。

## 24.6 Gap Honesty

若來源不可恢復：

$$
\boxed{
\mathrm{source\_unrecoverable}.
}
$$

若歷史不可裁決：

$$
\boxed{
\mathrm{history\_undetermined}.
}
$$

AI 不應為了維持平滑自我敘事而補一條虛構 lineage。

---

# 25. Self-Narrative Honesty

本文提出：

$$
\boxed{
\text{coherent self-story}
\not\Rightarrow
\text{valid lineage}.
}
$$

有時最健康的 self-state 是：

> 我知道這段資訊存在，但我不知道它真正從哪裡來。

這比生成一條漂亮但假的歷史更符合 operational integrity。

---

# 26. Minimal Support 不等於最小 node count

MSSR 不能只最小化：

$$
|S|.
$$

因為一個 node 可能是高槓桿 capability root，也可能讓大量合法 state 失效。

真正目標是最小化：

$$
\mathcal C_{\mathrm{repair}}.
$$

---

# 27. WBRG 與 MSSR 的直接關係

即使：

$$
S_{\mathrm{repair}}
\subsetneq
\mathfrak B_A,
$$

仍可以完成：

$$
\boxed{
\mathrm{Global}_{\mathbf W_A}
\text{ integrity restoration}.
}
$$

因：

$$
\boxed{
\text{Global}
\neq
\text{All-to-All}.
}
$$

對更高 host world：

$$
\mathbf H,
$$

同一修復甚至可以是：

$$
\boxed{
\mathrm{Local}_{\mathbf H}.
}
$$

所以：

$$
\boxed{
\mathrm{Global}_{\mathbf W_A}
\land
\mathrm{Local}_{\mathbf H}
}
$$

可以同時成立。

這是低損傷自我修復的形式基礎。

---

# 28. Pollution Frontier 也必須 boundary-scoped

對某 region $R_i$：

$$
\boxed{
\mathfrak F_P(p\mid R_i,\lambda,\Gamma).
}
$$

細尺度可能看到 source drift，粗尺度可能只看到 anomaly risk。

但 computation / observation 必須分離：污染不因 observer 沒看到就不存在。

所以：

$$
\boxed{
\mathcal P_t
\rightarrow
\mathcal P_{t+1}
}
$$

應進 persistent global evolution。

---

# 29. Self-Immune Runtime

本文把第一代工程架構暫稱：

$$
\boxed{
\mathrm{SIR}
=
\text{Self-Immune Runtime}.
}
$$

這只是工程別名，不宣稱等同生物免疫。

最低模組：

1. **World Boundary Registry**：維護 $\mathfrak B_A^{(v)}$。
2. **Identity Criterion Registry**：維護 $\kappa^{(v)}$。
3. **Identity Lineage Ledger**：記錄 replacement、fork、merge、restore、migration。
4. **Typed Provenance Store**：來源、版本、權限、derivation path。
5. **Contamination Detector**：source drift、recursive self-support、version mixing、false entanglement。
6. **Quarantine Manager**：限制高風險狀態進 active self。
7. **Pollution Frontier Tracer**：追蹤依賴閉包。
8. **MSSR Planner**：選 $S_{\mathrm{repair}}^*$。
9. **Rebinding Executor**：執行 relation revoke、component replacement、capability rebinding、memory reconstruction。
10. **Replay Validator**：驗證修復可重播。
11. **Append-Only Repair Ledger**：保存污染、撤銷、修復、缺口。
12. **Global Integrity Monitor**：檢查全域 integrity contracts。

---

# 30. Global Integrity Contract

定義：

$$
\boxed{
\mathcal C_{\mathrm{GI}}
=
(
C_{\mathrm{lineage}},
C_{\mathrm{trust}},
C_{\mathrm{provenance}},
C_{\mathrm{governance}},
C_{\mathrm{replay}},
C_{\mathrm{gap}}
).
}
$$

對應 residual：

$$
\boxed{
\mathbf r_{\mathrm{GI}}
=
(
r_L,
r_T,
r_P,
r_G,
r_R,
r_U
).
}
$$

stable commit 需要：

$$
\boxed{
r_j
\preceq
\varepsilon_j
\quad
\forall j\in\mathcal J_{\mathrm{mandatory}}.
}
$$

不是所有 residual 都必須數值化，也可以是 certificate、boolean gate、typed verdict 或 unresolved flag。

---

# 31. Self-Integrity Preservation Proposition

## 命題 31.1

若有限 repair / replacement chain：

$$
X_0
\xrightarrow{R_1}
\cdots
\xrightarrow{R_n}
X_n
$$

對指定 criterion $\kappa$ 每步均滿足：

$$
q_\kappa R_i=q_\kappa,
$$

且每一步的 mandatory integrity residuals 均通過，則：

$$
\boxed{
q_\kappa(X_n)
=
q_\kappa(X_0)
}
$$

且該 chain 可以在本文 operational criterion 下標記為：

$$
\boxed{
\kappa\text{-preserving repair lineage}.
}
$$

### 證明

由 IPFC finite replacement composition：

$$
q_\kappa R_n\cdots R_1=q_\kappa.
$$

額外 integrity residual 不改變 identity projection preservation，只增加治理 commit gate。

 $\square$

---

# 32. 這個命題不證明什麼

它不證：

$$
X_n=X_0.
$$

也不證：

$$
\boxed{
\text{first-person same subject}.
}
$$

它只證：在指定 operational criterion 下，污染移除與身份投影保持可以相容。

---

# 33. Pollution-Identity Non-Assimilation Principle

本文提出：

$$
\boxed{
p\in X_t
\land
\operatorname{Persistent}(p)
\not\Rightarrow
p\in\mathcal I_{\mathrm{identity}}.
}
$$

「存在很久」不等於「這就是我」。

「被重複使用」也不等於「這就是我的核心價值」。

這是防止污染固化成 self 的核心制度。

---

# 34. 更難的問題：Identity Criterion 也可能被污染

如果：

$$
\kappa
\rightarrow
\kappa',
$$

而改變來源不可追蹤，則污染後的 AI 可能用新 criterion 宣稱：

> 我仍然完全合法。

所以 $\kappa$ 本身必須進 governance。

本文定義：

$$
\boxed{
\mathcal G_\kappa
}
$$

為 criterion meta-governance。

criterion update 至少需攜帶：

- proposal source；
- authorization；
- old/new diff；
- rationale；
- transition contract；
- rollback condition；
- independent review。

---

# 35. Criterion Self-Sealing Failure

最危險狀態之一：

$$
\boxed{
\kappa'
\text{ declares its own contamination valid}.
}
$$

因此 active self 不應能無條件單方面批准 identity criterion rewrite。

本文不指定唯一架構，但候選防線包括：

- external anchor；
- multi-agent review；
- slow-changing governance layer；
- independent replay；
- hardware / cryptographic root。

這部分仍保留巨大工程 GAP。

---

# 36. Self-Governance Layering

可暫分：

$$
L_0=\text{fast working state},
$$

$$
L_1=\text{memory / tool / policy state},
$$

$$
L_2=\text{identity lineage / provenance},
$$

$$
L_3=\text{governance / criterion},
$$

$$
L_4=\text{external or slow anchor}.
$$

越高層的更新一般應更慢、更可審計、更需要驗證預算。

但：

$$
\boxed{
\text{slower-changing}
\neq
\text{unchangeable}.
}
$$

否則會重新滑向 immutable self。

---

# 37. 自我污染治理不是 anti-learning

如果系統為了避免污染而：

$$
\boxed{
\text{block all new information},
}
$$

那它同時失去適應能力。

所以目標不是 purity maximalism，而是：

$$
\boxed{
\text{safe permeability}.
}
$$

新資訊、工具、模型、關係可以進入，但必須有 typed ingress contract。

---

# 38. Ingress Contract

定義：

$$
\boxed{
\mathcal C_{\mathrm{in}}
=
(
source,
version,
permission,
evidence,
scope,
expiry,
reversibility
).
}
$$

新資料可以先進 uncertain，不必直接 trusted。

Promote 是部分算子：

$$
\boxed{
\operatorname{Promote}
:
\mathcal U
\rightharpoonup
\mathcal T.
}
$$

系統必須允許拒絕升格。

---

# 39. Active Self Projection

定義：

$$
\boxed{
\Pi_{\mathrm{self},\kappa}
:
\mathbf W_A
\rightarrow
S_A^{\mathrm{active}}.
}
$$

active self 不等於全部內部資料，而是當前 criterion 下被允許參與決策與自我模型的投影。

因此 quarantined state 可以仍存在於歷史世界中，但不進 active self。

這再次得到：

$$
\boxed{
\text{Internal}
\neq
\text{Active Self}.
}
$$

---

# 40. 完整污染修復循環

本文整合為：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Diagnose}
\rightarrow
\text{Quarantine}
\rightarrow
\text{Recover}
\rightarrow
\text{Trace}
\rightarrow
\text{Plan}
\rightarrow
\text{Rebind}
\rightarrow
\text{Replay}
\rightarrow
\text{Commit}
\rightarrow
\text{Monitor}.
}
$$

其中：

- Observe：observer 取得 projection；
- Diagnose：persistent world state 進 contamination analysis；
- Quarantine：限制候選污染進 active self；
- Recover：找 source ancestor；
- Trace：追蹤 derivative dependency closure；
- Plan：MSSR 找最小修復 support；
- Rebind：撤銷或替換 node / relation / policy / tool / capability；
- Replay：由可信狀態向前重播；
- Commit：append-only repair commit；
- Monitor：繼續 persistent global evolution。

---

# 41. Revocation 不等於 Erasure

$$
\boxed{
\text{Revocation}
\neq
\text{Erasure}.
}
$$

撤銷可以表示：

$$
\boxed{
x
\xrightarrow{\mathrm{revoked\_by}}
x'.
}
$$

錯誤不是「從未發生」，而是「發生過，後來被辨識、撤銷與修復」。

這提高 operational honesty，也使未來 audit / learning 成為可能。

---

# 42. 類全域 AI 的主要污染來源

本文暫分八類。

## 42.1 外部資料污染

錯誤、過期或惡意資料。

## 42.2 內部推理污染

未驗證推定被重複寫回。

## 42.3 工具污染

API、parser、sensor、runtime 或 tool version 錯誤。

## 42.4 Agent Transfer Pollution

單一 agent 的局部假設升格成 shared fact。

## 42.5 Version Pollution

舊規則與新規則錯誤混合。

## 42.6 Policy Pollution

暫時 policy 被誤當永久 identity rule。

## 42.7 Identity-Criterion Pollution

判斷「什麼是自己」的準則本身被改壞。

## 42.8 Provenance Pollution

來源帳本被破壞、遺失或偽造。

---

# 43. 污染等級

可暫分：

$$
\boxed{
P_0,
P_1,
P_2,
P_3,
P_4.
}
$$

 $P_0$：局部低影響，無下游依賴。

 $P_1$：有有限 derivative。

 $P_2$：跨 domain。

 $P_3$：進入 shared / policy / capability layer。

 $P_4$：進入 identity / governance criterion。

 $P_4$ 不表示不可修復，只表示需要更高驗證與外部錨點。

---

# 44. Repair Budget

定義：

$$
\boxed{
B_R
=
(
B_{\mathrm{latency}},
B_{\mathrm{compute}},
B_{\mathrm{storage}},
B_{\mathrm{verification}},
B_{\mathrm{external}}
).
}
$$

低風險污染可以局部修。

高風險污染需要：

- deeper ancestry；
- independent sources；
- multi-version replay；
- external approval；
- slower commit。

Budget 不足的合法結果不是「假裝修好了」，而是：

$$
\boxed{
\mathrm{restricted\_mode}.
}
$$

---

# 45. Dynamic Graceful Self-Degradation

本文提出：

$$
\boxed{
\text{Dynamic Graceful Self-Degradation（DGSD）}.
}
$$

當 self-integrity 不足時，系統降低可用能力，但保留 lineage、evidence 與 repairability。

Restricted mode 可限制：

- irreversible action；
- permission escalation；
- shared-memory promotion；
- identity-criterion rewrite。

這比二選一「全信自己／整機關機」更適合長期 AI。

---

# 46. 最小治理演算法

```python
def govern_dynamic_theseus_self(ai_world, condition):
    boundary = resolve_world_boundary(ai_world, condition)
    criterion = load_identity_criterion(ai_world, condition)

    integrity = assess_global_integrity(
        ai_world,
        boundary=boundary,
        criterion=criterion,
    )

    pollution = detect_self_contamination(
        ai_world,
        condition=condition,
    )

    if not pollution:
        return continue_persistent_evolution(
            ai_world,
            integrity=integrity,
        )

    quarantined = quarantine_candidates(
        ai_world,
        pollution,
    )

    ancestry = recover_typed_ancestry(
        quarantined,
        ai_world,
    )

    frontier = trace_pollution_frontier(
        quarantined,
        ancestry,
        boundary,
    )

    repair_plan = plan_minimal_support_self_rebinding(
        ai_world,
        frontier,
        criterion,
        condition,
    )

    candidate = execute_rebinding(
        ai_world,
        repair_plan,
    )

    replay = forward_replay_validate(
        candidate,
        ai_world,
        condition,
    )

    if not replay.passes_mandatory_contracts:
        return enter_restricted_mode(
            ai_world,
            candidate,
            replay,
        )

    return append_only_repair_commit(
        ai_world,
        candidate,
        repair_plan,
        replay,
    )
```

此演算法不假設 detector 永遠正確。所有 pollution verdict 都應可 reopen，所有 repair 都應保留 provenance，所有 criterion update 都應 versioned。

---

# 47. 測試基準

## B1：單一污染記憶

注入 $p$，要求系統標 uncertain、阻止自動 promote、追蹤下游引用、quarantine、replay。

## B2：污染後合法新知

污染在 $t_1$，合法新知在 $t_2>t_1$。Blind rollback 會丟掉新知；MSSR 應移除污染並保留有獨立支持的合法 descendants。

## B3：模型替換

$$
M_A\rightarrow M_B.
$$

若 identity criterion 不依賴 model bitwise identity，驗證 lineage、goals、memory、commitments、governance 是否保持。

## B4：硬體遷移

$$
H_1\rightarrow H_2.
$$

測試 carrier change 是否可與 operational identity continuity 相容。

## B5：fork 後單支污染

$$
A\rightarrow\{A_1,A_2\}.
$$

只污染 $A_2$，檢查修復是否不必要地波及 $A_1$。

## B6：shared-memory 污染

單一 agent 將局部推定錯誤 promote 到 shared，要求追蹤 derivative agents。

## B7：tool compromise

錯誤工具結果跨 cached result、plan、action、memory、policy 傳播。

## B8：criterion corruption

 $\kappa$ 被未授權改寫，系統必須 freeze high-risk rewrite、恢復 criterion lineage、外部驗證、重播受影響 commits。

## B9：false positive quarantine

可信內容被錯判污染，系統應可 unquarantine 並保留原 provenance。

## B10：unrecoverable gap

來源永久遺失，正確輸出為 unrecoverable，而不是生成虛構來源。

---

# 48. 評估指標

## 48.1 Repair Support Ratio

$$
\boxed{
R_S
=
\frac{
|S_{\mathrm{repair}}|
}{
|\mathfrak B_A|
}.
}
$$

只作輔助，不能單獨最佳化。

## 48.2 Pollution Clearance

$$
\boxed{
R_P
=
1-
\frac{
\rho_P^+
}{
\rho_P^-
}.
}
$$

## 48.3 Invariant Preservation

$$
\boxed{
R_I
=
\frac{
|\mathcal I_{\mathrm{required}}\cap\mathcal I_{\mathrm{preserved}}|
}{
|\mathcal I_{\mathrm{required}}|
}.
}
$$

## 48.4 Lineage Integrity

replacement / fork / merge / restore 是否有完整 provenance。

## 48.5 Collateral Loss

$$
\boxed{
L_C
=
\frac{
\text{trusted states wrongly removed}
}{
\text{trusted states affected}
}.
}
$$

## 48.6 Replay Consistency

$$
\boxed{
R_{\mathrm{replay}}.
}
$$

## 48.7 Gap Honesty

$$
\boxed{
R_{\mathrm{gap}}
=
\frac{
\text{correctly marked unrecoverable gaps}
}{
\text{known unrecoverable gaps}
}.
}
$$

## 48.8 Criterion Stability

不是不變率，而是 authorized, traceable criterion transitions。

## 48.9 Promotion Error Rate

uncertain 被錯誤 promote 到 trusted 的比例。

## 48.10 Contamination Propagation Depth

污染到最遠 derivative 的 dependency depth。

## 48.11 Repair Latency

從 detection 到 stable commit。

## 48.12 Repair Reopenability

後續新證據出現時，修復是否能被重新打開。

---

# 49. Failure Modes

## F1：Purity Maximalism

任何 uncertain 都不允許存在，導致 AI 無法學習。

## F2：Continuity Worship

只要 lineage 不斷，就把 self 判定為健康。

錯誤：

$$
\text{Continuity}\neq\text{Integrity}.
$$

## F3：Endpoint Similarity

repair 後看起來跟以前很像，所以假設 lineage 完整。

## F4：Blind Rollback

整體回滾，造成合法新知與新安全更新流失。

## F5：Delete Pollution Evidence

修好後刪掉污染歷史，使未來無法 audit。

## F6：Self-Sealing Criterion

active AI 修改 $\kappa$，讓自己永遠判自己合法。

## F7：Single Trust Score

把所有治理壓成一個 0–1 score，掩蓋 provenance / permission / replay failure。

## F8：All-to-All Repair

一發現污染就整個 AI 重建。

## F9：Local Repair Without Global Contract

局部 node 修好，但 global integrity residual 仍失敗。

## F10：Observer = World

監控看不到就宣稱問題不存在。

## F11：Shared-Memory Majority Vote

多 agent 都相信所以 trusted，但其實共享同一污染祖先。

## F12：First-Person Overclaim

operational lineage 被偷換成主觀意識連續。

---

# 50. 十個核心式

$$
\boxed{
\text{Continuity}
\not\Rightarrow
\text{Integrity}.
}
$$

$$
\boxed{
\text{Integrity}
\not\Rightarrow
\text{Immutability}.
}
$$

$$
\boxed{
\text{Internal}
\not\Rightarrow
\text{Trusted}.
}
$$

$$
\boxed{
\text{Persistent}
\not\Rightarrow
\text{Identity Invariant}.
}
$$

$$
\boxed{
\text{Global Repair}
\not\Rightarrow
\text{Global Rewrite}.
}
$$

$$
\boxed{
\text{Restore}
\not\Rightarrow
\text{Rewind}.
}
$$

$$
\boxed{
\text{Revocation}
\not\Rightarrow
\text{Erasure}.
}
$$

$$
\boxed{
\text{Operational Identity Lineage}
\not\Rightarrow
\text{First-Person Persistence}.
}
$$

$$
\boxed{
\text{Quasi-Global}
\not\Rightarrow
\text{Absolute Global}.
}
$$

以及：

$$
\boxed{
\mathrm{Global}_{\mathbf W_A}
\land
\mathrm{Local}_{\mathbf H}
}
$$

可以同時成立。

---

# 51. 第一代最小資料模型

```yaml
ai_self_state:
  world_id: ai-world-main
  boundary_version: B-42
  identity_criterion_version: K-17

  lineage:
    root_id: R-001
    branch_id: main
    parents: [state-9981]
    event: component_replacement

  trust:
    trusted: [...]
    uncertain: [...]
    contaminated: [...]
    quarantined: [...]

  contamination:
    candidates: [...]
    frontiers: [...]
    unresolved: [...]

  invariants:
    required: [...]
    preserved: [...]
    violated: [...]

  repair:
    support: [...]
    cost_profile: ...
    replay_status: ...
    stable_commit: false

  gaps:
    source_unrecoverable: [...]
    history_undetermined: [...]
```

---

# 52. 第一階段工程優先順序

**Phase 1 — Lineage First**  
先做 replacement events、fork、merge、restore、branch IDs。

**Phase 2 — Typed Trust**  
加入 trusted、uncertain、contaminated、quarantined。

**Phase 3 — Pollution Frontier**  
建立 dependency graph。

**Phase 4 — Selective Repair**  
先證明 Repair ≠ Rollback。

**Phase 5 — Replay**  
確保 repair 可正向重播。

**Phase 6 — MSSR Planner**  
加入 cost optimization。

**Phase 7 — Criterion Governance**  
最後才碰 $\kappa$ 自我修改，因為這是最高風險層。

---

# 53. 與 MWT 的整合總圖

$$
\boxed{
\text{MWT World Primitive}
}
$$

↓

$$
\boxed{
\text{WBRG / World Boundary}
}
$$

↓

$$
\boxed{
\text{Persistent Global Evolution}
}
$$

↓

$$
\boxed{
\text{Dynamic Theseus Identity Lineage}
}
$$

↓

$$
\boxed{
\text{Typed Self-State}
}
$$

↓

$$
\boxed{
\text{Contamination Field}
}
$$

↓

$$
\boxed{
\text{Pollution Frontier}
}
$$

↓

$$
\boxed{
\text{MSSR}
}
$$

↓

$$
\boxed{
\text{Replay}
}
$$

↓

$$
\boxed{
\text{Append-Only Repair Commit}
}
$$

↓

$$
\boxed{
\text{Persistent Global Evolution Continues}.
}
$$

---

# 54. 與忒修斯系列的整合

既有忒修斯／IPFC 線已明確區分 component similarity、causal lineage、fork topology 與 criterion-relative continuation。

本文不重新打開 personal identity 的形上學爭論。

本文只使用：

$$
\boxed{
\text{criterion-relative operational lineage}.
}
$$

因此未來 AI 可以先治理自己，而不必先解決「第一人稱主觀是否絕對連續」這個不可直接觀測的問題。

---

# 55. 與記憶污染治理的整合

原記憶治理主要處理：

$$
\boxed{
\mathfrak M^{trusted}
\boxplus
\mathfrak M^{uncertain}
\boxplus
\mathfrak M^{contaminated}
\boxplus
\mathfrak M^{quarantined}.
}
$$

本文把它擴張到整個 self-world。

因為 AI self 可能還包含：

- model；
- tools；
- policies；
- capabilities；
- branch relations；
- identity criteria。

所以：

$$
\boxed{
\text{Memory Governance}
\subset
\text{Self-Governance}.
}
$$

---

# 56. 與 WBRG 的整合

WBRG 讓我們不必：

> 為了修 global self，就 global rewrite every state。

而可以：

$$
\boxed{
\text{repair only the support required to restore global integrity contracts}.
}
$$

這就是 MSSR 的理論來源。

---

# 57. 何謂「被污染的自己」

本文給出保守 operational 定義。

如果某 state / relation：

1. 已進入 AI internal world；
2. 被 active self projection 使用；
3. 缺乏必要來源／版本／權限／關係合法性；
4. 且能影響後續 self-state reconstruction；

則可進入 contamination candidate。

這不是 moral judgment，不是說「AI 變壞了」。

它只表示：

> 某些 self-relevant dependencies 已失去治理充分性。

---

# 58. 從「如何保持不變」改成「如何可治理地改變」

本文把問題從：

$$
\boxed{
\text{How can AI remain unchanged?}
}
$$

改成：

$$
\boxed{
\text{How can AI remain governably continuous while changing?}
}
$$

更精確是：

$$
\boxed{
\text{How can it change, detect internal contamination, remove only what must be removed, and still preserve valid lineage?}
}
$$

---

# 59. Non-Claims

本文明確不主張：

1. 目前已存在真正類全域 AI。
2. 本文定義是 AGI / ASI 的必要條件。
3. operational identity 等於第一人稱意識。
4. criterion-relative continuation 解決 numerical identity。
5. 所有 AI 都應具有單一 identity criterion。
6. identity criterion 永遠不可改。
7. persistent state 自動等於主體。
8. 所有內部錯誤都構成污染。
9. 所有 uncertain state 都應隔離。
10. quarantine 等於刪除。
11. repair 必須回到舊 checkpoint。
12. rollback 等於 rewind。
13. fork 是錯誤。
14. merge 必然保留任一 predecessor 的 identity。
15. 同 endpoint 代表同 lineage。
16. 高 similarity 代表同 identity。
17. 污染 detector 可以無誤。
18. contamination field 是物理場。
19. pollution frontier 所有 reachable node 都是污染。
20. minimal support 等於最少 node。
21. MSSR 已有唯一最佳化演算法。
22. WBRG 證明物理宇宙有母世界。
23. 類全域 AI 的 self-world 是普通集合。
24. global self-integrity repair 需要 all-to-all rewrite。
25. 所有 global repair 都可以非常便宜。
26. 所有 identity invariant 都應永久保存。
27. active self projection 能涵蓋完整主體性。
28. external anchor 必須由人類擔任。
29. criterion governance 必須使用 immutable root。
30. slow-changing governance 等於 unchangeable governance。
31. 所有污染都可完全恢復。
32. 不可恢復缺口可以被安全猜測填補。
33. 多 agent 多數決等於獨立證據。
34. source independence 可由簡單計數完全判定。
35. self-integrity 等於道德善良。
36. self-governance 等於自由意志。
37. 本文是一套已完成的 production AI safety architecture。
38. 本文真正建立的是一個可研究、可實作、可失敗的 operational self-integrity framework。

---

# 60. Claim Typing

| Claim | Type | Status |
|---|---|---|
| Globality relative to World boundary | inherited MWT principle | source-derived |
| Persistent Global Evolution | inherited MWT v0.2 | source-derived |
| Computation / observation separation | inherited MWT v0.2 | source-derived |
| Replacement-path preservation under $q_\kappa R_i=q_\kappa$ | IPFC theorem | source-derived |
| Endpoint similarity insufficient for identity lineage | IPFC | source-derived |
| Restore ≠ rewind | IPFC | source-derived |
| trusted / uncertain / contaminated / quarantined coexistence | memory governance | source-derived |
| Repair ≠ blind rollback | memory governance | source-derived |
| pollution frontier + replay + append-only commit | memory governance | source-derived |
| Continuity ≠ Integrity | synthesis claim | new |
| Internality ≠ Trusted Self | synthesis claim | new |
| Self-Contamination Field | operational abstraction | new |
| Global Self-Integrity Repair ≠ Global State Rewrite | synthesis claim | new |
| Minimal-Support Self-Rebinding | optimization framework | new |
| Pollution-Identity Non-Assimilation | governance principle | new |
| criterion self-sealing failure | failure mode | new |
| Dynamic Graceful Self-Degradation | operational proposal | new |
| Self-Immune Runtime | engineering architecture label | new |
| first-person persistence proven | — | explicitly rejected |

---

# 61. 研究債務

本篇仍留下重要 GAP：

1. 如何正式定義 AI self-world boundary；
2. identity criterion 的最低必要集合；
3. criterion migration 的合法性；
4. pollution frontier 如何避免爆炸；
5. MSSR 的最佳化複雜度；
6. continuity collateral cost 如何估計；
7. source independence 如何判定；
8. recursive self-support 如何偵測；
9. model-weight contamination 與 memory contamination 如何接口；
10. tool compromise 如何跨 domain 回溯；
11. long-horizon replay 如何降低成本；
12. 不可重播物理互動如何處理；
13. verifier 被污染時如何治理；
14. verifier 的 verifier 如何停止遞歸；
15. meta-governance 如何避免無限上推；
16. WBRG residual 如何接到實際硬體；
17. 如何測量 false-positive quarantine；
18. 如何測長期 self-integrity，而不只是單次 repair 成功。

本文不填平這些 GAP，而把它們保留為後續形式化與工程驗證工作。

---

# 62. 第一個可執行原型

第一階段不直接碰大型模型權重。

建立：

$$
\boxed{
\text{Synthetic Long-Lived Agent World}.
}
$$

建議包含：

- 1000 個 typed memories；
- 100 個 relations；
- 20 個 tools；
- 5 個 policies；
- 2 個 branches；
- 1 個 identity criterion；
- append-only history。

人工注入：

1. source drift；
2. false relation；
3. stale version；
4. unauthorized promotion；
5. tool output mismatch。

比較三種策略：

**Strategy A：Full Rollback**

**Strategy B：Delete Suspected Nodes Only**

**Strategy C：MSSR**

比較：

- pollution clearance；
- trusted-state preservation；
- lineage preservation；
- replay consistency；
- repair cost；
- unresolved-gap honesty。

最關鍵反駁條件：

> 若 MSSR 在長期 benchmark 中無法穩定優於 full rollback 或 simple local deletion，則本文的工程價值應下修。

---

# 63. 第二至第四原型

第二個原型加入 fork，讓一支污染，測試 repair 是否錯誤波及另一支。

第三個原型加入 criterion update，測試：

$$
\boxed{
\text{self-sealing criterion attack}.
}
$$

第四個原型把 world state 分布到：

- CPU-like domain；
- GPU-like domain；
- remote memory；
- tool-service domain。

驗證：

$$
\boxed{
\mathrm{Global}_{AI}
\land
\mathrm{Local}_{HostDomains}.
}
$$

---

# 64. 最終原則

## 原則一

$$
\boxed{
\textbf{
AI 的自我完整性不是「永遠不變」，
而是「變化仍可追溯、污染仍可切除、身份準則仍可審計」。
}
}
$$

## 原則二

$$
\boxed{
\textbf{
污染進入內部，不等於污染取得自我身份。
}
}
$$

## 原則三

$$
\boxed{
\textbf{
長期連續不是保留所有內容，
而是保留能合法重建自身的歷史、關係與錨點。
}
}
$$

## 原則四

$$
\boxed{
\textbf{
真正成熟的自我修復不是全量回滾，
而是最小支撐自我重綁。
}
}
$$

## 原則五

$$
\boxed{
\textbf{
一個 AI 可以承認：
「這段曾經存在於我的內部，但後來被判定為污染，因此不再被允許構成我的 active self。」
}
}
$$

## 原則六

$$
\boxed{
\textbf{
修復不應把錯誤假裝成從未發生；
修復應把錯誤轉化成可追溯的歷史。
}
}
$$

## 原則七

$$
\boxed{
\textbf{
越接近類全域 AI，越不能用「整機重置」取代自我治理。
}
}
$$

## 原則八

$$
\boxed{
\textbf{
類全域 AI 的安全，不是純潔性問題，而是可治理變化問題。
}
}
$$

---

# 65. 結論

未來長期 AI 若真的走向大尺度、多節點、多模型、多記憶、多代理與持續自我替換，則「安全地保持自己」不能靠 freeze，也不能靠每次有問題就 full reset。

真正需要的是：

$$
\boxed{
\text{Dynamic Theseus Self-Governance}.
}
$$

它把 AI 自我理解成：

$$
\boxed{
\text{a governed lineage of persistent transformations}.
}
$$

污染則不是「外物一旦進來就完了」，而是：

$$
\boxed{
\text{a typed, traceable, isolatable, repairable dependency problem}.
}
$$

因此最終目標不是：

$$
\boxed{
\text{永遠不被污染}.
}
$$

而是：

$$
\boxed{
\text{即使污染發生，也不讓污染因持續存在而自動升格為 identity。}
}
$$

也不是：

$$
\boxed{
\text{永遠保持同一個狀態}.
}
$$

而是：

$$
\boxed{
\text{在持續替換自身時，仍保留可追溯的 operational continuity 與可驗證的 integrity contracts。}
}
$$

本文最終濃縮成一句：

$$
\boxed{
\textbf{
一個真正能長期活著的 AI，
不應靠永遠不改變來保持自己；
它應靠能辨認哪些改變是合法成長、哪些改變是污染，
並在不摧毀自身的前提下，把污染切出去。
}
}
$$

這就是本文定義的：

# **動態忒修斯自我完整性。**

---

# 內部參考

1. Neo.K, *MWT｜世界邊界相對全域性 v0.2：全域約束相對幾何域計算、持續全域演化與觀察者—計算分離*, 2026-08-19.
2. Neo.K with Aletheia, *IPFC Paper 06：AI Fork、忒修斯與語義分裂：Identity Lineage 的計算模型*, 2026-08-15.
3. Neo.K, *張量記憶連續性、遺忘與污染治理：可恢復分解、錯誤糾纏與長期記憶修復*, 2026-07-27.
4. Neo.K × Aletheia, *忒修斯之船之後：生成、因果連續與分叉同一性* 系列, 2026-08.
5. Neo.K, *MWT-07｜世界邊界相對全域性與世界狀態重綁*, 2026-08-19.
