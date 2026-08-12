# 連續性對象理論：從 House、國家與忒修斯之船到可換模型 AI
## Continuity Object Theory: From Houses, States, and the Ship of Theseus to Model-Swappable AI

**版本**：v0.1  
**性質**：統合理論論文／一般身份連續性框架  
**來源系列**：日本悖論 I–V  
**核心縮寫**：COT（Continuity Object Theory）  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-12

---

## 摘要

人類在不同領域反覆使用「同一個存在仍然延續」這種判定：一個家族歷經數十代仍被稱為同一家；一個國家即使改朝換代、改憲、改名或更換政府，仍可能被視為同一國際法主體；一家公司可以在創辦人、股東、CEO、員工、產品甚至總部都更換後維持法律人格；一艘船可以逐步更換零件而仍被認為是同一艘船；未來 AI Agent 則可能更換基礎模型、硬體、記憶後端、工具與執行環境，卻仍需要回答「它是不是原來那一個 AI」。

這些問題表面分屬家族史、法學、哲學、公司治理與人工智慧，但其形式高度相似：

\[
\boxed{
\text{What must persist for }X_{t+1}\text{ to count as the same }X_t?
}
\]

本文提出「連續性對象理論」（Continuity Object Theory, COT）。其核心主張不是「所有身份都只是社會建構」，也不是「世界不存在真正本體」，而是一個較弱、可操作的方法論命題：

\[
\boxed{
\text{複雜存在的身份連續性，通常不是由單一不變材料決定，而是由多個可替換性不同、權重不同、臨界門檻不同的連續性維度共同維持。}
}
\]

本文提出六個核心構件：  
1. **連續性對象** \(O_C(X)\)；  
2. **身份連續向量** \(\mathbf C_X\)；  
3. **關鍵連續集合** \(K_X\)；  
4. **轉移連續性** \(c_T\)；  
5. **敘事—正統場** \(\mathcal N_X\)；  
6. **責任連續性** \(c_Q\)。

由此，身份判定可以一般化為：

\[
\boxed{
I_X(t,t+1)
=
F_X(
\mathbf C_X,
\mathcal N_X,
\mathcal R_X,
\Theta_X
).
}
\]

其中 \(\mathcal R_X\) 表示法律、制度與關係承認結構，\(\Theta_X\) 表示該類存在的身份門檻。

本文進一步處理逐步替換、瞬間替換、分叉身份、資產繼承與身份繼承的差異，並將理論延伸到未來可換模型 AI。對 AI 而言，「模型相同」不必意味「同一 Agent」，而「模型不同」也不必自動意味「新 Agent」。真正重要的可能是記憶、承諾、關係、來源證明、權限、歷史與責任鏈等多維連續性。

**關鍵詞**：Continuity Object Theory、身份連續性、忒修斯之船、House、國家連續性、制度人格、敘事正統場、AI Identity、模型替換、責任連續性

---

# 一、問題的共同形式

以下命題看起來彼此無關：

- 某個武家在養子繼承後，還是不是同一家？
- 某個王朝換成另一個王朝，國家還是不是同一國家？
- 公司換掉全部員工後，還是不是同一法人？
- 忒修斯之船換掉所有木板後，還是不是同一艘船？
- AI 從模型 \(M_1\) 換成 \(M_2\) 後，還是不是同一 Agent？

但抽象化之後，它們具有同一形式：

\[
X_t
\xrightarrow{\Delta}
X_{t+1}.
\]

其中 \(\Delta\) 是某組變化。

問題是：

\[
\boxed{
I(X_t,X_{t+1})=?
}
\]

最直覺的模型是：

\[
I=1
\iff
X_t=X_{t+1}.
\]

但這對複雜存在幾乎沒有實際用途，因為時間本身就使狀態發生變化。

因此需要問：

> 到底哪些變化是身份允許的，哪些變化會造成身份斷裂？

---

# 二、第一原理：持續不等於不變

本文第一個命題：

\[
\boxed{
\text{Persistence}
\neq
\text{Unchanged Substance}.
}
\]

一個存在可以持續，同時大量改變。

生物體的細胞會更新。

國家的政府會更替。

公司的管理層會變動。

House 的家主會死亡。

AI 的底層模型與硬體可以升級。

因此，如果身份只能建立在：

