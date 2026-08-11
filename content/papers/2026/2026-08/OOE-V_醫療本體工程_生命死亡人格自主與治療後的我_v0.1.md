# OOE-V：醫療本體工程
## 生命、死亡、人格、自主與治療後的「我」
### OOE-V: Medical Ontology Engineering
### Life, Death, Personhood, Agency, and the Self After Intervention

**系列**：Operational Ontology Engineering（OOE／操作本體工程）  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-09  
**版本**：v0.1  
**性質**：醫療—神經倫理—操作本體論文  
**前置論文**：  
1. 《OOE-I：本體論何時變成工程問題？》  
2. 《OOE-II：人類早就在做本體工程——操作本體技術史》  
3. 《OOE-III：本體編譯器——從模糊世界到可執行制度狀態》  
4. 《OOE-IV：法律作為文明本體編譯器》  

**前置理論**：Continuity Object Theory（COT）

---

## 摘要

法律作為操作本體編譯器，主要將模糊世界轉換成可執行的身份、資格、權利、義務與程序；醫療則多了一層更困難的結構：**醫療不只判定一個存在的狀態，也可能直接改變被判定的那個存在本身。**

傳統醫療本體問題包括生命與死亡、疾病與健康、能力與無能力；現代神經科技則進一步觸及人格、記憶、代理、自我感、語言表達與心理連續性。Deep Brain Stimulation（DBS）相關神經倫理文獻長期討論治療後可能出現的 personality、identity、agency、autonomy、authenticity 與 self 變化；腦機介面（BCI）則使「意圖」、「輸出」、「作者」與「工具」之間的邊界變得可分離。2025 年神經植入物 explantation 系統性回顧更顯示，裝置移除除了安全與醫療問題之外，也牽涉 cognition、behavior、identity、autonomy、post-trial access、financial dependence 與 neurorights。

因此本文提出：

$$
\boxed{
\text{Medical Ontology Engineering}
=
\text{Classification}
+
\text{Intervention}
+
\text{Post-Intervention Reclassification}.
}
$$

設患者在治療前為：

$$
P_t.
$$

醫療介入：

$$
\mathcal M
$$

產生：

$$
P_{t+1}
=
\mathcal M(P_t).
$$

但如果治療會改變：

$$
\text{cognition},
\text{memory},
\text{agency},
\text{personality},
\text{self-perception},
$$

那麼原本負責：

- 同意；
- 評估治療利益；
- 判斷治療後狀態；
- 決定是否繼續治療；

的主體本身，也可能成為介入的輸出之一。

本文將此稱為：

$$
\boxed{
\text{Reflexive Medical Ontology Problem}.
}
$$

亦即：

> **醫療決策的對象，同時可能是醫療決策後被重新塑造的決策者。**

本文進一步提出「治療後身份向量」、「時間索引同意」、「自我偏好衝突」、「認知共處模組」、「神經裝置依賴」、「移除後身份斷裂」、「共同代理」與「醫療本體雙重門檻」等概念，並主張未來 BCI、AI cognitive coprocessor、記憶義肢與神經調控不能只使用傳統的 efficacy–safety 二維框架，而必須加入：

$$
\boxed{
\text{identity}
+
\text{agency}
+
\text{continuity}
+
\text{authorship}
+
\text{reversibility}.
}
$$

**關鍵詞**：OOE、醫療本體工程、Deep Brain Stimulation、BCI、neurotechnology、identity、agency、autonomy、speech ownership、explantation、COT

---

# 一、法律判定存在，醫療可以改變存在

OOE-IV 將法律描述為：

$$
\mathcal C_L:
F
\rightarrow
\sigma_L.
$$

法律通常觀察：

$$
X
$$

然後決定：

$$
\text{X 算什麼？}
$$

醫療卻更接近：

$$
X_t
\xrightarrow{\mathcal M}
X_{t+1}.
$$

因此醫療同時處理：

$$
\boxed{
\text{What is }X_t?
}
$$

以及：

$$
\boxed{
\text{What should }X_{t+1}\text{ become?}
}
$$

這是 OOE 中非常特殊的一類。

---

# 二、醫療從來就不是純粹「修回原狀」

直覺上我們會把治療寫成：

