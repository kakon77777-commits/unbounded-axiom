# 日本悖論 IV：家與血都只是故事的載體？
## 敘事正統場、「看空氣」與分散式社會計算
### Japan Paradox IV: Are Blood and House Merely Carriers of a Larger Story?

**系列**：日本悖論研究系列  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-07  
**性質**：探索性理論模型／跨人類學、制度經濟學與認知博弈論的待驗證框架  
**前置論文**：  
1. 《日本悖論 I：小幾何空間何以形成高政治碎片化？》  
2. 《日本悖論 II：個體會死，家為何不死？》  
3. 《日本悖論 III：血統重要，還是家系重要？》

**核心新增概念**：

$$
\mathcal N_H(t)
=
\text{Narrative–Legitimacy Field}
$$

以及：

$$
l_i(H)
=
f\!\left(
x_i,
E_i[l_j(H)]
\right)
$$

本文把後者稱為：

$$
\boxed{
\text{Recursive Social Estimation}
}
$$

---

## 摘要

日本悖論 III 已指出，「血統」與「家系」並非真正的二選一。實際遺傳親緣、系譜合法性、家系延續、財產、家格、婚姻、職位與社會承認，都可以被視為不同的正統性輸入。然而，這又留下更上層問題：**為什麼某些血統、某個主家、某一段祖先故事、某種爵位或某一條系譜路徑，能在社會中產生持續而真實的政治效果？**

本文提出「敘事正統場」（Narrative–Legitimacy Field）作為候選答案。某一家、王朝、皇室或其他跨世代身份單位的正統性，並非存在於單一個體內部，而是分散存在於家族成員、其他家系、政府、宗教、地方共同體、史書、儀式、媒體與公眾彼此對彼此的預期之中。每一個行動者不只判斷「我認為它正不正統」，也會估計「其他人是否認為它正統」以及「其他人是否認為大家都會承認它」。因此，正統性可以被理解為高階信念、共同知識、慣例、象徵中心性與制度承認共同形成的分散式社會狀態。

本文借用日本日常語言中的「空気を読む／看空氣」作為直觀入口，但不把「看空氣」視為日本民族本質。相關日本研究確實曾將「空氣」理解為具有社會壓力的 opinion climate；而博弈論與制度理論則早已指出，協調結果取決於人們對他人行為及他人信念的高階預期。本文試圖將這兩條研究線與 House Society、系譜正統性及家制度結合。

核心命題是：血統、家名與財產不必是終極價值，它們可以作為維持某個「被共同承認的故事」的載體。當該故事具有高歷史深度、高制度嵌入、高網路中心性與高共同信念時，一次養子、婚姻、名稱改變甚至部分血緣中斷，未必足以讓其歸零。相反，如果共同承認崩潰，即使 DNA、財產或名稱形式上仍然存在，正統性也可能迅速下降。

**關鍵詞**：日本悖論、敘事正統場、看空氣、空気、共同信念、高階信念、House Society、家系、血統、正統性、分散式社會計算

---

# 一、第三篇之後，真正剩下的問題

日本悖論 III 已將正統性拆成：

$$
B_G
=
\text{Genetic Relatedness},
$$

$$
B_D
=
\text{Genealogical Legitimacy},
$$

$$
H
=
\text{House Continuity}.
$$

並提出：

$$
\mathcal L_j
=
F_j(
B_G,
B_D,
H,
P,
R,
F,
C,\ldots
).
$$

但這仍然只是列出：

> 哪些東西可能重要。

它沒有回答：

> 為什麼這些東西會重要？

例如：

為什麼「主家」比血緣相近的分家更有權威？

為什麼一個養子進入某家後，大家可以逐漸把他視為那個家的人？

為什麼某條古老系譜即使已經相隔數百年，仍然能提供政治象徵價值？

為什麼某個頭銜失去法律權力後，仍可能留下社會影響力？

所以我們需要：

$$
\boxed{
\mathcal L
\text{ 的生成機制}
}
$$

