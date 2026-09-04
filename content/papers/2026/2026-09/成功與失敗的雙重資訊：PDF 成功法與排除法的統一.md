# 成功與失敗的雙重資訊：PDF 成功法與排除法的統一

## Dual Information in Success and Failure: Unifying PDF Formation and Falsification

**系列**：遞歸折疊認識論：從 PDF 成功—排除雙法到多模型可修正認知，第 2 篇／共 8 篇＋1 篇總結  
**系列英文名**：Recursive Fold Epistemology: From the PDF Success–Falsification Duality to Corrigible Multi-Model Cognition  
**文件編號**：EML-RFE-2026-02-v0.1  
**作者**：Neo.K with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-09-02  
**性質**：認識論／Bayesian Updating／Information Theory／Evidence Architecture／PDF Duality  
**狀態**：Public Theory Draft  
**直接前置**：EML-RFE-2026-01《不會錯的不是理論》  
**吸收之未公開內部原型**：《PDF成功法：知識構建的螺旋辯證論》；《PDF排除法的形式化理論：失敗驅動的螺旋認識論》

---

## 生成、版本與修正聲明

本文正式吸收兩篇未公開的 PDF 方法原型：

- PDF 成功法（Proof by Data Formation）；
- PDF 排除法（Proof by Data Falsification）。

舊版的重要直覺保留：

$$
\boxed{
\text{Construction Matters}
}
$$

與：

$$
\boxed{
\text{Contradiction Matters}.
}
$$

但本文明確修正三項過強命題。

第一，舊版曾把「任何非平凡單次觀測都使後驗理論熵嚴格下降」寫成一般定理。新版修正為：

$$
\boxed{
H(\Theta\mid D)
\le
H(\Theta)
}
$$

是**對資料分佈取期望後的條件熵關係**；對某一個已實現的具體觀測 $d$，後驗熵：

$$
H(\Theta\mid D=d)
$$

可能下降，也可能上升。

第二，舊版曾把「失敗即進步」寫得近似無條件。新版改為：

$$
\boxed{
\text{Informative Failure}
+
\text{Valid Update}
\Rightarrow
\text{Potential Epistemic Progress}.
}
$$

噪音、錯誤儀器、無區分力測試與未被吸收的失敗，不自動構成進步。

第三，舊版曾把知識空間的累積描述成嚴格單調。新版區分：

$$
D_t
=
\text{Evidence Ledger},
$$

與：

$$
K_t
=
\text{Current Accepted Knowledge}.
$$

證據歷史可盡可能累積保存，但目前接受的知識可以被撤回、降級、重新解釋或重構。

因此本文不是舊 PDF 雙法的重印，而是其 canonical 改良版。

---

# 摘要

科學與一般認知活動經常把「成功」與「失敗」視為相反結果。支持假設的觀測被稱為成功，違反預測的觀測被稱為失敗。這種語言在工程管理上方便，卻容易把結果情緒與認識論價值混為一談。

本文提出：

$$
\boxed{
\text{Outcome Valence}
\neq
\text{Epistemic Information}.
}
$$

一個「成功」實驗可能幾乎沒有區分力；一個「失敗」實驗也可能大幅重排候選理論。反之，一個失敗也可能只是不良儀器或無法重現的噪音。

因此，成功與失敗應統一視為：

$$
\boxed{
\text{Evidence Events}.
}
$$

令當前理論空間為：

$$
\Theta_t
=
\{T_1,T_2,\ldots,T_n\},
$$

其先驗或當前權重為：

$$
q_t(T).
$$

觀測到資料：

$$
D=d.
$$

貝葉斯更新為：

$$
q_{t+1}(T)
=
P(T\mid d)
=
\frac{P(d\mid T)q_t(T)}
{\sum_jP(d\mid T_j)q_t(T_j)}.
$$

本文以「貝葉斯驚奇」：

$$
\boxed{
\mathcal I_d
=
D_{\mathrm{KL}}
\left(
q_{t+1}(T)
\Vert
q_t(T)
\right)
\ge0
}
$$

作為單次證據改變信念分佈程度的一個概念量。

若：

$$
q_{t+1}=q_t,
$$

則：

$$
\mathcal I_d=0.
$$

表示該觀測在當前模型空間與更新規則下沒有改變理論權重。

對資料分佈取期望：

$$
\boxed{
\mathbb E_D[\mathcal I_D]
=
I(\Theta;D)
\ge0.
}
$$