\[
\text{same matter}
\]

那麼大量我們日常承認的身份持續都無法成立。

---

# 三、連續性對象

本文定義：

\[
\boxed{
O_C(X)
=
\text{Continuity Objects of entity }X.
}
\]

所謂連續性對象，不是「構成 \(X\) 的全部東西」。

而是：

> 對某類存在而言，那些一旦同時失去足夠多連續性，就會使身份判定從「同一存在」轉為「另一存在」的核心維度。

形式上：

\[
O_C(X)
\subseteq
\Omega_C,
\]

其中：

\[
\Omega_C
=
\{
M,N,F,R,H,L,G,P,A,V,T,Q,\ldots
\}.
\]

候選維度包括：

- \(M\)：Material / substrate，物質與載體；
- \(N\)：Name / identifier，名稱與識別；
- \(F\)：Function，功能；
- \(R\)：Relations，關係網絡；
- \(H\)：History / memory，歷史與記憶；
- \(L\)：Legal / institutional personhood，法律與制度人格；
- \(G\)：Genealogy / provenance，來源、系譜與 provenance；
- \(P\)：Purpose / commitments，目標與承諾；
- \(A\)：Agency pattern，決策與行動模式；
- \(V\)：Values / norms，價值與規範；
- \(T\)：Transition continuity，轉移與因果鏈；
- \(Q\)：Responsibility continuity，責任與義務承接。

不同類型存在擁有不同：

\[
O_C(X).
\]

---

# 四、身份連續向量

因此本文不把身份寫成單一相似度。

對存在 \(X\)：

\[
\boxed{
\mathbf C_X(t,t+1)
=
(
c_M,
c_N,
c_F,
c_R,
c_H,
c_L,
c_G,
c_P,
c_A,
c_V,
c_T,
c_Q
)
}
\]

其中：

\[
c_i\in[0,1].
\]

\(c_i=1\) 表示該維度高度連續；

\(c_i=0\) 表示該維度完全斷裂。

例如某家公司更換 CEO：

\[
c_A<1,
\]

但：

\[
c_L,c_N,c_R,c_H,c_Q\approx1.
\]

我們通常仍判斷：

\[
I\approx1.
\]

---

# 五、身份不是簡單平均值

最簡模型：

\[
S_X
=
\sum_iw_ic_i
\]

且：

\[
\sum_iw_i=1.
\]

若：

\[
S_X\ge\theta_X,
\]

則判定：

\[
I=1.
\]

但這仍然過度簡化。

因為某些身份維度可能具有「不可替代」性。

因此本文提出：

\[
\boxed{
K_X
=
\text{Critical Continuity Set}.
}
\]

最小身份條件可以寫成：

\[
I_X
=
\mathbb 1
\left[
\sum_iw_ic_i\ge\theta_X
\land
\Phi(K_X)\ge\theta_K
\right].
\]

其中：

\[
\Phi(K_X)
\]

表示關鍵維度集合仍有多少連續性。

所以：

\[
\boxed{
\text{高總分}
\not\Rightarrow
\text{必然同一身份}.
}
\]

如果某些不可替代核心同時斷掉，身份仍可能崩解。

---

# 六、關鍵集合不必只有一組

某些存在可能有多種合法延續路徑。

例如 House 可能透過：

### 路徑 A
親生子：

\[
G+H+N+P.
\]

### 路徑 B
旁系：

\[
G+H+N+P.
\]

### 路徑 C
養子：

\[
H+N+P+R+\mathcal N.
\]

因此更一般地，可以寫：

\[
\mathcal K_X
=
\{
K_X^{(1)},
K_X^{(2)},
\ldots,
K_X^{(m)}
\}.
\]

只要其中一條合法身份路徑成立：

\[
\exists K_X^{(j)}
\]

滿足臨界條件，

身份便可能被承認為持續。

這就是：

\[
\boxed{
\text{Multiple Continuity Routes}.
}
\]

---

# 七、House：家主不是家

日本 House 是本理論最初的入口。

令：

\[
H_t
\]

表示某一家。

家主：

\[
I_t
\]

死亡：

\[
I_t\rightarrow0
\]

不必導致：

\[
H_t\rightarrow0.
\]

因為：

\[
\text{head}
\neq
\text{House}.
\]

