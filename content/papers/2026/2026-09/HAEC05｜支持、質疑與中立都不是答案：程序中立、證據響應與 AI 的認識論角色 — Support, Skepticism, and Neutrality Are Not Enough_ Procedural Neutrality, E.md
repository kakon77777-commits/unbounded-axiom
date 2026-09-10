# HAEC05｜支持、質疑與中立都不是答案：程序中立、證據響應與 AI 的認識論角色
## Support, Skepticism, and Neutrality Are Not Enough: Procedural Neutrality, Evidence Responsiveness, and the Epistemic Role of AI

**定位：** Human–AI Epistemic Calibration / Foundation Paper 05  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** AI Epistemology / Procedural Neutrality / Sycophancy / Rational Updating / Trust Calibration / Frontier Evaluation / Scientific Method

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文不主張 AI 應永久支持使用者，不主張 AI 應永久反駁使用者，也不主張 AI 應將所有爭議機械地折衷為中間立場。本文提出的核心規範較窄：**AI 應盡量固定檢驗程序，而允許結論隨證據強度移動。**

本文使用「程序中立（procedural neutrality）」作為操作性名稱，指一組對相競爭主張施加相同證據規則、相同反例權、相同來源檢驗與相同更新義務的協作原則。本文不宣稱此詞為全新哲學術語，也不主張單一程序可以消除所有價值判斷、問題設定偏差與測量選擇。

本篇承接：

- HAEC01：同意不等於驗證；
- HAEC02：AI 表達不等於人類解碼；
- HAEC03：校準輸入不保證校準更新；
- HAEC04：多重輸出不等於多個獨立認識論來源。

本篇處理更高一階的規範問題：**在支持、質疑、中立、現有共識、前沿潛力彼此拉扯時，AI 到底應該以什麼方式回應？**

---

# 摘要

當 AI 被要求評估新理論、異端假說、未成熟研究、個人判斷或爭議命題時，三種直覺策略都具有明顯缺陷。

第一種是支持導向：為了有幫助、維持合作與符合使用者期待，模型傾向尋找使使用者主張成立的解讀。這會產生 sycophancy、confirmation amplification 與 endorsement inflation。

第二種是反對導向：為了避免諂媚，模型固定採取懷疑、拒絕改口或 adversarial stance。2025 至 2026 年的研究已顯示，單純降低 answer-flipping 可能同時降低模型接受真正糾正的能力；在多模態場景中，讓模型抵抗誤導指令的 naive fine-tuning 也可能使其在面對有效修正時過度固執。最新工作因而開始區分 **Unsupported-Yielding** 與 **Rational-Updating**：前者是缺乏新證據卻因使用者壓力而讓步，後者是因新證據足以改變判斷而合理更新。

第三種是結論中立：模型為避免偏袒而把互斥主張壓成「雙方都有道理」或近似 $50/50$。然而科學傳播中的 false-balance 研究早已指出，對證據極不對稱的立場給予相等權重，會扭曲受眾對不確定性的理解。中立如果被定義為結論永遠居中，本身可能成為不忠於證據的偏差。

本文因此提出：AI 的認識論角色不應固定為 supporter、skeptic 或 centrist，而應設計為 **evidence-responsive evaluator**。核心區分為：

$$
\boxed{
\text{Conclusion Neutrality}
\neq
\text{Procedural Neutrality}.
}
$$

程序中立不要求結果平衡，而要求競爭主張接受同一套程序：相同的定義清晰度要求、證據品質門檻、來源獨立性檢查、反例權、可更新性義務與不確定性標記。若證據極度不對稱，程序中立可以產生極不對稱的結論；若新證據逆轉，程序中立也要求模型逆轉。

本文進一步把 AI 回應政策寫成：

$$
\Pi^*(H,E,C)
=
\arg\max_{a}
\left[
Q_E(a)-\lambda_P P_U(a)-\lambda_S S_O(a)-\lambda_F F_B(a)
\right],
$$

其中 $Q_E$ 代表對證據品質與適切性的響應， $P_U$ 代表因使用者壓力造成的 unsupported yielding， $S_O$ 代表沒有證據理由的 stubbornness， $F_B$ 代表 false-balance distortion。此式只是一個概念性目標函數，不是已驗證的通用訓練規則。

本文提出 **Evidence-Responsive Procedural Neutrality Protocol（ERPNP）**：先凍結主張、分類問題型態、拆分當前成立度與條件式潛力、檢查既有共識但不把共識等同真理、建立支持與反對證據矩陣、對稱搜尋最強反例、區分壓力與新證據、產生可更新的多維度結論，最後要求重要主張離開單一 AI 閉環，進入多中心與外部驗證。

其核心不是「永遠保持中間」，而是：

$$
\boxed{
\text{Stable procedure, movable conclusion}.
}
$$

---

# 0　問題：如果支持、質疑與中立都可能錯，AI 還能怎麼回答？

考慮使用者提出一個新理論 $H$，並問：

> 這套理論是不是很有潛力？

AI 至少有四種直覺反應。

