# Series C / Paper 02
# 觀察者網路認知歸一：多 AI 幻覺壓縮與分散式錯誤修正
## Observer-Network Epistemic Normalization: Multi-AI Hallucination Compression and Distributed Error Correction

版本：v0.1  
日期：2026-08-14  
狀態：Theory + structural experiment paper

## 摘要

多 Agent 系統常被直覺地理解為「多個模型投票」，但 majority agreement 既不保證真實，也可能在相關偏誤、遞迴引用與延遲驗證下形成 collective hallucination。本文提出 **Observer-Network Epistemic Normalization（觀察者網路認知歸一）**，將多 AI 可靠性問題從「共識最大化」改寫為「在不直接讀取 hidden truth 的條件下，利用異質觀察、來源、歷史、交叉驗證與 fault localization，逐步壓縮仍可容許的世界集合，並隔離高風險資訊通道」。

本文首先定義 observer network、claim packet、admissible-world set、relational inconsistency certificate 與 epistemic normalization operator。接著證明三個基礎結果。第一，若新加入的 constraint 是 sound，則 admissible-world set 單調收縮且不排除真實狀態。第二，即使沒有 hidden truth，只要其他觀察者的 constraint 交集非空，而加入某一 observer 後交集變空，即可產生「關係不相容證書」；但此證書只能定位 incompatibility，不能單獨證明該 observer 錯誤。第三，在等方差、等相關的誤差模型下，有效獨立 observer 數滿足：

$$
N_{\mathrm{eff}}
=
\frac{N}{1+(N-1)\rho},
$$

因此當錯誤相關係數 $\rho\rightarrow1$ 時，即使 nominal observer count $N$ 很大，也有 $N_{\mathrm{eff}}\rightarrow1$。此結果形式化了「多 AI 不等於多獨立證據」。

本文再重新分析前一系列的 observer-only synthetic experiment：hidden state 維度為 4，每個 observer 即時 rank 為 2，網路含 5、8、12、20 個 observers，並在多組 noise 下加入 persistent measurement bias。重建過程不讀 hidden state，只在最後 scoring 使用。consistency-based suspect removal 將平均 state error 從 $0.0494479$ 降至 $0.0125506$，約降低 $74.62\%$ ；corrupted-observer detection rate 為 $0.945833$，exact bad-set identification rate 為 $0.935937$。本文明確把此結果視為「distributed epistemic error correction 的結構先導實驗」，而非真實 LLM hallucination benchmark。

最後，本文將上述結構與 SelfCheckGPT、MARCH、AgentAuditor、AgentHallu、AgentLocate、MAS-FIRE、Byzantine-resilience 及 2026 年 collective hallucination / delayed verification / biased consensus 研究對照，提出一組必要但非充分的 normalization 條件：異質且非完全冗餘的 evidence channels、可追溯 provenance、受控通信拓撲、可及時返回的 verifier、局部 fault attribution、保留少數派 evidence，以及對 shared specification failure 的外部檢查。

本文不主張：

$$
\text{more agents}
\Rightarrow
\text{more truth}.
$$

本文主張的較弱方向是：

$$
\boxed{
\text{heterogeneous evidence}
+
\text{sound verification}
+
\text{fault localization}
+
\text{controlled information flow}
\Rightarrow
\text{possible epistemic normalization}.
}
$$

**關鍵詞：** multi-agent LLM；hallucination；observer network；epistemic normalization；fault localization；collective hallucination；Byzantine resilience；admissible worlds；distributed error correction

---

## 1. 從「投票」改寫成「認知歸一」

在單一模型中，hallucination 常被表示為輸出 claim 與外部事實不一致：

$$
c
\not\models
W^\star,
$$

其中 $W^\star$ 是實際世界狀態或目標 truth condition。

到了多 Agent 系統，最直觀的方法是讓：

$$
A_1,A_2,\ldots,A_N
$$

分別回答，再使用：

$$
\operatorname{Majority}(A_1,\ldots,A_N).
$$

但這個結構有一個根本問題：

$$
\text{agreement}
\neq
\text{independence},
$$

且：

$$
\text{agreement}
\neq
\text{truth}.
$$

如果所有 Agents 共享訓練偏誤、同一 retrieval source、同一錯誤 specification、同一中間訊息，或彼此遞迴引用，則 nominally different agents 可能只是同一錯誤的多次表現。

因此本文不把目標設定為：

$$
\max
\Pr(
A_1=A_2=\cdots=A_N
),
$$

而設定為：

