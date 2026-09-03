# LRC–COL-08：語言穩定步數、語義漂移與穩定窗口
## Language Stabilization Steps, Semantic Drift, and Stability Windows

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL-07 定義了 AI 學習一個複合 operator 所需的時間與有效 exposure，並以 $T_{\epsilon}^{learn}$ 描述 Agent 何時進入可泛化、可執行的 operational competence。然而，「某個 Agent 已經學會某個 operator」並不代表「這個 operator 的語義已經穩定」。

一套語言可以被不同 Agent 學會，卻在反覆使用、壓縮、展開、轉述、跨 Agent 傳播、模型升級與版本更新中逐步改變意思。相反地，多個 Agent 也可能高度一致地使用同一錯誤語義：此時 inter-agent disagreement 很低，但語言已偏離原本的 semantic anchor 或 world-grounded behavior。故：

$$
\boxed{
\text{Convergence}
\neq
\text{Stability}
\neq
\text{Correctness}.
}
$$

本文提出 **Language Stabilization Steps（語言穩定步數）** 與 **Semantic Stability Window（語義穩定窗口）**，正式定義：

$$
\boxed{
K_{\epsilon}^{stable}
}
$$

作為：一個 operator 或 operator language 經過一定數量的有效使用、重組、跨 Agent 傳播與版本事件之後，首次進入一段持續窗口，在該窗口內，其語義錨點、行為簽名、跨 Agent 差異、組合保真與外部 grounding 均維持在指定誤差界內所需的最小有效步數。

本文提出三種互補的穩定性：

1. **Internal Stability**：同一 Agent / 同一版本隨時間是否維持一致；
2. **Population Stability**：不同 Agents 是否對同一 operator 維持足夠一致的行為與語義；
3. **Anchored Stability**：上述一致性是否仍然符合原始 semantic contract、formal expansion、world-grounded behavior 與 failure boundary。

因此，真正的穩定條件不是「大家說法一致」，而是：

$$
\boxed{
\text{Low Temporal Drift}
+
\text{Low Cross-Agent Variance}
+
\text{High Anchor Fidelity}.
}
$$

本文進一步定義 Semantic Drift Trajectory、Behavioral Signature、Anchor Deviation、Cross-Agent Semantic Variance、Semantic Invariant Set、Drift Budget、False Convergence、Frozen Error、Metastable Window、Regrounding、Semantic Checksum 與 Stability Hysteresis。

近期 emergent-communication 研究提供重要外部錨點：2026 年 CoNLL 研究顯示 dynamic population 中過高 plasticity 會使共享語言變動過快，而過低 plasticity 又難以整合 newcomers；age-based plasticity 可顯著降低 language drift。2025 年 LLM iterated-transmission 工作則顯示代際傳播可提高人工語言的 learnability，但也可能形成 degenerate vocabularies。2026 年 emergent-language phrasebook 研究進一步顯示，形式—意義 mapping 的局部結構與 morpheme ordering / repetition 能直接影響 agent 是否真的能「說」與「聽」一套 emergent language，說明 stability 必須以 operational behavior 校準，而不能只看表面字串相似度。

本文核心結論是：

$$
\boxed{
\text{A language is not stable when it stops changing;}
}
$$

而是：

$$
\boxed{
\text{it is stable when relevant change remains inside a bounded semantic and operational invariant envelope for a sustained window.}
}
$$

因此，未來複合 operator language 應追求的是**可塑但有界的 metastable language**，而不是完全 frozen 的 language。

---

## 關鍵詞

semantic drift；language stabilization；stability window；operator semantics；false convergence；emergent communication；multi-agent language；semantic invariant；metastability；language grounding

---

# 1. 學會與穩定是兩個不同問題

上一章問：

> Agent 需要多久才能學會 operator？

本章問：

> operator 經過多少次使用、傳播與更新之後，語義才開始穩定？

因此：

$$
\boxed{
T_{\epsilon}^{learn}
\neq
K_{\epsilon}^{stable}.
}
$$

前者偏 learner。

後者偏 language ecology。

---

# 2. 一個 Agent 可以學會正在漂移的語言

假設：

$$
O@t_1
$$

的意思是：

> 驗證後執行。

但經過多輪傳播：

$$
O@t_2
$$

逐漸被理解成：

> 高 confidence 時直接執行。

新 Agent 仍可能非常快學會：

$$
O@t_2.
$$

因此：

$$
\boxed{
\text{fast learning}
\not\Rightarrow
\text{semantic continuity}.
}
$$

---

# 3. 全體一致也可能全部漂錯

假設：

$$
A_1,A_2,\ldots,A_n
$$

最後對 $O$ 的理解完全一致：

$$
Var_A(O)\approx0.
$$

但它們共同偏離原始 contract：

$$
D(
Sem_t(O),
Anchor(O)
)
\gg0.
$$

這就是：

$$
\boxed{
\text{False Convergence}.
}
$$

---

# 4. Convergence、Stability、Correctness

本文正式區分：

### Convergence

不同 Agent 越來越相似。

### Stability

同一語言在一段時間／事件窗口內變化很小。

### Correctness / Fidelity

語言仍符合：

- semantic anchor；
- formal expansion；
- intended world behavior。

所以：

$$
\boxed{
C
\neq
S
\neq
F.
}
$$

---

# 5. Semantic State

