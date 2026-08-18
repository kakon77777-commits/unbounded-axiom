# ADHD 的連續配置空間：從亞臨床特徵到臨床診斷

**英文題名：** The Continuous Configuration Space of ADHD: From Subthreshold Traits to Clinical Diagnosis  
**系列：** ADHD 動態配置與認知拓撲系列，第 8 篇  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論建模／認知科學命題／研究綱領  
**文獻檢索截點：** 2026-08-17  

---

# 0. 醫學、分類與證據邊界聲明

本文不是臨床研究、診斷工具、治療指南、流行病學研究或醫療建議。

本文提出的「連續配置空間」「診斷決策區域」「亞臨床配置」「局部聚類」「配置距離」「功能損害流形」等概念均屬待驗證理論命題，不代表已被醫學界確認的 ADHD 病理機制或正式診斷模型。

原作者並非醫學、精神醫學、神經科學、遺傳學或臨床心理專業研究者。本文不提供新的臨床、人體、遺傳、神經影像、流行病學或心理實驗數據；所有實證性背景均來自公開同行評審研究與正式分類資料。

本文不得被用於：

- 自行診斷 ADHD；
- 將「亞臨床特徵」直接等同正式 ADHD；
- 將未達診斷標準者稱為「隱藏 ADHD」；
- 以數學距離取代專業臨床判斷；
- 推翻或修改既有個人醫療診斷。

本文最重要的邊界為：

$$
\boxed{
\text{ADHD-like traits}
\neq
\text{clinical ADHD diagnosis}.
}
$$

以及：

$$
\boxed{
\text{continuous liability}
\neq
\text{absence of clinically useful categories}.
}
$$

一個疾病或症候群即使建立在連續風險與症狀分布上，臨床仍可以基於功能損害、持續性、跨情境性、發展史、鑑別診斷與治療需要建立有實用價值的類別判定。

核心限制：

$$
\boxed{
\text{dimensional ontology}
\neq
\text{automatic diagnostic equivalence}.
}
$$

---

# 摘要

ADHD 長期同時具有兩種看似競爭的描述。臨床分類需要回答「是否符合 ADHD 診斷」，因此使用類別式決策；人口、遺傳、症狀與生活品質研究則反覆顯示，inattention、hyperactivity／impulsivity 與相關功能困難廣泛分布於一般人口中，且未必存在自然、陡峭的生物學或功能斷點。

2024 年 Arildskov 等人在 1,967 名一般人口學童中檢驗 ADHD traits 與 psychosocial quality of life 的關係，未發現高 trait 區域存在突然的 QoL 崩落門檻，結果更接近線性下降。2025 年 van der Laan 等人的大型 genome-wide association meta-analysis 整合 290,134 次 ADHD symptom measures、70,953 名獨立個體與 ADHD diagnosis GWAS，結論支持 clinical ADHD 位於由 ADHD symptoms 索引的 continuous liability 高端。2025 年 Knyspel 等人分析 10,454 名 21 歲雙生子，psychometric bifactor model 支持 ADHD symptoms 的 general dimension，同時保留 inattention 與 hyperactivity 的 secondary dimensions；遺傳層面又顯示這些維度不能簡化為單一完全同質因素。

然而，連續性並不排除局部結構。2026 年 Pan 等人的 JAMA Psychiatry 多中心兒童研究，在 normative morphometric similarity network deviations 上辨識出三個可外部驗證的 ADHD biotypes，並明確指出其結果同時提供 dimensional 與 categorical insights。2024 年 Nature Genetics 的 14,084 名已診斷 ADHD 個案研究亦顯示，不同共病與診斷歷程群體具有不同 polygenic profiles，支持 ADHD 內部存在遺傳異質性。

基於上述證據，本文提出「Continuous Configuration Space Hypothesis, CCSH」。令個體在時間 $t$ 的 ADHD-related configuration 為：

$$
\mathbf c_{i,t}
\in
\Omega_C
\subseteq
\mathbb R^d.
$$

其中 $\mathbf c_{i,t}$ 不代表診斷，而是由注意配置、抑制、工作記憶、喚醒、獎勵、情緒調節、切換、時間組織、情境敏感度等候選維度構成的中層狀態向量。

臨床診斷則表示為另一層決策算子：

$$
\mathcal D_{i,t}
=
\Gamma
\left(
\mathbf y_{i,t},
I_{i,t},
H_i,
X_{i,t}
\right),
$$

其中 $\mathbf y$ 為可觀察症狀， $I$ 為功能損害， $H$ 為發展史， $X$ 為跨情境與鑑別診斷等臨床資訊。

因此：

$$
\boxed{
\mathbf c
\text{ can be continuous while }
\mathcal D
\text{ is categorical}.
}
$$

本文定義「subthreshold／亞臨床」不是「其實已經有 ADHD」，而是：

$$
\Gamma(\cdot)=0
$$

的前提下，仍可能存在部分 ADHD-related traits 或功能困難。這些個體可能需要支持，但支持需要不等於 ADHD 診斷成立。

本文進一步提出：高維配置空間可以同時具有連續密度、局部聚類、不同功能損害曲面與任務依賴邊界；臨床 diagnosis 是在此空間之上建立的決策層，而不是自然界必然存在的一條單一歐氏幾何切線。

最終可證偽問題為：

$$
\boxed{
\text{Does a high-dimensional continuous-plus-cluster model
predict impairment, course, and treatment-relevant outcomes
better than either a pure binary model or a pure single-axis spectrum?}
}
$$

**關鍵詞：** ADHD、dimensional model、categorical diagnosis、subthreshold、continuous liability、biotype、heterogeneity、functional impairment、polygenic risk、configuration space

---

# 1. 問題：ADHD 到底是「類別」還是「光譜」？

這個問題若只允許：

$$
\text{Category}
\lor
\text{Dimension},
$$

本身可能就是錯誤二分。

因為我們其實至少在問三個不同問題。

第一：

> 症狀與風險在一般人口中如何分布？

第二：

> 生物、認知或行為資料中是否存在可重現的局部群集？

第三：

> 臨床上何時應建立一個可操作的診斷決策？