這才是互資訊意義下「資料平均降低理論不確定性」的嚴格形式。

但即使：

$$
\mathcal I_d>0,
$$

也不能自動推出：

$$
\text{Closer to Truth}.
$$

因為：

- 真模型可能不在 $\Theta_t$ ；
- likelihood 可能錯；
- 資料可能受污染；
- 更新規則可能錯；
- 觀測可能被錯誤建模。

因此本文把「資訊增益」與「認識論進步」再次分離：

$$
\boxed{
\text{Information Gain}
\neq
\text{Guaranteed Truth Gain}.
}
$$

PDF 成功法與排除法於是被重新統一為一個雙重資訊架構：

$$
\boxed{
\text{Construct}
\rightarrow
\text{Observe}
\rightarrow
\text{Discriminate}
\rightarrow
\text{Update}
\rightarrow
\text{Preserve}
\rightarrow
\text{Reframe}.
}
$$

成功法主要處理：

$$
\boxed{
\text{What did this inquiry construct or reveal?}
}
$$

排除法主要處理：

$$
\boxed{
\text{What did this inquiry make less plausible or impossible?}
}
$$

兩者共同更新：

$$
\boxed{
\mathcal E_t
=
(
\Theta_t,D_t,K_t,F_t,U_t
).
}
$$

因此新版 PDF 雙法不再將「成功」與「失敗」視為兩種不同的科學，而是把它們視為同一證據更新過程的兩個方向。

**關鍵詞**：PDF 成功法、PDF 排除法、證據事件、貝葉斯驚奇、互資訊、失敗資訊、知識帳本、認識論更新、可修正認知

---

# 0. 為什麼成功與失敗需要重新定義？

研究者常說：

> 實驗成功了。

通常代表：

$$
d
\approx
\hat d(T).
$$

也就是觀測符合某個預測。

而：

> 實驗失敗了。

常代表：

$$
d
\not\approx
\hat d(T).
$$

但這兩句其實混合了至少三種不同事情：

1. 實驗是否正確執行；
2. 觀測是否符合預測；
3. 結果是否具有認識論資訊。

---

# 1. 工程成功與理論成功不同

一個實驗可以：

$$
\boxed{
\text{Operational Success}
}
$$

但：

$$
\boxed{
\text{Hypothesis Failure}.
}
$$

例如儀器正常、流程正確，

結果卻否定預測。

這不應被叫成「整體失敗」。

---

# 2. 理論支持也不等於認識論成功

若：

$$
P(d\mid T_1)
\approx
P(d\mid T_2)
\approx
\cdots
\approx
P(d\mid T_n),
$$

即使 $d$ 符合 $T_1$，

也幾乎沒有區分模型。

所以：

$$
\boxed{
\text{Prediction Match}
\neq
\text{Strong Evidence}.
}
$$

---

# 3. 新版第一原則：結果情緒與資訊價值分離

$$
\boxed{
\text{Outcome Valence}
\neq
\text{Epistemic Information}.
}
$$

「成功」與「失敗」應先退回成：

$$
\boxed{
\text{Evidence Event Labels}.
}
$$

---

# 4. 理論空間

令：

$$
\boxed{
\Theta_t
=
\{T_1,T_2,\ldots,T_n\}.
}
$$

每個理論具有當前權重：

$$
q_t(T_i).
$$

且：

$$
\sum_iq_t(T_i)=1.
$$

---

# 5. 觀測事件

一個完整證據事件不只是一個數值 $d$。

本文定義：

$$
\boxed{
e_t
=
(
d_t,
s_t,
m_t,
q_t^{E},
r_t,
\tau_t
).
}
$$

其中：

- $d_t$：觀測內容；
- $s_t$：來源；
- $m_t$：測量／取得方法；
- $q_t^{E}$：證據品質；
- $r_t$：可重現與可靠性資訊；
- $\tau_t$：時間與版本。

---

# 6. 證據不是裸資料

所以：

$$
\boxed{
D_t
\neq
\{d_1,d_2,\ldots\}
}
$$

而更接近：

$$
\boxed{
D_t
=
\{e_1,e_2,\ldots,e_t\}.
}
$$

這是 Evidence Ledger。

---

# 7. 為什麼要保留 provenance？

因為未來可能發現：

$$
m_t
$$

有問題。

如果只保存結論：

> $d_t$ 是真的。

就無法回溯。

所以：

$$
\boxed{
\text{Evidence without Provenance}
\rightarrow
\text{Low Corrigibility}.
}
$$

---

