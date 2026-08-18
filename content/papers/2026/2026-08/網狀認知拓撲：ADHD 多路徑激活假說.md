# 網狀認知拓撲：ADHD 多路徑激活假說

**英文題名：** Networked Cognitive Topology: A Multi-Path Activation Conjecture for ADHD  
**系列：** ADHD 動態配置與認知拓撲系列，第 5 篇  
**版本：** v0.1  
**日期：** 2026-08-16  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論建模／認知科學命題／研究綱領  
**文獻檢索截點：** 2026-08-16  

---

# 0. 醫學、神經科學與證據邊界聲明

本文不是臨床研究、診斷工具、治療指南、神經影像研究、藥理研究或醫療建議。

本文提出的「網狀認知拓撲」「多路徑激活」「路徑多樣性」「跨路徑一致性」「稀疏提示優勢」等概念均屬待驗證理論命題，不代表已被醫學界、神經科學界或認知科學界確認的 ADHD 病理機制。

原作者並非醫學、精神醫學、神經科學或臨床心理專業研究者。本文不提供新的臨床、人體、神經影像、藥理或心理實驗數據；所有實證性背景均來自公開同行評審研究。本文新增內容僅屬理論整合、形式化與可證偽研究綱領。

本文特別禁止以下偷換：

$$
\boxed{
\text{brain functional network topology}
\neq
\text{cognitive-associative topology}.
}
$$

亦即，fMRI、EEG 或 connectome 中的 graph topology 不能直接被當成「一個人的思考就是網狀」之證據。

本文也不主張：

$$
\text{divergent thinking}
=
\text{networked cognition},
$$

不主張：

$$
\text{mind wandering}
=
\text{multi-path reasoning},
$$

也不主張：

$$
\text{creativity}
=
\text{ADHD}.
$$

本文中的 graph、node、edge、path 均首先是中層認知模型的數學表示，不是對單一神經元、腦區或真實 connectome 的一對一映射。

核心限制：

$$
\boxed{
\text{graph formalization}
\neq
\text{neural identity}.
}
$$

---

# 摘要

本系列前四篇已將 ADHD-related attention 從單一「注意力不足」標量重新展開為神經調節、選擇配置、狀態穩定性、配置熵、切換與脫離等多層動態系統。本篇進一步處理一個更強、也更容易過度推論的命題：部分 ADHD-related cognitive profiles 是否在特定任務中具有較廣的聯想擴散、較高的候選路徑多樣性、較弱的既有範例約束，並因此呈現不同於單一路徑序列處理的「網狀認知拓撲」？

已有文獻提供若干間接支持。White 與 Shah 於 2016 年在大學生 ADHD 樣本中研究 semantic activation scope 與 innovative thinking，結果支持 ADHD 與特定創新思考表現的正向關聯，且較廣的 semantic activation 可能參與其中。其後對成人 ADHD 的 unconstrained creative generation 研究亦發現，ADHD 參與者在 alien-fruit 與 product-label tasks 中較少受既有範例與既有概念框架約束。2022 年一項 population-based sample 與 adult ADHD case-control sample 的整合研究發現，ADHD symptoms 與 divergent-thinking fluency、flexibility、originality 呈正相關，但與 convergent thinking 無明顯關聯；將臨床與非臨床樣本合併後，關係呈現平台化或近似倒 U 型，而不是症狀越高、創造力越高。

然而，2026 年成人 ADHD strengths scoping review 同時指出：creativity 雖是最常被研究與提及的潛在優勢之一，但現有研究高度異質、測量品質不一，clinical ADHD 與 creativity 的關係並不一致，且 direct neuroimaging evidence 仍不足。該 review 亦明確表示其目的在於 mapping field，而非建立因果或驗證構念。2026 年青少年與成人研究持續發現 ADHD 與 mind wandering 的關聯，但 mind wandering 僅表示 task-unrelated 或 internally generated thought 的增加，不能直接推出結構化多路徑推理。

因此本文提出較弱的「Networked Cognitive Topology Hypothesis, NCTH」：

$$
\boxed{
\text{Some ADHD-related cognitive profiles may show
greater associative breadth or path diversity
under specific tasks,
without implying universally superior reasoning.}
}
$$

本文將當下認知候選空間表示為圖：

$$
\mathcal G_t
=
\left(
V_t,
E_t,
W_t
\right),
$$

並將輸入刺激造成的候選激活表示為：

$$
\mathbf a_{t+1}
=
\sigma
\left(
\eta W_t\mathbf a_t
+
\mathbf u_t
-
\mathbf h_t
\right).
$$

其中多路徑認知的價值不由「激活越多」決定，而由至少四個變量共同決定：

$$
\boxed{
\text{Breadth}
+
\text{Path Diversity}
+
\text{Coherence}
+
\text{Convergence}.
}
$$

若廣泛激活缺乏一致性與收斂，則可能增加噪音、干擾與錯誤；只有當多條路徑可被交叉驗證、淘汰、整合並輸出時，才可能形成任務優勢。

本文最後提出十一項可證偽命題，以及 semantic priming、free association graph、sparse causal completion、scaffold interference、divergent–convergent switching 與 longitudinal state tracking 等實驗設計。若這些 graph-derived 指標不能在獨立樣本中提供超越一般 executive-function、working-memory、IQ 與 symptom measures 的增量預測力，則「網狀認知拓撲」應被視為冗餘比喻而放棄。

**關鍵詞：** ADHD、認知拓撲、semantic activation、divergent thinking、associative breadth、multi-path activation、mind wandering、創造力、因果補完、graph model

---

# 1. 為什麼需要重寫「網狀思維」？