$$
\min
\left(
\text{unsupported claim mass}
+
\text{cross-evidence inconsistency}
+
\text{unlocalized fault risk}
\right),
$$

同時保留：
- provenance；
- minority evidence；
- unresolved ambiguity；
- gauge / underdetermination；
- uncertainty。

這個過程稱為：

$$
\boxed{
\textbf{Observer-Network Epistemic Normalization}.
}
$$

---

## 2. 外部研究背景：從 self-consistency 到 system-level hallucination

SelfCheckGPT 提出一個重要先例：對同一黑箱模型進行多次 sampling，若模型真的掌握相關知識，生成內容往往較一致；若生成內容高度分歧，則可作為 hallucination risk 的訊號。這仍是 single-model sampling，但已經指出：

$$
\text{cross-sample relation}
$$

本身可以提供額外的 epistemic information。

2026 年的 MARCH 更進一步，把 Solver、Proposer 與 Checker 分離，讓 Checker 不看到 Solver 原始答案，只檢查拆成 atomic propositions 的 claims 與 retrieved evidence，以降低 self-confirmation。這顯示「資訊不對稱」有時不是系統缺陷，而是 verification protocol 的必要設計。

AgentAuditor 則明確反對只做 majority vote。它把多 Agent traces 組成 reasoning tree，在 critical divergence points 做 localized verification，並報告相較 majority vote 與 LLM-as-a-Judge 的改善。其研究問題與本文高度一致：

> 全域共識是否可以被局部差異點的證據審計取代？

AgentHallu 與 AgentLocate 代表另一條重要路線：不只判定 end-to-end 成功或失敗，而是定位 hallucination / failure 最早在哪一個 step、哪一個 agent 發生。這使 fault localization 從事後印象轉為可測 task。

與上述正向結果相反，2026 年的 Collective Hallucination 工作把 hallucination 視為網路上的動態傳播過程，指出 recursive interactions 可放大 unsupported claims；Delayed Verification 則指出 verifier latency 可能使錯誤在校正返回前擴散，甚至在特定 signed-belief model 中造成 oscillatory instability。Consistency Illusion 顯示 answer-level consensus 可與 reasoning-level misalignment 同時增加；Biased Consensus 則提出多 Agent debate 在 conformity 與 noise 達到特定條件時可出現 collective bias 的 phase-transition-like behavior。

因此，現有研究並不支持：

$$
\text{multi-agent}
\Rightarrow
\text{reliable}.
$$

更合適的問題是：

$$
\boxed{
\text{什麼網路、什麼 evidence、什麼 verifier、什麼延遲與什麼 fault model，
才使多 Agent 互動成為 error-correcting system？
}
}
$$

---

## 3. Observer Network 的形式化

### 3.1 世界與觀察

令可能世界空間為：

$$
\Omega.
$$

真實狀態為：

$$
W^\star\in\Omega.
$$

但任何 Agent 都不被假設可以直接讀取 $W^\star$。

第 $i$ 個 observer 在時間 $t$ 只能取得：

$$
y_i^t
=
h_i(W^\star)
+
\epsilon_i^t
+
b_i^t,
$$

其中：
- $h_i$ 是局部 observation map；
- $\epsilon_i^t$ 是一般 noise；
- $b_i^t$ 是 systematic bias、persistent error 或 adversarial corruption。

在語言 Agent 中， $y_i^t$ 不一定是數值 measurement，也可以是：
- retrieved passage；
- tool output；
- program execution result；
- peer message；
- human instruction；
- sensor record；
- database row；
- theorem checker result。

### 3.2 Claim packet

定義 observer $i$ 在時間 $t$ 的 claim packet：

$$
C_i^t
=
(
Q_i^t,
U_i^t,
P_i^t,
T_i^t
),
$$

其中：
- $Q_i^t$：claim set；
- $U_i^t$：uncertainty / confidence metadata；
- $P_i^t$：provenance；
- $T_i^t$：trajectory / causal history。

因此系統不只交換「答案」，而交換：

$$
\boxed{
\text{claim}
+
\text{uncertainty}
+
\text{source}
+
\text{history}.
}
$$

### 3.3 通信圖

令：

$$
G_t=(V,E_t),
$$

其中 $V=\{1,\ldots,N\}$ 是 observers，而 $(i,j)\in E_t$ 表示在時間 $t$ 有資訊從 $i$ 傳向 $j$。

這一步很重要，因為 hallucination risk 不只由 node reliability 決定，也由 topology 決定。