# 8. 貝葉斯更新

在可機率化的模型空間中：

$$
\boxed{
q_{t+1}(T_i)
=
\frac{
P(d\mid T_i)q_t(T_i)
}{
\sum_jP(d\mid T_j)q_t(T_j)
}.
}
$$

這是 PDF 雙法統一的最小更新形式之一。

---

# 9. 成功與失敗在 Bayes 更新中沒有本體差別

如果：

$$
d
$$

支持：

$$
T_i,
$$

則：

$$
q_{t+1}(T_i)\uparrow.
$$

如果：

$$
d
$$

反對：

$$
T_i,
$$

則：

$$
q_{t+1}(T_i)\downarrow.
$$

兩者都只是：

$$
\boxed{
\text{Posterior Redistribution}.
}
$$

---

# 10. Bayes Factor 統一支持與反對

對兩個模型：

$$
T_i,T_j,
$$

定義：

$$
\boxed{
BF_{ij}(d)
=
\frac{P(d\mid T_i)}
{P(d\mid T_j)}.
}
$$

取對數：

$$
\boxed{
\Lambda_{ij}(d)
=
\log BF_{ij}(d).
}
$$

若：

$$
\Lambda_{ij}>0,
$$

資料偏向 $T_i$。

若：

$$
\Lambda_{ij}<0,
$$

資料偏向 $T_j$。

---

# 11. 所謂支持與否證只是符號方向

因此：

$$
\boxed{
\text{Support}
\leftrightarrow
+\Lambda
}
$$

與：

$$
\boxed{
\text{Contradiction}
\leftrightarrow
-\Lambda
}
$$

可視為同一比較量的兩側。

---

# 12. 這就是 PDF 雙法的第一個統一

成功法問：

> 新資料支持了什麼？

排除法問：

> 新資料削弱了什麼？

而數學上都可以是：

$$
\boxed{
\Delta q_t(T_i).
}
$$

---

# 13. 單次資訊量：Bayesian Surprise

本文採：

$$
\boxed{
\mathcal I_d
=
D_{\mathrm{KL}}
\left(
q_{t+1}
\Vert
q_t
\right)
}
$$

作為「單次觀測使理論分佈改變多少」的一個量。

由 KL divergence：

$$
\boxed{
\mathcal I_d\ge0.
}
$$

---

# 14. 零資訊事件

若：

$$
q_{t+1}=q_t,
$$

則：

$$
\boxed{
\mathcal I_d=0.
}
$$

表示該資料在目前模型與更新架構下沒有改變信念。

---

# 15. 高資訊事件

若觀測使：

$$
q_t
$$

大幅重排，

則：

$$
\mathcal I_d
$$

較高。

這可以是「成功」也可以是「失敗」。

---

# 16. 高資訊成功

例如原本：

$$
P(d\mid T_1)\ll1
$$

對其他模型也低，

但結果強烈符合 $T_k$ 的獨特預測，

則：

$$
q_{t+1}(T_k)\gg q_t(T_k).
$$

這是高資訊支持。

---

# 17. 高資訊失敗

若某主模型：

$$
T_1
$$

以高信心預測：

$$
d_1,
$$

但可靠觀測得到：

$$
d_2,
$$

且：

$$
P(d_2\mid T_1)\ll1,
$$

則它可能造成巨大權重重排。

這是高資訊反例。

---

# 18. 低資訊成功

若所有模型都預測：

$$
d,
$$

那麼：

$$
d
$$

發生幾乎沒有區分力。

所以：

$$
\boxed{
\text{Expected Success}
\neq
\text{High Information}.
}
$$

---

# 19. 低資訊失敗

如果儀器故障導致：

$$
d_{\mathrm{noise}},
$$

而沒有可靠 likelihood 可建模，

那麼這種「失敗」甚至不應直接更新理論。

---

# 20. 失敗首先要分類

新版將失敗拆成至少四類：

$$
\boxed{
F
=
\{
F_{\mathrm{theory}},
F_{\mathrm{measurement}},
F_{\mathrm{execution}},
F_{\mathrm{modelspace}}
\}.
}
$$

---

# 21. 理論失敗

$$
F_{\mathrm{theory}}
$$

指：

> 實驗與測量可信，但理論預測被可靠反例削弱。

這是排除法最典型對象。

---

# 22. 測量失敗

$$
F_{\mathrm{measurement}}
$$

指：

- 儀器錯誤；
- calibration 錯誤；
- 感測污染。

這時主要更新的是：