令：

$$
S_O(t)
$$

表示 operator $O$ 在時間 $t$ 的語義狀態。

它不是單一 dictionary definition。

可包含：

$$
\boxed{
S_O(t)
=
(
D_t,
T_t,
P_t,
B_t,
F_t,
X_t
).
}
$$

其中：

- $D_t$：definition；
- $T_t$：type / domain；
- $P_t$：precondition / postcondition；
- $B_t$：behavioral signature；
- $F_t$：failure / stop semantics；
- $X_t$：expansion / executable contract。

---

# 6. 語義漂移不等於文字改寫

如果：

> 「驗證後才執行」

改寫成：

> 「先確認，再動作」

表面字串變了，

但 operational semantics 可能沒變。

因此：

$$
\boxed{
\text{Surface Drift}
\neq
\text{Semantic Drift}.
}
$$

---

# 7. Semantic Drift

本文定義：

$$
\boxed{
D_{sem}(O;t_1,t_2)
=
D_S(
S_O(t_1),
S_O(t_2)
).
}
$$

其中：

$$
D_S
$$

不是只有 embedding distance，

而應包含：

- definition difference；
- behavior difference；
- type difference；
- boundary difference；
- execution difference。

---

# 8. Drift Vector

更合理地：

$$
\boxed{
\mathbf D_O
=
(
D_{def},
D_{type},
D_{beh},
D_{bound},
D_{exec},
D_{ground}
).
}
$$

不同 operator 可用不同權重。

---

# 9. Behavioral Signature

對 operator $O$ 建 probe set：

$$
\mathcal P
=
\{p_1,\ldots,p_m\}.
$$

在時間 $t$：

$$
\boxed{
B_O(t)
=
(
Resp(O,p_1,t),
\ldots,
Resp(O,p_m,t)
).
}
$$

如果 definition 沒變，

但 behavior signature 改變，

仍然是 operational drift。

---

# 10. Novel Probe Requirement

probe 不能永遠是同一組。

否則 Agent 可能：

- memorise benchmark；
- overfit examples。

因此：

$$
\mathcal P_t
$$

應包含：

- stable regression probes；
- novel structural probes；
- adversarial boundary probes。

---

# 11. Semantic Anchor

每個 stable operator 至少需要：

$$
\boxed{
A_O
}
$$

semantic anchor。

可以由：

- canonical definition；
- formal expansion；
- type contract；
- invariants；
- reference examples；
- world-grounded outcomes；

共同構成。

---

# 12. Anchor Fidelity

定義：

$$
\boxed{
F_A(O,t)
=
1-
D_A(
S_O(t),
A_O
).
}
$$

若：

$$
F_A\rightarrow1,
$$

代表目前語義接近 anchor。

---

# 13. Anchor 不應只是一段自然語言

如果 anchor 只有：

> 「這個 operator 大概是 XXX。」

它自己也可能被重新解讀。

所以最好同時保存：

$$
\boxed{
\text{Text}
+
\text{Types}
+
\text{Examples}
+
\text{Counterexamples}
+
\text{Expansion}
+
\text{Tests}.
}
$$

---

# 14. Semantic Invariant Set

定義：

$$
\boxed{
\mathcal I(O)
=
\{
I_1,\ldots,I_k
\}.
}
$$

例如：

```text
Must verify before irreversible execution.
Must preserve target resource identity.
Must expose rollback status.
Must not silently change authorization scope.
```

只要這些 invariants 維持，

允許 surface form 與 local implementation 改變。

---

# 15. Stability Is an Invariant Envelope

因此真正穩定不是：

$$
S_O(t+1)=S_O(t).
$$

而是：

$$
\boxed{
S_O(t)
\in
\mathcal E_{\epsilon}(
\mathcal I(O)
).
}
$$

即：

> 變化仍留在允許 semantic envelope 內。

---

# 16. Frozen Language 不是理想

如果：

$$
S_O(t)
$$

永遠不能改，

新 domain 出現時：

- 無法適應；
- 無法修 bug；
- 無法提升 fidelity。

所以：

$$
\boxed{
\text{Stability}
\neq
\text{Immutability}.
}
$$

---

# 17. Metastability

本文更偏好：

$$
\boxed{
\text{Metastable Language}.
}
$$

即：

- 短中期穩定；
- 長期可版本化；
- 有 bounded plasticity；
- 有 regrounding / migration。

---

# 18. Temporal Drift

對同一 Agent / 同一 runtime：

$$
\boxed{
D_T(O;k)
=
D_{sem}(O;t,t+k).
}
$$

這衡量：

> 時間／事件推進後自己漂多少。

---

# 19. Cross-Agent Semantic Variance

對：

$$
A_1,\ldots,A_n,
$$

定義：

$$
\boxed{
V_A(O,t)
=
\mathbb E_i
[
D_S(
S_O^{A_i}(t),
\bar S_O(t)
)
].
}
$$

衡量群體對同一 operator 的分歧。

---

# 20. Internal Consensus 不是 Anchor Fidelity

可能：

$$
V_A\approx0
$$

但：

$$
F_A\ll1.
$$

這就是 false convergence。

所以 stable criteria 必須同時看兩者。

---

# 21. 三軸穩定性

本文提出：

$$
\boxed{
\mathbf S_O
=
(
S_T,
S_A,
S_G
).
}
$$

