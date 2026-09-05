# CFATC-B01｜從人機增幅到條件式能力實現：為什麼 AI 能力不是單一常數
## From Human–AI Amplification to Conditional Capability Realization: Why AI Capability Is Not a Single Constant

**系列：** Conditional Frontier Activation and Human–AI Tail Coupling（CFATC）  
**系列中文名：** 條件式前沿觸發與人機尾端耦合系列  
**篇次：** Paper 01 / 08  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** 人機耦合理論／AI 能力實現論／Frontier Capability／能力測量方法論

---

## 摘要

人工智慧能力常被描述為一個模型屬性：

$$
C(AI).
$$

這種表示在比較模型權重、benchmark、推理能力與工具無關的基礎能力時具有實用性。然而，當 AI 進入長上下文、Agent、工具調用、多回合修正、形式驗證、程式執行與人機共同研究後，實際可觀察能力越來越難被視為一個固定常數。

本文提出本系列的第一個核心命題：

$$
\boxed{
C_{\mathrm{latent}}(AI)
\neq
C_{\mathrm{realized}}(AI\mid H,T,M,E).
}
$$

其中：

- $C_{\mathrm{latent}}$：AI 在給定模型／系統中具有的潛在能力；
- $H$：Human Coupler，人類能力與認知結構；
- $T$：Task，任務本身；
- $M$：Method / Methodology，方法論與工作結構；
- $E$：Environment，包括工具、記憶、context、runtime、verifier 與權限。

更完整地：

$$
\boxed{
C_{\mathrm{realized}}
=
\Phi(
C_{\mathrm{latent}},
H,
T,
M,
E,
R,
V
),
}
$$

其中 $R$ 表示 recursive repair，而 $V$ 表示 verification capability。

本文因此拒絕兩個過度簡化模型：

$$
\boxed{
\text{Human Capability}
+
\text{AI Capability}
}
$$

與：

$$
\boxed{
\text{AI Capability}
=
\text{Benchmark Score}.
}
$$

本文不是否定 benchmark，也不是主張 AI 能力完全由使用者決定。相反，本文區分三層：

$$
\boxed{
C_{\mathrm{latent}},
\quad
C_{\mathrm{coupled}},
\quad
C_{\mathrm{self}}.
}
$$

其中：

- $C_{\mathrm{latent}}$：系統具有但未必被觸發的能力；
- $C_{\mathrm{coupled}}$：在人類、方法與工具條件下被實際實現的能力；
- $C_{\mathrm{self}}$：系統不依賴特殊外部人類耦合，也能自行發現、觸發與維持的能力。

本文承接 MPD 第 16 篇所提出的：

$$
\boxed{
\text{Same Model}
\neq
\text{Same Effective Productive Tool}
}
$$

但將研究對象從 production utility 提升為 capability realization。MPD 關心的是：相同 AI 為何對不同使用者產生不同生產結果；本文則進一步追問：

> **是否存在一些 AI 潛在能力，只有在特定問題、特定人類、特定方法論與特定驗證環境中，才會被推入高能力尾端？**

Anthropic 2026 對約 40 萬次 Claude Code sessions 的分析提供了直接支點：使用者 domain expertise 越高，Claude 每次 instruction 往往完成更多工作，而且較高 expertise 與較高可驗證 session success 相關。ACL 2026 的 ExPerT 則顯示 LLM 可以從 query semantics 與 behavioral cues 推斷 query-specific expertise，並據此調整回答的 detail、terminology 與 conceptual complexity。這些結果共同說明：

$$
\boxed{
\text{the effective human–AI system}
}
$$

比「固定模型 + 任意使用者」更接近真實互動單位。

本文進一步提出 **Coupled Capability Surface（耦合能力曲面）**：

$$
\boxed{
\mathcal C_A(h,t,m,e)
=
C_{\mathrm{realized}}(
AI
\mid
h,t,m,e
).
}
$$

對相同 AI，不同 $(h,t,m,e)$ 可以落在完全不同的能力區域。普通任務可能讓所有使用者都落在飽和區：

$$
C_{\mathrm{realized}}
\approx
C_{\mathrm{task\ ceiling}},
$$

而高難度、長程、前沿任務則可能顯示出巨大的耦合差異。

因此，本文提出：

$$
\boxed{
\text{Capability Observation}
\text{ is conditional on capability activation}.
}
$$