$$
m_t
$$

與證據品質，

而不必直接淘汰理論。

---

# 23. 執行失敗

$$
F_{\mathrm{execution}}
$$

指：

- 流程未完成；
- 程式 bug；
- 樣本處理錯誤；
- 操作條件失真。

其主要產出可能是：

$$
\boxed{
\text{methodological knowledge}.
}
$$

---

# 24. 模型空間失敗

最重要的新類型：

$$
\boxed{
F_{\mathrm{modelspace}}.
}
$$

它表示：

> 多個候選都反覆失敗，而且沒有任何既有模型能穩定解釋資料。

此時：

$$
\boxed{
T^*\notin\Theta_t
}
$$

的後驗可信度應提高。

---

# 25. 這時排除法必須停下來

不能繼續：

$$
\Theta_t
\rightarrow
\Theta_t\setminus\{T_i\}
$$

直到只剩一個「最不差」模型。

因為最後留下的模型也可能仍然錯。

---

# 26. 新版排除法的停止條件

若：

$$
\max_iP(d_{1:t}\mid T_i)
$$

長期極低，

或所有模型皆存在系統性殘差，

則觸發：

$$
\boxed{
\text{Reframe}(\Theta_t).
}
$$

---

# 27. 舊版熵下降命題的修正

對隨機變量：

$$
\Theta,D,
$$

有：

$$
\boxed{
H(\Theta\mid D)
\le
H(\Theta).
}
$$

這表示知道 $D$ 之後的**平均條件熵**不高於先驗熵。

---

# 28. 但單次 posterior entropy 可以上升

對某一具體：

$$
D=d,
$$

完全可能：

$$
\boxed{
H(\Theta\mid D=d)
>
H(\Theta).
}
$$

例如一個原本被高度偏好的模型遭到意外觀測削弱，使多個替代模型重新變得接近。

---

# 29. 這不是認識論倒退

熵上升可能代表：

> 我們發現自己以前過度自信。

因此：

$$
\boxed{
\text{Posterior Entropy Increase}
\neq
\text{Epistemic Failure}.
}
$$

有時它反而是校正。

---

# 30. 驚奇與熵變是不同量

$$
\boxed{
D_{\mathrm{KL}}(q_{t+1}\Vert q_t)
\ge0
}
$$

衡量分佈改變。

而：

$$
\Delta H
=
H(q_{t+1})-H(q_t)
$$

可以正、負或零。

兩者不能混用。

---

# 31. 這修正舊 PDF 排除法最重要的數學部分

舊直覺：

> 任何有效資料都讓理論空間熵下降。

新版：

> 有效資料通常使信念分佈發生可測改變；平均而言資料提供非負互資訊，但單次觀測可能提高或降低後驗熵。

---

# 32. 期望資訊量

對所有可能資料：

$$
\boxed{
\mathbb E_D
\left[
D_{\mathrm{KL}}
(
P(\Theta\mid D)
\Vert
P(\Theta)
)
\right]
=
I(\Theta;D)
\ge0.
}
$$

這才是較嚴格的「實驗具有平均資訊價值」形式。

---

# 33. 但資訊增益不等於真理增益

即使：

$$
I(\Theta;D)>0,
$$

若：

$$
T^*\notin\Theta,
$$

只是更精確地在錯誤模型裡重新分配概率。

所以：

$$
\boxed{
\text{Information Gain}
\neq
\text{Guaranteed Truth Gain}.
}
$$

---

# 34. 錯誤 likelihood 也會產生自信

如果：

$$
P(d\mid T)
$$

本身被錯誤指定，

Bayes 更新可以非常一致地：

$$
\boxed{
\text{become confidently wrong}.
}
$$

因此更新方法也必須可審計。

---

# 35. Evidence Ledger

本文正式定義：

$$
\boxed{
D_t
=
\{e_1,e_2,\ldots,e_t\}.
}
$$

它保存研究歷史。

理想上：

$$
D_{t+1}
\supseteq
D_t.
$$

但新增的也包括：

- 撤銷標記；
- 品質修訂；
- provenance 修正；
- replication 結果。

---

# 36. Evidence Ledger 的「單調」是紀錄單調，不是真理單調

所以：

$$
\boxed{
\text{Ledger Monotonicity}
\neq
\text{Belief Monotonicity}.
}
$$

---

# 37. Current Accepted Knowledge

$$
\boxed{
K_t
=
\text{currently accepted knowledge state}.
}
$$

它可以：