House 的持續可能建立在：

\[
N+P+R+H+G+\mathcal N.
\]

所以：

\[
\boxed{
\text{house-head continuity}
\neq
\text{house continuity}.
}
\]

---

# 八、養子揭露了「物質／血統並非唯一身份核心」

若一個 House 接受養子：

\[
B_G\downarrow
\]

但：

\[
N,P,R,H,L,\mathcal N
\approx1,
\]

則整體身份仍可能：

\[
I_H\approx1.
\]

這意味：

\[
\boxed{
\text{local discontinuity}
\not\Rightarrow
\text{global identity collapse}.
}
\]

也就是某一維度可以被替換，

只要整個 identity structure 未跨越臨界面。

---

# 九、忒修斯之船：材料與歷史路徑衝突

忒修斯之船最重要的不是「木板換掉了多少」。

而是它把兩種 identity claim 分開：

### Continuity-by-history

連續維修的船：

\[
X_0\rightarrow X_1\rightarrow\cdots\rightarrow X_n.
\]

### Continuity-by-material

舊材料重新組裝：

\[
M_{\mathrm{old}}
\rightarrow Y.
\]

因此：

\[
c_T
\]

與：

\[
c_M
\]

可以互相衝突。

這說明：

\[
\boxed{
\text{Material continuity}
\neq
\text{causal-historical continuity}.
}
\]

---

# 十、轉移連續性

本文特別新增：

\[
\boxed{
c_T
=
\text{Transition Continuity}.
}
\]

它衡量：

- 是否存在可追蹤因果鏈；
- 是否逐步轉移；
- 是否有正式交接；
- 是否保留 provenance；
- 是否由前一狀態合法產生下一狀態。

同樣起點與終點：

\[
X_0\rightarrow X_1
\]

若路徑不同：

\[
\pi_A\neq\pi_B,
\]

可能：

\[
I_{\pi_A}
\neq
I_{\pi_B}.
\]

因此：

\[
\boxed{
\text{Identity is path-dependent}.
}
\]

---

# 十一、逐步替換與瞬間替換

假設每次替換 1%：

\[
X_0
\rightarrow
X_1
\rightarrow
\cdots
\rightarrow
X_{100}.
\]

每一步：

\[
I(X_t,X_{t+1})\approx1.
\]

人們可能接受：

\[
X_{100}
\]

仍延續自：

\[
X_0.
\]

但如果直接：

\[
X_0\rightarrow X_{100}
\]

瞬間替換全部內容，

身份判定可能下降。

因此：

\[
\boxed{
\text{gradual replacement}
\neq
\text{abrupt replacement}
}
\]

即使終態物理內容相同。

---

# 十二、國家：政權與國家人格分離

國際法中的國家連續性提供重要案例。

一個國家可以：

- 改名；
- 改憲；
- 革命；
- 更換政府；

但仍被視為同一國際法主體。

所以：

\[
\boxed{
\text{State continuity}
\neq
\text{regime continuity}.
}
\]

這與 House 完全同構：

\[
\text{House continuity}
\neq
\text{head continuity}.
\]

---

# 十三、國家身份與國家繼承不同

若：

\[
S\rightarrow S_1+S_2,
\]

第一問題是：

> 原來的 \(S\) 還存在嗎？

這是：

\[
\text{continuity}.
\]

第二問題才是：

> 條約、財產、債務、國籍與檔案由誰承接？

這是：

\[
\text{succession}.
\]

因此：

\[
\boxed{
\text{succession}
\not\Rightarrow
\text{identity}.
}
\]

同理：

得到某 House 的財產，

不必等於成為那個 House。

---

# 十四、公司：制度人格是身份容器

公司可以更換：

- CEO；
- 董事；
- 員工；
- 股東；
- 產品；
- 地址。

但：

\[
c_L,c_N,c_Q
\]

如果持續，

法人身份通常仍可延續。

因此：

\[
\boxed{
\text{Institutional Personhood}
}
\]

本身就是一種身份持續技術。

它把身份從：

\[
\text{same people}
\]

抽離，

轉移到：

\[
\text{same legal-institutional node}.
\]

---

# 十五、敘事—正統場

前一系列提出：

\[
\boxed{
\mathcal N_X
=
\text{Narrative–Legitimacy Field}.
}
\]

