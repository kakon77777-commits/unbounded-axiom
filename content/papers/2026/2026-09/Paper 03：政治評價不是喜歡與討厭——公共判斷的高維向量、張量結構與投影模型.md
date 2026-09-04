# 政治符號學 2.0——共享政治世界、關係耦合與動態契約
## Paper 03：政治評價不是喜歡與討厭
### 公共判斷的高維向量、張量結構與投影模型

**Political Semiotics 2.0 — Shared Political Worlds, Relational Coupling, and Dynamic Contract**  
**Paper 03: Political Evaluation Is Not Like or Dislike — A High-Dimensional Vector, Tensor, and Projection Model of Public Judgment**

**作者：Neo.K × Aletheia**  
**機構：EveMissLab／一言諾科技有限公司**  
**版本：v0.1**  
**日期：2026-08-30**  
**性質：內部研究論文／系列政治評價基礎篇**

---

## 摘要

政治討論最常使用的語言之一，是「我喜歡這個政治人物」「我討厭這個政府」「這項政策很好」「這個政黨很爛」。這些語句具有高度溝通效率，卻同時造成嚴重的資訊壓縮。兩個人都說「我支持某政治人物」，其底層理由可能完全不同：一人重視經濟成長，一人重視國家安全，一人重視社會福利，一人重視文化認同，一人則只是因為厭惡對手。若研究者直接把「支持／反對」「喜歡／討厭」視為政治判斷的原子，就會把多維政治評價錯誤壓成單一標量。

本文提出「多維政治評價模型」（Multidimensional Political Evaluation Model, MPEM），將政治評價拆分為利益、損害、權利、自由、安全、尊嚴、身份、信任、公平、未來機會、外部性與可逆性等維度。對主體 $S_i$ 、政治對象 $O_j$ 、時間 $t$，定義政治評價向量：

$$
\mathbf{E}_{ij}(t)
=
\left(
B,
H,
R,
F,
S,
D,
I,
T,
J,
U,
X,
V
\right)_{ijt}.
$$

其中每個分量本身又可依尺度、群體、政策領域與時間展開為張量。

本文主張，「喜歡」「討厭」「支持」「反對」只是高維政治評價經過主體價值權重、情感狀態、資訊可見性與語境壓縮後形成的低維投影：

$$
L_{ij}
=
\Pi_{\text{affect}}
\left(
\mathbf{E}_{ij},
\mathbf{w}_i,
\mathcal{I}_i,
\mathcal{C}_i
\right).
$$

因此：

$$
\boxed{
\text{Like/Dislike}
\neq
\text{Political Evaluation Itself}
}
$$

本文同時區分「價值偏袒」與「認知錯誤」。政治共享世界中的主體本身就是被作用者，因此其價值權重並非單純噪聲；但價值權重不能替代事實與因果驗證。政治評價需要分離事實判斷、因果判斷、利益位置、價值權重與規範結論。

本文最後把高維政治評價接回政治符號學 2.0：政治語句本身是壓縮符號，而政治評價的真正分析對象，是主體、對象、關係、尺度與時間共同決定的多維狀態。這為下一篇「權力越大為何責任越大」建立基礎：只有先知道某政治人物究竟在哪些維度、對哪些主體造成何種影響，責任才可能被形式化，而不只是道德口號。

**關鍵詞：** 政治評價、喜歡與討厭、支持、反對、多維向量、張量、政治符號學、價值權重、公共判斷、政治責任

---

# 第一部　問題：政治評價為什麼總被壓縮成情感標籤？

## 1. 「我喜歡他」其實說得很少

日常政治語言會說：

> 我喜歡這個總統。

> 我討厭這個政黨。

> 我支持這項政策。

> 我反對這個政府。

這些句子看起來很清楚，但對分析者而言，其實資訊極少。

因為「喜歡」可能代表：

- 覺得他讓經濟變好；
- 覺得他維持國家安全；
- 覺得他符合自己的價值觀；
- 覺得他代表自己的身份；
- 覺得他比另一個候選人好；
- 覺得他至少沒有傷害自己的核心利益；
- 單純對其人格風格有好感；
- 對其政治對手有更強烈厭惡。

所以：

$$
\text{Like}
$$