這三個問題可以得到不同答案。

因此：

$$
\boxed{
\text{population distribution}
\neq
\text{latent clustering}
\neq
\text{clinical classification}.
}
$$

---

# 2. 連續性與類別性可以同時成立

假設某個底層 liability：

$$
z
\in
\mathbb R.
$$

它可以連續分布：

$$
z
\sim
p(z).
$$

臨床卻仍可設定：

$$
z>\theta
$$

作為某一決策規則的一部分。

因此：

$$
\boxed{
z\text{ continuous}
\not\Rightarrow
\text{clinical categories meaningless}.
}
$$

同樣：

$$
\boxed{
\text{diagnostic category useful}
\not\Rightarrow
z\text{ naturally binary}.
}
$$

---

# 3. 2024 QoL 研究：沒有看到自然跳變點

Arildskov 等人研究：

$$
N=1967
$$

名 6–11 歲一般人口學童。

研究檢驗：

$$
\text{ADHD traits}
\rightarrow
\text{psychosocial QoL}
$$

是否在高 trait 區突然出現明顯非線性下降。

結果沒有找到：

$$
\theta_{\text{natural}}
$$

式的明顯 QoL 跳變點。

較符合：

$$
\text{trait severity}\uparrow
\Rightarrow
\text{QoL}\downarrow
$$

的漸進關係。

因此：

$$
\boxed{
\text{functional burden may be dimensional}.
}
$$

但這不表示：

$$
\text{diagnostic threshold}
$$

毫無臨床功能。

---

# 4. 症狀門檻與損害門檻不是同一件事

早期 impairment research 已指出：

$$
\text{symptom severity}
$$

與：

$$
\text{functional impairment}
$$

彼此相關但不相同。

因此：

$$
\boxed{
S_{\text{symptom}}
\neq
I_{\text{impairment}}.
}
$$

一個人可以：

$$
S_{\text{symptom}}\uparrow
$$

但當下：

$$
I_{\text{impairment}}
$$

受到環境支架保護。

反過來也可能有：

$$
S_{\text{symptom}}
$$

不極端，

但：

$$
I_{\text{impairment}}\uparrow
$$

因為任務與環境要求高度不匹配。

---

# 5. 成人 ADHD 的 impairment assessment 本身仍在發展

2024 年 Fuermaier 等人調查 92 名參與 ADHD clinical practice／research 的國際專業人士。

研究發現：

- 成人 ADHD impairment measurement 使用工具高度多樣；
- 部分工具的 psychometric properties 可能不足；
- 臨床與研究者對現行實務存在不滿；
- 仍需要更好的 impairment assessment。

因此：

$$
\boxed{
\text{impairment}
\text{ is clinically essential but not trivially measured}.
}
$$

這使任何以單一 symptom cutoff 取代完整功能評估的理論都過度簡化。

---

# 6. 2025 Genetics：Clinical ADHD 位於 Continuous Liability 高端

2025 年 van der Laan 等人進行大型 GWAS meta-analysis。

其 symptom data 包含：

$$
290,134
$$

次 ADHD symptom measurements，

來自：

$$
70,953
$$

名獨立個體，

涵蓋多個：

- raters；
- ages；
- instruments。

研究再與 ADHD diagnosis GWAS 整合。

其整體結果支持：

$$
\boxed{
\text{clinical ADHD lies toward the extreme
of a continuous liability indexed by ADHD symptoms}.
}
$$

這是一個重要的遺傳層支持。

但：

$$
\text{genetic continuity}
$$

不表示：

$$
\text{one-gene-one-axis model}.
$$

---

# 7. Polygenic 不等於單維

若疾病風險來自許多 genetic variants：

$$
G
=
\sum_{k=1}^{m}
w_k g_k,
$$

也不能推出：

$$
\text{phenotype}
=
f(G)
$$

只有一個維度。

因為：

- 不同 genes 可能作用於不同 pathways；
- gene–environment interaction 存在；
- pleiotropy 存在；
- developmental stage 不同；
- co-occurring conditions 不同。

所以：

$$
\boxed{
\text{continuous genetic liability}
\neq
\text{unidimensional phenotype}.
}
$$

---

# 8. 2025 Twin Study：General Dimension 與 Secondary Dimensions 共存

Knyspel、Morneau-Vaillancourt 與 Eley 分析：

$$
N=10,454
$$

名 21 歲雙生子。

psychometric bifactor model 支持：

$$
G_{\text{ADHD}}
$$

這個 general symptom dimension，

同時保留：

$$
I_{\text{inattention}},
$$

$$
H_{\text{hyperactivity}}
$$

等 secondary dimensions。

因此：

$$
\boxed{
\text{general ADHD dimension}
+
\text{meaningful subdimensions}
}
$$

比單一 scalar 更合理。

遺傳與環境分解也沒有支持「所有 ADHD symptoms 共享一個完全同質遺傳因素」的簡單模型。

---

# 9. 從一維光譜升級為高維空間

本文因此不採：

$$
x
\in
\mathbb R
$$

作為完整 ADHD representation。

而採：

$$
\boxed{
\mathbf c
=
(c_1,c_2,\ldots,c_d)
\in
\Omega_C
\subseteq
\mathbb R^d.
}
$$

候選維度可包含：

$$
\mathbf c
=
(
A,
I,
WM,
R,
N,
S,
E,
T,
X,
C_{\text{context}},
\ldots
).
$$

例如：

- attention allocation；
- inhibitory control；
- working memory；
- reward sensitivity；
- novelty sensitivity；
- arousal regulation；
- emotion regulation；
- temporal organization；
- switching／executive control；
- context sensitivity。

這些不是正式臨床維度，只是中層候選坐標。

---

# 10. 配置空間不是診斷空間

本文定義：

$$
\Omega_C
=
\text{configuration space}.
$$

臨床觀察空間則為：

$$
\Omega_Y
=
\text{observable symptom／impairment space}.
$$

兩者間存在 mapping：

$$
F:
\Omega_C
\times
\Omega_E
\rightarrow
\Omega_Y.
$$

其中：

$$
\Omega_E
$$

包含 task、environment、development、support。

因此：

