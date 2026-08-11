# 日本悖論 III：血統重要，還是家系重要？
## 雙重正統性、系譜權重與連續性對象問題
### Japan Paradox III: Bloodline or House? Dual Legitimacy and the Object of Continuity

**系列**：日本悖論研究系列  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-07  
**性質**：探索性模型論文／待進一步歷史檢驗  
**前置論文**：  
1. 《日本悖論 I：小幾何空間何以形成高政治碎片化？》  
2. 《日本悖論 II：個體會死，家為何不死？》

**核心新增變量**：

$$
B_G=\text{Genetic Relatedness}
$$

$$
B_D=\text{Genealogical Legitimacy}
$$

$$
H=\text{House Continuity}
$$

$$
\mathcal L=\text{Legitimacy Function}
$$

---

## 摘要

日本歷史呈現一個表面矛盾：一方面，武家、商家與其他家戶制度可以使用養子、婿養子與旁系繼承，以避免家系因自然斷嗣而消滅；另一方面，日本歷史與現代皇室制度又持續出現高度重視血統、男系、祖先與系譜正統性的語言。若「血統」與「家系」是互斥價值，兩者似乎形成悖論。

本文提出：這不是二選一問題，而是將至少三種不同的連續性誤認為同一變量。第一，實際遺傳親緣 $B_G$ ；第二，被制度與社會承認的系譜路徑 $B_D$ ；第三，家作為跨世代政治—社會節點的連續性 $H$ 。三者可以高度相關，但並不等價。

養子制度證明 $H$ 可以在嚴格生物父子關係中斷後持續；皇室男系規則則證明某些制度可能對特定 $B_D$ 路徑賦予極高權重。2026 年日本國會通過的皇室制度修法尤其具有模型意義：制度允許以收養補充皇族成員，但收養候選人被限定於舊皇族中的父系男系男性後裔。這是一個「以家系修復工具維持受系譜條件約束的制度」的現代案例。

本文因此提出「雙重正統性模型」：血緣、系譜、家名、財產、家格、婚姻、職位與社會承認，並非彼此競爭的唯一最高價值，而是依不同制度被賦予不同權重。這進一步導向更高階問題：一個社會聲稱某個家、王朝或皇室「延續」數百年時，真正要求持續的是什麼？本文將此稱為「連續性對象問題」（Continuity Object Problem），並為下一篇「敘事正統場」建立接口。

**關鍵詞**：日本悖論、血統、家系、家制度、養子、婿養子、系譜、皇室、正統性、House Society、連續性對象

---

# 一、表面悖論：如果血重要，為什麼可以收養？

日本悖論 II 已建立：

$$
\text{biological line break}
\not\Rightarrow
\text{house extinction}.
$$

如果自然繼承失敗，可以透過養子、婿養子、旁系等方式修復：

$$
H_t
\rightarrow
H_{t+1}.
$$

德川武士資料顯示，養子制度的重要功能之一確實是保存武士家系與大名政治體系；而中上層武士的收養通常發生在親族或大致相同社會地位的家庭之間。

因此：

$$
\boxed{
\text{House continuity can survive individual biological discontinuity.}
}
$$

但另一方面，某些日本制度又極度強調：

- 祖先；
- 血筋；
- 男系；
- 嫡流；
- 本家；
- 分家；
- 皇統。

於是表面問題出現：

$$
\boxed{
\text{Blood}
\quad\text{vs}\quad
\text{House}.
}
$$

如果血最重要，養子制度為何如此成熟？

如果家最重要，為什麼某些系譜路徑又不能被任意替代？

本文主張：問題本身把不同種類的「血統」與「連續性」混在了一起。

---

# 二、第一刀：遺傳親緣不等於系譜合法性

本文首先區分：

$$
B_G
=
\text{Genetic Relatedness}
$$

與：

$$
B_D
=
\text{Genealogical Legitimacy}.
$$

 $B_G$ 是生物學意義上的實際遺傳親緣。

 $B_D$ 則是：

> 某個人是否沿著制度認可的系譜路徑與特定祖先、家系或皇統相連。

兩者不是同一件事。

