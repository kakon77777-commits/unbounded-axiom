# 可重放判斷與語義等價：從 Event Sourcing 到 Replay Verification
## 動態邏輯解與生成判斷系列・第十篇

**英文題名：** *Replayable Judgment and Semantic Equivalence: From Event Sourcing to Replay Verification*  
**版本：** v0.1  
**日期：** 2026-08-16  
**作者：** Neo.K／Aletheia

---

## 摘要

如果一個判斷系統只保存「現在狀態」，那麼所謂動態邏輯仍然只是會變的資料庫。要讓判斷真正成為可研究、可驗證、可審核的運行歷史，系統必須回答：

> 給定同一初始狀態與同一事件歷史，我是否能重建同一個判斷狀態？

本文以 Event Sourcing 作為工程模式，但不把它當作新的邏輯定理。Event Sourcing 的核心思想是把狀態變化保存為 append-oriented event history，再由 reducer/projector 重建 current state。這與生成判斷天然相容。

本文定義：

$$
S_n
=
\operatorname{Fold}
(
S_0,
e_1,\ldots,e_n;
R_v
),
$$

其中 $R_v$ 為 reducer version。

第一層 Replay Correctness 要求：

$$
\boxed{
\operatorname{Replay}
(
S_0,\mathcal H,R_v
)
=
S_n.
}
$$

然而 AI 系統加入 stochastic model 後，bitwise replay 不一定合理。因此本文再區分：

1. deterministic replay；
2. committed-output replay；
3. semantic re-evaluation。

並提出：

$$
\boxed{
\text{Replay}
\neq
\text{Rejudge}.
}
$$

Replay 重建歷史當時已提交的狀態；Rejudge 則用新模型重新解讀相同證據。

這個區分是 Live Paper、ACO、長期 AI 科學與責任審核能否成立的關鍵。

---

# 一、只保存 Current State 不夠

假設目前：

$$
J(P,t_n)=F_p.
$$

若只保存：

```text
state = provisionally_false
```

我們不知道：

- 曾經是否支持；
- 哪個證據造成反轉；
- 哪個模型做出判斷；
- 是否有資料被刪除；
- 是否發生過人工 override。

---

# 二、事件歷史

定義：

$$
\mathcal H_n
=
(
e_1,e_2,\ldots,e_n
).
$$

Current state：

$$
S_n
$$

由：

$$
S_n
=
\operatorname{Fold}
(
S_0,\mathcal H_n
)
$$

生成。

---

# 三、Reducer

Reducer：

$$
R_v(S,e)
\rightarrow
S'.
$$

版本：

$$
v
$$

必須保存。

因：

$$
R_1
\neq
R_2
$$

可能對同一 event history 得到不同 state。

---

# 四、Deterministic Replay

若 reducer deterministic：

$$
R_v(S,e)
$$

對同一輸入唯一，

則：

$$
\operatorname{Replay}
(
S_0,\mathcal H,R_v
)
$$

應 bitwise 或 canonical-structure 等價。

---

# 五、Committed Output

LLM call：

$$
M(prompt)
$$

通常 stochastic。

因此不能在 replay 時重新呼叫：

$$
M
$$

期待得到相同 token。

正確做法是將當時接受的輸出：

$$
O_i
$$

提交成 event payload。

Replay 讀：

$$
O_i.
$$

---

# 六、模型呼叫事件

例如：

```json
{
  "type": "MODEL_OUTPUT_COMMITTED",
  "model": "model-x",
  "prompt_hash": "...",
  "output_hash": "...",
  "committed_output": {}
}
```

Replay 不重新生成。

---

# 七、Rejudge 是另一條 lineage

若 2030 年想用：

$$
M_{2030}
$$

重新分析 2026 evidence，

應：

$$
\operatorname{Rejudge}
(
E_{2026},
M_{2030}
)
\rightarrow
J_{2030}^{new}.
$$

而不是把：

$$
J_{2026}
$$

覆蓋。

---

# 八、兩條歷史

可以有：

$$
L_E
=
\text{Evidence Log},
$$

$$
L_B
=
\text{Belief/Judgment Lineage}.
$$

Evidence log 應盡量 immutable。

Judgment lineage 可以多分支。

---

# 九、2026 Agent Research 的新趨勢

近年的 agent 架構研究已開始明確使用 event sourcing，把 stochastic agent intention 與 deterministic state mutation 分離；也開始提出 evidence log 與 evolving belief lineage 分離的 epistemic replication 思路。

本文不依賴這些新工作才能成立，但它們顯示：

$$
\boxed{
\text{append-only evidence history}
+
\text{versioned belief lineage}
}
$$

正成為 AI agent 長程可驗證性的自然架構方向。

---

# 十、Replay Verification

驗證至少包含：

$$
h(\mathcal H)
$$

event log hash。

$$
h(R_v)
$$

reducer version hash。

$$
h(S_n)
$$

current state hash。

Replay 後：

$$
h(\widehat S_n)
=
h(S_n).
$$

---

# 十一、Semantic Equivalence

有些 state 含：

- key ordering；
- timestamps；
- volatile ids；
- model prose。

bitwise equality 太強。

可定義 canonical projection：

$$
C(S).
$$

