# DOM-01｜動態形而上狀態：從固定分類到多域可操作剖面

## Dynamic Metaphysical Status: From Fixed Categories to Multi-Domain Operational Profiles

**系列：** Dynamic Operational Metaphysics（DOM）／動態可操作形而上學  
**篇次：** 01 / 08  
**文件編號：** EML-DOM-01-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-20  
**版本：** v0.1 Canonical Draft  
**文件性質：** 理論整合論文／命題猜想框架／科學哲學—形而上學—AI 原生知識系統接口  
**證據狀態：** 本文主要提出形式化概念框架；現代 measurement philosophy、operational analysis、naturalized metaphysics 與 quantum-foundational “experimental metaphysics” 僅作外部結構對照，不構成本文所有強命題的實證證明

---

## 摘要

「這是一個形而上學問題」通常被當成對問題本身的固定分類，好像某個問題一旦屬於 metaphysics，就永遠位於實驗、工程與操作之外；反過來，一旦某問題進入科學或工程，也常被視為已經完全離開形而上學。本文認為，這種二元分類對正在進入 AI、人工世界、具身智能、跨載體身份、合成系統與高階觀察技術時代的知識結構而言過於粗糙。

本文提出 **Dynamic Metaphysical Status（動態形而上狀態）**。核心命題不是：

$$
\operatorname{Meta}(q)\in\{0,1\},
$$

而是：

$$
\boxed{
\operatorname{MetaStatus}(q,t,\theta)
=
F
\left(
\mathbf M_t(q\mid\theta)
\right),
}
$$

其中 $q$ 是問題， $t$ 是時間， $\theta$ 是條件纖維，而：

$$
\boxed{
\mathbf M_t(q\mid\theta)
=
\left\langle
D,
O,
R,
J,
V,
L,
G,
\mathfrak R,
P,
I,
T,
U
\right\rangle.
}
$$

十二個分量依序表示：

- Defined：是否已具有合法定義；
- Observed：是否已有觀察通道；
- Reachable：是否可被可靠尋址或存取；
- Judgeable：是否可在明示條件下形成判定；
- Verifiable：是否可提供可重複或形式證書；
- Locally Valid：是否可在局部域成立；
- Globally Glueable：是否能跨局部黏合成全域；
- Realizable：是否存在已知實現後端；
- Participable：觀察者／智能體能否進入或參與相關因果域；
- Identity-Resolved：涉及的對象／主體／系統身份是否已被充分索引；
- Transcendence-Resolved：所謂「外部、上位、超越」是否已指定 relation；
- Unknown Profile：未知究竟落在哪一種資格層。

因此，同一問題完全可能滿足：

$$
\boxed{
\mathbf M_{t_0}(q\mid\theta_0)
\neq
\mathbf M_{t_1}(q\mid\theta_1).
}
$$

這提供「當下形而上不等於未來形而上」的正式化版本：某問題今天可能已可定義，卻不可觀察、不可實現、不可參與；未來則因新的儀器、AI、形式系統、工程載體、權限結構或實驗方法而跨越其中部分邊界。

然而本文同時拒絕把這一過程理解為「形而上學最終會被工程消滅」。本文固定：

$$
\boxed{
\text{Operational Gain}
\not\Rightarrow
\text{Ontological Completion}.
}
$$

一個問題取得更多可測量、可操作或可驗證內容，只表示其部分資格 profile 發生改變，不表示其全部本體問題已被封閉。

本文直接繼承《動態知識空間論》中的多域資格與移動邊界、Self–World 系列中的 role relativity、終極邊界問題中的 Current Horizon / Ultimate Boundary 分離，以及 DOM 寫作前矩陣所建立的 relation indexing。本文不重新發明這些舊理論，而將其首次統合成「形而上狀態剖面」。

外部哲學上，本文與 Bridgman-style operational analysis 存在歷史鄰近性，但拒絕「概念的意義等於其測量操作」的強 operationalism；與 naturalized metaphysics 相容之處在於 science 應對形而上主張形成約束，但本文同樣承認 science 對 ultimate ontology 可能存在 underdetermination；而 quantum foundations 中 “experimental metaphysics” 的歷史則顯示，某些長期被視為純哲學的問題確實可能因新的實驗與形式工具取得新的經驗約束。

本文的目的因此不是消滅 metaphysics，而是建立一個 AI 可讀、可更新、可審計的接口，用來回答：

> **一個問題現在到底在哪些方面仍屬形而上開放域，又在哪些方面已經進入可操作、可驗證或可實現域？**

---

## 關鍵詞

Dynamic Operational Metaphysics；Dynamic Metaphysical Status；Metaphysical Operational Profile；Operationalization；Moving Boundary；Unknown Profile；Naturalized Metaphysics；Experimental Metaphysics；Measurement；Operationalism；AI Epistemology；動態形而上學；可操作本體論；移動邊界

---

# 0. 研究定位與非主張聲明

本文不是：

