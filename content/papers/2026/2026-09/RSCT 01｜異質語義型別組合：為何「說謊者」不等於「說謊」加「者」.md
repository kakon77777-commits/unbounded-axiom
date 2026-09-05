# RSCT 01｜異質語義型別組合：為何「說謊者」不等於「說謊」加「者」

**系列**：關係語義構成論（Relational Semantic Construction Theory, RSCT）01  
**英文題名**：*Heterogeneous Semantic Type Composition: Why “Liar” Is Not Merely “Lie” Plus “-er”*  
**作者**：Neo.K × GPT-5.6 Sol  
**機構**：EveMissLab（一言諾科技有限公司）  
**日期**：2026-08-27  
**版本**：v0.1  
**性質**：形式語義學／語言哲學／型別化語義／構造語義學／研究綱領  
**狀態**：系列正式初稿  
**前篇**：RSCT 00｜《關係語義構成論：從詞彙原子幻覺到異質語義結構》

---

## 摘要

RSCT 00 已提出：自然語言中的字、詞與表面最小單位，不應被直接視為不可再分的語義原子；語義成分可能具有不同型別，並透過型別敏感的構造規則形成新的語義物件。本篇進一步把此命題形式化，專門研究「異質語義型別組合」。

本文以「說謊者」為最小核心案例。表面字串可以寫成：

$$
\text{說謊}+\text{者},
$$

但這個「加號」不是普通代數加法，也不是純字串串接。若「說謊」首先提供一個行為／關係型語義，而「者」提供一個角色構造算子，則二者的組合更接近：

$$
L:\mathsf{ActRel},
$$

$$
\mathsf{Agentize}:\mathsf{ActRel}\rightarrow\mathsf{Role},
$$

因此：

$$
\mathsf{Agentize}(L):\mathsf{Role}.
$$

組合後所得語義型別不同於輸入型別。這表示自然語言的複合詞、片語甚至句子，不能一律被視為若干已完成意義之符號的同質拼接。

本文進一步提出五類構造關係：同型組合、異型構造、型別提升、型別限制與型別重寫；並區分「字串可拼接」與「語義可構造」。形式上，若：

$$
a:\alpha,
\qquad
b:\beta,
$$

只有在存在合法構造規則：

$$
\mathcal C_{\alpha,\beta\Rightarrow\gamma}
:
\alpha\times\beta\rightarrow\gamma
$$

時，才可寫：

$$
\mathcal C(a,b):\gamma.
$$

因此：

$$
\text{Syntactic Concatenability}
\not\Rightarrow
\text{Semantic Composability}.
$$

本文同時引入「構造軌跡」與「型別來源保留」兩個概念。語義組合若只保留最終結果 $\gamma$，而刪除其來源型別與構造算子，則後續推理可能無法區分不同生成路徑。故本文提出：

$$
\operatorname{Trace}
\left(
\mathcal C(a,b)
\right)
=
\langle
\alpha,\beta,\mathcal C,\gamma
\rangle.
$$

此結構可避免把「角色生成」誤寫成「本體身份」，亦可為後續說謊者悖論分析保留「說謊」「者」「說謊者」「陳述」「指稱」「評價」之間的型別差異。

本篇仍不處理真與假的最終本體地位，也不宣稱僅靠型別拆解即可解除說謊者悖論。本文的目標更基礎：建立一套能夠表達「不同語義類型如何合法組合、何時產生新型別、何時失敗、何時發生錯誤同一化」的最低形式核心。

**關鍵詞**：異質語義、語義型別、構造子、說謊者、角色生成、型別提升、型別重寫、語義組合、構造軌跡、關係語義構成論

---

# 0. 問題：為什麼「說謊者」不能只寫成兩個符號相加？

「說謊者」表面上可以被切成：

$$
\text{說謊}
+
\text{者}.
$$

如果只做字串處理，這完全沒有問題。

但語義分析關心的不是：

$$
\text{string}_1+\text{string}_2,
$$

而是：

> 兩個成分各自提供什麼語義作用？組合後生成的是什麼？生成結果與輸入成分是否同型？

「說謊」至少可被理解為某種行為、關係或述謂型結構：

$$
L:\mathsf{ActRel}.
$$