本系列早期理論曾使用「網狀思維」描述一種主觀與任務上的現象：

- 多個關聯快速出現；
- 不一定沿單一路徑逐步展開；
- 稀疏提示有時已足以引出完整結構；
- 過多連接詞或預先指定路徑可能成為冗餘；
- 多個候選解可同時被考慮；
- 最後再進行交叉驗證與收斂。

這些現象可以形成研究假說。

但若直接寫成：

$$
\text{ADHD}
=
\text{networked thinking},
$$

會犯下至少四個錯誤。

第一，ADHD 高度異質。

第二，「網狀思維」缺乏標準操作定義。

第三，brain network 與 cognitive network 容易被混為一談。

第四，較多聯想不等於較好的推理。

因此本文不是保留舊命題，而是將它降階為：

$$
\boxed{
\text{conditional multi-path activation hypothesis}.
}
$$

---

# 2. 第一個邊界：Brain Network 不等於 Cognitive Topology

神經影像研究常把腦區作為 node，把 functional connectivity 作為 edge。

可以表示為：

$$
\mathcal G_t^{\text{brain}}
=
\left(
V_t^{B},
E_t^{B},
W_t^{B}
\right).
$$

本文提出的認知圖則是：

$$
\mathcal G_t^{\text{cog}}
=
\left(
V_t^{C},
E_t^{C},
W_t^{C}
\right).
$$

其中 node 可以暫時表示：

- concept；
- memory trace；
- causal proposition；
- candidate interpretation；
- action hypothesis。

因此：

$$
\boxed{
\mathcal G_t^{\text{brain}}
\neq
\mathcal G_t^{\text{cog}}.
}
$$

兩者未來可以研究 mapping：

$$
\mathcal M:
\mathcal G^{\text{brain}}
\rightarrow
\mathcal G^{\text{cog}},
$$

但不能預設：

$$
\mathcal M
=
\text{identity}.
$$

---

# 3. 第二個邊界：Semantic Activation 不等於 Reasoning

一個詞語輸入後可以激活多個相關概念。

例如：

$$
v_{\text{storm}}
$$

可能激活：

$$
\left\{
v_{\text{rain}},
v_{\text{wind}},
v_{\text{flood}},
v_{\text{evacuation}},
v_{\text{power outage}}
\right\}.
$$

這只表示：

$$
\text{association activation}.
$$

不表示：

$$
\text{causal reasoning}.
$$

因果推理至少需要：

$$
\text{direction},
$$

$$
\text{compatibility},
$$

$$
\text{constraint},
$$

$$
\text{counterfactual support},
$$

或其他更強結構。

因此：

$$
\boxed{
\text{more activated concepts}
\neq
\text{more valid reasoning}.
}
$$

---

# 4. 既有重要證據：Semantic Activation Scope

White 與 Shah 於 2016 年研究 college students with ADHD，使用 realistic innovation task 與 word-association measure 探討 innovative thinking 及可能的 cognitive mechanism。

該研究支持：

$$
\text{ADHD}
\leftrightarrow
\text{specific innovative-thinking advantages}
$$

以及：

$$
\text{wider semantic activation}
$$

可能參與其中。

這是目前與本文「較廣候選激活」最直接接近的歷史實證之一。

但該研究不能證明：

$$
\text{ADHD cognition is graph-parallel}.
$$

它最多支持：

$$
\boxed{
\text{broader semantic spread is empirically plausible
in at least some ADHD adult samples}.
}
$$

---

# 5. Conceptual Expansion 與較弱範例約束

White 後續研究比較 ADHD 與 non-ADHD adults 在 creative-generation tasks 中受到既有範例與知識結構的限制程度。

在 alien-fruit invention 與 product-label generation 中，ADHD 組產生的結果較偏離既有 Earth-fruit characteristics，也較少沿用 task examples。

這可被理解為：

$$
\text{constraint adherence}
\downarrow
$$

或：

$$
\text{conceptual expansion}
\uparrow.
$$

但兩者仍不等同於：

$$
\text{path diversity}.
$$

因為一個人可以只沿單一路徑走得很遠，也可以同時激活多條路徑。

所以本文把：

$$
\text{constraint escape}
$$

與：

$$
\text{multi-path activation}
$$

分開。

---

# 6. Divergent Thinking 是接近概念，但不是同義詞

Divergent thinking 常被操作化為：

- fluency；
- flexibility；
- originality。

它最接近：

$$
\text{candidate generation}.
$$

而本文的 networked cognition 還需要：

$$
\text{relation structure}
$$

與：

$$
\text{cross-path interaction}.
$$

因此：

$$
\boxed{
\text{divergent thinking}
\neq
\text{networked cognition}.
}
$$

Divergent thinking 可以作為多路徑假說的部分 observable proxy，但不是充分證據。

---

# 7. 2022 年結果：展開與收斂不能混在一起

Stolte 等人的 2022 研究同時使用：

- Alternative Uses Task；
- Remote Associates Test；
- Creative Achievement Questionnaire；
- population-based sample；
- adult ADHD case-control sample。

在一般人口中，較多 ADHD symptoms 與：

$$
\text{fluency},
$$

$$
\text{flexibility},
$$

$$
\text{originality}
$$

呈小幅正相關。

但沒有對：

$$
\text{convergent thinking}
$$

得到相同關係。

更重要的是，將 population 與 clinical case-control data 合併後，quadratic model 對 divergent thinking 的擬合優於單純 linear model，提示：

$$
\boxed{
\text{more ADHD symptoms}
\not\Rightarrow
\text{indefinitely more divergent thinking}.
}
$$

關係可能在臨床區域平台化。

因此本文明確分離：

$$
\mathcal D
=
\text{divergent expansion},
$$

