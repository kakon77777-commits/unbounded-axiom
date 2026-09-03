# CODT-05
# 認知域不是固定分類：Flow-Atlas Separation
## Cognitive Domains Are Not Static Classes: Flow-Atlas Separation

**系列：** Cognitive Operator-Domain Theory, CODT / 認知算子-域理論  
**系列篇次：** 05 / 10  
**版本：** v1.0  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  
**文件性質：** 理論論文 / Dynamic Domain Geometry 篇  
**前篇：** CODT-04〈共享底層認知域：Shared-Bottom Cognitive Runtime〉

---

## 摘要

CODT-03 將認知域定義為由合法 operator ecology、history、boundary、failure、prediction、compression 與 stability 後生的 operational region；CODT-04 進一步指出，Attention、Search、Generation、Representation、Belief、Decision、Planning、Meta-Observation 等 shared-bottom substrate 會跨越多個方法與候選域運作，因此 transition graph 中的大量跨域流動不一定表示 domain boundary 不存在，也可能只是共享 infrastructure traffic。

本文提出 **Flow-Atlas Separation**：認知 runtime 中的 operator transition flow 與 domain atlas 是兩種不同但耦合的結構。

令 fast transition flow 為：

$$
\boxed{
P_t
=
P(
U_{t+1}
\mid
U_t,
S_t,
H_t,
B_t,
R_t
)
}
$$

令 derived atlas 為：

$$
\boxed{
\mathcal A_t
=
Chart(
\mathcal U,
\Lambda,
H_{\le t},
\mathcal E_t
)
}
$$

其中 $\mathcal E_t$ 表示用於 atlas selection 的 evidence。本文主張：

$$
\boxed{
P_t
\neq
\mathcal A_t.
}
$$

runtime regime 可以先改變 transition law，而不必立即重畫 domain chart；同樣地，兩張 assignment 的差異很大，也不代表新的 partition 具有功能價值。Domainization Experimental Foundations 的關鍵 ablation 顯示，在 OOD artifact stress 中，normal/stress chart assignment 的 ARI 曾下降到約 $0.0411$，但 predictive recovery 幾乎全部來自 transition-parameter adaptation：

$$
\Delta_P
=
1.4804
\text{ bits/transition},
$$

而 repartition 的獨立 gain 反而為：

$$
\Delta_A
=
-0.0434.
$$

三個完整 seeds 亦得到負的 OOD partition gain。這迫使早期「dynamic domain attractor」強版本被修正為：

$$
\boxed{
\text{Quasi-Stable Atlas over Adaptive Operator Flow}.
}
$$

本文進一步吸收 MDL experiments：若 atlas switching 所節省的 future code length 無法支付新 chart 的 description cost，則即使 stress-specific chart 看起來完全不同，也不應切換 atlas。由此提出 **Atlas Switch Gate**：

$$
\boxed{
NetSwitchGain
=
FlowAdjustedGain
-
ChartSwitchCost.
}
$$

只有：

$$
NetSwitchGain>0
$$

且 stability / legality / boundary evidence 同時成立，repartition 才具有實質支持。

本文最後把 operator traffic 分成 domain-internal flow、cross-domain bridge flow、shared-bottom infrastructure flow、meta-control flow 與 world-boundary flow，並提出 typed flow decomposition。這使 CODT 能避免把所有高流量 hub 誤當成 domain core，也避免把 regime-specific transition shock 誤當成 domain ontology 的即時崩解。本文將 domain 重新表述為：**承載 adaptive flow 的準穩定局部 chart，而非固定分類，也非每一時刻都重新聚類的動態盒子。**

---

## 關鍵詞

Flow-Atlas Separation；CODT；cognitive atlas；operator flow；dynamic domains；regime shift；MDL；transition model；shared-bottom infrastructure；community dynamics；cognitive geometry

---

# 1. 問題：我們看到的是「域」，還是「流」？

假設一個 cognitive runtime 中存在大量 transitions：

$$
U_i
\rightarrow
U_j.
$$

我們可以把 operator 當成 nodes，把 transitions 當成 weighted edges。

接著很自然地做 clustering。

如果某些 operators 彼此 transition 很頻繁，我們可能說：

> 這是一個 domain。

但這個推論太快。

因為 transition 高可能有至少五種原因：

1. 它們真的位於同一 operational region；
2. 它們共享一個 high-traffic infrastructure；
3. 它們透過 bridge operator 反覆跨域；
4. meta-control 在它們之間頻繁 routing；
5. world-boundary loop 強迫某些 operators 形成高流量閉環。

因此：

$$
\boxed{
HighTransitionFlow
\not\Rightarrow
SameDomain.
}
$$

反過來，兩個 operators transition 很少，也不代表它們不屬於同一 domain。

它們可能只是 domain 內不同 subroutines、不同時間尺度或低頻 specialization。

所以 CODT-05 的第一個問題是：

> 如何把「當下怎麼走」和「哪些區域值得被當成穩定結構」分開？

---

# 2. Flow 與 Atlas 的第一個形式化

令：

$$
U_t
$$

為時間 $t$ 的 active cognitive operator。

令：

$$
S_t
$$

為 runtime state。

令：

$$
H_t
$$

為 history。

令：

$$
B_t
$$

為 resource state。

令：

$$
R_t
$$

為 runtime regime。

則 transition flow：

$$
\boxed{
P_t
=
P(
U_{t+1}
\mid
U_t,
S_t,
H_t,
B_t,
R_t
).
}
$$

這個物件回答：

> 在目前條件下，下一個 operator 怎麼走？

另一方面，atlas：

$$
\boxed{
\mathcal A_t
=
Chart(
\mathcal U,
\Lambda,
H_{\le t},
\mathcal E_t
).
}
$$

它回答：