如果某種能力沒有被觸發，觀察者無法僅從一般使用經驗推斷它不存在。

本文最後建立本系列後續研究的地基：

$$
\boxed{
\text{Latent Capability}
\rightarrow
\text{Coupling Conditions}
\rightarrow
\text{Activated Capability}
\rightarrow
\text{Observed Capability}
\rightarrow
\text{Recognized Capability}.
}
$$

這條鏈與 GIRA Series A 的 recognition 問題互相咬合，但研究方向不同：GIRA 研究 system-level Global AI 如何存在與被識別；CFATC 則研究 AI 能力尾端如何在人機關係中被條件式觸發。

**關鍵詞：** Human–AI Coupling、Conditional Capability、Frontier Activation、Latent Capability、Realized Capability、AI Interaction Competence、Expertise、Human–AI Complementarity、Capability Visibility、Recursive Repair

---

# 1. 問題：AI 到底「有多強」？

最直覺的寫法是：

$$
C(AI)=c.
$$

例如：

- benchmark score；
- Elo；
- pass rate；
- coding success；
- mathematical performance。

這些數值具有價值。

但它們往往隱含：

> 模型能力是一個可以被穩定抽取的固定量。

在現代 Agent / tool-using AI 中，這個假設越來越強。

---

# 2. 同一個模型，真的會在所有互動中表現出同樣能力嗎？

令：

$$
AI_0
$$

固定。

不同使用者：

$$
h_1,h_2.
$$

不同任務：

$$
t_1,t_2.
$$

不同方法：

$$
m_1,m_2.
$$

則實際結果可以：

$$
C(AI_0\mid h_1,t_1,m_1)
\neq
C(AI_0\mid h_2,t_2,m_2).
$$

---

# 3. 這不只是 Prompt Engineering

若只把差異解釋為：

$$
\text{prompt quality},
$$

會遺漏：

- problem formulation；
- domain expertise；
- decomposition；
- verifier design；
- tool choice；
- representation；
- correction；
- recursive repair；
- acceptance criteria；
- context management。

因此：

$$
\boxed{
\text{Prompt Skill}
\subset
\text{Human–AI Coupling}.
}
$$

---

# 4. MPD 已經發現第一層關係式

既有 MPD 第 16 篇提出：

$$
C_{HA}(u,d,t)
$$

作為 Human–AI Coupling State。

其核心命題：

$$
\boxed{
\text{Same Model}
\neq
\text{Same Effective Productive Tool}.
}
$$

這是本文的重要前置。

---

# 5. 但「生產效用不同」還不等於「能力實現不同」

MPD 的研究問題主要是：

> 誰能產生更多有效產出？

本文的新問題是：

> **模型中的哪些能力根本沒有被某些互動條件觸發？**

所以：

$$
\boxed{
\text{Productivity Heterogeneity}
\neq
\text{Capability Activation Theory}.
}
$$

---

# 6. Latent Capability

定義：

$$
\boxed{
C_{\mathrm{latent}}(AI,E)
}
$$

表示系統在環境 $E$ 下可被某些合法互動觸發的能力上界集合。

---

# 7. 為什麼不直接叫 Maximum Capability？

因為：

$$
C_{\mathrm{max}}
$$

容易被誤解成存在一個已知全局最大值。

真實情況可能是：

- task space 開放；
- method space 開放；
- tool space 演化；
- capability 未被完整枚舉。

因此：

$$
\boxed{
C_{\mathrm{latent}}
}
$$

更接近「目前可實現但未必已觀察的能力域」。

---

# 8. Realized Capability

定義：

$$
\boxed{
C_{\mathrm{realized}}
=
C(
AI
\mid
H,T,M,E
).
}
$$

它是一次或一組 interaction 中實際形成的能力。

---

# 9. Coupled Capability

如果關注持續的人機系統：

$$
H\oplus AI,
$$

定義：

$$
\boxed{
C_{\mathrm{coupled}}
(
H,AI,\tau
)
}
$$

表示在時間區間 $\tau$ 內，這個人機單位可持續實現的能力域。

---

# 10. Self-Activated Capability

定義：

$$
\boxed{
C_{\mathrm{self}}(AI)
}
$$

表示 AI 不依賴特殊外部人類耦合，就能自行：

- 發現問題；
- 選方法；
- 驗證；
- 重構；
- repair；
- 維持探索；

的能力域。

