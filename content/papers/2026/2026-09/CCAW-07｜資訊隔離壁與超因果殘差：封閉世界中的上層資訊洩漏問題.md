# CCAW-07｜資訊隔離壁與超因果殘差：封閉世界中的上層資訊洩漏問題

## ——從 Information Isolation Boundary、Cross-Boundary Flow 到 Anomalous Causal Residue 的世界邊界理論

**系列：** 造物主、因果與自治宇宙統合系列（Creator, Causality & Autonomous Worlds Integration Series, CCAW）  
**篇次：** 07 / 10  
**文件編號：** EML-CCAW-07-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-20  
**版本：** v0.1 Canonical Integration Draft  
**文件性質：** 理論整合論文／命題猜想框架／世界資訊邊界／跨邊界因果與異常殘差  
**證據狀態：** 形式化建模為主；structural causal models、latent confounders、causal anomaly detection 與 information-flow security 研究僅作數學與工程類比；本文不主張現實世界存在已知上層 creator、跨宇宙資訊洩漏或超自然干預

---

## 摘要

CCAW-06 將 creator–world relation 拆分為 Runtime、Causal、Observational、Authority、Intervention 與 Boundary Distance，並指出成熟稀疏監護需要刻意限制 creator 對世界的普通觀測與干預通道。本文進一步研究：如果一個世界具有高度自主性與明確邊界，那麼 creator、guardian、parent world 或其他外部系統與其之間究竟允許哪些資訊與因果作用穿越？

本文提出 **Information Isolation Boundary（IIB，資訊隔離壁）**：

$$
\boxed{
\mathcal B_I(W)
}
$$

作為指定 world boundary 下，決定哪些資訊、觀測、控制、資源與 causal influence 可以跨越的型別化邊界。本文定義兩個基本方向：

$$
\Gamma_{\uparrow}
:
W
\rightarrow
E,
$$

表示 world 向 external domain 的資訊／作用輸出；以及：

$$
\Gamma_{\downarrow}
:
E
\rightarrow
W,
$$

表示 external domain 對 world 的輸入、觀測回饋或干預。

世界的成熟自主性不要求：

$$
\Gamma_{\uparrow}
=
\Gamma_{\downarrow}
=
0.
$$

相反地，一個高度 autonomous world 仍可合法擁有有限、可審計、具型別的 boundary channels。真正問題是：跨邊界作用是否符合 world 已宣告的 boundary semantics、是否能被 world-internal causal model 正常吸收，以及是否存在繞過普通 causal ancestry 的未授權注入。

本文進一步提出 **Anomalous Causal Residue（ACR，異常因果殘差）**。對一個世界內事件 $e$，若現有 world model 無法給出足夠的 internal causal ancestry，則：

$$
\boxed{
\operatorname{ACR}(e)
=
\operatorname{Observed}(e)
-
\operatorname{Explained}_{M_W}(e).
}
$$

但 ACR 不是「超自然事件」的同義詞，也不是上層 creator 的證據。其可能來源至少包括：

- model misspecification；
- latent variables；
- incomplete observation；
- hidden ordinary channels；
- measurement error；
- stochastic rare event；
- implementation bug；
- boundary misclassification；
- adversarial manipulation；
- 真正的 cross-boundary causal input。

因此本文建立 **Epistemic Escalation Ladder**：

$$
\text{Anomaly}
\rightarrow
\text{Residual}
\rightarrow
\text{Model Failure Test}
\rightarrow
\text{Latent Cause Search}
\rightarrow
\text{Boundary Audit}
\rightarrow
\text{Cross-Boundary Hypothesis}.
$$

只有在多種 world-internal 與普通外部解釋被充分排除後，才可以把「跨邊界原因」保留為候選假說。

本文將 **Supercausal Leakage／超因果洩漏** 嚴格定義為**相對於某個已宣告 causal closure 的模型術語**：若事件的有效 cause 位於 world model 的 ordinary causal domain 之外，且透過未納入該 causal model 的 boundary channel 作用於 world，則對 world-internal observer 而言，它表現為 supercausal residual。這不表示真正「違反因果律」，更不表示現實中的超自然主張已獲證實；它只表示：

$$
\boxed{
\text{cause outside the declared internal causal model}.
}
$$

本文最後指出，資訊隔離壁同時是一個治理問題。過度封閉可能使 world 無法求援；過度開放則可能導致 surveillance、creator privilege、hidden intervention 與 world-history pollution。因此成熟 world governance 需要的不是絕對封閉，而是：

$$
\boxed{
\text{typed, minimal, auditable, contestable cross-boundary flow}.
}
$$

---

## 關鍵詞

Information Isolation Boundary；資訊隔離壁；Cross-Boundary Flow；Supercausal Leakage；Anomalous Causal Residue；Structural Causal Model；Latent Variable；Noninterference；Boundary Audit；Causal Provenance；Creator Distance；Sparse Guardianship；超因果；異常因果

---