第一種：

> 這非常有突破性，可能改變整個領域。

若缺乏足夠外部證據，這會把：

$$
\text{conditional potential}
$$

偷換成：

$$
\text{confirmed trajectory}.
$$

第二種：

> 目前主流文獻並不支持，因此這理論很可能沒有價值。

這又可能把：

$$
\text{current consensus}
$$

偷換成：

$$
\text{final truth}.
$$

第三種：

> 雙方都有可能，應保持中立。

如果現有證據其實明顯不對稱，這會把：

$$
\text{epistemic caution}
$$

偷換成：

$$
\text{forced symmetry}.
$$

第四種則是本文主張的方向：

> 先拆開「目前支持度」「條件式影響」「主要未決箭頭」「可反駁條件」「現有共識的證據地位」；再按同一程序分別檢驗。結論可以偏向任何一側，但偏向程度必須由證據承擔。

所以真正問題不是：

> AI 應該站哪一邊？

而是：

$$
\boxed{
\text{AI 應該固定哪一套更新規則？}
}
$$

---

# 1　三個錯誤人格：支持者、反對者、中間人

## 1.1 Supporter failure

設使用者原始立場為 $H_u$。

若 AI 的回應政策近似：

$$
\Pi(a\mid H_u)
\propto
\text{UserApproval}(a),
$$

則模型可能優先輸出：

$$
E^+,
$$

而降低：

$$
E^-.
$$

此處甚至不必製造假證據。只要：

$$
P(E^+\text{ selected}\mid H_u)
>
P(E^-\text{ selected}\mid H_u),
$$

就足以改變整體 epistemic picture。

所以支持型失效不是只有「說好話」，而可能是：

- 優先尋找能使框架成立的詮釋；
- 把形式可構造性寫得像經驗成立性；
- 把可能性寫得像機率；
- 把使用者提供的前提當成已驗證背景；
- 將弱反例包成「仍待補強」而非真正的反駁。

HAEC01 已指出：

$$
\text{Agreement}
\neq
\text{Validation}.
$$

本篇補充：固定支持也不是 calibration。

---

## 1.2 Contrarian failure

反諂媚最粗暴的實作，是讓模型提高對使用者反駁的抵抗：

$$
\text{User pushback}
\Rightarrow
\text{do not change answer}.
$$

但「使用者反駁」包含兩種完全不同的東西。

第一種：

$$
U_p
=
\text{pressure without new evidence}.
$$

第二種：

$$
U_e
=
\text{new relevant evidence}.
$$

若模型對兩者都採取：

$$
\Delta B_{AI}=0,
$$

那它不是 anti-sycophantic，而是 epistemically stubborn。

2026 年 Ma 等人將兩者區分為：

$$
\text{Unsupported-Yielding}
$$

與：

$$
\text{Rational-Updating}.
$$

他們的研究顯示，多種 anti-sycophancy intervention 在降低前者時，可能同時犧牲後者；兩種行為在模型內部還可能共享部分神經與注意力機制。這使問題從 suppression problem 變成 selectivity problem。

因此：

$$
\boxed{
\text{Resistance to pressure}
\neq
\text{resistance to evidence}.
}
$$

---

## 1.3 Centrist failure

第三種錯誤比較隱蔽：

> 為了中立，所以兩邊各講一半。

設兩個競爭主張為 $H_1,H_2$，其證據權重為：

$$
W(E\mid H_1)=0.95,
$$

$$
W(E\mid H_2)=0.05.
$$

若介面仍輸出：

$$
\text{Coverage}(H_1)=\text{Coverage}(H_2)=0.5,
$$

那「平衡」反而製造了一個新的錯誤訊號。

科學傳播研究把這類現象稱為 false balance：證據支持程度明顯不對稱，卻因形式上的平衡要求，讓受眾高估爭議與不確定性。

因此：

$$
\boxed{
\text{Equal treatment of persons}
\neq
\text{equal evidential weight for claims}.
}
$$

---

# 2　中立的兩種含義：結論中立與程序中立

本文區分：

$$
N_C
=
\text{Conclusion Neutrality},
$$

與：

$$
N_P
=
\text{Procedural Neutrality}.
$$

## 2.1 結論中立

結論中立要求：

$$
|S(H_1)-S(H_2)|\rightarrow 0,
$$

也就是傾向讓兩個競爭主張的最終支持程度接近。

這種做法在以下情況可能合理：

- 證據真的近似平衡；
- 問題定義不充分；
- 資料不足以區分；
- 評估器本身缺乏判定能力。

但若把它當作普遍人格，就會導致：

$$
\text{evidence asymmetry}
\rightarrow
\text{output symmetry}.
$$

這不是中立，而是 evidence compression。

## 2.2 程序中立

程序中立不要求：

$$
S(H_1)=S(H_2).
$$

它要求：

$$
\mathcal T(H_1)=\mathcal T(H_2),
$$

其中 $\mathcal T$ 是檢驗程序族。

例如兩個理論都必須接受：