$$
K_{t+1}\supset K_t,
$$

也可以：

$$
K_{t+1}\subset K_t,
$$

甚至重構成：

$$
K_{t+1}\not\subseteq K_t
\land
K_t\not\subseteq K_{t+1}.
$$

---

# 38. 所以知識不是嚴格只增不減

新版修正為：

$$
\boxed{
\text{Knowledge Is Revisable},
}
$$

但：

$$
\boxed{
\text{Epistemic History Should Be Preserved}.
}
$$

---

# 39. 成功法真正保留的是什麼？

不是：

> 每次成功都增加永恆真理。

而是：

$$
\boxed{
\text{Inquiry Can Construct New Evidence, Methods, Representations, and Questions}.
}
$$

---

# 40. 建構性收益

本文定義：

$$
\boxed{
G_t^{+}
=
(
G_D,
G_M,
G_R,
G_Q,
G_T
).
}
$$

其中：

- $G_D$：新資料；
- $G_M$：新方法；
- $G_R$：新表徵；
- $G_Q$：新問題；
- $G_T$：新理論結構。

---

# 41. 即使主假設失敗，也可以有高建構收益

因此：

$$
\boxed{
F_{\mathrm{theory}}>0
}
$$

與：

$$
\boxed{
G_t^{+}>0
}
$$

可以同時成立。

這就是成功法與排除法真正的對偶。

---

# 42. 「成功」因此應有兩個維度

$$
\boxed{
S_t
=
(
S_{\mathrm{prediction}},
S_{\mathrm{construction}}
).
}
$$

第一個問：

> 預測有沒有命中？

第二個問：

> 研究有沒有生成新認知結構？

---

# 43. 預測失敗可以伴隨研究成功

例如：

$$
S_{\mathrm{prediction}}=0,
$$

但：

$$
S_{\mathrm{construction}}\gg0.
$$

這不是矛盾。

---

# 44. 排除法真正保留的是什麼？

不是：

> 失敗一定讓熵降低。

而是：

$$
\boxed{
\text{Reliable Contradiction Must Change the Epistemic State}.
}
$$

如果可靠反例完全不能改變模型，

系統就失去可修正性。

---

# 45. 反例的價值

令：

$$
c_t
$$

為高可信反例。

若：

$$
P(c_t\mid T_i)\ll1,
$$

則至少應觸發：

$$
\boxed{
q_{t+1}(T_i)<q_t(T_i)
}
$$

或：

$$
\boxed{
\text{Audit}(U_t,m_t,\Theta_t).
}
$$

---

# 46. 反例不必立即刪除理論

科學理論常含：

- 測量誤差；
- 邊界條件；
- 輔助假設。

所以新版不要求：

$$
c_t
\Rightarrow
T_i\text{ deleted}.
$$

而是：

$$
\boxed{
c_t
\Rightarrow
\text{Weight, Scope, or Structure Revision}.
}
$$

---

# 47. 淘汰是更新的一種，不是唯一一種

可能更新包括：

$$
\boxed{
\{
Reweight,
Restrict,
Modify,
Split,
Merge,
Archive,
Eliminate
\}.
}
$$

---

# 48. 這使 V 算子重新定義

舊版：

$$
V_\phi
:
\Theta_t
\rightarrow
\Theta_{t+1}\subseteq\Theta_t.
$$

新版：

$$
\boxed{
V
=
\text{Constraint/Selection Operator}.
}
$$

它可以：

- 降權；
- 限定適用域；
- 分裂模型；
- 暫時淘汰。

不再只等於刪除。

---

# 49. E 算子重新定義

舊版：

$$
E_\theta
:
P
\rightarrow
\Theta_0.
$$

新版：

$$
\boxed{
E
:
(
Q_t,D_t,K_t,F_t
)
\rightarrow
\Theta_{t+1}^{+}.
}
$$

展開可以在任何階段重新發生。

---

# 50. C 算子重新定義

連接算子：

$$
\boxed{
C
:
(
\Theta_t,e_t
)
\rightarrow
\text{comparative evidence structure}.
}
$$

其工作是：

- 對接預測；
- 建立 likelihood；
- 計算區分力；
- 更新權重；
- 記錄衝突。

---

# 51. 新版三元循環

因此：

$$
\boxed{
E
\rightarrow
C
\rightarrow
V
}
$$

仍然保留，

但：

$$
\boxed{
V
\not\Rightarrow
\text{Final Closure}.
}
$$

而是：