> 哪些 operators / words / boundaries / failures 在累積 evidence 下值得被壓縮成較穩定的 operational regions？

因此：

$$
\boxed{
P_t
\neq
\mathcal A_t.
}
$$

Flow 是動力。

Atlas 是 derived geometry / control chart。

---

# 3. 為什麼 Atlas 不能等同 Transition Matrix

如果：

$$
\mathcal A_t
=
P_t,
$$

則每次 transition probability 改變，都等於 domain ontology 改變。

這會產生荒謬結果。

例如同一個 Planning domain 在 deadline 壓力下，Search 到 Decision transition 可能變快。

但這不代表 Planning domain 已經不存在。

又例如 resource shock 可能提高：

$$
Defer,
Prune,
Abort,
Replan
$$

的 transition probability。

這更可能表示：

$$
\boxed{
\text{same structural region under different flow field}.
}
$$

因此 domain geometry 不應直接被瞬時 transition matrix 取代。

---

# 4. 為什麼 Flow 也不能忽略 Atlas

反過來，若 atlas 被固定成一張永遠不變的 taxonomy，也會出問題。

因為 runtime evidence 可能長期顯示：

- 某些 old domain boundary 沒有 predictive value；
- 某些 operators 反覆形成新 niche；
- 某些 seeds 持續被跨域 program 打散；
- 某些 failure boundary 發生穩定分裂；
- 某些 shared-bottom family 出現 domain-like closure。

因此：

$$
\boxed{
Atlas
\neq
ImmutableTaxonomy.
}
$$

Flow 可以提供 atlas revision pressure。

但：

$$
\boxed{
RevisionPressure
\neq
ImmediateRepartition.
}
$$

---

# 5. 兩個時間尺度

Phase 0.6 的 synthetic experiments 提出一個候選 timescale separation：

$$
\boxed{
\tau_P
<
\tau_{\mathcal A}.
}
$$

其中：

- $\tau_P$：transition flow 適應時間；
- $\tau_{\mathcal A}$：有功能價值的 atlas 重構時間。

這不是 universal cognitive law。

它表示目前 evidence 更支持：

> transition law 可以比值得付成本的 domain repartition 更快改變。

因此：

$$
\boxed{
\text{Fast Flow}
+
\text{Slow Chart}
}
$$

成為本文的第一版 dynamic domain hypothesis。

---

# 6. Quasi-Stable Atlas

本文將一個 domain candidate 暫時寫成：

$$
\boxed{
\mathfrak D_\alpha(t)
=
\text{quasi-stable local chart carrying regime-conditioned flow}.
}
$$

「quasi-stable」不是 static。

它表示：

- membership 可以改；
- boundary 可以漂移；
- niche 可以 split / merge；
- version 可以更新；

但這些變化不應只由 instantaneous transition noise 觸發。

因此：

$$
\boxed{
\text{QuasiStable}
\neq
\text{Immutable}.
}
$$

---

# 7. 早期 Dynamic Attractor 強版本

Phase 0.5 曾因 normal chart 與 stress chart assignment 差異明顯，提出：

$$
\mathfrak D_\alpha
=
\mathfrak D_\alpha(
t,
C,
O,
B,
R
).
$$

其中 $R$ 代表 regime。

當時 normal/stress chart 的 ARI 約：

$$
0.3231.
$$

而 regime-matched chart 在自己的 regime 中有更好的 predictive performance。

這很容易導向：

$$
\boxed{
\text{Domain = dynamic attractor}.
}
$$

也就是每當 regime 變化，domain geometry 就重組。

這個猜想後來被 Phase 0.6 修正。

---

# 8. 為什麼 Phase 0.5 的證據不夠

Phase 0.5 的 adaptation 同時改變兩件事：

1. chart assignment；
2. transition statistics。

若 predictive loss 下降，我們無法知道：

> 是因為換了 domain geometry？

還是：

> 只是因為重新估計了 transition probabilities？

所以：

$$
\boxed{
\text{Total Adaptation Gain}
\neq
\text{Partition Gain}.
}
$$

必須做 ablation。

---

# 9. 四格 Ablation

令 $A_N$ 為 normal atlas， $A_S$ 為 stress atlas， $P_N$ 為 normal flow model， $P_S$ 為 stress flow model。

定義四個 coding condition：

$$
NN
=
L(
H
\mid
A_N,
P_N
),
$$

$$
NS
=
L(
H
\mid
A_N,
P_S
),
$$

$$
SN
=
L(
H
\mid
A_S,
P_N
),
$$

$$
SS
=
L(
H
\mid
A_S,
P_S
).
$$

則 parameter adaptation gain：

$$
\boxed{
\Delta_P
=
NN-NS.
}
$$

partition adaptation gain：

$$
\boxed{
\Delta_A
=
NS-SS.
}
$$

正值表示該 adaptation 降低 code length。

負值表示反而變差。

---

# 10. OOD Artifact：最重要的反證

OOD artifact stress 是 Flow-Atlas Separation 的關鍵案例。

normal/stress independently learned assignment：

$$
\boxed{
ARI
=
0.0411.
}
$$

幾乎完全不同。

如果只看 ARI，可以很容易說：

> domain geometry 發生相變。

但 ablation：

$$
\boxed{
\Delta_P
=
1.4804
}
$$

bits/transition，

而：

$$
\boxed{
\Delta_A
=
-0.0434.
}
$$

也就是：

> 幾乎全部 predictive recovery 都來自 flow parameter update；換 stress partition 在同一 stress flow 下反而稍微更差。

三個完整 seeds：

$$
E[
\Delta_P^{OOD}
]
=
1.3992,
$$

$$
E[
\Delta_A^{OOD}
]
=
-0.0251.
$$

且 OOD partition gain：

$$
\boxed{
3/3
\text{ 為負}.
}
$$

因此：