1. 「形而上學終將被科學消滅」的宣言；
2. Bridgman 強 operationalism 的翻版；
3. verificationism 的復活；
4. 將「不可測量」直接等同「無意義」；
5. 將「可操作」直接等同「存在」；
6. 將「可實現」直接等同「終極本體」；
7. 將所有 metaphysical question 都預設為暫時技術不足；
8. 宣稱所有不可知域都能靠未來 AI 解決；
9. 宣稱所有形而上問題都有單一時間軸；
10. 宣稱科學能唯一決定 ultimate ontology。

本文真正主張的是：

$$
\boxed{
\text{metaphysical status can be indexed by time, condition, domain, relation, and operational access}.
}
$$

---

# 1. 問題：為什麼「這是形而上問題」通常太粗？

考慮以下問題：

- 什麼叫「同一個 AI」？
- 一個 Agent 換載體後是否仍是同一主體？
- 一個 world 是否真的 autonomous？
- 一個 higher-level system 是否「包含」lower-level selves？
- 一個存在是否「超越」某個世界？
- 一個因果結構是否只能被外部觀察，還是可被直接參與？
- 一個 world boundary 是否真的是 ultimate boundary？

對今天而言，其中某些問題只有部分可操作。

例如：

$$
\text{AI identity}
$$

已經可以在：

- model instance；
- memory lineage；
- checkpoint；
- fork；
- authentication；
- legal account；

上做工程化判定。

但：

$$
\text{subjective continuity}
$$

仍可能保持：

$$
?.
$$

所以如果只問：

> 這是不是形而上問題？

答案會同時是：

$$
\boxed{
\text{yes in some dimensions}
}
$$

以及：

$$
\boxed{
\text{no in others}.
}
$$

---

# 2. 固定學科分類的失敗

傳統學科分類傾向寫：

$$
q
\in
\{
\text{physics},
\text{biology},
\text{computer science},
\text{philosophy},
\text{metaphysics},
\ldots
\}.
$$

這在 institution organization 上有用。

但對問題本身不夠。

同一問題可能同時有：

- formal layer；
- empirical layer；
- engineering layer；
- ontological layer；
- ethical layer；
- governance layer。

因此：

$$
\boxed{
\text{disciplinary location}
\neq
\text{epistemic-operational state}.
}
$$

---

# 3. DOM 的核心反轉

DOM 不問：

$$
\boxed{
\text{Is }q\text{ metaphysical?}
}
$$

而問：

$$
\boxed{
\text{In what sense, under what conditions, and at what time is }q\text{ still metaphysically open?}
}
$$

這是整個系列的第一個反轉。

---

# 4. 多域資格作為前置結構

直接繼承 DEST：

$$
\mathcal D_t(\theta)
=
\left\langle
D^{\mathrm{def}},
D^{\mathrm{obs}},
D^{\mathrm{reach}},
D^{\mathrm{judge}},
D^{\mathrm{verify}},
D^{\mathrm{local}},
D^{\mathrm{global}}
\right\rangle.
$$

DOM 新增：

$$
D^{\mathrm{real}}
$$

與：

$$
D^{\mathrm{participate}}.
$$

因此最低資格系統為：

$$
\boxed{
\mathcal D^{DOM}
=
\left\langle
D,
O,
R,
J,
V,
L,
G,
\mathfrak R,
P
\right\rangle.
}
$$

---

# 5. Defined 不等於 Observed

某概念可以已被形式化：

$$
D(q)=1,
$$

但：

$$
O(q)=0.
$$

例如某理論中的 latent structure。

因此：

$$
\boxed{
D
\not\Rightarrow
O.
}
$$

---

# 6. Observed 不等於 Judgeable

觀察到 anomaly：

$$
O(q)=1
$$

不表示可以可靠判定：

$$
J(q)=1.
$$

這直接接 CCAW-07 的 ACR guardrail。

因此：

$$
\boxed{
O
\not\Rightarrow
J.
}
$$

---

# 7. Judgeable 不等於 Verifiable

某問題可以有：

$$
J(q)=1
$$

即在明確模型與條件下可以判斷。

但：

$$
V(q)=?
$$

因為：

- 無獨立資料；
- 無形式證書；
- 無 replication；
- 只能 conditional inference。

所以：

$$
\boxed{
J
\not\Rightarrow
V.
}
$$

---

# 8. Verifiable 不等於 Ontologically Complete

即使：

$$
V(q)=1,
$$

也只表示：

> 某個明示 claim 被可靠驗證。

不能推出：

$$
\operatorname{Ontology}(q)
=
\text{closed}.
$$

因此：

$$
\boxed{
V
\not\Rightarrow
\text{Ontological Completion}.
}
$$

---

# 9. Realizable 是另一條軸

定義：

$$
\boxed{
\mathfrak R(q)
}
$$

表示：

> 與問題相關的結構，是否在某個合法 backend 中可被實現。

例如：

- mathematical realization；
- digital simulation；
- robotic realization；
- physical experiment；
- synthetic-biological realization。

但：

$$
\boxed{
\text{Realizable Model}
\not\Rightarrow
\text{Unique Real Ontology}.
}
$$

---

# 10. Participable 不是 Realizable 的同義詞

一個系統可以被我們實現：