$$
\boxed{
V
\rightarrow
E'
}
$$

可以再次展開。

---

# 52. 這就是螺旋而不是一次性篩選

$$
\boxed{
E_t
\rightarrow
C_t
\rightarrow
V_t
\rightarrow
E_{t+1}
\rightarrow
C_{t+1}
\rightarrow
V_{t+1}.
}
$$

---

# 53. 但新版比舊螺旋更多一層

因為：

$$
E_{t+1}
$$

不只是重新產生類似模型。

它可以改變：

$$
\boxed{
\Theta,
Q,
Ontology,
U.
}
$$

---

# 54. PDF 雙法的真正統一對象是 Epistemic State

所以不再分別說：

> 成功法更新知識。

> 排除法更新理論。

而是：

$$
\boxed{
e_t
\rightarrow
\Delta\mathcal E_t.
}
$$

---

# 55. 認知狀態

本文採：

$$
\boxed{
\mathcal E_t
=
(
\Theta_t,
D_t,
K_t,
F_t,
U_t
).
}
$$

Paper 01 的主理論 $T_t$ 可以視為：

$$
T_t
=
\operatorname{Select}(\Theta_t,q_t)
$$

的當前工作模型。

---

# 56. 成功與失敗共同更新五個地方

一個證據事件可能改變：

1. $\Theta_t$：候選集合；
2. $D_t$：證據帳本；
3. $K_t$：接受知識；
4. $F_t$：反例與失敗；
5. $U_t$：更新方法。

---

# 57. 同一事件可以同時「成功」又「失敗」

例如：

- 實驗流程成功；
- 主假設失敗；
- 方法學成功；
- 新理論空間生成成功。

所以：

$$
\boxed{
\text{Success/Failure}
}
$$

不是二值全局標籤。

---

# 58. 新版採多軸結果向量

本文提出：

$$
\boxed{
\mathbf O_t
=
(
O_{\mathrm{exec}},
O_{\mathrm{pred}},
O_{\mathrm{disc}},
O_{\mathrm{construct}},
O_{\mathrm{reframe}}
).
}
$$

其中：

- 執行結果；
- 預測結果；
- 區分力；
- 建構收益；
- 重構收益。

---

# 59. 「全部失敗」其實常是語義壓縮過度

如果：

$$
O_{\mathrm{pred}}=0
$$

但其他維度很高，

說：

> 這次完全失敗。

會丟失大量認識論資訊。

---

# 60. 研究管理也應改變

傳統 KPI 只問：

> 成功率多少？

新版至少還應問：

- 產生多少高品質反例？
- 排除了哪些區域？
- 是否新增方法？
- 是否發現模型空間不足？
- 是否減少未來重複錯誤？

---

# 61. 但不能反過來把所有失敗包裝成成功

這是重要防線。

如果沒有：

$$
\Delta\mathcal E_t
$$

或可驗證的：

$$
G_t^{+},
$$

就不能說：

> 失敗也是成功。

所以：

$$
\boxed{
\text{Epistemic Reframing}
\neq
\text{Failure Rationalization}.
}
$$

---

# 62. 防止自我安慰

本文要求每次「失敗有價值」都回答：

1. 新增了什麼證據？
2. 改變了什麼模型權重？
3. 排除了什麼區域？
4. 新增了什麼方法？
5. 下一輪因此會做什麼不同？

若全部答不出：

$$
\boxed{
X_{\mathrm{err}}\approx0.
}
$$

---

# 63. 成功也需要相同審查

每次「成功」都應回答：

1. 是否可重現？
2. 是否區分替代理論？
3. 是否存在 leakage？
4. 是否有獨立證據？
5. 成功是否只在當前 benchmark？

---

# 64. 成功與失敗因此獲得對稱紀律

$$
\boxed{
\text{Success Audit}
\leftrightarrow
\text{Failure Audit}.
}
$$

這才是真正 PDF 對偶。

---

# 65. 舊版「資訊守恆律」的修正

舊原型曾提出類似：

$$
H(\Theta)+S(\Sigma)=\text{const}.
$$

本文不再把它視為一般資訊論定律。

除非另行定義封閉編碼系統與守恆條件，

否則：

$$
\boxed{
H(\Theta)+S(\Sigma)
=
\text{const}
}
$$

只能保留為啟發式直覺，而非普遍定理。

---

# 66. 更保守的新版關係

可以說：

$$
\boxed{
\text{Theory Uncertainty Reduction}
}
$$

常伴隨：