與：

$$
\mathcal K
=
\text{convergent closure}.
$$

真正可用的問題解法需要：

$$
\boxed{
\mathcal D
+
\mathcal K.
}
$$

---

# 8. 2026 Strengths Review 的重要警告

2026 年 Rafael 等人的成人 ADHD strengths scoping review 納入 125 項研究：

- 61 qualitative；
- 59 quantitative；
- 5 mixed methods。

Creativity 是最常被研究或提及的 strength category。

但該 review 也明確指出：

1. 研究高度異質；
2. creativity measures 差異很大；
3. 既有 reviews 曾指出研究品質問題；
4. 很多 included studies 依賴 self-report 或 screening，而非 verified diagnosis；
5. scoping review 本身不是 causation、correlation 或 construct-validity review；
6. 直接連結 ADHD brain differences 與 creativity 的 neuroimaging evidence 仍不足。

所以本文不能用：

$$
\text{many creativity papers}
$$

推出：

$$
\text{networked cognition confirmed}.
$$

最合理的結論只是：

$$
\boxed{
\text{the hypothesis space is legitimate,
but the mechanism remains open}.
}
$$

---

# 9. Mind Wandering 提供「內部生成」證據，但不提供結構證據

2026 年青少年 ADHD 臨床樣本研究顯示，ADHD 組 self-reported mind wandering 顯著高於 psychiatric non-ADHD comparison group。

同年成人研究亦持續發現 spontaneous mind-wandering measures 可預測 ADHD-related dimensions。

因此：

$$
\text{internally generated thought}
\uparrow
$$

在 ADHD-related cognition 中具有研究支持。

但是：

$$
\boxed{
\text{mind wandering}
\neq
\text{structured multi-path reasoning}.
}
$$

Mind wandering 可以是：

- 單一內在敘事；
- 隨機跳轉；
- rumination；
- fantasy；
- goal-related incubation；
- unrelated thought sequence。

只有部分情況可能形成有用的多路徑探索。

---

# 10. Parallel Activation 不等於 Parallel Conscious Reasoning

本文使用：

$$
\text{parallel activation}
$$

時只表示：

> 多個候選表徵在相近時間窗內具有可測非零激活或可提取性。

它不主張：

$$
\boxed{
\text{multiple fully conscious reasoning streams
are executed simultaneously}.
}
$$

認知系統可以：

1. 快速輪轉；
2. 部分重疊激活；
3. 非意識並行；
4. 工作記憶序列化；

而在主觀上被感受為「同時想到很多」。

所以未來研究需要分辨：

$$
\text{true parallelism}
$$

與：

$$
\text{rapid multiplexed switching}.
$$

---

# 11. 認知圖的最小定義

本文定義時間 $t$ 的候選認知圖：

$$
\mathcal G_t
=
\left(
V_t,
E_t,
W_t
\right).
$$

其中：

$$
V_t
=
\left\{
v_1,\ldots,v_n
\right\}
$$

為當下可激活概念／命題節點。

$$
E_t
\subseteq
V_t\times V_t
$$

為候選關係。

$$
W_t
=
\left[
w_{ij}(t)
\right]
$$

為關係強度矩陣。

edge 可以依任務標記不同類型：

$$
E_t
=
E_t^{\text{semantic}}
\cup
E_t^{\text{causal}}
\cup
E_t^{\text{temporal}}
\cup
E_t^{\text{analogical}}
\cup
E_t^{\text{goal}}.
$$

不同 edge type 不應被混為同一關係。

---

# 12. 激活向量

令：

$$
\mathbf a_t
=
\left(
a_1(t),
a_2(t),
\ldots,
a_n(t)
\right)^{\top}.
$$

候選擴散模型：

$$
\mathbf a_{t+1}
=
\sigma
\left(
\eta W_t\mathbf a_t
+
\mathbf u_t
-
\mathbf h_t
\right).
$$

其中：

- $\eta$：擴散 gain；
- $\mathbf u_t$：外部／內部輸入；
- $\mathbf h_t$：抑制與競爭；
- $\sigma$：飽和非線性。

此式不是神經生理定律。

它只用來定義：

$$
\text{association spread}.
$$

---

# 13. Activation Breadth

設定激活閾值：

$$
\theta_a.
$$

定義有效激活集合：

$$
V_t^{+}
=
\left\{
v_i
\mid
a_i(t)\geq\theta_a
\right\}.
$$

激活廣度：

$$
B_t
=
\left|
V_t^{+}
\right|.
$$

亦可正規化：

$$
\widehat B_t
=
\frac{
|V_t^{+}|
}{
|V_t|
}.
$$

NCTH 不預測所有 ADHD individuals：

$$
B_t
>
B_t^{\text{control}}.
$$

它只提出：

$$
\boxed{
B_t
\text{ may differ by profile and task}.
}
$$

---

# 14. Activation Radius

若輸入節點集合為：

$$
V_t^{\text{seed}},
$$

定義 graph distance：

$$
d_{\mathcal G}(u,v).
$$

則平均激活半徑：

$$
R_{\text{act}}
=
\frac{
1
}{
|V_t^{+}|
}
\sum_{v\in V_t^{+}}
\min_{s\in V_t^{\text{seed}}}
d_{\mathcal G}(s,v).
$$

較大的：

$$
R_{\text{act}}
$$

表示激活延伸至較遠概念區域。

2016 semantic-activation 結果最接近這類候選變量。

---

# 15. Branching Factor

對當下 activation frontier：

$$
F_t,
$$

定義平均候選分支：

$$
b_t
=
\frac{
1
}{
|F_t|
}
\sum_{v\in F_t}
\deg^{+}(v).
$$