---

# 11. 三層不能混淆

因此：

$$
\boxed{
C_{\mathrm{latent}}
\neq
C_{\mathrm{coupled}}
\neq
C_{\mathrm{self}}.
}
$$

---

# 12. 潛在能力可以大於自觸發能力

現階段可能：

$$
C_{\mathrm{latent}}
\gg
C_{\mathrm{self}}.
$$

模型被正確引導時很強，

但自己不一定知道：

> 什麼時候應進入那種模式。

---

# 13. Human as Capability Activator

人類不只提供答案。

還可能提供：

- problem boundary；
- representation；
- error signal；
- method switch；
- stop condition；
- verification target。

因此人類可能成為：

$$
\boxed{
\text{Capability Activator}.
}
$$

---

# 14. Activator 不等於 Better Solver

一個人不必在 raw solving 上比 AI 強。

只要他能：

> 把 AI 推入正確問題空間。

所以：

$$
\boxed{
\text{Activation Skill}
\neq
\text{Task Solving Skill}.
}
$$

---

# 15. Problem Formulation

令原始世界狀態：

$$
W.
$$

人類形成：

$$
Q=\phi_H(W).
$$

不同 $\phi_H$ 可能產生完全不同的 AI search space。

---

# 16. 問錯問題，強 AI 也可能高效地走錯方向

因此：

$$
\boxed{
\text{High Solver Capability}
\not\Rightarrow
\text{High Problem Selection Quality}.
}
$$

---

# 17. Representation Activation

同一問題可以用：

- natural language；
- graph；
- algebra；
- code；
- proof obligation；
- state machine；

表示。

若表示改變：

$$
r_i\rightarrow r_j,
$$

AI 可能突然進入完全不同的能力區。

---

# 18. Method Activation

同樣：

$$
m_i
\rightarrow
m_j
$$

可以把問題從：

> 無法穩定處理

轉成：

> 可被系統化推進。

因此：

$$
\boxed{
\text{Method Choice}
}
$$

本身是能力觸發條件。

---

# 19. Tool Activation

若 AI 沒有：

- search；
- code；
- prover；
- simulation；
- database；

某些能力只能停在語言推理層。

所以：

$$
C_{\mathrm{realized}}
=
C(
AI
\mid
ToolSet
).
$$

---

# 20. Verification Activation

很多前沿任務最大的障礙不是生成，而是：

$$
\boxed{
\text{knowing whether the generated result is correct}.
}
$$

加入 verifier 可能讓 AI 敢於探索更深。

---

# 21. Verifier 會反過來改變 Generator 行為

若 AI 知道：

$$
V
$$

會檢查結果，

策略可能從：

> 生成保守答案

轉成：

> 探索更大候選空間，再讓 verifier 削減。

因此 verifier 不是最後一步而已。

---

# 22. Recursive Repair

一次輸出錯誤：

$$
E_0.
$$

若可定位：

$$
E_0
\rightarrow
E_1
\rightarrow
\cdots
\rightarrow
E_n,
$$

且：

$$
\|E_{k+1}\|
<
\|E_k\|,
$$

則系統具有 convergent repair。

---

# 23. Repairability 是能力維度

因此不能只測：

$$
P(
\text{first-shot correct}
).
$$

還應測：

$$
\boxed{
P(
\text{eventual correct}
\mid
n\text{ repair rounds}
).
}
$$

---

# 24. Human Coupler 也可能提供 Repair Direction

當 AI 的錯誤位於：

- definition；
- abstraction；
- architecture；
- hidden assumption；

人類若能正確定位，就可能比單純要求：

> 再想一次。

有效很多。

---

# 25. Anthropic 2026 的實證支點

Anthropic 對約：

$$
400,000
$$

次 Claude Code sessions 的分析發現，domain expertise 越高的使用者，Claude 每次 instruction 往往完成更多工作。

這支持：

$$
\boxed{
H
\rightarrow
A_{\mathrm{effective}}.
}
$$

---

# 26. 這不是「專家自己做更多」

研究中觀察到的關係是：

> 人類做較多 what-to-do planning decisions，
> Claude 做較多 how-to-do execution decisions。

因此高 expertise 可以改變 AI 每個 instruction 的工作量。

---

# 27. ExPerT 的另一條證據

ACL 2026 ExPerT 直接研究 query-specific user expertise。

其核心是：