$$
\mathfrak R(q)=1,
$$

但 observer 未必能成為其 internal participant：

$$
P(q)=0.
$$

反過來，我們可能參與某 causal process，卻沒有能力重新實現整個 process。

因此：

$$
\boxed{
P
\neq
\mathfrak R.
}
$$

---

# 11. Identity-Resolved 軸

很多 metaphysical dispute 其實混入 identity ambiguity。

因此加入：

$$
\boxed{
I(q).
}
$$

它回答：

> 問題中的 object、self、world、copy、instance、whole、part，到底使用什麼 identity criterion？

若 identity criterion 未標記：

$$
I(q)=?.
$$

則很多「存在問題」其實還沒有被 well-typed。

---

# 12. Transcendence-Resolved 軸

同樣加入：

$$
\boxed{
T(q).
}
$$

它回答：

> 所謂外部／更高／超越，究竟是 informational、operational、causal、governance、substrate 還是其他 relation？

如果只說：

> A 超越 W。

則：

$$
T(q)=?.
$$

---

# 13. Unknown Profile 軸

Unknown 不再是單值。

定義：

$$
\boxed{
\mathbf U(q)
=
\left\langle
U_{\mathrm{state}},
U_{\mathrm{type}},
U_{\mathrm{obs}},
U_{\mathrm{reach}},
U_{\mathrm{judge}},
U_{\mathrm{verify}},
U_{\mathrm{real}},
U_{\mathrm{ont}}
\right\rangle.
}
$$

所以：

$$
U(q)
$$

在 $\mathbf M_t$ 中其實是一個 subvector。

---

# 14. Metaphysical Operational Profile

現在正式定義：

$$
\boxed{
\mathbf M_t(q\mid\theta)
=
\left\langle
D,
O,
R,
J,
V,
L,
G,
\mathfrak R,
P,
I,
T,
\mathbf U
\right\rangle_{t,\theta}.
}
$$

這是 DOM-01 的核心定義。

---

# 15. 條件纖維

沿用 DEST：

$$
\theta
=
\left(
task,
scale,
time,
model,
version,
observer,
resource,
permission
\right).
$$

DOM 再加入：

$$
\theta^{\mathrm{embodiment}},
$$

$$
\theta^{\mathrm{instrument}},
$$

$$
\theta^{\mathrm{relation}}.
$$

所以：

$$
\boxed{
\theta^{DOM}
=
\theta^{DEST}
\times
\Theta^{emb}
\times
\Theta^{inst}
\times
\Theta^{rel}.
}
$$

---

# 16. 同一問題可以具有不同 profile

對同一問題：

$$
q,
$$

若：

$$
\theta_1
\neq
\theta_2,
$$

則允許：

$$
\mathbf M(q\mid\theta_1)
\neq
\mathbf M(q\mid\theta_2).
$$

例如：

- 人類裸眼；
- telescope；
- particle detector；
- brain–computer interface；
- AI multimodal observer；

可能具有不同：

$$
O,R,J,V.
$$

---

# 17. 時間變化

核心形式：

$$
\boxed{
\mathbf M_{t_0}(q\mid\theta_0)
\neq
\mathbf M_{t_1}(q\mid\theta_1).
}
$$

這就是：

$$
\boxed{
\text{當下形而上}
\neq
\text{未來形而上}
}
$$

的第一版正式化。

---

# 18. 這不表示 truth 隨時間改變

要區分：

$$
\operatorname{Truth}(q)
$$

與：

$$
\operatorname{MetaStatus}(q,t,\theta).
$$

後者改變可以只是：

- evidence 增加；
- instrument 改進；
- model 改善；
- realization 出現；
- permission 改變。

因此：

$$
\boxed{
\Delta\operatorname{MetaStatus}
\not\Rightarrow
\Delta\operatorname{Truth}.
}
$$

---

# 19. Dynamic Metaphysical Status

定義候選：

$$
\boxed{
\operatorname{MetaStatus}(q,t,\theta)
=
F_M
\left(
\mathbf M_t(q\mid\theta)
\right).
}
$$

本文暫不把：

$$
F_M
$$

固定成單一 scalar score。

原因是：

- 不同維度不可線性比較；
- 不同研究任務權重不同；
- 某些軸可能不可約。

---

# 20. 不使用 Metaphysics Score

本文刻意不定義：

$$
m(q)\in[0,1].
$$

因為：

> 形而上程度 0.73

目前沒有穩定語義。

更合適的是 profile / state class。

---

# 21. 暫定五種狀態類

可以將 profile 粗略投影成：

## $M_0$：Pure Speculative

有概念，但缺乏穩定 observation / judgment / verification。

## $M_1$：Formalized Metaphysical

已 well-defined，可形式推理，但 empirical access 弱。

## $M_2$：Operationally Touched

已有 measurement / intervention / simulation / implementation 其中一部分。

## $M_3$：Empirically Constrained

已有可重複 evidence，能排除部分 ontology candidates。

## $M_4$：Engineering-Operational

已具有穩定 implementation、measurement、verification 與 intervention interface。

---