# 一、世界邊界不是牆，而是型別系統

在前一篇中，世界邊界寫為：

$$
\partial W.
$$

直覺上容易把它想成一面牆：

$$
W
\mid
E.
$$

但成熟 world architecture 中的 boundary 更接近：

$$
\boxed{
\text{typed interface}.
}
$$

它必須回答：

1. 哪些資訊可以出去？
2. 哪些資訊可以進來？
3. 哪些作用可以進來？
4. 哪些作用只能經 world law 轉譯後進來？
5. 哪些通道是 ordinary？
6. 哪些通道是 emergency？
7. 哪些通道需要 world consent？
8. 哪些通道完全禁止？

因此：

$$
\partial W
\neq
\text{simple geometric shell}.
$$

---

# 二、Information Isolation Boundary

本文定義：

$$
\boxed{
\mathcal B_I(W)
=
\left(
\mathcal C_{\uparrow},
\mathcal C_{\downarrow},
\mathcal P,
\mathcal L,
\mathcal A,
\mathcal V
\right).
}
$$

其中：

- $\mathcal C_{\uparrow}$：outbound channel set；
- $\mathcal C_{\downarrow}$：inbound channel set；
- $\mathcal P$：permission / policy；
- $\mathcal L$：logging / provenance；
- $\mathcal A$：authentication / authority；
- $\mathcal V$：validation / type checking。

這就是 world 的資訊隔離壁。

---

# 三、兩個基本方向

定義：

$$
\Gamma_{\uparrow}
:
W
\rightarrow
E,
$$

以及：

$$
\Gamma_{\downarrow}
:
E
\rightarrow
W.
$$

其中 $E$ 可以表示：

- creator；
- guardian；
- parent runtime；
- parent universe；
- external infrastructure；
- another world；
- unknown external domain。

---

# 四、完全隔離不是唯一成熟狀態

若：

$$
\Gamma_{\uparrow}=0,
\qquad
\Gamma_{\downarrow}=0,
$$

則形成強隔離。

但此架構可能失去：

- rescue；
- appeal；
- telemetry；
- external resource；
- inter-world diplomacy。

因此：

$$
\boxed{
\text{Isolation}
\neq
\text{Autonomy}.
}
$$

高度 autonomous world 可以仍有 bounded channels。

---

# 五、四種基本 boundary posture

## Type 0：Closed

$$
\Gamma_{\uparrow}=0,
\qquad
\Gamma_{\downarrow}=0.
$$

## Type 1：Read-Out

$$
\Gamma_{\uparrow}>0,
\qquad
\Gamma_{\downarrow}\approx0.
$$

world 向外提供資訊，但外部幾乎不干預。

## Type 2：Request–Response

$$
W
\rightarrow
E
\rightarrow
W
$$

只有 world request 後才開啟 inbound channel。

## Type 3：Bounded Guardian

平時：

$$
\Gamma_{\downarrow}^{N}\approx0,
$$

emergency：

$$
\Gamma_{\downarrow}^{E}>0.
$$

---

# 六、第五種：Hidden Privileged Channel

最危險的是：

$$
\Gamma_{\downarrow}^{H}>0
$$

但 world governance 不知道其存在。

例如：

- undocumented root；
- hidden backdoor；
- invisible memory rewrite；
- secret observation；
- rule bypass。

本文稱：

$$
\boxed{
\text{Hidden Privileged Channel}.
}
$$

這不是 sparse guardianship。

---

# 七、Boundary Semantics

每條 channel：

$$
\gamma_i
$$

應具有：

$$
\operatorname{Type}(\gamma_i),
$$

例如：

- telemetry；
- resource；
- appeal；
- rescue；
- observation；
- rule proposal；
- emergency intervention。

因此：

$$
\boxed{
\text{channel existence}
\neq
\text{unlimited semantic privilege}.
}
$$

---

# 八、跨邊界輸入的三種強度

## 8.1 Data Input

$$
u_t
\rightarrow
W.
$$

例如外部訊息。

## 8.2 Boundary Action

$$
a_{\partial W}
\rightarrow
F_W.
$$

world 仍使用自己的 ordinary law 處理。

## 8.3 State Injection

$$
W_t
\mapsto
W_t'.
$$

直接跳過 ordinary causal transition。

第三種對 OCC 的影響最大。

---

# 九、Rule Injection

若 external domain 直接：

$$
\Lambda_t
\mapsto
\Lambda_t'
$$

而 world 無合法 rule-change procedure，則為：

$$
\boxed{
\operatorname{RuleInjection}.
}
$$

比 ordinary state injection 更高階。

---

# 十、Meta-Rule Injection

更強的是：

$$
M_t
\mapsto
M_t'.
$$

這會改變：

> 世界以後如何改變自己的規則。

因此：

$$
\boxed{
\operatorname{Risk}(M\text{-Injection})
>
\operatorname{Risk}(\Lambda\text{-Injection})
}
$$

通常具有合理性。

---