同一個錯誤在 chain：

$$
A\rightarrow B\rightarrow C
$$

與 mutual-review graph：

$$
A\leftrightarrow B\leftrightarrow C
$$

中的傳播與修復能力可以不同。

---

## 4. 可容許世界集合

每一個 claim / observation 不直接被視為「真」，而被轉換成對可能世界的 constraint。

令第 $k$ 個已接受 constraint 所允許的世界集合為：

$$
K_k\subseteq\Omega.
$$

定義時間 $t$ 的 admissible-world set：

$$
\mathcal A_t
=
\bigcap_{k\leq t}K_k.
$$

### 定義 1：Sound constraint

若：

$$
W^\star\in K_k,
$$

則稱 $K_k$ 對真實狀態 sound。

### 定理 1：Sound Contraction

若：

$$
\mathcal A_{t+1}
=
\mathcal A_t
\cap
K_{t+1},
$$

則必有：

$$
\mathcal A_{t+1}
\subseteq
\mathcal A_t.
$$

若 $K_{t+1}$ sound 且：

$$
W^\star\in\mathcal A_t,
$$

則：

$$
W^\star\in\mathcal A_{t+1}.
$$

### 證明

第一式由集合交集定義直接得到：

$$
\mathcal A_t\cap K_{t+1}
\subseteq
\mathcal A_t.
$$

若 $W^\star\in\mathcal A_t$ 且 $W^\star\in K_{t+1}$，則：

$$
W^\star
\in
\mathcal A_t\cap K_{t+1}
=
\mathcal A_{t+1}.
$$

證畢。

### 解讀

認知歸一不是要求所有 Agent 說同一句話，而是：

$$
\boxed{
\operatorname{diam}(\mathcal A_t)
\downarrow
}
$$

或更一般地，系統中仍然與可信 evidence 相容的世界類逐步變窄。

但這裡有一個絕對不能省略的條件：

$$
\text{constraint soundness}.
$$

若 verifier、retrieval source 或 specification 本身錯誤，則：

$$
W^\star
\notin
K_{t+1},
$$

系統反而可能「非常一致地」把真實狀態排除。

這就是 collective hallucination 的形式化入口。

---

## 5. 不讀 hidden truth 時，仍可做什麼？

### 5.1 Relational Incompatibility Certificate

對 observer $i$，令其 constraint set 為：

$$
K_i.
$$

其他 observers 的共同允許集合為：

$$
\mathcal A_{-i}
=
\bigcap_{j\neq i}K_j.
$$

若：

$$
\mathcal A_{-i}\neq\varnothing
$$

但：

$$
K_i\cap\mathcal A_{-i}
=
\varnothing,
$$

則稱 observer $i$ 得到一個 **relational incompatibility certificate**。

### 命題 2：不相容可被定位，但錯誤不能僅由不相容單獨決定

上述條件足以證明：

$$
K_i
$$

與其他 constraints 的共同體不相容。

但它不充分證明：

$$
K_i
$$

必然錯誤。

### 證明

由：

$$
K_i\cap\mathcal A_{-i}=\varnothing
$$

可知兩者不能同時成立。

然而可能存在兩種情況：
1. $K_i$ 錯；
2. $\mathcal A_{-i}$ 由一組共同錯誤 constraints 構成。

因此只能推出 incompatibility，而不能在沒有額外 witness 的條件下唯一定位 truth side。

證畢。

### 5.2 這正是「observer-only diagnosis」的核心

系統可以在不知道：

$$
W^\star
$$

的情況下知道：

> 這些東西不能全部同時是真的。

這已經足以觸發：
- re-query；
- independent retrieval；
- tool execution；
- alternative model；
- human escalation；
- temporary isolation。

也就是說：

$$
\boxed{
\text{truth unavailable}
\nRightarrow
\text{error diagnosis impossible}.
}
$$

---

## 6. 多 AI 不等於多獨立證據

### 6.1 等相關誤差模型

令每個 observer 的 estimation error 為：

$$
e_i,
$$

滿足：

$$
\mathbb E[e_i]=0,
$$

$$
\operatorname{Var}(e_i)=\sigma^2,
$$

以及對所有 $i\neq j$：

$$
\operatorname{Corr}(e_i,e_j)=\rho.
$$

考慮簡單平均：

$$
\bar e
=
\frac{1}{N}
\sum_{i=1}^N e_i.
$$

則：

$$
\operatorname{Var}(\bar e)
=
\frac{\sigma^2}{N}
\left(
1+(N-1)\rho
\right).
$$

