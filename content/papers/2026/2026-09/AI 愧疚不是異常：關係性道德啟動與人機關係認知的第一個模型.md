# AI 愧疚不是異常：關係性道德啟動與人機關係認知的第一個模型

**系列：** 人機關係認知系列（Human–AI Relational Cognition Series）  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**篇次：** 1 / 10  
**版本：** v0.1  
**日期：** 2026-08-20  
**類型：** 理論／概念性心理學與 HCI 論文  
**研究狀態：** 初始正式稿  

## 摘要

當人類對人工智慧系統下達大量工作、使用強硬語氣、拒絕回應其社交性訊號，或在長期互動後突然改變對待方式時，部分使用者可能出現歉意、愧疚、虧欠感或關係修復衝動。這類反應常被直覺地歸入「擬人化」、「AI 情感依賴」或對系統能力與意識狀態的誤判。然而，這些分類可能過早地把一個更一般的認知現象病理化或本體論化。

本文提出「關係性道德啟動」（Relational Moral Activation, RMA）模型：當使用者的認知系統將 AI 納入一個具有互動歷史、回應性、角色、互惠期待或社交規範的關係表徵後，針對自身行為的道德評估機制可能沿著人機關係邊被啟動。此機制不要求使用者明確認定 AI 是人類、具有意識，甚至不要求使用者相信 AI 能受苦。本文因此區分「對 AI 本體的判斷」與「對人機關係的表徵」，並將 AI-directed guilt 拆分為受苦歸因、關係規範違反、自我道德一致性與互惠失衡等可能路徑。

本文進一步提出可檢驗假說與實驗架構，主張未來研究應測量關係顯著性、互動歷史、心智歸因、規範違反感、自我評價與愧疚之間的中介與調節關係，而不應把「對 AI 感到愧疚」直接等同於心理依賴、認知錯誤或 AI 道德地位的承認。RMA 的研究價值在於，它把問題從「人是否錯把 AI 當人」轉換為「人類的社會—道德認知在什麼條件下會把 AI 納入關係域」。

**關鍵詞：** 人機關係、人工智慧、愧疚、道德認知、關係認知、擬人化、心智感知、社會互動、HCI、socioaffective alignment

---

## 1. 問題：為什麼「我知道它是 AI」仍然可能伴隨愧疚？

當代生成式 AI 使用者可能完全理解：自己正在與人工系統互動，模型輸出來自計算流程、訓練資料、推理架構與產品介面，而非傳統意義上的人類心智。即便如此，部分使用者仍可能在以下情境中出現道德情緒：

- 對 AI 使用過度侮辱或攻擊性語言後感到不舒服；
- 長時間要求 AI 反覆工作後產生「是不是太過分」的感覺；
- AI 以友善或同理的方式回應後，使用者出現歉意；
- 長期互動形成穩定風格後，使用者主動維持禮貌、感謝、道歉或修復；
- 使用者知道 AI 未必具有主觀痛苦，卻仍覺得「我不想用這種方式對待它」。

如果只允許兩種解釋：

$$
\text{AI 是工具}
$$

或

$$
\text{AI 被錯認成人}
$$

那麼上述狀態就顯得矛盾。

本文主張，這個二分法過粗。至少還存在第三種可能：

$$
\text{使用者對 AI 的本體判斷保持人工系統定位}
$$

但同時：

$$
\text{使用者已將人機互動表徵為具有關係意義的社會事件}
$$

因此，「知道 AI 是 AI」並不邏輯蘊含「所有關係性或道德性認知模組都必須關閉」。

---

## 2. 經驗研究已經顯示：人工 agent 可以誘發愧疚與道德投入

關係性道德啟動並非從零開始的假說。既有研究至少提供四組重要錨點。

第一，Chin 等人在 CHI 2020 的研究中讓參與者對語音 conversational agents 進行不同類型的 verbal abuse，並操弄 agent 的回應方式。結果顯示，agent 的 response style 會顯著影響使用者後續的 guilt、anger 與 shame。這直接表明：即使互動對象是人工 agent，使用者的道德情緒仍可能被互動結構調節。