$$
\boxed{
\mathbf c
\neq
\mathbf y.
}
$$

---

# 11. Clinical Diagnosis 是另一層算子

定義臨床判定：

$$
\mathcal D
=
\Gamma
\left(
\mathbf y,
I,
H,
X
\right).
$$

其中：

- $\mathbf y$：症狀與行為表型；
- $I$：功能損害；
- $H$：發展史；
- $X$：跨情境性、鑑別診斷與其他臨床資訊。

輸出：

$$
\mathcal D
\in
\{0,1\}.
$$

這裡的二元值只是抽象化「未符合／符合診斷」決策。

它不是對 DSM 或 ICD 的重建，也不是臨床計分器。

---

# 12. Continuous Input 可以產生 Categorical Output

即使：

$$
\mathbf y
$$

與：

$$
I
$$

是連續的，

$$
\Gamma
$$

仍可產生：

$$
0
$$

或：

$$
1.
$$

因此：

$$
\boxed{
\text{continuous phenotype}
\rightarrow
\text{categorical clinical decision}
}
$$

在數學上完全自然。

---

# 13. Clinical Threshold 是 Decision Threshold，不必是 Natural Cliff

若：

$$
r(\mathbf y,I,H,X)
$$

為某種抽象 clinical-evidence score，

可概念化：

$$
\Gamma
=
\mathbb I
\left[
r\geq\theta_D
\right].
$$

這不表示：

$$
\theta_D
$$

在自然界中必然對應一個：

$$
\text{biological discontinuity}.
$$

其功能可以是：

- 提高診斷一致性；
- 決定醫療服務入口；
- 支持風險／效益判斷；
- 建立可溝通類別。

---

# 14. 診斷類別可以有效，即使邊界不是自然斷崖

很多實際系統都使用 decision threshold。

例如：

$$
\text{continuous measurement}
\rightarrow
\text{action category}.
$$

因此：

$$
\boxed{
\text{operational threshold}
\neq
\text{ontological cliff}.
}
$$

這是本文對 category–dimension 爭論最重要的修正。

---

# 15. Subthreshold 的最小定義

本文使用：

$$
\text{subthreshold}
$$

只表示：

> 存在部分 ADHD-related traits／difficulties，但目前不符合完整正式 ADHD 診斷要求。

抽象表示：

$$
\Gamma(\cdot)=0
$$

但：

$$
\|\mathbf y_{\text{ADHD-related}}\|>0.
$$

因此：

$$
\boxed{
\text{subthreshold}
\neq
\text{undiagnosed clinical ADHD by definition}.
}
$$

---

# 16. Subthreshold 也可能有真正功能困難

可以存在：

$$
\Gamma=0,
$$

但：

$$
I>0.
$$

此時：

$$
\boxed{
\text{support need}
\neq
\text{diagnostic status}.
}
$$

一個人可能需要：

- organization support；
- sleep intervention；
- educational accommodation；
- environmental restructuring；
- psychological treatment for another condition；

而不代表 ADHD diagnosis 必然成立。

---

# 17. 2025 Subthreshold Review 的啟示與限制

2025 年 Ogundele 等人的 narrative review 討論 subthreshold autism／ADHD。

作者主張，若未達正式 NDD criteria，但存在顯著、持續的 impairment，可以考慮記錄 subthreshold condition。

這是一項臨床討論與作者建議。

它不是：

$$
\boxed{
\text{DSM／ICD 已新增正式 subthreshold ADHD diagnosis}.
}
$$

因此本文只採用：

$$
\text{clinically relevant below-threshold difficulties}
$$

這個較弱概念。

---

# 18. 不要把「接近診斷區」叫做「其實已經有」

若個體：

$$
\mathbf c_i
$$

與某臨床群體平均 configuration：

$$
\boldsymbol\mu_{\text{ADHD}}
$$

很接近，

也不能推出：

$$
\mathcal D_i=1.
$$

所以：

$$
\boxed{
d
\left(
\mathbf c_i,
\boldsymbol\mu_{\text{ADHD}}
\right)
\downarrow
\not\Rightarrow
\text{ADHD diagnosis}.
}
$$

---

# 19. Configuration Distance

若有標準化 configuration coordinates，可定義：

$$
d_C
\left(
\mathbf c_i,\mathbf c_j
\right).
$$

例如 Mahalanobis distance：

$$
d_M
=
\sqrt{
(\mathbf c_i-\boldsymbol\mu)^{\top}
\Sigma^{-1}
(\mathbf c_i-\boldsymbol\mu)
}.
$$

但：

$$
d_M
$$

只能表示多維統計距離。

它不是：

$$
\text{diagnostic probability}.
$$

---

# 20. 相似配置可以有不同診斷結果

若：

$$
\mathbf c_i
\approx
\mathbf c_j,
$$

但：

$$
I_i\neq I_j,
$$

或：

$$
H_i\neq H_j,
$$

或：

$$
X_i\neq X_j,
$$

可以：

$$
\Gamma_i\neq\Gamma_j.
$$

因此：

$$
\boxed{
\text{configuration similarity}
\neq
\text{clinical equivalence}.
}
$$

---

# 21. 不同配置也可以產生相似表型

反過來：

$$
\mathbf c_i
\neq
\mathbf c_j
$$

可能仍有：

$$
\mathbf y_i
\approx
\mathbf y_j.
$$

例如 attention failure 可以來自：

- arousal instability；
- distractor competition；
- working-memory failure；
- sleep-like lapse；
- high switching；
- motivational mismatch。

因此：

$$
\boxed{
\text{same phenotype}
\leftarrow
\text{multiple configurations}.
}
$$

---

# 22. Many-to-One Mapping

形式上：

$$
F:
\Omega_C
\rightarrow
\Omega_Y
$$

可能是 many-to-one。

即：

$$
F(\mathbf c_1)
=
F(\mathbf c_2)
$$

而：

$$
\mathbf c_1\neq\mathbf c_2.
$$

這是 ADHD heterogeneity 的一個自然數學表示。

---

# 23. One-to-Many Across Contexts

同一配置：

$$
\mathbf c
$$

在不同環境：