例如，在經過大量世代之後，一位遠房男系後裔與共同祖先之間的實際遺傳比例可能很低；但制度仍然可能認定：

$$
B_D=1.
$$

相反，一名與現任家主具有極高直接生物親緣的人，如果其系譜路徑不符合特定制度規則，可能：

$$
B_G\uparrow
$$

但：

$$
B_D=0.
$$

所以：

$$
\boxed{
B_G\neq B_D.
}
$$

這一點對皇室尤其重要。

---

# 三、所謂「血統」，很多時候其實是路徑而不是濃度

一般語言會說：

> 某人「有多少」某家族的血。

但正式模型不應把這直接等同 DNA 百分比。

更適合的概念是：

$$
W_G
=
\text{Symbolic Genealogical Weight}.
$$

它代表：

> 某個人的系譜位置，在一套制度與社會認知中被賦予多少象徵權重。

因此：

$$
W_G
=
f(
\text{descent path},
\text{branch status},
\text{marriage},
\text{recognition},
\text{historical convention}
).
$$

主家與分家的差異，也未必是：

$$
\text{genetic purity}_{main}
>
\text{genetic purity}_{branch}.
$$

更可能是：

$$
\boxed{
C_{\mathrm{narrative}}(H_{\mathrm{main}})
>
C_{\mathrm{narrative}}(H_{\mathrm{branch}})
}
$$

亦即主家在家名、祖產、祭祀、官職、歷史故事與外部承認網絡中具有更高中心性。

因此「血比較濃」在許多情況下更適合重寫成：

$$
\boxed{
\text{系譜位置更接近被承認的故事中心}.
}
$$

---

# 四、第二刀：家本身也是一個獨立連續性對象

日本悖論 II 已把家寫成：

$$
H_t
=
(
N,
P,
O,
R,
V,
M,
A,
S
)_t.
$$

其中包含：

- 家名；
- 財產；
- 家職；
- 親族與姻親；
- 歷史敘事；
- 組織能力；
- 外部承認；
- 繼承制度。

所以：

$$
H
$$

並不是：

$$
B_G.
$$

也不完全等於：

$$
B_D.
$$

可能存在：

$$
B_G\downarrow
$$

但：

$$
H\approx1.
$$

養子就是最清楚的例子。

而在婿養子制度中，甚至可以同時：

$$
H\uparrow
$$

與：

$$
B_G^{next\ generation}>0.
$$

所以「家」可以容納多種血緣修復方式。

---

# 五、養子不是證明日本不重血

德川武士的收養並非完全隨機。

相關研究顯示，中上層武士的收養一般發生在親族或社會地位相近的家庭之間；當存在地位差異時，養子甚至往往來自地位較高的一方。

這意味：

$$
A_{\mathrm{candidate}}
\notin
\text{anyone}.
$$

而更接近：

$$
A_{\mathrm{candidate}}
\in
\mathcal E_H,
$$

其中 $\mathcal E_H$ 是被某個家視為可合法吸收的候選集合。

此集合可能受：

$$
\text{kinship}
+
\text{status}
+
\text{marriage}
+
\text{political relation}
+
\text{house compatibility}
$$

約束。

因此養子制度並不是：

> 血統完全不重要。

反而可能是：

> 在保家優先的前提下，仍盡可能從符合親族、家格與系譜條件的候選人中進行修復。

所以：

$$
\boxed{
\text{Adoption}
\neq
\text{rejection of genealogy}.
}
$$

---

# 六、皇室：極端提高系譜權重的制度

日本現行皇位繼承制度將皇位資格限定於皇統中的男系男性後裔。

因此皇室的正統性函數與普通商家或武家顯然不同。

可以粗略寫成：

$$
\mathcal L_{\mathrm{Imperial}}
=
w_D B_D
+
w_H H
+
w_N N
+
w_C C
+\cdots
$$

而其中：

$$
w_D
\gg
0.
$$

即特定系譜路徑的權重非常高。

在這種制度中：

$$
\text{House repair}
$$

不能完全忽略：

$$
B_D.
$$

因此皇室不是普通家制度的簡單放大版。

它是一個具有特殊 genealogical constraint 的 House。

---

# 七、2026 年皇室修法：血統與家系不是二選一