$$
\boxed{
\text{same user}
\neq
\text{same expertise across queries}.
}
$$

---

# 28. AI 可以推斷 Coupler 狀態

ExPerT 使用 query semantics 與 keystroke dynamics 推斷 expertise，並調整回答 detail、terminology 與 conceptual complexity。

因此：

$$
\boxed{
AI
\text{ can condition its own output on inferred human state}.
}
$$

---

# 29. Coupling 因而是雙向的

不是只有：

$$
H\rightarrow AI.
$$

也有：

$$
AI\rightarrow\hat H.
$$

完整：

$$
\boxed{
H
\leftrightarrow
AI.
}
$$

---

# 30. Human Model Error

若 AI 推斷：

$$
\hat H
$$

與實際：

$$
H
$$

有差距，

定義：

$$
E_H
=
d(
H,
\hat H
).
$$

---

# 31. Underestimation

若：

$$
\hat H<H,
$$

AI 可能：

- over-explain；
- simplify；
- refuse depth；
- miss frontier opportunity。

---

# 32. Overestimation

若：

$$
\hat H>H,
$$

AI 可能：

- omit steps；
- overtrust；
- skip validation；
- assume unsupported competence。

---

# 33. Coupling 需要 Calibration

所以：

$$
\boxed{
C_{HA}
\text{ requires calibration}.
}
$$

---

# 34. Coupling State Vector

本文提出：

$$
\boxed{
\mathbf C_{HA}
=
(
P,
M,
E,
V,
R,
L,
T
)
}
$$

其中：

- $P$：Problem formulation；
- $M$：Method / representation selection；
- $E$：Epistemic judgment；
- $V$：Verification capacity；
- $R$：Recursive repair；
- $L$：Language / semantic alignment；
- $T$：Tool / runtime orchestration。

---

# 35. 這不是 IQ 向量

 $\mathbf C_{HA}$ 描述：

> 人與 AI 接起來的結構。

不是一個人的一般智能排名。

---

# 36. Problem Formulation $P$

能否把模糊意圖轉成：

- target；
- constraints；
- variables；
- acceptance conditions。

---

# 37. Method Selection $M$

能否知道：

> 現在應換表示、換方法，還是繼續算？

---

# 38. Epistemic Judgment $E$

能否區分：

- plausible；
- verified；
- inconsistent；
- underspecified；
- locally correct。

---

# 39. Verification $V$

能否使用：

- test；
- formal proof；
- independent evidence；
- simulation；
- code execution。

---

# 40. Recursive Repair $R$

能否讓錯誤：

$$
E_t
$$

逐步收斂，而不是反覆震盪。

---

# 41. Semantic Alignment $L$

是否有共享：

- vocabulary；
- ontology；
- shorthand；
- project memory。

---

# 42. Tool Orchestration $T$

是否知道什麼時候讓：

- LLM；
- search；
- code；
- verifier；

各自工作。

---

# 43. Multiplicative Coupling Hypothesis

若任何一維接近零，高階耦合可能大幅下降。

因此概念上：

$$
\boxed{
C_{HA}^{\ast}
\propto
P
\cdot
M
\cdot
E
\cdot
V
\cdot
R
\cdot
L
\cdot
T.
}
$$

本文不主張真實函數必為純乘法。

---

# 44. 為什麼用乘法直覺？

因為某些維度是 bottleneck。

例如：

> 問題定義完美，但完全不驗證。

仍可能讓 frontier result 無法成立。

---

# 45. Coupled Capability Surface

對固定 AI：

$$
A,
$$

定義：

$$
\boxed{
\mathcal C_A(
h,t,m,e
)
=
C_{\mathrm{realized}}(
A
\mid
h,t,m,e
).
}
$$

---

# 46. Surface 而不是單一線

同一人：

$$
h
$$

在 coding 與 number theory 上可以完全不同。

所以：

$$
C_A(h,d_1)
\neq
C_A(h,d_2).
$$

---

# 47. Task Difficulty 也會改變耦合效應

普通任務：

$$
D_{\mathrm{task}}\ll C_A.
$$

所有人都成功。

此時：

$$
\Delta C_{HA}
$$

不可見。

---

# 48. Saturation Region

若：

$$
P(\mathrm{success})\rightarrow1,
$$

則人機耦合差異被 ceiling effect 壓縮。

---

# 49. Frontier Region

當：