$$
e_1,e_2
$$

可產生：

$$
F(\mathbf c,e_1)
\neq
F(\mathbf c,e_2).
$$

因此：

$$
\boxed{
\text{same person}
+
\text{different context}
\rightarrow
\text{different phenotype}.
}
$$

這與前七篇的 dynamic-configuration model 相容。

---

# 24. 密度，而不是天然牆壁

令一般人口 configuration density：

$$
\rho(\mathbf c).
$$

ADHD-related diagnosed sample density：

$$
\rho_D(\mathbf c).
$$

可能：

$$
\rho_D
$$

在某些空間區域較高，

但未必存在：

$$
\partial\Omega_D
$$

這種完全沒有重疊的天然硬牆。

因此：

$$
\boxed{
\text{density enrichment}
\neq
\text{perfect separability}.
}
$$

---

# 25. Local Clusters 可以存在於 Continuous Space

假設：

$$
\rho(\mathbf c)
$$

具有多個局部峰：

$$
\boldsymbol\mu_1,
\boldsymbol\mu_2,\ldots,\boldsymbol\mu_K.
$$

則：

$$
\boxed{
\text{continuum}
+
\text{clusters}
}
$$

可以同時成立。

這就是 2026 JAMA Psychiatry biotype study 對本篇最重要的啟示。

---

# 26. 2026 Biotypes：不是「三種真正 ADHD」的最終答案

Pan 等人在 pediatric datasets 中使用 normative modeling 與 semisupervised clustering。

discovery cohort：

$$
446
$$

名 ADHD 兒童與：

$$
708
$$

名 controls。

external validation cohort 包含：

$$
554
$$

名 ADHD cases。

得到三個 biotypes：

1. severe-combined＋emotional dysregulation；
2. predominantly hyperactive／impulsive；
3. predominantly inattentive。

研究結論明確稱其提供：

$$
\boxed{
\text{dimensional and categorical insights}.
}
$$

但本文不把三個 biotypes 視為正式新診斷。

---

# 27. Biotype 不等於 Clinical Subtype

目前影像 biotype：

$$
B_k^{\text{neuro}}
$$

與臨床 subtype：

$$
B_k^{\text{clinical}}
$$

不能直接等同。

因此：

$$
\boxed{
\text{data-driven biotype}
\neq
\text{validated clinical diagnostic type}.
}
$$

仍需：

- replication；
- individual-level reliability；
- treatment prediction；
- longitudinal stability；
- cost-benefit evaluation。

---

# 28. Normative Modeling 的重要觀念

Pan 等人的方法先建立：

$$
\text{normative distribution}
$$

再計算個體 deviation：

$$
z_i
=
\frac{
x_i-\mu_{\text{norm}}
}{
\sigma_{\text{norm}}
}.
$$

這比單純：

$$
\text{ADHD mean}
-
\text{control mean}
$$

更接近個體化。

因此本篇引入：

$$
\boxed{
\text{individual deviation profile}.
}
$$

---

# 29. 配置偏差向量

定義：

$$
\mathbf z_i
=
\left(
z_{i1},
z_{i2},
\ldots,z_{id}
\right).
$$

每一維是相對 reference population 的 deviation。

但：

$$
\mathbf z_i
$$

不代表 pathology map。

它只是：

$$
\text{relative position}.
$$

---

# 30. 正常範圍本身不是單一點

reference population 不是：

$$
\mathbf c=\mathbf0.
$$

而是分布：

$$
p_{\text{ref}}(\mathbf c).
$$

所以：

$$
\boxed{
\text{normal variation}
\neq
\text{zero variation}.
}
$$

---

# 31. 診斷不能由「偏離平均」直接得到

一個人可能：

$$
|z_k|\gg0
$$

但沒有 impairment。

另一人：

$$
|z_k|
$$

不極端，

卻在特定生活需求下有嚴重功能困難。

因此：

$$
\boxed{
\text{statistical atypicality}
\neq
\text{clinical disorder}.
}
$$

---

# 32. 遺傳異質性支持「一個 ADHD 裡有很多路徑」

2024 Nature Genetics 對：

$$
14,084
$$

名 diagnosed ADHD individuals 進行 case-only genetic heterogeneity research。

研究顯示不同 ADHD-adjacent profiles，例如：

- ADHD＋ASD；
- ADHD＋substance use disorder；
- adulthood-first-diagnosed ADHD；

具有可區分的 polygenic score patterns。

因此：

$$
\boxed{
\text{same diagnostic label}
\neq
\text{same polygenic profile}.
}
$$

---

# 33. 遺傳異質性不等於可以基因診斷個人

即使群體層：

$$
PGS_A\neq PGS_B,
$$

也不能推出：

$$
\text{individual diagnosis}
=
f(PGS).
$$

現階段：

$$
\boxed{
\text{polygenic association}
\neq
\text{clinical diagnostic test}.
}
$$

---

# 34. 高維配置空間的多尺度結構

本文將 ADHD-related space 暫分四層：

## 34.1 Trait Layer

$$
\Omega_T.
$$

連續 symptoms／traits。

## 34.2 Cognitive Configuration Layer

$$
\Omega_C.
$$

認知與狀態維度。

## 34.3 Functional Layer

$$
\Omega_I.
$$

日常功能損害。

## 34.4 Clinical Decision Layer

$$
\Omega_D.
$$

正式診斷與醫療決策。

因此：

$$
\boxed{
\Omega_T
\neq
\Omega_C
\neq
\Omega_I
\neq
\Omega_D.
}
$$

---

# 35. 不能用一條 Axis 代替四層

錯誤模型：

$$
x
=
\text{ADHD amount}.
$$

更合理：

$$
\mathbf X
=
\left(
\mathbf t,
\mathbf c,
\mathbf i,
\mathbf h,
\mathbf e
\right).
$$

其中：

- $\mathbf t$：traits；
- $\mathbf c$：cognitive configuration；
- $\mathbf i$：impairment profile；
- $\mathbf h$：developmental history；
- $\mathbf e$：environment／context。

---

# 36. Functional Impairment 是向量

成人功能至少可以包含：