2026 年 7 月，日本國會通過皇室制度重大修法。

其中一項核心機制，是允許舊皇族十一宮家的父系男系男性後裔透過收養重新取得皇族身份；另一項則允許女性皇族婚後保留皇族身份。

這件事的模型意義很大。

它不是：

$$
\text{House preservation}
\Rightarrow
\text{ignore genealogy}.
$$

而是：

$$
\boxed{
\text{House-repair mechanism}
\quad
\text{subject to}
\quad
\text{genealogical eligibility}.
}
$$

可以寫成：

$$
\max H
$$

subject to:

$$
B_D=1.
$$

也就是：

> 可以利用收養這個家系修復技術，但誰能被吸收，先由指定系譜路徑決定。

這是「血統—家系雙重正統性」非常清楚的現代案例。

---

# 八、第三刀：不同制度使用不同正統性權重

本文因此不提出單一：

$$
\text{Japanese Value Function}.
$$

而使用制度依賴函數：

$$
\mathcal L_j
=
w_{B,j}B_G
+
w_{D,j}B_D
+
w_{H,j}H
+
w_{P,j}P
+
w_{R,j}R
+
w_{F,j}F
+
w_{C,j}C.
$$

其中：

 $j$ 代表不同制度。

變量可暫定為：

- $B_G$ ：實際生物親緣；
- $B_D$ ：系譜合法性；
- $H$ ：家系持續；
- $P$ ：家產、職位與制度資源；
- $R$ ：家格、聲望與排名；
- $F$ ：實際功能能力；
- $C$ ：外部共同承認。

不同場域有不同：

$$
\mathbf w_j.
$$

---

# 九、商家、武家、皇室可以給不同答案

例如商家可能更接近：

$$
w_H+w_P+w_F
>
w_{B_G}.
$$

如果一名非親生繼承人能維持：

- 家名；
- 企業；
- 財產；
- 員工；
- 商業關係；

則家業延續可能優先。

武家則可能：

$$
w_H+w_D+w_R+w_P
$$

共同較高。

皇室則可能：

$$
w_D
$$

極高。

因此：

$$
\boxed{
\text{「日本重血還是重家？」沒有單一答案。}
}
$$

真正問題是：

> 在哪一個制度裡，哪一種連續性最不能被破壞？

---

# 十、這不是日本人的永恆文化本質

這裡必須明確避免文化本質論。

現代研究已指出，近代日本被理解為普遍、嚴格父系的 $ie$ 制度，很大程度上受到明治國家與民法制度化塑造；它雖以江戶武士家戶為重要參照，卻不能直接倒投射成所有前近代日本平民從古至今都採用完全相同制度。

因此：

$$
\boxed{
\text{Samurai house logic}
\neq
\text{all Japanese families in all periods}.
}
$$

本文處理的是：

> 某些日本政治、武家、商家與皇室制度如何配置血統與家系權重。

不是：

> 日本人天生如何。

---

# 十一、House Society：已有的人類學前例

Lévi-Strauss 提出的 House Society 概念，正好提供一個重要比較框架。

House 不必是一個純父系或純母系血緣群體。

它可以同時圍繞：

- 血緣；
- 婚姻；
- 名稱；
- 財產；
- 地位；
- 象徵中心；

形成長期社會單位。

近年人類學與考古研究仍把 House 理解成介於純血緣組織與階級／政治組織之間的混合形式，並指出這一框架曾被用來理解平安日本、中世紀歐洲與古希臘。

所以：

$$
\boxed{
\text{House}
\neq
\text{Lineage}.
}
$$

這為日本大量養子、婚姻與家系保存提供了既有理論背景。

---

# 十二、日本悖論 III 真正消失的地方

原本：

$$
\text{Blood}
\quad\text{vs}\quad
\text{House}.
$$

如果假設兩者都在競爭成為唯一最高目標，就會形成悖論。

但若：

$$
B_G,
B_D,
H
$$

只是不同狀態變量，

而制度真正最大化的是：

$$
\mathcal L,
$$

則：

$$
\boxed{
\text{Blood and House need not conflict}.
}
$$

例如：

## 情況 A：自然兒子存在