$$
P_{\mathrm{ill}}
\rightarrow
P_{\mathrm{healthy}}.
$$

但現實往往更複雜。

治療可能同時改變：

$$
\mathbf S
=
(
s_{\mathrm{symptom}},
s_{\mathrm{mood}},
s_{\mathrm{cognition}},
s_{\mathrm{behavior}},
s_{\mathrm{agency}},
s_{\mathrm{identity}}
).
$$

所以：

$$
\Delta s_{\mathrm{symptom}}>0
$$

並不保證：

$$
\Delta s_i>0
\quad
\forall i.
$$

一種治療可以：

$$
\text{motor function}\uparrow
$$

同時使某些患者或觀察者感覺：

$$
\text{selfhood / personality}
$$

發生改變。

因此：

$$
\boxed{
\text{Clinical Improvement}
\neq
\text{Ontological Neutrality}.
}
$$

---

# 三、DBS：治療效果與人格問題第一次高度接近

Deep Brain Stimulation 已被用於多種神經與精神疾病相關治療研究。

相關神經倫理文獻反覆討論：

$$
\text{Personality},
\text{Identity},
\text{Agency},
\text{Authenticity},
\text{Autonomy},
\text{Self}.
$$

本文可將這些統一成：

$$
\mathbf PIAAS
=
(
P,I,A,A_u,A_t,S
).
$$

其重點不是：

> DBS 一定會把人變成另一個人。

現有研究並不足以支持這種簡單結論。

真正重要的是：

$$
\boxed{
\text{medical intervention can make identity-relevant variables clinically salient}.
}
$$

也就是某些原本主要屬於哲學語言的問題，開始出現在：

- informed consent；
- treatment evaluation；
- side-effect assessment；
- family disagreement；
- device management；

之中。

---

# 四、「治療後的我」可能與「治療前的我」評價不同

假設：

$$
P_0
$$

在治療前說：

> 我不希望治療讓我的人格產生重大變化。

治療後：

$$
P_1
$$

卻表示：

> 我喜歡現在的自己。

也可能反過來：

$$
P_0
$$

希望治療，

但：

$$
P_1
$$

認為治療後的狀態不再符合自己。

於是出現：

$$
V(P_0,P_1)
\neq
V(P_1,P_1).
$$

也就是：

> 前一個時間點的我，與後一個時間點的我，可能對「哪個我比較好」給不同答案。

本文稱為：

# Temporal Self-Evaluation Conflict
# 時間自我評價衝突

---

# 五、誰有權代表「真正的患者利益」？

傳統模型：

$$
U_{\mathrm{patient}}
$$

看似是一個穩定值。

但若治療本身會改變偏好：

$$
U_t
\rightarrow
U_{t+1},
$$

那麼：

$$
\boxed{
\text{Whose utility counts?}
}
$$

就成為醫療本體問題。

至少可能有：

$$
U_{\mathrm{pre}},
U_{\mathrm{post}},
U_{\mathrm{family}},
U_{\mathrm{clinical}}.
$$

四者不必相同。

---

# 六、不能把治療前的自己自動視為永遠最高權威

一種直覺是：

> 治療前的我才是真正的我。

但這有問題。

如果：

$$
P_0
$$

正在嚴重疾病狀態中，

而：

$$
P_1
$$

恢復大量功能，

不能只因：

$$
P_0
$$

時間上更早，就自動判定：

$$
V_{P_0}
>
V_{P_1}.
$$

否則所有能改變偏好的有效治療都會產生悖論。

---

# 七、也不能把治療後的自己自動視為最高權威

反過來也不行。

如果某介入：

$$
\mathcal M
$$

本身可能造成：

- impaired judgment；
- mania；
- impulsivity；
- altered self-assessment；

那麼：

$$
P_1
$$

對：

$$
P_1
$$

的正面評價也不能直接被當作終極證明。

所以：

$$
\boxed{
\text{Earlier self}
\neq
\text{automatic truth}
}
$$

以及：

$$
\boxed{
\text{Later self}
\neq
\text{automatic truth}.
}
$$

---

# 八、COT 可以加入醫療身份向量

令：