$$
\mathbf i
=
\left(
I_{\text{academic}},
I_{\text{work}},
I_{\text{financial}},
I_{\text{relationship}},
I_{\text{daily}},
I_{\text{safety}}
\right).
$$

因此：

$$
I
$$

不必只有一個總分。

---

# 37. 不同人可以在不同功能域跨門檻

例如：

$$
I_{\text{work}}>\theta,
$$

但：

$$
I_{\text{relationship}}<\theta.
$$

另一人相反。

所以：

$$
\boxed{
\text{functional impairment}
=
\text{profile},
}
$$

而不是純 scalar。

---

# 38. Impairment Surface

給定 configuration：

$$
\mathbf c
$$

與 context：

$$
\mathbf e,
$$

定義：

$$
I
=
\Phi
\left(
\mathbf c,\mathbf e
\right).
$$

這形成：

$$
\boxed{
\text{impairment surface}.
}
$$

同一 configuration 在不同 context 對應不同高度。

---

# 39. Clinical Region 不是單純球體

若將 formal diagnosis region 抽象表示為：

$$
\mathcal R_D
\subset
\Omega_T
\times
\Omega_I
\times
\Omega_H,
$$

它不應被想像成：

$$
\|\mathbf c-\boldsymbol\mu\|<r
$$

的簡單球體。

臨床規則通常包含：

- symptom pattern；
- impairment；
- duration；
- developmental onset；
- cross-setting evidence；
- differential diagnosis。

所以：

$$
\boxed{
\mathcal R_D
\text{ is a decision region, not a Euclidean cluster}.
}
$$

---

# 40. Subthreshold Region

可概念化：

$$
\mathcal R_{\text{sub}}
=
\left\{
x:
\Gamma(x)=0
\land
\|\mathbf y_{\text{ADHD-related}}\|>0
\right\}.
$$

但：

$$
\mathcal R_{\text{sub}}
$$

內部同樣高度異質。

可能包括：

- transient traits；
- mild persistent traits；
- impairment from another condition；
- compensated profiles；
- developmental variation；
- measurement noise。

因此：

$$
\boxed{
\text{subthreshold}
\neq
\text{one latent disorder}.
}
$$

---

# 41. Near-Threshold Instability

若某人：

$$
r\approx\theta_D,
$$

小幅 measurement／context change 可造成：

$$
\Gamma_t=0
$$

與：

$$
\Gamma_{t+1}=1.
$$

這不必表示：

$$
\text{biology suddenly changed}.
$$

而可能只是：

$$
\boxed{
\text{classification near a decision boundary is sensitive to context and measurement}.
}
$$

---

# 42. 診斷變化不等於身份翻轉

一個人某時：

$$
\Gamma_t=1
$$

後來：

$$
\Gamma_{t+1}=0
$$

可能反映：

- symptom remission；
- developmental change；
- treatment；
- context；
- measurement；
- criterion differences。

因此：

$$
\boxed{
\text{diagnostic status over time}
\neq
\text{immutable cognitive identity}.
}
$$

---

# 43. Adult Review 的重要提醒：即使不再符合診斷，困難仍可能存在

2025 World Psychiatry 成人 ADHD 綜述指出，部分 childhood-onset ADHD individuals 到成年後可能仍有 impairing symptoms，即使不再滿足完整 formal diagnostic criteria。

這再次支持：

$$
\boxed{
\text{diagnostic threshold crossing}
\neq
\text{all-or-none disappearance of traits}.
}
$$

---

# 44. Persistent Trait Without Diagnosis

可能：

$$
\Gamma_t=0,
$$

但：

$$
\mathbf y_t\neq\mathbf0.
$$

這並不矛盾。

類別判定變化可以與連續 trait persistence 同時存在。

---

# 45. Transdiagnostic Overlap

ADHD-related dimensions 與：

- autism；
- anxiety；
- depression；
- sleep disorders；
- learning disorders；
- substance-related conditions；

可能共享部分：

$$
\Omega_C
$$

區域。

因此：

$$
\boxed{
\text{shared dimension}
\neq
\text{same disorder}.
}
$$

---

# 46. 診斷仍需要 Differential Information

若兩種 disorder：

$$
D_1,
D_2
$$

在某些 configuration 維度重疊，

則需要：

$$
X
$$

中的其他 evidence 進行區分。

所以高維 dimensional model 不是：

$$
\text{diagnosis-free model}.
$$

反而更需要嚴格 differential diagnosis。

---

# 47. Pure Spectrum Model 也會失敗

若只寫：

$$
\text{everyone is a little ADHD},
$$

會產生嚴重概念錯誤。

因為：

$$
\text{trait presence}
$$

與：

$$
\text{persistent clinically significant disorder}
$$

不是同一件事。

因此本文明確拒絕：

$$
\boxed{
\text{everyone is on the ADHD spectrum}
\Rightarrow
\text{everyone has ADHD}.
}
$$

---

# 48. Pure Binary Model 也會失敗

反過來若只寫：

$$
ADHD\in\{0,1\}
$$

並假設兩群所有底層特徵完全分離，

也無法容納：

- symptom continuum；
- subthreshold impairment；
- remission；
- context dependence；
- genetic continuity；
- within-diagnosis heterogeneity。

所以：

$$
\boxed{
\text{binary decision}
\neq
\text{binary ontology}.
}
$$

---

# 49. Continuous-Plus-Cluster Model

本文提出：

$$
\boxed{
\Omega_C
=
\text{continuous space with possible local density structure}.
}
$$

概念上可以用 mixture density：

$$
p(\mathbf c)
=
\sum_{k=1}^{K}
\pi_k
p_k(\mathbf c).
$$

但：

$$
K
$$

不預設為 3。

2026 biotype study 找到 3 群，不代表自然界永遠只有 3 群。

---

# 50. Cluster Stability

若存在 cluster：

$$
C_k,
$$

需要檢驗：

$$
\operatorname{Stability}(C_k)
$$

跨：

- cohort；
- age；
- culture；
- sex；
- medication；
- scanner／instrument；
- time。

如果 cluster 不穩定，就不能臨床本體化。

---

# 51. Cluster Membership 也可以是機率