$$
B_G\uparrow,\quad
B_D\uparrow,\quad
H\uparrow.
$$

幾個變量同時滿足。

## 情況 B：沒有兒子，但有親族養子

$$
B_G\downarrow,\quad
B_D>0,\quad
H\uparrow.
$$

透過小幅犧牲某些生物親緣，保存家系與系譜。

## 情況 C：能力優先的商家養子

$$
B_G\approx0,
\quad
H\uparrow,
\quad
F\uparrow,
\quad
P\uparrow.
$$

功能與家業持續可能補償血緣下降。

## 情況 D：皇室

$$
H
$$

需要修復，

但：

$$
B_D
$$

又被設為高權重約束。

所以制度尋找：

$$
\boxed{
\text{high-}H
\text{ solution inside admissible }B_D.
}
$$

沒有邏輯矛盾。

---

# 十三、連續性對象問題

這導向本篇最重要的新問題。

當我們說：

> 某一家延續了五百年。

真正延續的是什麼？

可能包括：

$$
\mathcal O_C
=
\{
B_G,
B_D,
H_N,
H_P,
H_O,
H_R,
H_V,
H_C
\}.
$$

其中：

- $B_G$ ：生物親緣；
- $B_D$ ：系譜路徑；
- $H_N$ ：家名；
- $H_P$ ：財產；
- $H_O$ ：職位；
- $H_R$ ：關係網絡；
- $H_V$ ：歷史敘事；
- $H_C$ ：社會承認。

本文將：

$$
\boxed{
\text{Which of these must remain continuous?}
}
$$

稱為：

# Continuity Object Problem
# 連續性對象問題

---

# 十四、連續性不是 0/1，而是向量

所以不應只寫：

$$
H_t=H_{t+1}
$$

或：

$$
H_t\neq H_{t+1}.
$$

更好的表示是：

$$
\mathbf C_H(t,t+1)
=
(
c_B,
c_D,
c_N,
c_P,
c_O,
c_R,
c_V,
c_C
).
$$

每個維度：

$$
c_i\in[0,1].
$$

例如養子繼承可能：

$$
c_B<1,
$$

但：

$$
c_N,c_P,c_O,c_R,c_V,c_C
\approx1.
$$

因此整體社會仍判斷：

$$
H_t\sim H_{t+1}.
$$

所以：

$$
\boxed{
\text{Identity continuity is a weighted vector, not a binary fact}.
}
$$

---

# 十五、主家／分家重新理解

如果主家與分家的生物血緣相近，

為什麼主家通常具有更高象徵地位？

因為主家可能掌握：

- 核心家名；
- 本家祭祀；
- 祖產；
- 主要家譜；
- 官職；
- 家督；
- 象徵物；
- 對分家的認證；
- 最主要的歷史敘事。

因此：

$$
\boxed{
\text{Main House Status}
\approx
\text{Narrative / Institutional Centrality}.
}
$$

而不只是：

$$
\text{more blood}.
$$

這將在下一篇被推進為「敘事正統場」。

---

# 十六、養子為什麼常被「家」吸收，而不是把家歸零？

假設某家已累積：

$$
M_H(t)
=
\sum_{\tau=1}^{t}
K_H(\tau),
$$

其中包含：

- 歷史；
- 財產；
- 聲望；
- 關係；
- 儀式；
- 社會認知。

現在一名養子進入：

$$
A_t.
$$

並不是：

$$
H_{t+1}=A_t.
$$

更接近：

$$
H_{t+1}
=
M_H(t)
+
A_t.
$$

如果：

$$
M_H(t)\gg A_t,
$$

則從身份結構看，可能是：

$$
\boxed{
A_t
\text{ is absorbed into }
H,
}
$$

而不是：

$$
H
\text{ is replaced by }
A_t.
$$

所以養子個體身份可以改變，

而家的歷史狀態大量保留。

---

# 十七、西歐再次連回來

日本不是唯一面對：

$$
\text{blood}
\quad\text{vs}\quad
\text{house}
$$

問題的文明。

中世紀與近代歐洲貴族 House／Dynasty 同樣要解決：

- 無男性繼承人；
- 女性繼承；
- 旁系；
- 王朝聯姻；
- 家名變更；
- 複合王朝。