而不只是：

$$
\mathcal L
\text{ 的輸入項目}.
$$

---

# 二、敘事正統場

本文定義：

$$
\boxed{
\mathcal N_H(t)
=
\text{Narrative–Legitimacy Field of House }H.
}
$$

它表示在時間 $t$ ，一個家、王朝、皇室或其他歷史身份單位，在相關社會網絡中的綜合敘事—正統性狀態。

可以暫時寫成：

$$
\mathcal N_H
=
F(
B_D,
H,
R,
P,
T,
M,
A,
I,
C
),
$$

其中：

- $B_D$ ：被承認的系譜位置；
- $H$ ：家系持續；
- $R$ ：家格與身份；
- $P$ ：財產、職位與制度資源；
- $T$ ：歷史時間深度；
- $M$ ：集體記憶與故事；
- $A$ ：婚姻、盟友與關係網絡；
- $I$ ：國家、宗教、法律與儀式承認；
- $C$ ：社會共同承認。

但與前一篇不同的是：

$$
C
$$

不再只是單一輸入。

它會反過來改變其他變量的意義。

如果沒有人承認某家譜：

$$
B_D
$$

的政治價值就可能接近零。

如果沒有人承認某頭銜：

$$
R
$$

也可能只剩私人自稱。

因此：

$$
\boxed{
\mathcal N_H
\text{ is reflexive}.
}
$$

---

# 三、正統性不是「我相信」就夠了

設社會中有：

$$
N=\{1,2,\ldots,n\}
$$

個相關行動者。

每一個行動者 $i$ 對家 $H$ 有一個判斷：

$$
l_i(H).
$$

如果正統性只是私人偏好，可以寫：

$$
l_i(H)=f(x_i).
$$

但實際上，政治與社會身份通常不是這麼運作。

行動者還會問：

> 別人承不承認？

所以：

$$
l_i(H)
=
f(
x_i,
E_i[l_j(H)]
).
$$

更進一步：

$$
l_i(H)
=
f(
x_i,
E_i[l_j(H)],
E_i[E_j[l_k(H)]],
\ldots
).
$$

因此出現：

$$
\boxed{
\text{beliefs about beliefs}.
}
$$

這與博弈論中的 higher-order beliefs 具有直接結構相似性。

---

# 四、「大家都知道」和「大家都知道大家知道」不同

假設：

$$
E
=
\text{「H 是具有正統性的家」}.
$$

第一層：

$$
K_i(E)
$$

表示我知道 $E$ 。

第二層：

$$
K_iK_j(E)
$$

表示我知道你知道 $E$ 。

再往上：

$$
K_iK_jK_k(E).
$$

如果形成 sufficiently deep mutual expectation，

行動者才可能放心依照它行動。

例如：

> 我自己相信某一家很有地位。

沒有太大政治效果。

但是：

> 我相信政府會承認它、其他貴族會承認它、婚姻市場會承認它，而且大家都知道大家會承認它。

情況完全不同。

這就開始接近：

$$
\boxed{
\text{Common Knowledge / Common Belief}.
}
$$

博弈論研究已反覆顯示，協調不只受個體一階信念影響，高階信念本身也可以改變是否成功協調。

---

# 五、「看空氣」作為遞迴估計

本文不把「空気を読む」當成日本特有的心理器官。

只把它作為一個非常直觀的文化語言：

> 我不只看事情本身，我還看在場其他人如何理解事情。

形式上：

$$
a_i
=
\pi_i(
x_i,
E_i[a_j],
E_i[E_j[a_k]],
\ldots
).
$$

行動者 $i$ 的行動，

不只取決於：

$$
x_i,
$$

還取決於：

$$
\text{我認為別人會怎麼行動}.
$$

這可以稱為：

$$
\boxed{
\text{Recursive Social Estimation}.
}
$$

日本「空氣」研究曾把 kuuki 描述為一種 opinion climate：公共、媒體與政府等不同部門的意見氣候會互相作用，並形成要求順應的社會壓力。