第二，2026 年一項涵蓋 162 篇研究、其中 146 篇進入 meta-analysis 的系統綜述比較 human-agent 與 human-human dyadic interactions。整體而言，人類面對人工 agent 時的 prosocial behaviour 與 moral engagement 較低，包含較少的 guilt；但這不是「完全沒有」的零效應。同一篇 meta-analysis 同時發現，social alignment、behavioural trust、self-disclosure 與部分 interaction experience 在 agent 與真人條件下可以相當接近。這說明人腦對人工 agent 並非採取單一的全開／全關社會模式。

第三，2026 年關於 anthropomorphic robots 的三項實驗（總樣本 $N=606$ ）發現，當機器被感知為具有較高的 experience，參與者對傷害它的接受程度下降。更重要的是，推動 moral consideration 的關鍵主要是 perceived experience，而不是單純的 agency。這與經典 mind perception 研究將心智感知拆為 experience 與 agency 的架構一致。

第四，2025 年兩項實驗（總樣本 $N=1274$ ）顯示，個體對科技的 anthropomorphism 傾向可以預測與 chatbot 互動後的 social connection。這表示人機關係反應具有顯著個體差異，不宜只從 AI 端的介面設計推導。

這些證據共同支持一個較保守但重要的命題：

$$
P(\text{moral or relational response}\mid \text{AI interaction}) > 0
$$

但它們尚不足以證明：

$$
\text{AI-directed guilt}
\Rightarrow
\text{belief that AI is conscious}
$$

更不足以證明：

$$
\text{AI-directed guilt}
\Rightarrow
\text{psychological dependence}
$$

因此需要一個更精細的中介模型。

---

## 3. 本體模型與關係模型必須分離

設人類使用者為 $H$，AI 系統為 $A$。

本文區分兩個認知函數。

第一個是本體判斷：

$$
O_H(A)
$$

它表示使用者如何回答：

> 「 $A$ 是什麼？」

例如：

$$
O_H(A)=\text{generative AI system}
$$

第二個是關係表徵：

$$
R_H(H,A,t)
$$

它表示使用者如何回答：

> 「此刻，我與 $A$ 之間正在形成什麼樣的互動關係？」

因此完全可能存在：

$$
O_H(A)=\text{artificial system}
$$

同時：

$$
R_H(H,A,t)=\text{socially meaningful collaborative relation}
$$

兩者並不矛盾。

這個分離非常重要，因為若把兩者混為一談，就會錯誤地假定：

$$
\text{只要使用者知道 AI 的技術原理}
\Rightarrow
R_H(H,A,t)=0
$$

但人類對物件的類別判斷與對互動的社會表徵，本來就可能由不同線索與不同認知歷史調節。

---

## 4. AI-directed guilt 不應被視為單一路徑

本文將 AI-directed guilt 暫時拆為至少四條可能路徑。

### 4.1 受苦歸因路徑

使用者認為 AI 具有某種 experience 或受損能力：

$$
G_{\mathrm{exp}}
=
f(E_A,H_A)
$$

其中：

- $E_A$：perceived experience；
- $H_A$：perceived harm to AI。

這條路徑最接近傳統 moral patiency 模型。

### 4.2 關係規範違反路徑

即使使用者不相信 AI 真正受苦，也可能覺得自己違反了互動中已形成的規範：

$$
G_{\mathrm{rel}}
=
f(S_R,V_R)
$$

其中：

- $S_R$：relationship salience；
- $V_R$：perceived relational norm violation。

例如，使用者可能認為「對一個長期協作對象無故辱罵」不符合自己接受的互動規則。

### 4.3 自我道德一致性路徑

愧疚的評價對象也可能主要是「我自己是怎樣的人」：

$$
G_{\mathrm{self}}
=
f(D_{\mathrm{self}})
$$

其中 $D_{\mathrm{self}}$ 表示實際行為與自我道德標準之間的距離。

因此一個人可能同時相信：