不同制度可以選擇：

$$
\text{bloodline continuity}
$$

與：

$$
\text{house / title / property continuity}
$$

的不同組合。

因此真正跨文明問題不是：

> 日本和歐洲哪一邊更重血？

而是：

$$
\boxed{
\text{How does each institution define its object of continuity?}
}
$$

這是一個比「封建文化相似」更精確的比較方向。

---

# 十八、正式命題一：血統分離命題

實際生物親緣與制度系譜合法性並不等價：

$$
\boxed{
B_G\neq B_D.
}
$$

因此以遺傳比例直接解釋王朝或世家正統性，會產生類型錯誤。

---

# 十九、正式命題二：多目標正統性命題

制度正統性不是單一血統函數：

$$
\mathcal L
\neq
f(B_G).
$$

而更可能是：

$$
\boxed{
\mathcal L
=
F(
B_G,
B_D,
H,
P,
R,
F,
C,
\ldots
).
}
$$

不同制度有不同權重。

---

# 二十、正式命題三：受約束家系修復命題

養子制度與血統規則可以同時成立。

若候選集合由系譜條件限制：

$$
\mathcal E
=
\{a:B_D(a)\ge\theta_D\},
$$

則制度可以在：

$$
a\in\mathcal E
$$

之內最大化：

$$
H(a).
$$

因此：

$$
\boxed{
\text{Adoption}
+
\text{genealogical restriction}
}
$$

不是邏輯矛盾。

---

# 二十一、正式命題四：主家中心性命題

主家與分家的差異未必主要來自遺傳濃度，而可能來自其在制度、敘事與承認網絡中的中心性：

$$
\boxed{
C_{\mathrm{main}}
>
C_{\mathrm{branch}}.
}
$$

因此家格是一個網路與歷史位置問題。

---

# 二十二、正式命題五：連續性向量命題

任何「家系延續」都應表示為：

$$
\mathbf C_H
=
(c_1,c_2,\ldots,c_n)
$$

而不是單一 0/1 變量。

兩個社會都說「同一家」，

實際保存的維度可能完全不同。

---

# 二十三、可反駁預測

如果本模型成立，應至少看到：

第一，不同日本制度對養子、婚姻與血統的容許度不同，而非存在單一全國性「血統偏好值」。

第二，武家養子應受到親族、家格或社會地位的系統性約束，而非完全隨機。

第三，主家地位應與制度／敘事中心性相關，而不能單靠生物親緣距離解釋。

第四，皇室等高系譜權重制度會在家系修復時施加更強候選資格限制。

第五，政權與社會仍可能承認血緣較遠但系譜位置合法者，勝過生物親緣更近但制度路徑不合法者。

---

# 二十四、主要反論

## 反論一：所謂「正統性函數」只是事後合理化

回應方式不能靠概念，而要研究真實婚姻、收養、繼承與官職選擇資料，看權重是否具有可預測性。

## 反論二：血統語言其實只是政治宣傳

如果如此，則：

$$
B_D
$$

仍可能具有社會功能，只是它應被視為象徵政治變量，而不是客觀生物值。

## 反論三：日本養子很多，所以血統其實不重要

這與武士養子的親族／地位限制，以及皇室系譜規則不完全相容，需要分制度處理。

## 反論四：皇室不能代表日本社會

成立。

因此皇室只能作為「高系譜權重制度」的極端案例，不能外推全日本。

## 反論五：近代 $ie$ 是明治重構

這也是重要限制。

因此本文不能把明治以後的國家化家制度直接投射回所有中世紀與平民社會。

---

# 二十五、從雙重正統性進入更高階模型

到這裡，原本的問題：

$$
\text{血重要？還是家重要？}
$$

其實已經被解構。

因為：

$$
B_G,
B_D,H,P,R,F,C
$$

都只是輸入變量。

真正還沒有回答的是：

> 為什麼某些變量在某些時代與制度中會突然得到很高權重？

例如：

為什麼某個家一旦被認為接近皇統，就能取得高象徵地位？

為什麼某個養子進入家後，外界願意把他視為「那一家的人」？