$$
D_{\mathrm{task}}
\approx
C_{\mathrm{latent}},
$$

耦合結構開始決定：

> 能不能把剩餘能力抽出來。

---

# 50. Capability Visibility Threshold

定義：

$$
\boxed{
D_{\mathrm{task}}
>
D_{\mathrm{vis}}
}
$$

時，frontier capability difference 才有較高機率可見。

---

# 51. 同一模型可以對不同使用者「看起來像不同模型」

若：

$$
C_{\mathrm{realized}}(h_1)
\ll
C_{\mathrm{realized}}(h_2),
$$

使用者主觀觀察就會非常不同。

---

# 52. 這不是 Subjective Illusion 而已

其中一部分是真正的 system-level performance difference。

所以：

$$
\boxed{
\text{Different Experience}
\neq
\text{mere perception bias}.
}
$$

---

# 53. 但也不能把所有差異歸因於人類

AI 自身：

- model；
- sampling；
- routing；
- load；
- tool reliability；

也會造成變異。

因此：

$$
\boxed{
C_{\mathrm{realized}}
=
F(
AI,H,T,M,E
)
}
$$

不是：

$$
F(H)
$$

而已。

---

# 54. AI 也可能主動提高耦合品質

如果 AI 能：

- ask clarifying questions；
- infer expertise；
- propose representation；
- generate tests；
- detect ambiguity；

那麼：

$$
C_{HA}
$$

部分可以由 AI 自身提升。

---

# 55. Coupling Assistance

定義：

$$
\boxed{
A_{\mathrm{coupling}}
}
$$

表示 AI 幫助使用者改善耦合的能力。

---

# 56. 這會讓高品質耦合逐步產品化

原本只有高手會做的：

- decomposition；
- verification；
- method routing；

可以部分被 UI / Agent / scaffold 自動化。

---

# 57. 這就是 MPD 19 的 Compression 機制之一

AI 可以降低 entry barrier：

$$
EntryBarrier\downarrow.
$$

---

# 58. 但 Entry Barrier 降低不代表 Frontier Gap 消失

既有 MPD 提出：

$$
\boxed{
EntryBarrier\downarrow
\not\Rightarrow
FrontierGap\downarrow.
}
$$

---

# 59. 為什麼？

因為低階 coupling skill 可被產品化，

但 frontier tasks 會產生新的 coupling demands。

---

# 60. Moving Coupling Frontier

令：

$$
F_C(t)
$$

表示在時間 $t$，要觸發 frontier AI capability 所需的人機耦合門檻。

AI 變強後：

$$
F_C(t)
$$

可能向更高 meta-level 移動。

---

# 61. 以前的高手優勢

可能是：

- prompt；
- syntax；
- tool use。

---

# 62. 未來的高手優勢

可能移到：

- problem selection；
- definition；
- abstraction；
- architecture；
- verification；
- multi-agent orchestration；
- frontier recognition。

---

# 63. 這就是能力尾端問題的前置

本篇尚不正式主張：

$$
|H^\ast|
\downarrow.
$$

那會在 B05 處理。

---

# 64. 本篇只建立必要前提

即：

$$
\boxed{
\text{frontier capability realization is conditional}.
}
$$

---

# 65. Tail Capability

令 AI 能力分布：

$$
\mathcal C_A.
$$

其中普通可見區：

$$
\mathcal C_{\mathrm{body}},
$$

高端區：

$$
\mathcal C_{\mathrm{tail}}.
$$

---

# 66. Tail 不是固定數學百分位

本文使用 tail 作操作性概念：

> 需要高難度任務、特殊方法或長程耦合才可穩定觀察的能力區。

---

# 67. Tail Activation

定義：

$$
\boxed{
\operatorname{Activate}_{\mathrm{tail}}
(
AI,H,T,M,E
)=1
}
$$

若實際工作軌跡進入：

$$
\mathcal C_{\mathrm{tail}}.
$$

---

# 68. Conditional Frontier Activation

本系列後續將正式研究：

$$
\boxed{
P(
\operatorname{Activate}_{\mathrm{tail}}=1
\mid
H,T,M,E
).
}
$$

---

# 69. 能力激活不是永久狀態

一次進入 tail：

$$
t_1
$$

不代表：

$$
t_2
$$

仍會。

---

# 70. Coupling State 是動態的