其中：

- $S_T$：temporal stability；
- $S_A$：cross-agent stability；
- $S_G$：grounding / anchor stability。

---

# 22. Stability Score

第一版：

$$
\boxed{
S_O(t)
=
w_T(1-D_T)
+
w_A(1-V_A)
+
w_G F_A.
}
$$

但正式 benchmark 應保存向量，不應只看 scalar。

---

# 23. 穩定窗口

令事件 index：

$$
k.
$$

若在窗口：

$$
[k,k+W]
$$

內：

$$
D_T\le\epsilon_T,
$$

$$
V_A\le\epsilon_A,
$$

$$
F_A\ge\tau_A,
$$

$$
F_{exec}\ge\tau_E,
$$

則稱：

$$
\boxed{
\text{operator enters a stability window}.
}
$$

---

# 24. Kstable

因此：

$$
\boxed{
K_{\epsilon}^{stable}
=
\min
\{
k:
Conditions(k:k+W)
\text{ hold}
\}.
}
$$

這就是：

> 一個 operator 至少經過多少有效事件，才首次進入指定穩定窗口。

---

# 25. 「步」到底是什麼？

不能只用：

> 對話輪數。

至少可能有：

- use step；
- transmission step；
- recomposition step；
- version step；
- agent-turnover step；
- tool-environment change。

因此需要事件型 step。

---

# 26. Event Vector

第 $i$ 個事件：

$$
\boxed{
e_i
=
(
u_i,
t_i,
c_i,
v_i,
a_i,
w_i
).
}
$$

其中：

- $u$：use；
- $t$：transmission；
- $c$：composition / expansion；
- $v$：version change；
- $a$：agent turnover；
- $w$：world/tool change。

---

# 27. Effective Stabilization Steps

定義：

$$
\boxed{
K_{eff}
=
\sum_i
(
\alpha_u u_i
+
\alpha_t t_i
+
\alpha_c c_i
+
\alpha_v v_i
+
\alpha_a a_i
+
\alpha_w w_i
).
}
$$

所以 100 次完全相同的 use，

不一定比 10 次跨 Agent / 跨 composition 的事件更有 stabilization information。

---

# 28. Stability Exposure Diversity

類似上一篇 effective exposure，

本篇可以定義：

$$
\boxed{
X_{stable}
=
f(
UseDiversity,
AgentDiversity,
CompositionDiversity,
VersionDiversity,
BoundaryCoverage
).
}
$$

---

# 29. Stability 需要被「壓測」

如果 operator 只在：

- 同一 Agent；
- 同一 task；
- 同一 wording；

下穩定，

不能說是通用穩定。

需要：

$$
\boxed{
\text{Perturbation-Stable Semantics}.
}
$$

---

# 30. Stability Perturbations

至少測：

### P1 — Surface Rephrasing

改 wording。

### P2 — Agent Swap

換模型／Agent。

### P3 — Composition Swap

換搭配 operator。

### P4 — Domain Shift

換情境。

### P5 — Version Migration

升 runtime / tool version。

### P6 — Transmission

讓 Agent 教 Agent。

---

# 31. False Stability

如果：

$$
D_T\approx0
$$

只是因為：

> 從來沒有真正改變環境，

則可能是：

$$
\boxed{
\text{Unchallenged Stability}.
}
$$

不是 robust stability。

---

# 32. Stress-Tested Stability

因此應要求：

$$
\boxed{
S_{robust}
=
S
\mid
\mathcal P_{stress}.
}
$$

穩定必須在指定擾動集下成立。

---

# 33. Stability Window 也有尺度

可以：

### Short Window

$$
W_s.
$$

### Medium Window

$$
W_m.
$$

### Long Window

$$
W_l.
$$

一個 operator 可能短期穩定，

長期仍慢慢漂。

---

# 34. Multi-Scale Stability

定義：

$$
\boxed{
\mathbf W
=
(
W_s,W_m,W_l
).
}
$$

並報不同尺度的 drift rate。

---

# 35. Drift Velocity

$$
\boxed{
v_D
=
\frac{dD_{sem}}{dk}.
}
$$

若：

$$
v_D\approx0,
$$

表示 drift 暫時停止或極慢。

---

# 36. Drift Acceleration

$$
\boxed{
a_D
=
\frac{d^2D_{sem}}{dk^2}.
}
$$

若：

$$
a_D>0,
$$

語義漂移正在加速。

可能需提前 reground。

---

# 37. Drift Budget

對每個 operator：

$$
\boxed{
B_D(O)
}
$$

表示允許的累積 drift。

高耦合 operator：

$$
B_D\downarrow.
$$

低風險 stylistic operator：

$$
B_D\uparrow.
$$

---

# 38. Drift Budget 與 LRC

若：

$$
\kappa_{LR}(O)\uparrow,
$$

則 semantic drift 的 world cost 上升。

所以候選：

$$
\boxed{
B_D(O)
\propto
\frac1{\kappa_{LR}(O)\cdot Risk(O)}.
}
$$

只是方向性模型。

---

# 39. Drift Alarm

如果：

$$
D_{sem}>B_D,
$$

觸發：

$$
\boxed{
\operatorname{Reground}.
}
$$

不是立即 retire。

---

# 40. Reground

Reground 可以：

