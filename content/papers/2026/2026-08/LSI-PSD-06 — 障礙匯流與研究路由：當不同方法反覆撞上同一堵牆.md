# LSI-PSD-06 — 障礙匯流與研究路由：當不同方法反覆撞上同一堵牆

## Obstruction Confluence and Research Routing: When Independent Proof Routes Repeatedly Hit the Same Barrier

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 06  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Obstruction-Confluence and Routing Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文將 obstruction、confluence、no-go region、route inheritance 與 barrier robustness 定義為長程 AI 數學研究的可觀測方法論物件。除非另有嚴格定理，本文不把「多條研究路線反覆遇到同一障礙」等同於該障礙在底層數學中具有絕對必然性，也不把 route confluence 等同於不可證性、獨立性、命題為假、問題範疇錯誤或任何特定未解問題的最終判決。本文研究的是**搜尋制度內的障礙證據如何累積、去重、交叉驗證與觸發研究路由改變**。

---

## 摘要

在單次 theorem proving 中，一次失敗通常只是一個局部事件：某個 tactic 不適用、某個 lemma 缺失、某個 goal 未關閉、某個編譯器回報 type mismatch。然而在長程 AI 數學研究中，同類失敗可能跨越數十、數百甚至更多 artifact 被反覆重建。更重要的是，表面上彼此獨立的研究方法可能經過不同表示、不同引理鏈、不同尺度與不同 decomposition，最終反覆命中同一類不可閉合節點。這時候，失敗不再只是：

$$
r_i\rightarrow\bot,
$$

而可能形成：

$$
r_1\rightarrow O,
\qquad
r_2\rightarrow O,
\qquad
\ldots,
\qquad
r_m\rightarrow O,
$$

其中 $O$ 是一個經過 canonicalization 與 audit 的 obstruction class。

本文建立「障礙匯流」的操作性理論。核心主張是：長程 AI 研究應把 obstruction 從臨時錯誤訊息提升成一等研究物件，建立 canonical obstruction ID、assumption profile、route provenance、first-hit time、revisit count、cross-basin support、repair history、escape history 與 audit status。只有如此，系統才可能分辨：

$$
\text{same textual failure}
$$

與：

$$
\text{same mathematical obstruction},
$$

也才能避免把同一堵牆換十種語言重新撞十次。

本文定義 weighted confluence：

$$
C_w(O)
=
\sum_{r\in\mathcal R(O)}
\omega(r,O),
$$

但進一步指出 raw route count 會被「同源路線複製」嚴重灌水，因此提出 independence-corrected confluence：

$$
C_{\mathrm{ind}}(O),
$$

其權重依賴 route genealogy、representation distance、method-family distance、premise overlap 與 shared-memory overlap。兩條只有 prompt 改寫不同的路線，不應與兩條由不同方法族、不同形式化、不同模型與不同前提集合獨立命中同一障礙的路線等價計分。

本文進一步區分至少六種 obstruction：

1. local formal obstruction；
2. missing-premise obstruction；
3. representation obstruction；
4. method-family obstruction；
5. resource obstruction；
6. statement／framing obstruction candidate。

其中最後一類只能是**候選診斷**，除非存在形式 counterexample、inconsistency、faithfulness audit 或更強的重新表述定理，不得從失敗頻率推得「原問題問錯了」。

2026 年 formal theorem proving 的若干系統已經出現與本文高度相鄰的工程訊號。APRIL 把 260,000 組 Lean proof failure、compiler diagnostic、repair 與 explanation 對齊成 supervised data；Mechanic 以 sorry-driven decomposition 保留已驗證區段並隔離 unresolved subgoal；Goedel-Architect 要求失敗 lemma 回傳 structured diagnosis、forensic trace 與 suggested fix，再用於 blueprint refinement；LeanMarathon 把長程 formalization 的 goal drift、dependency tangle 與 local repair contamination 視為系統級問題；2026 的 Lean benchmark audit 進一步指出，kernel-verified proof 也不能保證 formal statement faithful 地代表原始意圖，並辨識出 counterexample、vacuity、missing hypothesis 與 specification hazard 等缺陷。這些工作共同顯示：**失敗、錯誤、診斷與 proof graph 結構已逐漸從邊角 log 轉成 theorem-proving 系統的核心資料。**

本文最後將這套框架接回 NS-203 corpus。既有 observatory 已觀察到大量 recurrence、no-go、confluence 與高階採樣，但目前最合理的使用方式不是宣布 Navier--Stokes 存在某個「終極障礙」，而是建立 obstruction canonicalization pipeline，測試不同 series 是否真的在 assumption-normalized 意義下反覆命中同一 $O$。若未來能得到跨方法、跨表示、跨模型與跨 basin 的高獨立性 confluence，則應提高：

$$
\operatorname{Priority}(\text{obstruction-focused research}),
$$

而不是直接提高：

$$
P(\text{unprovable}).
$$

本文由此提出一個核心原則：

$$
\boxed{
\textbf{Repeated failure becomes scientific information only after the failure itself is canonicalized, audited, and genealogically de-duplicated.}
}
$$

**關鍵詞：** obstruction、confluence、proof route、research routing、canonical obstruction ID、no-go、proof repair、failure diagnosis、route genealogy、weighted confluence、independence correction、AI theorem proving、proof-space observatory

---

# 1. 問題的提出：失敗到底是不是資訊？

## 1.1 單次失敗通常資訊很少

設：

$$
Q
$$

是一個目標 theorem。

某條 proof route：

$$
r_1
$$

失敗：

$$
r_1(Q)\rightarrow\bot.
$$

從單次失敗本身，我們通常不知道：

- theorem 是假；
- tactic 選錯；
- premise 缺失；
- proof 太長；
- representation 不適合；
- model 不夠強；
- budget 不夠；
- formalization 有錯；
- verifier error；
- theorem statement 有缺陷；
- 或只是 implementation bug。

因此：

$$
\boxed{
\text{one failure}
\approx
\text{low-information event}.
}
$$

## 1.2 長程研究改變了問題

如果：

$$
r_1,r_2,\ldots,r_m
$$

表面上不同，

卻都停在同一個局部缺口：

$$
O,
$$

研究者開始獲得額外資訊。

例如：

$$
r_{\mathrm{energy}}\rightarrow O,
$$

$$
r_{\mathrm{compactness}}\rightarrow O,
$$

$$
r_{\mathrm{recurrence}}\rightarrow O,
$$

$$
r_{\mathrm{geometric}}\rightarrow O.
$$

這時候新的研究問題不再只是：

> 怎麼證 $Q$？

而變成：

> 為什麼這些方法都要經過 $O$？

這就是 obstruction confluence。

## 1.3 但「看起來一樣」非常危險

兩個失敗文字：

> 無法控制剩餘項。

可能指：

$$
E_1
$$

與：

$$
E_2
$$

兩個完全不同的剩餘項。

相反地，兩個完全不同的自然語言描述，也可能在形式化後是同一個未閉合條件。

所以必須區分：

$$
\text{textual recurrence}
$$

與：

$$
\text{mathematical obstruction recurrence}.
$$