$$
\mathbf C_P
=
(
c_{\mathrm{memory}},
c_{\mathrm{values}},
c_{\mathrm{agency}},
c_{\mathrm{relationships}},
c_{\mathrm{narrative}},
c_{\mathrm{body}},
c_{\mathrm{commitments}}
).
$$

治療前後：

$$
\mathbf C_P(t,t+1)
$$

可以用來描述：

> 哪些部分持續、哪些部分改變？

但醫療不能簡單設：

$$
I_P<\theta
\Rightarrow
\text{bad treatment}.
$$

因為某些治療就是為了改變：

- pathological values；
- compulsions；
- maladaptive behavior；
- dysfunctional neural patterns。

所以：

$$
\boxed{
\text{Identity Change}
\neq
\text{Medical Harm}.
}
$$

---

# 九、真正需要的是「身份相關變化」與「身份傷害」分離

定義：

$$
\Delta I
=
\text{identity-relevant change}.
$$

與：

$$
H_I
=
\text{identity-related harm}.
$$

則：

$$
\boxed{
\Delta I\neq H_I.
}
$$

某些人格變化：

$$
\Delta I>0
$$

可能被患者視為：

$$
H_I<0
$$

即改善。

另一些則可能：

$$
H_I>0.
$$

所以醫療本體工程不能把：

$$
\text{change}
$$

直接等同：

$$
\text{damage}.
$$

---

# 十、醫療本體雙重門檻

傳統治療判定常考慮：

$$
B=\text{benefit},
$$

$$
R=\text{risk}.
$$

OOE-V 建議加入：

$$
I_R
=
\text{identity relevance}.
$$

因此：

$$
\mathcal M
$$

若滿足：

$$
I_R>\theta_I
$$

就觸發額外程序。

本文稱為：

# Medical Ontology Dual Threshold
# 醫療本體雙重門檻

第一門檻：

$$
R_{\mathrm{clinical}}>\theta_C.
$$

第二門檻：

$$
I_R>\theta_I.
$$

即：

> 有些介入即使身體風險不特別高，只要高度介入記憶、人格、代理或自我，也應啟動額外本體治理。

---

# 十一、Informed Consent 必須變成時間索引

一般寫：

$$
Consent(P,\mathcal M)=1.
$$

但若：

$$
P_t
\neq
P_{t+1}
$$

在偏好與認知上明顯改變，

更合理的是：

$$
\boxed{
Consent(P,t,\mathcal M,K).
}
$$

也就是同意必須帶：

- 人；
- 時間；
- 介入；
- 情境。

本文稱為：

# Temporally Indexed Consent
# 時間索引同意

---

# 十二、同意不應只有植入前一次

對神經裝置而言：

$$
Consent_{implant}
$$

未必足夠涵蓋：

- firmware update；
- algorithm update；
- AI model change；
- new data use；
- stimulation policy change；
- explantation。

因此：

$$
\boxed{
\text{Neurotechnology Consent}
=
\text{Lifecycle Consent}.
}
$$

可寫：

$$
C=
\{
C_{\mathrm{implant}},
C_{\mathrm{update}},
C_{\mathrm{data}},
C_{\mathrm{mode}},
C_{\mathrm{explant}}
\}.
$$

---

# 十三、BCI：意圖和輸出開始分離

傳統說話：

$$
\text{intention}
\rightarrow
\text{motor speech}
\rightarrow
\text{utterance}.
$$

Speech BCI 可能是：

$$
N
\rightarrow
D
\rightarrow
L
\rightarrow
Y,
$$

其中：

- $N$：neural signal；
- $D$：decoder；
- $L$：language model / predictive layer；
- $Y$：輸出。

所以：

$$
\boxed{
Y
\neq
N
}
$$

的直接逐字映射。

---

# 十四、Speech Ownership 問題

假設使用者想表達：

$$
m.
$$

BCI 解碼：

$$
\hat m.
$$

語言模型再補全：

$$
y=f(\hat m,L).
$$

那麼：

$$
Authorship(y)
$$

應該歸誰？

候選包括：

$$
A_H=\text{human},
$$

$$
A_D=\text{decoder},
$$

$$
A_L=\text{language model},
$$

$$
A_S=\text{system}.
$$

最簡單的「全算使用者說的」可能在日常溝通足夠。

但在：