因此「看空氣」至少可以作為本文模型的一個經驗入口。

但：

$$
\boxed{
\text{Recursive Social Estimation}
\neq
\text{Japanese-only phenomenon}.
}
$$

所有具有社會規範、聲譽、慣例與正統性的社會，都可能出現這類機制。

---

# 六、從「空氣」到社會場

如果每個人都在估計其他人：

$$
l_i
=
f(
x_i,
E_i[l_{-i}]
),
$$

那麼整體正統性就不能只用：

$$
\sum_i l_i
$$

表示。

因為：

$$
l_i
$$

彼此互相依賴。

更適合寫成：

$$
\mathbf l
=
\mathbf F(
\mathbf x,
\mathbf W,
\mathbf l
),
$$

其中：

- $\mathbf l$ ：所有行動者的正統性判斷；
- $\mathbf x$ ：史實、家譜、財產、儀式等外部訊號；
- $\mathbf W$ ：社會影響網絡；
- $\mathbf l$ 本身再次進入函數。

穩定狀態滿足：

$$
\boxed{
\mathbf l^*
=
\mathbf F(
\mathbf x,
\mathbf W,
\mathbf l^*
).
}
$$

這就是一個社會固定點。

本文稱其宏觀結果為：

$$
\mathcal N_H^*.
$$

---

# 七、所以「故事」不是假的

這裡需要避免一個常見誤解。

說正統性是「故事」，

並不等於：

> 它不真實。

貨幣、國家、公司、爵位、法律身份與婚姻都具有高度社會建構性，但它們可以造成非常真實的資源配置結果。

因此：

$$
\text{Narrative}
\neq
\text{fiction with no causal force}.
$$

更準確的是：

$$
\boxed{
\text{Collectively recognized narrative}
\rightarrow
\text{real behavioral constraints}.
}
$$

如果所有相關行動者都預期：

> H 家具有某種地位，

那麼：

- 婚姻選擇；
- 官職選擇；
- 禮儀排序；
- 財產交易；
- 政治聯盟；
- 媒體描述；

都可能依照這個預期行動。

於是故事反過來生成現實。

---

# 八、自我實現與自我耗散

設：

$$
\mathcal N_H(t)
$$

代表當期正統場。

若高正統性帶來：

$$
\text{better alliances}
+
\text{resources}
+
\text{marriages}
+
\text{visibility},
$$

則：

$$
\mathcal N_H(t)
\uparrow
\Rightarrow
\Delta \mathcal N_H(t+1)>0.
$$

形成：

$$
\boxed{
\text{positive feedback}.
}
$$

反過來，如果：

- 國家撤銷承認；
- 其他家不再通婚；
- 社會不再相信其家譜；
- 財產與儀式中心消失；
- 公眾停止使用舊稱號；

可能：

$$
\mathcal N_H(t)
\downarrow
\Rightarrow
\Delta\mathcal N_H(t+1)<0.
$$

形成：

$$
\boxed{
\text{legitimacy decay}.
}
$$

所以正統性不是靜態資產。

它是一個動態、反身的社會狀態。

---

# 九、歷史時間本身也是一個放大器

一個新興家與一個被承認延續數百年的家，

即使今天擁有相同財產：

$$
P_A=P_B,
$$

也未必具有：

$$
\mathcal N_A=\mathcal N_B.
$$

因為歷史本身可以累積：

$$
T_H.
$$

可以粗略寫：

$$
M_H(t+1)
=
(1-\delta)M_H(t)
+
\Delta M_H(t),
$$

其中：

- $M_H$ ：歷史—敘事資本；
- $\delta$ ：遺忘與失真率；
- $\Delta M_H$ ：新事件、新儀式、新記錄與新故事。

若：

$$
\delta
$$

很低，

且家譜、儀式、檔案、建築、墓地、姓氏與公共記憶持續存在，

歷史深度就可能產生：

$$
\boxed{
\text{temporal legitimacy compounding}.
}
$$