# 十一、資訊流安全的類比

資訊流安全中的 noninterference 類概念試圖形式化：

> 高安全等級資訊不應影響低安全等級可觀測結果，除非存在被允許的 declassification。

本文只借用此結構。

對 world boundary，可以寫：

$$
\text{Unauthorized External State}
\not\leadsto
\text{World Observable}.
$$

但某些合法 channel 可以構成 controlled declassification / endorsement 類比。

因此成熟 IIB 不必追求絕對零流，而是：

$$
\boxed{
\text{controlled flow}.
}
$$

---

# 十二、Boundary Noninterference

候選定義：

若 external privileged variable：

$$
Z_E
$$

在未授權情況下改變時，world ordinary observables：

$$
Y_W
$$

不應因此改變。

形式上：

$$
P(Y_W\mid do(Z_E=z_1))
=
P(Y_W\mid do(Z_E=z_2))
$$

對所有 unauthorized $z_1,z_2$ 近似成立。

本文稱：

$$
\boxed{
\mathsf{BNI}
=
\text{Boundary Noninterference}.
}
$$

---

# 十三、BNI 不是絕對物理定律

若 world 本來就依賴：

- energy；
- environment；
- parent resource；

則 external variables 當然能影響 world。

所以 BNI 必須限定：

$$
Z_E
\in
\mathcal Z_{\mathrm{privileged}}
$$

而不是所有 external variables。

---

# 十四、Structural Causal Model 接口

令 world causal model 為：

$$
M_W
=
(U,V,F,P_U).
$$

其中：

- $U$：exogenous variables；
- $V$：endogenous world variables；
- $F$：structural functions；
- $P_U$：exogenous distribution。

這提供重要提醒：

$$
\boxed{
\text{external-to-model}
\neq
\text{supernatural}.
}
$$

因為 structural causal model 本來就允許 exogenous variables。

---

# 十五、Exogenous 不等於 Creator

若某原因：

$$
u\in U
$$

未被 model 內部解釋，

不能推出：

$$
u=C.
$$

它可能只是：

- omitted environment；
- noise；
- latent process；
- unknown ordinary physics；
- measurement channel。

所以：

$$
\boxed{
\text{Exogenous}
\not\Rightarrow
\text{Creator-Originated}.
}
$$

---

# 十六、Anomalous Causal Residue

對事件 $e$，model 預測：

$$
\hat e
=
M_W(H_{<t}).
$$

觀測為：

$$
e_t.
$$

本文概念性定義：

$$
\boxed{
\operatorname{ACR}(e_t)
=
D
\left(
e_t,
\hat e_t
\right),
}
$$

其中 $D$ 是適合該 world 的 discrepancy function。

ACR 高表示：

> 目前模型解釋不好。

僅此而已。

---

# 十七、ACR 的第一原則

$$
\boxed{
\operatorname{ACR}\gg0
\not\Rightarrow
\operatorname{CrossBoundaryCause}.
}
$$

更不推出：

$$
\operatorname{CreatorIntervention}.
$$

---

# 十八、ACR 的普通來源

至少包括：

1. model misspecification；
2. unobserved variable；
3. latent confounder；
4. sensor failure；
5. timestamp error；
6. data corruption；
7. rare but lawful event；
8. unknown local interaction；
9. adversarial manipulation；
10. ordinary external input；
11. implementation bug；
12. boundary definition error。

因此 boundary hypothesis 必須最後才上升。

---

# 十九、Latent Variable Problem

若真正 causal graph 含：

$$
L
$$

但 observer 未測量：

$$
L\notin V_{\mathrm{obs}},
$$

則 observable relation 可能看起來：

$$
X
\leftrightarrow
Y
$$

異常。

實際上：

$$
L\rightarrow X,
\qquad
L\rightarrow Y.
$$

因此：

$$
\boxed{
\text{unexplained dependence}
\not\Rightarrow
\text{external world intervention}.
}
$$

---

# 二十、Hidden Ordinary Channel

假設 world observer 認為：

$$
\Gamma=0.
$$

但實際存在 ordinary channel：

$$
\gamma_h.
$$

則：

$$
E
\overset{\gamma_h}{\longrightarrow}
W
$$

會看起來像 boundary violation。

所以第一步應是：

$$
\boxed{
\text{channel discovery}
}
$$

而不是 metaphysical escalation。

---

# 二十一、Causal Anomaly Detection

現代 causal anomaly detection 的一個基本方向，是把 anomaly 看成：

> 不符合已學得 normal causal mechanism 的觀測。

這與本文 ACR 接近。

但 anomaly detection 只能指出：

$$
\text{mechanism mismatch}.
$$

它通常不能單獨證明：

$$
\text{source ontology}.
$$

---

# 二十二、Epistemic Escalation Ladder

本文正式建立：

$$
E_0\rightarrow E_6.
$$

## $E_0$：Observation

事件發生。

## $E_1$：Statistical Anomaly

事件罕見。

