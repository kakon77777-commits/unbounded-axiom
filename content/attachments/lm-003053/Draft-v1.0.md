# LSI-PSD-08 — 生產性錯置：錯誤問題如何生成正確的後代理論

## Productive Mis-specification: How a Wrong Parent Problem Can Generate Correct Descendants

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

科學史與現代模型研究反覆顯示：一個模型可以包含錯誤本體、理想化假設、尺度錯置或缺失機制，卻仍產生可重現、可移植甚至後來被保留的局部結構。本文把這種現象形式化為「生產性錯置」。核心區分是 parent validity 與 descendant validity：父問題、父模型或父 framing 的錯誤不會邏輯上污染所有後代理論；反之，後代中出現真實定理或有用工具，也不能倒推父 framing 正確。本文定義 mis-specification vector、descendant graph、truth retention、transfer utility 與 salvage ratio，並提出「父子真值分離原則」。2026 年 missing-physics discovery 的工作進一步顯示，模型誤差可以被局部化並轉化成缺失機制的符號發現；這提供了從「錯誤」走向「可測 discrepancy」的工程接口。本文同時設置嚴格限制：生產性錯置不等於任意錯誤，必須要求與資料、形式驗證、局部有效域或可重建機制保持接觸。

**關鍵詞：** 生產性錯置、productive mis-specification、model discrepancy、missing physics、descendant theory、structured error

---

## 1. 父問題錯，不代表子結果都錯

設父問題或父模型為：

$$
P.
$$

它在研究過程中產生 descendant set：

$$
\mathcal D(P)
=
\{D_1,D_2,\ldots,D_n\}.
$$

常見但錯誤的直覺是：

$$
P=\text{false}
\Rightarrow
D_i=\text{false for all }i.
$$

這在邏輯上並不成立。

一個錯誤模型仍可包含：

- 正確的局部關係；
- 正確的 limit；
- 正確的 invariant；
- 有效 approximation；
- 可重用的數學工具；
- 新實驗；
- 新測量技術；
- 對錯誤來源的診斷。

所以必須把 parent status 與 descendant status 分離。

---

## 2. 父子真值分離原則

本文提出：

$$
\boxed{
V(P)
\not\Rightarrow
V(D_i)
}
$$

以及：

$$
\boxed{
V(D_i)
\not\Rightarrow
V(P),
}
$$

其中 $V$ 表示適合該 domain 的 validity predicate。

更具體地：

$$
\neg V(P)
\centernot\Rightarrow
\forall i\,\neg V(D_i).
$$

這是生產性錯置的邏輯底座。

---

## 3. Mis-specification vector

「錯」不是單一軸。定義：

$$
\epsilon(P)
=
(
\epsilon_D,
\epsilon_S,
\epsilon_A,
\epsilon_M,
\epsilon_R
).
$$

其中：

- $\epsilon_D$：domain mismatch；
- $\epsilon_S$：semantic / representation mismatch；
- $\epsilon_A$：assumption mismatch；
- $\epsilon_M$：missing mechanism；
- $\epsilon_R$：resolution / scale mismatch。

兩個模型可能有相似總誤差，但錯在完全不同位置。

因此任何「錯誤越多越有生成性」的粗糙命題都應被拒絕。

---

## 4. Structured error 與 arbitrary error

本文只研究 structured error。

一個錯置若要具有研究價值，至少滿足其中數項：

1. 有明確 validity regime；
2. 能生成可檢驗預測；
3. 偏差能被測量；
4. 有可識別 residual；
5. 可對照更高 fidelity 模型；
6. 產生的子命題能獨立驗證；
7. 錯誤可以被局部化或拆分；
8. 研究路徑可重建。

反之，任意拼湊且不接受反駁的框架不屬於 productive mis-specification。

---

## 5. 後代理論圖

定義 descendant graph：

$$
\mathcal G_P
=
(V_P,E_P).
$$

節點包括：

- parent assumptions；
- intermediate lemmas；
- derived models；
- experimental designs；
- computational tools；
- transferable theorems；
- corrected formulations。

每個 descendant $D_i$ 都需要自己的 validation status：

$$
v_i
\in
\{
\text{unverified},
\text{numerically supported},
\text{formally proved},
\text{empirically confirmed},
\text{refuted}
\}.
$$

這能避免研究者把「父框架有問題」當成一次性刪庫理由。

---

## 6. Truth retention 與 salvage ratio

定義經獨立審計後仍成立的 descendants：

$$
\mathcal D^+(P).
$$

truth retention ratio：

$$
R_T(P)
=
\frac{
|\mathcal D^+(P)|
}{
|\mathcal D(P)|
}.
$$

但不同成果價值不同，所以再定義 weighted salvage ratio：