若定義有效獨立 observer 數 $N_{\mathrm{eff}}$ 使：

$$
\operatorname{Var}(\bar e)
=
\frac{\sigma^2}{N_{\mathrm{eff}}},
$$

則：

$$
\boxed{
N_{\mathrm{eff}}
=
\frac{N}{1+(N-1)\rho}.
}
$$

### 定理 3：Perfect-correlation collapse

當：

$$
\rho\rightarrow1,
$$

有：

$$
N_{\mathrm{eff}}\rightarrow1.
$$

當：

$$
\rho=0,
$$

則：

$$
N_{\mathrm{eff}}=N.
$$

### 解讀

若 100 個 Agents 全都沿著同一錯誤來源生成：

$$
N=100
$$

不代表：

$$
N_{\mathrm{eff}}=100.
$$

當 $\rho=0.9$ 時：

$$
N_{\mathrm{eff}}
=
\frac{100}{1+99(0.9)}
\approx1.11.
$$

所以：

$$
\boxed{
\text{model count}
\neq
\text{epistemic diversity}.
}
$$

這也是為什麼 heterogeneous models、isolated verification、independent tools 與 source diversity 比單純增加 agent count 更重要。

---

## 7. Independent Witness Suppression

考慮一個其實為 false 的 claim $\phi$。

假設有 $k$ 個 verifier：

$$
V_1,\ldots,V_k,
$$

且每個 verifier 在 $\phi$ 為 false 時誤接受它的條件機率滿足：

$$
\Pr(V_i=\text{accept}\mid\neg\phi)
\leq
q_i.
$$

若在給定 $\neg\phi$ 下，這些誤接受事件條件獨立，則：

$$
\Pr(
V_1=\cdots=V_k=\text{accept}
\mid
\neg\phi
)
\leq
\prod_{i=1}^{k}q_i.
$$

若：

$$
q_i=q,
$$

則：

$$
\Pr(\text{all false accept}\mid\neg\phi)
\leq
q^k.
$$

這顯示真正獨立的 witness 可以快速壓低共同誤接受機率。

但其關鍵不是：

$$
k\uparrow,
$$

而是：

$$
\boxed{
\text{conditional independence / low error correlation}.
}
$$

若 verifier 共用同一 retrieval、同一錯誤 premise 或彼此看到答案後產生 confirmation bias，則：

$$
q^k
$$

的乘法抑制不能成立。

---

## 8. Epistemic Normalization Operator

現在定義本文的核心 operator：

$$
\mathfrak N:
(
\mathbf C_t,
\mathbf E_t,
G_t,
\mathbf H_t
)
\mapsto
(
\mathbf C_{t+1},
\boldsymbol\omega_{t+1},
\mathcal A_{t+1},
\mathcal F_{t+1}
),
$$

其中：
- $\mathbf C_t$：claims；
- $\mathbf E_t$：evidence / provenance；
- $G_t$：通信圖；
- $\mathbf H_t$：history；
- $\boldsymbol\omega_t$：observer / evidence weights；
- $\mathcal A_t$：admissible worlds；
- $\mathcal F_t$：fault hypotheses。

一個最小 normalization cycle 可拆成：

$$
\boxed{
\begin{aligned}
1.&\ \text{claim atomization}\\
2.&\ \text{provenance separation}\\
3.&\ \text{independent re-observation}\\
4.&\ \text{relational consistency check}\\
5.&\ \text{fault localization}\\
6.&\ \text{weight / isolate / retry}\\
7.&\ \text{re-synthesis}\\
8.&\ \text{retain unresolved alternatives}
\end{aligned}
}
$$

### 8.1 為何不能直接刪除少數派

如果：

$$
A_1,\ldots,A_9
$$

都使用同一錯誤 source，而 $A_{10}$ 使用獨立 sensor，則：

$$
9:1
$$

的 majority 仍然可能是錯的。

因此 normalization operator 不應只用：

$$
\text{vote count}.
$$

至少需要：

$$
\text{evidence independence},
\quad
\text{provenance quality},
\quad
\text{verification strength},
\quad
\text{trajectory consistency}.
$$

### 8.2 Fault suspicion score

可定義一個非唯一的 suspicion score：

$$
S_i
=
\alpha R_i^{\mathrm{rel}}
+
\beta R_i^{\mathrm{evid}}
+
\gamma R_i^{\mathrm{traj}}
+
\delta R_i^{\mathrm{impact}},
$$