---

# 十、主家為什麼可能比分家更「像原本的家」

第三篇已提出：

$$
C_{\mathrm{main}}
>
C_{\mathrm{branch}}.
$$

本篇可以更進一步：

主家是：

$$
\boxed{
\text{Narrative Hub}.
}
$$

它可能同時控制：

- 核心祖先祭祀；
- 家譜；
- 本邸；
- 祖產；
- 主要家名；
- 家督；
- 象徵物；
- 對分家的認證；
- 主要歷史故事。

因此在系譜圖上：

$$
d_{\mathrm{genealogy}}
$$

不是唯一距離。

還需要：

$$
d_{\mathrm{narrative}}.
$$

某個分家可能生物上非常近，

但在象徵網絡中：

$$
d_{\mathrm{narrative}}
$$

更遠。

所以：

$$
\boxed{
\text{main/branch distinction}
\text{ can be a centrality relation rather than a blood-percentage relation}.
}
$$

---

# 十一、養子為什麼常常不會破壞整個故事？

假設：

$$
\mathcal N_H(t)
$$

已非常高。

現在加入一位養子：

$$
A.
$$

養子可能使：

$$
B_G
$$

下降。

但如果：

$$
H,
B_D,
R,
P,
I,
C
$$

大部分仍然維持，

則：

$$
\Delta\mathcal N_H
$$

可能很小。

甚至，如果養子：

- 能力更強；
- 家格適配；
- 與原家存在親族／婚姻關係；
- 被制度正式承認；

那麼：

$$
\Delta\mathcal N_H>0
$$

都有可能。

因此：

$$
\boxed{
\text{local discontinuity}
\not\Rightarrow
\text{global narrative collapse}.
}
$$

這就是前面所說：

> 養子可能被家吸收。

的場模型版本。

---

# 十二、皇室：敘事正統場的極端案例

皇室與普通家最大的差異之一，

可能不是：

$$
H
$$

本身，

而是：

$$
\mathcal N_H
$$

具有極高公共可見性。

皇室正統性受到：

- 法律；
- 儀式；
- 國家機構；
- 教育；
- 歷史敘事；
- 國際外交；
- 媒體；

共同參與。

因此：

$$
\boxed{
\mathcal N_{\mathrm{Imperial}}
\text{ is a high-density public legitimacy field}.
}
$$

一個普通商家換養子，

可能只需要：

$$
N_{\mathrm{relevant}}
$$

中的少數人承認。

皇室的任何繼承調整，

卻會讓：

$$
N_{\mathrm{relevant}}
$$

擴展到幾乎整個政治共同體。

所以其：

$$
C_{\mathrm{coordination}}
$$

與：

$$
C_{\mathrm{legitimacy\ update}}
$$

都會更高。

這可能解釋為什麼皇室規則變動特別緩慢。

---

# 十三、正統性更新成本

本文新增一個變量：

$$
C_U
=
\text{Legitimacy Update Cost}.
$$

如果某個身份只被五個人承認，

修改規則很容易。

如果它被：

$$
10^6
$$

甚至：

$$
10^8
$$

人以不同方式理解，

要讓整個社會重新協調：

$$
\mathcal N_H
\rightarrow
\mathcal N_H'
$$

成本就很高。

因此：

$$
\boxed{
C_U
=
F(
N,
D,
I,
T,
Q
)
}
$$

其中：

- $N$ ：相關行動者數量；
- $D$ ：認知分歧程度；
- $I$ ：制度嵌入程度；
- $T$ ：歷史深度；
- $Q$ ：規則改變幅度。

這是一個重要的新預測：

> 歷史越深、公共認知越廣、制度嵌入越強的身份，其正統性規則可能越具有慣性。

---

# 十四、「空氣」的雙面性

Recursive Social Estimation 不一定是壞事。

它可以產生：

$$
\text{coordination}.
$$

大家知道如何稱呼、排序、繼承與互動，

可以降低：

$$
C_{\mathrm{coordination}}.
$$