並不是政治評價的最小單位。

---

## 2. 同一標籤可以包住完全不同的結構

令兩個主體 $S_a$ 與 $S_b$ 都表示：

$$
L_a(O)=L_b(O)=+1.
$$

若 $+1$ 表示「支持」。

這並不推出：

$$
\mathbf{E}_{aO}
=
\mathbf{E}_{bO}.
$$

例如：

$$
\mathbf{E}_{aO}
=
(+Economy,+Security,-Freedom,+Identity),
$$

而：

$$
\mathbf{E}_{bO}
=
(-Economy,+Welfare,+Freedom,+Fairness).
$$

兩人最後都支持同一政治人物，但底層政治世界不同。

因此本文提出：

$$
\boxed{
\text{Symbolic Agreement}
\not\Rightarrow
\text{Evaluative Identity}.
}
$$

---

# 第二部　政治評價的十二維基本向量

## 3. 多維政治評價向量

對主體 $S_i$ 與政治對象 $O_j$，定義：

$$
\mathbf{E}_{ij}(t)
=
\left(
B_{ij},
H_{ij},
R_{ij},
F_{ij},
S_{ij},
D_{ij},
I_{ij},
T_{ij},
J_{ij},
U_{ij},
X_{ij},
V_{ij}
\right)_t.
$$

其中：

- $B$：Benefit，利益與正向效益；
- $H$：Harm，損害與負向成本；
- $R$：Rights，權利影響；
- $F$：Freedom，自由與選擇空間；
- $S$：Security，安全；
- $D$：Dignity，尊嚴；
- $I$：Identity，身份與認同；
- $T$：Trust，信任；
- $J$：Justice/Fairness，公平與正義；
- $U$：Future Opportunity，未來機會；
- $X$：Externality，對第三方與外部系統的影響；
- $V$：Reversibility，政策可逆性與修復能力。

這十二維不是封閉集合，而是最低可擴張骨架。

---

## 4. 利益與損害不是同一條軸的正負值

直覺上似乎可以寫：

$$
H=-B.
$$

但現實未必如此。

一項政策可能同時帶來：

$$
B>0
$$

以及：

$$
H>0.
$$

例如大型建設可以創造就業，同時造成環境損害；國防擴張可以提高外部安全，同時增加財政負擔；科技監管可以降低某些風險，同時壓縮創新。

因此：

$$
\boxed{
Benefit
\neq
-Harm.
}
$$

它們應分開建模。

---

## 5. 權利與自由也不是完全同一回事

一個制度可以在法律上承認權利：

$$
R_i>0,
$$

但若主體實際無法使用：

$$
F_i\approx0.
$$

例如形式上具有申訴權，卻因成本、資訊或風險而幾乎無法行使。

因此：

$$
\text{Nominal Right}
\neq
\text{Effective Freedom}.
$$

這與政治符號學 2.0 的選擇底空間區分一致。

---

# 第三部　從向量到張量

## 6. 一個政治評價必須標記「對誰」

若某人說：

> 這個政策對人民很好。

「人民」不能被當成單一均質點。

令群體索引為 $g$，則：

$$
\mathbf{E}_{ijg}(t).
$$

可能存在：

$$
B_{ijg_1}>0
$$

而：

$$
B_{ijg_2}<0.
$$

例如同一住宅政策可能：

- 對既有屋主有利；
- 對首次購屋者不利；
- 對租屋者產生另一種影響；
- 對未來世代又是不同結果。

因此：

$$
\boxed{
\text{Average Benefit}
\neq
\text{Universal Benefit}.
}
$$

---

## 7. 一個政治評價也必須標記尺度

令尺度為：

$$
s
\in
\{micro,meso,macro,civilizational\}.
$$

則：

$$
\mathbf{E}_{ijgs}(t)
$$

表示同一政治對象在不同尺度下的評價。

例如：

微觀：

$$
\Delta Income_i<0.
$$

宏觀：

$$
\Delta GDP>0.
$$

這兩者可以同時成立。

因此：

$$
\boxed{
\text{Micro Loss}
\not\Rightarrow
\text{Macro Failure}
}
$$

同時：

$$
\boxed{
\text{Macro Gain}
\not\Rightarrow
\text{No Micro Victim}.
}
$$