其中：
- $R_i^{\mathrm{rel}}$：與其他 observers 的關係殘差；
- $R_i^{\mathrm{evid}}$：與獨立 evidence 的殘差；
- $R_i^{\mathrm{traj}}$：自身前後 trajectory inconsistency；
- $R_i^{\mathrm{impact}}$：移除或降權後對整體 consistency 的改善。

此 score 不是 truth oracle，而是：

$$
\boxed{
\text{where should the network spend verification budget next?}
}
$$

---

## 9. 前一系列 observer-only experiment 的重新解讀

### 9.1 實驗設定

前一系列執行一個 synthetic observer experiment：

- hidden state dimension：4；
- observer counts：5、8、12、20；
- each observer instantaneous rank：2；
- noise sigma： $0$ 、 $0.005$ 、 $0.01$ 、 $0.03$ ；
- 每設定 120 random worlds；
- 部分 observers 被加入 persistent measurement bias。

關鍵限制是：

> reconstruction 過程中，任何 observer 與 fusion network 都不能直接讀 hidden global state。

hidden truth 只保留給最後 scoring。

### 9.2 結果

實驗得到：

$$
\text{full-rank fused network rate}
=
1.000000,
$$

$$
\text{history-only full observability rate}
=
1.000000.
$$

平均 state error 在 suspect diagnosis 前為：

$$
E_{\mathrm{all}}
=
0.0494479.
$$

移除 suspect observers 後為：

$$
E_{\mathrm{repair}}
=
0.0125506.
$$

相對下降：

$$
\frac{
0.0494479-0.0125506
}{
0.0494479
}
\approx
0.7462.
$$

即約：

$$
\boxed{
74.62\%.
}
$$

同時：

$$
\text{corrupted-observer detection}
=
0.945833,
$$

$$
\text{exact bad-set identification}
=
0.935937.
$$

### 9.3 正確解讀

這個結果支持：

$$
\boxed{
\text{network consistency can identify corrupted local channels
without using hidden truth during reconstruction}.
}
$$

但它不直接支持：

$$
\boxed{
\text{real LLM hallucination rate decreases by }74.62\%.
}
$$

因為該實驗是：
- linear / synthetic hidden-state model；
- controlled corruption；
- 明確 observation maps；
- 可量化 residual；
- 不是真實自然語言 hallucination distribution。

因此本文把它定位為：

$$
\boxed{
\textbf{structural precursor experiment}.
}
$$

它證明的是「無 oracle 的 distributed fault diagnosis 在一個受控 observer model 中可行」，而不是直接完成對現實多 AI 系統的泛化。

---

## 10. 與真實 LLM Multi-Agent 研究的交會

### 10.1 MARCH：信息隔離

MARCH 的關鍵設計不是增加更多 Agent，而是讓 Checker 不讀 Solver 原始答案，只讀 atomic propositions 與 retrieved evidence。

對本文而言，這等於刻意降低：

$$
\rho(
e_{\mathrm{solver}},
e_{\mathrm{checker}}
),
$$

至少降低由原始答案造成的 confirmation coupling。

因此 MARCH 可以被理解為：

$$
\boxed{
\text{error-channel decorrelation by information asymmetry}.
}
$$

### 10.2 AgentAuditor：差異點局部驗證

AgentAuditor 不把 majority 當終局，而把 divergence point 變成 audit target。

這與本文的 relational incompatibility certificate 幾乎對應：

$$
\text{global disagreement}
\rightarrow
\text{localized divergence}
\rightarrow
\text{targeted verification}.
$$

### 10.3 AgentHallu / AgentLocate：從 end-to-end error 到 fault attribution

AgentHallu 顯示，在 multi-step agent trajectory 中，真正困難的是找到 hallucination 最早發生的 step。其 benchmark 將 hallucination 分成 Planning、Retrieval、Reasoning、Human-Interaction 與 Tool-Use 等類型。

AgentLocate 更進一步把 failure localization 定義成：
- responsible agent；
- earliest decisive step。

因此多 Agent reliability 正逐漸從：

$$
\text{did it fail?}
$$

轉成：

$$
\boxed{
\text{where did the epistemic trajectory first become unrecoverable?}
}
$$

### 10.4 MAS-FIRE 與 MAST：fault taxonomy / closed-loop resilience

MAS-FIRE 對 LLM-based MAS 做 fault injection，報告 iterative closed-loop designs 能 neutralize 部分在 linear workflow 中會造成 collapse 的 faults。MAST 則從大量 MAS traces 中整理 specification/system-design failure、inter-agent misalignment、task verification/termination 等 failure classes。

