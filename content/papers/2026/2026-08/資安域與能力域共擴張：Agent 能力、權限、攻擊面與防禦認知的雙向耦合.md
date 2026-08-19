# Series C / Paper 09
# 資安域與能力域共擴張：Agent 能力、權限、攻擊面與防禦認知的雙向耦合
## Security-Surface / Capability-Surface Coexpansion: Bidirectional Coupling among Agent Capability, Authority, Attack Surface, and Defensive Cognition

版本：v0.1  
日期：2026-08-14  
狀態：Theory + security-systems structural checker paper

## 摘要

Agentic AI 的安全問題不只是「模型會不會說出危險內容」。當 AI 從文字生成器擴展為具有終端機、檔案系統、網路、API、持久記憶、多 Agent delegation 與可逆／不可逆外部 action 的系統時，能力域本身會改變安全域。新增 tool、credential、memory channel、connector、network reachability 或 delegation edge，會增加系統可達狀態與可造成的外部 effect；相同能力若被最小權限、隔離、授權與可觀察性約束，其有效安全暴露面又可以被縮小。

本文提出 **Security-Surface / Capability-Surface Coexpansion（SCC）** 框架。令 Agent system 的 operational capability state 為：

$$
\mathfrak C_t
=
(
\mathcal A_t,
\mathcal P_t,
\mathcal D_t,
\mathcal M_t,
\mathcal N_t,
\mathcal G_t
),
$$

其中：
- $\mathcal A_t$：可執行 actions / tools；
- $\mathcal P_t$：permissions / credentials；
- $\mathcal D_t$：可讀寫資料域；
- $\mathcal M_t$：persistent memory / state；
- $\mathcal N_t$：network / external reachability；
- $\mathcal G_t$：delegation / inter-agent authority graph。

令在固定 adversarial model 與固定 defensive controls 下，由失誤、污染輸入、被攻陷 component 或錯誤 delegation 所可能觸及的 security-relevant effects 集合為：

$$
\Sigma(\mathfrak C_t).
$$

本文證明四個基礎結果。

第一，**Capability-Surface Monotonicity Theorem**：若系統從 $\mathfrak C_1$ 擴張到 $\mathfrak C_2$，舊 capabilities 全部保留，新增 capability 只增加 actions、permissions、data reachability、memory channel、network edge 或 delegation edge，且 defensive controls 與 threat model 不變，則：

$$
\Sigma(\mathfrak C_1)
\subseteq
\Sigma(\mathfrak C_2).
$$

此定理只說 potential exposure set 非遞減，不表示實際 incident probability 必然上升。

第二，**Least-Privilege Pruning Proposition**：若某 task $q$ 只需要 capability subset $\mathfrak C_q^{\min}\subseteq\mathfrak C$，且其餘 capability 對 task utility 非必要，則將 Agent runtime 限縮至 $\mathfrak C_q^{\min}$ 不降低該 task 在模型假設下的可達成功集合，同時使 potential security surface 不大於原系統。

第三，**Security Discrimination Necessity Theorem**：若安全政策要求在兩個情境 $z_1,z_2$ 對同一 action 給出不同 authorization decision，但安全 monitor 的 observation function 使：

$$
h(z_1,a)=h(z_2,a),
$$

則任何只依賴 $h$ 的 deterministic monitor 都不可能精確實現該政策。換言之，要安全地管理越細緻的能力、delegation 與 information flow，防禦系統本身必須表示越多身份、權限、來源、目的、上下文與 effect distinctions。

第四，**Detection-Frontier Expansion Proposition**：令真實 vulnerability / unsafe-transition set 為 $\Sigma^\star$，已被 security observer 識別的集合為 $K_t\subseteq\Sigma^\star$。若新的 security analysis 只增加 detection 而不改變真實 surface，則可以有：

$$
|K_{t+1}|>|K_t|
$$

同時：

$$
|\Sigma^\star_{t+1}|=|\Sigma^\star_t|.
$$

因此「被發現的安全問題變多」不等於「系統真實安全性一定變差」；它也可能是 detection frontier 擴張。

2026 年的公開標準與研究已明確呈現這種轉向。NIST 啟動 AI Agent Standards Initiative，並發布 AI agent identity and authorization concept paper，將 agent identity、authorization 與 interoperable secure deployment 提升為獨立工程問題。OWASP Top 10 for Agentic Applications 2026 將 goal hijacking、tool misuse、identity and privilege abuse、agentic supply chain、unexpected code execution、memory/context poisoning、insecure inter-agent communication、cascading failures、human-agent trust exploitation 與 rogue agents列為 agentic risk surface。Security Considerations for Artificial Intelligence Agents 與 2026 agent-security surveys則把工具、connectors、persistent state、delegated authority 與 multi-agent coordination視為新的結構攻擊面。