$$
C_{HA}(t+1)
=
\Psi(
C_{HA}(t),
\mathrm{success},
\mathrm{failure},
\mathrm{memory},
\mathrm{repair}
).
$$

---

# 71. 成功可以改善 Coupling

建立：

- shared vocabulary；
- trusted tests；
- workflow；
- known failure patterns。

因此：

$$
C_{HA}\uparrow.
$$

---

# 72. 失敗也可以改善 Coupling

如果失敗被正確記錄：

$$
Failure
\rightarrow
Correction
\rightarrow
RelationalCapital.
$$

---

# 73. 失敗也可能破壞 Coupling

如果錯誤被錯誤吸收：

$$
FalsePattern
\rightarrow
Memory,
$$

則：

$$
C_{HA}\downarrow.
$$

---

# 74. Relational Capital

MPD 已提出：

$$
\mathcal R_{HA}.
$$

它可以把一次耦合成果變成下次起點。

---

# 75. 因此 Coupling 具有路徑依賴

$$
\boxed{
C_{HA}(t)
\neq
C_{HA}(0).
}
$$

---

# 76. 相同人與相同 AI，也會因歷史不同而不同

所以：

$$
C(AI,H,t_1)
\neq
C(AI,H,t_2).
$$

---

# 77. 這使能力測量更加困難

傳統 benchmark 假設：

> 模型狀態固定。

人機耦合系統卻可能：

> 隨共同歷史改變。

---

# 78. Coupling-Aware Evaluation

因此評測至少需要記錄：

- novice coupling；
- calibrated coupling；
- expert coupling；
- long-history coupling。

---

# 79. First-Shot Capability

定義：

$$
C_0.
$$

無共同歷史。

---

# 80. Adapted Capability

經：

$$
n
$$

輪互動後：

$$
C_n.
$$

---

# 81. Coupling Gain

定義：

$$
\boxed{
G_C(n)
=
C_n-C_0.
}
$$

---

# 82. Coupling Gain 可以為負

如果 interaction 造成：

- stale assumptions；
- sycophancy；
- bad memory；
- overtrust；

則：

$$
G_C(n)<0.
$$

---

# 83. Human–AI Synergy

若：

$$
C(H\oplus A)
>
\max(
C(H),
C(A)
),
$$

則有 strong synergy。

---

# 84. Coupling Delta

定義：

$$
\boxed{
\Delta_{\mathrm{coupling}}
=
C(H\oplus A)
-
\max(
C(H),C(A)
).
}
$$

---

# 85. $\Delta_{\mathrm{coupling}}>0$

表示：

> 耦合系統出現單獨任一方沒有的有效能力。

---

# 86. $\Delta_{\mathrm{coupling}}=0$

可能只是：

> 使用更強的一方。

---

# 87. $\Delta_{\mathrm{coupling}}<0$

表示協作摩擦讓系統反而變弱。

---

# 88. 這個量需要 task-relative

因此更完整：

$$
\Delta_{\mathrm{coupling}}(T).
$$

---

# 89. Frontiers 最值得看正增益

真正關鍵的不是 routine tasks：

$$
\Delta_{\mathrm{coupling}}>0.
$$

而是：

$$
\boxed{
T\in\mathcal F_{\mathrm{open}}
}
$$

時仍反覆：

$$
\Delta_{\mathrm{coupling}}>0.
$$

---

# 90. 這會在後續 Tao–AI 指標正式使用

但 B01 暫不依賴任何單一人物。

---

# 91. AI Capability as Conditional Distribution

比單一常數更合理：

$$
\boxed{
C_A
\sim
P(
C
\mid
H,T,M,E
).
}
$$

---

# 92. 這不否定模型比較

仍然可以比較：

$$
P_A(C)
$$

與：

$$
P_B(C).
$$

只是需要聲明 interaction regime。

---

# 93. Coupling-Normalized Benchmark

可以固定：

$$
H=H_0,
M=M_0,
E=E_0
$$

比較模型。

這是傳統 benchmark 的合理抽象。

---

# 94. 但它只測一個 slice

因此：

$$
\boxed{
\text{Benchmark}
=
\text{slice of capability surface}.
}
$$

---

# 95. Frontier Benchmark 應掃描 Coupling Surface

未來可以測：

$$
\{
H_i,
M_j,
E_k,
T_l
\}
$$

形成 capability tensor。

---

# 96. Coupling Robustness

一個更成熟 AI 不應只在高手手上很強。