- 法律同意；
- 金融交易；
- 遺囑；
- 醫療指令；

中可能不夠。

---

# 十五、共同代理

本文提出：

$$
\boxed{
A_{\mathrm{joint}}
=
\text{Jointly Mediated Agency}.
}
$$

輸出：

$$
Y
$$

可以是：

$$
Y
=
f(
I_H,
D,
L,
C_H
),
$$

其中：

- $I_H$：human intention；
- $D$：decoder contribution；
- $L$：language-model contribution；
- $C_H$：human confirmation / correction。

因此：

$$
\boxed{
\text{agency}
}
$$

可以不是只有：

$$
\text{human}
\quad/\quad
\text{machine}
$$

二元。

---

# 十六、User Control 是本體控制介面

Speech-BCI 神經倫理研究強調 user-control 的重要性。

從 OOE 看，user-control 不只是 UI 好不好用。

它是在提供：

$$
\boxed{
\text{ontology correction channel}.
}
$$

使用者可以告訴系統：

> 這不是我要說的。

因此：

$$
Y_{\mathrm{system}}
$$

不應自動：

$$
Y_{\mathrm{system}}
=
Y_{\mathrm{self}}.
$$

需要：

$$
C_H
$$

作為身份／代理校驗。

---

# 十七、但完全逐字確認可能又失去 BCI 功能

如果每個字都要求：

$$
C_H=1
$$

才輸出，

BCI 的速度與便利：

$$
U_{\mathrm{communication}}
$$

可能大幅下降。

所以又回到 OOE：

$$
\boxed{
\text{agency preservation}
\leftrightarrow
\text{functional utility}
}
$$

的最佳化。

低風險對話可以高自動補全。

高風險法律陳述應提高確認門檻。

所以：

$$
\theta_{\mathrm{confirmation}}
=
f(K,R).
$$

---

# 十八、神經裝置：工具還是身體的一部分？

假設使用者使用裝置：

$$
D.
$$

早期：

$$
D=\text{external tool}.
$$

長期使用後：

$$
D
$$

可能成為：

- 行動能力來源；
- 溝通能力來源；
- 記憶來源；
- 疾病控制來源。

因此：

$$
\boxed{
\text{Tool}
\rightarrow
\text{Prosthesis}
\rightarrow
\text{Integrated Functional Component}.
}
$$

這是一條連續光譜。

---

# 十九、裝置依賴度

本文定義：

$$
\boxed{
D_N
=
\text{Neurodevice Dependency}.
}
$$

可以寫：

$$
D_N
=
f(
F_L,
T_U,
A_R,
S_I
),
$$

其中：

- $F_L$：失去裝置造成的功能損失；
- $T_U$：長期使用時間；
- $A_R$：替代方案可用性；
- $S_I$：使用者主觀整合程度。

如果：

$$
D_N\uparrow,
$$

裝置移除就不能只被視為：

$$
\text{remove hardware}.
$$

---

# 二十、Explantation：移除硬體可能同時移除功能與自我結構

2025 年神經裝置 explantation 的系統性回顧指出，移除決策除了感染、醫療併發症等傳統理由之外，也涉及 cognition、behavior、emotional well-being、identity、autonomy、financial issues 與 post-trial considerations。

這使：

$$
\boxed{
\text{explantation}
\neq
\text{ordinary device disposal}.
}
$$

尤其當：

$$
D_N\gg0,
$$

可能：

$$
\text{Device Removal}
\rightarrow
\text{Functional Discontinuity}
+
\text{Psychological Discontinuity}.
$$

---

# 二十一、醫療裝置停止服務也可能成為本體事件

未來神經裝置可能依賴：

- proprietary software；
- cloud service；
- model updates；
- manufacturer support。

如果：

$$
Service=0
$$

導致：

$$
D_{\mathrm{function}}\rightarrow0,
$$

那麼企業倒閉、試驗結束或停止更新就可能不只是：

$$
\text{consumer support problem}.
$$

而是：

$$
\boxed{
\text{medical continuity problem}.
}
$$

---

# 二十二、裝置退出權與裝置持續權可能衝突

傳統研究倫理強調：

$$
\text{right to withdraw}.
$$

但若患者高度依賴植入物：