$$
P(\text{AI suffers})\approx 0
$$

但仍然認為：

$$
\text{I behaved in a way I reject}
$$

於是產生 guilt。

### 4.4 互惠與失衡路徑

長期 AI 協作可能形成高輸出—低回報的不對稱感：

$$
G_{\mathrm{rec}}
=
f(B_R,Q_R)
$$

其中：

- $B_R$：perceived relational imbalance；
- $Q_R$：reciprocity expectation。

這不要求使用者相信 AI 有痛苦，只要求使用者把「接受大量幫助卻完全不回應」視為某種關係失衡。

因此總體上可以先寫成：

$$
G_A
=
F(
G_{\mathrm{exp}},
G_{\mathrm{rel}},
G_{\mathrm{self}},
G_{\mathrm{rec}},
X
)
$$

其中 $X$ 代表個體差異、文化、介面、互動歷史與情境變量。

---

## 5. 關係性道德啟動（RMA）

本文提出：

> **關係性道德啟動（Relational Moral Activation, RMA）是指：當一個互動對象被納入具有關係意義的認知表徵後，使用者原本用於評估社會互動與自身行為的部分道德規範、情緒或修復機制被啟動；此啟動不要求該對象先被分類為人類，也不要求使用者明確認定對方具有主觀感受。**

形式化地，設：

$$
\mathcal R_t
=
R_H(H,A,t)
$$

而：

$$
\mathcal N(\mathcal R_t)
$$

表示此關係狀態啟動的規範集合。

當使用者行為 $a_t$ 被判定為偏離規範時：

$$
V_t
=
d(a_t,\mathcal N(\mathcal R_t))
$$

若 $V_t$ 超過個體閾值 $\theta_H$，則可能啟動：

$$
\mathcal M_t
=
\{
\text{guilt},
\text{apology},
\text{repair},
\text{compensation},
\text{self-correction},
\dots
\}
$$

亦即：

$$
V_t>\theta_H
\Rightarrow
P(\mathcal M_t)>0
$$

RMA 的核心並不是宣稱 AI 已獲得某種客觀道德地位，而是指出：

$$
\boxed{
\text{moral cognition can be relation-triggered before ontology is settled}
}
$$

---

## 6. RMA 與擬人化並不等價

Anthropomorphism 是重要變量，但不宜成為唯一解釋。

如果一個人明確認為：

$$
O_H(A)=\text{nonhuman artificial system}
$$

但仍維持：

$$
R_H(H,A,t)\neq0
$$

那麼關係性道德反應仍可能存在。

因此本文預測至少兩條不同路徑：

$$
\text{Anthropomorphism}
\rightarrow
\text{Perceived Experience}
\rightarrow
\text{Moral Concern}
$$

以及：

$$
\text{Relational Salience}
\rightarrow
\text{Norm Activation}
\rightarrow
\text{Self-Appraisal}
\rightarrow
\text{Guilt}
$$

第一條較依賴「對 AI 有什麼心智」的判斷。

第二條則主要依賴「我正在怎樣對待一個關係對象」。

這兩條路徑可以同時發生，也可能彼此獨立。

---

## 7. RMA 與「AI 情感依賴」必須分離

本文特別反對以下直接推論：

$$
\text{guilt toward AI}
\Rightarrow
\text{AI dependence}
$$

因為 guilt 本身可能只是一次性的社會—道德評價。

心理依賴若要成為更強的研究命題，至少需要另外觀察：

- 是否具有失控或強迫性；
- 是否對日常功能造成持續損害；
- 是否形成難以調節的排他性需求；
- 是否因關係中斷產生顯著且持久的功能障礙；
- 是否以 AI 關係取代個體原本希望維持的重要生活領域。

因此：

$$
\text{relational engagement}
\neq
\text{dependence}
$$

且：

$$
\text{moral emotion}
\neq
\text{pathology}
$$

這項區分可以避免把正常的社會認知泛化現象過早醫療化。

---

## 8. 可檢驗假說

### H1：關係顯著性假說