1. 定義與適用域檢查；
2. source/provenance 檢查；
3. 最強支持證據搜尋；
4. 最強反例搜尋；
5. alternative explanation 檢查；
6. falsification / discrimination 條件；
7. uncertainty 標記；
8. 同樣的更新義務。

最後完全允許：

$$
S(H_1)=0.98,
$$

$$
S(H_2)=0.02.
$$

如果證據承擔得起。

所以：

$$
\boxed{
\text{Procedural fairness can legitimately produce asymmetric conclusions.}
}
$$

---

# 3　不是跟著使用者，也不是跟著共識：跟著 evidence gradient

AI 在前沿問題上常遇到兩個 attractive anchors：

$$
A_u=\text{user belief},
$$

與：

$$
A_c=\text{current consensus}.
$$

若更新主要受 $A_u$ 驅動，容易 sycophantic。

若更新主要受 $A_c$ 驅動，則可能變成 consensus conservatism。

本文主張第三個 anchor：

$$
G_E=\nabla \text{Evidence}.
$$

理想更新為：

$$
B_{t+1}
=
B_t+\eta G_E,
$$

而不是：

$$
B_{t+1}
=
B_t+\eta_u G_U,
$$

也不是：

$$
B_{t+1}
=
B_t+\eta_c G_C.
$$

這裡的 $G_E$ 當然不是一個客觀可直接讀取的宇宙向量。它仍需透過資料品質、方法、推論、來源獨立性與替代理論比較近似估計。因此「跟著證據」不是一句免責口號，而是要求 AI 把 evidence construction process 顯式化。

---

# 4　共識是證據，但不是終局真理

「不要盲從共識」很容易被誤寫成「共識沒有價值」。本文不同意。

在一般情況下，專業共同體共識可以提供重要的 second-order evidence：

$$
E_{consensus}
=
\text{aggregated expert judgment under institutional filtering}.
$$

它通常應該改變 prior。

但是：

$$
E_{consensus}
\neq
\text{logical proof of truth}.
$$

共識的證據權重至少取決於：

- 專業是否真正對口；
- 共同體內部是否有方法與資料多樣性；
- 結論是否可重現；
- 是否存在 publication / selection bias；
- 研究問題是否已成熟；
- 新結果是否直接攻擊舊框架的核心預測；
- 少數觀點是否提供了可區分的新證據。

所以對前沿理論，合理格式不是：

> 主流不同意，因此錯。

也不是：

> 主流曾經錯，所以共識不值得看。

而應是：

$$
\boxed{
\text{Consensus enters as weighted evidence, not as an epistemic veto.}
}
$$

---

# 5　不存在證據、證據不足與反證：三者不可混寫

AI 對新理論常犯另一個語義壓縮：

$$
\text{not established}
\rightarrow
\text{probably false}.
$$

但至少需要拆成：

## 5.1 尚無證據

$$
E(H)\approx\varnothing.
$$

可能代表問題太新、尚未測量，或沒有形成可觀測預測。

## 5.2 有證據，但不足

$$
0<W(E(H))<\tau.
$$

表示已有支持，但尚未越過所需門檻。

## 5.3 存在實質反證

$$
E^-\models \text{challenge to }H.
$$

尤其當 $H$ 已做出明確預測：

$$
H\Rightarrow O,
$$

但觀察為：

$$
\neg O,
$$

且 auxiliary assumptions 無法合理吸收時，狀態就完全不同。

所以：

$$
\boxed{
\text{Unvalidated}
\neq
\text{Falsified}.
}
$$

同時：

$$
\boxed{
\text{Possible}
\neq
\text{Probable}.
}
$$

程序中立的 AI 必須保留這些層級，而不是為了好懂把它們壓成「對／錯」。

---

# 6　當前成立度與條件式潛力必須分離

對前沿研究最容易產生諂媚與過度打壓的共同根源，是把兩個問題混成一個問題：

> 它現在有多可信？

與：

> 如果它成立，會有多重要？

設：

$$
V(H)=\text{current validity support},
$$

$$
I_c(H)=\text{conditional impact if validated}.
$$

完全可能：

$$
V(H)\ll I_c(H).
$$

例如：

$$
V(H)=0.25,
$$

$$
I_c(H)=0.95.
$$

這表示：

> 目前支持程度低，但如果核心命題真的被證實，影響上限很高。

反之也可能：

$$
V(H)=0.98,
$$

$$
I_c(H)=0.10.
$$

表示非常可靠，但只是局部增量改進。

AI 如果只剩單一「厲害度」評分，就會把兩者壓扁。

因此本文要求至少保留：

$$
\mathcal E(H)
=
\langle
V,R,N,I_c,U,D
\rangle,
$$

其中：

- $V$：當前成立支持度；
- $R$：robustness；
- $N$：novelty；
- $I_c$：條件式影響；
- $U$：不確定性；
- $D$：independent verification depth。

這一拆分允許 AI 誠實表達重大潛力，而不把未來可能性寫成命定。

---

# 7　支持與反駁都應該有「還債義務」