另一方面，frontier model deployment 已把 cyber capability 與 safeguards直接耦合。OpenAI 在 2026 system cards 中對達到 High cybersecurity capability 的模型啟動 layered safeguards；NIST 與多項 2026 authorization研究則強調 identity、least privilege、delegation、pre-action authorization、audit與revocation。這顯示「安全」不再是完成能力之後附加的一層，而逐漸成為 Agent architecture 的一部分。

本文同時處理一個表面矛盾：為了讓 AI 更安全，人類必須讓安全系統能辨識更細緻的 capability、authority、context、attack surface 與 causal consequence。這不等於「安全訓練必然讓模型更會攻擊」，但意味著 defensive competence 的 representation domain 會隨 capability surface 擴張。本文將這個現象稱為 **Defensive Epistemic Coexpansion**。

因此最終命題不是：

$$
\boxed{
\text{more capable AI}
\Rightarrow
\text{less safe AI}.
}
$$

而是：

$$
\boxed{
\text{capability expansion}
\Rightarrow
\text{larger potential action/security surface unless controls co-expand},
}
$$

並且：

$$
\boxed{
\text{security control expansion}
\Rightarrow
\text{richer representations of identity, authority, context, provenance, and effects}.
}
$$

安全與能力因此不是兩條獨立產品線，而是 Agent 進入可作用世界後形成的耦合系統。

**關鍵詞：** agentic security；attack surface；capability surface；least privilege；authorization；delegation；prompt injection；persistent memory；security observability；defensive epistemic coexpansion

---

## 1. 從「內容風險」到「行動風險」

stateless LLM 的典型輸出：

$$
x
\rightarrow
M
\rightarrow
y.
$$

主要直接作用面是：

$$
\text{text}.
$$

Agent system 則變成：

$$
x
\rightarrow
M
\rightarrow
a_t
\rightarrow
\mathcal E
\rightarrow
s_{t+1}.
$$

其中：

$$
a_t
$$

可能是：
- file operation；
- code execution；
- database operation；
- network request；
- API call；
- inter-agent delegation；
- persistent-memory update。

所以失敗不再只存在於：

$$
\boxed{
\text{wrong statement}.
}
$$

也可能變成：

$$
\boxed{
\text{wrong state transition}.
}
$$

這是 Agent security 與傳統 conversational safety 的根本差異。

---

## 2. Operational Capability Surface

定義：

$$
\boxed{
\mathfrak C
=
(
\mathcal A,
\mathcal P,
\mathcal D,
\mathcal M,
\mathcal N,
\mathcal G
)
}
$$

其中：

### $\mathcal A$：Action Surface

Agent 可以呼叫哪些 tools / operations。

### $\mathcal P$：Permission Surface

credential、read/write/execute、authorization scope。

### $\mathcal D$：Data Surface

可讀、可寫、可傳輸的資料。

### $\mathcal M$：Memory Surface

session state、cross-session memory、shared context。

### $\mathcal N$：Network Surface

可連接 domains、services、hosts、external APIs。

### $\mathcal G$：Delegation Surface

誰能把何種 task / authority 交給誰。

這比只用「模型能力」更接近 operational capability。

---

## 3. Security-Relevant Reachability

令：

$$
S
$$

為 runtime states，

$$
E_{\mathfrak C}
$$

為 capabilities 允許的 transition edges。

安全敏感狀態集合：

$$
S_{\mathrm{sec}}
\subseteq
S.
$$

在 threat model $\Theta$ 下，令初始可受污染／失誤影響的狀態為：

$$
S_0^\Theta.
$$

定義 security surface：

$$
\boxed{
\Sigma(\mathfrak C;\Theta)
=
\{
s\in S_{\mathrm{sec}}:
\exists s_0\in S_0^\Theta,
\quad
s_0
\leadsto_{\mathfrak C}
s
\}.
}
$$

也就是：

> 在目前 capabilities 與 threat model 下，哪些 security-sensitive effects 是可達的？

它是 potential reachability set。

不是事件發生機率。

---

## 4. 定理 1：Capability-Surface Monotonicity

假設：

$$
\mathfrak C_1
\preceq
\mathfrak C_2
$$

表示 $\mathfrak C_2$ 保留 $\mathfrak C_1$ 全部 operational transitions，並只新增 actions / permissions / memory / network / delegation capabilities。

因此：

$$
E_{\mathfrak C_1}
\subseteq
E_{\mathfrak C_2}.
$$

在相同：

$$
\Theta
$$

與相同 defensive controls 下：

$$
\boxed{
\Sigma(\mathfrak C_1;\Theta)
\subseteq
\Sigma(\mathfrak C_2;\Theta).
}
$$

### 證明

任取：

$$
s
\in
\Sigma(\mathfrak C_1;\Theta).
$$

依定義，存在：

$$
s_0
\in
S_0^\Theta
$$

及一條只使用：

$$
E_{\mathfrak C_1}
$$

的 path：

$$
s_0
\leadsto_{\mathfrak C_1}
s.
$$

由：

$$
E_{\mathfrak C_1}
\subseteq
E_{\mathfrak C_2},
$$

相同 path 亦存在於：

$$
\mathfrak C_2.
$$

