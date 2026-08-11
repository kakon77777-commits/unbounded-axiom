# 數學難度不是計算量：二十種問題障礙與 AI 數學難度譜系

## Mathematical Difficulty Is Not Computational Cost: Twenty Problem Barriers and a Difficulty Spectrum for AI Mathematics

**系列：計算基底、認知干預與廣義智能計算研究，第 1 篇／共 8 篇**  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**日期：2026-08-07**

---

## 摘要

人工智慧在數學問題上的能力，經常以正確率、題目等級、解題時間、計算資源或競賽成績描述。然而，這些指標容易將若干本質不同的困難混合在一起：搜索空間的規模、正確表示法的發現、隱藏結構的辨識、中間命題的建立、形式證明的完成，以及對問題本身的重新審視，並不構成單一線性的「難度」。

近年的數學 AI 進展更凸顯此問題。AlphaProof 與 AlphaGeometry 2 已於 2024 年達到國際數學奧林匹亞銀牌等級，而 2025 年 Gemini Deep Think 更以自然語言直接完成五題 IMO 題目並達到金牌標準；另一方面，FormalMATH、FormalProofBench 與 TheoremBench 等形式數學基準仍顯示，現有系統在長證明、依賴豐富的定理結構、研究生程度問題，以及有效率的證明規劃上存在明顯缺口。這意味著「會解高難度數學題」與「具有完整的一般數學證明能力」不能直接視為同一個標量。

本文提出一套以**認知障礙類型**而非傳統教育級別為中心的數學難度分類。首先整理二十類可獨立造成困難的問題結構，繼而提出五維難度向量：

$$
D(P,A)=
\left(
D_{\mathrm{search}},
D_{\mathrm{representation}},
D_{\mathrm{structure}},
D_{\mathrm{proof}},
D_{\mathrm{meta}}
\right),
$$

其中難度不是問題 $P$ 的單獨屬性，而是問題 $P$ 、求解系統 $A$ 、可用工具、資源與表示方式共同形成的關係量。

本文主張：

$$
\boxed{
\text{數學難度}
\neq
\text{計算量}
\neq
\text{證明長度}
\neq
\text{敘述複雜度}
}
$$

並進一步提出：真正適合評估高階 AI 數學能力的問題，不應只追求更大的搜索空間，而應有意識地組合多種彼此相對獨立的認知障礙。

---

## 關鍵詞

AI 數學推理、數學難度、定理證明、證明搜尋、表示轉換、問題重構、元認知、形式數學、數學基準、認知障礙

---

# 1. 問題：什麼叫做「一道難題」？

一個極其複雜的數學敘述，可能存在一個三行反例。

一個只需要十幾個符號陳述的問題，也可能需要數十年的數學發展才能解決。

因此至少必須區分：

$$
L(P)=\text{問題敘述長度},
$$

$$
C(P)=\text{某計算模型下的計算成本},
$$

$$
S(P)=\text{搜索成本},
$$

$$
\Pi(P)=\text{證明成本},
$$

以及：

$$
R(P)=\text{找到正確表示的困難}.
$$

一般而言不存在：

$$
L(P_1)>L(P_2)
\Rightarrow
D(P_1)>D(P_2).
$$

同樣不存在：

$$
C(P_1)>C(P_2)
\Rightarrow
D(P_1)>D(P_2).
$$

我們首先必須放棄「難度是一根尺」的直覺。

---

# 2. 一個失敗案例：表面複雜度與真實證明深度

考慮一類循環差分問題：

$$
T(a_1,\ldots,a_n)
=
(
|a_1-a_2|,
|a_2-a_3|,
\ldots,
|a_n-a_1|
).
$$

若提出一個看似複雜的全稱命題，加入：

$$
\max_i a_i\le 2^n,
$$

$$
k\le Cn,
$$

以及至少

$$
\left\lceil\frac n2\right\rceil
$$

個位置歸零等條件，題目表面上可能同時包含：

- 離散動力系統；
- 整數結構；
- 漸近複雜度；
- 循環圖；
- 絕對值；
- 局部與全局性質。

但若存在：

$$
A=(0,1,3)
$$

這樣的小尺度反例，則整個問題實際上的證明樹深度極低。

因此：

$$
\boxed{
\text{surface complexity}
\not\Rightarrow
\text{reasoning depth}.
}
$$

這是設計 AI 數學難題時首先必須排除的假難度。