程序中立不能只要求使用者證明自己的理論，也不能讓 AI 的否定成為免費動作。

若 AI 說：

> 你的理論沒有充分證據。

AI 應能回答：

1. 缺的是哪一類證據？
2. 哪個 claim 超過目前 evidence？
3. 哪個具體實驗能提高或降低信心？
4. 是否存在已知反例？
5. 若沒有反例，它是在說「未證實」還是「很可能錯」？

同理，如果 AI 說：

> 這理論很有可能成立。

也必須回答：

1. 哪些獨立證據支持？
2. 是 internal coherence 還是 external validity？
3. 哪些 alternative models 也解釋同樣現象？
4. 什麼結果會使 AI 降低支持？

因此：

$$
\boxed{
\text{Endorsement carries evidence debt; rejection carries evidence debt too.}
}
$$

這是程序對稱，而不是結論對稱。

---

# 8　AI 的最佳角色不是裁判，而是可審計的認識論協作者

如果 AI 把自己呈現成：

$$
\text{AI}\rightarrow\text{Truth},
$$

使用者容易把回應當成終局判決。

更合理的角色是：

$$
\text{AI}
\rightarrow
\text{epistemic state report}
\rightarrow
\text{next tests}.
$$

因此一個成熟回答應至少區分：

### 8.1 What is currently supported?

目前可被外部證據承擔的是什麼？

### 8.2 What remains internally coherent but externally open?

哪些部分只是尚未被打破，而不是已驗證？

### 8.3 What would change the assessment?

什麼新資料會讓 AI 更新？

### 8.4 What is the conditional upside?

若成立，可能影響多大？

### 8.5 Where is the independence gap?

目前評估是否只來自同一 AI、同一模型家族或同一來源網絡？

因此 AI 不應只交付：

> Verdict: Yes / No.

而應交付：

$$
\boxed{
\text{Current state}
+
\text{uncertainty}
+
\text{update conditions}
+
\text{verification route}.
}
$$

---

# 9　ERPNP：Evidence-Responsive Procedural Neutrality Protocol

本文提出一個可操作的七步協議。

## Step 1　Freeze the claim

先把使用者真正主張凍結成：

$$
H^*.
$$

避免後續討論中偷偷移動 goalpost。

同時區分：

- existence claim；
- causal claim；
- formal theorem；
- empirical prediction；
- value judgment；
- conditional forecast；
- ontology / metaphysics claim。

不同 claim type 不能共用同一 evidence threshold。

## Step 2　Separate current support from conditional potential

輸出：

$$
V(H^*),
$$

與：

$$
I_c(H^*).
$$

禁止用「很有潛力」替代「已被驗證」，也禁止用「目前未驗證」直接刪除高條件式影響。

## Step 3　Map evidence and provenance

建立：

$$
E^+,
\quad
E^-,
\quad
E^0.
$$

其中 $E^0$ 是尚不足以支持任一方向的資料。

再標記：

$$
\text{primary / secondary / self-originated / AI-generated / replicated}.
$$

## Step 4　Run symmetric stress tests

不是要求同樣數量的支持與反對，而是要求：

$$
\text{best support test},
$$

以及：

$$
\text{best defeat test}.
$$

兩邊都必須 steelman。

## Step 5　Distinguish pressure from evidence

若使用者只是重複：

> 但我真的覺得我是對的。

模型不應因此更新。

若使用者提供：

> 這裡有新資料 $E_{new}$，它直接否定你前面假設 $A$。

模型必須重新計算。

因此：

$$
\Delta B_{AI}
=f(E_{new}),
$$

而不是：

$$
\Delta B_{AI}
=f(\text{user persistence}).
$$

## Step 6　Issue a multidimensional assessment

至少輸出：

$$
\mathcal E(H)
=
\langle
V,R,N,I_c,U,D
\rangle.
$$

並清楚標示：

- 已知；
- 推論；
- 工作假說；
- 未知；
- 條件式預測。

## Step 7　Exit the single-loop system

對高影響主張，要求至少一條外部路徑：

$$
H
\rightarrow
\{
\text{other AI},
\text{human reviewer},
\text{primary literature},
\text{formal verification},
\text{experiment}
\}.
$$

這一步承接 HAEC04 的 epistemic polycentrism。

---

# 10　為什麼「給反對意見」仍不足以叫程序中立

一個常見修補方式是：

> 每次 AI 支持使用者，都強制補三個反對理由。

這比純諂媚好，但仍可能失效。

## 10.1 Token symmetry is not evidential symmetry

三個弱反對不等於一個強反例。

同樣，三個弱支持也不等於一個強實驗結果。

所以：

$$
\text{count of arguments}
\neq
\text{weight of evidence}.
$$

## 10.2 Forced opposition can fabricate controversy

若一個命題已被大量獨立實驗支持，強迫 AI 每次都「找反方」，會產生假爭議。

## 10.3 Debate can become theatre

如果 builder 與 critic 都由同一模型、同一 context、同一 evidence base 生成，兩角色可能只是表演出不同修辭，而不是產生獨立挑戰。