本文的全部工作，就是把這個區分工程化。

---

# 2. 從 error log 到 obstruction object

## 2.1 Error 不等於 obstruction

定義：

$$
e
=
\text{某次具體錯誤事件}.
$$

例如 Lean compiler：

```text
type mismatch
unsolved goals
unknown constant
failed to synthesize instance
```

這些首先只是：

$$
\text{formal error event}.
$$

只有當多個 error event 被映射到一個穩定數學缺口：

$$
e_1,e_2,\ldots,e_k
\mapsto
O,
$$

才能形成 obstruction candidate。

## 2.2 Obstruction 的最小表示

本文建議 obstruction 至少表示成：

$$
O
=
(
D,
A,
G,
M,
R,
S
),
$$

其中：

- $D$：domain；
- $A$：normalized assumptions；
- $G$：unclosed goal／gap；
- $M$：mechanism of failure；
- $R$：repair history；
- $S$：status。

例如：

```yaml
obstruction_id: O-0042
domain: PDE
assumptions:
  - critical_scaling
  - bounded_energy
gap:
  type: uncontrolled_term
  normalized_statement: ...
mechanism:
  - estimate_closes_only_subcritical
repair_history:
  - interpolation_attempt
  - compactness_attempt
status:
  - audited_candidate
```

## 2.3 Obstruction 必須帶 assumptions

同一個結論缺口：

$$
G
$$

在不同假設下可能是不同 obstruction。

因此不能只存：

$$
O=G.
$$

更正確是：

$$
O=(A,G).
$$

如果：

$$
A_1\neq A_2,
$$

則：

$$
O_1
$$

與：

$$
O_2
$$

不能自動合併。

---

# 3. Canonical Obstruction ID

## 3.1 為什麼需要 ID

長程 corpus 中，如果每篇論文都重新寫：

- residual gap；
- closure defect；
- uncontrolled supplier；
- missing rigidity；
- pressure mismatch；

而沒有 canonical ID，

系統會失去：

$$
\text{cross-paper memory}.
$$

於是同一 obstruction 每次都像第一次發現。

## 3.2 Canonicalization pipeline

本文提出：

$$
e
\rightarrow
O_{\mathrm{raw}}
\rightarrow
O_{\mathrm{norm}}
\rightarrow
[O].
$$

步驟：

1. error extraction；
2. mathematical gap extraction；
3. assumption normalization；
4. notation normalization；
5. dependency normalization；
6. semantic equivalence audit；
7. canonical ID assignment。

## 3.3 不允許自動過度合併

若：

$$
\operatorname{sim}(O_i,O_j)>\tau,
$$

只能產生：

$$
\text{merge candidate}.
$$

不能直接：

$$
O_i=O_j.
$$

因為錯誤合併會製造假的 confluence。

---

# 4. Obstruction equivalence

## 4.1 強等價

若存在形式證明：

$$
A_i\vdash G_i\leftrightarrow G_j,
$$

且 assumptions 已對齊，

則可標記：

$$
O_i\equiv O_j.
$$

## 4.2 弱等價

若缺乏形式證明，但 theorem-level audit 顯示：

- 同一 normalized gap；
- 同一 dependency boundary；
- 同一 repair requirement；

可標：

$$
O_i\approx O_j.
$$

## 4.3 僅相似

若只有 embedding／lexical similarity：

$$
O_i\sim_{\mathrm{text}} O_j,
$$

不得合併。

## 4.4 Equivalence confidence

定義：

$$
c_{\mathrm{eq}}(O_i,O_j)\in[0,1].
$$

來源包括：

- formal equivalence；
- human audit；
- independent model audit；
- proof dependency equivalence；
- counterexample agreement。

---

# 5. Route：什麼才算一條不同的研究路線

## 5.1 Route 不是 paper

一篇 paper 可能包含：

$$
r_1,r_2,\ldots,r_k.
$$

反過來，同一 route 可以跨多篇 paper 延續。

所以：

$$
\boxed{
\text{artifact count}
\neq
\text{route count}.
}
$$

## 5.2 Route representation

令：

$$
r
=
(
L,
P,
M,
X,
H
),
$$

其中：

- $L$：representation language；
- $P$：premise set；
- $M$：method family；
- $X$：intermediate proof-state sequence；
- $H$：research genealogy。

## 5.3 Route endpoint

若 route 成功：

$$
r\rightarrow\operatorname{Proof}(Q).
$$

若失敗：

$$
r\rightarrow O.
$$

若未知：

$$
r\rightarrow ?.
$$

---

# 6. Confluence：不同路線匯流到同一 obstruction

## 6.1 Raw confluence count

對 obstruction $O$：

$$
\mathcal R(O)
=
\{
r:r\rightarrow O
\}.
$$

最簡單：

$$
C_{\mathrm{raw}}(O)
=
|\mathcal R(O)|.
$$

## 6.2 Raw count 的問題

若研究者把同一 prompt 改十個詞，

生成十條幾乎相同 route：

$$
r_1\approx r_2\approx\cdots\approx r_{10},
$$

則：

$$
C_{\mathrm{raw}}=10
$$

會嚴重誇大證據。

## 6.3 Independence-corrected confluence

定義兩 route 的相依程度：

$$
d_{\mathrm{dep}}(r_i,r_j)\in[0,1],
$$

其中高值表示高度共享：

- 方法；
- premise；
- memory；
- model；
- representation；
- ancestor route。

令 route 新穎權重：

$$
\omega_i
=
\frac{1}{
1+
\sum_{j<i}d_{\mathrm{dep}}(r_i,r_j)
}.
$$

則：

$$
\boxed{
C_{\mathrm{ind}}(O)
=
\sum_{r_i\in\mathcal R(O)}
\omega_i.
}
$$

這不是唯一正確公式，而是一個可審計起點。

---

# 7. Route genealogy

## 7.1 為什麼 genealogy 比 model count 重要

兩個不同模型：

$$
M_1,M_2
$$

若都讀同一份 handoff、同一份 prior proof、同一組 lemma，

它們並不真正獨立。

所以：

$$
\text{different model}
\not\Rightarrow
\text{independent route}.
$$

## 7.2 Genealogy graph

建立：

$$
G_{\mathrm{route}}
=
(V_{\mathrm{route}},E_{\mathrm{ancestor}}).
$$

若：

$$
r_j
$$

直接引用：

$$
r_i,
$$

則：

$$
r_i\rightarrow r_j.
$$

## 7.3 Independent root

若兩條 route：

$$
r_a,r_b
$$

在 ancestor graph 中共享的最近公共祖先很早，

且中間 method／representation 分叉明顯，

則 independence 較高。

---

# 8. Representation distance

## 8.1 同一 obstruction 跨表示出現更有資訊

若：

$$
\mathcal L_1\neq\mathcal L_2
$$

而兩條 route 經 audit 都命中：

$$
O,
$$

其 confluence 證據通常比純同語言重訪強。

## 8.2 表示距離

定義：

$$
d_L(r_i,r_j)
$$

可以參考：