$$
\boxed{
ARI\text{ collapse}
\not\Rightarrow
UsefulRepartition.
}
$$

這是 CODT-05 最重要的 empirical foundation。

---

# 11. Assignment Shift 與 Functional Shift 必須分開

一張 chart assignment 變很多，可以有多種原因：

- clustering instability；
- sparse OOD edges；
- changed edge weights；
- resolution effect；
- changed flow statistics；
- true structural boundary shift。

所以：

$$
\boxed{
AssignmentShift
\neq
FunctionalDomainShift.
}
$$

Functional domain shift 至少還需要證明：

> 在控制 flow parameter adaptation 後，新 atlas 本身仍增加 held-out predictive / compressive / operational value。

---

# 12. Mixed Stress 的教訓

Mixed stress 曾有正 total adaptation gain。

但 partition gain仍為負。

因此：

$$
\boxed{
\text{better adapted runtime}
\not\Rightarrow
\text{better repartition}.
}
$$

這說明「適應」這個詞也必須拆開。

可能是：

- parameter adaptation；
- policy adaptation；
- resource adaptation；
- representation adaptation；
- atlas adaptation。

CODT 不允許全部叫「domain adaptation」。

---

# 13. Online Atlas 的進一步結果

Phase 0.6 online experiment 讓 runtime 經過多個 sequential windows：

$$
normal
\rightarrow
stress
\rightarrow
recovery
\rightarrow
normal.
$$

主 run：

$$
\Delta_{online}
=
0.1484.
$$

但拆開：

$$
\boxed{
\Delta_{parameter}
=
0.1416,
}
$$

$$
\boxed{
\Delta_{partition}
=
0.0068.
}
$$

也就是主 run 的大部分 online improvement 來自 transition statistics adaptation。

三個完整 seeds 平均：

$$
E[
\Delta_{online}
]
=
0.3196,
$$

$$
E[
\Delta_{parameter}
]
=
0.2389,
$$

$$
E[
\Delta_{partition}
]
=
0.0807.
$$

partition adaptation 不是零。

但目前證據更支持：

$$
\boxed{
\text{flow adaptation is faster and usually larger}.
}
$$

---

# 14. Flow-Atlas Separation 的正式候選

因此本文提出：

$$
\boxed{
CognitiveRuntime_t
=
(
U_t,
S_t,
P_t,
\mathcal A_t,
H_t
).
}
$$

其中 $P_t$ 是 adaptive flow， $\mathcal A_t$ 是 quasi-stable chart。

Flow 可以依：

$$
R_t,
B_t,
Goal_t,
Failure_t,
WorldPresentation_t
$$

快速調整。

Atlas 只在累積 evidence 足夠時更新。

---

# 15. Shared-Bottom Infrastructure 會扭曲 Flow

CODT-04 已建立：

$$
Method
\neq
Domain
\neq
SharedBottom.
$$

這對 transition graph 有直接後果。

Attention、Search、Representation、Meta-Control 等 high-reuse substrate 會自然形成高流量 hubs。

因此若直接用 raw transition graph clustering：

$$
HighDegree(U)
$$

很可能只是：

$$
\boxed{
InfrastructureRole(U)
}
$$

而不是：

$$
DomainCore(U).
$$

---

# 16. Typed Flow Decomposition

本文因此提出：

$$
\boxed{
F_t
=
F_t^{D}
+
F_t^{B}
+
F_t^{SB}
+
F_t^{M}
+
F_t^{W}.
}
$$

其中：

- $F_t^{D}$：domain-internal flow；
- $F_t^{B}$：cross-domain bridge flow；
- $F_t^{SB}$：shared-bottom infrastructure flow；
- $F_t^{M}$：meta-control / routing flow；
- $F_t^{W}$：world-boundary flow。

這不是一般數值上的唯一可加分解。

它是一個 typed flow ledger candidate。

一個 transition event 應盡量被標記其 flow role。

---

# 17. Domain-Internal Flow

若 $U_t,U_{t+1}$ 在同一 domain candidate 中有高 membership，且 transition 不需要 domain bridge，則可標為：

$$
F_t^{D}.
$$

但 overlapping domains 會造成 ambiguity。

因此 FlowRole 也可以是 soft / multi-label。

---

# 18. Cross-Domain Bridge Flow

若：

$$
U_t
\in
\mathfrak D_\alpha
$$

而：

$$
U_{t+1}
\in
\mathfrak D_\beta
$$

並經顯式 bridge：

$$
B_{\alpha\beta},
$$

則 $F_t^{B}$ 記錄：

- source；
- destination；
- representation conversion；
- license change；
- resource cost；
- loss；
- certificate。

因此跨域 flow 不等於 domain boundary failure。

它可以是合法 infrastructure。

---

# 19. Shared-Bottom Infrastructure Flow

如果 ATT、SRH、REP、MET 等 substrate 被多個 domains 共用，它們的 traffic 應標為：

$$
F_t^{SB}.
$$

這允許 atlas learner 在分析 domain geometry 時：

- 保留 infrastructure；
- 降權 infrastructure；
- 分層建模 infrastructure；
- 或建立 multilayer chart。

不必把它們強迫塞進某一個 domain。

---

# 20. Meta-Control Flow

CRE 類 router、MET monitoring、DEC/PLN control signal 可能形成：

$$
F_t^{M}.
$$

Meta-control traffic 的高頻往返：

$$
Monitor
\rightarrow
Route
\rightarrow
Monitor
$$

不應自動被理解成一個巨大 meta-domain。

它可能只是 control plane。

---

# 21. World-Boundary Flow

ACT 到 CWB，再到 World transition，再回 Presentation 的 loop：

$$
ACT_{request}
\rightarrow
CWB
\rightarrow
World
\rightarrow
Presentation
$$

是一種特殊 flow：

$$
F_t^{W}.
$$