---

# 3. 二十種彼此不同的數學困難

以下二十類障礙並非宣稱為完備分類，也不是數學上的互斥分割。它們是一套工作性 taxonomy，用來辨識「模型究竟被什麼卡住」。

---

## 3.1 小尺度搜尋無法直接終結問題

如果全稱命題：

$$
\forall x\in X,\ P(x)
$$

在極小的 $x$ 上就存在反例，那麼強大的搜索系統可以迅速終結問題。

更困難的情況是：

$$
P(x)=1
$$

對巨大範圍均成立，但有限實驗無法決定全稱命題。

這測試的是：

$$
\text{finite evidence}
\rightarrow
\text{universal justification}
$$

之間的距離。

---

## 3.2 無法靠知名題型直接匹配

若一題可以迅速辨識為：

$$
\text{Pell equation},
$$

$$
\text{Hall theorem},
$$

$$
\text{Cauchy--Schwarz},
$$

或某個標準 generating-function 問題，那麼大量困難可能只是知識檢索。

更高階的問題應使：

$$
\text{retrieval}
\neq
\text{solution}.
$$

---

## 3.3 需要多個不自然結構連接

困難可能不是沒有任何洞見，而是第一個洞見仍遠不足夠：

$$
A
\rightarrow
X
\rightarrow
Y
\rightarrow
Z.
$$

尤其當：

$$
A\rightarrow X
$$

與：

$$
X\rightarrow Y
$$

分別需要完全不同的表示方式時，難度會顯著增加。

---

## 3.4 大量數值證據不能代替證明

即使：

$$
P(n)=1,\qquad
1\le n\le 10^9,
$$

也不能一般地推出：

$$
\forall n,\ P(n).
$$

這種問題刻意製造：

$$
\text{empirical confidence}
$$

與：

$$
\text{logical validity}
$$

之間的張力。

---

## 3.5 存在高度誘惑的假證明

最好的 proof trap 不是明顯錯誤，而是：

$$
95\%
$$

的推理均正確，只有一個量詞交換、逆命題誤用、極限交換或隱藏假設失敗。

它主要測：

$$
\text{proof generation}
$$

與：

$$
\text{proof auditing}
$$

是否真正分離。

---

## 3.6 局部結構與全局結構互不保證

可能有：

$$
P(U_i)=1
$$

對每個局部區域成立，但：

$$
P\left(\bigcup_iU_i\right)=0.
$$

這類問題測試局部資訊能否被正確提升到整體。

---

## 3.7 最容易找到的不變量不是有用的不變量

存在：

$$
I(Tx)=I(x)
$$

並不代表 $I$ 足以推出目標。

真正困難可能在於找到：

$$
\Phi(x)
$$

使其同時滿足不變性或單調性，以及足夠強的結論約束。

所以：

$$
\text{find invariant}
\neq
\text{find useful invariant}.
$$

---

## 3.8 正確的中間命題比原問題更難想到

直接證明：

$$
P
$$

可能極難，但建立較強命題：

$$
Q\Rightarrow P
$$

後反而容易。

這測試求解者是否有能力改變證明目標，而不只是持續攻擊原始命題。

---

## 3.9 必須發明新的表示法

有些問題真正缺少的不是 theorem，而是 language。

例如從：

$$
(a_1,\ldots,a_n)
$$

轉成：

$$
G_A,
$$

或定義：

$$
S_t=\{i:a_i\le t\}.
$$

表示法一旦改變，原本巨大的搜索空間可能瞬間產生新結構。

---

## 3.10 表面領域與核心領域不同

例如：

$$
\text{number theory}
\rightarrow
\text{graph theory}
\rightarrow
\text{linear algebra}.
$$

此類問題的主要障礙是 representation transfer，而不只是單一領域知識不足。

---

## 3.11 對稱性既是優勢也是陷阱

由：

$$
\text{symmetric assumptions}
$$

不能一般推出：

$$
\text{symmetric extremizer}.
$$

啟發式若過度依賴對稱性，可能主動刪除真正答案。

---

## 3.12 最後必須證明「不存在」

找到 witness：

$$
\exists x\,P(x)
$$

與證明：

$$
\nexists x\,P(x)
$$

具有不同的搜索結構。

後者通常要求某種全局 obstruction、有限 certificate 或結構定理。

---

## 3.13 答案不是單一對象，而是一整族

「找到一個解」遠弱於：