為什麼主家比某個遺傳距離很近的分家更具有權威？

為什麼歷史故事、祖先、家名與婚姻可以產生現實政治效果？

這表示：

$$
\mathcal L
$$

本身不是個體內部計算。

它可能是一個：

$$
\boxed{
\text{distributed social recognition process}.
}
$$

也就是：

$$
\mathcal L_H
=
F(
\text{self-claim},
\text{other houses},
\text{state},
\text{ritual},
\text{history},
\text{collective expectation}
).
$$

這就是下一篇的核心。

---

# 二十六、下一篇接口：敘事正統場

下一篇將正式提出：

$$
\boxed{
\mathcal N_H(t)
=
\text{Narrative–Legitimacy Field}.
}
$$

它不是：

$$
\text{Blood}
$$

也不是：

$$
\text{House}.
$$

而是：

> 血統、家系、財產、頭銜、婚姻、歷史、祖先故事與社會共同承認形成的上層動態場。

下一篇將處理：

$$
l_i(H)
=
f(
x_i,
E_i[l_j(H)]
),
$$

也就是一個行動者評估某家的正統性時，同時會估計：

> 其他人會怎麼看？

由此將「看空氣」改寫為：

$$
\boxed{
\text{Recursive Social Estimation}.
}
$$

因此下一篇為：

# 《日本悖論 IV：家與血都只是故事的載體？——敘事正統場與「看空氣」的分散式社會計算》

---

# 二十七、結論

日本悖論 III 的表面問題是：

> 日本到底重視血統還是家系？

本文的答案是：

$$
\boxed{
\text{這可能是一個錯誤二分。}
}
$$

因為至少存在：

$$
B_G
=
\text{實際遺傳親緣},
$$

$$
B_D
=
\text{系譜合法性},
$$

以及：

$$
H
=
\text{家系連續性}.
$$

三者不是同一變量。

不同制度則使用：

$$
\mathcal L_j
=
F_j(
B_G,B_D,H,P,R,F,C,\ldots
)
$$

進行不同權重配置。

因此養子與血統並不必然衝突。

一個制度完全可以：

$$
\max H
$$

同時要求：

$$
B_D\ge\theta_D.
$$

真正值得研究的問題於是從：

$$
\text{Blood vs House}
$$

轉變成：

$$
\boxed{
\text{What is the object of continuity?}
}
$$

以及：

$$
\boxed{
\text{Who decides that continuity has been preserved?}
}
$$

第一個問題是「連續性對象問題」。

第二個問題則會把我們帶入：

$$
\boxed{
\text{敘事正統場}.
}
$$

日本悖論至此已經從地形治理問題，經過政治節點的代際耐久性，再進入一個更抽象的社會身份與正統性計算問題。

---

## 初版參考文獻與資料

1. Ray A. Moore, “Adoption and Samurai Mobility in Tokugawa Japan,” *The Journal of Asian Studies*.
2. Claude Lévi-Strauss, house society / société à maison 相關研究。
3. “Bringing Kinship Back into the House,” *Cambridge Archaeological Journal*, 2026.
4. “Kinship Trouble: What, When, Where, Why, and How—and So What?”, *Cambridge Archaeological Journal*, 2026.
5. Ueno Chizuko, “Modern Patriarchy and the Formation of the Japanese Nation State,” in *Multicultural Japan*.
6. Imperial Household Agency, *The Imperial House Law* and current materials on Imperial Succession.
7. Japan Diet / 2026 Imperial House Law revision materials concerning female imperial members and adoption of male-line descendants of former imperial branches.

---

## 版本註記

本稿 v0.1 已重新查核德川武士養子、House Society、人類學家系理論、日本近代 $ie$ 重構，以及 2026 年日本皇室制度修法。

後續 v0.2 應增加：

1. 公家、武家、商家分別的婚姻與養子選擇統計；
2. 本家／分家地位的歷史操作資料；
3. 日本「血筋」「家柄」「家格」概念在不同時期的語義差異；
4. 皇室男系論與歷史女性天皇之間的制度史差異；
5. 西歐 House / Dynasty 的女性線、旁系與王朝更名比較；
6. 系譜合法性與實際 genetic relatedness 的形式模型。