不必：

$$
x\in C_1
$$

或：

$$
x\in C_2.
$$

可以：

$$
P(C_k\mid x).
$$

因此：

$$
\boxed{
\text{fuzzy membership}
}
$$

可能比硬分類更符合異質資料。

---

# 52. Category、Dimension 與 Cluster 的三層統一

本文最終統一：

$$
\boxed{
\text{Dimension}
\rightarrow
\text{describes variation}
}
$$

$$
\boxed{
\text{Cluster}
\rightarrow
\text{describes local structure}
}
$$

$$
\boxed{
\text{Category}
\rightarrow
\text{supports decisions}
}
$$

三者不是競爭對手。

---

# 53. Clinical Diagnosis 的價值不依賴於「自然斷點」

診斷可以提供：

- treatment access；
- communication；
- prognosis；
- support eligibility；
- research inclusion；
- risk management。

所以：

$$
\boxed{
\text{clinical usefulness}
\neq
\text{proof of natural-kind discreteness}.
}
$$

---

# 54. 反過來，Dimension 也不能自行決定 Treatment

知道：

$$
\mathbf c_i
$$

位於某個連續位置，

並不能直接推出：

$$
\text{treatment}_i.
$$

治療還取決於：

- impairment；
- preference；
- comorbidity；
- risk；
- evidence base；
- contraindications；
- goals。

所以：

$$
\boxed{
\text{dimensional description}
\neq
\text{clinical prescription}.
}
$$

---

# 55. CCSH 十二項核心命題

## CC-H1：連續性命題

至少部分 ADHD-related traits：

$$
T_k
$$

在一般人口中近似連續分布。

---

## CC-H2：診斷非等同性命題

$$
T_k>0
\not\Rightarrow
\mathcal D=1.
$$

---

## CC-H3：症狀—損害分離命題

$$
S_{\text{symptom}}
\neq
I_{\text{impairment}}.
$$

---

## CC-H4：高維命題

ADHD-related variation 不能被單一 scalar 完整表示。

---

## CC-H5：Continuous-Plus-Cluster 命題

$$
\text{continuous variation}
+
\text{local clustering}
$$

可以同時存在。

---

## CC-H6：Many-to-One 命題

不同 configurations 可產生相似 phenotype。

---

## CC-H7：Contextual One-to-Many 命題

同一 configuration 在不同 context 可產生不同 phenotype。

---

## CC-H8：Subthreshold Non-Identity 命題

$$
\text{subthreshold traits}
\neq
\text{hidden clinical ADHD by definition}.
$$

---

## CC-H9：Decision-Boundary 命題

正式診斷 boundary 可以具有臨床效用，而不要求 underlying natural cliff。

---

## CC-H10：Fuzzy-Biotype 命題

biotype membership 若存在，可能是 probabilistic 而非硬分割。

---

## CC-H11：Transdiagnostic Overlap 命題

部分 cognitive dimensions 可以跨診斷共享，但共享不取消 differential diagnosis。

---

## CC-H12：增量價值命題

若高維 continuous-plus-cluster model 在控制 symptom score 與現行 diagnosis 後，不能提高 impairment／course／treatment-outcome prediction：

$$
\Delta R^2\approx0,
$$

則 CCSH 應被簡化。

---

# 56. 實驗一：Population Density Mapping

在大型一般人口樣本測：

$$
\mathbf c_i.
$$

估計：

$$
p(\mathbf c).
$$

檢查：

- unimodal；
- multimodal；
- heavy-tail；
- manifold；
- local clusters。

不預先切 ADHD／control。

---

# 57. 實驗二：Symptom–Impairment Surface

同時測：

$$
\mathbf y_i
$$

與：

$$
\mathbf i_i.
$$

建模：

$$
\mathbf i
=
F(\mathbf y,\mathbf e).
$$

檢驗：

$$
\frac{
\partial I
}{
\partial S
}
$$

是否在高 symptom 區突然改變。

---

# 58. 實驗三：Threshold Robustness

對同一 dataset 改變：

$$
\theta_D.
$$

觀察：

- classification stability；
- impairment prediction；
- treatment response；
- false positive／negative trade-off。

如果小幅 threshold change 造成 outcome validity 崩潰，現行 boundary 需要更多研究。

---

# 59. 實驗四：Normative Configuration Modeling

建立：

$$
p_{\text{ref}}(\mathbf c\mid age,sex,\ldots).
$$

計算 individual deviation：

$$
\mathbf z_i.
$$

再測：

$$
\mathbf z_i
\rightarrow
I_i.
$$

不直接用 $\mathbf z$ 做 diagnosis。

---

# 60. 實驗五：Cluster Replication

在 discovery cohort 建：

$$
C_1,\ldots,C_K.
$$

在 external cohort 檢驗：

$$
\operatorname{ARI},
$$

$$
\operatorname{NMI},
$$

$$
\operatorname{stability}.
$$

若 cluster 不可外部重現，不應稱 biotype。

---

# 61. 實驗六：Longitudinal Boundary Crossing

追蹤：

$$
\mathbf c_t,
\mathbf y_t,I_t,\Gamma_t.
$$

檢查：

$$
\Gamma_t:
0\rightarrow1
$$

時，底層 configuration 是否真的出現非連續改變。

若沒有：

$$
\boxed{
\text{diagnostic transition}
\neq
\text{configuration phase transition}.
}
$$

---

# 62. 實驗七：Subthreshold Outcome Study

建立：

1. low-trait controls；
2. subthreshold traits without impairment；
3. subthreshold traits with impairment；
4. clinical ADHD。

比較：

- course；
- function；
- help-seeking；
- comorbidity；
- intervention needs。

這可以真正回答：

$$
\text{subthreshold}
$$

是否具有獨立臨床意義。

---

# 63. 實驗八：Cross-Diagnostic Configuration Mapping

同時納入：

- ADHD；
- autism；
- anxiety；
- depression；
- sleep disorders；
- controls。

建立：

$$
\Omega_C.
$$

檢驗：

$$
\text{shared dimensions}
$$

與：

$$
\text{diagnosis-specific combinations}.
$$

---