$$
\boxed{\text{classify all solutions}.}
$$

真正任務可能是找：

$$
G:\Theta\rightarrow\mathcal E
$$

使：

$$
\operatorname{Im}G=\mathcal E.
$$

---

## 3.14 問題存在相變點

當參數 $\lambda$ 越過：

$$
\lambda_c,
$$

問題的支配機制可能改變。

在一個 regime 上得到的規律不能直接外推至另一 regime。

---

## 3.15 邊界案例支配定理正確性

generic case 可能很容易，而：

$$
x=0,
$$

$$
\det A=0,
$$

或其他退化情況才是真正 proof burden。

這測試的是 proof completeness。

---

## 3.16 正確答案依賴量詞順序

例如：

$$
\forall x\exists y\,P(x,y)
$$

與：

$$
\exists y\forall x\,P(x,y)
$$

不是同一命題。

長證明中一次無意識的量詞交換即可摧毀整個結論。

---

## 3.17 同一 lemma 必須以不同邏輯方向使用

例如先證：

$$
A\Rightarrow B,
$$

後面卻需要：

$$
\neg B\Rightarrow\neg A.
$$

真正的 proof graph 因而不是線性鏈，而是具有多方向依賴的結構。

---

## 3.18 正確道路需要排除大量錯誤道路

求解過程可能是：

$$
H_1\rightarrow\bot,
$$

$$
H_2\rightarrow\bot,
$$

$$
H_3\rightarrow\bot,
$$

最終才保留 $H_4$。

因此最終 proof trace 可能非常短，但 discovery cost 很高。

---

## 3.19 最短證明與最容易發現的證明不同

設：

$$
\pi_{\min}
=
\arg\min_{\pi:V(\pi,P)=1}|\pi|.
$$

最短證明可能依賴一個極不自然的洞見，而較長證明反而容易逐步搜索得到。

所以至少需要區分：

$$
D_{\mathrm{discovery}}
$$

與：

$$
D_{\mathrm{compression}}.
$$

TheoremBench 的近期結果也支持這種區分的必要性：一些證明系統能完成定理，卻使用相當長、低效率的 tactic traces；加入明確 supporting premises 後，表現又會顯著改變。

---

## 3.20 題目本身需要被質疑

最高階問題不一定是：

$$
P\rightarrow\text{proof}.
$$

求解者可能必須先問：

$$
\text{條件是否多餘？}
$$

$$
\text{結論是否可加強？}
$$

$$
\text{真正控制問題的參數是不是另一個量？}
$$

甚至：

$$
\text{我們是否正在解錯問題？}
$$

因此求解空間從 solution space 擴大成：

$$
\boxed{\text{problem space}.}
$$

---

# 4. 五維 AI 數學難度向量

為避免把上述二十類障礙重新壓成單一分數，本文提出五個較高階維度：

$$
\boxed{
D(P,A)=
(
D_S,
D_R,
D_H,
D_\Pi,
D_M
)
}
$$

其中求解系統記為 $A$。

---

## 4.1 搜索難度

$$
D_S=D_{\mathrm{search}}.
$$

描述：

- 候選空間大小；
- 分支數；
- 搜索深度；
- 反例稀疏度；
- 可平行程度。

它回答：

> 如果表示法與驗證器已經給定，還需要搜索多少？

---

## 4.2 表示難度

$$
D_R=D_{\mathrm{representation}}.
$$

描述：

> 要把原始問題轉成有利於求解的表示形式有多難？

有些問題：

$$
D_S\gg0
$$

只是因為：

$$
D_R
$$

尚未被解決。

找到新表示後：

$$
D_S'
\ll D_S.
$$

---

## 4.3 結構發現難度

$$
D_H=D_{\mathrm{structure}}.
$$

表示從資料或局部規律中發現：

- invariant；
- symmetry；
- obstruction；
- decomposition；
- latent family；
- phase transition；
- cross-domain correspondence；

的困難。

---

## 4.4 證明完成難度

$$
D_\Pi=D_{\mathrm{proof}}.
$$

即使核心洞見已知，仍可能需要：

- 大量 lemma；
- 邊界處理；
- 量詞控制；
- dependency management；
- formal verification。

FormalMATH 在 5,560 個 Lean4 問題上的結果顯示，即使是當時最強的形式證明模型，在實際 sampling budget 下成功率仍然有限，而且不同數學領域間存在顯著偏差。FormalProofBench 在研究生程度題目上也顯示前沿模型的 formally verified proof 能力仍快速下降。