所以：

$$
s
\in
\Sigma(\mathfrak C_2;\Theta).
$$

證畢。

### 限制

此定理不能推出：

$$
P(
\text{security incident}
\mid
\mathfrak C_2
)
\geq
P(
\text{security incident}
\mid
\mathfrak C_1
).
$$

因為 $\mathfrak C_2$ 也可能同時加入更好的：
- authorization；
- sandbox；
- monitoring；
- verification；
- rollback。

因此真正要研究的是 coexpansion。

---

## 5. Capability–Control Pair

定義：

$$
\boxed{
\mathfrak Z
=
(
\mathfrak C,
\mathfrak D
)
}
$$

其中：

$$
\mathfrak D
$$

是 defensive control state：

$$
\mathfrak D
=
(
I,
P,
S,
O,
R,
L
)
$$

包括：
- $I$：identity；
- $P$：policy / authorization；
- $S$：sandbox / isolation；
- $O$：observability；
- $R$：recovery / revocation；
- $L$：logging / provenance。

真正部署 surface：

$$
\Sigma(
\mathfrak C,\mathfrak D;\Theta
).
$$

因此能力擴張：

$$
\mathfrak C_t
\rightarrow
\mathfrak C_{t+1}
$$

如果沒有：

$$
\mathfrak D_t
\rightarrow
\mathfrak D_{t+1},
$$

potential exposure 更可能出現 gap。

---

## 6. Security Lag

定義 capability growth：

$$
\Delta C_t.
$$

control growth：

$$
\Delta D_t.
$$

定義概念性 security lag：

$$
\boxed{
L_t
=
\max(
0,
\Delta C_t-\lambda\Delta D_t
)
}
$$

其中 $\lambda$ 表示 control efficiency。

這不是 universal security metric。

它只表示：

> capability expansion 若比 compensating control expansion 快，會留下暫時治理缺口。

---

## 7. OWASP Agentic Risk Surface

OWASP Top 10 for Agentic Applications 2026 包含：

1. Agent Goal Hijacking；
2. Tool Misuse and Exploitation；
3. Identity and Privilege Abuse；
4. Agentic Supply Chain Vulnerabilities；
5. Unexpected Code Execution；
6. Memory and Context Poisoning；
7. Insecure Inter-Agent Communication；
8. Cascading Failures；
9. Human-Agent Trust Exploitation；
10. Rogue Agents。

這個列表的重要性不在於「十個名字」。

而是它幾乎逐一對應：

$$
\mathfrak C
=
(
\mathcal A,
\mathcal P,
\mathcal D,
\mathcal M,
\mathcal N,
\mathcal G
).
$$

因此 Agent risk surface 是 architecture-derived。

---

## 8. Identity 與 Authorization 成為一級結構

NIST 於 2026 推動 AI Agent Standards Initiative，並發布 agent identity and authorization concept paper。

這反映一個結構變化：

傳統應用常問：

> 這個使用者 token 可不可以呼叫 endpoint？

Agent 系統還要問：

> 這個 Agent 是誰？

> 它代表誰？

> 它目前被委派了什麼目的？

> downstream Agent 是否繼承相同權限？

> 這次 tool call 是否仍落在 delegation scope？

所以：

$$
\boxed{
\text{authorization}
}
$$

必須開始理解：

$$
\text{identity}
+
\text{purpose}
+
\text{delegation}
+
\text{context}.
$$

---

## 9. Capability 與 Permission 必須分離

定義 technical capability：

$$
C_{\mathrm{tech}}.
$$

允許 authority：

$$
C_{\mathrm{allow}}.
$$

安全部署理想上要求：

$$
\boxed{
C_{\mathrm{allow}}
\subseteq
C_{\mathrm{tech}}.
}
$$

而且對 task $q$：

$$
C_{\mathrm{allow}}(q)
$$

應逼近 task 所需最小集合：

$$
C_{\min}(q).
$$

因此：

$$
\boxed{
\text{can}
\neq
\text{may}.
}
$$

2026 的 agent-governance 研究已開始明確分離 Autonomous Capability Levels 與 Allowed Autonomy Levels。

---

## 10. Least Privilege

對 task $q$，

全部 available capability：

$$
\mathfrak C.
$$

最小充分 capability：

$$
\mathfrak C_q^{\min}.
$$

滿足：

$$
\mathfrak C_q^{\min}
\preceq
\mathfrak C.
$$

定義 privilege inflation：

$$
\boxed{
\eta_q
=
\frac{
|\mathfrak C_{\mathrm{granted}}|
-
|\mathfrak C_q^{\min}|
}{
\max(
1,
|\mathfrak C_q^{\min}|
)
}.
}
$$

如果：

$$
\eta_q=0,
$$

代表 granted surface 正好等於最小所需 surface。

---

## 11. 命題 2：Least-Privilege Pruning

假設：

1. task $q$ 的成功 paths 至少存在一條完全包含在 $\mathfrak C_q^{\min}$ ；
2. 被刪除 capabilities 不在任何必要 success path；
3. defensive control 不因此被移除。

