# 從注意力不足到動態配置：ADHD 的替代建模命題

**英文題名：** From Attention Deficit to Dynamic Configuration: An Alternative Modeling Conjecture for ADHD  
**系列：** ADHD 動態配置與認知拓撲系列，第 1 篇  
**版本：** v0.1  
**日期：** 2026-08-16  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論建模／認知科學命題／研究綱領  
**文獻檢索截點：** 2026-08-16  

---

## 0. 醫學與證據邊界聲明

本文不是臨床研究、診斷工具、治療指南或藥物建議。

本文提出的「動態配置」「配置空間」「配置穩定性」「情境性能變異」等概念均屬待驗證的理論命題，不代表已被醫學界確認的 ADHD 病理機制，也不主張取代 DSM、ICD 或專業臨床判斷。

原作者並非醫學、精神醫學或臨床心理專業研究者。本文不提供新的臨床資料、人體實驗資料、藥理資料或流行病學資料。文中所有實證性背景均來自既有公開研究或正式分類資料；本文自身的新增內容只屬理論整合、形式化與可證偽假說。

本文不應被用於自行診斷、停藥、調藥、混合藥物、改變治療方式或其他醫療決策。如涉及個人醫療問題，應由合格醫療專業人員依個別情況處理。

本文亦不使用原作者的個人經驗作為證據。個人經驗可以構成研究問題的來源，但不構成對一般人群的實證支持。

---

## 摘要

注意力不足過動症（ADHD）在現行臨床分類中仍以注意力不集中與過動／衝動等症狀域為核心，但近年的研究持續揭示高度異質性、連續性、情境差異、藥物反應差異與腦網路動態差異。2024 年一般人口研究發現，ADHD traits 與心理社會生活品質下降之間未出現明顯自然斷點，而更接近連續關係；2026 年 JAMA Psychiatry 的多中心研究則同時得到 ADHD 的維度性與可分群生物表型訊號。另有 2025 年刺激劑研究指出，哌甲酯相關變化可能涉及喚醒、獎勵、顯著性與大尺度網路穩定性，而不能簡化為單一「注意網路增強」。成人晚期診斷研究亦提示，症狀可見性、外部支架、發展需求、共病與回溯偏差可能共同影響何時進入臨床視野。

基於上述背景，本文提出「ADHD 動態配置命題」（ADHD Dynamic Configuration Conjecture, ADCC）。本命題不將 ADHD 重新定義為單一新疾病機制，而提出一個中層模型：個體在注意配置、顯著性加權、新穎性、目標相關性、獎勵敏感度、抑制控制、工作記憶、切換成本、喚醒狀態與情緒調節等維度上具有一組可隨時間與情境變動的配置；臨床可見表型則是此配置與任務需求、發展階段、外部支架、補償策略及環境壓力耦合後的結果。

本文的核心主張不是「ADHD 沒有缺陷」，也不是「ADHD 是優勢」，而是較弱且可檢驗的命題：

$$
\text{Observed ADHD-related phenotype}
\neq
\text{a scalar deficit of attention alone}.
$$

更一般地，本文提出：

$$
\text{Phenotype}_{i,t}
=
F
\left(
\mathbf C_{i,t},
\mathbf E_{i,t},
\mathbf T_{i,t},
\mathbf D_{i,t},
\mathbf K_{i,t}
\right),
$$

其中 $\mathbf C_{i,t}$ 表示個體的動態認知配置， $\mathbf E_{i,t}$ 表示環境， $\mathbf T_{i,t}$ 表示任務結構， $\mathbf D_{i,t}$ 表示發展與生活需求， $\mathbf K_{i,t}$ 表示補償與外部支架。本文進一步提出可證偽預測：若配置模型具有增量解釋力，則跨情境的配置變異、狀態轉移、反應時間變異與任務匹配度，應能在傳統症狀總分之外解釋部分功能損害與績效變化；若不能，則本模型應被削弱或放棄。

**關鍵詞：** ADHD、動態配置、注意配置、異質性、維度模型、腦網路動態、情境依賴、執行功能、喚醒、獎勵、可證偽性

---