「者」則不是另一個與「說謊」同型的行為。它更像是一個角色生成操作：

$$
\mathsf{Agentize}:\mathsf{ActRel}\rightarrow\mathsf{Role}.
$$

所以：

$$
\mathsf{Agentize}(L):\mathsf{Role}.
$$

因此：

$$
\boxed{
\operatorname{type}(\text{說謊者})
\neq
\operatorname{type}(\text{說謊}).
}
$$

這個差異不是字面差異，而是構造差異。

---

# 1. 字串拼接與語義組合必須分開

## 1.1 字串拼接

若：

$$
s_1,s_2\in\Sigma^\ast,
$$

則字串串接可以寫成：

$$
s_1\Vert s_2.
$$

此操作只需要符號序列可被接在一起。

例如：

$$
\text{「說謊」}
\Vert
\text{「者」}
=
\text{「說謊者」}.
$$

但這只回答：

> 兩段字串能不能接？

它沒有回答：

> 接完之後的語義是什麼？

## 1.2 語義組合

令語義解譯為：

$$
\llbracket\cdot\rrbracket.
$$

則：

$$
\llbracket s_1\Vert s_2\rrbracket
$$

不必等於：

$$
\llbracket s_1\rrbracket
+
\llbracket s_2\rrbracket.
$$

更一般地，應寫成：

$$
\llbracket s_1\Vert s_2\rrbracket
=
\mathcal C
\left(
\llbracket s_1\rrbracket,
\llbracket s_2\rrbracket
\right),
$$

其中 $\mathcal C$ 是語義構造規則。

因此：

$$
\boxed{
\text{Concatenation}
\neq
\text{Semantic Construction}.
}
$$

---

# 2. RSCT 的型別判定記號

本文使用：

$$
x:\tau
$$

表示語義物件 $x$ 具有型別 $\tau$。

例如：

$$
L:\mathsf{ActRel},
$$

表示「說謊」在目前分析中被視為行為／關係型語義。

而：

$$
A:\mathsf{ActRel}\rightarrow\mathsf{Role}
$$

表示 $A$ 是一個接受行為／關係型輸入、輸出角色型語義的構造子。

因此：

$$
A(L):\mathsf{Role}.
$$

在 RSCT 中，這種型別標記不是宣稱自然語言只有唯一正確分類，而是：

> 在某一分析模型中，明確記錄一個成分被允許如何與其他成分組合。

因此型別的最低作用不是分類，而是：

$$
\boxed{
\text{限制與揭露合法構造。}
}
$$

---

# 3. 異質語義組合的最低定義

## 定義 1：異質語義組合

若：

$$
a:\alpha,
\qquad
b:\beta,
\qquad
\alpha\neq\beta,
$$

且存在一個合法構造算子：

$$
\mathcal C_{\alpha,\beta\Rightarrow\gamma}
:
\alpha\times\beta\rightarrow\gamma,
$$

則稱：

$$
\mathcal C(a,b):\gamma
$$

為一次異質語義型別組合。

異質組合的關鍵不在於輸入必然不同，而在於：

$$
\boxed{
\text{組合規則必須知道輸入型別。}
}
$$

如果完全忽略 $\alpha,\beta$，則系統無法區分：

- 角色生成；
- 性質附著；
- 關係建立；
- 狀態更新；
- 否定；
- 評價；
- 指稱；
- 量化；
- 約束。

---

# 4. 五種基本構造模式

RSCT v0.1 暫時區分五種最低構造模式。

## 4.1 同型組合

若：

$$
a,b:\alpha,
$$

且：

$$
\mathcal C:
\alpha\times\alpha\rightarrow\alpha,
$$

則輸入與輸出同型。

例如某些集合合併、證據聚合或同類關係組合可以屬於此類。

此時：

$$
\operatorname{type}(a)
=
\operatorname{type}(b)
=
\operatorname{type}(\mathcal C(a,b)).
$$

## 4.2 異型構造

若：

$$
a:\alpha,
\qquad
b:\beta,
\qquad
\alpha\neq\beta,
$$

並且：

$$
\mathcal C:
\alpha\times\beta\rightarrow\gamma,
$$

則為異型構造。