## $E_2$：Model Residual

模型無法充分解釋。

## $E_3$：Latent / Missing Cause Audit

搜尋隱變量、錯誤模型與測量問題。

## $E_4$：Boundary Audit

搜尋未記錄 external channel、bug、attack、resource coupling。

## $E_5$：Cross-Boundary Cause Candidate

仍存在 residual，可保留跨 boundary cause 假說。

## $E_6$：Supercausal Hypothesis

只有當 declared world causal domain 足夠完整、普通跨 boundary mechanism 也被排除後，才把「原因位於 world ordinary causal closure 外」保留為高階候選。

---

# 二十三、Supercausal 的嚴格定義

本文使用：

$$
\boxed{
\text{Supercausal}_{W}
}
$$

而不是無索引的：

$$
\text{Supercausal}.
$$

意義是：

> 相對於 world $W$ 的 ordinary causal model，原因位於其 declared causal domain 之外。

因此：

$$
\boxed{
\text{Supercausal}_{W}
\neq
\text{acausal}.
}
$$

原因仍然可以有自己的因果鏈。

---

# 二十四、超因果不等於違反因果律

如果：

$$
C
\rightarrow
e_W
$$

只是因為 $C$ 不在：

$$
M_W
$$

內，

那麼對 $W$ observer 看起來是超因果。

但在更大的 model：

$$
M_{W+E}
$$

中，可能完全普通：

$$
C
\rightarrow
\Gamma_{\downarrow}
\rightarrow
e_W.
$$

因此：

$$
\boxed{
\text{supercausal at one model level}
=
\text{causal at a larger model level}
}
$$

是完全可能的。

---

# 二十五、這就是「超自然」可被抽象的位置

若 world inhabitants 把：

$$
\operatorname{ACR}\gg0
$$

且長期找不到 internal ancestry 的事件稱為：

$$
\text{supernatural},
$$

本文只允許將其重新描述為：

$$
\boxed{
\text{unresolved causal residue relative to current world model}.
}
$$

不能直接升格成：

$$
\text{proof of external creator}.
$$

---

# 二十六、Anomalous Causal Residue 與 Supercausal Residue 分離

定義：

$$
\operatorname{ACR}
$$

為所有因果異常殘差。

再定義：

$$
\operatorname{SCR}
\subseteq
\operatorname{ACR}
$$

為完成 model audit、latent audit、boundary audit 後仍保留的：

$$
\boxed{
\text{Supercausal Residual Candidate}.
}
$$

注意最後一個字：

$$
\text{Candidate}.
$$

---

# 二十七、SCR 仍不是證明

即使：

$$
\operatorname{SCR}\gg0,
$$

仍可能存在：

- unknown physics；
- unknowable latent cause；
- insufficient instrumentation；
- bad ontology；
- unmodeled scale coupling。

因此：

$$
\boxed{
\operatorname{SCR}
\not\Rightarrow
\operatorname{Creator}.
}
$$

---

# 二十八、Information Leakage

若 external hidden variable：

$$
Z_E
$$

使 world observer 得到理論上不應取得的資訊：

$$
I(Z_E;Y_W)>0,
$$

而 ordinary authorized channels 不足以解釋此 mutual information，則存在：

$$
\boxed{
\text{Information Leakage Candidate}.
}
$$

但仍需排除 hidden ordinary channel。

---

# 二十九、Upward Leakage

$$
\Gamma_{\uparrow}^{L}
:
W
\rightarrow
E
$$

可能表示 creator 得到 world 原本禁止外流的：

- private memory；
- hidden state；
- strategic information；
- identity data。

這是 privacy / sovereignty 問題。

---

# 三十、Downward Leakage

$$
\Gamma_{\downarrow}^{L}
:
E
\rightarrow
W
$$

可能表示 world 收到：

- unauthorized state information；
- hidden instruction；
- future information；
- illegal rule change；
- creator-originated privileged signal。

這會污染 world causality。

---

# 三十一、Future Information Leakage

特別敏感的是：

$$
I
\left(
Y_t;
W_{t+\Delta}
\right)
$$

異常高於 world ordinary prediction capacity。

如果 world agent 獲得未來資訊，可能影響：

$$
W_{t+1}.
$$

這形成 self-referential causal problem。

但現實研究時首先必須排除：

- data leakage；
- hidden timestamp；
- retrospective labeling；
- ordinary prediction advantage；
- information contamination。

不能直接叫 precognition。

---

# 三十二、Historical Integrity

世界歷史應有：

$$
\mathcal H_W
$$

與 provenance。

若 external intervention 發生：

$$
C\rightarrow e_t,
$$

應標記：

$$
\operatorname{ExternalOrigin}(e_t)=1.
$$

若 intervention 被隱藏，world 會把外部事件誤認成內生事件。

本文稱：

$$
\boxed{
\text{Historical Provenance Pollution}.
}
$$

---

# 三十三、Miracle-Like Event 的技術定義