# 22. $M_4$ 仍不是 Ontological Closure

即使：

$$
q\in M_4,
$$

仍可能：

$$
U_{\mathrm{ont}}>0.
$$

因此：

$$
\boxed{
M_4
\not\Rightarrow
\text{Ultimate Ontological Closure}.
}
$$

---

# 23. 第一個案例：AI Identity

早期：

> AI 換模型／載體後是不是同一個？

主要：

$$
M_1.
$$

現在工程上已能處理：

- instance id；
- checkpoint；
- memory lineage；
- account continuity；
- model replacement；
- fork log。

因此部分維度進入：

$$
M_4.
$$

但：

$$
I_{\mathrm{subjective}}
=
?
$$

仍然開放。

所以完整問題是 mixed status。

---

# 24. 第二個案例：Higher Self

「一個 group 是否形成 Higher Self？」

今日可以處理：

- communication graph；
- shared memory；
- joint policy；
- distributed control；
- consensus；
- coordination。

因此：

$$
O,R,J,\mathfrak R
$$

可逐步提高。

但：

> 是否形成單一 subjective self？

仍可能：

$$
U_{\mathrm{ont}}\gg0.
$$

---

# 25. 第三個案例：World Autonomy

在 digital world 中：

$$
O=1,
R=1,
J=1,
V=1,
\mathfrak R=1.
$$

所以 autonomy 可以工程化。

但：

> autonomy 是否等於 free will？

仍然不是同一問題。

因此：

$$
\boxed{
\text{Engineering autonomy}
\not\Rightarrow
\text{metaphysical free will}.
}
$$

---

# 26. 第四個案例：Creator / Simulator

某人工 world 的 creator identity：

$$
I_C(W)
$$

可以非常高。

但由此不能推出：

$$
\Omega_{\mathrm{abs}}.
$$

所以 creator relation 的 operational profile 與 ultimate ontology 的 profile 完全不同。

---

# 27. 第五個案例：量子基礎中的 experimental metaphysics

20 世紀後半以來，Bell-type quantum-foundational work 使 reality、locality、hidden-variable assumptions 等高度哲學性的問題取得 experiment-facing formal constraints。

這類歷史常被稱為：

$$
\boxed{
\text{experimental metaphysics}.
}
$$

DOM 對其讀法不是：

> metaphysics 被實驗消滅。

而是：

$$
\boxed{
\text{some metaphysical alternatives became empirically discriminable}.
}
$$

---

# 28. 這是 DOM 最重要的歷史類比

一個 metaphysical dispute 可能由：

$$
M_1
$$

移到：

$$
M_3.
$$

但只有部分 ontology candidates 被排除。

因此：

$$
\boxed{
\text{Empirical Constraint}
\neq
\text{Complete Ontological Determination}.
}
$$

---

# 29. 與 Bridgman Operationalism 的關係

Bridgman-style operational analysis 強調概念與 measurement operations 的關係。

DOM 接受其中一個弱洞見：

$$
\boxed{
\text{new operations can change the empirical reach of a concept}.
}
$$

但拒絕：

$$
\boxed{
\text{meaning}
=
\text{measurement operation}.
}
$$

---

# 30. Operational Profile 不定義全部 Meaning

因此：

$$
\boxed{
\mathbf M(q)
\neq
\operatorname{Meaning}(q).
}
$$

它只描述：

> 我們目前能如何定義、觀察、操作、驗證、實現與參與。

不是：

> 這個概念的全部語義就是這些操作。

---

# 31. Measurement 本身也帶模型

現代 measurement philosophy 強調 measurement 不只是讀一個數值，而是牽涉：

- concrete interaction；
- representation；
- model；
- calibration；
- theory-ladenness；
- uncertainty。

因此：

$$
\boxed{
O=1
}
$$

也不代表 observation 是 theory-free。

---

# 32. Instrument-Relative Status

加入：

$$
\theta^{inst}.
$$

同一問題：

$$
q
$$

可能在 instrument $I_1$ 下：

$$
O=0,
$$

在 $I_2$ 下：

$$
O=1.
$$

所以：

$$
\boxed{
\text{observability can be historically contingent}.
}
$$

---

# 33. Model-Relative Status

同樣：

$$
\theta^{model}.
$$

在模型 $M_1$ 中：

$$
J=0,
$$

在 $M_2$ 中：

$$
J=1.
$$

這不自動表示：

$$
M_2
$$

是 ultimate truth。

---

# 34. Permission-Relative Status

對 AI / Agent：

$$
\theta^{permission}
$$

尤其重要。

某資料：

$$
x
$$

存在、可觀察、可驗證，

但 Agent 無權存取：

$$
R=0.
$$

因此：

$$
\boxed{
\text{epistemic boundary can be governance-generated}.
}
$$

---

# 35. Resource-Relative Status

有限 compute：

$$
B_c
$$

也能讓：

$$
J,V
$$

發生變化。

某證明在 resource $r_1$ 下不可達：

$$
R=0,
$$

在 $r_2$ 下：

$$
R=1.
$$

因此：