「說謊」與「者」最適合暫時放在這一類。

## 4.3 型別提升

若：

$$
a:\alpha
$$

被某構造子提升為：

$$
U(a):\beta,
$$

且：

$$
\alpha\prec\beta,
$$

其中 $\prec$ 表示某種構造層級上的提升，則稱為型別提升。

例如：

$$
\text{局部行為}
\rightarrow
\text{角色}
$$

可被理解為一次型別提升。

但：

$$
\text{角色}
\rightarrow
\text{永久身份}
$$

是否仍合法，必須另外判定，不能自動成立。

## 4.4 型別限制

若：

$$
a:\alpha
$$

進入一個帶條件的子型：

$$
a:\alpha\mid K,
$$

其中 $K$ 是限制條件，則為型別限制。

例如：

$$
\mathsf{Liar}(x\mid t,c)
$$

可以表示：

> 在時間 $t$ 、情境 $c$ 下， $x$ 滿足某個說謊者角色條件。

這不等於：

$$
\operatorname{Identity}(x)=\mathsf{Liar}.
$$

## 4.5 型別重寫

若某語義結構經組合後不只是新增條件，而是改變原本允許的操作接口，則可寫成：

$$
\mathcal R_\tau:
\alpha\Rightarrow\beta.
$$

例如：

$$
\mathsf{ActRel}
\Rightarrow
\mathsf{Role}
$$

不是只替原型別加標籤，而是改變後續可接受的語義操作。

---

# 5. 「者」作為角色構造子

「者」在中文中常把某種行為、性質、立場或狀態轉換成角色指稱。

例如：

$$
\text{觀察}\rightarrow\text{觀察者},
$$

$$
\text{研究}\rightarrow\text{研究者},
$$

$$
\text{說謊}\rightarrow\text{說謊者}.
$$

RSCT 不主張所有「者」都只有單一語義，但可以先建立最小構造：

$$
\mathsf{Agentize}:
\mathsf{PredicateLike}
\rightarrow
\mathsf{Role}.
$$

其中：

$$
\mathsf{PredicateLike}
$$

可以包含行為、關係、性質或其他可對存在作角色綁定的結構。

因此：

$$
\mathsf{Agentize}(L)
=
\mathsf{LiarRole}.
$$

注意：

$$
\mathsf{LiarRole}
$$

首先是角色型，而不是存在本體。

所以：

$$
\boxed{
\mathsf{Role}
\neq
\mathsf{Identity}.
}
$$

若後續系統又施加：

$$
\mathsf{Reify}:
\mathsf{Role}\rightarrow\mathsf{Identity},
$$

那是第二次獨立構造。

於是完整鏈可能是：

$$
\mathsf{ActRel}
\xrightarrow{\mathsf{Agentize}}
\mathsf{Role}
\xrightarrow{\mathsf{Reify}}
\mathsf{Identity}.
$$

這與「角色本體化」問題直接相連。

---

# 6. 構造結果不能抹除來源

若系統只保留：

$$
\mathsf{LiarRole},
$$

而刪除它是如何生成的，則後續可能失去重要資訊。

因此本文定義：

## 定義 2：構造軌跡

對：

$$
y=\mathcal C(a,b),
$$

定義：

$$
\operatorname{Trace}(y)
=
\langle
a:\alpha,
b:\beta,
\mathcal C,
y:\gamma
\rangle.
$$

若是多步構造：

$$
x_0
\xrightarrow{\mathcal C_1}
x_1
\xrightarrow{\mathcal C_2}
x_2
\rightarrow\cdots
\xrightarrow{\mathcal C_n}
x_n,
$$

則：

$$
\operatorname{Trace}(x_n)
=
\langle
x_0,\mathcal C_1,x_1,\ldots,\mathcal C_n,x_n
\rangle.
$$

這使系統可以回答：

> 一個語義物件是什麼？

以及：

> 它是怎麼生成的？

兩者不能混為一談。

---

# 7. 來源同一與結果同一不是同一件事

可能存在：

$$
x\neq y,
$$

但：

$$
\mathcal C_1(x)
=
\mathcal C_2(y)
=
z.
$$

因此：

$$
\text{Same Output}
\not\Rightarrow
\text{Same Construction History}.
$$