# 64. 實驗九：Treatment-Outcome Geometry

測：

$$
P
\left(
R_{\text{treat}}
\mid
\mathbf c
\right).
$$

若 configuration space 能預測 treatment response，而 diagnosis alone 不能，才具有 precision-medicine 潛力。

在此之前：

$$
\boxed{
\text{configuration model}
\neq
\text{treatment selector}.
}
$$

---

# 65. 模型失敗條件

CCSH 應被削弱，如果：

1. ADHD-related trait distributions 反覆呈現清晰自然雙峰；
2. symptom–impairment relation 在獨立樣本中存在穩定自然斷點；
3. 單一 scalar model 已足以解釋 cognition、impairment 與 course；
4. clusters 無法外部重現；
5. high-dimensional model 嚴重 overfit；
6. subthreshold group 與 low-trait controls 在所有 clinically relevant outcomes 都無差異；
7. configuration variables 無法提高 treatment／course prediction；
8. dimensional measurements 無法跨文化或跨年齡穩定操作化。

若：

$$
P_{\text{CCSH,out}}
\leq
P_{\text{binary,out}},
$$

且：

$$
P_{\text{CCSH,out}}
\leq
P_{\text{single-axis,out}},
$$

則高維模型沒有保留必要。

---

# 66. 最重要反例一：Formal ADHD Diagnosis 仍有 Validity

2024 Nature Reviews Disease Primers 等現代綜述仍強調：

$$
\boxed{
\text{standard diagnostic criteria can identify
a reliable and clinically meaningful ADHD syndrome}.
}
$$

所以本文不是：

$$
\text{ADHD diagnosis is arbitrary and meaningless}.
$$

更精確：

$$
\boxed{
\text{the underlying liability may be continuous
while the diagnostic construct remains clinically valid}.
}
$$

---

# 67. 最重要反例二：不是所有 Continuum 都必須是一維

2025 adult twin data 正好顯示：

$$
\text{general dimension}
+
\text{secondary dimensions}.
$$

因此本文拒絕：

$$
\boxed{
\text{ADHD spectrum}
=
\text{one straight line}.
}
$$

---

# 68. 最重要反例三：Biotype Evidence 不等於終結 Spectrum

2026 JAMA study 的 clustering 建立在：

$$
\text{normative dimensional deviations}
$$

之上。

所以其方法本身說明：

$$
\boxed{
\text{clusters can emerge inside a dimensional framework}.
}
$$

這不是 category 對 dimension 的勝利。

---

# 69. 最重要反例四：Subthreshold 不是偷渡診斷

即使：

$$
I>0
$$

且：

$$
\Gamma=0,
$$

也不能由本文推出：

$$
\Gamma\text{ 應改成 }1.
$$

臨床可能需要：

- 重新評估；
- 其他診斷；
- 非診斷型支持；
- 追蹤；
- 環境調整。

所以：

$$
\boxed{
\text{need for help}
\neq
\text{need for a specific diagnosis}.
}
$$

---

# 70. 與前七篇整合

第 1 篇提出：

$$
\mathbf C_t
=
\text{dynamic configuration}.
$$

第 2–6 篇逐層展開：

$$
\mathbf N_t,
\mathbf Z_t,
\Pi_t,
\mathbf X_t,
\mathcal G_t,
Q_t,
\widehat P_t,
P_t.
$$

第 7 篇加入生命史：

$$
D_t,S_t,K_t,V_t.
$$

本篇現在把所有個體狀態嵌入：

$$
\boxed{
\Omega_C
\subseteq
\mathbb R^d.
}
$$

並將臨床 diagnosis 明確放在另一層：

$$
\boxed{
\mathcal D
=
\Gamma
\left(
\mathbf y,
I,
H,
X
\right).
}
$$

因此整套理論第一次明確區分：

$$
\boxed{
\text{ontology of variation}
}
$$

與：

$$
\boxed{
\text{clinical decision rule}.
}
$$

---

# 71. 系列目前的統一表示

底層狀態：

$$
\mathbf c_{i,t}
\in
\Omega_C.
$$

環境耦合：

$$
\mathbf y_{i,t}
=
F
\left(
\mathbf c_{i,t},
\mathbf e_{i,t}
\right).
$$

功能損害：

$$
\mathbf i_{i,t}
=
\Phi
\left(
\mathbf c_{i,t},
\mathbf e_{i,t},
\mathbf d_{i,t}
\right).
$$

臨床判定：

$$
\boxed{
\mathcal D_{i,t}
=
\Gamma
\left(
\mathbf y_{i,t},
\mathbf i_{i,t},
H_i,
X_{i,t}
\right).
}
$$

所以：

$$
\boxed{
\mathbf c
\text{ continuous}
\quad\land\quad
\mathcal D
\text{ categorical}
}
$$

完全可以同時成立。

---

# 72. 本文不主張的內容

本文不主張：

1. ADHD diagnosis 沒有意義；
2. ADHD 不是疾病／障礙；
3. 診斷 threshold 可以任意取消；
4. everyone has ADHD；
5. every ADHD-like trait is pathological；
6. subthreshold 等於 hidden ADHD；
7. near-threshold 等於一定應被診斷；
8. functional impairment 可以忽略；
9. genetics 已證明 ADHD 只有單一 continuum；
10. 2026 biotypes 是 ADHD 最終三分類；
11. brain imaging 已可進行個人 ADHD diagnosis；
12. polygenic scores 已可用於個人 diagnosis；
13. high-dimensional configuration 可取代 DSM／ICD；
14. 診斷 category 與 dimension 必須二選一；
15. shared transdiagnostic traits 代表不同 disorders 都是一樣；
16. statistical atypicality 等於 clinical disorder；
17. clinical diagnosis 等於固定終身身份；
18. 本模型可用來替任何人判斷「接近 ADHD 幾成」。

---

# 73. 結論

「ADHD 是類別還是光譜？」若被理解成二選一，已經不足以描述現有證據。

較完整的模型是：

$$
\boxed{
\text{continuous high-dimensional variation}
+
\text{possible local clusters}
+
\text{categorical clinical decisions}.
}
$$