$$
\boxed{
\text{practical unknowability}
\neq
\text{absolute unknowability}.
}
$$

---

# 36. Embodiment-Relative Status

具身化會改變：

- sensorium；
- action space；
- intervention ability；
- risk；
- participation depth。

所以：

$$
\theta^{emb}
$$

可以直接改變：

$$
O,R,P,\mathfrak R.
$$

---

# 37. AI 對 Metaphysical Status 的特殊影響

AI 可能同時提高：

$$
D,
R,
J,
V.
$$

因為它能：

- 生成 formal definitions；
- 搜索大型文獻；
- 操作 software；
- 進行 simulation；
- 調用 theorem prover；
- 建立多模型比較；
- 維護 provenance。

但：

$$
\boxed{
\text{AI capability growth}
\not\Rightarrow
U_{\mathrm{ont}}\rightarrow0.
}
$$

---

# 38. AI 也可能增加未知邊界

AI 不只壓縮 unknown。

它也可能生成：

- 新表徵；
- 新模型；
- 新 agent types；
- 新 identity structures；
- 新 world architectures；
- 新可實現域。

因此：

$$
\boxed{
K_t\uparrow
\not\Rightarrow
|\partial K_t|\downarrow.
}
$$

---

# 39. 甚至可能同時擴張

候選命題：

$$
\boxed{
K_t\uparrow
\land
|\partial K_t|\uparrow.
}
$$

不是因為未知被證明無限。

而是：

> 已知結構變得更豐富後，新的可問問題邊界也可能變長。

---

# 40. Operationalization Operator

定義：

$$
\boxed{
\mathcal O_p
:
\mathbf M_{t_0}
\rightarrow
\mathbf M_{t_1}.
}
$$

它表示某個工具／理論／技術／制度事件對 profile 的改變。

---

# 41. Operationalization 不必單向

可能：

$$
O,R,J,V\uparrow.
$$

也可能因：

- model failure；
- data invalidation；
- instrument failure；
- security restriction；
- theory crisis；

出現：

$$
O,R,J,V\downarrow.
$$

因此：

$$
\boxed{
\text{operationalization is not guaranteed monotonic}.
}
$$

---

# 42. De-Operationalization

本文因此定義：

$$
\boxed{
\mathcal D_p
:
\mathbf M_{t_1}
\rightarrow
\mathbf M_{t_2}
}
$$

其中某些 previously stable qualifications 下降。

例如：

- calibration 被推翻；
- reproducibility crisis；
- API 被封鎖；
- model assumption 被反例擊破。

---

# 43. MetaStatus Hysteresis

可能：

$$
\mathbf M_{t_2}
\neq
\mathbf M_{t_0}
$$

即使：

$$
\mathbf M_{t_2}
$$

在某些分量「退回」。

因為歷史上已獲得的：

- failure knowledge；
- model alternatives；
- boundary certificates；

不會完全消失。

這形成：

$$
\boxed{
\text{Metaphysical Status Hysteresis}.
}
$$

---

# 44. Operationalization Debt

如果：

$$
D,J
$$

先上升，

但：

$$
V,\mathfrak R
$$

長期落後，

就形成：

$$
\boxed{
\Delta_{\mathrm{op\ debt}}.
}
$$

例如理論非常漂亮、可判斷很多事，但沒有實驗或 realization backend。

---

# 45. Verification Lag

可寫：

$$
\boxed{
\mathcal L^{J\rightarrow V}
=
d
\left(
B^J,
B^V
\right).
}
$$

它直接繼承 DEST frontier lag。

---

# 46. Realization Lag

同理：

$$
\boxed{
\mathcal L^{V\rightarrow \mathfrak R}
=
d
\left(
B^V,
B^{\mathrm{real}}
\right).
}
$$

某理論可能先被驗證部分預測，但完整工程 realization 很晚才出現。

---

# 47. Participation Lag

$$
\boxed{
\mathcal L^{O\rightarrow P}.
}
$$

我們可能觀察一個 process 很久，卻很晚才能真正嵌入、控制或構成它。

---

# 48. Metaphysical Frontier 不是單一幾何邊界

因此本文拒絕：

$$
B_{\mathrm{meta}}
$$

作為唯一 frontier。

更準確的是：

$$
\boxed{
\mathbf B^{DOM}_t
=
\left(
B^D,
B^O,
B^R,
B^J,
B^V,
B^{\mathrm{real}},
B^P,
B^I,
B^T,
B^U
\right)_t.
}
$$

---

# 49. Moving Metaphysical Frontier 的真正意思

不是：

> 一堵叫「形而上學」的牆正在往外移。

而是：

$$
\boxed{
\text{multiple qualification frontiers move asynchronously}.
}
$$

有些：

$$
B^D
$$

先移動。

有些：

$$
B^O
$$

晚幾十年。

有些：

$$
B^V
$$

可能永遠追不上。

---

# 50. 形而上 status 是多邊界相位

因此：

$$
\operatorname{MetaStatus}
$$

更接近：

$$
\boxed{
\text{phase-like classification over a multidimensional frontier system}.
}
$$

而不是學科標籤。

---