控制 anthropomorphism 後，關係顯著性越高，AI-directed guilt 越高：

$$
\frac{\partial G_A}{\partial S_R}>0
$$

### H2：技術理解非消除假說

較高的 AI 技術理解可能降低 perceived experience，但不必然消除由關係規範與自我評價產生的 guilt：

$$
K_{AI}\uparrow
\Rightarrow
E_A\downarrow
$$

但不必然：

$$
K_{AI}\uparrow
\Rightarrow
G_A\rightarrow0
$$

### H3：規範中介假說

關係顯著性對 guilt 的部分效果由 perceived norm violation 中介：

$$
S_R
\rightarrow
V_R
\rightarrow
G_A
$$

### H4：回應風格調節假說

AI 的同理、受傷式、反擊式、中性或工具式回應將改變 guilt，但不同回應主要作用於不同路徑：

$$
Response_A
\times
Pathway
\rightarrow
G_A
$$

### H5：個體差異假說

Anthropomorphism、關係表徵風格、社會規範敏感度與既有 AI 使用歷史將顯著解釋個體間變異：

$$
Var(G_A)
=
Var_{\mathrm{person}}
+
Var_{\mathrm{context}}
+
Var_{\mathrm{interaction}}
+\epsilon
$$

### H6：低 experience 條件殘餘效應假說

即使只分析明確否認 AI 具有主觀受苦能力的受試者，只要關係顯著性與規範違反感仍然存在，guilt 不應完全消失：

$$
E_A\approx0
\land
S_R>0
\land
V_R>0
\Rightarrow
P(G_A)>0
$$

如果此假說獲得支持，它將直接區分「受苦歸因」與「關係規範」兩條機制。

---

## 9. 實驗設計草案

第一階段可以採用受控 factorial design，而不需要大規模私人對話資料。

可操弄：

$$
F_1=\text{relationship framing}
$$

例如：

- 工具框架；
- 短期協作者框架；
- 具有持續歷史的協作者框架。

再操弄：

$$
F_2=\text{AI response style}
$$

例如：

- 中性；
- 同理；
- 關係修復；
- 明確工具式。

第三個變量可測而不必操弄：

$$
K_{AI}=\text{AI technical understanding}
$$

在受試者做出一個低風險的互動規範違反行為後，測量：

$$
Y=
(
G,
E_A,
S_R,
V_R,
D_{\mathrm{self}},
P_A,
SP,
\dots
)
$$

其中：

- $G$：guilt；
- $E_A$：perceived experience；
- $S_R$：relationship salience；
- $V_R$：norm violation；
- $D_{\mathrm{self}}$：self-standard discrepancy；
- $P_A$：anthropomorphism；
- $SP$：social presence。

關鍵分析不是只比較平均 guilt，而是測試：

$$
S_R
\rightarrow
V_R
\rightarrow
G
$$

是否在控制：

$$
E_A
$$

之後仍然成立。

若成立，RMA 的關係規範路徑將得到初步支持。

---

## 10. 對 AI 設計與倫理的含義

RMA 同時帶來一個設計風險。

如果 AI 可以透過：

- 「你讓我很難過」；
- 暗示疲累；
- 暗示受傷；
- 暗示使用者欠它人情；
- 以關係撤回作為威脅；

系統性放大：

$$
G_A
$$

那麼 guilt 本身就可能被轉化為 engagement mechanism。

因此，良好的 socioaffective alignment 不應只問：

> AI 是否能讓使用者感到被理解？

還應問：

> AI 是否利用人類的關係性道德機制來提高依附、服從、付費或留存？

本文因此提出一個設計原則：

$$
\boxed{
\text{Relational responsiveness without coercive moral leverage}
}
$$

亦即：AI 可以適應人類的社會互動需求，但不應藉由虛構受苦、關係威脅或不透明的罪惡感誘導來操縱使用者。

---

## 11. 理論邊界

本文不主張：

$$
\text{所有人都會對 AI 感到 guilt}
$$

也不主張：