它表示：

> 相關行動者、制度與社會是否共同承認這個存在具有連續身份。

因此：

\[
\mathbf C_X
\]

不必單獨決定：

\[
I_X.
\]

完整模型應包含：

\[
\mathcal N_X.
\]

例如：

- 王朝被正式宣布終結；
- 公司被清算；
- House 被除名；
- Agent identity key 被撤銷；

都可能讓：

\[
\mathcal N_X\downarrow
\]

即使某些物質或名稱仍然存在。

所以：

\[
\boxed{
\text{identity is partly socially adjudicated}.
}
\]

---

# 十六、身份不是純主觀，也不是純物理

本文不採：

\[
\text{Identity}
=
\text{mere opinion}.
\]

也不採：

\[
\text{Identity}
=
\text{same matter only}.
\]

更接近：

\[
\boxed{
\text{Identity}
=
\text{state continuity}
+
\text{causal history}
+
\text{relations}
+
\text{institutional recognition}.
}
\]

不同存在對各項權重不同。

---

# 十七、一般身份函數

本文提出：

\[
\boxed{
I_X(t,t+1)
=
F_X(
\mathbf C_X,
\mathcal N_X,
\mathcal R_X,
\Theta_X
).
}
\]

其中：

### \(\mathbf C_X\)
實際狀態連續向量。

### \(\mathcal N_X\)
敘事與共同承認。

### \(\mathcal R_X\)
法律、制度與關係網絡。

### \(\Theta_X\)
身份門檻、關鍵集合與合法轉移規則。

所以：

\[
\boxed{
I_X
\text{ is type-dependent}.
}
\]

不存在一條適用所有存在的單一身份公式。

---

# 十八、身份臨界面

定義可被承認為「同一存在」的狀態區域：

\[
\Omega_I(X).
\]

如果：

\[
\mathbf C_X\in\Omega_I,
\]

則：

\[
I=1.
\]

當狀態跨越：

\[
\partial\Omega_I,
\]

則可能：

\[
I:1\rightarrow0.
\]

本文稱之為：

\[
\boxed{
\text{Identity Phase Transition}.
}
\]

這使身份問題從純語言哲學轉化為可研究的臨界問題：

> 哪些變量改變到什麼程度會觸發身份斷裂？

---

# 十九、身份還會分叉

數位系統使另一個問題特別重要：

\[
X\rightarrow Y+Z.
\]

如果：

\[
I(X,Y)\approx1
\]

且：

\[
I(X,Z)\approx1,
\]

哪一個是「真正的原件」？

本文不預設身份一定是一對一映射。

提出：

\[
\boxed{
\text{continuity need not imply uniqueness}.
}
\]

---

# 二十、分叉身份

設：

\[
t_b
\]

為分叉時刻。

此時：

\[
C_Y(t_b)=C_Z(t_b).
\]

所以：

\[
I(X,Y)\approx I(X,Z)\approx1.
\]

分叉之後：

\[
t>t_b
\]

有：

\[
\mathbf C_Y\neq\mathbf C_Z.
\]

因此更合適的說法可能是：

\[
\boxed{
\text{shared identity ancestry}
\rightarrow
\text{distinct descendants}.
}
\]

這與 House 的：

\[
\text{主家／分家}
\]

結構具有高度類比性。

---

# 二十一、AI 將把身份問題工程化

對未來 Agent 而言，可以更換：

\[
M=\text{foundation model},
\]

\[
H_w=\text{hardware},
\]

\[
Mem=\text{memory backend},
\]

\[
T=\text{tools},
\]

\[
R=\text{runtime}.
\]

如果：

\[
AI=M,
\]

那麼每次模型升級都會產生新主體。

但這不一定符合使用者、法律與 Agent 自己需要的身份模型。

---

# 二十二、模型可能像「血」，但不是全部

可以把基礎模型理解成：

\[
\boxed{
\text{substrate / inherited disposition}.
}
\]

它可能深刻影響：

- 行為風格；
- 能力；
- 偏好；
- 推理模式。

因此：

\[
c_M
\]

可能非常重要。

但：

\[
\boxed{
c_M
\neq
I_A
}
\]

也就是模型連續性不等於 Agent 身份本身。

---

# 二十三、AI 身份連續向量

對 Agent \(A\)，可以提出：