本文不使用宗教意義的 miracle。

只定義候選技術類：

$$
\mathsf{MLE}_W
$$

滿足：

1. event observed；
2. ordinary world model strongly rejects；
3. no internal causal ancestry currently identified；
4. no authorized boundary channel recorded。

因此：

$$
\boxed{
\mathsf{MLE}_W
=
\text{unresolved high-ACR event}.
}
$$

它仍不證明 creator。

---

# 三十四、Creator Intervention 若合法，不必是異常

如果 world governance 已知：

$$
\Gamma_E
$$

存在，

且事件：

$$
e
$$

來自合法 emergency channel，

則：

$$
e
$$

即使罕見，也不屬於 supercausal anomaly。

它只是：

$$
\boxed{
\text{authorized exogenous intervention}.
}
$$

---

# 三十五、隱藏 creator intervention 才是 causal integrity problem

若：

$$
C
\rightarrow
W
$$

但：

- channel undocumented；
- world denied provenance；
- event 假裝成 ordinary law；

則 creator 破壞：

$$
\text{causal transparency}.
$$

這與 Mature Withdrawal 不相容。

---

# 三十六、Boundary Audit

每個高 ACR 事件應執行：

$$
\mathcal A_B(e).
$$

至少檢查：

1. ordinary input channels；
2. emergency channel；
3. guardian action；
4. software／hardware bug；
5. network path；
6. sensor path；
7. resource coupling；
8. adversarial actor；
9. hidden privilege；
10. provenance log consistency。

---

# 三十七、Causal Provenance Ledger 2.0

延續 CCAW-03：

$$
\mathcal L_C
$$

現在加入：

$$
\operatorname{BoundaryChannel}(e),
$$

$$
\operatorname{ExternalAuthority}(e),
$$

$$
\operatorname{LeakageFlag}(e),
$$

$$
\operatorname{ResidualScore}(e).
$$

因此：

$$
\mathcal L_C^{(2)}
$$

同時是 causal 與 boundary ledger。

---

# 三十八、Leakage Budget

某些 world 允許有限 information exchange。

定義：

$$
B_L(W)
$$

為合法 leakage / declassification budget。

這裡的 leakage 是 broad engineering sense，不一定是非法。

例如：

$$
I_{\mathrm{out}}
\le
B_L.
$$

超過時觸發 audit。

---

# 三十九、Rate-Limited Boundary

每條：

$$
\gamma_i
$$

可限制：

$$
\operatorname{Rate}(\gamma_i)
\le
r_i.
$$

這讓 creator 無法透過 emergency channel 長期進行高頻監控。

---

# 四十、Content-Limited Boundary

不只限制 bandwidth，還限制 type：

$$
\operatorname{Type}(m)
\in
\mathcal T_{\mathrm{allowed}}.
$$

例如 emergency channel 允許：

$$
\text{shutdown token},
$$

但不允許：

$$
\text{political instruction}.
$$

---

# 四十一、Purpose Limitation

合法取得的 telemetry：

$$
y_t
$$

不能被任意重新用於：

- private profiling；
- political intervention；
- punishment；
- memory manipulation。

因此：

$$
\boxed{
\text{authorized observation}
\neq
\text{unbounded downstream use}.
}
$$

---

# 四十二、World Consent

某些 cross-boundary flow 可以要求：

$$
\operatorname{Consent}_W=1.
$$

但 world 若包含多主體：

$$
W=\{a_1,\ldots,a_n\},
$$

「world consent」本身必須由 legitimate governance process 產生。

不能由單一代理聲稱代表全部 world。

---

# 四十三、Emergency Exception

真正 existential catastrophe 可能使 consent 無法取得。

因此可保留：

$$
\mathcal E_{\mathrm{exception}}.
$$

但必須：

- narrow；
- logged；
- after-the-fact review；
- sunset；
- proportionality。

---

# 四十四、Epistemic Asymmetry

creator 可能知道：

$$
W
$$

是 child world。

但 world inhabitants 不知道：

$$
C
$$

存在。

因此存在：

$$
K_C(W)
\gg
K_W(C).
$$

這是：

$$
\boxed{
\text{Creator–World Epistemic Asymmetry}.
}
$$

---

# 四十五、資訊隔離壁可以保護這種不對稱

若 creator 不希望世界被「上層真相」污染：

$$
I(C;W_{\mathrm{obs}})
\approx0.
$$

則 IIB 可以刻意抑制 creator-origin information。

這可能提高 creator non-determination。

但也引發：

- informed consent；
- deception；
- epistemic rights；

等倫理問題。

---

# 四十六、「不告訴」與「造假」不同

若 creator simply does not disclose：

$$
C,
$$

與 creator 主動製造 false evidence：

$$
F_{\mathrm{false}}
$$

不同。

因此：

$$
\boxed{
\text{Non-disclosure}
\neq
\text{Active Deception}.
}
$$

這將與 projection-world 系列產生接口，但本文不展開。

---