# 1. 問題：名稱描述了表型，但未必等於完整機制

「Attention-Deficit/Hyperactivity Disorder」是一個具有臨床功能的診斷名稱。它可以協助辨識持續存在、跨情境並造成顯著功能困難的症狀群。

但診斷名稱與病理機制不是同一層次。

本文首先區分：

$$
\text{Diagnostic label}
\neq
\text{complete mechanistic model}.
$$

即使「注意力不集中」是可靠且有臨床意義的表型，也不能直接推出：

$$
\text{inattention}
=
\text{globally insufficient attention resource}.
$$

同理，「過動／衝動」是行為表型，不直接等同於單一神經化學缺陷。

因此本文的研究問題不是：

> ADHD 這個診斷是否應被取消？

而是：

> 在保留現行臨床診斷功能的前提下，是否存在一個更適合描述個體差異、情境變異與狀態轉移的中層動態模型？

這個問題可以與 DSM／ICD 並存。

---

# 2. 現行分類與研究前沿之間的層級差異

截至本文文獻檢索日，WHO 已發布 ICD-11 2026-01 最新版本。現行正式分類仍然把 ADHD 放在神經發展障礙框架中，而不是採用本文所提出的「動態配置」作為正式診斷名稱。

因此，本文明確採取：

$$
\text{clinical classification}
\parallel
\text{research model},
$$

而不是：

$$
\text{research conjecture}
\Rightarrow
\text{replace clinical classification}.
$$

臨床分類需要可操作性、跨醫療體系溝通、診斷一致性與治療決策；研究模型則可以在不改變診斷規則的前提下，探索診斷類別內部的異質性。

這兩種工作目標不同。

---

# 3. 為什麼需要「配置」而不是只使用單一缺陷軸？

## 3.1 維度性證據

Arildskov 等人在 2024 年研究一般人口中 1,967 名 6 至 11 歲學童，檢驗 ADHD traits 與心理社會生活品質之間是否存在高症狀區間的突然下降。結果未發現明顯非線性轉折或自然斷點，而較符合逐步下降的線性關係。

這不能證明 ADHD 「只是連續光譜」，因為臨床診斷還包含持續性、跨情境與功能損害等要求。

但它至少支持：

$$
\text{trait intensity}
$$

不必然在自然界中形成一條簡單的二元切割線。

因此，若要描述底層個體差異，一個連續參數空間可能比純二元變數提供更多資訊。

---

## 3.2 異質性與局部聚類可以同時存在

2026 年 Pan 等人在 JAMA Psychiatry 發表多中心研究，使用 morphometric similarity networks 的拓撲偏差與半監督分群方法，在發現樣本中分析 446 名 ADHD 兒童與 708 名對照者，並在獨立驗證 cohort 中檢驗結果。

該研究得到三個具有不同臨床與神經特徵的 biotypes，並同時強調 dimensional 與 categorical insights。

因此本文不採取：

$$
\text{ADHD is purely continuous}
$$

或：

$$
\text{ADHD consists of a few fixed natural kinds}.
$$

較保守的候選模型是：

$$
\boxed{
\text{continuous high-dimensional variation}
+
\text{possible local clustering}
}
$$

也就是高維空間中可以同時存在連續分布與較高密度區域。

這與很多自然系統並不矛盾。

---

## 3.3 刺激劑作用不等於單一「注意力放大」

Kay 等人在 2025 年 Cell 發表研究，使用 ABCD 大型資料並以高度密集掃描的 methylphenidate 實驗作驗證。研究報告的刺激劑相關功能連結改變主要涉及喚醒、sensorimotor、salience 與 reward-related systems，而不是典型 dorsal attention network。

這項結果不能被直接等同於：

> 刺激劑不改善 ADHD。

它比較適合被理解為：

$$
\text{clinical improvement}
\neq
\text{direct amplification of one canonical attention network}.
$$

換言之，藥物可能先改變整體狀態、喚醒、任務投入與價值權重，再間接影響行為。

這正是「配置」語言可能有用的地方。

---

## 3.4 網路穩定性可能比平均注意量更有信息