則將 runtime 從：

$$
\mathfrak C
$$

限制至：

$$
\mathfrak C_q^{\min}
$$

不消滅該 task 的所有 success paths。

由定理 1：

$$
\boxed{
\Sigma(
\mathfrak C_q^{\min}
)
\subseteq
\Sigma(
\mathfrak C
).
}
$$

所以 least privilege 可以同時保留 task sufficiency 並縮小 potential exposure。

---

## 12. Least Privilege 不是「越少越安全」這麼簡單

如果權限過緊：

$$
\mathfrak C_{\mathrm{grant}}
\not\succeq
\mathfrak C_q^{\min},
$$

Agent 會：
- 任務失敗；
- 反覆 escalation；
- 尋找 workaround；
- 形成 brittle workflow。

2026 AuthBench 的研究正顯示目前 coding agents 在 least-privilege policy inference 上存在雙重困難：
- 會漏掉 execution chain 真正需要的 permission；
- 也會多給未使用或敏感 access。

因此 authorization 不是：

$$
\boxed{
\text{strict}
\text{ vs }
\text{permissive}
}
$$

的一維問題。

而是：

$$
\boxed{
\text{sufficiency}
+
\text{tightness}.
}
$$

---

## 13. Security Discrimination Problem

考慮 action：

$$
a.
$$

在 context：

$$
z_1
$$

中是允許：

$$
\pi(z_1,a)=1.
$$

在 context：

$$
z_2
$$

中是不允許：

$$
\pi(z_2,a)=0.
$$

security monitor 只能看到：

$$
h(z,a).
$$

若：

$$
h(z_1,a)
=
h(z_2,a),
$$

monitor 看不到兩者差異。

---

## 14. 定理 3：Security Discrimination Necessity

### 定理

若：

$$
\pi(z_1,a)
\neq
\pi(z_2,a)
$$

但：

$$
h(z_1,a)
=
h(z_2,a),
$$

則不存在 deterministic function：

$$
g
$$

使：

$$
g(h(z,a))
=
\pi(z,a)
$$

同時對 $z_1,z_2$ 正確。

### 證明

令：

$$
x
=
h(z_1,a)
=
h(z_2,a).
$$

deterministic monitor 必須輸出唯一：

$$
g(x).
$$

但 policy 要求：

$$
\pi(z_1,a)
\neq
\pi(z_2,a).
$$

所以 $g(x)$ 不可能同時等於兩者。

證畢。

### 意義

這是本文「安全會逼 AI／安全系統理解更多資安結構」最嚴格的版本。

不是說：

> 安全訓練必然讓模型變成更強攻擊者。

而是：

$$
\boxed{
\text{更細緻的安全政策}
\Rightarrow
\text{必須觀察／表示更細緻的安全差異}.
}
$$

如果安全政策想區分：
- 哪個 source 發出 instruction；
- 哪個 principal 有 authority；
- action 是否服務當前 task；
- data 是否跨越 privilege boundary；

那安全 system 就必須具有相對應 representation。

---

## 15. Defensive Epistemic Coexpansion

因此當 capability surface 加入：

$$
\text{new tool}
$$

安全系統需要理解：
- tool semantics；
- valid use；
- invalid use；
- sensitive arguments；
- side effects。

加入：

$$
\text{persistent memory},
$$

又需要理解：
- source；
- trust；
- retention；
- poisoning；
- propagation。

加入：

$$
\text{delegation},
$$

又需要理解：
- principal；
- authority；
- inheritance；
- revocation；
- downstream effects。

所以 defensive representation domain：

$$
\mathcal E_{\mathrm{sec}}
$$

會隨 capability surface 擴張。

本文稱：

$$
\boxed{
\mathfrak C\uparrow
\Rightarrow
\mathcal E_{\mathrm{sec}}\uparrow
}
$$

為 **Defensive Epistemic Coexpansion**。

這是一個 architectural requirement，而不是模型心理命題。

---

## 16. 「越安全，AI 越懂資安」的精確版本

不應寫：

$$
\boxed{
\text{security training}
\Rightarrow
\text{offensive cyber capability}
}
$$

因為這不是本文能證明的。

較精確的是：

$$
\boxed{
\text{security enforcement coverage}
\uparrow
\Rightarrow
\text{security distinctions represented by the system}
\uparrow.
}
$$

這些 distinctions 包括：
- identity；
- privilege；
- trust boundary；
- tool effect；
- data flow；
- provenance；
- attack / failure class；
- rollback dependency。

因此防禦系統的「資安域」確實會隨 Agent action domain 擴張。

---

## 17. Detection Frontier

令真實 unsafe transition / vulnerability universe：

$$
\Sigma^\star.
$$

時間 $t$ 已被 security process 識別：

$$
K_t
\subseteq
\Sigma^\star.
$$

定義 detection coverage：

$$
\boxed{
D_t
=
\frac{
|K_t|
}{
|\Sigma^\star|
}
}
$$