高：

$$
b_t
$$

可以增加候選數。

但也增加：

$$
\text{search cost}.
$$

因此：

$$
\boxed{
b_t\uparrow
\not\Rightarrow
P_t\uparrow.
}
$$

---

# 16. 多路徑集合

對問題起點：

$$
s
$$

與目標：

$$
g,
$$

定義候選路徑集合：

$$
\mathcal P_t(s,g)
=
\left\{
p_1,p_2,\ldots,p_m
\right\}.
$$

每條路徑：

$$
p_k
=
\left(
v_{k,1},
v_{k,2},
\ldots,
v_{k,\ell_k}
\right).
$$

單一路徑處理：

$$
|\mathcal P_t|
\approx1.
$$

多路徑候選：

$$
|\mathcal P_t|
>1.
$$

但路徑數本身沒有品質含義。

---

# 17. Path Diversity

若兩條路徑的 edge sets 為：

$$
E(p_i),
E(p_j),
$$

定義 Jaccard distance：

$$
d_J(p_i,p_j)
=
1-
\frac{
|E(p_i)\cap E(p_j)|
}{
|E(p_i)\cup E(p_j)|
}.
$$

平均路徑多樣性：

$$
D_P
=
\frac{
2
}{
m(m-1)
}
\sum_{i<j}
d_J(p_i,p_j).
$$

當：

$$
D_P\uparrow,
$$

表示候選解使用更不同的關係路徑。

這比單純：

$$
m\uparrow
$$

更接近「真的從不同方向思考」。

---

# 18. Semantic Distance 與 Path Diversity 不同

semantic distance 可以很遠，但仍沿單一路徑。

例如：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
D
\rightarrow
E.
$$

其：

$$
R_{\text{act}}
$$

可能很高，

但：

$$
D_P
$$

可以很低。

因此：

$$
\boxed{
\text{wide association}
\neq
\text{multi-route processing}.
}
$$

NCTH 必須分別測兩者。

---

# 19. Path Coherence

每條路徑需要內部一致。

定義：

$$
C(p_k)
=
\frac{
1
}{
\ell_k-1
}
\sum_{r=1}^{\ell_k-1}
q
\left(
v_{k,r},
v_{k,r+1}
\right),
$$

其中：

$$
q(u,v)\in[0,1]
$$

表示該 edge 在任務域中的合法性、因果支持或語義相容度。

整體 coherence：

$$
\overline C_P
=
\frac{1}{m}
\sum_{k=1}^{m}
C(p_k).
$$

因此：

$$
\boxed{
\text{many paths}
+
\text{low coherence}
=
\text{noise},
}
$$

而不是優勢。

---

# 20. Cross-Path Consistency

若多條路徑最後對同一 latent conclusion：

$$
z
$$

提供支持，可以定義：

$$
X_P(z)
=
\frac{
1
}{
m
}
\sum_{k=1}^{m}
\operatorname{Support}
\left(
p_k,z
\right).
$$

高：

$$
X_P
$$

表示不同路徑對同一結論具有收斂支持。

這就是舊「交叉驗證」直覺的可操作化候選。

---

# 21. Convergence Efficiency

多路徑激活後仍必須選擇輸出。

令初始候選數：

$$
m_0.
$$

在時間：

$$
T_c
$$

後收斂至：

$$
m_f.
$$

定義：

$$
E_{\text{conv}}
=
\frac{
m_0-m_f
}{
T_c+\varepsilon
}.
$$

如果：

$$
m_0\uparrow
$$

但：

$$
E_{\text{conv}}\downarrow,
$$

則可能出現：

- indecision；
- topic drift；
- unresolved branching；
- overload。

所以：

$$
\boxed{
\text{divergence without convergence}
\neq
\text{effective reasoning}.
}
$$

---

# 22. Networked Cognition 的候選有效值

定義：

$$
N_{\text{eff}}
=
\alpha B
+
\beta D_P
+
\gamma\overline C_P
+
\delta X_P
+
\zeta E_{\text{conv}}
-
\lambda N_{\text{noise}}
-
\kappa C_{\text{search}}.
$$

其中：

- $B$：activation breadth；
- $D_P$：path diversity；
- $\overline C_P$：path coherence；
- $X_P$：cross-path consistency；
- $E_{\text{conv}}$：convergence efficiency；
- $N_{\text{noise}}$：無效候選；
- $C_{\text{search}}$：搜尋成本。

因此：

$$
\boxed{
\text{networked cognition quality}
\neq
\text{number of associations}.
}
$$

---

# 23. 兩種相反失敗：Under-Expansion 與 Over-Expansion

## 23.1 Under-Expansion

$$
B\downarrow,
$$

$$
D_P\downarrow.
$$

可能造成：

- 解空間過窄；
- 過早收斂；
- 類比不足；
- 創新不足。

## 23.2 Over-Expansion

$$
B\uparrow,
$$

但：

$$
\overline C_P\downarrow,
$$

$$
E_{\text{conv}}\downarrow.
$$

可能造成：

- 噪音；
- 跳題；
- 無法收斂；
- 工作記憶超載。

因此最佳區域可能是：

$$
\boxed{
B^{*},
D_P^{*},
C_P^{*},
E_{\text{conv}}^{*}
}
$$

的任務依賴工作區，而不是無限擴展。

---

# 24. 稀疏提示假說

舊模型的一個重要直覺是：

> 對某些網狀處理者，稀疏但高信息量節點可能比大量顯式連接詞更容易觸發整體結構。

本文將其改寫成可證偽命題。

設兩種輸入：

$$
I_{\text{sparse}}
$$

與：

$$
I_{\text{scaffolded}}.
$$