- notation；
- coordinate system；
- state variables；
- theorem encoding；
- proof assistant；
- symbolic vocabulary。

## 8.3 但 representation diversity 也可能是假

如果只是：

$$
x\mapsto y
$$

的機械改名，

則：

$$
d_L
$$

應接近零。

所以 representation distance 不能只看 token。

---

# 9. Method-family distance

## 9.1 方法族

例如：

$$
\mathcal M
=
\{
\text{energy},
\text{compactness},
\text{combinatorial},
\text{topological},
\text{probabilistic},
\text{algebraic}
\}.
$$

## 9.2 方法匯流

若：

$$
r_{\mathrm{energy}}\rightarrow O,
$$

$$
r_{\mathrm{topology}}\rightarrow O,
$$

$$
r_{\mathrm{compactness}}\rightarrow O,
$$

則：

$$
C_{\mathrm{method}}(O)
$$

上升。

## 9.3 方法族名稱不夠

同一篇路線可能是 hybrid：

$$
M(r)
=
(
0.5\ \text{energy},
0.3\ \text{compactness},
0.2\ \text{geometry}
).
$$

因此方法距離可寫：

$$
d_M(r_i,r_j)
=
1-
\operatorname{sim}(M(r_i),M(r_j)).
$$

---

# 10. Premise overlap

## 10.1 共享 premise 會降低獨立性

兩條 route 如果使用：

$$
P_i\approx P_j,
$$

則命中同一 obstruction 不一定令人驚訝。

## 10.2 Jaccard 型指標

令：

$$
J_P(r_i,r_j)
=
\frac{
|P_i\cap P_j|
}{
|P_i\cup P_j|
}.
$$

高：

$$
J_P
$$

表示 premise 高重疊。

## 10.3 Global premise 的意義

LeanSearch v2 類工作提醒：

> 單步最相關 premise 與整個 theorem 需要的 global premise set 是不同問題。

因此某個 obstruction 可能不是 theorem 本身的深障礙，

而只是：

$$
\boxed{
\text{premise omission}.
}
$$

這種 obstruction 應該被單獨分類。

---

# 11. Obstruction taxonomy I：Local Formal Obstruction

## 11.1 定義

例如：

- type mismatch；
- unsolved goal；
- coercion mismatch；
- instance synthesis failure；
- unavailable theorem。

## 11.2 特性

它通常：

$$
\text{local},
$$

$$
\text{repairable},
$$

$$
\text{highly verifier-specific}.
$$

## 11.3 不應過度哲學化

如果 obstruction 只是：

> 少 import 一個 namespace。

那就不要把它升級成：

> 數學表示語言的本體危機。

這是 observatory 必須具備的克制。

---

# 12. Obstruction taxonomy II：Missing-Premise Obstruction

## 12.1 定義

目標可能可證，

但當前 route 缺少：

$$
p^\star.
$$

所以：

$$
P_{\mathrm{current}}
\not\vdash Q,
$$

但：

$$
P_{\mathrm{current}}\cup\{p^\star\}
\vdash Q.
$$

## 12.2 診斷方式

- global retrieval；
- theorem dependency search；
- library search；
- human premise injection。

## 12.3 Repair 後應降級

如果加入：

$$
p^\star
$$

後 obstruction 消失，

則：

$$
O
$$

不應繼續被記成高階 barrier。

它應標記：

$$
\text{resolved premise obstruction}.
$$

---

# 13. Obstruction taxonomy III：Representation Obstruction

## 13.1 定義

同一 mathematical target：

$$
Q
$$

在表示：

$$
L_1
$$

下難以閉合，

但在：

$$
L_2
$$

下可解。

## 13.2 判定

若：

$$
\operatorname{Cost}(Q\mid L_1)\gg
\operatorname{Cost}(Q\mid L_2),
$$

且 semantic faithfulness 已確認，

則可標：

$$
O_{\mathrm{repr}}.
$$

## 13.3 不能把 representation difficulty 當 theorem difficulty

這是長程 AI proof search 特別容易犯的錯。

---

# 14. Obstruction taxonomy IV：Method-Family Obstruction

## 14.1 定義

一整個方法族：

$$
\mathcal M_a
$$

在特定 assumptions 下反覆碰到：

$$
O.
$$

## 14.2 Family-level no-go candidate

若對多個 route：

$$
r\in\mathcal M_a
$$

有：

$$
r\rightarrow O,
$$

可標：

$$
\operatorname{NoGoCandidate}(\mathcal M_a,O).
$$

## 14.3 仍需明確量詞

不能從有限樣本：

$$
r_1,\ldots,r_m
$$

直接寫：

$$
\forall r\in\mathcal M_a,\ r\rightarrow O.
$$

除非真的有 theorem。

---

# 15. Obstruction taxonomy V：Resource Obstruction

## 15.1 定義

存在 route：

$$
r^\star
$$

但：

$$
C(r^\star)>\mathcal B.
$$

## 15.2 表面特徵

- progress 緩慢；
- context 超長；
- repeated partial closure；
- same residual gap；
- timeout；
- token exhaustion。

## 15.3 診斷

做：

$$
\mathcal B\rightarrow c\mathcal B.
$$

若 obstruction 消失，

則應重新分類。

---

# 16. Obstruction taxonomy VI：Statement / Framing Obstruction Candidate

## 16.1 最危險的一類

當多條高獨立性 route 都在同一 statement boundary 卡住，

研究者可能懷疑：

$$
\text{statement itself}.
$$

## 16.2 但頻率不能證明 statement 錯

必須保持：

$$
\boxed{
C_{\mathrm{ind}}(O)\uparrow
\not\Rightarrow
\operatorname{False}(Q).
}
$$

也不能推出：

$$
\operatorname{Misframed}(Q).
$$

## 16.3 什麼證據才會更強

例如：

- formal counterexample；
- inconsistent hypotheses；
- vacuity；
- missing hypothesis；
- semantic mismatch；
- quantifier error；
- domain mismatch；
- reformulation theorem。

這些才有資格把 diagnosis 往 statement 層移動。

---

# 17. APRIL：失敗資料本身可以成為訓練集

## 17.1 傳統資料偏向成功 proof

2026 年 APRIL 指出，既有 Lean datasets 幾乎都集中於正確 proof。

這使模型缺乏：

$$
\text{failure-conditioned supervision}.
$$

## 17.2 260,000 failure tuples

APRIL 建立：

$$
(\text{failed proof},
\text{compiler diagnostic},
\text{repair},
\text{explanation})
$$

的對齊資料。

## 17.3 對本文的意義

這支持一個工程事實：

$$
\boxed{
\text{failed proof traces can be reusable learning objects}.
}
$$

本文只是再向上提升一階：

$$
\text{local failure tuple}
\rightarrow
\text{cross-route obstruction class}.
$$

---

# 18. Mechanic：不要把整條失敗路線丟掉

## 18.1 兩種傳統修復

Mechanic 指出常見方法：

1. 全部重生成；
2. 在原 proof 上不斷 patch。

第一種浪費已正確部分。

第二種會讓 context 越來越長。

## 18.2 Sorry-driven decomposition

Mechanic 用：