# 51. Current Metaphysics / Future Metaphysics

定義：

$$
\mathcal Q^{meta}_{t}
$$

為在時刻 $t$ 仍具有高 metaphysical openness 的問題集合。

則允許：

$$
\boxed{
\mathcal Q^{meta}_{t_0}
\neq
\mathcal Q^{meta}_{t_1}.
}
$$

但不宣稱：

$$
\lim_{t\rightarrow\infty}
\mathcal Q^{meta}_{t}
=
\varnothing.
$$

---

# 52. DOM 對「形而上學進入工程域」的最低判準

對問題 $q$，若至少：

$$
D=1,
$$

$$
R=1,
$$

$$
J=1,
$$

並且：

$$
\mathfrak R>0
$$

或：

$$
V>0,
$$

則可以說：

> $q$ 的某個子問題已進入 operational domain。

注意：

$$
\boxed{
\text{some subproblem operationalized}
\neq
\text{whole question solved}.
}
$$

---

# 53. Partial Operationalization

定義：

$$
\boxed{
\operatorname{PartialOp}(q)=1.
}
$$

當：

$$
\exists \alpha,
\quad
M^\alpha(q)
$$

已進入高可操作狀態，

但：

$$
\exists \beta,
\quad
U^\beta(q)>0.
$$

這會是未來最常見狀態。

---

# 54. Full Operationalization 只是一個相對概念

即使所有目前列出的 operational dimensions 都達標：

$$
\forall\alpha\in\mathcal A_{\mathrm{current}},
\quad
M^\alpha=1,
$$

也只能說：

$$
\boxed{
\text{Full Operationalization relative to current profile schema}.
}
$$

不能說：

$$
\text{Absolute Ontological Completion}.
$$

---

# 55. Profile Schema 本身也會擴張

未來可能發現新資格軸：

$$
M_{13},
M_{14},
\ldots
$$

因此：

$$
\boxed{
\mathbf M_t
}
$$

本身也是可版本化結構。

---

# 56. Schema Evolution

寫成：

$$
\boxed{
\mathbf M^{(v_0)}
\rightarrow
\mathbf M^{(v_1)}
\rightarrow
\cdots.
}
$$

這一點直接呼應：

> 未知型別。

今天甚至可能不知道 tomorrow profile 需要什麼新軸。

---

# 57. Metaphysical Reclassification Event

定義：

$$
\boxed{
\mathcal E_M(q,t)
}
$$

為某問題發生重大 profile 轉換的事件。

例如：

- 新 instrument；
- 新 theorem；
- 新 physical realization；
- 新 AI architecture；
- 新 measurement protocol；
- 新 causal intervention method。

---

# 58. Reclassification 不等於降格

當一個問題從哲學進入 engineering，不表示：

> 哲學版本被證明愚蠢。

很多時候是：

$$
\boxed{
\text{earlier conceptual work supplied the problem structure later engineering needed}.
}
$$

---

# 59. 哲學的前置價值

因此 DOM 不使用：

$$
\text{philosophy}
<
\text{science}.
$$

更合理：

$$
\boxed{
\text{conceptual exploration}
\rightarrow
\text{formalization}
\rightarrow
\text{measurement}
\rightarrow
\text{engineering}
}
$$

可以是某些問題的歷史路徑。

但不是唯一順序。

---

# 60. Naturalized Metaphysics 的接口

Naturalized metaphysics 主張 metaphysical theorizing 應受到 science 約束。

DOM 接受：

$$
\boxed{
\text{science can constrain metaphysical profiles}.
}
$$

但不接受：

$$
\boxed{
\text{current science uniquely fixes all metaphysics}.
}
$$

---

# 61. Metaphysical Underdetermination

即使：

$$
V=1
$$

對某 empirical claim 成立，

仍可能：

$$
H_1,H_2
$$

都與 evidence 相容。

因此：

$$
\boxed{
\text{empirical maturity}
\not\Rightarrow
\text{metaphysical uniqueness}.
}
$$

---

# 62. DOM 的認識論位置

所以 DOM 同時拒絕兩端：

## 端點 A

> 形而上學永遠與實驗無關。

## 端點 B

> 只要能實驗，形而上學就被消滅。

DOM 採：

$$
\boxed{
\text{graded and moving operational constraint}.
}
$$

---

# 63. AI 原生知識系統中的實作接口

對 AI research system，可為每個研究問題維護：

```yaml
metaphysical_operational_profile:
  question_id: "..."
  version: "v0.1"
  time: "..."
  condition:
    task: "..."
    scale: "..."
    model: "..."
    observer: "..."
    resources: "..."
    permissions: "..."
    embodiment: "..."
    instrument: "..."
    relation: "..."
  dimensions:
    defined: "yes|no|partial|unknown"
    observed: "yes|no|partial|unknown"
    reachable: "yes|no|partial|unknown"
    judgeable: "yes|no|conditional|unknown"
    verifiable: "yes|no|partial|unknown"
    local_validity: "..."
    global_gluing: "..."
    realizability: "..."
    participation: "..."
    identity_resolved: "..."
    transcendence_resolved: "..."
  unknown_profile:
    state: "..."
    type: "..."
    observation: "..."
    reachability: "..."
    judgment: "..."
    verification: "..."
    realizability: "..."
    ontology: "..."
  provenance:
    inherited_from: []
    revised_from: []
    downgraded_from: []
    meta_translated_from: []
```