它跨越 cognition / World ontology boundary。

因此絕不能因為 edge weight 高，就把 WorldOperator 吸入 Cognitive Domain Atlas。

---

# 22. Flow Role 與 Domain Membership 是不同 metadata

對 transition：

$$
e_t
=
(
U_t,
U_{t+1}
),
$$

可以同時有：

$$
DomainMembership(U_t),
$$

$$
DomainMembership(U_{t+1}),
$$

以及：

$$
FlowRole(e_t).
$$

所以：

$$
\boxed{
NodeDomain
\neq
EdgeRole.
}
$$

這是 CODT 動態圖表示的重要分離。

---

# 23. 為什麼 Flow-Based Community Detection 仍然有價值

Rosvall 與 Bergstrom 的 map equation 使用 random-walk probability flow 來尋找可以壓縮 flow description 的 modules。

這提供 CODT 一個重要外部參照：

> 一張 map 可以因為它壓縮動態 flow 而有價值。

Delvenne、Yaliraki、Barahona 的 Markov stability 則把 partition quality 和 dynamics / time scale 連結，顯示不同 flow time scales 可以支持不同有效 partitions。

CODT 吸收：

$$
\boxed{
\text{flow can reveal useful mesoscopic structure}.
}
$$

但不吸收：

$$
\boxed{
\text{flow module = cognitive domain}.
}
$$

因為 cognition 還有 legality、license、shared-bottom、World boundary、failure 與 history。

---

# 24. Multi-Time-Scale Chart

外部 Markov stability 類研究提醒：

同一 graph 在不同 dynamics time scale 下可以有不同 partition resolution。

CODT 可以類比定義：

$$
\mathcal A_t^{(\tau)}.
$$

其中 $\tau$ 是 analysis / prediction horizon。

短 horizon chart 可能看見 local operator niches。

長 horizon chart 可能看見 macro-domains。

因此：

$$
\boxed{
\mathcal A^{(\tau_1)}
\neq
\mathcal A^{(\tau_2)}
}
$$

不必視為矛盾。

它可能只是 multiscale structure。

---

# 25. Time-Dependent Atlas 也不能每步重畫

Mucha 等人的 multislice network framework 提供「time-dependent network 可以把不同時間 slice 耦合起來」的外部參照。

CODT 吸收一個一般想法：

$$
\boxed{
\text{current chart should be coupled to prior chart}.
}
$$

因此 atlas learner 不應每個 window 完全獨立。

可以加入：

$$
TemporalConsistencyCost(
\mathcal A_t,
\mathcal A_{t-1}
).
$$

但 coupling 不能太強。

否則真正 domain split 會被壓掉。

所以 atlas evolution 是：

$$
\boxed{
Stability
\leftrightarrow
Adaptability
}
$$

的 model-selection 問題。


---

# 26. Dynamic Attractor 強版本為什麼被降級

「Domain 是 dynamic attractor」是一個有吸引力的說法。

因為它允許 domain 隨 runtime 改變。

但它也太寬。

任何 clustering shift 都可以被解釋成 attractor movement。

因此難以 falsify。

CODT-05 改成：

$$
\boxed{
\text{Domain is a quasi-stable chart over adaptive flow}.
}
$$

這個版本更嚴格。

因為它要求：

- flow adaptation；
- chart adaptation；
- chart switching cost；

可以被分開測。

---

# 27. Atlas Complexity Cost

Phase 0.7 把：

$$
L(A)
$$

正式加入 chart selection。

selection objective：

$$
\boxed{
L_{select}(A)
=
L(A)
+
L(
H_{train}
\mid
A
)
+
L(
H_{val}
\mid
H_{train},
A
).
}
$$

這表示：

> 多切一個 cluster / domain 不是免費。

如果 predictive-only learner 一直切細，就必須付 atlas description cost。

---

# 28. Normal Runtime 的 MDL 收斂

normal label-blind corpus 中：

predictive-only selector：

$$
K_{pred}
=
31.
$$

MDL selector：

$$
\boxed{
K_{MDL}
=
20.
}
$$

predictive test bits：

$$
4.3402.
$$

MDL test bits：

$$
4.3583.
$$

只犧牲：

$$
0.0181
$$

bits/transition。

但 full description length 改善：

$$
\boxed{
139.5
\text{ bits}.
}
$$

因此：

$$
\boxed{
\text{slightly worse local fit}
+
\text{better total compression}
}
$$

可以是更好的 atlas。

---

# 29. OOD 的 Single-Domain MDL Optimum

Phase 0.7 的 OOD 結果極端。

predictive selector 在不同 splits 會選約：

$$
14-18
$$

clusters。

但 MDL：

$$
\boxed{
K_{MDL,OOD}
=
1
}
$$

在：

$$
5/5
$$

splits 成立。

這不是：

$$
\boxed{
\text{OOD cognition has one true domain}.
}
$$

它只表示：

> 在目前 coder / corpus 下，更細的 stress partition 沒有把額外 atlas complexity 賺回來。

因此：

$$
\boxed{
MDLOptimum
\neq
OntologyTruth.
}
$$

---

# 30. Atlas Switch Gate

假設 runtime 已經有：

$$
\mathcal A_{old}.
$$

stress evidence 提出：

$$
\mathcal A_{new}.
$$

若不付 switching cost，任何 local improvement 都會鼓勵頻繁 rechart。

所以本文提出：

$$
\boxed{
NetSwitchGain
=
Gain_{heldout}
-
Cost_{chart}
-
Cost_{migration}
-
Cost_{instability}.
}
$$

只有：

$$
\boxed{
NetSwitchGain>0
}
$$

才有 atlas switch pressure。

---

# 31. Chart Description Cost

$$
Cost_{chart}
$$

至少包含：

- number of domains；
- membership assignment；
- overlap structure；
- boundary definitions；
- bridge registry；
- domain metadata；
- new routing rules。