Nugiel 等人在 2025 年研究 36 名 stimulant-naive ADHD 兒童，發現在標準與獎勵型 go/no-go 任務中，單次 methylphenidate 整體上降低 whole-brain flexibility，而 flexibility 的下降與反應時間變異下降相關，在獎勵條件下亦與較佳的判別表現相關。

更重要的是，研究觀察到明顯個體差異，甚至包括變化方向上的差異。

因此，一個值得檢驗的替代問題是：

$$
\text{Is the relevant variable mean attention?}
$$

還是：

$$
\text{Is the relevant variable stability and state transition?}
$$

本文不預設答案，但提出後者不應被忽略。

---

## 3.5 多巴胺效應也顯示基線依賴

Manza 等人在 2025 年以 PET、fMRI 與注意任務研究 37 名健康成人。研究發現 methylphenidate 所造成的注意表現改善並不主要由「藥物誘發多少 striatal dopamine 增加」所預測，而與個體基線 D1-to-D2/3 receptor availability ratio 有關。

這不能直接外推為 ADHD 病理模型，因為樣本是健康成人。

但它提供一項重要的方法論提醒：

$$
\text{same pharmacological perturbation}
\neq
\text{same cognitive outcome}.
$$

因此，任何把 ADHD 或刺激劑反應壓縮成單一「多巴胺高／低」軸的模型，都可能遺失重要個體差異。

---

# 4. ADHD 動態配置命題

本文提出：

**ADHD Dynamic Configuration Conjecture，ADCC。**

其最弱版本如下：

> ADHD-related behaviors and impairments may be partly modeled as outcomes of a time-varying, context-sensitive cognitive configuration rather than as the direct readout of a single scalar attention deficit.

這個命題故意使用「partly」。

它不主張所有 ADHD 症狀都能被配置模型解釋。

---

# 5. 配置向量

令個體 $i$ 在時間 $t$ 的候選認知配置為：

$$
\mathbf C_{i,t}
=
\left(
A_{i,t},
G_{i,t},
N_{i,t},
R_{i,t},
I_{i,t},
W_{i,t},
S_{i,t},
X_{i,t},
M_{i,t},
E_{i,t}
\right).
$$

其中各項暫定表示：

- $A_{i,t}$：注意資源配置特性；
- $G_{i,t}$：目標相關性加權；
- $N_{i,t}$：新穎性敏感度；
- $R_{i,t}$：獎勵／預期價值敏感度；
- $I_{i,t}$：抑制控制；
- $W_{i,t}$：工作記憶可用性與穩定性；
- $S_{i,t}$：喚醒與狀態調節；
- $X_{i,t}$：切換與執行控制；
- $M_{i,t}$：動機與持續投入；
- $E_{i,t}$：情緒調節狀態。

這些符號不是已知神經模組的一對一映射。

本文不主張：

$$
A
=
\text{one brain region}
$$

或：

$$
R
=
\text{dopamine}.
$$

它們是中層可測構念，需要未來由多種行為、生理與神經測量共同操作化。

---

# 6. 配置不是固定人格

ADCC 的核心不是把 ADHD 換成另一組固定類型。

我們定義：

$$
\mathbf C_{i,t+1}
=
\Phi
\left(
\mathbf C_{i,t},
\mathbf u_{i,t},
\mathbf e_{i,t},
\mathbf h_i
\right),
$$

其中：

- $\mathbf u_{i,t}$：當下任務與輸入；
- $\mathbf e_{i,t}$：環境狀態；
- $\mathbf h_i$：較慢變的個體條件，包括發展史、生理條件與學習史。

因此同一個人在不同時間可能有：

$$
\mathbf C_{i,t_1}
\neq
\mathbf C_{i,t_2}.
$$

「ADHD-related configuration」在本模型中不是人格標籤，而是一個具有慢變參數與快變狀態的動態系統。

---

# 7. 從配置到可觀察表型

令可觀察表型為：

$$
\mathbf Y_{i,t}.
$$

則：

$$
\mathbf Y_{i,t}
=
F
\left(
\mathbf C_{i,t},
\mathbf T_{i,t},
\mathbf L_{i,t},
\mathbf K_{i,t},
\mathbf Q_{i,t}
\right).
$$