$$
\texttt{sorry}
$$

隔離 unresolved subgoal，

保留已 verified proof structure。

## 18.3 對 obstruction observatory 的啟發

每個 unresolved subgoal 可以成為：

$$
O_{\mathrm{local}}.
$$

而不是把整篇 proof 標：

$$
\text{failed}.
$$

這使 failure localization 成為可能。

---

# 19. Goedel-Architect：structured post-mortem 已經出現

## 19.1 失敗不只回傳「沒證出來」

Goedel-Architect 在 prover 放棄 lemma 時，要求 structured diagnosis：

- tried what；
- stalled where；
- gap hypothesis；
- suggested fix。

## 19.2 Blueprint refinement

失敗 trace 會回寫：

$$
\text{dependency graph}.
$$

修正：

- hard lemma decomposition；
- dependency rewiring；
- false statement repair；
- node drop。

## 19.3 與本文的關係

這非常接近：

$$
r\rightarrow O
\rightarrow
\operatorname{RouteUpdate}(G).
$$

也就是 obstruction 不再是終點，

而是：

$$
\boxed{
\text{research routing signal}.
}
$$

---

# 20. LeanMarathon：長程研究的失敗是系統級的

## 20.1 失敗不只在 hard lemma

LeanMarathon 指出 research-level formalization 的問題包括：

- statement drift；
- dependency tangle；
- context decay；
- local repair corrupting distant work。

## 20.2 Goal drift

系統可能得到一張 formally correct graph，

但其實已離開原始 theorem。

因此：

$$
\text{formal closure}
\not\Rightarrow
\text{target fidelity}.
$$

## 20.3 Obstruction observatory 必須保存 target fidelity

所以 $O$ 的 metadata 應包含：

$$
F_T(O)
=
\text{target fidelity status}.
$$

否則系統可能「解掉」一個 obstruction，

只是因為偷偷改了問題。

---

# 21. Benchmark defects：形式驗證不等於語義無錯

## 21.1 2026 benchmark audit 的警告

近期 Lean benchmark audit 在多個 benchmark 中發現：

- counterexample；
- vacuous theorem；
- unsound axiom；
- missing hypothesis；
- incorrect translation；
- specification hazard。

## 21.2 對本文的核心意義

如果 formal statement：

$$
Q_F
$$

與 intended statement：

$$
Q_I
$$

不一致，

那麼 obstruction 可能來自：

$$
Q_F,
$$

不是：

$$
Q_I.
$$

## 21.3 所以 obstruction 必須帶 statement fingerprint

至少：

```text
informal_target_hash
formal_target_hash
translation_version
faithfulness_audit
```

否則跨 artifact 合併 obstruction 會非常危險。

---

# 22. Local success, global failure：Grasshopper case 的啟發

## 22.1 局部 lemma 都能成功

2026 的 Grasshopper formalization case 顯示，AI 可以證明多個 helper lemmas，

但主 theorem 仍卡在 global counting step。

## 22.2 這是一個乾淨的 obstruction 例子

形式：

$$
L_1,L_2,L_3,L_4
$$

皆 verified，

但：

$$
L_1\land L_2\land L_3\land L_4
\not\Rightarrow
Q
$$

因為缺：

$$
O_{\mathrm{global}}.
$$

## 22.3 對長程研究的重要性

系統如果只統計：

$$
\text{verified lemma count},
$$

會高估整體進展。

所以 obstruction graph 必須和 achievement graph 同時存在。

---

# 23. Obstruction graph

## 23.1 節點

令：

$$
V_O
=
\{O_1,\ldots,O_n\}.
$$

## 23.2 邊

可定義：

- implies；
- refines；
- transforms；
- inherits；
- co-occurs；
- escapes-to；
- resolves；
- revives。

例如：

$$
O_1\rightarrow O_2
$$

表示修掉 $O_1$ 後暴露 $O_2$。

## 23.3 這不是單純 failure list

真正的 obstruction graph 記錄：

$$
\boxed{
\text{structure of failure transitions}.
}
$$

---

# 24. Obstruction inheritance

## 24.1 子路線繼承父路線的障礙

若：

$$
r_2
$$

直接基於：

$$
r_1,
$$

而未改變產生 $O$ 的核心 assumptions，

則：

$$
r_2\rightarrow O
$$

不能被當成完全新證據。

## 24.2 Inheritance coefficient

定義：

$$
h(r_2\leftarrow r_1,O)\in[0,1].
$$

高值代表 obstruction 幾乎被直接繼承。

## 24.3 修正 confluence

可用：

$$
\omega(r_2,O)
=
1-
\max_{r_1\prec r_2}
h(r_2\leftarrow r_1,O).
$$

---

# 25. Obstruction revival

## 25.1 已解障礙可能在更高階回來

一階修掉：

$$
O^{(1)}.
$$

但在二階 relation 又出現：

$$
O^{(2)}.
$$

例如：

> 局部項已控制，但全域累積後重新失控。

## 25.2 Revival ID

應保存：

$$
O^{(1)}
\rightsquigarrow
O^{(2)}.
$$

不是重新建立新名字完全失去 genealogy。

## 25.3 高階採樣

這正接到 LSI-PSD-04：

$$
\Omega^{(0)}
\rightarrow
\Omega^{(1)}
\rightarrow
\Omega^{(2)}.
$$

障礙本身也可能有 order。

---

# 26. Confluence degree

## 26.1 Basin confluence

令：

$$
\mathcal B(O)
=
\{B_i:B_i\rightarrow O\}.
$$

定義：

$$
C_B(O)
=
|\mathcal B(O)|.
$$

## 26.2 Method confluence

$$
C_M(O)
=
|\mathcal M(O)|.
$$

## 26.3 Representation confluence

$$
C_L(O)
=
|\mathcal L(O)|.
$$

## 26.4 Model confluence

$$
C_A(O)
=
|\mathcal A(O)|.
$$

其中 $\mathcal A$ 此處表示 agent/model family，避免和 assumptions 混淆時可在資料結構中另命名。

## 26.5 Confluence vector

因此更合理：

$$
\boxed{
\mathbf C(O)
=
(
C_B,
C_M,
C_L,
C_A,
C_{\mathrm{ind}}
).
}
$$

而不是一個數字。

---

# 27. Weighted obstruction robustness

## 27.1 Robustness score

定義：

$$
R_O
=
f(
C_{\mathrm{ind}},
C_B,
C_M,
C_L,
A_O,
E_O
),
$$

其中：

- $A_O$：audit depth；
- $E_O$：escape resistance。

## 27.2 仍是 search-regime evidence

即使：

$$
R_O\rightarrow1,
$$

也只能表示：

> 在已觀測制度內，該 obstruction 非常穩健。

不是：

> 數學宇宙保證這是終極牆。

---

# 28. Escape obstruction

## 28.1 Escape 也可能匯流

在 LSI-PSD-05 中：

$$
B
\xrightarrow{a}
B'.
$$

如果多種 escape action：

$$
a_1,a_2,a_3
$$

最後都命中：

$$
O_{\mathrm{esc}},
$$