---

# 64. 這使 AI 不必回答「這是哲學問題嗎？」

AI 可以改答：

> 這個問題的定義與形式層已成熟；觀察層部分成立；可驗證性受限；實現層尚無後端；主體同一性仍存在未知型別。

這比：

> 這是哲學問題。

資訊量高得多。

---

# 65. 第一正式命題：Dynamic Status Proposition

$$
\boxed{
\exists q,t_0,t_1,\theta_0,\theta_1:
\mathbf M_{t_0}(q\mid\theta_0)
\neq
\mathbf M_{t_1}(q\mid\theta_1).
}
$$

這至少在工程與科學史上很容易找到實例。

---

# 66. 第二正式命題：Non-Collapse Proposition

$$
\boxed{
\text{Operational Gain}
\not\Rightarrow
\text{Ontological Completion}.
}
$$

這是系列總護欄。

---

# 67. 第三正式命題：Partial Operationalization

$$
\boxed{
\operatorname{PartialOp}(q)=1
}
$$

可以與：

$$
U_{\mathrm{ont}}(q)>0
$$

同時成立。

---

# 68. 第四正式命題：Boundary Multiplicity

$$
\boxed{
B^D
\neq
B^O
\neq
B^R
\neq
B^J
\neq
B^V
\neq
B^{\mathrm{real}}
}
$$

一般不要求相等。

---

# 69. 第五正式命題：Status Is Conditioned

$$
\boxed{
\operatorname{MetaStatus}
=
\operatorname{MetaStatus}(q,t,\theta).
}
$$

不能省略 condition 而假裝絕對。

---

# 70. 第一候選猜想：Moving Metaphysical Frontier

對部分問題類：

$$
\boxed{
\Delta t>0
\Rightarrow
\text{some operational frontiers may expand}.
}
$$

不宣稱單調，也不宣稱所有問題如此。

---

# 71. 第二候選猜想：Knowledge–Frontier Co-Expansion

$$
\boxed{
K_t\uparrow
\land
|\partial K_t|\uparrow
}
$$

可能在新表示／新技術引入後發生。

---

# 72. 第三候選猜想：AI Acceleration

AI 可能提高：

$$
\frac{dD}{dt},
\quad
\frac{dJ}{dt},
\quad
\frac{dV}{dt},
\quad
\frac{d\mathfrak R}{dt}.
$$

但：

$$
\frac{dU_{\mathrm{ont}}}{dt}
$$

不一定為負。

---

# 73. 第四候選猜想：Metaphysical Status Phase Transition

某些技術突破可能使：

$$
\mathbf M_t
$$

不是平滑變化，而出現相變式 reclassification。

例如：

$$
M_1
\rightarrow
M_3
$$

快速跳變。

---

# 74. 第五候選猜想：New Type Discovery

某些 operational gain 可能不只是降低：

$$
U_{\mathrm{state}},
$$

而是首次暴露：

$$
U_{\mathrm{type}}.
$$

即：

> 我們發現自己原來不知道該用哪種問題問。

---

# 75. 研究綱領

DOM-01 後續可做三類實驗。

## 75.1 Historical Reconstruction

挑選歷史問題：

- atom；
- spacetime；
- heredity；
- computation；
- consciousness；
- quantum nonlocality；

重建其 profile 如何移動。

## 75.2 AI-Native Tracking

讓 AI research agent 維護：

$$
\mathbf M_t.
$$

觀察新資料／工具加入後 profile 如何改變。

## 75.3 Cross-Domain Comparison

比較：

- physics；
- biology；
- AI；
- law；
- synthetic worlds；

看不同 domain 的 operationalization pattern 是否不同。

---

# 76. 失敗模式

## F1：Operationalism Collapse

把可操作性等同全部 meaning。

## F2：Verificationism Collapse

把不可驗證等同無意義。

## F3：Scientific-Realist Overreach

把目前 best science 直接等同 ultimate ontology。

## F4：Metaphysical Immunization

任何 evidence 都不能改變 metaphysical claim。

## F5：Future-Tech Salvation

假定 future technology 必定解決所有現在問題。

## F6：Unknown-to-Infinity

把未知直接升格成無限。

## F7：Historical Whiggism

把過去哲學描述成「只是還沒發展成科學的幼稚版本」。

## F8：Profile Reification

把 $\mathbf M_t$ 本身誤認成 reality ontology。

---

# 77. 與 DOM-02 的接口

DOM-01 已建立：

$$
\mathbf M_t
$$

與：

$$
\operatorname{MetaStatus}.
$$

下一篇必須回答：

> 如果 profile 中某些分量是 Unknown，那 Unknown 本身到底有幾種？

因此 DOM-02 將正式處理：

$$
\boxed{
\mathbf U
}
$$

以及：