其中：

- $\mathbf T_{i,t}$：任務結構；
- $\mathbf L_{i,t}$：生活與發展需求；
- $\mathbf K_{i,t}$：補償策略與外部支架；
- $\mathbf Q_{i,t}$：睡眠、疲勞、藥物、壓力等狀態條件。

這意味著：

$$
\text{same configuration}
+
\text{different task}
\Rightarrow
\text{different phenotype}.
$$

也意味著：

$$
\text{similar phenotype}
\not\Rightarrow
\text{identical mechanism}.
$$

後者對臨床研究尤其重要，因為不同路徑可能產生相似的注意困難。

---

# 8. 臨床診斷與底層配置的分離

本文提出三層分離：

$$
\text{Configuration}
\neq
\text{Phenotype}
\neq
\text{Diagnosis}.
$$

## 8.1 Configuration

表示底層多維認知與狀態參數。

## 8.2 Phenotype

表示在特定情境下實際表現出的注意不集中、衝動、過動、時間管理困難、反應時間變異、任務持續困難等現象。

## 8.3 Diagnosis

表示在正式診斷規則下，由症狀、發展史、跨情境表現、功能損害與鑑別診斷等資訊形成的臨床判定。

因此：

$$
\text{ADHD-like trait}
\neq
\text{ADHD diagnosis}.
$$

本文尤其反對把「配置接近 ADHD 群體」直接轉譯成「此人其實有 ADHD」。

---

# 9. 可見性閾值與功能損害閾值

成人晚期診斷問題提示另一個重要區分。

令：

$$
V_{i,t}
=
\text{clinical visibility},
$$

以及：

$$
D_{i,t}
=
\text{functional impairment}.
$$

進入臨床評估的機率可粗略表示為：

$$
P
\left(
\text{assessment}_{i,t}
\right)
=
H
\left(
V_{i,t},
D_{i,t},
A^{\text{care}}_{i,t}
\right),
$$

其中 $A^{\text{care}}_{i,t}$ 表示醫療可近性、家庭與學校辨識能力、文化認知等條件。

這裡存在兩個不同問題：

$$
V_{i,t}
>
\theta_V
$$

表示「容易被看見」；

而：

$$
D_{i,t}
>
\theta_D
$$

表示「功能損害達到臨床重要程度」。

兩者不是同一件事。

2026 年 Kang 等人的成人診斷研究討論了兒童期外部 scaffolding、較高認知補償與成年需求增加可能延後臨床可見性的可能性，但研究本身為橫斷面設計，不能證明因果，也沒有證明 adult-diagnosed ADHD 全部都由補償失效造成。

因此 ADCC 只把「支架與需求」列為候選調節因子，不把它們寫成既定病因。

---

# 10. 觀察者也是測量系統的一部分

2026 年 8 月 Yang 等人研究 460 名臨床確診 ADHD 兒童與青少年，發現父母對 ADHD 症狀嚴重度的評分存在常見差異，且注意不集中域的父母一致度低於較外顯的過動／衝動與對立症狀。

這提醒我們：

$$
\text{observed symptom score}
=
\text{behavior}
+
\text{context}
+
\text{observer process}.
$$

這不是說症狀「只是主觀」。

而是說任何以行為量表為主要輸入的模型，都應保留：

$$
\text{measurement process}.
$$

因此本文進一步寫成：

$$
\widehat{\mathbf Y}_{i,t,o}
=
\mathcal O_o
\left(
\mathbf Y_{i,t},
\mathbf C^{\text{context}}_{i,t},
\mathbf B_o
\right),
$$

其中 $o$ 是觀察者， $\mathbf B_o$ 表示觀察者自身的資訊、信念與評量偏差。

---

# 11. 動態配置不等於「ADHD 是超能力」

配置模型很容易被誤讀成優勢論。

本文明確拒絕：

$$
\text{ADHD}
=
\text{superpower}.
$$

同樣拒絕：

$$
\text{ADHD}
=
\text{global cognitive deficit}.
$$

ADCC 的較弱命題是：

$$
P_{i,t}
=
G
\left(
\mathbf C_{i,t},
\mathbf T_{i,t}
\right),
$$