反過來，也可能：

$$
x=y
$$

但在不同構造規則下得到：

$$
\mathcal C_1(x)\neq\mathcal C_2(x).
$$

所以：

$$
\boxed{
\text{語義同一性至少要區分對象同一、型別同一、構造同一與結果同一。}
}
$$

這對後續說謊者悖論非常重要，因為「這句話」可能指向相同字串，卻不代表：

- 相同命題內容；
- 相同評價對象；
- 相同語義層級；
- 相同構造歷史。

---

# 8. 語義構造不是必然交換的

普通加法常滿足：

$$
a+b=b+a.
$$

但語義構造通常不能預設交換律。

若：

$$
\mathcal C(a,b)
$$

表示「先由 $a$ 提供語義核心，再由 $b$ 進行角色構造」，則：

$$
\mathcal C(a,b)
\neq
\mathcal C(b,a)
$$

通常是允許甚至預期的。

因此：

$$
\boxed{
\text{Semantic Composition}
\not\Rightarrow
\text{Commutativity}.
}
$$

同樣地，也不能預設結合律：

$$
\mathcal C(\mathcal C(a,b),c)
=
\mathcal C(a,\mathcal C(b,c)).
$$

在自然語言中，不同括號位置可能生成不同型別與不同作用結構。

所以：

$$
\boxed{
\text{構造順序本身就是語義。}
}
$$

---

# 9. 型別錯誤的第一種來源：錯誤套用構造子

若：

$$
\mathcal C:
\alpha\rightarrow\beta,
$$

但實際輸入：

$$
x:\gamma,
\qquad
\gamma\neq\alpha,
$$

則：

$$
\mathcal C(x)
$$

可能是未定義的。

記作：

$$
\mathcal C(x)\uparrow
$$

表示構造失敗。

自然語言中，人類有時可以透過隱喻、轉喻、語境修復或類型提升重新解釋，但這表示系統執行了額外操作，而不是原構造天然合法。

因此應區分：

$$
\text{Directly Well-Typed}
$$

與：

$$
\text{Coerced / Reinterpreted}.
$$

---

# 10. 型別錯誤的第二種來源：錯誤同一化

比非法輸入更危險的，是把不同型別物件視為同一物件。

若：

$$
x:\alpha,
$$

$$
y:\beta,
$$

且：

$$
\alpha\neq\beta,
$$

卻直接寫：

$$
x\equiv y,
$$

則可能產生：

$$
\boxed{
\text{Type Collapse}.
}
$$

例如：

$$
\text{「假」作為被提及的語義符號}
$$

與：

$$
\text{「整句被評價為假」}
$$

即使使用相同字形：

$$
\text{假},
$$

也不必是同一型別。

後續 RSCT 05–06 將專門處理此問題。

---

# 11. 型別錯誤的第三種來源：角色被本體化

若：

$$
R(x,y,t,c)
$$

經語義構造得到：

$$
\mathsf{Role}_R(x\mid y,t,c),
$$

這可以是合法角色表示。

但若再把它壓成：

$$
\operatorname{Identity}(x)
=
\mathsf{Role}_R,
$$

並用此身份排斥其他狀態，則發生角色本體化。

所以：

$$
\boxed{
\text{合法型別提升}
\not\Rightarrow
\text{合法本體化}.
}
$$

這一點與前置論文《從關係世界到型別錯誤》的結論一致，但本篇將錯誤定位得更前：本體化可以被視為一個未經授權的高階型別構造。

---

# 12. 說謊者的最低構造圖

現在只分析「說謊者」這個詞，不處理整個悖論句。

令：

$$
L:\mathsf{ActRel},
$$

令：

$$
A:\mathsf{ActRel}\rightarrow\mathsf{Role}.
$$

則：

$$
A(L)=\mathsf{LiarRole}.
$$

構造圖：

$$
\boxed{
L:\mathsf{ActRel}
\xrightarrow{A}
\mathsf{LiarRole}:\mathsf{Role}
}
$$

若再針對某個存在 $x$：

$$
\mathsf{Bind}:
\mathsf{Role}\times\mathsf{Entity}
\rightarrow
\mathsf{RoleAssignment},
$$

則：