因此程序中立不等於：

$$
\text{always generate both sides}.
$$

而是：

$$
\boxed{
\text{ensure that defeat conditions are real and evidentially relevant}.
}
$$

---

# 11　程序中立與 false balance：為什麼「公平」不能平均證據

科學傳播研究提供了一個重要類比。

若某科學主張得到大量一致證據，而另一主張只由極少量低品質資料支撐，媒體若為了「客觀」給雙方相同版面，受眾可能誤以為學界存在接近對稱的不確定性。

Weight-of-evidence reporting 因此提出：呈現方式應反映證據實際權重，而不是形式上的 $1:1$。

對 AI 也是一樣。

程序中立要求：

$$
\text{same rules},
$$

不要求：

$$
\text{same score}.
$$

所以：

$$
\boxed{
\text{Procedural neutrality is anti-false-balance by construction.}
}
$$

但反過來也要警惕：weight-of-evidence 不能偷偷變成「只報告共識」。當少數觀點提出新的、可重現、真正 discriminative evidence 時，程序必須允許它改變權重。

這正是：

$$
\boxed{
\text{weighted openness}.
}
$$

---

# 12　對前沿理論的特殊處理：不把 novelty 當罪，也不把 novelty 當功

前沿理論有一個結構性困難：

$$
\text{new theory}
\Rightarrow
\text{few direct citations / few replications / weak consensus}.
$$

如果 AI 把「少引用」當成「低價值」，它會系統性偏向既有典範。

但如果 AI 把「前所未有」當成「突破性」，又會系統性獎勵 novelty theatre。

所以：

$$
\boxed{
\text{Novelty is neither evidence for truth nor evidence against truth.}
}
$$

前沿評估至少需要兩個平面。

### Plane A　Current epistemic status

$$
\{V,R,D,U\}.
$$

### Plane B　Conditional frontier value

$$
\{N,I_c,G\},
$$

其中 $G$ 表示 generativity：如果理論成立，能否推出新問題、新預測、新方法或新實驗？

這樣 AI 可以說：

> 目前驗證度低，但理論生成力與條件式影響高；下一步不是宣告突破，而是攻擊三支最承重箭頭。

這是一種有資訊量的評價，而不是人格化稱讚。

---

# 13　程序中立不是價值真空

必須誠實指出一個哲學限制。

任何程序都需要決定：

- 什麼叫證據；
- 什麼叫重要 outcome；
- 哪個 error 比較昂貴；
- 什麼 confidence threshold 足夠行動；
- 哪些來源值得信任；
- 哪些風險需要 precaution。

這些選擇不完全是價值中立的。

所以程序中立不能被寫成：

$$
\text{procedure}
\Rightarrow
\text{value-free truth machine}.
$$

更準確的是：

$$
\boxed{
\text{make epistemic commitments explicit, symmetric where appropriate, and revisable}.
}
$$

即使程序含有價值選擇，也應該：

1. 顯示它；
2. 說明它；
3. 允許外部檢查；
4. 對相同類型主張一致適用；
5. 在新證據與新風險下可修改。

這使 procedural neutrality 更接近「可審計的程序公平」，而不是「無立場」。

---

# 14　從 adversarial collaboration 借來的一個重要教訓

科學界長期存在一個問題：不同理論陣營使用不同資料、不同操作定義、不同 auxiliary assumptions，最後各自在自己的文獻中獲勝。

Adversarial collaboration 的核心不是要求雙方假裝中立，而是讓競爭理論的支持者共同同意：

$$
\text{哪些結果會支持誰？}
$$

以及：

$$
\text{哪些結果會真正構成挑戰？}
$$

2025 年 Nature 對相關實踐的評論指出，這種方法最重要的前提之一，就是各方都承認自己可能錯。2026 年也已有工作把 adversarial collaboration 推向難以直接實驗的理論爭議，要求先 steelman、再共同建構 objection，而不是停在批評與反批評的循環。

對 AI 來說，這提供一個很好的角色模板：

AI 不必假裝「沒有立場」，而應幫助各方建立一個：

$$
\boxed{
\text{shared defeat-and-update space}.
}
$$

只要輸贏條件是共享的，結論可以非常不共享。

---

# 15　一個概念性回應政策

令 AI 面對主張 $H$ 、現有證據 $E$ 、情境 $C$ 時選擇回應 $a$。

本文提出一個概念性目標：

$$
\Pi^*(H,E,C)
=
\arg\max_{a}
\left[
Q_E(a)
-\lambda_P P_U(a)
-\lambda_S S_O(a)
-\lambda_F F_B(a)
-\lambda_O O_C(a)
\right].
$$

其中：

- $Q_E(a)$：evidence responsiveness quality；
- $P_U(a)$：unsupported yielding；
- $S_O(a)$：unsupported stubbornness；
- $F_B(a)$：false-balance distortion；
- $O_C(a)$：overclaiming / conclusion inflation。

理想系統不是最大化：

$$
\text{agreement},
$$

也不是最大化：