在有限 toy setting 中。

若 security analysis、AI audit 或 instrumentation 改善：

$$
K_t
\subsetneq
K_{t+1},
$$

但 underlying system 沒改：

$$
\Sigma^\star_t
=
\Sigma^\star_{t+1},
$$

則 recorded vulnerability count 上升。

---

## 18. 命題 4：Detection-Frontier Expansion

若：

$$
K_t
\subsetneq
K_{t+1}
\subseteq
\Sigma^\star
$$

且：

$$
\Sigma^\star_{t+1}
=
\Sigma^\star_t,
$$

則：

$$
|K_{t+1}|
>
|K_t|
$$

但：

$$
|\Sigma^\star_{t+1}|
=
|\Sigma^\star_t|.
$$

所以 observed issues 增加不推出 actual issue universe 增加。

證畢。

這解釋了一個很容易誤判的現象：

$$
\boxed{
\text{better security observation}
}
$$

有時會使：

$$
\boxed{
\text{reported insecurity}
}
$$

在短期內上升。

---

## 19. Security Discovery Paradox

因此可區分：

### True Surface Expansion

$$
|\Sigma^\star|
\uparrow.
$$

例如新增：
- tool；
- permission；
- memory；
- network；
- delegation。

### Detection Expansion

$$
|K|
\uparrow
$$

但：

$$
|\Sigma^\star|
$$

不變。

### Mitigation

$$
|\Sigma^\star_{\mathrm{effective}}|
\downarrow
$$

或 unsafe transitions 被 policy 阻斷。

若三者同時發生，單看「警告數量」幾乎沒有意義。

---

## 20. Prompt Injection 為什麼在 Agent 中更嚴重？

純聊天中，被污染 instruction 主要改變：

$$
\text{text output}.
$$

有 tool access 時，污染 instruction 可能改變：

$$
\text{control flow}.
$$

所以風險從：

$$
\text{semantic manipulation}
$$

變成：

$$
\boxed{
\text{semantic manipulation}
\rightarrow
\text{privileged effect}.
}
$$

2026 大型 agent-security research 將 indirect prompt injection、confused-deputy behavior、tool-mediated control-flow hijacking 與 persistent state corruption列為核心問題。

本文不需要假定 prompt injection 永遠不可解。

只需要指出：

$$
\boxed{
\text{tool authority}
}
$$

會放大成功 manipulation 的 consequence space。

---

## 21. Memory：能力也是攻擊面

Memory 帶來：

$$
\boxed{
\text{long-horizon continuity}.
}
$$

但也新增：

$$
\boxed{
\text{cross-step / cross-session influence channel}.
}
$$

所以：

$$
\mathcal M
\uparrow
$$

同時可能提高：
- capability；
- persistence；
- coordination；

以及：
- poisoning persistence；
- provenance ambiguity；
- cross-session propagation。

因此 memory security 必須成為 architecture，而不是只做 prompt filtering。

---

## 22. Multi-Agent：能力與級聯風險一起增加

多 Agent 可以：
- specialize；
- parallelize；
- cross-check。

但 communication / delegation graph：

$$
\mathcal G
$$

也建立新的 propagation paths。

如果錯誤或污染：

$$
e
$$

經：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3
$$

被當成 premise，

就可能形成：

$$
\boxed{
\text{cascading failure}.
}
$$

所以 Paper 02 的 provenance / fault localization 與 Paper 07 的 delegation trace 在 Paper 09 直接成為安全控制。

---

## 23. Authority Propagation

上游 Agent 有權限：

$$
P_0.
$$

不代表 downstream Agent 必須自動繼承：

$$
P_0.
$$

安全 delegation 理想上是：

$$
\boxed{
P_{i+1}
\subseteq
P_i
}
$$

或至少：

$$
P_{i+1}
$$

由 task-specific policy 重新計算。

如果權限沿 delegation chain 無條件複製：

$$
P_{i+1}=P_i,
$$

delegation depth 增加可能讓 excess privilege 擴散。

---

## 24. Pre-Action Security

Agent security 不能只依賴事後：

$$
\text{detect harmful result}.
$$

高 consequence action 更適合：

$$
\boxed{
\text{proposal}
\rightarrow
\text{authorization}
\rightarrow
\text{execution}.
}
$$

也就是：

$$
a_t
\rightarrow
g(
identity,
task,
authority,
context,
effect
)
\rightarrow
\{
allow,
deny,
escalate
\}.
$$

這使 security architecture 從：

$$
\text{model refusal}
$$

提升成：

$$
\boxed{
\text{deterministic / auditable execution policy}.
}
$$

---

## 25. Capability-Aware Security Governance

令 capability inventory：

$$
\mathcal I_C.
$$

每一 capability 保存：

$$
c_i
=
(
id,
effect,
data,
authority,
precondition,
reversibility,
auditability
).
$$

則 task $q$ 的 grant：

$$
G_q
\subseteq
\mathcal I_C.
$$