則這個 obstruction 比 basin 內部 obstruction 更值得注意。

## 28.2 Escape-confluence

定義：

$$
C_{\mathrm{esc}}(O)
=
|\{
a:a(B)\rightarrow O
\}|.
$$

## 28.3 例子

- 換 representation 還是卡；
- 換 method 還是卡；
- 增 budget 還是卡；
- 換 model 還是卡；
- global premise retrieval 還是卡。

這會提高：

$$
\text{framing audit priority}.
$$

但仍不等於 framing error proof。

---

# 29. No-go region

## 29.1 從單一路線 no-go 到方法區域 no-go

若有定理真的證明：

$$
\forall r\in\mathcal R_S,
\quad
r\not\Rightarrow Q,
$$

則：

$$
\mathcal R_S
$$

是一個真正的 no-go region。

## 29.2 Empirical no-go candidate

若只是大量採樣：

$$
r_1,\ldots,r_n
$$

皆失敗，

只能稱：

$$
\boxed{
\text{empirical no-go candidate}.
}
$$

## 29.3 名稱紀律

Observatory UI 必須明確區分：

```text
NO-GO STATUS:
- theorem-certified
- formally refuted route class
- empirical candidate
- heuristic warning
```

---

# 30. Obstruction entropy

## 30.1 研究失敗是否集中

令近期失敗在 obstruction class 上的分布：

$$
p_i.
$$

定義：

$$
H_O
=
-
\sum_i p_i\log p_i.
$$

## 30.2 低 entropy

如果：

$$
H_O\downarrow,
$$

表示失敗越來越集中於少數 obstruction。

這可能是：

- proof-space contraction；
- basin lock-in；
- taxonomy 過粗；
- 真正 confluence。

## 30.3 必須配合獨立性

只有：

$$
H_O\downarrow
$$

和：

$$
C_{\mathrm{ind}}\uparrow
$$

同時發生，才更支持「不同路線真正匯流」。

---

# 31. First-hit time 與 rediscovery lag

## 31.1 首次出現

對 obstruction $O$：

$$
t_0(O).
$$

## 31.2 重訪時間

$$
t_1,t_2,\ldots.
$$

## 31.3 Rediscovery lag

$$
\Delta t_i
=
t_i-t_{i-1}.
$$

## 31.4 長期趨勢

若：

$$
\Delta t_i\downarrow,
$$

可能表示研究越來越被 $O$ 吸引。

若：

$$
\Delta t_i\uparrow,
$$

可能表示 escape 成功，只有偶爾重訪。

---

# 32. Obstruction centrality

## 32.1 不是所有障礙一樣重要

某個 $O$ 只阻擋：

$$
1
$$

條 fringe route。

另一個 $O^\star$ 阻擋：

$$
50
$$

條 central routes。

## 32.2 Route-weighted centrality

定義：

$$
Z(O)
=
\sum_{r\rightarrow O}
\operatorname{Importance}(r)\omega(r,O).
$$

## 32.3 研究優先級

高：

$$
Z(O)
$$

的 obstruction 更值得：

- human audit；
- formalization；
- counterexample search；
- new-theory generation。

---

# 33. Obstruction budget allocation

## 33.1 Agent 海戰術不能平均分配

如果有：

$$
O_1,\ldots,O_n,
$$

不應每個分一樣多 agent。

## 33.2 Priority function

$$
P_O
=
g(
Z,
C_{\mathrm{ind}},
E_{\mathrm{esc}},
\text{transfer potential},
\text{verification cost}
).
$$

## 33.3 目標

最大化：

$$
\sum_O
\mathbb E[
\Delta U(O)
].
$$

不是最大化：

$$
\text{number of generated papers}.
$$

---

# 34. Repair taxonomy

## 34.1 Local patch

$$
O\rightarrow\text{patch}.
$$

## 34.2 Lemma insertion

$$
O
\rightarrow
L^\star
\rightarrow
\text{closure}.
$$

## 34.3 Dependency rewiring

$$
P_i
\rightarrow
P_j.
$$

## 34.4 Statement repair

$$
Q
\rightarrow
Q'.
$$

## 34.5 Representation switch

$$
L_1
\rightarrow
L_2.
$$

## 34.6 Method switch

$$
M_1
\rightarrow
M_2.
$$

## 34.7 Problem split

$$
Q
\rightarrow
(Q_1,Q_2,\ldots,Q_k).
$$

每次 repair 都應保留：

$$
\text{before/after obstruction state}.
$$

---

# 35. Repair success 也可能是假

## 35.1 Goal drift

如果 repair：

$$
Q\rightarrow Q'
$$

而：

$$
Q'\neq Q,
$$

proof success 可能只是逃離原問題。

## 35.2 Faithfulness gate

要求：