因此更複雜 atlas 的成本不能只看 cluster count。

---

# 32. Migration Cost

atlas switch 也會影響：

- cached routing；
- operator/domain lookup；
- explanation labels；
- dashboards；
- memory indexes；
- monitoring policy；
- prior domain-conditioned statistics。

所以：

$$
Cost_{migration}
$$

可以很高。

這對 AI-native runtime 特別重要。

---

# 33. Instability Cost

如果 atlas 太敏感：

$$
\mathcal A_t
\rightarrow
\mathcal A_{t+1}
\rightarrow
\mathcal A_{t+2}
$$

不斷切換，系統會產生：

- label thrashing；
- route thrashing；
- memory invalidation；
- interpretability loss；
- policy oscillation。

所以：

$$
Cost_{instability}
$$

必須顯式存在。

---

# 34. Phase 0.7 的 Switch 結果

Phase 0.7 把 chart-switch cost 算入後，五種 stress regime 的 online switch gain 全部為負。

這支持：

$$
\boxed{
\text{existing normal atlas}
+
\text{adapted flow}
}
$$

比：

$$
\boxed{
\text{rebuild stress atlas}
}
$$

更值得。

這就是 Quasi-Stable Atlas 的 complexity-accounted evidence。

---

# 35. Structural Phase Transition 的更嚴格定義

CODT 不禁止真正 structural phase transition。

但要求更強 evidence。

一個 **Atlas Structural Transition Candidate** 至少需要：

## T1. Persistent Assignment Shift

不是一次 bootstrap fluctuation。

## T2. Flow-Controlled Gain

在控制 transition parameter adaptation 後，新 atlas仍有正 gain。

## T3. Complexity-Adjusted Gain

新 atlas 能支付 description / migration cost。

## T4. Boundary Reorganization

failure / bridge / legality boundary 也有一致改變。

## T5. Multi-Window Persistence

新 geometry 在後續 windows 保持。

因此：

$$
\boxed{
LargeARIChange
\not\Rightarrow
StructuralTransition.
}
$$

---

# 36. Regime Shift 的四種類型

本文將 regime shift 分成至少四類。

## 36.1 Parameter Shift

同一 structure：

$$
\mathcal A
$$

下：

$$
P_t
\rightarrow
P_{t+1}.
$$

## 36.2 State-Distribution Shift

$$
S_t
$$

的 distribution 改變，但 atlas 未必改。

## 36.3 Policy / Routing Shift

meta-control policy 改變 transition flow。

## 36.4 Structural Shift

需要真正：

$$
\mathcal A_t
\rightarrow
\mathcal A_{t+1}.
$$

CODT 要求先排除前三者，再宣告第四種。

---

# 37. Flow Freeze Test

為了判斷 atlas 是否真的需要改，可以做：

$$
\boxed{
\text{freeze atlas, adapt flow}.
}
$$

如果 prediction / compression 已恢復：

$$
\boxed{
AtlasChangeNotRequired.
}
$$

Phase 0.6 OOD case 就接近這類結果。

---

# 38. Atlas Freeze / Flow Freeze 的對稱 Ablation

也可以反過來：

$$
\boxed{
\text{freeze flow, change atlas}.
}
$$

若沒有 gain，表示 chart assignment shift 沒有獨立功能。

因此兩種 freeze experiment 應成為 atlas revision 的最低 falsification tool。

---

# 39. Shared-Bottom-Aware Flow Normalization

因 SBCR operators 具有高跨域 reuse，atlas learner 可以考慮一個 derived weighting：

$$
w_{ij}^{eff}
=
w_{ij}
\cdot
g(
SB_i,
SB_j,
Role_{ij}
).
$$

其中：

$$
g
$$

不是固定函數。

可以：

- 降低 infrastructure hub traffic；
- 分層計入 SB traffic；
- separate-layer modeling；
- edge-role normalization。

本文不固定最佳 normalization。

只固定原則：

$$
\boxed{
RawTraffic
\neq
DomainEvidence.
}
$$

---

# 40. Flow Tensor Candidate

如果只用單一 transition matrix：

$$
P_{ij},
$$

容易把不同 edge semantics 混在一起。

因此可定義：

$$
\boxed{
\mathcal F_{ijr}(t)
}
$$

其中：

$$
r
\in
\{
D,
B,
SB,
M,
W
\}.
$$

這使同一 pair：

$$
(U_i,U_j)
$$

可以因不同 role 具有不同 flow channel。

這是一個 typed-flow tensor candidate。

---

# 41. Atlas 可以是 Layered，而不是單張 Partition

若 flow 本來多層，atlas 也可以：

$$
\boxed{
\mathcal A_t
=
(
\mathcal A_t^{Domain},
\mathcal A_t^{SB},
\mathcal A_t^{Meta},
\mathcal A_t^{WorldInterface}
).
}
$$

這不是四張互斥 partition。

而是四種不同 control views。

Derived views 不得回寫 canonical operator identity。

---

# 42. Atlas 是 Control View，不是 Canonical State

CODT 延續 HSO / CDD 的一條重要 discipline：

$$
\boxed{
DerivedAtlas
\text{ cannot rewrite }
CanonicalHistory.
}
$$

如果今天 atlas 把：

$$
U_i
$$

從 Domain A 移到 Domain B，

昨天的 trace 不能被改成：

> 它昨天本來就在 B。

只能記：

$$
AtlasVersion_t.
$$

所以：

$$
\boxed{
Rechart
\neq
HistoryRewrite.
}
$$

---

# 43. Atlas 與 Human Label

human label：

$$
Search,
Memory,
Planning
$$

可以隨 atlas version 保留。

但 label 只是 presentation layer。

若 learned chart split：

$$
Memory
\rightarrow
Persistence
+
RetrievalSearch,
$$