$$
R_S(P)
=
\frac{
\sum_{D_i\in\mathcal D^+(P)}w(D_i)
}{
\sum_{D_i\in\mathcal D(P)}w(D_i)
}.
$$

$w$ 可以根據：

- formal strength；
- empirical support；
- transfer count；
- downstream usage；
- reproducibility；

設定。

這兩個指標都不能評價父命題真值，只評價「錯置後留下多少可救回的知識」。

---

## 7. Missing physics 作為現代工程接口

2026 年 LISDD 的核心問題非常接近本文精神：物理模型不一定在所有 operating regimes 中同樣錯。它先找 clean regime，再定位 discrepancy region，最後從候選 symbolic library 中辨識 missing mechanism。

可抽象為：

$$
\text{trusted model}
+
\text{localized discrepancy}
\to
\text{candidate missing term}.
$$

這個流程顯示，錯誤不一定只能被整體拋棄，而可以被轉成：

$$
\text{where wrong}
+
\text{how wrong}
+
\text{what is missing}.
$$

本文把這種局部化能力視為 productive mis-specification 的必要工程條件之一。

---

## 8. 為什麼錯置會增加生成性

若原定義 $D^\star$ 已高度閉合：

$$
|\Omega(D^\star)|\ll|\Omega(D')|.
$$

當某個有限錯置 $D'$ 引入額外自由度時，研究系統會被迫處理：

- correction terms；
- boundary regimes；
- incompatibilities；
- residual dynamics；
- alternative variables；
- new limiting cases。

因此 descendant count 可以增加。

但這不是好事的保證。只有其中能通過獨立 validation 的部分才算 epistemically salvageable。

---

## 9. 對數學未解問題的限制

如果某個未解問題長期產生大量正確子理論，我們不能因此說：

$$
\text{parent problem is mis-specified}.
$$

因為任何真正困難且正確表述的問題，也可能具有巨大 descendant graph。

所以：

$$
\boxed{
G(P)\uparrow
\not\Rightarrow
\operatorname{MisSpecified}(P).
}
$$

要支持 mis-specification hypothesis，還需要：

- 明確 category inconsistency；
- semantic non-equivalence；
- proof obligation 與實際 target 不一致；
- 新 formulation 對 recurrent obstruction 有統一解釋；
- 或形式證明舊 formulation 沒有預期的 truth condition。

這條限制對 NS 與 P vs NP 尤其重要。

---

## 10. 生產性錯置與「問錯問題」

本文不使用「問錯問題」作粗糙結論。

更精確的情形至少有：

$$
\text{ill-posed},
$$

$$
\text{well-posed but unhelpful},
$$

$$
\text{well-posed but representation-poor},
$$

$$
\text{domain-misaligned},
$$

$$
\text{scale-misaligned},
$$

$$
\text{partially valid}.
$$

productive mis-specification 主要研究中間地帶，而不是把所有非最優 framing 都叫錯。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $P$ | parent problem / model |
| $\mathcal D(P)$ | descendant set |
| $\epsilon(P)$ | mis-specification vector |
| $\mathcal G_P$ | descendant graph |
| $R_T(P)$ | truth retention ratio |
| $R_S(P)$ | weighted salvage ratio |
| $w(D_i)$ | descendant value weight |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-07。  

**後續：** LSI-PSD-09、11、12。

---

## 結論

生產性錯置最重要的不是替錯誤辯護，而是拒絕兩種粗暴刪除：

$$
\text{wrong parent}
\Rightarrow
\text{all descendants worthless}
$$

與：

$$
\text{useful descendants}
\Rightarrow
\text{parent must be right}.
$$

真正成熟的研究系統應該把父問題與子成果拆開驗證，留下可以 salvage 的知識，同時允許父 framing 被修正、替換甚至放棄。

---

## 參考文獻

1. Yifan Wang. *Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy*. arXiv:2606.23215, 2026.
2. Authors. *Learning Missing Physics, Modeling Systematic Residuals*. SIAM Journal on Scientific Computing, DOI 10.1137/22M148375X.
3. Roman Frigg and Stephan Hartmann. *Models in Science*. Stanford Encyclopedia of Philosophy, current online edition, accessed 2026-08-17.
4. Karla Weingarten. *Productive Idealizations for Scientific Understanding*. PhilSci-Archive preprint, 2026.
5. Clay Mathematics Institute. *Navier--Stokes Equation: Existence and Smoothness*. Official Millennium Prize Problem page and Charles L. Fefferman problem description, accessed 2026-08-17. https://www.claymath.org/millennium/navier-stokes-equation/
6. Clay Mathematics Institute. *P vs NP*. Official Millennium Prize Problem page, accessed 2026-08-17. https://www.claymath.org/millennium/p-vs-np/