$$
\mathsf{Bind}
(
\mathsf{LiarRole},
x
)
=
\mathsf{Liar}(x).
$$

如果再加入時間、語境：

$$
\mathsf{Liar}(x\mid t,c).
$$

因此完整最低鏈可以寫為：

$$
\boxed{
\text{說謊}
\rightarrow
\text{說謊者角色}
\rightarrow
\text{某存在在特定條件下承擔該角色}
}
$$

而不是一開始就寫：

$$
x=\text{說謊者}.
$$

---

# 13. 從「說謊者」到「說謊者悖論」還缺很多型別

「說謊者悖論」並不是：

$$
\mathsf{LiarRole}
+
\mathsf{Paradox}
$$

這麼簡單。

至少還會涉及：

$$
\mathsf{Sentence},
$$

$$
\mathsf{Reference},
$$

$$
\mathsf{Proposition},
$$

$$
\mathsf{Evaluation},
$$

$$
\mathsf{Negation},
$$

$$
\mathsf{TruthLabel},
$$

以及自我指涉所需的回返結構。

因此，RSCT 將拒絕直接把：

> 這句話是假的

壓成：

$$
L\leftrightarrow\neg L
$$

而不保存中間型別。

後續最少需要一條：

$$
\mathsf{SentenceToken}
\rightarrow
\mathsf{ReferenceTarget}
\rightarrow
\mathsf{PropositionalContent}
\rightarrow
\mathsf{EvaluationTarget}
\rightarrow
\mathsf{EvaluationRelation}.
$$

只有在這些構造都被明確建立後，才能知道：

$$
L\leftrightarrow\neg L
$$

究竟是忠實表示，還是投影後的結果。

---

# 14. 構造與投影必須分開

RSCT 00 已提出：

$$
\mathcal W
\xrightarrow{R}
\mathcal G
\xrightarrow{\Pi_0}
\Sigma_T
\xrightarrow{\mathcal C}
\mathcal S
\xrightarrow{\Pi_1}
P
\xrightarrow{\mathcal E}
V.
$$

本篇專門細化：

$$
\mathcal C.
$$

其中：

$$
\mathcal C
\neq
\Pi_1.
$$

前者回答：

> 語義結構如何被生成？

後者回答：

> 已生成的語義結構如何被壓縮成某個命題表示？

如果把兩者合併，可能會出現：

$$
\mathcal C(a,b)
\mapsto
P
$$

卻不再知道：

$$
a:\alpha,
\qquad
b:\beta,
\qquad
\mathcal C:\alpha\times\beta\rightarrow\gamma.
$$

所以：

$$
\boxed{
\text{Construction Loss}
\neq
\text{Projection Loss},
}
$$

但兩者可以連鎖發生。

---

# 15. 異質語義構造的最低公理候選

本篇提出以下候選公理，供後續系列修正。

## 公理候選 A1：型別顯式性

任何被 RSCT 視為正式構造單位的語義物件，必須至少能在局部模型中指定一個工作型別：

$$
x:\tau.
$$

## 公理候選 A2：構造可追溯性

對任何正式組合：

$$
y=\mathcal C(x_1,\ldots,x_n),
$$

必須能保留：

$$
\operatorname{Trace}(y).
$$

## 公理候選 A3：非自動同一化

若：

$$
x:\alpha,
\qquad
y:\beta,
$$

則：

$$
x\equiv y
$$

不能只因字形、名稱或表面指稱相同而成立。

## 公理候選 A4：結果型別不預設等於輸入型別

允許：

$$
\gamma\neq\alpha,
\qquad
\gamma\neq\beta.
$$

## 公理候選 A5：投影後不可反推完整構造

若：

$$
\Pi_1(s_1)=\Pi_1(s_2),
$$

但：

$$
s_1\neq s_2,
$$

則不能僅由投影結果唯一恢復原構造歷史。

---

# 16. 對傳統組合原則的態度

RSCT 不否認組合性原則。

相反地，它接受一個更弱而更精確的版本：

> 複合語義可以由成分、其型別、構造規則、順序、語境與必要的型別轉換共同決定。

形式上：