---

## 8. 再加入政策領域與時間

令政策領域為 $d$，時間為 $t$，則完整評價可寫成：

$$
\mathcal{E}_{ijgsdt}.
$$

這是一個高階政治評價張量。

它允許我們表達：

> 某政策對某群體在短期經濟上有利，但在長期住房、自由與代際公平上不利。

而不是強迫回答：

> 所以到底好還是不好？

---

# 第四部　價值權重：偏袒不是單純噪聲

## 9. 主體有不同價值權重

對主體 $S_i$，定義價值權重向量：

$$
\mathbf{w}_i
=
\left(
w_B,
w_H,
w_R,
w_F,
w_S,
w_D,
w_I,
w_T,
w_J,
w_U,
w_X,
w_V
\right)_i.
$$

則同一政治評價向量：

$$
\mathbf{E}
$$

對不同主體可能產生不同總體判斷：

$$
U_i
=
\mathbf{w}_i^{T}
\mathbf{E}.
$$

若：

$$
\mathbf{w}_i
\neq
\mathbf{w}_j,
$$

則即使：

$$
\mathbf{E}_i
=
\mathbf{E}_j,
$$

仍可能有：

$$
U_i\neq U_j.
$$

這不是必然表示其中一方「不客觀」。

---

## 10. 價值權重與認知錯誤必須分離

如果某人更重視安全：

$$
w_S\gg w_F,
$$

而另一人更重視自由：

$$
w_F\gg w_S,
$$

兩人可能在事實完全一致的前提下得到不同結論。

這是價值差異。

但如果某人錯誤認為：

$$
\Delta Security>0
$$

而真實資料顯示：

$$
\Delta Security<0,
$$

那是認知錯誤。

因此政治分析必須區分：

$$
\boxed{
\text{Value Disagreement}
\neq
\text{Factual Disagreement}.
}
$$

---

# 第五部　政治情感作為低維投影

## 11. 情感投影函數

令主體的政治評價為：

$$
\mathbf{E}_{ij}.
$$

令資訊狀態為：

$$
\mathcal{I}_i,
$$

語境為：

$$
\mathcal{C}_i,
$$

情感狀態為：

$$
\mathcal{A}_i.
$$

則最終語言標籤可以表示為：

$$
L_{ij}
=
\Pi_{\text{affect}}
\left(
\mathbf{E}_{ij},
\mathbf{w}_i,
\mathcal{I}_i,
\mathcal{C}_i,
\mathcal{A}_i
\right).
$$

例如：

$$
L_{ij}\in
\{
Like,
Dislike,
Support,
Oppose,
Neutral
\}.
$$

所以情感標籤是結果，不是原始資料。

---

## 12. 壓縮造成政治誤讀

若兩個高維狀態：

$$
\mathbf{E}_1
\neq
\mathbf{E}_2
$$

但：

$$
\Pi_{\text{affect}}(\mathbf{E}_1)
=
\Pi_{\text{affect}}(\mathbf{E}_2),
$$

則發生投影碰撞。

本文稱之為：

$$
\boxed{
\text{Political Projection Collision}.
}
$$

也就是不同政治世界被壓成同一語句。

---

# 第六部　支持與反對不應視為二元真值

## 13. 二元支持模型的問題

傳統民調常問：

$$
Support\in\{0,1\}.
$$

但很多真實政治態度是：

- 支持政策 A，但反對政策 B；
- 支持政府方向，但不信任執行；
- 支持某領袖處理外交，但反對內政；
- 反對政黨，但仍支持其中某項改革。

因此：

$$
Support(O)
$$

應展開為：

$$
\mathbf{S}_i(O)
=
(s_1,s_2,\ldots,s_n).
$$

---

## 14. 條件性支持

更精確地：

$$
Support_i(O|C_k).
$$

例如：

$$
Support_i(O|\text{Security})
>0
$$

但：

$$
Support_i(O|\text{Economy})
<0.
$$

所以「支持率」是一個高度聚合後的統計投影。

---

# 第七部　政治評價中的反事實

## 15. 評價不能只看結果

一個政治人物做出決策 $a$，最後得到結果：

$$
Y_a.
$$