要求：

$$
\boxed{
C(\widehat S_n)
=
C(S_n).
}
$$

---

# 十二、語義等價邊界

但不能濫用：

> 意思差不多。

Semantic equivalence 必須有 contract。

例如只忽略：

- JSON key order；
- UI-only timestamp；
- display formatting。

不能忽略：

- judgment state；
- evidence cursor；
- source set；
- responsibility debt。

---

# 十三、Replay Contract

```yaml
replay_contract:
  compare:
    - judgment_state
    - evidence_cursor
    - claim_graph_hash
    - responsibility_ledger_hash
  ignore:
    - render_timestamp
    - ui_expansion_state
```

---

# 十四、Event Ordering

若：

$$
e_i,e_j
$$

不可交換，

則 event order 必須固定。

若：

$$
e_i\circ e_j
=
e_j\circ e_i,
$$

才可允許 reorder。

因此 event log 本質上也包含因果排序。

---

# 十五、Concurrency

多 Agent 同時寫入時：

$$
e_i\parallel e_j.
$$

第一版可採：

- monotonic sequence id；
- single commit log；
- optimistic concurrency check。

避免不同 agent 各有自己的「現在」。

---

# 十六、Snapshot

當：

$$
|\mathcal H|
$$

非常大，

可建立：

$$
S_k
$$

snapshot。

之後：

$$
S_n
=
\operatorname{Fold}
(
S_k,
e_{k+1},\ldots,e_n
).
$$

但 snapshot 不能取代原 event history 的 archival value。

---

# 十七、Ledger Tamper Detection

對高要求研究，可以建立 hash chain：

$$
h_i
=
H(
h_{i-1},
e_i
).
$$

若中間事件被修改：

$$
h_n
$$

會改變。

這不是區塊鏈必要論證。

普通 hash chain 已足以增加 tamper evidence。

---

# 十八、Replay 與責任

如果某 Agent 說：

> 我當時不是這樣判。

Replay 可以回到：

$$
S_t
$$

並顯示：

- evidence；
- policy；
- model output；
- action；
- approval。

責任因此從記憶爭議轉成可檢查歷史。

---

# 十九、Replay 與論文

Live Paper 的 PDF：

$$
D_{snapshot}
$$

可以指向：

$$
event\_cursor=n.
$$

未來讀者可 replay 至：

$$
n.
$$

看到當時真正狀態。

---

# 二十、Replay 與科學

如果論文結論後來改變，

不需要把舊論文當「垃圾」。

而可以：

$$
J_{2026}
\rightarrow
J_{2027}
\rightarrow
J_{2030}.
$$

研究史本身成為資料。

---

# 二十一、Replay 與 ACO

異常因果案例特別需要：

$$
\text{Raw Evidence}
\neq
\text{AI Interpretation}.
$$

Evidence log 可保存原始資料。

每代模型產生不同 Judgment lineage。

因此：

$$
\boxed{
\text{同一世界證據，
可以被未來更強模型重新判讀，
但不能讓未來模型改寫過去證據。}
}
$$

---

# 二十二、Replay Correctness Proposition

若：

1. $S_0$ 相同；
2. event sequence 相同；
3. reducer version 相同；
4. 所有非決定輸出均以 committed payload 保存；
5. canonicalization contract 相同；

則：

$$
\boxed{
C(
\operatorname{Replay}_1
)
=
C(
\operatorname{Replay}_2
).
}
$$

這是本系列第一個非常適合直接寫成自動測試的形式命題。

---

# 二十三、Replay 與動態不動點

狀態內容：

$$
S_t
$$

一直變。

但 replay invariant：

$$
\mathcal I_R
$$

保持：

> 同一歷史必須能重建同一 canonical state。

因此 replay correctness 本身就是一種工程動態不動點。

---

# 二十四、結論

從這一篇開始，「判斷具有歷史」不再只是哲學敘述。

它得到一個明確工程判準：

$$
\boxed{
\text{同一歷史，必須可以重建同一可比較狀態。}
}
$$

同時：

$$
\boxed{
\text{Replay}
\neq
\text{Rejudge}.
}
$$

前者保存歷史真實性，後者允許知識進步。

兩者同時存在，才是真正的動態知識系統。

---

# 參考文獻

1. Doyle, J. “A Truth Maintenance System.” *Artificial Intelligence*, 12(3), 1979, 231–272. DOI: 10.1016/0004-3702(79)90008-0.
2. Fischer, M. J., & Ladner, R. E. “Propositional Dynamic Logic of Regular Programs.” *Journal of Computer and System Sciences*, 18(2), 1979.
3. Alchourrón, C. E., Gärdenfors, P., & Makinson, D. “On the Logic of Theory Change.” *Journal of Symbolic Logic*, 50(2), 1985.
4. Brito dos Santos Filho, E. “ESAA: Event Sourcing for Autonomous Agents in LLM-Based Software Engineering.” arXiv:2602.23193, 2026.（新近預印本，視為工程參考而非既定共識）
5. He, J., & Yu, D. “Replicating Belief, Not Bits: Epistemic State Replication for Agentic Systems.” arXiv:2607.09748, 2026.（新近預印本，視為工程參考而非既定共識）