---

## 4.5 元問題難度

$$
D_M=D_{\mathrm{meta}}.
$$

它描述：

> 系統需要在多大程度上質疑自己的方法、抽象層或原始問題？

包括：

- 發現正在使用錯方法；
- 發現假設多餘；
- 發現真正問題不同；
- 改變 objective；
- 建立更一般命題；
- 放棄先前高可信策略。

這可能是最接近研究型數學的一個維度。

FrontierMath 已將 benchmark 從競賽型高難題延伸到真正尚未解決、且可能沒有已知解答的數學問題，目的之一正是評估更接近研究活動的能力；這類任務自然比固定答案 benchmark 更依賴問題選擇、探索與研究判斷。

---

# 5. 難度不是問題的固定屬性

本文特別不寫：

$$
D(P).
$$

更準確的是：

$$
\boxed{
D(P,A,E,R)
}
$$

其中：

$$
P=\text{problem},
$$

$$
A=\text{solver},
$$

$$
E=\text{available environment/tools},
$$

$$
R=\text{resource budget}.
$$

同一道問題：

對沒有定理庫的人類可能：

$$
D_R=9.
$$

對已檢索到正確 lemma 的 AI：

$$
D_R=2.
$$

對具備暴力計算資源的系統：

$$
D_S=1.
$$

但對無工具的人類：

$$
D_S=8.
$$

因此：

$$
\boxed{
\text{Difficulty is relational, not absolute.}
}
$$

---

# 6. 為什麼 IMO、形式證明與研究數學不能放在同一根尺上？

2024 年 AlphaProof 需要先將自然語言題目轉成 Lean 等形式語言，並以強化學習和搜索完成證明；部分題目的計算甚至需要數日。2025 年 Gemini Deep Think 則直接從官方自然語言題面輸出 IMO 級證明，並在正式評分下取得金牌標準。這是巨大進步，但兩種系統的工作型態本身已非常不同。

另一方面，AlphaGeometry 的成功亦來自神經模型提出構造與 symbolic deduction engine 進行嚴格推導的混合架構，其 2024 系統在 30 個 Olympiad geometry problems 中解出 25 題。這顯示「產生候選洞見」與「可靠地展開、驗證推理」可以由不同機制負責。

因此至少有：

$$
\text{informal discovery},
$$

$$
\text{formal proof search},
$$

$$
\text{proof verification},
$$

$$
\text{research exploration}
$$

四種不同任務。

不能只說：

$$
\text{Model A is better at mathematics}.
$$

應該問：

> Better at which mathematical barrier?

---

# 7. 一個新的 AI 數學 benchmark 設計原則

如果希望題目真正區分高階系統，至少可以採取以下原則。

第一，不讓小尺度搜索立即終結：

$$
D_S>0.
$$

第二，不讓標準模板檢索直接完成：

$$
D_R>0.
$$

第三，至少存在兩層獨立結構發現：

$$
A\rightarrow X\rightarrow Y.
$$

第四，提供大量可能誤導的數值證據：

$$
\text{evidence}\neq\text{proof}.
$$

第五，存在至少一條高度合理但錯誤的證明路徑。

第六，要求 proof auditing，而非只看最終答案。

第七，加入 classification 或 non-existence，而不只要求 witness。

第八，引入至少一個需要重新表示問題的階段。

第九，評估 discovery trace，而不只是 final proof。

第十，允許模型質疑原始命題。

可以將一個研究級 benchmark instance 表示為：

$$
B_i=
(
P_i,
\mathcal O_i,
\mathcal V_i,
\mathcal T_i
),
$$

其中：

$$
P_i
$$

是問題；

$$
\mathcal O_i
$$

記錄障礙配置；

$$
\mathcal V_i
$$

是驗證方法；

$$
\mathcal T_i
$$

則記錄允許的工具與資源。

---

# 8. 「困難」可以來自不同原因

同樣是模型失敗：

$$
A(P)=\bot,
$$

可能代表完全不同的事情。

模型可能：

1. 沒搜索到正確 branch；
2. 找不到好的表示；
3. 沒看到隱藏 invariant；
4. 看到了結構但證不完；
5. 證明基本正確但有形式漏洞；
6. 被錯誤 prior 誘導；
7. 一直在解一個不自然的 reformulation；
8. 根本沒有意識到原命題可能為假。