若只看結果，容易產生事後偏誤。

政治評價至少要比較：

$$
Y_a
$$

與：

$$
Y_{alt}.
$$

但 $Y_{alt}$ 不能是任何幻想世界，而應是當時真正可達的替代方案。

令可達政策集合為：

$$
\Omega_t^{reachable}.
$$

則評價需要考慮：

$$
\Delta Y
=
Y_a
-
\mathbb{E}
\left[
Y_{alt}
\mid
alt\in\Omega_t^{reachable}
\right].
$$

Paper 09 將專門處理這一問題，但 Paper 03 先建立接口。

---

# 第八部　政治評價的五層分解

## 16. 第一層：事實層

回答：

> 發生了什麼？

記為：

$$
Factual.
$$

---

## 17. 第二層：因果層

回答：

> 是誰造成的？

記為：

$$
Causal.
$$

---

## 18. 第三層：分配層

回答：

> 誰得到，誰失去？

記為：

$$
Distributional.
$$

---

## 19. 第四層：價值層

回答：

> 哪些結果更重要？

記為：

$$
NormativeWeight.
$$

---

## 20. 第五層：總體判斷層

最後才得到：

$$
OverallEvaluation.
$$

因此：

$$
\boxed{
\text{Overall Political Judgment}
=
F
\left(
\text{Fact},
\text{Cause},
\text{Distribution},
\text{Value}
\right).
}
$$

---

# 第九部　政治符號學 2.0 接口

## 21. 評價也是一種政治符號

「好總統」「壞政府」「愛國」「賣國」「左派」「右派」都可能是高壓縮評價符號。

這些符號不只描述，也會影響主體選擇底空間。

例如：

$$
\Pi^{label}:
\mathfrak{B}_i
\rightarrow
\mathfrak{B}_i'.
$$

某人被貼上「不愛國」標籤後，其可發言空間、社會信任與政治參與可能改變。

因此評價語言本身也具有政治算子性。

---

## 22. 評價必須回到主體—對象—關係

令：

$$
\mathcal{R}_{ij}
$$

表示主體 $S_i$ 與政治對象 $O_j$ 的關係。

則：

$$
\mathbf{E}_{ij}
=
F
\left(
S_i,
O_j,
\mathcal{R}_{ij},
t,
s,
g
\right).
$$

政治評價因此不是漂浮在空中的道德分數，而是關係性狀態。

---

# 第十部　十項核心命題

## 23. MPEM-A1：評價—情感非同一命題

$$
\boxed{
\text{Political Evaluation}
\neq
\text{Like/Dislike}.
}
$$

---

## 24. MPEM-A2：高維評價命題

$$
\boxed{
\mathbf{E}_{ij}
\in
\mathbb{R}^{n}.
}
$$

政治評價不能安全地被假設為單一標量。

---

## 25. MPEM-A3：利益—損害非同軸命題

$$
\boxed{
Benefit
\neq
-Harm.
}
$$

一項政策可以同時創造收益與損害。

---

## 26. MPEM-A4：權利—自由非同一命題

$$
\boxed{
NominalRight
\neq
EffectiveFreedom.
}
$$

---

## 27. MPEM-A5：價值—事實分離命題

$$
\boxed{
ValueDisagreement
\neq
FactualDisagreement.
}
$$

---

## 28. MPEM-A6：平均—全體非同一命題

$$
\boxed{
AverageBenefit
\neq
UniversalBenefit.
}
$$

---

## 29. MPEM-A7：尺度依賴命題

$$
\boxed{
Evaluation
=
Evaluation(s).
}
$$

微觀、中觀、宏觀與文明尺度可能同時產生不同但相容的判斷。

---

## 30. MPEM-A8：投影碰撞命題

若：

$$
\mathbf{E}_1\neq\mathbf{E}_2
$$

但：

$$
\Pi(\mathbf{E}_1)=\Pi(\mathbf{E}_2),
$$

則同一政治標籤不能推出同一底層評價。

---

## 31. MPEM-A9：支持條件化命題

$$
\boxed{
Support(O)
=
\{Support(O|C_k)\}.
}
$$

支持應被拆為條件性結構。

---

## 32. MPEM-A10：評價關係性命題