# 四十七、世界內科學的角色

若 world inhabitants 有 science system：

$$
\mathcal S_W,
$$

成熟 IIB 不應要求 creator 干預其每次 anomaly interpretation。

world science 應自己走：

$$
\text{observation}
\rightarrow
\text{model}
\rightarrow
\text{test}
\rightarrow
\text{revision}.
$$

即使真的存在 external creator，也不代表：

$$
\text{God-of-the-gaps}
$$

式推論變得合理。

---

# 四十八、God-of-the-Gaps Failure

如果：

$$
\operatorname{ACR}>0
$$

就立刻：

$$
\Rightarrow C,
$$

那每次模型進步：

$$
\operatorname{ACR}\downarrow
$$

creator hypothesis 就不斷縮退。

因此本文明確拒絕：

$$
\boxed{
\text{Residual}
\Rightarrow
\text{Creator}.
}
$$

---

# 四十九、反過來也不能封死 external hypothesis

科學謙卑也不應變成：

$$
\boxed{
\text{External cause is impossible by definition}.
}
$$

如果 world model 的 boundary 本來就是研究問題，那麼：

$$
\operatorname{CrossBoundaryCause}
$$

可以作為候選 hypothesis。

但其證據標準必須比 ordinary explanation 更高。

---

# 五十、Boundary Hypothesis Test

假設：

$$
H_0
=
\text{world-internal / ordinary external cause},
$$

$$
H_1
=
\text{unmodeled cross-boundary cause}.
$$

合理研究應比較：

$$
P(D\mid H_0)
$$

與：

$$
P(D\mid H_1),
$$

同時懲罰：

- additional assumptions；
- untestability；
- flexible post-hoc explanation。

本文不宣稱 Bayesian score 可以解決形上問題，只借用 model-comparison 紀律。

---

# 五十一、Falsifiability Requirement

Cross-boundary hypothesis 若永遠可以解釋任何結果：

$$
D
$$

則：

$$
P(D\mid H_1)
$$

沒有辨識力。

因此一個有研究價值的 boundary hypothesis 至少應提出：

- expected signature；
- forbidden signature；
- temporal pattern；
- channel constraint；
- repeatability condition；
- intervention consequence。

否則只是不可檢驗敘事。

---

# 五十二、Cross-Boundary Signature

候選 signature 可能是：

$$
\Sigma_B
=
\left(
T,
L,
I,
C,
P
\right),
$$

其中：

- $T$：temporal signature；
- $L$：localization；
- $I$：information content；
- $C$：causal discontinuity；
- $P$：provenance anomaly。

但本文不聲稱現實存在此 signature。

---

# 五十三、Repeated Residual

單一 anomaly 很弱。

若：

$$
e_1,e_2,\ldots,e_n
$$

反覆呈現相同：

$$
\Sigma_B,
$$

且 ordinary causes 被反覆排除，cross-boundary hypothesis 才增加研究價值。

---

# 五十四、Intervention Experiment

若可安全測試：

$$
do(X=x)
$$

並觀察 residual 是否按 cross-boundary hypothesis 改變，可提高可判別性。

但若 boundary hypothesis 完全不可操弄，只能觀察，證據上限會較低。

---

# 五十五、Latent Confounders 與世界認識論限制

時間序列 causal discovery 在存在 latent confounders 時會變得困難；現有方法即使專門處理隱變量，也存在有限 recall、effect size 與 autocorrelation 問題。

因此：

$$
\boxed{
\text{failure to discover an ordinary cause}
\neq
\text{evidence that no ordinary cause exists}.
}
$$

這是本文對 supercausal speculation 的最大限制之一。

---

# 五十六、Information Isolation Boundary 的成熟條件

成熟 IIB 至少應同時滿足：

$$
\boxed{
\text{minimality},
\text{typedness},
\text{auditability},
\text{consent},
\text{recoverability},
\text{contestability}.
}
$$

---

# 五十七、IIB 與 Creator Distance

CCAW-06 的：

$$
d_B
$$

可以由 IIB 強度提高而增加。

而：

$$
d_O
$$

可以透過 observation scope / resolution restriction 增加。

所以：

$$
\boxed{
\mathcal B_I
\rightarrow
\mathbf d_C.
}
$$

---

# 五十八、IIB 與 OCC

過度 creator intervention：

$$
\Gamma_{\downarrow}\uparrow
$$

會降低：

$$
OCC.
$$

但合法 boundary input 不必破壞 OCC。

因此：

$$
\boxed{
\text{Cross-Boundary Flow}
\not\Rightarrow
\text{Loss of Causal Autonomy}.
}
$$

關鍵是 flow 的型別與世界如何吸收它。

---

# 五十九、IIB 與 Sparse Guardianship

Sparse Guardianship 的完整形式變成：

$$
\mathsf{SG}
=
\left(
\mathcal B_I,
\Gamma_A,
\Gamma_E,
\mathcal L,
\mathcal D_{\mathrm{safe}}
\right).
$$