但它也可能產生：

$$
\text{pluralistic ignorance}.
$$

例如每個人私下都不相信某條規則，

但每個人又認為：

> 其他人都很相信。

於是：

$$
P_i(\text{rule valid})<0.5
$$

對多數人都成立，

卻仍然：

$$
P_i(
P_j(\text{rule valid})>0.5
)
>0.5.
$$

最後所有人仍然服從。

因此：

$$
\boxed{
\text{collective legitimacy}
\neq
\text{sum of private beliefs}.
}
$$

這是「看空氣」模型最重要的地方之一。

---

# 十五、敘事正統場的最小動態式

本文暫提出：

$$
\mathcal N_H(t+1)
=
(1-\delta)\mathcal N_H(t)
+
\alpha B_D
+
\beta H
+
\gamma R
+
\eta P
+
\mu I
+
\nu M
+
\xi A
+
\omega C^*
-
X_t,
$$

其中：

$$
C^*
=
C(
\mathbf l^*
)
$$

是共同信念固定點產生的社會承認。

$X_t$ 則表示：

- 戰敗；
- 除名；
- 醜聞；
- 斷嗣；
- 國家撤銷；
- 家譜失信；
- 歷史敘事崩解；

等負向衝擊。

這不是最終統計模型，

而是一個概念骨架。

---

# 十六、正式命題一：分散式正統性命題

正統性不是單一個體屬性：

$$
\boxed{
\mathcal N_H
\neq
f(H\text{ alone}).
}
$$

而是相關行動者彼此預期、制度承認與歷史訊號共同形成的分散式狀態。

---

# 十七、正式命題二：高階信念命題

行動者對某家正統性的判斷部分依賴其對他人判斷的估計：

$$
\boxed{
l_i(H)
=
f(
x_i,
E_i[l_j(H)]
).
}
$$

在高協調需求制度中，

高階信念的影響可能顯著提高。

---

# 十八、正式命題三：敘事慣性命題

若：

$$
\mathcal N_H(t)
$$

已被大量制度、儀式、關係與共同信念支撐，

單一維度中斷：

$$
\Delta B_G<0
$$

未必造成：

$$
\Delta\mathcal N_H\ll0.
$$

因此：

$$
\boxed{
\text{narrative systems can absorb local discontinuities}.
}
$$

---

# 十九、正式命題四：公共尺度更新成本命題

正統性相關行動者越多、歷史越深、制度嵌入越強：

$$
N\uparrow,\quad
T\uparrow,\quad
I\uparrow
$$

則：

$$
\boxed{
C_U\uparrow.
}
$$

因此極高公共可見度身份可能比私人家系更難快速改變規則。

---

# 二十、正式命題五：共同承認非加總命題

不能簡單寫：

$$
\mathcal N_H
=
\sum_i l_i.
$$

更合理的是：

$$
\boxed{
\mathcal N_H
=
F(
\mathbf l,
\mathbf W,
K^1,K^2,\ldots
).
}
$$

其中：

$$
K^m
$$

代表不同階層的共同知識／共同信念。

---

# 二十一、正式命題六：敘事中心性命題

主家、皇室或某些歷史 House 的地位，

可以部分由其在敘事—制度網絡中的中心性解釋：

$$
\boxed{
\mathcal N_H
\propto
C_{\mathrm{network}}
}
$$

而不必訴諸：

$$
\text{genetic purity}.
$$

---

# 二十二、可反駁預測

如果本模型有解釋力，應至少看到以下現象。

第一，對某家系的社會評價會受到「他人如何評價」的資訊影響，而不只受到家譜本身影響。

第二，國家、主要家族、宗教或媒體的正式承認，可以在沒有改變生物親緣的情況下改變正統性。

第三，具有較高歷史深度與公共知名度的 House，其規則更新會比私人家庭更慢。

第四，單次養子或婚姻不必造成家系身份崩潰，只要其他連續性維度仍高度維持。