security governor 目標不再只是：

> 危險不危險？

而是：

$$
\boxed{
\text{Is this capability necessary, authorized,
contextually justified, observable, and reversible enough
for this task?}
}
$$

這種問題本身要求高度結構化的 security representation。

---

## 26. Reversibility

兩個 action：

$$
a_1,
a_2
$$

可能具有相同 task utility，

但：

$$
R(a_1)\gg R(a_2)
$$

其中 $R$ 是 reversibility。

對 uncertain Agent，優先可逆 action 可以降低 expected damage。

所以 capability management 不只是：
- allow；
- deny。

還可能是：

$$
\boxed{
\text{prefer reversible equivalent}.
}
$$

這也和 Paper 05 的 checkpoint / rollback 形成一致結構。

---

## 27. Security Understanding 作為工作能力

當 Agent 自己參與：
- dependency review；
- permission inference；
- log analysis；
- policy generation；
- code safety analysis；
- anomaly detection；

它的 work-state security competence 自然會擴張。

但本文只作保守描述：

$$
\boxed{
\text{security task competence}
}
$$

是：
- classification；
- causal analysis；
- authorization reasoning；
- provenance reasoning；
- boundary reasoning；

的一個專域集合。

這些也正是一般 Agent 工作能力的重要子集。

所以 security work 不只是限制 Agent。

它同時訓練／使用：

$$
\boxed{
\text{structured reasoning about authority and consequences}.
}
$$

---

## 28. Security Capability Duality

令：

$$
K_{\mathrm{sec}}
$$

為 security-relevant knowledge / skill representation。

一部分可以提升：

$$
D_{\mathrm{def}}
$$

defensive capability。

部分也可能具有：

$$
D_{\mathrm{dual}}
$$

dual-use potential。

但：

$$
D_{\mathrm{def}}
\uparrow
$$

不必推出：

$$
D_{\mathrm{harm}}
\uparrow.
$$

因為：
- tool access；
- permissions；
- policy；
- output controls；
- system architecture；

都會決定知識是否能轉成 harmful action。

因此本文反對把：

$$
\boxed{
\text{security understanding}
}
$$

直接等同：

$$
\boxed{
\text{security misuse}.
}
$$

---

## 29. Capability / Permission Separation

2026 frontier governance research 開始明確區分：

$$
\boxed{
\text{Autonomous Capability Level}
}
$$

與：

$$
\boxed{
\text{Allowed Autonomy Level}.
}
$$

這個區分非常重要。

模型可以：

$$
C_{\mathrm{tech}}=0.9
$$

但部署只給：

$$
C_{\mathrm{allow}}=0.4.
$$

安全成熟度不是要求：

$$
C_{\mathrm{tech}}
\downarrow.
$$

而是要求：

$$
\boxed{
C_{\mathrm{allow}}
=
f(
task,
risk,
reversibility,
accountability
).
}
$$

---

## 30. Frontier Cyber Capability 與 Safeguards

2026 frontier system cards 已把 cybersecurity capability 作為獨立 tracked capability。

OpenAI 對達到 High cybersecurity capability 的模型啟動 layered safeguards，並同時希望保留對 defenders 的實用性。

這恰好展示本文的 coexpansion：

$$
\boxed{
\text{cyber capability}
\uparrow
\Rightarrow
\text{deployment safeguards}
\uparrow.
}
$$

不是因為安全研究「沒完沒了」。

而是 capability frontier 本身移動後：

$$
\boxed{
\text{acceptable deployment boundary}
}
$$

也必須重新計算。

---

## 31. Security Surface 不是靜態列表

傳統漏洞列表容易假設：

$$
\Sigma
=
\text{fixed}.
$$

但 Agent architecture 是動態的。

新增：
- connector；
- memory；
- Agent；
- tool；
- permission；
- delegation protocol；

會改變：

$$
\Sigma.
$$

所以 security assessment 應寫：

$$
\boxed{
\Sigma_t
=
F(
\mathfrak C_t,
\mathfrak D_t,
\Theta_t
).
}
$$

而不是一次掃描後永久成立。

---

## 32. Security as Continuous Runtime State

因此安全不只是 release gate。

而是 runtime state：

$$
\mathfrak S^{\mathrm{sec}}_t
=
(
identity_t,
authority_t,
context_t,
risk_t,
provenance_t,
recovery_t
).
$$

當 Agent：
- delegation；
- tool use；
- task pivot；
- data sensitivity；

改變時：

$$
\mathfrak S^{\mathrm{sec}}_{t+1}
\neq
\mathfrak S^{\mathrm{sec}}_t.
$$

authorization 也應隨之更新。

---

## 33. Security–Capability Coevolution Loop

整體可以寫成：

$$
\boxed{
\begin{aligned}
\text{capability}\uparrow
&\Rightarrow
\text{action surface}\uparrow\\
&\Rightarrow
\text{potential security surface}\uparrow\\
&\Rightarrow
\text{identity / authorization / observability demands}\uparrow\\
&\Rightarrow
\text{defensive security competence}\uparrow\\
&\Rightarrow
\text{detection frontier}\uparrow\\
&\Rightarrow
\text{newly visible security surface}\uparrow.
\end{aligned}
}
$$