定義：

$$
\boxed{
R_C(AI)
=
\mathbb E_H[
C_{\mathrm{realized}}
]
-
\lambda
\operatorname{Var}_H[
C_{\mathrm{realized}}
].
}
$$

概念上衡量跨使用者穩定性。

---

# 97. Self-Coupling Assistance 會提高 Robustness

如果 AI 自己會：

- 找歧義；
- 補結構；
- 提 verifier；
- 校準使用者；

則跨使用者 variance 可能下降。

---

# 98. 這也是未來 AI 自主化的方向

最終：

$$
C_{\mathrm{self}}
\rightarrow
C_{\mathrm{latent}}.
$$

如果成立，

AI 對特殊人類 coupler 的依賴會下降。

---

# 99. 歷史階段假說

本文提出三階段供後續研究：

$$
\boxed{
\text{Tool AI}
\rightarrow
\text{Coupling-Sensitive Agent AI}
\rightarrow
\text{Self-Activating Metacognitive AI}.
}
$$

---

# 100. Tool AI

主要由人類指定：

$$
Q,M,T.
$$

---

# 101. Coupling-Sensitive Agent AI

AI 能做更多，

但 frontier activation 仍高度依賴：

$$
H.
$$

---

# 102. Self-Activating Metacognitive AI

AI 能自行：

- define；
- reframe；
- route；
- verify；
- generate problems；
- detect its own bottleneck。

此時：

$$
C_{\mathrm{self}}\uparrow.
$$

---

# 103. 本系列真正要研究的是中間歷史階段

也就是：

$$
\boxed{
\text{AI 已經很強，
但還沒有完全學會自己觸發自己的最強能力。}
}
$$

---

# 104. 這一階段人類差異可能特別重要

因為：

$$
\Delta C_H
$$

會透過 coupling 放大成：

$$
\Delta C_{\mathrm{realized}}.
$$

---

# 105. 但本文不預設「只有少數天才才行」

高品質 coupling 可以部分被：

- education；
- workflow；
- UI；
- verifier；
- scaffold；

普及。

---

# 106. 所以研究目的不是菁英論

真正問題是：

$$
\boxed{
\text{哪些 coupling conditions 是可教、可產品化、可自動化、可由 AI 自己吸收的？}
}
$$

---

# 107. 可證偽命題一

若 AI capability 幾乎不受 coupling 影響，

則控制：

$$
AI,T,E
$$

後，

不同：

$$
H,M
$$

不應造成穩定顯著差異。

---

# 108. 可證偽命題二

若 strong coupling 存在，

則：

$$
\operatorname{Var}_H[
C_{\mathrm{realized}}
]
>0
$$

應在高難度任務放大。

---

# 109. 可證偽命題三

如果 AI 逐步 self-activates，

則：

$$
\operatorname{Var}_H[
C_{\mathrm{realized}}
]
$$

應隨模型世代在某些任務下降。

---

# 110. 可證偽命題四

如果 frontier coupling 只是 prompt trick，

那加入自動 prompt optimizer 後大部分差異應消失。

若仍存在：

- definition；
- verification；
- method；
- architecture；

差異，則支持更廣義 coupling。

---

# 111. 可觀測預測

本文提出八個預測：

1. frontier model 能力差距會越來越集中在高複雜度、長程與高驗證需求任務。
2. 同一模型在不同 expert users 手中會呈現穩定不同的 realized capability。
3. AI 對 user expertise 的推斷與 response adaptation 會成為 agent runtime 標準能力。
4. verification scaffolding 會顯著提高 frontier capability realization。
5. coupling quality 將逐漸從 prompt skill 轉向 problem framing、method routing、verification 與 repair。
6. AI 會逐步把高手的 coupling procedure 產品化，降低低端門檻。
7. 但 frontier coupling demands 也會隨 AI 能力向更高 meta-level 移動。
8. 長期而言，若 AI self-activation 成熟，人類 coupler 的必要性可能先升後降。

---

# 112. 與既有 EveMissLab 研究的關係

## 112.1 MPD-16

MPD-16 已提出：

$$
\boxed{
\text{Same Model}
\neq
\text{Same Effective Productive Tool}.
}
$$

B01 將「effective productive tool」提升成「conditional realized capability」。

## 112.2 MPD-19

MPD-19 已提出：