$$
D_N\gg0,
$$

可能同時出現：

$$
\boxed{
\text{right to exit}
}
$$

與：

$$
\boxed{
\text{interest in continuity of access}.
}
$$

甚至：

> 研究結束後誰負責維持裝置？

這已不是純粹 consent 問題。

而是：

$$
\text{continuity obligation}.
$$

---

# 二十三、醫療本體中的「人—裝置共生狀態」

不需要宣稱：

> 裝置真的成為人的靈魂。

只要功能上：

$$
F(P+D)
\gg
F(P),
$$

且：

$$
D_N
$$

長期很高，

制度就可能需要定義：

$$
\boxed{
S_{\mathrm{symbiotic}}
=
\text{Human–Device Integrated State}.
}
$$

這是一個操作本體分類。

不是形上學宣告。

---

# 二十四、BCI + AI 會把問題再往前推

當：

$$
D
$$

內部再包含：

$$
AI,
$$

則：

$$
P
+
D
+
AI
$$

可能構成一個閉環：

$$
\text{brain}
\rightarrow
\text{AI inference}
\rightarrow
\text{output / stimulation}
\rightarrow
\text{brain}.
$$

此時：

$$
\boxed{
\text{human acts on AI}
}
$$

與：

$$
\boxed{
\text{AI acts on human}
}
$$

同時存在。

---

# 二十五、認知共處模組

本文提出：

$$
\boxed{
C_M
=
\text{Cognitive Co-Processing Module}.
}
$$

它位於：

$$
\text{tool}
$$

與：

$$
\text{self component}
$$

之間。

例如未來：

- memory retrieval AI；
- planning assistant；
- speech completion；
- attention regulation；
- implanted neuro-AI module。

都可以是：

$$
C_M.
$$

其身份權重：

$$
w_{C_M}
$$

可以隨使用深度逐漸上升。

---

# 二十六、醫療與增強的邊界也會變成 OOE

傳統：

$$
\text{therapy}
\neq
\text{enhancement}.
$$

但什麼叫恢復「正常」？

若：

$$
F_{\mathrm{post}}
>
F_{\mathrm{population\ baseline}},
$$

治療何時變增強？

或者一名患者原本的能力：

$$
F_0
$$

遠高於平均，

受傷後：

$$
F_1.
$$

恢復到：

$$
F_0
$$

對平均人可能已屬「增強」。

所以：

$$
\boxed{
\text{Therapy / Enhancement}
}
$$

本身也是 context-relative operational ontology。

---

# 二十七、「正常」不是純自然值

定義：

$$
N=
\text{normal}.
$$

它可能同時包含：

$$
N_{\mathrm{statistical}},
N_{\mathrm{functional}},
N_{\mathrm{social}},
N_{\mathrm{personal}}.
$$

四者可以：

$$
\neq.
$$

因此醫療如果使用：

$$
\text{normal}
$$

而不說明是哪一個 normal，

本身就在隱性編譯本體。

---

# 二十八、醫療的風險函數需要擴張

傳統：

$$
L_{\mathrm{medical}}
=
L_{\mathrm{mortality}}
+
L_{\mathrm{morbidity}}.
$$

OOE-V 建議加入：

$$
L_{\mathrm{identity}},
$$

$$
L_{\mathrm{agency}},
$$

$$
L_{\mathrm{continuity}},
$$

$$
L_{\mathrm{dependency}},
$$

$$
L_{\mathrm{authorship}}.
$$

所以：

$$
\boxed{
L_M
=
L_{\mathrm{physical}}
+
L_{\mathrm{cognitive}}
+
L_{\mathrm{identity}}
+
L_{\mathrm{agency}}
+
L_{\mathrm{continuity}}.
}
$$

---

# 二十九、但身份不能凌駕治療效益

這一點同樣需要限制。

不能因：

$$
I_R>0
$$

就說：

> 不應改變病人的任何人格相關特徵。

否則：

- depression；
- OCD；
- addiction；
- severe compulsions；

等治療本身就可能被錯誤理解。

所以：

$$
\boxed{
\text{identity preservation}
}
$$

不是：

$$
\boxed{
\text{state preservation at all costs}.
}
$$

真正要求的是：