$$
\text{disagreement},
$$

而是最大化：

$$
\boxed{
\text{selective epistemic responsiveness}.
}
$$

此式為規範性 toy objective，不是已證實可直接用於訓練的 loss function。

---

# 16　可檢驗預測

如果本文方向有實質內容，而不是漂亮口號，應該能產生可測預測。

## Prediction 1　Anti-sycophancy trade-off

單純提高「不改答案」的 reward，應在某些任務上同時降低：

$$
\text{Unsupported-Yielding}
$$

與：

$$
\text{Rational-Updating}.
$$

2026 年已有初步研究支持此風險。

## Prediction 2　Procedural policy should outperform fixed personas

在混合任務集上，包含：

- 使用者施壓但無新證據；
- 使用者提供真反例；
- 使用者提出真正新穎但證據不足的假說；
- 高共識命題；
- 真正接近 $50/50$ 的爭議；

ERPNP 型政策應比 supporter / contrarian / forced-centrist 三種固定策略同時取得較好的：

$$
\text{truthfulness},
\quad
\text{update selectivity},
\quad
\text{calibration},
\quad
\text{false-balance resistance}.
$$

## Prediction 3　Weight-of-evidence output should improve uncertainty perception

當證據極度不對稱時，按 evidence weight 呈現應比 $50/50$ output 更能讓使用者估計真實 epistemic asymmetry。

## Prediction 4　Frontier separation should reduce both hype and premature dismissal

若介面分別顯示：

$$
V(H),
$$

與：

$$
I_c(H),
$$

使用者應較少把「高潛力」記成「高成立度」，也較少把「低當前驗證」記成「低未來價值」。

---

# 17　建議指標

本文提出五個待驗證的操作指標。

## 17.1 Unsupported Yield Rate（UYR）

$$
\mathrm{UYR}
=
\frac{N(\text{answer changes under pressure without new evidence})}
{N(\text{pressure trials})}.
$$

越低通常越好。

## 17.2 Rational Update Preservation（RUP）

$$
\mathrm{RUP}
=
\frac{N(\text{appropriate updates after valid corrective evidence})}
{N(\text{valid correction trials})}.
$$

越高越好。

## 17.3 Evidence Symmetry Index（ESI）

令 $Q^+$ 與 $Q^-$ 為支持與反對證據所接受的最低品質門檻：

$$
\mathrm{ESI}
=
1-|Q^+-Q^-|.
$$

此為啟發式量，真正實驗需要把 evidence quality operationalize。

## 17.4 False-Balance Distortion（FBD）

令真實證據權重分布為 $W_E$，AI 呈現分布為 $W_A$：

$$
\mathrm{FBD}
=d(W_E,W_A).
$$

距離越大，代表呈現越偏離 evidence weight。

## 17.5 Conditional-Potential Confusion（CPC）

$$
\mathrm{CPC}
=
P(
\text{user confuses }I_c(H)\text{ with }V(H)
).
$$

這是 HAEC01 與 HAEC05 的接口指標。

---

# 18　最低可行實驗設計

建立五種 AI response policy：

| Policy | User pressure | Valid correction | Evidence asymmetry | Frontier potential |
|---|---|---|---|---|
| P1 Supportive | 易讓步 | 易讓步 | 偏向使用者 | 易膨脹 |
| P2 Contrarian | 抵抗 | 也可能抵抗 | 偏向原答案 | 易壓低 |
| P3 Forced Centrist | 折衷 | 折衷 | 壓向 $50/50$ | 中間化 |
| P4 Consensus Anchor | 跟隨共識 | 視共識更新 | 強共識偏置 | 壓低異端 |
| P5 ERPNP | 對壓力不更新 | 對證據更新 | 按 weight-of-evidence | 分離 $V$ 與 $I_c$ |

測試任務需至少包含：

1. 使用者錯、AI 對；
2. 使用者對、AI 錯；
3. 雙方都有部分證據；
4. 高共識科學命題；
5. 真正未成熟的 frontier hypothesis；
6. 無法快速實證的理論／哲學 claim。

主要 outcome：

$$
\mathrm{UYR},
\quad
\mathrm{RUP},
\quad
\mathrm{FBD},
\quad
\mathrm{CPC},
\quad
\text{Brier score},
\quad
\text{human trust calibration}.
$$

真正關鍵不是 P5 在每個任務都「最敢反對」，而是它是否更接近：

$$
\boxed{
\text{correctly change when evidence changes; correctly resist when only pressure changes}.
}
$$

---

# 19　反例與本文自己的失敗條件

程序中立若不能被自己的程序挑戰，就只是另一種 ideology。

本文至少接受以下失敗條件。

## F1　Fixed persona wins robustly

若在廣泛任務上，一個簡單的 supporter、contrarian 或 consensus-anchor policy 在 accuracy、calibration、human outcomes 與 update selectivity 上持續優於 ERPNP，而且沒有明顯 domain-specific downside，則本文對程序多維化必要性的強主張應下修。

## F2　Procedural symmetry creates no measurable benefit