$$
F(Q,Q')>\tau_F.
$$

如果 statement 必須改，

則必須明示：

$$
\text{original theorem changed}.
$$

## 35.3 Obstruction resolution status

不要只標：

```text
RESOLVED
```

而要標：

```text
RESOLVED_BY:
- proof
- stronger premise
- weaker conclusion
- corrected statement
- representation change
- counterexample
```

---

# 36. NS-203：應如何真正測 confluence

## 36.1 現況

v0.1 observatory 已看到：

- recurrence 高；
- no-go 高；
- X72 有 confluence 語言；
- DCRP 出現 higher-order residue；
- 跨 series traffic 明顯。

## 36.2 目前還不能直接說同一 obstruction

因為 broad concept family：

$$
\text{carrier-supplier},
$$

$$
\text{rigidity-closure},
$$

$$
\text{obstruction-gap-defect}
$$

仍然太粗。

## 36.3 第二輪需要 theorem-level extraction

每份 artifact 抽：

$$
A_i,
C_i,
L_i,
O_i,
S_i.
$$

然後建立：

$$
O_i\approx O_j?
$$

## 36.4 Cross-series confluence test

例如：

$$
O_{\mathrm{X72}}
$$

與：

$$
O_{\mathrm{DCRP}}
$$

若 normalized assumptions 與 terminal gap 真正等價，

才算：

$$
C_B(O)\uparrow.
$$

不是因為都寫了：

> closure gap。

---

# 37. 一個 NS Obstruction Record 範例

```yaml
obstruction_id: NS-O-017
source:
  series:
    - X72
    - DCRP
first_seen: ...
assumption_profile:
  scaling: critical
  regularity: ...
  geometry: ...
normalized_gap:
  statement: ...
route_families:
  - pure_continuous
  - recurrence_shadowing
representations:
  - ...
audits:
  semantic_equivalence: pending
  theorem_level: partial
confluence:
  raw: 9
  independence_corrected: 2.8
status:
  empirical_candidate
nonclaims:
  - not_unprovability
  - not_misframing_proof
```

這比：

> 大家又卡住了。

有用得多。

---

# 38. Counterexample channel

## 38.1 Obstruction 不一定需要 repair

如果找到：

$$
x
$$

使：

$$
A(x)
$$

成立但：

$$
Q(x)
$$

不成立，

那麼：

$$
Q
$$

被反例處理。

## 38.2 Counterexample 是最高價值的 obstruction resolution 之一

它把：

$$
\text{suspected statement obstruction}
$$

升級成：

$$
\text{formal disproof}.
$$

## 38.3 搜尋策略

對高：

$$
C_{\mathrm{ind}}(O)
$$

且懷疑 statement 的節點，

系統應增加：

$$
\text{counterexample budget}.
$$

---

# 39. Formalization audit channel

## 39.1 先問是不是同一問題

如果 informal：

$$
Q_I
$$

與 formal：

$$
Q_F
$$

不一致，

則所有後續 obstruction 都可能被污染。

## 39.2 Audit trigger

當：

- counterexample 異常容易；
- theorem vacuous；
- hypothesis 太強；
- repeated trivial proof；
- proof route 與 intended mathematics 不符；

應啟動：

$$
\operatorname{Audit}(Q_I,Q_F).
$$

## 39.3 這正是防止錯誤 confluence 的必要層

多個 agent 全在錯誤 formalization 上匯流，

只能證明：

$$
\text{they share a bad target}.
$$

---

# 40. Confluence confidence levels

## Level 0：文字相似

只有 lexical overlap。

## Level 1：概念相似

同 broad obstruction family。

## Level 2：route-level recurrence

normalized gap 類似，assumptions 部分對齊。

## Level 3：cross-route audited confluence

多 route 經人工／模型稽核確認同一 obstruction。

## Level 4：cross-basin independent confluence

不同 basin／方法／representation，genealogy correction 後仍匯流。

## Level 5：theorem-backed obstruction

存在形式 theorem 證明一整類 route 必須通過或無法越過該 obstruction。

只有 Level 5 接近真正的數學 no-go 結果。

---

# 41. Confluence 不是不可證性

## 41.1 核心防火牆

$$
\boxed{
C_{\mathrm{ind}}(O)\gg1
\not\Rightarrow
Q\text{ unprovable}.
}
$$

## 41.2 原因

真正 proof：

$$
r^\star
$$

可能根本沒有經過：

$$
O.
$$

即：

$$
r^\star\notin\mathcal R_{\mathrm{observed}}.
$$

## 41.3 也不能推出獨立性

Gödel independence 需要特定形式系統中的 metamathematical proof。

大量失敗不能替代這個證明。

---

# 42. Confluence 也不是問題錯了

## 42.1 Framing anomaly hypothesis

高 confluence 可以提高：

$$
\operatorname{Priority}(\text{framing audit}).
$$

但不能提高到 certainty。

## 42.2 更強證據鏈

若：

$$
C_{\mathrm{ind}}\uparrow
$$

再加：

$$
\text{formal counterexample},
$$

或：

$$
\text{semantic inconsistency},
$$

或：

$$
\text{reformulation theorem},
$$

才可能逐步建立 stronger diagnosis。

---

# 43. Confluence 與 productive mis-specification 的接口

後續 LSI-PSD-08 會研究：

$$
\text{productive mis-specification}.
$$

本文先指出：

> 即使 parent route 最後被證明 framing 有問題，其過程中發現的 obstruction、lemma、counterexample 與 repair mechanism 仍可能獨立有價值。

因此：

$$
\text{route invalidation}
\not\Rightarrow
\text{descendant knowledge invalidation}.
$$

這是後續系列的重要接口。

---

# 44. Failure atlas

## 44.1 為什麼需要 atlas

長程 AI 系統最容易遺失的不是成功 proof。

而是：

$$
\text{why previous routes failed}.
$$

## 44.2 Atlas schema

```yaml
problem_id:
obstruction_id:
canonical_gap:
assumptions:
first_seen:
last_seen:
route_count:
independent_route_mass:
method_families:
representations:
basins:
models:
premise_sets:
repairs:
escapes:
counterexamples:
formal_status:
semantic_status:
transfer_targets:
```

## 44.3 Atlas 是 research memory

它讓下一代 agent 不必從零開始。

---

# 45. Obstruction transfer

## 45.1 障礙也可以跨問題遷移

若：

$$
O_Q
$$

與另一問題：

$$
O_{Q'}
$$

具有共同 normalized mechanism，

則：

$$
O_Q
\rightarrow
O_{Q'}
$$

可能產生 transfer。

## 45.2 Transfer value

例如：

- same compactness gap；
- same counting bottleneck；
- same coercion bug；
- same representation singularity。

## 45.3 負知識也能成為 proof asset

所以 proof asset map 不應只收成功 lemma。

也應收：

$$
\boxed{
\text{portable obstruction patterns}.
}
$$

---

# 46. Obstruction compression

## 46.1 長程 corpus 會出現大量 failure variants

如果：

$$
10^4
$$

條失敗最後 quotient 成：

$$
17
$$

個 obstruction classes，

這本身就是研究壓縮。

## 46.2 Compression ratio

定義：

$$
\kappa_O
=
\frac{
N_{\mathrm{failure\ events}}
}{
N_{\mathrm{audited\ obstruction\ classes}}
}.
$$

## 46.3 高壓縮率

若：

$$
\kappa_O\gg1,
$$

表示大量生成其實反覆命中少數 failure geometry。

這正是 logic-space integration 的一個可測面向。

---

# 47. Obstruction discovery rate

## 47.1 新 obstruction 增量

令：

$$
U_O(N,W)
$$

為固定窗口新增 audited obstruction classes。

定義：

$$
\rho_O(N,W)
=
\frac{
U_O(N,W)
}{
A_O(N,W)
},
$$

其中 $A_O$ 是 failure events。

## 47.2 與 route novelty 一起看

若：

$$
\rho_{\mathrm{route}}\downarrow,
$$

且：

$$
\rho_O\downarrow,
$$

研究可能開始高度重採樣。

若 route novelty 高但 obstruction novelty 低，

表示：

> 新路很多，但都撞同一堵牆。

這是 confluence 最漂亮的訊號之一。

---

# 48. Route-to-obstruction matrix

令：

$$
M_{ij}
=
P(O_j\mid r_i).
$$

若 deterministic audited endpoint：

$$
M_{ij}\in\{0,1\}.
$$

實際研究可用 confidence：

$$
M_{ij}\in[0,1].
$$

矩陣：

$$
\mathbf M
$$

可用來做：

- route clustering；
- obstruction clustering；
- bipartite centrality；
- confluence detection；
- escape recommendation。

---

# 49. Obstruction-conditioned routing

## 49.1 過去的路由

通常：

$$
\pi(a\mid s).
$$

## 49.2 加入 obstruction memory

改成：

$$
\pi(
a
\mid
s,
O_{\mathrm{history}},
B,
R
).
$$

## 49.3 例子

如果：

$$
O^\star
$$

已被 20 條高度相依 route 命中，

不一定要停止。

但可以降低：

$$
P(\text{same family retry}).
$$

提高：

$$
P(\text{independent route probe}).
$$

---

# 50. Meta-controller

輸入：

$$
(
C_{\mathrm{ind}},
R_O,
Z(O),
H_O,
\rho_O,
\Gamma_{\mathrm{esc}}
).
$$

輸出：

$$
\{
\text{retry},
\text{repair},
\text{decompose},
\text{switch premise},
\text{switch representation},
\text{switch method},
\text{counterexample},
\text{framing audit},
\text{stop}
\}.
$$

這樣 obstruction 才真正變成控制訊號。

---

# 51. 實驗一：Obstruction Canonicalization Benchmark

## 51.1 資料

人工建立：

$$
500
$$

對 failure snippets。

標註：

- same obstruction；
- related but distinct；
- purely lexical；
- one resolves another；
- assumption mismatch。

## 51.2 指標

$$
\text{precision},
\text{recall},
F_1.
$$

## 51.3 最重要

寧願：

$$
\text{false negative}
$$

多一點，

也要避免：

$$
\text{false merge}.
$$

因為 false merge 會直接灌大 confluence。

---

# 52. 實驗二：Genealogy Correction

## 52.1 問題

raw confluence 是否被同源 route 複製灌水？

## 52.2 設計

對同一 obstruction：

$$
O
$$

建立：

- same-model variants；
- same-memory variants；
- independent-method variants；
- independent-representation variants。

## 52.3 比較

$$
C_{\mathrm{raw}}
$$

與：

$$
C_{\mathrm{ind}}.
$$

若兩者差異巨大，證明 genealogy correction 必要。

---

# 53. 實驗三：Escape-Confluence Test

對高：

$$
R_O
$$

obstruction，

執行：

1. method switch；
2. representation switch；
3. premise globalization；
4. resource escalation；
5. model-family switch；
6. counterexample search。

若多種 escape 都重新命中：

$$
O,
$$

則：

$$
C_{\mathrm{esc}}(O)\uparrow.
$$

這是比單 basin recurrence 更強的證據。

---

# 54. 實驗四：False-Confluence Calibration

## 54.1 故意製造 taxonomy 過粗

把所有：

> estimate failure

都合併成：

$$
O_{\mathrm{estimate}}.
$$

## 54.2 再細分 assumptions

重新抽取：

$$
A_i.
$$

## 54.3 比較

若：

$$
C_{\mathrm{raw}}
$$

大幅崩解，

說明原 confluence 只是 taxonomy artifact。

這是任何 serious observatory 必做的 calibration。

---

# 55. 實驗五：NS-203 Obstruction Audit

## 55.1 抽樣

優先：

- X72；
- DCRP；
- MORP；
- FCBP；
- C5-H；
- Proof Asset Map。

## 55.2 每篇抽取

$$
A,C,L,O,S.
$$

## 55.3 建立 gold obstruction pairs

至少：

$$
200
$$

對。

## 55.4 目標

測：

$$
C_B,
C_M,
C_L,
C_{\mathrm{ind}}.
$$

而不是只數：

> confluence 出現幾次。

---

# 56. 成熟系統如何回報「我卡住了」

不應只說：

> 我證不出來。

應回報：

```text
TARGET:
  Q-001

CURRENT BASIN:
  B-07

CURRENT OBSTRUCTION:
  O-031

OBSTRUCTION CONFIDENCE:
  Level 3 / cross-route audited

ROUTE SUPPORT:
  raw routes: 18
  independence-corrected mass: 4.2

ATTEMPTED ESCAPES:
  representation switch: neutral
  global premise retrieval: failed
  budget x4: neutral
  model-family switch: pending

NON-CLAIMS:
  not a proof of falsehood
  not a proof of unprovability
  not an independence result

RECOMMENDED NEXT ACTION:
  counterexample search
  theorem-level framing audit
```

這才是真正的 research-grade failure report。

---

# 57. 與 LSI-PSD-05 的整合

第 5 篇建立：

$$
B_i
$$

與：

$$
\text{local saturation}.
$$

本文把每個 basin 內的 terminal failure 抽成：

$$
O_j.
$$

於是 proof-space map 變成 bipartite structure：

$$
B_i
\leftrightarrow
O_j.
$$

一個 basin 可有多個 obstruction；

一個 obstruction 也可跨多個 basin。

因此：

$$
\boxed{
\text{basin map}
+
\text{obstruction map}
}
$$

比單純 route graph 更能描述長程研究。

---

# 58. 與 LSI-PSD-04 的整合

高階採樣不只作用於 route。

obstruction 本身也可有：

$$
O^{(0)},
O^{(1)},
O^{(2)},\ldots.
$$

例如：

$$
O^{(0)}
=
\text{local closure failure},
$$

$$
O^{(1)}
=
\text{different closures all require same missing relation},
$$

$$
O^{(2)}
=
\text{all relation-level repairs reintroduce same global defect}.
$$

所以：

$$
\boxed{
\text{higher-order proof sampling}
}
$$

與：

$$
\boxed{
\text{higher-order obstruction confluence}
}
$$

是同一研究動力的兩面。

---

# 59. 與 Logic-Space Integration 的整合

假設 failure events：

$$
F_N.
$$

經 quotient 後形成 obstruction classes：

$$
\mathcal O_N.
$$

可以把「失敗空間積分」定義成：

$$
I_O(N)
=
\int_{\Omega_O}
c_N([O])\,d\mu_O.
$$

真正重要的是：

$$
\Delta I_O(N).
$$

如果：

$$
\Delta I_O\rightarrow0
$$

但 failure count 持續上升，

表示研究正大量重採樣既有 obstruction space。

這就是：

$$
\boxed{
\text{obstruction-space saturation candidate}.
}
$$

仍然只是 observed regime 的性質。

---

# 60. 最重要的認識論防火牆

本文提出：

$$
\boxed{
\text{Obstruction Confluence Non-Verdict Principle}
}
$$

即：

$$
\boxed{
\text{high confluence}
\not\Rightarrow
\text{mathematical verdict}.
}
$$

具體包括：

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ false},
$$

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ unprovable},
$$

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ independent},
$$