2024–2025 的 population、QoL、twin 與 GWAS evidence 支持 ADHD-related symptoms 與 liability 的連續性；2026 的 biotype research 又顯示連續 normative deviations 中可以出現可重現局部結構。

因此 clinical ADHD 可以被概念化為：

$$
\boxed{
\text{a clinically meaningful decision region
constructed over continuous and heterogeneous variation},
}
$$

而不是：

$$
\text{a point where human cognition suddenly changes species}.
$$

但這個說法不削弱 diagnosis。

它反而要求更加精確地區分：

$$
\text{trait},
$$

$$
\text{configuration},
$$

$$
\text{impairment},
$$

$$
\text{developmental history},
$$

$$
\text{diagnosis}.
$$

尤其：

$$
\boxed{
\text{subthreshold traits}
\neq
\text{clinical ADHD}.
}
$$

一個人可以具有 ADHD-related traits 而不符合 ADHD；也可以在未達 ADHD 診斷時具有真正需要處理的功能困難。

本文最終提出：

$$
\boxed{
\Omega_C
=
\text{continuous configuration space},
}
$$

$$
\boxed{
\rho(\mathbf c)
=
\text{population density with possible local structure},
}
$$

以及：

$$
\boxed{
\mathcal D
=
\Gamma
\left(
\text{symptoms},
\text{impairment},
\text{history},
\text{context},
\text{differential evidence}
\right).
}
$$

最終可證偽問題是：

$$
\boxed{
\text{Does a high-dimensional continuous-plus-cluster model
predict impairment, course, and treatment-relevant outcomes
better than either a pure binary model
or a pure single-axis spectrum?}
}
$$

如果不能，CCSH 應被簡化。

如果可以，ADHD 就可以同時保持臨床診斷的操作價值，又允許底層研究從二元標籤進入更精細的配置幾何。

---

# 參考文獻

1. Arildskov, T. W., Thomsen, P. H., Sonuga-Barke, E. J. S., Lambek, R., Østergaard, S. D., & Virring, A. Is Attention-Deficit/Hyperactivity Disorder (ADHD) a Dimension or a Category? What Does the Relationship Between ADHD Traits and Psychosocial Quality of Life Tell Us? *Journal of Attention Disorders*. 2024;28(7):1035–1044. DOI: 10.1177/10870547231222228.

2. Arildskov, T. W., Sonuga-Barke, E. J. S., Thomsen, P. H., Virring, A., & Østergaard, S. D. How much impairment is required for ADHD? No evidence of a discrete threshold. *Journal of Child Psychology and Psychiatry*. 2022;63(2):229–237. DOI: 10.1111/jcpp.13440.

3. van der Laan, C. M., Ip, H. F., Schipper, M., et al. Genome-wide association meta-analysis of childhood ADHD symptoms and diagnosis identifies new loci and potential effector genes. *Nature Genetics*. 2025;57:2427–2435. DOI: 10.1038/s41588-025-02295-y.

4. Knyspel, J., Morneau-Vaillancourt, G., & Eley, T. C. Using Bifactor Twin Modeling to Assess the Genetic and Environmental Dimensionality of Adult ADHD Symptoms. *Behavior Genetics*. 2025;55:1–11. DOI: 10.1007/s10519-024-10204-y.

5. Pan, N., Long, Y., Qin, K., et al. Mapping ADHD Heterogeneity and Biotypes by Topological Deviations in Morphometric Similarity Networks. *JAMA Psychiatry*. 2026;83(5):478–490. DOI: 10.1001/jamapsychiatry.2026.0001.

6. Schork, A. J., et al. Polygenic profiles define aspects of clinical heterogeneity in attention deficit hyperactivity disorder. *Nature Genetics*. 2024;56:234–244. DOI: 10.1038/s41588-023-01593-7.

7. Cortese, S., Bellgrove, M. A., Brikell, I., Franke, B., Goodman, D. W., Hartman, C. A., et al. Attention-deficit/hyperactivity disorder (ADHD) in adults: evidence base, uncertainties and controversies. *World Psychiatry*. 2025;24(3):347–371. DOI: 10.1002/wps.21374.

8. Ogundele, M. O., et al. Subthreshold Autism and ADHD: A Brief Narrative Review for Frontline Clinicians. *Pediatric Reports*. 2025;17(2):42.

9. Fuermaier, A. B. M., Gontijo-Santos Lima, C., & Tucha, O. Impairment Assessment in Adult ADHD and Related Disorders: Current Opinions From Clinic and Research. *Journal of Attention Disorders*. 2024;28(12):1529–1541. DOI: 10.1177/10870547241261598.

10. Faraone, S. V., et al. Attention-deficit/hyperactivity disorder. *Nature Reviews Disease Primers*. 2024;10:11. DOI: 10.1038/s41572-024-00495-0.

11. Mattheisen, M., et al. Differences in the genetic architecture of common and rare variants in childhood, persistent and late-diagnosed attention-deficit hyperactivity disorder. *Nature Genetics*. 2022.

12. World Health Organization. *ICD-11 for Mortality and Morbidity Statistics*. Attention deficit hyperactivity disorder classification. Accessed 2026-08-17.

---

# 文獻使用聲明

本文僅使用上述研究建立截至 2026-08-17 的外部實證邊界。

本文提出的 CCSH、configuration space $\Omega_C$ 、configuration density $\rho(\mathbf c)$ 、clinical decision operator $\Gamma$ 、subthreshold region $\mathcal R_{\text{sub}}$ 、impairment surface $\Phi(\mathbf c,\mathbf e)$ 、continuous-plus-cluster model 與 multi-layer geometry，均為本文理論構件，不應被誤認為上述研究作者的原始結論。

不同研究包含一般人口學童、成人 twins、clinical ADHD、pediatric neuroimaging cohorts、genetic cohorts、professional surveys 與 narrative reviews。本文不把它們視為單一大型實驗的直接累加證據。

---

**狀態：** v0.1，理論稿  
**新增原始臨床／人體數據：** 無  
**醫學用途：** 無  
**下一篇：** 《情境匹配與性能反轉：ADHD 配置何時成為障礙，何時可能成為優勢？》