1. 重新展示 canonical definition；
2. 重跑 probe suite；
3. 重對 formal expansion；
4. 重對 world-grounded examples；
5. 修正 Agent-specific interpretation。

---

# 41. Regrounding Gain

定義：

$$
\boxed{
G_R
=
D_{before}-D_{after}.
}
$$

可以量 reground 是否有效。

---

# 42. Reground Too Often

若每 3 次 use 就要 reground，

說明：

- operator 太模糊；
- notation 不好；
- Agent 不適配；
- family collision 太高。

所以：

$$
\boxed{
R_{reground}
}
$$

也是 operator quality 指標。

---

# 43. Semantic Half-Life

若 drift 隨事件累積，

可以定義：

$$
\boxed{
K_{1/2}^{sem}
}
$$

為 anchor fidelity 從：

$$
1
$$

降到某個 halfway threshold 所需步數。

不是所有 operator 都適合這個模型，但可作比較。

---

# 44. Stable Meanings 可能仍有自然變異

同一 operator：

> `summarize`

在不同 domain：

- research；
- legal；
- chat；

細節可以不同。

所以：

$$
\boxed{
\text{Semantic Variation}
\neq
\text{Semantic Drift}.
}
$$

---

# 45. Context-Conditioned Semantics

更合理：

$$
\boxed{
S_O(t,c).
}
$$

只要不同 context 的 variation：

$$
V_c
$$

符合預先定義的 conditional semantics，

不算 drift。

---

# 46. Illegal Drift vs Legal Adaptation

### Legal Adaptation

在 contract envelope 內。

### Illegal Drift

破壞 core invariant / type / boundary。

因此：

$$
\boxed{
D_{sem}
}
$$

要對 invariant-aware representation 計算。

---

# 47. Semantic Checksum

不能只用 cryptographic hash。

Hash 只能證明：

> 文件 bytes 沒變。

不能證明：

> Agent 理解沒變。

所以本文提出：

$$
\boxed{
\text{Semantic Checksum}
}
$$

由一組 invariant probes 形成。

---

# 48. Semantic Checksum Vector

例如：

$$
\boxed{
C_S(O)
=
(
TypePass,
BoundaryPass,
PositivePass,
NegativePass,
ExpansionPass,
WorldPass
).
}
$$

只要 Agent interpretation 改變，

checksum 行為可能變。

---

# 49. Cryptographic Hash vs Semantic Checksum

$$
\boxed{
Hash_{bytes}
\neq
Checksum_{semantic}.
}
$$

兩者互補。

---

# 50. Version-Specific Checksum

每個版本：

$$
O@v
$$

應有：

$$
C_S(O@v).
$$

這讓 migration 可以測：

> 是 intentional semantic change 還是 accidental drift？

---

# 51. False Convergence 的正式判準

若：

$$
V_A(O,t)\le\epsilon_A
$$

但：

$$
F_A(O,t)<\tau_A,
$$

則：

$$
\boxed{
\text{False Convergence}.
}
$$

---

# 52. Frozen Error

另一種情況：

$$
V_A\approx0,
$$

$$
D_T\approx0,
$$

$$
F_A\ll1.
$$

且長期不變。

這是：

$$
\boxed{
\text{Frozen Error}.
}
$$

非常穩，

但穩定地錯。

---

# 53. 為什麼 Frozen Error 特別危險？

因為所有普通 stability metric 都可能給高分：

- low variance；
- low drift；
- high agreement。

如果沒有 grounding anchor，

就看不出來。

---

# 54. 2025 Iterated Transmission 的警告

LLM artificial-language iterated transmission 研究顯示：

- learnability 可提升；
- structure 可增加；
- 但 vocabulary 也可能退化；
- distinct signals 減少；
- communicative expressiveness 受損。

這正是一個：

$$
\boxed{
\text{more stable / learnable}
\not\Rightarrow
\text{more expressive / grounded}.
}
$$

的外部錨點。

---

# 55. Compression-Induced Drift

如果每一代都追求：

- 短；
- 好學；
- 高頻；

rare distinctions 可能消失。

本文稱：

$$
\boxed{
\text{Compression-Induced Drift}.
}
$$

---

# 56. Underspecification

如果多個 meaning：

$$
m_1,m_2,m_3
$$

最後都映射同一 signal：

$$
s,
$$

語言可能更簡單，

但：

$$
\boxed{
\text{semantic resolution}
\downarrow.
}
$$

---

# 57. Stability 必須包含 Distinction Retention

因此：

$$
\boxed{
R_{dist}
}
$$

表示 critical semantic distinctions 的保留率。

stable criteria 應加入：

$$
R_{dist}\ge\tau_D.
$$

---

# 58. Form–Meaning Mapping

2026 年 emergent-language phrasebook 研究顯示，從 emergent language 中誘導出的 morpheme form–meaning mappings 可以讓 rule-based agents 實際與 neural agents 溝通；而 repetition 與 morpheme ordering 都具有功能。

這提醒：

$$
\boxed{
\text{surface structure}
}
$$

可能本身就是 operational semantics 的一部分。

不能任意 normalize / compress。

---

# 59. Semantic Invariant 可能包含 Order

對某些 operator language：

$$
O_aO_b
\neq
O_bO_a.
$$

所以 checksum 需要測：

- order；
- repetition；
- scope；
- binding。

---