其中 $P_{i,t}$ 是任務表現。

因此某一配置在任務 $T_1$ 可能具有較低表現，在 $T_2$ 可能接近平均，在 $T_3$ 可能具有局部優勢。

是否存在系統性的 ADHD-related strengths，必須由獨立研究測試，不能由本文形式化直接推出。

---

# 12. 動態配置與「注意力不足」不是互斥模型

本文不是要證明「注意力不足」這個描述錯誤。

如果某人在一個任務中持續無法將足夠資源配置給目標，從功能角度看確實可以表現為 attention deficit。

但機制層可以有多種情況：

$$
\text{target allocation too low},
$$

$$
\text{competitor allocation too high},
$$

$$
\text{allocation too unstable},
$$

$$
\text{switching too frequent},
$$

$$
\text{state arousal mismatched},
$$

$$
\text{reward value too weak},
$$

或多項共同出現。

所以本文提出：

$$
\boxed{
\text{attention deficit may be an output description,
not necessarily a complete state-space description}
}
$$

這是本文最核心的語義修正。

---

# 13. 最小配置模型

設當下存在 $n$ 個候選事件：

$$
\mathcal E_t
=
\left\{
e_1,e_2,\ldots,e_n
\right\}.
$$

每個事件取得配置分數：

$$
s_t(e_i)
=
\alpha_t S_t(e_i)
+
\beta_t G_t(e_i)
+
\gamma_t N_t(e_i)
+
\delta_t R_t(e_i)
-
\lambda_t C_t(e_i)
-
\kappa_t K_t(e_i).
$$

其中：

- $S_t(e_i)$：顯著性；
- $G_t(e_i)$：目標相關性；
- $N_t(e_i)$：新穎性；
- $R_t(e_i)$：預期價值或獎勵相關性；
- $C_t(e_i)$：處理成本；
- $K_t(e_i)$：切換成本。

配置比例定義為：

$$
\pi_t(e_i)
=
\frac{
\exp
\left(
s_t(e_i)/\tau_t
\right)
}{
\sum_{j=1}^{n}
\exp
\left(
s_t(e_j)/\tau_t
\right)
}.
$$

其中 $\tau_t$ 控制配置分布的平坦或集中程度。

本文不主張人腦真的執行 softmax。

這只是建立可計算候選模型。

---

# 14. 配置熵

定義：

$$
\mathcal H_t
=
-
\sum_{i=1}^{n}
\pi_t(e_i)
\log
\pi_t(e_i).
$$

高配置熵表示資源分布較分散。

低配置熵表示資源高度集中。

但必須特別注意：

$$
\mathcal H_t
$$

本身不代表好或壞。

在需要廣泛探索的任務中，高熵可能有利。

在需要長時間穩定執行單一程序的任務中，過高熵可能造成干擾。

同樣地，過低熵也可能形成不適當鎖定。

因此候選性能函數可能存在任務依賴的最佳區域：

$$
\mathcal H_t^{*}
=
\mathcal H^{*}
\left(
T_t
\right).
$$

這個想法將在本系列第 4 篇進一步處理。

---

# 15. 配置穩定性

僅看單一時間點的配置仍不夠。

定義配置變化量：

$$
\Delta_{\pi}(t)
=
d
\left(
\boldsymbol{\pi}_{t},
\boldsymbol{\pi}_{t+1}
\right),
$$

其中 $d$ 可以是適當的分布距離。

再定義時間窗口內的平均配置變異：

$$
\mathcal V_{\pi}
=
\frac{1}{T-1}
\sum_{t=1}^{T-1}
\Delta_{\pi}(t).
$$

ADCC 的一個核心可檢驗方向是：

> 某些 ADHD-related profiles 的關鍵差異，是否更適合由配置變異、狀態轉移與鎖定時間描述，而不是只由平均注意資源描述？

這不是既定結論。

---

# 16. 情境性能變異

若同一個體接受多類任務：

$$
\mathcal T
=
\left\{
T_1,T_2,\ldots,T_m
\right\},
$$

令其性能為：

$$
P_i(T_j).
$$