前者保留主要 content nodes，後者加入更多關係提示與連接詞。

定義：

$$
P_{\text{completion}}
\left(
I
\right)
$$

為正確補完表現。

NCTH 不預測 ADHD 一定：

$$
P_{\text{sparse}}
>
P_{\text{scaffolded}}.
$$

只預測某一 latent profile：

$$
\mathcal L_{\text{networked}}
$$

可能出現：

$$
\boxed{
\Delta P
=
P_{\text{sparse}}
-
P_{\text{scaffolded}}
>
0.
}
$$

此 latent profile 是否與 ADHD 富集，是實驗問題。

---

# 25. Scaffold Interference

顯式 scaffold 可以降低搜索空間。

但如果主體已經快速形成多條候選路徑，額外 scaffold 可能：

- 強迫單一路徑；
- 增加語言解析負荷；
- 抑制 alternative routes；
- 造成 redundant processing。

定義 scaffold cost：

$$
C_{\text{scaf}}
=
P_{\text{free}}
-
P_{\text{forced-route}}.
$$

如果：

$$
C_{\text{scaf}}>0,
$$

表示該 scaffold 對特定任務與個體造成干擾。

這是可測個體差異，不是 ADHD 的預設特徵。

---

# 26. 因果補完比創造力更接近本理論

Creativity 太寬。

本文真正要檢驗的是：

$$
\text{structured completion under sparse constraints}.
$$

例如輸入：

$$
\left\{
\text{prey decrease},
\text{predator hunger},
\text{migration},
\text{balance recovery}
\right\}.
$$

受試者需要重建：

$$
\text{causal paths}.
$$

而不是只產生最多想法。

所以核心 outcome 應包含：

- causal accuracy；
- number of valid paths；
- path diversity；
- convergence time；
- confidence calibration；
- false-path rate。

---

# 27. 多路徑並不必然並行

若候選路徑：

$$
p_1,p_2,p_3
$$

都在短時間內被產生，可能有兩種實作：

## 27.1 True parallel candidate activation

$$
p_1\parallel p_2\parallel p_3.
$$

## 27.2 Rapid serial multiplexing

$$
p_1
\rightarrow
p_2
\rightarrow
p_3
\rightarrow
p_1
\rightarrow\cdots
$$

行為上兩者可能很像。

因此 NCTH 不把：

$$
\text{subjective simultaneity}
$$

當成 parallelism 的證據。

需要：

- millisecond-level neural measurements；
- interference paradigms；
- dual-route priming；
- computational model comparison；

才能區分。

---

# 28. Creativity 的倒 U 提供一個重要一般原理

2022 結果提示：

$$
\text{ADHD symptoms}
\rightarrow
\text{divergent thinking}
$$

可能不是線性無界增加。

本文將此抽象成：

$$
P_{\text{div}}
=
f
\left(
B,
D_P,
C_P,
E_{\text{conv}}
\right).
$$

若 breadth 與 path diversity 太低，探索不足。

若太高而 coherence 與 convergence 不足，performance 也可能下降。

因此候選函數可能具有：

$$
\boxed{
\text{intermediate optimum}.
}
$$

這比：

$$
\text{more chaos}
=
\text{more creativity}
$$

嚴格得多。

---

# 29. Network Topology 與 Creativity 必須再分離一次

一個人可以具有：

$$
D_P\uparrow
$$

但創造性輸出仍低。

原因可能是：

- domain knowledge 不足；
- convergence 差；
- output skill 不足；
- motivation 低；
- external opportunity 缺乏。

反過來，高度創造者也可能透過：

- 深厚專業知識；
- deliberate search；
- analogical expertise；

產生高創造力，而不具有 ADHD-related traits。

所以：

$$
\boxed{
\text{networked cognition}
\neq
\text{creativity}.
}
$$

---

# 30. ADHD Strengths 不能被本體化

2026 scoping review 中，creativity 是最常見 category，interest-based attention、flexibility、uniqueness 等也被大量提及。

但 review 同時強調：

$$
\boxed{
\text{reported strength}
\neq
\text{ADHD-caused strength}.
}
$$

這些 strength 可能來自：

- neurodevelopmental trait；
- learned compensation；
- environmental selection；
- identity；
- occupational niche；
- survivorship bias。

因此 NCTH 不把任何「優勢」寫成 ADHD 本體。

---

# 31. 任務依賴性

定義任務：

$$
T.
$$

其理想拓撲需求：

$$
\Theta_T^{*}
=
\left(
B_T^{*},
D_{P,T}^{*},
C_{P,T}^{*},
E_{\text{conv},T}^{*}
\right).
$$

個體實際狀態：

$$
\Theta_i.
$$

Mismatch：

$$
M_T
=
d
\left(
\Theta_i,
\Theta_T^{*}
\right).
$$

performance：

$$
P_i(T)
=
P_{\max}(T)
-
\lambda M_T.
$$

因此：

- ideation task 可能偏好高 $B$ 、高 $D_P$ ；
- proofreading 可能偏好低噪音；
- emergency diagnosis 可能需要 breadth 加快速 convergence；
- repetitive procedure 可能偏好穩定單一路徑。

所以：

$$
\boxed{
\text{topological advantage}
=
\text{task-relative advantage}.
}
$$

---

# 32. 從「線性 vs 網狀」改成連續配置空間

本文放棄硬二分：

$$
\text{linear thinker}
\lor
\text{network thinker}.
$$

改成：

$$
\Theta_i
=
\left(
B_i,
R_{\text{act},i},
D_{P,i},
C_{P,i},
X_{P,i},
E_{\text{conv},i}
\right).
$$

因此：