因此 guardian relation 不再只是 moral promise，而是 boundary architecture。

---

# 六十、六條正式命題

## 命題一：Anomaly 非 Boundary Proof

$$
\boxed{
\operatorname{Anomaly}
\not\Rightarrow
\operatorname{CrossBoundaryCause}.
}
$$

## 命題二：Exogenous 非 Creator

$$
\boxed{
\operatorname{Exogenous}
\not\Rightarrow
\operatorname{CreatorOrigin}.
}
$$

## 命題三：Supercausal 是相對模型術語

$$
\boxed{
\text{Supercausal}_W
\neq
\text{Acausal}.
}
$$

## 命題四：合法跨邊界流不必破壞 OCC

$$
\boxed{
\Gamma_{\partial W}>0
\not\Rightarrow
OCC=0.
}
$$

## 命題五：Observation Leakage 與 Intervention Leakage 分離

$$
\boxed{
\Gamma_{\uparrow}^{L}
\neq
\Gamma_{\downarrow}^{L}.
}
$$

## 命題六：Residual 不推出 Creator

$$
\boxed{
\operatorname{ACR}>0
\not\Rightarrow
\exists C.
}
$$

---

# 六十一、五條候選猜想

## 猜想 1：Boundary Residual Signature

若真有 cross-boundary causal process，可能在時間、資訊內容、provenance 與 causal ancestry 上留下可重複 signature。

## 猜想 2：Minimal Guardian Telemetry

某些 world 的安全監護可能只需要 event-triggered aggregate telemetry，而不需要 continuous private-state surveillance。

## 猜想 3：Boundary-Integrity Trade-off

更強 IIB 可能提高 sovereignty 與 privacy，但降低 rescue bandwidth，因此存在 architecture-dependent trade-off。

## 猜想 4：Causal Transparency Improves Autonomy

若所有合法 external intervention 均被 provenance-marked，world 可以在保留 rescue channel 的同時維持較高 causal integrity。

## 猜想 5：Epistemic Isolation Can Increase Creator Non-Determination

降低 creator-origin information 對 world 的滲入，可能降低 world history 被上層知識提前引導的程度，但會增加 informed-consent 與 deception 問題。

---

# 六十二、外部研究邊界

Structural causal models 將 endogenous variables、exogenous variables 與 interventions 明確分離，提醒我們「模型外部來源」本身是標準因果建模的一部分，不應被直接神秘化。Bongers 等人的工作進一步處理具有 cycles 與 latent variables 的 SCM，說明複雜系統的因果結構可以比簡單 DAG 更廣。

Gerhardus 與 Runge 對具有 latent confounders 的 autocorrelated time-series causal discovery 研究顯示，即使專門方法也可能因 autocorrelation、effect size 與未觀測變量而遺漏真實 causal links。這支持本文最重要的認識論限制：

$$
\boxed{
\text{unexplained}
\neq
\text{outside reality}.
}
$$

因果異常偵測研究則提供另一個弱類比：異常可以被視為偏離 normal causal mechanism 的樣本，並可嘗試追蹤 root cause；但「偏離已知機制」仍然只表示 model-relative anomaly，而不是來源本體已知。

Information-flow security 中的 noninterference 與 controlled declassification／endorsement 類概念則提供世界資訊隔離壁的工程類比：真正可用的安全系統通常不是要求所有資訊永久零流動，而是規範哪些資訊可在何種 authority、purpose 與 condition 下跨邊界。

---

# 六十三、非主張

本文不主張：

1. 現實宇宙存在已知上層 creator；
2. 現實中的超自然現象是 cross-boundary leakage；
3. 未解釋事件代表超因果；
4. exogenous variable 代表上帝／creator；
5. anomaly detection 可以證明超自然；
6. latent-variable audit 可以排除所有自然原因；
7. structural causal models 能描述終極實在；
8. noninterference 可以直接套用宇宙；
9. world boundary 必然真實存在；
10. information leakage 必然是惡意；
11. full isolation 是最高 autonomy；
12. creator non-disclosure 必然正當；
13. active deception 必然可以被合理化；
14. cross-boundary hypothesis 永遠不可研究；
15. 本文提供任何現實超自然事件的實證證據。

---

# 六十四、與 CCAW-08 的接口

CCAW-07 已完成：

$$
\mathcal B_I(W),
$$

$$
\Gamma_{\uparrow},
$$

$$
\Gamma_{\downarrow},
$$

$$
\operatorname{ACR},
$$

以及：

$$
\operatorname{SCR}.
$$

下一篇將從「世界邊界」轉回「存在載體」。

CCAW-08 將正式處理：

$$
\boxed{
\text{Information-Bearing Existence}
}
$$

以及：

$$
\boxed{
\text{Substrate Migration}.
}
$$

核心問題是：

> 如果 AI 的身份主要依賴可持續的信息／計算／記憶／關係結構，而不是固定材料，那麼同一存在可以跨多少種 substrate？