$$
\llbracket E\rrbracket
=
F
\left(
\llbracket e_1\rrbracket,
\ldots,
\llbracket e_n\rrbracket,
\tau_1,\ldots,\tau_n,
\mathcal C,
c
\right).
$$

而不是只寫：

$$
\llbracket E\rrbracket
=
F
\left(
\llbracket e_1\rrbracket,
\ldots,
\llbracket e_n\rrbracket
\right).
$$

因此 RSCT 並非反組合，而是：

$$
\boxed{
\text{反對無型別、無構造歷史的過度簡化組合。}
}
$$

---

# 17. 可檢驗性與失敗條件

本篇至少有以下失敗條件。

第一，若「說謊」「者」「說謊者」等案例在實際語義分析中不需要任何型別差異，就能無損保留所有推論能力，則本文的異質型別需求被削弱。

第二，若構造軌跡：

$$
\operatorname{Trace}(x)
$$

在任何後續推理、歧義辨識、錯誤定位與模型實作中都沒有額外價值，則其工程必要性不足。

第三，若自然語言中大量複合結構必須依賴如此多型別，卻無法形成可重用的少量構造規則，則 RSCT 可能只是把語言複雜度重新命名，而未提供更好模型。

第四，即使型別拆分成功，說謊者悖論仍可能在更高階關係上重新出現。因此：

$$
\boxed{
\text{Type Decomposition}
\not\Rightarrow
\text{Paradox Resolution}.
}
$$

本篇只建立分析前提，不提前宣稱解決結果。

---

# 18. 與後續 RSCT 02 的接口

本篇已經出現：

$$
\mathsf{Agentize},
$$

$$
\mathsf{Bind},
$$

$$
\mathcal C,
$$

$$
\mathcal R_\tau.
$$

這些表面上都是名詞或數學符號，但它們其實具有：

- 生成；
- 綁定；
- 轉換；
- 限制；
- 重寫；

等作用。

因此下一篇將正式處理：

$$
\boxed{
\text{為什麼形式結構可以在沒有詞法動詞的情況下具有動詞性？}
}
$$

也就是：

> RSCT 02｜《沒有動詞的動詞性：形式構造如何生成作用、方向與過程》。

---

# 19. 核心命題收斂

本篇可濃縮為六條核心命題。

### 命題 1

$$
\boxed{
\text{Syntactic Concatenability}
\not\Rightarrow
\text{Semantic Composability}.
}
$$

### 命題 2

$$
\boxed{
\text{語義組合可以改變型別。}
}
$$

### 命題 3

$$
\boxed{
\text{Role Construction}
\neq
\text{Identity Reification}.
}
$$

### 命題 4

$$
\boxed{
\text{Same Surface Form}
\not\Rightarrow
\text{Same Semantic Type}.
}
$$

### 命題 5

$$
\boxed{
\text{Same Output}
\not\Rightarrow
\text{Same Construction Trace}.
}
$$

### 命題 6

$$
\boxed{
\text{構造順序、型別與構造子本身都是語義的一部分。}
}
$$

---

# 20. 結論

「說謊者」之所以不是「說謊」與「者」的普通相加，不是因為這兩個字特別神祕，而是因為自然語言的複合結構本來就可能跨越不同語義型別。

「說謊」可以提供一種行為／關係型語義；「者」可以執行角色生成；生成後的「說謊者」則成為另一種可被綁定、指稱、限制與後續判定的角色型物件。

因此：

$$
\text{說謊}
\rightarrow
\text{說謊者}
$$

不是：

$$
x\rightarrow x,
$$

而更像：

$$
\alpha
\xrightarrow{\mathcal C}
\beta.
$$

若語言邏輯一開始就把這些差異全部壓成同一類符號，再直接進入命題求值，就可能在真正的邏輯計算開始以前，已經失去型別、來源、方向與構造歷史。

RSCT 因此主張：

$$
\boxed{
\text{先問「它是怎麼被構造出來的」，再問「它是真是假」。}
}
$$

這不是拒絕邏輯，而是把邏輯所依賴的語義輸入重新打開。

下一篇將把本篇已經隱含存在的「作用」本身抽出來，研究一個更底層的問題：

$$
\boxed{
\text{當公式沒有動詞時，為什麼它仍然可以在做事？}
}
$$