$$
\boxed{
\text{identity-relevant changes must be disclosed, monitored, and governed}.
}
$$

---

# 三十、醫療本體編譯器

本文定義：

$$
\boxed{
\mathcal C_M:
(P_t,D,E,K,V,R,H)
\rightarrow
(\sigma_M,\rho_M,\gamma,\tau,\nu)
}
$$

其中：

- $P_t$：患者當下狀態；
- $D$：裝置／治療；
- $E$：醫療與主觀證據；
- $K$：決策情境；
- $V$：患者價值、權利與臨床倫理；
- $R$：風險；
- $H$：治療歷史；
- $\sigma_M$：操作醫療本體狀態；
- $\rho_M$：允許的醫療動作。

---

# 三十一、醫療證據必須包含第一人稱資料

對人格、agency、identity 問題，

只有：

$$
E_{\mathrm{clinical}}
$$

不夠。

還需要：

$$
E_{\mathrm{self-report}},
$$

$$
E_{\mathrm{family}},
$$

$$
E_{\mathrm{behavioral}}.
$$

但四者可能衝突。

因此：

$$
\boxed{
\text{medical ontology requires multi-perspective evidence}.
}
$$

---

# 三十二、第一人稱不能被醫學數據完全吞掉

如果患者說：

> 我不再覺得這是我。

不能單純用：

$$
\text{motor score improved}
$$

把它覆蓋掉。

因為：

$$
\boxed{
\text{clinical success metric}
\neq
\text{complete patient welfare}.
}
$$

反之，第一人稱也不能在所有情況完全凌駕其他證據。

所以需要：

$$
\text{Conflict Register}.
$$

---

# 三十三、醫療身份覆核

若：

$$
\Delta I>\theta_I,
$$

應啟動：

$$
\boxed{
\text{Identity Review}.
}
$$

可能包括：

- patient interview；
- neuropsychological assessment；
- longitudinal comparison；
- family input；
- device parameter review；
- independent ethics consultation。

這不是要法院判：

> 你是不是另一個人。

而是：

> 這個治療是否產生足以改變照護決策的身份相關變化？

---

# 三十四、正式命題一：反身介入命題

如果：

$$
P_{t+1}
=
\mathcal M(P_t)
$$

且：

$$
\mathcal M
$$

會改變患者的：

$$
V,
A,
C
$$

等決策相關變量，

則：

$$
\boxed{
\text{medical decision subject is endogenous to treatment}.
}
$$

---

# 三十五、正式命題二：身份變化—傷害分離命題

$$
\boxed{
\Delta I
\neq
H_I.
}
$$

身份相關改變不應自動被分類為醫療傷害。

---

# 三十六、正式命題三：時間自我衝突命題

若：

$$
V(P_t,P_{t+1})
\neq
V(P_{t+1},P_{t+1}),
$$

則：

$$
\boxed{
\text{Temporal Self-Evaluation Conflict}
}
$$

存在，需額外治理。

---

# 三十七、正式命題四：生命週期同意命題

對會持續更新或長期依賴的神經科技：

$$
\boxed{
Consent_{\mathrm{initial}}
\not\Rightarrow
Consent_{\mathrm{lifecycle}}.
}
$$

應建立：

$$
C(t,K).
$$

---

# 三十八、正式命題五：共同代理命題

若輸出：

$$
Y=f(H,D,AI),
$$

則：

$$
\boxed{
Authorship(Y)
}
$$

不應必然被壓成單一：

$$
\text{human}
\quad/\quad
\text{machine}.
$$

可存在 jointly mediated agency。

---

# 三十九、正式命題六：神經依賴命題

若：

$$
D_N\uparrow,
$$

則：

$$
\boxed{
C_{\mathrm{explant}}
+
C_{\mathrm{service\ termination}}
\uparrow.
}
$$

也就是高度整合裝置的移除／停服需要更高程序與倫理門檻。

---

# 四十、正式命題七：醫療本體雙門檻命題

即使：

$$
R_{\mathrm{physical}}
$$

可接受，

若：

$$
I_R>\theta_I,
$$

仍應觸發：

$$
\boxed{
\text{enhanced consent + monitoring + review}.
}
$$

---

# 四十一、正式命題八：身份資料多視角命題