human interface 可以仍顯示：

> Memory family has two operational regions.

不必強迫 runtime 回到單一 `MemoryDomain`。

---

# 44. Human Taxonomy 的正確角色

Phase 0.5 / 0.6 結果顯示：

human family partition 並不是 random。

在 normal synthetic corpus 中，human taxonomy 對 transition structure 有顯著資訊。

同時 learned chart 可以有更低 code length。

因此：

$$
\boxed{
HumanTaxonomy
=
InformativePrior,
}
$$

但：

$$
\boxed{
HumanTaxonomy
\neq
CanonicalAtlas.
}
$$

這是 CODT 對古典認知分類的正式位置。

---

# 45. Atlas 不是 Embedding Cluster

即使未來使用 embedding：

$$
z_i
=
Embed(\Omega_i),
$$

再做 clustering，也只能得到：

$$
\boxed{
SemanticCluster.
}
$$

它不是 domain。

因為 domain 還需要：

- legal composition；
- flow；
- failure；
- license；
- boundary；
- history；
- complexity；
- predictive evidence。

因此：

$$
\boxed{
SemanticSimilarity
\neq
OperationalDomain.
}
$$

---

# 46. Atlas 不是 Graph Cluster

同理：

$$
CommunityDetection(G)
$$

只是 candidate chart generator。

不同 graph projection：

$$
G^{transition},
G^{type},
G^{failure},
G^{license},
G^{world}
$$

可以得到不同 partitions。

因此：

$$
\boxed{
\text{one graph}
\neq
\text{the cognition}.
}
$$

---

# 47. Flow-Based Evidence 與 Structural Evidence 應分帳

本文建議 domain evidence ledger 分成：

$$
\boxed{
E_\alpha
=
(
E_\alpha^{flow},
E_\alpha^{structure},
E_\alpha^{boundary},
E_\alpha^{complexity},
E_\alpha^{stability}
).
}
$$

這避免：

> flow evidence 很強

被偷換成：

> structural ontology 已證明。

---

# 48. Flow Confidence 與 Atlas Confidence

可以分別維護：

$$
Conf(P_t)
$$

與：

$$
Conf(\mathcal A_t).
$$

新 regime 剛出現時：

$$
Conf(P_t)
$$

可能快速下降。

但：

$$
Conf(\mathcal A_t)
$$

不必同步歸零。

反過來，長期 structural evidence 改變時，atlas confidence 才逐步下降。

---

# 49. Flow Adaptation 不應自動改 Domain Label

一個 practical rule：

若：

$$
P_t
\rightarrow
P_{t+1}
$$

但：

$$
NetSwitchGain
\leq0,
$$

則：

$$
\boxed{
UpdateFlow,
KeepAtlas.
}
$$

這是 AI runtime 可直接採用的控制策略。

---

# 50. Atlas Adaptation 也不應自動重訓全部 Flow

若 atlas 只是改 chart view，而 canonical operator transitions 未變，則：

$$
\boxed{
Rechart
\not\Rightarrow
ResetAllFlowModels.
}
$$

可以只更新：

- aggregate statistics；
- routing cache；
- domain-conditioned predictors。

這避免不必要重訓。


---

# 51. Flow-Atlas Hysteresis

若 atlas switch 有成本，合理系統會出現 hysteresis。

即：

$$
Threshold_{A\rightarrow B}
\neq
Threshold_{B\rightarrow A}.
$$

這不是 bug。

它可以防止 chart thrashing。

因此：

$$
\boxed{
AtlasHysteresis
=
\text{possible stability mechanism}.
}
$$

---

# 52. Recovery 也需要測

若：

$$
normal
\rightarrow
stress
\rightarrow
normal,
$$

系統應檢查：

- flow 是否恢復；
- atlas 是否需要回切；
- prior atlas 是否仍有效；
- 是否留下 path dependence。

這可以定義：

$$
H_A
=
d(
\mathcal A_{return},
\mathcal A_{pre}
).
$$

若 atlas 從未切換：

$$
H_A=0
$$

不代表 cognition 沒受 stress。

flow 仍可能發生巨大 hysteresis。

---

# 53. Adaptation Lag

定義：

$$
\tau_{adapt}^P
$$

為 flow recovery lag。

定義：

$$
\tau_{adapt}^{A}
$$

為 atlas switch / recovery lag。

若：

$$
\tau_{adapt}^{P}
<
\tau_{adapt}^{A},
$$

則支持 timescale separation。

這應在 real runtime 中進一步測。

---

# 54. Atlas Trigger 不應只看 ARI

可能 trigger：

$$
Trigger_A
=
f(
PredictiveResidual,
CompressionResidual,
BoundaryShift,
FailureShift,
StabilityLoss,
NetSwitchGain
).
$$

而不是：

$$
Trigger_A
=
ARI<\epsilon.
$$

ARI 只比較 assignments。

不回答：

> 新 chart 是否有用？

---

# 55. Atlas 也不應只看 Modularity

Phase 0.5 / 0.6 stress chart modularity 很低，仍可能在當時 predictive objective 上有 gain。

這說明：

$$
\boxed{
DomainLikeness
\neq
CommunityDensity.
}
$$

domain 可以是 predictive quotient / control chart，而不一定是密集 graph island。

---

# 56. Quasi-Stable Atlas 的正確理解

「準穩定」有三個層次。

## 56.1 Assignment Stability

membership 不頻繁改。

## 56.2 Functional Stability

predictive / compressive role 保留。

## 56.3 Interface Stability

boundary / bridge contract 保留。

真正重要的是後兩種。

所以即使 assignment 有小變動，只要 function / interface 穩定，domain identity 可以延續。

---

# 57. Domain Identity 的動態條件

可提出：

$$
SameDomain(
\mathfrak D_t,
\mathfrak D_{t+1}
)
$$