$$
\boxed{
\mathbf{E}_{ij}
=
F(S_i,O_j,\mathcal{R}_{ij},t,s,g).
}
$$

政治評價取決於主體、對象、關係、時間、尺度與群體位置。

---

# 第十一部　反例與限制

## 33. 高維模型不保證客觀

把政治評價變成向量或張量，不會自動消除偏見。

如果輸入本身錯誤：

$$
\mathbf{E}_{wrong},
$$

那高維形式只是把錯誤形式化。

因此形式化必須結合資料驗證。

---

## 34. 維度越多不一定越好

若無限制增加維度：

$$
n\rightarrow\infty,
$$

模型可能失去可解釋性與實用性。

因此維度選擇應依任務決定。

---

## 35. 情感不是需要消滅的東西

本文並不主張：

$$
Emotion=Error.
$$

情感可能是主體對損害、尊嚴、身份與風險的快速整合反應。

問題在於：

> 不能把情感標籤當成完整分析。

---

# 第十二部　通往 Paper 04：權力越大為何責任越大？

## 36. 有了多維影響，才能談責任

Paper 02 已經建立：

$$
\text{Power to Alter}
\Rightarrow
\text{Standing}.
$$

Paper 03 進一步告訴我們：

$$
\text{Alteration}
$$

不是一個單一量，而是：

$$
\Delta\mathbf{E}_{ij}.
$$

因此如果某政治人物能同時改變：

- 經濟；
- 權利；
- 安全；
- 自由；
- 尊嚴；
- 未來；
- 第三方外部性；

其政治責任就不能只以「職稱」來描述。

下一篇將把責任形式化為：

$$
Responsibility
=
F
\left(
\text{Control},
\text{Impact},
\text{Knowledge},
\text{Alternatives},
\text{Reversibility}
\right).
$$

---

# 結論

政治評價不是「喜歡」與「討厭」本身。

它更接近：

$$
\boxed{
\mathcal{E}
=
\text{Multi-Dimensional}
+
\text{Relational}
+
\text{Scale-Dependent}
+
\text{Time-Dependent}
+
\text{Value-Weighted}.
}
$$

「喜歡」「討厭」「支持」「反對」只是這個高維狀態被壓縮後的低維介面。

因此：

$$
\boxed{
\text{Political Labels}
=
\text{Compressed Interfaces},
\quad
\text{not Complete Evaluations}.
}
$$

政治分析若停在標籤，就很容易把不同主體、不同尺度、不同利益與不同價值權重誤認為同一個政治立場。

本文最終主張：

> 真正高解析度的政治評價，必須先問「對誰、在哪一維、什麼時間尺度、造成什麼影響」，最後才問「所以你喜歡還是討厭」。

下一篇將正式處理：當政治人物、政府與制度具有不同程度的控制力、資訊優勢與作用半徑時，為什麼政治責任也應呈現光譜，而不能只用職稱或結果論粗略判定。

---

# 內部理論接口

1. EveMissLab，《政治知識的多源性——為什麼政治學專業不等於政治全知》，本系列 Paper 01，2026。
2. EveMissLab，《公民批評的政治正當性——從專業資格到受影響者 Standing》，本系列 Paper 02，2026。
3. EveMissLab，《政治符號學 2.0：主體、選擇底空間與不可代決政治的統一公理框架》，2026。
4. EveMissLab，《政治算子論》，政治符號學 2.0 基礎論文 III，2026。
5. EveMissLab，《政治科學的診斷革命：四光譜理論與治理科學的範式重構》，2025。
6. EveMissLab，《統治者—人民同向性原理》，2026。

# 經典理論接口

- Amartya Sen, works on capabilities, freedom, and social choice.
- John Rawls, *A Theory of Justice*.
- Isaiah Berlin, “Two Concepts of Liberty.”
- Philip Pettit, works on freedom as non-domination.
- Daniel Kahneman, works on judgment and decision-making.
- Kenneth Arrow, works on social choice and preference aggregation.

---

**Canonical source note:** 本文件以 UTF-8 Markdown 為正式原始稿。數學原始碼只使用 ` $...$ ` 與 `$$...$$` 作為 canonical delimiters；不以渲染後公式替代原始碼。