$$
\boxed{
\text{networkedness}
=
\text{multidimensional profile}.
}
$$

一個人可以：

- breadth 高；
- path diversity 高；
- convergence 也高；

另一個人可以：

- breadth 高；
- coherence 低；
- convergence 低。

兩者不能都只叫「網狀」。

---

# 33. Latent Networked Profile

本文定義潛在 profile：

$$
\mathcal L_N
$$

而不直接定義 ADHD profile。

例如：

$$
P
\left(
\mathcal L_N
\mid
ADHD
\right)
>
P
\left(
\mathcal L_N
\mid
control
\right)
$$

才是需要未來資料檢驗的命題。

這比：

$$
ADHD
=
\mathcal L_N
$$

弱很多，也合理很多。

---

# 34. NCTH 十一項可證偽命題

## NC-H1：Semantic Breadth 命題

部分 ADHD-related profiles 在 semantic activation tasks 中可能呈現：

$$
B\uparrow
$$

或：

$$
R_{\text{act}}\uparrow.
$$

若大型 clinical replications 不支持，則此命題削弱。

---

## NC-H2：Path Diversity 命題

某些 profiles 的差異不只在想法數量，而在：

$$
D_P\uparrow.
$$

若 path diversity 不提供增量信息，則刪除。

---

## NC-H3：非全域優勢命題

$$
B\uparrow
$$

不保證：

$$
P\uparrow.
$$

優勢需要 coherence 與 convergence。

---

## NC-H4：Sparse-Cue Interaction 命題

部分 profiles 在 sparse but informative inputs 下可能相對表現更佳。

這是 interaction：

$$
\text{Profile}
\times
\text{Input Structure}.
$$

不是主效應。

---

## NC-H5：Scaffold Interference 命題

過度指定 relation path 可能對部分 high-diversity profiles 產生：

$$
C_{\text{scaf}}>0.
$$

---

## NC-H6：Expansion–Closure 分離命題

Divergent expansion 與 convergent closure 是不同能力。

$$
\mathcal D
\neq
\mathcal K.
$$

---

## NC-H7：Mind-Wandering 非等同性命題

Mind wandering 可以增加 internal candidate generation，但：

$$
MW
\neq
NCTH.
$$

---

## NC-H8：Brain–Cognition 非等同性命題

functional-connectivity topology 不能單獨驗證 cognitive graph topology。

---

## NC-H9：倒 U 命題

部分任務可能存在：

$$
B^{*}
$$

或：

$$
D_P^{*}
$$

最佳區，而非單調越高越好。

---

## NC-H10：Profile 富集命題

若 NCTH 與 ADHD 有關，則 latent networked profile 在 ADHD population 中應有統計富集，但不要求人人存在。

---

## NC-H11：增量價值命題

若 graph-derived variables 在控制：

- IQ；
- working memory；
- executive function；
- language ability；
- symptom severity；

後不能提高 out-of-sample prediction，則 NCTH 應被視為冗餘。

---

# 35. 實驗一：Semantic Spreading Activation

使用：

- cue word；
- near associate；
- remote associate；
- unrelated distractor。

測量：

$$
RT(d),
$$

其中：

$$
d
$$

為 semantic distance。

若 activation spread 較廣，可能出現較遠距離的 priming effect。

核心比較：

$$
RT_{\text{remote}}
-
RT_{\text{near}}.
$$

需要控制：

- vocabulary；
- IQ；
- language proficiency；
- medication；
- sleep；
- age。

---

# 36. 實驗二：Free Association Graph

對同一 cue 連續產生 associations。

建立個體 semantic graph：

$$
\mathcal G_i^{\text{assoc}}.
$$

測量：

- node count；
- degree distribution；
- average semantic distance；
- clustering coefficient；
- path diversity；
- repetition；
- off-domain drift。

但：

$$
\mathcal G_i^{\text{assoc}}
$$

仍然只是 behavioral graph，不是 brain graph。

---

# 37. 實驗三：Sparse Causal Completion

建立三種 stimulus：

## Condition A：Full Scaffold

因果連接詞完整。

## Condition B：Partial Scaffold

保留部分關係標記。

## Condition C：Sparse Nodes

只提供核心內容節點。

測量：

$$
T_{\text{completion}},
$$

$$
A_{\text{causal}},
$$

$$
N_{\text{valid paths}},
$$

$$
D_P,
$$

$$
N_{\text{false paths}}.
$$

核心不是問：

> 哪組最快？

而是檢驗：

$$
\text{Profile}
\times
\text{Scaffold Level}.
$$

---

# 38. 實驗四：Constraint Injection

先讓受試者自由形成解。

之後逐步加入：

$$
c_1,c_2,\ldots,c_k
$$

約束。

觀察：

$$
\frac{
\partial D_P
}{
\partial k
}
$$

與：

$$
\frac{
\partial P
}{
\partial k
}.
$$

若某些 profiles 對過早 scaffold 較敏感，可能出現：

$$
D_P\downarrow
$$

並伴隨 performance 下降。

---

# 39. 實驗五：Divergent–Convergent Switch

第一階段：

$$
\mathcal D
$$

要求產生盡可能多的候選。

第二階段：

$$
\mathcal K
$$

要求快速選出最可行解。

測量：

$$
N_{\text{ideas}},
$$

$$
D_P,
$$

$$
T_{\text{closure}},
$$

$$
A_{\text{final}}.
$$

NCTH 真正預測的不是 ADHD 只在第一階段更好，而是：

> 不同 profile 在 expansion 與 closure 的 trade-off 形狀不同。

---

# 40. 實驗六：Cross-Path Validation

設計具有：

$$
m
$$

條獨立線索路徑的問題。