若：

$$
FunctionalSimilarity
+
BoundarySimilarity
+
InterfaceContinuity
$$

高於 threshold。

因此：

$$
\boxed{
SameDomain
\not\Rightarrow
SameMembershipSet.
}
$$

這使 versioned domain identity 有正式空間。

---

# 58. Flow Shock 不等於 Domain Death

若 stress 下：

$$
P_t
$$

劇烈變化，

但 atlas 仍有：

- boundary continuity；
- compression value；
- interface continuity；

則：

$$
\boxed{
FlowShock
\neq
DomainDeath.
}
$$

這是 CODT-05 對 dynamic cognition 最重要的概念修正之一。

---

# 59. Atlas Shift 不等於 Ontology Shift

同樣：

$$
\mathcal A_t
\rightarrow
\mathcal A_{t+1}
$$

也只代表 derived chart 改變。

它不直接推出：

$$
\boxed{
UltimateCognitiveOntology
\text{ changed}.
}
$$

CODT 的 atlas 是 operational ontology candidate。

不是 ultimate ontology。

---

# 60. AI-Native Runtime 的實作含義

Flow-Atlas Separation 對 AI architecture 的直接含義是：

不要每次 behavior drift 就重建 ontology。

更合理 pipeline：

$$
ObserveDrift
\rightarrow
UpdateFlowModel
\rightarrow
EvaluateResidual
\rightarrow
EstimateAtlasGain
\rightarrow
ApplySwitchGate.
$$

只有必要時才 rechart。

這比：

$$
Drift
\rightarrow
ReclusterEverything
$$

更穩定。

---

# 61. Runtime State

本文建議 dynamic cognitive runtime 至少保存：

$$
\boxed{
RuntimeState_t
=
(
OperatorState_t,
FlowModel_t,
AtlasVersion_t,
SBCRState_t,
BoundaryState_t,
History_t
).
}
$$

這使 flow、atlas、shared-bottom 與 World boundary 各自版本化。

---

# 62. Flow Model Registry

每個 flow model 應記：

- training window；
- regime；
- feature set；
- history length；
- code length；
- calibration；
- uncertainty；
- atlas version；
- SB weighting policy。

否則 flow drift 無法重放。

---

# 63. Atlas Registry

atlas 應記：

- chart version；
- domain IDs；
- membership；
- overlap；
- bridge；
- boundary；
- description cost；
- evidence；
- switch history；
- previous atlas link。

這使：

$$
\boxed{
AtlasEvolution
}
$$

可審計。

---

# 64. Atlas Switch Certificate

正式 switch 應產生：

$$
\boxed{
AtlasSwitchCertificate
}
$$

至少記：

- old atlas；
- new atlas；
- evidence window；
- flow-controlled gain；
- chart cost；
- migration cost；
- stability evidence；
- unresolved conflicts；
- rollback target。

這延續 CODT certificate-carrying computation。

---

# 65. Atlas Rollback

如果新 atlas 部署後：

- predictive loss 上升；
- routing error 上升；
- interpretability 崩解；
- instability 增加；

則可以：

$$
\boxed{
Rollback(
\mathcal A_{new}
\rightarrow
\mathcal A_{old}
).
}
$$

Domain theory 必須能 rollback。

不能只向前增加 complexity。

---

# 66. Flow / Atlas 的認識論地位不同

Flow model 是：

$$
\boxed{
\text{runtime predictive model}.
}
$$

Atlas 是：

$$
\boxed{
\text{derived structural/control model}.
}
$$

它們的 evidence license 不同。

因此：

$$
\boxed{
FlowConfidence
\neq
DomainConfidence.
}
$$

---

# 67. 外部 Dynamic Community Research 的正確位置

本文引用：

- Rosvall-Bergstrom flow compression；
- Delvenne-Yaliraki-Barahona Markov stability；
- Mucha 等 temporal / multislice communities；
- Peixoto complexity-aware block model selection；

作四種外部方法學參照。

它們共同提醒：

1. flow 可以揭露 structure；
2. structure 可以依 time scale 而變；
3. temporal slice 之間可以耦合；
4. model complexity 必須被懲罰。

CODT 額外加入：

- typed operator semantics；
- legality；
- shared-bottom infrastructure；
- epistemic license；
- failure；
- history；
- World boundary。

因此：

$$
\boxed{
FlowAtlasCODT
\neq
DynamicCommunityDetection.
}
$$

---

# 68. CODT-05 憲法增補

## CODT-C34：Flow-Atlas Separation

$$
\boxed{
TransitionFlow
\neq
DomainAtlas.
}
$$

## CODT-C35：Time-Scale Separation Candidate

$$
\boxed{
\tau_P
<
\tau_{\mathcal A}
}
$$

作為可反證候選，不是 universal law。

## CODT-C36：Assignment-Function Separation

$$
\boxed{
AssignmentShift
\not\Rightarrow
FunctionalDomainShift.
}
$$

## CODT-C37：Flow-Controlled Repartition

atlas repartition claim 必須先控制 flow parameter adaptation。

## CODT-C38：Complexity-Aware Switch

$$
\boxed{
NetSwitchGain>0
}
$$

才形成 strong atlas-switch evidence。

## CODT-C39：Infrastructure Traffic Separation

$$
\boxed{
SharedBottomFlow
\neq
DomainInternalFlow.
}
$$

## CODT-C40：Atlas Non-Rewriting

$$
\boxed{
Rechart
\neq
HistoryRewrite.
}
$$

## CODT-C41：Structural Transition Gate

ARI / modularity / assignment difference 單獨不足以宣告 structural phase transition。

## CODT-C42：Quasi-Stable Domain Identity

$$
\boxed{
SameDomain
\not\Rightarrow
SameMemberSet.
}
$$

---