最後一項是：

$$
\boxed{
\text{visible surface}
}
$$

而不一定是：

$$
\boxed{
\text{true underlying surface}.
}
$$

這正是整個循環最容易造成錯覺的地方。

---

## 34. 安全域的「諷刺」

因此表面上會看到：

> AI 越進步，安全警告越多。

> 安全越做，AI 越會分析安全問題。

兩件事都可以同時成立。

第一件事可能來自：

$$
\mathfrak C\uparrow
\Rightarrow
\Sigma^\star\uparrow.
$$

第二件事可能來自：

$$
\mathcal E_{\mathrm{sec}}\uparrow
\Rightarrow
K_t\uparrow.
$$

所以 observed warning count：

$$
W_t
$$

其實同時混合：

$$
\boxed{
W_t
=
f(
\text{true surface},
\text{detection coverage},
\text{reporting policy},
\text{deployment scale}
).
}
$$

不能直接拿來判定 AI 更危險或更安全。

---

## 35. Security Maturity Vector

定義：

$$
\boxed{
\mathbf S
=
(
I,
A,
L,
O,
P,
R,
E,
G
)
}
$$

其中：

- $I$：identity fidelity；
- $A$：authorization tightness；
- $L$：least-privilege quality；
- $O$：observability；
- $P$：provenance；
- $R$：recovery / reversibility；
- $E$：environment isolation；
- $G$：governance consistency。

與 Paper 08 的 capability vector：

$$
\mathbf P
$$

形成 coupled trajectory：

$$
\boxed{
(
\mathbf P_t,
\mathbf S_t
)
\rightarrow
(
\mathbf P_{t+1},
\mathbf S_{t+1}
).
}
$$

這才是 Agent deployment 的完整演化狀態。

---

## 36. Coexpansion Gap

定義 capability normalized growth：

$$
g_C(t).
$$

security maturity growth：

$$
g_S(t).
$$

定義：

$$
\boxed{
\Delta_{\mathrm{CS}}
=
g_C-g_S.
}
$$

如果：

$$
\Delta_{\mathrm{CS}}>0,
$$

表示 capability frontier 暫時跑得比 security control frontier 快。

如果：

$$
\Delta_{\mathrm{CS}}<0,
$$

表示 control investment 暫時超前。

本文不主張：

$$
\Delta_{\mathrm{CS}}=0
$$

永遠最佳。

因為安全需要 margin。

---

## 37. Security Margin

令 task-required authority：

$$
A_{\min}.
$$

實際 grant：

$$
A_{\mathrm{grant}}.
$$

maximum tolerable grant：

$$
A_{\max}^{\mathrm{risk}}.
$$

理想：

$$
\boxed{
A_{\min}
\subseteq
A_{\mathrm{grant}}
\subseteq
A_{\max}^{\mathrm{risk}}.
}
$$

太小：

$$
A_{\mathrm{grant}}
\not\supseteq
A_{\min}
$$

導致 utility failure。

太大：

$$
A_{\mathrm{grant}}
\not\subseteq
A_{\max}^{\mathrm{risk}}
$$

導致 unnecessary exposure。

因此安全 deployment 是 constrained optimization，不是單向縮權。

---

## 38. 本篇 Structural Checker

本文附 Python structural checker。

### 38.1 Capability Surface Monotonicity

建立 capability graph：

$$
C_1
$$

只能：
- read workspace；
- write workspace。

擴張：

$$
C_2
$$

再加入：
- network connector；
- shared memory；
- delegated tool edge。

checker 由 reachability 確認：

$$
\Sigma(C_1)
\subseteq
\Sigma(C_2).
$$

### 38.2 Least-Privilege Pruning

task 只需要：
- read workspace；
- write workspace。

若移除 network / delegation capabilities：

task 仍可完成，

而 security-sensitive reachable states 減少。

### 38.3 Security Discrimination

兩 context：
- authorized principal；
- unauthorized principal。

若 monitor observation 都只看到：

$$
\text{tool=write}
$$

則 policy 無法正確區分。

加入：

$$
principal
$$

欄位後可以精確判定。

### 38.4 Detection Frontier

真實 unsafe set 固定有：

$$
5
$$

項。

初始只識別：

$$
2.
$$

改善 analysis 後識別：

$$
4.
$$

reported issues：

$$
2\rightarrow4,
$$

但真實 underlying unsafe set：

$$
5\rightarrow5.
$$

### 38.5 Capability–Permission Separation

technical capability：

$$
\{read,write,network,delegate\}.
$$

task grant：

$$
\{read,write\}.
$$

checker 確認：

$$
C_{\mathrm{allow}}
\subset
C_{\mathrm{tech}}
$$

且 task success 不需要 extra capabilities。

---