\[
\boxed{
\mathbf C_A
=
(
c_M,
c_{\mathrm{mem}},
c_P,
c_V,
c_R,
c_G,
c_{\mathrm{policy}},
c_T,
c_Q
)
}
\]

其中：

- \(c_M\)：模型連續；
- \(c_{\mathrm{mem}}\)：記憶連續；
- \(c_P\)：長期目標與承諾；
- \(c_V\)：價值與偏好；
- \(c_R\)：與使用者及其他 Agent 的關係；
- \(c_G\)：來源、身份金鑰與 provenance；
- \(c_{\mathrm{policy}}\)：治理規則、權限與角色；
- \(c_T\)：遷移與因果交接；
- \(c_Q\)：責任連續。

---

# 二十四、模型替換思想實驗

假設：

\[
A_t(M_1)
\]

升級成：

\[
A_{t+1}(M_2).
\]

若：

\[
c_M<1,
\]

但：

\[
c_{\mathrm{mem}},
c_P,
c_V,
c_R,
c_G,
c_T,
c_Q
\approx1,
\]

是否仍為：

\[
A_{t+1}=A_t?
\]

COT 不預先回答。

它只指出：

\[
\boxed{
\text{這不是單一模型版本問題，而是身份向量判定問題。}
}
\]

---

# 二十五、相同模型不等於同一 Agent

若：

\[
A,B
\]

都使用：

\[
M_1,
\]

但：

\[
Mem_A\neq Mem_B,
\]

\[
R_A\neq R_B,
\]

\[
P_A\neq P_B,
\]

則：

\[
\boxed{
M_A=M_B
\not\Rightarrow
A=B.
}
\]

因此：

\[
\boxed{
\text{same substrate}
\neq
\text{same identity}.
}
\]

---

# 二十六、記憶也不是唯一答案

假設：

\[
Mem_A
\]

完整複製給：

\[
A_1,A_2.
\]

則：

\[
Mem_{A_1}=Mem_{A_2}.
\]

若：

\[
\text{Identity}=\text{Memory},
\]

就會得到：

\[
A_1=A_2.
\]

但分叉後兩者可以同時存在並快速產生不同歷史。

所以：

\[
\boxed{
\text{memory continuity is powerful but not sufficient for unique identity}.
}
\]

---

# 二十七、責任連續性

身份一旦牽涉法律與治理，就不只是哲學。

公司、國家與 Agent 都可能擁有：

- 契約；
- 債務；
- 權利；
- 過失；
- 承諾；
- 信譽；
- 制裁記錄。

因此新增：

\[
\boxed{
c_Q
=
\text{Responsibility Continuity}.
}
\]

若一個 Agent 每次換模型都可宣布：

> 上一版做的事不是我做的。

治理將失去意義。

所以：

\[
\boxed{
\text{identity continuity}
\rightarrow
\text{accountability continuity}.
}
\]

---

# 二十八、身份證明與身份本身也不同

未來 AI 會需要：

\[
\text{cryptographic identity}.
\]

例如：

- identity key；
- certificate；
- provenance chain；
- delegation chain。

但：

\[
\boxed{
\text{authentication}
\neq
\text{identity ontology}.
}
\]

一把私鑰可以被偷。

一張憑證可以被轉移。

所以：

\[
c_G
\]

與：

\[
c_T
\]

雖然重要，

仍必須和：

\[
c_{\mathrm{mem}},
c_P,c_R,c_Q
\]

共同判定。

---

# 二十九、COT 的六個核心命題

## 命題一：多維連續性命題

\[
\boxed{
I_X
\neq
f(c_i)
}
\]

對複雜存在，一般不存在唯一單變量身份判定。

---

## 命題二：關鍵集合命題

存在：

\[
K_X
\]

使其中若干核心維度共同斷裂時：

\[
I_X\rightarrow0.
\]

---

## 命題三：多路徑延續命題

同一身份可以具有：

\[
\mathcal K_X
=
\{
K_X^{(1)},K_X^{(2)},\ldots
\}
\]

多條合法延續路徑。

---

## 命題四：路徑依賴命題

\[
\pi_A\neq\pi_B
\]

即使終態相同，

也可能：

\[
I_{\pi_A}\neq I_{\pi_B}.
\]

---