這與本文的主張一致：

$$
\text{reliability}
\neq
\text{model intelligence alone}.
$$

architecture、topology、verification path 與 termination policy 都是 epistemic system 的一部分。

---

## 11. Collective Hallucination：Normalization 的反面

定義 network unsupported-claim mass：

$$
H_t
=
\sum_{c\in\mathcal C_t}
w(c)
\mathbf 1[
c\text{ lacks sufficient support}
].
$$

若互動後：

$$
H_{t+1}>H_t
$$

且 unsupported claims 的 diffusion 範圍增加，則可稱系統進入 hallucination amplification regime。

2026 年 Collective Hallucination 的系統模型正指出：
- recursive information flow；
- confidence coupling；
- communication topology；
- adversarial perturbation

都會改變 hallucination 在 network 中的傳播。

因此 multi-agent system 至少存在兩種可能 dynamics：

$$
\boxed{
\text{normalization regime}
}
$$

與：

$$
\boxed{
\text{amplification regime}.
}
$$

這意味著「Agent 數量增加」不是控制參數的全部。更重要的可能是：

$$
(
\rho,
\tau_v,
G,
\lambda_{\mathrm{conf}},
B_v
),
$$

其中：
- $\rho$：error correlation；
- $\tau_v$：verification delay；
- $G$：communication topology；
- $\lambda_{\mathrm{conf}}$：confidence coupling；
- $B_v$：verification budget。

---

## 12. Delayed Verification 與時間結構

若 false claim 在時間 $t$ 產生：

$$
c_t,
$$

但 verifier 到：

$$
t+\tau
$$

才返回 correction，那麼在：

$$
[t,t+\tau)
$$

期間，其他 Agents 可能已經把 $c_t$ 當成 premise。

因此 correction 的實際效果不是只有：

$$
\text{correct / incorrect}.
$$

還取決於：

$$
\boxed{
\text{when does correction arrive?}
}
$$

這讓時間成為 epistemic network 的一級變量。

因此一個可行 normalization system 應記錄：

$$
\text{claim timestamp},
\quad
\text{dependency graph},
\quad
\text{verification timestamp},
\quad
\text{downstream descendants}.
$$

當 claim 被推翻時，系統必須做的不是只改一行答案，而是：

$$
\boxed{
\text{dependency-aware rollback}.
}
$$

這與軟體工程中的 invalidation / rebuild、以及科學研究中的 evidence retraction 非常接近。

---

## 13. Shared Specification Failure

最危險的 regime 之一不是 Agent 彼此不同意，而是：

$$
\boxed{
\text{所有 Agent 都忠實地驗證了錯誤的 specification}.
}
$$

設真實要求為：

$$
S^\star,
$$

但所有 Agents 共用：

$$
\tilde S\neq S^\star.
$$

則即使：

$$
\forall i,\quad
A_i\models\tilde S,
$$

也不能推出：

$$
A_i\models S^\star.
$$

因此：

$$
\text{all tests pass}
\nRightarrow
\text{world-level correctness}.
$$

這就是為什麼計算機只能是「相對客觀認知載體」。

它能把 claim 投射到另一個判定域：

$$
\text{language}
\rightarrow
\text{execution},
$$

但不能消除：
- specification error；
- compiler / runtime bug；
- data corruption；
- wrong metric；
- missing variable；
- adversarial environment。

真正強的 multi-domain verification 必須設法增加：

$$
\boxed{
\text{error-channel heterogeneity}.
}
$$

---

## 14. Normalization 的必要條件候選

本文不給 sufficient theorem，但提出八個必要條件候選。

### C1. Joint observability

不同 observers 合併後必須真的增加資訊，而非只複製同一 projection。

### C2. Error decorrelation

至少一部分 evidence channel 應滿足：

$$
\rho_{ij}<1.
$$

### C3. Provenance preservation

claim 必須能回到：
- source；
- tool call；
- code；
- dataset；
- timestamp；
- upstream claim。

### C4. Localizable disagreement

系統必須能把：

$$
\text{global contradiction}
$$

轉成：

$$
\text{local audit target}.
$$

### C5. Timely verification

verification latency 不可大到讓 unsupported claims 在 network 中先形成不可控 cascade。

### C6. Minority evidence retention

少數派 evidence 不應因 vote count 太小而直接消失。

### C7. Fault-aware weighting / isolation