$$
C_{\mathrm{ind}}\uparrow
\not\Rightarrow
Q\text{ misframed}.
$$

它只支持：

$$
\boxed{
\text{the observed research regime repeatedly reconstructs the same audited barrier}.
}
$$

---

# 61. 非主張總表

本文不主張：

1. 所有 proof failure 都能 canonicalize 成唯一 obstruction；
2. obstruction graph 是數學實在的唯一真結構；
3. route count 可直接當獨立證據；
4. 不同模型就是獨立路線；
5. 不同符號就是不同 representation；
6. 高 confluence 等於不可證；
7. 高 confluence 等於命題為假；
8. 高 confluence 等於定義範疇錯誤；
9. empirical no-go candidate 等於 theorem-level no-go；
10. formal proof success 自動保證 informal target fidelity；
11. compiler diagnostic 自動等於數學 diagnosis；
12. NS-203 已發現 Navier--Stokes 的終極 obstruction；
13. P/NP 或其他未解問題可由 AI 失敗頻率判定；
14. obstruction 越多代表研究越差；
15. obstruction 越少代表更接近真理。

---

# 62. 形式命題總表

## 命題 1：Failure-to-obstruction separation

$$
\boxed{
e_i=e_j
\not\Rightarrow
O_i=O_j.
}
$$