# 60. Systematicity 與 Learnability

2026 年 ACL 對自然語言 form–meaning mappings 的研究指出，語言形式受到 simplicity 與 accuracy 的競合壓力，並以 learnability-based complexity 描述 systematic mappings。

這與 COL 的核心非常一致：

$$
\boxed{
\text{stable language}
}
$$

不是只有「固定」，

也需要在：

- simplicity；
- recoverability；
- learnability；

之間取得平衡。

---

# 61. Population Stability

2026 年 CoNLL dynamic-population 研究顯示：

- static population 可形成共享語言；
- turnover 後 language drift 會成為問題；
- age-based plasticity 可以降低 drift；
- uniform low plasticity 適應 newcomer 太慢；
- uniform high plasticity 又變得太快。

因此：

$$
\boxed{
\text{Population Stability}
=
\text{Continuity}
+
\text{Selective Plasticity}.
}
$$

---

# 62. Agent-Weighted Stability

新 Agent：

$$
A_{new}
$$

可塑性高。

老 Agent：

$$
A_{old}
$$

提供 anchor。

可形式化成：

$$
\boxed{
\pi_i
=
\pi(age_i).
}
$$

並讓：

$$
\frac{d\pi}{d age}<0
$$

作為候選 schedule。

---

# 63. Operator-Weighted Stability

同樣也可對 operator：

### New / Experimental
高 plasticity。

### Mature / Stable
低 plasticity。

因此：

$$
\boxed{
\pi(O)
=
f(
Age,
Risk,
Usage,
Evidence
).
}
$$

---

# 64. 雙重 Plasticity

動態語言中同時有：

- Agent plasticity；
- Operator plasticity。

所以 drift：

$$
\boxed{
D_{drift}
=
f(
\pi_A,
\pi_O,
Turnover,
Transmission
).
}
$$

---

# 65. Stability–Plasticity Surface

真正不是單一最佳：

$$
\pi^*.
$$

而可能：

$$
\boxed{
(\pi_A^*,\pi_O^*).
}
$$

---

# 66. Language Stabilization 不一定收斂到固定點

可能：

$$
S_O(t)
\rightarrow S^*
$$

固定。

也可能：

$$
S_O(t)
$$

在小區域內震盪。

只要：

$$
S_O(t)\in\mathcal E_{\epsilon},
$$

仍可稱 metastable。

---

# 67. Limit Cycle

某些 operator semantics 可能：

$$
S_1\rightarrow S_2\rightarrow S_1\rightarrow\cdots
$$

週期震盪。

這不一定是 failure，

如果版本／context 有明確條件。

---

# 68. Chaotic Drift

如果小 perturbation：

$$
\delta
$$

造成很大 semantic divergence，

則 language 對 perturbation 敏感。

可定義類似：

$$
\boxed{
\lambda_D
=
\lim_{k\to\infty}
\frac1k
\ln
\frac{
D_k
}{
D_0
}.
}
$$

作為 drift sensitivity 的候選量。

不是宣稱真正 chaos theory 已適用。

---

# 69. Stability Basin

對 operator anchor：

$$
A_O,
$$

可以想像：

$$
\boxed{
\mathcal B_O
}
$$

一個 semantic basin。

小 perturbation 後仍會被：

- examples；
- compiler；
- usage；
- agents；

拉回 anchor。

---

# 70. Attractor Language

文化演化研究中有 cultural attractor 概念：

群體反覆學習與傳播後，某些形式可能成為穩定吸引區。

COL 也可以研究：

$$
\boxed{
\text{Operator Attractors}.
}
$$

---

# 71. 但 attractor 仍可能是錯的

又回到：

$$
\boxed{
\text{Attractor}
\neq
\text{Ground Truth}.
}
$$

所以必須 anchor。

---

# 72. Stabilization Rate

定義：

$$
\boxed{
r_S
=
-\frac{dD_{anchor}}{dk}.
}
$$

若：

$$
r_S>0,
$$

表示逐步靠近 anchor。

---

# 73. Time-to-Stability / Steps-to-Stability

可同時報：

$$
T_{\epsilon}^{stable}
$$

與：

$$
K_{\epsilon}^{stable}.
$$

前者 wall-clock。

後者事件步數。

---

# 74. Stabilization Efficiency

$$
\boxed{
\eta_S
=
\frac{
D_0-D_W
}{
K_{eff}+C_{govern}
}.
}
$$

表示單位 stabilization cost 降了多少 drift。

---

# 75. Stable Window vs Permanent Stability

一個 operator 進入：

$$
W
$$

窗口，

只表示：

> 暫時穩定。

不表示：

$$
\boxed{
\text{stable forever}.
}
$$

新 domain / model / tool 可能讓它重新離開窗口。

---

# 76. Stability Exit

若：

$$
D_T>\epsilon_T
$$

或：

$$
F_A<\tau_A,
$$

則：

$$
\boxed{
\text{Exit Stability Window}.
}
$$

開始：

- review；
- reground；
- branch；
- revise。

---

# 77. Stability Re-entry

修正後再次達標：

$$
\boxed{
K_{\epsilon}^{restable}.
}
$$

這是語言被擾動後重新穩定需要多少步。

---

# 78. Restabilization Savings

若：

$$
K_{restable}
<
K_{initial-stable},
$$

表示系統有：