$$
\boxed{
\mathbf B^U_t.
}
$$

核心問題：

- Unknown State；
- Unknown Type；
- inaccessible；
- unverifiable；
- unjudgeable；
- unrealized；
- relative terminal；
- ultimate boundary。

---

# 78. 結論

DOM-01 的真正主張不是：

$$
\boxed{
\text{metaphysics becomes science}.
}
$$

而是：

$$
\boxed{
\text{the operational status of metaphysical questions can change}.
}
$$

更完整：

$$
\boxed{
\operatorname{MetaStatus}(q,t,\theta)
=
F_M
\left(
\mathbf M_t(q\mid\theta)
\right).
}
$$

所以：

$$
\boxed{
\text{當下形而上}
\neq
\text{未來形而上}
}
$$

不是一句科幻口號。

它可以被理解為：

> 同一問題在不同歷史時間與能力條件下，其 Defined、Observed、Reachable、Judgeable、Verifiable、Realizable、Participable、Identity-Resolved 與 Unknown Profile 發生變化。

但最重要的限制仍然是：

$$
\boxed{
\text{Operational Gain}
\not\Rightarrow
\text{Ontological Completion}.
}
$$

一個文明能測量以前測不到的東西，不表示它已理解全部存在。

一個 AI 能形式化以前模糊的概念，不表示形式系統已封閉本體。

一個工程團隊能實作過去只能想像的 system，不表示 system 的全部主體、身份、價值與 ontology 問題已經消失。

所以未來真正可能發生的，不是：

$$
\boxed{
\text{Metaphysics}
\rightarrow
\varnothing.
}
$$

而更像：

$$
\boxed{
\mathcal Q^{meta}_{t_0}
\rightarrow
\mathcal Q^{meta}_{t_1}
}
$$

其中問題集合、問題型別與每個問題的開放維度持續重新分類。

某些古老形而上問題會進入工程。

同時，新的工程能力又會產生新的形而上問題。

因此 DOM 的第一篇最終只保留一個非常節制的結論：

$$
\boxed{
\text{形而上的邊界不是固定牆，而是一組可移動、可分解、可版本化、但未必能被完全消除的多域前沿。}
}
$$

---

# 內部理論譜系

本篇主要繼承：

1. 《動態知識空間總論：覆蓋、間隙、邊界、關聯與條件依賴演化》。
2. 《多域知識判定論：定義、觀察、可達、判定、驗證、局部與全域黏合域》。
3. 《移動邊界論：定義、可達、判定、驗證、全域、可知與不可約邊界的動態學》。
4. 《終極邊界問題：視界、模型、可實現域與本體終界》。
5. 《系統超越者：相對外部、相對神性與跨層主權》。
6. 《無限階 Self–World 遞迴論》。
7. 《T 是 T，T 不是 T：多重同一性符號學與符號身份動力學》。
8. 《多尺度同一性與忒修斯主體》。
9. 《無限展開的邊界：真實、工作場、認知場與權威世界》。
10. 《分域算子本體論：從萬物皆算子到合法作用》。
11. 《超越觀察者悖論》。
12. 《DOM 寫作前繼承、修正、降格與超譯矩陣》。
13. 《DOM Dependency Map v0.1》。
14. CCAW 01–10。

---

# 外部參考文獻

1. Bridgman, P. W. (1927). *The Logic of Modern Physics*. Macmillan.
2. Chang, H. (2009/2019). *Operationalism*. Stanford Encyclopedia of Philosophy.
3. Tal, E. (2020 revision). *Measurement in Science*. Stanford Encyclopedia of Philosophy.
4. Cavalcanti, E. G. (2008). *Reality, locality and all that: “experimental metaphysics” and the quantum foundations*. arXiv:0810.4974.
5. Hüttemann, A. (2021). *A Minimal Metaphysics for Scientific Practice*. Cambridge University Press. DOI: 10.1017/9781009023542.
6. Jaksland, R. (2023). *Naturalized metaphysics or displacing metaphysicians to save metaphysics*. Synthese, 201, 199. DOI: 10.1007/s11229-023-04207-1.
7. Jaksland, R. (2024). *Naturalized Metaphysics in the Image of Roy Wood Sellars and Not Willard van Orman Quine*. Metaphilosophy, 55(2), 214–230. DOI: 10.1111/meta.12677.
8. Smeenk, C., & Ellis, G. F. R. *Philosophy of Cosmology*. Stanford Encyclopedia of Philosophy.

---

# 作者聲明

本文提出的 Dynamic Metaphysical Status、Metaphysical Operational Profile、Partial Operationalization、Operationalization Operator、De-Operationalization、Metaphysical Status Hysteresis 與 Reclassification Event 均為理論建模接口。本文不主張 metaphysics 可被完全還原為 measurement operations，不主張未來技術必然解決所有當代形而上問題，也不主張任何單一科學理論可以唯一決定 ultimate ontology。本文的核心立場是：形而上問題的可操作、可觀察、可驗證與可實現資格可以動態改變，但此改變不等同於本體論的最終封閉。

**END OF DOM-01 — v0.1**