第五，當社會共同承認迅速崩解時，即使家名、財產甚至後裔仍然存在，原有家格也可能快速失效。

第六，某些規範可能出現 pluralistic ignorance：私人支持度低，但因高階信念而繼續被公共遵守。

---

# 二十三、反論一：這只是象徵資本換名字

的確，本模型與象徵資本、聲望、社會資本等理論有交集。

差異在於：

本文特別關心：

$$
\boxed{
\text{跨世代身份的連續性}
+
\text{高階信念}
+
\text{系譜／House 結構}
}
$$

如何共同生成正統性。

因此後續研究必須明確比較 Bourdieu、House Society、common knowledge、institutional equilibrium 等既有理論，避免只重新命名舊概念。

---

# 二十四、反論二：「看空氣」太日本文化論

成立。

所以正式模型不使用：

$$
\text{Japanese essence}.
$$

「看空氣」只作為日常語言入口。

真正的理論變量是：

$$
\boxed{
\text{Recursive Social Estimation}.
}
$$

它應該能跨文化檢驗。

---

# 二十五、反論三：共同知識要求太強

現實社會很少真的具有無限階：

$$
K^\infty(E).
$$

因此實證模型不應要求完美 common knowledge。

可以使用有限階：

$$
K^1,
K^2,
K^3
$$

或：

$$
\text{approximate common belief}.
$$

真正問題是：

> 多深的高階信念已足以維持制度穩定？

這是可以實驗化的問題。

---

# 二十六、反論四：歷史故事可以被偽造

正確。

而且這反而支持：

$$
B_D
\neq
B_G.
$$

真正需要研究的是：

$$
\text{claim}
\rightarrow
\text{verification}
\rightarrow
\text{recognition}
\rightarrow
\text{institutionalization}.
$$

一個虛構系譜若完全不被承認：

$$
\mathcal N_H\approx0.
$$

如果被長期制度化，

則可能取得真實社會效力。

因此：

$$
\boxed{
\text{historical truth}
\neq
\text{social efficacy}.
}
$$

兩者必須分開測量。

---

# 二十七、從日本推廣出去

一旦抽象化：

$$
\mathcal N_H
$$

就不只適用於日本 House。

它也可能適用：

### 王朝

$$
\mathcal N_{\mathrm{Dynasty}}.
$$

### 國家

$$
\mathcal N_{\mathrm{State}}.
$$

### 宗教制度

$$
\mathcal N_{\mathrm{ReligiousOffice}}.
$$

### 公司／品牌

$$
\mathcal N_{\mathrm{Brand}}.
$$

### 大學與學派

$$
\mathcal N_{\mathrm{Institution}}.
$$

### AI 身份

如果未來 AI 可以換模型、換硬體、換記憶載體，

則也會出現：

$$
\boxed{
\text{What makes AI}_t
\text{ the same entity as AI}_{t+1}?
}
$$

此時：

$$
\text{model weights}
$$

可能就像：

$$
\text{blood},
$$

只是連續性向量中的一個維度。

這與本系列的「連續性對象問題」自然接軌。

---

# 二十八、系列的上層統一

現在四篇可以串成：

$$
\text{Space}
\rightarrow
\text{Node}
\rightarrow
\text{House}
\rightarrow
\text{Legitimacy Field}.
$$

第一篇問：

$$
\text{政治節點為何形成？}
$$

第二篇問：

$$
\text{政治節點為何跨代存活？}
$$

第三篇問：

$$
\text{血與家到底保存什麼？}
$$

第四篇回答：

$$
\boxed{
\text{它們可能共同維持一個被分散式社會承認的敘事—正統性狀態。}
}
$$

因此日本悖論已不只是日本史問題。

它逐漸變成：

> **一個社會如何讓抽象身份跨越人、血、財產與制度更替而持續存在？**

---

# 二十九、下一篇接口：連續性對象的一般理論

下一篇應該脫離日本個案，正式處理：

$$
\boxed{
\text{Continuity Object Problem}
}
$$

即：