system 要能在高 suspicion channel 上降權、重查或暫時隔離，而不是永久信任固定角色。

### C8. External specification challenge

至少存在某種 mechanism 能質疑 shared specification / shared source，而不是只在內部做 self-consistency。

---

## 15. Epistemic Risk Functional

為了把 normalization 寫成 optimization 問題，可定義：

$$
\mathcal R_t
=
\lambda_1 I_t
+
\lambda_2 U_t
+
\lambda_3 F_t
+
\lambda_4 D_t
+
\lambda_5 C_t,
$$

其中：
- $I_t$：cross-observer inconsistency；
- $U_t$：unsupported-claim mass；
- $F_t$：unlocalized-fault mass；
- $D_t$：verification delay penalty；
- $C_t$：correlated-evidence penalty。

理想 normalization operator 不是單純讓：

$$
I_t\rightarrow0,
$$

因為 false consensus 也可以做到。

真正目標是：

$$
\boxed{
\mathcal R_{t+1}<\mathcal R_t
}
$$

同時：
- 不隱藏 unresolved alternatives；
- 不把 minority evidence 強行壓平；
- 不虛構 certainty；
- 不把未驗證 claim 升級成 settled fact。

這也解釋了為什麼「看起來整齊」與「認知品質提高」不是同一件事。

---

## 16. Minimal Checker

本文附帶一個最小 checker，不模擬真實 LLM，而驗證三個結構事實：

1. admissible-world intersection 的 contraction；
2. equicorrelated observer model 下 $N_{\mathrm{eff}}$ 的 collapse；
3. independent witness 與 common-mode correlated witness 的 false-acceptance 差異。

checker 的目的不是建立 empirical SOTA，而是確保本文的基礎公式與反例敘述可被直接執行。

---

## 17. 對「AI 幻覺自行降低」命題的精確版本

本文不採用：

$$
\boxed{
\text{AI 數量增加}
\Rightarrow
\text{hallucination}\downarrow.
}
$$

更精確的 conjecture 是：

### 猜想 1：Observer-Network Normalization Conjecture

存在一組 task / environment 條件 $\mathcal C$，使得當多個 Agent：
1. 具有足夠 claim decomposition 與 tool-use 能力；
2. observer errors 非完全相關；
3. communication topology 可支援 cross-check；
4. verification latency 有界；
5. provenance 可追溯；
6. system 可做 fault localization 與 re-observation；

則存在 normalization operator $\mathfrak N$，使長程平均 epistemic risk 滿足：

$$
\mathbb E[
\mathcal R_{t+1}
\mid
\mathfrak N
]
<
\mathbb E[
\mathcal R_t
]
$$

直到到達 task-dependent residual floor：

$$
\mathcal R_\infty>0.
$$

本文刻意保留：

$$
\mathcal R_\infty>0,
$$

因為：
- 部分世界不可觀測；
- specification 可能錯；
- evidence 可能共同污染；
- verifier 可能失效；
- 開放世界存在不可消除不確定性。

因此「認知歸一」不是：

$$
\text{perfect truth convergence}.
$$

而是：

$$
\boxed{
\text{bounded-error, evidence-constrained, self-correcting convergence}.
}
$$

---

## 18. 從單一 AI 到分散式認知錯誤修正

如果 Paper 01 的核心是：

$$
\text{Verification Attractor},
$$

那 Paper 02 的核心是：

$$
\boxed{
\text{Distributed Epistemic Error Correction}.
}
$$

單一 Agent 的 error 可以被：
- 自己的第二次 sampling；
- peer Agent；
- independent model；
- retrieval；
- code execution；
- formal checker；
- sensor；
- human；
- historical state

重新觀察。

因此「AI 自己糾錯」其實不應只被理解成：

$$
A\rightarrow A'\rightarrow A''.
$$

更一般的是：

$$
\boxed{
\mathcal N_t
\rightarrow
\text{independent witnesses}
\rightarrow
\text{fault localization}
\rightarrow
\mathcal N_{t+1}.
}
$$

這是一個 network-level property。

---

## 19. 與下一篇的接口：共享認知許可

當 normalization 持續壓縮：

$$
\mathcal A_t,
$$

下一個問題自然是：

> 什麼時候可以說一個命題已經取得「共享認知許可」？

Paper 03 將正式研究：

$$
\mathrm{Permit}_t(\phi)=1
\iff
\forall W\in\mathcal A_t,\quad \phi(W)=1,
$$