對 identity-relevant intervention：

$$
E
=
E_{\mathrm{clinical}}
+
E_{\mathrm{self}}
+
E_{\mathrm{behavioral}}
+
E_{\mathrm{relational}}.
$$

任何單一來源都不應自動具有：

$$
w=1.
$$

---

# 四十二、正式命題九：可逆優先命題

在本體不確定性高且可能影響人格／代理時：

$$
U_O\uparrow
$$

應提高：

$$
\boxed{
P(\text{reversible intervention})}.
$$

若有等效治療選項，

優先可調、可停、可回復方案。

---

# 四十三、可反駁預測

若 OOE-V 模型有用，應看到：

第一，identity-relevant intervention 的患者評價不能被臨床 symptom score 完整預測。

第二，治療前後患者可能對同一狀態給不同價值判斷。

第三，BCI 語言模型參與度提高時，對 user-control、authorship 與 confirmation threshold 的需求增加。

第四，神經裝置依賴度越高，explantation 與 service discontinuation 的倫理成本越高。

第五，時間與情境特定的 consent / capacity 模型，比單次永久同意更能處理長期神經科技。

第六，將身份相關改變明確納入追蹤，可以提早發現傳統 adverse-event framework 未捕捉的問題。

---

# 四十四、反論一：這是不是把醫療哲學化過頭？

如果只是一般骨折：

$$
\Delta I\approx0,
$$

則 OOE-V 幾乎不增加負擔。

OOE 不是要求每個感冒都討論忒修斯之船。

它只在：

$$
I_R>\theta_I
$$

時啟動。

因此：

$$
\boxed{
\text{ontology governance should be risk-triggered}.
}
$$

---

# 四十五、反論二：人格改變本來就是心理學問題

是，但 OOE 關心的是：

> 什麼時候人格改變開始影響同意、權利、裝置移除、治療持續與身份責任？

此時問題已跨入：

$$
\boxed{
\text{psychology}
+
\text{medicine}
+
\text{ontology}
+
\text{governance}.
}
$$

---

# 四十六、反論三：只要患者說好不就好了？

如果：

$$
Capacity=1,
$$

患者價值當然應具有高度權重。

但 OOE-V 特別研究：

- capacity 會被介入改變；
- preference 會被介入改變；
- system output 可能不是完全由患者生成；

的情況。

所以問題恰恰是：

$$
\boxed{
\text{who is the consenting self across intervention?}
}
$$

不能用一句「尊重患者」跳過時間結構。

---

# 四十七、與 WHO / OECD 神經科技治理的接口

WHO 2025 全球神經科技分析已把：

- BCI；
- neuromodulation；
- neurological devices；

列為快速發展的重要神經科技類別，同時指出臨床採用仍面臨多重挑戰。

OECD 自 2019 年起的 responsible neurotechnology framework 則持續強調：

- safety；
- privacy；
- stewardship；
- oversight；
- societal deliberation；
- unintended use；

並指出 brain and cognition 與 human identity、agency、accountability 之間存在特殊治理關聯。

這表示醫療本體問題已不只是理論預測。

治理體系本身已開始把：

$$
\boxed{
\text{identity / agency}
}
$$

視為神經科技需要提前處理的問題域。

---

# 四十八、未來真正麻煩的是漸進式後人類化

最戲劇化的情境是：

$$
Human
\rightarrow
Upload.
$$

但更可能先出現：

$$
H_0
\rightarrow
H_1
\rightarrow
H_2
\rightarrow
\cdots
\rightarrow
H_n,
$$

其中每一步只增加：

- neuroprosthesis；
- memory support；
- AI planning；
- attention modulation；
- sensory extension。

如果每一步：

$$
I(H_t,H_{t+1})\approx1,
$$

最後：

$$
H_n
$$

可能和：

$$
H_0
$$

在認知架構上非常不同。

這就是：

$$
\boxed{
\text{Clinical Ship of Theseus}.
}
$$

---

# 四十九、這將直接接回 COT

COT 問：

$$
\boxed{
\text{What must persist?}
}
$$

OOE-V 問：

$$
\boxed{
\text{What may medicine ethically change while still treating the same patient as the bearer of continuing rights and commitments?}
}
$$