其中部分路徑支持：

$$
H_1,
$$

部分支持：

$$
H_2.
$$

測量受試者是否能：

1. 同時保持多個 hypothesis；
2. 找出衝突；
3. 淘汰不一致路徑；
4. 最後收斂。

定義：

$$
X_P
$$

與：

$$
E_{\text{conv}}.
$$

這比單純 divergent-thinking task 更直接測試「網狀推理」。

---

# 41. 實驗七：Parallelism vs Rapid Switching

使用時間解析方法：

- EEG；
- MEG；
- eye tracking；
- response probes；
- hidden-state computational modeling。

比較兩個模型：

$$
M_{\parallel}
$$

與：

$$
M_{\text{switch}}.
$$

若：

$$
P
\left(
D
\mid
M_{\parallel}
\right)
\leq
P
\left(
D
\mid
M_{\text{switch}}
\right),
$$

則不能宣稱真正 parallel processing。

---

# 42. 失敗條件

NCTH 應被削弱或淘汰，如果：

1. semantic breadth 無法在 clinical ADHD replication；
2. path diversity 不可可靠測量；
3. sparse-cue interaction 不存在；
4. scaffold effect 只由語言能力解釋；
5. multi-path metrics 不優於普通 divergent-thinking scores；
6. cross-path coherence 無群體或 profile 差異；
7. latent profile 不在 ADHD population 富集；
8. 所有差異可由 IQ、working memory 或 executive function 完整解釋；
9. out-of-sample performance 不優於簡單模型。

形式上：

$$
P_{\text{NCTH,out}}
\leq
P_{\text{baseline,out}}
$$

時，應優先保留 baseline model。

---

# 43. 最重要的反例：Clinical ADHD 與 Creativity 的關係並不穩定

2026 scoping review 明確指出，較早 reviews 對 clinical ADHD 與 creativity 的結果並不一致。

因此：

$$
\boxed{
\text{clinical ADHD}
\not\Rightarrow
\text{higher creativity}.
}
$$

這對 NCTH 不是問題，反而是必要限制。

因為 NCTH 本來就只允許：

$$
\boxed{
\text{specific profile}
\times
\text{specific task}
\rightarrow
\text{specific topology effect}.
}
$$

---

# 44. NCTH 不是優勢理論，而是結構理論

本文不先問：

> 網狀思維好不好？

而問：

> 候選激活、路徑形成、路徑比較與收斂的結構是否不同？

所以：

$$
N_{\text{eff}}>0
$$

或：

$$
N_{\text{eff}}<0
$$

都可能。

這使理論可以同時描述：

- creative expansion；
- distractibility；
- cross-domain analogy；
- irrelevant association；
- fast pattern completion；
- unresolved branching。

---

# 45. 與第 4 篇 Attention Entropy 的分離

第 4 篇定義：

$$
\widehat{\mathcal H}_{\Pi}
$$

描述資源配置的分散程度。

本篇定義：

$$
\mathcal G_t
$$

描述候選內容之間的關係拓撲。

所以：

$$
\boxed{
\text{allocation entropy}
\neq
\text{cognitive graph topology}.
}
$$

可能：

$$
\widehat{\mathcal H}_{\Pi}\uparrow
$$

但圖結構很亂。

也可能：

$$
\widehat{\mathcal H}_{\Pi}\uparrow
$$

同時多條高 coherence 路徑被有效維持。

這是完全不同的情況。

---

# 46. 系列整合

第 1 篇：

$$
\text{dynamic configuration}.
$$

第 2 篇：

$$
\mathbf N_t
\rightarrow
\text{neuromodulatory reparameterization}.
$$

第 3 篇：

$$
S_t
\neq
A_t
\neq
\Pi_t
\neq
O_t
\neq
U_t
\neq
G_t.
$$

第 4 篇：

$$
\mathbf X_t
=
\left(
R^{\max},
\widehat{\mathcal H}_{\Pi},
L,
T_{\text{dwell}},
\nu_{\text{switch}},
B_{\text{exit}},
R_G
\right).
$$

第 5 篇現在加入：

$$
\boxed{
\mathcal G_t
=
\left(
V_t,
E_t,
W_t
\right)
}
$$

以及：

$$
\boxed{
\Theta_t^{\text{topo}}
=
\left(
B,
R_{\text{act}},
D_P,
\overline C_P,
X_P,
E_{\text{conv}}
\right).
}
$$

系列主幹因此更新為：

$$
\boxed{
\mathbf N_t
\rightarrow
\mathbf Z_t
\rightarrow
\Pi_t
\rightarrow
\mathbf X_t
\rightarrow
\mathcal G_t
\rightarrow
O_t
\rightarrow
U_t
\rightarrow
G_t
\rightarrow
P_t
\rightarrow
Y_t.
}
$$

---

# 47. 本文不主張的內容

本文不主張：

1. ADHD 等於網狀思維；
2. 所有 ADHD individuals 都有較廣 semantic activation；
3. semantic activation 等於推理；
4. divergent thinking 等於 networked cognition；
5. creativity 是 ADHD 固有優勢；
6. mind wandering 等於多路徑推理；
7. functional-connectivity graph 等於 cognitive graph；
8. 主觀「同時想到很多」證明真正 parallel processing；
9. 更多 association 一定更好；
10. path diversity 越高越好；
11. sparse input 對 ADHD 一定比較好；
12. scaffold 對 ADHD 一定有害；
13. clinical ADHD 一定具有較高 creativity；
14. creativity research 已驗證 NCTH；
15. graph metrics 可以直接用於 ADHD diagnosis；
16. 本文模型是神經生理模型。

---

# 48. 結論

「網狀思維」若只是：