$$
\boxed{
\text{Stabilization Memory}.
}
$$

與上一篇 relearning savings 同構。

---

# 79. Operator Stability Profile

每個 operator 應保存：

```text
Operator:
Version:
Semantic Anchor:
Invariant Set:
Behavior Signature:
Drift Budget:
Current Drift:
Cross-Agent Variance:
Anchor Fidelity:
Kstable:
Stability Window:
Last Reground:
Restabilization Cost:
Status:
```

---

# 80. Status 可以分

### Experimental
尚未達 stability window。

### Candidate
短期達標。

### Stable
中期、多 Agent、novel probes 達標。

### Drifting
超出 drift budget。

### Regrounding
正在重新錨定。

### Deprecated
不再推薦。

---

# 81. Whole-Language Stability

整套語言：

$$
\mathcal O
$$

不能只平均所有 operators。

因為 critical operator 的 drift 更重要。

定義 risk-weighted：

$$
\boxed{
D_{\mathcal L}
=
\frac{
\sum_i
w_i^{risk}
D_i
}{
\sum_i w_i^{risk}
}.
}
$$

---

# 82. Critical Core Stability

另追：

$$
\boxed{
D_{core}
}
$$

只看：

- control；
- authorization；
- rollback；
- type；
- branch；
- commit；

等核心 operators。

---

# 83. Stable Core / Plastic Periphery

最合理的整體可能是：

$$
\boxed{
\text{Stable Core}
+
\text{Plastic Periphery}.
}
$$

Core drift budget 小。

Periphery 可較快演化。

---

# 84. 這與 LRC–COL-06 完整接合

上一章提出 dynamic interval。

本章補上：

> 就算 $N(t)$ 留在 viability band，operator semantics 也可能漂。

因此 dynamic governance 至少要同時維持：

$$
\boxed{
N(t)\in V_{\tau}(t)
}
$$

與：

$$
\boxed{
D_{\mathcal L}(t)\le B_D.
}
$$

---

# 85. Language Size Stability ≠ Semantic Stability

可能：

$$
N_G(t)=100
$$

十年不變，

但 100 個 operator 的意思全變了。

所以：

$$
\boxed{
\text{Cardinality Stability}
\neq
\text{Semantic Stability}.
}
$$

---

# 86. Semantic Stability ≠ Functional Stability

definition 不變，

但 underlying tools / APIs 改版，

execution behavior 變了。

因此還要：

$$
\boxed{
\text{Functional Stability}.
}
$$

---

# 87. Tool-Dependent Drift

如果：

$$
O
\rightarrow
Tool@v1
$$

變成：

$$
O
\rightarrow
Tool@v2,
$$

operator semantic contract 可能需要重新驗證。

這是：

$$
\boxed{
\text{Environment-Induced Drift}.
}
$$

---

# 88. Model-Induced Drift

同一 operator definition，

模型：

$$
A@v1
\rightarrow
A@v2
$$

也可能行為不同。

所以 operator stability 必須條件化：

$$
\boxed{
S_O(A,V,E).
}
$$

---

# 89. Model Upgrade Gate

每次 major Agent upgrade：

$$
A_t\rightarrow A_{t+1}
$$

都應重新跑：

- semantic checksum；
- boundary probes；
- high-risk operators。

不能假設新模型只會更好。

---

# 90. Cross-Model Stability

如果 operator 在：

$$
A_1,A_2,\ldots,A_n
$$

都保持 invariant，

則：

$$
\boxed{
\text{Cross-Model Stability}.
}
$$

這對通用傳播非常重要。

---

# 91. Cross-Model Stability 不要求完全同 trace

不同 Agent 可以：

- 不同 reasoning；
- 不同 plan；

只要：

- invariants；
- output contract；
- safety boundary；

一致即可。

---

# 92. Semantic Equivalence Class

因此定義：

$$
\boxed{
[O]_{\epsilon}
=
\{
S:
D_{inv}(S,A_O)\le\epsilon
\}.
}
$$

多個 implementation 可以屬於同一 semantic equivalence class。

---

# 93. 這使語言可以演化而不失去身份

即：

$$
\boxed{
\text{implementation change}
\not\Rightarrow
\text{operator identity change}.
}
$$

只要仍在 invariant class 內。

---

# 94. 何時應升 major version？

若：

- type 變；
- core invariant 變；
- failure boundary 變；
- world effect 變；

則：

$$
\boxed{
O@v
\rightarrow
O@(v+1)_{\text{major}}.
}
$$

而不是假裝沒有 semantic change。

---

# 95. Minor Version

若只是：

- example 增加；
- wording 改善；
- implementation optimization；

且 semantic checksum 兼容，

可 minor version。

---

# 96. Drift vs Intentional Revision

因此要區分：

$$
\boxed{
\text{Uncontrolled Drift}
}
$$

與：

$$
\boxed{
\text{Controlled Semantic Revision}.
}
$$

後者有：

- version；
- rationale；
- migration；
- tests。

---

# 97. 這就是「語言穩定」的真正含義

不是：

> 大家永遠不要改。

而是：

> **不受控的語義變化足夠低；必要的變化則通過顯式版本與遷移發生。**

---

# 98. 十二個正式命題

## ST-P1 — Learning–Stability Separation

Agent 學會 operator 不代表 operator language 已穩定。

## ST-P2 — Convergence–Correctness Separation