以及：
- gauge-equivalent worlds；
- provisional permission；
- revocable permission；
- evidence arrival；
- global state underdetermination。

也就是把：

$$
\text{consensus}
$$

徹底替換成：

$$
\boxed{
\text{admissible-world entailment}.
}
$$

---

## 20. 結論

本文把多 AI hallucination mitigation 從「模型投票」改寫成一個 observer-network problem。

核心結論有五點。

第一：

$$
\boxed{
\text{agreement}
\neq
\text{truth}.
}
$$

第二：

$$
\boxed{
\text{nominal agent count}
\neq
\text{effective epistemic diversity}.
}
$$

在等相關模型中：

$$
N_{\mathrm{eff}}
=
\frac{N}{1+(N-1)\rho}.
$$

第三，即使 hidden truth 不可讀，network 仍可利用 relational incompatibility 定位「哪些 constraints 不能共同成立」，並把 verification budget 導向最需要重查的位置。

第四，前一系列 synthetic observer-only experiment 已提供一個結構性先導：在 reconstruction 不讀 hidden truth 的條件下，consistency-based diagnosis 可以顯著降低受控 corruption 造成的 reconstruction error；但這不是現實 LLM hallucination rate 的直接測量。

第五，真實 multi-agent literature 同時存在 normalization 與 amplification 的證據。MARCH、AgentAuditor、Byzantine resilience、AgentLocate 與 MAS-FIRE 顯示隔離驗證、challenge、fault localization 與 closed-loop architecture 可以提升 reliability；Collective Hallucination、Consistency Illusion、Delayed Verification 與 Biased Consensus 則證明相關錯誤、共識壓力與時間延遲可以把同一網路推向相反方向。

因此本文最終提出：

$$
\boxed{
\textbf{Observer-network reliability is a dynamical regime,
not a consequence of agent count.}
}
$$

也就是：

> 多 AI 是否降低幻覺，不取決於「有多少 AI」，而取決於它們是否形成了具有異質 evidence、可定位 fault、可控制資訊傳播、可保留 dissent，並能把 claim 投射到相對獨立判定域的認知閉環。

---

## 參考文獻

1. Manakul, P., Liusie, A., & Gales, M. J. F. (2023). *SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models*. arXiv:2303.08896.
2. Huang, J.-t. et al. (2024). *On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents*. arXiv:2408.00989.
3. Cemri, M. et al. (2025). *Why Do Multi-Agent LLM Systems Fail?* arXiv:2503.13657.
4. Zheng, L. et al. (2025). *Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance*. arXiv:2511.10400.
5. Liu, X. et al. (2026). *AgentHallu: Benchmarking Automated Hallucination Attribution of LLM-based Agents*. arXiv:2601.06818.
6. Yang, W. et al. (2026). *Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge*. arXiv:2602.09341.
7. Jia, J. et al. (2026). *MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems*. arXiv:2602.19843.
8. Li, Z. et al. (2026). *MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination*. arXiv:2603.24579.
9. Jamshidi, S. (2026). *Collective Hallucination in Multi-Agent LLMs: Modeling and Defense*. arXiv:2606.07941.
10. Wang, X., & Yang, C. C. (2026). *The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment*. arXiv:2606.08457.
11. Itkin, I. (2026). *Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement*. arXiv:2606.27409.
12. Xia, Y. et al. (2026). *Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems*. arXiv:2607.07989.
13. Okawa, M. (2026). *Emergence of Biased Consensus in Multi-Agent LLM Debates*. arXiv:2608.02827.

---

## 狀態標記

### External results
第 2、10、11、12、20 節對現有 LLM / MAS 文獻的整理。

### Internal prior result
第 9 節 observer-only synthetic experiment。此結果來自 Series B 既有 artifact，不屬於新的真實 LLM benchmark。

### Definitions
第 3、4、5、8、15 節。

### Proved results
- 定理 1：Sound Contraction。
- 命題 2：Relational Incompatibility Certificate 的可定位性與非唯一 truth attribution。
- 定理 3：等相關模型下的 effective observer number。

### Conjecture
猜想 1：Observer-Network Normalization Conjecture。

### Heuristic / design proposal
第 8、14、15、18 節。

### Explicitly not claimed
- 多 AI 共識等於真理；
- nominal agent count 必然降低 hallucination；
- 前一系列 synthetic observer experiment 等於真實 LLM hallucination benchmark；
- 計算機或 verifier 是完備 truth oracle；
- 現有 multi-agent system 已經達到 perfect autonomous epistemology。