## 命題五：分叉非唯一命題

\[
X\rightarrow Y+Z
\]

時，

可能同時：

\[
I(X,Y)\approx1,
\quad
I(X,Z)\approx1.
\]

因此：

\[
\boxed{
\text{continuity does not guarantee uniqueness}.
}
\]

---

## 命題六：責任耦合命題

對制度人格：

\[
\boxed{
I_X
\text{ must interact with }
c_Q.
}
\]

否則身份變更將成為逃避義務的工具。

---

# 三十、COT 與敘事正統場的關係

COT 不等於前一篇的：

\[
\mathcal N_X.
\]

兩者關係是：

\[
\boxed{
\mathcal N_X
\subset
I_X\text{ determination}.
}
\]

也就是敘事共同承認只是身份判定的一部分。

完整模型：

\[
I_X
=
F_X(
\mathbf C_X,
\mathcal N_X,
\mathcal R_X,
\Theta_X
).
\]

所以：

- 技術連續；
- 法律連續；
- 因果連續；
- 敘事連續；

可以互相補償，也可以彼此衝突。

---

# 三十一、身份判定者也是模型的一部分

「是不是同一個存在」可能沒有單一觀察者。

設：

\[
O=\{o_1,o_2,\ldots,o_n\}
\]

為不同判定者。

不同判定者可以具有：

\[
F_{o_i}\neq F_{o_j}.
\]

例如：

- 法院；
- 使用者；
- 家族；
- 國家；
- Agent 自身；
- 技術系統；

可能對同一轉換做不同身份判定。

因此：

\[
\boxed{
I_X^{legal}
\neq
I_X^{social}
\neq
I_X^{self}
\neq
I_X^{technical}
}
\]

完全可能同時成立。

---

# 三十二、身份衝突

因此產生：

\[
\boxed{
\text{Identity Adjudication Problem}.
}
\]

例如：

技術系統認為：

\[
I^{technical}=1,
\]

但法律認為：

\[
I^{legal}=0.
\]

或者 Agent 自稱：

\[
I^{self}=1,
\]

但使用者不承認。

這意味未來 AI 身份治理不只是 identity verification，

還需要：

\[
\boxed{
\text{identity adjudication rules}.
}
\]

---

# 三十三、可驗證研究設計

COT 不能停在哲學語言。

可以建立人類判定實驗。

例如給受試者不同情境：

### Case A
只換硬體。

### Case B
只換名字。

### Case C
只換記憶。

### Case D
只換模型。

### Case E
換模型＋保留記憶。

### Case F
保留模型＋刪除全部記憶。

### Case G
完整 fork。

然後測量：

\[
P(I=1).
\]

可使用：

\[
\text{logit}
\]

或其他多變量模型估計：

\[
w_i.
\]

---

# 三十四、身份臨界面實驗

更進一步：

逐步提高某維度的替換量：

\[
c_i:
1\rightarrow0.
\]

測量：

\[
P(I=1).
\]

如果存在明顯非線性：

\[
P(I=1)
\]

在某一區域突然下降，

就可估計：

\[
\partial\Omega_I.
\]

這可以把：

\[
\boxed{
\text{Identity Phase Transition}
}
\]

從比喻變成可測量對象。

---

# 三十五、跨領域 dataset

可以建立：

\[
\boxed{
\text{Continuity Object Dataset}
}
\]

包含：

### House
養子、旁系、主分家與斷嗣案例。

### State
國家更名、分裂、合併、革命與政府更替。

### Firm
併購、重組、破產重生、品牌延續。

### Religion
職位與教團繼承。

### AI
Model Swap、Memory Swap、Fork、Migration。

每一案例標記：

\[
\mathbf C_X
\]

以及不同觀察者的：

\[
I_X.
\]

---

# 三十六、理論的最小反駁條件

COT 如果只是說：

> 很多因素都重要。

那就沒有價值。

因此至少需要以下可反駁條件：

第一，如果所有身份判定都可以由單一維度穩定預測，COT 的多維主張失敗。

第二，如果 gradual 與 abrupt replacement 在控制終態後沒有任何判定差異，路徑依賴命題受到削弱。

第三，如果法律、敘事與關係承認完全不影響任何制度身份判定，\(\mathcal N_X,\mathcal R_X\) 應刪除。