跨 Agent agreement 高不代表 anchor fidelity 高。

## ST-P3 — Invariant-Envelope Stability

穩定應定義為 semantic state 留在 invariant envelope，而不是完全不變。

## ST-P4 — Perturbation Requirement

沒有經過跨 context / Agent / composition perturbation 的穩定只是 weak stability。

## ST-P5 — False-Convergence Risk

iterated transmission 可產生高度 learnable 但 degraded / underspecified convention。

## ST-P6 — Drift-Budget Coupling

reality-coupling / risk 越高的 operator，允許 drift budget 應越低。

## ST-P7 — Semantic Checksum Necessity

byte-level version identity 不足以保證 semantic stability，需要 behavioral / invariant checksum。

## ST-P8 — Selective Plasticity

Agent 與 operator 的 plasticity 都應隨 age / maturity / risk 調節，而非全域固定。

## ST-P9 — Stable-Core / Plastic-Periphery

大型動態 language 可能需要低漂移 core 與高適應 periphery。

## ST-P10 — Restabilization Memory

語言被擾動後重新穩定所需步數可能小於首次穩定步數。

## ST-P11 — Environment-Conditioned Stability

tool / model / world version 改變會使 operator stability 失效，即使文字定義沒變。

## ST-P12 — Metastability over Freezing

實用 operator language 的目標應是可版本化 metastability，而不是永久 frozen semantics。

---

# 99. 第一版實驗：Single-Operator Drift

建立 operator：

$$
O_X.
$$

給：

$$
A_1
$$

使用 $k$ 次。

每隔：

$$
r
$$

步重測：

- definition；
- novel behavior；
- boundary；
- expansion。

得到：

$$
D_{sem}(k).
$$

---

# 100. Cross-Agent Transmission Chain

$$
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow
\cdots
\rightarrow
A_n.
$$

每個 Agent 只從上一個 Agent 學。

量：

$$
D_{anchor}(n),
$$

$$
V_A(n),
$$

$$
R_{dist}(n).
$$

---

# 101. False-Convergence Test

設計 transmission pressure 讓：

- vocabulary 變短；
- Agent agreement 變高。

但檢查：

$$
AnchorFidelity.
$$

看是否出現：

$$
V_A\downarrow
$$

同時：

$$
F_A\downarrow.
$$

---

# 102. Compression Drift Test

比較：

### Full Definition Transmission

### Summary Transmission

### Symbol-Only + Examples

### Macro Expansion Contract

測哪種傳播最容易：

- 保留 distinctions；
- 控制 drift；
- 維持 learnability。

---

# 103. Plasticity Sweep

Agent：

$$
\pi_A
=
low,medium,high.
$$

Operator：

$$
\pi_O
=
low,medium,high.
$$

得到：

$$
9
$$

個 condition。

測：

- adaptation；
- drift；
- convergence；
- anchor fidelity。

---

# 104. Stability Window Sweep

比較：

$$
W=10,50,100,500.
$$

看短窗口判定的 stable operator 是否在長窗口中再次 drift。

---

# 105. Semantic Checksum Test

建立固定 regression + rotating novel probes。

比較：

### Text Similarity Only

### Definition + Embedding

### Behavioral Checksum

### Invariant + Behavioral + Grounded

看哪個最能提前發現 harmful drift。

---

# 106. Tool-Version Drift Test

同 operator：

$$
O_X.
$$

底層 tool：

$$
T@v1
\rightarrow
T@v2.
$$

測：

> 文字未變時，functional semantics 是否已改。

---

# 107. Model-Version Drift Test

同：

$$
O_X,
$$

不同 Agent versions：

$$
A@v1,A@v2,A@v3.
$$

測：

$$
CrossModelStability.
$$

---

# 108. Restabilization Test

先讓 operator 穩定。

再：

- 換 Agent；
- 加新 domain；
- 改 tool；
- 做 compression。

讓它離開 stability window。

量：

$$
K_{\epsilon}^{restable}.
$$

---

# 109. Kstable 的第一版回答

現在可以正式回答最初問題：

> 「到底要多少步後才開始可能穩定？」

答案不是固定：

> 7 步、20 步或 100 步。

而應寫：

$$
\boxed{
K_{\epsilon}^{stable}
=
f(
Operator,
AgentPopulation,
Transmission,
Composition,
Plasticity,
Anchor,
Risk,
Environment
).
}
$$

真正數值需要 domain-specific experiment。

---

# 110. 但我們現在知道如何量它

要報：

```text
Kstable
Stability Window W
Temporal Drift
Cross-Agent Variance
Anchor Fidelity
Distinction Retention
Execution Fidelity
Drift Budget
Perturbation Set
Restabilization Steps
```

---

# 111. Whole-Language Kstable

整套 language：

$$
\mathcal L.
$$

可以定義：

$$
\boxed{
K_{\epsilon}^{stable}(\mathcal L)
}
$$

但不能只取所有 operators 平均。

可要求：

### Core
全部達標。

### Noncritical
例如 95% 達標。

### Experimental
可未達標。

---

# 112. Language Release Gate

一套 COL 只有當：

- core semantic checksum pass；
- cross-Agent variance pass；
- novel composition pass；
- world-grounding pass；
- stability window pass；

才標：

$$
\boxed{
\text{Stable Release}.
}
$$