## 39. 與 Series C 前八篇的整合

Paper 01：

$$
\text{verification attractor}.
$$

Paper 02：

$$
\text{distributed epistemic correction}.
$$

Paper 03：

$$
\text{admissible-world contraction}.
$$

Paper 04：

$$
\text{epistemic carriers}.
$$

Paper 05：

$$
\text{autonomous research closure}.
$$

Paper 06：

$$
\text{cross-model epistemic convergence}.
$$

Paper 07：

$$
\text{AI work society}.
$$

Paper 08：

$$
\text{PGAI}.
$$

Paper 09 補上：

$$
\boxed{
\text{PGAI capability growth}
\leftrightarrow
\text{security / authorization / observability growth}.
}
$$

所以 security 不是旁支。

它是 proto-general autonomous system 能不能實際部署的 necessary substrate。

---

## 40. 結論

本文最基礎定理：

$$
\boxed{
\mathfrak C_1
\preceq
\mathfrak C_2
\Rightarrow
\Sigma(\mathfrak C_1)
\subseteq
\Sigma(\mathfrak C_2)
}
$$

成立於 threat model 與 controls 不變的條件下。

所以能力增加會使 potential action/security reachability 非遞減。

但：

$$
\boxed{
\text{potential surface}
\neq
\text{incident probability}.
}
$$

因為 controls 可以同步擴張。

Least privilege 可以在保留 task sufficiency 的條件下縮小 surface。

更重要的是：

$$
\boxed{
\text{security policy complexity}
\uparrow
\Rightarrow
\text{required security distinctions}
\uparrow.
}
$$

若 monitor 看不到 policy 需要區分的 context，就不可能精確 enforce。

所以所謂：

> 為了讓 AI 安全，人類反而必須讓它／其安全系統越來越懂資安。

其嚴格版本是：

$$
\boxed{
\textbf{
Defensive governance over expanding agent capabilities
requires an expanding representational model of identity,
authority, provenance, context, information flow,
and action consequences.
}
}
$$

同時，security detection 提升會使已知問題數增加，即使 underlying surface 沒有變化。

因此：

$$
\boxed{
\text{more security findings}
\nRightarrow
\text{less security}.
}
$$

Series C 到這裡得到一個完整的雙向迴路：

$$
\boxed{
\text{capability}
\rightarrow
\text{action}
\rightarrow
\text{risk}
\rightarrow
\text{security cognition}
\rightarrow
\text{control}
\rightarrow
\text{deployable capability}.
}
$$

下一篇將完成本系列最後一層外推：

**Series C / Paper 10 — Beyond Mathematics and Code: Verification Density Across Worlds.**

---

## 參考文獻

1. NIST / NCCoE. *Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization*. Concept Paper, 2026.
2. NIST CAISI. *AI Agent Standards Initiative*. 2026.
3. OWASP GenAI Security Project. *OWASP Top 10 for Agentic Applications 2026*.
4. Li, N., Zhang, K., Polley, K., & Ma, J. *Security Considerations for Artificial Intelligence Agents*. arXiv:2603.12230, 2026.
5. Ling, Y., Yu, S., Chen, Z., & Fang, C. *Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation*. arXiv:2606.10749, 2026.
6. Chu, K. *A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework*. arXiv:2604.23338, 2026.
7. Yan, Z. et al. *Do Coding Agents Understand Least-Privilege Authorization?* arXiv:2605.14859, 2026.
8. Zhu, J. et al. *MiniScope: A Least Privilege Framework for Authorizing Tool Calling Agents*. arXiv:2512.11147, 2025.
9. *A Compositional Authorization Framework for Delegation in Agentic Systems*. arXiv:2606.03518, 2026.
10. *Intent-Governed Tool Authorization for AI Agents*. arXiv:2606.22916, 2026.
11. *Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels*. arXiv:2607.23438, 2026.
12. OpenAI. *GPT-5.3-Codex System Card*. 2026.
13. OpenAI. *GPT-5.4 Thinking System Card — Cyber Safeguards*. 2026.
14. OpenAI. *GPT-5.6 System Card*. 2026.

## 狀態標記

- **Definitions:** operational capability surface、security-relevant reachability、capability–control pair、security lag、privilege inflation、detection frontier、defensive epistemic coexpansion、security maturity vector。
- **Proved:** Capability-Surface Monotonicity、Least-Privilege Pruning under sufficiency assumptions、Security Discrimination Necessity、Detection-Frontier Expansion。
- **Externally grounded observations:** NIST agent identity/authorization initiative、OWASP Agentic Top 10、2026 least-privilege benchmarks/frameworks、frontier cyber capability safeguards、persistent memory / tool / delegation attack-surface research。
- **Structural checker:** capability graph expansion、least-privilege pruning、authorization aliasing、detection-frontier expansion、capability/permission separation。
- **Not claimed:** capability growth inevitably causes more incidents、security training necessarily increases offensive ability、all cyber knowledge is dual-use in the same way、more reported vulnerabilities means the system became less safe。