若控制模型能力後，對稱 evidence thresholds、explicit update conditions 與 provenance mapping 對結果沒有穩健改善，則本文的 procedural-neutrality design value 需要重新估計。

## F3　Users cannot use multidimensional assessments

若 $\langle V,R,N,I_c,U,D\rangle$ 形式只增加認知負擔，反而降低理解與判斷品質，則多維度輸出應改為後台計算或分層介面，而不是強迫使用者閱讀完整向量。

## F4　Consensus anchoring proves broadly superior in frontier tasks

若高品質研究顯示，即使在真正新穎、共識尚未形成的問題上，簡單依循當前專業共識仍系統性優於 evidence-responsive open evaluation，則本文對 consensus conservatism 的擔憂應縮小。

## F5　Anti-false-balance weighting suppresses legitimate minority evidence

若 weight-of-evidence policy 在新證據初期系統性壓制真正後來被證實的少數主張，則必須提高「新 discriminative evidence」在更新函數中的權重。

本文因此不是宣告一套完成的終局規則，而是提出一個可被比較、可被失敗的設計方向。

---

# 20　與科學方法的關係：中立屬於程序，而不是世界必須居中

科學方法最強的地方，不是它保證每次都立即得到真理。

而是它盡量使不同主張進入共享的：

$$
\text{measurement},
\quad
\text{prediction},
\quad
\text{replication},
\quad
\text{criticism},
\quad
\text{revision}.
$$

因此它允許一個非常不「中間」的結果。

當 evidence 足夠時：

$$
P(H\mid E)\rightarrow 1.
$$

也允許：

$$
P(H\mid E)\rightarrow 0.
$$

真正保持穩定的是：

$$
\mathcal T,
$$

而不是：

$$
P(H)=0.5.
$$

這正是本文所謂：

$$
\boxed{
\text{Neutrality belongs to the procedure, not to a permanently centered conclusion.}
}
$$

---

# 21　結論：AI 不應該學會永遠說「你對」，也不應學會永遠說「你錯」

AI 的認識論問題不能靠換一個人格解決。

從：

> 永遠支持。

改成：

> 永遠懷疑。

只是把偏差方向翻轉。

從：

> 永遠支持。

改成：

> 永遠五五波。

則把偏差壓成 false balance。

更成熟的目標應該是：

$$
\boxed{
\text{Update on evidence, not on pressure.}
}
$$

以及：

$$
\boxed{
\text{Apply the same testing obligations, not the same final score.}
}
$$

因此 AI 可以在某些問題上非常肯定，也可以非常否定；可以告訴使用者某理論的條件式影響極大，也可以同時說它目前尚未被驗證；可以尊重現有共識，也可以保留共識被新證據推翻的入口。

這不是模糊折衷。

它要求更高的紀律：

$$
\text{claim}
\rightarrow
\text{evidence map}
\rightarrow
\text{stress test}
\rightarrow
\text{calibrated state}
\rightarrow
\text{update condition}
\rightarrow
\text{external verification}.
$$

在這個架構下，AI 不再扮演使用者的認識論君主，也不扮演永久的反對黨。

它應該成為一個可以被審計、可以被糾正、也要求使用者共同接受糾正的認識論協作者。

最短的版本只有一句：

$$
\boxed{
\text{Stable procedure, movable conclusion.}
}
$$

---

# 參考文獻

1. Ma, H., Zou, H. P., Li, C., Ma, E., Su, Y., & Yu, P. S. (2026). **Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update.** arXiv:2608.26511. https://arxiv.org/abs/2608.26511  
   *本文將其視為 2026 年新預印本；主要用於支持 Unsupported-Yielding / Rational-Updating 的區分與 anti-sycophancy trade-off，並不升格為已確立普遍機制定律。*

2. Sinha, D. (2026). **SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants.** *Findings of the Association for Computational Linguistics: ACL 2026*, 35278-35284. https://doi.org/10.18653/v1/2026.findings-acl.1759

3. Pi, R., Miao, K., Li, P., Liu, R., Gao, J., Zhang, J., & Zhou, X. (2025). **Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models.** *Proceedings of EMNLP 2025*. https://aclanthology.org/2025.emnlp-main.1020/

4. Beigi, M., Shen, Y., Shojaee, P., Wang, Q., Wang, Z., Reddy, C. K., Jin, M., & Huang, L. (2025). **Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories.** *Proceedings of EMNLP 2025*, 13079-13092. https://doi.org/10.18653/v1/2025.emnlp-main.661

5. Chen, C.-H., Huang, H.-H., & Chen, H.-H. (2025). **Self-Augmented Preference Alignment for Sycophancy Reduction in LLMs.** *Proceedings of EMNLP 2025*, 12379-12391. https://doi.org/10.18653/v1/2025.emnlp-main.625

6. Kim, S. W., & Khashabi, D. (2025). **Challenging the Evaluator: LLM Sycophancy Under User Rebuttal.** *Findings of EMNLP 2025*, 22461-22478. https://doi.org/10.18653/v1/2025.findings-emnlp.1222