> 當我們聲稱「同一個存在持續存在」時，到底是哪一組狀態不能同時被替換？

可以定義：

$$
\mathbf C
=
(c_1,c_2,\ldots,c_n)
$$

以及身份判定：

$$
I(X_t,X_{t+1})
=
F(
\mathbf C,
\mathcal N,
R
).
$$

這將把 House 問題與：

- 忒修斯之船；
- 公司人格；
- 國家繼承；
- 王朝；
- 宗教職位；
- AI 模型替換；

全部接入同一套形式。

因此第五篇建議為：

# 《日本悖論 V：究竟什麼東西必須延續？——連續性對象、身份向量與制度人格》

---

# 三十、結論

本篇的核心不是：

> 日本人很會看空氣。

而是：

$$
\boxed{
\text{Legitimacy is socially distributed and recursively estimated}.
}
$$

血統、家名、財產、爵位、婚姻與歷史，

可以全部是真實而重要的變量，

但它們之所以能產生政治效果，

部分取決於：

$$
\boxed{
\text{其他人也預期其他人會承認它們}.
}
$$

因此：

$$
\text{Blood}
$$

與：

$$
\text{House}
$$

都可能只是：

$$
\boxed{
\text{Narrative–Legitimacy Field}
}
$$

的載體與輸入接口。

當這個場足夠穩定時，

局部血緣中斷、養子、婚姻、名稱改變甚至政權轉型，

都可以被吸收。

當共同承認崩潰時，

即使血、名字與財產形式上都還存在，

「那個家」也可能已經不再具有原本的社會存在方式。

所以真正的上層問題不再是：

> 血重要？家重要？

而是：

$$
\boxed{
\text{什麼故事被誰共同承認，並且大家是否相信其他人也會繼續承認？}
}
$$

這就是本文所稱：

$$
\boxed{
\mathcal N_H
=
\text{敘事正統場}.
}
$$

---

## 初版參考文獻

1. Claude Lévi-Strauss, société à maison / House Society 相關著作。
2. “Bringing Kinship Back into the House,” *Cambridge Archaeological Journal*, 2026.
3. “Kinship Trouble: What, When, Where, Why, and How—and So What?”, *Cambridge Archaeological Journal*, 2026.
4. Steven J. Bosworth, “The Importance of Higher-Order Beliefs to Successful Coordination,” *Experimental Economics*, 2025.
5. Robin P. Cubitt & Robert Sugden, “Common Knowledge, Salience and Convention: A Reconstruction of David Lewis' Game Theory,” *Economics & Philosophy*, 2003.
6. Cyril Hédoin, “A Framework for Community-Based Salience: Common Knowledge, Common Understanding and Community Membership,” *Economics & Philosophy*, 2014.
7. Avner Greif, *Institutions and the Path to the Modern Economy*, especially the treatment of institutionalized beliefs and self-enforcing institutions.
8. Youichi Ito, “Climate of Opinion, Kuuki, and Democracy,” *Communication Yearbook*, Vol. 26.
9. Yamamoto Shichihei, 『「空気」の研究』, 1977.
10. Ray A. Moore, “Adoption and Samurai Mobility in Tokugawa Japan,” *The Journal of Asian Studies*.

---

## 版本註記

v0.1 完成的是理論骨架，不宣稱已證明日本家系真的依照單一可測量的「敘事正統場」運作。

後續 v0.2 應優先完成：

1. 將 $\mathcal N_H$ 與 Bourdieu 象徵資本、聲望模型、institutional equilibrium 明確比較；
2. 將 common knowledge 改成有限階 higher-order belief 實證模型；
3. 搜集主家／分家、養子與婚姻事件前後的社會地位變化；
4. 區分真實歷史系譜與被相信的系譜；
5. 建立「正統性更新成本」 $C_U$ 的可測量指標；
6. 測試日本之外的歐洲王朝、宗教職位與公司品牌；
7. 進一步連接 AI 身份連續性與模型／載體替換問題。