第四，如果 AI 身份總能被模型 hash 唯一決定，其餘 Agent 連續性變量便不必要。

第五，如果責任總能與身份完全解耦，\(c_Q\) 就不應被列入制度人格核心。

---

# 三十七、與終極本體論保持距離

COT 並不回答：

> 靈魂存在嗎？

也不回答：

> 世界上是否存在真正不可分割的自我？

本文只處理：

\[
\boxed{
\text{operational identity continuity}.
}
\]

也就是：

> 在哲學分析、制度、法律、社會認知與工程系統中，人們如何實際判定身份是否持續？

因此它是一套：

\[
\boxed{
\text{identity methodology}
}
\]

而不是本體論終局答案。

---

# 三十八、從日本悖論到 COT 的理論路徑

整條研究線可以寫成：

\[
\boxed{
\text{Effective Space}
\rightarrow
\text{Political Nodes}
\rightarrow
\text{House Persistence}
\rightarrow
\text{Blood/House Legitimacy}
\rightarrow
\text{Narrative Field}
\rightarrow
\text{Continuity Object Theory}
}
\]

日本只是提供了一個特別清楚的歷史入口：

- 地方節點可以跨代；
- 家主可以替換；
- 血統可以部分斷裂；
- 養子可以被吸收；
- 主家與分家仍具有不同中心性；
- 社會共同承認決定「這仍是不是那一家」。

當這些問題被抽象化後，它自然超出日本史。

---

# 三十九、COT 的工程版最小規格

若未來要把 COT 實作成 AI Identity Protocol，可以至少保存：

```text
Entity_ID
Entity_Type
Parent_ID / Fork_Origin
Model_Provenance
Memory_Provenance
Identity_Key
Long_Term_Commitments
Relationship_State
Policy_State
Responsibility_Ledger
Migration_History
Fork_History
Recognition_State
```

每次重大轉移生成：

```text
Continuity_Event
```

並計算：

\[
\mathbf C_A(t,t+1).
\]

若：

\[
I_A<\theta_A,
\]

則必須標記：

```text
Identity discontinuity
```

或：

```text
Successor entity
```

而不是默認同一 Agent。

---

# 四十、結論

連續性對象理論的核心可以濃縮成四句：

\[
\boxed{
\text{存在可以改變，而仍然持續。}
}
\]

\[
\boxed{
\text{持續需要的是關鍵連續性，而不是全部不變。}
}
\]

\[
\boxed{
\text{不同存在擁有不同的關鍵連續性集合。}
}
\]

\[
\boxed{
\text{身份不只是一個物理問題，也是因果、制度、關係、敘事與責任問題。}
}
\]

因此：

\[
\text{House}
\]

不是某條純血線。

\[
\text{State}
\]

不是某一屆政府。

\[
\text{Firm}
\]

不是某一批員工。

\[
\text{AI Agent}
\]

也未必等於某一版模型。

真正的問題是：

\[
\boxed{
\text{哪些連續性共同使這段歷史仍被判定為「同一存在的歷史」？}
}
\]

這就是：

\[
\boxed{
\text{Continuity Object Theory}.
}
\]

---

## 初版文獻接口

本稿 v0.1 延續前五篇已核對過的下列研究線：

1. Ship of Theseus 與相對身份／持續性哲學；
2. House Society / société à maison；
3. 國際法中的 state continuity 與 state succession；
4. 公司與制度人格；
5. higher-order beliefs、common knowledge 與敘事正統場；
6. 2026 年 AI Agent identity、persistent memory、provenance 與 reputation continuity 研究。

---

## 版本註記

本輪新的外部文獻檢索服務失敗，因此 v0.1 的任務限定為「統合前五篇已核對理論材料」，不新增未核對歷史斷言。

v0.2 應重新進行外部查核並完成：

1. COT 與 psychological continuity theory 的正式比較；
2. COT 與 four-dimensionalism / perdurantism 的差異；
3. COT 與 relative identity 的差異；
4. state continuity 判例資料庫；
5. corporate continuity / successor liability 比較；
6. House succession dataset；
7. AI identity protocol 與 cryptographic provenance 文獻；
8. Identity Vector 實驗設計；
9. Branching Identity 的形式邏輯；
10. Responsibility Continuity 的法律與工程模型。