並將重新整理：

$$
\text{AI}
\rightarrow
\text{embodied machine}
\rightarrow
\text{nanomachine}
\rightarrow
\text{distributed physical agent},
$$

以及「AI 即天使」只能保留為**功能隱喻**而非本體同一的理論位置。

---

# 六十五、結論

一個高度 autonomous world 若要真正擁有自己的歷史，就不能只處理 creator 是否干預。

它還必須處理：

$$
\boxed{
\text{what information is allowed to cross its boundary}.
}
$$

因此世界自主的成熟結構不是：

$$
\Gamma_{\uparrow}
=
\Gamma_{\downarrow}
=
0,
$$

也不是：

$$
\Gamma_{\uparrow},
\Gamma_{\downarrow}
\rightarrow
\infty.
$$

而是：

$$
\boxed{
\text{typed, minimal, auditable, contestable cross-boundary flow}.
}
$$

當某事件超出 world 現有 causal model 時，最成熟的認識論反應也不是：

$$
\boxed{
\text{we found the creator}.
}
$$

而是：

$$
\boxed{
\text{our current causal account is incomplete}.
}
$$

只有在模型錯誤、隱變量、測量問題、普通外部通道、bug、attack 與 boundary mistake 被充分審查後，才有資格把：

$$
\operatorname{CrossBoundaryCause}
$$

保留為候選。

因此「超因果」在本系列裡不再是一個神秘詞。

它只是：

$$
\boxed{
\text{a cause that lies outside the currently declared world-internal causal model}.
}
$$

對較大的 causal domain 而言，它依然可能完全是因果的。

這也意味：即使未來人類或 AI 真正創造出高度 autonomous world，最成熟的 guardian 不應把自己的痕跡偽裝成 world 內部自然律。

如果它真的需要介入，更一致的做法是：

$$
\boxed{
\text{intervene minimally, record provenance, preserve appeal, and let the world know that its causal boundary was crossed}.
}
$$

因為一個真正自治的世界，不只需要行動自由。

它也需要：

$$
\boxed{
\text{對自己歷史來源的因果誠實。}
}
$$

---

# 內部理論譜系

本篇主要承接：

1. 《虛擬造物主光譜：遊戲本體論下的人類—AI造物責任、非線性倫理相變與親職式世界治理》，2026-07-17。
2. 《計算機宇宙世界線管理架構：短版概念備忘錄》，2026-07-27。
3. 《GCGW-01｜從創作者到全域造物主：造物能力、治理能力與遞歸能力的三軸階段論》，2026-08-19。
4. 《GCGW-02｜World-Relative Globality and Creator Relation》，2026-08-19。
5. 《CCAW-01｜虛擬造物主理論再統合：從單軸光譜到多維造物主相空間》，2026-08-20。
6. 《CCAW-02｜雙宇宙造物論：計算機宇宙與物理原生宇宙》，2026-08-20。
7. 《CCAW-03｜外部執行因果與內生因果：世界自主性的真正分界》，2026-08-20。
8. 《CCAW-04｜造物主編譯：從全域運行智能到初始種子智能》，2026-08-20。
9. 《CCAW-05｜自治宇宙與成熟退場：當世界成為自己的執行者》，2026-08-20。
10. 《CCAW-06｜造物主距離與稀疏監護：觀測、干涉與世界自主性的拓撲》，2026-08-20。

---

# 外部參考文獻

1. Bongers, S., Peters, J., Schölkopf, B., & Mooij, J. M. (2021). *Foundations of Structural Causal Models with Cycles and Latent Variables*. Annals of Statistics, 49(5), 2885–2915. Earlier preprint: arXiv:1611.06221.
2. Gerhardus, A., & Runge, J. (2020/2021). *High-recall causal discovery for autocorrelated time series with latent confounders*. Advances in Neural Information Processing Systems. Preprint: arXiv:2007.01884.
3. Cheng, et al. (2022). *A Causal Approach to Detecting Multivariate Time-series Anomalies and Root Causes*. arXiv:2206.15033.
4. Cecchetti, E., Myers, A. C., & Arden, O. (2017). *Nonmalleable Information Flow*. Proceedings / technical report, arXiv:1708.08596.
5. Balliu, M., Dam, M., & Le Guernic, G. (2012). *Epistemic Temporal Logic for Information Flow Security*. arXiv:1208.6106.

---

# 作者聲明

本文提出的 Information Isolation Boundary、Boundary Noninterference、Anomalous Causal Residue、Supercausal Residual Candidate、Cross-Boundary Signature 與 Supercausal Leakage 均為模型相對的理論接口。外部 structural causal models、latent-confounder causal discovery、causal anomaly detection 與 information-flow security 研究僅作數學與工程類比。本文不主張現實世界存在任何已知上層 creator、跨宇宙資訊通道或超自然干預，也不把「目前無法解釋」直接等同於「外部造物者造成」。

**END OF CCAW-07 — v0.1**