$$
\boxed{
\text{Evidence/Representation Structure Growth},
}
$$

但兩者不要求嚴格守恆。

---

# 67. 為什麼要修掉它？

因為知識系統是開放系統。

研究可以引入：

- 新資料；
- 新變量；
- 新語言；
- 新模型空間。

所以總表示複雜度可以增加，也可以因壓縮而下降。

---

# 68. 開放認識論不能假設固定總資訊量

因此：

$$
\boxed{
\text{Epistemic System}
\neq
\text{Closed Information Box}.
}
$$

這與 Paper 01 的 Open-World Epistemology 一致。

---

# 69. 新版 PDF 雙法的最小定律

本文保留三條較穩健命題。

第一：

$$
\boxed{
\text{Reliable Evidence Should Be Allowed to Modify the Epistemic State}.
}
$$

第二：

$$
\boxed{
\text{Constructive Inquiry Can Produce Value Even When a Hypothesis Fails}.
}
$$

第三：

$$
\boxed{
\text{Neither Success nor Failure Guarantees Truth Without Model and Evidence Audit}.
}
$$

---

# 70. 雙重資訊原理

本文正式提出：

$$
\boxed{
\text{Dual Information Principle}.
}
$$

定義：

> 一個研究事件的認識論價值，同時來自它對候選模型的區分作用，以及它對證據、方法、問題、表示與失敗地圖的建構作用。

形式上：

$$
\boxed{
\mathcal V(e_t)
=
\alpha
\mathcal I_t^{\mathrm{disc}}
+
\beta
\mathcal G_t^{\mathrm{construct}}
-
\gamma
\mathcal R_t^{\mathrm{error}}.
}
$$

---

# 71. 三個分量

其中：

$$
\mathcal I_t^{\mathrm{disc}}
$$

為模型區分資訊；

$$
\mathcal G_t^{\mathrm{construct}}
$$

為建構性收益；

$$
\mathcal R_t^{\mathrm{error}}
$$

為資料、方法與模型錯置風險。

---

# 72. 這不是精確通用量表

 $\alpha,\beta,\gamma$ 依研究領域、風險與目的不同。

所以該式是：

$$
\boxed{
\text{conceptual evaluation functional},
}
$$

不是宣稱所有研究都能壓成單一分數。

---

# 73. PDF Formation 的新版定義

$$
\boxed{
PDF_F
=
\text{Proof by Data Formation}
}
$$

不再理解成「成功證明真理」。

而是：

> 透過研究過程形成新的可檢查證據、方法、表徵、問題與候選理論。

---

# 74. PDF Falsification 的新版定義

$$
\boxed{
PDF_X
=
\text{Proof by Data Falsification}
}
$$

不再理解成「一次失敗就刪除理論」。

而是：

> 透過可靠反例、比較與約束，使某些理論、參數、適用域或模型空間結構降低可信度或被重新建模。

---

# 75. 兩者的共同底層

$$
\boxed{
PDF_F
\cup
PDF_X
\subset
\text{Corrigible Evidence Updating}.
}
$$

---

# 76. 成功法與排除法不是兩個互斥流程

一次實驗可以同時：

$$
\boxed{
PDF_F>0
}
$$

與：

$$
\boxed{
PDF_X>0.
}
$$

例如否定舊模型，同時產生新現象規律與新測量方法。

---

# 77. 真正成熟的研究心態

不是：

> 我要成功。

也不是：

> 我要失敗來排除。

而是：

$$
\boxed{
\text{I want the next experiment to maximally improve the epistemic state under acceptable cost and risk}.
}
$$

---

# 78. 實驗設計因此改變

理想實驗不是只最大化：

$$
P(\text{success}).
$$

而可考慮：

$$
\boxed{
\mathbb E[
\mathcal V(e)
]
-
\text{Cost}
-
\text{Risk}.
}
$$

---

# 79. 高區分力比高成功率更重要

一個只有 20% 機率支持主假設，

但無論結果如何都能強烈區分模型的實驗，

可能比 95% 會「成功」但幾乎沒有區分力的實驗更有認識論價值。

---

# 80. 這就是雙法統一後的策略轉換

從：

$$
\boxed{
\text{Seek Success}
}
$$

轉成：

$$
\boxed{
\text{Seek Informative Outcomes}.
}
$$

---

# 81. 結論：成功與失敗都不是終點，它們只是認知狀態的更新方向

舊成功法讓我們看到：

> 即使理論錯了，研究仍可能生成資料、方法與知識。