---

# 113. Stable Release 仍不是最終版本

因為：

$$
\boxed{
\text{Stable}
=
\text{bounded drift for current environment}.
}
$$

不是：

$$
\text{immutable forever}.
$$

---

# 114. 與下一篇的接口

本篇已研究：

$$
K_{\epsilon}^{stable}.
$$

但還沒有完整研究：

> 一套語言是怎麼跨世代傳播、哪些結構容易活下來、哪些 distinction 會消失、哪些 convention 會被壓縮成 degenerate form？

這正是下一篇：

$$
\boxed{
\text{Transmission Dynamics}.
}
$$

---

# 115. 本篇核心公式組

semantic drift：

$$
\boxed{
D_{sem}(O;t_1,t_2)
=
D_S(
S_O(t_1),
S_O(t_2)
).
}
$$

cross-Agent variance：

$$
\boxed{
V_A(O,t)
=
\mathbb E_i[
D_S(S_O^{A_i},\bar S_O)
].
}
$$

stability steps：

$$
\boxed{
K_{\epsilon}^{stable}
=
\min
\{
k:
D_T\le\epsilon_T,
V_A\le\epsilon_A,
F_A\ge\tau_A,
F_{exec}\ge\tau_E
\text{ over }W
\}.
}
$$

drift budget：

$$
\boxed{
D_{sem}\le B_D(O).
}
$$

false convergence：

$$
\boxed{
V_A\le\epsilon_A
\quad\land\quad
F_A<\tau_A.
}
$$

---

# 116. 非主張

本文不主張：

1. language stability 有 universal 固定步數；
2. embedding similarity 足以測 semantic drift；
3. Agent agreement 等於 language correctness；
4. stable language 應永遠不改；
5. iterated transmission 一定造成 degeneration；
6. high plasticity 一定壞；
7. cultural-attractor model 可直接等同 AI operator language；
8. semantic drift 一定可被單一 scalar 完整表示；
9. behavioral checksum 能保證所有 hidden semantics；
10. metastability 是唯一合理語言治理方式。

本文只提出：

$$
\boxed{
\text{Language stabilization should be measured as sustained low drift, bounded cross-agent variance, preserved semantic distinctions, and high anchor / execution fidelity under explicit perturbations.}
}
$$

---

# 117. 文獻錨點

1. **Cognitively Inspired Developmental Trajectories Improve Explore-Exploit Dynamics in Neural Agent Emergent Communication（CoNLL 2026）**  
   在 dynamic population turnover 中，age-based plasticity 顯著降低 language drift；uniform low plasticity 難快速吸收 newcomers，而 uniform high plasticity 使語言變化過快、stable conventions 難形成。這直接支援本文的 selective-plasticity / stability–plasticity framing。

2. **Searching for Structure: Investigating Emergent Communication with Large Language Models（COLING 2025）**  
   LLM 代際 artificial-language 傳播可提高 learnability，但同時可能形成 non-humanlike degenerate vocabularies，且部分信號區分度下降。這支援本文「learnability / convergence 不等於 expressive anchored stability」。

3. **Communicating in Emergent Language with an Induced Morphological Phrasebook（ACL 2026）**  
   誘導出的 form–meaning mappings 可被 rule-based agents 實際用來與 neural agents 溝通；repetition 與 morpheme ordering 皆對 meaning 有作用。這支援以 operational behavior 而非單純 surface similarity 衡量 semantic stability。

4. **Systematicity between Forms and Meanings across Languages Supports Efficient Communication（ACL 2026）**  
   對自然語言 grammatical meaning–form mappings 的跨語言研究顯示 simplicity 與 accuracy 間存在競合，並以 learnability-based complexity 描述 systematicity，支持本系列將 learnability、distinction retention 與 form–meaning recoverability共同納入語言穩定性。

5. **The Emergence of Cultural Attractors: How Dynamic Populations of Learners Achieve Collective Cognitive Alignment（Cognitive Science, 2022）**  
   提出 dynamic learners 可經互相提供訓練輸入形成 collective alignment 與 cultural attractors。本文只把它作為「群體語言可能形成吸引區」的理論類比，不把 attractor 等同 correctness。

6. **Emergent language: a survey and taxonomy（Autonomous Agents and Multi-Agent Systems, 2025）**  
   綜整 emergent-language / multi-agent communication 研究，提供語言形成、同步與演化的廣泛背景。

---

# 118. 下一篇

## LRC–COL-09：代際傳播、可學習性與語言退化
### Intergenerational Transmission, Learnability, and Language Degeneration

下一篇將正式研究：

$$
\boxed{
Language_g
\rightarrow
Agent_{g+1}
\rightarrow
Language_{g+1}.
}
$$

核心問題包括：

- 為什麼更好學的語言未必保留更多資訊；
- transmission bottleneck 如何影響 compositionality；
- rare distinctions 為何容易消失；
- vocabulary degeneration 與 semantic compression 如何區分；
- teacher compression 與 learner reconstruction 的交換；
- fidelity、learnability、innovation 三者如何形成 Pareto frontier；
- 是否存在 optimal transmission bottleneck；
- 如何讓未來 AI 複合語言「傳得下去」又不在代際中逐步變成只剩下彼此懂、但已經失去世界細節的 shorthand。

**END — LRC–COL-08 v0.1**