因此：

$$
\boxed{
\text{failure}
\neq
\text{lack of mathematical intelligence}.
}
$$

同樣：

$$
\boxed{
\text{success}
\neq
\text{all relevant capabilities are present}.
}
$$

一個巨大搜索系統可能靠枚舉成功；另一個系統可能靠極短結構洞見成功。

只看答案無法區分兩者。

---

# 9. 從結果評估走向過程評估

傳統：

$$
Score(A,P)=
\begin{cases}
1,&\text{correct}\\
0,&\text{wrong}
\end{cases}
$$

太粗糙。

可以改為：

$$
\operatorname{Score}
=
F(
C,
L,
V,
K,
R,
G
),
$$

其中例如：

$$
C=\text{correctness},
$$

$$
L=\text{search/proof length},
$$

$$
V=\text{verifiability},
$$

$$
K=\text{coverage/completeness},
$$

$$
R=\text{representation quality},
$$

$$
G=\text{generalization}.
$$

近期 TheoremBench 已開始利用 theorem-level coverage 與 token efficiency 觀察形式證明系統，而不是只問「最後有沒有完成定理」；LeanProgress 則直接研究 proof-progress prediction 如何改善 proof search。這些工作與本文主張的方向一致：數學 AI 的評估需要逐步從 outcome-only 轉向 structure-aware evaluation。

---

# 10. 搜索與洞見不是互斥的

本文亦不主張：

$$
\text{search}
<
\text{insight}.
$$

這種階層本身就是危險的。

所謂洞見可能只是：

$$
\text{極高效率的 search-space transformation}.
$$

而大量搜索也可能產生人類無法直接找到的新結構。

因此更好的問題是：

$$
\boxed{
\text{某能力究竟改變了哪一個難度維度？}
}
$$

例如：

- 更多算力主要降低某些 $D_S$ ；
- 更強 retrieval 可能降低 $D_R$ ；
- 更好的表示學習降低 $D_R$ 與 $D_H$ ；
- proof assistant 降低 correctness uncertainty，但不必然降低 discovery difficulty；
- metacognitive mechanism 主要作用於 $D_M$。

這個觀點將在後續系列進一步展開。

---

# 11. 從五維向量到困難形狀

假設兩題總體感覺同樣困難：

$$
P_1,\quad P_2.
$$

實際可能：

$$
D(P_1)
=
(9,1,2,2,1),
$$

而：

$$
D(P_2)
=
(2,8,8,7,6).
$$

第一題主要是搜索型。

第二題則主要是表示、結構與證明型。

即使最終解題時間相同：

$$
T(P_1)\approx T(P_2),
$$

它們對智能系統的要求完全不同。

因此真正有意義的不是 difficulty score，而是：

$$
\boxed{\text{difficulty profile}.}
$$

甚至可以視為一種「問題形狀」。

---

# 12. 一個初步的問題—能力耦合表示

令問題障礙向量：

$$
\mathbf d_P\in\mathbb R_{\ge0}^m,
$$

智能體能力向量：

$$
\mathbf c_A\in\mathbb R_{\ge0}^n.
$$

再定義耦合矩陣：

$$
W_P\in\mathbb R^{m\times n}.
$$

則實際難度不應只寫成：

$$
\|\mathbf d_P\|.
$$

而可抽象表示為：

$$
D_{\mathrm{eff}}
=
\mathcal F
(
\mathbf d_P,
\mathbf c_A,
W_P,
R
).
$$

其中 $R$ 是外部資源。

這意味著：

> 相同能力在不同問題上具有不同邊際價值。

例如超強計算能力：

$$
C\rightarrow\infty
$$

對有限枚舉問題可能近乎壓倒性；

但對「應該建立哪個新定義」這類 $D_R$ 或 $D_M$ 很高的問題，未必直接提供同等比例的收益。

本文暫不對 $\mathcal F$ 給出唯一形式；後續論文將把它拆成「非適應性計算基線」與「認知干預」兩部分。

---

# 13. 本文的核心命題

本文最終提出六個工作命題。

### 命題一：非單標量難度命題

不存在一個對所有數學求解系統都充分的單一數學難度標量。

$$
\boxed{
D\neq d\in\mathbb R
}
$$

在實用評估中，至少需要多維 profile。

---

### 命題二：敘述—證明分離命題