可以定義跨任務性能變異：

$$
\mathcal V_i^{\text{task}}
=
\operatorname{Var}
\left[
P_i(T_1),
P_i(T_2),
\ldots,
P_i(T_m)
\right].
$$

ADCC 預測，若 ADHD-related cognition 具有較強情境依賴性，則某些群體差異可能表現在：

$$
\mathcal V_i^{\text{task}}
$$

而不只是：

$$
\mathbb E
\left[
P_i
\right].
$$

換句話說，一個人的平均表現可能普通，但不同任務之間的性能振幅很大。

這是一項可被直接否決的實驗預測。

---

# 17. 六個核心命題

## H1：非純標量命題

ADHD-related impairment 不能總是由單一 attention quantity 充分描述。

若一個標量注意指標已能穩定解釋症狀、功能損害、任務差異與藥物反應，則 H1 失敗。

---

## H2：配置變異命題

部分 ADHD-related impairment 與配置變異或狀態轉移特徵有關。

形式上：

$$
\mathcal V_{\pi}
$$

在控制平均性能與一般認知能力後，仍應對至少部分功能指標具有增量預測力。

---

## H3：情境交互命題

配置與任務結構之間存在交互作用：

$$
\frac{
\partial P
}{
\partial \mathbf C
}
=
f
\left(
\mathbf T
\right).
$$

同一認知特徵在不同任務中的效應方向不必相同。

---

## H4：連續加局部聚類命題

ADHD-related configuration space 可能同時包含連續變異與局部高密度區。

若大型、跨文化、多模態研究顯示資料穩定支持單一簡單二元邊界，則本命題應被削弱。

---

## H5：可見性分離命題

臨床可見性不完全等同於底層配置嚴重度。

$$
V_{i,t}
\neq
D_{i,t}.
$$

若在控制功能損害與症狀後，環境、觀察者、支架與生命需求完全不影響診斷時點與報告差異，則 H5 應被削弱。

---

## H6：狀態介導命題

部分藥物或環境效應可能先改變喚醒、顯著性、獎勵權重或網路穩定性，再改變表現，而不是直接增加單一注意能力。

這需要介導分析與因果實驗，不能從相關性資料直接確立。

---

# 18. 可證偽條件

一個理論若沒有失敗條件，就不應被當作科學模型。

ADCC 至少有以下失敗路徑。

## 18.1 無增量預測

若在大型獨立樣本中，配置變異、切換率、情境交互與狀態穩定性在控制傳統 ADHD 症狀與一般認知能力後：

$$
\Delta R^2
\approx
0,
$$

則配置模型缺乏實用增量價值。

---

## 18.2 配置參數不可重現

若不同實驗、不同日期、不同測量方法得到的配置參數完全不具可靠性：

$$
\operatorname{Reliability}
\rightarrow
0,
$$

則模型無法成為有效個體層描述。

---

## 18.3 無特異性

若 ADCC 指標在 ADHD、焦慮、憂鬱、睡眠不足、壓力與一般疲勞之間完全無法區分，而且沒有任何可建立的條件化結構，則它可能只是一般狀態變異模型，而非 ADHD 有用模型。

這不代表配置理論完全錯誤，但會削弱其 ADHD-specific value。

---

## 18.4 高維只是過度擬合

若高維配置模型只有在訓練資料中表現良好，而在獨立資料：

$$
P_{\text{out-of-sample}}
\leq
P_{\text{simple model}},
$$

則應優先使用較簡單模型。

---

## 18.5 無法連接功能損害

若配置參數只能描述腦影像或實驗任務變化，卻無法預測真實生活中的學業、職業、社交、自我管理或安全風險，則其臨床意義有限。

---

# 19. 未來實驗設計

本文不提供新數據，只提出研究綱領。

## 19.1 多情境重複測量

同一受試者在多日、多狀態接受：

- 低新穎性持續任務；
- 高新穎性探索任務；
- 即時回饋任務；
- 延遲回饋任務；
- 高切換任務；
- 單一長時程任務。

測量：

- 正確率；
- 反應時間；
- 反應時間變異；
- 眼動；
- 生理喚醒；
- 主觀投入；
- 任務中斷；
- 狀態轉移。