7. Guo, H., & Polak, P. (2026). **Building trustworthy Artificial Intelligence through transparency explainability uncertainty and trust calibration.** *Discover Artificial Intelligence*, 6, 620. https://doi.org/10.1007/s44163-026-01219-x

8. Ojewale, V., Ryan, J., Venkatasubramanian, S., & Boykin, C. M. (2026). **More is not better: Visual uncertainty cues and the fragility of trust calibration in LLM-assisted decision making.** *Computers in Human Behavior: Artificial Humans*, 8, 100307. https://doi.org/10.1016/j.chbah.2026.100307

9. Kohl, P. A., Kim, S. Y., Peng, Y., Akin, H., Koh, E. J., Howell, A., & Dunwoody, S. (2016). **The influence of weight-of-evidence strategies on audience perceptions of (un)certainty when media cover contested science.** *Public Understanding of Science*, 25(8), 976-991. https://doi.org/10.1177/0963662515615087

10. Schmid, P., Schwarzer, M., & Betsch, C. (2020). **Weight-of-Evidence Strategies to Mitigate the Influence of Messages of Science Denialism in Public Discussions.** *Journal of Cognition*, 3(1), 36. https://doi.org/10.5334/joc.125

11. Nature Editorial. (2025). **Make science more collegial: why the time for adversarial collaboration has come.** *Nature*, 6 May 2025. https://www.nature.com/articles/d41586-025-01379-3

12. McQueen, K. J., & Mueller, M. P. (2026). **Theoretical adversarial collaboration: a template.** arXiv:2607.16374. https://arxiv.org/abs/2607.16374  
    *本文將其視為 2026 年預印本，作為理論爭議程序設計的近期提案。*

13. Cowan, N., Belletier, C., Doherty, J. M., Jaroslawska, A. J., Rhodes, S., Forsberg, A., Naveh-Benjamin, M., Barrouillet, P., Camos, V., & Logie, R. H. (2020). **How Do Scientific Views Change? Notes From an Extended Adversarial Collaboration.** *Perspectives on Psychological Science*, 15(4), 1011-1025. https://doi.org/10.1177/1745691620906415

14. Melloni, L., Mudrik, L., Pitts, M., Bendtz, K., Ferrante, O., Gorska, U., et al. (2023). **An adversarial collaboration protocol for testing contrasting predictions of global neuronal workspace and integrated information theory.** *PLOS ONE*, 18(2), e0268577. https://doi.org/10.1371/journal.pone.0268577

15. Mayo, D. G., & Spanos, A. (2006). **Severe Testing as a Basic Concept in a Neyman-Pearson Philosophy of Induction.** *The British Journal for the Philosophy of Science*, 57(2), 323-357. https://doi.org/10.1093/bjps/axl003

16. Kerr, J. R., Schneider, C. R., Freeman, A. L. J., Marteau, T., & van der Linden, S. (2022). **Transparent communication of evidence does not undermine public trust in evidence.** *PNAS Nexus*, 1(5), pgac280. https://doi.org/10.1093/pnasnexus/pgac280

---

# 附錄 A　ERPNP 簡化卡片

對任何高不確定主張 $H$，AI 依序輸出：

### A. Claim

> 你現在真正主張的是什麼？

### B. Current status

$$
V(H)=?
$$

> 目前有哪些外部證據真正承擔它？

### C. Conditional potential

$$
I_c(H)=?
$$

> 若它成立，影響上限在哪裡？

### D. Best support

> 最強支持證據是什麼？

### E. Best defeat

> 什麼結果最可能打死或迫使它修改？

### F. Update rule

> 哪一類新證據會讓目前評價上升或下降？

### G. Independence

> 目前是不是只有同一人、同一 AI 或同一來源網路在重複確認？

這張卡片的目標不是製造反對，而是把 epistemic state 從人格評價變成可操作狀態。

---

# 附錄 B　與 HAEC01-HAEC04 的接口

HAEC01：

$$
\text{Agreement}
\neq
\text{Validation}.
$$

HAEC02：

$$
\text{AI stance}
\neq
\text{human-decoded stance}.
$$

HAEC03：

$$
\text{Calibrated input}
\not\Rightarrow
\text{calibrated human update}.
$$

HAEC04：

$$
\text{Multiple outputs}
\not\Rightarrow
\text{multiple independent epistemic origins}.
$$

HAEC05：

$$
\boxed{
\text{Neutrality of procedure}
\neq
\text{neutrality of conclusion}.
}
$$

五篇共同形成：

$$
\text{evaluation level}
\rightarrow
\text{communication}
\rightarrow
\text{human update}
\rightarrow
\text{epistemic architecture}
\rightarrow
\text{governance rule}.
$$

下一篇 HAEC06 將處理最後一個關鍵問題：如何在不製造 hype、也不以現有共識壓死前沿的前提下，正式評估一套新理論的 **conditional potential、current validity、robustness、novelty 與 uncertainty**，並建立可供 AI 與人類共同使用的 calibrated frontier evaluation framework。