> 想很多、跳很快、聯想很多，

那它缺乏科學價值。

本文把它拆解成：

$$
\boxed{
\text{activation breadth}
}
$$

$$
\boxed{
\text{activation radius}
}
$$

$$
\boxed{
\text{path diversity}
}
$$

$$
\boxed{
\text{path coherence}
}
$$

$$
\boxed{
\text{cross-path consistency}
}
$$

$$
\boxed{
\text{convergence efficiency}.
}
$$

因此真正有用的 networked cognition 不是：

$$
\text{more associations}.
$$

而是：

$$
\boxed{
\text{generate multiple candidate routes,
preserve useful diversity,
reject incoherent routes,
and converge when the task requires closure}.
}
$$

已有 ADHD 文獻使「較廣 semantic activation」「較少受既有範例約束」「divergent-thinking differences」成為合理研究背景，但 2026 的 evidence synthesis 仍明確顯示 creativity literature 高度異質，clinical evidence 不一致，而且現有 neuroimaging 不能直接證明 cognitive-network mechanism。

因此 NCTH 的最終命題必須保持為：

$$
\boxed{
\text{Some ADHD-related cognitive profiles may occupy
a different region of associative-path topology space,
but the existence, prevalence, and functional value
of that region remain empirical questions}.
}
$$

真正需要回答的是：

$$
\boxed{
\text{Do graph-derived measures of associative breadth,
path diversity, coherence, and convergence
predict ADHD-related task differences
better than simpler cognitive models?}
}
$$

若答案是否定，「網狀認知拓撲」就應被放棄。

若答案肯定，則它可以成為連接 semantic activation、divergent thinking、mind wandering、因果補完與情境性 performance 的一個中層計算語言，而不是 ADHD 的新標籤。

---

# 參考文獻

1. White, H. A., & Shah, P. Scope of Semantic Activation and Innovative Thinking in College Students with ADHD. *Creativity Research Journal*. 2016;28(3):275–282. DOI: 10.1080/10400419.2016.1195655.

2. White, H. A. Thinking “Outside the Box”: Unconstrained Creative Generation in Adults with Attention Deficit Hyperactivity Disorder. *The Journal of Creative Behavior*. 2020;54(2):472–483. DOI: 10.1002/jocb.382.

3. Hoogman, M., Stolte, M., Baas, M., & Kroesbergen, E. Creativity and ADHD: A review of behavioral studies, the effect of psychostimulants and neural underpinnings. *Neuroscience & Biobehavioral Reviews*. 2020;119:66–85.

4. Stolte, M., Trindade-Pons, V., Vlaming, P., Jakobi, B., Franke, B., Kroesbergen, E. H., Baas, M., & Hoogman, M. Characterizing Creative Thinking and Creative Achievements in Relation to Symptoms of Attention-Deficit/Hyperactivity Disorder and Autism Spectrum Disorder. *Frontiers in Psychiatry*. 2022;13:909202. DOI: 10.3389/fpsyt.2022.909202.

5. Hupfeld, K. E., Osborne, J. B., Tran, Q. T., Hyatt, H. W., Abagis, T. R., et al. Validation of the dispositional adult hyperfocus questionnaire (AHQ-D). *Scientific Reports*. 2024;14:19460. DOI: 10.1038/s41598-024-70028-y.

6. Gao, Z., et al. Reduced temporal and spatial stability of neural activity patterns predict cognitive control deficits in children with ADHD. *Nature Communications*. 2025. DOI: 10.1038/s41467-025-57685-x.

7. Arabacı, G., & Parris, B. A. Daily life mind wandering and its relation to symptoms of ADHD in a community sample of emerging adults. *Current Psychology*. 2026;45:442. DOI: 10.1007/s12144-025-08962-x.

8. Ogata, H., Nakane, E., Kondo, C., Saima, S., Ihara, H., et al. Mind-Wandering in Adolescents With ADHD: A Comparative Study. *Journal of Attention Disorders*. 2026;30(4). DOI: 10.1177/10870547251385660.

9. Minamoto, T., Hayashi, T., & Al-Mamun, M. A. Behavioral and Self-Report Measures of Spontaneous Mind Wandering Predict Different Aspects of ADHD in Adults. *Journal of Attention Disorders*. 2026. DOI: 10.1177/10870547261448262.

10. Rafael, R. B., Jia, H., Rouel, M., Wootton, B. M., & Mitchison, D. Attention Deficit/Hyperactivity Disorder (ADHD)-Related Strengths in Adults: A Scoping Review. *Journal of Attention Disorders*. 2026. DOI: 10.1177/10870547261425737.

---

# 文獻使用聲明

本文僅使用上述研究建立截至 2026-08-16 的外部實證邊界。

本文提出的 NCTH、認知圖 $\mathcal G_t$ 、activation breadth $B_t$ 、activation radius $R_{\text{act}}$ 、path diversity $D_P$ 、path coherence $\overline C_P$ 、cross-path consistency $X_P$ 、convergence efficiency $E_{\text{conv}}$ 、networked cognition effective score $N_{\text{eff}}$ 與 sparse-cue／scaffold-interference hypotheses，均為本文理論構件，不應被誤認為上述研究作者的原始結論。

不同文獻包含臨床 ADHD、subclinical traits、community samples、college samples、adolescents、adults、self-report、behavioral tasks、creativity measures、mind-wandering measures 與 neuroimaging。它們不能被視為單一大型實驗直接累加。

---

**狀態：** v0.1，理論稿  
**新增原始臨床／人體數據：** 無  
**醫學用途：** 無  
**下一篇：** 《感覺變強不等於真的變強：主觀清晰度、元認知信心與客觀表現》