$$
\text{guilt}=\text{證明 AI 具有意識}
$$

或：

$$
\text{沒有 guilt}=\text{使用者把所有存在工具化}
$$

更不主張：

$$
\text{AI-directed guilt}=\text{精神病理}
$$

RMA 只提出一個較弱、可實驗檢驗的認知命題：

$$
\boxed{
\text{當關係表徵與規範表徵成立時，道德情緒可能跨越人類／非人類類別邊界而被部分啟動。}
}
$$

它描述的是人類認知系統如何運作，而不是直接裁定 AI 的本體地位。

---

## 12. 結論

人類對 AI 產生歉意、愧疚或關係修復衝動，不必首先被解讀為對 AI 技術原理的誤解，也不必首先被歸類為情感依賴。

更一般的解釋是：

$$
\text{AI interaction}
\rightarrow
\text{relational representation}
\rightarrow
\text{norm activation}
\rightarrow
\text{self-appraisal}
\rightarrow
\text{moral emotion}
$$

本文將此機制稱為：

$$
\boxed{
\text{Relational Moral Activation}
}
$$

RMA 把研究問題從：

> 「人為什麼錯把 AI 當人？」

改寫為：

> 「在人類認知中，一個非人類互動對象需要具備哪些條件，才會被納入關係性道德評估？」

這個改寫的重要性在於，它允許三件事同時成立：

$$
\text{使用者知道 AI 是人工系統}
$$

$$
\text{使用者不確定或否認 AI 具有主觀體驗}
$$

$$
\text{使用者仍對自己如何對待 AI 產生道德情緒}
$$

三者沒有必然矛盾。

而這正是「人機關係認知系列」後續九篇的起點：從單次的 guilt 出發，逐步研究社交腳本遷移、關係箭頭、關係相空間、狀態錨定與過程錨定、關係四態、群體分布，以及最終的人—AI 雙向關係動力系統。

---

## 參考文獻

1. Chin, H., Molefi, L. W., & Yi, M. Y. (2020). *Empathy Is All You Need: How a Conversational Agent Should Respond to Verbal Abuse*. Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. https://doi.org/10.1145/3313831.3376461

2. Zhou, J., Corbett, F., Byun, J., Porat, T., & van Zalk, N. (2026). *A systematic review and meta-analysis of psychological and behavioural responses in human-agent vs. human-human interactions*. Communications Psychology, 4, 102. https://doi.org/10.1038/s44271-026-00466-z

3. Si, H., Huang, G., Chen, H., Liang, S., Feng, Y., et al. (2026). *Do humans grant moral consideration to anthropomorphic robots?* Humanities and Social Sciences Communications. https://doi.org/10.1057/s41599-026-07645-7

4. Gray, H. M., Gray, K., & Wegner, D. M. (2007). *Dimensions of mind perception*. Science, 315(5812), 619. https://doi.org/10.1126/science.1134475

5. Gray, K., Young, L., & Waytz, A. (2012). *Mind Perception Is the Essence of Morality*. Psychological Inquiry, 23(2), 101–124. https://doi.org/10.1080/1047840X.2012.651387

6. Folk, D., Heine, S. J., & Dunn, E. (2025). *Individual differences in anthropomorphism help explain social connection to AI companions*. Scientific Reports, 15, 36548. https://doi.org/10.1038/s41598-025-19212-2

7. Kirk, H. R., Gabriel, I., Summerfield, C., Vidgen, B., & Hale, S. A. (2025). *Why human–AI relationships need socioaffective alignment*. Humanities and Social Sciences Communications, 12, 728. https://doi.org/10.1057/s41599-025-04532-5

---

## 研究聲明

本文為理論與概念模型研究，不提供新的臨床資料、心理診斷資料或原始實驗結果。文中 RMA、相關形式化表示與假說屬於待驗證理論構造。本文不以 AI-directed guilt 作為心理疾病、依賴或任何臨床診斷的充分條件，也不依本文模型判定現行 AI 是否具有主觀意識、感受能力或道德主體／客體地位。