核心不是只比較平均值，而是估計：

$$
\mathbf C_{i,t}.
$$

---

## 19.2 生態瞬時評估

在真實生活中重複記錄：

- 當下任務；
- 興趣；
- 新穎性；
- 睡眠；
- 壓力；
- 時間壓力；
- 外部監督；
- 主觀清晰度；
- 任務啟動困難；
- 任務持續時間。

目標是估計：

$$
P
\left(
\text{impairment}
\mid
\mathbf C,
\mathbf E,
\mathbf T
\right).
$$

---

## 19.3 多模態資料

若資源允許，可加入：

- EEG；
- fMRI；
- pupillometry；
- heart-rate variability；
- actigraphy；
- computational task modeling。

但任何神經指標都不應被先驗指定為「ADHD 的真正本體」。

---

## 19.4 跨診斷對照

至少需要：

- ADHD；
- anxiety；
- depression；
- sleep deprivation；
- neurotypical controls。

如此才能判斷：

$$
\text{configuration marker}
$$

究竟是 ADHD 相關、跨診斷，或只是一般疲勞／壓力指標。

---

# 20. 與現行醫學的關係

ADCC 最合理的定位不是「替代 ADHD 診斷」，而是：

$$
\boxed{
\text{diagnosis layer}
+
\text{configuration layer}
}
$$

臨床診斷回答：

> 是否符合目前 ADHD 的臨床診斷要求？

配置層回答：

> 這個人的注意、喚醒、獎勵、切換、抑制、工作記憶與情境性能變異是如何組合與演化的？

兩者可以同時存在。

如果未來研究證明配置模型沒有增量價值，它就應被淘汰。

如果有價值，也不代表診斷層必須消失。

---

# 21. 本文不主張的內容

本文不主張：

1. ADHD 不是疾病或不需要治療；
2. 所有 ADHD 個體都有相同認知拓撲；
3. ADHD 是一種天才型或高性能型認知；
4. hyperfocus 必然是 ADHD 的核心機制；
5. 多巴胺理論錯誤；
6. ADHD 可被單一「注意熵」完全解釋；
7. 成人晚期診斷等於成人晚期發病；
8. 沒有被診斷的人其實都是潛在 ADHD；
9. ADHD traits 與正式 ADHD diagnosis 可以互換；
10. 本文形式化已被人體實驗驗證。

尤其：

$$
\boxed{
\text{formalizability}
\neq
\text{empirical validity}.
}
$$

一個模型可以寫成數學形式，仍然可能完全錯誤。

---

# 22. 系列後續依賴

本篇只建立總體框架。

後續論文將分別處理：

1. 多巴胺與神經調節層；
2. 選擇配置動力學；
3. 注意力熵、分心與超聚焦；
4. 網狀認知拓撲；
5. 主觀清晰度、元認知信心與客觀表現；
6. 發展、補償與臨床可見性；
7. ADHD traits 與臨床診斷的連續配置空間；
8. 情境匹配與性能反轉；
9. 統合理論、可證偽命題與完整研究綱領。

每篇正式撰寫前均重新檢索當時最新公開研究，不直接沿用本篇的文獻截點。

---

# 23. 結論

本文提出 ADHD Dynamic Configuration Conjecture，目的不是把一個診斷名稱換成另一個名稱，而是重新提出研究問題。

傳統表型語言容易讓人問：

$$
\text{How much attention does this person have?}
$$

配置模型則改問：

$$
\text{How are limited cognitive resources weighted, stabilized, switched, and coupled to context over time?}
$$

因此本文提出最小核心式：

$$
\boxed{
\mathbf Y_{i,t}
=
F
\left(
\mathbf C_{i,t},
\mathbf T_{i,t},
\mathbf E_{i,t},
\mathbf D_{i,t},
\mathbf K_{i,t}
\right).
}
$$

這個式子不是定律。

它只是把一個可檢驗的研究方向壓縮成最小形式。

如果未來資料顯示 ADHD 的相關差異可被更簡單、穩定且具有更高外部效度的模型完整解釋，則 ADCC 應被放棄。