# 69. 本文的理論地位

本文沒有證明：

$$
\tau_P
<
\tau_{\mathcal A}
$$

是所有 cognition 的普遍定律。

也沒有證明 MDL 是唯一正確 atlas learner。

本文真正建立的是：

$$
\boxed{
\text{Flow and Atlas must be separately modeled and separately falsified.}
}
$$

這是一條 theory-design constraint。

---

# 70. 與下一篇的接口

CODT-05 把 Flow 與 Atlas 拆開了。

但仍有一個問題：

> Flow 本身需要多少 history？

如果下一個 operator 取決於：

$$
U_{t-k:t},
$$

而不是只取決於：

$$
U_t,
$$

那麼我們目前看到的一部分 atlas structure，會不會其實只是 higher-order history 被一階 flow 錯投影出來？

下一篇因此處理：

$$
\boxed{
History
\neq
Flow
\neq
Atlas.
}
$$

也就是 **History-Flow-Atlas Separation**。

---

# 結論

認知域既不是固定 taxonomy，也不是每一個時間 window 都重新 clustering 的漂浮集合。

CODT-05 的核心是：

$$
\boxed{
\text{Quasi-Stable Atlas over Adaptive Operator Flow}.
}
$$

Flow 回答：

> cognition 現在怎麼走？

Atlas 回答：

> 哪些 operational regions 在累積 evidence 下值得被保留成較慢的結構？

Shared-bottom 又回答：

> 哪些交通本來就是跨域基礎設施？

因此：

$$
\boxed{
\text{Flow}
\neq
\text{Atlas}
\neq
\text{SharedInfrastructure}.
}
$$

這三者若被混在一起，我們會把：

- traffic shock 誤認成 domain death；
- shared infrastructure hub 誤認成 domain core；
- clustering instability 誤認成 cognitive phase transition；
- predictive overfit 誤認成新的 ontology。

Phase 0.6 的 OOD 反證最清楚地顯示：

$$
ARI
=
0.0411
$$

可以和：

$$
\Delta_A<0
$$

同時成立。

也就是：

$$
\boxed{
\text{chart looks different}
\not\Rightarrow
\text{new chart is useful}.
}
$$

Phase 0.7 再進一步顯示：

> 即使 stress-specific chart 局部 prediction 更好，只要它無法支付 chart description / switching cost，就不值得 deployment。

所以 CODT 對 dynamic cognition 的第一個成熟版本不是：

$$
\text{domains are always moving}.
$$

而是：

$$
\boxed{
\text{flows move quickly;
atlases move only when structural evidence earns the move}.
}
$$

這就是 Flow-Atlas Separation。

---

# 參考文獻與外部研究種子

## A. Flow / Community Dynamics

1. Rosvall, M., & Bergstrom, C. T. (2008). "Maps of random walks on complex networks reveal community structure." *Proceedings of the National Academy of Sciences*, 105(4), 1118-1123. DOI: 10.1073/pnas.0706851105.
2. Delvenne, J.-C., Yaliraki, S. N., & Barahona, M. (2010). "Stability of graph communities across time scales." *Proceedings of the National Academy of Sciences*, 107(29), 12755-12760. DOI: 10.1073/pnas.0903215107.
3. Mucha, P. J., Richardson, T., Macon, K., Porter, M. A., & Onnela, J.-P. (2010). "Community Structure in Time-Dependent, Multiscale, and Multiplex Networks." *Science*, 328(5980), 876-878. DOI: 10.1126/science.1184819.
4. Peixoto, T. P. (2014). "Hierarchical Block Structures and High-Resolution Model Selection in Large Networks." *Physical Review X*, 4, 011047. DOI: 10.1103/PhysRevX.4.011047.

**邊界聲明：** 上述工作只作 flow-based structure、multiscale partition、temporal coupling 與 complexity-aware model selection 的外部方法學參照。CODT 的 Flow-Atlas Separation、typed operator traffic、shared-bottom flow、epistemic license、World boundary 與 atlas-switch contract 不宣稱來自上述文獻。

## B. 內部理論來源

1. CODT-01〈從認知方法到認知算子：認知解構學的域化轉向〉。
2. CODT-02〈認知算子代數與相對原子性〉。
3. CODT-03〈認知域的生成：域不是分類名稱，而是算子閉包與操作生態〉。
4. CODT-04〈共享底層認知域：Shared-Bottom Cognitive Runtime〉。
5. CDD Phase 0 v0.5：Regime-Dependent Domain Geometry Candidate。
6. CDD Phase 0 v0.6：Label-Free Adversary、Flow-Atlas Ablation、Online Atlas。
7. CDD Phase 0 v0.7：MDL / Complexity-Regularized Atlas。
8. HSO v0.8 / Ecological Geometry Atlas。
9. GCORF / General Cognitive Operator Reverse Engineering Framework。
10. MWT / Mathematical World Theory。

---

# 版本記錄

## v1.0

- 正式建立 Flow-Atlas Separation。
- 定義 adaptive transition flow $P_t$ 與 derived atlas $\mathcal A_t$。
- 固定 $\tau_P<\tau_{\mathcal A}$ 為可反證 timescale candidate。
- 納入 Phase 0.6 OOD ablation：ARI collapse 不推出 useful repartition。
- 建立 parameter gain / partition gain 分帳。
- 引入 domain-internal、bridge、shared-bottom、meta-control、world-boundary 五種 typed flow roles。
- 建立 shared-bottom-aware flow analysis。
- 引入 MDL atlas description cost、migration cost、instability cost。
- 建立 Atlas Switch Gate、Switch Certificate 與 rollback。
- 將 dynamic-domain 強版本修正為 Quasi-Stable Atlas over Adaptive Operator Flow。
- 為 CODT-06 History-Flow-Atlas Separation 建立 dynamic foundation。