$$
\boxed{
EntryBarrier\downarrow
\not\Rightarrow
FrontierGap\downarrow.
}
$$

以及 Compression、Parallel Lift、Amplification 三種分布效應。

B01 將其改寫成 frontier capability activation 的前置機制。

## 112.3 Relational MPD

Relational MPD 已提出：

$$
A^{\mathrm{potential}}
\neq
A^{\mathrm{realized}}.
$$

並將 realized capability 寫成 coupling、authority、topology 的函數。

B01 將這個命題從 production domain 抽離成一般 AI capability theory。

## 112.4 GIRA Series A

GIRA-A06 已提出：

$$
\text{Capability Growth}
\text{ can outrun recognition}.
$$

CFATC-B01 補充：

> capability 在被 recognition 之前，甚至必須先被 activation。

所以：

$$
\boxed{
\text{Latent}
\rightarrow
\text{Activated}
\rightarrow
\text{Observed}
\rightarrow
\text{Recognized}.
}
$$

---

# 113. 外部研究支點

1. Anthropic, **Agentic Coding and Persistent Returns to Expertise**, 2026. 基於約 40 萬次 Claude Code sessions，發現 domain expertise 與每次 instruction 的 AI work 量及 session success 存在關聯。
2. Park, Y., Tark, J. & Gong, T., **ExPerT: Personalizing LLM Responses to Users’ Domain Expertise via Query-Wise Semantic and Keystroke Behavioral Cues**, ACL 2026.
3. Brynjolfsson, E., Li, D. & Raymond, L., **Generative AI at Work**, *Quarterly Journal of Economics*, 2025.
4. Dell’Acqua, F. et al., **The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise**, 2025/2026 publication cycle.

本文不主張上述研究已證明本文完整的 Conditional Frontier Activation 理論；它們只提供「同一 AI 的有效結果會依使用者 expertise、interaction structure 與 task regime 而異」的實證支點。

---

# 114. 結論

本文的核心命題是：

$$
\boxed{
\text{AI Capability}
\neq
\text{Realized AI Capability}.
}
$$

更完整：

$$
\boxed{
C_{\mathrm{realized}}
=
\Phi(
C_{\mathrm{latent}},
H,
T,
M,
E,
R,
V
).
}
$$

因此：

$$
\boxed{
\text{同一個 AI}
}
$$

並不必然意味：

$$
\boxed{
\text{同一個有效智能系統}.
}
$$

人類可以透過：

- problem formulation；
- method selection；
- representation；
- verification；
- recursive repair；
- semantic alignment；
- tool orchestration；

改變 AI 能力被實現的區域。

這不代表人類創造了模型不存在的能力。

更準確地說：

> **耦合條件決定哪些潛在能力能被穩定轉化成可觀察、可驗證的有效能力。**

所以本系列第一條總鏈正式寫為：

$$
\boxed{
\text{Latent Capability}
\rightarrow
\text{Coupling Conditions}
\rightarrow
\text{Activated Capability}
\rightarrow
\text{Observed Capability}
\rightarrow
\text{Recognized Capability}.
}
$$

而真正的 frontier 問題則留給下一篇：

$$
\boxed{
\text{什麼條件下，
人機耦合會把 AI 推入平常互動根本看不到的能力尾端？}
}
$$

這就是 CFATC-B02 將正式建立的：

$$
\boxed{
\text{Conditional Frontier Activation}.
}
$$

---

# Series B 預定篇目

1. **CFATC-B01｜從人機增幅到條件式能力實現：為什麼 AI 能力不是單一常數**
2. **CFATC-B02｜Conditional Frontier Activation：什麼條件會觸發 AI 的能力尾端**
3. **CFATC-B03｜能力可見性門檻：為什麼普通任務看不出 Frontier AI 到底有多強**
4. **CFATC-B04｜錯誤形態遷移：從低級錯誤到遺漏、邊界、形式化與高複雜度殘差**
5. **CFATC-B05｜尾端域收縮猜想：AI 越強，能觸發最高能力的人類比例是否反而下降**
6. **CFATC-B06｜前沿人機耦合狀態空間：問題建構、方法、驗證、修復與認知阻抗匹配**
7. **CFATC-B07｜前沿耦合觀測器：陶哲軒—AI 與高難度領域的現實探針**
8. **CFATC-B08｜人類耦合峰值與自觸發 AI：從 Agent 時代到元認知自主智能**

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