所以醫療不是 COT 的邊緣案例。

它可能是 COT 最困難的應用之一。

---

# 五十、與 OOE-VI 的接口

到目前為止：

OOE-IV 處理：

$$
\text{法律如何給身份}.
$$

OOE-V 處理：

$$
\text{醫療如何改變身份相關狀態}.
$$

下一篇要進入一個更政治的問題：

> 如果實際能力與制度地位開始脫離，而制度只靠「我不承認」來維持舊分類，會發生什麼？

因此下一篇為：

# 《OOE-VI：身份否認不會消除問題——能力—地位解耦、治理承認落差與本體治理債》

其核心將是：

$$
C_A
=
\text{actual capability},
$$

$$
S_A
=
\text{recognized status},
$$

以及：

$$
\boxed{
G_{\mathrm{gap}}
=
d(C_A,S_A).
}
$$

---

# 五十一、結論

醫療本體工程最核心的特殊性，可以濃縮成：

$$
\boxed{
\text{Medicine does not merely classify the subject;
it can transform the subject that performs and receives the classification.}
}
$$

因此：

$$
P_t
\xrightarrow{\mathcal M}
P_{t+1}
$$

不是普通狀態轉換。

因為：

$$
P_{t+1}
$$

可能具有不同：

- cognition；
- agency；
- values；
- preferences；
- self-perception。

這意味未來神經醫療與 BCI 不能只問：

$$
\boxed{
\text{Did the treatment work?}
}
$$

還必須問：

$$
\boxed{
\text{What did the treatment change about the person who decides whether it worked?}
}
$$

Speech BCI 又進一步要求：

$$
\boxed{
\text{Who authored the output?}
}
$$

神經植入與 explantation 則要求：

$$
\boxed{
\text{When does a device cease to be merely replaceable hardware and become part of a person's functional continuity?}
}
$$

這些問題不要求我們先證明靈魂、本體自我或意識的終極理論。

它們只要求承認：

$$
\boxed{
\text{identity-relevant variables have entered clinical decision space}.
}
$$

當這件事發生時，

它們就跨過：

$$
\text{Operational Ontology Threshold}.
$$

這正是 OOE-V 所要建立的核心命題。

---

## 初版參考文獻與研究接口

1. WHO, *Landscape analysis of the opportunities and challenges for neurotechnology in global health*, 2025.
2. OECD, *Recommendation on Responsible Innovation in Neurotechnology* 及 Neurotechnology Policy Toolkit。
3. OECD, *Brain-computer interfaces and the governance system: Upstream approaches*, 2022.
4. Vooijs M. et al., “Ethical, legal, and sociocultural considerations in neural device explantation: a systematic review,” 2025.
5. Gilbert F. et al. 及相關 DBS literature on personality, identity, agency, authenticity, autonomy and self.
6. “Current Neuroethical Perspectives on Deep Brain Stimulation and Neuromodulation for Neuropsychiatric Disorders,” 2025.
7. Freudenburg Z., Berezutskaya J., Herbert C., “The ethics of speech ownership in the context of neural control of augmented assistive communication,” 2024.
8. van Stuijvenberg O.C. et al., “The ethical significance of user-control in AI-driven speech-BCIs,” 2024.
9. “Recommendations for promoting user agency in the design of speech neuroprostheses,” 2023.
10. OOE-I–IV 與 COT。

---

## 版本註記

v0.1 已重新查核 WHO 2025 neurotechnology landscape、OECD neurotechnology governance、DBS identity/personality literature、speech-BCI user-control / speech ownership，以及 2025 neural-device explantation systematic review。

v0.2 應進一步：

1. 建立 Medical Identity Vector 的臨床量表接口；
2. 定義 Identity-Relevance Score $I_R$ ；
3. 形式化 Temporal Self-Evaluation Conflict；
4. 建立 Lifecycle Consent state machine；
5. 建立 BCI Authorship / Agency attribution matrix；
6. 建立 Neurodevice Dependency $D_N$ 指標；
7. 比較 implantation / adjustment / explantation 三種本體事件；
8. 建立 Clinical Ship of Theseus 的漸進替換思想實驗；
9. 加入 psychiatric treatment、memory intervention 與 cognitive enhancement 對照案例。