## 命題 2：Text-to-obstruction separation

$$
\boxed{
\operatorname{TextSim}(e_i,e_j)\uparrow
\not\Rightarrow
O_i\equiv O_j.
}
$$

## 命題 3：Route-count non-independence

$$
\boxed{
C_{\mathrm{raw}}(O)
\not\Rightarrow
C_{\mathrm{ind}}(O).
}
$$

## 命題 4：Cross-route confluence evidence

在 assumptions、target fidelity 與 obstruction equivalence 都經 audit 後，

若：

$$
C_{\mathrm{ind}}(O)\uparrow,
$$

則對：

$$
\text{observed barrier robustness}
$$

的證據增加。

## 命題 5：Confluence non-verdict

$$
\boxed{
C_{\mathrm{ind}}(O)\uparrow
\not\Rightarrow
\operatorname{Verdict}(Q).
}
$$

## 命題 6：Obstruction memory utility

若 canonical obstruction memory 能降低相同 route family 的無效重訪，

則它可提高：

$$
\text{research efficiency}.
$$

此命題可實驗檢驗。

---

# 63. 與後續第 7 篇的接口

前六篇逐步建立：

$$
\text{search regime},
$$

$$
\text{coverage},
$$

$$
\text{semantic quotient},
$$

$$
\text{higher-order sampling},
$$

$$
\text{local saturation},
$$

$$
\text{obstruction confluence}.
$$

接下來第 7 篇會問一個更反直覺的問題：

> 當研究空間被約束、壓縮與閉合後，為什麼核心真命題反而可能變得越來越像「廢話」？

也就是：

$$
\boxed{
\text{Truth--Generativity Inversion}.
}
$$

而本文提供必要前置：

> 在討論「真理變簡單」以前，我們必須先知道研究究竟是在收斂到穩健 obstruction，還是只被自己的 route genealogy 困住。

---

# 64. 結論

長程 AI 數學研究真正昂貴的，不只是證明。

也是：

$$
\boxed{
\text{忘記自己為什麼失敗。}
}
$$

如果每次 failure 都只留下：

> 沒證出來。

下一個 agent 就會重新從零開始。

如果每個 failure 都被壓成一個過粗標籤：

> closure gap。

系統又會產生假的 confluence。

因此 mature research infrastructure 必須保存：

$$
\text{where},
$$

$$
\text{under what assumptions},
$$

$$
\text{by which route},
$$

$$
\text{after which premises},
$$

$$
\text{with which representation},
$$

$$
\text{what exactly remained unclosed}.
$$

只有這時：

$$
r_1\rightarrow O,
\qquad
r_2\rightarrow O,
\qquad
r_3\rightarrow O
$$

才真正具有科學資訊。

最終，本文把「失敗」從一句負面結果改寫成一個可積累結構：

$$
\boxed{
\text{failure event}
\rightarrow
\text{canonical obstruction}
\rightarrow
\text{confluence evidence}
\rightarrow
\text{routing decision}.
}
$$

而整篇論文最重要的兩句話是：

$$
\boxed{
\textbf{A wall becomes informative only when we can show that independent roads truly meet the same wall.}
}
$$

以及：

$$
\boxed{
\textbf{Even then, the wall is evidence about our explored routes, not a verdict on all possible mathematics.}
}
$$

---

# 參考文獻

1. Wang, E., Chess, S., Lee, D., Ge, S., Mallavarapu, A., & Ilin, V. (2026). **Learning to Repair Lean Proofs from Compiler Feedback.** arXiv:2602.02990. https://arxiv.org/abs/2602.02990

2. Qiu, R., Cao, Y., Liu, J., Guo, D., Gao, X.-S., Zhi, L., & Feng, R. (2026). **Mechanic: Sorrifier-Driven Formal Decomposition Workflow for Automated Theorem Proving.** arXiv:2603.24465. https://arxiv.org/abs/2603.24465

3. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468. https://arxiv.org/abs/2606.06468

4. Zhang, Y., Sun, Y., Suzuki, T., Lee, J. D., & Liu, F. (2026). **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** arXiv:2606.05400. https://arxiv.org/abs/2606.05400

5. Ammanamanchi, P. S., Bhat, S., & Biderman, S. (2026). **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.** arXiv:2606.29493. https://arxiv.org/abs/2606.29493

6. Lau, G. R. (2026). **Using Aristotle API for AI-Assisted Theorem Proving in Lean 4: A Formalisation Case Study of the Grasshopper Problem.** arXiv:2605.20120. https://arxiv.org/abs/2605.20120

7. Gao, G. et al. (2026). **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137. https://arxiv.org/abs/2605.13137

8. George, R. J., Huang, S., Song, P., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925. https://arxiv.org/abs/2502.17925

9. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 目標問題／定理 |
| $r$ | proof / research route |
| $e$ | 單次 failure event |
| $O$ | canonical obstruction |
| $\mathcal R(O)$ | 命中 $O$ 的 route 集合 |
| $C_{\mathrm{raw}}(O)$ | 原始 confluence count |
| $C_{\mathrm{ind}}(O)$ | genealogy-corrected confluence |
| $C_B(O)$ | basin confluence |
| $C_M(O)$ | method-family confluence |
| $C_L(O)$ | representation confluence |
| $C_{\mathrm{esc}}(O)$ | escape-action confluence |
| $R_O$ | obstruction robustness |
| $Z(O)$ | obstruction centrality |
| $H_O$ | obstruction entropy |
| $\rho_O$ | obstruction discovery rate |
| $\kappa_O$ | failure-event / obstruction-class compression ratio |
| $F_T$ | target fidelity status |

---

## 附錄 B：Obstruction Record 最小欄位

```yaml
obstruction_id:
problem_id:
domain:
formal_target:
informal_target:
target_fidelity:
assumptions:
normalized_gap:
mechanism:
first_seen:
last_seen:
route_ids:
route_genealogy:
method_families:
representations:
premise_sets:
basins:
models:
raw_confluence:
independent_confluence:
escape_attempts:
repair_history:
counterexample_status:
audit_status:
no_go_status:
nonclaims:
```

---

## 附錄 C：Confluence Audit Checklist

- [ ] obstruction assumptions 已 normalize
- [ ] target statement 版本一致
- [ ] formal / informal target faithfulness 已檢查
- [ ] lexical similarity 沒有被當 semantic equivalence
- [ ] route genealogy 已建立
- [ ] shared memory 已計入依賴
- [ ] shared premise 已計入依賴
- [ ] representation difference 不是單純 rename
- [ ] method-family difference 已人工抽查
- [ ] raw count 與 independence-corrected count 同時報告
- [ ] empirical no-go 沒有冒充 theorem no-go
- [ ] confluence 沒有冒充 falsehood / unprovability / independence
- [ ] escape history 已保留
- [ ] resolved obstruction 沒有繼續計入 active barrier

---

## 附錄 D：一句話版本

$$
\boxed{
\text{十條路都撞牆，不代表世界沒有第十一條路；但若十條真正獨立的路都撞同一面牆，那面牆值得被單獨研究。}
}
$$