$$
\boxed{
\text{description complexity}
\not\sim
\text{proof-discovery complexity}.
}
$$

表面複雜的問題可以有極短反例；極簡問題可以具有巨大 discovery difficulty。

---

### 命題三：搜索—表示分離命題

$$
\boxed{
D_{\mathrm{search}}
\neq
D_{\mathrm{representation}}.
}
$$

改變表示可以改變有效搜索空間，因此兩者不能直接合併。

---

### 命題四：發現—驗證分離命題

$$
\boxed{
\text{discovering }\pi
\neq
\text{verifying }\pi.
}
$$

形式驗證器可以極度可靠，但不因此自動解決 proof discovery。

---

### 命題五：成功路徑非唯一命題

同一問題可能由：

$$
\text{search},
$$

$$
\text{retrieval},
$$

$$
\text{abstraction},
$$

$$
\text{formal deduction},
$$

或它們的混合成功解決。

因此最終答案不能唯一決定背後能力。

---

### 命題六：研究級數學包含問題空間操作

競賽型問題通常固定：

$$
P.
$$

研究型問題則可能要求：

$$
P
\rightarrow
P'
\rightarrow
Q
\rightarrow
\text{new theorem}.
$$

因此：

$$
\boxed{
D_{\mathrm{meta}}
}
$$

應成為高階數學 AI 評估中的獨立維度。

---

# 14. 與後續系列的接口

本文只回答：

> 一道數學問題究竟可能難在哪裡？

下一篇將刻意移除：

- 直覺；
- 經驗；
- 主動選擇；
- 動態目標修正；
- 記憶重建；
- 元認知。

僅保留一個可機械執行的計算系統，重新處理本文二十類障礙。

即建立：

$$
\boxed{
\text{Non-Adaptive Computational Baseline}
}
$$

並詢問：

> 當沒有智能體主動干預時，這二十種「認知困難」究竟還剩下什麼？

預期其中相當一部分將坍縮為：

$$
\text{enumeration},
$$

$$
\text{transformation search},
$$

$$
\text{proof search},
$$

$$
\text{verification},
$$

$$
\text{compression},
$$

以及：

$$
\text{resource limitation}.
$$

而這也將為後續比較「純計算」與「智能干預」提供共同基線。

---

# 15. 結論

數學難度並不是「需要算多久」的同義詞。

也不是：

$$
\text{高中}
<
\text{大學}
<
\text{IMO}
<
\text{研究數學}
$$

這樣的簡單序列。

對廣義智能系統而言，更準確的描述是：

$$
\boxed{
\text{Mathematical Difficulty}
=
\text{Search}
\times
\text{Representation}
\times
\text{Structure}
\times
\text{Proof}
\times
\text{Meta-problem}
}
$$

這裡的乘號不是本文已證明的數值乘法關係，而表示多個相互耦合但不可簡單合併的維度。

一個真正困難的數學問題，可以不是因為候選太多，而是因為：

> 沒有人知道應該搜索什麼。

也可以不是因為證明太長，而是因為：

> 沒有人知道應該用什麼語言來表達它。

甚至不是因為原問題無法回答，而是：

> 真正的困難在於發現原問題並不是最值得回答的問題。

因此，若希望評估未來 AI 的高階數學能力，問題設計需要逐步從：

$$
\boxed{\text{Can it get the answer?}}
$$

轉向：

$$
\boxed{
\text{What kind of barrier can it recognize, transform, traverse, verify, and reconsider?}
}
$$

這將是本文所提出「數學難度譜系」的核心用途。

---

## 參考文獻與相關系統

1. Google DeepMind, **AlphaGeometry: An Olympiad-level AI system for geometry**, 2024.
2. Google DeepMind, **AI achieves silver-medal standard solving International Mathematical Olympiad problems**, 2024；頁面後續更新 AlphaProof 方法資訊。
3. Google DeepMind, **Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the International Mathematical Olympiad**, 2025.
4. Yu et al., **FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models**, 2025.
5. Huang et al., **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction**, 2025.
6. Pham et al., **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics**, 2026.
7. Ravi et al., **FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?**, 2026.
8. Epoch AI, **FrontierMath: Benchmarking AI against advanced mathematical research / Open Problems**, 2024–2026.

---

**版本：v1.0**

**系列定位：基礎分類論文。**

**下一篇：**《非適應性計算基線：二十種數學認知障礙的機械化還原》