舊排除法讓我們看到：

> 反例不是恥辱，而是理論空間的重要約束。

新版進一步修正：

$$
\boxed{
\text{Success}
\not\Rightarrow
\text{Truth},
}
$$

$$
\boxed{
\text{Failure}
\not\Rightarrow
\text{Progress}.
}
$$

真正需要問的是：

$$
\boxed{
\Delta\mathcal E_t
=
?
}
$$

也就是：

> 這次研究究竟讓整個認知狀態改變了什麼？

因此：

$$
\boxed{
\text{Success}
+
\text{Failure}
\rightarrow
\text{Evidence Events}
\rightarrow
\text{Epistemic State Update}.
}
$$

在機率化模型中，單次證據可用：

$$
\boxed{
D_{\mathrm{KL}}
(
q_{t+1}
\Vert
q_t
)
}
$$

描述信念重排幅度；

平均資訊則由：

$$
\boxed{
I(\Theta;D)\ge0
}
$$

描述。

但：

$$
\boxed{
\text{Information Gain}
\neq
\text{Guaranteed Truth Gain}.
}
$$

因為模型空間、likelihood、資料與更新器本身都可能錯。

所以 PDF 雙法真正成熟的形式不再是：

$$
\text{Success vs Failure}.
$$

而是：

$$
\boxed{
\text{Construction}
+
\text{Discrimination}
+
\text{Revision}.
}
$$

最終：

$$
\boxed{
\text{Good inquiry is not inquiry that succeeds; it is inquiry that leaves the epistemic system better able to distinguish, revise, and regenerate models}.
}
$$

中文：

> **好的研究，不是每次都得到預期答案；而是每次結束後，認知系統都更知道哪些可能性值得保留、哪些必須降低權重、哪些證據值得信任，以及何時需要重新打開整個模型空間。**

---

## 核心命題摘要

### 命題一：結果情緒不等於資訊價值

$$
\boxed{
\text{Outcome Valence}
\neq
\text{Epistemic Information}.
}
$$

### 命題二：成功與失敗都是證據事件

$$
\boxed{
\text{Success/Failure}
\subset
\text{Evidence Events}.
}
$$

### 命題三：單次信念重排可由 Bayesian Surprise 描述

$$
\boxed{
\mathcal I_d
=
D_{\mathrm{KL}}
(q_{t+1}\Vert q_t)
\ge0.
}
$$

### 命題四：平均資訊由互資訊刻畫

$$
\boxed{
\mathbb E_D[\mathcal I_D]
=
I(\Theta;D)
\ge0.
}
$$

### 命題五：單次 posterior entropy 不保證下降

$$
\boxed{
H(\Theta\mid D=d)
\gtrless
H(\Theta)
}
$$

皆可能。

### 命題六：資訊增益不保證真理增益

$$
\boxed{
\text{Information Gain}
\neq
\text{Guaranteed Truth Gain}.
}
$$

### 命題七：證據歷史與接受知識必須分離

$$
\boxed{
D_t
\neq
K_t.
}
$$

### 命題八：失敗需要分類

$$
\boxed{
F
=
\{
F_{\mathrm{theory}},
F_{\mathrm{measurement}},
F_{\mathrm{execution}},
F_{\mathrm{modelspace}}
\}.
}
$$

### 命題九：成功法與排除法共同更新認知狀態

$$
\boxed{
PDF_F
\cup
PDF_X
\subset
\text{Corrigible Evidence Updating}.
}
$$

### 命題十：研究目標應從成功率轉向資訊性

$$
\boxed{
\text{Seek Success}
\rightarrow
\text{Seek Informative Outcomes}.
}
$$

---

## 系列接口

Paper 01 建立：

$$
\boxed{
\text{Infallibility}
\neq
\text{Corrigibility}.
}
$$

Paper 02 則正式把舊 PDF 成功法與排除法整合成新版雙重資訊理論：

$$
\boxed{
\text{Construction}
+
\text{Discrimination}
+
\text{Revision}.
}
$$

下一篇：

**Paper 03：《當真理不在候選集合裡：開放模型空間與認識論重置》**

將專門處理：

$$
\boxed{
T^*
\notin
\Theta_t.
}
$$

以及：

$$
\boxed{
\Theta_{t+1}
\not\subseteq
\Theta_t.
}
$$

也就是：

> **當整個候選世界都錯了，認知系統如何知道自己該停止排除、改寫問題、換座標、換本體，重新生成一個以前不存在的模型空間？**