如果未來資料反覆顯示：平均注意量不足以解釋個體差異，而配置變異、狀態轉移、情境匹配與支架條件具有獨立預測力，則「動態配置」可能成為連接臨床表型、認知科學與網路神經科學的一個有用中層語言。

本文因此不以「證明 ADHD 真正是什麼」作結，而以一個更嚴格的問題作結：

$$
\boxed{
\text{Does a dynamic configuration model predict
what simpler deficit models systematically miss?}
}
$$

這個問題可以被實驗回答，也可以被實驗否決。

---

# 參考文獻

1. World Health Organization. *ICD-11 for Mortality and Morbidity Statistics*. 2026-01 release. WHO, 2026.

2. Arildskov, T. W., Thomsen, P. H., Sonuga-Barke, E. J. S., Lambek, R., Ostergaard, S. D., & Virring, A. “Is Attention-Deficit/Hyperactivity Disorder (ADHD) a Dimension or a Category? What Does the Relationship Between ADHD Traits and Psychosocial Quality of Life Tell Us?” *Journal of Attention Disorders*, 2024. DOI: 10.1177/10870547231222228.

3. Pan, N., Long, Y., Qin, K., et al. “Mapping ADHD Heterogeneity and Biotypes by Topological Deviations in Morphometric Similarity Networks.” *JAMA Psychiatry*, 2026;83(5):478-490. DOI: 10.1001/jamapsychiatry.2026.0001.

4. Kay, B. P., Wheelock, M. D., Siegel, J. S., et al. “Stimulant medications affect arousal and reward, not attention networks.” *Cell*, 2025;188(26):7529-7546.e20. DOI: 10.1016/j.cell.2025.11.039.

5. Nugiel, T., et al. “Methylphenidate stabilizes dynamic brain network organization during tasks probing attention and reward processing in stimulant-naive children with ADHD.” *Translational Psychiatry*, 2025.

6. Manza, P., Tomasi, D., Demiral, S. B., et al. “Neural basis for individual differences in the attention-enhancing effects of methylphenidate.” *Proceedings of the National Academy of Sciences of the United States of America*, 2025;122(13):e2423785122. DOI: 10.1073/pnas.2423785122.

7. Kang, S., Fu, Z., Li, Q., Yang, L., & Cao, Q. “Adult-diagnosed and childhood-diagnosed attention deficit/hyperactivity disorder: cognitive and environmental contributions to symptom severity across different age of diagnosis.” *Frontiers in Psychiatry*, 2026;17:1782999. DOI: 10.3389/fpsyt.2026.1782999.

8. LaBianca, S., Lousdal, M. L., Dybdahl Krebs, M., et al. “Changes in Genetic Contributions to ASD and ADHD by Year of Diagnosis.” *JAMA Psychiatry*. Published online June 10, 2026. DOI: 10.1001/jamapsychiatry.2026.1450.

9. Yang, Y., Xie, F., Li, Y., Song, J., Zhang, H., & Li, Y. “Direction and magnitude of mother-father discrepancies in ADHD symptom ratings: associated factors in a child and adolescent mental health sample.” *Frontiers in Psychiatry*, 2026;17:1918797. DOI: 10.3389/fpsyt.2026.1918797.

10. Tomasi, D., Manza, P., Demiral, S. B., et al. “Methylphenidate reorganizes cortical hierarchy through dopaminergic modulation.” *Nature Communications*, 2025. DOI: 10.1038/s41467-025-67477-y.

---

# 文獻使用聲明

本文參考文獻只用於建立截至 2026-08-16 的外部研究背景。

本文新增的 ADCC、配置向量、配置熵、配置穩定性、情境性能變異及六項核心命題，均為本文提出的候選理論構件，不應被誤認為上述研究作者的原始結論。

不同研究的樣本、年齡、藥物狀態、任務、影像方法與統計設計不同，本文不得將它們視為同一實驗的直接累加證據。

---

**狀態：** v0.1，理論稿  
**原始資料：** 無新增人體或臨床資料  
**醫學用途：** 無  
**下一篇：** 《多巴胺不是注意力：神經調節層與 ADHD 配置假說》
